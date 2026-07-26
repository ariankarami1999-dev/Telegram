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
<img src="https://cdn4.telesco.pe/file/gGqzAfwT_q-OmEUkRMRaUVE7hAV667MKtdi4Z_LS0S4J-0J-gmPaKcgHIVEbI2mmtcJa1KjHQ2W9JH6gwvCuARQt1UN0kBclRMU3u6fRZ-SyT6_XV3N-ojir149mFMr9BWPaQITHvI8b0NZfUT0GJO6Jd3Cd2omQdh9aeq_jTDvQfNySwCy2zaVbWqVe4Pz01Kr_9MxECGJp88YJibIeux4FTF0F3RvNieljWeQorObpFmbTsvzFz6L39rrUWqakfYdSk6l1eFdRbzP9wWmfVlYV55T1dzgA7_5iSJeScCETehwJpRh0NzFpWiiCpiEsX7NiErNIvOTP78kSKctPiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 20:19:44</div>
<hr>

<div class="tg-post" id="msg-675529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ec38fbe4.mp4?token=K0zkZbAz457DdNJ0EVPTj5VzACBEW5_fvEa6AdFwX5ltN-YTKn9VpvORZ1JeBdfUTx5Gv1VT0MH6dPhVO_a5gtySKBH7GGJ8h62C7eNJf9v-IM2ByLa_wJLi_1GtCKF_MiClcRD1xBiyDwBwRuXvhdl_A56q0pp1hNGIyhYalumDqbKp18Kuv9HFM1SAhCT2Uoa4VDy3p40Qp02OBOSZ7BLax5uCmWVhU2v0xYaNLedSFfDu-tQTxjQcdwJu2b6Fzl0JvsJuJUvKHgAKy8W9_PNaww0gcE_QWFyGII1xLGfQWs8zDCSOURv3LOM9m3VKWObyGLZtupC5NTPeQV_RrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ec38fbe4.mp4?token=K0zkZbAz457DdNJ0EVPTj5VzACBEW5_fvEa6AdFwX5ltN-YTKn9VpvORZ1JeBdfUTx5Gv1VT0MH6dPhVO_a5gtySKBH7GGJ8h62C7eNJf9v-IM2ByLa_wJLi_1GtCKF_MiClcRD1xBiyDwBwRuXvhdl_A56q0pp1hNGIyhYalumDqbKp18Kuv9HFM1SAhCT2Uoa4VDy3p40Qp02OBOSZ7BLax5uCmWVhU2v0xYaNLedSFfDu-tQTxjQcdwJu2b6Fzl0JvsJuJUvKHgAKy8W9_PNaww0gcE_QWFyGII1xLGfQWs8zDCSOURv3LOM9m3VKWObyGLZtupC5NTPeQV_RrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت معترضین به جنگ و خشونت در اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/675529" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLkymNliNn1nGh89fG8lT1aneEMJFE2CHemX9ZRuUsGfdT9fJHPMMZbvVQGsvgOZnyW80tmpELMYyCNiol38xJDoQ2tTZbL_CDi1XF-qOyPgNkpNZtJ1bEmftk5CRfXu4Kmf_BOLH2VYAxIY8Ga8Q-zdzVSNmY2zLAY34RakjTghPeyTV_rI7I1I-M0XbOHl457pVpXPA3DVzYRfbA13zZTjb2SR9HR2kRrVLcWrnMGvuuzFvAJ53ibb3bN1d_Ca08C4MKpyL2N5IsAuj8Ng5RpNjcdi7T-6LQHIQa3auPQ1ExafP08yc9ciyJrGnQWMZ9ZlDvXyE6E1iKqSb-JJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان بلاتکلیفی صرافی‌های رمزارزی؛ نسخه جدید برای رگولاتوری رمزارزها در راه است
🔹
عباس آشتیانی، رئیس کمیسیون بلاک‌چین و رمزارز نصر کشور، از تدوین متنی در کارگروه ویژه اقتصاد دیجیتال خبر داده که با هدف تنظیم‌گری میان‌بخشی و تقسیم وظایف میان دستگاه‌ها بر اساس ماهیت انواع دارایی‌های دیجیتال تهیه شده است.
🔹
رضا باقری‌اصل، رئیس کارگروه ویژه اقتصاد دیجیتال نیز می‌گوید: قانون، دارایی‌های دیجیتال را به رسمیت شناخته و کاربردهایی مانند توثیق، ضمانت و پذیره‌نویسی را برای آنها پیش‌بینی کرده است. به گفته او آیین‌نامه در حال تدوین، با استناد به همین حکم قانونی و سایر قوانین موجود، مسئولیت هر دستگاه را در حوزه‌های مختلف مشخص می‌کند.
🔹
با این مصوبه می‌توان انتظار داشت اختلاف‌های میان بانک مرکزی، وزارت اقتصاد و سایر دستگاه‌ها بر سر تنظیم‌گری دارایی‌های دیجیتال برطرف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/675528" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bc582944e.mp4?token=gLFniIGNcO1xSSGpmWcFjxGG-IZ9FO7J32M7nN2xBTQ6MTmTtBBa2kxoYcwlYnBYxYwRzBqDaN3wJDhfRBjS7s9xjV7y_PuHN57smkHwmzVvTjzP-L3_qDEFaKg7AXq20IVxjKcfYtDHA-FS3lh-njWLGoJB20rQ2Kq9xah9E70IdVSYREvYwed9iFEEhbYljBVvkAxiRrFPjM54DxmhjSHIIFBWhYUbK7WsG_B3KJ897OkyLHZAb6eb1jpPtZZWY6TNK57eD2oRJsmgQXYzy6jilUkA5IBvRFO4YemP_qTgcxttc9i-fCT1V59bZJcvYXJ_D3rALckFufIau7458w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bc582944e.mp4?token=gLFniIGNcO1xSSGpmWcFjxGG-IZ9FO7J32M7nN2xBTQ6MTmTtBBa2kxoYcwlYnBYxYwRzBqDaN3wJDhfRBjS7s9xjV7y_PuHN57smkHwmzVvTjzP-L3_qDEFaKg7AXq20IVxjKcfYtDHA-FS3lh-njWLGoJB20rQ2Kq9xah9E70IdVSYREvYwed9iFEEhbYljBVvkAxiRrFPjM54DxmhjSHIIFBWhYUbK7WsG_B3KJ897OkyLHZAb6eb1jpPtZZWY6TNK57eD2oRJsmgQXYzy6jilUkA5IBvRFO4YemP_qTgcxttc9i-fCT1V59bZJcvYXJ_D3rALckFufIau7458w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه: حرف آخر حرف رهبر انقلاب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/675527" target="_blank">📅 20:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef54d93ab4.mp4?token=NkwJGE-CUsgMsib_LInkkvSrKzrUtW9h9u7idSA-XwToQSJX8Db3yRefCwp8eo8DZ9svekYyQBGBl9tCvhfFJAcdXap2kmUIpv8lBTvjrHFOldeLKHRTc3FGcd4mA34q5yNKgE8Gq85W_OMowWfy_U7P0kvJ7VGsHfyOzJtAcuvox82k7ZWz08h8_ms6MuoSlhPTHMPORRDT28f2NruBvi1Q9FEKpfv4SbWcVFgyWOd2Ll1Nr0-4ZuC9DXgLPdPDI8sejyVOQpVhZ20NGIY9lNMg2kgkAL2HpDh-o5ap6hYEtYmC92J37eOLSiAiSKF5Z0mio8HCX2j17am7X2DaxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef54d93ab4.mp4?token=NkwJGE-CUsgMsib_LInkkvSrKzrUtW9h9u7idSA-XwToQSJX8Db3yRefCwp8eo8DZ9svekYyQBGBl9tCvhfFJAcdXap2kmUIpv8lBTvjrHFOldeLKHRTc3FGcd4mA34q5yNKgE8Gq85W_OMowWfy_U7P0kvJ7VGsHfyOzJtAcuvox82k7ZWz08h8_ms6MuoSlhPTHMPORRDT28f2NruBvi1Q9FEKpfv4SbWcVFgyWOd2Ll1Nr0-4ZuC9DXgLPdPDI8sejyVOQpVhZ20NGIY9lNMg2kgkAL2HpDh-o5ap6hYEtYmC92J37eOLSiAiSKF5Z0mio8HCX2j17am7X2DaxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام‌ دسته از اتباع باید از مرز شلمچه عبور کنند و کدام دسته از مرز چذابه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/675526" target="_blank">📅 20:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg1GiILbp8MXoRJPkAi_hKm8j8qCqkhfu5sXhctPiuSGqc2K40kDV-JdPbehWCmOfV0cQO5YkplvNj-4tf8TBtuB68N9_MG5dU-Wm18BJ91U9jEcJ5CgKxlEgLarAxObsKmb-i41iB-_DL8ygqYt2KcboD_TbcDJ1-CrUMpXbCs1_dcdm8IBGzHoUGwuXW7IfcdtLUH2Z1tsnTv-Ea4x8Z-WFFgfbII1hnpeXSs4eaVhf--j8xVlWY7biT2Xv_dzsPUV-fAFm2aYmdKWkjKtOcT8P6kotrF4aNK6KOOdDqEC-pmqDQ037gUVXIrgIiyWs3hVDtE4lWAJCcOV9BGrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/675525" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa317d4f93.mp4?token=XXgR4LdBV_pH_D-WbbfmZqOZe0KyA2Gmp2SgOO2atIyu6CLpAVl95zwWiXHrYiB-GnKLfaO9BopZHXVNY3dt_zRAeWhkXedaxSlShdXiwebadHzaYzsKLMkAgElcyNhW4njWfOHqnF1JH4KvM9Lb4UuMPZTaCB_R-WPgKzYsokdyLZyMR7ajt6xzKbJeZVbCj-ZZSvGdHDYMZR2ZCOqcUvsyJ8edm4Bis0t_o8NQm8r7YqS4beO4uzSz9jAyxWVJLuOxWxFNBWnLLpaB3XWZDQ6NMG-d-JqPQeaqJWoHLsmamzxwXL5Ttaaap37xfZ7o7WupDfe2jFXI_k_sEVZprSX-YReGBJjRwFIli-UCWOtTh2WV8JB7aTMu1l-Rv1hxizyt49vIhawT5x0X44yFWIFn7vebhcro0Mncpd2WeVdNvBSFzUo5PvwUzFlKCvCFLBstPX7UPc-wKngW8b9Kt_-k1csMDHk4vv2DWocRBFwK6Iz51Yg-G6slD-YbIrCMCM6-o1w_lBKHAYAsVgc7lJcjlnYK00VDSXt_mkcP3lewe2vf606gUXEH5UEIO3G6ME0a6Wi2NlxHnKE8GPowQX5zdRQrQ5L8cl1Pt1vnVh-nTobFwKgpjHoeK3dPF_VJtGvGioxlFuh4dOTquLVqxPP_L3142Usay-n-g6KDgE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa317d4f93.mp4?token=XXgR4LdBV_pH_D-WbbfmZqOZe0KyA2Gmp2SgOO2atIyu6CLpAVl95zwWiXHrYiB-GnKLfaO9BopZHXVNY3dt_zRAeWhkXedaxSlShdXiwebadHzaYzsKLMkAgElcyNhW4njWfOHqnF1JH4KvM9Lb4UuMPZTaCB_R-WPgKzYsokdyLZyMR7ajt6xzKbJeZVbCj-ZZSvGdHDYMZR2ZCOqcUvsyJ8edm4Bis0t_o8NQm8r7YqS4beO4uzSz9jAyxWVJLuOxWxFNBWnLLpaB3XWZDQ6NMG-d-JqPQeaqJWoHLsmamzxwXL5Ttaaap37xfZ7o7WupDfe2jFXI_k_sEVZprSX-YReGBJjRwFIli-UCWOtTh2WV8JB7aTMu1l-Rv1hxizyt49vIhawT5x0X44yFWIFn7vebhcro0Mncpd2WeVdNvBSFzUo5PvwUzFlKCvCFLBstPX7UPc-wKngW8b9Kt_-k1csMDHk4vv2DWocRBFwK6Iz51Yg-G6slD-YbIrCMCM6-o1w_lBKHAYAsVgc7lJcjlnYK00VDSXt_mkcP3lewe2vf606gUXEH5UEIO3G6ME0a6Wi2NlxHnKE8GPowQX5zdRQrQ5L8cl1Pt1vnVh-nTobFwKgpjHoeK3dPF_VJtGvGioxlFuh4dOTquLVqxPP_L3142Usay-n-g6KDgE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر سیل شدید در استان گوانگ‌دونگ در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/675524" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7JizUPPZ0o246jhB6kGnagvQjF3XJumQhamm7areZi5toe6cOxB_ZNFQlRQiyu5xkCAImng29rgUrAxvG1VNMuGai6HrYT6ceFIWlgTVG9XRWZ1JijFTSHytTyQSTx0R1j8iOnVEUbqQakJqYFvY1W6aLk-HVXvu_6Tv7Fzj0jJn7qEfzNhVXfrMVb4pjyOvsVjjpQgZchcLvZJgNt-s1oXnIm71vcQVVJbTRaRNcwk8spwmo6k9-r52cr3VLocSARkbmk_yQIsUgEwYRgtK94M-NyTUIG3uMbEHhGeoEHemudKz0994H6pV9xpPf7y5KAWT1oXypx685xR9s4kYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از یک دستخط رهبر شهید در دفاع مقدس
🔹
آیین رونمایی از دستخط تاریخی رهبر شهید حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای برگزار شد.
🔹
این دست خط در جریان بازدید تاریخی رهبر شهید از بیمارستان صحرایی حضرت علی‌بن‌ابیطالب (ع) و عیادت از مجروحان جنگ تحمیلی در تاریخ ۴ مرداد ۱۳۶۷ به یادگار نگاشته شده است و برای اولین بار رونمایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/675523" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/675522" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای سناتور جمهوری‌خواه می‌گوید ممکن است به زودی کنگره برای مجوز جنگ با ایران رأی‌گیری کند
🔹
بیل کسیدی، سناتور جمهوری‌خواه که ماه گذشته رأی خود را برای محدود کردن اختیارات جنگی دونالد ترامپ پس گرفت، می‌گوید ممکن است به زودی زمان آن فرا رسد که کنگره درباره‌ی جنگ فرسایشی اظهارنظر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/675520" target="_blank">📅 20:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3sOEsYWD1Z6qhlbak2L_gIoSxne7R0XVYv14ZfEFNqWJNuYs-H-Nyh7ssXbZVZwvYHEJ4W9Bb8oQG5P5NYJKQ3cWUVnLaPyG2atzLD49EBq1uHmrLqQD4uvmozs-euvHhSmP4FTh2MY_Juc6tKKb9ee5b16o2Di6gON76mwhXtHiOTXZZYA2FeJ8Nbo2Ktfi9sOzArWIZWwkXKnjnBi0QMiVYMviCadzFVljNct0t7FHHFQ-45PnXFBXJ0ZDXW58w54D3MvPkxTvVxWc0joX1URN1oRXv6ta7ZcyxpktkTC17wY8WyUOMPygTKEco5R_jjx_dZCqrsT6OXL8u313Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل تسویه بدهی کالابرگ‌ها حل شد
🔹
محسن فتحی عضو کمیسیون اجتماعی مجلس خبر داد: تا پایان هفته جاری تمامی مطالبات و معوقات فروشگاه‌ها (تا قبل ۲۰ تیرماه) تسویه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/675519" target="_blank">📅 20:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea43d43f7.mp4?token=f48SgpTqAnTTyj-PJJdv9ZTyYQmRNeM3ERtinlGsko7IQf8OUBipjMYW_1s0CpM97D4dgR2yFsj17ihofYpohIhO9MS3Q5P1KfqE9zk356WKI9JQv88ISTEsGw1JfAsx-FS5vA0YVr-tJMXY7OzH3loM_t3YHP-PUHujB92-yxEUm6PwV712XJxdfcOjplVs9vg30yzfutjGajx25TfG6bKjZvXE6yGlorzTqZHJKAw_l8eOKAM9odnA3gOodDDMqxwpq1nfw6lXZ-lAP3lRokObKv0QKvNB1TcAaLdY19syg55cirhMaTDG48MAW1uIzZg4n33r_Org7_pUQWzPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea43d43f7.mp4?token=f48SgpTqAnTTyj-PJJdv9ZTyYQmRNeM3ERtinlGsko7IQf8OUBipjMYW_1s0CpM97D4dgR2yFsj17ihofYpohIhO9MS3Q5P1KfqE9zk356WKI9JQv88ISTEsGw1JfAsx-FS5vA0YVr-tJMXY7OzH3loM_t3YHP-PUHujB92-yxEUm6PwV712XJxdfcOjplVs9vg30yzfutjGajx25TfG6bKjZvXE6yGlorzTqZHJKAw_l8eOKAM9odnA3gOodDDMqxwpq1nfw6lXZ-lAP3lRokObKv0QKvNB1TcAaLdY19syg55cirhMaTDG48MAW1uIzZg4n33r_Org7_pUQWzPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار رادان در مرزبانی مرز خسروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/675518" target="_blank">📅 19:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03d5d15f3.mp4?token=QHgWl_Lmh0M8mAv-nR4ExYZubmXiwrhXjTl08DLPruICzV2Y8A8CNCCKfd3g_kg_VfWlia6voQbeBxZVTDk1pbmL3r4OoH_49j3uRW8m3QsWkk6rxUb5Y8U1QeNhV5GxcVByTR9rV9fqvStj6bzEe3eISV7KnUizvumcr1ssEMc9KYNqMsLCFvjwYkbW-UcUwzL44vOpqoNN56LDAqXuDbfoAQAWpEmCF-DXgYzFOFVIQCG1hg8yPv4yTvILX1tT5ZmcKa8oz6mrSLtaLwra72MJciJrB6PDaWM_yVozXu7qjz68PNKlC5nF1T108AeO1tHHIPt_gN0MN_LSiBcI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03d5d15f3.mp4?token=QHgWl_Lmh0M8mAv-nR4ExYZubmXiwrhXjTl08DLPruICzV2Y8A8CNCCKfd3g_kg_VfWlia6voQbeBxZVTDk1pbmL3r4OoH_49j3uRW8m3QsWkk6rxUb5Y8U1QeNhV5GxcVByTR9rV9fqvStj6bzEe3eISV7KnUizvumcr1ssEMc9KYNqMsLCFvjwYkbW-UcUwzL44vOpqoNN56LDAqXuDbfoAQAWpEmCF-DXgYzFOFVIQCG1hg8yPv4yTvILX1tT5ZmcKa8oz6mrSLtaLwra72MJciJrB6PDaWM_yVozXu7qjz68PNKlC5nF1T108AeO1tHHIPt_gN0MN_LSiBcI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر کس میخواهد از تنگه عبور کند باید منتظر اجازه‌ی نیروی دریایی سپاه باشد، دست کم سه شناور قصد عبور داشتند که مجبور به عقب‌نشینی شدند
/صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675516" target="_blank">📅 19:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQuweF4lOVqmp2RMpQJ3b5gQ7LxjfLumEncREqpIgJyPCzKiG3ethbM2Y3Nq3_WYdNP60wO0O1Ra94ky78Ec15wcKJTVaFUJMvaa4jrYb6TEr78YD-CCmtlyowhnI4x7EXeSj0Fig51rkG24cu-q8QoS1o0C0Y727vSq2PQ9BCdZ5bSftToCeeOIP-UQO9yoLJFYP6MLrUlcCnVXCy5uXLNAlOF18KobZk76b3CmAv37uCX8lgs1aUb6Z3Zku4OMNaRj5d4ybklyGDQJ6S1UeqAhIoED9wn5Ai0oMA90__DgHrnCAf6Dd5FZssRrsIrI0v_k_sLa1I7oHRsQbI99ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات تخریب صهیونیست‌ها در جنوب لبنان
🔹
رسانه‌های لبنانی از عملیات تخریب بزرگ ارتش اشغالگر در شهر بنت‌جبیل خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/675515" target="_blank">📅 19:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شاکی پرونده پژمان جمشیدی فاش کرد  «ادعای اخاذی ما کذب محض است!»
🔹
شاکی پرونده پژمان جمشیدی بعد از پایان جلسه دادگاه در شعبه نهم دادگاه کیفری یک با لحنی قاطع و شفاف توضیح داد: تمام ادعاهایی که درباره قصد اخاذی من و مادرم از پژمان جمشیدی مطرح شده، کذب محض…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/675514" target="_blank">📅 19:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h69nXO4xAJPC7JsXBBZmUDlTIVEeuF0hW_Lm7ZXVCBIFv0oCGlgsbkrxQbAAeysYhEmEpMDK9MMgMzIs_5veuQ2mTybfUxjZXX86xrVoINdHuYmNJw-kHvprpwuUbYSaon5sbWzyzt3bG0Fvl9ZBSpz7iuFwM2D4VAtrpmG-mqAb1rPlKa3062HfoZOpaAR84YeksAx45339r0bPMRqE0JLVJIGUoNqGwF_ueAWyOhXGAKJllDlQlIJIvhXvlPsj_kmdSgpX0ENoA0aLviZzAqQLuHcQQrEvkpVDp6sEB6vV2WopaI-0Xvolqc4ahaIWNDntlsk-v5AijKvLT4bBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اقدام «فرصت‌طلب مستقر در کی‌یف» نمی‌تواند بی‌پاسخ بماند
وزیر امور خارجه:
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را کشته است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به جنگ آن بکشاند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/675513" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa009a05b4.mp4?token=l8thW4GPc1nmrv63hKv4dX-IDAyVko0VfVQ75DzxfWT_l4BqcPGznL0hqdvMq51W8-ySHfbdesbm-NogZstMi5JDTjLToZsZy_Papc2fnVLNe-5ILnAD2tHsdpw6guwdFhlNIT7fvI7VbtYfYS7vm1GbUAGDvXrMQJqNHHuzg3bRX0Kicy1W_8KLYRFbtcYkaCZBCl8eoLVJhKBZI2irHGLq6XVFXul_CRMP5sXwsluikHK0NLFltle4kyps8PPROg5GzQEL9lGSiie-ASiwhd2uJJYKfF0MDVoUqCEh6Kqm1vdFAjz6T9HVBVFmvVvXiFbczUAmJHmHPa5GXzKCirf96RLVbJYsa4---ihZAd_QN2Kf2gqyQ_0GLn6_SUmzMnGkO4i57avhdMYnG9gvskOsy0cifb6Nfjsj_YPdz4z1VIxjMMzsuoifJwr5Jl6-xxkkHUMnEzSkR7yN4R27p492UXDbcGFdEIJP-7CzMFXdXu_rdIwa_5a4LRCvRFo_6EVmUr8x5R1HP3_lJPeZ8Vlm3rjASDOAQ4RmwWnqGxjRwAnSC-bfFMnx0rZgt_YVQ0-YzPzP6xP0YOtW5h19M2xF8Ln7602B9HUJJUcHUmkrP5Ey-WhAqN6RtK7TqaGPHeTXVaWi97K4kQS-JXy3lsohZZrTHx8dVO0W4ajOAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa009a05b4.mp4?token=l8thW4GPc1nmrv63hKv4dX-IDAyVko0VfVQ75DzxfWT_l4BqcPGznL0hqdvMq51W8-ySHfbdesbm-NogZstMi5JDTjLToZsZy_Papc2fnVLNe-5ILnAD2tHsdpw6guwdFhlNIT7fvI7VbtYfYS7vm1GbUAGDvXrMQJqNHHuzg3bRX0Kicy1W_8KLYRFbtcYkaCZBCl8eoLVJhKBZI2irHGLq6XVFXul_CRMP5sXwsluikHK0NLFltle4kyps8PPROg5GzQEL9lGSiie-ASiwhd2uJJYKfF0MDVoUqCEh6Kqm1vdFAjz6T9HVBVFmvVvXiFbczUAmJHmHPa5GXzKCirf96RLVbJYsa4---ihZAd_QN2Kf2gqyQ_0GLn6_SUmzMnGkO4i57avhdMYnG9gvskOsy0cifb6Nfjsj_YPdz4z1VIxjMMzsuoifJwr5Jl6-xxkkHUMnEzSkR7yN4R27p492UXDbcGFdEIJP-7CzMFXdXu_rdIwa_5a4LRCvRFo_6EVmUr8x5R1HP3_lJPeZ8Vlm3rjASDOAQ4RmwWnqGxjRwAnSC-bfFMnx0rZgt_YVQ0-YzPzP6xP0YOtW5h19M2xF8Ln7602B9HUJJUcHUmkrP5Ey-WhAqN6RtK7TqaGPHeTXVaWi97K4kQS-JXy3lsohZZrTHx8dVO0W4ajOAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین جنگ‌های آینده را با پهپادهای بیونیک و هوش مصنوعی تصور می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/675511" target="_blank">📅 19:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDQBQ8HToyUNxk0nTpKWyn80SKcqUys_G9IeYdNMXoqR2s6KEe_kro13OkkTXnqW82wK7MFwtqkuWS1C3y6dwIeAHqNaUkxAFkwKAujEcUGXVcVXy2VwovCTA6DmUfzuFNsJsoVBiEqaXsr8z6Z4rFjoDLU9qjiDyadS0eoOAH5_zJIG2HgGrJKPjbPPU4_sQL-ZZm4-gDGx7QNLgXm2lpfHWltlS5FoAZgVHiR5gafV9_qE6fT6R-gyYRQLaAePwVyJtl5Wte_9J2SnsY7p0NdxNaJHSZf8BYr7pIFThmU8IxJLSRdgN-vLAleUQ3JHxPr9TsY6N_ruNkDCNXg8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فخری؛ زنی که در پشت آینه‌های تاریخ گم شد
🔹
در دل شیراز قاجاری، دختری به نام فخری زندگی می‌کرد؛ دختری شیفته‌ی بازتاب‌ها و نور، فرزندِ استاد بزرگ آینه‌کاری شیراز. او هنر را از پدر آموخته بود، اما دیوارهای ضخیم سنت و روزگار قاجار، هرگز به یک زن اجازه نمی‌داد…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/675510" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزرای امور خارجه ایران و روسیه بصورت تلفنی درباره تحولات منطقه گفتگو کردند.
🔹
حراج جدید شمش طلا سه‌شنبه برگزار می‌شود و هر متقاضی می‌تواند تا سقف ۲۵ شمش خرید کند.
🔹
سپاه امام سجاد(ع) هرمزگان: احتمال شنیده شدن صدای انفجار کنترل‌شده در شرق بندرعباس وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/675509" target="_blank">📅 19:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YChLmJ4OrJkjCFNJ2Uk0QUPsMWmGeckqQisuplmR38Ao9YQyYFFQo907GB94XqsDLyGLp4oExu02cX34rlbFleIF2V6wGPjcfQ7dHrc7mkn1nsARAT7eDaBhtqkYv0bnf7da4FlM-8aU-TfNB_couJZdsCJwZUvgdZmSnXqojWKMMqKcGfd5ovTv4dUZ9VdotqBqVuw66_4Kdr9KWH-ru0IZ24MKeFnWmFPxeFw1bXl7dYtAz3_1c3_jzl3vypi44d1U_BoYBoKJLmmlkyMCL4Y9kgQGroyFDbCudo8TCP0p2GAjaSH9jfjINY_g1xHywjQq6gQSHf7AKtU5X3qWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پنل تخصصی نمای ساختمان
.
✅
اجرای سریع
.
✅
مقاوم در برابر آتش، رطوبت و تغییرات اقلیمی
.
✅
مناسب برای مناطق مرطوب
.
جهت آشنایی بیشتر با مصالح و استعلام قیمت، بر روی لینک زیر کلیک نمایید:
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
https://hbboardiran.com/landing/</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675508" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اینتِرپل علیه سران گروه‌های جدایی‌طلب ایرانی اعلان قرمز صادر کرد
یک وب‌سایت عراقی:
🔹
اینترپل با پذیرش درخواست‌های قضایی ایران، علیه ده‌ها نفر از سران و اعضای گروه‌های جدایی‌طلب مخالف ایران «اعلان قرمز» و حکم استرداد صادر کرده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/675507" target="_blank">📅 18:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزارت نفت: بیش از ۶۰ درصد درآمد نفتی بودجه محقق شد
وزارت نفت ایران:
🔹
در طول جنگ، ۱۱.۵ میلیارد دلار و در دوره آتش‌بس، ۶.۵ میلیارد دلار نفت فروخته شده و با این میزان فروش، بیش از ۶۰ درصد درآمد سالانه پیش‌بینی‌شده نفت در بودجه تحقق یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675506" target="_blank">📅 18:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675505">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106915264d.mp4?token=I9HBE4AbxZtzxgFBUJYesz1V6FZU9gmryGq0VdbHwsz7Hsgu2Pgj8d4xdWa2jNZEHwn1V4xAvglNTK8oQIRGe50oKkX8IEm4h-PZhnGwucWF6My18kY_tVdwEo0OR-9pqtT_iyPogES2lFgoGvZwx7Vf8ocsWXGnx3ql6s28N3hRfHtLckyydjLniRE6-JkKClYSmK0SG53qS6Ul9Xdt0JNIY2Uteqa8Ws2B3nRMwdoSHeJAYQxBYdEIJycm7CODP3p3b7cIvZTXjDvjKL2HEfLs48MxevzvsoOCCtNZWu2jguNs8MQkYV9NyEZBeEXMFfyPbbgdS7p35O4cODB_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106915264d.mp4?token=I9HBE4AbxZtzxgFBUJYesz1V6FZU9gmryGq0VdbHwsz7Hsgu2Pgj8d4xdWa2jNZEHwn1V4xAvglNTK8oQIRGe50oKkX8IEm4h-PZhnGwucWF6My18kY_tVdwEo0OR-9pqtT_iyPogES2lFgoGvZwx7Vf8ocsWXGnx3ql6s28N3hRfHtLckyydjLniRE6-JkKClYSmK0SG53qS6Ul9Xdt0JNIY2Uteqa8Ws2B3nRMwdoSHeJAYQxBYdEIJycm7CODP3p3b7cIvZTXjDvjKL2HEfLs48MxevzvsoOCCtNZWu2jguNs8MQkYV9NyEZBeEXMFfyPbbgdS7p35O4cODB_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راب مالی، نماینده سابق ویژه ایران ایالات متحده: با توجه به حملاتی که علیه ایران انجام شده، توافق‌هایی که نقض شده و وعده‌هایی که هرگز عملی نشده‌اند، اینکه ایرانی‌ها به دنبال ساخت بمب اتم بروند، از نظر آنها رفتاری منطقی و عقلانی به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675505" target="_blank">📅 18:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خوک هار به کانادا: جلوی دود را بگیرید وگرنه تحریمتان می‌کنیم
🔹
رئیس‌جمهور آمریکا با متهم کردن کانادا به «مسموم کردن» هوای آمریکا بر اثر دود ناشی از آتش‌‌سوزی‌‌های جنگلی، بار دیگر اتاوا را به اعمال تعرفه‌‌های سنگین و دریافت خسارت تهدید کرد. #Devil
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/675504" target="_blank">📅 18:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675503">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/675503" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675502">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff49302879.mp4?token=EZ4q4ld4lbMZEK1jljbfF7u8ZJw8JsyFRhft23tRC--Rd8masgiSNy1eDR3RtEUdiJ2yuVwvnpqpFOwRbDe7IXgfLedkTzXyTCPn7mRTiLd041Nj_8xWiGjRjHakxlAGcMdjk2RFsszkDTmruWW3--MpWx-JUFEXRf3AGReq4MQM7OgFxNpJrbDDze_nZWO027lcfDJobRrqKC55N8_mNa2C7vXEYURqKRkJMb_TPXDUUaLr6xyXdLDiTMdfoUr5rsTxCARkbiF4Zn1Hu7nZfXcvu5CmbhyUZu5zH5FyTTNeQDmdoJiKxv5LyTeFHqHEOvfW8Bv_7kZ0EO_vlnsRbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff49302879.mp4?token=EZ4q4ld4lbMZEK1jljbfF7u8ZJw8JsyFRhft23tRC--Rd8masgiSNy1eDR3RtEUdiJ2yuVwvnpqpFOwRbDe7IXgfLedkTzXyTCPn7mRTiLd041Nj_8xWiGjRjHakxlAGcMdjk2RFsszkDTmruWW3--MpWx-JUFEXRf3AGReq4MQM7OgFxNpJrbDDze_nZWO027lcfDJobRrqKC55N8_mNa2C7vXEYURqKRkJMb_TPXDUUaLr6xyXdLDiTMdfoUr5rsTxCARkbiF4Zn1Hu7nZfXcvu5CmbhyUZu5zH5FyTTNeQDmdoJiKxv5LyTeFHqHEOvfW8Bv_7kZ0EO_vlnsRbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو جنایتکار: عربستان در ازای عادی‌سازی روابط با اسرائیل، یک برنامه هسته‌ای غیرنظامی دریافت خواهد کرد #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675502" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675501">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffmrwNs4TRjub6RCmjOfQkCFtRgRhOnqZTFD1LHtUl8-ihkvLolIv9iAq2PX_H-MbHrdU6fy1iz3r5acf51cRDSWO5VxsLgJObvXlJM4Wl2OrCn_E0PPw_ZS44hwEj_1phPkXfboQfKChoI_yfzLsxDoHCWRPdym1vjX2lV1Q2XWDNd44rIolk8HF9oFTU5fE7JbaOm_36_Ye2ZPXeDvAJHiTzSAT800vXWsRRklVGNBmZPiqn3NrpYTG_HmX9NSqDanGLg94d5wgrMrBAwatZyw-b5Wi6jiZYD2ztTMbKcQEVmt689dA2P1ZpnHXbIok3muKqO8b7EdX3W3-_EuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت جنگ آمریکا آمار تلفات را اعلام کرد
وزارت جنگ آمریکا:
🔹
از ۷ ژوئیه ۲۰۲۶ تاکنون ۴ نظامی آمریکایی در عملیات خارجی کشته و ۲۰۷ نفر دیگر زخمی شده‌اند./ خبرفوری
🔹
رقم اعلامی بیش از دو برابر آمار قبلیِ اعلام‌شده از سوی سخنگوی پنتاگون است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/675501" target="_blank">📅 18:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای خوک نحس درباره توافق هسته‌ای با عربستان: عربستان باید عضو پیمان ابراهیم باشد. الان وقتش رسیده است، آنها و دیگران این کار را به خاطر ایران انجام ندادند، اما ایران دیگر یک مشکل نیست #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/675500" target="_blank">📅 18:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhLxMhg975gBWPvPaIUoIJg1691Ti6V6Fy1LWgDjo26FwZkhzfEgGxe4nYNwrWWOHramzWp2F-js_FTiBMU0lP5vDG2dn5QD2oM-8TWSDKS0IRoihz52FA_HhoRM6JHz2We15VzVEqehCb8Yj_RbwGfWNMAvGSBxGCxTKa24LnOlSELfqV7j6l499hFEKSP69xSldIOPvNzgNRQc_4B6sUGBfAHxwXwcNc6B01SQWOiStrqYnTnL7aFVf4jm8v1cw-1B7zSTh5h2Iynv-HpcS_cNnMqmDzkU61GJip6gtYhBgMY6Ni4kUfVqXmZedvKjrBgI-Tdbyccy7c-tBuXJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی که زنگ مدرسه را برای همیشه در ایران به صدا درآورد
🔹
میرزا حسن رشدیه، پدر آموزش نوین ایران، مردی بود که در روزگاری پر از مخالفت و تعصب، نخستین مدرسه به سبک جدید را بنیان گذاشت. او با ابداع شیوه‌ای ساده برای آموزش خواندن و نوشتن، راه سوادآموزی هزاران…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/675499" target="_blank">📅 18:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675498">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7f1fdad6.mp4?token=FVkM584rpuuCeiD9KMgvmUtPMabNUN9rjAyygAc7AbcS2nPG2PyuU1JErw8C1hAYxCWnmmhsKZNCnmP_tAgtg-0U8fJ2aTuxu_VFnqAJYMI5rJ5lcnuMz93mzsXvw1s5aK8712pP8kRFkwLN0RJHx9i0Lpsz2_h_s-FTtIrQ5NCnk-v4Njyqd2GMRWc-bH-44UtsOcUBPHfm1pdaY83CztWFAreB4lrEnUMpIoFxdOovfCeYIO4H5FxXEICGkIGsoCgSbaLNRlvZkVWw4Rl2yasYo5hDYH9mefNP8VI9ptvgU4J_Ve57Coy0OnUqzAJOAu2O_nIxMRNUABDlvgXqmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7f1fdad6.mp4?token=FVkM584rpuuCeiD9KMgvmUtPMabNUN9rjAyygAc7AbcS2nPG2PyuU1JErw8C1hAYxCWnmmhsKZNCnmP_tAgtg-0U8fJ2aTuxu_VFnqAJYMI5rJ5lcnuMz93mzsXvw1s5aK8712pP8kRFkwLN0RJHx9i0Lpsz2_h_s-FTtIrQ5NCnk-v4Njyqd2GMRWc-bH-44UtsOcUBPHfm1pdaY83CztWFAreB4lrEnUMpIoFxdOovfCeYIO4H5FxXEICGkIGsoCgSbaLNRlvZkVWw4Rl2yasYo5hDYH9mefNP8VI9ptvgU4J_Ve57Coy0OnUqzAJOAu2O_nIxMRNUABDlvgXqmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قصد دارین تو خونه کباب کوبیده درست کنید، حتما به این چند نکته کلیدی توجه کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/675498" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675497">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
زیاده گویی نتانیاهو کودک‌کش: برنامه هسته‌ای ایران باید چه از راه توافق و چه بدون توافق متوقف شود؛ این جنگ با سقوط نظام ایران پایان می‌یابد یا با تضعیف آن تا جایی که لزوم توقف برنامه هسته‌ای را بپذیرد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/675497" target="_blank">📅 18:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675496">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک منبع بلندپایه ایرانی: اگر واشنگتن به توقف حملات خود ادامه دهد، ما نیز حملات خود را متوقف خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/675496" target="_blank">📅 17:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سردار رادان: توصیه داریم زائران مرز خسروی را در اولویت قرار دهند
.
🔹
رئیس پلیس راه مازندران: جاده هراز تا ۲۰ مرداد شب‌ها مسدود است.
🔹
سی‌بی‌اس: آمریکایی‌ها جنگ با ایران را سخت و فرسایشی می‌دانند و نسبت به آن ناامید هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/675494" target="_blank">📅 17:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع آگاه: ایران به پاکستان تأکید کرده است که آمادگی دارد مذاکرات را در ژنو، دوحه یا اسلام‌آباد ادامه دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675493" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نون پنیر سبزی با شکلی خاص
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675492" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شب به‌یادماندنی برای بچه‌ها؛ دعوت احسان مهدی به «سر سفره خدا» در محرم شهر
🔹
اگر به دنبال یک برنامه متفاوت برای فرزندانتان هستید، «محرم شهر» هر شب تا اربعین در میدان آزادی با بخش‌های متنوع و ویژه کودکان و خانواده‌ها میزبان شهروندان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675491" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
قتل خانوادگی در قزوین؛ پدر و پسر به اتهام قتل مادر و دختر ۸ ساله بازداشت شدند
پلیس قزوین:
🔹
مردی ۴۵ ساله به همراه پسر ۱۷ ساله‌اش به اتهام قتل همسر و دختر ۸ ساله خانواده بازداشت شده‌اند.
🔹
متهم ابتدا ماجرا را سرقت عنوان کرده بود، اما پس از بررسی تناقض‌ها، به قتل همسرش بر سر اختلافات خانوادگی و قتل دخترش به‌دلیل شاهد بودن در جنایت اعتراف کرد؛ هر دو متهم با دستور قضایی روانه زندان شدند.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/675490" target="_blank">📅 17:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحبا به صاحبان پهپادها
🔹
خوش‌آمدگویی موکب‌دار عراقی به زائران ایرانی؛ عراقی‌ها امسال بیشتر از هر سالی مشتاق استقبال و خدمت‌رسانی به زائران ایرانی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675489" target="_blank">📅 17:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTfN7XEASneaz_NE1yvTqPnFi3LIRfJKUVfLdBR8HG49XghMthzFsCduevtqUMfSpN_DONcBWUYDEaOjMXEdqeyHpjN7IT8z7tOJYCZvcb9_qET7FSz2PPV1WfZApDrWNuyiEHC5OXaK0gEFJNXR_0pJPUHq7idSHk85NxnoqwEE2QGbTI9-J4HIst0K0zw-sOzZiryG-EIywojo5-vXgqZLTeKQVOG5GJu57rrv6EQxJhqtZ5JlagYO07YSkMyf45FkbdLs2-IRg17LyZ_KH88ThKrUq1Yz3zjBR4yWjJhg8uhXKpHUrsow2HV3Hl9Yn23FbB5jqHqpa1onLQTpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای الحدث: ایران مذاکرات را متوقف نکرده، بلکه تعلیق کرده است  الحدث به نقل از یک منبع بلندپایه:
🔹
ایران به مسئولان پاکستانی اعلام کرده که از مذاکرات خارج نشده، بلکه آن را به تعلیق درآورده است؛ بر اساس این ادعا، تهران خواستار ازسرگیری مذاکرات درباره تنگه…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675488" target="_blank">📅 17:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHpQRPqhfzJNeH9rd-uE7tibujOQxFdMZ8ptWmFxyixKJUyraqPFmjr34OUn4a_pnOUjRh0xYW2ksMKa7phbN9z4sLe5LgEYVhr0Yo0HlfQ0_niKHK8NT67ZFl0od2Iz2EeebkMTyvmRkAGHevPCarUD681I4fN-1gUsTj12edd_5dKtfhDHIDlTeO-Mf5bLXbuzia3c0fAJ1ItmLsFeqe5JT5Jrsxe5wMslf-W2B3A74IO8OLCYMRana0-wuRqcylCGPJOxkH6a99vMOjTbYZP0_1FQSgfCx_KyrDj3eCzIjftlhcG4XGrkt_yGJciEPlFWNGHfGl9wDtJozIbyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باج‌خواهی طلایی برای زایمان؛ سکه طلا شرط جدید برخی پزشکان
🔹
یک سلبریتی‌پزشک فعال در فضای مجازی، علاوه بر دریافت هزینه‌های مصوب ۷۰ تا ۱۰۰ میلیون تومانی در بیمارستان‌های خصوصی، شرط انجام زایمان را دریافت یک سکه طلا یک‌گرمی به عنوان زیرمیزی قرار داده است.
🔹
با وجود فراهم بودن بستر شکایت، بیماران به دلیل حساسیت شرایط جراحی کمتر اقدام به ثبت گزارش می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/675487" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اژه‌ای: برخورد با مجرم و مفسد هزینه دارد؛ باید زمینه‌های جرم و فساد را از بین برد.
🔹
ادعای سفیر آمریکا در سازمان ملل: ترامپ به دیپلماسی با ایران فرصت داده است.
🔹
نماینده روسیه در وین: درگیری ایران و آمریکا راه حل نظامی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675486" target="_blank">📅 17:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنتونی جاشوآ بوکسور سرشناس بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه دیشب خود برابر کریستین پرنگا، با آهنگ ایرانی وارد سالن شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675485" target="_blank">📅 17:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد برکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEXBTbLmDGYgLkaGD67M5TJHal7HZNTNC9s63VzhnTNZllBXxhhSaMnvwAE8IZ96EJTv2vYgXeUaPpBjeYrCq2j1pvto_OCdukxrlLr5ajGqj-vZNTxBuULT8uD5HMgRi9hWJTMM17tRf3FrvnDnNxrs_CKGu7iwhjgxmz637zWKODOjmJy9W_i80BDsPQhv_NLEAOcO0vTsvlulOsVGsqsFYQvK7dVCvWNUtyaxCQn63AP-ACPjpf8pPkdJ49KzhCzruXUDEzNUFUplFSSDp-eBtfNy7qPC8zgo5QGIp2cvkTScMmDUz-xkhiFK6wCvjM-MZ_wtANmumwsqTpcKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📞
مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔸
سوالی درباره مسائل پزشکی یا درمانی در مسیر اربعین داری؟
🔹
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده پاسخگویی
🔹
مشاوره رایگان در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی
فقط با شماره گیری 4030 بدون نیاز به پیش شماره از عراق
یا با شماره گیری *4030# (ستاره چهل‌سی مربع)
@bonyad_barkat</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675484" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای الحدث: ایران مذاکرات را متوقف نکرده، بلکه تعلیق کرده است
الحدث به نقل از یک منبع بلندپایه:
🔹
ایران به مسئولان پاکستانی اعلام کرده که از مذاکرات خارج نشده، بلکه آن را به تعلیق درآورده است؛ بر اساس این ادعا، تهران خواستار ازسرگیری مذاکرات درباره تنگه هرمز، سپس آزادسازی دارایی‌های مسدودشده و بعد رسیدگی به پرونده هسته‌ای است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/675482" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
کوچک‌ترین زائر اربعین امسال ۱۳ روزه و مسن‌ترین ۱۱۰ ساله است
رئیس سازمان حج و زیارت کشور:
🔹
تاکنون بیش از دو میلیون نفر در سامانه سماح ثبت‌نام کرده‌اند که حدود ۵۸ درصد آنان را آقایان و ۴۲ درصد را بانوان تشکیل می‌دهند.
🔹
استان‌های تهران، خراسان رضوی و خوزستان بیشترین میزان ثبت‌نام را داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675481" target="_blank">📅 17:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی سید مجید بنی‌فاطمه در منزل زنده یاد اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675480" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqUYM6k-Ts24uKw0Qrc-gKNaMmDAFdGNCe0fOFilr3E8JgB8fRLHsTNdYMgEa4MItdrHyN0nTVaS9vlQyF3sX3_60_CV_WsU06BBjXiS5e3tGoiR-6yD6iR2LpW2nVEBbP7Iua9Xm9ARqbG-5sl8YyK6XexwEGPz1Grx3V9jTkVgb6_enHvNCnBHO6ABtJW4Zl0fggL-DKC_ntdiQQLNpN4--B0EwIkDgZkGeRykPy8N03EpE33YY8agGbiZEoobo3BrQ7O_hhsGegukbgNiVCrvbFw3QqqefoM3Tq_2bDSIkeDItqrDNSwbFFTkZ2pmXQ-cLXG6w0-3hmaaYBqy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inMY0-yucXsK71fK-shBPc1al0OOE5aZkxWh1YlNn7KEO9g-Kbi6WWTpGA05i9NmdOQEo6Ih9PacP3ipwod4qf-uam_VcRqEcW5KovNikcraaloRhiVv95slsnSt8ZaCWuVVlZ2zcqZQbIfqz41f-LNTJlH06_d6Rq1D2URvUL2n4inQKuG2SsVg0WINs96hFU_B0VOhsUpblsEkmpcFp4zZd7VH7YlHpDkTzFpwzimX9VtNoAYKZst32MIIRAH-gcQykJE4xaQ0C1ry39C4WMFVXu0kPK82WMUPepfu5Gx8lBlNLNXvZwUL8aVGE0wPljLImU3GoxTQNjTIsI0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNAfocusmt_Gq_YryRkbmf5kfxECFqKaMlr6ZBME9G-W6_GgIyCYdgSq92GYoHT-dfwR-X-z2E6OJPqUwgMh6whg2mcKaGa-XQbeyh7VWOse0zyE9NwnvylvNg5dc188UD3JH_B6N_60dpDUsdGDeVq6mXHl8RYYT5NmqfPmWgz1nvraIEKrQrKiEPyTEKaHkpubznfOlDoKgXEzFf33mLfj49qwg71FTdgiJdpYuITKGPzpVelx5-yUsiKFzHHGm7HX7UFMGayNta2jGz-fNysDpWSjWfCx7FQUAl1ZD-kxzHmY5vv5fuWQkLRKQy5h1NGxIRJp94PNo2rFDXgFFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازیکنان ایران در جمع بهترین‌های جام جهانی
وبسایت Sofascore به بررسی عملکرد بهترین بازیکنان جام جهانی پرداخته که در بین آنها نام ۳ بازیکن ایرانی هم دیده می‌شود که هرکدام در پست خودشان درخشیدند.
🔹
علیرضا بیرانوند برابر بلژیک: سومین گلر برتر جام
🔹
رامین رضائیان برابر نیوزیلند: بهترین دفاع راست جام
🔹
شجاع خلیل‌زاده برابر بلژیک: چهارمین دفاع وسط برتر جام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/675476" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
از میدان آزادی تا کربلا با پرچم «یالثارات الحسین» به نیابت رهبر شهید ایران
🔹
مصطفی زیبایی‌نژاد مدیر کل فرهنگی شهرداری تهران: امسال با پرچم‌های «یا لثارات الحسین» میادین شهر تهران و به نیابت و خونخواهی رهبر شهید ایران در اربعین و آیین جاماندگان شرکت خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/675475" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQJR69hxBLau3p7Lu6geUUxuy2debICLYuho_u1sJUhPFt3eXxNtOblXpjn3ZnFh3KN10vW9Yq28eUa5kq-ea8gBaRws4tZ9IsNmSYEymr0VVez5N1ofkK21XYRHQ9nnD64CStQh2n5uwCuyh9_5CcO1FJVHQl2yXLGpQK15ZAQoooEJSPlERFYxFAxfGKpMd4mB69hL6j4oaMN90nvu19IQoOCcuX6JMSm0gRkIuaDW95oBmmLtnF9VdJNMA0WYVrSLm6Viy5AQdh573mGfCB_7muNwjuHCjBWLP08dS9bAoZh7Fdcy1fELR-E3mUFr7Rp8LybwNzPqkhZR6YiylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل جدید هوش مصنوعی OpenAI معرفی شد؛ GPT-5.6 با سه مدل Sol، Terra و Luna  سه مدل مختلف معرفی شده:
🔹
Sol → قوی‌ترین و دقیق‌ترین نسخه
🔹
Terra → تعادل بین سرعت و قدرت
🔹
Luna → سریع‌تر و اقتصادی‌تر
🔹
عملکرد بهتر در کارهای تخصصی مثل، برنامه‌نویسی، تحلیل‌های پیچیده،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/675474" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروهک‌های ضدانقلاب را در نطفه خفه می‌کنیم   سردار محبی سخنگوی سپاه:
🔹
ما از نقشه دشمن غافل نیستیم. اینطور نیست که سرگرم تنگه هرمز باشیم و از بقیه توطئه‌ها غفلت کنیم.
🔹
دشمن می خواهد گروهک‌های ضدانقلاب، منافقین و سلطنت‌طلبها را مجدداً سازماندهی کند و کاری شبیه…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/675473" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نکات مهم درباره ساعت و نحوه ی مصرف مکمل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/675472" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWsKcdPu7MeD01p7IF3qc71mP2LdIOvmzLgL-ZLg3AgB8Tkit1fVMe06KcjiWNbc6L5p4Z5wxhwRMh96Zdah7eWIrozqSFYfWRh2MR24ZVO-9IKyPak3fct3E0aFN261wVwuD6IMzd24o3e-ilbrN9vS0sbHsYag1kEsQWfwJWUVuOeXmAzuLyQwb5jT_YypRAjWwu7Y4kcR8O7_clKYsO_vH1E4raRVfmiEC-KApUi0ED85GEH4GhDp3G-EiSeK-1XB68VTzy7y9N4rwkNDdQTTXWWQQavd0hc2qsEjsFMRQno09gkHHyc1W-fdA2Uj-kF3VJiTBM7JVJw_txUBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRHo6DXH9DVVI2vxr6S3wElGkkK-8Xu0Nv_33Bnb7cuJptHxJC4bCFx_anS-GLIr5XIpmhPPQRu6eucA8G1qjHEcYnNIO3885XsOE44jZKdH5zeqjMPV5iNkQQDidA-bIEBwWIPo5FAZjEYa9dmwbO8tqJGcdPOAfPkq_RNkuD8mQGEFjcnSMzSpq_c_kgCiQ-kGUYWLchMgzugi5Cz1qI55ff1uyyum89cugwq27077-zBtR__VSjfByr_iiqfseevVFh7v3rOKVFI_6kLDvaFUlbR2b8x7BgLw0uMuPS5gzsXriFcdhqxgVaM8wCmfQFSmHHxl_sQS1tOCNr-MgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjucbtFrQTnrStnwwFJ-sp3VauzHhEVippv6BGW3JocU8WxcgXyKcSROzIciq6v8mV21PncddDYV1GAFutXNKt9rYCp7M8HqCTEM9jqmJdNlywj6lCOzZxAmgswcSxFms1_7EFcRdndE8_qPyyeZzTd5uS0tXu3M6J2IvNRFvWXApHPK3ltn9eYMU3GhC-n8k3MqUg3EYazYrQ2vEPSbfO9kSbWyape2_hBSW08cR6zMSQGynYC3s4GVGKnm6S2n6IfKOyCYPYarPkaqxnXpv8m-zxUtz45_PeDUIsfQEtsY_iN_0spooBQ-ci4bb7yZgf7eQLOaQ0BdKMJlq3L6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjs1gdYnhGhWl1Glaa5QtpySx__NDvacfE-N3-2Osrqcm2Pryv9rdxJQf87pSMD7K8Ui5juExMr3o-edenQnEq6PDejOG1ie-DzbyL3o6I1KSxbR9pLXpI_NDU1shHUhav-ygKeF-kkLFBA6eQhmNrKkdmPDTA7TGMWIwAAJ-DTreL21DnvXoLTR8uSWshwJmyUULUThw4WiSw2aWa1Gw2FwfyqTbF7r0dhqxAJenwa9wpHQOeuk5hO4uIcCy3X5WfNXZfdI5eMfil8aJf1RhWjjRbY9MCk55XH3ZT4M4l8413MDHFc0n5eE0Mvdd33R22JRK5eDI8gvr3ts-8Ma-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده در مصرف برق، می‌توان به پایداری شبکه و تأمین روشنایی پایدار کشور کمک کرد.
🔸
استفاده از لامپ‌های LED و کم‌مصرف
🔸
خاموش کردن کامل وسایل برقی پس از استفاده
🔸
خاموش کردن چراغ اتاق‌های خالی
🔸
استفاده از نور طبیعی در طول روز
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/675468" target="_blank">📅 16:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd000ed14.mp4?token=dVw7u0fTb9ePnecX1uOHJGRXTVLAqv1yS-Y8D2nmvzTZ1p-rqcgLd95I2wrjtBC-6RnE1G8ukyT9_cnImSaDkbyVQfBgi21bOQYPd_em2gV8U3KVXB96ru10TpuEB4FmESp4jlyq5GxruZqf0uCylcW6pZrxtARQNahWjsHI8z-eRBRLjqkJ_StmxQxKzti_n1fvs_fQYvr2cwc25PSs6daoNn5WgrojCtD-BOv9QjblL_FwWc7QqlLWoW7YxPHGnxadK41ZHkUKT8tmYjHKwZBUE9hDcTKdiKYcZgqDGhJbslOOhfIfp6IY5FehqsXyLedRlXUW_3SJtbJRzF04wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd000ed14.mp4?token=dVw7u0fTb9ePnecX1uOHJGRXTVLAqv1yS-Y8D2nmvzTZ1p-rqcgLd95I2wrjtBC-6RnE1G8ukyT9_cnImSaDkbyVQfBgi21bOQYPd_em2gV8U3KVXB96ru10TpuEB4FmESp4jlyq5GxruZqf0uCylcW6pZrxtARQNahWjsHI8z-eRBRLjqkJ_StmxQxKzti_n1fvs_fQYvr2cwc25PSs6daoNn5WgrojCtD-BOv9QjblL_FwWc7QqlLWoW7YxPHGnxadK41ZHkUKT8tmYjHKwZBUE9hDcTKdiKYcZgqDGhJbslOOhfIfp6IY5FehqsXyLedRlXUW_3SJtbJRzF04wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام شهید صیاد شیرازی به این روزهای ما: بنده امروز با صراحت کلام حجت را با شما تمام می‌کنم، نتیجه تفرقه فقط باعث می‌شود در برابر دشمن شکست بخوریم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/675467" target="_blank">📅 16:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naqME7FeN4hVz0F_2mx60xrhDsRn2-jep3wYyc5hvaj1EZVsceI9GdwcoAtJgnA1rwYYdJA7hYPP3Wx1t3av-t-6-NGNSKcA7h3F89MyRkiQsgrtuWH-l7qKZvzf3-MaYCEb0D2ezPy7hfcwYZZkylJWVgUWrfcU_mNGxl64Lt-KHkQ3FK6f0_lDQ5hDaJF__Cyc-n455L40oTfgkWAx1ZRgApSrHrvTmCJevTFrJkG90B4Qzu6DNQlM2Ss7QZ8leLR_2KwooMxhpyS1BmaClanL0NvjoXxrDpq99FPdLxEe10tqfyC2dY6mbq46SjzA0ZBkhQzSoBBvQifWUNsERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرباز سابق نیروی دریایی ایالات متحده:
۳۰۰ نوزاد در گورهای کم‌عمق در غزه پیدا شدند، در حالی که دست‌هایشان از پشت بسته شده بود و زنده‌به‌گور شده بودند. این خبر در هیچ روزنامه آمریکایی تیتر نشده و حتی در کنگره هم مطرح نشده. همین یک موضوع به‌تنهایی نشان می‌دهد که این کشور تا چه حد سقوط کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675466" target="_blank">📅 16:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1gk1XsUofSIKuXX2EeyUl4q01vXPpTyT1ETsm_Ko4shLgxEGUp5m8NbIu-LUegFHu8Ik7fmMpDk5-PTsCa_bhGVSOUM3Gl9DGWd2lqyTMsWxLWYSpE8FFk-x9LaaXj7xALx9Dqbf0ilIDVyT-yGp5KGTclWoiWARBcPe8WrngdkT8ItDEwRbduOfY8BTzN1dVp6evQMz-ZDGdVy8vydDAE2TCexIGpYbl9GfcTts3YP98PXZCrz_v0j-FS7sZrLPRP8VzXCh_Efwjca3wL8OLvnKFOAbe3vhVRbQYQkRpb36g-JwjmZPC5rMBOitdso1Sr-ViorvKyhO7m8w9XzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای رونالدو حتی ماشین هم بخشی از استایلشه!
🔹
کری رونالدو با بوگاتی ست با ساعت چند میلیون دلاری‌اش!
🔹
وقتی جیکوب آرابو از ساعت خاصش با رنگ کهربایی-نارنجی گفت، رونالدو فقط یک جمله جواب داد:
«بوگاتیم رو آوردم؛ دقیقاً هم‌رنگ همینه.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675465" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گروهک‌های ضدانقلاب را در نطفه خفه می‌کنیم
سردار محبی سخنگوی سپاه:
🔹
ما از نقشه دشمن غافل نیستیم. اینطور نیست که سرگرم تنگه هرمز باشیم و از بقیه توطئه‌ها غفلت کنیم.
🔹
دشمن می خواهد گروهک‌های ضدانقلاب، منافقین و سلطنت‌طلبها را مجدداً سازماندهی کند و کاری شبیه اتفاقات دی ماه را دوباره رقم بزند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675464" target="_blank">📅 16:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUT-CuGTHvXKMukYN1c5PEkpbPIMi7talvMcJWqubqLjZme6nWJMrTam7h7Ss5mylPicS-ROGnFt__gfWRSYHG1Gi0GURaJxwXXuHPT9hfGurhSd3_5enbQAGqY9Fu3QY2T1Tk5K-8wdakTW7XGCWAXnh1_oB08R5nkl1mDUexgmLd5ztMdEK6mQIDbsUf-bEHK-U3JZmxkNnLcb2Ul7YuJ8gERUndVOG2A_Gl6hLUSLqstwE0mAjZH6uzRHNA-mtNG5tVq8ZiX5LqJde6gNla6G0r0L7iTMwCcdqNqqa9rq8vMjcXBZBIvArv4-fXGm8IBP1rPLhULmqfYMi5pLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رایحه‌هایی که سرحالت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/675463" target="_blank">📅 16:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8869df45.mp4?token=Vjj0FQOZg7YSX3D0ScrXXS7jMmEWuAv-CWvaPMFZ1VUOILccPQlq-WkxSGjTNzmMQx-hzhIcqMgVhNQwEl89tEJzabpRYU3xanVcbEDQ4Phx3DqCx-ISQc20KNYrtQsg87qWm-10mDxpPYSSDNiEcCdh4YpYIPwAkKS7Kjf_ZXf34mHhUvE2ohl0_fB6uVDqrUy3Hwv-C-wUIBzRyE0RgjtqvkgKVmF0DIALls6b2yixP-xEDsHnzeErvdFNwDL5f7dhU5gQV8eKZg7pNmrNtc_dPbrx6YdsBTcQXMCEHF3lOG7ENUi7B9e7tNyXVXOmQwkP3LyZ9j0vASPckvXjPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8869df45.mp4?token=Vjj0FQOZg7YSX3D0ScrXXS7jMmEWuAv-CWvaPMFZ1VUOILccPQlq-WkxSGjTNzmMQx-hzhIcqMgVhNQwEl89tEJzabpRYU3xanVcbEDQ4Phx3DqCx-ISQc20KNYrtQsg87qWm-10mDxpPYSSDNiEcCdh4YpYIPwAkKS7Kjf_ZXf34mHhUvE2ohl0_fB6uVDqrUy3Hwv-C-wUIBzRyE0RgjtqvkgKVmF0DIALls6b2yixP-xEDsHnzeErvdFNwDL5f7dhU5gQV8eKZg7pNmrNtc_dPbrx6YdsBTcQXMCEHF3lOG7ENUi7B9e7tNyXVXOmQwkP3LyZ9j0vASPckvXjPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک پست مدعی شد که کی‌یف آماده واگذاری ۲۰ درصد از خاک اوکراین در قالب طرح صلح است
ترامپ در جمع خبرنگاران:
🔹
طی ۳ روز آتی، جزئیات کامل را به شما ارائه می‌کنم. اما ما دیدارهای خوبی درباره اوکراین و روسیه داشته‌ایم که باید دید اوضاع چطور پیش می‌ رود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675462" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82abca7c11.mp4?token=L40rOaR0Dprnm1ULeovUg7jStXJ4kdz7Ofwja0BG_7NWSDPIUaPVL8CBLd6vhYn5AqggT23H3tJ78XXKCbknqGhKf3tk8BMmAHN4TvJlqSRy2isXz82dgPaD216jZZTl9NfKxlaLtvF6M4MEi7NOwCwhQn0Zl_U7x0CbkcR_kAkKI5ksrwFWrgUny1-Sb23bl5EwP8ZSp78olCJpYL91Rce8K0gp92zUw4YpQDY7fS3N29NA4ERHUZcDTJ6C_aNwnuAwaYWOEsucF5iTd1s6OEtWV439gsDrwpuy3ft1bHcMDugAsquYq54uzdV2HhdLnGD7kPXilCJ9mro0w_UUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82abca7c11.mp4?token=L40rOaR0Dprnm1ULeovUg7jStXJ4kdz7Ofwja0BG_7NWSDPIUaPVL8CBLd6vhYn5AqggT23H3tJ78XXKCbknqGhKf3tk8BMmAHN4TvJlqSRy2isXz82dgPaD216jZZTl9NfKxlaLtvF6M4MEi7NOwCwhQn0Zl_U7x0CbkcR_kAkKI5ksrwFWrgUny1-Sb23bl5EwP8ZSp78olCJpYL91Rce8K0gp92zUw4YpQDY7fS3N29NA4ERHUZcDTJ6C_aNwnuAwaYWOEsucF5iTd1s6OEtWV439gsDrwpuy3ft1bHcMDugAsquYq54uzdV2HhdLnGD7kPXilCJ9mro0w_UUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه از تصرف شهر شیفتشینکو خبر داد
🔹
وزارت دفاع روسیه تصاویری از آزادسازی شهر شیفتشینکو در جمهوری خلق دونتسک منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675461" target="_blank">📅 16:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10915659e.mp4?token=Zk-jPepjOYkND13lzkSDS1MqtjRPZ_yK5muEOg1MGgcTyz8P7L69RzQVyEISZimt3HFkuojk10L5W6gABmvv7DmaLsmY9fR4kg2ccbR_uCNz31HSQwemxTYilZbshCqhVR1jZibRz4VII-pp9sbFKxVXhLGd81C3Eg8DE5Ae_gb6hNj8yOyPrKFitQFC1Q15ueKDYdhF3mwVySmPxjdokE-o37bznf3u5AO0CfD12CNkHdu8TALoowijIr8zk3WgRnRJd0JdkP7EF6Hn5Ltn1NaD7fSkVAu_5vQUTzu4l-j8RyR4EgjqBd9a8OBHBaaVq4A3iuZJwyGRobC8l9wE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10915659e.mp4?token=Zk-jPepjOYkND13lzkSDS1MqtjRPZ_yK5muEOg1MGgcTyz8P7L69RzQVyEISZimt3HFkuojk10L5W6gABmvv7DmaLsmY9fR4kg2ccbR_uCNz31HSQwemxTYilZbshCqhVR1jZibRz4VII-pp9sbFKxVXhLGd81C3Eg8DE5Ae_gb6hNj8yOyPrKFitQFC1Q15ueKDYdhF3mwVySmPxjdokE-o37bznf3u5AO0CfD12CNkHdu8TALoowijIr8zk3WgRnRJd0JdkP7EF6Hn5Ltn1NaD7fSkVAu_5vQUTzu4l-j8RyR4EgjqBd9a8OBHBaaVq4A3iuZJwyGRobC8l9wE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت شهر جازان در عربستان سعودی را فراگرفته‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675460" target="_blank">📅 16:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
۳ محصول جدید لبنی یارانه‌دار شد
🔹
کارگروه امنیت غذایی ۳ محصول جدید شامل شیر بطری یک‌لیتری ۲.۵ درصد چربی، شیر نایلونی ۹۰۰ گرمی ۲.۵ درصد چربی و ماست دبه‌ای ۲ کیلوگرمی ۲.۵ درصد چربی را به فهرست کالاهای یارانۀ لبنیات اضافه کرد.
🔹
با این تصمیم، تعداد اقلام لبنی یارانه‌ای از ۴ به ۷ قلم افزایش یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/675459" target="_blank">📅 16:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmiYyaSnZpSJmqv08voGp4_EwQmfX9AuKg_6waraWzUV0zgMVPkv2_5NiQ-bXPp_6wY5-43cMcJuBAM9kVhPcPIQRgtLcsmRt67mJCRvG_8DjnZy20mg_es8PmqdPdsNHpVgir2JkZB5R3_tQnXhPQ0vTqQdDZKfF-1Mr7MYBk_VdIsYD4dY8D8OOWbNubeIo4XNBNeNBAK1a8lFlOWa4Jf-beRpaGuxnWRvMTa7yiWSPZvgjSIVl3e3DyOpDXZKvmDQg2REHgyKDMKSexiE5YdNc2CCBqnSEbnBu187VYtESVZlqPf6py8XIUxvLz-6N1cAijKMlbZ56RRfy5vI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMlF74LnRUNivg6sTuG-sI4IgH0gxTwlX4-2Z3DMah-j5MbmgbqYKF1_KoLi8d61iwtjcjLqX9VqlpvrhFdPOx8mRtXSQEgDEsdb3XTZdV6cubOLwbw_jVc5ZEVrJlCGZ0PaPFD_KAFrGdmRaI4vkWY9I4NVXKHg4iQ3-ixVDfiq0H_fVbW2a3QmO3rQaoDp7Kpelt-xHxyoyn0Cd9ha_Zc-UBjF8uViezo4IYgtBWoHxkExq3MoYq5TLFdptD_F_cgPi2yfeUY0pmEtbBZrvKcWfy28ipGo0dIxwlDSn0YN7MTzlJXHxshOo8zRCu4T_kP3jCxxV4KRb7koeqe47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVn7timNigmdI-jj8DgA1arXTbi5tTNj_YcNANh6XAK1QTQlipjIYsPcX1hp_pZoN4AwDSSOuUmNo94g5YD-1xJ8XsPQO4rXVty8szS44pt4F8uo7T1A4jISxTHZnrk2-J-FNkxoNlLZGpOHrLxd5ZJYVqFQGjC3S-jCh-cHLjP3lBg83U9orUVVNwFzvKtnT8_fBkNSVW0CvAaIxgV3gK-dtgZqMKi6RiynPP82EYowcrMQmoGEendQtUmYpw3QHvW_PA9dfvwtbrPqgWyhYi-zJxVxYMRp3F4VG_l-aCbYPJcbBkeOvB8fTYJHN8NUkhosDH3UN2R7rBn_z_guwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZRmYo9ZULI30ati-bR0JK50t9I-yUS942BfU1tvAKJu9453wBY3Whd98ebbmK56eeJLVUvRYU1SuvRTHbr8npk1lBDQU5zuRtsy1nX55sCFJsj7eGkjuENDMXzjIIhBCDRbyaDbLGjuXF4OmDeLWqiC_f_COrGsxtDqfpx45MybTH-2ll27D9pXiV5N2reGxP0nDwKqXzI4GlHZHb1QWnADqAZeqZMxFHvTRTh1HvwOHhvTOn8_6ElKufNIF-yFhmif-W0odUIuOIvAoEcAYAO1JUl7vsqxTz2Q4QNiVG4wteeU7qIWLLL9SHN0Hj1YzwKXcl_wxAu0PzUtRlQKBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فهرست خسارات اعلام‌شده آمریکا در پاسخ ایران
🔹
به گفته سخنگوی سپاه، در پاسخ به تجاوز آمریکا، طیف گسترده‌ای از مراکز فرماندهی، سامانه‌های پدافندی، زیرساخت‌های نظامی و تجهیزات راهبردی این کشور هدف قرار گرفت.
🔹
این عملیات، فراتر از انهدام تجهیزات، توان فرماندهی، پشتیبانی و آمادگی عملیاتی آمریکا را در منطقه زیر ضربه برد و آسیب‌پذیری زیرساخت‌های نظامی آن را نمایان کرد.
🔹
به نظر می‌رسد خسارات در ۱۵ روز اخیر به پایگاه‌های آمریکا از مجموع خسارات به منافع آمریکا و اسرائیل در جنگ‌های قبلی بیشتر و دقیق‌تر ارزیابی می‌شود. این موضوع، به‌روزرسانی و تقویت قدرت آفندی (موشکی و پهپادی) را در دوره آتش‌بس نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675454" target="_blank">📅 16:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXmMSPcRZHFKl5Jc26gz_5bSj4QxU2DIqqjgU9EPUfadFpV4HyoQXARruuBJVJCTk8Kr6LAXzNWJZb7BvZCYwlc0o8NQgLh-ecE_fEyV-Ejt17GpuA8HBuvN7m6GM60QVqEarvynjJ20FjoCFCljrOzS9eELn-jb6uVNzdetDGSe5JOg5XIqbWwjaGrNLysAtu0sUN36yOgBYatDyn_wdgv8BTuWDEgFhw9vpwlW7921My1W-IfnVAlZ4JDZpFD0km0aL1FbKOUBlzS270xVO27aNJGa7Uf1bVx1uzPDN5s0S9uL730pcWPuE_InvbhBhVwzI-oxSBInaVEi7Nmj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0sGNKGNh4TyZBmwoCMGPb2ZUYMrL3EV1oANLbAkjQldzHUQ1vR7N-VNXezgORWFHXrDwcAHPizGbhhpCJkkNIH9UnrtAL7cyEU6oLL3wRrUXKNVGaDRIDF5GttAJ4KH1iH5ZLnX9ck_Fx5xWoQjF1t2mkmGiG_g_2NqnuUIHsQf39iqJHXMWAhsRV6EDqID7W74FHMe82bK4yBi_V3Ry82W6BYKVRGOa8prFZQVgS5GWqBytGmtsuvb9rIPf-KtZ9pnnDByUK1xTHBDHa84AQuODQbnPjNOvV0A91v5Ompei9PQFB1D9kGxcQ9FyiPBK1uNqS9rmDXarYSko14XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4EQdOSvQ7tab6qmMYx-uzJzapRup129yYmv1oX4bIoSmnJUcO2l1_k_EHyWdVW8TXT4gXupKbmp3j_EvWuki5UvH01-77P7hhU8uJ3MzSFc8WojNOONG-phnByv7wbqAXf2lIJJ8-ACHQIBHjxjorxr7-BzTFGoZkY8cD6q1JfbAg3ZZUsARBA5OLuII8H0AYJLYWadUAwsqLNv24nlCwMGXIRFFhkQ1-TdohHK2EUMrFRuYJrs0xtftZ32nadVCTM54f6M0WrBj00jikaSi1XbpdDOIvyDaUhHOFBT9XgXLzjt2kwiugJWy4Q0uVV7NwI_6FJ7tgN3kU1KYJv8Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر با حقوق ۲۰میلیونی قسط داری، این ویدئو رو ببین تا تو خرج کردن کم نیاری #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/675451" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675450">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کویت توافق همکاری دفاعی با پاکستان را تصویب کرد
🔹
اقدامی که به گزارش رسانه‌های پاکستانی، گامی مهم در تقویت روابط نظامی و امنیتی بین دو کشور به شمار می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/675450" target="_blank">📅 15:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea40c5e8d.mp4?token=tK5q0UDrU9Pf0CRhNrJjRvcKMpjL6vpDcucEttfKGbg8YyzRaJFS29t3KN8ntxBt4OxSKkCO5IkcnBy8DeWW_ZZZsnZplA3pYqqGpYB17v9yqOpByDg8S0-P3MOPqHXq-9XDwemmKxRF3P1F0G1ogKtY2-el4tD6EkDjYH2_RwGoTB3npA2ZqHovV6TTm7JcR5XJEyeSJE5Lop1axCjMRar8USGt0DbeLZVf6IY-olJ2Fzj9XmmyzDJ_n5PiEH6bVgSXdav1iic_xP1XZXxiLNpiBw9Umzj2t3TiAK9NU7kx8Qk6QrHmky_Ut_pyC4gYSTSIPCD5Y1m9mXOIclWARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea40c5e8d.mp4?token=tK5q0UDrU9Pf0CRhNrJjRvcKMpjL6vpDcucEttfKGbg8YyzRaJFS29t3KN8ntxBt4OxSKkCO5IkcnBy8DeWW_ZZZsnZplA3pYqqGpYB17v9yqOpByDg8S0-P3MOPqHXq-9XDwemmKxRF3P1F0G1ogKtY2-el4tD6EkDjYH2_RwGoTB3npA2ZqHovV6TTm7JcR5XJEyeSJE5Lop1axCjMRar8USGt0DbeLZVf6IY-olJ2Fzj9XmmyzDJ_n5PiEH6bVgSXdav1iic_xP1XZXxiLNpiBw9Umzj2t3TiAK9NU7kx8Qk6QrHmky_Ut_pyC4gYSTSIPCD5Y1m9mXOIclWARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری خاص از نقش‌های اکبر عبدی در دست مردم مقابل تالار وحدت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/675449" target="_blank">📅 15:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj2CP1xgz8wnYwqFycaoZz54nYKMG3iYqawQ9IMmq6OUHWwI2vo9WV0q6ap22Z8rj25oR4PFX9UGKvfTeEQsTLUWCE6jFjlTVwEpos090k-sw1Z5v2mNcQPgYP9dfpvNNnClSRnGX0BGHsckCLVSyJdxIDlwX306kEXSISFDerjQFbnJJHCAvFyYhNLBz2bJYnjnoeL6XkHs0QELXufQiWSkZMnKzqoyCQNF0f_wN5q4GC9xKodFks8uKcEsyEqg2t8VP1VulqZA9MnxUNMkRYdCSbiWQyTkhI8j5PLZs-IdAC_Fh76LWvOWRwVt4oFqk1BuK7NUAFoEZUOUArVTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر این روزها فروشنده‌ طلا هستید، حواس‌تون به این نکات باشه که سرتون کلاه نره!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/675448" target="_blank">📅 15:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG5RIyO2PK8LDKQ3njyLjM-FTQ81AJb3FNJUj_gJ8vjedypjL84B189k7h1Abs4Et8x_QNSG7LLy8-1ojxyOObLtEoEOfIrDKf5nmm62gIB3ebGfFCzw43hSLbmmRAEmHW4hxVq2EWH6R1IJysjjN7-QGZW8xlIOqRl-O5CIpLDGIx1Etoh21RxsQffWQivIzyP1VqaeHr92gLD3fzn-rcFpd1g4cALfuFG5Fw4IcJe3-QawMpWbdZVTqOIRrI2faxGIghGpRd282xFxUSDqZmQCMRgP2BG_oYj2SpiPqzmRNXUx4oeg2U_MIFJP28YnWIEpOqZO3ZGR-GqH67TGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل شبکه‌های تجاری ایران با تحریم‌های آمریکا
🔹
به گزارش رویترز، واشنگتن در ادامه جنگ اقتصادی خود، شبکه‌ای از شرکت‌ها و کشتی‌های حمل‌ونقل کالایی را برای اختلال در صادرات نفت ایران هدف قرار داده تا زیرساخت‌های مالی صادرات نفت ایران را مختل کند؛ شبکه‌ای که آن را تهدیدی برای «امنیت ملی» خود می‌داند.
🔹
با این حال، اشاره این نهاد آمریکایی به توانمندی شبکه مذکور در «دور زدن تحریم‌ها و توسعه تجارت جهانی»، نشان می‌دهد کارزار فشار علیه اقتصاد روزمره مردم، به سد ساختارهای انعطاف‌پذیر برخورد کرده است. تقابلی که ثابت می‌کند تهران در برابر محدودیت‌ها منفعل نمانده و مسیرهای جایگزینی برای حفظ شریان‌های تجاری خود ساخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/675447" target="_blank">📅 15:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
انفجار نفتکش متخلف در تنگه هرمز
یک منبع آگاه اظهار داشت:
🔹
ساعتی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی ایران خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/675446" target="_blank">📅 15:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnqSF45xbCGLZNKFbhv7N7w57ZysnrGd1DlJVlh7JYENK4tDTTk89k-fWmAId5dNp-Qx-Wzw-xH7uQa-WqbMnq102bkbZGS5NTgoug7TEfW2SV7TB64yqZuDR9N3Vr5WusoUWNsuX6vRQaw0nPg5CdIhFFVwxqE7IhR07LiftV0VOlIZObtNMiO8zYar7P1YUQOJPY91sHrWGFsaaXPL_9i_sn103vKsHRKN0cQRnhs9mtTfvyOaIU58lU5JH_22IfWvEChApJm-Aj0KI6flcynqg3C5c-x9AVjXFYGPXhJW1asp3kU65Dr2a1f01O9zlywCENASRUzfUv0M6MrJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری خاص از نقش‌های اکبر عبدی در دست مردم مقابل تالار وحدت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/675443" target="_blank">📅 15:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ملی‌گرایان خارج‌نشین به جنوب بیایند، قول می‌دهم کسی با آنها کاری نداشته باشد
مرتضی محمودی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شایعات درباره اعزام جان‌فداها به جنوب، عملیات روانی رسانه‌های ضد انقلاب است و نیازی به حضور آنان نیست اما در صورت لزوم این نیروها با آمادگی کامل وارد میدان خواهند شد.
🔹
از مدعیان ملی‌گرایی خارج از کشور که با رسانه‌های خارجی همکاری دارند می‌خواهیم به جای عملیات روانی برای دفاع از سرزمین ایران به مرزهای جنوبی بیایند و بار دفاع از کشور را به دوش بکشند و من قول می‌دهم کسی از داخل به آن‌ها کاری نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/675441" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675439">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8aWQmCrPqKWLmmtIqodT9F5oGmzdDZClpon1oNgqgDXYNLb_0N5McvuLqRl0I86Xk-jE9E4VRYtaOrh8ZXD7CtkhHGN-Aelmtmq-aANM4bLXPh72hlltE2hCbgjI0V5a0rYHb7g4-P8wngzfBdN-SUOvERdb8FN2QEIUhPKPnyECnEdDWeKVUeL7oHVPiWc9wzjr8hmkFZb0mAMvMifDy85r8EWaIMtl6V-4tePfzzWJ4JIHu5Ph_RNQiBItBCNBfgKYwV9kJZYC5JNX3y9DppNrmJ0iWOqHh-JPr2khnhX4C3SiKitkvN-5bTlt7dCTy3LtMphAqnImPiTyEDDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
فرصت استثنایی سرمایه گذاری در   اراضی شمال کشور
📍
آدرس: ‌شهرستان بابل ملاکلا روبروی پارک بانوان
📐
مساحت 31280 دارای سند
💰
قیمت‌ کل : ۱۰۵ میلیارد تومان
💰
شرایط پرداخت اقساطی ( ۳۰ درصد نقد الباقی دو قسط ۶ ماهه)
📅
زمان ارائه پیشنهاد: ۲۱ الی ۲۴ تیر ماه ۱۴۰۵
جهت مشاهده اطلاعات تکمیلی و‌ دیگر قطعات قابل واگذاری به سایت املاک و اراضی آستان قدس مراجعه نمایید.
🌐
آدرس سایت:
https://amlak.razavi.ir/panel/auctions/#auctions
📞
شماره تماس:
051-91008003
#زمین
#مزایده</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/675439" target="_blank">📅 15:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvl7u0JL0Dn5lXAYFInzVYXbX6F_ufKZ3jS_keXEkpLcsuq4eYFB39qUF_WPEhtgFqYyyqZWGWagqZP4zaZnDzijKhENSt0s0xV_SFUJ_c1FFIDDrem2WnmPSzuQ8NWGuvbgSEU1f3C5nXqEKfQPrgRjs7k4RA3fLq9AbUR2-FuAyVT73835nS5g_0_tZMpQh72ah74QtUFJBhN51zmyNSB0lKxhy01GwlmO1P3hdJ9JBcxCw522g5znSO1rvkcagsuK5UEXGYPHH1lwFthv9yoFNPnbxHJ8ImDMRmsKHRb8aOhSsZ8zp1iZSfvXxGjEnuVJgqTFXGXKf1IyEGbSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سرمایه‌ای، فرصتی برای خرید طلا
🟢
صندوق طلای «رز ترنج» امکان سرمایه‌گذاری آنلاین در بازار طلا را با حداقل ۱۰۰ هزار تومان و بدون دغدغه نگهداری، سرقت و تشخیص اصالت فراهم می‌کند. همچنین برخلاف خرید طلای فیزیکی، اجرت ساخت و مالیات خرید ندارد.
🟢
بخش اصلی دارایی‌های صندوق از گواهی سپرده شمش و سکه طلا تشکیل شده و پشتوانه فیزیکی آن‌ها در انبارهای مورد تأیید بورس کالا نگهداری می‌شود.
▫️
خرید از ساعت ۱۱:۴۵ تا ۱۷:۰۰ و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها امکان‌پذیر است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675436" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پژوهش بزرگ محققان: دغدغه مالی مداوم می‌تواند مغز شما را زودتر پیر کند
🔹
تحقیق جدید نشان می‌دهد که نگرانی مداوم درباره اجاره‌خانه، قبض و هزینه‌های زندگی می‌تواند ساختار فیزیکی مغز را تغییر دهد.
🔹
این مطالعه گسترده و چنددهه‌ای نشان می‌دهد که استرس و مشکلات مالی مداوم در دوران جوانی و میان‌سالی می‌تواند به روند پیری مغز سرعت ببخشد و خطر ابتلا به زوال عقل و آلزایمر را افزایش دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/675434" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQBhPGvNJaSHLf1q2fCdUQxmYkTe5uj4Rx5P93S9IbuU3g3r58qrrqf9k9GgSrWBmUJP5-x4DxPGdOda-Qf8CHNXmtlBTKVTBQiScEwFMLCD7R_L2Oxn4jfFQ5atUYWRyNAp-RTdGo-tLVFdHcGh4p-E9wBhVZuX8aY7RWadCBAK666otwIAcJHy4PTB5I6aGR7KRcaOP8Xw7ZIDOiP1qFA5KGARNcVsTe_-SRTqbnXvYHWqK7rRXXVKTy_7szEJ9c8cW3qR-CqlNjJCgckKA5WNgWp3XRkheibz9YnEtHuZdEiOKZ0TbR2cseS8QY4VJ1UdA_RT6ucPm7m_Pqtxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
زیارت به نیابت رهبر شهید
◾️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲، شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/675433" target="_blank">📅 14:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc35f548.mp4?token=o2OgC-V9uCJPVZX9PttaAvsXtOnUCmZ3QkNUBV-qxjxhYAgwigbBPdhwNdGFN1mtCnEgbXJt_UIf7PnGqWJzA4d4PLddBpIu-IX6b_ohKb7nKzDWaj_qUGxFz-DUtL-7x_OVG7LHuLwN3Uyoa-mLR6HXfNYFg0hZmS1sYOpQX391KPv8wDBKKtQ4G5P0vC-09FxipmQ4Nuu-mYcF-isTw5NBwgkSJ2iJYB3eEfkcn6DPMOlZ47NXwvH6RsZXeYg3-a_0XhPHxKusHsq2wmw9zT8xShhRS1QDWvXjD5U3JRbpRN8wEXGBfMJMjX19_TLZ4Tmyf65O-V34myL7CZNF4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc35f548.mp4?token=o2OgC-V9uCJPVZX9PttaAvsXtOnUCmZ3QkNUBV-qxjxhYAgwigbBPdhwNdGFN1mtCnEgbXJt_UIf7PnGqWJzA4d4PLddBpIu-IX6b_ohKb7nKzDWaj_qUGxFz-DUtL-7x_OVG7LHuLwN3Uyoa-mLR6HXfNYFg0hZmS1sYOpQX391KPv8wDBKKtQ4G5P0vC-09FxipmQ4Nuu-mYcF-isTw5NBwgkSJ2iJYB3eEfkcn6DPMOlZ47NXwvH6RsZXeYg3-a_0XhPHxKusHsq2wmw9zT8xShhRS1QDWvXjD5U3JRbpRN8wEXGBfMJMjX19_TLZ4Tmyf65O-V34myL7CZNF4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای خانه را اهل خانه حل می‌کنند؛ بیرون از این خانه، کسی دلسوز ما نیست #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/675432" target="_blank">📅 14:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04731b9058.mp4?token=WgPoIa60sI8kd5lEyE3Zvbcm1JTqcNJnrzPCVr4ZXwP24tWVeGEaGKpvY-LMTEblfMxoJMLIHUROkuOEyPFaYHE9VtR8Gi0DAyzyHmw2WcM4tmwg2K-6FLmxvjoyfD_m0Sk8ld8CmYnkAIZTrtBdN_GzS6BbMsHOlLLeFb7qVevBwUeWSxLfGV3xJnjO2KYTBnlQtaM7mRazsFxi9DMdaMwno2fEuswejUj2_hUoQ6CIKOBdV5qnEQPiuAz8aeFTAwfeDV2gktpeSKMW_-KECOtXj4xsqxlhNf5hVimMMJAT5EF4v0c4_Nml62S1EHo-E4EAoqHKUhfSrL6dWgoCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04731b9058.mp4?token=WgPoIa60sI8kd5lEyE3Zvbcm1JTqcNJnrzPCVr4ZXwP24tWVeGEaGKpvY-LMTEblfMxoJMLIHUROkuOEyPFaYHE9VtR8Gi0DAyzyHmw2WcM4tmwg2K-6FLmxvjoyfD_m0Sk8ld8CmYnkAIZTrtBdN_GzS6BbMsHOlLLeFb7qVevBwUeWSxLfGV3xJnjO2KYTBnlQtaM7mRazsFxi9DMdaMwno2fEuswejUj2_hUoQ6CIKOBdV5qnEQPiuAz8aeFTAwfeDV2gktpeSKMW_-KECOtXj4xsqxlhNf5hVimMMJAT5EF4v0c4_Nml62S1EHo-E4EAoqHKUhfSrL6dWgoCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔹
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/675431" target="_blank">📅 14:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تردد بیش از یک میلیون و دویست هزار زائر از مرزهای اربعینی
سردار منتظرالمهدی، سخنگوی پلیس:
🔹
در بازه زمانی ۱۰ روزه از آغاز ماه صفر تاکنون، شاهد عزیمت ۹۳۰ هزار زائر به کشور عراق بوده‌ایم که این حجم از عبور با مدیریت دقیق و انضباط کامل همراه بوده است.
🔹
از این تعداد، ۷۵۰ هزار زائر ایرانی و ۱۸۰ هزار تبعه خارجی، مرزهای کشور را به مقصد عتبات عالیات ترک کرده‌اند.
🔹
در همین بازه، شاهد بازگشت ۲۰۰ هزار زائر ایرانی و ۸۵ هزار تبعه خارجی به کشور هستیم که نشان‌دهنده الگوی صحیح توزیع سفر در مسیر بازگشت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/675429" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارت شدید به ۴۰ تا ۷۰ درصد کشت پاییزه گندم در جنوب کشور
هاشم خنفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
کاهش بارندگی و گرمای شدید تا ۵۳ درجه در جنوب کشور خسارت سنگینی به کشاورزی وارد کرده است و به طور کلی بین ۴۰ تا ۷۰ درصد کشت‌های پاییزه گندم در مناطق جنوبی با خسارت مواجه شده‌اند.
🔹
باران دیرهنگام و همزمان با تلقیح خوشه‌های خرما باعث ریزش محصول شده و شوری آب تالاب‌ها نیز آسیب را تشدید کرده است. تالاب‌ها به دلیل کاهش شدید آب و افزایش دما با بحران روبه‌رو است و این موضوع سرمایه اقتصادی منطقه جنوب را تهدید می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/675428" target="_blank">📅 14:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فرزندآوری بعد از ۴۰ سالگی در آمریکا بیشتر از دوران جوانی شده است
🔹
آمارها نشان می‌دهد در آمریکا، تعداد زنانی که بعد از ۴۰ سالگی بچه‌دار می‌شوند، حالا از تعداد مادران جوان بیشتر شده است.
🔹
بسیاری از افراد ترجیح می‌دهند ابتدا درس و کار خود را به سرانجام برسانند، از نظر مالی شرایط بهتری پیدا کنند و سپس برای بچه‌دار شدن تصمیم بگیرند. همچنین پیشرفت روش‌های درمان ناباروری باعث شده زنان بیشتری بتوانند در سنین بالاتر باردار شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675424" target="_blank">📅 14:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4IK4S_bWgYaMH-R1FiCdLifUn9F874NuDJWoivDLnizIW9DAU-XSXJRBPd6Zx6cfrlJNgOMnCoOi2nGjPzMTgsHQnVWOZf1uLjasd6YYY3OIV5pauOktGezkyrwCLoPIS1RnNFXblnGYHX4kkNnApLWpPN6qqjTHKJ32XXzfDrbjyH72q0vMyvKTksVqoIDK-iakbXkt2XlRV-rMRSBMjbFuGAlnMy1Y9930fTH1nz54X6mToocFFven891e5DRYdTHn7-ryzzvn62t4wK1vpxDkGbhwpQfR7ZEdmoGFaoNetCV348VI-tzgyiWUQ8U4amuMzaWnIoGNfoXWpFoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
افزایش
حمایت از تولید در بانک توسعه صادرات ایران
🟢
بانک توسعه صادرات ایران در راستای افزایش حمایت از تولید و تقویت بنگاه‌های اقتصادی، عملکرد موفقی را در سه ماه نخست سال ۱۴۰۵ به ثبت رساند
🔹
گشایش اعتبارات اسنادی داخلی این بانک در سه ماهه نخست امسال نسبت به مدت مشابه سال قبل ۲۰ درصد رشد کرد.
🔹
این بانک در سه ماه اول امسال موفق به گشایش اعتبار اسنادی داخلی به مبلغ ۵۶ هزار و ۶۲۷ میلیارد ریال شد.
🔹
این رقم در مدت مشابه سال ۱۴۰۴ معادل ۴۷ هزار و ۱۰۰ میلیارد ریال بوده است.
✅
این رشد نشان‌دهنده عزم جدی بانک توسعه صادرات ایران برای گسترش خدمت‌رسانی به تجار، بازرگانان و فعالان حوزه تولید است.
🔗
مشروح خبر
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/675423" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b32939c2.mp4?token=YXC7AapY2iX0EZmwb7YbC0e2dHlUpGmEZfsKNZZKGPIUpcjqZPvIJz7taNbZaDDl4wF3_QuVH0zRBI3XRZx0TzFFuCGth9RmLlDkZ7HWV3RUAn0oWjCLN2tiQgNcXy-ii1GkMVvadqi8omJdo6Li7Ys72g1M7dLQ_PWHnODYeOPr_d5JhTarqm1FA7U-HzOA9CYpYsiLRihZpLd0vItvJPlHRNppCngsQSBKt97WcfFF7QhJgda4oawZJTY8V-ChrYGEyRvGJBevCvDXRWg_UI8BOqhv0AhfPAQ1nD9vbpup88xmYX3EDyofGnb78JQkxya2rxuFHqjc9wkFryqupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b32939c2.mp4?token=YXC7AapY2iX0EZmwb7YbC0e2dHlUpGmEZfsKNZZKGPIUpcjqZPvIJz7taNbZaDDl4wF3_QuVH0zRBI3XRZx0TzFFuCGth9RmLlDkZ7HWV3RUAn0oWjCLN2tiQgNcXy-ii1GkMVvadqi8omJdo6Li7Ys72g1M7dLQ_PWHnODYeOPr_d5JhTarqm1FA7U-HzOA9CYpYsiLRihZpLd0vItvJPlHRNppCngsQSBKt97WcfFF7QhJgda4oawZJTY8V-ChrYGEyRvGJBevCvDXRWg_UI8BOqhv0AhfPAQ1nD9vbpup88xmYX3EDyofGnb78JQkxya2rxuFHqjc9wkFryqupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی متفاوت از طبیعت بکرِ ییلاقاتِ تالشِ گیلان
ییلاق ناوان، روستای مَکَش
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/675422" target="_blank">📅 14:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a995cdd107.mp4?token=eMA1L-xOcbp0sOJv9khq6iVO0vL064snST1ZxAsBc35pqiN8tLin5_Fg-cHA1s4-Yn-MP3LKaNcoPrFnI-4voaE7HKjTQo7h-XWI4uBsBgyQ2v3HJiNiqLfkW2-e2Rg2RfE563Y8X8RSapbZFfDcUn7ascvS2xFvu7jmNuxsZxTWQhiCsGMkfWihZ5R2zzOrR7duurE8ZQSxH85WqAZ_xS5068XUWU_DeIFAAHF8Ltpnm8jFnQgOAeKuKS8zzUqofOtihCK4QXoRSQPTiHeclzwSyKTy8iRGANBqiErlfonCpqvIU6mRbgPcMnw4prFFpZU80I2Vjc2JiPivgYxYB4Yqyprk9uFoBZD37We1pl0AwlX-xN3S0TC5LxrcURZ6uCPHxTDakJZqAYXL8wk4IJyGNgqUFEk7oo3h9LwesuhDJzQ5_KnlLlHXGXZMt27yQJDJLqHVTSI-0jw-8i3DI5VdL8sLFT7ZANng_EMdLZzv7o7Fxf3Y47SD4zpDERQxyngAbpqavgxDFXvQWdsL6XnNpVT_3AMukoXVL01yWegD_4FJ3dsKm14kVgCne_K1ZleEoFzZGjzWADSMIfvAzlMHg-4ShYYFoKxyZLHrwiscwMFuOgAis0OCRNfCIe0Rvu89UVn6mpX5w8zhNKUuyb5R_725G0h19zPef3uZ75Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a995cdd107.mp4?token=eMA1L-xOcbp0sOJv9khq6iVO0vL064snST1ZxAsBc35pqiN8tLin5_Fg-cHA1s4-Yn-MP3LKaNcoPrFnI-4voaE7HKjTQo7h-XWI4uBsBgyQ2v3HJiNiqLfkW2-e2Rg2RfE563Y8X8RSapbZFfDcUn7ascvS2xFvu7jmNuxsZxTWQhiCsGMkfWihZ5R2zzOrR7duurE8ZQSxH85WqAZ_xS5068XUWU_DeIFAAHF8Ltpnm8jFnQgOAeKuKS8zzUqofOtihCK4QXoRSQPTiHeclzwSyKTy8iRGANBqiErlfonCpqvIU6mRbgPcMnw4prFFpZU80I2Vjc2JiPivgYxYB4Yqyprk9uFoBZD37We1pl0AwlX-xN3S0TC5LxrcURZ6uCPHxTDakJZqAYXL8wk4IJyGNgqUFEk7oo3h9LwesuhDJzQ5_KnlLlHXGXZMt27yQJDJLqHVTSI-0jw-8i3DI5VdL8sLFT7ZANng_EMdLZzv7o7Fxf3Y47SD4zpDERQxyngAbpqavgxDFXvQWdsL6XnNpVT_3AMukoXVL01yWegD_4FJ3dsKm14kVgCne_K1ZleEoFzZGjzWADSMIfvAzlMHg-4ShYYFoKxyZLHrwiscwMFuOgAis0OCRNfCIe0Rvu89UVn6mpX5w8zhNKUuyb5R_725G0h19zPef3uZ75Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سیزدهم از فصل پنجم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ خانم نرجس اربابی که بعد از ورود به دنیای برزخی در کنار یک همراه، شاهد نگرانی خانواده و همسرش می‌شود و به تکرار، رفتن کامل و مرگ حتمی را طلب می‌کند و ۷ روز متوالی از آب روانی که توسط بانویی به ایشان داده می‌شود، می‌نوشد و در این میان شاهد عذاب افرادی که مال حلال و حرام را رعایت نکرده و همچنین دوخته شدن دهان افراد بد دهن را درک و مشاهده می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نرجس اربابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/675419" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8884c8a3.mp4?token=lybra3h9ZAqsIlJt6iPu_xvb0EhXL24ONZIWk_hcxIzN8Io4pY-xY-NcEZniDdWGuw52kG9DcnkIuOuCPUfK7IOwb00xuoAUGZSNRDtf6Iv5aCFo_EnEufeWoEqMSOF8q-ChPtqh943qPIq7S337u4ldkc3fOJos3825cXmg8ZsCF01ON8IB03AGnPpJjxSvTHgt9RAqHGr77vcBzfMrvQ1gxKhglhHPSzfDXg3Z6TpNBWiZNIhWx-QqQMME8zK2eI04bah0FKbr8cQo_KdXdp6LNwDNtlP1hJnAiOxUo2xEyecjYhahiP_-R2hQo-9wl77jHdO_9INRHAhs97rGc1TdRVXEIKIdaJrSMR4JjWO5eMti98DB_ytZe9DDEEHU5ADzn_hcD33DLlXZStIN8JYtMigkgMmq251UcL2plj21Nk5vBAVt3E4jw6VZM-WTg0bbtE_pDw6_BL6qnnRigqefJuvTejoIe0kXVdeIMR_fNw_1V0hFH-8IG2ngcfl9M-2WbM7RJ7mfeDTVfRY1UAlHtT_uJx_sV_IVr9jz6QHmkoR3r4EJT6LfKwlXGx084aibRNUO6SkZcsNqh7mbXJfQmkYG1O7OveJxYHr4sAmXAnOb2Tpc3t7LeJPjA1aRU2sXG0AFxY4YXI5I7JFNwVfOOGPOEpOuz4MEZc2zXJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8884c8a3.mp4?token=lybra3h9ZAqsIlJt6iPu_xvb0EhXL24ONZIWk_hcxIzN8Io4pY-xY-NcEZniDdWGuw52kG9DcnkIuOuCPUfK7IOwb00xuoAUGZSNRDtf6Iv5aCFo_EnEufeWoEqMSOF8q-ChPtqh943qPIq7S337u4ldkc3fOJos3825cXmg8ZsCF01ON8IB03AGnPpJjxSvTHgt9RAqHGr77vcBzfMrvQ1gxKhglhHPSzfDXg3Z6TpNBWiZNIhWx-QqQMME8zK2eI04bah0FKbr8cQo_KdXdp6LNwDNtlP1hJnAiOxUo2xEyecjYhahiP_-R2hQo-9wl77jHdO_9INRHAhs97rGc1TdRVXEIKIdaJrSMR4JjWO5eMti98DB_ytZe9DDEEHU5ADzn_hcD33DLlXZStIN8JYtMigkgMmq251UcL2plj21Nk5vBAVt3E4jw6VZM-WTg0bbtE_pDw6_BL6qnnRigqefJuvTejoIe0kXVdeIMR_fNw_1V0hFH-8IG2ngcfl9M-2WbM7RJ7mfeDTVfRY1UAlHtT_uJx_sV_IVr9jz6QHmkoR3r4EJT6LfKwlXGx084aibRNUO6SkZcsNqh7mbXJfQmkYG1O7OveJxYHr4sAmXAnOb2Tpc3t7LeJPjA1aRU2sXG0AFxY4YXI5I7JFNwVfOOGPOEpOuz4MEZc2zXJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روی این پل، دو ایرانی به شهادت رسیدند
🔹
حضور خبرنگار خبرفوری روی پل رودان به بندرعباس که توسط آمریکا مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675418" target="_blank">📅 14:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af46fd431.mp4?token=t8EayKdJfqmYu-1JMD1qirOltZIK1RY0cB3egm4w3NvlvWQKdbiStVwSOwbwNdh7v10DLZqjy6auSwRwYUhpPkfxygagGiW8gY_F_5YM-ujQ4XJxXEvo4Vwf9rwaaGFrPvYK83AirmWccikYogAjJ8oeFY-YDs4UeMGNBJ1vJ9ozXFSzJHwS-176JcbDIqPx6uWR9mwBybuqe7XVJBO5xDjCsD8rsLhpyBuuFSiAL-X_PJaMGyIS_c8SeaT9s6OoQB6RxL208RCRaDLq-nd2gYqkaz_KzSCMhjFVoyRpzPxNI4h2nyOs-lFx0U8QLaw8gTrLMQRnWJD1oAlCYNGBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af46fd431.mp4?token=t8EayKdJfqmYu-1JMD1qirOltZIK1RY0cB3egm4w3NvlvWQKdbiStVwSOwbwNdh7v10DLZqjy6auSwRwYUhpPkfxygagGiW8gY_F_5YM-ujQ4XJxXEvo4Vwf9rwaaGFrPvYK83AirmWccikYogAjJ8oeFY-YDs4UeMGNBJ1vJ9ozXFSzJHwS-176JcbDIqPx6uWR9mwBybuqe7XVJBO5xDjCsD8rsLhpyBuuFSiAL-X_PJaMGyIS_c8SeaT9s6OoQB6RxL208RCRaDLq-nd2gYqkaz_KzSCMhjFVoyRpzPxNI4h2nyOs-lFx0U8QLaw8gTrLMQRnWJD1oAlCYNGBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
قطعی برق؟ نذار گوشی‌ات خاموش بشه!
این روزها با قطعی‌های برق، داشتن یه پاوربانک دیگه یه وسیله لوکس نیست، یه ضرورته!
🔋
پاوربانک شیائومی با ظرفیت واقعی 5000 میلی‌آمپر، همیشه خیالت رو از بابت شارژ گوشی و گجت‌هات راحت می‌کنه.
✅
ظرفیت واقعی ۵۰۰۰ میلی‌آمپر (یه همراه مطمئن برای شارژ روزانه)
✅
نمایشگر LED دقیق (دیگه نگران خالی شدن ناگهانی نباش!)
✅
ایمن و مطمئن (مجهز به مدار محافظ در برابر نوسان برق)
✅
خوش‌دست و جیبی (وزن سبک و طراحی شیک)
✅
مناسب برای شارژ گوشی، هندزفری، ساعت هوشمند و سایر دستگاه‌ها
قیمت قبل: 1,998,000 تومان
❌
🔥
قیمت ویژه: 1,598,000 تومان
✅
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
📦
با توجه به قطعی‌های مکرر برق، این پاوربانک می‌تونه همیشه یه منبع انرژی مطمئن کنار دستت باشه. فرصت تخفیف رو از دست نده!
https://memarket24.ir/product/brief/60476/180124/</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675416" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75623e9328.mp4?token=DTr1glOhMsUUXmvpxuq8LggAL9_SbwF8EfYaJlop22pMrtYX1Fdyk94a-4MJjGhBMrA2bB6U1fgdu2tSlVki0ge_uS4uIznBmeD8MIbYa-hfvc8cCe4F9r60XVb1bKzJJ1Q-QFMSP78iAYZw8-IOkn6z14F767WIrtBS5LylshiSDdSFBblKQiqwjkP_z0dBi-kPZv43bDKtEPa2-NHAdi8V9Bur1MdGbSOSjqQJ8HDpRDZPHYhJqXeRhELbhK2L8QfAh59YIC9T8VzZJcBQ3_yCFCi_K74kCeLm_VJo5XRgYdVCp2FqRCuka7B64Y7E_hoeZnh1_tbd-7QBnlwDQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75623e9328.mp4?token=DTr1glOhMsUUXmvpxuq8LggAL9_SbwF8EfYaJlop22pMrtYX1Fdyk94a-4MJjGhBMrA2bB6U1fgdu2tSlVki0ge_uS4uIznBmeD8MIbYa-hfvc8cCe4F9r60XVb1bKzJJ1Q-QFMSP78iAYZw8-IOkn6z14F767WIrtBS5LylshiSDdSFBblKQiqwjkP_z0dBi-kPZv43bDKtEPa2-NHAdi8V9Bur1MdGbSOSjqQJ8HDpRDZPHYhJqXeRhELbhK2L8QfAh59YIC9T8VzZJcBQ3_yCFCi_K74kCeLm_VJo5XRgYdVCp2FqRCuka7B64Y7E_hoeZnh1_tbd-7QBnlwDQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت اشک و گریه‌ هاش این بود که می‌گفت از امام حسین(ع) خجالت می‌کشیم که فقط با آب میتونیم از زوارش پذیرایی کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/675410" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077e4d4ba3.mp4?token=aEGDcvb11vaPnRqHAXf4Dpi6SSWLfiy-xV6Rabx3Rw40g4uBJ_E5KkqiWNvVvW6osiRPw7Xka-iilqViQXQraYq3UhQTY6MzFfpazDxc4P-Ie5ojGlVFQGF-usx2C4t12m8W2hE7H6wAhBp2g_NWpDC4s2UT1W0B9TfTd-xq6b3k28-WH7Ktnq0xIYoDCbz_FVbXhS9OwXWf7ZAkSn_BAQJees9PCOf6fm7uFTFr2Mg4n2Bv3wwfQXa0vyxxhpIpf4-01T66wOthJC0PaQGxQBoRWcauN2I_Vq7fBpEHKrVpwTvLCieodAT3LJikeyDDBLrLV8IudI3BeFAg-av-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077e4d4ba3.mp4?token=aEGDcvb11vaPnRqHAXf4Dpi6SSWLfiy-xV6Rabx3Rw40g4uBJ_E5KkqiWNvVvW6osiRPw7Xka-iilqViQXQraYq3UhQTY6MzFfpazDxc4P-Ie5ojGlVFQGF-usx2C4t12m8W2hE7H6wAhBp2g_NWpDC4s2UT1W0B9TfTd-xq6b3k28-WH7Ktnq0xIYoDCbz_FVbXhS9OwXWf7ZAkSn_BAQJees9PCOf6fm7uFTFr2Mg4n2Bv3wwfQXa0vyxxhpIpf4-01T66wOthJC0PaQGxQBoRWcauN2I_Vq7fBpEHKrVpwTvLCieodAT3LJikeyDDBLrLV8IudI3BeFAg-av-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسر بایدن خطاب به ترامپ: چرا انقدر عوضی هستی؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/675409" target="_blank">📅 13:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/If6KkaJZzrO5dHbfZZLt5-UOxUdqg5LxEyfZVKrdj0HYQrKh2MMqk-f7907Sucb0wCqeuhtlm30zG0Rl2vvHOAXqKeqaCHA7AkcVUmz8j22I0tllySofNAQWMnK6b1Fq7M1ppPim471ox91ZKXGZ9z-9PenCHB8nNc8T8DY9Ff5Oo3dy7bQ5v1bDZ6AdQSPizZGuC_dsEqcPYoqR2MEfy_XaF-54PkPRbMcphaD051k26MPHAdpu-VLZ9QNxmEUdKWXq3csm-mhqxKzb7ZfFVxRuR6wyd6Fk2o2_t6pLZ5f90AYRqOHhglIAhEMWZpfCTa5dYERfGvna2sFsOlGruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp6mdGitLRSbkkzFAhiriLA_Fsm5Aynen_HeQFewOdHUujWlSILzRfqzD7q1tqSiDTcgnBrwU7vrMJ6wR975aSOw9SBKnmXyxqjrvZygpuRhzZxEYcIpqHfe0td8wNL7Gtgl905K5HJjsiEnyzCxoKTpm28matyhi66WLhwitSxfmp3D41jwwBsnNX1rO3dLjgFIMi34NvOamp9rZ8T-mQqmNLy3v0yoFkM_p5QzfEXx8cZx9SJnjYffLUTau6QvBrcMgR3rNZ3BxHiNWQC6nynSIqpIzF9_WnxOsMOnttvza0C7JwK-ftzpvNmucRwWXgWjjs3g1hLxbEH8GDFbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orVQTWHiOMWIEVuXcFeUkkzOiLNL0C-GYIUVuYxeZVXUh2ZdbEWv7WimTzLCxdH9K4YWR5q-uTSOk3rRyuevYf0DsXkMMBdw_0DHbA9FAFYttBT1WpyKEh64p28Zi3H_a0hShWLownKIo7e9mzFOWfyTnUel8IqSyzRWmYfJnwqzS-YuwZipI4pT7yHcmAWWL2NEkHkFpkBM6uM4D0joP4TBOi12nVj5MzUsaiZkIdTptNjXahetIhd_wV6ESxLMxC5dtbVOAJ8mVsO2sTXYZzBd_jug1uQQM5HTDexxEdcR4zTzj7T6LWwEnHYWmaLv6KlLoFnD5byCXI8nvDDhPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گونی‌های اسکناس در بغداد/ کشف ۲۷ میلیارد دینار عراقی در پرونده معاون وزیر نفت عراق
🔹
بر اساس اعلام دستگاه قضایی عراق، ۲۷ میلیارد دینار عراقی در جریان تحقیقات مربوط به پرونده الجمیلی و افراد مرتبط با او کشف شده است.
🔹
بخشی از وجوه در اختیار افراد دیگر قرار داشت و بخش دیگری در مکان‌های مخفی از جمله داخل دیوار برخی منازل نگهداری می‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/675401" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4G2Iw-s1NzVVPmDQNRk6-M4keT6CWueHPvf0Jn3XSgc_cutP7O-ooMk_8y6FpHAIs8qBvlWwpJCPk6XRtxk6zuCuVCIZ2GKL18sU5Pocx_CbzDG-4EA2IoewVlwCxzqqympqLvywc61OelJFs5_lEfVhgkqa3Wj-jpn8Kp675RgmXHBXndPqbgP5cykZK-KQPavEjw-w5qDKby-1ErFweJMq64r2dm81lsmK_6cKb-cpDRUOJlNYyKLhCm954m3RWzpvYTTEWcZ6ksBCGgQh9E56DaAxyVVddcxLKWyuslTInLay3hTeiI_D9zoan3YNS_ar9xgThHmw6tNATIvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندی ساده برای دیرتر رسیدن موز
🔹
اگر قسمت بالای موزها (ساقه‌ای که همه موزها به هم وصل هستند) را با یک تکه پلاستیک بپوشانید، ممکن است موزها چند روز بیشتر تازه بمانند.
🔹
دلیلش این است که موز از همین قسمت گازی به نام اتیلن آزاد می‌کند؛ گازی که باعث زودتر رسیدن میوه می‌شود. پوشاندن ساقه، انتشار این گاز را تا حدی کاهش می‌دهد و روند رسیدن موز را کمی کندتر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/675400" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675392">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arOjLfw3vwJ_glCxMly-w05KiYyY2gvs60SCz5HMd9kiEnlfsZz0vHs5HtgftmeN1iLRFA6uwUG8agIg5ZECYEXdsPqw21DnIkC1xBtKaQcR8eFt2NsI_UP7ftk1kIAFYr9LCL8mqgN_y-AzChkj-gs5kmCXM6WpgxkwZk76ZPGfp-WFRkcluENKigBk-qvv5z5e70JCq1j1fdo-e4afh3vRgJewSYq0zRB7OCQpMIMGUXnaQzsnNVYhZQhaQLkh_ZkN8wvj0WQ3OvKtGwLnwxUgTVAgCBxgzEthNKk9UOW8u63QDX94X16w1HabrqP9fsXMjhwx3WqNgK1usd_EoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_zhSyezgA6_PsZJ2atGRMLg6ckAAljhanShjw_wWTAHIxbc0UxuNMXHxAEHcPLF_9kFZHHbyrPt321T7y3kqi9tetsK7kW0_YN0Pw8eaLoY_qph5LlL-vamWaKuwGqxx0tNslc2UK3364N9OXIkX98lSt_p8seYpnYCnDrFq_JOnuidYz1cAD1QQBV5reTrXQkb416-SkZJnasBqWcxA2FYTJ7KHh_1eTtIk-EyQSGRqObFftltgTlKFK3f2M6xUL2jYmVPdU9_2K9g7J_eyWb2_giyPLMaO9dTq7g3FuxERpYBgid7FH2lSHqYctlkjveQsmcEXDfEH0NEVT55XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xp0QqgC0y2iH_u-aw5WYyB3Pb8RsgaJRTR32B9p6NgAXE-knKzfLqyhEIDB0GTAgigArbGjn9cH2DFe-zF6LtFaEDR1ufpCKfXUS-7scEs8xiD0ozgZk2fYAfAnCmQK-dm6IGezNLyzr6VK83-eSeprVF2pp8YMjC67K-Pn5kN0fXEhqGM34pzYO4Dev_oQ9sUolhBnqpacyp6dMxvCH5YWTCMDZzBT3xRYIJA_WARYe2bQpERX-ZR0CFPIYqQTkjeODd83VYJITDEv2et8AJbQHFO6wU8nKKmbbLpCXuJjFKH8sR2oglccGRiwIpyiU8L89Z1tkjHhTJ0C624oCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubIDtp4K71Rh2DnEIYAQPveCPjfA1eQzfRyQEh8L1e0vXR5RTWc1PUw1PqwY99JKJgIq3Kf1t7XEsVuc5xLs7EA5UoqmoITY1kYOTG_hyzYWTTnK-y01FMkcEU0pW5RrJMrbtCh-u_OT6g8dWb4__OTEC4uOZr2UhM5oTkRLSqxK-WdZCcrFdZJm1ZF5NaSi5kpdIBuGpIujC-05zRCf5laLpXG5nKZpgiE7twZGQvfuoh-Z96NX3G1yHnOsTz35rQBuizBnwKKEmjhb4BFwqujUjwH2h0tgKGF5jGT_TK48ZPEEn6DqyKCSz6js7iogJ97wuvsRpTVVuQ_bpzdbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve5ydn9n6ky3zEv6yMD2r4HOBfZpVa4n0VPXkohUYWyqzhT_iRG5C254VlCW0QF9BKNMrLR4E9L3PYi1gmG_JG06pxAImAtRfwXhnEBFE52hKvTb8-VlHtOZX9so5h0MU4Tt1SdJzMz2hWCtiWNdEFMUFJBWnmNsQWnTPhjSiF4Xa9ByaaaKYTlccZ4zQsmr27_Wp6fqkw667zzLw6N79QUF3lHs0jWOCXfY8RnWVk0G2T9FluJOtVsEUtQ6QjD8LOBGuFKxIABEV7X491G79_fJ-cvg9KDBXWS29lRuHBHxwgGeyxe6ThgEDyh7xvyMYX3KlZTY7iFwOiCj2wQZqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مقدار دقیق مواد برای ۵ تا ۱۰۰ نفر؛ دیگه نه کم میاری نه اضافه می‌مونه
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/675392" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675391">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
آشنایی با خدمات مرکز داوری اتاق بازرگانی تهران
🔺
حل اختلاف قراردادهای تجاری از طریق مرکز داوری اتاق بازرگانی تهران نسبت به دادگاه و محاکم قضایی، مزیت‌هایی از قبیل کم‌هزینه بودن، یک‌مرحله‌ای و رسیدگی سریع‌تر و کاملاً تخصصی را دارد، ضمن اینکه محرمانگی پرونده اختلاف نیز کاملاً حفظ می‌شود.
👈
سایت اتاق بازرگانی تهران:
https://news.tccim.ir/
👈
صفحه اینستاگرام:
https://www.instagram.com/tccima/</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/675391" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
چالش تفاوت قیمت‌ها در بازار لاستیک
🔸
تفاوت قیمت لاستیک در بازار، یکی از دغدغه‌های مصرف‌کنندگان هنگام خرید این کالای ضروری است. بررسی قیمت‌ها در برخی فروشگاه‌های سطح شهر و تعدادی از فروشگاه‌های اینترنتی نشان می‌دهد که بعضی محصولات با قیمتی بالاتر از نرخ مصوب (۳۰ تا ۵۰ درصد) عرضه می‌شوند؛ موضوعی که دسترسی به قیمت شفاف و فروشنده معتبر را برای خریداران مهم‌تر می‌کند.
🔸
برای نمونه، در یکی از محصولات بررسی‌شده، قیمت مصوب یک جفت لاستیک سایز  ۱۸۵/۶۵/R۱۴ از یک برند پرفروش حدود ۷.۵ میلیون تومان است؛ درحالی‌که قیمت همان محصول با مشخصات یکسان، در برخی فروشگاه‌های عرضه لاستیک و فروشگاه‌های اینترنتی تا حدود ۱۱ میلیون تومان نیز مشاهده شده است.
🔸
تپسی‌گاراژ با هدف ایجاد تجربه‌ای شفاف‌تر و مطمئن‌تر در خرید لاستیک، امکان مشاهده قیمت محصولات و خرید لاستیک‌های موجود با نرخ مصوب را فراهم کرده است. کاربران همچنین می‌توانند لاستیک موردنظر خود را به‌صورت اقساطی تهیه کرده و برای دریافت خدمات تعویض به اتوسرویس‌های منتخب مراجعه کنند.
🔸
برای مشاهده قیمت‌ها و خرید لاستیک با قیمت مصوب و اقساطی به
لینک
زیر مراجعه کنید.
https://tapsi.link/rh2g6</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/675390" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPxoS2oeOD8E7i9G_3oForWXJo5Z89wjWAFZxy2v7TuCmtjaOTvY5VC6oESYnD9DcFZUr3FaRTS8MqvZIEN-co_NgpSHrgVyCP46QK-pt_e6w4-AaVqxSvD2GiwS7Foe6uDvLevJ3Drifl4KzycfIGGfo8qASDeCfENYnhOAOzPKzt8FMLNKrcpJybngMw70cDTh97-N9f1z2jxVKKY5AXQUnV8LqhJYak3x9ncKkI9lZLmmDoiPOG6ag9Mv3ORLXtbfWJczxLQklgHz3GJBz4XxJBp9hkgwqkTCUM4kkRO5raYiceWKNI89G3aGZo5nvrPqQV_Y_pGnKES6Ye5Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ مرداد ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
امروز قیمت دلار در بازار آزاد با کاهش نرخ به ۱۸۷ هزار تومان رسید.
🔹
همزمان بازار سکه نیز نزولی بود؛ به‌طوری‌که سکه بهار آزادی با افت حدود ۴ میلیون تومانی به ۱۷۵ میلیون و ۸۳۵ هزار تومان رسید.
🔹
بازار طلا هم در مسیر نزولی باقی ماند و هر گرم طلای ۱۸ عیار، روی رقم ۱۷ میلیون و ۹۷۲ هزار تومان ایستاد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/675389" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور امریکایی: هیچ تهدید هسته‌ای قریب‌الوقوعی از سوی ایران وجود نداشت؛ ترامپ آمریکا را ناامن‌تر کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/675388" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی، هنرمند تکرار نشدنی سینما ایران
🔹
گفتگوی خبرفوری با مسعود ده‌نمکی و احمد مهران‌فر در مراسم تشییع اکبر عبدی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/675386" target="_blank">📅 12:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانی‌‌ها روزی ۷ هزار تن مرغ می‌خورند
مهدی یوسف‌خانی، دبیر انجمن کشتارگاه صنعتی و صادرکنندگان طیور ایران در
#گفتگو
با خبرفوری:
🔹
به دلیل بالا بودن عرضه و پایین بودن تقاضا، حدود یک ماه است که مرغ زیر قیمت به فروش می‌رسد. پس از گذراندن دوره ۵۰ روزه، حدودا از ۱۵ تا ۲۰ مرداد مرغ با قیمت تمام‌ شده کمتری به بازار عرضه می‌شود.
🔹
میانگین سرانه مصرف روزانه مرغ در کشور حدود ۷ هزار تن است. فعلا صادرات مرغ نداریم و به واردات بی‌نیاز هستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/675381" target="_blank">📅 12:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675379">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داروهای روانپزشکی رو باید تا آخر عمر مصرف کرد؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/675379" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675378">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsD2kxtQtb3tjukJoaTFwG1DmnBZYNs5QAehSR0IJZ5IURYuZwhk51x80J91dB8SHj0hgFVJilXUbwUYujEpFfFo1WDhR7bOE2yNLr_tf6aizGaiXw8bF7mWWmXWI8Hu5OlVJpEc5BW4aDEZ99GpXK1MBg_zKpIKygPI_DWShRtNm5T1_4EZkFvwP3eN1r0UD0MFqsBqlbWUwhbIdYS8PMx_X3McN1h-hraTHonyYal_AQ1up_Tw4yUFRU15wEPKohG6w1LdvFEMN8yQVMcKpmlBytyB9LEbsFy0XudxI4yNWVA4bvcwKlk6W4GUBpf5dHWBiVu5BU9Wg0m2IYX8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
برسد به دست زائران اربعین
تمام خدمات مورد نیاز شما در یک اپلیکیشن جمع شده است:
🔹
بسته‌های ویژه و پرتخفیف رومینگ (اینترنت و مکالمه)
🔹
بیمه رایگان تلفن همراه
🔹
تامین ارز زیارتی
🔹
استعلام گذرنامه
🔹
خدمات سلامت آنلاین و...
📱
همه در نسخه جدید اپلیکیشن «همراه من»
برای مشاهده تمامی خدمات دیجیتال و خرید مستقیم کلیک کنید:
https://www.mci.ir/-4I2DXIW
https://www.mci.ir/-4I2DXIW</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/675378" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: سال تحصیلی جدید حضوری آغاز می‌شود
🔹
وزیر آموزش و پرورش شایعه مجازی شدن سال تحصیلی آینده را تکذیب کرد و گفت برنامه دولت و آموزش و پرورش، آغاز حضوری مدارس در سال تحصیلی جدید است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/675376" target="_blank">📅 11:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توصیه‌های وزارت بهداشت به زائران اربعین
فرهادی، رییس مرکز سلامت محیط و کار وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
باتوجه به تابش شدید آفتاب که حاوی اشعه ماورای‌بنفش است، به زائرین اربعین توصیه می‌شود دو ساعت قبل و بعدازظهر حدالامکان زیر نور آفتاب نباشند و ساعات استراحت خود را در این زمان تنظیم کنند.
🔹
در ساعات اوج آفتاب حتما هر دو ساعت یکبار از ضدآفتاب با SPF بالای ۳۰، لباس حفاظتی و ترجیحا روشن که تمام قسمت‌های بدن را بپوشاند، کلاه لبه‌دار و عینک آفتابی استفاده کنند. همچنین خوردن مایعات، به‌خصوص آب و یخ، از گرمازدگی و اثرات سوء اشعه ماورای‌بنفش جلوگیری می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/675374" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
فهرست خسارات بسیار سنگین آمریکا در پی حملات ایران منتشر شد  سردار محبی سخنگوی سپاه پاسداران:  طی ۱۵ روز (از ۱۷ تیر تا ۳۱ تیر) آمار خسارات وارده به شرح زیر است
🔹
در حوزه راداری و پدافندی:  ۷ مرکز فرماندهی و کنترل  ۳ سامانه ارتباط ماهواره‌ای  ۶ رادار پدافندی…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/675372" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تیزر/ مروری بر مجمع سالیانه «وتجارت»
🔹
تیزر اختصاصی شهر بورس از مجمع سالیانه
#وتجارت
.</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/675370" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
