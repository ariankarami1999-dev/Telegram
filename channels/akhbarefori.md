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
<img src="https://cdn4.telesco.pe/file/PDgrB4vGEfeYGq1eUfOS8P1nw22r5D6RAEDR2s8FAEq9ltpQtIvnFbdb4gZ3wDVVpmMn8WUjo503Z9TxtGJPd8YIJmZbN6X66I9LydBfwHSupY1KPXsx6ElPCyvndMtseNlgAga4hxgVjxMOfY3XDrR-X4mxM0PHbTvvb-0kjq_mKalwX9OTIcOo3TSmN55d4mqdtNyEbo0ZCEVbRb_e2nchR2ojI6_Kz1bn3SlXSdnENHL7j3k8F1r40Vqu6wYKbF8b0H9CTvw_pkdNwsBSRyKj0A9p0XCiv4pFq1hgb1P1lZ2QT8f0ZOV2qI1FhVE-8pHZaL0gRsq-25VBscbgbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 22:26:50</div>
<hr>

<div class="tg-post" id="msg-671538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از کسانی که مذاکره با ایران را رد می‌کنند، راهکار جایگزین می‌خواهم
ونس، معاون رئیس‌جمهور آمریکا:
🔹
نیروی نظامی یک ابزار است، اما دیپلماسی ابزار دیگری است. من از آمریکایی‌هایی که می‌گویند نمی‌توان با ایرانی‌ها مذاکره کرد، ناامید شده‌ام. پس پیشنهاد شما برای اینکه مردم را از تیراندازی به کشتی‌ها در تنگهٔ هرمز بازداریم، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/671538" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مخالفت AFC با درخواست فدراسیون فوتبال ایران
،
گل گهر نماینده ایران در آسیا شد
🔹
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/671537" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر روبرتو پیاتزا درباره کت‌وشلوار پوشاک زاگرس:
«کت‌وشلوار خیلی عالی و کاملا مشابه استایل ایتالیایی است»
«زاگرس؛ تلفیق شخصی‌دوزی صنعتی و دقت در اجرا برای ارائه‌ی محصولی با استاندارد بین‌المللی»
📌
مشاهده در اینستاگرام:
https://zgrs.ir/zi
🌐
وب‌سایت:
www.zagrospoosh.com
📞
02143064000 (داخلی 330)</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/671536" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
احضار سفیر انگلیس در تهران به وزارت امور خارجه
🔹
در پی اقدام ناموجه دولت انگلیس در قرار دادن نام سپاه پاسداران انقلاب اسلامی در ذیل قانون مقابله با تهدیدات دولتی، هوگو شورتر، سفیر انگلیس در تهران، امروز چهارشنبه توسط علیرضا یوسفی دستیار وزیر و مدیرکل اروپای غربی وزارت امور خارجه، به وزارت امور خارجه احضار و مراتب اعتراض شدید جمهوری اسلامی ایران نسبت به این اقدام خصمانه به وی ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/671535" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوه قضاییه با قاتلان شهید عجمیان و شهید آرمان چه کرد؟
🔹
دکتر محمدحسن رجبی‌دوانی، پژوهشگر تاریخ اسلام در محفل الهیات انتقام از نرمش قوه قضاییه در مقابل مفسدان داخلی گفت؛ افرادی که باید به قصاص و مجازات می‌رسیدند تا در نهایت بتوان خونخواهی و انتقام از امام امت و شهدا را در خارج از مرزها پیگیری کرد؛ اما خیلی از آن‌ها به سزای اعمال خود نرسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/671534" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجارها بار دیگر در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/671533" target="_blank">📅 22:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سی‌بی‌اس: مقامات دفاعی ایالات متحده در حال بررسی طرح‌های اضطراری برای اقدام نظامی احتمالی علیه کوبا، از جمله یک حملهٔ هوابرد، هستند، هرچند که هنوز هیچ تصمیمی گرفته نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/671532" target="_blank">📅 22:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پروژه آشوب با تصاویر قدیمی؛ ادعای تجمع در پاساژ چارسو تهران تکذیب شد
🔹
عصر امروز، چهارشنبه ۲۴ تیرماه، تصاویری با ادعای اعتراض مردم در پاساژهای چهارسو و علاءالدین تهران از سوی برخی اکانت‌های ضد انقلاب در شبکه‌های اجتماعی منتشر شد. شماری از کاربران در شبکه اجتماعی ایکس نیز با انتشار مطالب مشابه، این ویدئوها را بازنشر و تأیید کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/671531" target="_blank">📅 22:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک تغییر: اولین بار که رهبر شهید را از نزدیک دیدم، فقط مات و مبهوت نگاهش مانده بودم/ آن‌قدر آرامش و نورانیت چهره‌اش برایم عجیب بود که دیگر هیچ‌چیز اطرافم را نمی‌دیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671530" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/671529" target="_blank">📅 22:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل اصلی آتش‌زنی فرمانداری و کلانتری شهرستان دهاقان به دار مجازات آویخته شد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671528" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTf8_8qxH-JvCUXreaAqhlZg_76JSwAmIVr4qFEXSeMSex7bvDqiwGzAaxl0feF48xiIIgLQA-jvxnWpbxy1v5d00QT2EtmncFmCnozoDML73MclSJgPFwQTbrBeGjoMsIVMnNLMFEBkOPQ17exK2EeUmNv8mXMft7umpNxSC1Sr1-DZbc8uzoGAccmHW3Sps9V56IQcOn_PxJ_45RX3MjJhnxdovBJ6klxxT6a6sBHnmz2FMlhtVJz1q8Hu4wmwvPtSDUjb_JDBrjqyp2QFxDncLML8aMdjEH7i8PZC_E8OnLLXZcn13_gsnDRvzdulwHEjvJyKka4n92bGjkSw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_xrWNfcOtxwznTC_BYlIWwWNoQnccaUntU9A_5JmQfalE47qf8W6HoNtq_ysTEHsmJhVz5GK2pL-4XKzQRQqEHM_0bg7OjT-y4xYKw2xi-dtlMo3jenNdNTYXycmAh_iygSk1aFlxyyiQm0GBD9Vm63fUrjDZuVdaKFgBXa_ypxD_sbZK9yTMxS88OtHBKuMjjb_qKxljvkThA_th9gH4hQ2-6CkCaUwzvt7ehqODMANcxbRT2wB-b24ta2nT8iH4qqnii4WFTlvv0D2jA8ECnNCspmoB1FuHQvhpV475H_m8HkQvxuqsKsi3HQ9lmjXsTTM3CR0d4NdkwCu9XNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH0XBfV_0VRLsS1J1ChcC5eelRp77EJMPokvNWVpZTa81r0cskulhzIQyqiB-9dfSsEQj80CbKiFe_r47oGRAj9B9DfkMmuS8SAF7QTu1HBA3xoi3mm8o8uRy7FcIYARR6nWF2JCq7s2kVDU3KSnWvdjxLVRq-9YmnQhl_zV_TqWKwlhOp2-9eulrsAAIWjHcunRAgBUCQls6LGIiIVXA3QBz2U_uBABvKik2E7MJTavwJO777DvW3ZLFw4iH3bXGr8QhLJhN48wyUSyUvbFVr2gVews8ZE8BirmTdnMA3-PASry5nI052VvYz9psLnc5wmKA6UvMbfMmeoK7gQxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqA_yfx4t9SKgS0KLQriB5bD8jTnpBkL5XNoRq78UUJj3d8AY2FAzc5z9dtiAtYmwwWAfcG05mu-mn9u_vkGp5Uh8JV6koUpBaiznmXcmuc6KHbLcQWE2QIoL_6vvKAfKeyxbCEjl0B50zjuXKIxuvhGX1HilLDAwzSh0LNJa7v-wobvY3_tHJIbFUS9KMYDGlBAA99kX41iRu4PyFLzxrmqYYMLTYb8-HYfnIs1ShhCeH730IBUg1Ppeskl8Wnq7HW2E95EF5Rt_GUe-A_D_bGMHV33-eVwouAByQUchRdshKhPaZaBfxlf4gXg9pSxKezu-CFGJGgU2BWowTGUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwe3F5HlLwtX8xPJlGESGZ6Ltou6Jth8IFCUpAq5aHxy_dKw8TKWGQmQTa57e63ugwoEiEjCg2WhkO6nbODi56YL6x98WJMWfqqBgeWHNRtz-aAqiO9jOWb-Ws7OwXyCuTYFHf4zPVFCZYWlxh8sZXikQxPJZqnt7agAoyAUGPaYdwcguXQlY3PFPl9L6p-b1Q_FpozxQ17aEm3KNw7VyYu3q2NtAqKa2if6ZMlYbF5Qyznu7xfEgstExCtwNEVz1M7I8wZUcI4VJhccrZbl2DNL65QEodFAuSY8XaOFnHgbwlF9hLAHLC5BbdgIpD6RKv54CT6MDcnesxeFGRQdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vz6TRtA7f03aRqb1bAgVih42-APMTaRsjLCrJaDNxCXaHOT28OstNMv7u_iR3dHb0_lTRwm-_UF3PDaAIIt8ptGPxXlnmhtQ1OlnE6oY37nEzZfmb562zplU6x-0Hwh7DKpiwuNnj4nCycxFehVmYPyLPFbj-4uSfT0lObCKIAmyUCmxZNNFn0jT3bC4C0uzdmsqImoUgR32QPTGrMYUH5UnorbifiRJCeJlqdWhpynBYYpe-DfZQGUfxHPpLb2s9Q_N2pwjIJ1GlXYGiEa_UhNWKxsPB3osVSpMNT0RY-RXxd0g-D6WCSgG1PTbE1dat-MlNTsiqDnNMGhnvE3FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmbOcJXdhBeIQGAxSbgw1F4_p738MDvBrAIU7nmTecSSJ0UhUlxaIujOOZsuPUUZ-j5dHhyjfn_CAP-npRr7yUa2rr3qhMTK76JbuBAqpLBfxz99nRTup-G-XBx77k9CvlCpSmenuSe0ir-JNF4FlqRtRbSGnTBbIxHKpq89jecCe0iQgLRMCeMDJyv7CVsCemhwZoBnkmEI2l-YHyBOrcfYwImOm_YgaeA4ZthSWYzQ5XOV4sYm-TeGQoiPjVUM5Ufio3w4OpvPxA1OCaFjFbqKyRCnzvmgj9jq6s5Ya_Fz4kPMG1-BnVamhqcD-uDqzLihQg871cYXa6buyrnWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3TFxuu2O7VV0x7cyQN7MCz99D_vD4uLzAzkcqPLBSGIraDXn6Wy-bQPuZcHw94Ce9Ms7vFdtyc20c2t6QChU60z-sckZpUWGvjrjPkd1YI_LLgws5XLED2vjvrd73NQUxLtcNKhxcl2RvfN75a6kf7gdx_VbirFRko_9-OmI2DOqyOlNXhxZWwPpjrFHYTabZvvpIjKFDc_p8sYQwcwh2QbzN3309BTEf25u5D6j3sMC0WRYIkVwyhWbaVgykSFe4Q0P_v7Nrlk8xgrPwcjS507OHkHLQls6Gz9OpWs5STN3Mb_I0RHoCyijPOf3AeBWDo1MH2CQwyUGETUUGtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqvp3vRaSflKCUokDsKgG3Uy-0R8u9ixqutmpUJkhCb8maPZ5BfkKhxhPq2660gmkXe66xVmviyZvfaKz4_vAKT31cnfeCKOin95BcgWRxxZADZEfAgPFj4py7P5OeUGM2lAkPSmez9MhpxAnorZnckhUPuiUwDtj4F8ZOgqs-zBQ3zybWAwF74vGDS_cQ4F9SXAgjOaWHIHmlMsxfarKmVQJyOvObtso3B1zRr_1pltgL45uFaWielSMCqkaBKZlbWlrK7zQ7fANNXn1MUJJBzq9n07ejYIzwIbFPNPKYwu9b6475o0irwzaGI7IDEANjSDT_efky89EPF7G1haGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfqLt15qgXvwqit1zOg0gasl2EylADyPREbJJTDS0B0j-T0_cx4uzMIu5EHnFz7u4fUt1jkef0fUASt8LwytNEAPg4qPMRPiRTbP3ftmFoReU8Hs_ufR0_a3WpjQB8pFhlMoqDSkaQAGM3ScQhmHIwqF5N_sgkeXotGO2rTgjRAuL34RIhc8kEaArW8ZPnBNYJ4QE9Ybi4FHMZBJILLMLxNX6C0jKQp0KaOGbhiPsPrwulPJDRLmCkf_RR3vNhsBRlnsfOEJXLe_iarFALmzg6sBZh4nXOa5lpRHdsWMWx_aEUh4IeEl-C5N1h5aDX1Jk5NQLOnAmK2h0zw2J3QpRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/671518" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
معرفی فیلم: کتاب قانون
🔹
ژانر: درام، کمدی، عاشقانه
🔹
امتیاز (IMDb): ۷.۰/۱۰
🔹
خلاصه: زنی لبنانی که پس از آشنایی با اسلام، با مردی ایرانی ازدواج می‌کند و به ایران می‌آید؛ اما آنچه در رفتار برخی مدعیان دینداری می‌بیند با آموزه‌های دینی که به آن ایمان آورده…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671517" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شیطان زرد درباره ایران: من از تعیین ضرب‌الاجل خوشم نمی‌آید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671516" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی نظامی یکی از ابزارهای حل مسئله است، نه راه‌حلی نامحدود
ادعای جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
کاری که رئیس‌جمهور بسیار بسیار ماهرانه انجام داده، این است که گفته ما در این شرایط زمانی از نیروی نظامی استفاده خواهیم کرد که به چیزی که سعی داریم به آن برسیم، مرتبط باشد...
🔹
اما ما قرار نیست کاری را بدون پایان و به طور نامحدود انجام دهیم... ما سعی خواهیم کرد از نیروی نظامی خود به عنوان یکی از ابزارهای متعددی که برای حل مسئله در اختیار داریم، استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671515" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مأموریت من تحقق اهداف رئیس‌جمهور در قبال ایران است
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
این همه حرف‌های بی‌ربط و مزخرف وجود دارد، در حالی که کاری که من واقعاً سعی می‌کنم انجام دهم، تحقق آن چیزی است که رئیس‌جمهور به من گفت تا به آن برسم، که همان حل و فصل این مسئله به گونه‌ای است که به اهدافمان برسیم. ایران سلاح هسته‌ای نداشته باشد؛ جریان آزاد نفت و گاز را داشته باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671514" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انتقام دیگر هیچ خط‌ قرمزی مطرح نیست
🔹
گفتار مهم استاد رحیم‌پور ازغدی، عضو شورای عالی انقلاب فرهنگی  درباره از بین رفتن خط‌ قرمز‌های انتقام درباره انتقام امام شهید امت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671513" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ونس درباره مذاکرات با ایران: نیروی نظامی یک ابزار است، اما دیپلماسی هم یک ابزار دیگر است
🔹
از آمریکایی‌هایی که می‌گویند نمی‌شود با ایرانی‌ها مذاکره کرد کلافه می‌شوم. پس راه‌حل شما چیست برای اینکه افراد دست از شلیک به کشتی‌ها در تنگه هرمز بردارند؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671512" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671511" target="_blank">📅 21:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اعمال محدودیت مصرف آب در فرانسه در بحبوحه گرمای بی‌سابقه
🔹
وزیر گذار بوم‌شناختی فرانسه مونیک باربو روز چهارشنبه گفت که این کشور با وضعیت خشکسالی «استثنایی» و «بسیار نگران‌کننده‌ای» روبروست و تعداد بی‌سابقه‌ای از مناطق تحت تأثیر محدودیت‌های آبی قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671510" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تصاویری که می‌بینید انفجار موشک نیست!
🔹
در شرایطی که برخی استان‌های جنوبی کشور درگیر جنگ با دشمن آمریکایی است در همان حوالی، معدن باریت آبترش رفسنجان با انجام عملیات آتشباری مشغول توسعه عملیات معدنی و افزایش تولید می‌باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671509" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/671508" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی هوایی روسیه ۳ کشتی باری اوکراین و ۴ قایق بدون سرنشین اوکراینی را به این شکل هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/671506" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به مقر تروریست‌های ضد ایرانی در اربیل
🔹
رسانه‌های عراقی از حمله موشکی به مقر گروه‌های کُرد ضد ایرانی در اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/671504" target="_blank">📅 21:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» در بندرعباس
روابط عمومی سپاه امام‌سجاد:
🔹
امروز یک فروند پهپاد «لوکاس» دشمن متجاوز، توسط سامانه‌ نوین پدافند هوایی سپاه امام سجاد تحت شبکه یکپارچه پدافندی کشور در بندرعباس، ساقط شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/671503" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تداوم حملات توپخانه‌ای و هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تداوم حملات هوایی و توپخانه‌ای رژیم صهیونیستی به مناطقی از جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/671502" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام امام شهید، یک مأموریت الهی است
حجه الاسلام محمد قمی، رئیس سازمان تبلیغات اسلامی:
🔹
در پیام رهبر معظم انقلاب واژه‌ای بود که انتقام و خونخواهی را از یک سنت جاری الهی فراتر برد و آن را به «مأموریت الهی» تعبیر کرد
🔹
برای اجرای «مأموریت الهی» همه باید آماده باشند، تلاش کنند و برنامه ریزی داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/671501" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مهیب در اربیل
🔹
منابع رسانه‌ای از شنیده شدن مجدد صدای انفجارهای مهیب در اربیل واقع در شمال عراق خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/671500" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671499" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDF1PtQ-FJG1DDIpberz15WZchVQAdljVFBbm-p7nkPMiv1qO4_eKlbVaUdp1aakD6IoiXtD7WNzM-U6Rmvpl8F1Gva54ked1HauiUo3y1TFVAVPOvxp7q6PnPYqTgconryodZ5bimiGpO4jyTsCLnMEK3Tgs8ww972m_AzlHG_g8t1x6hX8mUicqYC3k5kM1_xOL91bdqY2w4s6V8GkCNGKOxLN4vwoqcQRVDXQmhHLVOyIBSa7g4nb91oHjNA3sgXdTneXRpfNxnCptF72gdjh4WMLMxUck8jsM0NBUumNiHgBGdpYBYUE3ofYlMuStSRwJ9qFznnmLJbRYfhbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران یک جان به‌هم‌ پیوسته است
🔹
ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/671498" target="_blank">📅 21:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
قالیباف: مردم جنوب کشورم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما
🔹
به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید،…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/671497" target="_blank">📅 21:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
قالیباف: بنده هم در میدان دفاعی و هم در مقابل طراحی دشمن در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/671496" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/671495" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671494" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف: همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/671493" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
♦️
قالیباف: مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قواست
🔹
همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671492" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
قالیباف: باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم
🔹
جنگ و مذاکره دو روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ، بخشی از راهبرد…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/671491" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
♦️
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔹
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/671490" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671489" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/671488" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHOLv9iYoXVLcOzAcAm5wM1bfCw4MyjaSM9blB4uaCGmFcGS0VzyPWwWKBc_wDxX5AUtGscN2TkrlWNBMl_ewmf8NdAcMFZ-D80cHuDqFl-4d9Jpvv16z8_qPfilvRuvsoheVs2BeyhgKSDcxCCq9djTS3eVHckkjbmw4WmNFVhL_LKV5ZZcFtPgue7hFA1GFyHIq6cfMJjDOXJr-18zognCTn-g64P52JRHNAWotZeN5Oxyx4Ngu34NBArC4f-NNyf4P2sGMsPxTUpAG-XvsoB2IxE0Rxhqm_RUW2S5qlaq5GEAviOY0pwlhCH8WZCFhUZi_vqQrRzI3HxJDY9qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، سلامتی شما بیمه است
رسیدگی به سلامت دندان‌ها مهمه و داشتن
بیمه تکمیلی مناسب
خیالتون رو راحت می‌کنه.
✅
در بیمه‌بازار
می‌تونید پلن‌های مختلف را یکجا ببینید و پوشش‌ها و سقف تعهدات را با هم مقایسه کنید تا انتخاب مناسب‌تری داشته باشید.
🦷
پوشش دندان‌پزشکی تا سقف ۴۰ میلیون تومان
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/671487" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/671486" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/671485" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/671484" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ رعدآسای ایران
🔹
ساعاتی پیش در کویت، صدای انفجارهایی از نزدیکی پایگاه نظامی آمریکا شنیده شد. برآوردهای اولیه از آسیب شدید به تجهیزات و نظامیان آمریکایی حکایت دارد. با وجود سانسور گسترده رسانه‌ای، جزئیات کامل عملیات به زودی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/671483" target="_blank">📅 20:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط تیرهای برق در نیویورک، چندین خودرو را به آتش کشید
🔹
سقوط دو تیر برق در منطقه «کانی آیلند» در بروکلین نیویورک، منجر به بروز حادثه‌ای گسترده و آسیب به اموال عمومی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671482" target="_blank">📅 20:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اکسیوس: دیدار با نتانیاهو در دستور کار ترامپ در هفته آینده قرار ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/671481" target="_blank">📅 20:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
🔹
رسانه های عبری گزارش دادند صدای انفجار در نزدیکی یک واحد تجاری در منطقه هرتزلیا شنیده شده و پلیس رژیم صهیونیستی تحقیق درباره احتمال پرتاب یک شیء انفجاری را آغاز کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671480" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دبیر ستاد مرکزی اربعین حسینی کشور: همه مرزهای اربعینی کشور، از جمله چذابه، مهران، خسروی، تمرچین و باشماق، آمادگی لازم را دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/671479" target="_blank">📅 20:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix0GF255cVZjj69Qlsi1-MYlt_i6sTHpbeFk9Uh1NWq5TiAuQ_vI8nWnnla96ViMcwUKPmxszZvO19n9pmd2YEnjjdPKGRUdCmjxG57XYcpbQ6aF72gVBNsz7z4Jx1TgQgfq5rCo7W7iN07PmnRvb2mTLVlCdrCkSE453i6Wi6n7WBw8LN_bvpoRyvr_8tGFOyDnL542xR9xFfsTuTbnNuXwRr5VdJGCNroKB4aMR0aT5vjcJKzJnRa8lLAvCNBiynW618EQa4qdfVK8EEV_LRpH8rWsniNOhwXiOMOPg-aF66sq3hJZc_GjzslHeqjaTv8-Tgw88AT3LIRdeWxXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/671478" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاقانه‌ترین وسیله‌ای که امروز می‌بینید؛ «تلاک» به خانه‌ها آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/671474" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
خبرگزاری یمنی «سبأ»: فرودگاه‌های أبها، نجران و جیزان عربستان همچنان تعطیل و از چرخه پروازها خارج هستند؛ این فرودگاه‌ها در پی حملات موشکی یمن تعطیل شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671473" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
تجربه‌ای شگفت از مرز مرگ؛ ۲ ماه کما، ازدواج در برزخ و بازگشت به زندگی
🔹
00:06:30 دو تکه شدن موتور در اثر شدت تصادف
🔹
00:09:20 نوید بازگشت به دنیا در اولین دقایق تصادف توسط خانمی با چادر خاکی
🔹
00:20:30 ندا و فرمان به انجام سجده شکر
🔹
00:35:40 نظاره کردن امام حسین(ع) هنگام تعویضِ سنگ مرقد مطهرشان
🔹
00:47:20 تناول انار با پوست از شدت خوشمزگی
🔹
00:56:50 ازدواج در برزخ و تشکیل خانواده
🔹
01:04:00 شفا یافتن و خارج شدن از کما توسط انگشتر امام رضا(ع)
🔹
قسمت دوم (رهگذر خواب‌ها)، فصل پنجم
🔹
#تجربه‌گر
: داوود سلیمانی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671472" target="_blank">📅 20:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
🔹
این پروازها که پس از پنج ماه وقفه اجرایی می‌شوند، از امروز (چهارشنبه ۲۴ تیر) آغاز شده و هر هفته در ۲ نوبت، مسافران را جابه‌جا خواهند کرد./ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671471" target="_blank">📅 20:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWpQLdWmRX5As3LSI9hR1DY7K3ylC27kdrraWsVX5WdhXEXgH1mYpBaBZ8Q9-VIuR7lUb9DyRShJzNctk0Yv0SNAeAVk1jY3q9vGV8GTMb9dKTh9ObyuBnckX4bKFrDONlmdDKq6ZGs4T_uNll6A9ah7hY-cEpJGPW33fLtgB0HMCTfgtFxLVgUBMUueco-V5aTAOERUqjmqeB3-JfHuuzEAjV1-CppEIsx0XC9vBG34InaGxib45B6_HTve52H-jJmG-yKssznzRmvEthGFyw-gUTN6PTTEen17c-rNvSM1SBfv8Nm8MzI1D2lT_NCEV1LQk9lDRc0Gi7rQYrOSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست سوم   ایران ۱  اوکراین ۲
🇮🇷
۲۲|۲۱|۳۰
🇺🇦
۲۵|۲۵|۲۸ #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671470" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آمریکا جنایت خود در حمله به انبار گندم در هویزه ایران را انکار کرد
🔹
سنتکام گزارش‌ها درباره حمله نیروهای آمریکایی به یک انبار گندم در هویزه واقع در استان خوزستان ایران در ۲۳ تیرماه (۱۴جولای) را رد و انکار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671469" target="_blank">📅 20:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671468">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXNyvNkhoREMd1UJhNqd8taLeTDz4kqNDBsrFYqk0mU5RaRelhJ6VSb7s34IEv7_Rpl2hAPgoRbaVlIj4xWmI2d_8qKqCqCqqQfhiTaKlF4JoNHuZypKt8S8L-EosrK77AzOGr3ZlgsX2xeR9XwKKmlFUzhR1yYN1Uqovyc3oGrOtrgctp5cfHItvXkh2PyYXua6ZuPWnig63m96Kx5cE8XGe-SQ15_gAq2ur0YEiX3yyLf2ACNP48DOKQAgzqk0V-0ldrvjn6uSWZyKQGk_RKI-sxSuh6KYRRGYjZqOXp6tGu_5dQHcIQ6OqeWXCo3HErptvxjMFmN1VxnTwbcQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت یوسف پزشکیان درباره موضوع انتقام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671468" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpH-MI0tMitkw8EHVpB8JyiubFfeI6bjg3EsnhcgclRLh358G_1_vIDowbEmSxyKCcpgY0sXDoAwSkZwcvxqsB6t2qx6ntXcV4-8pSTFeZakSpSGk-1mBPEDVIL7VDahJz-GELbw_nooTaYgTZzagmiTU9TASCAafExU9tNGciUyDdi7F0agVaVcqBujB_v_hNMAfGOYfTKGSyzF9bgWn8n_YLNC8Vp5FLuhMHlOJO5TCmK1d3y93xaU1wORhpUJoOSNGgCN7SnwvqBIJa99KTkqYQsLIaQZe1leDOEV9jGwU1_tCEGFZDmlCFbkGOvQFe6AfMrbCEcrmIx7DYeLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl3O7JO_Wiv-TS_iVo8CuCOUC3mVzHU8mWDNq9-p-10SDmXyb-wEWq74H2Cy_9Mwl4AF895ILIHnawfW5O9ieTHe23Pwgzso_0uriIRNjhFhDqMxobEI36QqfvaZRExr5rlRxiz_zMI8vNQqeaXypyfT_o0M7Pk_Vxe98wFqSeIRObKrDBbZD-p_-SeTye6pxFuh2SD1c_WbaD-pBCIEM03g0I57ELmPPN6CXabOJukwpzkerUP_Ozcs_aOxJ7TWFGYCiNZh0XLQ-bAmEkGFdmHLP0uFs7Wh2X-imYsycf0vSSa0oD5l0WhbY2Jmjo5RNHtNn0wouEw6oGcYJTxCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkFlN_9x6HXGLS8Vm9qQE0PykMtN26G3o6bxBH-gno4bvuinhFrVfmvjZe_owXKXKrseiNIYlQ8QhZ-r_zrx5NQBd2l0pZcx6CcB9sQXbsyeQ3cMzjXzqSabqXGbTbl2jj6kY4udU8c9sN57lvicUxdDAcqt7DeT6dTX70HIyXJ0y-89ehoN29VEJ6o3ic8ekB__JIDsLiTYeFC1P3ioq7lv4n6gCqRMw9SVW86HBv-2PMVWW_Gn3sDDv3sCzIKGlkA4XgqUhatOvnPxY-ldoxi27r7N-Uqdz8zXsm4cWN17fynnQgxH7gqxQiDndTFlGmLo9iXjKjPc6PQVkoTohA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671465" target="_blank">📅 20:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عون: تلاش برای توقف جنگ علیه لبنان و عقب‌نشینی نیروهای اسرائیلی ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671464" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یکی از مسئولان باشگاه پرسپولیس: اخبار مربوط به مذاکره با یاسر آسانی صحت ندارد و این بازیکن در فهرست نقل‌وانتقالاتی سرخ‌پوشان نیست
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671463" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW282-1Xc-iLjlW8IU-fpaJrDZLt2XSJ8MaGGz4iYs2ES_b4fZYny_LnEWwT7_cbY1ezCe1Tk2IaoFx7LNoTqC70xLAvFYuY7fsiMeNXC60XaDD1p1Dod1i62LBDkJhmUZj9snOcnXhYvTo7WQPKdgGTlJjMPMfZUCuBrNpdZxXvLhEJQDTdIHvDr9P6Kbw6fV5_gT2WMrU04SDlGbJGETU72Iyy7NtUGtaVW3fHilc0vE5bsEeR-iX6EfYUpvmGBXHR5UFptUiK7Ajh3l8gDr0PagjJEiJ8CMHLSOCNrXWnFiDN4wapBpy8ZbYnwe_8jLSbdYywRZGrJoShTSAvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه امروز قیمت‌ها رو دیدن...
تو شرایط خریدت رو هم ببین
💎
اجرت از ۳٪
🏦
خرید طلا با هر بودجه، از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671462" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: فعلا برنامه‌ای برای مذاکره نداریم و روی دفاع متمرکز هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671461" target="_blank">📅 20:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1_1693951181.pdf</div>
  <div class="tg-doc-extra">7.8 MB</div>
