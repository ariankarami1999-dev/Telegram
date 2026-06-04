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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 175K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYuO2L-BeZWs2T0lY4eyU49bWopc8zDMdDwL31Uiokyu3-n-XsZyKQxrWebZu7TN-gk4tjSyowElh_uvHz230F82x7xBk3WIS_CjBvX0FXA9RAYDbhvU0toGCkX4YJbxeD1Q1K9wjt7LYpf4OP_DLO9iVnt0_vArQYmg3VDPbqqsj02hznQrVzu9kqd6aJOUw_o4WO-xxL2UISOaVJN4B3A4cY3j5hJKoAgTZaB1yob9CQr_qoy-bOdXgv1ixmMaBan7Qk6kAnBmX9H0LJ433tmJH4S7EiFX5e972Pf7bc9P07RX8ZYdSpU3fcu60G89ulvhqioyw6jRn7pbosAQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF8kNm754rXiNs1QK0quCTA4S1dQPeElj4KxFLtAmuFl2hOFsDPD4w_eFcxqBHUVjw_Wp96iY4vnm2hV4_u5eagDeC_Gi1_SenT5y0Kz_3DKwS4Th9UAWEVed-EDONehg2eUj-5SrUZX8kDkAHE-R69TY0lN3VjzeGUNgAJS_hXeicgtlE1A_-PVK0vxuc-eMAjUgRX3TgtkbT7gYfl2rAVdQEkOwLzK0HnleWNHHPwajlNQWiOA2gcbpDPtm-waO7BCdtOX1AEYRvy9LP9FnoZv8K64W0T0Yg37KZ0NvkjiJeeNQaUPPMxWQ3N2eFvo0CwGpQOalkhinBZa0kSyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcR-Q8MXuC2mAkmqnbb-Ww3Lr9lcvvvw2l9UDOA8MDlk132C15zpvaYRZ2HtCIrkQjznKxkbf6EWJPa5NFe7LZp-vIdGlL2_yNzvPGMUSq9JgSQTwVjZqV3KsdnvW12M6j7ljt8IPODYZHuW_RV_itEPrQLadR0-JYrsrPIaaf4Razg8gNCUGyeEcJtq-WXDnNUMa8zqcckigX0d-Qjv_PCt4igTW7wHWentFgAa9SqruuGQWDg0bg9n3IGuBipJumwO1_K1h3T3qoPXk8oTyLO1eHeUTNXc21P1760NKZ3DR6jqLi18SW9cPodUQ5OUTw36X8ezbAcqZtZOyQOCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-t5_rs7NOYy0Xh0sYI4xFzEP9E4F57DDWFWNoLFB_go2z8L00lwnuWkVxj0bZbT3QfVZLBG_7bqqd7hSFEwQrpkezZyvmCQNO0sS2XEbyBh9Uce36xdRwAL-FNh_sYsgG21aoUTJl79iRxMbn_d-MvpKahfjaUYH0gWi18nMf_BfKodHg86FACSZrOFia1h0iyU98e-E1tiOqn9_lLZlQl5o1Iu4h99N3vFTX6hv7wlTOcuLEcnZ4eGtFTRzHGjoAs_-qiq-lNVNGHFHQGryaYf7_RsJKk7JQVFcBmRqGGdsQqexUWpfPWqkksfPHvlU-lkho4PxbzPp-6fWXbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQC_U9WD-VIGuFyG5tazb5DElHVIk5a2wZWs4nkbOITxXP2ftvr92jrwyhyzYDTqooiUoXgyOt97dIJFXc5zgAQ1NqJzw2YKfSsMZALVWTYPiZlc6uRLPhWAr2iwu0jVeZ9OcH3s6mT5-TyXDlZecQx0daH9T88zGg_J9jYow8s61zURTrguhJ4zcl-E7HRxXseizS4QVtjVTww2kapRnP0IHIz9ioc6jnokdYfRG5nLsZdpAplZ2hdCKABuGyYufKMOVv4Sg3H30gfIIcOcQzfHpCeEr6eROygxvLYi5GCSqmreTLjqrFKoLlzh2fPATGbH-CZt58UU87_w7SeI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYSzinCQFlYh4886qNz7QwyZMRpfiDVNrLQg-B_cw54od36Bl59sZ9ycNIKoRxJeFDjZk17Kpt45WkaSO3P7oWLz7w2qqT58Np5skL0Zxr5uBxbx0TGmH29OKXElZ52ibXeBQYuskGmmmNgc_bFyHQ_JlubE35LyFHFzeG0ubwX0HcVs93AftaXQ9uMgLzFMTZ7YQXJSI3gWNUHVjUkd72_uZODDde2P4te6X0yNelp6vZbxRMUboe-gFKljGg73MVgZN2wUvjSJqZcfcijaKhVnbhrk4Zwg1ZuRGTeeOODjejFYqoWkrCXdHdKhxb6_hhVfV2-6LcNowIT8MOwi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbR7vC-96L4GaFPKD7njr-lHrD7cplek1oNP8qSytfQ-4rLXVp2766vInjuc-xznOAqvO7ehjYzi5eTOJGFe2zaRdgkGke3KdtQsu6z4lPFkc9DOeMcytf6AP5BSqo44wZ9xfvRkiWCLv3F_2zdr0_rHNSPJ4aQAHDQAf6c4GgY2h1LVKa842stlcXCgggoxGScDBY8_zsEjjh9_d8ek113rkUtwzXou94CnhiSjjdzb8njoJ-BMXpXXBvJcXnaLv8-oZWUR6LgF6hqWqOyIH5_79QJjzus3JAHQsX3GAg_sJT7H5oZ1rDR3XvC9iTT7Eo7QBm3Y5_IZ0Q53GR7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoykqZrWzb6lKz8Jnka4ZDglPFtFRzvlqdTzybpwO6mFK82TOry8ZExtwB4Ox6hsN8wDTFy0cX2rnVUVGxTq8VxJS3gaf6eqz8z1IXCGi2UORKcrPpdb2AiusnEdAC1-4Sg3SyzIdy2LFPas6ZaG049HpZELjElsn7s69_4BztQ-EcfSptKyQRSDlFbla75_oNM1Y2gCeTTVgtsdqabPUw2mrHqOezbnEEtrvq07vESTCcGklsByVmedthY7rIMo9z5EBjaTAXvDmE5f_ge37mes5mmwz7ZgiYm7r5CYd7md68josVhmHa1h5Tg-syDOYBQLKVfYI9cJgx8sDlh2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaEr0WJBGKGOo9fknuongQ7uWE7J7L3lknXbWJOFrkzBpfPmPL1xKBgsS-21QcShvEfAq-pZPBZxafn0Lmz6dkNf-6y7_qT3QUA7X_tO_zPIDZFRtA_bUXQF_0zMQGPI8Aj4oOg4nCaJNE9EIIgpMggboLUOp02qnXQ3kINll_DIlu-i9VCZT0oHFVCfrU94xRp-IKkGLw6iioZiDf8MsK-XxwYIcLyx_GQXaLd8qrsmErslDFs-vWvTo_l8tKyoTpRBFRGYqxZ1TLqcwa7gnaqcqHZcGe5qPlFZoj-zVK1K4sEKHDqfs7v0WoeAu-5S4ECmcI3Z8XF7J0PBago0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGUbzYKohhqZ8AI681JtGU30TtODqwDdsY_--OLX5j-QbTPVtXrO0D9PeKWN9KgcbKFLzNteuADd1yomEyCqAWRZ6s0q7fH5VhDnU2DJsc8LbLsxXLVasXHxQNyaF4DmMzIm31NijGXI_kTF679fVglRy_HgEbkfeAreWGU2fwRbU27mDyvTTp0FISHWOpNrDl0tUsXYiiFZGXUy3xZ7LVXHQZLPudVzsE6rquQEMAZx8mwxbB7EOK7cHtS5KJNIixmVY5xsdMDo5zu2SNN1aeTe2mGp9CqRwZ1NCcKtFIFhrIff7osJx8IpvBCFgLnrKFzSpAIcG5j-qis7e2ponQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDgKXmO_XuJ97NWPXvTx0Erg4wlQeEkFqYKGBeoZ6sLinLclAJw4JKuyiVKuxiLDrH92mmaau2zVGmHPYlI_McbkJQthCMov-vA7nTnE-JE1SXrWru1fDz30RhQ5vAlqmYaWWves8o929LJWo1KpDBje7uwJsxHmRzUDiUI_bvHIcYA4ahp-6lHTZ3CfGjQWObjeNNpT7I5tHiDZ4gEZqcdKVj_YPrTEtn47k0_HakuI0eP3BjSdWKBV7gJqXpw1p7CUtl4Xa7Al8vvu427Axf_5r3AT_TpZGtJz6g5v_XzakIrOpG6gXwTkV3HqczJnd9H_GrTQtZkpzm6iIVmxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22738">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22738" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAt33RujyxzBVJtpp19lhwx-nsDw-XKbKLUeHv2oOEipu0WwC3Avz2r6fy5FaVBPddjs3eNsXK-G0-2fePZy2_rLftd8i6LUd3Hx2gRL27U1tOWW7-vQBoLs-M0siHpi1GV2EJ9L2uzuiyT-oQRMiwvzVPxnq6TMsmx07oP2Kx6mwCCK07PxA2rhQ4rSRFwwrlIxvO2Rte0_TAmWoMo4vgowTjk8pdsXEkYCj1yjJIXy0ecLcONGG7m3Y07G_Yj9V7NbPtiUTCzNsbWU-dKtQqXGplgEcZbgGDqeXslAecxSFvHv48DEuEgR2jvalVwPaIg2g6HcYfO3jucQA46FIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q81PgzSjaiKyvjgjQfNlE7qRV8lqLw1bSDSFfWCat9LaZyt52FoSvsDH9WhBlTJNJVq8jNraUR2EymgGA2HiW3bUePqpwjk8bcU28rEgjV1vKyMFsRSvZuCi_d-pu4Wk8V9kBgbveZNo4qIgz5IF_RthgGzTsD-wIfuUrta8itOQfqjT0NaYD3bCbclhwAXnLxSDr4QnpmksGSMEstkMNIHGe1mn8nr2hRNWwXMqDZTKurBiHZMKJ5QSnFEuLI-KuFP8tLRE7uSVv1hUOeHH4uq6TqZWGIA3_adZm2pvWMz28efbYThXUbhiTtHNl0z0TaBTuQfDx0ugCz6YJjs5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLUO4jvDdTBhO_7BLxEBr2p0iDkYF6w2ttLjkTsxfjSBYIJVvaL4EIyPPqyj8G4kQGGfmZt5Wk6pKmCxJ-_GD2ZCNga4HqqRdnl2m5vONI9Xyiwk7RA1rXJDeklLbb0lp7cCyQAz9I_GEcQmWXOb6HSJvEg9ErAkKlVML_aKIOGYZzTGkQeJ9Damr72Y_mpkgERsv_0v-oCwHmSsvUk_tlG1v1DTktQtdeDUuHFpj03ylqH7pWImG_ZbF16CE2yhwJOKD8rq3f3gnQJ-cUpNoj2IniQnSY0Hcf-fEiWUKwauViIWTb_K7roqebzUz5v15EgTto04N0nCM_1mnhxQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW3tjeiplsN4j1FksxijzPYXxobfE5q6wb-XZEMgwEyfgoUfgTm0NWxkuRlR0re0UmqzjxiBTwOLnEHAFBmP2DoBUFFyKnoG2c9EGO9e4PuvYanL1adW0p6JT72Zs850eCkqYWdxLq-o1ZZrdLK4V9n3ggm6goKQKQnGc6MrkZ1KEVGJ7RUMnAvBtgJ4AdVbTjiZSoQ1I8E8NpBoiFiBL9aPGadYrrZZxTdvsIgGzlrkc9wxyBUo69UdZQfH6HrgdlIVlbhIHl_cXkEE-eujRP2YQAejMZUdd7AXKxjho9d2zYL8bFvjoiw9_Kd3M53cZC4oQFqUp7Q9LcqwhwYdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO3WcyfZtwOYcYQZCaxxr7KYIrmfIoavnjETa3bQzMQc5LAoW_CXTv1FXTK1azkGc-7hmr9xhYVwakGwZYrL1Hr47L26gqTRVbydPzrksq1oRSAq0HqBcQE2cJtUqm9MKE8ZjtoDKM__kUGNIyDIs6bTfL1OHYpUyDaB8ZJkItUWVLEw9RqqhS4t3GkKsnehV0JZj0qvebHzvUx3CqDHWnD7Jw2tcLtGFdEJ95gFchjWEpuX0-hXnLuv2bkY52uknagdU0g_GvoMfFoEXs028ll-YyNKn_Y5sGrwzLLWj3eeawlhtpTyTWz6W_YW6NtzuoSuXzqd9yQNezZHqSoWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsntaLrcVm_2400WSiI9oy7_pfdb1m8Sgv67ZcmpCMcpQvhwdW-kJGF7vQy4pgP2i2wwVzh60m31hrWzoyKLDxE8y6oumRZNZ6Kno6jDqheUVrwjzR-1-5T05333TYj0fJMBITqy2SOeDPv5DbdUD4xkOUlWNrdlr9GRG-DkeOnswPG5ZRBtnmGdVwQT_Aoc8B-Of2oz_XbEeswQS8TnViubV1afkW3URHK_fjLwdRNQ7hbNW3Hqq8U78GeSjZUxmFmI3H1DaAFguIF1YAim7ruUQtpGa16ilEuqWlSvtrJ2FOEHOZ6PBKA9X_wANSUJ8HtnFRt4SvBLObvbocLU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q187LdnhZ5itiftc_xLbg5Faao5SZoI7c4F_5uPGTo6rA0N4_lIJCki4_Tz7klAEq8d7_HQGD0IQTwfTbefQhBkQAhNQeunsCyraOMwnVbw9qih22qm-4fxmj2qY9Bxx3i5atvynZiISq5_ALa9A_2sJW5VuGNj8OG9ju9H3kQRLq6mK2454YOuoUtEG6gVSdl_-KYgUXseIawkOUJLxpB8yYzmXmYLOKJuxWCjxZ9pNHyZ1DDS9n--Epps0WMHSTazAXOXw7KdHGrWL6vcMaPn6OTlPM-AkQfd7-WQP_fVCj_YiNz67xyoXEgzBcS6W15qYhQ18PpAi7pw74lFdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaCsjjB0LIUc-Id4kuL07GPQYOJPslbNltp1WD9KFMAifw74ANN7hQuY1mM8WyFwAGEIAmI_d6GLV1UuRy-O9D2O2MxvZIjcaS9pJif96hhCBUqbv4OazFpgyr-pclfGTk4VwefZSs7ZOMDqzmCH-Vx7Amz48uF7_-_JBwBPD6ETdJZ5gqXD1ZCNSTneB_upPhPhnG_3b9XCx8lVaNJUPon_sLk8bB2wwaVukpZPBpF9HHfTSya-Ysm5UQ7Xy18hg7TI8j_RY1Q-fXPt6thzGj2E_144ftmssivEM9tGXbS4MSk451qvWQEY7UQkxBzQxXUZST5yjBzJJAkF2JFQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiL0dL45HEoMRkZT5gnf1e0Jhgk6PCMN-ZhQutnTMwsvWqVmGyz4UryOghrS4Xy6iVzAnO2cnMpYmAx83iAHEDfPZwNEIU_S3gLoXooVamV3-IRr2G0k-iuenAf9IDjHYF-PsqnclwGoAaWL8n4Rfew7koy57BxHWVnn8Uv8yyEHzzBwN-PPEMOFdoAUraGdRYgAuuLAunH0zz6faNSQ6ZB_WO2CMdlGbgeDB0paRYwzA3k7DQnjdUjNnikNliP9jUUZmMvGStLrSYTNaTjKYG7d1Qn73GV7seXoUnqXN1sYL1R-miU8cV-rmufbD43G_Q2Ie8Kn_s2Sp60tArLY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFK4Id5eAhnmKcMyNwnFHS7qtr5UvYKNMcwi3qRqPDYoKZTzIsYzSLpUFy-g8JgcNcXLS10Rq5zZb9XlLdTYRURKYLa7mjotgrGr4qwPmQNKLpbRwkMoY-_qHaLlBnUj6I62j5tcTC1NlAZILnp0_RytA12qLTTUDcxtzpEL4zbhbfdoobpSaFCCgTuoCGJKPTxPROXPi4Ey18OWE1gOhr2kSDORDYVPH-KILn-iSrx-M66re2zMIu4IHLCQHvDXU3Blkdlw4Bat0Mz7v-Xk2g_nANFe5cFrXhfJ9dp-IPIebeXzvHSHzNpgYiV3jX8nYljpMoI4ziYBN3rBAmDbow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqwEBMzhFXfOZpDJHbZxkwtDedsnVCmp8JLJ-RPCZf0j75LDqrF6t5kKcty_0HawXgRtmdvzt-iQZ6aM975Ehr0p7dzE3PguMS8JyJVHr6dix5nCE475Spjgjght2IpLADoXtbKcxAqndF6PUsJKzfzTT81JddjJCGw3oW3nHuiBQZah52-hi_jPGgfc2ulKZoWHpCHWvecFc97jMXIoxNXMMXIIiO8VeTPDIog64_B7rXf38AgYVsD-B6sA6-TfzThpGuwDhPrd6Em_-fpXjKgZHSz_PPeXIa_hUB7QizbWeqCmH3J4SEzc4Xcy73iGGcrIGPtOAvMRl0IMV2ywLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiLC0K1k50byTc-Bf-yt8iRX8mYDpA0lBNRA5nFWhmKjefD3dK1XwSZxWWEEPHxDhS1jYKBQEWPVgI3HPzuY9Lf5ElS8U2u50JQc-7YSkqiLPnyaE3Lv78KLVzq1jvkvhJBabqvbwyeSMGFidQfAJ9aMt1jIkxVorXHSbRyRe9B0UutYomaKWqn_IRxbidDZ-luBOG6VbyZXVrivbk6h_P0vOX6ESRAUb2XouLhuF_mGuHOWLbWlT2b5abyWignVwBI7nzCnYTH0UkXGsQNKVs2_JSP2jGYNJsaJumzHyLTaLTr7A1AEeTPKab0_u_Ph5rfkEyU0WBbZ-ZdXALGuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0NI9iVvemuyRkrQOI4HNR53AUh74Sys3zyAirp133zC6VewFioifE-K-L7wPj1yffofB82bI3c5g50ar_KQ5Xtu3lkVIX-OwbLVtRI81uUXxMH5hieRbBYAsJNsxuFGvTGRf2B_ACpotWfKVPYEgt5uoHf3Br6sw_TSduI6ZUyiDmpcSd5iHfAbrJrXvT_2LHp2PXQDPy5cIaA_sBYKWWqBdFZiXP2w6BJeDKjLkg0RVuMa2qPp7JfWFJQH3wxIe-IxnX6FOSM1YMp8HBvuTccIfzMiQ6pxcvwxYr0M4FslbVBbS1R8uioNl0PUPYeoJiGtjbHcTKUI4MR4EhB3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnsY-aVSJMpzM3l3JAMdp_0DhI2GonfpwoHnEXy2ClXF6vtvM9VFp-qtvON9Y1-QZ60uXNm8cK9UDWfUwaTLY9oU3vNlsOcPzZuNptSEcihQ_uJYdfWcCOWCXIdy4CL2sZbnoYcjrV4VSUMGRp0rt-PBjbJFpzkKY54avSY0HpquOfP7YYEQPQIbpDeRHXwbwadnUm8QDjOC0gxbEjVV0X0hYU-lxKty-O9ZkT_VIDwvvXdlsWTnxKpBQqO3ZVZdOhwuezUkwykUsbAllmNaAHxEFUBIUSxnyDDpWl6SZ-3WHHuFJXLiHbFeMToXIWue7QC0F5JbNsORE6Wz6tVsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSCF_1r3lKwCFEOlRmfIWI2fKXxWKWS4kmY91QryTq7vr1LqwvmPgd94OolRKKuwwO71xTzDNiiYcYycqlyyhMUZZyFpTTFiIAintrbtRWhBpeOzWszFq1_UvuWyvp12PJUDfe3Q8airAF0_eOCZVIUzuDQplhaVYV_eLN17NStp3a8IBJw7b8JER2RN5cJ0AvhhDahwmAOYsBy6NWH8QVv3QTiZJoQczD03Hjf0bEE8KblvelZf2pTR4e2b37fzxWTRY922VT2C5LTd4neu8LJj4PuWX6CJUCJSQJzEgIeeuZ8yGAvMzNfliajLVkPSQ0Q1Ig5On1ZdOFRa5DQUyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=Zo8kb7vzbzOYXD0UV9zwBQT_vA01J52kOxQsTl0kz0vl8iWi-Z87b0d13-fBvYpLlw5tyyo89T5Te0vqaZmQdiPnvLWUZuFbeQAmEMz6kPNSzrjptgKUpb1ytlfmRauuXEEhLTw0ViySLmqcj4z6uvzexo804BiaTQY67EBpmqIbhAoCPCWK6D3DDHzUJ_CQ9g9lpA5xn2u-1362Ke6cl99HjrfHdcuX-a-pgmYZxqdjZ8ClP7zV9ap-g0XplmzXcQtpZ230u_zm7RFkyrveV1PK3cxEL1nkOT6usE_OPAzE-gB1IeOE9JDzRLMapRCcs6moMlfjz50NYWFCvRRD4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=Zo8kb7vzbzOYXD0UV9zwBQT_vA01J52kOxQsTl0kz0vl8iWi-Z87b0d13-fBvYpLlw5tyyo89T5Te0vqaZmQdiPnvLWUZuFbeQAmEMz6kPNSzrjptgKUpb1ytlfmRauuXEEhLTw0ViySLmqcj4z6uvzexo804BiaTQY67EBpmqIbhAoCPCWK6D3DDHzUJ_CQ9g9lpA5xn2u-1362Ke6cl99HjrfHdcuX-a-pgmYZxqdjZ8ClP7zV9ap-g0XplmzXcQtpZ230u_zm7RFkyrveV1PK3cxEL1nkOT6usE_OPAzE-gB1IeOE9JDzRLMapRCcs6moMlfjz50NYWFCvRRD4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQVF_wP330aEgd3o8_s9ifL1Y_vBCZRKBjv1Xy_AGgwwvzxOKXVWpAp00FrFwL-r30N5EuKQmyMRIGQCDmlN8v3pFbg1XB-bSndIfGG7RDmzO6yODB8RLfHP2q61lDeOpOeQA2RTGkuh0HAbrpkUL_ZMZKE7-GY93pKnf1TmSemeXwIHHRJC0hhy4hUQ-dVW3E7Bl86c_SSLwA-U505ZRJmoGlY0Zm7oTrq1OIVZ--oJdtkm8x5f6YZHz_xWaFvuo6A17NFxbAtQcBG_uNMwkXpdDgT0NJp50pHBQV7p7iYik3gu7_hPLBUCdtDYtPv4xSVNkCyT6xj5bM3wSonh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnIWFHfupCjzO7Fk18O43kofPwW93LRb1fDiYtEdspABFLZtzxFz9fxgsIPjpf3920b0rwUMmKXxYE0lZiepxZ6YexupJdO9b5dEkgRhAWEZdS0RrCTGNrfcQteKAexElEvl3qtKofN3EpsXFDNzBQnqjk8BfUQm_WWNk9w_VzsYwsoQ_TfHaTkviUfuPg8lvu0LLFn0jTsi-5GsXhkBoyBn00-2zdpS3grK8oOTbR8VlaA82gnBwMQiuGmN6Gsk5Lz3SzbU0VK3ibWMjWFx6150_LzugwUjmTy2uq4pq-fyT738vVylVZMoFXI_CbQL8mQNC_i1_0qWk9uVHWhBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=MKY5KIh_WlZvWOfbxl5tWxqdiz2I6x5rjsX7VDm7C-epjGpPwRRLNd4pAUCo9IHuFr3VdDSJI-01m46_ynQkueG00zcZiPQyUe_HlcclT-FG0i7DvmYGZ5mqw2pmJ9LTeh920WcEuLSZdZ1aES4rkfOqwRs0NCqhzMcdk_-8B1QihoqaMggFirnK3tgZ84MSQg2O7MddtvbBBBA4ss6UmWJ8HW5Ai3flVDPxvXNAfXstfNsRSspaN6IzlkpTHwoMQlsd84lMeWhkWTOYqQY-sa09cv_UiKQtv-v9FuVhf-xPo9YKi984Et2ZvqQw8RHeJ1M595I4KLuoDDkCaTM4zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=MKY5KIh_WlZvWOfbxl5tWxqdiz2I6x5rjsX7VDm7C-epjGpPwRRLNd4pAUCo9IHuFr3VdDSJI-01m46_ynQkueG00zcZiPQyUe_HlcclT-FG0i7DvmYGZ5mqw2pmJ9LTeh920WcEuLSZdZ1aES4rkfOqwRs0NCqhzMcdk_-8B1QihoqaMggFirnK3tgZ84MSQg2O7MddtvbBBBA4ss6UmWJ8HW5Ai3flVDPxvXNAfXstfNsRSspaN6IzlkpTHwoMQlsd84lMeWhkWTOYqQY-sa09cv_UiKQtv-v9FuVhf-xPo9YKi984Et2ZvqQw8RHeJ1M595I4KLuoDDkCaTM4zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhsM9BTbxwaDn3Vxifgqf4Cmzo126CgEV-fZ2A5FlgADuV6UL_lpmmh8E0eyqcQ5Xco9pWqhwL4BjkkwguG3yi1gBsQ1pNPs_n-dvfOfDDmDLYLoOvVL7xOq1N1GW4ZBsxYQazvPIl_LcDNz1s0QbemFg-mu5FroLKW9E7AbKnUQFkaCM7_xYstGqrgSstfau6JMOxPr_88a0pEcr8ucJ6RgQOWmB_76MH5rKPHH7sVz_hFuPehbZ0w0vd61G7GVocvTsfJ2fy77NtsPNZnCaB4R1DgAmGZOZXFVkEujLebEICQHnL7Imk7SNkgqHHbcNoqfYueaOZ38P8QvQUDJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6PYpOHkLIQNCB-4CN7eHZ2CJLZgzRsrUilGjm0MZ-nR8GcB07amZNwl34IcqUkBxtfFE1zwz89zPQLiOEbl3qoEMmPXzN7d7d5pXxthvPu0j9b2dTe5l_Txd0Z4BqI-zJrfRihCoMeNDj0DXnvEZAhMOOWBUMp7mgN77fKX5UaRPpZ7f9Hr3KWK1zhUfk2wfsGhYdZc6Pfky7vt8KZhEVTpNAH6lOIed6J_91vtOXYSdGinQpDfULIXKA82qwHs2jxDJgNtkrj5IVztOJmpPWimxEqWlNwGbfhUBs5Ez3v0OlzP8QRNAcFjCmOuqIYmjiqh-69k2sskHwH2RBnF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaLMX6V0Wu7V3ewH3dE9rxRNPmk98BS40KUtMPYvvyI2DZx8N4YpHDYL1xG4Czq-VlN9B3LtCg2HXBiMZof0dLYutVCZZO-YHz5i-c4qanMStgQq-C_gCPIfoOtdG8gt0UbejWmbd9WBbhCP4WSa0hDeLplsMyjuEqU9WJm46g0Ng4wvc4-amu_lZ5XBDm9KIpyLPQ2HfPB-8pecCtdH6Sbtp6P9_LAN9hjl76V3J-sAdDN2kDwFICuiiF6UoT9JcfKO3Tnfv-F2q7iw3-ILrWJpvoQhn6Lmf6SQtFpFI67PNTzV3mIJZFMZRPxLI0adL62BAS0-Ua8gNktwbMHzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8H9Mvbs9M8uuIRmTbnQHV7kZK7ow_2YWJUv11UyYP3_wUVLQLdxcbA3ftbWZ0j_AnCxQuLXwgrCVA_DsIeTDr2HQPjedSQnuRsQRrerx4TVD0DGVBbZcGxm1xf1Nh_xih5tInxYUPdDCj_N3OdZkCO7saWdwpjl3-kzr_7sfOaQgV1m-LllHBtXKpsvzQZdQFvI0SRlcj6is21dkMNFlJaQHscOj74SCIdcG90V5-DlM_IJejU6lTe4O4vtmUMKFA4BpxdFs_8v-9e3od3nzsqoCSp9AtF7S4gcIf-xQe1n8OCRVhkpP6PIh3dm123rF345_9dZ4fjwYn23mmleyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH36LgPYgeYsivAqnFV_5VMkd6LNankaMKxrrUwE1M_Q52jCiACLHTM-HIjvNaUvsrriM4quazvKJb1iSPixQuvwFyLPpueb-z-MTmx_vcjn6nByx5EVETeWjcGyyR20l2Lng8EiCxkHZc_9kcGd1PLn4YnoCja2GD5jzcB_64-sLIYI_RbsCrraQuTJAxijpjJ_DDsmgu8Ki8el-vHkZXBUN3qRw6i8T9ckzJTONjzrVqunW4MDjQVHR5u1xFLVr74l1bfDhd9xIfFy_LJGG2iqILYziklEsASaSXS9_UlIUCnTFjDv1CpNcGw0vwUFOhwI30St8LC2TnS6KtAgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=jXR055FN9Hu9_v1q7gVw-Mro9E5RFDr_0rUAzIVLw4SxozdrkIHQGtzC73fxxdifX0s0fi102MtJizR-q9qzbZGlJrxIdUFn5ZAXdbnIkVh1i-n6dqwpmjQaqWrq0P0_-8o39f8Fg8iNGtmhp6uKBkNH8dxNqsGHyLsFS9NFZ7Qw7HhCWVLa6HgQvz2lo8Ypzwfssdje-Q3EB-WfI13tWnMOOALNCKhGxkujrPG2y_fd7GUQ6s-2Cx4HhKAHzvpAiqz5jmLxc3dX9NrzfT-rU7vwuFR_VJ8fwkrwjjRaq1-iv5o_dFKRZAzZoHloUVzga3bT9jXFWkLOYaISbXgVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=jXR055FN9Hu9_v1q7gVw-Mro9E5RFDr_0rUAzIVLw4SxozdrkIHQGtzC73fxxdifX0s0fi102MtJizR-q9qzbZGlJrxIdUFn5ZAXdbnIkVh1i-n6dqwpmjQaqWrq0P0_-8o39f8Fg8iNGtmhp6uKBkNH8dxNqsGHyLsFS9NFZ7Qw7HhCWVLa6HgQvz2lo8Ypzwfssdje-Q3EB-WfI13tWnMOOALNCKhGxkujrPG2y_fd7GUQ6s-2Cx4HhKAHzvpAiqz5jmLxc3dX9NrzfT-rU7vwuFR_VJ8fwkrwjjRaq1-iv5o_dFKRZAzZoHloUVzga3bT9jXFWkLOYaISbXgVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9_UZ5aNUXAE5cNZRgeD-MB1o6uGFKFYVrOS2n-yIvGlUL_K53l6NTdvSjUPOziYnF4jXES37J773ffJ7Ah69BnLHhVi5RSnR9-eQeAqHDP7zorGwV6UBbEx9x9itk2CsCXmXOmDqTaExDkMt7Fc_CK6QCwDivug04OMkPRObr_OR-3yB4VyIwxem61LNPTvz8EbJfxTPcWyWqJc3cPsy7GGun48mso2EuTIs5L9GlivqG_I50rbA-bm3Hg_I2QrDkmHXjkWz6zz_8YUjOfIZXkzpjmbvAHmXsPU-QeYKg85xC1FsKGs4mchqgRz6azn9mLywIVBA-W9QC7q-oP2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLEJRVZACDikhjL8XMcOLfaiTyQDExFdMuAr49GbnYODgwkIYd8ZLV27sC3SsmCvFY3dGw2E-pp31FOMsuaYmjnEzH092NDd5UWSlu6yzeFhrJcG9WRnFFIUNyXxgc_Y0XAUMl26uE9yCwrb9HMvHsAm6BJ_uNF4I3Ftj_PTwjgnC_iPnoJCTaF0rsXZKz_vDSpibBohshANidvZrACwLGtJoNlrcJjh7c_1QSECJkFj-qNeWa_Erpm8mc3KMF122OmgrSQ-v1ZxVIx3GktAT-0B9Du50q3AVSi6W_Xt0lvpOI6H_jzKC0S5a8K1HQB46TfNH11b7Gp1UvsmbGpAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqjjNYRZwhcuLkax0_qkCmPBPt-59NkeA-O0KT0pT0TftVuweMAL4QXA7ZVNLUZY11oT22hXpMo6ZdGHHrAW01ckEqMGGXGKd1O79cbWyNAJlz64PYsnmI8zha_5Wo03bLU58-HHDdAOr8kg9yXrIjyHHm_ho9oyeitLQ5nw5eOd0WrMqxwh0_bDIfnLHT22LI0d4aTaEnloISyKZ84BO82pyPH_hruzE43tJkIFv2rd1t_PHxoYCGKSbfM2seZBfdLTfrgoIWsMypYvvEDHYY7Xpy6XMR3ugLV7KYIri-OaJhmK6BhJouWzPn_7EvddyFY0QnZ4oFfPzgiYEkkGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktq2EjwFZg5IBCWqToK-nh3eR-miA_ksWwKHhEFaWN6bqtB5HibhqKARXtP1ic-vAPzUTi8TonX3MwtQlRBdwBxXUeq6fJ_K_xVd3IV8KhArMLyaEM0RA7Xrz2XWkrZvioddxNLKfRlnRXnuHjqHjryImmjHV2IdW84DqlQ6QsJE7THCH1JNOf335vfx7xTkutOqpCwCr9XV8b2SCde7IY9IMHWrQLi9aiso09Lrab6WODgfLN9SYsVr007WPlPMvURRIypKtcRrwgFkEknqYkVSr1fN0PZ_7pqBKl1_b4yWnJJvSm4Lt4rdl0w8BiOLvT1vngYIukFEexsqvP6fyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=fLTMrXiiST8Xl2SmEyyLI48GL-YKcUv5FmwaKNWE84GIbCkJbiDRzOLB9HeWJ6XR-0zFtXnkDh2j3EjAYKTaQkJmhHi20dpCEEfJr7jCA1ImABlvr1NpPLS_wbH2DX9s5-b1xTcvDXDrn3FiHeZtq2i7nVC5IPdfQPoISS_eWuhd5Cf_bm00ql5RMLXimXwsGGravesnowS3BizkddrtLxAzmphaLdQ49f-PCmHAwe0Vqa0UIh0vv4SiYxJyw1TIu_AebpO3853In3SZZkIBD51xPb9SJ3iJG8o3xAhTeBobZ-nLCgWeM9q-vqvFFX-mfKBCzXehF935gcuV8OXmKlVWBy8I8H9mTY_QDNQno0idxSexMV9kukHs_pZ8SKu7XFu8HiruqStj9WWtke5FkwQF7XnI8jZpLjcEdaqhmgnF_qr1o1jy80n_DWK-W_UxErGjGnZZd3OtKefByTHdc4xCNRWAGiTzaVD05mtP3UIq6z7ryPmJkwrkeHGGumLXRrSn2L5cUt0TuJGyvsmvx8MTsiC961wppsC3Crn8dYxqpENGjePjsLSQTXJuNNQdIJuaQtp23LaWejIQp4jvLaj3wW4DosHCUYukfL8oo32Wd3G7vV6A4gxOOU7N9oxg0i3X3gwv1d9b_SGK2SHrykl3o38JwZKSoNYcEz3Yb7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=fLTMrXiiST8Xl2SmEyyLI48GL-YKcUv5FmwaKNWE84GIbCkJbiDRzOLB9HeWJ6XR-0zFtXnkDh2j3EjAYKTaQkJmhHi20dpCEEfJr7jCA1ImABlvr1NpPLS_wbH2DX9s5-b1xTcvDXDrn3FiHeZtq2i7nVC5IPdfQPoISS_eWuhd5Cf_bm00ql5RMLXimXwsGGravesnowS3BizkddrtLxAzmphaLdQ49f-PCmHAwe0Vqa0UIh0vv4SiYxJyw1TIu_AebpO3853In3SZZkIBD51xPb9SJ3iJG8o3xAhTeBobZ-nLCgWeM9q-vqvFFX-mfKBCzXehF935gcuV8OXmKlVWBy8I8H9mTY_QDNQno0idxSexMV9kukHs_pZ8SKu7XFu8HiruqStj9WWtke5FkwQF7XnI8jZpLjcEdaqhmgnF_qr1o1jy80n_DWK-W_UxErGjGnZZd3OtKefByTHdc4xCNRWAGiTzaVD05mtP3UIq6z7ryPmJkwrkeHGGumLXRrSn2L5cUt0TuJGyvsmvx8MTsiC961wppsC3Crn8dYxqpENGjePjsLSQTXJuNNQdIJuaQtp23LaWejIQp4jvLaj3wW4DosHCUYukfL8oo32Wd3G7vV6A4gxOOU7N9oxg0i3X3gwv1d9b_SGK2SHrykl3o38JwZKSoNYcEz3Yb7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vduxRb_kUO7K3GW9w1gbWyqYqeBQNXoy5DUfJaQ2mR_LmVG6278meUiBkAdfLhY0DZNTrwcvqXkgLLag9gprX9T51hnuX5bc9SF_CeQ5yyFan2tz1b_uDO10SHlkNYLUWkx2_p76dgm4G71i8EgaglX2z5gKqOvjUsx2EVP7U94N6gGzV63pKWmUD9F73J0BQxrq7qEO6D1WuJnJdLGdPMG2xZEEH4fGcEfBpFYU_7tKf3nxQs26Y1VwNsvydkISWlnsqYhex0FF3SfKhrpGJsR5rt-8GRFRrBHBzRes5CmJ9gGYk0Z_AcGKHSZ60Cpf0mL1eexljiGMi3Ng2cgTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVHzJxuCL2j7DGEhGykxuw4SAygCc0CpsoqOU7lwpl2r-xI8SzC3i3lDHjy6nYJRATqLQ17dKR7YtfIvdvzj439xCan6V5OVt9liTYlvYuIDGcnrXv9QXJZ6QwmGym7gRChEEITH2dWpz0SPVC3v7GhLbTunKDzyqgXpqfZQ3i8AXbaos30DaWk5W6290oo6Anvb6DrrNd-fUqdbC3kAQ6XmzrQXbSeqsmIuh0ON9ob7yWSpqCl2mctYCwqCi9xyuYE_vYETmzq4DZCbi0Nx2CbwH4_C5bumG2mEf4ug-eltCrnl2C6Y6vc7hy4mB2ZiGHp-eJVvaid4VMQXJ90LGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrTOY7NRVTcLYi5uOPBxePs98rs7CfWc6AZVQ9Re11N3QWSwljYt83ODWhh-xjDNIzk43DBNu58FouK_LvWSMwR8VA5a7PtlqEQb6TIgouT28_9-WFblviRSry_Jt82veMd9FV9jE-Ff5hIi1R0mzwY28FdsBdCAQVc6FFxWI-yx8E9uXpddXaOeHUHd81j3rxYolfPUH5kXYzbQ0JEf59fY4LqMsSV3v7IUv6CCgSL9JPoAbluKXxCoAmfMaxkam1bD2VCkxPNQcYnfG3LfKYSRT5QAl--AlcHIPnHFRicJ1fpZnZZoYHcFWCzBYXh01ZUoqRsYMgN22PKzuWQgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbM5EFjE3FsHwZdbUkay-rJqh6YPgWa-3i9-zpO3O_jwRZa9cn_1MPcYKzbOaFRahJYO7wS93PAkLdg6u7LrW3ug0bvHoHsn3pqbO4qpi_ymJ7sO0Xd44Eu3B2edBf3SL1qVZdHj1_Zcvar-7V1F7Zr5WSG0fAMCpTQMNVMzfMMNSi04pjAZZQmZy3ccFUX23dy8JqWvTo_tyjr-wMxvt4b52dNU9ukaSLu3r3WsseqolfC7KF6jT5XqvjIpqZ3uRQAo2nPLX6C_IMpBGOskF5hxlgeu3LikR_wZZ6KF3Aw92ChBM6ahzPrxEXKW--QEDCxO9pQitU_nbwfLhNKM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLd_Cjc76CDSnaAZbZxROqtXoFNTKlS8X2eOKT_-zpfey2HR4jouQsoeo7M25QTeBZyPhmBIyMTM4q48vcUGpOfR-vU2Zw73pIAlmBCqzFSKkJpMe6axIr78Gcp6Buz9GkaLJLRN0cERsnUR2B29kvRqZBDjH6s0E2_M0cYjsfp7EV0ZlPO7TT6ogNYVxgCWv9yBMkSRJ7Dt93dDEW8IMpQTvZ_hXBmkbC7XB04985H1P9JqJIlxRASZegB4g5l9SOxJyDI68-d3vHFhB3T6cKBgw29VeHqMRnpL6HGtUeRhN5xeIlN3SvG76PtTtyICs4BZp6Kaxda-kCg3yUYtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoaK7UDhcMliM8KGz-Po7yrSxk7rmeVwzz8CvIukorcua7kRrqu5lumjDFkV8uLwz3BCGLTDXgOCf4UZpX0mmdMYuRS331sHCVWR2zfWaPboeT7guBEG1ZavpyYsnLDd5XbTOE7z5D9YUA08w7MaRfDnIj-OuPzPhWOoU0z8HLHEktuVHSpWD1anR5JDiA2_yvNgg0sCxhLNadKO-l1hdah5WdKD2aCiP8kfdT9dOiadboksOvmDJHHkQ0-la8uHwzx85gacKSjsB8CX5MiBUPT9cOWFwBfI9-U51hmuxhE4Vpda4teEr7J6A-6TjkjrE-z7UECgBVoLbUHcWdYQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV-Kc4qZIk9jq-WZ1dsY2JYQ3WubCv-GLc-Eg_x08nFZsDRkEp8EkfW2nBgF4lHu81OCG-j4CDnp2D7ILK1NKvork8eK42ELv2d9Er2-d80XOx4UTlufpvRIbgPKqS7suJRJVqjlqLHhrYhcma6hOEwHcxRjjRAnbRM4lfqAc43tYrdbAcXjPXaZLP15pIIu4p6pwRMzuxmFBRNUPH-JJsDT04XGZqt29mUC2vMZD3OZJIio4cJaQB4ddouFmW2vKmvQKZzsJV-KcPamnTbQHw4gSYDP7NNAyxKroWuOI8hY_eXslZh1znSLci-IHVbkApUIhBWyzQYV9AsZ8Ve2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=rD-mrUTlvxsZh_KbPdqyqDMRezQziZ_58wNbRo0kPyMjrQW0kE_TSLTKbRHxY2EHhbziHHTrUnaOR0CuwXFHP_bJBbXYYb9hZm9XFIxviffKazwunOgF2lpp7ClEF_y-1_KZIzD_JTGh_iPVEepSpH-RD1mnmGJAqnqDpZ0GdvFMlj7lzdyFEsS0Csg4fiSB4P6eG0Pkfc7fs8GZsXWObPdP2lWm3fUUsOTXWisQY9Tvzk9rIUuUk0mY9aL5HW9BICMYQq1tjE8d0mwDqEphVg4Ht0tJe5xipog_8vmZ35ZKBUNulH7sTkO4Ojk1qUEbXkW_7z6mAW1x3O0NEtiN7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=rD-mrUTlvxsZh_KbPdqyqDMRezQziZ_58wNbRo0kPyMjrQW0kE_TSLTKbRHxY2EHhbziHHTrUnaOR0CuwXFHP_bJBbXYYb9hZm9XFIxviffKazwunOgF2lpp7ClEF_y-1_KZIzD_JTGh_iPVEepSpH-RD1mnmGJAqnqDpZ0GdvFMlj7lzdyFEsS0Csg4fiSB4P6eG0Pkfc7fs8GZsXWObPdP2lWm3fUUsOTXWisQY9Tvzk9rIUuUk0mY9aL5HW9BICMYQq1tjE8d0mwDqEphVg4Ht0tJe5xipog_8vmZ35ZKBUNulH7sTkO4Ojk1qUEbXkW_7z6mAW1x3O0NEtiN7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7wiExW9Qb3ZEjz-sjkh2SF7Q47KggkmFeaez0Cm-D_RTI62xRhfYTRd268A8WzOWt-ZEyA3oCh5TWAKRdEOtmGo550bwc7u_ANij6EBLjtyqTcdNLp1ddEQRlH8HLsfhz50k-kKFADlY2dZTudFR0IkqaAJfKI__uVyGaxaFg3RyUxeIRlfbjt9qN0y4PKsQIq-8yClBmmsuc8DsAYDcoZKiex9k5zNid1A1CpGs-nj7j3ln3tmwdhT--ksLuw-BcC3IQDKuouDN74BxcBQnNhRbBoMxY1UeUka-raUDtuvVncPu81p6zXpy-IVUwUGtxsCW-i6c1m87ji7XhlHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnOraG8mCawGvPDAh7Hbl_fkPEApPYVFbOOX94Pj86xoCHzVCeQoBQQerfcCTpc41vBmM0wKxIFgO4Ct8y7kfwPm2Nky_ia21cfEaqqdfRhnVc6u0qhmyQa_ooj2AqDyBCbZLQ2Ffd_lk6iDVmCtifyDkVQ4JAP4APqGG-ht6Mk0ArH78FyfdvwmiVhKroVpLljZAgMCjrdLBEKprpJy3VEJmgPCB1VmlbGRBD5hs0D8ozyGzSwFgeREf1p9_T5rEl0RYC9Ir7BkColptFl7zYIAG2KLLnpHixmLLbjroPvqLPbUkuhabk1rL2Xjtel6keMezib8Zz9WvvTcDK2XPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ke5-BlbgGDvtJJEAtcCcGGRxCYo7Yx7JxHu3TVGIVdc9y1cw5HrtLMfVABxEaIZspKe9c3kWfaX72YjvBy8hWGrCADRHFOCh1gotfxNDZRs3wUcMgzDV-EHcfMg-2LANqHlwM0BXm10YcB39sXt9-aJUl_LiFzYyS1Xb__nxaPTq-1wMUNFmVgxR8gbo2pGBuVwqOnH6mfkpln6jrblAc9vqq4K-Vh4aYeqFb2C4lfL8gp34VqPOpHcXzY-IfXQGTUYs-L40MUEG-iARun2I9JhMw2tz5IH6XRBXtJCVhCWbDBGzv0lhTX62VQ4wj8dJrOL1-mSSicVGtg6j9amA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=jQ81H45Z388wxV4nF8cTiCoJtpvjEfiWxmEeYV_kw9eqtCWXvPNhNGqZt3uB3jSvp5uaIbPQbLomqGL64BMKgUFdHrS3Fe3ONoWnCXeNJm2__4QgRs72SnMPKhZpXP8_nGF9xNbHUvXWRH6C_eyR0djpXFSONzxJXNHa4yuBzeFgeT3g5UqFGr8ICp4A7PppVgq3g86YJRG-7Qt90OA4bBThEwTMEyf_IA1riwUvyHmv_SVu0Ow9eYRaq86SGuNz4rnbuZjJmJnkqLDWmakEi3N7PaSDA2o8ppeLKf1PNQFV-wOAwZC-3QRsWr5hwkswZkLmgU7wLdXWqa51u6GIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=jQ81H45Z388wxV4nF8cTiCoJtpvjEfiWxmEeYV_kw9eqtCWXvPNhNGqZt3uB3jSvp5uaIbPQbLomqGL64BMKgUFdHrS3Fe3ONoWnCXeNJm2__4QgRs72SnMPKhZpXP8_nGF9xNbHUvXWRH6C_eyR0djpXFSONzxJXNHa4yuBzeFgeT3g5UqFGr8ICp4A7PppVgq3g86YJRG-7Qt90OA4bBThEwTMEyf_IA1riwUvyHmv_SVu0Ow9eYRaq86SGuNz4rnbuZjJmJnkqLDWmakEi3N7PaSDA2o8ppeLKf1PNQFV-wOAwZC-3QRsWr5hwkswZkLmgU7wLdXWqa51u6GIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDbbhuriMYgx6yJQwd4z2EHhpgKle6aRL4FQyBKArHLI5b2zx8aGsfUpFkKhRl9X5Ysxb69kFw0vKsvq0syeqYMElC8PygsDOI7S43wKmZrTeI-Nzq1lFyKoeXBsfdZ5anIzMJfzeA_yetybHVzOaGwK4M-OiytNe59PKIW1xLBtAyP-5PgMmhk1jYt624luXpAtIANnolWEcQqohxyBHlwTsC4sBcB7J_sEzY2Y3vJ-joXsfltdRdtX5f0-Pc2nCjpFRNYTQCH28I0GSyNfBW-s0niGz4hCX-tHUq1qBQanYe_IzJFaxuIbT2kOXykk0_ZvuO9YDpp7UonACsDaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=HFw7ymCGdnWGph217hbZoZopoXZz5DYAU8lz7NwDrlsOYqpM4YTjif1W2EU99Mr-7AOkJ_VKcahB1dORBIxq3Gwge9iwEAjN_jLB5QXWL9fjCR-pHG0iuXx9vguaH7xPNOxjgm7cOt2U-IsTX1ZvQs7kQrrmvUIxo_dkFrkEtwZHN_Gmuo-KwDwmlnE8MB6wNlvnGGse66bpyWvAX7K-a6AzsY3odUF4VdMA5omilRXG6GjbTp5XrOZuby0a9s3mxorUsXepfBG2uCyBN_elN0FF0_r2V5XhxTEaDFXeGgwV9Dr9peIpch89foEXO-4NoN7io444w_W5obV--vWq0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=HFw7ymCGdnWGph217hbZoZopoXZz5DYAU8lz7NwDrlsOYqpM4YTjif1W2EU99Mr-7AOkJ_VKcahB1dORBIxq3Gwge9iwEAjN_jLB5QXWL9fjCR-pHG0iuXx9vguaH7xPNOxjgm7cOt2U-IsTX1ZvQs7kQrrmvUIxo_dkFrkEtwZHN_Gmuo-KwDwmlnE8MB6wNlvnGGse66bpyWvAX7K-a6AzsY3odUF4VdMA5omilRXG6GjbTp5XrOZuby0a9s3mxorUsXepfBG2uCyBN_elN0FF0_r2V5XhxTEaDFXeGgwV9Dr9peIpch89foEXO-4NoN7io444w_W5obV--vWq0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umAiD-ar5UiNND-HZrcPFo_mQ0x-3ATfVcHoKGMbBNm17xMUKxQ118B8A0-H-s5zwDH9DM6hhS06qVBIsQoGuMucyj_ADAK_BUaOLr6ewaYilx27fjkyVY7_pR2PVWpIjFr3QSW8dnxtQIhv7ubBiu-5KSXiguCNItgnbtGzl7VZ1BoFbR34vNlEUwG3a0PYLCE120NfxUZf4te-UeX9PE3mDcY5GPnyTMleWylp_OlL-38P8xFVDPi_Zh1WFFUQq1h0Clj4WtT_C5RXtHgOFWnQxymiQxZRtY4ArIIpvvojf4ccBHwgDA25aesCLNN71dz0nZzyAYc4bN_-9wiTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=Pu2Z-YTHj_HF0Kng1OLfvQEs8pIowFD6YbBv1UjIFXLtCVo6fl3-V6RQwtmPBiCxB996Gqw5109EK8Wtje2_JVNuKfEenpdTRMlX_4JHNbPxKsyEVSeUpawszq8iZM6X7j5ix0uLNzzFHhgLPNe262otsszZIsksda81Eo8IGvnSFKNlnojPQQzQOvbUHasWCjaVCu2MHJYqy5Yo5ebzXfKpLiHHA8TULOGYBGVHUPkMe6dC8CQHC8d9KPdCK_58gloFw3gzqrPYe9IO1_RJ1Grmk4jCbDpbhDv-5bqPwzVcLgTyFuaNE7cD_M8dzHbRKVV2BZGfZzG0VdFapeOS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=Pu2Z-YTHj_HF0Kng1OLfvQEs8pIowFD6YbBv1UjIFXLtCVo6fl3-V6RQwtmPBiCxB996Gqw5109EK8Wtje2_JVNuKfEenpdTRMlX_4JHNbPxKsyEVSeUpawszq8iZM6X7j5ix0uLNzzFHhgLPNe262otsszZIsksda81Eo8IGvnSFKNlnojPQQzQOvbUHasWCjaVCu2MHJYqy5Yo5ebzXfKpLiHHA8TULOGYBGVHUPkMe6dC8CQHC8d9KPdCK_58gloFw3gzqrPYe9IO1_RJ1Grmk4jCbDpbhDv-5bqPwzVcLgTyFuaNE7cD_M8dzHbRKVV2BZGfZzG0VdFapeOS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxBWv7-vFitsAZu2TmZ5rMgH2DM9Sn83YlNv5v9BrwvHI5uuYZAuIhC6sg1VWo48F_vonp3PWduUYMwSZoqVilakmKFYxLESwlQcOv6H2Fj7NcHXqSgTnkI_o88aBjGy69stA2Cen3HWnDlhqT4CiZSbi8vvdCxWgmOg1HLyizcDYNULcEI7KOOpKBrqHCT4uYeOyL3KPb85SfRaFdb66L2QmSvkugwtZZz_4Y4ro6KRaDjX1ag-VgrEE_xGrKI3km-l5_Im9rK9pXKH2arYDBfHaxUDKhgmqaxAmPpZqpvxox9ePPfmsoNCIEgcYDO7Z6oxvSsdrpwMho4IEzeKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZajtIyzqMffT6Q4ZsFXCvvewA3-Rhns1aAJrXm3dvxHUT9GVhV8eIpMYSPhNLupl4CGzyn-zfzjs-WuuKJ7Ym5kPolVRItpJBnhxMQL5NiSsP7qdb-bPZJHY4pkVF0afE7Rb5v0m936HaXqitQHAp2B7EQ0AYNR7GEWTVk6r3IKXl2U5Uz4SdnCsRMBa1IdTSqtZmMai6F-wxm9-UOrhyjJ2FyCEiwljRZeMKellNPgeR17PeLXiFJVPf6BsjKQFlQyagLmZK34e-tx3bk1cZlQ7plHG0Z7PfjnMAsoPLKr761qZdCqcUudYSLO6YZdHgwSV714OOJJ6v8C2OhAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBVIfn2Ewh76udgrsXTXf5cCqD2LAXbMDHcUXLg4Qo5DTNtZlx-bUkoIh3uEViqC5F1UsOXmOUpxudXW1hyRL39ozoBYBhMOLRvTE8a5heWJPvA7NIq14UaXTH2u7iGjlCZ1zigpQR9lcMRwy0rvQLOfrv5YZEd2oMP5iZ5O9jue_UH4XQAfDrt4QeWKwiwEq4eZratL7KfV6POxSPXt4sXuMI9ls0KOA_RUpcyz6uXftsMMn3VclAjoqICPLT-Li9zkw87yh5BbXklpacc2_mPAVehvl7xT4PA1QD7szajYCQfrQF0YuiQu6dwAEpkj1I6z8d0tAa5pUaOPjQ-pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od6RFtXZ2huB_vipadQVd-_A73yb7RhNiizgaSoWQhSiwNDTaLKyetPkr4onH8m7kdtL0fo783j02hsepPTNnm7tprJ8D9rcprjbdtf0E1j8vnnvRD5WdEjLTSiQGyJWuUXERaiWSZShKnHTf1xYOBqTfOV4e9f5PPjU6GapD8e77t4xvbe0xGhV-09fepWbykfo0mkrEJxMatirdSkSim2f0Mr8hbqo24Psm-c9v_8e8zvBRfpxAj7Rxy3bMa_WnVwTIq5FgQ00zqFjnFDdguZQVUMWAFzETisce6a7bIj1xItJcF5l-arAKa-__OSEfLB37HgR4gGRdHibcaM7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=ptG3psmEi0YsqEuuxnxgRy_u5FiOHEylu75agUMZGkmYhsilQ2FtL1FqTNhh-rLbc7yt47kTNMGQkEuJvgtylxXV68roumxC1ZLZp4IYQG5kWtp_DA_XxDG8l2t4Ysmhx2knAGMzXuEsgrE4omlNsWrzFR3EupFh-LGf6UHzsr1rsAocJa0Enq95TnEz_LIdae7O_1O6fmI95O-rI-xJNllUb4RxJtDck08mf8wDn3pYnMYnK9oHgld7V7Oiwoul_dQ0dijhGkrty_5v6UBE9OnRRpyou4TC2EwBor0yleQbFjkEIFZkgpVJGZbN5mRuiMi2eQwPyeHMV-uUXOhAcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=ptG3psmEi0YsqEuuxnxgRy_u5FiOHEylu75agUMZGkmYhsilQ2FtL1FqTNhh-rLbc7yt47kTNMGQkEuJvgtylxXV68roumxC1ZLZp4IYQG5kWtp_DA_XxDG8l2t4Ysmhx2knAGMzXuEsgrE4omlNsWrzFR3EupFh-LGf6UHzsr1rsAocJa0Enq95TnEz_LIdae7O_1O6fmI95O-rI-xJNllUb4RxJtDck08mf8wDn3pYnMYnK9oHgld7V7Oiwoul_dQ0dijhGkrty_5v6UBE9OnRRpyou4TC2EwBor0yleQbFjkEIFZkgpVJGZbN5mRuiMi2eQwPyeHMV-uUXOhAcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5CgWeXLJBZAAvjLczdL0bcGvDLTMvGcgx2eokmpQ1-tzsO4Z17qrHpdOQaX-dLWiSmayU8Xh0b_VEhGnzjvKmv95Yv4ViKIq6M1sxM9jeJfOwdA6J7_fszbPe90M-mMkFOv0MOapiQj8-eSMv6JzATJPWxF2g0FNohKwKkIlmpFOPaUUzw_oi4gTLKfKZHM8JbDKlhN1o4mDv5CrDNIerRrazMFXMKD6jZMXEpj9oW6wLjPOO_klxJBlAUpso__BxUFE57dXvGPXO3uK32cVO1dDsdCaumwYoNDU8CWqHQjBlU2wj2qkAb4WL33SGwSHChB8VfurhUb_Zrm9ZySww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBRWIfR2j1bt2hwlxouYIjVsn3MTMJqRffuFioE8ZuTrIbfgBiVwup-Uj2G2NpnH9JK_gN9kCxndi_n0KyOZvKE1ajx3p7YiEeCjF1AvLlc_ySn9Hr1Jq07DCJCWjmG1r-Y8JJbiaKeUr4E9Fgnt9j8igwj2N1WwtCGMXnIyzrW7t2XTmlc5oh1sUdKNiQtr7JXlvWeQUY6jzbAUxnuJGDQM2JQe465wqtKB4Z-JjvXagyiJ9szuoWfAVoipBvRfbuuKx3xIDlQSzJ5Tt_j1MnRHAjcEfP5wKK18Ky0oR-6ys58qr3CPLah2M8zpY-iBBHZRYY3hltmRzpw8iUhYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oozxCwX5RC35zMsjLSYye9N00YXTElWjNxSP1a6jDDqNj6li_iubvE1KYaSIxNHcBNeOG2IP_j163ZWzJUbKrHhy7qY0SvXDgjvl8LeSuSwj3uH0HqnFvI-XpruxplirIDm_V82arYjlBBGEQ4YQZGBEYM3Sgvu9GXrNVNWvt7ziMTNDJ7u3FsOLFo_y0ffSRwUmnKvnKzTKllLdMr2K1ZvcqHomHpvUSWl2Lsf41LOVbwZXTyZgo-w_G04Adj1irEt5_2376dAmzP2Qe_kthRPBeQnNDgnyfqWTWSSQDJu_D6QwAU43Wb3Ni01gNsDzn8_ii3LWvBTw2l1il05eAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUd1Xp7WudFQeaHy2--dWIPp9G1ruHeLVP2br6TRabRsLyNXWJhsukcEB7nR6yOPLwF-azJEMrm8IIZB24Zi-0yEFqeymaEdWa64xFrGWzwENqGuPn4fSDoWHLt4SLIdyy-mNDQbCltcCWXAkIZFxTiPC6SNsvPly2Dwah7MZLY87pWb3GPkaw2ybcTDKdMW4Plj0nXTiAh7Quf3ACHLkVoRb1zqDy1FCR-HtojNH6YA94e1IU-ulkoUYXO9mqHd7uAQoVE8ntpjdVrzibyPPUbBsiL0LTBhH_ZsRd25v0YboN_0FkYu4KDb6MbBp4E14XCmQuYj8m011JRT9i3-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPrNoGCX-CTpo7dtxy0HZBqYxg2B_OG0oEHeAWITky4OVdd2DziobcFfEKfyQ8FiXAJtLkpOhBoj37OMTm6lieNWImmXIpMkESkB29spdDa2_vvZQTlzhSnx8g383CH6bAySOnyx4_8kVzhWmTqMQkid2TFvajkP0Tbvd42PqtSepYJqAzHXTTnKzb-SjKe1dtkfmlTDbgaNnxnGuwiu0hgYJewv7ZjyhLnLU6lA6Rmvtu0zD6dGZK4b5Esa6CAGTBUbY1H9BHeMC6KG-lzqzF1wrr7DoO3SbR3FkSf46WR44vT8GqGaZqbsPLwF0qVVtoFLEN0bWoTK_u5b14uJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2_np8kbf7FT4s5mzT6BPzojVImoE5pkP1Fcjd1CnwGjLw9CVS32kO-bRBppCDvM3fCjXieUk_hEreBTmm15zMe8TGZSPL33_J0nEhlymgyzGxx0uwyfbzDPop9bmYPVXqQVkDh9zjB_6V59pGXY27vg1bfT7IrVaJqnBWc9BO5roOAtwXP_3F4v_bdTxUuXYLY7qXv8ftjxi-t51sYbLIGnyNzmPf6HehbSu2wLLp7L6hmPN8OR7cj0s8z1OMpWHeGrEJBqZnSyU4sQa7NZ9XCDAs8Xyu5Gw5YMdMX9eqG4RLjXNhY-Bm2qpWA_2k5YUbDJY9Y24ZFnMLnsa2diOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI6X6GlSkm-ztyU1yG-qdz4Oz_hr_YtrIodoLCazSXSmzODQn9mryGdVOyxj3J6Crnes8z47QGflmk7hHSiWpwrHmqrl6Z8I2Afut_NDmtVTxNVyDTO_N3i_C5Fj0JGXgw85GYOxNvHW4DX_oFkQplJTchTBFQ03vAI2fGopNn_Ef9GSh_OHBB4t85XqsNMvlA1vlP9alHp8tfK0aarALX39Op0ccY_g7Le-qf1aTF4pJt5S6sM8q36rSf4-1Bl7pzKtf-1fhhQJ0Bn5pfFjbpqRLnIyoCgGnh1MHicd-wl36mMfULloDR2Mvuux3RIVZmrM3tDQoZr4_itwp5pN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIsDxc4BFy20L6nfkkMkUQ-z4a2tj6h0C9Lej03enmIkSEi9_rjmdBEIQ2_clVD2-7dDnyxglFgtZ5jIwrtEeZyJGujDIise6ayN9P2fTZen7KleiEndpMyN9GnAIpTa6azlQHh6UjnERroj7X7cmgryFT0vxmwR_yeP9bzAg32P6bEwtz7IO0JjGHIAXIoD67WeFqM8Xjh9pJkYGSVL8Yg_bipvU-GVfa1hJbN3SwIpBCeOAw0-8fIZaT5WLrooj2CHHaV4P-IAYNYrQiicsR9EU_CjnVR-pY4i_xlqojUkCW-UsjAEfw-mj5wz7PySBhjhW3IOJ7eKRo0TuqL2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seCt2YMapLFYNLoQFhy1INt5YuN-JjNWYddG5ms-sD06Y1rMnBUnQUfxnuT2JFrblnH9FfiizT5zjJzjpXGma5iuN4ktaFzJTEle4hu9Cgr32NWsT4eHMD_LJ7m3OkaI0ESUaVpB_W_0PCXA0ozcO3_ZiDgyfdhaebMzW1wJh5RD2w48I4lHRc6v8fDg0WUSwdZQ0kj2HVfNPGBWr1hbX6yRqhVUD7T2sL5AiEMjLpU4ik17O7cZdgHcwXFswjLEMdXsIa0cBVcoXBn0B2Hur2SBFDoLAmo8AXf9_4dvBewSMKZNa7n4ldL7xijP54EP6lUDfp9KUkegdrcOVBe7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMEwa2b6QcvVICE03LO7WLQ4HDgX5F09J5Z1AnzkstdlDqZrQb9ZZS79DO2sxfQuJP1Z4In1ic94FU7RHr5N89syt2w7_53rD3zCiDoHqnzBsRQlGLTCpAPiEsgTSUSEgdDbhb7z_p3fpyi25vvdR-BDIw99lZZdALkWpF9F9cumadQDfFIrEPktBHzd88C90W5k4aO5HpbnpPktvikzF4IWJvJZxQXIlvdppsb4ZnKVRGamqR4brxk41s9CVWpwbR8E9KzJIx1c-P4lp70CoSMGHc5MXR7zNRZMVvWrXzTjC334hD5hOn6940MXLKq_QlXLsIW0HC41gSDfzsDo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6GuZic3iIlrzCKPNhT0gf7z2SAp9BuTQDTKxxXiEmyRfUTtUj4nSmjR9pR4Qd72T46GF1Kq-kCw0LmG7D_ukqmwmmXp0mOr5wh4quyzrIzrCSa1hqGE6PlhiUsQopyNtPd5fgEf_YItk4_Mtd1zOKBLEYXlFWTtYi3cF99btcbC3WAm9csYK85moj7cBaSeN8T4mFsMZRTdn-qZwEJBCDC-OEEeMV7unpM1wemly8Ji01Oahxvq6JhdJdXTRK1sUAkCqISsJyzmdo-0DHV_7NUvEU_cK5Dv9hyigm8__QuhAAjmXRjFk-c8zfu5HpmV5x9pBkxmKWi7KbIK8VzU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccX0m8VhQ4ytI8WmLC96HG34ny-z1Gvf3MPzm5S6mdQa_ODR8LyRhn3WanQfEWZ34_y-z4fZYV4BgYEJOZhHKo9PPwe_8j4byOQS0-cL9k8gT_RoK90yfSWxtxPlLQ3_OfL2fDtMlEr6AggePbisK6ZoAhFGl1mFhHVqZela77LEnf7dTVkmxW_glVGV0Yu78_A7Fi5N2SltNBIgYGDSIDswfPq5tYEwBrHrdl3Bh11hIbreJNx935tnP6Dz6e5MAuu9A_SByQHDoxMpHOZKqwmnuFiOqR7akJVkOGNRQdplDOSYSSkSisUPKbs1q0SsQnsRAKzqWVK25_dTVYKAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xet2mIOOkruhp1ci3uoVZuXozLBAfWpohsLcEjug-LamfWvk10X0xt4qBxEwZmLKHVYNEYjV2i2KZeAxuZp4IvC-hTlgQFQQ7dC4BJ41oz4YIla-YYyiY_oTagW78ZU-Hut0pXDMVl2azmapwMytZEBfVDBipW44M2aYNjlBvXOf5rtTMLCE918bIdAO-NYg6023ZFgxj8e6KlGOGlDzrYWqzt-Cjr6p-p-3sNTzCvq_HuHY3VTy7YgWJK1utx4qi01d0ATu-c5Za69imdLFg9v-6VdmjIJZja4n7yvQ8KvmIVlMJt-SI4uJBwONJYTEJhtsKw7reG5IHckpo2WejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=aHUBgbwJqyYSGUH1KxkQo3pqSP_rhoJIkHP08FK3DmdAGHDhuW8Mka2lp--ywc4WkWPiJTbIqXfbtXCeSyCX6zHzxFBYSHbU6t6Du3ncb7Cpr7c7TnNdQTuCTwfUoUXcVnn-6AV-OxatgF2rjDazSlVM2hakRFPBmdWTLI_GAIEQtf8tBmkb1OuJ-M2f8oJhbLwI_h-M_l77ESffLfKJTbjkrmMC0gizOKTx4xPxVuW-mrUuYTWdBNj_hL3I361WEx7PS00_dsqSTuiSwI5jwYiofdYva_MzS4RcGRyLGaMQDL4XUIsaeEK2w6RIGK76iiEN5utHBWpxigAOoPuasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=aHUBgbwJqyYSGUH1KxkQo3pqSP_rhoJIkHP08FK3DmdAGHDhuW8Mka2lp--ywc4WkWPiJTbIqXfbtXCeSyCX6zHzxFBYSHbU6t6Du3ncb7Cpr7c7TnNdQTuCTwfUoUXcVnn-6AV-OxatgF2rjDazSlVM2hakRFPBmdWTLI_GAIEQtf8tBmkb1OuJ-M2f8oJhbLwI_h-M_l77ESffLfKJTbjkrmMC0gizOKTx4xPxVuW-mrUuYTWdBNj_hL3I361WEx7PS00_dsqSTuiSwI5jwYiofdYva_MzS4RcGRyLGaMQDL4XUIsaeEK2w6RIGK76iiEN5utHBWpxigAOoPuasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM-Scj4XoeUQNz1pimjiOWzSLhTXcC_05cPLFyfumiTGJ8ehiym3JAoixC0GvecBrgZfd6TVE0O3eThnWg4LzFB5u-BXSCqFG9ushLzYQ6LLx4EFQ87YFbsuEQs1jn2Ws3Y3IExeAVJwn8UwHwNJuWdRAVC2AULXIskukNYm09XzFpJdVGH3QLKXO26o4pNcdjEtJhCGvoxG54yTeZVzriRoo22G_GDLEEKQOrjefmbmJWISIBuYzUVPH0guVMc15u1W-u9ywWzJrRYvmOorPR2dAk5RkOIEPtT5gms0-a9Gs3Zug76pRiXQrQ_qS0FX8m86X-ZmQyu8DSZ6Xwci4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO3T5o6F_FgcaD68ygtLhdbsJMQKX2AlGkoiUsLIVq4DrOkiE78Ur4l5AlYxmAcCeLw3813D4Tu40sxEx28NbQysVO8TkKRSCyHsR8BExv-wQYqmte-hb6qZNlB9YFs98rTppBQI8_qi_CYAvycXDNGUu1XiKAFBhDO0Smw_Y8MXsuEAL5XZRPfxuSHXVtqNpF5ZnT_OnV2pRSQu1x9d7LeyyDzPcjjnSMyC6xlunkCJqakYcX2ISevziIIoR2_G7GEjc6YF-EgOrmMe6gUASuuNzcnT1WDqUODlVv6XTyj7hyJCqq7frGHUZKX9lxjxqJ3aFw958Vr50iF1Dt2YAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=l95B6MIJe2ibL0OkJ2_A4yWdCY9jWENTG9S7nmX5QFNhib5c2bPEiwtpiU8IVJXdJkn8dBTAXxBCnFmBShbZ0ihW1l3UQzjL59-FnWzzPGhJiEyaRss9OkTIG7DW-cWsJ0uGCNhMpGv0GWo0MC4h8Vx7yYBJw_n556vJlTK-FsbNQKmmrcg7_PppXoRMn0FqmH6HUIlY4KEZWSdHd_0-9ondax_93xniSHjyMEJi8mLlHLnKBOh-9aFvA_y-s2tyJT_81-eJDwd83X2qbk5YJAbTFY1-E9_6ElxK7ESuDgcI-D-iSh-ZszQfxDSQaG97cneGzhjhTVn9nFWS0jyh9i1Re4Z3oeAAcB8vk-fp0Qt6Rnjj6B0ompOkx7FC1leIvPXljNt07bk1vYAgotCbdbF78WXRjPDHVqiaO202LOT1Bu--oZqWe3wOrUf_59OsAlEFA3Q140uSEFqBWYkrHN41tOxru6j5yqcn8qBGN6K1JwLHTbDH1bv3cY5GvxfvgIQ_G3w19VoiqDltnhw1G1jHnaIQ9sQ277ciUYyGqd2JvL6kmBnsNvVwHUaCFvwldKkmUweM-2Fx1ez-9DK6QBAmkRi56mTEUaysmcjhnqEBZDptSr1gt2HETaJU5T9miuwePnWF8fgmGembHlE_T0Hv_X20OQPTMwyDKstpQg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=l95B6MIJe2ibL0OkJ2_A4yWdCY9jWENTG9S7nmX5QFNhib5c2bPEiwtpiU8IVJXdJkn8dBTAXxBCnFmBShbZ0ihW1l3UQzjL59-FnWzzPGhJiEyaRss9OkTIG7DW-cWsJ0uGCNhMpGv0GWo0MC4h8Vx7yYBJw_n556vJlTK-FsbNQKmmrcg7_PppXoRMn0FqmH6HUIlY4KEZWSdHd_0-9ondax_93xniSHjyMEJi8mLlHLnKBOh-9aFvA_y-s2tyJT_81-eJDwd83X2qbk5YJAbTFY1-E9_6ElxK7ESuDgcI-D-iSh-ZszQfxDSQaG97cneGzhjhTVn9nFWS0jyh9i1Re4Z3oeAAcB8vk-fp0Qt6Rnjj6B0ompOkx7FC1leIvPXljNt07bk1vYAgotCbdbF78WXRjPDHVqiaO202LOT1Bu--oZqWe3wOrUf_59OsAlEFA3Q140uSEFqBWYkrHN41tOxru6j5yqcn8qBGN6K1JwLHTbDH1bv3cY5GvxfvgIQ_G3w19VoiqDltnhw1G1jHnaIQ9sQ277ciUYyGqd2JvL6kmBnsNvVwHUaCFvwldKkmUweM-2Fx1ez-9DK6QBAmkRi56mTEUaysmcjhnqEBZDptSr1gt2HETaJU5T9miuwePnWF8fgmGembHlE_T0Hv_X20OQPTMwyDKstpQg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikk-mLwUTZGbj06VHybdbbBzyrkbpltNwmjnjofNAu7tMl1EiWjHlnGrjMwC4iuTCIdUsZwFv0aiKzO2jup31lEEXhltvTPfbi47W6naa9R6xyt4wfHRbkMVBIewtbR8P4U8Qqt6d6VTPEtp_Oe_yGLZ_X6Knu6V6qtQsVDuGY5gWTrgAlnpmNT0NEMsHZhWXSTCBKIiS22UaK9tl7UAbIaw6C3T3fHHkwrru1dyX1OAHcKOOt77jd9pSeCUFYyngb688i4-_RupDB9H2BFhq3P0iv7rCE82kF0tLF3UI6_TIA17ttdOXjxcMQ6q0vh38NTcV2qNFRYxTCB4rhe0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=NPPOURJDTt0SuhDoZsJ2SKjOlRTkSn3C6GSalXfVXUkptG6SJMYjGii-yeeglkUm2He0egw_P8mahQ-nqI3saLPhmxkw_QvD-iwrmu0IfggoYc_ZAfUiyULEEggzeADT-52UDcU2Eb1pYwqe1CqH17_Sh3AgXXYzNxCv0uEBcwZjDdxf8ZQ-9C3Wj_t9R0o_0WiUaLIspByowlhHhIUJTxlWfvc2EYRmaO9gTpDMEbKDGhT76P9Uupfju8QK1SQTrrJrOUPZUvOG9b-3ezCTj9WvECBXeOm11BhW_Fpls1H8zWw3EDXCZiWTfcdLuBTY-Bdi1N5fOHssNP71w5L7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=NPPOURJDTt0SuhDoZsJ2SKjOlRTkSn3C6GSalXfVXUkptG6SJMYjGii-yeeglkUm2He0egw_P8mahQ-nqI3saLPhmxkw_QvD-iwrmu0IfggoYc_ZAfUiyULEEggzeADT-52UDcU2Eb1pYwqe1CqH17_Sh3AgXXYzNxCv0uEBcwZjDdxf8ZQ-9C3Wj_t9R0o_0WiUaLIspByowlhHhIUJTxlWfvc2EYRmaO9gTpDMEbKDGhT76P9Uupfju8QK1SQTrrJrOUPZUvOG9b-3ezCTj9WvECBXeOm11BhW_Fpls1H8zWw3EDXCZiWTfcdLuBTY-Bdi1N5fOHssNP71w5L7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1wXvQhmg4SggSMRJcyEAJMMOc_WNjBX8P75zTMOcXhR3EIj0GF5wW25nMDDVidJ9QjtdDPWpftq-Nq5qf5hVORw7v6SRUPuK8UH9zpxygSL47M_79Y957T34_d2XqV5NM3KpXkSKFvn_GPYOHaAOGH8KOnFJILcv3g7xPJOunkpNc0O99rsg5gHNp69-mQv4dpA4of9IBs8hii5Qpumcf6egVO_ClbHf590O69mIBfhSigFqMqTycXlFkvBGAuQ2FYPGRVg055AkMAqvJpeGUf2rHR21AfDozEFlmn2PnQBN5dHZCRFelV7-HSC12oKUqW5Ggfb9mIkCT1sIGu4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPO0qzC5Yb0MrOwfKeepaTakbT8cCU2p57Y8Q3L9EDHpkTpR3-ikB-kOOiMa626K_LvpeMTsnvKhUFkuhnSQJbsZYy3lVU1dD7EVFz2-zoQsxylCvS_fsEPcVYI6No5nWFagzuTaqJuAHET_DAcCyHev1sIv0vid_72IPc5TomX_oPYlgFl5lpGFlkorkQcf08NyZLBYVqMc-fF3_ZwmC5WS_9DP9twYpHyjQKuxovkAnjHmHX1eMkjQ8PzaCIHtRg80EmwNr6PXGLmfPYvVPZd-GU4jod3qw4h11kuVXZGpScL4kXOIisX_jaqnCQF4TqJ9Dan-a7lb41xambZn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHhECpjXFS-0r4tCbHpxNCTldQbpGueEtvsBpgCUEMJnvcEkpWJoUP-cENR7cyls3uwb1qi5-VDwOhu4B_ls-eg14d8N-JnO108VF9Nz625pGG8SnnyglnIkHvsOSQxurd2dY3O_Jd-5lLrIlvXhovQBshrQl9BClWiCM8kgbqnoZtuKPlpHfkXs1AClS8mYj8DchZ0YocAnFWYk9Su1iJXm0w9YEytwQFeZUEa1jMdClLuDuHcgYQeHMkNYOWlMjFs-uH8xNCT3hG2qudXyz94CMbsZq9Km-wxGyKEstp97pu-Qyk_f_P_5R45dTnloaiIpXnlQqeF-YOcwIYmmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=IuvjCdJQ7cYi8pMy6NAEnncaGRDMS90UT-9Ux5EUIkjt-ZBoZ-s9lkbc9psOm6hdSMFc7HG_TDuUBML_tLo2viCSGqv-l7XZOC7OSeYWCaFw_RCBeQuZFgX9OJqn11WVjuno0yQsQHSZdy1xjDqceqdp8L4mLDfysNR6hB8SPcRtYSSZktzfzsWIrIIkAPORQ1sNu7nPK0t6OOaBqge9msGdb4LbnbmtMCQX9xon18EDKCKqpcwjvdNYfN-ljb90b_P0QXoyfv1YFK26daY7GH9WZX0lKLRh1lUjRAnFRTpniKKTa1w9MzVPnqLWu6oSvcLBXUFYBQLbcSvToZgpRG5-0JGYoxo3Zbe-9GL9PlRJeFxj_37HqyM19hQsw-IAKvlSMC0-lkAbbtiLAxAPMNanQMzl4jbBZuB0AOK8THpM91mKot100DPJba55DL4ldlNzNmGFqnDXKToLk1fcEVKfP6ujfU-sAw6osEunNBV2RiDjUL88KJjw2Hm_LUrUzOLgaq90WwXhGdof6YA_z7Z3Z3GVMxQW-mQ8B70rABcxmj9IldWUO0OOVmgFvpXfA1xmHrZpbRkJUScF5mHR0egLaDlWFiyAdm1mkJ_0uGQaMIZ77nMHbo1P0odSPZp4fcGvF4LVf6whAH3NoVpNmIuueOgEe1AMXJ_GvtPqseY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=IuvjCdJQ7cYi8pMy6NAEnncaGRDMS90UT-9Ux5EUIkjt-ZBoZ-s9lkbc9psOm6hdSMFc7HG_TDuUBML_tLo2viCSGqv-l7XZOC7OSeYWCaFw_RCBeQuZFgX9OJqn11WVjuno0yQsQHSZdy1xjDqceqdp8L4mLDfysNR6hB8SPcRtYSSZktzfzsWIrIIkAPORQ1sNu7nPK0t6OOaBqge9msGdb4LbnbmtMCQX9xon18EDKCKqpcwjvdNYfN-ljb90b_P0QXoyfv1YFK26daY7GH9WZX0lKLRh1lUjRAnFRTpniKKTa1w9MzVPnqLWu6oSvcLBXUFYBQLbcSvToZgpRG5-0JGYoxo3Zbe-9GL9PlRJeFxj_37HqyM19hQsw-IAKvlSMC0-lkAbbtiLAxAPMNanQMzl4jbBZuB0AOK8THpM91mKot100DPJba55DL4ldlNzNmGFqnDXKToLk1fcEVKfP6ujfU-sAw6osEunNBV2RiDjUL88KJjw2Hm_LUrUzOLgaq90WwXhGdof6YA_z7Z3Z3GVMxQW-mQ8B70rABcxmj9IldWUO0OOVmgFvpXfA1xmHrZpbRkJUScF5mHR0egLaDlWFiyAdm1mkJ_0uGQaMIZ77nMHbo1P0odSPZp4fcGvF4LVf6whAH3NoVpNmIuueOgEe1AMXJ_GvtPqseY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsaqRcl3RCXYH9p1aljD3WQSNZh-g63ODMzo-1U_uelBoI7cSKPliyVtQ4IBTrzA-Bf3l-J1yoeiC2QzJxBjWHhEEDLFaDLfPVNcuA1g_e6wfrZ1k6fOJUabUisCcEcIcpyEyBTxrz0J7p6W7WnVCUZhO6ZFh0LrXgFtBPU9h6M3HCqB_B1sDEA8c8rmEQBIRgQCBT754JvJ2YG3c4JNnaKQAVFp3g7FQKqEFZRu2NorvjJqF28FGaTYcZBAe6TOmjhNJgs1ofBT39KujB-hxnzw57jd-CZ-Drli9j1pLkMgabdEv_BahxIfJFrvjeR3D0-PtGE8zcnwRKUbtT7PzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQWb4bgK15gvkoeRdlftHfsNaN8At3iwP7wG690sZOV7yOV58qkfuIa1tPYdc3p2FT-Bipkp84TyrNMBQFcIbR5z6zx80_hnydZ2bf8Lg2Wv3FDvpY_Ek_pAmovuPx6nMVQvUC4vlZ7LVFfFsSQLvdF1V2vdyyRSEB2HaAwBxGT9K75Xjd7m5Z1bEMHZchQizu7KiRB7feaMVuAcNtlRg40pgQYLuJCwtMJcx2lZokCxvFMDj4EeJYDATu7dIibbQr-F78MF7O2_G6k2-TWwe4_8egQyyMoINluq-MqrpP5fl9QjvCzoasU6frLxVamkj_aeGrsbddWLKEFyrqQ_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCav4_K_7o_mAPzC_fTyGjYvCtfyG_5Fz_0tCepaGyWuPTznvbCqy5niVnAPq2CNoOe5noNDWJfaQFAUl8uCtaLAHHBlYup71kqRx6vypqtPOliHUKgT9B-1Bd-LaQhXpy21D--0myt1JFkk6xkgYAAJzZsDMbp9JFEdCtKtYI3D-iG3GRhnJvIWfTs0qh1ecI0S_j2UPEqDPzyhInRAWhArL1kt4aEkyHGZWJAt3eceJzgEE-yOcz0pMGOmyunp2YeSTW7HLPmWTevRRBfP8xuYINxmUn2Q1N83NIzPmGXbAKmJ5XZ-ieiZkKstP9yxhuwes5jw91cJYZ0L4sqN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4MzTPbTXIWLS-ifvCQjcauOm7yAxJG9nh3cwp9x1I4cOgsjMq21NitkVIbG_UtrXs-uGXSX-bBjI177zBQSuuT50EnVF8ebP14aYPzA3bY8lAzVj6hI9gLOMnYB79et9EyVbOUYVEl1_3vINiAAuRjVVxsAQJuOeah7Kjy0Vq8wKiV01L6Lq8z_18mzue1vXmgUUTUHUydgTe_YKzV2qnSofzDKxwe_RgM_6ALhbmpjt-lv7aE_LQjaoyTgaxlyD1vy1NSFaYa2nk2BrqM_DF4FFOdW7QSYpIQgctHzawkm6qgbl4W7wvfp-ldunksw16tciAXTNiW2pPFi2KwKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0-l8YWbvmx-KeWktbz4a10N_W9bsCFo96K-dQkG4Kh3ufJtf4z-G0c8tjNGNMxFrRcPPeZ1492Anabjij2VQGiVD6CWUkShnmUIZUMzGPsXSHzSzw7slBLqP5AYKsqNdLWZcyCRrqFuoGi9SfU_1NGQVUYcJTahcpnasG_X5FZioDtBHnw9pzvez4IekV1DTa0siXkL6IOCJBmqn9suQawMlBs83GpOdoVVuIdaVHkuWby4GFRGX87U5pR-lnH1BGI4xnynsEn1uBqQfwaF0ioyd7Z6E8j2tF_eLtT8d5qEH1biFJnaDdTdGCdgFf8bvbulUz_gCULreUBoXfyfCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=HjAwJxhCGGr-mAqBDxu-wTTi4QCWeUDu8s9x2atwOy9AaelCNL0Kulys2O4n13GNyWaxrhpq_8Jl_vtTsgASOMHELD9fflr5qUMDt_Ql912I90wuuf-4jRJkVyWEdLPdenSvnmn7vJIU7nZKa_m2yot47mxVdaM92KSTM_0IUqCpWCW02yaq_DcWwUZptLG4Ar-pfnB33QyxFDSSy52xF37Bg0Rsf9cGcJ0xYwOrFsKO8sjufAHWudcloZD8PaqQps08qX8F28M5qz5pDyCLuZRvRfeCcVIgeH4dFHC1QUo4V6rHnSMvRWk5OEi_A53Fvh4QfNoUyH6KATiD_ASMX017dbwl-GXbGTm3-_A2MHBNeM96YFGUFpQriBx8EdtsLxq4NOUwqkJ-f9GD21S1rY8V6VBeogKevyUj44i8kHVARa5GbofEppe-eSB2UMdICrlRc77UO1bCmlfKUQ8MwqrtYF-20QILkWyzAaVBanISlUPcgXZPqgEqYpMWbCzBXNwNTczQE_VzaWYd1EyFz3ZZDgZhZhiLihFOFgBTEvsXEyanpWPWurHkQ5YPY2m9CtqJylQkCWMEaVPzNBrfzinMbonSpiJEO9_Ih7Rfeel-DF49RqUdzoAJYNpfGKqz3_EsczvK7KGe89mTOaAPGoY6-GTysjWwOuakoGVkpo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=HjAwJxhCGGr-mAqBDxu-wTTi4QCWeUDu8s9x2atwOy9AaelCNL0Kulys2O4n13GNyWaxrhpq_8Jl_vtTsgASOMHELD9fflr5qUMDt_Ql912I90wuuf-4jRJkVyWEdLPdenSvnmn7vJIU7nZKa_m2yot47mxVdaM92KSTM_0IUqCpWCW02yaq_DcWwUZptLG4Ar-pfnB33QyxFDSSy52xF37Bg0Rsf9cGcJ0xYwOrFsKO8sjufAHWudcloZD8PaqQps08qX8F28M5qz5pDyCLuZRvRfeCcVIgeH4dFHC1QUo4V6rHnSMvRWk5OEi_A53Fvh4QfNoUyH6KATiD_ASMX017dbwl-GXbGTm3-_A2MHBNeM96YFGUFpQriBx8EdtsLxq4NOUwqkJ-f9GD21S1rY8V6VBeogKevyUj44i8kHVARa5GbofEppe-eSB2UMdICrlRc77UO1bCmlfKUQ8MwqrtYF-20QILkWyzAaVBanISlUPcgXZPqgEqYpMWbCzBXNwNTczQE_VzaWYd1EyFz3ZZDgZhZhiLihFOFgBTEvsXEyanpWPWurHkQ5YPY2m9CtqJylQkCWMEaVPzNBrfzinMbonSpiJEO9_Ih7Rfeel-DF49RqUdzoAJYNpfGKqz3_EsczvK7KGe89mTOaAPGoY6-GTysjWwOuakoGVkpo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFbGFZk3pi6vA6FP7l0nCPkiyBcXerStF86mZ31HHjWHkWFZa2ZN2OMX3ND8wqz-KnQoK5jHvccAVTDz2vdDlwbI3JacKzTUhXqwG9M3-ylDLOQF9JYA1sHbBHlTA9BppSIkDVRI7oaVJWWmZ_JappOuOtIvr4Q1XvEMJexb4jGawpYzmW26cmZewuTcZBiSvDOLzOqqK5VN_uUfUW93aTliNN1NETDYo2Xo6t4R6PohEMd2NDHYK5wTFXqCNij7QUXJCaEYGNMjO9hLFXYVWLMH026nQ2yFxvOg23vVWtVN_Z_HlbogxFnmwK5bn8_yy7z2E4l_Hibga9yJxmZvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
