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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-667888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی   #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/667888" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdEW1muYEdQpqbGndjYXTFdbG9HAL6cv-OhWd40yWEOtQEgAHptTt7dwQuhujGuGzBXBGrzjnz-8nt1WEAipSVfmikFtlj3gBNDabgHFUCVY3XMrrTJpGXetYFIt_5QMjT4LKtkhlihl8boQYBMR20QHpDRgidxk5w38IeDUgYk3k66BD3AJFCpd9jGtqa4E3A02bDunlFjXxW8IyWPyzeU3CeCB--WbwEfD7GxZT9Z-PV8cSyylynnS48wCWi0O6O_TYAAej-o3FWDq96l3ikR5b1ELiNois4QohcaNC1Dz1Sz2NCcb7YhdrtF2ouNNJ_CDpZc7J6gs9laALGAegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzn7UJe2iT-VqyCBUwuNZWjRpRCjI03BL9FGNJGFVK2DdICw1E9smUQiow7K7rJlGEB2Z6AZSzort77rKG9MYK6BCXsrpCcjVaDgHUysSxCbNvGmZwC0gBdrXiHNHWAhUmztn5SxwupRWHbbU5Jt7cuRbNRGk55efO6sXbWc10FKFJb1O5v5jR5_2A28XtufPxk8jyUeHuFSKJehiWX-WRafVF2-O-RX2KnTR0jzd_fwCNYuB98RRsPMs9AQ0u1wm73cqwv7EnbAsraWcwluj9lSdDn1u8PxPGfEVWGTEf1DLekwS_iOrSvVTdvWGaLO6EznRncUdI8i60B1a1eWvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز حرکت کاروان‌های پیاده‌روی اربعین از رأس‌البیشه؛ جنوبی‌ترین نقطه عراق به مقصد کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/667884" target="_blank">📅 14:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه: در ترکیه خواستار تعقیب قاتلان رهبر شهید هستند
حامد خسروشاهی، کارشناس مسائل منطقه:
🔹
شهادت رهبر انقلاب، در ترکیه بازتاب وسیعی داشت و هیمنه ابرقدرتی آمریکا و اسرائیل در ذهن ترک‌ها فرو ریخت و ترک‌ها معتقدند امام شهیدمان با زیرکی توانست موضوع موشکی را به پیشران نظامی و سپاهیان تبدیل کند.
🔹
ترکیه یکی از شرکای راهبردی پروژه اف‌۳۵ بود اما پس از جنگ اخیر پایگاه مردمی خود را به سمت پروژه‌های موشکی و پهپادی بومی سوق داد و خود را مدیون رهبر شهیدمان می‌دانند.
🔹
در ترکیه احزاب اسلامی بیانیه داده‌اند که نباید اجازه داد قاتل رهبر شهیدمان با حاشیه امن به کشورهای اسلامی سفر کند و نباید این جنایت عادی‌سازی شود.
🔹
رهبری تأکید کردند که باید پرونده شهادت امام شهیدمان را در مجامع بین‌المللی و دادگاه‌ها پیگیری کرد و از اهمال در این زمینه در گذشته انتقاد کردند.
🔹
رأی دیوان بین‌المللی لاهه باعث شده نتانیاهو از سفر به کشورهای اروپایی حذر کند که این اتفاق باید برای سران آمریکا نیز بیفتد، هرچند امید کمی هست اما باید پیگیری حقوقی ادامه یابد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667883" target="_blank">📅 14:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667878">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNDsn4NIhLZBr8GmEEKcXxnHqLQTyGfKlOQHMzs8KwQLgkP2b6jIKr7cOAA8tLO7VH6sCmcA10bCg5FdaokvzUOaqsR5Q8KPjhPTb_oamMH62GmsxNadfBKwDUAa3dQw7idE9v081uHQbgf_nC-MOc_VRdGiupRND_TE7mt_Q3GqeyLiS0PmR46Ed-6_1MZeWG7Nbzc535-hH25eI9gyqlY-hHWTmZGWvCD2QSv-YpUafk621Qn7jfA_Tt0cGpPaklkAfckAIsDOurPQEYkCMxPz9slcPEYrc4NJnHAvRiSn1bD0_sJhgbSx9T8QgSwFsenBDVIodGPsed3BBnIglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htkXCYWXljam3yc8iXH_zOx4FH-xYW1_q36-cYUcUSvn7arPXBqnj--r8jW-T5_89p9c5-S3HfIv9RUk9g0h8HWdijx6-y1qsUB9-QDCnP49PsxLbxoMvXRr8iDYlr6r0qVooRXlCZ1p3Nm1Y2oJYymLzLgknwF2xACteniTYpkNvH76SJdMy2zp3JZpfrpoaucwU1RZ6ckHFqAybfVlQd-_jEMJfbdgLSh8qMUlCZ29eq5zuxXO4dSgLmdU1UEUbYac7Hde8qECHU3-SnQCZPRnYaHDB8v9UXkY9rVnk_MwFTeYnxGXoPh5IGs3fZdBU6Z94Rr_eMzSv08P88InjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYsOwX6yc7-9QWOKqKo8xTJf-_hmUNXBJ6GlfFMFZz0I3ZkjBGSVZNQ-UHWRixFGmui1ziOmyYfpZ7pu05mMM6O1AUCstPkOe3B4HNTmuzsaRYsIZosVmnkIuUCJH1oInslN2MRTdoWEm8scAfsxZfv0FNnt7gC5KK9td3BY1GvGMZntX2yMHFhJn0Gxk1f50bBCU83rSdGr_UWY7FEPdsU-DOFqukLt1O_Fqh6RrzugRRkQldWftqtWdSKA29UQT_0KQve8QcqmISMIf3l3iALw1ss3cz166df14yMB-jcHApORaUI0vRG38R90zcPVPfgzruIYcUVtTnBk2oQ7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j37H85Fo-ZydDNeAl_Kgqn0Ci1eaCiRGGmdMKSzfyJnwqWXd-XPweoH5xyq9-y6_466uq58RSBSg2znp-oPildqrInV6Jc2NYTKuWm3nQ_icSTB00yk1dx9QU8DWZ4OiegIO8yEHPwJwvjZDUb1duv62yOWGC5KNn1t4oucP4NluZuOh0rynqCQumXvY3-n5PQCBN5VgPrr7QBX_ufz-5yQJ0l0YbxDp4maTViXimtpwQHcloDBjej-h9xcsLCuFChj62dQ3YiXEFuq3r5vwlDY2AjQEvph9zQutsCJ7wp_nPe6HP6HXtOR7ivpeYUn_HqnosK8ZgTgn82TS97M8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP_9gj3a5jYjXFxfWKvYTlu6uy33cYON95YlRZKO34iEKFVKSLplgWu4C63KWIqPIHadOvhVz_h5QM2vk7P8TcUWF--WSKlojILx4EpSpsg4IPtFS0GansqNljn9MX74LrzsYP-FvJ-_ERzjrh-3-Xq865oM4f0UFd4AtQEUodrdQOZHbyxWfZdCVwep1ZWn48wrMlVHBOuHoyZklLRlRQcZSmb1ZZ4UNvuNMnsuxENo5lW4ImvxB5nqKbNJeCJNnwSn3McvgwCUHu3EvZG7oSqAvdxJX4q_3e7sPC5btuYM3gE59VeUbi0jqMWqZ6EfplEOQcSKaDmRt4ZZSkEAuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلسکوپ جیمز وب در چهار سالگی خود تصاویری حیرت‌انگیز از کهکشان قنطورس ای ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667878" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667877">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667877" target="_blank">📅 14:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667876">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین‌الحرمین: حال‌وهوای شهر کربلا، آماده مراسم تشییع پیکر رهبر شهید است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667876" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667875">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه بوشهر، فعالیت خود را از روز شنبه ۲۰ تیر از سر می‌گیرد.
🔹
فارن‌پالیسی: مهار ایران شکست خورد/ خلیج فارس به‌ سوی نظم امنیتی تازه می‌رود
🔹
امروز در حاشیه اجلاس سران ناتو در آنکارا، نشستی درباره تنگه هرمز برگزار شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667875" target="_blank">📅 14:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667874">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نسرین جاپلقی که در سانحه بسیار سخت تصادف جاده‌ای، روح‌شان از جسم جدا شده و به خاطر رؤیت روح مادرشان و فضای بسیار زیبا و دلنشین برزخ با وجود درک سختی دنیای فرزندانشان بعد از مرگ ایشان، باز هم تمایلی به بازگشت نداشتند اما با نذر و نیاز بازماندگان به دنیا بازمی‌گردند اما همسر و برادرزاده ایشان در آن سانحه از دنیا می‌روند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نسرین چاپلقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667874" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nir2H0RTs8DL6gHgkYBX0pNLdvOPkde6tBjxdlBiX7rDVEuYc1CaiHrSg_SshXFrvwElDk7Hriahy5dSzBjcmXjLn0eTD7wuFPtAXvu8Q4QexqjztnqWZukMDEshpd3hrtPGqwMcxN0WFVsxx1SAGOsG4c46XcAtVa-1SPmD5-1WXgI4coeQ2nEpZQbwUlv-_o9uja-LlJDE6AYjv45GBo-SOT-jby55Tp4XOXDgkxl9KktQVvrfPyJKfR5AFPF7C4U0lCCWSI6KgaVMbXB1x-IfXE5nE7qgMIi4Zo7HF1HtWwvLukGxxwQYyT_-TA2Vump3AgVjBSDlc9jzoLHIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه
؛
امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667873" target="_blank">📅 14:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7UsLf3zWN76bkdsbihUbBcAZAON19JWSdU-KIUTM1kWvr7_uJY5PfUuYukbsH9VLalmmWXLsxdRrDBTD0lP82IRy--cqlO0RmhFvITPqTlMSKD3JbfNN8RBeks-9_Ex-MxZ257jugb1dC7NtYgkzus6iJtQLALRCPo5t84qsEdHGkQw9lo4Rr7MCa4QYZoqOJX8-UKuwH5rtfWDqq_X6uZV7B3Ez4Az2MLNTAYe0ZvSSH5-7RkYB0F36wDMEo3ckqZXPIguJPuMljqsko4ehV-ZI3TLsaM2x2JpgjaJfNHcw1tOp9SabrBB2_fS2oTsiOmfGjIQMz0a3Wu2H2UWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk-_lhli8FhaceI3tAp_N0l-4_WxHpH5LXpt-ng5JTNwwILlN18UXeH0UNz9Me60_X_Rynyz5Q9Z8-5BlLip1QwRqDV3P1Bux5cZKoOIgx5toVjwIs9EkKGsxUVoYEWZdz1WtZHbKBt_007-j2roDO3tdq9Qf8LOvAMYXkwNGEBemaxrz8OObUpezHukcs1YuIJGRTeRMvO8U3viPajmnA-Y4k6v7cYZaqTgBsvdLdMbEOb2ofKhPdQDtGyxvRTUhTEpbUcFoTD3Q1KBQxX_7DmGlY2aHaAmpOtWpM05ybymAlxInwuEkAZnCBT0KXZ6fV4073NHcgdQYWHjGMtZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l68hoHEqcHRRyqa5WlH6289lbD3F8rvObLYnJCyh6HhwLFzqMZGmGv9juTRylxRSaqYsDwlk7lUQHIrPAU9Pi8TIXioUs80kEo_7-jttbphnKF4vRDJRr0Usw2we9f5ahzCJDlAqLwsGFHmiLoPfNusjNKJIkviKxPC8faya7EvVy0UrOZqW0fl8i_RwNd4a27eGT6jyuXGv7jChyh_XEHmuiRH6jg2vpz5vZyHzAsfhnsFCwbdoNsN11imXXg374V-Om5-tGXvqDkZ0spZSbThrsOJ19RLgY_dX4muGalEQLZf6SrPxrgxAMH5tdmwK2m9XqfiJ0iEUja9s_VNlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERNDbZGpjoBssCQnUXdatEeVThELh_f9K6btmxVsGwa-ClB5EHXFuc6fRpk6PHeliRRJTx34MWdUMP2QT_4Zrz1f5823Guvu2M7lZkLp7F_1u-iOngfXN_8hUor14ZovetB-Jcq-uzyWuUU7EsyGKZUQcoBLSO3lW34FF14eg0kaxyD3RnMQ-R74RWasSP8YlXeeLutv495AGPXxSlV80i1IrswOlw001Y_3ebkPdq1mPD5PVVKEIXXQitRgA76fJzwUeFf5nPqTB0pMkkKtYRqi_A7ijJ6lLcUeWo6lXSHREV2EPjy7HrgOIPzivr01JsvuhCWoaKbwBszvsDEBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kg2sts6EVINr1slCwqcOGGqsKpHQzLf2exvFLIUXANkdBNyroiepN6KDm5dOmHPC2OtbIyUMtdDW_YdFRSTr8xVIw4osdO_7ziodwbot1fu9ys77UxYIpjAFM8SrfCRXJlYY0pAswhg_Auf20HiAFxMYQbyvaCXyVg7Z1yPJuhtowLW_hGl15Yfo6z5glHJBaTvkIKpNwWd4X14AqVtAdfZ2Bt57IYtJCATMdp_vWruWd-5emKxkZ1CyDdskGleRIQa5h4Z3_IgT42jsQPvkw2OHdZoPG-gThv9qBEXTKNAcuVTaYNW0hPUvxCrXdLSUUqGvWN6TYzME7N2I59Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4107eRJIfDPIALZs7ubGPnw4fBDFNvGuYBV4ddIVqXysz1Zu4mc7_cAasw_qDkrMbPNemfJi8MAxIvFb17PI1sqb1i56B8xk-4Nd5L3vLup-NTLYcrsxVrjUUNmijpkSMl2b2NLAYtZ9vkFZHonVfDl_IslmSQEeWviJmQX92Gvw-rHpnBBG3ZGZcAEySM6BldT61PmVs6Q-9wULaCWY2N2L0cZfQhv5apLgoylgcKE2bfcwnpNnK9H0m4ydI4gz1F6JeL2zNlHVcAUUTkvhb-27Pa0ntLjtTRckrsm4Lmtss0TYa9Pul75H55TIWyEXXAeaEkAtCURTqUnDsDl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY9JvQg4D1BiJXtjz3Xnm-sKU78UTDoXX0TVE5y2ejLGPS1PolrU2tkIgmE841iVxcW-lIi2oT7RXE4y9et9_sBEv0CcdU3ZQHlJ9dcpTeAm0GU-Sv1RFYcMymgXWwmCM56W0xdv0MWFFwtrSr451bRpa_gSKRkhls3VxjulJWSIaee9-HpKmLWAMyIpTtoaItuqmmF2PCBQv6jjgJPm_QApLrRyph-k-J_okot2M1W_C1Pymup5Ycvb7ez3NP4B7_UkjU0EooiI2gNpsbrTtRvMQejeffsWH2vaJHyGpWgBK2MWXb-n2o4i3TfAvcGIVbRhmCRak_NBWU2bJzaR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqVP9dGUhYQMIrDLaNqMy-FnojZLXb3BS6w5kw5LjhVqxM4n5HBkV-_cqp6GsvSYVvMH0UWNt4kkVOfiPHJWbYyO1IZ63G7zwxDkNimgT2_Xp2_HjG5jSKaNaEyyqP6LQHwc1fIUZ_EkSFrY8kQbN2R_yq8bfDi-vQwSt405-h-5meSrDwWsblhdHZmziGk95hfPrf6nLdb5CqkJcwcL15iONB4G9AlDhHbV8EK1HGvT9zyd8i169j2VsjYVmkYNBs441fBFwmc7FSaxwFIUr7cGSiX7Mnr--H4NDwR_I75gLJVUf66HHXTwTp1SyKILufXrfSd8EuPY47kPREpShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2iMQ2ngHmq2Xg3d5kdmh69tqMe8Zx7w2lfx8ffap9pN6m2yHl2if8GxlPDygaHjYjMprnlGJVmLcHHHwOerpO4eXPiiOjJxBPuf3rHHCsRTmiJqtzdxsHUTmsyntMJhIWjrIlBv3e-PFAAKqs18HIOV2RLV3Tfs0cAt0DWkwNe8H0WLXzH282Hpy9X9aWOPACIHJUx0kVELQwz4rrqlSRjR64_dVN2H_cKbRk35iSjD4_3ZETqabJcXwRl9lLYODEAojiLJY8vU0RtSsomR42SqeBT6wz7HajxvyGqPHYhKGaq6ey9O7z5w5xAvaGXouecu4xeoNyp8DnkrqCPWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRqnWeHQEAjG1uHeg7Gn_oODSgkyWETqBflGFAgDXZmvFAdp3wCZvun6EpaJpZNS-mqpT9hzZ_GjFrvzSxUfHEoEMyEdoPwShRSOUFYrTJKRTf-4TwYg1-64jKp0aYxa_dBHzjb0n6uk_gt919qJLEibfBRwGQqvK90L7-vFRr8l8f07oWGtWy-Xtum_QAbY2UyGauiMdgtk1JhyqlCQNlA_NYDEe5_7qf28pmHHlwEv39aSm2T9vgpiRwVMSTVBQrwrZsnUhTFxEqe1voVaTi7jtf2PNhXwM7CUbmRHXuPuVxqALBg7qjDqfY-sJdBSFzLkwBZAFk37SEJ0eaGk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات وداع با رهبر شهید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667863" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زائر تشییع رهبر شهید: امیدواریم مسئولین کاری بکنند که حداقل در دنیا باب نشود که رهبر یک کشوری را از آن بگیری و هیچ هزینه‌ای بابتش پرداخت نکنی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667862" target="_blank">📅 13:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ بر آمریکای جکسون هینکل فعال رسانه‌ای آمریکایی در تجمعات شبانه تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/667861" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ناو «آبراهام لینکلن» از خلیج عمان خارج شد
🔹
تصاویر ماهواره‌ای تحلیل‌ شده توسط شبکه الجزیره نشان می‌دهد ناو هواپیمابر آمریکایی «یو‌اس‌اس آبراهام لینکلن» در دو هفته گذشته خلیج عمان را ترک کرده و حدود ۲۰۷ کیلومتر به سمت جنوب حرکت کرده است. بر اساس این داده‌ها، این ناو اکنون در موقعیت جدیدی در دریای عرب مستقر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667860" target="_blank">📅 13:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اطلاعیه شماره یک ستاد استقبال و تشییع آقای شهید ایران در مشهد
🔹
جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم‌مطهر به‌ صورت مستمر و بدون وقفه برقرار خواهد بود و محدودیت‌های تشرف، صرفاً در صحن‌ها و رواق‌های مرکزی، از ظهر چهارشنبه ۱۷ تیر به‌صورت تدریجی تا پایان مراسم تدفین اعمال می‌شود.
🔹
تردد از تمامی مسیرهای منتهی به مشهد مقدس به‌صورت عادی و بدون هیچ‌گونه محدودیت برقرار خواهد بود.
🔹
مسیر قطعی استقبال و تشییع، خیابان امام رضا (علیه‌السلام) تا حرم مطهر رضوی خواهد بود و تمامی مسیرهای پیرامونی این خیابان برای حضور گسترده مردم آماده میزبانی است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/667859" target="_blank">📅 13:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667858">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی در آلمان در گرامیداشت یاد و خاطره‌ آقای شهید ایران برگزار شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/667858" target="_blank">📅 13:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667857">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
فرزند شهید نصرالله: شهادت رهبران، انگیزه انتقام را دوچندان کرد
سید جواد نصرالله در حاشیه مراسم وداع:
🔹
پیوند پدرم با رهبر شهید عمیق و معنوی بود؛ این شهادت‌ها، عزم مقاومت را راسخ‌تر و آتش انتقام از دشمن را شعله‌ورتر کرده است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/667857" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است
🔹
نماز در حرم مطهر برگزار می‌شود و خیابان های شمالی هم محدوده نماز هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/667856" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۶ میانبر کاربردی برای افزایش سرعت نگارش با Word
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667855" target="_blank">📅 13:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNMPjlMjHbhHy0yN9L8QecbnpdNOPW1SjOZb5BIVZpOigUbEIO2iw0ngGfw_qb3ExFeIDm7L06Qeqh9vV6ulOj9OIHn_xK1nVhvk89nDTLIKYOexA4UDc6MRYlv61ZHjJRCnZzsaEbTO4v3dG6XUcz-rrfGt-Z8JspC-HxAsPuC00zdlQdseqBWcDT_yEHyhA7pz2SGkEr0FeU8R4sDIgkC2H12ybMm_GoCgVwqb_IhDl5LdnRs5Tz5KZfla7iOH4BLSP_1uCLVundvNPeqx-s0tBxIC_8mbYe3hefEme-zTNGSfzlLDX2BvhoOtk8ASNXfA6b9lC0Bw5NOpJWVAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسماعیل قاآنی: تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق مشت های در هم گره شده دو ملت دربرابر فتنه های آمریکایی را محکم‌تر و خط سرخ خونخواهی را پررنگ‌تر خواهد ساخت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667854" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDLb_koEzPME_pBseGf2NuT7f5S4Jj9_100d5oLEDfzVdCzv4ozp7c3vGhXHsro9LKsLBT8KyKEuGpI7wzfwGIbUbRV_q_qm5d0IoLxQF_XsvFDnaENp-5xArHKIZFMiCJW4usOivddqiTpXxbkDCQfzo5h4drd8XxlVscUZIQUghvQI7499bvpy6RkZ0x-MZrga8w_lkQ--ObUdx-AB5duXiJ2KUyRSQ7D3JgLL22G52J_isvF6qlaGAHc7vgJK1tXkwbTQwuj46_Q6QDnE2EzPOQa7Q-I7AtHawYcFIPwys-vjtbxUNCouWEzGAXt-XjQn_hgEioTzYtEspk-B7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران با رشد ۱۲۲ هزار واحدی، برای نخستین بار وارد کانال ۵.۳ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667853" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: دو کشتی تجاری توسط سپاه پاسداران مورد اصابت قرار گرفتند و خسارات قابل توجهی متحمل شدند، اما هیچ زخمی گزارش نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667851" target="_blank">📅 13:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عمان  سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667850" target="_blank">📅 12:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راشاتودی: سیل میلیونی جمعیت در قم برای وداع با رهبر شهید
🔹
شبکه راشاتودی با انتشار تصاویر هوایی از مراسم قم، حضور بی‌سابقه و سیل‌آسای جمعیت برای وداع با آیت‌الله خامنه‌ای را بازتاب داد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667849" target="_blank">📅 12:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2128df50.mp4?token=A_T8LiLFIT808h-zeW5E5G21TQzIy9ETtB9MnZcFIBcKR8_XandF_HtIMElUsuXmt0OuSOGDS-O2aNFMgRpOqG6UZMzL7l0WLl2_Z4n0GfCIoiCVNq4J-lDUZ3rzQfWBlR4XoENe8tyq_bJ4Vun9eZ_Vg6WSTth0wlHv8Nn0VI5dVfMXCTEm0dzk_p4S2Tx12q3js_2HuOKNp7tdbbg-taN9ANHrC-Cj5n5AfN3v3joDFRcpekaGwSPCpicBjiOLawr9lkVdsMahqAsn54WUDDWXmz8p-1Rp3e0Gk6IyJuheOoiJGWBNuVTCLWwDysuVbeCqBUXxq-3QUieRmkrEJYxans1oMG2V6MlxGfH4KxV7xsDi4dbQPFxRjL6lLjNl6fEK7xBe9ysy4WO4bLyO-Z8J9AHbtLGW6z_SxXlU9MUpg41VyJ5o1I04doErmPZeMvEG_pd16Z83G-ImkqWCI8CfG-vImwLCE8OUkFXeQL7lKGrmpAxbwKHp4k8xRcNKItGzVHwTvZk0DZHiqzt8av8iFy6_93pnrtfWcENU0TPRy9PJw0031EklAQilVv6tDvqGrGtek1ZpK1ST7S839NgA4onSmt2fIR51LkQd3F7RUuNtUiOpd-507AuJGDCCp6Vp-qOwsOpvaOOk3nUNpcNblht9KXQ4MWImUfAndAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2128df50.mp4?token=A_T8LiLFIT808h-zeW5E5G21TQzIy9ETtB9MnZcFIBcKR8_XandF_HtIMElUsuXmt0OuSOGDS-O2aNFMgRpOqG6UZMzL7l0WLl2_Z4n0GfCIoiCVNq4J-lDUZ3rzQfWBlR4XoENe8tyq_bJ4Vun9eZ_Vg6WSTth0wlHv8Nn0VI5dVfMXCTEm0dzk_p4S2Tx12q3js_2HuOKNp7tdbbg-taN9ANHrC-Cj5n5AfN3v3joDFRcpekaGwSPCpicBjiOLawr9lkVdsMahqAsn54WUDDWXmz8p-1Rp3e0Gk6IyJuheOoiJGWBNuVTCLWwDysuVbeCqBUXxq-3QUieRmkrEJYxans1oMG2V6MlxGfH4KxV7xsDi4dbQPFxRjL6lLjNl6fEK7xBe9ysy4WO4bLyO-Z8J9AHbtLGW6z_SxXlU9MUpg41VyJ5o1I04doErmPZeMvEG_pd16Z83G-ImkqWCI8CfG-vImwLCE8OUkFXeQL7lKGrmpAxbwKHp4k8xRcNKItGzVHwTvZk0DZHiqzt8av8iFy6_93pnrtfWcENU0TPRy9PJw0031EklAQilVv6tDvqGrGtek1ZpK1ST7S839NgA4onSmt2fIR51LkQd3F7RUuNtUiOpd-507AuJGDCCp6Vp-qOwsOpvaOOk3nUNpcNblht9KXQ4MWImUfAndAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
پخش مستند «بر آستان عهد» روایت دیدار تاریخی وزیر کشور و استانداران سراسر کشور با رهبر شهید انقلاب؛ امروز ساعت ۱۸ و فردا ساعت ۹:۴۵ از شبکه مستند
🔻
مستند«بر آستان عهد»بازخوانی روایت هایی از دیدار وزیر کشور به همراه معاونان این وزارتخانه و استانداران سراسر کشور با حضرت آیت‌الله سید علی خامنه‌ای،قائد شهید امت در هفتم خردادماه سال ۱۴۰۴ است که به مناسبت ایام وداع و تشییع رهبر شهید انقلاب توسط مرکز اطلاع رسانی وزارت کشور تولید شده و از طریق لینک زیر نیز قابل مشاهده است.
https://aparat.com/v/yzsg6d8</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667848" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در قم به پایان رسید
🔹
مراسم تشییع باشکوه و تاریخی رهبر شهید انقلاب آیت الله العظمی سید علی خامنه‌ای در شهر مقدس قم به پایان رسید.
🔹
قرار است پیکر مطهر رهبر شهید انقلاب و خانواده شهید ایشان فردا در کشور عراق تشییع شود. #بدرقه_یار
🇮🇷
…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667847" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAEByMtbzRvqx1EB0JJ4KKpetsHBXH7PVZAmmjYo6BFUxDCVoi8SJyG4JvifBlbPp5Rnw3rWa4JL7Bd_Pkn4Wtjl5DE5ewiahNzrHPDEgLWJuEbh20xjdfCpzVZ6dnHgEPF7HHDL1fK6VkOQEC63iOQv4QNL1wY305vsoXNy-0zagPhldc_G56DUMAq4Kn6R0jM5MH5YFY281G_l4fIEXJCgIjABb0mu0GrfcDyemc7FyyfXt_VlNCP6orZ1ZOY51rFDmyrcyeE_29oy3SsAhzEsQr6YMy3qN-uEwN48lr4dE79sJybFuLwsodFjmTuhnZ7Qg89ETbGyMvOFbOOD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOQX8EViBslIhGx-DR6JEuY5XXu6THRxRWf13ZzEmo4hBg4tKIYGx4AycknKZNAwyWMAz-LrwTBQEbOIB9eE3qwLR4zwpADXUnzWJyGqz4wqEcJwzq1NX6cv7I5ZwA2ql2QRgy9TDIb5tYhnXTXFnSS7dCYYI2_BPB2E6ZQ2QwHC8AimeEiJlKsIBBxoWL1_HelSnYuayto362O91XKEycqUtbygT2hlCFxhulnAs9-aBR044H6KSzKrsWUB_EBBy9Fqmcl42beB8xt7XYzZY2Yz3GlXfFM6zQe8R-K7jstPo2rkOPIQTcrog1uYzlNyjGCALwO9SyPfWiE0_fO_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6I0GmHRqRMwWk-yuiDODZmPRJxGaz11XKvwvVH6-yLq6KxxGgfIozHiw-9gVUL3pq4gBO1hA_Int1vL3q5XGXSb6NkiEPgBqdGtkbV0_GyRMIz2qEUSg97PqeK7QPAsEFms835qhaFkDL9qiXDUz9v59N1yJlpcWgce8l2gLUYdx_8g6Ln3UUc_3b7zSJmTBl2sV40dPki56A5QXXWfVjjawE2qRjIBDMldva7G2aybGkEdzdlj-AcLyAJaU4__nmWuzf4Z4s4IOBpaiCefYE9Imya1zIgCHIrM3GWMITDUAZS6w5WdCsijSMcjoSjb0cNqHgydCJTLz0lKH3--bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flLUyid90G1xBXinhgjt8dWFksXfYujDbndMVClXXSIFM_nYyjKioJBrrxyDOg8wf1QD66QZiwdn9Gt9DltdFMYmLYbObmCR5b9vVv-HxKjUF09aVB2oQS89PQEwsNm-IgqWOTeiQVe1N9ZoZG1Dk8FYRdkO6YlEwme5nfleC7F-Bx96Xw61lGsn99DPSjw0NtwFms0X4mC9SVz13yc_ZvkNmA1tdeZ2n3zFX5GCfZpYafG834oA0dMqyjiB1paZ7FmxePfi_B2tDBrRIqtlF6reSg6-iXC_klQp-1--sDrMXDa_PTkN5cbufQyBtuYUzwsFGKpRaJVJgHaspD-0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxYkbdbCPCj1g7gEZ6IzA8UbLdd3p2EhooBpE4AyomTkWqndO361DL7ykmhd1jdftXBhxBrA5ZaQGOkVmCEa1DJHlPROFs3fpRgstCvVytTzMvft4g1b4vM0KuoNgPo7hkiotzfIXgS4CAdU8jCpy4MuMyZtN4Ews8Hbh9HoQxcg_nthx79dXxyfN8TTX1Sk5mQEG6KyqGIJgDKsq-X16EB1GIZChBUi09iZbsc4eyGhWSk8ytaN-zOuHkoBVFjHyGQilW_ic6Hf9Zo09mw5z_IwhfXuy88ngyDGVA27F7RWYcNmZZCvFKHZaoGPpXV0GZ52pOVG6_ZNqipvotwEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJTrm4KRV53o887_cCeW6j5BS0mekp5EQhZyg8xSLlpvKBw6nVxrRzBz1wPbbKqujISu7xsWfWc_Z_DzjYulHpZSmRdq_vjr29y3T34mQVvZR0Cp8FlIxKi7tkLdC8uOwCMojl62_QuMFr8ZvvB5zMyCtLwqfROt-4tSN7Z5Ty8UoRtmntiC2BdLHDON6tQA5YlToF7Yz2zEbuCABL6FdCPN3K12bWUl_HlWV7Ra25DvqzeALv0LBl3EzPaF0wjyGyDPWzH4bGt7fpvpOMsEdn0Hn2QP1pi6_-qxH0BzZ4ioKg8bxB6Uud1n7rWHH67nK_h-Dp1YKycE6ek-usJXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bcw8u2tL03KGeb9B2gLtZ_bmLSpbQCnLs6033U0toljK1ydI6kR3WX5ryQwRxhg5i3EJSng1nXbLENvw97tzt9VcRZR7u5veTfeXNsrLfDMyDQ9Sn1TR2EiCvYHXMRYgPPfssPgMtRX11q4B-O4cPUC2VH8pP9KvzyURiCDqJgPRvA8NwAK1EgPYag6_Z8QSl9Yt1gz1U950Bp7Z75CeZaAEunIlVEqa2LVD2gD08u9ISKu3ws_imHks-nGK5eZp6NIfVfupHJ5uxNHY0rliZng_xql43_aSaH9vs-BIijcREBg8w8-kXDdeyxY20HphpaITKfXzkPmzmM8_YwcNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrK-A4zbOc4hWEn2qBoqPbaTRtQqZz-o0Q0SmS5obulUT_e_dR1iHnX9ZtEbJMF6D5vIrPVSbgnDE9bpEPc8WA6t-WJc0TcouK2zbYmN8Xm_V7_VJbJJKHjPsJIqY2SWZwXhd5xuE6t15e77Q4qMO-bKH8Rk1ixib-JwTP2uEuHBpats5sJ9TH9RsOrfjKBoheWjapWJZsjm8jAKchsmpZF0O6IJbyKLaqsJRA29-CZolyxuWC8Qa-ImqvgQwHUONjXPQmB8_MX3Ef8w0TLPr7GoMe8u988mt-jDav_bdDR7ezgfjcygmbqXxBFSZGs3H-XISXIh9GOCSKXETHI1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم تشییع پیکر رهبر شهید در شهر قم از دید لنز خبرفوری
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667837" target="_blank">📅 12:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209d04c63a.mp4?token=NC32yu42cCWSb5pjrKkNlBfXT302y8IZQltU5MLE96R7iIyoOI4FszSx2pood7VlzAZG9y1d5k-EMh5z1-ZjAL0yXegcRZDzxB0Dqf2k4bE4r4AXYyvaJsXSadkmILHhxcbzAyBtUMr_DrKlm--CtN8OFEoEc9a7Jne0dVYrMKgpXy2JUsKkEUvvIbdF9z5ORIA96bDVmhxjwoZ_1i31eec_TZx2G6apFU1pP0mWszPehREFnpQ1kgWmprWgEzuHHiFbPsPDXdRfocqVzZTZYLNmnQlUivXIqRa8U_ajzwkR2O4YcBCVAQqKH9dOfBWHiqKBNFiXRA3P4CAxPDFY8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209d04c63a.mp4?token=NC32yu42cCWSb5pjrKkNlBfXT302y8IZQltU5MLE96R7iIyoOI4FszSx2pood7VlzAZG9y1d5k-EMh5z1-ZjAL0yXegcRZDzxB0Dqf2k4bE4r4AXYyvaJsXSadkmILHhxcbzAyBtUMr_DrKlm--CtN8OFEoEc9a7Jne0dVYrMKgpXy2JUsKkEUvvIbdF9z5ORIA96bDVmhxjwoZ_1i31eec_TZx2G6apFU1pP0mWszPehREFnpQ1kgWmprWgEzuHHiFbPsPDXdRfocqVzZTZYLNmnQlUivXIqRa8U_ajzwkR2O4YcBCVAQqKH9dOfBWHiqKBNFiXRA3P4CAxPDFY8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران نیست، اسپانیا است
🔹
در جشن سنتی سن‌فرمین در پامپلونا، تصویری با شعار «اسرائیل را نابود کنید» مورد توجه رسانه‌ها قرار گرفته‌است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667836" target="_blank">📅 12:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edVQxzv9X7cxTPr4ztYfhA_eAErHdk_edtP1QvlAcqRATT2a8oB7rK6g6nd43yP63RmZUFuzYKNfPiqBYKgZf6iw84DTV4_PTsWLrX3JW7sQt_UwDtvs-7LU6ca9ph9FaHntGlAJruubzfl1pkELv7LcYo5f77jEGN7aqGV6BkP_8_6AzH5uFaHO4Kx1UvQeuJi_ZSU48ugdd7dH7k4orGrbsEypWRdzVgpoEYo-slFjfh3g3Q0JxZCMDhnaaqxOqePEXuftyXnzPvDr4UoW0a7grTvPqkhKeyQDl67cQ5yhItQzkHXQZUPdx0fhcTxOruJc66nFhcmKmkADK_L4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در قم به پایان رسید
🔹
مراسم تشییع باشکوه و تاریخی رهبر شهید انقلاب آیت الله العظمی سید علی خامنه‌ای در شهر مقدس قم به پایان رسید.
🔹
قرار است پیکر مطهر رهبر شهید انقلاب و خانواده شهید ایشان فردا در کشور عراق تشییع شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/667835" target="_blank">📅 12:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13eef82e5.mp4?token=Wqh8Fb0YgBifVVaqpeIvaeoP7M-ffdC6C37C2Mil6KKxAy68dpDsnc5yKn0mSgZsa-b73_xhCThPp3Qz0PM1WuYp5O5TmZ760-CPxhXepe3qiCmb1Mw6cyKmXvW36tvnyoCn3wQLgZReuq_x-2XiR8z61Ny5jqupPluftD9Xqnz15KGBd5fkPEmYJ8pHTRgEVt9lvyYc4d5AjmdBwZZ_mu3A98f8ZQ1PXXILczhox2XeBCoocYL_h2HGelExxWfKeB60KQO9PWMa5ukMD60l1pTNOzY0Y0_icHFvXbixpBlefHxCD3b1KOatH4vaxELAiNcQUHUD9VwiZYJoCBFPwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13eef82e5.mp4?token=Wqh8Fb0YgBifVVaqpeIvaeoP7M-ffdC6C37C2Mil6KKxAy68dpDsnc5yKn0mSgZsa-b73_xhCThPp3Qz0PM1WuYp5O5TmZ760-CPxhXepe3qiCmb1Mw6cyKmXvW36tvnyoCn3wQLgZReuq_x-2XiR8z61Ny5jqupPluftD9Xqnz15KGBd5fkPEmYJ8pHTRgEVt9lvyYc4d5AjmdBwZZ_mu3A98f8ZQ1PXXILczhox2XeBCoocYL_h2HGelExxWfKeB60KQO9PWMa5ukMD60l1pTNOzY0Y0_icHFvXbixpBlefHxCD3b1KOatH4vaxELAiNcQUHUD9VwiZYJoCBFPwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه باشکوه خیل عظیم عاشقان آقای شهید ایران در قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667834" target="_blank">📅 12:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پمپئو: انتخاب چهارم جولای برای تشییع، عمدی بود
ادعای مایک پمپئو، وزیر اسبق امور خارجه آمریکا در گفتگو با فاکس‌نیوز:
🔹
حکومت ایران عمدا چهارم جولای، همزمان با روز استقلال آمریکا را برای برگزاری مراسم تشییع آیت‌الله خامنه‌ای انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است، نشان دهد.
🔹
ایران قصد داشته پیام دشمنی خود با ایالات متحده و ارزش‌های مورد ادعای این کشور را به نمایش بگذارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/667833" target="_blank">📅 12:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d6fe01e.mp4?token=GKFQ52puWIDComYtklo3Rh1hdUflPg4v2xEgCWWk_pRJ6Ok1tzPeGRoanfgaBBwQwWB2RggZNzTqfNs9oVhquopGHI4EiJwuM9ouXmqdApja5e9_aQKxDGZVNtkMKYcOk4eyJs5wg-qa-aF3eS0gQpKEitb6QToD4D8agANgO_OIAWQvyGxyiwsGMcuHUeCikG6H5r-RQ0vMMlXpA5iB6P-DaT83dPIRDLloj5AGU7lf3ji1ANedtsuwPkJymexhWPrNtlvnpdwc1yFk2E7k-DQ_5lsdcGj6CLWnVnjVmymIjbo8ceP8JohEViIwiDWD7430XEX9Qk-EUvtrT7IpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d6fe01e.mp4?token=GKFQ52puWIDComYtklo3Rh1hdUflPg4v2xEgCWWk_pRJ6Ok1tzPeGRoanfgaBBwQwWB2RggZNzTqfNs9oVhquopGHI4EiJwuM9ouXmqdApja5e9_aQKxDGZVNtkMKYcOk4eyJs5wg-qa-aF3eS0gQpKEitb6QToD4D8agANgO_OIAWQvyGxyiwsGMcuHUeCikG6H5r-RQ0vMMlXpA5iB6P-DaT83dPIRDLloj5AGU7lf3ji1ANedtsuwPkJymexhWPrNtlvnpdwc1yFk2E7k-DQ_5lsdcGj6CLWnVnjVmymIjbo8ceP8JohEViIwiDWD7430XEX9Qk-EUvtrT7IpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فضاسازی کربلا در آستانه تشییع رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667832" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5951235a1.mp4?token=pbVoWdqgcwSoKmr4A-sPx0v6ycCExx6WyNfC_G8_F72VmlGFjBK8TAfrVWeOooHXn42yUp-LIyDUuVKp_fxzylYua8Aiotosn_3-nT4DoEahFVkzX6PadlSHEVtZjqaUnITaEK0UyVh9BdTjGjduQgdXbzqZzVvO88KptpBGuc7euqKxuJfPGXpo1aGnrCTYsVyqcf5ZodBjXMXej9fzx6Pdu8jkthudaCL1XD3P5wLp_RSEfSIiAltvdT4GCRymSQGtKiEN2XsmIJSR2LYnMAT4swZNlrfRyfPZwE1a4J1XrnxNbZCyyt-2JWiG5bTkH_GTRqu8azKtKW2eMF1pzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5951235a1.mp4?token=pbVoWdqgcwSoKmr4A-sPx0v6ycCExx6WyNfC_G8_F72VmlGFjBK8TAfrVWeOooHXn42yUp-LIyDUuVKp_fxzylYua8Aiotosn_3-nT4DoEahFVkzX6PadlSHEVtZjqaUnITaEK0UyVh9BdTjGjduQgdXbzqZzVvO88KptpBGuc7euqKxuJfPGXpo1aGnrCTYsVyqcf5ZodBjXMXej9fzx6Pdu8jkthudaCL1XD3P5wLp_RSEfSIiAltvdT4GCRymSQGtKiEN2XsmIJSR2LYnMAT4swZNlrfRyfPZwE1a4J1XrnxNbZCyyt-2JWiG5bTkH_GTRqu8azKtKW2eMF1pzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خالی کردن دل مردم جرم است ...
@TV_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667831" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
روزگار سیاه آمریکای حذف شده باوجود رانت «کاخ سفید»/ شیاطین سرخ مقتدرانه به یک‌چهارم رسیدند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667830" target="_blank">📅 12:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667827">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70352bb00.mp4?token=GjTQ8A7SjU3pI94gJ5TGo1nGx0BWExXua0qlp7h-z4hN0is5yEOQBYTxd98h_1j9Q86g6XRWutVmT6ClbAhRr8gPdP951YMYyEpXRPWmvNJZYg03DcIDQ0Nwq-JI6YKZEN-Lft3UCsbzhJbryIK4EysY0U4TdWb4Fk209vGQ0SFkEvKOeo7mtayFZ2dn7fi9GKHPxbhWYAfcuAoqrkIqRisK0iy57cishaxXu6wGZ11QGoAT8yq8tPR0imlFM5noU3ZKD36ez_Qxcy0kZon7cPopNr5T1-rnfHNHihtvZ8DAfaHr0c4w7Syyv4PzVYZv5jqY865pO0sXOOcMQxXCpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70352bb00.mp4?token=GjTQ8A7SjU3pI94gJ5TGo1nGx0BWExXua0qlp7h-z4hN0is5yEOQBYTxd98h_1j9Q86g6XRWutVmT6ClbAhRr8gPdP951YMYyEpXRPWmvNJZYg03DcIDQ0Nwq-JI6YKZEN-Lft3UCsbzhJbryIK4EysY0U4TdWb4Fk209vGQ0SFkEvKOeo7mtayFZ2dn7fi9GKHPxbhWYAfcuAoqrkIqRisK0iy57cishaxXu6wGZ11QGoAT8yq8tPR0imlFM5noU3ZKD36ez_Qxcy0kZon7cPopNr5T1-rnfHNHihtvZ8DAfaHr0c4w7Syyv4PzVYZv5jqY865pO0sXOOcMQxXCpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله فاضل لنکرانی: خونخواهی امام شهید حق مردم است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667827" target="_blank">📅 12:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667826">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdZ2F-1HWMeeYgGu4V-YUkQn5v01c2BifZ5T9eMXPtm4UvL_3siCTo0__xXzKUXGdQ8JmXjuPQGy3p9WEeVpP0dvU34vFCYqpp8DXAwBiMpOQNBGVD39KjDoQ5-uxc0nY4kDd_TODOfaOVX_978Q2C84QusRYmAPWWCGundVq38fPrw75hXQZV8ElSIaQIU3Ny9y7tnFKZqATKjymnuU2_yqhPIThlrR-GuhERev5Uldjq07-8nc3lh4gTPie3eyGo6myzBXPWA0-LAdu767bYE0K9RPhag4THGPLC4Qc6owOGWjpUyNVGdUV6rIKl8TAV8nfD5K1exwfhBGHwA_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران با رشد ۱۲۲ هزار واحدی، برای نخستین بار وارد کانال ۵.۳ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667826" target="_blank">📅 11:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667825">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
خروج خودروی حامل پیکر رهبر شهید با بدرقه مردم از بلوار پیامبراعظم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667825" target="_blank">📅 11:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667824">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgpwtn-pmVt3pEaFtaIFDeavRGslRsqIet4bvwZcXKaHZLggiGbPJ6rjxYDEI1A_o269idtwHqVl8QKoZ1Al4LeNGgnwTZ0u9jS87n-kSEIRts02j1wfTTtmcA8Y4Fo1JHzxzxL3R4qbrQqrmROJDRf-LV3oJnP8DRlppMh-xSqP3IGGNXCoEJnO7xwCZfcYqdnPPgL-rNZ-xh0Ofn4qivhBk1UcPuqaw2MJTy9JOXxffsUZTEyZoJ6yoHJlkqUoEp0yv8OzGTMnUyFfZFiYGnlYHsf2L4xNzkNZi28nPzlUatENK7SrZkQp-xO9SZEJiCR24B1OOJhYMeFVWqTSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی مشاور وزیر امور اقتصادی و دارایی ازخدمات رسانی موکب بانک توسعه صادرات ایران
🔹
حجت الاسلام و المسلمین ثقفی مشاور وزیر امور اقتصادی و دارایی در امور ایثارگران با حضور در موکب بانک توسعه صادرات ایران، از اقدامات و خدمات ارائه‌شده به زائران و شرکت‌کنندگان در مراسم قدردانی کرد و مراتب تقدیر و تشکر وزیر امور اقتصادی و دارایی را نیز به مدیران و کارکنان بانک ابلاغ کرد.
🔹
وی با ابلاغ پیام قدردانی وزیر امور اقتصادی و دارایی، خدمت‌رسانی صادقانه و حضور داوطلبانه کارکنان بانک در این اقدام فرهنگی و معنوی را ارزشمند توصیف کرد و از مشارکت موثر بانک توسعه صادرات ایران در اجرای این برنامه قدردانی نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667824" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667823">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB21e9RmURxeRLL0RsqMIXEdzSybrRK7lL18PtcyA4MVTp-2kNjGBVYP_XTPNIN6lXOllejuG5Z5n04SDuE2R0LDzVt3m7zFwtchBsf1Awudoeq2q74UTBrO5js5svqWPw21qFDqU8QQaOJap8VYqTbinykxs5TaE2gXxyEozFXZan1g_2i6NAzjNjcZ6tTuH4ItCtd91UJU258TI1Zu5Bt3V9mIi3qhLU04pYMyFiqqjshbKaJrvcm9oPaBG8RqHoZ8E1YKzG8R8BzsBzRL-iKcNWrsjLAKyE59QfGdM8f4CXat0lKs-MX9-8q392fkumR_e5q3mPfKEymXTA_VHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/667823" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZJbfGXY3zJqU6gMbkkrlByUJK6qcqjvlHaSA7pZ94t91uTJUAXcICGiY_Phd13PAJoJaW8y6jAoW7rGQLVy0ibb-C3xmPMJavcj5yVaz2rMFzG01aaErXNtTIBcoyhSzjs_hTQwuPi6lTlKyIg609Da4Rq98d1yVwZCpOEtjPbLs8frTt0718w8s9FVC2nTAiEuHNpJYSHfYKtCAmTO3456YYIrForCYv9svq89Kg_4AkPq8IK4QjLOnsz08T26_de1-k4W6mPVr2_f-b8Ue52ARfgGPeiZsktmRUbonqhtedk2ZAmuov6u6VtCnMxG4aH7SmY-hqwgE4Enx39_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoiVmYj1OWrueNogn_FSM1Kwyy4lzSS3bQbtYsFZGH6fRn6GAUUZ8J1xjBRRqcUfIpEF1s8IDN_YB3wpWQz5ivSssnwa0kjvs8IQaet5DVqJ88dKQgOjVnPfVcRyncCFoxXBQ7wkYJhwLBB8BadkGIsF9mzUCXpZvoHW6dt8jFI9AjKpL3UyjTsoMO1h7cJ3jvdTKX8Pa7wi4F7BWY-aCs5rbwC9vFkxf-AroZTdRkvbs6jJc-6kldkUWLj20s2eFddiEoHwGemnIEWsM_8_D27GptGICVdKJvhVrI8Q_XpjyhdgV6ixBeirD5N3RVwcVfLlYxt60CoIbHgrLa2Nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbxSKuT7nV5eUW821tWZPO4ePwEV9-VHsBZXZXufnVflKeUoiQFARWYSH-MU4IiuKJ81nWcAd5aQV281d9oeVtLiglHLiVjsPDQTJoc4ZPUm0xBA_FqPWMUCLTueJojWkWdNK07zElJXDp7mXQqeTj0Y2K26lB3Usq_0s-DYCOqRpIdbmrllHehR35R2czSeTOY-F5mf92plxTS3kCgq0s4u3rZ5ByrvEoUDeocP2Wwg_uy4YPMO5piU6bsomrjMKKEdyXHSm8yeN60XV4J1aCYg7rHxuYBP_3WKsugR3uFem-uZau2UTJYMpaXNbPlCBArv3F-PqiqIOkj4mvqoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMqHr_g3GAhfJqpaY8RX2OgZ--f1YlV8AbHcvTTE6yJuesruZP6bujPTYxVWzIphdo2vqQ6orh8Q_w9RXYva4csGw_lVQNAYrCi_IL2tOwnE6fJsETRNH2MFjEfFOAAtwuTTWpCG086L37AOUKOHjWe7Zzdm-H4XPXSIt8iGCOdbDCdIT69KU6nmP0OX8BeCca0W30iZe81zD2_mH9sz3sMsu3AxPHPqQNljWFdb5PFEcNBBBauplvQ6tsjYRqyAqwxcAzF7KJIRP_hiTf0Rj_ra6pu4EKQ9XPoPhYcpbS_q42fu63wdFp5zU550-4P1KiV7tobEM8QQNdCVvb85Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co5BOhG5f3zNCv5eEZYCQXnkqtvNMrdTRoBL-J68LrfAjZIT_53NbeShY7GfgHaBWGK6wKird4V7Qs8CsPn0dcg6uqqInEHk9U7L0GQL9w3gCRH-gzGLvw_aPqjVwkHyXORBF-P0-SHp7uNOYLsZ1vuRiGEAF_yJ3XM-TdNuromCXv5kZt21r83_Mf9_bbAtA-m_s2xLH5fDyWvC7Bq7r0BhkKmGkJayt77y7LGCPOrbYtvOve9Rbak-p7vn8eJudfNXKF2f3CchvWvPyWlhossNfGowXZVcXFyY9vK2Y-fOLex-FpQVbu2PcIHkms8WvCtjPttQlMp3H4IKfw1deg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نجف مهیای میزبانی از قائد شهید امت می‌شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667818" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دریافت کارت ورود به جلسه امتحانات نهایی ۱۴۰۵ از امروز آغاز شد.
🔹
۹ نیروی پلیس در حمله مسلحانه در بلوچستان پاکستان کشته شدند.
🔹
طوفان با سرعت ۱۰۸ کیلومتر بر ساعت زابل را درنوردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667817" target="_blank">📅 11:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8d0bb6a8.mp4?token=rvsqkQYLtIsA9Vi_ueMxr-QBdoc8EUyQz3xdNLSQy1z0hvPij_zMW9ukI-jRiyKnvEznW35_tVGg9W9b2YAah63SKn_l6ZyWn9ITyfkprjmR1VutoZFiP_99NLhjyu3d5x1am_I8rbeoFHIDG1TCx0QpR_Fp10zSEVPz_gf4BH0OEoNSXLkqe1iz0RgsNBPwTRmmmEGwSJ2sJzAWMXxO6AaTIZv-Sm3uyDUGaiEpiadK2vibRIFGUdbWMwiHdploA_8Uy-WOn--sgXvCB3k3PRh407kJx-xf3ko6hpZPvC3CTNLxT8H8Henf54C9JhFF7WNY2Q81F2xsyeevIbjML5Ahreegj__n907vUKxFpCMcRTIcMQqOaM6qjLCt1sXIqKiKJ1RsyPpj2yfuUMuC9r2Z1RzAOC6pLyQ9GDsmO8Cx9W28wJkHRrYc7ZSOSgRH6gZUmG5cUYHilRMCl3_w3rsF2dKueG7U5qGLP1fNdTypP7XBXLxWKa10P5NO56hqOB8ZcL8RfNY3BYQk_17Z3Lah4ay1dHssG_CL9YfMwue5S2pf-XLc2pi3A7AtWSx2jCl48LiRN0d1JqViDx_w4WJH2MwCc5cLGwwA_RmF6e9yVs2qn9KpZ68WCLQxE9CNxkB4_agyBesl1znLGm7jjLCZzwdk3SM3O434Zl4_wwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8d0bb6a8.mp4?token=rvsqkQYLtIsA9Vi_ueMxr-QBdoc8EUyQz3xdNLSQy1z0hvPij_zMW9ukI-jRiyKnvEznW35_tVGg9W9b2YAah63SKn_l6ZyWn9ITyfkprjmR1VutoZFiP_99NLhjyu3d5x1am_I8rbeoFHIDG1TCx0QpR_Fp10zSEVPz_gf4BH0OEoNSXLkqe1iz0RgsNBPwTRmmmEGwSJ2sJzAWMXxO6AaTIZv-Sm3uyDUGaiEpiadK2vibRIFGUdbWMwiHdploA_8Uy-WOn--sgXvCB3k3PRh407kJx-xf3ko6hpZPvC3CTNLxT8H8Henf54C9JhFF7WNY2Q81F2xsyeevIbjML5Ahreegj__n907vUKxFpCMcRTIcMQqOaM6qjLCt1sXIqKiKJ1RsyPpj2yfuUMuC9r2Z1RzAOC6pLyQ9GDsmO8Cx9W28wJkHRrYc7ZSOSgRH6gZUmG5cUYHilRMCl3_w3rsF2dKueG7U5qGLP1fNdTypP7XBXLxWKa10P5NO56hqOB8ZcL8RfNY3BYQk_17Z3Lah4ay1dHssG_CL9YfMwue5S2pf-XLc2pi3A7AtWSx2jCl48LiRN0d1JqViDx_w4WJH2MwCc5cLGwwA_RmF6e9yVs2qn9KpZ68WCLQxE9CNxkB4_agyBesl1znLGm7jjLCZzwdk3SM3O434Zl4_wwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پیش‌فروش بلیت و برنامه‌ریزی منظم سفرهای ناوگان حمل‌ونقل عمومی جابه‌جایی شرکت‌کنندگان در مراسم تشییع قائد شهید امت
‌
🔹
معاون وزیر راه و شهرسازی و رئیس سازمان راهداری و حمل‌ونقل جاده‌ای با قدردانی از حضور میلیونی هموطنان در مراسم وداع و تشییع قائد شهید امت در شهر تهران، گفت: با توجه به پیش‌فروش بلیت و برنامه‌ریزی سفرها از سوی عزاداران، آرامش در سفرهای بازگشت در پایانه‌های مسافربری تهران برقرار است.
‌
🔹
رضا اکبری افزود: پیش‌فروش بلیت در سفرهای رفت و برگشت و تامین ناوگان مورد نیاز از سوی شرکت‌های فعال در حوزه حمل‌ونقل عمومی مسافری، موجب شد سفرهای هموطنان در شهر تهران به صورت برنامه‌ریزی شده صورت گرفت.
‌
🔹
وی ابراز امیدواری کرد با تهیه بلیت سفرهای بازگشت شرکت‌کنندگان در مراسم تشییع رهبر شهید انقلاب اسلامی در شهرهای قم و مشهد، شاهد بازگشت مدیریت‌شده و همراه با آرامش هموطنان به مبادی اولیه سفرها باشیم.
‌
#چشم_به_راهیم
#باید_برخاست
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667816" target="_blank">📅 11:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
تیر دقیقه نودی به قلب کریستیانو برای وداع جام با رونالدو؛ اسپانیا به یک چهارم صعود کرد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667815" target="_blank">📅 11:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
عناوین و ضرایب دروس سوابق تحصیلی در آزمون سراسری سال ۱۴۰۵
🔹
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش عناوین و ضرایب دروس سوابق تحصیلی در آزمون سراسری سال ۱۴۰۵ را اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667814" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
برگزاری مراسم وداع با رهبر شهید ایران در تورنتو کانادا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667813" target="_blank">📅 11:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ed2469d7.mp4?token=mZpDdRjSolkJMptlmHgFwEBaNnehKNd3sr3Yauzim28GnBKCaHoMoCbIR01UlzaEYimbi2h9o0dkMuqA1WSKhmTPd_loj1kd1gMx6uZI8XR-okGPSTgZ8am1pnmCzX-PHyyJjvM1CYYGwsyrXNLjUc201lNY7ZAv-5QXQrjihW9LIH8c_wLfHHpXDGwGeZcLsPTN_RSAjQGMsWHUddwXjMIRvQ2UCl2eexe87Of9R7hOmorPK0I5eSb_lXZDpzn77ea3maMGeyTpHzSYjprcarKvu9jfR5nrCSrodugIo4KB4tEybPm9gswvUOHU95Inm50aY7wIWBgwdr5eVOSFVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ed2469d7.mp4?token=mZpDdRjSolkJMptlmHgFwEBaNnehKNd3sr3Yauzim28GnBKCaHoMoCbIR01UlzaEYimbi2h9o0dkMuqA1WSKhmTPd_loj1kd1gMx6uZI8XR-okGPSTgZ8am1pnmCzX-PHyyJjvM1CYYGwsyrXNLjUc201lNY7ZAv-5QXQrjihW9LIH8c_wLfHHpXDGwGeZcLsPTN_RSAjQGMsWHUddwXjMIRvQ2UCl2eexe87Of9R7hOmorPK0I5eSb_lXZDpzn77ea3maMGeyTpHzSYjprcarKvu9jfR5nrCSrodugIo4KB4tEybPm9gswvUOHU95Inm50aY7wIWBgwdr5eVOSFVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران #بدرقه_یار  #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667812" target="_blank">📅 11:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رویترز: انفجار بمب در نزدیکی هتل محل اقامت ماکرون در دمشق  رویترز به نقل از یک منبع امنیتی:
🔹
چندین بمب دست‌ساز در نزدیکی هتلی که امانوئل ماکرون در دمشق در آن اقامت دارد، منفجر شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667811" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJOqrRAfx_jmIEnbZaI1Nfmrto8y_R5KcJmBU9aZ2EkO_7zTUtEpI0d8wOEc-0VNIVTJ5y8NsUB0K5MkXjzuZz7wj4UKYEM9usUoRxE6kM9NGQhxgaujCBuEqZRHsJK_R7RyFMp7BU1PAq_ZdKYMSVMVv1yRmoJ_roEWv_0s7v4ss370AtWwA2tBowme-6BtobvVlyuL7U8IBv2z_S_86fJMyPVyjSdWQ8KaJ-e-6IOHYrXfr7xAfVop84ga2Esdelc63ULUeDWeqcKpAhZRdkyWE0oGPpTHSFPg7EaX2Vgx-io1zZWYPAWW1VclEADEY_S5tIvTbLXdDHzW-_zeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VADYvbrqUI2fx8iIH__juc9jeI4168EJxSWTiX4nHRxWIgy-m1qV9U1oMe1EuDbeg9rdC-Rgsnq96lBWzOdFZGkCAml0mp-j5LYVESqLbO8ce9JJFKpibAFoe4L-dyF5nDQ_62PBYNPWiMP-igQdFRpWqDDUiXuLrnAL6x1THfda_JMAbtf8NpUuv6ynovSeWLsEliG5ry_6CCOfMS5Jw18ca5y08Ws7hedVrdBJDTR_YUE3OdIf8MaP2anOWml3U-yMFavKu0-ZWt8qHLVB0rX7niUmPfxWNE2lW6iWHVF9s-AatCtJHQTST9chLSV2Y4fGTfgaVbor01sQEIhJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrkwe6HL3kYGB_lObYiKry4MsL37xU3Nc4DpK0sBMmZAQigOc-a9SoUuQFPaBArbuek8uN6dJEeCPofc02G2lxktAVGKBxmMrye8tOHqHIPQjP_Ogf21inkQeRSluySIugct6kM_nMqjizeecxEVLsGPRO7BSYV2Fr0px3vYFf5zHdXSWKA3IYR4yXua4xkjrHJ6439vSItqAsV_rdHiOXs6Emayn0IoCoBeqWs2-0ZdeOA-uUxXsQlctrRIoRd65mwnOXyuDlktIop-NeFyCG9SsUYa9GX5WlbaqlAjnN2IvPe5nu1ic7IKaOMFAAWzWzFsN6tDYVFgUNSRHsB8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIjrvx6FidZDdldrMG_Rq43EBfOpExXWB3kI5OUmOHbewH250Qna5hMk4uE-lyeOuFD1GTXHYp9wVEsH36RzK-lyiTayHmHhqz9cygHbecUSiZJjVL-1bdnWT8NlN7thpisSA8fSLiKscpJ8ikHrc2wuSKIZHV5_V-goegFWU-913718_Jz5e6nLlQgQXMZ-Dt_-HmCWJ4j12mYnTF3JxeIrj2_RKOtARImwxV6W0FK1fu2ftRutitypryC-Aa881hTFGwllZHnoEVqJ88VscjhFBmpUclRfUpyz6vWTz4VdIPy-eucRECwChz-A3kgXzgad2IxMkfUBscFNNIf3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsBsGszyRNRW2evQ-UQZ07dXpTkxqJUoRi4sAvquKfkg248ZP-wYs4c3e5dKFR9Ios3vB9Nkb4rHW8CTzjfBfN3DXsKsvXma-CPdICmEYjc1ZwoPayWpFGBcuv3tFR059-Yw3gxATJ0Xxwb64E4Rb5VdjGXLeE4B9l3IZYHxT_96x114HIR3H8SlgVtFwE5SNRS-fhW928PweoJntSkLsL7X7zK33hZUNRjdeZtf-61A-G1P_18khz4Tpk67uMEdJ7KF0bI4SCZuCQon0fPX7wMsaigxm4BOfaV2zVy_16FmiZPNmw72SITV0v6xyS4SnZl2NhhKLPO-P9o4uIGr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DT9rTgH3Nj8XI1UZoxqRR7AWQ0pWEDfOkX_qzSemnumFV59GcGhMnj4Vgr6NdSP__IE4hkDJM5lRc1SvSsRA8QO5a4MwFm2LFXKyDzzxzrYue5D9FHGqQqV8waiMIGOZ6RlA1T-Pea2wt_72Zp0utnFbPqC4zvUsoXhBxmKImNNgVo5_6bb09NbFjMvL9fHaYqInIEbWZNDg2w7oleCFlmvU63U0qbH3GbMNAjyJAnCVg76cDsVl1TZV2RnHGCA4ez1RXLb89Ap-Jt-U72LS-no1sUOvz1xMWJ1sMyOvLhbgtp-FDZxZdBYT_HOwR_PvD64V3DbmnoUalatT_XBQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmJKDFYoZi5pUOi-yZEAOokfL7ur-32gh_Bm6B0VQM-J6K5v7oIu0_RJAF2FfXEPZFEFGnNsqJLgu0R61fXpkTHI8aNnY5RUQJXJ8CtFYBXT1rbRcr5dyGwCeuATPbvoIOrgqKFSaNcYaoy0EzH5Fn8GsHQqAW9eEIjrKZwR5dYiQTlcZz_b9If6eSTMl-5llrccBgSfRbw_gHqAtV-MFFwStk5ZXEkmpqvIQ6UJR9i6Hdp59J7hLBq0ksfrtyIk_O6V9HEmk3-UqYX6spYH6a-i1y1s1DwzcTHPfunftFu_BcIcJVLEoFet5MzR83VSUlpjuDZ5Uz36sg7ZeQoucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoVVhSjA3JW10z4tLHpxk5bvwDW7odxrNNPfc-8yzhbguvWz6oPZpW3QuZgzwBPmMBFczp5xWOi3DPJNddkUtyBq7UgY5_bG3HFoa0ZgXeMar1rzMzCfKRM7cbfhixqEfLnvPZJB4SvWUSnjCCIkKY_SsxKE31o7gaffITwV4eytn3ubwdQ2mQpAg_tF86wdCso46JC1VmJsHAvqtirbbIdeuJQ2hg49Lqk9_a8ih18IzzZCvP5rDnGhtTTPDE4Rdjyql0UN3QTHtAiwTblCsMVy2hXLOMVBC6Z85jarr9L1lAdaYPaFzFIs_x5mRsBaoOdcJH0-0iP55Af7rTTYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-0Rl_6dbCHDfyl_mmWwPK1MRJEnlDY_Bg1gT5oNHhTxTBKJRX1mkCEKT3DWZK_MxsnU9Ty_IkZR-giwcsFOcgZANJKHMF49b-DO1x7vYiKKtBBMaMt8oKJEr_RCFxg0kbrNgT96xg-6c35_cNG_fz_wOi5n8aJIX4DdrHKN7xlEur5eZ9cwWNAKYa5nu-3-zAxBZgaS5fnXISwyalzTuwqB37fc1aNNr1Zsesg0zl1S6wzczNX39_acTbyb6j4hKn78diSIh9sRb6HWKYrK6UquHyRPjBqTFtcpT_nwbqKohIKKgwjKsnjxcTCq2Tw8SI1ZdTgWtNnjy2X4KQ4mMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi9qm2DXSjd17SHEpe7OgMQN-3Puphxxg4dPwpR8SJClZbqyRuoCIDCD8D1ydaiDW8O0sMX8r8lwZK498k4xSGe-gqczCw0cjd4c4C3Uby5IfKg2tUM862opNIwNGO11H6EqugdvikO4olLOPgj3l6_OThQtWtDPuwiO0O_ZGecTrCvKQSCk5yyt_DNh8SUs0aI2jimq0jD1droShPprpafSqxYdwUzIQty3-apFD06yFjyKi78664TfwD1T8y2RGArYcbh_BHf7HwoznyPRE5x6ZPnjFweVfS94PSz7b3Gi-JGKS1AQYlPP6KXdGTiLK3bViWTcUIPRBAGh4P6spA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اقامه نماز بر پیکر رهبر شهید انقلاب در مسجد مقدس جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667801" target="_blank">📅 11:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667798">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای غمناک قم در آخرین ساعات تشییع پیکر رهبر شهید انقلاب به روایت دوربین خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667798" target="_blank">📅 11:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667797">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کوهرنگی رهبر شهید انقلاب خطاب به رهبر انقلاب: تا آخرین قطره خون بر عهدی که بستیم هستیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/667797" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667796">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
انفجار خودرو در دمشق همزمان با سفر ماکرون
🔹
انفجار شدید یک خودرو در نزدیکی هتل «فورسیزن» دمشق و برخاستن ستون‌های دود از این محل، همزمان با سفر رئیس‌جمهور فرانسه به سوریه گزارش شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667796" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667795">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دومینو حذف میزبان‌ها تکمیل شد؛ گل چهارم بلژیک به آمریکا توسط لوکاکو
🇺🇸
1️⃣
🏆
4️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667795" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667794">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9JQwnNZasI5X8FBi5xACQ9HdgsB8d-nVhVbstdIa6nAUAICsV6XBHq3LSDQA4Y18uPsI4F9_3VdzAbjiGyBhfDi3Jzp0eWfPt-e0dNV_aVtxjjoxTFRO4QoIrP0WhI90QLoPCOHJ9GHiuvhe8_Q5GPqnQXeqviQPzTO7c_d0l7fL2JXBMJf4h7GAbiof74ccXdunszfu9S3tfdrBmuNzXbsJzxPo_yrva7Xovn95rLWBHuC053xu8bUNdvEfWzQIaKtqE3gpqoIjlpSddVYSBykR44nwbn7mSB5LYRbxZ1T3B81N3-wpy2MeGaND8q8pCcagrOUXOsqt75DKsbvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667794" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667793">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9cqffsPNLomArlPwcKtF5F5wTqCQek_-vyMIYNUQPZL0ZogA-gJs-XDs1e2egOqGAS-tfaa81TJ5B9TgqtsuLLfF43No4Pcqhr5wEKkdTBStFifW_2feQuklyPxxq6uK34X_toBgR0RTANt7CUs3LHaz9O8fSHFgoTsdq6klX-xl18WMcnm9pKcGvWqhsvaZcs0DVeJliDVsRtVp0_ce1zAAZnm-KZfDD-7F33t2lzK7TZiTWo7czkOH9bkJan5eRHJ1C2ra11G_QfMaA-uhYpZZQHOp9_N8-_xdDEUh5Vq-55DMM244yDF9Jh19oBvZLz6yUUSGHkpPITvS2Rulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده پاداش بزرگ برای اجرای حکم قصاص الهی
محسنی ثانی نماینده مجلس:
🔹
کمیسیون امنیت و سیاست خارجی مجلس طرحی را به تصویب رسانده و آماده ارائه به صحن مجلس کرده است که در آن، برای هر کسی که در اجرای حکم قصاص الهی نقش داشته باشد، پاداش نقدی بزرگ و قابل ملاحظه‌ای در نظر گرفته شده است/خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667793" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667792">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1B8lvmnFC5_hgOKgvkYT8GFuNcY8Fiq2r1j9mePzlt817DCWi75SUYb0cPaI-HDgZBKNj71MgMgMptChODE983pbex4eKcPzMHBpPMAc3UQPydIMIozvvb-wAo0706dCtdESIuKMFU4Xl4QyCsVDnNfuSLBU7yqo956AfNifto5rEfAfBb_Z8tsfU06Mw3jZ3zthRKPWr8leqYqqIoK6oCiyk7OMzt-RjfeVEeYZSUv1eooLSCfNmDnTZv6vHeDXIeoVhxpbyeEkWJZw_vzR-j956BCH5HxTPIq3_aJL4mt-pwvmJF55XDEnyuBxvkQkjnwLFMnKuEWRWfiGg8ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم فلسطین در دستان خاویر باردم(بازیگر اسپانیایی) در جام جهانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667792" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667791">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم بلژیک به آمریکا توسط واناکن
🇺🇸
1️⃣
🏆
3️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667791" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667790">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
قم تا مرز انفجار شلوغ شده است</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667790" target="_blank">📅 10:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش وصف‌ناپذیر مردم قم در آخرین وداع با امام شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667789" target="_blank">📅 10:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667788">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم بلژیک به آمریکا توسط دکتلار
🇺🇸
1️⃣
🏆
2️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667788" target="_blank">📅 10:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667787">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqgyLipZ014ZEyl66-83-bQ3QtaaTawXi1VvdVSljYPHbuIblDJhIfAuFUHmUbWsxgKMmhaILwvxmLgOUlEMwf6ZMCXyeOHv35aZStDn1wce3oAz7IAN-NpXx5vPk49TQRgKCyChA9pTXGdLNSzNJXGnXFwyFg3sJzeKwvD4WBACSDgqNKVsITOJTNCPSop9YAa1DbI3kHUzvKOr8CrcdLfEwIsx7RNf0HKlIxN8_aK3i7mqiuX0Xo-QLYvLEIIgybZqNBL2cKsAQ_uP9KOVKPYC1lJqkoQ1XFBcvMkXPaCVtgXEL4X79roL_lD9blI2v2jt-BaGGCp8sBg1DMFgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667787" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667786">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آمریکا به بلژیک توسط تیلمن
🇺🇸
1️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667786" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667785">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری به نقل از فرمانده سپاه قم: ماشین حمل پیکر رهبر شهید انقلاب و خانواده‌اش تا زیرگذر حکیم خواهند رفت و از آنجا به حرم حضرت معصومه(س) منتقل خواهند شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667785" target="_blank">📅 10:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667784">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a510abb9.mp4?token=CbTeV9GDbpB-6E_3EWmnF1RcdrEoiywIFlB63DbAHG1r0Q-etKdkyjoJsDdlC4BUnGRbxFO_uact6b8SPjK8q8lS0YBzmJWbJyyQq8Q-_fx7Vv11Xj_wTNN-d7LqOTiyGqB8ukPgSokZtPgqbKUc3feW7s_fRq7pAK9jtEreYOgOpTPlzH74OueMgsRpdosA002fujNxPwGKyJc3qZLlkntsc1Wfye8Rk1vnyZrac9yb91-tq1iCbF1UxxZD95Y0RugaGdy3Lw3HzE4uXsth1TvFhxQS5q3us2CrgCF5WZLXbT18OolzUzsdT2L9XIdfkcINJ2pErFDfpmASKCcKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a510abb9.mp4?token=CbTeV9GDbpB-6E_3EWmnF1RcdrEoiywIFlB63DbAHG1r0Q-etKdkyjoJsDdlC4BUnGRbxFO_uact6b8SPjK8q8lS0YBzmJWbJyyQq8Q-_fx7Vv11Xj_wTNN-d7LqOTiyGqB8ukPgSokZtPgqbKUc3feW7s_fRq7pAK9jtEreYOgOpTPlzH74OueMgsRpdosA002fujNxPwGKyJc3qZLlkntsc1Wfye8Rk1vnyZrac9yb91-tq1iCbF1UxxZD95Y0RugaGdy3Lw3HzE4uXsth1TvFhxQS5q3us2CrgCF5WZLXbT18OolzUzsdT2L9XIdfkcINJ2pErFDfpmASKCcKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به آمریکا توسط دکتلار
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667784" target="_blank">📅 10:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=NkZ6nmqOg7cFR9J-o3pZsXVeuaYaD4Rzibe9n9sfeQsqbo0fhYDkOnWITY_M_OZ568Vvs_Z9DCMzqV1fZG9tOA-PKwFRNDHMag8sEexwPJZZ_iu9qaEOuA-BA0d7slalbPNTcmyn2Rk7opozpo5BDN4Xmgy0pdA7bguzDRXJF3Dx9IzimF9fjZzwwy6L7lUrfP1qeNqbwXaoM3F4ONgkb9_DBTif6pjyX4NbIt8FnaAkkieyNT4IPKzTu6ns2UhGqwBVcAP9HinKqMSsIXv0ahlfp9qE-4K1fVpJrcR6QKj2CLzKUsGEO7VJnkL1tmGyy8nvicNmzyjyOlwq1HhLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=NkZ6nmqOg7cFR9J-o3pZsXVeuaYaD4Rzibe9n9sfeQsqbo0fhYDkOnWITY_M_OZ568Vvs_Z9DCMzqV1fZG9tOA-PKwFRNDHMag8sEexwPJZZ_iu9qaEOuA-BA0d7slalbPNTcmyn2Rk7opozpo5BDN4Xmgy0pdA7bguzDRXJF3Dx9IzimF9fjZzwwy6L7lUrfP1qeNqbwXaoM3F4ONgkb9_DBTif6pjyX4NbIt8FnaAkkieyNT4IPKzTu6ns2UhGqwBVcAP9HinKqMSsIXv0ahlfp9qE-4K1fVpJrcR6QKj2CLzKUsGEO7VJnkL1tmGyy8nvicNmzyjyOlwq1HhLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستوفر هلالی، روزنامه‌نگار ساکن آمریکا در برنامه پرچمدار: رهبر شهید انقلاب به مانند امام حسین بدون ترس شهید شدند و غربی‌ها چنین چیزی را نمی‌فهمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667783" target="_blank">📅 10:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb471b531.mp4?token=uR5TNQoCna-ddCOwDMXUDMOIQp3zbHEHNV7H6yS055LZm4OzPK_ld-oNJ2tFmNUTYO8W2PnJY_O6A-gEUeTd8-IuS2ARKSCUkmQJ5uXdriK_QUFL768F16jGVdg9W4pqDh6tqqOh8YrzWjJXdLCsukbvl7Xld1CvYWpLVZB79qiZid2eHwyK7NoEMDwSTYsY5PKokKXO3bc_-AGRozEpZGsnQLjzhE_qfBntBD2wj2wu_V7y2JhAnkvBJijVnQDUgYYILR1XpwOYhv06k6CR66QOZNBM-29XHbyrJ858geBruR_101zctob7gdvEUfa0mLHCuSCo8H31hi1O8stmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb471b531.mp4?token=uR5TNQoCna-ddCOwDMXUDMOIQp3zbHEHNV7H6yS055LZm4OzPK_ld-oNJ2tFmNUTYO8W2PnJY_O6A-gEUeTd8-IuS2ARKSCUkmQJ5uXdriK_QUFL768F16jGVdg9W4pqDh6tqqOh8YrzWjJXdLCsukbvl7Xld1CvYWpLVZB79qiZid2eHwyK7NoEMDwSTYsY5PKokKXO3bc_-AGRozEpZGsnQLjzhE_qfBntBD2wj2wu_V7y2JhAnkvBJijVnQDUgYYILR1XpwOYhv06k6CR66QOZNBM-29XHbyrJ858geBruR_101zctob7gdvEUfa0mLHCuSCo8H31hi1O8stmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عجیب از رانش زمین و سیل در شمال غربی چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667782" target="_blank">📅 10:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CngFvqLhwQqP7zHTuarbQoPoA6rQ7vAwYYK6H7gfEGME54BgujYf7LFWeNRsk1t7Y6sPiNKmUfXmlhoGS_0tAQ-tSLyyQAOqHCpsds5Xj8LVQ_4nd0Y99jTMsNx02t5qN2ZR5w_L9JmkgTcoT2T1xat71QbL-ExOA6IHpW4zE2-Tis9F9tcOsbUcd0bK_qk0_YRzR7bcjHyffdgAzed5AlH8l05Ry4Yyr1ufzLfKpSIsWbORrzBux6yiK58Mx6m5_0nGDu0iFoh9ladys5hTtvTtgL_JnZn3jcEPqgvlpXrRPNvSJ5Bs6ajRKzO3QBymjeukGAMYuFuVDSsQ3_1Aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQVEvDP3LRXDbkvpPxTilrqqSrdVC8ccB9FLeNcomYGHMt39sfv2dhb1ftJEX9VlzECxVQfSMoyWvOg87SpebYIeIYIzXkpE9qWy0w-2u2SJFwhpWzU_gQhs2YmAwpnTmoO71BXbOwHx6X2sBEGEJ2EYI4O69CCtW4VrQLQvoBQvjMSJISnrR5b6G98B60t6ZR-rPCAhEa9oCSyycwpaGsv6j9rJ85BjJxk6ZXGm0UHurofaNlk4JHGFcY364B0A2s45mqeKLPo_8MScOmjbWWlrQw9lrutwRolPiNV7PVFQsiNRcwCZRB3zCIpDyonSTfcV5rbHolWZMcRC4vP05g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4Qq3IbVaR7JU0pBpwaOLsvIyhowouxtGl93Ez7_83vbIhO4DrDWHOs4m_6gCD3iI1h2LGYV9xWFn0hQ39OGF3HD0hJLNaEE8JfFM2optkiRfus6scpZNXrsmPhe5vGqVUirtgHYB2vLPeSoEcIJTEqfmPcKwm9I7eUhh4RoEc_I_Rm6hpVjK_Xb_iCC1TEuEyV9LUeOIRdl5R_V8-YczBo2SwUnRevqUnH4mjtYzC20sVvu8FnPloq9Bo_9zFG4WiyPbAPUmGa7xk__hKAIw4qVczJfxo_ikjKKhZTJrL77oe8CccFo6_DY4Y--tOL8r3jl9EHGvJ6CQriFpN7Q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARuP93SZKIlKT8E2kYzjcKgdlVLiIFv1vjsFhrQOD5K3jFvrh9EMurreTutuX2Mje9qM57Blk7GBwHIQAsSv8Lx1XyWHY01-lwiAXYwWfGRV_6kbJ8AJkQE5vFIfnKNp6hn6rLHgf-rSV1H2l1ClECRvKyCAbQC212EOokLkLRzF-8b9pLiTwsfEPAZ52wzWgiBJQ0lwCDW226QdeQoqdkUxXzbeH9uZfvcooukjvDdRIn6MxFaa0O4pG06KJn8QdwcsIVhlrWUTxuOg9bvsK-d-5CB1pzFBwb8KhiUUxIZl87FGn5ji3iY9PhNBERA2jWacUIlXjv411M9Ed_Fs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOlYw0ncHB3QfO4_vWEv-JcPWwdlyLw_qnMvgBE8Un9ADG5mj0aijNwAAdysD1KcVb3mXAFuLb7Z4LxbvzU6Ft8E3PMgBuNX8uvAekEqwvchWPnSqt8sov1TJzFkW8opHVadhLYD9J1hpA4VUT9e0e2AQS706M0TViXFDS-f2CJFvguUml2FvGyrXKDCmTwxYB4XGKeZHUDmAQkuLe8VqOP6r85NJ6WdoHkjlczzz-YJBJvCvuy-0gpl7l21NTxztodnX034UIbJ23rbQxmFgljmRbYpu39gfpEy43_s_W2_i6vUGRvPujMnfLFu-3tWrF4TuKKzoJT5DmguRrlifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O05xgr5b-fQNf9z-ejfUtfLYh6BSksR5SOuoEvlJlbXrf8eFk1pMOHc_v26WOtp80nI-jn95I_HWT3v-ImlwloNZ1EnlVr-CFlxcJ_imJiirXsTSiuhFJNbIfCjKG-WQkttBK0GsfciXaNAu4WH0-_TCHIHtkix-XzSA-S5Q4eOcKtdRBMBZvYj9CgNJbw5lzrX6yN7SCQRDRRSZbr9toV44UBNu0Rc0axtTQbonoxi-IYrk_V7FaLMg1BNbwrMlPIU02ljJnlyEWd5RTOftLJ_V3zJmkesAxHan-lCrDy3pLf7mWFKWTFOMElX740tiey0txXQekAUh6EXi0GhZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fy6GabTmnGqFiNIKGROO59eQOhCOOqHoP9xvgQWeEeLfRsITt4o5gajIqJCxMIz1WI6zq0e8nBA9Idv0DV-Kkv0JcE9rRpNgQ0x311SVyyYoNbED4xEvuJrDg2tllElKpqeBFdaJ2bBC9QXOPoFe9ZRu2e3oD_6XzOyjlu59m1yzbIK6ZceJDrLdCfruKR9EqDrb1Y0UE5HTfNFFSO3AhLdETkQTG7xcDou1nl-9zGPpCBVmZ-eMaYg-czVNHCENxJmKyNHBS07lGnCl4U0YPB_Li_4Fre1SLV_NzESPzLSN6szJosWU_LQTSO-9A7ZHqMU6vZ9fRHI9WEsK5evpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEL3TP4T7Ixy9eNA2gjMEYxONk1NMsbZ1yfd-WIrTouannBVR1nshv33-9p0Wg_NZmFtm-7t2IiMySM4EqV0aphtX_sXOaO_kly9ACc3nUT-GKiorkqIiXskxmfOlTD4Y0phOfDClFu5mjtuFiXZlN2o21qfkXIklJuk3IwLwqMsTWL_cehOm8UH_zVoDLbpyX9TXZgrjBCW_VGBVZy6WTBcPjyIv75x_02zysBG6ApEyonTSGgMlI33tBtpWqHDHC47Nt2PDNFzaaXeOdDJmfz9EszIPid8e8HD57nr5KwAhlBU4VDYyHwZRjBnf4ViQhOHkwvTIeJ-oNJaGWZmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cax1AIDDN_0m-JoP2ZzrpgNPCorvl5WpNPiy2ZmGg_hmG4gnAKjYnZke4ZJzSlyJ5qU8CJBnxGotBtbmzbga9isL8kHiVN7EgSbOAPx4SJr7pZFZRLewkyBiul5XBgf0abGOGS3SHpy11Z2xWiwn79nexCuOi219X-HiceO6c4oPWsrX3zauzvTWyVr5WaD3YflPm_zYtq6Nv2SbxFM1qYrD3QjREZAMl691S2o3i-CYs3UTubCWFXe5548Gd83rXIMol90K58YyIpWPDXNMWUCkiQig5beVckPZKNg1bFwghLbzfpu1RhrkLqWz_C_URCabsmkr7jJeZuxAEGY6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKjlKBlVUVGq3AzM3ACASJUH_ViK8qWSXmaKA-Hu57jId9fsB6bQYL0ZWL90h8xQbVD0bQXyBduOhJs-Qq2_cpFlhkhOG_LfREK08GI_m7vL7SMqyPM5OZVk6HDHSaphk24D1-SMHICavLK9j-kadIxLrHRUIhUUApBegjEf9J2eZMLrjSUCXSbeWAkkgquW84LzN6nQ02dqLIvZJ2MBYUorwAipAgAramkom6Yy7g0lGvhoyRq3PZAqxtCpaYKFpZMtYGswkTvYe_NGA_O1laIVh2aFAgyYZBwjA3hXXGXrLqcVX4BK_YCE3vuoHUnEJbxxixS__33xK3ivgjjLKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش «مچ‌بند سرخ»
🔹
مچ‌بند سرخ، نمادی از وفاداری به آرمان شهیدان، ایستادگی در مسیر حق و خونخواهی رهبر شهید است. با حضور در مراسم تشییع و بستن مچ‌بند سرخ، بخشی از این روایت ماندگار باشید.
🔸
ارسال تصاویر از طریق آیدی‌های زیر
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667772" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZkoSjpssCM4SXg4Iu8fpEEM2asKXm2qXU1DuleNP2pZlhe9ogV2AsLM_QT_Xp1OhY3aaQLiCtfATHhZ7HtDLgXV_PgLwTUkK9vHn_VZkUiznwAdlFGFAb_9cZprnGfudyKToWIHBnzO4ApHkHOC5vKMDiJr-PsmgEhD1H97XjSdio27MPDutYn-EtOUGilG4ZyfudHUe63yJuTWjpVTzVUv9V3vuahTI6bpAhNMxNIs6migXRWboNYdSFtQXabFxvoxPkZ6yN2r_zumEu3ETaXAjJMEyj-C3_nAkI_NsEPAduQvUOzoFMftQ3-3jA0E6usbZUC03N6eNdpN6RxDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه صفحه رسمی تیم ملی فوتبال ایران به اظهارات سخیف وزیر امنیت داخلی آمریکا و شکست امریکا برابر بلژیک:
Dance with me!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667771" target="_blank">📅 10:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667770">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کنعانی‌مقدم: مجازات ترامپ و نتانیاهو، تکلیف شرعی و قطعی انقلابیون است
حسین کنعانی مقدم، کارشناس و تحلیل‌گر مسائل سیاسی:
🔹
حملات منتقدین به عملکرد دستگاه دیپلماسی منصفانه نیست و  زبان دیپلماسی چارچوب و ملاحظات خاص خود را در قوانین بین‌المللی دارد، اما این رفتار به معنای عقب‌نشینی از خون رهبر نبوده و کاملا در راستای دیپلماسی مقاومتی و کارآمد است.
🔹
هر دستگاه در جایگاه خود منتقم خون رهبر است و نمی‌توان از دستگاه دیپلماسی انتظار حمله نظامی داشت.
🔹
پیگیری حقوقی و محاکمه نتانیاهو و ترامپ در دادگاه‌های بین‌المللی وظیفه جدی دستگاه دیپلماسی است و این دو قاتل هستند و از مصونیت برخوردار نیستند.
🔹
شمشیر ذوالفقار در همه جای دنیا بالای سر جنایتکاران خواهد بود، همانند حکم سلمان رشدی، مجازات این جنایتکاران یک تکلیف شرعی و قطعی برای انقلابیون است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667770" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667758">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAW9IsmTPwIKjrG8j7HBx927w6g2wXJ-nXgLRno9iB5URZcR0qM8dNCbWrze5-MySEgasovsOMl1d4ISLgsXFbF0iFn8lEo1lJVinc5i9wgKS6H-9mwhqyV3Q75n-qAGCNHWuQWKQMHH6KOTLKexAk3FXu6IqyXVQXQWUmQrtyVwZwOPZkT7KKVpND_0fVlW4h3mWFsu45P36i9E09auqYc5ZinyS6IemIiCNpMD0Qrr2SVowoGsTnGHJcl1XYSyRZWGzjGnGvwEMHNVVTHH9TKbpiFjPRWQmpFwlXMQ06Y27WqK4HbKXxW62pG0GwHSEXIdzZ8RxyKuPPXdKkQsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfSBZ0fCeAIs3e7C7Y-7N_Tr6J96mv2qxcefl17y_3aIwk52vA3IhHWHMDimcx_iIQy3c0auMSQiJJ_9Ruv24v6hMyLFo331epj1wxAkgoA-SRRJdhhUtCYj81mZedeJf5KaH_HrPMeSJPAOOoJkiY-jUI2UQhaTSinCRUbCYhMGfUlqG_mrQXrmKOg7EPvHLDw-vRDNyHlhHZhe1TLn2mrP_McqsjUxUNhNZpYrEw7tToyZQJJDwSzMstyU6NbRLCRC3Jl1qpPonyyODt9uwEucOxNcZqfo_p2ihDXNmAtHLbXNKruv4wCs-BFAiatsQovfJ2uKFU6Qb4McCpbSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6rku2IZ0RQic9I5gM_1N5ltYiAS6Ht5YPwZNWIL8jHHG-Pzhi2LN0I5_2Q9qZH0ROO-WqCIr_Nplts0w6k9QRvKKfDahOnOCQ5948rBLT2oAY_iY_7NKcWq5eSZunZUeqX_2LR1QFrNF07SV3bLdPq8jic9O9UpkQcxvdqWByOcRw5gZNV9phLaB61emsReWcbyriEc0XslMI9XsLHLlx6cogt5_mZRqQomjhPmyNytI35WYIZ3DIIUV5DrjiFBg1rCXiqZCbF8WLkl1KyO_hppbQx3K2Am9IseqDuAZUGsMSKXAz75LBmT465nguCoaCvwbk6k-j7ESdcq-kPsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V50WVTwndWpneWSt6RRs2M9Xjt5mEjFx3O6esgLQift-n2qrnQTWR6TwqpRaJIdGMsLzmOXqF3RdmFuOWzQWsT-A80gPA7FqkVGM9LsBh4iB66dxniiNOS4xAnYXYEi_Qshyf6aTSBu6U0U_gHTmvHmt7X-ZvNnfC74DyrulRoTGSC-spZ6KO2pjloDRCzv243BHNt1euuCLUBhtUGgF_xaKBDPCTH00mAlJ9TnJiGz7ns51Ic6f3r_QbxaS8GwL-OtRH61T3UiYrrew0Mj2HpTGw6lbbKgx0VosWQQVOTmsAzFSCXlQtgSWvn1eiQxDSMUclAqnra4JSFiN17G3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF-LMUYb8JXvDUNL09eiGyNk4hG1uFkNzYVO7QrD6caWCJTTX87exBDgnDgTp1ppjcOjDtNoEkXZQj-yMYka_pacIj114qCZnAeM6YtlpK7L-AFLNDfAQBTceuSUGeGFIY_KYr8962yibp77d9qvqYVUEeRSuoz_dBpKk6zL74B5yml2-6zhHza7nE-UEzfb3Czn_iUrt4s2sIBBk5JYv_snFVLEvjcw02e3LI6VPrYPWrmfsPzoad5YQ1O8dxSTqtqHM6FXEnmJn0Ss5C14NZo5ndM9x3EJ-yRDuxwS5qfYryoyxu8UxFL-EQiT3cqklGmYoHufTH9p_8Fliyfw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxRGlmUszOcdJ9vDxpwSfuOGdUxnaOhRCqWnO0tOjtX5hrSoYltcUOgv-RRSUXqOekdzshNTbY6Oa8oqD288C1NppK876OE_-6sMJPt3hbJzqMLnDQg4qyML1NXnX_rUWm8mYVycujasMX4PKWkI3SF65aI36lgvrAzZNo3Kq-531j6W_bkzdMgpGOjTRX77PDmTsuLsS51jRbbpmTl2sGzlNhzLwDpLh58Z1-00Gxv-Ohn1XvjCRB2fV1z9H7UNN6TfeUIJDo4BbshhRP-_Bgm7zE0fwpAiem9-iSE7W-qErxwJ0Uy-Dau22cMS57r7qGNA2ewoG-KdODXH0H8dZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk3mN6kZKI8SsltCHGc9cWVD9Kkjtbs4ZJWaui3jNnIIRyUoU3i5gDGGFpnee_M1Z-0scaoQHJRTu8Dhxv3Spw5LyA9SMEzRsX2S8wEf_y1KRiGudOSgjRalZ1TTcXq-RKzzkNeAl6BRhivZUrTATG4YDO8U3cJn2E0KAHIVOFnz9YA5widjfq9SR28cA3m89LUg1ihqsw_yDKQ6WosRHRyH7HIwI2l0NbT4mlFcPQ5h7N7Qc3eoLUhS3p1Ez6Eln7nRDoDzuw43hwlSgP47kJ9eXgUxz7NB82xklvv628OPqyVEgUVBsBDsCFc2FQA0FuD3qbdr3-86okY1TZn8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrovyh72sK-fGkIWgMYAxHPZtB5AH8r5pXxdtrIE2FescVKTVuYPn0ksyBdn9YOoVzt5HZyvanbsn_OvThgC_VyDWXyid3TtnWeDXpP57rxhQJ1H8pCApNP7atKFnkVRuctOvEVk9QONzF07JDnmemTgLh5dFS-FnkRkpB2WCTfFg0MH14zZzwhXxKkOaXbniQSNIpC6VDb8uXqmxUVkFTnvJuKirWR1ePm2AoEKM1FLDwY3jsEUAwrct7EmhqU5Z8znLYv_mrtoRJ4bRQ3e9XtZRGU67lYvzt5ILExYBgdBpHhB015Sd2YcYjvykQDCJ6NMLkxZbRMO1MYSNPU0EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای تشییع پیکر رهبر شهید به روایت عکاس خبرفوری
🔹
سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667758" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIBEmpD_VuTYsx0vpPqYY-jGC16i4rLH2v49YMMhZ43ptq725gYHBfLj0mUY_nCWQ3IjQ019pSIyQWIfxg6aqLBuFphCDfN7cC4HkC-AMiGLVtwPHuBLZWYl_cM_D6nZ3TAvgZ_V6DC4UYZPnKZBZ-i9MmmRZ74qeHEb-EVkxthanXPHkcl9b8j2w8aOGYjE8054TmtLUtfEo6qfeWENu8Wr8JOArqpWLMUCwhUAaRyJN4sq4ShhVrcZwvdSRRPOAOmCSbNNUntdeUgC-aajBpaSU4JgW6kflp5olRuh4oTXSwGWn6l5UxCDHd2p3MdgjLAG1KFBE_BISf5O6EIYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۹۷ هزار واحدی شاخص بورس بعد از سه روز تعطیلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667756" target="_blank">📅 09:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f8b7cce9.mp4?token=tsf8qImSqaU9IVdK519BFeKzvbrUjN8oDHDotH_mPi9UApBjEs9uZN6mX0w4sQ1dVYp-X2i_ivEwv3TJ_JdK-YXlPjsVNv77PdG4O2ifjyGCwvNwQ2oJPIwxwS3xpsZ-2-yAfnKAO8LQsWP6t4iDYTCFh0D2jyNcDtIthI9mzEOOJXQanUIp--XsxEXbw_3SLhtxJ4YBzUAWRoAR_4b8vrIGpU3Y1XZGYbJexhroUVniOC8OogL0dDmU6naxbHKIWtc3MbesATnJuPYk4NVLZVPKBtNR9UFoskR5gMZFhWVVZF005AbC_a6cLZcnnnOdXp_27V1VhrzHsMmtRaofuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f8b7cce9.mp4?token=tsf8qImSqaU9IVdK519BFeKzvbrUjN8oDHDotH_mPi9UApBjEs9uZN6mX0w4sQ1dVYp-X2i_ivEwv3TJ_JdK-YXlPjsVNv77PdG4O2ifjyGCwvNwQ2oJPIwxwS3xpsZ-2-yAfnKAO8LQsWP6t4iDYTCFh0D2jyNcDtIthI9mzEOOJXQanUIp--XsxEXbw_3SLhtxJ4YBzUAWRoAR_4b8vrIGpU3Y1XZGYbJexhroUVniOC8OogL0dDmU6naxbHKIWtc3MbesATnJuPYk4NVLZVPKBtNR9UFoskR5gMZFhWVVZF005AbC_a6cLZcnnnOdXp_27V1VhrzHsMmtRaofuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو قاب متفاوت از آیت‌الله جوادی آملی و رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667755" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e919e965a7.mp4?token=tOBXaceWlK7BuKr1V0-uiDsyoRpFd8dh-HXtbNwBrMPpm0G6moxqNj4sVhRJxb0mbSKhubxQEVrK6qQymf2fjNLZPJm5848sgEqUunmFdn-uhP3IKY31H37XUcYF4eOHrUWsLoBDRstVg1ufhgT8bq6-y3GHXMj0bdKj0FXcrEw6yJt7Wy4VpMRh4RZxjT93ys7fsJtTBu9Dtmv9vDI9u19UyxVgkT5MCxzl8GyHl3n7pPjY1SEnpaeHfPB11aAYQoX_q-kBmeWoN4XQ5GHcyBxv2SqnW4JwNEC_ZM_Yie36ysHfSNuzEa4VNo5sZTlX-4t_lCrc--1jwcj3ha-gHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e919e965a7.mp4?token=tOBXaceWlK7BuKr1V0-uiDsyoRpFd8dh-HXtbNwBrMPpm0G6moxqNj4sVhRJxb0mbSKhubxQEVrK6qQymf2fjNLZPJm5848sgEqUunmFdn-uhP3IKY31H37XUcYF4eOHrUWsLoBDRstVg1ufhgT8bq6-y3GHXMj0bdKj0FXcrEw6yJt7Wy4VpMRh4RZxjT93ys7fsJtTBu9Dtmv9vDI9u19UyxVgkT5MCxzl8GyHl3n7pPjY1SEnpaeHfPB11aAYQoX_q-kBmeWoN4XQ5GHcyBxv2SqnW4JwNEC_ZM_Yie36ysHfSNuzEa4VNo5sZTlX-4t_lCrc--1jwcj3ha-gHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: پیکر مطهر رهبر شهید وارد بلوار پیامبر اعظم شد و این مسیر به سمت حرم حضرت معصومه طی می‌شود و بعد از آن به نجف منتقل خواهد شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667749" target="_blank">📅 09:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993310a40d.mp4?token=X8wSJ1Lw7JxkfpGCOoihNhheanGgwRup1Ne3z2zNDacpF5AEbzB0OAieFJZ6g14mLW-rOKTWIpp6fP_4W8ke5uXik4Y6pn20mPAG-4dyX36RSE-QDzkICmrxuOIbccu1SBTgYmaON0AZ2_4S_dLBssTcoLisFNYZV9-AAKd--bOjzNJH8xBTOQEa4G7OHuAqZOqxXMmwxF5iMVc1NGP1Db74CLciVvy1mPWx5JA58L0QXC0LFjWKHa58PhQWtvw8v7gOpG3_ah_SnxDEzTCjrHAm99E3O_m3H2g3G7Bza2kDu1FK-1jJsbKv-sgHJlUH-t5XyCeh4P1-_c6-6bib_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993310a40d.mp4?token=X8wSJ1Lw7JxkfpGCOoihNhheanGgwRup1Ne3z2zNDacpF5AEbzB0OAieFJZ6g14mLW-rOKTWIpp6fP_4W8ke5uXik4Y6pn20mPAG-4dyX36RSE-QDzkICmrxuOIbccu1SBTgYmaON0AZ2_4S_dLBssTcoLisFNYZV9-AAKd--bOjzNJH8xBTOQEa4G7OHuAqZOqxXMmwxF5iMVc1NGP1Db74CLciVvy1mPWx5JA58L0QXC0LFjWKHa58PhQWtvw8v7gOpG3_ah_SnxDEzTCjrHAm99E3O_m3H2g3G7Bza2kDu1FK-1jJsbKv-sgHJlUH-t5XyCeh4P1-_c6-6bib_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون - قم/ حماسه ملت ایران در تشییع امام شهید
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667747" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upswYnsqhr2nbpdlK8Zvb9QoFmk-2h6KcsGalTUJRxrFTwODN9jlksEvcKhTurAfCW0zBtcRR8m4IBl-0EQWhYI_YwJXTypTeCRiAQksYL1oDzVSAXd-vt8la8sSEQsEtVQbJdLjMiB7qPMUxYRVXIsn_6DeN-6XuSpkJSdh_uP5j_7hJsCyyLGrE0xAthKfB-V59ZhzSj59ayThtsFEKTllAAHfIb_7KBWm-j4KyZgPrUHqfi_MXtMMz8VoLoFc1eeCwugM3kFLwXQaXJDi_RobZ67IKYocfG4W4htdPKjwZcWJIdHMXq6TxyazoUvw9UDqVmmVXaa6QKQPCs-U2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش صفحه «Troll Football» به نتیجه تیم ملی ایران و آمریکا مقابل بلژیک در جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667746" target="_blank">📅 08:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAWaWFIDUihP-zhYVyWyaxfY9cmqlNWWCpSXr6HhaHYFS9wb0-tMWHQdgokpFeNv80b8Tg74lcrDGhoqDJ4FJu7ieELuYpsIB0hWbOwP55e16jYYSt9K1AK0MOmhVBcguJLIyiEuusq-8ybFNnEqusgdBvIBSiAwv5EPFhhiMZlyawkoeCZ0PWfiQXsIyiegjrQpLeDjaFseYat5RIm9UjPJPLtR4o1Pfvg8qHylQ_OoDXjcifstBJ0n2N9FkYqcOS5fru3sB-n7VL5MHBUGQlOOHFzjapgV0heToAYqKbHuqL0FZQnpp9rszhFjZuY2Md6iK2tLHgGmh5RlJaZz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4GAK-35bhgIi8gu94u0EQ17PpHRyXCa2nWRdMytaIWWS7ClwJZEGb03Z4nAz_7ZqaCZ33tVyOJxP9ru4uIaNewu5XMJwt3pAyhaiGD8OY9gTS9CURlv62iQ1aisVJaoOtr9LPgEozUrCsUpfGBxK_J3x3HIV1TslMRp65ttY9ZHzKISF5YoB1VeWF5DBMoWxktFFy_ahrzqCZ5jLZGV--Rl4yxoOxJWUTA4FKPHMZQEUjC1u1dJk6SsRJ7qy-p_3Ud13l8a5RpYABxa9lF6TaIXOTj5GRDORHGZ4J22tKlFu_jj6NZlpFj1ujoP91jANu6vB6Tp5VLfpKG4DiXIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHFhki5DJ19_x65P1PoXW672VoGi9T3vddrTiNaMNd-bUDC76b_Izk1R9yCOYK54NpziOecydnH-c96fppIv1BYKqfax5Hnq6NRPqCi6USjzct2s7fm1mxKuKSGK4b2T6MT0PJKkc1JCym6Yx2V-z9eBxvtkd-9NoWd3nMWlOrfK2HfkG0Hm4u5sflq88B88Brm2BnqLk2WiumMq73jAV5iQORWu5fWJQ4MXsUqnBG-Hz53kUsTs22vWvStk7TEGwO4AiTjEmEfdJEU18HmT_MWWWmFzGpT-TShVxVvkRpcvYXOjoiUxCRJOzN9-TZ5ucGhPO-TykaycSh-ejXBCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUYQBAo0KoEisX-nB13fBguf9cnzORZM52z2iQbB_2mWM8040Jw4BjXk6OOFNQS3as0i0-_1x7PEf_paiAKzDwaUjhMXqqVJobG2iIoz_I40kkFNrCW6t3uWxzTedW_Y65aO0C8SpfgOw8X5a6Hr4m_VXGSEkAO751-6te0eKLpFhByxgYDsUPWZj87bnJYncdap0Z3xdhnk3aj3v5K5KJkWvhYJR4jjjKKhXsgmnqithIF95u3IbiIEVYxvZ6k3mMSVaCWtIUTmKFrJgFjeLZV9BhhqJAxZ_pZ646DuHoA8eRpYtXg8vHSW3ArkRT8wmn-f8K_-07G9EDMC1peCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0uDlX6PVJenTYAO0TjmlIJmohHWhEL8HPRMT8WSSofcCcFRM-D20yt8OmRNiVYYOr49PNGQqpXKEvShJvNSq_GYOmrpgW1LP94iQ3GNb7yqjU96HcLuzJheUIaG9lvhxXOLLRjJfOLoDJceB0yPc2vujLwTxb9XSqDhgWEOHfaiivN2LtF1ZwLVDQadIGVrjwA4C--_WosOIRmXEtJlhBnO9b298IxqjXYZfnSj2xPPlgkk_pS5WoqAxiWGu8tFwyS5KbB91cxw4kT3GjhlkuZROMUh-2k5LXzGpFt04WUYExFCnr6AumXt9VV29mUdNfgIDQI8v6e8TlwIbSJoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFDtd8zACvv-Ju9Rr5nEyDGBM1XFMZXpnXikmOcS5yTXuhJ5wv3iGkN2eoCA7kdpE3gTT5ettw_ML2PE-qMiMFbmSItokATjiaPJHJGu5E_QSV6Hmt6QdUEWNHm1NjuDaFmrn026khB7L3TFoMZiIzWSG31DrGnEyRfQkQZE-w-l48DeXsKmQ3RDneTrmzV72Hlt7auVWm3G_nZUfstfUR191MLt3-VfTl6Ed1jQyIQ7YA_Uavkx4hsG9tgvZ6fDBqZZTeMKcWXlJJLFkOAQ2s7tRGH8Yi-1zesgoNfo5WeqANOK3vqn9rsN09TeLrBB81e1zOdYFAQMFrzli1GJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObDyQ0wsIa62w0EaLHXR_rINETGbOqhWZligeeE7UtonB9tj10Mu3_8E12VHOKW56Zz5fsztaIacgqYelLqqgJSjZTAjFSKYqXPhwHghmd4yGjX4lMCXguhw9F9pHyAC-h6t_s4HTn4tu0K-9Gl72LxUlW4J0_GE1fSpbhl0Ey01mzotNVNiKPsmZXYzDe_7VD6_ZdsBnMkg9BVSnUKZ5BJVBByH8m7aORQ82O7FTZ0WVE-MnB99nLzVJsP0gwHWMTK963o6KaBiVIJWoitevUezvS480h2OmGBSykRlGzTaNG704q-jeytckiIk2egcmbWUKcyD_H_F9PFZZluriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7Eu4vMGjaFc3MxyD4pSIRXutmQ6oT5tVzmYJbbQe3vnUPo9woBPqevMo_Sh6HBg0sQ_GcpxFhq-xZlxoGAvdzgC51_ldF5b7luKjSs2YGeICjtFuKAi_SJFGgVXZ5fd8_C3atw0w9H4N_N4FPw8Zb0Xacgh__pF5CPd_ALXZI5qIn-Pu0Il6IeqsgL9GZ6JANzkFljlVfm_OXqMqEwi_sYk6w81U5GqlRU6xSDjB6ZyXQKdd90-TOCKVDKHceiYiguoYZO2P8erj6ZQ878PqlGY9qBhv4cZcNqIY80tBkSqAlgjiLREBTblpHYW4X7ewHS6OWYV9HTUs9Dp0-mP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب‌های هوایی از بدرقۀ امام شهید انقلاب در خیل عظیم جمعیت مردم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/667738" target="_blank">📅 08:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ab3e269f.mp4?token=mt80nJTlJ_5bgkIYYmEY0eJ6n1pgLHLKgEmfDxvI0wQWVhSJ1pQuB3sMfEIOG1t4Z4o3pRCgER92Wlkb7oJXzQKTAR-WYTByHP1f4iumuoPZH8jYW8Ic9t7cCuqwpvgjWtth-mdit_o2kA8pIzS6B5fn55oyoyWsC6d7C4kwkptCY6ZLJbb9kj58Al6LaBNNV1yYl-8zjj4i4se7uN_3lFbFULp9Deu0sRNqs3AMA7p4c4SSeGiN11ldz8grIO1zu6W7isHSQWI48a5OLinT8lcXQc5xSzvWWxft3yvLLwb9Q6fi8xZM1vCq0NmGoNhHAQcD_e2HW3gk5snEefIKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ab3e269f.mp4?token=mt80nJTlJ_5bgkIYYmEY0eJ6n1pgLHLKgEmfDxvI0wQWVhSJ1pQuB3sMfEIOG1t4Z4o3pRCgER92Wlkb7oJXzQKTAR-WYTByHP1f4iumuoPZH8jYW8Ic9t7cCuqwpvgjWtth-mdit_o2kA8pIzS6B5fn55oyoyWsC6d7C4kwkptCY6ZLJbb9kj58Al6LaBNNV1yYl-8zjj4i4se7uN_3lFbFULp9Deu0sRNqs3AMA7p4c4SSeGiN11ldz8grIO1zu6W7isHSQWI48a5OLinT8lcXQc5xSzvWWxft3yvLLwb9Q6fi8xZM1vCq0NmGoNhHAQcD_e2HW3gk5snEefIKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از حمل پیکر رهبر شهید در کنار مردم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667735" target="_blank">📅 08:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA4PDRDwxWyXWFf5oVKkMzYhmFQk-LSpolXH8EPiJaP8t31g6746ooEFA0VIQ6PcBgldKxGYxa5-PQTGvbn2mwO3H7PFUYR6rY6P-z-H5MBkH6uuU74aMxaUbg2gNaRJyWGUtpeH_zbrTJZgJRwBipoccGIo87EGNh0dsmr45aThgNnuG8x0dZbkiEgJ4Ee5NTLWgqxozksn4YG05e0Ku3hmlYWJ_tO9KFzM5ORCbjvvF4GXkxw0gA8OHFOjybUq5ouhwPwPVQeAIUfMnVhjF23m91l6gSiNFmlo4orXOqADn9oXZKcKnQppv3MDcC1C9N6VMMP0bnouQeOZ-kp1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: نه مردم و نه نیروهای مسلح شجاع ما، از هیچ تهدیدی هراس به دل راه نمی‌دهند
🔹
میلیون‌ها ایرانی سرافراز با وحدت و همدلی گرد هم آمدند تا به حضرت آیت‌الله العظمی خامنه‌ای و میراث ماندگار ایشان ادای احترام کنند. نه آنان و نه نیروهای مسلح شجاع ما، از هیچ تهدیدی هراس به دل راه نمی‌دهند.
🔹
بند ۱۳ یادداشت تفاهم کاملاً روشن و صریح است: تا زمانی که تهدیدها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد. به امضای خود پایبند باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667734" target="_blank">📅 08:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667727">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp6N0_Rzeyg4-VomKVki5NkI0hrB6VfGsGT3v26kD_Pu8hsHFsRi7sEaUVt4hdtZXOAQLK74h-7lRULpgCqAi8C6zyTRDqPJltyiB6vjlQMRYaEfujikt8gkAvQpvxo4QjlhCh9PpRmmQ9GE4Z5XMwW6cdU0z8GfkBg1jlbifoyTpVPbpqsQPOhyMaDhInK1tNHTBYTnBAguaaZeR_XGtFilX9X7gi7_Wccax2phOQaHSGC7YX89c51Sjr-WO1J3XSlng6HEiFMbmdHmrVeHgJMPU2Aba1pCLRrNq8v7b3MHtg-VezUVRTONzaGl94c0Ro1OiA0YMfdujXSySpTiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667727" target="_blank">📅 07:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
حضور جمعیت بی‌پایان عاشقان رهبر شهید در خیابان‌های اطراف مسجد جمکران پس از اقامه نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/667723" target="_blank">📅 07:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inpxhuUydXVvZ2lJrU1upEgCKE5KFinc_FtADi76OwvHRsCaZRChOHHSHHhuwx7JILHc0Q60InIoqC5nJqvTQOGkT3t8nGlIgJJ92ECucNNArtxj8hH4KpIjErmqq63Iivm_MAtZSiwS0gVMHv_y1HWZ9y6smRR-AjKxzkKWNkMBp9OBPo3aoOYBbbvHIkow9rkK48oC0z2HARaHVS0zpgHhcyrvZTIHXes47L7bQ-9xWhoD7zGNyLVOVt3JESaEu4XehF5EfdgDdMI6Mw11bh_A4UqygtoFBeJnSm929u3nDy_TJhmv2KJJJnpo8fn4UV59MTMDabRd7dtaDJx8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی دور یک چهارم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/667722" target="_blank">📅 07:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhilzOJiOlPuYhYZc7suqc64DEH30Y_EnBmWKRFHVDI9G3jJcFpAqdxPqOv8JlxKjOJltH2VSgx4nc4Nk6_Gk_OtR1Zl4HfTINAh7h5kdu4ptNNhn4ZWmtWroewCtS7-2UMsprqG3BwgnLrN_TBfPMjUcfvqn2dL-FDYXMLZE5luXwtO4jzaQvFKX5edROnuzz8qrW_oVI4qdHIhf8-GjAWniOxgnEvQWiMhQrEO7d5WKg8r3T3fwj2dfYfAfu468ldzZM8u86nWOo0thjZ8-sevudkpv1gQMrZrJMLPV69aqTCprOCE3SqnFhtdfih2FiIdldsN7aGfiPBv1JAuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توییت صفحه «Football Tweet» پس از حذف آمریکا با تصویری از ترامپ و اینفانتینو:
فوتبال برنده شد، سیاست شکست خورد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/667718" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از سیل جمعیت دلدادگان آقای شهید ایران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/667716" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/667715" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه حجت‌الاسلام هادی خامنه‌ای، برادر رهبر شهید انقلاب بر تابوت ایشان
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/667713" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667710">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع علمای قم با امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/667710" target="_blank">📅 06:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«محراب جمکران»؛ لحظاتی خاطره انگیز از حضور رهبر شهید در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/667709" target="_blank">📅 06:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667707">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیتی که انتها ندارد ...
🔹
مسیر حرم بانوی کرامت تا مسجد جمکران مملو از جمعیت است؛ موجی از حضور که لحظه‌به‌لحظه بر گستردگی آن افزوده می‌شود.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/667707" target="_blank">📅 06:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667706">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین انداز شدن صدای آقای شهید ایران در مسجد جمکران و گریه‌های بی امان مردم عزادار
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/667706" target="_blank">📅 06:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز دوم بر پیکرهای مطهر خانواده امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/667704" target="_blank">📅 06:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/667703" target="_blank">📅 06:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حضور پرشور مردم در نماز بر پیکرهای مطهر شهدا
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/667702" target="_blank">📅 06:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعاهای خاص و همراه با بغض آیت‌الله جوادی آملی هنگام نماز بر آقای شهید ایران
اللهم انه نزل مجاهدا موحدا
اللهم اللهم اللهم انه نزل عندک شهیدا
اللهم انه نزل عندک قتیلا للاسلام قتیلا لامه مسلما
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/667701" target="_blank">📅 06:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تصاویری از پیکر مطهر «آقای شهید ایران» در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/667697" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667696">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه پدر زهرای ۱۴ ماهه بر تابوت دختر شهیدش در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/667696" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtoxOnsHaOMvnZbh7GihJf0NMCCPgVEDvdAbn1G-eeRjdGS8w4uHnO5rZHUWTXkhqx4ymTFoe0eKk84eQIp5lLOZ-B--yc9EYkWm0dcjj2dNH51siUqBusEH0tXChEsfPISZ5SaEnqr8X_BSBBE6_wySSayciMBz13hyBVRD2QOCe5yGeEhkx3Sb3-5lOpmIdYygUpvGmHIQIrxAB_wxbfYgfwoYv7iFbAQE5_qYDoacko99m2pZZFle-A3OcxRQQ4WDJN6eS_N-4FH6ybZJcN7bzeAA42lT0v-uCA3Jnldp01190St8RBNqTPrqMTS2btXe7RIe8bMJWvp0IMP6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۶ تیر ماه
۲۲ محرم ‌۱۴۴۸
۷ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667694" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV5DoRVyfLQvZIB4d8Lt0nXz33vAeEpDZUk2fRTJKPzOAcuSyRGOFfHN6_U-HR3UVcLuLCWLi0IBxVhk_HykUINKEjbO2_UXC3UE9DYlvZ0ULxt-PhigWx7Gkza7zBh0uCUeZhGbO9UGIpAqdF3tjdiuJ1cnfLPgKXEcsjLIOazLNMgEcxSkFB082B0M2_-LAWHr7vOyOvH5-uutJTHxkuxPXrXDuTuIzRWIvawd68EVtoM-_25_zXfVcRqxc2dOcGthFWz7lFaqa4aZ6RLc-hAYBkBygamdk975PTbUR6hbAtmx5swnn-1zO3KHRX1r2vPSH0VMdbRO6UcwgK0d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عما
ن
سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/667693" target="_blank">📅 03:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از تشییع رهبری در جمکران؛ ظرفیت جمکران درحال تکمیل شدن است/ پناهیان در جمکران: مسئولان در خونخواهی رهبر شهید صریح‌تر سخن بگویند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/667692" target="_blank">📅 01:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل کتائب سیدالشهدا: هر که آرزو داشته در مراسم تشییع امام حسین و علی ابن ابی‌طالب علیهماالسلام شرکت کند، امروز در مراسم تشییع امام خامنه‌ای شهید شرکت کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/667690" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZxpE1o-UF-CO1Bsp3rux4zNEnh2z-EKDM7c2ixuQngE-wxB1gqLgCSKGm1n5Nr_Qn9pcVZ5_-FkZ_SeJN0qXYjuSsPLDcbPFsIJJvxXJdMgyqDamt9Me53w5cnL_2icTpi1-wSCvmqze7ENQiNSlp3UA5FMAOnSXR_WQycpDIGyjjgIdZ5hujiC9bh_otyiLNotqKk5wwWjdGmxyFemk1pJll6x2IWdaA2kc6foyU2XYLqrpHJQw-MLsX2mjK-Yo8k-SoFzcppz5wUqq9cy59GRXxS-iMhshQ8WwJ1oBCOq_EMBz8QGed-VQBqic2a9MgTa1GdJQGHekmrvk3lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
🔹
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/667683" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ نمای هوایی از مسجد مقدس جمکران؛ ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان  #بدرقه_یار #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/667680" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
آخرین لحظات حضور کریستیانو رونالدو در جام‌جهانی با صدای عادل فردوسی‌پور
🔹
وقتی برنده، تیم دیگری است ولی دوربین روی افسانه، فوکوس می‌کشند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/667679" target="_blank">📅 01:13 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
