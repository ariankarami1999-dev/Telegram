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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 424K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiMPOzTfymkxhsqm6Z94bQmlsAffhLdLgJ6QwKShAbheF9xqD9Sp-JsafB69me6foS5Xb1P5iuywXGIhAm7FxtJ3bfwLwEvaJNMcby_E_5WAGi6ThMIhjNSBCANrXEudATeA8qut2fnjKgglva0syi3fdETwXRIzDVAx0iMGtK22h2tfQuTbYyBvDp4UhYopjZ67fd6ZOAuo7qaOLF1xt5ZwjDo88rtrqxCI8OxO-2EC1DlJxKjZYO3FkNJaJxdvEO2b1Ys-whec47_sEm7ktPnFrJwb-k2815wbhal6feYFPkAZxztLrfvENZSkii7fwL81o22eDuKz26jKhWiO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08az2MUJsIz5uBlB9Wj2As7wYWC9OcP-06L7S9e3mO_QEPs-cIcrcWWfC4kGWLX8URbzvbGOBjczy8PeD_GTBl2AxG0BFHuop0_7gyR3qibVP7q0BB6u9nGh3jYFZ9v18_ZqwAnYnjXdhoFCDyQjddWIdUB6gx_Z50duobQo6eyyGD0jpb9eZ2hmm7hPHsgef5sLu6ZOuw3FdUqj7JAcD5gJNwz45nhPUxvFW1gBick5nNgT8h_SilJz8Bm7THml-drobqJKosj6EpHjIyvplHC8UC_T1v0STtgF0L7N9yAIuEsS_TU6XE9j0FD6NEAs6MFhWOB7uaLO_nO-qposw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvARRLiA-7oBSC_8tRNGkzqh4dChfqL4hMwaHTpg4L9GhaPQjmCyG14WsAcW3BXFqdsxceBuXJIiLCF_ClDXFCKbkQFLgJl_5QbKaYCY5gTt0pJ4GPRYYARyONNv6jym223_QVwVm6VbSfpp44m2QEYPweozlThxCI0R2qY80F7M5A8sCYl3RACrptXOqFeYrtLKXilK7Xmvu_xLfp3G9tz7fQr-XuZ7T5kGU8B2ypqJ45R0AeYUauoSmesBfZwFjKboPDTqR1uBn5TxWnfL_nuESJw4e9WTosMiCTcuN8r01KrN6yKDYV_pppNXA2Qo92e6FiQpNHYkxxRCMzY5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rutWJ-aS4A2ppOXmT1dr1AKLIvV9Q63AxkLDNdhuLxr4aGm-Ww_rytRW4GFw9dGm6cBpiZfXgXomxqaP5OsN1MlDePzgBpx0kRbdffm3n8XuthYUbjAekkxNqEIh0v6s8R41BjEHLUQbjxrhOdpQ5QS1Dujp3CPEqak-FUHDoaHVnzSFNu0CHIrL4zUO7Ak3jZ9WfQiC1N9ZtGsibvdQIbLOTZa01Wex4xS8IjOtlnCJqujAax0CvfZ-Ep5EQXA6galqN6pDtDn_DNMRtD_QCzaJ0K29FmwJvsJVzdjZAzTfBXAu4RzgOE7nXzUn6DqeuY4H4SFM29eooc31IFgrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm4CnRcR49AB06gTq4ZNpYLZYFzefnIKGuO6iQfRZ_LICE3Jul4wj0gYtyE4RfCHtOh2LJUCBTi1seSEoX3VDS9k7kEcE3SuoXNzp2CZp56lMkd_8t4wozFyyaz2do7LEQmxlQAfIutYxkI53xQFtRV74ocozZ-Sv3wtzLQufjixHxbtLa0_ZrzDFfYaXlruU4XSG18mI-420LnB0K2YxFhwULiT30vK5_g7VWu1g6zbR2CGBKXkTWKNKi6muJGRS9jFIdeqFZ6g7dSTvtvYgyG0ZAoLvOhQNNbmLedHz3GM4vePD0bWDMMsC__XhdlW6tRt3cPYcWMYkYyO9UVaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvW6LCyxYvvJAD_Wc0c-tMwN3XA7IIHoatTAap8o9N8a0d1CIhmt3G8SMWE2Kbl3jKy-s2nHMsUebSqSA29eeDDOvW_HxaHuFztg1vDiq7PlOnHNVOwSikmgb5ub92HkheXI5gk7qv0gOSQvaNeaciI0iugBisialqZAkqb5Z_ioiGkgK6kXcRH3i4j4Bdp75QwgMwcYBGbf5lklOsxF1RxkQ7mR_S9SbGrmi63UoCFdC-z-6O114gZBKw3F5k6VJBb7etd99kAvT7onzd0bNAbtGi9BHGtzYMO0WQ0yvK2WOSYJUy8Ek4ohe71yLRZc8qeJmLN-a2dsDnjkzmyvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWguu9UU-Ll0EyXY0O2akFAK1KJkVhjcKuKy_EwQd8yM95_jQzlt0jVXVfJqi2sVwB3GGTafhu0g1cw2dS2tYyM_VoYwKHFArgw44oauNhHE3jlhy8U4YqEU8T68bxK_xSfcD9RlvSMzt7Fg9DrxA283NXeRooI8VKGOukAXdCna-VuxZ3wC96--vDqyYIIwbiddRQ-d6K9Q3tykDqrVy5eacmbvodDyBFD6-8eFD6SBy4XK4duG2BTxstEvhMd10r0dKlUUE360m9SyCjEIFC0hCq3zcP-0gzdbzihG3YI0LKfG1o5UabzG-smgP3eLfxaF_mOxW3drRw4cfjV7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQgvXUZGDtq8f0Iyz4QpwlALcMjZwC41j-YdumBrdpdX-ofekd7JBi8xQtJQQFk1ycnGuslzjsi8Fh54qgVS3oPh1HylfzTi6upD9hd7YkUDDyQY6mCwSDE8W-hPO0QhHDZaQy9pNxhvC7X0FMMW3ElZJE3DOIAnTijzRxS-0YjFeKyhmPNs2bLam1-5iYuR-Hue9kACCDWU_k0W3u2zL10WbUyMXQodQJTXmigtSf6LvdXjQ54JYeu9QuMRTyJji3HiUVWuyB-S9YN7Eij15uLtt6UJH4qqNzgEWQVKSv3EyskA3jUkyXinAtYdVAGyON-h5ZmPaHw8W7PZSZBwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1yT2uz2ZZs2ZAOUCSBabcnN4fj_MPtQHO7SoxZED-7BFRsd681xtaMpMobgopTeCN6x2IBg97K8TxpPz0grnJw_wFFwn2DJuHnVhDb_LPwH6nhQoq6QZJRf2nXkMlgjbenf_KJKWAv7FsopGicaGlwgjiiAvVk6GYg7IXy_YiNbc8FbG7sajSWD1NO3bkyiFvTJhbqOd4dE44mvfMfnL8SMVkPovPxtYohWz4gFuMdKhznHdvy-Jt9gNRZeC6pchAYW38LqYCJkk6tJCGQJ-JNlHd-q6vAq8HbLcXXEYpWB8lPPUFBh9IYV5bxTcc1JZFSjX9GASRR4iWr_p-66gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7G1V4OsRS2w5l2i2gMa5V95OhXYBHn2BUC4fPS4ghNVqyxGOGLuUcTlsgDxocFZXynS85JzWy3q1CwxgHdQ5jYEAM6Ih4nwiQkU7l7cWQwdsuin7d464x2MVzCidte23of9FPshv1TU-Sqg_Z2x6aPUqRnenpOfzH0YMm8mnpT9a1WO0OlqyUO80yRVQDz2fOpt_lFhETk8R89STd-Lsl1_W0_8IulJRtp5cgf0S7uPB3p1kr0WNtZywbMExaTG5-83oEeu6kIzUB2yjPJTQ6htxxMSirMUhiBBN7v8bwRCwwjkEzSSGpCMyynCql5q90X4QHY0f5k-MC-Mr8f35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIX5c4QIgqOxQaKphC5SFr9J6eP9Enwkh_S7xK2vXNTOwrRXoQsWRHCDHGY-cTeaZ5K9G1OKh7j--4hJ5zuTmxB3vPalIb7sdVXbe9qEPUAYlYkJJ7xHckjRsM46M9i7Ybyame_pfrKrafc2_arQOkEoUch0obpwq2jppadPWris5Cl6b1yrPQV9n2tVT10RUREMNebsWfgtXiXmiPnYHz6wq66XAPZFnC90nh1wpf4NkHhj5QDJAn-Bs9hPl8QnKvskcs9J7XEf8jnVWIVjGLkCiZRvXWeM6Rijrajd2Nw5f4LVZzcdabYA2tWdpiMhp4fAzsfPES2pIbhAUYH6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Rc4CtwFINz-euCeStzljOLei7JlRtRLJQy7ge6qtqlUHVV3eNJjkMFSKCJPKutWBzxy2AQq7brXFP6Rb04nsiT4ofFjZGNZVrxICHWAjqXyZIwbLbf5gyUt-kHRybDGMJTe8INOG3pic8ZzVGfHZgZqTa62RerBe_x1BJKwasbwrsTkShYrPF1x34J8jUhCWtg-jRgrcCxUGuGUMbh5p9_W6OryKsthmzZtNOAlWgke4ivnxGn6cidaKtzhofGVLBhosfeas4dDlBQaaTAPCP9DiMwUMcL4ekBDljxpHRmFqAghWSeknsDqoM64NGZBWpFXhNs83kBVrbSK-Cwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCyI3h7CdSXfOTanNHzaZY1vvirSOjzbMekUVFQuTzdIepP_62jUKjS8Uqo-C30fLyxMMDHjDRGP3B_EerMDXSR4DhbnUOhqgYSB0zuWgOwcTivsHGby7uJtpJfdQpi3Akye31vKQC1xCXSnq6BkDpwIKMFhFiykNQcH5MJx0On3ed_SQzEFBc2zTkjkwWDKKrF1bnRejw6pSXwlRdN_xh6nDHJJVwD1_U7gzvdHwCCknNnuefhG4Z1UhwlVxzaNAVRSTfUt7k0rUmLSrPGO9NjUtBlUwQED1_s0M_QZ0QK705ed7bRe4vvmEHg66EbTEzx7KHNumYZcCroxurVU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkfdgH8VDVZKikJAGS-tHqza0NX_LbEIQr7ShnkVqf8Jc4i3W9aKpEFkDKUQ-Xzs4DIvcF5C4LGOiiH5NpyZxSDVeL5oKLbnZ1czBeQMrIUiz2j49YF8mgktRMslaCBS8psWqWkSnU-GIJhvYtxs6fZvWxrzcOZzoEsOGIamMIltM83aEhtF1mm5crlci68Okj8usmlHYpSsN1CrHSJyHV3zx706qfIgxxnBEd-BnrlmXqaQW95TosMiKv9sz7Jq_JBISCyx7G-GsXiol7waX1GSFJ8KaHnq_e-2xaXqLIb8h9ViCtimUVduuk4tzZzXEqXCY0FwPbsD3dKmIXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKafCsAWx3Jk4qCe3vjb6UoCDXsNx_rGIaxBsYmwHFIG5N25a0FH-zmQ80GDgZ6qnq7Y_d7bIrvsXtkbOwNczPByhTm1ye0K01upuLDQOpznIE68SKMRWGbvkQLRdx28La9Vn54JtHGI6z-gwjJcMz2rzbxFkDsBvAK_fx1ynYCd_QwcA54cdKpK-vaW31XBbkKWraPBTiZjjSA_P3jIblM974NySBZ7e0s-P0i8KlJyfRhEsuljz6XD74SkXXNRcVgCeUUtzDSIMd05xnIX9GDCCuY6gXbrdkiVgzJlIzLHHb813i__ZUSYiVObLYsuBxA2HOxTs8wwDKvysPLL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL4m_RTOwkpu_diztFnW9lf4yvcOIqSbcRzoH1qx4lur01djzBuD0TO2jJ6t0P9U7t7UNjR0pHpZrFP1wsOBxh8yAsHZxjq4si7A9XWQ3MHy9IO-viM_aDsFuAAAcXN0YKIPAnTrbQRG4py0L6btaP3q4c7songFaq0n_9u-GnR-d_7poI6oivQ6tLE5GfzO-3rGEf8h_JnyU5Elplfhi6GEor-hezxpcGo_15oTzz5BRexm_znCX2QwfTmGXjBLeVziuIkw6qc_9WJaQISzxG55prRc8CigvsSvTj6iCgPNwKas0Bec-Oqt0j1Pbecc5_8IuWsnwcKLpxGyXtm3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWXykUQGfzj9sACsoCI0DIjk7Ayu9RB4M83ktoAWZ_wkU9H-DCOVGLSX0_PNaJXDfvfDKav3fSV6fPbS3efBnM_uKY088JHvojlA0YfNzXlQkTnyS7VcJJoPVh__PW-sqA6ss63z-XSXjMU3O8yyx_DKxiUAiKG2kkOq-dViRUeLjhuN-JqgIbhc_1nlQM9XqQk60mKFg_W-K4Mat0zzGPYxeYU-AuK3hVAu1to43H-IH9x0M8w1Ix1ylI7igvWiZ4cAqlo1awZXASdyIRC6EVOjGnbJmVCvP-6v5akr465L09MoKoB_cc7a4flIcSfHAEuWvipNxtU8qLRDjkHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTemXLV_bWU54sQCvmTXJk9ozAiBjZ9mkbeeolUfzsMLjklG3lYNWVUF0-PPDS_bLZ_P7MwRYyD8LbRfiGUalxiLQBuocWkWSjW8aZiruGT1GJXwT7-liHpJwYixy3ZuWQOENFpEcP3_UjDtO7X6HjKQA7KfQNLjNp1IkT2U2htIXnOvow8XL_6BnOYM4WDBnhh_cUYiQVMhuC1cKP7ElNCsXgtj498dJENqsDIwMncjQ-FZy-xdTssqkrDNDjnkWWJ1l3tPXY-jkyfglo0f8bUuoJu2XNTXEUh84LQ9KWgvPvk0EzTDbo19em1r2hRUyE7TdEJi95QHhSVCtGiYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlpiyJGLhPBNRSiUdnSujNrbvH46Mb-advRRtV3JmUHFuW5HFe5t5bJFf75Ce9VyC2K7K-eM0H20miWDN5QmikP6CdGxhwhmqt-35lJrNYdZdBq1tJ3yjSY2bAZrpQpfeGqWrgPGISqO8csVcTw2EqKi4fzxm5kasiemOazmMsok7ENrs2AIAc41kTgky5Nnz1vyArL2K4Z2SlhYv35GITvBbWoHqXAd-nAL7aqZZwPq_KET69yXEHuZVNgDImOIfLXwfM2SVrZk7PnJwbIWVnOTrv-x6R6Aq8TRgDBrVXTSL72l2L2ISmuH58P4UtvSAHi-SFPsnlyioBHusQkETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tagpIDIlETH6S8ELHIoU4_KEDSLk0jpygaKLKguwuLMUCbMXQjMKIXoiHcBrqFVjvXSoeLLde5Cja4WdFK1r2kXn6c3N0FVa3fcidYfo1JvnDNbTmlKX65zaxY_fA_kosA31KVmQKpbsA9Qkf0kVQl_VFjlZ8WKkoINZlin5rNOJtD5bdInFudyFiMgojehcofcHM1gooAKIEseL7iOXquMFTzTb5gXs208VwSoes4m7NaiCrrHhDpY9BXqPVNAck2St80jr5dqgGLetvqBYLcO9JV9P4LGPqUKFOFGDXchY6ZAFlTH1U0ptgi6mD3mILM7vtxL15ByNJYCyubDNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRheRWbXZaVNtwmufKtFgMRJ2iOR3r_y0x1-9HHt9FOqCXlHqCDREyqZFdLWkXB1g9gk6vvgHWsrFCPIRVvDYqe2bmqdo-eookibACccIsl8DAOXuA08XDiIJ5ZaCIBn4KUn50vv37fKZCznI8kg0b3yfBrliYjOQ7pAoqPhHLdZZyziqMfCE0xKaN4hMqUEQ--m6Ob6WE0BwEacxS64-vu1vCFxdwAUozo5ddi1IXJameIuv21eM5Rfan-k4RPYrJK9RShqj79SXDEsmsUXkro2LZXnK1br6wLctfg1upEvi2a5YL6QlPn-p1NVb00ZiZKVpDho3OhnVYS4R8W0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWjRwW99JfXDa-p_hzOx4786H0qlFfU52BC7QcUNJGf65A3d4cWRTvD5kr0XPFszV4BzQQm1QAK3XkupmdOa2tWqVQebFeqpJHjLvm3MWE2xAx4a3Unh_i1Yvmebozj3Ul1VL5CgwsQynkMDM2bv_7XlL67pQawI3yJjXdcMLmcGacnjPvxafJUzBFhlrozorIxyqvQP3ILM5ibgMiS_jEm7VVgvUoMDuT2nq4AxPTLPyVSZ1aPJ_Nleezn_QRK2THIopl5emogII59NLhDttmdJqIOY-P-HeRElO7GHzfr5wE_enQ3D559FMlEs56uv6qpZjNPquhDWs15mGMJo5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9rAqk8QImbrG4LMpZRrTYn9Tg6m9VxBTFzQfFSDCT2SN7fL1T2XtO0WeTnXQMU73zRittq3AqAyFWDaITzd9V6r806Tk60SZj3EeFMtLqnTCkZD7LeoWQRIE09Vgjg0cFoHv9vy6nNFpPurE49bv6bi_YiREO2vb4BUbHFZQcQOQ0wY8O_N4mhZax4cWkKMvRDMMeR6xKNRWwUKqJaHqivlNB1czfU2nfFQllrsxsARi7OR9yC5d1dQP0kfCv9K17riNyHWjAxGwnjYu4AHrBaeAw75Enil3N8bzy_HeWf03h5DNT6ORnuuiiBGxszVt8VviFW5iqUdQuL9daI-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEDFvtInPwnHZHnWzbVScXl56lzWagmsX6B4jPve7nR-JrMJiDxVvozFRM7ppi1qheFnLwAG_vx3NxSSB4AiGZ_hsYNA1PI5v3B5KqRQ9pu43AFFwRqRoItPGveSJrTM0jmEUGtXbVIZK-e2bW7rkcyzqcNmtJ2lcyCBkyPsEskniaUTaPKMKUO-BX2LaH4X9_1iwTxdNmqH7T-8oPs9c4Qg2VVc9A0hDQ2m92Ax2-XsqUypmr0qKsrNqeNebT0B5TIsQe0KQi1h3raKsww5dxUkamvKFqJjIgCdM9zzkOKUpoj2ylmRPPSfiBzDdb0lcXyPCjIs73fM1bKkftqhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmYeMOfX0cz9EpaTAVveN9Srfjcb2oNoG3QV2LhsBU5MIttrVAxeGnMXlD7QCkGTvHLtqJiu3N3Nyy4FTSvLtyycbzavmDGe43kbb4kPx9zWrmNbnJU4Md4I4XSzEjuipHPjJnxchbSO_dPa2evifuL1sX7FBX8nuTafpI3OnDzWb9abVMiF2GF1ZDkXfQiE42EANQNRFTJ3iSzGQf8CAa8_8PQPZ4S8H38oEj22m0J_RPgwNGWsohfoLEGDiIvrSDHDnPd6IVI2JIjvTMSWuG1iwJnRh8n5_2ZW6A8iehqJnCMHBLk1pm3pcOAiN-szKgSmkKCr2AyZ_i2tn8okmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxlAS1NotoxFZO9kjE3hql6MvfZQyaUrEUu89Nmc5oZz-266LsGk_TmWthm2SF9HdL2WOFfX7spvrRa7Yf58iFchkZueL5-HNYf2KEyuZ3UcJrqX0anW7GED_RKuAxq92wBVhW_3w3nPwy8BAa7_azFoR1gk_h7a8D3qQXofEb5MmYXUJZ3KtE417kYBaoeOC38bJ9sKQQUkWQGvQhG7Bq42WuOSkDSFvPpo4UF4DW1eawZLv93-QfA7BYzTeCaX-IlFRpMCHDI7g4x8IZFfEpBIYClJG5HSI-4TMMvDeFHJbWdD420RYWpA1DxGuBAlcMz0eDi2LS3rdaESfsAtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYFhrAoqKFXiIu7dZCdZOk4ytMzKdgYQcr71bVJoORZ6UW9IRM50spsJWdoby8QMY34uhgDaVL2EfGqyHA7eM4tzcxt9jb_7_8U5zInX7Kdvvgndd7SwiHNDwlDJ92W7d9lcwWCgztK8QUZfTFIcdNRh9oNW9ZhO8NLwgeDYb73Fn3MEUd7PLGxEgiqchDjBh8XnK1g4A3XQ2MhmYPrcviXwVMNhdTVp6k33j9hLOioN80X3eSDMfcMRCFfIkCG98i-qO0NhyF__jayoS_u1IE8_Eb37WIO4LsmNbK-uvhYNEeCBklMU0Ybk2BjKktkk1P9OySC25-h5P1dSuFOKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1VwdLC9maOXgiDn1NjmJUExdMSQqOhQv3nLPAH1xEq0jh2R2iAEqMqw36gWTM6kI4w5dzR-_i4DcJCrX5hVPi2MyCuKOPvvtd1a7jB9jdVxGRq8znznFR2DHf7XWCHdg5y_y-jjIYC2_HOtXzqnFro7InCho9sYtKwr-352a337BPpT0qwXzg2zGWlE1RD_M6prQaER3Z6XrNrhRmvRd7sSCiT5ghpXgI7qQB-vGf0snR3yMDqnrzV_5k1JvWR0eZRSGqbjx7GZNhQpP97Ll7HvjMqZNzTlfIuV2QMXbYPr-3gzX1pFO4-YIKp4-gBb5fCNngAHRay5K5_u8TfqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO35uAQeUNpOOKbyQTPO-pyouQ6Q6j3Z-BQaqEzww7vN9z0LnDV5N8aO-icv9TJLLbrHEcyaRwsh-0nsa2-XTkfkfjkri4LAkHO8wghcj9ubxjAKuBxrAKqaQvkp46h6jLHl3dXYoM4brLuiwICD2EDgAWHRwCMCZ5Zf5zrqvKDQysTfEhvzObM9zORVBW6OyP2gG9ZwJlXVluplmuCDu7-RouwM60QwIDQggss3jLcyPUya0IS03BXytKt7aob5d_ecO4Ty7b0RbsxL2lzH2WXcQkM3hzZcMW69m_h5aqMQ_cVTKqJctAUhJdAU5wG7cPyBVnBEPaREXybN_bgoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF9jSsh1No0chBCn_mlHsR7MmsqgcjwW1pkU9U0fc3PaPQfIFFU7oTvrIhRaRztSHEGtAhDa3FAc-FiLErHYr6r2J2hatqmRqjmCv6ptKCP9RaKC_uN6YL7W1jsj1sCbG8s2nRW790FhBjkjoGpfBCWrGZTxIOGuO3LNDWESqsPJZFUKAKnJ-VxdKgwMDV0StXo6SLQvuKJqPw_ZNmYsZJXzBVzb9Z5vo5W3NEjhAMTi-1iueEWwRllHJsk1uSN5-5-XNwyyFrQHZ4xz6B0lG3ytAkGr8_vs3bOJmIujvIShyORSEvfm6XW1O4iZiiRD6VDVJVWZfAKbZCMYpQUGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCTvftmg27ECdPMkfsXn06sX00m3Qpqlfw_gVEZCqrT1JRPDsmsudigDXIpaSbXGBF0listQCnOU3KEeRyyew9Pbfequc9dbGXyeVJvbxfav-fvmq8ZPyIKrc59649KU5sCQjaTSU3eWcY3ruHC14V59iK2xS_ZC9m4_IGRcU1OdLwwHTTbwEw6QabWO-uXmP3lnra-3Zph0_2uMTPxneC6CGJr7ko0t5G_ywtQaXKXSEwUqC5W9wZmT2OnpKDcJir99_2eemI3nOGKr_790Phcblx-oFlCo1PLDAvxOrCpsUIF8klRlQsFxU8C-yOpBPgiXOfrq-1JgRczN8NnzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu7wtTD9V8aoV8x3sqRfxmg5kczCXqxbx_ypVgogbZhS-YXafEEKIXksAjTASdGXMFHzBow9txeliG9T1Kd4hkA3dvrxjqJrdvSB19fdeCP17qtfaYs1sUeuJsQwcYXrtscxA6TBZtttIXdiums23uA8VhPSbtaXZR8BT-FuU33qCclwcdWVxb0ocQuuxJ1xOpMwTwdyfbnsQ9u8qP4NJ3HN_PjphQY-i0Yr1jO9ZO6WTxXHvpx7i-PNLEc1vdtfZIsUQAZ7Kq3CMRszoVvVfOwfHv-TrpVTTWUSlEsoMaO7l-tiRhsVE2lXH1ELkWqJjA8aucjJZr2LET36OwJr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=RKx4fmNlcGZ316JhCScCG9NnQB-Y8rS7WryPDLI2zS5OKkIpqfC-iVuYMEaCBf0ar_YrDk5a6fsweyP56ZpoWq45Tmmzns55Qa8qLsufEil6Ds_v-3wutkv1H-4166-4weYiQC0_qr3-nKdju7RREj0Kb3XmiS5Q9QF-7Trq9lnqGmUELWZr-7F5o8IgGRB92YWNLTsB3RLMdqxC7iFYlQ-tqQKGj4Mim6oWHGC0-kDU88WX2Hfj-SccAjaAyl-Fwb607hKlV1sRf_WiuPmjVt2x_RmQ_EWCTfC9eOgM3PgQpNfgbpleHgm6MpLEwP4Y3II_Ihwii82V0J7CnLWqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=RKx4fmNlcGZ316JhCScCG9NnQB-Y8rS7WryPDLI2zS5OKkIpqfC-iVuYMEaCBf0ar_YrDk5a6fsweyP56ZpoWq45Tmmzns55Qa8qLsufEil6Ds_v-3wutkv1H-4166-4weYiQC0_qr3-nKdju7RREj0Kb3XmiS5Q9QF-7Trq9lnqGmUELWZr-7F5o8IgGRB92YWNLTsB3RLMdqxC7iFYlQ-tqQKGj4Mim6oWHGC0-kDU88WX2Hfj-SccAjaAyl-Fwb607hKlV1sRf_WiuPmjVt2x_RmQ_EWCTfC9eOgM3PgQpNfgbpleHgm6MpLEwP4Y3II_Ihwii82V0J7CnLWqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvTcmX-4WlG8cFXLcm8l_eUbcIJ92MbLsHr66ko667hZJyInOIiHkYbg6GfnrrhaD1JdbdBq5ua4XOBYolb3KXscQoE_VSnHlE9GmW-4jNfKKkhj8wXlnCZd_xmtv8RHJ-EODsLxXhAYZp4EDb75fog2Oe4CTjvyR2zYrSBc9zs-c1xj09eNNRNgH_wD1Zfs-GCk9OlttPb5WbxuD_L85kUdgQdPGZ04NaHmNNMLaxY9whbnpk3jOUY84HlmvNNoUvoZ1YPk3YldcgJavEywyBXdgXkLQMWfV8uN_XYjMMH5xfvWZBfbCPIeFNAKdvojW7aI5ybTc60ZYhmeHcKh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWshepm97zUhdg6E3FFW6ARAjj5vgmSt9FygGbKYRXwfGrL5QAb8JVUpmv90w8tqgMNNUSrR7Xq6sILwr0NLKD4VLuMCbNE3E8Kd-H2nASDKSunDC1a57fD4bg2V2dZquMgw7nYc0Zud5MvXtMP62vHuA5VJn3Dol6juCBoARn7JmvB57PCnfszxjKciXyZe9g6IKFpcxOjrL1Vzh14-ogqfhobxRgPeHCA8mS-5WB-81qg9VHWWITrQejRIpETWEE_w52x95f83OQPWUu8bH1dVJFdsvZJlw81dfXPaBxmX1hqlfdQ5DrZ6pgpmyQbYAGIFFslNfuiO5BapFYgI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Eb8RSK8bEdHMLnSQDV_F4O_VlwpxKf4dcBRNu-fNmfbJLt-UkmUNLyyW3dElRiizB41YVthZSYVqgol8eTBr8f_qp-YsLEgUcfTReWz4oJlhDWoMFXk3_mnlJ7ZX-mLh4BpJZ_T5S_EYWu5N_IW577Gi_u2Koh_S2xOAVUedS6XY_9_fUi3kt4PRoq6Wx0u8y_4ZEaB0kVVF5b0sjkWfy28htxrGrf2Z6rUGInfpdJScvTrsTxcfIzqfa6CPe2c-sutM_BdrXNwayao3xL7F5Dy3hgR4VCQFjNKJimTRmrp22twUNlz8KQoXDToqSfYUpVDjlVXnj2efmUZtvYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNPixLOBZ971FN1EQGgQnW7MheUzVOyC2B_JIynRDDrBnEHAw7wOagD8K7TwSeyqO4t6rSzht_udBDWMpWTh5xFG_TLYXgZCVU7JRngFQV99Besod3lmM--Y4W0gLGBe2oAR7qts9pN0Odfp-7CykFUguI48BlKhkMuSv-JK6RXGzly316QkV3rsnXG-eZhXYNpNI9AMKGkzryK1Gxwe7GT1ek-iHfCvCvwOlt0WEfgDK0jHGa2wMntv0LWzXT0ryT6aksd0GumwH_VtPw_cHdXg7ooelW5Y1xGWX690krp5QI0XDAWqQykROqO89hZs42bIOlQLIEk-RhtBOxnNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD-5GbnY_TspbMlUfsvZ5SMSCj-YT7sMZvJn36YI-E6qug0_DbFIi0vgMD8HtGmJU_Ucx1o_x-0QCLvmPcPPzPg6De6L3nxhCpmLA7e6zsQ1PvRYV8TMbX8U327cBroUwkEvboMhMmWqQ9UJNiV8aQK9araYH4rwnEFviV-vdBUCzg0Aw_2dCiAZfKe9g2EStx9-Dt4YMBE3M1XWcZkPaeRfyRnrI_NxVqjdJaxh-3e0GwswWFnUxjFlV1vxw3FqdjLOtDfKjcX5oh5s2h9Mv3hIFRyiMkiZZSBRAztCAmyok-F5rdeU0KIrg-LYEv4sdBfgRF6DDqeYYIgFsOVE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAb9xtj2sKspB5KyvIufLyh_VtmaL0BAi29CNqYa0MYOkDU5bEO0NIJ7rMbjcL5H3GlaOmdO4rRhB6OJ_NDi5920wdlmUgF1ThkmKqeHrNo9FrqB2aaDp5t4ryDoKXKRfp7DjQarEBNjIu53Vhb-rX13XwFsvBkKIbZW89jDCJKuEOIa0ZwMOxkTfMr4pqWjBk8RhzuK_apGF8VBXJQMzCx-xfjYR2fGRbQpnH-IIt9itME37oSlxnczBt53xUoaxZn9mn_3r8aLpiQKvFe2cv4qMR7MNHtV2xxMXAZqkg5VrlgGHPnby3edagfdPEy-CWl_cv1V1mHffyHQvo4rRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWMYXEA6cxj4K9PPovZGGXBot2BtMAyOeT-bRCsa2oM01Ou5JliA9YVuIvTWpESk3hU-blmm4pnsh0uJXGU8Md0WyCtEHSOseqwvIgJZpFNGvU_liEM5z8WzmXVEPNpbg2eVyzN8ziJtY8AKEU1kv7_Ffm8GJjYuSi-tIh1tSifDwGCW4qySP14Eih0mLCvO15rYoVfc162ozKRpFFasOPmGnP5ow0vCp2eRlPFs4qmrglHU9GiW7_s6qmnb7iOJed9HwgeArdeTr0ihjh0LQv-tf06LftNQ4WWDjM9WW2NQjA0gQzz1tRLAQbqoSsGpYmPBYHL4EdAqKwxncoanmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX8KAqxS_48WFSVGQq1jNCaSbeMgfS-ygwoxrq_qcj5Br-dZ-9VfKKTXP2-DEsc8eJLvNf_6Kp1CVMKhUFF_yFLa-13-bzZVgACZYjSkIBPakG1xs9zoBbTB31Xp7ZKtVxqnNOJoDP4XO3263scnllFPSnBmpgR5ftFCcVvJvKCk8dUBT1Ns74U6D1dhPKA_34QbjmxZ4ek6xtyTYZX0NoT3nzYFE-D5etr3sfTNOItsKtrx3AYXCBKhMxP0NFNJLVl8npKnbrLsL04twAI1Q0G1YnQGQ8UbuX0o0rCC0vLbPuJhhHYWdY10LR4ZFNTg925CR2YCWrRU8ld-ySA8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IndEr3pguyYRS1rXQeg799bVRkfpxHkRD3tfclBwBTtCwV0RsPx5k4yxAieyUrjK7q0PjfKVT1vghw6zw6nDE1wVUqW-coKXgw6lUQkd86aCCSWM1DDztqiy2arZ5YzlwxjlbmYhSOoizMXLrO1FMpBoszGknEfoSqAdlimg-34FQTPJ6i5aTY0pQvGKVq528fp4gfc8o0FehEWRKt1Yc0zUBU5oeQsQrdHmxeKLWj0VV6EYoX6T0njggUo_-KEpyiu-OCbyNo575iN_3U4aPiN2sbI_rFmyRxIReRnPJ9kha2Ijk9L6ct8fk9UWlMldZtwkSdrCMh0_3YRcG1wyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ5J4X95UlecnTJJq_9SvLZF7xPXvzvKoftdQX_nn9HB2gDxzAa7VMADtazUAE7_eXOcdBO1ZNGuXWl1ay846Se2ZY11v-VVr19GFgN_x3FAFnUC5m3c1PAPHJ8lOqeBndl0MZ1vL7peWi3G6DAo4jerkfWoIL-ea2P-0Y0sV76-l-6vJhAXKD2e_dJ6fKhoRQy36OkIW1HMuAdCt3ggNmmRWw5sh_U-QNjvlFaEMzRngPr79sWzqRw01-1fQed5vF9AXzbfNJHyxmKCqMtGJCAI9k8e6DHI5ByF8B4b62yzwo_5wszsfru0Ewp7Gv9BZwUHmcv9sI3kICEYGD0lFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swaCnZ5RTlvE0FaU1JAWBxk8xtZJGn9S8_vrgyFilkN9gYFlMxgTUx9DwfYq2BTccnq0GzhZvFa1CCaIU5x8NK3dJg1YUtQ2Ca5zSQ4DsDHYNxIUJ1U1oQs_N5CltXld2SNDcKsyiqHa0xPcm5oAnVG3diGz9OElCiZ84HIVfgGeGQpfG7BHDt61JC5qD7tZBvICT5GlAc2-BXHIVAbQRGdWPJXsm1f5cZz87ZjoI9ds-P6U-3a3sb66xpE87LjQ65mqX48WGhKMmC4VSyPN0H4IUZJO8pt5v9ak8-WI8dNtnIJzD4NPW7NXqwEedwl5gkfFQF3D_H1pcv_6b48qrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvSGjoA6zBBhrq_0pWeEmjE7X7B_ktmXyjUuChv4a-O7OefecelVQgC1PD6jWXNVQnp9nBISTFI3eFb6E7CKXxYrZGsdR66GIOKhqVqKyEzxo6MSgTBH6_iqYG8vH2auUt8oix3UxFRjWfqGDjZHKUSftgsI34osZAfVj_a3HkbkZQHRHzqE_nqg6b-bOQZIsgjfkllS_vsJeYyfyMHjsosiPTSkmILEnTcaVRa1HvT5GmxErogPEfk2C5Oz_1DucLm7CBl0v1gNVQQjmrLTPPWJTtzeOxc5_h7T0ttEjt5_BcCgmvU8yPN62HFB0m6bRMa25a6R4T-HJlngQ7KfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=dYOW-LtXh1qIw9jzVilr6WVcZYyq_BSXTAj33hyDbSByKevkGTAOT38815Ol3rY41zFKc8YETBwyGs8LrrIeRYD8huGYIrRGVhRWiyChL1rRJrBOsK_sFw3IHdIXJtkTZmsxuIr_8JL5kxWEIv57Ta69sY9OxrdxaLdDxLFlTvyRYK_a6sX-WEk6LMGnnaKcwbWUXdZirrUWntnQTbg5kSBSzFoUrYfKolSi-ahWku44-wqMGE-Noo161B8kxq09xH7A8RQFQwAUH9_u3PRt1e0n6wM4fHcw9xSbFk1Mp27mqeJkDifSkcFbbD5m5YWKF5pj39AUt98C7c6Utz3x5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=dYOW-LtXh1qIw9jzVilr6WVcZYyq_BSXTAj33hyDbSByKevkGTAOT38815Ol3rY41zFKc8YETBwyGs8LrrIeRYD8huGYIrRGVhRWiyChL1rRJrBOsK_sFw3IHdIXJtkTZmsxuIr_8JL5kxWEIv57Ta69sY9OxrdxaLdDxLFlTvyRYK_a6sX-WEk6LMGnnaKcwbWUXdZirrUWntnQTbg5kSBSzFoUrYfKolSi-ahWku44-wqMGE-Noo161B8kxq09xH7A8RQFQwAUH9_u3PRt1e0n6wM4fHcw9xSbFk1Mp27mqeJkDifSkcFbbD5m5YWKF5pj39AUt98C7c6Utz3x5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=gm7qMazpiMO28qPMR4gXDTNfvmNsBFSx-s6zLxTYjyAQdiV4LTRVXKZeYcDAAgWimRI3RQr-Ycbwz3InMlPI3ixnQC_5zoin71i3zsjjNUq3EBzdYxv0zkvpA0MO27wo6NYKnQeog6feoW_VjRgG2AM5EPhAztnuLQFYjVroxcmMQPTL506m6jyQbP2rNjbYp6I_-JaBM0AtdLIvyz7mmPnNheAg6VgTPlY4INotfJ8NC9qvUTdSeXMM3RDc-KKgjzyekdHOSJew79uN0zPVxI3SnG9RyBWm7EQp9XF6D11xvzh_JOb45fwpG4Fw1UJbpIAwPtSZPr_4jhRDNgG9QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=gm7qMazpiMO28qPMR4gXDTNfvmNsBFSx-s6zLxTYjyAQdiV4LTRVXKZeYcDAAgWimRI3RQr-Ycbwz3InMlPI3ixnQC_5zoin71i3zsjjNUq3EBzdYxv0zkvpA0MO27wo6NYKnQeog6feoW_VjRgG2AM5EPhAztnuLQFYjVroxcmMQPTL506m6jyQbP2rNjbYp6I_-JaBM0AtdLIvyz7mmPnNheAg6VgTPlY4INotfJ8NC9qvUTdSeXMM3RDc-KKgjzyekdHOSJew79uN0zPVxI3SnG9RyBWm7EQp9XF6D11xvzh_JOb45fwpG4Fw1UJbpIAwPtSZPr_4jhRDNgG9QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2k6IPTvEv7kche3W3R5L2rpBUcWqabCbXCo8rXKr-1T5FirzRXzFF42E-UgwGmfvA9EH0Sw1MbwhiUB9r0yK1wXhCkoDjAmXYXuQKayvRv5SSqI2vMsNZg_i5qAx-2aAuXkcHhkGT7s8DuSL7NHdk-HbBNywQnmsmzVWxXWsjpeNnALXUSzw3IqDIy9CKHk9KRyy1i9DTOKrrYU4q-gNxRnd1-IwVzquEDtUrccn8B3NDoGpLU5kcmdMGBClOXQy3IRlI6yKHbOaPb7vtNl1oEIQIIhn9MBrH6IZ4U0P0dtI8kvxIKiW6BL5xMkk0oE-i7NE8ZofHJfojsIS5g3dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaU1-BMgkCJ2TF31lfK9kACgl2HIYyJ8UIV1VmL5Z8nqe1vZnAxLYychg8WRrbbGuhY-j797jZmMsVPxCWbOgTjkIDxge2VDqHPlgmlISUbwNxfYniCkWfz4YUGWxZYt8QHaSqMSMc5ztRJE3sE67H8U02mq3p-zF-zcQj737fVTnqHfLZFT-yORlnJGbU_GGpoBsfFZ9rnecNLqtOkL6YS7FwFXM86_5Iwh02SZ5U8qv_ag_wq90Zd8jdstF4_v2oxy09Z4xT-5VqP4-TCuYmu9IqqFQQKVH4fu7nzUEW_Nn9iuqDs5L7M63KrlQ2Dkb_MCrHah5Yc4NkrL4vhqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeYLDP9_dVdQSvp0M9AFxLFJ_toe5JzvIaKdRpxSg-jwc752mBFlmbzQieIoxxeD0eQ5CHxtZyalO1dGuZtRLx2103pvpGEOW2eKDz2FdmOFhhkMxnvFVkCGxoBxQl-EYPmj1NpXg3Cpf61rTESUE9w8YPdjQFiLpyOc38_K9xK8rpnbglb7OgMKrYUkfYD-VEIe3grRWF_xNX4o8ssmmiZLOL0pjo8GkCAJl8zSTQ_49JwyV7rn3t7iy4llMUiVA_6PCQkWycy5Pbydt0uADCY6Q-xaqIW_v-uhoQjvI52NlE_dBeVesXKr2kFZu_9v9IzVKN4u6GuVp6U9q6FJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRXoOBY3M5AZZNpe_YHRdD38nRZOi8v-B0fpC_E_2K2MOWandlKR-4vy9a4coBlvSxw81OqVHmBDtKwTx61K5eNhHoimp55g1lWoIOwWa-GtslbcWcSfH0fFds8UgxVJJtTZ16x_DSVg_a26OPTp_9_dyLR5rFzzu78N-kuKC9rGy9jm-cWkZpijlLXiSdASk0N2yWYHdbE5z2QdFOX0UefgGzMmbhNOdGkNWTjbf-uQRTS5OHecnPL7qN8HA-IeQX-RmI5bDzfT7L7BsjBuURC1Aa2QSkgGs1K8bCmHQK3ncM9lI2u3Kpl-UMR5l1nsV7F4hdn6NJpw1-7PLZwnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug3bmwKoRXQACjCpxr5AGVpCSzI9gHGdD6WZU5KGzrkDZ9ISf7nnlD_Q1E2R48y5RCdjFPQWBU246avZgdUCVD4rMD5mM0Nnq3j9Fc14CakjBkKEZgLFzG3DqRVsGsGjdD1gOFlIlbzMw4W78L5wUycvAZsZmXnhkkWD1CYqogUQBoAi1r3rzXsynhHMGqQ0iZbTBRtfq_OU7sEbMVL9ee_QsfBHWu5iuoYq-J9XMmmhu4tMGUyKwcAuHu6eujebSJjHTpiTp20IIrtusbPsrIkTJBkegWziomfavQepd-NVBc88zHx5PBI8x5-lmOL28kllFqFbznA9GgD7PUfF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5rYVUZ25IiC5Csw1Vtl45fpd-apMNF7tCIBcQSHe1vBH5PaMLA438vX4rIYkZ5cJWv1ZpUR4RsZP3tvTxRJ0w_ZlRh5jYl-yta85hm5VewmebCUHa9cc0h0RKminr243JNr_YtVHyHA7SCLIBj8_wKVYl48Nsr_ieIoRG0BBrd0OI8QZBkuwPpBv-adeOzP2DedLnmgWdng4wZDJNfs400esWwYRu5Tf6Tkfq1vycSP0vSa4LplMhYWAwpfxrONuFUsG9NUVdrhOZUPILomd_gpQFJY2RvQpIgydZ9z8w9juqB3JYxVGikKYqzi1OknOOgUqWtmD31QwXPPq4JMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpgyZgXeY8A_RyVQCwPxF-QVVsuWexf6tSRQ3-dsYnK7cZ8ti8rejqPTVARizxnb66auVqFm8MFjxqYKNWXXdQIdQwZcqeXQ3v4A8zbPlrYjLzU0I210mrY7uJYVK7Aj23gjS8e-NVE8wKQoUBe5dSvyGOq9dvBquLQmxHEcD04icQQb2DkMIt8K3JDsKJBW5A6GN9KrnkF-5ULfPl8sFDW4K7sr9DJe_aJf19K2Up9EZ1G6LP6SmVoczxLgQuzyO7pmwfnXA1hiJLvCHXtlkivEvd0yUu48wKAMmFl49XNSNqKAhegl-thoHiq7CBFINb8KcYUVkoSKM1aSuACfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voxU-fUmX2XflCOhwIlCs6eQkLkmPbIl7_5Q_La_cvF1phjZS7Vycgq_Wv5VUzDQPYB7cZohg9KrN2z5GcAryvd69mhn_P4OJMF7B1dpMjM5nT9Rxd1JcorDM-mr6mE0sbvoUVDo-F6hMmKPPetA7TX_ILJPMz9gnqaVNZ4ycOIT8LIzV7Nc9HRSeZV3YL37VxSMcEHibBwBlvmJ73rCn4iSTDwdIebpLcX3AngqW8gMbvYZPrb_CpUSnwDYu1Wxlp_uuSLuCRThqtdxMgrcwP_4tGAhlAmKcgnT95rWhhXUf2IvtzihSyCxxQpssyRAa8l7b4OC3rbpWyyjcfCTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBfm5X7SpAyxVtYEwCUqZ4F3xJ3TvxsnHGPvhGDiL9OqreNKgBqDhgmhgxx7Vlmj8ahUZ2YzIvBpQPezFdN-uLfNuK4AnZatU9O5nTgEJCBqVvaqvfyITKiE8Vp-GqdusVr1kIpcXKVDqM7RZl37pH3yKbPjMmDy7RficrAJUQuYeln7IHY8WtUGneoqIIhvJ2R7dbtzP5mkRg7g7Gh0hSgYqjnEuS0C2a-tsNqr2FAUOiAOIihaHvqDWz-ip5-iwl5818VTsypPpw9E-blJr6xnSV36uPYNNLjbqYFWQct0Z38iPb-HuEWg56KZ1p3jbmumCsqJT8yaItSlgFeeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP5NvPsSU6G5DNlHLJnbg-vkK_gu7RzAdSuxlS39utIX1vgzOXBFG86WMiQlMi8434nSLmWsvKIjmcQbaHAoBv6oP0Z8rreLyu4fAKG1f4PjHku6jhXsyFoSk3-frWs4Xu0MH9155XNx-AH9AFCzAcWgq3y7TYWVTQMkVt-prm4_z8tkhFhs5PfZeVFUj4imHM6VK12jrlLjKdEzOPbqjSYnVuTMSYJDRMrx8fEbi2XBT9Q2SYwes6y32_ITWC2QFLfgx-d6tlqh5jS74e53EVwhybpUZqG5rJsoAWozQfVVKjkd2UTf-6okAdQGm8-Sb5vG17X051q_s9RywqicEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=R9MXzQSWlEMMPCHdagAT00QRnTiSflyGsoYgWzgkqx0YbC7xzGJPkX6BHmNoh8jreK9fcLNDr4WZy2WFbPEytS72JisqnjetNqKOleFobLW8MB6IPs_MfHQD9RtiRyLEVL6eU1BmP_PQZJmsFUsBjPF30u76Mx-bzSrrmhdu-BUYzjDxb6BA2I8LbLraXkYMOmXMK8qvKQAlZ5pnRFcUvEOTQIgvFS1GRYlmEksMp0Hs9J2IgXER21jGoLT-eD6lE4YZAo2MGTk0Z7cmZm9lNymj6eEf_gIXCoc4QFSp036gx6BW0KEZA_Fsgak6g537G98CB5lCysyRRSm2q8sZnWIXoXf1SQrnXNwUgeFP3Eie_KBsp0CV08QvNhp2KL3wDYsQUqecfToylKTkmuP2-rdSYcpryczY_pXxUjAsENvMs8b3sxtW6cEebIMDY3KQyBLtiBSRiWtZstxVqXENdKA2K-86XcvNbsY9Ssrd1W4uJCrwtTf5N4tujf-wH95ZdEcmOmysH2gGgUeK2pQB5z0_sTYD-I8WT7vWRntWPscfrsWweYyHfKEdLFfkaYlADOXk6Ob_I34WAp-zejGc1ebs35wmMiBIBk9O3pbVWdgfMwem3PYGRu3zrDb72PCQaI4UoEFYK-s0O2F_I88N7OW1xZ_tXxM7p_xtHxlIDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=R9MXzQSWlEMMPCHdagAT00QRnTiSflyGsoYgWzgkqx0YbC7xzGJPkX6BHmNoh8jreK9fcLNDr4WZy2WFbPEytS72JisqnjetNqKOleFobLW8MB6IPs_MfHQD9RtiRyLEVL6eU1BmP_PQZJmsFUsBjPF30u76Mx-bzSrrmhdu-BUYzjDxb6BA2I8LbLraXkYMOmXMK8qvKQAlZ5pnRFcUvEOTQIgvFS1GRYlmEksMp0Hs9J2IgXER21jGoLT-eD6lE4YZAo2MGTk0Z7cmZm9lNymj6eEf_gIXCoc4QFSp036gx6BW0KEZA_Fsgak6g537G98CB5lCysyRRSm2q8sZnWIXoXf1SQrnXNwUgeFP3Eie_KBsp0CV08QvNhp2KL3wDYsQUqecfToylKTkmuP2-rdSYcpryczY_pXxUjAsENvMs8b3sxtW6cEebIMDY3KQyBLtiBSRiWtZstxVqXENdKA2K-86XcvNbsY9Ssrd1W4uJCrwtTf5N4tujf-wH95ZdEcmOmysH2gGgUeK2pQB5z0_sTYD-I8WT7vWRntWPscfrsWweYyHfKEdLFfkaYlADOXk6Ob_I34WAp-zejGc1ebs35wmMiBIBk9O3pbVWdgfMwem3PYGRu3zrDb72PCQaI4UoEFYK-s0O2F_I88N7OW1xZ_tXxM7p_xtHxlIDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfTaHWlRGr3zwrvnTPPYmIN120rAFVXtDRFZjwLKbAN7ZbQldyzvHsbOhPn1OJ1ud1y1nelrgfA4aP2LnLDazGIoQCQrhC2JyIqw5NwlWU-NZGCjviM8ykNnQXZcnYvTNGsGlQfhg5lE1qN3IqM9VfaHDiCVeopkPiLzQxU_sgS4ghxG0VeOQYjG1gnf750kFA8QTR9BkKYTOMG6akNAfwsvrjHxb4HNYAgIDXfO686oUcX1nxGWYTXSSnWWrr5hZug6QMaJ1sIMHxfu9ko2Om6zxjColJJ5byqKqtBrQ2uIFC0YOTuRphFqQI93r6xGBUfs061ihfCQQea4eGBHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjEpGFIctrWQOWUK53Ahvd7KTE5y1s4oS0P0JuCuqFfY2VoUlAszWe4kuMBYtB6Utl-98gP-J9jMjlJtsDiJrEkcn-AriJJ-FNjqFAVw6Iv-1E_hAO-D1DTSicr-YY0yTzgWsEzWH3CVP6htkgZrbTTWuOEIWmDVMQUGqa6n79V6YBQmn-080HttGH8mSrnHZ-fWN0YfeV2AfwqzlJtw0fX2siXim9AZEtQWcFc9cI9AVKZqyW1MS5u_8dut2_6g0-1Po-pmCusqOAa32GFXCkIB-EfOTAnEjtZPWN6LhTQiSvNlQb-TM12ey4To75P84TLam07oVYDAbjVaMXnWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryGfYoZv1LZbZjSkfpw8jNHWRouWX7OkeCvn2kzYhv6zxqoOr_N0PkpxSAxp5pb-FQe7w92bBMtXB3M6Y-K3k-qa3qnXZ6FwY0Seb64DoyN9zm_H4_X6PwWA0ZuExdHjJib-i5JrifKB6eI9v92u9iKtrLbrEM6O_yI3Z957gyevBDMwVMTBA5qRyl6t4noTCEMNo4sOxnRf9BTFj0H_lKSIxpZ68OIKi1tqP1uRuxGzsA5KtJhxmVtE9KTQYSlQ-fiQFldjhyvNfisZQBFY9CvGwrbleXTXPIWxji3mE_WuNexEMAAx5wFbqRQjRZcLE57a1nNFpMk0PuvEp0FMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=a4usFTKQp1HmclCbpwRI_WjC5os0JNnZ7G4ddDbrt8LHzrtuILMxFhkWW3cpr-gJW1JULci_Buv6jO0CKvgvtzCPtuLki5FTIbEzmPt8PmT3kzX_NeP5OdjUBkApomcQSNc134Ctdx-LVzW47t8HtUS3syQO5vnHZVWesFN3ydVAcl1rbVFDeHWt7BhuGrLlqk0vKFF99vIciPYUzBBuqyCIIy65nKDpnS2g6vusiBfrUFu53GTEE_XUoAhxdXpddfTTq9V4-6GcFAcfndXHYPUVSzyA6po1p3RCh46hLbIhRvuq47GDu_EYl8YkkzispsLs_lgvETTVyi5xQISrqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=a4usFTKQp1HmclCbpwRI_WjC5os0JNnZ7G4ddDbrt8LHzrtuILMxFhkWW3cpr-gJW1JULci_Buv6jO0CKvgvtzCPtuLki5FTIbEzmPt8PmT3kzX_NeP5OdjUBkApomcQSNc134Ctdx-LVzW47t8HtUS3syQO5vnHZVWesFN3ydVAcl1rbVFDeHWt7BhuGrLlqk0vKFF99vIciPYUzBBuqyCIIy65nKDpnS2g6vusiBfrUFu53GTEE_XUoAhxdXpddfTTq9V4-6GcFAcfndXHYPUVSzyA6po1p3RCh46hLbIhRvuq47GDu_EYl8YkkzispsLs_lgvETTVyi5xQISrqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyGJ49x3gKuN1yHYBw076eKzjN_4DP_X7n6cjto7zDx7lIJ_oVptPIbrLBO6cUDnbbsM9lWoYBGStRzC0CIg0YJvOD3cMc3pokCSo6lCEaLrWYW9gVZg_RfEvkSHTEwpzU4VZ8sUoypBkdWjIV9RexEOy2MmH7TNVpo9iu8ZhP-nWgWOlHRyAMfZHpIDU86ovLccCEJpCNK1ZRG6N5HL6DNs7dDj0KRHGDD0wQHPRwrpCttkua-rQ6a3OHLNIfN3y6XXPSY9jAyHpycVgH6DtmNrR03yDmZr34UQVFtmPENQRI0aRp01Bt7MeUgJnOtpSWi_A150z1ntzP2AMWYmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjvadI7g1M5G7zvrSDv_-rr_4CvBwASrwpq9udFli8o1LeKyYrw08MP7wW0tUh_a8l0Y_PNx7D2TO1HftWMEaiXXMDa8eBnGIXZycTNWK_eE39d3wqKU2bvMCt34u2_T2f0j_K7STnMdw15pDkVXvhjA9ZksFYrsWp0YZsLDHrIqFB-JzlDYDfyaFKGvV5QW4-eDAdsPradzmK2cEic-IOmm9OMVKx3Ek6ciJ9vtuCe8dGWFTevVvY1RdL2EpQ422uDDCaftv00PekVdWxkcNeBSLfwQtC1MaOhIgT8dQKXtAxcNivOa7Mfu1ExawQfYusmJThXUSkVR-5GMPo0e-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ4tfRvmEEfeKDyeCQcM50p-hU-B8f0USrAjXxnIiEpUsN6vc1gO6fQKb0ATkeGtQQFYhd-3O66CPNHNm36xvplfqD23A8nrmCkZ9rrSMQiKn8_fmLDoRM7Qk7g3DC-mPDSoySg8FJYLsCx0hdQbVixg7DX1g97dduWtHw_pcHgiSC6fAfWJ2lp5gGgaNsedA97wSAmwrde1GdPC0shnxKyNULz7d5Lx0ZYOMZWaA-esSF7KgIPO6hmoKqPjcmLQgVHlJzn8VpY1gFR4zwCmVL-VZwG2brLWZ8aY8Gcws7dcb6e0t7PdSAVFC2Y9m5oZhfobwtreKZ55Zdubbkb1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uefN1ltAAkFOBnWt6nQVy9neEgbB9OXwL7g6qikJg2IO7HctX1phSARBH6UZ2MQY5lO8sD_OypicbiX9Uh6hheOEmrR55thL3pEwr3rvIjdlNNeRcVTlfJMfoxZjwZuWWqLuNcJtQ5oitQ-9A9AniD5uwtrLvKreDXAogPce_sBfh6dd7DIhCu8OOnVUMlZQEdhqrB3pEN-T3wY8mD6kLFni4buGIdx6KBw1Y5Is6ydPCtrIZl8gfJ__B3PpCCif7HJOQLE-0_g8qjAeAy3SRQZu31YecpSSNHereHtFfJh2_naerwe9chDVuTWyGNaZyDZthzUpLkRgofwd4K0-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8H8p_iDxJuCJsh2VZYf6UpLZID5ndCwZICSrv-RBsrIV7dAtvymoHsVxq0iE4YwUFEE-Sm2oyHjQab77O8i99FEaV6F6uRZpIlzoGzSJmRFNvmufN73DrAzJ6dVFwKTjeqZqmjIR4ajyyb7ymc99JqMNCH__rCCRYhfDGMExLbjv0hk2GeY2VqvnJB4InOhk1obmBU8BOpZ1HKDxwP8b-ukXlkRBz4gveBbnY0DUGLlTbckApZRMhMMOv2-jUnZohl2zTqPKlwrVUgZjQ3hrGS6ufE6oTvGkDaNz7mo7RTrMILO5hT6aoohHo05_irNH759xsxfTArJk3h47Y9jQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmRjKlmqoclGtSphfzkR4rwCm2SiZ02QVYA3jmz-ybVVN1uSuePLXRsMo7Sk8nAg-nxMA4b1pk0s4qkItbzqF8d_1P5tYR9BqfITRx-e2oywr7NB6-u949stloP6WdvAOXXxNEMEfxgnk8AhTLb7IrWgQBe-JwtWcSNJK4zkyNYoIFeE75QRW_ElCIkxqqPVSWRtgexJyX7GRhlT_hOxhIC718etLRoVrIqaYmpu7ZbJfkoZFnM_AtSz3qg6emDpNULRkfrG_Vi6dlfeYN4hmKUEmpMt5ffGekozDYalK95MIFQXR9ogSaPuNqcNRXZfTkn6j66RGPG5Pu8mBswMLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgeG2zQX-HejiMFXV2nppAWLY31fax0OacxxYK4Agl0tUvgXwQNWKCVF4iSqwL4LDEZMYce1lKAN4m1U-_SxMm-B_ZloReja5mY7-tMGsCHbS5RRYiswchqQ9K5MRxKYAIgTrwalrPBqVD0Ty_1OeBQ5576yJkjy4ZUwFmoKpxo9Up0Cfti3VvNeq9xCeWvTRqmmL_GAXrDLh_OxpfezgnLcLpm2Bk957VclOX7VTaf4lP3I4jl8DciQ-HywD_TV2jTF4L5ZY_HFmdf79jZpnMU-gCloJ2MvFRNxt63Q_yYvAeITBNqy7bIg25qtb4_7Dm5w1Y4swhC-DecZeEUDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNvGoxmgD4i17VY4xcSt64FzZ9lTWuagbdgr7_ugNaEHBstx7sh5qO23rGJtfd33aznBWzAHHpGj3vsvq3M1nTjrOoRWWI-oSqkDbl_sz_w2H0VsUjL1YPJCy5rBYIz4QmVlB-MVUJoDLhQGFPDXh11yx73LLxLBScpUQvxGH_QvLidu3iFMY4voI28XsuJiKBpbiupcEXOeTBTsnNUYaKbSPfuK0bvai9HXWrl2EP8t9OmlaYsjhpdyMstAf4KXV_uvXGOyWrlKNflZyErkApQx4hn5hev8vOlkpHxW8bmYsU0OvbSyIpGYJ8xrYlhoTMNy4gL76QAytF_MDbM3mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3cM9J26805dgAgXZ8G3EeY-mrVKJrdXDmogMC7f1xTjanm22PcUsfla3ALrqhBMKAM_eBYA1AT7UaQFvaxve9FHyHYGzzzWNK1HRSWPKgXByry9AB5McPBcoDFet7HKQlj9AfUojkfW2I9iQXlWRNV1SseF2OUP6-lVD8pT_QpBpdS4Is0LZGNFveUAYj8XwMX8lVxMwDIdRnxA3eAZUG7eU1KWYOmlZw0lf12PVdImyxbKIshDV0irJHQRyT_3lpQTGvX7zUmn9u-eeXjHTUHnZqeZGCePevaCe0oL9uh5Ria2sYO350vbxtbT2c0NktKFHH8io6F0WZBjV5JwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYIfqnJKYCHxl4eEsu8gJdZK8uqVw0Yfo3MPNkL_BXLiE8spe1CEQAkSfA_mWVF_i8HBuGAzCPwoYIMNyjq1D1kGE3fZzeoYpp4Q9v9JO1Tmr3uwxEMbtstHszOp67S4oIK2Mu3lemtpspxvi-3DN90gRFSf4bvBqMVaSAa5MOv9pQZU2ERFIMvRuZycbyZ-u0dxqKvwM83AZ10pK-_NQ1l8Mn4J0XRivyEHizmjG8KcOJCbKxX_bRxtPMG2Nu-fe7YeZm9WQGmi_Yxv84_P3Fw0nmJqAzRsdMtT2wTbP59vSgN2dFSNCzt2YLk20ddjGZf5VDV3UBhD5u6VK4x_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHigYcNUbYkAjRH6LX0G9CUS-pGkLCErFG28j4e37tDWZeE3S3V9zXV-rGwNO59ytnt26cSP0l5cZNW62tQ-J5U1EHw1TMmcy-6guama3G0INC5sQzqFQYcUnGuGxvGngW-7CSjVu41sv8Thiyz1ByUWknZa0MTTgsQUdxg4e0o8x-I0_DnxoDdPpLJhfbmaZLAnddlG247F9iLp8pMT6qRYTE4S4RcoovgxGZqpJLSmWiHUlgkntEsMZpKtU6MyN1sw2LO6928NWuRm9FLwVwarp68O2B8N6YbTuDBMF_20dWA4T8WRFYizc50BpNR2qC7ZLwv-ENiwtwU3CiWYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDpgFITrx4eOik-913iUtZyVnZAv8ONhIX7V9G7vpcH7AERjGOsXIm_YoipkrhX4WTidUrJ_EnWd0gCvBXDhS3lNTgaH0ncHCoqBjNX4hK4KX7p4KKdSE5cJQO2TTHoFZ0IYnRlGzE5-SL71qnzYDvc0A3pwB-i2L5Hw5QpCdQcskM8fuec1AyezZzec9hsiW5jgV2PMheGRtXHVu6h1U3JYwvLM58g6mp3Hv9mx5FZ78zrFENRhZMvywkY5v4s9e_TTJhamIaviMl8BA7dTVCIyZl5kHj9UQdrB_DGNxoqsbrhz72HbngROEiGbxoTSHvy-Klo_9eB5cwBEJox4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcVtsv1bDKFJtYqBb2icp2e4xKf3l0W2khwEbVrdAWhAPu1LyywH2MHVVm10CQFDqfOsWf5BF2yaMdqPTNCM57DFyGj580JmxdQh1CdpTjFTXIX-i9dWSvM9XPKm7S55G3TEM_JNmY_r2bUrDzgdxgjDwLQIxSOTapVpsNKwNwJl5t-fvYZnI1UxsYokuqn_OMqXnvgVHWTgwHCr_4iiIJk0BVWuXNwwWVw_x0T8RNRQSQV-2A7C96ywAL6ofrPFugZ_zVpmWwju-bgDJ-FN3A5rCbZ99w1v9hxIkKdIkS3sCMsuR9q0AWGZeSXCYIiJKIAK_TaQ-3FfU-rWf8WfXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivL62Y9w9WFCNlX5qRzMZROb3D4Hg6jLfY20IPikAGvwJos5nXV_lCBC1INPLrJ7ZTWPQoHBgcTQp6Uk6DMof8oP-EysFM5Y80uDswxPzI4QQ6hxVz31u83TKGOmAwVJvuQxRYKE-NrxdhCqt9h_TOaZ-GqIMrVmYWl-CFBoMSo2rhGilW8Ft5TLlJiIyTtQP1dqs4fLqL4W7un-O0a_q4qxqt_dO34z-K4QFPelYbIU9aJweBH_Rw21WO14Et9CV5f30JKZKC3eL2cMMk3t3blra2sLnOvwsCoT2xPMGN_SktlBUjTpE5jBDeMGwB1QUXGDKq4J3Jpwg_gq2LsIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBklQ9s41a-bf80E8OtIjOKNRQMiMZHW-AX-TtNNxQSUHIf1-Az3wrkyc60LMdAkaydEgD04sgWuI01bsw1vJ88qKy96AH8FKc8YeAILhU5FrrlIusQ338eqmTbqPt4PY2cyAHH2hrvIBRpcGqFYlMH6YV_Tt5S9qbV2EwgY0DOWZtdXdMlFpdXbmv0e33Py-Kbt8sJosR-pB02Xbu0_mDmRy6fKK_rCTdtJ8UmlCI-6MB_c-UPWomVk_U68ISMhAfjyS-s3iGNYxqJXYuq7PQtQutQrCPS07UO5YTGMYBTwIYwgLnrXTDRkCA9bDAmEYSEB7IFxKURq736N4Qd_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR9bR7U9NeSrIdL_Sf7KnULHaln17vEOg33ikTiE2LylZWdcnE3GKfh24ix2ypi0NhIVx9zxi5Y5NEkM3Yyh9OOnmOkemERiWttrjn9WiXVbkbyFXdiJ7XcEt44giLKsUYttkUsbbc1_p3K7fGKnivCXQW-HIDPTbpPR-4wNXzUl5c3rZJo6my12Xnilp6qCbi3TO4eSio5Quq8LToj8oCTaKWGedH84iX0XKiBn03NTAPJ6oMsjuPZdrBZq1RksEKe-Y68DvSJ7pqo7WGr_7RtF5AhvuP5StxiDMY-qL2JDiJEAnHvGNlbsUEexekz0g6_hYVdOl1sL9OcgPI9pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjZqjfoMdzkHiUzzZzmw5_GX07ERDqoh2m2qqvU5jHyL-byNM9MxxJcLrVbnYGxq1kTDUIQaOSkX7lsIas3MeXvmz5QpIkIGCxcHJW65eBeCaRijzHGOnHivUG98yIU3dWCEAzvydkGWswk9fhQ1GI7fGnqX_Wg9vlAL0XWFzLFEmU0NuavLDFfDkJ1J2UxOKaIJ88VPoDkjjvyKr9qXfugHduYwFd4KrcPIq_x9eKuBx1AZ8MR-bYFq7qwKk4npg6vklZANDnpvKRQI3ONMiCpbxODe-Cy_ArIt7x-WBG97H16Um5GdjISOd6506kL-6iBfp4Ns7R_4ZO4MNGLaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0atZG8fNuzjA5yhJi_HeRJIIT4O3jafYPJhWIq029gpaA9htxQ3ByeQmbwnIq0W8A8QEn9ZaKeJUuFVR01UcnG1zbr_t_9pZAPrqn1WDIurfuHucXvoz0uv9GbXjMhgXztt8rAGfS6rv-ifOWvGC9BW9g-eqou0bmiMiLsXmRGV6lNgeWD_OzObW_jBQy9xa1G_tFDXblit7BYPZPaFXhuKdlEve-8PxhTffY99eI05pe3vnA7EwDPxc82qwQmhjy6ON9lg1AaD5Ik47QJEGWUa7mfCb7Ehfa5erpz18dcY-4398hWxNrcXBO60htgjx_JEuKZnj4gefoY4fo80Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=E2txP5pHhTl7Q-QjueLFVZfzcMbyQrXDfMUqbymlyxYPiXbEt0lm5DSBIMNiJ8Z5SXNqmD3ROxTVfj3LiNe7AG6_erhitQ86iiI7J7F_MD77iJm4p8iYqA5SaQEqlxzIv-S39Q2V1VOHTLU7tK1PEfgdEjdNo99EnQN645kdh7rBhndqfW97qYzbrQ_f79TweaKaeNSmLQNRgiEMprdPL7KQz8gt7-E2yVqb2fYLmU9k771K48Dm_KV9CAeL__i_PbfUir5KJx3YKmzmhCgwzh32czmLsB_QdrSDmrjsFf5X1F9LMGwwtUiFhodHqTjY0o5nOwRB2OhkPW-MEqgoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=E2txP5pHhTl7Q-QjueLFVZfzcMbyQrXDfMUqbymlyxYPiXbEt0lm5DSBIMNiJ8Z5SXNqmD3ROxTVfj3LiNe7AG6_erhitQ86iiI7J7F_MD77iJm4p8iYqA5SaQEqlxzIv-S39Q2V1VOHTLU7tK1PEfgdEjdNo99EnQN645kdh7rBhndqfW97qYzbrQ_f79TweaKaeNSmLQNRgiEMprdPL7KQz8gt7-E2yVqb2fYLmU9k771K48Dm_KV9CAeL__i_PbfUir5KJx3YKmzmhCgwzh32czmLsB_QdrSDmrjsFf5X1F9LMGwwtUiFhodHqTjY0o5nOwRB2OhkPW-MEqgoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=JvvDIlyZ3pn16E1gQIkUmu_ql8xtq02Afb2SHkfH6V9XYRk2p3dSwfdI2jYsEi-ZQVFtCiIYF-Qj0MZEEe2_XR7O8hV9lD83KSFgonHrY-ZbKNmamt0B4IkrkBhdQTI8Q6xmxgQenerZhlBe_12RyDMIEqjj-3N9EOQUuGYbsvZfCouq90e_3TMgLQw7-AMxJF6Sjh9vpI4CLyIJgJgv6aR3otQ-adoNXl5dLjQyH9hRsYbgIbnKav29yvuVvOtzcHzMCuJubxHV7VCnG4m2VkeT_lMgfANP2pCEo2pIM8c5cqzkotuiQqBM3sy8g0LYsx-IT-kpxR8T2p0UpWfeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=JvvDIlyZ3pn16E1gQIkUmu_ql8xtq02Afb2SHkfH6V9XYRk2p3dSwfdI2jYsEi-ZQVFtCiIYF-Qj0MZEEe2_XR7O8hV9lD83KSFgonHrY-ZbKNmamt0B4IkrkBhdQTI8Q6xmxgQenerZhlBe_12RyDMIEqjj-3N9EOQUuGYbsvZfCouq90e_3TMgLQw7-AMxJF6Sjh9vpI4CLyIJgJgv6aR3otQ-adoNXl5dLjQyH9hRsYbgIbnKav29yvuVvOtzcHzMCuJubxHV7VCnG4m2VkeT_lMgfANP2pCEo2pIM8c5cqzkotuiQqBM3sy8g0LYsx-IT-kpxR8T2p0UpWfeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=TP88icXQVmmaorEGri4igQ94HYotzIUwjd2-f-2pibEXE1GwCa6ZDi0fomf1y2LsAEaNCW4JigkIYUPVZPGBhXvdLYcM_Biu6UqPYjjl6jHRx8PbiRuxHBwmzEsXClpgLoMoM0pldxrQGnlmn-l3hsy7uutGapLeI_TmGjonuJB4mKYsK6OMt6VAp7ArWxWQ1d1ILO9oEdqa8AEOMp9B_INgMaatW0TRwrg7PrFXAmt6pRQd2BQkr-EZ0sW4MsU91eeGSrNR4oWJRvr7a5Op5Vrh_0NMcKhYvw4Qt2O0mg6mVp2fKpDMNPcqPf92UB-0PXP3Iangeq7eFk-X_rMKdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=TP88icXQVmmaorEGri4igQ94HYotzIUwjd2-f-2pibEXE1GwCa6ZDi0fomf1y2LsAEaNCW4JigkIYUPVZPGBhXvdLYcM_Biu6UqPYjjl6jHRx8PbiRuxHBwmzEsXClpgLoMoM0pldxrQGnlmn-l3hsy7uutGapLeI_TmGjonuJB4mKYsK6OMt6VAp7ArWxWQ1d1ILO9oEdqa8AEOMp9B_INgMaatW0TRwrg7PrFXAmt6pRQd2BQkr-EZ0sW4MsU91eeGSrNR4oWJRvr7a5Op5Vrh_0NMcKhYvw4Qt2O0mg6mVp2fKpDMNPcqPf92UB-0PXP3Iangeq7eFk-X_rMKdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPny1rsj76EWV3_qmjGRsZq4UdjjW1kz7027PzJ5QnS00vh-CiekJkWO94nht-jC7i3_177-8AXVZLLzSFTLCX9QzNfUS6CmP88V2RxA1O8C3fxZAziv7S4189DMfIKHIfZV2V4YJRE3VpsOYwmEa0bgWdT0Ry1fS3K0Co8rRYG4nMt2rorxFO0FPsrZUK1nrDQPWedwB3OBjUHqq6Vm01FMA2p0B3BQRdXY0vElB3T1c9MMAZqsKwoaBDXYihht2Or6W4wbZHbRzFnjQGLNM6wOPUz2I03hxtVbfR0kkI7-2MAPxtJMLuFsyzMURC8cPWciMAzmcg2CqMJ5TUD0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU2ZJF2EhsDR6mz8LXLwa8Pd6qFBtBoU4uBmUdHF62EtO_MbpIS5l2at-xawq2wZMmMa5URGwTTsw-g7FVSiH1uWZZc7Oj_UCzNIvumjd1yjVmLI3gdQhrSebT1coOvb0hS9p0RhcXVvPKB0PER_OTFT-HdY59zEn1d-kmddw2J5n9nje-q0m88B7HNm7eFmzgjYdDyUHcMY2eTlAk64IGHybl7zzfs5r0CdFktx2GOylRmiZDVSRz68mwE1ckaY9EC221uSCkakYrqoCzy4avCV0jBfb0Gi4MfwRtDQ2huwvB0mVy-mlWgpqnnF9TOJPgaTWem3OYz9oznSqlug4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=mv91sVlmTV12R05zUlAbxpuh0jNH9o1Ykd6AU00aMS6hsrNiwBOch5SoIFjphnvjUMiIVOWDOWLWanTfSWBaD61x6nzH2KQ0wYpBMv5maZW0REz28ZJ2Ij6Wkp0NMnYvSdCncHxDaTqh9O8STwfr4e4Vl60aN1szD0XrXwswg8kSnMGT6Fn_TZNnWffUOPPgIX3QAk1JpfcZNeN3TCaQn9JSYhzortiomXCYTPCxqxT5QZtnkVbnJ44Ia1xSMoNxLiERPcDHdm1aIa2nnNgDrHXs34ghIzMaKvPhgacvqs4GkHXHsm3cGVOWJrybNC3DvJB87k1158daboTZWT67Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=mv91sVlmTV12R05zUlAbxpuh0jNH9o1Ykd6AU00aMS6hsrNiwBOch5SoIFjphnvjUMiIVOWDOWLWanTfSWBaD61x6nzH2KQ0wYpBMv5maZW0REz28ZJ2Ij6Wkp0NMnYvSdCncHxDaTqh9O8STwfr4e4Vl60aN1szD0XrXwswg8kSnMGT6Fn_TZNnWffUOPPgIX3QAk1JpfcZNeN3TCaQn9JSYhzortiomXCYTPCxqxT5QZtnkVbnJ44Ia1xSMoNxLiERPcDHdm1aIa2nnNgDrHXs34ghIzMaKvPhgacvqs4GkHXHsm3cGVOWJrybNC3DvJB87k1158daboTZWT67Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj0yq6AS2-FiNjKnjG2xFRcokE5VLI0mJJguue3zD1erq2W5w1_fYjWK_wmtOFrSMVgfu49C2-ZTYYpMkGWskS1KNrD0X1eNKkvg3LTcAG6XO-6MSPaYHJzmkhFQzmIbG-oUXOjuoBEo-GBMAXgmLGs8Fc3ztgjj_pbU1Y1QTWVzmcP6bzB2HOq18Kka5DcKrpxyYM8VuSt5PAiAkismQ_jnemrkurLpCkQy5UysmexlP-9sPH3O3uyMfeadL-vkdpzrBNtUtYqDnwwQF3wBSfWt2_pTvCjjAXM0dgb5pREOZEZ5Wb90uAglwe18s6c2EDvNtyid_lQ_AZKJdroT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlbX19u7kv4dp-eprAllRWrwUyni80BRkfuZxgEQp54X2s_CudroMf8Ku0pH3A7pgjPZ19LYS4IaMyextoImvg93i8s3FPTjMWWbCrv8HeHJ0c-7HLhhz7VyaVn1Nq6k90UBx-pKukxIVuynPUO5_vQdVSgfbG9Q5GiyMEChbfbbwcm_56ZvOWLEx7L8jtj0Bc4yAbVS8d7m-Y5kPOgNibhg-bmWY8Rfmhwj1tm5L1Ma5HEca0C9jsE_xrdP0r8KewTCR8ZPP7DJJAEXB3SJUFD11LfD5AzW-17yhJvH2fVr0USQDqnBghWZKFo6LtWZWzxt4H0lVYCzFG2pUCf82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7ED1MLvdsT1fhljfnOsNjtNChf2r4wA2iLtAQGCTvgUN1Fncb0OFm5GTZYTP8jVrnWW-jCLNBeG-WErFxuCHNRk9WMrby-bFoGBHY69eUZRNnj4ce8cllZL5gYfOwq2EaChCgEnrUVKimbvgSuwRfhDEtADg7-jwhMVI-rcG8CKWhtMggGLsGl77oy7GFd5HB97sjlAUqAG0YCVCpnI-coUWKse2zvBxLYTzc-KDVAn_ftW1lo65QLsM5H7JJRQnpAUBeHgFJGeCwyWln1wSpnkPv3AmX6_rivEc_w4iV7YFW5fDIHBD6icX3aZYeriOO8FI9HsnWLYcAiuKs2FTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npv38IzDDLgLQdxg8yT8poPsMaygAdIjhJ7fJaDUeg4S66cSN6hyYng8VX4CkIYuAaQhoLFQvFSg_7by6v6FUvznMgQPdGPxFgQUQ84qK3lTdYtM5g0ybPLpgyyxgdUhHn_k7I01d7CKSRtX5LRaRJHM4JHkBDKlP4HW-JANC2sU2CyHCbU_pFd3sJcpT15D0UNPEYEU4aLtyvksF8dCKuGh2DlP8ixDaIrbgR_t58KDR7EFnCg5kCV23wjV5Ckx-KFMulmgrV5xQkif3UvF_3zCzD9FVAnLV-dUWoPUZmqLbBeiqu_5NgKabVHLasdv6uNaXkATuvoR_ztJ2J6jww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lETU3nNOWeRpNDMa2_jrmzGvuWWigxqaWorps2bwZtZlwgZrlmJ3OlYxyKa3UsTQSmsGCjxy_izDR5BU4yTWtel3h81vfWXHV4Ytrz4DArbM9IkIG-_QL1sXW68VuCpxw2o4ZGLORS9e7R4xy3WF3W55ZOu6Z70bEazGG_QgcjK7xeP_skAYf2R_lEXQQW8U4nuVXvgt7SBvnT8HrO_WKdwJtaZOQtLi9W8bg_xlfoDrPqSlhG0ANUfho7C2sBpnOxQv1pD2etIZ34DWJr4R2TGLXh-uEY7qxRPyVWqw3lH-AROXfkPNY7-ukt7MlS4TM7slI1IBnM2xWHmI9DTTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
