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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 424K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 15:15:01</div>
<hr>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r36ArEaf3Zpc146X1fLUU4B3KHNusHJMhKQ1XRbA1nKtuotBrZ_fdSrThuvypQt3ooY8HRPaB_5ZK921FgCmgImRnl1dUKJ2luKGdDOVSLJzzDLTOIn1WejFIS4k1zS4l9mZyHHMPb30r1KHLEeU_4cSzfPUL17eEBsRSNxgbAtX8zrwz5eSrYrSLy9nMxZTzbiQ33jER1Oh3V8gQttJr1UAXbWQ3Nt2d1u8fnkYHn_T7GFMcL0V3MMKxgWZZQcugz_8hfXd59HBw8wKzIT4tjHgy9YZk0uhVGpCF7tnAGRFCYM1Kv5YyHwvm3Cz2M_1li7DbBtOWfOuInDVO2BGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7Dxxhyz05k8N4zA4SkQdQneKJChbUHumD1G6BOmFXRK2JNVhOEq3IkmKqaMNHCPtrZQ5agdfMFdpJN0MBghOu-mnzsJJ2nOcjSW9vqNnZUtgrlFWklG-FAPR1j7XAWirIP6xNoVhUN3vkirngv0cb7w5pN_5CEpeKZ4ftxXbJ5VHmPoZp6JelQXmM0BDYLQ43rdsKx8TwISZ__gsnJWgMtlKkhA-5tguAOS2bpW4lTNwAqqKy56GRhO_kEm-hn45V9_7nb5r5a_U4FIP7mtG3W1VoOP0rQlV0PTs4CGsLJSu1DQQVJRn-WJuDxpJLLveb1sQ33x-8dTwlnZvOfqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGgLmFVYaKR8l9xSjnkyFNarXnXsTmZTzQY8Vz6276LMEVWChtRqjKoGjwIAafEoFnfmvVkmKx_l6KOL_rPpeoNsIzL1wvNM68hOzNAkk1Cck6wlyOp-KPlEazkW-AD5fGU9QvfnKEv2ow_egEw9MaQmiuw-rSNOhboSDiorFzLVERuWygMM9QAz7pG-buKbt8wX4EdjCSaFo1JdpPlKLk45gywEnZEQze1kmy4j8sTzzn8liY49U-FP8qrg9cx50Gy1PSQgygJqAOZ4JlhckPHQzkrHK0iUEPYR9G8cQFWdc_GsiTSx_hHLw5fNwfP8xps_kvU3bQFPesIiI-J0og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEGG2VQs7mKAiluUnoFhNa5-NLscgLHLoL6AuOKsz7kBVVycV26Vub2aN85Td0RYM9GqPNFjcP2QeDBb0Cgzn9BkYGMgAMGojWpqJOj6JBRRKTWty5Fizhmq6QgTXTGynf7LmtfAPjygVjpY5EyTBpe5PFceXXCSZzbtz4SvFBs19j9beqcxiKm1K2Gmzga7rLlIcsMSuf3PstpUPBlfgowAMg5C7PzuPadelhEZBBz_vKzKpPTCeJVKQzp0WqWcsaWcPnK4H-URnmHpzSg1Ivd5nMR0tembkT4_HBKKnXQec7HaY5xyy2iCSIqJJL6Na3Lc02U5SeJ5e14k6muNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJe5WjnWK2BClSb6LCaZFtXzgr0x6fRaaB-2LZkU_xhwqExkkZbU6E5oEtqph4U0kbb7NkOXV5-HtDAP8Op7TKPDz7jqWMbmhnvcAxYC1vggvC7sdNBvDmCQCw3GCXNSfMDvul4HW96jkFFeaSCnNJ3xpYbcCcAGhjFj4jyAv3ktvpJW48z8oAtbWihVdzdOHkKf40AOI-26NkzqfZx0Dj6-8gdSTGQHJJTukQgfV-xyupCKybAm6Dm9a8njfzcj3IM6kZ6mpI2xpBKzH6eJVu50SP7Ct8yQigU70kSHV9YZu11VVAUEyob7nobWeVYFCciBzNmfgRYQvRunirM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf__u0qFYpuD_1-6Ohm_m9fujtjTc02TtbHq3RglO1sqyULvDgv0XIwzgZWviBKcsaQ5oa5ze6bKxJ_8J4JaMzCWHNanXblPTvkv60y2anLUkjXizwGLl_dcawKGWcZUcuAgSPAfdcMWRBra3UvgPDxKETWfa4J5wY5vQHjQAq7rkYrgvHAR9mkAnraaghKXoD_0IwG33OdEPHR-H_IX_xXGlMhQw-qkxje0JyfdelhgxTNjWY7X0zBZgqg4BbxMcXSxn5wdYKJrbREv2Be5c1QiS9HOPN9YCy47tPuyBlLUQv9r9XBj9zxuzpDU1Gf_U9e_X-GdzeK-znRxNDvp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1qFi5NPtQNL8jN0ao0sqmK7yugCS0ZaBZZAGTgAZKbW6hppXJtvLfEkEEERPdku2GYdO3-k1mVx1PXHR63VzUco1hAwVksuIW_PyNbt5sGVXUUOg_NnlLMhkrxK6QOBC4KdZImznHvpCovOahdNBxwbcd-P8-9ISItDPsOZitcsVQzweDMeByu6GZRlQ1GyFl3Xav2uhpmSfuOoE519ZfVg87ALKUWQyyFQE7hni98UhKLTJmYrMS_n97bJZe4Ltce0uEXx_J6me5ZErNdw09NH0u_46AOWVkqCGUcXDXNzNYzj6gqpKY5iBoPJBseXmxjATAiOiR9y3EUbfEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0nmQuMvx2kQmfzdz8wSQM96i1eQzPYR7Ah29IYHupKq5vr4Ymf-07n5BT0qUyfJDhCc5u8beUttlFkDlK14fR1fwNtpbAL3936pCx1QkI7iY7Y5tmIRLhH-2V-CD_XLoqnGa8MpgkfRtZAQWT-a3URUDOD0L7WqEMDNMUs0QztjtpHNj5hxERN3U8jGYjmaOqmLvdcCDiHyE_KX58rL6QaCsruwXwobO6PMoWHOt9qgQwTDil_7nKBgHIc_lQoWjbkDkjRpgpdNHNhk5p2U_DtRzbO-5hNIzzgkWe43vywVlvF6vKvzVPbklQaONHxE1AG-a7FfCXUI3N-g17Gxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmNygX_HyyvuOcMk-vvEB5T4oL18hitAJvdDvZr9vs10Qv5nmNRTAIWGP_FNzu7ABpHlraU3Hdk-MqsC9ljHV5xA_B8dXQFx7kE0oiHL9oC0W6bvt_2OvVouSdZz78E6kaICB3L0I8PidsC6zQm5fr94-KKzqCnJv_87-PhIG40ssI8QhD4lQoSb4RI0n5tGjN-TFISxutQ7vTn7JtrWrnuZncr6bxlX4WGj1fPEmTL0G8nKjypo73xBiwMnEHXp3IcfY20SMKy6zOksg-b-TXRyDIpgHyJ0vlzIbbdO6zalOwmc98heYz0iKgXahDIYp4jDRJWzK7v7Utvwj8HUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLSkupeRUMs6AzCGUEpCniTZM6vXvnQ8KFbfWps7_cft6USFWIinsOjX-5fmSpEcOKi5meSZ-fozlRiSq3OnGpeIjLdxqrXNg9N0kjNZAtk5aBE7PvwxK20M03ZIsJ7Np1Ni99xzRod73-v5U2RllbHPx2aVlXfi0dCna6Ukw9IKz3l_dCoX96HAVPcMeZlo8mkMHkO3wsT16oaqMQCRN9ilw0OB2uryA7I61ngfFk1iuXLuaUJFXLxBZhJ3jV9LOeTI6BDXQohAJdvERSJZTlxT6KneHrSdNxjx6vYSdX-qMFQ1cjD4voZ3Gft4k-ty1MLI-qr7RzC4yJTckUw5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzj97lJr9HTGwHELc57kMbO83OAmc8aJAM4IVvJzPm0AL11k6lyt7wFL7mV7whh0fUyRiLRAlqMaAtHx-D27cRHX3FXa6iZp1zYql5I3BEcMWrkvj4uHGVrisDyueMikHtfMVGHTzm-Ndj8wyanXlXJSehlR1HZbQ8kustgnYcyLFlrLrPvhi_Foe9ey_aCl4-8ZXGHKF5nMdTb4qt9uNUUw41VFUYj30U1YKaKUNAz2OAkBXZJdhhdSiEGJ_4JmzqABBTkpFR8o_mGtjyN3-G5Tn74-0VYfhe9hjK7c4vvD4AxZZHUCwOvHOn5Zjq86dO4dUO-X8fh_Cuoz7a5MWcNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzj97lJr9HTGwHELc57kMbO83OAmc8aJAM4IVvJzPm0AL11k6lyt7wFL7mV7whh0fUyRiLRAlqMaAtHx-D27cRHX3FXa6iZp1zYql5I3BEcMWrkvj4uHGVrisDyueMikHtfMVGHTzm-Ndj8wyanXlXJSehlR1HZbQ8kustgnYcyLFlrLrPvhi_Foe9ey_aCl4-8ZXGHKF5nMdTb4qt9uNUUw41VFUYj30U1YKaKUNAz2OAkBXZJdhhdSiEGJ_4JmzqABBTkpFR8o_mGtjyN3-G5Tn74-0VYfhe9hjK7c4vvD4AxZZHUCwOvHOn5Zjq86dO4dUO-X8fh_Cuoz7a5MWcNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpEGHOSdjo_mTJOR_awXv5vngu31nR-nS1x1bpul5Q5I4KV9NHOfgH9R1E4yBxS3DYSnKGjbiviK3yqGNbogDbdh3a9vjPheTABm6NQB5aOCJW3Ar4N8mU1l3uFo_8HG9qwRE8QTDifdkIvOlv-P19X3ErfeSNDgTD-IwIlDNMYK97RgM6z1u90edGfMQvqQdi1nb4-BXhlwyUFziUHMlW0PsOWPPh46M7O10oqdL7O8FBtR2iObyRaKhEYuxZvao799OMWpcsDE5F2KQk8b1MrfPMkOR_9kf5SP8cWDOldsqhwZWv7fdbjrnnFXCWdVxhNc3rFt54yRbvuTCNZ9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6wfVNXPsUu8TyKuWbeBXfF7PGamn07sIvjKXVBZ_dOvIpyW2d4aevsWxf7M8whoIXvTNqhnNoai9v_VcpRR215qXdXr7D4yEqGascc8PVY9m2mIksLrRqqaEebxD3_AydrrC8Ul5W5cOvRASvnm157nVHaNAl1rZNsDWp-9MTdJdF7yp70N_fDuoB8n3lc7NmxuHnDImGaFI_myqYlcKHrUQvsOvoM1D6WbvcKWAkoWAr7fBOCxP3Gh3e6T9983ecg7LM4oEmQkOMS0LceGXZkLrIzti9q5etKL9pKM-NvLiwXHPZ_sQ_ON4Z8aKWbV7XyORMCdIoy0JoDgle4gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=RVNvO4gzAytMLNafsEb273cJcjVLfHJaS3QpZj-ljaeZJTo_pOhvfpcRPKchwPBwOFXZy0YsZiBVtaVjGANJCPnK9axP54lSlH3cS_hJfWssuZcqs9hDiTtDKgHuRx7Z5CPVXUB3YsbKVvjzHlojTGNDavQcJECP-sWFYmz60akvpZKnPpWnBE-FPrmKttOhL2P8D8qSTnXuw_QzgDuL0AF3J4BfJLRGBgyKt-hoYPtb4R36ebyzob5ukgJil4RjVcL5BpPTwFHR5UBxr-kHttMxHPKkF8MhaxKEZhi5FJC46GXB2Rr8g-TLXksftXAlGws53KRWAXvcH6LoTFdyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=RVNvO4gzAytMLNafsEb273cJcjVLfHJaS3QpZj-ljaeZJTo_pOhvfpcRPKchwPBwOFXZy0YsZiBVtaVjGANJCPnK9axP54lSlH3cS_hJfWssuZcqs9hDiTtDKgHuRx7Z5CPVXUB3YsbKVvjzHlojTGNDavQcJECP-sWFYmz60akvpZKnPpWnBE-FPrmKttOhL2P8D8qSTnXuw_QzgDuL0AF3J4BfJLRGBgyKt-hoYPtb4R36ebyzob5ukgJil4RjVcL5BpPTwFHR5UBxr-kHttMxHPKkF8MhaxKEZhi5FJC46GXB2Rr8g-TLXksftXAlGws53KRWAXvcH6LoTFdyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiMPOzTfymkxhsqm6Z94bQmlsAffhLdLgJ6QwKShAbheF9xqD9Sp-JsafB69me6foS5Xb1P5iuywXGIhAm7FxtJ3bfwLwEvaJNMcby_E_5WAGi6ThMIhjNSBCANrXEudATeA8qut2fnjKgglva0syi3fdETwXRIzDVAx0iMGtK22h2tfQuTbYyBvDp4UhYopjZ67fd6ZOAuo7qaOLF1xt5ZwjDo88rtrqxCI8OxO-2EC1DlJxKjZYO3FkNJaJxdvEO2b1Ys-whec47_sEm7ktPnFrJwb-k2815wbhal6feYFPkAZxztLrfvENZSkii7fwL81o22eDuKz26jKhWiO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08az2MUJsIz5uBlB9Wj2As7wYWC9OcP-06L7S9e3mO_QEPs-cIcrcWWfC4kGWLX8URbzvbGOBjczy8PeD_GTBl2AxG0BFHuop0_7gyR3qibVP7q0BB6u9nGh3jYFZ9v18_ZqwAnYnjXdhoFCDyQjddWIdUB6gx_Z50duobQo6eyyGD0jpb9eZ2hmm7hPHsgef5sLu6ZOuw3FdUqj7JAcD5gJNwz45nhPUxvFW1gBick5nNgT8h_SilJz8Bm7THml-drobqJKosj6EpHjIyvplHC8UC_T1v0STtgF0L7N9yAIuEsS_TU6XE9j0FD6NEAs6MFhWOB7uaLO_nO-qposw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvARRLiA-7oBSC_8tRNGkzqh4dChfqL4hMwaHTpg4L9GhaPQjmCyG14WsAcW3BXFqdsxceBuXJIiLCF_ClDXFCKbkQFLgJl_5QbKaYCY5gTt0pJ4GPRYYARyONNv6jym223_QVwVm6VbSfpp44m2QEYPweozlThxCI0R2qY80F7M5A8sCYl3RACrptXOqFeYrtLKXilK7Xmvu_xLfp3G9tz7fQr-XuZ7T5kGU8B2ypqJ45R0AeYUauoSmesBfZwFjKboPDTqR1uBn5TxWnfL_nuESJw4e9WTosMiCTcuN8r01KrN6yKDYV_pppNXA2Qo92e6FiQpNHYkxxRCMzY5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rutWJ-aS4A2ppOXmT1dr1AKLIvV9Q63AxkLDNdhuLxr4aGm-Ww_rytRW4GFw9dGm6cBpiZfXgXomxqaP5OsN1MlDePzgBpx0kRbdffm3n8XuthYUbjAekkxNqEIh0v6s8R41BjEHLUQbjxrhOdpQ5QS1Dujp3CPEqak-FUHDoaHVnzSFNu0CHIrL4zUO7Ak3jZ9WfQiC1N9ZtGsibvdQIbLOTZa01Wex4xS8IjOtlnCJqujAax0CvfZ-Ep5EQXA6galqN6pDtDn_DNMRtD_QCzaJ0K29FmwJvsJVzdjZAzTfBXAu4RzgOE7nXzUn6DqeuY4H4SFM29eooc31IFgrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm4CnRcR49AB06gTq4ZNpYLZYFzefnIKGuO6iQfRZ_LICE3Jul4wj0gYtyE4RfCHtOh2LJUCBTi1seSEoX3VDS9k7kEcE3SuoXNzp2CZp56lMkd_8t4wozFyyaz2do7LEQmxlQAfIutYxkI53xQFtRV74ocozZ-Sv3wtzLQufjixHxbtLa0_ZrzDFfYaXlruU4XSG18mI-420LnB0K2YxFhwULiT30vK5_g7VWu1g6zbR2CGBKXkTWKNKi6muJGRS9jFIdeqFZ6g7dSTvtvYgyG0ZAoLvOhQNNbmLedHz3GM4vePD0bWDMMsC__XhdlW6tRt3cPYcWMYkYyO9UVaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
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
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvW6LCyxYvvJAD_Wc0c-tMwN3XA7IIHoatTAap8o9N8a0d1CIhmt3G8SMWE2Kbl3jKy-s2nHMsUebSqSA29eeDDOvW_HxaHuFztg1vDiq7PlOnHNVOwSikmgb5ub92HkheXI5gk7qv0gOSQvaNeaciI0iugBisialqZAkqb5Z_ioiGkgK6kXcRH3i4j4Bdp75QwgMwcYBGbf5lklOsxF1RxkQ7mR_S9SbGrmi63UoCFdC-z-6O114gZBKw3F5k6VJBb7etd99kAvT7onzd0bNAbtGi9BHGtzYMO0WQ0yvK2WOSYJUy8Ek4ohe71yLRZc8qeJmLN-a2dsDnjkzmyvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWguu9UU-Ll0EyXY0O2akFAK1KJkVhjcKuKy_EwQd8yM95_jQzlt0jVXVfJqi2sVwB3GGTafhu0g1cw2dS2tYyM_VoYwKHFArgw44oauNhHE3jlhy8U4YqEU8T68bxK_xSfcD9RlvSMzt7Fg9DrxA283NXeRooI8VKGOukAXdCna-VuxZ3wC96--vDqyYIIwbiddRQ-d6K9Q3tykDqrVy5eacmbvodDyBFD6-8eFD6SBy4XK4duG2BTxstEvhMd10r0dKlUUE360m9SyCjEIFC0hCq3zcP-0gzdbzihG3YI0LKfG1o5UabzG-smgP3eLfxaF_mOxW3drRw4cfjV7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBuULCBCWqM9Cdpfv4HgQVlQCNN88PSeV9RJ5eFmZQdWR3ldNLRnLDMJfdOrR9WCe8hfYqP4tEoEPUiX8_7q7OTRye-w0VjAf9qzpME7LjEKHOf4Fbq_Av-ujkpMfEEripIkUGk-LedWGh43-bFcMUGaFM8lRMncBcI494-SK40kOAQ1CYX1kjiSlCL7Rd82bStx8DRlI2uGXmVZI-qofEHtkyEPtdT_qEogoixTbAzQpHR-iCNElqD1pROZZEQeXAzdifUNJvdNujbHx8JU38gjJxMwbksBdnumpJx-T4xp7NBXobMVxTBtJ70ajiseyicnOi4MW5cBwxvuJqpPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AApilATnLRxxB4UdomS7RZa4pgMOi0bqceBg8vVkVHtabsx-wfp1lz573PTCfdJUPoODkUANLlAFCf0ApU9FhmY7Bo298jbwchdwHyvYEjVoVAPNqRCy_fxXNl7nDOJSFzzDuEF8mMmbjKUGfrVIwLkhtDCI-zIrpYIjhmRQzwOjzvdpCu5He6CC0dO4IJLUStyoVMWCrndgxirGiCoO2AP-EEfxV2UswecY8EDqOGNhtgDFibcafDNz84tqXtiIgotthes3Agtdkagn9d8eC89eHNiT9VyAA3SmgNyX-Ec9tdkMi8O6p8uGZVDl--pUO7i8euvLUrjdrbt2tOrpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL4S0_FejAlcnBX4lG3FLwlZyYyCDvVNemBju8I1hFUwALYrc148zOpmlzSHAMQ1cIHt6HvO25YSDQClXvG3_LxWZNuunY3E5Qmh79aPEuimzVGSuQMfPJlblWOS6kF9QPwt0xb6ZfrAiVqYXeyMDfIAYctiL8KUZgyqMBK_1UyKtDb6fat2INqCQjBEyrM2uYi2ksY5gk5iiYelRtbVNtFd1PiUivvZlcCqDq5w5gMG_KjBEoE4QK5bumJXnGMbtuBRbM79XREu_oQDoZ0O039RhDYR48xEL-rBU6uGICJCOmOrtNFhROHmX6tKMnvW0Zf3kzZbss5XDlUGuEMvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtg3Kil6sQhDDbMsepauqQaQCzNtO2cczSsC6iyS-wYvpyFe3Fm63wEgH5j8mg-icjVcey0N_EKinUxdHlnHyKNITfF06Cd4MZB0RxzfK86e87TWfTfokbINu6MFQhD-uOgMJsGj-mTFRE7cCWJO348jsTkrEzSyTzc52hPYZdsifLOKx27nRIkVBJv1RkDSGVP0mDHQDiO6__hMHbmJpovhGaXhfZW2katHUmf4_o_4gOSQ-B47eA2cpgOsyJlob6LR2qlrCLgimD6T6yOfogvoT3PLgZtUFYen9_N5EqkutejX6S0XR6QpF_H4twF72xV2l24Md3ZzJNa9FBFVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKx7cqEOQtczTeqn43dSlrgWUuNyGXBzjFKEZFdzHUyA2UMzHz9T-1Q8oVj5PUtDu8lLvBmF--2t7SHXRroDei1lUZiofajMH-_CCZ8qcvlY-NLeoaEKz1_jKhMNq0SPAUB9wigPgTKdy2DghXJjkgWzKj9BSzCxfq59TqHmGlWtbrKl3z-oH_guP_vAYRJwaL5WrNK5yVeo-mwwqONrr5u7hBGpSIGlillCJxx5R0ApTglJMhuw2R2Se1qDNr59WL0shoxVZP7PVN7HhCFR8B9aM_s4PndkdDJzwV8N69eHAcS68cZDb4vM4SdOjaPX8yrWLt4dBfwpcq65T-h7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTk4D_0Z81XMHpmGa7FgFiNAn1CA1mhNwuQUcPOB1trHJV3F4jHoRsWAMBf8oU-Hu9i5rWJy18WOsDYi60CWdjnHNzEvyXUMWDWSn9fQsb44eV6FDmbIlO3e5v5yRqxZjxHyPmCM_WvDyd4H3h-ljZ6_KbfXCmqDf-9Ix1V3DOof4MSJWiE30MjV8IUTIahiP7932w3qU_HRIlqGFFs5_oBrDLdfKzbhdWklqMDJbNGWoce3L20e1zq3LkK12aXong4aTBGtfKP5wG_UL05bJDW9CvTW0_U28I7xjzSGWi_YL-AGrZrmjZgzyzjZNRPD4B2kD_tk2QP_O4_D8ijesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjYxpk1ml4XlgjHy-7eU4vneTBL9XHWpsq633avsIoPC-VR7SEH4v_L1WIkCXJL5zXaQTrheHAbgASUid4_DIz6bf6uKK0MSW5XPaJm5hqbx7ePMoS4TicH0oWddWAoOUen32zrkYuowlP-c_YTaCO6S0wv7Eknjhv6P2SAFLg3--BiYrlyitJKPpEPgsauy3JNnoQXhrsHP4Ai8S0xs5AH7veI5BcsKxFP2YScmDEtGJsivbfFxMaSjs9yrPR3yHxunvZUVTqZz0CcMYsXRPtTtYvBNFyTnh21qkRT65y8qjN5CGFbaxHsvJxUS4eBLBpKWmokXGs-Y7Aiw-KvUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrZco7pn-x421rrbnH0wQP1wcolIgr-aq4i7vSy4PUfI12FW5r3PyDNibLjf2OdsqvSDimGl_LyUgAOOCeozxjvW22AOR1c58QvTMLeA5wO5_Ly5Hl9pSN93-ZWvm3GryAMWaVq8fzavhUafsQXafo1F4VeU7GCl0cix_oIMMNOK8h7uerMRq9bZlg3RefRG5pVQdylSo4hiygVrUMiCs2WddMvmbbhEthojW3riufw02nNJ3QrSWKcULfWGsD9-A2qh0IXMC4Rzc_rLfm3WfcU6e7FjWahMeihSuQbozBRAjJ6YjVkD51AJy3EWv5d32f2emd0hf-fuI2w6MehLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb5n_ZOmAJk6EOhvPK5n_3FFZTl11CIvP7g1lnEAk-vS2nPBA6T2yxN4J-7grUnBw0aDN7tz1RhlQ_0mf-XKK1QNF9jzsVlW6gOnX3g9x5_KslYJuQ8YLOQG99w3rroGak46zqNnRz5vgZuW7Vioq6FnxEuD3UFNawt7Q5xDGC5JiySmyKfRoWkJhUyzN6ZEYzghfgy35hNulv8rb1DBDMrjvAp06p9KiIt7Z3b5dAEx3iq1nTbON7s1qsPhKELN-KuT9b1buFyae7m2Urk5AoFeIQ9eFDiDxiPmdB5dKPF1PsKAisQwn7bxcXpQ49NPqeUOvzND124Qi0s_JToC4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF0L_HNBZwa1HMM7rvc8XANJHj6nwdYpuSoEcsxiAJ-U0Mu4Z9NbiMaLBD2RQeQ7HYymm6B6NaQMRvLSWcgKpM5GsypmjDLtrNT0i9p27lrh2lJU6ZdL5DycMm2Q4FC02uzToDOwmXfWsRM4LtQmRSSvE2JTaBs7-uyuMWreSYIgL615Ki1T318eahdPh9QZdmAMRw5UPxwjFzWScGTAoMAv5AmPW4gnQpCmN95QUVS0-G2eud76WZ2H8krMpuc_F3CwhE8BpFntdnc-VG9xBJeJGWhwBGFtMu4bPlLzd5n8TkCP8_29S0_vLctDxe-pbL013grA7yQ05vX6YIQVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxWpCsjrAxI1bYNWSg8IzAi5bU5MF8KlOot1hDAr0jwQ9S2KHPdzm2TeDWUHc8JUAj3Vv8yCG2RkVr4O6UYFPuqK5dC3Y7Y96cnSfRFnwGnikXWG3gKCOPPO26PFZmEWY-aA7tC_XgnLNSsoCx2lD0jeh2_hRguBOIsg5kJWwaHb4Pbk6CNwI1jaPMRIZ-IjtcQNMNxnOm0YQdUQ5WkIEFlVZdleTkxURBKlSeV01MKeiz8h4B5uP9mfpn_kd_CJTU96N4cwwVLS2AM1K5PF2BMCcEkUuL8uEJs4MtNs5YtX-1PjODsHUdFoIBSDNScVu2w3q_LYk8ZTxsiOhTFF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ize3kEa_n2ODDN715TbZ4kNme4j1C5kqiEiF5_msDaq7_nSJovoXvuswxBFFvFXS_BEs26YNtvJ_JHyxwgAWuOy19uS202Nt0R3NIL0tBx-jboBv7lShX4Xe0vPqXlblXGwjjHxuoeB5ahUcfWFLQmJfx11L2UfXbIg5b_bGEz_YfPHoMn3aEA6eFsVyn5R485869kZ0aoApWZiUhPPa1weLZKLmR7qeMk0Dv-jDI_4OIh5u-n12nq7gmsg_-E4XAKqreNiJt49_Eh_HxNqRr8JVjEK6nquUOttOcQR5CzuwihcNCbpIAIah9uj4lsB3MoEnmvOzSgSh5xcKxlMwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl_TfqPEp_yroSQiys1Zwo0hRzxPfw9z3wfkIZyIb3nE9WBdGJ-KFjnDB6QMDEXtd1xxs7unlyIf3GL6twRRmXEHGDCVmRrzB7UUzPinkZZNYHaIPrbJ6Lov32RN-1iDiqZX1C0-3NQDnnfMnF5mKd3-Y24D6JWkgOriPcYWZ_gEdYe92u_C1DMvBq4Aj_eWdZMAF38PmA7MCpg443nvS_2_GCEL2Og5zqsRqVXV_gmpoV9jUYNLBIQZKC-zn3p70rZqguO6Z8rCS7QbVhNGLw1MalUWAiOu2c-B7LUTkpIJKItHHln_of7w03EvsNhAmgTfQXBzNkqZtnYmGZGvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As7ueXSKxLccd2-ngdwYDmymFgEgenGBQal9ux7L-gwxRRzQQ7ItVYzPOl3UUHCZDhTM6SwOmjnFr-glsRTVO04qq9UcSit7njJmqU1KW1ETcgRrxtB3NztZJ5WAaTfV7ZarxbkkPpQTw5LWyQjz1uhHvBCg8KExFlDZSNgj1-4b6tL5nD4XgX2BRkG5hoeb0XR5iwD_VLYU-ZLAES-wt2X3l05xKooMNQvRyRvCNZVx-USIBrver7n4BJWe6wJzeI_weqmepcNVV7Ueu6hVfx6AntpQ01aGL1q2Qa54gm_rGCiAVnKuGaR_O2RE1-eICZ2fbtlyBG532s35ESC5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLv_KT8IEVP5LtwgS1ntvjLsbpa0uPGdO5qYwKGmAXuUhqvZuoL-b2mENf-5DP-NC2EfZ0Ka--6Hm4zIMinWFLTdW5HO042NEj7uEsvWF8SzTO0fYGSMPnR7ib6xEdxtWWqUGpP5rCh7xCEDrqbs5xpn1NNi56NEee62ziu5jgS9XKN3WdGUGDFOh8QB1c-KAcwHVgQZtlqbA46_hTsV2PaqxkqeRMe0hLT2f8q93LudHcJ2KIQPTQVDiJ_rLvQINqa-QOji7DE79rfMM38Ip3pb7FStpcmuy1rkhpqWsIY80s82w4ccdlr_MtcXeWmbBqdffq7Gq_hvQMLIhgeL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpPSZvUCRfwawqYSrdyvgau2WhyyySV7KFZhWXJrMNJEL8CJ7IuyS3rTJF_4BpA-rZ8fX1YJwptEjKkraYoJ3zKplKQgZw4l1AnURM9VSMlkNdAs95SRvoIp3BpVozEvIrW2kCYHs1VjoGbaV2TkfuAsaLa9DDwJB6yiV8ZB30-O0fOxXt57FUeRMqxlsgTBQvieNrpZk5J4S7NaJ7FCYuwZO5gjv4LTAEGBRr3sILje_ACcvur4kRfns4KmOU2Oww-QjXMUvX1Vq0xTXmnEGAwpsaMITU03EJFMzsP4VC1V1NEzdD_MwsMaXfIUvnrl7bmXWvOhllZ7HYH5tMKePg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFPLlNyy8Sv8o9jjbSTw_jn4WK7v1MsiEvzjvGp838WuG41XHNKDrgpnHecDT93z6IP59veJGvuv7Be_oCpKso_O6UlvMD5x_RRbmesEFX_2NITVM0KblHtRx8QZzA6SAscbVVMoheHvISrQmJHYgGVBmkk_giWZmULEA0P5XeLJVX3GgYWmyKu2heZFAs6Gpk4g__2ba1RyZ6DLIXyxhB3yPC8pBiU9rLm3mne4wQLQkPkfnHkzhblswT45NXoOYUqGIEJbBJoMIYaCP4LQM3CdzMJcVqAyazuVt2ukVV8kilqKELrNiirwe6bBwBQuGrMUsp29U3TlM4j-KUhv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2q7OQnAvjMc9p4CrbOd3qtJImjcYK6saYQFEWkHCvG0IRYRug-W2ufqUBGDw2lLHkbsPUhAo-l2AE1rgZWI5YECEn_GnEvR2cvG4QLZz4JZmXF9UXplMT7XGbuAPtDcQ9OSyjI1rfKxtasRXZclIsKz-21VAu1MEXbuQuLRcqQjzttnbO0PzclrQpEzkNN6Sx4CrI7JqE060H74TQGnyiAOJu_UCgf2lGgdxhMU7TP10hMmo4VFF7b7mc7CcEi8a9hy4a4pJXdrS665ktN1rsyYq23hClfFozXwpqXP0rbPF19vOuXcjX3uzS7vKpUnfPjWFtG_0PS15bDFfk-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0R79GZy5gIH_3LuiUfVzfW5ojIL3FFyE5Pp16UqZCJKN4OP1U3qHsMqRapjiO1sqJSiZ0Nced3kEov259EazJItocRhqpW7V_QveVMYcoffm-PqJOLj5MqkT0wAIMZl9jK5oHlOLHHYC7ASaVc1gUUoSrQ56ytV5i7tauZXGSpTdzPyNfZIRBqd7vk_JmKpA4VQaYo3uVzHBPW7mLgaxz8hyi2Zt-uO262enpHZGYLTNjUBIICaykoewtLPt0f8s9mJgqo0ipzjaUwENnPeejGj-czXE40x53CX3a-RaKs07xGMjua-kbrhM0zN_EzOJ1AhuUayo62w7TvY7WRTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snCRANXE1aAemceOVyN7LCk58nPTAdi2n5BHfFzCRrMjc9ICfuxCOq7DDtSCRd5-O2WT6xDhwfMB2xfsAmqki4wstW1JKQXdYPP7gkXOF9zUWh2RgMV7j1d0Yg9OkxjYso51xDUlO1SanOItmVYXsK2e-UKYePbFGQCCYSpHOxxomRTpXWaypplGuJhGT1t3PWpz3VFXheMZT7Gm9NGFSnMXaigiOBO770hK3A3wdZYFosXB4sfL6CkzwPPdMqZkgW10A1tEqzIxTvfD2QUTo3SfrgzY3eMiK-SijDljiBNsG-uUUy8ccUuLcoQs6VXAyVscBloJujGGIiuAhHh_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJ3jSOmFEOiiD9ZPZpO5J6P4rBZ6k-eYH2SETDzpPZlH-7urOD-cqp01pJphl-2ItI9tJdC0m1g5oSA9_WFaluaew3bSwh5ffJ6Dj3gcEtjK59SJJ3FMBIWpA-h3KJtw4nOR_wax11l4gh-9j38QapP2XyPEonKqx6YanikinP368queuYq16TUM1eI8eFNfCvePqH5aB6P9Uc4DqMoV5cbTCs9JvozL14yku0nojhgFfZRIA7ltz_fOQb8-qCdOqTqN-nmw9Rlq-rJadbhhZQtln-LI-7B-vKUC75qtT_l32yKstIjARl80xfAxNlb-WKSIL9f5xQQ-Rypr3t_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3OX0kkmK-E20Nj0Xw6sa-nLjHCtPmjOPX0ojXKzynIJdTg_dssquZVfjDBX4mAjdrLzj-Fm8-jLr9uiOk7DTmWcrtM7oE7eqeKCv8VQR2BEtdLZElpxznzRlrIF_jxICx9K2e-lv4nEEBASGjSE7A9B4K41WKSuz8OnN6by5QLi_WmKe1PSMnEh6MWqHSQbPi8hIBAVXA-x1e9549wHvAVpvjR7SrJikG4n9hMbY_VBDjH3FTbbojWWNOJObO2zZ2k-Pf5NHmLYD81Sy202dUVV53PYOnV1y6U7CST0-uBNNL1PSdVfF-lioqTXRyg2667Rn9uhTBHQgUlYY8basw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEedlJGW2Scl_vm8C0hYFOM1X0aIu8ZKR1WcisXFzneaLkgW_7ThlUYmieLlnMCzkvSfyQy7v6wlXyQF1JaqumpNUkEyRcjKTwoc03FWb7zKCK5xuaYzIyJWbN3eClk8KBURhctsm5K46xkxAjbYoAj8iR1Lob_Rr4D006GLHvDAr1GU3RAt_-kyVQ8iuTUStd1ICk5t-BKxK3vViVQe5d8SlDGDUz4BLnUQ-V9NwBfPSM2U2_tnCsH2TIAJm6ZQgj8kxXLi9EiJ_vLA95V_viTZC_q_-wl9GAJ9PjFpBIc5rl5S66wGZN2M2UYJmfFYSzL8Q1JvkGOgWn5kl1TdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlQ9XgFxEwaL1hFD0SsX9h1S-_FZKS7ol7dnPYD3c_SJrf9Mh8OVza9axgVgA6DQELtC5-yAfAHbwoUjzYWy9adQrz1m7az2OG5KEZM6prumIpbrzHHRZevjow4yKmF0_w3bXH9E-lZRgoT5N7cSP8hp9Ej2cJxxVPX3n3LoVE9V2l5WTYGoRXDaXKvfTChW1yYBJLgvZ645vp0qT2T_7t_vRxazy-Cd7SRQRm63RiHeQzUxb4v-RaFM0EiBNNZ6ndK_i_jtbHfMaRLMYpkJ9TkXcKbXWcmljw_b9QA3OwpteZ6Lnn7UFc0ryux0yS1NcN3bf-t8AihCF7SLiDhs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k61moLGKs2K5XhlpWt3_1cP5-nZI9dNM51cymTR3XKeIbqCWKb8Jk0zJ_6xoOjH2yINwkqdeg6TPEQsnBeE9veaeYZFkjTgxZQgXsLN4tpXAOvNY4unWPM3Dbi9ze04b1XMc2VbhQEic9Q4YFRrFrnNgm8CVQSL1zNphoBXFXlB_sghXWVYJl91ANSFAbTifURn9HOqX6WvxsoZVCW53JBAJS0lmQsE0c8TcljPS6EuvZaE39a-3BRztEo-LDKFNutlYlp5l8Pj1q7mRv_dBp2N78GwYayLZedmlJJwgtb3jMpZp4-HAyJlj6tGFHbippuEx36HBEKuYH315ggZ4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIl2fbO7sW--5zC-q0C5wwumy0iAw1XOtopyepksiLomAR5VebCEWtPS_dSvt4D7Nu6Akvu8pXIXCVV7toFP_MO9ZHAgoy_Ceaxq_3bmRYhL6Xaxva0avGL3FzGapgB9iGhk4Pcz0fm_HsoqJPri_T3JAvJrY5EFPwwayEXiQ--U_2UYzqVSJv5BQBHyZ9Zb7GIHW2KFFYJn6vd7AZz1Ij50G5SOPSWE97HJqY_WQq7arUQtXpFEZF-Ay11yxJ4xCgTe287AJhjqpCD0XpVqOyXskBHFI7SPm_uAsXD77Sv6S5vEGIPenqfBGg9LziSQavR43hHTP8ILNgbuhRyiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=pJgfhsYLt90oNvt08rnGYkYc52fZ9ZX7rsOm_02r06nAT6SfQc3yyzQK36Gq8Ag93ehSo3L0kH2PovBsNni0znQW27Gu9-_H7SwDncX8LErX5ae7uIa22_nDMjzkBHjNufBgvjbqXQLZvUUDhfhmsWM2uphs4xnkOdETOYB5IPun3bLnF36Wc3DzQkS0DzQ3HzyvU3XdOzBkNdkba_pil0SADoc--7Oc7IX-VEjx4sechkSPqFj8M4dYRqyYn8N8TINmaZ-46lLeJqY7K7DOpDi8MPfblL6nOwWQNoWeQjmKAU6RjX6h2xuX-JrR78pO_Qdj52NZcEOijZxygx-tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=pJgfhsYLt90oNvt08rnGYkYc52fZ9ZX7rsOm_02r06nAT6SfQc3yyzQK36Gq8Ag93ehSo3L0kH2PovBsNni0znQW27Gu9-_H7SwDncX8LErX5ae7uIa22_nDMjzkBHjNufBgvjbqXQLZvUUDhfhmsWM2uphs4xnkOdETOYB5IPun3bLnF36Wc3DzQkS0DzQ3HzyvU3XdOzBkNdkba_pil0SADoc--7Oc7IX-VEjx4sechkSPqFj8M4dYRqyYn8N8TINmaZ-46lLeJqY7K7DOpDi8MPfblL6nOwWQNoWeQjmKAU6RjX6h2xuX-JrR78pO_Qdj52NZcEOijZxygx-tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZfIodcdVXJBs_lzNEpT36OMnwbNLsaVvqToRK98fo5laur0TVzoqNisaAXkeUiOHR_5BkfjRZTc_XkxVWN7mZjZ6LNr9au5Rrs38DCRZYo_nrmixIC1VM1V9H0YtnkMil8oWFp1okq2YEXCDJgb4hVqBg1pVgDs9S6ajTPTbN7mnu-VxCTknw00jMvezw5voO0-u9Toi3zfnzp4fHIxXSiDpdDFKaMSCjO4VCpnVCCetarel9oeoibkFbAc3YXaXNR0ew69slfAS177tRdRxJ_uGRcCzLP-EDzcxanqpbYARPBes4kXa-PQXMjLd6gKaUsWLvKfTrwpqDPcbLBfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILP_5li0dNme4-ptFsqW89VMJbvzaucWuq2RQXeuGjCn-gOz18r6pZpFWWTs6glY85pvb7DM11W32kGv5epxOySTq1rTlPau2-HKD_r6zr1YzdZHLl0CwmL4rSrxLKdlSw08o-68RosUGZiSpdkjjS2EK34oWdDFEeg6mQxk15R1jDDn62AdeSvniyRcoUXXMBLgAJz83R3Gkd_dUrNZiaPmpFnlAx-93Y0GCJ5NEGrOtBAKIHFrWDfTugzgRirAvim0wOIrekUql98FpmUJQ31QCC1iPu_rjZcR65gD4JRC0XoYq0WufjN8XMSVTPdRZUtXeUMREuwSUWDKQwfuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVpsuWz5mVEz2Ge0oUj1NYajAG08vlTv4AlAypmdCEcNeD39EzweMynwPqSMqXgmD6766C4cFFVKEAUdDECNa3QdIYJz5gVJqjqk6_-xoVUzEJ3lH2HZdKZSyEm8UKnjzxpL3Phm7sgMb9oQTyPZxScnCQ4MF70pPdIdr0Yu95z-zwf5LPKZ3PkGAaXyShJg0Z4nxVciB5IL6h8yGNzf2kuOAUBkY6BBxyhSTeTusAVR92xQy5jDq6VOtS7NZHhHSiSEtghPH_1vX_A-Iep1FXXnbEgTPL4_0zPf0C7UI4PRQWXUlPt_A4R9jSDKceotrYSaRSy8rDxQeOGZmJlioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV8i5-TRwz22Z5ilvNPkVpEQgaZW_UBcjyetSbZAyY1qkalhpBoNR4QP6eD8rzfIDLga9q2RHfxoND50buuBbCGDe87fcAu-KjiyAlOGrbpl_l429o-ZNU7gcK9IIua1Hs8qaPkCo6cQkXWz_1wwi66hNeCqT25YVHEtMjvCR9hiNl4G9GYAKMH55XLfM6VJUZbfGOh2seR4gYMSlInhrlgceAoW2t_X3Z9JL5Ta_S7PN-pU-FVcZ5zTUcwGC1XiivSJqFSS1UYnogL9_GFH5tDJMChuOXkmn3YlPmNcCVSMKtGldI_HoK2r9Y1PM8J0kcbTYhluVvtgGBmqcoudOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1gOK7aEloVUR4D_iT2NUU4wVitdvSJ1u7l2zo34oY2lobQ891dEXUe3UWKS6OnSo0RuLAbteJkvP_FsqB5ikU4LRS3FuxJU0JzAEnRtDei5nqZBuwWxlZOYsAnxU1ow4eJgf3CnsAusdBzDHe-GgvHUriWsn8Ar-Y1IRYQq80bnU5G_p2vWpt8EIMenncMriurv151ckfbA1xNWLyqDaWyKkeoriX3PuZYwL47Df24qV51Xo5a-uy3GLm3Q1o_XvqCOYge8ve_haYfDPeRs79h-vsjTUHujqp1XVlvT4Iezyh8hTfwq9UtfB9PuacaLdilyOp-uxKUAHDogShq6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJoF8D7N_ahj2gsYUHjQlj2GYPEwWY2Y-tSqIxdTG9pWbKxtQIHTQBdCVZiKp2O7zAsnl3lzI3ND5HEmOzcqwSw6JOvTCEVN2xnzcGlzmtcn17ddSZf-Xc3I5gH1pkhMjL0N19lrJQxGJ-36cxvEcKGfDM1rNXtFXVjBN_o1UX9zWF_ztI24QqFDUI4SpLxGd_cPkP7Ir2TVSdUojt8ISN1rT145y468DdhKZout-iPdhLvc2O5O9UHTkIj3JjuxyFexdAvije61wn40AVZ-0GurxiV8Nhi3xEtaP0v5GOi_-VuFf5pymA65KDsyRjup_fIBAjjzPsK6FLEGpphl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn7CPCQLO6AVjjXCAoR8F85bfl50rJkO_rRz7jH-xxUGcZziGbpB-03PVkXRXVuGD5WxnquubI35DkPzIs46tGu0TnFwtS8kbxss-pLM6nnh_k-VfrtvksFrRx_vlw4fJUHPhLb3382FJXeymfoZpOSgZKTGQ3Ws1i8feRvlybDCgQiALzdIEqMR9ZpJVYcRDb59PKHOzVYztmEM3MKiNXS_vQZcbZfxEfthDFXVQ_2JPXR3AOfIMEalxiBo3wiMI-973RGMbO3kOedTU9KWVBuGBYPWp1J1wR3WJkqYTnuPpAl16F85L0bmunMTvzpqE_aA-H-eOpbBxiBu0C3BZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9_1Tvg-oZHM-khwTvezGAqbrnXMU1vxCX1ZTz4nTL1nu71KRAkvkpKHEvH1SNiCkqmLyoqavoJaZY8Vshrckst2LdXvlSM9AcnHzmz6Syr_tuyJ6T-QZITvYv4b3KGxMQXjs104O7FxW0ui-sIEaMkNF0c_JW0k1Sa-MSLqEJGLLodmmltHmc-LHyIZKhhpJcD_BAs4Nz9epK7YsGnV01267TceZnuHBL8MLKclMZEMh3uPLsE9RZLBYSmhrJeYlomqUzN7uX54P4ohh9Z-EPmftrRUfLNfobuACsaYtlcY2UyXcHCfzckSKFdIrn4-G4-fzM3zNSHdS52JNWTBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faj8pmPx5LmjI_WtZbdfkif8DCKnHuMgQTXI_G478T5KDe6z63eSu7IU8ZUGw93CShmU5uPCt85luOpBns1wVLbFIvsrp_zE9YamyYcdtcj-M3trFd2vxIYH1UTflECFRZ53Ia5laSS2VO4dxH-eTbsXf_MFM20K_4PQqRViDYxrOMKqrhbHYNgCE3tZoH6UEVQ7AZCZPSMTYvd7w3Utnd8WhIOgrkCTvd1AV4DgmMWA2Y2IxQoEkKcGqDu-B36TFpf_F_K9AQvJflUe8S9GSXpDXTXDvzPajbaLczczts1SDqbsPRCX9EysweqFX1M8ejFTux80W2zJ2s5OUUcS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRe2tvVy659v9FV1HsIRlHQOGIerGrclVL6mos3ALRDIsqawhs-MIAolnTUBEVQ8tdWyHmmOal7zt6mcBjFIG3R9I3sv9ysBvRILwRF-J6oGkzmhgKFqA-lLNrfYYCznT2h5Nlayaqhdv1pFdRSP-ztkx40sRlryABAwWmFgs3i6GHtDduP9qM58WbFaXKEg3uPc5DYV_tXXd0K-m2coyaV1-KvuL19Q9GFRR80D9a-Ew2NPm6nIU1OXldZkJOC57RqHMvne8G46olNKGGqd5jJovvH0njt4HUcKsYkEYjMbCVxyz4Rky-CLOrAjy0crkyozDnMH8LbjWoru-sSW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZREwDsUtBsMlf53C5IHnx9QV99pnge_Ueb_2DRbK1DeaaHuv4X4IbrjBH3lyz6p-PU3oAYiREF3tVDQxOzLmrCqcy9ZGLNq6GI7uLQqMjB3oC-AKAKoHFgzE_G9tFsnaYzIjmtV2aAvz4cfi_5f620Lws3BC0swakDZQpuearVh9KoYwyloWdreM_hKgT-FkCUPW59raAk9hgJfrw9E43Gh0V5mgELtnABnnNtSDIv7dV7BrFPM_xX0oESDeFAeJRvhEFQ0ncuBkLV3WuRJ0aQY2kldss5hvvG73kBmK6Jpwx3RZ7iPHZCj3e73C-2cGrSnvHhVNYBtH3wOk6xh-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAjaPP76id2KjLwpyzV8l2JHR_Kgb2oCDe7LbVhl9XJquEDGLo0OFpstIgBSQdh6ewZ3RbzJu9hNDVOYlCSIyj62goAjGVeI7Y_rux57j8Cr9LMXZQob-r9-V8CVJtmo-TLsNEC06yo7cCOIrXpd2LRbi8hgn5dsdVRyzKJIEQS2WNFB1l1ZevSRjZT5vjdjz6LmOFriBthUbneag7xAuDhg8_1RqY8T59gVnoDZR_IP2mcdzmdimbwOd32pQZfLTVkmjH6z2Oz3NaRjF5bwzm_nASAdY85I8RqfKdq395PW0Yd-LS-CI1tCn4QRjqis1mHYoiXTBddAms182tOdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3G1tYfCzWtWZ1VmLJ_mpu1H7O8xS_E9vvV5ma6Z52oMhLvSnVmnokfoA24xaMpy1LY7HOf0zQmMlqfa7J6HKd8d2L5rBZfPhG-wc_cAXa_YffEBNiJMhniLwEE5dI88KTp-byjVmdSrd8ZMz5G0iEvN5XRGePe6coX2G6cpepgIBYrnbujnHKDcfjU-1a8fEtSGNDub1HjNZNfFFIQDRHU6jXbrHvj8XFCeepChXRAZBU0X7LlcfV2fOYBX87Utrzf0CQCcKSNov3uvnXg1h_5T6qwCL7AGg2XanQHrWrQ0fjNBtNDqZYBpZP2YrjHxPJO6t6DeFXysFlp5nAL-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=L9rvK9y36Yt01NX-uIMK-0elV3WTcYbCW1gupQ1guZC2sgHf6hDQYBmfwZiKdXZIVeDHpbWRP1D6y9gomTIiwFbwDrjYtAUxgdZsZ23IRNw2U_1TWDkM1VkGKDYmSJGyigeYUWLyE2NtFdzjAFRBV6wR2oSnZxTsTgfxNxvrBJrGr1lzPUtiXmF2O9NoZsyjGC5dAs-XekSLmc4HzqULIHJe0FHja6Z6BS_HA-SQ_QxplzxvIdRH2aEe4I-oqSD8mebK6ufMax93nola0wNcRoUXysJEYEbib9nHXU7eY6HcO69hRwyAG3cMoH_AOYpa9cWEHT8BEwthheiOMZLmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=L9rvK9y36Yt01NX-uIMK-0elV3WTcYbCW1gupQ1guZC2sgHf6hDQYBmfwZiKdXZIVeDHpbWRP1D6y9gomTIiwFbwDrjYtAUxgdZsZ23IRNw2U_1TWDkM1VkGKDYmSJGyigeYUWLyE2NtFdzjAFRBV6wR2oSnZxTsTgfxNxvrBJrGr1lzPUtiXmF2O9NoZsyjGC5dAs-XekSLmc4HzqULIHJe0FHja6Z6BS_HA-SQ_QxplzxvIdRH2aEe4I-oqSD8mebK6ufMax93nola0wNcRoUXysJEYEbib9nHXU7eY6HcO69hRwyAG3cMoH_AOYpa9cWEHT8BEwthheiOMZLmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=T1ZWtsZkcHl3Ix2qSQsG0KRXjRk9dXHNdEqhVZB1pAyI5OgzwZIa0jP3tstdtS9wbDWt5R-Dvu8zT8l5HReK1EM3Vvqr4t-ivoQI4knKy0JX7EoS5gpo0rvhA5oA5OPKKQG6XEvvvAV54aeIndcerlBmt1b02YFpOcG9XyrIwpw8fA35w1_5USqlYCrBpYG6AY0RA3_4ERumyYqRNOIquUGpaLmly5PAhmSfxDIHzMwqHe2QylwEdh3P6q0AH0hjVtSp5CnAfJ55x9irQylC_PKhkcgRhsRsPqoojrCwbC5E-EqW2pF_cAPDQfvOAOcwM0G79f_0f5qx7CMRdWpySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=T1ZWtsZkcHl3Ix2qSQsG0KRXjRk9dXHNdEqhVZB1pAyI5OgzwZIa0jP3tstdtS9wbDWt5R-Dvu8zT8l5HReK1EM3Vvqr4t-ivoQI4knKy0JX7EoS5gpo0rvhA5oA5OPKKQG6XEvvvAV54aeIndcerlBmt1b02YFpOcG9XyrIwpw8fA35w1_5USqlYCrBpYG6AY0RA3_4ERumyYqRNOIquUGpaLmly5PAhmSfxDIHzMwqHe2QylwEdh3P6q0AH0hjVtSp5CnAfJ55x9irQylC_PKhkcgRhsRsPqoojrCwbC5E-EqW2pF_cAPDQfvOAOcwM0G79f_0f5qx7CMRdWpySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_0GTOCYJIosc_R0f96EXu09xR7JdtS7H77D75q7kGlH4sdbFqVJc24vGFkq8gyrrwivHSSnya-9bskXX16RqeRuIWunQSoi4rqflnJjGUA_D_hsI5T8FufCz-SoH5A9ABf-mmkn8-m9c6c5SG4U1aKZF_XvIMXJ7JI30MP_OzPqytSrEszeJdt_EVC5tji0VyXbRzI7PPYehERgfDGbBtya27KlQTX5luMOgHjYpBeRr0lCRNjy8H-UhvYlz0nrN9XwxTW1EvyiMMfPdbNLXjajhiSLL6MLFrRpao-RPDeR0FGyKt6VBaGTQli519fuy6z4OR1rCBicKviFvicEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzv7EVNrU5Bt3DFtWHhjJ_Hxx2i9zrOF0DDlDja7jWaGlmy-wiOT19xITY9tPOqsd8hwGNH2GlMRVJ2jrTG6GslIRU2T8ni34eBnnkSRRNbP4zBGGSSz71Ne4kUKHgMlGge8VeliMXvLTqTud0Rr8_Zfc7PzUdh0t1GjzZyTDGlyBkB18wuw737kMogt-XGBAMf5lvSqNviqrOoGhXLP_ioJPpf8Ssyrt6iWh1x6DJWdz_5pFpQQaOIIS0RW4ET1HhlGvHI3L5nwYDxqtk791FvzBTm1Fjc4_4U2OhR8f8_Tzc6Z3aPv4Mz2zTmiQ1eapiPBVlmIMVPNM2jJtjWT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2IYx1LTA7PR20yi37XCtY3XnJYMo4v7bLO_CJJLj9amNtdLOx3odENC8QE9dogLwLlmoG1MJxrOHbn-qX9GnsUlFbqfYDlPVm2JCHFEw8OGWOiqoVP7QEgix_Vt0q_yQKqlGG40HIl-XEXgEg-X4wiDFYVqV3oMUSHgubnEmPUR479XOz5QFsCADO3yoGShUe4Wg7-WCoCf6OpkkWv1IHkAPkaCroefYHEb10c64oq_3mNdE9MfdnZerlpj41v-AZP-s662-l3MTAIqvYoSF0y2dWkFtj09nqy2DTAjLvmmCJqPd5meGd_dVSx-GPMSsJwn7DWDZ28M1G5ZjoffiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4vv_R-lS_3_xDuBplgmDi5ah0Rl7BLUQUv73yuLs04cHd5MZe4LJu8arSzLYP_wJYW-OTvigZ6Jl5CkEj9LvMfgZ-X5rjBi9levJIkbKN9sIyJVa3nvIwXmRUOMg1Ef4VSYRQSKrIsGMByEKObRYgIJJ7NPhjXhlIpRLuaReZmKf4gLX6kj3em1GPWmnbEL8H8oE8vKutnlBwozxz281WgfcfihbnEjICsSNhNtPs3Ectl2TVeFl1Ak7HSLTmGOKtn9L5308JxKyBq24fnpaI89jUu1ETLk4iQuA_E4XnZQls1R_FAwr87AefPyu10ITNvqZudPjPSzoYqngYTwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFphnW2JN650QKPBIoYWoizvY2qPNW4hhJ12xGY56KIIiNkY4CVOY1DRTuBbklA6wZ9XCAGk1pC-k6L3BFrlor62MIidSFntPtRVd5cT7B4LdeKVnS1PZqZJh0auouCIJJEXMiO-WQwEp1iCqZPsB2uT9cByI2qOMIv3PGZBUuTYxXvYDXL_ztVAYD0-COOYB6295VSdXIXMvIyx-RRup-VuwyRwymRHTyup311h74vNor8jv03mEotw1uWqxaT3mcB4aWbHETCS_1wJQqY5muqg5zoQOHWAF9RabC7THsOiZXCpbYn8zE7oLXHodOycJWfjOM88Mpxfb0kBOJMk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFbFGURFW5ZO4kWZtGPUkBFjKHmLM3fD2XQsn67nYXyPxiqSUihbRhySVEBD6huvi9xYOgH38ffoZI5RlLYXV7Q62xMO_ioU6WXkLX_yhZQ3Zv2WSOYEDN5TnmN20SsFjhsY-y3LVFhR36RDxQVQTKLLOttay9DTfzmCANoDdwhiaZKIaG63bwvAKd_945X-cfZ8oA4DRvPDE_qdvhERtM4l6R9KAW5lAxEOUMng6OqKMSB6YEZhWNTSnoXD0yAmzWmkUwFXiCp9z83v7hp9OUmpGHDHFVsdmfS0T0fXBiUneUwM9BU0MNrq7vvsky8_3ZerlvIBwIGZMgR9U19N0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHCO5AjQ5bolBkRox2TKNTS2P2GFynn3csjxW7LcwWYuo7potU-ebrxS82yqOglxksseQinU15Jid-E85-itOBGTTXOWaIloCsoD6adka0TOIt34z7bNGf52Y5USviQiNJLuXfaXASLYCpCrYNMMUqNq8a2SdOnJR8eXZPlrhHK214YO7Fy-Qye9ikiZuNnth2VYmJerTOxzlCr7MxGWGPg2gsxxstjxl2_3KEsZPP49kDU0V57qOIGWPnU9a8F-4jCRW_wapXjRJAFM0par-Wq4A9n772ohP7n6Of3m-LY1eaawEnFhj8Febk_iVK-BHGtfUMmFKw-gbyoeZtB2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-FM20cxSoTuwdZ_5Be5k_o2PGmLQHcuQcGBJY6_RqI2KPLbmjaECw3kRUWdG57Yg2Vd20TlDYXSMNKrkf1gQoanWN7ZXjpXAoKzC4xGR0CZBSk6AxUSgUhAE01Naw_KnQ-b8U_fAJXSq5LELRaWzwauAnYiY2dQ1JK9c5eI1miWZea5t8DlYnonCQJOs6CJl6Ir-NewulHoh0glSLNN7BfgSD8-VQhcO3FqP9O_JsMLMa7u0i3zwHTB5vP--YMxGAxOmoiiTAaFRJrotL7UXYkWrV0sLKPUuuKf6TpFTn4vfeVP-g47L6ikn1pqKrRb3ewXXBDJThtOWDRI37VoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3jUq2g0LwhZOdcrf86EtJFB7i1ddysoygI7IeObOYZJ4NhvSAB0fHKiJ17EsD0ON5j5Nssda3tTaw45GBtZwX4ll7YoLz2X15PRYgy_u7kNXHbRSksCy4-n3fVVWWyDFXYhDqUys0Wiw_7420erPpUUcNvJNuoA9FNK49_BymyGKEoQlw8ZClushrSYXdJzDvoHPV_Q7uIgV5_7XzEX7T8wvIRxkoxoaQMENc_cEnr6BllQoYlmdIBXg9MAQFnI4PW-Svdo3hMf2Z3NjnnHxbTsre2eb4BbeXdXoMpXlWdIlVv9Zr2Yk4A8sibqK6C2nYkWwAFa00RW_IKT0sD37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-1RuYvHXzJHUu2B744TuM8JDO44tbhkto1eVTfRP0CX4SkN8oWPq9RnUaH04eHxZDq3xNOry_IDZwmaPWtG_0rK_tRH9lN_8yvho0J7z6B4Km5SKJY3CAqxVofIL9FR6mj5iwnug7yWElH4aHFHT1QiiMfHqZOG3LM8aBpN_B38xKiDJxMlHIm7Z1QvXwITDKfaam83-QrSFHs4Vp9Of5wLerNqFyaVG7lh1KeHLfQWbHN6d7P6nvBDAZfPoFSBYRrk9dJH5EdZ-LjXOuATF4t22R3lRni93PCAwQfZCUIV7QE9uzrEbKYD_BsJvXrLDtkXvgIFr99Hewe10bdNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=G5CNg94OcC2YTPspzHU_bT2hE_72t5HVU_4CvwqRCSasTp_9oCaKacQEP5vtRgRwKv_v7xhse9SW1g53a0oseYp2ZS64F9HaqRDWgg_KqD3iEqFcO_1TR06im1MeogBH5zngUgromRYnmb1eyi6X-HW5vT_xaNuqT1Lgbt5WKvpRQuRzkWwCbjsjiKkOFNsaeL7fzOaqXSzpUD426Vhmu2VGh5jAQPYvdyywfJlEWO4XxDXArKnVmlbIVyr92Y62__u9EQ2D8cdNYM6GvgxYFp52GGF_RrcEj7FeIoGASNIfvVG1DBcgGlAkJV1q-RkcrHnEIn_WDP3dBhkTGE6-lrWRvjewnPYTygyPJMTRGBR6S3LQZ1C_XboXHZjesgKrL347jlOBGmf21LhmZWFZwmRCF5DZNr-b25olfNsbnWX7g0JZKpiQb76T6FidT4lEdwjyejVChexlOTfDNvMChDEAWMFXDNbHWKpozx8oqgLzVkJBTDd7SqOk7VCwstL3orZXsoLT1nDyuvFnjm7W5CFlaCOOLXhxPRS8QgAT-xg3fRd-mYifSiiDABeqvPfNhf7tXkhwXYX9M3rLWwg8pQ3z9hWz47I-gWOqbk0J0d22yqnQZhub2uTMRShpop4rR9BkFzB4AtYkCn4gtb83R8i1STuaaksOW8hBtUwdnD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=G5CNg94OcC2YTPspzHU_bT2hE_72t5HVU_4CvwqRCSasTp_9oCaKacQEP5vtRgRwKv_v7xhse9SW1g53a0oseYp2ZS64F9HaqRDWgg_KqD3iEqFcO_1TR06im1MeogBH5zngUgromRYnmb1eyi6X-HW5vT_xaNuqT1Lgbt5WKvpRQuRzkWwCbjsjiKkOFNsaeL7fzOaqXSzpUD426Vhmu2VGh5jAQPYvdyywfJlEWO4XxDXArKnVmlbIVyr92Y62__u9EQ2D8cdNYM6GvgxYFp52GGF_RrcEj7FeIoGASNIfvVG1DBcgGlAkJV1q-RkcrHnEIn_WDP3dBhkTGE6-lrWRvjewnPYTygyPJMTRGBR6S3LQZ1C_XboXHZjesgKrL347jlOBGmf21LhmZWFZwmRCF5DZNr-b25olfNsbnWX7g0JZKpiQb76T6FidT4lEdwjyejVChexlOTfDNvMChDEAWMFXDNbHWKpozx8oqgLzVkJBTDd7SqOk7VCwstL3orZXsoLT1nDyuvFnjm7W5CFlaCOOLXhxPRS8QgAT-xg3fRd-mYifSiiDABeqvPfNhf7tXkhwXYX9M3rLWwg8pQ3z9hWz47I-gWOqbk0J0d22yqnQZhub2uTMRShpop4rR9BkFzB4AtYkCn4gtb83R8i1STuaaksOW8hBtUwdnD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXytDQDM440WxFq5LizefWBijeLOyfOmhzfUtakiyvtOC98UyjJz6cEqQ9WqLgwd4gvbvlSSEPvb0CktVIvsyjJzgA9yRUf_0yz2JKux6aLZdX2rmqzPGNYiJBk5AEVI1sRYPGEKBYzSrq4FiIJSNBMzYQX2pSeEHsiucHcQu9DlLbyVfZIyj6DwnNrtH6kdk6k9_QvXbUTuM1BQz_TV4lPB6Hmm3dlpSC0Y_gMCh8tAuPcPeDnsowAj2Ift0sAuiRzdzvWkdzHjVOc7D3qoGjIRmmKwitUBfKXVshYXgtbL9YWj4o_CI_P0NF-dMqRLvxpN766_oDMJFZ2iqir-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6qNwRsLjIN0smgor-x32-jSS_O4oYD2ehVsgUAWR8aJT1SbVjFwvC446fejh8vnUbdpTi-k8CKFVsbzx8c9xydtKgoBetE0lU3j0U8HO4zoapWaFNAGXaE6ZqC8P8pJxPbuRow5aNXdw8F_jmeyvZtmYFRJ6zmVnyBZQ5CPYY8MbI4nAq7Q1w-4EZFz6KNg9hteTJ-J8RwvzTiWP3oeXOTBys98ga9H7LK7XghibWy6xH310id_YFRv59bK4dWULFHehcJxB1onYceaMPm_MC47hGde5bW-SOB3CmM1Tt610IcJbXw9EPjvpyr1vIdeCEIyAAt2MGFcrrpHp5qD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruk92OR81LXcL1gUBupWWggkgAuNbP22dW1yQFII3kNLoJW_7oWthdYbFcgboeblKq2IvjGDEv-65WekZ1B-hri2i0bruOv6YlQ_jBsFmjz01iqE_1RXjSdhuhfCXciuZIsKVg8h4XUjGpuM6jDaYVmB3EYdRrlWo_hF7hgHs_FWYynd833tJwQkbxS3AIYV1jAQAuUYA8tvQgRLCraibsXDJZpn-sVqiDweVj3Gy-hfKT7WLIevpUMI6YJeU_Qq5LV2C6lqSZFiSZgK_HWsz6e3SOQDNOdMYUBU6uYC5Y8ETuOBEgCTwf0lLjdGiBj0o00Bz73NBORYF8m5hnVE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=MV2dJNKeBN1cANa5iqSgccAPQEwqzmnWQw9zabj4p7RoKlpPQ8B32LTGPwVOpi3lFDLwJCiWQHnHcacgucrnGubDf1CwmTKPrDbsWDqnPcioVABLNKJcD1odzqE5kfxeMe9uuksBvS2UUjhXycaIUwlf4oc3gIYXFLVwoJAZrrY2ALyGK4d6nhtZOWNFgBkD5_EzApMJHC82P4zcVy-Bit24AeKtG7WYZ8C0YcVwz_4BCCeT_2mKD1Rs2BTxNhahSDng_cXe-AkNNZaWTI9e1mmR6Iiu9liKqYW1FI56xcieVvc2_S2MgVJ83wT-lzxkAvt3bu4P9KbWf_e_r4UQeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=MV2dJNKeBN1cANa5iqSgccAPQEwqzmnWQw9zabj4p7RoKlpPQ8B32LTGPwVOpi3lFDLwJCiWQHnHcacgucrnGubDf1CwmTKPrDbsWDqnPcioVABLNKJcD1odzqE5kfxeMe9uuksBvS2UUjhXycaIUwlf4oc3gIYXFLVwoJAZrrY2ALyGK4d6nhtZOWNFgBkD5_EzApMJHC82P4zcVy-Bit24AeKtG7WYZ8C0YcVwz_4BCCeT_2mKD1Rs2BTxNhahSDng_cXe-AkNNZaWTI9e1mmR6Iiu9liKqYW1FI56xcieVvc2_S2MgVJ83wT-lzxkAvt3bu4P9KbWf_e_r4UQeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJVZhTxaII0gB7zBKlf1S7lqj1PfvsB5NlZC7n9V43etbFC3cHtxrqQOzY3p3b-dMPCfMEBlODWZfmV5c-Sa8kxCUNmULqEWXm9V81WXAz_9l0JEakiM7Uqu8kEOPH3lJX_WIoXI1IK8PA1ISmC-_245e4sLyj-FeiAfBr1Gufry-dV2iMPwDJXcmVnY_3ZgbDmWOASrdWBEDMvQID55-Y3GPXQHGRwCHh7mddygGfTvVW1dbGFKNkQSnmVFMvgpgy2s_brRr5j0j4dpVBYCda38twDhP5N6MFlsK7hhDj7_wmlqPWebYE4WkRG-0MiQ2mn2-YVzuIRQCOFcAfavRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NixnRIQHY8ybTn3zv0f0d063RdKssRNJQ2_WEF_RoFCBIpf85ftUredsz2bQ_L1WGbe3EpBLVaLf-LZCx_AjBinMSeUm0TKNQVbPTfUc1FqxGqfZwRReXztGCFNxpd3wgOG3EMIYdl0LzL6sG75LqHc5Lvx1W1W5sgZLCkHDERv3nE3xf9VJQ3KrAkDlrInt-19XVgfzUfTDho2uqMvQNSdBZvGZpqm08CmCZCwKG1gogMQdPekjCalZIGy2gNms6tXm3lr46BH3enMfKkcdDZ0s9Vuqh_SszhcifSmoExt_rjZ4vDGSZQT1Lw8u7bQHqUdscLGemfx3Qq63jcmwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRqVq5SbmL9QoBSL3JLS0rFTRh-SEL_EvklqdC4hJQn2-UrlaLl-yGmP72V8hdQzm609yuFg_83JLn1suUbvJ8WURL4a5kFan9qQRiD1XT-GpX0G_eMcIGKyJHh-3GQZ4ZMr1X1y3K4g0Rce5FG8XpczPSpIkG8vyX1alWSiBWJZh0xmJlM_YyPRP84sGcQxVovO9NWSDBxqCGBYH1JBqFcnChTIqpWfPK8KJncOhzWeF6_746Jb1bc6iZu7gwW4sxzl82Hv_61CMdY1u6R5mJuUcODeLnKenFVyFx-0foVcMlUg8zM04EG0iDalUz18pDjFlrICm7CnOZNVmC0ppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwQvKzRGbJNKCrneyF0ig01ClIk0i3DrEIg-wFLhcHeiABx_9yyCTCgvI4Y4OSM_GxHLLWyLA3CjgR1Ig2q8HmVNIkKUM_4j2odNw1k4Z1p_A5Se-dikEbgAhvUgKnhqboMWaFyaZ_WzFAaNDa568r4sst1IK_zmFGWljZD_PQBSmP7tnXoee9OHIgC93sY4CAfDVnrHqHH1wcwhCRuKaLO1SWE6A_UcB4-pS5ltZFom1UpU2ItjbUb_Dzgzbzeo05LqUMx5SdcrN8Mui0YNjU8vNofetGOlIRCiDUYYFYQGuRDDZEE9fIyGzqI1Qd5ZjH2E5sNK03ZvHdzhCK7cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gu2B4V9tj_0WhvMnRKDxIcGctBr-hdHOx2kBo9anJ6G6yTt0Ffg1Ho1uDgrJP1Fn_Jiy0_I5keVZi74BOKC7qcW54lTdhGVSq-hnGs6fjQNrwhFxRHrEfdDbE_hD7GOnbWoAL-vgRSp02VtV8GKjhA69s4zd8rHBozXQMwm-E2J-X2-ii-x4v5xKEBkNPSO4dpQIFAJMhokcPiYwM2-0QtNEi1rm3qSskEkoDTxycsKUaoZPvduDlpsbRL6bp9l5tp5IJ5Yq7GZBn5HspOIYIyc4LNBeV2uf8dEEUxom7m-2HcpP2O7zx2OrnCfvzBstZYaJQ304fG1F2dN4o9TXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIosUA_CAenAavhDzy4ackNlUboZYEpu7mbiWQ_XRBGQ8PvF_JFukjFiYMJj_RYQ9b-AHxZKEGAVT0lxVu1ol4QTLps8_5rQF7jNvXbS5v9_n5iEUzXRFMimy2_2p7rVdvRJNw3iE2m0xgjrlPfTqMyxUpmw8sL3Uotpbkq1E7blYa26mY3yPCkeIsBZys0ZwAr5x-fk7Y4vvggJjDIqxVlVHCpfkhA6i61L9Hic_nuUqKOL1IPR1kF7LYHiz1PE9pMVyfJ94OwpRq-AkaEGKR_3wl_kwvb45R1qdhq8Y5kodE35jrza0ToK4-LmJV4SuiUdBj277ISq8Kzn4pzKlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjR08TpU23NnaRXZfFPubVnmgnO9ASDWGXGujO4m5k8EkC3n4I0ZVDVpxE7Ub42FEAmu1SjtXvJ5QGdF_y5r30_8R8bLf5kZyOVv44wEr6ZZBnHkR6NI3wqngY-K3ygS7ZRuHGL75Gaab2QBPuWQwQj9_gufz5mJV82TnXDTnEAHlr24D1bCBafMb-SdT5d8dz976ZHB7UvKN7Xvv5tnp8nV8N156wnWitCZ8Hhj3iqmegEaEQraqSZUdTU9RfrqmEfF3DMRuAp0yHsLccGYSATeteQcs5qB0VUin0E6-j6eTIFrtZCqRJqEKp6XxHCCgk4I9Y8zBYpqIllQrP1FCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM1shGmtz9Z1vqm7ofudZX-odgU6QPlc8hGiQZRdjWKuTWES-zC1FkINOdyfTgcNmVUQJnsrHOomyw57RSKiTJXwoD37eb5RxNvCnvsI6UlPtY-Bw9ey3j6PM6M_uztgR7r2rG79AY5tuQvVJjjB2IxO-HSc7Lm_mdGEC4WzeZVw1_N-UPX-Bebd5ZN25Q6e37I50tCUo9P6YaQKZpNKLrdyYHCidsPoWSbxnIixpXRxQs7-SecWPiMdIqqtlWNGXKArf_V8XcOhtjvCTKnEAQREO1dYF6Qax0ByY4vokWIGLnn1hry-_u8x66CabJviHAlshvMt5wdNtylNwEJwZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ9eDXeP3UOLrhEYb8tKYlqbNY1uO4iuKMBIGeVn-ra4yJGkhCTjeqZle7nR-NSEvPD_Egl37A5fJtsnf0mdYf8U3cO2emZGAXD4TidmJKF-GNA9RvUNZ3a8Vr2f8geca0h3E1H9TKafXWeMXjBfpYPbALr8jePUUM14Uwvdb0U40-iG6z8OmUZymZoL2y6N23luyTdb4in2MkkLN9AZUiDf_IxGqxE2Df9yZJgEkU6so9cDtBfXtbCAT8VR4R7BGQqXcqvzEHeejf0hvMFs2ZAfNPn-eUAFpOME-K5-fQojMePZMZKanl9ZZJndhaOEJNpclxwU2LKZuBTQVzxaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYgQx7EDRQOAQGODVvKBEUCE1HZfegjEoFwGNolPhoUB6yJPxp-nxvKOImgDE1oEV-oqgrjld_9wQXPirb_nS52ErGSGgMasCuPtvskhoE7uQfpSHvrIKeT9apMmkHWhF4xkztLwxDm0pf1zgmXXYvCwrhijhUVGPaE8TAc0Iv0s4Tkl8Kp6qYX8VTWtvYQjq1heCWeHXrwmFLvRbsaoJRh5WcbvXqjK0NwsEzLZEVBPOJonEwZujYM8dKHH1X_tPCnCoxQgDoVNx-HHuU39ANpWyDCaZL4cHvkLU9FPkjoAvjPQcGQzYPZC6co_tPRxSVsY4RFuLfxoupqPvKDfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5ltOmhYqPYUnjLC750k2de37weKDKJyuM-EIvzEnDwJNTCJGtv4-IqpfpbHpH_cDuuNdDErdW6JrsKLzBgXZ2gkj6sJ26D2-9TvdhydqJLqvljS-jxTXvW_JBQcvtWwfmenOrxTLZzbJ_2bjkZYdrp9baFAxOcMxEQWl18uaiAUUZ8MJmQfiTjSQpMWTcSspr_VdZO0lZBa6eMNsh4D6j9fpP8CUzn6XzRihjgfIjYqYe3KxCY9R6rvZMyVrEponU9tWmJLElW9I7deL9jKvOeHmIHZxj3zr1nRnlmX2M3oemmBV__BwuMq0OjA0Dv_UhMjsf-6yerI5pDq5u3ovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quHQrYxa8-3slwu_IpU_m50PO_pkcF39ba_eZu0vEF1tlIeMpR6a4MOSYTRO6kWuSiAsF49mGhTAubpY20PppkXLIaUYZOvt0QiDTMZgGr_hCvP6ce3Xrm6EdtbSxKF1Qg0RYh4mo1GIrFaFkXQYkHsP0C7ElX3jIWvzOABNXpTg-Hl1xSEpEOImonW0mHj60pMUIJG-7YEKFi8ikKKk4HbYvYlAomrD7wt_RzNM0xD2mfopGqt1pm_IfO8lu01-EVGpD0TQLvpYsICYj2tLcu0PdX2rZ4u_-Jtw8u-KCLRpFCbMLUQsUs_BEPuw14Jjaf-Jj6mxGKuef7YrfOXRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVrrqPUiJBahaN-JdOhurVYSBtaZ3chOrFbvzgUS2aX3ybgGpk26wbPGGLaMnXhAGr3Bcnxgx2x5briTWuPBlk9eBJ1cd8F4IP4CoF6bKuAnZ7u5xKcc5UWIKswdwPAOm8-CWiPx9jsMgdLlRy_9CmYovlgAiAxFJdQPYOiqJbEPxrDR334y8pJY1yHFUnr9jTgQfwVgcVQkKhhAVgAPQZgdMlqpZhdYBDq9AeZHpeDwcpcS_O29IR-of53HAXPKpBVAVXYRMKf4Q8n4AmGPHeb9GSB9lTsYpHTSPF-PqfIDI7CZrVN1-RWASTYC-0JoDdSEDPPFEVYZ0a5CxZdH6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt5u5ns8POyQAC_EBnJfpBL0ov2j9JkgyTkD9FGS_UE4izmxa08ST73eELs9gHMDfLBkiMj82JLmS1KEeeQ20vPbZVtcrX4_HuO8jiG88DZ5R4YlyB5ZQw5h8Bj3f1kyMXbhQWCk3JfHzuqAJfF8udf6rZ73dbIxfyBjj_SIfFP8-UWekf_nh8pzk3UeI__z4fnjKCylKUaaBT8HiroMRMf6OOWIYb4UB4s6apoMffgJTHPAy3qHKelxNO3-TFfuiHQuznlcovB3Orkt50GOKk4qPbl3kkfvIxQzoXSq_lS8ni99yNkoOxU_M24xNjhbhsrYUQxOmlg88Ng5JtDBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
