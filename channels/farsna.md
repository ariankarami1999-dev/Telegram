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
<img src="https://cdn4.telesco.pe/file/akrNT6MUbyo4zgosE-HIRwpsjKINJds9zmQl1EFAETxfUz0GOaC756n4o0k0rMaQi3CJV9MToDWbdaCiWNl3BrWfhhMcigAA0mVksAkNYElSBdaHXG9ZdbKAJfGhsIBh2fRNW4cdNxgdk7r2tigzuDPhVHxGKEcLFWTV5sZm8U0iOU_MEfcJ_TO-4ZcCziRMASitLu6guf4gZFjODh1xDDgYMMFbzpzgRSXWDlm_Ff6rl7-w2IyN0ZhBJhihM8on4Cz-IN15iH5-2JUaOuNHplIXeJ_JHfd3vUrbfJ48wCHhnCYXDK_ccW_S1KyN5WIPIKDOmtDujEC-t0dMH9-Cpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 09:29:20</div>
<hr>

<div class="tg-post" id="msg-436074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آغاز صدور ویزای عمره از امروز
🔹
عربستان با تأخیر یک ماهه صدور ویزای عمره را از امروز آغاز می‌کند. وزارت حج عربستان اعلام کرده که «پذیرش زائران عمره از ۲ هفته بعد از آن آغاز خواهد شد.»
🔹
امسال زائران خارجی ۲ روز پس از پایان مناسک حج می‌توانند به عمره مشرف شوند. البته سازمان حج و زیارت کشورمان هنوز مجوزی برای اعزام زائران صادر نکرده و وضعیت بیش از ۵ میلیون دارندۀ فیش عمره در هاله‌ای از ابهام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 505 · <a href="https://t.me/farsna/436074" target="_blank">📅 09:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShGPE7MSg7JykOy9mILstMqJn2ovw8HajQqEEIzs5zRtwzxrijF44k_LY42B-Gjw_XZToICuCHijYTkeXV6VHw70WhLrHoy31B1SY638BWlH4tQssQxSb5EiDUuyJ88CdBbKXo8Syh7EIOvayT6o_x2Ohb47mEAhqI8gcEPMHwMadtxAKeGszZiAL91H55b0DjXeEJqh_lhjHxS8ddrRpkhTuxtzZz0kpC-rQbWvkrmJuwAZaYXWjPGsfL_jOKyRq-tt5NAsnaGXMjDmUSxVuwtwbeU82kX4AooNFGlbFrV5LgZIwwLbCnT3SrqGEmRXNfr7-tVTE8zzfulVPLxiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر جعفری: نهاجا برای هر مأموریتی آماده است
🔹
معاون هماهنگ‌کننده نیروی هوایی ارتش: بنده در موقعیت‌های مختلف مسئولیتی، در محضر شهید سیدعبدالرحیم موسوی حضور داشتم. ایشان در هر جایگاهی، یک فرمانده معنوی و دانش‌محور بودند که بر دل‌ها فرماندهی می‌کردند.
🔹
چه در «دفاع مقدس ۱۲روزه» و چه در «جنگ تحمیلی سوم»، مجموعه نیرو‌های مسلح با هم‌افزایی و براساس تدابیر ستاد کل و مأموریت‌های تعیین‌شده از سوی قرارگاه مرکزی خاتم‌الانبیا، نقش‌آفرینی کردند.
🔹
نیروی هوایی ارتش نیز تمامی مأموریت‌های محوله را در تمام ابعاد به انجام رساند و از این پس نیز مطابق با نقشی که قرارگاه مرکزی خاتم‌الانبیا (ص) و فرماندهی ارتش برای آن ترسیم کنند، هر زمان که لازم باشد، وارد عمل خواهد شد و مأموریت را به نحو احسن اجرا خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/farsna/436073" target="_blank">📅 09:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf53bd474.mp4?token=Kbos3pC9HOoFFPk9as2raugFJihucgy4FEZLK4Off_zk9Bo9rZNnP796ngjV5EA__x1ThoH0yW5nxR6e2YrUze_H2hIk0oDfwRIdb9YI0PCc2CadfROSoVvvSk9ILmaO8fV76joWhvcuqZ_OeVzMTw7DwT-VtibBo5440hVXgoBiJjQ3gMyXf2d3YA8GmwmIcTV3XxmGd07QVFQ5M4JdacWWvML3aO3eB1-xKHyidPPS-Gypr0UsssulVG7YkRaTjXfRG-1JtqID2jpbsK4YXgACCH2wxXn5uVVB0Vx3dvIoqVzNaLFMiKulhmz_VGDirT3mooMDggePcOe8NA49Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf53bd474.mp4?token=Kbos3pC9HOoFFPk9as2raugFJihucgy4FEZLK4Off_zk9Bo9rZNnP796ngjV5EA__x1ThoH0yW5nxR6e2YrUze_H2hIk0oDfwRIdb9YI0PCc2CadfROSoVvvSk9ILmaO8fV76joWhvcuqZ_OeVzMTw7DwT-VtibBo5440hVXgoBiJjQ3gMyXf2d3YA8GmwmIcTV3XxmGd07QVFQ5M4JdacWWvML3aO3eB1-xKHyidPPS-Gypr0UsssulVG7YkRaTjXfRG-1JtqID2jpbsK4YXgACCH2wxXn5uVVB0Vx3dvIoqVzNaLFMiKulhmz_VGDirT3mooMDggePcOe8NA49Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهمیت منطقۀ محل انفجار در فلسطین اشغالی
🔹
شهر بیت‌شمش واقع در غرب بیت‌المقدس که محل وقوع انفجاری مرموز است محل استقرار کلاهک‌های هسته‌ای رژیم صهیونیستی است.
🔹
پیش از این برخی از فعالان رسانه‌ای گفته‌اند که احتمال می‌رود کلاهک‌های هسته‌ای رژیم در پایگاه هوایی…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/436072" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-01PTGe2e6j1AsAnf2O0fI96x9zGBTIb_K1b1ENwYKH_YeHo0Rj-Z_o5bQkepl-cKC_mF7up6kqWd_5IUijBs8tb_vRE6NieUKL2CeSqEq6XKYAj7t12W0LBER-WfujSBhxH8F3zv2RUJ_k4nzfax_LZMR0x5-ElhNK506rqYtAkN9DIVtmyFrVPkHQpO3dJlYxgueVVv7Ky-IqDbQ6_qEczpm3U13qwk63ptXM9UhyzbrSNl_rT-A2SLhoNBgqq-nykXl0Y2v-NaC6QglrBYtB_RRCF8Pw2xxF-VZ2K-RPAPM7vh7Hj81LjNhZuvbwbGI6VdMaZR_MulA8KEsSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حمایت نخست‌وزیر اسپانیا از یامال
🔹
پدرو سانچز: دولت نتانیاهو از یامال به‌خاطر برافراشتن پرچم فلسطین انتقاد کرده‌. ما از همین‌جا حمایت کامل خود را از یامال و مردم فلسطین اعلام و از نقض حقوق بشر و قوانین بین‌المللی توسط نتانیاهو ابراز انزجار می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/436071" target="_blank">📅 08:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5b035afa.mp4?token=CAPMThxLz3rcnAVwsaGQshILCv6gmNwReGOSaJBrRoN1CCJG8VlWP3RB1ksnsp1KiV8t2XCmxRWIAnoTjO9Vw843ipe_qWks1wypus1UVOR0F7sLGFqKxI3CEgioB1bMJ9P7JwOoefj3fkW4VnkRi3hFHVH4yChkbbf1xSkwz_uYbkAIt5zJAQOXa9y8wJJEE2W1OX6z3cFcZqsZBXwb80w7nuBicGPm37swDDp8uJL-r_h9ESL53w2ejr3Kcj6c1KlPCV84IFKxZP1-yg7Kng1RCEIVYANwGzmyCfgcKU1GVmrvB0r6J_idHdH7lPQLF9dv4NNM1Ov6IRRwTrOXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5b035afa.mp4?token=CAPMThxLz3rcnAVwsaGQshILCv6gmNwReGOSaJBrRoN1CCJG8VlWP3RB1ksnsp1KiV8t2XCmxRWIAnoTjO9Vw843ipe_qWks1wypus1UVOR0F7sLGFqKxI3CEgioB1bMJ9P7JwOoefj3fkW4VnkRi3hFHVH4yChkbbf1xSkwz_uYbkAIt5zJAQOXa9y8wJJEE2W1OX6z3cFcZqsZBXwb80w7nuBicGPm37swDDp8uJL-r_h9ESL53w2ejr3Kcj6c1KlPCV84IFKxZP1-yg7Kng1RCEIVYANwGzmyCfgcKU1GVmrvB0r6J_idHdH7lPQLF9dv4NNM1Ov6IRRwTrOXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجسمۀ طلایی ترامپ یادآور گوسالۀ سامری شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/436070" target="_blank">📅 08:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سامانۀ بارشی به شمال کشور رسید
🔹
هواشناسی: امروز یکشنبه، گسترۀ بارش‌ها در آذربایجان‌غربی، آذربایجان‌شرقی، زنجان، اردبیل، سواحل دریای خزر و خراسان شمالی است.
🔹
در دامنه‌های جنوبی البرز و نوار شرقی کشور افزایش وزش باد و در برخی نقاط گردوخاک پیش‌بینی می‌شود.
🔹
امروز آسمان تهران نیمه‌ابری، در بعضی ساعت‌ها افزایش ابر و وزش باد شدید و گردوخاک با احتمال رگبار و رعدوبرق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/436069" target="_blank">📅 08:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR52taIybJu5INBZfudHGZ8Actph12QBnKrsV7wWhRTtKV0El8-0qcIXazyKIhamjYEXTrnG4cduFAuqy1LsrIIsw_urXLiwW3JWtBhNoAz9IcIEQ_5C6mFwjxHjX7yqCSvPu2G3RdlwBbKahAQt_wSc8I9emOLmsB6N96qamDIj9m5XaplIOv8DgZvomTL99kM-xKoK7Owg9fyO4pOZ1_NSM7fKJAB4wsbcYDo7dRiw2i7GEATymJq6_hTLzJyM7FT7U8gxb-z7sT9cOpFwZn-DHCc2PW1o63BQZQBAjH35ktUgrX5ECiwsxCLD0N1qmJslsyfEZwJbX19Mosf2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل‌قبول هوا در پایتخت
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت هم‌اکنون با عدد ۸۷ در شرایط «قابل‌قبول» قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/436068" target="_blank">📅 08:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436058">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr75kS_emK8sqzYmSm8KJ2gsjF22zrpIY-yfMFov3gMK8IPbXqcl9df9lib4UCPZ01tT1plUGpsMaDWZAF3Qfbkbq6uSbitxh83W4K_GyKYik5Qu5G5Ixij-_yKGwK8NbFLFzZRLtdw_msqGHOAfQQ4RgRR2XlHomdyEiyTwPg99n8huIzcz8DxqWknBdNtvmFCRf8K1uqodpB0FrCDHTWY4GPpeSz5y-I8Bdr1tpSd4y1IY0ob7R-onvm1UwHY-wUTz5KpETKI7bcO3e4zLJ-Lkj0k63P5q03L1I0uUKkDR9L88TGD_2OJPKa2tdUtdCHEQ3yrhLyblNkps2pNEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffSbJrwVfTP7fhXxx8SDfcMItnnbWdAGc-xu9XPRtepkCL3YpUvnULnB0HWzIlp0z-5Bg3VcRK_y5RbhMT3GlZwh7BhflgmPBaudYGiXOdBgDNEUgpaFkg_bm416Cy40CuvJXT0vFyV5hFY13DD71qFS7MzEY0b0ifKMyzw57xJSMfwRqTOX1Q_Rgto5mb1W5cQGz3hRh0dNniF1HAhxITbKqo40Ypwu59PweMCmbcognu59vQqi_kPzBSgzlDgxaPvmkiRVfyRCINpZTqe4iraoz608-UmUut9QGQihZd4H9MjqlTjwEYfLaG8j7g8FOhJ-ZLfyFNVOcgIhpGCS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvdQvsVzv4QI2T5_-2RfBy6cbYfQ7bSfHVJqw1APM4YgzEo8aA7UfDPYTCNbAVvN8k7ZoEoVa_YkHeAwkr8IIHEAHEjZU9wXYuq9Cg7VJKwPNzyu65beSIZQisqa7KPe3KobIMYDHun8jBQwxgbZeYumd30AhDVRKNYMrqDzIISoi8esdE-8w9sBNvUx-vZsRB-XCpAEr618UuEi7gPIF6--b62ra-lsPFPmkWbpIEUY5QiwhRhXZVWsNfsjMCGKUZCtl5WV98o1brihTxg0ioncsEADPgiF2hxsEpnfl5D2OasDwzkqYJTBdxIbTdeN5ewSFovS6QKvO1TfnjJ6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIDrA0DI9Gi1FhhgsRnnt4bbYFQQrfoBrryBzRts6L6BK0R-BL0TYcUNTIvPuycAl_YBW2sY2HqvFwaVK1T7Uk0KDvNsQ7Yk22jWgBQ7rfmWV2SJRyJACC0vHtjcI-h1ovSBtjYIpq1Lcm6jHLCFUQWeXlkID5rSaiPDrMoHHBPnpeYNOfJwqurx4Rye8I-UcngrtLYH1IrO2KgPF3ZvXyvk7Ml5sDxPfKQWWaeFOKAE-FglTLYB01EUL92TWl8eqPorpDhkZ9c7-Up7AglRYhf_lgEOdwPQu41nyqBrQHFoFADywUav5PlzL26vAEeKsDiBXMIbzm_OndW2d1ZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwJxiOIlJV5xwc5xAMLZ0-p0atOOAjrsQC2uTqtPl1qn555Rk04SXdLRZx47zubNwTQQnM5DNWq1bL6_igZSd50j4i_QxGhPViJvi28uDLUrCHW4wE1cXjPPZgQsNa-IUhghscjPHG5PLRwOacPT-IgbFi6bY2u4aUKR78TVVp8yLV_ukYUda9G1A1Ne6W4bi34ltVdiHnEtERflXT5YfWXlWjn4ilNg1XbCICZPbk-gD2T7JWLyA2xZJavAvkZsuQaLCmmOI91IFZDh2tZWuAGM3yI93o5ntTF3TouZdQg6PZvNuWVQ8I5icHJrFq-tixLnUc62jW-cbs07WXIByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEFm6zNfxXD9IK35OuulMlU3L74rOsQc7CMrzJ0Qwk0EY6qntmJhENgkISd5tcmgecXhcTUdgS3wFJI5WsuLlZCsuPVsZcOXBS7m9ACBF82SAFCDcJbRUS1m_t8gjTSP_GjWxjUyPNTHm7ynBoWsPIs0_1VwqU41nIzmxl4GsbLsDzMHWwf1ChZ9XTrMKnVNLtOekf1kycFbZ5kZhtzBXHdR4wF_R4wseVzSw0Mz4Cs62H3rPwok0Y3OTXrabAlxfBUv7DIEd4MOwjCHtTP6vT9dgpoylltO-Bj89LZl7YNrD5QbepUHUTGre74BmmT4tC-BXP3gVV59M_EjlL4CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrG9kKP1UxZ8esefZlE76Ux92BjS2wX6PGMPi1kn9hbNmE22g1khOcB3-OpRhuPgY1koIxheepJ_JWe53uQat8Z7vNEbwKsCZKtrCfYIvLrHrpeSdakSHsVoQBy4RB8HE9mFt-1_Ze1_EO-X3QWjkHIrKTiA4wIAVEPsS7R4236v2o7V7ykK1gZLfrjjkig_nOH5Lq4Tu_NwXF9GbVAhHdcMCPQpv0VrSaQVaPQylcuzk3nEmrcGOBRNWrUR0Ct3CDJslnTHAzOzFqHXqebJdOTKVdapbkPTxBntZIDS6PekD2woTljTfPqgIvmgePfo50oIzpqatR3uJ4sXcOqexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2PPQe3rvPxk9lqogOT_u5YsW38zLb87rn_KI9kGBYd1yRxwyr8noivixSUaViW1HcZDCKlH7euOuHvfbWhIM42jqkpkQFeE8XkB095IfawLRcQb2qS_exgQyQGJkAZDyGfs3yKkbSYOvxBaMlv6bAi5oB4zsrMfT9AerLdxBwQrXTj9n-mceWwe1ObVPY4dcX0OM0LMwOZUB6NDef03EY1pFKg31dIWjigLMocOxh_8htABLD0E5_tbfbExKCP6K3WYlaaQmwy-3gdMnbN8vQuXweLBNDz1aaMulpxK_To59EBf7aWRqE_1MJrEFyubzjg-uNdaldogWjYrNcREQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgIGEjtHKYU6UnaGxlu3RlbhBNCBqjVj_aIngomfAkpi4DDl8IsLeyVT5308u5h12HuTvxPYx1SEizVS8gmFylMCfYFZqf9yAIMr-aqlET8867qKN1igPKH3vjl5frd9iMWpdd4S5DZHFt9c3AQmyguknaFzCN9QDy5VpcFg6_bbZWHka7A1RGHhoPumkRuVMxUYFOx7CD-rZLxoVRbJpr_him3aWNngEG_XJ6E3ZSrQxTEQmci_hffsK2g3MHz2mfryV3pesUz0B9wOGDdK-6VsLM04ZWCszTK2THOk4eoWhwMvRScki_N-7cTNhQoUseezx1ebi3PrKgjvl_fbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNnJ5CMAG37nrUwjMPZ8_hDXMtAaXQcJT_oCAkfLOLCYh4Y6vXozjUclOU2GjYe6TFWz3zn9fATEsQGaJBEX8pPVnDrMXFZufZ3_3qVCs1M1XbXQOFfbVekiDzMZuZUDBjSBvcnjJB93ufluPpMfEmThpocoEJPNt_0nLNfg2FFxUi-sDOXthM385SLpvFZO7X_e6voh11e3Qni99dftOsss0NI3zN0STM5sJSaPti3AurIuSJzzhZ7OdqM1ZA8ovOCo9L4h8_vXnCdCvNWBWwBCH7drNQnpzI6aJkAItwIFHTZGxVsXeSsVxdTMwaKBDdiBG5ixFW5CeOa1zovs1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نقش‌ونگار زیبای بافت آجری دزفول
🔹
بافت آجری دزفول، با آن نقش‌ونگار گرم و کهنِ خشت‌وآجر، هنوز از زیباترین میراث‌های معماری ایران است؛ اما این هویت شهریِ کم‌نظیر امروز زیر سایۀ فرسودگی، ریزش و بی‌توجهی، بیش از همیشه در معرض فراموشی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/436058" target="_blank">📅 07:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436057">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
معلم مدرسۀ شجرۀ‌طیبه میناب: هنوز بعضی از اولیای بچه‌ها تماس می‌گیرند و می‌پرسند بچه‌ام روز آخر چه میگفت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/436057" target="_blank">📅 07:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436056">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
عکس امام شهید و رهبر انقلاب در کشتی توقیف شدۀ دشمن!
🔸
تصاویری از داخل کشتی توقیف‌شده در آب‌های خلیج‌فارس، توسط دریاداران جمهوری اسلامی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436056" target="_blank">📅 06:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436055">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM7NlhlYttmaY5E31fdr4tg753FbOj-iq-PgnDNa3OTzZ2fVyLzqFjtmDKoDZEeg8lgBkrPxgvazOJfNbZelGuPYeZSeYW8wgOtMVxP4BPO00sguaaKn8o43xZKjB25Q_W_Ygmbzof-twjrhjS1JQDYeG_h7ozIX6IR8L3L-nSIXoqAYMea0W_n0Bm8MRJ8wf7xH0761lru6mn-XVx-0mWsnWKQ8xEoB4BpjIoZn8yTqGxmVecnXicBJZwFCgCJuqlnWE-be4qUT9ctDWppfCnRN1ahwesoAcWL5hpESmjJ5plCu9rkttcBbS9CgeyAqXTH65vBD-3dSR-XjS0N3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسوایی پزشکی در دانشگاه‌های آمریکا؛ فروش اجساد اهدایی برای آموزش ارتش اسرائیل
🔹
رسانه‌های آمریکا گزارش داده‌اند دو دانشگاه مطرح این کشور، اجسادی را که شهروندان برای تحقیقات پزشکی و علمی اهدا کرده بودند را در اختیار ارتش اسرائیل قرار داده‌اند.
🔹
این افشاگری باعث موجی از نگرانی‌های اخلاقی شده و اعتراض شدید خانواده‌های داغداری را به‌همراه داشته که این اقدام را «خیانت در امانت» می‌دانند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/436055" target="_blank">📅 05:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436054">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcaa9f3eaa.mp4?token=Std_8tgtfMdHuu_CXIKwUwEkLx0Q8nSI_R6gsaF37n1ZS4CaxXZeb26NKNUuNGY8AKU585EbrnJi_cUwIfXplWiaVxH2yJBcweuwUNQroPvNg2neNfvz_bJaj8K1IZYdfut9_zwd1QiVaVMqgAO3ZyVkFDTsCw_oF1RyCDETsd-Wuy28HTEUtneQBDoJzQlZTc0125oM7G-pE_1sgbZUEwYYcivlR5owvbXcoEVA9zu3FgDqepcmwCdONzuQvj_AcToekChQ0So4DbbN-UnoVWxX3v0ApDF3E1TeaJu3EOum22CUOiy_knvBh1icm6_6jClni1vKArkmMG93nsucbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcaa9f3eaa.mp4?token=Std_8tgtfMdHuu_CXIKwUwEkLx0Q8nSI_R6gsaF37n1ZS4CaxXZeb26NKNUuNGY8AKU585EbrnJi_cUwIfXplWiaVxH2yJBcweuwUNQroPvNg2neNfvz_bJaj8K1IZYdfut9_zwd1QiVaVMqgAO3ZyVkFDTsCw_oF1RyCDETsd-Wuy28HTEUtneQBDoJzQlZTc0125oM7G-pE_1sgbZUEwYYcivlR5owvbXcoEVA9zu3FgDqepcmwCdONzuQvj_AcToekChQ0So4DbbN-UnoVWxX3v0ApDF3E1TeaJu3EOum22CUOiy_knvBh1icm6_6jClni1vKArkmMG93nsucbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حماسۀ خیابان در شب‌های نورانی اردبیل
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/436054" target="_blank">📅 04:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436053">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50621f1431.mp4?token=ivQJay-0hPv8uNB6SGrEa-1DwMUAAy6mgtL7YIwrnx51vhiqgcOAZ6G4B5FWhycYOgsNdtm7qrwh1gFJaLrTrtFb6KUOvuA2rzgUtA99oNTWXy7-XKIvfnkgdH11uIUKVKVrwffqm4OfBevm53aZulTQ_jlN16YWPOzhQi0eY9MUfjFzow06_mkkqJZqyvaMCjQnHsMN-usQ3VEpGlYjaT85ccCASGLWAOtGnSeCbVmmWuKfAXLUQfRKOxXoXZM9N4Wv1FshWhtv-kddi0KZsEdYhjnU0ykVv-Px1WC6mH13mSidccSIyx_qDOanZJecwl8roDm8FxF8Di73gDrzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50621f1431.mp4?token=ivQJay-0hPv8uNB6SGrEa-1DwMUAAy6mgtL7YIwrnx51vhiqgcOAZ6G4B5FWhycYOgsNdtm7qrwh1gFJaLrTrtFb6KUOvuA2rzgUtA99oNTWXy7-XKIvfnkgdH11uIUKVKVrwffqm4OfBevm53aZulTQ_jlN16YWPOzhQi0eY9MUfjFzow06_mkkqJZqyvaMCjQnHsMN-usQ3VEpGlYjaT85ccCASGLWAOtGnSeCbVmmWuKfAXLUQfRKOxXoXZM9N4Wv1FshWhtv-kddi0KZsEdYhjnU0ykVv-Px1WC6mH13mSidccSIyx_qDOanZJecwl8roDm8FxF8Di73gDrzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر انگشتان‌مان سند وطن‌دوستی ماست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436053" target="_blank">📅 04:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436052">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمدید یک‌ماهۀ اینترنت برخی مشترکان مخابرات
🔹
شرکت مخابرات اعلام کرد تاریخ انقضای سرویس برخی از مشتریان پس‌پرداخت فعال را یک ماه تمدید می‌کند.
🔹
بر این اساس، مشترکانی که موعد پایان قرارداد آن‌ها از بامداد ۲۱ اردیبهشت ۱۴۰۵ تا پایان روز ۲۰ خرداد ۱۴۰۵ باشد، به‌صورت خودکار مشمول تمدید یک‌ماهۀ سرویس خواهند شد.
🔗
جزئیات بیشتر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436052" target="_blank">📅 03:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436051">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2562f833e7.mp4?token=ZIsrmx3YNq8Zdyb2B0G4G9rT1EV7IxGOvFoGgV6WTpgd00k5m8KHHU_-ySIViitxsncswCBjqABTIQanUzGTsGM8ksEGqX550I6-pDxaFCBwYdaDX_r4VcWGwjh7LtHiKiNEKkyqKw1lLQ_2rDlg-ska_Y5XJm17i2D1ectOuGTtGWfqdzdSUlAoYRJyI2-llGde3GQMc7k7EflcEL5tuGd0qhGpNnCgcl7KgF4ubcYsa067uWSbimrBd5erz3M-M9qa9pXOO_ZlescKFMs972Z4hGWmVMcQlXzT7J0LZQPE0wreHMkm52_Ivpj1wltxLO00FFYbYrkZqlNbqPkUax_HcU2O7EWNidsPm0dGLHnUhLAM2r2XMc8ZPQlsn8Z61MIexC8OlQq-za0hQn5AeIgMkjAmH0c3NecTJFWLbGHqZe76qwubeCvDmgIEoAq1-Po-kJpd3y16OWd8hgeu7cnnIYHGltNMqvfrN9MyX8DeVYLg4vAbDGfU9IogztN_LbvuMzUGZKueB_tMG68CyrI9qJc5bTpuIo8Vys-KFhpwvbmlNw4pO3F4hSG-tXCW5_Uo753xzym7istu9gTDIHbicgA8nBCD3HCaCIlBpvtOH2IQgpT-qydWG-wo1VC4fvjULUSPNn4g5gRPHJ_Xuv1dcjlV9uCeyTkuT_z2QBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2562f833e7.mp4?token=ZIsrmx3YNq8Zdyb2B0G4G9rT1EV7IxGOvFoGgV6WTpgd00k5m8KHHU_-ySIViitxsncswCBjqABTIQanUzGTsGM8ksEGqX550I6-pDxaFCBwYdaDX_r4VcWGwjh7LtHiKiNEKkyqKw1lLQ_2rDlg-ska_Y5XJm17i2D1ectOuGTtGWfqdzdSUlAoYRJyI2-llGde3GQMc7k7EflcEL5tuGd0qhGpNnCgcl7KgF4ubcYsa067uWSbimrBd5erz3M-M9qa9pXOO_ZlescKFMs972Z4hGWmVMcQlXzT7J0LZQPE0wreHMkm52_Ivpj1wltxLO00FFYbYrkZqlNbqPkUax_HcU2O7EWNidsPm0dGLHnUhLAM2r2XMc8ZPQlsn8Z61MIexC8OlQq-za0hQn5AeIgMkjAmH0c3NecTJFWLbGHqZe76qwubeCvDmgIEoAq1-Po-kJpd3y16OWd8hgeu7cnnIYHGltNMqvfrN9MyX8DeVYLg4vAbDGfU9IogztN_LbvuMzUGZKueB_tMG68CyrI9qJc5bTpuIo8Vys-KFhpwvbmlNw4pO3F4hSG-tXCW5_Uo753xzym7istu9gTDIHbicgA8nBCD3HCaCIlBpvtOH2IQgpT-qydWG-wo1VC4fvjULUSPNn4g5gRPHJ_Xuv1dcjlV9uCeyTkuT_z2QBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هفتادوهفتم بجنوردی‌ها در میدان دفاع ملی، در شب شهادت جوادالائمه علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/436051" target="_blank">📅 03:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436050">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqO7gEIZ4idYtECnlnCTEe_W7F0gU9DLDvI_FZ12hCPm3HQFV79DROQoi90bDXyAKHo7WUKYx80reQZeV677i8G7BdVXOwZiOKdKXFCBnyF5YluznFDISBAkceFp31CEyWU2iT6zOWKhuCUeCUc3aYpST7NIcnCyBr_-dR9j8mQD76yBOV3pSmrBUEvgrD8_fhnT6Cl54OG00iaOpG-9rtZYIL_PHGT8zQf9OSjefntZwYyupbbDuvlAT43uKN0ozCqPvF4dSmmYzu1gApSpSUutPMFBaA-ZgYg8q1_Ig1Z_0zj5SbPZqdfCQiIBp-UQTRqsi5yaEtdiiVFIIvbCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف بُن کتاب برای اقشار خاص، در نمایشگاه کتاب امسال
🔹
خانۀ کتاب‌وادبیات ایران از حذف کامل بن کتاب برای اقشار خاص در نمایشگاه مجازی کتاب خبر داد و اعلام کرد تنها تخفیف کتاب ۲۵ درصد تا سقف خرید ۲ میلیون تومان برای همه فعال است.
🔸
این درحالی است که سال‌های قبل، علاوه‌بر تخفیف برای عموم مردم، اقشار خاص مانند دانشجویان، طلاب و گروه‌های خاص از بن کتاب برخوردار بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436050" target="_blank">📅 03:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436049">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8837b94349.mp4?token=g2enLBGAY00EojQAIhZbAb2-oy3T_0vSxnEa8kGBEEPELCOwFJ1OXcA9Z12sCAhPAKu-O5n4g97iNWE8-wp3fWIWbY5ia561XPXzvY2rEIBThvfDWQUUD0070NcgKLNFXAIJp92zzesubF1b9KgwFIE8jiWwtm-JDKvhKvQNM6tXri7UlnkhXwf08gB2kULYeidDIBYXcg2f-AFUsrQO5RhDCs330mB3qbdk1yHTLDChJM7npLrrWzAsVJdJLgvqWQsbwGE91Gtc1HTMKTg_LBufFGzpbJaXRXThmpTEic0HTRNohUkhWsAX9Dbc9gH5QShxzFgSQGzyGZlQtUD4yVcxWnwKb6_h8EDSRTf-GOOq6VHPONEF4IxkbkxsJmuGfHcgS49SnLuBrje-ntH1gaCqoPN_Oka96X6HFPDgYc9mqck5VoDrkeXA7HGtz2KsR0piyoWHWk_wZ7qrIIUmU_Ikdicz_fX6-y8jpJ_RmeXfowu0734Yn3D9O-YGJWmCwDriFchvFBONaAHafzrdbSVTAA57TE6WZQS1cV0WduY5bL1si1rxXMspWwOvq4swg6QhIAVzgEMvDy9036grYj8XzxK-4C-u41eaaPCQ9pBuyA7sUzFSbHPGYnFtjSqECVW-o6CwcttmjBC9Et-OR8kciSrRxDVK9hJylpB5D1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8837b94349.mp4?token=g2enLBGAY00EojQAIhZbAb2-oy3T_0vSxnEa8kGBEEPELCOwFJ1OXcA9Z12sCAhPAKu-O5n4g97iNWE8-wp3fWIWbY5ia561XPXzvY2rEIBThvfDWQUUD0070NcgKLNFXAIJp92zzesubF1b9KgwFIE8jiWwtm-JDKvhKvQNM6tXri7UlnkhXwf08gB2kULYeidDIBYXcg2f-AFUsrQO5RhDCs330mB3qbdk1yHTLDChJM7npLrrWzAsVJdJLgvqWQsbwGE91Gtc1HTMKTg_LBufFGzpbJaXRXThmpTEic0HTRNohUkhWsAX9Dbc9gH5QShxzFgSQGzyGZlQtUD4yVcxWnwKb6_h8EDSRTf-GOOq6VHPONEF4IxkbkxsJmuGfHcgS49SnLuBrje-ntH1gaCqoPN_Oka96X6HFPDgYc9mqck5VoDrkeXA7HGtz2KsR0piyoWHWk_wZ7qrIIUmU_Ikdicz_fX6-y8jpJ_RmeXfowu0734Yn3D9O-YGJWmCwDriFchvFBONaAHafzrdbSVTAA57TE6WZQS1cV0WduY5bL1si1rxXMspWwOvq4swg6QhIAVzgEMvDy9036grYj8XzxK-4C-u41eaaPCQ9pBuyA7sUzFSbHPGYnFtjSqECVW-o6CwcttmjBC9Et-OR8kciSrRxDVK9hJylpB5D1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم مشهد در حماسۀ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436049" target="_blank">📅 02:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436046">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJqagy4uuIaTUw3r-ROCA168fwTRV1os1EKPS-rsMOw0WQux2Ifnv2IS-tb0aWELt_817hTqjN2o-bBBAIMWF9Ul0eMNxyBpQKrrl8smKYpwRnSr8reuHlrqfkuNYlN9t1dpBlmuXE2giQ_0sKtEqDTAIh_SaH7RoJjkklXeHlAwea7EQmOn2uiHUSTIwqVI1GizgUv6NXp-y_OLtabIzJ0pGOaPRpl9Unk4wP6NkfPwmnrjNyQRAphR5JgOwfP-pyR-YWk6k9Oh2a6UWUAdgPHsnoNUWvqbPl3MQUyX5PSugjdb8e6WUQNGvZWYJvyIhd3NzQqm324tcXLuNk7mjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqMxNk2GlSPXBaiARIOC8cc-sen4A0yvcykcDpa4Opk6gWqbXoXlHYpD8taOmm9I-0ifUDh3qt4hnH2yWxsNvJbWQwc5HTZgxg1QUcvPw90HiDLddnAMJDElu6ebL2UQfeyIlmJ74k5z1gacSoV2gDxkozJkCzMapC6BQRsY7N_5h7qeQgrU5jDj0aED0EG-OCTvHoO-yHQ1cdyfeEOmo7rWBm63pcpq7yN-nD2B7EBfXoRb1zd0cmv66z9Jk3C9fb4VnljBUqJUAmjYplKAsbaP0yPABhdzOiT1yWgWPoh8IJau5ws9EIETrvLNIQmwVY1j0qRaD9EcBrju7uC8jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2670167992.mp4?token=DRCDtLu9_Ian1DZZTB1b2hHWraCCRjlMxpegab6CL-BY9nkSKKIoXCLn7m0K3vozoPCGqglJq1wWj5Myn7FBI6dxn0jyvbeTSoPAQkKAsmD1dmnaiMGbJFxvlUtjguq4NH_6jNDfZks0oK12VmcHtt4-XMlK-xY3M3L25aSI3PPbvtBRKdYthea0wa03FftMi3mkhHrzPhMm7hd3AH9EmNe09_P0u00cKKB4rxGxbuHspjss1OPrnaWU2m4w1aFWhwMbhLPATKcZ7r4xpvgoKNQ2imqUQxxfrVur0JDTXRIq9kBkQrfWkWhyIICe5cYanauS-PyvMbkx3WQFSkKulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2670167992.mp4?token=DRCDtLu9_Ian1DZZTB1b2hHWraCCRjlMxpegab6CL-BY9nkSKKIoXCLn7m0K3vozoPCGqglJq1wWj5Myn7FBI6dxn0jyvbeTSoPAQkKAsmD1dmnaiMGbJFxvlUtjguq4NH_6jNDfZks0oK12VmcHtt4-XMlK-xY3M3L25aSI3PPbvtBRKdYthea0wa03FftMi3mkhHrzPhMm7hd3AH9EmNe09_P0u00cKKB4rxGxbuHspjss1OPrnaWU2m4w1aFWhwMbhLPATKcZ7r4xpvgoKNQ2imqUQxxfrVur0JDTXRIq9kBkQrfWkWhyIICe5cYanauS-PyvMbkx3WQFSkKulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله با خودرو به عابران پیاده در ایتالیا
🔹
مقامات ایتالیایی اعلام کردند در پی ورود هولناک یک خودرو به پیاده‌رویی در مرکز شهر مودنا، دست‌کم هشت‌نفر مجروح شدند که وضعیت چهارنفر از آن‌ها وخیم گزارش شده است.
🔹
پلیس اعلام کرده تحقیقات برای کشف انگیزۀ این فرد و تعیین عناوین اتهامی او ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436046" target="_blank">📅 02:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436045">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbqwW7m1MSXOjwxC3qDOg-cyjqHDZsOr9kdKLMLlDjVkwvTowXbx9zuPCA-o0mUBrOYtNDyLQ6PXKDvb6bJ_phNWFqMo6vMwNpZM2RYc9P_0r_zA_j96-WnUwp8RrW1VakOZ7rPw7LKQe7XQtf8HX_gcJPiVBS8YVCKPB0ns1CPrTcB00M5aZjJqfTk31wpeljRqr71uRyBTgAboVBk8R0MvC_4rUUa0Y6tkyx69fpvNXZc1S3k3JnTSbKNETXTUpqHXNSb6kH3i8hhCpOczi7Lgr3tEsxH1HM4oY3FyY_IBUyJRXfxiH3uqpXlytqHI-Oodn3asqp0Q5Fop__rg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: نخست‌وزیر انگلیس قصد استعفا دارد
🔹
روزنامۀ دیلی‌میل گزارش داده نخست‌وزیر انگلیس به دوستان نزدیکش گفته که قصد دارد از سمتش استعفا دهد.
🔹
وی به‌تازگی با شورش در میان اعضای هم‌حزبی خودش روبه‌رو شده است. همچنین بیش از ۹۰ عضو حزب کارگر در روزهای گذشته از او خواسته‌اند استعفا دهد.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436045" target="_blank">📅 02:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436044">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
کرمانشاه، عزاخانۀ امام جواد علیه‌السلام شد
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/436044" target="_blank">📅 02:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436043">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات گستردۀ حزب‌الله به مواضع رژیم صهیونیستی در جنوب لبنان
🔹
حزب‌الله لبنان از حملات پهپادی و موشکی به مواضع ارتش اسرائیل در جنوب لبنان خبر داد.
🔹
بر اساس این گزارش، پادگان «یعرا» با پهپادهای انتحاری هدف حملۀ نیروهای مقاومت قرار گرفته است.
🔹
همچنین حزب‌الله مقر فرماندهی ارتش اسرائیل در منطقۀ «البیاضه» در جنوب لبنان را با دو فروند پهپاد، مورد حمله قرار داده و خودروهای زرهی اسرائیل در منطقۀ رشاف و حداثا را با مواد منفجره منهدم کرده است.
🔹
بامداد امروز نیز تجمعی از خودروهای زرهی اسرائیل در اطراف منطقۀ حداثا با موشک مورد اصابت قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/436043" target="_blank">📅 02:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436042">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">«افت شدید توان رزمی» دلیل عدم مشارکت انگلیس در جنگ علیه ایران
🔹
شبکۀ فاکس‌نیوز با استناد به دو گزارش رسمی از اندیشکده‌های نظامی و پارلمان بریتانیا فاش کرد، دلیل اصلی عدم مشارکت لندن در حملات تهاجمی علیه ایران، «افت شدید توان رزمی و خالی بودن انبارهای تسلیحاتی» این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/436042" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436041">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
مردم شهرکرد ۷۷ شب است که سنگر خیابان را رها نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/436041" target="_blank">📅 01:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436040">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5IhJ0hCiT9I01SjvvnBjBhKIbCHdhpjes13h3ocXVvAStYN99MWg9ytyYkEOlfEwKBbZ8tDQ-azKkZ4oHDwpEpwyY2Q359CJCvoOnzZ8_ee1oAVrV8ll9aqI92o7n6fQ5XGFn3O6sQgJFL8o26q9k_rpUpnPfaXkUaNR9xvEwWujRXhNoXz-OPVEcH6OCWZLduRfEmx-m5l_tTlUgooAr3bhPQvyW9cXS8Y_F6-XascwSWPhhmUJSHtf3VNwyIRYqmZnPZZj5uov4N8dA9JOzViZqswuLR2kKzoXVQCHvTb34RHl-PbTNYee9HsKzw37qcKFrqeV08VTTTQhQfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیۀ وزارت امور خارجه دربارۀ ترور فرماندۀ کل گردان‌های قسام در فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436040" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436039">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی سرود نوستالژی توسط بوشهری‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436039" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436038">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfGNUYt-3IKoXMl7l4ukTpNlj7P6CoghjsWi9irJPvqd1-b7LYCRY_gzOrBbsErmcVWwpQaacqpuU2C_jSGaz4gFY0CFEiUVQRH4gUoaaFm1_YX9NPHnbHttNYTBPxUxT8m9dsfZeGl58AleqWnmDBGIpB_7Sg6o9Xbm9ejS2YN1pcf_aVhdBlHmOP12K0Id8LrBBUTtg2rRJGYLnoc2bNYEJaKJsi7j3WlTG_sb9os_PX9m10wRQ48nhTwNqNQBZ-1aUGq48P5Mk3HjS_ZPcBp5D7xB-lDZU1sndhGGZcBc9cyIrBEX8Suu22SQTwBGP2V5pR3GrWVRk_oOzh8lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس مشکلی برای آسیایی شدن ندارد
🔹
باوجود اینکه هنوز نمایندگان ایران برای معرفی به آسیا به‌صورت رسمی اعلام نشده‌اند اما گمانه‌زنی‌هایی در این زمینه وجود دارد.
🔹
گفته می‌شود شاید برخی از باشگاه‌ها با مشکلاتی برای کسب مجوز حرفه‌ای روبرو باشند، که از جملۀ این مشکلات، می‌توان به پرونده‌های باز مالی اشاره کرد.
🔹
حالا یکی از مسئولان ارشد پرسپولیس ادعا کرده که این باشگاه مشکلی برای کسب مجوز حرفه‌ای آسیا ندارد و درصورتی‌که شرایط رقم بخورد، این تیم می‌تواند مجوز حضور در آسیا را به دست بیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/436038" target="_blank">📅 01:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436036">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2mu94z5vDXFjn49qvez8lzce-enl3rftq1ls6fqwSOlEFEhYsUx2v4Xsm6iJOJ_0k4b5gAg2gqYUOus_8cfGm-JPbyDuv_pWVNskZmRXjAkrQSdcPiE-60NwFAWGFKNl4vI7NjYqKnFHbNacEAU1CinxL3GFNCsC3BDEeX6lr_OkkVZLphnNLKqooUrBUOl1u1SiLsZ15e7Z0mxF0rS-ZTz0Ks0NaUQu0XOgtL8-KjzRk2eE0aoWRvN-IdBzhDSpwVo4tcfDE84AmhozXNXVq-o-5_ar1hoIEv5YSGnwPRlvZVFKMP6rh36FfQdOdFpOTsS_ekKixtuxJn2PUhLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو جنجالی آمریکا سرانجام به خانه بازگشت
🔹
ناو هواپیمابر «یو.اس‌.اس جرالد آر. فورد» که آمریکایی‌ها از آن به عنوان «بزرگ‌ترین و پیشرفته‌ترین ناو جنگی جهان» یاد می‌کنند پس از ۳۲۶ روز حضور در مأموریت‌های جنگی روز شنبه به بندر نورفولک در ویرجینیا بازگشت.
🔹
این ناو که از زمان جنگ ویتنام تاکنون رکورد طولانی‌ترین استقرار عملیاتی یک ناو هواپیمابر آمریکایی را به نام خود ثبت کرده، در طول این مأموریت طاقت‌فرسا در جنگ علیه ایران و ونزوئلا مشارکت داشت.
🔹
جرالد فورد در این دوره با مشکلات متعددی از جمله آتش‌سوزی گسترده، خرابی‌های مکرر سیستم فاضلاب و اعتراض خدمه به دوری طولانی از خانواده مواجه شد.
🔹
گزارش‌ها حاکی است ناو فورد سال‌ها با تأخیر در تحویل و میلیاردها دلار بودجه مازاد روبرو بوده است.
🔹
یکی از بزرگترین رسوایی‌های تکنولوژیک این ناو، خرابی مداوم «آسانسورهای پیشرفته مهمات تسلیحاتی» (AWE) بود.
🔹
این آسانسورهای مغناطیسی که وظیفه انتقال بمب‌ها از انبار به روی عرشه را دارند، تا سال‌ها پس از تحویل ناو کار نمی‌کردند و باعث شدند منتقدان، این ابرسازه را یک «آهن‌پاره بی‌مصرف ۱۳ میلیارد دلاری» بنامند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/436036" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورایی تهرانی‌ها در میدان انقلاب، در شب شهادت جوادالائمه علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436035" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIgK3yzuV2BeBWcOZDEuoe0jOYkQzPct9wH_YIRp6x1t5phylkGgRyGEwIrlSDpH2yLQS0nfNxQD43w1IRfzI6sXx7c4vXAJJ_qrBNcNHfTNB-S5MH7FHmtRmP5VwM3_sojv6NoI261bacizzle2VKOXtFaHPoRihtW64K7ZK5jZR0ncbBIN5Nz38vYt3OnQ4mZY-a9kODlCK97sqj7unQTKHTFEPkveT7CsQ7vX6NKzpZSe7r_BIwq04wdmQj9HlvFh6KUGjX8snMEz5ei2hwPqoXZegcMzHTZCtlFZkTQZGjKhhsrRpfIxwiM5Z0M7PAHRGlVuhF9ge40A4sZrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4JyAJIys9fwRyLJ-mpznkan2aiNtM9VWNsmkOjGVhOrdqs4LYB5ZqeC3TO6pkuNev3-lxMhfyKs6RB7-sKidgaBn2Al_F5QVtwZJCrfoon8pShNiWFitwaPP0Tlbkttw-rtyX_D97TNFNza9YQlP3OaEAPVP9eiTlUUvCmQMGSEgjDlnhEjkbNBREenC-ONG8-1ndOGzvgeMP8I0A2RSPO505wag401xMJo-Qxib5lIWeSgEPMMHwYT0VndQ7CsCiBBUEqggC5xwmNa2ISwnCy4o2j5qruczhJBPBp1KOUYHje7GiCkn2jc0KalqnabJbSvj9H12xqA4Z-HyMCjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhZyvp5_9_GaVd-HPbi6LxmoJ-3BmCd-BQIhK17nR4a8JGkx3-QE05iYTaLTLy2Wisq8RZjQGAtFs1NMj4CPJQryf4hzmecAePNOxjkI8sJPIA5bD-MywHI02eVYb22iUA-OapLq9d13tEyEDCWLbW1gpPg9B5t24csfKyzDUId1GaYWe6599tKz-TXm5wV7ywLUV4Y2WQNILZRqWSPxnZUATLS3UqqkC-oeoO_MlNhtc-RIG3X0qkrNz2Km13nsjogVyFHrYedmWZzlQYfJcL4V_kjKLzRZDAVUlJAzXA8h1VhZ_q9Wq6ptyTkZkjIDLBMR8kCFol74AW6PSwCoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiOC2lUzPqJsC83xAvdtsbfTdjlYS9EMtfoOA_zKtxbuZ9-W8Ns50Mz6Ypn43R8c3PNk8Vg7ozlBGWNfyDhpO1XF1rJxuuYuGo-kH81XhqI2Z3n1qDty6GdM2xKjffM3N0aYD3cYS51aHEh5G1eDmfOrmrWPVFuxeRTuLsxOXdnf2znD00-zmA41lF0H1sLZ0tqfvt7qb99zZ3TtT1Q9Ju9t8GCB0TdwgBbHqF7HT7EdPGVwzsbr4B6Y6w436LXoO6hRyVJjAjzUJRrOE_aSSt1Ef4RZbz9trGnq6C_We-ZcBN9Rr645WGjZ-W2gTOJPyXFTfrWatp_EgbD69AcNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKKduC4IoVAbrPfMsbAyy0ASOfSLI-LAKJEblZUNzWM3pqKnMtVomO1CZ9ds_yUkJHCILmYEbLwl4e6ljKtkjJkEiBj5oPdCs6TUAhiklTauMV_oaNnIRa9A-b1EmlMXopWBI9YIt0pFD0aprfJaB3KsDDQe9bzMj7MePdGuETSNc5itX2J1JOUG3mB9pXuHGnn8SK-TDXb4yScD5iXUaEt3s8cPbQePumVJCu0inmdpkMoOirTYv4j_j12go9FgYyYtdnUFTte-1fxz-hYicaFPkPqbiL8Cl6grahw-UyROlzNw7j83on8cwGDoTLbmociqjWp0HUxYKlrrFElrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۷ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436030" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN9dG5feGevYBznWq2KvQeVcl2qW6k-CXs54xrpkEriRnC9qEXpM2ojFM3sxB4TOUuxPbidgyBVZcKxizgSKxm3XDr3k5k67ySUeP1nbpO55_IzUqx344Ppj4JI_5NlnkSiOzKdMa5ukON3vKHyCV9d3Y0P2tGioDoCJJNdjAOUu0bzGkm5-wTlwu63BqXuZjHk_bJ_I9iYFMFqkrISTT4h2Wk4oQ1JJzUxklb4Rx7h1Ykb6C35MFWCVcD11RtuUaBZwGE7lz2ED5oiAEORdfs08KSuhNV-CvLSJRMIY-AwQshqZnrBiJ_qWwXTSVXwMNG8Jmf10N8XbNQrN97C5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZYmeiJmTYEA4q-_UGMiO8Elda4raezFtOJA91xVFIOFtiQq2dr_96zogLChpf4jlNJN_wafKBCwQa4N47DPGCMDsq8n2os4wgiX875i90rbbDFRvl84v91n__pZFmlG6KGTwBXKITuFMi2N4iQIGyI_HKPvXggl6Pjh1qfu0CpSrar5vLKEKWS9lZU8Txyc04GMq7RBJaA8kAfOaTXUzWPOaMMLB715MQKHEH4Iq2dynDFxAN0xfHvtLE6GeY8eFQaGuRfKSwbXvrrp84gepntdMCLHnDGBzPF_fG3rDpSgTDoz-43INcf-QcvYj_grwaRkzhDBk68uX9DgG2vHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9TFK84mrR3nMgg1uTJsMHnpDEmH0q4KKBSseq8HW6DVhfptlYoZkwV4ax2Vrq_gIvypaf9jWep-_4sp5VygGuhrZadHfRbXCqDGSNNhYx7brg7Q9NaaGwch9Xm8ajQ437LcULvP8SaQXwkJq8cVenhSWk4csYHlRg-89gNnJYENQkzy_2c4j4kjqvYrpki-LblQE5cNwh_0m_trvlnVOUPZZWBAqvtx7eRPnusJUNwQG1OuUxzpGdVt7Cs4KRMDbVftWUe0q0ly_9SNzOwgixtR-sN_VNw_Of2bre0RXSYCM2Vvg2ch8nmWPVUYHDWxl5quh-QOeFJIuhUYr6zuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfSpSLPCtprlhAv6gFkjwD6XlJ8lRhWWxFOII6J9LLFqX4toYjb4431uzVjKtnhQykQCo55Z9k_tBW-pRNqXgb79y-UiDMXvDIOWqs5v68hzPimQRf_gsD-lUBSAvzt5cEjLUiPyqK3vh-P4w43nHISYCwUilWv1hoVfKEw48xiRVjs7a5BPd875tz-d7i0yJJ5gpr96kdS0WyWldkI9F6RK_3YPbR4viPlsb6-tQRoqUHAonJ_Z3su0Ba3gU_sErKH3wx5FeD9NPX88U4SWyFapqeCsPLOssb5P0KhnRDvcGAYIxwgny0K1GCuSIJdwDabOOzXdP_vvvUW0G-p4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOgTzrWaocC8DUnK1G8OT0u0pLLJ9BDfmZwmnZfxvJOvEaAc84lTFJXPil3gDUgT6j3dGxpV4kfby-rK__R8Rkc_gfxBdEJjEoRA9QdqfbIH8zhrSnxwrlJsOANi0LSiqukKpvv8TeHhXxHG80nbKtVGcchBqEU7QrBe8d2h8CnGlAMBMI8dYqaUsPM9eu6oRol_W0JUlBNE_1lCGq2oDXvszRJ-m8qyIJWduLDdNpM-OdKTuQnxlywqFP65TLFRsYrxy6m783wSS4x2CMMG_c_Ciavdcio2R18leIg1sgDF0aKQjm7Kgt7xiDKuLbfFc_AAGDy89lszpc3vEbZ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bdffc4vkQalLOcD486iZLSnKf7kZ_XxHavjzwZGPAmnpkTB8vol0QelQuHYxW7MzeYsuXj1Qknc8EJuRpSfobMxO_TqezAn6BjXVy62_2a8mUI1LsWnD8NIyymlYKyizepPbiWeUxCetG-3wuj1-qYEFidba6oFSDoiPiLB64VLd-fXReeHvdNd71Tgwhqf46eS5yKzkTXN2Ck2S2o5jyVQXh3kjrdbWPbXI_FSrhXrcqoeaBauU_cu2RM30tjnam1ij6Dn8fBbSYlVA9g9N4ACXjRD0Ogj8rC5NBZRS6LvZs0hHNabVGy2d44iZqKLRCelrHtecR9sUBq3CH8rMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3sfW39HmcZbAXFyTD4IdPomHjRuucXcaXCGZgpZTVAUrfCo0lJSSDueZh1qvyZFWadzvr92orhAjJPvv7AnD7vRubZSN8XtveuLOPUp0zf9IXJ9l61zie4sDKV4mWW8DW5VVeqsLHUbXUPOy6LwNxDbpunURBcT8zCeoZB0-97ieYAGnFH4sVLW3SRxUzgS5aad0p5rncg5n0oGy5i-GPFNHAEzOckgks6J444s4nWPxbfeLOcHkDW3VMKqPw6sg8FwBLZhj_7ZUYIplPLHSqJDF4Syt8ArT07gVI5DgwPqvFYh4sWWSX_Oj_w5V4iPqQe3tWUr5H-HQBPPC8JoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAdat1ofGlrw9OrQMkAeFGXMex6qEAMfvf0vNC0OEUoVxFWDOeWhAwSGDgFR_kpGDzyZ7cC33v3N3kwjYa-1u2_TDBT-OTrM-sHon2GkJKV84cl-M_A2KyHyrlYgLCqMgJyaua9QoYqvFF5ByfBAreDNTyjwjPi4Kr7lZ1cDu-YF5uMA5M4wCJiFkfZva2MsVn_eLNP3iV0TzR6dEhz3Vcj-gzG5EHV1Lqt7xOR9SPctSWJ-Wu1mYmaFZIkEzpZCxQ7k018lt6PKjk8Ff2EYj6k5yxCvILGZeBH7QCo4lDhMIRSwhmHxXn3__HXL4VS_U_UaWXTUl7qXwZkHsreLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6UH0Oe0t1OrwurdPB823svpIMrf0UFE_-ABsI7eCyzXUukVkmoOQLfOm2rKph5TGrlz0FDSehjzs5L7affimYrJfyVpi-kplcCLD05JAQK-r01Z6CLsQDQwZ20ABtwrINmMr50PmsIJeD5B1GB-slapZPqCqZMU9OiNXomsCRYQgvX3EdEGxDmvNRu4m2RcTLRLb6qVJ1rd6rg5gBY2Qj6azzkiYkfCzMTCS7cM7gIlppF6qZRleBqvmnptXmx1F2UCyAdp1jR-cQXg0-4XSp8vMY_xNhu-x_3abRkX1LCPc9jJNvCeLEDt9YKr6U5f544O03Fp75i0_Nf6pHBqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULqfX2e3NpixDRlVSAM1GmpyfXg-ncuZSpnMfgYV-CccyoIWiBRLzHjZNvY7YGP8py1DGPiZN6AmP1vjEB5uytA23jfR9bXH0O0TXutbHQxDQsHRs2kYeKEF-FjFnKkoY0f7_jSASZ_swfCVqzQsxe20t8DSu53aUMkTq2fFmTh3jQBJBYaPiQVkHlo3IXWNU-uhERUa0RYCmWN9fpS_5PUoGJqICw-l5fl4zQ27B1G7EnFsmVIeZSbw2FCzzb5xYGAS2kBFmaMqjThs1vHqUgIDLK67qXPrx2BXiaBy0ldhKpwUNNKkZzg704_ZT8FMkXdMtB8MNDAwAv6lZdDGgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/436020" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_6I2ZZgVX_EUZzKN3bmXdYhYpOjo7HingeU5nUeErkTPTvnacRCd3dGTiBhnI-HQjlpRojvqR4AEfXWA5JLNcj4vKnWlC-QLjZwte4eUNodVSUYgfj7E1td8G-tpw2qqJByYoFA8kgAlwPo--ptfIob7c_D_OVngyGd0syP1J8qUZak29zTdyJW3u6KhufiPsD8kSPEMXSTmiP1fXGuXwjl-Ey7DUKMiWU4Wxc8jr8ccYMi7SVEX8Wn28Ah9b1QKPn_nTNDBJjS2NpdsI2AFHZVjlNiVexi6G_kQqqkLHM3Cv8NcfxlGHAecBKOXSOYbZOW9XIoPN8rbmlwXlOtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اتفاقات مشکوک در انفجار بیت‌شمش در فلسطین اشغالی
🔹
شبکۀ صهیونیستی کان مدعی شده که آتش‌سوزی مهیب در بیت‌شمش واقع در غرب بیت‌المقدس در نتیجۀ انفجار کنترل‌شده صورت گرفته است.
🔹
با این حال، کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/436019" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436018">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
در نتیجهٔ انفجار سهمگین در بیت‌شمش آتش همچنان شعله می‌کشد  @Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/436018" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436017">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ ثبت‌نام وام یک‌ میلیاردی کسبۀ بازار جنت آغاز شد
🔹
مدیرعامل شرکت ساماندهی مشاغل شهر تهران: از هفتۀ آینده با کمک بنیاد مستضعفان، وام یک‌میلیاردی با بهرۀ کم و اقساط ۵ساله به کسبۀ پاساژ جنت پرداخت خواهد شد.
🔹
بازار جدید به‌صورت موقت و با نظر ۲۵۴ کسبه در نزدیکی…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436017" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436016">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/436016" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436015">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3Axz81fA_VJRg0yYp3kQRecYOWSG5lsRoPamKu0Q20q-vI1c9teOFgwlfjXutboguR0uzeWslS85elE-7aYGNlZZIZpFq3KSQXKmv5tfoU1S2hF-yg755PGHF3Kh8EO_Rcp7K2hj6Hphsh3Ms6xRWBdA1BiC6chw37JvWddLLo_OW-BJgXTEgu92as9Zf_-awuYlxHcKMywTXcOPWokU8cYJDA8Co8ofutE3jpIjGdupksTRvwubRLNONnTtETTHaeQNYa4VEazMAZ5KnGKaMOtksaEXsMCJ3wnrPE4LtOolJSdxaT3BdByyL1Gpw9N5rVeL4Rde3dSlmXAvwF8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلیس و فرعون
🔹
روزی ابلیس نزد فرعون آمد؛ درحالی‌که فرعون در کاخ خود نشسته بود و خوشه‌ای انگور در دست داشت. ابلیس به او گفت: «آیا کسی هست که بتواند این خوشه انگور را به مروارید تبدیل کند؟»
🔹
فرعون که ادعای خدایی داشت، در جواب درماند.
🔹
ابلیس بر آن خوشه انگور دمید و در یک لحظه تمام دانه‌های انگور به مرواریدهای درخشان تبدیل گشتند.
🔹
فرعون مبهوت شد و گفت: «عجب استادی هستی!»
🔹
ابلیس گفت: «با وجود این استادی و هنری که دیدی، مرا به بندگی قبول نکردند. حال در شگفتم از تو که با این همه کودنی و نادانی، چگونه جرئت کرده‌ای که ادعای «خدا بودن» کنی!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/436015" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436014">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">هواشناسی ایران اسیر چشم کور رادارها و مدیریت غلط
🔹
سازمان هواشناسی ایران به‌عنوان متولی اصلی پایش و پیش‌بینی وضعیت جو، نقشی حیاتی در مدیریت بحران‌های طبیعی مانند سیل و طوفان‌های ویرانگر ایفا می‌کند.
🔹
با این حال، شواهد میدانی و اظهارات متخصصان نشان می‌دهد که این سازمان در ارائه پیش‌بینی‌های دقیق، به‌ویژه در بازه‌های کوتاه‌مدت و برای نقاط حساسی مانند کلانشهر تهران، با چالش‌های ساختاری و فنی عمیقی دست‌به‌گریبان است.
🔹
وضعیت نامناسب شبکه رادارهای هواشناسی، ضعف در شبکه مشاهدات جو بالا (رادیوسوند)، خلا یک مدل عددی بومی و منطقه‌ای در کنار مدیریت ضعیف از جمله نارسایی‌های گریبانگیر هواشناسی کشور است.
🔹
به‌روزرسانی و تجهیز زیرساخت‌های دیده‌بانی، سرمایه‌گذاری بر توسعه مدل‌های بومی و خروج از انفعال در برابر خطاها، ضرورتی است که تأخیر در آن می‌تواند تاوان‌های جبران‌ناپذیری به همراه داشته باشد.
https://farsnews.ir/Economy/1778961014305887280</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436014" target="_blank">📅 23:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436013">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقامت شبانهٔ مردم مازندران به ایستگاه ۷۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436013" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gClF8lpc8VZp2M0ddoNfhsbjgGdXftPfD9QrLgetxomtacpAN-JJ8Nl9xAsQsJP7O8xkXrwvIvpEaM076aTdHyZr8K21r1-filS4JV6amhxT9Mq6LvY6gNgHiKjurngxE_J0XCFAGkDqXkHJAHw6-3PjY3ik1iBw4-YiSmbeEtJAz80WcYgFao4ETB7hV1jT6MseqmPNFSLSanTo_u8NMnwKWUhN3NWPATJfkt6CnlMEWDlGBYU9hpWHGSjFP-4lVqHdgNOBSExrFAOkKUsaqfvT90RXdQtv5iLqIKvmqog4c1zRnxTfxMFekenEhBrEmUvdmRKYfXWps11JOQOd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTNkm9uxXwlJnqBQ-hUeGti8wXs3Dua-qAb3WhdWU_hJUYFuwmPm3ltvpMXHOHtAMI1SxzKenpyyR-WLiRgFKae3GcNYWJVIW2Gew5ivrUGMe_TH5KqE3TdXGvku-cSdywNjQ91he4x4hoYnUge3VSPhfE7rw5cijlGyi8vWizQMEn6wo0YndEBJaOELQVk1kjxZUK4eOolFg-ymww4naDDorpX3UtlsvRAl5oQzu9dxXJMgqDNCt6w4pt7AsquKiXrw0rKvkkK2sQYPl15MN_cFO7e6QxKVoG3DaFASfJhQPqEquzmA0KNAy-6OE7xU9o2jMMskcjYUixoc71ancw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saClPrqEVBPlL-MY1YXnktVcfMzug1Wnd2oyVvgqyAXfGMVd8bc5hmW0mhjGIM0Au2XvsngQdaGARdrrCzqJMEp3kywrYlRkM6BIcitxzJw-8tJRTO5AOw2X6WlB6lUXWzY-dJYeyL6Gubd-z9ksjPPJhU8cqpsFil28Rz9-QPnNNPCNEGlgcQgVGjaVAEMpLrMb5oLeu9EcmI_P5diMorCJzvpi_2jBDMgPkuefCUPd1eJYXqEiBWeZ47JJc_9C6YBjfGgrw2KiT4mmjsPAMVBNDqN6a-fEi-ozYmzJMNoQyX8L0kUHxz1fGNSerPaxSOEoJI_vtVAAEwC6_1rqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gx75Oym-QFz0U9J51NmLpi2J58sgjcGHuePbPWw3jt8ohDR2BzHEF_qRfN4brTakfIsS8v36PlufX8EcfsCDEkcLUZ1k2Qov3MZ8Q7glBo2RZQCSspX1x6ZGCzMqsOFwCXvSxqwNGNEcqe-3GHTdS0a_7UPVQTlp_jkRlXYIM0CYLn7Fj1s8PwbYEWKitadj_SXQY24GnV0oAcp7wI3OcUuRNmOpF1R4INw6R6MMvev-0r8a3Y3VvA2I5fqD77WAxLp4wIH3oIjSYqI6xpCk9wEwrNp6RbpUreC6hw-rr2XOHZN5FAMUYejCaxrtGGV570JJVCdtcqvekbAG6D9cCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgTw24YvLTkYD_ORvbd972L0vypVrlFIGim_0wERjAXKK0k3A2atnQOef5qtAKbFOvtPUxisDejW1rB9_vrso3ltD4ws2tz7QADDsUGc7eWOraL3nmvR0ZyAyYBG3Imv8CIXA1yaE-YXudUs-c2KwlobfbDen-m72YxoQhf2_18Xf2ZSVcFTMdKTY0LDNn1PFvMoFTJOLdMtEl43ZSI_SZZzy7_MmrJaxFycV2X1Bd6zCXZo8umHNDcwRznbIDxHaEYjxM_HwUgESuFJuOqV179x0ebgnv8Vmgc_-tI9FhT0AQMgHnQZY9E9Rtopvl6spuknYfisn_FqSjPlCB3uRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم رضوی در عزای جوادالائمه(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/436008" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/436007" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع پرجمعیت مردم علی‌آباد گلستان هم‌زمان با شب شهادت جوادالائمه(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/436006" target="_blank">📅 23:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
سقوط درخت در نوشهر پس از تندباد شدید و رعد و برق مهیب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/436004" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436003">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/436003" target="_blank">📅 23:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436002">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt_LFv4j2GisQa-aa0vr5o-Ltirp9pjAgr4CSVS0LOIp7odY40jhmjgtcv4jjh6ydekbKcbEePJpsaHp9L5DSjHj0v1TfMJ8kjpOO5dt1M3DvwCSvr-vC7kGGDiYzSd207WPmxWE-GkVHKGTtRMKC4TdfdvmaS1l27SGalkK5gNwe0XFQwqzGRBLDsWzQVaYwgHpQdjOvXQoYQGUa7QlIjSmKi76lidf38Ttanq5MbgS7KY1u7aqWtFcf5bVY-trCj9ypgRe4QEJUEnaNnErI__nIKX6byC6sWRg-PSuth4-wh4xT3T5vyIp9-CZKBS237j5AEQEvIsvZK1LQon2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: مقاومت ملت ایران، تحول جهان را سرعت بخشید؛ آینده از آن جنوب جهانی است
🔹
جهان در آستانهٔ نظمی نوین قرار دارد. چنان‌که رئیس‌جمهور چین گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/436002" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
بروجردی‌ها امشب برای شهادت امام جواد(ع) سوگواری کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436001" target="_blank">📅 22:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gShIsPjckJ0Syi7hUA-97_I7MiSXZSrSJe8AbNMKvv0nNRPJkKfrKNuO9aPoVE_-iQFbymrTVV_jsYK1ISGpKMQCDL1FXYLPvl2Tq2H2UYvgoCW7uoKInoc2ukREQSaogkwNSfK_qeS9GthA3HoK3ZZTHO283jGnpci7PPmEnYhb4HxbpfFGXwmja2gfdet_NcBtsXMmv2O0WEXSunvENhdxB90EJWQN0LiFSTk9JuPJMynn8udhkVhtY-UpmFB-wbUiu2VyfeaybJ2fPUwEj7qoRhGZgArpyKbIlySxbGSyMEP2P6dXRTa9XvK_IeTGYaPk5s-mVT2f9gwAujSFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوثری: هر تعرضی با پاسخ کوبنده مواجه خواهد شد
🔹
عضو کمیسیون امنیت ملی مجلس: اگر آمریکا یا رژیم صهیونیستی کوچکترین تعرضی انجام دهند، مردم ما، چه زن و چه مرد، در صحنه حاضر هستند.
🔹
دشمن هر توانی داشت در ۴۰ روز گذشته انجام داد، آنها نمی‌توانند به راحتی بمب‌ها و موشک‌های از دست رفته خود را جایگزین کنند، اما ما به راحتی میتوانیم جبران کنیم.
🔹
آنها در هر نقطه‌ای که حضور پیدا کنند، رزمندگان و مردم چنان ضربه‌ای میزنند که جز ذلت و خواری نصیبشان نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/436000" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4yYB-12x11Z6z2e1IY_nGKhM7IQQBWcYxg79kAq7f2EuHauE2g3qgyuxOEelfvlDCey5mjktBDq-TAivlsrC6lFA2PA9BYtkjWRo2rKkvG42lBVLRpu_E3kx9zTRf2cTegG1FZD9T-ew8vIn69aFZR6i_873YjM7rnA7Va8qevVTPvwSJbhdgprIWSA9Ei1EX8qIN5LgpX6z4_cjvN0V9B-3SXcxpDy46b6TNfQPyGJaSusDAmeZryzk9kKjZ3iC7l92pDbCa6VmGRxsyNj5E-Ohf3z7XW2XIIekCGCXAYr9sGkhwW4PGWWgaO5d8YNukmQFrvlOf9xF7RwzKqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست با پهپاد انفجاری حزب‌الله
🔹
ارتش رژیم صهیونیستی از هلاکت «یسرائیل ریکانتی»، از عناصر تیپ گولانی در نتیجه اصابت مستقیم پهپاد انفجاری حزب‌الله در جنوب لبنان خبر داد.
🔹
ارتش اسرائیل با وجود سانسور بسیار شدید تلفات و خسارات این رژیم در جنگ، اذعان کرد که شمار نظامیان کُشته شده در جنوب لبنان از زمان جنگ جاری به ۲۰ نفر افزایش یافته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435999" target="_blank">📅 22:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بورس آمادهٔ بازگشایی شد
🔹
سازمان بورس: آمادگی برای بازگشایی بازار سهام از اواسط هفتهٔ آینده وجود دارد. زمان دقیق بازگشایی بازار به‌زودی اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/435998" target="_blank">📅 22:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد الله اکبر مردم بندرعباس در شب ۷۷ بعثت ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435997" target="_blank">📅 22:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzXVK9hGE3Z52Yjib6fqyNtCH9uwL97-TLXGd0DG238nM8XGOu0AtBg5atFm4VaPFqTED5APakrXV6V4XVsvXEempGl3mAW_23Cmxz2kzy9ifRsAwUtFzgV7cyZn4dOTjH7LCqMnM6YmdXesagoAmvkkCwBFwYljkviSArjo5t85Q3IHav7fuJhwVk7Vsd-F3qeV_l_HmSpbaWzC4r58CxjCidf1if7JgAbJ4BpnnyAQHl6nukQlpU_4_AJ2SjG1c7fxj0yBfXQTvPJYabzonsmhNOljmLPXNDlwinDiIAdxG1d-riGyU8Ik1VZmQ4WNi9WDrjwIv98uhVtKFVhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارنمای بیمهٔ ایرانی تنگهٔ هرمز راه‌اندازی شد
🔹
تارنمای «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگهٔ هرمز را شروع کرد.
🔹
مقررات این تارنمای بیمه می‌گوید، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/435996" target="_blank">📅 22:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiI3rQRj6C_r406i0dastJRhmSi4wxHuqE4S8aoTHxxmjVJdmvaqf4PIRqmW4qpmp7nmlHmArtU9jBjqyBrf9AMJttHDJki9LoYc3-_0XSHnhwbDVz_JyoSp9SCetSIaEEaRqTYHWjpgbO0L8QGNcBXAeljVoXhPgxQOHhqKRQP92uraoCxlr0B1bJjuZtnsq08GQPvXHX0MSKJK6fa1ACyOnCN5xTnZZJEGDc2zzZ9cqSo48bVBZ1un97lhdEQB7teFtIarlXRGd3cokvCw390tqFJMEK4N4pWJvRCQM6YLjtkEZz_duX6XDKEhj5NpQzisvxh6uyJn23FRgJL9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران از طریق امارات با اختلال مواجه شده است.
🔹
پاکستان علاوه‌بر تخفیف ۳۱ تا ۴۰ درصدی در تعرفه‌های بندری خود، یک ماه انبارداری رایگان هم برای کشتی‌ها درنظر گرفته.
🔹
کارشناسان معتقدند که اگر این روند ادامه یابد، وابستگی تاریخی ایران به بندر جبل‌علی امارات که تاکنون سهم اصلی ترانزیت ایران را در دست داشته، برای همیشه پایان می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/435995" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435994">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دعای چهاردهم صحیفه سجادیه در مقتل رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435994" target="_blank">📅 21:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435993">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323911a5b.mp4?token=YpGhL1p1Veu9Xe_UJ9u4MBx72Rj3WQahVX08C2z36ezcRc4p6D0kf_9JjjVvFAQKo_OXD2vCFjseugrF5sNBZauF-saEG8UP3h-vAxhY4q8CrxMuz9iNmquu49IzsOPCskMTQLvMq8p4TCBbvx3gcEg5F4A1FziTmCFeGWtb1FCrVvIujHgW5NqevI5U9AbNJwAkSvkIk-D195sjeaAFhhCfv3nvc9XH4iQmGBL2g562uIwMuFoYF7B_XaF93KzvtmWaMZx5eTzHF1EbU3eKteNsZlf96mwXC5rf8IINL1dlfhtP6OSkDCWy2R9AF5jOLDz3l9VlAzeeVQpWjA9jhAuKzUE8ImLpKdE98CChNyPYONH_IXxBHIF0sfLGXrkJRK0hpMvFvAJhqHfO9aj0lTubupCS4nn5WKtz2fwy0F0EM4R2xF_goCGzyO4PgxBqI660_1oQFeUWWm9ek0q2mbryRGYDX7JCG8mdDtxO8hMKc9Af0junKUkusGlFXwo676yMzMttVJZS6BgcMlvu6Bys2VcKe_EONMqqxlzrxex051KWAarFQPc_zUJRDwkaNGXSFj4cXRD1667p-dHaxeGEPC3P8ScQWsxKdN9vGlZCtuwAFy8SYcqhSf8qs0J3g9Rs8aeBfSY4poHYAColQTdqTaCGlIgtRdOhN_fZ_I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323911a5b.mp4?token=YpGhL1p1Veu9Xe_UJ9u4MBx72Rj3WQahVX08C2z36ezcRc4p6D0kf_9JjjVvFAQKo_OXD2vCFjseugrF5sNBZauF-saEG8UP3h-vAxhY4q8CrxMuz9iNmquu49IzsOPCskMTQLvMq8p4TCBbvx3gcEg5F4A1FziTmCFeGWtb1FCrVvIujHgW5NqevI5U9AbNJwAkSvkIk-D195sjeaAFhhCfv3nvc9XH4iQmGBL2g562uIwMuFoYF7B_XaF93KzvtmWaMZx5eTzHF1EbU3eKteNsZlf96mwXC5rf8IINL1dlfhtP6OSkDCWy2R9AF5jOLDz3l9VlAzeeVQpWjA9jhAuKzUE8ImLpKdE98CChNyPYONH_IXxBHIF0sfLGXrkJRK0hpMvFvAJhqHfO9aj0lTubupCS4nn5WKtz2fwy0F0EM4R2xF_goCGzyO4PgxBqI660_1oQFeUWWm9ek0q2mbryRGYDX7JCG8mdDtxO8hMKc9Af0junKUkusGlFXwo676yMzMttVJZS6BgcMlvu6Bys2VcKe_EONMqqxlzrxex051KWAarFQPc_zUJRDwkaNGXSFj4cXRD1667p-dHaxeGEPC3P8ScQWsxKdN9vGlZCtuwAFy8SYcqhSf8qs0J3g9Rs8aeBfSY4poHYAColQTdqTaCGlIgtRdOhN_fZ_I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگرِ خیابان همدانی‌ها در مدار ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435993" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435992">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff25f4162.mp4?token=a4suji7b2DbVp_K_im8xMtKpYFH9wBTvbJCpZYa48gzfDuM_Go87ZC8lGc6pDvETfoe-uu9rHZ-sRR15XUno9nruH81yJ_u-YQDnhkA5YyzxgeLovDJBjVO2ev7weSrAhaE05fmiH-eG-3I214oEcllvwcdS-cfwNXbxZ3SjxVcKIRwnD4sSIpX9vzJZ4LmK0LC5YwTkC5IYc7p_qQugMaZGzMyENBCYT7ltyPVA63DCXmIQ37qQi7QTirmj5A5gyMO7TBTyBcqyajxcZ1ZKKi8itm2yUb_wmShnmAOGLgvyz99GjZf_ai4bN0zQ-1MnuJm7-bdXp9zD6MDG_oZocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff25f4162.mp4?token=a4suji7b2DbVp_K_im8xMtKpYFH9wBTvbJCpZYa48gzfDuM_Go87ZC8lGc6pDvETfoe-uu9rHZ-sRR15XUno9nruH81yJ_u-YQDnhkA5YyzxgeLovDJBjVO2ev7weSrAhaE05fmiH-eG-3I214oEcllvwcdS-cfwNXbxZ3SjxVcKIRwnD4sSIpX9vzJZ4LmK0LC5YwTkC5IYc7p_qQugMaZGzMyENBCYT7ltyPVA63DCXmIQ37qQi7QTirmj5A5gyMO7TBTyBcqyajxcZ1ZKKi8itm2yUb_wmShnmAOGLgvyz99GjZf_ai4bN0zQ-1MnuJm7-bdXp9zD6MDG_oZocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خزر به کمک خلیج فارس آمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/435992" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435991">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqeDeKe9axapPNpKn4-pprC3oOLfOX08ieOSuzoFoIg723nBNn-ZFNrYiznjlnV_qqn_hFEvd3qEB0aTiSBBwXvrU-mEyGVh3c0uMDxdQKhgkWGgj8lxTUuHH8izNSwJaVIxznak1Imfa-c4RG30dq99d-GWwOdOHLvHSN9dWNZ1Zry-kJMJwasORuPYEf-J3X9jcIwkZauZ6l5DfdjpnnMwbS3ZS3uw0Z-Z8l3q56lp1EaCGa9T2afPiD5bwJewYkAFmbUKJWrLINM4FSLqrY9sYqxNS5u3BCKDBBb1SMKHLeDeQtkbd1I69jdDkBg9xkTzaPR-7KN8DZuLrc04_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/435991" target="_blank">📅 21:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6e243109.mp4?token=Z0lnbwfqWJfpnem2NTklhgDUx2RCHj7aVPgbHFRLpPi7JqEQ6NzkXOFEzEhAubJNqbyMJtmt1hsiuQpbMGT8chFHCJrHy1daYUdd6ceS7AK9o9SC_u5tnyQpatlNyqO9_-_1CkLiuu4HoJLphJhYPT_chz7tKVTgzU0ZOsVPk0OBvxKx7DTyYFvsI7S80CIMhKDCSuIPy3thUDwIoVEo_6O8uRSWUCyn70wa1kpKcb4CCgXx7LNyiJ-zo-Nx6-WY2mVW2nUFUBucFKkdNYnl065e1Pdi8QPUj1L1t0QpQU-LGvjIYVgc9wPOVl8f1S3ggEGNIVPn9P04Gyvqg10hyoXl-GAsnEstIkrn1jWjYmXMP7yR6xOFnLRkVM-xaDmpjksK7QCdjnabRNHWpfdrhxMv4OvP4cf2sQ5RzrCnJX5a0yzDCHcK-KwVbhG-0PwvnpPqWKu49kcA2kTyg2ZC2Q6aT7q_5ZZ4Sn1MOvrOfCMFWiagsprmtgmDG1tzQ_y7FqRRauR6x7nEZgX7oE9Igq2gyUl71CIVeLQFKrE3V5wk9TglAOxs2lTGvM_N4sh_RoyX-0GMuldl6on4J1vSlIBXIZI1G1z_fGFXCEbk4vF00OZsfPuVCz7sRd7LO208-FKOezeOZIqrFlF4CJccf0vqvdh8TNEAPOqMKaSJliY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6e243109.mp4?token=Z0lnbwfqWJfpnem2NTklhgDUx2RCHj7aVPgbHFRLpPi7JqEQ6NzkXOFEzEhAubJNqbyMJtmt1hsiuQpbMGT8chFHCJrHy1daYUdd6ceS7AK9o9SC_u5tnyQpatlNyqO9_-_1CkLiuu4HoJLphJhYPT_chz7tKVTgzU0ZOsVPk0OBvxKx7DTyYFvsI7S80CIMhKDCSuIPy3thUDwIoVEo_6O8uRSWUCyn70wa1kpKcb4CCgXx7LNyiJ-zo-Nx6-WY2mVW2nUFUBucFKkdNYnl065e1Pdi8QPUj1L1t0QpQU-LGvjIYVgc9wPOVl8f1S3ggEGNIVPn9P04Gyvqg10hyoXl-GAsnEstIkrn1jWjYmXMP7yR6xOFnLRkVM-xaDmpjksK7QCdjnabRNHWpfdrhxMv4OvP4cf2sQ5RzrCnJX5a0yzDCHcK-KwVbhG-0PwvnpPqWKu49kcA2kTyg2ZC2Q6aT7q_5ZZ4Sn1MOvrOfCMFWiagsprmtgmDG1tzQ_y7FqRRauR6x7nEZgX7oE9Igq2gyUl71CIVeLQFKrE3V5wk9TglAOxs2lTGvM_N4sh_RoyX-0GMuldl6on4J1vSlIBXIZI1G1z_fGFXCEbk4vF00OZsfPuVCz7sRd7LO208-FKOezeOZIqrFlF4CJccf0vqvdh8TNEAPOqMKaSJliY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخت عزای حضرت جوادالائمه(ع) بر تن صحن و سرای حرم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435990" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KUGnahVyDpOR5P3V6AqFfNGrG8Di1v11tuSzkaBFwaIexuQ2Rvrj1c_HI4XzNFui675ogL5_BSZEYTs3YNi-rfBHEd-g05ylNMjf125Ee7f-HZQ5RDkv98QepVf_1zjYS4KBpoKebUB-92Z4VPTGPo70uWBxZ7FSOTSFbHaTkXzwYFhRvc5eWL_BF5mI0R67raSAENnJh0yi7OuAxz6dDeC1-cmpSU2plaEKWeHATKto-FZ5dGBFNJMqCmqA1MLN_9qPx5R23nOQKVN1nB7D9r4p_6ChxM4Q7-_dv-OvulzNokoevIjMm9gSIgYztLRnLQ3cy7VrkZbw0bZe1GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارنمای بیمهٔ ایرانی تنگهٔ هرمز راه‌اندازی شد
🔹
تارنمای «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگهٔ هرمز را شروع کرد.
🔹
مقررات این تارنمای بیمه می‌گوید، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج فارس، تنگهٔ هرمز و آبراه‌های اطراف آن عبور می‌کنند، ارائه می‌شود و پرداخت‌ها با ارز دیجیتال تسویه خواهد شد.
🔗
جزئیات و آدرس این تارنما را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/435989" target="_blank">📅 21:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3wwh51ifO-Bqgu2GKzdjmWOgyGpZU9ZnPKlOcnLnnVHe5_bA5NldtxxurUco9Rg6I_ny4G-CXXtRy1Er4yKp3_1RMuf_78BPciOBY6nPdrJn5SM6WIoQEfVJOOZqF6Qg4BFTMtQUd2mXTUJUCH0hfITUltNVc5lsgi5s-OFz54Vd2I6B7A3bgzgEbHwMko5KPnepoVm5ffk7Q8GdreRZ8qIXB44g9wiiEuVhlRpkViuL06NXIdlVgf29s4rZhyO2-skj-WGFashAEUUqvMAzURxTrOa6XdVV79bcHpNzhmMFS_0_oxZ-Hj8Y2IOJjsk4-2iFrZZExme5tX0ucxwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: تحریم گزارشگر حقوق‌بشر سازمان ملل چهرهٔ واقعی حقوق‌بشری آمریکا را آشکار کرد
🔹
معاون حقوقی وزیر خارجه: حقوق بشر در قاموس آمریکا تا زمانی محترم است که به رژیم اسرائیل نرسد. هرجا پای پاسخ‌گویی رژیم و حامیان آن در برابر جنایات غزه به میان می‌آید، واشنگتن به‌جای دفاع از قانون، به ابزار تحریم، تهدید و ارعاب متوسل می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435987" target="_blank">📅 21:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس، روزبه چشمی، امیرمحمد رزاق‌نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قایدی، مهدی ترابی
🔸
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علی‌پور
@Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/435986" target="_blank">📅 20:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5abfed34.mp4?token=qg_DSxUJdwk8ljq4nfdYLg3PnbrPJrEpLOpa8qItAoruuI4nqOq3CbHEe_Ai7Dgfz2_siRwvf5gszSUwNONGon2ifFnozRbfsFDHN3e5x9JgJH8aHtxBJJA0DQJt6bH--b3orSYoVHbfQqdKKXlledUelTlhhOMB5s_qJsDr5No4nUzq827-zUUHoPjCpgjFzmV0gADe5s4USjrAZ9g-tA873bIuEcPnHnBT1oVeP9lGME1ZbMUF-iHDyFDmXKYEYiK4iuu_PmIvlliLybeAWJi0OPXIha3aZGu1wo405dL5HnFOIaMmHZP6ZLglLQZNSww2eMmCZ_nBVnicgvg9DHxZE_-4d7MbfQH1weOIWMI3y18DaqDysJvDBh-ygZ_XM0CVf-0uAofHGktmzpYaroVnbBzZtWSYQV4KgSAIYO2yjYwwQn3o3HtgDcpSEBR5hM98wYZBEpc4eAE7fmL4PeeHbhslKl133yQgnhBpwGZzHC9Z3qUd6PUmY6WKZR0Zb9fZMVsniMs15s6hxoO7lGzPBce5jHkF_keSTOiz4J6cL_JgSsfRsr4wVAvW0zbPsqnQcQa0FgG6MarM_uLKR0EeXjScr8lG63aBrbcdNUYjTycaUseOUks8HLP4ov7O7MBpay7EMVz3plHI8ysDU_wgokDi9zlhwH7KZMD2I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5abfed34.mp4?token=qg_DSxUJdwk8ljq4nfdYLg3PnbrPJrEpLOpa8qItAoruuI4nqOq3CbHEe_Ai7Dgfz2_siRwvf5gszSUwNONGon2ifFnozRbfsFDHN3e5x9JgJH8aHtxBJJA0DQJt6bH--b3orSYoVHbfQqdKKXlledUelTlhhOMB5s_qJsDr5No4nUzq827-zUUHoPjCpgjFzmV0gADe5s4USjrAZ9g-tA873bIuEcPnHnBT1oVeP9lGME1ZbMUF-iHDyFDmXKYEYiK4iuu_PmIvlliLybeAWJi0OPXIha3aZGu1wo405dL5HnFOIaMmHZP6ZLglLQZNSww2eMmCZ_nBVnicgvg9DHxZE_-4d7MbfQH1weOIWMI3y18DaqDysJvDBh-ygZ_XM0CVf-0uAofHGktmzpYaroVnbBzZtWSYQV4KgSAIYO2yjYwwQn3o3HtgDcpSEBR5hM98wYZBEpc4eAE7fmL4PeeHbhslKl133yQgnhBpwGZzHC9Z3qUd6PUmY6WKZR0Zb9fZMVsniMs15s6hxoO7lGzPBce5jHkF_keSTOiz4J6cL_JgSsfRsr4wVAvW0zbPsqnQcQa0FgG6MarM_uLKR0EeXjScr8lG63aBrbcdNUYjTycaUseOUks8HLP4ov7O7MBpay7EMVz3plHI8ysDU_wgokDi9zlhwH7KZMD2I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادر دانش‌آموز مینابی از لحظهٔ شناسایی پیکر دخترش
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/435985" target="_blank">📅 20:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97746987ce.mp4?token=ThJEBb_F8n1iZURdMKgxShrFmIQ-CD8ccoiw0qPsXeYN4TcjrDa0isHdXMNYer1Ozs5sbJdPiP7H_pWHtCEeAupfBA3c23Mz13Fd4qSxcBiTLtXS3H6OVtNHarSTuJMLdzwsqeBY7FIB5UQdXifKNpRo_LoVWbAKHpAvU-ObX36THlkNAWF1qCucpdE909RRxAHeoT8sDkPNWg6SlQc2Eu8gKxIhSKJL0gi9Owil1hi7cbqL8Tm7Sfp5nWk30qx4msFcZ1v8QtZ4M5G1XjGJpTEx4C3ruDWCCgFVczx1dhNiBEkRVi3QKh8M-5516_TQ_U7I4ASNvCzfdT73WjWbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97746987ce.mp4?token=ThJEBb_F8n1iZURdMKgxShrFmIQ-CD8ccoiw0qPsXeYN4TcjrDa0isHdXMNYer1Ozs5sbJdPiP7H_pWHtCEeAupfBA3c23Mz13Fd4qSxcBiTLtXS3H6OVtNHarSTuJMLdzwsqeBY7FIB5UQdXifKNpRo_LoVWbAKHpAvU-ObX36THlkNAWF1qCucpdE909RRxAHeoT8sDkPNWg6SlQc2Eu8gKxIhSKJL0gi9Owil1hi7cbqL8Tm7Sfp5nWk30qx4msFcZ1v8QtZ4M5G1XjGJpTEx4C3ruDWCCgFVczx1dhNiBEkRVi3QKh8M-5516_TQ_U7I4ASNvCzfdT73WjWbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دفتر شهید رئیسی: کوتاه‌‌آمدن از تنگه هرمز ظلم به دولت پزشکیان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/435984" target="_blank">📅 20:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae639e1d5.mp4?token=k7pegYwmNaLgwn1ang9_HGVDR03yOPJBnxx4VPWtyOkuil6Vh1j7pPNyYNPev3nfrtyL-FzT7nm4YkFplHLtM9BwkuAgEDy1b6_sNFtwN1rBl04YBOJZhYnfxqNKbXCZVtKo42kYIyb-53nzl87hwFPasILnJt_faaQW0EcrruUY3QOtLEAVy5Xo4ZANHU5vWV4Yvk84QJFe8zg-SR6hsENhhI1MlvBN5bsIWDi5Fe4k64WXv1VXjnSyl5HBPCu-WWqHsXSma-Exm0horLFnAss3LN9v-bhvPZzG9p_ijtQYgPu50hR2gjDL2OTmAbiKY24u8jqeuqt_4ejfq9FMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae639e1d5.mp4?token=k7pegYwmNaLgwn1ang9_HGVDR03yOPJBnxx4VPWtyOkuil6Vh1j7pPNyYNPev3nfrtyL-FzT7nm4YkFplHLtM9BwkuAgEDy1b6_sNFtwN1rBl04YBOJZhYnfxqNKbXCZVtKo42kYIyb-53nzl87hwFPasILnJt_faaQW0EcrruUY3QOtLEAVy5Xo4ZANHU5vWV4Yvk84QJFe8zg-SR6hsENhhI1MlvBN5bsIWDi5Fe4k64WXv1VXjnSyl5HBPCu-WWqHsXSma-Exm0horLFnAss3LN9v-bhvPZzG9p_ijtQYgPu50hR2gjDL2OTmAbiKY24u8jqeuqt_4ejfq9FMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/435983" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلزله ۴.۵ ریشتری گلوگاه مازندران را لرزاند
🔹
دقایقی قبل زمین لرزه به بزرگی ۴.۵ ریشتر گلوگاه مازندران را لرزاند؛ این زمین لرزه در عمق ۶ کیلومتری رخ داده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/435982" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
اطفای حریق در انبار کارخانهٔ روغن موتور مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/435981" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfc6325c4.mp4?token=n7FHrgpYOk-_ebXRT672gARIDoIGPd1_fVFrUDFb-KQdh-vCcuv5EHtEMl8ONLkoCMIR6kIvK55VwxCpVU2NeZCCcxnSJDnutBQbu5l9CecLfUNrM4m1LANUYU5KgTSxVddWlChi1D-WSVYSRL_RBrAUGcNih4UHkIVGAigFFoj64nq5JBByxsYT690rmR0E6rY1MeDAtGxbPAHyWH7W-MQZyq3GdCjJXFfFC8UKrvkn01DR-5P7ikfu4NpUFiO3RDLpnYIXJH9ynQefwK3h36ZZ9b0LBRl2gARsD5M4hykmeKSC7a_Vyp9brSEgtOWNo-DbBwl8uOjotjujG60PX25NAXdWAsPJn-xSif9riEc70R981oMSI-OONP-PPq1tx7fbU9VGzNebz6-zUfOl9_IOJ82PCUyW81V07sIgE1_Io9aaW1K29iVZ9rh1i6OSYXSzn2sVorw5vba8ZgTLcsfocQjQ6I-3cwCiyYB4gOSgcfJdaCzfOBJVMNy9EA_2uFjk6zcOc9CPJPdEjvQUdQ1jSJfoaeZ71QxoEdg-LWxmuP1J_SceSmCAo-APur4lHER7-PGFiIg64RFU4ZeYA-IuBoBmP8kXZF55WJmXWcmHKKCICLG8DHQAxWqDsBgY3aYeO03zJDD7fiBnq-Guulr55106KH5d-cluwor01Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfc6325c4.mp4?token=n7FHrgpYOk-_ebXRT672gARIDoIGPd1_fVFrUDFb-KQdh-vCcuv5EHtEMl8ONLkoCMIR6kIvK55VwxCpVU2NeZCCcxnSJDnutBQbu5l9CecLfUNrM4m1LANUYU5KgTSxVddWlChi1D-WSVYSRL_RBrAUGcNih4UHkIVGAigFFoj64nq5JBByxsYT690rmR0E6rY1MeDAtGxbPAHyWH7W-MQZyq3GdCjJXFfFC8UKrvkn01DR-5P7ikfu4NpUFiO3RDLpnYIXJH9ynQefwK3h36ZZ9b0LBRl2gARsD5M4hykmeKSC7a_Vyp9brSEgtOWNo-DbBwl8uOjotjujG60PX25NAXdWAsPJn-xSif9riEc70R981oMSI-OONP-PPq1tx7fbU9VGzNebz6-zUfOl9_IOJ82PCUyW81V07sIgE1_Io9aaW1K29iVZ9rh1i6OSYXSzn2sVorw5vba8ZgTLcsfocQjQ6I-3cwCiyYB4gOSgcfJdaCzfOBJVMNy9EA_2uFjk6zcOc9CPJPdEjvQUdQ1jSJfoaeZ71QxoEdg-LWxmuP1J_SceSmCAo-APur4lHER7-PGFiIg64RFU4ZeYA-IuBoBmP8kXZF55WJmXWcmHKKCICLG8DHQAxWqDsBgY3aYeO03zJDD7fiBnq-Guulr55106KH5d-cluwor01Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری کمتردیده‌شده از شهید سپهبد موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435980" target="_blank">📅 20:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهلوانی ستارگان کشتی در میان مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435979" target="_blank">📅 20:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGJyRGFgEkM6BYw3Tt4w_8_TEJvgTqonxU-MnXZRunwH6_cbSXLwaTx_NKXDFn72QUfKnKrJzZ_Nd-OFwrX62SIaB60_2t1wAIWVifsPLjyp4ya-jjbcdrRtOOCWJSBgNhPkC8erKdaDlgLLvU_NHrHg9sCTkQ7TAamoMdFSswpsrK6je5voAkvt6oG39N1hGts-8RwI4EM4UB5e5VG7RG_j-ol90dxydQOeT-dKwNGe6hJIATv-OiRMUQUClH4cfsIXu3PqASpRIVV9EIgzHjsww9U0Tybof5V7W757l8sH9HR0wq4ZqZwyxuKpr2B50w99f4-SqqBFNXDJVZPxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: ساخت‌وساز‌ها در نیروگاه اتمی بوشهر از سر گرفته شده است
🔹
رئیس روس اتم: «عملیات بتن‌ریزی و آرماتوربندی ساختمان‌های واحد دوم نیروگاه اتمی بوشهر از سر گرفته شده است. متخصصان ما که در محل باقی مانده‌اند، همکاری فعالانه با پیمانکاران را در چارچوب تعهدات قراردادی خود آغاز کرده‌اند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435978" target="_blank">📅 20:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_MkoY1Ran_XQOFcT42LlckLd85yYBzLxjCfbJIexakQqScjgflpdia_CUtqjJRCstSSgktpWPgJYzVctL8oWrNek6W09piG6FMOvpWWuV3LBaiodNcQCOkUWA_whuYvXFiDXHPTLa5Hpb5skD_L-5UGqIQEqu_7XUhNEsM-7FnKmAjSb1bd2JuISFVEyRXy-VHml5ZLQi4iyg-2D8AbwqvkOS21zcvAWHEAspOFbujw9JPkGBedql0zyCEXPbu--J-eiBwzFS67SptuJwKbNIih4mnmNq5oUqkk_m9_EzkvP66V3fulz2nfL-un44vKnaf3N2D8V3BcZlNezeDt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHrUJ-q9lnjsXVEoh5lC--hIperwCNk4-gfcqqjFIjKz-psh_oJZbBG-lkbLCw0MDtKY8aKAbmjyskKIEbnTgvz2bjUtypT-aoReJT7ETKv1Ng4IzQmweqI2RhUlnUWkv6C7iwIWtkNFne8CBs4QNwHKV0jdtNSuG9H5KY847jJ4_O1AoJHzArs7cFiEkpysCyCbb3EyoJY31R_HOXGbC3D3VwIADGtkyZokWcX0EpFPZawaQUd3cv2YO-D7dzKzicTAK1MmGd82kAT_NfnCTmcJMCPXq50Z3pgElfMrZRaZH2QWAoWjp3EQEflXphNxarFCIG--dCIu4LE6ughJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sATRFv2-CDdhUamYmjckxkwZz7aQVZhP6Zc5LtTCH9SGfIJ3ZwZFhHlxwGmH-3EoB0HrJvPu67VUg9l2XHUclF4NZKPIcotq-4Q2d7iNohQC6SsnrCFSPHRCHSSLyzeb127C5moyKIvhe2896KqvBxaxOcMI6cpOfd35LNsTGuQpy5GXDwXmn8resJehAxQ1tI43c20NFwOQl1LullRUi0uJXidFmed2BCXCbobiRHl_CWao8Ch81GzBlsLelevw3fwdVYsSQPjxOZb22cg6kTXBj883N-C_tVzOqNEVrwzg-x4vKvs5M1aMnQkfslJgPfMsN2fV3mHUvHvBRP53JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caRDaADv3CqjBl3GEsbfEn1KwkdV75Wz41K7uEjnrHnCCPs5Wn0ZF6VF3d4t7zTH79aQtHMkPS37A5ayGm_XHMDKeC_CBElfJC6aiPoanrrkSw0T5BydDmQAfrt0y0WHY3KxH3PiuF1uVR4d0llHLjcRVmLVHSHFCoaQdqv1-uw2xETzzOkTJJPGbo04KtjqK28Hw6aFDzX0muQ6gidoNQ2q_5qgAqdCCSwO5Ru-a0ItfrA_ViqN4vpJZxER5lNtDwJmuaNDbTGW7aIHXywL2oOJbC6Bd9oXBJwjBp_cq2D10V2taFsi6EYo_Nyr4e8VcufOB8QOZ4FJAS7QKsZcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzGXX0qWnDOXsQ_aur9DC59bvY55pNVUfuT81AbBlAZLSisi5My43l95q_9ODfvI5gyxOa4SuliKLKrjN0zUed50MaugefXi7pToN1cbu8WfcqCeeWAu03haBLbj8TBHspGl64PVkl4vFcoWtggKWPK6QTfcE99JPOaG2g1J98Lj-n5r4oj7bbnVy3nhYRSrf3poWAg_RKPb3f0tWDSws7gYIje9HDGj8hkEcJZ_5-Il6EBOy2DKXM2Pg7p-e84Kea2Ntccjf-FoG72R1s543aO2I6qJEoJrmfRAeutIOe2A18ZpkzWONE7G4FY96q_7sNHfz8mxm32tCxAFiXyIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzDtauggh3zeKR3HC7AtuUieC4cH5ixUWfzm434vN8tmdml8FPnYiH9aiu82vLkh0-JF8SEF5LRYxgx8o69khmoHdZwZ5MTcDDmMe7Q_i0v-HubLkrEtTDvMDkDsy16p1JVNTVekqYpOwyIcOMXf1kyNO8yK17AJHoq4vs-Fb0VT5eg0bYX699SaQbHnMSMIbTInQvIy8ucQMDotlAirobtKimJ2N-wSC4uVVgOAdz2SyXjzOQJ33WSKUgKj8iBiPni0hN42-ytLDU2pQiSJ27wpoVDTdaF-gJiLTO1i09yJYfxtNbskC37p0_sQaU_2dayHzvO1qWhXrAW9krKkIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طعنۀ تصویری هنرمندان جهان به سفر ترامپ به چین
🔹
سفر ترامپ به چین واکنش اهالی هنر را نیز به همراه داشت که البته همراه با طعنه و تحقیر بود؛ برای مثال، کمال شرف، کاریکاتوریست یمنی در سه تصویر ترامپ را تحقیر کرد: اژدهایی که نماد چین است با یک فوت، ترامپ را به باد می‌دهد.
🔹
اکونومیست نیز تصویری منتشر کرد که در آن ترامپ به شکل فردی بدبو (که اطرافش را حشرات موذی گرفته است) در حال گفت‌وگو با رهبر چین است؛ علی نجدی، تصویرگر جوان عرب نیز با تصویری با زمینه پرچم چین، ترامپ را پشت سر رهبر چین نشان داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/435972" target="_blank">📅 19:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این روزها مردم دنیا ۲ صحنه از ایران می‌بینند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435971" target="_blank">📅 19:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk3wpqTw8uZdOtveQxOuo-3mEVp-BJTlPMViIJb9-ijLYGG14vBLeACWcSu2QsiPe1KgnDOlFSB10BBKbDGwW8qaG47bbOWFSdBwOJfnVdxOHBpEg7OejQ9rE8bLdsCIX7pPwQNc-UxM3kBI7Qx6Nz8LxCAIkMkggPu6iCg_4CFsyBj7-_KP5HF0GJ2o3cIVLfE67zaIk28wTmkAog-3yk5DN5btGS8q00bHVCRQeCVGVEYNXIV8R-ItCktlexhlWXNwjbWwwiGOFqyiUz0tA1d_QHVP8WubEom7viqlifKc2lVvaCZVW2UPfcLSoMlMqH9RVSPRe5n3dPIIcPobaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: سرو ۴۵۰۰ سالهٔ ابرکوه ریشه در ایرانِ کهن دارد
🔹
کهن‌ترین موجود زندهٔ آسیا، سرو باستانی ابرکوه، با قدمتی دست‌کم ۴۵۰۰ ساله، در سرزمینی ریشه دارد که در همان زمان نیز با نام ایران شناخته می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/435970" target="_blank">📅 19:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزش باد شدید باعث گردباد در اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435969" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/435967" target="_blank">📅 19:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ ‌حزب‌الله: تجمعی از سربازان ارتش دشمن اسرائیلی در شهر الناقوره با ۲ پهپاد انتحاری هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435966" target="_blank">📅 19:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌هایت را ببند برایت یک داستان تعریف کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435965" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخت عزای حضرت جوادالائمه(ع) بر تن صحن و سرای حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435964" target="_blank">📅 19:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfDzm1HmzvVMoJm2t1aDE58zDIc3g-oVy3iM2ut4QZsZjOzvhafKgzbrMTsaSt_irpabC9u-Vgf2b5XbXff6fbtT0o7PWI6Zs2EjFZiHQoZKSBwDj9rDjjfYli5h-bK1-jCcPyz2hrSvFeH8_HAYSgchbzEiKt9Cklgej8veRFIJ2-RtMTP_mNTY--_1_9hl1iGWkI8oWvH6_BeFfquGRpTwki5311UK0jqOg5fIRdMOYqGB14PcaFZXnq7K-4FF1apDg2LD12Rhk2LafcTqpBvgKHiVIJ03_5RBD8HO2VmnNrocAdSxwxqWfeAnKAnOFVBnseZ0kJQnm2AVzsiiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله راهکار صهیونیست‌ها در برابر «FPV» را به سخره گرفت
🔹
حزب‌الله با انتشار تصاویری، اقدام ارتش اسرائیل در نصب تورهای فلزی برای محافظت از حملات کوادکوپترهای مقاومت را به سخره گرفت.
🔹
حزب‌الله در این ویدیو بخشی از سخنرانی معروف شهید سیدحسن نصرالله را آورده که او با اشاره به آیه قرآن، گفته بود اسرائیل «سست‌تر از خانه عنکبوت است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/435962" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqG68xyDFNSzpXW9v8khJwGKWiotzhHXsZXj1RQHyyvxm9xUH0A8gZiGjcB3K5ELiHZeR2hL_6WQSDORk0tCGGwdw_zKMOIRUppw2SdJeKXpx1gfjD2J3rg8wwu7PNKiFGTV8L6RUMbVgeI2sDh3vdNwit00BgyMyvC5CbRPC9cbjaGuqIS8_kOH0PozCWYOOlkyLKyj5rP2owb_VQKNYW4Xpw6koJmlh5I56mRJEyOSrjC3ILITXOAgFTmMOwO-_TspNsCbB8bIaBTqUWgwkZAToIwdNBT8DRwjhZ4P7eUtPLd04ztYsWsQRoxchF8pLQAjhyCd7fUWXZiXLNFZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8YX96WknMUmpHSMOgOmSj0bGMuuebRrmfYGj1J0MTsmssKLoZ-qWO_F63D9mzSDt6UkUxJKasTcmLVjBtIuJ54dplLL2yTtVbMbITnos0aRWVzVZiCxKZ66wOTUW_Oq_Gx5ap3N4by8c8Sdoz7fhDUhKWM63ZIQuwSpVpywNre-7KSlAA9vl49amMQO6ZVg-K1cErBHCpfMDXYj-W4U83kfoABPr1GzqnsEXAqoEk9xC6_Ce3D4VHlqiYQ7q_8dIczkAr_O9fJPe4MQ1-okjOX0B27lLkbpGD1ttbUOzOXHTqWqsLl9g-G2kz-Qxenl1CaVRC2MqXFiV_pBo1ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz08Am-AJDXsetI6pkH8wNt_XbIfv8IJGoydAjwZ6rSm45P5xOvUKo7VWvgwK1JbCzEWvqXqhGEHPBQjr_zo8IRiif1YKbpwUihJX53hVWyYf6OVLkGA6f7ZIrsSI4ynzHJBcH_fGo6Nd9OW_HZNP00uzYjTj3pk8w1f1ND37icjqSOqWzFGG_tisWkRVhSJnfaQKWuIrMpGCFajxpDVQFQo0Y5phXa3MCgtTyBhS87m_TCA8D8rI7hzymGTyqheStsEXxzLXg1HomR-SMH_khDQsa9goruIvgFit5eC2p8MWfQRG0VNnCOiTECof2ntCcSyXp40eD3-gMO2jvSN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRe1-WFR_Xa86tthnlN2wSBSfug-nllNfT3PYMSt33f25EUYdkQdirhljpmw27MgQOmjDzJim-DyCTj9nMc0HJ-U4XtdkzE4KwkgYG5scNA15EKFaKiOSi059lwvFPB4AGp2q2B2zBx-bSMv-LIEj_D_rqCMrO1vG2RkyG8L7SM_LDmcU_Fi14CtDnhGthFuju7Mcr1IYBMWgoY1tIYDnv7wLV3HXWoNsHxxnu18cv84k71qLcPfmcrS4gyRai9N8mo8MF6jF6yWUHLRkfBjhfkVVhO-9WJz31uuN9ACqi6IqGaETatEEbbT7nTsK97BHI6mPAXWXGUeBYTNcefDyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/to-aldTPZcWbZlkO4NvKh4cexqPsIcrvftrUsIvqtX_KwPF4qFM7QNDm0h9-mq64b5wWzTQC3qU9FO37gIs-zTYspx-ZCjuWnkiI_LdRmrG3pvbyVd7o0Ze3OFqffvGPQF9nirZVtBHm-6KEPVsaYeYabZeYu8c3YlEZkT0NrJbu739T7vmdFEZrMUvSUjSu5vvyYG4uFm451PzxARKSLaQqbnY1KGeZtmhQOjuY04mIfMlJ9U-eODJ5fhlgt05Y90JjySE5Dneje4Wi-Oh5A7fl1kT0g2fRdq9OSjhwhRkTFnIqBM0tHKrwnq21ZidgGpQ3g18BOv59kRj-jhss0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt0zuaPb2TcQnpYbXyAoYv55uu6Z6UJkHJcMKKG5EZiW8IPm4CyAMllQzMn4LniS5LHTKZ5jc-lGCRJ54GypvP48HJTF5fFPujrTYil69SgZGaoIGFmVkulfDWEfigxkHwN-3EDYoEYc2Ayr_uEoZ7I0CkIYtwRXF6Lsu1_8ZuK8MzoPWTAFuwLveJOow_fiwuC2EVBygCZfuosyQF0GN3svbhqYvHtM30vYcQ4VYKtVlKUwqv32j8QX3XisJSvXQjBLQz6vdWYQGY7Kb_iLpJZDxGZFHITJprV2m5UiTo63VoS4rt2tQV2Ymgyu4g7OZH8uSaojczxW3LG4QIJ4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrFYkYTZ5aGh-j4eDTHlup2ExiLm9zhoNwYi5Z3GENhEzm6jxmk7V3GyjtW3u0KTcvRw8lGjgYo1e0SUq9B6WTR7Jm2j6sskHk4f3EmWQymC2VD_CXM0bv1w3ohITRXtNdZDqhMiEIGtXT8ahAf3v8umi6PXomYVY-YDcq6qcA59KyUDcSKOWw78nadL2bN6LtrCdYWRc4Bq0oVXpIfNwJWm0QgANxNXOHiuo_fhfkQeqhBXaKzlY7WB9zcvI7KVr1H_lPGdi-LczTnvXxAKiBTT8oIDGZkMRGSm90GmuDpHSeTHkKsqg1oXSCV7YDlSPtsmjgMlGWUXhD7ZifgH4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جریان زندگی در ساحل خلیج فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/435955" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsW9-4-b6p9dPMZ4yQMdJDIfJ4lEDG-G0xDkyf5Ql2mV_GiJEPRy1T6JC3QIUgcBVhQmAZC_SsZLq0M-Q6kA3xPVL3mX24nCJHK1PXxtsSMJHsHTLQrUpdCbcRempiP0Gc2g90lnw6tO6muKG_0485_S9nu4dtYL1NIJWYWnj971_xfs9fqMGUlUSGJDU6hdMuKHu-1lcZGLBJodCLSsOvD00o-nk2HeHor_RxWgPgUdn-j34fsgDT4vSrNHDJgKGYtCad4VhgYlVpVPYxMfjhf_xJPzsam5AvFHT9Y2X15tvek92M7d8M85vchcvfSA34M27u8JAnAK6-wMZePOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد  سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/435954" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@Farsna.pdf</div>
  <div class="tg-doc-extra">1.7 MB</div>
