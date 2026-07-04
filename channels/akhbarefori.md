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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-666352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPX_Mm1ESN2VNaPplrXaBv05wU05ZAkYouSk7KIiqpEXn46e8CYzJ2cqoBpxVnWkzDoH6xP3mP0ZVsueJS7d0yW6qs3fa3GHpItNG2_4CqBLllQIwKf5V24kEBSCu6ldz8_5ZPB-HQBguZGO2zQ1UlBmI94K6x9c5AA7gZiWzF1cI1KMdPN7aCZbdWRwuENUWbHTqmCz6GUkIlGYAMoZWjakIn5_9k42ykHMWsRKkOqBDCMl_DIdtIy0E4acClNiqgViIPjlEli8e3qFvqGWkwcFOzi0qmv-XgifocDZNje3PkEXSftB7Y9VG-NHbeo1cSSvoxTTJ-rmenMLM9KsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهانبخش:
هنوز با این حذف کنار نیامدم
🔹
برای صعود همه توانمان را گذاشتیم اما موفق نشدیم. از مردم ایران عذرخواهی و بابت حمایتشان تشکر می‌کنم. رسیدن به ۱۰۰ بازی ملی هم یکی از شیرین‌ترین لحظات فوتبالی‌ام بود. امیدوارم روزهای بهتری در انتظار ایران باشد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/666352" target="_blank">📅 14:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imHuCABTwOCm2iI_T1DvlH6tGssyCO7d591_SNfLBw6WuyoRJqnuUOnn1xKq1YgldusUSB1QalLxSzRiqHnhfoM84CIQuK73Gk_N7-sPsA2pEvlulFuwZS-Rln93WcvR_FWm6wPUOw8eQqHHTAxu4VU5-FARZvlSc_uj7klrksD1RYEuVG5hmcUwFQF3n2zSFOL5Hu1B-VqWaflAoJLJl34TxGvjVQo2ara8mOuqN-B_TZbIrG7RfxrLIaHq6VZRHURJ-qOAham28IKDB_5pWbE4b79GT4hC9vZ7T4DFQyvrvjrHSFqrEsnu88HCna2DrcRa8SUMhRNOMuXw54pyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند راهکار برای مراقبت از فرزندمان در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/666351" target="_blank">📅 13:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a794bd29a.mp4?token=I4sPDHXZWluSb-b1k5nZZNj5YhiMDC6ZxYT5kOmS07ohKXiDWvwiU0BRbtntZr1txrV7ycrM8wVkqfSbC1drjy6XzJQD392UrZMLcpd02XD34sGbHg38bkhobKwh9W0MI5i5tHVUtgLzEjBWzS0-R8QiIZe6CWUoGHxBPRG5MuzZmR0MnEpP1HKg0eS1npORt0fAM6Hvvjb4f98bOubp4QcVPzE-TWaQJ86VwkdNAMcQ_fdEECx5qZhvKgDbZqDs_PPmBZhQRXNtiDaBb461yRd8OL-5Mnk7X-8XMRoWBY5IJYD9ugQWu4KakfMTlEIsbAcQJpdeNOUNcjbuykau5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a794bd29a.mp4?token=I4sPDHXZWluSb-b1k5nZZNj5YhiMDC6ZxYT5kOmS07ohKXiDWvwiU0BRbtntZr1txrV7ycrM8wVkqfSbC1drjy6XzJQD392UrZMLcpd02XD34sGbHg38bkhobKwh9W0MI5i5tHVUtgLzEjBWzS0-R8QiIZe6CWUoGHxBPRG5MuzZmR0MnEpP1HKg0eS1npORt0fAM6Hvvjb4f98bOubp4QcVPzE-TWaQJ86VwkdNAMcQ_fdEECx5qZhvKgDbZqDs_PPmBZhQRXNtiDaBb461yRd8OL-5Mnk7X-8XMRoWBY5IJYD9ugQWu4KakfMTlEIsbAcQJpdeNOUNcjbuykau5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پر شدگی سد کرج در مقایسه با اسفند ۱۴۰۴
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/666350" target="_blank">📅 13:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPegM10byc63jrkg-jffF4Bmb0es3OMTZncI3tXVv88lCDK42pJMlD1SP71XVlECHvekdu4fvaB3J6wlTOAUMHS_wfqoVhlMfnE4g-1EygOiD9AU7zHVxPqzBb-pwwrtfm4gx_4lcXJ1m48VqejIfWhvSZ7ngIkHsK4YAkrjojEsG8bQM-tF2rjgK-TNzsJL0p51ZGpbLcm1G_yfeWBMnHpzioWASxwR9U71aNBybyHPXuxgNUtHrmKOygqQQGlXGRBQS2xjbrU6RgDqY3Avmz5_0VRItWQWNHnM6uiW-Ab-vONz6LZ8fYsEkL_8vMkFFsMu88rHKzTEeaLYKdl-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکوچیچ سرمربی پرسپولیس شد/ایسنا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/666349" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff636b5bc9.mp4?token=MwGlOpD3mSzKLwBo46r5zEPvX95kSiYhq3PqMHupgdIZL45VeNvQ3Yh_u9z6-p4kR2EC2R2cShC8wNq0fnXj-C-IHmLXfA7CDRQ4FOSMeO93-7pfUB9CI1cjbqrL-QWxr02S5GGBNWf7ScCaCPybRdeLfc-N4fNF80Z0MOUdmmXYA0IEtlWPqPuECWHhFsEcUH-0bYXQrzlLbCBkG0E0KPCb3TGvWILtGLMagGJDJ4DPcC7pe87X6_jW_eqzSrGfZAmeiHDvmUrQ44pCoC7XnBdxOq4HAPJ3kwGWEZa3_fl-SiOsynPBHKpMR-1Lz5iG4koBaBHjMDyOOmoW5TZE0QNadmbqKXm9Slx_L02nvLX_EMm2tR2hXjSQ_lyQ83B1QANi9o_tcUci4GVLMYlgm4agknglMbBvasJaM7QWR309SuGTKPZiQimLMRT9N_xG3n6UYIw20Z1r1072XiCb3q4Ig65YoT9-u1_6sb_1R4lnIl5P0Qw_H9yxzt4TjTzFlTusFhRNhM0ogOJec8qWRSI-TlYbjI3a-mLNvaDk6RvIdpkmbPWdQ4mM0HHkXaD6oUmJBSFhWFKRlJ20iQrWsV6MjihcllGjgCh7LCCft-Vy8scwCLWEVHHIlU2jf3ga_kFGLctlXdIMlXTfH69GD6kJNRZpjASp8KMi4LwvapM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff636b5bc9.mp4?token=MwGlOpD3mSzKLwBo46r5zEPvX95kSiYhq3PqMHupgdIZL45VeNvQ3Yh_u9z6-p4kR2EC2R2cShC8wNq0fnXj-C-IHmLXfA7CDRQ4FOSMeO93-7pfUB9CI1cjbqrL-QWxr02S5GGBNWf7ScCaCPybRdeLfc-N4fNF80Z0MOUdmmXYA0IEtlWPqPuECWHhFsEcUH-0bYXQrzlLbCBkG0E0KPCb3TGvWILtGLMagGJDJ4DPcC7pe87X6_jW_eqzSrGfZAmeiHDvmUrQ44pCoC7XnBdxOq4HAPJ3kwGWEZa3_fl-SiOsynPBHKpMR-1Lz5iG4koBaBHjMDyOOmoW5TZE0QNadmbqKXm9Slx_L02nvLX_EMm2tR2hXjSQ_lyQ83B1QANi9o_tcUci4GVLMYlgm4agknglMbBvasJaM7QWR309SuGTKPZiQimLMRT9N_xG3n6UYIw20Z1r1072XiCb3q4Ig65YoT9-u1_6sb_1R4lnIl5P0Qw_H9yxzt4TjTzFlTusFhRNhM0ogOJec8qWRSI-TlYbjI3a-mLNvaDk6RvIdpkmbPWdQ4mM0HHkXaD6oUmJBSFhWFKRlJ20iQrWsV6MjihcllGjgCh7LCCft-Vy8scwCLWEVHHIlU2jf3ga_kFGLctlXdIMlXTfH69GD6kJNRZpjASp8KMi4LwvapM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از مردمی که در آخرین وداع می‌گویند: «امیدواریم روزی برسد که انتقام خون رهبر گرفته شود؛ آقاجان، شما که همیشه اینجایی، ما را دعا کنید تا در راه شما بمانیم.»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/666348" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nudd4gjSWk8-VB22EHQ_uB-ahzyL95_ejWy4vI9xMXW1vS0uhvNkgYA6FNpKvljS-NUYLEwwUPhTrgkM41-akaFxE9WIG3Wn0h4VwOCXH9V5YdjX5pt8YG5oa5up8oE10EHuE925HUVu-KIxRzUqhCS1Gbm_vOGLfsEsk6VI28NOandBsj_t-SsIhJ6klvhjtCudCOFUpUadCTylK303surR5II1w-mIhzyzZeffTEbscxo1KUoTZHhjPdcr5Ps_z5SLz0rXXbEUuyEh5uHs4Wb1lm9Jl65ORf4qsufPSfFU5OWMt4qYBqPYJuJV-O0Yc7IkRvbd6MXkDndNfWYdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌ادبی سخنگوی کاخ سفید: جوانان معترض آمریکا را به ایران بفرستید!
🔹
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، با اظهارنظری جنجالی در فاکس نیوز پیشنهاد کرد جوانان آمریکایی که از تورم و هزینه‌های زندگی گلایه دارند، برای قدردانی از شرایط کشورشان، به ایران یا کوبا فرستاده شوند.
🔹
این اظهارات در پاسخ به پیشنهاد جسی واترز، مجری برنامه، مبنی بر اعزام جوانان بدرفتار به ارتش مطرح شد. ویدیوی این مصاحبه به سرعت در شبکه‌های اجتماعی موجی از واکنش‌های تند را برانگیخت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/666347" target="_blank">📅 13:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuZhf_r8boEk9TeAjyszp-QHGGbx9ZizkKiTn0sIGRQrBES_eeE3-Iu2kn7s6U0Ml3WdcGOIJ_9Zt08g8y741qnACn8TKF64cvWh13kFSJw3NJ1ar1l1yfpACCmCRQDJ7TBNuwtNymFZjq6PPDV7smtWLQpfacwnC14pMDp6U90y1C7AQnRjq3d7Zkd-kwC5K9Yl6Bi8Lh-QH8LpJi-o-Ab5cZjdrF-FkbIKEQJIFEjrIp1-ABwPxO-ooQkiDVHCg_UhUr_fvtwNn0SjCjr9urcsLAaVYKrmi40yF2atTdMYGcv35WtJpsnlGn31whu--_yYSFvQCgQJYwXsVBNvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSSRwaOSB1Jrq7hodIftju9DipowbvA1FvGw2aA0QgZ9PqspuZdFyHNNkQuGCoDclN7B4e1zid1wXuhncvzpLF6W_Zq1i971IgFcKRIzCC_OUzx5L8gh9fvcZ3p4StGRTsBNvbuKKpMEPjTlyTpDTCda2AbNHm_rowHUdOMPPjeEz101VTuPG1er0Pu33el_lWV-EKXNK_70-ZbTUoNdf6ZYhrhRXNlcgXxFejJB4LOVIlY-FB897rd_tw0ds2jKVvLdwyx0kWucTD6JD4rsYCpIgtsW2i7sPjhHwtZ2zJI3vUsD2THEiRKafKoRj-vSXnimsVOecU7QUALLh76xNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان  شانس‌ها در سایت پلی‌مارکت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/666345" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWnN3seEWewzXjTPo5AdzGNSWz5UN8MjFW7mNK6QzR37BF0HhuUEzdHmW_6adTZnvAnXj_eFD4uLXlPcdSbXNJ882mVDQu9Kl7-_0c22cwy0OEBqh3j7mVCiN2NC8V6XkXE5ZZlQmmIIBZaxgHmprAB-AJqPxI_CQ55jVYvcji2xAo0abFz4HeEXJ-_2iBqi8P-c1jzo6gc6PZlDQKqGHxLtZv2hdzhB79LgWn0wLj8jsrdC82a8QrDTTU8Oeg2w76fhYkNrKgDEamdDahZOcqszS04vKZsmerB4Ahb9iFjmb4y9b9167yUcOtQRiQpDpNP5wwiHRBooUXyt5k-P8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماز بر پیکر رهبر شهید توسط کدام یکی از مراجع تقلید اقامه خواهد شد؟
🔹
نماز در تهران توسط آیت‌الله سبحانی
🔹
نماز در قم توسط آیت‌الله مکارم شیرازی
🔹
نماز در مشهد توسط آیت‌الله نوری همدانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666344" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdb30a626.mp4?token=qBfu1HVthh_3_wquBRfSVUMPV9arHmFPduYLlWDlO4X6eFXKUGIj_-gXnNXmyl64enL1zHthIjgH6Fa8ss4zkt0SRXzXWGBK7TYQzD6QxlCU2Yiluc2g8zLeGwBSH6oqZQ2gnqy9Id9SFp8fWpfHtoRPxKIDDB6sQKQbyblYaOIC67kd_Dlj6v_1X0Zdly5mTMrG_AntLemW0y8e2k1OhNasR31m7BX5SHspiBXt9Me-4jLBIC-arunxvwLj4cMmSoATTfp5JzHYzdJxE-88baDdbCx1n6gc8YaJsrhW-oGWd8wnX_wMndpIenbxIW9FAkIs0G8gXkE3jbylsVYSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdb30a626.mp4?token=qBfu1HVthh_3_wquBRfSVUMPV9arHmFPduYLlWDlO4X6eFXKUGIj_-gXnNXmyl64enL1zHthIjgH6Fa8ss4zkt0SRXzXWGBK7TYQzD6QxlCU2Yiluc2g8zLeGwBSH6oqZQ2gnqy9Id9SFp8fWpfHtoRPxKIDDB6sQKQbyblYaOIC67kd_Dlj6v_1X0Zdly5mTMrG_AntLemW0y8e2k1OhNasR31m7BX5SHspiBXt9Me-4jLBIC-arunxvwLj4cMmSoATTfp5JzHYzdJxE-88baDdbCx1n6gc8YaJsrhW-oGWd8wnX_wMndpIenbxIW9FAkIs0G8gXkE3jbylsVYSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت دیدنی یکی از بازیکنان فوتبال ساحلی ایران
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/666343" target="_blank">📅 13:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUo79yF8-A8ZYzMLxmRtfBb97zkYPMacOjd6wtrJKxTu1EPA_6DJ6RTRs1AtM_q9QF072bVriYQNVA3FG9HNmRpBpK7LDIK63wua7mVQu5nI-jw1a4JdwZdoSleqqoxLt6yL8xsN7tN3653JPkxuKdKls6rqWngt1ZFL4SXuUuA5ME04nmqYvi8yTGZAOdjM5x65grkD87-uySWKConi_J0WqivtcBN_Uc3P53WKOIP92o4NyrVfK44N-tqHh-o_i3XqhZvNwVS2jq7A7yBjKRp-mGoFLYsWFu8dJDxSXrYsPYXFmUK-hp_em5o6rF-IHF9rtGStlO1Td0jm8TkE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPRPDEv-VcCafpyR0lV3S8q949fcoTicDNQfsz2BhpvzQx9F-bg_WE8RmAhGeH4fIpTvgUZzirWuvkS9OZ3vcxeKvWQv1C1DaJVwMxo0V8XzTrfiefbqwgwxC4VBmlWnpRB8Kbabsf2KP3CnGIlEfBBgMpSY-idL72rSjR0sHI2DNkFAIIbUsBqEefFaNhSLjBXoOpPplslDCpVUIJxXA4cD1XfygxpsFwtg23txA1r2R06V8ugLij8rK4UseSErsCTDFC6ZWxDOwYRqo5RsSkPJ2S11wnmyNPhzcFicXYn4KHZfdAshkQ-wJp7xZrLNTiN7sLeNIGKfikMMx_FhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPcNGmAEPZc1CAP_i6Q7OnWYAoZRDdQ61GyTlj3jYY8hkt31bYpefjZJHHTdB3LLp_fiKtX6ncv_ecyOL8DuwKIeKV3EJY2erZMbPmL5UPHfGJ1lGI0NXOqZ1LqD8Gh8mkZ-uIyiPpcZnWmpGMdPMg6--AqWjcDEMd0tu1PdSvWdJvUyCx6a93wfFgfBJxdRmymkOLaFDS7grcnN40PchsV-KdOVkuY9nbHHM0x31b5KclZ57hHKJ2zica4rF4Pk04zSnihWM0qH7LintNVkGZAQs375VhIKeWjA5bOZpomHyRFpoJI_k0NBTq8F9GNNLmkhbe7p2_8W8No5w79i-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری دیگر از مراسم امروز مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/666340" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Fl5aJua_JdGIceUUYNXeBLHlSGm6PdryOa149f9d7oyUvL-K4USrS6ZrWtg3iUxOXbg_L5ynnBtEhCnZGNrWDEB2uSd0UWZiI8tBZKIwwbzjWQcyozVlrEzPg5PENkqByuCfABujdUaoacLrzXtZfte9JuvLGprKH1ckb1m6YAeck1KNWXP3D7iIxL5OrneD6ckaE7spWltQgq-EZU2a3i3Mbo7WUyFSbSOEGOJbI6NzNOPDSjQ4Vmhh_l8dJ8IJHH3pkw7Uwal_4qAmQdwBeXWsYoaK6QeLU3kt1C5vwJsJFPMedZXWHkf87tgxWJ7QpagsNJMglxpnO--v2OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدودف: ایران سلاحی قدرتمندتر از تنگه هرمز در اختیار دارد
معاون شورای امنیت روسیه:
🔹
تفاهم‌نامه حاصل شده بین ایران و آمریکا، مبنای ادامه مذاکرات خواهد بود و مذاکره همواره بهتر از مذاکره نکردن است، اما این گفت‌وگوها باید در نهایت به نتیجه‌ای برسند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/666339" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3c7ae948.mp4?token=ME6DROSaYRCJoek7GsgoYQI1PkTO6BEtfwq1dYEmycMW75vf3ZMP_XgZfqHuLeqQwavRFbOapGZSpgAtDRmWDDY_rOsErgTIAiUA1LFdynYp_X-ALB3boj2u1_rNXmTFySBCH-MYysoDy_HvvfFblTTb3ZXy5l2JIAPQSdYpUEW30fioOhcEFg2VPQXlvJzmBgVNDVSQJMeyuHKfpPGWPORvuxeL-2a9Ck7slTcAt-ldXjadnQn_8IW-VlZoarxnL3LAEQzrytUsBlqWb8qaExvmbitmWeGWg0bWq_9gS-32sHFjanwnlhOsGCuuvM46240kQXeaxmFnXD_CregzJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3c7ae948.mp4?token=ME6DROSaYRCJoek7GsgoYQI1PkTO6BEtfwq1dYEmycMW75vf3ZMP_XgZfqHuLeqQwavRFbOapGZSpgAtDRmWDDY_rOsErgTIAiUA1LFdynYp_X-ALB3boj2u1_rNXmTFySBCH-MYysoDy_HvvfFblTTb3ZXy5l2JIAPQSdYpUEW30fioOhcEFg2VPQXlvJzmBgVNDVSQJMeyuHKfpPGWPORvuxeL-2a9Ck7slTcAt-ldXjadnQn_8IW-VlZoarxnL3LAEQzrytUsBlqWb8qaExvmbitmWeGWg0bWq_9gS-32sHFjanwnlhOsGCuuvM46240kQXeaxmFnXD_CregzJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمادگی شیعیان عراقی جهت تشییع میلیونی قائد شهید امت در عراق
هر پرچم تیری است بر پیکر استکبار امریکایی
قوموا لله …
🇮🇷
🇮🇶
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/666338" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac0aTm3cZLTEc0U-2J9nMsj_lVpdKrAqN76VVFzqBl1qd8AafXfqpWTz0ybvNKLjYP9pKQzFuS0DOe3hr9LgmxwH2Pg0w4f8FXwStZeXOPsfzRYa0kXbEhMb4MxNkU6d_ptyiplk0uPCWwUB4HnXXr-vYW9ekmb0XowpjsvpxaWvkeGDhg6p56Oe1ASc4XuA-oREYffTPo0IEXxM-g93JM2W1bbKNaZWI0Zrikm44juCK8Pzf-Zd6_ZE5tkQmpsvCIoMVUq58qXF8oHmdVYKJcMdTfri8OyGkBpH8VQplCR4MLUb0nua-upBIMeCd7zYJtX7SNcYuw_Eksy590Kv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان سبز بورس در سایه خروج ۴ همت سرمایه خرد
🔹
هفته گذشته شاخص کل  بورس تهران با ثبت بازدهی مثبت ۵ درصدی در سطح ۵ میلیون و ۱۸۷ هزار واحد ایستاد.
🔹
شاخص هم‌وزن عملکرد بهتری داشت و با رشد ۱۷ درصدی به یک میلیون و ۳۶۱ هزار واحد رسید.
🔹
با وجود سبزپوشی بازار، خروج سرمایه سهامداران خرد برای دومین هفته متوالی ادامه یافت و حدود ۴ هزار میلیارد تومان پول حقیقی از بازار خارج شد.
🔹
بیشترین خروج نقدینگی از گروه‌های بانکی، صندوق‌های سهامی و فلزات اساسی بود؛ در مقابل، هلدینگ‌ها و دارویی‌ها مقصد اصلی ورود سرمایه حقیقی شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/666337" target="_blank">📅 13:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_vHr-2XESGuR1QU8JnDhYbMEtM3NDeANB2wgdyJ8KqNmYKwbIIPKaPMnUYeSW3T4H1g3cw51XRY9YyW4_irRYMXglSoHLtiNpdEB0fQbf9rfaJ1KTKiG4MTy4YaIrRxu00FM7_eSW1pxHL5mIAZ_YCckfNHq_-F77Qt5mqo1cLwkZBVl0fgnfQ7pj6otaWDGsFJ-ADqZ1QH14fBhSlTpx03gX11l2GUUickpJoJ144ONoqFJE9y44CBVVWv24Z49e1KlEqjhB-oR922JFaeL2G9Vc5ZAcxC6VLVFXBM24_IwYA_MT8rBwIcGckEzKf2zXPfEYXmG_cmbCNzyd3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه‌های سازمان راهداری و حمل و نقل جاده‌ای به عزاداران مراسم تشییع قائد شهید امت
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/666336" target="_blank">📅 13:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRJWczQBUU23xAQ8Fl5R-i8DFcHeh7YexpRdN0jm5ie43dMmkJ4C3XIOtV8XZwv1O4Zmr8zlidb3XJkqEK_4vdOL_jXULx5BFYv4rYXahoeoCMFk9nvZIfeRqWQRwow5I7fDE8DCHfrODGDOCh5qBcggnt-zrdSDpB1bcHxnF8CbTPkfpcj8sdRBN4_LFl7WAi1AYhw7v64KgWMr1QG_SH1q-yFcsK2EH9XKvuV_-aW--RV56Ov22Kp9_hsctB_IlCm9TgUyVKd_Wo7lAmXaT1lXj8U8gaGkULigEvuPOE7cX73ZuU3sqPa3bMhsbHKhzuazqyz9t6k4g4WKKLe8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مطالبه انتقام «Revenge» در مراسم روز وداع
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/666335" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ddfb277b.mp4?token=LoOncuZULH5-zy7ppVDADNEimFE9Ji9ETr46bDbM3H6_ipOwEhdMNX8RKntoxe9OwJWrwsFtcyfMqTh0MJ5p4Oiz1khihOlJFXqMv7t2PEeD-uJSQ43FPGrpV1X7QoV_XYRAPOtbC-5kg3i6fWyrAQhVhmnhDvGhj9wZlgjwe-qa4u90MZKkg133Gj0-VAF9FiuhNqy6JQhUuXMjPewjYbfPbyE1TXrtWh0EX8OJmhQwMaafUkaWhtuyt9kdD3fzvV2B2wPiR0piZSTK5EGUVdUeZrvxYAUTWMsQEUWfjOhWn3XBK4lU6dzC6s2PjcSVvhxAiVnoscl0hi0tJEYsviqV91CPvYk28PGwp7ZZw959bS1hO0LSLQcTm7AHwbjFzZruJ6blmkXYg_KE4XzfuDil9mlcIiv3aMS4hzGfPV5tvobBcr_CjLxT6FNGpH0_2uRlliOBm4ZU8DrxTWtUBEAK2Q3EfjN-TdTic3j9rLt0QPYaTJp8oIkN01sgcfaRRSd6fbHXlLeqMXuoxJvoE2ANWOv9KhIOcTQV_oUrJtw2Cb55fozGd6m4NIQEsHOj2bWZugnEpa5bOwjUhInowZayhbTul_RtKYRhXf7gPZviyZJajq_Kw1llioNJXGYmkVyD4NemVvkGrU-UhJT1UqW7xKC9G0eecrG19fO6npM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ddfb277b.mp4?token=LoOncuZULH5-zy7ppVDADNEimFE9Ji9ETr46bDbM3H6_ipOwEhdMNX8RKntoxe9OwJWrwsFtcyfMqTh0MJ5p4Oiz1khihOlJFXqMv7t2PEeD-uJSQ43FPGrpV1X7QoV_XYRAPOtbC-5kg3i6fWyrAQhVhmnhDvGhj9wZlgjwe-qa4u90MZKkg133Gj0-VAF9FiuhNqy6JQhUuXMjPewjYbfPbyE1TXrtWh0EX8OJmhQwMaafUkaWhtuyt9kdD3fzvV2B2wPiR0piZSTK5EGUVdUeZrvxYAUTWMsQEUWfjOhWn3XBK4lU6dzC6s2PjcSVvhxAiVnoscl0hi0tJEYsviqV91CPvYk28PGwp7ZZw959bS1hO0LSLQcTm7AHwbjFzZruJ6blmkXYg_KE4XzfuDil9mlcIiv3aMS4hzGfPV5tvobBcr_CjLxT6FNGpH0_2uRlliOBm4ZU8DrxTWtUBEAK2Q3EfjN-TdTic3j9rLt0QPYaTJp8oIkN01sgcfaRRSd6fbHXlLeqMXuoxJvoE2ANWOv9KhIOcTQV_oUrJtw2Cb55fozGd6m4NIQEsHOj2bWZugnEpa5bOwjUhInowZayhbTul_RtKYRhXf7gPZviyZJajq_Kw1llioNJXGYmkVyD4NemVvkGrU-UhJT1UqW7xKC9G0eecrG19fO6npM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره روحانی از رهبر شهید: رهبر شهید به دکتر شریعتی علاقه‌مند بود
🔹
رهبر شهید به من توصیه کرد «بینوایان» را بخوانم/ رهبر شهید یک متفکر اسلامی بود که در ابعاد مختلف فرهنگ اسلامی تسلط داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/666334" target="_blank">📅 13:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5419682d06.mp4?token=GvIaCEmVTstAd7EfG5uyAN0-md_4f2OK5FmnfFzhge9U_eYcD1-gTqd9nR2AZzjpjit4vo8CUNVhmPARFo2wBBX4Ene-xyWDYrDLiFhe-PJ5nyAEkrMz2eKkUnRBcIrOfJchrKyy-9lFQkcBKzd58GLbUQamJqrdOeTaauY8oXGlM2H53hjKyBSZbKR3-MPH_tC8mUO2vh3Hz0XZ778BPyfFF0X4UgXF45HT-1LIcrZDWQ8cDVklbvCPehDVjrpUd1N115cxNQdJ0kYeFEyHx88BzZ3cnZUYndg2TJR3mGUGg_MO-JH9Bwld0BvWjGlLlKWaDLshRY3Hy5lkch8lIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5419682d06.mp4?token=GvIaCEmVTstAd7EfG5uyAN0-md_4f2OK5FmnfFzhge9U_eYcD1-gTqd9nR2AZzjpjit4vo8CUNVhmPARFo2wBBX4Ene-xyWDYrDLiFhe-PJ5nyAEkrMz2eKkUnRBcIrOfJchrKyy-9lFQkcBKzd58GLbUQamJqrdOeTaauY8oXGlM2H53hjKyBSZbKR3-MPH_tC8mUO2vh3Hz0XZ778BPyfFF0X4UgXF45HT-1LIcrZDWQ8cDVklbvCPehDVjrpUd1N115cxNQdJ0kYeFEyHx88BzZ3cnZUYndg2TJR3mGUGg_MO-JH9Bwld0BvWjGlLlKWaDLshRY3Hy5lkch8lIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مربی مصر بعد از پیروزی پرچم فلسطین رو برافراشت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/666333" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دستگیری ۶ نفر مرتبط با شبکه‌های معاند در پردیس؛ رصد اطلاعاتی منجر به شناسایی متهمان شد
سپاه حضرت سیدالشهدا(ع) استان تهران:
🔹
۶ نفر در شهرستان پردیس به اتهام ارتباط با شبکه‌های معاند و ارسال محتوا به آن‌ها شناسایی و دستگیر شدند. بنابراین اعلام، این افراد همچنین به تلاش برای تشویش افکار عمومی متهم شده‌اند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/666332" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
دانشجوی آمریکایی در اسرائیل با ۱۴۰۰ دلار برای ایران جاسوسی کرد
🔹
دادستانی اسرائیل، الی لاون، شهروند ۲۱ ساله آمریکا و دانشجوی مدرسه علمیه ارتدکس در قدس اشغالی را به جاسوسی برای ایران متهم کرد.
🔹
او در ازای دریافت ۱۴۰۰ دلار ارز دیجیتال، برای مأموران اطلاعاتی ایران اقدام به تهیه عکس و فیلم از مواضع حساس در اسرائیل کرده است.
🔹
بر اساس کیفرخواست، لاون در سفرش به آمریکا (نوامبر ۲۰۲۵) به یک آگهی مشکوک در تلگرام پاسخ داده و یک ماه بعد، پس از بازگشت به اسرائیل، توسط یک مأمور خارجی هدایت شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/666331" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWgmuSjKwt44z8mKtuuzRqLlofHWGQ-glT61RwVWh0ZjEob6kmPNeU8UwDpJzWbIQVZusfmtBeBlx3faegpfT4mr--2p225ugYTOnjEyCJQposOyd026gpFKSN_T_xJOqwNBrmyN2xJ5pk016Ae_tESDbwnzG0HFsdbFD7qU6GOkNaWkAuQ1QNIb1pAlps8lfoNcK4JkSK0nUzCgYleWWwl375Cb1yLLCXpDajHEa6nmP_AuO_aYvTHjmAyBMCQ6Wbaaj5l-W7-sdZKREFLd0VQXsshCf-zsxHJiI9MYOlgBMxEbllAlgkqAoxrwiAmwzhF0riujsNbLQ6xaAKmBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انتقادات بی پرده از مسئولان و افشاگری پرونده های خط قرمزی
⛔️
🔞
این صفحه دیدت رو عوض می کنه، در آپارات بدون سانسور دنبالش کن
❌
https://www.aparat.com/MADAAR_TV
https://www.aparat.com/MADAAR_TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/666330" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666329">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4417a5e8b.mp4?token=Lccr1tvcQ94KX9cnci4nVpNYFJUWwgr9R54yjUp-9ZFVD2x5xc-IfzEn1gHN-L2874COKPv1_9p1U8J82k2luhqUdznTDjd0xGvBpg5bOzOmluPvBeBFguauvP4SV4u27Cq5uf290Dz58FQDxGWZqDsmm8x_oTGhbLtufY_SOehBpVpmuOl2jBhSiBA5JqoSBajHtZXn6t5vtuPrCQKxwZESO05jVTkDgGjxAvmF6p3c5u2xD-p6rexr4XmlXtMxXHN-xgPJh4r_3ll55jDyjJvUF8tJvOMYdizmmV3RjAEobt_VIk2CSBU-pW_4OSVnGvAqerT3ITdXfDD5O3C2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4417a5e8b.mp4?token=Lccr1tvcQ94KX9cnci4nVpNYFJUWwgr9R54yjUp-9ZFVD2x5xc-IfzEn1gHN-L2874COKPv1_9p1U8J82k2luhqUdznTDjd0xGvBpg5bOzOmluPvBeBFguauvP4SV4u27Cq5uf290Dz58FQDxGWZqDsmm8x_oTGhbLtufY_SOehBpVpmuOl2jBhSiBA5JqoSBajHtZXn6t5vtuPrCQKxwZESO05jVTkDgGjxAvmF6p3c5u2xD-p6rexr4XmlXtMxXHN-xgPJh4r_3ll55jDyjJvUF8tJvOMYdizmmV3RjAEobt_VIk2CSBU-pW_4OSVnGvAqerT3ITdXfDD5O3C2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در تأسیسات نفتی سن‌پترزبورگ پس از حمله پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/666329" target="_blank">📅 12:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666328">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a2f0a68f.mp4?token=N8Z9pKbzL_6PHZ5mx1sb5njWdZBW15dMW4WdK52f9HzC7XKWC4Tj-YZKvdzbuadXhUYnQ_eRtbhw4vDvBL2MmllbvVHVY1sRvvALp_IQ3nbaBjz6CF_vp5dumxI1NjeLdAboNnRvaxBW-RbsKD71daxSb9JQjb1taJeoT_RiOAu-VuxiDGA-YktO7VYf3m5rcXiofE9fOMhAbVW5nOss6NV5I1VNNM_WqndZk4MWmQJIhSOA9SHeFeYmX-Zennp5kRtakWs5xOhGHZRqu9_wKOFWORcxqzKiOgzsYE5EUCxiF-fuw6Fcl_ct65-v0APNN7WzR1cA3TDcVwyS4JtfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a2f0a68f.mp4?token=N8Z9pKbzL_6PHZ5mx1sb5njWdZBW15dMW4WdK52f9HzC7XKWC4Tj-YZKvdzbuadXhUYnQ_eRtbhw4vDvBL2MmllbvVHVY1sRvvALp_IQ3nbaBjz6CF_vp5dumxI1NjeLdAboNnRvaxBW-RbsKD71daxSb9JQjb1taJeoT_RiOAu-VuxiDGA-YktO7VYf3m5rcXiofE9fOMhAbVW5nOss6NV5I1VNNM_WqndZk4MWmQJIhSOA9SHeFeYmX-Zennp5kRtakWs5xOhGHZRqu9_wKOFWORcxqzKiOgzsYE5EUCxiF-fuw6Fcl_ct65-v0APNN7WzR1cA3TDcVwyS4JtfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای محل استقرار خبرنگاران در مصلی تهران/بیش از هزار خبرنگار داخلی و خارجی در حال پوشش مراسم وداع مردم ایران با رهبر شهیدشان هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666328" target="_blank">📅 12:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I11Fxqv3J0tPF-93QBxsXdqjv4b5iMjLmzxW-hkrDl4qkK0D_AESohBpY9PfUvLtY3tLjlbKmG8QZI_xfurBmN8Geg2vaIQb_lpnyyhmio62yqVs9Mcj9WJFAGpsP2gZusD0__CPmLIx_QotBWhEEzzxWgb5l5lhT9pbjsJ9iW2DSOjRekSgTsLbcKJp5sz9pEruWG8SmPIJVnCF0kmp2lAvEz6zv7Jaw3jzdC2tpA2lzS_BoEGhm2crw8QiImh98iIJt3B0I9jvV4_vTwcuAQq_XJs6Usniq6FwwHYNe7FGUHXEQ97nJ5TDWDA4Sr9_oL884jIoYS-K3DDXTqmvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۳ تیر ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
نوسان مثبت قیمت‌ها در بازار امروز، سکه بهار آزادی را به مرز ۱۷۲ میلیون تومان نزدیک کرد و هر گرم طلای ۱۸ عیار را در کانال ۱۷ میلیون و ۴۶۲ هزار تومان قرار داد.
🔹
همزمان با معامله دلار آزاد در سطح ۱۷۵ هزار و ۴۰۰ تومان، در بازار مسکوکات ربع‌سکه به ۵۲ میلیون و ۸۶۰ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666327" target="_blank">📅 12:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0QX65DikJxA-ie23Dz1dBtLDHt8eSdinYzTaqnrgLIgc4Q8F4tVrGqoFhvAF56kvfPqLAtaEEAewTHackkLu5zg-xcsB6WQA2ksUtHKWPoVGEDGxTQA6lVezRu6dMHIKZuvt1nJVLcqypJli2uLk3tWX9p_11MimZNo7nFP-C1Kw96AsJw6fpYzV10-px4uQQhhcFFnrJ3ZvE6gb6YgeB5iLp_F5OagGNXGgbu9XNjlaNoyOuj3d0oV3zlhkigM2Y_H4iZxSh_0GR0hulRFENaH4lQc4-WWT827vJMCSFNB0IZApAnmBaq3er3NuWEwBvVmij-9HbUmr9u6hvfAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنها این کوچولو را با خونسردی به قتل رساندند
«الیویر ریمل»مدیر اندیشکده‌ی فرانسوی با انتشار عکس تابوت کوچک نوه‌ی رهبر شهید انقلاب نوشت:
🔹
آنها این کوچولو را با خونسردی به قتل رساندند - چه کار بدتری در این دنیا می‌توان انجام داد؟ هیچ.
🔹
آنها بهای بسیار سنگینی برای جنایات خود خواهند پرداخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/666326" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWvkEva64hp5mH-snW9cilLZvyX5a_6ARTjDoFDwA1FkAnO-q9T2kw4FU2jPgdZfCuEHjTRTmHbi22jenI4umAyTqusUIPEW2ImTuwvruZaO84TJLd7CTvRbA1WmD4k2LKdO2Wird-stOMjfULBPUYcWUn05CvxzJi64_jRYWce6R5YG9_fiEcj9clv3yhgoT_HVAUDIj3dek3pyOaLwzO_7gNgB69kVlqJ7zIbUQgsHBp7YuQrr_wxi2BZDAbyzXopVY_RQGmnr2I4pBfjoHH57W-UQTs_b66wAsaaq1PgcFZ3S58yM7Pk_a7914yH3I6UJsHptfVykAKFKXEDWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwFZFzuhA2lWdkt6Bwfw535o4bLyQYK2Z9mkHJEESeOCsUKZjbQKt28ljH0uzj6ub9qrw4ys_3BCoJRHpy1Em5NHRLCpdIuUV8vWkYUvVr5W8uPw58O-0ZqjdvQ6isD82o5YVDNXmfEhKo_MFs9NzxHZHZDeo7MgwimBYeyYagNrUeqOHaCGCQdYvv-XdlgT-DlQq5VFPQPyFpDIdv6W0gQ7a8DIwerCILGtB086u5XbYkG0uGYSeZt0-MGjLo4sYHCyblE8FbM14YsBrVb8Az_XQSv8xXsAzNyQAjZUTeF84l0XcQdIhZ31TT4xHn4b8hGYwx9SUsg94O6PHyZCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnXOwu8IjDL2hIhpYfX0wikZfaRodAF7pKhLRIe7BFvjkTskWcqfIv3WNUpAnHQsMCxAxv1-iQOhcSitu2vStASclhOV3Nn9tBrCtp0JmF0e636kdrvtx_c6WHvTOAu5CKLnzRTL_LLCmV9j39lOG4FgHwr1pVLHYwFJeWUiGugFAKVYP1ANAF2ZJizvUeYZmqkOSyzkG1CHByxZG7-VNmKShBrIi8N019_lRrB8b4S0PrIkuoHJJh0V5Wz1zafLlZK69Ic-OQAtSmTYKDrKtGRsVI38jgZq4YEF0u483c3ImG6iKKGzak82medOQBe3Ff6o0yipVnrXWnHqGMxSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDw-gGInctz_xQMm2HabrWSTsRflZjqvE-D8132t0B0fbNydCNpuI2ZACZoT7lCm2wqdP4gTq55-yBT7Gkir-ly-hDjU384jBgflJnBQBAW3htgZsE-HmTnyXRTH6SBjURmAbEWNxCzq85-e3QQ1PCQbSW4GosJIPyazawA2k3T2xnjcYoKXxz7jK5QFHNP-tfZ8FnZ7_oc1nLA2UvGdyUgXG8xkRNQKksOGbngJmqtU4dWK4g9ihvwBurhNWd6dkbORMtICYPa2vLRU3JGGgdtPyo-CQoQWO_2XM5PXFuD7o5faEEplHgOZK1KMKUdTseLm1wDnnZ4Oil5uzVU8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqwyclzPIQIN4GkqB4pMlDmP4ziRY69Afmly3chaKKsK03-NI58CQSWC3n5kelxcxgT18UwGX7-sLlP0cVK9AJBpaRobLIZMMNMd9HlLXY0p4CKwYGu_nVbo3w-kjw9aMvglNWrqV18w3K3MftpIpSpqE6v7oZDgfv4VaUT7lWDvTOsZkZPC-fyHjNSr2et-DDu8KkrD5LG_0fA0B9hiRdXAzm8k-e66IW1aCsDabslMuee2qnP4RWNEOEW870UlH1dkpmMCocfcwEhRqmZd6Eg0EdN4iaJQR4TCzZhZpIw-_N1T_w9I5Cay9nv0TghHUIrp1ecsrEOTJ5d3quvZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLHjpjb_-jjYPHCU3OfK8SDOTsgg0zEL3Noe7w2Ff7Z3kmIbVhgNw69mM_liPahLWzyaLbp9PNL36LqfgUIedtu_-DOtdPVwM3OZWqwjaUrELPGx-nAMpuGbO5_SSSAe2Hh44mYFOheee8bI-7maZexLhI5417vCLmrBKnlghcnzxytHgpraZqc4EEloln1dRLHBCnT0RsxoglukyAyHD3_PAB1zD-EOsKOM_ta35G_Pvp8VcOOMKbFvA_F8U5L3YwLrExLuqzPwIcJKMAItkP1N9F_6GhFh3a-5hpFleP3dPZh4TTtScmWPfA4slk7g1CChz7cSk45y-tWP5sJmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUKgAfPqIPaS5KpL5iZiw0wdGESWldMDwTtLLse5ghUpu1tVzW18YX1ecDXQ-uVb0ez56Dl_vNSjx54uTgR_s6M3UgmlbFbS3V2BLOen-AtQM8bGsB2atsPxc0epJMC3pZmfpivOpsXbsuRR48YEhPvU-x3BjBf0erntm5LBGLWXzrHnAy0qXzvu5xwvZT5UvAf3-W3BCh6bc7b9DBKCDKpuGZj6jluyvqlvsztZRjWJ4ZwQwSi7NFmKSs4I0CrnOgFrPdGXB5iknScVCk2a7JnGwpbmQBqXVER1Q_yNNGsOOq0arO9r8ljaMpWZHNuy_souByQ5GYal-TjDuCGbqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دلدادگی و وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/666318" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVIJoFoDx5i8xpnHrlEQvMFkjxMbZfFdQxYqOM7R-vo7WeyCl5prfgFrCimFIC1Ud-6QxJJYycHl6vc9isoQ3OGMqAFiYMoFB2v-fXasSlRaHZQJXlEre5a1yoxdy1G-NkCkeqWBNPNaCDFiFe8bITU6fnhGLuiroU1qIZg1QtJ32hy8yiaIm0_omhysoRDu0L6WtEAbQKE2KTlNF1NEuXZMD5adwy7y1y7qnnZ22bL6Ce2hF6fMWHh7HiZx5t2VcwU_6j_pnKLY2KoB8_uW1flz8QKt6HNARjKkAkKTQO3rwOA3jH7-gVFbwKVhhhkORedWVEtPBJMy8f1UM4StdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم ۶ تا کشور داخل پرچم نروژ هست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/666316" target="_blank">📅 12:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-sOpAAFOd07ZA5qqVwJCBpIN3ZYHuxxWTD-qeTXOfGdkWY_azIq8AbZVHrxqJcww91tO40bBsXbJQHc2mOclDY0ERD-TIajSxsDnzw4C9xTcXLYlgiVRwFZFWtCikxU8vAJ4v7aPlHLo5vcDE-5UZ3iqO52ovg6fMSWWJcylNmbxardFIcktDa2iQvMIDyUySK9mtIZJ_vSARHjUKkVzvsKdBTcOCdW8ISkGns8kDKFrb4tIuh1YZE67sWfP_hfpRkBZ6rAiMk9JTnZS4ARQMgvxc6poZ7NaZKORgMc0DFNF5EUSaZpt9bygL5SKUkhHyAL_PjJfjmxvnrAXU-f7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری برگزار می‌کند
کارگاه فشرده «عکاسی با موبایل»
◾️
تصاویر ارسالی شرکت‌کنندگان، در صورت برخورداری از کیفیت و استانداردهای لازم، در رسانه‌های خبرفوری منتشر خواهد شد.
#بدرقه_یار
ثبت نام از طریق لینک زیر
👇
https://survey.porsline.ir/s/3PHWMjxm
@Badragheyar</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/666315" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce35e147dd.mp4?token=S7i-gSWzFPocTr1j3HMAGUjABBtMIETtwb6raRNbF6vNEgnoENlwW9ViY8710OvfosaPQt84hovf1bfZOZDSelNMSoOvFy5HJXvALIsA62kSPwP5QaUcJyKcSkzwFmruolcS9tc86gCnvuzWU9WrWUHqNOLCQyXFf8pamLE7AUdABm02jjcPCbzH7IynCeFXXpuSkaub3mKqsIibrKNK_2_Ckw1mW1aFxd1qeLgfv2yohT3K5PBdI1lDqC6ZiYTWOH1L0_2S94lonEDSBi47zrBsiBCtEB40oTLNV9bnTCKdwVc1JYMHqKxLBZQ42SbtnIOsKgwb2KMeWBH5dPtQ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce35e147dd.mp4?token=S7i-gSWzFPocTr1j3HMAGUjABBtMIETtwb6raRNbF6vNEgnoENlwW9ViY8710OvfosaPQt84hovf1bfZOZDSelNMSoOvFy5HJXvALIsA62kSPwP5QaUcJyKcSkzwFmruolcS9tc86gCnvuzWU9WrWUHqNOLCQyXFf8pamLE7AUdABm02jjcPCbzH7IynCeFXXpuSkaub3mKqsIibrKNK_2_Ckw1mW1aFxd1qeLgfv2yohT3K5PBdI1lDqC6ZiYTWOH1L0_2S94lonEDSBi47zrBsiBCtEB40oTLNV9bnTCKdwVc1JYMHqKxLBZQ42SbtnIOsKgwb2KMeWBH5dPtQ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موکب کودکان خردسال عراقی به مناسبت وداع با رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/666314" target="_blank">📅 12:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1h3ZSZWN6__Aj66ezg5nP1DUylcOks6fSqcd138CmXmdVm8W1ZfLxuUc2r8z0bU1V_w6dsYVbA_pfnJj05_n7NPnuUoiqhPTl4aLUdQWsp7NP2lWFnmODq9xeP2PqU8CJAdIaPHKps8mSGXAlsCH-x81Uerm2wZ90ufFCOO5KR7YpiT8DyXBbkIGQqkGwXUbjB-KRqECix5UFGBm3dZ0tmy0Uwne3qse_morpb-Z2OxaD6mAiytGABznI5nOb0rY2APItEcNgE8kLpk14EJpsnCtUlG9e6d6LsFJxNw-uaspeasLTJ0XFLmINjqfaNWpzcR3_NuoII1931si6r1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
️فرمانده نیروی دریایی سپاه: انتقام الهی از آمریکا و اسرائیل چندان دور نیست  دریادار پاسدار علی عظمایی:
🔹
اینجانب و همۀ رزمندگان دریادل نیروی دریایی سپاه و حافظین تنگه راهبردی هرمز با خدای خود عهد می بندیم که با پیروی از آرمان شهیدان، راه رهبر شهید امت را…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/666313" target="_blank">📅 12:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a9faeb26.mp4?token=AqqyBQK6VtRUG8dJQJu7v_7p9H_WeQjFVnZvm7al9Kdz1yO2_Jqd8yVoszZiQRKY63ZoWIvdp1f5rfZDSBWjSayKNqcEvBCU4sSXJ5iZHLEAGGFJtGP1JFV9QLqPvTor9BYxIV2PgRhDRAUJMfA0zE0xDgIYDg4QIY74Q4rKIwuAdu1WA8yLbgG5w0hQbM9D4XP79Y0G6IMReD5hNVesYBcS0kckColhMnhCYCfJp9Wehm90p_4KyLzq7E_4BGBSST0qflpxZCcc9wzpwTE1ETgMqgUKTE7SYbFr50Za62LAFQzmYr6sO6im1qxB4ifBAZIhq17rqRgf8WrYMgSfTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a9faeb26.mp4?token=AqqyBQK6VtRUG8dJQJu7v_7p9H_WeQjFVnZvm7al9Kdz1yO2_Jqd8yVoszZiQRKY63ZoWIvdp1f5rfZDSBWjSayKNqcEvBCU4sSXJ5iZHLEAGGFJtGP1JFV9QLqPvTor9BYxIV2PgRhDRAUJMfA0zE0xDgIYDg4QIY74Q4rKIwuAdu1WA8yLbgG5w0hQbM9D4XP79Y0G6IMReD5hNVesYBcS0kckColhMnhCYCfJp9Wehm90p_4KyLzq7E_4BGBSST0qflpxZCcc9wzpwTE1ETgMqgUKTE7SYbFr50Za62LAFQzmYr6sO6im1qxB4ifBAZIhq17rqRgf8WrYMgSfTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایستگاه مترو شهید بهشتی/عزاداران پدر امت به سمت مصلی درحال حرکت هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/666312" target="_blank">📅 12:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e045f6d4.mp4?token=Cc5A9pr7jWMzxXQ39FNiYtJgrxlYbnp6CME2AZODRoFL_m1_JGT9VRb9aemzch05l5pTqeoldeKY7OSSBbFZ2rYDscjHei92CfvydxNZDus2sQZwN-LFyX_qN77fetxfWySQMhK_JyUDfuuX9BqnHpYMM6WJ8qEIK6X-mbYQfe7AH4rB2Tv89OhkjfrZoOF7d9FGMLz8-mRXrtn504H82LBqwBkDRvogFnlrI9PKH-uzW7bqx_W-UNahZvw2lN8J7Q7fv7dbCFCSJXSIVdBXrtLDgIKLxtsdpOErmJTn0bg9VrC2Cz8fic087EVFn2xIy8clnXNvDI7gPS0yzgRLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e045f6d4.mp4?token=Cc5A9pr7jWMzxXQ39FNiYtJgrxlYbnp6CME2AZODRoFL_m1_JGT9VRb9aemzch05l5pTqeoldeKY7OSSBbFZ2rYDscjHei92CfvydxNZDus2sQZwN-LFyX_qN77fetxfWySQMhK_JyUDfuuX9BqnHpYMM6WJ8qEIK6X-mbYQfe7AH4rB2Tv89OhkjfrZoOF7d9FGMLz8-mRXrtn504H82LBqwBkDRvogFnlrI9PKH-uzW7bqx_W-UNahZvw2lN8J7Q7fv7dbCFCSJXSIVdBXrtLDgIKLxtsdpOErmJTn0bg9VrC2Cz8fic087EVFn2xIy8clnXNvDI7gPS0yzgRLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مصلی تهران در ساعاتی که امت با پدر خود در حال وداع هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/666311" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0822c17c6a.mp4?token=gkKxjZgb6M7cVMHpxju4UIPppDxQSoXqfbIV3E-ZV-68F7Dri7NqcWHA4z_hQB9aVXLOm-6LSpLnuGsknbkUvbJ7u0OkTCh9cdpx1skvNPYaT-co4UAoTqekfmKGfcCy3aeGPP8oLyzbY3wvQPJvRVQ-v9p3PREXNT3vZuz3SUMqrcpLCmOnpmZ6yUYdnHWa1S57VWoV1JxvXWF5f-g1h5Fssk97X_xWJVuHpvAsvUTI1pN0x5Dr8DraOBzl5zXAw3468JwGFXhcZPCTIV3QrLV6gHEcXqPVpzpcrazV3NgjdxmQiqdVAb2fZ_AX-w4YEBpZWGpiiIx8oDr8kATWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0822c17c6a.mp4?token=gkKxjZgb6M7cVMHpxju4UIPppDxQSoXqfbIV3E-ZV-68F7Dri7NqcWHA4z_hQB9aVXLOm-6LSpLnuGsknbkUvbJ7u0OkTCh9cdpx1skvNPYaT-co4UAoTqekfmKGfcCy3aeGPP8oLyzbY3wvQPJvRVQ-v9p3PREXNT3vZuz3SUMqrcpLCmOnpmZ6yUYdnHWa1S57VWoV1JxvXWF5f-g1h5Fssk97X_xWJVuHpvAsvUTI1pN0x5Dr8DraOBzl5zXAw3468JwGFXhcZPCTIV3QrLV6gHEcXqPVpzpcrazV3NgjdxmQiqdVAb2fZ_AX-w4YEBpZWGpiiIx8oDr8kATWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی رسولی: ما برای خاکسپاری نیامدیم؛ ما برای خون‌خواهی آمدیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/666310" target="_blank">📅 12:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c086fdd47.mp4?token=m5LXUmgbLlDiwD3-_5oxOtOwxKRxCvZIjFGPrezDY0-HMnNdJ_uLo8Q1_kYClQNsxD5ujnjbNlu3le6Z6F5yv2vG7HLJhvAPB3rcv5XxW_6-eN1VqehkdB7w6YZc7CGDSikUVlesInrLMwHiV48Igf0N02-gBLzr72PO92sFibx0Xcitt65ifl_G8E5ErREgUGxgmzwOJDoWQtUuyVwrJXbQrAt8dXGmUy3-EDj88sTKhO4UkaGq-15XVQ6Cd3nGvaCUn4icERGpZJVMMhhUL65O6s7_yA0QRKsHMlqryNSvJbjPvEm58EN47O2BmLKxt7xyp1Goe_TFe7Wy79-rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c086fdd47.mp4?token=m5LXUmgbLlDiwD3-_5oxOtOwxKRxCvZIjFGPrezDY0-HMnNdJ_uLo8Q1_kYClQNsxD5ujnjbNlu3le6Z6F5yv2vG7HLJhvAPB3rcv5XxW_6-eN1VqehkdB7w6YZc7CGDSikUVlesInrLMwHiV48Igf0N02-gBLzr72PO92sFibx0Xcitt65ifl_G8E5ErREgUGxgmzwOJDoWQtUuyVwrJXbQrAt8dXGmUy3-EDj88sTKhO4UkaGq-15XVQ6Cd3nGvaCUn4icERGpZJVMMhhUL65O6s7_yA0QRKsHMlqryNSvJbjPvEm58EN47O2BmLKxt7xyp1Goe_TFe7Wy79-rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه یک سالاد پروتئینی که می‌تونه در رژیم لاغری قرار بگیره
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/666309" target="_blank">📅 12:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aghaye Man</div>
  <div class="tg-doc-extra">Amir Fallah</div>
