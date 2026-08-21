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
<img src="https://cdn4.telesco.pe/file/K1Q7InIamLBBnSSWjBaILyoQoDZ-Ifei5BatYSMJWLDPVXdffWvFCwa8ysFSGAnyMSdrbmw_LWuCSYSohxM1IV4O5h4AvMoQaQpNWE3YwKPIeAHr28I3W5qx4DCfHbHBQluebc88_0QLWkxh_CxkNf1s3zG-H9VCUKFYCiP4j_eG7_6IvAKWSUZiy_3Pd_4cEcNegw1to1msH8qyDqacK2_DoY-YOUVeB4zB3Si8EArtALsgZkozwrGnQvOS-p_9ePT35Bsl3hZ8UhARwLAbh5j1Ez6IRT1i1_0K0t3hCuf_dRcxs5BRoGbHantjX49xo1n7Sua65avT2-DNr6THvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 21:59:47</div>
<hr>

<div class="tg-post" id="msg-28206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaBVStWXvjb1I0VjjO0W_XY2e9Hooost51oghTff9hVAz5RPPb0bd3wYAnPMU4RxScknpHnODivZlhMEN8ID_Jn4rsOWr13UbV1o4oGADu2h7UjQg2jwYm1Wimd_QUPrrFYFWVJAC6uzSxcSjnHAdnX3I-Sg-1Q23uwuA2jUPtWo-_9xfTelVy14JC90OTQXArmnspYtMKpeJ9mvXiT72WbTUzGZf_mA3eH3_ZAJJgKrqIMaHElWPwb56jc4mo2JmneouapajkjwSH4X2Mwjp4addsSvcwBeE1ZB4fmA0f3SHnh8Sfwir7Rm_PwptvqgE6jxKpc3GGCl9c2K52ihPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/28206" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1EInrZcHmNy9lYzRD3FEQ2UVJeyLZI_rtQ42NGcF33UIidcEAXsC6yofx54jMEbb1cAL0QVAyfibCifiTaFn5_7ZHtncB8UrVPmq6CzBBTzfUXbBXa7EcSxHvhtK5ONatOt9kybWcm9He8II3M3e4zHlKvBXqQ7QSZpK99VkNJ8a-B3HX__K84GbEGmQrlfXghxaXrP2cxqdu55zbwlMo8FPkNt64rVNqUrI9TFRY0F4fFzbkWZcgYPOcCXMNTDMs_WqAaFfdh6WxSzdvZWJsAxhjhD-O4DqVHdQ_tAc9q4H4KOAtjnFRgsLmUQ9DBG7CAgZzqxZOPTmTZfKWZRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی طارمی از لیست المپیاکوس برای مسابقه این‌تیم درهفته‌اول‌سوپرلیگ یونان خط خورد و عملا از این تیم جدا شد و بزودی پوستر خداحافظی با او منتشر خواهد شد. مقصد بعدی او لیگ‌برتر اماراته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/28205" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvgVoub793zwUcTtPrCjcARTr3OoYxhAgj7HQbcZIVijq-MPx1M5VwUwAEb3-ZOT5GZmWOQBa9LBaybAP3uH1PaPJsC4ZJqPvo-f1DmAIa1a9HvTnhW9wC3k-E-Qs1RE28M2ad7JCJhMNegz_H7DSEbwCkN_ZIY4yrIt1TYmOHV26ZrBGTV7n6iCxpEE8Y-ys4CQfGwOazAOE9KAjj3t1WNRRV74UTqxbdp5gz6WshGzX7Wn7AYMLrq2Fjql6LYFiaYFdr8VUyzql3mW4rAtQEj_c8OyWiQ6GHAnNtienD2wOGtTIGPWABUN2HqmW5aLlDzmXU31f_jHSe-Hf2NmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شروع‌لیگ‌برترانگلیس بابیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
مارسی
⚽️
✖️
⚽️
استراسبورگ
⏰
امشب ساعت 22:15
🚨
ورزشگاه ولودروم
🎲
با شارژ حساب کاربری و پیش بینی رقابت های لیگ 1 فرانسه در صورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sg30
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/28204" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6923293dae.mp4?token=rJqjfMWUJSvPL3nC2-MdCgleEijRU-6ryQK5JlEUFb4kjVI8Vaqge7ROU6l-SvKOhkPS2zyphnG0ijBpvsM4Vv8dZN4x4J4b_UKeraDJ3DupJA-wC2oyQPmA34mtv5opTMH8U8Eb5Di0Bi_KH4PENRaZYRugn01Ej1HPGwPNJxwQBWwel_ED2OgbIbDJnFseXvSLPh6X36OHXgpHPZUD6sv99U3KC6R-7v_FuhIlNQO1TWbkqS-iN8Oy3UodTkbmbtdIZqVP7ySp9_Xx6XoC82viYGNqsBB-km5F_wj-wJU38MIQUQrZMQn5YMQs1vSL2b5-cjAnaypkHmvtiBDwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6923293dae.mp4?token=rJqjfMWUJSvPL3nC2-MdCgleEijRU-6ryQK5JlEUFb4kjVI8Vaqge7ROU6l-SvKOhkPS2zyphnG0ijBpvsM4Vv8dZN4x4J4b_UKeraDJ3DupJA-wC2oyQPmA34mtv5opTMH8U8Eb5Di0Bi_KH4PENRaZYRugn01Ej1HPGwPNJxwQBWwel_ED2OgbIbDJnFseXvSLPh6X36OHXgpHPZUD6sv99U3KC6R-7v_FuhIlNQO1TWbkqS-iN8Oy3UodTkbmbtdIZqVP7ySp9_Xx6XoC82viYGNqsBB-km5F_wj-wJU38MIQUQrZMQn5YMQs1vSL2b5-cjAnaypkHmvtiBDwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آمادگی بدنی فوق العاده کریستیانو رونالدو کاپیتان پرتغالی النصر عربستان در سن 41 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/28203" target="_blank">📅 21:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXVbC7FfaRchZmczuvjmUJo7ArFhsEyRygbr7IcsWeO4WB6EiI5QthtE8SzuUviiVI2IiWh0icyJS6AUKVbs1VDfL1TCenU5m_-x3A-dGSGqRX756l3aeMrleFi24WZG0yhBLBQ2sqHXLeqPi-agYXQePZE2Tcys5f44rPpnKQ9qrs9aSb-PLUY69fpSCqTxFFbC7jT-N0EY2nIJnQxSNHZliHzPZuS0L2D1ghP4FGyOh5vhMl1rhFJAc1pVbeCS8gCvxmKRS_-TRSTEDUhFpuhOuczExEgOKQtUIrK_No0batsQEoTSzWvSZjT8efN9VRIjFX3m5uRzW6cRg2LiUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/28202" target="_blank">📅 21:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McRWXVJEzxp7w_tBBbHvrjXChMLJ8mpkI3JaNd3WP03z1x6bmo5gZFVtzcynSVeRxRihNW5EUj2_5FQnw0Ki83jOjCykytnMJBTdbI5o0t_19VR4QfqXISuy4T_n2YV9k1SM6Ip9GoXqeYjpqR5WSrU5FJ8XqqPHNnc97iXd-kmqhdHJYSFKtDIhFGgvysRSo0w-dQx69xunQNozIAmpyG-GludcGYMOgzNb1U3nuJQ4fy4bpxHF00Kb-Ai2wU1fPrzDigIQBE_nDeJp0kY0wgPDdwI2V8tAL1Eso8jWlhzqK9xGV1C1Cca5YwF8ammUwzlC19G3QYN2a3xPcnOsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شروع فوق العاده الهیار صیادمنش در لخ پوزنان لهستان:
8 بازی، 360 دقیقه حضور در زمین معادل 4 بازی کامل، 4 گل و 2 پاس گل، نمره 8.3.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/28201" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoYHnF4zpxRYBR_nZ8Ksr83EqR3_O_flcO-8mlqD-PMtWSQtawSyQYaL3309pJJA3OV-0dQUCfckt9xqSrh43mwvlaGsf_0GHtgcsTBQ24_UJoKcRyDmVWlfK0rsadoSWfuPZ-g6tz71EdUzGcgizenyhjMAs3BX4JBdj0s7v7seZIlIza-ooGgnazSBEUpGkmbwwH7Ye_HjNxsjGG6ukEWxoRfGZB0u75W5wPRydnAlLuq8hauy1ZzpImjGUbHMx69qLzzFZg9KWx3BsVcpsQ-2ijhOzolqLywRIwlXU-sByWchR5clkUewHWm_AbN9r52mja72NdZwGMaZz8gaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/28200" target="_blank">📅 20:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3847125faa.mp4?token=NKO8AZ3fmlj1ZglCwhDPRHhif8ZV6JtEj-NT_SO2XAbtSnvLf0HQIlW-x_mnvhTgGvHhFaa-EZG4qxSVwcD_zci-D4T0ss_02Ml7sSQkmZi_kFvH1pezY8kCWKGZhwSep_NXHxgHnZFJC7PaHF03d-XDvDsySxOGSDJ1QTAQIkhsuCkEv_emVMKyshg8JK9h43QWw_5Bem4S-CCVhjvQ81MxYmMFby-b040OpO1CZZThNkLaMu3ABq30TN9s7ley94PTZEUtUY2sWrsD4fRyUA3In4M6zc-LTSwB22Ncupz65MXyL5WbzfKMaaIvnMhd88dnd6kHAQy21m7AZequXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3847125faa.mp4?token=NKO8AZ3fmlj1ZglCwhDPRHhif8ZV6JtEj-NT_SO2XAbtSnvLf0HQIlW-x_mnvhTgGvHhFaa-EZG4qxSVwcD_zci-D4T0ss_02Ml7sSQkmZi_kFvH1pezY8kCWKGZhwSep_NXHxgHnZFJC7PaHF03d-XDvDsySxOGSDJ1QTAQIkhsuCkEv_emVMKyshg8JK9h43QWw_5Bem4S-CCVhjvQ81MxYmMFby-b040OpO1CZZThNkLaMu3ABq30TN9s7ley94PTZEUtUY2sWrsD4fRyUA3In4M6zc-LTSwB22Ncupz65MXyL5WbzfKMaaIvnMhd88dnd6kHAQy21m7AZequXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهاب زاهدی ستاره سابق پرسپولیس: قهرمانی فصل قبل رقابت‌های‌لیگ‌برتر حق باشگاه استقلالست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/28199" target="_blank">📅 19:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=azhb0Ij3iryrDp61nDwbrPl_okLw8b41hqpCI5dgfjZVaWMbENX-Gmx8dPfAHmxzpaBDqydxAq5Hg_jj9U5QF0P329aON2J3gFA_yreCnqlnwHbBn0aAFH8lPvQvsg7nbZs7miendk9zvcRjJ-2SO7x5aa4ZhzFygZvkbztAS5juOfprJ5_w-0J_bRvWzDxiTWRgQN0E9ouMN8Wti3qfLg92nFAUHkb0uI39z9q8A4UgHyCyF41_kzyrYIvHIww_5nIcRcDZbOFi_CO1QyHwWuZJSV2rL506p3tOmxxpnbaT1-ZAYVURp_FHDT1rEZaZHnGQ1OUnUdCbkslQVX6hfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=azhb0Ij3iryrDp61nDwbrPl_okLw8b41hqpCI5dgfjZVaWMbENX-Gmx8dPfAHmxzpaBDqydxAq5Hg_jj9U5QF0P329aON2J3gFA_yreCnqlnwHbBn0aAFH8lPvQvsg7nbZs7miendk9zvcRjJ-2SO7x5aa4ZhzFygZvkbztAS5juOfprJ5_w-0J_bRvWzDxiTWRgQN0E9ouMN8Wti3qfLg92nFAUHkb0uI39z9q8A4UgHyCyF41_kzyrYIvHIww_5nIcRcDZbOFi_CO1QyHwWuZJSV2rL506p3tOmxxpnbaT1-ZAYVURp_FHDT1rEZaZHnGQ1OUnUdCbkslQVX6hfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
بازگشت‌عارف‌آقاسی به دوران خوب خوبش؛ اعتقاد بختیاری‌زاده به عارف آقاسی او رو به دوران اوجش برگردوند. مدافعی که دیگر سوتی نمیدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/28198" target="_blank">📅 19:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=U2sI-QVW70mvxJIiqFLmObP09U44qQmBeuoB_Qh3I7TDsCV3rbnRHiblRCKGAlORhFi2MzgciSsJleMj6IPwpiZq_oc9RLMmCKRxzWDJovwAGU1s2qbqoOewwkAiw1kgTH1bDXRUclx_2M2fsFLdnQbiByBYHCmQHZIpHmKgJAOM2UQqY0zPBDUH3AdULdPy6B8JrFdPFBOtzm5WUW6N3TP3I1pCmHMshfiKMNYg_szkpRCrgJ47oekQRl7R8swnJdilbI0RfFONLro1z32m-5Jat0pwuQEbkrc1SPkb1OaLRAjVSdaNwdDS0PNCX38uG6CD4rQPSVLM1RGVUxhK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=U2sI-QVW70mvxJIiqFLmObP09U44qQmBeuoB_Qh3I7TDsCV3rbnRHiblRCKGAlORhFi2MzgciSsJleMj6IPwpiZq_oc9RLMmCKRxzWDJovwAGU1s2qbqoOewwkAiw1kgTH1bDXRUclx_2M2fsFLdnQbiByBYHCmQHZIpHmKgJAOM2UQqY0zPBDUH3AdULdPy6B8JrFdPFBOtzm5WUW6N3TP3I1pCmHMshfiKMNYg_szkpRCrgJ47oekQRl7R8swnJdilbI0RfFONLro1z32m-5Jat0pwuQEbkrc1SPkb1OaLRAjVSdaNwdDS0PNCX38uG6CD4rQPSVLM1RGVUxhK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
میثاقی‌مجری‌صداوسیما دیشب‌از پوریا شهر آبادی مهاجم جوان‌پرسپولیس انتقادکرد و گفت باید میرفتی‌ قدردانی‌‌میکردی‌ بابت‌‌پاس‌گل دیدنی‌ بیفوما که این‌حرفش‌واقعا درست‌بود اما آیا خودت از عادل که تورو بزرگ کرد و به رسانه‌ملی آورد تشکر کردی؟ یااینکه رفتی شکایت‌کنی‌که پلتفرم 360 رو ببندند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28197" target="_blank">📅 18:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQfOvvTAq65colWzC3_Ttd7pDuFrTwhT_lpNMc5Gie5BsDe0Xsal12FDgTN96KqEu1m3W1XEKmgRin8-1JQOdWm2K8GugPu6y8-_HhfMnztcygKJ66gdkA6mag-GU1FkiEMQ-yfHxo8RFByT9WL6JIee-KoerdDD_t-M2ZHtqKO3IHTJelBzl75GVcqW63fEBs_5JD0oRGY5NCljFpVZ9ObxbmJRhLb-JlEJwbBNfZ6ngQGPC4P7R0CtRCmtTfnj6FGgf5JkFwB98t-Vx0TMGavNcIzbT5-da0dTM5fu_VGC8a5_BQCfsU2Xo-C1PqWE7iVfql5IQDh6kLhuS2btwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkwJ0DAR4ELP-rQUu23WW1LRnpgv3JHYm_ZPkz9qyaYUpa_kTRaseF2y8KrtiUt7ZNYOEd1Aw0kNW927kD7Bx45_iY8_buYGsveepBPbBCOONaaP7Y3nAX45L_4TcHBsYRKPXH7fa7TJugTTjdnn14YaRYYEV_542bsL_FOl32nPHkS2qt9HE5DMnQLsP47gLoAm8v6cmI383pAycVwkT5t3Q8ptRwm6hFb6ZFAeb4eKIqocaRjHV49RCoVMG1PthaoGlthNQblYFuHg159t2S4i7xRPT2O9KUc6irZzdL23B3hKYhIBfABeKvl5JoyE3b2R8X7ACd4D_d00ZQUaEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
علی‌دایی اسطوره‌فوتبال‌ایران بمناسبت تولد دخترش کادو براش BMW X2 2025 خریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/28195" target="_blank">📅 18:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHKTt1ndTDouVW3Qk_coNBJJOGBHWcuetGjYBTNFAE2vgitw6rQHjxlePRexmU2EMcmpq0UsCp_ZYJlGmTxuJFFomstGdBH52fuXkTuJR88TSWYGKkfBcFy7QX8ZCLx7B8Ralq3zZfYx_kmE7rfhJf7_WIxKKqRClrcZY6JqlcMHgcckO-PwlbxBLWwdUUEo8iN58Dljnomnv4pcYW_Ihh7RZc68YwpkYbBVpJsJxRkqFijUCzj0txDojHn9X17yoJeFEdgvuDVbny3P7iFB0GIuiibPM_5t-eca8-SZVg-_2NNa02NrM-Vbh9A1qaejjqiKKHW8Kre5N9JNhTtDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛ بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/28194" target="_blank">📅 18:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBaxdqMx_8x6bsylUF1nI6CWYYeEb-Td_KrjWEZZbvyfEwXTFwxN9w1RpZgAqKzneqAlVJBvlqDmjLII2ED8nin9DUDVdpo-OR23PLJqUlhgqhtdj2rq960WTktNj8RbEaEGdJM80lJvP5NJrOFmtOLw6TXpPRddlZPPy1T9Z5w35HnpBkxCMumh6g0JHbCjlc2WiavI5rfDXkqbIUoCUOIHfaX8D-S4UJagO_gP2ZznxFhB_VbqKVU4eHUu0TL3WWfStVMp3xyPU-6CzzZ2XGJzTCA0F3p2aGsO0Rw-H5DjaHfEe3yp5q5YN4P_rUanQtHNGJ8oTOEott4lzntl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛
بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/28193" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDgTi6feIRv92wVmHRYFn2UyKbTz2HUt8oj0cXgEbLG-WXUBkKeRKkpdeKhjDSBrqhxrG_gKM5mcrwLaFqtexXReiIcAhW3pM3VFemO0XodqjLelc__V7lwq82P9r5nrP9EpZAmPu66qIO-o5-VjjKHfgm0kIDE1a2lWVW-tGGwAbazu39dTXgQmJTH_by2U1HGkbmdP1LAp2aQAWh6EL87KTk-NwbQ7Hxya_NChWipFe5CrMwtnqhejP_evgGVirgTn802P0U1vWfRy5mFA9-JLYEqq4j0C-i4pXz3n9C4scB49keaguJrlpRo94tvlXVfgixdWn1cnWVVuOpgtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28192" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz2J5yQVfoM4w-EGdL29ihxmWXpLLseG-zb7lwx9haKGK5DTeaTCIVOEplqmCWEzh9bf3Q4323L4yQlsfqrExlqD3Zhpx51sNmVCx7R1ntB3voY4zRCOdTceQDGN-B-IHp29s9k6yRJkIKq9Q8Mxi3EnHnbf1sZia35U1ZIv_Fb76pgopurtMuHBUrr_Y8lQTtPCY9-GxrOjb1E7UChNkzOiEaU8FhuOiCK3XnLzk78PM2gQr5gjmMzC3r_sXpQ_zj2Rcaep6e50bKCJCyB1KL9NpPQURXuIoNtLgslga3U7-iLhDYAP4dpk2NLieH6iqcuecT42TWx2mYYLvu3EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28191" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMH6vRwilc5j7CNb129dytmEK5VBn0j7ZZFwI7Lf0za4TSwCAw-UQpsrQhcLm-XMe316Ab8DHXPuE_vTq_iJr1DtYgkzZAM7NIwOHnNg3Lhoz_jIaSErUpP14c8YbfNCi4l0ay4vlUIXRy-obZWvMUNhnyng1woHyA5JEfTW8YZ4NSUNHPF5OwuP5P7MsMpyJnDnMVeYDwEKIdwh6IWhdrwPIq8ChuWWLhgbuW2UwVCDTAjQ2-NnJ9wGX-ILxpJyRS_hSEFNajdMOYRplDql6P3rWM2JN_L4zz_dKGqXEkHe-NKi7LMveE7DT1IcCktE_R2IJYbNlaw3DOzKtQAsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه الهلال برای جذب اولی واتکینز پیشنهادی 45 میلیون‌یورویی به آستون ویلا داده که به احتمال فراوان باآن موافقت خواهدشد و این‌ستاره انگلیسی با قراردادی سه ساله راهی عربستان میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/28190" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=UdCa4XFHZqqSY05lMcr2TP1akoXSugUcwjmlIHv3kYx5bmGnE2RhTLmv_BetZ2Ii6oaPyZCJNnOcaewPPyQoYmuewy9oYSC9ZdajkE1NQqe1QazMBsbAyld4rzYJyNsCN0En4aSnlB0XPMhpW9n5xjUSDcZyEHPiaKF5DZIppDjuybU2hPDXYuomRPciXNKRt5st2AsZ2DjH3ieyfgaXRuFdN1tzq-jwaano5c4HOX4jHGWM5urwzAvKmMysiMQABHGMmAITAr66qrl-aTGEca7cSk9nHsNe3BsWRdLAIhDcpEOHJw7RYFUOTftzHhggE6AFlRvO9yoDOwGAdNCe04Jw1zXeAflHM6KlgSYDEqd_X8opSRXkV_SN2dePzt_8uE7ZfvVGOj6wPScZBaRtRnqlCrbK_RpPtJLFG7kSWV8tKoHwl5mJCSnFbEs9UqPUDe4c_cmyinlfVgJsOlSVtz5cBdkRvn-GN4gdK83lbsUtrDuD6IAH3kxvfacIimqIRjY9GGU2wubSjOn3O2XI9o4cL7p8PATSZWBTGWZIc7-G0Te6Fh_Gd9VZQFLuPnV4FsSUUsuitweu9-rzB6HpiEbDZI5q6VxgB5heRts0sCW5Kv8MRcljqnMJ6Iq21Wq7DOB6it-ChrPn-SSGfnP7mrqiE9p83VVBzTQ047hap2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=UdCa4XFHZqqSY05lMcr2TP1akoXSugUcwjmlIHv3kYx5bmGnE2RhTLmv_BetZ2Ii6oaPyZCJNnOcaewPPyQoYmuewy9oYSC9ZdajkE1NQqe1QazMBsbAyld4rzYJyNsCN0En4aSnlB0XPMhpW9n5xjUSDcZyEHPiaKF5DZIppDjuybU2hPDXYuomRPciXNKRt5st2AsZ2DjH3ieyfgaXRuFdN1tzq-jwaano5c4HOX4jHGWM5urwzAvKmMysiMQABHGMmAITAr66qrl-aTGEca7cSk9nHsNe3BsWRdLAIhDcpEOHJw7RYFUOTftzHhggE6AFlRvO9yoDOwGAdNCe04Jw1zXeAflHM6KlgSYDEqd_X8opSRXkV_SN2dePzt_8uE7ZfvVGOj6wPScZBaRtRnqlCrbK_RpPtJLFG7kSWV8tKoHwl5mJCSnFbEs9UqPUDe4c_cmyinlfVgJsOlSVtz5cBdkRvn-GN4gdK83lbsUtrDuD6IAH3kxvfacIimqIRjY9GGU2wubSjOn3O2XI9o4cL7p8PATSZWBTGWZIc7-G0Te6Fh_Gd9VZQFLuPnV4FsSUUsuitweu9-rzB6HpiEbDZI5q6VxgB5heRts0sCW5Kv8MRcljqnMJ6Iq21Wq7DOB6it-ChrPn-SSGfnP7mrqiE9p83VVBzTQ047hap2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
جو سکوهای ورزشگاه پارس شیراز در بازی این هفته فجرسپاسی برابر صنعت‌نفت آبادان درلیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/28189" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0qLna2wBy0MSNY3R_m8rb6oPwj2FArfIXyK4o-2YEg1WJcggqp6zUhyd7WUPsaxSQAlAolVSiKDythZepPYm13sU12HSj_DroXEpED-rV7Q4lpmkgdYf7pGqDmoL-2uHLmkunURDD1GLWfbqHAr9bTyyklWkY4lRvIrRjFgQTUnLr4CdPvnKlwczmVNLYZTP_R7yTKk2CJPYTpxoSJ4dhkz7TVx8QnuQm9Mvoth3Pdo8wKohswTbnHRyW5mhM5atpoBgDlOgAws0WeNKxTS76CuqEfqGz0pEMrV1_7qumZlyTEw3d-ay9HqcGcgJxq7Mum4eqNSFTo5lxxMPyxHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال سوسیداد
🇪🇸
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/28188" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phzEnV_t3dbzmzf7aTt2sGy0jY_4tdRbOir1MqG_wz2juOUz_RaKxasJZUfEfBWbSKnLOP_MjHZWclmJLdIfJooSdnf5STwFa86FE8cgfI_KbVjq3N6sIaqnfIhmPLDOo3yiglYe3RceHF9dnwFSwvdXVwqYLAqawMOvj6C8UjNZHhUNba6bweb-bNtpARW4pwts2GZciFlgxBCVARcBfs3K9n7n_BzdRGI9zqSfIOlSk-Uo8e3cKSv3CESzJDISpqad8QUh8iTseC1JDhLtNH6-elcMvSV3eMquGSqof9sxb30uXWQURWf297_D9Jw1jDOuOiXEmfb5TSMnHRjujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28187" target="_blank">📅 16:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKGMqpDPBoEm_05xXJm1YhowD3X_3ptyZApsUMMB00Aff_z47EMBce7U-zWh6gDepuJSyC6SbGEaOf7ghouTixUMxMefOiP1MHiVC84JhDZY3odss_qnYIS-2BMS19nUffEsiV_OfhsI6eivk5qQM9tJlaJ6xL8eoDC1m3DfsJ-rSccLZ4PoF3hEnrXAJTPVBR7zId81mwC_iOeWhu0i6LLG-qa5K3DKchXndErCML5Ajgy-ruY_WphumdQBNDjpr1unsgp-GRqb1zdowE3ZPEgtDSFtz0hKEC0-pkLPYqYt0iwQpR75znvXUolItWqtBoN0sOaDQvf_-Z2r4FxZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراپیست ریچالیسون رو یادتونه؟
از افسردگی نجاتش داد و حالا ریچارلیسون برزیلی این طوری از بانو آماندا خواستگاری کرد و آماندا بهش بله گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28186" target="_blank">📅 16:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrlLNnC5meDhEo5j6bEGNVz2MFiMGhXstVgqGhjDuRweYadN2fohJ-qEJBnI0nc33acdvhRgzLiEM53VHa9ReeDg0oAG9j_GyitRZ8fUqoPxypQHUVi3fiLN0Ur27IPv66ucnHa-mbUSbyXo8WVY95ittW0y1HPUsovS81Tv96ovmKPTKC8rZe6Fsh6mQFLURFwpCel0FNjP3Z57azXGGWwiF04oVWcFvPsgx8uyP1VCCy-hkGynrkOPgR4W-ShyVNecGZwKD5WzKn1qU1onSMq0IO3AysoB5hRg8i-IGIBo2NGbzFrKj-IWf17WnOLigl-y-Is9XOxWJnhWPV-oEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور مدافع‌چپ جدید تراکتور به دلیل مصدومیت یک ماه دور از میادین خواهد بود. محرم نوید کیا در مصاحبه اخیر خود گفته بود که چشم تو چشم میلاد زکی‌پور گفتم اگه تو سپاهان بمونم هیچ جایگاهی‌نداری چون زیاد مصدوم‌میشی پسر خوب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28185" target="_blank">📅 16:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7c_h6BOFH4Pka4yfleFLvbzW67gDcTRuY9meFZ8tedEiWwH0Uf9iyH1wUFw-j3chz_bsLClFYtEfkL_YrpLLYxfW-ientRrG2YmFoVkJ0BUzxU8YQltdxTtuNGMj8bt09_qlLQAcAOR6UiXefNqJNr5UnB6YhC8pgfmLoHeRPfSRAvN_2TyBb0AL9s6X5jWAis3mUV0yogp9M3SzEYhgLPt9VUPSSIFs-RTI15p_FR7e0xtdKCCWr3Uqn3liOA72iU47W5EIS4EYqgJLtKvTm-wU7tdpUM556hw3x44he_RLeJmAV-ea6NxTjbLvt5OlNaeTx8jACQ-nmM_pFRwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
برنامه و تاریخ دیدارهای دو تیم تراکتور و استقلال در رقابت‌های لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28184" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHSCXnFzWwA87lSFlW3aDxrT6ZNgY7A7e5GLyzKbxUw_kDwbJuR3Yho1S_J29elU5qchbzU62TFZ-M230JJ0F4E8JcHoJtVT1OhSPiMgxCTu2DtTC_qi_upzN1Y6dhWFQLk6mzxYXO4zibqve038crWgNZ65I-aM1H8Q5U9g8SoXvLdNaer6yeGtJqw8bmRY4q0UH5OKXXdIT9sVK9J3PMzL0gAxm98iTlx0veTu26IERj99f9m5wF0uGoA7FggD20hNL0vsBq-p5mtzAh9HH1BemkWXU3nr8QEQIkkj5yXtgKm7k5Fu9i2TDBVdN4JJC3B_kj-K26Ut0LsmXmwoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ادعای کارلوس منفرت:
دومینیک لیواکویچ گلر فنرباغچه با عقدقراردادی دوساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28183" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZGcxKp1gIXi9jfjANheA9CtiqIBazWtSWxjT5myxruqSpPapVKvp-mbRiyquCoR-fIp2gCWDi_fJlKUKfSFpHTEhs0kq_f1D50UxQJ_tKO8t-xoksOZ15LSwKJ7rAv-Hs7CQYMpcUQdODA1krEuNDsnHM8Lh9Jxw1vJ2-jh0B7EShci9gYIM_eWPoahHf6D6_nF2L2UfMwpNilLbfAwzamoBUz7E-BfeScDA3CEjGNyFnUQpe3qe9FDXsdF1u54dR1gzIZOb9BZEfNXe96QyDcEIgN0OBMJtqpTj8RzqzR4zgWuxraaPMqkZi5gG64I3dC3JnHorCQuG7l9wb2MDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس پارتی هافبک‌دفاعی سابق آرسنال با عقد قراردادی دوساله به‌ارزش 3M€ به الشباب پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28182" target="_blank">📅 15:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saQy3Ts6H4UEtu5zr6mONch6YrZV4CDYVHTYmmrFNsuEMV4QAHWC_uHf6N9pQ4WxMS7k0JeYQ3aG35Y-o_jBEoTlShcX-2fdvpcLMAdmO2R-k6HW0f4aLT238q-Zlu9TiUQWmdiMl5sT_zRJWNfdHmlvJM5NQgd-jGUXJs9rGaS6fpPkBZE32Q_0acOl9wZhaV9gl21dzAPfGc_NQIf32JTCtE_ZhNgmTNhKgAy4Q0s47tBlMsCVbRDFHVBYeApP7_5F6jDEntx46vjOEqJLBra3s3elQHfPLVHoCkaedIWxfKp5xF1MBM43R28MnvXaMjyWL8yMD_desDrkkBJ7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمد حسین صادقی وینگر 21 ساله پرسپولیس به مدیریت این باشگاه اعلام کرده وقتی کادر فنی اعتقادی به سبک بازی او ندارند قراردادش روفسخ‌کنند و رضایت‌نامه‌اش روبدهند. صادقی بجز گل گهر از سپاهان نیز آفر رسمی دریافت کرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28181" target="_blank">📅 15:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28180">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlE5gRBRJCFPLCcG9QTQ1QjyqDfQCeaA2ahhzaZ09efzYLgfon-bzdm9FG_CARdgfJki05zi9n3jLQhnsmfnScTTZG5ZxQuNuO7RIldk7q5JNadCmdETkPDPn4aAxzN5QUhSXvevyaLnw47osw0rhxOb1Dfl7inC6OZHcLqdjs_kOVnrpAgNdp-VNoB9mBcEfNQJGJSA_fmxOHOrIoJ-YmleYV529GBhQFmtWofj73xL69RuzJe0CZa1up6xdKUtGzoMfrizYWIgH1MRANVXL_3Ym0ZMwLUJipVbGeUvC6RXQn3Pf4LTNMrIcSZKDzKPbPiTT2QaAusc4D9tEsBWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ شهاب الدین عزیزی خادم دیروز برنامه سه ساله خود را برای مدیریت باشگاه استقلال تحویل هلدینگ‌خلیج‌فارس‌داد و هلدینگ تااواسط هفته آینده نظر نهایی خود را درباره مدیرعاملی عزیزی خادم در استقلال خواهد داد. عزیزی خادم اصلی ترین گزینه هلدینگ خلیج فارس برای…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28180" target="_blank">📅 14:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btdjGjCcawOYNqiO6wBV7jlxE2DMUqi5yO5x15Es3ztJQguUHrLp7vD-tERXP4jgPka4yYxRhNtcRjqW3XJgXLsBBclRZaRkkCScwhPHDda6-dxtAGnm-V8OHJ8kXgoFjIKXONABu8k_uyuonPkMt5x5O1hBWKkdbSyYSz5W8u_QmaX4MFhmXiguCRzKsfZsrm1i1NZqXN7xyTHdJgzblJ4dIIO3vq8A4AypJJOtwuh4QvsiSpBnj9YuOoAc3lMPcApf3eF-Ge96n6nmpsgCIExgehc5PB-oJ_LqVQdtjLGF6ARbTL9tuDi6mBad8u7Rb_FFScRom-GP8zzJCuBkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcaRMKfhtBbnsrrTaZeLpWaTVBkFDhH3fg5cdXY86eePjvTeAjwnQ-7OXdwCROx1vEq09u_sMbpJCNeN6YWO3NfJc7roMrb91XC6TtmKxABuewKLAFRQ3-ssG1a_M7yMrW1hQ_nuuFc_8eUgHKVdVThiMlQYMf2yMV21oJxrJ_tibeGvzHCbHEfiemUmbXTJp-Q_AwVZK-iuskUf2ixQ0uigd4XZve7H5IQ8dKyRU3wG-f-gz9eUG6qLUMRVpnrLWSZlgEVs21nXEIxusU1K8S_8ixpLvHieg8BEoecBFS4l2zsaaZOdedeN7Rlpw7MHv2fR2X8BIM8TZKPkr88SXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🔵
برنامه و تاریخ دیدارهای دو تیم تراکتور و استقلال در رقابت‌های لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28178" target="_blank">📅 13:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66740b5afa.mp4?token=B8Naebp_OIWkdVukLQS3Dz1e9xYN4ffPJPt6NntMoAzCqf6FQ954koDSmXyDA1R-2TN9S30qZECS11QrqjcN9ogS-qhXPyC06q9SxhM7CAZc6tceesgL5_8ljjJoQ3YYXQXwgX-HMgxnJbSXxsKBVoEtiaR59oDsBFjH88JKqOegDyBUoCybBtEnd663KxEtROzRBe68-yyLBVqxK70fOwf9ZtxZDgBEY82AoBgYQv088srJUmwjWtNtgvjCfsFVyQc33SHJMN6-cmXQroGt2yICQl5xJbJtnadcC5FCJJKtkpgkBt1oC2SD4hF6KoOkmFnErkoL2LUYP_acyVY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66740b5afa.mp4?token=B8Naebp_OIWkdVukLQS3Dz1e9xYN4ffPJPt6NntMoAzCqf6FQ954koDSmXyDA1R-2TN9S30qZECS11QrqjcN9ogS-qhXPyC06q9SxhM7CAZc6tceesgL5_8ljjJoQ3YYXQXwgX-HMgxnJbSXxsKBVoEtiaR59oDsBFjH88JKqOegDyBUoCybBtEnd663KxEtROzRBe68-yyLBVqxK70fOwf9ZtxZDgBEY82AoBgYQv088srJUmwjWtNtgvjCfsFVyQc33SHJMN6-cmXQroGt2yICQl5xJbJtnadcC5FCJJKtkpgkBt1oC2SD4hF6KoOkmFnErkoL2LUYP_acyVY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28177" target="_blank">📅 13:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyVIW5N3MiGPG73B8suNkD1W3aDgChIOyu9nsY1j_fCrWAS1My2UN0HFKHacSgsoA2MCQitJM92C0oTjTWSteKG_t1yYKZO0qmu-YbKdg_-L5MiFsRc15N5dtZoru-Cnr176CRt2bDzAzDke-md66b3KPhgegVOvl6hMV4oklR5BejlMYNd1vvxGaSkSPXRxGj9ftzVvg1fACPTjt9py1uKIwpHuTdM29JUazVzujp88RGWLUvhYEpRVIVB8QTCaygSesMD3GZuvsZoRl7js3-6hnxCyreSBX8FVwX4Wnrfi255eIbX_-vjq_cxFWRBrQjHZwBp56gbmjyByhw8bYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28176" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itKefVZyzYCbRTaDptIm5im0MmZp2SD2pdSsCB-6ccCnlwIG0K0gYo4oTgcbqANOLSWi4RL0OPr5cHT-NbyvjOydwDbXkA-8SLwG-sESalDoh0Fyq5oITMI7oeZMN7Yn-aQB3fJUjJtR-mFn_t5n3Oxb88Y4JWeVJSMkaRalF9T30iJ_zOd2LCbPyFvYnC9L_CUh1_addoAlQGT_4d_M-j84MqOiPaQ6SHS97Gy47AbftbLh6RZvBrs01S_wBmzU8-mH1Oiphorhiha6roRuvWvBPy79u1vmW0_wO1_Es1s8zSnuvVRDVBI8EtJ2HE57VYVOFRUxYEcc9UyTBrU3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28175" target="_blank">📅 12:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJnPsqJAE76qFwRKGE5cXmG1V_54EvB3_SEwZNuTRCg1nTdymMD9X6q6rZIefad1ci9F2zr1Ii930HimeJGZ2MVzXSo-GBwTQS0KJmlogc65v2NGhOeq4QEWlhu-eLUyEhhl4glnoIC2Cjp9HA88KSwXtvNRgFAzXSBS9MpBWKIO3-WTfRQXlqWR6kHpCmcwvGQ3Ro5QgYkgLWpclhoxxPcLlAxVEa-F7l-I7ecPyK0Y_qZCGYGucc6RAq1Rqfjt0fKiICxuQqUrmAKZ8jYHnByjpHWBHSjsGd0ruCT49u-DQoLVRjN40IQWOYqii0MS7gy9p3tvuleWqySMogozHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
روزنامه‌الشرق‌الاوسط:
باشگاه الاتحاد به توافق اولیه بافرانک‌کسیه بازیکن ساحل عاجی سابق بارسا رسیده تا او به عنوان بازیکن آزاد به تیم بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28174" target="_blank">📅 12:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4dtFukf53TRtv5_zDcVvINvW4U88EZ4c5b156zZ0O5OMEJOnPes1cwMRhWrZfZxLaWDr3Zo6_09k8G7o8wMXjf1XciIUsassGzYr8mYnBW8Hox4hwPXa6GWvsK8G9bpse_cXHVmT1NOC2TThlGgu1KP4tWy2eRmlkwXarHPXDpW6XkvjJgTlTFWwEQkKjUIEf1CP4z4aYcPTN5vyp8c1q1QtVMCe6E1HRw7pE-jA3iicF4PGLP4gL_pSYrOeQYBk5XJehrB6l5dcM9GS-FB2ahpsFqD67sCs7NjRCHBqyvcpvRMk_iJa1Qj-UB49qFnfbYS9EwTvs7iVGVKgolcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت‌امارات: مهدی طارمی به‌آفر 6.5 میلیون یورویی باشگاه الوصل امارات پاسخ مثبت داده و به احتمال زیاد این انتقال بزودی نهایی خواهد شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28173" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3bd66449.mp4?token=mLyl09ZwkHgojzAsUHYH2hhm9aU5YaREeeW04YT2rJ-F_xFt7CU94qi6J5qnYjeqRek2O5nEyolqYnlJK-hNwsJz1gOoPl5yaJRzQIkyy6R4Rjb9zP9dtU2p8Bz2EIbJ_YJONndwEigt7WQu_c0mFBkY3fo3qxEHnH0DgcO9LbtJbe0axEiKWm_M2nx4wXGovI5P7AwIo2IszCXtpHODolt7x9xyhgf-4jPjNTH-oxI6s4URDFL_y4rZgqNtz7xEkkRpWpWJ1Va2LUQ44m0NwJ1OZXJ2RoxQpDy9QaDWAUjzBI44xotFJguIpWNF1ypivhcwirODSl5EeWWhP0vNmBfIn_qDP-lnrp6gX2koEng9u7NB57yIH89BFYT8xuhao532QD5qJ4IXUDDOQCjeaQr3WVKNWsfCylQoqTfjXuW-_ydMs-NkpQIKbnUnasV8FOcEJ6AqG9YK_cmO-okpRC8ygxuFyPKpoyNnv59egyiq0mVcxmHXIZrivm0DmEv7UvDAPv6TPwPR84nJG4-pNtuFwq0Ckijrjk43O0jh6MLwK5Esq81sVL1jXwziYubA8dXNajOmoM1H4SAKvxdTWYCuKbJEFeePVMQFnM0L9fhoW39kN0AgL3TxUulKSJkRk5dVnRDxaVF8lY_ECIQ33mhOZfOTeMJaZhKZPVAspeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3bd66449.mp4?token=mLyl09ZwkHgojzAsUHYH2hhm9aU5YaREeeW04YT2rJ-F_xFt7CU94qi6J5qnYjeqRek2O5nEyolqYnlJK-hNwsJz1gOoPl5yaJRzQIkyy6R4Rjb9zP9dtU2p8Bz2EIbJ_YJONndwEigt7WQu_c0mFBkY3fo3qxEHnH0DgcO9LbtJbe0axEiKWm_M2nx4wXGovI5P7AwIo2IszCXtpHODolt7x9xyhgf-4jPjNTH-oxI6s4URDFL_y4rZgqNtz7xEkkRpWpWJ1Va2LUQ44m0NwJ1OZXJ2RoxQpDy9QaDWAUjzBI44xotFJguIpWNF1ypivhcwirODSl5EeWWhP0vNmBfIn_qDP-lnrp6gX2koEng9u7NB57yIH89BFYT8xuhao532QD5qJ4IXUDDOQCjeaQr3WVKNWsfCylQoqTfjXuW-_ydMs-NkpQIKbnUnasV8FOcEJ6AqG9YK_cmO-okpRC8ygxuFyPKpoyNnv59egyiq0mVcxmHXIZrivm0DmEv7UvDAPv6TPwPR84nJG4-pNtuFwq0Ckijrjk43O0jh6MLwK5Esq81sVL1jXwziYubA8dXNajOmoM1H4SAKvxdTWYCuKbJEFeePVMQFnM0L9fhoW39kN0AgL3TxUulKSJkRk5dVnRDxaVF8lY_ECIQ33mhOZfOTeMJaZhKZPVAspeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از عملکرد خیره کننده و فوق العاده پوریا پور علی هافبک‌دفاعی تازه وارد پرسپولیس در دو بازی اول سرخ‌ها در فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28172" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMToWmsM2QBUCwG8KmuUXazt7XnFK6_MT-pYHsXAbWqKsr6UKvxqEQfy4Yrm9h_5YGXIoDNOIeqpoTyQk1_XrZnSSnb88Q3IMr4Gr_MoG6IjR5If_J2Pu3S59OS4oSHOByS2irJewNwMw0z0PADMVhTzGnV6qVB9ylIqvPXBwvfvVrqLUqZnjfriVk67hHRCkVRvr44r3HbgRR4oE7ns708K-yYr4FVrpJTCYQH8NdtC63CWwp0fI_UAf2z_QJjUrQnq-R6supyFor84hdKvA8eMXpYc2ckmoXJSN0W78IeW2tSaOI_UVcPeGdfeWcTAMLe89BXj5M844hZqmNYULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28171" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4jT8ChD_WJWgbQTXNnm4v_QjW8dyy2WMhNe1O8INefa2ZC0_oSdMwacJ86OjA0mrZFDy-MOcaTV81pSHA1ZnSYGx4MhUxtojCKNXK7mSLMHynpSENXDYin5dvaIkUilTWAjNE7E1digtfRhpMCcltbB5GD-WdRhVPOY9w_LHXXecXA-0GfRWyWhfl3f53JJenLaLvmWep0Hv8LE2ffuNZA_2VEmzNrtfbSTuEfLeZk1126CTtgF-TjQPlxhbeLGfnoT4FnbfZ_FrP5JvbhWOEH4KtXj6gZ6p5JTYDlhwuHRdCXQ_Q4Wq8hBtdAsqbpy_GoVv-3J5h3T71l8HKCXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبر ریپلای شده؛ معافیت تحصیلی علیرضا بیرانوند به‌مدت دوسال دیگر تمدید خواهد شد و این بازیکن این فصل نیز در باشگاه تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28170" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28169" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km92euV_sEiGcIl3_B9k1R3il5UzlfKukOyWNSoD3tLyOY40zXOMvqhc097e6Kc7xl-Zy2kKRdvtttiYLSF23xtjbiJy_rci55H05VYKNDv4h7b5ZKLBS1OsQ9MhZNCun2lfWv1CkyyHxDr7EB9nkadrpyM8cMd-Lk9zD97ubqpGqb1Z6eoOThsAtz71WAmCmfEmvE_Qyr2HhBTViLscG9pLLos0XF_JDf2DmIhyxNucUCj_IjFn4E-aMpBQvK1gFjQl5WbbRsjVzKt9vajhno5eddHXzNUYIehKTPNALeM_nEW9pbp02Ildx4zLE4B1T_qY092T2_VKUWxnkaDnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امید نورافکن ستاره سپاهان بدلیل مصدومیت از ناحیه همسترینگ به احتمال فراوان دیدار هفته سوم مقابل استقلال در تهران رو از دست خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28168" target="_blank">📅 11:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28167">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS22Y_45sxyDKPPOj1p5sNodltwn_wA8S0Ufoc9-6AIuC4KFCxYeECFsUvlBJ9-xHDaD_nGzbopVRGx04XWvX-UAVwBTLCtvOqqmg9Ta_btNK8zE3PTgN0Kg7HdPOPoaRcHvU9sPf1GWrtdC7RFd1Qf9secBR1L-rh72HUvj7YQzs1FIMwWINggIPUC5PSY0M-xhMT90Yc2fuSC5y0-6yCNy29kmDdsH-XEIm8D2WYosc2L8qIvb9hJJ3gJAj38In8ocvduNZmMlKRinE92MJVWpSwCnFst4B_WbAtrjvjoJOOx57UdaM2Ix592x7adPRghBIUNUUp0fKZW-QI3kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28167" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO8cyQtgZpfzNXC5XSeKwDY7c53BaZ4-cNqxc-Xdzmh2-TM8D9VHIaht9FNvnzZStXbBt9Sh2SPAqWI-BdLHKguvCvTU4igPSyiGpMs3DnNmeKzsvhbiG3QvBJXRts7K7bIZHbWMjk8b6ou8taN7wDWBW6-8XWxhQpnL4oj0bN72cPsy3sj-h1gYr2QoWZJXRB2cxAhspkfWvwHsxRx_A_WNP2EdWMBDWQSATRMu5iswDuDwlZl4qnU6limpF3DkEzyWAAm9cmsHUbt9FXzEN6XvJkV2VLCzt4HGveguGD8imiGqi16B16vgiN26js0dKP6scbTqIAA90rWpW2oKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها سه و چهار روز تا شروع دو دیدار فوق العاده حساس هفته سوم رقابت های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28166" target="_blank">📅 10:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035583e200.mp4?token=XreoU6Zip906zfORn8KjDym2Jji9hV7hAW0-41V88h1oSBZdgs81Cze0ZF2C9-JerL9D2-bAfmTGUDqd7h2YUjfn1R3XB-5zXLz8qj5iV9Rzo8E-011szOzMXQ4Hyw49_M124haOKG8hXE0nsQVEb5eFIEIQZpkC6J-B3RCO4CHxvgnGOuplO8FNOZjYLNHI2qJoPzLbKGxEtXxviyuPKAyivOw8b1bwIqc2WqTctl7WBbYAZ26h4bSegrxx2D7atotXW6QbmJhRA4YS50pKUhRBjG75uhlzImbuy4qxfilnP76izQTQ4dMDuE0ItP5P0gVBbmBwmvzM997ELg16YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035583e200.mp4?token=XreoU6Zip906zfORn8KjDym2Jji9hV7hAW0-41V88h1oSBZdgs81Cze0ZF2C9-JerL9D2-bAfmTGUDqd7h2YUjfn1R3XB-5zXLz8qj5iV9Rzo8E-011szOzMXQ4Hyw49_M124haOKG8hXE0nsQVEb5eFIEIQZpkC6J-B3RCO4CHxvgnGOuplO8FNOZjYLNHI2qJoPzLbKGxEtXxviyuPKAyivOw8b1bwIqc2WqTctl7WBbYAZ26h4bSegrxx2D7atotXW6QbmJhRA4YS50pKUhRBjG75uhlzImbuy4qxfilnP76izQTQ4dMDuE0ItP5P0gVBbmBwmvzM997ELg16YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیگه‌فیلم‌های ایرانی هم نمیشه با خانواده دید
؛ این سکانس جنجالی از فیلم «زنده‌شور» رو ببینید؛
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28165" target="_blank">📅 09:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28164">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1FnPo-88jyReNT5oseOtNnjR1WM0b3eAAWx2Jte_3iL3c8ASeFTCW--SUOQgGxQZZIDvFn2S4ykHmVoNaysaV6axQBc7szAec4IXOkOOTJuciLorARLp9tGehvndNRJycFffANKqg7YG81q9CpUWjnxYxX94fFc8P5_AIavAWW9Q66zPHQKALDKFPbh794tw02VAPKAdSxLp5bPHNe5g2b-Inoh2UepYy0Yyar8Ko3yaP89iK4NWuP0Q6ddgV7IiBS2xWB-oGWGjtFA3O6QasYHpNr3knJPhIJQXxwqhSMYuiPA34W2GrXoBPng6sWNN3-EbuJwPm2CCdBWtYpZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام باشگاه بارسلونا؛ ژائو کانسلو مدافع راست تیم‌ملی‌پرتغال و سابق اینترمیلان و الهلال با عقد قراردادی سه ساله رسما به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28164" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXJLcU6PJX9Qu1bav1uliTS1Ztyn9Cm_JEUrZqOanGQOSf9YdWWvNLF2h5ZvIVEysmgXwOAlWncVqxDxN0LEydr7raNnCxeb7O3gXVDGhGkyX_1euOcJVu7d8FJQcTvlKjPaM7F9qpHSlZF0hNgHao0Y1b8kUH6oxIbuQKkGM-hgW9p9o63u2r8BWbR7Dy1-PkWvytHrL72VqRgnSpPfCqe0a2Itdlt4-_eqbfoTOa0fQHClHDrctkCLZNuq8rinelsSh10H6PZMNncHS9u-727Zf16QO63g2TkYAnYNFBSeU44ttNlvk4LOAQZsQmNQiUjESgk_OQ6D00Dhh_P9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب بالاخره هر کسی هتریک خاص خودشو داره؛ یامال جان آروم‌باش داداش تروقرآن، هنوز 19 سالته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28163" target="_blank">📅 09:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28162">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc_ohDgGkYbPdKwRs8vKvKtkEuYaPPmLztoDL7x-H39KLZpqzbSQ5pR1GsWxKD4fRS9xOrcikIdC61CUlga57qylexwd6WwMSh0WQBLzLLxZQphQredqkZNFYZXA3oZSrIXdk364T-nQIngZtod_Cnj_fD6tatyte8JJcMlRhxOMZT_SQdv6E58BEKDj6s33Z337BOlF6i-P_g2xSANulaUAJCAjT22w6eiesSeNSGERzF1NrNIZTOg_JsE228l4eLqB08MOGUjRRng4AsMvbNnPB6WZK2CQUr0oJVz6m3qiI6bT3MzoegoQ9AMd8S0hUPptchJrahCC8wqgWeKTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28162" target="_blank">📅 01:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCPwkofKFJ1HCuiqSYiLg_BTEjEgg1pHYq2UeTEU8-Qm_XXWK7SbDgAZIEe1KNb-7q3kuwUBpKS3-aTOgThUHj87eQnbpwZtffqv4wa2QxLCzvFT-3zWgbw7kqoXT4NoQ1BK84vjYieOHGMv2Pv-f5Oo5s0a-7pi8clLHRuHTAUFKWkQT5bHB4WmYb0JQ20i5ZHheslWPLmrl5GTw2afgE-OwmSW4Rs1nL0PgeNjkYfkOP0FtoOlgFMtoLw53VoUOtmb7_7p347igFf2Z7E65FVkulo2fMkIK264m2z8-Ww2rGhQUV7OBuhrQNOm_q8TeHDcYcVeLP_JuEOA7Gg_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28160" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb80RCWwg8nctE2kJhjFjQMscPV6QygmEwtUTSx7QdDPsY7ogCwZ9uN5Wy7IhGBojogwKSFIC1Gv3fOrRk_-M4-p6fNCpBV_V5cd_64zKccQOlC4TBkZnJt-GseI0kpnNvFHZ8fGdTCR42kZtLJ9FXu8c7Q10wwJk0VAmuudyVyDVPA62VvEPxLeg19oK0PlBXgh9dorc0Qy26ztAWDBs_NQ9cUB5cjDiwBEaUUFKLRp67Uxtlkuga5MD5dfOXlGa2ryq9nygEqbDrELC8gMXr-gK6HAOxBncwmhCML15ajtLSMQHZ7St7Qw4uNE6GGQ5S_xGXqXc9LJ9LBr93WrPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
آتش‌بازی لخ‌پوزنان در شب درخشش‌اللهیار و دومین‌بردپیاپی الهلال در آغاز لیگ‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28159" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msM_kgdas-OS9lHUFrz4x1EyVcpQkatC_5q__o0_Rtd0rXZYGTRZhiuCa0ff0E0v2vIkWlOzSXDCcMjFV8ifkYaRIqMexCimL0ybV5jSb3JGMYbQ7nJXBuEbNXUjLPYqX87eZHj_iU8zECoC3PrGiFZphtptPzVFyFMCuIaQWD82eBDQ-8es5lsLDN3dp9eLETqwqyr29IBZYLT0CnPRx_5CvOPrJTB654Md2UtFuMARLbzMsndtU3u9ejuFmhQkLATyl6YK58WSbAuao8pgys333Tx5nft31on99zu3VtOYTfE2zKBxAZkZ7wGV83WySWE_bphN3zxr-uQxs8-u1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28157" target="_blank">📅 00:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw8LMF8191XWCU5scm2Fkb1o121fujZQywyNtLxwl_hyER1e2jdH750rXSVWtKBU3BITmV6EYObvMEtHuWLKd6AlCJHxTVTMjm2AQSvm91c61JPYLr8a-vikLjHUN4RvmdmbeTedK2f-XqHvMJeuwQ_7fuXTL_YSeNuyySwQQdU_y9xWgWq3soYAw-uTeAxozxknvZRBnADYaF4BDawTHjbH8Z6sdd1t1i1yCmqJIT7K23Cdbpk1khwPrcJpwrRevyNw6lWxiW1GXPB-8Xvo8pAuZrGlO8zBqgmeofdPOUTU2anfxcpjAlBfmo7oN3EOO3MAbvr0RsnDogATOUb5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه الوحده امارات: محمد قربانی از تراکتور و پرسپولیس آفر رسمی‌دریافت‌کرده‌. درصورتی که بر سررقم رضایت‌نامه با یکی از این دو باشگاه به توافق برسیم محمد قربانی رو خواهیم فروخت. رقم فروش قربانی رو به دو تیم اعلام کرده‌ایم و منتطر پاسخیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28156" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf3NQmUbW0JPKO2-_xEGzdqnEGa6kGt9HO_uMNrYYJiADjpB4qLYLWlNpTGM6lJe8gd5iLwoqOQM7VXCWhHH1mxx7I4iVaY42AjSL4s7vcJvhIvrDGPWpt_QsmP2HcxgmtvW2r0bTCf3Cb0vk6smIsZh6g7NlMe0tH4HPBzFclVunvrJ_kJvXpwjDAj38delV3ZxjLQu_zDL-0B04lFGUvz-G5QyrXMjdq2jCeGoZagpJkJXmAp3ryIkSWfG9E_ni7Z1Dclzzk1DxCFK-iDLea5sqiCkH4z9jloCTIxTW_NQKFojCQnIE2LJkOoIYKU9zRSu3JNNU_FGP5sDvX4--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند شکایت به جایی نخواهد رسید.</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28155" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4_x6fUaI39Wg_z47bm0tccYl9q1THSpLro4BB4phC_fDZczTvHNgJ1YhaRojPA3oODfodHiQDFNGPHzuIdCkIrsLQPtJ140luigidoOGdZZEiVepW3baSRFGJKNwstVPAsneiTkwBwOTlW0sEBpKLTMZkapmWF9HVtfVOgK7GndNARih6nZV9vxPekesPL8kD0Mxmoxlcywq1NWLk7NG_1X3aJyU-HFMpGkNFiSSlg4zlYBE42C77IM2Awr8orXci-1zeAQ4CJR2Ld_dLQimi7aTcIkulgoxdmE69iDvkiGQyboQ5jtRsDEmvA32BsgLi_gWqAg2eN_fJnrAB8N4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28154" target="_blank">📅 00:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUTF1G3Hms7H5ZIB0L_O5SRnnahoa5wfFUzHSYn-OoDqkZnNEF-rGEaSugE_3k4dmz3dOpLg_XWea3ucqG1eqk3K94u1QAKlMkZbUoMhADKrNLuQCYUTOil-gWLbMtqzSfDvy2d1f_GlLXPEgH3pAGxZXsXc9naCLA1hEsKB9IBIEIGh3fomtV_H6ELWJFmuFwpmKOY23SeH1qq76HejBXniovz3JGqTqeTUeGzrzEXQ5l5IN56bfg29_P0YMBEEmlDuI9h47u31JKEj5KFmccoLOyJ7PptaEqVw3yx1xnB4xQ5QQLZ0PQ5v5coM6wMAHICGqRDYJAjXvQ4xlF2qfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلیلی‌سرپرست‌پرسپولیس: اگر استقلال تصمیم بگیرد دربی رفت 90-10 باشد چرا که نه ما موافقیم، ‌اتفاق بدی نیست که این قانون یکبار اجرا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28153" target="_blank">📅 23:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7QGvai9vj6ZP108S1M2euhjQjJpZMZpYvKVK4ZiR8pX1G5r8G2mg8GvC59zW0NzJcupizaQRY5NmCZM6znHWcktRT7pAAm66WWgUh1TQMThcrjHO69DHjjFYX25dg5sdwgKKF5P5kC81uUWkauVcoVKoSH0iiefm5rfVXm1cDOK6gI8Y-WbzJeEUFpyHtOTm5nMg9Q7DBLUVXKWARqwmK6lu8HcJYdSmv9Hvy6TSA8HGgGUNccJ6Nj0FG2c9886sDxMaKYODPohBwzgiOtLlPWQabZVqLVzejHx5hs3PRvcuNap0Ku3SVT5rpKmQw0VnlHG78F5CXqsNhY3nrVrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
باشگاه تراکتور با ارسال نامه‌ای به فدراسیون فوتبال‌خواستاربرگزاری‌دیدار حساس این تیم در هفته سوم لیگ برتر مقابل پرسپولیس با حضور حداکثری هواداران این باشگاه در ورزشگاه یادگار تبریز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28152" target="_blank">📅 23:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClhIiHKabBHGCAlmfV1tqeDRTR0vIRCTc2-cu0Qfss0x26USf52H2c9f8mKHCVZIXo_E88UP3E3ST7jiSji9DxusPgPs0hIQjA8K1E6aYGIdjA1nDDW0EZJDSQQ2ShAEGVnxeet5rizO8HYqZYs9JcS3NInuGnIAnIZXbxP27isAQUz-2LnB1NpsAxlOyKVFrn3W0GMA6aPeDW6SR8ghva5l1rZ68QZKkmSFW-8rZWCWkOVpbZJq1UY6bnjBIvfdJfWqtl8dyI4CugFynmXAGig7pBOHrixjcCr3VKJYbdHSQy38uwWdb_tbxx-FzN3kHcH062cSa4rSb-xVBKvMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز اینتر میامی مقابل فیلادلفیا؛ بازی دو بر دو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28151" target="_blank">📅 23:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv9-K3oTui068ExHOaZSIEuaiBA6fb57dpgLr3JJQQcN5B3qnmpNaXZqOdoh93n9uD_5rDz9ZeITQk9lCjLpYVEzHePcYZRDhzub9lztOCarRS9PAw9E7tgQnlIP1CPnc8cp5sPbg3cdSVzdnz5tD41Wciv_qt9xJgmjs9bBJS8NLdA71hj_-ijyN3mBDNWhn4-6hhAjMgvL0iiXheUQlmrLX47eiMMxamHYVUXiuNxorzGi_aBD2qLYH1aLRe-U3h8AcyXmk0ZkblWQCt8tJMXAGfobKfRZax1uZcd76_tK-CHAm0SadunRfyzhdU3wRSEJ63bE8L1LkB3uhMRV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28150" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28148">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAh4IUv3DxlGQ3nUW2FnB0bJd-CJURv-yCsZ3PcVsh5dwyTtae8peehptdJpPjVDmghvQ9-nAjT8y08Sz4yBlFk2uXOVL-5M2ym9KfpirExisGPiq-HUklSod1_-248LLc7ClXvdyetLyJND4fb_TscoE5bgPjIv-xU44Unj-24A3dmOSW-61TRZ9A-EYRbdOz5QlLynWzOkek9V8CcXCJ6I4QEipwr4Q3mYBKqZSXdfaZCVJg9M56z31QkcwA5fRmVHwZj5KX6UvRE9fh5KADVMVlsicyWSwp1YB2WaVDVsMXvcC_ZcQexE1IzftjLCRtIsbG-Geeh5qNlRgsvJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0rbgYMXDT-_U6iKWqOAocH_u2AajKZMWZo1BlP_LxiZTmKrOhFmTVg0WzGBwH8j-0sBD9EEx9QeHqz52eHDMIvW4R8CcEzEPEAUTO5uN3-qetWDDAYdO7RNXcGq7yq7Ire8t05w003cq9nWYM5VLvIj9w6BwZaQ35HFTBZrUHHTJAx4jcPDfrpty-shwxWSVIV745aBeXk-JL_5D2W7rGV_JVIBqQwFK_HrLURTfr6kTM_f2upUJZD1zkr0_gHGDg2kxcAc9dpUBMWlMNqTpYJqa6UqkFZLjVuZ0Bg0lhlVtJitXRwcbKp9uaK9IVvp-c9dKSxHB2pakSb7sbvEKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری ویژه برنامه چمپیونزلیگ که معتقده امسال باشگاه‌رئال‌مادرید قهرمان UCL میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28148" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPU_4rb1Qj7jt6Am_b9n2_7CFvdgXpLNKCi4Uvo_V0bHYaMwzMzpNFPFgYQ153eJqQWoURb1IeZ5eQvr6hVKHPZKNiNVVOrbbltS_UHxELnLxOzvnhq7qrcRWc4goDaq12XmPskdLEKFzDYgDjTDFjJzM6zER-2gi8FVh_2Jc0fmVxbVpD15Xd6qobkhUZ_mC3TcgYPOT8_Ly5qzohzHbwhxbb_EOGsL6mGJ8PptXAXzOMgtr_8LCyWIx8TfUmv341bVaCMCKmgpzptHXqDrNunUnnIN7EB61rMfJK9PgBpVkTuE2jPNhhU77fXQRlw_7F08got5NbA_4QRG3JJMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوسیل امشب درهفته‌اول لیگ ستارگان قطر به مصاف الریان میره و شش تا از بازیکنان فیکس این تیم ایرانیه: آرشا شکوری، علی نعمتی، امین پیلعلی، امید ابراهیمی، حمیدرضا فیروزی و فرهاد زاوشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28147" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE3wiGV1AmZH6UgXf_lZFUZSIaOUy3roYpZUmrs1p9kakAORccUMTfEpGpTFKPnHXa7vgpqvXJBhTLRCYFNLlsQLwn_WzWdTtrhy9YL2loBDsnP_pZnX4m-fhg9J19tRFe27swTUuBIUz3XCZMiDJk7bJ7oq5Ljdm5aBvkKKo7Rnemo1iVYnkc8iwkybRXeLDuxvkn7zr6SAJQtHZ_6ZuEBCv1Wc6f962VqTOKsuk97Th2kLSyKtgd8ORNNqFS8MHhMEsmm3Qw9skGxLhw39lt4QiYps713GXWCsaQeVVVmwNe9DwTPDrHHtNyY2qANqpVkkiXGd7m1-U55HBfhLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28146" target="_blank">📅 21:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa_S-tfOoMd_kaF5YXR7mtBsWlwcYmdp4KgFAKi_wMLdFRbGeR99ddU3R5w09ozYwhL66WzUbKUYszv0AFw0v_rNFSnDK-liuReFMg5ebd0rczS7zbtsYvEhCDONhcoQcHwusuJOmGbiXFRjLf-JguSnFzzJxi4qHr9Ds-hkIFwOlFA8IlIz5MwRXIy0eZYdikKH_6IXc8FrqkRB5SjO1YjOIbh6E7b83TJUOcZvLkHtmnNr-p2hy1dSIKtFKa-R2OVgmMfYowAjaDKE8_CPlxxPnBO4yGMVoOp915Z6CyHgAeY_qzdOAi6TRmvztBGX5TUpA8aRpZnUQQWW8fjHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت‌امارات: مهدی طارمی به‌آفر 6.5 میلیون یورویی باشگاه الوصل امارات پاسخ مثبت داده و به احتمال زیاد این انتقال بزودی نهایی خواهد شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28145" target="_blank">📅 21:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519060667f.mp4?token=o2gExsWxPhGu_cD0itC8WEHQWfSLxkao4iDNY_SW2EYwye66g9g76c6-HOPr08ZC0AsL-odmUECKgQz7LUnzfDbhEk3pPvYoUBWmAf9aQ9W8fJ2OJszxggXlX2peLAxLTcDRddisyiqK6M9gx-Tp8lHpZaNzXFSHCqzjl4qEVOyCC4hJgCxGUfr4dbAA19N63TMV8n-eh6T1D5G5HGD1xwI3WQxKw9mfu-qdAeMuaNMRxVB-N4g2ntD3uhknbg8j8S6INB2CjD63lkK74Hhhnrc3Wfd-PPcirQiJ3ySh3pW2yuzfbZCfyCiL6UIPfF6l88bctB4MpP8DevhslXeJcoBPhpkRs87jCkkn4xFJrk_IqlsFNDoyZnZpBT_yzH7uhgouvPsCSY4Jvbxn-V85OOReY2jutrbGVt8b-Dn1aCJtQ0ngC1-J8gttQiMMTm43b62m7zPv-mF7Xvl3wxA73cKjE36xgYPUDvC6PwNR1KHxwVbq9wkFhizjHnn_m3q6xlaUMm5OCWngoi3tWmYJx8DVO7YpBIzRkCw3PWt1F38HqxiUSgjhV6CRmunUoJHbWK4gfH_6dP6HK4bnXFj6xut1299kaV-QtANsnuSEdmQ03csHnjw01AeJ0NRXls2p497tlOJhvaSe9EZUPbmTaVgSXrmAQAM2KSMCLqbKWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519060667f.mp4?token=o2gExsWxPhGu_cD0itC8WEHQWfSLxkao4iDNY_SW2EYwye66g9g76c6-HOPr08ZC0AsL-odmUECKgQz7LUnzfDbhEk3pPvYoUBWmAf9aQ9W8fJ2OJszxggXlX2peLAxLTcDRddisyiqK6M9gx-Tp8lHpZaNzXFSHCqzjl4qEVOyCC4hJgCxGUfr4dbAA19N63TMV8n-eh6T1D5G5HGD1xwI3WQxKw9mfu-qdAeMuaNMRxVB-N4g2ntD3uhknbg8j8S6INB2CjD63lkK74Hhhnrc3Wfd-PPcirQiJ3ySh3pW2yuzfbZCfyCiL6UIPfF6l88bctB4MpP8DevhslXeJcoBPhpkRs87jCkkn4xFJrk_IqlsFNDoyZnZpBT_yzH7uhgouvPsCSY4Jvbxn-V85OOReY2jutrbGVt8b-Dn1aCJtQ0ngC1-J8gttQiMMTm43b62m7zPv-mF7Xvl3wxA73cKjE36xgYPUDvC6PwNR1KHxwVbq9wkFhizjHnn_m3q6xlaUMm5OCWngoi3tWmYJx8DVO7YpBIzRkCw3PWt1F38HqxiUSgjhV6CRmunUoJHbWK4gfH_6dP6HK4bnXFj6xut1299kaV-QtANsnuSEdmQ03csHnjw01AeJ0NRXls2p497tlOJhvaSe9EZUPbmTaVgSXrmAQAM2KSMCLqbKWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28144" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWAuq_tua2Xi2oQtMSS1E_ODE9n_CvHDxBDe-iX6vfVTMNUP17CUJ9zsTaKMNX17e9udcs8UWKzkSpk90PpdPeGG03_hzj8Zujz79zHaZ7Og4QGdS_2tOMCjArphEac6WsClNDLHYwdXhpIPpK_rSAqVmCjsqGQIsz08rZJw62QMnkZ8yl18tO7__4T3N7Y4pDdy_W2HYyx0M_HqiaKzGdIRpp7cc1kTUtssiK5Su4mQS_neFYElR4M4T-TESpx1rHEgimjqhY-371qoAaoMVTguwI5f3Zn2b9sX4RDHG0Id38N2A6XX94fahk1vEW0KlDQ9t6CbHV7c3otHVNcnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28143" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=pB8T1sJ4RQGv6Yz1OUQlmwgvJ6dKbxFUp4QWMdZw148rNvwKfTnXdTL6abQfCVfofiSXr-9ZZPpQVbhb2FNyOloiSV4BH1Az13cPg0rkyUqSlhOdJSTSQ83Cqttvhx1Y_aZMHmf1wNIqX6NudpvYRV5y85d7di0EGtoFu2MOrLw6_N-W9LOWRMER6mBDid2dbUNekytvoxSLVCxzpkOZJzFFoyK9BjQqqfgpc4v1H9vU1x6g4ry6lpY80F4l4AptVA6c1jqaPleM23mBV9Uq8iDBrkUUU4fJCaC7ZUOTuEFh22ngLg22Fdsmpf9vIUeejngq-16GmfKNTkijUh08xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=pB8T1sJ4RQGv6Yz1OUQlmwgvJ6dKbxFUp4QWMdZw148rNvwKfTnXdTL6abQfCVfofiSXr-9ZZPpQVbhb2FNyOloiSV4BH1Az13cPg0rkyUqSlhOdJSTSQ83Cqttvhx1Y_aZMHmf1wNIqX6NudpvYRV5y85d7di0EGtoFu2MOrLw6_N-W9LOWRMER6mBDid2dbUNekytvoxSLVCxzpkOZJzFFoyK9BjQqqfgpc4v1H9vU1x6g4ry6lpY80F4l4AptVA6c1jqaPleM23mBV9Uq8iDBrkUUU4fJCaC7ZUOTuEFh22ngLg22Fdsmpf9vIUeejngq-16GmfKNTkijUh08xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیویی‌از عملکرد خیره کننده تئو والکات ستاره سابق آرسنال دراین تیم؛ به هیچ عنوان از دست ندید ببینید و لذت ببرید از سوپرگل‌هایی که زده‌. اگه الان میبود قطعا ارزشش بالای 250 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28142" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28141">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a281101a.mp4?token=YQOK23G2B_Ye3faX9oBSwiHmR6BCfpEv_24qgMsB40MdOC0hOqJw1v2SDidOyNNVYSep2ATaiPuhS7DQHrU8S3X9CD8IlXaik5rTyiZaETFVGsiSx6yg0GGCeucUAwOHHdQkiJntNcvM1w3zTyLH_D-nApsRkJUQaqMQFzkhDGKl5CxriOBmXwphGNi1ZjR2Zz5bxFENUJ_9KWnrl6trU6vIYpTDAet-n3AxDDlTEf78YSTYhKn3Le4zEYZW4_LaVe5nJ1hQkUm_QmJg0tuZuZge_JDaj9_cEuMF_ofB4zq7G7FOECM8-KDeAICm8WeFtNw-RGpW7yxLPuoVbkGPmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a281101a.mp4?token=YQOK23G2B_Ye3faX9oBSwiHmR6BCfpEv_24qgMsB40MdOC0hOqJw1v2SDidOyNNVYSep2ATaiPuhS7DQHrU8S3X9CD8IlXaik5rTyiZaETFVGsiSx6yg0GGCeucUAwOHHdQkiJntNcvM1w3zTyLH_D-nApsRkJUQaqMQFzkhDGKl5CxriOBmXwphGNi1ZjR2Zz5bxFENUJ_9KWnrl6trU6vIYpTDAet-n3AxDDlTEf78YSTYhKn3Le4zEYZW4_LaVe5nJ1hQkUm_QmJg0tuZuZge_JDaj9_cEuMF_ofB4zq7G7FOECM8-KDeAICm8WeFtNw-RGpW7yxLPuoVbkGPmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فوری؛ کریستیانو رونالدو اسطوره تاریخ فوتبال: احتمالا این‌آخرین‌سال‌حضورم درفوتبال باشه و میخوام یه‌میراث فوق‌العاده از خودم به جا بذارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28141" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=Nw4GxpsGoEAVBdJfGEHr2oJYY154d6xJmct-yCdWPXOt5IH5QfvYK_tIV4p-v_j6XAmhzklqrpTxa_E-8xjqBeoGiO-toR3NvSQwwF3rA7ROsJify1V8XkRFucLA20oCq7DrMFHUYfEoZAqowhS-8tyfV4D_Hp3XoRdl-5syZXn-7RjeKZ3proHBNhtwpV13oWZkiqkuwlBwG9BSRBpHiGvGsX85lvMbIu3PwbvHNMDE6qopHGO2y7kkHLCUAp6hINVifUPbFCpoSixVO6Zuo8HDr9zb5IOkWmia5KIhXbXpqagDGWZCaD0PiopwiD_WmjPiy0ppUek9kgpzQAAX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=Nw4GxpsGoEAVBdJfGEHr2oJYY154d6xJmct-yCdWPXOt5IH5QfvYK_tIV4p-v_j6XAmhzklqrpTxa_E-8xjqBeoGiO-toR3NvSQwwF3rA7ROsJify1V8XkRFucLA20oCq7DrMFHUYfEoZAqowhS-8tyfV4D_Hp3XoRdl-5syZXn-7RjeKZ3proHBNhtwpV13oWZkiqkuwlBwG9BSRBpHiGvGsX85lvMbIu3PwbvHNMDE6qopHGO2y7kkHLCUAp6hINVifUPbFCpoSixVO6Zuo8HDr9zb5IOkWmia5KIhXbXpqagDGWZCaD0PiopwiD_WmjPiy0ppUek9kgpzQAAX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28139" target="_blank">📅 19:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28138" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAZTlv3t4zVKkbeYI28OjJpVSYTvhHXCRT5IqlZvfEgeIzU6UgRevtTYvuAev0y5E6oJtiQEgQgFeNtGY44dngwRGP9N1BzWIkujH1CoVHDThSr_s3E0zAYrv0s-ecoDvhKCrpopaW5n3g86lY14cx6Dth_PXWX4X3kkJVdz86V-qr21rbGf6ROhz-sh125ieG54n2eYyhzrd3uG9GxY59jIWsJnOsR03T4foiKXQJ0zr5Q9YNr4Cw8VtV6-P2eKpfAAoHgOhcBMOKz8bSXB1_rw5qUfLqPuFxw-bo-FDhRlP3ezg6nVOO2q9e5Rv8GS0mQ7FsItT_bG07mT-2oukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آلباسته برای منیر الحدادی ستاره مراکشی جدیداین‌تیم؛ کل دستمزدش برای  دو فصل حضور در این تیم 900 هزار دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28137" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpEeAPxt9cm8KqHns8wAB5AeLyG88eyCtIAoxU9Ym904NfeJhPJ2s991OP4rtF1RIc7KZlVTCzY5hnVfRiraMpl2JejydSweovNsU0ai4k1GwXN-9HSqC0eOUrtHmskPlJAkYDtuxoeO-wpvWiqzUOKObN1TiRiKrBJpEwXPI32e0iE-dKQs2FpqA26Lx19-RIOvl-d_bLlkzj8YoK68qLOlp1khFs5ZyxDFJHDahEjj3SPOYru_GmnXmt6U8lQLcTJB1aHaqwC0eCYBeOl7o5PuutIV1fSnTIeW_FepyxMqGxjdpS2EG6S1Zo52rLmaVAa2TnORE6ASTzY_VbU8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ علی نعمتی مدافع‌میانی‌سابق تیم‌های پرسپولیس و فولاد خوزستان با عقد قرار دادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28136" target="_blank">📅 19:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asL-0cE0D1JUPy5XOnFKip1ToNbi6NZQEL9aXn2UxvfRvfQr0D6nA-_1zOWOgXLnSJG2pq2yCo6iMVL8td0lXCqat10_6PqLNhfO7ed5MbkLqrWhelh5Gz2C-PzdkAOscf9VM9ufoIAXBeQHt24e1P-w6gbXUybh20lpwkT0euXLJTU5jLQvQ9QbVnp8HAaCgiMqPM1cN0OOXCIQYdutTHgICxK6y63QxDcsT7AuO3N8SWnBRyhqpN6g6ccdSses-NLshVcTOM5XsKe0gIXF3pgq0SYIh3sM05y1LyXrQs8rcV_iRFTidna850ut_ANlQuOGVU0KLI8KIS3BbC_Szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونالدینیو شاعر فوتبال‌جهان میخواد در سن ۴۶ به‌مستطیل‌سبزبرگرده و برای تیم راوانا در لیگ سوم فوتبال‌ایتالیا که بخشی‌از سهام این باشگاه روخریده بازی کنه. رونالدینیو اعتقاد داره میتونه کمک کنه که این تیم در سال‌های آینده بسری‌آ ایتالیا صعود کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28135" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXed62t7at9qlmK_ZrVuSNbrRZcTYoChr9rCZzqoJIwlv5WDPVn9Bg4MoE-VJczMjd6PkVPv7RQOYjC92h9U6rx7AAGTKSpNcztlYo_v_Md8_bQzp8OH1opEJrfZDzCASdQcwipK3HHSyv6avDhJY6PiLrmheb9Vup6QJQv_nmB_S2bKvZ0oZ3ZP3r7zxFbSsb8cU7Sl7RYrN9nGWLw4uzWDgrgXZ6bHK0epsi636_JidubbjRDOp7xHk2QBFktO2xI3480TrXZn3nn63uJ96s_iXPTRjL-tvTgOg-Qv0STJ-5kboSMf0p7JyN3faMobExhjfXOSpV1ZRFMtaCxk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28134" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=KezeVLfBog1O10m-aFsw7bQGiEgjHEf9Tmj8ts3Vc3voXGuKOW_L0DPjKI1J8-4pOR-FpYBTvWFHXb_hTC2XmGjzcFBQgZXZOUMQbuR65iBjfDbSzw_gEZV_cWzGhjmG2T3_44gOlknagtyX2ylkDx-jcjDjW9UNUSb_u3CThiDhgz08oJtQ2ITa4iTqjE6c0LaXYbbeCQHwU79IlPDSjVZ-7LZV_JrS-aLawgDi7BIFjfvnlDJPf4OhuZQVxeD_ai9wmSZaDKpz1ewiYV8ypa9rB1nc76Ra5iJKbW3y5kfiP3eEnPfoJCTSA11EmVyUNL8LxpL8Xef4eOQhCeBbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=KezeVLfBog1O10m-aFsw7bQGiEgjHEf9Tmj8ts3Vc3voXGuKOW_L0DPjKI1J8-4pOR-FpYBTvWFHXb_hTC2XmGjzcFBQgZXZOUMQbuR65iBjfDbSzw_gEZV_cWzGhjmG2T3_44gOlknagtyX2ylkDx-jcjDjW9UNUSb_u3CThiDhgz08oJtQ2ITa4iTqjE6c0LaXYbbeCQHwU79IlPDSjVZ-7LZV_JrS-aLawgDi7BIFjfvnlDJPf4OhuZQVxeD_ai9wmSZaDKpz1ewiYV8ypa9rB1nc76Ra5iJKbW3y5kfiP3eEnPfoJCTSA11EmVyUNL8LxpL8Xef4eOQhCeBbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
تیپ‌واستایل روزگذشته رامین رضاییان روی نیمکت تیم فولاد 11.5 میلیارد تومان ارزشش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28133" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNEp1SiG_K3g4tRADzbIpJlbyk89UzuAWVMp60prwYXer-eHbA8A5--lpp4l3WmOTxSMqr-evdc5sf5-uNwKImcnwSWzViOK-ep7xLiNgIYqHD7Uq1uSDC9zj7nTZ-mxqsGIRv-q-xsvrqI3HHhs0TG0T7cTPGoYsSyI24h9pN64YDEb1N4i9kRwyo5qDFYXpjEqXTlFr-gjz48SDwC1usaE3TJtZRcCMQypS9sfPG86BwwUjKxviqHjIqMUvBcKhOIRelhUjzP6Eww8hyNKwCvPCMVURmCjYki8xxQBb4jVRqYxp182V-Ty8unh6CzxluTrPwll_3bJa0XX7N9y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28132" target="_blank">📅 17:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPsRZQaAr9G4bDvAqcj3oVVr2MFsjfvqXRCUH-xldxlcqBOI2w9RKBKkkTGulOLreEr1ko4LAFCBMq2QLYXAkfUL9z2yzp2cqSCPGeHL1ps3cOKqslHS7SM-cbsTaP2pU8APwyYUzXwiXpgTzhVp7eX3zVj5A-k_4grrFVixEL5Bq9ok9hIcr_xKS3FWlBYjFEYEGCSV6qqOip-WMyBd9mtInqUVWQjldtlFFoAiyWuUlmPafznDkfRHKxc09d-xdbmqD_LkItdnhW7EQegub178Mw0Irw3ThGOXpiY5bTOBGnTQGBB4Lko0amd-xtHCNr6q9azOJkKS_E1ukv_k3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های پرشیانا؛ باشگاه شباب الاهلی امارات پیشنهادی دوساله سالانه به ارزش 2.5 میلیون دلار به مهدی طارمی داده و به ایجنت او اعلام کرده حاضرند که رضایت المپیاکوس رو هم بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28131" target="_blank">📅 17:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxwf9096JwamUdquj2s_Mgx740nWVsS1i91YAY_CcphqldlbuEbioe2YyPiAilv6brx8OxjCGBz_PPHMpM2zHJaz2dHRDlMx2RxR52Nm1sMo45BYnjIGwmwSz9k1_wgRTidYA26H7J24EI8EIxmBYCXjoSdpolmLJIjQ6ehnq6FZ__rRb-I10vWgy9P5tZfghXEGvTMqjnC5DIBmmDJh4cKcyikCupAaY4z_nNKDm1wb1fyEm0ObkUQopwFhT8PLoFW1nbPMnif_jBxSobCzUQTchG96Qp-worqgrJ9YNxsFzSkWq10COjYbsHFNq6gPcOD0MflgfAnkRkzjebAeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ شهاب‌الدین‌عزیزی‌خادم‌رئیس‌سابق فدراسیون فوتبال روز چهار شنبه با مدیران هلدینگ خلیج فارس جلسه مهمی برگزارخواهدکردودرصورتیکه‌طرفین به تفاهم برسند عزیزی خادم مدیرعامل استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28130" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28129">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=VswtaVp6swZPpQ-ut_9MHqmFMUm3A7YMfdlXLyHnkJstqMzFl45JcBQI84RcNHb-CoeQEeN_e0_vPYqwZuYtvJnuahV44BVwDchY3keB9wJ-G9ALPIe_RqWtF7p4tJRcrc_5NVxK8brGGWAt6LbD9NBCf7ygABrgtCP6Kn5KEH6jKBH0GiRWAd-W8gIoJl9kpckqqZybcr-AMDq1WxCNWoeHK9ArV_eC061DgdXF_etxZsWBMRz-VAVj3Q3oPhaGixJEN1TntxvoO_K7QX3kdWdfw6tqoXLHNbRAddKasjxwFYUc4Hb_BQ2TzKHErMKhbYoxtcgtBQf_nuMP59-M1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=VswtaVp6swZPpQ-ut_9MHqmFMUm3A7YMfdlXLyHnkJstqMzFl45JcBQI84RcNHb-CoeQEeN_e0_vPYqwZuYtvJnuahV44BVwDchY3keB9wJ-G9ALPIe_RqWtF7p4tJRcrc_5NVxK8brGGWAt6LbD9NBCf7ygABrgtCP6Kn5KEH6jKBH0GiRWAd-W8gIoJl9kpckqqZybcr-AMDq1WxCNWoeHK9ArV_eC061DgdXF_etxZsWBMRz-VAVj3Q3oPhaGixJEN1TntxvoO_K7QX3kdWdfw6tqoXLHNbRAddKasjxwFYUc4Hb_BQ2TzKHErMKhbYoxtcgtBQf_nuMP59-M1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزاز بازیگر سینما و تلویزیون به این شکل از خودرو جدید رونمایی کرد؛ رولزرویس کالینان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28129" target="_blank">📅 17:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ModrgCwOLZo4WDBku9L2rH4IxlMnxiLZrE9rcc_cVJsmnFwN4HXbXyHcWUyOYobAif5Z05iAEasxrwssH_M0XvFdDl4OHXBC3vchkc2GEUWW77hX5XREwvNl9HrlHErz4Cucx8W-2HKFqWu1VfPOKR8teeuq16qYt9t2qFam6RaUyYOKSxD9_c9UOInY-Dp8OpOWMSx6GmLml96G4lTIE-vAtjO9mgRaFmKnalUR6KSlL5pbORWpZpmsQjWr1sf-jGst1fwr3J5C7ZSarM3mCyiW6afsrzIyuHjex54GXQrYyC0MHQc420Ygb4EZ0FvTrj1FFXpUjBo2J4ATON5M1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی؛ کادرپزشکی‌باشگاه استقلال در تلاش است‌که مهران احمدی ستاره آبی‌ها رو به دیدار هفته‌پنجم باتیم پرسپولیس برسونه. غیب احمدی در چهار هفته ابتدایی لیگ برتر قطعی شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28128" target="_blank">📅 16:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ag-K4SwVZBZz7uau-asT9fRQnEnICQ5KkUC2zi7iblQxVTh2_fArLPvjAIA32E4V3fc8GNF8zizzlPQVnSDwprG1uI0g82QqScqO42Z0ycaPv4Ri-CSGjM52wPY_rK0MBw38eZs0gU9aFFDcuJ1oGgXpSr024UEh2BUnbs_N8GgIL4No41IzUq7cBnd90fhyKe8YeCRFYtrAogzBIOdI9QQqIF1xPbB2UgYQVknUQboEO-4p3jMAZLM4btXjOOgBIj5HbnVui3ghQa7UUteNUSuT4_T2eeSQ_QCsK5lQmSIj83JlZEwFW9hWxNJj_pNivReFbyd5J4FqgmFTDqgpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام رومانو؛ ژائو کانسلو مدافع 32 ساله سابق اینتر میلان با عقد قراردادی آزاد به مدت 2+1 فصل به تیم بارسلونا پیوست‌. کانسلو پرتغالی فصل گذشته قرضی در جمع آبی اناری حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28127" target="_blank">📅 16:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp8unFHuUSHN7Ewjzx0Td9gRPdnmJ1_5Jh_EtlclvUvHLRU7RqBrYaFl0hXJ28pUEVmcrDnU5YFI6YcZC9WAkIN96i01nNgM6XbSvxHrEPflFVKnl9n-uZDZfVRTEN3Mdz5XAg1hm-xG5onAIFC8yB2RW0WkjS3jMI6QW7AAlyVa_c70G3yxjSmKBK96S2nHjkDGhfYA7gS4o713ZdJpJ28XT11M4lmJlYNJAb8EYHTWaNNwjS4O_SbfqnaSJw9Zq0PQx7Wdm5Plyt1DfkL9hX_BrK1cgAYxo5KJXOddPL78OkLj5QLWxzu1mPETZGRrhdz0DdYO5yQuChwtVuFl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛موندو: دستمزدسالانه منیر الحدادی در آلباسته 450 هزار دلاره درحالی در استقلال سال اول 950 هزار دلار و سال دوم 1.2 میلیون‌ دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28126" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-N1fT2-fcOhb8-mSD4kxXJ0SSScW1lkWY6xXI8pTkLJuHmN8NobVeqy2v4sVgH_LPL7_2l7E_sw2IhT4tb-AVy5qZBy_nbuC0Tj3jR4cmetUg0gxplGT_NFLbreMA73GGwvyc-IfrChiyonYe910rI4vGKJGhidQC-zddFxEsvigLfYlazzrnm_3wfM_aiF2cv7qhNfB-YZ93UkXkWNib2c8aiHOAed2H-nwltllBhqkWaoYp3Xy5PsmU5-zCL_SyU-LTGOreKYIx5Z_0BjPsL7VvyQct-bbvTqfIXx3G3g0T3sw2TW5qq0-WmVokNbZK9Otenn_vK97-nfgaHgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28125" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuF3Z3B-HsNbC13COYEEFnzGVq0r0MVQN1XybHjNkKsKprKD4ipGX_EOgKPp-gt3PidYkAu8-MpZedjE9aKoAzLW_TOf5Z38DOgOhX0OpPHQWb8KG5fI8LiJrC5OyHpuG2GyCrFCK0O70LUi1DLS8fYk7dsm9hzMzU8gEyUOoWlAGYaWf2KUj_ZAKv9btzQfVIT46qslApTP1psGKjGQv0VUu1Qejjjf33hcStywuzgDI8WQO8DSH66F_Dnk57WSMZJDsSwuuLR5-0NFk12mQN6IFxtcK_gi_vs_8cuotGyk597T3orJulT5AHuk6Um7cgvTh2LReWd2lEGL8eZuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28123" target="_blank">📅 15:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brzhYZM8VbmQYdJU8CtYnUgmvRHDofF4ffEduPwvd2NSUYIw87vGMHiT6XLdcLpX4wJGrs_ksq_kb3fAXzMekg0R4wD6rllHEqPd6a28yOODNRrbl0DsNQlQomAOyuRMojs21moXoH6KMVn2OwaHNcCSYWeWWH9teX6XD9aJ8Y5cIZD5l68DMoKReuCOzUEt2SuqRgJJodjMoq5rJEtTAAKvw38a4MAcWleSwU98hzcaOD5-0R83zomP7U3nk4FAGJyogyyh4a6QUcKwBA-II07e0AA_0azqH5Y9GwhNY2O44BSmhOOdaIu_bob8k-sasfimSMEYphqMA3X_fsK5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها سه و چهار روز تا شروع دو دیدار فوق العاده حساس هفته سوم رقابت های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28122" target="_blank">📅 15:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=ZVSGJdnMhvvibRZhVkqoKsiAhmQeEbbJ0r9MYxWm5KsqBCIKLdak8cZ1OQGyElKoE14XT3-2Vm1CdpSqP8MKmz0uPLQlsgiXDBwQWUv6GoSc1cKpMsO058ir_6wYgG-pN6pR3LUdRrWc3u5WeNzg2b-KYS51V-W3_cQ8C67opH9HXkquOYtjcgNrGcfelx5CpQxW-DsPI7IoegyBml5D_wjL8RE2FVvlkLf5fUJ-Awz1bD7OWGqQRv924RYGxaczBJjfDMMyE52BTcl0_0FnETy1NADgecDPpMLSpfJ7Z2DHWoDKgwlwywIFhL9xFgZTjp1hv7dLksaJWwkK8bIBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=ZVSGJdnMhvvibRZhVkqoKsiAhmQeEbbJ0r9MYxWm5KsqBCIKLdak8cZ1OQGyElKoE14XT3-2Vm1CdpSqP8MKmz0uPLQlsgiXDBwQWUv6GoSc1cKpMsO058ir_6wYgG-pN6pR3LUdRrWc3u5WeNzg2b-KYS51V-W3_cQ8C67opH9HXkquOYtjcgNrGcfelx5CpQxW-DsPI7IoegyBml5D_wjL8RE2FVvlkLf5fUJ-Awz1bD7OWGqQRv924RYGxaczBJjfDMMyE52BTcl0_0FnETy1NADgecDPpMLSpfJ7Z2DHWoDKgwlwywIFhL9xFgZTjp1hv7dLksaJWwkK8bIBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌از وقتی‌باباش فوت شده اعصاب نداره بعد درحاشیه‌ دیداربامداد امروز یکی از بازیکن فیلادلفیا هم‌تو یه‌صحنه‌رفت‌رو مخ لیونل‌مسی اونم باپس گردنی خدابوند تو سر بازیکن فیلادلفیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28121" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLXVAYDzXr5_caER6gDTxuwa0bP4DfIpMnFQ756bAK2-RMMtYWk3xTN5rzPs-YwUUs9q23NvWM38rjsXq9d1wjRHrFTemyD5ThOxAsnkneBnXaLAqd609SI3tEVk88Mlzoqeb_mLEocehAAEtXhk0u_xnjpR_lej3DVXBrHMnuZvSaUsePGJzDK16H18nFSj0xcOmSrER1iIrUwKdPLZNFumAiKO4swBK_zC7e7Zkxh7FUY8NJmAL-IjHLTg1emiLJ8Aau_0_qAGA6yv_94aY_sYkjD3xe0MytVhMKRstAjMvkW3skkM367yhKlF0S9g3ADriiP5GHJsAlYmhWdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حضور الحدادی ستاره مراکشی سابق استقلال در محل تمرین الباسته حاضر در لالیگا دو!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28120" target="_blank">📅 14:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=H4rjMtOPbbawM-5j6_FtTMVAgwGsH-qSR92vKdBUdSFL5x7s4EKv5xPlyceiOIbYh4bS86iYbJIOvT1xe6kUOXU1qS_HCKCdQllAh7xoNXqWa4LmEUITb9HgaU-84k6h3vL_zuCdxlHaS_WtCayxJDV0gSVCexnJXNjc2dsmnI-vAgF39pxGdCUTTSCqe4ufIfcEf1yLTJ2wimIgn_TXb09b32o6yHVvdlioDaxIeiq5dQ37LFM62GlhEneeI3eGwVsL_Qj_m1vlkaRPrN_i8JqlUktn0MzqqhRj43vD8-UeX5z0R7-apqkF0aSqMtEVGXTJMqqvX2KBErVKogXVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=H4rjMtOPbbawM-5j6_FtTMVAgwGsH-qSR92vKdBUdSFL5x7s4EKv5xPlyceiOIbYh4bS86iYbJIOvT1xe6kUOXU1qS_HCKCdQllAh7xoNXqWa4LmEUITb9HgaU-84k6h3vL_zuCdxlHaS_WtCayxJDV0gSVCexnJXNjc2dsmnI-vAgF39pxGdCUTTSCqe4ufIfcEf1yLTJ2wimIgn_TXb09b32o6yHVvdlioDaxIeiq5dQ37LFM62GlhEneeI3eGwVsL_Qj_m1vlkaRPrN_i8JqlUktn0MzqqhRj43vD8-UeX5z0R7-apqkF0aSqMtEVGXTJMqqvX2KBErVKogXVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش: بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28119" target="_blank">📅 14:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9KuximxtC1RR4Yb8Houpli-JyG6tKd_4FPjNY_Bqt8jCQSuXIUiw9XZka61f8P5ZDk8vVFBHaIZ3N8v8y4K3lWOkuEktOyxfbDIfYhf4FPVkOwJzv7vEHl9mfY0WhEfGCR7khQOXdvuYqw_e-gBeP3wOmubdpYpK9Q1Z3ZRTtnOf4HUxpQzLzabnFWU_lOP8BeF4eDXJ047G29Lgj0WibJiuqAbMzR3YTcRqSuHn--b-kMV4f09s_zrpZgdjY3STZsz7IMwB9qXSZi5OZjfe02JdY3yhXv3lauRNyLB8Cm6RrhE516VY-mHrwo9xy3Kv3UDvN3sng0mbinzxi_bwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای دومین هفته پیاپی؛ محمد حسین صادقی وینگرجوان‌سرخپوشان از لیست این تیم خط خورد. ابرقویی هم دیگر بازیکن خط خورده تیم تارتار بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28118" target="_blank">📅 13:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlF06-Mv7kL26RQR0cy5Bca0YFV14HObpchpvxvegpCz57CpiNyZO4I2IocWEOhHhcA0MLjuE6MPv3G_4QsT7T7ro_9VbFAFIWD8GE5KEDLXpu9VgznbmMUatTza7zhq02dWmpmhd6ScRvMIpxwdD3XNsKg1-sW5Vt4iAnRSTqnRUyDAAlBYRUvVqOp2OMW3tD3XFftZF-Zu7bwsnucl0Y3WBIDUZqn-ALRHhpuByia_XRnTucRoT-39e4KV4moQfaTeaf5syMxuOcQ3yuSqHld0sbpkiFXaNm9mseVY1juRVjhfcVKwFr-thGNvChZeoPlrQ66tq-7sKsjYi1H5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28117" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-BLERUqULQsP0ExXdXKuwgJsEXhrAEjrBpj7A0FwP8Tnf_RlCjdvxYoaxNPFhvCo0fdq1RT9vSvarLmtS5NEeMsx33iCM8h_DoQlIOUZ-sF5grFoaA63HV_JRU6I0daMAWF8eFHydygeMHzEa9WRix-zX55Q-_PcI9ASO_T6kF692aJkC3ZNxC-vHk8lN5KK0YUGlWa-IoTLIUlJchKpjMs8qbHtJKW203TOut1zp7xsRHzRopQpTUTMgShF17mcjW6h8zplt_CVeqXwHelq1a1UsfB-LwThIGwabPTgp7SJjfhq1vD3Tab_I1rd1y7mdVBB8wqIJNqur3Qf3GFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جورجینا همسرکریستیانو رونالدو این رو استوری کرده و نوشته تغذیه مورد علاقه‌ من برای صبحونه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/28116" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Piu9v_I0FQIBWUtyEiRxNxKcQmRsJcdGpJfXV-MxfYBUDg9LuVYOt8IApjwU83GBdrJ9PHSYKyAT4j0AAxynmVV1ZfPvRsz0vj6dAfvFae2qfnnzJ_VovDVyxfW_SD4RG1I4MVaFSMzDyNDZAXq08QCn1gCgCjEfgtC-qy8qyLgq1arHQKcVMJBQJ3EnTG8nndtocYcv0qJT48DQWzxj8FQ49znlLtaaGWRFXXBXYe7Mal5yR4qgCB-z3dca6-66-zrL1wuBL_4Rq6JQzFQQ49pouTiZLf4qq-R5x7U6zf-qD_PUondbbxzJmD91VvQsz-7mawYZB___W5tyGoG9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
رونمایی از کیت سوم خوشکل بایرن مونیخ برای فصل جدید در تمامی رقابت‌های بوندسلیگا و UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28115" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28113">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfKNME6BQIBHYcOxVg8ZtFKfpkNW5tnK5oydNeEmZUpte204p3ucn119z6mrZ3zzS_QexF6DVePONfbPHOcwWIKyDXXkBfz3g60FVGDb1M5HPPx3QRM-g3KPiolTRlraj0tpleJQs_O4V6EGSQ30hk4pTTLS35mH6QFW_KZrptSg9-CDB312bE8QgU4UBDEcLNbsuzUcpWtVHAqndq3pCisGupjQ92QtGPM-oswaRknsyxy68_jVAna8kV9PnXbiJkUhxSwe2W13dxr09DZg5Bo9J9y6uqlJmxeboTUQABy8oIDcTglCJqcGUSn4d0JNm7Qmk6JVcwEj6-MeNNe5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی:
پدر رونالدینیو وقتی‌پسرش تازه داشت بزرگ میشد و دوسالش شده بود،تو برزیل با یه باند خلافکاری‌درگیرمیشه اوناهم با یه اتوبوس از روی پدرش رد میشن طوری که جنازش به زمین بچسبه. با تموم این‌مصیبت‌ها رونالدینیو به یکی از بهترین تاریخ فوتبال تبدیل شد و لقب‌شاعرفوتبال‌رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28113" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmo2RtTW2ysb1WmNPxTDUNPXwgN6dtHuNFq7ushP-lf4DELxEhy5Z_5FNSGKmoNS9k_QQDwj5tpeVFbxk3hCU1Up2J5oiMR4eD8T72755uDH3fVAtPyLr_m0g3yQz1GPcBx-47CDL0c0bkOdoa2mzY57uSTwqeGpXIQmCmpMp36lbDMTQV5YBTLI5wuHiO-bYKutKkQPo08KuDUgSppUQuHiXwMRkOWHRMcmtw1dqx25mz1c59iCDJhDrTsIzwmcDk7iRHc0ob51Tz9vWmtL4oxF_tifAU6DeBqOchqtBnYKymQonGiCgMskOhOiMAxs9CfCU9WecG8St_mnGpE7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیداسماعیلی بازیکن‌فصل‌گذشته فجر سپاسی شیراز باامضای‌قراردادی رسمی به ذوب آهن پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28112" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_R9F38y4382v2W1ZP-gj8tX12jPXYE_0XafMftrpBda62CKS8mzUZXGiE5UxbKGPplPN3CsTJvyyB1BNaRAE-LPdUSVOEU28OsU_kmzPHoodcbpvCEXWI95j2CKrUERgN4QkN4cprQRSxuoGEJPGu1Rw7w2GrwWRWuHJWRt4oXsFVTVmAb0s2DXUWGZQF7YnubRfir9l815WegyrK0QAjKL-IYQPag9_oBBRhjPJfU15MmPnXl14P8EF19-aWG64u0ISsM1_o_5Z6WYPxeridoZXiR0E-kQ-SxJhH8q-8EbM9qmyi_l_xR57zd-CaN4MBpgO7ijnH2G_ojDhBRkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
نشریه‌موندو: مونیر الحدادی در آستانه فسخ قرارداد بااستقلال تهران و بازگشت به فوتبال اسپانیا است. مقصد مونیر احتمالا تیم آلباسته خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28111" target="_blank">📅 11:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_ARpSQ6twWp7WblgOfqrA9nM7rdx-SucuODJQBK2ovLS3nTKLGH-YM0ODil6jbFEgESl9FODS9iva5C2v1s4m-zNPsmWQ3umPSRtPeQcGJ1O-jhbUj2dzrqLa-62dOaDbbYoljDFCDz0uGoj8jsVw1fmvAqpp83M-1uEPEqlvw_OqPjwcRJ9eGbkyCiOWLsiBkVAB4xfwvkQP9qWaZaBJ_wDvgCfIdzd-FQyGGUc-t65tqqzXsTP7N6evAFTb_gxvmgt3SjoPqGLSvfKJ-wft0uG7yAjp3zZKYZdFX6moB69W-lRbFTEHhnc54UWjFt-DIdRqBfqNZZ1gRRyDogLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28110" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🥅
کارشناسی‌داوری‌دیداراستقلال - نساجی، سپاهان - تراکتور و دیداردوتیم‌پرسپولیس - استقلال خوزستان توسط مارک کلاتنبرگ داور سابق لیگ جزیزه.
‼️
طبق گفته مارک کلاتنبرگ: گل تیم فوتبال استقلال خوزستان به خاطر اینکه مهاجم در آفساید بود و مانع رسیدن مدافع پرسپولیس به توپ میشه آفسایده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28109" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=tnWjlUn4SSiOilt2vbskDmBDT6s68QoV-9GgXxLXlEFqfdYR6xHTN4Dz8sVEvN7xKxufHTu4knlHeiQy1EHz8b7QLLYO_oj9FgO6L1Q2V6oHLBKr9gn1G_WIp_ziEIqBeaxOhdZic8dgV3OCyrs86FWVKQHtU527LAC0aAgCmGA9u226Lpj5ZOv90dXAZP11vXvF7zNqrd9c34wllC1F9jzYTzrFPErdlIgtlnciX3eXIr5mgRL1lV24QMJiaxLvGRts-TKOdWIkFFPF4U867NQsjalc1tNkK_BSfHtF-eJ1396J3dnjqf_Xs3-BYT76V6kk7W0IKIN-7iFHMT9_sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=tnWjlUn4SSiOilt2vbskDmBDT6s68QoV-9GgXxLXlEFqfdYR6xHTN4Dz8sVEvN7xKxufHTu4knlHeiQy1EHz8b7QLLYO_oj9FgO6L1Q2V6oHLBKr9gn1G_WIp_ziEIqBeaxOhdZic8dgV3OCyrs86FWVKQHtU527LAC0aAgCmGA9u226Lpj5ZOv90dXAZP11vXvF7zNqrd9c34wllC1F9jzYTzrFPErdlIgtlnciX3eXIr5mgRL1lV24QMJiaxLvGRts-TKOdWIkFFPF4U867NQsjalc1tNkK_BSfHtF-eJ1396J3dnjqf_Xs3-BYT76V6kk7W0IKIN-7iFHMT9_sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
تاکتیک تارتتا دربازی شب‌گذشته پرسپولیس روی گل‌سوم و چهارم سرخ‌ها به استقلال خوزستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28108" target="_blank">📅 10:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=X4ZN9hClVw1x_IZ1OcqISy4wWllipgV93-enGz_zjXmLK5QNYwlMyVRRqZ_M-DJQ8LV150w7_RURL-K7-_KrsQIg1jRuTJLIMPNs36LeebAive0ZllyE8ZFFO3C6-TVR_l0tIQGoQFTRfVGmtQ7uoKVcyY77J47UES_sI3_6XtYjcYxiyYj-Rl-PeN9JKQhXo91DwQDyDpVgr2HCdSqAHJFgpr13QMlE0BbpC1Huqwkqs4AAy24KksQK6e1qgQSGqJrvOk67CCnvsUDLzUA968PV1OQyqR1bKFJQ_ZG-KMKkTgTeSmXDj7K5zB-VPtfwpVMOMYlp-Hrh1cQVSuSDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=X4ZN9hClVw1x_IZ1OcqISy4wWllipgV93-enGz_zjXmLK5QNYwlMyVRRqZ_M-DJQ8LV150w7_RURL-K7-_KrsQIg1jRuTJLIMPNs36LeebAive0ZllyE8ZFFO3C6-TVR_l0tIQGoQFTRfVGmtQ7uoKVcyY77J47UES_sI3_6XtYjcYxiyYj-Rl-PeN9JKQhXo91DwQDyDpVgr2HCdSqAHJFgpr13QMlE0BbpC1Huqwkqs4AAy24KksQK6e1qgQSGqJrvOk67CCnvsUDLzUA968PV1OQyqR1bKFJQ_ZG-KMKkTgTeSmXDj7K5zB-VPtfwpVMOMYlp-Hrh1cQVSuSDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال جام‌ خوان‌ گامپر؛ قهرمانی آبی اناری‌ها مقابل الاهلی مصر بادرخشش‌ستاره‌های تازه وارد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28107" target="_blank">📅 09:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d55041935.mp4?token=Q-OFW8-h-9g7ChSpSw0uBZO5N6T90SqoanbR0sKHYnlwwJTPimD_pt1GRyiBBvb3AZlTGbT2uU9nf2-DI27tB8Ho9n_hdRI23QVWP3XRkPyYs3BYFinhPr14jVVVhS0R57DbCMzAg_asU5FhtcTzOkAQsROikgEFCxkDi3HZg4qxL81aw9YEJfc1pMcR2xC0Sie6LRUFGCnTph4sPC99vi3_u6yfC0-Yww6U6y62L6i13w6uakpBg4aI4-Kv_LBuUlpr67IXZ8jm7Hz5UohhutIx2Qz2EVQIrGkB805x1Ao4PGzm6k-XvKHesmgEFS1ST6JVE_fJqw8A1W4E4m6ptyDctwzoR12JAT_qcmr-a211lBVv6YFDnTinYcC0dMaSePmS51Bgx7AluxXg0Gi2_Vnr2TLDWTRPiJbuhKbsh2TWsI6VwQWyBAuFuGIDWQTWyGw2_BCycr6NLuIQoFXNrNSX85EOMUDMb4cw91tN6ikZ-uM3xD-9SI6C-O4tK1e8sA5mP9ZnZ5R_xTHA6swQTHcN5Ye4Z59DXfJFGSJ2ETs31HMxPJFHDe28FpO43IoBCTKLNGExk5v6ac9tmkrFLcs0EBWAGER9dzsTJ6ALBIOuLjz6-1_1KWRYrspn3wMxX5dpeCIu50yatB5X_svPZlsF-4xLUDPtEwPRuR9nff8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d55041935.mp4?token=Q-OFW8-h-9g7ChSpSw0uBZO5N6T90SqoanbR0sKHYnlwwJTPimD_pt1GRyiBBvb3AZlTGbT2uU9nf2-DI27tB8Ho9n_hdRI23QVWP3XRkPyYs3BYFinhPr14jVVVhS0R57DbCMzAg_asU5FhtcTzOkAQsROikgEFCxkDi3HZg4qxL81aw9YEJfc1pMcR2xC0Sie6LRUFGCnTph4sPC99vi3_u6yfC0-Yww6U6y62L6i13w6uakpBg4aI4-Kv_LBuUlpr67IXZ8jm7Hz5UohhutIx2Qz2EVQIrGkB805x1Ao4PGzm6k-XvKHesmgEFS1ST6JVE_fJqw8A1W4E4m6ptyDctwzoR12JAT_qcmr-a211lBVv6YFDnTinYcC0dMaSePmS51Bgx7AluxXg0Gi2_Vnr2TLDWTRPiJbuhKbsh2TWsI6VwQWyBAuFuGIDWQTWyGw2_BCycr6NLuIQoFXNrNSX85EOMUDMb4cw91tN6ikZ-uM3xD-9SI6C-O4tK1e8sA5mP9ZnZ5R_xTHA6swQTHcN5Ye4Z59DXfJFGSJ2ETs31HMxPJFHDe28FpO43IoBCTKLNGExk5v6ac9tmkrFLcs0EBWAGER9dzsTJ6ALBIOuLjz6-1_1KWRYrspn3wMxX5dpeCIu50yatB5X_svPZlsF-4xLUDPtEwPRuR9nff8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
#تکمیلی؛ لیونل مسی در بازی بامداد امروز اینترمیامی برای سومین بار دراین مدت کوتاه پنالتی خراب کرد. سطح‌گلر اینترمیامی روهم ببینید عالیه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28106" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=GyBHt00K9DzoHPisBZUZw1vcEhjSCwJa8ZPf6EwbV_WPLzw-b2A1K6UkJ-ynusJs-LJ7nd8OdzmMw-RgQw5Nhj20KhkVEAxZIapvuATDxDup1W7L_pUTTieTQSnY6vQPd6IaeOL-XaUiKrHdhDx3DbtF4rrobGDFlGaJFr4r2i_4BHaRk__VZBErm9EJBbdGaIxVcifdOD2RpsI6yNwfk1sDR5LcQ652XA69YHPOiJQ8_u79snR-iLtzj3T-aH118flmKL4EJCkmUWW8k4JwIBk5VuG_y0ye271YBZjAvrloyABVLDmtRoWwOkk3p_Zur__OMx1f20hE13jiUmiy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=GyBHt00K9DzoHPisBZUZw1vcEhjSCwJa8ZPf6EwbV_WPLzw-b2A1K6UkJ-ynusJs-LJ7nd8OdzmMw-RgQw5Nhj20KhkVEAxZIapvuATDxDup1W7L_pUTTieTQSnY6vQPd6IaeOL-XaUiKrHdhDx3DbtF4rrobGDFlGaJFr4r2i_4BHaRk__VZBErm9EJBbdGaIxVcifdOD2RpsI6yNwfk1sDR5LcQ652XA69YHPOiJQ8_u79snR-iLtzj3T-aH118flmKL4EJCkmUWW8k4JwIBk5VuG_y0ye271YBZjAvrloyABVLDmtRoWwOkk3p_Zur__OMx1f20hE13jiUmiy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/28105" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFRkgDQmKcK1uQLhXlk-1vapzeqzfikKQrPPOfMOcyAXDTQpPaRGaMV9hlQ-YZG3dmOJXQNoE4b8YunWQEkTbHwMwM2Z6KeODV_Ax8gOvXFzY3vgNAa02LTo_jAsAiVsbDpxRaZLP1sxQJFK4fUxmjppzrBaKo9O-GNIjDpwf3evX3-NVWJhuqM3pGaZ_ha3ZHLTu5yFuYtQEd2DsK8snBWJcEUlP7ik1fYnUEzc0TLOv-sR7xmlu-2kfO5vL62YVpBxkOc4gWG11LXraOxglVOsmL4oEli5ToBJgqngBSmI61PWCbOPa5T6SrO1dVPhyMA0CDHu1Gl5bPoM0IVwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دیدار پرسپولیس
🆚
اس. خوزستان از نگاه ورزش سه؛ آمار متریکا آخر شب میاد اونم میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28104" target="_blank">📅 09:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFm4NXqufrQZrQ-mpSKvKwbVczex3L6esY-hLa9Ruj6Re2o0opbLsQVk66ILYbDi3uQMRcOvnRt-DMqy_jbBc7fR-vo6IBonForJ3hrndRZKXBAkpe-ZMwEyJGeiQS3POVJKcayFssWjYMTCLI9GJheNFsRSocYga88OwbraDWZqZ5ovazYhKEkajyAyqoqWVoH6I8K6kwMUs4u2w3lG_Ni3fX4ocIrOlIdh7_DudRK0CYBQGlxQ6LfgIpQmQ15wJjpavg43wG-yj4b-yliGfTn0VKKSpDiOU6X_X5lJ_dBw8ud7mBE-mTlozxNDIokczu1vHwYKvJ2UD_KyfRhqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/28103" target="_blank">📅 01:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=Lza2ZS511SZ_mJDGxU9cjTCmsD8SXRH4g7mwblI9DlM1sBAIKRWF8rO4kNGU2VSf_Zei1jaWYNEiLXEIt6v5aEs6TtNkFG99xXsoIxkSKue-42RW-O_Ba7uk6cWzaoH6bABoJfJYeMLnEjNS3x8aNbcrC04e_6XOo_prAAdLG1jcshNEYFLtvxdy1k0W3ukfkCZEVstF9dN6qLVj0vvOz1axkluxMFRg7QbdWHAuF3z6nOo4veNacJ6RS2h9kK3_gBIX2LcWcT86TclVLRmm05WmhRMmK0NdCkkslwAUdaIHTP4RA5vdvEaXEc_MyNIokF9Dddt5yPoRP48fHq2kJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=Lza2ZS511SZ_mJDGxU9cjTCmsD8SXRH4g7mwblI9DlM1sBAIKRWF8rO4kNGU2VSf_Zei1jaWYNEiLXEIt6v5aEs6TtNkFG99xXsoIxkSKue-42RW-O_Ba7uk6cWzaoH6bABoJfJYeMLnEjNS3x8aNbcrC04e_6XOo_prAAdLG1jcshNEYFLtvxdy1k0W3ukfkCZEVstF9dN6qLVj0vvOz1axkluxMFRg7QbdWHAuF3z6nOo4veNacJ6RS2h9kK3_gBIX2LcWcT86TclVLRmm05WmhRMmK0NdCkkslwAUdaIHTP4RA5vdvEaXEc_MyNIokF9Dddt5yPoRP48fHq2kJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری از لحظه به ثمر رسیدن گل تیم استقلال خوزستان که نشون میده توپ کامل از خط دروازه عبور کرده و گل بدرستی به ثمر رسیده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/28102" target="_blank">📅 01:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omaYHoIVJxtuGsOWpEKb3zje7icaGAFkqMo6XOO6JIVMDT1ll5AqVUpHpRS873qYnJhD-Atu1ENkBohUYEwnfVI0Kq2ZnhOb8MVOh7ubBPPOV47lvMpXyhNP0mKwwiPE4k_xOGNHSamqk8XTrjSyTXOF09Vkt8EW1zAV9m4FLeP6UX2X3S9sHziXq0T5GrdAydO6cvtv8d6UgiSMUNF9zIa7oDQJBY37l4aljFx5yQmen0cAJcXMZIKFLyPWn1hFC1PD1_7BmH6BzutWOB56N5sZsbCsSWxgy83b_UTibJVDNOzfsfDiTCteh0fYhcOfXV4koUgnutUb-ZVsKCa-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف اینترمیامی با تیم قعرجدولی تا بازی‌ اللهیار در دور نهایی پلی‌اف اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/28101" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu8mXSAjVpx0LiimTi-Xclk13c0Wxo72Il8O9lvUbmG7l3A9XORFX1eJMjiJpZMHZ2k10ar-EBa94Jo4JmXizbYgYbgNpSBvwcNQT-BS6yB4xgVUR234uYHD83mbx3L__lJGsOGGGj_iZDwwQ8kAJ3gG5sV35htJGZhGoJ11OUIcnLGpA9exMqykjBtUdMNMHqBrCw03quxKyZsGCHMDZu9k1tRhoAnY2TrrNcr_KllPB-UQea3_-hNpAe4yBE9xJaxWPRdD05BEnMCPYT3PP4fA0jzVetcEGr6GqEhM5D16HKr8egGENwia-FJwfd83Whh3VcD6ybj-0s2DuaArDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
برتری چهارگله سرخ ها با درخشش علیپور و قهرمانی بارسا درجام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28100" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebAGgHE1aA5VI3gQiAHkzrSSPdyJ4BQSV1ZrnO80se7vIaH7j1B6pw8W-NyM40ExUNsHJbJ3nDZQwCVDx7ePn7dfKAc7DbOwBesVJvVxLugbUeN7OPw5DJZ3VoxFsciJCWOwGUm0jJt5EHx30sRPJajRBw81_jV5ENYecx34CfChNPqMV_89I8gFrhBtr5T2RLvR9gJ4tdw6hUvHyV9VB2cuyqcdlo5x3N2J28axSch5oHARjsY1MAYU7mW6N5iv7qe_h5ovqXRwdxDo1u048JwJh7J_XLW3cLn8KzaiC_PXevyrJPhJ7PhElD1T_ezYqtBbp9DZDX6YwwwO9kBOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/28098" target="_blank">📅 01:00 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
