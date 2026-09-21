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
<img src="https://cdn4.telesco.pe/file/TXjFBB28p284z6vBwR0Ilz-KNyFcpfDSaPszQK124QlyEALApjLF0iWpR_KiTr7Tpnar2JZUAytd4Kih4fd_r-Ynj-0J3lJRhsv0m3HaulvP0td7qZEGtJblarRR7NzP--QhtckYI6aC3fwAPShB-k4xGrAk6WjG0qCCMXWJtcX17EBkLJSYnwntqx_1sVcn4lv1QkBEtMaGAv3d0q3gJ4J4sXqm36bNlQQzi1JH78zOXcTAZ5yuM2CDHAlEM3HZ9kSry2z2-FGC20q8QPwN2aDe9-GIKAW5q6Bbj7ZcZ-ze_2W4SAurtQq2bqcFTCYyP8Us5TskzNiUCfsH2OKSHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-463492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیء ناشناخته نورانی دوباره بالای تهران دیده شد
🔹
یک شیء نورانی ناشناس شامگاه شب گذشته در آسمان تهران دیده شد و انتشار تصاویر آن در شبکه‌های اجتماعی، گمانه‌زنی‌هایی درباره ماهیت این شیء به راه انداخت.
🔹
پیگیری فارس از سازمان هواپیمایی کشوری درباره این مشاهده نشان می‌دهد که تاکنون پرواز مشخصی که بتوان آن را به این شیء نسبت داد، در رادارها مشاهده نشده و این سازمان دربارۀ ماهیت شیء نیز اظهارنظر مشخصی ندارد.
🖼
اما شاید برایتان جالب باشد که بدانید ۵۰ سال قبل هم اتفاق مشابهی در تهران رخ داده است
.
🔗
ماجرا را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/farsna/463492" target="_blank">📅 20:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCQXRihJ6SJZ9g7T-Qfhv-uvo-VH4ngZqy_e1yOTbTH-zTgUwUn_WsyDbNLaw7bj8XKMWl2INbp_sSOc0hqwIY5XggGyw2vv8XhMLdIeBSGReZBHJY5Os5_NALt4Znwpy7JUAJslf9Yj5Jwtpb1m4F4_OPPCm5P5GqvqXOGo1M1-2V23JfDlBotPu5J6pwjyPeT7UrPPtT_JulaTi4RDYFtDSFYC9ff2mlh_isRqHdKI5_Ur40IB5EM0kiK2GKvFkxbPEdb4tcQOPHdZCUGp8L_GIY3UT9N5slbieLZyDX7d4fENEB6yk2WGwT7QmMhTQ0JgBSeP_a1LC3EEC6pPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: از هیچ کشوری باج‌خواهی نمی‌کنیم
🔹
سخنگوی کاخ کرملین: روسیه هیچ تهدیدی برای فرانسه یا دیگر کشورهای اروپایی محسوب نمی‌شود و مسکو قصد تهدید یا باج‌خواهی از هیچ کشوری را ندارد.
🔹
پسکوف گفت: پوتین بارها تأکید کرده که روسیه، فرانسه یا هیچ کشور دیگری در اروپا را تهدید نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/farsna/463491" target="_blank">📅 20:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7616ee5118.mp4?token=BrZEMzDe74W9Rdd1TmnyBLGTEzzQeaUtTkV_XFZZeN--6kls_gquLwZPM7cu-8L0W_F1QcdVeGKkifcOjI4OxLcQbIlsU5En0ntSbw8CenCYWJGwi0gFYQ8dPupTgM9cJ1NYYnOX9tToQfUQi46X3bxld1tj4nBdsoT44weNH4Vry16xMUMYdun6m8sQLKw9qroib4qVfexjO4gJQ1mBlR2eBwYcGG7sbqCbuPqe884AbyG2G-z7uVPNqKJiHavL8rEBljvqVgDBXBsif2VoZC4Fw73QI9DTZNuPJhF7_WoDFjAabvre8gL2KWS5uxbY3gTvokIteaYrf1bD8agcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7616ee5118.mp4?token=BrZEMzDe74W9Rdd1TmnyBLGTEzzQeaUtTkV_XFZZeN--6kls_gquLwZPM7cu-8L0W_F1QcdVeGKkifcOjI4OxLcQbIlsU5En0ntSbw8CenCYWJGwi0gFYQ8dPupTgM9cJ1NYYnOX9tToQfUQi46X3bxld1tj4nBdsoT44weNH4Vry16xMUMYdun6m8sQLKw9qroib4qVfexjO4gJQ1mBlR2eBwYcGG7sbqCbuPqe884AbyG2G-z7uVPNqKJiHavL8rEBljvqVgDBXBsif2VoZC4Fw73QI9DTZNuPJhF7_WoDFjAabvre8gL2KWS5uxbY3gTvokIteaYrf1bD8agcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رواق کشوردوست به روایت قاب‌های تازه
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/463490" target="_blank">📅 20:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6215379.mp4?token=nfEgdSx3cEM45OWETt3StMUoGASzOMi6U0BGefelSjOwFwuQofFycwilIPDYry-6bggXwT0ZwoYJACSJOJHL6K8esqRsd7t6Kt-vN1aAWyon5qF7tWPluAWe1nUI6QmhAmyxP2F6iTpOs_TD7PA7BnRejtuX_d7njqqxEgBoMMR_0E3LpNRItB7tVvAnuVzkXL2q7bFed9podri7n36DjaDSAOHewA9Vzjtn3AKs4gVmP71M5cfWD0gxvvK_u3CAHThS9Xlm9f1dcLGWusGE7ZkNC5KMQrk5zSKem4EbocGdatr5KWFsHKbKpXazBJ95TJqoAZ6WVWm0yhJRsoYhKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6215379.mp4?token=nfEgdSx3cEM45OWETt3StMUoGASzOMi6U0BGefelSjOwFwuQofFycwilIPDYry-6bggXwT0ZwoYJACSJOJHL6K8esqRsd7t6Kt-vN1aAWyon5qF7tWPluAWe1nUI6QmhAmyxP2F6iTpOs_TD7PA7BnRejtuX_d7njqqxEgBoMMR_0E3LpNRItB7tVvAnuVzkXL2q7bFed9podri7n36DjaDSAOHewA9Vzjtn3AKs4gVmP71M5cfWD0gxvvK_u3CAHThS9Xlm9f1dcLGWusGE7ZkNC5KMQrk5zSKem4EbocGdatr5KWFsHKbKpXazBJ95TJqoAZ6WVWm0yhJRsoYhKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالای غیرضروری جای کالای اساسی را در واردات گرفت
@Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/463489" target="_blank">📅 20:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO8Klw0h2jxxlX8MXxxt5jt7vZptWjExuNB87v0fkrd1ldCrj9evW3PhyDccyFWFXKEGw6OaJKjZ0CKtzizYHbl33MWo66h5P_2sV01C_hYMoQ9JtjvwKiWQzsh7E0BSKt9b-0LZr285ypW-KryhN3948UoATd4-aa6dnQOnFq26F_O9mrPWYDGMkO5UGzUZsOQ8SaBRtfrR0UjfwshfwniNFKOeFHBUeFAXx82CaDH2grLoqN6kAY_s3Xiz7D-bHKj9LKtVsJ39YOMsb9WLgkUXv6Nwrk3V8Gh-54SWmaRVXVKNA3KQ0ttak2QgiQe7nLC_PEFXafPIeCvbK-LD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEooeMR24eqUOfrzwMri9QNDekMo_gncNFGnET7EvgdG4EXiLiwTTe9nVkP6wtuJ72aqJmAZgcPZ9aJc7kfNQJrmV9nfKaDZZs7hQf2xJ2uNAcweQV42_kpg7-mlBCgupwxN57InDpwPT_yTT5hJiGoCaMW6gOavYZliRO0YBk9ugnvhqZNW99xxG2R6aIpklM3Xn8lYRgP0O4m7A6054vKXCB7-RXpXJMg3BNx3syrNquF1waFJqNrc8i6gngQ4unBblNWnJ_ZNNEoHc3weg9WVaQpkMW_EyC0VFgFl05WSyZ0q5kYH-lXCImPO9YkK5yM9uwCi5PRfPf3Vw2mI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8v70L2S_lx1icxa0VCr7xewKxSG_mSbu60ZlzbHJwdMhFQ84RDUCBPWsk1fZq_0EWv1LTtPIQAI19AaVR9m0P-O8ooEKlIBN7mwuMaAFURD3IPfmVplaOzy2Hp1rYadsxvGiAafQV6cQlzQHmr-ny9oUufUsX7_zc5fqwaPlZqnfyk7lHbKC1NB5F6VrE6BYJhtqH3MZF6pDVxP5m3-_Uy32adrEoORYOGYEo67CHzyeNxq7IqeLHmnoDy3Lrqvh4xVkyptbE4XWzP-aEiggRrJSk7P_wI5JCy6RQV6aXMV3xWOZg4RC-1dTEG5NCCQNccyZj92it2YPPB-c14wPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNSrItI2ElqR9ouB8z2seD1_ps04j8FzM9QsSQ9XyIkEVCzaPBZt1Ebtx2yI2EHDdcijEkNNtxosjOyvG8iFNm8YG-nfC94xHKv6maHSF9Xe5FPdrO1uehEWYSO2w0MVtGeC1fD6kWOWDslQFcUoAIZ1kAje6c8eC2rb-I5txIF6ViBFQm-ZL7DRBuZUZGIBziudFaH5yvuLSTEv2TjQsjp-O9aAcEo6Enp9HfEZH1FVbb3CUuD1CUjAzVT0UHtypoaTYlDthXAmOYwoG0npjVcZ_4dRkJlrLYjM7xhQ4zKn5sPsAc0_gwcVy_LmCld-0oX0Bml3xnsGKZFJyd86xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYZFluRJsZK-M8-z2CTaKYbMP2tibr_8TaFnKQbI4BIxOLQcNqCJ_f5WdVbY3vQNnXhiIOTcsczGhP1TD6-7H3KTNRzrooFxrhY53QKXu23iWgWhBTL6nhABcWgTlGYd5KYpIbCAkYEH7-i_nC6stsbENrsdRsj8kXJ_1XcG2IgkbLlgww3bSAcov7UqZWerp1OGez7iOjhGgDuyR8lFkBpF4lk49p5QMjGODZ9i-00Kw2lxewE5Mgp5lV-01MVOepHfbSMZYg-n64uIBHt1DcYkJk6InFnGCivvzPhYCIW1yKP8pjVzrzdg5V6gpa6dGvprO5dR9GKfmEiLY-XuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYzhqLAUmCky3KSrEJzf6kLUhpQ8QLJLG80msPvPqivK3H3QgAg6Uw3K0tuqrKErq0YP66J_IXVI4mY8zyuUtdQrI5WG0lvGlCulF7sNMy3fszRFYrlAIBRLkO1YjBOvM1zr7TCmH_Kgi_JP8l0hxtuZa6bAv9u0YCdBkHeUPhUx9ssMgY50b1vdG330qzQ69WT7DP-JU0UHTVfEvqDhRB_C4pCkn_QkFj42VoOStl9spT1zGuYknWk_NSAWVVWIPiwxvppe3Ahw1Z18bqvSGrXINWbN8K25AqIGcttc6LzTmJ5ej9lDK6a7WXW-4ayjFuGPEgCkQQpHbnJKXiKPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS0eGNDX9CCrS22MZioWH0Ct9MYnwvEIdduvFY72hp1A5izYMv20DD9e2bBZuJwVyjCl6dPTrDxRkYm_lCWJEUzvUNTXcuOZPoHU3bi22jcaHHSQl5D9oBqY4wqKwmqpfMmHq-5Az1ku_e-lRhv2SuvLwX7L3hnlX-k4JYRNjGD2mWdKzhn2WLyt0PYWYCQSrGUDUlu5X4vBlXQwq2i0lKWyMClkH9nj_5ICmOtIPn9HnRUVKW5vIkzb04dSMUGI9xaRgFOOb3Us7KD1IcUgn_KTMCGk09M_lBy0wgCOcm60tObPo48z8uj7EH_O0dwpm5Ic-wixdKHTkcFK69rXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهتزاز پرچم عزا بر فراز گنبد حضرت معصومه(س)
◾️
در شب وفات حضرت فاطمه معصومه(س) پرچم گنبد حرم بانوی کرامت به رنگ مشکی درآمد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/463482" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHFZJT5o0OBA10N2YboJnLYlZMRYiqEGX4zK74Cdr5ckhBn9MZ_iXh462nYtNXuZ0ywOLnR7_5NboYkoAyULsxlQ8AROF_-NPl1Dh4zSJ8k3sA6L-KkuNfp7zoMSbqnWpP6JZF0eXhqpZgqPJeWMOjZo_GFA_fTMIeZmOXwL9NAuR1VGiwr9h8FPXtdAcIpEo5IxRbNGNdZXmyUmPkHuiZWXPnepN6_9DZTAVcJ_nFg_7s-GmeZ24_VvMW-EJhdsehSpcr2gBGMF5t_VDhkF802zNd-A1sfwDWNLslX2TEnr2tSE3-5qlgfnTbN1KtOJGCe-4b5-i6arTLccEueIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
در آیین اهدای لوح به سکوی تامین مالی جمعی بانک شهر تاکید شد
✅
«شهرکراد»؛ راهکاری نوین برای تامین مالی بنگاه‌های کوچک
🔹
مدیرعامل کارگزاری بانک شهر از دریافت مجوز رسمی فعالیت سکوی تامین مالی جمعی «شهرکراد» از فرابورس ایران خبر داد و اعلام کرد که این سکو از سه ماه پیش فعالیت خود را با ظرفیت کامل آغاز کرده است.
🔴
به گزارش روابط عمومی بانک شهر، در آیین اهدای لوح به سکوی تامین مالی جمعی «شهرکراد» که با حضور مدیرعامل فرابورس ایران، علی محمد خانکی مدیر امور مالی و خزانه داری بانک شهر و ... برگزار شد، محمد گودرزی مدیرعامل کارگزاری بانک شهر با اشاره به چالش‌های فعلی اقتصاد کشور، گفت: کمبود سرمایه در گردش یکی از موانع اصلی پیش روی شرکت‌های کوچک و بنگاه‌های تولیدی است که این مسئله مشکلات جدی برای این واحدها ایجاد کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/463481" target="_blank">📅 20:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463480">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e890df7bd2.mp4?token=likzL8kbyVVKTEBrNxOtsIX11_vsFqtvmkVNHvBCkw_oAiv0BRtm1RCb9NJnQ-8RwzWlI0LZn424xFR146r59REJBxol2RgJTxUG9PEVdnhArQNID6qMJISRGQWDLXCaTRcqpysDZPMkLWcIl32BRpVXD18XBOyV8WFMpyVQxlaksnKULjcKwnMcx0EaGmpr7qY6zjmAKTYej5gsVuKOfwQndaND25RgEZ3WoNt9rP6zqCuxx_p743S9N7smyRv_yFC9F-hJ3haKiZ6_svFIO1dS47MH3kXrhHIWdTeeYg5-DeUkQ_HIU2pX0mo7rDyI-MAs3OUUeJbOC8MXb-HRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e890df7bd2.mp4?token=likzL8kbyVVKTEBrNxOtsIX11_vsFqtvmkVNHvBCkw_oAiv0BRtm1RCb9NJnQ-8RwzWlI0LZn424xFR146r59REJBxol2RgJTxUG9PEVdnhArQNID6qMJISRGQWDLXCaTRcqpysDZPMkLWcIl32BRpVXD18XBOyV8WFMpyVQxlaksnKULjcKwnMcx0EaGmpr7qY6zjmAKTYej5gsVuKOfwQndaND25RgEZ3WoNt9rP6zqCuxx_p743S9N7smyRv_yFC9F-hJ3haKiZ6_svFIO1dS47MH3kXrhHIWdTeeYg5-DeUkQ_HIU2pX0mo7rDyI-MAs3OUUeJbOC8MXb-HRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
اجتماع بزرگ «امام زمانی‌ها»
🔺
همزمان با فرارسیدن میلاد باسعادت حضرت امام حسن عسکری(ع)، اجتماع بزرگ «امام زمانی‌ها» شامگاه یکشنبه ۲۹ شهریور ماه ۱۴۰۵ با حضور اقشار مختلف مردم، خانواده‌ها، عاشقان و منتظران حضرت ولی‌عصر(عج) در میدان راه‌آهن شهردارى منطقه ١١ برگزار شد.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/463480" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/463479" target="_blank">📅 20:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/943ee487e7.mp4?token=Cn61hj5tSISEHsSKSOiI0wkXZpqMVob662gMjgIe3ip2FEalNdNrQEpJPQC14ao1mSXMN-jBgl1ML4NxSiQCbRdrFNYYn1ZsGtofwIHYELq8piX7UG0G4gjMtOIEljd83NLjsl-0HiYVlzj1BNpgVlZbtKrbrmMhk5DyLorgg0VOoLUu3RmDh_lcIYCOrifO4-91onxHlVMvs8NRt-F6L-Dxtbfrh_GTq3atxnIv1Z-3TgSlZ4IW7OwmrjbBu7lsLyko0cdPh0wDFW5Bdumnds-n0_ZKsrDTgoY0LUrM2YdoIVy8V7sHVCKfVlohfoc5_gqK5QmPBYnE7Ezm-BFqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/943ee487e7.mp4?token=Cn61hj5tSISEHsSKSOiI0wkXZpqMVob662gMjgIe3ip2FEalNdNrQEpJPQC14ao1mSXMN-jBgl1ML4NxSiQCbRdrFNYYn1ZsGtofwIHYELq8piX7UG0G4gjMtOIEljd83NLjsl-0HiYVlzj1BNpgVlZbtKrbrmMhk5DyLorgg0VOoLUu3RmDh_lcIYCOrifO4-91onxHlVMvs8NRt-F6L-Dxtbfrh_GTq3atxnIv1Z-3TgSlZ4IW7OwmrjbBu7lsLyko0cdPh0wDFW5Bdumnds-n0_ZKsrDTgoY0LUrM2YdoIVy8V7sHVCKfVlohfoc5_gqK5QmPBYnE7Ezm-BFqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوفه‌ها پیش از پاییز به مدرسه رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/463478" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc03265dc.mp4?token=oTF14OwSlnsGwkv1ImWfQlIHctu4zHdYDbY5l0ztRZISjaL813Jh0gdN6wxuu0fxWG8Xe2PanP9VvXO_7EV06DONUR8y7-WCpee6usTndfHDepdkI1jqsTcMLC3p07kSHxblA0uTokkg9LvzdYYzSrkr48GGmZ2PMyfISnBwwLgdbaUmaaDN9xMj-lFlbOwUpHb8s9i8Y6qAQ5RylKCLPWVmdbvcBS_yw92jpWPvmKEeU_s_ouin0VJL5w-NIzJmmjXruFpWz8nd5KmxcrxFyl_X2ZRdBPFO8pId2_FtXeXmsLqT6be4R8teSJYIhrp3ylOSBJ1JhgfqRWxwp7sPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc03265dc.mp4?token=oTF14OwSlnsGwkv1ImWfQlIHctu4zHdYDbY5l0ztRZISjaL813Jh0gdN6wxuu0fxWG8Xe2PanP9VvXO_7EV06DONUR8y7-WCpee6usTndfHDepdkI1jqsTcMLC3p07kSHxblA0uTokkg9LvzdYYzSrkr48GGmZ2PMyfISnBwwLgdbaUmaaDN9xMj-lFlbOwUpHb8s9i8Y6qAQ5RylKCLPWVmdbvcBS_yw92jpWPvmKEeU_s_ouin0VJL5w-NIzJmmjXruFpWz8nd5KmxcrxFyl_X2ZRdBPFO8pId2_FtXeXmsLqT6be4R8teSJYIhrp3ylOSBJ1JhgfqRWxwp7sPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار و فرناز درپی مقصرنمایی ایران
🔹
یاشار سلطانی در میانه کلیپ افشاگرانه‌اش درباره تراستی‌ها، بدون اشاره به نقض‌های پیشین آمریکا، جریان سیاسی پایداری را عامل برهم‌خوردن تفاهم معرفی می‌کند.
🔹
این همان روایتی است که پیش‌تر نیز در گزارش فرناز فصیحی در نیویورک‌تایمز…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/463476" target="_blank">📅 20:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxsACEu_yPf86ust_0_AhuauCic_288NJFfVudeMEvJTJTyV1UJpwk5Ka6ykI-nCYL9Ft8zDDHIbvmdQmop_5FRNRBplXjlwdbJsK5YOXR8kxo2vOb8ZtRMMIxImrcywaMz74wnaQuByyX1IQUMwhVl-H_FSkDN82Z-7Vf9HvgPRXnzZmNFWxj8PYTjanhMYu1UQvcUVoneXN0BsKDUJXIW-nxq01NVLuZ20EmdeWthSVvm4NMZB0egh_0L1yV95FDKf1DYHpg4UkR6eyX6f8RjHXhHJpqcwL8bZ0wszTljs-ISVs_SrbKP2jzMpF3Z3qLwcP3lQUqCtF4yy6Yi5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf8qIKhGBfC3rS9A7J6EwtAKDuOpenF1KD77_eYWqwZ5rpFeMmthUe2iIdMgzizzl8mkCL9_JzGc3zV98Ca0FFUN4QhJvohT_a_JDngJ1FJ87fjaxP1H6FScFPzRQ4OMX9s-NYczRnUj3UNp5KCbmYbSR31e9AljI2j_9ka8i76Zb0lgZdmQBBl1j7VjMvehoK8_MilfZf5afE9psdEkNNnS7FEGiaEXwIE8WyvDCCBqwc8Nn91ekLvpJN33x6eKL4VgawiH5mv2x6jfvV61DH7MGSTUBUXFOLRlVGxrMtrgHuff--77p4VQDudNxn-sQLGSmcYnv6iYSW71N3P3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmLY1g274TKsZOKm6TzdTdMtOZUnaiD3NTjfgQ0RYEuzz1uU3hUt6S4OzSIOOIwQsDm3Mvavl4KWPOhvUe3ek7lwBd3_FarBOxt3-VrxooMeIfwKCifAjzpAWrahhPc-XIL39VqEeuBUZ9t2pJgMxfYKeejrIZK9NvMRQxRR1gg1JI7u1KqW2WIwZJEUYbB6y3z53TeRx647XMz7-HW4c9hipIkI7f_Eg5Stdrvv9UUoOB7QKI9kYujyg7hZbNgboHvsf3zg0SLCmmLUdgLEDddQoxBMxpV8Q66E2qWbz1ha6HshsbIwzoyLSuyBEgZpcuzE_MoltoFH9VhqtpMcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQ2e62uE0g9-cYZJTjgHIFJh5AfBIPzMQ4J3x0ceyLMvWQQpN-whDxZgg7ymaYmAYyvxG_mJcrGsxbDBsKn7vb-AmHFQb6nxbna4qyPu2MBtkmRA3PO0I2NGcxi8EZmexqNZl1PNYsaeOZ5xf_Te38CSV2KdT5PvhnKkaMx--t-RhJThjv9pzy5ZVpxFK2mXYPaFkbnBizX8EYQQps9GOATKWljjxcTB3J6nZ-M_wxOWVjslnUN_-e6Yu4Y6kauZG4-dvqVg9GZyBqiqaDK72-GvzSMAJNSwVjcPlcWFStJTxKJG2yHGfZAAylwK4Bb3Q8V-jZoM3EpP7BeRsVVXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuxk48Dv59Ne3MAI-8je82A1F8p0eNDc6BcG4TricCal2H4w-uO05CiCZ7EgYPbQlDJc9i3lOLld7VcE9CJxA_fbcNq2QVXNkJ9EinDvR8Ahh71P3YyAm_EoMECeHWiGeAvURmQNh5PDUCML6McVGeSg73uw_2wbngI-ymrGOqEDOH-S5ySimCMJD3l_GGv5LupZbbY-z0y2wiI4oCXbCTLAf4U8WmxXCt8_uDa5922eoGvuc3ayW4jrKQY9CzRktWyfrBkH-97vEFl1DAejCFRJzMCNWGLZIfHBhBbCGL0v9elNVDiUnUjayBxsTVSO-nHgBKQWpckSoAQG8S5_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uY3xz965nuZxWw-cxNjE_12MSnSnz3t2Nb-zscoL0VcEvOfDcSxidNL09UrZM4iIg9kWr0e8TJHRXjijuhPoe5jwiruefCFjQxbk2NiNupshhc-AKLBC4FM3ZDQefqRN8I0uF3kG5C8G03ekoS4k6U2XwpQBFAEm-sN5sKKLVv-1KbwzmvYqgTJtZaocuRYGzDCgMp5U2lWhuXSpVhQHi0_JGZkyMxfbQXh4C5eM7q-c24genqDIfH7xtYvtxbypWZMtGD_GaOgu77QmDilG_k43rOGWwMN0pssEhcgMTkDM20B1XZYQ_OPpIDh_qekEtFj0aHF8NGvN8QahW8UxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMKAZ28IS2Ylskjh5KhaLF2WCJTy_KRpa73lo7z3fapiOMQTRBceRbKEsm2Xbwq7ogCgcLUV03cS-rgOjCsVhLnT1S0_US7HlXOaqunySwRUwEcbmJqybCH0IUxAAB3Sc_R2cqmCwPOauflaNZe1s7PErBZp6epU9_-aJwmqpVfc2snGElLP4h3SiAdk9IsqA_Jd4DLJXqHEllwGJvc6JBLvGpLo61Hk74WWn7ld8_jjSihHAaR1n0TrTHjKPZbTHm9wfxUw1QPf34ktP11-nh0_um1yylXAEVALX8AsUyhF_w4nm6sej_gGcKUwu8uxMOi9k-sctXIquwPln2Hk7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور نیکزاد، نایب‌رئیس مجلس در خبرگزاری فارس
عکس
:
میثم نهاوندی
@farsimages</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/463469" target="_blank">📅 20:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6MzscNv0b06SCPL3P1xJ9vF15Z48OjR0qyFOC4HI35Ws2geido5a3LNJhTE0OB2udUfO0cI4RbIoAYiFWuvRycb-5loMAlCHtrLJ9LXXuP9R2UsYYVGW0N9l8-dObLnXTWkObSmmMcH7J6GLxvT7F2IPKtXvMychKGZHJzhPVWLzRCerkXWU2Gsx9M1ffGdIfk-kfGqx2yIXpD6LdzVfU3vyUEZ410e2jo8JhhwxlBzTbAVv7zhZTqolmWyULjSURyALYMKz2vPGZJpuV3G8ySKfAASKLbsM0zCFDqN70oM3nGhAz-BABe3U7Q8M92_21o-PMBDFfVxK5Ks2rtQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/463468" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f717cb916.mp4?token=jAE8V8Au-LL7pn9m_PHDYPVye-1FkJ6nCGwqgORiOv6n6cllvuSCMVIqI8WKCIkuXAFjpCDZN_2MBvprHp78LN57npv1Mc-er7SL4KtBhRMXwsHTSoJta7qxy2QbQ2QGZyfplgrmQyKx2EGDI4YX6m6RcbNbSomfoeRpD8LrAnn7UMiB0cJG5dCgG2rKBbIhM4HVe9LGcbBwol5HI_6e2-MuIULp2SK9Ze5oRuLPq9fRhQwxkgMDSPY4X0FhRpeLtoz20gxNFEsLkRapALUsUgJZwVyrjkcAdaLAe_-2I-ZEs8uCLrLMHeG5Fk37p8bIXIWVapY5Aj2Cmzr7Ovo4nFLGV4nQe6SbjCHSTijg3VRqmJF6RyJClm6r64qGX3YMATAfzii1pgbSMzituPJwzSITPWJSkEK4qnzuCWTzPN63Ml7TAkzgDouv2l46xFHXHg1cCRvdNr4D7_mO9xSF6Rz54SWd-IOePVLydx6bcgfkycuBbd2u5avcr9qLjYWqPLuPOzRjg3MUg4bqVGdCg1fF0Xnk9hX6jXPN6UoCrUbZ6CPtu8yof0D2n64aWJX4JvtRAz79MPvmYypSYeuyb5CD0L1mmjFNpxcOIbe3DBV9EEuZ6_JjD_-PkROsgq0_4VKZjN900PDzxrw0cMgHoALChAJvozpf4eWbkuJkJtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f717cb916.mp4?token=jAE8V8Au-LL7pn9m_PHDYPVye-1FkJ6nCGwqgORiOv6n6cllvuSCMVIqI8WKCIkuXAFjpCDZN_2MBvprHp78LN57npv1Mc-er7SL4KtBhRMXwsHTSoJta7qxy2QbQ2QGZyfplgrmQyKx2EGDI4YX6m6RcbNbSomfoeRpD8LrAnn7UMiB0cJG5dCgG2rKBbIhM4HVe9LGcbBwol5HI_6e2-MuIULp2SK9Ze5oRuLPq9fRhQwxkgMDSPY4X0FhRpeLtoz20gxNFEsLkRapALUsUgJZwVyrjkcAdaLAe_-2I-ZEs8uCLrLMHeG5Fk37p8bIXIWVapY5Aj2Cmzr7Ovo4nFLGV4nQe6SbjCHSTijg3VRqmJF6RyJClm6r64qGX3YMATAfzii1pgbSMzituPJwzSITPWJSkEK4qnzuCWTzPN63Ml7TAkzgDouv2l46xFHXHg1cCRvdNr4D7_mO9xSF6Rz54SWd-IOePVLydx6bcgfkycuBbd2u5avcr9qLjYWqPLuPOzRjg3MUg4bqVGdCg1fF0Xnk9hX6jXPN6UoCrUbZ6CPtu8yof0D2n64aWJX4JvtRAz79MPvmYypSYeuyb5CD0L1mmjFNpxcOIbe3DBV9EEuZ6_JjD_-PkROsgq0_4VKZjN900PDzxrw0cMgHoALChAJvozpf4eWbkuJkJtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۲۰۵؛ بافقی‌های یزد در شب حماسه، پای عهد انقلاب ایستادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/463467" target="_blank">📅 20:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQIe6IiXHYxRPBcFXGAe8V1lK2UaVANFgWM3b6H3iJFN4e2la6eyTYZ_eBDV3nucTHMgW0MZ7g24yKUyRrYw4RcS7rj7tsdT-wz6SFjmR-fIiFMV40fi5r-YEklOsNh42RnHEMNhyVQspVcj0cF8REDmLIuKnvKpECPIHNrh1vzkgLV_uTfjCGucEtLchmeFjbmrgMgyvBSKLTkmQPcKhKmdpxQI4Ih_pCp4exoR0XeWmqk0j0UF8nIFmRtI9z7GmGsrTmpTPTxSZ2JagGH1ZzZAqPLqFnK_uzjC9YThU7ppgR6iHAaB8lhXY76PV6_rwwKmTgu5Y-Owf188PIDMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیروس ابراهیم‌زاده درگذشت
🔹
سیروس ابراهیم‌زاده بازیگر پیشکسوت سینما و تئاتر پس از تحمل یک دوره بیماری، دور از وطن درگذشت.
🔹
او در فیلم‌هایی همچون کمال‌الملک، هتل کارتن، شمعی در باد، مسافر ری، چهره، همسر، تحفه‌ها و مجسمه نقش آفرینی داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/463466" target="_blank">📅 20:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: دشمن سعودی استان‌های الجوف، تعز، صعده و مأرب را هدف قرار داد؛ این تجاوز گسترده
بدون پاسخ نخواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/463465" target="_blank">📅 20:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_9bhLVpVx_llHytofOS2pg51pZ-wefon0J2zaHx80CHlUDBpZ6yTlY6LYnxsAiXWlkvsRXlrL0sRV69zyW61_Cp0xt6qOucshi2hXBxj0Vt7kIcimRpBYTnIvLm-h5DGiXkDjtdjrn-jfyPL0gjPt_C0gv98UMYYK-OjS9BwUyqOOrOBbonvlY0JNFWPWZgYlOUDyTyG9doUjd2l0HWsqYQPhj8kc_I3cOQ-LkHJGoDEq7P9R21JLAp-jPsFXIEi2wlS-ep01EuXApAvf15OtzAwluKjHqVi9RrlA9fgOnrp8_Yk7cxL9cZqIy6jHea_UdnUqFoRKrrnRVZqDQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: هیئت حاکمۀ آمریکا نمی‌خواهد صدای حقیقت شنیده‌شود
🔹
بقایی: وقتی هیئت حاکمه‌ای حتی مانع از دسترسی رسانه‌های خود آمریکا به اطلاعات می‌شود و همزمان راه را بر خبرنگاران خارجی‌ از جمله تیم رسانه‌ای رییس‌جمهور ایران، که نمی‌خواهد صدایشان شنیده شود، می‌بندد، این کار مدیریت دسترسی نیست؛ بلکه به معنای تلاش برای مخفی کردن حقیقت و ادامه کارزار اطلاعات نادرست جعلی از طریق نقض حق دسترسی به اطلاعات است.
@Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/463464" target="_blank">📅 20:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38893fa310.mp4?token=SI4p6DtzWRH77BzhdV4JdtA3jQC4z0lWpXA5T3gG-nmWKT5mhf3FeWSvnRx6N0mklZcZDC1rBkebJfS9YJsmCoVsnIBC9a6fuwqDhNsEQe2z4PEGPHmEHSex-cKlO9CmlyhSss3JN7m-9N0WKDmtj4GXbL0A-9ghDFQHa0LYCNWAD7_ltPogir7CtkzDswoGglMxui8_Ng5_o5zSQJsG5QP2zw9aZ6YcVFpy6_VMGP1JhEWJAOMf59SPml9fy-ejvdiXzPeRtaJ0m2oTUCmZTfzDQEpWhUvMjRoo7-GZJ2bZmjoD4kvvrndbxVeCssWea8XReNQq5ecrsMiGUFwUIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38893fa310.mp4?token=SI4p6DtzWRH77BzhdV4JdtA3jQC4z0lWpXA5T3gG-nmWKT5mhf3FeWSvnRx6N0mklZcZDC1rBkebJfS9YJsmCoVsnIBC9a6fuwqDhNsEQe2z4PEGPHmEHSex-cKlO9CmlyhSss3JN7m-9N0WKDmtj4GXbL0A-9ghDFQHa0LYCNWAD7_ltPogir7CtkzDswoGglMxui8_Ng5_o5zSQJsG5QP2zw9aZ6YcVFpy6_VMGP1JhEWJAOMf59SPml9fy-ejvdiXzPeRtaJ0m2oTUCmZTfzDQEpWhUvMjRoo7-GZJ2bZmjoD4kvvrndbxVeCssWea8XReNQq5ecrsMiGUFwUIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد
🔹
قوه‌قضائیه: دادستانی تهران علیه مجری، تهیه‌کننده و ۲ نفر از مهمانان برنامۀ اینترنتی «با ضیا» به‌دلیل طرح ادعاهای کذب اقتصادی و اظهارات غیرمستند اعلام جرم کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/463463" target="_blank">📅 20:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3TBwtT3CtCjmvJjL3-65sqwTIinfcikXE4d-MeZsU5HZ0gf1aRh3aHIKMjRXHz6mLOjw4xSGkEz3HxM4NwmENvYEMT7I_F8oVqQ4D2DIlpb1vdZcK1dyQbIwKOxk5MCj_j_V9zhff3vbYRaAPMIp0LfGSRso5VhvAIv64E51gU8-G-v_uA0kzdnS6Q0lqKigQw5aCRfz3kMRl5EdTHz3iDP7DPCBeMz101nlO5vuVNKBb0X2Np8-HgWooaN8mr3Uy6vU4UIi6ImOG0RtONkSlZR_Q-UID8PUmsrenhFH_pjyNqo8KdIMIWXhNBKS8pNMHuYP84qR2JBketaHQ8xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سود میانجی‌گرها؛ عبور ال‌ان‌جی قطر به مقصد پاکستان از هرمز
🔹
بلومبرگ می‌گوید پاکستان مجوز عبور یک محمولهٔ دیگر ال‌ان‌جی از تنگهٔ هرمز را از ایران گرفته است.
🔹
در همین ماه یک محمولهٔ دیگر هم از قطر با مجوز ایران از تنگهٔ عبور کرده و به پاکستان رسیده بود.
🔹
این کشتی حامل ال‌ان‌جی قطر قرار است فردا به پایانهٔ واردات پاکستان برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/463462" target="_blank">📅 19:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng55FA6-JnqPGj2fzyWX8khLgY5CtGktDrg2ef7Qeam4SppKq_yXSVnoM23fAYdTaVOVx73Syew0BopasNvKLRZrzepeZTWFBx0Mzqi4JZQQKEUWMjMpg-V-aAS9vB3W8YACtMhkV7vqf-V-aSp4MfjHHivs-QI-Byll1uqmjkyC_3gDy0zk31S8BoEsJQFgcMaJGyfzU3KUoQ4FGdEX_8s5zh1uO3FTQcHlWQaUZlulrAKME6j3XdmQGBchigT6W1Z0z_5I2-Uw0LmsKPoLznHv1BUB8TSOUwq4vDBL2SU2EEgS9JnwiHn25o0txgoHXtJ1S2PboMkBUPjn7ppi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عیادت نمایندگان رهبر معظم انقلاب از سیدعلی موسوی‌گرمارودی، چهرهٔ ماندگار شعر و ادبیات
🔹
غلامعلی حدادعادل و حسین محمدی به‌نمایندگی از رهبر انقلاب با حضور در محل بستری سیدعلی موسوی گرمارودی، هنرمند انقلابی و چهرهٔ ماندگار شعر و ادبیات کشور، از او عیادت کردند.…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/463461" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mamrOb7dxuEpo5fEsZ_c8ZUm5VMNQWKK7MGe8KGFJ55M9wwQoGa3MB5hmil5bISn2mFjKbBUUU6bF-TT0bcuNLeg9OD3rlVduie7f4CUY0P6DsvkijGnx6nKp6OuF77wvpxySwppurB9h7zegMvuCPhlZDSV1h_7HuuCK3KpIYgccD7D-yx4MrpSfCqIwSDoaL3qMWdIKMFHeI2rgctOn4TlPtpnkkLGhIyNUUaCVkiCgmB9EQ4RGays44njPZzPXWL-Xe7ebbeCdOSwmeRTw8-9VGoyi6l71wrcr7vj3eSkU43y22gnInRdJ0EWgk0FHJzdI2dyXRXL-RH6GeTS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۰۷ ماینر در یک خانه در بندرعباس
🔹
مدیرعامل شرکت برق هرمزگان: ۱۰۷ دستگاه استخراج رمزارز غیرمجاز در یک واحد مسکونی در بندرعباس کشف و جمع‌آوری شد.
🔹
در صورت مشاهدۀ فعالیت‌های مشکوک مرتبط با استفاده غیرمجاز از برق برای استخراج رمزارز، موضوع را از طریق سامانهٔ پیامکی ۳۰۰۰۶۱۲۱ گزارش کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/463460" target="_blank">📅 19:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41cb84f9c.mp4?token=wBryn2PicvDd_JN7i8zmMAOmQ0_EJd2T0_lKqSBhcGzZVggzBjuvfybrIKQEV3ACyofw1qELB2yOYei0_w5t1-02rod7DI6h8OczmLvUVFgSxVhVy5K1KWeh6XC7V4AWfl4f5wpST2hLpay5sJbTx14Huz-gWTd7cZOGhpap05zkAkte7aQbeijPmbVLP-Z7yAxYDQYra4BwMnDkN0oi-bHMwKkodQwbrlaBu4Llo6J4T8L-vhTdZDdoM7FkAMe4aDgokyUr8DL7n0nmmztTIhPKM0tBX7WTE1OqIGnE3b1UUm02fLTC3eVTlH_d8Yzcs6xyFOi50yCMRSMM7d_AtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41cb84f9c.mp4?token=wBryn2PicvDd_JN7i8zmMAOmQ0_EJd2T0_lKqSBhcGzZVggzBjuvfybrIKQEV3ACyofw1qELB2yOYei0_w5t1-02rod7DI6h8OczmLvUVFgSxVhVy5K1KWeh6XC7V4AWfl4f5wpST2hLpay5sJbTx14Huz-gWTd7cZOGhpap05zkAkte7aQbeijPmbVLP-Z7yAxYDQYra4BwMnDkN0oi-bHMwKkodQwbrlaBu4Llo6J4T8L-vhTdZDdoM7FkAMe4aDgokyUr8DL7n0nmmztTIhPKM0tBX7WTE1OqIGnE3b1UUm02fLTC3eVTlH_d8Yzcs6xyFOi50yCMRSMM7d_AtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، دست‌به‌دامن زلنسکی برای کنترل بحران سوخت شد
🔹
با تداوم افزایش قیمت سوخت در آمریکا دونالد ترامپ، رئیس‌جمهور اوکراین را تحت فشار قرار داده تا حملات به پالایشگاه‌های روسیه را متوقف کند.
🔹
یک منبع آگاه به فایننشال‌تایمز گفته تمام تمرکز گفت‌وگوی روز یکشنبۀ‌…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/463459" target="_blank">📅 19:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgU15QRFLQGMbwA83dz5xNAVdYvwGyq9NOfcwCu_rZiARZi1H8rdjpMiVxsfXBJRTDPgMbQ4fiO4cR_1lvu4pBCxKhlNG472jlwxO44BX5anwTBIoYdv-xJIYEu5H-wdj164CMAqNaykd-s98eNL1f28RjCzAVyK2McDrgKUzv-9yvIUwc3eytmq-OQJPvIOO6cIGnR23K9dL3ToBrKzOMycK-Be938NQMwTnEms9nWJvIK78LfBVvJ5_MeZn1IITCGu0qubpb3D86YxI_WrZRtgbydC7xTyBedNRZiJINAwDw4fRX1kl-_4F2FkDCePIGxqH6kx6Z3MZzFnKYTQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، دست‌به‌دامن زلنسکی برای کنترل بحران سوخت
شد
🔹
با تداوم افزایش قیمت سوخت در آمریکا دونالد ترامپ، رئیس‌جمهور اوکراین را تحت فشار قرار داده تا حملات به پالایشگاه‌های روسیه را متوقف کند.
🔹
یک منبع آگاه به فایننشال‌تایمز گفته تمام تمرکز گفت‌وگوی روز یکشنبۀ‌ ترامپ و زلنسکی بر مسئله عرضه گازوئیل روسیه متمرکز بود.
🔹
این منبع آگاه گفته ترامپ در این تماس از زلنسکی خواسته حملات به پالایشگاه‌های روسیه را متوقف کند، چرا که نگران است این حملات کمبود جهانی گازوئیل را تشدید کرده و قیمت‌ها را بالاتر ببرد.
🔹
یک مقام ارشد اوکراینی هم به فایننشال تایمز خبر داده که پیام اصلی رئیس‌جمهور آمریکا دربارهٔ «گازوئیل، گازوئیل... گازوئیل» بود و از زلنسکی می‌خواست به ارتش خود دستور دهد که حملاتش را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/463458" target="_blank">📅 19:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpWR2ueMbVuW8wd7NKDp6QD2Q645RMaJh8ITKHy8IH56F_6GFOwLHi0ctn2L0OqclRQs-Ic2IYECLIz2lU5Vc1hkk4LLyjZQeq-bSfSTjZslapfnavUNZVYPuThYHctCHHR8Psqwtn_wpQUydKIZEqSpbEv2TW5MJNF5Sd65wN4j_r8zR8DNWR_R4WbYzDx4ooZC8_U9ODqoPXsHgn_ptpWdmv5t3c0cqwyGLYwMatfnvsaYHc8mffb4F3HTZYGbHdMDu_YOG-_fCQUpIX8mV-81FFj4921Hk_CVWjRb9mOF8Pf2jwmI6MaQaFOBDAUCNH-rCGm3lPQ85IukUqLVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هرکس در حوزۀ هوش مصنوعی پیروز شود، پیروز است
🔹
ما الان از چین و همهٔ کشورهای دیگر جلوتر هستیم و من می‌خواهم همین‌طور باقی بمانیم. من نمی‌خواهم رشد چیزی را که از انقلاب صنعتی یا حتی خود اینترنت بزرگ‌تر خواهد بود، محدود کنم.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/463457" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1e33680f.mp4?token=qgMvpUVbSRhyfV7RIQv4kxarOXknF2WOCBLc9FIEhQd-RYm_UvXFceSy95psxTIM55-harBWtr9a7cgUhzkgeYLVHq-49S6uwJ6QGrNZrulcgL8wSwcuA-WA_GOG5g_KH-XpHRemCj6Wsr_BAjNhP-iexLzSPz4PvO3Fr_-SQdinS1pFoysoInshnDTn_Nuf7DDD06nt42OkxUpk_eJeI_X0264vZ7nU0bUEhkErs1b88LDheeQLi6RhqGYDooNDp7uGNnJ2KFqpMigI4DpqM2b3IsXlKs109Unc9hKUw7Oc3UlJ2cC8-7o48-R4tRhyxhHdAAUyPIGAFeJWjkGYeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1e33680f.mp4?token=qgMvpUVbSRhyfV7RIQv4kxarOXknF2WOCBLc9FIEhQd-RYm_UvXFceSy95psxTIM55-harBWtr9a7cgUhzkgeYLVHq-49S6uwJ6QGrNZrulcgL8wSwcuA-WA_GOG5g_KH-XpHRemCj6Wsr_BAjNhP-iexLzSPz4PvO3Fr_-SQdinS1pFoysoInshnDTn_Nuf7DDD06nt42OkxUpk_eJeI_X0264vZ7nU0bUEhkErs1b88LDheeQLi6RhqGYDooNDp7uGNnJ2KFqpMigI4DpqM2b3IsXlKs109Unc9hKUw7Oc3UlJ2cC8-7o48-R4tRhyxhHdAAUyPIGAFeJWjkGYeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان غذاودارو: کارهای واردات ۲.۸ میلیون دُز واکسن آنفلوآنزا انجام شده و مردم باید چند روزی صبر کنند تا وارد کشور می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/463456" target="_blank">📅 19:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267a6b76.mp4?token=Cbv1jPo1rl4ByuVWZje_QS2MtEO61hS06tHpFbshei9gETqJxS7tr-iL2r2y7BWi_SzmpGzZx98eHb6id5QSZdIbu6hv0qTlidiQDGtyYrjAfPDcrVX-A8Gk2kq96sv4yOAk9QSZYPuGpe_jFol15rS6Ope9TsrXc_QiIKTKljnyQ5S1YGG8gBAc53KZIFTLyOyaBKCX2A8sDAvujrLopKozyQsnUsxQbRhgVUCbExG2o-oTrNLDANf1rjk2FWMVtqLEM45t9xwivGyUB6clnmgM44EgoKGbc58zqOzTHrjOWL-w_78mGMyua42_6O-UXkKoTp3vJTST9if_AY4-hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267a6b76.mp4?token=Cbv1jPo1rl4ByuVWZje_QS2MtEO61hS06tHpFbshei9gETqJxS7tr-iL2r2y7BWi_SzmpGzZx98eHb6id5QSZdIbu6hv0qTlidiQDGtyYrjAfPDcrVX-A8Gk2kq96sv4yOAk9QSZYPuGpe_jFol15rS6Ope9TsrXc_QiIKTKljnyQ5S1YGG8gBAc53KZIFTLyOyaBKCX2A8sDAvujrLopKozyQsnUsxQbRhgVUCbExG2o-oTrNLDANf1rjk2FWMVtqLEM45t9xwivGyUB6clnmgM44EgoKGbc58zqOzTHrjOWL-w_78mGMyua42_6O-UXkKoTp3vJTST9if_AY4-hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر بهداشت: کمبودی در واکسن‌های ضروری نداریم
🔹
هیچ کمبودی در واکسن‌های موردنیاز عموم مردم، به‌ویژه کودکان، وجود ندارد.
🔹
با وجود جنگ و تحریم و محاصره، واکسن‌های ضروری تأمین شده‌اند.
🔹
واکسن‌های فصلی مانند آنفلوآنزا نیز به میزان کافی تهیه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/463455" target="_blank">📅 19:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff46b68e7e.mp4?token=Jrc118poIS_pbbQ31Oj8RQHERzL1d4c4qrkG-DJ2L_W8r7_hdNLyUlSNK7hp-sQO0zR_nr2Cd1CGtBU-hARDpqc-MEXiEV2djI5WR-GRZyjsShwGf7T3aHQ4kCuU6b8kHPTAxNzZ_E8C-kVjF-pwJCPtuDh71rC7NZgOy7keAcBZorvMLVe_YjVlD5xp47olCG_LeXZ-oOj2FIibDGGw2ldg4JI4psMjU4dr0RUiGK6ASwlsyEzkK0wk8aCuTysXEU9tX48nFdNcDg1-3WEDRtTw7cIB3xSoto-oIZBuUepW4JhV47wHe7PHFbgMXowDZQYfcg-By9gHbCycoAXShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff46b68e7e.mp4?token=Jrc118poIS_pbbQ31Oj8RQHERzL1d4c4qrkG-DJ2L_W8r7_hdNLyUlSNK7hp-sQO0zR_nr2Cd1CGtBU-hARDpqc-MEXiEV2djI5WR-GRZyjsShwGf7T3aHQ4kCuU6b8kHPTAxNzZ_E8C-kVjF-pwJCPtuDh71rC7NZgOy7keAcBZorvMLVe_YjVlD5xp47olCG_LeXZ-oOj2FIibDGGw2ldg4JI4psMjU4dr0RUiGK6ASwlsyEzkK0wk8aCuTysXEU9tX48nFdNcDg1-3WEDRtTw7cIB3xSoto-oIZBuUepW4JhV47wHe7PHFbgMXowDZQYfcg-By9gHbCycoAXShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواهر سلطان در عالم کار سلطان می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/463453" target="_blank">📅 19:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5e3c50fe.mp4?token=ZpFc_c_HNgpPwYJ6dUn9fDB2FZhunU7oUuLkM420-tLHmK20v5FBwvk_pC28QBe37_-2aXGt0bz5FkWEhJEE4bN1XBKQecrOOstTwlBQSrH4_LIlPIES95PxbVpk7vpLsU9eYySEIO6r2g1LS7k4IbYkyYReMbgdDprmfOH18t2znn1agKp6BxHVvPGbvMxtYz8SDS3K0WuoMYz5Pbxrx234_KSq9go49x-IqARSlfuwXntSrzZa8bHW9_CARGFQuef2SHay-Q0F5tBpx87FDKhRGsO-sp1GTKRyIDHFmf_s6JxdQnK1vcTo5EHB9ekLd-bkj2fNDHx74xEAyPslBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5e3c50fe.mp4?token=ZpFc_c_HNgpPwYJ6dUn9fDB2FZhunU7oUuLkM420-tLHmK20v5FBwvk_pC28QBe37_-2aXGt0bz5FkWEhJEE4bN1XBKQecrOOstTwlBQSrH4_LIlPIES95PxbVpk7vpLsU9eYySEIO6r2g1LS7k4IbYkyYReMbgdDprmfOH18t2znn1agKp6BxHVvPGbvMxtYz8SDS3K0WuoMYz5Pbxrx234_KSq9go49x-IqARSlfuwXntSrzZa8bHW9_CARGFQuef2SHay-Q0F5tBpx87FDKhRGsO-sp1GTKRyIDHFmf_s6JxdQnK1vcTo5EHB9ekLd-bkj2fNDHx74xEAyPslBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از پیام و پیگیری رهبر معظم انقلاب دربارۀ جان‌فدا  @Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/463452" target="_blank">📅 19:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNf5aqKUv1jmwMke71iSzOXCHi2zqrIG8j9rH33W_EZLzIOB6pHeqpBeMSi0_KnIMbw7Sux4ExLzxLcVwCSEwM7nHg29z7LfUqTtOTtyK5oscPcuVjWco1JkE_cQiHAZ2S1T9331L8WCI1cEyR4kuCWRI-qNC6vdn-GMANL3rIjDtsayWii4Vro7jxENykClbvmpNZ5uO86tJ1HTZjzCdhQtcbnvGXkL4Qjx4SDj4_Lyq_GHEWMX4WTLpRVc-UiPLtz2KC8uFEkgWNW_I-SBpY9az59WbuIZMumkcXpgbhA_tE57eTgpYH-LS_HrQddcU2v6arI24aO7P6cgkkOwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز زبان فرانسه یا محل اجرای پروژه‌های ضدایرانی!
🔹
مرکز زبان فرانسه تهران موسوم به CLF که امروز با دستور قضایی دادستانی تهران پلمب شده، مرکزی وابسته به ساختار فرهنگی فرانسه است که مدعی‌ست در تهران در حوزه آموزش زبان فرانسه، برگزاری آزمون‌های رسمی TCF و DELF/DALF،…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/463451" target="_blank">📅 19:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d86b1053.mp4?token=XEpvYEbd_5HfelZ8C07o-RORViwko_Exd6_MqFzKzRB55fUlQVKrFwAhEUKwsOeNN4q6yr98oyWM8K37FdB17n-j70MY_vO-eU3HB4clrvVu8ZgnKfEerrWbHwdtc9Pqc-e3oKSCwioCqy1QmTonVWVQWFc2YWxVjprxnKVp1mdhHYUj2YLj08lFSdFCEwFyEz5d_oT1YcsLO-ahkVnUE9TdQ8SypJVApwOt5JQ6ROkhuXRYxvfZq56V5X0aBHnXYSVjgbb2DsrMNqsjs6I9zZm9z7Mb0cn4391LQhQiJRPgw6Wo4Or8fvSU7VdA7VbW9I5O3HXbMTvZxD8w1Dkezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d86b1053.mp4?token=XEpvYEbd_5HfelZ8C07o-RORViwko_Exd6_MqFzKzRB55fUlQVKrFwAhEUKwsOeNN4q6yr98oyWM8K37FdB17n-j70MY_vO-eU3HB4clrvVu8ZgnKfEerrWbHwdtc9Pqc-e3oKSCwioCqy1QmTonVWVQWFc2YWxVjprxnKVp1mdhHYUj2YLj08lFSdFCEwFyEz5d_oT1YcsLO-ahkVnUE9TdQ8SypJVApwOt5JQ6ROkhuXRYxvfZq56V5X0aBHnXYSVjgbb2DsrMNqsjs6I9zZm9z7Mb0cn4391LQhQiJRPgw6Wo4Or8fvSU7VdA7VbW9I5O3HXbMTvZxD8w1Dkezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حضور جدی مردم در کف میدان از زبان سخنگوی ستاد مردمی جان‌فدا  @Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/463449" target="_blank">📅 19:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e92902081.mp4?token=dLl-cGeqSQyvAeAC2rYEl2cA20s2x0ixEQRL7w3MOibDWmrRJHoROXdANhGu4YkmEhl19HOfRImaQs8ybID8w0mMjro-9cXfwBcahJlxXRil8ETp7iAv2LaRir0wdKKBkWmOEUMtOu19RUhhkHUfU0cw-94j9rOO5Knkdbj4qJF2VFbmvbQQ1rfkPOi98uBZuZQybhJVio7WHrMfdtVgUJcNBhjXsKdZCl7OfQAmzUcQKQPzt2EafavW_8Y8Mb2lSvndMbd7TdhP9CTsd5lYl77Py9N_qJHIQj4spsdQAXRGdPAdm4JiagEEXzM135gj653CaqtgkIxc7daq_2cncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e92902081.mp4?token=dLl-cGeqSQyvAeAC2rYEl2cA20s2x0ixEQRL7w3MOibDWmrRJHoROXdANhGu4YkmEhl19HOfRImaQs8ybID8w0mMjro-9cXfwBcahJlxXRil8ETp7iAv2LaRir0wdKKBkWmOEUMtOu19RUhhkHUfU0cw-94j9rOO5Knkdbj4qJF2VFbmvbQQ1rfkPOi98uBZuZQybhJVio7WHrMfdtVgUJcNBhjXsKdZCl7OfQAmzUcQKQPzt2EafavW_8Y8Mb2lSvndMbd7TdhP9CTsd5lYl77Py9N_qJHIQj4spsdQAXRGdPAdm4JiagEEXzM135gj653CaqtgkIxc7daq_2cncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای ترامپ: خطوط لوله در سراسر خاورمیانه درحال احداث است تا دیگر نیازی به عبور از تنگهٔ هرمز نباشد.
🔸
ترامپ تا پیش از این مدعی بود کنترل تنگهٔ هرمز در اختیار آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/463447" target="_blank">📅 18:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd66c8779.mp4?token=qVmaIFKD2hDGrMKqiip8LGkW0mA6jd_Aa7Cug1Ns84ptyHviKEU-xrGAzbe73wGyI4bjjxUzKOshFPilxTaSzCMl7Ny4OCo8E8hnz_cjS4mumpdwj6W3fckt6PAVlYAzgeHXolgflOOvJ5ECH8akD-4OxKI58Yv4idTa545o-nmBqB6wzDE7d74dXrcp6WXn8JV9q1UIfCBmDwYwbmP-WZAhD6atB7rrlnL872UH2cMgF6AYtkg15p59hL1UkJqi0r30uLIhawXs6eKYL43my6c_oxNsKx6jIfjsvAlLA_decq37BlwVaF2R85hY95_mI2wjrnOWf_ooPbw3GCcnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd66c8779.mp4?token=qVmaIFKD2hDGrMKqiip8LGkW0mA6jd_Aa7Cug1Ns84ptyHviKEU-xrGAzbe73wGyI4bjjxUzKOshFPilxTaSzCMl7Ny4OCo8E8hnz_cjS4mumpdwj6W3fckt6PAVlYAzgeHXolgflOOvJ5ECH8akD-4OxKI58Yv4idTa545o-nmBqB6wzDE7d74dXrcp6WXn8JV9q1UIfCBmDwYwbmP-WZAhD6atB7rrlnL872UH2cMgF6AYtkg15p59hL1UkJqi0r30uLIhawXs6eKYL43my6c_oxNsKx6jIfjsvAlLA_decq37BlwVaF2R85hY95_mI2wjrnOWf_ooPbw3GCcnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سخنگوی ستاد مردمی جان‌فدا از حضور داوطلبانۀ پیرزنی با واکر برای دفاع از وطنش  @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/463446" target="_blank">📅 18:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=K6sDIt4iVlLv13fOm9M7e9J9covg8Lf14huolVsKj5pkhdG4mwLqlcfw8pDA6_OPF4lZ4ZqiFdfNpClHdg335zmDFS-q3ZukivW2dd69k24aVXvbjcdRxIiGrAwfV1ZVBJ254OFjAldxZU5ZXYO83iwFS3nM255KPXyvNB5HtdlLwdevHT9YZHUH1sjTxeh-sYFYAeR2s3_EDYX3-gysUign6kTaeSrTuqxTcg2vi9FgCadJwREr4F3mkCYeXh7EKfB1gaicL_Nwxa8zPDyZe8Ek8j1EVkUsuv3U8R2udMrEvL3VB__QA996M_NOXwvGCbV0reea5yLcc2ApDHgeRABWl6cZyQ88n9YoEeGxQH0rDZgV3_YjHl_sarCEss3U4Q9YwPODLJiIeYigCvLNIRlGHe91cXEPRWlX5j_XyEgQGwT7izCRUDiEFjx1QyfuJCZMaEZVO6whoSCqVkUYdIQPT55fR1HnuelHNME--5BJawNBosh3N_s8fUOLFGi33FgOyxRAWdecTNZvLS62CAy43f2Oc13BhKx_dcp2mjupiAjyQXnB9pTzIsm8MLXE2Yeu0oKg1kV2OhSIjX2ndVJmlVaBMue1tAKV_MGInm2sU8qoOtE6T4G4dSemLCYFOgWe_WjiOFI3o9XrOs_VsKtVm8xcVxeCZLPb3ql_VZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=K6sDIt4iVlLv13fOm9M7e9J9covg8Lf14huolVsKj5pkhdG4mwLqlcfw8pDA6_OPF4lZ4ZqiFdfNpClHdg335zmDFS-q3ZukivW2dd69k24aVXvbjcdRxIiGrAwfV1ZVBJ254OFjAldxZU5ZXYO83iwFS3nM255KPXyvNB5HtdlLwdevHT9YZHUH1sjTxeh-sYFYAeR2s3_EDYX3-gysUign6kTaeSrTuqxTcg2vi9FgCadJwREr4F3mkCYeXh7EKfB1gaicL_Nwxa8zPDyZe8Ek8j1EVkUsuv3U8R2udMrEvL3VB__QA996M_NOXwvGCbV0reea5yLcc2ApDHgeRABWl6cZyQ88n9YoEeGxQH0rDZgV3_YjHl_sarCEss3U4Q9YwPODLJiIeYigCvLNIRlGHe91cXEPRWlX5j_XyEgQGwT7izCRUDiEFjx1QyfuJCZMaEZVO6whoSCqVkUYdIQPT55fR1HnuelHNME--5BJawNBosh3N_s8fUOLFGi33FgOyxRAWdecTNZvLS62CAy43f2Oc13BhKx_dcp2mjupiAjyQXnB9pTzIsm8MLXE2Yeu0oKg1kV2OhSIjX2ndVJmlVaBMue1tAKV_MGInm2sU8qoOtE6T4G4dSemLCYFOgWe_WjiOFI3o9XrOs_VsKtVm8xcVxeCZLPb3ql_VZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
جان تازه در رگ‌های فلک‌الدین خرم‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/463445" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzuZzoLGXWAVD1Q40d2wiPZh6blIx5S1nIV_j2Q4ffIrAHQul8nt5BgRbTYR8rHZhr7O_bbFDke7_WuZx1McrUzETNvmKE1lOuZKyfNWjHFhcarAKjQR7hxbPYFueFgNwpwXP5CboNJgk1M55wq6QaQZIwgssAW2YLBKMPcqQJNrAL-UyaBNCUy0PRd5v8nvtQSj1po3DXpsZ_cVNbp3GN9fjsvW-_dPrMdf_UTmanlH-spSFahCaQRRen63dNVMlDezFKdFEcdjBxawqmRZL-EfxZiSo71aI1XsnX8OSeYPnOMhVQG3ty7sA-Zwovv454uvQpVqW6GDLCje7_p9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور بانک کشاورزی در IRAN AI 2026؛  گامی در مسیر توسعه بانکداری هوشمند
🔻
کنفرانس و نمایشگاه «کاربرد هوش مصنوعی در صنایع و کسب‌وکارها» (IRAN AI 2026) با مشارکت بانک کشاورزی و به میزبانی دانشگاه صنعتی شریف؛ با حضور مدیران ارشد، متخصصان، پژوهشگران، شرکت‌های دانش‌بنیان، استارتاپ‌ها و فعالان حوزه فناوری آغاز به کار کرد.
🔻
مشارکت بانک کشاورزی در این رویداد، گامی در جهت تعامل با زیست‌بوم نوآوری کشور و بهره‌گیری از ظرفیت‌های هوش مصنوعی برای شتاب‌بخشی به تحول دیجیتال و توسعه بانکداری هوشمند به شمار می‌رود.
🔻
این رویداد تخصصی روزهای ۳۰ و ۳۱ شهریورماه در دانشگاه صنعتی شریف برگزار می‌شود.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/463444" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/463443" target="_blank">📅 18:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg9eN4oUGzOffFQWDrYkrQtl2SPJwm6AQ2F3gIYz6xLn_ZdBwUQ0_YEwVm0c3nyRlLgwvKA-2T1UUriFNz6YZMmC9Lwm2Fhg5D3w8id2NJ_bHfROPGYXvu8yzykk4g4mHgjWg4OnWtGrOT822xGqUtTh_PdkQ1r6xZX6fIjp2YuS83zY8TYaOk8uHpWPA98_n8F2EPXbI-m4DXllXzthiHM16zweN9uuW4JpH9spzli9qDFlsIHP6EBGDEmwylN4s7Ih9j3ilYvmNCRcZZa7siyr2Ad-eCV8G79d44VOw-d49WturPF2p-nNRc1BabbTrljUFZCMPgqDAgA6o3BuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان به دنبال حذف ایران از جام ملت‌ها
🔹
گفته می‌شود برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانۀ جام ملت‌های آسیا تعلیق کنند؛ این یعنی احتمال حذف تیم ملی از جام ملت‌ها وجود دارد.
🔹
افراد مطلع بر این باورند که این پروژه شبیه پروژه‌ای است که برای فوتبال روسیه در محافل بین‌المللی رقم خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/463442" target="_blank">📅 18:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: در هر مرحله‌ای از تنش‌افزایی صهیونیست‌ها علیه ملت فلسطین، با قدرتی حتی بیشتر از آنچه در طوفان‌الاقصی نشان دادیم، در کنار فلسطین خواهیم بود. @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/463441" target="_blank">📅 18:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463440">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: تمام تلاش رژیم سعودی در این برهه، وارد‌کردن ترکیه و پاکستان به جنگ و آوردن تکفیری‌ها از سوريه است
🔹
ما به ترکیه و پاکستان توصیه می‌کنیم خود را آلودهٔ منافع سیاسی و مالی بادآورده از سوی دشمن سعودی نکنند.
🔹
دشمن سعودی با مقدسات کاسبی می‌کند؛…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/463440" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی مکه را اشغال کرده؛ ما از آن‌ها به مکه وفادارتریم
🔹
رژیم سعودی بیش از هر طرف دیگری از بزرگداشت شعائر الهی فاصله دارد؛ بلکه آن‌ها را شرک می‌داند و از زمان اشغال مکه مکرمه، مرتکب فجیع‌ترین جنایت‌ها شده است.
🔹
مردم باید جنایت‌ها…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/463434" target="_blank">📅 18:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: گرفتاری‌های منطقه‌ای، دست‌وپای آمریکا و اسرائیل را برای همراهی با عربستان بسته است
🔹
کارشناسان آمریکایی و صهیونیست، دوشادوش دشمن سعودی درحال همکاری و فعالیت هستند.
🔹
ضربات کاری و ایستادگی مؤثر یمن باعث شده تا دشمن سعودی تلاش کند پای آمریکا…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/463433" target="_blank">📅 18:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی می‌خواهد ترکیه و پاکستان را هم وارد جنگ با یمن کند و شب و روز دست به دامن آن‌ها می‌شود
🔸
حملات هوایی عربستان تا دیروز از مرز ۷۶۰ حمله گذشت؛ اگر حتی همین تعداد حمله به پاکستان یا ترکیه شده بود، جنجال و بحران بزرگی به‌پا نمی‌شد؟…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/463432" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avcd0EiPVx9SFmuw8gNYBuqCslCtQSOJILYkf2x5dwdR4xYM24ax0cNhebiYCunywL6wwBit4IXzV_RljOEf2g69SbVsw_WNSV9FBFMvwKucnl9u-rq1axReH_pCmAg8F21YR_89HSd2go7eCYcXX__pXht6nOaCIQUfcSpLjxh2dYDo1756MwpsQdGisWP9g2a3F6fE61zsDJNZDAa-dvQqMTQIgkrA6k_54y1meOPTbVZzLZ968PpOkTtp2Ab8484Wwve---QPAYZaLmNRPxEKWfgUwlID6r8v-dH0Ik8DYssofwrMVT3p1-SwHkVI3DVxYw02Vo2t8l5MQqsrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای کشتی حمل گاز در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس: یک تانکر حامل گاز مایع درحال خروج از مسیر جنوبی تنگۀ هرمز، هدف اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/463431" target="_blank">📅 18:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: آیا ترکیه یا پاکستان می‌پذیرند که عربستان در تمام سیاست‌هایشان دخالت کند؟ آیا کشورهای حوزهٔ خلیج فارس چنین چیزی را می‌پذیرند؟
🔹
دشمن سعودی می‌خواهد تنها مرجع تعیین مسئولان در کشور ما باشد؛ تا جایی که هرکس توسط عربستان منصوب نشود، هیچ مشروعیتی…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/463430" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
درخواست دختران میناب از وزیر آموزش‌و‌پرورش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/463429" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: کسانی‌که ایستادگی ما در برابر تجاوز و محاصرهٔ سعودی‌ها را زیاده‌خواهی می‌دانند، خودشان هرگز نمی‌پذیرند که عربستان فرودگاه‌هایشان را ببندد و مانع سفر شهروندانشان شود. @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/463428" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌ روایت رهبر انصارالله از همکاری سعودی‌ها با صهیونیست‌ها
🔹
رهبر انصارالله: رژیم سعودی فرودگاه‌های خود را در اختیار هواپیماهای شناسایی صهیونیست‌ها قرار داد تا از آن‌جا به سمت یمن پرواز کنند.
🔹
هنگام حملات ما به اسرائیل، رژیم سعودی تمام تلاش خود را برای رهگیری…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/463427" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb0b4a106.mp4?token=AHb6iWsgNO3xrPgrZpv4irqy0TZk7KE9Le12BLl47AuZ4A1p9fwzxOSl3dZwzaj_SnQSGtD6FnkbDbbbrn9TVRNlY-i-cWV2vvbMu6Jt7uQjcnB58TMai9JdwOaIn0mWZOUzs89iVko8VwFT_MXYCDtQbrOIF1NMzd7MFnLL8GTc3zIk7Dd6USdt9VyDRONugwfULip1zKhhnhcxNJNTahG9qQGfpiTFnO-dVXlGDFUuiZmwFXsh02Utoj7bwZPtCKa5Q8aCvxQqKVqQb8MSPLPglSzefzvtoftYjEdcLJ7aYFIMsxuGtf4-hwBnBl_-7xutr-bNQDqIbhtENEzaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb0b4a106.mp4?token=AHb6iWsgNO3xrPgrZpv4irqy0TZk7KE9Le12BLl47AuZ4A1p9fwzxOSl3dZwzaj_SnQSGtD6FnkbDbbbrn9TVRNlY-i-cWV2vvbMu6Jt7uQjcnB58TMai9JdwOaIn0mWZOUzs89iVko8VwFT_MXYCDtQbrOIF1NMzd7MFnLL8GTc3zIk7Dd6USdt9VyDRONugwfULip1zKhhnhcxNJNTahG9qQGfpiTFnO-dVXlGDFUuiZmwFXsh02Utoj7bwZPtCKa5Q8aCvxQqKVqQb8MSPLPglSzefzvtoftYjEdcLJ7aYFIMsxuGtf4-hwBnBl_-7xutr-bNQDqIbhtENEzaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد، نایب‌رئیس مجلس امروز مهمان خبرگزاری فارس بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/463425" target="_blank">📅 17:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
رهبر انصارالله: کشورهایی که برای تأسیسات نفتی عربستان اشک تمساح می‌ریزند، حاضر نیستند یک روز در شرایط محاصرهٔ یمن زندگی کنند!  @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/463424" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03dc3f3612.mp4?token=oTvmSKAvFSWf_-f5QcAdFeuYK-D6FSp5vgB9baKFNyMdpNAtyd70rABxvLEYRAm0ux1PuklYDhKjROAnMa-UqXc5op8JIC1KdrgQ_7X7ZXTkhE1chGnTjmx9n8DCdGSji4I57zaE1HLVsFOvGKfh71hKtbkdJ8YjNFSG2_3ksrBh8Cg0Z6rMlt8lQ-k7CH0xPxHFi1XKnSIMZ8C8ld8dzF-SfYmsod9E-K4E69gqD1gPBfo7cTilGmgvlSgJn8jzgfNP7Y6t5HDdY9NvG8tWdfVAJh74giF3eK3SBClNMSAWtQspmIG2R4gEVvqgqIVg-e8A--eKOfIS6FssInrYD2KBOJs7vqO-W3V8VVEOnmnT7uJnLMp6DTl0945s7H-RhvidoKxQ1bxNnHjSHcUahDApMXwxx1dkBuy9IIrsmiERCKg1VUWzzIWGT8bQEHTwdvzm29_jseiDr7Vo4QL5TO0FizKowpg3GeH57Ef1yfoOXxNrsQ_TtK7y00mvdonM3j0_BsUObMqoFLk1mz4LmshPcm1EyVhxv_FT3HDeoDjF99W1fNJdcCmURnJMgjU-dGZifiP-YMeWzssphUtdaJoZY7p4AWYyl01JvW0jJX5JK2CAKMnNlHTLu2TPvZonTt6KbXT8zvXNKFFCZzhjx2Q7gBBC9UVgVlUWt5VxxBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03dc3f3612.mp4?token=oTvmSKAvFSWf_-f5QcAdFeuYK-D6FSp5vgB9baKFNyMdpNAtyd70rABxvLEYRAm0ux1PuklYDhKjROAnMa-UqXc5op8JIC1KdrgQ_7X7ZXTkhE1chGnTjmx9n8DCdGSji4I57zaE1HLVsFOvGKfh71hKtbkdJ8YjNFSG2_3ksrBh8Cg0Z6rMlt8lQ-k7CH0xPxHFi1XKnSIMZ8C8ld8dzF-SfYmsod9E-K4E69gqD1gPBfo7cTilGmgvlSgJn8jzgfNP7Y6t5HDdY9NvG8tWdfVAJh74giF3eK3SBClNMSAWtQspmIG2R4gEVvqgqIVg-e8A--eKOfIS6FssInrYD2KBOJs7vqO-W3V8VVEOnmnT7uJnLMp6DTl0945s7H-RhvidoKxQ1bxNnHjSHcUahDApMXwxx1dkBuy9IIrsmiERCKg1VUWzzIWGT8bQEHTwdvzm29_jseiDr7Vo4QL5TO0FizKowpg3GeH57Ef1yfoOXxNrsQ_TtK7y00mvdonM3j0_BsUObMqoFLk1mz4LmshPcm1EyVhxv_FT3HDeoDjF99W1fNJdcCmURnJMgjU-dGZifiP-YMeWzssphUtdaJoZY7p4AWYyl01JvW0jJX5JK2CAKMnNlHTLu2TPvZonTt6KbXT8zvXNKFFCZzhjx2Q7gBBC9UVgVlUWt5VxxBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: اگر در قبال جنایات رژیم سعودی در یمن، منتظر سازمان ملل، شورای امنیت و دیگر نهادها می‌ماندیم هیچ‌یک از کارهایی که الان با سعودی‌ها کرده‌ایم را نمی‌توانستیم انجام دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463423" target="_blank">📅 17:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎥
رهبر انصارالله: ما با کشورهای محور مقاومت اعلام همبستگی می‌کنیم
🔹
هر تجاوز رژیم صهیونیستی، آمریکا و انگلیس تهدیدی برای تمام کشورهای مسلمان است و وظیفهٔ کشورهای اسلامی، مقابله با این تجاوزات است. @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/463422" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463421">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb8c7aef2.mp4?token=i1ydA_KksOeSZzO3MChBS0EECqs1B2DX2YVkrHeEkpgF9aoA-nVwf_h51ZuGKASIIdi6KE1m0VuZxWYRwJf195sWCyhuYMBnjLCjSssO2_1hyYHUsJ8vBFHJXaerqYiXKuZgUAHXMjeVf5ysjt32SNPwc63DOyp-hmKWcndJ8iw9Yl9w4haua3xReOpaQBrzSyE0j-sWWJOg0nWCHOfRu3fgsQxZ3uG-xChCzCJU5GXQzCXevJ_9rg9dVXpYG85_QF1DAmK3ryydL3PomfGcbGaQjfh3pZjRBxNO-Xesn3uQ9otZQjXlIDHTg9Q43c88GVTQGWI0XJufl-ud3Fb2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb8c7aef2.mp4?token=i1ydA_KksOeSZzO3MChBS0EECqs1B2DX2YVkrHeEkpgF9aoA-nVwf_h51ZuGKASIIdi6KE1m0VuZxWYRwJf195sWCyhuYMBnjLCjSssO2_1hyYHUsJ8vBFHJXaerqYiXKuZgUAHXMjeVf5ysjt32SNPwc63DOyp-hmKWcndJ8iw9Yl9w4haua3xReOpaQBrzSyE0j-sWWJOg0nWCHOfRu3fgsQxZ3uG-xChCzCJU5GXQzCXevJ_9rg9dVXpYG85_QF1DAmK3ryydL3PomfGcbGaQjfh3pZjRBxNO-Xesn3uQ9otZQjXlIDHTg9Q43c88GVTQGWI0XJufl-ud3Fb2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم متجاوز سعودی تابع آمریکا، انگلیس و اسرائیل است و چیزی از خودش ندارد
🔹
رژیم سعودی با مشارکت آمریکا، از نخستین روز تجاوز خود، مرتکب هولناک‌ترین جنایات در یمن شد. تمام مصادیق جنایات جنگی در اقداماتی که رژیم سعودی در یمن مرتکب شد، وجود…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463421" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
رهبر انصارالله یمن: تا زمانی‌که هدف آمریکا، تسلط بر ملت یمن و تبدیل کشور ما به پایگاه‌های نظامی خود باشد، مشکل ما با آمریکا و عوامل آن ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/463420" target="_blank">📅 17:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1igNzNyZ9AYGHodpnr5xVgs9gHGPErW6810sydjs7m4G-fb2Fu79ngLEEKQu2iftf8R3Yoqy6SPdoN7T6pe1IvqadtqsgeZ0siVCI98pbxyGyg_y99SYnwpsdisosie2ima3zrjpdHd3Gf8Ltt0sWIiy4Vy9B9atUp1AmHkZV_BxEasKJuD2luAm6-R9NCNw2xYouHrO8ZlLT6A429RBv1gpvxoM6bpsdoPPrIJHUkUlHpctVklJ8VL2kv6MaUcNnkaKx4lULLUDoh5DNDy64YPsgiM2zGyx5wUdN8Ei6ctSZEo2xwXHnb8ScYM2EZd_R3bbZekpB3pK9J69sHRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ ساله برای مالکان خودروهای فرسوده
🔹
مالکان خودروهایی که به سن فرسودگی رسیده‌اند برای تعیین تکلیف وضعیت خودرو خود باید در سامانه ثبت‌نام کنند.
🔹
در این میان، آن دسته از مالکان که امکان اسقاط فوری خودروی خود را ندارند، با ثبت‌نام و اعلام آمادگی در سامانه تا پنج سال از محدودیت‌های قانونی ماده ۸ قانون هوای پاک مستثنی می‌شوند.
🔹
قانون هوای پاک، محدودیت‌های سنگینی مانند ممنوعیت تردد در کلانشهرها، ممانعت از نقل و انتقال پلاک، کاهش سهمیه سوخت و محدودیت فعالیت در تاکسی‌های اینترنتی را برای خودروهای با عمر ۲۰ سال و بالاتر (مدل ۱۳۸۵ و قبل از آن) تعیین کرده است.
🔹
متقاضیان برای استفاده از مهلت ۵‌ساله، باید از سه‌شنبه ۳۱ شهریورماه به
سامانهٔ نوسازی و اسقاط خودروهای فرسوده
مراجعه و ثبت‌نام خود را تکمیل کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/463419" target="_blank">📅 17:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
رهبر انصارالله یمن: تا زمانی‌که هدف آمریکا، تسلط بر ملت یمن و تبدیل کشور ما به پایگاه‌های نظامی خود باشد، مشکل ما با آمریکا و عوامل آن ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/463418" target="_blank">📅 17:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شهادت مأمور انتظامی در حملهٔ مسلحانهٔ ایرانشهر سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل، در پی حملهٔ افراد مسلح به یکی از مأموران انتظامی در ایرانشهر، این مأمور در حین انجام مأموریت به درجهٔ رفیع شهادت نائل شد.
🔹
تلاش مأموران انتظامی برای شناسایی و دستگیری عاملان این سوءقصد ادامه دارد و جزئیات بیشتر این حادثه متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/463417" target="_blank">📅 17:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqFp0OFkAx4oS2lzVn9VFcVOoXFkMIeys8CsxdK35EWBVbjfZdZoH_5OTWxIKfWgeHtTUyPY1W-a7G2_YcAYEVPurNAZuSqupRFbJFesDjY5tRfgUd7cKgQrpCnDDByBUDntEE8LkWwHJHnqbMgNnMOgtR98G3yXpydV7EZRBbCypPKfH33BdOTlYlvhu9MiwbO7zlGx1kKGWc1VKZYybudBkawo0_pjFKQyB8dXvyzIKnlCvpwCwsFA9Fljvh_DlWMkT6GPApVaDLTH-8LOt54ROLpIOVwCNI6d9DyqtQABEuznSjT0BK3yc8PfvZKKAWmQ0xvNgh2WNtuqCU0-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور چاپ پول بانک‌ها دنده خورد
🔹
نقدینگی ۵ ماهه ابتدای نسبت به آخر سال گذشته ۱۹ درصد رشد داشته است و حالا کل حجم پول و نقدینگی در اقتصاد کشور به بیش از ۱۸هزار هزار میلیارد تومان رسیده است.
🔹
این روند پرشتاب از مرداد ۱۴۰۳ و تقریبا هم‌زمان با شروع دولت پزشکیان شروع شد. آن زمان رشد نقدینگی حدود ۱۱ درصد بود.
🔸
اقتصاددان سعید لیلاز می‌گوید روزانه ۳۰ هزار میلیارد تومان به حجم نقدینگی کشور اضافه می‌شود در حالی که دولت ۶ ماه برای افزایش ۳۰۰ هزار تومانی کالابرگ بحث کرده است؛ این رقم خیلی بیشتر از مخارج دولت است.
🔸
مهم‌ترین عوامل رشد نقدینگی در ایران را می‌توان شوک ارزی، خلق پول، ناترازی بانک‌ها، کسری بودجه و نشتی منابع به فعالیت‌های غیرمولد دانست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/463416" target="_blank">📅 17:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFIq6WRxYJeSqDm-BP_u7Mk8YLZqte7LCvITHBcr0DzBiPpbwapH-6ZcLJjuK4Kz92yXLrziZdOgTvcSWIxwAl9JGEy__Lr8NKSyl2oEyimkR9W8P4CH6e7woT5E8ulujSUoh7EKyq35MocTn9lFiR2hk8afxYtKn4EKGK1fHTlYW61ETpM2TaKbdiAy-4pD_Ut6PN3pEzKJPyKKnMAZPtscejnjHiGr363JOc7zgfpNDChVnoelQgVEeYmcTYZ8Dzv9yvxPQ5NhvSnVj2LRum5OI-tqiWPKzWFg7AqK_6qn6Mv7rYyZLnsp6FOWFaMNjNQYPQnLl7RGbJdUPEYRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیرخزانه‌داری آمریکا: پایان جنگ با ایران، راه خروج آمریکا از رکود است
🔹
وزیرخزانه‌داری آمریکا امروز در مصاحبه با سی‌ان‌بی‌سی گفته که پس از پایان درگیری با ایران، نرخ بهره کشورش باید کاهش یابد.
🔹
۵ روز پیش، فدرال رزرو نرخ بهره در آمریکا را به ۴ درصد افزایش داد؛ نرخی  که ۳ سال بود تغییر نکرده بود و ترامپ برای بالا نرفتن آن رئیس این بانک را تغییر داده بود.
🔹
جنگ علیه ایران و بسته شدن تنگهٔ هرمز  و افزایش قیمت انرژی، تورمی برای آمریکا به ارمغان آورده که حالا ترامپ به بالا بردن نرخ بهره راضی شده است و این اقدام یعنی وقوع رکود سنگین در اقتصاد آمریکا.
🔹
حالا بسنت در همین مصاحبه می‌گوید، «نمی‌توانم به شما بگویم درگیری با ایران چه مدت ادامه خواهد داشت».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/463415" target="_blank">📅 16:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6933ee189d.mp4?token=n2DcV_8plag3T3lylgNfX_bfIFMQnA1AmVKHY-UeAVAvYXdoY1Uj_y-9za0wcJWexIDsZKnYREPgQQ9V1aG7AowjXxX-q9thjcY6xRn9AtOnNBRuz8acuwYFJfOkzzCQRGnsPNDIAzZM2K5PdU8peokYBLjKJHXAL-kUemKaJmV6oCvumTy8XAkncbgueXjOfNknTwuoxIXq9Kn4mCaB3ivoepOcI1NWi7nocQNo_jqvAoXI3Oty22wo-C-4KWrl6ysUHTShuoHIQCiCfVBOcmm0HvI3afLLr_feJ9pprsuz83Mw7LY9nnin3kudb5Q5Y67owFYWYMy_OjPN76l8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6933ee189d.mp4?token=n2DcV_8plag3T3lylgNfX_bfIFMQnA1AmVKHY-UeAVAvYXdoY1Uj_y-9za0wcJWexIDsZKnYREPgQQ9V1aG7AowjXxX-q9thjcY6xRn9AtOnNBRuz8acuwYFJfOkzzCQRGnsPNDIAzZM2K5PdU8peokYBLjKJHXAL-kUemKaJmV6oCvumTy8XAkncbgueXjOfNknTwuoxIXq9Kn4mCaB3ivoepOcI1NWi7nocQNo_jqvAoXI3Oty22wo-C-4KWrl6ysUHTShuoHIQCiCfVBOcmm0HvI3afLLr_feJ9pprsuz83Mw7LY9nnin3kudb5Q5Y67owFYWYMy_OjPN76l8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر دریادار سیاری: دشمن می‌داند که اینجا موفق نخواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463414" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e94bb1174.mp4?token=VtrmiI-DJ2XLc9yJ99GcnmzBv1UyIPYgvijNl-IE6WA2uLcsg7drtUAgUktqf7GGHhHEhBuM3R77wzkAO5t1fiznDEraC_CC1RnMxL-m-GV9mz-TF0komHxr9ZQ1vwPka73Mwyz3s-qXc1sP6pFpOXnz-nYqKa58QOZi4ZPCh_anUG5sd20_E2O3H4wKYaGvYIvQgHcIzkkFfUKXvYzOBKqFpJGYkE95KyOuVjkaOdMkAxWVw6lAwd5gu8VH0t-xZMBngR1QhFVm80Q9jyafB4pKxAYJOUsbHOxheHaCxGLhTkmH9hGMl6b22VUgPKc57zW4Pbclzpe5M0fH_Z0m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e94bb1174.mp4?token=VtrmiI-DJ2XLc9yJ99GcnmzBv1UyIPYgvijNl-IE6WA2uLcsg7drtUAgUktqf7GGHhHEhBuM3R77wzkAO5t1fiznDEraC_CC1RnMxL-m-GV9mz-TF0komHxr9ZQ1vwPka73Mwyz3s-qXc1sP6pFpOXnz-nYqKa58QOZi4ZPCh_anUG5sd20_E2O3H4wKYaGvYIvQgHcIzkkFfUKXvYzOBKqFpJGYkE95KyOuVjkaOdMkAxWVw6lAwd5gu8VH0t-xZMBngR1QhFVm80Q9jyafB4pKxAYJOUsbHOxheHaCxGLhTkmH9hGMl6b22VUgPKc57zW4Pbclzpe5M0fH_Z0m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سخنگوی ستاد مردمی جان‌فدا از حضور داوطلبانۀ پیرزنی با واکر برای دفاع از وطنش
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/463413" target="_blank">📅 16:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7IUh-gBF5Z_XR_Fc386E9ZRiElDnQdmuzI_YWAFnXO7tW2NCr_GUdvmrgv85Eh4cRcCxM47ecwwbTiPyW3aNuWNhH7pdq69mj-J-oHdVBqdvZmRse7qJril9I0G0micgG4kRUrgvkHxYT5DoC1YU1z5LABgR0xeQ-vMUSe0c5eOaNjHUadLyzU1xFLo9OotgboXk2FJ7l0NCHzrKoUybLHGdYzZHnN2kyAdfUeKLKfbQsfPBGEM3IKJtJvB-tY0TrkeW31jIBOOm7kvHZQeRYgrjPBoDxvGFCayVbgUVELjGlybd-GfOIDvmrdptTVt54KBN6a2bSzhe59IMb6m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان فردا به نیویورک می‌رود
🔹
رئیس‌جمهور سه‌شنبه به‌منظور شرکت و سخنرانی در مجمع عمومی سازمان ملل، بدون تیم رسانه‌ای عازم آمریکا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/463412" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e80bff3f.mp4?token=IAn-O3Df1KxAu9jx_B6eLimQMhJqDii52adIfAX7iTZSqUUXQ2Uk8Mb0KqSFeg8260rIXbO7UQ82B8zWExnL_3Wxse4pwlUgv1EYvydQGzMlJpurxMrq8U29y_AeWJoIWrNjdpPTsTp9KUiMCzPGkqcCamiTQ339PJvAcGGN6F-NVbHnEnwmejWVL0VDIh2Yji6xQ3eQvvIOuiMhO8_TnOS_cfWdrEblK8vh8Q-MEoAxdDQ9fVE2mjojO0jDXtUQ4OTPwdEdCwfZaJpk6gF6QckMMZX-eDWZQLyW6oRcJob4g5eVT2FUXlr_TFVS4bS_dgDXuXtFTlkdssmvIqNKbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e80bff3f.mp4?token=IAn-O3Df1KxAu9jx_B6eLimQMhJqDii52adIfAX7iTZSqUUXQ2Uk8Mb0KqSFeg8260rIXbO7UQ82B8zWExnL_3Wxse4pwlUgv1EYvydQGzMlJpurxMrq8U29y_AeWJoIWrNjdpPTsTp9KUiMCzPGkqcCamiTQ339PJvAcGGN6F-NVbHnEnwmejWVL0VDIh2Yji6xQ3eQvvIOuiMhO8_TnOS_cfWdrEblK8vh8Q-MEoAxdDQ9fVE2mjojO0jDXtUQ4OTPwdEdCwfZaJpk6gF6QckMMZX-eDWZQLyW6oRcJob4g5eVT2FUXlr_TFVS4bS_dgDXuXtFTlkdssmvIqNKbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ رهگیری و انهدام پهپاد MQ-1 ارتش تروریستی آمریکا در صبح امروز توسط آتش سامانهٔ نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکهٔ یکپارچه پدافند هوایی کشور در آسمان  تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/463411" target="_blank">📅 16:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8rNjnGuh2PkPFWaNwD2-BPBshIoYlVHt0--y3QBBd9Pr9Z8rSr1eRiY53O-QAEKAG6J-2dYumBcDa4SIukHFsRoWYbzjqPQNGNiEQcEpHxZa-9yQ63N2T9n6ilY0LbkQwn9ChrvwPYmM0zlEj0MpQjjHHq0-KpTqz5-q5o-HgjauGH2JZrHjW2nSr-Yi-gRhgWGK_SeK735nCfSunWxPzihb85BreIQZzsNGiV8DhkW4njIBw7EdmudHAIszVza56KsTTCPrMGfCrghDtFmEDWxffyECin1DvWU1aJeL9mVTWGtH0V6tl8I01MXCg8u7lU55A3Wp33RXhRDiu4smA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۸ سکۀ متعلق به دوره اشکانیان در دورود
🔹
فرمانده انتظامی لرستان: در بازرسی یک خودرو، ۴۸ قطعه سکۀ تاریخی کشف و ۳ نفر دراین‌رابطه دستگیر و برای سیر مراحل قانونی به مراجع قضایی معرفی شدند.
🔹
بر اساس نظر کارشناسان میراث‌فرهنگی، اشیای کشف‌شده دارای ارزش و قدمت تاریخی بوده و برخی از این آثار مربوط به دوره اشکانیان اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/463409" target="_blank">📅 16:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سقوط قیمت نفت هم‌زمان با سفر میانجی به تهران
🔹
هم‌زمان با سفر وزیر کشور پاکستان به ایران، روند ریزشی قیمت نفت شدت گرفت.
🔹
پیش‌تر هم، سفر میانجی‌های مختلف به تهران زمینه ریزش قیمت نفت را فراهم کرده بود اما هیچ پیشرفت قابل ملاحظه‌ای در پرونده مذاکره اتفاق نیفتاد.
🔹
هم‌اکنون قیمت نفت در معاملات اخیر حدود ۳ درصد کاهش یافته و بهای نفت خام برنت به حدود ۱۰۰ دلار در هر بشکه و نفت خام آمریکا به حدود ۹۷ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/463408" target="_blank">📅 16:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl_YyUv0Qz05rcB9JLtviJId_59L-9Dhche7hAEc0BzRRwt7Ai27ltzK5VKVDElNX3_zzxzpUe7CKgeGGMmTR-45o03zeJwJYs1xX9yGEasxGBO4cyNZqXaql6FjDTFDQYn4V2jpopGq4gCmcUYz-sdV_cbeNvtvV_LNsdcWDviZYRh4w8rEJLGY7xmUVpHJueqoOxzJ9lbE_FZjVd42wxK5omMWqYdVXQo4-RxJ0kXX972_J8ruSjf9CeF7Cb1vwsXewmTZrMIaaBsT8rpWrLwMAoQM-oDhSu4Bc_UG2MM0wzjeeb7xLjaGZf6wCUa6mrDGKtEh_fLU5U3iaYHJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هدفمندسازی یارانه‌ها: یارانه نقدی شهریور دهک‌های چهارم تا نهم واریز شد
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/463407" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PygJ_-KUt6O5iDNPhkxBgOnIx6VkEtsX1A8HYuinMttVWD6SvVThMtwfQCYnOKtwUopw55EKBkh0ob-jzjK0etbd_RXwhd6HVY4oSxtycJgCK9hVVajVcnI12MWBquTs2xFvw-YRSH8XMfpayPaOo0xcllTiFS5ZNWN5Qya3J23NFYg0Y4Rxk8zCuoaGn3SeISGKD_A9-ke3fdkUDzwPlPCDxDIkWVvC8R74DZKDjaoEf3RntanUO-odwOXPmwVTLg_Hdy6qlaeFgHq-8VSX3DZUMwDAzLP5c6XpLTsXvI78TESVw5CAuCdlyPu3NEPEgzeDq9FW25XhKYGWp642ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7HkjfeBuA1UeTwq5TeWjsTYC9QhtA2lmGBdLgDMFt7p_w8V4XQBrILntsUUN7KXBBotRXOyiIT1QwslfVHyh_zvGf_eKgpZya_SHMzeps0JffTwr9BYhuZIKk7Hmn-tphFpqZ3r4sPVYB9WJHCnglRjXAgkHAxbK_HXeI0XMOpV9kK4kS4cA85h9aDIxEVndNy1gQgs1Eml9NlVKhw8sawqy4DQoIkwsRahWC5onPXD0z1tQBab4HIL61JizFRBGrmXy9hqtkGxJv4z1NwkDRef921obJ2ppOUtJNqtSIFbW7JZMwoD1x6SHjqS63xjXiCclficAK5n8LwEETdgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7baLZKXNr2ccCM2w14HDNSmlSh-v7pupu-8Kw9Oz1qj3GPEWoYirHffAinRtRRBktqc_6Yfb0p3ij76BNe5_1tr-FAy3rBZpPnnWPaImUWWVpBVmlvMswLRCEZz58Qeo2YoUR8M3bRhmS8VrLfLHqLqVWAPHECFnktO1fi0t-mwLTuqc8W1NjOZSSvYUrrZOmp7lHmUSinDQX31ehofiWsDxS5TbuKz3vwLXZ__LY1xVNQ9qM5kvLqZDcZlAkODuXQICpj8Mvq7aCRhh9nl5g0jw7yo0NOYnZZjUjKq8NK6bWAzMse3Fo_G_t2A6VDACccHzntMq8T5JvuyRTAEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/einp8Q5Jd7H8pEIQ4BWhwQYM7WaLOsX7rpkhnyv30GkadVzJcc_Nrw5A86WLkfrVxzxU1WURh1rCPjgW-M4yvpAMRwk5BfJs8OlhI2YMvhnmNXg5Xzrya93eKdX-lB9OxhbwlPpURCLuykWaIKhoEgkte3GpXeXjh7DvETRKmWOrFLoCpEdclRoUAs-771T_cRekd3Rb5FCBacBGXgGnka6cV468uM4JLhAp1jxc3b780xBEaCZ8ZdwMitbe6gwKU8mvuUf9m5-1TmTea1AjAGBEP_omMx7Eo6c3HhmwrI9hpMjzNvQbv-fMvAGfswl12b8PQ83Fkopw0QYwCbntPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6BMsI5MjKgE05re7Dz5GpDn9KHE8eWlqT4vI7-PI0JF0QzdW7KIeMlCQavdkg0FeLQy9sCpxbD7ygwpxJ7Dfm1yb7zvL8YVYTy11usaK-J8n3MJRjp3FNVGQMTUZuvBXZ0vhQxULelySHm0kkUB_GZ5cKchv603CB2gp-fgb5GcTfBFl2j_hddNdLh7VlnAFJQrlUF4aPcubCCHP2qo8Y29YKq9g-IPWDhP7f2MMWbDx5X-dQxJvgpY4aYPxJycXIXtVEMvefut0Pexzj1Dic0HMZdTBFnbqVTqMWKV3amwebaFU8b8kGcxOK3EqLyXovUAfeJ2uoq2Tg5Wjq562Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErTnCvtytA0NwracmJo_8LExwvhmrRLldSolqOGemfvM6t79a_VO0WO7eso_Nnf3MKb7noLiGGGz1YB0vPOej3tUbZbdvykp2EXj2Xj9Z_WtgGNmtamZirOG0rwb0JC4rO7Xd10YmRgBtfBmKIvZ6afiWsIboB_ylOq-r5DET9x9p7qhtfZydu-OVyHpW5R9w5dmuZmBrEaLCpmzYhm2BQ8cq6-dN6qfBcnF2iU7z3ju2Umdc5SJmGSNKKX_VieD75s9kO0bg_gIJY5X3QFot5lU1PmTqYqUZhIMrDeUx5EzPij4KO8-eq5z2o63mPXRPWJrcIpj2IiyWEj0mLou4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbJgDlF1Wb3mnnQIW-WnKj7OJ37jtlsZ6uuvF3BmOKCogo1vYL-9MbHo4NhXRKSqC0IlQyn5WSFkDuZMQM2WizVjNlrkR59S61GRS3wWJZjiznzeHh-PcSCk9jqg8oRjW29zb9C4-TN9U2fo4Vq22Bx5tVobn15mH2T4mO0NBea2xIg2FmvygIyxFdAAn-49Z_CHW8E4yxUhARu5wFzzfn4dAmX4tJUD4MqWl7MkAfK0quFpN9qzyZJPbWlGscc7NI1KctLd38pFnEabPgQMUEsLMi42kVJma05y7kgrVAhLkXPkzoRIJexlm2-tC2H0rZUsQlJnz4t-WNG6T5VI-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان امروز هم‌کلاسی و معلم دانش‌آموزان شد
🔹
رئیس‌جمهور: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد.
🔹
فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود. به‌دنبال…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/463400" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a465c69810.mp4?token=RlEnTd06fhSPEfwC7b0hdeY2zqg9ZsZ3enIIfAJA1YNnY9x0AhkGf3NxgGQFWc3N2SVQ-AnSNY8iYOAPDuceHVDCF1B6Gc-4EaCiA71PwbxWsfNgTrhODKPTBlVPsJVh1nY25-gIWUom4kcABbm2YV-huuIJ-_cQiTVLvJDk4h919BGWDJLjI4X4gwx-g5jNBnAJ5rgsugVwBAu2m5oKV9SmP1SiVRJaH8bq5X1V3-4cYWkztElv00IS6KKcR4d2LgaUBTNmNdH4qTcLcxJ4rHyZFaE3DJsh3n6l8zHA_J2r5qFAPDwe3GGzld38m01RCcv-QfjnbMcTBGxJLfwUfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a465c69810.mp4?token=RlEnTd06fhSPEfwC7b0hdeY2zqg9ZsZ3enIIfAJA1YNnY9x0AhkGf3NxgGQFWc3N2SVQ-AnSNY8iYOAPDuceHVDCF1B6Gc-4EaCiA71PwbxWsfNgTrhODKPTBlVPsJVh1nY25-gIWUom4kcABbm2YV-huuIJ-_cQiTVLvJDk4h919BGWDJLjI4X4gwx-g5jNBnAJ5rgsugVwBAu2m5oKV9SmP1SiVRJaH8bq5X1V3-4cYWkztElv00IS6KKcR4d2LgaUBTNmNdH4qTcLcxJ4rHyZFaE3DJsh3n6l8zHA_J2r5qFAPDwe3GGzld38m01RCcv-QfjnbMcTBGxJLfwUfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان امروز هم‌کلاسی و معلم دانش‌آموزان شد
🔹
رئیس‌جمهور: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد.
🔹
فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود. به‌دنبال…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/463399" target="_blank">📅 15:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استانداری هرمزگان خبر غیرحضوری‌شدن مدارس استان برای دو ماه آینده را تکذیب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/463398" target="_blank">📅 15:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21b2c97f9.mp4?token=sFLKviVI_B2u59Rp0NYcM-frvlUoQpwIxihSbB5J0DrVnmGd0qBc-nthUvGh95iV59SHsJKf9UhZyKLarxw7sW26yVQUF8tiIefL2UGznGtUkA02bfXMR3Ls52LFEso32PKMyQUHSG6cQd52Rk1UhxHgamaItbWQ4wv4WhEEiXjT6DZC2HHJYfrJJda0brr5kp4wy0RXyz6kQuPAN9zodqtJtWHs4WIBBdOqo0VFBc84g5q0TbVliO5qTn-D-T9-FYe6fFnWvtlOVycUIk_bjOz9yJX2COmCuoaPBlKd_8SAl91i_AiWBprH6Xi4L1qJNDzrqK2gG1O_AU-AyQh2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21b2c97f9.mp4?token=sFLKviVI_B2u59Rp0NYcM-frvlUoQpwIxihSbB5J0DrVnmGd0qBc-nthUvGh95iV59SHsJKf9UhZyKLarxw7sW26yVQUF8tiIefL2UGznGtUkA02bfXMR3Ls52LFEso32PKMyQUHSG6cQd52Rk1UhxHgamaItbWQ4wv4WhEEiXjT6DZC2HHJYfrJJda0brr5kp4wy0RXyz6kQuPAN9zodqtJtWHs4WIBBdOqo0VFBc84g5q0TbVliO5qTn-D-T9-FYe6fFnWvtlOVycUIk_bjOz9yJX2COmCuoaPBlKd_8SAl91i_AiWBprH6Xi4L1qJNDzrqK2gG1O_AU-AyQh2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی سپاه: اگر تهاجم جدیدی صورت بگیرد، قطعاً سلاح و جغرافیای جنگ را تغییر خواهیم داد
🔹
اگر تهاجم جدیدی صورت بگیرد قطعاً تغییرات قابل‌توجهی در دفاع ما و هجوم متقابل ما وجود خواهد داشت.
🔹
آن تغییرات، تغییر در جغرافیای جنگ، تغییر در سلاح‌ها و تجهیزات جنگی…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/463397" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/463396" target="_blank">📅 15:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463395">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی قوه قضاییه: آمریکا به ۷۶۰ قایق در هرمزگان خسارت زد؛ پیگیر شکایت صیادان هستیم
🔹
کاظمی، سخنگوی قوه قضاییه: در جریان جنایات دشمن متجاوز، ۱۲ نفر از صیادان هرمزگانی به شهادت رسیده و ۷ نفر نیز مجروح شده اند.
🔹
این صیادان هم‌اکنون با مشکلات عدیده‌ای روبرو شده‌اند که مسئولان محلی و ملی در حال تلاش برای کمک به حل آن هستند.
🔹
دادگستری هرمزگان در این زمینه اقدامات لازم برای ثبت و پیگیری شکایات را انجام داده است و وکلا و کارشناسان نیز کارشناسی‌های لازم را به اتمام رسانده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/463395" target="_blank">📅 15:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463394">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
در حملۀ پهپادی نیروهای مسلح یمن ۵ نظامی نیروهای زمینی عربستان کشته شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463394" target="_blank">📅 15:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463393">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5df56c00e.mp4?token=qQWbedA7jGaZEOWuwub2-COqrjTaMscaFlDxN-Sef5f20dK_MgnNx5WsFUvSCPWxnyEbfhsLOuRGYSbNcfOShkCZrkjLSHaIb8QrsgyJrCJk1sxUXy7Jc-e7M78ib9imvHgOE0t0ojZuPNrzbIyGvqMINWSR4VL1SR9rPpbk3au-H1_WCCAnBaLbbGF8XqyylOCp8NLOIU6vNEM-f1BoxFKqmjwgnx_tcu-DUTURK6MK2a6o1A5XjHPFydYQuYCxoekyA58-ckxVfLk0J2TP5IegEYSZUL2DleVP8ASijTM1pZ1AneTvwgsz6XYVaJ-f0pzcJu_jnMAjQnCkbQ_0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5df56c00e.mp4?token=qQWbedA7jGaZEOWuwub2-COqrjTaMscaFlDxN-Sef5f20dK_MgnNx5WsFUvSCPWxnyEbfhsLOuRGYSbNcfOShkCZrkjLSHaIb8QrsgyJrCJk1sxUXy7Jc-e7M78ib9imvHgOE0t0ojZuPNrzbIyGvqMINWSR4VL1SR9rPpbk3au-H1_WCCAnBaLbbGF8XqyylOCp8NLOIU6vNEM-f1BoxFKqmjwgnx_tcu-DUTURK6MK2a6o1A5XjHPFydYQuYCxoekyA58-ckxVfLk0J2TP5IegEYSZUL2DleVP8ASijTM1pZ1AneTvwgsz6XYVaJ-f0pzcJu_jnMAjQnCkbQ_0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا پای صندوق رأی از گرانی و وضعیت بد اقتصادی می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/463393" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ab28dc44.mp4?token=ScezvvAkeL77yWfPMkPZWBF6vicBcva6VbIyg1-aYc8KS4MZg5YwaYM5HinoJPbxQwGq38pokVBLz_c8D-lBybA3X0n6_JW6991H1nPr0AklG02Kn7G0JKk7xlZg-fb9jFX-BvHekbSmSh9Wka86oN6XXcJV04UEQx30I118iWMtgU87z8CXzMVBwFplHcylmjCKSMikU2e9f1wr2wB-4OqX9JZnOdDQOjQoSspriPMAdvGOk56PbTyzGrXgDbsAvTDRmoe3z4XANd1AL-QUQKfuRtvhYRxVr62-c-_-4FSTMiOyzdb6GpClNBbheCrShmsIRrSYK97seF3yUOMLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ab28dc44.mp4?token=ScezvvAkeL77yWfPMkPZWBF6vicBcva6VbIyg1-aYc8KS4MZg5YwaYM5HinoJPbxQwGq38pokVBLz_c8D-lBybA3X0n6_JW6991H1nPr0AklG02Kn7G0JKk7xlZg-fb9jFX-BvHekbSmSh9Wka86oN6XXcJV04UEQx30I118iWMtgU87z8CXzMVBwFplHcylmjCKSMikU2e9f1wr2wB-4OqX9JZnOdDQOjQoSspriPMAdvGOk56PbTyzGrXgDbsAvTDRmoe3z4XANd1AL-QUQKfuRtvhYRxVr62-c-_-4FSTMiOyzdb6GpClNBbheCrShmsIRrSYK97seF3yUOMLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
رئیس‌جمهور در پیامی رحلت عالم ربانی و فقیه صمدانی حضرت آیت‌الله شبیری‌زنجانی را به محضر بقیه الله الاعظم(عج)، مقام معظم رهبری، مراجع عظام تقلید، بیت شریف آن عزیز، حوزه‌های علمیه، شاگردان، مقلدان و ملت…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/463392" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaqY9wGJqsO9fj67VLxvCV77yasjNaPUeGGlikYLGCARF1UvKDnmKF2ZnNXrTIEWqQ1TYL4Fggl6oAZyyweTiPlNllTqa4fKEv372TWCG-wisRjU1gT82MY4fHtplx1w6NuVXR10oFRFzTIMFKhhW5XopgnJg9juhsYxdcu5tjebpgcMzk-VODvVx3SLcjXq5WyqtFbM_7_ej7YV02cRBxyvPtKmpCRBloo7h5b8U6RpjJMrFk2X67gu1WzzoIyKn5-luDGqCcx8Y3spphAQSy4ynSpudQWSZQYNV_1riGm-d2o3CqpUKzSZOsQFxPdki9mq8FGMSYKYil_XYHVNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9a2VEBdrIFouBsKcTBuJmYLMvMAebjgQG4GT0bPEmeyFOrF2EWXanKEONkaluCSFXa0VAl_6QCvLRQ9E8di90wzKc7T7Ga74VtWED0gVBJEC6UJZHy3sInIh4LoIo3oq61qslrVdblxi1qLDEmJSDIeR8rEDaipJmqtml2osw2zsn9V5xn_d5Y_FFllwMCULbg8sC3PVFAGyMvON2z2NwDeGbVqENJILwGdgVFNDBTy4NNF_hzq7_90GT5lIj3SKCIpA-b-SC5ZlhIvgj_v8hkkodX593X83x8jNQlMC-MZFaO0Z7Ui664u_K2nF0F1HKfCQycKgF4t_qfP2YFhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tl6-MVFZRniMup4PQv9DlR64W0dDvN99O-95P_g4PFUMmnYHmFYvMWFm6umyrvZ3QtV1HX5jJDkuboUlLdwt9pTBsNh50IUrJ_SI76ofNExPruaP4lwHDaPPeB8Oq4N7X_vkDDJbTPyi0nmrSriXXVslbrB0uTMNKtLzyma20pFramhfbz1M0U6Sd_8F6P1WZ3JRnJTZDrzqnZQE7O6LGnHrZZB8OTgRhHqJWFFRZqghOGD_uuvP1ZZZUwtfbsFQEb0SHcbxNrcRDwRyX5K7Ejm4CrQoZI4WyHfUbZwIymlSrmlKQ_DoXWyZ_-jjANmZ6G_ZVkL48-wXZ5WEXCeX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNIEV6k7S-o9kEXflKgUzGvpccd44CGQFAM7HWqslfeXLxsnnZ2fzEM7fPFMYMcCJgATqEj-ItIddo33Iiosa4CtqMeN2d3L09vh07CIjbP_KoBOgyB_v9P-eciBA3a85TBbauaY4XAFJI_eqtawT6xxYWQk-Hq_PRCY2oKiJN2vG00NdQwFjI3OAwfZE-zI1dMUYF6OjBTDM2p3cpdoO67B_Y1ObCO0Qtp8Stv0TX17mFX7-raE3r5OCnW56Yjao8qJxLjjVDVt6YvSAoXKaDK7PAby2vWZL2UGMkBgDqjCs0O46hDxUZvGpa0-joZoIZBhNbyBh9tGg4H0iwYeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEbDYmNuRZFHzD4nxXiWCxvwCafnugUWR0E5PzObZ8dL_BhW2QoieBwE3azxZzv95rDL6ivqt39a9JIYHf94zPmI_Koqxmfzr82nx1XackbRxPJtqSD7u2zIuKbfBiAd872nJnrQEsFRU_LCapB241pk_mu-4KsnLf6aPKjLgtvdWqmvlUCWv9Yd4hZdsUByVaxKPhZNiXoCyBAX4bcaQJRlzvc_Zw9TPqLuael0UtOm1RsVDZ-a-FEmNHexxY44M0sx5mUuaVv4p0fKNt7rTjZKLMc4pYmLJspgksZWyym974KbS752zGuZcp1jcqW14j4TNoMGkGomofXupjFMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3juuWVVq3VPG2k8i0eDP761dHdlFbOcbXyJ-uIQ_bdXr1lpIg8EwrPDdtayrkjB8cjCBZkc8t60dYuDU0CiyeNTzWkqcFFnys8WcuIxSmehkNbdyDtNAYJ5epmMfRKP4r1v78G_nKFq7XP8IZIImKW_5Ab1VKSh9R3NLeagtZ6uwdhShtp5gsPa9iGBQUU8fi94gZnFHxT2dad6fX-uMb4PGtSCNsuoGI4ro27tPNWb-tWRAHL3_vamqIFksGwUSIMNvOfsK-Xe8tNjkFH9e2dt4NWtcMv9QbxrHSxVbgWVEHjkyQPUe2_T6UFhzC-rYfW56HAWzvcPVg_PbLJ9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaFYzUx54zr1Bbq1es545m0AyOoKwHyCQH5f_v08LJZ7XuYHgD3abF24GQMu6fKTNZ5NpK85A_CoSOXAA3k4ZQZbzlCBAX3Kl2pwNrD-n9GkwAy8eqKadYsAguULoyoNYjLOooz2FzawQeAQCzQynaB3Qvj_h64kOY1sUwUUa8-dyiDTaT4jWWnowEaFPmvKnSR8b49rFXcBmsqqMOJ2vnFCaJsrUNHfcG39meEnFUglpgSvW3j0f_wj6ggQ0nREJhBusQbMD3JYBrmLxo4UNKf39ZHa81KIQp9vJ6OMgFo4-Vg_Q1VJG_k9w56aRBQcepdid4g1d7Pwk1wFP43nMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن جوانه‌های ۱۴۰۵
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/463385" target="_blank">📅 14:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b04b9187.mp4?token=vnNIxCXnN8aNCp8iQkxDRj8Z3Rxz0D8u7EtWCf4teUmJT-iEvvy80_if1XatXbW5MjQII207rTxulLQbgpTy0u6TM-x5SJjY_hjbXT1ETCj0jgOAbv3f1o5dwejaZkdZwjyRegbg72dUaQkU6KkDP715nH6P1c2Nq3_y8M4WITiJe9p7FhCcCO05Z6swl-S-N2zXoPOW3q2TZFRDGW-sFq2Jt7figcf3PUotNxYB462cKserdV9dwTO3rIBOMYsosvlkvUH1wLN4tbuP6zm_u5xCEySMBODLIiWcbFCDXRvVK7dsV12Ds0UV83y9M3E8d72E46T4hAg8UtizoP3h0bquQn1XUttqqukGD-NZhjb1ZsZOyehvf-FHRR87db2O9D9ffyfpTl2ouv-IE_HYT_qrhD6DXeaQo2W18DJ73BRPce-jGANStpmra02Oh0E0E7GCv1WfokWqoP4VaxOrzkn7oYAgx36kR0cicqz8o7NSPzmAaOts-1qMAWH1i8Dzdrzqqmpe9je8xyjWYKLV3nwCGrer_7QcULiFtT7tQzwtbyJ4NOkDZsqvoudg2xm6ES3hgXhlBfRz4XbVRFDA8vXe-lIOqwW3xgztkG301Xg3NhJiijmSV2cqsqBg9GqIEo41PoLXW6pZxzqICRAkrUdyJavC11m1Rfi9YUPhmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b04b9187.mp4?token=vnNIxCXnN8aNCp8iQkxDRj8Z3Rxz0D8u7EtWCf4teUmJT-iEvvy80_if1XatXbW5MjQII207rTxulLQbgpTy0u6TM-x5SJjY_hjbXT1ETCj0jgOAbv3f1o5dwejaZkdZwjyRegbg72dUaQkU6KkDP715nH6P1c2Nq3_y8M4WITiJe9p7FhCcCO05Z6swl-S-N2zXoPOW3q2TZFRDGW-sFq2Jt7figcf3PUotNxYB462cKserdV9dwTO3rIBOMYsosvlkvUH1wLN4tbuP6zm_u5xCEySMBODLIiWcbFCDXRvVK7dsV12Ds0UV83y9M3E8d72E46T4hAg8UtizoP3h0bquQn1XUttqqukGD-NZhjb1ZsZOyehvf-FHRR87db2O9D9ffyfpTl2ouv-IE_HYT_qrhD6DXeaQo2W18DJ73BRPce-jGANStpmra02Oh0E0E7GCv1WfokWqoP4VaxOrzkn7oYAgx36kR0cicqz8o7NSPzmAaOts-1qMAWH1i8Dzdrzqqmpe9je8xyjWYKLV3nwCGrer_7QcULiFtT7tQzwtbyJ4NOkDZsqvoudg2xm6ES3hgXhlBfRz4XbVRFDA8vXe-lIOqwW3xgztkG301Xg3NhJiijmSV2cqsqBg9GqIEo41PoLXW6pZxzqICRAkrUdyJavC11m1Rfi9YUPhmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از دانش‌آموزانی که دیگر به کلاس برنگشتند
🔹
پزشکیان با حضور در کلاس درس، به تصاویر دانش‌آموزان شهید مدرسۀ میناب ادای احترام کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463384" target="_blank">📅 14:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lijoKQu54jtr0UCkpLb3-4BFuBvOWwG2OeLn6wozLE3y_gCo8X4B-2luHkND0e6A4wxkrt3rS_MTTMGPVIszYLHc1ER9YkhwMaFJBKpxpF0mcljL0Q5w4jEKg5EnGS43hHJBjUAa0ZfDYq7UdJKHjNsyPEcpunUyHXM0_UIb34ExCHgDYnQL4yh9QEK6WyoeQx0NWo8pbplYwOMF-KN8QgiQ7Z0I6glB4x4IKwax5wmG3ilwdfDOTrlb3dk-3OukvA7aMMo1QVjtp_S9-d7yio9hSH8j8dyxjd5qmeEIDDlKzbo7cf5h62XG4r-GlZm2QoB7MxB0GoydfYMPFgz8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ورود ۳ رسانهٔ بزرگ آمریکایی به کاخ سفید را ممنوع کرد!
🔹
با اعلام ترامپ، دسترسی «سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو» به کاخ سفید به‌دلیل آنچه «انتشار مداوم اخبار دروغین و سفارشی» خوانده شده، به‌طور کامل لغو شد. @Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/463383" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b390ee69.mp4?token=LqWyk-19KYh-RrDopnWRV3R2Xjzn46pNjDsckwhb4x1H2Kuvc9OpQ09G3BfxmpNN1iPCOh142aCdutbUjtoPruENK9sFFN5GuYhtKjfEanpL6ExTz6if5lQ2qjm1qmdvWMR7Y2M16sOL4cBqnZdIuF8g3aDv8ix-YQnd1rlLtYbOsuk_rNufQttBkKhdzhMECupObiBNBfVpqR8CVd67Ms_8xFEajfLFvqTcvqN2bh3zz6rXiAVNlJIiPolLPfugBNE9sajkZurfJVs7JJ0MGYMJ-BjCq9X2ETbLqElMpuVVXVRqUEgIbrV_twwqrqTw247fUBtTqHuP_jyURR7_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b390ee69.mp4?token=LqWyk-19KYh-RrDopnWRV3R2Xjzn46pNjDsckwhb4x1H2Kuvc9OpQ09G3BfxmpNN1iPCOh142aCdutbUjtoPruENK9sFFN5GuYhtKjfEanpL6ExTz6if5lQ2qjm1qmdvWMR7Y2M16sOL4cBqnZdIuF8g3aDv8ix-YQnd1rlLtYbOsuk_rNufQttBkKhdzhMECupObiBNBfVpqR8CVd67Ms_8xFEajfLFvqTcvqN2bh3zz6rXiAVNlJIiPolLPfugBNE9sajkZurfJVs7JJ0MGYMJ-BjCq9X2ETbLqElMpuVVXVRqUEgIbrV_twwqrqTw247fUBtTqHuP_jyURR7_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرخ نژاد:
پيشينه بانك ملت در ايفاى به موقع تعهدات، زمينه ساز اطمينان سرمايه گذاران به اولين صندوق ارزى كشور است
▫️
مديرعامل بانك ملت در آيين آغاز پذيره نويسى نخستین صندوق سرمايه گذارى ارزى کشور (مانا ملت):
🔹
در نخستين صندوق سرمایه گذاری ارزى كشور، بانك ملت مدير ثبت و مدير عمليات ارزى و همچنين ضامن نقدشوندگى است.
🔹
ارز منتخب صندوق دلار است كه واحدهاى آن به گونه اى در نظر گرفته شده تا با مقادير حداقلى نيز امكان سرمايه گذارى براى مردم وجود داشته باشد.
🔹
ساختار صندوق صدور و ابطالى است و سرمايه گذاران براى خريد و فروش نيازى به بازار ثانويه ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/463382" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWgCjJ5VwNgED4fjoQ0lgqSiRy1Fo2dBXQafdPVkD3Jodtxz7AT69shPcyEV65HNrGhy4zmXVuEplgqKrX5WmxEvxtnGY8fSbjGKZ7EtayOJ8SNOaJ_W6ycNrE3cTR2NFo-UIAXr_Ns4GbW7Md8vItI__lqrgfU0vkM9wQU68IQQ60a-ZtyVxWSylQOhhSSmHWtihpkt6xN1Y7XbIPAaeOwpFsN3uAqJAnpVM79nVwdvpG8dNUFkUvk84VJybXwI41sUTOe1i7-GoLMS6l6lZps43qe5KIs_oeEV-PUSvESi30onsajHOF0BSiO39kHaT3psfNu9PiFs8ijwrvXUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز جشنواره «مهر معلم» با تخفیف‌های ویژه بیمه معلم برای فرهنگیان
🔹
بیمه معلم در آستانه آغاز سال تحصیلی، طرح ویژه «مهر معلم» را با ارائه تخفیف‌های ویژه در رشته‌های بیمه بدنه خودرو، حوادث انفرادی و آتش‌سوزی منازل مسکونی برای فرهنگیان و خانواده بزرگ آموزش‌وپرورش اجرا می‌کند.
🔹
به گزارش روابط‌عمومی بیمه معلم، طرح «مهر معلم» از ۲۵ شهریور تا ۱۵ مهرماه ۱۴۰۵ اجرا می‌شود و فرهنگیان و مشمولان این طرح می‌توانند در این بازه زمانی از شرایط ویژه و تخفیف‌های در نظر گرفته‌شده در رشته‌های مختلف بیمه‌ای بهره‌مند شوند.
🔹
بر اساس این طرح، ۷۰ درصد تخفیف در بیمه بدنه خودرو، ۷۰ درصد تخفیف در بیمه حوادث انفرادی و ۵۰ درصد تخفیف در بیمه آتش‌سوزی منازل مسکونی به مشمولان ارائه می‌شود.
🔹
طرح «مهر معلم» با هدف توسعه خدمات بیمه‌ای ویژه فرهنگیان، افزایش دسترسی این قشر به پوشش‌های موردنیاز و ارائه خدمات با شرایط ویژه طراحی شده است؛ خدمتی که تلاش دارد بخشی از نیازهای بیمه‌ای فرهنگیان و خانواده‌های آنان را در قالب یک طرح اختصاصی پاسخ دهد.
🔹
در این طرح، اعضای خانواده بزرگ آموزش‌وپرورش نیز می‌توانند از مزایای در نظر گرفته‌شده بهره‌مند شوند. متقاضیان برای اطلاع از شرایط و ضوابط طرح، مدارک موردنیاز، افراد مشمول و نحوه اعمال تخفیف‌ها می‌توانند به شعب و نمایندگی‌های شرکت بیمه معلم در سراسر کشور مراجعه کنند.
#بیمه_معلم
#آموزش_و_پرورش
#جشنواره_مهر_معلم
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/463381" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/463380" target="_blank">📅 14:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSfyEP3mR5EUi3IPGqLe7hlsu4gz8Mh1TNXXEOoSFPTK8QkjRDwOF0IDXP0szNzXdANp62bclTG2LxMvRE1t6-Ln4iG06NiAw6rRhGgDaw1jGEoZts6TD4uboYmrPDlDcMoQp1lDptiLEXeC4_JdH5QWpHXLcbOMZoRYzd6tEoF0hXyYMUJ7g0RiMfbqACF34aUk2MgW8ykQ1z3BOaTqXeJcprzGgR5nJky5a0m-r6RG29iZ0FUEzCNszhCBfgQAqDD4i9Ak6MWE7g9SLaeuI-_1jGF-8f4eYxZADkxd5_xKJNNMfFMshbNrV2ZxjUwiRtvYCx2VkX59LW-JoAM4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/463379" target="_blank">📅 14:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsMqM1-c-WgogWt4exYUMRrP0v_oFLyJbst94ihoIcNCfV_opavi51wQHx_CdGpQU36JhP5kMp4Au8n-DMKruJD4lshmGjePFRMWP9t6jqsd0QMVbAFD_aHCSF0hcTRXu7HYQTNmnNnbX3jdldwmeRu7M5uX1iGwYSYNdebDdH3iIqEqm79HoZPD0ZlA5xy-UvLXF2iSyZ1Q2-mv8iCh0zF4jcdxYPPPX9hVJaXTAkUH22Mywqv2y_OWhQNuqOAlgURsI4Dy7mr8psikh25_ksASI_waowq6Xl1-xaRWEJgjMmHyY-tVvJcX7c88hAKIG4SQH8KsG7LFFgoN9_hltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز زبان فرانسه یا محل اجرای پروژه‌های ضدایرانی!
🔹
مرکز زبان فرانسه تهران موسوم به CLF که امروز با دستور قضایی دادستانی تهران پلمب شده، مرکزی وابسته به ساختار فرهنگی فرانسه است که مدعی‌ست در تهران در حوزه آموزش زبان فرانسه، برگزاری آزمون‌های رسمی TCF و DELF/DALF، تربیت مدرس و ارائه خدمات مرتبط با تحصیل در فرانسه فعالیت می‌کند.
🔹
این مرکز در مرکز تهران و در محدوده‌ای نزدیک به دانشگاه‌های مهم کشور مانند دانشگاه تهران و امیرکبیر مستقر است و سالانه تعداد زیادی زبان‌آموز را پذیرش کرده است.
🔹
دادستانی تهران در اطلاعیه پلمب، CLF اعلام کرده که این مرکز از پوشش آموزش زبان برای «شناسایی، شبکه‌سازی و تسهیل خروج نخبگان از کشور» استفاده کرده است.
🔹
دادستانی تهران همچنین تاکید کرده که این مرکز از عنوان زبان‌آموزی برای اجرای پروژه‌های ضد فرهنگ ایرانی – اسلامی و بر خلاف امنیت ملی سوءاستفاده نموده و اقدام به شناسایی، شبکه‌سازی و تسهیل خروج نخبگان از کشور می‌کرده است.
🔹
فرانسه در سال‌های اخیر در چارچوب سیاست فشار غرب علیه جمهوری اسلامی ایران، مجموعه‌ای از اقدامات خصمانه علیه ایران را دنبال کرده است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/463378" target="_blank">📅 14:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCghkIO3VospfVII-ynp0ao3h6QBdzu3uXrpWoY-SBzy7l-RQOwjHsjHkxvAWEifpWrXqPBw4F6ZWGIooRSerju1DNB9nAoNLBKqQqsVk3c4vHiEA6x6vIZHJAuxLY2gp57c2Gx5Un30ZCAn7ZSxcOnk_vLclBFKrPWJEB9bOnH21lYqlUvuocPitKPWM56wMNXdePSoeMHTdvvydJoS5kSJFHTZ8-_DaXFqMqfwKcLvOYm8YL-8_A-jEPVdVVMXKKcH2Q5PS1sYlsghvVgKNAip4ZV8DYEUhwQgUke2AOBxelaxpD4pe548CTBP0B-dz635AKziY_254QdjVcxvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه رحلت آیت‌الله سیدموسی شبیری‌زنجانی را تسلیت گفت
🔹
سرلشکر وحیدی در پیامی به‌مناسبت ارتحال آیت‌الله شبیری‌زنجانی نوشت: رحلت جانسوز مرجع عالی‌قدر جهان تشیع، فقیه اهل‌بیت عصمت و طهارت، حضرت آیت‌الله‌العظمی آقای حاج سیدموسی شبیری‌زنجانی(قدس سره…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/463377" target="_blank">📅 14:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_l3uHug3JyxytvJi2RbZC914TpFCqNge8ciwsySubQ7R8EnMXPlmt99bukdGH5mSwkmU64XATUIc7_FliRyiYmbPZYVXwCpQpZPm7z7KHo0MHtQFqqGcJ9Lhzr5zDnA2qUissWfjwrnUwmH4ywURTvuTo7LEuW8AfrYZNAlcSK1KT7kLl_BBX96jtRkVT_lz7XX4fSnsZXAKzuoXSITSZa4XtQtB3oKG5ZQsDZYO3769yoCVodLR3_2Xa0Sqtp3DjJQyxydR5GJ3-NA3CqrUxsYn34-PurPYBR9QdWy6T6mnpfrB5rJ17N2LrLr0YoK_xYURah5XEd4lEh-UPwTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: ارائهٔ کالابرگ با مبالغ جدید به دهک‌های پایین از ۱۵ مهر آغاز می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/463376" target="_blank">📅 14:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqT1Z988ZQeDp40pC-jCs86SUAcTlgGM4O0Nd3qufgqej5BLACJdDm3RfbH8u8bjIe8zhgns7Yx01lT7RNTW0bf3K6kfq-0dNBjVmnYF41TX_PFnBVtf3r9RcrRJq-97f66asze6JP_pfMvdKJwamHbWNec8i-f3KV1OAG_fXxfaJLhWg97Lve-5S9DmxDXdKC24akAi8j6POZaR0Y19dUzOhUbLsKFCerqKgXw1UXe_yoMHem0gTaHvgXbia2IvSq87tGcRCteXJ46GCJGSE2QYrMQYdHBHgg3fmwPLPqj2-02zlOm5Uf_ahVUVODAt6VS0uCKP7PMzodoGO_F4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارشاد: ممکن است در صورت آماده‌شدن مقدمات، نمایشگاه کتاب به‌صورت حضوری در آبان برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/463375" target="_blank">📅 14:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وطن‌فروشی جدید سردار آزمون
🔹
در بحبوحۀ تنش‌های منطقه‌ای و همزمان با حملات نظامی آمریکا و رژیم صهیونیستی با همکاری امارات، سردار آزمون، مهاجم تیم ملی فوتبال ایران، با انتشار استوری‌هایی در صفحۀ شخصی خود جنجال‌آفرین شد.
🔹
این بازیکن که از ابتدای جنگ تاکنون…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/463374" target="_blank">📅 13:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09914fb83.mp4?token=HtU0yj9eys0w_-Q-1UqmkUp1fkUm8-8x6_OZQ_t2nyepCaeykuMAw28MdgqD5rAE6jHff4f0naH5NlMyVPBcLcWIwCcLXohX7II3ETQvwcaykDJm_lW0wVAQ4cT9FCS1WUIwPSLT3MNhf7XgXV8bAARnwiNpHNw820EMyuhXTNTzzMb0SxmafJk61BK6U5ESAmFNTPc9yKGsZ-e5CfHoJVtioPAbg4lbZY7K1biYAuis69-yrPLECwcGwRdL6lyA_0V-3hxeoxOPrPuuPYKSL1Q0xY76LR9WBGwVcgKftCAhM8j-_uzp9UdG4ooPrtkItx-EiYBN2AKbpwPyoZ_1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09914fb83.mp4?token=HtU0yj9eys0w_-Q-1UqmkUp1fkUm8-8x6_OZQ_t2nyepCaeykuMAw28MdgqD5rAE6jHff4f0naH5NlMyVPBcLcWIwCcLXohX7II3ETQvwcaykDJm_lW0wVAQ4cT9FCS1WUIwPSLT3MNhf7XgXV8bAARnwiNpHNw820EMyuhXTNTzzMb0SxmafJk61BK6U5ESAmFNTPc9yKGsZ-e5CfHoJVtioPAbg4lbZY7K1biYAuis69-yrPLECwcGwRdL6lyA_0V-3hxeoxOPrPuuPYKSL1Q0xY76LR9WBGwVcgKftCAhM8j-_uzp9UdG4ooPrtkItx-EiYBN2AKbpwPyoZ_1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهریۀ مدارس غیردولتی از ۲۸ تا ۲۲۳ میلیون
🔹
رئیس سازمان مدارس و مراکز غیردولتی آموزش‌وپرورش: شهریۀ مدارس غیردولتی در مقاطع مختلف تحصیلی از حدود ۲۸.۵ میلیون تومان آغاز می‌شود و در برخی مدارس شهر تهران به حداکثر ۲۲۳ میلیون تومان می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/463373" target="_blank">📅 13:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh9NXqsSDdePOxYWJqTkPMrWjdGPNLi2tC5yZeS-39XK-Qkrfcyx4GdkfE0UzjWPRjgHuTkLC_APIM45EcNQV-pDKqSL95M4Q3ku5sPX_SQuKJYnLHUuei9wvV5UW6rh3HUSyor8Wx4RoWVbWgF4tiTrIqPNrquZZdD7n9nTPLq7tawvCO6w901vckjfzJrvF8fGTrCthctKIX8FgYMIDQqpYMj2-wk6fyppCn8Q226Y-9ZpPeP0vhmU24gSjhysLtN_0c77LlFGFbRFcpyuMtCu1ieC3ZEGr_CAHzWdqMiSXPuvudeDYOsBUXFdQhq03L5oq1o1gPORfOopa6XIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سبحانی: آیت‌‌الله شبیری‌زنجانی در علوم اسلامی صاحب‌نظر و دارای مبانی استوار بود
🔹
آیت‌الله سبحانی در پیامی رحلت آیت‌الله سیدموسی شبیری‌زنجانی را تسلیت گفت و نوشت: آن عالم بزرگوار از ارکان حوزه‌های علمیه و در بسیاری از علوم اسلامی صاحب‌نظر و دارای…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463372" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjMgFFr2c8tKfc9wHStbVgT064ujbu3PzWqYuDAmX7ogVxLnIMv17r75mWX9h0ba-29PJB8N11t-1RInKCzjDptjTNYyv7lNrxN1WT5O5b6Q2C1IsFX5Mce0FkgqZAg5FOeJ4j7nHWyYclM-iu3oJtZIjhuxWVtXrAcaeUD70dxKB-KMOJjOWb09zr4BU7DqnzEDONL4KYlQznd2n3Ntgkf-R8QA07ej7hHuAv17nLfovpDG06hjsW94IiKRRFKq0hILLMDCzNS3VQ4bDDTbr7L_vFzAGTjiwRI1nMz85HXvAqJJEqdo_96xwuzdmlYyvbG1kHr8F6bWCKMs3HKrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفتکش در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس به‌نقل از مقامات نظامی گزارش کرد: یک تانکر در حال عبور از تنگهٔ هرمز توسط یک پرتابهٔ ناشناخته هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/463371" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s30SatuJY5c_gopbhr9sioowIcIR2IyBvsBO_D-MpDWxaGuRXbSlwMW38G1UK37dTC8zcLuX-sgCY5T0lezgIZHdM-4b4lOJ2cy7G03e7ICkhGineLRjh8uFEoduIRuC8uoITG1zc6ZjAJ3sD9xczWFvP7svtD0mpYaEaYLkj7yiNvgHNKYH4hhV6ZorV8F6l6smP6hPVkx7143K2pLl5sCbTzUHvvcO0UFlaM1zDTmE_n9htcAf0O6oweYXqwITuPdLQYZelqYVc2cZ6luGKL-SR_Uys23gx32uoDo_SR7Hc0vaY8JJglM0k-7sSoc6eIoQhbo9qilTVT9bWQqWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آیت‌الله سیستانی در پیامی رحلت آیت‌الله شبیری‌زنجانی را تسلیت گفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463370" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1aWo1SnSQYnsTEL8CWQfH0Te_PsR6aRxx9ysSan1JsK4wzDuTYRkscLPpSaqK4c7vJj4S3dwgeDwQ6rXq1VDhD6l-IQAxwdIYTslMeG_ONlTYfi9vojCeTFunqucwIxe3GZLWcuZl--Col6n3RR1NJsx4aKR4E0FGVLirgkmeSLlTh2fohsouY0t9_wZ32cJFbtZNjwH85DZm1GkO-W9lJh1oqmIiefzVzT6f4ezTyIu6BDw0qz3h_6eGoV2rhqTVH4qGanqHNNxy_eozFRM71U30GyrrQXNJ0kwqjONBUJkO4fRcU8Fup3RVGnWPnf2C_OWdfFkPK_OSvcLfGQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۱۲ هزار واحدی به ۷ میلیون و ۲۸۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/463369" target="_blank">📅 12:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgo2bg4DsluGxBldg2s42hdctgmcdgBCPn151Rv-w_psPRdJTkt42bniin7ayAyPHZs9Gtt7CtTLCWEWrnCoVMZq_KOANknnbf8G9i5EoQutO8RtHLyBM8Xz7koYbZiCmKq9eTWd_OdYg8wq5v2fyEH5lYCyrM9hKgdwEKU3xa6t_TX7KT1UYuzv5ajdyaLX8g24BbS2MwzFYaAaIpWClwOmYaNSrfd0b87Hb4BbNLuJqnOeMZJ0-vqKQsdQJCaZlomtuVYf76TBmYiZb-5GuHvEygTD1ukt0uTmKOYkBORsk4RO0JPbSnnJScC8dGN3qog1H8zRDAckjdqpsvwhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«به وقت ایران» ۱۷ میلیونی شد
🔹
برنامه تلویزیونی «به وقت ایران» حدود ۱۷ میلیون بازدید به خود اختصاص داده؛ این آمار با بررسی تلوبیون به‌دست آمده است.
🔹
«به وقت ایران» با اجرای سرباز روح‌الله رضوی و حضور وحید خضاب و نیما اکبرخانی به عنوان کارشناس، از جمله تولیداتی است که از آغاز جنگ تحمیلی سوم روی آنتن رفت.
🔹
این برنامه که به بررسی آخرین تحولات ایران و منطقه می‌پردازد،‌ پیش‌تر هم از جمله پربیننده‌ترین تولیدات صداوسیما بوده است. بر طبق نظرسنجی مرکز متا در تیر ۱۴۰۵، «به وقت ایران» در رتبه نخست پرمخاطب‌ترین تولیدات رسانه‌ای قرار داشت.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463368" target="_blank">📅 12:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzNiSJ660ZvDsMt4SONw-Xm0SUqZsbnwSASy6wQL6V_-8Yt2zPkSziJeTMvdoU7LFsrq-Mqmx7h6RTr6k-mJJqbp2MvDX8ymo7_Y0Qqxpr2iro_UWMyLQl8Eflv3IvY83L_rmSLsXmsvlT9wI53o0vbZOUuzp_dm7D0euW50EBZK9D6EFDRepc9PzMmgl6xCNciqzPDQjpjMCZhPSNVD5KizztJ9vFlJiKHnZhPBkvZITyjx5SO6AyPWDBGTTd7sIVA_3qEw0GoRFDMV7otAa6-emj-_6OIfl45USCim0MOXvSIWu_TM5vxjPto8aNGYWqhInJne5DMGX2N44itVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضاییه ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
اژه‌ای در پیام خود برای تسلیت ارتحال آیت‌الله شبیری‌زنجانی نوشت: ایشان از نگهبانان امانت‌دار میراث اصیل و عَریق تشیع و از استوانه‌های حوزه‌های علمیه و از برجستگان علمی و عملی مکتب نورانی فقه جعفری…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463366" target="_blank">📅 12:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انهدام مهمات عمل نکردۀ دشمن در ملارد
🔹
سپاه سیدالشهدا تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان ملارد امروز از ساعت ۱۲ الی ۱۷ صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای نگرانی برای شهروندان نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463365" target="_blank">📅 11:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE2u1Xtua2HkHyNVw5NJ77PBJ6rZvQZLcmjXrHRHqd9G4tOrE9lbjamXr01Q-6Exd6EDeYr0PpWb2_SyXxmxC6cX21j7I_aq8pdD3cqJbF4o-CeiaZN8XJhE2p0Jc64HXHoLJpZN60RHwyMKFXOjefmoJDmhUkyhhskkZ_9e19bgGz3VrWm2kqFQjn-Ch97DXoj9qUrwhP5HwSEZT8mVYboaoYAcix2YgSy5x-1UfotKwD0qWXKr2qvh-Zy2vJ8D2fvJGhB6yW7KrO2ZmeRRviv-ejw_butat0lKBH8YeiJo7qHCeVFb9gQub5l_Iwvki9OfgWFUYrjFbRkuZurTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463364" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ2dRWbUFlJ5jO203uYImFlhARoqNwv0Iam3s5ZUkN2_aZqkvJTN2qDblhV099tynBqs9-6oSaOe1TBciT-aN34S3f2SNQLxly-DGQMyZFn1kfvyc1F9261IykgIlDGAhGZ87IvOAPen62btOxkWuwqgsrZQJEuSJqcFry4gYpFIGxPeG-tXAduxNX5K9KTFkq8qvsoceDblM8qRh_vgtDlap40jr4Syx4ntR3_ZMMD-hSyds17SZLH3IhkwY0XCL8MVjLKgtFnO8MRrAWnALU26a-Brlh5O__KTykhimVNeZoWdLmXKN39q3G74tYxleAN47RpOyOouYvLhXTHjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح: طعم تلخ شکست‌های بیشتر را به دشمن می چشانیم
🔹
بیانیۀ ستادکل نیروهای مسلح و قرارگاه خاتم‌الانبیا به‌مناسبت هفتۀ دفاع مقدس: کشور با استفاده از تجارب ارزشمند هشت سال دفاع مقدس به‌سمت «ایران قوی» سوق داده شد و آمریکا و رژیم صهیونیستی، در جنگ دوازده…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463363" target="_blank">📅 11:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان به نیویورک می‌رود
🔹
رئیس‌جمهور در روزهای آتی به‌منظور شرکت در مجمع عمومی سازمان ملل عازم آمریکا می‌شود.
🔹
رئیس‌جمهور ضمن سخنرانی در مجمع ‌عمومی و اعلام مواضع کشورمان در خصوص مسائل جهانی و خصوصاً جنگ آمریکا و اسرائیل علیه ایران، با سران برخی کشورها…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463362" target="_blank">📅 11:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAtNwqoS9XdIsC_15eeNNMrHzPFNJ5KAXHii6sMWdCtR_VDv8FUQHPQTpzE3VDwLrKSPqpTC4XT6KcroItrYePM6Rjnmn5JwMo6MJ3dTGkQUe7WHeNapGQJ479r7nHzitwaJ7ra2TaumChKAHx5UN-uFJ3gN_-ggd_MR7JY-Ldb3yNaNAF6DpkJ81L9izr2A53mc7Vm0AIH6eHdljxKdKQ7M3Z1WiD8ZziN7lgJlfKe1Ed3--fmiMBBozskC41VywghkrmbimUZ2Y8zztyBLoeNN8IDAihQNv6qi0D4JlPv7j6tKkkhN1DLhdiW8vLVS-DRvLXKeR83ol_NLSm2nZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فقط نباید صدای مردم را بشنود؛ باید واقعاً به مردم گوش بدهد
🔹
«دولت شنوا» نگاهی متفاوت به رابطۀ دولت و جامعه و راه‌های ساختن حکمرانی بهتر در دنیای امروز است.
🔹
شنیدن، شروع فهمیدن است. اگر می‌خواهید نگاه متفاوتی به حکمرانی و رابطۀ دولت و جامعه داشته باشید،
دولت شنوا
را تهیه کنید.
راه‌های تهیۀ کتاب:
🔹
خریدآنلاین
اینجا
کلیک کنید
🔸
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
🔹
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🔸
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
🖼
انتشارات فارس مرکز جامع کتب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463361" target="_blank">📅 11:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463360">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دروس حوزۀ علمیۀ قم تعطیل شد
🔹
مرکز مدیریت حوزۀ علمیۀ قم: به‌مناسبت ارتحال ‌آیت‌الله شبیری‌زنجانی، دروس حوزۀ علمیه تا پایان هفته تعطیل است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463360" target="_blank">📅 10:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VG1ZYPO4MSKRrGumEbBnVXHhxY89ZkQnCerFJlchUANP3RgxcCVQ18mVQy-gkg2XWGAMXYB6uOpXzMOoCDJDZl3K_RRuTQUjnraY-p80NbrRh3rPaeyNeb6cBgc3T-GbmtDWsGMNTsF8GUiM-Qc_-pY9V9TRS2T7QBXIEj52zX-IyISo0WbnjglVe93O0AYzJYZWm7iOgl5dnrMPIaUZaRIrY2lV7z6HbQpjV4OUoHtAxx13k97FETMquFxFAEMyyonFgjr_FbtOoRPv51wT6Snbn1Pmc232E5ADxEXYz2J3LmVbH5ZWoFBJ0ePPCzXEAlQh9wiu3ekjDqpYOC2KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp7df8SmixqLvwQU21pCrhTSpsEXPIvz7fZ__rD8C9I8k2mFcSUmEpHAwFEL5UK9VU549o-s6CzaL4XvQOvHUCZ45b7lYAUsRM-6261vfWWTYsT4ZZEJstfDz6tKfCEF2KmdAnxltKisV-9K6VL5wZlpJ6rTZLJmT6OKhb53Dur3rM6n6Vo0_NYRRFv9e2SLJDJmXCUgBHdKcItgT9IfFKze8j0nVdFkUz-_IxHO2iIIXG_EPRg4yPTMBxR5uFePn5txS8i4HAu39jh85IhyiqC7BkYYZlWteiF1vkTqNTXEMZ3JbqDz6HZ2XZSV62-1LS07fGpYukKlHNm_-wNUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFHW8qZJ91W3eQ12iBAibsaeeGcKG1Do8VXfJT55Us1GxebypietvalijPNYhlDlm0vfIU5pkB3tFuyPj2O3vRkg1Kt2CMIy1_8OaidGCeYFsHl94OAPPlCdlAFxNsl3f8QsgTYZ4DzFNT4sqLvt3xwyb8ghSnK4nUHgbELpq7Ezk6UJBA2vsTdF44qezRf8Jg36xY9kl9wdIzFrJdCG5hoD7ZLDN7rox2QjmH4IiqeF1aEwNL6hl6XboDJgU44SoCpCAGCro4ISbXTRZW7aYxGsh0Pot0FyOSq-FK2RM_KyjdTd1Beh2QuIkj3nNUCTT449NBPbaGVSIZFSPtlklg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر پژوپارس قاچاقچی که با شلیک پلیس هم متوقف نشده بود!
🔹
رئیس پلیس پایتخت در محل نمایش کشفیات موادمخدر پلیس تهران به پژوپارسی اشاره کرد که با شلیک پلیس هم متوقف نشده بود.
🔹
سردار محمدیان دربارهٔ این خودروی حمل موادمخدر گفت: این خودرو که حامل موادمخدر بود حتی با شلیک پلیس به لاستیک‌ها هم متوقف نشد و راننده با رانندگی روی رینگ به حرکت خود ادامه داد تا وقتی که با شلیک پلیس به خود راننده متوقف و ۳ کیلو شیشه از این خودرو کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463357" target="_blank">📅 10:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیروهای مسلح: طعم تلخ شکست‌های بیشتر را به دشمن می چشانیم
🔹
بیانیۀ ستادکل نیروهای مسلح و قرارگاه خاتم‌الانبیا به‌مناسبت هفتۀ دفاع مقدس: کشور با استفاده از تجارب ارزشمند هشت سال دفاع مقدس به‌سمت «ایران قوی» سوق داده شد و آمریکا و رژیم صهیونیستی، در جنگ دوازده ‌روزۀ تحمیلی و جنگ رمضان، در برابر ملت مبعوث و فرزندان دلاور و شجاع آنان در نیروهای مسلح، زانو بزنند و سر تعظیم فرود آورند.
🔹
نیروهای مسلح، معادلات امنیتی را به نفع امت اسلامی و ملت شریف ایران تغییر داده‌اند که نمونۀ بارز آن، به‌دست گرفتن مدیریت تنگه هرمز با ترتیبات ایرانی، فروریختن هیمنۀ پوشالی ارتش روبه زوال، هالیوودی و تروریستی آمریکای جنایتکار، و ذلیل کردن ارتش کودک‌کش صهیونیستی است.
🔹
نیروهای مسلح در برابر دشمن کوتاه نخواهند آمد و طعم تلخ شکست‌های بیشتر را بر متجاوزان و بدخواهان ملت ایران، به‌ویژه دشمنان آمریکایی، صهیونیستی و هم‌پیمانان آن‌ها، خواهند چشاند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463356" target="_blank">📅 10:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14286db87.mp4?token=K-kbigXmRq44m_wcmR-7ienmG0Rl8cB5CwSQWSNNEFaCXPFeVhA2gPyCu8-W8-Y2onLxHQvkqD7ysHpUO96mhJoMsVoMXlePGZmr3-w-gAcpD3smq8xR7rCmLb9VN_jaFU9ulXaDG4iFR-4XnZILCPCPmHjQdY05iOiAg67ioapftR1UnZoGoAmn3xhVmR21zDMC1OzUtYAAYbH2batX3sjoSzIDrHbnlEMnwc8wJqF-AH2Kh821cw7N9hq1CSpTbQXcmANWw9GUUYkV2hXTeSyh9YuVmLZ5FINjYRoN43psC9j9hwbZSvo2cai2Xxk_ysA63rQskv9Qerhn5dv7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14286db87.mp4?token=K-kbigXmRq44m_wcmR-7ienmG0Rl8cB5CwSQWSNNEFaCXPFeVhA2gPyCu8-W8-Y2onLxHQvkqD7ysHpUO96mhJoMsVoMXlePGZmr3-w-gAcpD3smq8xR7rCmLb9VN_jaFU9ulXaDG4iFR-4XnZILCPCPmHjQdY05iOiAg67ioapftR1UnZoGoAmn3xhVmR21zDMC1OzUtYAAYbH2batX3sjoSzIDrHbnlEMnwc8wJqF-AH2Kh821cw7N9hq1CSpTbQXcmANWw9GUUYkV2hXTeSyh9YuVmLZ5FINjYRoN43psC9j9hwbZSvo2cai2Xxk_ysA63rQskv9Qerhn5dv7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زن ایرانی کافه‌نشین است یا میدان‌دار؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/463355" target="_blank">📅 10:29 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