</div>
<a href="https://t.me/akhbarefori/666308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آقای من، نبودنت هنوز داغی است بر دلهایمان
راه با رفتن تو تمام نمی‌شود و ما عاشقانِ تو با نور امیدی که برایمان گذاشتی، ادامه می‌دهیم
ادامه می‌دهیم راهی را که شروع کردی و نیمه تمام نمی‌گذاریم
دلتنگ‌تان هستیم تا ابد، آقای من
🥀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/666308" target="_blank">📅 12:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49366411a5.mp4?token=uIHFL7mNZ-kfjoQYutEs7oRcn4Z-OKA0IDD9svv_GfFgpFYj6If3XBgg9FdBml6Ypb54BDHQWVa2U5-fyhL1t_zfs8Qgkc4ddXBT1TuZLhoGV9jjvBSBwAXDdPnqYmtJH3-r4QYVx3aLB8UN3iiyHZv5QaQukP2z38REX1kt0xHZq-2GiZVKWj2T3K6MzyGPPP2Am3SuluBNILXCn534c5ZL8JxtDDeGQqaLfQCfi2kowqyq_iNKZqBSylx_zyzqSvCiGvX7gqyCpzRL0X1DGy_w1p5rUsKRl_fVGwSEe1plzZoufSnAeBhjmDPEGEDVpkslRWZKi8op_jS_njjR-pUyyd4PPwz29x1vWDRswyDoJeXi7rFPHk0enLV0uqEt0XjbfYzN9bsWQoOf5f-bOpaoqc5VhJ_oh5D1-4gKxGzsFxZnw09T8z1j9AB6wM4f4EkTdINysmtlloazA1ptrVJGZX7ULBhNebYBOAGZEh6RPAlhGeO86mWE5fqf_p4pVDwiK_CX16Vi6lf7kvy8po778uLval9hqylueyqFrL1Kf9-GuQMnUHW2xiQk2UsT62ZUM9kMhWNVXAXFG2IQ664kIE2SOuGGBQMzqS1Ny1cdcQhfvnRjd59kH9rZL165mQcIw37NbbIFFdIkWNwz7YoWKiVXWM9QnFnaWbkLMZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49366411a5.mp4?token=uIHFL7mNZ-kfjoQYutEs7oRcn4Z-OKA0IDD9svv_GfFgpFYj6If3XBgg9FdBml6Ypb54BDHQWVa2U5-fyhL1t_zfs8Qgkc4ddXBT1TuZLhoGV9jjvBSBwAXDdPnqYmtJH3-r4QYVx3aLB8UN3iiyHZv5QaQukP2z38REX1kt0xHZq-2GiZVKWj2T3K6MzyGPPP2Am3SuluBNILXCn534c5ZL8JxtDDeGQqaLfQCfi2kowqyq_iNKZqBSylx_zyzqSvCiGvX7gqyCpzRL0X1DGy_w1p5rUsKRl_fVGwSEe1plzZoufSnAeBhjmDPEGEDVpkslRWZKi8op_jS_njjR-pUyyd4PPwz29x1vWDRswyDoJeXi7rFPHk0enLV0uqEt0XjbfYzN9bsWQoOf5f-bOpaoqc5VhJ_oh5D1-4gKxGzsFxZnw09T8z1j9AB6wM4f4EkTdINysmtlloazA1ptrVJGZX7ULBhNebYBOAGZEh6RPAlhGeO86mWE5fqf_p4pVDwiK_CX16Vi6lf7kvy8po778uLval9hqylueyqFrL1Kf9-GuQMnUHW2xiQk2UsT62ZUM9kMhWNVXAXFG2IQ664kIE2SOuGGBQMzqS1Ny1cdcQhfvnRjd59kH9rZL165mQcIw37NbbIFFdIkWNwz7YoWKiVXWM9QnFnaWbkLMZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره نیچروان بارزانی رییس اقلیم کردستان عراق از دقت‌نظر و حافظه رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/666307" target="_blank">📅 12:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تمدید مهلت بازگشت ارز صادراتی تا پایان مرداد
🔹
سازمان توسعه تجارت ایران از تمدید مهلت اجرای نرخ ۶۰ درصدی بازگشت ارز حاصل از صادرات خبر داد.
🔹
بر این اساس، صادرکنندگان تا ۳۱ مرداد ۱۴۰۵ فرصت دارند ارز صادراتی خود را با نرخ ۶۰ درصد بازگردانند و از ابتدای شهریور این نرخ تا اطلاع ثانوی به ۷۰ درصد افزایش خواهد یافت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/666306" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666305">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdAqz4aqcXBNC1aL0E90oPFBJm491Oq9ZxJ_YuuJv9ppZglMcxaQ4lWNi3G087JOnMcPtKh9XD3zqo2o55TdupGSHqf2knwKyPWGVU9OK3VVsxVq04izDg29qjHgLA5TgW2pV0i_hyQkm9N7M_MBmeh45QfLRzNUXvT3NxyLSFjsB2ElhvuZI8sQY2x8oxSvcU-7PdRnWUAfYBPi_5TDCocyqnfagxc9wAvVpqvA5ZLD8T1c7aF8nmHNUB0DuOtLSurgwkQaNLkdBUlHHffAIcWX2dvnIL_F9_ENi43CLpQbsA4H4vuUlLEhQjfKuw7xN3Oumi7BmZZSvZ-0-Zu1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمهیدات سازمان راهداری و حمل و نقل جاده‌ای برای خدمت‌رسانی و حضور حداکثری در مراسم وداع و تشییع رهبر شهید امت اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/666305" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdHS_3U-mpnhi91pLYL-_TINRXgb3Q8TNkrcgqa5s6tIXHFCHo_CmU2RVTjx8CR-OnbCvg3xUcqU7y3j485qmIRgD2NJ5LX3Z4ZKONuDhTFPvfb8TEIBfQVlFCTfYu1_HiUUnLFindpz6Tz6KxlYZfclj9HDz4BqUlbbjoTwChWUEbWKNnhlQhaPguLDalkRsCVclGHG_QU8e5SmEtgeMMs_xHXEoIf9IQNYJ4UG8hypVRtbh-DrvtMyh7fDaxwAEBXyAKO_8SoWefR4owz9whU65jjC3KXev5GyB4K4wrK_P_3cR4gUEzUwXQSF6gEhL_ytMGayCk1UnNkNKXJBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_BFzP9D98OscMISYrzxpjLP53tdO-uUw21nkfWH9zCdk-k31Eeq9IrlpWU9TUUVMgGp1czx5kMAZdnledeaSF1wKJzcG_ujTiV8S5TRI-a84wOBkNxJ4cxo5wRrSxEHPEHnpYlsEa5HH-7xhuDL75o7lhfFoaf7vIlivYwHS6MQyKi5UN_mXuzqu9eMLWmh6iAPKsey-TwRdL56KmJtTsQWcRRJYA4l6bj3fvAZEMk4m_Vd0u4zpeNnx-bWK3D3LSj4VrkaApXmejI9K7pG2mrtex-nSMUcIzByHKMRbUloYA9a515MQji1Grxe1dFPYhG1l0aBb0CVCchraLrzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWgDnuXMw9pjhz9DH-sHBGYTVn-rNgQ0XT0GrkW7rH93WjvptAALmVRoiog4m-lRZYYQSnliv5BxGFhU45wMQWU_mwBSaUu_vwB6TqHjqIL-TmaQ9LFcNBWi_NDuTEc3Fg3mfGKUmICKi_Uw5f_rDweTq7emGGDQj40FhuKzd_ZPjXEaq2V9b3o81PX9NQMny1rau2AtWzWc9u2l9vq-qzDtTZyNnmPsOYfYT22isI67S3HaexIS2Gu_-RLCjYYN2NouHYw66PIcx57BO9QMucTygXjhMYD8sPa-8WBeANA8_f6m3l9KRedwilZ8jzL1Tz-e4An4ZWHu66VCCEohaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASr_1DZNT7Vzn7w1E7pGSFXdkBr6-ATf23w3CSHpQc39ED8mHiBzZDnJ_Bo-E7wVHNLve1J5FayTroCXOcO3n08n8Zo5KsmK-_ERPTxtGctGWTRhh31oqM8tiBXJeLPWp1HSwKxNUpkDPUO02gFq5POiJ_gPbeiAropYztiMJmFoQhlm4AwmHbN16dGP-0Q7b9JNKeIOSyklWulvFM_mmD17ftfGksOl22DFBBUVkQzEZQGKpWzsPYh-YcpMlQ_o0M3DdfGmVhhEfc-lR0IWIXcouNSWSIzfazEnFERexXNMmlOezK8OHkn4qykp-oDQPAGJ3bPBqXoAY3Kzea28LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUqBDwlS528WuWtOVAgVnHLL3mTRBBJ7y3NtEvv3mODZzgx5iMpviwck2xSxU4fHr8CAR0rxa-hhDJVEo07ilymBTbnnyWihTyjPEl8bYzUwlPIsYVsQ9K2slzuVoAZAwehuhmmW5Wc-jICcuHnQzx8TL4KEArJlsvxZ-GhcQecQZdctX9k-O2bXPzOZlmcUbd0w6z2oRxGBBsmPalnOP33ftficfvSRVzDBE7uEy5I8OAKShKxFvWc6wUkdo1M3Ziu2kCJUf8bgdfZ9kSvcc16tUiNs4R76sucTW52inr0sloIh0WKPPBe-JGFg2rawjd7Vxg2WKDNDoqqqlnFmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aP8dAaJF5kHMThuD9NaVIv7oj1yrMYnGnxZp7GWBnezCCzRaVJnxWTEmKhWdVb71io0WtlIprsUqrI5aaSDAKBnXSRoKKPOXXCUqhal7b6nGmJw2mWS8bFY_15I4Sja8JH8go_7_dhZTwIsWHyvBXe2QwWqd1RvflhKANKWYzD1rhJv92i9QAmlH9qKHvDMAAHfs_vDoAyLmjAfXs2r_z_4XCzpy3nWBgamXn7iFGwej1qovPbocG8ttY_FdrSLclD4-sWXjlNwjaZGSY_7NLY9Bpea0RKvPGFmfUjgq5PCKrwL2m4dhKR3xtmIaR6fhAcKb0bjAsUec6Io-QPh8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkvQ4GV20OdVTj90vL1fo_uJYQ2z3LxB9cecDYZJxJ8fwBbsTdH5SVyhzML4VZTzCJBBq9SHxZvORSgxcdmCVNatb97u1qVpqOd-wUOHfWpaVlP3Si4FTyAgql3DTuryfuhkY3_4miFWLGuLzyLwzYylTlYr_WJT8gL4eAZDaGrDiNHvbGuqI1dLcKBuKjCio6RCWQaEqkAAInJPHvuP3jnIUsv6cYkixYX8qguioc3iy4OTafEqPHMc8ssjaoXEpBF5Xa3WKeatpmqeMihrpTsw5N_L3vuD9WzsOAoAkk7YzVVQPbiI7jRjvM8dta3vDk1xRmEk8yJu9Qid3zxS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPW-t76QPuqTbDc_V_RLXIZVHvS00rNRpoagnbIFZWm4kDLz-QbYxYufy2lCwGBomlVZvB7o-Rw9ARG4J9nOO7v2Pc3rpSNFN7kXkG6RnH62AUG-ogd0Gz5KKxed1qAAJUwzSSaZrmNqcE4mE098TegRQMlC8US14Y6HYpS6tB372w3_r7HhNemBrsSf5EcoXX8mjDjI4COGX7rV3t_6JQ814RxSDmLgM_4nXZbnIyT9ayUoiR4Ep7IV7ZOSrT_fqLrggjwpuf7lvAU4UU1gokdq6jRkyuN2rq_Wcn5um71espcwMPLKOc5d626cqm09clnE6caIch-0wOQ_nNJA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8cdgjqd_A20rVBs6heAaeFU0h5lYULTNSvrN85mEA2vbL3Jv-aIKrVno6xjkA6JTdxGXHwXdEhprbOUoQJpot3pL7wfLbHGa5jgLovzW2ZitKzA_LabZRZEfRqLWenKjNT5kUn83AqigAQyGwZ9MFd3j6Oba7LerGGTXfdKxEPGnSv1UkpbWTaI4zAPkfTvcoLztfjvATvvnjOsWDecw4W9Im6GzKqJxiMxY8t4Mc6oG3Of_9-x6q45J-YihLsEI1H8p9qx8_eOrcipiklr0DB0M-rowWIlki3lIucmlffhQDrjtwtTXCOohKO8RXLDaZlu3cnrD5BSRafwWO3sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kt9yMjoUkSowmP3bccTs8lcnbEXuhzMTAz-xA7uz_kPiomOAIKRXXqEPQh65dI6Rb07puz7SwV-uCKRoiYRMGNCRLNM-9uSTi5ez0ib5BoqZZ50jokuhKHwxqzzT3i4CsLitrIoz7IZR5b5nm7E0vLATKtKHqzyq98BbmmKkQOpboHdxngxcFMJcKQQXr0wMSB-R04ViR0oBHOUWKOMyRmar3GNaJfCiCXeeJQs5BrVVk8PHPqpPEgJ4HaKzpH5viqjd2oq_UUDpXm6bvSgKSesZgRwQHFm87El8Q6BdbCRaHq0ggBSyPXSB5pFpIHQ5EcLOJHzCNToQIXAsqFqdMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری که رویترز از مراسم امروز در مصلای تهران منتشر کرد  #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/666295" target="_blank">📅 12:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه الجدید لبنان: بیروت موافقت کرده تا در کمیته‌ای که تحت تفاهم‌نامه آمریکا و ایران تشکیل شده، شرکت کند.
🔹
مقام یمنی: رهبر شهید ایران الگویی منحصر به فرد در تاریخ هستند.
🔹
پلیس‌راه راهور فراجا: ورودی‌های تهران باز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/666294" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXpm9CfWN37911gkF4FOAT5Uo0CSuOBUUvRwsnZlsq8Q6Jex5Spg_jG7kDLc_wVQEPMluKfjhX4v997-qUookOZL2Li_i036fNNPj7-QIpJk-mlj5xpCY8Nv1dYa9AiXoEKrgboLLU_72LQg9BFOonhzx_IBLdaojBE-U0vCO00k0KtvGdauskuc7WWyVLQfbTaHyhyC71EG9EW61GZErq3D5KpsgshaGr0ipi0LmOsHL9WKT6CWNG7Uid0SR6Fvtf51MEf8PS16Qi0046IVNU2JYy6VaoX1g5ePGzXc8SWJBedQIPbi7MVfgaN4YXoPwLjEJ4pOW76eXfQyxaB48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب در مصلی امام خمینی(ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/666292" target="_blank">📅 12:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIVhauS4KWerHSY78aPuwUV3Rw8q3gI7osLkpv-hxZ5y3ceVH6XTaNizXzMXfNZt-8oq3ECk0kCiArBxbO1f-8IWRjkL8FqLHQo4vcnMSsk8rjfN9jLFkhxTMJWPshsepHZWVLWJg8l0yXNyP8nLH-iSodj0PCeLHUNBs-LSLYO1EZgA3PEczuLSoQUXwIjH9zRKXemxYp8wzvwDDLYIh_-rR9lZe2w7VFc2hFtztCXby06pjN6xWFNRH35xw28M4AE-v90bQC5j29mCj9JY-bXmIm_wy0Lbq_21bnS8cwnhr2U4I8STRDHZiFDfUcRdyM0iXI0BBBpS4E-AyPqKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: تشییع رهبر ایران نمادی از مخالفت با آمریکاست
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/666290" target="_blank">📅 12:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در محدوده جنوب اصفهان
استانداری اصفهان:
🔹
انفجار‌های کنترل شده مرتبط با مهمات عمل‌نکرده در جنگ تحمیلی سوم در محدوده ارتفاعات صفه، مناطق جنوبی شهر اصفهان و محدوده شهر بهارستان از صبح امروز تا بعدازظهر برگزار می‌شود.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/666289" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رستاخیز خون‌خواهی
🔹
گزارش خبرنگار خبرفوری از مصلی تهران هم‌اکنون #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/666287" target="_blank">📅 11:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
صدور کیفرخواست پرونده رضا پهلوی
🔹
دادستان تهران از صدور کیفرخواست و ارسال پرونده رضا پهلوی به دادگاه خبر داد.
🔹
این پرونده پس از تحقیقات و جمع‌آوری مستندات، با اتهاماتی از جمله افساد فی‌الارض، هدایت اقدامات تروریستی، همکاری با دولت‌های متخاصم، جاسوسی، تحریک به خشونت، تخریب اموال و فعالیت تبلیغی علیه نظام به دادگاه ارجاع شده است./ میزان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/666286" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae0bc8eb4.mp4?token=FMfB09EJ1wtfWiCZUYwPt9EBOjQleyJZyyARinqa_iUzo2hq8xcnYoPdm_BliErHGPqcWecWiY4gby3uIfg5RlbXRyUzBTBlQBLTegxZZq41IcskuMt9soamz-BjXc6-gr6eRrwlSJXLSqw6uFOQ4ifU79zuLAicADGwR1kgTHYp1a71zoS2SlDh2mnTiCZjr3aOHaV-CPZvGIgnPvsF3ICkHJKILShwM2R9ybNw0Hxv2MFpoUshkSEXbftN3ODhYI0AWneGSe3hzfpgWN90-e9HOrbiie_eVLBJwU0Kxn9-h3W2XOSecFFO8h2LxoLvjPMAwn4_IVZVaRJvkWNDxx_CvAYwsSwNQmp-0UJ0LLG9FFIl1bGH_MWq9RL2zfWPF3IsVLvusFncJbusDC1hhus9CLbozNuKH7cDJ0pBwlBgEaJc2oDVit8--qYMXAYJEdXs9a3vOIdw2UEgKvdkEuFkw6AC1lEtLiKyBEJMO36G7uTbwFMnMVGJFtuN5qZdQFIGvtSeQ7pGZ0Tj46RcEbM1eUIz32pNsi7ofOAVw1DSUOOqbM-3iEp23csUFfTBsxfUnW0DVRKYhqyXt-FA4GSLW0fiZERuqKoI19al-NVmoaNS9lDxGTCoAsRuD9hNDusKtiCT-0khT8h6J0rWdugedfB7PLPCQBMJfEhYC1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae0bc8eb4.mp4?token=FMfB09EJ1wtfWiCZUYwPt9EBOjQleyJZyyARinqa_iUzo2hq8xcnYoPdm_BliErHGPqcWecWiY4gby3uIfg5RlbXRyUzBTBlQBLTegxZZq41IcskuMt9soamz-BjXc6-gr6eRrwlSJXLSqw6uFOQ4ifU79zuLAicADGwR1kgTHYp1a71zoS2SlDh2mnTiCZjr3aOHaV-CPZvGIgnPvsF3ICkHJKILShwM2R9ybNw0Hxv2MFpoUshkSEXbftN3ODhYI0AWneGSe3hzfpgWN90-e9HOrbiie_eVLBJwU0Kxn9-h3W2XOSecFFO8h2LxoLvjPMAwn4_IVZVaRJvkWNDxx_CvAYwsSwNQmp-0UJ0LLG9FFIl1bGH_MWq9RL2zfWPF3IsVLvusFncJbusDC1hhus9CLbozNuKH7cDJ0pBwlBgEaJc2oDVit8--qYMXAYJEdXs9a3vOIdw2UEgKvdkEuFkw6AC1lEtLiKyBEJMO36G7uTbwFMnMVGJFtuN5qZdQFIGvtSeQ7pGZ0Tj46RcEbM1eUIz32pNsi7ofOAVw1DSUOOqbM-3iEp23csUFfTBsxfUnW0DVRKYhqyXt-FA4GSLW0fiZERuqKoI19al-NVmoaNS9lDxGTCoAsRuD9hNDusKtiCT-0khT8h6J0rWdugedfB7PLPCQBMJfEhYC1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همخوانی سرودی زیبا توسط رهبر شهید انقلاب
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/666285" target="_blank">📅 11:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p53mm6vBg_EvNF3mVS70oCvZbR3A-d6SQgG5m0hgHo0z3xz7DELpc33zJQnj3AHyXn5EDz0Kg2-4nXv9Fd6WYQvqRyLqtFDzLNEFDcnONfdDBy0Uc1CEkbsHc1u5VNStfwIkLlfwdeXe0TF3B5YzAtoB9KlybJlp13c551uflTuOVzPWjrYEf4tVLuYSy_ImjYU2O8a30t-_AzTgFLdRl8S9RtoXLm5dSDhLM_TtOjqy9Sk4aMHm8ZKV8pkkwmpx7QyTFWx7wjc1WDglxM4gI7oy1vZXhTBe-lZWbBLmzsNvAnKNh5AIOKFF4rt1PF0zvJ-xIRECujqYPlKwIXtRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: سری جدید ۱٠٠ دلاری با امضای ترامپ
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/666284" target="_blank">📅 11:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8e4a658e.mp4?token=KOn6FwnsAIn6TTl4Ch_0XvnFHLSO6kL_LUNzXq0gqeYulvXHBTH2iDshzehzSseO-6UntO7cA98_ynh9Ukmbli927Cij8ExvYzGB6w_rKOYVKetS0LXYzN_AW0fqgl0bqnXul_fentAeA3NEp8MMV_6becUfrjyYl5Pi6TAxRRRfihwb9_SgzpcrHHwyWq5ILnAnPW6iD1oshZIdTKYVKLMH7UP2sBV_5pqVlW5cKY-xN-0w59B79-z8iczdSj8cUOj46yZSea48GoryjRqrCenG7Lin_-uYsF-jV0HbT4e1F_VKuXkQNFPf8ksnqldOTQ2Eg0Q-C8EGDAdOHCrRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8e4a658e.mp4?token=KOn6FwnsAIn6TTl4Ch_0XvnFHLSO6kL_LUNzXq0gqeYulvXHBTH2iDshzehzSseO-6UntO7cA98_ynh9Ukmbli927Cij8ExvYzGB6w_rKOYVKetS0LXYzN_AW0fqgl0bqnXul_fentAeA3NEp8MMV_6becUfrjyYl5Pi6TAxRRRfihwb9_SgzpcrHHwyWq5ILnAnPW6iD1oshZIdTKYVKLMH7UP2sBV_5pqVlW5cKY-xN-0w59B79-z8iczdSj8cUOj46yZSea48GoryjRqrCenG7Lin_-uYsF-jV0HbT4e1F_VKuXkQNFPf8ksnqldOTQ2Eg0Q-C8EGDAdOHCrRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استوری دروازه‌بان نفت بصره عراق به یاد رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/666283" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyBRmQr9g1Reg51Hefw3tyPAnHePZIZGEOk1IoBmyWZH43-qscPFWq1ciXBFlOqy1l4V02WLA9zNCpcFu6hBTdw0XFVHu1p-O8yhjFfHYTAe4uKHxbfZ2pe_MN-kOjM72ryEEE7jtolmc3_DA4yDnCfVzj14kuJDsSBIfNVMJdngwrv8sOorvf0E8HqtGn_aUrMU5Nkw3gCpiQEU_ZuBXPVsUmzIcLOlVuIjfIn8KluHniD55Fd8d2jRasa4Ur7fUc-hG_kehaW_YbaYHpe7SW54ojvC0KiYqssXo1of3TSp_55B05KwfkhIFX0kA-C9ARNK7vCosR9movk3ApSSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qi_LgLWpUtPlWEEXK3-Jwn9zsMGzNlUA05lUE0Zi8llWAlqX-8CHA4W3-BqXBp1BodPaHqh7fkHKCA3z_kuHooxLv4OnvUPIkZOp593Bwu92pCNYAVTbbHIsOY9z5qaZInOkt9MV1xrRUwtWR4uiMQ1GSF81qG0JiXAbPB0QCJRvoBHHDw1Mnt664btRxmE3QdF6Z_wbRSAb-4LPiWnfx-oohZfeYt61tk74ExosuHpEczsO2ovzRJHNbkaCEHy1Zb4QitQlkrSdxPzUOppwIT7Cd0OijYQtp8sX49pK-I7E32_tV0luSN4uwTU05AAuYRT91OnOyx8IoQRJREKoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmkZvR5nF5VePE_sV7qElP7VmvIxj6tQqPortMe8qbuV1uulA11ecSUTlqBaN_HP6VsYYl1t35uo56SKDu4MI3Pn2iHvWGHhuCKfWAmk5F5yWIwMB22N-Pq5BcBjPzgAWGV3VFw9N2hMuzkVolS6vvSjcri0ycK7nu3pT_dX6T5cv1RCe0IJpMlzpiPPu1gILEXg1oqEdleFj_bbonO8KAYfJn1b9jsaN1dme5AJbdh1_fyZAswQb8iJipmz_o7e4uaCm2O6E05axCGkkpkx8KllZpLugR2-G66Js1J0Ij5ZjdHnJrBDG_Y7C9TgFO5k3y5QARqE2DEHR1FHI_16Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfIj7rGWZ2v7Ys_HMWVpyhBKu4PJewefxiXgX63_WnCFcK3CCxo1YSuU6ZcmFpI43fHr0x8-knOckNOY-oX56K8b4yPaoRWo-2v4l2rkLc1mxPpwtV54G_8Gy52EvMhCWEVIyMCkrnub3YYxCpaSagKd73paDEY6phgQ0bT-BZGJRJo--G3W9XptjxxzAS6eF1EibYnV1lzmRbwbZowveXS9FJh7Y-LgboQTDAj7W6aSS_OzljPDt08bk-o_gSwBmf_3yiNHfXDL4CeHfiwkOPaQfA5bp-Kn1VtdNUhTSvHHgWGddbBJg6sSdOMaHXrXk-D2_FqqaaWIoIjhEXUDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmiWNNsqYHus9qoe1fO69NEOxM75YOQGfHeRxlMj85OYU7B6piFhSiWQ61BMlnZrCeFvgHiXdQnGqutVdfcoqq6Grb9MsBnrSq4HfnlJIUnV9t0vt_swalk47hhJ-kRp5i0A-VQoqpeS2BgtV1901i4M5QDodoBbU1DsGDuyXz6mj7wt7V9w_SSZPiMzvvOOTCFIw9wwExFv9EGf2zEGTe8eg_JUcHHfE6mEBQ-R1yLZjNsCT6tT_cdiRr6wuamPdKlBdGXHQWVONDOydQdUj6MumNMZgOI2Dc_ltKvVamG8JlxoAeJBkYP55nH4HpJnjQkNLS_vttOskNpluSJpWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONDLIIf0JWcq5kxARQ8emB5sd_hcdTZvmn1b5HRTRexaJMV14KrovXfmpDB0weLXkEHBUeZ2J3EShN2a6FByzuA0BL1GVJRMxab85nji1VDxVvSXXDOWato2J8ZcruRd1CAmjdHUvjobVl23YrcnTo7bVqKpkeVxhcV79hsnJTXIc9M2aL2TuJGHrf_lgoIVHpx9mjI5BVouNJ5_CWEj0ROTl4cOtZMr4qr3CYepPyGlUz-BTTyCJSyPWN2DYGWDKlCqo2K4UBsybgqNpiXedE5wwtXYKllKPDXCoC1x5Rg9jdjK82DkawlLyHgcC-z7BnTbBwnd6JnLoPliN9qwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POHxEZEV4kcJ49m7qIZ2Z6PJwGWuQZxM71ryIbenS5hiAuX0pfwzHtc0k3EVyRWyObYhmic6fYtCtN4I-8kNULW5ogjrtUIAxGAXhZw8J3XnJ2lq3c7cPlmpuelLjzFxe_6EokSj9aJQupL1r33WMWIK0mQ63gNiZiu7wtN8WzpNgN2tO7cs8YMHhtNCVy5KZPRDGhscyk9c_X-332CxyoTrXjYiwB_Tjua64QqWS_8bPrJpETODYZXc2W0AK_LHtH10jXp_4auRq3EXPwPRs_1N7rh4CWY1MyJ0jix-6ibUS86f_QObZNn_JF0AyeIwgLPqZFA0p9-spU9EndCW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM8ZJbLhMt4Sxybalpq87Hqs-wmImuL29TlJn6yjWe8TLSdPgrR_5-Ct3OAazQN4HEB_97TYNjWNUjPPHo1Cr3tX98Zxl1Ax4AUR0zKOYpljQ9gC3dVGQtGCUhGhRWpMQBtgrZn7tn7y4oKsq7eQAuUx67Jkc4FdqCP7fU2kmZO-byRs6l0kw8TuRXDO05VglCONL4GTd3pc-JId2Rux5eQ8Fm9ShZa0Ff1xdRynwuk1IY986DWjJw6RFeyxLKKDuS7sWSVMdP_xPBmFOH8L76ewqFWN53IZCZDD6vfCrcwt0JCHwUmWSLmNyZ9vWvQwLaiRtP2CdRRlkMiNe43ukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از بهت تا بغض/حال و هوای مردم عزاداران در آخرین وداع با رهبر شهید انقلاب
🔹
عکاس خبرفوری: زینب سادات اسماعیلی طبا
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/666274" target="_blank">📅 11:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
️
فرمانده نیروی دریایی سپاه: انتقام الهی از آمریکا و اسرائیل چندان دور نیست
دریادار پاسدار علی عظمایی:
🔹
اینجانب و همۀ رزمندگان دریادل نیروی دریایی سپاه و حافظین تنگه راهبردی هرمز با خدای خود عهد می بندیم که با پیروی از آرمان شهیدان، راه رهبر شهید امت را با قدرت و استقامت ادامه داده، و رجاء واثق داریم که انتقام الهی از آمریکای تروریست و رژیم نامشروع صهیونیستی چندان دور نیست و پرچم حق به دست خلف صالحش و ولی زمان، بر قله عزت و اقتدار برافراشته خواهد ماند.
🔹
امروز ما وداع نمی‌کنیم؛ بلکه بیعتی دوباره می‌بندیم با آرمان‌های او، با صلابت او، با ایمان او، و با راهی که از سینه‌ی او تا افق‌های روشن آینده امتداد دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/666273" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
🔹
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت./ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/666272" target="_blank">📅 11:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQQscHkXuhLtCkSQCBEabOV2tsMxtcmMi3Yo6xscppdmsfv1yjO6HlMP6tEtVmzKrN8_SkbPDoYW95TEvep_gV-xxuYxdm8qyMlvnCJ0DVhqQlP3Wf1ndbn_xD2eEsyyhwxfgeTgGOUXmEOEuTogAXcDyESyJ4JZzqBtaJRwRCCmuUGybai35RXueo0xKrO3s9eNDaZZR3TJC1UQnNF9bTNrHrpkO6dEdQOjhuCOf-TfhjeNsYi1-GwHv5YiOG1jY1elZmzC9ru-mPjecoVQbMrlyvkjQ0VEUImEHHWBs6pfpDaY2JPBk47faIV8yXAsBDeo4vJmJr75KiSbtZbDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛
«بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافیست از مراسم تشییع در شهرهای تهران، مشهد و قم عکس و فیلم تهیه کرده و برای ما ارسال کنید.
▪️
سوژه‌های پیشنهادی:
پرچم ایران
ثبت لحظات مراسم توسط مردم با تلفن همراه
حضور و شکوه جمعیت
فضای مراسم و جلوه‌های معنوی و حماسی تشییع
▪️
آثار خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666271" target="_blank">📅 11:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuYcqnTn075Wc_g06G9ZyNZYl5RkLz8YPHEsa3yJYHnPs4DMIOa6hRZleLodKbYGGgJlS6KZx8mFsVs92OXkd4xS23vzeuFPmoHA5Icj-3EjAzSnmzW7hBDZikiQ-tgcixXcRVXSoMyBr4H6qX3xG3eiMihEGpwcVNtaQS1d-fBoLdZvr0KKEATcoTs5dHyfkzzHBCfKnUr93XUdLHNAOVnSF4r_h5jxhD7BvUeweGasQxpTTBk1ItjrRrPkPi5p27YgCtimzIK9vdvCGWEOVxy3dfZoFkhBZ1tx4Tmuo_r0LZBQ8frZBE_AjvgUz3KKT1Ay09bijwJZhhGuxef4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای انواع پلاک خودرو در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/666270" target="_blank">📅 11:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7eEzAn92SJ4o_kmJc4JFFoaIsPYGWxuzT9tdrpj3XhT5piTE7t7Fe8AqFzYfChlhEsW373YTcGsFOiRlyUISlxLLErz9EpF-lF-0JApf5fj850bLxF1Z-Umaeocda5wQQ5C1a8LpUifNVd106Hw9BqLJyZF6iz3BKWcXdECKs-_WdXzVYFn7izzShGCReQwvvmspRyncOt1bidjOZElNRLJGBw5eJzNaP_tnsE2Fbj7AbcgjoZ_3x7land9iKJSncaDQ454BF2S9ro-YOryPozm5rL4xmyg9IeOxNTdQYQoaSXbVzKEeTpQlTzUTaR--uTZHPc2RUjCj-iu5dFCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این بار، قرارمان یک مچ‌بند سرخ است
🔹
پارچه‌ای به رنگ خون؛ نشانه‌ای از عهد، وفاداری و مطالبه خون شهیدان.
🔹
بیایید در مراسم تشییع، با مچ‌بندهای سرخ تصویری ماندگار از وحدت و ایستادگی ثبت کنیم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/666269" target="_blank">📅 11:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef946d3a0.mp4?token=hUG5L9HlCYMya37eC1cKJ33mXhuNOtJ1rZ6ja8Gt9pWYD3AT3WklWZqSv3CVF9xTfR77cxk3lQsEBxht5183drCoArSsseGJ1Pw8ilCwDqW0SEQIzbIDI1gy3j2G1cQKQ_l997qV9q2LsYl6ahvS3qhr8faW32GfnIZKbdMUlQWXkIjHA3kJ6ONxxCkTT3E-5iYTOgAYi6_gFhANKInemoU3qDhFi1x-2d_wAVVTUVCLJvt3HIqHjCx4-jZpsdBmVS3a_DTa1Sntv4KGH0yRlcn05p5b5YVx8BzQP3qLMzQ8CUArbceu_Hqiz9ova0IyPZiHTk-SBobTESIHJq74VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef946d3a0.mp4?token=hUG5L9HlCYMya37eC1cKJ33mXhuNOtJ1rZ6ja8Gt9pWYD3AT3WklWZqSv3CVF9xTfR77cxk3lQsEBxht5183drCoArSsseGJ1Pw8ilCwDqW0SEQIzbIDI1gy3j2G1cQKQ_l997qV9q2LsYl6ahvS3qhr8faW32GfnIZKbdMUlQWXkIjHA3kJ6ONxxCkTT3E-5iYTOgAYi6_gFhANKInemoU3qDhFi1x-2d_wAVVTUVCLJvt3HIqHjCx4-jZpsdBmVS3a_DTa1Sntv4KGH0yRlcn05p5b5YVx8BzQP3qLMzQ8CUArbceu_Hqiz9ova0IyPZiHTk-SBobTESIHJq74VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود مردم به مصلی با آیین خاص برای وداع با عزیز ایران
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/666268" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666267">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرفوری
pinned «
♦️
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
🔹
خبر تعطیلی شهر تهران در روز سه شنبه در حالی منتشر شده که پیش از این سخنگوی دولت، شهر تهران را تعطیل اعلام کرده بود.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/666267" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiVndAVi008dKG9kVXwTRnRjFRUmJOTi3-YXUNx7L0S6x_b8mKEyL21t89LGmELz7GgFtOx4WMoQ1vJ6RcAnyUWUFki0ZL7YpJOVxRuHh4pAsnQ6VVb1uttaCu8aeWa7WJo4L1tOhGJaX9D_udPMVLFL3Qhho_86Oebs33nwwRqZQX10urVeV378R9qnDHjLg2zglJ-vDYdq7_BsjDlv9OS_u2C-9Hid761U6raMAx9k5GDU4RiX5592LElfdLHEhZaYQdPdAaHUJyXrw0JJbps_DgCsCUMW3xR4oeXj7ChifVU-e1z49uXTwGRlzcnFx126-ASUOR2Z4qp1c7emVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت غرورآفرین شهید مدافع تنگه هرمز به آغوش میهن
🔹
پیکر مطهر شهید والامقام حسین ستوده، غواص و مدافع حریم آب‌های سرزمینی و تنگه استراتژیک هرمز، پس از ۳۲ روز جست‌و‌جو در دریای عمان، به میهن بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/666266" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aeb6f1e8c.mp4?token=hGuf5cXjVGjdmoUyS_diZlZI4HZZS1ri7sV5rTVnrgLC4v_5ly3sKc9XffcpZda_6TCW19P0h0ksGtgx4HQm5KB3x1L21DHocfh9GOMV2kaU8D2j0fuqaFnRvGViy4RM0jv1i0KTJrH_nqEwrjz5fXFrHRPAPx18oqLBKUR8gowTAfJpZ8qDzEDrmMwURzn1o-AqTkATkCN4NoAt1C0tMjqhwT4gqEpoi0w8SIuaUu-CaEwwJFfx7XN9xja5PkBRDQGeG4ST06JfZO-xPdQP5xOP86ahgnGi1HvlVjbJ9qHXgtah5DTWfKwVJ7iBnaV3Xfm0KFqpVOhP8mrpUUrSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aeb6f1e8c.mp4?token=hGuf5cXjVGjdmoUyS_diZlZI4HZZS1ri7sV5rTVnrgLC4v_5ly3sKc9XffcpZda_6TCW19P0h0ksGtgx4HQm5KB3x1L21DHocfh9GOMV2kaU8D2j0fuqaFnRvGViy4RM0jv1i0KTJrH_nqEwrjz5fXFrHRPAPx18oqLBKUR8gowTAfJpZ8qDzEDrmMwURzn1o-AqTkATkCN4NoAt1C0tMjqhwT4gqEpoi0w8SIuaUu-CaEwwJFfx7XN9xja5PkBRDQGeG4ST06JfZO-xPdQP5xOP86ahgnGi1HvlVjbJ9qHXgtah5DTWfKwVJ7iBnaV3Xfm0KFqpVOhP8mrpUUrSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون حال و هوای مسیرهای مترو منتهی به مصلی برای وداع با رهبر شهید انقلاب
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/666265" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آلمان، ترکیه را در کنار روسیه و چین در فهرست تهدیدهای امنیتی قرار داد.
🔹
فرماندار مهران از آماده‌باش کامل مرز مهران برای تردد زائران تشییع آقای شهید خبر داد.
🔹
شرکت نفت روسیه: پهپادهای اوکراینی یک تأسیسات تولید گاز در سن‌پترزبورگ را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666264" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رویترز: ژاپن می خواهد بعد از ۷ سال از ایران نفت بخرد
🔹
ژاپن، کره جنوبی، هند و کشورهای اروپایی پس از تشدید تحریم‌های آمریکا در پی خروج دونالد ترامپ از توافق هسته‌ای ایران در سال ۲۰۱۸، خرید نفت از ایران را متوقف کردند. در سال‌های اخیر، چین اصلی‌ترین خریدار نفت ایران بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/666263" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04b415aa5.mp4?token=SufgC2vH3aKu68O89bVtpefM4lFNdrzA-5VkhmoMF-9ozj5iYT2l-D5gaF9eKT8dE4I1modwJyRy4GxMNNrwAGvwMUJYRLTVxIsKfDY_2Bo53Jrt0k8ZfxLB96NYHiyKkPAKZSSXr7Uosjtc-KimK7VGill6xIhaOA-Spo3jW2Ngm5Fq5AGgPIaBDNOZsNP1-vMnsiYl4UTz9zgitPg3EoSmq88yiEk-qpwfXE7fUBboDCRJCxGwPjPpDt8aI573LFwW40_WsOsA80ubnp_oDErLDFZIfROlcbfhDfJyY4xMD8rXhaOgTc8kGXM7nvwV8uZUq5XBceYkrfM1r4fLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04b415aa5.mp4?token=SufgC2vH3aKu68O89bVtpefM4lFNdrzA-5VkhmoMF-9ozj5iYT2l-D5gaF9eKT8dE4I1modwJyRy4GxMNNrwAGvwMUJYRLTVxIsKfDY_2Bo53Jrt0k8ZfxLB96NYHiyKkPAKZSSXr7Uosjtc-KimK7VGill6xIhaOA-Spo3jW2Ngm5Fq5AGgPIaBDNOZsNP1-vMnsiYl4UTz9zgitPg3EoSmq88yiEk-qpwfXE7fUBboDCRJCxGwPjPpDt8aI573LFwW40_WsOsA80ubnp_oDErLDFZIfROlcbfhDfJyY4xMD8rXhaOgTc8kGXM7nvwV8uZUq5XBceYkrfM1r4fLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رستاخیز خون‌خواهی
🔹
گزارش خبرنگار خبرفوری از مصلی تهران هم‌اکنون
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666262" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d98b5acb7.mp4?token=SiIalaA6s8xmbCFm7Jo50S8TasfEsNnTq0KDDA1lYBMFP5NrGRYGUE6f_MxQhhvEQza76CU36HMZimNFuFDT5T1BIZxzXP68x6LHHTOPa2WBgAhqItuC451NDV5EgQBFyZeGtu19hnlqm0R_adG3f9lBE1z6Qf1dI2Z9lYqrYE3qVQQM3y7JDKBF07cZpE_JFoE76oiUlS_LlRAvHX6e3uXdUlgMC5WOmwev4ZEvnz-hh1FHPVwe6eg2vm_GmmUjf889gLJI2lvkodMiPu3IYiuIviJxrTKC4fCoYud6PW7wi_tHWKLshRJF5b7vmJvAYmjnHcsKt-VqaWbM1GTnDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d98b5acb7.mp4?token=SiIalaA6s8xmbCFm7Jo50S8TasfEsNnTq0KDDA1lYBMFP5NrGRYGUE6f_MxQhhvEQza76CU36HMZimNFuFDT5T1BIZxzXP68x6LHHTOPa2WBgAhqItuC451NDV5EgQBFyZeGtu19hnlqm0R_adG3f9lBE1z6Qf1dI2Z9lYqrYE3qVQQM3y7JDKBF07cZpE_JFoE76oiUlS_LlRAvHX6e3uXdUlgMC5WOmwev4ZEvnz-hh1FHPVwe6eg2vm_GmmUjf889gLJI2lvkodMiPu3IYiuIviJxrTKC4fCoYud6PW7wi_tHWKLshRJF5b7vmJvAYmjnHcsKt-VqaWbM1GTnDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری، روایت مردم از حضور در مراسم وداع با رهبر انقلاب: پسرام رو آوردم که سرباز پسرت بشن
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/666261" target="_blank">📅 11:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjOM287_lR6oMmuYwq2G4X0L7cFdRitKt9JyuN2wMfj5Ja3xJNmweqnUYMcAKwhC9gJ-H1Vyvz08HLIVnCSeuwJaq28Yziae-rYwam4L6hvP-W_2sKe0onlo7NAHiyvBgYt3uLbhE9aZTuV_928r-H_hQit9IuagzXBsC8F6OMSGtjFXJN0PFLDAzNxY42Gjq6rx7JciWy5tAjck13pN_B3Z9MR6m42ZqleMBKuNFHaRq2snHHcOODzXrmEMOmAPWWWuG64HkTBmEZAgC0q8b2oWsM2nGU8jyDTAygylQh_q3GoDQtbrQK26NZDf9qK9QbqLbaUrLBTQo9cq0ZQgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jnl2Emu375srp36nlhjUB8YF8qcm6lHmOkEKHnxGmnWBNzRLlIlDocT5GSuJk8IDZpSJzvNCv99l-13XYp56dXNVnAQbdtksaQtzzGKzr4mcwCmBktVCWesRsR_-HJco-S2KPTi6Bl-sV6Z5eIkKLpDr_8e9JU0V8wE5ZAZKnH1jRfYIa2x8LEoGS2Ff-ZhcIdFgEWLDW2N-He2MR-yC7-rDRgbBR6rU_MS-g7zzk4IFVvn2RzYUiXfIxLkWumbiJ-KW_dvIrBFcPf_iMX5eWmgR2S2Li5OptfePFUXWGe0HKAA6aNOEzLfZkGMiP4vMMQ1Sj_AS4M05onVrX0YozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPmRFWgIVq6Gx-W9GUz5MlDrwoXKH5QWhi14gJGpg4NE2Wrgp3g22Ks1DNmEFdrZxDOpXaNoDjMxe3x70VfqYOE8wtQC9yjH66flCozQeQEFU4mSU7obYA2ACSrQ6HZJ1cq9tVGL-AJssBkgNpYdMRcPZm5dHyywErjs7pfyg59L7H_HhFiqYXAt12HLzHKfqy1gy2tXT_GAJ9_X6jbqssg2MLrxZr58XpVnX1mvAkcpQus34b7C8yP68ZgFfxmuqAB-jxNliHnj4a0YGzqW-Nt5er7y7rA05sRiU8qdR1JGiXhiSOK9BAGfLD-d-XNURVOmYEScKz7lIXncBX3MVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVY7_LTg7sXfyxq8rU3Qwd6Tvq91Tszec8Khz5eWTXsYCwqmShRm4qxP7IXGojxGQ-gwjN1xwUucVOgtaUpTzCgNlTTJsLH8TUE2dXFg1MWukCouWg8M3r37SFJEmuxlhS4jLHb6SAyMriDMzMsdxw3TszShq93aNDChlfPT2yj4bn3GY2adHxMIe1MQAcVSdWHUavsgUHadqM7vVZj93gl43Y9qtEmOnBWqK19zXefSdpx_40y92ZZ24XeTtcft8OoGNcqMflc2q6XkKG7O6D5J50PVV1t2ibxL10F-bZ5mmk_UzmzUrXoocroguPfFh03tPG-ayiypK-iwk3oHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWWm_3glqPoi85u9ij9_H47XrOEdAkuqL6edECTATazpiy99vwf4d51aII2ZgHlaLeZDbNYqjZkG-fMWqd9wiwuDCk3LN8Y-iDzHM50GOUYsC0toiK4nJSwKpx96etgB61pxjvbaaeMfeLpXAEDFc0w5Tv4mfuxnGisaF_GcICOT32LGuqBkHPHpxzo7_pTkO92m3snjfltcIljSJg3DjLEAHlmixqficWWKl9M5iEDn0ylwOnwfMYi860rVaAltD8GwXmnBg6j2noBKDLCFd6UZgTftpeceEuGkdl9JKHLIG75OaGIsHeYZ0JHAbQtWp4agPMvcqWtV8RK4BbRyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCN-PcjiWJcphTa4rkczsXYRUjw_qqu6zNlRRZ9UCSQa5wY5t2qqH47nBFnpQ89gg4C83PGbTZ7g_ZH9b0F5kZ6y38bg8tno2Aa9JEEmA4yk9G1VAfjr-cqUm6vKrZKRYyPR3QKw8v5rXhEQOZGlINIFfIlYW-6_PbmDvpqmCDbUGMTM4wGDw0EEJK8zVLOp5Kqx453ra8qaYpazJ2xvCxR69eg-uQeYB4NgqOpakQ0kUraCZDcnSJNprt0BQNSqXPeiIhUnQak7I3jCEXTlw9huNI09RG3NH9Eqox14aLDE_QuUNl6atEOShLO8XVkPKW7IBobBwCVbq0oFLbxQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quRNbDtgUhU577yXUYqCYLfnI_uDc6dr-3o4cCWPlv9FkFN27kaoxM38ZJL_TT7GFkKHgYTptk0ANqwVNnboU9X3uzvmsciZcxeygyrEFWH93c63OKp7I1pV52TLQeOhq3XqHs715DajNw9bnzQ4xuiTNx-yzzAnjSaAI6tEcGehSLuNv4F-k-ZMpzqWFZwZWJQH5348uje9r1c7p-RSxn5Y4bQQ73UUvfM4_9A-JSqcVQwyI_gTNlZjClenjj20HPu0OPwOjIPfMbQBTXRejsfT-Ae-o8E-LmEA8CDoLSieylKz5Mdhl6OP4iQlUl9Xuus0dRjNZFURggmqSCYU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMPYz4-i_z0VS0bXzw6aAFbZLw5TmsJlwdjF8prziskVARWgsAsmuPRWWhMJVPu6Xfy9S0V305YHxMCbmTAM_5gqWhf1NymK5HrUNtThvyLvp10TgzUcHyJR-S1Z7XpBvI3x3h1ca5EkmOzcoZtLbucw-MqWzoKuT1Kc9cZOYf_9eN8W7mgrDTidMWSMQhgXIJEkuB6kLamse4Kp4EjpEd9alDLI5BtdFtZQ7tyUlSy99GEMzIgOWWtG3dQQa7OD6uZ1QvBN6ng1Atq_gOQyR4ILONN7-gfMw-0hqDGXgUACzjMlyxHsqsgcpTv5Fvag46v7IjoDmh6wCAr__82zpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLRp1U0dYR3VpJz5ge18AAVCpJMron1ZxzNsrFLO3rOAhYLqLfWgN7YqeaJtLulA-BoixqTtnJhIB2r6-a3YIRi6m8Sq6vUThPvZhUtcS4XbHNi68SjEFondz7cTD1cHuHEdOx6t1bBBA98ldR54K2ZM3lKmHO1nrzzMZ966x8WlZqv1aH8wEqxYdvIxRFZLc_Bl2JaE-bx4yrARx02HA9xp2UwD777SpFzTY5UTANggjLbDpNkTKJgp5_P1ZmJCcl40UgW9kuFi5o8aPHdyWIVuXCnbTFR2GHqXOdcm0uD0ZTXMX1qK2dDnWKgOa2jCc1BdfJYfQfzf08Pr1GQwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTG8eeixJAch9xnW1WoiHUMM5Fc0Jv_M8nqqUTy_5tPW4U_sDQH_qxDAdMyJYTdI9uPX-fMQIk8epVdqhk2wLOrDOd6_GHAo0xzx-c3vHNc5pF3mOOe6KSV8OLpH2H8xCazK7pIQ8uN-3MAFHEw5EiGeclGCtGO88nW2tCnPHLtfduUH54k38pvxehUDEOVfBv3tMrEa_rmHjggJCQxei5CQSGRPFlbgkWAUiZoU3LeJI2ywaCo2TJaUi8gHDsXwaAra2tjDzBVVJ0-2mjgQEF8OxfFUpMYh--TOqmzVkk6lBIPq_76bspL9m7OyIxSkSDVpKiN679-PxixrICHvlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/666251" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وزارت اطلاعات: انتقام خون قائد شهید و شهدای مظلوم را از جنایتکاران آمریکایی‌-صهیونیستی خواهیم گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/666250" target="_blank">📅 11:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkHwwJExQghvYIC7vHtbcIa4bdwGWZO0YlZbXSmnqJBz3PVFHeuZhrv0q0Wx0Mwsv2gBXVsSb2_BWCRUgdtUp_ROKPfEbV4fLRw-7D4uara-jSibwjBUDmIHfP9oZgIL9bmuEcFPuPEb9-ay1HTtIaIupu17N52BCW_3DE3eIJklP6k1zlqrbSMWuBmrkLQy_bwJ-QSu9z7Ve-XFhgJvB1lshrSpqIoALv-DMEaifM3PUpB_6AKGqp66QnkXEmHnEqCdMcybvhC5-iQ3bc3RbpWHCNBSuv-TLtarnyR2pllPXgGHsPITeR7fZK_3z_2bOV0Baa-hm0UvHvtXzCEp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان اقامه نماز بر پیکر رهبر شهید و خانواده ایشان اعلام شد
🔹
فردا، یک‌شنبه ۱۴ تیرماه ۱۴۰۵ ساعت ۶ صبح؛ مراسم اقامه نماز بر پیکر رهبر شهید و شهدای خانواده ایشان برگزار خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/666249" target="_blank">📅 10:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
امنیت عراق: در مراسم تشییع پیکر شهید سید علی خامنه‌ای در عراق، منع آمد و شد اعمال نمی‌شود.
🔹
نخست‌وزیر گرینلند: ترامپ از الحاق صرف نظر کرده است.
🔹
۵ صیاد ایرانی محبوس در پاکستان به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/666248" target="_blank">📅 10:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Gn2U16ouEyFNEauvuBwHKWxVfWCG02nJh4YWwcZypIry0R5OTrtibAxUlyNmZDgjXwN5mBPnbyAWoJIxqkZGRV7QBmOHpmRX_X2o5LPMoD8UZlWK2Cm38R7OnI3Ocj0YowjpeSe8v9UILLEqcwu4dw3nnUTQE0c_UVRF9EWGZl9fcsRP4Wpl3Xc83HbXECYX9TNuaugTsPaes_-YsmXunfb9bo1VkB4SnKqdwGPcdOVa59jHmpkUjQBw_kkH9oiTRpVOeICZ2OLJ7MvyWHp3RJ-VVS6m2OOm_NcuyPTlU7-qqIr7QdyGSIYa1_KVpqdYPonq_XH9eulH2Qu88uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگه‌داری شارژ تلفن بدون پاوربانک!
🔹
چطور در مراسم تشییع در مصرف شارژ گوشی خود صرفه‌جویی کنیم؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/666247" target="_blank">📅 10:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0sVOfKyqQuxV7VlmX5rbVDfrdcAMXSRDtLnnpXTG9riChI1yte0rlNtrEHaec8eYuMwrPgy1J7cF-Osz58PdU6F1-HPZ_aR-EU6eY6LYSJEuzyoOUB_Sq7x7RQeFnGOeCe1ESn-GFYe46M-aI4hwW9Facu8Y8lMIbpk4vr6eFBqpMJd69frzJ7mrKjR2z8EQtENaXtVysP_-53S9aYRl98UkX0-cTh8maM_Uz4oXbhrOvdFmY6asrsP-sQUQg6sSBbxth8G2_JEKhKm8QBLhwlqbXyamq18uZL80JWQ1fm5rDMYakCt3GiukThSEiVT58MKksfsQlMiUz_S8a_Whg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/666246" target="_blank">📅 10:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
🔹
خبر تعطیلی شهر تهران در روز سه شنبه در حالی منتشر شده که پیش از این سخنگوی دولت، شهر تهران را تعطیل اعلام کرده بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666245" target="_blank">📅 10:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3me4_gHd9xRORO5vKVNfdDwHcnX7uRWWRjuFAFbp9mCh3WwBpQpugI63ctmP4j7jIQpXJwNrp-gVjDEkTU7QBPaE6xhmbAgclRx-zAVZIzHAfByDTffs-DX1ZvTAiaiAlG0HRoo1xQxB1-qaIhy6S_DwiO6kd6fcxBJvi2FRvo3KRfRXqRPe6EU4CdwtJ82KNgHjJ0HPlvPy7186q7daLrUJC3qvEDWEV-BV-up9JkwhHkw-pJbBeF97MzBiNXhSjRVYvZlBJka9zTm0Y8yX73e-lqMpUzDpAsC7rkMdhdm90YXfvesRn6bXlwSnW3a-CQu7rJRB9y1KP35ky7ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری که رویترز از مراسم امروز در مصلای تهران منتشر کرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666244" target="_blank">📅 10:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR5nTPX0dhwbIRF-4zIuJT9XOQXBgOjib_C7OkqVI-Id4LD2mO4wkWavgqcQFOw2DAraMqpiff2WFIVZiOh3iwB4jGkGMljp18c5zwZ1N8gIaR6Zcrkj4VtPp-c0OxbnI8TceXnZVHC2sQWsWCeBFtJeRpzdJ1jBBw2_meMX7t3xOf5Nw3ujkRwXx89p7j1dx4pdcopE2SRjmg8-fwqiwgYfWlXZheJcMqFQpA-pdlxtRqHQKHF9SOMwlLBhZFSkCswy2XEXgaJ0PHHPf5P39AhYxjEmYlbCuT5AaeHa69NpgRfsXlWbXSWASrqJjF5FOlc6m2v7qdMD7mqtLkIqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تی‌آر‌تی: عزاداران در تهران خواستار انتقام شدند
شبکه TRT:
🔹
هزاران عزادار با حمل پرچم‌های قرمز، نماد انتقام، در حیاط مجتمع مذهبی وسیع مصلی بزرگ تهران جمع شده‌اند. شعار «انتقام، انتقام» در محل برگزاری مراسم طنین‌انداز شد.
🔹
مقامات ایرانی می‌گویند انتظار دارند بین ۱۵ تا ۲۰ میلیون نفر فقط در تهران طی سه روز آینده برای ادای احترام به مردی که سه دهه و نیم کشور را رهبری کرد، شرکت کنند./ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666243" target="_blank">📅 10:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIaX3ZzeuMbsAPA11znf9T7gZ-l0RKzEcaDEet3lJEw8dis8ZtmACf6xXYbg-pyNC-FUbpZfyn8wZPsV0zXRKk-QTZCuEiCKhqOuBaubtuovSgCJIRGyE_Xj2jJlZltqmTebEuFfvQp8_0jXMLNrzbadStUxoQEzJLIdlQHi8eT3OtN4ExYSbhvg7aF8N8Q0bptLMwGrCmCyT3KovVC1k4gemxcJjqMARVsSOCOcTPP-q0TDTPCSjoRb35ukKM9UViA7qw2XF_RLLOhp-ODR_TTzurKIG-R8xaZJsO4dXxgcNJo4Qf3-4ky4tR7byffFncLZf2qYAxZ8BPU-lBmDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم منتخب مرحله یک‌شانزدهم نهایی جام جهانی ۲۰۲۶ معرفی شد
🔹
در این ترکیب، نام ستاره‌هایی همچون لیونل مسی، هری کین، کیلیان امباپه، مایکل اولیسه، میکل اویارسابال و ووزینیا، دروازه‌بان تیم ملی کیپ‌ورد، دیده می‌شود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/666242" target="_blank">📅 10:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6afe047d.mp4?token=BEC__lbzVwP2Cp3uOFS-dAKYmVFueYX19I6VzzFKXaw0Mg5Hx7z8y504PTN4zsStlmA8cM1zXFT8XkiAphnvnMP4o7pfU8ZTiv5cb06U5YaZgpS5JgnNf4SoYVjJSwR0yBQE9uwoJJP-lH4YhojHUjSeoRBz6JEZ_HEq3yLKc0HHEqxZi_Rntt2bKXmcey1YC9Y8ANREwtm3ivuYYyEOimowmlrFE5XJby7XS-_aEQ_h04kTE3YlyGMLEDlF_4LalbRNw6DhUX2-FCgNmNAKllYWKbx9ogs2Vk7UXgUD9puZX0VHd9_dcN9r9GzWECRcgAIwAuHSuxGm73U8Im5YIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6afe047d.mp4?token=BEC__lbzVwP2Cp3uOFS-dAKYmVFueYX19I6VzzFKXaw0Mg5Hx7z8y504PTN4zsStlmA8cM1zXFT8XkiAphnvnMP4o7pfU8ZTiv5cb06U5YaZgpS5JgnNf4SoYVjJSwR0yBQE9uwoJJP-lH4YhojHUjSeoRBz6JEZ_HEq3yLKc0HHEqxZi_Rntt2bKXmcey1YC9Y8ANREwtm3ivuYYyEOimowmlrFE5XJby7XS-_aEQ_h04kTE3YlyGMLEDlF_4LalbRNw6DhUX2-FCgNmNAKllYWKbx9ogs2Vk7UXgUD9puZX0VHd9_dcN9r9GzWECRcgAIwAuHSuxGm73U8Im5YIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرژانتین در یک ماراتن ۱۲۰ دقیقه‌ای به سختی از سد کیپ ورد عبور کرد؛ گل سوم برای آرژانتین
🇦🇷
3️⃣
🏆
2️⃣
🇨🇻
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666241" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a04365ff.mp4?token=GtA77zTcihsMNUnjaD_IZuZNb05bQmh9nrAkR_U5rX6ya-QQqlTzlWbOftdj1XGHOaG9QxyVDZ6AAnwfYV7gui8tRXb7ET1vCehV3vEaoS7dgc213JrW-bkhY_BjB2yxAoc4aZusvELuP8fNFR5y_OjHp1JBEv3jS8GTgQFPDjaJtg0F7Y0g1iLzdqaPCOqL-qd-rmORLmAsRuuAbn-BQpMN8HS5bAg0Ox-9UF9YbEZjAkpCQfaqhPbcuz0TDZjMuhI8dOB_8hLyhpB8r-0sKkFYlXVpzi1H7TK-1Id22VyxLHvgLT8K5StOYlraKZC1YzeY9bLbhmbQ4UM6y_z3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a04365ff.mp4?token=GtA77zTcihsMNUnjaD_IZuZNb05bQmh9nrAkR_U5rX6ya-QQqlTzlWbOftdj1XGHOaG9QxyVDZ6AAnwfYV7gui8tRXb7ET1vCehV3vEaoS7dgc213JrW-bkhY_BjB2yxAoc4aZusvELuP8fNFR5y_OjHp1JBEv3jS8GTgQFPDjaJtg0F7Y0g1iLzdqaPCOqL-qd-rmORLmAsRuuAbn-BQpMN8HS5bAg0Ox-9UF9YbEZjAkpCQfaqhPbcuz0TDZjMuhI8dOB_8hLyhpB8r-0sKkFYlXVpzi1H7TK-1Id22VyxLHvgLT8K5StOYlraKZC1YzeY9bLbhmbQ4UM6y_z3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زن اهل کشور بوسنی: ما پدرمان را از دست دادیم
🔹
زن اهل کشور بوسنی در مراسم وداع با رهبر شهید ایران: ملت بوسنی تا آخر عمر مدیون آقای خامنه ای است، ما پدرمان را از دست دادیم و اکنون چشممان به پیروزی و قدرت ایران است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666240" target="_blank">📅 10:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2601907e81.mp4?token=CkiVd_J8VpG6-Ci-37LEozs2UU6W_0Wia-k6bbbjWgXk4UPtaHqYdH4JRaRBLcy3IEAhfUpBG6YOKuppvjsGILLQoTBpvsExwErMem8G2nK8KbqT7oFFGaorB--WMdmcUuWxouMZDSfgWyV0GyT3Hpv_AMQ5PmBls8jxAEFSmAVM3xShysn55MeZSYFAq0tDP1rcu6SEwxl0cIl6VrcRCBZQJSiVunFGYs3R6znTAFfxtghNVxh4w6MOMKuZi7i562r5xTIOdmDBhJZunm4fmnWYxCxCxCvzyTYx2G7lPGK-oyt5RS_lItBzTEdfvJZKo1aPyCKqe98SxV2qJityzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2601907e81.mp4?token=CkiVd_J8VpG6-Ci-37LEozs2UU6W_0Wia-k6bbbjWgXk4UPtaHqYdH4JRaRBLcy3IEAhfUpBG6YOKuppvjsGILLQoTBpvsExwErMem8G2nK8KbqT7oFFGaorB--WMdmcUuWxouMZDSfgWyV0GyT3Hpv_AMQ5PmBls8jxAEFSmAVM3xShysn55MeZSYFAq0tDP1rcu6SEwxl0cIl6VrcRCBZQJSiVunFGYs3R6znTAFfxtghNVxh4w6MOMKuZi7i562r5xTIOdmDBhJZunm4fmnWYxCxCxCvzyTYx2G7lPGK-oyt5RS_lItBzTEdfvJZKo1aPyCKqe98SxV2qJityzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم کیپ ورد به آرژانتین توسط کابرال د
ر
دقیقه ۱۰۳
🇦🇷
2️⃣
🏆
2️⃣
🇨🇻
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/666239" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b799a87d.mp4?token=vWA2JtQJPNtuvxUh08m2zZk32DaTcC0yGttJde-Rr02g7rliw_6VT7m8K6TKG2QiwTWgsfq2S7Ylh_wxN5JHcZhUbYpdNidgmef511uvKl5FHc4PUnkcW_VfH12iFZpZMd_3hixb5Eb_G1MMNrEPqmPDEvtfQ2By2BX2Fx66qv8olFi4erAB-VZWRRgBcmdN9fH5SQv-SDCreZnWk6-L8fXtPpXGoq7IGhoz50mHGofgjMz_gNI0FNX_RTOWp3Ua5JpyEwNnma818Tl007zgvRE_fh9YII6hv-1EYDOmIVFI6neuFU1Gk02VJ3mtwqHxCaXmUgTsGl_78glzg49Hvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b799a87d.mp4?token=vWA2JtQJPNtuvxUh08m2zZk32DaTcC0yGttJde-Rr02g7rliw_6VT7m8K6TKG2QiwTWgsfq2S7Ylh_wxN5JHcZhUbYpdNidgmef511uvKl5FHc4PUnkcW_VfH12iFZpZMd_3hixb5Eb_G1MMNrEPqmPDEvtfQ2By2BX2Fx66qv8olFi4erAB-VZWRRgBcmdN9fH5SQv-SDCreZnWk6-L8fXtPpXGoq7IGhoz50mHGofgjMz_gNI0FNX_RTOWp3Ua5JpyEwNnma818Tl007zgvRE_fh9YII6hv-1EYDOmIVFI6neuFU1Gk02VJ3mtwqHxCaXmUgTsGl_78glzg49Hvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌هایی که تهران از مراسم وداع مخابره کرد
/
از بی‌توجهی به تهدیدات اسرائیل تا بی‌اعتمادی به آمریکا و آماده‌باش نظامی
🔹
گزارش الجزیره از حضور مقامات منطقه‌ای و بین‌المللی برای ادای احترام به رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/666238" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ba57b304.mp4?token=MognXGS-H4R6qipVd4dX6tcC_EvfaTOa_aHo4qWPaVH9YS6H8GEtwSTDebQMwbZD3ClvdZ4ndOSEQVEak0J7bUSMXX_bgDIOxLL4YA57Erhm1dfyOW1KDbYM9swmOwzOIRRddL3fAIQl0T2hiLgdZ2OYYCaPiEp-0dxqsGNH7394K3CWMGUWXhK3-KTjb19QrVoRwNScse1pcD4PQMJQauzeOXggdz1agJMWr-1Lne4yBkvxHU5Sehi_87zEtFR50Wpv7Mpxjz38OGjYstr3YKSyPF1l1mPU_eM81drRnG80QT7Kr5ypqcUSAfpWR3GunoxoGu6Q_ooKhWkGhZf83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ba57b304.mp4?token=MognXGS-H4R6qipVd4dX6tcC_EvfaTOa_aHo4qWPaVH9YS6H8GEtwSTDebQMwbZD3ClvdZ4ndOSEQVEak0J7bUSMXX_bgDIOxLL4YA57Erhm1dfyOW1KDbYM9swmOwzOIRRddL3fAIQl0T2hiLgdZ2OYYCaPiEp-0dxqsGNH7394K3CWMGUWXhK3-KTjb19QrVoRwNScse1pcD4PQMJQauzeOXggdz1agJMWr-1Lne4yBkvxHU5Sehi_87zEtFR50Wpv7Mpxjz38OGjYstr3YKSyPF1l1mPU_eM81drRnG80QT7Kr5ypqcUSAfpWR3GunoxoGu6Q_ooKhWkGhZf83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی CNN؛ تشییعی که می‌تواند بزرگ‌ترین مراسم تاریخ معاصر ایران باشد!
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/666237" target="_blank">📅 10:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c2d402b5.mp4?token=jZB8l5qkXOw-qXdLUA8pwyr4Yd1g13JbbOGNuN40jBu0rMj3wLEakOYYrxgyHKyu7NHtfghrfDqe8g_tF8CoakApmxlKIpWL3RYDCrIFdIUZWiIxms2iJBnjVIifJwZmkG9ee453fYPhr7kZpKTb30aCPJGB8qhtDilrmnerYBvU_T9hejAHfDMiDtM8ed7gEV2hVFJvY84YfCoWfUN0LODbNIS2pe1HuYnh-y4qInqbV9cuBjqhYSNridMj5r2eNcEC0AOMVyHE3sbXWbA_6UX7ev5inzY1MgT0kagnOIvFmFVBnCV-ymXDn7z9EobrHwlPJjb8vsRY32PERYaAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c2d402b5.mp4?token=jZB8l5qkXOw-qXdLUA8pwyr4Yd1g13JbbOGNuN40jBu0rMj3wLEakOYYrxgyHKyu7NHtfghrfDqe8g_tF8CoakApmxlKIpWL3RYDCrIFdIUZWiIxms2iJBnjVIifJwZmkG9ee453fYPhr7kZpKTb30aCPJGB8qhtDilrmnerYBvU_T9hejAHfDMiDtM8ed7gEV2hVFJvY84YfCoWfUN0LODbNIS2pe1HuYnh-y4qInqbV9cuBjqhYSNridMj5r2eNcEC0AOMVyHE3sbXWbA_6UX7ev5inzY1MgT0kagnOIvFmFVBnCV-ymXDn7z9EobrHwlPJjb8vsRY32PERYaAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به کیپ ورد توسط لیساندرو مارتینس
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/666236" target="_blank">📅 10:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwLU9CBRgx3xFovO7ZxrIhklBGSWFsA9oqN7CMGVwqbimKZ_-mCSXi307yMOF_32wYKYi6LOFvhwlJi0lITXNrbpwJWBiNzk9y4ZdlkQlK0vb-FEhBqsvYWnxIrEZCl86pZ5Qr2a8mNA5lzj3PQKSwZT7x6LBtTrkIFqN6aJ9P1JC-wRfA1O4dr_PQMyJU6SKeUfKrxvNMmXfy8syaKJi7McDDvTwe4i87903-34j_gXSvf41cWBNoZ5DLb0SCZQfasD2E0QlIoRMHW2rRaRHFkWtcDEPSN0t4JHTitinfs_MfNdLOcjUMy9HBfknBO3f_5_-ku6DYh9DB6NBA22sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/666235" target="_blank">📅 10:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=rW8zjAXfgFh18f8bmTBe0GbKTyzdK1xg7DdpPmS7cptEQ4A_Rh3LMbhbCzwYkT4q2n9_Rf_9a8YRfi2g0hcRFwYGjKbiz95PZlPMamyJeX_QfuC4S8pSTNSxOIBfyHWmPH2pWKy4TURoV5o793_zaTP8r10jzxgvNgHSBRF1lVrbjbT85-kAw0IGYVfV1CGIkNsbfL6Yae7z-A1E8C6kPrVa5AqkjiobGifpC7KtTUGBr4hWz95c7kQ3DyfWTEGJpZ3i1Gtwig5WFV9YtDZI2X9Zy_8OFq22wsOHrJykfO3FB8QF-V2xUFDaIr35hfv4qscDBg--p8Jtm9o4KY_DIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=rW8zjAXfgFh18f8bmTBe0GbKTyzdK1xg7DdpPmS7cptEQ4A_Rh3LMbhbCzwYkT4q2n9_Rf_9a8YRfi2g0hcRFwYGjKbiz95PZlPMamyJeX_QfuC4S8pSTNSxOIBfyHWmPH2pWKy4TURoV5o793_zaTP8r10jzxgvNgHSBRF1lVrbjbT85-kAw0IGYVfV1CGIkNsbfL6Yae7z-A1E8C6kPrVa5AqkjiobGifpC7KtTUGBr4hWz95c7kQ3DyfWTEGJpZ3i1Gtwig5WFV9YtDZI2X9Zy_8OFq22wsOHrJykfO3FB8QF-V2xUFDaIr35hfv4qscDBg--p8Jtm9o4KY_DIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: مصلای تهران غرق در اشک و فریاد «انتقام» شد
🔹
رسانهٔ آمریکایی سی‌ان‌ان در گزارشی از مراسم وداع با رهبر شهید ایران، مصلای تهران را غرق در اشک و فریاد «انتقام» توصیف کرد و نوشت: هزاران عزادار با سینه‌زنی و شعار، پیکر آیت‌الله خامنه‌ای را بدرقه کردند.
🔹
این شبکه آمریکایی به‌نقل از آسوشیتدپرس نوشت: جمعیت یکصدا فریاد می‌زدند «حرف ما یکی‌ست؛ انتقام! انتقام!»
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/666234" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b28c8fbce.mp4?token=TRNspOQL33K-Y3B1ycxXHzkvZaNtZfi69YBKKoZ5VPyOYnUYnyQiM6GcS_n73AgLy3srtp8Ex44N_Zk0l7WablnqoSiU48leDeMxsY7Mz3y6YO-FH8QCmgYaTPKf3jm_o-JvqWBwVg6Cp0_A0q725sa6x49CWxKyd51RSySqRQpzaqeR9R-lU-rDpHQjnWSLIdUBvXHU4zZa6OVdrdQwgfvlvS9qfBUuPqe7daP_6cdcghf8WdNAfrFcPqUUUoFvGBIs9ssRXWzFl894VPvjwH8z7uIvHjv6u5EhqcXBPysrkplD6PQZ0AL0lsDGPT-RbVo4ZT5x66EHvXJmCxyrLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b28c8fbce.mp4?token=TRNspOQL33K-Y3B1ycxXHzkvZaNtZfi69YBKKoZ5VPyOYnUYnyQiM6GcS_n73AgLy3srtp8Ex44N_Zk0l7WablnqoSiU48leDeMxsY7Mz3y6YO-FH8QCmgYaTPKf3jm_o-JvqWBwVg6Cp0_A0q725sa6x49CWxKyd51RSySqRQpzaqeR9R-lU-rDpHQjnWSLIdUBvXHU4zZa6OVdrdQwgfvlvS9qfBUuPqe7daP_6cdcghf8WdNAfrFcPqUUUoFvGBIs9ssRXWzFl894VPvjwH8z7uIvHjv6u5EhqcXBPysrkplD6PQZ0AL0lsDGPT-RbVo4ZT5x66EHvXJmCxyrLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کیپ ورد به آرژانتین توسط دوارته
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/666233" target="_blank">📅 10:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8bed2b7f.mp4?token=Z8XgCK-MHk3rDPZCe_eQvC05gPYmYKRoTXUreZJCBKuvV54-rCB9l7WDmeDBlhQL0bjZs6WT6s_6o9v88ALmtw3XM_f8uKDGrGSzOHa5orDBHkt_4UQHMSm54qDt3leBYigY_P2oDyWEcR8yIY96gxwGAkQDeYiXjNDgi5SoDnYUHOy5Y9CGfy-K8n3vSeSNwfvDnnrxDKtH-TD5XxBrY5AqV-vOyp0J4sUiPHhHEIHyPdB0bGKHchUXVfiuGZ3pXixjJzpFz6015w-mvkgpxcXO4EEfx-gfVgDK3frRw-zi8zjtMgT-H1_-5gZSvemTITEiYkk-AVjRQ9z7S55y-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8bed2b7f.mp4?token=Z8XgCK-MHk3rDPZCe_eQvC05gPYmYKRoTXUreZJCBKuvV54-rCB9l7WDmeDBlhQL0bjZs6WT6s_6o9v88ALmtw3XM_f8uKDGrGSzOHa5orDBHkt_4UQHMSm54qDt3leBYigY_P2oDyWEcR8yIY96gxwGAkQDeYiXjNDgi5SoDnYUHOy5Y9CGfy-K8n3vSeSNwfvDnnrxDKtH-TD5XxBrY5AqV-vOyp0J4sUiPHhHEIHyPdB0bGKHchUXVfiuGZ3pXixjJzpFz6015w-mvkgpxcXO4EEfx-gfVgDK3frRw-zi8zjtMgT-H1_-5gZSvemTITEiYkk-AVjRQ9z7S55y-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به کیپ ورد توسط مسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/666232" target="_blank">📅 10:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4mZ_kkt9pxVur1rCFaX4p61jWhSYqJIqlVy1HRa2BnNpoyPZX7_j3cO1JtJNwYkmRJjZ8jOTkP4uledukUCt4iGXqTuv7Y-7CS1S6Nr0Pr8DwztridM7eRBcss8uc9Ugwe7VxHfDJphmZM1YGqM9z4_YGgRmJbjFB8YuyB3JI9GjjE9AcFEvT9Wie7r923GVxIB13-gfHIBq4Rz9a_1ancuMU3UKlfyNqJyCljTQaKMDmU9uo_6zoSh3LIm60CF4rwYXRqVKUWIG57Iu0wNHj6NVgdPgUcZAdpB5L0PhFd8HGWw_LJv257oa0axjvxPdGXuvkTwpwNuBZHPp59iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی به اولین بازیکن تاریخ تبدیل شد که به رکورد ۳۰ بازی در جام جهانی رسید
🔹
یک رکورد دیگر به نام او ثبت شد و هنوز هم ممکن است تعداد بازی‌هایش را افزایش دهد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/666231" target="_blank">📅 10:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeBSh_WaGxhLHCIo9t8EkETAHsZpQCFWrzXbm7mnQ08AOY0EGLZYIiktecFlK1-aDZWfgEAcwhe0cF_mASIV2lkvrefRQ-gZlMRBuEWQhOFMe977M4BnvM5kZzXmrTKEkKiPk7Tz4WACi_cgOECEpHmU-cKlPAeAEl7g4csbgqfKlllBrMw-WvMwDcg23QQLEVdJ83BNHwbMC13pV1WPJ-lNvUmVzQQIXOKsW0ZCtyXfeD-IEc3hmC8AWM9_MwpGqj9hev98MTH7_lg7xpkI-dsx7GAZ-cAH8Fus_t_YXTSo9a76l_DZxHTz0O2_C1LPuIMblTuxvg_7nJzQlEENtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موفقیت شما بیشتر از هوش‌، بستگی به افرادی داره که باهاشون بیشترین وقت رو می‌گذرونید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/666230" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بیانیه مشترک انگلیس و فرانسه: عمان موافقت کرده با بریتانیا و پاریس همکاری کند تا اطمینان حاصل شود که آب‌های سرزمینی تحت حاکمیت این کشور، برای کشتیرانی ایمن هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666228" target="_blank">📅 09:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFyL_71i-LRduc0jJTwY01s5hM85unn_KBzvxC4NinLwbPA1vHICn1KlF8lIx8rTIdxKlnOhFXzJ0rrzEpKPhA9sKPJrnarH7LUC45wa7KM_8n593D2l7ijxFvDPBR2M3ZkngVzkVXmuAiv1na4o0J652YR4kYN734nS5JT8WlTysYa81yHZ7R_IRkiAzAqEHoDKZHxdE6XpMiPjDOKkclNYpTQM23QDLO_AsZDDiQu-cqNb-wMhAe2wDNTIZV2Ym8k5BI7mF00aYurexbjpeMaYDSqp58vIb4DomWOzjgnrTZK_DKKFFMwATi4Lbs1BlTJNqRupxvQdy-vr4rlp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تابستان بجای آب، این نوشیدنی‌ها رو مصرف کن
🍹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666227" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666226">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2a46e92f.mp4?token=b75SW2rvEbEhJ45v3PfjbnOG_Fag5FWQY_RTn_30RYp1MrRvZWrSs0tc5cRjIVk8ZWAsXeBipZFlK5Yr0nyE05JwMdBoy-MnGK01CZNKS11Akfhjq3Sc_5FcY-nnPTpTO0Y59CtFF-ZEvDdqYnu6v0WXeNHzlo2QFvsadN5ZJfjNUC_ggxHBum3tEoJYcrAXS5Vfb0L2eXXkjgE1c0AfBezLv0oRDeZjwVsocd4nf39yeo1UAnDapTyKRnJwwyiBhlWwwFsihY1Kqq5L9-_pj9bC6zNtm1-YHnZT4Qngwb-qdYo82P3Yz_tVekbEonARbLE0b-RmEVCrZQ9XkQHAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2a46e92f.mp4?token=b75SW2rvEbEhJ45v3PfjbnOG_Fag5FWQY_RTn_30RYp1MrRvZWrSs0tc5cRjIVk8ZWAsXeBipZFlK5Yr0nyE05JwMdBoy-MnGK01CZNKS11Akfhjq3Sc_5FcY-nnPTpTO0Y59CtFF-ZEvDdqYnu6v0WXeNHzlo2QFvsadN5ZJfjNUC_ggxHBum3tEoJYcrAXS5Vfb0L2eXXkjgE1c0AfBezLv0oRDeZjwVsocd4nf39yeo1UAnDapTyKRnJwwyiBhlWwwFsihY1Kqq5L9-_pj9bC6zNtm1-YHnZT4Qngwb-qdYo82P3Yz_tVekbEonARbLE0b-RmEVCrZQ9XkQHAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو رفتی دگر ماه و آیینه خداحافظ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666226" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
انا علی العهدی
لبیک یا مهدی
🔹
مداحی محسن محمدی پناه در مراسم وداع با رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/666225" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8b6eak_Gq-MmiH7f4ZItN5zF90EZVKAAeQKvf3nmeaEGK7klpNtGwGg653H53HKpMnMAQrSlpjIpYBLtQ0k3V4u4bLCz8yRigBglJ2BLdeobCfswi7YP0_y24SQKYfI0WgA7li_aLuKDyNYhgJl8lS87_Y2PPgJy-guADj5sdAb_XYuZ_7p3N6GTvf2p5PZG7ZsYkTT-XCiaWVathkpFXedrx1XwzMKKONDY1Kk9c0TS57Fy2A1Ts8DoBYK6LFEykfVXkIylkYQTUSHmM-a3gDiwERQ865HyaI3ektFpvVW6Um10ubs86KaQ8kn4wBBhaTmSjB8DPXyidfEON8QEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toLZs8Szia9A_xDSJd13M20bl_lZYDTc4wlKR5y_f0bR-jne5qRvM5C8_ohDRcuOiUYBVPNKZ6Ye1Y8rPZCFzHPNELasyI0HXINx1oes16z9g8PGHhVa5zKDaYG2HoDLICEbkHNIa89MNo9c8jH52sdt3ECSi2g-uRorRyS9j9DCZ1-RNkte8G8OjSxLGYH48auJScAzI3JHNXxSQ5Na502izzkG8yGMA63sosyw7T5ZCvaphSEYp195xpXtoEpG1jP19Lu0n7Q4t7vNCZGvkChuyWzKnMMwQu8hHyYRCQqRr_rxhDsVmh_qUwq0VMJ9Mvy1pqHvOPXs0NtOfx9YJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCT8IWTMrNhozRAARJefWMIuL3xAkfaEvdDrK6ailKzNrFg42VBsPFlAsxlnhYPk1ik4Ms3G-3_4-V25L6zh5I7pzxPqX-NA7VxcPyv3-iZaojhGsMG4gbzZaTWFMV2yrVVdefYip2jq64jqzWOrzI9nbFnrfhNusvovs3hetdRHWjYwsQssv5uUjzAbaBlYzdWE7CXbWTfqrXLFWAdWljdbVifI1_6CK0KZO26bN1tDaHx4-0QRL22kN1HG3gHeq0BPAgF2FyWRk0yqdC8XDiTqm5dgMoDDJnGOBXXunxusVynaOeiuCGFbS6iE1vqez4xvOxdeGPtCgkPi1UM6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB7wml_HshNabYSrBFheZIO0yqciXIzM91s6kuaeIL7SiBUUhZUxp0lfPvaXRKUfSXPBc-20fXp5fYaCDcZ6otCKV0QY_CseDriZWIcUEy3IjIlVNI0Ok1s_Apgsp_fxBvSVrzoIFbwoKLi-55peD3SpabB4zEe1Xf3Sx1kSmb6TrJmF9MVsGW4vud6n_R4ZJItnLteHdXzxfP6Rhwih_13rQ-NBTp43zfRbQNAWXMH29JSz4cJeOMs4yPhT5sQlJ8vUUFaiLfzKCY2j_DkZ7ik5xIL2CLxcFsXy-c29zP14N7fpNwJ4TOy6jCeGHF5eTZMEwaldwyKLP7M1mAOKMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98adf9726.mp4?token=BYnKTwvSJ8XXHefJnONAK-Y-zVtfoPWyUNbj_vDJFkKR9PIK0FtZZHMNcEjxDRaMUuRQmdDf7ghzcWbrRZfiitD27jDjVlM6P-hvM9x7YDduwXxiDPGqUNStyhl356e7L7LDa-1WzY15RSbaz8WBA7Q0KUTzi5pFik_Jw3auAE4Qd1PU4CNSLJg2GNRql5NP_u5lSRYAThp5NZSHIsluky0KTaAHNw8N6vz1hW31Hs8MN1upwmyD6sctIhQRI3QpgaW43bIyX9Wphg3swDIVqFYdfqMZNITeGCm6ma_6sCgqm6KY3CbKeBWrVqmirNM4X-6BIUegVsgMpihkAe6Llz7f7aNCCZZcLvQbKxB1TFARvg3Rq6Gg4GmvC9n7dHTVB_1FHWOQx3e-T3pr4Cd-GDEclI26h4-4QRJsOJiubgETY22T_MwM-a46ZUN5dFUiseTMeRg8SVJXHfIygHUUT9kWeUjWv-XpP1828cLzKfI6ixM49ztlmcaHzZtzb_tRGCDYBczzoblsaVtWwjb4b4RCv2CljM3_gAQ4qdHPGFTWAP2rZUOld2RoqRtAbFtxu8O_yOumrAvU6b6IpdmeHeYdfC-owATKdLX6W3TkZNfHwodEe_CGpE1IFEbrsPGSbdXnfQ3bGz39MxeyZA7IcbDj_UDqPk536Q3gYFxV47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98adf9726.mp4?token=BYnKTwvSJ8XXHefJnONAK-Y-zVtfoPWyUNbj_vDJFkKR9PIK0FtZZHMNcEjxDRaMUuRQmdDf7ghzcWbrRZfiitD27jDjVlM6P-hvM9x7YDduwXxiDPGqUNStyhl356e7L7LDa-1WzY15RSbaz8WBA7Q0KUTzi5pFik_Jw3auAE4Qd1PU4CNSLJg2GNRql5NP_u5lSRYAThp5NZSHIsluky0KTaAHNw8N6vz1hW31Hs8MN1upwmyD6sctIhQRI3QpgaW43bIyX9Wphg3swDIVqFYdfqMZNITeGCm6ma_6sCgqm6KY3CbKeBWrVqmirNM4X-6BIUegVsgMpihkAe6Llz7f7aNCCZZcLvQbKxB1TFARvg3Rq6Gg4GmvC9n7dHTVB_1FHWOQx3e-T3pr4Cd-GDEclI26h4-4QRJsOJiubgETY22T_MwM-a46ZUN5dFUiseTMeRg8SVJXHfIygHUUT9kWeUjWv-XpP1828cLzKfI6ixM49ztlmcaHzZtzb_tRGCDYBczzoblsaVtWwjb4b4RCv2CljM3_gAQ4qdHPGFTWAP2rZUOld2RoqRtAbFtxu8O_yOumrAvU6b6IpdmeHeYdfC-owATKdLX6W3TkZNfHwodEe_CGpE1IFEbrsPGSbdXnfQ3bGz39MxeyZA7IcbDj_UDqPk536Q3gYFxV47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع در نروژ همزمان با مراسم وداع رهبر شهید ایران
🔹
همزمان با آغاز برنامه وداع با رهبر شهید ایران، گروهی از دوستداران جبهه مقاومت روز شنبه ۴ ژوییه ۲٠۲۶ در میدان "گرونلاند" در اسلو نروژ تجمع ضداستکباری برگزار کردند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/666219" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f01cffa58.mp4?token=NJA56uAZoRYGFJmV9P_MrYpEvVSYbtcbww7ba8tzukSCr-8jL3SaHPMIldK_ih7XxgUkBzzsqw-ueeTWTvJ-XufzA5qS8nlFI6gYLGFOIz2WLvT5Xx8M_G5lNQ10k2G5zlmz_eGk44IDJhZIUNWYwYzAvrr9ezssK5oXgGZZ6U8LdT3W_JOiwNH2gpF-YZfj_DcFYXZQ4rQufZqc1E4mMujmchsWP3MGNQVT8et9VYYlzFYiZL_S0T_5SUzkV4g_ILLFdR1B0qvdj7Grv0JDnEf6CaY0TXmA9NNium9ITThLfPiBj-nBxYqfC362P3L3-L_Zrvuj3khSbV1K8ZaPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f01cffa58.mp4?token=NJA56uAZoRYGFJmV9P_MrYpEvVSYbtcbww7ba8tzukSCr-8jL3SaHPMIldK_ih7XxgUkBzzsqw-ueeTWTvJ-XufzA5qS8nlFI6gYLGFOIz2WLvT5Xx8M_G5lNQ10k2G5zlmz_eGk44IDJhZIUNWYwYzAvrr9ezssK5oXgGZZ6U8LdT3W_JOiwNH2gpF-YZfj_DcFYXZQ4rQufZqc1E4mMujmchsWP3MGNQVT8et9VYYlzFYiZL_S0T_5SUzkV4g_ILLFdR1B0qvdj7Grv0JDnEf6CaY0TXmA9NNium9ITThLfPiBj-nBxYqfC362P3L3-L_Zrvuj3khSbV1K8ZaPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت زیبای رونالدو برای پسربچه‌ای که همه‌چیزش را در زلزله از دست داد
🔹
پسربچه‌ای که در زلزله خانواده و یکی از پاهایش را از دست داده بود، با پیام ویدیویی کریستیانو رونالدو غافلگیر شد؛ رونالدو از او دعوت کرد تا یکی از بازی‌هایش را از نزدیک تماشا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/666217" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666216">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ade56c25.mp4?token=Ss4mj_hftUYoO2lHP6Jn6XPF-aiQzYGNh4KtLDl--wlTgxm7l1EXEz5DtspIEVG5KlGb0xE0IZvU6S6dYgQZhkBuDSQmAHxWBu-YSqYMZDIZVJeith6oPWpeJKFoJmrcHGkkz6cGyhTe7ZL7OGmekdleBSvjB9q7szSd7GriX8pGjl5Xk2unUH-R3xAPxsmx3JOo4Cy9sc5FMzajVT9KtqUrJvTxMkQMAPwJoS-nXHej-0jSKTvcNLtIKxoB2OxAM2Up5pd-c6XybCYO0o6dDgs2cMJPsy5G0XIxlouNX_3I-BYhQ_UD_dFryF8XOysGi0Q-3rS-iof6m0idT9ZOgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ade56c25.mp4?token=Ss4mj_hftUYoO2lHP6Jn6XPF-aiQzYGNh4KtLDl--wlTgxm7l1EXEz5DtspIEVG5KlGb0xE0IZvU6S6dYgQZhkBuDSQmAHxWBu-YSqYMZDIZVJeith6oPWpeJKFoJmrcHGkkz6cGyhTe7ZL7OGmekdleBSvjB9q7szSd7GriX8pGjl5Xk2unUH-R3xAPxsmx3JOo4Cy9sc5FMzajVT9KtqUrJvTxMkQMAPwJoS-nXHej-0jSKTvcNLtIKxoB2OxAM2Up5pd-c6XybCYO0o6dDgs2cMJPsy5G0XIxlouNX_3I-BYhQ_UD_dFryF8XOysGi0Q-3rS-iof6m0idT9ZOgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رمضان سال ۱۳۹۸؛ ویدیویی وایرال شده از دعای رهبر شهید انقلاب با حضور گسترده شهدای انقلاب
🔹
در این فیلم علاوه بر رهبر شهید، قاسم سلیمانی، محمد باقری، سیدعبدالرحیم موسوی، حسین سلامی، محمدرضا زاهدی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری و مجید خادمی حضور دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/666216" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین | فصل‌دو،قسمت‌شش</div>
  <div class="tg-doc-extra">حکیم خیام</div>
