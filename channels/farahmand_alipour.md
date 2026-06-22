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
<img src="https://cdn4.telesco.pe/file/LT3hMl2R7w7y6l6yPsDugVDXYOPjJa9G8Gk1FUKJ6Nhmgy4ULMkJzuEgGDC5EzO1keP65ohgHtQj1ODY-zI8fuwkN_N_CocBgfYYOKHSTgsDr5G_cT56Lx8CnlTUV9PyV0F4YLp2UK-z8E7UC-pVNqBD1E4ioe0GQo8wSI_eIT4guiIFX4ZC26Tf27e-si2Z_lsPJfNi2Z3LglHm9P85Yray1HaAvbuuuIMXFFXyEnC4aRXaZJtqxxXCljUaARVfDK2pmNa8qkTD-oHB8XLyGMESDan5GUPQJN0LPwAx0tz6yjOKHyQ97lKNkWW1aEfu-8w6LlZjz-HyCJGCYdi-Kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv4zlnOPtBcyxvpNu53dEjnxLCY9FSYzpUGEa8o5G8wPV0waLcREqAJZtb1H5HCsKlWz-gXL0OF4KqsWCGj7jngJOBuZuZWxloo5L8fZtG3v2qHg17S8uwjZsitxOAPoa4XMtFpyqC-5HGc1BieB5QExO531_P-kz4MVKsbVbm2oc8Verf1I5Pg0478VUh0zrmwYLcEH-Cq-fA_VjyRuRAYfXBbx6pY9ulPF4GhZAdIghMVarN_zC2toQ3ZjtBS2_My7SIOPFYDYPEb24BaAGy4Dk--6j2r7KBlllinWIOBj-G2ttarumz_-_6uc9xvCpFnU2CWkG162nSZHZ0SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3z67X9JkE0iA6VGYTVb7vqyZUkVjtXzKoYKxqA9JjfZGG5BhKzYtjBpJkcJsb02p0Ud77sD4jGuW6DVr4XLmmMSUPfX0Cu1Rq6zDp7kSGLEmlkSwDYwlPcVeLOmBkCR3FE92fN5_TgNtsEE8StX-h2D3EvnXXis_Gk_Lwyd-CQhBCOWxcpmpLiCyATmOQxW4b5xL45RmMoIQkMWhmaMFbflpwE3xjTw5rlrpjm7Qw9zekNmreEJhEyI6R-2zIAXOPz7HOXBVcPfAcBWwCZx0BTwK0NRGgXKGVFIB6dqlNXeXxqq3vMH6vI6DF7i-rTrD24QASs3zFlZo-t7KpW1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScwO_3xK60fcKFljmgBJYNV4e4DxBgqzEO1uLenk2HPvA7TS5onQn5rZA_X2yNFwcZsHXBsbUikXWCTpD9Dr1bu9JtbtVedrgMQI9QZmvCLi_PztZ6ukdWeP28RVTYs88n-DsmIQ5n_V6Q0rhUG7HnPbRNGF1ZOungfj6kIo9mnYIjjQy8jshqJrI5xfyrAB3nKIrxWKv6FCSfeBJ914TRN8xF08ZwcpvygjimUi9h5waxF8iLjah4-GFvuCGZuDM2YdSyRHbpCg0zaYXAeVt7Z3CMkGrAUPdK886X9d2YhCYO6u2zrCJiFyY-7JMqw6eW2Hq7YRWaeKmdo_W9xGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3bxx4fxSx63_FfohgEqFjE1qGXeTDA3PbgbUXfn4-UBWE2tNwtZpY94ILw_HFCpqV7gDm3U4qyrTJW5URhuOqlkFeXrX0msXySBvg3VzD1230_-Ky0eoCs6ROVCXB9yEqoxkBhT9IDTTaxuRapMh9WoVAFXVa8R8sazgR4khfsfc4kcWhD4G3fe4VRhKnJXsgjWJqnbEHE0QbKwE1m76EHzHQ282hdhodCQ3QGwSwwtdsJsVG9Mo6mO7LCXniobGjJpBYTnlr4l-RS8PeVcDPWe58b-aCKLB1-TRzymFHshMCQrVLVtPMllBtxnnLo3bolui9VpDrC0FUrH-nitKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMEJDHImA3LZAKp0PlrLbwyqddPAs-Nx8LbBSYrTVEqk23uh8oppLDPO-HYR-MOlGIzDmRfs-ftdSEVHW9-1G1UZQM0FGPVxRIQz2GfdVji1to_LDR-UkVXAM3lFNvbITVwojZpIy4C7prwsBuGcV8WcAu9xUihIkvGcZHK4YU_FOz8QP3ifMaMLHhA74iSaGQmI9cLQf8d_kx3Uj1RZaufuYiLQZEOLgKgQEQryLmPjDS1hQi3RShukQZ7_wjDwZ6ZijgCHNatQ_MDjeQbcP9Tysr2yJh-G8xzdobbrigcfzNhDiF6vrjxML2O-g2gkFjubhaSgF66LIuL-WQbElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYnfPFsRRGpKzNNfc8YAodSzpW0H_a4thhaeJ_XXbdUtteXIyJye54Rvd0MhzD5SIhc_I_4ReovGtP9fdpMdQG_T6SXAOJCSQhJDXf0FPepfXTQTuIdkaVtZkgyFia6jPmu_zSkL2siOFaRRmhMX0IRz5Wq9itjlC4FyOVDD4LGYiiEu-hXgZ6xEDzhObUaQRsYEjIieVIZmSY8oPHs9FUt3SXTII_D-bFZWAZiXWxSSorVS4e_K6MO042IcPNZznsnbIa07XJvLMYhdT_HWMSnRNGgbFbXLsvzNsehd8J1UdkbieK68wEqaWYsUzoYsNArgmdkkh1KGcgOSLSoUVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRMGjR_kUKZw5WQQVNdhkE4kdvWUBddcFTmeYacXXlQY5hLqYnaBWif_KFM1dBbAmJXangMEGrmuH0jKXm-L5YLqY_pyEzvV7RgRupCB1xG20vZHBkYlf9YQnC5AfztEsWAsHxh85dvMRgNb9FXN3yzBhdOf6g_2rVsBXPXQRaoaw6tnm3AnSE9v_OEgS29MfBMjmxOBHbs9MpuDLw8gsx-TU-ehGE6tIiI1hEmNvQhujfaXe_EObGgQr3cfEZn2VytHEuTG_qB60fULSpHbcfLMPI3Nl9k6wN2V1O-x2Lj7Inl8girEmUQB5YRDGTAqc6fSEC31NJlvy7j1ZndjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIinY0MFaAW6k6z2K3hUb0170UpuB2heigF5UcSdeuS91zQJ5vy1GubbRec2t-dvqz_jKK4Qm4tmjSs9x6x6lzsJIhnTw8Fk_bHjWJPhNH4x4Oi5LjugAiWnjCj2SHyr3k0ah2QYyhWysAica4RerzIkeP1l4rw5sar9hEWnjCkP3iElB38-lorz5xlaRsyyrbyC131O0D9I6NY_cmVtCmkX-WQkSaqlYsu1o1xo8gitEj9A6LaTEebeMXX3VBWgyiqTcZzLAZHa-Dzbdsxp6pBmECf5f6qAwfewWsKdnbkq5t6fZ4chpgkHzVyAFfMyQKcsgoT5JIcFDZDN6N5IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJPVLvahshFW0k6cQc419bTwku_x39NwS7WiGVBNSSnpozd2yn0VvhVte2Ipg5wmBqco4gJeOGfE-f4L5G__XrTrnkVyWM6l2TLPCbR0eeFdv7xfC_N5klzYXoiz-MKlq2o-LjwAzVdZQ8qYnggblArunLF3tfF2WgZxFBdlFRv98BiJq6OJcmmZ31tetKHDtOneBa7qaAKf-BCJLDftAtP2XUHlpaEwvvKJHeUoENbfJLQr43BTg_TqW8eMeSUOd96x-Qu2jriqLOO6r6AmA7-OsdfndoHCqgWJBEJP5xq5ydWICBI52ltCgNnmo5Jw9efDx8nuEk628Coj91SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYhK15Sh0cGS91laW-EHNkwXJ1erUyknj2kwnWuYQEnWK8Ra6bD5C4JWBbpZhG6G5N92AdhONmky-ExHQAM3nDvLeU8cw_j4hg1GONC33pEVwyjHIWvcs0MjRtCBDTNItnTnei590jAQeTHI-B2qtDZ_TansdeD7FCTBMCcpXn0dHHvJCMPitgdUJPxBw7uFC-6gI7IEzgcWXIUsWEe7uAXnfUL7HrnZ0QTGY8W8ORvusgJ6onnHxRNH-VjziZgQ6xdGuaQvnn4Yl-1dbw7ysf89H_hXckK3KW4jd-72JbVem_0rYPxGiyugZp6kuN4M0Ci_RZWhTesaXemaAebPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk6UzVHiJ5a-wdt0SySHcSrQ8Y-4lxQVZTO6H2iQzaRkCpqU-5HA65T3835alxbJElUi4teeWwwuGK--Uaj-E9VTOP_3YcZWEVx1Zb8ugOZ01F4MUCqjLb5ZSgcGH823Pj7GN_aQS_4_6MZ6wKoymD_gRN-Lz6DcdJkbBoTPNfpbeRpA30GGt5fGqzAHyLQiakSlhzVQWVk_y7sBwpe5c5zAkXKZ-9F471rtEgj-oMnS0fPeHQyH0TzCT1wcyemKXXq5yeL0mzki0WjVLkBsBUc7ZPpUZM6fSWI22_grsYvtYQYWnrrthHcwJp37YPKhnRVsVLTdjpx3K6JOKSkw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Qj3kf-JJzINr17Bd4aFUCxfE4RNS74s08-2sj1vTt1Y68KO7rkOl8bv5Nzr6Dxpy-VSDZqbC-OgtuwHMXozZsPT7b3O-1gIW4parsuZEEjsYqAx6nrAQFNYpoyX19IC4psoqsnlqurvaZxOF7YRdd63iLoPo0N1BY6lFHScmTesRFSIgicaurVD0fJufELkf32dI5wuk03y_Ezw88HG90GhfPHercRsaInDzNgSuDYEF6VanyYR31UU74SA2PqN4sRfq9kzt07ZSWG-01uj_UEuq4NE5e-toJ1_WHK5g0cxBxflg3z5WOik3uG6GNQoRzm9ZLe02dTJzDPSgM0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZEUxik4qkJOxt2zT3M0zPIEtgXQV5xt35_mCBT17DAz0rWwr-YZxJ-w4w7O355ISyODabxtHfiUjw8rZi1TLgUhoU-WHv-hk8C2HWLRP-Bnf_ACQ5EQc5v_qXW-Q59GM69UTW32x5rRJLNOjL7x42dAJ569rymI2VVdkGoNE4kI_TD5k04zPC5BwOR8Ab5j0JkrSphgWF50RkPDWeoP8nzG-BlRIFeJalW7jM3GZjmwEQ8U4maGJ4BDRcJ2gXuyTiUV6ssgjIYFknUsKqtFCcnIf78qGzsII4asH1D2B-Bns9r4PLNvAmpSSgV2NdrZpKLiXvx_D6FrN7SSSy28kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbQ88cbc9JkPY6MBzhTdnlh1gN_DP2rftIDatKBIBa9g0seSU3ApaaEHWGLNHJm2fh989ZF4aukxXwturVk3sYourRCDw9s7pPou2D_7bkL5LJhi39CXaMVnL7RFJfEN3LHNxZqn9Xuu57yi-SH-LJYZej8aqh7EaBBlT9cKGZmPkGpGjDsm40FhZoZx6IyfYmhDnEq7Cw_Pk87Q9K6nHgVxofpRfb7e0PScIswKS2CekyuzKGMaTeebN5VhIJ_RO98kCUgfYI7Gf0m-FhgqvnrUNEoU-KDdyMIqXq-oycCuV5JKVh2vUb0CPKztRfpJLh9o4P1aPIfhkyCdmtovRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SiR6NJQh67CMyAmwIoUKL9_gwIQkQeVnre_ELRfi8oXodNfMmSW81S5xB0ydBuNSPf3c1PCfbi0JLnO7psQwDJ3PldpPdfZOkh1_VpLBbRryl_QgS_nn4Wi-Mn93q9brtzTXLAj_57cwaqC68ZHSme2ANQO53rWbjmEEYjJAmMromb2PHuAGqBquo565HI4Vn18g_vEeHcKipgSKY4pA6xAt7kGzuHbh4e62EM92RU4RudBbl8H-xpKbBvQ4M7YAq8IpPwswDbvtmUxwGUT2EXlkNIeTWaD1rhPPQ1DxcmlhTdQLfDi9801gJEWcuISmKFiLe63tvl-woVSMYqj1XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SiR6NJQh67CMyAmwIoUKL9_gwIQkQeVnre_ELRfi8oXodNfMmSW81S5xB0ydBuNSPf3c1PCfbi0JLnO7psQwDJ3PldpPdfZOkh1_VpLBbRryl_QgS_nn4Wi-Mn93q9brtzTXLAj_57cwaqC68ZHSme2ANQO53rWbjmEEYjJAmMromb2PHuAGqBquo565HI4Vn18g_vEeHcKipgSKY4pA6xAt7kGzuHbh4e62EM92RU4RudBbl8H-xpKbBvQ4M7YAq8IpPwswDbvtmUxwGUT2EXlkNIeTWaD1rhPPQ1DxcmlhTdQLfDi9801gJEWcuISmKFiLe63tvl-woVSMYqj1XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdGReSdfRYJjY816ofPlrYoKi30IZ_dgjADFBXYpTnO5br0S3oQsBdebhvuWfmqgppN_4Xu7rPBMPCKK8HOA8T_tGxjWnb7UWzFRPi0icx-qKO_YGp3aXGd4r2TTw0ZMgRvJF17rK5VtayaygIOoPLM3AFMvR7QFN_-mxaS53tIs03odOA34hYw6BI8CwRlqaTbcqVgGoXVSP3njVpHoFuqnSAipvuFG6A-uIGwYxqLHjDjJIctmlnUSVio5X4hxYZlpnfQEMDYDwi4QT4BHABzPsKJtDXQ8mw-ptr0hDaMPjIjsFjwr967ZnvvDbLxlY2DUqkNMrBkqUCbcDWbzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=umex0X-gcOASqGkAIRXGhSnzjEvIdC_XT6-I4r0H7NytaiHVT9-5UpklNPGmeF8TXjz7Tt7ybTjHuLhpTMzxvL_4s6ToDsh-wdvVm8kYTJF8lj-SjYzK1goEJxFF-bR0oTlDYKutCIS_Eva2Ap_TX3GzbRtx14Dpj9qCZEF10iJrKk26K-MoQsBtC4qT1rAgYSDrDhK1r0u3P8Tvt2mRS35TS-KflmIm1uT8cZ3MdkjUyPCFadTh9MlurWWeOwdAvj00WOm1MkdDeXGw4W-_2QIgQUrFoLJkd0E7Tb_zOmSr-MN_Eu5gdqvRHdeGIKppcsCaqJ5yFfIGGmIuvcQtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=umex0X-gcOASqGkAIRXGhSnzjEvIdC_XT6-I4r0H7NytaiHVT9-5UpklNPGmeF8TXjz7Tt7ybTjHuLhpTMzxvL_4s6ToDsh-wdvVm8kYTJF8lj-SjYzK1goEJxFF-bR0oTlDYKutCIS_Eva2Ap_TX3GzbRtx14Dpj9qCZEF10iJrKk26K-MoQsBtC4qT1rAgYSDrDhK1r0u3P8Tvt2mRS35TS-KflmIm1uT8cZ3MdkjUyPCFadTh9MlurWWeOwdAvj00WOm1MkdDeXGw4W-_2QIgQUrFoLJkd0E7Tb_zOmSr-MN_Eu5gdqvRHdeGIKppcsCaqJ5yFfIGGmIuvcQtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=T3YYAM86i715Ie6xOjHoreW98AvmvrLTJ3ttYai75gy1exaFib6z-fEqnu6uB0tKbbAwjm075X6igSAUxpw5zESRMyLKMLljaZ_85EgXWX7zFDAGlGZK3boAf7GGREHvfigWQ-xDRNnLDYFVc3kcW4tvCNeMftbbd3PcNWuTA7bUkIaWG5rbJfR_J8Qtpq0IdUgB4u-YgpGBdR0b_SBT-PqAIzoYdwbBHWCApWzKnalLFMLA4tbnlCLYuD81HQqrcXXZ2zLntGp3ZkySisXriuliLFeSJRr9PWMhYaAre-gucVme5mBqr_3IYQgU-8ac416ii9pkZ5zmJzesYCSpHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=T3YYAM86i715Ie6xOjHoreW98AvmvrLTJ3ttYai75gy1exaFib6z-fEqnu6uB0tKbbAwjm075X6igSAUxpw5zESRMyLKMLljaZ_85EgXWX7zFDAGlGZK3boAf7GGREHvfigWQ-xDRNnLDYFVc3kcW4tvCNeMftbbd3PcNWuTA7bUkIaWG5rbJfR_J8Qtpq0IdUgB4u-YgpGBdR0b_SBT-PqAIzoYdwbBHWCApWzKnalLFMLA4tbnlCLYuD81HQqrcXXZ2zLntGp3ZkySisXriuliLFeSJRr9PWMhYaAre-gucVme5mBqr_3IYQgU-8ac416ii9pkZ5zmJzesYCSpHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez2N2yyLY87yk64Vx-GIATOZVTFjLOzAUDDt7dogaGQIzMuIocbhNGrRgsAZhu9FhYWSZyvqKYoiYATXSUNqCvUUFvlFdI_dbvrO_I2lXoYjQtIG_2KmbkJQ86teQWiUFCHMiZmZx7SbddvQIU7O6_ITgg3NZdKl3REkP6V0teAAWy5ZLwrarRjyAHth8P_PfE1yov7dT2_5BDk-O9dtRyYb5ptBTSt9IZxy5czZMYj8D-2Ysqjpue17RIMqdefvdxN9deyi-sgFR6FCabe5l5z-GgWTgou6MFetjImjTmopHyihdg3JB5x5_-_o-DN1qN6btKvdc7OZ05xwXS_6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=ZV5DKEjdyRDacrT8SXSMFQ9q7phvCqPZFkEA2mvXDh9aaun0gC0TMFUFRS1zvC0GJp3seUtTKJ6eMmZwym9JDSy4Qe7kqlC1JGAUBBdLllnzzOmkN4dZvBEdep1lDanNGSZBi_K_4aYyAsLayDGrjsY8sO1PNKTXMO-niYWf-zhGuNxgyM4TU-UrGDupYpis9YmjUOJsRGyqEp0U1oJ9g2_Ynynb12DBq_xjCZwsiOjBhU02Yc2utyTgDbqREBwwq35V721OT9GGQoX77KWmAby-eb05PcWX3ODUAS90LcKKsVhFcchnHWfM88H9toYUR-nqaoNiJoE8FxC-kRONuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=ZV5DKEjdyRDacrT8SXSMFQ9q7phvCqPZFkEA2mvXDh9aaun0gC0TMFUFRS1zvC0GJp3seUtTKJ6eMmZwym9JDSy4Qe7kqlC1JGAUBBdLllnzzOmkN4dZvBEdep1lDanNGSZBi_K_4aYyAsLayDGrjsY8sO1PNKTXMO-niYWf-zhGuNxgyM4TU-UrGDupYpis9YmjUOJsRGyqEp0U1oJ9g2_Ynynb12DBq_xjCZwsiOjBhU02Yc2utyTgDbqREBwwq35V721OT9GGQoX77KWmAby-eb05PcWX3ODUAS90LcKKsVhFcchnHWfM88H9toYUR-nqaoNiJoE8FxC-kRONuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn_ba-FOH-ErX42q_qESwHWWRWck5PvtUODcBEOqf4FyADGrIiIFTdfs407tbJFB8coqFN8tz5dmz_CXrIS99rqEdd_kFtlL_hdsX08hntYpqJK8eYmq8AfD8vG4w8W38akwIafb0s-DyqvMPSYNWxBnTIIoEOEJKYjRezAehcMsgqcbFRKhKJkw7qqRV3pObR3067YYGZZaBAb66RZflkAZW4l6PQBzhGDlnysnro6UAJFlf1jwi_ox2FcDyOyulQ4_j33ns8hj5c2yrM5BEjgDJIwaqmsq95n0M5_dHlzqsLX3zzHNd2Msjer-qzE7Gqm4iDb37s8y0b0tSRMsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMDUyzrG7Gr33AFjuhsuWcm9gUURhOhVZwlNpFLAvLCcqDfDkPT4lw4Sy-roD_p_nlTCYLjk6_34-iMzcyXqiPz7qbBW4L7dqVFUeY90P3CnflyVPebEJukdOTP-0ZuHteoz7bOQ--KnhoaYxWdDSsJW3ioQAvgTqcYHfBpFXgG0R_PFIuVS-8EVVUbL_Prg_Fl9iA8M_y9qNrFCZx6UOhPrQ48yXnXMV-Lr3Rg7KfbjuMN2LQuDt1CdNLkETRvY53cgXHai0OXlT70jcFA7d5exL2lO9LQcvs0cVH_CCqtpNEA-96v17GhkEtQdtrufsXER88NvamrYtCkfo5dhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu312Th5RpwyNVLL9dfT9krsah_fUFu7-gCyYVAniLsoUbjLXoyHoxQyGO2n4inJ37vSbUXp_VHsrg9V81l_Ws8RIP1FkZrEMJoK9eJ2--L5vsm14w9eHtcipHdaxX-FYOfYob2h-SBiUHR0Vh2sIvRBtqUsId36-OApPSMn7Wm98JJxz1IEFyMwDycQgWnK7-b27p_prjtp3m6JQ-OT03O7jaA3C9vuMLs46GrrNZFKOebkV4gkw3T6ndXt6_ZJXlQG3zpPqRbH_Rs12mhaYmUDkPBzZLa4bGSb45IKQAq-yEkkDAPL9wBJBUzEGT6JP7br_tE7Ko2VrX1t5zvnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg0WvLuQVaAub5W7KkAnAzIHwDjaUqSSKVezsyKkOCnIln07zxbIRaXus3bYXaIH_-n50hIeycspldQlFjfyS7ce_IjAIiQoV-sVfrAZrYR1ppF39xEiwNMjXcsXNxtfOKZ6WjJ66mGLLeYMUliABT6-xLFhUwiEiPeWzoxI1cggQW1s27yqifq39zt34ErWpolgPsI49W3yyU1oiC-Nyazx4W1JWhoasQiVY_NQ8Ib7AZuiICoB_7Epb1e10PCbhBetgVm75Rnttodplny7c0QeTqrnQRLzLIBE05XQqfl2BI2r0lZPwGQD1ypwENURyicMrWnhfWM91FcyroieUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vyLcQnhR7UhETEOPP8qgrUwup5ez_Wt6X9ZIXRK7iT1a8oR5tua8PX3Mx-75lo1IePec_syYYApN6t9u8ykzxQHBD0-2b3SGz36UGCQImpwMk6c-ny252kfNv0sBkZOG67FecCWoBJh14LF9-Q7NIjo4iYoQErm0ycxEymRTNgAElnvs6jgOEpyD-X3p_xtoSlniF5ELx7J7HW-HUInA1jilyJbRJdWA8K26LjZO4OhAf6b612jcC07fEb-TRJICpv_0iHdujO-zp7XUjVHnI-TiGNFZm7dhCrSR8B2Z_jyvQTBTGubJWfopI5kP1bjhgPnSzqbqcE1JOvxG0GwFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vyLcQnhR7UhETEOPP8qgrUwup5ez_Wt6X9ZIXRK7iT1a8oR5tua8PX3Mx-75lo1IePec_syYYApN6t9u8ykzxQHBD0-2b3SGz36UGCQImpwMk6c-ny252kfNv0sBkZOG67FecCWoBJh14LF9-Q7NIjo4iYoQErm0ycxEymRTNgAElnvs6jgOEpyD-X3p_xtoSlniF5ELx7J7HW-HUInA1jilyJbRJdWA8K26LjZO4OhAf6b612jcC07fEb-TRJICpv_0iHdujO-zp7XUjVHnI-TiGNFZm7dhCrSR8B2Z_jyvQTBTGubJWfopI5kP1bjhgPnSzqbqcE1JOvxG0GwFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=UO_aKZ8bMz3BnHpahFjZ2o71LMPOai5NbTCeccDhfuSFxarSqIv5Z4wHFAaRHetIt7XYr4mFwaZrXGAhZthDUUTsVTEpCIijV8i_rqa42F3dGY-MgM3GBmyD3dh5qg3JXyE8sQSvaj6e7TY16KyeRIDSM5R-T24X463Zi1CdVILOU2l6oEQrks1rMbLDNTRQc6BIqHAwNTh45J6rPS1cxnr2GlL1cesGXQTZFyiWmgcS9vKQh0o_HyPg45BLn15oUZdOhv64yD6w1pcaKaSAlVhq-LV1myiRs248ze3DpUE-56PV3Fo0gdN0G4SyKA3XWJiGmvGs1kdJihFlHc7INA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=UO_aKZ8bMz3BnHpahFjZ2o71LMPOai5NbTCeccDhfuSFxarSqIv5Z4wHFAaRHetIt7XYr4mFwaZrXGAhZthDUUTsVTEpCIijV8i_rqa42F3dGY-MgM3GBmyD3dh5qg3JXyE8sQSvaj6e7TY16KyeRIDSM5R-T24X463Zi1CdVILOU2l6oEQrks1rMbLDNTRQc6BIqHAwNTh45J6rPS1cxnr2GlL1cesGXQTZFyiWmgcS9vKQh0o_HyPg45BLn15oUZdOhv64yD6w1pcaKaSAlVhq-LV1myiRs248ze3DpUE-56PV3Fo0gdN0G4SyKA3XWJiGmvGs1kdJihFlHc7INA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=oVKMcPIWkfbQHYuhwFM2u2fw5sXsLzpabMMa4u7Lm2J8ClQyXMX8rpheRZXE-hRAe9JMJY2-8Wng1dVPYSPcDTjyhap_F3OSdr2uqGLysLJ1byc5NSETk5BWH7KrsSdwjwyG7jRrOC3gc_NtOJn-qvzJAzPk78mnOgOOCi9m6Ze5sgI1HtD_uLdJvGBxMChjw1-FiNER08vqTnHB7HgOjOhslRwOjU1Zh5K6FQP3y0uxFCq1k9902eCRZO6tv4Hi6P314v3_oMFmWNPjMBJ2U1Y0OU71618BBaFgIRIkG_R3B9Sd4xmnEmMMBPJhYfozv8VOzlu6MLSSV_94omiSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=oVKMcPIWkfbQHYuhwFM2u2fw5sXsLzpabMMa4u7Lm2J8ClQyXMX8rpheRZXE-hRAe9JMJY2-8Wng1dVPYSPcDTjyhap_F3OSdr2uqGLysLJ1byc5NSETk5BWH7KrsSdwjwyG7jRrOC3gc_NtOJn-qvzJAzPk78mnOgOOCi9m6Ze5sgI1HtD_uLdJvGBxMChjw1-FiNER08vqTnHB7HgOjOhslRwOjU1Zh5K6FQP3y0uxFCq1k9902eCRZO6tv4Hi6P314v3_oMFmWNPjMBJ2U1Y0OU71618BBaFgIRIkG_R3B9Sd4xmnEmMMBPJhYfozv8VOzlu6MLSSV_94omiSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VKUOGj9U4H0dZL60_5o_jIChV9vSLhgfe6ugxDHbyNlNMAWYaJC0lSmnH0AQj5iw48hOaq2VW6eeQHYQ5ArjCFHhQv5rGyhA-ezmhVnqIHtytbfFshqqWUAFZToHHWU2MgoITnxzWryN-Kyg8mh7saR6CaI6-_SqaqqZplSmqZOsvKak6r0NHSxDt3ZwOdXIEJkol9je_YBYacOsqh5qn8AVxwr-do0fEd9rqU8Ye5o1EJKoWGMKD-rcRKzsi3Do7UTH07xmm5bu38GjhsLEuTh4BqSuC4YZHwZ6Cyc6_zD7FKNUf8CFxr2Ox4x2BeB063pAHI_w-YlwXMBcqRjmNgXTULL2DGGuZopRQ0KjHGjvgAEsS_MOZ-wfWOR4OeUkC8YDH3kShBrhk8X1vAdaHxP3-InkN0BvLAxF9-kyTa2YH4XfgENzH74_qwI7Nb4qfBOo_jVhd-fIfltBlcR-E69r1Kzl2a5krpynvi38lIie9VdJdyjFeq6rnsIFj2Kj__RoinZseyKMuM9dzpps7wcat9zTbpi_6Owpns5KNnDFQ5QDcORgpOpTRS67GxM-WKsUvCsR0aFaLMnQqB_BUNZKrbbJFSeFWHjf54359ieN8itlK3g99JJbIF9cCneuJYsiM3cw6DUUxAq51P_RsBdYbsMA8Bec2SRlqmN3CGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VKUOGj9U4H0dZL60_5o_jIChV9vSLhgfe6ugxDHbyNlNMAWYaJC0lSmnH0AQj5iw48hOaq2VW6eeQHYQ5ArjCFHhQv5rGyhA-ezmhVnqIHtytbfFshqqWUAFZToHHWU2MgoITnxzWryN-Kyg8mh7saR6CaI6-_SqaqqZplSmqZOsvKak6r0NHSxDt3ZwOdXIEJkol9je_YBYacOsqh5qn8AVxwr-do0fEd9rqU8Ye5o1EJKoWGMKD-rcRKzsi3Do7UTH07xmm5bu38GjhsLEuTh4BqSuC4YZHwZ6Cyc6_zD7FKNUf8CFxr2Ox4x2BeB063pAHI_w-YlwXMBcqRjmNgXTULL2DGGuZopRQ0KjHGjvgAEsS_MOZ-wfWOR4OeUkC8YDH3kShBrhk8X1vAdaHxP3-InkN0BvLAxF9-kyTa2YH4XfgENzH74_qwI7Nb4qfBOo_jVhd-fIfltBlcR-E69r1Kzl2a5krpynvi38lIie9VdJdyjFeq6rnsIFj2Kj__RoinZseyKMuM9dzpps7wcat9zTbpi_6Owpns5KNnDFQ5QDcORgpOpTRS67GxM-WKsUvCsR0aFaLMnQqB_BUNZKrbbJFSeFWHjf54359ieN8itlK3g99JJbIF9cCneuJYsiM3cw6DUUxAq51P_RsBdYbsMA8Bec2SRlqmN3CGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VSL7FtqkGCJB9_kjh_c40jnR6fUxDjioo9N78KjvUXKm64v0jYmzIeXlyCY0zdcUXK6Ykxgeg5u0cUhnyYKn6SvELoFEJO0dwLfbck4Jwa8guN9nNrFN4Bqegw9hZeFiioTqK5zKO6W0oFzButc0QJINz8ly3QYjueySvAROgMhAgnkJ-x30Z6lB7MraBFzpKfETf-62uFWiGM-0nUTHNLcAVEAQKiEMiGjQf5gB8LIyxXe_fnmecFCU78jSCZDwtC3mbLgag_re-8wz0KMWH5nR1j2T8Gd_r0FozIPCvnoxISNeOUGhkTsyjLhs6eMdtuOT-7-J-xL21SE5um7mpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VSL7FtqkGCJB9_kjh_c40jnR6fUxDjioo9N78KjvUXKm64v0jYmzIeXlyCY0zdcUXK6Ykxgeg5u0cUhnyYKn6SvELoFEJO0dwLfbck4Jwa8guN9nNrFN4Bqegw9hZeFiioTqK5zKO6W0oFzButc0QJINz8ly3QYjueySvAROgMhAgnkJ-x30Z6lB7MraBFzpKfETf-62uFWiGM-0nUTHNLcAVEAQKiEMiGjQf5gB8LIyxXe_fnmecFCU78jSCZDwtC3mbLgag_re-8wz0KMWH5nR1j2T8Gd_r0FozIPCvnoxISNeOUGhkTsyjLhs6eMdtuOT-7-J-xL21SE5um7mpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ONcP9_Ke3ZEl64hfGSAxogPpjJRJvSNFXk_jnTnK_c5QDHSMQlYnKQK-hg07jfqj7c8p7teIh7I5r1aXLFx_-8ngqwL6Dj15VGa0l0JvdZreuOW1aJEyn1zuSxSZflBSs7GaOV2j-ijGyd6dKm8n5rB2d81mQFHTbFh_RR2-ZdyampDyZyRDoglY5D8uWsbo67PUpQ1bEpIoGAmw3TZBmtQXZmXJRAAjSIxKVfG1ey13YiRQZspC8wF4i8zVhYYHJhHYG8d6ZmNBC11hFELYLROHo45aQ8cNHlS5ihYtkzvfXdmMMqX2bpJjMXXD8MYONRoQOI6otnmUHlpP4PfX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ONcP9_Ke3ZEl64hfGSAxogPpjJRJvSNFXk_jnTnK_c5QDHSMQlYnKQK-hg07jfqj7c8p7teIh7I5r1aXLFx_-8ngqwL6Dj15VGa0l0JvdZreuOW1aJEyn1zuSxSZflBSs7GaOV2j-ijGyd6dKm8n5rB2d81mQFHTbFh_RR2-ZdyampDyZyRDoglY5D8uWsbo67PUpQ1bEpIoGAmw3TZBmtQXZmXJRAAjSIxKVfG1ey13YiRQZspC8wF4i8zVhYYHJhHYG8d6ZmNBC11hFELYLROHo45aQ8cNHlS5ihYtkzvfXdmMMqX2bpJjMXXD8MYONRoQOI6otnmUHlpP4PfX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjWxHy0noa6YQyb1z9qECoD3jnjK7TwfBlp27k_WloGoGQTPOdTHcuwlpj0_ncN7aqKsZMdyf6_8pmMW9YRkQ65PVtqeE2dlOQNAUrJjE-fc45nlbLk1UyUtUHauOJsvefnfjpy2aHwXsFbccZCUF3TlC1S3Qj-uz64h7S7YHBoL221zvY7BJRlY_ppKPY0DsK0IkpE_s6Ya1_NQDJjqSMvcXtIgZ2NEhkhnXBWU1wFCZWRqcZBRMWCZ2waK9n6o4RRuratz04EtOvj6oGzCP4RILOpl2I7PBlLkok7q4QdCQ8rJJVHON5upz7RBMg8tc44Hlb00UCllYhbhnJEIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=vyFY-fRXad1LM3wzdqhiWTn0GwQsGH6nuimYc_VIqy9s6b6EBLImxrLHaC2j-vv6jlw3L5lIFZdJV2afHt2dCkHtaMsu-oXlyn1i_IA5tza_-teejPJiuW1xrC4dR_jbV9CeO4RvHPdMxQwgFeCjHpSUGP1mjlCl1dLH2n1RTwnP9SKHgxkiyLwRTzDLxQuDVmnegcN26UzLqQnQ6fbbmdsqfIFaW6ZunD4j7HjJp4FVo1Vw8ej0d7UCT-pbHwcGpvg8KExnjqEp-BnKP6lp69cxRfrGj8DB4yUvyKsNYfNLQ3dSvGnlRNNvsUxze1SL6w3rI5X3IwfnlyqPhdgwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=vyFY-fRXad1LM3wzdqhiWTn0GwQsGH6nuimYc_VIqy9s6b6EBLImxrLHaC2j-vv6jlw3L5lIFZdJV2afHt2dCkHtaMsu-oXlyn1i_IA5tza_-teejPJiuW1xrC4dR_jbV9CeO4RvHPdMxQwgFeCjHpSUGP1mjlCl1dLH2n1RTwnP9SKHgxkiyLwRTzDLxQuDVmnegcN26UzLqQnQ6fbbmdsqfIFaW6ZunD4j7HjJp4FVo1Vw8ej0d7UCT-pbHwcGpvg8KExnjqEp-BnKP6lp69cxRfrGj8DB4yUvyKsNYfNLQ3dSvGnlRNNvsUxze1SL6w3rI5X3IwfnlyqPhdgwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHdpff4wQqi2h4Yk9nJ0Bg9mJRk90x__vgzxXnv6ow67wS80c_HvANhhPlnGdSeey35TztXWI-ytg0hqjOfN4dbg2KYSDbQlqxqO2WFK35Qw4Y9Rjo9ZDYCRFV0Me09b8eyzwplJe8ITxxkzHmvEyPjNw-FNgU69id54YhhAG8FOBx_ly4-VS-b4Rv2gWxWoXIWclHDxqLJOH7PFp4jdNBcnMdJymsr_SSLdgy-_6idPvP-8KyFirE_FD9-CcspI60MqtIiK1RmF0TBQXKcaFAyhZeXBsI2SeYzHX8n3zFBwKcUU8o7n0Em2v6G9OJYdTlicddAFKG_LA4SqJT4vbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww7nxS5RbE-hd7BBFnXYPgGftMuEjuub4FFW6_Y9bvf8t3m-eCnpyPhcaAXe2JjnaCKCzsHoGewVEDC8aKVqg8CzG2qhLBBjefNXIWX0Vz3rHocK5NIPYw-0zb4iWTdJhi1paLTBYaLO8n2D3M5FtW-utzU0MBJ2k7Na22r4sOpp7etpJAq4d8y_9PgHRFy56GBrQDbNpsunZsnDB0oVsqUYJ9OvJNADwCC8KfO1SHcKliFYUNwnk3wZjccsmp2fb6BCp-54ABUbhwsFun1FvD9zo06kvc8nG7dY-au9jLV8CXIaTFjpC-ZzMJvyJ1lbNtXHoZzkiPJMcwgvjmmHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Pn_x1_URKcEOgIH1AuuUzIQPGcsk5hEl2X0F0o9WoKx9ZaXkArfGtgHb6Oe3CB7MgtKDE8zA8mnw_G-mkUrKrDeQSX4D52-Uz3wpG77Co_9ZSfqlDldbQGXi2unaLvQJP1xKnW6e-aOeZElorTgfA3_3-MFed7MSSWg107BSbnBrq_pSJgvh3pMefAK9mPs3GZfckZ1QQbkUSA1r3wMYvZ_kFGN8vqBuOLHid2mD7GwIU3gEnRepPQgS01VvGuwJObK3PqPUnM6adbNxfUseMBIO1oOzjStKpUXfbUXeDEqP2-L2c9b3roOrWIT8EFCXzAy8hcvi8NhUNOfKNquauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Pn_x1_URKcEOgIH1AuuUzIQPGcsk5hEl2X0F0o9WoKx9ZaXkArfGtgHb6Oe3CB7MgtKDE8zA8mnw_G-mkUrKrDeQSX4D52-Uz3wpG77Co_9ZSfqlDldbQGXi2unaLvQJP1xKnW6e-aOeZElorTgfA3_3-MFed7MSSWg107BSbnBrq_pSJgvh3pMefAK9mPs3GZfckZ1QQbkUSA1r3wMYvZ_kFGN8vqBuOLHid2mD7GwIU3gEnRepPQgS01VvGuwJObK3PqPUnM6adbNxfUseMBIO1oOzjStKpUXfbUXeDEqP2-L2c9b3roOrWIT8EFCXzAy8hcvi8NhUNOfKNquauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=YI99D0Ir3EivKcB264piQOV7xtJMBQ2-4UzMTWGIQfDNj7j8nhFZCGS4b4jrhmd78SP3jZ8_ul-fXVRK2HIS544IZCZyVEse1ZMOvllSX4N_GRIp5zwKXosCYk32QFPpEQeMDpxkvE1LGHOa_SQY94Uq0-KNeLspsLHL9UMFcNLLA8-p_9SkuXRjAuAdWMrf9cDcvNv_BkDb37zQKMMCQoe1T7tu2RmXBbSnvzjZTPbvZxgaf0vWms4FCdTymesyiSyqGLq1pxJ7SDmjA4iytRViH_vC7AVooaIszmw-z-E70r2g51mjXc5Yi0AoXmRJb8jHdx2CYKVvHiO7aU3SDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=YI99D0Ir3EivKcB264piQOV7xtJMBQ2-4UzMTWGIQfDNj7j8nhFZCGS4b4jrhmd78SP3jZ8_ul-fXVRK2HIS544IZCZyVEse1ZMOvllSX4N_GRIp5zwKXosCYk32QFPpEQeMDpxkvE1LGHOa_SQY94Uq0-KNeLspsLHL9UMFcNLLA8-p_9SkuXRjAuAdWMrf9cDcvNv_BkDb37zQKMMCQoe1T7tu2RmXBbSnvzjZTPbvZxgaf0vWms4FCdTymesyiSyqGLq1pxJ7SDmjA4iytRViH_vC7AVooaIszmw-z-E70r2g51mjXc5Yi0AoXmRJb8jHdx2CYKVvHiO7aU3SDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ChxuREDJGuVY4vvstQ59A7LG630ONhQajhWXXuLGma7jVOZMRktYxx4vjitZ3NcDMy1jUFMePeqThnfVYdYUICXJVTOR2LWr9MGmCDSZqAuznUaQLQnF6Iw4punJgc1JRzIxhrVVpxeWF6uUqeyTo2iJ88_JJwTz7lCS5L4-SrJ3fLFG25Hwy-e2PW-10F_dc2i9u1CqGEq9Ifma9X_a-geOcVWperDbRKDLawJX9hvHqM76Cimi5ag3ahHQSsM6UqneDz9NHuPIfa6dsSwHMKc1tf-eSMY6D-AqWSPBsOcMcaldkarQ672Zfyn8Lvrkeo3R4p9_eE3GbZUQIH8F9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ChxuREDJGuVY4vvstQ59A7LG630ONhQajhWXXuLGma7jVOZMRktYxx4vjitZ3NcDMy1jUFMePeqThnfVYdYUICXJVTOR2LWr9MGmCDSZqAuznUaQLQnF6Iw4punJgc1JRzIxhrVVpxeWF6uUqeyTo2iJ88_JJwTz7lCS5L4-SrJ3fLFG25Hwy-e2PW-10F_dc2i9u1CqGEq9Ifma9X_a-geOcVWperDbRKDLawJX9hvHqM76Cimi5ag3ahHQSsM6UqneDz9NHuPIfa6dsSwHMKc1tf-eSMY6D-AqWSPBsOcMcaldkarQ672Zfyn8Lvrkeo3R4p9_eE3GbZUQIH8F9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhzadTiRas-OIgKQkkxIlQqvrBQp7wYN3KaKWOr3o4UiMSPhfwRM6jOFXsb5-HZHk_Utk_BwFq7I94q6jPDxBbWXEFPUHFaDjS1JmbTMQ59sh94c51DLaJ02NjtKhNoDS_91mhhQCzax7fsBYMT5gKKnbafs7GLDFcok6vxZWiGV6z1V86TTMfBTBy_UDWdlGgI9DG_A367Ovh8aO_4GEyucROeWSdYkiyaohNYTr0XVU95kFw1Brikk71bKqbP6SqN5QYUlgij1PclV3B2ImiYo91jMEcWSOLOdH2_rKfqz1Otgkoxk-Z1h0ujRDX0SzlsOaggyGCKN3NW8_cyP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=jbJvu0IpU7cDOjF3ljQUXkjgnepAulZ5Wsi0gS3HI_o51kqb4p01u0mNWrowBLipIKT62elHx8LXTieAVt77MIhd5gZRK1w4aVTuxMb0FJjejYX1SjoCli0I-uJHnkdmnP5u5V5SosaCFu1uNcsHq4CC5HNHOusN2dyMGEI__DveNsn5Q1IfvWdEZ7EVTaZgtV4YK2Lk_5FFPrnBaeqfWnhZLFwPlJuGPHHW6P0OKxakRZtgDRFzjTBNc4BaXNDHYqLQZC1vjE78AttxpGcwVY56DlknaTtrstciWoN4wFZJgEt0d4u8o5gDRAf2zN7MRnEmF1ZHj9wRhckaBlw78Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=jbJvu0IpU7cDOjF3ljQUXkjgnepAulZ5Wsi0gS3HI_o51kqb4p01u0mNWrowBLipIKT62elHx8LXTieAVt77MIhd5gZRK1w4aVTuxMb0FJjejYX1SjoCli0I-uJHnkdmnP5u5V5SosaCFu1uNcsHq4CC5HNHOusN2dyMGEI__DveNsn5Q1IfvWdEZ7EVTaZgtV4YK2Lk_5FFPrnBaeqfWnhZLFwPlJuGPHHW6P0OKxakRZtgDRFzjTBNc4BaXNDHYqLQZC1vjE78AttxpGcwVY56DlknaTtrstciWoN4wFZJgEt0d4u8o5gDRAf2zN7MRnEmF1ZHj9wRhckaBlw78Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=AbZTVrZohj8U0_hjxf7tvMbjrWD1IHnJUcswSasnCw6UZTf7fH0urnnEItR7yHZJusiPQpaX7QL_9BwQlZ1hp91HWJK7x8sntqPmyarkKCsUv8jpw7IPIvEYRFGCVqN2EiKQkbSCVsP673BMBAz_TWRxRo8Z-fVD-uSZwUbN_kmBFSGdfkd8Dvm-c2aFd7kR1XJoWpdyQpFPy_ojoaoV9v8ZPLll4wGGbP-EfeAn9QUBngfKK_uE-xM_1AezEbGkEsZXaMie9NdatXHSAkbg7xEQMqG7qb1yum13lrBTSmQPV8kVA1XXKadtv_8lsW3T7uKHvaYGrGwA62VV2rQ4UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=AbZTVrZohj8U0_hjxf7tvMbjrWD1IHnJUcswSasnCw6UZTf7fH0urnnEItR7yHZJusiPQpaX7QL_9BwQlZ1hp91HWJK7x8sntqPmyarkKCsUv8jpw7IPIvEYRFGCVqN2EiKQkbSCVsP673BMBAz_TWRxRo8Z-fVD-uSZwUbN_kmBFSGdfkd8Dvm-c2aFd7kR1XJoWpdyQpFPy_ojoaoV9v8ZPLll4wGGbP-EfeAn9QUBngfKK_uE-xM_1AezEbGkEsZXaMie9NdatXHSAkbg7xEQMqG7qb1yum13lrBTSmQPV8kVA1XXKadtv_8lsW3T7uKHvaYGrGwA62VV2rQ4UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=WAKTXx79tsbOUXGgsM0sN4aq5UdD1Iz5QHNJxCv8PW05Ef-dfH45esXDIYERm436aLVlBqvboIB4b6-clvoEVcVZQzclIiO1aOe9fjI-DIhNjAo1vcKHXO0EWHbkgrAI7Fh5Ml8LtXcORwear1nvksw6Y_6absN4cU4Q2xHlsk_rjcEkQtpHjiPHK5bsTWvLtiJfHpMevJLWDVg0sRbjcaAiy57NnueKV3xABxf_N-wIQ-kjggsoVo74MciqhNXEFMxrPHHfY7Ju1i237NDio03V2TrxnnqP4eywdNqVqXgonnH4sqMagknDCdqvWITrY3hWKcesx0AtpzHA1ubFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=WAKTXx79tsbOUXGgsM0sN4aq5UdD1Iz5QHNJxCv8PW05Ef-dfH45esXDIYERm436aLVlBqvboIB4b6-clvoEVcVZQzclIiO1aOe9fjI-DIhNjAo1vcKHXO0EWHbkgrAI7Fh5Ml8LtXcORwear1nvksw6Y_6absN4cU4Q2xHlsk_rjcEkQtpHjiPHK5bsTWvLtiJfHpMevJLWDVg0sRbjcaAiy57NnueKV3xABxf_N-wIQ-kjggsoVo74MciqhNXEFMxrPHHfY7Ju1i237NDio03V2TrxnnqP4eywdNqVqXgonnH4sqMagknDCdqvWITrY3hWKcesx0AtpzHA1ubFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOonW7rejHnvk03LvQfKf5OkcdSUECn2yrFJwj7jYUAH4HlLZbJ0jzJXANl5vWp8nETHhk1f7FFvEX2JRiFAyoSCfCEmdpAWpB4y90Y7mBGjCFWrYPShaMITfSt_CCSN1RH0jg4FVNgM73RCbyVjY-dN0NE3R2uyAJQGKb3f0IUDT6pgw6SOuwpPUbgYIN26-ODkfQjMwj2GViwUbweRA2WTgkHqQDqEf_bjrvZLLVhYaX9PA0REbfhtU9rZpgBmNAyPSEpi7px9GHstySdiBA5VQxj0fg5G2YM1awpIJ2q4UZykLZvLdFgusm_GSzhtiqdnnEA-XFb2a7hRHQm6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=dEDcWAMRUXeIFLj2nO88RKf8aC7Q1kRFVSDrJn-HShI12kCW7WyT47A7CTGkl0vGJ9Po-hsmlEtXN_jyflkE-YBVv5pR7AMmWRG1jB_CNHZrcKvAzTeoqz4KN0iCJZ2I5OqgYQ4JcvHDZg0xbnBxVEzdpgHA6CXgWl1uSJ5yU0PZTQulBtWP81CwIDFh4T4PstHo0JL1D5GeByo3Ol0yol9a_8rgfU4wE_UnsDAUz2Iht0OZKGtSwj6o5-4HvRoHelz-Y2c6tRLcsQ6pqrVElQVcSnsjmxDjRCjALeqReEf4qlEYVNOw38c2Sa8iTEhQ6jrSC80j0nmOvfl-qIaN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=dEDcWAMRUXeIFLj2nO88RKf8aC7Q1kRFVSDrJn-HShI12kCW7WyT47A7CTGkl0vGJ9Po-hsmlEtXN_jyflkE-YBVv5pR7AMmWRG1jB_CNHZrcKvAzTeoqz4KN0iCJZ2I5OqgYQ4JcvHDZg0xbnBxVEzdpgHA6CXgWl1uSJ5yU0PZTQulBtWP81CwIDFh4T4PstHo0JL1D5GeByo3Ol0yol9a_8rgfU4wE_UnsDAUz2Iht0OZKGtSwj6o5-4HvRoHelz-Y2c6tRLcsQ6pqrVElQVcSnsjmxDjRCjALeqReEf4qlEYVNOw38c2Sa8iTEhQ6jrSC80j0nmOvfl-qIaN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEBbiFw6CZGVPnOYdeluwt5M0wE5jvILivqyKlHfnX2ftJ89Cf9yx_LiHJ3l_RPlN7HGY87ktR6LjGnpJ-O2YVluCjJIXoCCPDbp7bIN6rnVLR3din7L_HdN7h1EXkWkAdqxoo50E8DJ4LsrnB0XtFZnC79y92mef_tvhdfxAJY6EjipIsJZ-hEHIQcSjiSElHkcEpj-FOYcMD8pS630BYjjm-_REj4N6nBpK2LqsH_YIax6i5KGTOzCKtU6z5bVlC_ckotdVBTOHZjIUJWTiAcvMwWP2H7evEKDwxttKI-ACibEf9LUQn2mGVZ10zqHGDkjPC0s-XeVS6Bh8SJHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=CKovms0W5x5Bmz2IIKPuK0avV-wtb5BE2ouhfo1Eew2sdP4dtGptht-Roqn9riupXaDiXS3F8wUV0CNbI5pH5XFfQtvldDWUnhnd8xag4YmumhHAEgtp0HIWBT6fCQ-li5JZqS2A28XtIPxT-1gZFOVCvjV4hgN2-GZrj5Wwbw5CIkg0LSUZkg5jH9rm2pr190vDXriYs1jWUpQ8fyWX10OZuOLf-u2OckUHt_idyW7EIB5UPfmarpr85OhTKGJ9GsZR2G6IxpzjYqr7d_22HToxaDDHqwl_dZKjEam4Gon_gNl3c1LXw5W0De_pqyqe1ROHsOjot1psYcy8nahing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=CKovms0W5x5Bmz2IIKPuK0avV-wtb5BE2ouhfo1Eew2sdP4dtGptht-Roqn9riupXaDiXS3F8wUV0CNbI5pH5XFfQtvldDWUnhnd8xag4YmumhHAEgtp0HIWBT6fCQ-li5JZqS2A28XtIPxT-1gZFOVCvjV4hgN2-GZrj5Wwbw5CIkg0LSUZkg5jH9rm2pr190vDXriYs1jWUpQ8fyWX10OZuOLf-u2OckUHt_idyW7EIB5UPfmarpr85OhTKGJ9GsZR2G6IxpzjYqr7d_22HToxaDDHqwl_dZKjEam4Gon_gNl3c1LXw5W0De_pqyqe1ROHsOjot1psYcy8nahing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsUMAlGUmRMk63bKj9SRbgxvScCOsOPqr5mngKR_a9t7_8NqndUZmpd_vaOB7DHIe7qatzsfrqoVmclsSSMkgjJFtf0AFF_A0XRg-fs7qVXvVCBGi3zXvYlbrmA1H3V4iToXZl5kN10fYzVDL4iZgJKUsfYFsxHcU5rB_ElFKNienXJP5ksznPM8HWyhib0nZ-fUdiZJcDJ9KdhDQDjxvPboWGK9JF2pnVjybg1KIWWxqHpQTs8vwkh18ycPmhey3erCSGPN3mdwuuzlgikOzWqwjVWKoop7B2oGa6bLZEYY2j9M3n_5AM3cxy2oSy8x_0gRyWj6GCoCTIEqeKYhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=jcNK0JZZackxa-7sCB1XieKY29l1xPPbQVRUBpajx9QxOP45mDKRONC83_rdq2IE1qnRBF7lUgBdGQspwx4mclljpwCaEf7qHS9Pqstpkj0-tBXEo3TqH7HY753mf5uKe7ZpO7fxou1Yb4mcZwBrbmurpooX2A8Hv4n2VwJdo3G-3-JgdNU7rSwiO7NyKNiuWGQd-3e8JkvQSz3xziFC0xh766F-lwymIjHTnpqhoFRNg5pDujY8WdUCuEkygXRXbUXVE4TsG-SYXbfHje86NXLnM_5zUT8_ujqPYRulMO8DoIVVZ42srgHm0L6eGK8eOYJ3MmkzjOjvqmiu3rNQYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=jcNK0JZZackxa-7sCB1XieKY29l1xPPbQVRUBpajx9QxOP45mDKRONC83_rdq2IE1qnRBF7lUgBdGQspwx4mclljpwCaEf7qHS9Pqstpkj0-tBXEo3TqH7HY753mf5uKe7ZpO7fxou1Yb4mcZwBrbmurpooX2A8Hv4n2VwJdo3G-3-JgdNU7rSwiO7NyKNiuWGQd-3e8JkvQSz3xziFC0xh766F-lwymIjHTnpqhoFRNg5pDujY8WdUCuEkygXRXbUXVE4TsG-SYXbfHje86NXLnM_5zUT8_ujqPYRulMO8DoIVVZ42srgHm0L6eGK8eOYJ3MmkzjOjvqmiu3rNQYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-CMVwcQuY1uSVjz5YOzblFHhxaUDIGC4RasocLY5-hOOsvfbWntQQz0Ueo8dacL1ygkMgOuJrp_dmrXvY7IZSPcswXf63nh0n4CkHNbrs1XDmzX8PxYUCmf8hxWfXUpfQQ7gCILyHsEatAYWN9qpvWidL6R7kbwX8Mem6kuOxfdNxhSbIL1jQf1ewuAyTqF7Hx5x-Q0VbqvcxTdIohRUFOF9DqxQpxionQ4L0imoG6V9iP93RffJq9KzRORJ0u2jrNYL6eXMyWM9M5WMDgq4qLWTkNyE_rpEY8D5rIk6awrkgNBHxBUudVYFCSkln7LiNANziIIJtT_tlmbz0bBiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Ul1duYmbtvZIcSvvTCBS9MScHgaslu-tyr9Ff1J-GJfdtDKXAW90t2p8VndR6KrQecS9Nup55B_d5fq-Hi1giqNSCTIV8NbcQh4-zpXqZ7gv1R6zCSvVcHo4VRZybb3MgaBB6P38tb9eUnQiY4KxjAIasDYtmuC3t4n5LnHXLS9Y6BNnd7IB9IJHr9FgdKcPsXZBk68dLT1AwQMHS_J_Quueg-NK4IqesMFcRyL7kUYWl4Rg3O9_5aT2VOQszyntOHN6YmLQ9v5V4qGNdq1UUgLFpUY9RrtFFRptChEiTpY1CftY3QSydWUFUQaMxctajYDmyytAOi0FOX-ziemA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=fpxvGFh_QQlCuD9yrxhG3jm4eA4kjCmDw56Bjl65LYoxvudZvGW9mYlAIs_QyOWuQcrGCxF5E8uOLlQGyG7IjeyNxdbodE3-4jtQWSIQ9OBzfBy8hHoMK9laLW4sH0PHseF5xK7T9SwSMH6Kp9NGUMvv4l3JLWmNc6NAJ-JNpKh4nDxkCUBQ112FAKGaO3I-dFtRZYofDprfEgMtNhLjLlrj3zWoFFSVKqM-XHI9c7aTYw9MHypjOfdkMmZ5Mtf_M3pdikqxOGLUq1CB7pnWf9VQyr8zf0-JyZLLjXtrdgp9PoSmbBI0VQ68-YAbchqFhTYevpv6Ga2YopMWP3AUYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=fpxvGFh_QQlCuD9yrxhG3jm4eA4kjCmDw56Bjl65LYoxvudZvGW9mYlAIs_QyOWuQcrGCxF5E8uOLlQGyG7IjeyNxdbodE3-4jtQWSIQ9OBzfBy8hHoMK9laLW4sH0PHseF5xK7T9SwSMH6Kp9NGUMvv4l3JLWmNc6NAJ-JNpKh4nDxkCUBQ112FAKGaO3I-dFtRZYofDprfEgMtNhLjLlrj3zWoFFSVKqM-XHI9c7aTYw9MHypjOfdkMmZ5Mtf_M3pdikqxOGLUq1CB7pnWf9VQyr8zf0-JyZLLjXtrdgp9PoSmbBI0VQ68-YAbchqFhTYevpv6Ga2YopMWP3AUYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOHka8JMeM6UerralNxgWGE_QTYZgpy9kxcNnRKFQIItndzmUC8ITlNnn0ZDSwghcO5Qd8NFMhuSjnb06uc6WqqqEPKq-BG3u9nYXZYFcz59LmHolOasAhHt2P9LqWNYlCb-axi_t4rj7V14zDI7Cv2MjgWZ6lBAWVmkfjwdHBwgSd6SubMCxDXGLJSQYdGBhOwAIKwRpA2l_zngdYREfyVhwDV42M2dY2h3jLby73Bd6IBLIq7Y9UWlRkyEWQ1M03swMrhf9uRWzNBpq-_3cxKoC7vqQz9mXvZW0F9EBlrHdaFZmnZzTS1JV3e3NRXbhMLQk2TULLEoRwNCsXuB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRY6B9dIcdN7R-FN_qWn_Sqyx6bTAjmCVD5TE6pqT6zfnaG83ymkAruFECnKtO_3t0QYLGouKX4ttP5-hpSLuIxFsATWdpKh8toONEF5vvQUYQqRamsB0OH9U-If7KfRr10ktmNnDj0okJFHhRz-sP6ZXpi-YGhEOtPdda5xVMxyzY_Fk7xKdbsnN19KLRGFiVLMqTU7ID7SU3uFky6VSEK30GnXCpj7TJVQeYeUtiz2bwx2vPdYGp8L14jw_kfP9YZV7fMQnC6arIIBtuWmCpaQS4kQ7YHiISp3zkH-jiNzCry8jCcMCUmNiAzQhf5RjnMbtglI0DHfW2FILpIUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVMZyWrtPgLcXnt6Tz2A0erKtLLQQRkJx0E-KSP7HiDaH9MWbfZh3swNYumxNbTzkEV9ost1st6DOYVjZ5a6-sankXJ1gChMIXV48G4I-GR00OmKPNikoLDJ-Vo1eEELdpc-t_gfIRv8tf-RUnv7KB4NOzCEr38y6HjFJJHsxuSqtvm9OgECheFQA6DzDTybodsLeY3Z0i6l4ibVIEPCh9CNGQWPHf9hppyTf2V61PRhKx5RznfOAyUTlE7OqFwhPi2PhFxHrnXxIWJv4lzUZ9uf4WYrubjrfHnUa9oy2rUlGKzREvwAZDKUKN9IxKXGAiO2Vh3CZxZ6PPWMxeYIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gymkAt62w9i7_vssYKk5oA2UOiBrB2W4Q-tbq2w9PVk1_ISAH97mGjlKUkbFg7nc7VypJbY0zRzHWIz9J8zPN9ghW7vLVz7jy8rZ-4pl6VZDYZ_j8SFOsk4IY7-3555Az1nT9H_zQXgQaJhHHVm9F-u5QiwcYW9oZV3rztfEIww1MvxdAXxhVSjBYyazG6ugxE-LTl1Z1P3j1OqhTiqL15mYa2bzlhS8U-4lAyKD_wAfKOqRMT1b9iX5lrawXDAFRDgOrHp7O3oJhmf_rGzYfDwzeqVu6SmdTsnkApJeMtSsjzInf-6z7Up21IqDdy55f7c-B7MsUIRckekS4Z0l5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi2wWagqQhQZe2TzR5hzFze0uygq9HWri6uwaBrN99JgFudidIAtCCYW6UHmvngVbPXNiwMTluC_tO8Hf8hy0hdMBCxG-44mL0zNH5z2v7al7i-87tq8a_eI9yi2c1Rp6ZQjP0HAcZFQa9lM-35FZqqXc3Bf2qJs9Mq1SiAtdkwGmPSYZ_4eaJwnumtVCH7-KsJqia5B0iosCIahttpN8o0S8SyydcTOtNHKPsAVvC6US8MJBGG6CqdiolbHREp8PRjWlunFHzavpOr8HEozI51SCywCK2fhlgAX8mSVE5-ya9D6yxLY9UdbEeTLTN99LOpCfdYlWNNcKBzBea0TKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=HggCwMoBoDhvC22knY6gTh-ssDPpw9KYZpYHPF8psX6FbGBEL2hTZ7y79opeFgAmK63u4U0GHt791ku0XjHSVQrYqbnStSgP3PicABqOwUJlPxsthMSC-7rjdpWx9Nu0UjEvsx_qFQltMkv88la-d19TXFGcFykR8tlbXF_hlDompt6dDYbHLN1Uw6L5WBsqcBK--DgNvjmJWxDOUMk_obGIElvSo2rYMsQMYkmbc4qyRxeX2c6OcGpwYrEwkGvsS9lkLAmq5N_ok5FMmls6w9ugNasjYKOurdKKhqL_e93oPaTP2wAPaQ-j1a8mVA91OeO3vZNsISyv2O2MJ2VcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=HggCwMoBoDhvC22knY6gTh-ssDPpw9KYZpYHPF8psX6FbGBEL2hTZ7y79opeFgAmK63u4U0GHt791ku0XjHSVQrYqbnStSgP3PicABqOwUJlPxsthMSC-7rjdpWx9Nu0UjEvsx_qFQltMkv88la-d19TXFGcFykR8tlbXF_hlDompt6dDYbHLN1Uw6L5WBsqcBK--DgNvjmJWxDOUMk_obGIElvSo2rYMsQMYkmbc4qyRxeX2c6OcGpwYrEwkGvsS9lkLAmq5N_ok5FMmls6w9ugNasjYKOurdKKhqL_e93oPaTP2wAPaQ-j1a8mVA91OeO3vZNsISyv2O2MJ2VcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=hpvVDVanCE1QTmQRHtZGAqz3v_qSEqqdL0g4jkJAlVQQoD_Ad7ExGQmnp4tZw5dywKmLOxVFAX2DujpzXOgMJMlfISGap7SJQ1N_WAIIkR0t0BC5c8Dv5EcwU_xpnY2Nf_okVY0DSlpFaJFspJUE5vPcl4wqheMvkeGBkhoD19ORdH3kbY8DuLaKrm2ydhzuOpIYZV6zr9MyRyIqHlSVfEmRtQhgF4g4BxUM6FkGMW5u4TfDCg-JMCfBZKNtquyghcJnvDLmNo2GdmrH79Tk_Fqe1tNYwtb2rzJFtJ30KC7LEfvV3659HyenLA5BkfKFKe4gcQaHhlmD0oCwUnHOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=hpvVDVanCE1QTmQRHtZGAqz3v_qSEqqdL0g4jkJAlVQQoD_Ad7ExGQmnp4tZw5dywKmLOxVFAX2DujpzXOgMJMlfISGap7SJQ1N_WAIIkR0t0BC5c8Dv5EcwU_xpnY2Nf_okVY0DSlpFaJFspJUE5vPcl4wqheMvkeGBkhoD19ORdH3kbY8DuLaKrm2ydhzuOpIYZV6zr9MyRyIqHlSVfEmRtQhgF4g4BxUM6FkGMW5u4TfDCg-JMCfBZKNtquyghcJnvDLmNo2GdmrH79Tk_Fqe1tNYwtb2rzJFtJ30KC7LEfvV3659HyenLA5BkfKFKe4gcQaHhlmD0oCwUnHOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=F49qO4RnIfQx-R_WTmWbN7FkSKMFSJDqQ9R64F1TS6POocfUBZN-Zav07xSDtF8L9igc2s8L2N6ahAdb5o7Xft1JVJgOW4jtRSAftN3pXD32IucNQBjzIj1xR3-wX4MkvvZrcFWMUs-tXw9yXTt0TLh1nk_FEhcDWytcyhlYUeR9IRBuQ5JzOTZkVY3bZ6R5psE7UqsDMdkekRHy2RoNp5oCtCOr4VNaOhrHVQkEDk0T3Sx9COYsA1HsK7kl_b3Gg5dj9bI4yfcK06N9sD7_kPwZ6ApjVY7X86BrjJQ70FZztFf6gLSkGeIkLybApdCm_hLDUhhhKuj_9-RMvvF2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=F49qO4RnIfQx-R_WTmWbN7FkSKMFSJDqQ9R64F1TS6POocfUBZN-Zav07xSDtF8L9igc2s8L2N6ahAdb5o7Xft1JVJgOW4jtRSAftN3pXD32IucNQBjzIj1xR3-wX4MkvvZrcFWMUs-tXw9yXTt0TLh1nk_FEhcDWytcyhlYUeR9IRBuQ5JzOTZkVY3bZ6R5psE7UqsDMdkekRHy2RoNp5oCtCOr4VNaOhrHVQkEDk0T3Sx9COYsA1HsK7kl_b3Gg5dj9bI4yfcK06N9sD7_kPwZ6ApjVY7X86BrjJQ70FZztFf6gLSkGeIkLybApdCm_hLDUhhhKuj_9-RMvvF2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=mi0LRdJ3vtrk0hmP8D6tBBIyggcP9DZcoMSGc59kzAU7OnecCQoSGihb7d-9KIMvJJwKrm0HHS66uz8kWGiYz6V7NKjAujnWW1sUAnWxvHV2CfoVICOuiYFswhbb32tvMJx6JimryETvMy20w0wcD-fCAQh4ynhtrRKXDC98g_3Nl7p2TGZpOOO7nL4mAH5YuvRQf_SbCpuV1EcWptZQ5-ejSnxLbQ2mSR6SKKAsuZ34h3IeBpGAzTokMlDVKP0ZEMiyb9PpNKZQAAE9g3cdonml5ZYuhW1yW5l7TbgsqDB3F_PVZfz_cDoxwMDbIscPE2yhORZvSkkYdl7wzmRG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=mi0LRdJ3vtrk0hmP8D6tBBIyggcP9DZcoMSGc59kzAU7OnecCQoSGihb7d-9KIMvJJwKrm0HHS66uz8kWGiYz6V7NKjAujnWW1sUAnWxvHV2CfoVICOuiYFswhbb32tvMJx6JimryETvMy20w0wcD-fCAQh4ynhtrRKXDC98g_3Nl7p2TGZpOOO7nL4mAH5YuvRQf_SbCpuV1EcWptZQ5-ejSnxLbQ2mSR6SKKAsuZ34h3IeBpGAzTokMlDVKP0ZEMiyb9PpNKZQAAE9g3cdonml5ZYuhW1yW5l7TbgsqDB3F_PVZfz_cDoxwMDbIscPE2yhORZvSkkYdl7wzmRG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAYu_JHZlzdt5OiBxvxXiATLcgho_54Hi56bWaBA5g2wHjTJag-YYEdWuxMvu3UvuNuXSyaiNkYovxk5TdVnPl2-2mT79Cbta1S2kJjNiKdZdexydmmZyuJS66gprKJfswrbiaKdtZesUcDrGCe9g_j9TocENBhennoQGlUapnz93QdTFVhXty2rS_jGaoJTYfME-H0YJm_3X9trKf8vqo1FkMqAa0HqdLDM-xuDupd-10-_64UyTr2DwCwUF5qTG_A9qJGt33ieBZAU-0sw7fDqX9k_GVdyY5CJpPhkA2FbkY_QVsNzIEB-b7ZG2IR6qRbdo8MRae2nx3gtXOoLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swyxEldw7ko66O0aLSaeRABtID6-VSfpprTxrQ7KfzduRXtZxOsTzCN2gaD1t2mVxIHUKN4TD7wlcMImnZamoAwLTpkTaq4942ll2WM5osS_DrkGrttvRd3YJ9K0Ibq-Qc89OLNHAps-LLbkgRNaHY1A6KhZrcIGw4C3KVYz7Rhqoougt8_BzxE16whgWDH2XkV0X-ifbT8745uX2EUhJV0deke78Ksa8BMrqpAZlHu4lBoPtqSHW7PIuaFPxpqv-jmONNQPAmreJWNN4TXycggjBN8bIOvfRKXqEkiGjfDsdRN8KO2lyOPBV27S4AiQ0kFKXO7ziWmoD2PxmISNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=fjujI6ZFzVEOd6Ne4X0dc0RI7gb8Xmb8DLvvhohEeiMX-xfzAu7ucvfUnIoEb1MamZscZ50ZpAJ5BScGF87gtHDonlj4_9-AaJuhyb9GHcg5oBV3D9R8sPxcME_Wg49y2c3ZUyaxpGsgcaVp-lUZGZDLomQs0NdiL8yB7P-EPMtq9LLbfL5blnmMY1xfIGxjdmeDAh7VqD_mKyxBJJUVnNfuoV4hrvrunjA9zDriNkoVqPYGO51wrE2978D1hnoF7Xg_cmJuazPR7i7cr08kEmzIiOWaxyiFGa58IgqoGPHrTGUYv_215LPBmsZYn_MFgyG103FIXVOs_KKFtw3UEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=fjujI6ZFzVEOd6Ne4X0dc0RI7gb8Xmb8DLvvhohEeiMX-xfzAu7ucvfUnIoEb1MamZscZ50ZpAJ5BScGF87gtHDonlj4_9-AaJuhyb9GHcg5oBV3D9R8sPxcME_Wg49y2c3ZUyaxpGsgcaVp-lUZGZDLomQs0NdiL8yB7P-EPMtq9LLbfL5blnmMY1xfIGxjdmeDAh7VqD_mKyxBJJUVnNfuoV4hrvrunjA9zDriNkoVqPYGO51wrE2978D1hnoF7Xg_cmJuazPR7i7cr08kEmzIiOWaxyiFGa58IgqoGPHrTGUYv_215LPBmsZYn_MFgyG103FIXVOs_KKFtw3UEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8EyLcGweGdSe6dl86NrLCESk0T7j0gfHqD1hg05br4XFsrCw0dhXxNxn7uvfp9x_A_Voi4s_C4GTgDnS-_EEQv15HEIFn9XhxnI2vn1xveBahbq32b5DIf1Eb_tQOe1GZSA_o1Q_RIOo1cW-6A0eUQSGXaUV1e7HY4ugM95MAHfmj1jT3wIVHId9yizCHdThnPw3GqxEc-1GRfH5Z1-00Q09qQG5SWrKc56fd6GwU-Ip-UTPDhYgVLmY3tM-l8TOe_m4wHztL1F58s_x5boLDIN0oetmM9I5cbYtKgB_t1JVtTHKfnMnVPWfJ_a919zwTPyR4n1K7_6XuI9YYrbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=LHe1DDRd4Nt4RDEVU1knlRvlMRGUZgiiwoN25an-BHuN47JToGDolZ029HDoR39iHPXRN6FEvvLl4Qig6fC-iduLeSgJgwkpqDmZS1tcoDxJPH5PVyWusdG5J2CaeVn5DlNGivlPwniyUya6tGxdHHTn0Sp_pxVcXFNxa983d52MV0xqFzHnizAN_xygVUDIiX-pvFIN7GQ0VbxrTlYFqLfZyPzwoBoMA8nP9X6dxF_v8gOQfBxGnjqTIMcPFdYue_kpNMTB7WJSMcZPFkyiUyraVKDZ3Ca2DiszLKIiyn8mYrNcXTNQVpo5oLO6uY7R7G0J0CA4A1wu6VWfZIBiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=LHe1DDRd4Nt4RDEVU1knlRvlMRGUZgiiwoN25an-BHuN47JToGDolZ029HDoR39iHPXRN6FEvvLl4Qig6fC-iduLeSgJgwkpqDmZS1tcoDxJPH5PVyWusdG5J2CaeVn5DlNGivlPwniyUya6tGxdHHTn0Sp_pxVcXFNxa983d52MV0xqFzHnizAN_xygVUDIiX-pvFIN7GQ0VbxrTlYFqLfZyPzwoBoMA8nP9X6dxF_v8gOQfBxGnjqTIMcPFdYue_kpNMTB7WJSMcZPFkyiUyraVKDZ3Ca2DiszLKIiyn8mYrNcXTNQVpo5oLO6uY7R7G0J0CA4A1wu6VWfZIBiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq3MtSr2cIBNqDya7YRupIoDjqqErvzPc4DzWyyz3OvoYbDjXcgQ3wiDx0PGDADWcIsAx7Ql3w94QQKSO_J-QgjrJt8pvQHLzfTpAARXmhJPcz-r5VfseROmgH0flvzF_SX6D-Zt5gw9ytU9t8RXoPKHiTY8tQsnqPQcxXHt3JIukia2xahAK7qLRhbmzIHlvNu2JjvQCNtxf_PisutcaNnnv0Fqipd_uidsRET6tGjyWfC2v1T8gzQy00L_B7gOsxKALGMky8Q6La-lm2rR3Uq12CIJzhER2_N5f9D9lEJ2CK7te39TX8a0n8fVqCv7VrpxOHsk1_cXBJMk0z4zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiEohrfyfaIfe3P8w1z_yCUw5wcj04gJm5w_u3o6nr7TZyTt_Y-KX3d8inewomzyYazv2t-zxqCiM3HDWeGtRlk3_1j72Biiqed_77hGQmdAlKccjTptTJBPB_u2n-CbkTpelkzUV_z5-U1udfpCvZPHp52T2-gtUQ-T6aVVAg-dDUooSueTUW1e9b1WKaRu0p9Gg2QMnvkEtsK8uTNce1q2L4ZWqlcMps7rnrjAE8hsaUSK-mhYp3GKe9xvEBTRpW-JxNpdLBiwjTJsXcpodozUCz3Pumg6tM_weBpyImU1vPauFHF8rxUUXoNwDNmkSOlvvSGGGB1e0fNO9hhESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=PryycLCyeQkuNJxF07dgsFkecpRuFJXpUadsldf8AxnXuynShxPVHtuGCHlYzuq4FW_wF4JCN_OQu5KaKtF3WeWC_Ch-41Dt1hfFdMk_Sdr7Yw42JnLvWVPRII23d8ApOmhl9AgXj3lb3E2fLGorKm-pMR-yw0Wwd4w8wYYWdgGKp5Y-tpPY2J3X8JR8SExMwwZQMKnAyZ-YkXgZZ3lNWaSLOauEBaoETPEwWbcIvzCQu1h2LiM6sBSbwFiOAB1ggwhyhOKcGvr1z7J2gJdgY6ReB_5Q0uc9uyYK_4V1DwcrPN78VETYb4ZUyH97XxRBwrPsCBuegcH0b2FgzYy1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=PryycLCyeQkuNJxF07dgsFkecpRuFJXpUadsldf8AxnXuynShxPVHtuGCHlYzuq4FW_wF4JCN_OQu5KaKtF3WeWC_Ch-41Dt1hfFdMk_Sdr7Yw42JnLvWVPRII23d8ApOmhl9AgXj3lb3E2fLGorKm-pMR-yw0Wwd4w8wYYWdgGKp5Y-tpPY2J3X8JR8SExMwwZQMKnAyZ-YkXgZZ3lNWaSLOauEBaoETPEwWbcIvzCQu1h2LiM6sBSbwFiOAB1ggwhyhOKcGvr1z7J2gJdgY6ReB_5Q0uc9uyYK_4V1DwcrPN78VETYb4ZUyH97XxRBwrPsCBuegcH0b2FgzYy1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Qzye6jzUZiO9MjDUoXS_Wt6Sau9c_o5rEE_YiXgk7nfkP1swLViKdny2K25oGpKgt84LVfypAmeNVKpyKKNMoyWeVcW311ERYMiJuVG5KGGBRq3eDGGxfu0LKjUiu1zrskyMElBAOiWUi1oY5i5yiNXkoX8H1fyP8Ze8bFPJPYqc-9pl3568RGWhxCPXQeimytDZDsUcZCcf13ApiK6mgzvObKrCzJxqmldcy5sPktNSIiNrxUr6F3gZg_xCLyopIEL4r-H4czrFw5D4xfprl_4NkqrivAEnzpqjjUndYK6dWBltkxh6KU3zvSUBHDQohimXUx0aZJWo44EWfkduWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Qzye6jzUZiO9MjDUoXS_Wt6Sau9c_o5rEE_YiXgk7nfkP1swLViKdny2K25oGpKgt84LVfypAmeNVKpyKKNMoyWeVcW311ERYMiJuVG5KGGBRq3eDGGxfu0LKjUiu1zrskyMElBAOiWUi1oY5i5yiNXkoX8H1fyP8Ze8bFPJPYqc-9pl3568RGWhxCPXQeimytDZDsUcZCcf13ApiK6mgzvObKrCzJxqmldcy5sPktNSIiNrxUr6F3gZg_xCLyopIEL4r-H4czrFw5D4xfprl_4NkqrivAEnzpqjjUndYK6dWBltkxh6KU3zvSUBHDQohimXUx0aZJWo44EWfkduWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck6tF57es_KinDR5j28LK7nNkA384K1mEZ40gUHaTQwG_5yVPyXANrc5m-arbleuzBqtPTIiF5AKal6YdfzVHLGzoRbbC_HSj_SiFfkr9ESZDwCuNYF_WTzP6pkI2DXbocAZ2RovFvsDlsMz1P052s5YMY3NmLZU1T9leBmGwA0AcTdgVuhfLDwQrlkD9IVQNccfYheYv0yKR4Ho9W5p59V7E8TeyJjQyWNtz9XWlbu01NspknlM-T6_wT8GczMeNEydL3guJ2AlWs4c6hE5jAttbbpnY0OtxuHxlGC1doO2E644YkMSRK9DKqU9kYYWZy8-JERtffUxLuvwervCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsVOSjpZEDm5QI3s772EafH8hZfMvZ-YazEVKFoKp8SNo_yXWuKmqJx2PyTVs8J6Ojp0-Eo5Fx250wIjEqPGaHaUkm2y5aTwnTTNSJ4LnjG1tlnlHs0c2WYDVxoTmD46nVJhPdUiYW9BmsG4uKIHcoivYTEGZPaoVV9UfkVct85sH1jbqRMPcqlJgyKVAh34gXLp64yBRBRO6jEj-8Q7TjKVlAnyvC30iq3p6pbnBs4GH3uT2XgKDoMbXrVsOqNkCYWQpnH3beEuE0xTJmtvxmD-0MY32Kwz6wHEI8ULYYC-8Ssuu6hZvuVOm9xnpHirSk33vS-pcGrClUEMP_qqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWANZfYBF5G_oE02ZWFGsL6ykw2hC0rVEjSoAAJSkGcDkeaWjJ9jFYgPIqjUaxOqPboxLNxp7B-edEy-SHVqKVrMT6MHWqwQR4obkuK2qoP7mDYuspMVT82BaXKsCXLGfYS_KLzJnGGl5x86EcHVcHCb7uk1fi3aD_Vh_M5aZGjzdLVVrxTUuPPRzyhJZxFQqQamOSV6_M1hWISID1iT_rUH4tattP4f6n9yzmDph5iD4UVl1tpYt66sA_qYh_syQfVsVJTE4i7WCJb_j_sl5LnwLoPegi5A8Ehjyz_XbZw1BZzATQizItIfZYdolz5KGnrUQr2IcSrRaroOwOXWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=lgcs8mRQKUqa9lLHcx73C69hWZTkeKIWOSLZR7asRmr8TgHESir_vbaF_ZW8t5PI9yjkhCYnFb0PTPySe78ME4m5mErOtJiSmbIhSTrfMUjCmKoy6maj9O7zMjIAb_rq0Hv0lLyhGv_rpJin2niwBWxzWJ9SnoDEl7Q3y9P2ZBosQQ3XcuH9J6DbzqJ1lmzSUOzhTz3gIXWklirVo1JBZshbmwtQYhAGU_x70hxAwhyETfPIlGuCP82KkTQj9wJEANVdfkg22A7TGPsZp_FiYGRUsLrFkPy0WAVtFFlFCrH7a4P9KiRYb8Pyc-4Om2h5mGh5ts7yVqaZqcs7AhpRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=lgcs8mRQKUqa9lLHcx73C69hWZTkeKIWOSLZR7asRmr8TgHESir_vbaF_ZW8t5PI9yjkhCYnFb0PTPySe78ME4m5mErOtJiSmbIhSTrfMUjCmKoy6maj9O7zMjIAb_rq0Hv0lLyhGv_rpJin2niwBWxzWJ9SnoDEl7Q3y9P2ZBosQQ3XcuH9J6DbzqJ1lmzSUOzhTz3gIXWklirVo1JBZshbmwtQYhAGU_x70hxAwhyETfPIlGuCP82KkTQj9wJEANVdfkg22A7TGPsZp_FiYGRUsLrFkPy0WAVtFFlFCrH7a4P9KiRYb8Pyc-4Om2h5mGh5ts7yVqaZqcs7AhpRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6kIbD2jWollPBoIwQNAw-CzdYWiKfge6WmmBG8N8o8y-NvGpzcHRvKfrmNs9QhG1TVBu8ybxmhNmNizF3ejRsj9DNwiCD4e5ZlkWi1ibDW7i_NHCgnQHK4aslQkecj3NXRZPJDEePB2IE4LU4uPkyNxc_8Q_sMAv1hNmK-jM1MDRp4EVB986XVgM05UkHWTQJ5uhc8vXAviPQkLlDYrFfrhJDmsnnmv7zI1tOZi7C7EiCOrYHCqibUHRNQ3BM81uLGQBypscrSjmjBSxxI2JjbW31Ms-2OZ2rk9QGGh9cIob7FJsO14BtjxzDADW4WSMHUwpzgZ6oEEwUAYBvPFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ0TVrwKR65CdGmmx_tlMoOzkky-4ijEX46ggQaSw-uAG7dWnQZ_Fdscxir6F9hv9Rc4-DJXMIN1qKC2ng2bpPTwcdwCDns3qL92jJFCNR_slxN026mG_emLDv--6MUq5wgTB5vg2OgV96BWdDbA4gkm3Y0ootfPuwJzLQLKPehgIdgJWsA_53kqSfkpjpcGOvDwjqm_MQsKaIyXs3FbRUU_W9irMENcHJTetOQ2pMKSy2Jtnm9UF7w02O11UTtEwMXGodzlRjPLXiKVfRfC96dF_dQofepq8vBHLWEzfvIJUH8Uyq8J8MlhaLs6i48NYBYMlxsFDH_63sW5U7gH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-EarfgqkozDOmPt98M67xig54izH7RjRaFpOvqzGU0I3baRetjM1_GX9Hb8P0lIsO0jZ8P-Y-KX7Yx12hLCJSkh9qH-0PrqljV2oiczA4xsgm8GkHmXEWDSpiiJJzxG1crY0IwB490q8cS4SqYka4KCl_-NjhTVvqjzzTGpekbuDvn_-cEMk2FSwQqXjjb9DE1QgCm75M0aR4RvPdHEDcgUZf8YgibdIbm2ymOztUJ-tYGaYFNyecFcnxEbbfcGnENozs3kLkfzsCttvXcCMGMStBi1Vnw5l7sfcl0uAXRMgaQJNaoEDiSFS9G0MIM1bjF2_C3AJpJsPVVAHI3E3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6UFFktpQhoknesQj5hAjmMv59LFlE39hsqm0wy7QmZH3wodBsx-blroOeNZCfDQ2HmarqBVr4Y23dv6eKnmYJgPo22eK6Y-9VRgOzy0dqdmEPUE0sy_2O2woW3_H5l_tBLG_0KiOhv0ai9L1mNNp3UuA63au3ZU-rnEzBv65yaEofZCC6OnRh5bBbeiLH5pemT24CQhPHde1CeHPyUSQ_NGWQZO9MufvgfsVbmc4dT44QVVzIE-LxLPUQ-KoNCUZpqENm1cHRGxIEIp_M3WVW9fBOajJ76J6m-QI_b0yIiCsOeKLauejXl3xkAuw7icfcAgViqAXZMWNtLgVXVKAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=vDBqgwh1X23aiqa5eMLUFo5xar8f7dqiG9ApU9T8U_tfkL19oUyxzKOLZd89Q45g0BP7DA0XNgshNz-glZpiQVZxAOMx2rxz4xL7i1Rsfi4Wkt-O_oGh-TrcPFS0M1QKtRsijmn2ZyD_jMEEX-lcZb0xQrSh7-FcQH1L8GgOUE4rJBpuLe4Dr-jVn-InYGWmEjToNe7NhEza7QQto2L4TJRjCgCnhKWkoz3fMrxrYDjcddGpNbVfZTU16STo-tBxvdB2x9I-Bun0t8lBmqgBm35LMZFKUqSCATV6YSxXfoEv5cCTSftekPuZSssFnlbBIK1XSe-4VCU8x_5nPqSkJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=vDBqgwh1X23aiqa5eMLUFo5xar8f7dqiG9ApU9T8U_tfkL19oUyxzKOLZd89Q45g0BP7DA0XNgshNz-glZpiQVZxAOMx2rxz4xL7i1Rsfi4Wkt-O_oGh-TrcPFS0M1QKtRsijmn2ZyD_jMEEX-lcZb0xQrSh7-FcQH1L8GgOUE4rJBpuLe4Dr-jVn-InYGWmEjToNe7NhEza7QQto2L4TJRjCgCnhKWkoz3fMrxrYDjcddGpNbVfZTU16STo-tBxvdB2x9I-Bun0t8lBmqgBm35LMZFKUqSCATV6YSxXfoEv5cCTSftekPuZSssFnlbBIK1XSe-4VCU8x_5nPqSkJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmOGxI2_xOZ2h5-cYf6NSYGxviFNJYyPQcM7gZ_2WqrCyb-MfbjAIKNBDG4jb2RKFl0SzEl4XHlEwc9FhmbpRjZS7hj5gERQkVjAIoZZm7N46dk-OvGPwdwGoHXfs64JN6cLMY8_iBrxOT-mtIHUrIlsVIoiTYQ3p_t3BxEXUxDMbqVKFcIrEWaIUxLelAvGHBglyiMFiGwhNrVIjD88QCW0EwduZuFSKUQy_SEV7vGGYBd1QUfcsc5o6dXq1OlVN_nN21HeumodjofJdr--X_BhGQiF3vgvMchFy-O3GAe7f7djNriol6N9C51xKLYu33Tu0UbZ8JsNBxPOE6nkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=PzE3uk4zGcD7hBj7YXvYUBooYOO1mdPYghhp4pZD6tBTbvq7VI4r7cjbGA2u5afkLDzNUqsbHotyONYNBvo6j-pMwLbqdnlBV7XgNmpcZm-ZQcExTLBJXPDHGO6D4_NAEQPGK78w16lTbP_elX2waYYTwvn0C47fVZcGBWoWBEqscCVjM_unha6om8km5zFpK4VNDMbI-mmtUvLD2cgPr0Ae9z179u7LPxixW5_-4GNyaGg9dtz63HC11-94QddrbMH4OykAzjLdxgtpz6Tg1gN1caBosAzNNF8GyPZOS82a75x-aX2GasX2bEZO3cyx3Tjz0Kq-8AtuYL9HGQmMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=PzE3uk4zGcD7hBj7YXvYUBooYOO1mdPYghhp4pZD6tBTbvq7VI4r7cjbGA2u5afkLDzNUqsbHotyONYNBvo6j-pMwLbqdnlBV7XgNmpcZm-ZQcExTLBJXPDHGO6D4_NAEQPGK78w16lTbP_elX2waYYTwvn0C47fVZcGBWoWBEqscCVjM_unha6om8km5zFpK4VNDMbI-mmtUvLD2cgPr0Ae9z179u7LPxixW5_-4GNyaGg9dtz63HC11-94QddrbMH4OykAzjLdxgtpz6Tg1gN1caBosAzNNF8GyPZOS82a75x-aX2GasX2bEZO3cyx3Tjz0Kq-8AtuYL9HGQmMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=c2-_Bj6e5mJHzk5rpR6SlHU7ZuMG2XI4-IZMpq8MzdlQplfKoBmM9vXbvdiQBMcaZT5oUdbmpzaMlmOJSgXbJWGZ-8nq6KAX9w91WPbcLVQXzcY-595fzucGXNc-HdW5l1ao2NyO4l9EgGmJXk9r6xvlz6kFyeA-SpNv0IKLKNtCuvzSRTtubR2Slh0Ll1fKZNwfxCTTYMZMK835u5LAlD0DVyoQbNLjM1W6qF8BKCXBkhOkf396zImXN98czm7Q9ei8po8jkWjmTPtKjhrpyhw3rLM_d50eWNbDwmDswKzdpDs3ajLlnDk6Fsh1u3GHajl1niQVnQApQ7GDBzug5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=c2-_Bj6e5mJHzk5rpR6SlHU7ZuMG2XI4-IZMpq8MzdlQplfKoBmM9vXbvdiQBMcaZT5oUdbmpzaMlmOJSgXbJWGZ-8nq6KAX9w91WPbcLVQXzcY-595fzucGXNc-HdW5l1ao2NyO4l9EgGmJXk9r6xvlz6kFyeA-SpNv0IKLKNtCuvzSRTtubR2Slh0Ll1fKZNwfxCTTYMZMK835u5LAlD0DVyoQbNLjM1W6qF8BKCXBkhOkf396zImXN98czm7Q9ei8po8jkWjmTPtKjhrpyhw3rLM_d50eWNbDwmDswKzdpDs3ajLlnDk6Fsh1u3GHajl1niQVnQApQ7GDBzug5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWjfTf9jRiZg_5j0gJwm6uHLH9YTBsmwec7eQBWWZ_svKnJlqv49NQ-CD6f4iVoGRuWiD3N4vPjXGDFwvsVCgOVI_Nf2u6L5fcvEEG6zM3LrYRgI5S-9982MW_lASL-oiCbmKRUm9jVzvR2XyiPusKuNQJZD6wX_rASArWoOwxvVfiXywapzZyIppZ52iHS5EwWK61W9qmo6s23MZOnMQQqcVpCdtiM35MDwv3sTuhyNbE1Ax8cEzNCdu72S75ArfdBUap2yFeOYSDAv_z1UKqSxXik7jRfdOVj1VGSotyx6AnOyGNjCNPxsBWKufyXcqUlMCrj1gQplUI-bTT5PFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=UgTaKBeyRJa64pEhJTsmo3m626SQMjf5oOmzlTOzZIw4n4pQRo_xtpeXji7m6gKwf7ZzCbNLjGXPDt7GAyaH97blIjOjA1FGkNKUWkSiO9X6dSRarzTe4OZoWg6rfaL3iEk1Rrcd69jTau0SXQnvUBKSj6NjHx1VQF86tLAy9VKBI13UVd3RwAVkfbtJCQX0hSNzRiLO7bl3Sh0jmCdoA3JxECFkgiqEkX36Qva6pklzyuQT_BTTauwyCMPA0Z1rZPrUWgPzW2jzChGcH6rrgHtlQD4ZscfGFYmLhfuQCn2sa8BAyzK8GAQuD7fXfccrRoM2rgidfCjpaWJXj-RSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=UgTaKBeyRJa64pEhJTsmo3m626SQMjf5oOmzlTOzZIw4n4pQRo_xtpeXji7m6gKwf7ZzCbNLjGXPDt7GAyaH97blIjOjA1FGkNKUWkSiO9X6dSRarzTe4OZoWg6rfaL3iEk1Rrcd69jTau0SXQnvUBKSj6NjHx1VQF86tLAy9VKBI13UVd3RwAVkfbtJCQX0hSNzRiLO7bl3Sh0jmCdoA3JxECFkgiqEkX36Qva6pklzyuQT_BTTauwyCMPA0Z1rZPrUWgPzW2jzChGcH6rrgHtlQD4ZscfGFYmLhfuQCn2sa8BAyzK8GAQuD7fXfccrRoM2rgidfCjpaWJXj-RSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
