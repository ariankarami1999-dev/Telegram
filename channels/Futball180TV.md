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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 540K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پایان نیمه اول
آلمان 3 - کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/93009" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/93008" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گلللل سوم برای آلمان</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/93007" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پنالتی برای آلمان</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/93006" target="_blank">📅 21:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqm59a4aYC7VHPyZP4THkRs8k3-MoXwb-BugWK8GG0llOyJdaXULS3q1ML-VpmwwvntuponDE80f3NUBOuR4JvPrSkm-XEwyCuQH3OZeHQdzvf5o3Se5-fuwscq9dEp_RAx-aDScIC3uMWRG3m62RXDu1yVbVZo4JGskL2AAjpfRhF_RVgezp83WltmICNUpdH13vRCSJKBDNk1Om0-79O_zAkrPwmUu50jSm5QGkUtwNMHWwGzJZdMbncKUP7Tq9t9s7sK6Fv5NSYlJy_UqwBDEkgtszy5VPi9MjsMdj9YNPFyyqy38orpSX4EZTacB6VJpteu523YF30KbC_05hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس رودریگر خوراک میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/93005" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9MafFC4eeL7IcIfQpTbVzp9PYNGWScnAuWzCjcbFAYM1DHvgIXRPqswtym8-sv4DUIkJO-MJtaKti_jxh9a6m0oNQcPa2jyZNI7rSihWFhr2wnXTowAZ3yjY9Z9hANjWkr8Ukxr-bM65gk4lI__tmKDlrwNoWxcDJ-sLFi9OtNPc_YDUMusjmxdyHybvFI3zz-QxXOuN7taWJquu1Cpzwl4MqYML16ezBiAUYaiS2AjKIdFxXRXXXgLMrhRv_4Y6EW9yBrXC9q8F74IR-KGF-Bl8eqUmYtmWBlRyHH_N7RD9djX36nF2R4v9F9WBB_BY_hATa_6lAX6FErYWqWRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سریع ترین گل جام جهانی 2026 تا این لحظه توسط فلیکس انمچا به ثمر رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93004" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل دوم آلمان به کوراسائو توسط اشلوتربرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93002" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcYnpJI2zouUPX5xpmUtiaM7o-B5uv-TeDco5hW0woTOEve0thT7T1Tm6nIs2986j4jZCc71Laalo8A5y-jAyrO2w6QoOtqVFZK7ZowM2T1jiQX1q_xEVmIA2zuxjfsh6QuqN9MrHQZXumvWS7ZqhuRFmt7s3rDtoXmxfYmSyMLtowYsBzC2_VL7PbJrox0BGaV8z_SuEMAAwmO0QjLbnBGio9C1OFQ540Jxu7jsQOlqzW1a40cK1RWNi82U3sr0YPw-OE2t7VMcCqDA4yMhycXA38j-IEJOyeuYeBa2smDmC2duqA_VDZtcHQl_2m5YBDkYI4iO7lRZrB1jSYQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: ‏پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93001" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاو‌ام‌پی فینکس | صرافی ارز دیجیتال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkpu9GRfqFE-cetrgvuwSZkFMgfgj3AYWEUTBlRJEL5sM_EpuwBAJ4AddNGOiuFZTcW52mkNWrFApb0QxA09ZtgPiw_f9BwItHMA98LIa0wFJSGzFxBiTNXw86L3-kyghNIwCXgP9paYdP--vVubs39IZPTFM6islIiz4fjji4dLhodHd60ZIjm4615c0TszTYp6tB7ZUSpBJruVS992nOUoTJ49Nc78SRi70HVCxZ7R0-jw6m0bQ9b9EFbkyl_7buFMmMjy1r6bxd6z8vNBfBHCFOpAwFOLmBMQNQJK9XuaSNBvWePu09ieIPjYwpvmo-hQnQU2dQMNHI0IU8Yx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
تو اوام‌پی فینکسPOOL پول میاره
❗️
🔔
فقط ۱۳ روز دیگه فرصت داری که توی استخرهای تتر، طلا و بیت‌کوین مشارکت کنی و تا سقف ۱۹.۴٪ سود روزشمار ببری!
📣
به صورت نامحدود واریز و برداشت ارز دیجیتال انجام بده و تا سقف ۳۵ میلیون تومان هدیه بازگشت وجه از ما دریافت کن!
💥
وقت رو از دست نده؛ POOL منتظرته
🔗
کسب سود و دریافت هدیه واریز
شبکه‌های اجتماعی دیگه او‌ام‌پی‌ فینکس رو هم دنبال کنید.
💬
اینستاگرام
📹
یوتیوب
💬
ایکس
💬
بله
❤️
@ompfinex</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/93000" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/92999" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWNKf1OTVCUzMIdDN7aQuf9YEjd3In2XbgjfaQkXHM1sNvnjQiIQChxKwYv--ArGtynKWYHDA7JQgF8OU2cWhNMn0sKgE7ENcjlpfiL_1KDcF-o9MHBvhUynnxaX-GEwy4eSk2BY0nZ2CdRFcFF-xTkkMMXz3evQZXfftcytelhtlXgDRXhevdpXJkoZWOZGwnLFR17MPqOqPsjJy4C2hHzp_p5efUw_YtXt-R2ckqL6W8E5rG44dQ9aijvvbAhG10lCINgtba6RH6P4W6US5yNNJh44CHSQZ1i1Mnk_9ZnBK3AJFR-zh4sfUyItLJJJ82tn-7n-15WJmGTn6OZlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/92998" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گللللل آلمان دومی رو زد</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/92997" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آلمان بدجور فشار آورده</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/92996" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چه سوپر سیوی داشت گلر کوراسائو</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/92995" target="_blank">📅 20:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnszHXI0TmsxVRWCiKeEbrtSvka4EvW0R_XziHaI_2wYkt0-c2DxKKY7RMKXtE061JGGmuChkKxTs3Ns-uVmDrEYgWLu4MDDBxzZHhYpql31ti6A11FYZYqXKzp6jsAnT0e_JoLCwRzeP2P54UNyILK_v-QNOfE07BtcYxID4p-vL1BYEOUQz3RqzL2bqrATMopeiuf___3ZghMxFImY5NCER4UxcRwEHJkWs8Uth6mVbACO393A6NlydtyebBUsK59oLXqwrYRb8ZLbbH6YMGkGc-ut9UGLU62ogJ6F2ZYN250LF97Z4yfpUTQJcOwxs1qL5UKqhGl0RDpM27sZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالی دیوانه وار بازیکنای کوراسائو بعد از اولین گل تاریخشون تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/92994" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کولینگ بریک</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/92993" target="_blank">📅 20:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=Whw2ejG7WD1IFP8waS9_5EhBMcNiByUf48ZNaPWG5T7W43NmSeGeYsXJh_g1eCj_YSYNH8Tu1QnV7dmM4drJ5l37FmpDC344YxJD0ofj_q64V8Fz3T5QWvqyz-yZY7iPvbLFVoF9NEtajn4NCbjalokH2t5w8R301060aKQiyFOnjT4FcByz9UaWvkJXHRFncUBSql2NXutDMQi4grx8MNVlZ047n7MoiwChai2Za7mavLtWg1dDdUjnfIdCPPYaqbrcyVmdnN83X647gW0-4ewj5e2GfKFhm0FkytWtzAKiyoy2zDwuPTgDTPHzw2eWw8TRmL6Y4XZZIwB0uNEiXYewwbKjDVexUtRQD8bmMs0tyKONbYQ0UPGkpuVNPzklCyndkObePsnytBxDOTiE6y_LRlBvUVXdTM1f5AmI0IhO3U6OaAfVCH-G42edExRFIv64lrX4UG68t2--EwlxaGZ4yDvl5njEwMQa3ULA9OCj5Emc96BEvrvsdN705SQbfSYDD-EwKy8kfIbVs1oudTvYtSNzS0I6hmiH1B7sFpLdnh-tWPXoMXMV2kt2Fo_f6OZUA7n6FbipYtoRw8p-4Ojp3GOFH-IGocu8ufYUlS65il7PeHiaa5jRc4iL8Aaz0S_NNuqpvdLoMZcvAuUc37xOXl5LhQlf7vFFTurmRCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=Whw2ejG7WD1IFP8waS9_5EhBMcNiByUf48ZNaPWG5T7W43NmSeGeYsXJh_g1eCj_YSYNH8Tu1QnV7dmM4drJ5l37FmpDC344YxJD0ofj_q64V8Fz3T5QWvqyz-yZY7iPvbLFVoF9NEtajn4NCbjalokH2t5w8R301060aKQiyFOnjT4FcByz9UaWvkJXHRFncUBSql2NXutDMQi4grx8MNVlZ047n7MoiwChai2Za7mavLtWg1dDdUjnfIdCPPYaqbrcyVmdnN83X647gW0-4ewj5e2GfKFhm0FkytWtzAKiyoy2zDwuPTgDTPHzw2eWw8TRmL6Y4XZZIwB0uNEiXYewwbKjDVexUtRQD8bmMs0tyKONbYQ0UPGkpuVNPzklCyndkObePsnytBxDOTiE6y_LRlBvUVXdTM1f5AmI0IhO3U6OaAfVCH-G42edExRFIv64lrX4UG68t2--EwlxaGZ4yDvl5njEwMQa3ULA9OCj5Emc96BEvrvsdN705SQbfSYDD-EwKy8kfIbVs1oudTvYtSNzS0I6hmiH1B7sFpLdnh-tWPXoMXMV2kt2Fo_f6OZUA7n6FbipYtoRw8p-4Ojp3GOFH-IGocu8ufYUlS65il7PeHiaa5jRc4iL8Aaz0S_NNuqpvdLoMZcvAuUc37xOXl5LhQlf7vFFTurmRCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول کوراسائو به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92991" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پشمام کوراسائو گل مساوی رو زد</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92990" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl-8qv9OiRL2jUqV3Lt3ux8IN8rM0hoOhIG0RlKAbmlvwuvt0dZD79CnekekmFa76IQreKztPXZME4bWqSkdCFcWDrcQyta5lFb_Z84YckesLNsrp229Oo7I2QuvW7ns4YAjxCIMJA8-KUhbM5TFBK90qY0l79kxpA1zExW5cEw5qOxHr9HvTkmzaK-8qw4zJ1-cDNRTqxVbe2ZMYjBKR-Gbm_Ywon1xnOy6zt3y2HTuvTCaNes0TTdzBEl-OnNT7wuSUuoRU3B1OIm67s4uASGGCcVGz6pbaWCRvrtO6087MDpHrdl-T0ZrwOsGhrxs6iG5SKcAJIJ680LgDMcWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت گرم کردن آلمان چه خوشگله
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92989" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043736f33a.mp4?token=NUBLvuVA-MRM5WdMFs3PKEbcC0A3Qz5osFnVekYseU1lC10GwMmJmly6aUsLGAWpWbLgaWvWC5pvxlQbPc-ldpsFXbuXl4Sx6y1hD1BXKFFWgeUbuw6gpJF8lJlQITdQKpphj6fDaoIketKqZd_5G2zXAxPWd2JW264ziF6wpPk-QfqwRxUF0IBE21CRv5AHQn7qBmEUTWbabCjgrKPBaLUyX9r8tMeWmQsJgVYQwa3d8WyWUAU_9Uc344VaT__UvGYDIqqXi9P1gyVN28SF2pAXSXUGb7SHUDKTUq3-k6NBlRvRGWLOCPy6dRqFMIpKthkidNDqRb23ih5SOQdJLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043736f33a.mp4?token=NUBLvuVA-MRM5WdMFs3PKEbcC0A3Qz5osFnVekYseU1lC10GwMmJmly6aUsLGAWpWbLgaWvWC5pvxlQbPc-ldpsFXbuXl4Sx6y1hD1BXKFFWgeUbuw6gpJF8lJlQITdQKpphj6fDaoIketKqZd_5G2zXAxPWd2JW264ziF6wpPk-QfqwRxUF0IBE21CRv5AHQn7qBmEUTWbabCjgrKPBaLUyX9r8tMeWmQsJgVYQwa3d8WyWUAU_9Uc344VaT__UvGYDIqqXi9P1gyVN28SF2pAXSXUGb7SHUDKTUq3-k6NBlRvRGWLOCPy6dRqFMIpKthkidNDqRb23ih5SOQdJLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید : میخوام تو جام جهانی 2030 بازی کنم
نازاریو : 50 سال تمرین نیاز داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92988" target="_blank">📅 20:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=cw4ltbn3JOJIRJFTnng6EycsDCvELp7kZtvdJu44-6MucF7P4r1ZRcYXdHOqeakyhRwKy8fV33bgcrVpcB5WiHGpa9s_2_zpW3wc4HMet4qyJV1jYnoczSjM75OdoPglR0qmWS9i1BsjeTToJmueWpZm1T__sl7p3bXME67RKDjil2dMIWTjWK-ZWP0f4P-e2QugD3jjt2moDoH0QMpJ3DVnxRD6K0idYiCw7aJtFoc40Z8lpyBtkV_obcX33y35S9O5_h5RvELs7PZCyHcmJJoXcgfHG4D48UVrkeslnW9V_9eawwSgjrGpEHd7U4U9Zh__5KUdtHmlWaOlPyaKIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=cw4ltbn3JOJIRJFTnng6EycsDCvELp7kZtvdJu44-6MucF7P4r1ZRcYXdHOqeakyhRwKy8fV33bgcrVpcB5WiHGpa9s_2_zpW3wc4HMet4qyJV1jYnoczSjM75OdoPglR0qmWS9i1BsjeTToJmueWpZm1T__sl7p3bXME67RKDjil2dMIWTjWK-ZWP0f4P-e2QugD3jjt2moDoH0QMpJ3DVnxRD6K0idYiCw7aJtFoc40Z8lpyBtkV_obcX33y35S9O5_h5RvELs7PZCyHcmJJoXcgfHG4D48UVrkeslnW9V_9eawwSgjrGpEHd7U4U9Zh__5KUdtHmlWaOlPyaKIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند این روز های اینستاگرام از اعلام ترکیب تیم های جام جهانی و حالا ورژن ایرانیش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/92987" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn8unF_jvo1Sj4yuL-E_2FARdkR3vVFNTR2QJfGt3PKWwK1oxvT0WNhyeEHBwjw_hokgu_ej2jCBeR6zn1EEiQh9g_w9xOx_Jmf32-ywHftcNbxOsD5e83FLt9dgzsb6i0zKX3QwmVAjAKgmcON_xcQERS6Lx2JZVg3gNCZRMFMz4EfxZGJxtsBykS1ATlqbDTqu9zTLCBr_bdwdFPsQ-KBQIiA-GGAYtQtPhcuYofQ8d3Y0RBuhLVTcNue3pbfb94DexPk1GcD0r6a_Vm-WKBFbyEe6RDjnWeZO8Y_ag8-eomZStXZYAveaCflitQZoMCF0ur7jvjJGUbxU-EwUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
برو ثبت‌نام کن، تو مسابقه شرکت کن و ۲۰۰ میلیون تومان ببر!
⏰
هر شب ساعت ۲۱
🎁
جایزه ۲۰۰ میلیون تومان بدون قرعه‌کشی
🔴
ویژه هواداران پرسپولیس
شاید امشب نوبت تو باشه!
اینجا شرکت کن:
📍
zaya.link/p4irm
#پرسپولیس
#ردکیو
#۲۰۰میلیون
#جایزه_نقدی
#RedQ</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/92986" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کوراسائو کلا تحت جو جام‌جهانی قرار گرفته و همش توپ لو میده</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/92985" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQDocCiL2F8ygK_ljjhP_YMeC3P6f1-mlPg8BPtGaKNVEz8_IxcdpZlUy86jUmQWw8JhdIj_lz_u_UqoDxHnkSZpBRAWCTkX60W46kGpuX-XUm8mBcVdU6mqqdvspdsIRDED0GWkEhFCTyqsSf7MigyCHxTqd8gkRLvoXY-9AIreqaeDT49T7rRL6EUKn6phxuVSqDo_P7J_lhcVzXiabapd-zCki8N6pNd8KjoRv6he3IazT1Ch8JdxYFsNLh5jNH449eFtKiXFuMwxP7id8dFgInZNT0m1YKSfa7C73CTY8qf0CnSckWVW3t0zptL10GRDVkB0AHixXg8n2GddDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غنا؟
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/92984" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آلمان می‌رفت گل دوم رو بزنه</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/92983" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=ZnQx7-KXBNMT8F2WX-PFfY-apVlSxTvt5fPaqoMdtUzvr3CgeTeRj7d8955rBGVKHZZdprqc1NCizkWwPgkNYDMAlti_H2iWfi3gqDRqXmpmX0hhG5ZbkvNfUvdcf0L0Gly5oeNyq3QS3VGncCjPlSJRs3b3s-yKw9bNO5J6wG2nNQSRhMdJO1nYcGRoHEal_cWpFrQjlfdENqUYgg91dZqSy1Uh_Rgo6WpqC7i-Bnvq1dmykkC5fVx8GJcA1cNpuQapa56IBduXWLffA60Yna1hE2fYIrxk8IAVX1QkoGCIVEb9_u8pXLJteBYx7URUAH6Q590_d2UeRJhPHnYIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=ZnQx7-KXBNMT8F2WX-PFfY-apVlSxTvt5fPaqoMdtUzvr3CgeTeRj7d8955rBGVKHZZdprqc1NCizkWwPgkNYDMAlti_H2iWfi3gqDRqXmpmX0hhG5ZbkvNfUvdcf0L0Gly5oeNyq3QS3VGncCjPlSJRs3b3s-yKw9bNO5J6wG2nNQSRhMdJO1nYcGRoHEal_cWpFrQjlfdENqUYgg91dZqSy1Uh_Rgo6WpqC7i-Bnvq1dmykkC5fVx8GJcA1cNpuQapa56IBduXWLffA60Yna1hE2fYIrxk8IAVX1QkoGCIVEb9_u8pXLJteBYx7URUAH6Q590_d2UeRJhPHnYIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به کوراسائو توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92982" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گللللل آلمان اولی رو زد</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/92981" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آلمانننننن دقیقهههههه ۵ زدددددد</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92980" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گگگگگگلگل</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/92979" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTFQTcikpJLgqOvQGb3kewbU89Z81BHr8MvKQ2PkY-4uZvtKuqKVC5Cvuf_i2xD_xkA-W3r4iX5XRl3xKzP58LOPuldAjhdpBx2shNv1LQIrks6DQFE5tU25IZ8kWDdFTfumYRR-lCY-yREh1hectVpI5jG8cxGMQ4DJIELdpJvLESM0OcACrq1yBXn00tWbUQKQsDtj4wWk7g-k2xVncEUgwwfOTWniqxHLtD_XPDq4L6wwqJN4bVuMnrjwgnzX5Q8KqsyaUrh5yfIsPyYJAcCQ3DBgAx1CIPzDJ2-xGagiIgggZODjztEc0S7HKSle7WSR3DyGav3SYKY6f6rKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
: شبکه ESPN آرژانتین: مذاکرات وکلای انزو با رئال‌مادرید از یکماه پیش تا الان درحال پیگیریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92976" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کم‌کم بریم سراغ بازی آلماننننن و کوراسائو</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/92975" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPN8SBU0QLoYOJul37B1ELPc3V1Fr-4RKYuGVnVK9phxm7z6JBZeJbSHkpxa8gmwBKTRIzeH9VkKFicI1nK7mV_ufjQizGNG1Y98Zj2eNHdCynbaaLUD07YH9MyNHSjaTHr6fEu0N-yvkvTxbohapYkyVbP4gLt_BAubpi6BTv2gP3lPH5NiFJyuiJlgKbYrwASytEZkiedrB5N1VSHt0BIpEaMwQQy_szrbSRU7O_TX2amquWzfytEwJMIS6JRY5t0kPm-eneFin8YX3EobE4TnJccLw8tbgFy5-Aic8j0ux4BlTaFG0nWM5TAXJxyeWWgeyN1c--yNAamR617nIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید یاسین چوکو محافظ مسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92974" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92973">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn9sorH0eQqhToGqJxANwOxKq-mPligjq8QcAK-J6B4s_cxXGyhCEmd7cTDP9BzNyFBTkP2-1JO3GYhulzHP8m4rVELy1Lzk-ete9_HAR22BJyv4RMF92jdGF6I9Fzcdd4TjF52M7GiZPNKbWL4dCLd8CbBM_iLKfujBVwJF9x8-3ayaPHIV4JguibJL7167O6i1pNTe3x8Y_U0MnhfX5FVkMEjORX2o4HavRwlyIatH8prM4c1cIpjR69JwpCydRRwCLfhtzQTPnxoWAwyyxGBm3p7neyHWH4GEMvcUTCJKgZglMtIt8E_6EwS0xWaQsz3QAS2YoX8vp1MrFX4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین تعداد فینالیست شدن تیم های ملی
🇳🇱
هلند ۳ بار فینال رفته ولی قهرمان نشده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/92973" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQsqoH4sd-kdEhbqhtNrAOqJ6eOuQjnbyULBI2xhGv1M4I70YCJ3oZVEifT4SqOD_0ZvbJY5K9t0vnm5PFXgpuV25N0kdamb1pTb4ErCN7exY7iyu_WEzIFeQ8vPqMr26KXKsbvgfskw5Qy7JhfwK-UXHx9TDhP0B9l8BBPmCxnzj9XhMbWsv63c7wGj-kIy_fkMd2zYOtqkZloHNaRN4uGNmnjpRX3QmkNMe8WeM4RWpl8nKXQcR6NIYUHXZUTBl--aexymxsuqNrtJOj6uxGX2I3wHMix6O6TRCer1W7zgFOkE2flY67TZlxWnO0quqyH1Zb9ceww_K1-NLCu4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد پدرو پورو ستاره اسپانیایی با تاتنهام به مدت طولانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/92971" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfrFIVgKY-hB5IlJwPFPhTKVhigOuDx-pw1iWXnBdZ1HIyuFpsK0_dq5ovpy9mv2-WqY04_qISnNW3ApEJvaDQrH6w7OlnSRBGnIiixqMNdMMIpYyfiU03U9OeH_aoKyz0QysSTRi6REpfG6Nt2w05nNmCG-0elGbd2rgswYn5g14dXNgON6GQ1h7045sXZ8w0v_wmOePgWfnJps4u0cPp2ob_8WKMcKKu0A1bopuDbZi9ztcfE7FwO0hTD99wYn2ZPydJKbE5WNhrL0eIYEBm1emQ6rUY57D64OWJhZh6dK05nJo6mfD_gu_YEKCMTD8xU9iJgiaHhSyNu0CEGL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/92970" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyCUaUaXfFl0DjdzDVrkOscfMjAhbXVQFJdzncaLfncs6Ns1dLIbQKP0U5kPWvMt1BIpZoKUF0y4E_uEMoiKORt8SldBA4tn7z4HLu6W-Lc8k96lkMbVnIoGQXPaVBMqIK4IqYM0v5eycPwhOb3ZDLip6b_4tsP1dRbMWQTVv1q4_eG7FiJL9C_jxBOUiyVwF8v5iKQQzJ1nPCdy7pKkRPpIU7sHthg3R_zBoDy9qBjKuGyw_OzryJSph4hTyWP84x_IjHvIXGGiEynexxxje-Z0pXcBkrcffNICKdsgioCJEjZmkH3xPCCTIzAp-GzBMQtqQP3bgNxhX4xxylbr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: نقل‌وانتقالات رئال‌مادرید هنوز ادامه داره. منتظر اخبار جذاب باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92969" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWQr2W5MfcGHyA_WVcWUZOGcOSsphSk35FoAVp_7h7jTYwlZvxZevPwL7eYkycarO8VVUkmFPPxaA8pi-Anqfgs0PWObQdDYsMmp-ky7jb_W21ECwn--JJw9orTS5fdfBg_ZaRMwscHxUgCVVeWT5z4dMlnTKGLBuCsQVEWIVSi9DhgJVP3HlQzrGxqhDyiKDmQI9wd5aQBai7xDZzSXDhH71kH259uGVLI5_FEsEzBUAJqugaEbD3st5H-hmolZd2xeFFgGhju0uVVYuzZcQoqg_iFVLmSkDnMzrofystwge7Nu4NYc-_xaWPcBZPbiA5rnY28accTMtWoD0ElL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
سامی خدیرا دستیار ژوزه مورینیو در رئال مادرید خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92968" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnHAYLKs4HvuYGuIi7lP8yfPvzgr6wzIBGEFYKFSAPsjnJAbnd0b6DNkomfu43mJPG2mrja5BOHHLFHGYKpMybtup9wFNkGJUEI25SkS7Zcx0XBFpjWdrQIz2mh2Zu6RKpsQtQdnUfgrpnuwez_sy7C03waYIZsDoQZkW-DggBH0KCM-zLklh4zNGbx24rnPBJowDRYKNC_xLyXGDgvjESkhBNgxREwu8ALiTn8_WAZ7x8ktWsr1MSlBdw8s3S2Zoj_zHWGfK-Cwil2mIOKNDt7vCGwv3y8At6cTYcTCge2XjB0v0D9l0Z0w9WJKBLXQNCtmOr2h5w9GL5pS8YePOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4p1UGIPwCPs4fMtr9_31PtrRjvbgbip-EgRsccFPHDXxW8JijftPU1ORzYOX0s8CNVvOJxtfVDqSE4wGBb9sfVZ3WFHt4D5WYa3fgqcUFxcfRdnB62hkOvtlhriuAiuzG9VpjlidATEmhBdq4fS0fzPhp63uv4FTBxsP8L4-oCWsXv1fZqfxrYpq2N60W_g_PCTf_jXZSP79OxcFn8gczunvWqTcEr2K7_HxUMvej0BHxvCOYjgg71dxBnOaQKJfYKU33pX5GXEhehoAz6QpG4B-TqH20hANo_4JATdMMI12HNPqz9odIuCPPEj-b4Hb8Jr4RlooHdNEHJW-zLWSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
حضور توماس مولر و شواین اشتایگر در ورزشگاه قبل از شروع بازی آلمان و کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92966" target="_blank">📅 20:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92965" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUP0xbHw7OIpsAYbrcc6sYqRDql5A4-_5lBqMl-Nc0y_5WyfGQCgFojgkDq7yelPNZCa7ENHZFRmzKffSw7UxXJkig0K5X3_b4rnLTVAvG6nDJkg42choGiG1quMK9y4cbtvshNQKdVtADe2XWb43wogEFZOyGayMUPJ1lAQ0uGONDFzav3qeo3T70oXD6cdRDj9SJzQKjWW679ko-JbjljdXEAtnohpPPAKrH6_r975lkltYL_vgRnZKR_JcNaS4jxqJm5YiPyyKJ4eWnukODt7z91FU9QEcEAr9PkvXZLoTw61UCxaB_3ogQqBv5omdP0rXNToACGt-eJ0hJwXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
رومانو: بعد حضور کوناته و داشتن رودیگر‌ و هویسن، رئال‌مادرید علاقه‌مند به کالافیوری نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92964" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUp_ughnUmQ6LXcfbe0sXH_viZbI6pSPh8BtrFn-xsMWI5_OiM6QPYQdU5190k1GHIU-oge6ifzdlUJbE1OCDD5rU2be5KKGht6UJxFYJL6UciUdfPx7BcimOnAuRC2MD04UfqyXrVjVpH8n4bwk0sRDzF0T9WIuCwz8KtWOAeQN8Lssf-l59UG_hwrfqoecloiyVMWmcxXO3wfn22Yt1SToK2qGj6SW-Z9rdDRNMSW2X4VqN7fNdWGnRHdVz8IXFJhqIIdJ0cGmdBsvm9BU0lxxMvzeKk0LbPGgR4vhbC_l3vufCNjZTT-6ktMlomNwBH2oYVRcjKLlY68qb-qhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام جهانی رو کامل و 4K ببین!
🏆
⚽️
خرید مستقیم اشتراک ESPN ، BEINsport و...
برای داشتن بهترین کیفیت و گزارشگر اصلی
🔥
با اکانت پی‌پل کایا
✅
✅
✅
میتونی با این اکانت چی داشته باشی
⁉️
🔹
اشتراک شبکه‌های ورزشی
🔹
اکانت‌های PRO اپ‌های مختلف
🔹
خرید از تمام سایت‌های خارجی
🔹
و هر پرداخت ارزی که فکرشو بکنی
چرا اکانت PayPal کایا
⁉️
چون این ویژگی‌ها رو داره:
💰
حساب بانکی متصل
💰
هویت شخصی
💰
متصل به ویزا کارت و مستر کارت
💰
ساخت کشورهای برتر
اطلاعات بیشتر و فعالسازی اکانت
👇🏻
🔥
doo.st/FIFApay
doo.st/FIFApay
doo.st/FIFApay</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92963" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=mmO6iCxZbJyjzEL5339MqrlgJ6LlDEcT9GkqQbRZJ2i6pGgLa183gCK6dAQP0jVPIyj-rvxcOXspQFq4TlF_VlQ-9erAyVcu7777Naed2fRX3ub0KjDFiyW5GYBoRKjgas07HBk5CaRDNmALk6GuaiIAiyoXWZmhyyUuJI-SGFEfgi32VwlG2gLmBn0olyp_4lRSQNI17Gcb540Oe1fQmPFcWa9N8MiQq-qV15LSGlILxP3QuE9smXfMLMcwSJr-mqlScvnCRe3ozzjRuYJ3Juf5x7EB82_iNcCAshb0L7Y87Rug1KcLXNd-WV6u1Cc6aA-1JhubrIrtFLsGjLH6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=mmO6iCxZbJyjzEL5339MqrlgJ6LlDEcT9GkqQbRZJ2i6pGgLa183gCK6dAQP0jVPIyj-rvxcOXspQFq4TlF_VlQ-9erAyVcu7777Naed2fRX3ub0KjDFiyW5GYBoRKjgas07HBk5CaRDNmALk6GuaiIAiyoXWZmhyyUuJI-SGFEfgi32VwlG2gLmBn0olyp_4lRSQNI17Gcb540Oe1fQmPFcWa9N8MiQq-qV15LSGlILxP3QuE9smXfMLMcwSJr-mqlScvnCRe3ozzjRuYJ3Juf5x7EB82_iNcCAshb0L7Y87Rug1KcLXNd-WV6u1Cc6aA-1JhubrIrtFLsGjLH6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92961" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmXr-PQLUK-2YdNWgnJd1_YqlMoRE1-iYXY0ufNjxoX2A1NlMmxCH6KLjQzMeNbZvuQQMWAvlzI-EOkAk9EysXvNMm07pMQ7EsME2zuD8My1jo9P2MKwe8KRbKeFlfVOQf4r_1_Khs5Tt8Trfhf8vnArs9IzKEN2BWJWrUrYEDTRexZQrZi0IvG1hMrE_qXym5i9MB4QQvnSYTo69_ElGm64lqEIdPUJOgO509Gor_478pRMZkXGoVOSH-fOTppPM0iAATOPp2hcubKwgd81165JbLLlB2Iriyl6CNanKCrYhs8zvcc0Vv66Qp4dQuEI6AArCkFmW9SdSxzPDnITsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92959" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خریدای رئال بجا اینکه سر و صدا کنن کاملا کاربردی و متناسب با سبک نسبتا دفاعی مورینیو هست. پرز ظاهرا سر عقل اومده و نمیخواد پولاشو به کص گاو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92958" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پایان ست چهارم والیبال با برتری ایران
🇧🇪
بلژیک 2 | 17
🇮🇷
ایران 2 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/92957" target="_blank">📅 19:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">كوناته ۲۷ ساله است. کوکوریا ۲۷ ساله است. دومفریس ۳۰ ساله است. سیلوا ۳۲ ساله است.
❌
خبری از جوانگرایی برای مورینیو نبود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92956" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92954" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92953" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnDo1R4GCViw1aVPB6M5SXyMMEnr_Wj9CBGPbTBQGsgxLxBHffIitEyXr3sALKfzhfNAIfWgyPiI7nwbroA7Agw6nPYwYn_z9LO8TJNinRh6D_Y1jGd5Rp6iMx3z2MxGFOwWGYCjPyhxQ9gfkKbMDcY4Mwa6yQ0bwp3KvsRr-wwtPjvHK6S-XFJyFie-7tT50dO0Rmjz4ExYa-Ga8Hq4sh522jHOSij82zWWL2kIn8FOVQbS8e0XiPGz7oex1Y3PNXEruf3y3J9xu9nBQKsdVkZ2yFw_esxgAPGmBwM8TfYoP0eaO2G7SfSZWqmY9tso4PHRWPEPT3M74U8ndIJtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:
• ابراهیما کوناته.
• دینزل دومفریس.
• برناردو سیلوا.
• مارک کوکوریا.
پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92952" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/92951" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSH5d0YUOlQv9wD4QbuVdR3iuUTqHrmIHuJ7C5bLNL9eeiU8rlxhIy7J3us1UIz0bR-VESnrtJAuOKGbrzxjEXk9hBd3pHbvOiNbPowPEhIsttdbz68gx7s3Xze1qoA6b0JNcPZ807NZn455-k4AlStR7HFfmqcnZKZ3VgobNseP4-wGGppG57QefBTzSfK8-stQb0N3Ry1W7Ziy5k04GVBCj9vHNh5uknmlABvY2iKK6piwRg0MWlZ92pNc8Yf0JP8HziJ49jlW4Oth4ualk6P-nreYk-nYvBMTZouw_HC-cFMR09HPnNCh5TBog654Uie0NZwCA66z6YjQHXYgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک کوکوریا، بازیکن جدید رئال مادرید، یکی از پرورش یافته های لاماسیا است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92950" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCPTu3f3pPy7EcLLeHTbHYTyH6EYnNc3FqyVE0jW1gJGheHKbnH7psboo15gZpXgdwo9evqo1CbypGbRtsh_qyEEF5hTFrZYorvRyJ4m7u82mp4MXhB4huqIxZlm-zefypBJ7CQPsIS6A6TG_aNdzgBAf37ByBo6xIKL1y8JRj54lDZlLVjM5g5h8PdTyqZ6PJg_FdrxnmHCoIT0_iJUYthhIxrq2U6Zi42_-dP2PA8KB1x3nNqD4BJb1OmUMT1V8-Gkc_nfZi7DnfkrhCE7YENPjrBRBSrBrjOD3YfwvrYEUog1paMYZWlvDc1zv-Xng61Q-VtnV4_ExfEthSxF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92949" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilyTd27xxuHWdQXYQehXiPKCFMqD2geCBt39HbEQWcxyTjweOc9vUdqdNgB7inki2q5niujNuKozbCAXqFcr2fNbPhZmHER2oG0ZjZ1R6XJr8Ai8maJGCnDieLLd1bA8vYgz459RcEhAo4seDvXwITNI8DpfGkS5iOvdhQ2F4BWbzpZHEaWoJUrKgteby-4YaT1s4Obh_WSJZ4SSIXo3DYNpiN2cxpukP56IpDISyLzgqURAZl2FwqkYBXppRQ_OzHkU8WRlY5DUnB8cz-uQ-w5XsWezO9p_XgtPSKjMu67DD0H09KgVD_REZVnYb7m9b_2k-lPvlHga_j_Hmo9Bcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد آلمان:
بایرن مونیخ به دنبال تمدید قرارداد با مایکل اولیسه تا سال 2031 است. دستمزد اولیسه دو برابر خواهد شد و بالاترین دستمزد باشگاه خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/92948" target="_blank">📅 19:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پایان ست سوم والیبال با برتری ایران
🇧🇪
بلژیک 2 | 23
🇮🇷
ایران 1 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92947" target="_blank">📅 19:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92946" target="_blank">📅 19:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92945" target="_blank">📅 19:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92944" target="_blank">📅 19:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc2oIDK6VgpbO-PukMLRQy5sdrA21i_UASIpZPD6e74J9xCssh80T-DInlu3oM8L2iewLobXB45KpPj-AHPjbMPqZgnPV3TevigQ-XfZORP9gklFOeA6m8anA4G6heRbsYdUoW2XzLgV1n3Y5mU8G1BO3oHGPm_XtBqR9xrx1VEF2SpUpeWXlmCwKJyWzSMIAng_EOCrNqFnfohZftDjbUQWcqsU2PIjmT0xqI7WbfKzpUGggFwA50BLoBLeL12PVZcQa2EgtHl2bRMjWLoh-HOG66ZmIhmF9oEkEEndERKd5A4C4mUree93t2vSxnNEmZverSJrZ7y6Ifs-uXbdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:
کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92943" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgPTGwutMXora-7K6GWJGyQVyFrn9FiGwVuuoISkiTkOCvpv1vaY-aBYMVsmA-gyeHD6d5nKR51nf3OZCeO4k0kjsFYBilbDs6O6-Q_ejPLEGAxzPMWyA6Vzz3tQL2Q6ndmC9TM4q_Sz08587yo3Y_LUJlYxkEbmmZQI8SZ2fRaH8hCcdArWYVANsB8hB8Fjr4GBX1QGg3NHiIIHaxgMZ1XAdROcMbRA6e4PV_RCZbDUT97S8fVZuPEIi6ZbVnwH56BifUcZc4AVP4dBFV16doZik9BtSQgqM7F3FnwLCNTKsBOr_2oNt14G7xf-Cnv2kQHxHTAjHdqrFWRckm7loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترکیب آلمان مقابل کوراسائو؛ ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92942" target="_blank">📅 19:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eERVlsZmv6YWv7XZE9NFA0NJNlBPJoVMVLPqNLKeeQTNLCVA1KBPEHw8nGIZxsQw44eT3bpRoOjjvDY1s2frzE5_2CH3NPl53vHHhAg0GJ8mgYzKHJLcM3iDTV9YLe41qOQf5TlPeCYd62XaL_TBRxcZaWKDH-cxc4eaDJ_3d3--eWZZb5NDDZKhNSXQf6GisWa_sQPsoaEe7GVt--AsdijMfQzizUViap4TW9IdgAuTXUy_7E9-Jsiylegp5QbFpnlozUARXKRTbKBd16Wq2oMRv46czqHeTZMGdfuzjJ7XlnuACysb9qwawaF9LMtALTHmd9Kka3UewKQsnNci6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترکیب آلمان مقابل کوراسائو؛ ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92941" target="_blank">📅 19:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پایان ست دوم والیبال
🇧🇪
بلژیک
2⃣
| 25
😐
🇮🇷
ایران
0⃣
| 22 این ست اختلاف ۳ امتیازی داشتیم و باختیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92940" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfiSNIFA8JsW_z28KuD2HdoGXC0zmwfduBtEeJM0JcNNFYL2-8cWtt8f_ul097nn_5upC0qc2j6ZCFYojANm29qO1wdBkwwHUtHLEt1toTLBqGJDa8qavu2ssChgy3FxoDeAxp4RDlw93U6LeSXoTyq3qYfE41wFeeTaPJSAC7EElJ__TWLd_VN8y8WVcwSzgO3QdECnfPEsITFtqEHQDzdD_Sz70unWhn8is3ZFQDKy1kIopt5T4Iy8zcdECSJbsJhMFmDqcKgNqI1-FkAcAd8Ck0vfm-U6JJ6UP230z6nQPT0VQRZwttT4ngXiiUIa4OyQGMwiliBc0q3KUx8j9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تایمز:
باشگاه آرسنال مذاکرات خودش رو با ایوب بوعدی آغاز کرد! ارزش بوعدی قبل از جام جهانی ۵۰ میلیون یورو بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92938" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_LWisEhzHW5CL7G9q96epqPGBnmRsL1ZPW-VypfIM7QjMPTde-SOdV-qRFAL73fUHLj4UQjkxQP-sRcd2R9AmFYd1GtzaU0iVarHWNMT9pBvu32gKnkpvtzU1a1L0ZvrY7wo0THSMdUeuO7oftuxYO2FmxS4QjGuWM-q1wWJ49bCUEKrrW6bPleQggjxsCkWFjx4EnZxTgrRaWyb6mupBdYYNl-76959O2qDWS4VwZjyVDE61j4uOzss_RwAd5-cEuR-YwIcic9-J9absqOCHAzYI_rayPIqoJ5GYY5ruMsSAFKfNWvdDH9AZy35PvnmeAxqXfaZliweinzhMO8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه‌های اسپانیایی مدعی شدن که مورینیو از عملکرد کارراس و گارسیا در دفاع چپ رئال‌مادرید رضایت نداره و ممکنه در صورت پیدا شدن گزینه مناسب، این بازیکنان رو در لیست فروش قرار بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92937" target="_blank">📅 18:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
به گفته منابع برزیلی، نیمار فردا به تمرینات گروهی برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/92936" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc034209e5.mp4?token=iGf7CyRHtZ2FhT9s7eh_hr2mWbKq6alPdk_xZNpxmUmFXxCgxt9hLSG_M_e8ZMphKQWym6mfUkQ3bBDZyvP7JbZJnRn_092c4MB07KvG5qp5nGYaOby0MYKewPJEcgan6msHF1Bmd-9EXDrsHkQIba9tsbfW1K85wLjtfkGSQ390nbaGMdTZOtNFe9ivj0Op5byEVBgLn3kBkNJTiEaePLdbRs8RittD8WytORz0XK5Umi7UvA3IJovIVJZvksl-xjwi55N4Y4qWy2ua_VlcpXQZpU-53DyThvyxteLQhUbranEwGFJ8W8R_hlzWJDyvkUJ3Qn1m05gYcvmAd8yC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc034209e5.mp4?token=iGf7CyRHtZ2FhT9s7eh_hr2mWbKq6alPdk_xZNpxmUmFXxCgxt9hLSG_M_e8ZMphKQWym6mfUkQ3bBDZyvP7JbZJnRn_092c4MB07KvG5qp5nGYaOby0MYKewPJEcgan6msHF1Bmd-9EXDrsHkQIba9tsbfW1K85wLjtfkGSQ390nbaGMdTZOtNFe9ivj0Op5byEVBgLn3kBkNJTiEaePLdbRs8RittD8WytORz0XK5Umi7UvA3IJovIVJZvksl-xjwi55N4Y4qWy2ua_VlcpXQZpU-53DyThvyxteLQhUbranEwGFJ8W8R_hlzWJDyvkUJ3Qn1m05gYcvmAd8yC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ولی هواداران آمریکایی جام‌جهانی یچیز خاصین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92935" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پایان ست دوم والیبال
🇧🇪
بلژیک
2⃣
| 25
😐
🇮🇷
ایران
0⃣
| 22
این ست اختلاف ۳ امتیازی داشتیم و باختیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92933" target="_blank">📅 18:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-t-NGtl5D86CnxhNQxIuk2HE-ognbtD2PqnoVbwrFQ0UP-edkfSRnSX_Md5qvphhP-rZyrAiYSe1s-V8e7kNo_fb64cBzOcpm58N2wtWZLfmGKemKSSFCaqsnlJO1uI2VXK4Ki0YGPl0BR0m7dOvaJTIZVDXRBT-esWLqBNmhmwAUyrgiRfcbzRN7vevlqcsm-WyoWBX75nobuIFx8wHCWFtyNTUG3X_tdf03FqPESJWVwq2D2zmSuxoKw7Qceayi_myz5jyi9JHfz6_zyzhAAdEXqU2fY_ykk5rrayTG3cPQ5NqpRkICJgj78T5I3BZPmO9MpvCrBQo-DJJj7kEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووورییی رومانو:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی مطمئن است که به زودی قرارداد یوشکو گوارديول را تمدید خواهد کرد.
🔵
قرارداد جدید تا ژوئن ۲۰۳۲ با حقوق بهبود یافته تمدید خواهد شد و باشگاه معتقد است که این قرارداد تقریباً نهایی شده و منتظر تأیید نهایی است.
🇪🇸
رئال مادرید هفته‌هاست تلاش‌های زیادی انجام می‌دهد، اما اکنون سیتی خوشبین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92932" target="_blank">📅 18:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c11f0246.mp4?token=UAhj4MQ5N_Mmvqg4AL5teo5YFiWPkfK5UrVm9s7tmPzNWd36XWtIeqI4j0uW1zE3U_6Mpn2btWz17FI5YPN4YzzQlzcliiO9rK9FW0aJMaxfATc80AyFh3RUySoEVVqtUodVplelsU0HH-rkiWV45ypqwr5pc7Qm7fa8RFTxf56IRCMbXQzQKERz0YLQ_zDUuVJS8oHM8Rgwno8-4FfyjjTUwE4VRUR17J7yhfRhv7VPWF0TBduTpUA7imigyh7JOFMseMHRDt-AUc2A7FLsDwpE-3ghCjbWCPnPvoBkJmsVM6qnPDBmNP6t-0G2GQ6x3t1ZZPBx-hqAekCwVu7BGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c11f0246.mp4?token=UAhj4MQ5N_Mmvqg4AL5teo5YFiWPkfK5UrVm9s7tmPzNWd36XWtIeqI4j0uW1zE3U_6Mpn2btWz17FI5YPN4YzzQlzcliiO9rK9FW0aJMaxfATc80AyFh3RUySoEVVqtUodVplelsU0HH-rkiWV45ypqwr5pc7Qm7fa8RFTxf56IRCMbXQzQKERz0YLQ_zDUuVJS8oHM8Rgwno8-4FfyjjTUwE4VRUR17J7yhfRhv7VPWF0TBduTpUA7imigyh7JOFMseMHRDt-AUc2A7FLsDwpE-3ghCjbWCPnPvoBkJmsVM6qnPDBmNP6t-0G2GQ6x3t1ZZPBx-hqAekCwVu7BGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
همچنان از بانوان سرزمین با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92931" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇮🇱
فوررییی ارتش اسرائیل:
آماده شلیک از سوی ایران در ساعات آینده هستیم، در حال حاضر تغییری در دستورالعمل‌ها وجود نداره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92930" target="_blank">📅 18:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmNRzMRmejKMyIgr21qBT27sz0WpzhZYi-_kv9FpKRod9Tm8SWWvtPHlJg1gvgDoV8WVaa825S3_uFiMt3MmeHven-rS7dRmRcdLgunw8jw98t6-QInzuHNpY1i2lgbnxzeuk1vaVvAZU2Y_Jz7CVcXXp4j5UOf7I5VfQWZgbYgMAbC8huMWRr83LPzwj3EdG543RIrARX_cIgaWHRUpMM8rkD0BE9ZdLDoz1R-uBWzxFypXywx0nase-a2klthLyK0OB6dUVpw1tNaQXulj06oPscAlOgjIMKj02ycysjBhwg5O3gwlU_yGsYNmzvx5XaKhIm_H2AAEhquVHU0xdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇳🇱
🇯🇵
نمایی از ورزشگاه دیدار ژاپن و هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92929" target="_blank">📅 18:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایان ست اول والیبال
🇧🇪
بلژیک
1⃣
| 25
🇮🇷
ایران
0⃣
| 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/92928" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🙂
‼️
🏆
یه هوادار ایرانی بلند شده رفته تو مکزیک و از خودش ویدیو گرفته. نزدیک بود زیر دست و پا خفه بشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/92927" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgfvCwCvMfA40KWerUu1uJ_yvrRyDt-Uq3zpIvLAoZTC-3Wq9-gphtzbdy4NE3WxSk9u0-nRCPXsETot8IY1Xq3BtKMFn63VetxyXAtM6qM4mZpI3mwQDQi-u7bCOUfBDrt8LcSuL2e4ti1hsQlnw8aAQ66R0v_klXTpsmbfY7P9bSx__EOrsLgUyBCcZj3PHu6sQ9qGx7KI-9ITOa2Siekr9pfbtGXN0vdvPCiGruLpM8tHEyT9Ry55Bqi-82AUCEQye3JpRQYFXx30O9qh5ZA6bJwTqyWIjXnfGqP4DOJLRos4goOcnUwkdo67cbhUSlxh1TjkAcoScAP5jyLKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bab5S1oB9zeV5MM6CnxuY4g38gbbSwJ2z8IFCUS-xxkPJYURBoYRzeMh-ux2GbNpqVbx6qJWhsfm1i0F4PYClsWd0XmRiqP7vq_NR91pKfnyNWag4Hvn8pjcUOItaof5mlvSgihvvuwDJnEpP3v7b4Sqffk9ltlzJrMfQapZko-WfjSayIIQ_1oSDmos0VpXvOHewVOP15YsKi1P1nyjei0H7laItg99mWAjlAlRzCOdfMIBDmCO4v1N7Mj5hNZ5blbPY8v_2syCr-RFxw1JnN1QbCk3sIP44sE0TlRVhUtFKfmy1Wr0f7kJ2VF8BY5UVadHgLa8sjCYFIIGExGHqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا در بارسلونا
⚽️
رافینیا در تیم ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/92925" target="_blank">📅 17:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAKlTkr-6f_IBMv4sOukp12xw2ZFiXz6a3a3EannURN1pYlb2VoJ4U3UBou8GnlKVYv1kGEnzL8PtUmY9toK_no3vlK19VovOsIZQg7K5TTFJQ4518PcuJMvPV5HBpRMGKO6MYy6ir2ey_ptCWggvl1TxD3Xw4c6W4fBiRYt7pgGXEEIdteOCrDJpMbBV9h1HSiqVxEpuCJidDF2D3SpAkAQEIdM6c93etKlLsCIowreDIIRiwUV4frqTK2jZxq0upzcF18RDGgBM8gjrUWLPfTZmX_XsLP7Cb1rRRhD-aNLz5GJS3bsGvwPx4ME22AgkNQIlX5mrR9cdp-jHbpJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🏆
رسانه‌های‌مکزیکی گفتن که یه پدر در مراسم افتتاحیه جام‌جهانی دخترش رو بین جمعیت گم میکنه و با نشون دادن عکس دخترش به مردم سعی داشته پیداش کنه اما تا امروز موفق نشده. ظاهرا احتمال آدم‌ربایی طبق گزارش پلیس مکزیک زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/92924" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbveW6XmyFoYSwRrF4-LP-o6BMNCjnDfIwUD96LNWQWwL7tEPa51F7BzfV7TKbnurlZb7Ajy-KAx6wZo57t4PeDXq-89rmEdRYMDFawWKgbtRrnuop8gaLGho8L8hh7Xk1lhM0cadpCHvwePG1rkT4_Ydr-kDMTyg1L-F4vdhDVIx9XBHn0uXclZmOeZvPOZ_h_8HHgGdNcvOh8jPDiWrj8xYfV6P9N_azkW0zot2YvoirokJu0tg_dQajtpwCqvRWZ7MvWEBcJxYGGh8_VdTFjPPFSZ8VNMx-O7gLrOoDhBm8mWGfyOgWh4PP8SY4HJJpauD1QvCTOeR8L1rPh5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یورگن کلینزمن درباره قهرمان جام جهانی:
اسپانیا تیم مورد علاقه‌ست، اما آنچلوتی برزیل رو قهرمان خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92923" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9y4OK6yN1fVHQLXkRiHDcwRENfJU7a_hpyoIuzT39o5Cdu4brhh1ou6cOdmtDfF3kzBHZTdaBuz_xutHaG7FlBXsKmzHGOCtEyAAIhZftjOxhwLkOWK09o_p2z_q5TGkmPrpyZi8JdJNje3f_6xl399d8bgeiwKhZR0UxtdqaFLrvP1iBgpv3LjqmlTibdGNNZZqagwO1O7-4IObpewGwRdUFxb5TKOi-2WCxW0q3dsx8jHbpxRybuBGLEFFGMXCYRG5YYjSgXX2Y0msEEsQ2VGD1jAaNkRES206oAmWM_Z-q49qUevLrTQCbtO3p6NkBSYewZbV4JWjC7AtvU3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92921" target="_blank">📅 17:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b3d55458.mp4?token=SPGB4JzStTflFKvKwTE_PSWWCokAOWOLQyweKBfuE6WzE_XSdqXn32cHwC0nyreLJE7hcttihU72tpVcm7sx9BuKjPXG4qyM_63_Y8wK1a_0IzmzRKjbAGCk94WKtL20W8nlCnzDTo-YVdUiVY4WK-I76YPbY3cAahYDXRvex7Hp1FTsUYR8foE_4Iqb2yP3rEOs8vZWfEfRq_IxCXB14KWUoeE4QQVFxIjtjLsmCOw5TwoK2Sv8IBTXL-SsGZUILPQPGT_KVQ9hO3vBYGoSsOPsYEqcv5MbgCqQj5VP6YG01nMn9x5EjH1t96oYedXRQ3ZoRGZvcXCqqkQUuBFT_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b3d55458.mp4?token=SPGB4JzStTflFKvKwTE_PSWWCokAOWOLQyweKBfuE6WzE_XSdqXn32cHwC0nyreLJE7hcttihU72tpVcm7sx9BuKjPXG4qyM_63_Y8wK1a_0IzmzRKjbAGCk94WKtL20W8nlCnzDTo-YVdUiVY4WK-I76YPbY3cAahYDXRvex7Hp1FTsUYR8foE_4Iqb2yP3rEOs8vZWfEfRq_IxCXB14KWUoeE4QQVFxIjtjLsmCOw5TwoK2Sv8IBTXL-SsGZUILPQPGT_KVQ9hO3vBYGoSsOPsYEqcv5MbgCqQj5VP6YG01nMn9x5EjH1t96oYedXRQ3ZoRGZvcXCqqkQUuBFT_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف‌طویل عکاسان بازی برزیل برای ثبت‌قاب از نیمار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92920" target="_blank">📅 17:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXtotUCceVUYfSXPrsmXCc92dbNJRsClWKBJYksO486rL9xCqgBlDycIYj1jLESGSwOEYqaKNUuO0fQj7wVdC0DHt2W773jrISJP_LuOlB-ltU_IPBcXbwb1suSt9wFS0w84uEhRHHlKPWOoNARwkpIUV9rM73eSBph9yAtO1kXw-4N7QvS7MoQBfadE06yr5-Hgu7qyrc1sCI4OPVRrPwtmBYq9bRVav9xneup6NvQccaTO50zjfVKdkP7IVEjQI30Jh90RQU48zgOSFlye6pqQF6h-BEDTY4S3Yxaqc-TxgaOBtrczQcdVqfCTLZVPGhB1dHCiVeQqmxRQUFrb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم‌ملی والیبال مقابل بلژیک؛ ساعت 17:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92919" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی بلژیک:
⏺
تو هر بازی ۲ ۳ گل میزنیم و اول صعود میکنیم
🍿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92918" target="_blank">📅 17:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae33cfeb0a.mp4?token=Teg1wDoULCnGN0XZeJ0Fh96K_j5OL2ErTLYKVJrTiNSmdMC2LspQmZAF3zDr6oQ7vBCtU3Q07KN9lEv0UWyRaGyNgtg2Lp-3ua4MP2s3b3N7_H9eL49Wgy1n6p1qX4TXTILIxJZGN_Pu7nbrk19fDjqnfLjGNvi1xpJmtzweuyVNXJI_d8hYD4C_FcGmkY91lm7_0FJvlmhGa5Uye2VK6_UB5kCey4-aTyK62JwX8-ElfTZmKKrAFfsOxWcNbURK9infPQTmwEGPuxzk47pljIj_DWgErIiDotha_FMEPZIMYoUTVuAhdnpCRp3Drz0bLWUcZbS_77FeemwhU5VmIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae33cfeb0a.mp4?token=Teg1wDoULCnGN0XZeJ0Fh96K_j5OL2ErTLYKVJrTiNSmdMC2LspQmZAF3zDr6oQ7vBCtU3Q07KN9lEv0UWyRaGyNgtg2Lp-3ua4MP2s3b3N7_H9eL49Wgy1n6p1qX4TXTILIxJZGN_Pu7nbrk19fDjqnfLjGNvi1xpJmtzweuyVNXJI_d8hYD4C_FcGmkY91lm7_0FJvlmhGa5Uye2VK6_UB5kCey4-aTyK62JwX8-ElfTZmKKrAFfsOxWcNbURK9infPQTmwEGPuxzk47pljIj_DWgErIiDotha_FMEPZIMYoUTVuAhdnpCRp3Drz0bLWUcZbS_77FeemwhU5VmIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇰🇷
هوادار کره‌ای و دوس‌دخترش در مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92917" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c830c9efc.mp4?token=J4nJ1HacuRWoqqRjpaSx4At3jcOIHNA23UKbcWZ-ld6EVyYBvLDOXGHYZJS66DymD9M7E2uAI3zsILgrQPZaC0p96L2ZzS1kXS_niDStls9qrQGAUrYXQ6sBSnKyOwh1VCYm_Yn8bifDH34ewxcD2oyM-2m1Wje0d4LOwEmi5zkkhdnwMNjdxVh2yr5KpeRNAXMBAV8oNh3gZfxyeomFIOeZJe0l4rO6IHkh5kQ5W9yd33PgVbP3hB0xL34fH06T9hDWlAYjGaiGyq3j2rPmP3uBi3VV0ko8rU_y1nGHx_NQ-Mg7LTMsm5R2_5531t-DZQD1wNOyYMsvdIYd86Vuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c830c9efc.mp4?token=J4nJ1HacuRWoqqRjpaSx4At3jcOIHNA23UKbcWZ-ld6EVyYBvLDOXGHYZJS66DymD9M7E2uAI3zsILgrQPZaC0p96L2ZzS1kXS_niDStls9qrQGAUrYXQ6sBSnKyOwh1VCYm_Yn8bifDH34ewxcD2oyM-2m1Wje0d4LOwEmi5zkkhdnwMNjdxVh2yr5KpeRNAXMBAV8oNh3gZfxyeomFIOeZJe0l4rO6IHkh5kQ5W9yd33PgVbP3hB0xL34fH06T9hDWlAYjGaiGyq3j2rPmP3uBi3VV0ko8rU_y1nGHx_NQ-Mg7LTMsm5R2_5531t-DZQD1wNOyYMsvdIYd86Vuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
این‌بخش از برنامه ابوطالب که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92916" target="_blank">📅 16:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7f647c15.mp4?token=kp7XR2soFPxBG65pHrfQIfDW_V-pnL5cRjpwCgYouA_BXB_aLWxUDnq0N6a-h_g0iRsK7gN9tXmYV0vmK2osggp0fiRY-QTdvjko1h2opI1zIirm9dJduf-iIV_OmbnKapH_JfpnZylDkqFzHQBSLo8Nry3JBNzcDlXaEchZAXElRU2SV40rj9NMnpSvS5c3nOiiqnptJE0I4Pjw3G7v7-MySjJSm4w8eWv6M1zSmsXh8eJ0EmDTA5re0dcKy7_toDgIQLaywOcx9w72WCC6hHEE3GCF_k-wQa4DzVoXyoi-5N-6JtwFl8ZGexxCk-sK8cOvU2fT7fGNsrKy9O9qeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7f647c15.mp4?token=kp7XR2soFPxBG65pHrfQIfDW_V-pnL5cRjpwCgYouA_BXB_aLWxUDnq0N6a-h_g0iRsK7gN9tXmYV0vmK2osggp0fiRY-QTdvjko1h2opI1zIirm9dJduf-iIV_OmbnKapH_JfpnZylDkqFzHQBSLo8Nry3JBNzcDlXaEchZAXElRU2SV40rj9NMnpSvS5c3nOiiqnptJE0I4Pjw3G7v7-MySjJSm4w8eWv6M1zSmsXh8eJ0EmDTA5re0dcKy7_toDgIQLaywOcx9w72WCC6hHEE3GCF_k-wQa4DzVoXyoi-5N-6JtwFl8ZGexxCk-sK8cOvU2fT7fGNsrKy9O9qeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیویس رفته توی خیابونای کانادا یه دوری بزنه و با یکی روبرو میشه که کیت کانادا با اسم دیویس رو پوشیده. بعد جالبه وقتی باهاش روبرو شد تخمشم نبود و طرف اصلا نمیدونست دیویس کی هست :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92915" target="_blank">📅 16:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efae1e173c.mp4?token=mmjDQFveeYEI1lRmZm8Y4WZ7ljiaDd-YFIwCltlymq1Koa8uKUd_KkhgQHVqcmOpWynKB5ORrM0qzGe_FzekYtfpr95guswtEV1ya5MrpFJECN8lGhEmO9Vo-ilidKL3f8PjNiUTfVrSsHuZ9Vo_zmmByHe-0ZYjc5PczmznyqcdrY8SieegprXuj80HTGFAON19FVLcD6V-W23nRixx9RFvnF99MtR414JnQNS4Fd77GW4R6Vy1NZJNnBafnv_chS4-3pThGBb6JlI3SThyKG4SSt0xXzrP_7__BiPm69gPz-kK8sNsjlYpSUlE33UrsFXphXSTHsRfAbEVcfx8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efae1e173c.mp4?token=mmjDQFveeYEI1lRmZm8Y4WZ7ljiaDd-YFIwCltlymq1Koa8uKUd_KkhgQHVqcmOpWynKB5ORrM0qzGe_FzekYtfpr95guswtEV1ya5MrpFJECN8lGhEmO9Vo-ilidKL3f8PjNiUTfVrSsHuZ9Vo_zmmByHe-0ZYjc5PczmznyqcdrY8SieegprXuj80HTGFAON19FVLcD6V-W23nRixx9RFvnF99MtR414JnQNS4Fd77GW4R6Vy1NZJNnBafnv_chS4-3pThGBb6JlI3SThyKG4SSt0xXzrP_7__BiPm69gPz-kK8sNsjlYpSUlE33UrsFXphXSTHsRfAbEVcfx8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جام‌جهانی ۲۰۱۸ تا ۲۰۲۶؛ تفاوت از زمین تا آسمان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/92914" target="_blank">📅 16:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فووووری قالیباف: پس از چراغ سبز آمریکا به رژیم برای تجاوز به ضاحیه، سخن گفتن از ادامه مسیر ممکن نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92913" target="_blank">📅 16:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_11qxmLaM7YNPGyxt_4Dc5zXjaQ7D7yoXFmWMbXHSfasnzahnfeHSLDKvo7L8RRsuTUAkQmi78vlcUCfXGzFLzwQ_LvNv9dbt21kTvQGpga-ILf3dtL8S9D61xb4w1AC4Hl8c9OVy_nI8mm0ic3x71T-t5_y-ZglFzfedi7ZSlnF68xEckNDhCax9DMHrheDUFLA7QfG_CjoZluS6Xix8FQen-3_9Dc8JWu2IaE8WiUxs5AyE4dtuzxbxuOgd-3LtpIefd4QtWKHlCxzIqaAwot6wOCOQeEva-yODWPbMWTd2rexXaUlzzTMUd_Z6l9aHVfVfKDeuVUEl0_Y6OGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی که از این بانو شدیدا وایرال شده و همه اعتقاد دارن تا اینجا زیباترین صحنه جام‌جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/92912" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgLxm0DbL97iX2O3NqruuIwa15-HX4AhUdUVUXpUvwE0P0KoIZc_2PFTqIodmF20eBTa9d-AcGkOUUfMdgxgSRTJ5wXtYyJoyT_xqyYaknyc43MW1tu2z5ebtqMtQGsSxyhFWElztuXmT8RpCLDk0N7pldTaNS4XtAhNlz_O-UfzS1Xn2Pph3KBNuNUXfGMH9S7a7UjvPw3ivTrBHewTRHpIvL-JP5eU9jTOSQBU0YNljhqBmbyGzWPiRjIgSmCr5GyCU3lDPM7Cp_OioPVmSW05dqvcPAJMSU_adGjvHYJfkNdc-WhxXaX6y0_yQgNcYmxpC8w2uxxZCpBIwHznDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
تموم بازیکنان پرتغال دستبندی از نخست‌وزیر پرتغال، دریافت کردن که نام دیگو ژوتا و تمام بازیکنان پرتغال در جام جهانی روی آن حک شده است.
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92911" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f746cf4.mp4?token=dxryGLcvhPp-rCvEOUuR22iqiOvjAhGwM5qWrGG_4s0OklD-YzzRl1363vFMy5kvSB7VPaScsALeBHRcnokt2Tu2R7nNvco9SnTt0DeR3lXDTDKwn8fq4B8VXz73TRvsPsvLZW1u5SmjuB3iP8a9j0PbLLv4iK7Ek5317S-WZAib5rYoLVI0Yhq4GhYQ2oNNgSHheLYSW7zvqS4eCOUAOKhdvDLMP1KxNRmbnlNqYqJJE3WxN4LlK04RY0XBS7glXa3ElAFqqmY3XKC1u67Ny75AW6JN1LsMvu5gfB6PG5DMDtxnImVbk0PqophUPj5IqESUO5pDCQ7XyhZMIQB7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f746cf4.mp4?token=dxryGLcvhPp-rCvEOUuR22iqiOvjAhGwM5qWrGG_4s0OklD-YzzRl1363vFMy5kvSB7VPaScsALeBHRcnokt2Tu2R7nNvco9SnTt0DeR3lXDTDKwn8fq4B8VXz73TRvsPsvLZW1u5SmjuB3iP8a9j0PbLLv4iK7Ek5317S-WZAib5rYoLVI0Yhq4GhYQ2oNNgSHheLYSW7zvqS4eCOUAOKhdvDLMP1KxNRmbnlNqYqJJE3WxN4LlK04RY0XBS7glXa3ElAFqqmY3XKC1u67Ny75AW6JN1LsMvu5gfB6PG5DMDtxnImVbk0PqophUPj5IqESUO5pDCQ7XyhZMIQB7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره دردناک و ناراحت کننده کانسلو از مادر و برادرش…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92910" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMsCYu498yGow3TFhlA8t4MlkJ-sotSwqSJFM9y0sBH7YBmMFJlNpe6mhusAtgF_socQtEGnEBQ0KtXsYT5U2LnQj3QF_harUYVz70rxtWcbHqgDJgGjowyuAgvGgmgWe7InzPMXvyFRkjV2oEO4O__nhrV-aCwzaJ8NQ8qly1Y0F-YZ8QNb-jwucCA4NmuycGU8JhyE1NwOF5Uwe1cvjlVEshQZPlRFD1yJX4nNfqJ9ou_D1Y07_ecUSwcgR5fyOK41k5jA_DWfz4SCiYEMcEJgQIRatO6NkiNvJdR6WrgXq70EVDRJl4EPsCMHJvGXWmLjNpeSIKG4JQrFSnOfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایوب بوادی 8 سال پیش، بازی ایران و مراکش‌
حالا اون دیشب تو جام جهانی مقابل برزیل بازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92909" target="_blank">📅 15:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugrsTagSvW2_id964jOqZAqA3lBj0UqsIoJwF6a4FdG6TmJ4fDJO8IXLeBcx1xduLwvH5r83x_WczFprGOrDeKAvjjobCBLu90URhlSrzTICWrYX7Lf7aGR1UCuABsdwjT4x5YdZLVjV7u7qlZC2ZT7FJQ-Mz7dGtg34kFmhunOPMmO9SDeOYzV4GEnyiEWV-pI5rwFJXpowQSW_sBVEvlaK10A0uj9eswekCfmWN1IkVQ9PvaBfGQbrmyStj0Vurjv9OFYlbm2oI7jjUVxSNhUQTD5RK_Ssyy4XNTZd-IZEpqMaRkxMsNyZnE_Bs2eBEv48JiR5w7QQr_E8ACVisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ادعای اسپورت کرواسی:
گوارديول قراردادش را با منچسترسیتی تا سال ۲۰۳۲ تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92908" target="_blank">📅 15:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ماموران امنیتی جام‌جهانی یه لول خاصن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92907" target="_blank">📅 15:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r26IGMYJ0r9yB042oARR2C_el8-8pSmjrKFSKDM5VFjUXI50mu3T3M2ylZpvVUPBDQwOuu1tMVY0ch7htJODWpy7okOVslyIOdhbJWTfq1IeiYaAl5HBOwb3RDcKzPeNsAEzC7OM4Q061y0R609QKbvZx06ay9mN8A9eBk9DJIym8qrrgxI0ThBt5KIbWQN-mD7K4ZiZ7Py_afY5GAhmm3gEHJzh8s542KZPgGcpLDNRnAVHJxjxGg3WHZZan1XwuLv8S142mscJEfk_rf_sHVUqknzetS25YGfsFhQqlJl5KmbgE1Xmfbgo160fMdjCwBNh2u1yGrmNe61pSMvUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkPKD8Lj_OFz6GKr5qXNlSawMzyicvx05w9KBFja9ok1rrNiEfd0W6HSzYR1LqczIR2iDFPb-o2ILEQjsZ7W56y3d1UuwMOwjJ8nB2-x5tcMf58PUUjq9xfAv8-3u8Sw2yE9WiJqRNq6Tp4UpdaDS1WEArJ0nwq9JYOxttmKddIFWuhTzHtC3hTLUm2NPdBXqZmZh0K4Si_Gt889yv-OEuOPJlriKmlFVre_iSacZwUnfX04YrBcAYsoQrMrEYmCpg4gE_88qbbAvesz2gCLPsCFK2xFGDGUIvEOyh0TIYbR3ZRSeT7_i4DPZ7cYRdMa76GzL-dVVw3jvv5xg1uQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW40gRVayyRJSdZ4GOFBOU_fax1LNggcLAhiWHdZQFWYMH3T9xxpJPlipa2A2aCd8W5Swru0jZiXGT5uWs_PZaanfLQMZvQM5jMOZgINUABkzXYFD-JntVlqwXkrnsDbI76lTJosFmNMAPveB_mkFWyaH6KrLihdHhNa-in6kcpV3Fa19XfO5gix7ValKX6wBp89hBowR0dG7tmuHk6Oagqnb3YRHNY5NSKvupmOLTeAS0JG_1vhKUGgoIuYhHhMKvyUp5eqt6wPA3gxc3iW3nCQrbnVStFu7_dm1tamdusIBmF7UkWJWmX2apJMhqHNgtK9Flsw4A-pfDBkEFEwNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم بعد از آشتی با وینیسیوس
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92904" target="_blank">📅 15:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح پیرس مورگان از برتری مارادونا نسبت به مسی و پاسخ جالب جان تری از تجربه بازی مقابل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92903" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های حمید محمدی از دلایل شکر‌آب شدن رابطه میثاقی با عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92902" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92901">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92901" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92900">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmxygqt07reJA8u6MMMi0GOEhsY5fIeDfJdPkWHfLOGTH-If1tUR4sqBdfF3ygEkqiVsqzC1QqQc16XtTWa1T7IeF2Ovzp8LeZeYaK9ImQ6HFiOsv4gXhIjIIXAOLI8PUocv4BpE1Elp7a_OULODC0DBWW9hS_UPDGIwQgeUcHV21v-NqD2nOGGNLdAJ3qPoMrZzRIGSraBG_tHM-FXOJOc9i-xPxfJ4G5TyZXwbnNMofLZt5jPICALo7q1rS5Kf9c-dSEZpDeD9dfGUhyztVd9gzo5-pAFkdU4G5MfultoHAhmpmJ5usAnNYn2eTQO0MW_PEvNTv7KBdpYLqaUVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
پدرو پورو مدافع راست تاتنهام که گزینه رئال هم بود تا 2031 با تاتنهام تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92900" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92899">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇴
این پسر آرژانتینی وقتی بزرگ‌بشه میفهمه چه نعمتی بغل دستش بود و استفاده نکرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92899" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osw4xiXfwDlzA7eCPbQIofmSZftFbOcftfuL0mF65cf3rd-Q-NBkvEH6b2ZTGaISJLqo7mym6jSP0GNKl9FLWMkaA3qGgnNZ9rbFAuulmM8gorEmXkPmHPdaA3QKTfqMMyBwf1KjaLFKNKDQ44jw7zeQL6qUPbrbLs9utYZZvReH_D6tVzeqiXQKEb8cvKDWcO7sMucBCKTyq0TmoXiteY_XsJL9mrZ7_m7YVa45vGVIpFYPhBOgvAhvOrOsQ3Cozav7sgkucWXu34PpzPVrTJxw7VIZs4ZOuZNxcbrL830hjyErGIZjvVbiUaY_K5tA1LrdGYah4mq5KLOuSsSDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و ارقام تیم ملی آلمان در تاریخ جام جهانی
🇩🇪
:
🏆
• ۲۱ حضور در جام جهانی
🏟️
• ۱۱۲ بازی
✅
• ۶۸ برد
🤝
• ۲۱ تساوی
❌
• ۲۳ شکست
⚽️
آلمان در مجموع ۲۳۲ گل به ثمر رسونده و ۱۳۰ گل دریافت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92898" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
#فوووووری؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92897" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92896" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPgNkVSJiYcuvKvVahOvA840_rrUZ5W8lKZUeMQoPaD39S7eqluVEyjhPOSJkh9VyT9hwnf-rRlPoKGR2-dSTN91PLEv8Og1839UsYRfwiY_xNgwn7fcQB3vY2-LpRYU0_3IEBYM280c8m6TZfumrU58kzhVqVdbkD2hTzxSA0EKdvJDkfyrJHxqaF64YnTX9RkJPqYKN7tAJaCXMl7BFv0uzG6YBsoAffdp_JwIwBtYJA-rkbsnO1qVRnn8AkRlktONd4MnClavz8ULeVGY6GyMPN6MTeOd9OIHkrKyA6B2Gcc5NdzNAzSQKxYTyh4hTomLVHJW3XfnEvQh1ubVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوووووری
؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/92895" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
