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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 170K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x35l6y5pb0X2_VWxkRrS4PLf1cj3T3NUx-f_DbQdYR_0V_9CTTC5AfFlP7srTCCm66AqK6TMlAHG8xVU6yyWtlPJd6jfFByKCkAIha2rIS4v2Ne2-_KqWtQ7_fJBBZeGeDqWh38SJ6AjbODc0uxvPvHBU8V4VTh2tHZ8CAn-TnLK25hrMiE7mndThessg7MK1Nr5QcVM-oheJMaqAmZ9ZMQ2AnvyQ_ZzljpbM4YZ_s9OGeWKieZea-MU9LpEmFWdBeG34oPQNKuNdFDKBKxHsBvmz1CwdacUE5UQdxlm4QZwq7bMKQ0MZPGqj8hvI9WwYRePoiAjWhkMEZm2uKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9su5uUHDZv13ifItH1MDNVxbIL_cyTcbJeIlOkLKhembWD_c0KG3ip0A-EE2Ddp2XUfAPoxj3vPXdU6HleHZXQsqaQEquL-NmYJQj_CYul2R_CCpqZZ9egRjo4jdCbJUVyx0ePYHitVIZtruhz0hvgI1WCKIwNOGGCKQ9rhnkrVENGZRbGoC6qJmwxd334shEssEyPWepPntnbxwEqvh4SPFzDlpZ8lLFt0MfHMode3veECCEmX1mqZcpdp-PdZMIZ6vA4TA6S-VDsupv1Wb3B3O8_PG_3XTn7Wj_PovkjBcul-77EfID_3UxXWAEImEZ7GjkRcBWibHWHmvL9TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6dAyJ9M5RdZkvu6C5YI30L1Auv-9-ljqz_BDCa718dqgTxb3bpdfUoOhsAwrEQPDeMAURwnXhh4aRzgdFW-V9dtnM1fEOTsj1XXXbiJ7XFWOhLMJUrfsUKaGvm4BVkVlGuODUH7JYdMiAwBHodTcOtQgHYKZ7Yb-8v-ROJ0q3PvIe916pNUlL9F1vnXrxqEQQt47w1vonc0p1wBpd0ma99q5lRR1yA4koyUFScMpBNhcn9_iC_8ivOGqI9mC2aA7_An4msxJNv6EELI_18RDV8sWEOKhddZKtYo1e0BIbIjgV01nbMaMXA0pGzndJRpD9C6_qogCatjnAaAMw-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOk__lUQxzF-um1A9asGb1MxMX9ZaLYYwi1BF3LHS8dy9SQFoMZ4xAoISnnAKgUqHFHx2MLDKMmYw6HuwAXprR9p5W3Rl1tvJ-Fv8GTpe55_xlSLW_Kz7B7PwcOHd4DiDLj1tX0dg8Imv-bIT3cWI8L6aJ-x2qeEhn6wRG242j4KTDkXUH62XZsZ1tPUfYWZmvGcWIuc_1yrtvajLeOTQeeFyWC7AvioyP0KXWLmEUcLFFGfUI-ApGNLo7UARu-BG6q4aiy_N9QZxW_siLvTJUAZWlHhPZP2av9_O5PNSbkoDD9QeRePFI0t3SJZOWKavDdGRcOp-B6SfiI8Kzyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdfUg5RoYL6e8f1KTqwO37rEo5oo6OScHpvuIytu7FraghLeCOJq8Pm3lCEGQ1RaBKivPw3Afrm8tLO6OaDqTZNjSCHG8ErETLiRYPFyG__f4tsmKGU1Ta0NtBzQWyRRWq8CzSpWhQQ-4ifP47V9Fy6LSK7ELY6_2X7GAZB7qm5fv5OxdlBM2xKCgSfYNZITTKwyBkAwX4BmTvPV3o_4er8Y57ZZeXyEfib78IEPffpYU9ZCIh7czJHat9UqMdWX_peylJeKJpi-3lzsBAaa_g2DsGdlU7T3_gH14eaP6TuIcw0AspiaXA94wHWkfVs7sjfI2Ci-dL4xxfouHWWP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2huXpSMcXWKFDAAzzYxHQ58XrtJRGCTwwPlZnTq4wIlmaN82YeSBUApT0Z8CFqEqQlSSPeoC2TN6neS2Dtoni4Z6Cipjm_HxdnSHGsr0v4qudEwpA35MJ_64KL-jaDyKXzBzL332qGz4EHW-tGVL3EHKPsv4MklDPUos7rT90rwJUbzHHIV1lDBsFvGfGo7NLNf8oEEhNI2reNoYSlQ94BOBNZP2U5XB58c8ZNeAtaSMyqJBzGUUaWXVwF5D7P-1Hz3LUAiRVscO122_FtlfmB5J1ZZ8vwbVd4urKMp2xN0_djcINopcnmUdtVH5RfIAcdqx1JUmClZV9bgUUY2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMxCMZA8bUJhYvRkCMEaiIDM5MHMjFtI6pCl7bosHnapSiY5LEwLHcotcb7zF0KYJcOrdgvu3YGuC-7EJKD58uZYcKuizaxKphP7pRqiGrJOgcKfvyxuK0E_7szKhsrXE9BpcdIq1ZgZnBMIgQYHg7cWxong26seg_UyLkFzmkQ14gXmaASbczvDW0PhyRlBPwn3J2r8ry_5YHt-FPwAAZD84ldZ1rL6sijXD0r-nlLKeyPnQLwZTTg1NcOQW9oT8ta0_4F1QQpZPBMdzVe3Z6HxNYiEYb0FZIY3kAJr9bYfys_0jjc3R9a2XblJbbSSzaKWDBfZiYXIGw6Ysik-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAp2fx5XydXLenPLnJGUwURU4GAFzyVfJiJ4Qw6qhvw4S6WGlxJinZCOj3AlwD9CbRFWGFwK4z9449QmAxwJ5rGmu7qIsV7FDKFMSF8_jhxRZlSYiWmWhJLCXmpzlShvMXF0gWXwPo0aGkrUG9cg1aiNQHnhjoJPN1Dy64c8ZVEe4GQ55sJq0kCYsQaQK_iZIxl1KNqSe8kGt52hNcuyMdJpcoebXYykCJ3oaujk-KCQMVBNQqF7p20rG0m6mc0fD8gmNkCxRy57W-F9aHJCgR6KZbp7PfIimn26D55Q89oIrOljVB-CtHv6d6mqwskKulQppmOcDIAuAqqbaWfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYuy5VYV3-BebA4gB8_S4riHk1yL0RIdMUjld6v9AmYvRm39bcC6rPNyIn5nglZBz_3EekZQHQmNihww_bwI_Hi7xIE_oqW3KYF0ZIE7MtBZYeTesgzjFwXzya3Vw1TYDro3I66jWIUzXE14MSyFiPich3M0vmFGNGmocxTu6MrZlDB3WS2G37qJvpYHL-WCoPKUMqJHJ2xjlDDl_JFsCxE7-49OeYt_RCv1i4nLU3Yn104skW0saC91uw0ISBKr6QuzdkTkadTv0gPFNrWJmz6LDTQJ66vStg1UICj_GSy_nDeDzO07WqBLhlAY0AhqggcoXn_LjctkF_MT7EiXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j92rMftzWhqto5RtBsyTKgz74zgizpLk37Oij546OmIFGfIjbLBBg6P_DXosVfLirQcI8MaFJvCXi0JNJnaw3xkVq83TZ_kmIPSNYjsA_TvRvZRv2gRWnvXlIF93scfW_MDJBZSsTwVtAq9Y3-aGSmyJMiLdnecNc5gDo2jRhu_W982N755GIbXHXfWH87f18_r-S5YxlqKKOIPS-NkKbd75VQmHAo4zReldfeqx2OVOgqORy-Z-laABJK3ianeEjh0HeYrsala8_4GYZivMXiRRUF0fXFtpsXBAiu-hlnOWP3ueeSWRqXiwDP1Yiq_FWTHDEQaY1RjSzGg6i6iT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZiJ5b2qhaY4CB_dBCNXXN_uxIZtwLpiTvXxj2ir-JyJM-_ctkUIaDhNCS_pDG4P1R1qUklGVqs8dC_CPL8J9r3pyxQSAnjXS7DZsanswuF5lT1D-roZif7ixcryHK7vnyAIVrNaFEQBXXOVcGq26oJTlNkinsOu6gIAaxeHMYrKNhhpqFF1T0uCFxlFAJV6fDi0ribpAEfeW73HZBaA7SW-8wjt00CJr31Dtkt57ZRtSX4qbe1SHNsFaLul-i7g0ksDZpQoMvIcicJUogW_CgfeAHtSAgtXmzCbEaNiaJN4Z3gdI-Yh6IfqVdKVEcjCUVXx4qhYersMRiuWR6_99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
باارزدیجیتال‌حسابتو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
18
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23007" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUws58UoTO8kclUEERXyAJOArfGdK5zt35ijG_CRw37ZHP8TigtYTVnXqrXUf8B1rGc96Mt8pcmLMUaTbyqEgqehsTRa1MYFB8OpoJRZaAuqNXnhALyBiL20_HmrHa0EPJSeuh_OJxE9jP7NvDwwyDJowJPXKhNn4NTuqxYzdqcbuFgbmQjzF7AWjxpDK91J5fp-3bFFy_YPtmYyzh-JtWj0L05v7HlnPEDVRHNsEH-Imy78v51CP1ksj3BcFjH7_gofNcSJgnSDyp84gNdZoyq1fhBgIC-xU9GdUqFGVbpsywuLnLUxYAxiFsNcbGBxKgRJfNzacqwC___2Z0c7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXD-9APXbkff5q35CVGalgeaEGaNhOIRWKck1tQv4wZ9QLz_wPDK3sPS5aFh6dlYicGd9Vd7wASSIyOeTejZJQ0_aMz2sDVaegM2DsRbi7Ux7TZ9gVFs9Hb4Fks1kbpOlacMZeUldHwDBZu6tXH2mw9qZ_i2hZ-jFUuf-_nlQ9ZNi48YgWO2yuo6My6QhC66pRr2J5ycSWN3E7tC4ptVJ_XYELjXxkQq57dZzsmS6hvZZTSg28fKGLk9F2orEsoNEaQZNOOkT3YZA8c3mztfkqhCNAQJChr95QGC0-v69-DJwSlVmulzzL7deeAhKZBEpG961PvBzYzHk_UBnEvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QhhUIe8ce52IX358JgLGGj-d3Kb0b3IJ2B6kZZP2PmNP4NktrMKXpMI7_4A3O_Y-XAUYoApzsxMLAxAR1ZU38m-F-Ztoml98vRmQm4bdcAvoAUKLilH4-_CLoY9ztveXFp-3A-QyoXFbSHhafnSqwbLTWbi4TeLE4BMxmBGH7y6bdg1HsROQSH6wHZsgiIrOhOpJJxiGsaW8YWVFbiL8Qfjwr_eiW4Qzw28Nv2DiscA8Sqp-8zIJxH0_MwMNe_pdwNtjMBA4kRPy9K4PsyZoZUFz_wsrD-ZCioZAk_T4oMQ4-8E0NXMgFiUhs7buycWKsh_cpZQuKIHVCaUg05rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0MPrhWISxO6oYWhy4nGiRGR7Fx3tXst5lw3DiYcnsevXcD_lXSgOTKgll59r5gADQYe9X-ijHDU8XsTFwBIHsdXJOvl7kZuvrlE2euoSWDsqeZNe-oVFy3ExVb5tNL640kwil1PK0yxRwfbk0kBOCOaMflO7M1I8A-Cd84sJpcwfwMd8hebqMMzQRLl7gWAY_qLG8Unben2n6pL3Am6x0DUx-hB8bNVzLKLtFPJCqLO1P0aMBhQoGjfV2jifjcXpjQh-wAXnplQM0xL6npZuHBwH-3imRaM0MreqIxJHNx-2gR7dOqYFRxyvM_45UJrkA_DIhkIs3NEHj8clGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7q-rGHBgR5xIrV7cr9jpNUSnCKLtfqAgLMPG_QzjTdHEo9m1g9EGsoa6vCBD15KYvnvnGZL0nZ_q6yU8WJUuYoabt9dmT2TTCWC83oUSX7qeX8rJ_HOLI8t2Vtx2VN7ez7gEYjGd4GA7hcnasFNRfNHecx-Jdp-GLbWldBckT45XjPjqeW-cgX8U3Rrss3C-umQngN6c8CcFcssJ2f6CaG1xghb79l96HQa88OFMw7oiNVr26l7t8SpTmVFNsaP4A10503jYuSIoGVV6gLCDvDV8AzQ-WsdFd9BNj1MJQhP1mr_kYGNSb9cNb7DhvtMX6LcNw7_AIwjUwZCkP_dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3s7Pqn8dZkWsMbiqN5lgvl2TdRBTxonj38inyyxSbprHaP7iRW1iiaNsu7L4FJ_Ecn9ij8uEV_RwQG2-C7HF5NZLQmEkR0wAXtmomvJlilo_qpqRtrKNcbbXTIVP_bF99zc_QPQmKelEud76HKh6S5UYPLUjUH8_cwGsqsepEen9L-7JOG1zi5Jya8D4y1wLde_2XU8LeSu72iWDs-uPWXzcbmpev_5XYgABSPgfETZwRwLemLskbu2z-Ngy31Br37V-DX1jNSUWZnC1-BBnTyQannFTCXwm67VcfZjxQMjIYowchS33Zm35BUsjQEBheJFgnMqk_TZIT6dC-XJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51L8pvwybOBjv2Leig4GykKBwj4IHde_SQlye_pIahCAU1MIur3w0xGfFRWSk_M-L_kla3RqmuHkOexRu7v1X12Nxm-r6zMipfiK9tWrG47KqGQ58v-txZx_XXPrIaL8fV9bi8zUumhxek2-dVToQzgZUlf9ZW3XQAgEvLaTHipXmTp4IUDosWJArKbwJEOmtFiIEaGK-SZ5Q29Jw3xZszXr1tatK7vBZDGpW4Lvm49VByTas1K3u8-n1zFG-ob17V3a8XGdxnT0T0VACad9SJQYhQDDlS_L2zgJfuzodGsjOT_Dbms4hsuZZuTOK4aWg8DQGZ8WGDv4wc0WLLGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HroeOGKFzmue2hXxkbEN-2eETIiF5RmjA5G-uHooE54NdKWQKUpdY4a9DNu2MA6FfyJzwDf3PSsAM70e1PK4zGpZbqFBAoLoBiksAjXwrsCS1aziHJw9ETXcZqDkRoztmmiqBEvDxbzG-K8m9JQAPh2P8PJRJ_LSACSIplihPhx7w1aR9DEQeJN0NWBODiDwf76_eH5E-iFwKEfZ6os8wmSrOQ0C-ImIzon3-WH5lNzYU-9JMGh7iFsW9VkYcS7Xvg1PXrKoBavsD_Nq3n3KQPfqjhinhA_woJEoD91bjKUYjrhTRZNQrbTnpjWyXW1_cM-3WAET965VzP12ICa9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PChUvRqqhNa_4Is8T0QoRgpQm8s9rnmu6q3qV5FxN144zetcl0fvrMf2DU2_7MtTqhvPke0QtFy-SDRoQFsHAOheh0pLngdT7CTIO0GNyNAPKr4b0GKnej4CwXnXTM3ARj9SSGcB3mEVb18WHeInYJ38LB8fasG8eGIFkDxAojEfEvEYgsLloci-yfqipPIp5F31Yz9__D1dyKCxs7m3l4vIuI3OvmfsTxxOU2ck-6lEKycDUjFB2GWPKpNJaVb45LQZYxWHGTwok52tsZ6tFe_4A79r0EjRGMZ3i0s2ktnYRTArXs7piBJDzDOJoPHgB1wZjbUBo6C79qZiu_uRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NA28acDsd8L1x2-ZIG977mW43EWgxBt8O5k-E406WbNFcSgZXwLcZ8vm6hDVdDij9B96wAXMClU7t967hugMYJ63Ts4uZI3wl_i4B9tH7Vj_f0qpjNGuzE7JbRARe5Dmg-jR4-G3j9mRjYUjBLaNf8HXq88jfyF_zCiFv5zZEKAUYGUGHKKoWi3XdmrtRPRZhqU7ys7y45OYdaA9XHvOFeo6odkjXTzaLQ9L2uk2scOPG3kK2KS2XIdSZ4qra4PLsJc5IkpjvA1vEvCANW88Ek0w1st1D18K-UQehtI6ySBgjCIB_W9Yt2QWBIB2u47vzO_IeO4SXEluW792l1im5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=fyvVwHJht72WuCVxJu9U0hmOaQUJJzyNKlucaIePXUh-vwE4GxQTtI9TrFm8Zit9gixwW8xPvreCjJcJMmltafoFojSy2kC9GqtpE7xJZFrs8jWOmlcdrqwxjoXYme_pK8N8Gz_bLmStFl0YyNVy-S9TphpfugATaQIfClqFspoFUM2-XYpa89aFxzBarKq72bPu8QgaMd_u9sTiEdfX-oufaJmRFuwCMP5MaxYc79tc2avBgdfaLoeb_YS5FXu6MkMuHq4m8cYNlv158mDUb4jqDudQjIHt0NbCR_z4X1QCuG56fNnem4T-W0keX45abmpoNJZAXRdyR_az_KTTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=fyvVwHJht72WuCVxJu9U0hmOaQUJJzyNKlucaIePXUh-vwE4GxQTtI9TrFm8Zit9gixwW8xPvreCjJcJMmltafoFojSy2kC9GqtpE7xJZFrs8jWOmlcdrqwxjoXYme_pK8N8Gz_bLmStFl0YyNVy-S9TphpfugATaQIfClqFspoFUM2-XYpa89aFxzBarKq72bPu8QgaMd_u9sTiEdfX-oufaJmRFuwCMP5MaxYc79tc2avBgdfaLoeb_YS5FXu6MkMuHq4m8cYNlv158mDUb4jqDudQjIHt0NbCR_z4X1QCuG56fNnem4T-W0keX45abmpoNJZAXRdyR_az_KTTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22982" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4L-n623iNXuLUY-RgCNgzSGLuNes1Uq0qNa3I1rKhbknRecD-5j4boXt3e9k-JKe8E6G3KAWv2Vk4GSma9tEMFmlrbSrQ8SbW9BRGP512UZZYJM_V7duJrCT8B06P6vC6ZyW-t8VBNjnGhMys63caPxjVnCWKsVVEUq_MghrV7Yo7T9K0GqYMgm9JfBsgiM4KhBd-PDnWQk8daKQi9jXd04x2rsMbk_5nihg8RGxdH8TSBum55BrKrGuqOg83YvPRmIGi_uI3CukRxCkQS3zGwqlAnu8LcZ30HwCPCS1SflQemoX2Yb6carZRGgfte2PeRlmU3fVyUcflZDhi_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmHsAoA9VLqcZnwvLn0yiYbUOB1P1GlXzyUWPGXLNcJi6dLKmvgKHO_n8j4f3TLkt4Ko0cHTUSrfSTd0t29kwPTBk1jeWpNlH027B5TfYzE1XE_2JQm8IIxmSYQ-ybPDGJbwfd-vfdRpiNYz2vLwQO7-WQDLebji4KgvhFwPWf16nLVm_YARzJaT4llwLsOwFfQTd2UeXZwjs0LoVWuliVo7_2wfgqDnudV8NjnqFFAoN8lect7BktxPCCZsQngeBDMCJXW9cvdSZyNZcFsvMFPzZ-ep9TbqPU1qVoDt0fxsULghvg8YC6VKH99yUh2wcqMtTarKSpd4VoOWdYrDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfsLSjubmT7QtbTTGcZBTP4rXi5PBnQYrkOcSI9h0J-3WabcFIRVLW2_0yoyQkaQmrrDe-ZR7MxQGpRQOIlWSnIktffv_cnztQEi86SEBjh61-otCHcjNYE9e8RnFdK71o3Yg62l67X0_kUmahxeuBv7iFexU787t1qMVKFefHd5FzyQc-ccJuYcv5CXJnf-5sSWLqbz5lvMKw9QlfFVI2Gs7v1oQyJUc0PJ1Yh4m5y5muGIVayljgNHQbWrAq4NosKV7o9ogND3SQfMeTERzQTg8bILpyUZ7v_Fy3d1Xx8pE1_UK6mfMA4r1ZcKiuO6nRLwFyPmZ5QMNspEOFbxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcpMfNE-WaKje2gp0oThUaeOFSwGuQB_aT7fbuuDhrkcz8H0Cduv0F_CvAjYbvb8DZwcQg48pI3OHXJGwTE_Kj35RxzM9tSls-LnLFJDLVfW5lmG5qszrT18W0K7MyL2-IiRd66fAbUW27SgCybVQ5dkhvC2Tn1akzObl4CqHWr7pH9rWkKOOeHO3fOBlx81EXgMn7MnJ_0npFnUeKSgW6QhIs0_RoM3aBvXqshRXvX8nQcc1RUlv1i2Cbn57VfTYrq1F1UjpJ-zkgxC8odlqppmYUZX95_RWg8uttBLvZPkFHmb1PNUbnmYTyyorEgcbCpvqPbKpiloTmweOoMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaQCrrPK8s2Qbqv19fem8IUU6mEpdT0F27Cc8hi8AW-PNkZ1UF7JEzCjxls6Icje2Bhwx2QYvTNLTmfQA09pqMX3yy2UIUxmnVhN1PkpA6nFHds5AWKZwBDf4CuAek-SdOponpd9gqRnRFSD1mZ9_qs6CLc3qrp7mYuBBrkrll2vMXK2-aLGHZennjpK-8CzfrucPas6guM3O-OvLHp3hSTIRQuz8wWDuKi483c_ll30_vZfFdfSkul3KESfYq9TSVJ5vau755acbMEtnLvRDz7yEUEHxtAXorUkhNoeTQ_UPmcNtyNQOjrK0kNTyTlMdjD4iQcEKwbeNrEll1rDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noXf63rWj7UaQDzIMzs6Xl9IX1aZsNt_38XsHkMMNn0GGm1Cgw-LKi-ALnmv5CgAFepRzafk15jOioSI5wsaSYL82HnjV9Wtx0Q4quYHO1RKvovc74lMnte4inNwSX0qDXuw_NZBiny7BJEtdrlQMYx7FFNUvHAyXUb8aqVz_j6z-dcSPQ7IiC3oVfGVztprC0nMPIuG9DVNqLoreZnMVrm87k4qzZzh3zQKEyE4VNr6Ww--xVR51ukVs3kdDzzQYql9f8YzDpORKA_2s5L9LjjJOnAyMmhB9dHu94bTeki03rrMyby1i3t04EFauV3oyrMjHOkQJKIt7vTA_2_nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbuH35ptNoz37kyS_sl2FdMBnQr8CxAO16fVbFOBewmgzsQ4ucUmh-aTSNF-Th_J-HkdLOoE8q0neuDC0Shu63djVDJ82WAlOsPjl6SI4ieyha7_kbBJ3H5T5KVmyL5QV5FRoaN__N78jkIuAmp86Lgd9rMFwSIhjoLeoTfP6lU4aM19oJLFm0I4gBqLW1cwHiiTkDcLj2OzB89wpcfT-P043dKFy-teBeDxj9rY1CVWjS-HIM9nIXe8e14VHWK1-FqOrJLG391kW3wrtBdX7PK1CRzbxDsqPkyWvWebmfArRIbCL4EuV82XSSh3WM8CCl0SXlg3iE1GFLuJguXszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrsl0_kbQgeW0PcUVtyRK9j3Bah2Kpe-40R5mkeAUzqQyLtboDCbnEEnibh-FSmhg9bGuF9H8aR38_ujdI-eLDUKyIBjeAoGHCjoj6XgwzYCeX1euva6JlFTvv8vjE2aIpBnqhLi9Aq-RZbCK5mz5iJua8-Lb9hldYIoGiIP6HsZIiaRrGzSuWn1eiUw-eJLifV3X8dXlr58HvM3InLmpb45eQ0uaNxny1PDgXx2y_lKhgDDHh82Z2FxyB3hVPTM4hKf3rXyYosU1kQ7JvruNyO-QBdBsvKF5445nLW1VScO3SWH6vUmqDM8uf7CPkFSZ0IvUbVWsCbrnPcumITKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsg8CEDKDyY1pUG7hP7_2DDQbG4mcF5iVS8GuNEueNSkInR6-_jDYxsiqfqBz395Wn7CjozIoTyX3a1ZoCSjekYyybx_4UqJs3hL2CSDfY3bQmcnL4_hN-lHo8uoN01FW1EltoXhH80PZhLEF62M3GTGyiWXv-PRHmxTm3YfQffl2t3btAV8pyaa-zZW8yndTUellN1WUPS4QFFNErpKMK3Dm5ycou7Xdg8fjq0Ig_vqLnwUoANQ8IMFhM-H9-uoybXRyPPN3woRpGDNcogrkv9cjoWz5PNgoOpBmFEQxv_8mY-e8zhN_kfy4w8oJ0CMYbggJEY7EpaVzBLixCKHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Aeea5xwR0qSCQzOgqZg3nOZjrXo0nJAy136pbHf2NbVVzzCWuNaKO_sYbdGi8XjSZpnxjOhg1l7373V1DyHedI1XCZrM9w4lV6KJAiaghfWUNn8MRGUoADFCwxcmEgBiu8Ue8UCIGSVDm8Fm3bUW4HF_2TyBMoW7hhvCIzpKS0wWEXnproUwPt4p0ruxfD4PfH-pZPmKVtEJW0lC45i-uwG23HFYN8UC1ZgA4NdyCfHqUIVUo_CNNqDboM9S5mMCR5CoRkc8MX3gbqd58ci7KzU0JKR5xd_IAICMz8cnGuO-ynCgimJr7oTwnksFqPNQsUk6qAgbVwOA1wS7WEwM2b-uZxzFtNwBQKNIHGOW8yU5aufJLuGo0s-eFY9-JTFg3iTWlQQKNeOB6x6VGKGpFVHWPu-JMXs9pnn6Ao7aoLNgd2TtOaPxqzCIwkPAxvIplqJ8-vzwiF4OIUa4M7XhaNKKeKblij7jhfNXSgHrwvaQTQLNCCZwzndPuOQDksr_TMOpOQQVQH3cPX0tzm0Ql_czDja4o-pMEyFh9cX8ZR1Bvs5p0huRQmj5hXnvLI63G85h4UlbWQVyij-JFZvLE7ILRmjup_uU29dgiKpKNVbhBKd_wJI0xuGni3cXX92nPjN8UQjasStdcTmrybMrkzM8H3KPHH4SJ28Rc5XR2B0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Aeea5xwR0qSCQzOgqZg3nOZjrXo0nJAy136pbHf2NbVVzzCWuNaKO_sYbdGi8XjSZpnxjOhg1l7373V1DyHedI1XCZrM9w4lV6KJAiaghfWUNn8MRGUoADFCwxcmEgBiu8Ue8UCIGSVDm8Fm3bUW4HF_2TyBMoW7hhvCIzpKS0wWEXnproUwPt4p0ruxfD4PfH-pZPmKVtEJW0lC45i-uwG23HFYN8UC1ZgA4NdyCfHqUIVUo_CNNqDboM9S5mMCR5CoRkc8MX3gbqd58ci7KzU0JKR5xd_IAICMz8cnGuO-ynCgimJr7oTwnksFqPNQsUk6qAgbVwOA1wS7WEwM2b-uZxzFtNwBQKNIHGOW8yU5aufJLuGo0s-eFY9-JTFg3iTWlQQKNeOB6x6VGKGpFVHWPu-JMXs9pnn6Ao7aoLNgd2TtOaPxqzCIwkPAxvIplqJ8-vzwiF4OIUa4M7XhaNKKeKblij7jhfNXSgHrwvaQTQLNCCZwzndPuOQDksr_TMOpOQQVQH3cPX0tzm0Ql_czDja4o-pMEyFh9cX8ZR1Bvs5p0huRQmj5hXnvLI63G85h4UlbWQVyij-JFZvLE7ILRmjup_uU29dgiKpKNVbhBKd_wJI0xuGni3cXX92nPjN8UQjasStdcTmrybMrkzM8H3KPHH4SJ28Rc5XR2B0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=vS5ZH8pjrXRxhBZ4PX_WDrrL4Jtx7bcPk1P5VccByb_yROIT0C8oLsiVzDlC5YrrOLh7meLMrawkfz5FkYU5dDuSxehlCSJUbpoTiNZIMLTVDmSe2EX0ukv-y7dEyycP8WoKFWcRGch-Dgf1HNYToFosTbFOVptVtRI4_pMkneUOGvgjgmXo8TuVWm74grnAuW3xGyCkTQ8JjNbPGS8GsvGtoSbxREp0ye3Mz8Nc7QUu_RvlPJQxUr1LXFj4rs1p7XzVLp8R7VT-JSXMq_Yn1izO55OsAvs332DGTzho68ffWSyvXO_-vKDDDKHuSoB7CoCt1Z8ArUK-Njmo8G9_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=vS5ZH8pjrXRxhBZ4PX_WDrrL4Jtx7bcPk1P5VccByb_yROIT0C8oLsiVzDlC5YrrOLh7meLMrawkfz5FkYU5dDuSxehlCSJUbpoTiNZIMLTVDmSe2EX0ukv-y7dEyycP8WoKFWcRGch-Dgf1HNYToFosTbFOVptVtRI4_pMkneUOGvgjgmXo8TuVWm74grnAuW3xGyCkTQ8JjNbPGS8GsvGtoSbxREp0ye3Mz8Nc7QUu_RvlPJQxUr1LXFj4rs1p7XzVLp8R7VT-JSXMq_Yn1izO55OsAvs332DGTzho68ffWSyvXO_-vKDDDKHuSoB7CoCt1Z8ArUK-Njmo8G9_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGeyr-JpsH3t4XtD-yUnr_VxtM-1Zf8QdCFvEFMNNTps-7W8TXKFBS5pihhp2qRaZ5r0z2QWWre-968Z4R1hQi2BSOv_4p1NgK-iXZoICgyIOzefuFwJxEREIgcy2VOgPj7mVBuPhv8auOkSwaKNBd-WJZWRx4huOEIZ7G2kqflzEiVI34gM1r6cg0plLGvw4KioR4zuw7thZ_ia2Vlg3-Jnp0ZCWquIX0ELDq32un015BKVwTWgOOmFqPrhaKzJ3oAwuVKCUmcNbsfjX1IfxaBO__E7j8ejxfiF_DAZiaq1kzq8VH1Zys8MKUS7B4ZdnXNti6Bz_ekuqNfjunJ-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=TEz3wfpDM43EJUEo6Ekhaye70F4gyxW9_p8QbnTwSGipoX7nzifr4wORp-EDq5BVn4dOsEHg0q4uL-ItqNwhxChGdDwqvxGbFgSMApo6mj-ra4r8kMIRZ_1UhT7yBXWxrH3DcUsH1lRwd71SWV9PI1h5aUxnfl-fSOzozhQzhaMAz6stdW7WBfwjynW3f31tMQicIeCXgxfHBncG9MGQ01XkwZUHOQyRb1F3x9m4NUBbZbamUdbZXNZmmabzmvpYZnO_woMWqh06q0aNc1Kx1nl3Vls_SVXk4Qxw-fPHoN1Xi4ha3Dp1rPglnZvW-WUSGwf9o1rwVp8VUnTXbLACtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=TEz3wfpDM43EJUEo6Ekhaye70F4gyxW9_p8QbnTwSGipoX7nzifr4wORp-EDq5BVn4dOsEHg0q4uL-ItqNwhxChGdDwqvxGbFgSMApo6mj-ra4r8kMIRZ_1UhT7yBXWxrH3DcUsH1lRwd71SWV9PI1h5aUxnfl-fSOzozhQzhaMAz6stdW7WBfwjynW3f31tMQicIeCXgxfHBncG9MGQ01XkwZUHOQyRb1F3x9m4NUBbZbamUdbZXNZmmabzmvpYZnO_woMWqh06q0aNc1Kx1nl3Vls_SVXk4Qxw-fPHoN1Xi4ha3Dp1rPglnZvW-WUSGwf9o1rwVp8VUnTXbLACtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NobPEuBYrXKYCSoLyFbw0DEBxTyBoX_ADT0xTGKetjhhUb74ObexeSVWxesj6hmK3WZy4dOcklZKfdVauQIX8SYAljH9NjF2e94ZmEkHueShAqEvF79TjaGx6FND27xthn9vy9CK4ZiBNBAzYAasR31eFz_-4yAQ8BZ1otyW4wc7Qhiu_TD78SqbdYtT_bv0eZr1-ZZnibkHYEfDEF4UZRXK8UH60WXgnw03yILxfM6lS_rto3Ye2T9-dJDeEd2Q1CJBEitWms2FL732lbPkV0_fh26253hdCoGd5ox6rgbIoG8zZ397KfcD_pH9SdC2WYoS28Dr6r9FVXXgjMYDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9YElPGdOsTiZLbxl0hv4Eg1PEhJHVO-ZiMpj7dLNw6EkQNIi5K8bIrRFNY1gwi_787bXV0GR9QNdM8T2cMSahEJBqm0FPjq8xghUnsM4A7weELoG0DajoMFroAQhBnn1Pkx6TOWBs5Y-E8mUybB-PiB4cMvKtgUAS7juvoaflcveQseqDQ4TbFADpb_LQlvR-CaeH-1kk9BCy6slbsQk82Be0rS9KjmmnNNoNle3z7-6u4nQf5OO1Tj5cQSyyPsEVR1QJWw06PJYBmf8O31kOtIko7rMTHuiF_D08JxLo-l-_Sg7ix3vnApeMl-mh_cHVRmOpfal6uUhBiedGhDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Vg-5NphaJKJGfbeJOZ3xZ3IdfeDZngPT-fGX8xLK9Kg57krOFP7bxUhRDAO_yeriYa8y2eYNq2HGzcjguIEWrFnL5DdmRj7eRsZg-toFewECukU-Ja_SqfekUuRjAWQXdEEVwSExCuSKsW2ZjptC2I_YvDxmWr6Hzb90tuojJemmeRDiFte0iBhX6ljgYGDfypyEJXnFAVG4yThIqtX40mHd0pmZfNWUHGjXWhgYon4vAabfJI5q7_KgbuFaOywHd2BjTGUlLOlfNppnUfSYPTGhMSxIObXpYTHqWMKJVq78LD2RLU03JgnHOnw6_xjC9Wssa0SlBSgfZx1TR_aCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Vg-5NphaJKJGfbeJOZ3xZ3IdfeDZngPT-fGX8xLK9Kg57krOFP7bxUhRDAO_yeriYa8y2eYNq2HGzcjguIEWrFnL5DdmRj7eRsZg-toFewECukU-Ja_SqfekUuRjAWQXdEEVwSExCuSKsW2ZjptC2I_YvDxmWr6Hzb90tuojJemmeRDiFte0iBhX6ljgYGDfypyEJXnFAVG4yThIqtX40mHd0pmZfNWUHGjXWhgYon4vAabfJI5q7_KgbuFaOywHd2BjTGUlLOlfNppnUfSYPTGhMSxIObXpYTHqWMKJVq78LD2RLU03JgnHOnw6_xjC9Wssa0SlBSgfZx1TR_aCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0Qaf-67DIwaHCwSMHEmA6rBw6s0XLv8fD8W23c02bSr16YkPFNOnW3jnxzHYw35_P4ULs-ZMaVb_L7QTr7LZO1CiT7dmlyQ5S9IOC6hDapgqYMuUZ2eiuuZ4-eOiy1FmNJ9HlSDU3As9Ge-k78q_Vd0qDYDlsquJAkXftm9_xr4Z6RraL3-7qyqFFd_JPPpWnZsUmt-dd3Bpx-_53I7eAz5WGw_r5gF3GuqAbmDB-LvXL6PJB9Bo4pAm1puyN7LlmTYufScR_RbLu_GO7pJo7Fb81DK5lWcY8q7reoWXzt4hYSriBKsTT8MNYSMp4zDr0pt8Ien5-XTAN7X9eMs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ8BabrmM6K1uO8FqenAPVKVCTwkSueS4kltJwcEafRVas7H6YdTGMIrrYr-7PdEGHJ_AeVuEWNFvIrkKO_G-rhFhXnzSbnJQx0QNHM9xKQlU8dBxRKfstufEAP87Nc0jGlyzI6A06U0EpBTsr-MyRuiL92RhWQ_w2_AFV8T_X663h6JyMjCE1XXvmAaI_eB13KsQAr14PJfOh2rHgNYIVmhZIuR3OwvGHZcW9-L8KzHQHBHg2wN_8S-QyDKr_H9Bz05cJV-JRuXuUX18UwPXcUN0Go04-bpKmiTyfP4Pxxs-6OUDs4WqsfA3hxJun9icW9Ekri9CXtfNSlJKB57zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdRmT0ajWGbN-dKyyMFXLmg9UhzzX0S-ZroVBWMZ2Nb-yn_rPbNUTTrWiBCP_glPnUvzMEIQs0hO8fNdCPyyZEPGY6Mx8BY721itFl2J9r-1LYU9pvyKz1DqOVs1s9YjxfHuf99D_XQNmszc0rDoJhEzUkzymiuSKjST1ldCbJfVlYViecdMXejPxO-M0WfKXM66eIkuuk2te8p0w5qQfcAHWz3gGZ5y8LJNoIYRjRpYh1Xt4KwJxdCTsVsUH2cOExajSB_McKclIBZFCrJ1LVxhX0ns6y424A8QuzVUCigeavHUFZfZ98KrlHp2gR3hhLnsCn9MaWcY6ROfX8_bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLuIUeU4Splgflslej4FFxQpTkvcFwyyJ62UZ7-gufmM6Vo0yYr_HgRu8P1YMq0AyT1yyhnRHnW7E4uyfxtFNXHOibU38OOq1G5wNqtTTPL8Nz_TOn8aXkbMA-_2wp4CJ944u3JU-__Ch_7LCbLTl6OU1saJhw5deTzCIDrHjqT2mynlcMfhQedc4jFUdY_pjObzlSSuKHLlE-90hkkDT0kroAmDHPHa5QnLryjRTee1TEmwQqdRMbrdhKya1TRUCjb8tCC-nQFo3zEes9yYzIIup-uv9YgeJ4n6mxUB94_--PaDIejrqFevA88zd-wLACeOowsarJ6Han9DVDQleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=nlEhw5mAmvQRxWWOtz0BhzD1aSYWdQxgH7WHlH4kgr2Ux62EAuYn2jCFsXrbv_uDQp7xwMQSIIdPMvmmDWYn9POZwaE2SxtAxbrkTnMpO7iWS4JSPevKE7GJpT1ydtPMqOT_nLgo6awoklKhUwwCqOlFR7dKn1K_4tP59slHW4AwLGmm_utiRBL6AVUL9X17Lmuf8Ef5bpvT42H20LhLAwLxtY4acDjivKNs4ZvOyVOc1FMV0gg3rjguQfr6NWE0aSkPY6FoL7FpcrDKxHS0L296yjUooPeSBFWhODWkWTxOixRlfl9VRI0m_kMu2gOIEHVBqBZVD8LrbNKoNItPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=nlEhw5mAmvQRxWWOtz0BhzD1aSYWdQxgH7WHlH4kgr2Ux62EAuYn2jCFsXrbv_uDQp7xwMQSIIdPMvmmDWYn9POZwaE2SxtAxbrkTnMpO7iWS4JSPevKE7GJpT1ydtPMqOT_nLgo6awoklKhUwwCqOlFR7dKn1K_4tP59slHW4AwLGmm_utiRBL6AVUL9X17Lmuf8Ef5bpvT42H20LhLAwLxtY4acDjivKNs4ZvOyVOc1FMV0gg3rjguQfr6NWE0aSkPY6FoL7FpcrDKxHS0L296yjUooPeSBFWhODWkWTxOixRlfl9VRI0m_kMu2gOIEHVBqBZVD8LrbNKoNItPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2sdNMpkfcI2CwxtJu6h6UNUHoZyiRg2fk0lunp7H9C1rz_c0im2I2LhGVL_NwLGx2bJOBJ0P8AowMFTaP87Sl1Bnr8-qIgnZBkrQqEkfxDeS_x6ViImCtfm4LijiwZltuovCx44lsgOE3RpLq6n817qFu-SldT2t6hKtjTX9atssfCL7sxGsjhogUMwEMYrbvVTzBw1uJNfgLusgnH73LDxCjq5AHHUNvYzABFrEvrGJNS8Qtb183raDWyQST10V1jQ5Zo2_7EBOTSLmOrOWUDH8AOH5efSCa3FerlGjAXcbpCbyR7vbsDJBSbw0j0wNcYrca4Vswi1Q-CtX1AJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=gHvqJ5P7wzsvGLOlPwZVRcW5ei9m0G2Y5y4Dja2Qv5ZKHAr0HECm9XQj94KmFFB0zMEDsbWu2hdoBAsBdpW84j6slexQYepnYk5CVUy4QBm7qNk2IBNG7H-yN9VSZDFWHI8pfUmY22L-AXAiEfQwqaJd5ks7BGXFpRp9uSY2VJ7lLMdegeRQhGE7VCGSFEqEOD5mG8J_BfbO6hEr1kkHOwUsOnQqFvqHE94Yy1qX8DR7aiNCAU_oY1OV4i4OFP-eN5zh7BMrJJRdKulGCaBpsCnAQDy31C5kDlfYB8Cl7s7TZWFRLL_kntesGFbZ3FLhBkphHI0s68k_PVq5KiiBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=gHvqJ5P7wzsvGLOlPwZVRcW5ei9m0G2Y5y4Dja2Qv5ZKHAr0HECm9XQj94KmFFB0zMEDsbWu2hdoBAsBdpW84j6slexQYepnYk5CVUy4QBm7qNk2IBNG7H-yN9VSZDFWHI8pfUmY22L-AXAiEfQwqaJd5ks7BGXFpRp9uSY2VJ7lLMdegeRQhGE7VCGSFEqEOD5mG8J_BfbO6hEr1kkHOwUsOnQqFvqHE94Yy1qX8DR7aiNCAU_oY1OV4i4OFP-eN5zh7BMrJJRdKulGCaBpsCnAQDy31C5kDlfYB8Cl7s7TZWFRLL_kntesGFbZ3FLhBkphHI0s68k_PVq5KiiBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITl5Q_i_Ul6cxgPWSmewd_yOcmmbVSQtYSulmcTBqdVbdCuwagU2_Lezi_IVc8pv0XjxlbhvlruF6qTt90HpZLaVbxJoihO1oMfH843K3d3v3hpW3Yt-WZ9IVv9QUSZZSR3AD1uKGmSFliIaSIcXZ6IwyQLfGc1AYQRjFWdLTCc9TOf_BY8ruiAswzp1tS-Z9eo-uup0nBxTiyyLqKTIugsvwxyrQ8JmXM04aFZp8UIrxcORBrCksKqEBeIxu8Aw7i0wdsm_FnNNccAz6msu3_rBMg3cTY0JYc8-1waybN8G5ItVHDzJYDjL1p3guhZwZnKScdpIIkF90qgoAgkGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4ryqJ4UZl3N5c-DCrJazVbepWs6qFV0EU0BjlzEKJPNRUTKPMd1wvxj3RmDgYk0GljWGkczIiwCrtCSCLAAvtp82iTrchRfyTpq6HnVESY7aVSDtuIO6DxFW9L0m_a584mHz-wHXBJ7lC7UH0Ex92D_z_kEh_f6K3qVpi-gCODWj9aY8aZkNcYwvCOAOviQK6ryiW36EIP-nmRvM9VP0cmZo7PhNNF3hPreTaqdoNowXqwDSA-bC3IBPgrVThs6yW94bXexJt4Yp96JQ8iH_HIxQXHn7mXSU4TUDLYC0SEiNFejxfhNpsLSzDNLOHY0Bv7Ln_3XVFvgvDEmVBBmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrBmSLmkqZ4jQS2Jq59lChZCb8iALpz4znT6EQL58J7FNVhv4jfmEuGJrgnvlRDCqM3wsloW5T2XtHpkVc1-Q8xtm3_NtWp6xe8YOvf6yLFe3ipHqkuN8Hz1p3p-StGZSAXHD-MK5Cp0OJQ9F3VfY-mec7TjalniQ3V-emYz1qiH2f-4t7CisEr6YvritagFvIHhRZSx-guIcQ_U5jqN8pzwJUNWmYkt_T9xvvxCkI66RUTeoqrUJhJYzZXT-BbGWebKEQxDjUB6OqPpo__tOOE5QPK7dwme-SAXmJnO9c5CKnOBw4mdK8AR4oz0qCvxdmYlV4mAbpJkT6IoL5UcLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvTSet00RsD-q_Wz3ivPTX84HgBvxi14llS0TP-s7AENn9008Lo4R45-YNRXG5a0KCKRLtosAASEIxyuuBINXYH90lFyVk1WgXIa0n1j6AWqNZQ_WftjsMfDshdNaw7EDNuyfk16HXKW-R96QYtcNn-maBzMs9-EPOpvo4vkRyBWiuQK5IXLYmzzbSEtoEEUmKLsiEk-VqjdWvRRD-c2SWL--w59NwUHvK2qAexmI9xBqMloLSMdw7zvfH2S2xkeGFSECHt09ZpYSooXuRCNTueoahHN_aPZS0TM0V9cwhhW7lI1PwBw5GI4VA-kqsTmxU-Kwc8yfC-xDYJS--A7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=ZzIJYLIH_wX-V5bM0Tz7a2yKsowpYqul_xDliD9GURr16eKw0f36D4CFFL-99trfuwrsCN5vhkx0c-9D778lXubGmELFDJyH-vqz0uM0Cvf3Qpr09Bmgv_OWrnE6_eBoPgwoirtxzZMJRakKw--q-_4WMNbaPVHcWjb4nbQCbx2OxnC_Q899_6SMqlaUYD_9rKu_LKdarfyi2ubJdPnGblbkGEKxVnuVJwifyAta_Hl8_jRAiZ9Zrpmacyj1Cgk3UKh3-MeEZz-u58gTFoKmMZSHqKOxjW7pXVWVlFrc3-1HExxYg_RmNf1LGNnIvHDVYRjs5E8qN9xTSJ3aBx15EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=ZzIJYLIH_wX-V5bM0Tz7a2yKsowpYqul_xDliD9GURr16eKw0f36D4CFFL-99trfuwrsCN5vhkx0c-9D778lXubGmELFDJyH-vqz0uM0Cvf3Qpr09Bmgv_OWrnE6_eBoPgwoirtxzZMJRakKw--q-_4WMNbaPVHcWjb4nbQCbx2OxnC_Q899_6SMqlaUYD_9rKu_LKdarfyi2ubJdPnGblbkGEKxVnuVJwifyAta_Hl8_jRAiZ9Zrpmacyj1Cgk3UKh3-MeEZz-u58gTFoKmMZSHqKOxjW7pXVWVlFrc3-1HExxYg_RmNf1LGNnIvHDVYRjs5E8qN9xTSJ3aBx15EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owPqVHBsjomoZph77npYI-PCIpazmiAx-sWJgaoFmW9v7dbA_YQpih1nhih28rsebVbpgrYb06IKaPM27QLv4-6hHkzmYEcIL5-tA9ZNuQa_FQ44mYEccRz-8Cg-c9G2_TY_h4ABFXLrLVyMGaLFOvzUnRe4jUTB7CUq_qnYfHUzOSXwAqjpXl6KOz_iPwy7WN4mkBJ_3zgMbvMKUqOH0QCPNN-8ghLWh6psZOPyrm2TnZ6sXjF6sGlGdYYpZddzvw46mQrvOhvoCqES7z3yO8wRqficcZ7t2NqSaQYUP6EYXslZEBnOkQMuCqddSqybGLpyYqTuZP7nA25GpqcspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7tRD8bvSdjPq1Os7Cg4rPeoJsaN5magUD8I7QVbBeLhXQYQAvnLZp-BWpB7k2FSQ3MzS9WdCSspPxwNE5JV1-bh_jVWVGT-NtpqjXSR2INoyAHSZFr4I5pQBb3rEvs3W3S9jiI59tOMlCpq_IurJ35Eo9Wy4oNH7JGMMl6ZjGlmbX6bJ5vJ4b4dK5pu75vrpjobK4alCLkds5AcY-ztxTEctFv90HKLxBnV2z6nvkTNjLa_4A3P2sEKGvh1kgIRjYJXo50U3DY9LOz6X7iiys6_cFaMT_fH0BjrHdyT9_6fsV5TVkhdqomBU0tvI7CHO_SsNMTYnA_Oq1cptc9m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emx8qBlwdMqbwgyB-hcHraVLRMgdsjo-hDhVkBh2nG-3KY2yAV3Vm8LjygpGzQHuAf1UcUqOUxtxkBzkz3C9sqyUdWCjMt9Wk25zmah3VLxqT0vZjq9Pw9YIbwRgnZyjvhrqon0ib1SYOiyA8AV6PZqucwAOu91aDe1zqAtoyguEx5eKnWdr8epV5GdSf6lFO_BPrZ2dEFrfAmGUJMVzGCOdKKoSemw67ll7oWj6w_A0gf-3yO019ssZgb-hsW9mWfU8cZkVWqLBrmjyUVhXg05_iSoQ5PWMQWc3mmKy4fnc68l4FDXbsY4yb4035PoGvnwCQjzN4rG76hVyFod_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=XoRTkFpn8NNRjTuiPK0-l_kK9y9VmiNwnULmTrNA1g86ccdVijQWn63_qCsD5zTJllBnn3QxwO8rUcBLkha6XA4QwZT2WmkRKoUq-gIlu1c1owYFRsT6866Oiv1rV61h7wxD1-so11d3KlopXptVDIp9VvwHe-OlW-HBuNmwnuMGvXEoVUJ0IXonEWlZVk9UVvVVZO1OLZUH1nLIttgi9kZklbaD5VnZWkCGXOUEcBB-5NviTe6oLToIs_Nc1C2q8zp596UnUO_flT6-2UWKKuQn9fE2A2tkMXzcQ92vJVaUJMTn_TsFES8lNSvJshyxOY99OVVRvMwBeuagqHqNWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=XoRTkFpn8NNRjTuiPK0-l_kK9y9VmiNwnULmTrNA1g86ccdVijQWn63_qCsD5zTJllBnn3QxwO8rUcBLkha6XA4QwZT2WmkRKoUq-gIlu1c1owYFRsT6866Oiv1rV61h7wxD1-so11d3KlopXptVDIp9VvwHe-OlW-HBuNmwnuMGvXEoVUJ0IXonEWlZVk9UVvVVZO1OLZUH1nLIttgi9kZklbaD5VnZWkCGXOUEcBB-5NviTe6oLToIs_Nc1C2q8zp596UnUO_flT6-2UWKKuQn9fE2A2tkMXzcQ92vJVaUJMTn_TsFES8lNSvJshyxOY99OVVRvMwBeuagqHqNWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2jFezPTyKD1vydBfxyBwR93plwQ5j-USmjp8nbOiMcKL8PUzQOXYsPK03aXgCsBZ_f6SzjitKR0Xft1XWGqAstFMHkrG4yIXxrmX8bF9NW0Ing3V8wXX8yt9kY6-Vz6PhgiuHEafBewjqrnXtge6l6GZoCT0_WP1VzIwnoyiF2b4udQTTv4LK9c2_OoTId0azKgsjuKamIiIg-UsuqHqkJ7LY2xgoHzNvxYsOldmF2Kaj0vKAuaOQMAnxA-m8PicmndES2-Er74CyKtvAbN54mnJ2oSABfaNdM5yA6s4yuJ0Ocen4EyWp828HzXh8k9-VtLpLezNKYhjwztzJ9jWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1ahTdZc2RAywN3PhcpKk41715hx1WxdCi-kpD6dt-eR9p77EysxEC2e-Jopxz7sN_BItgaRbyfHk4_6SnKr_tsQiAqEftP54iqhmKrkOxJHWlIds4f4EeBaBXHeCv7h_xeZqI6c4cgQ-IGCWRc6ZwjtVTWTCxbS6jAYsBSVUVIWBLibXnkSXBOt0EyVgYYrB_w2ai10RJr6amvpvOHiXAUAR_FlsgJz-jRH6dHh1BdTDU3lZgy4CKXLt2yUr0S8F6decwywSjUjyczoGkAmPqRKIsX10D_YCdX6inObwgTck7W1Do8Ori9WhjQl41JsQ6zYeKoJ4W8EZ66OdCAl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfKwHaJvTcG_iE3Hf8yIW-VV4tO3YVtkdF5upSjKCC3u1B1-O54Tr1COS_ZSo00P6GH7X3Stf5QgT3b9q0jv9HcZmGnbIZDRQhkJoyzefklMbPxObDYsLoYPdTYVNaj5wixLhXR9mGmg6a0q1kwLtDhLPm-WN7rm9p-5olopFlb9CKuMzuzQr9xHG7wrW-CVF9JIeNYdGZoDgcIqHh4tTXKJqF2jVOYJaGyLXPzUFm9JuCMbGwldkmNYNFpx_RfCFNolARGdQYknKzpK5b9vzlTx_1ui85IuOOcZJjeohOF5nwV33sAi9mv3uvdJMEA3yVM7MdA5r0bLCl_nPvXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=NhzIeof_hQuH9evrY1cthszuLCXUIzaFPANgSyZpiLTL3r10itKzwJmpJbE4PLHWvFEI-3INLDY27s2pkmRyFLWXTEZ0G-wuTetK-vVw6ULJtz3fDbgf6NIfqxJxBEljSj5a_O455mmbvG7JQCAj9K1NEQ1HBwQLkKoQJR65CiopQkeNxJ0JvasN8yMoXN62sCViv5TvUwesv_B42QPMEKxccpUL0PW-Z_Hg_Neq8ic96gdQD3m2cHl3y6XWw2MEvUe5ava95-7sz56lyDt2mLpBCqfpRb6162NigDWGb7IcEQ-A1ycS2o15tR7NNleK_2hV1zyH3c0k8WNT9nMllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=NhzIeof_hQuH9evrY1cthszuLCXUIzaFPANgSyZpiLTL3r10itKzwJmpJbE4PLHWvFEI-3INLDY27s2pkmRyFLWXTEZ0G-wuTetK-vVw6ULJtz3fDbgf6NIfqxJxBEljSj5a_O455mmbvG7JQCAj9K1NEQ1HBwQLkKoQJR65CiopQkeNxJ0JvasN8yMoXN62sCViv5TvUwesv_B42QPMEKxccpUL0PW-Z_Hg_Neq8ic96gdQD3m2cHl3y6XWw2MEvUe5ava95-7sz56lyDt2mLpBCqfpRb6162NigDWGb7IcEQ-A1ycS2o15tR7NNleK_2hV1zyH3c0k8WNT9nMllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLPnyaXT6ErTsBIXpLph40CickpaTZgLpDJCBpcVGRwrp8eKxQfx8ZbTwTplccaaLWO_yksGAx-CGUfHpDkOFgoz6fBkSjL-Dn_ihtiU25osMr99z4BD3CAOsL90utNsdsNWgdUWNZJBiumZS0uORkOWfCQiBNDIUoHSStTjt22Q38ofU0NyY398utlJrIvwtqDmaE8ICoZFha_IOeGImvIeqEVr-RX9Xp2T40C5S4V3wLEF0kw9O67gJDMho_IlHpelj-pS0Idi0IaXf0iMOk5aJuGYKnzMdK4YWNjuLZiSSK1MeKRlWs07FQ62D8M3-Nn6YMUVcbvv3MHWmbpUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD6SLsDgXFg9BjSxGWPkD0OQnsZ0uewgGK1nIWiaQrCOZXk5hCz7WGnhGJ9AvlC_LhX3_PYk3T0LoudMDiG2zeJVIWVVsrONemBujgtrrmZCkaiv17Ke0qjBiVv9SdFAzo7jgNBIr9oob8Tdi9Cug5ig7AsjsGY0EHDDDSxFfmKRPQSpY3UMxInSuTMXR-BcOIoMmvRVoVcUVdhocdF9hthIOfhGQWPi2mihptCUFcPcfihG3h0a_a6umMxlAhBarT4i3iZtUU53lhJhaW4LC0Y3fRk1mkSvZ54brKcwrzLewGH2rdrl_MA2CA1Qj_vwF77YhPjUdzk3OGlEd1huZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIcfpCZqXwxWzvb1p_nmeSh_OaZf_-tiItaqhf1ZX44LNYsFfSWssFdrnfs1n1qhl_RWRM6beKKhokDfZ5FE7s4bjYugTTDDqLRZviEaEl7TR8IFP6NPGoqXrlgKgv8wxInEdTxGQ-c9FSUDFOeuZtA8a41MSnDD-urIctrbCEcPAgu96y0WJBrtuaS0dLCn5Jue0JC3_YjWxWdezqsTKmfLLk34h98oj4T77-tWDjRsjmvkyDIGR6ZQ_k7y_KTKmAqV_yRi2RqA2UvXMxTBIBot24kbc50PG4TSZUT5isqR3ni0M0xU6MKuPn9oKLSnKMtndRdTSuMCMG-9ioen2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjVtR_qj7duaSO0DpzSZw6b0LVEIYBuvtCXnirIhynQNBhps1u_vDebb78PIR2pnwu3LE4AtJVKAQesCTp9E4YUZZyJvtiMLgd_YRPyZgvbcMTTRKrsNzeBWz2R1i7wGVvObb4pQb7lWowMQNPW7CrPP4mTtF652oHbbN-CgD3u8JPdOKU7D9Z5gnl7BsQtwPtFtuCPUBuzFGN5eF9uzp160UPkzLEjUwFWun3_5BuRUBAU5tiluuLmbna0cqnp_ZZafWDII-lPUWtlPfOJFjEBA7SN5qVleKqjA-LbTBmRsEKy6cmTLGDJScsqMvwEsHm1s5Ny6raLPVweofyJ4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7Qls39Mp4RtSLOoSJb3QSyB-UiIX5LzZZXyVonvD45AkMc7VVq4bi5xJUyYdEnokbZycF8kVMpIxNwYsLbQEO-z6DAYaUJJy1ujt9aScacRgXEqVoUASNQy7KMS3qEkF_gwRHSyURCK5EiyM6q4547VIp5INWiYxpLhKsVKW_SaVKtjwsqtPEKBnVdzLz7uBkT_qveNaet0wxRCjubipkrqjawWL-0AbVhFkchLX-6u-1YzA6J949A4QFWef2SfKMtLBDDBDGqM1vNsnLVAq_8h7p8BGiwnbWVDJgClQSTjfTNl0Ah1hGU5FgY4EVZLFB5ld3wXuuBKhmnsTbVqGMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7Qls39Mp4RtSLOoSJb3QSyB-UiIX5LzZZXyVonvD45AkMc7VVq4bi5xJUyYdEnokbZycF8kVMpIxNwYsLbQEO-z6DAYaUJJy1ujt9aScacRgXEqVoUASNQy7KMS3qEkF_gwRHSyURCK5EiyM6q4547VIp5INWiYxpLhKsVKW_SaVKtjwsqtPEKBnVdzLz7uBkT_qveNaet0wxRCjubipkrqjawWL-0AbVhFkchLX-6u-1YzA6J949A4QFWef2SfKMtLBDDBDGqM1vNsnLVAq_8h7p8BGiwnbWVDJgClQSTjfTNl0Ah1hGU5FgY4EVZLFB5ld3wXuuBKhmnsTbVqGMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb6HsWSnR8B9EWv4RB19327H5x7V0VeQYGiDfISa1iQBGZ0655sFTk6C5hbNYxPbxFz4CVtD-QMFzRkC3emo8xKWo53hLOOGmhdJPdfUV_hHjvJNNLf9Ygr11LUAZrldJyKeDeLYmH0RqTEiNMg8HtMJ7PeoPiGm3Ox0mJHKERVyEo0OzStkYdiQ7ltotALuBBf2jvj3GLsKDv7Dh3ZbloYIKrMaU0aZ-uuHz_Z2QLZt6ba6dpSPWuKGYPR-FS9yTcL5CJuVDlFrXKg3upB0_6IhigijUxp3Acj_mPjvRasAMZ-6ze9eXgISe79eFJXLvSfdwncvGQoqoMPxXYh0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOPlFjjL-7oKRHajrLHVnJF6pycjp87oQc1NAjHhZm0k864BiD98617zuTCbta3dM58MpTM5do1uLEKYwhokvZm76mu4-RiLC9Z_DGgzcquUc4DcN2oxd8E8MfURohRCd9_vS2wytjvz_b1kl2_o0YROgLpK2eTItt29XJvYGC-d_RtCBD6dOGf-q_dwn5rOhF4gDqhwINQ8ICUG9jprLyCTHKpcrmvN0i0QmbwRF3dF05NsIU7_FMRlOwOOtrOXvBzAUhAymRGsSAEYq5yT9eNKmqWnrI_gsQCmIXyqMswrpfMyhZkOwHDuGnpu3kFfnZTJZ0GqBuiA7W2EybsP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPU1XyElb8N7VW4dlACjPKpGSQcnUPJwKm38EuMdtgnjUsfXkq6qiv7o-s4mU61MQcEX-00hzGlignFAkbzQ-XM-W6SXYC-m7ECYyS7u9Y6QDO63VoA4VXPf7TTNNJU5DuMxj92ouT2H2aFo_eb8iicRBZaJuNkWxLfRtt6HPVXeYsAGrCPDpQoWlnS7Ite4FJhc8WDE3-mi2VMW-7Z5eHlxARO_kfv5NCer_0L45PRp-7wNymc59HEVuS5HSii8fxLPS9j1UxbwZE2KarIeZM-Zff-NaorSGXGgZNdwDo3oI82rC1PfQSm-xXr6T2h67WU91xnxZNbdbUCjSzOibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=mINN1oD8vjU-ktarvDC98XHEaKJvSagYLj2qIiYbd6yQ_jOIdxqpLDCFI4EZBLHIriISWI20fbkcVQku3SHch4OrTpzQ6e4TBWqqH7cOLvDhLsLIDTrj9hVUZSO4gCZgjaCEe-LB5KgUpyqPrGhtHbZSDihGltdYTGYS9mg49evurDcBK-k9i7xQdgcjTH08kXp3f8ljOvmNVnYCWACu-ObWhmVQog3PtnZiN3aLNb7fRfUypGaN-sHIDAF_N8qxaoipwrrr0J4oYF2XbiXOjqu-d_q9X5xkSSet5BS26oGBr4zSVNU-4K9CYpbySvreWglTS6SyvY79sjs0ugAabQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=mINN1oD8vjU-ktarvDC98XHEaKJvSagYLj2qIiYbd6yQ_jOIdxqpLDCFI4EZBLHIriISWI20fbkcVQku3SHch4OrTpzQ6e4TBWqqH7cOLvDhLsLIDTrj9hVUZSO4gCZgjaCEe-LB5KgUpyqPrGhtHbZSDihGltdYTGYS9mg49evurDcBK-k9i7xQdgcjTH08kXp3f8ljOvmNVnYCWACu-ObWhmVQog3PtnZiN3aLNb7fRfUypGaN-sHIDAF_N8qxaoipwrrr0J4oYF2XbiXOjqu-d_q9X5xkSSet5BS26oGBr4zSVNU-4K9CYpbySvreWglTS6SyvY79sjs0ugAabQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmuYGzmDnAgvmzTMntT9DYjsEJSHoDi-M6IB1llh6TaotJSp6braNv4-PFbx1NgOKeNUysv-xbD3j2kZ1Q-noFrCoUD8f3cDXv_PKcrDX6NZ852o2o_BRRy8xwfyi0OwmXiMr7TLoqPmlUBWD8dxaaIB5CftYCtKIyV5UlTq5EIHbMZ_OP99_E2KkucHJiKl-Lrx3azrjxeQ5YcMnLydDhIVKtfL1RSt9RNth2QOx8JjFV8Gwp0kZ-zK9SVMbvzDJvHjHnoIdm5n6t3AJmR75chmFSgVfPlUkrgiXSzcx8_QFuO5nxmNRAwz8j-dzQBlGKVn3qWzxKu5K9O4bOLkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg-U9ANFWylpA3Ne0Esee9ialcpMQCvtgt1eTokTQ4kP04oYvN1qUmnuYA1G1_88b83Jz9HVv50cfEOqhtYWI_M1QbmeNMt-mXgtLLVL-39gTsTv99Anzulf2xm6hCQjewz32ereB4kOEg003jwE4fWnWXVmb35b5pX_lX4H2HsPT_2aYGgejXDCrTdfAmu5f3JVYpTmBgKBQ3mr8zCxR10JTpKRteVlpNgSE88pap463RNCkxe4T_Ltm9IpWGhHmoyu3yTr-Ry5T90rs6hfRqjKLz2NMFcScbjeUpf6C2oKCF766xwmgLMAWDxw7U3bjwpBXRep8oHAnW7Uz-j7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC8MEfY5FL-zODfhbgPAsd7KVEEpvcAyT50sxq41WJucmo9vPZtUQ2pu05LxRx2Owft1qD0wkxk3Nke7mNKWwt7wJFpWGYABS6Nr5u2KVslsH19yWtaYNyjvmOrLJ4BDcHoVxaPHLsIJIcYxgROEGxVC5jQOejSTzf70TYwhRFnnz3iQVd2JDgsxoFQ0dhi8w8kDV6gogMMTAqZC8tWG5TM6z-IQgLRbIIP_JLA8lIYPNEJvTLj8mEnhX9RslyMa5Rg6FLCcxpcfqapTK8oBb3FrYRKN9fWUUdKMDguBwLxCfBbAUBUx5fssT_7BTrIjYpu1UBbZr3AulDzFwemgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzxTqA8FJrPX_Qv9WsINDZlWoZrbLxjmogP7vYSEsop_LHgX0qq-9_dHUFVrc_WzgazLvxtwgNmCDT4xyepZmfH_s-7Kl4-ZQwdPvjTfglQn76ZsfxRvcle9Xt-iEtdr71ozncm83cPTYZtCOxiRG39Ypue5v86JTWBjjWdebG4nHLqGQYbmBKe63y7x9_JVDmCE33bSwgce0mtYY3Hp0T16dSIKFrTgz0vGm1N0xjStoLZcI2mNl_8eE2rBmlQsjo5A6gCB-Nvm50OgBdT6C4oLQPqV3SnTMAbrGQRG9k9tbP3seeZOVa5wcAa2qVb061NvSFvfhE2AuDaUii-Zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNiz4Up29G7AzraXqk08nviHcXGpp7WtGJ1D3g2HkDezNZHTMq-xbDTnveYPWnzNsyUg4FJFuNmv_CXTw_47ItXiIFvDe9XRZwtzI3EVe_SUPNIu4T5OVIeKqrZt7ooAYECSQo-qjOwBmiF47L_clXXwht9ZQ3DDNVNDgrBig_lmiURR1dkcdtylM3fhYRTETAHMZTI2k2dN8fXBTEuR0K6QYGD2gW8iicXcacIju2Zhw36_PVSCVsQCRW8SO8d0vPd3-CFLylRK-og6wFB7njXB0pfYmxk0OKsQC-WurgN_DhTRSVClWOqz_AUWlJj1qqwIPGRpZk487UQiHTCtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgOHVzD1hF-NfjPFP0q-27Ycl5yx1R4kQ_bebultMw3JatnSXpPXkyOvDFsl04nvWdse2j5FH3zxr_tytwTisGxtxHnA112PQe7HIkTmn-fbizaJFOSfdFsaHzP1XBh04GXarPg6ez8JF80MedI0AX7DMX3kyfV2MtHkIJSy518scfbHuLYhtFRkuMp8yD7KeL4Bju3q6dKuphvxtAUHLxMcqFVM5chs7H7utxPSexprf5LDu3yNpUvnIfOt-nJX5uNAa-8I6Xz3Yeitb2ceRuVqu1XNw4gm8-aDURhPOY7PRLTtxJRiCfMnso6rg-CVchMTBE3bwXGto6M9V14_EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni_lVW7PSTy2LET8IkiqAXQe9cpyBwT6ifUyod5GdvEb2NmB_ltQUrXN8Pa2j-P_11eaw_HjW52n3axa1CYvVIDQrL_vCEFzkBx6yTVkWQGVd59e9-1ds2FtqcMqTcIPSJPVYi4-sps-sPKskrMoScnzeIVg7of8StxXhW0W846ZN0_2oXE1IlcbUOpGLVCNQIRfQNI7HveMlwz20jCPhLg25i2r9uO3HE-e4u3DM37ZWWx57WMJDwuoAyitSMUK1vdRrWdCYRGJffNPyksyMyS5SshpHUfWyky7iN2A4xGDY-cBSN1X-QQaYbGy2L8N37afxisr4t3EhHv6jpaVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUht6rhgsFZIllcvZfYa55zL1bw-JldXHWw0nAa7v7gLQqOdknpVibD348DUYhyezCl1ZcpuGQjss95ooFd-K9DDx8S40W3mUUwCQqbfQPJZlTMb2dSsMNqfcLNpVtsuwZhp_nLk6pZizqaD0BhYFexHffcol47gMUm4LIALtvgnojWaGNE75Id5MY90_dRhfVzQaQZpiO5npUozwxAYq1isc92k1_v39UJy9drc1AOuc-Hi6tMqRyBPJTyzfYL4bQGD8mTvgra_BG7vjydfxSMEffQpIr3EgHdi5xuE9PHZ7hJtguSoVvp2jdQX3f89FigNnTX1m7eVmXks_IoFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt72oY6_lV_7ntlM8uKf0gWt7YZR3uf_SXW1UKMFj65N-_usvUiJLMCUjB8yV-zK0wM8nRu2WjEPWMxlfrShPdK5l44z8LnUQ0NZri7527K6JXGyrNzt63TRnUbWzUpj1yEPNLznw8xPSaJWOuCi4la__CTU_upW9TS8NiHzKZkIPZ3AXrNbQ9iD1y5hKM8ci91Kpk139yEEs_zB1owYN44VNU_4T6oFf6jr-spTJ30Z18944He6GssTOedeq7oPMbGxeHuqStg_PeL4uXpUjJOWy0XivXhwYw5RNQDoqMBV_baPjKubeNPruPlH6wsdKbFWkp67r6yVj7dXZtfQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=CzNFa09EslT8giYHri2D2h6nfqQck2jYXUI7eQHSMc9Sea9U7wmOPQDK0B87i9A9VtLGNYOYzsAy4HH3SzX7anOPnwNqeDYttby7xvBh09irpg6Sd5m7phJ7Dou4PUFQRG2p1JksvVlGIvpNxk44KodAoi8DlTcbrf1MnjyTsOS7RFKEvR8Xz8lE5zDTvkcBZ7OWlF0pRK4ue1Zhf_21a8Gw6LqtbRWVwrfjEmBpUC23cgNISYnUSwJkGA3JLd2p1MMzry_9sREtr-R-WvyTkCTnNWgZMcWqaDnW6TzOkcb7yK_qMe-sf4DEpmF7OBoFVIoTDJ9S7JmmDln2C1002g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=CzNFa09EslT8giYHri2D2h6nfqQck2jYXUI7eQHSMc9Sea9U7wmOPQDK0B87i9A9VtLGNYOYzsAy4HH3SzX7anOPnwNqeDYttby7xvBh09irpg6Sd5m7phJ7Dou4PUFQRG2p1JksvVlGIvpNxk44KodAoi8DlTcbrf1MnjyTsOS7RFKEvR8Xz8lE5zDTvkcBZ7OWlF0pRK4ue1Zhf_21a8Gw6LqtbRWVwrfjEmBpUC23cgNISYnUSwJkGA3JLd2p1MMzry_9sREtr-R-WvyTkCTnNWgZMcWqaDnW6TzOkcb7yK_qMe-sf4DEpmF7OBoFVIoTDJ9S7JmmDln2C1002g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik-q0pUE7rND9NW_xQbmQ23q_Bj-XVNe9l2lLtmWr2Q5HmTmodmFico4GrJ-8PHeMWsRrjZ7VfR4DUyZsaf63NH9MZwGUAiYiPrZVsDZSKsBOAc83dWnmcqXP1J3_kdeMCYY06Mle_uv-pJFDlslvK9uB72_U4QYlJKxI0ft7bf8sAA9hW6bs2VFoOaVgKD7AwVok1mLmjs7CNl1324OYUWgEYtAgC4ZBbFq5YCj5fhk-ciM2XYaB0Co4PyxnfPnMi8YaE3i8axKfwk6FIOtfUGgTMKwErRT2WVQs-sgTS8n3NdEg-dO7JJfS2cy_fiD_HHDmQ5EaaoaSwAqwTNPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=VZi8jikQxT4h4Xcn9H6XVOMc7nPBEc3DSaHLMAXAqv0pHFkXdycparUvBZ-NXKhfgrFNAw022UlraG65e1n0dQQJb1MiuAD3v6i0BO1eQzajyhUq9YMuzTCsMHk1kvJI7mLuojDB5pVDWVgJfjd-v6ZKJB5C9NqD67jEZOveFI2o7o0V6Ptq5ZvgKe-Z7y8LU3RdNrA92RDmGQlvtMdb0CbBTgVGSxZCMmNZYMRJF_iMIZsZ4qzf8CvkMW0xXG4bsQvw8-P20WxXtb7u_xBu3Jv0rf44IgqxAbf-1B-stVs1C9hn2tkS8Vw-DXpVuFqwROB8iNsPsE1nDumXPtQfiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=VZi8jikQxT4h4Xcn9H6XVOMc7nPBEc3DSaHLMAXAqv0pHFkXdycparUvBZ-NXKhfgrFNAw022UlraG65e1n0dQQJb1MiuAD3v6i0BO1eQzajyhUq9YMuzTCsMHk1kvJI7mLuojDB5pVDWVgJfjd-v6ZKJB5C9NqD67jEZOveFI2o7o0V6Ptq5ZvgKe-Z7y8LU3RdNrA92RDmGQlvtMdb0CbBTgVGSxZCMmNZYMRJF_iMIZsZ4qzf8CvkMW0xXG4bsQvw8-P20WxXtb7u_xBu3Jv0rf44IgqxAbf-1B-stVs1C9hn2tkS8Vw-DXpVuFqwROB8iNsPsE1nDumXPtQfiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVCRNvyJ2dV3bGF5QXrD4hJACijZVfWBkB3vlaCaRVr9IRwv4HaunMahlOYUz-XWQ92Gwqs9Z0CdKgxYpXheE0szYDpVtnSjPXBwB9rveTOdYELA2OOZpU8FRUJtXvL3jlXeVcTg6fuAC6SRNEph0hhiVhCN8DYQCvFWs2DlJBkIvVQMr3x7FSmyghttifOdTF_0PEWYwZngvZEs-Ua8gFg75CwEZiOCMALfzJZQbl69PlAw3fIGHCgaT4rKvcvG6yqxyo5aoujrh5rSwVWENVqyhzyRQOmhhR1dhop6_VcjHf06umLpOlh1N0I1N97qcDVtu_KrRPCPBBcvZ3gwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drTW38h8lsZJ3tEkUbJbk73Hy5gvK2Pq0db3tN4_PlZH9jhmUZIZuqLw_wBKan8K5dEY_6uYO1b-yHfzXTn6TNOAf-f-0fHFw_IvamzuwEksojehsxQYXvIBCRkaKGqk8chpP5JJ0bYm4d3RHJKiZBkm4v4DE6seGjZulMEV7n83Zs--5k5aksyiEwBPLP018jNri72D5PRlHCwakNsCYF-vPIJV0ak5-IVo4TFdkf8LNWSSemT2eX8XIU8pW17FoPqyXW0OS25FOy_vc_j1k2gmSz-ZdYWOAK7zEv4t3V-AMElG-rFcwumD4bycnwGaa97scPcby_nJ9TGy8YFBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=Uxf2qcuBljw3N-SgIm2ZeFfQSRRDHknPUtMkHF1ShkhoYvRhNkEjeOoewSK9bSya-Bipg5EkTGjqU20Vh8uKDdAoRnhJA3sEVFE5IEOPlPcg2Dpn88N2xmuq8MRJIdoSKhIWUjIMeaUJtBxbunKr6NCZsfWbZr6W2JmoJs5xWJM1lUqCoghCPG_JewFGk1jVhj2ZiSUnpJ-Q_DoGPSL2u4D0OwU6AqZC8BZI2r8QtCiz-xjzsFCZQoJQNVyUfM6LrVnrs9nkSyruV149FBUeHGbuzpx0fdSa-OmuaZ8TyTFmAWYQ1NFeBLPGw6Fl0WVGZ39eL4lrA-z6KhwoZnCJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=Uxf2qcuBljw3N-SgIm2ZeFfQSRRDHknPUtMkHF1ShkhoYvRhNkEjeOoewSK9bSya-Bipg5EkTGjqU20Vh8uKDdAoRnhJA3sEVFE5IEOPlPcg2Dpn88N2xmuq8MRJIdoSKhIWUjIMeaUJtBxbunKr6NCZsfWbZr6W2JmoJs5xWJM1lUqCoghCPG_JewFGk1jVhj2ZiSUnpJ-Q_DoGPSL2u4D0OwU6AqZC8BZI2r8QtCiz-xjzsFCZQoJQNVyUfM6LrVnrs9nkSyruV149FBUeHGbuzpx0fdSa-OmuaZ8TyTFmAWYQ1NFeBLPGw6Fl0WVGZ39eL4lrA-z6KhwoZnCJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huQWXgi7uFMPdzDHiU169t-UKdV0Zr5Pym4W1kH7pvdLxG2OFUeeLlqdgA8piLbqHR1nQlZvko_0UwZ9nBLGd0QuVLoVPogujSlwndxb4K76pQqGSDGiws5gS22U-8Sstbea9wGA3COV-jlpt31QpX739ky3v9ABUI_kZWnxWiPB4pnLVOeG9sFhV18S5-G8tHloLn7CHXcrAtTeUXws5HHL52EePGXB0NG5r4NpK5vggTR2BzQwv7iZP43fBuajh2NmF4ZcZiR4iK9AycSa2_qWbgiPPYQf6kZ2TIu2P1nKvk3kN5AEkHpa1XbLyBLBZdpKaSJODjwczjEz6h2ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
