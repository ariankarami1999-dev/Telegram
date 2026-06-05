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
<img src="https://cdn4.telesco.pe/file/qeghiE8jeUaI8iy7zxIkIG0DnkQ3UgsNuSCjJ2lwj8uOgij4MwKXcJK7gT4TA29EGphsBdLksGURx2IoiQzq_ScWSecjUzg6EOFPGiEHO3Zs5ZWma1jYXre2Va82CO_pQ1caR4nH7fEIY-ZovabaB6OvpJX7sYmScLjup-95iPuAZL1h3uHTHCR_9MLHX0xYns1e5nmu9doYWDXZKCrHATJB4JTL7H-dDqFos3eRjqkNpxNXbpfKnpNciYVms_GOOkKb_Fv8hYuYRR8SfYxxLXlaODCgBSyhErSFs1KIn-3NUFgUK_hGbQDpXO4AFq3M6skobeWEu0l5Zq373IA9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5enZftL_oUXzwdzfG104wQSgK1hlaG7wAOhvSZf6lENQXMP_kLhYGcli0jS8xfSIXxt4juk2Tc4lvCAMih1sTMVZ2tQLnA2M_VQXJHunBqwfKMyrB-7GGJVhaxAeyJBPOVtq_-IHOBlAndaqigbAkY9V2kEyzRIYxc8HCGA4kT6BZA0bIEnnhPc_Gz2evaWJJ2GWlQpOihsh2pDUo9JQtr6ygGC-xd9hfoPCHfjdErvM96k4JM2mZrRaEJlI1cbeWQipsP582qZeiemccnLJGc-5RnxEb6i13lIHFGz83aNnuFdlc-QZvp47ZvtP-xqrIYkQXxbQeOa799rdI_-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
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
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhi1INbTD-9KGiid6nSyRXysoyi90ao5Atu6VcuzAbXInzeUrKW8GrsWDN0r8qjn3v_RIBso6Unu6xegfDMhBaTdomDlGgKuF9krbP6nAXk1cpAxQ6b1jX642AeTAOl5wlxkaHXSMDpx9BgLHL-juKbcoJYg6pXbcxj_onu4PqwsgGMOr5xcV4-3p10erIV4C5zGDyzaabAnzKUQy4IyTCXcI-jZ_4U4sbxfupiR6ZWShkzbkghmAurrUFHhreTwYK-qL-8Hf3AcKnqnGutZq8GehrMJHWtnoP0u-OFKbBX2UGiwgEyYU005pxEbYpW11cqh37OcQIhqp1um3NYhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVgeQmSJWoXiQQ4u55m8BLoCSUKZiFhV6si8msKnpA22zPz9Ruix9Dv5dNS_MRgzRQEIEiv7dCI4TZ1naSc2qlWhIf1i217mw_b2fJx2oixn0uHKoC98cIlAkJFCwlDlhjNSn2dzwH6AyEH2EZNtAY1s8GAmF3wSRFeU2-LuFk1h1S7HlLzcrSmebmWP47Fj2tLwpxusfQIhJ-9M-Yk24Mr9V7xkLoE9T3DFxSllroZlW1XIIsqWV79huCgl1n4gn8gER5pCYTHonCciMDUk84hgOZPI_NrXjyG4YgTWLwivlunSfQH0b67rbVQ6wvnwNCVq1UIWYM77Xy94WWCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ru0uFLg-MjRQdRgTw19pAyHYgJAVqqpNywZ6lU3VD8FlwTflCvlCx2RqP3s0cPf4a9T_RT2WFeTvs-xhBxbDW_CKwrrxOKd6YbLQvG-VceRVL1nXMJ1ql1xgocFwQnS4hQMyuijhoTflwi7yFGgyupzxZR2puyK-VBvyMlDZ3B4Zz8Qx90r3P0yBELi60tSaAbhrhIy1cER2wzm-iSLWBnGRj3alzkU3NGpkQgHhhKuVaHrc0s1Hl-jUZvO4PDqs23SBMxxee-EfZfM-b0QGNIjX4W8_bZAejUReecmBRP6HaP8qHdaMmfU6JTTtyHraeURjLnH-58Rj1oXEsQYL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ru0uFLg-MjRQdRgTw19pAyHYgJAVqqpNywZ6lU3VD8FlwTflCvlCx2RqP3s0cPf4a9T_RT2WFeTvs-xhBxbDW_CKwrrxOKd6YbLQvG-VceRVL1nXMJ1ql1xgocFwQnS4hQMyuijhoTflwi7yFGgyupzxZR2puyK-VBvyMlDZ3B4Zz8Qx90r3P0yBELi60tSaAbhrhIy1cER2wzm-iSLWBnGRj3alzkU3NGpkQgHhhKuVaHrc0s1Hl-jUZvO4PDqs23SBMxxee-EfZfM-b0QGNIjX4W8_bZAejUReecmBRP6HaP8qHdaMmfU6JTTtyHraeURjLnH-58Rj1oXEsQYL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OehIvZkB6AMJFtJ4xHIgqjOX8ofQ-BeWnrUPlUPoRFCUYuEYubiKNA9cTcirEY_6u8OrNf1B62GDvUu0iAVHlgUdcTBBbLC-1vdV3yAgsHEQoU0VTegx00jC7pw8vHGrQFhUOsDFdh5jPOJr76igBKnQOTz-QQK2TdkGsGh7upl3e7QmnPaBFKD716ZbdhoQVKmJOrIx_W8f7nljK65hOfMEigZ442egqGq-vnFtbLOvZUw8H5TD0_JmqDK1i3Oyt_N-CqMIbU5ItdROz2PoivFJ_owxZgKj18bpxC-0RvG0ZL0ctvp3YeLBEZoSMMPURU18y8I-841rHtxKys11JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A4R2AsnA1FwKqgsMerlpwj5RkB7sTtp_bKkAfYNG1qDvd_DbyvHEyF_rk6yicSG9hdRHOmh7uO_EqgJG08lEFGzGUiD5waY62mel4Bm86Pn8YMq1ywpTvOUQKk6HzmU1RaihPh9AkdFOkJ7w2auN7dQGuO-avm3KTXAyYIWtNe6-MCOtCu7984wwkeVZupmDDVEI5hM8p-32-gxG5Xw-Krn8mJQDwdS85IklDdMvIQpROSAfpHne9VWN8HK0YnAh9t4arIhbITNWoSuk22SPsiMT6so8LcHm99BT0A2-1nEvm8Xx6Frf2CWSRJ4OUlapo1gwj-m-4-r87hVx7UQpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cDi66_mNSLcCd3J2g1GblkjelDaquKpVGgGb-qbv0O3-OAciAM-Dn6NF17O9xr0qlgaSLe833oIv5YBg6Mx0bDbmtLSLmGffMGFtU8kFwV-I4ijy05uaTgWp621KCIfv4x9Tp1ygBUfw9QLJhW3j52ryN242FyEMNfb9r3bfzlGsuCD9esxb_9QvUwLfSM0s_5NBuvhuJ0o1WyEj-Q6o82K0ZsfAUCpiiJLCGru8110VJZqqpoZP9Vu6f6lppdZGQgFi262BweqO9_YziNHIW7ytGlaWNlOEoKu2XNGroB72ZpS6V6qyq2vuoepfzfLL4OJr3fT-FbqaEA7D46BFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nT_GuD1h8D6GxcagBaznAHidqU4rfFGtGufPxumde6Ku_l9qKgsCbohHR-DNRTrRVwnu83T5U1nHYNaGt5Q1VSphvZZDduqksx-Rryp27VZpbD_CoU7mt5p7Anj-bN5Gs2KXv0LKfWMaFR67PUbLdysv3b8IR8cyvFxDBIwAr54MCYTa79N-BF-Dnjh9mQ2fIdVKhVnjVL5HnkJUb8cy0H87YjCeeDwB3CCgYfOz8rOD0BiWJDBgT9ZZtbQCewkiFymyZXNyeG85QDF0Udh8XStlJWwSXF25zwsaYjJTaiIHP1LjbEUp-1yNi7pZM2iulmKIV2sJeupNOPlVQpnCJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9A-v9wbyl0UxMfufyme9Y7dV1xIX79ALbikF1noLO03NUWlb9Qlk8IlTSaXaObeLBoFf8Mt6KnDABYPwVBomTIAaip7DuypKKQlPPsAMvy16n2rr6tQXZcko6DCvxF_U-FVS3sClxRqNNE1x37uKft1sKSsfFT-JiJmZAh3NUjkC3-Tb8S5ce9P-oVfQlYMKWvDzYuIY3YkBlPTcXWcB_8JwGMKKaZgQtoyuqz-4ZGl3C4_EZMMVWd-jyrN_RiZrQvUt9b90LPf-0OJ3RQz9lYyYW-lSF_2JzVXRQTX1_EPSjQTwOjj5ffcpAXC-dBZcTaUJ33Fulqy_ZHm-Re1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxq8wiJouZdUybB-E-_oW64PQsAD9ODxyxcZQdLjL9rh1RnueRu97bK6rF-todr1iZLKCopQ2QrQDtagnHXMx4Ga_7jqfLOVw_JMLWqF15ZJhPMKYOQpSz0KQv8l6NzRx_jvKqKIHRCybBtqjQfSC86lXmX-L5D-UFJb48NGExYm2Tu03ur6DWOFyTnV7tYQf-j2cQthIg5ICeR6XNtOl4nUEFBM0bJMApryZ-IMiszpgNHyOt2-Z1vQEEsy3D54T0sIzoeKzyvL0J8lDiK2pz8rKo8EX3bZtX7hT6er2oWRJSQuLqEFE-dVAhnbCG3T34EorRSjV3nzJxK_nHGMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsiWpIoiWa59JCirB-yWGcp1RYcec4qOhsHaCDZI-ACRkhio3gHWYx8LQYrYEWCAVmMFKzKPZwQoalFkVx2uBAjapbw3dnM72phchMMKQ2jo8PoVLK8yMvCwvp3olmdsPTAguLub27THsX9UGLzBvzsWRsFFf80JzT5qqfW0He2fosXL9TXhp0KlWYP2ePhQ84w0N7qwY_vcRe3xqKTI0mrFGgOWqxWBleBVTRu0AFTRJHwISY6JSnaUu8W12RtgZBGiiR8HQzktoxBwtj1TxTsaep-0WyyHGuTSvxkLizv-HMtInhWl2gRdVxwGLFNmx0Zpm7GRJvdOkkML7722WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFdFGx-sF62jReH3YMgZz5RT945tgHLMtsSNWyKRBRq9dngpTSYNAqwVhSGvgX_gxPF5o7Ty4JB_jlxmVBhEPIcOqIcy-B_tkqlCrXghUtuAv2Ncq0fxM5pz7dChm-NDVJGLrmZwTIfALSqLrvLsMIouBUHzyc7EahwhBMBskXGodI0mGDxgqMkzW6dRTcJAXelYzPGDVvdTwQa4CjSA8e0LyXoVb52jTrsquG-bB36wXlE31mE9HvLwaVgJ78VLd1fATYvgTcNeVH8eAswrVlnJheHcALWP-9fNf1hbepgPkapJ0N6gN-WmsPuv10pJbFbD80BuIzSzORK5uPvapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=K0IPzJC3VCT8V8mQq9SdG4Up0OZODFFH3JCyYBfP9JvCRGuaaL2sIGRDVgWkmObpfXogM2cazeykRAq1Wc5SCwjklnDAOmBSS7lbXyQJyAe5UHM8cHUiiaZ0BjWa-7LkmzHh735ZSdG406C0cAPWUavNh-OQFvpmi7XKeWBZR_d90t2ft1WKgocQefwYzDtlBRJ4gGeHwwvaGIyPkDA1bOZVmX810IVLZWXyeOwsr6k3dQgzt0zji2WCK6GS986bP6qqUj--z8-zDosKW9KKd8XfQdb9MipQCqR0uBX3IiS9iEhJmg8z0L7mbvx2T8KK_Wnz0JZ94Ase-ZASfKDAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=K0IPzJC3VCT8V8mQq9SdG4Up0OZODFFH3JCyYBfP9JvCRGuaaL2sIGRDVgWkmObpfXogM2cazeykRAq1Wc5SCwjklnDAOmBSS7lbXyQJyAe5UHM8cHUiiaZ0BjWa-7LkmzHh735ZSdG406C0cAPWUavNh-OQFvpmi7XKeWBZR_d90t2ft1WKgocQefwYzDtlBRJ4gGeHwwvaGIyPkDA1bOZVmX810IVLZWXyeOwsr6k3dQgzt0zji2WCK6GS986bP6qqUj--z8-zDosKW9KKd8XfQdb9MipQCqR0uBX3IiS9iEhJmg8z0L7mbvx2T8KK_Wnz0JZ94Ase-ZASfKDAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5xoVi5rdmseZTytKspDnBI5xLOqkWXF90GoGyaCDciIVflcITQWf5loM7UUakcNLxWWzRwA9CEvsKDBWlzflqX4Kba8Vu6leE9E3vRsjXrHpGNmgfDVPw7kCQLzhzilwlqDeljYOr5Qpz9p4aiaLXWz9Nmjo7ObwY9NokjPGR0bBshHnU15N05IdGgZwFjwOkVmZksJ0mAywmXMVpdrGu6kx8wzVwB8q6tohKHFQOmzJKFWB_AFbHDLxyZT1C_QAYXLiuSdhA9FqgpBGTfbwvwNRX-P75Mb24i26zHuNEwOdLxFEVMDznUagRFKTr5V-nzGUz61k-IM5gwsGX2ZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
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
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu2gcUpyu5uFj2gOKjqI2eDZMSJXqdcIdxiaxr6XrUeFaGDWwJWwnMbU2YvkJBo4rCSCbezeAFt1hCCFS25hQLaZ2mJwZSOK2BicPEaTqcZhYJG2ex8PLqY1KEx7Nhc57YDF7H80OETwFQFF3wTHPhc2tbgXAHyI_m_5mBMzys2fNdK8jgEdLLKOwIUJ8BhjxGhCBDvsGtgkgA9yh1H_kkz5JMGJbzSZz2JF9wJkNM0zyU1i0mrR0FMIJ4sHpfzupNPNh6-jU-gwjQY1H7t1Gzd67ESOwA3QG97tyUyIcqudkwkeBDCiUDCBLJA-0wrVb3wUSSwfJ3k0R5Wd7IlAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CibgmHCRvAyZ7D40PIWUAhCeDBQzAWkJ2AcfAwxfEtU0hL9QdBCnAsFEQmTp7aAjp0oETvxJyygokBG5N3OeONSGrPmf9oTz49kyIVLEBQDBKvaMsEE3MVuxm07KYE8T4xnXwDzU_PerkVc_BZZ3Cm0Cd6gzpUHEFJbbkdUQPrVjZnu99WlzSbRr_pa6NtJfTDUra4plAjdgFT0CzAAA13A5g-P_BSa4wmPs_yneE4Vuh8l9VioeJwO0IFfqcG2u36K1wurrpNOstMbT1Q4OmOJ8WDlToQDXVZNaRs-i082bggLia-HybMeTl2ACmZ3L8HJWBBcAn4f6M_luCl4kwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=brCWb1AGxAvYt1GV_K508mK0e8Ny9ICLphmhn8CSjLiJhjnuXeEprPPLdU6At7UxtqNwPF6JtqgrkTu_p1Ca7QcwDXtWXCYVUEn3vlaIpHI0mrKEYjTz0g9FglUR1ER5h53T4U-i--Ouq4l6wY63dHSPGZK_x46d4xlDGi68w0sHBNU1iY2rbcfl-843UTqpQ-dHrUNKkbYTgEss07CwauJCk0bwZnFgF9umvZsDJm-p78Apk5UYvkD6iqKyKMTaxXZe6qd3lhHstpUGLPCUChNkCns5E6ciWYYXtxHK4Y55nVVt9fG_mG4p6jHLt-ERkQGItUmW_VurUGKPGzaFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=brCWb1AGxAvYt1GV_K508mK0e8Ny9ICLphmhn8CSjLiJhjnuXeEprPPLdU6At7UxtqNwPF6JtqgrkTu_p1Ca7QcwDXtWXCYVUEn3vlaIpHI0mrKEYjTz0g9FglUR1ER5h53T4U-i--Ouq4l6wY63dHSPGZK_x46d4xlDGi68w0sHBNU1iY2rbcfl-843UTqpQ-dHrUNKkbYTgEss07CwauJCk0bwZnFgF9umvZsDJm-p78Apk5UYvkD6iqKyKMTaxXZe6qd3lhHstpUGLPCUChNkCns5E6ciWYYXtxHK4Y55nVVt9fG_mG4p6jHLt-ERkQGItUmW_VurUGKPGzaFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=UXvyoaTcUrNrOVQ0SH__MHUv1CmDXhwumgAdsbxjU6cyatQNbjyZQwlv4vI2Z3Rvd_ArfGR4xR2LTLg7i0aii8cSNLNSZpdukm1AaMkw7dN8xJV2IeUfceeeqnfUqdMGFObhFk2Aa5QdEQ74-aqzVxo2SXK1BFquA_JOq7UwzZTNRUXD_J9h3jGWSbuAsme6p05v2DjgP_jIh9xkdkcwnIrMh2VmN4TnyO499bgciITcG6vrh3ZDc8CdcdMAI6kcK6MCMvStXauK2wd4Cer6K8e3zSwk05SFnGirThl8oBjOZbsiNhQbFhbDli0biV1tCXXhMC82EcnMmo8vYTwkPGLBk54dijCwwyIO0PQvZP9F-yWrMTSRgTKEv-bn_ftUx5kvcEmayS1aZOBjkS779qi2NYei1hO9E4Hs2aySqj57zEDYW44hTNBqbQSnJi_DzoGxE8FsbMUXqPfco8r0ad_GigVqtC_a922FLDBJ18DtN1uB3JDGwo6Q1G8GCAiMhu4iaEEtp4Y7pnNIWEVAhjfF9JNgxKzQncj5WNKEgeFwt94k2o89qXO3D5A7OwtOsgUg8p06sDLKAKJjDD_wykwZDm4qm6J9fVY89SfkRYdivQCR_iNxXyFDN9F-HGDno2JKoi2aSwzT4_xLhJpPAnSGd3Ncgi97maVFOpWk7n0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=UXvyoaTcUrNrOVQ0SH__MHUv1CmDXhwumgAdsbxjU6cyatQNbjyZQwlv4vI2Z3Rvd_ArfGR4xR2LTLg7i0aii8cSNLNSZpdukm1AaMkw7dN8xJV2IeUfceeeqnfUqdMGFObhFk2Aa5QdEQ74-aqzVxo2SXK1BFquA_JOq7UwzZTNRUXD_J9h3jGWSbuAsme6p05v2DjgP_jIh9xkdkcwnIrMh2VmN4TnyO499bgciITcG6vrh3ZDc8CdcdMAI6kcK6MCMvStXauK2wd4Cer6K8e3zSwk05SFnGirThl8oBjOZbsiNhQbFhbDli0biV1tCXXhMC82EcnMmo8vYTwkPGLBk54dijCwwyIO0PQvZP9F-yWrMTSRgTKEv-bn_ftUx5kvcEmayS1aZOBjkS779qi2NYei1hO9E4Hs2aySqj57zEDYW44hTNBqbQSnJi_DzoGxE8FsbMUXqPfco8r0ad_GigVqtC_a922FLDBJ18DtN1uB3JDGwo6Q1G8GCAiMhu4iaEEtp4Y7pnNIWEVAhjfF9JNgxKzQncj5WNKEgeFwt94k2o89qXO3D5A7OwtOsgUg8p06sDLKAKJjDD_wykwZDm4qm6J9fVY89SfkRYdivQCR_iNxXyFDN9F-HGDno2JKoi2aSwzT4_xLhJpPAnSGd3Ncgi97maVFOpWk7n0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCXUidP7ZC1UgDmJ3TPJCP-cvfL_EXrAqHUxkXcYNjKIxSW_nz7UFiJRmbmj8hwJXg0EM5FRoEscXmhl1ys6lj-TWM5ZQP86CtQm-r-BcWTHN5_gjyLC65pa2ic7EP50TFGE46V8-pcSBFGvyAs-Q0a3XKk9GVdYq9JdIkJr_l6r1-VRF6E_P3JurpD7D6IDdSb97XN5bLyoM5Peh46NVn-M1geAc1cKgutkClY860cy85RxxOF5qxIf-uKQcyAsHCyn3QZ1XGpHUaMcvrpN76kZmx10mXriJxXUzpoov2dam4eHxvU_F1HuFJD-iUI3FKv2GqG2OMhm135ijABTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
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
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=fStrIDAsWMrWuLFlFHsEFTdnyZoFizpTs6sjWCeMU8vXtQL_jgGT9CIoKrVcHj60FFICrfQmNjkhA4aGK4lfLsMv8YG7PaQ7hKpc6PHW3Sl4GRZYwcmp6a2evzzGgoRabiEQLbbEkzHMQ353eTfuiLzRZfwkr8aSA5Lv5LzIno5qrBCzb5gWAI2BmlH5z5nCk6-QXdlKMKwmv4cz0b33mMfVogBFfJVE4tzvyhUiHvEA01ueSWMnLmRRrgp6zPwcNHccJRWbBW40auzXoZaFaW1z-LccfqbpeyP3LRWvUfs1aEKJrmxhEvy6R8olAjs_HFoQAq5uGHLOr5MNeGvYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=fStrIDAsWMrWuLFlFHsEFTdnyZoFizpTs6sjWCeMU8vXtQL_jgGT9CIoKrVcHj60FFICrfQmNjkhA4aGK4lfLsMv8YG7PaQ7hKpc6PHW3Sl4GRZYwcmp6a2evzzGgoRabiEQLbbEkzHMQ353eTfuiLzRZfwkr8aSA5Lv5LzIno5qrBCzb5gWAI2BmlH5z5nCk6-QXdlKMKwmv4cz0b33mMfVogBFfJVE4tzvyhUiHvEA01ueSWMnLmRRrgp6zPwcNHccJRWbBW40auzXoZaFaW1z-LccfqbpeyP3LRWvUfs1aEKJrmxhEvy6R8olAjs_HFoQAq5uGHLOr5MNeGvYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTN9tF9HyBfd9cZIDPuo-FGNe3rLPy-o9Yehjh6e5nsjV_9vCDDCjk0kT-_3yw9CJoonXk5MmMACOm9Vy9etlh2pkp5Z8Ou7R-QWAiOoJOE9HxBAoA6H2w0kt2bEcBRtcU4aiKHmrVq6H4KyQMTlQasC7lMKx8FkiQ7eTbVJDUHBUVeK43QKu3PWke7rcyEr2CgwHKbtWfsTl5mJEclHygRI68k5UBMvi5rPNy6OTUST3ZFVLp-HG-AMPgK5IL2yO5d43f_2mZne85fEbfyD8sJTRJx3-sCgvtckLzV6uSQuLzO7rapqRQmZkuBD7G1Php0F7GKFC6ioeCugVt-tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=jBY-MUI4jjJKDdE3VEh9r2Ny2f-JQltGrmO1nGeek7mjX3OXLdoQFcQnjxJeEy3ox8VBaFRJF01mUOoGZeuUAxv8pVJbJFyuPyUhj9VPI1_WAV10i0fX79DM_GCvnNJjQp6s-BzQ-jrUkhdeLZqy7E7PGL1ytbv8L3zjFvaDbBudMGfsZrgqQ5Coc4O8FjdhlctG59sK_d_w-bhkQJX3VY3RQN6ztlZ5pmXpQ4GB-gI71lParNaXPf4nXtHLN0GHtXwhgrC0rkPjpmlZL5AFu9Rmppx_eYIbw1WFtgkieaMrGftz-gHA0amvy6jdOv5zg7wiWfuEtmB_IgmkgyLwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=jBY-MUI4jjJKDdE3VEh9r2Ny2f-JQltGrmO1nGeek7mjX3OXLdoQFcQnjxJeEy3ox8VBaFRJF01mUOoGZeuUAxv8pVJbJFyuPyUhj9VPI1_WAV10i0fX79DM_GCvnNJjQp6s-BzQ-jrUkhdeLZqy7E7PGL1ytbv8L3zjFvaDbBudMGfsZrgqQ5Coc4O8FjdhlctG59sK_d_w-bhkQJX3VY3RQN6ztlZ5pmXpQ4GB-gI71lParNaXPf4nXtHLN0GHtXwhgrC0rkPjpmlZL5AFu9Rmppx_eYIbw1WFtgkieaMrGftz-gHA0amvy6jdOv5zg7wiWfuEtmB_IgmkgyLwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgWr8VBzGfMukkJs_tJ-b225A5tzYN41BRnuFUFeTiBaWot1brNfCV5yrrMXKK7kxNDftae9pUZCuMkTF9pn-uQIA2PXjFsINhjswCaFWHfV5KL5VSJeTHyjxUWQV4z-TnHkgkfiz2kUqdpaMt12Th8CYNa69eDJpQfISGncM5RxaZ0PJLr1fW1gDll13xL43ZkJPkWNvh_c2nClt4nyXP5L7W67JCNvyLYH2bKLy7aIHhMK3EUCJGCosbfdtzRl7XajR99pd3rkSbKNaNqEzZAJDFYadVs70mifnniNk5oyQBRj61qq_CxJjsy57PlU65-_302jhV5UPxRTYQZbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=EjcE_-4gii7B23sd10uYkUwRmvgG__BCsO8-X5F9MqkTVqYrs9BQ1G1nKLA21oiL7SqTW27tAMgL9mamBvc3aK8KZuM92cZtemcnSN146UBq48EK4UoYMww1ap1s6nQTwK9d41jpQ8sEs2qlJm4a0MtJdYEr7qE_HCCuSoYsPuouwTLEeDkej0EehZjmKR-4MbWRCJJOQiOBLD82DasZA2oC7fwZ50ZKpmdCLQWeojFGOzsFvBke8Q5qg5VCtyrlO93fIPfL_wjTmHShs4hoKN6L8IrKu3JbKoXuUlLRgJ8Dsr0W_BXInFZ1yPN5QYY4rE5ohSZOJnIvMXEviAwTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=EjcE_-4gii7B23sd10uYkUwRmvgG__BCsO8-X5F9MqkTVqYrs9BQ1G1nKLA21oiL7SqTW27tAMgL9mamBvc3aK8KZuM92cZtemcnSN146UBq48EK4UoYMww1ap1s6nQTwK9d41jpQ8sEs2qlJm4a0MtJdYEr7qE_HCCuSoYsPuouwTLEeDkej0EehZjmKR-4MbWRCJJOQiOBLD82DasZA2oC7fwZ50ZKpmdCLQWeojFGOzsFvBke8Q5qg5VCtyrlO93fIPfL_wjTmHShs4hoKN6L8IrKu3JbKoXuUlLRgJ8Dsr0W_BXInFZ1yPN5QYY4rE5ohSZOJnIvMXEviAwTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=s_MPFKwzp_VBRX644waaXQz6Uiy5OzT_5QOiYLPExIBwFjaRUD-vtid4bPC6itWj1fpigt-7LEF_ptHNm7Ftq8XOE6WbQDvwdpamgrTjcaTXhy3FKMwAqw9gYVHVWdaulCs09wg2ygDevG4UDpwLGzsa6Zjpokge7KOmHWeg-t_StpuZG9B_ZsbCoKzc02DJONa65L6WPLmre10aJBKCoeQ3TJIzSvoPIRqj0u4SaZiXtYZ7WhZLOmK8yjxYfMN5WtJCRIv7YgF0ZgbksFvSyZr9krUE0CozJAqCkrMjFQDqNncAiib83E6LilKWiImx56lIR-uodeg6N93nRl6lCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=s_MPFKwzp_VBRX644waaXQz6Uiy5OzT_5QOiYLPExIBwFjaRUD-vtid4bPC6itWj1fpigt-7LEF_ptHNm7Ftq8XOE6WbQDvwdpamgrTjcaTXhy3FKMwAqw9gYVHVWdaulCs09wg2ygDevG4UDpwLGzsa6Zjpokge7KOmHWeg-t_StpuZG9B_ZsbCoKzc02DJONa65L6WPLmre10aJBKCoeQ3TJIzSvoPIRqj0u4SaZiXtYZ7WhZLOmK8yjxYfMN5WtJCRIv7YgF0ZgbksFvSyZr9krUE0CozJAqCkrMjFQDqNncAiib83E6LilKWiImx56lIR-uodeg6N93nRl6lCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXjN3P5jKwC9yMkTrkMheQ4BOuLJ-9_F2ZK4NLrs0AFYkkGLOFPfHxlZabABmyseU0qcuHCsnymVDvptBb0ud4nqYjgfnLU3TOxb3u5-mIihucmpWr6enigCj5nZ1gLssTdaTupKW8ix78XTGnK_fZ2p5IQh9GgDIEj3a3pCuwodG9VoQbS9PLcN724MD48-a65d6CX6CZ8zqwDxt84olHfI8wN5nWJhm5QrAtaDYU8JtMlsGS88Mg7fSe0eYqSzoOeoxSYSAuTndigU-C7Qay8hwry_BzlwHq41wTkAWcRnnmm8d86YG3UsmHAEe8Xt_Fr_QNWhUTFyMkZXP3rd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=KM9nq3M0XyDW-yMLKDUEsSCJoAU64LyLk9pLEcBcaQJ_MfRbOqvGUb4_I5DewOjfyum_bXAUYM1aE7cRBoMpk-zC7YCz8kb60ZJcDvq-okPvCTimFp4T8nH48wN_82Xm_fwnr_x5WhqEcViTGCtAFBFFKK8TxLaJG3VUEdc6PjuBMknGnX_X7MgSGsWpUEAKWu2ur1PVBWsW-ppvVHIENjK34jZMBBOuBHhsBZj9jzf8PVwWUoEHg3FcmhU4PvyrzSbVqCwc_cbUGmms0GJkdTI7GrUVjfhgY4LODl462iPpONIvhYgAqM-1AmN1yh6pNlYAIPXXJTrV6i0ab2aQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=KM9nq3M0XyDW-yMLKDUEsSCJoAU64LyLk9pLEcBcaQJ_MfRbOqvGUb4_I5DewOjfyum_bXAUYM1aE7cRBoMpk-zC7YCz8kb60ZJcDvq-okPvCTimFp4T8nH48wN_82Xm_fwnr_x5WhqEcViTGCtAFBFFKK8TxLaJG3VUEdc6PjuBMknGnX_X7MgSGsWpUEAKWu2ur1PVBWsW-ppvVHIENjK34jZMBBOuBHhsBZj9jzf8PVwWUoEHg3FcmhU4PvyrzSbVqCwc_cbUGmms0GJkdTI7GrUVjfhgY4LODl462iPpONIvhYgAqM-1AmN1yh6pNlYAIPXXJTrV6i0ab2aQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKBbgKskL5V-qNp_Og0wyNuKcvW3IDf0FSDRDvMgZLDhEIsQmiKrq0yTShzKT3T9w-XI5MlCkNy9WSfAhjen7LTIlQUNm8BJ0pXN3nZkpFrTGaCacX1ecW5jPzp4LAUfCHc1ENXwCPQ9C0sWNBMbe2o-CCRJ4xZKamDk9Bx1S2wu4H7m1F_K5lP7FmddulAWU_P8Z0ivazAaQM4dxgN4TsFQ7SBtd29X9NMFo34sprbhsO9wvcWVcTnqlJjpYWdkcMructrzeMxZ4jwy-m21oS3bcuoU-dr4VM0WS3CW1U_gBzs6_5UOivc2mq4J9pA7DgFkEamuoisOSp9wrAQ0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=OKV4i1FlGvoEWjCc_IV53v_LMbYRKsel7_XgqHTekThdKN-gwmbrSA1tcvhcokvJWaRInDfcRTKOJX73GIFSdAj24yO_i9IswOMQ0oqeqsBOlqnjsnvWLrk-X1LWYWIjiOP_h_wvxUh26H867fxkAPTXu8gzXaUF7k3d9alHJzUSGjwYqCJikRh6FY1OTvUh-q6iiCyq5SbcED7cIiEMEGUTx5j6D2iJetYBSIXFQiOteug4AioW_HgNWcWo1Dv18Fq_otFHldZIWABU3X_gGMeHt4MqA69rpzd0V0WOq9GIylfJvx0OTq9h8Oh83Hgt1BxaauvS0pGMTjfifT5OgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=OKV4i1FlGvoEWjCc_IV53v_LMbYRKsel7_XgqHTekThdKN-gwmbrSA1tcvhcokvJWaRInDfcRTKOJX73GIFSdAj24yO_i9IswOMQ0oqeqsBOlqnjsnvWLrk-X1LWYWIjiOP_h_wvxUh26H867fxkAPTXu8gzXaUF7k3d9alHJzUSGjwYqCJikRh6FY1OTvUh-q6iiCyq5SbcED7cIiEMEGUTx5j6D2iJetYBSIXFQiOteug4AioW_HgNWcWo1Dv18Fq_otFHldZIWABU3X_gGMeHt4MqA69rpzd0V0WOq9GIylfJvx0OTq9h8Oh83Hgt1BxaauvS0pGMTjfifT5OgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=m6vA4J5RHGELRa16cydv6_2nDznLFSCVnLT32g7KClPLo_VIE0vQoNEvNwHmzolQXNAs--hbQdDYWONUpbF-eHEHVZRLFcR6K5PYPaZh6ncROgUp2HQLx60u3OLPKRVExKxG1t4W9d14zXljysIK3l4C_COHUoimWkwaL9eZPHlowBJDzCQose_ykHu1AFC0fSuJ-9O79mWADvqhrBcyIvGqf5b0HTqhVpr174wg6z5RqrCN8DAB6U9efmla6w8Po_1yXIEpwHt_pWDZ-ZlV02FEkrseHYdg3Imwtl8E-M7vVaGRyLuXZ68ScqaQbNBrrgyNnigVYtYXFT7Fsy54Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=m6vA4J5RHGELRa16cydv6_2nDznLFSCVnLT32g7KClPLo_VIE0vQoNEvNwHmzolQXNAs--hbQdDYWONUpbF-eHEHVZRLFcR6K5PYPaZh6ncROgUp2HQLx60u3OLPKRVExKxG1t4W9d14zXljysIK3l4C_COHUoimWkwaL9eZPHlowBJDzCQose_ykHu1AFC0fSuJ-9O79mWADvqhrBcyIvGqf5b0HTqhVpr174wg6z5RqrCN8DAB6U9efmla6w8Po_1yXIEpwHt_pWDZ-ZlV02FEkrseHYdg3Imwtl8E-M7vVaGRyLuXZ68ScqaQbNBrrgyNnigVYtYXFT7Fsy54Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=CkYU0Jnf4lyxPBWR4LrX_g5vCW2PwLlMFHxw5aUwGOxu2IUnNLXMQSshqpuwtW2gEDaD26fC1NagWvbIp3HLXaoQwALsGrxpxR1ughmEC5hj5eRtdWHxRy77W-H4a0tS-7HiWHddz9qXg1nM_UOuNkxx4BgpRBLztjvmVE13blgMVK_2iiubA2IzdzPcEA7ceqHxJNdwTBhZOeO8uY_IHuYj4OCOPuxvCmfXqMzlAWFj8XKF3e3aouNX-Cyt8p87R3CMUOY-E4fRCmayVT1Oc9Eph71iWf_yqmyCCFf5LJCt6npcDOmc3-4F22YH_UFW1zyEjf3Ewfel22rRi0SsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=CkYU0Jnf4lyxPBWR4LrX_g5vCW2PwLlMFHxw5aUwGOxu2IUnNLXMQSshqpuwtW2gEDaD26fC1NagWvbIp3HLXaoQwALsGrxpxR1ughmEC5hj5eRtdWHxRy77W-H4a0tS-7HiWHddz9qXg1nM_UOuNkxx4BgpRBLztjvmVE13blgMVK_2iiubA2IzdzPcEA7ceqHxJNdwTBhZOeO8uY_IHuYj4OCOPuxvCmfXqMzlAWFj8XKF3e3aouNX-Cyt8p87R3CMUOY-E4fRCmayVT1Oc9Eph71iWf_yqmyCCFf5LJCt6npcDOmc3-4F22YH_UFW1zyEjf3Ewfel22rRi0SsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=go5Rqafl09SiqUCviavbbpmIwmxW1uOG9sdfF0aZ90nHDnPU3QmPGy6IRgx6U_iQlpSA8DPwTPafiEap3BQSdOF572nq4jH_Y-9PLW6E2bslSh0VdOlHMzzRo-CwDjPKUDAjfsy916VtI5dBhlrd9uaMOgKBQCbDhXHfKs9MPMdUycwTJgFMFzygrHYRUTDSwG4XgOMRKB33itHLKGOeyrDnRHiPEaimbglvlNq3UFh-Enp33vIBqRGPe6LGglEWb8wj9QKFEIFeoW0cOOf_R9snr13J7fVjtBZFYTdlcsDz9XqLKoL1fvvMvzsbqZaj5VkUK-NncLzD5VEfSBCieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=go5Rqafl09SiqUCviavbbpmIwmxW1uOG9sdfF0aZ90nHDnPU3QmPGy6IRgx6U_iQlpSA8DPwTPafiEap3BQSdOF572nq4jH_Y-9PLW6E2bslSh0VdOlHMzzRo-CwDjPKUDAjfsy916VtI5dBhlrd9uaMOgKBQCbDhXHfKs9MPMdUycwTJgFMFzygrHYRUTDSwG4XgOMRKB33itHLKGOeyrDnRHiPEaimbglvlNq3UFh-Enp33vIBqRGPe6LGglEWb8wj9QKFEIFeoW0cOOf_R9snr13J7fVjtBZFYTdlcsDz9XqLKoL1fvvMvzsbqZaj5VkUK-NncLzD5VEfSBCieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSQmArFBJIoPbf2uTej6lmsYbdJaiQg59Nk9pbhT454weymgskHHC2AsbFBKvFMCYAQ_pJvtrvM5wLmNUOvWBWr4jbP_CCYN7UvvFAKLlrPV-rkon45PJFZlTy31GfbbxEHu6FftQPyIiE1eo9hPfufQqJrkrmX6CXA5N9tcknjQf8atGDyEN6gFI0y3mM9LBjBkJ9sGGwZzI3ta4GWjjNIR8ARVA_2eMVuPnz0ZV_l_VRwahJ_S2nVTP8QLdgEqyMHNfogZa9ujMUQaodzsv7zU-804Jzy7176fz0vbkQaUbPj_btJ3Pw0LCTOL-uOmMmCXKpeIC4yBEr4hU86_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smZddcHgQcC_D-wQ8IcGeuyvM1gFyI7rxxKU7YZ7f3kntZMTYKCIOVhgcIcxEpyY5wK72khsv-nBq7Rrsa-_I-fiHx2GLpt4yBoEfCV-iBWEMMEIFQsKZ2yuG9tk-QMl0c99smCXfR5ev6I17OPb55a9syKAD9rc2evX-qhoIjEHhxGuKGD4SniXSTyKc5HZyLKlFB54VuWNoJqMBa9-0Cpw-4BYhv-rCpI_UDvkWnsi5n_CEpCBFqaXkXZy44XQBgtv0cRyNIbv_DETTrV8eU9p6UlhPZiZNOvcghe_-Y0XVerTrLtwYATcN0Lojad5XTEPGMJ2DYfU_Ik-1V8hjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAPVvaYRTUBJx3gJML7BZcqpf8rs5TQz0igbMo9JGeBoIp_o2jeLmvgl4mKm0ZjDLGsZ-1e3CcwKwMXb007sAgdSXQNqPc8XkSVER_Xgsk98l7xieqrO93oGGAY7SO5fgW-4ljt2AktIekxfpvmcfAy9s3tqtGa6P3YLKL-eH6XTVRsyt7pq5yWmSpAPxnsrqakKSOxilYNeVQUZNtwUTDKbFlsA6pmzu_rZIBfpKauhXFKFIrA4KB2yaZs_-TEXsHCN8MGIdvKLSphGmp9OTQlweui9rmzP7GSzBWN2UccdiXEwr3Ge3gKGcColpz-2omo29y5ygPsKhktYhRYJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmZqlAxmcnkDysf37D0oKUHmYcZz4Ikww6_yowOKzj59acWThwLTD79Jjabx8L-3rlQP2B6idZdL0YExwIdTQ9ee4TjeHzhsZrZY-SO6Z1fLV2La_cj_7DJNvaR0gfG1foklQG6up0JoprDnV90fCMZ3RsHI3SFS0DUqJe-sb4ough1NO6Q1POqi3X2fbIKSo7hmeIdRaouzAas8T-OPGtfokEhr4QbgiuMhSjXakOsqU1XN7zCQGxOb-weVCdMiYfASMI4pPS1EG3iIN3MsKsOvoq79SfZRxuf8uHWu6UBLVHUtHyR9SVaC4YUvTRYskugRbWlknkeHaTA1n0xUQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-SKtYlyeFaw5wsFOC-p0AXRuyZKwaJPEclRs2vcJLs9wqDo8ult6ckXB-C68KQ093iUe-rL6tFvk29QxrDuB5FUkkB-5ZhIdMi91vOKsGchaC6UNrf8XWzzvlt8veSm7KKCIGm2tUo2tMssDKFqbo02UckcuYN4bzwoYy3RVzn8GJ8T1v3miPReaTLaCyveIsntDKUoJQwrlPbm0GTZ2tiuCcpyjWFP5oB9F26l4iOHDZ3Ai9Vq5VVKlm1orebdR5i0SIQvAzVPYKa3UolQLi68HL3_B91sHlq7lDYWZSW8sumUjvF5m6Gee_R7i87WsZEMWLXyexfmzAWW54180A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=QR-DfG5gwSs769HG7Il-dYVyp6E1lE8o35Ivq3wuW1g1STfcyf0c8assmDe7M2JkReXry71336vQ7nKapHVvVOG8Gg1f1psq5aOitKYShzRAgzdUjRhalwQ2vJmi-b3TDJBZM75WbIFipWu35h8bd5g9Hq5ya2CUnNm5n-RSg_WqsxOZzgcq1OZgo53bYP1MmLZ86XoudtiKZPzGlROYrTT8f2gQ_C3snBwLKTccOMIaJLvofYJfYuJRSPsrfXw_SxcmSHsIqN8wHlHBPersi82ThjATJQFI6tn_dG0xk-XR4Ci5kQtFhZLynrgkdYHkY95PN-dUsUhOvFmRDOknwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=QR-DfG5gwSs769HG7Il-dYVyp6E1lE8o35Ivq3wuW1g1STfcyf0c8assmDe7M2JkReXry71336vQ7nKapHVvVOG8Gg1f1psq5aOitKYShzRAgzdUjRhalwQ2vJmi-b3TDJBZM75WbIFipWu35h8bd5g9Hq5ya2CUnNm5n-RSg_WqsxOZzgcq1OZgo53bYP1MmLZ86XoudtiKZPzGlROYrTT8f2gQ_C3snBwLKTccOMIaJLvofYJfYuJRSPsrfXw_SxcmSHsIqN8wHlHBPersi82ThjATJQFI6tn_dG0xk-XR4Ci5kQtFhZLynrgkdYHkY95PN-dUsUhOvFmRDOknwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn42bRThi6cZAxL3I4HbgibtsmVP9gBgSkuKhpxq5FGnC6In-esOD0vixG5JTu4TPLXeWEpsgLfRwhuC0I9Vm0ozRx1mDRg_lDAjUv4G_aOhn8rgCOEFx43lc2uE1SQkzFfU8njDGPMpuG7uz7SCCv20q7rOaDHRTPgFV7gZr4oaawlwY06DhRX6lPDSu6-Wr3UJyh5DbnCcZgXajnRcgasEK8h917zox9GktVn6O_5nl9__wse0KEQVkQa2Hm0AXcyfuPU0aGyefN4ZUJkg09ZBo755bwxPqRRCNqM4zW_liwiTLqnJZnd6BOtsUSG5Dtj5-Ex2KBfsClQCaWnDyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siFk7R_pDIjM3gWW5doJjRJ2kVYMcM6v9HDxiPbZJhPGWBapWXGubZi-kYR5p-Ni6MT8wU5QyQc3tvu3oghJIwukSejMGtY4uGsjXERoFLp07vKIC3P4Ar-X0t4hI9yyXXyMzR7D92yz0GsnVyBGU8bmPHas0ZT2xYnbZYHdpgCkZTaQpYO3DGMs3i8fBBgMYzkWryGbR0SiJ4ISqnAEMrPEEww_4IOOKU0n7ZYtDzfBOrZVNElAiWJojmV4FzGVqpmSR82fKgLf-RDTrk6LpjfXNI7ryc3ifP02rsdxS_MbDp4Rgn4QB9ai0Q0w1fbAuBefgM5jmB5TIhe_Jr8O2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzSyosARB3i7GkWvAU7Zyp3_qogKo_7VJv23GklWK62i-0Ni-3jFF4Sfxtv41vNuvydesX9-z5e0wiO7UOv0hZ6HmxwETpwzWJ2ztlSC9abdenL3Alqktnv2OW3aM2pQXe9aKKGKNO95xGYGBG2K-faXww34CXhlC7Yti0HRfWkjSHdRX5b_vl2pXOlQvtWE0Pb8h-74VVIjxqhw_JP1HtzzYsd4UnzRbmCBqO7DXvAYGqLF8dZ54vCa_af3uui4PDAfsWOzQy9CVbgL76qUkISRKKm3zCteaY6qGgx0sfjgM0-0Njn16sRFwhwwpF6Jjmh7qYXtjs-l3MqIUw4Xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbDteh-TeEmsdvi2Mva_K2RQB2PtaF4Ue3-RiaoutNEoyHmednKNcVObAxPE48dcJUsPT6nbxPe4GHEWh-1rbDFhc1xZtuGcJB4dm1fWRFTZ5m_LmIzOEz2ArD-zpv1jwZ-D6AEahlzJNxB84izOENJQNAO_bPzWqDpa6W81kwO1nbExtEKY7sCPK3rH9LaxOpyTv4zyajV1F_arAw3VWtboqncd1OuCbQpug07amTlreRJes48dVUJvpXNbS6f4rEXHUr9WjZOqNGJP499n9vGog07R5kp9fvtK0NQFGwt5evzemxEclSDSxtiyFs_KhRZIQi3hY4pfH9-w2aiF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siYg-MvaFq-wIL8bSe_QVkmBuMjJWL-2ZQ7xGtoLwQBZbf7REtd90CPcPupzhBW_vttfWei7rqOm5sjqsrrTISdtJOG8d63FdlOK5hPGtzFndS3dVBMdQw3jwIQMYG80gjH_c9dbS_UOQhArA1XXFjNIeKkR7Xl16_xCol0tVZZSL-FHDW_ZxKuvqL2vaLSWi6RfEUhcF7G4qj7rD7JYYz9yWtdMYllgyjRzWs2LOJRMBPD_Fo8WPNJVw6J_m89qEBNFWIZBvkI5i23H4DTwtMbbms-IikGYV1Ir4z_i7bX-lNa1-A2xwXGy7knSs4ta-aXHkp1xJwGS9DffZ4Z25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgMmZS3FBqc2C990beYs2rQTa_QCu4qvoL9CINDQfyDc2CYRk2hJHhnPRdohBcEpMwsBiQdaTSqOa75Z8JMNilNWJ1n92gcdidsbtYvcY0ZnjUnIOU5kG6dAoAEpCZY_rHMKLLIRU3IjAoAARXApJ0u30rk6QJNhQ_tfhNxRiBieLx34xeGWpWXqIBTS8xnpH3FQ91o0M-zjxsuHYMWwEMNnK1VD50GU6cHDriUn_O1XUNXCN-gFvdqLK_G5fJ7iC0jEjvY2r-VGeeUm0xgskyFoLH0GmiDc-seB0ViP6TStdbe0gREbroKMsgMQDdd10hbYe6jdchrwkMkBzQdzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=qA3lW3XmPz-KMXq-uxzIOCpBnDem-pY3tAHKyWiYY0ZcM1-oHR95a0_YyTzu49ea5Xo_3H29U2UxTwF3rWLP6YYWXt_lgpc8wbvmCKYY1cH-URMJGtQcm7AJBjLT0lQ1Qn3wARQMRso8aebB3gtOjpT_42tcDF7SLG-L2y0LecGmCs4kwphtOb0p4v2zxAZiJ7ku6M_DHGx_NqOVvqydUkj6iQ-F6JdJksgGsHPvv1-GuVeGEXu9NJj3zgRJZXZi7xLAuvXslkvxZu-wkt9L4HyWACeXLh3eruuibGrMTKaWgvr4VCIIC31LZRO6OEGAiBtU27jdWqoHrvez87psgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=qA3lW3XmPz-KMXq-uxzIOCpBnDem-pY3tAHKyWiYY0ZcM1-oHR95a0_YyTzu49ea5Xo_3H29U2UxTwF3rWLP6YYWXt_lgpc8wbvmCKYY1cH-URMJGtQcm7AJBjLT0lQ1Qn3wARQMRso8aebB3gtOjpT_42tcDF7SLG-L2y0LecGmCs4kwphtOb0p4v2zxAZiJ7ku6M_DHGx_NqOVvqydUkj6iQ-F6JdJksgGsHPvv1-GuVeGEXu9NJj3zgRJZXZi7xLAuvXslkvxZu-wkt9L4HyWACeXLh3eruuibGrMTKaWgvr4VCIIC31LZRO6OEGAiBtU27jdWqoHrvez87psgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DEoVSC_9xQY9Y1SrMgFNDZmfawlRpcdWN7KYe3ucQZFi4-G_92B5pzfA4F__93sdJhWmsfZymdjOxhNpEgRujRKwTmh_XbO5F3xiZ0KlYZw3bSYGP8RGJB51-VCntJJdrE6Smg03H5RF0do3hkmm9_d-egLBBxDZQjY5rIJMsQRlJKHtdif_Twsvbi3QxpzULBjNTbUCkKGF9cogPS3MKCXKE16QFLolYtWbU_0xsJv_vy-1yCe8GphYx9fA8t8m--W5Pcev0s51nq7RIo2Q3nyEhU1zmtNygq_Bz15wyHkqY-uPeMPG1PsQVH8KHT091Jkh0IrrFg4ZngUMxtKUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DEoVSC_9xQY9Y1SrMgFNDZmfawlRpcdWN7KYe3ucQZFi4-G_92B5pzfA4F__93sdJhWmsfZymdjOxhNpEgRujRKwTmh_XbO5F3xiZ0KlYZw3bSYGP8RGJB51-VCntJJdrE6Smg03H5RF0do3hkmm9_d-egLBBxDZQjY5rIJMsQRlJKHtdif_Twsvbi3QxpzULBjNTbUCkKGF9cogPS3MKCXKE16QFLolYtWbU_0xsJv_vy-1yCe8GphYx9fA8t8m--W5Pcev0s51nq7RIo2Q3nyEhU1zmtNygq_Bz15wyHkqY-uPeMPG1PsQVH8KHT091Jkh0IrrFg4ZngUMxtKUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=Ihw2z4cUFl9Cep1gG9xFjod8IKCbNW-Jo_fM4ywITMxcWzqTfv3CF8bKvTalq1wLOCvT8aCCAJXmVXFWVoYqHYZBaono9EOdfswcv3MtPYRulNUw7fSSvRdFab8qamsOzueB7Pd50oYoqrorxHp3EKxKQQSa3_EnLmPSITk-n1RGOLhjE286RoSvVo0qGalmjd3WtNRnI8no5PvmJyb5BGL-MM0iL7YqlHqlhMMqkZZxOR8t-kqg5rnWlueL8upW8A07braVvii6ZwT-_mlkv0Vq_XEM5ujdTv2lNw8cXaSrv4u22E7RZCuIlxEwc899bfs1sB018tyPiHTdcaLGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=Ihw2z4cUFl9Cep1gG9xFjod8IKCbNW-Jo_fM4ywITMxcWzqTfv3CF8bKvTalq1wLOCvT8aCCAJXmVXFWVoYqHYZBaono9EOdfswcv3MtPYRulNUw7fSSvRdFab8qamsOzueB7Pd50oYoqrorxHp3EKxKQQSa3_EnLmPSITk-n1RGOLhjE286RoSvVo0qGalmjd3WtNRnI8no5PvmJyb5BGL-MM0iL7YqlHqlhMMqkZZxOR8t-kqg5rnWlueL8upW8A07braVvii6ZwT-_mlkv0Vq_XEM5ujdTv2lNw8cXaSrv4u22E7RZCuIlxEwc899bfs1sB018tyPiHTdcaLGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNkQjB1Apo1CCjzhLMJqGfB8Wl8lCRAn5nCflV1vSv9hULUSaroTvMY_N3CwiIOK02d6ItNvYPesW_HawFO4khtMRb5zy7OXo7w9m9dHomIPy5bdXbYWG2wGr1D5eW9VoCUi5JTOcm-GLFwtok2ZKlK0-97Lc26Kre6LDfN4ZrgsYyTe10xpTCEqqtc9euMz6HcQfndC3yF25DpHCLYt38J07mlf6V60zll7n8rmBJOJPjdtOE2nKqgqH7-2g71pDlzqkFc3AfD5IvFiLtCyu1S6J_vgShIB4RFF___2ZIHDcLecRWN6QjT973g1-7qoQKF4ZgkFUy-CRqWbKKACCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=ZLYcEWZueR1w67BzbkCKjZupTXaifojdkvlHXGWcRFTITQi6EAhLxcUJtc2WhOuqYkjMIu9EF5nSkz2baS9C5qZ9GV_bEa8ZfcuFLueBIuYrsx0xLRAFu5IwMWlox_ugPEf0U08X1ectHBu6SaSfnSbfHBWB3mak54yKdGvDWa3i2wRuLjwoV1-qntaS3VTOHTQyd2Ojzkoq46GqWt2SQgUHmL2UUc_0avBhgGRnoO39R0HwZHKubKcCu3gG8t9WKasVXLBd5wbKRLfZqg7ZXf4UWjpnSTfpY3Gmsnmg2iJMF1mSiiw2x-uveL9gSf1GRurbTz1KCaMFQ-swlYag3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=ZLYcEWZueR1w67BzbkCKjZupTXaifojdkvlHXGWcRFTITQi6EAhLxcUJtc2WhOuqYkjMIu9EF5nSkz2baS9C5qZ9GV_bEa8ZfcuFLueBIuYrsx0xLRAFu5IwMWlox_ugPEf0U08X1ectHBu6SaSfnSbfHBWB3mak54yKdGvDWa3i2wRuLjwoV1-qntaS3VTOHTQyd2Ojzkoq46GqWt2SQgUHmL2UUc_0avBhgGRnoO39R0HwZHKubKcCu3gG8t9WKasVXLBd5wbKRLfZqg7ZXf4UWjpnSTfpY3Gmsnmg2iJMF1mSiiw2x-uveL9gSf1GRurbTz1KCaMFQ-swlYag3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=a1eeG_ibhXtrqCSzt4ZfWj5yRV24HFVhss-im7GPyxSrKV-j-lv2EFlHkO0XGAXSK5reeQIZXCSHJshMst3Jc7s2t9GTDozCgIxzjZ9tTAeK9xieK_7woP6ZNVQ63qn-ewB3Wn7IqMKRnRS8LTlKI1ToLp1kt7prf9zLyZli2J7DdrEdfnnb4d2cRIf7zYXTv1dFjLWVJqCCUScPPvukvIze_9ZOU8IsaObioP4Vj67YQhPRzninlbJZaJzqeCVC9c8XOv1-7G_WEsjBlk-JWTKxSGuJdYB8lbxTuYq8UJK1nDEYoOJ7uP0wvnT4Sk4Ba6JbTVc3ypOjobRGJnsagA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=a1eeG_ibhXtrqCSzt4ZfWj5yRV24HFVhss-im7GPyxSrKV-j-lv2EFlHkO0XGAXSK5reeQIZXCSHJshMst3Jc7s2t9GTDozCgIxzjZ9tTAeK9xieK_7woP6ZNVQ63qn-ewB3Wn7IqMKRnRS8LTlKI1ToLp1kt7prf9zLyZli2J7DdrEdfnnb4d2cRIf7zYXTv1dFjLWVJqCCUScPPvukvIze_9ZOU8IsaObioP4Vj67YQhPRzninlbJZaJzqeCVC9c8XOv1-7G_WEsjBlk-JWTKxSGuJdYB8lbxTuYq8UJK1nDEYoOJ7uP0wvnT4Sk4Ba6JbTVc3ypOjobRGJnsagA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=dgQXnz7fL9PhnpBru-3akjtuyCTEcJWeVTRzHi8TJXCuOYDHUKcJmQI4-KGSkeCnVHNUgcwx_Nsyyy1bRkdLfapUqFam0oUpnSU4CU57_HMAcEj-toXld0wm2Cvgj3W_I5c72s4TRFHmT4OdcXGQj8zUOnS8ZMUtcELdL5jKBfOR1Zq4HT0DUG3fABfkcNrIYUxsMff3yNlRFCPxB_G5_G4trggou2Vhlg4RD2uqv-1UPBYwuaO2w4iZY8nt-FaQpTBGYcZffMxWjAmUBCruFsjcvLbneofDAz2KdWQ1dVZbIj2X4Exg0L4dNlR-6WA9znzxQcQVRdEG2_4dmMuJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=dgQXnz7fL9PhnpBru-3akjtuyCTEcJWeVTRzHi8TJXCuOYDHUKcJmQI4-KGSkeCnVHNUgcwx_Nsyyy1bRkdLfapUqFam0oUpnSU4CU57_HMAcEj-toXld0wm2Cvgj3W_I5c72s4TRFHmT4OdcXGQj8zUOnS8ZMUtcELdL5jKBfOR1Zq4HT0DUG3fABfkcNrIYUxsMff3yNlRFCPxB_G5_G4trggou2Vhlg4RD2uqv-1UPBYwuaO2w4iZY8nt-FaQpTBGYcZffMxWjAmUBCruFsjcvLbneofDAz2KdWQ1dVZbIj2X4Exg0L4dNlR-6WA9znzxQcQVRdEG2_4dmMuJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=tt60l7ZfogGgNOii88ITGuNio7wzXq0QkdyL9CXw2RB5zZAbcX0czwa1LTSA6KF5H4o7IgikP7ms6yIrklRQmhLIeIoJKsZaA21UrLVyXebhgaCtY1XDEPWY90_0Z5bc7cVzZQDFCcj4Jofa-z_8z_D1ujhl2hDSsDJhvpjir8rrk82V0uleN4c6joB8RAdpZVD4YGzhQxYDzmCw44JjVQd0zPk_-DiDQCjPodqGQ7UbCyD_JvaKPWXEPbkEp4KADwfNg23yAZqd9BOjGvPzj8YLL3Wj2gmQkHOnb15xWsX5a2KFrl8qPh247pEWzJWm_KcYxSyEB-cx7dUq1UwljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=tt60l7ZfogGgNOii88ITGuNio7wzXq0QkdyL9CXw2RB5zZAbcX0czwa1LTSA6KF5H4o7IgikP7ms6yIrklRQmhLIeIoJKsZaA21UrLVyXebhgaCtY1XDEPWY90_0Z5bc7cVzZQDFCcj4Jofa-z_8z_D1ujhl2hDSsDJhvpjir8rrk82V0uleN4c6joB8RAdpZVD4YGzhQxYDzmCw44JjVQd0zPk_-DiDQCjPodqGQ7UbCyD_JvaKPWXEPbkEp4KADwfNg23yAZqd9BOjGvPzj8YLL3Wj2gmQkHOnb15xWsX5a2KFrl8qPh247pEWzJWm_KcYxSyEB-cx7dUq1UwljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_RYUHvI5DKHkIH87c_2e8Jq4W3txJXI2N0PXHraQTj2NZ1IHHnVnIktEgl8zWAisbbq4CVBVF7ZwHVNtUzunoC0_1pXUtUVLX8hqBNNB2EEZQIRtyfozyDCYbPMclicQX-vDK_xO2r2hGVaRkCjJCjnECmzFdFCjaR7TAuEOmBnp6C-mPNymsXRiPlVns8OQJBd7_q2iqO_hAoQfBlh4lwfBIDUlQMwZvfHsLviLKIbGwlb7HI13J9EJlmFtNVmxlrD7FkVPJUnihDxRW2Gh49B1Br_-IxY9zsB8rGUdoteSzXTbpQ4vV9qi4pXH4uGsS3Q9jjsAK0hHWkoyc1JOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8-1v-0HQbLRE1VXoQPVxLDYWrkYccnGdoIZyjj5YI5L_6lDKMEk4XIoUb8HUxjpnJpKFtTvegWfhn1forksVouADFB4oWIk_kMyFMnui7t_Fcty713pGVuTAC8lX57vZfNcomAnvGVgpmn4qotDQr-sPFV7jPE9EQwA5JogOYZGNHgxevtEY0G0BueKPgafQ7Bc3HsV0KkbhnF2tWyfXKd-zJhipoh-zKqhrA3bajiFelHu4KHIwwmaEJ90QhkSlKt2YJhetFpJ8poW3-q_GbKDYBbKDlBvLmCA7sTFZ77QTyzjgNpjOMjUIoDNHXAdJGIu7M7w3JLGXBT7ChY8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbK_RMxTZPYMbwMTRpW4K9knvmkHg6IJ_Hqyb7_ezZDOhfwu32Ul5dkoYw4FYOJnNKOm1RLHnUq7mMjm3MdHEqpwBmxTKXwOPx1UFH18henFWX1hS3ifxqwzvzXajGXBCsRWC_JkxNS7RXQAONQ_t9_eNsECtEcklc8O0306m3fM4YG9aglWU4Hpkfp59sz-UHG8e7GNZMLiPXjGCTIchQkUkr1kMLC2K2iNiWbeeFh5_osTJVmSlBx0P_d8C4I1Yeb2eb2orKU_dRKP9YM2XB-5gE4y9n0M0TyBxycfft-qpyu4EvRaKFjeSWczcYRKpqwxmwj6v5IPc72E57dqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IUA0R1tLyL-oStnNQo3J1lQiZh8fg0Hgy-VoAFRYKYlr5Mk9hwJpEyZgILp5BJCroIgfBj4cV9tKYkNFl6czHDmbMwGC1xA7U8h43lGEOG1u17DOd5MO6w8_IHgcG7SkWNpYqfhiFJ1Fv7GlYr5HCZNPNS6NnjXRSEqHh1kLa5zc6LlMRHSVFcDThuuofqIGjR4PaafwUyOqQZJ6X5XuBTx7SBTIZbDAWyHsmK7QVH8EKCwOW6lwT1I2fwklDScMW5ZP98FCIpvXzS8xVAKktsgpAEgUBSyN92bMNHltmmXENwBG4w4uGR2ZrA2bhQtO7WY2aCV6XEIoHnHkL4rYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bakyhqY03bxSpeT6xkc1gJAEzguzKXU_bc1eh_adXFAf-_4HfGcRFsvkBd8jXA1A0jRwNYYwjmel733_-Zg8l9X-Ye43AnD8TDaOVR1a6RKPt4T0856IeNzqEzF6orYHcHj0NGiw_YpLqZESqqmWdMAk_nS72kpE-aCxIELd9k2mIV5S7ZBSemBpipWjz73aPwcjOv6Lnkl58IX6zYSAX8z18B2lg9HzZ2BpaQQJttDDO9cYOiRnalV0GacpGIQMEGpJu575eJBg5MXCyIbw60t4wPzTmFm6_KZ5m77MOiJK4bsB1OnU8nhCjT5oHlabTziTjqZJbXtXrbFNPMWbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlFpjtngORGno-lAVkiQOz7gL1Y8KhicuMZVF0MDMpwfmV2DGvCyUfvIuJ5afZahv2wNbeg7GDCiuNYZ_6Gx-_3NULX8rvps0dggO9EvDodcbMtUO0ej_e5-asd_1bOLIE6eYGW1Ay87BhoiCwpkKnBB_8UEIByrbw2kYwyo3a3EkN9evdyCV9YDxSEEuhE14gkHIkpCgS1G5NLE1t9Gd6CRnmfMxUWs2ywPwPMFXgbn3ifqUhIMX8giJ4NduJx8winhK78Oapzls51DNxcxFiStctrMukn_yP89QPZzWxoZ-dRMa7AH_rNzU14cM5UMp4X6PtWHaM7gytwpcFYitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtQHKTWldbeGyneznoRoONX18TIRKAFyAjsqvhVnsLYcWhEhIkfBBeQ9d5CoYA2AkOac5eUazaHpRYP0ARI9vzAs73xAO04beFcf-SRm6_yd2WLhkPpyN9cSVSz1nj5ulBb04dqi3Y-goIQHYVkUvoHh5ce301-8Z7AlXCMtlMgZXdxUqt5_mKmQbbPWSbY_lTeObJr48_z4Fu1akmZyN1DlqoOwpNmeLX6QkpOsC2PpTjkvmTGML7RQR4cTr1Pn0ZxTKlFMBcdYvyUwNmm4SCoJvzrreL2uKsGj1fp_YXEpfvrojFL9wfs30XD6F-Um0Q0q3CFTpl-C4leBJgKvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni8qEaNuJKR4CEq7uX4EN6aCgntgIJBsXo664si8WiOjtzG8somW2V6XOClBgTILv6r56Ww1ccMpOXPBHtYv5sPGAv0gy6GMnPA39VV_pNKlw-r9cR0jfj1tffaolVp7dboq2QUUDuXC_f0x0GDpiZk9KgjF_pWK_HbsNHbXAtUHTgAw-k39ruOe-bxsNruvP1CKvH5P-EAr5WZpP2UN9SMa2I9E6qDqhi-3ZmQCc9yjquvj1x966zo5hhjUezfBSGGfp5dPdfMMIlwIJY2VL4WKBbjmVikUJGBkGKDEsGdtx0n-d9zo8JhOnnVGd5sUUrDHFxJvppoOoUeD8y9awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEMfrw3dv6Mc_UfTRuPNSZADaFuA6EbFKeGx8WT9bnYjA0lIsRYfkP9_KkRq8Iujg2WbjJ0l1pZTMRUnsoPkR-h6FjTQm3iDuyBH2RKpR3--RIvPtgYLjiyD-Yk89_JaTU2rGAAj-mUMOzfnZmkSpEifA23ayNUg_lYj2ir-L-WMCGmcQ-ZvoNSA1eDRRoHKVbbwjkhafq7MmkGpKB1peBxfS5UaTL-dTgFxPGXaaa40T-LTOWfX3AV5aKwXurtGFbaN5eRzzMElcGtBHhTpk8btzGZdU5oaPBG49L5qXgXuoHk5ueQs_B_0xhqlAHPNXF9-GfI8gL1qhNd4wWolZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=vqXnZ5dkaCqgm4rsMMjIQsZqffI5L2VLVDGKclTztRTNH9-A5-3M9Kmqjb_kAznqIJ8T9saKjaOqag1yylpZ3qQ1l2YYLcjxWWX2RzfsrRmiXN8AETCk2EORvNZy-YOSZKANT7xU2L9s1oe0E-FQfKCCGF2qZNc3nXOgm06zkkfVPdKojt-qReI23hIF01Db8022wRMeNHCAktjvegkf8y7Fw-_wu-8cLYgRm6irprOeFA67w0M7EVjrIKOPsS8dmwo5jjZz08dBXMHyGs2JLpSgIWja9lQM0mkvc1QXq_Ca9935OrWVgtuCS_Mp30_zvTWLS5B6GPldxCIJllikzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=vqXnZ5dkaCqgm4rsMMjIQsZqffI5L2VLVDGKclTztRTNH9-A5-3M9Kmqjb_kAznqIJ8T9saKjaOqag1yylpZ3qQ1l2YYLcjxWWX2RzfsrRmiXN8AETCk2EORvNZy-YOSZKANT7xU2L9s1oe0E-FQfKCCGF2qZNc3nXOgm06zkkfVPdKojt-qReI23hIF01Db8022wRMeNHCAktjvegkf8y7Fw-_wu-8cLYgRm6irprOeFA67w0M7EVjrIKOPsS8dmwo5jjZz08dBXMHyGs2JLpSgIWja9lQM0mkvc1QXq_Ca9935OrWVgtuCS_Mp30_zvTWLS5B6GPldxCIJllikzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
