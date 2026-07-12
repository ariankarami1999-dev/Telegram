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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روسیه در واقع تندروهای رافضی  جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد که تنگه هرمز رو بگیرن و بزن زیر تفاهم‌نامه!  این شد که شعار دادن عرزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان  و حمله به سه کشتی در یک روز رخ داد.</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روسیه در واقع تندروهای رافضی
جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد
که تنگه هرمز رو بگیرن و بزن زیر تفاهم‌نامه!
این شد که شعار دادن عرزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان
و حمله به سه کشتی در یک روز رخ داد.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b23JA1V-CUObD6TwsH0RRZ5uUMT3GPFPlu8-Ear75DGj3Dify3JlWq8Pl8-QxvZXuUgcw0tQb-3Hjt8QDWru6E6a-YCBxcDtcSptuUZWy8I5yHtbAWx5m6cRcP2WXFd35rF3YAZ2jw1fIwR11r8q_iZ1FbVInjo3zu12LOhg6uQqFHka6XRpBEB2BNC86F7q-1MCzjuqTeBHf94Ui8gTdFXCzs9R4KUBPeV4fQU0FnYyv1JQheOE4zzsFokjQ3_-rWVB4UagcPau8qToGGQ1SOKEfDbnAm_kZ6huOR424klAvZAD5pN2yjmCbJu2AshOo03ovnPRIKhYmCehAAI32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmu9B_s9vTvyGj2zrTe2Se3chjW2pVp_c2Bn-1El-QP9_jMVDGuE8_juGijtDpMgRtXTEQnvMhxqeCIt2l-5hb5cq5AwyewDBxzvb1uqXXDBbmKBkSxT7-Pu4ApO654kjS1l8LwE2_d0RGI4Y47P35pSif4QVhBQlK7Tfy3ApU0b7jtfRRcD2X8nfBk8rmssW4K96l51gzutnV3p3QnINZEIsDH6eP0ZEpnMUEDm-h85JtuCMMxclxDhNWztnwbXFB_9vSJQc_QPt2iqGkwzsP2TkW-EESCrmodrHUzBt0WQqiUEs93kL8FOaJD-GwGEoiYlKhvvtkuKirTpS-JJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wkjnFFYSVLJW15uFIllcIY9Hr80JsZJObJ_zS_d0dY5c3k_F7S6twNyo619DnxB4hfYYVqigNEh6FzUBXvgLdLJm4Wh0P9zhS6rIw9-AtZsOcVOWk_ZypNnHEhXtDJd_Sr8lwkAw1HNqPVIPBDb24w6axNW3__btmlZwBxU_gPvmqJWjDUq1GTNLNofdipbs7HRrC1iZT5Rt-RyoE5EJIgPMNNkTqjnT7H_wbxqAzrTykEqZMWQw5rjo8s5JgYjymhgPuYJ3qWIeqfj1AKFfADjNqeUOp8KA-7BTOx3eMCSo8TUbIsUQeMqIaGWj3yitW1xtQwLcNx4UCOgTB0JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=KLVf-jkwX0F-6q1mG8wCfQh7vkvbfKH2Eb6rtrcUA6-WCSOlpVOgMKgH64tpKFQM-3QSOYzmyGr2lLSpBp6gaSKBd2xSM4M7FazC-fqG3tNhT0DeaCGqxjmGWXOGjCadw_JUakk4Hs-IymwdAl9DWH9fYOkrFOMhnQeo8Cj2okWNeShwyJ6OrfULYW4ymK6kbSsD7ehEg9ahzNK-bvDA3MKLRQkZWmcDaKtzcJBnyLbq7WEsGaYxoI09CP66SP9-tpN6RryDls43i4_-oSDJhmaSUFzYuIFLqy_yCEc6WQN8lkY8_UnbKe9r_b9FMMtnn1p6X_CfZDkXQbIA5B9olJfBHgFIlO5DQk3Rxet--n7XovdpuFyoGFNG82fU8pE7WWw4kUqXXpp5_PCVsu-wRkLBlsHOBRHom6vSkcaHxfEezQsvIZhYUaZOMEXNp1_cExnCVovu-aRBO_VWRyZjh4syYvumq-HdxRe3_6hrQRTdnrw236qOhJU6_zryz-0JB5q0_FvPjoJA6ZQzuV1NX0MdaDKoQ2GNm_JgF79B5miUAj8MpDJc_n7KrORou-6F5DZmBGAFjFVL4-RAlGtPQkqZNsC3jE6NOn0gyX5gCT7nHIGguEowl4zSrU1MmH7YDAA43KCSWCt8HzC4mvaze8lpSy74mEfun7Hf5QM7BVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=KLVf-jkwX0F-6q1mG8wCfQh7vkvbfKH2Eb6rtrcUA6-WCSOlpVOgMKgH64tpKFQM-3QSOYzmyGr2lLSpBp6gaSKBd2xSM4M7FazC-fqG3tNhT0DeaCGqxjmGWXOGjCadw_JUakk4Hs-IymwdAl9DWH9fYOkrFOMhnQeo8Cj2okWNeShwyJ6OrfULYW4ymK6kbSsD7ehEg9ahzNK-bvDA3MKLRQkZWmcDaKtzcJBnyLbq7WEsGaYxoI09CP66SP9-tpN6RryDls43i4_-oSDJhmaSUFzYuIFLqy_yCEc6WQN8lkY8_UnbKe9r_b9FMMtnn1p6X_CfZDkXQbIA5B9olJfBHgFIlO5DQk3Rxet--n7XovdpuFyoGFNG82fU8pE7WWw4kUqXXpp5_PCVsu-wRkLBlsHOBRHom6vSkcaHxfEezQsvIZhYUaZOMEXNp1_cExnCVovu-aRBO_VWRyZjh4syYvumq-HdxRe3_6hrQRTdnrw236qOhJU6_zryz-0JB5q0_FvPjoJA6ZQzuV1NX0MdaDKoQ2GNm_JgF79B5miUAj8MpDJc_n7KrORou-6F5DZmBGAFjFVL4-RAlGtPQkqZNsC3jE6NOn0gyX5gCT7nHIGguEowl4zSrU1MmH7YDAA43KCSWCt8HzC4mvaze8lpSy74mEfun7Hf5QM7BVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIQUHMvPYDZbwHnxOiGQE50K0UdbcPllsJBzgqIZy4-GSyG0sqI2V7NCeZVRr3dcAenwlbKOC1_uhY1mpp1mzd3JfUIRRgOzV9DbmmkW2vObBi9Y4NgmcAWB2UUQH9oFssENTjgYbKLXCGuIhXs4L7VDM8YlEwcMII8kTCALL6kGKHC9uomf8zVpCQqy4RXBgzCJ2ZTsHd3wELhzovLpfpikjz6hEjmoC6r7hBe0jvWgzgA3AZCbLxsowhoFB29yDEQ_SGd2bFRShAE_xUwHhb2GmzdfZmxEDr8eQrua2kOOGp7YFXrNQRtf1FrWAb7DaJioPy9fOB_RCMBnzF8ePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmdTl1HSKv95gdD-cahVZB5A6bs0ORhItRRYTVOdiNexqdtIOmgdlLgScRC-fhLXuoos-pChWIt9RPD45W4rtjrAbueZGdQM5TqqKR_P023J3BmTzLKZia1U9VXy2Wxzi57EgbwMC_FRcW6hnLgKG3CMA_zaiUAZAygRC2Rm3u9LHHCyCj-08SzM7w2AWqN_hkux5Q27u7LJP4u9Snb7WB0vVpq_YnBv016TrEj6T_qqS9xT1xJmMYRUwmTKEc65Uo_NOs0k9OQwe8J5on_b0U2z64nUvPonph882SG4h56EBPyhA-lmnOo9XYn0tGsRLjHRe6zZsKMpZ2uG6r-VZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=WvclIbJeClTjTaq_xdpuxi33M9bHlODcOpEzMHn_8BDBEgYMwZ-QjQ8ohqVniJse3Ns6muQ9FaXOQOGbEdjOAOmD8S-WIG9K5jJ3EzkiH-LAP7y4YmrtI8LzPIKsf3mLFp_w89DkUZtCmWXcbiS8s-NEK6ETHxXN-zs7g7nHTsBbwmRH19f8Kz_dp92m7zawfkcnnWl4yIKEH3wzNAqVnIaEZ5LoSgG5sy8AuFs2H7eXUK98jMSyQm7e_jaeiPOlGq4I9CJFTv2dqJ_u3pxrvL3M_Rhn9SOQbpBZ4bwYI4C8fCvTWf3aA3wmBVSda5sis5eu0DhpVZH-EakWJi59Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=WvclIbJeClTjTaq_xdpuxi33M9bHlODcOpEzMHn_8BDBEgYMwZ-QjQ8ohqVniJse3Ns6muQ9FaXOQOGbEdjOAOmD8S-WIG9K5jJ3EzkiH-LAP7y4YmrtI8LzPIKsf3mLFp_w89DkUZtCmWXcbiS8s-NEK6ETHxXN-zs7g7nHTsBbwmRH19f8Kz_dp92m7zawfkcnnWl4yIKEH3wzNAqVnIaEZ5LoSgG5sy8AuFs2H7eXUK98jMSyQm7e_jaeiPOlGq4I9CJFTv2dqJ_u3pxrvL3M_Rhn9SOQbpBZ4bwYI4C8fCvTWf3aA3wmBVSda5sis5eu0DhpVZH-EakWJi59Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry4ioj-VKhy75hoHC92jk__buHq3I2rlwyfLMaeupkz97pXSaD35n0TiiY1vBMIrv1n6ymLNhy9UV9ID1XKklyLC1XMUBB0AagcoazoMC8Ljb9WvPyeCZTVH6s9EUQ6RytYpXoZZBNrVJiEgup8upjAX-EbL5IGW10ac5dK1vjp1j-SOkB0nCvtWTrXTa61ltKd7B3odEG7tymuE3UeBF7oaHIePJCEP1FPtc6MlOWt1XYG8PdK1_nSb00pwKHLNNnaFgWzPPBoYKhAxaYD2hUKAy_PlOxlmhTPVBZewiU7NikWvFMRJLVBvmrwkKJtp1msHzyhJlrXBFPT__jSl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rceJVYU589Wadm0oouxWGenhDL4TkuJ986crKiRjneKDE45ePDH0AJQk8KdH7uCvWf7D8hXgw8NFbvlOc0FAW1j_PV0IXLQpIHGxY4dAGqn_MgM74pDMuKoz8ROm65OVrW0WmsvTJp8NlcLecJVdSfZPjrECLKmFLmjtDf-X9DCSsLD5kETKozKxCMB_SBWT9wvwv_Gr62nLX0pN3NqQmGVHsS-V6bSqIT3GG2Z0853sPtUpoTPYUPCSFKjo7jQCImBF8EzdI8UkHRUpYTIJIYxD7srttvJyC-_c24fsq5dDwyeW6-NOHsF89_f2ukPoz1QKdeA9w3fjp7xcE2gGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVP6Sa-fKwXq5l-ROZeonvUvDww6VWA5zbjUNrYX-M2buiexpvCmxIjXLMEzO1pPP8mzq1foxgqXqAazPCfkHBUB3vGsELfhbSjUiDzLbniHYwEORMtFsDyJeYDcQsSr9PPfldjXZrcXJfG0SyEuORtFHFlUOvl-l3C3B2CRlL_mkRp9t0SZkE5FcnlEEUsiOBu7H9KtQmtAPtx_Ea2DsG3nWFYF432GKRhEuVkyl7D-yDr7Z8wT9A9fko9GQ0aQ5cHSspvzszd5DL_SQwsNQ57mIM0GehWMNDLpSMFcVlOLkG0JVxpnnzEwXtl27BOp_VdRUTRIFUzUXmvryccfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRoQd0u0qFE7ywy8u3OnVuLB4492frC6ne5KA0A8z5QN3PaI5SLIwBYOhOPpTKVJlOJSK1qj8lwBU39S6rEbMybs_r7NHG1EzIajE1oHP_HhuuETZeHrkNAsAU7-1vEOHUt7M8zOUYi4KIh0miU2B116_cQpVgz3KUGtzJcjRosBZGJsvraSTVBLHBneWDt99p4zs9vJnZdbN26a9LpZfpjQSBIpfeDqS0HyIarhkFKA5xkxW0onIi_6C_KibNjyRz7tOv95h-BEs54xej-vkoxdOuzPyLsiHR6dWqDI7dNkDvM4UVvPcWNKgIy8eLTZEBQ2cpvOhltei2ut-xktxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7c7mP3Z3ax2MGFKEN4SgLcY3JkUYC4TqIid1j-qyU46KMlkWHxqB7c9tahFHPOWud7_fBLGkb1mwymzNXIXepC0ruiJAHcrglYuccZWzf7A8tOyVTDAX3JW-dxPwylhlUz2CRcnIGq3LT17t6_LvQoEtYZt-kWncZsSzZs5M-_1ykOgOwNv7flrbf7Hcj4FyuEQctsioXstHH9PdtE6201G33uAlav-SYqev7PX3mvtMmIdxBt1db-0MA4KNn8v64iyqX-ClGBBj2sFAR9U4lfFMa6DECL9SX0zkksJRuLV6w0zA45fizqjRT38Q0-hN9M_eoeS91-9-pa8SIGabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LteeSkqtvHT0oJu4C1E9ZHVGHRf2FtQVzA7BhGAiZLSkiTvPYX8LADwYORucXW32BEm3d4ELCYpgeOt90CiqOu1Gi3hcsTZtnqCOM67IYx8qT6vrbGbuwYMJuHqy76NN_ddofyFlBwW0gPRYT01RNYtbwdNxEefNTWdLlJW9wiDqUOkzDE0OyjTy1mI6O37-5lgZVWX3nP5TKUR1N9hv-I6RlFZCkapHhkfU-UPq0d8pXaVTboMekdILcjIoPIxdEBobecZ05vYJyehM_MB-v8VKbfIEat5eLvhPoqeh9TTOuKYVLyi6HEc8YPSp19I-LY6qRYCz3bIPN7goH7utQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKkD8kI65tOxEf2UlDp5Q3hEAOqSjuP6CbB06JwPOuFK_seSSO4qAdbGWQihFuQx2jhK08aetWQwDDIXfyXX1h5GbBGaK5vX-xmDRPJlUMeZtY14TnXrjuNdChmRAGIkPlmu6TSE3GVniV6VKmbKUWuXpLlHDqmWWaX89LadkBpotho4v8sYjRjglZr6w032DZysRHQMoOQsqrUNDl2XSLUoS05udm5IaD6MOjUWHK_nAjbeYBnjWD9yRCWKqcE6VYrpe2Kin2vhxqzVdzm5JVnVLQaufPvq0xbFxjMHP4ups1Gs6wYNTiwxEjb0WtyReK_XkrNOfZfvz9wJCBzzVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=CuJDn6KjDHDQj7-8F7v6t3tmISQimjU0Is7Fu0t6GUmheZ5PMAd_ncIeP55Y5_xcxtjZ-amD8G2hKyzttVME6UPtQWs57_vh2CbSZ5pYxqCzryu5-6VM2dU_IJf6bKmf6Ds7Fg7lnk6mCfNcmMuGh0FUOACCKqsZpwA8pfwnWE3PWuoGRDQEmJ-X5Tt8uCCt_qwInn4Rb1uKqctn52zqGPHJQ2jpMzak_6WsxPnvos0YOo5Gdwc1zbXy3LQ38HLjpMfYcJnJocoIu47dYsWN0P3kt3E4_ffAATrBzTY8Ng00JToKnfDgf_JwWigu-nF9v-o4mVCmu1mzHioKFVQQuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=CuJDn6KjDHDQj7-8F7v6t3tmISQimjU0Is7Fu0t6GUmheZ5PMAd_ncIeP55Y5_xcxtjZ-amD8G2hKyzttVME6UPtQWs57_vh2CbSZ5pYxqCzryu5-6VM2dU_IJf6bKmf6Ds7Fg7lnk6mCfNcmMuGh0FUOACCKqsZpwA8pfwnWE3PWuoGRDQEmJ-X5Tt8uCCt_qwInn4Rb1uKqctn52zqGPHJQ2jpMzak_6WsxPnvos0YOo5Gdwc1zbXy3LQ38HLjpMfYcJnJocoIu47dYsWN0P3kt3E4_ffAATrBzTY8Ng00JToKnfDgf_JwWigu-nF9v-o4mVCmu1mzHioKFVQQuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=cXz1r8b-Fp-i7-ZzSm06PCo2SXB9-oRW1FS0Zo20d1W6s_zDv-RyWA76_jNo58DSMvoWu-Qp9LJ2Dqnq7piaqtgQCWR-Jx_xSlhhQKSQpZV6b_wltul3uQaNzKUXD63o3X-fQw2oV8idh66FIqPBtQ1rjZQItAMJh8Pj5Vr6rpfcqaWtNB_XQhg9gG2N5CzblaMACCtGmsA-X9rMpvw7Qlp6O66JC-qHCXs1o03lCqIqnUxds3109qG6pYCT097YX-1wXeEdfDNcPmI6azlw7hHltOzBd5rZ6AhKN9UiPLwZMNgHJ1HpszYeS5HX__Nrxw7m5ZFZ6FMU_GyXzCufDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=cXz1r8b-Fp-i7-ZzSm06PCo2SXB9-oRW1FS0Zo20d1W6s_zDv-RyWA76_jNo58DSMvoWu-Qp9LJ2Dqnq7piaqtgQCWR-Jx_xSlhhQKSQpZV6b_wltul3uQaNzKUXD63o3X-fQw2oV8idh66FIqPBtQ1rjZQItAMJh8Pj5Vr6rpfcqaWtNB_XQhg9gG2N5CzblaMACCtGmsA-X9rMpvw7Qlp6O66JC-qHCXs1o03lCqIqnUxds3109qG6pYCT097YX-1wXeEdfDNcPmI6azlw7hHltOzBd5rZ6AhKN9UiPLwZMNgHJ1HpszYeS5HX__Nrxw7m5ZFZ6FMU_GyXzCufDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk97cZdk0i0Ts8_aEEqYsPWkDr5flL-ETrQQRpcAdSfOD0Cj5jCAAI_iDp5J06cdCwDiEs5SDXlyAdRdBs_y67o_lKxlkhXM5pvV_KUZ9WnKecCgu7PKqZX3vELfX30M-1Zvp3AZ2O2yK_cb940DfA-rochaDyvBj7jAYXhxkiJkjjjjROzm5tmw65WmXztviAJ-VkEOdRZTAkUnLH9g72hg2FIQBuNOHkFiJhzwYKrpLUF8xAun0QyCa2O4B4pe8X0twedfHabVSXPqW5yaOhFduFkTqsCHdH6L-Zu8CTaPd_GA2_llCcy53aIUJXlY6MSS1tBePGuxg6Zu1yaIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJcLFQacA_O_eMM_fiKsEOAopIEXJssmMfeE2b1HZNqA7mbQLH24aTz5zVYh2Mc8IFSTjYKLIwSaTRuAsLVQKWvTPdPwPSkRtBWFB9NRQLgSnwFzqz3WI393IsDlR1MBEk1OacY6GPGeIb0pt0So9lCeiQfi4M8CfU1CJpOrcAJEJjk2DVKpXXl7stwPm7JmT44hnZnD-APjARXO4OwTXD1nDbJToSuwxTcb0kWJaatAHjQQHrTNl5cT6V6QmAfL6Pzj3f1V7utNOYgQAgXguwYO81XYwjLnuhZMvWBU_YAt5nBiqjJW3catWgMIFnSY4LK_8KOyMfuWRda6zk6_5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ng3jckc62nc9XzTTqu-OOcoicVEOuTV5kBHUtZVOJO6vVaJ-8XvIuTjOdUCSSp_gzwybbY8aA7qR5jc9Ec1qQayWLzRnoxr3nUwrnATg3YvO96KeHgGKdgv2X6DUBZ5oTcSMUp_9es8dgNlVCviWF3gRTGKr0IqT4yx20sMyWP3ArzVH1oKEE65BMHTo8kCSRKvCvsW137lgglQmZuh1kxojEAmSiehcWcMMXoC-lgrgy7cW7ZV9O_Hp-8_s2dJfZF_cGoCe3sjzwYoSU8UqGOKtoiOr-2jCk4ea2-CX6GYJpOm9waUgSHXBL0zctY05YAY_hYgWGPQgBTs_2e2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lR-LM2asaX7C2Fx1xN5voXnC20f8XtDCpV3WWfB641vUwMtuo_k6fgEseKhq6LBNS853Td-6y9iPq-2efOfS-HTkZCrwlZclaS2U8DrODC-aDvMFEh8Za8in9Ycz14K_8Q2TbWCyWKJKFqiF04iS5EtizMqwhzTQ2mmJpiX-PbG_lf87vU6Cr5KQynISilqrqzAvq0mihVmbxnVIomLhsG7dCurRje6LMsOWANvjwNz2HCmXLO7sPOur7ypVa-Tb4WoG2RFgqdh8z5WqYhlIbLdElAIUlGj4ZtKv2ZyJ1nzVXW52SygsJljV3OX2iD1gB-A1stpoZt5ogova30I2o1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lR-LM2asaX7C2Fx1xN5voXnC20f8XtDCpV3WWfB641vUwMtuo_k6fgEseKhq6LBNS853Td-6y9iPq-2efOfS-HTkZCrwlZclaS2U8DrODC-aDvMFEh8Za8in9Ycz14K_8Q2TbWCyWKJKFqiF04iS5EtizMqwhzTQ2mmJpiX-PbG_lf87vU6Cr5KQynISilqrqzAvq0mihVmbxnVIomLhsG7dCurRje6LMsOWANvjwNz2HCmXLO7sPOur7ypVa-Tb4WoG2RFgqdh8z5WqYhlIbLdElAIUlGj4ZtKv2ZyJ1nzVXW52SygsJljV3OX2iD1gB-A1stpoZt5ogova30I2o1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WpWxOyMCc69lOr12op1-WXYBdU38_DynH_eaZgfOsRpkgdKmqroQXZ-FbPZLJ5VbxXMgKIMxynuXO39Li_RCfT4jpEaJPRQK1NUKluhLwVVkBwyd_LMNKPXwO6a3EiE9uO1hiVGD6z8t2wH8GtyzOPpTPkJtQgI6bi12kU1GcM9omvH4Gn26154Fy0j5uTXEuTqErWwAX8hvllWOOnnndHmLyPDuL-hiynLbOpAC1r0hyyGj3FLy4HGTXFhTSqlM1NFJviO9Ovc5boUrUQVBimXC-TOS--j5FwKBxX6C_juKa6dQdxdfuQMFlxZDnppIvBJ2a7NSPlXZw1YwsqlxTjheQ8Xw4ZgVfDd0h4ZHFkTPw_vUNWTa3Mi5cpTxq9HsIprYWwY8Bij1QbanHl6rOk-dSHR3TB0AxsGJn7DXdtGi1FHIErVik7lzeex4y1xQFIP1t1nHWBwwsCale8Z2jL1EUUGyX44JhnMoWUYuMmrULrx1PJL6i5uIg28bmxGwuCWl7BBSNO_KK5lekWzpn1gZ4qrRUlxuUvKf1zAT1dKSwL5m4mU9XkUKcalVQWmTt4SCUoe66Py3qUcdHmLzupjaB3yoGnoNzCQ1pVKKVtTlGt4pOerR94Kjtg1IxenC_pSkoNS7NJQzdP9fR3nU39bQVWEI9aqrxmMz1hlGmZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WpWxOyMCc69lOr12op1-WXYBdU38_DynH_eaZgfOsRpkgdKmqroQXZ-FbPZLJ5VbxXMgKIMxynuXO39Li_RCfT4jpEaJPRQK1NUKluhLwVVkBwyd_LMNKPXwO6a3EiE9uO1hiVGD6z8t2wH8GtyzOPpTPkJtQgI6bi12kU1GcM9omvH4Gn26154Fy0j5uTXEuTqErWwAX8hvllWOOnnndHmLyPDuL-hiynLbOpAC1r0hyyGj3FLy4HGTXFhTSqlM1NFJviO9Ovc5boUrUQVBimXC-TOS--j5FwKBxX6C_juKa6dQdxdfuQMFlxZDnppIvBJ2a7NSPlXZw1YwsqlxTjheQ8Xw4ZgVfDd0h4ZHFkTPw_vUNWTa3Mi5cpTxq9HsIprYWwY8Bij1QbanHl6rOk-dSHR3TB0AxsGJn7DXdtGi1FHIErVik7lzeex4y1xQFIP1t1nHWBwwsCale8Z2jL1EUUGyX44JhnMoWUYuMmrULrx1PJL6i5uIg28bmxGwuCWl7BBSNO_KK5lekWzpn1gZ4qrRUlxuUvKf1zAT1dKSwL5m4mU9XkUKcalVQWmTt4SCUoe66Py3qUcdHmLzupjaB3yoGnoNzCQ1pVKKVtTlGt4pOerR94Kjtg1IxenC_pSkoNS7NJQzdP9fR3nU39bQVWEI9aqrxmMz1hlGmZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej2ApWcDtjjIhgOfton93PCJ82K-zGzLJCYUZJpk2VdRg1odepuck1R-DXEkNw0lUg5Nr4Tzrw1cO8m8UcyP7iKy60b1Ybn8dYsTGXx5bOnDAUz8UYU3oUbKEPphkNP8o5uTOv3BezoWgB-agScllpphlHMQuLnn3ZGx016NrqV0CUIqO6UK0kl-rzhNH_RnGBw0gGHdylx9RNEK2iLp97rcbqqeiu6WcplK-VmllVhmkUBpAm6nmTCAjZ2fVroj5BJOPr9LkVGINFTIB6JQeCahm5uB8BdgouZ4RXrer3ypUOJn1QFb-xGVf-JrGVyYztUoe_BJgU0ZAkjIjIk05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEBDSuP5jJvUIwOUeEwBi20lOWnhSzZfHyNaUSAoL4utOq55aG2KUtC0lWJnd9aCdGcWuIPdnpcmTfxATQo6NEmMKdMUHGDBsOTxmSh63PW8B73Iv-KvasxwgFB_ht6yYTO-WOkzPEkEjBjL1reFPKI0yECXJ9iQrIQnkK7j3boKU218lFp5l_1rXUlKM3aNbZcK6tE8auoQTZXpzd1ogfDjZ21wDRYxhlKvebNa2n8ccRG4TaDBrL4FPOxfeUG7ctzZa0kfmSgGojXVC9sGc4KseUDFaeke43vXMOYDbZf-LU-6ELxdDb7-EJLhjB_WxiJLY1g7M7OUY5i-wiKQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vreveW4aB2w9Pp6zgMV4p0uoU0JuRbPF-ob1nGrD_CMqWyXJ-ZuHLlZVZlW3XoV1OjgRbJVQ4cO80_h4WlaqJuk3GYFsjZGJ_C5RuNGQyjz-exs7DQcxhj7e_Od02P6O4nDHJDlvUhUoXdVr7KvItNm-pbtjdPrUOOYfWradnhkiro6D4leXJEj43bh2BijTsm64-47cGrLdrTzcWTDqQ9xXz2aYfCXdCxzXFC5AcqoI2V9NaSi45GSAsT66ckTaEAnHbMv6naefLCsbVBhXszxFSOAGYsLKXHg5jAzSOoIteIvywFZDeivqIVGyOjLkIfJKEmmTnfmwpvTllDWdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=C985s3uGTLn7fgc9W8esA0SohuzcLx1M2x1uJMRdVZX-LVdW1yjvPiQ_I9j_K7Rhng9DOzWuWoZbJFPJ0fZW24HqGMdD1mYWelhgv228s4MA6LjtORnlbfPknvUPk1jT_7O8LTH9og6ohv9Kp0vx-RRTd13fFdvvbZQYpyxJQKNCGmALuM0ex9cNyYCvHq8alB9Loi4MxxOnb8JLplUW7yU_tZKCEWclunskVZQVru9qMJdVwZNMOtUp0TmaHnXKTGK82jg1pmcWgLBJweMtoQRWTeB_JLGkDb1ZgXzCDeoRjbkHpKXQELP2SHgX6EQJC7lNwoaoRzdLZ78-KKExGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=C985s3uGTLn7fgc9W8esA0SohuzcLx1M2x1uJMRdVZX-LVdW1yjvPiQ_I9j_K7Rhng9DOzWuWoZbJFPJ0fZW24HqGMdD1mYWelhgv228s4MA6LjtORnlbfPknvUPk1jT_7O8LTH9og6ohv9Kp0vx-RRTd13fFdvvbZQYpyxJQKNCGmALuM0ex9cNyYCvHq8alB9Loi4MxxOnb8JLplUW7yU_tZKCEWclunskVZQVru9qMJdVwZNMOtUp0TmaHnXKTGK82jg1pmcWgLBJweMtoQRWTeB_JLGkDb1ZgXzCDeoRjbkHpKXQELP2SHgX6EQJC7lNwoaoRzdLZ78-KKExGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYLY4tsECyZCiGeuz-L99szeHtV67VKVo6BBhhvitPNqNr0tao_azauViFtvL5V2ByDG4ZN275T29dt3IjN-EjH9-sV7O2TYt0cVlAWfy8HbOFXcoYwo4mT46rf0YZC_Vej2NbHtvOulAWOVZo_4QZ1-icVg8jbmfdIQD7bCs2qhTu7pcLMPGIPWUZ3H_wv6ihFkXcY-ApvB--FRsRqTNlprUNQhBs4BX-ffEu8awNj6HxcX861vYYZ_vHDCJjrRm5_io348kPXbhp1sdr0bFxIiHNyUPBo5caFFJvtl70QWhZnG0Emje7FncqBx0IKdea2_Zxf6UHLPBCOo6hY2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=MlvtDVK49jyr8ZI1dIsKaCzEzmg25M48HNhbbHAxO4KfsPsnkGb6gtjOuQZY7y0MORdmsymGjkYFZOaXYSG0GlsFjB4P1GCVV0OX08uaMmfTynGvIBVb_ptzvhPax_VRmDnoG8Nk-ptgQ644zIzZ73SUExcTg2uJcCfAca8SFPK0W4IG07UrSzPj_0MVfu6Xts17MP9JtoDsO0xgBVCo1x2GlVTRwmexrxrz30eXRtNlVea8YAzEWfYkFaV8yIBpkEaZrhmZAY11L0ZU2xapupJjyzG72fYGmHwC1hAmMvVSssXzJKtkDcNIUCJMLMe3fnUfhwSw1b9JNEOgS8fq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=MlvtDVK49jyr8ZI1dIsKaCzEzmg25M48HNhbbHAxO4KfsPsnkGb6gtjOuQZY7y0MORdmsymGjkYFZOaXYSG0GlsFjB4P1GCVV0OX08uaMmfTynGvIBVb_ptzvhPax_VRmDnoG8Nk-ptgQ644zIzZ73SUExcTg2uJcCfAca8SFPK0W4IG07UrSzPj_0MVfu6Xts17MP9JtoDsO0xgBVCo1x2GlVTRwmexrxrz30eXRtNlVea8YAzEWfYkFaV8yIBpkEaZrhmZAY11L0ZU2xapupJjyzG72fYGmHwC1hAmMvVSssXzJKtkDcNIUCJMLMe3fnUfhwSw1b9JNEOgS8fq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbKAhlgs0q6wrVJ2w5No_P6ny2QPxgU4qXmiHvHmuUb4PK_mFIS47TRcnpG8bUopsFvrnHXl0mYCXI7Ld41wdeNbJiEDnQiJbLkv0-0w_tmdvTns0oCjsnfk0hb7Btl3aiBWePizJoyoOZIld2bRdjMEYYhieyghx7we_bAX3PgV5MrbS06OPbszrP2XpsAoTR7c4cRzRxdM8IzChmLURO6p_EakB-z2aad1owCmmL5usvWbPmRThiLAM0m8SfAqlaQ-x2m73MMFzEI9QLgXEMCqmJUZOlcQx-_ZX2GldIYmDDhKk7MAGsNwyxjOO-wXl8sYAzDflcWchRX_S6KJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVKIgHMtO3S6oAg0FMIzfcUdvQm8skI_939J7zPx0uQuceQgUsRZLOhaQj4vnD-v24E45BAyXYLQBqiHcXuR9kMhe2bR3kD46oRWrM5BiAdemHVKL8NmPySEvpzqb5eYu6Ai__ac8-3yb9n5HQcB4NywrQfX8_OD9oxmtAhETzNlzo1-kRwOhrzF8aFVHRkp-4M0r9BDEFH6LGcu8_VsKdzeiUdlOgN0AniBTtvX-8nXBjPyev2pgs3Z08PITZKfIU9S5ayrrGRoA84G8h5Tac5i5jLxCP5j-JVNA7E8fkbGIX1d2Xow5vSUwXlP9E0bDTdAp31sYGlAdFKOUFfXRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=M-Pa_aaoZJ_A3wGMT-g3TJcHedb8oBJMmTx3zofc7aRkFgz9J-BvHaGd9B0h-Br-TrsB01aNBAZn68NjvYfJk3bSeN8YlbUyw-9nvyq0xq4LblpXPGnpUxDpfOzoVn5BACwbPvoLwYMkhsmrCtOPmqyEneeeJ72hbjzRzC9q-HJ1XsqUznZdyvVa_RXdU1fKLwPmuzTvhDzRUrHdvhS1HUE-lF38wFj5fOJvVydgj8T4OLVFB9beXPoaJtegteAY9SF9CaIk9Rx0YkO372NLdXgKLishxHu3mBTE5OjyRkgN59I7WEdk4JGSfWDkkhKyzy69CPYf0T9SNmYflzus9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=M-Pa_aaoZJ_A3wGMT-g3TJcHedb8oBJMmTx3zofc7aRkFgz9J-BvHaGd9B0h-Br-TrsB01aNBAZn68NjvYfJk3bSeN8YlbUyw-9nvyq0xq4LblpXPGnpUxDpfOzoVn5BACwbPvoLwYMkhsmrCtOPmqyEneeeJ72hbjzRzC9q-HJ1XsqUznZdyvVa_RXdU1fKLwPmuzTvhDzRUrHdvhS1HUE-lF38wFj5fOJvVydgj8T4OLVFB9beXPoaJtegteAY9SF9CaIk9Rx0YkO372NLdXgKLishxHu3mBTE5OjyRkgN59I7WEdk4JGSfWDkkhKyzy69CPYf0T9SNmYflzus9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ZPg2iODOMEBsm5Jh5kBHnF_kghHRDCjzpKxO2TtrruuhnzEW81V1n4lV2Cg4r8Q_ypQnksiJffwByAn7BhA3RhQcP7zrO34qeXimGpcw9AJU1iAUFaiFv01se69PotTQo1sBwEj__iG302AYKw1CdIu6PTbSMxJmzMF03XueyRVW5VRieApeNZ8TeZD1s5Zol5MLmwuvyHpF_eLtYnxwDjifqjwW-9VeWf0j5KXq6gp_hTFkdl5kenbjAmKdnqGZvGe5qOEMUj5n0NhlFKcoRFLIlEtVVnkSlQkFZCdsbwK5vIBg00HzrijXEB7Zz8R2DGnrgo8JX7JBwMWbMzfCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ZPg2iODOMEBsm5Jh5kBHnF_kghHRDCjzpKxO2TtrruuhnzEW81V1n4lV2Cg4r8Q_ypQnksiJffwByAn7BhA3RhQcP7zrO34qeXimGpcw9AJU1iAUFaiFv01se69PotTQo1sBwEj__iG302AYKw1CdIu6PTbSMxJmzMF03XueyRVW5VRieApeNZ8TeZD1s5Zol5MLmwuvyHpF_eLtYnxwDjifqjwW-9VeWf0j5KXq6gp_hTFkdl5kenbjAmKdnqGZvGe5qOEMUj5n0NhlFKcoRFLIlEtVVnkSlQkFZCdsbwK5vIBg00HzrijXEB7Zz8R2DGnrgo8JX7JBwMWbMzfCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=N5PPAsLZ6krcZQArCpbX4JqXWPBois4tRP_oFRGF0ffOt5Fzo5IQYifn9A42LA38WU3bYcNtxB2WQUyBHjF1nBsOm5odBal9K-EIuUzsQ_UUsUlRyD5tyfQVv9tHgQ_h73BkS3SLQQch2WCYRdccb_vXy3BG4KEJ4PGngOqPoIzWxfUC4S72LnU7Pk3xGRqziIeYQLrDJ9bBoMufl5B8QxYugSLfo-WN7wf8gv1pblFXnDix_UMrxaqvGQzhgihFcTS2fWOn0zaGl2ABdYiUizrGQJL1JXgm-5SKXLTZ4QZXyaKB3ZDnuUYLfqcJ1Ddcf2TzI81OFDv-nZf4fQYQ3CaM4su4R8Iw6ySaX02zJtTb_obA81f7FrWV8ikWH4tkdLsXrhaKeemkxpms1YX5UvY-_16FuOeP9fyVDCo7ldnuzLX529XhpaKNQT-bYVRa3wr4wXxZ5WlhtrnIJ4X1Ft4GELFHhnLcIBcNueauizGIFh3OT6C1ybD9ZrByUv0xvrW7S9uo5UO7D_uJdSZ9DBT5gXPoev4kwru3fwv0vwFNy_uy3TGzA2KwqZe33BjzfO1IWnGxOnkjebQxqs5_RNiv68n_QYZdFvd7TjKv5hQ20gnjT-x2Acm4dd6CdRw0TDhqiCC4SyZ3P2nDzf1h0tWFZfrTKB7deVJTl4dfjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=N5PPAsLZ6krcZQArCpbX4JqXWPBois4tRP_oFRGF0ffOt5Fzo5IQYifn9A42LA38WU3bYcNtxB2WQUyBHjF1nBsOm5odBal9K-EIuUzsQ_UUsUlRyD5tyfQVv9tHgQ_h73BkS3SLQQch2WCYRdccb_vXy3BG4KEJ4PGngOqPoIzWxfUC4S72LnU7Pk3xGRqziIeYQLrDJ9bBoMufl5B8QxYugSLfo-WN7wf8gv1pblFXnDix_UMrxaqvGQzhgihFcTS2fWOn0zaGl2ABdYiUizrGQJL1JXgm-5SKXLTZ4QZXyaKB3ZDnuUYLfqcJ1Ddcf2TzI81OFDv-nZf4fQYQ3CaM4su4R8Iw6ySaX02zJtTb_obA81f7FrWV8ikWH4tkdLsXrhaKeemkxpms1YX5UvY-_16FuOeP9fyVDCo7ldnuzLX529XhpaKNQT-bYVRa3wr4wXxZ5WlhtrnIJ4X1Ft4GELFHhnLcIBcNueauizGIFh3OT6C1ybD9ZrByUv0xvrW7S9uo5UO7D_uJdSZ9DBT5gXPoev4kwru3fwv0vwFNy_uy3TGzA2KwqZe33BjzfO1IWnGxOnkjebQxqs5_RNiv68n_QYZdFvd7TjKv5hQ20gnjT-x2Acm4dd6CdRw0TDhqiCC4SyZ3P2nDzf1h0tWFZfrTKB7deVJTl4dfjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTNSnBp8bic1yRkkwGFZMQ58KjcefOavX6hN5ZZ6rdaQ6qbxDHAIqLrXLUJhEuTVxvPpb6hNCZbIOnEurlsnKAXWRELd1C9m81Z-x2Bl7iK8Funw-w71D9LYys5LrUaCGp__ydzkVNoPuU7tbwFQaneSGmmshajLo4q8QYH4GaufZJ7LGe1j8ChtdT_A_fzx02rOMBetoMw69g9NFf4R8upYbSGQh-40vcO0GK75QZ3mbpjbPruBjlFf7EVbtfincFZxVxwAEzGz68FVHkLCnTDlPXsD7z09vkHGwArrggbnKp8DO2_HnJKoA6fankJO4x6gdEZNGS6xDtVcZuItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax0aPpnwN96CfBydzcCa_eR3iiWQ0ISmZ_kUHblIgSy-NuT0OIspw_JisYnfUuOV8VIRY2x7NUBcTrtLkpkxUnF7vLAn8mF9kEtffyCCFfvN-ZJaPnp8I9CRkXXQRwDg8f6jrcWqP3Pl737SWZfHRf4L3UJu4sNkWKLSp4QBjTgVnA7A9TUgO9gXvs57Cte_GbwTqKXxY9aWYj85qwKz4m_-aeZAuqaA6NAyYYwAiKA5pom7_eUjPiYiVG8pQKlbuu7ghzg7gehLrQfKb8hkMUszUouV9pjjaz75NK_1Y9dJz_siDSiqWNnwz2dqpt8Sk_L1OglAP21YORtDBIjHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrML-4ZkZj2uQZUshsNlo7uvswGqdik7XsBI1rmeyuW4xUyvo5-keuvhGssSdMBH9AK1RTnhHjuHNVEgJeJaoddwwHYL_9w3ghsHtC52jViSRRSNxjArAedC_r-C54A9L8K5cwa3CdZy7NYzpyqzq94k32-2YbVhdjSy6dYQVX7wFBmrLS6L3f8McT_2mWZ--LQGovlQqmmhuznccf4a3uW0nLt5Qun9chtiQ0gLgFTj27UKabN9c2McWYUT2frcTotI0w8O3fLvw8uVAxjP2DmJuxMQsE9I3rMPH4Zv7oKvLW2iqS1FwFOTUn1zeY3anblUdUJk1JbiD-wblQY1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=WPXWuITdnZls1zXSaH-23w8asSIwBkI3hkZ6gU8LRtP7xsJD_yTEOHbWO36huhQFOYNgzA5tdnonQEF2izyOlzqZlCJVLCCQw3PEmMy6ycdCVTxD_Y2-GV9mufoHPX6VttUUKPAKfSdsNIku6yaRdjNSxEUR3VKFvQmQHKwAaNfZr7cD4r78UfRQSyvevyZGfCCe8-qWCBc2iiwR-O_dMwUoBFT5q-u3kIu-aJPb27OxekQhNtVpUNnaghaHIEeA3dzsGJfgrNe6adtnXrNQmOL6fsZkZ9-zKc1RWx9h0TSfjKIAl6GgR1W1hV7z_llbFoyJvuTGOi2DUkHdRzcUZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=WPXWuITdnZls1zXSaH-23w8asSIwBkI3hkZ6gU8LRtP7xsJD_yTEOHbWO36huhQFOYNgzA5tdnonQEF2izyOlzqZlCJVLCCQw3PEmMy6ycdCVTxD_Y2-GV9mufoHPX6VttUUKPAKfSdsNIku6yaRdjNSxEUR3VKFvQmQHKwAaNfZr7cD4r78UfRQSyvevyZGfCCe8-qWCBc2iiwR-O_dMwUoBFT5q-u3kIu-aJPb27OxekQhNtVpUNnaghaHIEeA3dzsGJfgrNe6adtnXrNQmOL6fsZkZ9-zKc1RWx9h0TSfjKIAl6GgR1W1hV7z_llbFoyJvuTGOi2DUkHdRzcUZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=FLDyx-5FN4lcKlIK_Lm--eebQwU4_i0k5VpxPe2X8QIyRy_C5UqvZddJ620bQYADaC3Hl7P1VEtm54ug8qpwJL6wsqI9NjfAzUuFR5BgEO8fqdIlPgBSGfJhTw88Q7BpLrvSlA9AfmP5jImF6NuBkZE0Kl5ezr12KHe_ExcTF1UXuYeuRCElRAaVAdmYPso_sXViHU2wABSDhVauzou8XcWDSBDlMKy7C0ccYsHXqvMRBkiy-9Qx2MOWkqhpjKIGWBkgQ0ohBbv7iYKo5i9neSxXYP_ZsF5LSfQtkP4wUeefoIv67ebd6fD7KpSy0A2D6Cm2Sk1csIvIkcKebG4lxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=FLDyx-5FN4lcKlIK_Lm--eebQwU4_i0k5VpxPe2X8QIyRy_C5UqvZddJ620bQYADaC3Hl7P1VEtm54ug8qpwJL6wsqI9NjfAzUuFR5BgEO8fqdIlPgBSGfJhTw88Q7BpLrvSlA9AfmP5jImF6NuBkZE0Kl5ezr12KHe_ExcTF1UXuYeuRCElRAaVAdmYPso_sXViHU2wABSDhVauzou8XcWDSBDlMKy7C0ccYsHXqvMRBkiy-9Qx2MOWkqhpjKIGWBkgQ0ohBbv7iYKo5i9neSxXYP_ZsF5LSfQtkP4wUeefoIv67ebd6fD7KpSy0A2D6Cm2Sk1csIvIkcKebG4lxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=Y5C4tpuKksSDER0TxVz4_AambbPw2XFxeqBv0F_-hnpXAS1eV0lH51lpOE8ZhJAmb_JauTuJM9mO9jSkcNI9vLwmPXiXcAu6tYofB3rL4qUU5TKrz8mSNL0AeqUudJN1lX0-8EjdqnuNOaHNM4bx_czsJnrJ-VIu_yFbxSgyFFY_T422BV05yYVJPzS9L5gPMYL1ILq3FhPwCcTwzEDuJ_mVFLGuGZfWyP07xo6j3UU2LrqLMcPF6KvT7OdZHTSAOC-OZctWpZGbzTG90Kd0e3Xr8GZ6WO8sa1nRr88mgJsSMh8YsINFPNLHsqfeIsgmAxiu8rfIHsgg5EyRxTu9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=Y5C4tpuKksSDER0TxVz4_AambbPw2XFxeqBv0F_-hnpXAS1eV0lH51lpOE8ZhJAmb_JauTuJM9mO9jSkcNI9vLwmPXiXcAu6tYofB3rL4qUU5TKrz8mSNL0AeqUudJN1lX0-8EjdqnuNOaHNM4bx_czsJnrJ-VIu_yFbxSgyFFY_T422BV05yYVJPzS9L5gPMYL1ILq3FhPwCcTwzEDuJ_mVFLGuGZfWyP07xo6j3UU2LrqLMcPF6KvT7OdZHTSAOC-OZctWpZGbzTG90Kd0e3Xr8GZ6WO8sa1nRr88mgJsSMh8YsINFPNLHsqfeIsgmAxiu8rfIHsgg5EyRxTu9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Qdi-wdOTSiyTAA6XozrmvT3IIRq1vk0FTAdVYusMUWpzqQBapHTk6DYa4t3h2-R3s_SbZs1OvtwrzAt9Gn1I8xpAjrpnmDfk-OwiblP8pbeaO9DbC8_7Qat5NFPtR-EUEcPBzVLSNRThLvXDC6KY-XqpBC-PvQmnpXg18VnJTjS6c3xczQMe2gG8hJvmfDQaVB-kO3rzqqc3KoxEjMmjSoVmmQidjEISB9sXF0wSMGfC3ohptm_VcuGpzibUdzE0yFaq2gNiirg7E5BdjeO-h2Fqyye1crK3gXt0Zh3SkTfokcMTHNGl3VXo7UOZY6yBAts_5u2bUSofV7i2es1N1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Qdi-wdOTSiyTAA6XozrmvT3IIRq1vk0FTAdVYusMUWpzqQBapHTk6DYa4t3h2-R3s_SbZs1OvtwrzAt9Gn1I8xpAjrpnmDfk-OwiblP8pbeaO9DbC8_7Qat5NFPtR-EUEcPBzVLSNRThLvXDC6KY-XqpBC-PvQmnpXg18VnJTjS6c3xczQMe2gG8hJvmfDQaVB-kO3rzqqc3KoxEjMmjSoVmmQidjEISB9sXF0wSMGfC3ohptm_VcuGpzibUdzE0yFaq2gNiirg7E5BdjeO-h2Fqyye1crK3gXt0Zh3SkTfokcMTHNGl3VXo7UOZY6yBAts_5u2bUSofV7i2es1N1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKoyUZxryZUFv2sShUTdEGeAQR4mnB4ltB5pCF0fzIkBDITz11BW6cqKeR4t1T-dDtZzLtTZf1e-TXh6ZgqD_QA7reCQe2cZBr6wpfx1JldlMV6oJkRod-0Q6cQpj0voL_AYI--wVBC-b-X9Fzga01Urk29hH4XqULAB6YUy3C6yjwVWg_PaRz-wwEIyGG46004yzCTE7HXFrTeIZxbe2GaKWlj3U_7RStQ6UHGbCUsG0ugYsnAHxDHgkxFW5mP0GlYY52_9NAjIjlJA6f4mPqqqdqVsogZ3tzR7K2rjhOU3s9I9Y4M-6hzBBSpgZDfhDEzpfYq6kr-kJfnqE6tCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=n4MdvrKpEUN1GUTWopIDtKdLF1RhY7s0OQ8OayInOSGHlr6ItUShldvtTRy1vx7Apx7mZnKw9g0IjnptE9GCHhXiMKjGKKsLVEaDd9bWGWMRxtk11eFjCSg54gKK1fkNZljg0nyj-QFluLyvOT_ujUeTWu8qamS5SZ-xaYNSXX0G6ENX9jybI1S4VuNtTjKEbE9QxRDtZ8uF7NCycuuCYx5HIg_p2cUsCSuKEwi5iU94YaSZ2I0Xa85-V1qm2cM3geyic1DDhLMPnncMv9jWMT4E7iODWQOfTGBHGQ8TwDiP8wkmMs6Eq-O6g6gCU2B8TCmk5MWLUiKmKQ-Omsspe2Gv3tF98oWxGM21X99dnfIgcMpyYPl_5sb1ZeEr3qQMYuWe5arT21g3CkmQsBr7vflgxmSGe0FrnrLxUK3VreYai19o2njlwIc5AZXQ_P9JEvlfmvmbZo3as_nNln0Q5NnBD39dY4KD3-DLRGEyl3-G_dvJJ9qeJPadlEhg6FnDBd2-Qh-uoL3y1gkKq6Ltn2UTyqAxJPuIcKgXzFKglswtUj4GJn7RN9OThO3CEeLZPlU51y0hCbC_iGyW6P0AYa2_m13ULx7_HFKKEOEiqq6GHjRvED24UnMNK-DDmxWBPEQTyOwkjPcUJeYsRZ5b9uDUqCBGOKANMu6nYF1PH7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=n4MdvrKpEUN1GUTWopIDtKdLF1RhY7s0OQ8OayInOSGHlr6ItUShldvtTRy1vx7Apx7mZnKw9g0IjnptE9GCHhXiMKjGKKsLVEaDd9bWGWMRxtk11eFjCSg54gKK1fkNZljg0nyj-QFluLyvOT_ujUeTWu8qamS5SZ-xaYNSXX0G6ENX9jybI1S4VuNtTjKEbE9QxRDtZ8uF7NCycuuCYx5HIg_p2cUsCSuKEwi5iU94YaSZ2I0Xa85-V1qm2cM3geyic1DDhLMPnncMv9jWMT4E7iODWQOfTGBHGQ8TwDiP8wkmMs6Eq-O6g6gCU2B8TCmk5MWLUiKmKQ-Omsspe2Gv3tF98oWxGM21X99dnfIgcMpyYPl_5sb1ZeEr3qQMYuWe5arT21g3CkmQsBr7vflgxmSGe0FrnrLxUK3VreYai19o2njlwIc5AZXQ_P9JEvlfmvmbZo3as_nNln0Q5NnBD39dY4KD3-DLRGEyl3-G_dvJJ9qeJPadlEhg6FnDBd2-Qh-uoL3y1gkKq6Ltn2UTyqAxJPuIcKgXzFKglswtUj4GJn7RN9OThO3CEeLZPlU51y0hCbC_iGyW6P0AYa2_m13ULx7_HFKKEOEiqq6GHjRvED24UnMNK-DDmxWBPEQTyOwkjPcUJeYsRZ5b9uDUqCBGOKANMu6nYF1PH7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=VNt5x3xgKXX1RW4iNLfR6W6fZHjpyr0Gd98v722MgvfrASVEtmxJWWwueZuSTLNprSlTg2awN5NNl6zN574E7GtgFl68QiJfkDgJpuuIHR-OtrUKUUHTSWKdcHn8EEmlKvUa4OZ-WociFoFSwwogy1IYzfgWvlonz6o8vF7lWT57alXR_v00AdwKMJlOW8RCoM_fm0IyPnbi2HZzS2h7y45ejJcWk5id65tAB4ZZWmu9Szdiwn5miOSuMjeoSi3UcsP9rFVgZ2iYGt8EATShbONghXF5q0WESqfXFf4eLMReGxXvIMrEf0VWlRnHNTyNUQSGiNn6alEEHgLCDPdriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=VNt5x3xgKXX1RW4iNLfR6W6fZHjpyr0Gd98v722MgvfrASVEtmxJWWwueZuSTLNprSlTg2awN5NNl6zN574E7GtgFl68QiJfkDgJpuuIHR-OtrUKUUHTSWKdcHn8EEmlKvUa4OZ-WociFoFSwwogy1IYzfgWvlonz6o8vF7lWT57alXR_v00AdwKMJlOW8RCoM_fm0IyPnbi2HZzS2h7y45ejJcWk5id65tAB4ZZWmu9Szdiwn5miOSuMjeoSi3UcsP9rFVgZ2iYGt8EATShbONghXF5q0WESqfXFf4eLMReGxXvIMrEf0VWlRnHNTyNUQSGiNn6alEEHgLCDPdriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpBD93cn2bf9G62PgxLEinsk95Iz75ZJw79JCYLXd_7Fi_GXOhh1fcuvibf4SJJcGwqx_FVbr9G-yjkACCDfccAEoOfvLeY_QGgyKvDJUXplvxZzHthtulfeE1SvJAcztJVJDlRtJNK96aBDPlwi92bkMZgck-LwieyhZQ3JKetVdiuJgzw7yo6tkstpU_dufvKujyFViGZcP9F8Bn7qm0BSa9YGQLEcKLG3ij3AsGes1qTmkc0tm-BpuU432giF1NPVQQes8seJUjd3g9_CTr039ih_daDMG_2JvenMTKuF4lsnUOhpBVIG8QGE86WTlzuwqgFT9o9_pPr87O0EnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=nwb2IJ5Ofs-9c1_0rW7TAK01jH9e9Jk5rl9NPNcgrk3aj0Z1RV-3zydOKHw_C_vsbprWUzt0sIUQJ2cA1fUdzKxFuvJedSjxDemQUJ1Qj-Jz7ap7B3zAMlwvq4PhJvUCrSRuR0PEPtzHMRFotBPmcYy-GrBupOolf2ZIdrE88k5Cj5By0k9WxNNVXFhKA1o8l2KUduAR2yRySpBS2cwS_qoeQSUkALAxdK3Js4FnKJ8W911HK_YXZ_e7cwaKAF_zwiy4OUZN_nNBjBhivcyjLkNCeN4S3PUaQtLXVnLK7RjrqGnGdgIRMdegkLoAK-A420oOB0dpMb7FIOIG4pja7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=nwb2IJ5Ofs-9c1_0rW7TAK01jH9e9Jk5rl9NPNcgrk3aj0Z1RV-3zydOKHw_C_vsbprWUzt0sIUQJ2cA1fUdzKxFuvJedSjxDemQUJ1Qj-Jz7ap7B3zAMlwvq4PhJvUCrSRuR0PEPtzHMRFotBPmcYy-GrBupOolf2ZIdrE88k5Cj5By0k9WxNNVXFhKA1o8l2KUduAR2yRySpBS2cwS_qoeQSUkALAxdK3Js4FnKJ8W911HK_YXZ_e7cwaKAF_zwiy4OUZN_nNBjBhivcyjLkNCeN4S3PUaQtLXVnLK7RjrqGnGdgIRMdegkLoAK-A420oOB0dpMb7FIOIG4pja7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=iJrXjUztrkMYDT3NJlOk9aTxG9dFkDpU3-qM5aexCXJPura6358H9_jT_LvS_cDom3LMwOsoOEEThJvGFpgR0UWN_gF5HdQFWl7-jBLg4t-ziBoaZjUNM-zFCRvCiB7s9KkDt01fVxn0hkTIvp0c_nmrT4-p0BPNf-RbXOWvcLbBRBV8Y8hOwItp986vPrced4sbTJmFgOumxOCpGpBrhmTdx6PruZEY3tmYBevRTdrh-Gx-Z3QnsYrQiz2keOgbhHloX_1U-NI8jghLAxtjkBPuMvz9wyX6ccht2qoRWS9ZlrkFFugZcBmwGc9AWKjscBiMyFE5is7u-o6jP_1Btw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=iJrXjUztrkMYDT3NJlOk9aTxG9dFkDpU3-qM5aexCXJPura6358H9_jT_LvS_cDom3LMwOsoOEEThJvGFpgR0UWN_gF5HdQFWl7-jBLg4t-ziBoaZjUNM-zFCRvCiB7s9KkDt01fVxn0hkTIvp0c_nmrT4-p0BPNf-RbXOWvcLbBRBV8Y8hOwItp986vPrced4sbTJmFgOumxOCpGpBrhmTdx6PruZEY3tmYBevRTdrh-Gx-Z3QnsYrQiz2keOgbhHloX_1U-NI8jghLAxtjkBPuMvz9wyX6ccht2qoRWS9ZlrkFFugZcBmwGc9AWKjscBiMyFE5is7u-o6jP_1Btw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP2SHfSSxJVd04dsbL3wvtxc0aq3t2lsSU0d1dpUZ_qN7ZpoG5OkiiwIFizJEbEbQLzfa5d6yG6S3HKTOv-zD_xbeMsuglx8_eriqek1YTSnh9KMMX65SMWJUsnK2xqyC3B_DDhDoLE3uYbz_w9BmTpqVQuZ5rdGHr43AvNNZ_HtHCfWV7eP4jBR5qYZik_iYJGKlA_6GiAfLadtaz9KYIwmWRPar1O0J8riWhcGSUCSWVQhCmJJMsxM5IVO9eJ_-IA6b8o8Z5jAYajCp_Oou04us6ajLjPpiOYRyJql8Of1ROEugEvcMQR7Mv-jaZhe9mMcYfeTvbhmz85so0AL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=k6ybG0iHt33NrNMW8-1z0czh69I6hfPpe6FoRfPW4QiJMklTnaaAo8NNqatU7DJ-ELYcmcUWAhYssurVW2fo8kiY-zXJdcKk3kITpx7zSN7Qh4vnnK3uLWNmIxd5Gn0yI6jFjH4Oq9yKJvyPvW4LreouWGiSEJot2x1HSBzqg_MQzmkTdiWTqXwCpa2LSDFXpyUrYjiePTBHFrOnCwdija_IzeF2PxJj9ahZqBarBwNqsRYjxlWgA2ikkYz8a-gpKvpTtcMFmZoLRYfAJIfiwv4PnLG-i5nn7NaMr_TKlIUYiz_n_KHlKhgKWfXnP8H_oHUS26qmyeh3SwuvgHq6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=k6ybG0iHt33NrNMW8-1z0czh69I6hfPpe6FoRfPW4QiJMklTnaaAo8NNqatU7DJ-ELYcmcUWAhYssurVW2fo8kiY-zXJdcKk3kITpx7zSN7Qh4vnnK3uLWNmIxd5Gn0yI6jFjH4Oq9yKJvyPvW4LreouWGiSEJot2x1HSBzqg_MQzmkTdiWTqXwCpa2LSDFXpyUrYjiePTBHFrOnCwdija_IzeF2PxJj9ahZqBarBwNqsRYjxlWgA2ikkYz8a-gpKvpTtcMFmZoLRYfAJIfiwv4PnLG-i5nn7NaMr_TKlIUYiz_n_KHlKhgKWfXnP8H_oHUS26qmyeh3SwuvgHq6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6qYzimIT3nv0ja01jIdYHLi6EbGOaiZlQXfd-UJ23oFcdbdIUlDNnoTlG8aDMlsmk2cKiepInQw7IkUcs37LKcmn71OpbqqKAdBd18gcWv5GzuywezydbUnCMwQsY0ezkIx1xt-VBCates_gE3ONpfUGA8z4uI5Euoil08eVPe5oK7erHqTc__tt9T_uxEg3X2645T6q1tNrlgYdQFUsTjTtfZ4lZm__AZZyQ-43ueDJjYaW13_vwwlFUdWQ1CIJGmF2FmKcuinSc6bwJ3GQHmKFzTo5erMSZnwMv3sFatJQknPbA5HikBnAfn-2Ugk-b9NGaKwppSAOe2UllpJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=HEwiWzvNixHSDIFuC5wV0bf1BB_MIj68uiOJhiDyIUzUnnjGZB1pi0b18PFc6tFK9E4MMIcPn3wYHBcBrIAe5xkH9J9mFOj-5PufBPOwgNKtARQIaYaMQlMWXkzdWw7j6t5HPwd-a56_vwpb0PSsucadZL93njTh8m_CgZ7wTN0wtPejJ21YLejtaDVe51gBFFmFQcZy31vPF_tW3TNzPfYgwGPxCP3SdE5BXvmohKYkxhm-NorfLSOncTkEOgl86HNJxmei6Xi-1Isi7ep6qRMWylltFpuClFiKqowZGIahc1UVLKcemvOe1WX6dVmFHI3uM3B0MJQgij5XIBjrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=HEwiWzvNixHSDIFuC5wV0bf1BB_MIj68uiOJhiDyIUzUnnjGZB1pi0b18PFc6tFK9E4MMIcPn3wYHBcBrIAe5xkH9J9mFOj-5PufBPOwgNKtARQIaYaMQlMWXkzdWw7j6t5HPwd-a56_vwpb0PSsucadZL93njTh8m_CgZ7wTN0wtPejJ21YLejtaDVe51gBFFmFQcZy31vPF_tW3TNzPfYgwGPxCP3SdE5BXvmohKYkxhm-NorfLSOncTkEOgl86HNJxmei6Xi-1Isi7ep6qRMWylltFpuClFiKqowZGIahc1UVLKcemvOe1WX6dVmFHI3uM3B0MJQgij5XIBjrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlLAKh-G1V5gF2mr2Xy43sSyGaIM8_1IBidEUDty3bmav5j4WSIILANJOtNqH9jR2cfPj-4LqP61HX1LpXfZYVpcWG035ikRhAD9cCDIdohzqC8lFiR3SBB3MDw2PzUUHLF2_U5afVbWn0KLIkhqGWvSl9C4zg8wq_X20bE1JI--0-xf0Zy-nU6e49FJLETk1it2kjWEnUTdby1xFkGotYQl5lQx9hBeEYB6_zaIJNODSgBkKRYYrigbWbUSlVTHAyeqx8Xnj8V4md53l90DKBG9D8No1FLgB9FBV1tzpB_wls48UjMCv8gVcK4ca7pvPTtUL13uEDp5S3NAhrtENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
