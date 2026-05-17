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
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 00:42:31</div>
<hr>

<div class="tg-post" id="msg-436284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io0_NaIIw_esONcbMj7O2lczRq-MqZHsbxYGq6WMmXqGkt4xnGLPLeZ3Lu1WCKcd-NMAsZ8PTQZIKUsCwy8tVeckBtjWaOWysuUxNYXaBDVEvDDzBOaGB9V_SYOP5dgdhuFyOKXzocktD7I9MmvY5wEeNWymWTYQlfRC6CfUWw2epsPHhB7SJFQwv533-f1bbrpvrs4YgtYTkTwMCVJ7tKRDUdmWnWyr7dUcg1rE109ffj4iGWeL6DxwPzFqu-XDBq215VuUhiFj2YQ5s5tE19lG0o6hDw1ehI2katQQ1GQSALORK7EI-SCqNWGTISwnnmgkS0YK7Ku26-GfDGokjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه‌کارهٔ جهنم!
🔹
شخصی از ستم و بیداد حاکم شیراز، که از خویشاوندان اعتمادالدوله بود، به تنگ آمد و برای دادخواهی راهی پایتخت شد تا شکایت خود را نزد اعتمادالدوله ببرد.
🔹
وقتی آنجا رفت، از ظلم حاکم شیراز نالید و درخواست تظلم‌خواهی کرد. اعتمادالدوله که ظاهراً قصد داشت به نوعی از سر باز کند و مچ فامیلش باز نشود، به او گفت: «اگر از حاکم شیراز ناراضی هستی، به اصفهان برو و آنجا سکونت کن.»
🔹
مرد گفت: «نمی‌توانم، چون حاکم اصفهان برادرزاده شماست.»
🔹
وزیر گفت: «پس به کرمان برو.» مرد پاسخ داد: «آنجا هم نمی‌شود، زیرا حاکم کرمان داماد شماست.»
🔹
وزیر کمی فکر کرد و گفت: «بسیار خوب، به تبریز برو.»
🔹
مرد با ناامیدی گفت: «حاکم تبریز هم که پسرخاله جناب‌عالی است!»
🔹
اعتمادالدوله که از این همه اطلاعات و پافشاری مرد کلافه شده بود، با عصبانیت فریاد زد: «اصلاً با این اوصاف، بلند شو و به جهنم برو!»
🔹
مرد با خونسردی پاسخ داد:‌ «ای قربان، به آنجا هم نمی‌توانم بروم؛ چون آنجا هم پدر مرحوم شما پادشاهی می‌کند و مشغول حکم‌رانی است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/436284" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: تامین پایدار کالای اساسی و جلوگیری از گران‌فروشی راهبرد اصلی دولت است.
@Farsna</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/436283" target="_blank">📅 00:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادعای عربستان دربارهٔ حمله پهپادی از عراق
🔹
وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شدند.
🔹
عربستان گفته حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/436282" target="_blank">📅 00:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSus3I9vJLCzwOLf-6E18PKFWjhmkVCEheLIUZqsYwm3rBCAkcrnZun4xp2ffSvKPoG736iOiDuzkVuqkK9jJ37hiS33EFUo-rsz0zFniMfa_Bn1yWKfurIhPvcKNosviC0RiCbLRAuPr7YU25uvkR3jWs-inlHoY4rjd3lRYVl68RxDDbvKIm6MpyKb6wzURAtPISDg7YS3E9nmSrboKnCwL7Tyh6_Xq0MbyAy3EK3oItt6rJszrv-8YHjpTIBY8EkY1vMRuR5q57YORhOnhpB-O_-8-rVXEa0Eu88vLJhmte49XDnWICMiakB7AimqZwQIlqGlORc_0w3y-EBz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoRhjW8sd0Aqp9r3Mv3RRBRNIW0CZf0N-e1OyrJh8aJNuPFpWYWmlYwfPmd4Z9Gzg44kCvqnZBKLZJ_qcAb2Y9dKGmnUCxhvN-mFgaa99GHQd3QD-GmDUQiT-xy26rtTgPFuuvEv6zM2jdji0oyXosvmN5OkdZlyDhgp9sQjHrYEWF3r1v4QvPuoFa7DIPBBQdNrwxMETFLrlX_0aJlZtwU6Ah-1F2V6wLMDUVjh64B1SGWlHBfSKVjIXM_upRARg7lnKQfJE5wn0zP1ybXJfXvjiSzOs_HPi3cNaZ0zIimhNLS5WLuN6aMmDtDW8QxAI5E-tms_VbigoH5DG94Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3JenI_MKu-nvULSagchAiLtHd6gXhaW98cJZYK95Doy3PEsnBl1h9hMC4E3zPm4mYGwWQPEUNDlI8qU0RaNa0WdQAhmivbr1deF0h6VjMTrqH2m8GDQ9Bn-5GD_qX32QfcZuaEStf7sQhiEiB2MIULZ0jEMxnNRPIDZR9LSE1lJU5OwyOdB-x_lvvvrx7ouRZZnRnA_2yVa_QlETuu2V4bfHvO3TDw8VjPsvZjaUDePIy3cUvYdA1pDrnFPUNma6tFDEYC90zeDfRYd2AUvDLREsH519SyYlgY-PvhaH4JZA_2_3wD1LIiXYpQTFEdEeRv5Qmx_q71YnSi5zf1RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqkP0k_8ngL4lfJitB-bQsfu3p1gmZTt4MqSeuphtyBXPfwjDOSIpB3UUzYgTLwuyKhtKAdBnoVAjeRFuNxucFg5jOWKa_BapSQ8DPuCyZ2SgGMeNHo1nAAuCtV8Rk0fe0p0fi-kjunWTIAELegqfTDL_Ib7osF8S9BZY-NFTGraBO360IIuHkca0KAGOZ368KZ39Axf_gLXRXWS2ic82GHkKyMfuttd0hKLDYpSzm1SR2PgJLmL-YlGBrkb-H_piuyCCdbM0wdFJuh7rLq9eMFsw6gJPxudTf8KlPJ6YIrM-g4ourTN_vvCG_ECDfJup_UFy1v094Tm3Twaq8Ri1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXYL3ix1h8sxxOzWWMFfKsDObmpRTRA6Jllg7i7OpP7p0t1EET1Z8VqSKqaZri_VREeupA6_PxkMaBK4nlasQ1NkyPp2bBAZ_xf9bymRmz_FiI16q8-_9bOAS65bsIe4520kSZMFFSFrv_5pe2Z8cTeQQBmNN1jstUlNOlyGDZEPiwwnOyOUh5Aka51XjDqYy73_WNvHWlVhMPB3chZ31K4cnQvVICgY1DgBRXcFy1zPPDTWllTMJ-3STlWbdT4mU9Dw13GUsVG93gKCwUDDIz32V2maJoDowm8oBapL5iQ45rnCOmcXS1tlR1srVwqbWr3JcXo9tHMeKPL4d1sVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4c7LJjBpbxsg2cXUfhptHxTf56NYJuMYz0_7XxegxvVumrtPGHKC9_jfaUnfvY9WC94PbXvHdPAqqGZG_XDcrC11RVTjDx7rCvhV137i6T-YJJNSalBAIuImvaK1BxJv-VqfGDR7z7HSwuTGFVtX7eQgM-NsX9GzlRyotTWy5jTQ214Xw10fUVd9bWqaYFMAQ3g-Pmmxf3jUNDlY2TBKonxklrl_-iVQ8eK2M6RMG6xT6epmqNVxoVO7QpKsF3-cGC2BuJBHvrUohkBNr7r9Sw0j3JsPxHTAhntO6F5XWrY3FX1n1cEfXhCwhCaMOJ4R0slN4M44AaQm1hP6lS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liAjq4-eL5YRSwewL4Iro6MkuPRu-WWTSMz1vfJep2R32kzX2i8GvHj5H9K42ymceR70fbw2NTJZF8TQV9DMzkt5oM4SjYPUf4uXvh50m9SeY_nuj1KjVDXytC6UjLuCri4220K0t2eho1cSwW21akgPe71OIDfEE6oRa7vz6Y2dw_h-o5c7nY6nj46AnM4O3guKqTcAts5hFJooefGXzadp7lQILDlAhiOx2B0gzFoSTooPt4qb_HQeeSSgG7-5E8EJArZ2Zp5z8SJsTAfkWxVnaxSCfo7qPy_CcUnDQrj7-FCtcC3Rv26cZwMQwcTy6PdvXlgAZgQUQoW7vSV37g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موسم برداشت گل‌محمدی در خراسان شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/436273" target="_blank">📅 23:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین سرود ملی در موج ۷۸ تجمع مردم لردگان چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/436272" target="_blank">📅 23:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام پهپاد آمریکایی در یمن
🔹
برخی منابع از انهدام یک پهپاد MQ9 ارتش آمریکا در آسمان استان مارب به دست نیروهای مسلح یمن خبر می‌دهند‌.
@Farsna</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/436271" target="_blank">📅 23:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رقص پرچم ایران در ۷۸ شب اقتدار در میدان سلیمانی کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/436270" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: وقتی آمریکا می‌گوید ایران نباید دانش‌ هسته‌ای داشته باشد باید به این موضوع مشکوک شویم
🔹
این شک به‌وجود می‌آید که نکند این‌ها در چند سال آینده کاری می‌خواهند علیه ایران انجام دهند.
🔹
ممکن است بعد از این بگویند ماجرای هسته‌ای حل شد، حالا برد موشک‌هایتان…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/436269" target="_blank">📅 23:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها امشب با شعار اقتصادی به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/436267" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436266">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g61E_WpTFgNyfHUoj2lkYAKAvO5_3d7nSOKaxNGw3rlPPc52WTRzgn1gyflZULH8C1jajEJvKRFO7aIHGnQn3JnVHRdbtJ4XYgd3hyshWE5TxtEh473o_lrKeL0WRgRRGLuGwhB0tFST5oMnm4_uldemTw5Bw4O-vHY8l4ElSr1v4ewtCSEU3GqxiAAjAsG8tLdn11hbSkrayX1Ra-mpJ98xFkGT3TojS-ZL5PfU2E_hYjyjW36nrbGnCnz4jiYj9vLlQp6b0vAl1BXBFh-tvqM19FtMAIfJT62GLp1flEfL3Td0Yz3CUy3if9fxPEf_o2nIs5FLKruAEWoZK8nVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه‌‌ انتخابی دولت برای مدیریت بنزین در پساجنگ
🔹
درپی آسیب به زیرساخت‌های نفتی کشور، افزایش مصرف با لغو دورکاری‌ها و اندکی اختلال در مسیر واردات، دولت مجبور به گرفتن تصمیمی برای مدیریت مصرف بنزین در کشور است.
در چنین شرایطی دولت ۲ گزینه اصلی را روی میز دارد:
🔹
گزینه اول: افزایش قیمت نرخ سوم بنزین موسوم به نرخ جایگاه (براساس مصوبه سال قبل)
🔹
گزینه دوم: کاهش سهمیه‌ها بدون تغییر قیمت که طیفی از بدنه دولت آن را دنبال می‌کنند.
🔹
طبق موضع رسمی دولت و گفته‌های معاون اول رئیس‌جمهور دولت قصدی برای افزایش قیمت بنزین به‌عنوان راهکار اولیه ندارد.
🔹
دولت درحال طراحی بسته‌ای برای مدیریت مصرف بنزین است که در اولویت آن، افزایش قیمت قرار ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/436266" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
ستاد استهلال دفتر مقام معظم رهبری فردا دوشنبه ۲۸ اردیبهشت را اول ماه ذی‌الحجه اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/436265" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
۷۸ شب است که قرارهای شبانهٔ مردم شهرکرد ورق می‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/436264" target="_blank">📅 23:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
۲ جنگنده آمریکایی یک‌دیگر را سرنگون کردند
🔹
۲ جنگنده اف ۱۸ نیروی دریایی آمریکا در جریان یک نمایش هوایی در ایالت آیداهو، در هوا با یکدیگر برخورد کردند.
🔹
هر ۴ خلبان موفق به خروج اضطراری شدند، اما هر ۲ جنگنده سقوط کردند و منفجر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/436263" target="_blank">📅 22:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
محسن رضایی: بسیاری از پژوهشگران عربی می‌گویند ابوظبی برای عربستان است
🔹
اگر امارات در جبهه صهیونیست‌هاست، پس قبول دارد که نقشه غرب آسیا باید تغییر کند. آیا بن‌زاید می‌پذیرد که ابوظبی جزو عربستان شود؟ @Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/436260" target="_blank">📅 22:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
۳ نفتکش ایرانی دیگر محاصره آمریکا را شکستند
🔹
تنکرترکرز: ۳ نفتکش ایرانی با ۳ ترفند متفاوت خط محاصره آمریکا را شکسته‌اند.
🔹
یکی موقعیت‌یاب خودکار خود را خاموش کرده، دیگری پرچم روسیه برافراشته و سومی از خط ساحلی عمان استفاده کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/436259" target="_blank">📅 22:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: محاصرهٔ دریایی آمریکا را می‌شکنیم
🔹
صبر ما حدی دارد و نیروهای مسلح درحال آماده‌کردن خودش است. @Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436258" target="_blank">📅 22:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: یکی از ۳ ناوچهٔ آمریکایی که از سمت عمان وارد تنگهٔ هرمز شده بود بر اثر حملهٔ موشکی ایران آسیب دیده است و آمریکا صدایش را درنمی‌آورد.  @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436257" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055b2b9f77.mp4?token=APNZqY60QhAYr1f47ctBWs7MlaqfHrAJnAOyuRqlaqfauDUIQIyXBqeBc-PIPROD40BGUeeKrXsx29q1GEMdsO2cowTefZfbrnt_6cc1_-9TMB_TXcBABalxgjzlNQvkBTDxwmQeskYAGBNb-Lo21wOibLvUPWG3TT1zil_5tVkrjISIXjddk5hGFekyDMCC_VISqnju2KybGNp3Q8sHuJYUQlooBecEm4SiTK1PbE6nq-HNN_GjHzLLBB1cozaXy4nJZ62z7tKCV0lGWrp7V6vguSrsNwPdKNpprdr7Cd3OVD3l8TlJTVwNLgkZaNTI_f4xNJqSuPcOnszdX64ziD6NiEEH489X1cHohs6wovq4nZkQpYdyC-TDfxWXVjbFliw6-nAHzYc-hhkJTcu7v7IubY-oMTDjkYMwIZIgabW95Ouf-4aFop_ZzO9uy5gy5M4LoI_OAgZHwG4VePgJkOg6kCINnmy26Yb-zgs8e4DbLud3UqA0pANFUWxqiKlv1ddtOGJMZzAFEp5cnh-oLbQwf4ulVPr-cY5re9L50na4ziDG2t361MgnV7KI0CZ3oHSkgMnnVKsSjQJjASRsCn7uxyitVp5Dd0SnaZKI_thRxbVqwJIMVjsHcjXiNsF-7cq8CNZDfhN1_QZBtKoL9h-W9bD8h2jArEaNX90ABq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055b2b9f77.mp4?token=APNZqY60QhAYr1f47ctBWs7MlaqfHrAJnAOyuRqlaqfauDUIQIyXBqeBc-PIPROD40BGUeeKrXsx29q1GEMdsO2cowTefZfbrnt_6cc1_-9TMB_TXcBABalxgjzlNQvkBTDxwmQeskYAGBNb-Lo21wOibLvUPWG3TT1zil_5tVkrjISIXjddk5hGFekyDMCC_VISqnju2KybGNp3Q8sHuJYUQlooBecEm4SiTK1PbE6nq-HNN_GjHzLLBB1cozaXy4nJZ62z7tKCV0lGWrp7V6vguSrsNwPdKNpprdr7Cd3OVD3l8TlJTVwNLgkZaNTI_f4xNJqSuPcOnszdX64ziD6NiEEH489X1cHohs6wovq4nZkQpYdyC-TDfxWXVjbFliw6-nAHzYc-hhkJTcu7v7IubY-oMTDjkYMwIZIgabW95Ouf-4aFop_ZzO9uy5gy5M4LoI_OAgZHwG4VePgJkOg6kCINnmy26Yb-zgs8e4DbLud3UqA0pANFUWxqiKlv1ddtOGJMZzAFEp5cnh-oLbQwf4ulVPr-cY5re9L50na4ziDG2t361MgnV7KI0CZ3oHSkgMnnVKsSjQJjASRsCn7uxyitVp5Dd0SnaZKI_thRxbVqwJIMVjsHcjXiNsF-7cq8CNZDfhN1_QZBtKoL9h-W9bD8h2jArEaNX90ABq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حضور شبانهٔ مردم مراغه در رزمگاه خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436256" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed901ee5c3.mp4?token=WacjwXDqANpsLg032hJjeiD5ERGeC2s2z-fJszPQ-Qxrd1J5YgeR5pxGqHz7I0yZ--o7kGotD5HYE8cMAuGBEB1bLET7RIYNF4echjuty1X4VMUEkQZ4g3RIqxFXLaCw0oipdTxv-p_SvJKAML7KTkK0kniyM6tw8Hu-FqWGTdaoK96Zgqy1I7g-XmUWiabxcLU3lS6Hd0ie_ry1Ek3aUaiON71hAOMPNm_LC8W_aTiUBcMhXSM-pHrSlCPc_K6-aGCyE-9bTfI9ZipQkrVK5h6_YYWjj0mH_zTvD0u1zNN_BYjxStrI2IAvuSE1SH8qbLLbhGRKAz9seNItn0biMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed901ee5c3.mp4?token=WacjwXDqANpsLg032hJjeiD5ERGeC2s2z-fJszPQ-Qxrd1J5YgeR5pxGqHz7I0yZ--o7kGotD5HYE8cMAuGBEB1bLET7RIYNF4echjuty1X4VMUEkQZ4g3RIqxFXLaCw0oipdTxv-p_SvJKAML7KTkK0kniyM6tw8Hu-FqWGTdaoK96Zgqy1I7g-XmUWiabxcLU3lS6Hd0ie_ry1Ek3aUaiON71hAOMPNm_LC8W_aTiUBcMhXSM-pHrSlCPc_K6-aGCyE-9bTfI9ZipQkrVK5h6_YYWjj0mH_zTvD0u1zNN_BYjxStrI2IAvuSE1SH8qbLLbhGRKAz9seNItn0biMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: یکی از ۳ ناوچهٔ آمریکایی که از سمت عمان وارد تنگهٔ هرمز شده بود بر اثر حملهٔ موشکی ایران آسیب دیده است و آمریکا صدایش را درنمی‌آورد.
@Farsna</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/436255" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
چرا باید پای ایران ایستاد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/436254" target="_blank">📅 22:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnR7SBMJ792iWkd6_9xR4jCC5KLhcxOILeXUjUg2Ab3gasqZXLRB4d5tYbjog5Z4dicot5_kgOJON4Ye_pj5QSGCwlnWU2HpDX-ej_KVbc_xeZCwsJlF_wkp9ZiwsV0RNYHR89sg9KjRnpA2XQRi1h8y0eKrO5AV1_VdSx4exxrLoKFK53ptjmUv4UhvgIFxWrE-Bl-c54Vq5PwLF5D1H6NMRttJVPs0LMvpYFlqoWGZtXYNpvIekf2kNoxqc-jhrnnU13iY7Se0FvaUxEMRiMYj4DoFrzGGFUFiOLBaOv-ZbNo7i68NJT3BLNCblQfKdHAkdkDUT_U3I6jo1DyBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پلتفرم‌ها در کشور خودشان از اینستاگرام و ایکس هم غول‌ترند
!
🔹
شبکه‌های اجتماعی فقط اینستاگرام و ایکس نیستند. در بسیاری از کشورها، پلتفرم‌های بومی آن‌قدر بزرگ شده‌اند که میلیون‌ها کاربر دارند و حتی از رقبای آمریکایی قدرتمندتر عمل می‌کنند. از چین و روسیه تا هند و ژاپن، هر کشور نسخه بومی خودش را ساخته؛ با فرهنگ، زبان و اقتصاد مخصوص همان کشور.
کره‌جنوبی
🔸
کاکائواستوری: اینستاگرام نسل میانسال‌ها، مخصوص کاربران بزرگسال که با کاکائوتاک مرتبط است.
🔸
بند: شبکه گروه‌های خصوصی؛ محبوب مدارس و شرکت‌ها با بیش از ۱۵۶ میلیون دانلود.
🔸
سای‌ورلد: پدربزرگ شبکه‌های اجتماعی با آواتار، اتاق مجازی و پول دیجیتال. میراثش هنوز در همه شبکه‌ها دیده می‌شود.
ژاپن
🔹
میکسی: شبکه دعوت‌محور با نام مستعار، محبوب سال‌های ۲۰۰۵-۲۰۱۲.
🔹
لاین: اپ پیام‌رسانی که پس از زلزله ۲۰۱۱ ساخته شد؛ با استیکرهای بامزه و بیش از ۷۰٪ جمعیت ژاپن کاربر.
روسیه
🔸
اودنوکلاسنیکی: شبکه هم‌کلاسی‌ها، محبوب نسل مسن‌تر و مناطق روستایی، ۳۶ میلیون کاربر فعال.
🔸
وِکُنتاکته (VK): فیسبوک روسیه، ساخته پاول دوروف؛ صدرنشین شبکه‌های اجتماعی روسیه.
چین
🔹
وی‌چت: سوپراپ یک میلیارد نفری؛ پرداخت، رزرو پزشک، خرید و خدمات دیجیتال زیر یک سقف.
🔹
وایبو: ترکیبی از توییتر و اینستاگرام؛ ویدیو، استریم و اخبار زنده.
🔹
دوین: پدر تیک‌تاک، با الگوریتم «For You» و تجارت الکترونیک داخلی.
🔹
شیائوهونگشو: راهنمای خرید و شبکه اجتماعی سبک زندگی؛ محبوب نسل Z.
🔹
کیوکیو: پیام‌رسان و شبکه نوجوانان؛ پایه درآمد و کالای مجازی.
هند
🔸
شِیْرچت: شبکه بومی هند با ۳۵۰ میلیون کاربر ماهانه؛ نسخه محلی برای کاربران غیرانگلیسی‌زبان.
ترکیه
🔹
اکشی سوزلوک: دایره‌المعارف زنده؛ فضایی برای نظر و تجربه کاربران درباره سیاست، فرهنگ و زندگی روزمره.
جهان عرب
🔸
یالا: شبکه صوتی زنده؛ گفت‌وگو درباره سرگرمی، موسیقی و مسائل اجتماعی، محبوب خاورمیانه و شمال آفریقا.
🔹
موفقیت این شبکه‌ها به درک دقیق رفتار، زبان و فرهنگ کاربران محلی بستگی دارد؛ خدماتی که نسخه‌های جهانی نمی‌توانند ارائه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/436253" target="_blank">📅 22:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b447f158d.mp4?token=swq247jKoeyhoa0cDba64g3ykIGEcDzCbYtZJCNSNz6SqxVXoI-ktfpmlfI75zeRkx2t8p7pVrh2BFdkiRF_hB_6x0dg2hCIxSiV9SQvIlaxxWHXyT3_TyM1fF11SgDPgfO_mZ7ygWgX40hXqeF6-QtBAcSPPdodp7HYB4GyvTXRVw1AYOh5iXv9T7W6LHqxqz2peKQAsDu4Yoh3JavwxA-kHe_nZzqpt66Io4mxhGUAFJ5h7qsUdbzF37phy3QlkQ8FJd3b72GgtQZbTThwFdnSZh3Ar3FIJb7uUwvTZYNWFTfGugrlI1i5PbzEP1EOn7yJoUgkaE0HZoaTm1Ocgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b447f158d.mp4?token=swq247jKoeyhoa0cDba64g3ykIGEcDzCbYtZJCNSNz6SqxVXoI-ktfpmlfI75zeRkx2t8p7pVrh2BFdkiRF_hB_6x0dg2hCIxSiV9SQvIlaxxWHXyT3_TyM1fF11SgDPgfO_mZ7ygWgX40hXqeF6-QtBAcSPPdodp7HYB4GyvTXRVw1AYOh5iXv9T7W6LHqxqz2peKQAsDu4Yoh3JavwxA-kHe_nZzqpt66Io4mxhGUAFJ5h7qsUdbzF37phy3QlkQ8FJd3b72GgtQZbTThwFdnSZh3Ar3FIJb7uUwvTZYNWFTfGugrlI1i5PbzEP1EOn7yJoUgkaE0HZoaTm1Ocgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دهلران هرشب برای ایران پرچم‌دارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/436252" target="_blank">📅 22:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7582a2e9d.mp4?token=pm0NWIxENWA4d1_Xn4BYQ2Aw2ntNcokV5BpXQzSGN2Nqm3NwdK7G9CH6NNjBEQ7Ibn1yLjD42H3fG5yRwAgHt-uFT4XYbto1MCOtJsnAd8cLTl1rkUo372pty8AyQH_anGWUPcCqaCtiycWypvKoRtMKfsVBfPDF8k_fCQ5mntaa3lYfZPwdAJlcOdFtwgowbsC-pBqu59w6C_oqQfXGynX09mGbYyFJAyYZ-452TSOYGJEL8DNfsrnlwEpGChH7j4EVA5FJxVGMMP8I7h1SKTltjrzUaUwMgY4mU9KECSo-2KnucmclTQ-0Ld3BtosaJNd7Dj_GRLHjPGxMjdirO7D_UgjLp8I2NkpgMHOefx_JbJiEzQkG613wMz-i9PQlWHSfe19sNQhtePnRlKKqQpsNp4zl0NuB1zyiIyJsQ-e_3LE6IxszBANxEhheBJWgicydouBKwjKmgi8cRSx5vhpME_Nju_5H9A2VlohYz-LVKcI1pcnw-t4usKCBLhBqZn68I_v5QEHGiA-xek1l8HCciOdhN_w5WaNsbemlEEQUMU9dayqQ5azMI7EmxTbfZsBsQCK27c0EqYWZSMgtVA2Hf67m3lm8iyAvtqWOTwYf4S7u06MK1CiIb8_A8QOV_Nj4xWnOWtTnMQu5nXn1MbLOMzK2izWDoXvK4rlyLlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7582a2e9d.mp4?token=pm0NWIxENWA4d1_Xn4BYQ2Aw2ntNcokV5BpXQzSGN2Nqm3NwdK7G9CH6NNjBEQ7Ibn1yLjD42H3fG5yRwAgHt-uFT4XYbto1MCOtJsnAd8cLTl1rkUo372pty8AyQH_anGWUPcCqaCtiycWypvKoRtMKfsVBfPDF8k_fCQ5mntaa3lYfZPwdAJlcOdFtwgowbsC-pBqu59w6C_oqQfXGynX09mGbYyFJAyYZ-452TSOYGJEL8DNfsrnlwEpGChH7j4EVA5FJxVGMMP8I7h1SKTltjrzUaUwMgY4mU9KECSo-2KnucmclTQ-0Ld3BtosaJNd7Dj_GRLHjPGxMjdirO7D_UgjLp8I2NkpgMHOefx_JbJiEzQkG613wMz-i9PQlWHSfe19sNQhtePnRlKKqQpsNp4zl0NuB1zyiIyJsQ-e_3LE6IxszBANxEhheBJWgicydouBKwjKmgi8cRSx5vhpME_Nju_5H9A2VlohYz-LVKcI1pcnw-t4usKCBLhBqZn68I_v5QEHGiA-xek1l8HCciOdhN_w5WaNsbemlEEQUMU9dayqQ5azMI7EmxTbfZsBsQCK27c0EqYWZSMgtVA2Hf67m3lm8iyAvtqWOTwYf4S7u06MK1CiIb8_A8QOV_Nj4xWnOWtTnMQu5nXn1MbLOMzK2izWDoXvK4rlyLlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/436251" target="_blank">📅 22:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سردار رادان: از آغاز جنگ ۶۵۰۰ وطن‌فروش دستگیر شدند
🔸
۵۶۷ نفر از آن‌ها موارد ویژهٔ مرتبط با نفاق، اشرار و گروهک‌های ضدانقلاب بودند.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/436250" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_1qsyjuxOrI3TfW5gStFVVGL9iq9sZtGWc_Jd0O8CjRL3rHoplGVe3P8MKEaCrAu2GfZGpCtfVNxWpWxJKy2XnVMqmIEOe6Is0aI80qpHnG59Q8wiSh57Hw4O31JkNF4suG7yGuTAjN-c0506ddRuavNwSL2YBCzQFQDN1g0F_sd4fsznvbFjYkd95fgQg6YNW9oSErqi3SNzXZQTUY_zBCoTV8E-eifzw4MdvggJcC6q6Vu-V-fvyvoUFZB3wNK7GXuvNn_-y6Zq7SL9QnxzJoptp1q_poTpnCfTZb3iybPIa52cDM4YJ3_C2upPm60PIX3r4cLKJtQmRM2yFz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FM_yKb4DOadW7xdRaMi6daFl6ByLi2XqzTB-lK0XvhqZKONFQVWlhua8VZY7DrQ1S7Af9bHVHMcdiK2c99njX4NDIaksHLFT91TLK-8trs0pAwhU9vObUpNrwSFdoJPQ-37QvylFVdbxw-jdHwagfrRRQqVm0dNCjE5iA8M6GhGih3l4jlkm-Sph_oDP7cVXNy7bQ9IVc2-atGhrsP2lRVOT9rr8Pfwy5_fSm28Mg9wL5WGQC9IhoLqR6KReTu7ougoUyB9zx_NLHGTn6HBcaCUZcKkOibbe1zE3LAym6e06LtOSJyrvdraWEAepdTg_R6dE1f32W5OgbVGEEamGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmtmgKj4oLphWKH76063Kxl1IFTqULriQbcvt3EqSJf3ip3t6loDVZYpBFV2sUgnmvE03-dY0hH1Fox2VGrQ4D8wnGohyBs2Guqs2uytcqATLnY_EmfjtdJ1QQTfT353OWMS4dyQVJ9KYEbiv9_5_OusdfQ1A9MOazDrJjzxnA4zQbn1v_WOHeKXCYEn28hfFTqjdxD4UkI5WuQWzwET9rEDNldQ9yNqGo1lB1MHcv5i3agUKPV4xvcH8944GibaFaoN9bkyTvpP8fJ25Wym7UXTJL0DVRj2AJjXewEJl5MlHDOFe23f3LvTHwSFgJPcKaHhZcmJ-e5WVND2AVIZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHKngJGuGqzZDyCinuEla5vdLQMuxiCy9A51r68zmvifsgEiHqrZFzECK-9rJH32PZVB-M2FIhuikW3Ss2fnAAtoLaz2kwOob3Ph_TwK3tikJd_nhrMg52WjkLF5V9M_Rui_Fc0XylQj6gkQWm9na2mahGkrywFhxTbn3cFRZcehPEcybAkwr9ciiN1IzRVO3-nz3InR_ZGLe7bTd9CZIbpUKIfX6D6ShUfJIUYEbhjh60BpRlPFQvyQpY5Dq1HWRtnPrdsyv1FziT-KWebm5HF3aiJ4YQJ5ziRnp_LYXkRbHnYhnMk10P5wgMWP9wDhl1KBg4AVk5uAvVAJpZjK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWVvkMD7UiKNdN-nPpisviWOzc0VROkuTgdlkBtD_yPJJSdH8LB66B3Xj-88zrHuyyDhr0yAkdBBvLLLlNcgJPzsLktJFBU6QT6koEFIGixuo5Dqr36GAKXnlVWsCntiRdDVLjwzkeiNSNQYUnQYDX5aYBQhKyrWJDHJ8U0mP__cBXiOauNgeW-sMecxvrAvQQN4im5nwhbepkRaI3DAroPt97NsO4kom9XTda72_Mp26WzzhFqS6jhm7dg66Va0Qyr3UdLCHdiItmxB2LXVfa-mwb4rZWJJwBsPATXQvJvK_RpmMnT49znZMOnvuCs_cRRJDM8R4U0GJWpgpo-fbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vo3s29WELyWPFZlukmpiBNfb-VJPeE7O61n4VspLpbu08VpM8uqISx0Bv0YqhibMc6src8DX05F-ggtCvxK7DAb0T7KRFkJjFxfGX8UABNr-qrJDknbicwpH3Xrye78otFGSL5IBi4swvAqrFOYamrLc1y6WUSZc_DRlZK7oAIc7kFeaZiAJn2W3Z3gkTNHgNFic-D_rLPT6uokdes2CW1Z_T9tzbiUQuUPS_DilN38pamURxlAat1BJjIp-Ca-a-y7yI6GQ2cJTtdwr-PpIa-PqIJHXrNZNgiuyk8yHh9etfXRuapwu3ZtIIbJExQpXOqTyCPN5_ySnDE26XCDnRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI1kvr33jCvS_LSVo4d1hRVsnqwLRDRmTPChYg7wzrvfyTw1gxTkwCIsOzaTeVqL7RT9LVQ4c8M_CteSO9ukRspjxFuskB74mUe2U9qwgbrBP8j6UZkPIoDp26Xrqg_7dX9JlY7Or8SrtqdyDauX9RhNoVLeZ5otThOCoLpRHd0ItatQquxO-5M2jKDJc01VID7Ta07Y-9Ecs9x9PfiZJ0o66ijY2Derw0FTk-onIEih-eqpraEGDSovE1C0pd5SK7sydXy3skEHVEsrLJ5HzmXPuhFUopJ9MFTvfH2vHb8v-gqec5a1pc035kgEFI5-mMqoRI3bal7yKnXL8dPXvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سنگر مردم بندرعباس به روایت تصویر
عکس:
عماد یگانه‌دوست
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/436243" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436241">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bad9e4b7.mp4?token=lvWpZDgbpy1PyalRedqCqPalhpsD6HrQ3NpOauOPWQXewtHWbwecVyxBnVIrCfOYiM8dzw-BQSxuOewNiQmhrjwUVkIz3V3pAjJ0U5MVxhPoJn8MBqh-vOakIFOuHD6eAUVUEyHn7USQiKt3ycX3NWhRwmyfBj7GzBdKbe9jL0AV8ijkpuxFBAmadCjFWbDMBRmElqM0E_4L081MJYGmb1DqEqr_56-KD-6FhGihUrCWmmvRUjs-0KIFm-2KVUM6-K1bsxx5Na8PFf04GZWpuOJ97X9kLJ8AaSzNURQXKE8hzaMAjSYymQYSxgd6ubk4jEjrIypcu1HS8J-kneLmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bad9e4b7.mp4?token=lvWpZDgbpy1PyalRedqCqPalhpsD6HrQ3NpOauOPWQXewtHWbwecVyxBnVIrCfOYiM8dzw-BQSxuOewNiQmhrjwUVkIz3V3pAjJ0U5MVxhPoJn8MBqh-vOakIFOuHD6eAUVUEyHn7USQiKt3ycX3NWhRwmyfBj7GzBdKbe9jL0AV8ijkpuxFBAmadCjFWbDMBRmElqM0E_4L081MJYGmb1DqEqr_56-KD-6FhGihUrCWmmvRUjs-0KIFm-2KVUM6-K1bsxx5Na8PFf04GZWpuOJ97X9kLJ8AaSzNURQXKE8hzaMAjSYymQYSxgd6ubk4jEjrIypcu1HS8J-kneLmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تنگهٔ هرمز، کابل‌ هم حکم کشتی‌ را دارد
🔹
رئیس اندیشکدهٔ اقتصاد دانش‌بنیان: در تنگهٔ هرمز طبق حقوق بین‌المللی، ما این حق را داریم که همان تصمیمی که راجع به عبور کشتی‌ها از تنگه گرفتیم، در مورد عبور کابل‌های فیبر نوری نیز بگیریم.
🔹
یعنی شرکت‌های عبوردهنده…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/436241" target="_blank">📅 21:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c115053608.mp4?token=eqnSUw9tdJF-h7dL5hCNDyf0af6FCEnIx6M5cTZ0d7qndbeHJs2elzBMaN2-GlA5EajaO6-8MBcN8Tad0Go3CrzWe-DARjUSGPqi2C5JTUehF4mU6rUG1jrLIs9MQZIFBFhtB1qWjhqqd_q66mA8aDMvwuSjHFIdWskf0dvIt7KvCdrDK5pckbUtrnU3G1QukcZKyVYyIztTsCedK3infz6A_KktKUataXsooDsByrMvHQsDksh_vcviQtHVUO5H97n3s6de5QQwhJhBBPSP4TLv6DCY1fZg5z8PZfDXAD_MHixyOvJIcIZh9HpJ2tssAQO7-RnLXtQaat_pG0dwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c115053608.mp4?token=eqnSUw9tdJF-h7dL5hCNDyf0af6FCEnIx6M5cTZ0d7qndbeHJs2elzBMaN2-GlA5EajaO6-8MBcN8Tad0Go3CrzWe-DARjUSGPqi2C5JTUehF4mU6rUG1jrLIs9MQZIFBFhtB1qWjhqqd_q66mA8aDMvwuSjHFIdWskf0dvIt7KvCdrDK5pckbUtrnU3G1QukcZKyVYyIztTsCedK3infz6A_KktKUataXsooDsByrMvHQsDksh_vcviQtHVUO5H97n3s6de5QQwhJhBBPSP4TLv6DCY1fZg5z8PZfDXAD_MHixyOvJIcIZh9HpJ2tssAQO7-RnLXtQaat_pG0dwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: مردم صبر کنند؛ با بالارفتن تولید، آرامش به بازار خودرو برمی‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436240" target="_blank">📅 21:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3032165313.mp4?token=nc7qpzRD6sAjnA301VCvfa4fgeCvTwD6KDgLG2-wqW3fsD8y6OoKS5fThlTepzEXBFJ0olDebmP_ux4yZqtgTzr6MrbsBNAjXZcJOJHSbhk7F3bM6Nnot3H9m8Y-fkh0kg5u_BV5lfR-K9sV0_JRrH_M-IetIUcqNxHRLHw9vAD_zwHExhLqH6rTmpVYbsF9oEYWUIG8a56lAyCbRS_6XRiksfKLHzmags_8Kd2lbMNRGl1w1v4e0FL0g3QEJDqoQMEqUCSG9gqFumbToLyvgKS6vt70igToxFzmX370Zqsb6LVJrb6RWfwjD5aFc2gM-a0U-LhTD35qhYMCTwxtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3032165313.mp4?token=nc7qpzRD6sAjnA301VCvfa4fgeCvTwD6KDgLG2-wqW3fsD8y6OoKS5fThlTepzEXBFJ0olDebmP_ux4yZqtgTzr6MrbsBNAjXZcJOJHSbhk7F3bM6Nnot3H9m8Y-fkh0kg5u_BV5lfR-K9sV0_JRrH_M-IetIUcqNxHRLHw9vAD_zwHExhLqH6rTmpVYbsF9oEYWUIG8a56lAyCbRS_6XRiksfKLHzmags_8Kd2lbMNRGl1w1v4e0FL0g3QEJDqoQMEqUCSG9gqFumbToLyvgKS6vt70igToxFzmX370Zqsb6LVJrb6RWfwjD5aFc2gM-a0U-LhTD35qhYMCTwxtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌آفرینی گرگانی‌ها در قرار ۷۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/436239" target="_blank">📅 21:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8DvKvuoPIIrfVscBzkIn4Bs3SQ85ANbB7EmRRLtGdWLDQwYoN8Mkdjbd5pD8TlMSDihxaICj1ownr8lkt_Jnh4-872JTXpqJBkJKp1JFKbtXXqEVnDnF7TfCLIjgEUffsJfvBEt6SyrvegvINz2_LI7XyG7eOaxZTdWzV26BEVw2ikrSW-nFuOkY9QFIzLvyIr0INNqg0dbYrp1fiEZl7FeMklsZBluLdX4ENKP7vEmPu313sR2XrzNm0TsNWhPnTKRtwseUmeaI50VQzK4GIRfgn9UIgFAWmBNqayFTJ5aFYSSNDI9W5FFfUcbiEP7Dry6x-FxU0iFHAXZ2Y6k8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ای‌اف‌سی سهمیه باشگاه‌های ایران را افزایش داد
🔹
طبق رنکینگ‌های جدید منتشرشده توسط کنفدراسیون فوتبال آسیا، فوتبال ایران در فصل ۲۰۲۷-۲۰۲۸، در لیگ نخبگان ۳ سهمیه مستقیم و در لیگ قهرمانان سطح۲ آسیا یک سهمیه مستقیم خواهد داشت‌.
🔹
فوتبال ایران در فصل پیش‌رو (۲۰۲۷-۲۰۲۶)، ۲ نماینده در لیگ نخبگان و یک نماینده هم در سطح دو قاره کهن دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/436238" target="_blank">📅 21:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
رژهٔ دهه نودی‌های چنارانی در قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/436237" target="_blank">📅 21:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6z3iIusLUuS-WIpQsvWRbNWiWhLFM0_rz-T1-xTSQMow0bG-uDxuUcrtlpJlVRB0DfWt2vmpINbKFfyijELKGKZnEX3NTRdq2NmvSYjMOVYeYhSTqma1ENbpiAhNARazzbxU2q5Dtrosa0zwxMNtTlSqjpQlC_riT75C4uvbj7DSDuKLW1PytKae4gxlf34tbUVsGHC8Uqprvr7OUMqZ03ifrBV6f0JRwIpiXyHrYcxMxSJQWqvu-axNo-kepdpHyxr90zjDvhgaWbbqsdDHlo694lnSMX3ZYdYIKWgP_ga4q_fDh2EoFJzL25JbZTjTXvsGSgWsS6Zny6itJTJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همای: دعوت رهبر انقلاب به بعثت هنرمندان، فرصتی برای همدلی است
🔹
پرواز همای، خواننده و آهنگساز در گفتگو با فارس: حالا که رهبر عالی قدر و جوان و ادیب سرزمین ما سخن از فردوسی و ادبیات و زبان پارسی بر زبان می‌آورند و برای محافظت از فرهنگ پارسی و تمامیت عرضی سرزمینمان در مقابل متجاوزگران و حتی سرزمین‌های عرب که به مردم ما خیانت کردند تا پای جان ایستاده‌اند وظیفه‌ همه‌ ما هنرمندان حمایت از دیدگاه ارزشمند ایشان است.
🔹
شک ندارم هنرمندان به زودی سکوتشان را خواهند شکست و پیرو دیدگاه هنردوست و ادیبانه‌ رهبر سرزمینمان خواهند بود. این تفکر همان اندیشه‌ایست که سال‌ها هنرمندان در انتظار شنیدنش بودند. حمایت رهبر عزیزمان از هنر و فرهنگ پارسی برایمان ارزشمند و بی‌شک به حمایت هنرمندان از دیدگاه ایشان خواهد انجامید.
🔹
بعثت هنرمندا یعنی هنرمندان و مذهبیان با هم پیوند بخورند و برای خدمت به مردم مبعوث شوند. با این فرمایشات مدیران و هنرمندان با یکدیگر آشتی کنند و برای خدمت به مردم قدم بردارند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436236" target="_blank">📅 21:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436235">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
کفن پوشان پیشوایی جانفدای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/436235" target="_blank">📅 21:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436234">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZC4rfBzbPolocj64kXbluzEBkkGVxd9v0Q3NWEhfHkXwpagAcncw6yURO8dR6oaR3XgANYHAPlv2q8GPWSMqk9G1WZc4rEdwtK8_2kgWjhywgkLojdw39z6_rxXubQFUa-D3WyXf0EbdNuUIIAMyDC7Dbeo8d67udRn75yIqMoqEYRvJFvgrAdpjv55c4nsaIOPtU_5Sl7hGvi7qmBlhuhy08ALYSw8AJMn0HfUWLCLGyCCGN6Mr_KM1SCVOHAonPr9Vtn5kW-zVhgA-OcgDDk2NymMmSfoVGW3NO764pW9kpD7Vpb4227SZ5ueLBI8rDmO0B0uX7BSOmo5V688gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیلی: وقایع دی‌ماه کارِ موساد بود!
🔹
روزنامه عبری وای‌نت در مقاله‌ای به موضوع اغتشاشات دی‌ماه سال گذشته در ایران پرداخته و حقایقی درباره آن را افشا کرده.
🔹
وای‌نت آورده: از زمان شروع ریاست دیوید بارنیا در موساد، عملیات روانی بر افکار عمومی جامعه ایران به بخش مرکزی مقابله با ایران تبدیل شد.
🔹
ژانویه امسال، هزاران ایرانی به خیابان‌ها آمدند؛ پشت این تظاهرات، «کار عظیمی که اسرائیل انجام داده بود» قرار داشت.
🔹
برنامه اولیه اسرائیل این بود که جنگ در ژوئن ۲۰۲۶ آغاز شود، اما پس از شورش‌هایی که موساد در ژانویه سازماندهی کرد، نتانیاهو به ارتش اسرائیل دستور داد زمان عملیات را جلو بیندازند.
🔸
نکته جالب این است که پیش از این افشاگری، با وجود همه شواهدی که اسرائیلی‌بودنِ ماهیت اغتشاشات را آشکار ساخته بود، جریان سلطنت‌طلب و رسانه‌های فارسی‌زبان اصرار داشتند تا نقش اسرائیل در ایجاد و هدایت این شورش را به‌کلی انکار کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436234" target="_blank">📅 21:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436233">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">دسته‌گل جدید مدیران استقلال
؛
قرارداد ۲ میلیون و ۸۰۰ هزار دلاری بازیکنی که به ایران نیامد
🔹
شکایت کارلوس استراندبرگ، مهاجم سوئدی-موزامبیکی از استقلال که به‌دلیل ارسال قرارداد با ایمیل رسمی باشگاه رقم خورده، حاشیه‌های زیادی ایجاد کرده است.
🔹
طبق آخرین اطلاعاتی که به خبرنگار فارس رسیده، رقم مورد توافق استراندبرگ و استقلال بسیار بیشتر از عدد مطرح شده در برخی رسانه‌هاست و این باشگاه مبلغ ۲ میلیون و ۸۰۰ هزار دلار را به‌عنوان دستمزد مهاجم سوئدی برای دو فصل تعیین کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436233" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436232">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: یکبار یکی از دوستان گفت اگر به تهران بروی چکار می‌کنی؟ گفتم پاکبان می‌شوم.  @Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/436232" target="_blank">📅 20:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436231">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
روایت دختر شهید دریادار تنگسیری از پیام «مشت گره‌کرده» پدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/436231" target="_blank">📅 20:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436230">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: مقاومت و تاب‌آوری ایران و حضور مردم مقابل ابرقدرت‌های دنیا کشورهای خارجی را متعجب کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436230" target="_blank">📅 20:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436223">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPDhErKxGXbPG2PBy4ybCMOzv_A1MlR0aNT9l_4omfjim-tczVK222gfh5nyC5Op35loloXMyNZqEl6pmw-U15Vfx6Q4r1Jv7EgVprqbD8ylj0sdzaFAnF6pS-ULMwZyW8XgOkeEP0PSNQ9SQLyz000t8L6KzKYDujWN1VpGJZf7byoLfq3agYv9H2xGJkKtdVZsnLyUw9MpIXV17X3VVfYmKZvAx17plBBH1_uuG2n2OTk8BtHP9KjB4lePNIeBfu1F1lZde4ypMWwnWujA_mVM94I0QMJtTbBkz8TWkjSaapCNR4GlliZYMH5V1A1RNF5iBq5rfxB2DE-bVx4pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVB3VASMm_xnvw0wR6ywScnIwzM-1KLzJq0zLICXvBCnN1SSzQF7085Es737RNwX2O1Bme-Nuu_RZ7cK6Hqs_Zh1x-kFwkoFIIyDWNoXqqMfVVMa7HvO8JTRJJQmz-pRJcPx_dutDmWOls2U-KL2O_HXZduw8cwSq3eCriOFTbJrYk-qGJHe7ae2ZqxHxFT9eOeUxV3IvGnJBXEMUol3CKhmPU82py375OVxayGHQ84Z-ZlEHQZ1BDKj5COCYTVf3CrQ8Y6Xjz4s33KVQMaWmyWWFiQMayfGXpAF5c7EloJvvVahH_nW_QH9_UyrAKjpK3CNlvLhlbJT-PYdHvySHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7lbJbvCbPZSUoxOPpRAhAsloQz9dXN3tfP0h0X3KCqJ6C62_JzgR9yovnOxV_YB81DOcknlHJcNIBwHEHQD7m6o6D-m12wTXSJXEg1WqRc8RS8rWsUjtD4jvcL-r3x0J-TUeH9MLJBD7fVb2jyZKQzotEVYwqRJduWfUBNib2a6gsV7z8ovJcfqaZUaNOSH5rD4a57qt6ayhih5xWRqBsx7xtVUrTjJunemzgGLtXdV4v4CsVQ9kzxnRISGLOOwM5-eSRRjWw1l-27wA32I2GvjOgDHRNOa4eXinTlP1QMlpMDf6Pa4aTbLlVIPPUuN-Ndwuli9ciWukZ23BZU_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkXdQwe5CpGj77VDR6sznix6obOYZD-ZvJlz9xduU-JgTPLO-f67kfHCKkaqIJfG1VrQcvZM_rqtPqUiRyV7pt5ZcdLqEXdtfE-WcDGJRwwgXTRrYtKcZcqzyJGkmnB0asKcw-ry6GmIyVE7YFmqxRC7XBdg35Eb32UZygT1Xe3zplso-xe_VLH5bWSIhi5xqUVOCj0KAeEbe_TMHQzFgTbz0HK_eBdeJ0yOPkiZYCCPROY6qCqoJB8GVyJP4g37dkjaEQMwpUt5xdS_NYwX1KjVkpsU-xJEe77QXb6B-Jb6BNqGJPv8mthETp2sZkZc_lCQDUZ9mWhcRNFLomUtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnVeayMoTFLMYS7bvj_gCdiIIQ6hV81nglKDzA3DhW-dXdg2pYoVhL-GReEtkO6DEYYKpXYs4lIntbTG_A88UBxVpjo9XKNLxZKWySigDIEWcwKeU_ot-NsJIMEwDWbpsDEypiP6iaWG4QqpvE-n62vddoSA7F1YO8IlAwVLGKh52QJ0feMNyDRF09W0Q22SuSdPxnuaKgeHC3mPwl1nYBIbyQx8pYEd0lC9Y2xutmU8j91MJ2dlfkT28oypwgOoI08AnsuHuB3_8TZv3IEUOCgYJdIwQKdnVl-yl4tlFXJ29Z8PRur7014PMGj2o9ZHXYFDaTS0vpO4w3it41MGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7FJ2O8PNVlqfjskkmC4D6p0kndcrCUa1EOf1rilbm1F57gTkogee_g5gUogxIE09kl-D0pqC8hRrXAb58C-MM8aWuJQj4Q8Yc8pvLJ-ejEtF_PLgM0fnVqM2u8A5R4d5py3u92Ba-4p1pFWF74BEFkOGDB5bYcHgLQF_gBZk3JFWXIzHd9D_Stfh_iHUIjTLV5rzqsVgywBKPHE9N2I5U3QL5hgVqXOKBi98eV7xfx9iX2cscABDQkgdiLuR9_1NlznI5b0bK8qcmiIDQAVgaGOPi5U7s1Q_BoXvy2_6VF8rfgqGa4XY4JulxcI97oMZ3R4YJ5ht0lbBmUQOQmDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOHSiVmPRed6ts1GKlGY2u8s4a1tPX3Soe3vTnqX0Ex6eWsF5CffX2rDY-lfL2qYIf9WlYpv1B2dF3KQvXxlHBJoYrNADZkqULlxz9k-82JvcoP4BW6y43iMWqwTeNH0ktBE3fSEdvsdr9mGNcwJooOKkpOzVW5Qo2dCaXu1Bkw9mq9KY8iQ_JeZH8UDBMEFsjuQCIsZqmVViUFghoqjKfN9jUPgJl_zDaUcyeunq8SyLz63SEQZm617Kr1HsAyTXzoykkpEscts28HxogxzbfWPA6DJFhDMQ-LNt7n84wCrmEP6JBW8jxWlZqfXX_xM05pfaLyyQcHDpAo0izxLMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت وزیر شهید دفاع در مصلی حرم حضرت عبدالعظیم(ع
)
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/436223" target="_blank">📅 20:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436222">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مسیر جنوب به شمال تونل توحید امشب مسدود است
🔹
مسیر جنوب به شمال تونل توحید امشب از ساعت ۲۴ تا ۵ صبح روز بعد برای تعمیرات مسدود است.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/436222" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436221">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVp_GKD1QWlFpevud3G5-7dUa3byoHRJ3v7DS0PGXnG099I9OpkgnQSIgOd2BHeRJdSylC1CZcpoxBWq1AXvPerDpC5m15sFvVQoPHT5OtU339pldLeE7hoOqpzzCHNh3JwzvbxxftQHxV8FKaq0rLZjebka5M5f0oF891yk1LhmJi1XzSdPz-ZWwS941ENzx_3h4QdjUpeS7-valEwcfHQqK4A6tx6ztINmB8Ux9wfhb3KpE3zPW2pK3jx0MORfSV4Y96IHGJ9g8ADuvBS4nlv6OoWz3RjUaV62UyEVpc2fmldzhQ9M_hqX6hPr3vOMoYRGDVkPjYzvJYy5F9hsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: تأمین اثاثیه منزل برای آسیب‌دیدگان از جنگ رمضان، به‌جز شهر تهران به‌عهدۀ بنیاد مسکن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/436221" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nApdJlrXRk0TbLBGpFRUzA3aA4D96g_iaDmvPrs2kuVHz_UiMVDgzZeLdbzwwVWPQfbdswMzSFPKGajSgIZwmtMAVGSIQvgmEbjcsFuqDGtc1OEYyV5xlLHivm87mgbr_cE9LqpQZwsxuwzSY5OoMFcLRyZnvKnXhLNx2zR3ADMezZhaOS0br7riyn0_l_3ITRhXUV-CloQ9BRD99frO5O_yQpTftN3SmoDdHheDALmXLsRFJG_RRrjcUhVZwY3M6zSgAhwOIBmN3AUuGl9Ndm5bDpm8srKs9RgIJGEYzoMitBQIzEyi5lg9G9bTUUHc_ivcQW1G7hslzjKxLdRf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkB2XbKrTn08CNgoaE1u7DijbMGybfHXUi4dEKTjBZwq01q300N9MFmmoJ9mDuX3Zs8ij7TiRnKdMTHL7DBDFxLSBCqTtbHgKatylYpG8CbpmVgSmhJEpKWpCIzKzHZPQ1xSjGBHT0eStKo5NIqz4WqsxYcN2IFKmCc8Xc8LWmdFZWfHIVk5gmHiKTXXVTGB0RFJl0uWjL9G0O4C0M_WrIsviFc3zp7qUBTOQBjvsNEqd2xRcXV3gTvyzCzptrO_J-69VYnlynFRPDyFl3h1IrBO8bd212S_eLeFGXrMf3pmpn5BnRiYclM4k7Evu5tr3wqYcJEHuDcVu3Zxnr8p-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXl9r47bWhI3we8tk4E1wvEpinRxCYq_wvzKVkxKu1lIyjpECjx8Hcrl_WmJzOjOluf3WKljosXkoQtbWvOESMeVYznnGylo5Cfx1Shp3Vu11e0OFxnF58-penjZV4FRjKBo0gVfMAorbkWMN3GlezTCaYi9wgG2yIeevffHCEu3tJTwAMQq7IzJOB0Tx9Th2J51mc7vboUDrUJ_NzHeVUtqrBnur-uRyl6PQs4OwNP7BY0HpJ9bvaalkfXOCXtFBlUBz7-tF1KHDRAn-z-sfq8TrkQEPBm5KNi_HUQQP3wFcy6jiRga1tSyFHN3wvgdekG7ijBUh_YB5ufLKner4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuLmZHX9f9O0edXu2SpKMeQRTtdVYwTvvws10oBMeGf_Vi6U9_FyHZwVGfGXMMyxEubxzwRZSDxdnKOUlTGxLTSmyDhzkWKuQy6vGQf3lug1YAD4IQCuaRqo_boF3yCtBVBKbSuJpM6GZ5-5lJbCWZkegicfbJVuExKYDI-XRpLn1t08PaSy9qzay0VI2eZxpGX3doxNQL7rGfLs4vVtajX39AEz-fwOhTexPEEj7vTA70prUiz72uA5xd6QNe8iaqAaoIDA7BxjoE-YYR1MOsU6HSwzawlRDWGlmg_aSvmKkHyeAFf3tQXQdf1FV3FIydOKlC-qVfYS2Wx6SP-b1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWiul3iB71YgTOqEPm0f91GPa4aEgKtwWyAWGfpg7H6smoK5HP7c5ttnQP7YB75Oe8_8vA9D1j1OdtiC7YLmc9G2MHUAFSwFYX4_ax1rEAw8eeRHhAkuydRmmgH9N4Us7co0yDLgGWIxCIOqNE4TWFn6JAz_tf5vf6ynqzBUpuIdJFtvoO_XZmQUjlB-k70q_RPbfegoAQTUNCIVfHyQ74H0kb9748OVHyfLmUEsnjrxh0rr9Ia4c1kXBCK-uYekfuTB0WcC_E29UITNlMo0-imdvLA2pzQeALnLRgx3bKJBS5HjfqMBCuC2nJE6YoyLmVlg8mjtPoekVoxAs5Lo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkfH4Y036ju8yIwAS3FsCzaQmluSb1F5hdhJzvfpISbwfPbBr_gW6kkzae4UKa0PUWHqcVQmeZCXFr4o9ILi_tSxpeuV2G6qEfCRX8az73m5XKvNX_RET5sYyVrtm-4oFQsKqP5bGdx_RqPHeeQgarlkfI7ErTzbWnjCPre0UVfsowSJImNbobnGb7AjO9StEwu1pTXOC-hKypmgRbZHAhQOhboX09BRPZq2NDXD3mtYVitfU21BN4F5fVukJv4EhGg1UttO9hN-ahr1xKW6Qz0vUFzVB9ZR4ILAAmqRjPaHcLeu2f1N541Olw1TH_-AVZgBI0unGpL8u-9lCEQcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1BhZW_EraM30Waulprr90ujrFPjskWl2-t7SLmBIq0kfdM4MUDurHfjyh0qLrZQEKLrl-vMQi1jyqWmsdjPpt2OSx9V68jFb3vQM40VLVWs5DsEaIFtwbate0ZiFz24q3QIvqnBON7Pwy9oTGh9jH0RV7q82t42ZstMBH1pLc_agNNHkhbCtbjXWakMd77JoahXXVmAHqwQ4t_kkug-C25LN8xDXGm9gwDq3P_OD2M9f5Og2wlYhedcrEx3fqHe4iYvGwYgS_-xEuiTd0vGjFOv242ay0J3uUzADHVtKmHuidzgsg89EHg_6dnwRYOmkVKPBsYXOZkjHK4huvcJmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
وزیر کشور پاکستان در دیدار با پزشکیان: شرایط اخیر به‌خوبی نشان داد که در بزنگاه‌های حساس، دوست و دشمن واقعی چگونه شناخته می‌شوند
🔸
این موضوع می‌تواند مبنایی مهم برای تصمیم‌گیری‌های راهبردی آینده باشد.
🔸
ایران و پاکستان همواره روابطی نزدیک و برادرانه داشته‌اند…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436214" target="_blank">📅 20:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007cdcfef9.mp4?token=XZJ1TqR1gd2F7w9aQeL2eLK9EOcfBrjq6P5IanKBJLqrt11ydUIn6xF_7ZJwjhMROr0z3JwXRyMpidMurTK-MPBHzI_P1cQKth0KRUssASy2XR4WZMpK9AuiXdnuVjaFqPwhHTrj64su6g4TPZjdS0JGkFE7cSUATJo9YWxunT7u6VVQEol6Z06JjziI9hW14a-b0eY5ooesnW3yx4DYmdX-Lt-cIOYUxSxqLNbd7lzXI36RJndjfk9NhRo6wEhPudhAtmvIsn4a7E7X2Yj2CRhZrvd7iZd2-emUnoMsbjMzuczcKk__wlK4KMqbnLV07AwIETrA4h9XNd7wf2upnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007cdcfef9.mp4?token=XZJ1TqR1gd2F7w9aQeL2eLK9EOcfBrjq6P5IanKBJLqrt11ydUIn6xF_7ZJwjhMROr0z3JwXRyMpidMurTK-MPBHzI_P1cQKth0KRUssASy2XR4WZMpK9AuiXdnuVjaFqPwhHTrj64su6g4TPZjdS0JGkFE7cSUATJo9YWxunT7u6VVQEol6Z06JjziI9hW14a-b0eY5ooesnW3yx4DYmdX-Lt-cIOYUxSxqLNbd7lzXI36RJndjfk9NhRo6wEhPudhAtmvIsn4a7E7X2Yj2CRhZrvd7iZd2-emUnoMsbjMzuczcKk__wlK4KMqbnLV07AwIETrA4h9XNd7wf2upnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: گمان نمی‌کردم قدرت موشکی ایران این‌قدر بالا باشد
🔹
باید پدیدۀ شهرهای موشکی را به‌عنوان امکانات درجه اول درنظر بگیریم. ما باید در کشور شهرهایی داشته باشیم که تمام امکانات حکومتی در آن پیش‌بینی شود که در صورت حمله به امکانات‌مان گزینه داشته باشیم.…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/436213" target="_blank">📅 20:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-38.pdf</div>
  <div class="tg-doc-extra">8.1 MB</div>
