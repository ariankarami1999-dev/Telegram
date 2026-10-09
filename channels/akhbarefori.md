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
<img src="https://cdn4.telesco.pe/file/Omc2RfyXRMwm9N40octplrz-Kw2cj_33NRvXDHtSamGlDKKVZABlPrDojgpsQZ1mSiVUqXfGIs9qH3yrpDNbRUwpHk0KrojK_rhAZb_ulF76Ck4F-YLyLpz0Ar1HEzLrFFHQ1gRd03GAmX8djScUnEiGbOSj9H40OIObOD1qefvA70SQZOCPQ_56ng77rC4taXuw_IVNoikEv0fMO7sU5a3LjQRZ4AV7tZiieLmxcruP6L3Uaja3-VX5JvUQkCcXpWV5ZFElCCfL57S8fe1BVZaeYpG3zSMYhMF9BEKtB5HTbJS4253CxY5dmquP4SCoAaKjp0GYXdjGSkJQBH67pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-697077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرنگار ارشد دفاعی کی‌یف‌پست: ما در طول روز فقط سه ساعت برق داریم؛ روسیه زیرساخت‌های حیاتی اوکراین را هدف قرار داده/ وضعیتی که با نزدیک شدن زمستان، نگران‌کننده‌تر خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/697077" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بسنت: دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/697076" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5287688d95.mp4?token=g8LznVVEv4NHZpMFjVP4Bce5BaZSDck_ft4W8HLerdsfCjnYjbEVOxlCDNxBLZqK1xkQkVzdNamj4i80iPuH378OH_OaMo95PTr4a2uSguTLQpRKeRzm98Uja3CtIA_cMmqtMmk2Aun5zxqoz66Vso_q9pyUiN4IZiSic8xwtAaE0CZMUuYyxr9WR5g4WI4-Vq6z9nce5mn5NQmkXwZ8PewcOZ3KgM6CYrg4TXwT3xkFKAsdk9jC--epHf2lMjfWDC-yombGF_1rkdBQdy55RxMRRNjaaqZjjjIHc2sICgdXB0COuqzfRwnEc0XZ0Mb8scNBV1mDqEfExPV59LKQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5287688d95.mp4?token=g8LznVVEv4NHZpMFjVP4Bce5BaZSDck_ft4W8HLerdsfCjnYjbEVOxlCDNxBLZqK1xkQkVzdNamj4i80iPuH378OH_OaMo95PTr4a2uSguTLQpRKeRzm98Uja3CtIA_cMmqtMmk2Aun5zxqoz66Vso_q9pyUiN4IZiSic8xwtAaE0CZMUuYyxr9WR5g4WI4-Vq6z9nce5mn5NQmkXwZ8PewcOZ3KgM6CYrg4TXwT3xkFKAsdk9jC--epHf2lMjfWDC-yombGF_1rkdBQdy55RxMRRNjaaqZjjjIHc2sICgdXB0COuqzfRwnEc0XZ0Mb8scNBV1mDqEfExPV59LKQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرافیتی این توهم را ایجاد می‌کند که خانه محدب و برآمده به نظر می‌رسد
🏢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/697075" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پوتین: روسیه آمادگی خود را برای تأمین نفت و فرآورده‌های نفتی مورد نیاز بازارهای آمریکا و سراسر جهان اعلام می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/697074" target="_blank">📅 23:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزارت خزانه‌داری امریکا مجوز موقت انجام معاملاتی را صادر کرده که شامل فروش، تحویل، تخلیه و واردات گازوییل از روسیه تا تاریخ ۷ آوریل ۲۰۲۷ می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/697073" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f0886b31.mp4?token=F5PR5rdHCNkXeh021oprXPDzEsESmicv7yKetWAEV_xeNp3QML_qytmBWcG6-52HDgtRhoh3q5H9ma_jKPlRcU8IWSmRBRrY9FB5lceYSQdez54Y5-OALuUf4zpmaqMHcwukNK6MCNdEwLsh4oboS5vPMObZ3o6Ela6Yg1UKIfl-bZdY0Bh7fPCrzs8doWEXhRVdE6bGF-htVwzDy2SagAlJWxRqXfcfjUP8Q8Mw2AsVtpNoUZfz2HrH-a3duUYfsjZvRGAATLdUEsO0pshJlX0ndtYtk4REtHSp0VwJ1XMmTFOoq5dGhabqM_Xw-H685FRWzl9V6dvKy6qb0c7vbalW_0KWEOLWx30hSRVgHqcozOkJ1uecz6lz3wd1nwx1mPjY-8PsXs03qEjdh0vnwp7zqaBem7rBnsKUaKTCWVbYTBRmYfsz3dwwB0DiqjUbwAwpu81d1mFOhZmUCVSqRS2y4N9fgrSC5PXdOu-X9qRZlNIIPkH6Gynvsm8Ie618KbsBmCYdwUduk90ZMrZq-nzRskxm7Uir6nvpBWRDL3IQjpoGaD-I5yEQJxfdziO2ONov8m4Nu-lNTg0cGLO8R-3xPb7VJQWo38Xz4KvO-kIpq6AJklQPVHtg4jg-GdTy7ExgqaB_euQPkXldOjjOz-PugMbPvDB2daYuHeQowOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f0886b31.mp4?token=F5PR5rdHCNkXeh021oprXPDzEsESmicv7yKetWAEV_xeNp3QML_qytmBWcG6-52HDgtRhoh3q5H9ma_jKPlRcU8IWSmRBRrY9FB5lceYSQdez54Y5-OALuUf4zpmaqMHcwukNK6MCNdEwLsh4oboS5vPMObZ3o6Ela6Yg1UKIfl-bZdY0Bh7fPCrzs8doWEXhRVdE6bGF-htVwzDy2SagAlJWxRqXfcfjUP8Q8Mw2AsVtpNoUZfz2HrH-a3duUYfsjZvRGAATLdUEsO0pshJlX0ndtYtk4REtHSp0VwJ1XMmTFOoq5dGhabqM_Xw-H685FRWzl9V6dvKy6qb0c7vbalW_0KWEOLWx30hSRVgHqcozOkJ1uecz6lz3wd1nwx1mPjY-8PsXs03qEjdh0vnwp7zqaBem7rBnsKUaKTCWVbYTBRmYfsz3dwwB0DiqjUbwAwpu81d1mFOhZmUCVSqRS2y4N9fgrSC5PXdOu-X9qRZlNIIPkH6Gynvsm8Ie618KbsBmCYdwUduk90ZMrZq-nzRskxm7Uir6nvpBWRDL3IQjpoGaD-I5yEQJxfdziO2ONov8m4Nu-lNTg0cGLO8R-3xPb7VJQWo38Xz4KvO-kIpq6AJklQPVHtg4jg-GdTy7ExgqaB_euQPkXldOjjOz-PugMbPvDB2daYuHeQowOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس مسائل غرب آسیا در شبکه سه: ترکیه قصد ورود به جنگ یمن را ندارد و نقش احتمالی پاکستان نیز به دفاع از خاک عربستان محدود می‌شود/ تاکنون هیچ‌یک از این دو کشور برای جنگ با انصارالله اقدام عملیاتی نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/697072" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV_Tt14JyvG1FpOXrRgdTJpenM5qoc6R4JWYA8qNkf_aIpel9jcmYmcDSc1ZftTV23aDJOcYb0lU8ju0pXNENOR2CjZyUoGzDSwpH37hL7lTIiQi_9DT3u1xbQZXB1Y7jkawDeyz8qKMQ8XxdmcfLrLRHwdhCqT04Mi7fLU7S4RuTmhLkeQKkS6D6plg_3sMY-SR1VBPemxAeI1rnn0ETnVn8rRkWY7hTu5q-cxbYepcBawXIRQaQHa3LbwDUoEBKIROZbS1FI7cx7jBgJYA8hj9EnEu5A_V37iIMWZjM4GBE5Vyud3OXDEdC-oFmgT0n7BFypTleCPcehcUkPfeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه نهاد آبراه خلیح فارس در مورد وجود دامنه‌های جعلی
نهاد مدیریت آبراه خلیج فارس:
🔹
با توجه به برخی گزارش‌ها مبنی بر سوءاستفاده با دامنه‌های جعلی، تاکید می‌شود کلیه مکاتبات پی‌جی‌اس‌ای از طریق ایمیل و با دامنه
PGSA.ir
صورت می‌گیرد و سایر دامنه‌ها فاقد اعتبار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/697071" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFN6m5f_jelQw1GyRaVEfe9cSLqiE2lV1OIXT0ZVUTySnou9jvQNr5A7OOJ_2KAlQhrMD8LAeWHs-4EooDHW9V_iTfIzS6RXp96idJxDvksEwZD5OWKjHeETtYMenEzreOsHGW7zj29_E3jNo2IEzKl7mscaOmADrpnunNJ_2CQYPnDdLiZZ77sMPBqOqeP9Fc5Qgs4ZJYQ_5bPhFc6yOKOIrXuGMU4jlyNKbBhci8llcFeEk5f7umjtreEgOm8iF_T3IX8r3NfpbGTiCOFAT5Lj7AAiPm11-pNON1vM2VkdHrUg58mGBW2oa-I_HMta_vVq5HgLmbBdOBw0M23iSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولی نصر، مشاور سابق اوباما: به‌نظر می‌رسد روبیو در حال طرح نسخهٔ دوم نظریهٔ «برخورد تمدن‌ها» ساموئل هانتینگتون است
🔹
با این تفاوت که به‌جای تقابل اسلام و غرب، این بار از تقابل تمدنی میان ایران و غرب سخن می‌گوید.
🔹
پ.ن: هانتینگتون معتقد بود پس از پایان جنگ سرد، مهم‌ترین خطوط اختلاف و درگیری در جهان به‌تدریج از رقابت میان ایدئولوژی‌ها و نظام‌های اقتصادی به اختلاف میان تمدن‌ها، به‌ویژه تفاوت‌های فرهنگی و مذهبی، منتقل خواهد شد.
﻿
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/697070" target="_blank">📅 23:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تاج رقم قرارداد قلعه‌نویی را اعلام کرد!
رئیس فدراسیون فوتبال:
🔹
قرارداد قلعه‌نویی تا جام جهانی سالانه ۳۰ میلیارد بود که الان سالانه ۵۰ میلیارد در نظر گرفته‌ایم‌. عدد ۹۰ میلیارد برای جام ملت‌ها را رد می‌کنم‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/697068" target="_blank">📅 23:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b9bc7145.mp4?token=DEbEJ7DIvC7CdAqKCX7Dpg6ix_KqP0UxJG1uCNwU0xihVINjBNG366OM-10NaQYeDECqZjheoxrZqDpc8k8qJZTAGQuSF8YUuKZhRFc5nnl7OwwXBOPW9eg6ENkcegDckBjcNC9E4JySsd0EYMxAtE9dWtYKm1knrQx29bFDRuZJDxi2afsHh5mzxuxpjdSvC1gGUhR8PNuIOp_eUuNuBdLn4if5lQ-UIErUNk6fkNHdTu84cvg7GfdpzTKuRNl-A0AGKXS-MU68fJOOfmRlVr7cD80FJqSlGhLHTJU7o82pNXvR5INHgN-M22Nz6DBKuuQ-G5oiljgFUtNe1K0Eng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b9bc7145.mp4?token=DEbEJ7DIvC7CdAqKCX7Dpg6ix_KqP0UxJG1uCNwU0xihVINjBNG366OM-10NaQYeDECqZjheoxrZqDpc8k8qJZTAGQuSF8YUuKZhRFc5nnl7OwwXBOPW9eg6ENkcegDckBjcNC9E4JySsd0EYMxAtE9dWtYKm1knrQx29bFDRuZJDxi2afsHh5mzxuxpjdSvC1gGUhR8PNuIOp_eUuNuBdLn4if5lQ-UIErUNk6fkNHdTu84cvg7GfdpzTKuRNl-A0AGKXS-MU68fJOOfmRlVr7cD80FJqSlGhLHTJU7o82pNXvR5INHgN-M22Nz6DBKuuQ-G5oiljgFUtNe1K0Eng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در تأسیسات نفتی بقیق عربستان حکایت دارد؛ تصاویری از روشن‌ماندن مشعل‌های نفتی برای بیش از ۲۴ ساعت منتشر شده است.
🔹
بقیق از بزرگ‌ترین مراکز فرآورش نفت خام جهان و تأسیسات راهبردی صادرات نفت عربستان است.
🔹
یک کارگر خارجی مدعی شده این…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/697067" target="_blank">📅 23:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Ma6tUwZVhFksEnqjaRjhdNxkt5rLuc06DTB-9hyZNJg1MIafwDV3h9aw9iUB_-2VGARyj-Jnwum2sT_CBmt5JBUIJxe_vzaARSkGN44KaEW0DWePHcjnxgbRw5TCzI1RfDPCy9q9IGOLOilrmTI7dUn9nhL4OQO2EhZuPeEd7dk9qqrN8z9tzLvRkeGAFBVt1TV58uqA3wA7WbchqWX1d7EuFKD1j0M_bfPTa7Uhf1gE0k3_GEGPxkxyiAaoE8FUL3Ry5LWS8EWInaz6I7mn_BQijXDC1R6bNVOo83mSrLwXk6M2BydjRqZ4uYL6s9ekEo-idgUtpGwYx7Dt8acA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیوی انتقاد آیت‌الله مروی به قوه قضاییه قدیمی است
🔹
واکنش مدیرعامل خبرگزاری میزان به بازنشر فیلم قدیمی از آیت الله مروی و حمله به قوه قضاییه: دروغگویی برکت ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/697066" target="_blank">📅 23:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTprJpcdfDOCIcWL5K2OsyPSFrjuPl32mZFXA-2Nx96UwBKXAfmLoQ6xxmmWe1BBAKW4CpM8Delr_CHYcfIxctR88JWzXSNPocwBGnDEtqV0TDio3_kXxsZuLhnxoME6pn7tK3_S5kx38_5U-pd05SHZNtZAL3qTAQnzE2gNzS4ylyFsV193fsQoIg_BHgjYljojIyRPNA22-XQEx7LwiKAHYV4YsYb85PvkRK_YKvQAJsyIuPBMGzjtR2GZ75TyMbpRRUcljUyxsTm2VlUkoIiQp6obMku5l8f84iSrcNepg8DNCS3MPXHDnsIqbak_AVa6bwjk__zKcXUsbxYvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد؛ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/697065" target="_blank">📅 23:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwlgHJ09E3SUuZY0D93SZfVaaAUuXzcGeqf9f3Xwz9_RXfkWqDv__t3Drm-de6Cd3e8OnxxpD2mXreHu-E014rYPuAesZ00pwIJ6MBdiWoKzAbI86uqVYeW8pV_Tt-1m_-EfX4ZZlFS8VgT8AdoWACz1RsWjDkcw6sXGt5MWykLt_nCSFJR5WqoGjrh_MTV0n89B_Y9sR7VJw_1UxJwgq9mG8aQhHvpVCf1UDxFMhVTeEt3WA8ThtD6Yc90_Nt3iDxZk3ksqP-7KqW6ob5Sl0JQSKKGAZh12shyuFdmX7z-0mzITudxsSSphHIiI0AK_rJu9QlzG30pt4r5BaPi6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در تأسیسات نفتی بقیق عربستان حکایت دارد؛ تصاویری از روشن‌ماندن مشعل‌های نفتی برای بیش از ۲۴ ساعت منتشر شده است.
🔹
بقیق از بزرگ‌ترین مراکز فرآورش نفت خام جهان و تأسیسات راهبردی صادرات نفت عربستان است.
🔹
یک کارگر خارجی مدعی شده این تأسیسات هدف حملات پهپادی و موشکی انصارالله یمن قرار گرفته و فعالیت‌ها متوقف شده است؛ این ادعاها هنوز تأیید مستقل نشده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/697064" target="_blank">📅 23:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان10-میدان دهم تهذیب</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان دهم، تهذیب
🔹
تهذیب به معنای پاک کردن پلیدی، ناپاکی و شر از هر چیز می‌باشد.
🔹
در حیطه‌ نفس بشر خودبه‌خود مایل به انجام کارهای خیر نیست و گرایش وی به متضاد آنها بیشتر است.
حلیت‌ها بدین شکل هستند:
🔹
نفس را با سنت: از شکایت به مدح گراییدن/ از گزاف به هوشیاری گراییدن/ از غفلت به بیداری گراییدن
🔹
خوی را با صحبت: از زجرت به صبر آیی/ از بخل به بذل آیی/ از مکافات به عفو آیی
🔹
دل را با خلوت: از هلاک امن به حیات ترس آمدن/ از شومی نومیدی به برکت امید آمدن/ از محنت پراکندگی دل به آزادی دل آمدن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/697063" target="_blank">📅 23:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
کالا ۲ روزه رسید؛ اما ماه‌هاست که گیر کرده!
🐼
🐻
محموله‌ای که از آن‌سوی دنیا رسیده، چرا هنوز به دست صاحبش نرسیده؟!
📦
وقتی گمرک از مسیر تجارت طولانی‌تر می‌شود!
🎬
این انیمیشن طنز و تماشایی را از دست ندهید؛ داستانی که برای خیلی از تجار ایرانی آشناست!
🔻
ماجراهای راه ابریشم | قسمت سوم
📺
تولید جدید TOOSA Animation
🔗
https://t.me/toosaanimation</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/697061" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=HYb7pAg9ZeI_npbdyPxAzMaNhgMajwuTiE7k6yPe4gWaSH86yEevJX_AmqyrmSkMlYDOnoii9LYIdmzYC8EtN3b-_EaHftqItT5HKtylu1DbNiYmjHJMnEvn0eNCGT7sVyLlLhZuf1CcWScPNp8-MUvoRnnjXtFamX9TSL2CHvabP00km6bI0ATa10lGAV49Hd8K-4SLx-JKRNmtqOD-kS-PC1ZnIyctJ1pPRpP9l6vP_8IVyaOkrxsrUmH3X-RrPSoRuUiflgN3oWgrtLP46XlnAPRXMe4ccuWssXmhvQhyzfNkQEN7FegECuKFx44bQfvQjGqxm--3bfU5qFop1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=HYb7pAg9ZeI_npbdyPxAzMaNhgMajwuTiE7k6yPe4gWaSH86yEevJX_AmqyrmSkMlYDOnoii9LYIdmzYC8EtN3b-_EaHftqItT5HKtylu1DbNiYmjHJMnEvn0eNCGT7sVyLlLhZuf1CcWScPNp8-MUvoRnnjXtFamX9TSL2CHvabP00km6bI0ATa10lGAV49Hd8K-4SLx-JKRNmtqOD-kS-PC1ZnIyctJ1pPRpP9l6vP_8IVyaOkrxsrUmH3X-RrPSoRuUiflgN3oWgrtLP46XlnAPRXMe4ccuWssXmhvQhyzfNkQEN7FegECuKFx44bQfvQjGqxm--3bfU5qFop1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
🔥
این دریل رو می‌خوای؟ قسطی هم می‌تونی بخری!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل:
۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
✅
امکان پرداخت قسطی با ترب پی
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/fast/46482/180124/</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/697060" target="_blank">📅 23:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUogCDQYTFTsLnVYDX3gT6FeT9-LE7EqIMYaAmevIWmI6AdX2Cub2T55zXOQoCp5MIh46a45ifmTk6cBXrmUiWcAb2qw-Ep1NpadzEXalsA2TRsFaUpH4QwDlvJdu5ChRCGBzdO0FCQk8IexKhuCf1tfoR2oa-OHFgWlJts7Re9x0G-ShIa9Gt4PEHayIss1sAhfEtvelEAhNEb-2rdYts8iynn7AXuXFyk1QwJvanl7aVFyvInbHe_9lzOAQHXKvfTM3xbz0MQvEZCk7SAuQytF9b1YYqfv6Vuyx5wpuVrvzyhKbDL32Q5Y8Hh-2HiTkIXn-VY8BHybjA0YcNUQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/697059" target="_blank">📅 23:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
🔹
برخی خطبه‌های نماز جمعه ارزش شنیدن ندارد و باعث گمراهی مردم می‌شود.
🔹
پیغمبر و حضرت خدیجه خودشان هم در شعب ابی‌طالب زندگی کردند اما اینجا مسئول جمهوری اسلامی در شمال تهران زندگی می‌کند و به مردم توصیه زندگی در شعب ابی‌طالب دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/697058" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697057">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB__BA5LXmYdYgKYlGDYO2-tURHIjGwhHdiujw23Yp4mQbE0mAPYiKRlf-bl44W7CzWFNijPNcCS3NBZ1bi67aefA99DX80rohKh0Tyq9ObmIkNlzbBGumBIXnp-3iO5rV6vWrABAiJTLcmiOP_t9rn2a39lf_f1fHBIm21qn39W34BnTnEd7OBrS_QfAd7KYsbrfe7AAGYnCezKQMyEUrW_qc8KJCfqd4OdMHplKtRV2oij4BuP3PT_UvQ49ltA7lmxCfzf2q1zKeXUS9arOQCmzehyC8DrAUeEE92XiqZgkpfjKQYAVE7WTmDMD5No_u2YWk69yaERv906gCLD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/697057" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697056">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در هزینه‌های دولت اسراف عظیمی وجود دارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
۳میلیون کارمند دولتی داریم که با کارمندان شرکتی تعداد آنها به ۴ میلیون نفر می‌رسد.
🔹
۸۰ درصد بودجه کشور برای حقوق و مزایا به این افراد تعلق می‌گیرد.
🔹
معادل کشور ما با ۳۰۰ هزار کارمند دولت خود را می‌گرداند و ما با ۳ میلیون کارمند این کار را میکنیم.
🔹
مابقی فقط حقوق می‌گیرند و پشت میزشان روزنامه می‌خوانند. در هزینه‌های دولت اصراف عظیمی وجود دارد.
🔹
همان پولی را که دولت باید خرج رفاه شما کند، از جیبتان برمیدارد و خرج بنزین می‌کند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/697056" target="_blank">📅 22:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697055">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87787c9aa2.mp4?token=UeAHZ73vrrq6TyTO7YZtjPPUapxHhhVE1zxOr34JBPbOkbNbfPN3PX-DUBiI5raRuFlV6eWyEYJi2rTCE__zsBn7ZBZJ62JlAsUkQ3w0ryA_M4oozF_HCYNu-IJTVqmT5zdYYalk0E_dfPrFa9SPKGAONbcJeufBJSnR5TO_YvOqQOKccLZrzQhahvaOt5CTNcLuV2AkiNgLkLkyVGu_YwpLxOar_JQR_Wr4kI1psH94exB4ngSTWZC_ZN4VrQSR3gYlkTW1dZwVIzWR2sZhARHCwU20xsbox1cISmSi4FUZEKGs8Y6CjN1BO5ehycxCUwimcwfZxww6kRvxu-PN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87787c9aa2.mp4?token=UeAHZ73vrrq6TyTO7YZtjPPUapxHhhVE1zxOr34JBPbOkbNbfPN3PX-DUBiI5raRuFlV6eWyEYJi2rTCE__zsBn7ZBZJ62JlAsUkQ3w0ryA_M4oozF_HCYNu-IJTVqmT5zdYYalk0E_dfPrFa9SPKGAONbcJeufBJSnR5TO_YvOqQOKccLZrzQhahvaOt5CTNcLuV2AkiNgLkLkyVGu_YwpLxOar_JQR_Wr4kI1psH94exB4ngSTWZC_ZN4VrQSR3gYlkTW1dZwVIzWR2sZhARHCwU20xsbox1cISmSi4FUZEKGs8Y6CjN1BO5ehycxCUwimcwfZxww6kRvxu-PN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت خیره‌کننده دختر ایرانی در باز و بسته کردن سلاح
در حاشیه آموزش‌های نظامی جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/697055" target="_blank">📅 22:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697054">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
هرکسی ایران را دوست دارد اول صحبت‌های وزیر خارجه آمریکا را بشنود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/697054" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697053">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bf58452a.mp4?token=P17mbBno9cRP2nZoUQ-Lw9kWrgs873TjGEk_GY2-86oy50yESgr9BCUFK2OKReP1vrUZv0YqiY-_HEWkjdwmGK5t6eTYn7d2OJ409-nkBiRN8miKiK-gVx8ju6FScfkFRJcLAxM2AMbXjSOtL8DhVvy5o5bwwYfwxRLNekoGXS4FC7PUdZfLqi0rrejmnQXRVIyQ-vEEAr16JTxJ2ybOMpgrQvE2zjGpSl13lnt0OfYXWivjFbMcnUXPq1Vmob0exPhqR7DtQW6ymr22MfVRiLKrWvdhhNBpxItaMek8379Tcywcv2rndaDoJBAZu8-YLDA5co6GqYlZ-DXsKNEiMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bf58452a.mp4?token=P17mbBno9cRP2nZoUQ-Lw9kWrgs873TjGEk_GY2-86oy50yESgr9BCUFK2OKReP1vrUZv0YqiY-_HEWkjdwmGK5t6eTYn7d2OJ409-nkBiRN8miKiK-gVx8ju6FScfkFRJcLAxM2AMbXjSOtL8DhVvy5o5bwwYfwxRLNekoGXS4FC7PUdZfLqi0rrejmnQXRVIyQ-vEEAr16JTxJ2ybOMpgrQvE2zjGpSl13lnt0OfYXWivjFbMcnUXPq1Vmob0exPhqR7DtQW6ymr22MfVRiLKrWvdhhNBpxItaMek8379Tcywcv2rndaDoJBAZu8-YLDA5co6GqYlZ-DXsKNEiMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکرهای نفت عراقی در داخل خاک سوریه هدف حمله قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/697053" target="_blank">📅 22:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ضرغامی: من اجازه ندادم میرحسین موسوی در سال ۸۸ در پخش زنده با مردم حرف بزند/ سعید جلیلی به این ماجرا ارتباطی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/697052" target="_blank">📅 22:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e67bbba26.mp4?token=rGlWTOyXEHdtSqPGhyjK6u1OMxVIaBwfaDCvdfPbtzmpFC_mz12sCxjhpzoBLmHVC_-sjA58Nql9I93D563rhkNxF__eN68KcG42moUOs7MHk97Y6rdnZaVrFA1OrhnM_hBkL8q4c0-KVz2gIro0BH1z2QYOLSvtfJ_4id5HeYM9IYg9ETcQCKFTN38O2RGTVVP3mURP4QqcbSH-pFmrwsYt6u-jCw0gWWPmkVcexKFGvjjYLdAYC6GcNE9-FqzOi8SbJRgQ5RtvdFeKBJHO5562nd60ktYwc7-Lg71n33SrGCl0BThhf13f_H8tmvd3zO_woa3QJHtYrCYJSUgYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e67bbba26.mp4?token=rGlWTOyXEHdtSqPGhyjK6u1OMxVIaBwfaDCvdfPbtzmpFC_mz12sCxjhpzoBLmHVC_-sjA58Nql9I93D563rhkNxF__eN68KcG42moUOs7MHk97Y6rdnZaVrFA1OrhnM_hBkL8q4c0-KVz2gIro0BH1z2QYOLSvtfJ_4id5HeYM9IYg9ETcQCKFTN38O2RGTVVP3mURP4QqcbSH-pFmrwsYt6u-jCw0gWWPmkVcexKFGvjjYLdAYC6GcNE9-FqzOi8SbJRgQ5RtvdFeKBJHO5562nd60ktYwc7-Lg71n33SrGCl0BThhf13f_H8tmvd3zO_woa3QJHtYrCYJSUgYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق با شما بود؛ آنها فقط با جمهوری اسلامی مخالف نیستند، آنها با ایران مخالفند...</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/697051" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f3c4bb53.mp4?token=PUtBpY98fSlBVlWfHGJR1XbDiNDuSx4ZCKozd2O1yT65r7JwjKZv1bu1I5nTauOvBdbpecLPFQo2To3vg8LlhBVGaaf1T3WAQ39hyHqdLXUPNMI9p3Qr9mOQdzo2Nn-ui1LNER39N9KhOt8n3mWuFpKxPFklGhHBH6fe5isE27N8hDPMyeTDiDfkeo3H3wCGxGEAnyfi6vENL7DZSfUk22gnf64Yl-fDBfw7qUVI8s8R9jSgJabtROXppGzKzqPRd43XSkvcccGbeDspX74PCpi39ffhCsJqlJ6_CAl4K5EsSoREsTVTAOVTqfUhKPbLiGcMScfTJXjv-faTpTse467sHTUmxvD8nemO8aw9643nVRG9qNoubmmQ1yEQ8PnWCJtC8YwcQemC49A6swfUQEvXKCyM8x-Pb7H23XbkqxadO6MoRL5PFtyjoA47J-vaGrkTp1NJl2A0qFd8xNO7SQIaBk7x7isUp6lR0S6vSYbV0nmKlVj9-EGzTquBmQ3wVltpqUG_ZnaAiiwowMdY57Ki1-jdbqv_o85JzefVL3TfdAZuQfia3Wcl8EY29MA17y4MwfVpFTofBaz3yX8raknfofTTZ8hs6ZHllWIAOuzaw24HzSCrWIIcfBSpKbBMesAKWSJ_6c5mpL_HRoo3TJF7XkyJGK2e1VaT0l-BYY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f3c4bb53.mp4?token=PUtBpY98fSlBVlWfHGJR1XbDiNDuSx4ZCKozd2O1yT65r7JwjKZv1bu1I5nTauOvBdbpecLPFQo2To3vg8LlhBVGaaf1T3WAQ39hyHqdLXUPNMI9p3Qr9mOQdzo2Nn-ui1LNER39N9KhOt8n3mWuFpKxPFklGhHBH6fe5isE27N8hDPMyeTDiDfkeo3H3wCGxGEAnyfi6vENL7DZSfUk22gnf64Yl-fDBfw7qUVI8s8R9jSgJabtROXppGzKzqPRd43XSkvcccGbeDspX74PCpi39ffhCsJqlJ6_CAl4K5EsSoREsTVTAOVTqfUhKPbLiGcMScfTJXjv-faTpTse467sHTUmxvD8nemO8aw9643nVRG9qNoubmmQ1yEQ8PnWCJtC8YwcQemC49A6swfUQEvXKCyM8x-Pb7H23XbkqxadO6MoRL5PFtyjoA47J-vaGrkTp1NJl2A0qFd8xNO7SQIaBk7x7isUp6lR0S6vSYbV0nmKlVj9-EGzTquBmQ3wVltpqUG_ZnaAiiwowMdY57Ki1-jdbqv_o85JzefVL3TfdAZuQfia3Wcl8EY29MA17y4MwfVpFTofBaz3yX8raknfofTTZ8hs6ZHllWIAOuzaw24HzSCrWIIcfBSpKbBMesAKWSJ_6c5mpL_HRoo3TJF7XkyJGK2e1VaT0l-BYY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتاب ۳۱۹ ساله نسخه دست‌نویس در دوران صفویه
🪔
📖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/697050" target="_blank">📅 22:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
انفجار مهمات به‌جامانده از جنگ تحمیلی در دالاهو سه عضو یک خانواده را مجروح کرد
جانشین فرمانده انتظامی سرپل‌ذهاب:
🔹
سه عضو یک خانواده شامل۲ فرد بزرگسال و یک کودک هشت‌ساله بر اثر انفجار مهمات به‌جامانده از جنگ تحمیلی در منطقه شیره‌چقا شهرستان دالاهو مجروح شدند.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/697049" target="_blank">📅 22:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شهادت مامور فراجا در حملۀ تروریستی در فاریاب
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش در پی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/697048" target="_blank">📅 22:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/697047" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4019f8179f.mp4?token=ESv8EMZUlO6vp42r62MSVwx0Ey5a8186ZnNFrIUpSCDjXwimpFT0rFj3rXERhzEdn4GIi1FnmzLD9WB-XOgY4zz7zdtOUIugzV_wOJfgJhr9cAqQG7WeUZw5PDsNDGiqT9O0wRn9ppt44PWhFbZajDoLwYzD9sOqANOHNs4TkPlwMwvBS8ui3Mkcl-RjaG6fsYCXC0XEDNbhhM1NhRczHN0ADKQXkKS-SmLkDNl1z_X8xV_p5gUbaad1Uv5yceXsB1DGLxG1vyElYFlunm9nTpP3-6rVoJt6giZlzeJPIAtUCoqQm65AtNTRyTXWQDD0LEnNcSBR7dAxk7pPb7YChw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4019f8179f.mp4?token=ESv8EMZUlO6vp42r62MSVwx0Ey5a8186ZnNFrIUpSCDjXwimpFT0rFj3rXERhzEdn4GIi1FnmzLD9WB-XOgY4zz7zdtOUIugzV_wOJfgJhr9cAqQG7WeUZw5PDsNDGiqT9O0wRn9ppt44PWhFbZajDoLwYzD9sOqANOHNs4TkPlwMwvBS8ui3Mkcl-RjaG6fsYCXC0XEDNbhhM1NhRczHN0ADKQXkKS-SmLkDNl1z_X8xV_p5gUbaad1Uv5yceXsB1DGLxG1vyElYFlunm9nTpP3-6rVoJt6giZlzeJPIAtUCoqQm65AtNTRyTXWQDD0LEnNcSBR7dAxk7pPb7YChw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوتن شکیبا: من اصلاً آدم ازدواج نیستم، بخاطر بازی نقش حبیب دچار شرم می‌شدم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/697046" target="_blank">📅 22:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بلومبرگ به نقل از مقامات غربی: ایران علیرغم ماه‌ها بمباران، موفق شد کارخانه‌های موشک‌سازی و پهپادسازی خود را حفظ کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/697045" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697044">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بر اساس گزارش منابع محلی، صداهایی که در یزد و شرق استان تهران شنیده شد، ناشی از رزمایش سامانه‌های پدافند هوایی بوده است./ صابرین‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/697044" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It__ciphFEcUJsDvX7_H6TV7Js05KaT7m7AcxO9d3CAxn2jK0zLRBtc7LDvIYf_jsd9yzerI6Q22e6-2ioxoUVI_718keu0pHsl28Mr-DGaDIXowYmAb9kkLX8TbU4zZ_YYCHENN25wA_Lv2CIRMsMs5XFt5U-NL5FKMvmsgQSIyWhCXrBUQMN3VkRX22BqqaKj46Da3KqOylxhIPrUTzqzzfBCwih0tPTKYMmRWKuo25MzPQfQrx_AU7foP2nKPieXgrsB2lt0zUMCZt7w4847sL7WFijKmclHX27vu3sz2iMxbwGCOAHYbrRJwZDtAt1zzAIuzxPpCDMR3aavvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/697043" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: دولت خودش از عوامل سقوط ارزش پول ملی است/ گرانی قیمت دلار به نفع دولت است
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
اولین کاری که باید صورت بگیرد تثبیت ارزش پول ملی است.
🔹
هیچ کدام از مردم از تثبیت پول ملی ناراضی نیستند، اما دولت وقتی دلار را گران‌تر می‌فروشد، پول بیشتری به دست می‌آورد و به کسری‌اش میزند.
🔹
دولت خودش یکی از عوامل سقوط ارزش پول ملی است چون در آن نفع وجود دارد. بانک مرکزی باید جلویش را بگیرد که آن هم ملاحظه دولت را میکند‌.
🔹
ریشه‌ی گران شدن بسیاری از کالاها و خدمات این است که ریال دارد ساقط می‌شود.
🔹
دولت باید سختی‌اش را بپذیرد و بگوید به جای اینکه از جیب مردم بردارم ۳۰۰ میلیارد دلار سرمایه خودم بردارم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/697042" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKrlUCanGB2Y4wMPW7O0gSiJETv-19fW-NhoZ1c1tRXxYcxps9ou3sG9NCBK6fBadTKOr8jY4hoEWIRZ2R3A7EJqD1umUkmz3rvycgPZHiAVV8LX1m4TPgQv5TUD-TOC-fJPtSQvy1UpjrBJvhKd3_m1UuYnJJUoFEgHR9STcBRsfLZs58XsLEbrOIppnVZGZXUYKcAuiI8HS_bxtdgRl2YVhhyH7wFytQxYU0UlojFAttQfX_jsQbDA_zbAvT_KCPdt8BRYD71AVZSG1vzADG1E1gxmABFAslMOih2K6ZMLDBULw9NaEsVrp_E466t9CjLvPSWfXNkftwrRRFUnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکاتی کلیدی درباره‌ی کم خونی
❣️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/697041" target="_blank">📅 22:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اسرائیل ترور کرد و آن را به ایران ربط داد
ارتش اسرائیل:
🔹
ما یک شهروند سوری را در مرز سوریه و لبنان ترور کردیم که به دنبال انجام عملیاتی با هدایت ایران بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/697040" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معاون وزیر خزانه‌داری آمریکا در امور بین‌الملل به الجزیره: ما اقداماتی را برای قطع جریان ارزهای دیجیتال به ایران انجام داده‌ایم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/697039" target="_blank">📅 22:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
معاون وزیر خزانه‌داری آمریکا در امور بین‌الملل به الجزیره: ما اقداماتی را برای قطع جریان ارزهای دیجیتال به ایران انجام داده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697038" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQEizh3BG-6MDteEkInQwGRkMyLQKxMqyGVH21jfMnByfOSTbdRnNu329k2pHcEGB5_FVVnaPm37hRBRLnVa29yNFw0ZXw_-90j2nspNuz9liaCsMCPO87PckezSxg-EGrG_HaNKoMxEcNIk01e1VNEKMuloxOl9p7xpjEffEuLgvgKBZBJrga8e_CcW_0NI010wERH42LjuF9eDyXggW7LMN86SKXQO990DrPazeZWjFx5__QoAVIl1JuK4X5DrTIK_mNqA_-mljSCtGz-93xBm-5C4fIsMFEf3Ns4ckrNYbeYkAPi9tl2Udb3q-XXdcYG8QD-yp1XhZRVsY3-V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBNoewqr5ZRsj628JLBT31O0MgSd1IOC8Ar_joDCSh4_8F1UGfIh5VqyJNI5H1Li6-CIidlJw-R9_8WbWMTAc5w3mp9h5ZHhzv1ntTd_S7h9zQqyIaRMhpw6aZ_k6ekTtIw3nNXaxkiGkM86aRuTDTiIYPLJ45UmOjJ3NznySl1HLmyNMlZU63kWD6JX4d9lreZ6f7_O8VpuOAnTGhU9qsRVRaovl-oO8h62vGthTCTwRhF9XXUIr8nPytQqgDTkrFFc_lJjkfhnmn6HAfOd-UQ2PTgyLl5jNpHWBK0FsjI8NoCJIC7AoSd7cTMtUi5YaStyPJMpgVS9a0cT2DwiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAuqiOIjWqQwCWBCajI750Oj2qNDk5TxmU-8OichSeyKpGtLiWei_TiWWb-9nRc_2yfjmq3HDhZG_XuikBEd3UsC8nbTYupzFPRjQoupJmXTZxLT1jRA9tfNnB-7sr9ZvZrs_pKuVBiCo8m7NfOP6n8MxdnzQE-YpAVd65_pTClwDDwcm6WqfqnEA9ZrQfZw1sqNwPrEVUJaIGtY1WWgp1vzu10GXTcj9IdoyPIEX21NWGcTEl-tvCxGcxq63KJo8izk76FvRG3MvgsRo5OMKtUgbScDQyvOMsKVvUg3TMEe1sLfIg_oaQHq5yV05oUidJilDsX6_4RvbadF7oNxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند روز پیش همزمان با ماه کامل بر فراز آرامگاه کوروش؛ شاهکاری تماشایی!
🌒
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/697035" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ساعتی پس از اعطای جایزه نوبل به قاضی دیوان کیفری بین المللی، آمریکا تحریم هایی را علیه این نهاد بین المللی اعمال کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/697034" target="_blank">📅 21:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
زلزله ۷.۵ ریشتری پاناما را لرزاند؛ آمریکا هشدار سونامی صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697033" target="_blank">📅 21:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e28f907f.mp4?token=nlaRWd6MqiicmkG6q_8KKP8LluzDQgd3zekozYCge6cDgAbSaBfH16ZTMyueU1U15NiWI1eYLlqztRDSYFxpla0mYDM17-eolIUXXqBLGdfmtSqKkBVTgvqH8n-TiATDuxPp9gzmgvzCP9fLz6kZI975vGQzBPnFfXoZUhngvtRNJEl7WXIwjHkSLynkooyTMbQl99F_6V027yxQ11gdiNvyET1hlRNbW4cnBDMJRJsVo1pHmLsMOoSGAbAaVimW5tTDtwyHIwX3wIdRaJwo9eb0e0rnmnVoalEEUtgiFMBG7IWbRvja-iiA8NFWkuLrSV7zwLrlCMGlML6tIbRw3lohofJEcDrrZzVQA3PG_5RFNi15IJqSnr1CiaGq7PTirdUPwqZdjAAx6H6pYMfglpR701GiVrI2mhXEq7vB__D6LZVjj_Rl3waainEElGx5XxGhN2m3vAK4TtqCgnblvMLT-3mXfSSF7LRqnNOqEB35bR6ao0VN62HWv9p1WkyJRW5K6w7jJ5JKL4sYrQccyvWMW-h6zBY8vRvXpTD1uzrKyhSOocrKxhPb2cKmJH4Z8Mq9NiRMuPlt9eV8ROy3NcmmmYnMToZe6KSwb-Qw8gAZEME9mZpCgaCi_IEkr0CQ1CD0lw7wBIqa7mkLvxYHaLrZ8-Xp9mAj_LXg_NM9tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e28f907f.mp4?token=nlaRWd6MqiicmkG6q_8KKP8LluzDQgd3zekozYCge6cDgAbSaBfH16ZTMyueU1U15NiWI1eYLlqztRDSYFxpla0mYDM17-eolIUXXqBLGdfmtSqKkBVTgvqH8n-TiATDuxPp9gzmgvzCP9fLz6kZI975vGQzBPnFfXoZUhngvtRNJEl7WXIwjHkSLynkooyTMbQl99F_6V027yxQ11gdiNvyET1hlRNbW4cnBDMJRJsVo1pHmLsMOoSGAbAaVimW5tTDtwyHIwX3wIdRaJwo9eb0e0rnmnVoalEEUtgiFMBG7IWbRvja-iiA8NFWkuLrSV7zwLrlCMGlML6tIbRw3lohofJEcDrrZzVQA3PG_5RFNi15IJqSnr1CiaGq7PTirdUPwqZdjAAx6H6pYMfglpR701GiVrI2mhXEq7vB__D6LZVjj_Rl3waainEElGx5XxGhN2m3vAK4TtqCgnblvMLT-3mXfSSF7LRqnNOqEB35bR6ao0VN62HWv9p1WkyJRW5K6w7jJ5JKL4sYrQccyvWMW-h6zBY8vRvXpTD1uzrKyhSOocrKxhPb2cKmJH4Z8Mq9NiRMuPlt9eV8ROy3NcmmmYnMToZe6KSwb-Qw8gAZEME9mZpCgaCi_IEkr0CQ1CD0lw7wBIqa7mkLvxYHaLrZ8-Xp9mAj_LXg_NM9tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد میرسلیم از افشاگری های احمدی‌نژاد؛ افشاگری وحشیانه جایگاهی ندارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
رویه‌ای که از نظر اسلامی قابل‌قبول نبود در دوران احمدی‌نژاد رواج یافت و آن تخریب بود.
🔹
این تخریب‌ها از دوران احمدی‌نژاد شکل گرفت و به ضرر کشور ما تمام شد.
🔹
رویه اتخاذ شده از سوی احمدی‌نژاد که «بگویم، بگویم »، معنی ندارد. برای ما مسلمانان افشاگری وحشیانه اصلا جایگاهی ندارد. افشاگری معنی ندارد و باعث ضایعاتی در جامعه می‌شود‌.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697031" target="_blank">📅 21:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3af0af2f.mp4?token=nKDwmcmlUBAQUxNrMyC60AWwYV1E25QGAmrFFkjYeucp8DYGQfvUEZvdZlwFNJfe0deGW3wplS3uo6_Vas7kaAXDCjajA8fHRHe2hWZn1hNmri5qu0NtixatNHhCX_ovluKMtiiSSw_rUnnIu0gbmJHOKFwy6vNWBpR9qoAdexqarYi7eqrTgQIcKX00x3da4B_tVveK3SEP4hEpcGEp2q69WHMMQWgopm5w19i3kiPcAjECWC9kQ8pmZBqXoEAKGErAjw97wpY8aNjPKKkVKC106dArRx3Om7RKGEY--cSVaEuWN-cBahK7aChVCOnbVAhm47ZyKFKzqEx-7ADttilIthjPyDcLQZcAkmGt0uWU9e5ZmT9WUQEXAbQaAVESyttKn33IbuZ6ntcL6cYv5BL3D1grgj4Aok50ECJgpvjnrpyImYc1LeQHFlY9c-lo9AZ7xY0-ikPejlaPYyUKLPEd37K4dSDXXwsJXcCAFhOWTWNXdCa8iI5Y7-o2h7Ndk3cPN12YMp0xxwAxRsYUVpcmRK4YSPhQ3VVNcYWqup8aleDObMZRRC64xEn5w77dbmC1X5R33cxOzWLLqFFuqEmWHkg4FQXBeUQurx-AQywtBXTXZvmD1W0vCACZrb6nu6e3GuyByu7bUV2X9dDOZ-5kOreLonRETPZEPk4hv2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3af0af2f.mp4?token=nKDwmcmlUBAQUxNrMyC60AWwYV1E25QGAmrFFkjYeucp8DYGQfvUEZvdZlwFNJfe0deGW3wplS3uo6_Vas7kaAXDCjajA8fHRHe2hWZn1hNmri5qu0NtixatNHhCX_ovluKMtiiSSw_rUnnIu0gbmJHOKFwy6vNWBpR9qoAdexqarYi7eqrTgQIcKX00x3da4B_tVveK3SEP4hEpcGEp2q69WHMMQWgopm5w19i3kiPcAjECWC9kQ8pmZBqXoEAKGErAjw97wpY8aNjPKKkVKC106dArRx3Om7RKGEY--cSVaEuWN-cBahK7aChVCOnbVAhm47ZyKFKzqEx-7ADttilIthjPyDcLQZcAkmGt0uWU9e5ZmT9WUQEXAbQaAVESyttKn33IbuZ6ntcL6cYv5BL3D1grgj4Aok50ECJgpvjnrpyImYc1LeQHFlY9c-lo9AZ7xY0-ikPejlaPYyUKLPEd37K4dSDXXwsJXcCAFhOWTWNXdCa8iI5Y7-o2h7Ndk3cPN12YMp0xxwAxRsYUVpcmRK4YSPhQ3VVNcYWqup8aleDObMZRRC64xEn5w77dbmC1X5R33cxOzWLLqFFuqEmWHkg4FQXBeUQurx-AQywtBXTXZvmD1W0vCACZrb6nu6e3GuyByu7bUV2X9dDOZ-5kOreLonRETPZEPk4hv2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیام دانش‌آموزان باکو علیه ممنوعیت حجاب دولت علیف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697030" target="_blank">📅 21:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای
سازمان تروریستی سنتکام: از زمان ازسرگیری محاصره علیه ایران، مسیر ۱۳۳ کشتی تجاری را تغییر داده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/697029" target="_blank">📅 21:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رئیس هیات عامل سازمان گسترش و نوسازی صنایع ایران: سهمیه سوخت خودروهای فرسوده بالای ۲۰ سال قطع نشده است/ فرصت ۵ ساله برای جایگزینی داده شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697028" target="_blank">📅 21:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e21e8d23c.mp4?token=SfUuzqvXFNDGvItlPkBEkOhvy56Su-Lb4AWjJ_YOqAjmM7ngJ2DEzVOkSItKRXBRcgfFOsN28Vk5h4Y02WfTh-qAA4uomVV3J0p-yN4jdnfeKY9NuS3F3XFoXwffTB4b4SR8sWsD-Qi9lidzAt5e413wo8PtNJ9aUBZx_oVuSWLZeBT_KuOdvhAwQTg-AUp07oSWS_l4teSWrbEKb-Cvfa2dQ2QmRPKLFR4Dk4PundlqaebzEm9vUtK19OpNg7YMyfOmQUOdJ3zTSjFZlLRjvAAq-oM8gWmfHCs5F5fwd0-UdMmtd2xaZ2jOrO7_sEvSBqknVKyq8AyNFF2YNLsAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e21e8d23c.mp4?token=SfUuzqvXFNDGvItlPkBEkOhvy56Su-Lb4AWjJ_YOqAjmM7ngJ2DEzVOkSItKRXBRcgfFOsN28Vk5h4Y02WfTh-qAA4uomVV3J0p-yN4jdnfeKY9NuS3F3XFoXwffTB4b4SR8sWsD-Qi9lidzAt5e413wo8PtNJ9aUBZx_oVuSWLZeBT_KuOdvhAwQTg-AUp07oSWS_l4teSWrbEKb-Cvfa2dQ2QmRPKLFR4Dk4PundlqaebzEm9vUtK19OpNg7YMyfOmQUOdJ3zTSjFZlLRjvAAq-oM8gWmfHCs5F5fwd0-UdMmtd2xaZ2jOrO7_sEvSBqknVKyq8AyNFF2YNLsAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات عراقچی در خصوص نشست سه جانبه ایران، روسیه و آذربایجان
وزیر امور خارجه:
🔹
به ابتکار روسیه این نشست شکل گرفت و بعضی از پروژه‌های مشترک ۳ کشور مورد بحث و توافق قرار گرفت.
🔹
پروژه‌هایی وجود دارد که همکاری اقتصادی ۳ کشور را دربرمی‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/697027" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697026">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5200dd53.mp4?token=hnsxzTT9e-q8rd_gsj01U60BAIVtNXa9dqVzr5vsy8XDuwvZH45BoNc_c6CTA8-dVOE7H1ONUEvbMqSgElufL2279LcAteyDaHebuEgsoeLQCDS54jJRBlhSXTDBIGOibnz0BvyBEZTh4vHKjrxFLSryLzdUxIyWXK2Khk9fjJklYkExuA0r7nnlvVinX7g6YoCXcuexZ6PwdWvhH43SMAFQSQalhOZIiJjudMXbeR6gInFwHXDPqEfUjnBKxy_fbK_5dP6HU8PWpTf9ve4uWeUrM1_1w2Q0pPWTAFxosRC3-MJLW7jf-p8qhap3zs9XErgglKYGn-XRmpx-SHkwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5200dd53.mp4?token=hnsxzTT9e-q8rd_gsj01U60BAIVtNXa9dqVzr5vsy8XDuwvZH45BoNc_c6CTA8-dVOE7H1ONUEvbMqSgElufL2279LcAteyDaHebuEgsoeLQCDS54jJRBlhSXTDBIGOibnz0BvyBEZTh4vHKjrxFLSryLzdUxIyWXK2Khk9fjJklYkExuA0r7nnlvVinX7g6YoCXcuexZ6PwdWvhH43SMAFQSQalhOZIiJjudMXbeR6gInFwHXDPqEfUjnBKxy_fbK_5dP6HU8PWpTf9ve4uWeUrM1_1w2Q0pPWTAFxosRC3-MJLW7jf-p8qhap3zs9XErgglKYGn-XRmpx-SHkwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ ترفند ساده برای تشخیص تازگی مواد غذایی که هر کسی باید بدونه
🍯
🐟
🥚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697026" target="_blank">📅 21:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bcc79797.mp4?token=PTgVFQiSRLTDgM7sYbO6cr46xhTAOsMw4MUZeO4WkfEzj2vIYznTX54XH24D8R5mv33XrNNdoAA3snmLt9fdYL8LXgZ8cl_iV1biVjZtgu7hjM1aGQ-3X-Y9wPek-ZBMexsHTAl8xuGjOMpbH4nRFHn30s28eOAD3KCzzgijn1sN1rxjmmEFX8W_lrED1MF9l1P7xdBM1im2OM_igPst6Z_ebUEo5rcWVlvQHQAs7WOhhOXKYC-z-eblaSr2BMI5zIKeGxM3ixmzoGm_Ek2PmBiqmtcUP2ofArQTzuYhW8HtExJLCjl1-_Gecmk8FrFT8v7QfFC66Bp7y0L2AHqPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bcc79797.mp4?token=PTgVFQiSRLTDgM7sYbO6cr46xhTAOsMw4MUZeO4WkfEzj2vIYznTX54XH24D8R5mv33XrNNdoAA3snmLt9fdYL8LXgZ8cl_iV1biVjZtgu7hjM1aGQ-3X-Y9wPek-ZBMexsHTAl8xuGjOMpbH4nRFHn30s28eOAD3KCzzgijn1sN1rxjmmEFX8W_lrED1MF9l1P7xdBM1im2OM_igPst6Z_ebUEo5rcWVlvQHQAs7WOhhOXKYC-z-eblaSr2BMI5zIKeGxM3ixmzoGm_Ek2PmBiqmtcUP2ofArQTzuYhW8HtExJLCjl1-_Gecmk8FrFT8v7QfFC66Bp7y0L2AHqPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پربازدید از اعتراضات دانش آموزی در فرانسه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/697024" target="_blank">📅 21:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرده
🔹
اسپیس‌ایکس با خرید فرکانس‌های ۸۰۰ مگاهرتزی و مجوز پرتاب هزاران ماهواره، به‌دنبال ارائه اینترنت ماهواره‌ای مستقیم به گوشی‌های معمولی است؛ فناوری‌ای که می‌تواند پوشش موبایل را گسترش دهد و وابستگی به دکل‌های زمینی را کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697023" target="_blank">📅 21:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
احسان دهمرده، از پرسنل معاونت فرهنگی اجتماعی فرماندهی انتظامی سیستان و بلوچستان در حمله تروریستی به شهادت رسید  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/697022" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b979e766ff.mp4?token=SohuyuZ7CBrG_ApHhwSSZ6lMQNQuj6SsBBmFCrK4xDBkQuIys4RmEiHjmKeRRxfpEQ_PKUk8es_lx-VLG3iHz4YFGJWbwDUxuH_N4t5pW7_i0KHXCtS8qYEbTD8GI4H2oFD7NyQCjVOW5wPDj40vgqgZkwJQE6m-7aMloT1AjNvJXMKuEku6WUlE5aKN6DuUl-un6wmjD14d34UE2KbB9YkvAmqFMSbXSj3ryK4D501HcEPt8-katyPOWIdhrRMpe6wlX9dYPZAswB4K4BBTxq_y52DABj3xrk2VUn1gR-5WPifH3_DmSGNtydp9yMr_oRIcLO-Nxo1ttGPEsuPphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b979e766ff.mp4?token=SohuyuZ7CBrG_ApHhwSSZ6lMQNQuj6SsBBmFCrK4xDBkQuIys4RmEiHjmKeRRxfpEQ_PKUk8es_lx-VLG3iHz4YFGJWbwDUxuH_N4t5pW7_i0KHXCtS8qYEbTD8GI4H2oFD7NyQCjVOW5wPDj40vgqgZkwJQE6m-7aMloT1AjNvJXMKuEku6WUlE5aKN6DuUl-un6wmjD14d34UE2KbB9YkvAmqFMSbXSj3ryK4D501HcEPt8-katyPOWIdhrRMpe6wlX9dYPZAswB4K4BBTxq_y52DABj3xrk2VUn1gR-5WPifH3_DmSGNtydp9yMr_oRIcLO-Nxo1ttGPEsuPphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یائیر گولان، رهبر حزب دموکرات (اپوزیسیون اسرائیل): ترور علی خامنه‌ای بی‌شک اشتباه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/697021" target="_blank">📅 21:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697019">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: انحرافات اقتصادی کشور از دوران هاشمی رفسنجانی آغاز شد/ این انحرافات از همان زمان ادامه پیدا کرد و گریبان کشور را گرفت
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
رفسنجانی به عنوان رییس‌جمهور تصمیم گرفت سازندگی را اولویت قرار بدهد و مقدار زیادی نقدینگی برای این موضوع صرف شد، اما معادل آن محصول و نیروی انسانی وجود نداشت. لذا در دوران ایشان به تورم ۴۹ درصد رسیدیم که خیلی زیاد بود.
🔹
دلالان زیادی در این میان ثروتمند شدند. اینجا انحرافات اقتصادی درست شد که گریبان ما را گرفت و ادامه یافت‌.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697019" target="_blank">📅 21:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697018">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jamgVLFq90HK8-rKPkE4VO1cW-iug4yYoaT5PNyPHvxwpWivT2qAhecqPA_a5iI0uB1eY4H7Ctslo24T7GyQ7l8tIvi7VUtYdaUhKEC-4O8UQJfnMAuHaJX-Gdhq94REN5Wyx8gBcBk8feGPBkApJJrjOB1iMTgzMJax2NpMylT05PJWf6hZr1wIuOJ6OIPg8mEPre4585-Ter4iDnUzcCe1qairfK5qsoQC5FVY7cV4jnmi83sRIO8xkyaaxfuctevdW7BSemhC2RZyhte0zxt7Lk1jJ1E8x9U2Y_tCU-oQoA_lKDULCxbUEOhiV7jrbs2I7i2tfJYb_XBi8P97BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باز هم دست ترامپ از جایزه صلح کوتاه ماند؛ ناوی پیلای، قاضی‌ای از جنوب آفریقا برنده جایزه صلح نوبل ۲۰۲۶ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/697018" target="_blank">📅 21:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697017">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e34bb4a.mp4?token=uKQVvz4D89RTVcMIkG2fuFwXR-hVYoCR1CLgXmYhgrYskBTeFnqqqmUFZKN9KcUykPfaFHGA4qBGIq-4g-UN_Kke1GD41dOyJ7TJd2SSyjtdMIQl9eL79Z3Pgo0hDdBTsOq2u3gj93iifrGRS5OMRw4WVbWtgP_Gae1RwqPjrSxNDxXySMJynyAIfLnX47zEM-3iFJX8n0RG_aeQ7DCKP8vL4Jo8oCrKCWdLXZtq-p8EKi5VWNCJB2J9aSw02ZlfDVYWLCPhZtxEeaJfMvAPcVpCVL0iWJ72w-BvYRaTqT-01putYHPEIi6lOUEfHCy_hBMJHaheZjzRBKr8RQ2vtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e34bb4a.mp4?token=uKQVvz4D89RTVcMIkG2fuFwXR-hVYoCR1CLgXmYhgrYskBTeFnqqqmUFZKN9KcUykPfaFHGA4qBGIq-4g-UN_Kke1GD41dOyJ7TJd2SSyjtdMIQl9eL79Z3Pgo0hDdBTsOq2u3gj93iifrGRS5OMRw4WVbWtgP_Gae1RwqPjrSxNDxXySMJynyAIfLnX47zEM-3iFJX8n0RG_aeQ7DCKP8vL4Jo8oCrKCWdLXZtq-p8EKi5VWNCJB2J9aSw02ZlfDVYWLCPhZtxEeaJfMvAPcVpCVL0iWJ72w-BvYRaTqT-01putYHPEIi6lOUEfHCy_hBMJHaheZjzRBKr8RQ2vtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگو جدا افتاده از گله/ دریاچه مهارلوی ایران
🦩
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697017" target="_blank">📅 21:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697016">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d6c9260b.mp4?token=lNLeh4PNI9sse8MI3_TzL6DLCHBSAmIUUOJ2JkBRz9YTZbnNUxAp8jbG2L_kLUziFTpsugh-zrpPWlG-P4OOZKBR2M0j0mAjcjHZswfXhzP-Ni4cO4tEno8M5PsuiTMUbE7tg5ZOUbNGnHXpjTlWCUh8RhJV34CjCpiQ0ZL50v9mFf8aCzD02OqxpezPZvUDHHjg2xpj3KHEIYkuJeIHwU0gsZ_8qL2LoKyDyUHowO3CkvWdcEPXPIn3hDTnO3wgtRYAB40plbler8swq5Cv3HnPn8T9oltsP71Ol8RtCTzkdcS15mUpWACDRjjDmFKwr8RjHf5pqP7T0GOiMwounQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d6c9260b.mp4?token=lNLeh4PNI9sse8MI3_TzL6DLCHBSAmIUUOJ2JkBRz9YTZbnNUxAp8jbG2L_kLUziFTpsugh-zrpPWlG-P4OOZKBR2M0j0mAjcjHZswfXhzP-Ni4cO4tEno8M5PsuiTMUbE7tg5ZOUbNGnHXpjTlWCUh8RhJV34CjCpiQ0ZL50v9mFf8aCzD02OqxpezPZvUDHHjg2xpj3KHEIYkuJeIHwU0gsZ_8qL2LoKyDyUHowO3CkvWdcEPXPIn3hDTnO3wgtRYAB40plbler8swq5Cv3HnPn8T9oltsP71Ol8RtCTzkdcS15mUpWACDRjjDmFKwr8RjHf5pqP7T0GOiMwounQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب‌های پایانی سیاوش/آخرین تمدید
📣
دعوت بازیگران کنسرت نمایش سیاوش برای شب‌های پایانی
بلیت اجراهای پایانی کنسرت‌نمایش «سیاوش» برای روزهای ۲۲،۲۳،۲۴ مهرماه (چهارشنبه، پنجشنبه، جمعه) از فردا(شنبه) ۱۸ مهرماه ساعت ۱۴ در سایت‌ ایران‌تیک آغاز  می‌شود.
https://www.irantic.com/theater/52434</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697016" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22ac382f6.mp4?token=dBLhsFKfG8YSve59CixueVcwisC79oKfLpbZumMfONhySDfRQRUl-kOt4iH_tKmV8L3me6_5gQlwUNJ3MgA2UH117J0WO6mpVR5YyXgeWHLA2LTN33_X9x7XuWdQt9Oyu8lBxEFgWCETf5gD6dH4rJLadrY4PlLqmPmGK9wW2LyX7SbOFe639FM6yrn9kfdyRcqjQ_ihlQLkPVQy3qsFzQp0dx8FVp_Pd3hk2uG75flPxmgYKC3vRrgY4DY8N0j9wir4QADerNHVXltwLh9Be6GZd1XGyTfe57tqPeFqipIMY--zwWtT94T3ZrHL9oE5DUCeizzPWhm9u_m1Urna5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22ac382f6.mp4?token=dBLhsFKfG8YSve59CixueVcwisC79oKfLpbZumMfONhySDfRQRUl-kOt4iH_tKmV8L3me6_5gQlwUNJ3MgA2UH117J0WO6mpVR5YyXgeWHLA2LTN33_X9x7XuWdQt9Oyu8lBxEFgWCETf5gD6dH4rJLadrY4PlLqmPmGK9wW2LyX7SbOFe639FM6yrn9kfdyRcqjQ_ihlQLkPVQy3qsFzQp0dx8FVp_Pd3hk2uG75flPxmgYKC3vRrgY4DY8N0j9wir4QADerNHVXltwLh9Be6GZd1XGyTfe57tqPeFqipIMY--zwWtT94T3ZrHL9oE5DUCeizzPWhm9u_m1Urna5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان بازی| ارونوف برای تارتار گل کاشت/ سرخپوشان به یک‌قدمی صدر رسیدند   پرسپولیس ۳ -- ۱ صنعت نفت
🔹
گل‌ها: تیوی بیفوما(۴)، علی علیپور(۵۳)، اوستون ارونوف(۸۵) برای پرسپولیس / محمدحسین باصری(۶۵) برای صنعت نفت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697014" target="_blank">📅 20:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f98bbb43.mp4?token=uvfn1ereDfnYDQ4-SQzHEaXaJkD1GjYQymuV21l6Dto4HxZAsYtwuP39FepskNfiNK6cDXwZRAzW2kV6IvscbV3BFjHFVFEFA-zx-grcsjrJ0Noijut2Jo2cPwFYsKbHmj_3l_L452Wn7fBN065UlIDadLrR41YIPHVir4jXlWrUtYT9lB_XVdQzmoLrlWPBKcVhIy7Beg_DnQwbiE69ezn6RF3N-uR4MK-JVQKi118Sf_pLKfnxZzovyW29K-5COUGST16lZ-eVZHdN7lqcJ946O9229X6CfHJsTYY50g5shRawjw55cVtFj2c6UI6mWuQ8Xvo6rjrnCCOW_1-Jjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f98bbb43.mp4?token=uvfn1ereDfnYDQ4-SQzHEaXaJkD1GjYQymuV21l6Dto4HxZAsYtwuP39FepskNfiNK6cDXwZRAzW2kV6IvscbV3BFjHFVFEFA-zx-grcsjrJ0Noijut2Jo2cPwFYsKbHmj_3l_L452Wn7fBN065UlIDadLrR41YIPHVir4jXlWrUtYT9lB_XVdQzmoLrlWPBKcVhIy7Beg_DnQwbiE69ezn6RF3N-uR4MK-JVQKi118Sf_pLKfnxZzovyW29K-5COUGST16lZ-eVZHdN7lqcJ946O9229X6CfHJsTYY50g5shRawjw55cVtFj2c6UI6mWuQ8Xvo6rjrnCCOW_1-Jjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده جنبش حماس در ایران: ایران به حماس کمک می‌کند؛ ولی خرج حماس را نمی‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697013" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62dd728d6.mp4?token=o9Jli9jbqtoAC7SJWzOXO5JgPHr3KCMGci_UcxHbp2yFf0brAz_Trfp6yjgRs9MPzkejbZ6XOhOh3D7qkFnqytDvTHwE98nqivaeNinULoDnoKdgPALGujeko8cRw7HnhCz129gviVIKIbTWK_A6uCbSF4EieRNdW0RhcYZrem4pMti6hAS-OH8RgEU86U0XdnskTiIjIKlVkA54DOqDCnp2XJGyVAJxGEMwy3F6fe2ek5U7IGm2NLopUJjcF315YWOSTiHP6ntKbwwkMEUi_g3f7AD3sOifyuL-DFtDYwvgRHmIw42ynMHD3QNb2u00Lm1T3vz0gbpu5DOdOt-y8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62dd728d6.mp4?token=o9Jli9jbqtoAC7SJWzOXO5JgPHr3KCMGci_UcxHbp2yFf0brAz_Trfp6yjgRs9MPzkejbZ6XOhOh3D7qkFnqytDvTHwE98nqivaeNinULoDnoKdgPALGujeko8cRw7HnhCz129gviVIKIbTWK_A6uCbSF4EieRNdW0RhcYZrem4pMti6hAS-OH8RgEU86U0XdnskTiIjIKlVkA54DOqDCnp2XJGyVAJxGEMwy3F6fe2ek5U7IGm2NLopUJjcF315YWOSTiHP6ntKbwwkMEUi_g3f7AD3sOifyuL-DFtDYwvgRHmIw42ynMHD3QNb2u00Lm1T3vz0gbpu5DOdOt-y8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتهام‌زنی دوباره نماینده آمریکا علیه ایران در شورای امنیت: انصارالله ابزار تهران هستند؛ ایران باید حمایت از آن‌ها را متوقف کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/697012" target="_blank">📅 20:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تصاویر منتشر نشده از شلیک شاهد ۱۳۶ و ۲۳۸ به سمت مواضع دشمن آمریکایی در عملیات نصر ۱ و ۲ و عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/697011" target="_blank">📅 20:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: دولت ۱۰۰ تا ۱۲۰ میلیارد دلار به صندوق توسعه ملی بدهکار است اما پس نمی‌دهد/ روزی ۲.۵ میلیون بشکه نفت را مفت می‌دهند و مردم هم می‌سوزانند!
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در مجمع در زمان آقای رفسنجانی صندوق توسعه ملی درست کردیم که سرمایه نفت (از آنچه به ارزش ذاتی نفت برمیگردد) در آنجا قرار بگیرد تا افراد نیازمند سرمایه از آنجا وام بگیرند و از محل تولید و سودش آن را پس بدهند.
🔹
آقای هاشمی گفت اینها نمی‌توانند صددرصد آن را در صندوق بگذارند، اجازه بدهید ۸۰ درصد را دولت استفاده کند و ۲۰ درصد را در صندوق بگذارند.
🔹
در حال حاضر در صندوق چیزی ندارند. یک رقم فقط این است که دولت ۱۰۰ تا ۱۲۰ میلیارد دلار بدهکار است.
🔹
دولت سرمایه‌اش زیاد است و اگر بخواهد میتواند پس بدهد، اما در تعارض با منافع مدیرانشان است و این کار را نمی‌کند و فقط ۲ و نیم درصد آن محقق شده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/697010" target="_blank">📅 20:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ae359f54.mp4?token=nOTmfzjFOM-nDgDFPdKxBxSd5XwHwgnoM07fJOXGPpCBXjknuTuliQ-ALrmJjqQ9opiA4jBHMDSu-7z7uALOiQ2_yYj2q-druIadfCwn1JBHitQO6bZQzDZrtik1qfXwMM0qKiVMIID3btNnKSbH3tZtp8fMeLlcR0eiW8GH7FqeFju6kEbDZOZR3hJbdZnSaQvKFUjp-HQ4aCIbOh1pDZN6Rf61HUzVyKiC1CcY8vAzSjgQlmN6xDGkjRD3oiV8NiZECuXkKu1hscrEVkqB1wHefJ2hDr5XNOmVCrjYnFUBErjQLe8KNb1_-ZhPFTkfqY-FUd-OixkSThqucMnnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ae359f54.mp4?token=nOTmfzjFOM-nDgDFPdKxBxSd5XwHwgnoM07fJOXGPpCBXjknuTuliQ-ALrmJjqQ9opiA4jBHMDSu-7z7uALOiQ2_yYj2q-druIadfCwn1JBHitQO6bZQzDZrtik1qfXwMM0qKiVMIID3btNnKSbH3tZtp8fMeLlcR0eiW8GH7FqeFju6kEbDZOZR3hJbdZnSaQvKFUjp-HQ4aCIbOh1pDZN6Rf61HUzVyKiC1CcY8vAzSjgQlmN6xDGkjRD3oiV8NiZECuXkKu1hscrEVkqB1wHefJ2hDr5XNOmVCrjYnFUBErjQLe8KNb1_-ZhPFTkfqY-FUd-OixkSThqucMnnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «نور» تبدیل به ریموت کنترل مغز می‌شود!
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/697009" target="_blank">📅 20:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عقده‌گشایی زلنسکی درباره ایران و روسیه
رئیس جمهور اوکراین:
🔹
اقتصاد پوتین را تعطیل کنید. دهان روسیه را ببندید. با فروش‌هایتان به روسیه خوراک ندهید.
🔹
به ما دسترسی به استارلینک بدهید. وقتی به ایران حمله کردید اسرائیل کاملاً حریم هوایی ایران را کنترل کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/697008" target="_blank">📅 20:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYdPeZi9xafw7_VZpmEB0gCZ3I9uB4TxKvOD7d7I60aTRgseQ9Er97l_hVJLQV1IAZWikH0qSF3_wImrDX9_K063YsxkVIECVu86C1FiWDKSdsMba4R8cBVHg9tswXOHhZ2dIjg2gjR210I5Nn6iLKwvJ_8B0EzCRj7l8n4pqHaDmiVb6WRsSJMKXuM7ORve3ISPke8ocZTE6koy83pOscDG3-wWCWA9_EQOYi780CGryQP7G9-8DCCJ_juaWsuVTNqzUwNxAAiKq2TNahLdC916IYXzQMuuEcRGd8v4QTgKtzmneUcM_zwll05z6WX-bSGeTE9e2UrZKqPk3kCsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شواری‌عالی امنیت ملی به آمریکا: برای تکرار شکست‌های تاریخی از ایران آماده باشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/697007" target="_blank">📅 20:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be0df3c01.mp4?token=BQMpBi6_N72-S6AGIZHwi_dPhM4Dy27GjtY2aM2sfjKbbr2lv1dNWTVLK6svDaEB-ye1kmo5GG-W_OOdU-6vp43gijBkQOWFiyRgAiyYlnReqKImaQHzkosNMSeUsFSr7t5t3fBjC8jnQQ3ON2WuiWcQ_npJHT-qFek1wvcw42x9_DyqwaSYEu_pUsf14rVTvfGqUu9WJv5Pal0bY5QHDLfT3CYBbAEm9Yjxnb9sPGNtdoOAMZ6Cl4aAvua3BvymKxtuzxVa6uB19gh2FxWzXEvmUpVj8nHyQ0xI0ASge1-K8OkWyryK2_MAHZ3uaKh69b5ILJzBIwJg-znnlvYU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be0df3c01.mp4?token=BQMpBi6_N72-S6AGIZHwi_dPhM4Dy27GjtY2aM2sfjKbbr2lv1dNWTVLK6svDaEB-ye1kmo5GG-W_OOdU-6vp43gijBkQOWFiyRgAiyYlnReqKImaQHzkosNMSeUsFSr7t5t3fBjC8jnQQ3ON2WuiWcQ_npJHT-qFek1wvcw42x9_DyqwaSYEu_pUsf14rVTvfGqUu9WJv5Pal0bY5QHDLfT3CYBbAEm9Yjxnb9sPGNtdoOAMZ6Cl4aAvua3BvymKxtuzxVa6uB19gh2FxWzXEvmUpVj8nHyQ0xI0ASge1-K8OkWyryK2_MAHZ3uaKh69b5ILJzBIwJg-znnlvYU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وعده وعید های مبهم و تکراری ترامپ درباره ایران: به‌زودی همه‌چیز تمام می‌شود و قیمت‌ها به‌شدت کاهش می‌یابد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/697006" target="_blank">📅 20:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjE58kf1lBrJdSDRhnRFj5_iWL6nUl_V7kf5Y12OENY4cE_EZsfdoeHQkQS7eeOCEScPO-8W0Po9B3wBRRdpEV2kSw_p04Kc1-94P4fhn367SQyS_vt6ZpkpAWMhb4O0R-3FVdzhMT7tb7XM3b8Nj7k8pIRslks4lRnLWmoCHh8iwKfF2PZSMNrNAWEgVdW3oSjk9lrjPJKL6U-tX8iakmDc0999MUj164LVh2CYYQFvPndC-FYads9Q7C5PrxuPXbxKesHh01W9hpJARn5JuAB2leYbjhb9IDFc_PvQCeSYyjcERXAtsP2E9D0YUeFY_nv6Dl7IVDexsbXHUpxwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWbKGTueOpS8O7prHBrQKOaM3j8vVSRgLQQ835WJ5LI7QpJ75fE97VizpC_tzFQkY6JsQWKDDPVt_IagzKcxBSZ2CY7zHl9Bf8Gng99P8Hb0fHCX4dOIfSjLMEc9TPOydmtRwDynXUGMbYGEe3Ye4OAaNBsdPqt0m3FosDDzlT2eYEPzh0hmJvY6hW8Pflf164kvutRY_ESAvMlem2BT_i7LPzUDkvYm5pCit8WXIN3EaHUx6zhpZLHUQRNNYzwlsY2wqTvClJH7kdXafU1A9IF9K7NPpzWtCjodfpLGN1g29Sk-uvKpgr4fxm_Ok-cOjSf4e2LtGKiEYSdMhT1jBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZsvG_vjIofTpGfb4VExw4EK1dTADNXuSVeKD5ncYnIHpkEGZE6xL1KiiRK-4vSr4n-uR6AisncZU0LwXzfFr6ZXtDpGuqBRcLLc9mknM_-92DSd_njsvrW8m1CMfUzFzH1S_mDcfghbcIOnlLsJ68kcVjCBMRrMjbzRDCJ2zXdkdeB4mObtEWvxzYCgTCFpHIfUd7ysmB44ACmO1TsgjV-rzJPH9_Eefy58GI_sZPU2SZE83T3xumjxzEJ6FbyADHHYw4aNmfMIe1RxHnUlClf1eMGHWy-mpRnMppxmI92kj1-tkvzPl_OOMkYJciamUo_UsNameLKdy6jZdXBzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGJ1NxD1YdFpNvquGG0cTFyfl1m1KMWWow4PSrLVdXqQ5-GLq-jnZXmaNXCqP5b2jtkJKTZuIQANxxiSMpis0XTP8loatMrpIX4Tgqk0MRTchh9urQAdod0nytwpk6Gi2GPXQB9sl5nXV_4oubDq5iooFndQMeucOYoQ7zrHBuxunzMMgfGzOUPPE6KQ8VXqGPNVJPy5zH01kQ-Wa-7dc6n1WpOwhk08HYyckPJz5tyIBRAoHA8PgRRhEyRXlpszlVZ7wLWsAOuix2m8DsGnSQNqrxqDkZwHsbEYbajm2NQC_UJ8v5PcEozNlcH0kU5vyie15klF2iTIWWAJkfhv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nH2T48EWNN6uk82JGpXsKtRfQ5iOUUn8H3UCFRot4Rbq9_b6Rfm2Fmo4SgVNOHaNV7V2ZjyMu0AueAZFnqTsiO3_hKLzCWps-XC0Q_JdyCVBw-N6MqKT_HPvIZ3jPOm2HVZUQkJezra2kPsrtd3LRxIbhOBj5-22yDm4HoGeQVTGbcioVTW6cPtC7u3kzP1VMggCQJ8k6wznG811Uf_Im55M-9ZBbOdksdQBQel7qxH3DSZmKn83kHHUulSHiWPP9fKy4QdpHIPoNwfyYyV80vCRiZIzSSnTa8g76SeNEZHcERdi7QT00HMu4n4KW75hjc8LL9jTAwFujk9NbBzxZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس‌های ناسا از ماه در ماموریت آرتمیس ۲ که برای اولین بار منتشر شدن
🌒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697001" target="_blank">📅 20:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دست‌وپا زدن تبلیغاتی ترامپ برای لاپوشانی شکست های دولتش: آمریکا اکنون بهترین کشور جهان است/ در دولت قبلی حتی یک سال دیگر هم دوام نمی‌آوردیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697000" target="_blank">📅 20:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: با ثابت نگه داشتن قیمت بنزین، عملاً آن را مفت‌تر کرده‌ایم/بنزین ۱۵۰۰ تومانی سال ۹۸ امروز معادل ۱۵ هزار تومان ارزش دارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
قیمت بنزین از زمانی که آقای روحانی گفتند من صبح بلند شدم و خودم هم خبر نداشتم، تغییر نکرد.
🔹
درحال حاضر که قیمت بنزین را از ۵ هزار تومان به ۱۰ هزارتومان افزایش داده اند، چیزی نمیشود.
🔹
مردم خودشان سرمایه های نفت را سوزاندند.
🔹
در زمان احمدی نژاد درآمد نفتی ما ۷۰۰ میلیارد دلار بود.
🔹
سرمایه نفت را تبدیل کردند که مفت تر به مردم بدهند؛ خوردند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/696999" target="_blank">📅 20:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شفادارو؛ آزمون پایبندی به قانون یا میدان جولان سلایق غیر کارشناسی!
🔹
اظهارات اخیر رضا سپهوند، نماینده خرم‌آباد و چگنی، درباره ضرورت توقف واگذاری هلدینگ شفا دارو، در برابر دیدگاه نمایندگانی قرار می‌گیرد که خروج بانک‌ها از بنگاه‌داری را ضرورتی برای اصلاح نظام بانکی می‌دانند. در همین چارچوب، مهدی طغیانی، نایب‌رئیس کمیسیون اقتصادی مجلس، از عرضه شفا دارو استقبال کرده و اقدام بانک ملی را گامی در مسیر اصلاح ساختار دانسته است.
🔹
نکته قابل تأمل آن است که خروج بانک‌ها از بنگاه‌داری، خود بخشی از تکالیف قانونی مورد تأکید مجلس است. بنابراین، نمی‌توان از یک‌سو بر اصلاح ساختار نظام بانکی تأکید کرد و از سوی دیگر، بدون ارائه مستندات روشن از تخلف یا تضییع حقوق عمومی، خواستار توقف یکی از مصادیق اجرای این سیاست شد.
🔹
واگذاری شفا دارو قرار است از مسیر بورس انجام شود؛ مسیری که امکان نظارت و شفافیت را فراهم می‌کند. در این فرایند، قیمت‌گذاری منصفانه، رعایت تشریفات قانونی و احراز اهلیت خریدار باید خط قرمز باشد.
🔹
اگر درباره قیمت، صلاحیت خریدار یا آینده تولید دارو ابهامی وجود دارد، باید همان ابهام را مستند و شفاف بررسی کرد؛ اما تبدیل نگرانی‌های احتمالی به مطالبه توقف اصل واگذاری، راه‌حل اصلاحی نیست.
🔹
مجلس می‌تواند و باید ناظر بر اجرای صحیح قانون باشد؛ اما انتظار می‌رود این نظارت، در خدمت اجرای تکالیف قانونی و صیانت از منافع عمومی قرار گیرد، نه مانعی در برابر اصلاحاتی که خود بر ضرورت آن‌ها تأکید کرده است./ اقتصادآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/696998" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خیالبافی مکرر ترامپ: نیروی هوایی و دریایی ایران را کاملا از بین برده ایم/ هیچکس از محاصرمان از تنگه هرمز نمی تواند عبور کند!  ترامپ:
🔹
ایران روی موضوعی کار می‌کند که قرار است نتیجه خیلی خوبی داشته باشد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/696997" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">24-1 Ane Manaee (1404-02-13)Mashhad Moghadas</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/696996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وچهارم؛ بخش اول
🔹
ارتداد یعنی عقب‌گرد از مسیر هدایت بعد از شناخت آن، نوعی بازگشت به پشت و دور شدن از نور الهی [01:45]
🔹
تقوا سیستم هشدار درونی‌ست؛ هرچه قوی‌تر، تشخیص وسوسه‌های شیطان سریعتر و تغییر مسیر آسانتر [06:08]
🔹
علامه طباطبایی: بیماردلی = ضعف ایمان؛ و نشانه‌اش سیر قهقرایی دل است از محبت مؤمنین تا حب کفار [10:58]
🔹
تحلیل ریشه‌های نفرت از مؤمنین و گسترش تدریجی این دل چرکینی و ذهنیت‌های القا شده در دل انسان [24:23]
🔹
بازبینی خود، ترک قضاوت عجولانه، و پرهیز از نگاه تکبرآمیز به خطاهای دیگران، درمان نفرت‌ها و سوءظن‌هاست [27:58]
🔹
نقد خودحق‌پنداری، تحقیر مؤمنان و فاصله‌گیری از جامعه‌ اهل ایمان به بهانه‌ پاکی و رشد فردی [34:24]
🔹
"با مردم باش، ولی در گناهشان شریک نشو"!.. فاصله‌گیری از مؤمنان، سرآغاز انحراف از جبهه ایمان به جبهه کفر [38:14]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/696996" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90313e13ce.mp4?token=oVtniyr2pFxg8_8cbkqpXkaYCogNL3dXHBcDSUm9ClIgI7ZqZgpNo-0abLXipOM-cmD2Rp739jC1WtwI1qEok0rUGwRceyJ783txZtiErfTSFrdMyFvoAz4ckfPM6tq22g7JDKmHk2M80PYATCOY1fFAJRRx-V4BKX6J5927VpLlJibecNxc1Mf7loS8Ec3R9I_a8lXDlUXvxvbZEydl1Cb7pmduCq9Hb3wzQtj8FGgThLIQlI7-PfzM953_lIWNq-m3OHidZH_fVvdG3-i6UjTDO96JfaOxUcBjcxbCFgZQnKt2Y0ewwsL-f8EHeDahO7iRubcQsDM1EKwWnSxaYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90313e13ce.mp4?token=oVtniyr2pFxg8_8cbkqpXkaYCogNL3dXHBcDSUm9ClIgI7ZqZgpNo-0abLXipOM-cmD2Rp739jC1WtwI1qEok0rUGwRceyJ783txZtiErfTSFrdMyFvoAz4ckfPM6tq22g7JDKmHk2M80PYATCOY1fFAJRRx-V4BKX6J5927VpLlJibecNxc1Mf7loS8Ec3R9I_a8lXDlUXvxvbZEydl1Cb7pmduCq9Hb3wzQtj8FGgThLIQlI7-PfzM953_lIWNq-m3OHidZH_fVvdG3-i6UjTDO96JfaOxUcBjcxbCFgZQnKt2Y0ewwsL-f8EHeDahO7iRubcQsDM1EKwWnSxaYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران احتمالاً مکان‌هایی مانند سن‌دیگو و لس‌آنجلس را هدف قرار می‌دهد #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/696995" target="_blank">📅 20:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای ترامپ: من معتقدم ایران مسئول حادثه هواپیمای فلای‌دبی است
🔹
ترامپ: عقب‌نشینی بمب‌افکن‌های آمریکایی از بریتانیا، در پی یک تهدید صورت گرفت و ما می‌دانیم چه کسی پشت این تهدید قرار دارد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/696994" target="_blank">📅 20:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696990">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hk-ply1L81ay-0utreh_tY3PUeu3-6UIqxX5hyENGCFH7gX-LN-hx4q77zn67pysbnSYH6pbH9AB09MpupzqYbAYER_HHsHkYOFWzauwBv5FjzmLP4MHollgy93v5Nnv83QLYkP9lQowDi3zGFR8mP86FovGMjgPewENREp40ikw0eBxYDRvwjGJin0Vt3KhEOxGVolpqQVB5CoQNT9JZV3_TngVhIsU7bYAjbgExdTCH8mJ3hoDt2O0N4l7gHj9NrAftK0_IeOuUekK09qT1tkKwBaNlU7VHzHgHeLP-7AlBFbIne7cU64Z0lPvkvgcEb-MHwmzM6ykP9kxmAzAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6pxeCe1nUMXOsDiwWq525A6lFQO0dbUbQTWdqVHLJCJ0qkSPCw64VbqDJ2B_0kWL1mVAYoLmAa6zDP7CMI30Gk0ZbRQOL9nxPAGP78kgiowLHSHr-g1yzrfedDDFZaX3ktFStq6zHpjXKOxqruEMRMm61HTKcXlZab-JpF9zN-ju1l5-N37LMRafSQ03J0thH286YsUIb-LDkjSRyKQDQwMAjrOyI1348s0ThcBL7MVjO6sAONxfockZTLbGVpiZ-RGDwHY9LkLf_ridZsmu5xSF_jDApDiTeEQCz7DVqXzzBVc6gBqsK17ElT2I_4jFqdPL6VMede8PjkFC7Qwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuEvL2BgjSg0Iy08Big6qhQY9ZTXfMte5mU6vLrRy0C02IcwZYGeAck8kEQU12ifvZbnibVjcfceQbP-UM4O2WRPLTubk_ME2N_SEROAJuV5fE3z2gEVw1PjHmXhK0-y7CR2_2xien9KQcZIJoiEACuEFAVjC0m3BniQ6vlA3NdKZwmg3JlDEBusFVNWfYcifwM7c66MOMv9GHZtvaChMX2wbRwyaYqZSexxb5ToJTkYjdayyxPvz-0XlAqBSYxcnVbXzU9BTAxPcdWPvD2don48t3CDARCKeVMS3T4sr8XfjZRSVu4SJcrNOWf354937awrsQzkt1Dz6SfF8eJJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U34ZWpCIcekQ-JURfTIPFtH1bAUnm9uh3c3R51eyCB_5yKemjmfCFPdp_9yjADLcXE0oy4cOu9afvP7OFfcn4U3VWn61w2wsMrbIi2QdACL8OuWXfis2pFwug9jOFMQDXcgIXTda4eH4h0GJSazPAnM7VDqK6OnnzBE9NcUxCRMCHWCQi_b6nQtRiBB7IUXFmPA1oCGgyXfYFN_59f-Q9rOQKdz-44_K2eakIdMui5U1Lak-NRgxRtRK_8QqfuSnBGnFCHtyzfaaQJsHNA6LmnfZtoGgs4OAXkGrbYB9Yhzz5dHBLjHE1-nwh74WOYUK98Ad80cckIebppDS7T4ZDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع غنی امگا ۳ را بشناسید؛ برای سلامت قلب و مغز، این خوراکی‌ها را در رژیم غذایی‌تان بگنجانید!
🥜
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/696990" target="_blank">📅 20:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alEMRbVd2qYfsD7CO-YHwLseKY0_vcQVU57GXyhzJ3j_IUuadl2h0SrdZ9adxRTjyaLRv74Thgd4so_CyIYCzHpG5EqyCMsNLwD-G_nxcfJ5953pQMJgIgwfhBYDIuOpq3qsYz2DMNTKjrr3OAJqeLIZRGN8v7GV71KCHg_PDxrjh0t0qMk8fu8kdv-Ihwfurd-KDXsuXzW-AsjEuFuJUr9U6MybN0whVj9CXWGyklBhOZU2dGOfa_wTL3w9vbQUhn9HmjZpZT-mv-A6j7xYdwr9igeRl4CKefbtWFxWrgvZGPSXGFLhvzj6dcPI9HY4camgP35AeKQM7vpb0--ljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696989" target="_blank">📅 20:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696987">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ترامپ: ما دیروز، ۲۸ میلیون بشکه نفت را از تنگه هرمز خارج کردیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696987" target="_blank">📅 19:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696986">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خودداری سریلانکا از کمک به کشتی‌های ایرانی!
🔹
دولت سریلانکا اعلام کرد فعلاً برنامه‌ای برای کمک به ۱۹ کشتی ایرانیِ گرفتار کمبود آب، غذا و سوخت ندارد و منافع ملی خود را در اولویت قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696986" target="_blank">📅 19:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696976">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYI3l1gboXi8bQ03HYHeJDzKVhgqfL_lW8Tx3kFolp0QUCA86m2RnzmFk9wMShdz2bs-fPAAwbIYVqRS2gsa4uFsA1-8k8sx-iLRRDrjouzZDNg2KAS4seYDYzpQkRP_JVHk0JjhiqSg6Jzy7iztCq2-Lgc4b7bf7hUBWbcWN-FFzyEu8wh3Ll__pm385L-PGGw9xUzFzJDwnl76P-sAGBzLD8StTzXbsNpVXDO2tii8lhiBFeooZnFBhwi2XhndK-ehmb5EXyVAmVAtamM_DMr4-_DT2UDomwW46KhYwhgtLzXdewUwSqk6YTGeFqQ5mywmgdP1B-C4z4PBBIoKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SteDY1_5pS77OEHF0pj4Jt4YYFbQRg_wM86p5Cg4iqzU7Ye99EE84jHfYrkPHv4W_pQxVJB_CDytJ_rpPXdA7yLYhU5ZYTSrdBmAblOkkGJAXSzTBMuL-klyheokfPsmHwjPxG9NTjzelutFFu8cMJ56yCjLJfwwPuPAuVgYHBzHjfUqOYOHWpHmh8TRBolr6tsTrpy87NFQNf98N52ea6SKpgfgM_hytEGxGaQ2wc1Kk57bFl_GaVka3j8LiTF3PtOXUglCuxBFLaW4P2GvUKZyzBJzJmMrl386RcY0JOKIGkLdwyDtGBpnx2ht5Fl2aIZNOTdTr4UyHcXzSak7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItmBiUImR9di6LpPwwUw8WkOy5NjSeyw1PyKQMISe77kghUqOVVbkQOzeT3CRVuJTZxH8ullpIBJ-tw2IUs34WWOa1hqRArozkbwXykuaHcLrli5C6KlQ8XYim500xNuLy92zB2zesOXtko2mcTS6uZPbzKUMi0TNdh_FSFfTv6bN6Z7i1fSoSTNuY_i3dvucRm3cay82H7KLrSJCYPkYTKZICHBffCav4bHggPEUPLkLq2kAwTWkvsVLBuxTCNGUh9SoC2A_3VGxT_ubSSV1S7nUtNM1jPRGeAWaHenP_jMz6F5g19Y7A_xQoR-Pj7t_W0fDklGeFTbtf8XT1aZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGmSb2XyRwPzKhUDX7nUPYWCeDHrpk8rpOM87QhvRVzp57r1_lmZ55TwCAFA_xjM2Wgl9qfXKCX92R-rPHDVRo4R74UsJ0MZqkScenRtXJI1kKIVIXX0OncVHrYhmBlqIasjzZOV00KkaZbdhKukTjKaEUUs3giGaac6h1WHvV3_CxtPlB9QQ-jNFzzdotxOIrVKz-eC0_grpSTnY621FvHUZMogwsvnmQj0Z8lyDSuzCO75Mwg3dqfqfdTpyEPUWyqLi3JOkTE5L6GLYVV4se9NL9XAa5bOZeqmxADFovyq5_5xtK1PHlqIJnYiXtaH_QGOLUastZj50g8m9ElDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZNXETLf5VUw_HNc9wPQpl87VTyWVs90dMNcZoh7AWw65qwEBLL5FlE04LtMZfErdBbLp5L2b1aFSvP5TOwcPIHxyhuYHNARVHRV307XBA3Fcqpl1iUKEnpz7MZfymMUabUO3NpPMkVe3-W5Qz5pc9oKHRqGRg0ySnTw_-X6tdKocls6JTWnWGtuWoJFN2xNk6hS90hXsEw9lf6JJdEHTiCbt7LF01-lgMNg_58h3NfjkVjqoP65q4sSQxcD1dSSJ9L5Wc52TcGx7_-0cQaurxH1wL250bCYXHmMopuNrnUNPjGS2jYER6T-SQcFO9q2u-U_lcMxaGx2-t-s9-eQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mW-FfZADy1QNJKFu0x-_oZeiJM8h0YTx3pAjAWpcz8acm7IvGkTDVyQFnZUE82VZWjrzE5P125QwYThqWake1v6KXirOEucved9wwc9OeL75GzNaAbiyOsdl5Mx19gXJv4nDTdt0xCwzJKBV_X70hGE_JPGQl01gnFDCSO7SKXcY0sf_l8ls-LcVdcsM_PT29EG6-_uBzSawKku0RRLlIv6v8jUnv5kqfC7Kh2AJBDq_yJVW_D7VZimvh4pd0jpkFhKD2kThvJ8UoIo9nNA1-qyrgaRT8GLNrYYSARNGaR6buP5ZCeeH0Gj7eOcmPaY_IfKan8t_lMCe35HdoapLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GffxTLkeP_hPW3kXoOxZdFMDxgIkprA3vFCu9pa0kfPpXUk8x_Tpnl5O0gHKb4wiN1-mMSDA57fMe4wTo7Jn7JgILiDjUVG6CvkI5-35D0oIx7RUhNSmOAsru0sTcYI4Gtvo9nJqfRSwZCHPDQQbasTd_XYuPsfN4L0AxnXfT4mMg2HOy2cH-4IlwVxqaC28PszFwCGuSNd9k6ItQhmBDEUoTb-rfCpgnNNyuQLrXlAySEQ8gZcYzXzfDNmOaxmyGCi083WW0YP8uIKURP7K1HTJf0X2H1bMN3gl525yPxUwXNmB0SUFLu9wXRbXr8ATQdextbJS5kxWnCEnBIC1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyZBqW-zcbW8sEgf3x5ucteb2t60FXJIPeAKE1aUTPyek4zGDZGwI4aqhVxxCqDlWAjzgkNkfFnd6AULK-pjBuC5GRrM-yOrmkSMKDZLO30wbJFucjUaJjRz72JIOtBulvrpdBXLPfNMJTWrrbfc62LDeKy4ngC2oii-mx5TZphuht8bmwv5qK9zyxWQMP2dKY4RGzzDtww5bQsDDU81AIgNRC9XvYxounypDZmvKLqYWoUxsm_C3IySXVKAjrOqbC6yKN9kQEU42An_BJa3FRlY8atGmXqWZM0K7HXsVjl7zW2BlM8l-GYlE1oIw92StDivUBd4HutJNQY4pEtrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c84vhMK0JPA09DCpupOzZyikm6-ZG_zLL1-wjUa70zwr9ONx9-DOVT1mFPTuRUdQglXsZzuZFKAugYNVMTSaWHq-wWBnd2RIfnRQqLSO5AWChUGMkMgZs3nkP1hmynKJMuGNpEruaaDIqA8fQ9ExtPMNQLNYK2WdDnavME0S9ulWXYuw9oZjS_0d3gOhYcYo6Z-F0VNUl32fUeYBvHen_CZ432oxCghi2Jxs4RhhuKHbNEwSQMXLLxvMmzrv8YnxrXUxgqixW9LhpG1AHkWJB8zmmVsjr54KfDF7K7kcxwcEWtIXPMtDIN2gkMmeLKfE39gENrhPUVHzJHqcyf5elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YELZDQe0GOQd2SFeYId0RJXhLfUWtokKT0ccY73qu5UNsYMIiOBlIGdzvT5utELbBL1D34bvizmCCgW3gwTx5V5jxUUr3jsGwP-4Q4rGybyzDD92tDhCB7tVvhft8YgV_cgJHE4NVF7AtCpY-lZdrQwzUcHPI_NnXbFHKvf9Ey-kW2v3st1bQs_5-0cTgD1xvQvs0G-LdbfqTeZ2iM9nVIFeKopTePDTFA7zigmpTDrRZ_hRMTCBD8svwJCvb-Jgd8WjbDUx3kprRFO3C1lmkEMW2CiRv8i9GBLJV2furgUdVFN0HLZaceZYiWdSqxAuhGf6RofYiqTUtnqdBhjE_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صف وام
🔹
موانع واریز وام‌های تکلیفی، به معضلی جدی برای خانواده‌ها تبدیل شده است.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#صف_وام
@Alo_fori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/696976" target="_blank">📅 19:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696975">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
مدارس هرمزگان فردا تعطیل است
نحوه فعالیت مدارس از روز یکشنبه مهرماه به شرح زیر است:
🔹
بندرعباس:فعالیت مدارس در تمامی مقاطع تحصیلی به صورت سه روز آموزش حضوری و دو روز آموزش غیرحضوری و مجازی در هر هفته انجام خواهد شد.
🔹
قشم، سیریک و جاسک:فعالیت مدارس در تمامی مقاطع تحصیلی به صورت ترکیبی از آموزش حضوری و غیرحضوری خواهد بود.
🔹
سایر شهرستان‌ها: فعالیت مدارس در تمامی مقاطع تحصیلی به صورت حضوری خواهد بود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696975" target="_blank">📅 19:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696974">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEIW38vnDqWTFM3vtrpl4Ml7-BR6a3kJcEQ8mkKcsAPm0QmhTPDwxhYMR_T5LsDgD5_AacGjDRRVx7wLMMiKhKAX2lntktTTXu1FLn8lJMsbKp6XMtiwrLZSwYY9wEU1filF-ep8lhOD9XKXc_FCNDEf7PSl3M9MOkL45R3x1rWbRs4XnGHvxjeVFjUbPuD7jVB4bzDxXIcx4riHoTYqjxU52UYRmXHaYZSd7brgmUsI_32gGBqp-IbpKJmAOg29z9pgzDIRJ-hL4YjUZS-4bhxwrxKpTDQZA2ixYk3UtofRKnzaf_9p6K8D78DFmegPib5-Sw3nuBTEBaidnE2OSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696974" target="_blank">📅 19:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696973">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3744f0de5f.mp4?token=fUUrA11F1TY5yM5WwrvCQOcXhf15hyQ0NVcb0AC8yn5hEXcvUH2f7ftjr5ZS1n3QyMzhbhENPFzO61xS543MGIZc8DWDBwx2Znf4XI4Sn3dsOSkf1Xfax5hwQAkVEb4ijGKzrporUzzawCiCCsYnUXTWQsMTOCfCmeIgQU4KIDLmaLSA0e7fUn2Ryt7NiKKFD-Q_i4JH0YZd_k3TuEH6WXHVIa_gfC3KXbEbVPuNSLJ3rdR_dkG4uUR8neIeZ11CK4r3WVkLR65zLExOa7l0TX5bOAFpN2CD4rUKIvHYNsNLzpNy1fgku4u0q40rrGimdHQfaXSmjXSd7TQWO-5aIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3744f0de5f.mp4?token=fUUrA11F1TY5yM5WwrvCQOcXhf15hyQ0NVcb0AC8yn5hEXcvUH2f7ftjr5ZS1n3QyMzhbhENPFzO61xS543MGIZc8DWDBwx2Znf4XI4Sn3dsOSkf1Xfax5hwQAkVEb4ijGKzrporUzzawCiCCsYnUXTWQsMTOCfCmeIgQU4KIDLmaLSA0e7fUn2Ryt7NiKKFD-Q_i4JH0YZd_k3TuEH6WXHVIa_gfC3KXbEbVPuNSLJ3rdR_dkG4uUR8neIeZ11CK4r3WVkLR65zLExOa7l0TX5bOAFpN2CD4rUKIvHYNsNLzpNy1fgku4u0q40rrGimdHQfaXSmjXSd7TQWO-5aIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما دیروز، ۲۸ میلیون بشکه نفت را از تنگه هرمز خارج کردیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696973" target="_blank">📅 19:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: چه کسی گفته نفت مال مردم است؟ نفت انفال است و متعلق به خدا و رسول/ نفت سرمایه کشور است، نه درآمدی که آن را بسوزانیم
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
اینکه همه مسئولان گفته‌اند که نفت حق مردم است، بیخود گفته‌اند.
🔹
بنزین را به قیمت مفت به مردم می‌دهند.
با محاسبه کارشناسان قیمت هر لیتر نفت ۲۵ هزار تومان درمی‌آید. در آمریکا یک لیتر بنزین یک دلار است.
🔹
دولت این پول را تامین می‌کند و از بودجه برمیدارد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/696972" target="_blank">📅 19:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e4dfdd97.mp4?token=LOH7LRbINlYwHjlJP20POyIfY53958tN7Vs40tlKEYhX-rvxKnQXCFd9b5wqIOLTY8s9vRlTZAAhQA9S6aDT7n6WElHGF63l83Noll__vQsBHQgYjIxj80iLeSxX5tjig6ZUCxINFz1BVu7IGuc_Bs91qnwZqJrjwXamlCqiH_sXOfrJQoqk4RZVnz9fnvkAd81_K3K5oBQeP1qjrsiSEf-j7Eje1cCT2w526U5dGaDpHOuclyqmwYnARTbnAiRoVYH-VGjZvjWsljMgA89uTUAGO-HoDx2usmMRomGUzOakdKC8Gq7Wy6hglUiyN-CpXTq66nI9mXqvJF8qVqmmLEolINzx_SxYgwM6E-E6t92JQLG76aJ972TLbwhndLb3BBSNZZ_tkZDHYJwRvFMF5ctdUCTOOHwcW68a3jV9mAVUBrvmRxBvwb_39wtB7AQkin9trfTLLmX0Ty4BfnRNbtoLnNDkYgyV2ZGxe9QJvRzI3YEW-CZ3t-p0Qk130iGgS06x1muB-HOHVU8RB-6CfmUKjckT8V5GFWEzSfp753EsEKsbitiNiYrLit-FMFa6BVTupAU8fMJaTHs0vSi5XoT7XaUZg7mY7tPMz_d1nNkPv69-_1YhDst6YNzx6CWBDeR0PUe4fFUI2o45Wd1EOAI3ZrwTzuCmUMeot-Sy9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e4dfdd97.mp4?token=LOH7LRbINlYwHjlJP20POyIfY53958tN7Vs40tlKEYhX-rvxKnQXCFd9b5wqIOLTY8s9vRlTZAAhQA9S6aDT7n6WElHGF63l83Noll__vQsBHQgYjIxj80iLeSxX5tjig6ZUCxINFz1BVu7IGuc_Bs91qnwZqJrjwXamlCqiH_sXOfrJQoqk4RZVnz9fnvkAd81_K3K5oBQeP1qjrsiSEf-j7Eje1cCT2w526U5dGaDpHOuclyqmwYnARTbnAiRoVYH-VGjZvjWsljMgA89uTUAGO-HoDx2usmMRomGUzOakdKC8Gq7Wy6hglUiyN-CpXTq66nI9mXqvJF8qVqmmLEolINzx_SxYgwM6E-E6t92JQLG76aJ972TLbwhndLb3BBSNZZ_tkZDHYJwRvFMF5ctdUCTOOHwcW68a3jV9mAVUBrvmRxBvwb_39wtB7AQkin9trfTLLmX0Ty4BfnRNbtoLnNDkYgyV2ZGxe9QJvRzI3YEW-CZ3t-p0Qk130iGgS06x1muB-HOHVU8RB-6CfmUKjckT8V5GFWEzSfp753EsEKsbitiNiYrLit-FMFa6BVTupAU8fMJaTHs0vSi5XoT7XaUZg7mY7tPMz_d1nNkPv69-_1YhDst6YNzx6CWBDeR0PUe4fFUI2o45Wd1EOAI3ZrwTzuCmUMeot-Sy9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یازده سال فعالیت پیام‌رسان «بله» در مسیر توسعه خدمات دیجیتال
🔹
پیام‌رسان «بله» با گذشت ۱۱ سال از آغاز فعالیت خود، همچنان در مسیر توسعه خدمات ارتباطی و پرداخت دیجیتال حرکت می‌کند.
🔹
این پیام‌رسان در طول بیش از یک دهه فعالیت، بستری برای ارتباط کاربران و دسترسی به خدمات دیجیتال فراهم کرده و با همراهی میلیون‌ها کاربر، مسیر گسترش خدمات خود را ادامه داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/696970" target="_blank">📅 19:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: دیروز «بیشترین میزان نفت» از تنگه هرمز خارج شده است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/696969" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پایان بازی| ارونوف برای تارتار گل کاشت/ سرخپوشان به یک‌قدمی صدر رسیدند
پرسپولیس ۳ -- ۱ صنعت نفت
🔹
گل‌ها: تیوی بیفوما(۴)، علی علیپور(۵۳)، اوستون ارونوف(۸۵) برای پرسپولیس / محمدحسین باصری(۶۵) برای صنعت نفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/696967" target="_blank">📅 19:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/696966" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e3251bb3.mp4?token=iaOs81O4mfsfbiYfXzVUOE0-gnzQg31ODHQFy4t6k_bPtuLHVx5F4yH-7TLH6ULPseyd8fLwY5_BKHyLOu55REJV-9akL9oKBH11IlO7OfBp6Bojd6CH2Mz8F-eluBSzpYSi-nhujhdGI6T2u-YfFY6DhRGOz7s1dGH12D2at42dK7mI3sDVtpOtvajFBuR-TxstP-_KTh8ZJ0R7-KsqYewiUTqArtAIcLkHqz8fVBPy6_T1sX85gnlQgsW-IF1huF3PSF3dELZp364udQcyZwJo8XhlkSNZSF8LbUbBVcDIegVcOsritsMNDqEzzYyzbFVUwk4ilGAv_Z0GLns3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e3251bb3.mp4?token=iaOs81O4mfsfbiYfXzVUOE0-gnzQg31ODHQFy4t6k_bPtuLHVx5F4yH-7TLH6ULPseyd8fLwY5_BKHyLOu55REJV-9akL9oKBH11IlO7OfBp6Bojd6CH2Mz8F-eluBSzpYSi-nhujhdGI6T2u-YfFY6DhRGOz7s1dGH12D2at42dK7mI3sDVtpOtvajFBuR-TxstP-_KTh8ZJ0R7-KsqYewiUTqArtAIcLkHqz8fVBPy6_T1sX85gnlQgsW-IF1huF3PSF3dELZp364udQcyZwJo8XhlkSNZSF8LbUbBVcDIegVcOsritsMNDqEzzYyzbFVUwk4ilGAv_Z0GLns3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس به صنعت نفت؛ اورونوف در دقیقه ۸۵
🔹
پرسپولیس ۳ - ۱ صنعت نفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/696965" target="_blank">📅 18:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ab30119.mp4?token=A-XzLxT2TAWL2AvH-OamqfITcEQ5n8k8cm5Mcu1Q9Qvww8Icu9b3BRl8TVLGCrVrpB-WZlWB-snGVta_71QqIhT-9_oSEYEHwvll6bzLkR-lqKjtakrgA4ckkpc_MpwOU6ePvnHNF4DYaPRg6ThPagSr_VqSFgZqePFpOHqFpK5QIEA4xtRvGG6fS5ScapPie-IX5qnsfZU7xMYEMwCBTI2fxC059TB4E1gKNc0iiKkBUe_OxJO3527PP0R1jYNP153Mfwj6_MaiKMgp7-5b-zDXOB2YbODGOrpZMdHwR-7B8c4T309GQSIbOc2PLqCsc6B8ruo4sl_FiHUym7dYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ab30119.mp4?token=A-XzLxT2TAWL2AvH-OamqfITcEQ5n8k8cm5Mcu1Q9Qvww8Icu9b3BRl8TVLGCrVrpB-WZlWB-snGVta_71QqIhT-9_oSEYEHwvll6bzLkR-lqKjtakrgA4ckkpc_MpwOU6ePvnHNF4DYaPRg6ThPagSr_VqSFgZqePFpOHqFpK5QIEA4xtRvGG6fS5ScapPie-IX5qnsfZU7xMYEMwCBTI2fxC059TB4E1gKNc0iiKkBUe_OxJO3527PP0R1jYNP153Mfwj6_MaiKMgp7-5b-zDXOB2YbODGOrpZMdHwR-7B8c4T309GQSIbOc2PLqCsc6B8ruo4sl_FiHUym7dYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلطان شناسایی شد
مدیرکل محیط‌زیست استان تهران:
🔹
یک پلنگ نر در منطقه رودافشان دماوند، با نصب دوربین تله‌ای شناسایی شد و نام «سلطان» برای آن انتخاب شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/696964" target="_blank">📅 18:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: من چوب آزادی‌ای را خوردم که به ناشران دادم/ ممیزی کتاب نباید دست ناشران باشد، چون دنبال منافع خودشان هستند
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در زمانی که وزیر فرهنگ و ارشاد بودم به ناشران گفتیم ممیزی انتشارات با خود شما باشد و خلاف قانون اساسی عمل نکنید وگرنه با شما برخورد می‌کنیم.
🔹
چند ماه گذشت و این ناشران برای پول درآوردن خیانت کردند.
🔹
کتاب افتضاحی را منتشر کردند که نمایندگان مجلس به من گفتند این کتاب چیست که برای چاپ آن مجوز داده‌اید.
🔹
کتاب را که خواندم تا نیمه های آن که رسیدم حالت تهوع گرفتم.
🔹
به مجلس گفتم حق با شماست و در فاصله کمیسیون و صحن علنی، معاونت و مدیرکلش را برکنار کردم؛ به آنها گفتم هیچگونه اشرافی ندارید به کثافت‌هایی که منتشر می‌شود.
🔹
به نمایندگان گفتم قبل از پاسخ به سوال شما از درگاه خدا استغفار میکنم.
🔹
ما به ممیزی متمرکز برگشتیم و الان هم معتقدم ممیزی صورت بگیرد و نباید آزادی در اختیار ناشر باشد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/696963" target="_blank">📅 18:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a955c8f2af.mp4?token=CXohBkLgsW-wFVghxOwDsB7uPw_dtncshzQVu5Zn7uD_X62RYY7L8vR9HqmdS6448hQxPmf8ZiEq0VUdp6GtqgNCZA08ofhlEUap-cu-mx0NVKNU6V4yUSOdKN4wnzBtUqRY8CsoibnIbjz8XEj_sd4qJ14SHkO3RZOZeg0J1XUR9YSphc_180Kk3Jrrdme21YX7uPG2lV5I57ypLd5Ep4UFYr85xwraHr2nUe4vKZNbwHAYKk0BLHg5LvGuM7fmL9vmsawf9jBQ1PI8j18kCw8Z9npJ84qubQ1w8sqknaspg6Yn88kYuUoFm69LlYYJoBWDDc0Q5VNzWO-VhTOooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a955c8f2af.mp4?token=CXohBkLgsW-wFVghxOwDsB7uPw_dtncshzQVu5Zn7uD_X62RYY7L8vR9HqmdS6448hQxPmf8ZiEq0VUdp6GtqgNCZA08ofhlEUap-cu-mx0NVKNU6V4yUSOdKN4wnzBtUqRY8CsoibnIbjz8XEj_sd4qJ14SHkO3RZOZeg0J1XUR9YSphc_180Kk3Jrrdme21YX7uPG2lV5I57ypLd5Ep4UFYr85xwraHr2nUe4vKZNbwHAYKk0BLHg5LvGuM7fmL9vmsawf9jBQ1PI8j18kCw8Z9npJ84qubQ1w8sqknaspg6Yn88kYuUoFm69LlYYJoBWDDc0Q5VNzWO-VhTOooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی زیبا از حرکت مه بر روی ارتفاعات کوهستان سهند
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696962" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rdCpKQ36ikHdvqTbm-tts4cE8ojOcDUaSA1q1f0T8aRHCWNt-ynxSnU5FJaeSKIo_3kX_HCUXObfF_EPxOcGDwTNyZijdxDMzAap3xzPxndzNVLh8RrYyJumSFe7S9r9qB6GAhaXmT_UL9q1E0uIsUCESPHhdjhjegmJhhGPFo7c1WIUfOi2zGei99zkyepDl2YVdwXlgRIaAvuE3iQQ9_bscjODBv6uL8I3wz6dwZy-mUH5fn42GE2RHmR-qE1TK9tk8xegc1eZWpELXy1PVHFX9BjpGRzKSOQ0CCvtcWln_-HkEKhIuvYk5TVqptp7_8PIN4lvZWTf50caqhUDlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rdCpKQ36ikHdvqTbm-tts4cE8ojOcDUaSA1q1f0T8aRHCWNt-ynxSnU5FJaeSKIo_3kX_HCUXObfF_EPxOcGDwTNyZijdxDMzAap3xzPxndzNVLh8RrYyJumSFe7S9r9qB6GAhaXmT_UL9q1E0uIsUCESPHhdjhjegmJhhGPFo7c1WIUfOi2zGei99zkyepDl2YVdwXlgRIaAvuE3iQQ9_bscjODBv6uL8I3wz6dwZy-mUH5fn42GE2RHmR-qE1TK9tk8xegc1eZWpELXy1PVHFX9BjpGRzKSOQ0CCvtcWln_-HkEKhIuvYk5TVqptp7_8PIN4lvZWTf50caqhUDlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول صنعت نفت به پرسپولیس؛ دروازه سرخ‌ها با گل باصری باز شد
🔹
پرسپولیس ۲ - ۱ صنعت نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696961" target="_blank">📅 18:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a787cce95.mp4?token=tm6WvC8sGXMMvkcgqoDyd8ROKtDfyGBPpEkGSaNSd_kAdKTzUIL8NerVeaJa-04MTzuCs8gIFLcvQXDlOO_bKJYWlmeeTQRe7FJjxF7CoJBkCiMIBTGLgacbB5WABPLdzO5p_sXOnFkaOti7Hqdy28NvceEg8B_YSSCrgjdl3UEGUtawO-ypqSYji4IJ5aCadnr-_WYAApv7o7wovZpO5A6DIRwkf2CmY3XOVmR8FL4-EIW9yRXBLHyZU34tjrBhAJiYaQRTNaRu8R5GRNVw11qquIkQOrC-I7YLXyyuD1ByHDFW15AS7lmGMflykYAxa8LlRatNG866zsE2sfZhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a787cce95.mp4?token=tm6WvC8sGXMMvkcgqoDyd8ROKtDfyGBPpEkGSaNSd_kAdKTzUIL8NerVeaJa-04MTzuCs8gIFLcvQXDlOO_bKJYWlmeeTQRe7FJjxF7CoJBkCiMIBTGLgacbB5WABPLdzO5p_sXOnFkaOti7Hqdy28NvceEg8B_YSSCrgjdl3UEGUtawO-ypqSYji4IJ5aCadnr-_WYAApv7o7wovZpO5A6DIRwkf2CmY3XOVmR8FL4-EIW9yRXBLHyZU34tjrBhAJiYaQRTNaRu8R5GRNVw11qquIkQOrC-I7YLXyyuD1ByHDFW15AS7lmGMflykYAxa8LlRatNG866zsE2sfZhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی پربازدید از زد و خورد یک معلم و دانش‌آموز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/696960" target="_blank">📅 18:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=GZGWz4STtzVxYqqbbNL-miZyDDa2730l2XXentt07h-W-4TW0q7QHKtezE-Lb9zlaJS7Wcl1lcBdaQ4N1elwX0bck0KfPlIgw6jV-ButKX2RFGqv1zx3ZqppO4tZKiXCbb1uoKU6-o4ys2hNpJ1PNa9IJfwac5LVgnOstuVOx0CZESp9A6ypB6OurZ6LIkpTWnsr5Vjvc-aNeRxL826jcbmFmKBdGPg7WovQ-hW2x5l9IySwD1O6zjdu7b_wCYE_FOkwWNP4Z4tqbB9mcKTVoH30T2_5jhmTBOLyZVstrWLM0ePeaHUnAxazCEora5OJm-GfdxovFK1gMNq8mzNm7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=GZGWz4STtzVxYqqbbNL-miZyDDa2730l2XXentt07h-W-4TW0q7QHKtezE-Lb9zlaJS7Wcl1lcBdaQ4N1elwX0bck0KfPlIgw6jV-ButKX2RFGqv1zx3ZqppO4tZKiXCbb1uoKU6-o4ys2hNpJ1PNa9IJfwac5LVgnOstuVOx0CZESp9A6ypB6OurZ6LIkpTWnsr5Vjvc-aNeRxL826jcbmFmKBdGPg7WovQ-hW2x5l9IySwD1O6zjdu7b_wCYE_FOkwWNP4Z4tqbB9mcKTVoH30T2_5jhmTBOLyZVstrWLM0ePeaHUnAxazCEora5OJm-GfdxovFK1gMNq8mzNm7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به صنعت نفت؛ علی علیپور در دقیقه ۵۳
🔹
پرسپولیس ۲ - ۰ صنعت نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696959" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
امام جمعه تهران: پرچم داران فتنه زن، مردگی، بدبختی، ترامپ جنین خوار و نتانیاهوی پلید بودند
🔹
همین ترامپ قمارباز عضو جزیره اپستین و جنین خوار و کودک کش و دوست پلیدش نتانیاهوی پلید در جریان فتنه، پرچم به دست گرفته بودند و به زبان فارسی در آن فتنه پیام و شعار…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/696958" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMIdq1gA_Vi-2oy4TIUxgpYKBjn1uC-ARWikQ3LEAXKFkJFUF9FUQdFVG9Wtf-OlmZNSLYVl3RS9wXMi_o-yqVa4jrFbVJZB37C7vYP-ahb02B2KAfsG-GxfSqjwlhBqQbbkavc7jfhmAwPaZZjbeBsWw3NwjAfO7hNI0ksr3J-N4hN1jmqg2cbnF66OO15Xh0JS0afZ_1Ei-XBr9_jN93zEU3hMf_67ylJYM7tCOB8wGZdcY-UW0ZFPjEZSvdMYHRMfBb5mMVsfl31GFKcH5wXrhVxLERImqCeRjS3YZ2cqE8I8w4tTVCuwXKxwu3JhXIZhjKCcFH6ueRT6-VWyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باز هم دست ترامپ از جایزه صلح کوتاه ماند؛ ناوی پیلای، قاضی‌ای از جنوب آفریقا برنده جایزه صلح نوبل ۲۰۲۶ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/696957" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: ۱۰ تا ۱۲ خانواده از قبل انقلاب واردکننده خودرو بوده‌اند و نمی‌خواهند این کار را رها کنند/ واردات برایشان سود بیشتری دارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
ایران خودرو خصوصی شده است و باید صبر کنیم که چه می‌شود.
🔹
کسانی که در سر تولید داخلی میزنند فقط به فکر منافع خودشان هستند و روی حسن نیت این کار را نمی‌کنند.
🔹
در یکی از کشورهای همسایه ۵ هزار خودروی وارداتی برای کسب جواز‌های لازم معطل مانده بود؛ خودروهایی که ردیف قیمتی هر کدام از آنها ۴۰ هزار دلار بود.
🔹
۵۰ مورد از این خودروها را در اختیار کسانی گذاشتند که میخواهند تصمیم گیری کنند تا راهشان باز شود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/696956" target="_blank">📅 18:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: امارات و عمان در اجرای سیاست انزوای کامل ایران با واشینگتن همکاری می‌کنند
🔹
ما در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/696955" target="_blank">📅 18:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
هشدار نارنجی بارندگی در ۶ استان کشور
🔹
مدیریت بحران برای روزهای ۱۸ و ۱۹ مهر در گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی و سمنان آماده‌باش اعلام کرد.
🔹
احتمال رگبار شدید، رعدوبرق، وزش باد شدید و گردوخاک وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/696954" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696953" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6TC_KQX3jNHxbUub6NwnqxEcWptadM7pBtJ6d3Dkx5G3eJl730okifPKpctkLkXG5VtFCwJaAIZTv8NUaMxV5L34pZsXvG2YwDqpt73lKJkPvKeO38Fen1JpWOodlftsgenlREwxvqCO1GWxIIL6hJBxb-lKdfiuCwGge3MP7985VxAZ6wUflb1AFIjyO4aGgm_a6ckeC5o-hJanl4LFemfCpRa0RNpIxIQv2Cr_hrDpsNhanrbjkjZ06Oek0uuoNt_WfKQ7XiUkHvZoflR75n8KmJk090AzaVdWo6YAoYVjH3UnePMcVwhDPEWTg4wPEn8EUO96NdbSIRw5CVGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/696952" target="_blank">📅 17:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
المیادین: ارتش یمن ارتفاعات مشرف بر شهر «تعز» را آزاد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/696951" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