</div>
<a href="https://t.me/farsna/435953" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موافقان و مخالفان حمل و نقل رایگان در شورای شهر چه کسانی هستند؟
🔹
همزمان با نزدیک شدن به پایان اجرای طرح موقتی رایگان شدن حمل‌ونقل عمومی در تهران، برخی از اعضای شورای شهر از بررسی طرحی خبر داده‌اند که هدف آن رایگان شدن دائمی مترو و اتوبوس در پایتخت است. قرار است فردا این طرح در شورای شهر تهران به رأی گذاشته شود.
🔹
براساس اظهارات مطرح‌شده در شورا، ۱۰ نفر از اعضای شورای شهر تهران از این طرح حمایت کرده‌اند و معتقدند رایگان شدن حمل‌ونقل عمومی می‌تواند به کاهش ترافیک، کاهش آلودگی هوا و افزایش استفاده شهروندان از حمل‌ونقل عمومی کمک کند. به گفته موافقان، این سیاست در برخی شهرهای جهان نیز تجربه شده و نتایج مثبتی داشته است.
🖼
اما چه کسانی در شورای شهر با این طرح موافق هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435953" target="_blank">📅 18:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کپیتال اکونومیست: درگیری طولانی با ایران، قیمت نفت را به ۱۵۰ دلار خواهد رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/435952" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدور دستور توقیف اموال ۱۲۹ عامل دشمن در آذربایجان‌غربی
🔹
رئیس دادگستری آذربایجان‌غربی: دستور توقیف اموال ۱۲۹ نفر از عوامل دشمن به‌دلیل اقدامات ضدامنیتی و همکاری با کشورهای متخاصم صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435951" target="_blank">📅 18:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط یک شهر پاکستانی به دست جدایی‌طلبان
🔹
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435949" target="_blank">📅 18:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای سربه‌زیر شدن ترامپ در چین  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/435948" target="_blank">📅 18:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnJh71IbW4LjEIsrKwOrsDWGqBUAsUs896ASWJjITS-cfNpqM0cgr5d-7X5B4GMS_UZHVJpzORwinWZn-3x9d-hiUP3CTOYS8MBsG7Y-5ZvN7I3cf1pQ4D7yLKA7mBA4GAsnpCkfKja8nGftdKGLHyjakInTQm22U5mkc2nQN-YFB5BVY6-ORwxEtCI7qsJHsvjkPPF5w11mkIg5tqca7T_jJcpFYuaXKq48GxP_sUzL3osnYJjlX3-vaae97U_qddJRfnh06hMWXUkwk0Wb_c7prMO5Dj36JYKFWj__QgIicxed3LlAi0Hl6KKogzpdJJtn39hK0m8N6HRZ-OuG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLlJBpOqHSLMLSmFceiIpzKgk8mpCQzsi3CdEGZuYikpFp5lhEF_ZQ2b1vyY9lcpZzUAzE68Xm1n50mKooK-loTHRm9nMLcHPgTO4SjCvb32IO5JSPTK8JcJWE2u1wAeLomiWwXkR5rr54tdbAuA7oeKfbuoCvjZjQ4rtlCM7883eRqHp8iO1QuNEmhAjmht4SxQwCxqA9vRx-rLYwfWqsiDCL9WAwRpSohTGn0a293PtXwOkfMNZU8NnDJaQAoD8hC1zc0SfLI4s8DrKIYxeS7dD9ZyeXTqOYoAMxxzrva8vy9tsmAhr20VxfNX4O7CmWh0qkjdqDPw8H_NDcNHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJYydWuwxNlv7fsNDs_HUUpow-D1lVcw7cO-Gip9a9JEkhs2pUuQwNLgIHSkE2RYIChGBaJE7hqDW1GuDBESBZdJYPYtiEOu_vnhL8HK87gfbYEeY5soa8mxRJQPNgRECJsnlAfca4_I6xJsMCGCaeUfHwCNQM94h9p4pV4JKWfkBqj5Vw7Ny7KT2ceU2bAtNiRA7wh5xBkFbGThtRMGCu78x3iD7211_RI2wSFZBhYAfVtuMDkLdFE_Mm1giAm57cRXAqTeD7ZPpPInDeLzw3BrVepYQA3uhKCh1FHLbWnEN6-zdipSNjpen49LQ33rEYk35HecvcI19PMg48IEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrd7XNNB9bftbpHJ8ZUYDtuDTMAK3-iLKBk3veFptJfbEbLlQVLUmB7paTUigYzcRy3kwXquAer-lCbQ7c5G3YygeSBUuggzMSPh58BVy-NkQNOlbNy9P7jlcNezkKfg-f4V3wwe3I8zMiLk8P4gPtstBxTGhJx7EHTNVN9ciMginJ0EMmxNssFxYM2kOiipmQUHQAlquMKFVwZ6YoOStVOUvgtCupTTZA99jIciIh4yzPV77czBuf7CLUK7UCcTo6KAZ6SJ-v5qW6CyrT2EVnC8WKq1RC1OD_pnPsTaqnjoQ7c3-kzQTWyGO14rHXCFsFpLRIXvMMrvlfruEcEFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGsoiLw5IlWg25iUZyTMHz8jjpTQBOoe8XqQtHvFyXKnukVULQsNxLXU-ABGSyoeQ2Iw7D17PgXxFYbzTkUJNp5lXiEmyBHdM7GrqIKAGx7SZZU5q0kXsAdKVKZH21zXGlxmapUdBcxQreBkEFi53bF2SOb41FZyV_8mnr6DDgJ1r92PcXlOQXOPNBLcE9lR2Yk42yXg3v-9N6JaDttUwf9pCspK5MuMcQ9O_Owvly2M2RdoiPoVswkVq6_i2xNE1MZjBS4SRy8bSgQScFyWsbOvnolZCuB6Qm7fu39WuhG7_WL3DTY0Xu2yk4LKUA4ux0QC07KSbqnvixz3dCwbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRACJDK27nND3NM_XmofSEhGiTuU7Gt6q15ccwq22482TwcH5J1JaEs1mYU918YMiErb09OnRvWS34mEZ0dH8RV-CUmBLsghWdluQzrFEB2BsuhxdpvYWkO-QNfHXcc3bi447UtvfsTcLsmvKcIbZpZS96nzY2uSYbb9zNsfFqOCQgtSVHbisDr6BjkaBA6a9yRZ3VAe_-e6eunMCZe_YqnIyBUE9GMw_11FQ-yFkqou1-H4cK_D0r4GmKd6DQVERdHqg7apAafLcdNlA0WnC81Lu1e86IW6_TuJJOvhuk99Ixo84_knNJfImBFWwyzUjAQKojIeIlGx-FHELNL8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkdR2WYttbH_dib2MlzG87nsaX4jypLOC6ZD4KMZ2tO2IiK4hTXDHndhcd9DEVRDX-VgaHliL8OLurZrPIKXFvvv3H3PD0I2NLTAQ0Zh_FSIBWix8soW5-LCMzKzEhVa-xFuneVxnjf6bvYW7V-_jxiYde4GDNHOXm6tr8ml0VRLQccaQH1m3AMoRBOTG2X-DPlknUOJhaOnaUoELGM933IKgNz44DoEppVPefIRdwjHMzQ2MW3Cg1qheqyVhWpDHZhD8mi0QNcOG65CZZsPK-hJTDcUKq32rLsOplhO3eGlN8S3hd1DIhIm4o9HHEt6nVfsCRE0FxYdBw626TXKSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فلامینگوهای مهاجر میهمان بهاری بوجاق گیلان
عکس:
یعقوب رخش بهار
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435941" target="_blank">📅 18:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435940">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به یک بولدوزر رژیم صهیونیستی
@Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/435940" target="_blank">📅 18:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435939">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-37.pdf</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/farsna/435939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-36.pdf</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/435939" target="_blank">📅 17:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435938">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va2922388hGoouYqbApRzFEbsy4ZySDk1YQE6pspASHnUboUZqdXf6VdzXYR5Kd0zEmqR5MDXAlBlmj8hONqkCA98RMU7Zts6M4k6ZuCQQ3HkazVYVGXNXHwmB_wdOoWZ7mDwHMjFSd41You7JzrLEPSwuDgl1f41ya5IcgHZQzOqQPpi2Mwx4MtIpAKXNe82kv-alrIYMI_c0cQnFU8QHWDJT8b2u2Juyf50PCrrG6hoeEvp1tczzKxuxMwoqDVCEPP_fpWfHf-WTjL6SAyg9Ggju6_gGkrX2K1Gm-Gbm7MKbTpxktK_RNN2dz6Avyc1S44EU0WoZ29_3wDEQuSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگردانی ۲۰ هزار ملوان در تنگهٔ هرمز
🔹
حدود ۲۰۰۰ کشتی با ۲۰ هزار ملوان همچنان در تنگهٔ هرمز سرگردان هستند. از زمان شروع جنگ رمضان، ایران کنترل کامل این آبراه استراتژیک را در دست گرفته و قوانین جدیدی برای تردد کشتی‌ها وضع کرده است.
🔹
برخی از این ملوانان حتی وضعیت قانونی خود را از دست داده‌اند. شرکت‌های کشتیرانی پوشش بیمهٔ آنها را لغو کرده‌اند و حالا دیگر نمی‌توانند وارد هیچ بندری در جهان شوند.
🔹
جکلین اسمیت، هماهنگ‌کنندهٔ دریایی اتحادیهٔ بین‌المللی حمل‌ونقل، وضعیت ملوانان را با دوران کرونا مقایسه می‌کند. او می‌گوید: «در کرونا ملوانان ماه‌ها در کشتی‌ها گیر کرده بودند چون اجازهٔ پیاده‌شدن نداشتند. حالا دوباره همان وضعیت تکرار شده است.»
🔹
این درحالی‌ست که سازمان بنادر و دریانوردی ایران اخیرا با صدور پیامی علام کرده تمامی کشتی‌های درحال تردد در آب‌های منطقه، به‌ویژه شناورهای مستقر در آب‌های سرزمینی و لنگرگاه‌های ایران، می‌توانند در صورت نیاز از خدماتی نظیر تأمین آذوقه، سوخت، خدمات بهداشتی و پزشکی و همچنین اقلام مجاز مورد نیاز تعمیراتی بهره‌مند شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/435938" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435937">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌ هدف‌قراردادن یک خودروی دیگر اسرائیل توسط حزب‌الله
🔹
حزب‌الله: یک خودروی نمیرای وابسته به ارتش دشمن اسرائیلی را در میدان شهر الطیبه هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435937" target="_blank">📅 17:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435936">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/435936" target="_blank">📅 17:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435929">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahp8cv6NXJo916Ywu7yVobAfzzDQbqa0RUzfECPP4TbfkX8VSz40CldadQdOcv9wOiWA2fZ0wogRoex1iZiPA6Gp5X37zrHrNC_txFjx6FO2IriySsJjFzopxN62SRJWFGkdyBpPfeC2QmjxPvVRyciO3hgAZsHqs3U0By9LOiDtDKoT-X_AO5e2y34c-5Oc1-OBTzWXxhlwABgK2Nwr6topA2PXAkUJyjB6w8sEMslpD3H95hzQcdF_-8OOVIIXm_E9bYclCl9NsEtzqrT05N2foZqSL4-ZAdY4-JmPidwtB9kOy0d8gn4Hpa_8LQ0z073IMb-eJjkmPeJtV5TKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYibfWk_xIdW5uwkcdWRq4NSpvGzQ6nIjOqMbkgm5ohbLE0pfCCtzuF86sabJ6zq20nZdq5BUHjrDME1Hquk6CNBCgghM4NDtYqPxUAvC8-TNjNxwnBchblcahB4kzEiIntSp4MtPH4KaQNTNChiHygl2MLKH9hwpDVrXig_NxOcNs0PUuTVamtbjor_f_r-MRqNKNldUmLxa0iPmZctYlyj-Jjwon8peTZJ01Q5s4-dwcSjt-z0YuViNLdG-fRL6cowB90z2q0mjIiN0w-mCNLETOyAtoDvYP6npuVg3kZyIL2S_knRcXNrF6N7EIcecv7rfY3DtAbnxF7faMRa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh8YNmetgxsH2d5VRy2UTQWhdNnAUivqIiBipNGNl8LPxE-2GjterFxa4cEWseuKgNNzQpE3XEfgpWlWvl0ROy7FPklAcsOShKwQm6ErTIaro5uo-Uld_9CoPWCrDIz_uqti9OLEd9AY58OC4h5eB1r70LhA-euW9nc7sosu5X8a5xEqQhsInLUFEDdjWurCNAb-LzgahJbwu0lfHoeaTxjYO3xVqII-oHPnP8w9iTeyb2CRQSH5df-SpDeinWLzJL5SV6KY4QqDv01xS9q0qnvBmzeKBNx0084vudeFSRXXi7XZZQlcygHoUiduUSAC79D5ffj5oBD1AE1DJN6mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4XexA960kwiNh5QeaeGtiOjoWE_5Q3uXbCP5s1bfs0RJEqgL3Mo8uZG5lLiLvPzVpvQotA6pQabk_sBWC4b4zjX8cp12cJDjR5wzedmP9003K6HPLDXpGW03lsgDG3SihUzdMyWqtw0YW4_zVj9Xw8vH8n2ZfGVNqvUsh7p0T0tFdgHG_CFwJV61-qHt5KT1Gbd2ZLlC3_N-m6STm-xEw52E0f3b8oEwVTcgDbNoPMgyHU2iW-7kNqsGUw1VF7gez9sbXo9z1eVdqtBENAPsZlXRle_xbPjYHcwyiPM6zcJ4u3Dpc3dmCvjw08HYHKEfcCxraO9C_9IKvwiLlQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmC07ykMHqXlEkrQyyGMgL77wdkA1CVbraWfDSz2r5WZlHxVSb2XcGAR_sfb4XLii6ehfCrhOeHm1SDd5LeD8B_bsLaDJ0NNevYGCPMQPoHkj-aKdLoeL_0uxulbTLp1RdavPh0Ko8lbLDt4gIbQHPt21nFnNdEQQK6LBYm3aTNseeKvQ-TrDiu2dDK06Tuv-62mhTt0-ULFyH1nSo5OoufV6E03sgcb7d766P-Qpwa5Kv4CfBnTK1Css8TV4FpJRwZooQUsB1UKvvHL21OcoGznQsCz50o4rltk_7twi4-X9AL5aaqjb_G1NwmqHW2f5ouHH7TycSFkr53d9ai_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxze38A2L8dc7Ojj4EVFolKR9eDa9Mc9YafPEO-OP5BWSaUZa7tQ1oii_BgZWUev0GYnw6e4WXMZ9oiObuQuIeBO-ar6eQTR-Oc4umqhhtbyq02OGSqrBbodj-uyz0shTWNeN-ATt_GK1d1s14b7_oxVb7NIB_qbycIwSO5Ra0Vu8rlEuW-_kBbph95HsgRp9aumyxoHpylHIrjq_nuDJ-qWm5OuoUScaVpnMNleICV8LhTTQBd8tfFehQ9FXaaWek9C_lO9-j75K_kWDvtqflJmWVmQxMIC0XHAIclgXc1VpcXbUbmQ0ENhsDUpel6ew2jWJ5gOBnBI2nVWv8GL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh74LciT7Pxf6nqKlfHau0DrUOzwXEl0lXzuYjifeJZr4HnHodpa8aMNblaNZ0qOPZr6UC5mvZkud293HY8bRYkeYJfcj82l4pokGiCMcDeY1KLBYRM_BkKEF9jzexWt1mF4mtF4af8tIP3U_bFTkLxldHtZ-KMPJDAy_jvs8-tz_BZvoLy3dRCbnQesnrLbxvtYeuDxAUX-cj9SMvO7_LFqsDM__ceCpHniOYG15TSpMiYXNAaInDiKG9Tpt9gN9_XflMj0d-346j8ROkur_wiQMCinaGFtZVFWN48hwQEMA-n7rJYUb0floF2F90wVo9C74nNyH5jq4aAfV1GdZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اکران فیلم «نیم‌شب» روی پل طبیعت
عکس:
محمد وحدتی
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435929" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435928">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/435928" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435927">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه آمریکایی: دولت ترامپ، کوچک‌‎ترین درکی از تحولات جهان ندارد
🔹
کاتسیافیکاس: باز کردن تنگه هرمز برای آمریکا غیرممکن است؛ درخواست آمریکا از چین برای اعمال فشار بر ایران نشانه‌ای از درماندگی و ناآگاهی از تحولات جهان و فقدان هرگونه راهبرد مشخص در دولت ترامپ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/435927" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1MLmsfUJielzYvJ3gRZk4iqBMyW_1BQxf2LUAOXoJfbJbJKO42SwrOtMm2R-4sx59WJh0Bs1I1e96aaDEEd9zK9iqW1Wc7lO8jRfkpgDeh2xCen-t4fJMfy9defHBhhBgPT6jg-P7aRrBNMkKU0bCGCgJwqzXs3pMHUiT_c-h9EbbMy2nZpGcBWEbcVu2fZO31QjF5GOcaIThMMNBmUosPAyWnKLFljy9wX26YCm87t2kI55-5fRWISzMKWsMAgCbIh0qJvZ2077KzDMAKac29UTgO6bM25JP6SfrTegZiTtM3vJGoU_RO5XAslIPT55Kh8Xma-RQrMYNBPP_qjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGeaQFdHBtouF6yElUEhEGxU0FV5p6t57wHhdaFhW_5FJek9uB96xl-SGTct7sV2xqPoaZSt9OiUkqq6pEb6SVtc7w5kr6eV1IzfXJu5sS1DYAktslXlv5LkTIGaKkJS9xOI3kTZcPFWtN_RefTH6YMQdXLcDvE3qoFxquraEQjqheEUvg2lzcw4_zUIzuxQ1_RBLJgb0w76gThmwmPcAOFrtjScxoKgaz7Zq7CwrdS_BxyB_vqRzTqcGS1uQDl9cRtSSUXNHn3Abu1EHpVjxGXPcNx9sAxy2BRWkKoKGZDNZJ9Wh40nXFBboFhtkqvCZl5eBLSfsAA9qW2IZXWYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4PW2ZXlOGmscMbXuKC0TEtdEq-fCM5H378K48AZfSHs-O7YA_vS7vSHOIY28xEo-_-DQOIlUo7E1h1pP4aCYLoIVV3AibnKhxY7zR1CZvuPkc5q1WjKylNzAQ2qo3D_xL0U4F1bRyJxhibA9fXFfhLKAb2WKmG4wpddZI4MZlUjOzZQ-29voO-IJtdTCELtKPSKcAN4j7Lp8OQRFxJFazrs4i7zuFZv4Q4qSiPoyWaOgQPz70OEC1eMjvyC66pfSGWNRsTxspZerYKEZKNF-ymSMbOGeNPr22Anrst2lTTfhQ8abgE3alAE85YuViejx0sVhXIsQxhMx8DhKEEhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSoDtG8MULu-wKCeoTuKnAlPU8sBR3Ria5gAiuwlmJaWGd6O5fMj5o8w_nRYqjQWwvpUZdCNv-m80G257AKIhfvQRlIBS4n2hLZNAAg1gFySIs7gJFJnT-Lf0BxHvRcTwe4aNSNbQ8xCz_6St3_L6htg1xqO0_tGrbU0wLn6P0XMpPj6FIswHeBkDtnrNpOTPkXi1QUiJo2H33b0FnGXaahy7gnvnVm0FZfv8y0tJJ2-fT_6N_HypS6ivONzhKQ1m4W83BmR_mhveUvu_dyayXz9xXIwSH_smDSIW1cEnG8nXCbnO0E1SA56ml1yxvsg17cDbWO9XnUImYkArs8iHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e83XnV0Uwd9kyS7cTyhSdcwqdbJoIRRNWC95wbAqSTfoewpgJsyKmjNNvX-nChZvxXvANcx1OPym23YH20_UO38esaOTI-kqQWIs4SeGRUxuleot1p7HhGBqJgogm4Uf8c5G8-V8cmwyn4PJMN-30dnCVdY0woHj-OICrKQT73dT0iMuUfTPiuwCoGdpS8fHxrSSMpmQwUCbrj-Dap_-KgS8j1PLwfzzwS4x71v2tarYTvyfjB93X_iYlp6ChW0Qc9W67z78kbgC7TejYvw3h4-thebl8D2X1sJorDdsGYs3MPtt2Y54D3rf2GjiZq6E62Uyx1raxKN3Sdx4DVK05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaIY-2m6Q0brlfNRYJx9YUXK396Hawk1IQYnwjX4odv11Oak_AT-hnE4JpPGyMlXxLdevGyBe4iuvrRqcp4TQVOEZXznWNrkkfusoi9VmFeO9HS2qSzp9_v3PK1ItzMp6L25jngKzQ6SH6dyi1I56YFVeLVz64euV-VaaGhtPswCjdY3Nqkdpl6dNshBtIzbBi0ZjRfRN_Qrnf7PkfrVega7WlCXAQB9apy99OEn97lCoohfGzBW0rVk3n5BxJQ3Y7Pj_oKyD1OUCKbyf48j7LrsJJedskFhIy7LPdMRCIrXZpop20I1OC3CqbyPyAc1CF9UMSRYEFBEDwnZsFis_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuLMNE-wTKexAwpQ_dgGPod4WqjrI3xMSB8kLy735skYp0_kA7TPUQlSJVunkssQvF22EfW82uOsUiP7pASxdVfNFrwiLaOUh3TRe9pvcnQ7Ug3mORXyzdJ5b41-99sFXnP-x3RLpXMg3bSgfNyvovrs4oVIwaOaxss3HAZ6j3OfxaCSDKYo9wf6X8_LU0fJarQ_FkB10JZNkoSsJe5dEVztr76-97ghuSkMXi25s4c8CKNZCDnvJdaZxfB6fU3JTBbffSVXDekEKTSPfOabCap3qZUTpDqNtoVcbOXnPS4A73zOt8FMQJd8TeqMFSz79hRm1J301qpEybP2pkTnjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله رئیسی
🔹
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله سید‌ابراهیم رئیسی و همراهانشان با حضور وزرای دولت سیزدهم امروز در خبرگزاری فارس برگزار شد.
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/435920" target="_blank">📅 17:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwNbqLOXOPX16QkO2eRgrA-KBxKyNChCRx1uELhNlH-FhO-lBDNgC3uriK-fqytr21IsF18tz3gKbo-6i9W_nzox7_cYhQWxk_Q2Pi7imsEgVm2qsUP47rryDxcNIunGjfnDbrgo75GxFAYJX8_IF1NOgxIteVoh9DWK1-sKaWuVq_NFvxlqJvL_UOzt74onU0ajA2QutmQOQQ-Cg4KuWVTiqX8sTjk4Z7BQ-U7imRqitUpL8_QfCtTbR5-dDlKDkmm_hd8nF3TKSDUZ6DjIz0Cq5bCzypJMvpqLmu8CyFLhohcQW5E6bZPwemPMVP_PVNuMCqpz4lbNg16LG28xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار لوازم خانگی در شوک گرانی‌های پی‌درپی
🔹
بازار لوازم خانگی در ماه‌های اخیر با موج تازه‌ای از افزایش قیمت‌ها مواجه شده است؛ به‌طوری‌که قیمت برخی کالاها در فاصله چند ماه تا ۲ برابر افزایش یافته و فعالان بازار از بلاتکلیفی قیمت‌ها و سردرگمی خریداران خبر می‌دهند.
🔹
بر اساس مشاهدات میدانی خبرنگار فارس، قیمت جاروبرقی که زمستان سال گذشته بین ۱۲ تا ۲۰ میلیون تومان بود، اکنون به حدود ۳۵ تا ۴۰ میلیون تومان رسیده است.
🔹
قیمت ماشین لباسشویی در بازار حدود ۸۰ تا ۹۰ میلیون تومان اعلام می‌شود؛ در حالی که همین کالا در اسفند ماه سال گذشته بین ۳۰ تا ۴۰ میلیون تومان قیمت داشت.
🔹
فروشندگان بازار لوازم خانگی از شرایط فعلی بازار به شدت گلایه دارند و می‌گویند نه خریداران و نه فروشندگان چشم‌انداز روشنی از قیمت‌ها ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435919" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جادهٔ چالوس مسدود شد
🔹
پلیس‌راه البرز: جادهٔ چالوس حدفاصل کرج - شهرستانک و محدوده خوزنکلا و پلیس‌راه کرج، از کیلومتر ۱۸ تا ۳۰ به‌دلیل اجرای عملیات تور سنگ مسدود خواهد شد.
🔹
این محدودیت ترافیکی در روزهای یکشنبه، دوشنبه، سه‌شنبه و چهارشنبه از ساعت ۰۹:۰۰ تا ۱۴:۰۰ اعمال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/435918" target="_blank">📅 17:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان با استقبال همتای ایرانی وارد تهران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435917" target="_blank">📅 16:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه‌پرداز مطرح آمریکایی: واشنگتن در ایران کیش و مات شده
🔹
«شکستِ» راهبردهای آمریکا در جنگ، حتی تحلیلگر برجسته آمریکایی رابرت کِیگن را هم به اعتراف واداشته است. او که از جمله حامیان سرسخت سلطه آمریکا بر جهان بوده، اکنون معتقد است که ایالات متحده در ایران…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435916" target="_blank">📅 16:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکاری یک اسرائیلی با ایران، بدون دستمزد و به‌دلیل نفرت از اسرائیل
🔹
پروندۀ یک فرد ساکن فلسطین اشغالی که بدون دریافت دستمزد و بر اساس نفرت از اسرائیل با مأموران ایرانی همکاری کرده مورد توجه رسانه‌ها قرار گرفته است.
🔹
«احمد دعاس»، رانندۀ کامیون ۲۷ ساله  متهم…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/435915" target="_blank">📅 16:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انسداد مسیر جنوب به شمال کندوان
🔹
پلیس‌راه مازندران: از ساعت ۱۶ امروز مسیر جنوب به شمال کندوان مسدود شده است؛ حدود ساعت ۱۸ از پل‌زنگوله تردد به سمت شمال نیز ممنوع خواهد شد.
🔹
همچنین از ساعت ۱۹ مسیر شمال به جنوب مرزن‌آباد به سمت البرز و تهران یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/435914" target="_blank">📅 16:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScuAbZ7mAUDRUNtAl-ZdUt7-2_QaccBkYnCNO5vkNehbGyzISaH2uUcyJaQ_VStyWzF4QGj5dfEZrdmMFaoqy5LJVQdjO8563Abf3Yfq_LvVh-Q_eJceWd5UEeH6aK67nAVsla_-j47jGagj7sHifJY8Fhlc7LSt5XHokjl6LQ_bMWd_8UdSNjNCK8RI4GXPEwawB6j69UeHU1qfcq_EGrQGJJ7dB9u8RaM2Df79Is3HUAAkU0dgz2ygBVNUHjVpC4naD3qnmpDmeuTRL5ccGt-o0xXuPHBt8hXVt_JypjyVWK1CeX1lKJ3CKzVxqDzuHJD29rYTFQ2BGFPYyNvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری خبرنگار فارس از چندین بانک نشان می‌دهد که اغلب بانک‌ها با وجود گذشت ۲ ماه از سال یا پرداخت وام ازدواج را شروع نکرده‌اند، یا اگر شروع کرده‌اند بسیار کند این وام را پرداخت می‌کنند.
🔹
یکی از بانک‌ها در پاسخ خبرنگار فارس در مورد تعداد افراد در صف می‌گوید: «سیستم ما آمار در صف را نشان نمی‌دهد فقط بانک مرکزی می‌تواند آمار را ببیند.»
🔹
در صورتی که پرداخت وام ازدواج به همین روال پیش برود نه تنها افراد در صف موفق به دریافت وام نمی‌شوند، بلکه تعداد بیشتری به سال بعد منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/435912" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ book.icfi.ir آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435911" target="_blank">📅 16:19 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
