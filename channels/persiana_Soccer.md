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
<img src="https://cdn4.telesco.pe/file/Ly8Q7R0nBATnUgJMD9geHOL1M9zUhe_qMeBnYkiaSsVII3qDMYOvYP_7oVSjW53PQBbSb04gwsuV9FMH1gqlfmGYnKEeW3RcKzcovLWZWgI-sGvMdC1VwSK51ZXzOtB7qMoLuI6JDXZZPqeiUm5HrvsQ_b2Ks2mBV1hqYgytzP0EnpaZnUY0eNGGtwgQhv5wtrc5OLQRxa7zgglBe-mPabT-SOtcUJdVphkSa9h_dO8Dv8RCdHWxu8p7Ik6MJtPobfq2YhbHWHU8-5paqDDwIN093Dt_JH7MqBwwystIYPUXZx6_8SYg6Uatvkl0AUuA6kkjhJe6wKss2QC8RvWlKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 175K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-t5_rs7NOYy0Xh0sYI4xFzEP9E4F57DDWFWNoLFB_go2z8L00lwnuWkVxj0bZbT3QfVZLBG_7bqqd7hSFEwQrpkezZyvmCQNO0sS2XEbyBh9Uce36xdRwAL-FNh_sYsgG21aoUTJl79iRxMbn_d-MvpKahfjaUYH0gWi18nMf_BfKodHg86FACSZrOFia1h0iyU98e-E1tiOqn9_lLZlQl5o1Iu4h99N3vFTX6hv7wlTOcuLEcnZ4eGtFTRzHGjoAs_-qiq-lNVNGHFHQGryaYf7_RsJKk7JQVFcBmRqGGdsQqexUWpfPWqkksfPHvlU-lkho4PxbzPp-6fWXbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQC_U9WD-VIGuFyG5tazb5DElHVIk5a2wZWs4nkbOITxXP2ftvr92jrwyhyzYDTqooiUoXgyOt97dIJFXc5zgAQ1NqJzw2YKfSsMZALVWTYPiZlc6uRLPhWAr2iwu0jVeZ9OcH3s6mT5-TyXDlZecQx0daH9T88zGg_J9jYow8s61zURTrguhJ4zcl-E7HRxXseizS4QVtjVTww2kapRnP0IHIz9ioc6jnokdYfRG5nLsZdpAplZ2hdCKABuGyYufKMOVv4Sg3H30gfIIcOcQzfHpCeEr6eROygxvLYi5GCSqmreTLjqrFKoLlzh2fPATGbH-CZt58UU87_w7SeI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYSzinCQFlYh4886qNz7QwyZMRpfiDVNrLQg-B_cw54od36Bl59sZ9ycNIKoRxJeFDjZk17Kpt45WkaSO3P7oWLz7w2qqT58Np5skL0Zxr5uBxbx0TGmH29OKXElZ52ibXeBQYuskGmmmNgc_bFyHQ_JlubE35LyFHFzeG0ubwX0HcVs93AftaXQ9uMgLzFMTZ7YQXJSI3gWNUHVjUkd72_uZODDde2P4te6X0yNelp6vZbxRMUboe-gFKljGg73MVgZN2wUvjSJqZcfcijaKhVnbhrk4Zwg1ZuRGTeeOODjejFYqoWkrCXdHdKhxb6_hhVfV2-6LcNowIT8MOwi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMG4qBvKc49199hfzY1IbmfMcXqPe3MLCaXeFhODXR-CtyIz_UGcHzJs7uRy8oeUMNW3dwblR-nliamfG6STEHoiyXgdVN7wkUZCPzEqivlM4wfgJXkg1EP93ReR_hURFPAwqnAnmYStFQ7ZBKo-V9p7mokwf_0qIlpiKQuMpn_vcwE383EKeHOcZ-fCSuYHqprWEJPe2pfXw8oywwKD0mkQOnufJPBOocGxV-uIkMaSXDp9dZyyiSDeOYDqb1dhrtfCUIK7lTiZAO1sHy4mqH9O4jubea_gW5SPkFPiE5pQxON19ZQqJJI5yDaQfCPLrB8dSIQe_yc02OBCPth3SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=WDKyhWrHclb0VAkIcOnDEiWMvbsWawnxgeoVvK4SX8pqxkHpqP9UTA3FEVpDq39Mh-_m6kpfRLf1X2sCHniSrULNzQh37CJwmHi3Iz2FxqU0VbeG0qnrLdVHSD_MeBM4CBZ2ZzExuaNeOpSeeFhWtWAHgZWYbFgA2cj-ldeGTNAUsHPjbk8XjTOxQTIGEA1JdRltggX49peVJrXmIxP7RyivCN_yMik5MWH9gE8DCBFKlu4ObF4SysHqV1688LWTo0ET13cZSTlgcwqnz07tTRD0FOissaxBB95k9_ZfgVuvc_ryoSWwMQamrFuc7wq19pQu9IEZEVp1ZYFc6Qqz6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=WDKyhWrHclb0VAkIcOnDEiWMvbsWawnxgeoVvK4SX8pqxkHpqP9UTA3FEVpDq39Mh-_m6kpfRLf1X2sCHniSrULNzQh37CJwmHi3Iz2FxqU0VbeG0qnrLdVHSD_MeBM4CBZ2ZzExuaNeOpSeeFhWtWAHgZWYbFgA2cj-ldeGTNAUsHPjbk8XjTOxQTIGEA1JdRltggX49peVJrXmIxP7RyivCN_yMik5MWH9gE8DCBFKlu4ObF4SysHqV1688LWTo0ET13cZSTlgcwqnz07tTRD0FOissaxBB95k9_ZfgVuvc_ryoSWwMQamrFuc7wq19pQu9IEZEVp1ZYFc6Qqz6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbR7vC-96L4GaFPKD7njr-lHrD7cplek1oNP8qSytfQ-4rLXVp2766vInjuc-xznOAqvO7ehjYzi5eTOJGFe2zaRdgkGke3KdtQsu6z4lPFkc9DOeMcytf6AP5BSqo44wZ9xfvRkiWCLv3F_2zdr0_rHNSPJ4aQAHDQAf6c4GgY2h1LVKa842stlcXCgggoxGScDBY8_zsEjjh9_d8ek113rkUtwzXou94CnhiSjjdzb8njoJ-BMXpXXBvJcXnaLv8-oZWUR6LgF6hqWqOyIH5_79QJjzus3JAHQsX3GAg_sJT7H5oZ1rDR3XvC9iTT7Eo7QBm3Y5_IZ0Q53GR7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoykqZrWzb6lKz8Jnka4ZDglPFtFRzvlqdTzybpwO6mFK82TOry8ZExtwB4Ox6hsN8wDTFy0cX2rnVUVGxTq8VxJS3gaf6eqz8z1IXCGi2UORKcrPpdb2AiusnEdAC1-4Sg3SyzIdy2LFPas6ZaG049HpZELjElsn7s69_4BztQ-EcfSptKyQRSDlFbla75_oNM1Y2gCeTTVgtsdqabPUw2mrHqOezbnEEtrvq07vESTCcGklsByVmedthY7rIMo9z5EBjaTAXvDmE5f_ge37mes5mmwz7ZgiYm7r5CYd7md68josVhmHa1h5Tg-syDOYBQLKVfYI9cJgx8sDlh2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaEr0WJBGKGOo9fknuongQ7uWE7J7L3lknXbWJOFrkzBpfPmPL1xKBgsS-21QcShvEfAq-pZPBZxafn0Lmz6dkNf-6y7_qT3QUA7X_tO_zPIDZFRtA_bUXQF_0zMQGPI8Aj4oOg4nCaJNE9EIIgpMggboLUOp02qnXQ3kINll_DIlu-i9VCZT0oHFVCfrU94xRp-IKkGLw6iioZiDf8MsK-XxwYIcLyx_GQXaLd8qrsmErslDFs-vWvTo_l8tKyoTpRBFRGYqxZ1TLqcwa7gnaqcqHZcGe5qPlFZoj-zVK1K4sEKHDqfs7v0WoeAu-5S4ECmcI3Z8XF7J0PBago0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGUbzYKohhqZ8AI681JtGU30TtODqwDdsY_--OLX5j-QbTPVtXrO0D9PeKWN9KgcbKFLzNteuADd1yomEyCqAWRZ6s0q7fH5VhDnU2DJsc8LbLsxXLVasXHxQNyaF4DmMzIm31NijGXI_kTF679fVglRy_HgEbkfeAreWGU2fwRbU27mDyvTTp0FISHWOpNrDl0tUsXYiiFZGXUy3xZ7LVXHQZLPudVzsE6rquQEMAZx8mwxbB7EOK7cHtS5KJNIixmVY5xsdMDo5zu2SNN1aeTe2mGp9CqRwZ1NCcKtFIFhrIff7osJx8IpvBCFgLnrKFzSpAIcG5j-qis7e2ponQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDgKXmO_XuJ97NWPXvTx0Erg4wlQeEkFqYKGBeoZ6sLinLclAJw4JKuyiVKuxiLDrH92mmaau2zVGmHPYlI_McbkJQthCMov-vA7nTnE-JE1SXrWru1fDz30RhQ5vAlqmYaWWves8o929LJWo1KpDBje7uwJsxHmRzUDiUI_bvHIcYA4ahp-6lHTZ3CfGjQWObjeNNpT7I5tHiDZ4gEZqcdKVj_YPrTEtn47k0_HakuI0eP3BjSdWKBV7gJqXpw1p7CUtl4Xa7Al8vvu427Axf_5r3AT_TpZGtJz6g5v_XzakIrOpG6gXwTkV3HqczJnd9H_GrTQtZkpzm6iIVmxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=TXlK604Di_7aWOD3uskUIsSDiXwmJ7Jp5NY7HaxZTEWwumocBwwsM4H9pLEWyI6QlUav3u0kEzNdeFM9eZ6FxjwABq0QRS8pqcOdb72WMvsg20q1Ize7QuqTDTJsV2_fiQY7iuNUHEqRhi2ANz8dKx6cyBOA1eNjkN18ygG7U41RmU__VbIJtFbPsAd_RYi19lJkwWYus3ZoVLomP_xNSO9OXgZZev3VmkPKBr7WKEX3Lu_mbYQVUE448YgF5y-FS4_DuagJoZj6QQEkMNnbvVFgOZKBnsggBwidr1CiAbEXAWuI4EaBb1gxiWGhJHZlJUE84cCWH6V2CovLIQYJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=TXlK604Di_7aWOD3uskUIsSDiXwmJ7Jp5NY7HaxZTEWwumocBwwsM4H9pLEWyI6QlUav3u0kEzNdeFM9eZ6FxjwABq0QRS8pqcOdb72WMvsg20q1Ize7QuqTDTJsV2_fiQY7iuNUHEqRhi2ANz8dKx6cyBOA1eNjkN18ygG7U41RmU__VbIJtFbPsAd_RYi19lJkwWYus3ZoVLomP_xNSO9OXgZZev3VmkPKBr7WKEX3Lu_mbYQVUE448YgF5y-FS4_DuagJoZj6QQEkMNnbvVFgOZKBnsggBwidr1CiAbEXAWuI4EaBb1gxiWGhJHZlJUE84cCWH6V2CovLIQYJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ‌توم‌دوس‌داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال‌کازینوشبانه‌راهی برای چند برابر کردن سرمایت
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e13
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22738" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAt33RujyxzBVJtpp19lhwx-nsDw-XKbKLUeHv2oOEipu0WwC3Avz2r6fy5FaVBPddjs3eNsXK-G0-2fePZy2_rLftd8i6LUd3Hx2gRL27U1tOWW7-vQBoLs-M0siHpi1GV2EJ9L2uzuiyT-oQRMiwvzVPxnq6TMsmx07oP2Kx6mwCCK07PxA2rhQ4rSRFwwrlIxvO2Rte0_TAmWoMo4vgowTjk8pdsXEkYCj1yjJIXy0ecLcONGG7m3Y07G_Yj9V7NbPtiUTCzNsbWU-dKtQqXGplgEcZbgGDqeXslAecxSFvHv48DEuEgR2jvalVwPaIg2g6HcYfO3jucQA46FIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=fqA8HIBFDBr-nuupiDtPoKV3N2H9vUj8v_U_dwBPtucMT00583-n1Tq8pek5apYSX5-QDicZDSViNDL28Gx3inupSRhl78a7JqFOjkQ9uVOK_qI_NWFunDYEhOaJ9m98OiSNJq2cjX17hJf2b3_i4VaERYex4fpRWEP32dgtHd465dtD1UzGLrMLZkwGhYFch5Aov9p5Eayq2jVHPFxnMsCqecgR2bnCD0ikiFqEIfdUju2QT7Swe-6CdGhz5c4TSJsV80akO6BGLOwWy29Wfxah9vv3_QYL7ycPOyLj7G2v_2n2VdQdw2ZNSba_LzneNK5PFn6Vv89GDZDxFxI5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=fqA8HIBFDBr-nuupiDtPoKV3N2H9vUj8v_U_dwBPtucMT00583-n1Tq8pek5apYSX5-QDicZDSViNDL28Gx3inupSRhl78a7JqFOjkQ9uVOK_qI_NWFunDYEhOaJ9m98OiSNJq2cjX17hJf2b3_i4VaERYex4fpRWEP32dgtHd465dtD1UzGLrMLZkwGhYFch5Aov9p5Eayq2jVHPFxnMsCqecgR2bnCD0ikiFqEIfdUju2QT7Swe-6CdGhz5c4TSJsV80akO6BGLOwWy29Wfxah9vv3_QYL7ycPOyLj7G2v_2n2VdQdw2ZNSba_LzneNK5PFn6Vv89GDZDxFxI5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=bnolloNZbuecW6ZZKmZY1FBi9_TPbB_26i0lP1mxvvM5GmDPJ3Cv_MdBBAKifKRaF0KfCKo_VnI7c_yxWZ2tHT7jEvfWoFICIcBhETOaR58XJkmvBCJ4s196LiBKPxL__Sz1sHE2GQSQ9MRiNwi34hfYNfEoMGiR48fmkDnnU5nwjtuGUHc_dNWVm_z3rQNP9t71OpEmEbrckXdEKrM5yBNM_Nk9Qxgd9O5SvtTMpbylvG5WP2dSk2PVJLzfSiqs_LhFiSLI-XwbcFLl2RmxOtPufWnWmonkBmadpf6KCiyuQkPs1-6KDvX2l_IpT8S49Z22hwugmHFxvH-Ifez-Q5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=bnolloNZbuecW6ZZKmZY1FBi9_TPbB_26i0lP1mxvvM5GmDPJ3Cv_MdBBAKifKRaF0KfCKo_VnI7c_yxWZ2tHT7jEvfWoFICIcBhETOaR58XJkmvBCJ4s196LiBKPxL__Sz1sHE2GQSQ9MRiNwi34hfYNfEoMGiR48fmkDnnU5nwjtuGUHc_dNWVm_z3rQNP9t71OpEmEbrckXdEKrM5yBNM_Nk9Qxgd9O5SvtTMpbylvG5WP2dSk2PVJLzfSiqs_LhFiSLI-XwbcFLl2RmxOtPufWnWmonkBmadpf6KCiyuQkPs1-6KDvX2l_IpT8S49Z22hwugmHFxvH-Ifez-Q5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ7BJJRDno7cmEIDGqfmkWozCkp1N9ytZ3Li5plcj0LMap4liG_cGwZqE-pITjsgmOjQhgxgxNmdaAp7fInvi7CfH9RwEg6B8Ig19RmvUixm0VAoiclUpj28t2V64dnfCg6MyGAZUZnPgH_V9cj5KvfgYKd_y7oTucNJ_WvSzFecD2qJW1do0-9OKVRWKV5BfNJNSjKFF-rk1r0l4tIjRduDaNqto7i2-Qn6rRMkg6evHYAEmtwsVYS0un82ysKCDiQG9Oy8pynnb8PlIymyAOAjkSeF4sT3x5q7NalYUzp4bCV9pmX04YXyMQyK9KeEcvPnH7QgBoLJVye_5blpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q81PgzSjaiKyvjgjQfNlE7qRV8lqLw1bSDSFfWCat9LaZyt52FoSvsDH9WhBlTJNJVq8jNraUR2EymgGA2HiW3bUePqpwjk8bcU28rEgjV1vKyMFsRSvZuCi_d-pu4Wk8V9kBgbveZNo4qIgz5IF_RthgGzTsD-wIfuUrta8itOQfqjT0NaYD3bCbclhwAXnLxSDr4QnpmksGSMEstkMNIHGe1mn8nr2hRNWwXMqDZTKurBiHZMKJ5QSnFEuLI-KuFP8tLRE7uSVv1hUOeHH4uq6TqZWGIA3_adZm2pvWMz28efbYThXUbhiTtHNl0z0TaBTuQfDx0ugCz6YJjs5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLUO4jvDdTBhO_7BLxEBr2p0iDkYF6w2ttLjkTsxfjSBYIJVvaL4EIyPPqyj8G4kQGGfmZt5Wk6pKmCxJ-_GD2ZCNga4HqqRdnl2m5vONI9Xyiwk7RA1rXJDeklLbb0lp7cCyQAz9I_GEcQmWXOb6HSJvEg9ErAkKlVML_aKIOGYZzTGkQeJ9Damr72Y_mpkgERsv_0v-oCwHmSsvUk_tlG1v1DTktQtdeDUuHFpj03ylqH7pWImG_ZbF16CE2yhwJOKD8rq3f3gnQJ-cUpNoj2IniQnSY0Hcf-fEiWUKwauViIWTb_K7roqebzUz5v15EgTto04N0nCM_1mnhxQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=kO_yjcmLWh_puC9SAAyrQIOcQljhvIcl2gqXEnciy_p9oVA8oF6Mqug7RHrrgC8SlqeuuUWprmPKs_lRA_eilcA277sQt8RbswEu7-rGOJbqhsjWVKOWNVJ1mWvvO8SNAxRpnaTwS8q7C49mN1FXl4Ma0uhY4aPv6zPKwlqhvWjkTtB5OTGjkAjgxUVkUE2KFhhcUYk_RKv7v4FtQT8WywEYIZtmjv22JNhb47IH1dDMVXITtiDBEshL7hgBT0JK2ltdDBi1M1-ccUPHFnxlJVVJFymtNK_ukMROcMVjrWubnZ657yCJYKtTDcgSA-TruHEv9RQxt4_qdTriQGrdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=kO_yjcmLWh_puC9SAAyrQIOcQljhvIcl2gqXEnciy_p9oVA8oF6Mqug7RHrrgC8SlqeuuUWprmPKs_lRA_eilcA277sQt8RbswEu7-rGOJbqhsjWVKOWNVJ1mWvvO8SNAxRpnaTwS8q7C49mN1FXl4Ma0uhY4aPv6zPKwlqhvWjkTtB5OTGjkAjgxUVkUE2KFhhcUYk_RKv7v4FtQT8WywEYIZtmjv22JNhb47IH1dDMVXITtiDBEshL7hgBT0JK2ltdDBi1M1-ccUPHFnxlJVVJFymtNK_ukMROcMVjrWubnZ657yCJYKtTDcgSA-TruHEv9RQxt4_qdTriQGrdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW3tjeiplsN4j1FksxijzPYXxobfE5q6wb-XZEMgwEyfgoUfgTm0NWxkuRlR0re0UmqzjxiBTwOLnEHAFBmP2DoBUFFyKnoG2c9EGO9e4PuvYanL1adW0p6JT72Zs850eCkqYWdxLq-o1ZZrdLK4V9n3ggm6goKQKQnGc6MrkZ1KEVGJ7RUMnAvBtgJ4AdVbTjiZSoQ1I8E8NpBoiFiBL9aPGadYrrZZxTdvsIgGzlrkc9wxyBUo69UdZQfH6HrgdlIVlbhIHl_cXkEE-eujRP2YQAejMZUdd7AXKxjho9d2zYL8bFvjoiw9_Kd3M53cZC4oQFqUp7Q9LcqwhwYdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIZVxJGfFRC0w1MkFRTk1FhEfgnz3XCh8pxdTCmVpmz22RU-3qy_x39oAzYEqOZrnx69hYatVpkSl6vnVlLHDoJtrip98rxP8o_mo9bXjVe5LdcLUd9gh7sboDjhEYkp2U-ykJ21Ybu2YS7bnlV8pExZIJ3RhmH5_q8ySLT6wZ7LQpGgH84xlDmevtrmJsX93FoOtFbKgl_nNsA49fZl_VXmrNxDFKuqjeX95-9hhRThf3VYC1vA3h9ddHeoqyEI26ecXiUswcS1nTPTUmah4L1ZJUd7xdw2uV4uY2wVzi7qpACSWqf5cdEyShS0rlZQMt2ZQMex3AsQQ6HR3P1d9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFQ3TBlbzXScu-I6486nR16JM8PQ8blOf0MBl4xFm9aKdQRFm5JRwoYNzV_6_G-_QLhj0MXbGhlFsgxuh19LV24bQx9ejdL6VupQLz5BLSdDI9td5W2wa0iNrfTnOVY671No8xP5pAWpIxmk4cBV1DUVRZ1v5lV0Vtqg5qxCkk3SFIytgLfcv_Uq6sTbHE9NjN0prlfGVPeXolFdvdKVNipZOTbdhi3AQkdGmvbLBzneEomLODnaXJB1vOr9EG_uYYo8PGxffKsmykprD5AB7D8PsAkT1-ai9SzPaGPiaoWbd17AoMDTsa7TLJcOun7Q4RXqzTLHJjMTLPzke7krnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfvq-_A_dnTrzSykHCosI3CkbYorWb5YVgep-dOZlzj4jZ-eWz3jtt5qhHqCU0iRpChqmmPX-iW9t2LycoU5G1JNP5ChCBze4RZw68htKoPoxCyGH2xptUhZR-3oXcY6jn8gq0FneMcHJCAbrEBrnI_LM0jXkZXzVa0WcgSJJSigrA1iZqOuqPIPQQzJxpYHfj2MKxbNSFtRIM0HqN45r5U9JnlXGa6qSgPFYwNfmjJz2yN5tFitsqTMjFwHL2oGPQJK9umTPaPMsZWFm5YKZN0BNgrHCNljycgKpsdYX2Rtacz7Dob_IAYg0hFySzZwD-PVoAHM6km4xKzhxOuVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxP5XMGdayx1ZuUzuRf_2-xPaQX7F0W8GiQQfOcQAwOnedYPOwaBeVBCKzaNgtShGkiorSm1Mho2efNL9lCAzC03wFagBFgNrScwXPtbDg8VkgbWCNuKfQHNFZXFh0UCtEG8DIS4f3oicVmf4jfEauZdl9b3aJ_GIRPra3mJA6S4pmMtNxdezz5wZ1t2WOjC49yQ-_zOeNZDC8nCKYMHReltXZliHCJ_lP_S4T_Yz-3mre_23pK1F88JI2-crJVlYVQO8ohnR4FTUJ7jWd1jr3LWyNqlFZGvOSdoEowo8UhWvwX3NOWwPSJDoetJYz2k8WzjhQO0_kB1xJ0FgTfFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQPeVhEuUADxeBohr0iJSXMZrVscMMTSuqoHOzoFQOnGECTax4bnNOU52f4q6uPKnjuoEIDEUuPrDd7DCznLYFJPLcyRzT6A5ENOnkGMCa3cROeps-JUWggXydwoXOtMdJIupeIzx77BcnN_nSNEUq_L-zrAmmez4QUrmhD1hG-mbF2cLB1UaSS5UvCGVI899UksTi94ojLA7hBXY7JWSwSbtWhxxAIczvdMSVykEmbKwgQ-jDkPBUfUjbQ7lyW3RDpDudyXGJ-kvgm6M5UJlmuRA5VOhjJlbm8jNCfrCwbQsdFcXQ_wQfCK5lMeAAiHAtkiwOWeEuAuNsQTitDB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
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
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22723" target="_blank">📅 21:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giH06imVNuu_EVWcKd8b3aAgrQQxxWY3I4nQsVHPmzcWlXIzvwwDwtrQZvHjngusKzZdNLXVP-1m9krSsBHInlJZbTnk4SPTT82muzeo4fisww0s-MeeL5uazDsQw6Fep9R9PILLOz0wL2eeG_hME01OrrSrkCLmfcG3odPe_CzfFakCbVBAncoao4J-JS2RrrZqNVXCQKCtl3znhjL1kzW-Fwrg8izGxBTpp8qzballgOYwsb4W2-c4uByUXuh__3gx0vlrhYjx7L9Iktp_RGHPrwARwXVrb9kIZI2gLqB99wt_l0CQjQO7DXYjd0B92f0qUj1TjFmaSNnfGQ3bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec7pFA4oA63tf1qKOjJvw2yydldJTGQBUQDweNfEnVtBLWVsteok3ZIYUI_WxcEaD6IOGOuKUE499VudDbTmmlxNoNn6GW1zcRfiq4UdAdKNy6aAaf-T-FWZYuf0D1M4Ie-Hfyl2hhfYaJbWhqdooiVFWfFAmtj2OLl8JX4Xw-DZOb9uMtMAtYa1nvZzTpciEHIcNoHvAhxhZtHJEY8qbmGXlI33PEO8xijaGHgRdv-bgi2-9edF5uPLe1eWJdGhVFwRFEjeLs-nq5DR5dQF8gNLZXavkWgfjwp4mz3rQacCQoP7EDwhmDu7lk8N6i869IKdBZjIBeCLnzqNYIqLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOhJX3ieTGcVeyxFs36GmkGdVj8ZzZ1A45x5dgAAFTw_D8w5kf1HmQ6RJBRcASp0OtVQke3emu5YeL7BIvJ9cgFmDWNPpSh8Wj0Ouve80aeJbhWP5AJIPcRe5zQKCqQuU25k0svfG0V-6aRsMlIBMm-A6xiRNyCZRH333Yt4AJeF2a05tpt9LjCu0bjvLKlceXlis_RnD46U45gI4n_WVes5OlLG0JDYstaAJZvD_IEF5mN2lJdvuFCXab4zwMBzT5dzWXr-T-3PrFybm8SkuujEu32J8sZhs1hlFhgk_NJvDeI_9ZDQCiL6ePdcfs5v7vtEkNSIzybEsO3NHYrN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTBwcJ_ed36_3dy40YUD2lqqzgFlHBkarJQ8c7NASw_11TCqZL6RgoZmukyqrwMls9nayejMkcc9z-lN-NbfWeGnhpQf_tMD7Cwj-anGzvgYyFemyqs6wVWxUAV2hA9aknApndgVnBfToreN3sZ2jplxEbEeaanfXNr1qvVIJnuBPC5AVILYC8Bmlk8D4wwdmuPffh8V_6-O9wZElvHwqu-_Za-AKLUBEVVTMIabqOSzUCipC23rtAVizifnZABQtGD0U4_o8bCEBd9buRKVP3lzd-c8fMyTI1Q-C8K4K8dD-CxU72TeXL4Wvt0FQdxpLrIDw5CNM9xbxZnDGHqRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEmc11yTrDS8B5grMq7LYMwfJ9470rfl_SaZKdqX1twzLBtwpEpSd7QF-1mpgdQAsmi342mAcAS0LkV72I8cFKHRV9rODYhbu8GLGN5mQ9n65aFNaoblr3dQoLItRVclzTYjeCXvssMfbn0mvmMK8dPWGZGVqrzO7B7e_u7RxakhAz9hrgDrG43tnrwv9SWgEors9cb5ptPuBySNHHfG9SOncYqmPOR3ucZ0wmUXWy6qX95Hu4MEnxYuXjwxYAKC79bMfA-aqvS-gm_k5IhEQ22n23QDlKZH_6xTOIWadraiArIfX5__DLg1KNNFJ5UJab_F74SjOTVEgy5MJ4kH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFmyzW26rib0iR0AtdMYP6YazoihszxMxqvSHNYD447U0ampz81fL7zw452AcIUjSzBKu_P9-ladzPDC7QqBtzonEO1DTESLsHybuCFSBP1g_hkB5HGg--Mb87maA7HkKRPqYOd8bOi-hCuoSmwVMGK7PWTyai5ViM62H6--1LVCqpJfekgOvpoNjSxjDTIPE8sneSE6W8XFMZntIs44_SN6jEKvfrk_b7TLDGEnI-CC5dCc6OFj3iBdFGTGjl34JlG05G9UTOYKjhjaYlTdZ68hpW47VxkY-EJQnG94WcBmwigBn0nXhDhbo0HgoP7nWudgGwIgyIf6uOA9PyUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUth0sMnr0dbJDs1GX3-9WQgy0JhicmdNZCpCy0JlG0f6K5epUW2E_DiSQwvVjWW0SifRrmU33O7dmCh1dXRfgArgiP1Ad1GoIfKbcTfq6GsnUAnVy1iQkgY1x0onJ8GWhL2pLU2hf5uesZfsPPMPFNl2znD4VUuW6RTdcgWbmOQ7U7KeTDt4kbvxBxHd0euyQplErAD-72ySrGZ7At6CNsde3N21bD7fWLPtDKaAZWFYmPKK9NQRwC71GHGF4uidIr8DomOoluinDJotxMd7XmjTn1r_sDiRlXn4f01BTjMMnfgiBd3blOzKHWH5S1yDNqpzwtk6ntWRXWXatLOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqHCwfxD6pozj44BgOabKMzxKSEhTSo-vhtcnJhbHXpEN1mZfXXDg3HuSLnNTMZIPARTnTRoYk8hKXI7letbp9S1a5c2ZTuhWHCXWDI5dPC8EfWigSMxCJ53vST3ct-TjSr8uCyZdp8lZ4KoJMY9KlWQqBpWJOWNbhjNZ_X2Ws-ynxtgnAR1cRl7t2c_Z_lmxBXrG7U7hjKmkaV-1aAN2OLYAhf2uBIjPinuTGOPzDmExAPe5B0D7vYEtvZVWoVLlwVng1-FQyD9Nt5R4uOfIVfrLjHktECAHMBAmb62AxrwGRY8ydMwtYIsE_tiqZ-VAeZmlI9rkERxVyHzUQkREg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=UxxniO0cC8VzZRLtgouamqn4qDqWAmcM9rXHHvEn7jxRPRKmHhfsX7yIayY1-EpDBNtqD-bCK-xz2MnTSR8MhXPjWb_Qcts8ir3zkRbHuE8zLnPB9oarAXbEzmNHTD0yx_vHqLZPRL5EP7xkK-VjNMJVtuAKvW9yfRpCkWtiIW26mZ3L2Ilhp4yM0yiti7vIyGJkHRAyI4MWYpUlrTchKA0VoIZbwbp_2li-9Mrl7stByD6GQfSHSiE--WZKuKprGXWBDL9Tv4ZMnFOq49YOuc4i8Qbgl7CCZuiAFAau9bONMFHlY6dXKgEMhIQ895QqqjUiwkCbqcZlcxMgQk0RPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=UxxniO0cC8VzZRLtgouamqn4qDqWAmcM9rXHHvEn7jxRPRKmHhfsX7yIayY1-EpDBNtqD-bCK-xz2MnTSR8MhXPjWb_Qcts8ir3zkRbHuE8zLnPB9oarAXbEzmNHTD0yx_vHqLZPRL5EP7xkK-VjNMJVtuAKvW9yfRpCkWtiIW26mZ3L2Ilhp4yM0yiti7vIyGJkHRAyI4MWYpUlrTchKA0VoIZbwbp_2li-9Mrl7stByD6GQfSHSiE--WZKuKprGXWBDL9Tv4ZMnFOq49YOuc4i8Qbgl7CCZuiAFAau9bONMFHlY6dXKgEMhIQ895QqqjUiwkCbqcZlcxMgQk0RPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFDJkyh96Kvf7OaJ3kq5oI2cl4n3k4XT0-iIOALWwzK5NTFI5E8vkUIgdD1VM-gWLgV-2u7BoyWLa6q9gJH4e-oGRVL9Ok-nANvk-WEZqcMvf5OeiG8uGTaSEoDbIkDcaP5lnJDKYe2nWTWpjDVyb0-nXQgGHaHBNuMr486uUSQqzlJa6iK32ME-COI501GeROD0uZ4dCHpuYs1wLivN0u_y7vbFFBhha56k87hYfKJplG7xCq00wLvEL1soVMW2mixSH_uUl-UnsBR5EaUqM_kdHy1o8OvMT7P-vhUBcyIRdI_7VJJx2UTQYodpwu8wICGCSMLstfpJXYZwsCaGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNHGwPdsD8GRlj5s61a3y71ykVQo7gX0buGSWApUNS0zzj5jO-AVg-Yq5M0b0hL89SjRpEeYDeVSP79tlO2o32O6d5EfRkx_xtxubQf4geGJFCGnbObNmqx23woDHbQ9Gnggu-MICsXAINF_upp3SpoMCUNmItr_0WQvCCP8mwChCXohKuPZz_r3fDt43fOmNfVNmLi1x5AfzeyavYBQ-vsLblLEibDip1NXTu4J990FpBtBMCBH3oo54kBkmQuOp649cH_lxF4cENVd7FNCTM-ebl9sdA-Xs-mi1MhFkNyc25uy0WhYpQpAq9_TISY6dw-zyC0PiGcYenwPDq23nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=RsrGVXqdiUNXd67esQsXQk6o-fm2BX-372vAcZzDHpyEhiMBsL5qNmKUME-_UzyzazFvri1ugutylRO0rZ4m7wuJZ2-MpY_UIu-mDIPKEoHEqE4t0RC3bFgIpCKn_VURYcl7lf4t8ciItM3hDsXNQheVq4D_r9Y-41fPhJzJetMC1tqI6OdBYIvRJkkoeHaKPg_HbEGJJbxh64v6uVtUbIKLD2d8pW5fTuntOkaUjC25csQ1wAjz4q8XaQgzln53F7x7_PzZ-DZKF8IBXB295Z21L1quikw5nwYx0VxcEhR8Rl4PQKY9jXGgduhrrC-JanUh8lGIbOb_3P9MncwgNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=RsrGVXqdiUNXd67esQsXQk6o-fm2BX-372vAcZzDHpyEhiMBsL5qNmKUME-_UzyzazFvri1ugutylRO0rZ4m7wuJZ2-MpY_UIu-mDIPKEoHEqE4t0RC3bFgIpCKn_VURYcl7lf4t8ciItM3hDsXNQheVq4D_r9Y-41fPhJzJetMC1tqI6OdBYIvRJkkoeHaKPg_HbEGJJbxh64v6uVtUbIKLD2d8pW5fTuntOkaUjC25csQ1wAjz4q8XaQgzln53F7x7_PzZ-DZKF8IBXB295Z21L1quikw5nwYx0VxcEhR8Rl4PQKY9jXGgduhrrC-JanUh8lGIbOb_3P9MncwgNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlkwZCh7x3iGr8j2OnygtWkBNzEFFTm0GJZeugYyhCa8h8OrDvblLh9IBdUAYmgfkFLWbSPxZh_INySuP_-0qBbHagNQRlg-H-Hbl5qW_wgCOA44E7f5f_I7Hp0v6swsmF81cxaSaLkRijKNvCgUCQvluKr3VZi3-fS_G-IEWnhjSJMXDSxzszDr3YXsmY6ihnosJbEiSgLGqY5Z4lpE7biVHz2693eFCLFp1B3JNEgyqs3MqHsySt6ccAqMX-hHJIC61fI9QCu1E3cvQ6HGrQtL0vxJZHiWIIoAcu7fahT3nDniwFEKpqXBdGfvv0t28YkJkTFyyZ1diTcOzxwkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWEi18vyNvv4DLVwlrJrA_xmO3LyB1FHiDi9uDUzzzPGXh6uo-yOFXcfQoYF7VLGbTZJDpvXl8u97p5i7hJ3-BfzzHsu8GjYgA-LvDQCd6fDA4JZkyUvZDGROKfHAu05oTlgEbNLECkBrb9hDNcqhU-u6VlfqAO_IukTI5osTjXFzcEaA67jQDEKOGc0-It3U2GGuQhvErqDLJEbDhMB7LNfTlbJJkgFxx-gLgvH5a2fVCMYM4WMv_gESn4muNpmGvi5sV0vMa-EQDMLigU6Kp_3oi3Bsg7c12Z6D_juCcVXJiTYIWaEaJyfLwQMNm1P9VbuInW_JJIBhoGiIN5PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0kX1mocJHX34k_8s3i3e-Ccs_-Qa7CsCh-LTHH8C3Nd56FWS04paR6sP8DjURfaEbt7ODE3-9xUXtmP339IM1vZHwLH_BpKd7kIW-6iBfWXCi8547NLBFq_fcF620zrYcM_P68pFQMBqh6tputZdbq9fhmOgpHAQy9FtY28dZRyUccLRaPeFdsXLLRaUUjzcgOqHpKZP-PNrgZcLSd1yJwsgPtwTA9IrmzPibL4KvclW3YSqPg2HKLNkFcFsxeN0QMpCLILUKrWBUklwxjMNuNCDa1YJAuiwbCbztt9cxKZP8z2wQGUJ2NhYazdZi3FyhTvZeo8cGdPRFx3EiHwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIVVOPTuLlaQE46TBYBKIPYKbpk3Jw9jiM5YOsClm5beyYgb3tdAO59efDVz7ixrRviuWz22QCxmlZTIN33pQxECBVKEDy6hp-B_HG-HWVrtUs5MoGS3sjuM70iW-Altg7YiFYIowX2-t6slYwZ-aDA-1RSUgda9ozsZKgytMMi37GOBtSFMA5lMYHdF5P3su_V9KCPgfS2DLcwVd323GL5Ospm-RzVQ3dkqtrwlCkEUp5MMtZEzZNfnrMbRY1GSyMgRFlC8arEwULZp44O9aauXG86Nr5oTCMzc2gW3sQoUN0-MM-1_n2HEaFx6wMwRtbq4_UsMGVVeC2I_E1F1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPRnkN1WmVuB9AUlsJW0_eABj-V_Lbz3VPWtzNHthlIFvYa7b516I2zs5CkRnET9r3tttoee9biKqvfZEuj36HZDOMZl-tIsPvS-bGMLLvTC1CLEBwOqQmdox5R8Ofc0V8iooUqoCutpLMn0twKGynqjE695TzlgRLrPREPT6iTeNPoirGqYpg5w-O_m2Z7SI0DT7Tf1NT4RYZnsZFGEqjDKWZR3ys9iN8HJHHLvCfEAiaCIWjftA86jtq_6Entkcb6Z3l5FEQp0xT7gxeaDbaFm3IK3leYUYU6qvHathdBhQ8VPhbs4DZlUVgQkCnqxurNUVCr6VVU1NCNMh37NaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=T9fvAoLtVqYD5HzXjFYe1ns_8CR52V6cyT2Yzk00vzrj21ByL6JOhRnjg7tHFCYLQ7IGw2FW1x0pZM6EeqbRUEVNt6wagGnSi1X1TGYj6890IEV2lMVZXLRZWug61jPwz3HRx9UMm0zI18cDFozBoxaoIXUEop2oGkaEU_E2M9J6Rd7MvQM0a0eto7aBAM2rKAlexqnDK1LTX8KH_PHPwJwxKAEgBsDk0ZDGoSUzT70f2YFkrxmENpzrtkGhgBxxu8r-zoyDiBxBCzUbM0CA7zwbCFdx5qNlSeeb3zTayq0nwBRLCH32o5tdxTA6DchxwfsRGdMsyE6olkcGazf3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=T9fvAoLtVqYD5HzXjFYe1ns_8CR52V6cyT2Yzk00vzrj21ByL6JOhRnjg7tHFCYLQ7IGw2FW1x0pZM6EeqbRUEVNt6wagGnSi1X1TGYj6890IEV2lMVZXLRZWug61jPwz3HRx9UMm0zI18cDFozBoxaoIXUEop2oGkaEU_E2M9J6Rd7MvQM0a0eto7aBAM2rKAlexqnDK1LTX8KH_PHPwJwxKAEgBsDk0ZDGoSUzT70f2YFkrxmENpzrtkGhgBxxu8r-zoyDiBxBCzUbM0CA7zwbCFdx5qNlSeeb3zTayq0nwBRLCH32o5tdxTA6DchxwfsRGdMsyE6olkcGazf3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9weSgozsal4MFt0a7thXPB2MdCi9XwxocBREsHDjkpYr2pTpVVNbhEw5PLE98cthtCc_9Onh-n0XZY8-6_KdMskdFsqEJlCXXoXqT8xBSK8tldPZEw6UbUFdPHtBHE6fKwaIWwlv-ea9hDgh4StWTPCbq9skWtdRpL6wRLlrujS-wuTXXWzWf56GOFku0qzUyqBoOckWgwn1mcYVxt348eVa19kzO4ebHFgqPPH8MC6JJu5cQ0skGScnXdJ-RRq-PImb6k9WLS4SNwoqk5CAvJA8kUOu1nK53m-wyr5haapm3zovYi-AzvVPb6RO8MWrbEgLPFBXsrAqUkLd3YsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMTz59WP_qH2QHxzMJQ-NsY619QHB6nyubz4Mvn01KNjFDD0wXERH29JJjCgpPmjuySJyj0eE5QF5vuToOfBIQiC1IK5N5VkSITHJM8uq-2oZncHFGV0Xn8AD-p0aPPGhQm9WZ1rfaxQfwKKVZjD2K2wPk0Orc5E-AdRV1-I-w_OEM128PlMDwPCUUtODdvn8Xok0lrvB5JBhbn7pdj03dbUn1eMiN89iYzxfa-Ij_faPQOJzUtsv39f92njQMjKDz2B9Gfx64Jo7flCA2xrTciV0SwmE0PK9l0Z8a6U_v3J-SJISktLoL8kydwvYZKH2go3m9HHJalRj-90qbLLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKkKExgn-H84gF3crqTl4_XG34QXTdx9rb7CVInttTHjmlF-x793-Qx88OFf5TMeJc00rc-zQVVHUt96S7frw0-jDGpfZCbXqA0aZyt64IikOPEeu6PfA7blc7BW4MfUVHWWSruHjZN7Yv2sEvZADPApsxLhskJhvWxfKAhNC9X66FLVAiDOqy55cxYB-mBrrFLJPngMClMgdFnPjauDL0IHVso0igC6kxIPA7lznIle4VsCLJJV3J01WJeZFC9boJmSMVCVteo4So865sVmOxfKV6TbgLof0vu1IUuobSRLgxxF87Z5B_gLr2XwGeirgNa6PmIdAd1edeM7zu5lgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8oxgXyBc4fRHHhXlHWlTk30v4lGw1f1lbaE0LZwoZyO2GO5z4ouPOoza_y3M6eB5wQxSxeN8GoJTia39yHuVnA1-THjE4XNNFNmmRTi54Lk9i35iIoovoS6DhEBh2GgvC6jsb95vvLaCHdxxP3Kpt1K7hMGQxkocM7mRGdM2QDKIoFJbG6gf1-Ru_suCWYxM7aSub3SiZGc8Pn5zYXoL0fk0FtvPIb6OsrF9QQrpMNp8Ybc8iF_GKeu9ATI_qheyoup-iZtbt13F_whWU6njHL-P2tQAwHyLY-7y_T6La9D5DkAlIzWTJmsSSKzWjMfqD8e5x2P_HM8Q9qI4bZuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=i5ANw7iNecT3jaNRTDD5VEsF4mXDF_kszAjiLaKmmoUnVmFuxZaSLOGQRX9o0_MHSl3ReluOICyn1PNiDWz3x8TsZnBgMIi61zhNz2LKEbkACNWMrU00JH79jkknO9jWebF4ftunL7XuegGm5nN2WktZSfB-aBclVrfORvIQIex5A-IukGQcYaYWaloUaIfKbbIQa2uCqGpQs01EJwiQ7yQ62ZhQu-orz_QicN5SW1e0QswwPPtc2uusqpSb8hAiAzA7Od4pAJSHoWFjgKH4IwdlHYe4ceTHQQgbIk_Fp8mgbsQGulxCSRtX1suSog4vj95ynlwLRuwM2M61iPEffHhpVB2U3IyPTVv0Cu3xg2EC1Q3RmAmCtkeUh8iFl8cAKlVewhrtdmVDHQ0PwfhGdzIViboi5wH8NqqCx0VbVCdH154cGdhykcNJ5lo3W1x3xqIRoG9g8v-uvxnjJuuTtziRitU6Oj7x1El-TNSjLnG4yiBHwJP-kC5hy-0GnZBtMxROmPUQlfxaRAj1EmWw_inlMt3rZI8kK659wpY6W7RciUbYc6fJq_Qk_empApQqk9sbur2eRqclY1q5WhF4F7Y9A2ZbAs2CmN3k0n2Qqab5q8px8SSNghKlC-ZyVwgQSjXJZHieYpUS9PoOtTxdaN9o6ihhsKAoDGEwSuXu-ds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=i5ANw7iNecT3jaNRTDD5VEsF4mXDF_kszAjiLaKmmoUnVmFuxZaSLOGQRX9o0_MHSl3ReluOICyn1PNiDWz3x8TsZnBgMIi61zhNz2LKEbkACNWMrU00JH79jkknO9jWebF4ftunL7XuegGm5nN2WktZSfB-aBclVrfORvIQIex5A-IukGQcYaYWaloUaIfKbbIQa2uCqGpQs01EJwiQ7yQ62ZhQu-orz_QicN5SW1e0QswwPPtc2uusqpSb8hAiAzA7Od4pAJSHoWFjgKH4IwdlHYe4ceTHQQgbIk_Fp8mgbsQGulxCSRtX1suSog4vj95ynlwLRuwM2M61iPEffHhpVB2U3IyPTVv0Cu3xg2EC1Q3RmAmCtkeUh8iFl8cAKlVewhrtdmVDHQ0PwfhGdzIViboi5wH8NqqCx0VbVCdH154cGdhykcNJ5lo3W1x3xqIRoG9g8v-uvxnjJuuTtziRitU6Oj7x1El-TNSjLnG4yiBHwJP-kC5hy-0GnZBtMxROmPUQlfxaRAj1EmWw_inlMt3rZI8kK659wpY6W7RciUbYc6fJq_Qk_empApQqk9sbur2eRqclY1q5WhF4F7Y9A2ZbAs2CmN3k0n2Qqab5q8px8SSNghKlC-ZyVwgQSjXJZHieYpUS9PoOtTxdaN9o6ihhsKAoDGEwSuXu-ds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7lSahKfaIYQLS-iwK1k4KPoLnMYnGyavzABwIePe_59hRDwG0OTIyahAiAmpOjftFHiojSELqCfAXE732hrCDbmZi0qGX7zGy-2m42xaLwkKT1Eer_XWfZCPux4yvTFb5t6oMeuwswaVVDv61lZUb_kWIABwhMu1so5jDk_nTZIKea_Gk2kMHTUjkMyWe0O1kVS-UcrnYWlhcLH05aUkZa2j_rDhy1LOmETuXotyEppNW74fX_ZklMHwEWACFiRdsacIo-k4iT0RDiKkWQUm9AAPhADlwhuoR0qTT5AIg0aVirgoDMqJG1-nSbhn2_ac_KxaVoLFVPwzJIxZRjy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv1J9Qn2mgMP0Xn3k3WRDnbOtvsVWTCooSBvjn2I0lDfJPX8eZVL2esWVtPIbBymwNAoUgc1fIngi6k7u2ssQrm3_dlDm-uvMATHkD8ST6kUc22uGfmWc3FSRqnH-bHX2UfNXDPXeP6D3DnIK7J3Igtr_nBGWvSOllTYvcwqJYj2_eLnVG8njRt0QM7YKM99nedX1M9BBHZ5refbFL4UOFXT_ISlSUjmeAztmQiqwA3erOdBuIyuTsuw4dypg0NDNYXUv4RxXaSJkbut4BznqCS61_dQ6Dzzoh9AqMSWC7ql0bDKajm4NFQ4DzIM9Xa2UZ8RZp9t1sH9aPHwlrYgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrTOY7NRVTcLYi5uOPBxePs98rs7CfWc6AZVQ9Re11N3QWSwljYt83ODWhh-xjDNIzk43DBNu58FouK_LvWSMwR8VA5a7PtlqEQb6TIgouT28_9-WFblviRSry_Jt82veMd9FV9jE-Ff5hIi1R0mzwY28FdsBdCAQVc6FFxWI-yx8E9uXpddXaOeHUHd81j3rxYolfPUH5kXYzbQ0JEf59fY4LqMsSV3v7IUv6CCgSL9JPoAbluKXxCoAmfMaxkam1bD2VCkxPNQcYnfG3LfKYSRT5QAl--AlcHIPnHFRicJ1fpZnZZoYHcFWCzBYXh01ZUoqRsYMgN22PKzuWQgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwkId9C2_kQD0Iu6euJGgC7_L52BV7QTY59v68Fc8i-tPJPJ3ZQOb11YGfELyWTgAdPBZJLOJP6hg49r1HvNxR5lGTpL4YRUdXa33PVirqyf2DznSpXwHPbqgLJame_rbb3upec_Bv6nJg1izas4GHPUiKXXZ2gARj0dGBL0zkd-LDYvoIWp1C310OE6VMnBnKMCqVkr3qGt-EbrZ1h3iK5vyN-HAsRRtqZ2NLXIkUO0Pftu9OSNk-KfuU9CECK1vKI9V2NPuyRncjPuowef-l3zAVjfBBj-2a8tEU1oYziAuNXih33y-gDmF85t8K6kfBGd_TC5zB6cC4C4aA-lTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrDwpJZHiBUqnKC6HevKC8-xBwhT08b4mHg7I9KlBz-h6Ww28vnl77O7GIU5-5lLeG63d0VJ-_4MJCptIfV9TkM4zDPu_3V5qA2_MS1VdkpwFm_zYKKlrVmau1L7ZU1Lmtxa-vDmTX83u1Y_gGnB42wZ9ev6pg4bZadmMKRSgXm4WCC6558P30IyTYWRXOmbNqRnxpbNMT688IdrKGAoRxP7bCt5PwoQUMRtBmNotumEGXy0qiuqozGMo-qt9X-pmEmZzWqqseqJV1hUJYbzPXo0t6JnFiU7Reunf_oY-s_ihRXJ2pG1pcT8kxFKe8rTVsBRXxKrCtfvj0y3JB6bWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs-AvUxGcfAyDrtulA_IsBZhkf--OuxTIVY_DQea4mY7yFzxU48OoxlXFEYDJohoSfT5MYdMJpq9ncqvGBQOrXR9nkdH042WnmTnx-qxBLnHNvzZ3aDjLfRI2WQY3NJwxxCOhet0KelpaImoh1k58apP0P_PaUkTF7CJoUhsP21mipK7UN-mzUcRkJ5XZtTKJ6Wb8D-2QUBLaxPU0XVXUuAroTKFIJl7W9L8eHN9OkDJsQqUUBrKA4B6NbuNaSxbtmxjmKUbCB-c2-BCeUYBlh_bU8ufAvv9nbrJPz5Oe4_vOcyXQnYTM1OeW5axRFXXmW3fX_PKs1qONEW1kUkF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV-Kc4qZIk9jq-WZ1dsY2JYQ3WubCv-GLc-Eg_x08nFZsDRkEp8EkfW2nBgF4lHu81OCG-j4CDnp2D7ILK1NKvork8eK42ELv2d9Er2-d80XOx4UTlufpvRIbgPKqS7suJRJVqjlqLHhrYhcma6hOEwHcxRjjRAnbRM4lfqAc43tYrdbAcXjPXaZLP15pIIu4p6pwRMzuxmFBRNUPH-JJsDT04XGZqt29mUC2vMZD3OZJIio4cJaQB4ddouFmW2vKmvQKZzsJV-KcPamnTbQHw4gSYDP7NNAyxKroWuOI8hY_eXslZh1znSLci-IHVbkApUIhBWyzQYV9AsZ8Ve2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=L-nwezVk_v_WShhr7AKtKkQcy_1bkMDqsXjR8q-buLjMbBsnyCD08_8HmT_0n8ETNM2EjFkZcJY2UlFrp8egm5c5BEtCIVRWmprPjXEtWlFtRdwbKMpC1Y6nPp8mdpl4CyUbZKAhRIqi5q0LfMgI86SW7H4oZB9MOfWvYt-NIxrNoseHLkuq9Fen84V9o-0R6-2DSd8NrNNaCGzu5AQthhS77pzOxKUyn2HfDFzGC-0qKNdghlstd5-IenhYGOkryArDcNU05XOc2V8dcIsx-oCB5Uo2F0SgCdWcj8svrS7MaGC-sSxQq0vH2dstba8bdIOCdItDbuQjc1s7IjD_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=L-nwezVk_v_WShhr7AKtKkQcy_1bkMDqsXjR8q-buLjMbBsnyCD08_8HmT_0n8ETNM2EjFkZcJY2UlFrp8egm5c5BEtCIVRWmprPjXEtWlFtRdwbKMpC1Y6nPp8mdpl4CyUbZKAhRIqi5q0LfMgI86SW7H4oZB9MOfWvYt-NIxrNoseHLkuq9Fen84V9o-0R6-2DSd8NrNNaCGzu5AQthhS77pzOxKUyn2HfDFzGC-0qKNdghlstd5-IenhYGOkryArDcNU05XOc2V8dcIsx-oCB5Uo2F0SgCdWcj8svrS7MaGC-sSxQq0vH2dstba8bdIOCdItDbuQjc1s7IjD_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SndZOpXnTRwW7u6eoK7wGfOwKc0KVtzU451jykUvwvj9arwqfC6O9_crZmz3EkR1kggo8BzW0tIDRlwFdIG0YoYjDx4dk3G90hhZvIPzTY1NjuRQgTqzvBZ5c_I5aW8rYVzF27m4v0AC-6pOjuH-KmjY4KfmqrEecbrjjJzp4R3yYauqxLwfl86htWYWQxknIHRrYE3XEgA22AUw_UFEZfuOEVa6kW8s7UAIVLu4cU35Sq0dJcBR_tp_HDE8TTywVqPp4538qRfGn3NVOgayKxIfLPlHDUXQm8aUD_riCkUW2mF-GtvFB5BBxYuSyRixJFX45Zt5mmg8Sv0Sg02J7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAKXvQ1pnIbt-CneIajsvAaU-BcM9y6QoXgG4HB0M_dxfyCSSd4hTTI0Rioc9TJs1_zmiA7NbRiFXaeUMShJGD6m5UpVtn3_wm2n8VCTG7BQIuMzfGzoukPvS8n4ibY_NSpIvOoYFHq6HcQt9rHE-ur4VINhiU-MjBCDvsxQZiJl0JQlABBAYX9Ov2cu9Ufx2T8RSvVc4Fl_ldRFW5E2cRpWlcbW37iAEy_s_jErjJWk3KuN_2CY4UBJ-Hxhsenm-zzFK5U7Y7B4npHMyg85Khsm7RlEVLp7S4x1dN_s-W_bor1SprmVZYZTIxSDRVCskUtxXL3IguW-h7zjg-esXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSyu9-oslGL49B_SAsMlc4LN9RzB3Wji5r08egt9psfy21PIfknGWVbsURUKtee1d-VftdntqaWB-x-MRDkhc8ywVvDiAPBl9Rf0i-VtyO0OtwXYJJNpmX0ZqzTXbFzTiC79G6r3LhzMJhdqMvyX2kMhpdFBLOCDr7wOF4-fGrrQAaJIF1gyMkcC1uawzrem6XRtV-0tFgkbj40QDNIt28D7pdNeKNVpmMxnVSVsG_gZqZXhM9iPXQXTJDQ9zUYq4LQETlczZYFHJev54bTqfkMpU0Rpx2INUUlj-iPDuHoV1Piep33CDmsfiz9v75YqE5oASZBZEp2L9lV2iN9Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=joyD8PIHMcHh3KVj3Ofy_95GsCAWxR2bqNLTekD92otVxA04SBv5pTYfHGS98vU6hetNOM3LaQvmehbbZqcV6254ktaeWoXHyCa3W3Ivp2avNs46wBL6gStTlgI4k5BXhzk13DIjCnVCeX-MLdm-d-72upUgPufwgHe8v6OiOsxgIkh5TMlRRTa3Os3ssTDM9UqQybLBwHM8fJ4cwariH6bAPtd8Kea4dwIDl6vSD9XWZn2vKnWoLBUjWTBqtK6vp9fE1mc-GwxOj0h4qWYdu6A8pp9Xk5WnlUeqqC08eE7SXz9Ee2YNNyYH0LugE9ZjNJpZpVA4HZI3Iu70t-H1TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=joyD8PIHMcHh3KVj3Ofy_95GsCAWxR2bqNLTekD92otVxA04SBv5pTYfHGS98vU6hetNOM3LaQvmehbbZqcV6254ktaeWoXHyCa3W3Ivp2avNs46wBL6gStTlgI4k5BXhzk13DIjCnVCeX-MLdm-d-72upUgPufwgHe8v6OiOsxgIkh5TMlRRTa3Os3ssTDM9UqQybLBwHM8fJ4cwariH6bAPtd8Kea4dwIDl6vSD9XWZn2vKnWoLBUjWTBqtK6vp9fE1mc-GwxOj0h4qWYdu6A8pp9Xk5WnlUeqqC08eE7SXz9Ee2YNNyYH0LugE9ZjNJpZpVA4HZI3Iu70t-H1TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT9_Dv3mpLktyfuyrzCECY0DAb3MefrgbyjpjKPjScL9Irp95YtSmcWhgpuK1zzyBqAX13znXGxAIjMmh8qxWG-jUAuv6z4PP9qH_U-vum7F_2xkebviK1tHmXhQN08keXWjYQoUoHbC9cVXW3IBZfQ0bhnYj_1DclOnDfRhl7N74jEl9fMZ4wSV1cMte75J5Usv6eucGFjN11wlS07WopghtsEj4jqEZpkDzJuWw1oeMCEv-aEwDfVyVXayir5V1CAG8Q59fzTzJ-yzvE3IQyg0sNg4q_pRXKW23MrySaP-fnSduZ8R-0HJglRxoplS1KLVk5LeBAeIhNK4VWM7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=nOs1LSWy9hlCKhHiA173hGxnHWOlMkMR98Q6brGV4VhF2J2iRzJl2pofHly5Xmn2EyWvXuO5_5bij6K2i96DFpmSSh0CxBB3m-m27AoVDJKdGlVt01UIbQCsNYAqhztL_WsOa1NoDFfKDJm9EBQdlCEte2vXztV8TU9n4Jltn07-zL1B7ZWS1na78TnOP41qlC0AMJ6-ff1KW-g5fL-rSm-77wAxyEbQnUBAwQHagK2IHdMOhVzV-fXvszVySfAzjvX-mOAVDvom8PZ88wCHMbrfVjZk1InqEvt6a435V16HqwZnlGc3vDdu6Yei-VMkZuoIq8sCce7zrMMeeoWQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=nOs1LSWy9hlCKhHiA173hGxnHWOlMkMR98Q6brGV4VhF2J2iRzJl2pofHly5Xmn2EyWvXuO5_5bij6K2i96DFpmSSh0CxBB3m-m27AoVDJKdGlVt01UIbQCsNYAqhztL_WsOa1NoDFfKDJm9EBQdlCEte2vXztV8TU9n4Jltn07-zL1B7ZWS1na78TnOP41qlC0AMJ6-ff1KW-g5fL-rSm-77wAxyEbQnUBAwQHagK2IHdMOhVzV-fXvszVySfAzjvX-mOAVDvom8PZ88wCHMbrfVjZk1InqEvt6a435V16HqwZnlGc3vDdu6Yei-VMkZuoIq8sCce7zrMMeeoWQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVetdVA7t5D8RqjnZDXCKQmFwdLxyfrrHBm-O-8b5bCn7mDht-3n9iGFHoftJ9nPMCHVwqrIlayKo4B5eR7FV-IZNG2SgfQSuDTZ6z717e-iQXCpeG_YpuQES5rs_lGSsHcJRdrkfrseNLIKvrLmlP_5FDU1HK_eLKj3cAlPCqUWu7jhz1kK7hn2fO4Tfy7t31-0Tk3nH6Rbylq-jrMpuhJ6QjEa3Zosj2Ncr8be5n05XKTfCKw6XcKuOB5qKwVQCaX3lrf0EYPcCTXFFI99RUj8DbTJlGonwiGoGbnza1ayj4ecNNBvvYzMqoZN4zSxrSVG4NFzEjODx0YhogBgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=Pg50woXSU_mrAY2TB7_UHfm6g8ak_FITI1asrn3IGQxetM03g-yPr11XkW8ZO0VGs8QdWa4tzbhU_-2eEGEpw-A86DWMAKFGQ1DzJckQ68E5bolFWyaK7BuYMGi9atmoZYqqS54fx8fimRzxBOoQZ2jaiC1x9PCEq4E-WYZfdndsyGXYEjBPP5dIbtzPIZzKII0bkRSvrrGzRxVPNJAOjiZ8cP_Mt31pZOTAr5-bLGCnxTF2qZgII_Jfe_e72YKvzpz9KVHIvfX4kvRNld0wuxdGyYSBpptNO_xopswVWGjKBoMG0zURVi8TqGLyLmHOLJqQ-IIHPPMUoQjQiOtYHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=Pg50woXSU_mrAY2TB7_UHfm6g8ak_FITI1asrn3IGQxetM03g-yPr11XkW8ZO0VGs8QdWa4tzbhU_-2eEGEpw-A86DWMAKFGQ1DzJckQ68E5bolFWyaK7BuYMGi9atmoZYqqS54fx8fimRzxBOoQZ2jaiC1x9PCEq4E-WYZfdndsyGXYEjBPP5dIbtzPIZzKII0bkRSvrrGzRxVPNJAOjiZ8cP_Mt31pZOTAr5-bLGCnxTF2qZgII_Jfe_e72YKvzpz9KVHIvfX4kvRNld0wuxdGyYSBpptNO_xopswVWGjKBoMG0zURVi8TqGLyLmHOLJqQ-IIHPPMUoQjQiOtYHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMU44SdVSIvWurYYUT2x6O_AclEovJjO1iSL-1DosQpegxuGkSwTasZCbgLskc2cjcheauE8eU3jYOx_jEAA7JfowldP1l41UdNMMzmgEv3CnLq97S9J_EQEZ8SjbowSQFmq5xARDFq0Ia_xttNW3lR0rc_FgPL8LZ-qzxJmnJ9vwqRe3bo13db6ZzULwD-DKc8J1Inh7gxiun7Jla0JiqCMU9atrVpGGfxD3hc6AEJ3_s0XmOeflzAa51-fDrJsRSUQrRWteO8NK6lWSoPK63ALqnwselcvg6-zW5-kUsjARREEphsqzKSfPK4i4qIb6L21iO_T_Wfnd_NDr7lZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF63aESSqQ8skHgpXNh5ZeRtdyhstJVlNE4E3tk8e30Ud5ZgwtTrMiDaGBmjMXTGMsGVZaxv9003zkbg5bmcR_TooHIfto3TbjwGRleUYhZ18E18t5IEnXfs4SUuLhOsj3j6-JNs42HI3emL-bGJwGeAQ9-R6MSl4kT0nGFOaxaSFtnhZRdEXYhoXrZ-1ayfpi9BkkorIvLWapnjeyZKGRU4XvHbVal-pFMv3wc9lHMzKuCnv9zbKd7R-zQ2RrvnQQHyq5Wfj38c7SzXInjuWiqAOPrvSIixHgLw-hwRcmo97Ak7dIaEhqvF7CJ1vpt_OV2G0eVctRcLcEJnp_ahiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBVIfn2Ewh76udgrsXTXf5cCqD2LAXbMDHcUXLg4Qo5DTNtZlx-bUkoIh3uEViqC5F1UsOXmOUpxudXW1hyRL39ozoBYBhMOLRvTE8a5heWJPvA7NIq14UaXTH2u7iGjlCZ1zigpQR9lcMRwy0rvQLOfrv5YZEd2oMP5iZ5O9jue_UH4XQAfDrt4QeWKwiwEq4eZratL7KfV6POxSPXt4sXuMI9ls0KOA_RUpcyz6uXftsMMn3VclAjoqICPLT-Li9zkw87yh5BbXklpacc2_mPAVehvl7xT4PA1QD7szajYCQfrQF0YuiQu6dwAEpkj1I6z8d0tAa5pUaOPjQ-pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5AdvdWdP7G8o8CTXtUwCR28IUCVnDmG8AACBSNJp0oQpmZzNd0VvLwkbODG_yhdp3lgVN-MZTEL7Dou_sK49B2vYsu-PI6c6drKK-OPCLmO2IM9CkLJIr7qJgoy1IKVAgDP2pQzpl-XNnMS1q5jkBzO2ZKbBDHb-b7jTO8emgT_TT8s98YpEHIQuhBM13QluqU3AwiXag6tGS2qqPyIRhGCivrxS0ox4EJs8A6alDipO0Cx9YkbjvNoWU882FpUjomrS2rto76l41C1aTkHgNWN3QkmSzLFu2PfNZJwrKr2uPqQ82KVY41kklAEiGi0tZfVEYIIB4RTDninp0_N8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=fmtd0iIbt1cpqID5PsafHPDIqitrsy47Tv1Att-MqosxbMcMtPsm6cReAG-z9Pz5t4CHAOhZpdjXygzZRcimRWp907zs1tnqN5F4t1BLshItsflbLGn_dEfBKX-cYyjhz8P84XlP-iureOqXdXj91J4cyZTbfgQ8VRkNrOHm3nFrwNatfZrS_MrzDLYKaADGNCuEZ-rxL7ufL7JIOF_IRS86z7mkB1lkGGcCFQZwFWNUKshCShIV-MbStoou6sHsLz54WvcScVVrvsDeL0JXlQfneGzbrLKWMdMhExnXCrq7KA6trMdi1l-gVBy4K6UERFpWcZtcIHtzSbno4U7b0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=fmtd0iIbt1cpqID5PsafHPDIqitrsy47Tv1Att-MqosxbMcMtPsm6cReAG-z9Pz5t4CHAOhZpdjXygzZRcimRWp907zs1tnqN5F4t1BLshItsflbLGn_dEfBKX-cYyjhz8P84XlP-iureOqXdXj91J4cyZTbfgQ8VRkNrOHm3nFrwNatfZrS_MrzDLYKaADGNCuEZ-rxL7ufL7JIOF_IRS86z7mkB1lkGGcCFQZwFWNUKshCShIV-MbStoou6sHsLz54WvcScVVrvsDeL0JXlQfneGzbrLKWMdMhExnXCrq7KA6trMdi1l-gVBy4K6UERFpWcZtcIHtzSbno4U7b0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGJLu-ofBoe8WwAjawaPuwQYN1uuCPOZaMsyO0KgaFgJbPv52VDlZKQ9HOwjXp_ptdSti86n6drmWQuOyzkFrMFDg5_vgWv0vxhwKX4EU0BQWHlh_T4ju1UF5vISau4XlIMVOthmhc1h9XnJW24VYVHSYBCQpf4oZ6aY531nnSPYTYUWKFuVPXqkICRwoh_ljCzYBh11vG_yX0xo-NIc77a3XjdaiD6DT7APufxWdmvKq_V-blAeR1IfKJb37oNkd37-5po2uU3hnTdT9ttw4FARupYKA_CvnOwKxlv1rHN6p4H9dYnI3BuZs49-nTkNBW_ZxseB9WzXfLuVcID3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLAESq479-uVbKF0wbiH0jiEWHU6svifYoXZEWuNpj40ibLeOtPBo-78WzwcWo3QTs3mDkRS08Q2GwNu5moWqU3FysiMV-jQSWsQskVT199ziZuhNlYdxxndWPbNBmvAOYDCPryZ5OOVqqYZlD9x9aB97U67LW91k8vCbq8v24Q4J7R686m9HiZGCh5mijlPBhGTOk3lgVVxjumPqwSs_ZJAjnWTJNOYYyeTPpC6UB8SIqBPKIrx_LgD2hMMBWRiy4MLF5qPoSX-Z2lhDnzFVb42ldu7dvyRrjv7CBbfXQTiT3c_qSGC5gaTOmx5eBJ_T3w72dQ3EwQbI11oKa9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmWuqJZQqlYuGXZbAcO2sVelilDACGXUmpXEkVTb_oesAFqdGYA1m9Q52U_pN2xl5_94v7Cqf403uh6XTIiLDUGvUkolvDxhqEKfe9ooJMNkIE-3e3I504RLOGb5_sntmsyxwSYxFchfUVJ_I_cpNep8zUsS8VMc6Q1wEA0Sh-tNrH9n08L-o9rfVEPSuWD4-X2oS0m216f3CyX3BuKBDahd7V4B5m9KgHJxA0fb_v1J-4qqRLUhwR--DuHfxnKW9ZPD9HuNe4S7pQd_sF-TP_9m_ou_v307nDFtrQ46BWUWyMeGK46-IqsSGMLq0Hxn0M2NWXpoGwouuDCv3xJqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWeeH7N04zK9mdRxRmke29SK2AGnXEEFAP7CY3MEja6-SAB224n0rr_W--1NZtsK1OQDaDzZV6R5JVOn4kSkNMzeoJ3tP0cH2hEO9uzULD8xiWADnvjGwXJY-ZbSSal77g8KRhW9VkdlXq4mJS4GOqvyjd0lRZUGc42oAXUTtIRq4NDqZ4jAQOINgnQQ7DosAl1W4AKyo6MUJvIYaKfNBKd0A-ucNOOM7TT2oV5_D7H1scHVYQ00xzj8WMygl5fWtepKASZyBKD7c69BM0a9gnnJ12riXlxzfF_19bxdD455giWQxAromkgOwIj5jaExrVc0MjybtVCxgk1ixIj_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqCK9bLVbMsz4oVPOJUExcYmNBheoUcY6MJWKjuCoBr6TTXrC--160bTltLKxZxU0FSzpSC2V8OqKXPY6-0TT0oD8gMp0nMQOdruha1tHCfs9Vy2zVL8KdjGGm50or744E2faO9PdEpazkOdcfB8d8k-Y5tmuEgeccMsJzCRoUbiKNwkMeMe_ORPqKCAVhYyKhEQWPgF52iLfsdfUNGXE0Lickc0AwUtvJar-Ee4Ca-jSe755XIlanIaFI6xKl_lxzTYdH1HYM7lenboSC6cDfHp5L8fvo6uW4iPI9_7MB3LGcUdztNNAOyID4IxhAWIZdktWYnseRHcB1GUWqGrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBiZxCi_-jaoXWbq_zU-_JWlQA_00aDlIGbY8jEtPBY7JGYXqz9MZdksAn0E4WnByehb0ywzKDsHX91mQTqigq5jIRN6yU4t_v4gtcDZS0kadQTSm-iIvY88MOrZn_EGy2Ty7er4aZ_YPCU_haLlV0polJV7G8RPq1WVpM0OvhDI7rIDnVkNV_ZImBV1kKNMEsvlp7G9c71PEQE1dJXXxcXvlAcopsMIkmzkIA6sox0SV7rndzHXru06qs1MQeneUnlxKC2xS__pmeLnjBEbbsY1kf-i7tnvuLiLiu_d_190Vc7sGeBCbr-crDc6JGwEBUaJp5JkyzQJnW9r3mJFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdKOqaunFjzoGz0Mue2bMLVHq6rZSLrkOCNRRU1gqDQtcLVS00Hd74MmFuUfw6_eDfwl8r-kJf3H1x9FBiZasCmrmLAYueVme8kkJj7kBrIux2k30qjT7HDsNHWvRn6pOZrFbrj6GS7hNuCfVW7g_Z9BFujKwVUV9o9DIpYzFrkm821yZQ2MBIDo6fBbW1OSku-ximzknmKIQtMyXg4Pv4kY2eYUBhkL0WE7cn8Ufc-dFo2fTJxJ8B1C2xlmjWuwGfNco5G9__B6dN17iD-5AGYzfY2F5txyEhpZ3m5dhmlbd5zg998Pv17_bypd0g3eFjG-FbNQ2lXEwu3k7itqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmtRXmz1geRh34iTR17YxnF8tLUaV9KLHmDq0lNhmOlPNaNfN2ks90mw1k1T3rI3W9R1NXFykZiz4-WNYTYj9QhOfenUn2a36FxnDVC6VUenx5LCUGnBN6Ri8ZtcUBjqXfGr8rjHS7MICwyJP2rihpsTJlcGVV6xbDi_TpU0hQ2cqg0xsNk2YILfKMZHNoBuutP6a5B9juR_Y66aUvczdD96smDgovjnSUzaURwZqHYQ1mKRXsJ7eQBZGFATyempPyXmkF2EgRv0CruxpioqCnn_tpg0bAgQs1CSvyYut5wzbLAyTwX6_c8KauiSwRFnIUnCJqPONfItPhFvxQJbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seS2Y25QYTAuSkFGrwo62003A3vtNMGRYFGw4chJ-QVdZa2a3nJ1ZUPvES9YSUPVO0gHvLz7x0mSiwbsaOyTuVbihECgYt6bnVOYQEDssKHpzuhR7GtLT9SmDBxfBwkHy3oLxOs2sJCTKaExptLStAMWK5O-Z4LI7VqF_u-fzzb6GitbwGEpHPOLeIDqvcBcBGCE3t3szct1SzjgXvWZDHY1mOPlubGXsOPi5iW4Nsok07lZfIflHjgkDt3fBJUuEYyhDdC0BzyfFrYQ6fE2i89j20Ph2JMHGU5svMi6CMJ7QluYoC7Kub12zRTSndP4MJxt_2pKfSOm8A3MX70ZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcD9sSMSHyUnqmCSqMfUWtDBdmMDWt1LnUZqv0qb9PrV4o5hvqsSQg6mRDA-0lD9LAhMqjlikCTb8Kq79lauBlc69WrXgqWH8WqmrjukKReylZ3gS8LyHKs69G8WT7MB6rue7cFztbnSjop7TJ-eYO2gEzADM9rzHIwOCIPdnVlQ-ebNJNxXWXWThgQrvRQLHS1UERJigZ1usS7A3sYzD0FbCjYrOaGsQnB9yT-XyQT6jxFmJjfp9Lz1Yfp6p02-LsUJa4h3lQbRnkThHcEBc2Pm1QoQp__4eQv-kMn_TUamfIOBSCC_hLFeYHkweck1fsitiPWW5DiKcGqDEL-NVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9bMvJ-uQYkFyscRol6nZO5srHc8cfj45uo1S9K31BkODvWeC8jcVtlws6tR7Mqjc65POgke_LHA0TPTdqDQhu-5k3VPjf-nP_Tmttrq1Df8whswa77g9W5ubP2j9mLK7IgZXnLPAaS9lINRjiGwzBabRivtSMv3XWxI_zJ9TssAJYKY6p2lqXjv7KIvOpfXUlILlA9DMRieJHy9YwxK2RRbrmDQnZ87D2Wv8lWoSmLbQpJj3Llfxv2PxYvXYLa8um5hxSngX6MYYvfsv_YkGrPLLdr8o5e1fHaQn1Y8oCPQiZFxjjKSW6hIaQ6faw2VHhmzkkjlXndncvBJQou4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsEJTuUaTgHIkpq1eFORprteSVeC1VgzL0c7dQJpDI8IUAMcZWyKkHxBykRaHrq5WHONPa4LXbruGDE0ug1AQqN3AD3F44ww1C-e80_-5oyp0Y8FVsfyGF_BbiAsNi5c-CPsmdAw6s2BmJOPtk18JSSUr4Bdli-Rc-uI8_hxbK97dsc0ZVA5unwpnihlFbeWXSb6_cA5EMNsK3dfXFq8JK6ChsCPnOrGpN3grq8Jdn885c9CUQAHDOXAQx-XvNkTytnGXWZFcoXCAxwDhMulrrI_oJOR9CHW9qtUoKVyAHTgXsEt6E0aIaymqSZkr-4VXDFru3TjD5UaSBVpzDEfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ4ctnveOAyvlVlV5Nl0w-uEGjvc_ypNqVi2QZxPC_yPvXzcJ87IuKSsEfQgBWL1dEhlZBWNN-MBlv6PORBEPFQklH3FrFq4kLnYIyLpt6uq_-IazmgCDAXmDn1WAzdu0vbvi5VS6veb5nd6VXKoqlzvfiC7NAyI74H5VKxWF5vdFGJId1Cs-KLSwDBbjNElFsfWceNLHposK1GpBGbUC_7_Y8PKiaofHIXEoFsC3iTwoESmo8DuId4ZquaYy6Q16it9OhyHD4zjktKREP_lIpX1vXJndHNYGKcUoJDrbOHt2H9_1RhLjZIgWEy35GoAM-UxRa4439v8GyjGmRhJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=hRQOOPJ42S3rChCSj95v4sPZhlQxiEeAI1wzpoSMN214xpkyZ_sRVwp1JWro-kgtl2E5Hw8q34mSZ_PHNoPtAQQws70Zc7t1hAZrmK2stXEgoKJ6nbW0XXu8YJrfTjk298T2--sTWDTEtEkbQz4tzx3R8j3wZCz262OzbouhMAQM4hJc83eo-ihLn3UsGz19hqkaKsbK9ujBVPMO7LQyb2Oeo6N16wAkD1OJkhXjh-OvI9frtGljVUf7B-Ii-7cR8qv5MJt2TXIdVie2SHnwcA0mhmbejI2R0EqQCSa-YM0hS06g-r9NatF7d9QVtVZq7nROBRhC8VO1yOK1esiJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=hRQOOPJ42S3rChCSj95v4sPZhlQxiEeAI1wzpoSMN214xpkyZ_sRVwp1JWro-kgtl2E5Hw8q34mSZ_PHNoPtAQQws70Zc7t1hAZrmK2stXEgoKJ6nbW0XXu8YJrfTjk298T2--sTWDTEtEkbQz4tzx3R8j3wZCz262OzbouhMAQM4hJc83eo-ihLn3UsGz19hqkaKsbK9ujBVPMO7LQyb2Oeo6N16wAkD1OJkhXjh-OvI9frtGljVUf7B-Ii-7cR8qv5MJt2TXIdVie2SHnwcA0mhmbejI2R0EqQCSa-YM0hS06g-r9NatF7d9QVtVZq7nROBRhC8VO1yOK1esiJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbLfh80pHcrkTThH0-GpHS0HACLqmrD-0lw4-4oxh_lTG5yCgYL9nyoDf_3crTIRyNDCJN64Yp_dGx9ALDw7QdWZyKZ_rK2mQdXpvnDfni2vS12w9jlXyiRaCwe_dbpcpK8EZcRYtjCDjnb4_OCIgPBrL0B3kGKwn-AmRWJFsFaI1yDPk7rpGLAVPTB2niuIM6PWrWXb8a6Cud2d1Hpx1JFB4N4P8IJq9aaS-mvoTXtQGiHvbu7dvMC7tUcmCtjZoVRlLPb8qqMAnQmh_AWLpTkUBTZYsxU0li_c1xIB0d7SVMVey9_LQKLNX-IEIoOWPoCoILOqEpKOEwW_Tjcs1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIbG0vEXMf8WJQbpYa1Os-D9R5Lr-Nlis86EgH4Pd1rjf4l6MdYpmacF1gH8kF1mvQp4Gr4clgiX9YWqS6z0i6V3r_xg81zLRcYS-TeLp2SsOivgFB0QUUrsLXfJ1_SJEhkat3nPDU_j-T48M4aAt1PIyzD-MlgTDksmfQj_WI8x2OVRAn58CyUmXxtvElx-GW5tg5iGdPgPPIl2au5CJzplz015sLY7ONE59guGpoxtpgKd1UhHwHd_oA_JR8ZMZAQhLOOBCw2dDpK5KuOQVyd7B856UcUzq6fn_rgb_iR2Fi1X7YfAbk8KrqfLn7rJrkriTi1_PK5LME42zJhuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=AAANuun38USAumYsPlHJxAAGuZiXfTf_F0bkYvNw9cTsHg7bRiEZJbWaxON4ypcdyIfS3I1grnDftUm3DwjJK64Va5ZxR-6p0KlJvyYgypTu987a6vhQENFfaEEe-97wVH7CHaX9Ser_sDTkhQnhNgs8vJjrmLLgg88w5Jnj3Jwh97UziOMLWCZZJpftQPGd_e66VsHmgJgsTl83kk1lzXt4KNDcgWA9IHaEmFpHAkDPNltyStQDf9DwZOkJ_VQOt_Dk-CZnzmDjuYm5WMOdgiHTmiRv7snt7VHuP_F1NQ4McXa4WuEGh0w6wTrvuTdn-BeNMncMeOJhR2OY3B-8YjJSojSB-n3MSHZxsYbaPfDIcdTNzC6M5SyWRO0TgApwUPv-LoX1AeFU5B284gZwRVylMS4aCB3h5CaDjQ6K8PymiaMb1GCuHhV3hu29kAu4W4x6F1piFi8DduMK9AoPHFwXPnAN6IsQYO7QAsINoB1vqNGtX1pTCf3Cjh9X6eOF0e67mdUzphYM5y4jmlmFhplQjQjN60ReAmGAtOoNh6fdgVuTNucSelqCwf8mhZHWDIowb8l71mSPATcx-IuP8BwuCN1p_w9VebYTBEaRZ-y5vwENYOuP5aQSacNDTLV1cJE2i2Z6eWPgHL0E3InV4TQKm-K_Wai2BEyk2kJQvi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=AAANuun38USAumYsPlHJxAAGuZiXfTf_F0bkYvNw9cTsHg7bRiEZJbWaxON4ypcdyIfS3I1grnDftUm3DwjJK64Va5ZxR-6p0KlJvyYgypTu987a6vhQENFfaEEe-97wVH7CHaX9Ser_sDTkhQnhNgs8vJjrmLLgg88w5Jnj3Jwh97UziOMLWCZZJpftQPGd_e66VsHmgJgsTl83kk1lzXt4KNDcgWA9IHaEmFpHAkDPNltyStQDf9DwZOkJ_VQOt_Dk-CZnzmDjuYm5WMOdgiHTmiRv7snt7VHuP_F1NQ4McXa4WuEGh0w6wTrvuTdn-BeNMncMeOJhR2OY3B-8YjJSojSB-n3MSHZxsYbaPfDIcdTNzC6M5SyWRO0TgApwUPv-LoX1AeFU5B284gZwRVylMS4aCB3h5CaDjQ6K8PymiaMb1GCuHhV3hu29kAu4W4x6F1piFi8DduMK9AoPHFwXPnAN6IsQYO7QAsINoB1vqNGtX1pTCf3Cjh9X6eOF0e67mdUzphYM5y4jmlmFhplQjQjN60ReAmGAtOoNh6fdgVuTNucSelqCwf8mhZHWDIowb8l71mSPATcx-IuP8BwuCN1p_w9VebYTBEaRZ-y5vwENYOuP5aQSacNDTLV1cJE2i2Z6eWPgHL0E3InV4TQKm-K_Wai2BEyk2kJQvi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBYBVrC-Q1y07375-qkyopso7Y2dPV84-veGCfJ8AkGFEETsMF1OJIR_UYGBsS1OK6nhrSeou2D1VqYc6Y7CeErlgTaWEbUuyCNLWuOsvUkFS9P3l89Sk08eP4it2XOQystZUVDl5gE0Q3LpY6buSr6u3Ko8LU6z2RfwHou6YepSNoEH_6EVjAH2pDq6-B3sQMxKN6jLJlwz7Go51cWdX5dv05ZZEtXRqnWScw58XU6Of7asNekOofkToYhQxm-fJCFIZy6hZju6yok8cXXbm0qvcS2_W-hcnRYNQHdGkGKZLqf3UHS45ywjhDQHbPhRS3RMzLNG2TNItMVa7Rppiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=O0dWgW6C5aKpXOvWvIVEvXkTDsko0PchQxaiwNun4K2OqQhQcsZze5hRkxyxW32-q42mywnVEPBFHhgz1kJZ0JrD26jB37DayXuS4yWxxlFX9vXkj6Hn8o8K4oD7RCV9F0WO18uBzpS7xdP4PrOo3wi5H7-bsyQtYuvZl-_t13ojkBWom5bXo4pbz_ySD_XDYCMd7b0OO8JqB8LRSIbxHZPzCO601EffEAbJ1LpCFbNzYGSSXKBRE1zIcAi-9LQwjsHbbUGMo4t5tFion9_352Dt7w34mV4MSls5iHMI_d-PTKz1nQ9R1jE25S-Mdy1j6MTsIhXIjCwsoq-1BqXul2p3u55DEYyfxdnlYdMCZavNcFZ7ZOsitGZTwOHQpJN9RcZjWg8Yt-Tace1PVe9ZGfvOUxIH8Qis_P3o6jMTSaUhXZKW7RaFPwktMtM7FAxJq9DHya5SUz9ih7EvlCw9UkwquNWo-SeQuh85yoQj7QCAK9fqwREZkZS5sTbEu9na6S46b47JKII96jBGNVhoTsrVxJ7FVZSH6bPq2TenJe96_3xRF-di23otBn9K3Amb9q36bgiKJ46wUPwbamub32CIm9eUQDpySzB-eV90oodkl8zMU9gbhCdBBdYNYwuSMrLj-r16hrf2DPS3KTU18kwUyEmPqZoG7_syGqLkPZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=O0dWgW6C5aKpXOvWvIVEvXkTDsko0PchQxaiwNun4K2OqQhQcsZze5hRkxyxW32-q42mywnVEPBFHhgz1kJZ0JrD26jB37DayXuS4yWxxlFX9vXkj6Hn8o8K4oD7RCV9F0WO18uBzpS7xdP4PrOo3wi5H7-bsyQtYuvZl-_t13ojkBWom5bXo4pbz_ySD_XDYCMd7b0OO8JqB8LRSIbxHZPzCO601EffEAbJ1LpCFbNzYGSSXKBRE1zIcAi-9LQwjsHbbUGMo4t5tFion9_352Dt7w34mV4MSls5iHMI_d-PTKz1nQ9R1jE25S-Mdy1j6MTsIhXIjCwsoq-1BqXul2p3u55DEYyfxdnlYdMCZavNcFZ7ZOsitGZTwOHQpJN9RcZjWg8Yt-Tace1PVe9ZGfvOUxIH8Qis_P3o6jMTSaUhXZKW7RaFPwktMtM7FAxJq9DHya5SUz9ih7EvlCw9UkwquNWo-SeQuh85yoQj7QCAK9fqwREZkZS5sTbEu9na6S46b47JKII96jBGNVhoTsrVxJ7FVZSH6bPq2TenJe96_3xRF-di23otBn9K3Amb9q36bgiKJ46wUPwbamub32CIm9eUQDpySzB-eV90oodkl8zMU9gbhCdBBdYNYwuSMrLj-r16hrf2DPS3KTU18kwUyEmPqZoG7_syGqLkPZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=t107ObJVDindWkvIa4FiUGTXwrXd9AzZqDNYawKZqpF8s4YCAnWhMFZVD3OGOEa2gJGvUPcCH2q0lT4JuzMx3PO8fmKB37NDyhAG4uvZKO9oNp24crp1F1eJ7mWYCCvIGv7NgnzyxsCJ_5oWjXVhic6TTof3rHrGHvWptovM-u2KghFtt2vCcKtNlBIqaXV9ohx76PyA6nsw0sI2YOs781vuc0xH7CD1-0sdkbSr-KF3UBMEzqA_yvGXIqDXVeXJlr31RH-xdSNtR33aBrralrr42SBNavgbBMbmEKHDN_m6LuWx7osGMv8gRkCfnfwVByTXPo7R6-wwoDAtBk2coQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=t107ObJVDindWkvIa4FiUGTXwrXd9AzZqDNYawKZqpF8s4YCAnWhMFZVD3OGOEa2gJGvUPcCH2q0lT4JuzMx3PO8fmKB37NDyhAG4uvZKO9oNp24crp1F1eJ7mWYCCvIGv7NgnzyxsCJ_5oWjXVhic6TTof3rHrGHvWptovM-u2KghFtt2vCcKtNlBIqaXV9ohx76PyA6nsw0sI2YOs781vuc0xH7CD1-0sdkbSr-KF3UBMEzqA_yvGXIqDXVeXJlr31RH-xdSNtR33aBrralrr42SBNavgbBMbmEKHDN_m6LuWx7osGMv8gRkCfnfwVByTXPo7R6-wwoDAtBk2coQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdP7OTr9tYCDP7YmaSad0tvb-GJo1UVLBYBjHK4kuvHFoI0VDqkhTTIkD5uMFx8E0TsNG0WGZw4E-HmwEpFHjFEBMazoFg4HFhyH-TSjeWKKkmYp6b_FKYryaigXCowM2vZ2HjjRph9jXtRU6DkBkrToXsY6RvebroozI5Yk2J5UVhxaMkJp3hwFYBIphrFVyZdMNTntUqV6GzKVzV1at9EgkES9Tc4zkBADj21WuTbIaOGjYEWeWWKbUdOJQ8FX9PrZZCPVm62As7cZ4tewtetuQC_Mdh5xoALfGD9zURhcHyiyEOh6pjt1FAX5iNb7Jj7oE9mi5OlUzCK4jHQ6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrsZj8b59Ty1hHR6gxb6SDrcqLw2b9ss2rgAOFBKwEi4iUCH-kK39MMD6ERxZee1QbWNjP_Otrh5MxwKMNM0SCEvCg6soOphZgyLMo5bEOYRBY8fXjFGVGEhXyll7weKuKoWbNnkPU-ObCeHFmviXYfxPswhMNVJyUptG7ekd6vr_IidQ30Rn9-c-ORUUOJPk-eLkw50EIckos78C2ndyb8T8sj88rcKAAq1j7Zvku_K_7AvbNZ0GYuppDeQEM8uk8Qf3CxPHWvp-OSk_YKq56vE_sv2f5ZdZMLW1GCXvVDTb2yVQ2UjK4kS7Aw-aBCGvALZPlrCcAbw_muwX_eoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiMY0H4tR3xSMpqFPplXWuHMHw3cbn7xkzn4Yp87Z4rw_OjBDVCnXzBPvx3Lyo4v-1ZgRnzRgEFgS_ZRc3GVRzMGTQnXpKv0G7hV2gJTnhfHIFkQSfFC_P1fd0xVyb_yG1Ccd2PDeiwr46ELlLeSwTsaeljC_sK0jQd8TnmZEBT-OwGkT2mHwONg8rbQfzQasNsqpua0TfvZtfBRy_iv7Cn6qLbnz0PsU2whuVJRchJONk2e79Jw9T3f2HoaL0uKQplkbCYyYsQ_dlCS5fXsTu51l64ciOuMTUayfnoBGJaeieiiMyKnm41AQymOPA73SK52UHv5cDD4iaYeVv00Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-SxY2yXaM8f7cKqa1xq3Q3xYLCuhWtXFzwpfaGlyxMrEDovWzsCHtslXcNt-8P5UGEoASMVQ5D0PFtoP8oW-gGhsCAh3VkMP6OcPnuD7HUxbgB12EWkEhtlJo8v86-l8OQ18PBpnfpBxwnW9_PCHQm3zmEkSAW2r65z77x1UKawPOj4Pwr-DcwEvhr7EQuPR-NYtClyS_cDVivT3xS0slYS3Ml21cXOQDts8SiTeJepBOXdU8xKuJbxxQz5QXySVg_yT14YiB74NvyO5F7ufojptaoyK6g025VV1RGSTqq8chudsl-d6k4vu3FDlNwEJw-BQwjODOrthmlkK_Qi8VfO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-SxY2yXaM8f7cKqa1xq3Q3xYLCuhWtXFzwpfaGlyxMrEDovWzsCHtslXcNt-8P5UGEoASMVQ5D0PFtoP8oW-gGhsCAh3VkMP6OcPnuD7HUxbgB12EWkEhtlJo8v86-l8OQ18PBpnfpBxwnW9_PCHQm3zmEkSAW2r65z77x1UKawPOj4Pwr-DcwEvhr7EQuPR-NYtClyS_cDVivT3xS0slYS3Ml21cXOQDts8SiTeJepBOXdU8xKuJbxxQz5QXySVg_yT14YiB74NvyO5F7ufojptaoyK6g025VV1RGSTqq8chudsl-d6k4vu3FDlNwEJw-BQwjODOrthmlkK_Qi8VfO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVMX_Q_uDNMC4CBjrfF_ywH_gcj5sTcYGnvu_mHzfUCRGv66jEQ6-tbe67_qpKstxuzT6VBvEK5ZpsbH-dUkhaGtZFLAryPsDKV8nBEPqM0jpM6J3lZlL549AyIcQiIIFf1J-HKYl5XAlqoOiqKn0rkMc40KRCI8MaKmgivLupEqY44pTL2dHzDL06CE_wszxxBzDvH1enXiPsjM5o6AaisM0S06Cai4lFHpbEkFUJDOSHap1BbWlUg2HLz5BunnG-9hyL2qVbxLDYO7uBExj6sK4EH-gRh6yyZN2Xm4fJuCUxAo2J2auCU5bP5YPmeIOFp2vXybUd_Xm2Nnv4S25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADTdJXO15ShG_U9rpGcuQJQBBEoqsd5m_p_3GHJgFP5K8nzrb8zcpDAowC9p9X6L1LuVFyfsSdu9uHU-nIuF6crToOUyeb3V6Oh-VUMACwzYKH0XXHGhbzWE0pcho_dNknFDNzn3EI5jrf__OL50E-MLPXfcph_Ql7KKf2IpEn64jo6_Dfn-fZUFjX03DMCInbBx3ZwTqZGL2WeafTMHU9fnvnsQf88jHUcy-2S7jNUqXtNXwYNYGo_Br_2oEqb-t0K8UpO7Ra_phNQdBKPMAlBdAlvBNCLhCoFHCbLqluo6awv6SeBI55iu9a5k5qEzPxlDUvjA2ND9xf4ToegPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJQcmjeZIqgrZE0alS2zlc81laKDfm28q_FiYmnBDJBY7rxUawwNuM8womTkEp8K9k1yEwOKD6E9RuI3OffvUu-3ZiY1zhtj-u3m3bMTPIF0IKZfToY0L790a_j41aUUnWszlThXxUN6-RMofS37moUffvKGR1PGc0FGGIm7Re8MAZrqxz8tZ1QhSzdGjylcgYuqez43vn8Lo8GSaEP4SmVmAgX8TXRU2aBEndMgvPmi5BN6EQOJhx41HOxOB8UvnFGX-_ydrBJK24s-Jpos8-er1udfAeJSlIBcYMBsGxNIK62VJ9scAPOFtXOP65_byDxd7a2ilHNxK8C5h5F1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CK1c9dcpuGbRfglvr-QjGtGcugmYe8gphIWVQtaELKy6gK60SI8G2rss3Rzpr_BbrUxC6jLCm8QyGVQT7XV9QIgtXxsvu02GC7yxIswlF4EakupQI37ZxFXlvoEJnE1hEIHCMpj2B629MRsbj35L0YAlohMMB3w1Vf7C1UWcpdy31xuu46WDkIbAQytgIzN3e5oozm8us9jeKXmX7EMOuQuqgCP5rAB3Qz9KUKddn3G0SQhODY-k74Qns2-KupZt3ycE8bVW5nyakMS6ePketDesGkyNsiNBB-FK7Flyb0N4kud10o-k6O9QqHEGAKdeAouVFTk7UzeZ-4krwLrLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kB1lXEx_0INZXR3CEZ7Y2JkVjAEqyFqM7jNf8G1xAeVLnGTjvCOifGZr3uNDCM3bEBe1DfLPdoQgmjGw00T--lMulwsUoRZkxlw-fMPhQ84mKORilaChvMKjQTQ5CGKkb8cKcpEmlUiRzzkcxA8bB-nhKcW-E36LIOC4V2agrW7qVWCVzlwH1PNgS9kd2wzH8DNO5oZFlRCvUCQyvGNXhby8CTDkGBIBlrpGwRXgRRam-Vm_VBPak4jduArGXTRf7a0LzcREzvAP75j19a_GtpEXVXrUyc9JrC60rStyxwxH2KXpS60JmPqe8p7w_xwqOnZriusiiEPMrrYYXlyaRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=On2ZSHfJZ-Qn5O7ZdY_MMiiHRb2_nSU9OFT0uyOklDjprC0tR0_i1YRrOYbYt73GCDl9jjw2wWo3onm84PlpV83rGsrNEZNH7CvHjyCkY2lnz10tOPhW0mDH-TKVU3n8Yvj_a8jOJ7sPveWIvsw_vmxGWlucjzSTRu89gqro9JvSMHzsdAx_az82SyTUwVqb3E7baC0QBCiY4yWpAhpRm35bHRcWdy3_8X8Fhhqj8scyUpk7pip6o0tLKYTsn7rlxHlMwMBI2X0TwBfyqIQHunfB8CgVTfK8HjEJH_vacdcqZOep9GMBF2EmSUPeRNg0tgqGEhAtmtPcSeF2yOmVICMWwfz39GmayUvJo-LkrBvjKHmPbw7JlB6fUJ6HY2YuxDbyeUKJ9YrETxMqXltFHpoVoiRi6hi1M9TBCjkviHdIv2J-8XM0NtFpG1jVPv3ufhxXmTDcFJOkMgqnUVeoIBjeCKD-kUsLSWJpSobTQcfu9RniEtI5dLDZ0ODtsKalSwLtno1IxWVOlAxUTapkEblcBPCJIOEUJtx-h00a4fQ5SaFfid66yv0zz3BaN1OVm9I6HFHpGEtMYxM9nBaJr3ACptt7Tj3KGbfOB5sIddGffHTEbF_0mTmSWSNcorj7t6Ue5w477w0Hq9o4IdIisxZOXUzEwRmjieQHJAKDDsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=On2ZSHfJZ-Qn5O7ZdY_MMiiHRb2_nSU9OFT0uyOklDjprC0tR0_i1YRrOYbYt73GCDl9jjw2wWo3onm84PlpV83rGsrNEZNH7CvHjyCkY2lnz10tOPhW0mDH-TKVU3n8Yvj_a8jOJ7sPveWIvsw_vmxGWlucjzSTRu89gqro9JvSMHzsdAx_az82SyTUwVqb3E7baC0QBCiY4yWpAhpRm35bHRcWdy3_8X8Fhhqj8scyUpk7pip6o0tLKYTsn7rlxHlMwMBI2X0TwBfyqIQHunfB8CgVTfK8HjEJH_vacdcqZOep9GMBF2EmSUPeRNg0tgqGEhAtmtPcSeF2yOmVICMWwfz39GmayUvJo-LkrBvjKHmPbw7JlB6fUJ6HY2YuxDbyeUKJ9YrETxMqXltFHpoVoiRi6hi1M9TBCjkviHdIv2J-8XM0NtFpG1jVPv3ufhxXmTDcFJOkMgqnUVeoIBjeCKD-kUsLSWJpSobTQcfu9RniEtI5dLDZ0ODtsKalSwLtno1IxWVOlAxUTapkEblcBPCJIOEUJtx-h00a4fQ5SaFfid66yv0zz3BaN1OVm9I6HFHpGEtMYxM9nBaJr3ACptt7Tj3KGbfOB5sIddGffHTEbF_0mTmSWSNcorj7t6Ue5w477w0Hq9o4IdIisxZOXUzEwRmjieQHJAKDDsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-KIM_OS1Tf3MRSMGqP5KKMaxTmISDGHIre5SbXSvHk__Dv1j0qbeA8z3e1xY6yjfdWL3MoE297u0RV-jRw2m7iN-HyFH834wxa0i4ZjwMcI0m602h-Nt-UO1KBfW0cj2cdHmxn1HD5KEMF_vt-UiWoJ-5qUQrryId8DywNsF0qMq7O_o1xxUZOX68kGGr8TfGh9-HgiS4LZgp97YE2kj6KU9vd74kBVzB-DfszsMsOkr-ke3-UCbyxZ5AsxMdiYI_zIvOeWVHtyhum0Lix1QhgZboxIPRP7XdXC_jhEeKZeFmHIkeJ2hqKNzziV_NwTnkvKNGs6LNRhlJeMD2j82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=CDwATw3FpK_kxB-M6PQe-XM4fhsg7HKBFEFn6c20yDbY1Jy2xZQxbqYuzdQ1BEoaYNx81CNn7MepQTZPM3xjNbfAvt-exTUYGuRay1T9HpuyjwacMi74YDzLs6tCaaQYtD9sJKBWBogq0IpFbIBOW-V2_i3KN4iYqrmmfAFEOWmvLfcUnx69ZNHGaLbW-VcniW2FNfg9Fne9nrnPmhhqld3hs7-_i6UrtS1FVn3ytYA9sVfHLv4u-uaplB_vU3hFDXEo0oiwgnmFpCVci2hvjT0IfLkQYvYG9S5qsgrm6cIe3ffcOJh4txL7XoYhv156ZeMjW5jxnAbf2cYB53R51VNonF6hAV4EhzTq-3DOiwUHcKNpGqTULb9xUD5SHQfL5Iwo62TcQK3NPtGdZrQsd2vM88eaNohqp0iY4VY-bG3PK09FJ6bofTm3bWAh07HHBZrpwNTs0Kc2RtEev-2sBnjdOnrQeA40CTXwOmGlrpFjBAy8wP6fihAtGD0oT_9bW-wVNaw8NTYsxnk5whjCCjYwXBbaxyPoBnvxE1LlZ-HiyBQX2xk4dFdRFWqwuWQsBKo8V-5cxq7XiiYl07ag2_9zbuZSwcF3FAStU4B0ZJ60u0LPwLpjj3Ax_7s33_9ifWbJ_4Bc1_lth3JE0ERybx6dEcE8j7M9WOyHyOoLwb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=CDwATw3FpK_kxB-M6PQe-XM4fhsg7HKBFEFn6c20yDbY1Jy2xZQxbqYuzdQ1BEoaYNx81CNn7MepQTZPM3xjNbfAvt-exTUYGuRay1T9HpuyjwacMi74YDzLs6tCaaQYtD9sJKBWBogq0IpFbIBOW-V2_i3KN4iYqrmmfAFEOWmvLfcUnx69ZNHGaLbW-VcniW2FNfg9Fne9nrnPmhhqld3hs7-_i6UrtS1FVn3ytYA9sVfHLv4u-uaplB_vU3hFDXEo0oiwgnmFpCVci2hvjT0IfLkQYvYG9S5qsgrm6cIe3ffcOJh4txL7XoYhv156ZeMjW5jxnAbf2cYB53R51VNonF6hAV4EhzTq-3DOiwUHcKNpGqTULb9xUD5SHQfL5Iwo62TcQK3NPtGdZrQsd2vM88eaNohqp0iY4VY-bG3PK09FJ6bofTm3bWAh07HHBZrpwNTs0Kc2RtEev-2sBnjdOnrQeA40CTXwOmGlrpFjBAy8wP6fihAtGD0oT_9bW-wVNaw8NTYsxnk5whjCCjYwXBbaxyPoBnvxE1LlZ-HiyBQX2xk4dFdRFWqwuWQsBKo8V-5cxq7XiiYl07ag2_9zbuZSwcF3FAStU4B0ZJ60u0LPwLpjj3Ax_7s33_9ifWbJ_4Bc1_lth3JE0ERybx6dEcE8j7M9WOyHyOoLwb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXuP9kWFRphj9aBNv13-WZIZ-np2aE2RkqDNzWsq_Tf6ahigCQYWMTfgWvcDY78VDBu34HYD9GUHjfTVuCXHMeoO9OMxkNiYEtp4_l6sjwSk2THFc34hILONad47A0Enu95KXTjevKpeul2B-wD8Kydd-skbgUCdJpYkblLUTUPT87QwIKDSY4w1Bzln1e0kW5gnG2K9ThYKq1df4IksaJ-RfD0po6M77yGYGeCuEGrjQjWlqVlisaUUrqQq_oQwVNQldWI40uqyRnL8Ofl5IfMoZbZBRIP1XwzbfgkyN4Co0b1ic2hEkcdrgQAnQz0_JqT_B6dOjJPoRRKqzFb_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
