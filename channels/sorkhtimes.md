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
<img src="https://cdn4.telesco.pe/file/oVblIRcwq4PFyUWIzYne3tF9Rff57yOih4h6MIYxRGqf3bx69LjC5bNcSVlcvvrP9PoDvE8SEJahkP7bhI69nPkIwQFuDK1EO2v-Db-hSPYfDbzmpnANVZthSXz-Pe2zJ9VFSI2RMRnzi86MAQ4Fzd4ikSsj7VwxorpzKthZkvK6gc6xXMyZxaK00rrFGHrEneX49T6bg0yPAUSLiY34vfrT-w0zliKBBh-l7Q0lrZAI659bqHujMMRaTEWWBuzWNyMG0hUkaL6OuJbov1mCdxGAyoeh_h9pNDx4q1ZZnzfnr3oyvVMkfDok9lesg6JLT2CgYtaQxqHQhflOSLyINw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 272 · <a href="https://t.me/SorkhTimes/140839" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.  #دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/140838" target="_blank">📅 18:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140837">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrgtdrr9YnsVwo7Fhocj1exP7va3NN65jXJeiBbZ8vHwQCbqYVjS7jgZLNVTjgxQn3q8A5Jjs0trgV88HT5n1wDMIxFXsvOZhAoHkTYI1Kd49AKddapT-4BhL1AwbIqpEU6l9-bEXO1ebpekYGgS09QplgNcnMfZqKB6RDmDihIT9w4lJeCFdbYQ06FwNSCxqxrGgL616t-jgrbRuuEn45qB5gIroOfeEXLCXYciMfM1NzcT2iVQO1mkAgBWanGbKlvUbhvSecXdJ0Pv-zn_x1SbFQEA5BMFTumDKZfctXLPy27ZVTeYidjyjUPHjajyIJye3yIcRxdbfb5o2iv7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.
#دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/140837" target="_blank">📅 18:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140836">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3zHAMxSwVrlql21mHhNOKogpWC8IHUmhjrBW7CBmf9lLzhgjJci79NWlFl7oIelng3v7nNG_rr5SD3S6fxvpconMc1olmisaFsX-jochgsNxFnM7XknFnZLnY5AuMYP1D3tlv0RDzvNywVBtq7k63pOhYS2NFALv4dTKvRo3h3SK5JoUy9xehOKmOrV7M4QZAIfqB35lUQcxKfpFKKvMqbXav6_KvbTzFLNgKXwoXGQX9kS_GtEUCDTM5WSAks-qW-2T69l627-yL-f2Cy4D_2R_Nx8lsB7Wqsh7wlaBxQLZafqJY8x3yDgMEWcCNZvsRMkZChXYHWsmZ6VQmnqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😀
سخنگوی فدراسیون: قلعه‌نویی از باختن بدش میاد به خاطر همین بعد باخت جلو ازبکستان اعتصاب غذایی کرد و چیزی نخورد
🗿
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/140836" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140835">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f945d97990.mp4?token=YqiuaXNDymh-M5NABvtZ3Htnkppgrb4J5i4I0tsfiPcqUgF5J7I-HTfOdSa8gHw3i-CIQsJSof8uHg6TqmoZ7iOAsPdM0_woJQYEiYNhYSjk0e_8yNjMegdd4-X9OOgCvtiH4juWwMkd4YCT_v7v4kwfT3xWMoahpZswh8RcvCb8T9t1F_VfdmvV0BGlMLvTVprZGbrRVs-NKLAdLtzgIdokiK2Iapi0kAzZxHpTv65IMWkiciJScyu3Jx-PgbV3t59sUfX2Pb1drF9eFa0nIHHQ0JohAL8p3je6kzooO2s6L-V1sSKgjkn0SlokBKBM0LDehK5w-AGoTUwVy34SzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f945d97990.mp4?token=YqiuaXNDymh-M5NABvtZ3Htnkppgrb4J5i4I0tsfiPcqUgF5J7I-HTfOdSa8gHw3i-CIQsJSof8uHg6TqmoZ7iOAsPdM0_woJQYEiYNhYSjk0e_8yNjMegdd4-X9OOgCvtiH4juWwMkd4YCT_v7v4kwfT3xWMoahpZswh8RcvCb8T9t1F_VfdmvV0BGlMLvTVprZGbrRVs-NKLAdLtzgIdokiK2Iapi0kAzZxHpTv65IMWkiciJScyu3Jx-PgbV3t59sUfX2Pb1drF9eFa0nIHHQ0JohAL8p3je6kzooO2s6L-V1sSKgjkn0SlokBKBM0LDehK5w-AGoTUwVy34SzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول
پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/140835" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0t-rt6_7nS5C7JJuqWUMyzER6lpeGFgIST_cpIoNx5BCaJqTz-qMHHqJGp7DEmy90VEUzDVD7sDU1-DN5t1B28fqaZX7cwUYVI0xsQyMG8G-ooMZEok4L4Yp4UQmCMZQTczJgooJamQsGP0mV6tXb8zxuciwll8ItNhYI_CEzTiCYLQeAZw3oGzQeDWhp2-_4tY4zE6PqJqzF2cOTN2hcqDFLVjfXRFuSMq0YEzr4aS2io8XCm92m9m99OjHm4A2rR32ZzlzAfEnf6PB9Uvx2-It7Fxr4v1F39N099S_MB4mVK1goYvwUxYoXbmqo7K1d5urTS6J-G5HAqRW3bulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پایان نیمه نخست دیدار تدارکاتی
✅
پرسپولیس یک ـ گل‌گهر صفر
✅
گل: محمدمهدی محبی (۳۹)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/140834" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=jClV_TBb6sJQ7GeP7jv6YxGmssQ3oZPtz-zyu17cvjSkefOJNKTpTKMtQYaJs1y4S_p5xCRZe4cVi_88jHV3Ps6IH8RRivcgQ02nq___LdJWotIUEm14oiz_N_iRtRknpST1uyiycdJ66ZukKewfrppbPBVxFgBTkgT8YLE6QRYOK1dKM4hiHOHowW3cYPB5KlmvbCT7HWd3H_3p9f6fYxZr89lZNCFSZhlpebRqs1i8fUqZIBKycvONiF7WiRNJwE2gteeZJuMUlzN4y_4QDKfQuNrJrKhXJ32xFQGKmtQFEkGmIbrml2Vi1vsGmgE8w8hnd34Tu8wFU2_AbMPqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=jClV_TBb6sJQ7GeP7jv6YxGmssQ3oZPtz-zyu17cvjSkefOJNKTpTKMtQYaJs1y4S_p5xCRZe4cVi_88jHV3Ps6IH8RRivcgQ02nq___LdJWotIUEm14oiz_N_iRtRknpST1uyiycdJ66ZukKewfrppbPBVxFgBTkgT8YLE6QRYOK1dKM4hiHOHowW3cYPB5KlmvbCT7HWd3H_3p9f6fYxZr89lZNCFSZhlpebRqs1i8fUqZIBKycvONiF7WiRNJwE2gteeZJuMUlzN4y_4QDKfQuNrJrKhXJ32xFQGKmtQFEkGmIbrml2Vi1vsGmgE8w8hnd34Tu8wFU2_AbMPqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حاشیه‌های پیش از آغاز دیدار تدارکاتی پرسپولیس ـ گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/140833" target="_blank">📅 16:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=auBBUt8yJC3kWOOSpSddLtY9GVzI8hJWL2cklF_760VhWDkpq0sDNZSitp_sZc5K5NdOj_BiqMLGCwaBq54mG7iUsXDZtm7k3Jpb7OJU8EJA1iivP69IWT3hZozeV-njeaeQy61hkR2oqB_Nh55dt_hhOqwpRiIpqhBY4o_opFSCeOUKXIwVY-OymDbkxlz0h0Apv5HCfcnYGceVy1ttLesp5Fy6gk_dVcCEBLANE9OU-1z-UdCHddf353CNQrfaa6Fnci1TvgA0z_XZQUjFXeoBdPmDvGjZp71-Oxr-QvGcW0LGKLywvw4g_onimD9sfTHAIgQjnPqMC09e9ZsDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=auBBUt8yJC3kWOOSpSddLtY9GVzI8hJWL2cklF_760VhWDkpq0sDNZSitp_sZc5K5NdOj_BiqMLGCwaBq54mG7iUsXDZtm7k3Jpb7OJU8EJA1iivP69IWT3hZozeV-njeaeQy61hkR2oqB_Nh55dt_hhOqwpRiIpqhBY4o_opFSCeOUKXIwVY-OymDbkxlz0h0Apv5HCfcnYGceVy1ttLesp5Fy6gk_dVcCEBLANE9OU-1z-UdCHddf353CNQrfaa6Fnci1TvgA0z_XZQUjFXeoBdPmDvGjZp71-Oxr-QvGcW0LGKLywvw4g_onimD9sfTHAIgQjnPqMC09e9ZsDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/140832" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi18b-7hA8cMMNK8rtr5VyPr-7ogBLIB7X16fUsCFBawl9dtoDYCWTI-S_66N28Ygd-rQ-TpGNf0g1-TXJX_A9me6MRYUZnDEzR4OzkTRDcWfeIUVexUCBIbXuM8Oa5-v16nHcaW2kChEiuIOnK6Pv7uTySUojQmTehbZCIlaQvex0yp5ljjFACVzjAdC8durvMJy-Ownnz5wKtRBSIZcQIDxN_l8COq7So-Do-lONUrOriomrhLDk2EyY9KMZ-8pF-FUuaIwO3TkgEmyj45tVFta6MR7RKdIPLvIki191EKTcnj88GWdkIgVAFiTk9ns8BxtnvJL9eRQez3Gunx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است
.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/140831" target="_blank">📅 15:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/140830" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gzA9ZRyhBlQl61z3GV1Vhi-rkIk0CSS_lAVyY2Q8xW-qGnNyKoppfEYEEGsarrWThdKgSFRwiwA99lNWhMZvWeuZsEfOyK8mvFKuHURBnqBh77crfC6Z-rt1hNmBElEver_4jiGz-g-zxh4_XWHyrNBPYlNfaDRETCtceBslAILiOa6z7Lr4qr46hbc7MUlpBRdbfHy0n1JwK9HOdN9zHLoOsiiAYsG09DC5JxfLAefZ_yfVOvdR9NPYrE7n27hnRU3WWKuTO4GjTh8ls8liMioPQ-TZ4Z0BBEkeCzjnWSZRFbhQKJdXojGqAGVMf3KkowcrHQUz3DQ3sdADypng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول مدالی لحظه‌ای بازی‌های آسیایی ناگویا
✅
ایران با 15 طلا، 17 نقره و 13 برنز تا این لحظه در رده ششم ایستاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/140829" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAi1Jh-UvQuFTHQR2gJpQWsthtocSzDg2J_mzCgGWVwPUiHbW09BcLzev41jt9sZ2b2jHWshVR84adwdgSphfrdoizjGNRRmTYUmoDj1PQvjluP8_pqVv9KrxxKEKCM19T0MwkRSguWEL8dxbAQWJWGImVWAAbpxLoTM8tUDyylCYBX1W84lgg_J0ILwdBtHEGPq7ehs0-k3c5x0tNIBrY3qOeMLCvQD9w956aOKm-GIl4pFkLAW6strlDYRABsQ3Tf45Z47UilfAA25Qmi3b38VSOIk4fuCNsP3Oaa4Z-zevwbjDcpUSFd88wNTTNN7Iv1XUELDyJl6BRZWw2R3U-os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAi1Jh-UvQuFTHQR2gJpQWsthtocSzDg2J_mzCgGWVwPUiHbW09BcLzev41jt9sZ2b2jHWshVR84adwdgSphfrdoizjGNRRmTYUmoDj1PQvjluP8_pqVv9KrxxKEKCM19T0MwkRSguWEL8dxbAQWJWGImVWAAbpxLoTM8tUDyylCYBX1W84lgg_J0ILwdBtHEGPq7ehs0-k3c5x0tNIBrY3qOeMLCvQD9w956aOKm-GIl4pFkLAW6strlDYRABsQ3Tf45Z47UilfAA25Qmi3b38VSOIk4fuCNsP3Oaa4Z-zevwbjDcpUSFd88wNTTNN7Iv1XUELDyJl6BRZWw2R3U-os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
✔️
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/140828" target="_blank">📅 14:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INeu_XuwLJmBdPdvFs3mkkg9Lssa5Pj2jfg2lzSh5DvAT-z7LQXs6A44S4V-A0L8nm9ISi2WLlEvQlAYlCnOH5qjGK8yS4SSrkw3yMpjEYsnyIZzWyt_-zNKe_DQCZcvlKTziCFD1NxI0fQvRCJKzOYUHQtkWoX7yorIruVbxkaTYxfrgGvHbQ4xvPLySUh1DpkWiH5-kEyI0iGVYCBzfFsHzCKzzG4DmAjKpkvnW6EoSX_GAZwTwK3p8pLV8LhHrVVLylBOnv8uOBgZL6kH60B1WpwyArewbu-XqLVqzjFtWk3KLoOIGNXJm2b-_1gSnZbZfCA46dqFcDd6GlhSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
چهره خندان و شاداب جلالی در تمرین روز گذشته
❤️
✅
ابوالفضل جلالی مشکلی برای همراهی سرخپوشان در دیدار با صنعت نفت ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/140827" target="_blank">📅 14:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5WJ4SmUnE0s9Lj_OA5AgAnBwtDyL4pZDKckUhdIwwJxszIV9k6qx214G-CPuiduSlF2SqeZKspo41fJi6uJIV4Ol2ekhutC7EqZ5Z5YlT6uREktzfPQJyyjmaecNapGRNRVpKSIcD4jwe8zI_uyfV7bBgrsPSeKor0Dk3c2vxQ7jTSn51w3bhLoVQbYM-cCbCGXfbRzW7io7KLpfwvJyoEVJ_2EaK5Q-P5uJyZmYJkQfsRvLHuawXix_3xP8ofKLYr-QUKwK3iAiUjdswvL4Sq-ohyMw8m59RjagfwQuAC9fsbWeMqRXMQQVnHDEgQueGI-xBEzYGr5EAo1seRj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد خروس‌ها و آتزوری؛ جایی برای عقب‌نشینی نیست!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇮🇹
ایتالیا
]
⚽️
فرانسه با وجود غیبت امباپه، از نظر عمق ترکیب و کیفیت هجومی دست بالاتری دارد؛ مخصوصاً با بازیکنانی مثل اولیسه و دوئه. ایتالیا بعد از برد پرگل مقابل ترکیه روحیه خوبی دارد و می‌تواند با بازی فشرده کار را برای فرانسه سخت کند. با توجه به فرم دو تیم، انتظار یک بازی نسبتاً نزدیک با موقعیت‌های محدود و احتمال گل در نیمه دوم منطقی است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140826" target="_blank">📅 14:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/140825" target="_blank">📅 12:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
تیم والیبال ایران جلوی تیم دهه چندم اندونزی زانو زده و بازی به ست پنجم کشیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/140824" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/140823" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: منافع ملی؟
✔️
شکایت از آسانی را تا آخر پیگیری می‌کنیم!
✅
یکی‌از مدیران پرسپولیس مدعی شد هیچ توجهی به درخواست علی تاجرنیا ندارند و شکایت از یاسر آسانی را تا زمان رسیدن به نتیجه پیگیری خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/140822" target="_blank">📅 11:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3D0ExMEYOq65-hpwPUpwj-i1h67iOaPHEUtSsOh1w9jE_ixNr7Eug3iqwj9gNTMT7hGz8MKncj5iUMtcOACb6tgSPW9jYXrxjOnzzNC739m1O_A_pVeyYzsF_HK7c25CYXD7kzlVpswitmAscZZbhY2_DmvKWH1qgfNSDGOwsKsO3ugdE8vh-XGEOhpjOcbeO4VvprRBbvX1w41v3fGj83P_uRio37e0nh3jRKAG4IyQdTa2diPxcsqZfFtq_yhpfaR-SSuup-hYOU07p2wQbhDpxynzHK48AMXNWmjt_EdEm7WTlR2W5bRUKLvNgYa9u1BfQ-P5NIQ1Bj5NXtdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
⚽️
👀
‼️
فکت عجیب ؛ مهدی طارمی در شش بازی اخیر خود در تیم ملی، نه گلی زده و نه پاس گلی ارسال کرده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/140821" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140820" target="_blank">📅 09:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140819" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWP81E4rb-5Cncb4WyJHqVBsrhgFTxdwgmVGv6OTvCTMiBFZUk6U8KyQew2osYzZ6p0y-VXPmdazn0GVeXZ2tfvcmCnS5lTNH6tgM9S7z8MR8HhaDY7AOyB_U-ealUM_P1xxtQiNLDkMcll72Lk9wcNfnhiC7-BZNnzIip-JX8H11MVEBvsLeqJvnfAcdXb7PslM1S4okwq8EPShlEnv5qftqLt7b6MXV_fLX7FNLyUTD8j6KK5DqhlzgyMVNUHmJZs3l2Sib5DOt0uUsln-rzA4RpUgIoq2i0fLkatZjn7W4oynsP2quFztjz3DEPjekNpsO_c6SpG_oHJVfQ0maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امروز تیم بانوان با زنان نوشهر بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140818" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140817" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g33l_jPqNtkf4MxXYmDygMv4T9TOa7E8fJLis52jns6FPl0Zzh2yGT-uYeLuT4hcIh56uzoL8-1AWu6fPI_AHDLRngu1uyQ0gG-kDJzEStzKweVEUUAHnTGjTRAipL03cRIjOiyNX45RLL3b4cM3JFAtWB4hEXA9MqVu200ArQVjhaizqzxGN7Kjlq8eO_BU9F-O6_mv1H0wZHHBtREfymtmmf5OX7nWVtYKRNAez5KKbIOO4uuMkI-APvd9MPInB-y3gOOo_vouQXp_fZ1mLhZ0iW5ABPtnRIZvhMN69FzYXMbqYhL9IFpGaYz5w3xihCpCR_d6HhL9U2LixXK9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک شب پر از بازی‌های سنگین و دوئل‌های نزدیک؛ جایی که چند دیدار می‌تونن تا آخرین دقایق غیرقابل پیش‌بینی بمونن.
🔥
⚽️
از تقابل‌های پرریسک فرانسه با ایتالیا و بلژیک با ترکیه تا بازی‌های متعادل بوسنی با سوئد و مجارستان با گرجستان؛ کنداکتور فرداشب ترکیبی از مدعی‌های واضح و نبردهای کاملاً قابل پیش‌بینی‌ نبودن است. در سمت دیگر، اوکراین و لهستان روی کاغذ دست بالاتری دارند، اما فاصله‌ها آن‌قدر نیست که بازی را از قبل تمام‌شده بدانیم. ۶ بازی، یک ساعت مشترک؛ از اولین سوت تا آخرین دقیقه، شب فوتبال ادامه دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140816" target="_blank">📅 01:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9phN6VeVMtnberXPNa0YvZY2EUpKUVyW9UdAFR2PBLyWu8NwGFxn152rs4Q5qA3INgn65i_i_mdS6CAyuGjAv6x_zeLsKVPYdNQtc7g1ZTcM7Hf_rU67vzDir241T-ucTZKfCJPdk-tODL0J6pYolHgP-QDBYmyoAsgR8m9DeV1c2qWIGC7BmCCwjpBtJh8Us6PWpLUOE7ayid-a44vaZX48SNkk9QFql4vcRHApLkQmwk3cP3UQNOuTRpmEPnlleCS9wi-X8Bn5mjowo3Ca1tgutTQEuZnHmvPkaDYfPsnw0HlIBdL2Q5rvX53IZ9V4kr_RqEYJnC-qPMMBa3OpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گفته میشه که پویا اسمی ۱۶ساله یکی از استعداد های جدید و درخشان پرسپولیس هستش و تارتار میخواد بهش بازی بده و مثل زارع تو گل‌گهر بهش بها بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140815" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBIlFnAVZXMhDLxYsVzz12hQj2Z6colSCtqdustbtZDP9rZ2T3zBhw6knDAACWvcG1VjbiyYn2pEUiEpKUiTeGEefmqD3Q4nza4UFPKtHEzbJZ8Su1JwoVmMW4kFOt2xZF3-Z-KU6xQ4ea7JvaNQwfrfycfGy4oE1OeRNc03xahu883jkDVv9nsVKW8RIW0diwp6RqGAYEVdhUHAwF6y71uJ3nf8s-S7HZgX170QZE1Jwclr0_Ssosh3vj91D_HGXceTPfPCrhx4g06UeXYu-LKUPqKkSK7taxwhpP3gsHyx3i-eA8C3zcON-kH2obd6prVclgcJnJ4ej93p1UFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس فردا به مصاف گل‌گهر می‌رود
🗣
تیم فوتبال پرسپولیس در آخرین دیدار تدارکاتی خود پیش از آغاز دوباره رقابت‌های لیگ، فردا (جمعه) پشت درهای بسته به مصاف گل‌گهر سیرجان خواهد رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140814" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140813" target="_blank">📅 00:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEeQdR06QIDKOvI634J25miKSlNjdb_mfi2T4R9g6Iz0ZQUVS1ujl0xzZmO5-jTWNihKEqsWbdErNiq6t-glRDe9upGrJZ_aL0DvAN50nVXqCABvltzQbzjHG_05zSta2-DGZhpMPnsBozUphikfqazJZr6gtFY2kHNUaS7ShgV5VqM_Z5FDnkSAHiaIn2Uskf67AF-3CKbQdiqQEzNAmxUCKacrLCsg3zyN98A7MhEb7FuHsg3DFOYxe66yEAX4IwuzF-udHIQZC80MaxiRHx_M6wM5eXqcAWzaMtfcNj72PwYImEtmA8eU2T4AZv9gXF1LhSBuHoDd3gxDumYszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت ملی پوشان پرسپولیس به تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140812" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140811" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
جنجال قرارداد گرا در رسانه‌های مجارستانی
🔺
رسانه‌های مجارستانی با اشاره به غیبت گرا در ۶ بازی اول پرسپولیس، دلیلش رو مصدومیت پاشنه عنوان کردن و درباره قرارداد و دستمزدش هم نوشتن. همچنین مدعی شدن پرسپولیس دنبال پایان همکاری با این بازیکنه و اختلافی هم بر…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140810" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
هاشم نژاد به تمرینات تراکتور برگشت و برای بازی مقابل استقلال اماده هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140803" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXqelgtsIGPVR5qt1eF7xwJ8NIQ5RcsUxdyepnPykuafJ9ZLsMRIOJ3AM2sYZ72fHxNlhxlvEDJHAZRQys-PKkAPxA-rkJmgZTb-q4lnXvzXZCgivpM1ipCcFKrgn3TkhEtZX-FlXH_0x8rzahJP6XJ3fC1ORNs-SdAmu35MoMWFM7z6fJtJoBcVQVJcDwccabmrnHyjmW_1ZMiKy3iS3AvX0vIsb5x1cAB4jQWsRD91NiBvUBbP9MgixZdPN4xwAulXuhBwNg7m2FbEaTJHgWu0PedXu6eRVuI-0MG9nkKqK3-LBfLDGpscw_6ycxTI2I5zcmCDGkz8YGz6R9p4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد شمال و جنوب اروپا در یک جدال سنگین امشب در پارکن!
🔥
⚡️
[
دانمارک
🇩🇰
🆚
🇵🇹
پرتغال
]
⚽️
دانمارک بعد از برد ۲-۰ مقابل ولز با اعتمادبه‌نفس بیشتری وارد بازی می‌شود و در پارکن هم معمولاً تیم سختی برای حریف است؛ پرتغال اما با ۶ امتیاز صدرنشین گروه است و دو برد متوالی داشته. نکته مهم امشب غیبت کریس رونالدو است؛ او اردوی پرتغال را ترک کرده و برونو فرناندز هم با مشکل جسمانی روبه‌روست. در مقابل، دانمارک روی هویلوند، دامسگارد حساب می‌کند.
سناریوی محتمل: بازی نزدیک و پرموقعیت، با شانس گلزنی دو طرف.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140802" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140801" target="_blank">📅 18:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcrNK7ih2T-MReb7FAaRwJIEeu0L83ripxioAKDxePZJlI5kzDcyNMrLl0_91E76aPnAgTfbdpJ4W70bkFkTK8_5Gd8gn0CmqYRSmkBRFLkTC_zEU075DPVKpTyTSR8awTa9Z_LeaKaKjsfpa3YmnEWoP4GCChUnEuT4dZkw8GPm2tjhQAORVR8j9qQAMjxMG4r_cxt5CFhSQMIT1TtkEitp6erCcS_5bl2MC443-3NHIffLOXB2JlF198V7DuNilRP0j5Z4wlM1uVFimLjL7IhGwGbCW2C1VVG1XaH0FoJzKkdDcr5TH-BAfgZiNbp5C46NWTLNPMJdYOD1CYIUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور دویدن را آغاز کرده و احتمال حضورش مقابل صنعت نفت وجود داره/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140800" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOITnLXkuzLS4i64xad0rllYm_Fj13nrIfzDjkPzLSXwyBteqddtq2t15i-jCg2DroqWPSPEvsyMhj7x0z22vQ_9BdQ9sEFh2LWOF8wHbFwn5mBqyLkuKrI0uqwbVch2jXB2rzun4Rxlu28pqFkmhe2O2Qk2RnNl2W5P0rr5EKXcx8bCMLK8XlwhaGfwDu0I9EIxS3rukiACx6ymP_ojjQWHY8HbHqdkomprjGN05OnEEwtERkSD0n0c5-mroKV3qfvjsWzOFgP5PyqPIVun7CVv20PPmaIQqJ7Fn2kVE8wtEfryTb4gr3NthjaZimO7RIyjnqUemKBQfTpLrQcKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گویا بازی دوستانه سلحشوران تیم ملی برابر گینه بیسائو به دلیل محدودیت‌های پروازی لغو شده است. به این ترتیب سوژه خنده سوم این فیفادی از دست رفت!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140799" target="_blank">📅 18:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140798" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btAXFQyQkdFBGqqhXG0RbpHuMqjpSa_xtXHHs4uYox6VMnAgEv6FIn3UiUt6ri5a_-39UUVDDb9xkDB6XBV7kTkRb4fYMKH1ZmGg54Irtrp0WbOdns3PMDd3lr3Gn7vIsO1XoM5brOFgKdgUAJ-qa5hRmryuHYWxYXK7ToRKwjb3BClLuL_Lj6X17yqq-OM8MpckwbCKgny-8awbIK5IeVIoknjrAhfosPzAf_TbDBO2DA8FAgi3UQvXbMdtQRZg1kKF4hskM20cwkhUwitB7xfhZiBTPPFdI-8VJTPPndIAXEuoR3g7HUdyxIHFwbpg_pWRn53PDmMIW3bxA7QozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
ایجنت دنیس اکرت در تلاشه که این بازیکن رو فرو کنه به یکی از تیم‌های ایرانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140797" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPsFXR9_RZ1G6qI7xrekms1QBhl9a4meOEq4PDJh2QmAToG4R5GSVn2E0WqC2qCnV4H8XiP-VBcKjvi9ndc-g2o4b06r20Ae8dK1FaWXcdthavi3SquuH0vY2IeL2H-bdg8Mdzi_J0DqFSygnCWq0Sfpig6D8jYjChCvSnU4KVmkBs1ZOZ1rLPfCFfyCqSfFMqjV3JADWiLML3patbVl-0Wj47iFql5hPUUI73RfgUqIYM5xlzsTAjSm3iYtWEsl4w9GxQ-IYcqgWV7jTC6uvQr6mQnV_EifrKAJNhLfHATvs2WG8rp3DnmZfw-MbxeQ1jyf3WBXAmlCa9uULwJRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afjRv9e-BHGni1PVRdi0QVe_lUCCaZGKmn4GFVrlYgO8h40huLvm4OxmfKdBVd0stqOTFvovlM4YKo_IUnUzaxxlseuDO5vwJA2Zijbn1MrtRc823sH1MuqAyNj9NA4YoiRByzAsCTMSySpex4Y9xsXsF8OIM2Cp8FTJ-apPUbW1lLSx_qHDsFDtwk--tjmNwPDBwgpmVMDFBHout8uaGKNkZ9igReaegA2BovO53DrUn3lw87qPfvkOzDFbIhe8TSRN-XqpVnzQGGRnmgSvmOWZlXVgrFVm83idvBfJe739H4PM9AXnzKhXtt3jxtlgb9ktqUlXemCfdZONJq6ZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic_TJGWb8Hrl2D_Ei3qQVL_E9CcAf0jlLa7hBpXoZ7ER-kxHZuNBdO1VFLgMLdzmMHmiymbOaNUva95qZESnkE3abVHKgAnzTZFjbGyLZWGu99Zvh--DHIAvUEiYotxkpzS_iPyeTfJWwxGi2NeWQWP7YeluDDVPexKaw9rZuQsLlZIHjTEnYe1_1P8zWwJDpwOG6oqs4JddIs60NKs7x6jc-utM4CXUX0WjxT1If-Do2Hbcj7p1p7d5eWnEA3VgH5Jn2itPQH4JzidWCqqw82XrCr60pR2Tu0Ppnn6IesSplx-dQwOg9pzs-eoRCTOI6ZUGTBzeasgk1L_3T-GnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMrrF8qHuZqbBuHRKS91P9oGCisA3I4j8f0AdHfpldhuszIn8tybp1bpz8n49h2KqdxLmqVoKsOuxUAYmPi1X0xu6ZSw8Zlf0zlOGcBEO3n-einUcKsvvkMZspH0nE_tIWiOaJMJ7VUXbqC5dgUfJHlQIKT2U8jNWndcYcRayFwTqbLKFAMNT9Yy8Vu3PAyihbmli-rUIuMSERnhcH-DlaSM3RwWNWAynVGTet20zVATJFb_8BJP6NuxeVYgOi4S5rG0qQMv7IdUwnI2c76MNvRrG-86ODIECNjUrmQidDwUJU-OzS5Kt9bgpnH01zZmXQkwg2Z5LfITBn1Ml6WAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtxwEL6QaTL0uo_HU8OIVvTwH5Z7P4GkjlzUu6NPbwFs-Dqfi-CjzU8GwG505zMcW4LixCKHexpk0Xj4BNNcacgR5HmhoWV9UiO2MiSOiRE6ZtcDZUvCNbeobcrT5s_yKnLv_GXxtBJCmLETokPTjqb0e3JYHVs8DcgL4s822sa_YGYKo8tU-mlzM4LNObI3jTI_VFEKGTNQ_72rVzKs_YS3heK8tT5o45k2p9_FslTBOaVQxru_c8kAGyGxYbV3CxkF8F85SL17ZpCaWhInxgUYxekzrPeEfybjDlD0ClMv47xLKzmlqd7-IBqICURfinTxTveX5XTIkl1i3I8sxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4m6dYDFOcTYTi0euCQUmFFvRfT3dSojg21Ptq8Fp4w4XEbXbmT36FES6jLDg3szQ5q3408ZEzfgyVpPXZR6TSbo-N8zz4V03f7haQnLdtD7fI8mfkUrnAMweFGvip1Biv-EiarWxgl5ZboeLPf1sXJAq3jxkWt8kVs8DkYPGeR5Y0n_ZsoeJBoHBZ2C3hLsvU9Oy9qzygyVMAos9bRhiddHLP2kIKwUYe_6wJtGzs2Ge_sfFXIU4ioVlTVgQriuOIjZO3QpXiNBPZutdEhfyydfpNGFzfNFBZKnPGp8IOna1Ko8wlhHv4I66X4xr6s3nfYSTdoCS-Su5mGfdUZB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIiZNxIUHkneWYUsg9vzAENRArMetYsOkadPsMOypGm57TCIeaWXCGYorFJqD9r0FtYPtnTY78ietJFspwkOxwSpfI21kh2L-HZjJls0sGLReSnFxJio3sYvrIBNEHuQKaX-_-B4Ttr0gclHYUbY6zA9g4Lm_eGvukxhoHM7j2L7Ayp0aKySDChC20zAB0MFfT6Em6QNk-rGW4HhC2W3C4fhzxcujtNZtXA94N4PZiwQXxybtVWnka8OfS1p8pX4CpsVnw54dOmpcmY4ncSeZAXHwNkhMlzmMdyvEY_ZXr5oF5KKjJTlgB9xKtqx065DVB-RfrgV89NNI6yyodRbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140769" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Y9fRjUSXH8RBPFfY6lE-gZk1dEEne49WDfCQ2DnRG0HxTrtscItE993_-RR4G1LWHdDYCn82rBLaaue1_nuRikacHGkA-3FZpx74SMRBbPQfajKWTFrXEqH238WikHIHl5CSjZE5UmnRWEfpwnKJf8okEEkrap3kHBZIgl2khqj1ef9M83FKvfl3RtofXbk7agHJz3Eh3EgHhW9I2WmPIblx5pi8NdjmCblYUbjbiPwPMFdurdgqHPZogouKzOQaJwvunbdB2kHZjl6rkwBx71FJVTiNnERcotyKrdZhET6jUCeeNQHmckkvu5VHXAEvFFuYGkHe4mhg1PdZdHDvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c458bfa09b.mp4?token=Y9fRjUSXH8RBPFfY6lE-gZk1dEEne49WDfCQ2DnRG0HxTrtscItE993_-RR4G1LWHdDYCn82rBLaaue1_nuRikacHGkA-3FZpx74SMRBbPQfajKWTFrXEqH238WikHIHl5CSjZE5UmnRWEfpwnKJf8okEEkrap3kHBZIgl2khqj1ef9M83FKvfl3RtofXbk7agHJz3Eh3EgHhW9I2WmPIblx5pi8NdjmCblYUbjbiPwPMFdurdgqHPZogouKzOQaJwvunbdB2kHZjl6rkwBx71FJVTiNnERcotyKrdZhET6jUCeeNQHmckkvu5VHXAEvFFuYGkHe4mhg1PdZdHDvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بالاخره گداوند رو‌ بردن سربازی
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140768" target="_blank">📅 23:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=EotsUD_p4l0h-FtccCaqtbK8A9XGAeKneZlbJnxCJ7m3obeYIX1Fmkd0qYZUzeo5XPOW8amcdxXAHATm6C-hbZ85o5-Rdb4aESbynBvM0-MUEN5tkj2Ql2Mmhd1PBBYLKzL99VpUw1a-GwWDshhnYXHJVg3OWB0Q2chu2Y0G0qOqf0pcaMaUYEVJlGFZkVc-xcf597PEsAsXoYrX59-qDG47q8toh-9KC6_ocAamAPscauc8cwsHBElCsVfBIoSfAxXQlXnZdmXfYE-IdRzzNA3CB1lOruLfkIC6zT5EDKJZApeeNDRi-4CCmp2jIxgCDbGS-cEJ8Ayt_OE2PutZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca8ba9d21.mp4?token=EotsUD_p4l0h-FtccCaqtbK8A9XGAeKneZlbJnxCJ7m3obeYIX1Fmkd0qYZUzeo5XPOW8amcdxXAHATm6C-hbZ85o5-Rdb4aESbynBvM0-MUEN5tkj2Ql2Mmhd1PBBYLKzL99VpUw1a-GwWDshhnYXHJVg3OWB0Q2chu2Y0G0qOqf0pcaMaUYEVJlGFZkVc-xcf597PEsAsXoYrX59-qDG47q8toh-9KC6_ocAamAPscauc8cwsHBElCsVfBIoSfAxXQlXnZdmXfYE-IdRzzNA3CB1lOruLfkIC6zT5EDKJZApeeNDRi-4CCmp2jIxgCDbGS-cEJ8Ayt_OE2PutZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140767" target="_blank">📅 23:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLRtIsxQVxXygE_pmk_Dhw2kruB8mIncIwnsCSvGt361Kh8Q72lDH4oD18Sg3-JX6RPQGIDy6jt9o9WnrE64VEWI0pxjtWug3vWrt_FyDXgxHlg3EupX6R4iPvHGMI19cfKs1pqH81fcLtVEmNZza9ZJb0YvDwKu6X3iU_KbBnAijSP4gMCNCkC6h_nDbRWt0eDxwe9d14b-9_uij1BiRFZG4_B_sCF6dG4UzuzrI7nqFeWNN6rNtUKScfM3XEQgvKH5GUEdLTrdXtQfXuil2582LKjCa6Cv4rlA31t2V5C4Fu3bJEWKS3LEbWWJR8xP4wVoUz-bcY4WMDWyiEeZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🤍
قلعه‌نویی: اشتباهات و نتایج اخیر رو می‌پذیرم و مسئولیت فنی تیم با من است. برنامه تیم رو دوباره بررسی می‌کنیم و در انتخاب بازیکنان، تاکتیک و آماده‌‌‌سازی تغییراتی میدیم.
⚪
می‌خواهم تیم ملی رو حتی بهتر از قبل بسازم و از مردم می‌خواهم فرصت بدن انتقادها رو می‌پذیرم اما تسلیم نمیشم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140766" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqsgXz9sLCEB4wxiLGLigWqtEooPeSmVa9iAxhYqfhfG6H2msd4D7Ed-3meo4zbn-AkZAULp7jL6oH7T4wZKVKn7621WV8AeRCChJzKuZzNjhW0rb10ZUbOaYm2KCiCOjKmF4NKuyX0fP_w0QewojPsyE5nhUDzvqHnnjR6ztkhXPsW6b8pqMk0SAsfab9dxm5m_eLuW--I0ZhIo2H8AvpmhBBkECob7mdpkvWITNPJnSnZQzTJJRk7YyUbqXaiJ_PWToyvqSAqZJ3xlRbK6JLnq1sYUlWpVQk5FQ0enYY22ibPkSqlCdPRS656fDxL4_lMancrliMj9uXRV4_jwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140765" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140764" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140763" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامپ: جمهوری اسلامی‌ هیچ پولی براش نمونده؛ برای همین فشار آورده که توافق کنه و رفع محاصره بشه. وگرنه چه نیازی به توافق دارن که پیشنهاد میفرستن؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140762" target="_blank">📅 21:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140761" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJHE1eehzophifZKiPsnqC9Hf6sTcwgKbH4i5L1AtR02_YhVovDVNPz2oU6dKS7vRurPIoQDnmrUxhHp1jtXdUd7ye4T3OZLNQwXL06nA0EpdHE0uCVUvRKKhaEz6rzWMdHWp8PydzakjIiGq0yn0DFztumc7IZZiDINqxsawHbAKEc-jUDlUJ5HR4B8n8eeRGHiPEP7udfaRvm305AiKTYx2geqXvCkeo7zXWhq-MbphoX-bIrkbC6zz9C7VuBQWzm_w7GlHpDTQ9VdJpRgzP76LzYrPJP8Nf4idiZ9sHFZR_FBPGzrBMb8f4BBvfhaQNTEOFqX8RxkrdyEUjGPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
👤
رونالدو اردوی پرتغال را ترک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140760" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fppfXRj2gnxtq7rh5daO5X6uOSyzv2XSrUDh4-fBeB7ntxv7Q3kXyN_G7XDW2NFIAlmrJvy9KoXy16xXuMBBnYcttb_XOBR4WRTrmSVtmRRP_42NwAPXbPTsjJu3RMZKXGc0ThKDsCpDhwZr5FER2HVc6T6L_Xl3l3lumM5ZOjPVLZde0zOif7wMFM-dKAiCCGV3Vztqj5adoDwlGGXzbG2Ahvc14Y7lBoxYKDUeHaBL_yrWgMPuFriQAEMpfeK4xgp9kE3c9OwMR7dEaNCHhC2gJ2EEucME5r4qmcqcSN9NN28L2cs4gwhLjLE8B5wmAVal6nzkXA2PgOunFHgDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نزول فوتبال ایران به رده ۲۳ جهان
▫️
تیم ملی فوتبال ایران با شکست مقابل ازبکستان و روسیه، در جدیدترین رده‌بندی فیفا یک پله سقوط کرد و به رتبه بیست‌وسوم جهان رسید؛ جایگاهی که در سه سال اخیر بی‌سابقه بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140759" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhp76orX8ePw90d0ajsHvXUY32D4tdnbxJ0i2j87RMxlQrJASqK97_1IgQPpEcZZ9YQbvpsQu2KwnLO2GRLgf_RpH6IrGkvv7OKHYL0lr08OJeMySmP2YRnpqTH81X2nvy2Jnz92ajykMfiGZsvxqNFThYiOlZi5LbsdvMa5VBAydyzjLqRjqPLlm_ruIPrGj3sF07EKXzl4TR8XUq0XvJKZ7rd7tMhX_PZ7n-V4G4FjzvoBcrcbWc0G6n4hcQCmdd1IEyNzwZOueP7gKsSfinwsRoAJ9C_toeBMXnVDTsD2g1sHrAAij8dDyHKHt6zPHt2L-dyOqgsDlUoUkZW8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🩸
لیست مصدومان باشگاه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140758" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140757">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
مذاکرات مدیران باشگاه پرسپولیس برای جذب فرهان جعفری ستاره ملوان ادامه دارد و اتفاق خاصی رخ ندهد این ستاره به زودی راهی پرسپولیس خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140757" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKK0HvL4SFWvKKUSveDagqVfQ2FsbDbGsrWShD4jgobkBFQE1aoEZjfvjo2zIQXJrscTZj6CSCGqCvImnmxfZlZRu80bDwJSKyzLQLbf2Bm5KNAODqgSIVMNZ8BAvkKUgZ3M_GeWUPAqsvqDS9sKQNZR6N3fIw32HVR24at4P4TkMurV41hsOMIQBkibyHsUz3Nmvsu83wXZgeRWBZM5zXs67Vtf63CFoYP2wS4ianp7jWnH0GMy3ekRmKyuWsIG7D4bAcvueM9F6EdTpxjwRblGH101e12usxajLmsUK6nCMIAdc8ETeE5IkMCPXIQAOg8N35gkT7h5WBTCkVs-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140756" target="_blank">📅 20:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnsjm85vONG7lUkdzdTeCIo56HcZVUM2Kkuc1LHtXK3FyW0Ff1AIzmdNhGD2-K80cMDlt4YYG3jHYzDhvc4H65A5clahYbTs4y48nlJBPqsHt3wiU6rhBsVg6Ed_ZN54w0Dez2PzeXodjh65X2ex-eTA9qG8G89ZBnNBKS--_pjDX1kvl6_LJA7_iPv6DP3myDS7S4EQRqlrxuGgSRFLElDVJJcSdPa_uaO0_8yHXkAfrlA2EGn8mivuelfPL730drY2WA2a15V73nA7lXmPucTKcyDm6Mtn6tMAFq9f1d2RlXcpLOKCKTI109hSBYdW7FjjE2KyVhqpPezPYPtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=vUd3Av4y4_6zkmyEP8OL1qTGyqEIcUXVh0-wAimyDmPkivDyIRTngi2cuRwDtr95ZKsU5F-pFCsHfDh9oukmCTmhWVnLg_fOfGBwvCGHDDJCkIoLNpaRiA4DOfRNkpBC3Z-FtXthKppzYgPio8dammZprUNjksH1xXbepKCjhj76ISdzgjVXScITlktCekHiwIkGxmP-xW9JP3uaZs9KIa2FQiUKo-yiqXsVgELCGXkmi4OPXstI9nta0UhcMclFc1aBmYDdnHaukbc6YG0sc9QJASptDwPo4QqCIiHrvV-EjatjE8c-VUSW-9BOBgn7ggS07UZpL7MCUeN7cJ23KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=vUd3Av4y4_6zkmyEP8OL1qTGyqEIcUXVh0-wAimyDmPkivDyIRTngi2cuRwDtr95ZKsU5F-pFCsHfDh9oukmCTmhWVnLg_fOfGBwvCGHDDJCkIoLNpaRiA4DOfRNkpBC3Z-FtXthKppzYgPio8dammZprUNjksH1xXbepKCjhj76ISdzgjVXScITlktCekHiwIkGxmP-xW9JP3uaZs9KIa2FQiUKo-yiqXsVgELCGXkmi4OPXstI9nta0UhcMclFc1aBmYDdnHaukbc6YG0sc9QJASptDwPo4QqCIiHrvV-EjatjE8c-VUSW-9BOBgn7ggS07UZpL7MCUeN7cJ23KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIiZOL6Jn1QDF9LovOCYbg-fhY5dQqyDYvU229hXGDzFVydLGFvTe9yDjsplppmwJzfHFt1t7oVojVhzQmExRa2tPwfN_1YzxsHGkVmK1WAklrSr8VUahPDZFU4RZvgc6ytscooLLMX0TovCjO35tCRxjyjrjCydfXyAHd2WTn2a1h-Enh4HJUXjHCjqL6NRqr5GitYrfmilRusfdu4OoFg1sWNu6DBB6xxsxp9HKFxdPnI4hbWto9cFMgT6vssoF84xNA33DhVXeBxzEkbgMRNrqg4_Efd92a7fZLDpQ62uuj8vlNGlEWZAyVrbbPGuv1EigHWRkUvh2_QZoSIH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaIIKfvWdADTcYEnawmHf-mUcd1-8yvfuqOdGGuSK7UVp43FuYjCegZSzi7tM5wWueJaG1rAKsNdNhd-EeAJKrBca6QYDLJDREtCYvDIg6yPlGSOoILPxoYOwG1heEbBPF-2CgjkCQAJiH3fCNEph26nn7tQQwkapK8fsM3oRwMTfNYMvRFz4CiykKS0UG2ZSAPvFrLLonTCnN912ipdFUPPJsBlEf_ibAm2rLiUvkzEDiE-vgFtYz-M7r3zdY3PbuE2smyB5vFop_F9NppZ9HMisaaFYfjZRW8uKF9H2kybTjPIxCrSuusmj-7bZJiF0WdvJqy5wT0ZOZ-RgLKDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