</div>
<a href="https://t.me/akhbarefori/671460" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب به نوجوان گفتن از نوجوان شنیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671460" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El-IIwbRX2GqEf5YnLWHnF5dXh0z4bqGPPK0rKNmvZWVQPTnjNkewWtATRdQNm_euGfXUTCpzO1hie3yLDfbWNvTte3nuPLjSEuN9g-k9BzQQz8loyjfrvntUePzhXCH2SJJ8NtcJi9cgPwAsfdqToBO5NZ28R8XmvDc4L0xoVVgI_ZncAcXiILN33QILTzyActB-ICA9Lf-gEgvy8oAi2iJFFqQyLR1kEhB-yJfzw2dmWUgMBn13tBj_W8sdpELZNx7QpDBA1wMPKUf1INv0_kZTXyqsOswo763zvhrVxNNCrr_ZAuqbihhWiMpcTiPHWsvSBUYrTwcEo9gxhIFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P422JLmDhyqKFMxGOdZ91lITVEE-Y4c78bTz_AJcZEy__kOud1xUe11jLUT_nAoYt7kxQxnAIKb6caPBvUswGfOBmqDz1JeIsoEUZ_a3ReZ1Fp5vKNeytl_7Ls7nfxJkxEWrFOt_asqg2-PzT4Ws6mdDHHGCIJdudV6S3Hb68Eb1GOwrGIbyQPLT0boQLnWgwHbzgGgYseXdBcUZRbYbg-As78pitpbM2vguGFkoS11sMhhSrIpCUSW6WW0cLI2m-glmkVatztZ2UUX4QjWIFRKesKudNAJ_zN8h2FfXVRFPVnqSYOdgd9SFjlcEBrqBjLVolJCaeEbeAghC-trfvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر نوجوانت به جرفت گوش نمی‌ده، این کتاب رو بخون!
🔹
«به نوجوانان گفتن، از نوجوانان شنیدن » اثر آدل فابر، حاصل سال‌ها تجربه کارگاه‌های آموزشی است؛ کتابی کاربردی که با زبانی ساده به دغدغه‌های نوجوانی، احساسات، انضباط، گفت‌وگو، مواد مخدر و... می‌پردازد و راهکارهایی عملی برای حل چالش‌های والدین و مربیان ارائه می‌کند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671458" target="_blank">📅 20:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtvwuK2U5YJGaoXfNp1k0KrnJfATLBn-L2jTj0qFNe08VTUzyIR9H_k0fT_VyhJlms-a6Kek5hc8YNs5eV0oWvtsTauLJtSf5RTZvLVe_r0H9fL0rEBolyNbDlPuTJO_SeL7GlIK-3T2nFuAo4rAmuLPWqOFAFLLm9Cb5pqB-kRhFyQuNHClqkJFB-73q4HFoLGhoRyQdJVLwZz4OJp4JpuJKjTT7AnrlGp05yVgvwhylSciSSgSbIB8S_GKCMuhaTZc5ZguRmLhIpFgaZ_NEOckqazeJEbwifwTGpjPismiWz_AjbQRX0hLK9FWji2AQ1yFWq1tVg88twREhVYnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلاهای بورس کجاست؟
🔹
در ماه‌های اخیر طلافروشی‌های آنلاین با این نقد مواجه شده‌اند که به اندازه‌ای که طلا معامله می‌کنند، ذخیره طلای فیزیکی ندارند.
🔹
حالا یک فعال حوزه طلا این سوال را مطرح کرده است که مگر صندوق‌های طلا در بورس، به اندازه معاملات خود طلای فیزیکی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/671457" target="_blank">📅 20:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWvb0kdtJJ9vfMTrNwGRfHBpr2Fyu78VajPJqUTDUVceCURTjrPBOrEeF-8SH0noCKMuXgKbG4sxyFl_EsYkGFeMD7w3YW44npcSCDGydI5m7esUWdUAdnqSbjMdAc0rnDJ-NyZf8FZg4HKYGdLrYL9UgZnk9kJl4L7zVi0V7EqtMFFVE-A8UCnmgZ4VacDUYXzkWqZJZ7_yqy44-kfDmZkqsK74ostPJO4eDNXbzJzlVD14WlPTc-xvi_OQxJHeHogyDEch_9aRUUA7lvIXCVw1vTS7pgxg2HImPdSYtz433asiNijmu2yv59xn4OLfRQiwHtXAGhczMF76qWU1fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/671456" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حملات فسفری صهیونیست‌ها به جنوب لبنان
شبکه المیادین:
🔹
توپخانه ارتش رژیم صهیونیستی منطقه واقع در بین دو شهرک برعشیت‌ و بیت‌یاحون را با گلوله‌های فسفری مورد حمله قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671455" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست دوم   ایران ۰ اوکراین ۲
🇮🇷
۲۲|۲۱
🇺🇦
۲۵|۲۵ #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671454" target="_blank">📅 19:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671453" target="_blank">📅 19:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/671452" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxBP8byHvY7gumD2CgdnFqwbWNged4j0jRfvPG8qD82oh_Sjsp7MtC6V2nhAbH88HeHZhlx54qLrbVIAG_2mYNVMI-AcZX4zdRinNb2drYWycn91kX-jGNci5SUVfraEHRBwaOPAZfMcKfcSsGndCZG1FMSI2vC7lu3qV8IWj9rRw40sDsvPeqtPzn-z88qWk6Fe-jnl5D_c7VR8irreEDB89azmB0dLYkOtBm_LxSU_gFyS388vig371PXFjAn9tqw6asWw7baZaMVrOc4RFEO4lE7Ga6bjgzxb39s9iNsCIXlIozaRLZ2haB7ti7fsO_34STnwQm3Ba8fWiIkopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر عضوی از ملت؛ یک پرونده انتقام!
🔹
این اطمینان را به همگان میدهم که ما از انتقام خون شهدای شما صرف‌نظر نخواهیم کرد.
🔹
انتقامی که در نظر داریم، فقط مربوط به شهادت رهبر عظیم‌الشّأن انقلاب نیست؛ بلکه هر عضوی از ملّت که توسّط دشمن شهید میشود، خود موضوع مستقلّی برای پرونده‌ی انتقام است... و بخصوص نسبت به خون اطفال و کودکانمان حسّاسیّت‌ بیشتری خواهیم داشت.
رهبر انقلاب
۲۱ اسفند ۱۴۰۴
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671451" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/671450" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVN5Lah88ZxRQ0Ujv0kzf09wjxF1S1XYbAt5dguZ_JjQRBVjaSqxsnRZKbvx9z5X3-6jrV8VdCSqPdiYvtRPCrgl7aD-ZuDMDDkW2RfY0Ox6_prtjDSdlD5RBqPLNnC7e9wYstGiDZhmZxPuYGAVH1edOIjZgqfTqbRTnBuMULjDUHyGFQmmrPh-OKgAxWdm_OiO9l2ccAOtc8Zccb66SgDdDD_wsBF_pEK2JvAikJ24PDAWt09Rh4vrYT1rCMQIjhWlm6rI84PJTMc-UatFnC_fnRcTvU69Lh_2G0Wslqotiq-5w7VfAV3xFc1WFR29bYDnZpdPIm9AUcXT00yU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور
🔹
روابط عمومی ارتش اسامی شهدا در حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور را به شرح زیر اعلام کرد: ۱_رضا شفیعی ۲_فرهادعلوی ۳_ابوالفضل ملایی ۴_حسین جعفری ۵_علیرضا قاسمی ۶_حسام‌الدین…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/671449" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671448" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671447" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxj3rNycE49l0K7zO-AwFuIpJw7bw3VD71lBNn2ziGXUBJ4_reiByICVff03UudT5YRtwYJfGsegvc4XYIjh-iirCMxzO6JDQJ9xgwolmQb3Zz9m3HfXKCCoU6U3lqULm5B0JvyFUkgYW0a_6fpfST4zE3Vn8OlSO9x1HU6Ec6bKFzmezlSzv8hPL75dfBWur3HER7PUbsf4_cCPUmhhv_oSKpKzof8_sbE6J33CZU9LMa4XaaPub4vruW9iRcE-nslg25rBZpVz7FtkE_3DM0-eNur312xfX6PTJeSLhZh_z4C6SfakZ7Gapn2WvjsGCDSQxfUiJbtC66RKsDV72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه اقدامات رژیم صهیونسیتی را در فلسطین اشغالی محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/671446" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول  ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |  #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671445" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرویس عجیب والیبالیست جوان تیم ملی در دیدار با اوکراین
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/671444" target="_blank">📅 19:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7d-CX2PV341PU77rUw3lUpPu2bugXUb7cs0S7Ewg6wmeugC6MKumTbJ_gPJwbl1YkQTZ0j31tlXSepgiDSyQgbuf5RWNBHGgw6YuK8Ec4nA8KiB6yMZb3cFwYpffvY-cesz7kc3Sk304xjV4lGn2PZ5j2dDfx-JR8ga8RgQ2RyPzMhxDbGulF4poY94O72eAlBe-Mtscm0Y7DMqWPeP0nqGlWSlvo9EjBi1HkWc3JJfkd3L9uKBXMUZRtXpa2wUT7U5jVV5P_azWsS9OLByyPuWJtSzOxfx1QdI7rokeOxenuert7VyJyXnpbvMLx9GFK5FZiebQ3MK73hb95_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/671443" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تصاویر دیگری از لحظه حمله وحشیانه مزدوران سعودی به فرودگاه بین‌المللی صنعا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/671442" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آمریکا با ادعای اشاعه هسته‌ای و تروریسم، تحریم‌های جدیدی علیه ایران و روسیه اعمال کرد
🔹
وزارت خزانه‌داری آمریکا در دور تازه‌ای از اقدامات محدودکننده، شماری از اشخاص و نهادها در ایران و روسیه را به بهانه مقابله با تروریسم و فعالیت‌های هسته‌ای هدف تحریم قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671441" target="_blank">📅 18:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اصابت پرتابه به جزیره هنگام؛ استانداری هرمزگان در حال ارزیابی است
🔹
دقایقی پیش نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌ای منتسب به نیروهای آمریکایی قرار گرفت؛ استانداری هرمزگان اعلام کرد گزارش تکمیلی پس از ارزیابی‌های اولیه منتشر خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/671440" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_y5vU-XTSMntD_rUFULBz6u3HskJ1LY7fHPsHtphePB5a3Y_UL5P4fB4nwAQwF_KcjtDUZp_T3Im9bq9HxTL2WuLSfeSPvWHWvaXhJIgMR-b_dHKiF5HHfKGtioht2sRJPWRl2slDh7qW2fYcgEvIzInkf7YcOkrRQBuZ_nYJYSuAlJFNkgInDFRLWcHQS72qunW4s5pEfr-ppvMJGXWmOdAysa0Uz5g1t4yjcO1t7tjczPhsLYtpwQoXRCaCnIMEPHhP8xsr4Ec6dzhd_IOR1GYn1ykUU7UT48ybboCiaeSfRVVOnWhhsGyAIvAr1szh01LD6KjNCDI6n3c5XEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد کشتی‌ها در تنگه هرمز ۹۰ درصد کاهش یافت
🔸
در ۲۴ ساعت گذشته، تنها ۱۱ شناور تجاری شامل ۸ نفتکش و ۳ کشتی باری از تنگه هرمز عبور کرده‌اند.
🔸
تعداد شناورهای عبوری نسبت به اوج بازگشت ترددها در ۴ تیر (۵۷ فروند) کاهش چشمگیری داشته است.
🔸
تردد کشتی‌ها اکنون به حدود ۱۰ درصد میانگین تردد در ماه‌های دی و بهمن سال گذشته رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/671439" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Wb7jjbKvZgk_TRuSTxUPrI6W4rFL-Re7h9sdW2eQEGx6kugRMEJYC24y-kc-OtSWbbQZqaLtLqEkmrboz3Ogyiz92cBK0OoW5Ly04Ld5N4YZOAc3LxeQNJ3vbgx55pYGmncectCrrbafehYL8Wxw0z9WP7bsqpfpBhM7N40y96xflFwV4b7lNXTfHA0RPMRCGUv6_pOVPBgtMyz9soaQi5TWFzf5fWgVTUZQslDJNC-dQyfUGH1Q2qb8SCOPd467JKXM-pql7VbV27tDCE4_4WNhNzWvvlAd5Z8nFqFaYpzg2ccX487_deRplex3YXa70NumhdITYkp9tGgAOXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: نقض تعهدات و تعرض به خاک ایران بی‌پاسخ نمی‌ماند
🔹
سخنگوی وزارت خارجه با تأکید بر اصل «تعهد در برابر تعهد» و حق ایران برای توقف تعهدات در صورت نقض طرف مقابل، هشدار داد هرگونه تعرض به خاک کشور، فارغ از موقعیت جغرافیایی، با پاسخ قاطع نیروهای مسلح مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/671438" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول
ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/671437" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
جلیلی: خون‌خواهی امروز ملت ایران یک مطالبه جهانی است
🔹
خون‌خواهی‌ که امروز ملت ایران آن را فریاد می‌زند، صرفاً یک مطالبه ملی نیست، بلکه مسئله‌ای جهانی است.
🔹
این مطالبه، دفاع از حق همه ملت‌ها در برابر کسانی است که به خود اجازه می‌دهند با نهایت گستاخی، حاکمیت ملت‌ها و عزیزان آن‌ها را هدف قرار دهند و به آن‌ها جسارت کنند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/671436" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از طوفان آخرالزمانی در نزدیکی سان آنتونیو، تگزاس
🇺🇸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/671435" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Di05xbGqTG8Wfj4mioVaC-oslvaLG2crpmXeHkJf-yAZFu9Z5IA08dHJWJwp3erdek7BuhAoBPbhX0PyCbBdiQLZ05N3Osn4SjA1khQYGlYjwBhBEWFuXX7eWvtM4dYGffhVFFlmoAbTOldM4m3Kg-mcCl-XG9tHKCUodgPGZ01KhGD-YIvcsm4P5A4o7mrEsVL-Xdxb-GXTAe5ZlgkQp20VZ4yiyeGT2Omu7zI7pMGYAXNgUR_11X7NadOAQT75weqEndW9vLr7EwvDn24UXR6VtNJMIo77ExImHXJX0gTA7DXq_Ozj_UE0-HrjkdU6EYmlgCALpBdGBOE1wnz9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlwSOBf5E781CX21LOwrgCC7pF68kGL1lKTqgPluX1JI1mrj5eQcnOl4J3Plf5AjkhxTVwQzIWCYwKZTvB0YGHY40lqLShrDvmDsgThNGc9WF1VFQLnu6-WQkstBuSRhjcddmhGNsQ5s2uJgk4d4tJeFiEluXndBdcadNldi1MJtoCZpGv1ZrmmL_YEM4Fdf96efNhpXk8pjwWJbJxTzDRqtywmDc0vT9MKtLl7_pEOCwzhRCCFLvq6i4kU7cjOQLnSJw7KErY8apEMy4PfsdeD54s19Sks9hZW_AG_A7jMZeo-mYzRTZQQUiRe2KJhstEQ6go-fXNVgow4whXPKCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ایران، وطنم ، جنوب
🔹
استوری رامین رضاییان درباره اتفاقات روز های اخیر در جنوب.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671433" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkF3sx9Ewah4t7xyyQ2gjm9ezjAu2t6xaNjgih2W3lSKZgd3Pg5nPEn96JYuft2yqgv2LWv0P8rqaWmy0tppET9OtzFH_2Cvod8RDoxA1KPgwHG4o2sZUHnmOHWnVlHOUTrg-BzWwyahlzN1t8MKPRVHeqAZLtHE5J7r7RSs4jdyYUSVjdvKRKJCc0-MQQRpOIhL-n5Mlgq4iv-YjdEAq2Ll0LIyNirvZbhL2HPu11JcGFtiBb5tZJCI6XjrmwNuRuUpYLOnpS1TPPmHB4ek2bSXP9ewK6WpoT-VU8E6bNPfU9iZWkH-hl93X_OLAvpP4LsYuwuUbaJzjm7XL4XJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه‌طور یه انتخاب کوچیک می‌تونه به کاهش مصرف برق و کمتر شدن قطعی‌ها کمک کنه؟
🔹
انتخاب لامپ LED با کاهش ۸۸٪ مصرف برق می‌تواند سهم شما برای همکاری با هموطنانمان در کاهش مصرف برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/671432" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUNWEwm_jO0DVWXxzhnMJlnpdljg3MDc8AtNnGE-WrvrWJ739RcVQsqjhQq015oOnRd5s52z5douA3qAFWuFG4x069Qhp5i3oBj4xLf7natbx_hxn7TykgEdlPJScoXIu7hZo-2nbbkgUtV00udcmw1d_ZP1bGp1Ljw6S3QnEVWBo9Qj-3c0e0ZxpNhdV0u9P7bVuia8pM9657i0Rf51RYqYvj-fN61mi17pXQ6ip7IRK3nxYXhBCHwAS2aCmIMNdOq0OsL0L9uEUjgLp6wFo-BUpdpWpmWOSBQq_0FRAZY8fQiROPiEA1k_TMA1PWEEM1SNbX49pF6yKj3HR0eoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران درودی؛ بانوی نقاشی ایران
🔹
ایران درودی، بانوی نور و رنگ، نقاشی بود که از دل رنج، زیبایی می‌آفرید. بوم‌هایش میان رؤیا، کویر، آسمان و امید سفر می‌کنند. او با تلفیق شکوه ایرانی و نگاه مدرن، جهانی شخصی ساخت؛ جهانی درخشان، شاعرانه و رازآلود که هنوز مخاطب…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/671431" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوسی که هیچ سلاح آمریکایی قادر به حل آن نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671430" target="_blank">📅 18:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال‌تایمز: ذخایر بازار نفت در حال اتمام است.
🔹
ادعای تازه ترامپ: روسیه آماده است به‌زودی توافقی با اوکراین انجام دهد.
🔹
یمن اقدام انگلیس علیه سپاه پاسداران را و گذاشتنش در لیست گروه‌های تروریستی محکوم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/671429" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله توپخانه‌ای ارتش اسرائیل به شهرک عیتا الجبل در جنوب لبنان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671428" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: خوب خواهد بود اگر اسرائیل از بخش‌هایی از لبنان و جنوب سوریه خارج شود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/671426" target="_blank">📅 17:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر همسر شهیده رهبرانقلاب: اینکه ملت و رهبری خواهان انتقام باشند منافاتی با مذاکره ندارد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671425" target="_blank">📅 17:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOAZgS2DZTAEMVw4UNYaQLHs8NnHgQmrgSM0qfFWNUmyH7oPEm_zOmqAQjiX5XgvZnL4TYaZ-OXHA8Nq9o9eepzje-d3HH5O87BIFihx56tSeu8r2d0jxiCEkvspM2Y5ZnCXV3hV_0iaHtPaGF5JAEk_qqWalbm92vEl6Ch5lkvAp9UtrTO4Qa3ECpzABLYqIFTv9Q0cqwZG5D7BsAq0UAQa6Sq1DCADTio7AE54FbyTji3rqPhX1DdLo3vERi4cmZFzFqr0GyF9woDHnSR5xst6tBTCaEPuZFLTpBMIC4klUrc6CSzjDlOa22JoHxb9du4uI2xQBd-9ikP-8cYjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvuPRoscqm-XKgGvyywq3m0gd-DgsVmR0FVax7BjJqLYc7EsArthyqDQHSGpXUB1Fix0CwxkNjT82RG3eCoqDg2dpb2iizqdrcA6bf_Z5K4K9_l5XfrYcoA_J0VMA8fHr3jntUyNUVieL3j9mHhejXJUtOYf6-cTxsqVdmuwTlPEbNoisnCVgxnHDTN0yJWkL_5whOkkArsowPwNVz6yoTz4mVzJPtFYVTfKuoVFaK_H4Dpovb5khwkwZ8Oqi0oHMZIX8kVDM9Zbd5vO5qU8bFPTuX8ykFk-yYr2uTM2tUAPQ5s-VMQOfH-7bcHM4fnttHwR7P1Fpxs-8I9qiszchg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران در رتبه ۸۶ جهان از نظر چاقی مفرط قرار دارد
🔹
مصر، آمریکا و عربستان از جمله کشورهایی هستند که بالاترین نرخ چاقی مفرط (BMI بالای ۳۰) را دارند و ایران با ۲۵.۱ درصد، در رتبه ۸۶ جهان قرار گرفته است.
🔹
در ایران، ۳۲ درصد زنان، ۱۶.۳ درصد مردان و ۱۲.۴ درصد کودکان به چاقی مفرط مبتلا هستند؛ موضوعی که نشان می‌دهد زنان بیش از دو برابر مردان درگیر این مشکل‌اند.
🔹
تغذیه متعادل، فعالیت بدنی منظم و اصلاح سبک زندگی، مؤثرترین راه برای پیشگیری از چاقی و کاهش خطر بیماری‌هایی مانند دیابت، فشار خون و بیماری‌های قلبی است.
@amarfact</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671423" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hC7zQzfxVL1trCq58hRwncO02v9g821th-v6g8iqIb4r4v2YSIA9xgERSiSyI5w43dw3XSEqSXySJb7fZIQP1H6xPPJ2w4YvTBTh_fwGAiNepnUzQz7IJChYKxCHoqjWUFdo9vzu3FBtHxynLAE4KPoMHmRnQkRhdJ0hBHd4KwxrdNSRtE7s0KzD-wmhBM9i6tDvviS9FdowsYnVLjx5CadE6smWFAKNxxWiSaHeB8JUYtkaLXQQBEzViD3OVlBLy_MvcMHd-01yGbCGIXt_8vmv2EWjfrsLoF9PU2JT0BQQpFgvPKyAXlrYQbtgagI_yC96W8fiFx-fvVzNQmd0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u502A8Z88HgGFqJ-Wnb99jc0glJ305tVF6D0FJ3uEulmQdRuMu2JoBxorvY8k4LAEnQFu25xGfrFq1tyXKZD4JxzshxkIWxiBzaYe-k_osrKOTos9h2f--NdM8VknD3hgliQ58Q-OFcbTkv0awSaaJP7KiFo4UdGm7pirsbIfvhm3CWhtelONMcVqhWAt1jEYauIEFoiENwj4ipU1YXHNoloWCmhsRITUErgWlxwZcKpV3Mzjmo1Rd-3Go3lRSD4sIVh0UM4K5qQwwYhHCLCQrlSsMSaXg6AlDKTK76PZErs5mTBBw_n4ZyhUbH9pk_oBwNgAr1wyhi-mIoufLFaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKhynGwLEuBieDUW0dgBX2Tf5dyyK_5dMiF2P63kUiatxHcfi-iUlE3abQRLsuYl65s9p1RdsW3qUp0NxcQ0yso1r8q82NpwOiPvLWAWGpiB-MI7pgzqicy9Cog24lWfM2OvflBNWQdtwYQkkas727HAd57LI_QCB_7t2aPdqpp0eRvR7__1GB4NrzdAB1aCz10qkoI-Wda4RrXVwevK0XwRv5c1NHT75tzsZf_SSCQh7h6rhOXe5ACSkSQAQB4IS3npbyuG5-PjRATIqaDxZdAwn4_kFYMVenJzTmuwwl6dquw2Bn5Nbi6nV9xk1OXciUCUb3Om-kHc4TaT4riAcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویری از پذیرایی یک سرآشپز ایرانی از بازیکنان تیم ملی اسپانیا در جام‌جهانی موجی از واکنش‌ها را در پی داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/671419" target="_blank">📅 17:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فوری|نشست علنی مجلس شامگاه دوشنبه ۲۲ تیر ماه با حضور ۲۵۹ نفر از نمایندگان در بهارستان برگزار شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/671417" target="_blank">📅 17:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlEf-ilwJWH35cGvObChzJDwyQ8I49ov2g7iARMedDehZA4R6P-hmyitkJmZkNTTC4aZhJGNeFly5RajeZOSRggcB_j2JCV0-Y8FPTcwlafmFlu_-1np6iIpHXnLH3-qbW5r8NnTiMv9JOcAfsM7KbtZjzDJW5KF0wWsaacz_gJxtuto1ezu8yyfhFtmcUd-dMmUsmbriEVuLjt0Th7rEEykrxBo3ryN_OAMFKVrR9q4Yo9mitAC5LPSVE0hPi9jRjwn5lZJYLEHllOro36OuJUOnNisxAzft4fTWw0FPbQrNWl58W0bgm1W9c4GxaGdblVSB1oO4bu-8bpL2n2mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/671416" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تداوم حملات یمن به فرودگاه ابها عربستان تا خروج کامل از چرخه عملیاتی  منابع آگاه در صنعا به روزنامه الاخبار لبنان:
🔹
حملات به فرودگاه ابها با استفاده از سامانه‌های موشکی جدید و با شدت بیشتر، تا خروج کامل این فرودگاه از چرخه عملیاتی ادامه می‌یابد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/671415" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
