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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
<hr>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/et-fccib55eslOMEVbD73D4-Z8-sk9HrN5QGPetS7Sgacck-K3VwY6xkQ4lXJNzoExH52T5rHRbhh0mnE3vGyhW3Pt0FaH8yHOfxyVaEgq_VOvOLhmjOt6G7qEzOHgwdMTjGpB4c2IcbH8UWVSLIHGwkeLQap8pFooiPvB0HEsN8VPfmIJ2ek3gsvL_Cvpqw2uIHLXDNtMHLsV0rYYDt7l6Y6CTr0k_dN9WzOSHi9K0BqN26VUUPaH2WDD4fUZ7CiAO-Y-ytwc1lqWCnr_9paV0ICFYLOC0G9U-e-EJHEvoZseUIcEBKP60wn2HZut6470ic0m8IcPB5x9XrTLrLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBhBfOZ2RHAlWjwbjxviJYLYlYScUGXRiWGPYRjyuJfkJJwjtEPeOFSakrseImM-rcX02dfi3QiSCHgYtAPEE0cy3mipNpIOhJ2-Rgw7nntcqy1iOa5_YcbMxGRYaNZ_LSbys8Pove9nkvu-CJhsIuEiVxL5NaVS_oM0IzZiUMTvWw5KFIhVJ2e9hbBAK_p53_21Khq7AXkUFQEXRpQkvBb_OKVHssoQLmPeU1ZD4PJfrx36ZxYlhNNFNbSbvsKZ6ryGW0MdoZZg1TX1QHsDCDCV4teYoq6vGBaQjNFJen9ngw7w4zNB3yxDdJIlZu7xOgnk9caAXbrrg0tcrHSgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5tshjScOqoxyy2zCmi75fZHUfeHJTjRbOC2GRgs57mnboHqXA5Ha1b_-fSYbuk76EnfqI3VCKMsIWbkg_pi9CwQ9CFAfaKn7OZ7_BiiLmcR4Bj7MIrRfvrLYmojRHbFupFfS1oGIB7elrYF0WS_yefprvILM2_TM9KJDxOF1gITNXLex2pQ4S6HAnwSn6p6ecu744XI3OnPuQ3S7tztbhiH-jxO1mmSRDsG2NZe6O7qtlfjZ1O57-TKQXKr5AIkWUoAbDVMBXbUAPq0uJEYsgVVWVo6RV8JoPJPZ3HzIXu-8JNDtCrKI74v2Ee8g4r8KbUEyZTLukBSKagwMIzxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcBBQOU50mu1zjgPoS_TyHADiTZjeR4N2jT82_U1Riz5kIVa_JeGOMTWmhXxl4nuBz-XyTEVUZAxAvlBs0TNDssbvPQAli9dLh7dkfN2QjqS-fY-qNExRNR00PCp13RFRGbSU_G_jmyQorbIQJJ-_rQIvA2QD8ECOO8PUELIqaDyQ85zjaXXcfCKpVbKjuLJ9bGYsHAqstBcozJrjWhsxvTZQgGD-rRIsTHaEa-1aWc4-31ixyRr496pAu2lZL7psQ-wT9k4awoVRrj5sYNjcYU2WKTdSY8fLT9PGZQaiOWLea2PABjIolTVTbbARlakPqk2ZbvXdNm_caM2m0tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOBjBZ5BgCF9Ly74FCMz_P1u8e5b3sOtNVFSAStzdwzaLJvrjvNuzhkgzNbEv14N2WF2HKGkLZBnBRs-IPJGnPsB_fVkn4sOsOVyDnO6M78V3t_ymhX6KhJeNP7JxHX2lrmUC_uEPZveFFAEm1O33mOO3204cmbb-u0wxm-ogOc1tscF5EL8EcOocQa_4j4uDmasJBFe-gwjIniuEKTzuQCnEyfa5rvDWgw-2lxgT4IZAx546cYtVQt65XcUL0HIyy5DuJwL_CmuUioqrIP2T0sMZ7fC7ghlxereEDN0qf6R325IKxAjgpGef5I7z-HwItFYwSSDQGB39F7mlb5rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRIvvsQDyiWv9EyJLkMBXXJtL_TG2oIToPTeBe3lzqHoROkO6m6Vwdy6MDh-INgzYoyiRNeBUjAiqoxDGjJz6ijjTN9Tk0ctSsd6J47QkBqWZmh7RV1eheoEASjmxu0lf4NCcxQUJo06WBJeToajM6SLKKdcqRkOPPqPchcsoMog3KeTPmzcrLZD7V9y07wjeS4LxTfheQkD0_kciL7segk5SQ8QG5q74v1VV72HqujHPWL6MxZOxFAZ9F9kW0Bgbg4qu9JYeFk-reoGAIFUaFEsRuEf6ZN21YhHmx44_0cjGchoj-Cmmc11dE0PgeJ4GTKIumqEHYQfjwESEsfE7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bERYZWhZwUAs39VmbdueLslRK24ZFHe8EODyK-sLB3lngXy53h6DbknZEf0mHumT6bzrwvZa5sdkyP3mxoezzn-ujPp-9W9d85BrZJzOIqh78pDLlWKc3ndJo3cEy06LeZDjWXPoO4GaKGiiBTVqdKA-lkbh2GwKobbCsz6dSv8WRJiFjXYcUgYYl7LynstO30HOUs2e-DTmhTIriZkYEIHN0TJ3BxF3aqgHlgprMKvbUIQM3H6kROA4DUEPXoTPJOTH7MqfPkb8OZwAfNwv_DnjMp-dsdJu49WM6G7ogR9P0jBl1QvLQVhXW7XehszFAKBv_m6LnIRw5OaZ7ogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGB_hIJ4x_eeF4liERJ4531TJLXigjXpmvYRDEc-s3vDBHkCxi26ld3tVP0WWgEgV3x1sB18CdpC33NhU3Nap1cx98I1ViLxCg2_Uc2SjuyLEaqxGOTbJ5B0NRq4ofwk-rziQLwnxtifq0P0rx7t-Jf26HaKzuIN_LxGNtU51_fFNOkXQiiwPFU4oqbZKbhOGt8RKlU1VXMHWiku3BMcXvz3jeHNYf29uljLQM-7_sPjiO-FqP-YRwBbbMkGuflryZQFzC2t4pf5foojAo0UxHLICP-e262dhTMeEudFhLyYWQcOcQaZodaPLHCyKyFIfqCi4ZiBvurQ_ZYsmSsxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrLIoSt7QfZ9FVIWJfy6pdftUrpt_Ju1hlt7vPBQ98ivQySKckRrklFTdlDbgZVxAJQhL7pPZNeVGQhzYvjL6MnGA3f-BNoGM5_ZQs5A2PUpeRrKFwjrhs1VcHhLKAOzSTBQhNKOLTUB9q2gsImtNIm7GG_aEsDwI26vfpjy5p55dokIgSC2zMchForSDEJ4vlMf3SGK5nd5OKDvHzR1_RJwkrd_DpjYgaEyRpaFBIIonI3x87YPFpkdbVbr_Bok7iYSi_9mlv7uDnUgbGC0x_y_HCPRffnWLiGzOCovr1v3Fqff64yR7-lPs_gZoe1jJrCbH96ZhtxpcT4PPocOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MryE288iiuyg2pyqk1Lzqq7bl5o1GZ1NsyrD3fy1DBQpOV1ffBnnJ_8kQYO46Oi-65YvDmmFiRHGZUdE_dfx_D9wW1antRZ3mCqsRKmyQVKNti3cmOchdImBjUJhsKnvXySftSLgjISqm49JZIyzEA4TGSBimrpqHKeMvrikGM_094zXW96luHqv09R0nOpHNoGLenn78BHCdkAHkmx2jGBQeh_givX3d4Ex4tClGm0bNlQ6Uxty9AjRMEctCqAqp5T6CjrGeG7iVVcBEv9QeeTm71B02cEqEQH-AZZDwOSXeeuYEbXi7LqlBcD2PX6fCbCaug0G39hfjs0iqfuVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN2ng2yqFG0m_xZf_ZIviGi8Upf7SVfUJrNly0tkcSC1E2uR3EmOdbsCN68LdhY7wpeQR10h80EkiQQJyTGkth9OtUuTvZLQYPvqmkWr9lHV9xsrPsYP686OkC1-akuGL0adVEfVTaG7w3Sls-aSoUzOJtc4RtWO-7rUslh8RMcqS0Tl3FhrQq3Yq2g4TBqE8lYEEg5ikyM7EgJNXPZGqEw7ihkivR-EM0xyTxx82mrC92YeC9AHc3DLysn8A9QMZq4d8Emh8v6Kc0GWV4gamO6gRO4NyRDsJa86NmbFHOgxkYWfsWo5Fp92Ucr-9OMwxRGznt-U2WkfXZ7r7lViAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syrvwY2RNDkvuBpzr6dI9kBySbICZM5sV3QF9OhQ0GXv_gXQyUFxdu8mWRoK6zFnpg-Io7RNjkq2CLFUF3rx5KBjYFJDMQ5lxBh-okNoRecgUuw0PK1AMz1k1LUwyNGy6R8L8FjlaY2cOKlqW6KnwRAmvJwsWviATUwGO-NdQSY_wyEqxg1YZjex06STpcXo6JpPCoLjx800vgkSwkJ4AenUreImy8awXTALs6qCEW6Ir-gC7QFGJAp9jrB-enXcMSC_q14VLxARG6gIYqwDUfrHlu_2m3ZeA_nIgKo56PZEPYJkBwo6XVmKyCe4Sfuc1fsatm-TF2_iOD5ocqCxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=k83ukwEhxZZPdxiE-CvApob0Rqm17_G7100k5ttV_LIpUfHzhK58uhqlaDzCkAUnUgAo-s-d33BC72MJ2Y7Usa3vTM_gaqnyrvdwH3a0o_cZq9bMO_BKJmAtDUzj3d-DHpIJHi9ZV3DxCjINMj2FNXklS2LngasOQhLP5oKZixcqQSJJxBWq11z2Uw-TtckfVgZ0LN1kyghRFFqSIMgX4dYrxQDdH0pRgQe40h9-xBHY8unrF_wqJsbOgTEYpqlqK6GPO72fa61By29766thcf_UvHxEycrh0DFDHRLpsvVu2EMZYZuVVJHHSEEnMaB66un9pgduKSAZB8snU3z6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=k83ukwEhxZZPdxiE-CvApob0Rqm17_G7100k5ttV_LIpUfHzhK58uhqlaDzCkAUnUgAo-s-d33BC72MJ2Y7Usa3vTM_gaqnyrvdwH3a0o_cZq9bMO_BKJmAtDUzj3d-DHpIJHi9ZV3DxCjINMj2FNXklS2LngasOQhLP5oKZixcqQSJJxBWq11z2Uw-TtckfVgZ0LN1kyghRFFqSIMgX4dYrxQDdH0pRgQe40h9-xBHY8unrF_wqJsbOgTEYpqlqK6GPO72fa61By29766thcf_UvHxEycrh0DFDHRLpsvVu2EMZYZuVVJHHSEEnMaB66un9pgduKSAZB8snU3z6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=ivyhmlpxL175jt_BstLqP4w7S_RCbTWDhBDTyaU94QrQ1t1UM0eRd5j4KmhLYa7zy3hiSjWIE4BI_VsiNM5UAxRp-hDs_xk3LiEUKT19iI6opqYGZ3NddwIfZHt_xb272yfFO2v1QyWSKibn8Dt7JyI6HK-UQGK8RPBQoY4MwB5KRmCwYU9TMm2pgsA9Pb35AWAGVWohpq2s-b_xQKTJ8pUKxCrb_MiyPkSWqtD219qTayPOl4ImcxZvF-nwOPF0CW8jeBN1jdtZMxnpEXEUblhOVupj5a-t-RqwVYK4XryFTtPn6O_r05TfwbH-CbJXMVgeNGj4Pk1EvNmg47V5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=ivyhmlpxL175jt_BstLqP4w7S_RCbTWDhBDTyaU94QrQ1t1UM0eRd5j4KmhLYa7zy3hiSjWIE4BI_VsiNM5UAxRp-hDs_xk3LiEUKT19iI6opqYGZ3NddwIfZHt_xb272yfFO2v1QyWSKibn8Dt7JyI6HK-UQGK8RPBQoY4MwB5KRmCwYU9TMm2pgsA9Pb35AWAGVWohpq2s-b_xQKTJ8pUKxCrb_MiyPkSWqtD219qTayPOl4ImcxZvF-nwOPF0CW8jeBN1jdtZMxnpEXEUblhOVupj5a-t-RqwVYK4XryFTtPn6O_r05TfwbH-CbJXMVgeNGj4Pk1EvNmg47V5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=qX3V84a7G2NgS_mikQQ53z0o1umQYtSyhyU2p0Xj-6TeW-p4CI8sYb96qozOKDUxE_4cLn_7ZeL0v_wwHOTkSAWxcxA5NoQDDQsTxDQmLGAho5UcJnLOTwlyNKtAirwEFODh2AtQefOy6gqSY5OkzAysIduw-S316SljTky-BqHO3OALM2AsT-fJUDD-R6MHlROW-bQxrjUTivAj5LFHmy_vObTHvzS87gSE9QSY6fOIk8UmaG99ql8sS43CmY_Y5HPGq2BzFhqBhYzeCJPyxptjiQGd9nQMK_1wuIQEAiu2-6U_FSPTBZ2ZE9gD8-z4qiRJtkfPIXxAzrGOGtqyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=qX3V84a7G2NgS_mikQQ53z0o1umQYtSyhyU2p0Xj-6TeW-p4CI8sYb96qozOKDUxE_4cLn_7ZeL0v_wwHOTkSAWxcxA5NoQDDQsTxDQmLGAho5UcJnLOTwlyNKtAirwEFODh2AtQefOy6gqSY5OkzAysIduw-S316SljTky-BqHO3OALM2AsT-fJUDD-R6MHlROW-bQxrjUTivAj5LFHmy_vObTHvzS87gSE9QSY6fOIk8UmaG99ql8sS43CmY_Y5HPGq2BzFhqBhYzeCJPyxptjiQGd9nQMK_1wuIQEAiu2-6U_FSPTBZ2ZE9gD8-z4qiRJtkfPIXxAzrGOGtqyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=pQwfvFnurR50n5FZuXsyHkATaLMJdN8v-LX1QIvT8KERUXg1vlfPhMKKNGhsb0ml5QLYW30qXhAUYnGLRR175tXiUuYSr7IE42qJmYtnXx1WKtgeVhcZnXosoeIcsH2ocqgQtyqtNgAygWjcGnbRXaGZj6bu4UJ8209-h8QvUkxMnPVl5aUcLNijsjM8g2dB51LVzBfMAEw4iZbtCKviNunI5xI1lervZveICGLGUsNOd2N_KRI6L-u-wJvsmyudybWog6nXsqpNb8P9vxoDIwvgUdFWjy-ezCUASwbYlrjdZ0jKIPYHS6h5WNS9AGtgMBbalvKp2-wpaJfMQxCI-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=pQwfvFnurR50n5FZuXsyHkATaLMJdN8v-LX1QIvT8KERUXg1vlfPhMKKNGhsb0ml5QLYW30qXhAUYnGLRR175tXiUuYSr7IE42qJmYtnXx1WKtgeVhcZnXosoeIcsH2ocqgQtyqtNgAygWjcGnbRXaGZj6bu4UJ8209-h8QvUkxMnPVl5aUcLNijsjM8g2dB51LVzBfMAEw4iZbtCKviNunI5xI1lervZveICGLGUsNOd2N_KRI6L-u-wJvsmyudybWog6nXsqpNb8P9vxoDIwvgUdFWjy-ezCUASwbYlrjdZ0jKIPYHS6h5WNS9AGtgMBbalvKp2-wpaJfMQxCI-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd2TEldGYrCDZCZMHyPsL0EefnZqsHhO-p3a1AouX4FbduLiaKfa09vv4jmgCf_3rH-ZL7KxqSdJfnz5oYelmKDzv0ppMvcf9iz_BDRm18BOJyZv-KtwueyAjKe5-Vnl0exbWTvTg6AfObFzvJB2DaKmsw7BAkZbms0InC9Y8mTVAJ4GHwDA9j1p7crxcv2O_OeeGlSchBe0fAe8RS_2_SdP581gbNDLBcqyUUw18b8Zp6-w1FmjDSf1-BVBUxhna1F50bmFFcOjHFzccL7-KbEJyT6wGfDPLKLTeH8-qTndIW7WxPTy-ERV9AVeVipul_optNj7GQ1q4be9GaGtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsv8lx8MqNDtIFtRgWAkWUIacITpODLKdZuXl5btWz11vBWzqWmoF3WXP0No-KK7NyxqKjU990OFa8KHnBHS_wYs-U_7CDYTnV41KV6lCwZ74Odp-S3nN2FnhK_ACZxsbKOFsBfzBWONKVwMSbCvt1as-TpDgNmrmx7oupipryoG1A9bNUd0COYdyISqaRl8PyvjbOlSlE5AufQGuol-NCWFUrgkoZo5aolv-OMTYVN9Sigfn5sXWmOJ3buF__57-qqYsycHKNdEIA1uR2J5LmyIyRdEbk9H10YXwIIxaL0Z6rts1PZN-k9GDmui5lTBOPYsgz-V6DI8HDbpablshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=AiAJJx6raXI8I0EqgPNxe4FK54wuH4_Zk8lZzn5LNFRfe7yTs0Ncx_UHvROLjoE47hZ8y7tc3vLqPPOgT1YQ-OYs3VZS09GMKt5wkM9HTfalY7GnHfzqQgxsWeMZbfqVFIz2RPb41yLRSOmRi_CvyufP5kW0HZNqpcSoB8AhvlAfIvY72T5q7XENHa0Bn_QoO3A6rR31kXl2R_WlhX6L4eT_FV18wNPHR9fx_GsC7Lcg9fyQK3sh13Xhfqk4L-ld1UstaOMehxPsMuGQGk3l1SUp29rJq9yS-1qmcbFiNToWYtQCbiw48yfpQISqUppjAeObaQYXmyrIAZn0Yh4c-BYRvdRcxow7nABZiSSiAxZTDk9mDDondueaZLpQa_4HCI0FheuPwGbPvA8aieqw_AETbxEAwV1uZ4x6rz0pRQcR3ahVhaVLU5driGcTje0NZyhg7DnsfOwY4-CtpR86E35apVW60CqKNboLQRe1gN8c9MPGhLXJ4KnQLGaapPyMitKed5XWLCdIvUu67Vbd9cDmdKcKCe9UUmLZ2kPWIdyjEeycnB-McCij7VxljrllwOQQMbe87zev6cKpxNJdpVFkKj9nhSTT3n2SaLzt0rEriU6abkBV1H6cHr_m__5oQg-fjRkr9QP6SMwpgoWBR44EPDEd3maXPfNoVrc8A0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=AiAJJx6raXI8I0EqgPNxe4FK54wuH4_Zk8lZzn5LNFRfe7yTs0Ncx_UHvROLjoE47hZ8y7tc3vLqPPOgT1YQ-OYs3VZS09GMKt5wkM9HTfalY7GnHfzqQgxsWeMZbfqVFIz2RPb41yLRSOmRi_CvyufP5kW0HZNqpcSoB8AhvlAfIvY72T5q7XENHa0Bn_QoO3A6rR31kXl2R_WlhX6L4eT_FV18wNPHR9fx_GsC7Lcg9fyQK3sh13Xhfqk4L-ld1UstaOMehxPsMuGQGk3l1SUp29rJq9yS-1qmcbFiNToWYtQCbiw48yfpQISqUppjAeObaQYXmyrIAZn0Yh4c-BYRvdRcxow7nABZiSSiAxZTDk9mDDondueaZLpQa_4HCI0FheuPwGbPvA8aieqw_AETbxEAwV1uZ4x6rz0pRQcR3ahVhaVLU5driGcTje0NZyhg7DnsfOwY4-CtpR86E35apVW60CqKNboLQRe1gN8c9MPGhLXJ4KnQLGaapPyMitKed5XWLCdIvUu67Vbd9cDmdKcKCe9UUmLZ2kPWIdyjEeycnB-McCij7VxljrllwOQQMbe87zev6cKpxNJdpVFkKj9nhSTT3n2SaLzt0rEriU6abkBV1H6cHr_m__5oQg-fjRkr9QP6SMwpgoWBR44EPDEd3maXPfNoVrc8A0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=Sqd8asOjtQ7thwNiDzbS_9Si43tAguN2VZ8lZwJiq5Dsq7Eh98nkB_uC3Xr2HXEumtIAbkxDgS3carwKy87GQlnPKE9G23ph15XYgl05YFLsudlJdsoWfOfBup_mUo8pkChW8teKcr2ovYuX0IsWndkvlOqE_Ozw1r0DySQm2FjcKP95ZZEWpBGo9yGcZeottexZ3sOdplvDardSFA_GPb271ev9QQYtmIwdApv66sihKc-tIkcXFw8RiNLMhIXwN9LE-YcsxJvZv3leF4sf4L0PZ1mhr_pGTXfIyM3pQ1Ad083KkjOZTeZumGoQ2oRZWZgUzt2nSt4SDt1Fx1Mfx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=Sqd8asOjtQ7thwNiDzbS_9Si43tAguN2VZ8lZwJiq5Dsq7Eh98nkB_uC3Xr2HXEumtIAbkxDgS3carwKy87GQlnPKE9G23ph15XYgl05YFLsudlJdsoWfOfBup_mUo8pkChW8teKcr2ovYuX0IsWndkvlOqE_Ozw1r0DySQm2FjcKP95ZZEWpBGo9yGcZeottexZ3sOdplvDardSFA_GPb271ev9QQYtmIwdApv66sihKc-tIkcXFw8RiNLMhIXwN9LE-YcsxJvZv3leF4sf4L0PZ1mhr_pGTXfIyM3pQ1Ad083KkjOZTeZumGoQ2oRZWZgUzt2nSt4SDt1Fx1Mfx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI9NzxNKnBfoiCVQafmGvjNqFs2irv7OMWENn6x6qbVWWi3MTuccegOO91ethtUbjpchk2IOLG9uGaFWasi6RzZH60HdM0EIRsEkpwLTub_g0puxf_C5VHFgB8nmSvHFV-NYVXz2M_3jwAU1S72yQIVAe7DQhFAdQZ2k-3G7cqorj_wXxB-EJ588ThmVVdRHvBR8I969Wf730gVVvyWPN1qID8swLnjQftg1ysfYabGO_C_hV901freT9a-gPQjS5sBq54b7lH7JnKDZoN41Tspb3lelfx0M_9t3a2twPMthQNxZ44Nv8AEmolIeqzAcejwSd8nLGY8GE97PLN1wuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=J7RmcWQCJ3dCEo301qHDOtLzgLlk_QLAe6eqKJomRlGd-9qTTcV6pE4ddqZHJWKCpG4s86gS3fpUtMGIgM6nDqURDrQ510qrd7JouJeadiLVCUUtzwKHo34pFWO2iPWn-hGReMjolOGPtx48BWYvXEk0EpL8XhqRImxulSpMQtYD8bx_2AKDI7offCSXRMcYbyimjSRSqGuZL8b3bnJ-VoBxsSj0dh4okJimYul1YP2ruvJkov6PzJvSqey6N2iapozkwqgivw58ubEDIYzDGKjfar7HNvwvGR1XmPVsayW5CcsAdM4r37uGne5FYO4mt2UdBamcvjYOVKp7y0NDng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=J7RmcWQCJ3dCEo301qHDOtLzgLlk_QLAe6eqKJomRlGd-9qTTcV6pE4ddqZHJWKCpG4s86gS3fpUtMGIgM6nDqURDrQ510qrd7JouJeadiLVCUUtzwKHo34pFWO2iPWn-hGReMjolOGPtx48BWYvXEk0EpL8XhqRImxulSpMQtYD8bx_2AKDI7offCSXRMcYbyimjSRSqGuZL8b3bnJ-VoBxsSj0dh4okJimYul1YP2ruvJkov6PzJvSqey6N2iapozkwqgivw58ubEDIYzDGKjfar7HNvwvGR1XmPVsayW5CcsAdM4r37uGne5FYO4mt2UdBamcvjYOVKp7y0NDng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=G0VZlVUkuhlHTWHugas3nKoWOYVtzeEBFuNoflnWAF0pJ8PuwjxSGqL0R7wHPtBylqwhgcxHGtMllx3ULPp3rNktuqbZgr0DapZXjcrf6IeDdgNVUgKNc-v5ifdO0Dp99CPzcgWoTpBfKZO_1FewFoJWieQk78a3GhrJ1yNGE0HAWsuYi5gDd0lWEm848dOmmAEDClyN721tcG38jYOJFxb0YvBywTXM2FnqUlWR_oI85MjTb0qSM-kF-xSHKGditY6nq3abq0RCplCz8lLZVuTtfuUpoWzUyE_AIkwQpcmewlUjQK8HWNfgbv2uCi51Yyk9xPRRGS6pxeO0NjiNlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=G0VZlVUkuhlHTWHugas3nKoWOYVtzeEBFuNoflnWAF0pJ8PuwjxSGqL0R7wHPtBylqwhgcxHGtMllx3ULPp3rNktuqbZgr0DapZXjcrf6IeDdgNVUgKNc-v5ifdO0Dp99CPzcgWoTpBfKZO_1FewFoJWieQk78a3GhrJ1yNGE0HAWsuYi5gDd0lWEm848dOmmAEDClyN721tcG38jYOJFxb0YvBywTXM2FnqUlWR_oI85MjTb0qSM-kF-xSHKGditY6nq3abq0RCplCz8lLZVuTtfuUpoWzUyE_AIkwQpcmewlUjQK8HWNfgbv2uCi51Yyk9xPRRGS6pxeO0NjiNlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbBWdhpFa5pBcc_mAUpD7EiHmJas4RURpDe4_TO_eow61If9lkK-aWkcOxkkS7rnP5CXj0Cn0F2ibwmUQLJF8-H_lQ2o_zO2iGEu-2nD_UGgb51y_0waBzvA3PQfAtfcOAlwzaFqeQ46WvwJU8pPX8-yd-IxUNqoL-MbPaqO_MguCQXachCAUrTebc3QvTrDAvH3f_cWWOWc1Oi-Q7dTpCo7R_91QaTI97dCheamOG5DWSR1ksrV2ghZeLhvjH_GD6Zm0Gfms_oKNHXqsi7-CtD2wcg9hMJzPqYZZuZaPqZ3RbkTSZ8m9VwxrB6zyiNGfADqg_7THCF_09K2LDWq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSTtj9gmGGk6xKfeDWENNUTjuPrisFTMa0bGSGEVY_yQkhHwgsAP7YD_CY6G6HMIcR1JlD8GVzpsmXW3wsOI1fRJ9JU9bQ3reCzYkdlYo1zUHAuXZxFbekEzEn5Sp51WXcjMXDIKgPHt3HTN5DvmBuTUle_ATHDkmJdH5HWbWD7hX-OImTAtVIGxfCepozKFozzNouLNluSm6oDiIhHJkdvQ-h_XH2JqTPrjSBhO6ju7EPvNdo5a_Eq-168FaCgOzakZE8fPi6pYTW86G1KTiFqJrbXeeXP5OjP_bHAL2wz9x_CGUdlpLMpvyacm3ny3ZYv-zkaTpk2v365IxPXfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNFA4NtjAnxfnijiYBhcg0JoZ_TINzb-c0r-EzHENJ297u887H2vxfL3jZuub28rqkoKPWNxPor08QRrPxrbT5qZ1l06uvm7fu-r3r8VhLPkrfMhWTtLVONxtzwTtgsZUSX2_pi0Q3VH4--FLndbzWzzzj4ConuxUU5d3q1rhMR8DonpG-UTA1QRHGySweK_ge1_tTJM2FDSlbE-6d_Tl_qnxTkpJPwxlVVU6VQlgIoGQ3daamsno_LnGvUvzZ5tPJa2LgVbpdLw6xQHTFSMLDSUYZ8-gsDhIkfBOagkvjMvIQ1isIMpB8_7ToLJJo3Gzt0bEYIVz9CgkVR5h6S8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKF9ZqAQVYyRLU5YkkKbUkh1djMPYBwhmwwclLacFlcb0QjzvsgN-LVp1dvMjfoNLhkOezQpG2uFbagUYpH0053KnyJyhHekq-unwshMYhVZHs9Mt1aaSZgvlhU2SR5hVaBHYcdTqeRhEVo_iI6bZPCtiKBll2tS7D3OS5ppdntmcHA60MHDWXTEyQTq_58yHukOsv-OdC12HGqtFgFAc_Vv2zacwLz8gweihn0NwqSc77Yll9LpJlEUF5M21mIR0h18Hskmtt6yTC0JKu7E_26C0G-CPOe0qboKGLqi3RQ9B3afvb2o_Zbqs7weO761mDIeQkNQ0n4B-FHWXw8JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=bFFAWQEMuvuAHCzwB8nCjhILAdA7_Ww3iJupdHV3dHuumKuL667OAdO3mlc247oeRMv83f2QpEhLVfDnSlOlFPIzGmgFVWabpzSn-Uk2N0GwPonv1mIvn3-Y6Z6PgolVJ2-Q135rshmNDu9jol3iSEnZMpUZzf8IVKTrow2y-dZDpV8vHX0VFVEUfp96OGTPfsAgs2RZNq5fx0OVzRsJYvFjGMMoDV-A91r2Mwygzd0n8i1vD2RqfrM8dbAcdKTDpSWELjrfKe_25PEKGs7n52zALYnNVjWT7Trhgy-cSbnSx_nAazRAxdmRevFIQPhmdUwXLnf6QqOIyQHHnh5PDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=bFFAWQEMuvuAHCzwB8nCjhILAdA7_Ww3iJupdHV3dHuumKuL667OAdO3mlc247oeRMv83f2QpEhLVfDnSlOlFPIzGmgFVWabpzSn-Uk2N0GwPonv1mIvn3-Y6Z6PgolVJ2-Q135rshmNDu9jol3iSEnZMpUZzf8IVKTrow2y-dZDpV8vHX0VFVEUfp96OGTPfsAgs2RZNq5fx0OVzRsJYvFjGMMoDV-A91r2Mwygzd0n8i1vD2RqfrM8dbAcdKTDpSWELjrfKe_25PEKGs7n52zALYnNVjWT7Trhgy-cSbnSx_nAazRAxdmRevFIQPhmdUwXLnf6QqOIyQHHnh5PDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkb7AwJ6tTtNdxl6tMnNf0Wh3wuhCynyzTXc6ZPggA4-bfqf96TxJV9mrbufDTGVTgwGNSrpAAiEbTAbkGj_qemI0y2JZsq5LarSy2Z-ynEnonBFgnZieow7mk5D9zI0RPkmI-Yvies75-LRrtDCr6zdE6CmU0eDtSydnv0CDvBC76rNaF2tUIMlAhIm0AB4YQuzoLHjgfLzxfIifW_ocSk4xckc--oO3yaTaNVxWZdRMTBADLQcKKrQWp0whP9OkPg62Q0gDh9SnBSnZDe4aQ5ZDgiIi1tAa0OHPcsG4Q4URkQS_H9iJzOXMuHLWz7-s8iPzBqg5vDDKxNf925v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=vZIvxVrNQR0CIMyIsCZ6a6y2FJfiHj7BL3Cg0lDrbMzMwANVT0M9VQzcO15foBGX9gjX4ytDQOlatt7BzxOVGJbZiGszwQIH79WcvGp6EvZFyakbOFYwS8lV1aUL1TguEUu6geDz9CQMghX3KgAxhALCmg2HonFWJz8gRnSlTG-P6FZleFeQUofltRj68rGCyAXML_pab_gwRaL0sj5zY2eHIBfA_NQHF3v2aV7QFnW0rCIUWzkSP9KZmsc7wpv2LpdE60SJGzmpQduSMVM6tzXy9ApgVP2lG5k-ioTKhJLTxdi0AVxpWn4kOQsnleh4yrc2sVQuJtvrDBadh7KtLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=vZIvxVrNQR0CIMyIsCZ6a6y2FJfiHj7BL3Cg0lDrbMzMwANVT0M9VQzcO15foBGX9gjX4ytDQOlatt7BzxOVGJbZiGszwQIH79WcvGp6EvZFyakbOFYwS8lV1aUL1TguEUu6geDz9CQMghX3KgAxhALCmg2HonFWJz8gRnSlTG-P6FZleFeQUofltRj68rGCyAXML_pab_gwRaL0sj5zY2eHIBfA_NQHF3v2aV7QFnW0rCIUWzkSP9KZmsc7wpv2LpdE60SJGzmpQduSMVM6tzXy9ApgVP2lG5k-ioTKhJLTxdi0AVxpWn4kOQsnleh4yrc2sVQuJtvrDBadh7KtLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=EQaHsRUJCBl5UZ7REd6U9zjScy_ZN8Z1rEyOwPcoBnSqZOpfnDt-KZ2PyboGibtXv8yEILPpVVEsV1ob_6I4ehY3A3YCInPdrORs8_TtomLjU2HkZx3ora8f9cA1YxhMh9SwiBYu9jqiFRrS6c7Mjc_Db5IAWHGqwWDG31WO8MdcUBK_As2LFAnA9IfaP8E7ky26iggNkGqaRpCZquUnBXJsEZp5K2t8Gm7LLkKnMJ_VAXAG_9uxL3TgtEqFcQsS4XMNfsa9WE4G97lqZZhveHYFARBpvkKe_pimG9APUwVj-pukxeiNilr4U32xoPVIEHJItDTV5kBkDgP_95SJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=EQaHsRUJCBl5UZ7REd6U9zjScy_ZN8Z1rEyOwPcoBnSqZOpfnDt-KZ2PyboGibtXv8yEILPpVVEsV1ob_6I4ehY3A3YCInPdrORs8_TtomLjU2HkZx3ora8f9cA1YxhMh9SwiBYu9jqiFRrS6c7Mjc_Db5IAWHGqwWDG31WO8MdcUBK_As2LFAnA9IfaP8E7ky26iggNkGqaRpCZquUnBXJsEZp5K2t8Gm7LLkKnMJ_VAXAG_9uxL3TgtEqFcQsS4XMNfsa9WE4G97lqZZhveHYFARBpvkKe_pimG9APUwVj-pukxeiNilr4U32xoPVIEHJItDTV5kBkDgP_95SJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPtjR7vMawViEWJyencyl8tCVcxQ9qSjAne1WJEM7kiJDvnHbR69W6i-ppQNbMJN8WyeWj6UODs-WjYnb76vvS9HKDh1lovgL7FrLDNzfbfK3x_MY-8ejqFPZTd9GMtKvFc7GGPVaLXpanXeN8Z_XUlH84MY8AYGyKn1FSmFKSga_qw0zbprGUcJVUilrCLI1gZudGp3IIEHA8A1aRbDBJDf_voOys81tY7FkvoYdqV3tL-A5l_XsvrqZ3n8foI1hasnJiOZCAd56oQdzoJm6g4GiYHpPFdYFe1EqdNTL8ov_0gEWfHFk4ihw6ouWZrOsHbEZANt0p2e0Zyx0kRrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=PndNTSZYBwu9hYg9sCK3PK_FSKq1MqAcgHxm3NgDlE7J5Y6kvQnOkTxWQN_qzaVOm7BmthUaHQgVev6sdYWGCGPP5aMkl8VbWF7O8QOGWM6jPnqYPWOBKWEKMlWXOhwj7hAcrHG5dcLKy7wJlhL8Qe0cHBId6HbMAQAHrCnIX3MIyzSSAtIMmaJU5kxocXDwKMYD8Hl1FRCGiOnZvfDaeHqhx2FCmpW40DkbZIOgJwWmbbY8f9tIiEBtlGMNtmyjU92x-2f5GMwDZmyNdP797Qre7yA5tonc_tdy8VbGqoLEj06EOl9T49VLOzaBG2LhGxMaCC855L15Dgml8mWbiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=PndNTSZYBwu9hYg9sCK3PK_FSKq1MqAcgHxm3NgDlE7J5Y6kvQnOkTxWQN_qzaVOm7BmthUaHQgVev6sdYWGCGPP5aMkl8VbWF7O8QOGWM6jPnqYPWOBKWEKMlWXOhwj7hAcrHG5dcLKy7wJlhL8Qe0cHBId6HbMAQAHrCnIX3MIyzSSAtIMmaJU5kxocXDwKMYD8Hl1FRCGiOnZvfDaeHqhx2FCmpW40DkbZIOgJwWmbbY8f9tIiEBtlGMNtmyjU92x-2f5GMwDZmyNdP797Qre7yA5tonc_tdy8VbGqoLEj06EOl9T49VLOzaBG2LhGxMaCC855L15Dgml8mWbiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIlYnSNrhMD1YkCEKrqk3mANBrx4tqb5kVuG0XylqPrUgxjJDxSWjAT8es1Orv2LOtAnqiZJa3_qlNNFYX08YYABMbKdJJJ9sDKb9t4dZwcQPq-8B0DOi28LGXEJZwjaL1cDYEeDALX4ZN8CrRUJsI5lJ_T9wduEw73d5b-N6GPDO4mc7q8Mp1lcfDS-IxVEFqmPNsotVQ2m9qoFqsjB7QJqVSUGXpQIIe1EIP-83ML-cmYuWkj1_dBzXaqoGd8SBU8ElIFCWBCnqneI_shTFXGgibGlfWcXlxtVzSOMeJmynqRMQj0vhF9S_mEjFxqJLkXm0wjWuGGD2b5YgH9wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk0oA7keoVslOZL9sbyHbmgA1E6euk7EGWHjgkj7qjoSAy7rDHgrNbpOaRzRNDW5ihHRBIxn_yFzG2NXMj3m0i7lcSALoQZz1Gbya60XwUuLVUCE38dykQBNVjSRkuHKw0CgVsteMT0gAIAIL7wbuBo8Whe3uRxP8RmqhHV5iJJa2LEZD_IlfOZIrcNaxJYAnvfgpV2MXBqe07NaT4bCdBWReYCaoBgcgZYeObCtry0V8kNvbeUwYJeB9bMelUb5NAEk_NxalxMTctp8H3ylaSpA1lfKOo_ZyH-xdMAt5FHfl1RKMSHoc8UrcuVxjIV7SE5DJJvmjqaXCtVVjXu33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=OPyg8unj0LiVKWbu7sZ_kBuLrwk3Yd5Xz9YO5eOc5slj_v9Bpnh0LHFDkpzq67xzs4mQZwwXB-chFbUzf33dyMJB5bQUu56NFddEnHhm_ZDvkvL9N1MFhx4S_vZxlBiKMaGo_O17nr3KRdH9IlNTTQ_YrGVEZV4qKjtv15w9Su_SHRJRM4QrXoXJIPzLcG8GAZcdv2n1tFwXqMnlIegYHchAn2ol7YXmr_V7HH3xOTGoug-yAarxC4SErZEuXiNM3-0-uHYgCupkJrjs7IO7bU1gJqsflXUedbSn2XVwKl0oYNTsuLE8O5mSNhBDZOUeQJEsFKZggVq_6vkNo0PabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=OPyg8unj0LiVKWbu7sZ_kBuLrwk3Yd5Xz9YO5eOc5slj_v9Bpnh0LHFDkpzq67xzs4mQZwwXB-chFbUzf33dyMJB5bQUu56NFddEnHhm_ZDvkvL9N1MFhx4S_vZxlBiKMaGo_O17nr3KRdH9IlNTTQ_YrGVEZV4qKjtv15w9Su_SHRJRM4QrXoXJIPzLcG8GAZcdv2n1tFwXqMnlIegYHchAn2ol7YXmr_V7HH3xOTGoug-yAarxC4SErZEuXiNM3-0-uHYgCupkJrjs7IO7bU1gJqsflXUedbSn2XVwKl0oYNTsuLE8O5mSNhBDZOUeQJEsFKZggVq_6vkNo0PabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9aIwpiMcuU3DyN3g2dQ0gueYBXH_B2DqdIRXStbiRgIZx4zexBzBT1FnCTxmn4jvv2jEkyJqJyNqiPrNo9QIimkSqzai-KhoHKFZHMnoYfzfrf6-vnfLPojDHpaPn-pPifKzKsbMDw06L8hpjAgt9ibvJNdzjfOtfSjuSldSxgAjQDDY4m0fgB8TsQgJ8omcZZg2z3WOCu413-EbUL3He4jk5Mx3O5hS3-fLHaY7q94efKzqBFdk0m_sW1d-0nVjprKMqDYLoOQ0P6LDEJxQQ-9tinyFkTnRF6NZ2olQ-YRF62JUOErSvGn-vbp5IdWC-_SPQQT23VFYPmNXmOlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-Plhn0QYYYuLr8PecqvG1NprR1Yrb9cOCeCauFcTJTa5qgfVNN8apLbJHUzfaAeoQiZsgA-6vzONYEHgwDDEvmqHOKkgJKjCdue5uWziOWrIEjGC22wYNaJBDf9n35u3REWjlcARred1K2RnaxxV-wqNFrSjHta1Rlj9JS9DHZWdJXR04CEJqW2ESdwMtpNEh0sLy2xwvUCub0FpEpCZfLSFYrbQqvfKMPa14u7UZIRs3cbIDc0rYlih72ysCeLzdOfgBah8fJkUlJpiAvnMPiFmHcHIYBjkelU_YuKERJ4ocxPu2n9oqMwNQ_DIMOv7ujmttBaB5EhWrf-hxqeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=XiMK6BO3EjG42Oe5euVXrPsjIwiGGXe_woXYLHxLNfnq2pCn5-FDyUb9P4-yZUAPqTtpH-bznZn6dH5EiKARC8R3Nsou-SH3u9G9beSDeVfZpJ9zEsrWlnGouKIpEjVVjyIwFBELCN49XSLyDu3S382i4YoXKqtZv7Mi-c8WskDRnxTALg3EVkW_f_JZVsap_D5YRVU8Snh6gLcegHk8NYMWPBzbViYHi6r6uHNom0_z1SIpOexsuvcX_WrTxmFIIQ4xbTmSlXWqtUX5QgrL2EGK_bKSnTVZPVvyJ5Jq0wTdOpZSjUv3gYwAU7ghdIHXPVH5uSGaZI-2ocVcyiCxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=XiMK6BO3EjG42Oe5euVXrPsjIwiGGXe_woXYLHxLNfnq2pCn5-FDyUb9P4-yZUAPqTtpH-bznZn6dH5EiKARC8R3Nsou-SH3u9G9beSDeVfZpJ9zEsrWlnGouKIpEjVVjyIwFBELCN49XSLyDu3S382i4YoXKqtZv7Mi-c8WskDRnxTALg3EVkW_f_JZVsap_D5YRVU8Snh6gLcegHk8NYMWPBzbViYHi6r6uHNom0_z1SIpOexsuvcX_WrTxmFIIQ4xbTmSlXWqtUX5QgrL2EGK_bKSnTVZPVvyJ5Jq0wTdOpZSjUv3gYwAU7ghdIHXPVH5uSGaZI-2ocVcyiCxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=lNn1WNouIoidgpob7ifEY44uEjZK_CHz9F8yyBYnXtzlsjQpMg7cDHK2gTL2HGBZ6F-VuSWmagtFKYF43mefgsImyVRqFw95rE86xILswHrfdNpKTIy0125a6i3GBmJ_jtsIKV2_ik0eYQWhRosRaXll-Dz8r47utat98xCcEnaBqU58wUu2L_4L2iSn5r4aRFiFwccOoOrrz2TT76McbwlbQy2vBfPoUv5hxrF5u8aYvY-wkXLiCMhvw-gh52OZfBjUdeO2G5pxgAsUmeizgc8rP9mgEr3zAy_hH8iy3ZZW7jW8KtfGGqdKmHEUH9mnmv7CAtziJJ7BvwWaP4feLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=lNn1WNouIoidgpob7ifEY44uEjZK_CHz9F8yyBYnXtzlsjQpMg7cDHK2gTL2HGBZ6F-VuSWmagtFKYF43mefgsImyVRqFw95rE86xILswHrfdNpKTIy0125a6i3GBmJ_jtsIKV2_ik0eYQWhRosRaXll-Dz8r47utat98xCcEnaBqU58wUu2L_4L2iSn5r4aRFiFwccOoOrrz2TT76McbwlbQy2vBfPoUv5hxrF5u8aYvY-wkXLiCMhvw-gh52OZfBjUdeO2G5pxgAsUmeizgc8rP9mgEr3zAy_hH8iy3ZZW7jW8KtfGGqdKmHEUH9mnmv7CAtziJJ7BvwWaP4feLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeIfkFnYrPkYlvsa5eYIIj7Z3ofvmRveeihJiA-jFfyEyQoiMP0F7u8OtYuMMidXCrOM4nJdTXohiohNARgqqeeqoE3dSfWM1lLgtdc-WVYKNbtz0tW8ilT4rKthubMF701eRli5sqjUc1aaOL3BFEDk8hY90RY7FT3-egED7IY4cJAbQXtt_h5nfxrKr-785C6kbfbZoD8Zzm4qTnQJuDV-ejJrvbgZ7wwK5FPdyFZX_oo82uvrAXGqHVoJY8Mjsw5iQ_9QudFuMSU1YG5DGD54eaxl_SXVjb4JFbJf4Ne8GhMMoQTRGP2mIWxfJ5LeWw3fSb2YxOxCF48QReVvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=DJBpzDd86UXLbL_yuChCetYVxSlk4gdTm1o2LhFpsgUt1ZoU2ODh8OMsIsQOQzSmUa_tpd4ZM0cwyyeZgrIksaVCKPxUmTKUieeE67IKUemuWyOQJ5BVrh4XeUCS_CsntzkOv9RCHQQb-Wdjad19SDd03dYp4fzYUWeIlUGC3eVNwR5dwds-Un1-oONiZIT35X3ydwuHLV7rT2y-MNE8fyi2Z5OyADiRFIyPftLDrzzH0RzWpUOdwIGdqVOWjjC1zmm_Wxgp_Aj-foo7u1ZAnFhnt2ael30jxigG6NijIC0_B3q8WbkNLzFpwf_WE-GYnT_N5OFu8zR0Bajp3eHbCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=DJBpzDd86UXLbL_yuChCetYVxSlk4gdTm1o2LhFpsgUt1ZoU2ODh8OMsIsQOQzSmUa_tpd4ZM0cwyyeZgrIksaVCKPxUmTKUieeE67IKUemuWyOQJ5BVrh4XeUCS_CsntzkOv9RCHQQb-Wdjad19SDd03dYp4fzYUWeIlUGC3eVNwR5dwds-Un1-oONiZIT35X3ydwuHLV7rT2y-MNE8fyi2Z5OyADiRFIyPftLDrzzH0RzWpUOdwIGdqVOWjjC1zmm_Wxgp_Aj-foo7u1ZAnFhnt2ael30jxigG6NijIC0_B3q8WbkNLzFpwf_WE-GYnT_N5OFu8zR0Bajp3eHbCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=Mk6UNY2uFCzpvrCgGXAgxMEdPU4izlkNcQTA1YuEBofBKb1US1mDSidAbLC-3UfZ6iZfOewj0VItj8H8I0-AI7zbBrc1QP7u9dwuGauApDfuVxJKi8jgrSgjJo85UMrlWsuGR2eF8b8hzAMYszDrkD3JQ1VszIjx4PfQGE7-j9d3kWKtsw-XIqiY0YJk1iQuz-qBBumUraG5JnqmJIF69omIx4MBthmxDMGLpBoV5IhbXR24CDcVx_lEmUU_gwpueFnoT5UQ4OsSm6hK5cv3NjOFvB8YtnBvvoxosil_RGtLzrqdINHcLfOxgl52NO4UGOpWi4C33ROkMDDR8s8_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=Mk6UNY2uFCzpvrCgGXAgxMEdPU4izlkNcQTA1YuEBofBKb1US1mDSidAbLC-3UfZ6iZfOewj0VItj8H8I0-AI7zbBrc1QP7u9dwuGauApDfuVxJKi8jgrSgjJo85UMrlWsuGR2eF8b8hzAMYszDrkD3JQ1VszIjx4PfQGE7-j9d3kWKtsw-XIqiY0YJk1iQuz-qBBumUraG5JnqmJIF69omIx4MBthmxDMGLpBoV5IhbXR24CDcVx_lEmUU_gwpueFnoT5UQ4OsSm6hK5cv3NjOFvB8YtnBvvoxosil_RGtLzrqdINHcLfOxgl52NO4UGOpWi4C33ROkMDDR8s8_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=CSZR-XKus5VirFjwRgwtNQbkcpM4GR-0Tixj7DPS8tb0Ee0jv7cUwsC8crTr4ucjwRZ1cUlrNkMboa7f7ikt3jeqadN5pgChSJaHwMn2dAGF4oellAKtoZ0CGZVqnXH3fVNbYIK-dgYS86QLhIzz8ohpqkab2hwQZr1vZLvidAfXzuZpApRTRdvbSvZ5006UdTWHyXrPIAuvOOifoXdkI5XlE0Q7E4OaTp3sZl8KPwl9trBuHE1Aq4D65kBv6--3ne_Br8UE47-mzDbnMMwXSe-rG-S94lc2QxRkMObAfotr81DLU7k2gNW28yY44ZVEh1godPB1Il2rWNl5aXZ_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=CSZR-XKus5VirFjwRgwtNQbkcpM4GR-0Tixj7DPS8tb0Ee0jv7cUwsC8crTr4ucjwRZ1cUlrNkMboa7f7ikt3jeqadN5pgChSJaHwMn2dAGF4oellAKtoZ0CGZVqnXH3fVNbYIK-dgYS86QLhIzz8ohpqkab2hwQZr1vZLvidAfXzuZpApRTRdvbSvZ5006UdTWHyXrPIAuvOOifoXdkI5XlE0Q7E4OaTp3sZl8KPwl9trBuHE1Aq4D65kBv6--3ne_Br8UE47-mzDbnMMwXSe-rG-S94lc2QxRkMObAfotr81DLU7k2gNW28yY44ZVEh1godPB1Il2rWNl5aXZ_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=prKYamTy-3Ybf8Ir-RqkFZfTG5RtvsdhJlbN7QfH-Ax-wncStR1pL15QN_Q19MrPHGxH1peHtcfZk4P6EDZpqH6j61340lXMthLxNm5_YpbTAdDyzTCJmww7i_1DqjdwprHdQXUL7UC7QJQbvVCouaeTfatkxGdMOUm86DsEPNCeMfjYUdyUPR-KIgKl6xw3CIjEtRn85iGWGdTPoXfy2p7R-vNkKvLwi2ROpm8vKUOgqQ-SLWlMSiZHDnHMFPPOci9lhD6bAs9ii7PMEBIVPfPsQcyZLoX6nMR6wNeP2Arnl-U819T5f0zz0VuPUxRNQ267dUYAMCSK-YQTCHzNuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=prKYamTy-3Ybf8Ir-RqkFZfTG5RtvsdhJlbN7QfH-Ax-wncStR1pL15QN_Q19MrPHGxH1peHtcfZk4P6EDZpqH6j61340lXMthLxNm5_YpbTAdDyzTCJmww7i_1DqjdwprHdQXUL7UC7QJQbvVCouaeTfatkxGdMOUm86DsEPNCeMfjYUdyUPR-KIgKl6xw3CIjEtRn85iGWGdTPoXfy2p7R-vNkKvLwi2ROpm8vKUOgqQ-SLWlMSiZHDnHMFPPOci9lhD6bAs9ii7PMEBIVPfPsQcyZLoX6nMR6wNeP2Arnl-U819T5f0zz0VuPUxRNQ267dUYAMCSK-YQTCHzNuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBaovrnLWZjQBDsV6Wx5FiPfsPh0h26wPapOkKCb8t8NlpzI19xnGHl0XCL3xNTy-DxsIqiNUhWnmjWAYWGuOHnUkCTZX9vJZG7EZ1Z5q5TCMzz4gi9DlOPi6fTZsFinlTOxuL1JkfETglpUq9vBhijOTjWtSF6PWhe4ZbHdImYE4mOKGnjdHe2fpZVg8-n-idS31j9SZdtIvAK6QgrBRCSh9zuoFtX2HKiNtDqTc-2dWRKLL6nw0dl52lNP_xLN239o19EqTsO4RXUpekyR4XLPldi_EjMesFFiv243I2c6ACiSClbdxeCN11J2PE5BgcGs8k2R_I-JssmUaPcQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAjL4-s-jd1u6HGxpVanm9WQ7FqJ29Os0BwBGOcBslfyprgTsUdQE2jhLe5HBT_LHltU5pgPC0V3O0DZ6K3YZNLnPya4YZyVvdkh6lCLJRRh0uZPsTow5eV3qqI9raXOD38j4XoFcqLEBMBWAlKqcXjMWSRtnHB-oDJtpV5GMNcqLqam1Y0TBs-fjZeZyIzpHMC7-XIr2Y-A5jW0qq8xzBBjHKcslyHL_vH39W3mBKlQTcX-4bFTV9DPVjQS3c3qtd_X_GQWTxDrPp-HunQwLNc5P8vm8-O90yNTvikAyRLrNcFwK9eLEQk5C2ROZ2gC1zUJwFhaWdpi2QmxZvIjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=bJSG7HEgI6UblvK-znY3CYkfZio1zocwdqzZBFm3NK9hVd6ZaxyBtG-D4z8QpRvZhMv_Hok9bLuLmTdUm4pmzoTFNhJ1cPFRbb4L2MPBFSrRhv8o6sizEm6WyYgVcKHE-CoDoS5MK-nR-508ZEfq7NalvM3wtISRI0q0-0HPhUxgHwehdF_P7yMC3mRUWugTiwXVs9D9xRQSnSDRzgzD-pqSrXILENJrnH0R0PQ2XrxvV425H2S2a2c0tylOdTzEqN-5mf8KJrN_OozB7dNFsDKhrYfVkt-lxELcqLheoZ2_1d95ot_uj25J1nn-M101NJR7PV1wYrRQolo6ZXKzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=bJSG7HEgI6UblvK-znY3CYkfZio1zocwdqzZBFm3NK9hVd6ZaxyBtG-D4z8QpRvZhMv_Hok9bLuLmTdUm4pmzoTFNhJ1cPFRbb4L2MPBFSrRhv8o6sizEm6WyYgVcKHE-CoDoS5MK-nR-508ZEfq7NalvM3wtISRI0q0-0HPhUxgHwehdF_P7yMC3mRUWugTiwXVs9D9xRQSnSDRzgzD-pqSrXILENJrnH0R0PQ2XrxvV425H2S2a2c0tylOdTzEqN-5mf8KJrN_OozB7dNFsDKhrYfVkt-lxELcqLheoZ2_1d95ot_uj25J1nn-M101NJR7PV1wYrRQolo6ZXKzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBZ2Q_6-Tn4CSSE6TKNW2he_FgUNJZciIh_HNY8-5YkW-tiRatJSL90KhFovn7iqtvejbrXrXauxOgBdvdOC_5Da6-KwUQKf_ivrVhDr1eEPMgqfrYDMoO-PK2UDjDNRsDI9rIUlvHsFKNUHA4I44hpkzRp8UniHDzs0hINmqjL3yBz-nj_1Sj1sp2VnuDYLNnc3bm73iGKetZZDW5khT0AGjMNjWCF1Cz0NbV_wRqaaZBYv4zakYtZU46vm7QvWX1A6aFfPc-cuDLkMtdxnvLVOwy9M9nSYT9DJmg90tOAwjfAHt3TmyYiaZPmT6gfEdgeOJKbkDEZi88UIv20smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaLwfQk-kodq6wXbdhCmeBNMwWLiyhK3jN_uNuyQ17xc1WDBO_S8v-0XNKREzewE0SQ4RBxPE4mwVq-OyJJUtJz84naYhv8gnqQGSGhPCmhUpWVXPvCGuVWLGKEP63keOYydA4tWjFeoY8-1hs2Tqap0TBSgB2qNtS4DbktFPsdRdrK2L8avm-m1sRj8qMgGxpOrcyLNI26rtZvQHz2Yh1puUPd5LuvURdhJf1EZPsvz5WUHfrSlglafplCs7XtK8hsoI2MlBrGdm9W52PYb_IAQ8XSCL_ECuSvJCbE7-nWoBRGwMqlWFwrvfA_GcBLuEYcos33Ur8XfyqCdVL6xIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RyJt92bEGjTlI-cac1SYfWiW0KhaV2xydKTFn3Ru9XkbU8ZGOZxpqkiitos1jFLb7bo4BTMeW22_P0lR--0QUWxA6gDv35ilHPxFQ5H3hpqAjrvsqrDQcQx-2_TVrDEt2lKulwuni4IwXT1FQDgXySNyXlJ8c2RRo1cQWClRFTzAuybs-yLhY0W-motNB3zxYTfzJXv7sYS6TUpZVmKcn3LDNdIsPgj_mCv0zye4yRQis3LnyYCUaSwxuRuL_GxSoy5_IsosZhmQp0O5Wmc-VRYkY4t3EZ_J6UCNaISoZztq91fONIaTJW4MPwsihti5YxyLiO7LNuPgfcHu7S2PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nlczGKKACA-qVK8D81NnumKXC_oK1gXVmKvpTTxpCKSXNlmKsY0wtxVtjVoY2CKuyoN5m0A_ltP5NN6upvIljT-Rdmr1r3HWVBDa1w0q0D_3hNAjZYePE-d4BV2fNMq30urwYgz4h_4odqsCBx4aJMyhGhb8A0ANDosnHq93HXkHTsPx1crdDm8owwvVOZMJ7QvtOOYop1lge4z-nzqqyFZAgQ8VaD6_F8aLC7feWSYeY57ltmmin3lYR8hVHV31LZ_Gi0UiHUcQ2YVKCh8iyXyLGUiQqwd9mg3hg8y2T5Vnmmz6h9tTLuA6ur44tEB42uU47Bh4m8ju5jDQYWKfzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=YTHnEAabosJQXXQi9G5OqTl9zyEqzh9dFucIoxkR4jCOjzCkpvLqxNsw-Ee7gvugtcmIqoiJUBLZQYNBsonYxrhpXa4jy62v1-lpXSFCwL0F5ArCQkYa8lM2-uqHhR-Ath88ozbhi-tioLJloPVGImtHVxuvXD5pPgwfYxOb65Fg4jYvhatR-ZGBwLVhfxeTmBTwr4IZ63jclsFDLj2Kx7cngkYNxN7cQ_dJv_2CRb1BNc4AXYpjBYuDA3Vqt992_D3qC1E6piTD-1QXIUdYB4dTIwn6y1jHFBH3FrammRKFHVdKraz-7rG5JGCAUyPahlA2DGZ5Jb5Evn44yXNXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=YTHnEAabosJQXXQi9G5OqTl9zyEqzh9dFucIoxkR4jCOjzCkpvLqxNsw-Ee7gvugtcmIqoiJUBLZQYNBsonYxrhpXa4jy62v1-lpXSFCwL0F5ArCQkYa8lM2-uqHhR-Ath88ozbhi-tioLJloPVGImtHVxuvXD5pPgwfYxOb65Fg4jYvhatR-ZGBwLVhfxeTmBTwr4IZ63jclsFDLj2Kx7cngkYNxN7cQ_dJv_2CRb1BNc4AXYpjBYuDA3Vqt992_D3qC1E6piTD-1QXIUdYB4dTIwn6y1jHFBH3FrammRKFHVdKraz-7rG5JGCAUyPahlA2DGZ5Jb5Evn44yXNXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DT2PvYQi_9E5mYWvY3AQ1Gsq0H5-CnQXGmzUJ5UD5fkktK216P-V6Q16yYN2iyRR8HjldN1LE24kFZydNSV_Xo8zAq0Mizs3eZQJI-ZvkTEbOTUXIcP1HP42dL_R_T0P7Q5gyNHvVo5NuUcIyNNrqPJTTG4jOBcsLMILkEUYq7nB3MjJSHBRlVUPx-W6XGs46u5gTpq5PUeuTfOeZxJoWJKnPXwMs6SrLnA-UNlrpCMuveDjcsPb39JWQxMQMIxKdd4HX4joUa8_DzqdOEfQsb71a0iCxI6XCpMM_P8SnJw_G_KTqSLTlIaWpizoBaTQl1c68bf6H5zrmw9gmoln7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=A-7f3zTG_2nDI2MO_JTkve70awBY7FxB6hypjuvM1vHTNyhnWwhi1133HSMZBrXKHscFUkrA3YZg_Rdjk8BvFVE9yXW8w2_tNCcO62lp0eCuO9zChymMLhYFsbyb8Pp11VilGVVv5DmMonvfp1S904XTfv_zIdlQf8B_6B2YTaji136qDwF4Mh9vb2_ud8s5NsmL7tDFxqfOni089OwwzPFUswj2qyPESWi1PvAqBy37QMl5UhMlZgQ7A1UNYuvOc1g4ju4n4RPP6f1V39PCXWBCd7pUSd5bgTqAGCm1X5s_GDauHAkZc-VZVxYAmDG3B07Z9W6KtY4OigCEatEs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=A-7f3zTG_2nDI2MO_JTkve70awBY7FxB6hypjuvM1vHTNyhnWwhi1133HSMZBrXKHscFUkrA3YZg_Rdjk8BvFVE9yXW8w2_tNCcO62lp0eCuO9zChymMLhYFsbyb8Pp11VilGVVv5DmMonvfp1S904XTfv_zIdlQf8B_6B2YTaji136qDwF4Mh9vb2_ud8s5NsmL7tDFxqfOni089OwwzPFUswj2qyPESWi1PvAqBy37QMl5UhMlZgQ7A1UNYuvOc1g4ju4n4RPP6f1V39PCXWBCd7pUSd5bgTqAGCm1X5s_GDauHAkZc-VZVxYAmDG3B07Z9W6KtY4OigCEatEs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sesuY3urf8p4tz0t55D7LLtZ0Qsq_hgeQRlJb0PN5CIGeeu0OKSVxQ7JB4oWZrW9OaNW1dDhyFmaYQ4xCD8ipNlCXrFL0W-01wn0tJgDLgy1nwqleAcgOrlZTS5jFh6NPbkMfLGXcmFMqB-PhSlvueIDa1GGAwYKjICpoyFLvo8qljZlNXlmpOV-jqH_Oi4Th09q_0Kput_VP8FhXV4q2Tz4CRnDFfWfjQBAFd55zQFFnpXtKP4RX5Dq-FH4dKsDYFsl2Sol86PdwDbHbyN1KYhfQTKuYUHeH5u2VNK0-1QC6CjQAwHzFNaE6vKwF3SvH2g84zT4H8FDvnBs2QPx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hplSIC8AaXKA0mDYzE3vAJltGxaH58M2FbsLHhjAp8Yc6Qner85NB3Y6hl70scNaPsQc1do7MB2bMQtIocDxnjLKh0trzb8GL8D_UOnSiOJB90rmNg6QognR8b-gIYx0HgPWwBZr-dO3-1hfH2KaxnWRbwwnRN4garMVC8-D2jaLkE5Q7gSgTE0l4GWmwZM2I9sphY5-Bod1WP9Dr7S6EvcgmjdYFh02ux3WLwP1G8J35JVJB0CeorKf4VnttyT_88Yt-_4NFTaCreb2RgcwfRjkHKsdnSEtkIMDoDckwRV7Mfc8vtn3394VveKfHZ0XyNp9zdQ4YrcMUZKtaBMZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=Cd_Tmf2_joC-iW3KPG8H0A7Si-kZIvPcOeSaFOXVl6VhaHALSpNscc4DfXXWpA6uNIlgugFcaWlBQV_7pejG1pWw9clcf5bxoiJczVpMajyKMrxvCtw0fJAKA5IjOA8jKyw3U2I_10GqobPKgv-kj1rLGUnqDJyCOpzKnCmTk1teE_nkJYAwQKFe4g_vKogohdrDjiS_pEV30ri7WJIGBJY7PHVzwdB2_t_Ace-gPldRg7R002uvRZZyH_6ZJ2UsjLA6b5X6Y84ceVBMsUFwe8yQGCaMdt4T9cxnMtZQUgB6fgGii-heyWbXOHpfiLC-I8RfYLLxFt1j9vMVNOkyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=Cd_Tmf2_joC-iW3KPG8H0A7Si-kZIvPcOeSaFOXVl6VhaHALSpNscc4DfXXWpA6uNIlgugFcaWlBQV_7pejG1pWw9clcf5bxoiJczVpMajyKMrxvCtw0fJAKA5IjOA8jKyw3U2I_10GqobPKgv-kj1rLGUnqDJyCOpzKnCmTk1teE_nkJYAwQKFe4g_vKogohdrDjiS_pEV30ri7WJIGBJY7PHVzwdB2_t_Ace-gPldRg7R002uvRZZyH_6ZJ2UsjLA6b5X6Y84ceVBMsUFwe8yQGCaMdt4T9cxnMtZQUgB6fgGii-heyWbXOHpfiLC-I8RfYLLxFt1j9vMVNOkyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZv09xok3Q2lmwyeX9PPVsKokd-gikDDdbAdSqpLWoxV8Uoc_6GNjvQQD2v9BY4w9hGVjWKr6m0m1dk5Y0bap00GKSYnFwszs_XcXYnKxQutA5zAE-36sMjfEtr-NZxO3H71e5iN-xkyegQ9hQCB6ky5hNTCS9LNFUWzSOEkhyM-_9vwgt8svCw5LZkbcLctdYt-0nVvVC_zqwHsEVA0fG72S_gP6y0JRcSU4wDemANWZgnwSeOCWr0lPkseQBfHq_5Zvu7imppODjipPiwE_Gk-6CV4hPF5GlU-5Dpax0NeCDzdlgXJRmEH7G4LLCe4lFOW--WIR3Qg9IsldpKY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=P07I9Ko5MfXPIonCDC5nd5BUeeQlh_be3DZ5V9-myHILI8_r6etD4GHJz-SwhOTuh004PjHJTVBV-t4Bbk9WGpAkIKWLkg-kR9WG7QWJLoRxy5Ln8ZJ9NjR5OHr7PUdhkEkNKt7PnXSqlE0zW-nUjTmpYS1unekyxT6KDxwRBBaRAO4JZqYhM16sUEHp0_gnxAT7jRCsLLO0te1L3n_ZqsebfN4ZpR16lGLY6ABwuDW48eVuTFqKCAwSjNIdeeXusz1xWmrxukPQFL6cnyS8DdLQuodhiiMbpcnMwTK2aa_t3GpsQ6ZBTjw4J3Sx7VuR6YA4BjCIh-IyEvMcnz0GbD8MaqqpE6lEyhY8IqLVavpav8i2yAfjgwqXOUkRRLfonUff1_rnEobxFtz1BPPDE0QmbuiKgI72RD4a_ltFn0gMieEwegl12zEB9yIDqqAxVURjARW71ApDSG_u-E2IrD3tBgoL7Paampji96ZO96FzXD-FokWYBg30hpExp1D4VCF1_UP4lrNtCJ5kVyHqHf6-6yLE7Etngt_RjjF1TWGyl7J54iqnTp6QPU2N011IsYp4MuebjKdgNJUHOJ_xejR8SneLBzs45YL6xol4YWaA-jCR6sxYwZvMLsqbBa3oabdxNbvvO2xqDfAks7ldE3Q161WIzUcsqE585rXgV9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=P07I9Ko5MfXPIonCDC5nd5BUeeQlh_be3DZ5V9-myHILI8_r6etD4GHJz-SwhOTuh004PjHJTVBV-t4Bbk9WGpAkIKWLkg-kR9WG7QWJLoRxy5Ln8ZJ9NjR5OHr7PUdhkEkNKt7PnXSqlE0zW-nUjTmpYS1unekyxT6KDxwRBBaRAO4JZqYhM16sUEHp0_gnxAT7jRCsLLO0te1L3n_ZqsebfN4ZpR16lGLY6ABwuDW48eVuTFqKCAwSjNIdeeXusz1xWmrxukPQFL6cnyS8DdLQuodhiiMbpcnMwTK2aa_t3GpsQ6ZBTjw4J3Sx7VuR6YA4BjCIh-IyEvMcnz0GbD8MaqqpE6lEyhY8IqLVavpav8i2yAfjgwqXOUkRRLfonUff1_rnEobxFtz1BPPDE0QmbuiKgI72RD4a_ltFn0gMieEwegl12zEB9yIDqqAxVURjARW71ApDSG_u-E2IrD3tBgoL7Paampji96ZO96FzXD-FokWYBg30hpExp1D4VCF1_UP4lrNtCJ5kVyHqHf6-6yLE7Etngt_RjjF1TWGyl7J54iqnTp6QPU2N011IsYp4MuebjKdgNJUHOJ_xejR8SneLBzs45YL6xol4YWaA-jCR6sxYwZvMLsqbBa3oabdxNbvvO2xqDfAks7ldE3Q161WIzUcsqE585rXgV9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=Ogc2_1XUXjMUe7B-9rAwJ8W9JDBaHVsYhED6Q59Lwj1BSdo8_k-sqidQ0i6Vf7jRfSzhtPWleEAXR7UpwD26dZDhEAS-vu7loYeQsQ8prXVu5t4uprbFL3pWeUwO0-l3RXGteIKGC5Z5xNjB7srTpcJQ_aiUH0UWE-57xiUt8IhuqQWa_pT1hqGmk_vM-v_sugiPsSU2vhdCzS9ShnrOqeDvsaVBaJ2l4ZO6gbFZAKnGnKrc0udfcGRBom5UH7C1B8tp0kAYl3AwiXQP4eBR2uNutDp-kAViKHuITfJXGoWPy0e4_kehTf-6KOKvs9TpPwFK1jg3LAI3wPvQfNxEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=Ogc2_1XUXjMUe7B-9rAwJ8W9JDBaHVsYhED6Q59Lwj1BSdo8_k-sqidQ0i6Vf7jRfSzhtPWleEAXR7UpwD26dZDhEAS-vu7loYeQsQ8prXVu5t4uprbFL3pWeUwO0-l3RXGteIKGC5Z5xNjB7srTpcJQ_aiUH0UWE-57xiUt8IhuqQWa_pT1hqGmk_vM-v_sugiPsSU2vhdCzS9ShnrOqeDvsaVBaJ2l4ZO6gbFZAKnGnKrc0udfcGRBom5UH7C1B8tp0kAYl3AwiXQP4eBR2uNutDp-kAViKHuITfJXGoWPy0e4_kehTf-6KOKvs9TpPwFK1jg3LAI3wPvQfNxEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aunRUWaKKtIid6vKzU_MxoGvisQs7g1K5oxEOikuhF4tld091Ug24QfvH5sLotRaCiESB1wk9CKLZqji4dqXblLmNGsaxQAyehTgg9w0wwnB5Pqj86DpgPYDPwbfUVUG8jV5OvM1BAUreoKRYi6Pe2WmteANHOGkne93BX5WhzqQR2P5SAr2SvF9cBgaxx_NwQuV-agnBLMQ41D1dRx-BBwFXyoTtmZYd5-N-07aVSKsQ5yQKWCiSkZiKdIJG7A4byzBN8C80_6Dv-ps5HhKDCpistnguyRQ0_Lv9m9tbHJ2bZTlkntUVcd9cLNpStFbD7wsv1WGuGDt1LIkr9o5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=EQx2EWR8BWZUaDEirxhJORZU4KTIv-jNAVAWWffOLRxI3U0u-IQCq5DxQ8ZE6EwSR8d1HhQd2Q9Et8VSipAo5bujL7tA_G-jxlfoHToT0CLiQK2Op2iOlis-nK2oAD-Y3oB5AieB5zZfE1XbOzI18q_yUp2WXHhmABAqjQ2GeXiLSxMchAUnzQxPd3mFr9mqSdZ8KqW0SXPYkkLkGi8Z543mVCv4dxpTulLZeq0tN-tgS2rpvsxHforl7J0arTlPuTUY8qiQ7WiuEMrJchSXfHbZor8IQrLUItq1oZwQFzHWoNKnYejfnIy9_GdeOhRnyQldAiX9yniZNbClPGr0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=EQx2EWR8BWZUaDEirxhJORZU4KTIv-jNAVAWWffOLRxI3U0u-IQCq5DxQ8ZE6EwSR8d1HhQd2Q9Et8VSipAo5bujL7tA_G-jxlfoHToT0CLiQK2Op2iOlis-nK2oAD-Y3oB5AieB5zZfE1XbOzI18q_yUp2WXHhmABAqjQ2GeXiLSxMchAUnzQxPd3mFr9mqSdZ8KqW0SXPYkkLkGi8Z543mVCv4dxpTulLZeq0tN-tgS2rpvsxHforl7J0arTlPuTUY8qiQ7WiuEMrJchSXfHbZor8IQrLUItq1oZwQFzHWoNKnYejfnIy9_GdeOhRnyQldAiX9yniZNbClPGr0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=dII6YCzQt5LS6z9XargK-XBUx4IzkavOjUH5R4gLU7MQuWyU3dLJX7gkxrEajJB54XOrhJak1qc9fWctlFzrvHmILk1lmwH9fkVqTpqGv7C_3uSE36l79ANG7M2PgDpQJ8ZE0nYhP_tEygFoBB18FvUPtIJUOHj1wFSqTAnIql--CHwqBM66IFaVBENFRXe0WecLtpqFLifgAuoEvyYYe9aCfXSeBaAkhfwbwmMRxtQmJrHSvObOfSOCh7PlDjOmcgbsYTm_0dhhEKBgyMuGqUOwr6KG-xVCPU7SrgS8PX9YRcLfUdpBBiFUqScc6rc90uzpdMB-lL8FMYfq_CKo2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=dII6YCzQt5LS6z9XargK-XBUx4IzkavOjUH5R4gLU7MQuWyU3dLJX7gkxrEajJB54XOrhJak1qc9fWctlFzrvHmILk1lmwH9fkVqTpqGv7C_3uSE36l79ANG7M2PgDpQJ8ZE0nYhP_tEygFoBB18FvUPtIJUOHj1wFSqTAnIql--CHwqBM66IFaVBENFRXe0WecLtpqFLifgAuoEvyYYe9aCfXSeBaAkhfwbwmMRxtQmJrHSvObOfSOCh7PlDjOmcgbsYTm_0dhhEKBgyMuGqUOwr6KG-xVCPU7SrgS8PX9YRcLfUdpBBiFUqScc6rc90uzpdMB-lL8FMYfq_CKo2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4y6eTQwtuAfPdAe-we8P45D_-WpkZ6PkKODgXaPuODg-xRynBnzKIlZjkk8FFeFxBoEbEml-IP-AS0poIYdTwtoxf4Y0kEoNcQkGc90g1grRdwC4i7eajKTPzQ3ivaU1EHOx8W_QQSgo5sh3fNSMNRZRzlpYxUJbTM_hpF1BFNlxdYrmuDhwjdOD13f6rc4OiI223yP9JUjxnHxfq53mDRiVziRDYhDT0LwyKRO1TiP1Gr9wYadKj68HURqtb9dgIIsGVWYU8Tj0fmLNbEa06Iu5TCZb0YzGZgOQ7LXoFvr4b0X2v6jVqEBoTM1snd75sh7-Wu0aUKkBWDdjJeq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