</div>
<a href="https://t.me/farsna/436212" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-37.pdf</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/436212" target="_blank">📅 20:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct0DETgeTozJHLV_Z6_wtZwBE-EcA67OYRKcmS6SYCXkyV99PRbExSd5I57IUncyzjoxHjfafqbAtDyNlt05abws9b6sr540SHsXKIGV4e50tzEUgs7oIqbNESH2rVIdufi48NEYOF-32UJ10cK1rplWAFBCZZPJVEMvehljC3h0a6SWNzs_ITvDqiGgKJjtE7MlSPE2Y1H5kREv3_q9vI2IgJMIIIeh_b291h7vRFZDeJc2SibPcxF0ohaLX_ONwEZPG7LWFjdsiSrSTbeg8HSc-rPyYgj-y2XFVYrauganCJVJS8sDGoum727CFRlPtu5iTpDImaeT-r44lhUSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/436211" target="_blank">📅 20:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">علی پروین در بیمارستان بستری شد
🔹
علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.
🔹
پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده از بیمارستان مرخص می‌شود.
🔹
پروین چندی پیش هم به دلیل مشابه در بیمارستان بستری شد اما پیگیری‌ها نشان می‌دهد که خوشبختانه شرایط جسمانی او پایدار است و مشکل خاصی وجود ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436210" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9hvJhPak3GpOnNgkdn-OmwuTWxUokyXEFEfFPZcpOr1HlxI-iMLhcMsMAZU1kEQ5Gy_VFF9qYrlm4wJJc0HQrANU7gT8Uw7W9karfOwcI1AoaaBzTTMFNWao0JRHHLDx8x3c2vyv5k2WRDWDKNGyXT3TlFGnJI6ERksw-No6f0pzo3KbmMD9P4mBY9IZYtYCZk0bZ3H26swqP4JP2wgWaRvadshqeLio1oPQNlEGp3Yipm5PEvZXtKp10ySuJgaZZF46epS7_fm27f2tvE4EvAfPRMz55-g2wt15JUX1CxvubUBgAbAR7mkvCVwWreTipw-clqUMBFZ7VHf7o_0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قدرت تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436209" target="_blank">📅 19:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddccd8a31.mp4?token=g49PQoTBeg6-6Fbm9elIE7r87fnH74vuMkbquCzRKZV-QfjT4kI3mHg2k-M_Da-bOALfhUUfn4b_r4xWsba0kAaOk2oevniPipnINkbCQ6j-gVF_Z-GRpVJQk5pJMP5rswnir0XlnVVnbqx1ZWk_DALj9OIShgVjIND1563O4-paYU7DV78oEOqS82N2cMfJC-Xlu_XG0TAdXTWiO--ZItQfsqQJOX57Let9xySv1RWximP1-_Xx23IPvKebGQDoues-IpjHJOeDccGc005S0e6cMkcq1HlA8uLg-9QUGv1Ms1guMQ0_eA95Q19Sl2cgbZatB6rfVFjkRRLNa1mxJArRZuUvTxmM3mTERoqAnK7p9DM7gOQReVRqOn8-pwU43IrFocFkikZOrdypO_MYx9bLwz-6d-7XF2QkL5Fm1uKvUKU87rvqasry3igr0gI5h8g3iKpqa0Z3ys7mxOkX90zckaFRZb444PL3mpAN7ebW3-TxYpCwiC7GEZXWQHVH03o4whK8_rUA3Whb7-tJFDSVZeZYA8Q7Mjctx8Mr4suGoZYti4MVHutLttc9cDIZ_xNNGIiFOFX0dWfec-V5IU0JEvLqGfxJ0TJ20wiKzcTM9DGAV-2cb2q28niyxGw9OLZh4nJD1LWzMq2S85ptZDrgSxSbOC5vHzTqb3wp4QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddccd8a31.mp4?token=g49PQoTBeg6-6Fbm9elIE7r87fnH74vuMkbquCzRKZV-QfjT4kI3mHg2k-M_Da-bOALfhUUfn4b_r4xWsba0kAaOk2oevniPipnINkbCQ6j-gVF_Z-GRpVJQk5pJMP5rswnir0XlnVVnbqx1ZWk_DALj9OIShgVjIND1563O4-paYU7DV78oEOqS82N2cMfJC-Xlu_XG0TAdXTWiO--ZItQfsqQJOX57Let9xySv1RWximP1-_Xx23IPvKebGQDoues-IpjHJOeDccGc005S0e6cMkcq1HlA8uLg-9QUGv1Ms1guMQ0_eA95Q19Sl2cgbZatB6rfVFjkRRLNa1mxJArRZuUvTxmM3mTERoqAnK7p9DM7gOQReVRqOn8-pwU43IrFocFkikZOrdypO_MYx9bLwz-6d-7XF2QkL5Fm1uKvUKU87rvqasry3igr0gI5h8g3iKpqa0Z3ys7mxOkX90zckaFRZb444PL3mpAN7ebW3-TxYpCwiC7GEZXWQHVH03o4whK8_rUA3Whb7-tJFDSVZeZYA8Q7Mjctx8Mr4suGoZYti4MVHutLttc9cDIZ_xNNGIiFOFX0dWfec-V5IU0JEvLqGfxJ0TJ20wiKzcTM9DGAV-2cb2q28niyxGw9OLZh4nJD1LWzMq2S85ptZDrgSxSbOC5vHzTqb3wp4QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج ۵ کشور کلیدی از یوروویژن در اعتراض به کشتار غزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/436208" target="_blank">📅 19:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aundPuhn7gcpdPQn41dEmdalTtYAki_DcH7j3xBjAmvfc5VwWn4u9YXowghbO19lUuh6occYXBixf3XeshP3ubOfytvrRyPsd3NH0yHKRGFn0mygEswuEO9uKpIA6Vp0yBJKMVi3K1tnij9v4TdDDoZ_slneIvGd9sAUScRvPXljzck3658z2I5PZ3H5v6uOVBoQrXNGAqsiuys5iGCYD4hswe17ZM3uTGNLy_0KcE_8jCDEukDsgbk_DlzqKScHQVzjzyOOpvWBEow5feIEzBBRaRORCNTWn9dRpi119KB1xNg1nVAYRcsHwGXEhgwLwi8PL3hHxZhXfuy9DsBfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور ضدایرانی: هرچه بیشتر تنگه هرمز بسته بماند، ایران قوی‌تر می‌شود
🔹
گراهام در مصاحبه با ان‌بی‌سی ادعاهای خود علیه ایران را تکرار کرد و خواستار حملات سنگین‌تر به ایران شد.
🔹
وی با اشاره به بسته بودن تنگه هرمز گفت: «من فکر می‌کنم وضع موجود به همه ما آسیب می‌زند. هرچه قدر تنگه هرمز بیشتر بسته بماند، هرچقدر ما بیشتر تلاش می‌کنیم به توافقی برسیم که هرگز حاصل نمی‌شود، ایران قوی‌تر می‌شود.»
🔹
سناتور ضدایرانی با اشاره به نگرانی‌ها درباره شکست هم‌حزبی‌هایش در انتخابات میان‌دوره‌ای به خاطر جنگ ایران گفت: «ارزشش را دارد که شغلم را از دست بدهم. اگر مجبور باشم شغلم را برای اطمینان از اینکه ایران هرگز سلاح هسته‌ای نخواهد داشت، از دست بدهم، این کار را می‌کنم.»
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/436206" target="_blank">📅 19:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8410dfd5.mp4?token=DP584kEl2FYdnRp8zgHJfpDaGRm3fotuT4TVjO6ihAcM-CMfJ8JSw2A6Hwm1VZhKX2JlHNnQC5Vfh4-kV-DAwcebD6vusCMPUFZ-hUqVk-0f3b6bdVUpaFDnynd6GbHD8ByduPpug2fm6DLGJwL2zWwqs9pMB5gaXMuscpRgWnq2Luwkr3X4zHdzLKfW58pkIl4FMtm6ycojZbVya91974TvKG4GZDXLQ7-EGPdKZKCqnkNRtPtgHnlFhdh_NyCH2x39hDfpEPhRtq75MdpWuFL920O6Spz2RFrBgpzub6FH8eykkyGAHncHSjx7wEh74-p9umF-csXkr4rOugAMES7kkmRZMfWqay8PDO2DKrt-6p7qIvw1FUln4_J3MaNLflzMzRFJgbDggxZNJRfAMqqa8GX5dDKYxoicC49ZwtsZMVW_zBSBwlL8PY2IL75qOiYdkYvpiszMCZKkdx5A_M_4zcgpv5JWu99yBWgfRP1i8YmcfHhG6UXI4eyLlCzwa_zdbE5iyZGdQZnvYC4OKU9isiJsQXFSv2Uby6CFHNPhxcaw1XF8hijKFnOR-R8XL2Y8zFfKlGJviglq7J8xxuH7Y89s8jdM1-DktPgbhAepXUo06dar6PHBoAMsEURHU8kTMu71Hbfy4RtQAV6oV3_I8sRyk6jiKXE0Fw_XE3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8410dfd5.mp4?token=DP584kEl2FYdnRp8zgHJfpDaGRm3fotuT4TVjO6ihAcM-CMfJ8JSw2A6Hwm1VZhKX2JlHNnQC5Vfh4-kV-DAwcebD6vusCMPUFZ-hUqVk-0f3b6bdVUpaFDnynd6GbHD8ByduPpug2fm6DLGJwL2zWwqs9pMB5gaXMuscpRgWnq2Luwkr3X4zHdzLKfW58pkIl4FMtm6ycojZbVya91974TvKG4GZDXLQ7-EGPdKZKCqnkNRtPtgHnlFhdh_NyCH2x39hDfpEPhRtq75MdpWuFL920O6Spz2RFrBgpzub6FH8eykkyGAHncHSjx7wEh74-p9umF-csXkr4rOugAMES7kkmRZMfWqay8PDO2DKrt-6p7qIvw1FUln4_J3MaNLflzMzRFJgbDggxZNJRfAMqqa8GX5dDKYxoicC49ZwtsZMVW_zBSBwlL8PY2IL75qOiYdkYvpiszMCZKkdx5A_M_4zcgpv5JWu99yBWgfRP1i8YmcfHhG6UXI4eyLlCzwa_zdbE5iyZGdQZnvYC4OKU9isiJsQXFSv2Uby6CFHNPhxcaw1XF8hijKFnOR-R8XL2Y8zFfKlGJviglq7J8xxuH7Y89s8jdM1-DktPgbhAepXUo06dar6PHBoAMsEURHU8kTMu71Hbfy4RtQAV6oV3_I8sRyk6jiKXE0Fw_XE3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت امدادگران از ۸ اصابت در مجاورت پایگاه امدادی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436205" target="_blank">📅 19:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec43abb129.mp4?token=C-8oPc9vpGFm8nfe0vXnWKBGn1A1YyM5jXbP-BlHRq1xCk_b9yet9Ehd362bpxALSWhnseHddXIkMno1QELoZ4cMYSiNJLvJ0b-ubuXf55jbZRYsffo629dSY84OBC8fx0wqWf5I_PWHWRZYyA9T3QwcJjXqsm3hLaeP34vSlG0e3b2ROzD3RXItwGf0PKcVMkZLEvwruiSzxzZQRf6R_IH5BpUUfljrI0vRWx7mo1W04ci5nOTwTInWNAcjlrnssX00tFjNV0MD7a-Ni4B9Thrsc65lhaVcZUa-btO95tKVghd6hEAT1Z__e3cRYr7hO6S_8OrLBBaP4N0S1jzsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec43abb129.mp4?token=C-8oPc9vpGFm8nfe0vXnWKBGn1A1YyM5jXbP-BlHRq1xCk_b9yet9Ehd362bpxALSWhnseHddXIkMno1QELoZ4cMYSiNJLvJ0b-ubuXf55jbZRYsffo629dSY84OBC8fx0wqWf5I_PWHWRZYyA9T3QwcJjXqsm3hLaeP34vSlG0e3b2ROzD3RXItwGf0PKcVMkZLEvwruiSzxzZQRf6R_IH5BpUUfljrI0vRWx7mo1W04ci5nOTwTInWNAcjlrnssX00tFjNV0MD7a-Ni4B9Thrsc65lhaVcZUa-btO95tKVghd6hEAT1Z__e3cRYr7hO6S_8OrLBBaP4N0S1jzsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار بازنشستهٔ ارتش ترکیه: ایران عزت جهان اسلام و آبروی منطقهٔ ما شده
🔹
ارتورک
: من یک اسلام‌گرا نیستم اما باید گفت که ایران با ایستادگی خود مایهٔ عزت جهان اسلام و آبروی منطقه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436204" target="_blank">📅 19:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436202">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
طنینِ حماسی، لاله‌های میناب در نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436202" target="_blank">📅 19:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436201">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR76eGORUfb8SHbhivqRkaly4ojAQcNSNMUD0zNiBeSJLHOMWxBtm9TqSSnL3MPzN3FLQwroHxMfIjKFLj-Ycb9TGkqJO9L0YImj_l-ooQD9TRKozPUbbD1f1H7n66nKge5zcLi5IJ9T_L53-ZsWcqlwci9CcGRabipRHoPYImQfVMW68iy3yBeLoIpbj9RFh_PsC4FgzaUveci8iVq86Aihj45WK0xewZ5rNKTXi80YbNwrk2P1AMv3NFclOlOJH92qwB3YULcpChdkmxtg-iN0Ia-vjR78AN5FmEok8sqrGwJJj5OT_vEvx-Xzhz2pijfkAut2ZupSCBmvrex08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ عملیات حزب‌الله علیه صهیونیست‌ها از صبح امروز
🔹
حزب‌الله: مجاهدان مقاومت در یک عملیات تلاش دشمن برای پیشروی به سمت منطقه صافیتا در شهرک یحمر الشقیف را رصد کرده و در مسیر حرکت نظامیان صهیونیست مین ضدنفری را منفجر کردند که موجب کشته و زخمی شدن آنها شد.
🔹
سه حمله کوادکوپتری هم آشیانه توپخانه ارتش اسرائیل در العدیسه، یک خودروی نظامی و یک تجمع نظامیان صهیونیست در شهرک البیاضه را هدف قرار داد.
🔹
محل تجمع نظامیان صهیونیست و خودروهای آنها در شهرک رشاف نیز امروز با چندین فروند راکت مورد هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/436201" target="_blank">📅 19:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436200">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bccb5391a.mp4?token=ZALjl8nf1NksqBm6WhCFzdgnl2lxIIqBV4iH92vyLvhkPNrmQeXR8M33Bc43MHZ4AIf-9ouFSHBlmN3FQEIH6iwoBUSLIT9VM4RFEC3Qi5tqUcH58gJuLhHwIOKZQsiFbTQP1hZIJ2IL0O36nBGkIc6r8nBWOy_0xo_tdC8hhHa7vmApAJOsvBWcehodavAQOn08cbqqNiYgAMknvQmhzjFgQ7IfdPUoRKytKGmzjHxL_xHS3XPonudu-nPOWbZY7sQiCf5SsPADU5-aQHw-jTt0Sg4jzLP4zv97gI0BII563HvinEtoaaOWyfMj1j6MUBJOgtUTpesCMvKF3jQMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bccb5391a.mp4?token=ZALjl8nf1NksqBm6WhCFzdgnl2lxIIqBV4iH92vyLvhkPNrmQeXR8M33Bc43MHZ4AIf-9ouFSHBlmN3FQEIH6iwoBUSLIT9VM4RFEC3Qi5tqUcH58gJuLhHwIOKZQsiFbTQP1hZIJ2IL0O36nBGkIc6r8nBWOy_0xo_tdC8hhHa7vmApAJOsvBWcehodavAQOn08cbqqNiYgAMknvQmhzjFgQ7IfdPUoRKytKGmzjHxL_xHS3XPonudu-nPOWbZY7sQiCf5SsPADU5-aQHw-jTt0Sg4jzLP4zv97gI0BII563HvinEtoaaOWyfMj1j6MUBJOgtUTpesCMvKF3jQMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: ایران چریک نیست، مدافع است
🔹
آمریکا در جنگ به اهدافش نرسید، بازهم حمله کند نتیجه‌ای نمی‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436200" target="_blank">📅 19:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5650da56.mp4?token=RQJtEDw0zJGAP9w4pZSqh7OciPEJcbnIltJwKWF68AVaHt6ZIUVTpHZqo6_23mcI6GBN0FD8zUCtFqRaSslvKKvVtO6F8JA_JWd_U2x8i4v_MSSfWDpRkxtCGtc0Hhj4SqKonYACVv8FJ5l0gtvZWnX6b4gosH9oBKe0JFko7zHdWVUMTkITOnaxJZ41Q9ZgL596VFbGqM2Oyn0S7HWSeWMXE9jaUCjmoYuqJr3KSEu-29SY6hNMMacfklzwkI4vZx71apAuNToo7oVY4756YxXFdp4wI8P9qzlWF57Xm55AWxUDZrQkyq2XrNBXaS5o53HTaMKp2HEBxh4p9PaM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5650da56.mp4?token=RQJtEDw0zJGAP9w4pZSqh7OciPEJcbnIltJwKWF68AVaHt6ZIUVTpHZqo6_23mcI6GBN0FD8zUCtFqRaSslvKKvVtO6F8JA_JWd_U2x8i4v_MSSfWDpRkxtCGtc0Hhj4SqKonYACVv8FJ5l0gtvZWnX6b4gosH9oBKe0JFko7zHdWVUMTkITOnaxJZ41Q9ZgL596VFbGqM2Oyn0S7HWSeWMXE9jaUCjmoYuqJr3KSEu-29SY6hNMMacfklzwkI4vZx71apAuNToo7oVY4756YxXFdp4wI8P9qzlWF57Xm55AWxUDZrQkyq2XrNBXaS5o53HTaMKp2HEBxh4p9PaM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: الان کشورهای جنوب خلیج فارس در برابر آمریکا موضع بردگی دارند.  @Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/436199" target="_blank">📅 19:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ بازگشایی بورس از سه‌شنبه
🔹
معاون سازمان بورس: مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد. @Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/436198" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22707d6d68.mp4?token=E-z-m95y_FknHfhTUD--DbaIoIeQ9lfWCpGIAmLoZxb0u_vsQV0mLOZeh1EbTP6pHdLWMp_4cLPDaFd04Nc5hB-E_QZkAeHSAerNMZenh6JfmSqaOrmuDPg7K0vDMD3xnN3s6hiXPxc19SIbOENyryGPWkk-M2j_hvafR1dADU4XjM4hY2TSh1k2pMIcS6fmT13KYKlnfDyC8KNyCbOZ92MtktkTA5LyJPBVAzEy8d2vY-kXXrpj_lQcuM5pO5VPEIt3L_zqPrigIUIjghn2VXwO1lWGb2MBFE_y2Uzzes1SGTmoFiiYn68NGCCHt1_paoqJ55O7CEaZyEFiDxSfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22707d6d68.mp4?token=E-z-m95y_FknHfhTUD--DbaIoIeQ9lfWCpGIAmLoZxb0u_vsQV0mLOZeh1EbTP6pHdLWMp_4cLPDaFd04Nc5hB-E_QZkAeHSAerNMZenh6JfmSqaOrmuDPg7K0vDMD3xnN3s6hiXPxc19SIbOENyryGPWkk-M2j_hvafR1dADU4XjM4hY2TSh1k2pMIcS6fmT13KYKlnfDyC8KNyCbOZ92MtktkTA5LyJPBVAzEy8d2vY-kXXrpj_lQcuM5pO5VPEIt3L_zqPrigIUIjghn2VXwO1lWGb2MBFE_y2Uzzes1SGTmoFiiYn68NGCCHt1_paoqJ55O7CEaZyEFiDxSfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: آمریکایی‌ها ما را بردۀ خودشان می‌بینند و این موضع هیچ‌وقت تغییر نکرده است
🔹
اوباما این نگاه را با ادبیات ملایم پنهان می‌کرد اما ترامپ این موضوع را ثابت کرد.
🔹
به‌‌طورکلی تفاوتی بین نگاه اوباما و ترامپ نیست؛ ترامپ این موضوع را با لمپنی بیان می‌کند…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/436197" target="_blank">📅 18:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad20418791.mp4?token=qH-xRmIYTFPs8QknbDUS6YbJV_rOKO5HCDgjo8xAKUnvQoKbFxbXgyBq-TKS3gzGOC9APt6ydqsJx2BFin3TZ4Ua6nx2cP_5gxLYTv_gpWCCirbZ6vXiJmn1Easl8DWFE3aFbBK0ixRa8p-0Hf4mMuy5ESIF6K2BA7Ey0WT0p0vxHeGjCY37nr7lyz7jF01bTrdlQCTAARna10ZOpmyKw14zGI1gUKW2Szxqzk6W-o6rNdYb3uWJDqaCvyd_cyC9wWR1ZniOth60lEIGAe1W7U1lGcz6WcGwMfHO72MrFWM8G1YbEiilA1gKJjKBYeKrkvZM09fTX2Y_kqNA1-7dAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad20418791.mp4?token=qH-xRmIYTFPs8QknbDUS6YbJV_rOKO5HCDgjo8xAKUnvQoKbFxbXgyBq-TKS3gzGOC9APt6ydqsJx2BFin3TZ4Ua6nx2cP_5gxLYTv_gpWCCirbZ6vXiJmn1Easl8DWFE3aFbBK0ixRa8p-0Hf4mMuy5ESIF6K2BA7Ey0WT0p0vxHeGjCY37nr7lyz7jF01bTrdlQCTAARna10ZOpmyKw14zGI1gUKW2Szxqzk6W-o6rNdYb3uWJDqaCvyd_cyC9wWR1ZniOth60lEIGAe1W7U1lGcz6WcGwMfHO72MrFWM8G1YbEiilA1gKJjKBYeKrkvZM09fTX2Y_kqNA1-7dAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: اگر دشمن درپی دیکته‌کردن شرایطش باشد طبیعی است که مذاکره را نپذیریم
🔹
هیچ‌کس این را نمی‌پذیرد مگر افرادی که ضعیف و ناتوان باشند. @Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/436196" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4b17bc31.mp4?token=LXxkQIOyJ2ze6fUy5yG1ErozW4S-mdsCTGM9qkYTVLQvKGMhwRRgxNWXDGhTlIJ6ZhRvJqv5VoklhaPwAKUMN_g5qj-F-pbwH3RrJK1D9QsWOi7w76WqhOKSjmhq8_kqLWmmk9LOmq5sZW0yhw_oknL1DPIFW1hpm_SgZ55fXAcaLwFlhFcRSB0h77_0RHRuG0B9AP7SI_03gp0WFQiWVhgnTkb-f7D-UVYHOqvOk_nQOZLCNQuPkc3_KJmhLQic3NGKY-UdEwkkIpnoapYqRU2Exwk0oETRNS--jyz40JlPbuNxrVuxnTy11q7CzkKte8SRAWNhf9knjCykmzDw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4b17bc31.mp4?token=LXxkQIOyJ2ze6fUy5yG1ErozW4S-mdsCTGM9qkYTVLQvKGMhwRRgxNWXDGhTlIJ6ZhRvJqv5VoklhaPwAKUMN_g5qj-F-pbwH3RrJK1D9QsWOi7w76WqhOKSjmhq8_kqLWmmk9LOmq5sZW0yhw_oknL1DPIFW1hpm_SgZ55fXAcaLwFlhFcRSB0h77_0RHRuG0B9AP7SI_03gp0WFQiWVhgnTkb-f7D-UVYHOqvOk_nQOZLCNQuPkc3_KJmhLQic3NGKY-UdEwkkIpnoapYqRU2Exwk0oETRNS--jyz40JlPbuNxrVuxnTy11q7CzkKte8SRAWNhf9knjCykmzDw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حرم کریمهٔ اهل‌بیت میزبان دسته‌های عزاداری شهادت امام جواد(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436195" target="_blank">📅 18:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5fe32273.mp4?token=Ob-K7P3IDXGkHs7X-_-Y5EesOS0SyEo6nNJUgV2xE7osiJnvoeTCd_NQfGXfhYJkWMQu1tFKdd1-hd5kMZysiRz1LHOKJV6Tk1toBAZVIDX6f9vX4jFS_RhLtJlEwhuNc3BfkodyqHONK_yteU2-QkXDBFvU1oZQcyQUFKqt3eAVI5rdbVeeX43gBHYYecKBM-A36bC9ioPhADa2Nv-JC93PEiACvGoX7u022lsiOm8_NrbNSYkj6GTEBtlY5taDMcs8IZxfkG-O5sjRk7HoHUgpdx9qbwUIv0CW5mbHiAkDa_aEkriH7QwaeZH3fPpILvCVk_BCJcZCQ5Sasg6DYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5fe32273.mp4?token=Ob-K7P3IDXGkHs7X-_-Y5EesOS0SyEo6nNJUgV2xE7osiJnvoeTCd_NQfGXfhYJkWMQu1tFKdd1-hd5kMZysiRz1LHOKJV6Tk1toBAZVIDX6f9vX4jFS_RhLtJlEwhuNc3BfkodyqHONK_yteU2-QkXDBFvU1oZQcyQUFKqt3eAVI5rdbVeeX43gBHYYecKBM-A36bC9ioPhADa2Nv-JC93PEiACvGoX7u022lsiOm8_NrbNSYkj6GTEBtlY5taDMcs8IZxfkG-O5sjRk7HoHUgpdx9qbwUIv0CW5mbHiAkDa_aEkriH7QwaeZH3fPpILvCVk_BCJcZCQ5Sasg6DYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
فنجان دوم اسپرسو با مهاجرانی  گفت‌و‌گو با عطاءالله مهاجرانی را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436194" target="_blank">📅 18:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvicauhH-VMY5adJG6Rc-XspOeyGWCf7vpc3-N0vryeQFewgaif2RZLndESr3Zpg4HKef0MQTlMX4yUiZqs9M347Ho7SZVYmlKh7PhBgRBi1zBstCdrMXjmpN7x9xtN87O4GW34DruZadbgzJowXlPzMN3eeoDW41jU4Oh7MFmvroqZLI5J10MX3QM3EXauh0F_dV3bicLAkFRPhvmzmBCI9SMk0QGXscHF-6pTlSLIrufysLE9ClXsoExwRuMSbVqm14Sahz2fqePSHx1kTAO_ZuKbNJfQyGdP1sJrrygSBdZbRFKVtDD2sblGY5stMeH6dQAuDJTlooKTbd9VUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
فنجان دوم اسپرسو با مهاجرانی
گفت‌و‌گو با عطاءالله مهاجرانی را هم‌اکنون در
سایت
،
ایتا
،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/436193" target="_blank">📅 18:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/436192" target="_blank">📅 18:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
پیکر شهید عزالدین الحداد، فرمانده گردان‌های القسام در غزه تشییع شد
🔹
شهید الحداد دیروز به‌همراه همسر و دخترش توسط رژیم صهیونیستی به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/436191" target="_blank">📅 18:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb58f7967.mp4?token=S1g4f3zvd6lYGqBfXtCHx-hpC2w0TFEEkC1xAAjNWWPEqslZEH-f0MZBcG5BjnijbbuZkva-YPGFdEWT-_L-zKizB8TVrp1SEQ4J2lSRF6pIoJEPo88dmQHRkThHeB1xLn-uTPk87DiddPV8u0DHutDeWcbxVZLaKf52wcwNA0o2jn8TjNgGt_XBQUpJFUD_NO15BHPUryAZQYInTS4GNCe8k9R4nh8INCFmZ1TWgTDdC5_YsvrSVy1-YtqyKckS_ORSKnE-mUQB9A8JWOWy4zIBAoHnHe4DqxhxFngCGNfEzLFCNNxs8r_qi_tO4L1YOc9hJE4CUqzigc9xxS-9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb58f7967.mp4?token=S1g4f3zvd6lYGqBfXtCHx-hpC2w0TFEEkC1xAAjNWWPEqslZEH-f0MZBcG5BjnijbbuZkva-YPGFdEWT-_L-zKizB8TVrp1SEQ4J2lSRF6pIoJEPo88dmQHRkThHeB1xLn-uTPk87DiddPV8u0DHutDeWcbxVZLaKf52wcwNA0o2jn8TjNgGt_XBQUpJFUD_NO15BHPUryAZQYInTS4GNCe8k9R4nh8INCFmZ1TWgTDdC5_YsvrSVy1-YtqyKckS_ORSKnE-mUQB9A8JWOWy4zIBAoHnHe4DqxhxFngCGNfEzLFCNNxs8r_qi_tO4L1YOc9hJE4CUqzigc9xxS-9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: موج گرایش به اهل‌بیت(ع) از زمان امام جواد(ع) گسترش بیشتری پیدا کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436190" target="_blank">📅 17:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
قالیباف در دیدار وزیر کشور پاکستان: برخی دولت‌های منطقه تصور می‌کردند حضور آمریکا برای آنها امنیت‌آور است اما حوادث اخیر نشان داد که این حضور نه‌تنها امنیت‌زا نیست بلکه زمینۀ ناامنی را هم فراهم می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/436189" target="_blank">📅 17:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📷
وزیر کشور پاکستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436188" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3564b1a7a8.mp4?token=C0jf3hn2oPEzQ4JXDha2p5pFvUKgkG39b6pnMHj1chR8LcTGSqyJwH2xTGy6b5pupXikdxccHfFfTE1kyrEC4Naf8uLTUQLQeSWsjn9EyD9sdVadpipoJSO0HVzIAPRPbv4lBFalt4g11KKbMwmxy_SNanh0eO4Vpe1TRh7p4NPw2HMZwCM11oAirfb-C19jnM48jZDs6LgmhJMCdTzS-n_wpkqU9laxCJb5I3EOZRXEBJJONzpPM8FWp4XiJTQ1uCsowe-6qSbE5PDBxoqwhteCo3TMPPlY1L2dfVM0ceQ_mOT3IK5u92mrmpTqipBRCNLdZ9qUNcH9R_KW_XMilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3564b1a7a8.mp4?token=C0jf3hn2oPEzQ4JXDha2p5pFvUKgkG39b6pnMHj1chR8LcTGSqyJwH2xTGy6b5pupXikdxccHfFfTE1kyrEC4Naf8uLTUQLQeSWsjn9EyD9sdVadpipoJSO0HVzIAPRPbv4lBFalt4g11KKbMwmxy_SNanh0eO4Vpe1TRh7p4NPw2HMZwCM11oAirfb-C19jnM48jZDs6LgmhJMCdTzS-n_wpkqU9laxCJb5I3EOZRXEBJJONzpPM8FWp4XiJTQ1uCsowe-6qSbE5PDBxoqwhteCo3TMPPlY1L2dfVM0ceQ_mOT3IK5u92mrmpTqipBRCNLdZ9qUNcH9R_KW_XMilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع سربازان ارتش رژیم صهیونیستی هدف پهپاد حزب‌الله شد
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436187" target="_blank">📅 17:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8efY_o923zAC_eE-pefv7yETJvLNP2BMOh0lJ9mDUKsyIoPodvlDRmo5oOqsh9SoZMs7eLRh1nlHRFwcsS5aV9ljcvZq0lmcKoiLXzENQ3dnTLMbxWmUhz1wQFJGCLZWkJriLcx7fDNaJn54oCmYdFbKvnTG0l4JaDSyNO6tQgRBOfZtxOcOWMm8WCUGwlsDMsAArUGASmjQrIU4Kitj6v99YdJWBGf377vy2dWFVFHpjdWFeFT4-xWW9KK9CgLs2DQeM4n1vJnpeTOW9o4N5PTPAO1HZ-JAA-KZyN-gdzxLBIGGGm3ZgfKiVpVH2E6ceFOP-3KBc1ZfTZPE-JrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت برق را گران کرد یا ارزان
🔹
دولت با تصویب آیین‌نامه‌ای، مشترکان باقدرت قراردادی بالای ۱۵۰ کیلووات را ملزم به خرید برق از بورس کرد.
🔹
عمدهٔ این مشترکان، شرکت‌های توزیع، صنایع و کشاورزان هستند و بخش خانگی به‌دلیل قدرت قراردادی کمتر از ۵ کیلووات شامل این مصوبه نیست.
🔹
طبق بررسی فارس، رقم خریدوفروش برق در بورس انرژی طی مدت گذشته در بسیاری از زمان‌ها از نرخ دستوری دولت کمتر بوده است.
🔹
کارشناسان معتقدند درصورتی‌که ابزار بورس انرژی برای تجارت برق در اختیار دولت باشد، میزان مصرف بدون اعمال محدودیت قابل تأمین است و قیمت از جمله عواملی است که در کنار ساخت نیروگاه، مدیریت بهره‌برداری و تأمین تقاضا زمینه مدیریت انرژی به‌ویژه در فصول گرم و قطعی برق را فراهم خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436186" target="_blank">📅 17:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0a7ab35f.mp4?token=JExVdjP4IPsBsLbeqjj-ak0fXQr_5N8dFq1Daib824Y1AQo3bsjVQE_pbOjTsaDySfL3yWz8tedQNejzZXhQNM9CUzpuT0HTDC7vwC5OqdzlDnn-XyGFP6T5IjvrRjNTXIB9BV6y2-I7NLzii3VywGfvEUrtpVrYf1K1a8B_ibp7AUhFMrBjYQGqE6T3MjF0-y0PfET7htddLwypb_cYHhwLHuMQUXkh40MQdkfMQEmBknBjZST3mCZaUSbZyqNlihPP3jeJJmDJDkdyqbaR3UGQBlNtS2RrQBgu7xqQGXg9aQtktpHB2I1T9GNhSxLJVCFMUOZA5wJBhvfli8pqMi7E9xVo4sARQprs3U1rfbNLODYnSyvqfcyCvF8s5_VCFDP5RTdBFbn-eMrzzm4DJaiKfPotanuhU5ErZWTh3znb1gWa9T4N9mz81DPv5r5Hc8lLKZDUMTIIadRrEeGOk3zUgYtjbXlnqVgohau5EYVmjJ_xCm8qgXu7XrBZql0FQ9XtwLUaVRJFLwHRLqxBdczg2-Bp8YTLDCMd7nLU0l-xL-pSCdXAoXlBSXqNUwqPjGrcNVuNxHov1Pxp5Bz9-g7REGABppSvf5kB61Gq2yXEMM3WtFEkiFyVaMYd49378TD6wYpnlcAXvP4-33_wfXu2SNJux39LKsQSiwDsKII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0a7ab35f.mp4?token=JExVdjP4IPsBsLbeqjj-ak0fXQr_5N8dFq1Daib824Y1AQo3bsjVQE_pbOjTsaDySfL3yWz8tedQNejzZXhQNM9CUzpuT0HTDC7vwC5OqdzlDnn-XyGFP6T5IjvrRjNTXIB9BV6y2-I7NLzii3VywGfvEUrtpVrYf1K1a8B_ibp7AUhFMrBjYQGqE6T3MjF0-y0PfET7htddLwypb_cYHhwLHuMQUXkh40MQdkfMQEmBknBjZST3mCZaUSbZyqNlihPP3jeJJmDJDkdyqbaR3UGQBlNtS2RrQBgu7xqQGXg9aQtktpHB2I1T9GNhSxLJVCFMUOZA5wJBhvfli8pqMi7E9xVo4sARQprs3U1rfbNLODYnSyvqfcyCvF8s5_VCFDP5RTdBFbn-eMrzzm4DJaiKfPotanuhU5ErZWTh3znb1gWa9T4N9mz81DPv5r5Hc8lLKZDUMTIIadRrEeGOk3zUgYtjbXlnqVgohau5EYVmjJ_xCm8qgXu7XrBZql0FQ9XtwLUaVRJFLwHRLqxBdczg2-Bp8YTLDCMd7nLU0l-xL-pSCdXAoXlBSXqNUwqPjGrcNVuNxHov1Pxp5Bz9-g7REGABppSvf5kB61Gq2yXEMM3WtFEkiFyVaMYd49378TD6wYpnlcAXvP4-33_wfXu2SNJux39LKsQSiwDsKII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من پشتم به این پرچم گرمه
@Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/436185" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ الجزیره: پس‌از حملهٔ پهپادی در محوطهٔ داخلی نیروگاه هسته‌ای «براکه»، در این منطقه آتش‌سوزی صورت گرفته است.
🔹
العربيه گزارش کرده که «این حمله تلفات انسانی در پی نداشته و هنوز مبدأ آن مشخص نیست». دفتر رسانه‌ای ابوظبی هم خبر داد: نیروهای آتش‌نشان، آتش‌سوزی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436184" target="_blank">📅 17:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
پزشکیان: در سایۀ وحدت و همگرایی اسلامی، رژیم صهیونیستی هرگز جرئت تعرض و تجاوز به کشورهای اسلامی را نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/436183" target="_blank">📅 17:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
پزشکیان: از دولت‌های پاکستان، افغانستان و عراق که اجازه ندادند از خاک آنان علیه ایران اقدامی صورت گیرد، صمیمانه تشکر می‌کنم. @Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/436182" target="_blank">📅 17:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
پزشکیان: هدف اصلی دشمن ساقط‌کردن نظام اسلامی بود اما تصور نمی‌کردند که مردم کنار نظام بایستند
🔹
هدف اصلی آمریکا و رژیم صهیونیستی از حمله به ایران، ایجاد بی‌ثباتی داخلی و تلاش برای تضعیف و ساقط‌کردن نظام اسلامی بود، اما آنان هرگز تصور نمی‌کردند ملت بزرگ،…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436181" target="_blank">📅 17:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
پزشکیان: هدف اصلی دشمن ساقط‌کردن نظام اسلامی بود اما تصور نمی‌کردند که مردم کنار نظام بایستند
🔹
هدف اصلی آمریکا و رژیم صهیونیستی از حمله به ایران، ایجاد بی‌ثباتی داخلی و تلاش برای تضعیف و ساقط‌کردن نظام اسلامی بود، اما آنان هرگز تصور نمی‌کردند ملت بزرگ، شریف و آگاه ایران تا این اندازه با انسجام، اقتدار و وفاداری در کنار نظام و کشور خود ایستادگی کنند و در حمایت از جمهوری اسلامی و مقابله با نظام سلطه، این‌گونه حضوری گسترده و معنادار در صحنه داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436180" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4dbebb04.mp4?token=M6x2VQ_kp-D634mbRFehHn9fkkp9Q5J7AP14OnzfTN4B8WX2kGfdXnrCVrI-2rXvSu-zI_jd0ZNXIP_6Uu9cN_ObCjbegbBvdc3JmkGiu3PA07u15zx8m9MnTosGzkgACiXWNDnrgAmAzXkTFtLOO2qWj4x9U4oGhvoZF7ZGYArF046f8jUSNde79JSkNmWgaUXIMNADbdi62xuK0UhlxjS5W85UlufkVwrBXnSepuHaIT2EnHgjQefGq-LS6ghCQGe3M62iykaNTkNEbR5CEf4jKZh90iPIWLNbO2wbMEwCrHYFpVP1WylydE2Dfn6v-d-BOlb4rg5BgIRS5qdlJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4dbebb04.mp4?token=M6x2VQ_kp-D634mbRFehHn9fkkp9Q5J7AP14OnzfTN4B8WX2kGfdXnrCVrI-2rXvSu-zI_jd0ZNXIP_6Uu9cN_ObCjbegbBvdc3JmkGiu3PA07u15zx8m9MnTosGzkgACiXWNDnrgAmAzXkTFtLOO2qWj4x9U4oGhvoZF7ZGYArF046f8jUSNde79JSkNmWgaUXIMNADbdi62xuK0UhlxjS5W85UlufkVwrBXnSepuHaIT2EnHgjQefGq-LS6ghCQGe3M62iykaNTkNEbR5CEf4jKZh90iPIWLNbO2wbMEwCrHYFpVP1WylydE2Dfn6v-d-BOlb4rg5BgIRS5qdlJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اتفاقات مشکوک در انفجار بیت‌شمش در فلسطین اشغالی
🔹
شبکۀ صهیونیستی کان مدعی شده که آتش‌سوزی مهیب در بیت‌شمش واقع در غرب بیت‌المقدس در نتیجۀ انفجار کنترل‌شده صورت گرفته است.
🔹
با این حال، کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/436179" target="_blank">📅 17:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87e991cb5.mp4?token=dp0qiE6uebyJkEr5rnW-GJ9mlUaKvyt6Wx6y6tp9DDUBTT3C-Ts5-zoQo0WCw9O5lLZOTsZZj2Rf8erzWy6TdKlKC0CmFFNGWwjJ9aN_cAESpaKx9jKBM_IRaUI_JlOwRNo2uxC2Y6oIYTDM-wk3DNUGeTtzfhFGgsh3AWQKthN-ZkIIPi4uET4w5uFmcp7xN25LOxgRV6HYUPRWml5xlh39Iavrl2NXi6e6wL9nzzMPgVsJVBk5VdJ03Tzu92j-wCR-9zXqysJDRiWmE0dZH_nj1pthyXlxyLrAtP-24Vj1NtDdi4V9hCTDKy2JnNq423bWG8t7s9kviSIjBTrpSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87e991cb5.mp4?token=dp0qiE6uebyJkEr5rnW-GJ9mlUaKvyt6Wx6y6tp9DDUBTT3C-Ts5-zoQo0WCw9O5lLZOTsZZj2Rf8erzWy6TdKlKC0CmFFNGWwjJ9aN_cAESpaKx9jKBM_IRaUI_JlOwRNo2uxC2Y6oIYTDM-wk3DNUGeTtzfhFGgsh3AWQKthN-ZkIIPi4uET4w5uFmcp7xN25LOxgRV6HYUPRWml5xlh39Iavrl2NXi6e6wL9nzzMPgVsJVBk5VdJ03Tzu92j-wCR-9zXqysJDRiWmE0dZH_nj1pthyXlxyLrAtP-24Vj1NtDdi4V9hCTDKy2JnNq423bWG8t7s9kviSIjBTrpSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: نیروهای مسلح آمادۀ پاسخگویی به هرگونه تهدید و تعرضی هستند
.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436178" target="_blank">📅 17:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cgzrl_FtUI1lQ7d4zFpApBu0-NPQiqLQOqHgPFUfVZOIv-r79RNmqTs5Z1UTaDMUEWVFhGRayuI85H-pti39pDIDGS7goE3geWkaBSj3YPiGzToYJQdRfevbwj3yGQ7E01wLsFV9b3T3UKGZa16QP5qDbfdTAfRAJFLYv-4blXJeQki8n7JkQ6VSJXOVweg17NX2E7AiWFrIrG2SN4dbq6_uCRjs7b8FrR06yx3rPAZh9wdDpiK7ZMjGDIih6-PxzLVFSvQHzS16p3IIp4WEfpEzZCh4JlFgl3Wo4eDzhxfhKz9rKqqc5fJ4c7OEB8ONx1QWWA6Z9s9UpHsRG2vukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH6PYlI-Rcb6JHo5saf6ySiykrvIz-H4VvUlbghKzp4SpLtPAVUNjzXQCdiKDOF9MDDdoyoCV-InimNk_fMzx5c_Y8Z83xj-Tie_0ppOBYKRjduzk62LR-Yj0h9O99CWnTu9yiUcRW-GlL5kmepblNc0E11XMgNBRCv5Z0XCPAFABYq1OLwlqB6ihWqV2gdhemDK5dzlVqB6oHfxw5S3kprnST02euMgXK93d8-X4MB_97YIBBMZARY89gu19O_IM_XVQrpe4cOx9rUZbJKjdY7Z0qXM0tTq94oiVObHHxGGs9kJZYouWzMZnA25r6di8HvrFX-knQq4iGjpKMP_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vd2Y20-mY2A9AlWbiAdaIpV00h47FNdRXECdd9gcaCPRDk1YQlUbhZWWb-b55hwIpBzZbx7ylQ706eA7D7oF__JGWCYvzDzg9hwXCy0_6ZDTR-mWleH922Oy_QtbIMq1uE9cNaWHeXqMRAm60PhmzWIJ36CjSuRe21EcJStOVHkn74KqhiKfuzTE9hovduvK_M4n-51bfD1KrM28sEXw248_-y919d4jIqGclSum0WqSXH_fjZvMdD8wMStuIAZhyU_iQU1nwCJSiIlGKH0ab_MiKCK6AKg-LGYoTIAnre3_KrteYSraJoWCmmOfhSdOWDsy7cwRwdBPl3ilXxi1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUnJDUaiGvWEujtCtgPW--etOswcsDZRjvzNah5Qu_2LjcQR82sDf7XPJYOev1u2StzlZA-JtTRFr096j1eEHoxpdeerQ6NFfOFcXRF3RHRHs2g5K7Cni0lKtxsygFZUEt3MKylPvGPWR8F0FA_ygsMrxOF3YN9Sl8nMOu9MlNZPN5fpqncMbql-NqU9RHpDzL6xxYBA8OuV49yF5e6lUwi37EPaz96Ypo4wtiJPHQs2kfAGpN7jEKPcnjXTeeH4WP6bQoGqzacuQraXVEhOC0LqEV8pjuyd-Q22Hqg1dwvwTDnRO0E10DPMcPQLewDFPCe_gV6cvE5NCu2cw8JO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL6WavJL8HY3P0XSXU7TdvH_kNo6VrvbY8sC9-UXfIGJzzqSO4K8qnHTNeo0i1igB0B-ceJ574jFoSxuOZXlxWnfml7JxAq9RTG14Z7IXY0nj8VQsu48o0jNSWAGStdMtMTRH7ovhN-zGqKbVNkaXQ0di6jAAAfJ8IQNsQHAZSnQ0hQSlHIs6opijqw7lR-AdrHYKK39S1OsebmVdWuHNz435neORcMA1IyOi4b9KRxs3zFLjpZATKOjApW_woqyeLLwQN7SoalZfCn5XAS6G3ng8031T93Ufmhh8dFqSzgAye5BoB8G5BaDW2nUMNuIADrUGKFKpRUjEtVz0fW6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGgvE8GRNHu2thN-uFEpErAb5BEnlWSUunu4p-W_Erxt-eeQN9zIZkiFoTeKvmeJMMwYXnGA-js8gQXleWtQ4tva_QUEGJ4OY9YIpOxRDOt35lGnaNfGzD7O-ES49hqZRh4oI20sGgFQ0JJm3YGsu1eJPl7cjBKrujvnLJ_zbVHOgjDzau78jMWmv-v6om4T7FtnyG6MsJDrZ0A76NiaF8nw2urffEg1XsIWi4YUrAxmDQb2XYS6kNGIs3VsDiIvaCPYbLry4pDMOMI5J12hWIDlHAnEGLGE-xfRfWIZoOxOY4S4_VG4eO7dubQSRENEU1pIBh9eQVOnHatyJmzFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ1c_8xjS5llBd5KgCgP6rBKOlQrTQn14F-qL86Fr_o8d6Nbr411ENtKPuI6BaMivpGV0fyDpMoneNj-tgFs4Wse9Ij_-mV4-xV59fFmcCSxjSPkXNSNQrslqo95C1HDbyZawdkgV2s21qdsGdRasn30ueKd-yDEpCcJfKo6LquiyG1W26CMCXgHnmnMBoYdg0zc2gJMv759rBt1l3MIgxma2-t36KPPya_HsDEe09lBP53L0kbCMnBAlBG_VTca1ZY2KpOr0rZMtENN5zYpKSZnFzXpqpJAfatza_3xlXIX4SlBYTzX9Eq3YpJKUn270UcTUMvSIq4laVUZB99vMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری شهادت امام جواد(ع)  در امامزاده صالح(ع)
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436171" target="_blank">📅 17:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هزینهٔ ثبت‌نام کنکور ۱۴۰۵ چقدر است؟
🔹
سازمان سنجش: هزینهٔ ثبت‌نام در آزمون سراسری سال ۱۴۰۵ و همچنین آزمون اختصاصی پذیرش دانشجو–معلم، مبلغ  ۴۰۰ هزار تومان تعیین شده است.
🔹
همچنین علاوه بر هزینهٔ اصلی ثبت‌نام، مبلغ ۲۰ هزار تومان نیز بابت بهره‌مندی از خدمات پیامکی در مراحل مختلف آزمون دریافت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436170" target="_blank">📅 17:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9Xtxw0WXhMaM3fi-oNXCuRPuaNZNHlBIn_D5k4b2acckm57bJQApABdh9vIC5GlFVsivSDIOfAGEuMutx9XqTi1KByzh3Bmiq91q-Ku8Gay8f-K_DyayrXQ23qgPV5pN4aLdbUVtbMxVE_orv9ViTeNTuIYP6rM612y-8NGG18oZtoVGyY6zXTMNuS_Gtbu0i_p4qY-QK5Y8a5WjNvPQYSbrnifWz9YC3xvRUFdZKHdUD3UCXKdt2s_gnCLwTqnqa-m7OdSMTihhswKIVY0g-Q3zhZpxbcoRHh2B2b3a6xFder0ZJIYLqwfA2_m2IUhJL9FKeJszaEXDgavAmINew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlx5VVZ6Ze1jxJJ2c1czb0CtKnXtwIUk-PJYCfuwF_VTvQpuWBVeWZw3vN1T8O2FBc5C_THLRKOn7LDyHVpgx56mASO0UyqbOUvyCuos7FzHJMjyFO4njXNyQLgj5Sq9ne5wNXgfYAkwOGogw0L-dnjWI-fEh7X0Z_TWhk0NWIZ8nBme0SVsFmcBfCNwedY9BtzLzeH9M_H0G1ohyZYPWPdwY-OW5qR0coAJUcHo4cZsv6mPQj7F4xC5-9zYftl_rO9yXJPuWApXF4PIDs-07tzPfdXWFZXa8MQBsi6nZNZIbbhOC0buNPGgJ8jHg352gcYSuBBdEPZ3DnYsOiej5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQIndR74qYVHVqoljsF2AFLA691F4bcGGuTXTtrglLrcOfwBlC91wXiaNs32NPU7V-OBaZttW9w5MKw0UWPuH8hiFKdUe_MZ-HO4XsCYT0KZHeFx3xVlN2vuBMddYY9XIrgt2qC6Zx0Mm-Pmwu5fCksMasepGKLltD25RCQe3cB5UXC3bam-T2-9nZ0iTeG0zDbTVE1x-IJP1IZLgVax2kyWrx4kIbCtbmjmTfNu1d_DPfm-T-5Wt1RRearaC4DTF_3U8X5WjkAFbBNUtwidGTYZMMkXMxlevymQZqoeX2casMD61AlHnqV1cBrXXOhsgBHahh89LYapN0SjSHAaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XglKIrwcm9ZCz9a6WnoqPNZIB7p0nZtcTMhbelkPPG8m0YBl2QdjPdi-TrtyEBlmwMSvt2uyRO3_KjC6hGXgv8HGU0pOW-JqGMGSXVhc_9KYYSZ1y1IA9g_Wp2Uxta0IMRHnm0MkAGeR7VceZ9eqTxvTACHXAykSNph5ziklzz3C7DBoDmCNd0ZWE0vzGJEXCWoGNZoVv58J8ITRFkSl76wZiij7rSdHWQWUQVGjbGTYpPPlNxPB40LvYlAHBrvqlrPzmCxN7Tb5pI5OPlkwBcoWZ4-hYrtZebRKc-v1GAsI4oF6WeK7zWhAYyoZvETiMvXNKnQ2PhTswlY1B6QZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GirfmAJ-1oQYtVRWxbH9Gu17UrcoqxKmZkGtK2JkSJe-7CcwDCTySkHC1eA-gO3bfDUgQoPzmBoMhcau156TosixfIuPLIu9yM4KVzb2wU0NT2qdiJ_QAoidCjqVQpGYeLvSBkbJHo82jDtKA0VunBu2Is6rpgAboEDvTcsttS18GqfGcMn-OQeH9elppjgNOQJkGy9iU_f8I6oCklDpC0Of21gJ7e7Ga_uf5TkseHtCVD4O_WkWfdP94SdptSLv8pgnUnQMbvcA2THf7mu8L4u5K6k0gxiOBE0FteOd4pDlQr3M7jf2D_CFjnbY57_YfnfLdcwReieryNrgVxq3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان با قالیباف دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/436165" target="_blank">📅 16:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280d1519e8.mp4?token=o1IeI3CHgfuIkwx6tGZceKUt_rxkWwAEIVHylcvxfOCVuCRUGUxRQFw8QBZ8siDCZA6i4XtjmdI5uCR3-1yuK9M3_Fk01WjPYmJiY6yaZyj5dxQmR6H9oHy2OZbOTqAYYB9uaD4TrC9BYJQRy-nqSK5swk6KCSCExsDIJDv0AVtmMRH1DXbyGMafP9gOZ2u3Tq9LH6oim4blkV2JvqDVJTpHMFHpIqvKbditzbi-zqQQU8aLrIPetdC8F1-fR5ouIVLN-EjrNNphRahHp_THePhzHZrrV6vQiINJIICIwK21I2qOT6Ying4IgE40zcnW_52aawAaK35buaB15EQp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280d1519e8.mp4?token=o1IeI3CHgfuIkwx6tGZceKUt_rxkWwAEIVHylcvxfOCVuCRUGUxRQFw8QBZ8siDCZA6i4XtjmdI5uCR3-1yuK9M3_Fk01WjPYmJiY6yaZyj5dxQmR6H9oHy2OZbOTqAYYB9uaD4TrC9BYJQRy-nqSK5swk6KCSCExsDIJDv0AVtmMRH1DXbyGMafP9gOZ2u3Tq9LH6oim4blkV2JvqDVJTpHMFHpIqvKbditzbi-zqQQU8aLrIPetdC8F1-fR5ouIVLN-EjrNNphRahHp_THePhzHZrrV6vQiINJIICIwK21I2qOT6Ying4IgE40zcnW_52aawAaK35buaB15EQp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی بابایی، نایب‌رئیس مجلس: اگر دشمن به نفت ما حمله کند، کاری می‌کنیم تا مدت قابل توجهی هیچ کشور دنیا به نفت منطقه دسترسی نداشته باشد.  @Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436164" target="_blank">📅 16:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ثبت‌نام آزمون سراسری ۱۴۰۵ آغاز شد
🔹
سازمان سنجش: ثبت‌نام برای شرکت در این آزمون از روز یکشنبه ۲۷ اردیبهشت منحصراً از طریق درگاه اطلاع‌رسانی سازمان سنجش آموزش کشور به نشانی
www.sanjesh.org
آغاز شده و در روز شنبه ۲ خرداد پایان می‌پذیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436163" target="_blank">📅 16:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU2q7A5Lv4cq8vA_x3c4CAAw5_Un3E2gy2-Y3mtQf1leFtOnPNDLjafpk8gIh1pDb-hvQKbh2uc_t0T7nsEzuez-BYaunztVdP9WRPJ8mZrwx003vcvE4tcegvsqMkTaDM0FfQsq4YLOb70DB5i8uWyzD9c0ryIbQCa23SYIH0eYdMw3OU7IVML74KnZrceDpSGfGHKBaZ3lPReucmdv7y4v5gWPUpOTy6OQp5g_bs8RZwXl7wVi3NHHIh0hvfiBhV-JOeZ-GZgKLa2b7fITQWscROHqPyKbIYFokUMo7ru1qHHDqIm442b7ZR1TWhHXoJTv4FwknZebc5fLEpkf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب در امور بین‌الملل: به‌زودی واشنگتن باید با فانوس به‌دنبال بقایای اعتبار خود در غرب آسیا بگردد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/436162" target="_blank">📅 16:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlpPKq1ERkwtCZKTDqw4CFzULTWsU2Aho73M3CPpgKw7vAcfpp9IVjSMVlDIrB_hISoOi7ptSTyR-3gZem3ECXAH9xJZd7yyWn895gRySm5OQm5i1O_J-pE0hfyJ9vzzXpBkLQmMt34odVh2hKe3-dXPk-m8GllGZz36eprI5hd-DfQvQ1cnSjIVlNjFY2Wk2YE38D_UIb7cC5G7d9GGRJ5AtgH4p8lGPTuL6LZ7mgAsaWBZM_Jeub9HhNtTqkJaSO2vu1ijcMLZIyzWiMkaA4j0zgfzvYNqPdVh-TZ3VVhIOa2j58nFMSNGAKSUCqZEoVzzJF0tFroSACcGzq_w9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قالیباف به‌مناسبت شهادت فرمانده گردان‌های القسام: شهادت الحداد در دوران آتش‌بس مُهر تأیید بدعهدی دشمن است
🔹
رئیس مجلس در پیامی به‌مناسبت شهادت عزالدین الحداد نوشت: بار دیگر دست جنایتکار رژیم صفاک صهیونی به خون مجاهدی بزرگ و نستوه آغشته شد و در زمانی که…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436161" target="_blank">📅 16:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی بابایی، نایب‌رئیس مجلس: اگر دشمن به نفت ما حمله کند، کاری می‌کنیم تا مدت قابل توجهی هیچ کشور دنیا به نفت منطقه دسترسی نداشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/436160" target="_blank">📅 16:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیلاب در خیابان‌های بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436158" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUiYD2f20P2SnyUyJhOnQ-eEYTU2dKQamsDmKFEHm-QUr24slhcz4Bf_w00q5m6z_x8hqyDqTUsCKce03da272DO8hqQZzAEfrYiZ7aKEAglEGzEXpZ0EaHeUVKABl2I9KQbJJSAqOa3CXq0ssxPk6sbxlBETQrhnt9P8X7p4p8PTXSVHeShLo75ftNfqKOl7dSrkJ_AnQXUGefntFfKgldslYxDLE2yna7wHfTc4JU9JKRYj9_XRMFxJrlaHuSklRSsljSVDl1-5go5M14YAMzASL7ccv3vMyNILVBbHukSE4CGnQYJ9AESkNC3-TgSMLyMWPPXZPC7GHF6G-k_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy6FL9HqkuCKx5lBL8o4ttgazjjPFQc2qeXYbrSsDRFVDjxc-EKS4aa-iVosamnnE_k_uBAEEYoOj335v1691rMbSPq9M1APDJCQnXJKQAc5-bLlT1PmG6IUP5w0QxWSEGonVxQKdbe2mFfvcG1ovY4tU-ucZc3AK4UzMneyIkV6EnmLL6F7GmMg_NcEfDbiYGJa9oLQD-wlr_mzN2re5cVGsOYNSHh7kfa-yXDZj6Gs6HPAsx3eCRYqb-oLPgfIjT2flaOttq4rC_OvxvNla7TltBx7Eppty5mg1_8dZjP39wx2iHlMWxgq66TSlA1Sl2bciRszENE79-jvuru6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqbkUQeN_XtMn1HX6ISR62lvuq78qCnV_rGJhIDO_ivUtloCOlE-tbOGlXaI6nqsKJYQ331LXpzqOryXAUkVNmxzk8gdLyxcAZvHTYqbepCp7T5EDfmIXLTPMbjHSxMsDtgYGVVmayZxSp0yYhD8c20zKx-iAex49Si2EgajqkS0XG7QH8XiBQgHrSOtZ57Hc24asfocZ1FfUX_5_4mxj0N0GkaYzpHDXMz5EHO-3dqm4TzdWye95K2zfC3Tk4bi76Fa_yLV_8MBNRYhwqbvG8rzEr0jNkb9F6mpO640qR0FQj8l0b52NHQGHu7_PL27u_TM-KDinPOyPWbEQ0exVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/no0hgBqH8xwzE_r9jOBzq2V-d7V5tZIomL2WeZbgq8e8Ys_ZVWpxttdTVbxLLtMy45MT6SUXAI2Pc5TmWytIWM-ZLCW4YBlPp67hoj_s5rAp26mexUYMyDtmu6nbQs9moZ-tOUdhU1WikguUm2tITHmFmWo-QNy3k63l6Y82qL27oF23-Y8dhKUHxWBvvPLg6ZZuF-LUN_Gq8LtNihLt1omLIyapQlEtmwyAUkly7mLaXrF6dHHkQy-Z4kULpmr7UXdZ_ndTzchz95ysRFFzgsuWtbR8PTU07RHAX-uPt5vtMMhOe-_Q63kmt6CaKyeKTlZDV_4UlwMNxkP1b1ZiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5Iug8w5xlaw8ht9HZ23aj9tSTNj-kKNErUhF8asFvmYU_DkKxtNxZwjqweP7WPcrXm3BKuI9i0oo7gfyDvyegE6Xj5CwZMrjX4WVZis8qtdP-1YAJf7uwdhHHacFC4Qm2uDIgFT2LFQqcCeBfKiHJJlQmX5qjZPes-j1s1cXGlpFSuiu4P-unuM1RTZDw8CyYGvifJJnuTDNUDnoDdWtEum0KSlWwe4-rZ09E9ytGqC_b7m1xEgDp2-aymA85fKie4nz7dkBuUvTrBNC63h5sW4mHOsfQgQNKN6lMMZQzaGpxvB9DZoLCKGbSOQ7kiKA4xL3IUevnLarjkq2v6yKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWxHgUxCCGx8NbQzfuCA3JrToDuc9_NQwjd3mzATmUJfnmmgbIOjy7axgp92ANs5VCI9zSIrRiHBiaCE53xRtZbYcKaUcm9g-MRDETvuY2sfgxGO9BZ_NRQF1t-sNvtZgAjlJqo7Zm4VkTb86ojLyyOxCnGfauYLcyREf-k1pASNi0nsfTXvuvCiZOKyeA2NxcLyJP7xGLJ_Ixv-juSVzdRxLnfZnOAkTWQAs9JylI_b4UDBGsAwVC7cjz5vxCVFc5GffRMBPDvbAD9sa0guDbL1RFOSQVmsIeufQae9Avq_ZhswUjnQsc3Wkbmpl3B8Q7RrHxlUWJHh_lH6RlcNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_i6wuJeyoV13JVJ_okWUr5eY1kEDTZZ0IWg80SLG9P9R4Is3X-F30entbJ4e8oQk7Bd-xLK5MAi9yI55w_yHAIKy0zTu7VCQK1BQK7PnZJ3-XYfwhVtXYWGPFuzxzsdLRTTY3YiQVE9kb4mVYff2op-aM0ajFIplyugiZA1gzoNSamF3FUIvo_iqGUCjKs0QgtO5sr3q90Ji5TnZ207C01ojUuAV2BQmg6PSd8NfLakjmvMEcMGhQRD3NdzWnnzaLTV_1ITZqh7jduKsMCU6aCXVaKLms1LxdadxW5sAffFUns0ng6L4ciB4Yq4yj1VvNkAQ4nQgPLYrRO5lssZ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزارع البرز غرق عطر گل محمدی
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436151" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=jsHD0y7MrDTSwc5UXHwNQ6JbCJQy-dROXGKk-KlcCoXxkSzHxfLunQeGBTLThuzYStjA0AUgzp0tX8fIfW1QqnM189mjFUjrhRog8wSSeUigmb71ZKiMM5MuAWro4og0b5P76HxAoOi8GfVsp3VrPfpmiPsKID6rEn6Ki23RZchy5sE3_8bp09Q3UsoguzUmQ0TETdbSf3hp2qao1_wSUZ5Y70PVjH_v42pqxdsakn-3aaCHbIX1UHN-U8F0WkN7j5eieaehZSzPQP5kNIpgyPx06qmlp4o53M4kWchKCM5i4Cs3TGzqjNSDpeyLLLfjRM7ijLUuICDWXnqucRzuoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=jsHD0y7MrDTSwc5UXHwNQ6JbCJQy-dROXGKk-KlcCoXxkSzHxfLunQeGBTLThuzYStjA0AUgzp0tX8fIfW1QqnM189mjFUjrhRog8wSSeUigmb71ZKiMM5MuAWro4og0b5P76HxAoOi8GfVsp3VrPfpmiPsKID6rEn6Ki23RZchy5sE3_8bp09Q3UsoguzUmQ0TETdbSf3hp2qao1_wSUZ5Y70PVjH_v42pqxdsakn-3aaCHbIX1UHN-U8F0WkN7j5eieaehZSzPQP5kNIpgyPx06qmlp4o53M4kWchKCM5i4Cs3TGzqjNSDpeyLLLfjRM7ijLUuICDWXnqucRzuoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
توضیحات آیت‌الله صفایی بوشهری عضو مجلس خبرگان درباره محل درآمد رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436150" target="_blank">📅 16:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1IEUEMWOE2mSQWb8vITQg58GqhQ3KSS2PkZWEU3GzEplm_CUKyWBlDV6hIPaoX-bADXnZ6gLgp8o6J0sKtMuDLW7jmdGXL7YZVTLfFvnAX_wLn2OjYHsgB79gmlJRBtDUbVhhl86HenZNAcUXZjrktX4i5yARgeKZFgM5miCnPFyFa5V6VizpT5wdQ-ImS-0xASkDE3k4csZP18ZNYU2vIJdu1rb_VMLilLgnRRMX9klc1g-SwSGxF_jjXWVF6n65z9FIV0mvLE2zmk04IVcnqPgSLo5zC1FJFLOemT-iq_HmGHsMewSIzkM9lUlnan7KjWAFYgHHHsI_6z2c8A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور برزیل: من با جنگ آمریکا علیه ایران مخالفم و ترامپ هم می‌داند
🔹
داسیلوا: ترامپ می‌داند که من با جنگ علیه ایران و مداخله در ونزوئلا مخالفم و نسل‌کشی در فلسطین را هم محکوم می‌کنم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436149" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436144">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5AnC0Qgsk_a4DTU7QrmtLnlN5FyWsspwKbFMWtASUs_MmiCeeJyBqIjzgaQIAhLGmXqQeKrMswWxL_T3p4G8HxhNz7lBLvu3BrPTbh26F60l0hqHQ5EorCqOD1NrKvyc0n6VNUA-vE2tyzhPKpXOrlyLj-jjeQuo6QAqVR3YSYi-Ai5YrsXhfCgadWFPjgGzk9jDuHUSyXz8HiPda3COOtzJiqXxTE9nksi1GqbKDjrQIo_O15eSgjLMSWyC3t8yh9fZJZ9SgwzLaS6qBN50hSNUlConKZ2qPKM7Iuef4JT1CvOXovy8Yck8TrrZubVfVE4vbze_JEeIKS2V5KC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bM0fge9ErvbzrDy5B0Wp8JqAGYcQ4XYlFzgJHu9oFiQphIne13o865eZSOAoyETKiap8sdivZI5xehNiVKc3jdx3xPSpEIolwI8sTqA6NXrQ-VRcxq_-2oY9DWcvprLp49IpAY6EBVKWyydyC4GmaGgnOrW-vcfyKw6VMfVyc9wqougxE3Wl756Psc3K5YnOQv16zmfp0brrMIQtz78E8XC-WWWkEsmZw49XWuCdTkmaQiknBj7cwu3o9UWuNZVBCLp6KwtevhEZQKBOoC8ZeL6sE9cO4ntdLoSIIunGVtuN7hd4jmt3T7li4gYoCYY5xsYQWqn47qqBMupRWvSCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQfJZfL6tyc8gaSDwY6pfc23hAzUPjpQ0UhHWF9Aa3dE8OV9dA-IQhROFaP_wZmGQCustw9aXgShu_M8NhP7aAEt-3ktAQTqcGiwsd86dg7TUsRCwX3pzGUsJZ4lvwn8D-m5U_bQEolf1-fOj5HaDcMoRQyXf2Vgr6ChKsdmF5_crESB1nXvxRazWACYxIcxUs3gMLt7vGMRg8wYFKe1xGkvTDMY8w73eoQlGSsRV7gfV29OK4of8wasPBIY4pQ8WDI4wOK9VnnCfcFn_WaCCLXMCN-qD6xdGhGYH7mc8Hane7LQ19nvwwoWmQjttnOIo-yM6z3-lATxck3vAUCauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEuM716P4K388EMPHGSRplA_ioi9DA6Z0qn-G5cNk2oDTlOwwT-YAfurMIdZ4A2eXUnkvMFMjtCtcACuE94QwvN8JUvGsDK5m92Wv6AiKknuWS1MVTDLRDSENbhBBKQGAINsxrS5uOEKI3M596KLSdVmA7ZAoTa_X2HahSJf-yDHzPI-V0_7exueXU1MX-MMMKLB8vKQf4Ihhm0cdkGj-TQuzashb0n8P1O0fJo51zySPJYFEpccp-Fe1OQiOM4687gfN7wopViJhDYdAPxfQQXfYkFhhWWPwNTGe8bM_er98GRdfKKZsv3xn5I_YWGD_jL4u3mdcKpeZmWH4nHViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MocvlpPdF4D28gVL-cqMZaqBVGu7Ckh1QQlgYiJwLOoQ2JjrL1CVk5ud1VH4vz5tPBFTaWN2_v-qDOxUzTP-IXtfMJrELwdyZ4dfGwlwNIg8YLKQTra-QRiDLVQWwFjhEmjHO7AgDuL9DhZPW5JqraefZ2uGfEXukpLwiuNjNCzeW6Ic9Q5q-H2i_4YGENMsXHpD6nCwyP8ZgXLXRxooHB-EzaAAgm47S-iNVipkhS9O4U6dFE9Ewn2zZ2sjyFVImBafIbNsbH4pf0mhngp3bNxcuLdoMQ3ISlujHJ9fo_1dj-soAVkAaGKWjk9hZkbPR21TK5arVFgtnUFtkaA2Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قلعه‌نویی در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/436144" target="_blank">📅 15:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436143">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdYqMDikG0iQ1rXAB6nlxJqAPBoSwkcQfAFafDpYSVIgtONwn84nUooZMa9pPKdokqoGxdZTgg-KBfeU69wo_c2KPmGofOfrFq_esJggtHjnssLg-yAA590I199lJ8QAIKOxlnFr6RlsmXeS6Nh3OlRJ8AgiHwIMJYVl0skVB3UiHR70T8mfVjrbdkjuC2Wf5F2GnshW1ve_sr_YcGaHhH6sgulV6_XmvOEqHR93J_hkMogXlveFotRdqdTMuDNAE-VNPO8YhpjTqMwbditHT0QDfL-aJmO3c3qWTgKboHIly2r5KEmcfV6Ow3Bax4NbmB1hPfdtelRBZFxm7WxH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزفاکتور دور زدن محاصرهٔ آمریکا با کمک میانجی
🔹
براساس نامهٔ معاونت اتاق بازرگانی، طبق داده‌های دریافتی از سفارت ایران در پاکستان، مسیر کراچی به مرزهای ایران درحال تبدیل‌شدن به یکی از گزینه‌های جدی برای دور زدن محاصرهٔ دریایی آمریکا است.
🔹
طبق این نامه هزینه‌های این اقدام شامل هزینهٔ بندری، خط کشتیرانی، سپردهٔ تضمین، ترخیص و حمل از کراچی به مرز ریمدان است.
🔹
پاکستان همزمان سیاست کاهش تعرفه‌های بندری در گوادر را آغاز کرده است تا بخشی از بار ترانزیتی ایران را از مسیر امارات به‌سمت بنادر پاکستانی منتقل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436143" target="_blank">📅 15:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436142">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از سربازان دشمن اسرائیلی را در چادری هدف قرار دادیم و تیم‌های تخلیهٔ مجروحان دیده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436142" target="_blank">📅 15:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436141">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDIIkWYfuTfC2YBCLjknsN53C4XP7nSzQ3zaigo87GCOSwy1yOochfx_wEx-zBKC7sJnmvaYPKUBRUMul8B05W6frSkccj53oJHObHA_jc-qFEoEIGslACndPulHo6cBxtFleO474RKLQyMno5szVsqhE7r6j7HPC8dMT7inNQAtSo6FGRz89B-igrM6MIhpIuihq6ofQwl7VpMvn1WPanFmGbcXNeZVw3TZQuokOu8Ij4kLLPMorZDJ7l9ifM9_AohWNHDsPheQUPXjC2QoQh0_rfW1ekB7J5H7w6zjObpCQQ7T1_v8dXslSgzzq81ziIKA_KsIyLSmyijmw3SJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان خواستار آتش‌بس فوری در غزه شد
🔹
رئیس‌جمهور پاکستان: خواستار آتش‌بس فوری و پایدار در غزه هستیم. رژیم صهیونیستی باید پاسخ‌گوی جنایت‌های خود باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/436141" target="_blank">📅 15:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436140">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیزات ارتباطی صهیونیست‌ها هم از حملات دقیق حزب‌الله در امان نیست
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/436140" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_wwyZ_j-BDXm42CUQ5ZegHATN3QQNTicr2OKftM7aualKZf0t06qp0VELOoPUOlCMJCBwECpAdQ_xUiuzZNtEtjKQoWUAuCbTN66uXXj1UWHLUEWz3QMWygN4sS4lNqAr2tkqV6d8GdQv4zbxuhQbOy8e43_uoIhZbBA4xWIlhNCaoqQpZ897rd-8hko9F2X6RBtDsIelAk6NMI-BfoPmk7LyNMaiQCpa-sldEVHsObiImMjD4etkpev3APKtIqwgIkugyyLczZvFrTKuHc-kKzTCmTdmR8GM2oMQYxHnhcvTJTTiwV283NO48Gj_Z_x0Dr57V06Yz-pSMuzhY_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4EghAjnH8uiSmFThfP4KINwU-dzGYSyjJeJYWrbNF-pjICO0CqIVnDIBA3x_9b5_LPlm0cX2gxN5V38YHkBw-e82QuPh12eKArc1JzXBXtqVEQAFM_2Gbd3a6qrVbLzVyOK_jIB3efFoiUf-zOydp1qTvd3YdfG7FWfd4bMdn0lW1r2x-qAF3qvwddRbSOpMptvpc9kAiAkGOBiMBqaLd4cP-rUTnO9OXzGrdms0Wz1ziqAC5HrFmG02cL1X6teGFRS9pjtRKiIkdwNJ9bHqS8u2xJT9k_s-Ze0oMs7ccC_r1AhfCdI1p5Qzw2BF5y_BYk_qZzgs7IvErKdc5ejYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhC1JImoH7MZKrFpjNcIAeYec1K96MbngWR3KrOcVL4ARmYE5lg2K2nB-H96tygrUFertoWCPVerHrjnG8v_sQ2QqjXlQdV-aWvr5YMrughpCMOZNHk8EoPFHel_nreKaQx3ftD4FBeI1keCanjV9-q0wX95fboE9BHegZ59JyfkICPbJGui6nA_U1NirIS_okGHDFTmPY_9KlTwKBlhbBljwporMEbCbeHYoXjkpUa_tNLvlRkDmIcVflJDnBcHIA6lNObAU2b5WOJhmUaGbIf3MHEZk4dOgH2Y3K0H4TWSRRoAiv2hQ1bJKLeLAzvsYqIWKawGI0EhAbD6UU0jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrScIHDMcCxgs8P8ophXfKG4UbI3TNCSsrGN5fvPIjTYwZ8-jWYOf7RFlm_bfRrRBcdjVGt4Czi2h0SpGTFqD_uT-euFJQdfxCu2DSubEDdZ7C7DAH0ThC4DlT9ArhYp5Ezwtq_ImDG3yT_wGX4RcC44R_20pXdFSCEvWbDk0XnZVwMHu8OATj552UzzwNTzWmgS4FScoJqkhPWw8FGsHZRIUlNmP55cQJ_cdIYNwTv_M3n2ddT9ziorfEByygg4aNAwnnSRERgjM3Sl-BsLppFsDMoUR7AYwYr8cuPBUHL_t_KPGIZMBVWNjrOwmC3tUYlmDGrDCLKFoLlpAm85AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JA9zqv9wTwzF8Uq18uAmNQz9Si7gvcBDQVBPhriAFH5Xnro34NJLc8P04QEZyfa9PEsioNlUGNHQ2jlAftZOf9BacU60tXr_YOlV9tUAxHv66hWd7KxYxhVMxcQGOvUZZutqpxAPgfbUa8K9o8cA_OkFhExKrkq7XhAY4M4D38BeYhYisTpBpwOF5Nz_l5iAOMvtQ56cHzYJft7pCXUVoc1KRlzc1aBPbCTJ1jqJzu0QaG5ydQB48T1brPa-srRx-i0-QPHnLmzvH669VWjQTxzqc6-ZyXl0_eHibtYFCOPAjNBCpfGg4Iz6jUyq6QzajP5jeFFXNXw-7YMT0I1a8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-3rNaCwfmhCpl_OVhQs_26dA7IHbYDOy7w-i6dDE8N3GzhI8hh_MhBO9saE70PFSaKe65iCtKS-VqFMAJXXx-n76VG4XcE_c0qVO9YrTOmPs_jvre6Izz8085mOmHkiftg6_jYkEveYeyHJcIpv4gr2nyQBKvU3p7oHVuv2XKytGsh6q6AchwNtBLyQFGQESyRFpEkR2cbLJIYrzNxaWaCzS-k5AGGK5arCB17C6ZEezZi2BCIg5uEfan86zQ0ZCk_3HpcYdWSTXxLcBfP8h1JyiVj3W_m7tXluH1emHUXAcJKVh3IjcXJvumLdZpQA3SQjlqY2Ec09cwG-hapjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H92rnFhDjOsCJT4OVtwyookqxYuJMArrCjyVEYeu_Hsjw_BmLGzWaIqRFsIuLsEb5Roj5QJKi_e5xb9xvgQEz7772DqfP2-1XgyJvdTP-t_Iu4ML9_aC4Sd5Ug_oRbWCeD0XM9Qr1uSoOrLU1OFal5AipqCSc3TpyFVwcY6paXLG2EjjrmdpucRse2pg3qUMpP6pgIiNzcc0aCG66zZHGg4KdHbCKHgs8YrztC35H6NK2EEzlCaom7NTUQ6ko-0WLN8ZOPfd-lP0NPu50eoI60n2mLbut2TKEUlqfgeqaxET19fmbn0Q3Ok96uQxnNZ9k5sTorObc_dG4b_x0pImoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مرمتِ باغ گیاه شناسی ارم شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436133" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی وزنه‌بردار ایران
🔹
علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی، ضمن شکستن رکورد دوضرب جهان، مدال طلای دوضرب، برنز یک‌ضرب و نقرۀ مجموع مسابقات قهرمانی آسیا را کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436132" target="_blank">📅 15:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجات دنیایی را از امام جواد(ع) بخواهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436131" target="_blank">📅 15:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید سردار نائینی از روزهای آخر زندگی پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/436130" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انفجار کنترل‌شدهٔ مهمات در محدودهٔ نصرآباد و میمه تا فردا، احتمال شنیده‌شدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436129" target="_blank">📅 14:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: امیدوارم سازمان برنامه و بودجه زودتر پول گندم‌کاران را پرداخت کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/436128" target="_blank">📅 14:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/436127" target="_blank">📅 14:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: برای اولین‌بار ۱۰۰ هزار تن محصول تولیدی کشاورزی فراسرزمینی شامل جو و روغن از قزاقستان وارد کشور شد
🔹
دستورالعمل جدیدی در پایگاه اطلاع‌رسانی وزارتخانه قرار داده شده و حتی افراد ایرانی که خارج از کشور هم هستند می‌توانند بدون مراجعه به کشور و از طریق همین پایگاه و با کمک نمایندگی‌های رسمی کشورمان در آن کشورها این فرم ها را پر بکنند و نسبت به کشاورزی فراز سرزمینی اقدام بکنند و از امتیازاتی که برای آوردن محصولات‌شان به داخل کشور، موجود است بهره‌مندشوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436126" target="_blank">📅 14:47 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
