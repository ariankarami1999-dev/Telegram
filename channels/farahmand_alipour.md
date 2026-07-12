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
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 14:35:32</div>
<hr>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA5T_yyIkebjp6zSipKKrT8OrtsARS3Y5P5UQqsXqZQdiUYxeR5CtUu4thRTL4RJ-PpZUXPH3oi8t6WGaL-o__k5KAk239Sr0cRS6N_A67wz6CQ5QLuiAjyPYhVquaCpI0jScD77iIHFbv9B_f19iIke7L69Av_aIm146MFGdq52s_q_efk0ScjO2Zk2xwj3DNqbtKKta8irIdWWL6M4hCSOhQU-zAjFdJs3BBXbdqqxV9bEAQREoyv1L_ivy_3mXJnTz5pIuw1ToIt6VGyo9tb16ruMYyJGFeginwdJO4UumNet8L70YdScmwGYToczalz-bJBTIWKZtGIlXg1H7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b23JA1V-CUObD6TwsH0RRZ5uUMT3GPFPlu8-Ear75DGj3Dify3JlWq8Pl8-QxvZXuUgcw0tQb-3Hjt8QDWru6E6a-YCBxcDtcSptuUZWy8I5yHtbAWx5m6cRcP2WXFd35rF3YAZ2jw1fIwR11r8q_iZ1FbVInjo3zu12LOhg6uQqFHka6XRpBEB2BNC86F7q-1MCzjuqTeBHf94Ui8gTdFXCzs9R4KUBPeV4fQU0FnYyv1JQheOE4zzsFokjQ3_-rWVB4UagcPau8qToGGQ1SOKEfDbnAm_kZ6huOR424klAvZAD5pN2yjmCbJu2AshOo03ovnPRIKhYmCehAAI32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmu9B_s9vTvyGj2zrTe2Se3chjW2pVp_c2Bn-1El-QP9_jMVDGuE8_juGijtDpMgRtXTEQnvMhxqeCIt2l-5hb5cq5AwyewDBxzvb1uqXXDBbmKBkSxT7-Pu4ApO654kjS1l8LwE2_d0RGI4Y47P35pSif4QVhBQlK7Tfy3ApU0b7jtfRRcD2X8nfBk8rmssW4K96l51gzutnV3p3QnINZEIsDH6eP0ZEpnMUEDm-h85JtuCMMxclxDhNWztnwbXFB_9vSJQc_QPt2iqGkwzsP2TkW-EESCrmodrHUzBt0WQqiUEs93kL8FOaJD-GwGEoiYlKhvvtkuKirTpS-JJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=Qad0vGOcXyeOku4YRkwYrnP3kltyQPa9jQRtOZjjFjvUXa5zagyThxzrRA8ucl_P4tK5UNxyO6Fo6eIIPDPt_v6Q_O0jXbz77n0WE1BMstF8zS8oNOLLLjs7O1OG01OlpNri7Fg9a-ArjU9e541GgXQ3XDgemTIsOQKNka17c6HBsNbDHPOw-tZM2boq2EuuMTWnggBxiYyp3Xe60eJ9oounvhNIvDud12i8mLjRYwHhFJWroaVV1vaJoK8vSGjobunXd415Yl8GJ57uNEFDCUnRvumA3VuFWj2jS5CyWoznhSlJ4dYC6QweiJrmeK8KDHRO2FFBjsMlhpFpir7Qvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=Qad0vGOcXyeOku4YRkwYrnP3kltyQPa9jQRtOZjjFjvUXa5zagyThxzrRA8ucl_P4tK5UNxyO6Fo6eIIPDPt_v6Q_O0jXbz77n0WE1BMstF8zS8oNOLLLjs7O1OG01OlpNri7Fg9a-ArjU9e541GgXQ3XDgemTIsOQKNka17c6HBsNbDHPOw-tZM2boq2EuuMTWnggBxiYyp3Xe60eJ9oounvhNIvDud12i8mLjRYwHhFJWroaVV1vaJoK8vSGjobunXd415Yl8GJ57uNEFDCUnRvumA3VuFWj2jS5CyWoznhSlJ4dYC6QweiJrmeK8KDHRO2FFBjsMlhpFpir7Qvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqcbaT3oLtfoTtA-ossrFzlswUQWFSuyWLjoUbmycqkrCFNBbV1-UCIg4Z9MBnexn0JezGXyvQCGoXpv7OSgI8F5-s0X3GLEEY0_z0xQeyeX5_eqh3gj4D43Lro14OSqCXu_xxv9Q30ixLjjp4J1oZIdvTDgH0kTepNtBgcwIYVKTcwwlTrQWsW58Fo6d2jZlaSACs1hUp_ID0VxPIyzGy_nB8Nc8JQy_EFQhAdWQJsc4nWgW5Br941HBqdc6dyR_c5QjspyTvHH4c4rySCYWnF8EkX8JTiZioAuBOOAvIUM3EI8ym5kHzSw38jvzHBRaY39Iq7ISBSCbnabpVUd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sDYq-guyRSP6Lt4S1FsZ7_nt9rRZMUuzjvo2SvyEcR8hAXUL8MHCINtkycC4erJ-hRK_0sqfl2uDop_6Aoi5BTVMS1wfm2xmWkpTADWHD3kuuWQylDoC3bUngVHLSk87hPY35tgMFKKLFKgOAD7S8RzCk_adtcUgPDE0a4EFBnhCXaESoNlBa-UetENeTdVFxO3idNMWZ7aPbJJosJK1rcXb9erI8Pnc7DFaQEcC_PsGV33HmgDXJILyvu7CuFsVHAXs7aLqZ5VLn5zvhE3He9nE5j4jdmi6DowjrPqRw-Z2dhPMPc7nmLLk-04yvnJzjfMtWM6KlSOuBVKTd9N3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sDYq-guyRSP6Lt4S1FsZ7_nt9rRZMUuzjvo2SvyEcR8hAXUL8MHCINtkycC4erJ-hRK_0sqfl2uDop_6Aoi5BTVMS1wfm2xmWkpTADWHD3kuuWQylDoC3bUngVHLSk87hPY35tgMFKKLFKgOAD7S8RzCk_adtcUgPDE0a4EFBnhCXaESoNlBa-UetENeTdVFxO3idNMWZ7aPbJJosJK1rcXb9erI8Pnc7DFaQEcC_PsGV33HmgDXJILyvu7CuFsVHAXs7aLqZ5VLn5zvhE3He9nE5j4jdmi6DowjrPqRw-Z2dhPMPc7nmLLk-04yvnJzjfMtWM6KlSOuBVKTd9N3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcNfqSEc4-7V-aSJphiLkhDawdrobgrfWrFD9leF53kyhKWzexu9Hgw0A0uI_dKm9IWB-6NLz3BCLcwcUlucqlP8ViSVSHYaB4to1O9jF8Ho0pBrSjqxu30L8zgrQvHFvdlnKXS1WCBOAFU_fw-Umf0yMAxX-IiAFWuNiVEf9SF5jJtpXYQ5bXe1M4ZVM6VCxQR8vZYB6eFvpPaLIAUkUcBxRrwn81xwTimGfzE9Bi5JfYKWsKIEVSbEVm2HPxjer4Gpwphg9xswjZsJRiEX1GPmtEGPN3F_oeUg8flzvDRI1U4llkMg8LlRsi0yUeS65NLcwBE5kFtHowQ6caYdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPnXgcmOINPTZcxqP_n-GWXenVZgiR-YwaMkgLKaa-fc5toOllleTlhy4n2Nv7nQPc3CX73w3g19GfSnU2Aqv1g23jZqTOpJVB4ZESpVkPqkakkZiW2AN0rlmUs9virUkDbYwe8_uda7ZJf8n3AhaOZWY172MNfEnDdjYNW3vdtkxCbK_1o5u1mqghjUaW-_RkuzUKsDPYJ_UDRYD4uAj_JvkqDbUYJjq6E4T1uI8AYTjv0rnI9sLQgieijEAOR_BhM40RHBYUJeiXxLBdqvdxp--6d5LxBjRnjhr83JJ76s3gakcNNVS3FJiy7x-KAUIRVRFPCC037wkwpBbfRN-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=qPhpUmXLs1zzKAdtE-ZWZbPeFz00e64vGShVclOsxn5YsdbMBJEissdJa24bzFC_mK04iOJtRwLRZcIaF1HYYekrpyS6t_qVpuGeh857eonfZVcmjS0qSgev4HfkiWRefllN2BSfDEC6b9fUwY580M1scBK62bzeh7GOPRhDXgKFYfVS54dN9ygIMxcb_Xyei-SYMenQPg9GVORfexupDThqxYyFqYfmmUH9Q1PZvMRV0Aeb08Bt2bxnKZhCo6oSyyI6lwhYQT1_Onoq5QGc2LBvyEiKCthN5qAOiqroDPxUBDTde81zXY2R8x_XIMCqCFuakUwp1sDJ2glOIHwI1Q4aKMoqbb8T_KG0FhOm0vHHxP5An69I3FbVg0qxykuz-QtRmKQacTh-qsSgrcUuSPnOYgvt6qWzRtp9-MbgUzoymEURBYQIMUnVuAsoJ8HvV4lGLDg-ef3QW5ulaxT7q5wrxq_0oSyt0ZQbh4C41rdbk6AA8wWm4oD-wtn_VAmQ8wAPIt3UOSNJWKR5am6lV7fWytg4BONwEcHaV_ZPS3cf_D7lpV50xnFfuAXfOF9bPlWvhjLfntiQ9_RsgzlVVbP9gC3iFns30SEJ8-d8qfdksJFo0twLIg70lMuLYKc2m2jdICSKrZceTIRDrsqEZcJAiFE2v7vDkNzr4egfdOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=qPhpUmXLs1zzKAdtE-ZWZbPeFz00e64vGShVclOsxn5YsdbMBJEissdJa24bzFC_mK04iOJtRwLRZcIaF1HYYekrpyS6t_qVpuGeh857eonfZVcmjS0qSgev4HfkiWRefllN2BSfDEC6b9fUwY580M1scBK62bzeh7GOPRhDXgKFYfVS54dN9ygIMxcb_Xyei-SYMenQPg9GVORfexupDThqxYyFqYfmmUH9Q1PZvMRV0Aeb08Bt2bxnKZhCo6oSyyI6lwhYQT1_Onoq5QGc2LBvyEiKCthN5qAOiqroDPxUBDTde81zXY2R8x_XIMCqCFuakUwp1sDJ2glOIHwI1Q4aKMoqbb8T_KG0FhOm0vHHxP5An69I3FbVg0qxykuz-QtRmKQacTh-qsSgrcUuSPnOYgvt6qWzRtp9-MbgUzoymEURBYQIMUnVuAsoJ8HvV4lGLDg-ef3QW5ulaxT7q5wrxq_0oSyt0ZQbh4C41rdbk6AA8wWm4oD-wtn_VAmQ8wAPIt3UOSNJWKR5am6lV7fWytg4BONwEcHaV_ZPS3cf_D7lpV50xnFfuAXfOF9bPlWvhjLfntiQ9_RsgzlVVbP9gC3iFns30SEJ8-d8qfdksJFo0twLIg70lMuLYKc2m2jdICSKrZceTIRDrsqEZcJAiFE2v7vDkNzr4egfdOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhzZXVoPhOySbDI4oF8HPd-ss6lAjw0lZJk1rzF6MWAeE0ujNAko_IMdH380ywir86YXpE03mX2zayhJjADeekp8IzUb4ITGyrnTJoNksSFMl9qdtZwo5uURwFs-Ezm4_HV2x138RTvRuxxdsLfRociH77TuKVbAvEZokuJlQmRIt1VtIlr5u4p7GpUbQ9h5OGBKdUo7lBev_ZrJQ4uK8edwlb8y00XaXxC6N_3-qxk_vxonEyMht0k3Iwe4bfVRZN99Zb4XKCqdfIaPcqxtYFvzTHJcP_hVJIO62PKLi8M7Q8Bqg8r1hZEdreS90cKWV2IVC3pjAIdhKq50rwFk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_w9eUUMFEqcVgZUi64qso7j194MV93V294356t97mqKfmUDqYvnDlH-iz54cRHCrvb0LrjZz_YJqE0TNvDVy7Rof2JckwQ0hZxwkslEzxgyWjyWU6u_575MfR0Wq6uoj6JmHUMPF6PqMFVhKFQumCbl4JRoN3fZ17CDg54mQfM6swg76tMHyEzHsCk6X3_6hR3GJuuPJHi04jnJcnhujIfLXIoXRUyaKTbc_-Gczdqjiz5XD0Oyq5hqUqrlilOusJ59e9gJrncx6YGeUODDD_0NIiACaq6Gb2KJiv6Csu_xmxy-Nt2wW7FuJKx4iwjseuSI7i1qDug1QZoQ2wREUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HOzwhPBGvw4giJobbkMUzIrrBIukXWqeFGuYYrJyUXqsKnQaaYX8Gkzrx1JlhDPoyFOLmAMaZqEBPn4QTKB31j1k_Lvi9OefATMFE0ZrArqsdu22Xj-ghpzhbzPlRMBNjK0VsovPzUVQYjbVlZcjP8OnEulpTASTcbNlyZl2xhOg872jinNiYXl8WLJPSRBd7W6c5rvm-n0c28zF-N9F48hBkre5-5hK03uaTu_i-Ctb5vPw-1VDPv2OSsbccVJh-n1XPh_IDjRn0gblgLeaK91jKZogXMrJuNADQjO92JmYIdM6GRIpKPn7G5MjYaF4kzsOv4oOD4UwbLThevi8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HOzwhPBGvw4giJobbkMUzIrrBIukXWqeFGuYYrJyUXqsKnQaaYX8Gkzrx1JlhDPoyFOLmAMaZqEBPn4QTKB31j1k_Lvi9OefATMFE0ZrArqsdu22Xj-ghpzhbzPlRMBNjK0VsovPzUVQYjbVlZcjP8OnEulpTASTcbNlyZl2xhOg872jinNiYXl8WLJPSRBd7W6c5rvm-n0c28zF-N9F48hBkre5-5hK03uaTu_i-Ctb5vPw-1VDPv2OSsbccVJh-n1XPh_IDjRn0gblgLeaK91jKZogXMrJuNADQjO92JmYIdM6GRIpKPn7G5MjYaF4kzsOv4oOD4UwbLThevi8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6g13iRLpAiDjPj_wChLK3NyPiuZ3kOVq1rkcXV3FQQa74nq2jSET8MKs2n87Q-pJHKyBEgComSyOInB49i-HL6CCY2hRM3na72kRF6-2CVUwjXwH0eZE7tKOrlWhwER0Uy5jAnATQrJ6n5NvT22cGCpTgKzXHcFPCTIKvDf0rqyTdkVU79Kg7FIXP1CMpUDITvfpc_flk0u73MDA9fZ6QQkKmUn40SUzSvOFRKMKYl_iy4Y7zf-PH-awVyZ2KLKhZy1XN5JxafLSqnKEE1yECFxnxXesipQnLJKZ8wEaC15hyuxSyG86YBVX-Ram2ZFep75Kqc4HC8vVtrv9cz9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAvZ352S4sjVmtPILDOZfPg4xbOf3JPnD7WhD2QbZLT6lT9meFBWNMmUgzio1zZs7QBI9ArG6nHM7tKRQY8mgHxL6FvHDo98r9seIitW4MaiKPKoOpmxJGowBQC721j5St7OBdJYD9buNPO1LmK4BA7mKOIDGdVkyzuqnVK9lHYQ9HscG4bLLTTKT2_ADuSrNyoEDWneDGx2FrUaJgmvbDoVwo5Ioi7xqbJ41HAgVK_c41NvR8jaTaqJ_LdcloHBl09mbt2tUBXPJxZPh-A-TCtE8FvHVPjc29GHGeVVkjOTErZo9h5TO6aVSNSz4SATSmbeeLKjcvU_ms14xvSiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx7pmtulSgtu9J76_H2v6HiNMK68daeG_yVJ4lGfQVqj7fIvK_GC9I6vOhj6V2XIf6L08Zq5QSWhoDN0Mva8iHQ-HKb1nVZEcZRbYmlL7UIFaI_QL4AfGckveglwLBlZy_wfbbH14XYcgaVVehwQ1WDV11S4nTV2IVgsxPU3_czqqgKoV_ah2aUVbTnNhJpps1L75WSPKwgP-2eJD0pbmexu1lJRSbCc6ojt5NTl59MPAUnNa4D-A-w5-gj3KgeJAjoijgs9UI3hwfFDsz33XAW-pv3Fr88if31yGP9H1NK9KORGNF43WVklfAMpqgeqei16ZO13xwICmWRGdohMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg0Kt9_H0t4it9KVKebWdgc7pftDSlyhc37tB-PZ6wzy9wGul8I9fbccTFaJyJQWELKI3m8VYRMn8P0e9vK0Xsf6kHurFgMGNdOkD5KdhmU8TB1QTBRwQ9FTEUijrrAYN0Zta0H4zy7mfgduXW5Z2cXzw8Z2QQelCKGCuDRdM8No2xFTG92Gs7Xcut1-KJD4HbQcro4lYL2Trl3EZiUPmZGOBdX2MzXvF3WIUiFacpGtLUZfIzBNpk4enuowz2GricJtGvgzHwRaKqbCH1iYKcoW9To5hAJ1edhMKKyvnmr6pRyUeBqnBjBc0xbstq_qIMm3zt_MfJd0dNhbp3Pv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHSOw2p_g7Fox9OZJrMArNiLrHBrteI841VOhGVj3hD-FirC_TTXNg_WTUIxGOIQubtpAUz-ppitpCQzu3ocAnCo9pG2IBWQyLncyNuukXQwJILSdBUW_EpNkzPhjiYZG9PyxHgO869qbL2TBHPg4WwT0DnMXm8DHdxVBM3Lc-rjGv5tZeL877w8yXz_xuYVl1jSpnpfnyhngrVTz2vafLRK4_Z0ITVkN4JUhyyzAlsqgSPM_iia-7YbSuw02n8wjHY4xOQEr30ed0LVOv_XrPHY50pKd4pewdeITB43GZo4yn4jMPSyc49EUnDpsyF6GiOPXuyRwNs4yrIpo3dp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGgnc9Q5cyDwU15NNc_JECdZ6BlTX5Td7z0LJstJLW4_ziqNtu4Vf-PxDl67N_wrdZ7LQH5DKz0ILAS_25bkZCZ2OZ0beLQkJnZozZIib-fnSwOK8ilvmXSzTBBiFpn76VdN-b9100udrcCqUZD3vKfLF7tz0_AfuGcLBYQD8sjxnv2kniL8arKg7-xShmw77ptGnxnuL8HLK_-F4REb8jLm4yJTGQQZUx45T04qcfyo9khxl0Gjmd8alK0mFEs33iR2LnfgiNt_DFcDLjUobg4HM1pPv4XkyeB6ZGppjqSP01SYcIUz1usoMJZmNvVN2wgKLnv73NW7VmZL38Hd0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odreLMC1quaHYaRy52lC5jd-2E9B7tmPw6ewpAH_1ufRWOhOzTFdWzbz8_tZvgF15o9TWi_xrUIln_33IGIWn6yLEOZoy7V41j18vdvwuzT-v3ecO83_WwNx_ztFENeJ6lLRkZ2_IIA2DkqwhjHrIhQcJNvdI8KkIpg3b-07bEc3HB4bgZEQknu-gAngyz-RdOAw3221M0u0noYkuJrsVb1iokFG5F0N5xCyRPRQx7-8wcjYVQ11G3QlE1ABqMm15UL3spcgiXcbGhkPWbPH17RKXBmI1_PhZ-oGRSuq28qxjISSCHdOUZBua8PWgumCkXC_tnbAIJpFQWAdkMwhUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScKjG1J7G1SJYgIuu0HIV9IRHLPV-HN_KlOyvk8_vQ73Fm0qa-BMLCqTFEl_-tX3w5gWgstAk0gfZuZIs3zxp2yAw8vGhCkB4OURgAQQAnN-WyR7t_31GNh2KUQba-6AzoMrGm9tCVi0w7JtAkuy1O_Vwf_kGW-HK3O4K4wQZY2gCysA6ej_0AX2n09SZWN4BJPL54rs_PQSzfrw-SAcU06-AvV_bxPo2DijAUPO_i_Pvdc5iAlVENVs1e5ZdSng9RvSTPaVAgiGuAqnoIm_Ke4JmXwMZsdu31XlRml9AmrNnHmANHCNH8hNcRnaOUjt0WHWHtMcaKRKBaxZlKxcag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=ROCHg4Rtx2hevlIYkMrYsoPnAn_U8GVLrgJSSEWWPsNDwCUZOEme_ZRiSd5eBdjPac5sj41WdWsNgmI599Oe6VY_NuP7KQg1NFw3qdzbBSAmtFxLsc9sbVnIVFiVCktHQHMZP_yyHERguoe23IVkulhew4vaCegTSu6kEl-92Dkufs6mp_yNPT6S-F6O-pN-D5rKYTkDbK2mKVF4b8yHQIfllRpC6lTN1xXQrys1De5ojuEzwJ--i6jE5KvyMYe7Q5GK7LsuKHOgeJ07eOyvuFcjgC6o4O37LodbGj71x-TyNy0CwzY0gKEdPl446Tzzgtjy2Rpebwcra7D2a4WJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=ROCHg4Rtx2hevlIYkMrYsoPnAn_U8GVLrgJSSEWWPsNDwCUZOEme_ZRiSd5eBdjPac5sj41WdWsNgmI599Oe6VY_NuP7KQg1NFw3qdzbBSAmtFxLsc9sbVnIVFiVCktHQHMZP_yyHERguoe23IVkulhew4vaCegTSu6kEl-92Dkufs6mp_yNPT6S-F6O-pN-D5rKYTkDbK2mKVF4b8yHQIfllRpC6lTN1xXQrys1De5ojuEzwJ--i6jE5KvyMYe7Q5GK7LsuKHOgeJ07eOyvuFcjgC6o4O37LodbGj71x-TyNy0CwzY0gKEdPl446Tzzgtjy2Rpebwcra7D2a4WJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mcjQ_9Vh2PYu8wzJcSTgXLtEDMQjLfJmCc4e9QuekLSsB6vgA_4p6PO72fVtWLAdCEhV-7XQFcC5tDEo4mn771VEamZqHdvis_5MxaZdDAkMiE-fSBLfHSQB9aRMayRCa2HFoECYu7oQuLl9tHGFmF5Rz1mV6nO-apPxUhJ3tNsnjCHFc550OBKndj3OB0Gb19tegVgF9DNY7Jwh1B-VDLPuL71CTxuVuhg7c9A0yB3gsMpVzd6yAS_MKsZqkMA1ErSJ-ZzsTtBo9xIG4Dxb0h2Gd9xb5ufCPYSyYpZDCPA-P2Ele8QMokxnDD49o9KcGIXbjqAyKDsTh6DDLzFQRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mcjQ_9Vh2PYu8wzJcSTgXLtEDMQjLfJmCc4e9QuekLSsB6vgA_4p6PO72fVtWLAdCEhV-7XQFcC5tDEo4mn771VEamZqHdvis_5MxaZdDAkMiE-fSBLfHSQB9aRMayRCa2HFoECYu7oQuLl9tHGFmF5Rz1mV6nO-apPxUhJ3tNsnjCHFc550OBKndj3OB0Gb19tegVgF9DNY7Jwh1B-VDLPuL71CTxuVuhg7c9A0yB3gsMpVzd6yAS_MKsZqkMA1ErSJ-ZzsTtBo9xIG4Dxb0h2Gd9xb5ufCPYSyYpZDCPA-P2Ele8QMokxnDD49o9KcGIXbjqAyKDsTh6DDLzFQRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPBAb_AOQwnVvbnJPt-i7zVGvwRfpA9X7pX4HS5jQf0eaU-LCecSNZxZeIIVc5l-TdOU61Vu9uKVM3LrH39u4bjxjCq_am3oT49BeP-XOLXSig_scq5nMnAzizpVHAs3Gq7ab-h5XbB1jXRAmjdblJT_WItqrx3lzCvbCHmc7_gNuHkvyu5f5x5Ayz09ZTq-yGAmIkI6kS8Ym6VxixKy22nGfYQyH_1rzcGoD1eew1yjSWM4fh0Q8RuTVbgW9uXMLpQfNuMjUEPjvL459F8w44XQu-PGZmphKPhEKw8uf5WFqoCR-f-lQL9XwwuJwKwK53PSx-pWJgbBFZfeLt7FNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJG4F_LyhRKJmsajv1HX4H3RxWKl14cFi_K8lTm7bL8faBPDTH0SNDZcXgU0z3F9MQ4dXi6AUs7UvTrhHi740FH13oYibGd6dUBYVubqRCITuNFicpQoKukIR5EACCuzH2mxBv0eGMlMjsYlFLgvgu7_2ExRp5PwCN-h2e-8AUaXFn7gtfKyW6Ko37_05IogW9Z9sM60_ZT5nTKLUAsZiT5DV7XDgjDJoDV04Rx0iZXynOAR6Y2MtozlBtXTb_kyvhUCiOdBwkWeGxgQeyBUE59g-tQy080IlTj4wS_NRDxbH97NkXfSTkOlOUZLVxcerzVcixcWGkjLrxFtaiMfBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-ito4rR8oVizISz5sHadvBdKe-Pd5xlUtpLAipfoSJvmgZFvamw6G-RPWIgGUTzSOrG0w0pUp328siTRbJuuUKEspVZEFsQiehfyHxuI6I-LF25CmcxANW54KlbABHXIhRK3GysBOBDXTrxb6d3xmsznL-0m6XRV30WCKRCqr2X4OEK0SqJkPw5BV9sAR4JXzvz4FSaYOt_Hujw8QnzDznW5OM4xaBnOkgTkgKjbZ1GwjcAKY2yl2saKda-NNbIUOlJ1UNrqFjm-d-WoR_uaQMXfsS4Es7kiKR1QVkxbvcSPXj9nBg-1vllvUKFs2TXGvFHcszRX1UzxUZ1baofZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lXqNCynKaZxP3NR9k5SeE_DumtWZv63PkiE2-d_sCWX5ttHZbWDdCZB-kcthfeHB_5pLMd-Ls8ETTSP0ZEIQ_-gprsfyC8bBxJXEDx2YJ6OxDom8CfUWy1_QBMMyVMcqyTy2P0-kRYu0AyYm2_Tg5GDwQyVqaKND7a70wmTBFJ_PF5igwZWO6sgFuydTAw6XFLYxewlbyJnBwEh9lQFXbbSP_XrruT_U78ZJNAnVl-RTTVRWJV6CZqVVsQ00vfEVgqyYvC2grs08vfzklUiO0MbcTIUgaUklstBGtzwJL8jMCMFRJmQ54wV4nhuVbf_MKEaYBTr1GsKHkFUpggft8kM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lXqNCynKaZxP3NR9k5SeE_DumtWZv63PkiE2-d_sCWX5ttHZbWDdCZB-kcthfeHB_5pLMd-Ls8ETTSP0ZEIQ_-gprsfyC8bBxJXEDx2YJ6OxDom8CfUWy1_QBMMyVMcqyTy2P0-kRYu0AyYm2_Tg5GDwQyVqaKND7a70wmTBFJ_PF5igwZWO6sgFuydTAw6XFLYxewlbyJnBwEh9lQFXbbSP_XrruT_U78ZJNAnVl-RTTVRWJV6CZqVVsQ00vfEVgqyYvC2grs08vfzklUiO0MbcTIUgaUklstBGtzwJL8jMCMFRJmQ54wV4nhuVbf_MKEaYBTr1GsKHkFUpggft8kM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=AXZ32tq17Iz8jq91ilgQXX4E9eTrz9v_WmJimYBcH86Zwi9Cz8CYDrwJ23cg5-QnoavpN-89FU_MioeZob73sWTmrg-ZdFOoJO7astTd7XCjEKd8335XfrPDD87L5dqzwvnYWg_jGcq2FK0slEhUCFrXvKYl0BXA8Du2lTNLNl8WWqbJG-7d_tHQKLJ2WV16IBciCj83SQhseNREa42Ocths1cc7TBbQtorWsYpRCBS1hZVe3ypmoXMQr1TbT7M8sgXyCgbIZcvBs0g-tJgQk8I-dhC9Gy8ytVRjWACzknbvoovHv6mJVGs2filvyHotNLeaigwwWygGnhMEwie4MycqqLVqdhQzgcIQSSrBbdNG8Q6QF7lSZbH3jGItuNkqpEfGlRRsinktJE6XiX6vP808iprQQc_VnqUpV5iIvFuhEumm1ea-hQ8nhefnlDBl8b00y_nSTXyCMkyEyMpbPoZK3gUcyAf5IfpMeoxKlE4sCgwcxMRF4bkSsgJvSDUMANfZ3-Aq9sqhi2XciAo56ISSTObzrgtvNUR-smFXbFJIj3B2jwikGZr-JpEEdCJrMDFRVEbS01Jm9CBixYyHaJqc_bViFpkb2XBL9qpCPaQ5shuKrLHqpSOeHhN3IfkYJWa62z8XDAhc1mFGYIb7gvFhKWItt3YbJ7hU-Kxozr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=AXZ32tq17Iz8jq91ilgQXX4E9eTrz9v_WmJimYBcH86Zwi9Cz8CYDrwJ23cg5-QnoavpN-89FU_MioeZob73sWTmrg-ZdFOoJO7astTd7XCjEKd8335XfrPDD87L5dqzwvnYWg_jGcq2FK0slEhUCFrXvKYl0BXA8Du2lTNLNl8WWqbJG-7d_tHQKLJ2WV16IBciCj83SQhseNREa42Ocths1cc7TBbQtorWsYpRCBS1hZVe3ypmoXMQr1TbT7M8sgXyCgbIZcvBs0g-tJgQk8I-dhC9Gy8ytVRjWACzknbvoovHv6mJVGs2filvyHotNLeaigwwWygGnhMEwie4MycqqLVqdhQzgcIQSSrBbdNG8Q6QF7lSZbH3jGItuNkqpEfGlRRsinktJE6XiX6vP808iprQQc_VnqUpV5iIvFuhEumm1ea-hQ8nhefnlDBl8b00y_nSTXyCMkyEyMpbPoZK3gUcyAf5IfpMeoxKlE4sCgwcxMRF4bkSsgJvSDUMANfZ3-Aq9sqhi2XciAo56ISSTObzrgtvNUR-smFXbFJIj3B2jwikGZr-JpEEdCJrMDFRVEbS01Jm9CBixYyHaJqc_bViFpkb2XBL9qpCPaQ5shuKrLHqpSOeHhN3IfkYJWa62z8XDAhc1mFGYIb7gvFhKWItt3YbJ7hU-Kxozr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDUq1QLzJtjin1VCN5NkaJoudV6ol_c3u8CpDj-kOoxy3Qp0pC5S-5I4M5gSVl9fH7JmElWvnd1mbOZ0sKlUgtML4K1UmM5ZOZvPTmDRukm4Hu5S8lNoRGAfFxfqFZwCuv_Km0fFRxTOXYz4mI5EAJ2XI533EjjKXq6H59ibYDcqOiGSsMH--qUNm5tVptr6Cg-U6xK8bkUfFlqb4Z8YV05RMMBaYOz7doSIP9be7hKgu6xZzspLRGiPmibGq2dzoUam2Ht3CnHtrTOfDEfQywFPkC8-EZzQxpUd3hqEmMW_yywcxKfS1KW387vyAdsONSUcz36Nig8I4gG0p0styQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyIKkBL1lPeE9_mv8njkn18wXnI9dIj1FG2IVmT5T8DRLO1mGt53KjftNp_zjLoI529s8rtgp_TmfzsQe-sb85DM7CzST5-3_G7fa8Dt83P_J9lz5ccOTA43Ynb6_rd4iYhT6Cg-0XVLuAhyy9T6sjgmW1hn20Ax8X4hK3PNfKT_kstZW1pxZX25iys7AjfMRzNk0vMUPmjnuayoW0CEMiRsa59c0hFAcBui8MuM3hFBsT-_JVEqtx5c-SeKtVmAH8sT7jvVZ2ufgTqa75obLgnQXPPTrlu_yLqq2bB4akuT19xtHfVTIr85nsw_ksMzIr5AODO6golnQ285_1qixQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1tfKc6s1wKmWhpMM8tviGzBLtzuluSWkrtUQ7fKdxWpf1hHXKuA8tpPk1Ikc9ygZHizRAxKgzhmDzmmBM820ULgny3_e_nVwMb2u_vNUX4v8Ss-gITQiq1Qv77SdBMvw0TLndyd_K8W1pPum8PeagCzS71A9Im935cj8feAJvGOr9nZXnVQytyU_H2y2CbFgwiIqDDEj67BiEYD5nBFa3kkDvsok-YSIxVIxl6H-9NvWcFfBxkvPgBuMshExbGltj_l9ecEljhiug3rT68p4vWk2c1JTW2VlWmG42-Hqe4ZdVlIC8TbXq5am1rPEuGR7bglpa4FuTdzzPbDUnZPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=lJ8J1nLyO9LQJoaprjAaQMfNE7H_STh7tP9MXr-rzNAl6iRR1U_SKuKkkCNNVt90DpVt63IZlaO7Xojw30Oq3GlVfPrI0VN178_IC5bkKxqT-V5XFwT0R55TGfigoMvW-otzlVDXWlfetlf6lV3YOtx4MQxQHAKROZIzUiKBusv8Wv09cbvlS6drfSki03O6outikZ7OhzIBhmwa0kxCYy2HeVp1bqxCM5FTBhgXAf5wi9cpU8MXAGr1ZUD3n87shwgApomIS7OLty-Zb3AOB9b1eHVBIw0gGcALqWurm0HYXpgpKCVidJVTecn_PIGjPm83gzPNGDJ0rGL1tk7wBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=lJ8J1nLyO9LQJoaprjAaQMfNE7H_STh7tP9MXr-rzNAl6iRR1U_SKuKkkCNNVt90DpVt63IZlaO7Xojw30Oq3GlVfPrI0VN178_IC5bkKxqT-V5XFwT0R55TGfigoMvW-otzlVDXWlfetlf6lV3YOtx4MQxQHAKROZIzUiKBusv8Wv09cbvlS6drfSki03O6outikZ7OhzIBhmwa0kxCYy2HeVp1bqxCM5FTBhgXAf5wi9cpU8MXAGr1ZUD3n87shwgApomIS7OLty-Zb3AOB9b1eHVBIw0gGcALqWurm0HYXpgpKCVidJVTecn_PIGjPm83gzPNGDJ0rGL1tk7wBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7PUP3a0Lpg1U7PrlnG85C-9KOoeFx5yPkE3SaFZZ0ZH5kgDUtd2Wx-wvlxFCu2fDKg_KiXuKO_LyDS1XvE-UQyL5A7Jp-R1aTjDERfNgoHrQun14S3MhhCcWCLFUzwp_PdjFwbpwUIcQrkEdQck2eU0saSeM9jOkpnIhowmChBtpRjIof9891NTt6MmhsLzBHJhNrq_92OyBzro0PtNoV_rqEPEggiYDp1t-1LD0rXCMzkPunZf_yMOCuRzxMuLIJbIryBPHXJ3AXAiA0Ohg_L9aiYwivr9E7WlT_FHiujP9CETUbtflIfTmd6ykCCZe90DUOjQenM5VBgQOxL0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=S15KqS-FSEVM_29W0oJ5p6X1PajS_IciXvSLcSvvq05L7IESopxvYxBzrDaa2nAKPdbBvb8RsFPdreZbfh6bWTq4bmUUSutjHikgHvo9SWYDyeXyWKm3VpGe8hJHWma08-ow9KRH7S6NFkjW_u3ZpN0FSnt64-9sGumsun7BxBJ7MQGb8qPneMwsVh_Z3d2dzFvVPd5q41EhP4sbzOf4SEsO4VTdkZcecFSg-XhA7GypnAe-28X4AiRsM6jvETEle8JhIhYG7qyyybNINhYcnRhaRsqb8Y4K9jjBqbYWkju-CtmWQ439X0ygqZghlKKTgWcv_Bi7uJZioSiu_BhJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=S15KqS-FSEVM_29W0oJ5p6X1PajS_IciXvSLcSvvq05L7IESopxvYxBzrDaa2nAKPdbBvb8RsFPdreZbfh6bWTq4bmUUSutjHikgHvo9SWYDyeXyWKm3VpGe8hJHWma08-ow9KRH7S6NFkjW_u3ZpN0FSnt64-9sGumsun7BxBJ7MQGb8qPneMwsVh_Z3d2dzFvVPd5q41EhP4sbzOf4SEsO4VTdkZcecFSg-XhA7GypnAe-28X4AiRsM6jvETEle8JhIhYG7qyyybNINhYcnRhaRsqb8Y4K9jjBqbYWkju-CtmWQ439X0ygqZghlKKTgWcv_Bi7uJZioSiu_BhJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlfJEzKwzO05R7ph5brW7dKH4a8XHGmDaIOzgNJcyhx3R6OMSMOK2UUYQ8d4dIiD6rb_AXMLHVwkxxu0eSyWR3b6Qn9yFN2lXR04rvOJwe4K_T3GibPTHUbKuwCOSqstF4-IAbDazFQBX9BW7yvJ7OuAkC1_23qeklBskcQGGK1xOyJwoFIXSK9LlWDJul7RdOE0MFHVFYZorsFqmmtgywE_H4a_2tSC8hBQEOh1i2xQIWNGA6efED5Zmad91BzWaoRZWxidzlOL-4aolTgV8SN5oaf2JcOt3S3bES587AUjBGvF6ZX9Jnpnxda2GJwH49DceibeaNMzVrGZhaIYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBZUk3c3Nm5P4ErY8Ci8SKZY53UtsVn01jzDL7k0PxCRj7iXsuJ_Z0TQAsSeRjdOxw8XyDLJYBg2gh4khm1NcfgxYN4g4Gg963iSIhsstIm_1MeG1IVCJAe2dcDIXOMPDcze1nXMYx3S9Bc8SwUUWp0DsVEhWhdF6QAx-hqBrYV762whCSO7G9ZDRKCaYjCIEhv7gsbInLGwsNLbwel1SQ56upBxCjE1p9QQzXXgNnBmRdNlkw48KNAo8FQhL3Z765cddQ1bGWyM-yCxiC_9HlYSX0cX066bsAsL7Ii3STFQF5gRkrU7l2WSXY_Dr__ugMff9c2xwoJ-yQ9yEuuOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=AR9sPCZhswNrIQ1IhFmrjexZmsJ8vwbhTrvWY-hq3hrQyXaysgGtzSlbvXNiuOqjcZgqqdWkrLTq09WHrwhMqBO34hLtp6Xj0NXxPEl6NKS2DKkm7ShHbPOAMy1ov7V6eiJSVaTxGsUuPYXa5uLx1BtK8WMMxr8x9XpXnufTlmOKKPrniTispVpCX54ZFLOCCqLtJfF5VXHI6OJobUGdgtwf-FzOvzVhuuushAQfGWSnxzunl4UkKmE3sCfR8Le7zCAVySCXUL6eu7qrb0NahC3JPNrseSlw495F6xg_DmTctOfFBxX-15leZO0E9dfEQWgAR7Wrt8x0oT5IOmQgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=AR9sPCZhswNrIQ1IhFmrjexZmsJ8vwbhTrvWY-hq3hrQyXaysgGtzSlbvXNiuOqjcZgqqdWkrLTq09WHrwhMqBO34hLtp6Xj0NXxPEl6NKS2DKkm7ShHbPOAMy1ov7V6eiJSVaTxGsUuPYXa5uLx1BtK8WMMxr8x9XpXnufTlmOKKPrniTispVpCX54ZFLOCCqLtJfF5VXHI6OJobUGdgtwf-FzOvzVhuuushAQfGWSnxzunl4UkKmE3sCfR8Le7zCAVySCXUL6eu7qrb0NahC3JPNrseSlw495F6xg_DmTctOfFBxX-15leZO0E9dfEQWgAR7Wrt8x0oT5IOmQgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=mQbjFSCPNtgsWdCMj2og3gbfbr6RRJS6VAn1w986nyRQ6Kx-05gDMFjkalgSnYARWlQM0AXxN3JxmlKGk6K93600UZBmKxv45vullng1xKu08FACQGU7sPrbw9ir3kFC1WKuq-jarvu8F2R4eB5iRxy3zk48NrU8j4UfBeILXvTqLEbN4UFcBbquFZhm75f9X6x-8liInKuRUU8G74dWoik54eQobfgDZeyeQ0W3bszWBL0Y-imZ4hXS6ItJrQGJxAkHcb8qye5ixFd1qe62-2dSO6UVlAdrHyDC0U7ldt20dG3QsDAv0nu8cDaUhH_R2SNaMEceQTc77lNtt-F8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=mQbjFSCPNtgsWdCMj2og3gbfbr6RRJS6VAn1w986nyRQ6Kx-05gDMFjkalgSnYARWlQM0AXxN3JxmlKGk6K93600UZBmKxv45vullng1xKu08FACQGU7sPrbw9ir3kFC1WKuq-jarvu8F2R4eB5iRxy3zk48NrU8j4UfBeILXvTqLEbN4UFcBbquFZhm75f9X6x-8liInKuRUU8G74dWoik54eQobfgDZeyeQ0W3bszWBL0Y-imZ4hXS6ItJrQGJxAkHcb8qye5ixFd1qe62-2dSO6UVlAdrHyDC0U7ldt20dG3QsDAv0nu8cDaUhH_R2SNaMEceQTc77lNtt-F8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=fwjWI-1CWsn1Pz2GTHFA7_xji87_RtV98ZC9y2pYJrS7-e_6BBjrAeA87_CINzqOje7KTMM2EjDbL2ktHHQOGSMcsF-CdQCfr_mRXlnIBidKIWFLtrfgNsjBu15So5Dp_-wYd651s9Iw3j-bOCXmrjtCuRPFvtS44c7pFq67sWMOnKaJIiGolm0hQdFuY7xnmpKhaHp5yKsoWUNWXtkqMMwFFZHeqHRciejWNwxrbOC4t78iZXzzQ0EfNKVlM5ck3NKfExNu-bqRWjKn2ocqD97Y0WwdDAvoE9lCBxmZu0I0MlsJmCFPEnF5NxIUI7HTXR8H3pTiPK2rTwO3QxwAtGwUS_f6zBFeBvGo7_pv3RQCY0Oe9JQNVNsYbSwu-b2C93XW8rerS8VzDX563mZhFHouPrMMlcnF4gs2zAseUCGPoM7jUbRJ581lTByuH_IBNB5hP5fDv_HMm-Bc6Xih1pRIAB1WYApRODIbSrmdYQ0BwFQAWaU7l2JsenHbF7LK-VeCPejkX79ARGxoDNU5o7oyyzP6whhcoloQJEzgyDw_Kagz9Qjl51akqlMW5jcOOws0PrGD2Qdd284F8C5aOcdQfLbzAcHBHc3AVaFf2iY8KENcDhfg0-rVyELLcVJSe_7xPIBby-GJR1oSR0o74pGokvHQaiWKAWC09LqOHNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=fwjWI-1CWsn1Pz2GTHFA7_xji87_RtV98ZC9y2pYJrS7-e_6BBjrAeA87_CINzqOje7KTMM2EjDbL2ktHHQOGSMcsF-CdQCfr_mRXlnIBidKIWFLtrfgNsjBu15So5Dp_-wYd651s9Iw3j-bOCXmrjtCuRPFvtS44c7pFq67sWMOnKaJIiGolm0hQdFuY7xnmpKhaHp5yKsoWUNWXtkqMMwFFZHeqHRciejWNwxrbOC4t78iZXzzQ0EfNKVlM5ck3NKfExNu-bqRWjKn2ocqD97Y0WwdDAvoE9lCBxmZu0I0MlsJmCFPEnF5NxIUI7HTXR8H3pTiPK2rTwO3QxwAtGwUS_f6zBFeBvGo7_pv3RQCY0Oe9JQNVNsYbSwu-b2C93XW8rerS8VzDX563mZhFHouPrMMlcnF4gs2zAseUCGPoM7jUbRJ581lTByuH_IBNB5hP5fDv_HMm-Bc6Xih1pRIAB1WYApRODIbSrmdYQ0BwFQAWaU7l2JsenHbF7LK-VeCPejkX79ARGxoDNU5o7oyyzP6whhcoloQJEzgyDw_Kagz9Qjl51akqlMW5jcOOws0PrGD2Qdd284F8C5aOcdQfLbzAcHBHc3AVaFf2iY8KENcDhfg0-rVyELLcVJSe_7xPIBby-GJR1oSR0o74pGokvHQaiWKAWC09LqOHNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBPXyMUF58rr1SdXjtc_vp6kBpjWLARlI78aFEUIR5_4P27QGVb6Nv9aMvYPl-YAAOm9KhSbw5VX0wdrWUwZTOxo34HlifCSnbrVW6F4rUoOhFmW8Lh_J1-Rn9q2Umzid3ytNPthcXN5o5ggOXd9Tw5prIFBptTXJ_gqZxBACy_zzps7d-4ucc7kl3fZJiEohIl9IG9zhSoRfde4gQwjz_3sk2ColIjbQL-Yd1M-kik5Ug2bTrzR9dvqF8NyUlZIXFlJkHybcoORkgoDhi_PdyoFSal4NFU4j03bFeHpjP3licUZ7JXp6xYWFuOQ_fEZG0FMIBhvNBT96URVSJ_2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_N3-rxAlo7TvPoMiaur_IjK2c80SGA4y-581Edxc-cT5bBScg2OlAl3-8HSTRSWPnwmZOOtaZ1bSY-loUujW437NMcyKr9H6OIh5tPox4n3XOWaWqJ90f1I9ExIbQTXLG7o0T0DpOHKOg1ZWM0BZYi9645ES-eJGBj6-FXuxyrvM1DIEZtJxjkgCTcvzfcmxRv7fe8lSKhBCkZBLF9zhdF6In2xGYga4KOnWcqmW4lREt8-ons9jgNiPuZcK1J8d6cMe7Mn5Px405j5X6Ydpx0aOCaArPfFpioa1Z3rxjE8v0S8xyNGV-cncMNH0t6PpcPIws09VqA5wGwnACo6Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_teIWMzl1PzzBJyhAVM8AUW_pzhYQtCzDNed-fHiojCjDZF6cMbbgrxjsJyPDlGHchrtKekxTh2Tsi1FobrfsS4AliKF_4YFLMM5_5HNXcDAtui4ewvnQlO7moG9hgvTNI0cHubyYytlvHpvxxdoXqMxbnDmA57gEOlSC7ser0RI9Gfq4dLrEqXRMx3Lvika5vicmmSOp5Y2oAhTgwJlXOx3G1l5-ij5-peEtzXNiU6Ges8fYvjme4dt6bsm4S2Mxa0Tosx4m0ZjHu7v3Zi6MV3JUYZdUVexOHXLX_dahDQtjnwpXPAxK_o4iXIunBjsXcTNbs5rRQKUZBGVLdOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=mPx2kC7MPd6Yk6fepHoAvuYr0w93STT8U7X3enKJis7ySQw6je2XLASDs4WlRR9eFfYUnlg32MDDX32B7c1EL4y0bRWAuM1n8dBr7ulPyc_c9DkXZxz-0RF1sqNkA5SdSVM050gCi5B1FuFG6r-4IfB8-CxM1RvtV1ZQXrRnumz46d1tdpvZFAmMLJuuod9htAfhb7OGjVH5gC4rrH6jYz6N2kYcqfLesJxAmK-xkL3QP6ISNi8beeJT3rCvqLnoR-KPEfBtCmOWLuXS5A6yh5aBxSPBZFwrMXrwt7mADE6SmguJ2VGDV-mucZYAAhg9nfQupOyrCOon3kH3rOilLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=mPx2kC7MPd6Yk6fepHoAvuYr0w93STT8U7X3enKJis7ySQw6je2XLASDs4WlRR9eFfYUnlg32MDDX32B7c1EL4y0bRWAuM1n8dBr7ulPyc_c9DkXZxz-0RF1sqNkA5SdSVM050gCi5B1FuFG6r-4IfB8-CxM1RvtV1ZQXrRnumz46d1tdpvZFAmMLJuuod9htAfhb7OGjVH5gC4rrH6jYz6N2kYcqfLesJxAmK-xkL3QP6ISNi8beeJT3rCvqLnoR-KPEfBtCmOWLuXS5A6yh5aBxSPBZFwrMXrwt7mADE6SmguJ2VGDV-mucZYAAhg9nfQupOyrCOon3kH3rOilLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=is3J3-Rh44DK-sS_4rYeIFglYYqkubep_XE7sTVJ3KNhfSF5ivHwj23iUGVQHQJMyruF-rH73TbpxxpF_kKPKMBp-OupEa24u16VFJUl01Mb44tukumLk1sySWCWewKQ6NOPepClpI-ddFErFdJD16cZ5awlzXE-K_ZSqLfEiOSPe75g0ZXmNjw4M6h1aECSg_QbiokioxuDQc1ypy1LBG0k0QlNCU3I1YaPYpecm-LuEpzIae2OIlxS8bYZEJo11qEbjskSgnXM5zmE4dz8QqrEERl2QU2vHqakyLCBtU2bJOHgwW2AsojjpneWz0Q5bFg6miNgsz3A7fL2-DwSNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=is3J3-Rh44DK-sS_4rYeIFglYYqkubep_XE7sTVJ3KNhfSF5ivHwj23iUGVQHQJMyruF-rH73TbpxxpF_kKPKMBp-OupEa24u16VFJUl01Mb44tukumLk1sySWCWewKQ6NOPepClpI-ddFErFdJD16cZ5awlzXE-K_ZSqLfEiOSPe75g0ZXmNjw4M6h1aECSg_QbiokioxuDQc1ypy1LBG0k0QlNCU3I1YaPYpecm-LuEpzIae2OIlxS8bYZEJo11qEbjskSgnXM5zmE4dz8QqrEERl2QU2vHqakyLCBtU2bJOHgwW2AsojjpneWz0Q5bFg6miNgsz3A7fL2-DwSNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=kkRGfF0jEEXJ6u-ZOzJuYqoXHNG0vbyRL6dMkDG0PP5nYnlfdHYh3gN9-MSxWW0y3j_ev7wiw25fJ331ppPuEHDQoOqyz6TXRHqQ4yPk5nuRLg9qH2ueP-D_GhRvEbq9P8ICfpeEY9Cl-PL-9_tu2r5awP3zlrJf2EB_KQnLzwcTcYZVc914AvRP__fpt4HLKAGPDKuTLTcVDaizSS9Jo_wpdl5lXdXqzA8uqFRxB1Rtc4PVxPmlsePlt4OQPFjzTP0oWyDd23VQQyySLMwAUsJfgNfoIaBaB6oP8cnJKqDfu3pfZW86oAHjKduNlJMWM1vs97tqu1bv3LpSjPTljA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=kkRGfF0jEEXJ6u-ZOzJuYqoXHNG0vbyRL6dMkDG0PP5nYnlfdHYh3gN9-MSxWW0y3j_ev7wiw25fJ331ppPuEHDQoOqyz6TXRHqQ4yPk5nuRLg9qH2ueP-D_GhRvEbq9P8ICfpeEY9Cl-PL-9_tu2r5awP3zlrJf2EB_KQnLzwcTcYZVc914AvRP__fpt4HLKAGPDKuTLTcVDaizSS9Jo_wpdl5lXdXqzA8uqFRxB1Rtc4PVxPmlsePlt4OQPFjzTP0oWyDd23VQQyySLMwAUsJfgNfoIaBaB6oP8cnJKqDfu3pfZW86oAHjKduNlJMWM1vs97tqu1bv3LpSjPTljA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=rzhSqOX_KuS96WZKQtAnKn96yqvEyl2ewX1ce6uZLRQU3UD7-nLyke2Izw79_g6KhlsVyaa_EnPneEWvoBJFpkCm5QPzGpoosIAw7NIG3JFf7s9BoB9psBn_Uu2AbgG08vUj0QgB64MV8roEsJxB3-CEHUBHE2irtdRs1jjvcW2TqnocHLV1Q3D6YlhPiqScCXSqFQS0G_eCjVhNPpHtLvBKfVFyyCmuHzQY7W_c1NZbTSoy8iWknWqtM0xHaawbEYV7eFZmsrmTjXrZUnRqtzEc24IWDdgwsKMS4-zh0J6M8CqQHkTphLrFXJeYC-LquGeZPnmZ35-yNinzgmr9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=rzhSqOX_KuS96WZKQtAnKn96yqvEyl2ewX1ce6uZLRQU3UD7-nLyke2Izw79_g6KhlsVyaa_EnPneEWvoBJFpkCm5QPzGpoosIAw7NIG3JFf7s9BoB9psBn_Uu2AbgG08vUj0QgB64MV8roEsJxB3-CEHUBHE2irtdRs1jjvcW2TqnocHLV1Q3D6YlhPiqScCXSqFQS0G_eCjVhNPpHtLvBKfVFyyCmuHzQY7W_c1NZbTSoy8iWknWqtM0xHaawbEYV7eFZmsrmTjXrZUnRqtzEc24IWDdgwsKMS4-zh0J6M8CqQHkTphLrFXJeYC-LquGeZPnmZ35-yNinzgmr9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piBuo91u4P3gbvwX7Rk0vYhWilxoWh2NYkJV1PVwrlDF6LTKO1etX6IUZopR4Tz3QJeOSNv-yU1k-NwunCsKFNPfPVPL-xYjs1tQop7Lk6EotWpD3P86uvnmp4zvwaaqnWBe5oz_LmwMz_JaKwGydc7hcgTdq999b0_s7SOA8m5bZbfOE7lp8cO4_ka2B2_g6PCKmAfHElqlFUszZ7lBT4ucMEdwVwGRgAhbA9Wklh3F49Sc_BeRG8BGbne134CZkJoYmFDmU3oxzuabm_iJqlk3k01Jg29_3H2KP78aenl9rYt_fk5SmYHkYhGV_NxMIMrxddfHstgKnhg5wHhW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Td8qrUc0jfuDMJW-rswsnkl0WgYp6wgDjy6MsaWNdwyP_BWfwG5Es1XT_Kgeq5B_CWv5Q5ZElsCsNyNEU4ff1gJ2fLw7AuzgpduK8cZkzA7lkZUW1mZs3iMv1KpNUY2f803qgdhMm4OFU7b1UWgQq7P3s5Mia56RrttJ4pR-xmp3TNBDq3RGUtQy8OYc9Xc2XVm9uHe2MfFYKKYRODLs5CicrDbvxS-DtEAtgqUuJcdRlGi1WOfqXFVLEaO22LfzYjMm7PPWiRv-z7fQhAkcd45iHaSA2OedN8DUt1jqQzwFvwkRTUJknPAISKBjRupobh_MwnRm2WOe-0U7llVE_GbRrVrpQWZv2B9cT6rM8y4yzO6FabRLxAVMueISCJA0N2DnbioL0JyyXNnTdni-nmOVuuP1ptCkm9_q-XsAxNTOMp3TMPAU_45jCBn6yV7PzjMeOr-cqsU6keCDdzWG0tbJgMhQNKWEYuRB51emBwgOzfDo73xFifeAfgCZPskR22BrYjRfCIiPXKnRFJmAxGxpLSKSTKhDfAzxYHhYHfbrshOghpAgIVfRkobgqIFCn6pAErapeiHeHxodlIFWgw_YYA-g9zUeT9QzktNMt40_q731edSm0Uoy3WFWsgP-zMh839cTx4D2BRdnQaCK0AfS7GF0B72uU5CT-QmDa9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Td8qrUc0jfuDMJW-rswsnkl0WgYp6wgDjy6MsaWNdwyP_BWfwG5Es1XT_Kgeq5B_CWv5Q5ZElsCsNyNEU4ff1gJ2fLw7AuzgpduK8cZkzA7lkZUW1mZs3iMv1KpNUY2f803qgdhMm4OFU7b1UWgQq7P3s5Mia56RrttJ4pR-xmp3TNBDq3RGUtQy8OYc9Xc2XVm9uHe2MfFYKKYRODLs5CicrDbvxS-DtEAtgqUuJcdRlGi1WOfqXFVLEaO22LfzYjMm7PPWiRv-z7fQhAkcd45iHaSA2OedN8DUt1jqQzwFvwkRTUJknPAISKBjRupobh_MwnRm2WOe-0U7llVE_GbRrVrpQWZv2B9cT6rM8y4yzO6FabRLxAVMueISCJA0N2DnbioL0JyyXNnTdni-nmOVuuP1ptCkm9_q-XsAxNTOMp3TMPAU_45jCBn6yV7PzjMeOr-cqsU6keCDdzWG0tbJgMhQNKWEYuRB51emBwgOzfDo73xFifeAfgCZPskR22BrYjRfCIiPXKnRFJmAxGxpLSKSTKhDfAzxYHhYHfbrshOghpAgIVfRkobgqIFCn6pAErapeiHeHxodlIFWgw_YYA-g9zUeT9QzktNMt40_q731edSm0Uoy3WFWsgP-zMh839cTx4D2BRdnQaCK0AfS7GF0B72uU5CT-QmDa9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=glT_lK-a4472Ylu_dG_sQMGN38Hm6W6g0mCO6GRK_ljcFCwSI8EtRTTLI-hM9KV6mFtgsFCCc68OYtagiqE3S4qMEjkX0ntaZG_JRRA6FMmytitFVhT_EB560eGJa8X3TLb8WLfCSy3su8CV9Yzhag-dmmnKQlGxYOuXu-ijMIjxcLsnqEWIBW71Vj8KkJ3o1y7RA1at8y_CZyc3Ctp94Jzn-OOXljLtPtdWmH13fpa6qswq_Dk_-r1qRRfQyszAzGMWrBdSbcx4ON7x4itn8gG23jOJD1u_HlpHT9Q13QSISxCklH38QP7RJMoj6be7kqbMpCcsrTz-IbPyBkxX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=glT_lK-a4472Ylu_dG_sQMGN38Hm6W6g0mCO6GRK_ljcFCwSI8EtRTTLI-hM9KV6mFtgsFCCc68OYtagiqE3S4qMEjkX0ntaZG_JRRA6FMmytitFVhT_EB560eGJa8X3TLb8WLfCSy3su8CV9Yzhag-dmmnKQlGxYOuXu-ijMIjxcLsnqEWIBW71Vj8KkJ3o1y7RA1at8y_CZyc3Ctp94Jzn-OOXljLtPtdWmH13fpa6qswq_Dk_-r1qRRfQyszAzGMWrBdSbcx4ON7x4itn8gG23jOJD1u_HlpHT9Q13QSISxCklH38QP7RJMoj6be7kqbMpCcsrTz-IbPyBkxX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlVISn_799bdkpUZIRsKpP9EzPEGNEYyUgG3pWEis9bdYl-vvlmxprlLGkGMeb-m2XxGAFhYNiFhqBVFrAugTD-dfLzUFQeK3raKL-Zj-vDJH3yYsu6dXhMLwvw4s-5bJeLgjBuXByB6-MEiSCCJoQLmUD1GYvdox8f4YbJqAszQu-IjuYySzEK07S-GZfEHvCL_6kLuchLZM-kjdkYUik800kiASCuFW94WDwxrGSZyszUVmzc1PkjrWOSUGAvCqkwV8STgKTTugXeG_ySMmMZO-9Evygn4c1Qx_pypQyHmf7bNuY7sQn6ZfsleJA4Y738JCcepzNajFNmJSYo0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=mH9bNGDcvMcd9Ql14fqQ7DWQHpKiE-ahULWUIOupwWpsTqrCTT6P5Ear1b_bgeURD4zEcOnQPsq_8k6SF6DSSK2Lzhv_J31RooMHHg_7kEN6hfeiGFHB7AsVn7qS2BU2cINOmTMdYETRgK4tAwoTQCMDgMxU3BTKcp3yhShzaCI5V54bTYitB8-inGw9-jrwVRmzeavUoh9BdYls7OA1z11D4pZBnWurzrfx0GdYqkW_NICvFmt_X9sy43irCAw1o7gp9aaRxiUuS0Gog7RzeiPSn6rzgRslbV_RsIF_43GfqJtsbF-afr5qosFbz0U0JsMRyxSjX7_aKzQmZ04j4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=mH9bNGDcvMcd9Ql14fqQ7DWQHpKiE-ahULWUIOupwWpsTqrCTT6P5Ear1b_bgeURD4zEcOnQPsq_8k6SF6DSSK2Lzhv_J31RooMHHg_7kEN6hfeiGFHB7AsVn7qS2BU2cINOmTMdYETRgK4tAwoTQCMDgMxU3BTKcp3yhShzaCI5V54bTYitB8-inGw9-jrwVRmzeavUoh9BdYls7OA1z11D4pZBnWurzrfx0GdYqkW_NICvFmt_X9sy43irCAw1o7gp9aaRxiUuS0Gog7RzeiPSn6rzgRslbV_RsIF_43GfqJtsbF-afr5qosFbz0U0JsMRyxSjX7_aKzQmZ04j4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=Te-5nusHrAl_gvLL_EpgcyA4WstZXjGQZYQ94-nAtC7mGVtWBNMzbqFW2uSyamJO182bExBwYtYxIJDcuPnIoEEdpssDFuAxvEvk3FDU4M0aR7jcFNxuOirgO5BymzkQRbIZYIvJBEc2yLBFlTiiBJ1qKqcNJ-7rvEe7efhEA3Cal0FFwGeUj1FJbUjEEiOnqYc0yvBGikJfmPt4b88OMKihcz0lFXieBBPRL9QW21IDH6AitUKMpKJucDOKQODPIuqAqtSlKRC8_uGXVA_a2CJSGtPoVZECXe2jXDR9AH844xAftB3VZb8-bE37Dg0QrQujm7wHXl41L0RTMTZAbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=Te-5nusHrAl_gvLL_EpgcyA4WstZXjGQZYQ94-nAtC7mGVtWBNMzbqFW2uSyamJO182bExBwYtYxIJDcuPnIoEEdpssDFuAxvEvk3FDU4M0aR7jcFNxuOirgO5BymzkQRbIZYIvJBEc2yLBFlTiiBJ1qKqcNJ-7rvEe7efhEA3Cal0FFwGeUj1FJbUjEEiOnqYc0yvBGikJfmPt4b88OMKihcz0lFXieBBPRL9QW21IDH6AitUKMpKJucDOKQODPIuqAqtSlKRC8_uGXVA_a2CJSGtPoVZECXe2jXDR9AH844xAftB3VZb8-bE37Dg0QrQujm7wHXl41L0RTMTZAbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnPp4tdG093iPG6h6mwrmq0uh5JRGPgP4ERZ74s35ECaKqo4vbE9CDf3SMIGIKjB9NcKDIytbzisWpXExdpD5JCv9rSVXuP5iPbD5NaZBqEG-oI145COc7532dDdXf9T_QcbUzYB1OkAQPb2mzxrx0RWJ-jhyuWY78JXduqc_Zs1xC6s-UMpzntd4cbkYWGZjXtncXFAnc6MG0zdm5cmc6MeeuOnSPa77ATF-Wsb_gGqkCVR_wzQMUn6qkvmeyFEONB5hTnxN3TbmaprVm80JzATCm4k3_2YErnmy4AfA6xeR_M8F8oGe1UW9bF3n5dE3EdX1B2C6wyb3B5EHXKXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=KWz-pl4lgPoqEH3u5Lh1KdVE8a4ra4vwoYpODiGu03_VWbfOvbbsBOrIjl15z8zJjwgCE9mN2HciIM3rW5GpjXmk3-YP2-DazzXTO62Dqx2Vq-KaXm0DHpnRmMaEewgtRHSqEwg7-4HEJKbdxcpSUOvDCkKfQyu3dftr8Be-URdaKvn58TsSq3Kh7xxwMaV_ABOOh4Abzcw2T_N66lX-3HMCTtubygmqfzGj82L0AgkzCq9erosX0SEVcREDEC1AS0fz-XPFBVqN9gbgUemn4zG4uIBPq4hU1nu92EOsOxRgBmB3TVEvLFNDItUgbCq6aH78JXy3SwuYK3VXdQ9Umw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=KWz-pl4lgPoqEH3u5Lh1KdVE8a4ra4vwoYpODiGu03_VWbfOvbbsBOrIjl15z8zJjwgCE9mN2HciIM3rW5GpjXmk3-YP2-DazzXTO62Dqx2Vq-KaXm0DHpnRmMaEewgtRHSqEwg7-4HEJKbdxcpSUOvDCkKfQyu3dftr8Be-URdaKvn58TsSq3Kh7xxwMaV_ABOOh4Abzcw2T_N66lX-3HMCTtubygmqfzGj82L0AgkzCq9erosX0SEVcREDEC1AS0fz-XPFBVqN9gbgUemn4zG4uIBPq4hU1nu92EOsOxRgBmB3TVEvLFNDItUgbCq6aH78JXy3SwuYK3VXdQ9Umw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4-vo2SJzpSCITQhA7TEP6-9DTWCypmhrLaNfOTjcV1PMJ1z2PyP6NYuT6Jsyj90Cd_FhR9R8yea76fI0aWjKOVkJeXyiKRAptbVz8B6-zwYT-DyzntK5E4hGRtqrLdC80P5kSO2ttoqwAFzuC0gEMV1XbeFgmbVx1rB7FMInA6k8tH20fWnfidZcW5nkZB4PwsXe5VuKU6fz48D56m2XnRtVB4IgjxxwBqrJaQ63xhHdBGnxJaa_y0OjYp_hyda1wDnLGRgQjTjdR0AlV12loVMNpqvm5Yxa8GvWTEmGR1mgiOeszdl7X4lI-QJxxTaznFlfODU4hSvBJqJelZIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
