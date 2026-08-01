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
<img src="https://cdn4.telesco.pe/file/GPKg24XXa2wmqLwmi5fNgrEi-pVT83114BbcAyoLh7HZKJ8aVCSz2j0EY3VXAGrp53MJqDGSEiQr2DX8HV66MYe01mRg8WrBDu_bIrUKr6ZaG-RY6nh7SoYHZETvQMfyGy8TA4jsJ6zljki5flxExCKkFBEBh12BTSqAyFMCmbdxaPKFgpWiFQRTDHUQkWpwGwtbOddPqMmx-wN3dNxEJvzf-C-j2EkaaMV-q33xEPIL5WSb1gMe4ReGLq4b6EdWjiXK7k0E0iB7a1Of8mPmGwnNkAxPDHVkprfzLKvol_X-LT7cXKxvXfrvpifJv55dwCxpoaMTZtDh0Gk5NPTTcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49864c315c.mp4?token=Dby-gNPKudGlE5N708wHJ2a2pDAffeSYvAfyza_H5OOFy3jLrbjt20_KHNa9XZ_BKfxTA6vw68oMGMBnXKxWzMeVEwFFZlm_pm0gxzmJMFgXo_R1uR_Zg-IEUvnL7l7W-jtrTWCHmesmC3To4L8z70CZ4YLzyC4sPELuQwHtxtwSP3tFN6zzY4vSTHkTyeBRIu_k95twPljDn092bxjE0gMp_EGYeIEx4Uwt-KBLFMdj_AMnt773rKaKyaZtcP2l1e4pbph3sXM9IObRYA3SpnrWMn6zNjAqFABCFSllRKGeUHrpvn59FdTww0Yp8xuU7kGgma48LWtm8DOCzOLSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49864c315c.mp4?token=Dby-gNPKudGlE5N708wHJ2a2pDAffeSYvAfyza_H5OOFy3jLrbjt20_KHNa9XZ_BKfxTA6vw68oMGMBnXKxWzMeVEwFFZlm_pm0gxzmJMFgXo_R1uR_Zg-IEUvnL7l7W-jtrTWCHmesmC3To4L8z70CZ4YLzyC4sPELuQwHtxtwSP3tFN6zzY4vSTHkTyeBRIu_k95twPljDn092bxjE0gMp_EGYeIEx4Uwt-KBLFMdj_AMnt773rKaKyaZtcP2l1e4pbph3sXM9IObRYA3SpnrWMn6zNjAqFABCFSllRKGeUHrpvn59FdTww0Yp8xuU7kGgma48LWtm8DOCzOLSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزمون ساعت ۷:۴۰ شروع می‌شود، ساعت ۷ در مدرسه را می‌بندند؛ چند دانش‌آموز ساعت ۷:۰۳ دقیقه پشت در مدرسه مانده‌اند و به آنها اجازه ورود نمی‌دهند
🔴
این اتفاق والدین دانش‌آموزان را به مدرسه کشاند و باعث بدحال شدن چند دانش‌آموز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/139140" target="_blank">📅 17:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فارس: یک کشتی حامل گاز طبیعی در تنگه هرمز هدف قرار گرفته شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/139139" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فارس: یک کشتی حامل گاز طبیعی در تنگه هرمز هدف قرار گرفته شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/139138" target="_blank">📅 17:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_9GNFhH7bIZhFGkoiwYWmZxPgBzkUQ50DTSpJ_K_86p5YjPOfzjNNQmj0q2oFRPdl9Vwx5oekI6gvC33lBpqsfFjYc1ZjNsAWrgKTws7u_e2_nu8iSslYvpig47_e1f7EwpRY1r7fWccEKMdFeNAdu0n-CoTDB4GvHqmHVWNGeI0iH3-WIap0UnmiHURpkR_I5otLTHygQsuTXatodBBUTEvNPvTNOc8NseqYCQHoE7g32cCOfpa5RNWLX_AA_4qJ3p59J1BpqfgpPTlhOz-GFr7O0WokTbLSThFxB2EMWZVnmOokHukNxgyYs0w8587t3NHhENxQdzvZT7E0lH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحقیقاتی از سوی خبرگزاری رویترز نشان داد که شلبیت، یک صرافی ارز دیجیتال بدون مجوز مستقر در دبی، از ماه مه ۲۰۲۴ تاکنون دست‌کم ۴ میلیارد دلار تراکنش را به عنوان بخشی از یک شبکه مشکوک به دور زدن تحریم‌های ایران انجام داده است.
شلبیت دست‌کم ۱۲۵ میلیون دلار مرتبط با بانک مرکزی ایران، ۲۰ میلیون دلار از عملیات‌های مشکوک به استخراج بیت‌کوین در ایران و ۶۷۶ میلیون دلار که به بایننس منتقل شده بود (شامل حدود ۵۴۰ میلیون دلار پس از اقدامات اجرایی مقامات نظارتی دبی) را مدیریت کرده است.
این صرافی به بیش از ۲۰۰۰ وب‌سایت قمار فارسی‌زبان، بانک مرکزی ایران، نهادهای تحریم‌شده ایرانی، عملیات‌های مشکوک به استخراج بیت‌کوین و کیف‌پول‌هایی که اسرائیل آن‌ها را به سپاه پاسداران انقلاب اسلامی (IRGC) مرتبط می‌داند، پیوند خورده بود.
سازمان نظارت بر دارایی‌های مجازی دبی دستور توقف فوری فعالیت‌های شلبیت را صادر کرده و در حال بررسی ادعاهای مربوط به پولشویی و تأمین مالی تروریسم است. وزارت خزانه‌داری ایالات متحده اعلام کرد که از این ادعاها آگاه است و آن‌ها را «جدی» می‌گیرد. رویترز نتوانست مشخص کند که چه کسی در نهایت این شبکه را کنترل می‌کرد یا بخش بزرگی از پول‌ها به کجا رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139137" target="_blank">📅 17:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کشورهایی که توسط سفارت آمریکا به شهروندان آمریکایی برای خروج از آنها هشدار داده شده است
بحرین
مصر (بی‌سابقه و برای اولین بار)
عراق
اسرائیل
اردن
کویت
لبنان
عمان
قطر
عربستان سعودی
امارات متحده عربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139136" target="_blank">📅 17:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا جلوی رسانه حرف الکی میزنه، اونا دنبال مذاکره با ما هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139135" target="_blank">📅 17:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-eTIJfUU4NSG7mCj0jvEjeXEOj6r2O1s14mTbuSDYF6HBBUfv6RqbKImL4P74RGt8m3sLOitt-FQbWCfnIow5fgKMqDp6d6yRYiR435LWs_oz8Eawuq3RrTizX10VdQaZbDchqsvS6WGJTSO-FiM67g3fEh5nvcpbPOFsqI0V6bz0StQE0mYmbXBec6tyCBWulYZymZAfOXdrasnbffkrtta9asqoh2YWG3hK6hEXibAIfauJfEsTt_lr59YK1yNO5LNj8d3EfcL85PhnbfW2ccvsmAl2G8gEkUca7c0GDJwwExOIitKlHvYVBMDxD-mUQ9tPRoHB5lsL89j_UJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعزام تانک‌های ارتش به جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139134" target="_blank">📅 17:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52322b2b53.mp4?token=ew2e7kA8hbzhFDpZmg6p5TTKflSahHANcUvw5v9dh0VO6W10SGPOLYMDcQvamISh7reH-OAOYKlwwy44b-4QuqQghVsZYhcPCJ0S1f66rdlLSgz9pNTZfR1iMK2C-ynlHlWWR6wgIYzmqUpHF2y-IbtQ6wLWw4-mcuvQFP_EhIyK6vQu2KAj_PRXeiHiFOSkVEgAcQBviTSvK-GMU6zNWx07Seo1ccVqYoNxiqfPWZ1NcSt73iLQHelQOrd_EjvVsaiVFc9pqSV265Qk9yoob4b6CL8MHqbTFYWueefkyXEPtqmiOg7kFVl3izBO3A8FT3OC_xVQ-i0pNWwycHLcc6tA5IIPC2fjLo23FinRpO0_WWwGF76d5noCQawpdiiyDBvHQ6I3c0G94orddmurXKeHt5lnu8CfMmBoKY2f3o5MCg5eNBe7kk6QD4iaEW7u4tEd1IL_He1Q8_X_JuJS0PV4tDEQGuGldFAW3vrnUvGZXlDPQ9Pf8VB7um65cdEUlUEmC8NSlQOg2hvD9xMNZJC1Vhba2IuH6wjdZ3MxoGT9SK7JEP2WYK8aaehg4_2HSa8AiWxQvbt-kX5_T8HRhI_IM49R8SDJ-cponQgioLpYMUs6UEgp3VgaW4Bl7DicpnGrmgkfvuKBHZQ021Ulx8Q2arS1-Ht6VfcIbyRLTVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52322b2b53.mp4?token=ew2e7kA8hbzhFDpZmg6p5TTKflSahHANcUvw5v9dh0VO6W10SGPOLYMDcQvamISh7reH-OAOYKlwwy44b-4QuqQghVsZYhcPCJ0S1f66rdlLSgz9pNTZfR1iMK2C-ynlHlWWR6wgIYzmqUpHF2y-IbtQ6wLWw4-mcuvQFP_EhIyK6vQu2KAj_PRXeiHiFOSkVEgAcQBviTSvK-GMU6zNWx07Seo1ccVqYoNxiqfPWZ1NcSt73iLQHelQOrd_EjvVsaiVFc9pqSV265Qk9yoob4b6CL8MHqbTFYWueefkyXEPtqmiOg7kFVl3izBO3A8FT3OC_xVQ-i0pNWwycHLcc6tA5IIPC2fjLo23FinRpO0_WWwGF76d5noCQawpdiiyDBvHQ6I3c0G94orddmurXKeHt5lnu8CfMmBoKY2f3o5MCg5eNBe7kk6QD4iaEW7u4tEd1IL_He1Q8_X_JuJS0PV4tDEQGuGldFAW3vrnUvGZXlDPQ9Pf8VB7um65cdEUlUEmC8NSlQOg2hvD9xMNZJC1Vhba2IuH6wjdZ3MxoGT9SK7JEP2WYK8aaehg4_2HSa8AiWxQvbt-kX5_T8HRhI_IM49R8SDJ-cponQgioLpYMUs6UEgp3VgaW4Bl7DicpnGrmgkfvuKBHZQ021Ulx8Q2arS1-Ht6VfcIbyRLTVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل : ۵ انبار سلاح حماس تو غزه رو منهدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139133" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTUJzNHf2fcuUmR2xQ-hxZstz6bDc7MQY8WmopbeZudP-aEURU4dydmHOKSRXhzqgc3LlEsKKVJvxS_NMmYLlg7iy_d9OppTMii2MTBvc194lixZ0xujVbCOee6pcwaSYnsmHnC7uLhqaWSO6vDHmpPQyKJpq8WktvT9MasbaSlugl4e40ltY0WisGCzK9QhhbKeL10V9BTGZyuG1AMcTukwiGP9JSPwfAmunMONvDH-F-mHyB0qyfRhLPWI2dFT9lXOAy9p_MvP9FWT9ksW26zzKHCnSmcVotZrZQjGEAZ7gEDEbi21z31xEedEKz8mcMQkpYdndpo81K0HUVnfsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورنیوز: حمله امریکا به زیرساخت‌های انرژی ایران، فقط جنگ با تهران نیست؛ قمار با امنیت انرژی جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139132" target="_blank">📅 16:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f255af304a.mp4?token=cg0UB6rHHFUZLBWA7s6gndttaPhPOtR7QGO7yVpiIsdOBB-cDxyyhE-R31Vu_d66L0ZcnycCt_uXda7RpvZZoCeh8tAB4k5B0NyfmMHVcHYdYlSPUIKu9QibVkmmYtgSYXGR-woRJmt-WDCt2ZGOt4bqQYRgitKwnUBoAWOfj1crVkEGWO0Fbq4HN1pTUm5R-qSXvB5N9hRoFB1GWQiiBcicezBJzJ_zBeWOsehwVMI8ZM16fcW7GHAa1DHMemSFltAQ6glUR6ychL8CvdKT5AP5idiH60FC9_zKSTwELyl8n9iXsg762n6dkupIT3wOsewvsM89Lq7GouY8MaaofA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f255af304a.mp4?token=cg0UB6rHHFUZLBWA7s6gndttaPhPOtR7QGO7yVpiIsdOBB-cDxyyhE-R31Vu_d66L0ZcnycCt_uXda7RpvZZoCeh8tAB4k5B0NyfmMHVcHYdYlSPUIKu9QibVkmmYtgSYXGR-woRJmt-WDCt2ZGOt4bqQYRgitKwnUBoAWOfj1crVkEGWO0Fbq4HN1pTUm5R-qSXvB5N9hRoFB1GWQiiBcicezBJzJ_zBeWOsehwVMI8ZM16fcW7GHAa1DHMemSFltAQ6glUR6ychL8CvdKT5AP5idiH60FC9_zKSTwELyl8n9iXsg762n6dkupIT3wOsewvsM89Lq7GouY8MaaofA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
یک هواپیمای جنگی آمریکایی در حال پرواز در آسمان شرق اردن دیده شده است.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139131" target="_blank">📅 16:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مدیرعامل روس‌اتم: حمله اوکراین به کشتی روسی در دریای سیاه راهزنی دریایی است
🔴
همه ۱۷ خدمه کشتی که محموله‌هایی مانند مواد غذایی منجمد و مصالح ساختمانی را حمل می‌کرد از این حمله جان سالم به در بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139130" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پرواز (گشتِ) جنگنده‌های آمریکا تو شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139129" target="_blank">📅 16:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا، جورجیا ملونی، و رهبران 21 کشور عضو دیگر اتحادیه اروپا، از جمله نخست‌وزیر دانمارک، مت فردریکسن، نامه‌ای مشترک امضا کرده‌اند که خواستار اقدام فوری اتحادیه اروپا در پی ورود گسترده مهاجران به سبوتا است.
🔴
این نامه از ریاست جمهوری اتحادیه اروپا (ایرلند) می‌خواهد که یک جلسه اضطراری وزرای کشور اتحادیه اروپا برگزار کند تا اقداماتی را برای تقویت مرزهای خارجی اتحادیه اروپا، مبارزه با مهاجرت غیرقانونی و قاچاق انسان، بهبود بازگرداندن مهاجران و حذف انگیزه‌های عبور غیرقانونی، اتخاذ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139128" target="_blank">📅 16:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بر اساس گزارش‌ها، یک رزمایش محدود و در مقیاس کوچک با مشارکت نیروهای مسلح قبرس و نیروی هوایی سلطنتی اردن در حال برگزاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139127" target="_blank">📅 16:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
واشنگتن پست: ژنرال الکسوس گرینکویچ، فرمانده ارشد نیروهای آمریکایی در اروپا، به پنتاگون هشدار داده است که تعداد ناوهای جنگی دریایی کافی برای محافظت از اسرائیل در برابر حملات موشکی بالیستیک ایران وجود ندارد، در حالی که در عین حال نیازهای دفاعی آمریکا نیز باید برآورده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139126" target="_blank">📅 16:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsfXSk4eRAXcURkkuIKBce4pr7c3BU39aUtdkQ5Cq9gh9fnuU-oX7qwqG2P9RL-HDVn9Ebk8DeyZNKM2SbUJH-UrEvPgsvDOgMj6lwVLRQK5XVK2GeSqeHv_IAUtZ907TDUSSI5TlEfR1YZbQ0sBmOHb7dT4hjjrcH2MZ6GonmLmhSYtxN_QMwCrFxf-KOsvRoKra_gGPrytTGJmDSnIc2tCbjwSZqKm755xrHxG0HwQyTa6W_CEFu2zl_l7Fc6Pup11zVmCu-Os75uh8Xl8BDxARAf-zRke5xrDuxjmXoypixn1BnkrNNOiVyFptEj96CmFJqtDZPisp-dprR6lcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک مقام دولتی:
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/139125" target="_blank">📅 16:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=fgtHd43gnh7WoCCxzy05wFsy5iipP5XK_hflwrrzikWPKXnoFpnDjkvhASrUIB12MCju1IJmlblKCcKpx9fai5VaisV_AkW4TT09r_Wxw8yNSsVYuvJxJ26G7wntb38rpBNPjXfL-SqcnaPZnsOM7zLEACrxACvdQafN6R4VrlvYqvXmA91C4HZBLIwBJeAn6o7JSM6jCiMYCFawTN31BBn7VGYvc9MWBDvCRmhSZwzyiO43EaouQGvf10PPBPVT0DxpJm8RDaxdFTEQ8Gi4hAG2dPoemoG_a_h_I8At-ly33qct7COWlstCF2pI03WlZ0lrwjhBUt9xqzAb_3FASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=fgtHd43gnh7WoCCxzy05wFsy5iipP5XK_hflwrrzikWPKXnoFpnDjkvhASrUIB12MCju1IJmlblKCcKpx9fai5VaisV_AkW4TT09r_Wxw8yNSsVYuvJxJ26G7wntb38rpBNPjXfL-SqcnaPZnsOM7zLEACrxACvdQafN6R4VrlvYqvXmA91C4HZBLIwBJeAn6o7JSM6jCiMYCFawTN31BBn7VGYvc9MWBDvCRmhSZwzyiO43EaouQGvf10PPBPVT0DxpJm8RDaxdFTEQ8Gi4hAG2dPoemoG_a_h_I8At-ly33qct7COWlstCF2pI03WlZ0lrwjhBUt9xqzAb_3FASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مهیب یک کامیون سنگین در روسیه
🔴
یک کامیون باربری بزرگ در بزرگراهی نزدیکی روستای «مارچوگی» در منطقه پرم روسیه منفجر شد و شعله‌های عظیم آتش تا دقایقی به هوا برخاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139124" target="_blank">📅 16:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwnUXXCpx6y-Ew7hURGiCLOTDhT3IatcDCstzHAK-9NigD3H7ai3azgpTtj-MSXEWtCJdR-uIpuDf7jSjoMgk-YGN9wyAusD7eyMrvOm3ie_tbTfCdVH1HIcKQTPpA4K8V54AzR6LIueFv6gr5kdSSMjJTijHBVReQCJayyKzAOSZA01zV8x1iLJX2FXX5HfEMv8qIoT_nmxP0rYrBUB_F_G459zDwJmii0ZWBqPM3N7Rhck0V2m4USAwT9UovnkSdxMfInl1qm1CuvHiVAtbS8c8DtgQdROwH1a-49pj3BEuWFaQOCHlEfgGmJabtflaIc1XnSNO3mBABOMyjJ76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز صبح "آروین خیرخواه" جوون 20 ساله‌ای که تو اعتراضات دی‌ماه دستگیر شده بود، به اتهام محاربه و افساد في الارض، تو زندانِ شاهرود اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139123" target="_blank">📅 16:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxop0oZji2h9BKE72o09YlrMiPDxShPnTss3nte_xtjdPf-dODd6BhsLXIxmfoIQXt6SkTtcU5XHBfgZ2Ie2_y32jCALVWtN_NPPWGbEd07weY5u7MWBNsYoML7V6wjp9hrm3O4ACdb9pJWP8xKaWGk1vAnAPIRvJf4SSk_DzPTLFJZ6994q35afPWyfgF-TXwdegsFBOBqWLLtANkc6L3blBxf72QNnc9f1Kobn04wwljYHktoA8o2EUweiDIuQt2yfyttoI6XEuyM651TSQV-jbLhcVShy-Mqo7o6PtSzS6NZ-QMIjKc9qQPAuuI6dCsvUswfHysAcA6XHpc55Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از رذل بودن نماینده‌های جبهه پایداری همین بس که صبح تا شب میگن جنگ جنگ اما پشت پرده دنبال پناهگاه مستحکم هستن و مردم بدبخت هم زیر بمبارون
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139122" target="_blank">📅 16:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
طبق اخبار رسانه های داخلی و عراقی ، بودجه مراسم اربعین سال 1405 مبلغ 137 هزار میلیارد تومن یا 730 میلیون دلاره !
🔴
این مبلغ از ردیف بودجه عمومی برداشت شده ( دارو ، غذا ، آموزش و پرورش ، صندوق بازنشستگی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139121" target="_blank">📅 16:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پدرو ساچز، نخست وزیر اسپانیا، کشور هایی که مرز های خود را بستن و قرارداد شنگن را با اسپانیا به حالت تعلیق دراوردند، خود خواه خواند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139120" target="_blank">📅 16:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا، درباره فلسطین: به نظر من، حزب کارگر خیلی دیر اقدام کرد تا خواستار آتش‌بس در غزه شود.
🔴
اقدامات بالقوه‌ای وجود دارد که من در مورد سکونتگاه‌ها در کرانه باختری بررسی می‌کنم، و این موارد مورد بررسی قرار خواهند گرفت و در زمان مناسب اعلام خواهند شد.
🔴
یک فاجعه انسانی غیرقابل توجیه در حال وقوع است. ما باید هر روز به آن فکر کنیم، بررسی کنیم که چه کارهای بیشتری می‌توان انجام داد و حقیقت را درباره آن بیان کنیم.
🔴
شدت این فاجعه انسانی غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139119" target="_blank">📅 16:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZe3VcqvG-vPvQZh_twWIx-aBf9bwfB7cJcchj8IQp8iULpQZA0B_1riBgMko2OZ-H6vdRiXNB-LjqTO15vj4Ky2uj6lUVDTml-douZnuOZfItzjaEKFBLWBmwMjhavMjFOZefGQHPYmdCPhoa74MLUYFOlB6i4eFsHayMEbp45ACY6cppSbrxoO-dItUVDvo2klYJ_tIpKZqn1c1BJiCyHAtNfdnaynKt1jBzyhx6QljkOYPY0wyAsR6r_WCo1ve5zwGvOPkPnaLkKp2hTN4Dqhu72X3aKhpdHw1lxxbA3XndlpvgJip_NCPGZgJ6VoAqJCPNlVAQW_4bblO9LF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPiBw4CVwofGAy7QBCfGlIZ0nhu5lIOEXikbxhGLO4lF9gvpUDlIVtu-zZRAnONhLnGonSptUohZuym5u5eH5VnWIEnOTBW7Ra8upcaqvLkjAUOJ8fc0QhGOnl-p7dBZRq6lOaFdkc7VyA8SoHE2YwcJbFy6GmlY_OWSfELXkXo6K6z77R8K3sAwrtynOtmyaxIL3PmjzS1UuQt9QLIK3l8w5asGveKGwfoFw1nF3dGaHdJm7sPhVPNJ3VJ1zwCKkWHwhK3gDDitAZ_bSlRV67KyPmw78Kbuo8NT8NYlvOMYeBUKD_wsH3JbeFy922mme8GN4mf7ExtZlHghiUhsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3jf2KHLHDcZTvt29qPwGfe2UWT30KzJ55GqXg1ecOPS3ZXywskBCoW1rYQj6nU5G37JC6APPlvUCAo1z4sVMMGDbHVaoYJbziy5EPBISr8dPG3uf87miNf1ZazqG8f9K4nbv2cqeQ-jKpg6bVnjhFWGMrpfPzKCHfzPaVM-ZqES8_Xr6umkHLolKon-yzLPS_Ovy2rk0hfMXGPX1jLKsfT8Kiah1i12_aN6AAh33WW-g_P0ub3GLagt4wWezSokoZS-b6MKdSon4nIGLoWnNGnsAa1UC1LdRdL5mp8bQ05RYMJ5Lw5GSEs-cAk3K1DRhvxKu0OmAIg30cv2cD0HkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید از کیف حین حملات موشکی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139116" target="_blank">📅 15:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e99e305a.mp4?token=vvKIycj0CHe52HjQjc9JKhLVEjdGcC5MaMcERYVEIV9KobPb79yYmeYmNskpEsHcgeBx1SgHoBo00D0Lm6WCaid67hlWBCrZvYhXz4DwwiLkrNmtkwtqpnEB8CNVoFy-f5-kr87Gm54JyVzbPZ-BGuUll1bODBpLM3IsRWoqmOE7wO_vmF9zS4pZ4JXChp0XrxuzXeemCGBq9WwMNNBWTL50Oj5a0DkfKQOE6e-kljMlVT0Ql_LZbuHZ5kzlcQoVXH66bXJ_69kNjcQfX-eMV_1dC4_KZGMWwUEyuaNJnQ76cCaZkMpH_PFqIO8LLOquZ2DpQC4nnMJfJ5T4gAj9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e99e305a.mp4?token=vvKIycj0CHe52HjQjc9JKhLVEjdGcC5MaMcERYVEIV9KobPb79yYmeYmNskpEsHcgeBx1SgHoBo00D0Lm6WCaid67hlWBCrZvYhXz4DwwiLkrNmtkwtqpnEB8CNVoFy-f5-kr87Gm54JyVzbPZ-BGuUll1bODBpLM3IsRWoqmOE7wO_vmF9zS4pZ4JXChp0XrxuzXeemCGBq9WwMNNBWTL50Oj5a0DkfKQOE6e-kljMlVT0Ql_LZbuHZ5kzlcQoVXH66bXJ_69kNjcQfX-eMV_1dC4_KZGMWwUEyuaNJnQ76cCaZkMpH_PFqIO8LLOquZ2DpQC4nnMJfJ5T4gAj9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات آمریکایی
:
احتمالاً این حملات می‌تواند هر لحظه، حتی در پایان این هفته، انجام شود. در حالی که ایران اعلام کرده است که در صورت حمله آمریکا یا اسرائیل به زیرساخت‌های حیاتی، آماده پاسخگویی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139115" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63b8ad888.mp4?token=cSJojMCZAKOc58dZlbU13I3pw54dwkJABg-72_X-wNXk4GO64cEahDmSQSANAGFmnB80ikokA-ldgn4eTr9L7d1On7i_8Vw5OjcApAeCi4YDdAJv4nukWlsLHWRTl-gpnisl6HwSKPEJSOTDk8iAtYUu-cvoqII0LBToj7xTjgBE5oClcfEhtyFKtiBwKZVbB-O58FgKo92I678-VJ_0XKqnzDAK7yuOFpVQWMmQMSd7M77kiCA0CyVTTB65IT6eDt5ZLh2nHIkEPJVIvSbrwjhlV5iUjFpOPOAyoIQekIPm3_UyCos3_AQuYqm2R4HMW7I20SoqzBe104ihvrEbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63b8ad888.mp4?token=cSJojMCZAKOc58dZlbU13I3pw54dwkJABg-72_X-wNXk4GO64cEahDmSQSANAGFmnB80ikokA-ldgn4eTr9L7d1On7i_8Vw5OjcApAeCi4YDdAJv4nukWlsLHWRTl-gpnisl6HwSKPEJSOTDk8iAtYUu-cvoqII0LBToj7xTjgBE5oClcfEhtyFKtiBwKZVbB-O58FgKo92I678-VJ_0XKqnzDAK7yuOFpVQWMmQMSd7M77kiCA0CyVTTB65IT6eDt5ZLh2nHIkEPJVIvSbrwjhlV5iUjFpOPOAyoIQekIPm3_UyCos3_AQuYqm2R4HMW7I20SoqzBe104ihvrEbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش یک هواپیما امبرائر ۱۴۵ از باند فرودگاه شیراز خارج
شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139114" target="_blank">📅 15:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به خان یونس در نوار غزه باعث زخمی شدن چندین نفر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139113" target="_blank">📅 15:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / گزارش بلومبرگ، یک نفتکش قطری حامل گاز طبیعی مایع (LNG) به نام گاسلوگ شانگهای، هنگام عبور از تنگه هرمز، شب گذشته در سواحل عمان مورد اصابت یک موشک قرار گرفت.
🔴
این نفتکش در ۲۷ جولای گاز طبیعی مایع را در قطر بارگیری کرده بود و در ۳۱ جولای در نزدیکی ورودی غربی تنگه هرمز، ارسال سیگنال AIS خود را متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139112" target="_blank">📅 15:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
برای اولین بار، سفارت آمریکا در قاهره هشدار امنیتی صادر کرد و از آمریکایی‌ها خواست منطقه را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139111" target="_blank">📅 15:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JY4S6HnFkB4njGjkncl1r2McbEUkxIzY62bBGiamTTU6CqpPErz9r274PuGUR1v-JRc6n5GyCo4SrLAllf-kMCXhXzD5oLtv877nTr6Pa55iLyUKRZDt78w3JeJ3X1l-0GXDnRHRnW9WmZhR88Jpk9BzxTgtkEdpL64XpjEMYqvo60mR_Mzo7PWexrZhMOagqN4qvqRachQve0JQmv86syWEGqcZEzTvFvS6d6SafAstgpt9gqdYBl8flXWwcLF5gZPTMofgRFRvhOcqFQ0JLEQRW6tCBh7LbFAnjaeaWxM57iZeS-xG8e4zxS268rd4ejXZtYweLOGov6fS1V_5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIJblLgb8AyDtVcvXezpplLgNkiVzxwkjD-XYpmAXWXK_nhv8Xlv82tF5CDXXamAtKCoiIEzhWvRawIzPtnXa63k_-cULL2xgg9ZNecGPvYufEe3-z9AFq5VBNmxsLlxGqk0IQJS14FVOVTiw9som9ojmkr1YTSkCL-1iz-8Ee7OzAfDlLuc5e7KnMqogGDwczftk6zIhKk-1cbdeDSJXkwZyPlxphTuYdrtcX23C_7UloTbQuZG0ndofoxADmBYPKJCdkd1jlEhzPt9vhzQSNyfMTqgMWz77So4mbKUGK4yu-YjagdbyjePk7EYNESKplGapiDIqHwqSNv6cCUR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9Pe2ovJH3UZo8NDDVGzP8G3C74jdfIS0P7NYjjwbR2dXhPltanIqsTq_vVeSvfPdgG0M5iA41dk56ZiselOGsWp5LlY5XHFzGIPRlmaAleLeu80LjaVRirphiZsmwzMEVRhTDXYpW_FnBfj_KOmbhEQDT3ghzIWUGdHH_MnVA06oOg4LhNkeIkyPQYj_HH6rOUfA9HR-1iOLCGMvVS17r8pSdK78dQD5fZmB_pUgVKshsOtyqMyORTvYAecALxAurOIzNtooI4-tSBPTa1tjh3cEtMibF00rRJQqshKiUmpR3RXX-HDPdWEpLaxoub5JjAKeHhyc5YSEZcfbFjgFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سفارتخانه‌های ایالات متحده آمریکا در قطر، بحرین و عربستان سعودی، همچنین به شهروندان آمریکایی هشدار دادند که منطقه خاورمیانه را تخلیه نمایند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139108" target="_blank">📅 15:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOsDcwL08p3wX9wKYq4-YMdsEO5Ry3R4A6IgTkUmxh5JC7_yjzDX3ORMrJy11Vyh_k1KLdnLR74Ykibf7Q8OVtDGNYPM-XlwTePlcZ60zm29cNBb4L_LplhG3Ze3B2SqWSe9sqldI3i-Pu0tfEmHyvml__Hkd9kruwMUoAQgQ4pz39_eNCApDLuqYnOXBHpFtKF1ynvqfUVKPM21SN3hYPH5yxK0jjCIZX3SA2GkJZJbq_RujmhNOQ0dHQ-1s57e9PIcaudmlftKygLuX4ijTn6AslYX3TMrX7SB-kceOE5ZzbJU6AOi4vGW7EHpJWI4t3O3HdbjZxt939H_ndczjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: اگر سناتورهای جان کورنین و تام تیلیس، که هر دو از من ناراحت هستند چون از آن‌ها حمایت انتخاباتی نکردم (یکی شکست خورد و دیگری کنار کشید!)، حاضر نباشند تاد بلانش را که به گفته همه یکی از محترم‌ترین حقوقدانان کشور است، به عنوان دادستان کل آمریکا تأیید کنند، من او را به عنوان دادستان کل موقت نگه می‌دارم.
🔴
هم‌زمان با قدرت برای تصویب لایحه مقابله با سیاسی‌سازی دستگاه قضایی تلاش خواهم کرد؛ لایحه‌ای که به کسانی می‌پردازد که در دولت جو بایدن و اوباما به‌بدترین شکل با آن‌ها رفتار شده است (در حالی که با من هم بسیار بد رفتار شد، اما من چیزی نمی‌خواهم)
🔴
تاد بلانش صدای عقلانیت بود. این موضوع فوراً دوباره روی میز قرار خواهد گرفت و من آن را به سرانجام می‌رسانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139107" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تعداد هواپیماهای سوخت‌رسان آمریکایی مستقر در خاورمیانه به 113 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139106" target="_blank">📅 15:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عارف: دولت برای دو سال آینده حتی برای بدترین شرایط برنامه‌ریزی کرده، اما حفظ آرامش مردم همچنان اولویت اصلی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139105" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بلومبرگ: کاهش ذخایر، بحران سوخت در ایالات متحده را تشدید می‌کند؛ آمریکایی‌ها با موج جدیدی از افزایش قیمت‌ها مواجه هستند، بدون اینکه از بازپرداخت مالیات فدرال که در دوره افزایش قبلی بار را کاهش داده بود، بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139104" target="_blank">📅 15:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و قبرس عملیات گسترده‌ای را برای مختل کردن سیستم موقعیت‌یابی جهانی (GPS) در سراسر هر دو کشور آغاز کرده‌اند که دامنه این عملیات‌ها به لبنان و سوریه نیز کشیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139103" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال: ترامپ، در ساعات پایانی حضورش در باشگاه گلف خود در نیوجرسی، طرح‌های جدید حمله را که به او ارائه شده بود، تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139102" target="_blank">📅 14:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / سفارت آمریکا در اسرائیل: آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139101" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سفارت آمریکا در عراق: به شهروندان خود در عراق توصیه می‌کنیم هوشیار باشند و از دستورالعمل‌های مقامات محلی پیروی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139100" target="_blank">📅 14:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/139099" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه امارات و انگلیس درباره کاهش تنش‌ها در خاورمیانه و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/139098" target="_blank">📅 14:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اداره کل هواشناسی استان تهران نسبت به بارش باران، وزش باد شدید موقتی و گاهی رگبار و رعد و برق در مناطق شمالی استان تهران هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139097" target="_blank">📅 14:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قیمت دلار به ۱۹۴.۲۰۰ تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/139096" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/139095" target="_blank">📅 13:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1VQzmnKm63z0sHI0ZeZXWv151duACtLxQo6dFbs8lamFQUyngCZVUBd0jsDpfFt5SSKCzCq_bKMnCMf4T6BP0H8d3uFYlke55Qws5_mamDkrwsC6UBb8s4Yp7FMPqvaW0ZJL4jlTBheY8wW3N_jKz56fHF5FkiSei_itTXs2bhGB8fQ9TL_HTGMsDvVmndSCteMZD0i6TyOmH7CGhT-SVDnTQ12m7PyWNRzlLiIO8n2zh-lF2D5Ldnrbox9tZXQ1_w0yQuwOnB6V-_DL4HdM2cndKy3zyB0MQHKQEHkS_nrDTqO16UJQcfYDCX83lLbH0B2LTtuG_LlAMdq2fnnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده شود، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم؛ به نفعتان هست که حماقت نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/139094" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/139093" target="_blank">📅 13:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139092" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر کشور اسپانیا: شمار پناهجویان [مراکشی] کشته شده در حوادث منطقه سئوتا، به ۶۷ نفر افزایش یافته
🔴
کسانی که به صورت غیر مجاز وارد سئوتا شده‌اند، هرگز اقامت قانونی نخواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139091" target="_blank">📅 13:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / پاکستان به ائتلاف دریایی عربستان پیوست/مقر این ائتلاف در عربستان سعودی خواهد بود و کشورهای عضو اولیه آن شامل عربستان، پاکستان، کویت، بحرین، قطر، ترکیه، مصر، اردن، یمن، بنگلادش، نیجریه، سودان، جیبوتی و سومالی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139090" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
درگیری دو باربر در بازار تهران بر سر جابه‌جایی یک بار، به قتل یکی از آن‌ها منجر شد. مردی حدود ۴۵ ساله پس از مشاجره با همکارش، بر اثر ضربات چوب جان باخت.
‏
🔴
کارآگاهان پلیس آگاهی تهران اعلام کردند عامل جنایت بلافاصله پس از حادثه از محل گریخته و تحقیقات برای شناسایی مخفیگاه و دستگیری وی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139089" target="_blank">📅 13:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc1_TyUfdxvQaTQDieRKvXcUu23b6UmPi0HURQ-PwQMqOre66szHCu-mRjxZGXzIMwrWLcZgwyuBi3ZTm8HrTA6zqjnWMsjMnxRqEp-6hTyWHzQcQWxdhjK656PoAQZ2DhuU7vFvCkVHCTO9sPUupXaNc8bs36QSDhllM6UcbIHA52AaSfKJsNV21PTTTJKjzeYv02QqDZmX7byjCFG8uuWJW6EFvMKGL-k2TUyKJWYVBoQ8JBJWJqbDILNcoDzuaEdOwEZyd-ZfiirTGbjg9sFXss00CJs7rmZ3GnCWjUHlfmw1XzU7WU7K8-KfXIYXE-RTltrCBYyM-9ix9EiEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / مجلس با رأی اکثریت، وزیر آموزش و پرورش را به استیضاح دعوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/139088" target="_blank">📅 13:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دو کافه دیگر در تهران پلمب شدند؛ مراسم بزرگداشت شاملو نیز لغو شد
🔴
دو کافه عمارت منشأ در خیابان نوفل‌لوشاتو و کاما در تقاطع سهروردی و عباس‌آباد پلمب شدند.
🔴
همچنین، مراسمی که قرار بود به مناسبت صدمین سالروز تولد احمد شاملو و هم‌زمان با انتشار مجموعه جدید آثار او از سوی نشر چشمه برگزار شود، بنا به اعلام برگزارکنندگان، «به دستور مقامات» لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139087" target="_blank">📅 13:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUV5sTXuG-tMYXiWTerKO9qeP6Q85meK8vOzbHo2cC9pNMztMYrKa4ndIQbXRx4yG21s_TY0MJo5_J0N4QPlP-f0lfw0fO3g4tBHhB4YYYSdFaaa041yH5O6dk52NsehcGl1J173D8nbD-b8AuhX_baeI0HIBRvcpyyRyeYtKWv8q26mkKU4_YffyDEjaXvP4WmOL210MLyFTPvrR8NOhpGmlVKw6tucgbDJnsBtCp-ASrl-1wM1jBfa0103sgyC_O-txVVRyQynkd5SWCFqXqZqZmMxLj9E7i_QpO7zIFQB8r7HkbsDmDBI5_GG4WZ4vhETWxyf0rwa9G3CAd7TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون سابق بازرسی قرارگاه مرکزی خاتم الانبیا در واکنش به تهدید های ترامپ:
اگر به ما تعرض کنید، سیلی محکمی دریافت خواهید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/139086" target="_blank">📅 13:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا از استقرار راهبردی ۴۰۰ نیروی هوایی خود در عربستان، کویت و بحرین خبر داد؛ این نیروها از ماه مارس برای تقویت پدافند هوایی، افزایش توان هشدار زودهنگام و حفاظت از زیرساخت‌های راهبردی کشورهای حاشیه خلیج فارس مستقر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139085" target="_blank">📅 12:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بلومبرگ: بعد از تهدیدهای حوثی‌ها
دست‌کم ۶ نفتکش عربستان به‌جای عبور از دریای سرخ، از دورِ آفریقا می‌رند
🔴
این مسیر حدود دو هفته طولانی‌تره و نشون می‌ده
🔴
نگرانی‌های امنیتی و اختلال در حمل‌ونقل نفت توی منطقه داره بیشتر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139084" target="_blank">📅 12:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ذخایر استراتژیک نفت آمریکا (SPR) هفته گذشته با کاهش ۳.۸ میلیون بشکه‌ای به ۳۰۸ میلیون بشکه رسید که پایین‌ترین میزان از مارس ۱۹۸۳ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139083" target="_blank">📅 12:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اکونومیست: رئیس‌جمهور آمریکا در موقعیت دشواری قرار گرفته است
🔴
تشدید جنگ، اقدامی پرریسک خواهد بود و پذیرفتن کنترل ایران بر تنگه هرمز نیز در داخل آمریکا برای او شرم‌آور و در برابر متحدانش در خلیج فارس غیرقابل‌قبول است.
🔴
به‌نظر می‌رسد فعلاً ترجیح داده است برای خریدن زمان، دست به تعلل بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139082" target="_blank">📅 12:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
آژیرهای خطر در کی‌یف، پایتخت اوکراین به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139081" target="_blank">📅 12:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efghBcsxBMAtbfjvpwOCwKVpR38JQ_08OhbDx4OkCK3LojxpwGiz_i9LtnibQ4LxUAdiPtUFjKlHtZG1wahcq7qLQ9N7DLaJ15-KjDK53S9gW_prrEnnNzHrmGv2_FF15j-pp3eoNg_1z7VwBseiksUCvv0BMsS6DMPuEx-nblvcUb5IjLMLyHsttEIxznUlVXRK4D5QwlM-U7s-GaoITbK6lKPtS1h6PmqYQdCLEg6z4XcPJHA4-HkIN0-hwk3gSGrrb_5X5Ecjbyw1iXHBelUS4AR-9wBZ_Fh6N33N7j8VR7CMZwRJ2Y7Yqie0zfjeVDBz9N6VaBKn1kXxcVe6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده نزدیک به جلیلی: باید برای ما مسئولان پناهگاه‌های امن تو کوه‌ها ساخته بشه تا تو بمبارون آسیب نبینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/139080" target="_blank">📅 12:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم : هر کشوری که خود را سپر دفاعی آمریکا قرار دهد، در آتش جنگ خواهد سوخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139079" target="_blank">📅 12:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سفارت آمریکا در اردن از شهروندان این کشور در خاورمیانه خواست با توجه به احتمال تشدید تنش‌ها، خروج از منطقه را در نظر بگیرند یا برای ترک فوری منطقه آماده باشند.
🔴
این سفارتخانه هشدار داد افزایش تنش‌ها ممکن است به لغو پروازها، بسته شدن حریم‌های هوایی و ایجاد اختلال در سفرهای منطقه‌ای منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/139078" target="_blank">📅 12:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3f1b61e.mp4?token=I47piY-i9VNqbMm_QfEPYz4IelK0tLWLGs5U3JHNaplswGtPlnKqUvY0lCCHt45RyIKKUQnzCK8pbPxi8QOmzG10smSYVJY_f4rgOMf01iz4n4tSehqSSv1RMd1cNjFLoUYK2XiuW6vOb8jAYPRyiCTXSB_KmddS0pGbIpGzilwbAXJzgIfKZfb6fbHH5kdELmKr5-J1EU1l-R-7eNkelZTT1ndw0ZwHGbtDiP2cya5gzbOaBa_Yq4SXgxrUSpACujbWJtO-G4n5w3RIwT8HHS_G-76elMd_D4flAJvtRXo73WrCfXN6JawNumz3flR098wAmfMztxkSKSulxPjEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3f1b61e.mp4?token=I47piY-i9VNqbMm_QfEPYz4IelK0tLWLGs5U3JHNaplswGtPlnKqUvY0lCCHt45RyIKKUQnzCK8pbPxi8QOmzG10smSYVJY_f4rgOMf01iz4n4tSehqSSv1RMd1cNjFLoUYK2XiuW6vOb8jAYPRyiCTXSB_KmddS0pGbIpGzilwbAXJzgIfKZfb6fbHH5kdELmKr5-J1EU1l-R-7eNkelZTT1ndw0ZwHGbtDiP2cya5gzbOaBa_Yq4SXgxrUSpACujbWJtO-G4n5w3RIwT8HHS_G-76elMd_D4flAJvtRXo73WrCfXN6JawNumz3flR098wAmfMztxkSKSulxPjEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه دستگیری سارقان مسلح منازل چهاربا
غ
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139077" target="_blank">📅 12:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e157b43618.mp4?token=ZLb5IgR7LQW5n4EynIEdebzq9UcKCz8jOwc7GqiMZFOQy5Vx2q0yAVHcuaLRd_43q17fWmsHtqzazJPBVY1V_Xe_TcyPVeFbrkqDI9qFNIpj8rYYPAzrEs7Z9faq62ScJyKMlrLyTi8FguUlZaSCQ0Hx6P0tYEeTsCKQ4jxHCRN19ov7rj5IOsShsRqvw2RK3kxI9RhHRhIgU0hcgsmuy214SmB2IRBJPUUTFjN_RXh2JN2Smbxxd3gw37H5WrZoP1rXQMboV5xKB9whK8LAPhWZtEHRC5nt6SaNZkabOsbuJNZsrV4NYU0Bp4uywTgfXFP9je71vAJ7GDra7JVLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e157b43618.mp4?token=ZLb5IgR7LQW5n4EynIEdebzq9UcKCz8jOwc7GqiMZFOQy5Vx2q0yAVHcuaLRd_43q17fWmsHtqzazJPBVY1V_Xe_TcyPVeFbrkqDI9qFNIpj8rYYPAzrEs7Z9faq62ScJyKMlrLyTi8FguUlZaSCQ0Hx6P0tYEeTsCKQ4jxHCRN19ov7rj5IOsShsRqvw2RK3kxI9RhHRhIgU0hcgsmuy214SmB2IRBJPUUTFjN_RXh2JN2Smbxxd3gw37H5WrZoP1rXQMboV5xKB9whK8LAPhWZtEHRC5nt6SaNZkabOsbuJNZsrV4NYU0Bp4uywTgfXFP9je71vAJ7GDra7JVLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔴
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔴
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم گرینلند می‌خواهند کاری انجام شود؛ گرینلند از دیدگاه ما مهم است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139076" target="_blank">📅 11:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5hnx50ipo616zIr1xEAbZfIV-Q1_cEmxIKkWia6EGcnHDi4qo7gHQmG7IsmyIX6ph7RWAVY2MI9IyjNz3MhO1EAlq3cw2k8o6HhdWEk3RjbKXXTqdFIncldfvAw6qfcdIPp9_mb77o9BHge-n20WlY6aifJhLqKSgnlgIJJqvFzFQS_kPbBISqOIIHRPTYEHhv2u8QPxfpklOmyV-VYUhG3itekJ5wz3XRbnLwnN2orcAvfk0hP_yvxCiR4nBwQVy74LIKTA_TedBZzaeI7hkuHtYNsKd3-aL4GJRC1BoFcWpC3Vf7FfI1vEA4CFkEFQzc3OEMsLyL1RqjUz51bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTQXgF4mvg8Whl-N0297JjrIEHr2hvkfyDndqgn0HeqECqBfvTdT05B9Fv0gBH-5Czr4t_ySbRnAS59PPD9yBqJSGulPOS-TBJyzl53dM8ZbELKXLGqe5gWIlxMHhkWyJOVo-G4tFs5BEAY7H3HGmZSxI2qL-dGvce5vc0oqsod5qPpTYkn0ucMBRTWpA6gxgrT19UddxWXe7M8qgnDed2p_ZRtEwRCvOQ88OnBDJ8jwLZDZIy026gNPrcCa7nEPTOQAsO3uNfZWqzRD1u3up2_AovE_12w-5KIdMwOccYh7P0RvYbxMTsL40gxG_dDpI4mHp21yByLC2SrSe9NZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uugs0FMCh8ELZZeNGquCIzFrzvBDavZSjwZSay7zbTwAG7qJ0j-JAbKoi6MSQ3HlWHvRTFfkGy1bT9cABgfHVAiFJnOXrY66mNI0drxwNZKCmezICrNfy-EskXzT-ZTT7RLgwU0FLfiglzDPkdkS2i5_u1ZkWM4ge8pAi-18z-JvCnSm-7SZ8sN3srrBDN9MdkxWr5833_NgVJlzE9E-QSjQWPGaCn9IYvF2omIVfn-0ltJ3YpHmCokWkPnxltP5DuleCehXOUamud5KwezwaWL7OBQmoNumebNqZV2hAsmrJRmj_SeClApOD47tVxSDI4LvuQoZZrDxOPqCqT9VBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrZGH9Nc4h8X9iJK9suS9uRMroqx5QZUAItnT9tGSzSJL6MMfDsBWeHRdW7Bfm817FLFSH6FcOVzhpAt_7txon5bC90yV3coYCyLbuqrsx-GYxZJdmvlAJhnvoaPtN6NJlp_mNmO3egwYIRDek2tHQHeRlNvudZnteRH3Yt7CjRM9JkRMvBKAhlT2pdZDUj0L9NytdxU0XYeG142O_EdsTcZ9VHXyDouZvxZ39NPicI5wZcZlSqtuqNHowZyvMiTq53XZvtieezsmILrxp8kz_GoZxgmJHW6i8PDNU4O3n384Zin9FN9hsAOav-qDZWii72oQuBCrBfHAyXpiWyRiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از حمله‌های دیشب روسیه به کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139072" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
حسین یکتا:  ما قرار نیست قصاص و خون‌خواهی رهبر را به ظهور موکول کنیم ما خون خواهی و قصاص را مقدمه ظهور می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139071" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=cQDZa6NPAjXU7kj8nI0dS_AqgJfPhgro_WHJXtUyulPa8SPdKo7a2WGUbDjWoeGp3EBWFp3HWjauNea_XQD4lbNDrgKp7KNRoJPof7KDaIb5t-7O8PdAhpIq26FkWg-oG18eOYHPSwJ8yNSUSOps07RLaLDslCg-f6TjRTC6B0zYCFjqCYIaEBM9qIWflS5uziFSAcEzmT9BctfmpF_MogaDubn5dikaQckjxHFpXvDCDl2WaZNwlVbfelkwuzVTJNlYi3GpD4jvDQDms1qg_Gfo97FQyK_U9i_2cvYYOYInKRWCgUUkEElnVw8BzdpIsl0JeWpyNYR7s37VCTDVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=cQDZa6NPAjXU7kj8nI0dS_AqgJfPhgro_WHJXtUyulPa8SPdKo7a2WGUbDjWoeGp3EBWFp3HWjauNea_XQD4lbNDrgKp7KNRoJPof7KDaIb5t-7O8PdAhpIq26FkWg-oG18eOYHPSwJ8yNSUSOps07RLaLDslCg-f6TjRTC6B0zYCFjqCYIaEBM9qIWflS5uziFSAcEzmT9BctfmpF_MogaDubn5dikaQckjxHFpXvDCDl2WaZNwlVbfelkwuzVTJNlYi3GpD4jvDQDms1qg_Gfo97FQyK_U9i_2cvYYOYInKRWCgUUkEElnVw8BzdpIsl0JeWpyNYR7s37VCTDVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: آمریکا و اسرائیل برای شدیدترین بمبارون علیه ایران، طی روزهای شنبه و یکشنبه [امروز و فردا]  آماده شدن و ترامپ دستور حمله رو صادر کرده
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/139070" target="_blank">📅 11:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبرنگار نظامی وب‌سایت "والاه" اسرائیلی:نشانه‌ای دیگر از تشدید قریب‌الوقوع تنش‌ها در خاورمیانه... ایالات متحده خواستار احتیاط و هوشیاری بیشتر شده و از آمادگی برای احتمال لغو پروازها و بستن فضای هوایی، از جمله اختلال در ترددها، خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139069" target="_blank">📅 11:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله پهپادی اسرائیل محله شیخ رضوان در شهر غزه را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139068" target="_blank">📅 11:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورش زندانیان ترک در زندان یونان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139067" target="_blank">📅 11:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW5ltn4dP5mAje2eu01Bt5ctLkWS4yKuQ70vDmVT0GQjejn1s7pxPw6awfhGCGIVM_ThE-fR-ZPhQT_oS0pDkGOPLcqEl2Z9VEJPVMTDo_qty6KAOMRnW7GBnkPAUqB4_QZfysxJmlYHbKJyky-yvP9u9IEO6mMEz0qtJM6BDtuy74jcJ6fr67pgct5WcQe-aJthz_QoEcKslhlRg-GUbvxPWY0UVRftq37T2hK-TkD9B-kCRlVjMnWOVvtXzqAH8DaH8K_Xwwpl8_jdHw1YtC0YQ21CfoXKj0xzYfuFdkApsRqiodDkEe5_BAvAzK269eeDIuOIpwx5li-Y4tkX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اتاق جنگ اسرائیل :
⌛️
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139066" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مارکو روبیو : طی هفته‌های آینده تلاش می‌کنیم
🔴
ببینیم می‌شه مذاکرات بین روسیه و اوکراین دوباره شروع بشه و این جنگ بالاخره تموم بشه
🔴
البته می‌دونیم هر دو طرف روی یه‌سری مسائل خط قرمزهای جدی دارن و تا وقتی این اختلاف‌ها کمتر نشه
🔴
رسیدن به توافق خیلی سخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139065" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn8y8XDuEqSn21RbGiqhEAspVuq3trRG_jBcf5A56LmU-LWWvPL2NQct-GqZcSNVTOJ6E-fWjYpoVmU60zOkKy0Lq7QUYyXpAMNXA5WnAkeKeuDt1-e7do4egZCvuUHAiHESzv3A0RfPICM6XSmgMxSD1qBuoG-1eXhQGDp_97CQvP7JlSVq3_3MneNO6Luo3vvCKTL1E-YdDPIm_DFQHuzry0lj9qDU-e6ElH3uHJnpVn46eyp1GUqJ2k4enmX_GLsjTVTPg3lyRFuBpJRpzGHJ7Q2N9kWc6FhGJlEBjqIazlQK3-rbZgR9GqTxcDtq0IbvVtacl4jeqXLdwBAN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نیویورک تایمز: بمبی که دو روز قبل بر روی یک خانه در قشم پرتاب شده است حامل یک تن ماده منفجره بوده است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139064" target="_blank">📅 11:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو موفق شد ترامپ را متقاعد کند تا حملاتی را علیه بخش های انرژی ایران آغاز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139063" target="_blank">📅 10:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی بی اس به نقل از یک مقام ارشد اسرائیلی:  ترامپ و نتانیاهو سه گزینه برای جنگ، از جمله حملات نظامی متمرکز بر مسیرهای زمینی تدارکات، را مورد بحث قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139062" target="_blank">📅 10:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBjTLfOG2kvTlDPBvh9GDQV_h8Q61MPD5YwOnS2sJ126-FsaCuz4OecaSeTFttdDK_6bDH_bNHFWFS4ki6Z8oWwYZKCT0QeOUTgMK8UbgwTDxidaYvh3ayBg9IGUuFezIRpX2YFe_n6taX_glihtFImmTkKXEpmVbKCR9XiDV0SHYPEgxs1jQfIgclf3b78M9tso1pQ6JfUXmSyJ1jxNNJqh_uPwcsWqdr9G6k5IyeeARX4nqS3CWaYehl5rI2fF2PfjwqkdTDdkKqYSazgg8G-ItWUNTq--3BMmodac5oUtXk_33-unmrR6iTxggKC1T50YEZPg0kszJqy0OpXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران با کاهش ۳۰ هزار واحدی در کف کانال ۵ میلیون واحد ایستاد این لحاظ که شاخص هم وزن ۸۰۰۰ واحد رشد مثبت داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139061" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:  تنگه هرمز متعلق به ایران است
🔴
ما به ورود آمریکا در تنگه هرمز مشکوکیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139060" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139059" target="_blank">📅 10:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ترامپ به‌طور جدی در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است.
‏
🔴
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139058" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
زلزله ۳.۸ ریشتری بویین‌زهرا را لرزاند
🔴
این زمین‌لرزه ساعت ۷:۱۱ دقیقه صبح امروز در حوالی بویین‌زهرا به وقوع پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139057" target="_blank">📅 10:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4mBrYvyJS889asiVxN0bCfZXl4ncQH-7m6_hK13HlYD5z9n8ol94AOztToHB1BDuhwvN6DTLaTdIzAbbkfbmBV-yEOFSxxhyN8rFbyY70cFnYeofScjD6Jb_74qIrLrbC3YGtZANi1e6yOqCOUxqYnc7axthjnxNfTFUVXbicAHmTy4VbIE2PSU1GQoLOZSm39ji5zP5bt4HLximTsPEHejoKdQsglkyBYd9vBnVDLlTILux7XNbV4Onfv7x7r32CO8Ei7MCNLhRqHbAAI3Xb4f7pqDY-MvoqpxhuXrO55TYjD9gKkNGzmB8977IAFfWdzSi9QwV4DT9o8YY57jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد فرماندهی نیروهای مسلح کویت اعلام کرده است که سامانه‌های پدافند هوایی این کشور در حال حاضر به تهدیدات ناشی از پهپادهای ایران واکنش نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139056" target="_blank">📅 10:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف:ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/139055" target="_blank">📅 10:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ارتش کویت از درگیری پدافند این کشور با پهپادهای «متخاصم» خبر داد
🔴
حساب رسمی ستاد کل ارتش کویت در شبکه اجتماعی ایکس دقایقی پیش اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139054" target="_blank">📅 10:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه ۴.۷ ریشتری جنوب ایتالیا را لرزاند
🔴
زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر شامگاه جمعه منطقه «کامپی فلگری» در نزدیکی شهر ناپل در جنوب ایتالیا را لرزاند و دست‌کم ۱۰ نفر را زخمی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/139053" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfTCJD3nUnM9p1Xxm9EMGLdO5KCG84Bgr8m5GwWzNfQOuZrhcYF77B3vh1rr9LD5jC_QMBq66NOOH7A0C0P51-yPIWsTzBszJ3iS74l-G87R2YHJwrCwroDz1WYishUz3uJnvK4OFxJU_fFamgQgXIi57mUbo_xKR4W4yLLeFVwD2qMENFk37lSuLdPjYcXhKAl-K01Mg7QGDF_kPNdYYz9CUl0gZqRyu1EHsR7BDnsUnn4VvkPOLBMkyP-Hc14yH3lTdyXiy5iysF66F_1cWebjOJv-CWDdxGZEekb-iVfEB5EOKu_sVLOaQ8slDTt73-YjiKF-2wXeDft9uOTF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: مشکل اصلی ایران و آمریکا مربوط به حوزه هسته ای و ۴۰۰ کیلوگرم اورانیوم است و بعید است با بمباران زیرساخت انرژی و هسته ای، سیاست های تهران تغییری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/139052" target="_blank">📅 08:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فاکس نیوز: موجودی موشک‌های «تاد» آمریکا به کمتر از ۲۷۸ موشک کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/139051" target="_blank">📅 08:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی کاخ سفید در واکنش به گزارش‌های ادعایی درباره احتمال حملات به ایران در پی نشست کابینه آمریکا در کمپ دیوید ادعا کرد: دونالد ترامپ، رئیس‌جمهوری آمریکا، همچنان به راه‌حل دیپلماتیک متعهد است، اما به پاسخ دادن به حملات ایران ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/139050" target="_blank">📅 08:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4bpMYchyJ86W5jml2mnPGS2VcSqm0-FyWciMOXbELh4R8Kgr7x8OCctXUgdVggyQQ8VlAzpeN_saTnNcCg2HL6jV1ljVbZyu15rMHaDYIEKONrh6mzkijz9YEZ6HAmlWYmwXXSH6YS-JXlLEwtLFMFRuShZhyJbG0dqlxJjjXJ82HYyLBs4oulFKQWhjh3yhMdRZ-vnFTE9l1fqVQbyhs6DDO0jiMmYf585n8GRHBt7gHvnZhHmdj5-X_aUo3siG01zNRc8JVb7Mr_yfta22gqzSEAtVcUNWx5iuX4mtENY-mw5iqrDPQyJ80GjLT3V_qHYV72pU1gSRhGpP3Uj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: آنچه که در اسپانیا اتفاق می‌افتد، با ده‌ها هزار مهاجر غیرقانونی که به آن حمله کرده‌اند، در ایالات متحده در دوران دولت خواب‌آلود جو بایدن اتفاق افتاد، و اگر دموکرات‌ها دوباره به قدرت برسند، دوباره اتفاق خواهد افتاد، حتی بدتر.نگذارید کشورمان نابود شود. به جمهوری‌خواهان رأی دهید و به ایالات متحده افتخار کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/139049" target="_blank">📅 08:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=DqxiyYI1QFP8pbOZafFe3UiWmRfxEmMFkZ5f4uVYtKre2Lu_KAM9XNmiEVlyJOjVtQuJLJTUmkgr6eo-bNDnXOPZLNy9WQOk7OY3wLLHf7dHTooUlAlKWWtQmwHn4ZLA8rAhwyHXPKTOSepPzTZNSLu_zCSY1fzXAG-mN2P56Xgh_pjrqpPNa211yv3F4Y_MyHjvpcz5TO61nBnnCNNDw3HBxO7UJjY20901J3baYGRX4gp-SBsKpPKlS7sPEqNZnmwD1yDRnVCQ4e3WuavoelDxI1xLbsJ8-oASZ_84RCAYtlDdb3voG8j7rtu9Ofu7KzpMKludMUl4W6yKnyPx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=DqxiyYI1QFP8pbOZafFe3UiWmRfxEmMFkZ5f4uVYtKre2Lu_KAM9XNmiEVlyJOjVtQuJLJTUmkgr6eo-bNDnXOPZLNy9WQOk7OY3wLLHf7dHTooUlAlKWWtQmwHn4ZLA8rAhwyHXPKTOSepPzTZNSLu_zCSY1fzXAG-mN2P56Xgh_pjrqpPNa211yv3F4Y_MyHjvpcz5TO61nBnnCNNDw3HBxO7UJjY20901J3baYGRX4gp-SBsKpPKlS7sPEqNZnmwD1yDRnVCQ4e3WuavoelDxI1xLbsJ8-oASZ_84RCAYtlDdb3voG8j7rtu9Ofu7KzpMKludMUl4W6yKnyPx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، با هشدار نسبت به پیامدهای هرگونه درگیری میان واشنگتن و پکن، گفت جنگ میان دو کشور «فاجعه‌بار» خواهد بود.
🔴
وی تأکید کرد وزارت خارجه آمریکا در حال انجام «کار دشوار دیپلماسی» برای جلوگیری از بروز هرگونه تقابل اقتصادی یا نظامی با چین است.
🔴
روبیو همچنین تصریح کرد که وقوع جنگ میان آمریکا و چین سناریویی است که «خدا نکند» هرگز رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/139048" target="_blank">📅 08:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فارس: مارو از زیرساخت زدن میترسونن ولی مهم ترین زیرساخت های انرژی دنیا در تیررس ما قرار دارن و اگه بزنن میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/139047" target="_blank">📅 08:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/139046" target="_blank">📅 02:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHRNe-KutDAgJnbbMhDyMYecE4TuFpGGN4LPjpJtunJCk0aIH1jxweJA36boqmw0EcW07TALAzVaQLy-DLV-SFEO49HGWs8jvOLogMAtRNv5mbchBilb32JRHdL-VgignPVS9Z1_Zyp3pH0Xqd6DU02Y2mWcYooJ15Fbg29PA_PyZ8JfiWvmHZ25IgFQ44tbERGNrQM69cEgnOQwWogZXxfx8bvLzYRhSknvPeIBtZFswimsDJR-kJLOwvZ1tO64lsvjDE0FPg7iPq3ZgK5aNvTKIARGvoc6gFcaE1x1jnnKo4KoKd_uB9-zXmC6N129r6TB_b0iS3L9KBoLTsKjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقال تجهیزات ضدهوایی به جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/139045" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
قشر تندرو واقعا احمقن، میگن اگه زیر ساخت مارو بزنن ماهم زیر ساخت منطقه میزنیم خب بر فرض شما زیرساخت بحرین و کویت و ... رو زدی. خب اونا پول میدن آمریکا بازم براشون میسازه و آمریکا سود میکنه، ما چه کنیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/139044" target="_blank">📅 02:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/139043" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان: ارتش آمریکا مقدمات لازم را برای انجام مجموعه‌ای از حملات علیه زیرساخت‌های هسته‌ای ایران، از جمله کوه کلنگ، فراهم کرده است؛ هرچند این حملات صرفاً محدود به این سایت نخواهد بود.
🔴
مقام‌ها گفتند که این آمادگی‌ها طی چند روز گذشته شتاب بیشتری گرفته است.…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/139042" target="_blank">📅 01:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان: دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/139041" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان:
دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/alonews/139040" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
طبق گزارشات به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ اینترنت سراسری قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/139039" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
👈
آکسیوس به نقل از مقام آمریکایی :
رئیس جمهور ترامپ به طور جدی در حال بررسی حملات علیه اهداف انرژی در ایران در چند روز آینده است، اما هنوز دستور نهایی برای انجام این کار را صادر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/139038" target="_blank">📅 01:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
طبق گزارشات ترامپ یک فرصت دیگه به تهران داده اما فقط ۲۴الی ۴۸ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/139037" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کاخ سفید: تهران تفاهم نامه را نقض کرده است، بنابراین رئیس جمهور ترامپ بیکار نمی ماند و پاسخ حملات و اقدامات ایران را می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/139036" target="_blank">📅 01:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بازارهای جهانی هم اکنون بسته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/139035" target="_blank">📅 01:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/139034" target="_blank">📅 01:17 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
