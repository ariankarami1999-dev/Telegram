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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 02:32:45</div>
<hr>

<div class="tg-post" id="msg-666166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr8wvGm6M_NiWOTQvFSnkwl0oA6b4e-BaBhzpE3Olo8LfMC4iJK7hmoz_wRB63FnQBh_V4XHtkBdAOc51HyjkWrNRl4nqPlhbfePNZYyMntuqnwWFk6mQfEP0vlANQenMvzSym6jHDZSeQQNU4MA-UMuCGYrfV0vmEFE7Ya6oTh4EhkSu1xB7m5A3UOn02g2d9k5_UcoTbD8DbaXdYX1WSw0AljPjU-zGhAGty6Re5AhHTjWuYiRfKBYxXM_a0d_jUBC6kBAvVjQgAP91_spMOJwlzieEzxXPNCVmXFrM-9svHORdFGLWNZ7atj2fPnAztcYGZvB8ZaYC0bzC2boRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مسدودی خیابان‌های منتهی به مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/666166" target="_blank">📅 01:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میزبانی از دلدادگان در چهل سر، محلی برای استراحت، پذیرایی و خدمات درمانی عزادارانی که از سراسر کشور به تهران آمده‌اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/666165" target="_blank">📅 00:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgjxVjvGw0GsbL4ahmi3IukMcVF_hrKpFJ62PaOF_6aRrdBNxu4PH2ABX-7E142NQrzbn8liz6sU3BIzKs9EwRMD4WTRtF5PKqkzGebqTGY9TBGsgLJhD8p7JmdrY0JR2XHxgFDqO_1_SlcPsxEIbSlA4BBsnc9M9eCZPI5-cMnovrRJcSTPS2Bo2onTKhGJER4EN77OvqIgF5n4iv8C9OZ5h7-9dPrBvKW6almtn90ugfFHKkPJwDCrDqzue8fUWrGE7hvCcGgLtKJOnrDVs_3fVUBO_bbI1RoAJkSdxcdHZT5fPxdOzYtrSUS15T3UklKPXAE4ZG9VcXpDEHPv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های صعود کرده به مرحله بعدی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/666164" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxoL3poJaa_wkICiDJeaEQ_KusXJYags5mbuDYmBs-XPW1pqUeT_rRh6xD1EyAC5nk_0oD3RxHiyh26yz6gaYOIlng_rZ8666NlOpyyNFVpHrcsx0-O5-Mawfcz-hlk4kkkbMpoPIfiVBbQeh3ZaH6-3tnOmapxoA7LGJ96lGePqBnY2JRGlk4Du2LihkjshtausXhux_M7HAAn5QwDnPrxS5qJcrOq4zA6MOB55FL-9yG3KeWLQEhG7aY9_nRnp3JEY3YYoTSRn8mYC7eNvEytWFsUJq2rFUpqDKFDy6NNq0UVkpQ6vMnMxa4en1K2CvCGlIglFZ4GTe6o8sUe5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد
ایتن لوینز، روزنامه نگار و تحلیلگر آمریکایی:
🔹
به‌ معنای واقعی کلمه، تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد.
🔹
روسیه، چین، عربستان سعودی، قطر، صربستان، هر دو کره، ونزوئلا، گواتمالا، گرجستان، ارمنستان و کشورهای دیگر.
🔹
کشورهایی از همه قاره‌ها و با پیروان همه ادیان گرد هم آمده‌اند تا در برابر امپریالیسم آمریکا متحد شوند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666163" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
خودرو شخصی به مرکز تهران نیاورید/ برخلاف جهت جمعیت حرکت نکنید
سخنگوی سازمان آتش‌نشانی:
🔹
از مردم می‌خواهیم از آوردن خودروهای شخصی به داخل شهر خودداری کنند.
🔹
مردم با استفاده از ناوگان حمل‌ونقل عمومی به محل برگزاری مراسم مراجعه کنند.
🔹
یکی از حوادث رایج در تجمع‌های گسترده، گم شدن کودکان است و خانواده‌ها باید در این زمینه دقت ویژه‌ای داشته باشند.
🔹
مردم از قرار گرفتن در کنار ستون‌ها، موانع و سازه‌های ثابت خودداری کنند.
🔹
به همراه داشتن آب و تجهیزات محافظتی ضروری است.
🔹
به هیچ عنوان برخلاف جهت حرکت جمعیت حرکت نکنید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/666162" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو دوست داشتی با این شخص دیدار داشته باشی؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/666158" target="_blank">📅 00:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or5Dv8cH9QZX8LfnocpWc3yH_wWVmSrcsPVN3uRyfDCcldMLKr8HZ2nqExsRwHgj-BrPWLr0ggyNqf3ZpTkuPAk6epWaViE9_8_2Z_83wcxH7lL5b1bbclIfr1PiRkLReldKbH9R2o1xBqf4Yrj9Q7A_EkYXVudtmQKcw9Lmqq2SFHCJINcwuz2-YJY1bOvqvDJnRLt5_TtZI7Sm9nt_SwYQGftff6iEauyti8rQ5lhjq09nmKQz5XdsoNUBYlLloUwLnWQnkwEdc49Gu3-pJtaaiqCGu9kbHEC1nd5qfV6JkcQiqUbXrU3Gj-jwUihldBgJTewY6bq_xJNjTUO2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مصری‌ها در ضربات پنالتی صعود کردند/ آخرین نماینده آسیا هم حذف شد
استرالیا ۱(۲)
مصر۱ (۴)
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/666157" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه اتو زدن پیراهن مردانه را یاد بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/666155" target="_blank">📅 00:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع رهبر ایران می‌گوید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/666154" target="_blank">📅 00:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی محل استقرار پیکر رهبر شهید برای مراسم وداع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/666153" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpAQDV8iIlxzqrgp--5m8KONF-PZuYq9KyX8WXuPxyygJTKdEqFuFsxZnGR7YTcOAcm83g1JawRlTUHKVXvLZhN4aiqpw-tgvrrytAGOdAJhFIw4p1irDouv67BYobROFpkynuwcq-4maVnl5N4vy3uwgNOCorHfO5oXbFmFXEO9s2ZJwOsNWLpBq5YK_PzAhxP02a2gB68yynaWQ3IoJ9cHoB7RKHm24GLAgE2uY6LbUrN2tJq3VKEJbx_pHPUIFy0II9pYJel2HfpA-gE1mWgVkZKYa4IyUQzrcdSa5qaefoO3BovuBxsEipFrmpIP-9nL7oCdXgkGapX6hYxo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد هانی در تاریخ جام جهانی رکورددار یک آمار تلخ شد
🔹
محمد هانی یک رکورد منفی تاریخی ثبت کرد؛ او پس از ایوان ووتسوف، مدافع بلغارستان در جام جهانی ۱۹۶۶، تنها بازیکن تاریخ جام جهانی است که در یک دوره از مسابقات دو گل به خودی به ثبت رسانده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/666152" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گیلان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب رهبر انقلاب به ایستادن مردم در زیر باران در هنگام سخنرانی ایشان
@akhbaregilan</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/666151" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2uE6nKR_5d7NPdPI4adzh7wdkQ2RQpyCGBlzbSlQb2_1tft7VdMWos8meOAlDkFdq1MQrUIAqdWNRb871STSoC8sw4PVhk6BE-nL-jA0oDzRupceNFQuT_bAVeE73PcW0A-oP6WjE2pU99D6FoJGOTXoGHB8cL5OhS4rPiMRtWz6KlpogkPMRUJdkrec8Y6QpaptiMVdllbd0PFMXxIFWMklnAZfz82wRIauMIKas4Ugh4shkK0sUafM8Qg_PtsybOmcOPTVMDB3dq-mboZNeE9tdOOWY3zRZsGJm9ImMvXZhXe65Ur2XrHOujaohoKv5vOmXutRsUvvwZxx2tIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرخی این مچ‌بند، یادآور خون شهیدان است
🔹
با مچ‌بند سرخ در مراسم تشییع حاضر شویم.
🔹
تا عهد خود را با راه شهیدان تجدید کنیم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/666150" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDX99QrriDJxfMjkeCRq06vYk1JHdTo_jltSj4rHUSkL2zrgsxN9ffDe4OBdaKgFb5W9-0AwP1-KE_e-dyB-mghK2DuTHC1eiPVGMLH6-3y9ECC2ebnWDCSvXuLGM0Pg-1zXRNgC6SK17g5N0onHPI3ZW_zmEFbtZBivxWMwG0fLn_hCpfoCzOOUr_L8duj62STFx4FFdB6OIx9QKScjsR4R187wcLIHKxQUypnZDin99u_jAxcO9L8HE2ZqdxT61usSmmn6B5F4u97F7mi5I12svoDjXAAJ6qsm24-pi7FSjklcHRpPDaqQNZPBiQtF0JqDWXUE2sPEtLqWU2VPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/666149" target="_blank">📅 00:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L677KhVfKJ4cyUOCskcyEy17UDu2-xz0YmYYtm_uuz3cP9Bs5K9Zl_GWx-HOUj-XlalRF1FQCSZz4yHal_ExXSjYKVLG7PTOGMnJTilKfxNvOrlylkKGmHV-k1lcOZ8oyQwmCvB7csvweHYCO-5NWqgGXnv1Uqwv5dkFlULYRadLjdXBWHLEKthK8QDhle4n49OWFwygp_h2xE4yZ2goz0tF9NvimkCLLnVBhZE-uUti8KS4TFABqfLoo2JCpqzg6iSXohqBCcUFQ55ajD5W-V2RagpaqLZ2VpiX7iyIM3Ds0U46mzSfYFF8PpPDxLz5TPgYlfHxNPuOYATBA7f3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا به کانال ۱۸ میلیون تومان نزدیک شد.
📊
بازار طلا برای دومین روز متوالی روندی صعودی را در پیش گرفت و به آستانه کانال ۱۸ میلیون تومان نزدیک شد.
مشاهده قیمت طلای معاملاتی در میلی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/666148" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
امروز در مراسم وداع با پیکر رهبر شهید انقلاب چه گذشت؟ + ویدئوی کامل همه هیات‌های خارجی
👇
khabarfoori.com/fa/tiny/news-3227494
🔹
ترامپ از حمله تازه به ایران خبرداد: رادار جدیدشان را دیشب نابود کردیم!
👇
khabarfoori.com/fa/tiny/news-3227444
🔹
جزئیات اتهام‌های متعدد جنسی علیه کاپیتان سابق تیم والیبال ایران!
👇
khabarfoori.com/fa/tiny/news-3227506
🔹
مدل جدید تذکر حجاب در تهران + عکس
👇
khabarfoori.com/fa/tiny/news-3227466
🔹
مجری مشهور صداوسیما تغییر جنسیت داد
👇
khabarfoori.com/fa/tiny/news-3227473
🔹
ویدئوهای جنجالی را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/666147" target="_blank">📅 23:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bc6f80d9.mp4?token=YS9PpWERBOgB_PkLWK2GEMmSZMxCarW9W6l8O898spFHmVqayAIZDKLsnrn6UH4pgd3cVoFUiYd2GP4NyIovuX3xR_l8Gw4TVS4je1Wy9XtUspn_zHctwKw8yMK-Lg09pvfBDrAeABEMeCQcgihEr4FpPAAuBYh5Zq-YeSl3XhKVOjy22i3Z69glCPiuZkA9SatROWm7Q7wlcBXuwSB8VoQNaXXbUAKZPKcanL_7AHCLmbyhRMmIh3XmO79c1GbHwH0z8NfNY2HWhPMNpYMHVKvGMIv6dOllPVaI2721zGx3uFhUwcjGDTMxFpBA1M1D4lcOuGalqxEaiO91cnjcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bc6f80d9.mp4?token=YS9PpWERBOgB_PkLWK2GEMmSZMxCarW9W6l8O898spFHmVqayAIZDKLsnrn6UH4pgd3cVoFUiYd2GP4NyIovuX3xR_l8Gw4TVS4je1Wy9XtUspn_zHctwKw8yMK-Lg09pvfBDrAeABEMeCQcgihEr4FpPAAuBYh5Zq-YeSl3XhKVOjy22i3Z69glCPiuZkA9SatROWm7Q7wlcBXuwSB8VoQNaXXbUAKZPKcanL_7AHCLmbyhRMmIh3XmO79c1GbHwH0z8NfNY2HWhPMNpYMHVKvGMIv6dOllPVaI2721zGx3uFhUwcjGDTMxFpBA1M1D4lcOuGalqxEaiO91cnjcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه به رهبر شهید
🔹
شرکت ملی پست ایران و شورای اطلاع‌رسانی دولت در اقدامی مشترک و همزمان با با برگزاری مراسم وداع و تشییع پیکر مطهر رهبرشهید انقلاب اقدام به برگزاری پویش مردمی «نامه به رهبر شهید» کرده‌اند.
🔹
در همین راستا عموم مردم می‌توانند نامه‌های خود به رهبر شهید انقلاب را تا تاریخ ۲۵ تیرماه ۱۴۰۵ با مراجعه به دفاتر پستی سراسر کشور به صندوق پستی۸۸۱۱-۱۵۸۷۵ ارسال کنند.
#باید_برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/666146" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بازتاب وداع با رهبر شهید انقلاب در رسانه‌های مطرح دنیا
🔹
مهم‌ترین رسانه‌های جهانی هر کدام با نگاه خاص خود به پوشش مراسم وداع با رهبر شهید انقلاب پرداختند.
رویترز:
🔹
شهادت آیت‌الله خامنه‌ای در پی یک حمله دشمن «با سنت قدرتمند شیعی شهادت و سوگواری همخوانی دارد؛ سنتی که در آن گروه‌های عزادار با زدن بر سینه و زنجیر زدن به سوگ می‌نشینند.»
گاردین:
🔹
مراسم وداع با رهبر شهید ایران به‌گونه‌ای طراحی شده است که نمایشی باشکوه از سوگ ملی، اقتدار، روحیه مقاومت و همبستگی اجتماعی در ایران باشد.
فرانس ۲۴:
🔹
ایران در حالی که برای تشییع رهبر شهید خود آماده می‌شود، به آمریکا و رژیم اسرائیل در مورد هرگونه حمله هشدار داده است.
ایندین اکسپرس:
🔹
مقامات جمهوری اسلامی این مراسم را نماد وحدت ملی، تداوم راه انقلاب اسلامی و تجدید بیعت با آرمان‌های متعالی انقلاب اسلامی می‌دانند.
شینهوا:
🔹
مقامات و نمایندگانی از بیش از ۱۰۰ کشور در مراسم تشییع شرکت کردند؛ از جمله سران کشورها، روسای مجالس، وزرای خارجه و شخصیت‌های سیاسی از نقاط مختلف جهان.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/666145" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpTpdv0AekE8OGs_o4xnhWPC2UZaykwyIQHMPblaaPvZZEDsZdIvRPjN9_MGg-rQMtO8awTsoFYIFVRSGo5EPonQv5j7tVHYUpNVb6zzrcGx5-b3ySH7a4dgCC-tnV1aLYWdNzozqqidaeOS0r1yz_aNWQpMYQ8RWEVN5JbWgEnZDOIg8lw1PIOoLeqy7IZRrN4O9TGPftHWhHaJtMwwbVMJ3JNEnCLKI5-DPPk40FQqdJwd2F7NfWCuoGnZpjoaaooAoq8-Tmdxs39zOyv9Mt70F72jSOo5jtZxhD2d7ccilWhnhLOo30zYXTsSlKQUioS0ppGN4OKICYPsxzZ-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویرسازی حشد شعبی برای مراسم تشییع قائد شهید امت اسلام: حضور پیدا خواهیم کرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666144" target="_blank">📅 23:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تفسیر جالب رسانه غربی از مراسم تشییع رهبر شهید انقلاب
میدل‌ایست‌مانیتور:
🔹
آنچه این تشییع را واقعاً بدیع می‌کند، تبدیل اندوه به ارز ژئوپلیتیکی است. حملات غرب برای «بریدن سر» طراحی شده‌اند؛ تشییع نشان می‌دهد که بدن اجتماعی می‌تواند سر خود را به شکل نمادین بازتولید کند.
🔹
جمعیت خود به سلاح تبدیل می‌شود. پانزده تا بیست میلیون بدن که در صفوف راهپیمایی می‌کنند، بیانی زنده را شکل می‌دهند که اراده خاموش نشده است.
🔹
این رویداد تنها یک آیین مذهبی نیست؛ بلکه یک مانیفست ژئوپلیتیکی و یک همه‌پرسی متافیزیکی درباره خود امپریالیسم است./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666142" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYaPmtypZJssl-y9N-X2DVlruXlgyL8sbht_dMAtbgtMNMQNJXEFGhkpknAw5yv6WE3PIvapVqg9D2Gc2yOcD9pU4ZOM6p5nqPW4PQAPqxurgPkbpWD6j_0ARSAwtjbbaIuc2PTX0w_oEe9OU0UiLypk350TrVwe3T1nOrGiJXV2iwyZAIS4G9Cnx9vNFqbnK7YGuXKTN5qzx0oDppwOXBfLxE80RpJhPV4CBKFUCHKfmcaOe_Uc29TiRAR8Y1a_ZmC3yVWRf5ZGQb8dVIvQHodZqGFeGr9Q-gkszZLPAPpaDqqO0OiOSXlIWyCIxPB-s3pYdZ8B25YqWewem9S1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
اشک‌های سران قوه و مشاور نظامی فرمانده کل قوا در لحظه وداع با رهبر انقلاب
🔹
‏این غم مقدس است این اشک‌ها خوب است اما مطالبه مردم این است که این اشک و این غم به خشم علیه استکبار جنایتکار بدل شده و عزم شما را برای خونخواهی رهبر شهید راسخ‌ و قطعی کند.
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666141" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/666140" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/666140" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/666139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/666139" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXrzpLJD92uZPh47nvzeJyPONofqpnG8PL1bpQe4R5k_SIC2NCYxE8hDLavZmO6uxEcqRe9Jx8jj0vmS--lApIziXH43S-XYfUci0Vxe2LspGhujBAyc3qmwdnUu2BAEnXhaN2XujagXh0IJCcDA46jE2E1YwC_0SjQ58J6NguckFTXTgmI5YlnZu978yjL0Lfg5CvCq3Jm7QJABTQiV8Ocpn6uPdh6vBfXIlq5bn1v6RlYgOCaO7yCONuDspugjsaHP0eoZcCNG76B8ZS8iWRmeGNAOcQh8zeVGAlQIwnKbkUz-2Q22sppjnNMOrLITYrZOwBGc89N8QRxgukkewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ در آستانه مراسم تشییع
🔹
مچ‌بندی به رنگ خون؛ نمادی از وفاداری، حق‌طلبی و مطالبه خون شهیدان.
🔹
اگر شما هم در مراسم حضور دارید، تصویری از مچ‌بند سرخ خود را برای خبرفوری ارسال کنید. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/666138" target="_blank">📅 23:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استان واسط عراق و ذی‌قار هم به مناسبت مراسم تشییع قائد شهید امت تعطیل شد.
🔹
رئیس اقلیم کردستان عراق: جمهوری اسلامی ایران با پشتیبانی مردم وارد مرحله جدیدی شده است.
🔹
مکرون: ناو هواپیمابر شارل دوگل در پی تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/666137" target="_blank">📅 23:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW3MyPK7RkDGtA1y9LIAtsoEtSFullvhB5cQ8A-R_lbQwmBr2EPg2-tytmsGHEGHe1kzDva-EIlmcNEuI15FFWpZxv3GDdyCIMWGIytLhCtlwnRdrdAXpyP0poeflAEHkJEwV2O6MVE5ympXohmL-odLl-fyHPc2GBSKO-Mg2mLQLVWNA5Hy4c_iWFdNd8fTcsa8E5Ma1QFveOCEQeFzE7CyI62kr_1vSOXE1zyJ-zrUjtf2Me-x3hg_HvMQX3Ubu8hUaPDdRo3-0vr-1rRn4OicEcETaEzs7yVF04a4QI4cEYq8x7pnuxE5jI1rj4hnPf9CtI7PS28h2kmDMo9hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شعار نوشته‌شده روی موشک عماد با سرجنگی شدیدالانفجار
🔹
رزمندگان هوافضای سپاه در آماده‌باش کامل عملیاتی حس حضور در مراسم بدرقه رهبر شهید را به شهرهای موشکی آوردند و شعار
باید برخاست
را بر روی موشک‌های آماده روی لانچر نوشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666136" target="_blank">📅 23:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عطارزاده: مردم بصره و شیعیان پاکستان خواهان میزبانی از پیکر مطهر رهبر شهید شدند
سخنگوی ستاد بدرقه «آقای شهید ایران»:
🔹
دولت عراق برای برگزاری مراسم در عتبات عالیات ستادی به ریاست نخست‌وزیر تشکیل داده است.
🔹
مردم جنوب عراق، به‌ویژه بصره، و شیعیان پاکستان خواهان تشییع پیکر در کشورهای خود بودند، اما به دلیل محدودیت زمانی این درخواست‌ها عملی نشد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666134" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCWwWdxidYeS1nX66qm1shpkhdAzL4fs-Spctl94K0XVclqa1xfUR1-4vs_5-cJssAIc-nFGB0hDEw42cqIu59NLmgnuEcO_2absFLvjsKBjllufpDVyBvFIsvks2fTrmtiC3mO57DFkFHd7wVgJd-kY0puWSXrqKLBZJoE_RnpG--r7CG5AwfLVRe3p0KTGddtMCJy-8zRaD53BmOrg55LmwNV7wkImdk2WGTPoevuITly5HqMO1-ciK4bhXVCU2hQt68IFFxboFJg2I1M3fjWFbLR_xLlTA2oBifGiD4dofnaz32Us14X2FT3JaonPnHhx_GsowQKomXjQX_67lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_نهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید حسین آجیلی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/666133" target="_blank">📅 23:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dee87ae4.mp4?token=bfmUI8BkK1xevMpoKOgk8lxfEQzivLmfGuX_Nbb7qT79GrCGNjN5GAsd2bEs2CDBIqNkXVtJeS9i8leE26duvSzP1oDY36c8UpVkpJqCng_RLLKjknws0XSiDL9Dalop1Lby1oAn12CzA_iItCm-3vGA_TscGLdG7hq9cEzqq3YR58Bd15xJaBD5zEdIfNvP2jGohVDu-7BQ-rziit4CSUnuOmhgBDnbQVK7_D5WOpfTRZpelZQre_dmOpVs2xpqOUjbGMgKGoo78yh2eNGDg5IbaspEM07Z4EgcBYc_CwePz-Zfz1AixSSJsAWUoY1-aNfjYDgoMy-cY-iswxmRNGZw3yTZUt6Qg415MQgMN3SseEdOlY6N5R7BgOzdniaESS3yb0iVtT5AayudVyYjy7XpSH5IEVSuYtnnBc2dDNndKL5Fi2T-JvKjOFU9S0ahRH_ZYlqyBbS_eX5nT44NplgXa2_Wrh3E3UZ--YIGlF0RXxM4o9QIzN-52KJHlyHfgdtlnSTvhQxPlgN7HboB99-DIpgmyqq9VwBnOpj8VSvTLFMID6OpF4Q1xUi5iJicTWjqhb8a5UUDd2DfOEQ4JULyourQ1ruJxAIZawwmD4ALzwe6w_eTQ2tQ_p6RDfFk5A-PwitMlQoyb1L1JyDsC2fg88jq9R0D4PhMT8qmeJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dee87ae4.mp4?token=bfmUI8BkK1xevMpoKOgk8lxfEQzivLmfGuX_Nbb7qT79GrCGNjN5GAsd2bEs2CDBIqNkXVtJeS9i8leE26duvSzP1oDY36c8UpVkpJqCng_RLLKjknws0XSiDL9Dalop1Lby1oAn12CzA_iItCm-3vGA_TscGLdG7hq9cEzqq3YR58Bd15xJaBD5zEdIfNvP2jGohVDu-7BQ-rziit4CSUnuOmhgBDnbQVK7_D5WOpfTRZpelZQre_dmOpVs2xpqOUjbGMgKGoo78yh2eNGDg5IbaspEM07Z4EgcBYc_CwePz-Zfz1AixSSJsAWUoY1-aNfjYDgoMy-cY-iswxmRNGZw3yTZUt6Qg415MQgMN3SseEdOlY6N5R7BgOzdniaESS3yb0iVtT5AayudVyYjy7XpSH5IEVSuYtnnBc2dDNndKL5Fi2T-JvKjOFU9S0ahRH_ZYlqyBbS_eX5nT44NplgXa2_Wrh3E3UZ--YIGlF0RXxM4o9QIzN-52KJHlyHfgdtlnSTvhQxPlgN7HboB99-DIpgmyqq9VwBnOpj8VSvTLFMID6OpF4Q1xUi5iJicTWjqhb8a5UUDd2DfOEQ4JULyourQ1ruJxAIZawwmD4ALzwe6w_eTQ2tQ_p6RDfFk5A-PwitMlQoyb1L1JyDsC2fg88jq9R0D4PhMT8qmeJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از روایت مردمی که ساعت‌ها در انتظار ایستاده‌اند؛ از سال‌ها همراهی، احساس دلتنگی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/666132" target="_blank">📅 23:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8xf3YgFe6HihVg3eBim0pkQVh8ivdb3kcWAzmjABO7tZMx0jEzuYRdzl-Nd6FXmAKlBMUVTQajbOhvNQp2dQs7CLOyzsaz_h0-ZjpGn5SyAve9SvQS8EF21JjQTwPFvyT2tvPEWG69AtXO_SqT_bA6UkMwPidXwW9lK89pj-Wh1s1FetP4Jclarq0pn3kc_cF7iistWq1bT1CE9-0mOyBwm08sR4Jr4O7Kl2mHJOu8qt6kP_Yx4dsFpvr0v1fDfTYKWiOaBRMwmuB1JtdFUcjeitix-63BOHvMyGohDJFMWHEFQd8g_8VsrA7nTLJrJrhrL2pWXbnUHx-qPouHuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱.۸ میلیارد سال تا پایان حیات؛ زمین بیشتر از آنچه فکر می‌کردیم زنده می‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666131" target="_blank">📅 23:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ نامه ای از آقا</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/666130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
سلام عزیزای دل من
دل منم تنگه براتون
برای اون حماسه هاتون
توی خیابونای این شهر
منم میام هر شب باهاتون
🎙
#مهدی_رسولی
#رهبر_شهید
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666130" target="_blank">📅 23:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استاندار تهران: مدارس، مساجد و ادارات مسیر بدرقه، برای خدمت‌رسانی به مردم باز خواهند بود.
🔹
تعطیلی رسمی در بغداد به مناسبت مراسم تشییع رهبر شهید ایران
🔹
ادعای فایننشال تایمز: تردد کشتی‌ها از تنگه هرمز در هفته گذشته بیش از چهار برابر افزایش یافت.
🔹
سازمان جهانی بهداشت پایان شیوع هانتاویروس را اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/666129" target="_blank">📅 22:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10891a982.mp4?token=WGLQdYujWgkpcvV-3jn3Z4xh8Ijtc17ZA7iEbGbp2hrum2Sq7jhm2noLSKUP7if7SEDoKlrDwmLFqihKzID864xJ17EKScHZVyPu-F7GRVFdARQZddm-zNqk6EwB9n6aH5w9sDZ7OETh49ajJakwAtmLvpfBfuWHuaSu5BJMfczfNiSsd2DFdhFBA8zAzdhdrWt1DdHWSgUZRiN5h64T5h4jBl7_7ubakw9Re9VLPNWO61grp26EUJjVU7ojtqdxQVvNzRrNnnBw4yh4xL6pgs4Ewh0jI3JMCDiBvp6o99uYL3IZWxIXNQetp8_1M_ZdbyzlR5-XQTZ1NGcdx3C--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10891a982.mp4?token=WGLQdYujWgkpcvV-3jn3Z4xh8Ijtc17ZA7iEbGbp2hrum2Sq7jhm2noLSKUP7if7SEDoKlrDwmLFqihKzID864xJ17EKScHZVyPu-F7GRVFdARQZddm-zNqk6EwB9n6aH5w9sDZ7OETh49ajJakwAtmLvpfBfuWHuaSu5BJMfczfNiSsd2DFdhFBA8zAzdhdrWt1DdHWSgUZRiN5h64T5h4jBl7_7ubakw9Re9VLPNWO61grp26EUJjVU7ojtqdxQVvNzRrNnnBw4yh4xL6pgs4Ewh0jI3JMCDiBvp6o99uYL3IZWxIXNQetp8_1M_ZdbyzlR5-XQTZ1NGcdx3C--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت نهم مستند احیاء و حقیقت | باران مذاب
🔹
وقتی یک سایت فولادسازی هدف بمباران قرار می‌گیرد، انفجار تازه آغاز ماجراست...
🔹
در میان کوره‌ها، خطوط تولید و تجهیزات عظیم، هر بمب می‌تواند زنجیره‌ای از بحران‌ها را رقم بزند.
🔹
بارش مواد مذاب با دمایی سوزان... نشت…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/666128" target="_blank">📅 22:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmfF_Py2y2MI4nDdHrYMJzVm8qtRsSMLslmTSb-2aI1nJ-JZsr7UDY23j1gAPpFKESOCL7MfSC2rGNJCmWWZ2h3Bf-sbrQZB_sS6D3NNqidc2owoi2Gk-7UG3-M4A8Z-4uMV4AsD9vbfuw1pVKoKOJRNppi6COYQ0HzOnS8nFCkMWQx2hZ0OYM6PyP4quP57KYm52LfswUDwyoJyEkDeycJatA-W19gE5xB2sbo1jBaXo1JsrPRMpeTFWRsx6aaMDzR1Yormpbu46hQbBKTEpFSqi3P4uQ6_p9lUN43TGT6fPNUT5QvS0e_VV7RLQy-3Uqzn78Ob8fCY-q3SNlb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرمربی کره جنوبی استعفا کرد و پنهانی از کشور خارج شد!
🔹
سرمربی تیم ملی کره جنوبی، پس از حذف تیمش در مرحله گروهی جام جهانی ۲۰۲۶ (با ۳ امتیاز) استعفا کرد و به دلیل موج گسترده تهدید و انتقادها، مجبور شد کشور را ترک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/666127" target="_blank">📅 22:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_GlUQbo0uxe_uZQXFev0cBVHSXvtqiP1ycGAFYwVsu5YWBBh3UNv5bcNiaJysyjJjUtD3F8Anhgetu12rqz9HCfOrhdBANa4IxVqeNu3lKlzu0_FPGiLblMcMTMULewSjt3MLdbTOhX36LjZ9E0HqDbPb7coNb_v7L6WaeYCUIJju-tIasgYXkGwk6pn0vMB40J-lJnxfzd51rPETC92upwJH-4_amX6a_5isoJFxkrzRYNd3-II1UwW6b1iC9NJxLZvb_bVcQFZcSjGD5Rikt_4a14aYtqpOpsvX_mb69e5EyaCtpBGnqC_YlQERGLa0FH1rP8ZzgZI2BUMKzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ در آستانه مراسم تشییع
🔹
مچ‌بندی به رنگ خون؛ نمادی از وفاداری، حق‌طلبی و مطالبه خون شهیدان.
🔹
اگر شما هم در مراسم حضور دارید، تصویری از مچ‌بند سرخ خود را برای خبرفوری ارسال کنید.
#مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/666126" target="_blank">📅 22:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=JTzu4vS9jRGSHMaLD0-DvQUHNYxuzwmGCSQqVjd3b7BttrYc9yGZ5sS5IgNIQS_4KRfyPnFzPn8Do9yaVgy0pc3lMvbQpxhB_TSf1UxH-Ee7cBVBn-P87ybZBkeId24VZQCgDwiBq4cGCC6hQHhJcqEJqLJBJBUQWzbuEo4FvS6JdSf2dJrdiCg8HmkPit_9ZK3BpwcSK3WHVxbJoH5njcKE6WyzZveBJp7528S93n66miUg1vX5E3BFKcrh5AFXm4l6iSLK_C88jdJo9VBsbiV4vlm_M5qy6GvNBPQ3ARKYD-x0eStea_XHSoYahyhT6KbvWeCPqQyXkdcwvnUJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=JTzu4vS9jRGSHMaLD0-DvQUHNYxuzwmGCSQqVjd3b7BttrYc9yGZ5sS5IgNIQS_4KRfyPnFzPn8Do9yaVgy0pc3lMvbQpxhB_TSf1UxH-Ee7cBVBn-P87ybZBkeId24VZQCgDwiBq4cGCC6hQHhJcqEJqLJBJBUQWzbuEo4FvS6JdSf2dJrdiCg8HmkPit_9ZK3BpwcSK3WHVxbJoH5njcKE6WyzZveBJp7528S93n66miUg1vX5E3BFKcrh5AFXm4l6iSLK_C88jdJo9VBsbiV4vlm_M5qy6GvNBPQ3ARKYD-x0eStea_XHSoYahyhT6KbvWeCPqQyXkdcwvnUJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از حضور رهبر شهید در حرم امام رضا(ع) در سال ۱۳۷۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/666125" target="_blank">📅 22:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070fa33f86.mp4?token=XJNyZlfij8gD-64ZFRbkHgq3dzGjuZPyXH9saRD_dShc8AyVJX0cGZ5jkEWZeqn52GIq3vokuc3Iz9ykam8n-pyyTSjJbICwkc_SFaAqjSpxQSETSdYrejpww9brpRvzNtumvoBxNics7ku98Q0qAhPTfLIJTXeu6PkVMhwMEj3KSnHCd7-RsleVUmO7mbD-vdX3zEFC4YTpUaG2xacsdJIjlOMGjjfp51AfrYDQzanAjidzYYpWVHpFyfB6mdipCJroCqNOXBjZDfewOqUfWQsvDc47TvMqnB3uFB0YIDGWfGTPl72-3TQYwkEGmOlhuvjBNHJhEnbd0elWfp3CJQiPvcFC-QYy5fTzF1X2Z1dCQzy6zPxjCKi-X53wcG-1-3yxbykSUskziMw8AKSRo3aYMDn5dahstrXffN-cGNJmQ-i56kA54bNsjOTzDdaiO-dkVnKspgcVNAR9Lg2OueS78lF_HHidPGUy6_YE9lPvqucMOYEHdj3dm_VDUQ4SpWGEiYu8EL5LSqj4Iq8SB4DEX8N0CahArw63ukhNafQUpfrrRqde77woXL8fA5-Wlmk67MdxShSsInuyyw9Kuzo0ZUpPKXaf7g2a5z9oFK3SvvaP-cL9uOalxDWkTzj4edweW-GwDKxtjuzDLA65HKWBs6gs56XzrGMfBs8Ku-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070fa33f86.mp4?token=XJNyZlfij8gD-64ZFRbkHgq3dzGjuZPyXH9saRD_dShc8AyVJX0cGZ5jkEWZeqn52GIq3vokuc3Iz9ykam8n-pyyTSjJbICwkc_SFaAqjSpxQSETSdYrejpww9brpRvzNtumvoBxNics7ku98Q0qAhPTfLIJTXeu6PkVMhwMEj3KSnHCd7-RsleVUmO7mbD-vdX3zEFC4YTpUaG2xacsdJIjlOMGjjfp51AfrYDQzanAjidzYYpWVHpFyfB6mdipCJroCqNOXBjZDfewOqUfWQsvDc47TvMqnB3uFB0YIDGWfGTPl72-3TQYwkEGmOlhuvjBNHJhEnbd0elWfp3CJQiPvcFC-QYy5fTzF1X2Z1dCQzy6zPxjCKi-X53wcG-1-3yxbykSUskziMw8AKSRo3aYMDn5dahstrXffN-cGNJmQ-i56kA54bNsjOTzDdaiO-dkVnKspgcVNAR9Lg2OueS78lF_HHidPGUy6_YE9lPvqucMOYEHdj3dm_VDUQ4SpWGEiYu8EL5LSqj4Iq8SB4DEX8N0CahArw63ukhNafQUpfrrRqde77woXL8fA5-Wlmk67MdxShSsInuyyw9Kuzo0ZUpPKXaf7g2a5z9oFK3SvvaP-cL9uOalxDWkTzj4edweW-GwDKxtjuzDLA65HKWBs6gs56XzrGMfBs8Ku-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.  #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/666124" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FRSII3I4L1aaAiRvbiX3_3Whdmxm6-YTZsekUXtDaLEa17gw70qqtpqaRkM6G8ExOj15rc258bMzKiAamdNVXbkCEkCIJxoceiVLyMEwBTD6HvtWFfMQrRd31pmpkAgmGKnBZeK6bOsSToGwS3VkZYYsMM2oCZ0XauwQRuBcUh1-Nx1b7WWw7YG0cQzCDTaY9ZcvmLjwOE_O4j16OWUda7vKWx5Ovu3RrZPGigqdkxeQnKkr5tA-azYaKsNcM8BD61DbpjxNSaubM0ykd8mIlpKZcgc91w8tRj6PpfSypfMgYkcr5VTL9uZ5VTuvdqgR_uFlTrU7LB4gDYhSRWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت امارات تأیید کرد که شرکت ECT Aviation Support عربستانی که توی اماراته، ۵ فروند بوئینگ به ماهان ایر ایران تحویل داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/666123" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u51fJ7hbgOhQ2g7ypBIUrdofePovVQl1jyFerrG9C0v9TqtJPaPdsYw81JpgDX5w0ZCs_1NlJFm5_3_i1Um6ae910hwjW3XgRO3yfadlD6E1Xw3v5MQjZdHMBXSuZqmbEFGzm0XkrpL-8No4BtSc_BXm6codkoPLRmT-C_fwMEB8llhzAXzFd_WQpyFBdbeyw6q0MDFCaMHXDNcDabse4c1lJsVjAvoYBF86snzn2cSMjRhiL-wVy_3-MjTGWub_tzfrHJBu4brkZOnufsqSGyyYWoIr3tS4dptyqyOwQwO1Z9WfaOw6ngvtuRkZ57qzBxoWLe90YnVnCJ-J6_9BiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۳)
🔹
به عنوان کاربر فضای مجازی در اکانت خود:
۱. ویدیو، عکس و متن از بدرقه رهبری را به جای استوری و نمایه، پست کنید.
۲. محتواهای جذاب این روزها را حمایت کنید
۳. برای پست‌هایتان کپشن انگلیسی و عربی بنویسید
۴. از هشتگ‌های معروف این روزها استفاده کنید
▪️
پ.ن: پیام بدرقه باید امید باشد چون او نماد ایستادگی، استقلال و شکوه آینده ایران بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666122" target="_blank">📅 22:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aadf84bc2.mp4?token=STA_eM32h1yvuktHH2s5UWYmntgAMKotUE-1c-g9EQuphwuRZwWOJ-TAg6XFJ6lWpl_nUJ7RSIbi68cuxTmdQ0BWLihpJMBfkzetCre2I_fPM1VyOLZjEU1VwbQxxei9g0TQ9Xwos2yjaqtuEdHFXuF8o2avB3hGFjnahv8soSLP7KHnFveTWHwy2jWAoOUT2nrjOneG-hPlgV1c8b_rawXNO9LYkeWE_D-q0uu4T1GTgRrONpt96iTMbSzluNz1tfVTUODqEJVecZJCB335CDOQyqblnguiMs6VmBMYtXtIujhDJLpmxtjOim5BIWgzw0Nju0bYUZLEAyYia_OTGmssCJEMeqYRqeJT3t7q7Wmnf_avW1TqM0PmABum-F00DgaOT0TlV5_AFyKLyfDzl_JukxqJ-oIX7eR-QBhpfTS2GYMkgA2D3-3fU5_p3haxfHdPtLkHXO39JQTdR1nXv_XvV70xWUT-H5TLgt9ZtqfXXPus-4PWFC_hWjhm4DpPCCJ7WZ2SlVzd_PfcdWz362-W00dFjx4_OYifhYtFM-XrrFAaLVM2avqFAte20hY2lN2WNUMuHWJkrRsuDW1YwkXFQsbywS10vX8K8aBDPkjirMu9RzhJaRTQLGu70cUSczsbP9P679CmNMxOfhxOBwqm58UDvLXZ1e3P922XeEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aadf84bc2.mp4?token=STA_eM32h1yvuktHH2s5UWYmntgAMKotUE-1c-g9EQuphwuRZwWOJ-TAg6XFJ6lWpl_nUJ7RSIbi68cuxTmdQ0BWLihpJMBfkzetCre2I_fPM1VyOLZjEU1VwbQxxei9g0TQ9Xwos2yjaqtuEdHFXuF8o2avB3hGFjnahv8soSLP7KHnFveTWHwy2jWAoOUT2nrjOneG-hPlgV1c8b_rawXNO9LYkeWE_D-q0uu4T1GTgRrONpt96iTMbSzluNz1tfVTUODqEJVecZJCB335CDOQyqblnguiMs6VmBMYtXtIujhDJLpmxtjOim5BIWgzw0Nju0bYUZLEAyYia_OTGmssCJEMeqYRqeJT3t7q7Wmnf_avW1TqM0PmABum-F00DgaOT0TlV5_AFyKLyfDzl_JukxqJ-oIX7eR-QBhpfTS2GYMkgA2D3-3fU5_p3haxfHdPtLkHXO39JQTdR1nXv_XvV70xWUT-H5TLgt9ZtqfXXPus-4PWFC_hWjhm4DpPCCJ7WZ2SlVzd_PfcdWz362-W00dFjx4_OYifhYtFM-XrrFAaLVM2avqFAte20hY2lN2WNUMuHWJkrRsuDW1YwkXFQsbywS10vX8K8aBDPkjirMu9RzhJaRTQLGu70cUSczsbP9P679CmNMxOfhxOBwqm58UDvLXZ1e3P922XeEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای سوزناک ترومپت در مقابل مصلی/ شهروندی که نمی‌داند چرا ساز می‌زند اما مبعوث شده
🔹
روایت شهروند تهرانی که از روز اول جنگ پس از سال‌ها ساز زدن را مجدد شروع کرد و حالا مقابل مصلی منتظر شروع مراسم تشییع پیکر رهبر شهید انقلاب است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/666121" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a99d98f1.mp4?token=dDzw7VLp5azFpyp76_7qwteL8qqX-XdnhUWCI_3QZ9Sa7PlIOHZhX23AY7zwXMpRF2T5nh5DOoXM0MUzrzPC3wfoBoiQIY-Te-xxmb3-tX-oh7-Js7ZD0xgybCZLwgrFozal6WF6eljDdKemSOJ4SXmLziN2zgzhhe4u2UGWWRjQpO6X0Zy9E-XumU-Rdu5kMEUZ49m-v7jg1ZIOB0nlqHg65PO5I6OxZN2AeXMcdiLxQWHfGWTlWlZHn5DKdJytBuaT0WbBklYWOs_HoK-sJTnRbGyk79wOw4XLoPhUsSl0zvgPGi0s-r8okJNKbIc5p1jt8KbwMQRJFgJkcX05PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a99d98f1.mp4?token=dDzw7VLp5azFpyp76_7qwteL8qqX-XdnhUWCI_3QZ9Sa7PlIOHZhX23AY7zwXMpRF2T5nh5DOoXM0MUzrzPC3wfoBoiQIY-Te-xxmb3-tX-oh7-Js7ZD0xgybCZLwgrFozal6WF6eljDdKemSOJ4SXmLziN2zgzhhe4u2UGWWRjQpO6X0Zy9E-XumU-Rdu5kMEUZ49m-v7jg1ZIOB0nlqHg65PO5I6OxZN2AeXMcdiLxQWHfGWTlWlZHn5DKdJytBuaT0WbBklYWOs_HoK-sJTnRbGyk79wOw4XLoPhUsSl0zvgPGi0s-r8okJNKbIc5p1jt8KbwMQRJFgJkcX05PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه مهم برای حاضران در مراسم تشییع
خبرنگار خبرفوری:
🔹
از مردم درخواست شده از تجمع مقابل مبادی ورودی مصلی خودداری کنند. درهای مصلی از ساعت ۶ صبح باز می‌شود و زائرانی که از شهرهای مختلف آمده‌اند، برای اسکان و پذیرایی به درِ شماره ۴ مراجعه کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/666120" target="_blank">📅 22:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dc29f2e0.mp4?token=fvJOI4g77f4noe_kY3zX9OIk-34oNMXzVwdv0wWp0EJfg0HCGx2dh9WnIkZtFy0JqcPkpME74lZWCIyDtnrgZ-ra3y_mqAjIUDulCY2Lh0A1wkDESI_WhVMjAxD3jp0DAongoFLHQHAizxQodEDAsl6tHDJsXSKWzdMxSHs8mFv27X5p7S1UcA9W9dt-RY0ou18xcGvAtuzyTKpSyP_dj03s9HRCq-muCUQLIjCGysFVby8nYbhXBF3rRH3T5LN5WkCrYwyoH2v--KLmSTc6JSxQauZx1T3Z2-psIOts_CJr9taB_U3hyJk1IaAt85PnnBmpvGoptT0E0_a-2uNglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dc29f2e0.mp4?token=fvJOI4g77f4noe_kY3zX9OIk-34oNMXzVwdv0wWp0EJfg0HCGx2dh9WnIkZtFy0JqcPkpME74lZWCIyDtnrgZ-ra3y_mqAjIUDulCY2Lh0A1wkDESI_WhVMjAxD3jp0DAongoFLHQHAizxQodEDAsl6tHDJsXSKWzdMxSHs8mFv27X5p7S1UcA9W9dt-RY0ou18xcGvAtuzyTKpSyP_dj03s9HRCq-muCUQLIjCGysFVby8nYbhXBF3rRH3T5LN5WkCrYwyoH2v--KLmSTc6JSxQauZx1T3Z2-psIOts_CJr9taB_U3hyJk1IaAt85PnnBmpvGoptT0E0_a-2uNglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/666119" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ایران آماده میشود؛ برای دردناک‌ترین و در عین حال باشکوه‌ترین بدرقه تاریخ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/666118" target="_blank">📅 22:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آغاز محدودیت‌های ترافیکی مراسم وداع با رهبر شهید در محدوده مصلی تهران
🔹
محدودیت های ترافیکی در محدوده مصلی تهران به دلیل پیش بینی حجم بالای شرکت کنندگان آغاز شده است و ضرورت دارد شهروندان برای شرکت در مراسم حتما از حمل و نقل عمومی استفاده کنند. #بدرقه_یار…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/666117" target="_blank">📅 22:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oit2iYYuICEJgvDnTqbboaoBYTVugJ0ZBaRnbU9Cc5bspyLGIMZ87TcySr9PVLylBOG9Rbtgp_4L0T4J2z732qkFwl8WDaWuOQOVxw3J3fNtAWoei44V5xKbzp7YhQk4otuU_oR_lf_7gGUNZgfsSm9Xx_aKndO26a8Y0XJ12pVi9UldOT4wjFrp7MzxdyVUAYRjuO50sSgNdhHPhGv6DZWgsFX0Z_YrwQPDHt6IEsTdaSI2Ve7YwtNG7HNN574lXIeUjeDr65g0N7CVKHVfdvhxM5eeZw4VwKAJaoPRkDFmL21NxiKtNivvqBM00yBt15Prn1e8AWjxcrFUqRwFjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/666116" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c51b3a8791.mp4?token=kCpquN0cqxdxwucHd3YZYysDa_eXvy_xpbG9nc_SuDM1oKJt6m4RQQ3nRn9-g1g2RquoOO3kA2n7oaoNpzFWC8Z44zGD1xyxWCDbtwMYeRBIq4h5jnflCWZtZrUAJqPVbqhavJ-mFfCwsEUYkCW5BuQookphmLIxUrtULXlNf7J3d6j0kPPsUXsMWLi0-iVsT9-JsLYzLh_BgwrKfwR2_kLVM0iOjXzpfjABam2N_1OZMWaN3U_lpvmy310QfJvdTpCfz7VPATuADwGNraRiPLpgXfrW8N12qYApYlx8oxrLwUKupIthezf0NPxPznvSk2shWFGqWz3bnMlmuno1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c51b3a8791.mp4?token=kCpquN0cqxdxwucHd3YZYysDa_eXvy_xpbG9nc_SuDM1oKJt6m4RQQ3nRn9-g1g2RquoOO3kA2n7oaoNpzFWC8Z44zGD1xyxWCDbtwMYeRBIq4h5jnflCWZtZrUAJqPVbqhavJ-mFfCwsEUYkCW5BuQookphmLIxUrtULXlNf7J3d6j0kPPsUXsMWLi0-iVsT9-JsLYzLh_BgwrKfwR2_kLVM0iOjXzpfjABam2N_1OZMWaN3U_lpvmy310QfJvdTpCfz7VPATuADwGNraRiPLpgXfrW8N12qYApYlx8oxrLwUKupIthezf0NPxPznvSk2shWFGqWz3bnMlmuno1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای خونخواهی مردم از زبان مداحان: این مردم پرچم خون خواهی را زمین نخواهند گذاشت...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/666115" target="_blank">📅 22:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvly_IMaVE2PFO8_Eh3_JDNM-HMyyGm9T-0d6UUK7p2LxanzgwNl34xu31a6Nw0vv1FJ5ykNSe7P1nR-qjm6Nwnw72dAl5Ate8_Y8VMsTGV_CLlUaDs-zNS7ZKbovXAykjONosrz5mRCwS07RrfqYBQE1bSBjU-h7iJmB9wrppdfubIy6zb7HWvMZHfkVWv-fnis0Ge4sRmLG6xWPajsQRXOCEGXiAB9cZdDgniNmUTXwJpsbX7JBd0cwVpM-UzEMq1x8N25q4RCrDY9ZiJvRF7LrwYwxIq0PkRoBGmOTMGN0edECgwUX7Hc7-RCRE43d3zjwPrfL6kbpLAJbnA8cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/666114" target="_blank">📅 22:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdHpbm5vQ4i_k6yZ55BhQxvSFuBvPv5CudHmdrstiQVCg6SxfvC2nz7C7n-_uCI0CcFz-evJkAkI410HU9Rltgod7kaBoGakDk4t9MDmrrrxeavIJb0-_V7u8sJ8QRcoqgxbXymBt3Urk2iyllYKDslshx5UHAx-ce7Cd1kVxdWDVymJ0Dgbd_V671gPxVFTXNe-goY-4pjoquvgBNbFOMBsb_YPHD58t5dboR_QNV8UMK7gyMJaJUoQF9au38ueHQ2V-3spSipp4jwIZhhkCE6gkTEBLLsrXBr6rqI1gZGAw8o5FKcAxD57pw5_qWA-pNE8Ivva2B40XOkN4nY5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به گزافه‌گویی ترامپ علیه مردم ایران: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده، ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
قالیباف:
🔹
تصور کنید بیش از چهل میلیون نفر از شهروندان کشورتان برای تأمین غذای روزانه به کمک‌های دولتی وابسته باشند، اما همان کشور، ملت دیگری را به گرسنگی متهم کند.
این حرف از سر واقع‌بینی نیست؛ یک فرافکنی آشکار است.
🔹
توصیه‌هایتان درباره برنامه کمک غذایی (SNAP) را برای خودتان نگه دارید.
دارایی‌ها مال ماست، انتخاب هم با ماست؛ شما هم بهتر است به نرخ بالای سوءتغذیه در کشور خودتان بپردازید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666113" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
چراغ راه مبارزان حق
🔹
در تاریخ پرشور شیعه، نام‌هایی هستند که فراتر از یک شخصیت سیاسی، به اسطوره‌های مقاومت تبدیل می‌شوند. شخصیت ایت‌الله خامنه‌ای نه‌تنها به عنوان یک رهبر، که فانوسی فروزان در شبستان تقوا و عدالت بود؛ مرجعی که کلامش، طنین زنگارِ ظلم را در هم شکست.
🔹
او در قامت یک مرجع تقلید، پل میان آسمان فقاهت و زمین مبارزه ساخت. خونِ پاکش، نه پایان راه، که آغازگر حماسه‌ای تازه شد؛ حماسه‌ای که در آن، هر شیعه وارثی برای خونخواهی اوست.
🔹
خونخواهی او، فقط یک شعار عاطفی نیست؛ این رسالتی است بر دوش تاریخ. خونخواهی یعنی زنده نگه‌داشتن خطِ مبارزه با طاغوت، یعنی تکرار نکردن خطای کوفیان در تنها گذاشتن امام خویش. این مطالبه، فریادِ حق‌طلبیِ نسلی است که خونِ شهید را در رگ‌هایش حس می‌کند.
🔹
امروز، دل‌های مؤمنان با یاد او می‌تپد و مشت‌هایشان برای قصاصِ این جنایت، گره می‌خورد. خونخواهی، لبیکی است به ندای غیبی او که از ما خواست تا بیدار بمانیم. ما مدیون خون او هستیم و این خون، تا ظهورِ منجی، چراغ راهِ مبارزان حق خواهد بود؛ مسیری که در آن، ظلم هرگز به اوج نمی‌رسد، چراکه خونِ طاهرِ مرجعیت، سدی استوار در برابر سیلِ ستم است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/666111" target="_blank">📅 22:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548f5f5f40.mp4?token=A0yt_2xc_Gg5lHyRIVh9YxDPXAprDfURv0TEGlJdi6XelwmDGsfxEyGJlkrQZBOE231UY12YILcvAz8WG5AwAx5pHLZVNuwSTob2F-JWdfHbz5Angl0Wm5usZgKJUwzwgOm3LWTin01-Zoebyx7Qpn71shGkGzXC4d5vDen8ouvK1L6_hUCGkKfxX80XhtuNPSnapRSWcNwdCPp2WTq6Q2kxj0FH-Dwrok8vp9cVGE0bUSb5a3GHiuamwGrb_Svc8f2rWYZkYRwagmz0vcmeULSoOTIl9CtJS2s-XuolNYFaxd5b7z4q8E6zKqSwOQNpcy4wZQRpTQ4Yli7VsoacKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548f5f5f40.mp4?token=A0yt_2xc_Gg5lHyRIVh9YxDPXAprDfURv0TEGlJdi6XelwmDGsfxEyGJlkrQZBOE231UY12YILcvAz8WG5AwAx5pHLZVNuwSTob2F-JWdfHbz5Angl0Wm5usZgKJUwzwgOm3LWTin01-Zoebyx7Qpn71shGkGzXC4d5vDen8ouvK1L6_hUCGkKfxX80XhtuNPSnapRSWcNwdCPp2WTq6Q2kxj0FH-Dwrok8vp9cVGE0bUSb5a3GHiuamwGrb_Svc8f2rWYZkYRwagmz0vcmeULSoOTIl9CtJS2s-XuolNYFaxd5b7z4q8E6zKqSwOQNpcy4wZQRpTQ4Yli7VsoacKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار سید مجید موسوی، فرمانده نیروی هوافضای سپاه در مراسم بدرقه پیکر رهبر شهید انقلاب  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/666110" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
قیمت طلا بالاخره بالا می‌رود یا پایین؟
🔹
بانک سرمایه‌گذاری گلدمن ساکس پیش‌بینی خود از قیمت طلا تا پایان سال را از ۵۴۰۰ دلار به ۴۹۰۰ دلار کاهش داد.
🔹
در مقابل، سایر مؤسسات مالی همچنان دیدگاه صعودی‌تری دارند، به‌طوری که مورگان استنلی قیمت ۵۲۰۰ دلار، جی‌پی مورگان بازه ۵۰۵۵ تا ۶۰۰۰ دلار و دویچه بانک سطح ۶۰۰۰ دلار را برای طلا پیش‌بینی کرده‌اند./‌‌ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/666109" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سی‌ان‌ان: تشییع آیت‌الله خامنه‌ای رژه پیروزی ایران است
🔹
سی‌ان‌ان این مراسم را اقدامی عظیم با مدیریت میلیون‌ها عزادار و تدابیر امنیتی بی‌سابقه توصیف کرد.
🔹
برگزاری چنین رویدادی پس از ناآرامی داخلی و جنگ با آمریکا قابل توجه است.
🔹
یک پژوهشگر نیز تأکید کرد ترور او جایگاه نمادینش را در نگاه حامیانش تقویت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/666108" target="_blank">📅 21:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HHEagGt7oQylwFsxo_gSrxHXZ3V1qO-09pnw41wGKlwrfNLmh-gADaoKeP9tjVnlYSkQIBKLyc67eMZkirIyr4rjocPlzBVjodp_6adeAFd3x3K9bJKtQuUPpViu3jGpJnzyNSESgRqjGOvnQj1QH-z25RaOEBshRu6-Dqc8lhDFRa3Thks2uOKX14qClMTRhR_gq5qT5F7PWJlcXPdGPK_f1BP9-jhGC34yOpKoUuKwWgyjm9QERPNeNATIGFSVXZdMuotTgob4UA9y0298NV-PGDiIBPmNplD_Kyir77HbxeWuUQk-UPJUL4hjypjjPEeOnZT8O0__BM6IcdF7GeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HHEagGt7oQylwFsxo_gSrxHXZ3V1qO-09pnw41wGKlwrfNLmh-gADaoKeP9tjVnlYSkQIBKLyc67eMZkirIyr4rjocPlzBVjodp_6adeAFd3x3K9bJKtQuUPpViu3jGpJnzyNSESgRqjGOvnQj1QH-z25RaOEBshRu6-Dqc8lhDFRa3Thks2uOKX14qClMTRhR_gq5qT5F7PWJlcXPdGPK_f1BP9-jhGC34yOpKoUuKwWgyjm9QERPNeNATIGFSVXZdMuotTgob4UA9y0298NV-PGDiIBPmNplD_Kyir77HbxeWuUQk-UPJUL4hjypjjPEeOnZT8O0__BM6IcdF7GeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من آدمی نیستم که با لالایی دشمن خوابم ببره ...
🔹
نگاه تیزبین رهبر شهید انقلاب در  دشمن‌شناسی و جمله‌هایی که ماندگار شد.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/666107" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=F3XyeoPhAfb972S2syEsFTJBQyKeipC3RJohz1-U34A7orss6PHkD3ckBZrdBgdaest6zz4nvAabZvnkp4kTYKnmGJFvmTiHcih0TpERgAa5VvR_W3VUSfVlmS9m50EdpvqhS-mzV4FF-XVcd-hCHplEhnAGq_3rVTKpLwDQExm_zuzOTdOJWx2a40qnaEux7CsZ49YoQ1Rl3NRk69CgWhpvovdWVRVeUm7R5h1nU1LOdyA5RihPgbdoai_ho3t-aFjr9XSRvpaGHAEWOkmMAiIUtzpla8FdwiyAaQPJFpxprHIr9YD7qCr3ByAh4N3hK5lJdsn_1dwMv2yp5BSKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=F3XyeoPhAfb972S2syEsFTJBQyKeipC3RJohz1-U34A7orss6PHkD3ckBZrdBgdaest6zz4nvAabZvnkp4kTYKnmGJFvmTiHcih0TpERgAa5VvR_W3VUSfVlmS9m50EdpvqhS-mzV4FF-XVcd-hCHplEhnAGq_3rVTKpLwDQExm_zuzOTdOJWx2a40qnaEux7CsZ49YoQ1Rl3NRk69CgWhpvovdWVRVeUm7R5h1nU1LOdyA5RihPgbdoai_ho3t-aFjr9XSRvpaGHAEWOkmMAiIUtzpla8FdwiyAaQPJFpxprHIr9YD7qCr3ByAh4N3hK5lJdsn_1dwMv2yp5BSKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود ده‌نمکی: در تمام سلسله‌های گذشته، خاک ایران از دست رفت و کوچک شد ولی این مردم اجازه ندادند در جمهوری اسلامی یک وجب خاک ایران از دست برود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/666106" target="_blank">📅 21:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=jfG4nzolmnmIalfq9WVs1gq4WJ-EwxO1VpQarOfZtpUlq981id7GIrQ-4FvtTZu7uYtjSR-HJaaEHItfUgAyiq-7-db016XWQFAkhXCDbDLD1hlTJcxhr99RQ9EUkAB_K8Y-Cmt6Qkk3_MzxTS3jGnejWeBqiB4hKWGKLwCe_KnfnPzFPNEKiMeknEUMhzPorE80AVxMvJDaMl3q8VrMVqtBsw2vv1bzLctSLgHw6bDo6TYzSCbAbef7h3djv_k7HJZJ8an8vZNInCg1nYHlPI-QuFzUaFpUBjgOTsDA9mKtSG44908n-VpnwFCFQsYv4blviZKcULDffO_VEaOA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=jfG4nzolmnmIalfq9WVs1gq4WJ-EwxO1VpQarOfZtpUlq981id7GIrQ-4FvtTZu7uYtjSR-HJaaEHItfUgAyiq-7-db016XWQFAkhXCDbDLD1hlTJcxhr99RQ9EUkAB_K8Y-Cmt6Qkk3_MzxTS3jGnejWeBqiB4hKWGKLwCe_KnfnPzFPNEKiMeknEUMhzPorE80AVxMvJDaMl3q8VrMVqtBsw2vv1bzLctSLgHw6bDo6TYzSCbAbef7h3djv_k7HJZJ8an8vZNInCg1nYHlPI-QuFzUaFpUBjgOTsDA9mKtSG44908n-VpnwFCFQsYv4blviZKcULDffO_VEaOA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل جهاد اسلامی فلسطین: خون رهبر شهید مسیر آزادی قدس را قوت می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666105" target="_blank">📅 21:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af27e340.mp4?token=uBn7hnydhy-cZP0uf2hDQRtqmsB6n21BUJZlJzQPYvr3Np-DfJA8UG8tttqhdSLQYwMLxkc8iVplR-28S54ObdI19U1AGIySu72hrt8VTRMvkn7LX4BLX2uFddW0BCnIp-G3xYlnPCLq296Eljiay37I3Qw5jeYzaMwLn-p7ZRe5QVkzk4J_1-krfzA75jzHuD5zxBvBZAAkcMp6tJmXrGCDILAOmZw_sLIHyA7IAVfy4sZusqU072z6nkzD4KOZu-RHvcpy_RErgumOWnbJ-OYr1k-pr_0krxk8PCLs9OJXjx2H7k4760ghSwX05E7eHY0z19A-i8cGmg2T9qyRjki0JlqthwncvFaws8D3x2C1P9Fn_89pIsfGJm8BkUcC2Dm8f0SkXrS0IzoiHgiO6QNn92eCjmz0Pk2lfWoohgkpExqBtD2wGQRptuyzl9XlAh4vhU9y6aHfF8i5GyhqFd5oYXgfmNIIftdw88nHWFt2Mb0kssIvyjX_gMv9eiFu4Cc14hKl86EZqd7TbCqYuIWDZn9l0NIohAPY-zAA7z9KQcobFBk26Og0V8Q4F2EHZSUB2fUx99fmJa6XCjRZCz_HpUIvjAouwGuMdkQ2ZyFDS4VdvTFN-bM-fGKD2deTxIFuIm2uIUuYGqzmWBsW6BfWI58aefsoQXMfXdtgAfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af27e340.mp4?token=uBn7hnydhy-cZP0uf2hDQRtqmsB6n21BUJZlJzQPYvr3Np-DfJA8UG8tttqhdSLQYwMLxkc8iVplR-28S54ObdI19U1AGIySu72hrt8VTRMvkn7LX4BLX2uFddW0BCnIp-G3xYlnPCLq296Eljiay37I3Qw5jeYzaMwLn-p7ZRe5QVkzk4J_1-krfzA75jzHuD5zxBvBZAAkcMp6tJmXrGCDILAOmZw_sLIHyA7IAVfy4sZusqU072z6nkzD4KOZu-RHvcpy_RErgumOWnbJ-OYr1k-pr_0krxk8PCLs9OJXjx2H7k4760ghSwX05E7eHY0z19A-i8cGmg2T9qyRjki0JlqthwncvFaws8D3x2C1P9Fn_89pIsfGJm8BkUcC2Dm8f0SkXrS0IzoiHgiO6QNn92eCjmz0Pk2lfWoohgkpExqBtD2wGQRptuyzl9XlAh4vhU9y6aHfF8i5GyhqFd5oYXgfmNIIftdw88nHWFt2Mb0kssIvyjX_gMv9eiFu4Cc14hKl86EZqd7TbCqYuIWDZn9l0NIohAPY-zAA7z9KQcobFBk26Og0V8Q4F2EHZSUB2fUx99fmJa6XCjRZCz_HpUIvjAouwGuMdkQ2ZyFDS4VdvTFN-bM-fGKD2deTxIFuIm2uIUuYGqzmWBsW6BfWI58aefsoQXMfXdtgAfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همونی که براش نمردیم آخر سر فدای ما شد
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/666104" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owDtCvR8tBf_0VZXGLaMzt2WZHtsUoaWmxa-kteMODlSIw48usQmxVfMFMSZltk4q_GqsN8kkyzB5kleDFTFEuyG1rwQvkNBzfB30UOckHqoFQGhDO5sgLtxTn0aL5YyOHkAp_gKSiEPHBU1nIOVBho5jX_tp33YFjRTsdtnvmfx7HoRUw7VJuDyYK2PwiJCfet53di62uLZXyq_FNx4Ls0urrMBX0U_uswonnFUb6RfezLYB_rANUbcsAtq1NB5T4OSDGTa9-j4azMwlFkNJ3B9cH_3B1LLG64jd5QfqJ1bZXVkYrgTvvbgz7ngQYS95tAFxu4JKhQQHx44MgQEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abXf3QGkUZIzM0iXHVg4g7oIEAty9C1grkjAOBk6MaBcLDBf-4OpmAW-m4IRqtMDcpLbleyyk3arfuQ7KP-n8YQuZhKbn2apYEs6Fjcs7QOmfyTIqw7C56ocC6Li-IVkDe0HO_tvhGwaHtxaA5oDRQQVp2i6fTpe_uY4nPFoSjlk4YoZKv9broXz-QRBaUOm6QFCidzrchNQ4cnxvDM8ZBLphcGajHt6PU2GFO55UjWWLwfbNwuStwpf4oqYbZ-ZuU0VMfSAU1Z7qNPVCt5BdbeJTujJpwTmADvDvZrlO9yslyozSccB6-fIsn2ZDaapnPs6YAd3A6CjOfNstNSdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD7Q_Vb6WQ1QP-pwjxlUo5wmTM8UHnv0GjnDHUl4rAFI6UzU5zTqu2ghjjZh4xZD5zMJQucsJEAkbCH7kzQdeptrmGQoqR07KAuEFPBorYX01SgI5qbeNuTPpBja5bheuFZe4CohpqK14DknIfv-zupe26PvCGNDRmHsxYxB2ymrTijxRWBkK_ldzBmvBrJ6FUQ4G0r9ooFpFxwO50cOwKYdBezyEGl4im0VleWpkAjeTp1GqDQczuzsGf_uWUddnTsi2gdSCDAgey8exPDm12O7DxvXU9UOAZFWUjE4I6P1ILbFlQh1Zsm1ZAJCqqjPXXddMGWE3l_Loc1GM0BFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnHJq52-4zOrnHLZMn-0JLdMQyvLcfec1Z3B8GnpcGfH8pE6fxo3nl7URbSMrWaHQ0kZc1VtaH9lnqB2klPKAlUxITDW4FkUi7akpGL8YHLhgSuyNEgFPpEc-CqjNZ6t-jG4cq5onc0FknqmDxDrsDv00aTZnPTJwaZIQB0bVzbTZJmfIH8zAc4X-njw6lyhLL98l-NukZa_MYucJh6UWLGHDxqfyIyV4yQueJL7kDuZOel7cYEg1W3NHZ2qp_9jeZ40u-MZzlw64vRUvaWzlUf9NCdQDRkROHN0_rn8NSoFMJ9HxgBO6PW9tNttWpPrnqgItYNkgPVd3bH4ran0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvavUxoHGvbOdGWl_XrswtRc7d5cNv6G5KulbUKv3Uys038BQKH6yzl_45wDiMTxrtITIorp2W_s0dmqOy5ok_CJYE7BlsliwxBrUdhqT_vGGlaohJNi5Dx4U333RVFD48CBr22AFtVc8QhtR-ua2Cb2jj_7gsWObrP3hSbmMibZXsH2bXuNVD3O2gyesdu51G346AjVFCYJ40XRdGJCWcmxRY9HGhaSE1FnefNvOE77wij3GEr5XzDp_HSy820vMaGByI47T2IBuKiLyKDtnaDq2orJZNJjIaeSmzX0Znrva6KDxh-4rScW9w4t_V8ugk9u5Bhi1heNTKp-2sEdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkXE3lB6p1T2flU5u1M_TnzMWy-lQejL5LEFhPPswd763waTLMgbehMTdly1eJQxpKWi-C0WEJT8yE0DSryZwQnG3bpGgFvPhlwDKDU4cCR5SZpPb8tqhwBbq44KZN_NX6BQoLbFD4P3xXouL_y5VeIgYVd4geuRkTNiTm2f6IYrJdjJCAo_eKozV50y8TFG5aQuI32mX1oswL4dC4ezaTGTcFXlOxZk2tTRU4DjrJtIycp9q5CjZMiTmKbKo0K14NCKoHUCgwNs1IrsUxoNhgNFoANDjfoHtSSCZKB5JvpCN3Ghk67cjAx8lA4Ahamb30CAJ0H7-jZuL1tMpVKrzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دونستن چند نکته میتونین مناسب‌ترین مواد غذایی رو طبق خواستتون خریداری کنین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/666098" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666097">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
افشای‌گری و بهانه تازه در آمریکا برای حمله به مدرسه میناب
🔹
یک مقام آمریکایی با شرط فاش نشدن نام به آسوشیتدپرس گفت که پنتاگون از همان ابتدا می‌دانست که مدرسه میناب مورد اصابت قرار گرفته است. این ساختمان در فهرست «ممنوع‌الضربه» (no-strike list) به‌روز نبود.
🔹
یک تحلیلگر ۷ سال پیش مدرسه بودن آن را شناسایی کرده بود، اما این اطلاعات به‌درستی در میان بخش‌های نظامی و اطلاعاتی به اشتراک گذاشته نشده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/666097" target="_blank">📅 21:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666096">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=Ihcs4FtnBTYJdZXYSPx1X9FSiee5KeY6EwI5Z_KNMSoMdzGiokluCIOZc-ho68z4p3T1-4s4M1FkFIUWztPFl_uVomkKvlMKzmhuRdw_fRmNeAi6Vh6KJF16kiKGRfEJhsELxiUsuiY9nGBaRdaCNj_S8lCG1lWKI-UMndOmqLysVTZ6cT-WAaMr69V4JQt8_b6OR5W9GYXQFllyaU4jhHfU0SucEHgsrAMFWHNYHqyVktOl1XvqlFOcVZ9rPzwB2ljGFc6f2VT-oL7RaCtUe8HR1Y1rXi5fq6wk11YbPs2BoycD5shanXPdwTzZPjMwCHxNOFz4S8kQ6LMCL2bk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=Ihcs4FtnBTYJdZXYSPx1X9FSiee5KeY6EwI5Z_KNMSoMdzGiokluCIOZc-ho68z4p3T1-4s4M1FkFIUWztPFl_uVomkKvlMKzmhuRdw_fRmNeAi6Vh6KJF16kiKGRfEJhsELxiUsuiY9nGBaRdaCNj_S8lCG1lWKI-UMndOmqLysVTZ6cT-WAaMr69V4JQt8_b6OR5W9GYXQFllyaU4jhHfU0SucEHgsrAMFWHNYHqyVktOl1XvqlFOcVZ9rPzwB2ljGFc6f2VT-oL7RaCtUe8HR1Y1rXi5fq6wk11YbPs2BoycD5shanXPdwTzZPjMwCHxNOFz4S8kQ6LMCL2bk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس موزون برای اولین‌بار راز گلیم‌های آبی بیت‌رهبری را فاش کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/666096" target="_blank">📅 21:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666095">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3106e1b313.mp4?token=p2Y0lwBNSZ-_aaO08hK6B37mDB6tL6jeainvElhNUWlbUZBlIZADV2_oU6qn1jeMfw4IlUIp5ooz9NBvrImqDKCOeRkq_O1Oc2B2j7bbUpGNs8NAvxjGZtXFhElJhzJTF5LtH62SdVchKlyBSRWKTsQ_KELDAc-6VATjtMnym78DtjDHzGnYHGnfKKrY-DnGdasJPtd6RANLibFaMV4WuTZlQYYozCOC2_mA4X2fiMM_qlL8M-SniYfTVbDNIdg18nu76fxjkLL6t5iFtqqVIcEimqEKDUppVF1NfIW4_uVrzKE8hSL8u0dDYUmniOmaao0rFVA9v96t3doUri5UOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3106e1b313.mp4?token=p2Y0lwBNSZ-_aaO08hK6B37mDB6tL6jeainvElhNUWlbUZBlIZADV2_oU6qn1jeMfw4IlUIp5ooz9NBvrImqDKCOeRkq_O1Oc2B2j7bbUpGNs8NAvxjGZtXFhElJhzJTF5LtH62SdVchKlyBSRWKTsQ_KELDAc-6VATjtMnym78DtjDHzGnYHGnfKKrY-DnGdasJPtd6RANLibFaMV4WuTZlQYYozCOC2_mA4X2fiMM_qlL8M-SniYfTVbDNIdg18nu76fxjkLL6t5iFtqqVIcEimqEKDUppVF1NfIW4_uVrzKE8hSL8u0dDYUmniOmaao0rFVA9v96t3doUri5UOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار خبرفوری از حال و هوای اطراف مصلی تهران در فاصله ۹ساعت مانده به آغاز رسمی مراسم وداع با رهبر شهید انقلاب
/
مردم پشت درب‌های مصلی ایستاده‌اند
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/666095" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1429dd2146.mp4?token=dnu7UC88PXn9p1y9FjX0x4zrdFLx266JBPhszJJrqJNHODs8ZoToxFY20BbYdS9zjUrbxffRmP_H-Jlr6DXhh9Zg7SxGnsAftZfP5dkw_pFgNfdQZSWNLjLETsh9YVsMKwLTEcKDGpGbmJIMaI1tEjLY9ILtqzQbgnsD3ONqRecAzwTvDUcDzU9GPPy6rswqQkZhM3K05OWddD2KpKMZJn_HWJOrA7wAiCY4Bq9KGWFFXf2RLFIbtJbEmaJMRLC7MPIDc7N2MoRz0W2oOmVYeJHK6lvygkQJiNrQM4UAXJYDXqJNzVDqSz-VxGLqsNpO8V_XTYvs70QNsGdGOAXP2EXMk9W1Oe_MlGa9hs-zhR6kJQlwi1d3keAsZAZvSONTIKoAGORt9NhS4TtHLNHjfDMtWuhJmOJQxFzbmxiRTxOnftwMAVjIdme7sNpzILeD2uCN0Q_BN8bLOZJcY4NThid9OIyz98nn3hqSPSs_vlmmLh1YA9KPjK-_bwQwFxhM2-zHG-XTLgK-Mks-qhnVg8PjeqsvYPCXNCMyn-ORh_D9Mkjc-od99EtacAF3OQcCbH_kXejrxNxPmeJxii6edidGEhmuddftgIwjRcuc7omlcGNawE__Gabv_BSHEJXakPNm7_K6GrdGMALDbBLG32AywEPcES2FfL6v8smbFiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1429dd2146.mp4?token=dnu7UC88PXn9p1y9FjX0x4zrdFLx266JBPhszJJrqJNHODs8ZoToxFY20BbYdS9zjUrbxffRmP_H-Jlr6DXhh9Zg7SxGnsAftZfP5dkw_pFgNfdQZSWNLjLETsh9YVsMKwLTEcKDGpGbmJIMaI1tEjLY9ILtqzQbgnsD3ONqRecAzwTvDUcDzU9GPPy6rswqQkZhM3K05OWddD2KpKMZJn_HWJOrA7wAiCY4Bq9KGWFFXf2RLFIbtJbEmaJMRLC7MPIDc7N2MoRz0W2oOmVYeJHK6lvygkQJiNrQM4UAXJYDXqJNzVDqSz-VxGLqsNpO8V_XTYvs70QNsGdGOAXP2EXMk9W1Oe_MlGa9hs-zhR6kJQlwi1d3keAsZAZvSONTIKoAGORt9NhS4TtHLNHjfDMtWuhJmOJQxFzbmxiRTxOnftwMAVjIdme7sNpzILeD2uCN0Q_BN8bLOZJcY4NThid9OIyz98nn3hqSPSs_vlmmLh1YA9KPjK-_bwQwFxhM2-zHG-XTLgK-Mks-qhnVg8PjeqsvYPCXNCMyn-ORh_D9Mkjc-od99EtacAF3OQcCbH_kXejrxNxPmeJxii6edidGEhmuddftgIwjRcuc7omlcGNawE__Gabv_BSHEJXakPNm7_K6GrdGMALDbBLG32AywEPcES2FfL6v8smbFiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رهبر شهید از مردم تبریز:《مردم تبریز را متفاوت‌تر از همه جا دیدم》
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/666094" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666093">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN3Ec0y0HhxSJaznUj6n2yGgAQK9hqJYoVATDfcimeDgJyxzx81XXhoEjPkbiLW0IiDS4fHxV-AfHlKkQXAsxBXqc5xqdnnu9xoNX8MQcmKltRs3VQXNgbtQ7hp4l620lCeAAczPtfQeUs3PgTsthxsOMVg1cguTcDBl-GkaMbw4PW77-M9jGHa-mb3I6f_PSnLLk9pk_baW4e-dtIZ7vSr_6Vro5LtG9Bl_W7Z5jgq2xbUIhwCD91SrWlhVmRy0UG_HWn4HTdgVMZOgCPb1kNOKBCPi-3a6NrEWxC8HFahM6gfBdkDOi29NZGNJNSOFEhjTg4QbUaGzDXPXrMtU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران   #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/666093" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود خودروی حامل پیکر مطهر رهبر شهید به مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/666091" target="_blank">📅 21:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=vYnvn7z4HNWPVvMzsHC3_ATo6ZBistZewL9Cvbsn9oWBP1J9n2IKOdvxFqQEKNb-WQLogz0xu4lYarqQ3CMiKJ3H_9o4r_AQ4a8KOoKKFu1uerpx696Xtn1P-CvdkCaDg-g0QYtQGSb38h_INXJSapSA-jx8_0DU0A0TP4oWe3JZnee35iStDtLIaak_Q945pjwzWQNjOBzqIjzxn3imXkQtxTVi4vm1CWV3NzO63VeLxoHdv_DAs6lzlfBnTlrQxEVYdaYEkqpXbKB2SwXaFMo0OtQ8c3BXkSYOjaBrIB6m4pM90LmVJyD5BKIuz6niPpXIXRts_R5FUI3dgNEvvmS8hejpZKlg-Mjk1jixRvwOEqKeKg1t_rxQiNJgDLoIxJg1gZMF7JE2hsWdEiAOsvwrloQZ5q8XvvLlGMyJ92edpBSuuWYFa1Nh9KXPu-lHA3MoqM4VamMhcUpG9rj1gTWdFfhfF2o5FTYG-JE3d3V5xUq6OlSwxSsYSXZLMrE8ZJMl6PxfJwtcpZ2zrapC69C8eY_uHSnGPOv2DQMYRYdoSoepn4tu6wX3IlS3SkTd3rM6t90KrnA5iSAA_muZ8r40dln6eByEDqrqQC7eLjvv-C6cIe09P4J9c1FVhAJX2re072sQbpfFCmMq1MCLimgvXuZ4_b_sc_1-QOAvV34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=vYnvn7z4HNWPVvMzsHC3_ATo6ZBistZewL9Cvbsn9oWBP1J9n2IKOdvxFqQEKNb-WQLogz0xu4lYarqQ3CMiKJ3H_9o4r_AQ4a8KOoKKFu1uerpx696Xtn1P-CvdkCaDg-g0QYtQGSb38h_INXJSapSA-jx8_0DU0A0TP4oWe3JZnee35iStDtLIaak_Q945pjwzWQNjOBzqIjzxn3imXkQtxTVi4vm1CWV3NzO63VeLxoHdv_DAs6lzlfBnTlrQxEVYdaYEkqpXbKB2SwXaFMo0OtQ8c3BXkSYOjaBrIB6m4pM90LmVJyD5BKIuz6niPpXIXRts_R5FUI3dgNEvvmS8hejpZKlg-Mjk1jixRvwOEqKeKg1t_rxQiNJgDLoIxJg1gZMF7JE2hsWdEiAOsvwrloQZ5q8XvvLlGMyJ92edpBSuuWYFa1Nh9KXPu-lHA3MoqM4VamMhcUpG9rj1gTWdFfhfF2o5FTYG-JE3d3V5xUq6OlSwxSsYSXZLMrE8ZJMl6PxfJwtcpZ2zrapC69C8eY_uHSnGPOv2DQMYRYdoSoepn4tu6wX3IlS3SkTd3rM6t90KrnA5iSAA_muZ8r40dln6eByEDqrqQC7eLjvv-C6cIe09P4J9c1FVhAJX2re072sQbpfFCmMq1MCLimgvXuZ4_b_sc_1-QOAvV34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/666090" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb3a83365.mp4?token=k13itiEv2wqKTHC2vcS-KoVR5KeMpq8V4-LI7gaC6efcA4o89U1mJpNOsgTJShYaaTqnrNPu9ZvuV9PdAl8EU7MlcgoNpNgNu9Y6BfqEvIGNRTGKaERYewZoxXf36WDs04xTLnAxfl3GSJxX36ZR6sxDJEJHJhhvvrD5yDCnJPO1vrRyb2_Ld2Z3kghpkNpz--JGjDkGsTDmcyy6CzTFSf3Nhp5KEuL_8lQIiw6W9_Z0rveHU2GLK1GCMaPHW_x4kIlgsEUMRofic8dK-XGY_pXL6skBpEm2DAEmU9G9DJwGpuf4pVB5HjKwLmeVoH2N5PGsfiPJY4seIXQNhPlaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb3a83365.mp4?token=k13itiEv2wqKTHC2vcS-KoVR5KeMpq8V4-LI7gaC6efcA4o89U1mJpNOsgTJShYaaTqnrNPu9ZvuV9PdAl8EU7MlcgoNpNgNu9Y6BfqEvIGNRTGKaERYewZoxXf36WDs04xTLnAxfl3GSJxX36ZR6sxDJEJHJhhvvrD5yDCnJPO1vrRyb2_Ld2Z3kghpkNpz--JGjDkGsTDmcyy6CzTFSf3Nhp5KEuL_8lQIiw6W9_Z0rveHU2GLK1GCMaPHW_x4kIlgsEUMRofic8dK-XGY_pXL6skBpEm2DAEmU9G9DJwGpuf4pVB5HjKwLmeVoH2N5PGsfiPJY4seIXQNhPlaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه: امام شهید ما زیستنِ با عزت را به ما یاد دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/666089" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eb178548.mp4?token=iDEMt5UCrujCSuK7kfHG5ZjonqB-k7psW4HfmCurjuFtXhAxHIbjVxjwOaF0pti4mogIEzNDF0w92jOuBDgXaHmpPoRkPAgruAS0m5bf_rEIELAn80wzzwHBPv-ggzOKQvYjHzVkw_0Nt2Fod4LF9p4m1C3WWLlMsoIOL3lJM37ohCeZKU0AInlg9t4pgQp63kTF26z3YozMVoeKMfaZOt7DRo2GHfrJHVI46sXRCMsBUyduFgWhoL5yxPTDj9hOiU_nR4EJ6M_3334mGPTojcg_xVvNwiR30eSMLNy5bpEYyJ-mBK1TvhpLjw6uOop1HVhzXNx1BMwrcs6GJ5HPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eb178548.mp4?token=iDEMt5UCrujCSuK7kfHG5ZjonqB-k7psW4HfmCurjuFtXhAxHIbjVxjwOaF0pti4mogIEzNDF0w92jOuBDgXaHmpPoRkPAgruAS0m5bf_rEIELAn80wzzwHBPv-ggzOKQvYjHzVkw_0Nt2Fod4LF9p4m1C3WWLlMsoIOL3lJM37ohCeZKU0AInlg9t4pgQp63kTF26z3YozMVoeKMfaZOt7DRo2GHfrJHVI46sXRCMsBUyduFgWhoL5yxPTDj9hOiU_nR4EJ6M_3334mGPTojcg_xVvNwiR30eSMLNy5bpEYyJ-mBK1TvhpLjw6uOop1HVhzXNx1BMwrcs6GJ5HPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید عباس عراقچی: رهبر شهید انقلاب همواره ایران و ایرانی را عزیز و سربلند می‌خواستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/666088" target="_blank">📅 21:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtyzjKDwnTM47MzqR12xlkiVU7rNPgQrm8cdW6dJXEr5NbR5JtSQb4cQky7Om7KOfH0xfh-7moMnt7nWBZsQAMhASh2aXI0kZDTx5Oq4ZdrMVQ9Bb3G9tf3HXL2RBJB-mo7NP8gFkwFuH1nUk1NfTRU3cgX2sBUPdfcV1nsDIAh8beERWAwbGUP3lNm7TfdIC_CwOCDzg6Zo4SnCM-EOER5V3LY7Jx_Ydg9yoG7dTY8Onrsj0oozoRpMvx6anxzC3Hj9Jbi7YtEV0ZuHvJk9JVEFZtAh3YZg6CEJVOAESfz2fP42kFdWlOa6_fpmCOP21NbQ5P3HC0j_iRGEfkeKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری برگزار می‌کند
کارگاه فشرده «عکاسی با موبایل»
◾️
تصاویر ارسالی شرکت‌کنندگان، در صورت برخورداری از کیفیت و استانداردهای لازم، در رسانه‌های خبرفوری منتشر خواهد شد.
#بدرقه_یار
ثبت نام از طریق لینک زیر
👇
https://survey.porsline.ir/s/3PHWMjxm</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/666087" target="_blank">📅 21:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مینو محرز: هانتا ویروس جهش پیدا نمی‌کند مگر اینکه آن را دستکاری کنند  مینو محرز،  استاد دانشگاه علوم پزشکی تهران در #گفتگو با خبرفوری:
🔹
ویروس هانتا سالهاست کشف شده و جهش پیدا نکرده است و از جوندگان به انسان منتقل می شود، نه انسان به انسان. در آن کشتی کروز…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666086" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNY4GPnDKPAqQAuPHFsssQhaN80zecMwjrDwzgOahRhIQq6F5afIfrK4QZoWNPHbzHaaJakLE6PDsWF0QVMltOM_UXhvLZEKwi6HkEjJgY0K3wldvTVRrLY8rNp-kIPyN-Rg9HXbnl3qYjUz7helGH7bS1Yvd96SG5c2Ry1xeIAuVJR3AzubORGTEebVULGIrtakwN6DaUYFZFenKMMarcHYr4sBsWg7lpx1zH2x5gc5LQu7kyhQ7ETv380mbo3fC39kmUmWlR-ueHH1H1_iSnhJBXp9wJLXtFD6qow4zK0stc5ETYLx0BeAY_7ZhlvzvmFihPoNt5uDWIqoypNYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک اتفاق عجیب برای تونسی‌ها در جام جهانی؛ تونس با دوپینگ هم نتونست
🔹
تست ۸ بازیکن تونس در جام جهانی «غیرعادی» شد اما به‌دلیل پایین بودن میزان ماده، محروم نشدند.
🔹
احتمال آلودگی از گوشت و یک رستوران در مکزیک مطرح شده است.
🔹
تونس در مرحله گروهی حذف شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/666085" target="_blank">📅 21:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
انتصاب یک زن ایرانی‌تبار ضد ایران در دولت آمریکا
جروزالم‌پست:
🔹
«الی کوهانیم»، فعال سرشناس ضد ایران، به‌عنوان مشاور ارشد سیاست‌گذاری در نمایندگی آمریکا در سازمان ملل منصوب شد.
🔹
سفیر آمریکا او را «نماد داستان آمریکایی» خوانده و گفته شناخت دقیقی از ایران دارد. او متولد تهران و بزرگ‌شده نیویورک است و در دولت پیشین ترامپ نیز در حوزه مقابله با یهودستیزی و پیمان ابراهیم فعالیت داشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/666084" target="_blank">📅 21:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1594c4dbef.mp4?token=oMLPRmJVozlRj6N99nbKeoyhW0NNc1vJPtejeEWMlkWZtO78Wa34RhZ-0-PgAfwuNfgQQ9Ybf2hYrTQg-qMpjbOjtW26uWcWFQio_E86dur66zSG6BEWM3UKqmWdc2r0eFjxNz5YItUTtOPX__Ke4UFfcH9ai97yKKv2faj3SoMYzg-jYBjGZtmUrUfILtuBjr7ULwzZHJ0LptAzZ3aWh0VZWt1GebIft4wIpLX0rMelhzSSKRYMtqDPbh1Tjy5axtmtHyI3PP9NSsjA0GCfgQxfIYlkY4Vczateh_btFT9hHtvHedni4MdJ5V_BUzNZIyTN9aEu5Pr2Wmf_iHmEZGOYsuoqg2CmCHlNBv1HgUHFQtU5p4oX_pfp22yXs7e9aY0OezS_feU7yU5EvjqnUm44Aspuw21AELroBwgALAQQXMX-MWB0jZUSHXwEQpzM_EkLnR3HF3DWbVhvEJ1NhGLhNDf8WRyw55AatOfs1j8lJDI2xgczejx6jgBIg37jMlaopuCDSncenjcf6USZ9eFRje68srRgJ40KBFTxHfJryjjDnAILz5-UJCz0UdiJJqjnThkXPupBo-9H4eS9Py2_54v5JAAZsxfjLnqtr833SOoXZyIzc43kBd1770ux-wiM6UQ99pADXnlsWWjXNxQBbv9QgyhAaZ2Vn1VEE48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1594c4dbef.mp4?token=oMLPRmJVozlRj6N99nbKeoyhW0NNc1vJPtejeEWMlkWZtO78Wa34RhZ-0-PgAfwuNfgQQ9Ybf2hYrTQg-qMpjbOjtW26uWcWFQio_E86dur66zSG6BEWM3UKqmWdc2r0eFjxNz5YItUTtOPX__Ke4UFfcH9ai97yKKv2faj3SoMYzg-jYBjGZtmUrUfILtuBjr7ULwzZHJ0LptAzZ3aWh0VZWt1GebIft4wIpLX0rMelhzSSKRYMtqDPbh1Tjy5axtmtHyI3PP9NSsjA0GCfgQxfIYlkY4Vczateh_btFT9hHtvHedni4MdJ5V_BUzNZIyTN9aEu5Pr2Wmf_iHmEZGOYsuoqg2CmCHlNBv1HgUHFQtU5p4oX_pfp22yXs7e9aY0OezS_feU7yU5EvjqnUm44Aspuw21AELroBwgALAQQXMX-MWB0jZUSHXwEQpzM_EkLnR3HF3DWbVhvEJ1NhGLhNDf8WRyw55AatOfs1j8lJDI2xgczejx6jgBIg37jMlaopuCDSncenjcf6USZ9eFRje68srRgJ40KBFTxHfJryjjDnAILz5-UJCz0UdiJJqjnThkXPupBo-9H4eS9Py2_54v5JAAZsxfjLnqtr833SOoXZyIzc43kBd1770ux-wiM6UQ99pADXnlsWWjXNxQBbv9QgyhAaZ2Vn1VEE48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
​​
بلندترین آسانسور فضای باز جهان در چین؛ صعودی ترسناک در دل کوه‌ها
برای مشاهده اخبار بیشتر از چین، کانال را دنبال کنید
👇
@AkhbareFori_Cn</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/666083" target="_blank">📅 21:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/666082" target="_blank">📅 20:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=SiThNycKRj774S4jzi5XHgFM-HQ2BfFnL8Rp5EarxIkZgwzD2IwCcqdpFX_D6qAzFj4yzS5u434qS0WVyn2Oju6e-qA6yK2rp4XDf7DLHTlVVKpLVbkzpY7l3lGVz2lEmqQTdM5sB6KO7TwnpuKfVeHpAckG4YNEQG4h4l3Y-88_bePTYEuOca49KnsNgx3MuekFnf9cBK5MPrDuP_UOdoaTvXsfz4tJv882B0vgywZsen0b5vLwIeMM7GA-cDATUNlQNmd4iS1Vfx0YtlbGlsIysa_iE_tVc4BGZpQ3lq_6EJUYGO2ej1KvxZqN7n8lmgfaqw8CF509xx04r_3ViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=SiThNycKRj774S4jzi5XHgFM-HQ2BfFnL8Rp5EarxIkZgwzD2IwCcqdpFX_D6qAzFj4yzS5u434qS0WVyn2Oju6e-qA6yK2rp4XDf7DLHTlVVKpLVbkzpY7l3lGVz2lEmqQTdM5sB6KO7TwnpuKfVeHpAckG4YNEQG4h4l3Y-88_bePTYEuOca49KnsNgx3MuekFnf9cBK5MPrDuP_UOdoaTvXsfz4tJv882B0vgywZsen0b5vLwIeMM7GA-cDATUNlQNmd4iS1Vfx0YtlbGlsIysa_iE_tVc4BGZpQ3lq_6EJUYGO2ej1KvxZqN7n8lmgfaqw8CF509xx04r_3ViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: این وداع آغاز ورود ما به مأموریت جدید در مسیر تمدنی و رهبری سوم انقلاب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/666081" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f93f1b0.mp4?token=KzM5VZ2OOMFowN0hqoyRPmRpFsxb-CGNCqriJcpIb0EUAo9GKJA-fQarSzRGjhLs5VjCSBZOQohiQAzhqbjtYX1KZdG9EHmZsNqpUgeOV4Jwz0Ec1cQXuehPzDi9qDGwMOKSRnP09-3Dc2qRIipQoolKTCqVRpyPsobW42O0xE-6K7MwFfPKhhbPPl2Wf8gelEkwldVu3Hc_5rHWluDzUcY0r4LGCgaPLk43fZGX_5bjbT59hwtNCFX8NEXDA-JjUjUI0RBCKCtoFjX7qpG6_SPSFsw1iaNz6ZFEdrmR9VYmVGvLnlVZurRTdJmaisYbboHYH9rn_pzqNzgRLscmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f93f1b0.mp4?token=KzM5VZ2OOMFowN0hqoyRPmRpFsxb-CGNCqriJcpIb0EUAo9GKJA-fQarSzRGjhLs5VjCSBZOQohiQAzhqbjtYX1KZdG9EHmZsNqpUgeOV4Jwz0Ec1cQXuehPzDi9qDGwMOKSRnP09-3Dc2qRIipQoolKTCqVRpyPsobW42O0xE-6K7MwFfPKhhbPPl2Wf8gelEkwldVu3Hc_5rHWluDzUcY0r4LGCgaPLk43fZGX_5bjbT59hwtNCFX8NEXDA-JjUjUI0RBCKCtoFjX7qpG6_SPSFsw1iaNz6ZFEdrmR9VYmVGvLnlVZurRTdJmaisYbboHYH9rn_pzqNzgRLscmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از خیابان‌های بغداد در آستانه مراسم تشییع پیکر مطهر رهبر شهید انقلاب در نجف و کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/666080" target="_blank">📅 20:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4nGljLOgV2C47p8cFeTWjn7oiuTYsXbN8VDbaHntvUQfe_9wp6TNXYmp2nzwBjJpIm6EF3XvA16CgDdxI6NL9SCqbEMyq3Lb6ySd3WhIFsU-x0qolvDVe3epSFcVm-JbcLJiJkwGPHFOTVDvUex7fxBkQ2qJzACm84dNK16XBIi_E134IJQONdT_00XRCqBJ3cN-rFcveBmcBuLIq-stJU7ILmzV4YOweWV6GDj5aYj694d9S_Qxkvl3QRrAlgG1zs1bVOTAAEQihpVQLMCWlOixyeom7z5iXQUp4ON3YVFME21aTtvobBOxWThOLUHIbi7C8s5MWz9kfDU5lkttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق گسترده حساب‌های کاربران ایرانی در Claude
🔹
پلتفرم هوش مصنوعی Claude موج تازه‌ای از تعلیق حساب‌های کاربران ایرانی را آغاز کرده است.
🔹
گزارش‌ها نشان می‌دهد سیستم‌های شناسایی این سرویس در تشخیص کاربران ساکن ایران دقیق‌تر شده و بسیاری از روش‌های رایج برای دور زدن محدودیت‌ها دیگر کارایی گذشته را ندارند.
🔹
کاربران تعلیق‌شده علاوه بر از دست دادن دسترسی به حساب، امکان استفاده از تاریخچه گفت‌وگوها و قابلیت‌های Claude را نیز از دست می‌دهند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/666079" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f7c19410.mp4?token=QuwH4cKZ583zcGEJ7kd5_f1ODQfQKx3LN8FsEO8X0g9s3KBFYQOwAIdjcUqIbwRUY1UFgBzdCuogjJxDWqXEB98waOPaC7jHAAa75rNoFTa8-EvuU1uKdaOey6YVvDg4j5bpjumS0-idAO5nKR_gCrajaU2Xcu22OZI4jVh7jV6x6dgmEvGKrlkww35i8mImC0B25AjimOV0zpE7wB1zOMP4u3JFabgcK-Crq6L02uKafyEBvAVxkI1pO3wFGF1oJ7TVMIEiWlGRUl3dE1n8SH2g3vdLgBTdjKyuTYq9bjDHS1X0i_FW7hYn6af_OxOr1-GDK4TQ_1IN-oQX7wU_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f7c19410.mp4?token=QuwH4cKZ583zcGEJ7kd5_f1ODQfQKx3LN8FsEO8X0g9s3KBFYQOwAIdjcUqIbwRUY1UFgBzdCuogjJxDWqXEB98waOPaC7jHAAa75rNoFTa8-EvuU1uKdaOey6YVvDg4j5bpjumS0-idAO5nKR_gCrajaU2Xcu22OZI4jVh7jV6x6dgmEvGKrlkww35i8mImC0B25AjimOV0zpE7wB1zOMP4u3JFabgcK-Crq6L02uKafyEBvAVxkI1pO3wFGF1oJ7TVMIEiWlGRUl3dE1n8SH2g3vdLgBTdjKyuTYq9bjDHS1X0i_FW7hYn6af_OxOr1-GDK4TQ_1IN-oQX7wU_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزیک رپ جنجالی برای رهبر شهید انقلاب
؛
خداحافظ وطن‌پرست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/666078" target="_blank">📅 20:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74183e02b.mp4?token=AUu2Uo1qKh0VGNw-M6fSxZKSazVbd0WVl-x1iKFvkIMcAI0kfVoLAMCtrRbj93wZtdxKNwBuHH3JkXNxUzfs9Z5mFkQZKUJK0fQim0kEaj-KxSw-kf9UvqUtLdSWvN--CA1xX4l4M6qlyQVmg_m1-S8ViYC0I2B88UiJQA-oN4q5PfFdduHf2Ag85J8xhBzeXPNQBdcoLWRQ0JvE65GV45N5RJIDePLGknjX_Kr8geWced7J-8hB0El7mDjdtTm8KUGmoEiAy_UmfdlxZiCCNAja49uutTYWJq35hjXusGz0zMOy-hVJbxVQOXhNpKDG84n8cZPP7Q08L0IBEhkEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74183e02b.mp4?token=AUu2Uo1qKh0VGNw-M6fSxZKSazVbd0WVl-x1iKFvkIMcAI0kfVoLAMCtrRbj93wZtdxKNwBuHH3JkXNxUzfs9Z5mFkQZKUJK0fQim0kEaj-KxSw-kf9UvqUtLdSWvN--CA1xX4l4M6qlyQVmg_m1-S8ViYC0I2B88UiJQA-oN4q5PfFdduHf2Ag85J8xhBzeXPNQBdcoLWRQ0JvE65GV45N5RJIDePLGknjX_Kr8geWced7J-8hB0El7mDjdtTm8KUGmoEiAy_UmfdlxZiCCNAja49uutTYWJq35hjXusGz0zMOy-hVJbxVQOXhNpKDG84n8cZPP7Q08L0IBEhkEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ایندفعه ما برای شما با اشک میخونیم:
اللهم انا لا نعلم منه الا خیرا ..
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/666077" target="_blank">📅 20:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666075">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادای احترام قائم‌مقام وزارت خارجه عربستان و هیئت همراه به پیکر مطهر قائد شهید امت #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/666075" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdy19qGL04HMY_3pKFmT2Kc-BBh83TPj0T4i7p7ENYyA_t8qjoaS3W53WL53WwAVAUqDVG19cPjNR-ybwwmOdyy2QjCHGMluMCM9pN1IJomsuPfGbZJYKbfX_ljdbK7A4hKs6q-dlhzuP3p2xq6tb2yPCYkWt5Lynkz-OlOCLGYHQUoDFAXV2g9a6xD_Xf25JumTi--Sf22XpSUbOCVSUaiF-i042esMC0bDsNMlDWY5sbOFFPiddOOKGvRQvy8lz-YK2SPr0xnF6LPPssbg1orkjkYSAFF6Ghs6ZfKhDAneqzq3Nl0gIdi-H_GgsLAhieyw1jXKpfmbJjfgzFSUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیصل عبدالساتر، تحلیلگر ارشد لبنانی: چقدر مشتاق بودم که از شرکت‌کنندگان مراسم وداع با تو باشم، ای امام، رهبر شهید. ای عزیز امت، با شهادت تو ایران دوباره متولد شد و به لطف خون تو و خون شهدا قوی‌تر خواهد شد تا سدی محکم در برابر آمریکا و اسرائیل باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/666074" target="_blank">📅 20:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=dy_VVPxwwHgOMfOp6KRjzS_p-sntVY75np38dX67n5lODxQiG7ONOhQOeko_cTduX5OtMOMApLgmhPGVqFOITmbqBgpAvTTuX7dElF4RQrFcfS_mh_otOlYBcZNOkdpxcP9GOTaS-RMvD4YjhQo_TKFy2thLfuxef1ruRI2sZW5D9AS3PtV0XV285fDWIrAWJILHOkM2Q8naDVIdEe-AjRMlAuzAlPKPZVthC5jFFlZ2X_YLj1rSglaVYMUIN1vo7AQ58TyUwbVwot-Xb1Gw1IbSpNGDSeos8b3rFWWdnmszaqC-ju3vhnYvXdUcvIj1FQSJRM43UobB8Q8H8IubmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=dy_VVPxwwHgOMfOp6KRjzS_p-sntVY75np38dX67n5lODxQiG7ONOhQOeko_cTduX5OtMOMApLgmhPGVqFOITmbqBgpAvTTuX7dElF4RQrFcfS_mh_otOlYBcZNOkdpxcP9GOTaS-RMvD4YjhQo_TKFy2thLfuxef1ruRI2sZW5D9AS3PtV0XV285fDWIrAWJILHOkM2Q8naDVIdEe-AjRMlAuzAlPKPZVthC5jFFlZ2X_YLj1rSglaVYMUIN1vo7AQ58TyUwbVwot-Xb1Gw1IbSpNGDSeos8b3rFWWdnmszaqC-ju3vhnYvXdUcvIj1FQSJRM43UobB8Q8H8IubmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/666073" target="_blank">📅 20:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666072">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پیام سخنگوی وزارت امور خارجه در فراق «آقای شهید ایران»
«بقائی»سخنگوی وزارت امور خارجه،به مناسبت آیین وداع مردم ایران با رهبر شهید انقلاب ابیاتی از حافظ را منتشر کرد:
🔹
نفَس‌نفَس اگر از باد نَشنوم بویش
زمان‌زمان چو گل از غم کُنم گریبان چاک
🔹
رَوَد به خواب، دو چشم از خیالِ تو؟ هیهات
بُوَد صبور، دل اندر فراقِ تو؟ حاشاک
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/666072" target="_blank">📅 20:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رازهای آسمان هفتم از زبان یک رزمنده
🔹
00:08:00  فرورفتن ترکش به چشم در جبهه و جدا شدن روح از جسم
🔹
00:17:20 آرامش توصیف نشدنی بعد از جدایی از کالبد دنیایی
🔹
00:23:20 حضور در مکانی که از من یاد می‌شد
🔹
00:28:50 درک و تجربه شدیدترین درد
🔹
00:48:10 صعود به آسمان هفتم با همراهی ۲ تن از ملائک
🔹
00:59:14 ماجرای شنیدنی از اهمیت دادن مادرم به عزاداری امام حسین (ع)
🔹
01:04:15 امام حسین به قسم‌های مادرم پاسخ داد
🔹
01:27:90 درک معنای حقیقی حیات با مرگ
🔹
قسمت بیست‌ودوم (اکبر)، فصل چهارم
🔹
#تجربه‌گر
: اکبر بابامرادی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/666071" target="_blank">📅 20:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666070">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965b9bc9ab.mp4?token=btQBz0-LOj-57tbN8F827rP8DhIIiydjgxhCyujcWTcByTkkKr82zMsmHXP1CsFjwhOwP4FmF8uhh8KE_I6wBZE1obI0cIRlJw1-8y3MM7rJghmSw5NDlkdizQkkeu99beHLtqu-b9JAhQD5LXS6fI6KG_0ibXD_ruDDbdKwK3IcnXCn-hIBlUK7nf1TBrydTQ_IcxrAs-ijv37xTL2hJsD4MwxDNbe8PZCQH2G6uk_FGTkgbF0l7u6MToVM2XRYk9C5F5vI36V3piITQOsk8XRmNZY3hVrvHUSgF0uQbOEBrqCcncLgkNdFJ727RLOPCOW5uIvJ4tOdrWHT6gaZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965b9bc9ab.mp4?token=btQBz0-LOj-57tbN8F827rP8DhIIiydjgxhCyujcWTcByTkkKr82zMsmHXP1CsFjwhOwP4FmF8uhh8KE_I6wBZE1obI0cIRlJw1-8y3MM7rJghmSw5NDlkdizQkkeu99beHLtqu-b9JAhQD5LXS6fI6KG_0ibXD_ruDDbdKwK3IcnXCn-hIBlUK7nf1TBrydTQ_IcxrAs-ijv37xTL2hJsD4MwxDNbe8PZCQH2G6uk_FGTkgbF0l7u6MToVM2XRYk9C5F5vI36V3piITQOsk8XRmNZY3hVrvHUSgF0uQbOEBrqCcncLgkNdFJ727RLOPCOW5uIvJ4tOdrWHT6gaZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ارلینگ هالند اهل کشورهای دیگر بود؛ سوژه جدید کاربران فضای مجازی!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666070" target="_blank">📅 20:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
استاد فیاض‌بخش: خداوند فرموده است اگر به پا خیزید یاریتان می‌کنم؛ باید انتقام سخت گرفته شود
🔹
از غیبت صغری تاکنون، دشمنان جرأت شهادت رساندن مرجعیت را نداشتند؛ حتی در دوران پهلوی، امام را تبعید کردند.
🔹
اگر مسلمانی به فرض پاپ را ترور می‌کرد، دنیای مسیحیت علیه اسلام جنگ‌های صلیبی به راه می‌انداخت، غیر از این بود؟
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/666069" target="_blank">📅 20:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXKGbGfl2tTZF01laDqPDCDGCglxEwW5ogMBMdUhkfIf_JHRW2H-ZbrOl13-pPdVE7CyIo03lm_NiNNgTcQiBh8xlszcl75fyRCkYQkmoWLb1lswzodr4HvfkGaIfy3Csvz2TDQCJ9NrZPF_m676xpopkEoWyj7GOw0z1BmN78DgVN9Q0jikq9u_po6mVc5WISiqXaHdRPNYN0rbvseiOp0wGw4i4BWpysg2Ko2r4xDqu7HwW-0XgYuVQ0evRc2Zpblis1tzY_SgCNs3lEZdiiPdaoS60rhzcdbFvqaIthbVJmFRylxyBKkVLJZV_ZZ6d8Sy4IArwnwolqIo3hAEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی داور بازی حساس انگلیس و مکزیک شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/666068" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffcaee042d.mp4?token=rLW9hZPoOvBMRB-v0TjJVnNegQHAqkalfYEnz8tloxCjuvlONsIpPNPnq0cJllnXxCjhnj7HD9BG5bFojemouhXFTrpjtyvlqSCRZWvUHJ5XBiNhvIhCmRzOENDiEH2pi8_eG-_PcDAX_q1_TeKNfyxdNCcCwPU60_EenyiReRbQqZDYjWkvbA9O8Bf2NJ4GUl91aPCfKR955PFaYTyx4mSgtNnV8dnkbY6QKjzvp25sqNBUDoRZFUSHFSQkA2ry0BtQQ0TIeC8GRqP9ltSV362istBEeThzFipKaujbgQ7EH07WkRy5v-aoLAJgvRlAeQvBgSbU0xHQvUw8Sh19Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffcaee042d.mp4?token=rLW9hZPoOvBMRB-v0TjJVnNegQHAqkalfYEnz8tloxCjuvlONsIpPNPnq0cJllnXxCjhnj7HD9BG5bFojemouhXFTrpjtyvlqSCRZWvUHJ5XBiNhvIhCmRzOENDiEH2pi8_eG-_PcDAX_q1_TeKNfyxdNCcCwPU60_EenyiReRbQqZDYjWkvbA9O8Bf2NJ4GUl91aPCfKR955PFaYTyx4mSgtNnV8dnkbY6QKjzvp25sqNBUDoRZFUSHFSQkA2ry0BtQQ0TIeC8GRqP9ltSV362istBEeThzFipKaujbgQ7EH07WkRy5v-aoLAJgvRlAeQvBgSbU0xHQvUw8Sh19Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظار مردم برای باز شدن درهای مصلی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/666067" target="_blank">📅 20:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: توسعه همکاری‌های اقتصادی و ترانزیتی ایران و ازبکستان باید شتاب بگیرد
🔹
مدودف: روسیه در سوگ شهادت آیت الله خامنه‌ای با مردم ایران شریک است
🔹
انصارلله:محاصره فرودگاه صنعا باید پایان یابد وگرنه فرودگاه های عربستان را از این لحظه میزنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/666066" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
دفتر نخست‌وزیری اسرائیل: بنیامین نتانیاهو در جریان گفت‌وگویی با دونالد ترامپ توافق کرد که به‌زودی دیداری در واشنگتن برگزار کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/666065" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj2Vvgu6QNcdFNF5UIoTbU1IKdNIBxw0-YRxfn-GMIkooUVncoXrdolQfsV3i2PKkgVcjoXu4q1_O0jn5benC9wPWY9ve8kvgKyqqDLCZG5wujYOLFfSR5Z-rI7vXI1beZemWVh89ajmm2uOFzcpnoXYG8iLAcWr_-F_9PRhNzxiKqGcRVimlsZVnRU6iE3S-76pOOa9kCgGXNtuhcL8s1OUhheH8m8iMoF72wicgmRjY-e98e1mnwp7tA2tfqZeJGCbOnFHvbkpVckkyI2u1JGGdidlt2iy4C0jWu0TyDOoP_0tCKG8sUbg7aMgFYAgu2gSMfD1Fjk-nhtXvAyxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/666064" target="_blank">📅 20:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حضور بافل طالبانی، رئیس اتحادیه میهنی کردستان عراق در مصلای تهران برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب اسلامی #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/666063" target="_blank">📅 20:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb2931460.mp4?token=GpA5p2J9g6o7JxWkRjNToVUSkMtzhs361MgOBEHWo2RDOtW261ZzunQD9kVSOTEtwL685GHRtasDpDmicvu8xx04dgbYJ8x0NLKfNmziBztDNLfuGHwXu4fcMmAmwcJ2RUajXPPEazR1rWt4E4axOa-_Rnyrknj89teamvrxNyBVLsjVwbEjY3hsX4_fClMf0I7LE2l0XV2iIs4wZIcRXEkDLN56nQMLUN3gGDMxyXLhJB0X5c1uTY5u3kwWkg4r1lcL9iKOZKxRLbb0AFW1DOCwaSq5IWX-7Ivn1SBA2pyL6AXEyh2ysuzuedkKevePXgfzIPfx5E2sqNBFkkJ5jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb2931460.mp4?token=GpA5p2J9g6o7JxWkRjNToVUSkMtzhs361MgOBEHWo2RDOtW261ZzunQD9kVSOTEtwL685GHRtasDpDmicvu8xx04dgbYJ8x0NLKfNmziBztDNLfuGHwXu4fcMmAmwcJ2RUajXPPEazR1rWt4E4axOa-_Rnyrknj89teamvrxNyBVLsjVwbEjY3hsX4_fClMf0I7LE2l0XV2iIs4wZIcRXEkDLN56nQMLUN3gGDMxyXLhJB0X5c1uTY5u3kwWkg4r1lcL9iKOZKxRLbb0AFW1DOCwaSq5IWX-7Ivn1SBA2pyL6AXEyh2ysuzuedkKevePXgfzIPfx5E2sqNBFkkJ5jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سیدهادی خامنه‌ای(برادر رهبر شهید) به شایعه تحصیل رهبر شهید در روسیه: این قدر این حرف‌ها مضحک و مسخره است که نیاز به تکذیب ندارد
/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/666062" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP9kMEuqW0ZwzW-qcI9VSwfpaeCdsNSl2QmsmYsSq-14a1d8LYegX6aPaeQe3-EciTmu3BbTQ7ugiGUFuapb21r7d03H2OyRmVVQ0gmGKPDpiPIssBkXi6AGEeUsII1VJBqNq_44WNi5d7wrI6yO6vBNtMWMHObY7Znj2zbuY0SbY-wf2Eu-vpmL_IfO9MxMQsUuRPKCsh2HfyP0a2iosTaxnYxmQiddi_95MYFM8bgNkx1ktTim8y98B1KVyisD6sPgrfOVExZkUol1TBQNGsjMRr3aon_lsFq0cY5LWAxM-2iFPuZwHXjRyr1jjyhu8iV-j-zNDfdt5_m1NMaLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت قیمت نفت
🔹
نفت تگزاس (WTI): ۶۸.۶۴ دلار
🔹
نفت برنت: ۷۱.۹۲ دلار
🔹
نفت امارات: ۶۶.۲۰ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/666061" target="_blank">📅 19:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری‌های شانگهای به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/666060" target="_blank">📅 19:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3a42644e.mp4?token=CQoCs0xaFPqYmPynPbUoy4nTc6SbE79inHd3NsZhIgafpUWHZ1wg0WKV7NAqjaHdAuR7cdH_Z2bobnFgrXkc060lJm4VNFOK0Ku6IhQ3G8DKpiP2PdxSKY08Bd5hKM-e28cN-T4vRVLsAKAqWDY2UJWyZ-2Evz2WmynnBuBvVlkSt-JO1WqqPug9ubcpwMRiJfsIzOa9Uy2Az9Is_5TUsH1136hEFU9RgW8mAwO8pC4wnuBEzOV_zexlrDZKq4HletLKTdqI7-9GKNFVMX5t8lfMg2yJ8C59Z5F_wsnWIgZ4SlXuYuMu9x1j5zDsh-PmkXIqrKgwqhWTEP2g5gQb8zIGtK0M4e8S8zvUe-BlwqhGfLgPmNGO7Q7hJDA9HC629GnWISOxuVIEbiA2LWgVb79CAQ9tNRWaFmcwr9HE3ZN9mjBqR_Ow-lm5YrgB6JGfPdcvsV1_gZkv4rJYGCYIXbcspx-xUwDZr4DdZYGT8-Tv_Uhir-9RMIl0gXbc6Ip2KdKTcq0_AoJaRUIVUgVPTSoU5O8sHo-R2LQOfSEca1fvg7Lpq0aUiGbnxPAfAEtqlHNvRD3YeJGcQF85_6ch5aR7_CNLuVhQBtbtMn4-INcPuo6ZYmq2w-CkspRb-YymkPCViU3DI8LsZNHxYSb_rjYKcRJ6NSCK_f7fJaIVuXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3a42644e.mp4?token=CQoCs0xaFPqYmPynPbUoy4nTc6SbE79inHd3NsZhIgafpUWHZ1wg0WKV7NAqjaHdAuR7cdH_Z2bobnFgrXkc060lJm4VNFOK0Ku6IhQ3G8DKpiP2PdxSKY08Bd5hKM-e28cN-T4vRVLsAKAqWDY2UJWyZ-2Evz2WmynnBuBvVlkSt-JO1WqqPug9ubcpwMRiJfsIzOa9Uy2Az9Is_5TUsH1136hEFU9RgW8mAwO8pC4wnuBEzOV_zexlrDZKq4HletLKTdqI7-9GKNFVMX5t8lfMg2yJ8C59Z5F_wsnWIgZ4SlXuYuMu9x1j5zDsh-PmkXIqrKgwqhWTEP2g5gQb8zIGtK0M4e8S8zvUe-BlwqhGfLgPmNGO7Q7hJDA9HC629GnWISOxuVIEbiA2LWgVb79CAQ9tNRWaFmcwr9HE3ZN9mjBqR_Ow-lm5YrgB6JGfPdcvsV1_gZkv4rJYGCYIXbcspx-xUwDZr4DdZYGT8-Tv_Uhir-9RMIl0gXbc6Ip2KdKTcq0_AoJaRUIVUgVPTSoU5O8sHo-R2LQOfSEca1fvg7Lpq0aUiGbnxPAfAEtqlHNvRD3YeJGcQF85_6ch5aR7_CNLuVhQBtbtMn4-INcPuo6ZYmq2w-CkspRb-YymkPCViU3DI8LsZNHxYSb_rjYKcRJ6NSCK_f7fJaIVuXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظریه‌پرداز آفریقایی: آمریکا ایران را تهدید کرد، اما خودش با بینی خونین از میدان خارج شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/666059" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ امام امت به سلامت</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/666058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
ای ناگهان عزم سفر کرده خداحافظ
ای گریه ما را در آورده خداحافظ
امام امت به سلامت
دیدارمان روز قیامت
دیدارمان به روز رجعت
🎙
#مهدی_رسولی
#رهبر_شهید
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/666058" target="_blank">📅 19:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
دیدار سردار ابن‌الرضا، سرپرست وزارت دفاع ایران و فیلدمارشال عاصم منیر، فرمانده نیروهای مسلح پاکستان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/666057" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه تکنیک عالی برای کنترل نشخوار فکری…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/666056" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666054">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-XjI8SL_RXpkZ8CrmUblLUgNqGwtNZ7ZLF21wYykDydVYK2GXTUXY8ZuRuND9_EWO7ahtujSHSsJ6KTLQdyI19NNTZfciX15-OxnNc1h2OluK3BkvHXkPSOXiVxy1ROBJLnjl8s8Y9TRw45BinzoZvz_fLJrmCfVLfAx8sLufa5til2SLa8zf11apuC4hOc_toEGBBLQP-yX3HcdAMpRiadnmb7v-yc8xvzrbljxN96YH6agi9kmfDVF13JzklP_j2GXMem12cp8u2K-s1odBPgPi4wrdwa1E1wTD4lz_wsbNiviYOhDzQJaTBaVjP1QAyMWjFWrzFsVOmvviIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داماد شهید رهبری دکتر مصباح الهدی باقری به همراه همسر و فرزندانشان در کنار آبمیوه فروشی خیابان کارگر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/666054" target="_blank">📅 19:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666053">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSQrEVi9keVDibfoGjDGHywNPCACx2vPzj76WFqnChbFrwbbmbjVChr_2pik4WJoNF3xLShvBkNEJSkvdp4I34bOFefuNWh4cqcmxdVn4TAK5akYvbi8jAiiyGl2nUy2GyutpfpMIWkeMIh59XwRiebI3ggW0tUYf6UFgKmi1Ol6htwFKLay8-6sdSMxsuAolEqoTEFky2DDl-hl3MtNMCwrwO8zd6-pflSAQ7anIRzmiWoaneRkEaCgA0PN_oUTbHHOf01fChwAafaSP_xxox8ENSvdfo7MeT3l49y1RtcKd_BSExu4fGz97RdocLGbVrJr3Oh4rIGWbI2sBxR3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار عاصم منیر با عراقچی
🔹
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان پس از شرکت در مراسم وداع با رهبر شهید، با سیدعباس عراقچی وزیر خارجه ایران دیدار و گفت‌گو کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/666053" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4fXfNpaQblHBQ-YjJT8Ev8_IfWGqTXSCT6YvxJ9ZD_V_9NIkK92A8jux9qWaMmRDx_q6OrpT7KGOEwFw2vIAvYAXXgAwTjXQXBaaIMIhJO41TOKJNamVKuN2oW2HHaIMJrRbsmz4EK0J9FTbXNR1gEKCVsoCFMU64UdyEZyB6nEej1uWtj5Hq9HoE9UE4ZwlK0GUS-ArHi78k9s40eWjXy6AOZF-fJ7HnW2FyGlBxi96khiSRfFagRN658cuSovGPMYel5NLd0Da0Jncyy6g0y2r18Md_HTSvnbuQk35jWSiFd0CPpRU-GKobqJzVwR083pD6k_fsa0QjN1ADJ7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشتر به سفر خارجی می‌روند؟
🔹
در سال ۲۰۰۰، آلمان، آمریکا و بریتانیا بیشترین سفرهای خارجی را داشتند.
🔹
در ۲۰۲۵، چین به بزرگ‌ترین مبدأ سفرهای خارجی جهان تبدیل شد و هند نیز وارد جمع پیشتازان شد.
🔹
برآوردها نشان می‌دهد در ۲۰۵۰، هند، چین و آمریکا بیشترین سفرهای خارجی را ثبت خواهند کرد.
@amarfact</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/666052" target="_blank">📅 19:31 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