</div>
<a href="https://t.me/akhbarefori/666214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
حکیم عمر خیام
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «خلاقیت‌های متقاطع در کسب‌وکار»، «مدیریتِ فرسودگیِ ذهنی (Mindfulness)» و فرار از «سندرمِ اضطرابِ آینده» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666214" target="_blank">📅 09:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25918ae43d.mp4?token=HtbWoIi1z66DGU95ISmIldsiE6VOn_IAX1m8E9SAH41gPC0jZ4ZTAG05gxiS3Zu4_7ve8Osq47Oclo8ZSvdj1WU0yegg8c3H0g4GkjxV_rVsix8VUy6s3MDwn6Z_jizRLRWD-4NE1SRB_bEiP_pjMQXBYuX2ESECk-gEkeOO3MWzFcQl6wba9HvKsaRg4q46pKcHUrVIgRlnZQ6fi3WUL6DVDBVDhhVzbdtsnY3BWZlc_DTJYGmSz6GPYLQze0W2p2K1tyfrfn2jGdC_ir76qqHiZN_G0dPReD6yxzdXCFRPb7y2Q9d2fCVdhRT4Hjkessro0oxH_NGOx2yo0Crv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25918ae43d.mp4?token=HtbWoIi1z66DGU95ISmIldsiE6VOn_IAX1m8E9SAH41gPC0jZ4ZTAG05gxiS3Zu4_7ve8Osq47Oclo8ZSvdj1WU0yegg8c3H0g4GkjxV_rVsix8VUy6s3MDwn6Z_jizRLRWD-4NE1SRB_bEiP_pjMQXBYuX2ESECk-gEkeOO3MWzFcQl6wba9HvKsaRg4q46pKcHUrVIgRlnZQ6fi3WUL6DVDBVDhhVzbdtsnY3BWZlc_DTJYGmSz6GPYLQze0W2p2K1tyfrfn2jGdC_ir76qqHiZN_G0dPReD6yxzdXCFRPb7y2Q9d2fCVdhRT4Hjkessro0oxH_NGOx2yo0Crv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکیم خیام و تفکرِ چندوجهی
#پادکست_کافئین
| فصل‌دو،قسمت‌هشتم
☕️
🔹
ابرنابغه‌ای که نشان داد چطور یک متخصصِ تراز اول، می‌تواند از قفسِ تخصص‌های تک‌بعدی فرار کند، دقیق‌ترین محاسباتِ ریاضی جهان را انجام دهد و با دکترینِ «زیستن در اکنون»، اضطرابِ فردا را کیش‌ومات کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/mxf2h48
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666213" target="_blank">📅 09:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee473a0fe8.mp4?token=ukO-U8DRIl93oOmAo5AdRcgpZU47jefLWxK87Ac_EYrV-qt60uVT8VGFJETauRDduM_xkp-d594KLv2KgeUpcQBUzwOUb2wrb3w7bzMCj6-qRGvUa88yUrG0w-aCUVBZyN3L407EsD6DCDp_WAti6ltNUN5CUABYNInYEb8detPXL4JEcMVRK29aT2lw-pyj1JmHATP_r-XdVemFpej_VUHrIFqrtFxT-rwQSFyeqe8wPPecspmhXN1tGzKWUWC9b9YNVIVuFU9P9ca9ZPdd_zQAIOuVpiPJ4ylS8w4G97XfFYXME2ninSrQkj0GBYxV70dg1qISXD67sl27GIP-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee473a0fe8.mp4?token=ukO-U8DRIl93oOmAo5AdRcgpZU47jefLWxK87Ac_EYrV-qt60uVT8VGFJETauRDduM_xkp-d594KLv2KgeUpcQBUzwOUb2wrb3w7bzMCj6-qRGvUa88yUrG0w-aCUVBZyN3L407EsD6DCDp_WAti6ltNUN5CUABYNInYEb8detPXL4JEcMVRK29aT2lw-pyj1JmHATP_r-XdVemFpej_VUHrIFqrtFxT-rwQSFyeqe8wPPecspmhXN1tGzKWUWC9b9YNVIVuFU9P9ca9ZPdd_zQAIOuVpiPJ4ylS8w4G97XfFYXME2ninSrQkj0GBYxV70dg1qISXD67sl27GIP-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما بعد از این آشفته خون امامیم
ما بعد از این زنده به شوق انتقامیم
🔹
شعرخوانی احمد بابایی در مراسم وداع با قائد شهید امت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/666211" target="_blank">📅 08:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666207">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_PJHDvXhB1K4H2Sff9AKE6dOaVi84GFQAHHUGjvMmHaZlorQMkd4v5kVwT0OsEGPs2KjmSJ9lvmsS9c_VGejBLl9Geqw7CV4_-eHBJyEdhi2unj9QiSzsXNgRkPahq6Xv23eN4zZQvRwKZaGAPg6GEKxuVBAD--SirMSQn5iuA5Fxo_QkToLqLnUpE1EHaEHHzO8MXGnLfx5QWdKSUnp5SXj-ijZPXKLj0Kchs5j5OROEgcrXz8TY1z_53V2TvMZy3pt3uF9phFgSjpI22ul3ulBlGluEsJUBChmUFuU6mg3fswH454dIpqTRZIDvYZcMhXU6NEgw4dPqJUmI58Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gq8TXfixi_vjJBp_kXUD7v_pNo2QE_e-B9uDsUow7OqiXVIL9ojCC77aES04cvzAWvuUJsqJPnHxiTGJnBl65CZNY2sFVeuyUfZID4Ncw1SJJzb3S2LibjDCGIWZW66srXfutJoCasHu7yC6fC_ODzACNxWoK0pfRfjZpIgQ_jQqoaKWsHa9lNtQO6B2GU3C28-OuS7TYmAzuaIKyeugI1NFY4QaOt4MneiJko3i91g-Eg8KiuYo1fddgdI35m4EBxAAOdExQkdO7Uyo9AkN1cCEQ43XoUhyB_Bh-AuHfQ3qFULFkmtLhKqTKiy7GzxfjJgkH6G08kkNXasnYZaBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOcBgtwM-CeLMvK7paeG5Cpd9bsr0lVfXfAibWfn1MbuMtlHmShmXaaIbHOnsbPU1XTOx86Xemo_4nzJMZg6SoDqAIvsNLkXzBwO7r5Zz0IxA8QUE-AGkrqC3iNYJ4ZOupSKcTcfkXftu0kYgvcqTnVtStos1rEA_NTTiQfrjrgyMWC7EpAjNVP-1RpuqUUkHFZX718jA6-9EKGIA7zYts7ZnMp2P0AOUsepzz8grPFC63qFl9EO_1mOeiGuGnaUryuw5Rti54E-1X8WqP1y_cCwnuEciNtPEYI5i_fzGQ_DHHAVij_gdZLM_tletgw2Q6jKj7B1Q395lxtBqAa2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzSXwgN6j9oSU_XVYcegDgPKOxkLgLjZMWl60OyjxJQBNnHTVAoLQQLN61YnCPJzOY1OLUpQ08I1ziztIpbf-TefGGbFhLwFORZMu22xLGYZBE1Fm-R5We71yj8-UTikCJ8yaY6uyXXCVldzChKLodwUukOAhzlao7ah1lpiRw7zU61htldokQ4_lnLxLiAme8rlbLDtexeU2UnWaffxdDLDe4Xk5tBTttRC4XTMIQO2sjL4YGLi1VYnulzIWJ62bBTNcdM8x93MVv9XinaeGOCyDy058rI2fT1S0v6Gk4fpSarnWSaDGaYDNaI0QjKxpLOeUf0mJV-83QnZW8vh9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری
مراسم تشییع نمادین رهبر شهید در نیجریه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/666207" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یالثارات القائد الشهید
🔹
شعار خونخواهی مردم عزادار در مراسم وداع با «آقای شهید ایران»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/666203" target="_blank">📅 08:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meoJgnJSJYYqDoyFqSYszi1M8iMkl83G5xCYZ-6LVGzknqLL7_6FVzgd7j5qltgCXGyemMbdBIufNa6Cvuoqmii2hpJm7gRaL3OG6vCOa3G5kZBiDDBxQTq9ByLxIAF_dp8tg1r_fXwkgIgaVz9VuaeBDpCKlUiGMlCF6co-HRrAJoGxDpPom1tOlBJJGWXuJ19wR6f44dGKeB-isXHXQI8RY0woqV3Puq19DxaYg1r2Itz6RiacN9TI0doKl_bp7h86SDIvnr3F1y5FOpTjeBpxrw9Yh8fnEGinI-A9R5Ythb71u2p4FrEQHr8SI0lLAMFhhV03gziz42cV3_2LdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم کشتن ترامپ در مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/666202" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاشا، در انتقامت بشود کوتاهی
کَلا، زمین بماند علم خون‌خواهی
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/666201" target="_blank">📅 08:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666200">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032448e94a.mp4?token=mA8qYJXYcm_54_FBG4IAfvgTyLYPeNoAQblvANHUTKviWGgiTtUXJemjFvI-u-uumV9OBlqCex3KMLma1T-iFH77dJCoEY3_etbvL-tkkooyt2qN4ow5MyrHaUkpsh5i6z3771IgVOvDKh43l2X1BSF82BuNBNd8prnK_J2BKu3wrX_CrzX4AAyU5jpT049V3ayX0A_O-gY_FynDk2GRISY3yBM6w_DOY_bYXzUTsAtrhOvmYWMETjozXhXdi92wgbk1MJIw_3GO2iXPinoOezEjNrOfEVLg7vgyKCw7gR2mP3uEp4g5zDZrnqHZ-5qEl8l80cb4n_Rp8dXkSaAL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032448e94a.mp4?token=mA8qYJXYcm_54_FBG4IAfvgTyLYPeNoAQblvANHUTKviWGgiTtUXJemjFvI-u-uumV9OBlqCex3KMLma1T-iFH77dJCoEY3_etbvL-tkkooyt2qN4ow5MyrHaUkpsh5i6z3771IgVOvDKh43l2X1BSF82BuNBNd8prnK_J2BKu3wrX_CrzX4AAyU5jpT049V3ayX0A_O-gY_FynDk2GRISY3yBM6w_DOY_bYXzUTsAtrhOvmYWMETjozXhXdi92wgbk1MJIw_3GO2iXPinoOezEjNrOfEVLg7vgyKCw7gR2mP3uEp4g5zDZrnqHZ-5qEl8l80cb4n_Rp8dXkSaAL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: «ایران می‌خواهد به توافق برسد؛ آنها به شدت مشتاق توافق هستند. ما چون آدم‌های خوبی هستیم، به آن‌ها یک هفته برای مراسم تشییع فرصت دادیم.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/666200" target="_blank">📅 08:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666199">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌صدای «لعنت الله علی اسرائیل» مردم در مراسم وداع با پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/666199" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666198">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اصلاحی تخصصی برای آرتروز لگن (hip_arthritis) #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/666198" target="_blank">📅 08:05 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
