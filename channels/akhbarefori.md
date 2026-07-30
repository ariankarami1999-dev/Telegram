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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-676795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دادستانی تهران علیه افراد حامی محکومان بی‌رحم و سنگدل کودتای دی‌ ۱۴۰۴ و جنگ رمضان اعلام جرم کرد
🔹
هشدار دادستانی تهران به برهم‌زنندگان امنیت روانی و حامیان مستقیم و غیرمستقیم دشمن در داخل
🔹
پس از اجرای احکام قانونی تعدادی از عناصر کودتاگر دی ۱۴۰۴ و عوامل دشمن در جنگ رمضان عده‌ای قلیل از چهره‌ها و افراد با اتخاذ مواضع دور از انتظار به طرفداری مستقیم و غیرمستقیم از چهره‌های اغتشاشگر سنگدل و بی‌رحم آن وقایع پرداختند.
🔹
این حمایت و طرفداری سوال‌برانگیز در برابر حکم قانونی دادگاه که همه مراحل دادرسی را طی کرده و در چندین مرجع قضایی و زیر نظر قضات باتجربه رسیدگی شده بود واکنش افکار عمومی را هم به همراه داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/676795" target="_blank">📅 22:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد متفاوت نسرین مقانلو با هوادارش در حاشیه مراسم اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/676794" target="_blank">📅 22:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8d15aa0b.mp4?token=YizA8lsA2L-ogiTWRPzIzLh9B76SsI64f_b8itzGSt1H9scsjHK4CIzgXkc7xEjOq7mGB_DpJf9E5KwzPi2d_ziOBZALLknIeM2r6XZ2Yy8guRpKfJjcri-qi06bP0N5ADHDokXZplFGF5THBSYMZKCXzyxEZpR41QDg1HrnrUUUHVTyP34RwczGKsNJ79L9So4r9WTgk1OO7FWEvizwmT_w_CeO8B40W5qaw_5DYv00QJl9u7mlJyJb7cmS17CyyXmSp5op6LmhoP3FlBD-cJNRZdIeZ0P-GxrPo-aJxrQaE3_M_UfQpaOIqEofRcawc8246evHSAp9IcYWJz2cHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8d15aa0b.mp4?token=YizA8lsA2L-ogiTWRPzIzLh9B76SsI64f_b8itzGSt1H9scsjHK4CIzgXkc7xEjOq7mGB_DpJf9E5KwzPi2d_ziOBZALLknIeM2r6XZ2Yy8guRpKfJjcri-qi06bP0N5ADHDokXZplFGF5THBSYMZKCXzyxEZpR41QDg1HrnrUUUHVTyP34RwczGKsNJ79L9So4r9WTgk1OO7FWEvizwmT_w_CeO8B40W5qaw_5DYv00QJl9u7mlJyJb7cmS17CyyXmSp5op6LmhoP3FlBD-cJNRZdIeZ0P-GxrPo-aJxrQaE3_M_UfQpaOIqEofRcawc8246evHSAp9IcYWJz2cHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیستی به جنوب نابلس
🔹
نیروهای اشغالگر اسرائیلی به منطقه «بئر قوزا» در شهرک بیتا، واقع در جنوب نابلس، یورش بردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/676793" target="_blank">📅 22:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676789">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOo4_lRwiaCqeEQDPdyyNsSDSPRS4KFwfa3v-n5nzpK8A2Csx2J9cnPzkT6l_3C3dOcYFT-p05XrFh5wOsS34UUDvr2MqCaa4b07zQ8gxJRmKbzJHNCJFzl1xGVavpMWj0XT6aS2OKbSHR_801LVJN-qxFzf-4ZYM-DP-m-uY_Xe-ER66BuIcoUli6d5UsiL6dDkj6NP5KOK5T8goj1Sy7IyZc3Mz8aeq4YOFHC8sUn8J0-cyjK9t7iFuPlVYu8NgbnfIofj5anruPJG9Ro5_ZVpLKsEtS4N_95KFmfsVmbsEGgddleixGqXZvpXbaaTRsuhmq2gG4EAujfolFQT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJjGyRuw_yZZx05HJHLfKfRcb5KxLgHBESL62arPEgMgGB_2s8dub-UvrRNNga3Xrz9d__RXgHOPwOSjcEGlgQRBe7Ko2u9oSTiQ6PX5W9HjZ5-sN5s8zEEgbAgRs4rNirSPFohu7y3RqGrIVwmQSIYpyFE18yDkWCUcnP3NSGFSworbfR9vUlhMS7exBZQ_C02J9ic2MjQLJfzy9ekQh96X-6NtvMqSo0QZehCuUU-fQyKXeykwuLFXIuXM7P3SXaZo0A1ugFM2CD30p7_lMCwh5duT0ydsTaFZewz-ubXqr54WAiPLfASc0xZAfuS3b9nAy8ep6H6aPeWv-Cvqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDMwKZtTRuKzEBLO-gqz5Y5OKZe2SlUoAlXclVrrKLYU7Bs-6pXj9OYPZuQqN0E5D9a1dKGBUNUH1Vimv9l5mADkUWZuzleGK_8qs19qhZA9wC7OUrdW1KQjQ9SLf5Q5BGLUsd9ELhiDIgFIy8-kl9F1EmFx8CZljAw9xSSO06ryxgFMpXpPqqlxZ1KDQ2yAWDdIhEqaTmYmh8dHXCYrVREKWpSoVOcA5q2uFd0Y_PLQiF6R8OK770rlA95SxOO1rB37GTw6NwgE7A3a-t7o-v7IZei9zMIgQt9ozsMGKPeg2P8KhA3DIjTunABuh3T36K0HQzr5rQFwmZ9z2lwHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVJfU1_bx8bLQDnROcGCqFI-kk_ECpwEVV0_P3R-znKa4ymB52tX0oeNj58SfQaUkPu--WL8aXc74Va4rBj5cDMhWGA5cGiH5FbYLjqv5PCkzeRb2pj3Ns8GIIJaWjuLGzJVAdXMRErk6_x3YEQoZDZyVIXEEaozdklLM5JrZ6GfBdi4KoCgSYLgqkNX5JJXjrr_cMDwxQ3QuiwsamhGQtDwknTefnmA21HFRmReklw13HG1qqb_V-BQb9pxYEirmWIoKTWS5z7cc6qC1Xohrg0SKAkeWGG7iTnDysdgtZ93RNjkdnW7Nl0O9EWVkOfUXuo_vHdHmCcRiVBeHyFpQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نه به دورریز غذا
🔹
به‌اندازه نیاز خرید کنیم و از دور ریختن نان و غذا جلوگیری کنیم. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/676789" target="_blank">📅 22:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بقائی، سخنگوی وزارت امور خارجه: مذاکرات ایران و عمان ادامه دارد؛ تنگه هرمز همچنان بسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/676788" target="_blank">📅 22:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEY4Jk92FL2OOJfmUt4-WGShjjiyT2T3w7O77iFOsFR9P8veZ1B3eCk6nvsRdhHQRQfq5tNdFFX80jdj4yHmqNCiynyzyfg09ZjQz9Gaf3fQCVWk_lt8X-f1upolirtK88xr93Ey86RMpLuHQ7b1pE67pv7U__0eNpVby5y0fbSGAGCKkjDVmfU7D5cCdGAaC68XYA2KXzM2ctwd8gvU1D96BXJztM0yT7DeFAcvKr0I1_4ePbxvS_y0BZ1zYOMIRnjh42swHuHVEqW0eAXPAD-8vvWoKUyktEr53LIeBg3o_kmoiwl86sXKkr5SQG-tEZWqm3vvoul0vN4LtsjFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: آدم برفی
🔹
ژانر: کمدی، درام
🔹
خلاصه فیلم: عباس خاکپور (اکبر عبدی) بعد از چند حرکت شکست خورده برای گرفتن ویزای امریکا، به پیشنهاد یک دلال ایرانی تغییر چهره داده و به ظاهر یک زن در می آید. با این ترفند او می تواند ویزای مهاجرت به آمریکا را بگیرد…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/676787" target="_blank">📅 22:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTtR03R9SY82P0z8oKnMnIgT7BDXtWYuD-ryEhcJwdiNINTp6HiK_4Fw8vStx0yLVrBJI1Psj4NpwR_AR2jcSwGj7nu8V2RP5YvcgXVmxxK6klFIprPiWpzivaXqtn8awPiiMkySUzzR6arv_27zpYIc-uBjIyv3Y_Tc6fmUDxQPR4ntQFCRV0AeR46rZWyfHm4FbKvc2A1PUBNq0pkfzXJxw1UeJ0FPPxH1a4l36xHXG7wWvb5eH2Y4Td8YhuvrZAaxNWrdWk0sDVYVTJDboccJWpyqWYZo6W2z5tY4x1NEJiThoDaSeXxsQ_dLEXfPxMgJ93cbQ2h2lX3p71pvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه پیدا شدن پیکر بی جان کودک دو ساله در حمله امروز آمریکا به قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676786" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای یک رسانه درباره نقش پاکستان در عبور کشتی حامل گاز قطر
بلومبرگ:
🔹
پاکستان همکاری ایران را برای اسکورت ایمن دست‌کم یک محموله LNG قطر از تنگه هرمز جلب کرده و به کاهش کمبود انرژی رو به وخامت خود کمک کرده است.
🔹
کشتی حامل LNG العریش، پس از انتظار در خلیج فارس از اوایل جولای (تیر)، از این تنگه عبور کرد و اکنون در مسیر پاکستان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676785" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676783">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e84b3389.mp4?token=thl-45N_ccs3Q4vs2l9T_SE9qaLfeWBErO0UEq8KD9hTz1G42QO58cnVLH-DwE9Pzzb3qJRoLpxIKeCNd5wfnVGOnd7SUII2L-Ob2M_Vo_g9ggreM9b3OKeSvI-piJTUkd52IsaaC7poeYeUfgqHsKFYiBWtD3wXK10_KxLlizu3FV515d4wy3nVrD8HX8dNL1waS5SpHxdq9FOUAEKJvGmtd5oOiMROYd6j3uwL1lBUhX60obGxt4uUUn_MZGcEnVq5x9GlsycBU7TjruRjWLLUzDkPAqfLyFyJ9gLQ0iXkWj7fRFBVzA4v0X9xYdM-QUrXPsRh9NQZQw5lIjlTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e84b3389.mp4?token=thl-45N_ccs3Q4vs2l9T_SE9qaLfeWBErO0UEq8KD9hTz1G42QO58cnVLH-DwE9Pzzb3qJRoLpxIKeCNd5wfnVGOnd7SUII2L-Ob2M_Vo_g9ggreM9b3OKeSvI-piJTUkd52IsaaC7poeYeUfgqHsKFYiBWtD3wXK10_KxLlizu3FV515d4wy3nVrD8HX8dNL1waS5SpHxdq9FOUAEKJvGmtd5oOiMROYd6j3uwL1lBUhX60obGxt4uUUn_MZGcEnVq5x9GlsycBU7TjruRjWLLUzDkPAqfLyFyJ9gLQ0iXkWj7fRFBVzA4v0X9xYdM-QUrXPsRh9NQZQw5lIjlTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک خودرو در اسرائیل به صورت طبیعی منفجر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/676783" target="_blank">📅 21:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nM4WJMpmX9fL0qf9erV2pfDhHRGsBGDLgoDFHmKqHpVf0HBcPvT0DPqOfgKc-ySwiqxa1Fr93YyF_vOCvcAouVhWYf_ryevezZLQyF8eWts1x_6_qOroB95iyUOIpVyXwaRCEFCSouLhJ51wEVNL0cGyBNaPQN2PNn8AywUnNyYs8mqTCub2rvPf6bEh-CHrPhpqcqmxc-k_F-Mq3nrcfVyW9iQZpKEkFW_GNfr8asGoVMC2hse_HUbCXvF6-yfaDUU_mSCgzdqq-48K_CtC73lpjTP_zD42GLMsXfc6_eYUgGLLRNPfNRtcIm61VpA9xjmS3w8Ojq79LgUAdrXI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای سعودی در نزدیکی مرز با شمال یمن ماموریت جاسوسی انجام می دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/676782" target="_blank">📅 21:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDr8rqW8SU7GBq4FHCQRPBVHkbFMwggyR77ho3B2yrYe8Q1mlTl8d8scsT6cjC6G0P5qSvARcfTwKzroCtuAyNQwayl2Tyqb__MiULSb_Gzh-QBFgUZ7mcZ2MLCtAaJ-aYUXwqZ8sZF1RJtyKPpeLIvVdbgFRFxkzfNIdKEZ0fYdnz0aRm9SnVGqlFx18s1hMhejsgNYv2GdRypVn3mHGUdoSdBQQSUBxqtnGfk9uEPzr9Fm9wYWN7roJ_vYXNVlYqfh-LQfUplZk8v5i3OImNRGWtNtviPrR6h_suveG6I5xf8a1VIOQ-Dpa3k8bq3CP_mc1XvAIQ5AvqO3XADLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس بارگاه امام حسین (ع)
یادمانی از کربلا؛
برای خانه‌ای که با نام حسین(ع) معنا می‌گیرد.
💰
قیمت ویژه: ۴٬۴۳۹٬۰۰۰ تومان
۴٬۹۹۹٬۰۰۰ تومان
⏳
موجودی محدود
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/676781" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: با حذف دو دهک بالا، سهم کالابرگ هر نفر فقط ۲۵۰ هزار تومان بیشتر می‌شود
صمصامی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
نحوه محاسبه کالابرگ یک‌میلیون‌تومانی دی‌ماه مشخص نیست و گزارشی درباره آن ارائه نشده است. با حذف ارز ۲۸۵۰۰ تومانی، اگرچه یک میلیون تومان به مردم پرداخت شد، اما حدود ۵ میلیون تومان به هزینه‌های آنان افزوده شد.
🔹
به‌صورت کلی، ۹۹۶ هزار میلیارد تومان برای کالابرگ در نظر گرفته شده بود؛ سیاست کالابرگ به ضرر مردم تمام شد و حذف دو دهک پردرآمد نیز تنها حدود ۲۵۰ هزار تومان به سهم هر نفر اضافه می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676780" target="_blank">📅 21:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYMlV0KyuqyTe3MNk4k8-btnSwoFfvW_KMUAFnIV1GnCLpqZGzWT5WF2ct0xU2MJa9Eeex8sxI4R9qIOmo6j5XdD60dXJMH55vIpHWyDhweUBGtmyuUPuRGRuhEmbRI05FU_aQAL-HwgHPm5EgMeMd8pmZVQbusNtiN4Wxw6lb11in2OySrDSRGc5q9QDOPXWEgNfNhDkNfaOpKlGvrzsKNPV7sOMWQnoBM9rzV6knJYGxa1w_kIUYzJ-J5sjCNbJYSi0UNdXAd7Si0lZEi2pa_TCWl5J6S4pZ1AsVTY7r07ITQ2EWKiht_r4EwRfR_CFGTjgTjoaV-s0j7rAdGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باید روی تابوت و تجهیزات جدید امریکایی بایستیم
سرلشکر علی عبدالله فرمانده قرارگاه مرکزی خاتم الانبیاء(ص):
🔹
آمریکایی ها و مزدورانشان امروز تا اعماق وجودشان متوجه شده اند که تابوت آنها بخشی از تجهیزات آنها در منطقه شده است.
🔹
آن رهبر شهید گفته بود که زمان «بزن و فرار» تمام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676779" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-wZaYM_1JSAJilch-t3wH-ZdYjACNQqcJmP1R8BJsb6H91zM1XWvYfVAn4m4c1HJrG7Hzfeectt8QgD9B1L7JfNS7kQCo81eGF_7-VWoXDHIJl0bFBbtK5py3vJ7llfoBIvsxmUNPMTla7-nDeKnJB5A8YaMn03vKx7rV042iCzFSfxdvlaLwwV1vkym38FMPsc5prwYL0-KdWK6A97237Io8RZPAPUV__E_dcmGQItjlCmWQFqwp8Vc5XE2f5VMLMLt1VA75h0UhPv8b9paPe7ahFeO8KB6vcrVdze6Ixl2zDhSsxyFhaCr8uJ7wr-LXdl9WoavwtS_P6t8acWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: عربستان سعودی در حال آماده شدن برای حمله احتمالی دریایی و زمینی برای شکستن بن بست صادرات نفت از طریق دریای سرخ است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676778" target="_blank">📅 21:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گلدمن ساکس: تداوم محدودیت در تنگه هرمز می‌تواند نفت را به ۱۲۰ دلار برساند
🔹
بانک سرمایه‌گذاری گلدمن ساکس هشدار داد در صورت ادامه محدودیت عبور نفتکش‌ها از تنگه هرمز، قیمت جهانی نفت در سه‌ ماهه چهارم سال می‌تواند از ۱۲۰ دلار عبور کند. با این حال، سناریوی پایه این بانک همچنان نفت ۸۰ دلاری است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676777" target="_blank">📅 21:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROkZFp-ob9G1TkFYwGaWivjVj5eqUuWjsVABZyDYQ526fhyONhj7bhrcD9mXs8ytFdiMSNhn9hYtIQAupZ1BwhxmJZLWQGcZ8G3LKZrS67nn6PbcDBc0MXzYbruYTIfDVDZ8AKF6a_OPc4X3PwiIhGMTvrI6_UYsGxVtX8eaT_1FDaAhtEwuWyihCEz94qkXoSQEAmBDdnHTKepQhfW5TZ2oaSnN0n0MoH4imfor8i0y981p5UmRCWeR-9NPDMWlwbJic-LVsW5T-MhY6vTzlIoSLMFAoUz09vGY2MTYTAwRoW0-_7wjaIbkcYUejYUlwRwZrUZuFcjNNphR-rV60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها گسترده‌ترین شبکه حمل بار هوایی را دارند؟
🔹
آمریکا با امکان ارسال و دریافت مستقیم بار با ۱۶۷ کشور، گسترده‌ترین شبکه حمل بار هوایی جهان را در اختیار دارد. پس از آن بریتانیا، چین، امارات و هند قرار دارند.
🔹
ایران با دسترسی مستقیم به ۷۹ کشور در رتبه یازدهم این جدول قرار گرفته است.
🔹
هرچه شبکه حمل بار هوایی یک کشور گسترده‌تر باشد، تجارت خارجی، زنجیره تأمین و جابه‌جایی کالا با سرعت و هزینه کمتری انجام می‌شود..
📊
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/676776" target="_blank">📅 21:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgAHC7qkQKtRUb0VnfrR3zKQA0oDcZ0ote3TF-oPL7FUQ3wh1Qe8HJzNFPMbxti-w6RkoRmY2vmFDcyirtYYyp5RZXhDKb1P1ggBI3f4AgpBJKjEQuT9vohwPOZyzIAvS_xk5A_xUaHHNZ7iRTfzqimZStBqW3z-vDDQiZalebKcsn1VCMUmjRId9-xz45mfgNFDf8jYBQmhtZVJSMGf8HdVvhIWZGDuWx3KyhfTgs4BRn0v0WbmeShHMRhaKEMULZ6_qPY4_Zwse5JSS4kjseg3DRMxHwbzQsKhDoXpTV5vEmTQQdOKv0VXqjY3jtVY2kllSsqvtkmoZsSI0TITEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آ
مریکایی‌ها از ترس ویدیوی افشای اطلاعات ملانیا ترامپ دست به دعا شدند
انجمن شفاعت‌کنندگان امریکا IFA ضمن دعوت از مردم برای شرکت در دعای دسته‌جمعی:
🔹
پروردگارا، لطفاً به ویژه از ملانیا و بارون ترامپ، و همچنین از تمام خانواده ترامپ و تمامی مقامات دولتی محافظت بفرما.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676775" target="_blank">📅 21:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676773">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
میزان مستمری‌های ناکفاف برای خانوارهای بهزیستی
یاسر اسلام‌دوست کاربند، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
مستمری خانوارهای تحت پوشش بهزیستی در سال ۱۴۰۵ نسبت به سال ۱۴۰۴، ۵۰ درصد افزایش یافته است و مبلغ مستمری ماهانه برای خانوار یک‌نفره ۲.۱ میلیون، دو نفره ۲.۹۸۵ میلیون، سه نفره ۴.۲ میلیون، چهار نفره ۵.۳۷ میلیون و پنج نفره و بیشتر، ۶.۵۷ میلیون تومان تعیین شده است.
🔹
حق پرستاری برای افراد دارای معلولیت شدید و خیلی‌ شدید ۸۰ درصد و برای افراد دارای آسیب نخاعی و اختلال طیف اوتیسم حدود ۹۰ درصد افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676773" target="_blank">📅 21:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBESDQrU5rnmHTi9Df92Awsgm9lf0iIwpU9UyRCPQWa80PR8YKh9HQ3V4CFUl51OzD4wBwxvqHnWCetpWJOdSzlU1mRo9__nnkrNc64MVlGn5OpdFqK2zsMD_eRoS79bXW5ZRDJpkNcO1rMCm-ZIdOIH7EO24LiTCG_QBhPJG6UfJFYoYfwIfxOqqQ6wa1Gv5sfbUTXQJSs1tNfo2iW4rqqSJejY_w4DbGhdM0wJufVy_qQZSzrLeNDs4h6-UxKhc43nF_4LhRyxIMUyxLgqQM89l2yXGofsW0K9jb9cmil4PSz6bvkaIM5b9t0sUOtbdAkiWsvNCyQDzq0HvGzeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر اولیه از سولۀ تعمیر و نگهداری جنگنده‌های آمریکایی در پایگاه موفق سلطی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676772" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مرحله بیست و ششم عملیات صاعقه، ارتش جمهوری اسلامی ایران با تایید ضربه زدن به تاسیسات برق و ناوبری و ساختمان‌های اداری و وارد شدن خسارت به پایگاه، پایگاه‌های آمریکایی در پایگاه شیخ عیسی بحرین را با پهپادهای انتحاری مورد هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676771" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای نتانیاهو کودک کش: زهران ممدانی حامی ایران است
🔹
نخست‌وزیر رژیم صهیونیستی ادعا کرد شهردار نیویورک حامی ایران، جنبش حماس و حزب‌الله لبنان است.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676770" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا، ایران را پشت حمله سایبری به سیستم‌های آب مینه‌سوتا می‌بیند
ادعای نیویورک‌تایمز:
🔹
به گفته مقامات آمریکایی و ایالتی و سایر افراد آشنا با این موضوع، محققان معتقدند که حمله سایبری این هفته به ده‌ها سیستم آب شهری در مینه سوتا احتمالاً کار هکرهای ایرانی بوده است، اقدامی تهاجمی که در برهه‌ای حساس از جنگ آمریکا علیه ایران رخ می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/676769" target="_blank">📅 21:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنای آمریکا به طرح توقف جنگ علیه ایران رأی منفی داد
🔹
مجلس سنای آمریکا به طرحی که خواستار توقف هرگونه عملیات نظامی علیه ایران در صورت عدم دریافت مجوز از کنگره بود، رأی منفی داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/676768" target="_blank">📅 20:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWKaxWawWKIH-80bN7g9UlkI_NdhZmIJLcGlaRNDe8v9DlyQoAdCgUzmz8wF02PRAiUHx7Vxhcof1H39TJ_7EnhRfPu4c6ykv6ydjZIHp_yZkl4t4ryPrOGdLPxK2aGrc56yK01hWCiX2POa3e2KauIinX_cqmxb60GtA8q_kGE_fUPv_-f6A0SEMBkZGjOYRSl649Mk8zKVbXDGtgX5_z13C2B8-BFroTVyEUwzw9mPV5EJ_e8qkSmoVita1JbAhusTp9uqHKgmZtYSsuBPswc9ShxxBkxFyuEcxdj2TB3HqhYjLBtavytHRi9A7PncbGLEnJPCTX_2Ryf3-VIBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌹
یک قدم تا زیارت کربلا…
با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و فرصت خود را برای برنده شدن یکی از ۱۰۰۱ سفر زیارتی کربلا امتحان کنید.
✨
این سفر معنوی به همت هیئت قرار برگزار می‌شود؛ شاید نام شما یکی از زائران این کاروان نور باشد…
📲
همین حالا عدد ۲ را ارسال کنید و در این پویش حسینی همراه شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/676767" target="_blank">📅 20:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
گستاخی چندباره شیطان زرد: آمریکا ۱ فرد و ۵ شرکت مرتبط با ماهان را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676766" target="_blank">📅 20:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
المیادین: وزیر خارجه اوکراین در تماس با عراقچی از ایران عذرخواهی کرد
🔹
یک منبع آگاه در تهران به شبکه المیادین گفت آندری سیبیها، وزیر امور خارجه اوکراین، در تماس تلفنی چند روز پیش با سیدعباس عراقچی، بابت حادثه اخیر از ایران عذرخواهی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/676765" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTHkUm2BI8h-nYJ_hq9uypkcWtVxuTKUl2Tlug0Z6npUFn208ymoEu-pa6KcwKq87oY1YiCafb0O9_Iv25JFL_-XVykbsmTK8XUu6T6aXd03vDbR01-fHRutytvSp0L63V4F3IpfqlJiPN901BqYa_geuk-v8WAxtCBI2GtyVjBDcW-SH-tmY8hq7bSyepvyDkZqwHWl8uCacviwzOM_1YFdP-nRGXQ_2htE97F3RxD8XLyQXX2vfRtc9mUeivBMZkIZSQlyV9BirKMV4-riMOwQGDG2ewz5osdvFsZ4Rhbbnjx1Y9501kuyZOSD1YMLEsJhFBS82wH23ug2PbmaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ؛ روایت ریحانه طاهری از سفر اربعین با کاروان شاعران و نویسندگان
🔹
ریحانه طاهری، شاعر، در یادداشتی با عنوان «قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ» از تجربه حضور در کاروان شاعران و نویسندگان راهیِ کربلای معلی نوشته است؛ روایتی ادبی از سفری که در آن، زیارت تنها مقصد نیست، بلکه مسیری برای همدلی، روایت، مسئولیت و تجدید عهد با آرمان‌های عاشورا است. او در این یادداشت، از هم‌قدمی اهالی قلم، اشک‌ها، دلتنگی‌ها و رسالت نویسندگان و شاعران در روایت حقیقت سخن می‌گوید.
🔹
طاهری در بخشی از این روایت، دیدار تأثیرگذار خود با یکی از شاعران حاضر در فرودگاه و دلتنگی او برای رهبر شهید را بازگو می‌کند و در ادامه، از «قلم» به‌عنوان سلاحی برای ثبت حقیقت و مقابله با فراموشی یاد می‌کند.
🔹
متن کامل این یادداشت را از طریق لینک زیر بخوانید
👇
https://www.khabarfoori.com/fa/tiny/news-3234297
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676764" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676763">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی آموزش‌وپرورش: مدارس همانند سال‌های گذشته، در زمان مقرر بازگشایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/676763" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676762">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlcV3Q0TgwiVv2hWhgz1kDXb3BXOiNQCV7GBlcnMIBtosVlDwrGA_qosVdZPH3N4QRomizAZCCCKI-705HF-jiVB4bZQgjgz1PvQG8rHb3Aa9wbCEaSJyqeQyr7uLwyZnAnNdAP5zvuiaoTEfwdQbrMxarFz4LhKjVbTYuj9SeqLKvY7M_UIRGmXIFWehOWrAtEcDi6pdrW-hpIWEDGJujsu_oSnBNISC0ZORUjb1hvVhWPdn7Y59brVF5Hz64MPBXc1g-R5cQ2QKNjE69s_gy0KeZkRVofV9Oopx879WdCcAiqhh_xMjDMmnefYkNr2o0G8OXCFb0kVMjuwj1QF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه بنیان‌گذار تلگرام را در فهرست تروریست‌ها قرار داد
🔹
روسیه با تشدید فشار بر تلگرام، نام پاول دوروف، بنیان‌گذار این پیام‌رسان، را در فهرست «تروریست‌ها و افراط‌گرایان» قرار داد.
🔹
سرویس امنیت فدرال روسیه (FSB) مدعی است تلگرام با وجود درخواست‌های مکرر، از حذف کانال‌ها و ربات‌هایی که به گفته این نهاد برای هماهنگی حملات و اقدامات مجرمانه در داخل روسیه استفاده می‌شدند، خودداری کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676762" target="_blank">📅 20:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26f0d4939.mp4?token=NZ0UYadQSY7mbXxIarT8lrBzKtLEtynCZlwuq0fSmBODOcsmfzUXJszlIyKzX3lqPRk0oI6nPciVpDHUe_pBVrZ9dSwAQ6QWr6heFBO3N3cWSSo1GXHKzBg5BC7KkWvVoG1dUmpPQ5ZBsSBGsVQxzZd5fP8pPHLbE03KaRnbPmOdF-OAvbBEXBpdNIJIVEAQxbMQv7uOkKYZgk_0hfpgiPFW0hQQ9q08sb1GQNx73XdzTAX3Ezxovd1fY2AztkP18MBRuoNVkju-tZJLEMbJ3Eh1ieno4ceGO-Io9krXJdEti_Sy4KeMYW5WsDDdxerH_zERHxTlFW-TyLAhvKkTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26f0d4939.mp4?token=NZ0UYadQSY7mbXxIarT8lrBzKtLEtynCZlwuq0fSmBODOcsmfzUXJszlIyKzX3lqPRk0oI6nPciVpDHUe_pBVrZ9dSwAQ6QWr6heFBO3N3cWSSo1GXHKzBg5BC7KkWvVoG1dUmpPQ5ZBsSBGsVQxzZd5fP8pPHLbE03KaRnbPmOdF-OAvbBEXBpdNIJIVEAQxbMQv7uOkKYZgk_0hfpgiPFW0hQQ9q08sb1GQNx73XdzTAX3Ezxovd1fY2AztkP18MBRuoNVkju-tZJLEMbJ3Eh1ieno4ceGO-Io9krXJdEti_Sy4KeMYW5WsDDdxerH_zERHxTlFW-TyLAhvKkTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه پیدا شدن پیکر بی جان کودک دو ساله در حمله امروز آمریکا به قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/676761" target="_blank">📅 20:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
روایت تکان‌دهنده رزمنده ایرانی از تجربه نزدیک به مرگ در نبرد با داعش
🔹
00:12:00 شروع ماجرا از خوردن خمپاره به بدن و گفتن یاعلی
🔹
00:21:30 گرفتن بی‌وقفه دستان میزبانان آسمانی برای عروج
🔹
00:29:40 دلهره داشتن از کمک خواستن جمعیت کثیر انسان‌ها
🔹
00:47:45 حضور سه‌باره در پیشگاه مادر برای اثبات زنده بودنم
🔹
00:58:20 دوری از نگرانی‌های انتهای خوفناک با ندای آرامش‌دهنده
🔹
01:00:00 اجازه عبور از کنار میز حسابرسی توسط هیبت نورانی
🔹
01:03:50 رسیدن به زیبایی مطلق و غیر قابل توصیف
🔹
01:13:25 ماجرای درخواست حضرت ادریس برای رؤیت دنیای پس از مرگ از خداوند
🔹
قسمت شانزدهم (فراز آن بیابان)، فصل پنجم
🔹
#تجربه‌گر
: سید حجت امیرواقفی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/676760" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمریکا در تله استراتژیک ایران گیر افتاد؟
🔹
جنگ اخیر ایران و آمریکا وارد فازی شده که  کمتر کسی در کاخ‌ سفید فکرش را می‌کرد به اینجا بکشد.
🔹
در پشت صحنه جنگ اتفاق مهمی در حال رقم خوردن است. در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/676759" target="_blank">📅 20:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308db4cd83.mp4?token=DoqSvf8t_QTUscIflUkwpj3jIP5u3EzWI2T4dnCs53D7e4lMlBdcx47hs_K76YDl4y1CyPlgs7oDuFAbMCo7WC9uX7e-zUUs0Cp1FwtA3OmNNi9UJC8NUsU8MRcoYlQFU07R1975lzceMDm-AmJObMyMXu0cRQq7hzsH7eLV7eg9r_Hy9ibezHq77nCBOzcEoE2itN7SEclJRGKXNMGezYJDidndcpaE1FUSnzp7JBAJ4AM5aKs8CmioSK-2Ry16_eFQen3GS6lZ6gNu2sSBEr2TmcMF_pHaOj13Qa_tex-9RuCLWWYplnoZVM4FSesCyaLHOLYkv0uQ1-v4xYrXJlZGzj763cCMYFKD5DJ16BNXT0pKMZOmJAx3NtWFrn8TtmmTofolUm7iABN-bsBKEgK-yIJq2UbpeBTCsXivFbCAGCz9dGHv2SeTh9ACRXrD1_6i7PHZbMg1mv4-Nh-FFdejeWcdOlvQSRunkdD7lYLS3f9Y4yJAqqZMFbWgUm5unBu8E7c9nVhPkbRM_HR9w9KNuoty72OUJfwZTUYYi-8aUF4xUaVLjhcdD0rSUEp2nT5XFynjkaweKUTn8JaA6ywVPjCG3b-D129LiUwDhmW1ezeVUW4b6_7cmpVZ1aoeZ-_0n1rjIwvh44g3FmmtOvcjIxh3ZufsJGDNLnOeSuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308db4cd83.mp4?token=DoqSvf8t_QTUscIflUkwpj3jIP5u3EzWI2T4dnCs53D7e4lMlBdcx47hs_K76YDl4y1CyPlgs7oDuFAbMCo7WC9uX7e-zUUs0Cp1FwtA3OmNNi9UJC8NUsU8MRcoYlQFU07R1975lzceMDm-AmJObMyMXu0cRQq7hzsH7eLV7eg9r_Hy9ibezHq77nCBOzcEoE2itN7SEclJRGKXNMGezYJDidndcpaE1FUSnzp7JBAJ4AM5aKs8CmioSK-2Ry16_eFQen3GS6lZ6gNu2sSBEr2TmcMF_pHaOj13Qa_tex-9RuCLWWYplnoZVM4FSesCyaLHOLYkv0uQ1-v4xYrXJlZGzj763cCMYFKD5DJ16BNXT0pKMZOmJAx3NtWFrn8TtmmTofolUm7iABN-bsBKEgK-yIJq2UbpeBTCsXivFbCAGCz9dGHv2SeTh9ACRXrD1_6i7PHZbMg1mv4-Nh-FFdejeWcdOlvQSRunkdD7lYLS3f9Y4yJAqqZMFbWgUm5unBu8E7c9nVhPkbRM_HR9w9KNuoty72OUJfwZTUYYi-8aUF4xUaVLjhcdD0rSUEp2nT5XFynjkaweKUTn8JaA6ywVPjCG3b-D129LiUwDhmW1ezeVUW4b6_7cmpVZ1aoeZ-_0n1rjIwvh44g3FmmtOvcjIxh3ZufsJGDNLnOeSuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/676758" target="_blank">📅 20:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d68ce365.mp4?token=OaqGnCP3u9VSlLzOWT1vYnECvcK9g3zJ2DUEmzpIIKWopniC2ng6tyzU1QgJziJWHIy6deD_F0NUJ16gWcxSQ5aWubKoMloo8ltLHO1G4Akt9xBeb97iuPV4wI5HsThWwYQP5Eo-SOhuloHWAGAdbH0cF6iKS9KovC7jtdq1BhikzPegBuYapqczFnFrmDUfI9OXkG-rGTlsudBZTyXNMB5HJQERqdalc6IprFaMp3Pg-goj-xZd8im_9XW4R9348Qk_vuPASo3ftMpMDN-PdLGeM9-YSGz6xe--yKmWI3W0Gzys_ZmE-POSYX0jzQM7yqvsEWPAZLYifCE623YHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d68ce365.mp4?token=OaqGnCP3u9VSlLzOWT1vYnECvcK9g3zJ2DUEmzpIIKWopniC2ng6tyzU1QgJziJWHIy6deD_F0NUJ16gWcxSQ5aWubKoMloo8ltLHO1G4Akt9xBeb97iuPV4wI5HsThWwYQP5Eo-SOhuloHWAGAdbH0cF6iKS9KovC7jtdq1BhikzPegBuYapqczFnFrmDUfI9OXkG-rGTlsudBZTyXNMB5HJQERqdalc6IprFaMp3Pg-goj-xZd8im_9XW4R9348Qk_vuPASo3ftMpMDN-PdLGeM9-YSGz6xe--yKmWI3W0Gzys_ZmE-POSYX0jzQM7yqvsEWPAZLYifCE623YHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلال در فرودگاه بن‌گوریون
🔹
سازمان فرودگاه‌های رژیم صهیونیستی اعلام کرده حضور هواپیماهای سوخت‌رسان آمریکایی، فشار عملیاتی غیرعادی در فرودگاه ایجاد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676757" target="_blank">📅 20:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b92955f5.mp4?token=tPxbUvfBtwDSEGVtJqgkvm9mhLeGQ0h8PUlKgfc2TIT-8lddP_4kaUQAsV2XpmFC5SZCy7O0KCsSyN-XfKrjPU0mfEo4KNRysa8UJgPGZwdeUoTzsmYvGBdFHZpTzOX5mqBfZFHUiFwE4rs3aYOtYxlQzT0jzB1QXWKWvMia1eix3Qc1Tgxcl6Ua75LBudhcynF4nfb0uePwzk52DrGc7KXee820yDqV5FzMzPyyb_isq4ZHeUqqTFNflPY7tmrvu693iZEsxQ_c5v_L1LA_kXAFk8LrpCeMEyRM7ycREcYedic9tOYv-joUK9suMw0XbKZTpeT2JGN0rw1WhkCcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b92955f5.mp4?token=tPxbUvfBtwDSEGVtJqgkvm9mhLeGQ0h8PUlKgfc2TIT-8lddP_4kaUQAsV2XpmFC5SZCy7O0KCsSyN-XfKrjPU0mfEo4KNRysa8UJgPGZwdeUoTzsmYvGBdFHZpTzOX5mqBfZFHUiFwE4rs3aYOtYxlQzT0jzB1QXWKWvMia1eix3Qc1Tgxcl6Ua75LBudhcynF4nfb0uePwzk52DrGc7KXee820yDqV5FzMzPyyb_isq4ZHeUqqTFNflPY7tmrvu693iZEsxQ_c5v_L1LA_kXAFk8LrpCeMEyRM7ycREcYedic9tOYv-joUK9suMw0XbKZTpeT2JGN0rw1WhkCcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انرژی و سوخت؛ انرژی را درست مصرف کنیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676756" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676755">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1C-MXlLpJ259k3APo9gm0xL5vAOcO-m5F0yur2mAH10GZEBuwRXjna_bBfS3CV-2YMD-49npHjH0_c7dt5xEsQMjr1UQLFuB7See5ibogkuYfIHM8EB5-fmZBGNBBnhvbseX8um-6_hKINSk10Sfm0lUKxbhoTLDSs-bvvQGTp8U--jv3JSXzg1xkq0ODfp79A2cGOEoQgUgv203U5PPS1gcQPS8NbnO2EJiQMSuwRCilp3ICRcGkRJKqEwUyIvxVVc8LFGDBuA0YWduDNiVDM2-L-NLZNnQD_KL_yFFiNCpc4MnIHNORkjwp9JPyC_DG3UfjbEwabbYh2QGV9HQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور خود و اطرافیان را از اضطراب خبرهای جنگ در امان نگه داریم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/676755" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676754">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099ea6f44f.mp4?token=WX0cFnsj5w8CUCqzj9bZiePlVbUeDT6XxCemM1TUpiqMdxAcbQC2KYbLYfHvinYJq2uW_PrYeFSmGFM8maeR9lCghVSVwDwS1BjCxphZwHItNlPNeJbt0iAXgqtR_eI1bdIL7Y4LWJt_cd2zNfnazEbgNzdOgPkRy2j41bbRPSpc5q5AHmoDq99OUGjT5SECdMI2nZFb4-0qY1uryTipo0dLAgH19bvArjwowqX6t8_L8Ps40cRbhCcPVgPgfVyAnI-DfPEnHoXdcczIhIyzsXXHtAWfoITn5xAy98axyEInAGAbZbo1B_jBPx45xF3hWgHxFJM7IOX1cOfR1mdeng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099ea6f44f.mp4?token=WX0cFnsj5w8CUCqzj9bZiePlVbUeDT6XxCemM1TUpiqMdxAcbQC2KYbLYfHvinYJq2uW_PrYeFSmGFM8maeR9lCghVSVwDwS1BjCxphZwHItNlPNeJbt0iAXgqtR_eI1bdIL7Y4LWJt_cd2zNfnazEbgNzdOgPkRy2j41bbRPSpc5q5AHmoDq99OUGjT5SECdMI2nZFb4-0qY1uryTipo0dLAgH19bvArjwowqX6t8_L8Ps40cRbhCcPVgPgfVyAnI-DfPEnHoXdcczIhIyzsXXHtAWfoITn5xAy98axyEInAGAbZbo1B_jBPx45xF3hWgHxFJM7IOX1cOfR1mdeng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زمان درست حرکت، یعنی سفری آرام‌تر
🔹
در روزهای اربعین، انتخاب زمان مناسب برای حرکت می‌تواند از ساعت‌ها معطلی در مسیر و مرزها جلوگیری کند.
🔹
با مراجعه به صفحه ویژه اربعین در سامانه ۱۴۱، زمان‌های پیشنهادی سفر، آخرین وضعیت تردد و اطلاعیه‌های مرزی را بررسی کنید و با برنامه‌ریزی دقیق‌تر راهی سفر شوید.
🔹
برای اینکه زمان مناسب سفرت رو بدونی بیا ۱۴۱
🔗
141.ir/arbaeen
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676754" target="_blank">📅 20:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTrxhs3sXzM8pg-XJ0RN843tOUgbLW_I4B6Sy940lXixEAoMNl6R7n85Z2A0eoUvV9zdbG7B6jsfOghaOaz5GAjaZvYcsKa_mNa7ydoBvoGZIeIqhMMdWrjf-PGPnAt4oaRoCg4Orj1RYAx_sEl60seBr4TrrEov2pbiLjPkWEctqVqS5n4JmlEw5oqVDttQ5umXK8qBH-kxtzrP-fUdn0XtS09KqNa-Q_pfWZA4tS8EcTGcBT_NJ_FTfrmcc_ibUsHJEhUSPmgFGxx1BMERUkBAtiq6bYBNy1Tb2LLyqlP4YIp5Jkx5LJSC8L8_NPArau5_AklEH_vwthcPPKfqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/676753" target="_blank">📅 20:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnZ01Dwx-W9mjj3Ip9Wmb8WuYY6Y1mJDsB7WkekYtCnRmhg6U35DFeZUEYzuQuWvIy58zdSFcIm3aYUv1PKA5MdsoXyMv36PCsp-IQdbvm7T84rbpefQc5nTwrUd_e5BVXYQDyeIOvIcXQZ7k4AAqyI3j1IWlAqDoC1AKpd7laXVsLBXqt3TXPgRQW0LHvmi_4gUmhXelr5hAQRIRfgJeb2WPA1EgeV3UaMNtkGp-ZJP78r5wI9Lg0UtzJcnQb1zFxdVh7UovGV4HGS3jsj6JxEqAUpnW8rcLeKXxPQLYETaLsrGdE7lQrU_sRgbFuKYTyTN41cppFYOIkulv0Pecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgsYfh2U_Ji0A9kna4N68biwZD3syMHxCiBuC57diV3J6bYZuGA6-r-ecjo0Rw5nVXiQQQ0WBs48hZi7q9qXQIMI0YK_IGGrOJe7uNIYlaDbzgML9rSxyq-jF6Wj9NqrzAbyj1mbR2_ctKwavkC4iQ9eU2wBXFYIuhUAuYjDU9ADXhIeb7h3Z3aosUgD0y2dnWsfyqXWWeqm3-ho5nT_GiCFbqY7LByNa3gQrDFEexR_sgtRz_xMFetDWC_xCHsXFqOzDWrbkfMmwImjDNFomdld1u6jtBF51xjr0A6g938RobHy8FKPpmRUVGIJPUFQobaU2rI0slTkMZLRkqOGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCzdB9hBSrYv1ot4ftlloMWUM9nfCVhWDc1iJLz7EfXOQMx6vZY6b7_8y_2JooVAqIdwwclxk6-UQAHsBH1V9rc5s4g0Laq9b83tKxv0oz5uxNkye_RTDUyEmXKWfBSCtKxflOBgL1U3l4O9zWvaHwOk-diB94HK4MklC4r5mlumlaYiqI9dxtMJ1XZg4YU9yzTeBgjw3lMayfI_PREwhDJT3253yv03_EYWIJUvZDDzTNMTcRLFdNsankvGJmH9aK04sZw8vNu_xjRFM2Jr8bwsJpO-os2LwlEyHXq4-NnTvs_cwTjgI5G9yefouF-GLnqE7MbGWxUkc_zfwOgA2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شهادت ۳ ‌پاسدار استان زنجان در حمله موشکی آمریکا ‌  روابط عمومی سپاه انصارالمهدی(عج) استان زنجان: ‌
🔹
در حمله وحشیانه رژیم تروریستی آمریکای جنایتکار در ۸ مرداد ۱۴۰۵، ۳ تن از پاسداران سرافراز و غیور  سپاه انصارالمهدی(عج)استان زنجان به نام‌های  محمود ملاجباری،…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676750" target="_blank">📅 20:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWrfL9YsaFRwQFAYgdPJk44rUY0oHH9yuMS7UdJ2VAvB2xCtJe5ojyHCwc-ROQUMcJhPVyyCVg_-Ax10HQLaf4kAYgpbTwVj3uIDu3pMr5sYKG-NFpVQX9cFJvuLGaAbThLmAmICvYRMxjVo5kvEplwAKOKW5OQGSV2cH4Ell9Tggj9MdigxaGsUCigo99mA_jnc2XXJvn4c0i51O4CuIxoE4zxuPAV48YLQYsK26Z79ev6cAS7D_85VzkbrC706tTTRkkISXwe_cyXB_1JKTs7PJQNC8cqO8q8eJHMwtGvSST3-OmBDUgNPYfW1Wwpql3C8VY5ilPlxLa4yNFpj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbTtq6ADq4eV1FopQefJaSUWzay0j_lWymINFhwLJcOa7kqM06dRttWwJxFqXoy80pdCYnaqK1YBatYV9ll93PNVimIfUEZT5TjmH12dKMg_NxFw4x5sRgyaKLvJ3GfCQwrYaMGLOKQv3gwBOF8I8t0SDXr7Qa5dUjJH4Nf8GbdnG6jJvT29vG4Z2_3rXnUuN-Rp73Sio95Vrci_TbG-ylwlnMQYZsqLLC7WX3Bp0xOBkcmtxnbq_sgkMOKn96YUpI6cwwerQtVAKSXT7RMfk_4VAiI9oUBa95UrSMlqagqsbjmENdylew8wQJo8chN97_TKIwYGe0bTo7kyDmo0Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حس می‌کنی زندگی بی‌معنا شده؟ «انسان در جستجوی معنا» رو بخون
🔹
شاهکار ویکتور فرانکل، روایت واقعی مردی است که در دل اردوگاه‌های نازی فهمید حتی در سخت‌ترین شرایط هم می‌شود برای زندگی معنا پیدا کرد.
🔹
گاهی چیزی که ما را سرپا نگه می‌دارد، امید نیست؛معناست.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676748" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mev1mV6EGAHeBg2RX5sGDdIyAAFwK46Y_7dVFQPjB-3cCy1GyScGph_AVkYAGpXe7emTQLodunxtiZvaMjrEgjqkvTQ0CiW-kMo7XMnuF5I30lwaUtsBngXxKj-7V10imgvjoXtoiG-fJA5RsNSMj9rqzA4MAtG9FXhul2aFXQPR2WxixB3ZNpzIrvaXJmI1BOPrHm_N7ND4PaUJMiiAqy7B8Q6CRFMeyXB_9kgI4cDQAU4xSYTGAPTEYFkV9N_FO23lut9h8ERDVfBKmiPI7ohB9iSONGMLn3tULvFjVsuM0f4ekQZZs52yo5ev1BnqXIZTmOXLNoHkSOa-qdayfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/676747" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676744">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/676744" target="_blank">📅 20:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676743">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e79c675c.mp4?token=skTSd0asmUV932m4JOHnFktNfRI1AKsiFkjmCNsYhZNC5SUOD2pzhVtArferCd_BhxXKQU89k2J9tcwjI9oiJtPo6p_LOBafvz7MUZc3snESOG8n7e6dpYU-38ZP-u5xa17gKOwcDwh5mgw-Ttdxf3fGSh6KbkfR0IFPZ1CIpFWIUySCdaj0O0f-s_8xLPtsh-Zukq6otx_sUbyZIGPWLH_KNVhkTsy3Xw_OKpOd1iO3xD34Ern7_wjaGWIiD0du305NcjsC3dBPdgKjMphDHbjwK09rev_rmX6yNZJp0aPGrMW5rqBXSgb-5b2j-4iSsAJsWK33L9fYRXFFcdrQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e79c675c.mp4?token=skTSd0asmUV932m4JOHnFktNfRI1AKsiFkjmCNsYhZNC5SUOD2pzhVtArferCd_BhxXKQU89k2J9tcwjI9oiJtPo6p_LOBafvz7MUZc3snESOG8n7e6dpYU-38ZP-u5xa17gKOwcDwh5mgw-Ttdxf3fGSh6KbkfR0IFPZ1CIpFWIUySCdaj0O0f-s_8xLPtsh-Zukq6otx_sUbyZIGPWLH_KNVhkTsy3Xw_OKpOd1iO3xD34Ern7_wjaGWIiD0du305NcjsC3dBPdgKjMphDHbjwK09rev_rmX6yNZJp0aPGrMW5rqBXSgb-5b2j-4iSsAJsWK33L9fYRXFFcdrQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: من معتقدم اگر بتوانیم اندازه تهدید ایران را کاهش دهیم، به توافقات صلح زیادی دست خواهیم یافت #Demon
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676743" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676742">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676742" target="_blank">📅 19:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a79e0c68c.mp4?token=L_o4Ia5ucS93Xcu1emSdgkffyvCbjl0zPH4A9-8CmLo88x-fArdw7AKHa-Y0sdbcRVxMVJHKELZM7ONXW3UylJyb_ndg0dJPJAg-5fCCB4RJxAvSOrmjgG1Vov48nd62dyQU6opYj2heGk-lNZrgXP_t4y-flEUe0i4fYfoZ3VIAOrcXOWbiu02yjMHtSLy1Hk_fqaz2qJM1pob2re8Q_kAFOXPGTkzZjoh2WHef5eTVFFgNtbohZWqVE8U0K8BBAYEs7MKuTLZsocvXv24oSJdh1nwoJVBhr4VgLsdDVNYagilWUKr8jTn6HmsCvKKn8am9BeMtbY0Sx-XqaBv7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a79e0c68c.mp4?token=L_o4Ia5ucS93Xcu1emSdgkffyvCbjl0zPH4A9-8CmLo88x-fArdw7AKHa-Y0sdbcRVxMVJHKELZM7ONXW3UylJyb_ndg0dJPJAg-5fCCB4RJxAvSOrmjgG1Vov48nd62dyQU6opYj2heGk-lNZrgXP_t4y-flEUe0i4fYfoZ3VIAOrcXOWbiu02yjMHtSLy1Hk_fqaz2qJM1pob2re8Q_kAFOXPGTkzZjoh2WHef5eTVFFgNtbohZWqVE8U0K8BBAYEs7MKuTLZsocvXv24oSJdh1nwoJVBhr4VgLsdDVNYagilWUKr8jTn6HmsCvKKn8am9BeMtbY0Sx-XqaBv7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: من معتقدم اگر بتوانیم اندازه تهدید ایران را کاهش دهیم، به توافقات صلح زیادی دست خواهیم یافت
#Demon
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/676741" target="_blank">📅 19:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533dd4a054.mp4?token=aTCp-HEq9yrn5gDS6K4g-ZvlTMVCU8JjQQvxXF4jc0UFnizdkq31lN9SQgHDayt4Whd0GTETvBvCbdIUzBnqt9rlEfq6j6H49SgirD9Hh4rEahBCsZl5vGD9m1ryw5EPH9BeYhjudntWIG_fXc_2D344XDwdZ9NIXC0a4dDTjqkOmg1mTRTq4ZWhgR8s0PyOpevip_VxaFsg9pYSieFpqSGtGu-Xcb_F6MmyJgZ13xv_p_Pxc8tfubNpUYvAxa4oAH2KuPNYBLDYWJsQQuS2AHVpinFCaazX1ogKODu535ZIryO0AETVL_cDtWJmd7DLOmmigbel3ZTbvunlN4Bt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533dd4a054.mp4?token=aTCp-HEq9yrn5gDS6K4g-ZvlTMVCU8JjQQvxXF4jc0UFnizdkq31lN9SQgHDayt4Whd0GTETvBvCbdIUzBnqt9rlEfq6j6H49SgirD9Hh4rEahBCsZl5vGD9m1ryw5EPH9BeYhjudntWIG_fXc_2D344XDwdZ9NIXC0a4dDTjqkOmg1mTRTq4ZWhgR8s0PyOpevip_VxaFsg9pYSieFpqSGtGu-Xcb_F6MmyJgZ13xv_p_Pxc8tfubNpUYvAxa4oAH2KuPNYBLDYWJsQQuS2AHVpinFCaazX1ogKODu535ZIryO0AETVL_cDtWJmd7DLOmmigbel3ZTbvunlN4Bt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین «فریاد مرگ بر آمریکا» همزمان با تشییع شهدای اربعین در حرم حضرت ابوالفضل(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676740" target="_blank">📅 19:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: هدف بزرگ دشمن تغییر نقشه خاورمیانه و ایجاد اسرائیل بزرگ است
🔹
طرح اسرائیل خطری برای کل امت اسلامی بدون هیچ استثنایی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/676739" target="_blank">📅 19:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رایزنی وزاری خارجه عربستان و پاکستان در خصوص تحولات تنگه باب‌المندب
🔹
محمد اسحاق دار، وزیر خارجه پاکستان، در تماس تلفنی با فیصل بن فرحان، وزیر خارجه عربستان سعودی، تازه‌ترین تحولات منطقه‌ای و بین‌المللی را بررسی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/676738" target="_blank">📅 19:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار کارشناس طلا: به پیش‌بینی‌های آینده‌ بازار طلا تکیه نکنید
عبدالله محمدولی، کارشناس طلا و عضو هیئت مدیره اتحادیه طلا و جواهر و نقره در
#گفتگو
با خبرفوری:
🔹
افزایش اخیر قیمت طلا ناشی از تحولات سیاسی و نظامی است و ارتباطی با باورهایی مانند ۱۳ صفر ندارد. به دلیل نوسانات شدید، معاملات طلا کاهش یافته و کارشناسان توصیه می‌کنند مردم به پیش‌بینی‌ها تکیه نکنند و بر اساس نیاز خود برای خرید یا فروش تصمیم بگیرند.
🔹
همزمان بخشی از سرمایه‌گذاران به بازار نقره روی آورده‌اند؛ بازاری که پس از رشد تا ۱۰۰ دلار، دوباره به حدود ۶۰ دلار کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676736" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf6b5a81c.mp4?token=XTAu0Yw4rKGhr7uUtgl_SYClp5k-JPv7Rul3jbBu_aNolH1i9xYisnzbTqKEiF263KrwlgBkey9UBE_2pIs5lkhQklCmvHn42ZalX7uqFJ7o_SlWAjIpPxHQvu05E7ehol2Wfn2Et-4oQOzMV5mbso1r2hTdWluRZILpvtPRh-mzZkW_gcLeYtsXs4PFMVtN1K3JLqFDpRCE1ZAdhoEAZIuyBENOv3eMQW5iMZUwwUZRTJLXm7nsKKWguUeNgfOPt41EeLTIHD_6zd3NnRlC10LMUP_ESHYY4h_kkIRyPTvH1ZpWnuYdM_NOyamVCW_m63nrqTQ-hHeSGEZt8RmUHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf6b5a81c.mp4?token=XTAu0Yw4rKGhr7uUtgl_SYClp5k-JPv7Rul3jbBu_aNolH1i9xYisnzbTqKEiF263KrwlgBkey9UBE_2pIs5lkhQklCmvHn42ZalX7uqFJ7o_SlWAjIpPxHQvu05E7ehol2Wfn2Et-4oQOzMV5mbso1r2hTdWluRZILpvtPRh-mzZkW_gcLeYtsXs4PFMVtN1K3JLqFDpRCE1ZAdhoEAZIuyBENOv3eMQW5iMZUwwUZRTJLXm7nsKKWguUeNgfOPt41EeLTIHD_6zd3NnRlC10LMUP_ESHYY4h_kkIRyPTvH1ZpWnuYdM_NOyamVCW_m63nrqTQ-hHeSGEZt8RmUHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو آشیانۀ پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676735" target="_blank">📅 19:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پنجره متفاوتی به دسته عزاداری کاروان اهالی هنر و رسانه در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676734" target="_blank">📅 19:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMEMC58ctI_CP7sm7-XAQpUurfBS0FgKbaQaY6sxZFUhYhv30KF3bCOd-pcWg8aQ0CvZQO1rG3OnJlSxYaMHHOBhfZDf0lU9hvsPxy-lF5opJRs8livesk0thATMypxRIGslm8sZY81wqsVgq8J4_M30Tsf0Pmf60HeA5F488LsP131GgKC1QWunP9o2Myi_33dLR4DG9ov9ejQxwMhLo8A1wgDs3pgYzplCRpefN7Tu90V_o35p-Fum4mzdd0ajEkISod9LhVl8XipBIm-2GdMnb9CSz3_M-bK8mBeJaWg95Xt_ESTnBvp8n9YtcseYrPLxPMs7_j_7qXGpI6UzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از مردم جهان در یک قاره متولد می‌شوند!
🔹
اگر تولد هر انسان را یک رویداد تصادفی در جهان فرض کنیم، بیشترین شانس تولد مربوط به آسیا و کمترین آن متعلق به اقیانوسیه است.
🔹
از هر ۱۰۰ نوزادی که در جهان متولد می‌شوند، حدود ۵۰ نفر در آسیا، ۳۵ نفر در آفریقا و کمتر از ۱ نفر در اقیانوسیه به دنیا می‌آیند.
@amarfact</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/676733" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcIqCpew5SOZZ0gPsO0tVUG3u2HopgVW_ARoc9x1Io9b0mZf6PAYeginFuh4D6K3t-okbmmQhjz5OPmiUUEpPnbKVIkCtfs4XysOTbSKDBnrnVn9YHTHLpyZCcbP16eju6G2R8ZTLlf5xZjZldd4R1DniUDs3uGDkHr3WWNrxztHot_bqgqIY9EV9uDfwa_Epbg7B_RmjKjUoHfDq95XI6hBsqTVvIDjbvuvkRNk1OEMevh7GxMxQdYO2w2wqErjRLQyZquNBa4mJ3ngDcSHr3eVcnrdT72nxXdHICqtwrgT3Kzq-gNnu84VrkPT6w3vbPWf3ZQcUO4kP88chdo-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت بنزین در روسیه وخیم شد
🔹
فایننشال‌تایمز گزارش داد ۴۵ درصد از ظرفیت پالایشی روسیه پس از حملات اوکراین از دست رفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/676732" target="_blank">📅 19:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6jw300BLbLbaPZfKR-ZKf4fT0O8LUFHqrrDZMdozaHvIHyRm3vEeOtH-LhsD3AtPfmfDTKQ9lFqj3cf4FGMG5i53soEhTa4af9B7UJZtq0okbVk_jbuHXoadoCKJUL4Y3AT7mFdadPHaEtBMGEGSOy8XjfnheYSHmcVNA2T98WBsNcZaqRRwR5Xz1VtmbJR0VTbLN_b8n8dLoNcips15Y4DTO8QtTDsyjXYuulbP-D5BDzbrjH4_HyyGw4csSGdRqcbqZZMLTv6emRTLM-Q9ncxj372nBJ8wbnSiaKqZzdlEnyFSZKt0dAtVsTcVNLwOvClag2sAgy6lzAipAes2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مناطق مسکونی در شهرک طیبه در جنوب لبنان توسط اشغالگران صهیونیست
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/676731" target="_blank">📅 19:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d477085e1c.mp4?token=EY4LpOz_ex7OQFh9kRDljU8ztaL8F22vdYQ3OYv2a8rGp3OFySH743mNvbkAYy9vZ2t3jy2mrhKj9MR0vlPRNEbWVSxHMqgniny9cVXzXS26wMcA-cGJs2V2Ye3jkKTHq5eBpitTVq893rlbLL8LtVsehvFy8vBznjWQO-RePh2LswU0s3_pAWeKkmO1s3SAwCFhMfHKzl_zzyDvzXvLR0otLwGFgtG2FsM3dtJ423F5BLEF_eu3rWS5Eop6AcpS7oTHzlP4r-TFG7K_rZ00QM94N84n0DKwcWXAMosyCTAlVRXBUSjIP1Nc4W59SY-3A7_09eTQ0YMr0lqC8lPzKJ4OPhjtUu3hT5_bB04hPyygNfiWK3do643NR6GhXshgb1Iy-NaElEJseMwFBnOsxlXFnuGzhISc6PJepIF1mdyS-nWvEFJl2vjDqqECcpwQBrdOm5DlgAzMkBbDdI_vuG7IBUz2Qtla2vAlcZvy4aAx3KUVXl7ehOr2izggvVYGs7D499JhbaOH9b6eJk4Ax53fo4M2fkTGWG1CZ-j-R6txU9a6tt6LKNjWNHu0GupgbojXkprGs5PKi6MAjsN7ZEDt6-eEiiXhHDZjs_5-uJs0AGdb4Ka9LrE_zyyro-i0zQCvGhGKLyop-O7EWOjPoqxqDNehnsH34H1h5zJnhz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d477085e1c.mp4?token=EY4LpOz_ex7OQFh9kRDljU8ztaL8F22vdYQ3OYv2a8rGp3OFySH743mNvbkAYy9vZ2t3jy2mrhKj9MR0vlPRNEbWVSxHMqgniny9cVXzXS26wMcA-cGJs2V2Ye3jkKTHq5eBpitTVq893rlbLL8LtVsehvFy8vBznjWQO-RePh2LswU0s3_pAWeKkmO1s3SAwCFhMfHKzl_zzyDvzXvLR0otLwGFgtG2FsM3dtJ423F5BLEF_eu3rWS5Eop6AcpS7oTHzlP4r-TFG7K_rZ00QM94N84n0DKwcWXAMosyCTAlVRXBUSjIP1Nc4W59SY-3A7_09eTQ0YMr0lqC8lPzKJ4OPhjtUu3hT5_bB04hPyygNfiWK3do643NR6GhXshgb1Iy-NaElEJseMwFBnOsxlXFnuGzhISc6PJepIF1mdyS-nWvEFJl2vjDqqECcpwQBrdOm5DlgAzMkBbDdI_vuG7IBUz2Qtla2vAlcZvy4aAx3KUVXl7ehOr2izggvVYGs7D499JhbaOH9b6eJk4Ax53fo4M2fkTGWG1CZ-j-R6txU9a6tt6LKNjWNHu0GupgbojXkprGs5PKi6MAjsN7ZEDt6-eEiiXhHDZjs_5-uJs0AGdb4Ka9LrE_zyyro-i0zQCvGhGKLyop-O7EWOjPoqxqDNehnsH34H1h5zJnhz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه قشم: مظلوم‌ترین و محروم‌ترین محله قشم که کاملا غیرنظامی بوده، مورد حمله آمریکا قرار گرفته است
/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/676730" target="_blank">📅 19:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4z2xUK-tNwlOkgQFDRzsEnX4t1y-al4zpwQgCa9mVSsfZYUTdADOg83032naQrLE9Rg-AO99w1iiMdqeYM0JYEgJcFjzTaG8RC2HYSHR-zc5Q07tHH8XHviYE15W0oXTXAxUISGRy4WaCqRImyxop9HAiZZKN2yy0dcD5DAceyzuFl4zeSUZSW2E69oNAQteNYM3U4uQ_YMMN0zAYC1hYA1GEIkrYfRrvppe4rln7dBfqUSTkZjScTtma5EbVdrY59m1cG3Qre-lRv56vl2cl92th6_qCY_YoGVK3-XOVjzQB8B1Z3eycytIG_Av3QhAa0jbLsoBy8ZqJnvTsr4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: حوثی‌های یمن از عراق به عربستان حمله کردند
ادعای رویترز:
🔹
دو مقام در منطقه گفتند که بر اساس ارزیابی‌های عربستان‌ و شرکای منطقه‌ای، حوثی‌های یمن از خاک عراق و با هماهنگی گروه‌های مسلح عراقی به عربستان حمله کردند.
🔹
این ارزیابی‌ها که با روایت‌های رسمی متفاوت است، نشان می‌دهد که اعضای به اصطلاح محور مقاومت ایران، روابط و توانایی خود را برای آسیب رساندن به متحدان امریکا در منطقه تعمیق بخشیده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/676729" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سنای آمریکا و بازگشت قطعنامه پایان درگیری با ایران
🔹
سنای آمریکا امروز بار دیگر بررسی نسخه جدیدی از قطعنامه «اختیارات جنگی» را در دستور کار قرار داد که هدف آن الزام رئیس‌جمهور به توقف درگیری‌ها با ایران، بدون تایید رسمی کنگره است.
🔹
این قطعنامه پیش از این به دلیل عدم دستیابی به اکثریت آرا، چندین بار در صحن سنا شکست خورده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/676728" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjNVLOYrJ98WjrpWEbxIjOw8kCGJ9PvMi4HcQgytmTS2FOn20Sgn3BTKGsvGY4Eu4f0WM-nDFbGcVFr8h00eRljik8jNhPcDGGdaHZyjy-q2t7uZsH8XgEoiHBsIgiqnXA3dBi2d8U68Ze_BI2CcX3s2oyIli4WDqKNShKEcbB5Wp9dyQiP5zDygIAebJ6CL9RdI0PpkggUs1r2Tfx77LfXEsVaJhr-r2WTDaoRcsOYBZrytCPeG02f0fDmFcINhcbzvVC-vpHT_mtBPa0rj9LVluU0Nw8WxR9SQEwt7UrrNUDCbw6okeEUUWiMJ0n1-ghe8ZOSd3U_TcsJdkHIuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAx6lhzEcGCDi3ksl8wRk4d1aHLxmSAbmscmfx9-e6aqIQREms-IIdDdhohY2V2HGlzzISqQZWBgqm62bxTuepqYQ6KIYDDl9i04UpsCQ_bQTaufBUsU6qPqBqecpmufTdJ5PoonQmNd8FN1v__pzUf-6b5TJJxpW-IWlDYEgyPLzRTj7hmaArK0jAteqqjOT1jBPiP_RFOpNPg9nkn0lL6EFx9fWzKt5ci06S-AZ1bTZwbs6GhjB1xHs992e0_JP0I4JL2LkFX34TCR43DIQ4SQ_hW0foIpOqdtsQKiZ5iBffvbgfiMPAh3ZdspFRxYtU0HlhPOohsCGH-YEGEhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nor33ch7T3clXFpoqa1i1AUP5caP4MKM6q3Yu00YkrkEueUaBjBN99FQ7hj0T0fHECidgr8Mvn7OBNurbPuSqSdjaeX7BuWsR47BT13ROLTwpqf6JFV_nSX3zivCYF4sfEvEifaUG41-JZhU2HWf3xN1lQ9pPzrLDr2_eFWkoLRsY2KEWA59iGZgM-RpSiWCUyqFpy7eeZvWDn7hBvgmDKbtsFL7C1oVt2CHJpI6O72tJOSUHEX33B_PgIWO0_8KJQqxl4zVvN1Tv6oIMDgpoCCOH2-9QLtDo8D_Xdyaw67xeD-UcA-M1zvzRYv_GQ086lv49xTOLbFpuA3lHewarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggvwSkJgTrKxJQYg0CeiG-9TF0-rFtK8_MOInEGwaP6Djs-ju6cl4Dw8lIIVRXLxQtGWUDA7eQ41snl4yFEZzaXH1awgp5SeEgdO_EWFSd5ccGUEeXrKufGkVmPGEJZGXdDgJeYPdlrE5fjA8k5hDNc_46YlxeRmyRV2Epmr9VFgLzYngOYc56SjxKS4PuiGDUmlu8MmN4K32vjP5tLNYTbogoLUlEI2wL4fOIHv_AcmGHT8wqmRkjPsUxgat2y7lCVqe7LHfkacIK-h-OYbDtZcNYhhV62EuPL2zO6t_TJv4aOiM_ZOoVc-KlqSqERTSxyQ1EUPGlMI0QztRO-SEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تشییع شهدای حمله تروریستی آمریکایی - سعودی به عراق در کربلای معلی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/676724" target="_blank">📅 19:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676723">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شبیه‌سازی ترور ترامپ در آمریکا که مورد توجه کاربران فضای مجازی قرار گرفت
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/676723" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8CPW1h-Duxc9cQTA_Lokq635cDUZ4aZbZ3vVbdnEs9Ujqp1gGVpXJy7Wc46FB3Dg-o_H06ki2iehc8YmAuonrV_FYLNioIiYJ8iJRGZ2WcgMFH3goE1GrfmzAPs2ezn0SqKJQFgt6TV29EaUmjjkz3LSSRJh5booV9bKOpOB1zhdkpyHbA1OzpokHuUnKypoKo3iCEz1M2ZddUvCeEa8xDIxVOEFcPPHjxDLRVEdDR1Tysd0He3X65f3kasxXBQEqXVH3NIIrGPhW5Ik6wuhefg-VYi4HBOAq_K-m8EJDHStGNQtOXA_cvMDzKYHJsi7O8ZgqOUM_-986Muc0otSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ققنوس؛ پرنده‌ی نامیرایی که از خاکسترِ خود متولد می‌شود
🔹
در اسطوره‌های کهن، «ققنوس» پرنده‌ای یگانه، بی‌همتا و بسیار زیبارو با منقاری طولانی است که سوراخ‌های متعددی دارد. او جفتی ندارد و نغمه‌هایی که از نای خود می‌نوازد، زیباترین و حزن‌انگیزترین آوای جهان…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/676722" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc2c7b75.mp4?token=Y5MHxaepTs6hZI9VjAG7SQsZc_BgsgYkAzBSVki9jtIjf5TKyWSVvYkBNojkZRvO0iCyU5qQAQObucA6twYkV7qr4cBMIbRb156kZERCZPCXyuOotdb3n85UTGNXTOOLxgalaV2GLQDhORyOVQIesdHpqX2SgObIuFAIUaf1TGYLLBKVinw79lJpaxH11i0g1OvRHMw3IZd6M0KMHxJlGK-45gH3naPeeW9oEfr9l2ykE5aKCtmmmvWnNlRLMYZZki6_HOu4e8wk08cwhcbc4oyrycPua0KaK6dYjGLyn6LjhkG5agPg9wsvQPT6-OpObq_qL5ckF_k0oPxRQ0I60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc2c7b75.mp4?token=Y5MHxaepTs6hZI9VjAG7SQsZc_BgsgYkAzBSVki9jtIjf5TKyWSVvYkBNojkZRvO0iCyU5qQAQObucA6twYkV7qr4cBMIbRb156kZERCZPCXyuOotdb3n85UTGNXTOOLxgalaV2GLQDhORyOVQIesdHpqX2SgObIuFAIUaf1TGYLLBKVinw79lJpaxH11i0g1OvRHMw3IZd6M0KMHxJlGK-45gH3naPeeW9oEfr9l2ykE5aKCtmmmvWnNlRLMYZZki6_HOu4e8wk08cwhcbc4oyrycPua0KaK6dYjGLyn6LjhkG5agPg9wsvQPT6-OpObq_qL5ckF_k0oPxRQ0I60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی به صنعا تکذیب شد
🔹
برخی منابع یمنی اعلام کردند خبر حمله هوایی عربستان به صنعا صحت ندارد و صداهای منتشرشده در واقع ناشی از رعد و برق بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/676721" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676720">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان رسانه‌ای خبرفوری در مسیر کربلا
🔹
کاروان رسانه‌ای خبرفوری روز گذشته وارد نجف اشرف شد و پس از زیارت بارگاه نورانی امیرالمؤمنین (ع) پیاده‌روی خود را در مسیر نجف به کربلا آغاز کرد.
🔹
اعضای این کاروان این روزها همگام با میلیون‌ها زائر، در مسیر عاشقی قدم برمی‌دارند…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/676720" target="_blank">📅 19:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676719">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbb8c9ef5.mp4?token=VBWaw4m70XL2lNsBt2t9DWDkwEM3Aomrst4ER8_sk3FRJd9OLCkLjdTTdE4TmvvOygilYPXneRTEXp3hprkmxhBKCOkYBmMGBEhQG886uZwpUbblrd9vw_-BfCZCtGeXzQqCkvOMq4mY9-6aogV6SybEh0VxLUz19Z8u0fvPWRnMbqHuJAYWbh_uaKWgHuSo-4hXpvMARwmDcIZTXzKvL1ltNd0H997RAOihoODJIEod6-753vLIdWZz4IWMZLaKOJIlfNMY229HWBNhEwlFB9K-a_Kel6PR-5SuDKbZyNGclFi79udi8keexJp_ImHxK68NvT7j5-dn23vzLanhQF0rxhQ65QpjgA6te0JQ851QcyHFITod9i3mMsWMVvD4Rhkn5NlLDGUzZf2CV_ykINGQZdx2cBppPKNDtEfy3aVXfUX9zwI2ZxrZziZ4ghK97xcjyaP8dv9lmOpbBbOFuJE-qSYc8nhNStn33uiy2rqS5oZrPOura8AZBQKmwykghr0GhyA6QSKZokXVaJKtjdyxeBUYkD-HMQ5-oa4lIiQGbcYeKZkUH8Ch3WuNLE2NxNT1Ff5ZfhMlwMelVuX4FSm22A_8pT8tk34pbHa-lbjXJtNPcFIt9xtrZqYWXh8zaEVaWvvnPAcYo7064MBNnyGE6HUnQTDaWGGf8YLPGm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbb8c9ef5.mp4?token=VBWaw4m70XL2lNsBt2t9DWDkwEM3Aomrst4ER8_sk3FRJd9OLCkLjdTTdE4TmvvOygilYPXneRTEXp3hprkmxhBKCOkYBmMGBEhQG886uZwpUbblrd9vw_-BfCZCtGeXzQqCkvOMq4mY9-6aogV6SybEh0VxLUz19Z8u0fvPWRnMbqHuJAYWbh_uaKWgHuSo-4hXpvMARwmDcIZTXzKvL1ltNd0H997RAOihoODJIEod6-753vLIdWZz4IWMZLaKOJIlfNMY229HWBNhEwlFB9K-a_Kel6PR-5SuDKbZyNGclFi79udi8keexJp_ImHxK68NvT7j5-dn23vzLanhQF0rxhQ65QpjgA6te0JQ851QcyHFITod9i3mMsWMVvD4Rhkn5NlLDGUzZf2CV_ykINGQZdx2cBppPKNDtEfy3aVXfUX9zwI2ZxrZziZ4ghK97xcjyaP8dv9lmOpbBbOFuJE-qSYc8nhNStn33uiy2rqS5oZrPOura8AZBQKmwykghr0GhyA6QSKZokXVaJKtjdyxeBUYkD-HMQ5-oa4lIiQGbcYeKZkUH8Ch3WuNLE2NxNT1Ff5ZfhMlwMelVuX4FSm22A_8pT8tk34pbHa-lbjXJtNPcFIt9xtrZqYWXh8zaEVaWvvnPAcYo7064MBNnyGE6HUnQTDaWGGf8YLPGm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/676719" target="_blank">📅 18:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676718">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUrue6hcV8KbG2a1VFQypNhmb9XDWwSswr-KDjew8WJEcUH483wCZrK9TG8D3Kk4o9Trc39K2pNlHRUGn-73Nj5ryqUQv3BeRleRdOOGY6qdPzET2tsn8KjGKSjOaFB1gvRMiu1AQzLLxCLEBsmRLBit7PzWHok8FdxR3yfQXHwKGZaWr03Oo2JrJ4CLtU710Cgp-hkb0F7vzFzTnO0JJN3p8TY9WSlOfj2eXE6L5yYaa04q2zYY6n9rCBhD-HsAHfsMuoZElJaTtLy9KScVlsACarPm7eOZM8TdN6JeqrpCTX2Rw-r3Q9yvDcF0p1ChQ8dXHXt_WhhlLjlzSIl67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی به گوترش: چرا نام آمریکا و اسرائیل را نمی‌برید؟
🔹
سخنگوی وزارت خارجه در واکنش به اظهارات دبیرکل سازمان ملل، از او پرسید چرا با وجود هشدار درباره نقض حقوق بین‌الملل، از نام بردن از آمریکا و اسرائیل به‌عنوان عوامل اصلی این وضعیت خودداری می‌کند و خواستار ایفای مسئولیت سازمان ملل شد.
🔹
آنتونیو گوترش، دبیرکل سازمان ملل متحد (۲۳ ژوئیه ۲۰۲۶): ما شاهد بی‌اعتنایی نگران‌کننده‌ای به حقوق بین‌الملل هستیم؛ مصونیت از مجازات در حال گسترش است؛ نقض‌ها بی‌پاسخ می‌مانند و هر نقضی که بدون پاسخ بماند، به سابقه‌ای برای نقض بعدی تبدیل می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/676718" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676717">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در صنعاء، پایتخت یمن/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/676717" target="_blank">📅 18:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676716">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در صنعاء
،
پایتخت
یمن/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676716" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
♦️
رهبر انصارالله یمن: عربستان همدست آمریکا، اسرائیل و انگلیس است و در راستای اهداف صهیونیستی در منطقه فعالیت می‌کند
🔹
انگلیسی‌ها و سعودی‌ها قبلاً تلاش‌هایی برای اشغال یمن انجام دادند، اما به دلیل مقاومت مردم عزیز ما در برابر توطئه‌هایشان، شکست خوردند.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676715" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4de5c727.mp4?token=agIGVlocWVBUWf2UD7SZ6_ydXRcEaSJScijmTtpL9SxGIrtS4gBxpRNlWxKkJMLD4cxufXFcyTeOI2g7CveKxjQpCwFjLTKeB5RJRuVUAUng9oqCzKqNkEPEepVjHTXnPyx_eOpe0kh840MiIqMCGaKnKkBdrTHBl84iCR1ug_oGmaQ-ft1ZapXEm73jZbMKmlMNu11UHgaIxaErDbdw0SGjdhQB2G-7NdnRgFZOlLl-h64ujSdPCrjdJQ_fZ2RMvhFuzQHfllBR6ykJctP7w6cN9I8MJJR8wW6_C3Slahv7TCV7fJuxXe5P4XOZN-KCWhohfT-RsXYXryyjk27v_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4de5c727.mp4?token=agIGVlocWVBUWf2UD7SZ6_ydXRcEaSJScijmTtpL9SxGIrtS4gBxpRNlWxKkJMLD4cxufXFcyTeOI2g7CveKxjQpCwFjLTKeB5RJRuVUAUng9oqCzKqNkEPEepVjHTXnPyx_eOpe0kh840MiIqMCGaKnKkBdrTHBl84iCR1ug_oGmaQ-ft1ZapXEm73jZbMKmlMNu11UHgaIxaErDbdw0SGjdhQB2G-7NdnRgFZOlLl-h64ujSdPCrjdJQ_fZ2RMvhFuzQHfllBR6ykJctP7w6cN9I8MJJR8wW6_C3Slahv7TCV7fJuxXe5P4XOZN-KCWhohfT-RsXYXryyjk27v_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: اشغالگران صهیونیست مناطقی از جنوب لبنان را به‌طور گسترده ویران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676714" target="_blank">📅 18:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حوادث پرتوی
🔹
هنگام حوادث پرتویی کجا باید برویم؟
در صورت بروز حادثه پرتوی در منطقه‌ی شما، باید فوری به داخل ساختمان بروید.
صرفه نظر از مکانی که در آن هستید، اقدام ایمن آن است که:
🔹
به داخل ساختمان بروید، در ساختمان بمانید، گوش به زنگ باشید.
همه‌ی درها و پنجره‌ها را ببندید.
🔹
به زیرزمین یا وسط خانه بروید. مواد رادیو اکتیو روی قسمت بیرونی ساختمان می‌نشیند؛ پس بهترین کار این است که تا حد ممکن از دیوارها و سقف ساختمان دور شوید.
🔹
پنکه‌ها، هواکش‌ها و دستگاه‌های تهویه‌ که هوای بیرون را به داخل ساختمان می‌آورند خاموش کنید.
🔹
دودکش‌ها و دریچه شومینه را مسدود کنید.
🔹
حیوانات خانگی و لوزم مورد نیاز‌شان را به داخل ساختمان بیاورید.
🔹
منتظر دستورالعمل‌های جدید ستادهای بحران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676713" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب حمله در ایرانشهر؛ دود سیاه ناشی از آتش‌سوزی دپوی سوخت بود
🔹
در پی آتش‌سوزی یک دپوی سوخت در محله غریب‌آباد ایرانشهر، ادعای وقوع حمله و انفجار تکذیب شد.
🔹
علت حادثه هنوز مشخص نیست و تاکنون گزارشی از تلفات یا مصدومیت منتشر نشده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676712" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676710">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
روسیه ممنوعیت صادرات بنزین را تا ۲۰۲۷ تمدید کرد
🔹
کابینه روسیه اعلام کرد ممنوعیت صادرات بنزین تا پایان ژانویه ۲۰۲۷ تمدید شده و صادرات سوخت کشتی، دیزل و گازوئیل نیز تا ۱ سپتامبر ۲۰۲۶ ممنوع است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/676710" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676709">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک مامور در درگیری با سارقان مسلح شادگان به شهادت رسید.
🔹
مهلت ثبت‌نام آزمون‌های علوم پزشکی تا ۲۰ شهریور تمدید شد.
🔹
معاون رئیس شورای امنیت روسیه: جنگ اوکراین قطعاً با پیروزی روسیه به پایان خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676709" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676708">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-U5LfKb0GVfNYNyWEFIvuvgk4ySaqxuanW-FUEUpNwMi5rYh_GDI7QEvVxd3mwy8N1JXVbfTM-h6bMkEmC2WCKhbzrzYrHi9Z15Pri8KWVgrYYMSjqAiKvpW32loX__taCy8vwdtBS6eoM9GNhksuoW-qrv4tiUSs61juarddJ7ynyH-fLTQ-CuVBCS5al01cCYx5MuJ-mPlJSSH6BSOftfDU-4a3TpTFiZKKctCZoyy5N9GnWt81uD5PkQAyG34fZvNwHdj4dgcspv8d92RUpXig0odmKYS0lYQiXkt-HqtK_HF3-_hDxaRGrJGzcB3M1GhSA6v6x5uUtu9jLV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوبارو صابونی؛ تاکسی نوستالژیک سال‌های دور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676708" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676707">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DguXsuo_JdYFk7lK7Yer0wmfDsiLPByLjT6APRIKUsz8YrvdgP7TV4Q1YS7KPVLYesSwM7f47qC3_0HhQ1LXcWkjxJP-bYpyEcOjYk__DNbCtsoFlh-GuRbaGSxHkPH5hskeIjFv1jgXC8uN78R8Ys3lq1LXQPpNnenXSjjI1iln9chfdi56BwCTh5uQPcRtQ7A3Z7_BMa5wCm0CN4Rht6RX2WLhnKB532vsqJtjfKAsLeyLbmCeQjalB70VI7sLQPLWb6-YTIDjpffXxNyusv8dWwJ9D_2f6Dibh-GhRLghItosHPs2tOdY0G8A6zLWvni_r_HShufH-Hi1otT17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مناطق مسکونی در شهرک طیبه در جنوب لبنان توسط اشغالگران صهیونیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/676707" target="_blank">📅 17:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSK8liriGlJqfyXjwvPujchmpHHvaYnYf_DGQmJ4aHmS133GJdkWNAx49Gshc93iY_ccfGg-W9P7pN4Uc-M9gyMIuEZncYS-Z65jB6uzzz-7q_gzz1GeO1CzGe8BUxC2s23_zTLyIco-oEk3689GQ5thmsR7NUdmFgvSLmqN14gpCn_OBDNTASVAi73FJ2s3KLQFX8r-Q3Omv75G9Gt7gOp82gc76xLvvyabf2nUXJVjcOE7oTwtijrXR7JvvKgNWQYdPQ9XlzyJiBLwVxyCUJgMs3FcbJFQnT-1QpNh1-IPg4dkiGfO7y17-BNgW9EzP4c4ROpEPCQ-_9-wEuhMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2VELCc0LHQBVG-nhYA1jiQb85bABknAhUW1hNzMLfNk3pw0QbW4UUniWRDcwRP6zQ9tEJ3CpWT5e1m2fPk-LFtqs9aDz5pM94XEKo9iirU7fm7VqnnxUCjrXzm1acu8E-D5NqqoHJYbTCBwxhaih9UyEM-E7e25cLDbqncVqETI6ZFkbzItKqBtDkX8ivOuEqEu_jW43W8x-rl1r_ACXmmbFZsRjfPEKCVGIYi0zvNpASnLhjOwlZSdlJ-qOg-b39bp6vqATQVOoqybljyNTAyFO1t_HSmQ5qHQWfnKdui508Kpzk3SyX9P58VmnyTuIIrCnIlQY0o5VVZQZPa9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMT-b-JPaRm6XfhBG9vvaTPAiTt_hBTYrbCOx-rUBVzFgtH1-5TeSk2OEKsFvislKBEnntpaXdsjAHYxi8Z25g5xlwk7vw4uL_OIqnTZncpFQMMQCPb_V6YRcn_HlBt0W866uwK1CS60WVXl6fDq8aMgxnV_e7lF1qFTEhPokw2-KBKeTAjeIGWxQLtNQHgkUTdzKoxAmt9da9c1fM0twDzCqJaAFglkte3MUwve3WOP9lKdpSuxyHUd6FekL88CYDXMmbxExR0PlmUQcNBSamdPJajwizzpcHO16gilNmIY0f8ACKmNk6JSJWY0axnyJ5zEDgoKWEEEq72LrYdLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5Qe-4jgbak-RCplF5sGRDLbVNlR-MPouicg37EiRJiZRTA-M0pXw4Cn30NSEcGqo5nL7vLIm9_-XpMDQp10okQwwoiYEhC-7jE428nqJs5ZVaWnl0ACyHz9P71_6M_32CVaQQ7bCC7n1_XwDvhBKUg_o_jdOFddjrFmkypRXP3i2PHYQSmukDTMpiu1M1V_WJCGv5QZODNlXiQG5_G9l_8DC6Vt8bCWigMrq4kUFkUkuwH579Ug-TDbYehmUyPlVyBm5EM79YQdMeM2JhZJWofLTFHrE9GodFQar8PdwvnRPTCC8mZOaMLMIffvjjMq5zzQJiFzHX3UYd_LwT90hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده، می‌توان از هدررفت آب جلوگیری کرد و به حفظ منابع آبی کشور کمک کرد.
🔸
بستن شیر آب هنگام مسواک زدن
🔸
کوتاه‌تر کردن زمان استحمام
🔸
رفع سریع نشتی شیرهای آب
🔸
استفاده از یک ظرف آب برای شستن میوه و سبزی
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/676703" target="_blank">📅 17:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676701">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b70a4d890.mp4?token=sON-VG3thSoL6C4Je5y_gPUnCsY3FwXpJph-hc1LlsKRt4zFzH9PSfqgINpvR6dWql9eHMNHpN_9wz7CiuyBYo9PrO2kbS1-g7kf6n-2rMdfZ_KH_hCrF-5ioxylp96ghqOrq4LzVhsCb7PcoQlSr6Txhg-2V6bcpl-aFvmXB-tSR_dPgckgyaKxdE7u7f2j8uywmojjW71wvLibKEb0QmErZjo6D5Y_LzgJ35LTlswS68yqcBrXQppcbV4IK3qhqWKkpCHF_xcZlwOApOx3Te8zEgIoCHDeYtcXPqDL_tP7Q5tu_L6JzTGypIx006K-9qju3GKuUEx1JdGrft0Ryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b70a4d890.mp4?token=sON-VG3thSoL6C4Je5y_gPUnCsY3FwXpJph-hc1LlsKRt4zFzH9PSfqgINpvR6dWql9eHMNHpN_9wz7CiuyBYo9PrO2kbS1-g7kf6n-2rMdfZ_KH_hCrF-5ioxylp96ghqOrq4LzVhsCb7PcoQlSr6Txhg-2V6bcpl-aFvmXB-tSR_dPgckgyaKxdE7u7f2j8uywmojjW71wvLibKEb0QmErZjo6D5Y_LzgJ35LTlswS68yqcBrXQppcbV4IK3qhqWKkpCHF_xcZlwOApOx3Te8zEgIoCHDeYtcXPqDL_tP7Q5tu_L6JzTGypIx006K-9qju3GKuUEx1JdGrft0Ryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنسن هوانگ: دوست دارم تقریباً در همه پروژه‌های ایلان ماسک مشارکت کنم
مدیرعامل انویدیا:
🔹
این شرکت سرمایه‌گذار xAI است و دپست‌ دارد در اغلب پروژه‌های ایلان ماسک مشارکت کند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676701" target="_blank">📅 17:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676700">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از جنایت شب گذشته ترامپ در قشم/ حضور در خانه‌ای که شب گذشته در قشم هدف حمله موشکی آمریکا قرار گرفت/برخی از اهالی که خانه‌هایشان تخریب شده در سفر کربلا هستند
/ خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/676700" target="_blank">📅 17:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676699">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZYaKK0EqbDd-sMdYkoIaa1NghTKXLRRuQGxm_xKA4pulmewUOP-eHyzkzJf6LX-5vkapeJ5zeL_bwJDjgLI-hY20qSiPIJswc5UFbVS3fVPLvpe9SJLL5QuOUR61otdRK2ITtCdfPhLjpxMaheCSneMO7q092_a1rQv-hc9GNKU8HkZssMs2jkUoPFmfCK_Y2KfMq4tHB-dv2vnZsMMGZifjQB75Rh2W0X-5k9y7pTFh3iqEhsf7LtTWVQjFBfF32HLlJtaBl-NLDHcaCWbMI8ThWfnAag5ip5PrNsuybWv_GvA5CFkEHErX545TgaD-0eadtJCvQkIw8ukg0qP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام یک از موشک های ایرانی می توانند به خاک اوکراین برسند؟
🔹
بر اساس گزارش‌ پایگاه «دیفنس اکسپرس» و تحلیل‌ های نظامی غربی، ایران حداقل پنج نوع موشک بالستیک میان‌برد در اختیار دارد که از خاک خود می‌ تواند اهدافی در اوکراین را پوشش دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234300</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676699" target="_blank">📅 17:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676698">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: با ملت و مقاومت عراق همبسته‌ایم
🔹
سید عبدالملک الحوثی در پی «تجاوز آمریکایی-سعودی» به عراق ابراز همدردی و تسلیت کرد، این اقدام را محکوم دانست و بر همبستگی کامل با ملت، نهادهای امنیتی و مجاهدان عراقی تأکید کرد.
🌍
تازه‌ترین خبرهای ایران…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/676698" target="_blank">📅 17:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676697">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAMQzpKg7p3s_IAYK6mzTj_gWcnAaUQM54mdFk4nKftuf9lNCcp_q9BoNX8QLE5ddCQEuei_tkPdFfyobIsN-5w10IsQRpKyhsBYfuWJlNJLRCaI49o34dvH_XbJ7QLQP9q3o9Sdk1fqXaQ2bcAS41Trz_UVQU-Wisq-JgFz1-5hTKC1vyebtSl35FWgs6GsDDZw0holiYcQt090ZrQUWeTi7ELo-cT9FSQyN69_vtFpYIgdDoGIBufJm8VHCVN3O3_COAw7e01YpUGD-ZZvxlg9ErVntm3epV21FjlhOZvuYlVi6GqIk2oPoG6HMySo8eedELFNWN0fYNtd5Ts-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنبور جواهر؛ شکارچی که سوسک‌ها را «زامبی» می‌کند
🔹
گونه‌ای از زنبورها به نام «زنبور جواهر» با تزریق مواد شیمیایی به دستگاه عصبی سوسک، قدرت تصمیم‌گیری و مقاومت را از او می‌گیرد.
🔹
این زنبور سپس سوسکِ مسخ‌شده را به لانه می‌برد تا لاروهایش از آن تغذیه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676697" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آمریکا: به فشار حداکثری علیه ایران ادامه می‌دهیم
🔹
سخنگوی وزارت امور خارجه آمریکا در مصاحبه با فاکس نیوز: ما به ادامه سیاست فشار حداکثری خود علیه ایران متعهد هستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/676694" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشگاه و حوادث دی ماه/ اساتیدِ زیرپتو، در حوادث دی‌ ماه سکوت کردند اما در خفا درگیر کمپین افزایش حقوق بودند!
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
https://aparat.com/v/ocrv3ab
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/676693" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رهبر انصارالله: هدف دشمنان، تغییر چهره خاورمیانه و ساخت «اسرائیل بزرگ» است  سید عبدالملک الحوثی:
🔹
تجاوزات علیه ایران، لبنان و فلسطین در راستای حذف موانع طرح صهیونیستی در منطقه انجام می‌شود. وی همچنین هشدار داد نشانه‌های خطرناکی از آمادگی دشمن صهیونیستی…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/676692" target="_blank">📅 16:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رهبر انصارالله: هدف دشمنان، تغییر چهره خاورمیانه و ساخت «اسرائیل بزرگ» است
سید عبدالملک الحوثی:
🔹
تجاوزات علیه ایران، لبنان و فلسطین در راستای حذف موانع طرح صهیونیستی در منطقه انجام می‌شود. وی همچنین هشدار داد نشانه‌های خطرناکی از آمادگی دشمن صهیونیستی برای اجرای عملیات تخریبی در بخش‌هایی از مسجدالاقصی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676691" target="_blank">📅 16:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od9iw8AqwF7QJ-6JemH7ZIQyC2joJ7KsMW_yvX0b4BLk-HMldpVJV3yq2WZpdOPTAqRduWJ5Z_oP6oSOxrEePKvR0i_g1dI4SK25ojok5ylVrjjs5Oy1Xx0_V58tOLqa04nT17MdSkuB2XMrWxOO6ShLKjnFzzYb8acg4QpfpNr2IgWjeRzAjdCBa5ng5bvH_JdWkjjt3R9eXLxMlzBZlRcJm6QMBK395gesUuPwLynyEkDZJ_q79mh4RlBt4aFnCKnyCllQoNhvdtRse2jVi1CeSRdYVr0W6K50xWA1ql-ri7MxpQY9TkUKmvB5nBfGSLAQvnZQ_41zNWfoGGg6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۰.۳۲ دلار کاهش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/676690" target="_blank">📅 16:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7b788314.mp4?token=M4xsDNUTrLqiTr1DTdTbi_VTpZ3qPFfqBS_Vo01jJ4xycEA_cm1HzuQGz1aC0FM8rPYtAWucNBalg3-zKScwQo7h5SVgLpr07mWETYhiEyfeKFk4apc8mTw17_eiP7pDhZmTyQQ93u51irTY0CIZXKCV4wi4y8gvy-A-ijz5-i07Q1j5vjpDKowB_v6kVDB_ppcXH8bBqQ0Arkg8V_KIvjTQ2AeBAlEz40i_bwvWD-rNcVKZEjgLKGf-q2bSBHJRFwrbF3dQa2HyjzHTzCneQ_qF83VnC0n5wgWoWouUasVaJorAc75aaXyQaXZlI9NOi5ypzZFZm_YF0Kv-NUn7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7b788314.mp4?token=M4xsDNUTrLqiTr1DTdTbi_VTpZ3qPFfqBS_Vo01jJ4xycEA_cm1HzuQGz1aC0FM8rPYtAWucNBalg3-zKScwQo7h5SVgLpr07mWETYhiEyfeKFk4apc8mTw17_eiP7pDhZmTyQQ93u51irTY0CIZXKCV4wi4y8gvy-A-ijz5-i07Q1j5vjpDKowB_v6kVDB_ppcXH8bBqQ0Arkg8V_KIvjTQ2AeBAlEz40i_bwvWD-rNcVKZEjgLKGf-q2bSBHJRFwrbF3dQa2HyjzHTzCneQ_qF83VnC0n5wgWoWouUasVaJorAc75aaXyQaXZlI9NOi5ypzZFZm_YF0Kv-NUn7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۶: دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676689" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
راز نگهداری خودرو بعد از باران؛ نکاتی که بیشتر راننده‌ها نمی‌دانند
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/676688" target="_blank">📅 16:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQgRg1SYZW403jMK67uXC5ZP1hvPTh9D04jG6liM94AMbrfnjtBZZ0cv_agmoKYjHPT6tPMnaX8Qy05B6hnkXVwPSMZWmD1mb6pBmk5_TnhXJZJpGWT-Cp6kfVPcnWWgQKkG8MFwcMgZSpgqSoo_EBKG6BPU5WFevAQdKGQjP4_qlh-znP40ujLb7xblA8Mf63p0rxdorhSr0IhstMPIXnFBAPCbZOvNUd8WXbmecB7jJOiwkboki1AcO7SsZiAyjdP8iNNl0OKF5AMeUI8x-hnh82-rwO_Y2Qo18iT5n00o_pFxiewoqlFDwd02AtutUb-3lvEQDcdzjFUl9jAcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ضربات پهپادی موشکی عملیات نصر ۲ در کویت و اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676687" target="_blank">📅 16:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر آخر الزمانی از آتش سوزی جنگل‌ها در یونان
🔹
در پی آتش‌سوزی جنگلی در جزیره کرت یونان، صدها گردشگر از مناطق مرکزی و نواحی توریستی تخلیه شدند؛ شدت باد نیز باعث گسترش سریع شعله‌ها به سمت اقامتگاه‌ها و مراکز تفریحی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/676686" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/676685" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۶: دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی از منطقه را مطالبه می نمائید.
🔹
همگام با شما، فرزندانتان در نیروی هوافضا و نیروی زمینی سپاه پاسداران انقلاب اسلامی در میدان، نبرد با دشمن متجاوز را با قدرت و شجاعت ادامه می دهند.
🔹
صبح امروز در ادامه عملیات نصر ۲ و تنبیه متجاوز با حمله به پایگاه هوایی آمریکا در علی السالم، دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی را به آتش کشیده و منهدم کردند.
🔹
مردم مسلمان کویت بدانند، تنبیه متجاوز تا پایان دادن به غارت ثروت‌ها و منابع ملی مسلمانان و اخراج اشغالگران و غارتگران آمریکایی از منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/676684" target="_blank">📅 16:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETljda1B2iC6Iwi0FvUcAon03eAWtUxHpNpQuaUl4Bt-myItVps7pFssMvaaPtW3o_1nNUFweS3Xi2TPcfsVnL6nIVgik2XU-sDCxzgK67b8WBzoVlPhoz2MfQxUGEY0hi4OGHQBMzjyH2lGbtvf7wZ-_MViAJmuKl3kJpPh0rpVH0j4onWBi2M3rUaeNAXbu_IGdQtfJFek0fE16FBmfKcwnVEQB_W50CclWRF4E5Y1GAuLR1GKqwDnZbNGyFVyyqHpNZ4a_Dm67UjfMZcY7ctEv_2y5u7ckA_eJDzAD50TIJYtmWKk5HDmzn-PzMLs9SISxbFgLqVgb-k-WYfUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBLrZUP8BTTj6NOSQgIu8X0H5qk7rf0QLpSYmBW_IBlUwbQXsMW7KUhRVBDKl07HHjWIPWIq_nG5nRXS-6LWsEJGx-m1m9olvTTW23OuvM3nSDbXKh5KUcATZMtyQIZOj91ER6XchGTdnD_wyHMRdsUbSIpkSNt6XC-_MrmbcDJMQ0_OumV85nRCg6nASt-5x0H4nPapKhkzcubE8b8I3ig2naqYddx5DkdMBMKCpAfSIbtupT-HQpUnpAFOeJkoPBUHH6pfUuyzhOSaKgqyqfvsxKIwAuh6RqnY51t5y82bZvxUonFe8FDsoOton7RdSNTzuoUdyMQ2iG8cyl3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaieIU5chDfnwieFYCpZnW7s4F16MPvAWU_2XqZGahzepplEa--9i26W-VNo_unRFlnDRXqvHsng0Ve6gZrsIig4s3zDvvu3VZhUoD2WiYA4BmVuLrJI8PuPWIPcxvCAVQm8fj4E5CUti4AYjMxVlDM_oopxloxOKympsuIg8gc0COpVzKz4ZXrVangkzg4xX1BR_QNHvffCZpTS3rfO3imKxkjUiZSIlCtllY07uyu9w17LxcEzFJ_DCmlaYJB8HEJtKK4UqmnZjDH-yF8AT-ksi4lI4TQzMapNObPrWv4L-14Qh3NEfk7UQq4YNaCknLk86WT44DAF6orGJ5l68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jH48vkXBCmHX0HqgUSNwJiodJuxvswIGz1IwTlWFkPzDSN4pp0lX3ZQM8sZnQV6p_yxvgSS8Ejj50n8VQgcOZa6RkXNNNXKZ1ynbM1DUIiobza9aHnePQHEUphTMM0uAeBeDUgjY4hWsFHOBeh-cVhhcdEFV91KgGyzoZW0sljQb-jjioejvgeWWAqf3jl97J6S5cPfkFTwFfzM01eMmOUEprficPaOGxI0OAO7hwTChHPFH0UDGjF91mi7ie4_pneYZ9sqDkTvT3ZwH-po11Wwohbk01DpyrYzm15EmMfNfs3fGZwybV3TBBsHRAs-iuKBFbat4ikhjlxMkuvGSBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر علاقمند به سرمایه‌گذاری روی سهام هستید، این ویدئو رو از دست ندید #دارایی_هوشمند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/676680" target="_blank">📅 16:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cef79cdb.mp4?token=NNU_VeMNC1zARNppLSge7f4ouGQO7D4puZW4hJuFFGAdyjDNfx9DEyihrhyjGUo_oZpFap4URD5ZfoJNgSiYQHw3sdCrRgSw-XgMocohWW1bLup926SgpDYvuclx4cq3NREjOHax9wu7OmfvWBh4Fk7shTqfYoSPdBlp6BiK9DgrEFnXoZD4u_CESPgLAcLowgJkEx6RyQpkbcu8aMlUTqp343qVtKsdSKek2sF9NPj8IlaYGvw8zCGGNgnEi8KYH3bLHuxZJAahB5L6_m73MCXOrsk6ILNqsMGiJuTyTOnkBIT5ztBFBf8U35uDdKNZUmojFu3ccm9WlEQTUgFaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cef79cdb.mp4?token=NNU_VeMNC1zARNppLSge7f4ouGQO7D4puZW4hJuFFGAdyjDNfx9DEyihrhyjGUo_oZpFap4URD5ZfoJNgSiYQHw3sdCrRgSw-XgMocohWW1bLup926SgpDYvuclx4cq3NREjOHax9wu7OmfvWBh4Fk7shTqfYoSPdBlp6BiK9DgrEFnXoZD4u_CESPgLAcLowgJkEx6RyQpkbcu8aMlUTqp343qVtKsdSKek2sF9NPj8IlaYGvw8zCGGNgnEi8KYH3bLHuxZJAahB5L6_m73MCXOrsk6ILNqsMGiJuTyTOnkBIT5ztBFBf8U35uDdKNZUmojFu3ccm9WlEQTUgFaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا %𝟖𝟎 تخفیف + هدیه
در مهمانی 𝟏𝟎 سالگی «چرم مَنطِـ»
𝟓𝟎% تخفیف کالای اول
𝟕𝟎% کالای دوم
𝟖𝟎% کالای سوم
🔥
➕
𝟑,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان
«هدیه اسنپ‌پی» فقط تا جمعه
آدرس شعب و سایت
👇🏻
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676679" target="_blank">📅 16:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a32a231.mp4?token=RKGEQssOo_EY32O8_kiaHW9WO8mhPH2Wev634154SiOEPC7dNuQFtDJnMdt7lYttctr-qpMbxb42LWtYeRZB0nZ9E4w19PxGmoha7FFAp9b_EhAHdtmqDL6txUA_iice_3jAK-KrId3sW3DIFEWvtGcucAJRlR34UEORwfuKWAqNwYCMSFP8TO5Wn1ston7AfwILTYVdeWA0y6hdKAHY5H_9QaPo3QEpWok8ZeAv6FfgEjY4qbpNyWSNLYWHy2UWxP7haZLPF_PzIV8n1xt9RD2hkxgDpjmrhgio3n0kGg0PMhHqf-OpE9mchT8W_xqvJKScY2YzIzwCnrrPEYmnn6J44gUh4aphrs2fuvEHYZ7GW4pO_vmQjpDNewX6yuR--tWIQF2XAPa68dbkZZ3fkQYZrIm4zrf-l38Z6UA5PuCglIW_G3lgKCfKoHArhsDwJA3K5alhqhrYL0V8EA5CQoEBdEoYVp1RRFX6Pdj32bUFv4h_HKC3z0P5EaRnyb3UM6eZQteNSEmrRGehSxLq64ryaqhwNl4kO-9LlwMA73JaFbCq_hvY13lPSOQ8D5kkL7q2BASDXQbKDr3norcKN5WxMIEixkr5Xk0jPROMgXhfRY-9ipa72q3rbO3YTk5MQvnw86C0XLME4evdyIutEuPGcuxZM4_3_504lS4Tt0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a32a231.mp4?token=RKGEQssOo_EY32O8_kiaHW9WO8mhPH2Wev634154SiOEPC7dNuQFtDJnMdt7lYttctr-qpMbxb42LWtYeRZB0nZ9E4w19PxGmoha7FFAp9b_EhAHdtmqDL6txUA_iice_3jAK-KrId3sW3DIFEWvtGcucAJRlR34UEORwfuKWAqNwYCMSFP8TO5Wn1ston7AfwILTYVdeWA0y6hdKAHY5H_9QaPo3QEpWok8ZeAv6FfgEjY4qbpNyWSNLYWHy2UWxP7haZLPF_PzIV8n1xt9RD2hkxgDpjmrhgio3n0kGg0PMhHqf-OpE9mchT8W_xqvJKScY2YzIzwCnrrPEYmnn6J44gUh4aphrs2fuvEHYZ7GW4pO_vmQjpDNewX6yuR--tWIQF2XAPa68dbkZZ3fkQYZrIm4zrf-l38Z6UA5PuCglIW_G3lgKCfKoHArhsDwJA3K5alhqhrYL0V8EA5CQoEBdEoYVp1RRFX6Pdj32bUFv4h_HKC3z0P5EaRnyb3UM6eZQteNSEmrRGehSxLq64ryaqhwNl4kO-9LlwMA73JaFbCq_hvY13lPSOQ8D5kkL7q2BASDXQbKDr3norcKN5WxMIEixkr5Xk0jPROMgXhfRY-9ipa72q3rbO3YTk5MQvnw86C0XLME4evdyIutEuPGcuxZM4_3_504lS4Tt0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند عالی برای گره زدن
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676678" target="_blank">📅 16:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
هشدار عراقچی به بلغارستان درباره استقرار هواپیماهای نظامی آمریکا در «بزمر»
🔹
عراقچی در تماس با وزیر خارجه بلغارستان، موافقت صوفیه با استقرار هواپیماهای نظامی آمریکا در پایگاه «بزمر» برای پشتیبانی عملیات را «محکوم و غیرقابل‌قبول» خواند و خواستار تجدیدنظر فوری شد؛ او با استناد به قطعنامه ۳۳۱۴ سازمان ملل، واگذاری قلمرو برای اقدام تجاوزکارانه را مصداق «تجاوز» دانست و هشدار داد هر طرفِ مشارکت‌کننده در حمله به ایران باید مسئولیت تبعات را بپذیرد.
🔹
وزیر خارجه بلغارستان گفت کشورش قصد مشارکت در جنگ ندارد و بر دیپلماسی و کاهش تنش تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/676677" target="_blank">📅 16:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455426b2fa.mp4?token=tqMYkbepA71k0nPhdrIuULObhrxkLdTAuA-WQEGHfHe6cx9nIOIh--FWUUVBqs2rIeY5dyZZuv55fVot66Stws8kpQ3mB3sb5YGrRSYZHlhKKJc3FVx346gzfmf8dD5-6JlejNUGXnVWzzSrqrjLx0M9D_DIS6t-vQlVHpoWn5KVJPb1OS7HxOVcx_iTAVpSe018f2I_XxrNF-5x5d7lT3qjqCwx9wZBooJdkBFFQOEMXq_72f_Y6r81ksPJpvGjGeI1LR3wd-JjP0MCHTNmVLskztY_yTEl-nP9C9xifnIBu5Pyd7TjrUqXKBDSrfD2S725XnbFpLCJhHeaF6VaBUnxd-QZs9dZs1sn8PjJMNDjytqAsRAe2e-QaPmkeNhxtQPWjoIPZTYIpeLMxwu3KB_vJr9wURiQ6mB9X1Lpdbogfgyu_luOXpv0M-exRTwh-L3bOfOm2xlCZugxLoJS2mpqoGqVxzG8npfi6LZlC-IFbkl_Tk98GskZB53L9OCGTytbu_Dhne6OzkoMCaWrVJTMnpdEb49tXbHymadSWGlLU8d9VPfqCh7rpuBQZB7-ANXrEXUAVXi56XcGHvp4hRX8t7b-aNAdz3uFSLavDZm7Lh0oYovV1IWCcgRgHo5M6v-TYtB9SYDs1_A-iiMH3CvqJziqAWXwxzeACF8QnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455426b2fa.mp4?token=tqMYkbepA71k0nPhdrIuULObhrxkLdTAuA-WQEGHfHe6cx9nIOIh--FWUUVBqs2rIeY5dyZZuv55fVot66Stws8kpQ3mB3sb5YGrRSYZHlhKKJc3FVx346gzfmf8dD5-6JlejNUGXnVWzzSrqrjLx0M9D_DIS6t-vQlVHpoWn5KVJPb1OS7HxOVcx_iTAVpSe018f2I_XxrNF-5x5d7lT3qjqCwx9wZBooJdkBFFQOEMXq_72f_Y6r81ksPJpvGjGeI1LR3wd-JjP0MCHTNmVLskztY_yTEl-nP9C9xifnIBu5Pyd7TjrUqXKBDSrfD2S725XnbFpLCJhHeaF6VaBUnxd-QZs9dZs1sn8PjJMNDjytqAsRAe2e-QaPmkeNhxtQPWjoIPZTYIpeLMxwu3KB_vJr9wURiQ6mB9X1Lpdbogfgyu_luOXpv0M-exRTwh-L3bOfOm2xlCZugxLoJS2mpqoGqVxzG8npfi6LZlC-IFbkl_Tk98GskZB53L9OCGTytbu_Dhne6OzkoMCaWrVJTMnpdEb49tXbHymadSWGlLU8d9VPfqCh7rpuBQZB7-ANXrEXUAVXi56XcGHvp4hRX8t7b-aNAdz3uFSLavDZm7Lh0oYovV1IWCcgRgHo5M6v-TYtB9SYDs1_A-iiMH3CvqJziqAWXwxzeACF8QnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر قطره آب مهم است
💧
🔹
شیر آب را بی‌دلیل باز نگذاریم و زمان استحمام را کوتاه کنیم. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676676" target="_blank">📅 16:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نشست اضطراری وزیر دفاع عربستان با ترامپ و ونس در کاخ سفید
🔹
وزیر دفاع عربستان در کاخ سفید با رئیس جمهور آمریکا و معاون اودرباره تحولات منطقه به ویژه تنش فعلی با ایران گفتگو کرد.
🔹
گفته شده خالد در دیدار حامل پیامی از سوی محمد بن سلمان، ولی عهد عربستان بود.…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676675" target="_blank">📅 16:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6179d2b13.mp4?token=KX43iOI6FIjh5TiV454bArSMtVvTw0CWL-hkZYVPqRwY-rvAv6RSftPe5lMyiYPr4TMFqnjNX2_gTb2g4tDd7M2JFGs_8XREEmLVU-gdMpp3sn8L_JaIkF8DRdVoXiaodukKfXoBpBuzQBCUhCURy8jozlEweKCb7zwqxbB7r7-U-gHjCDcKSF44dyjodDUat2ouFp6InvqZtC73EujHdAEot7sHvrm2g61IyoOK19ZpmRs7zQherwt7bGfiCPuQnd6vV_bZWNYDrWp8vpArtmuWyCb_7rpBpXErUP1LBX5-m5fEKpzoRuLUIUd61VEA0cGmwX7rlJfhDBiaoh9zgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6179d2b13.mp4?token=KX43iOI6FIjh5TiV454bArSMtVvTw0CWL-hkZYVPqRwY-rvAv6RSftPe5lMyiYPr4TMFqnjNX2_gTb2g4tDd7M2JFGs_8XREEmLVU-gdMpp3sn8L_JaIkF8DRdVoXiaodukKfXoBpBuzQBCUhCURy8jozlEweKCb7zwqxbB7r7-U-gHjCDcKSF44dyjodDUat2ouFp6InvqZtC73EujHdAEot7sHvrm2g61IyoOK19ZpmRs7zQherwt7bGfiCPuQnd6vV_bZWNYDrWp8vpArtmuWyCb_7rpBpXErUP1LBX5-m5fEKpzoRuLUIUd61VEA0cGmwX7rlJfhDBiaoh9zgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/676674" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مهارت برای آینده چیست؟</h4>
<ul>
<li>✓ هوش مصنوعی و کار با ابزارهای AI</li>
<li>✓ زبان انگلیسی</li>
<li>✓ برنامه‌نویسی</li>
<li>✓ مذاکره و مهارت‌های ارتباطی</li>
<li>✓ مدیریت مالی و سرمایه‌گذاری</li>
<li>✓ خلاقیت و تولید محتوا</li>
<li>✓ کارآفرینی و راه‌اندازی کسب‌وکار</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/676673" target="_blank">📅 15:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1gq08bVWL0XahT6yhTv6nJz_EbIZBZRoiJp19-Q0xRbIpKoYHEnGKhs_2oC-254h6L0THBI8fnp6BS8cOqRnqsPhMcD6hEcQSiATzro26xivQLqJZxl7hYzXLjagh6DMgovtXCwHOs7YLHIDU7buEYez6PmJZ2_n53BC3053aVSn5y98bCkp0tgOaI8M8CVgGqKXHpHeySkzp8LxpI3XMfqHTIKVL8RZmwRnXtyL8Hki3UhyMqIH-zsMt4V7SV8a7PFVocBV1svK9IZJxhqW0Md90zmYGvG9ty8qilgb-huRjJmnW1JkXs7MqFB746yQOufwapmDsOoqoi9AeXS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مدیریت تنگه هرمز واجب و ضروری است؟
🔹
از گلوگاه تنگه هرمز، علاوه بر نفت، حدود ۲۰٪ گاز طبیعی، ۳۰٪ کود شیمیایی و ۴۲٪ غلات جهان نیز عبور می‌کند.
🔹
اگر ایران می‌خواهد سایه جنگ را از سر خود دور کند و اقتصادی بادوام و بازدارنده بسازد، باید نقش خود را در مدیریت این گلوگاه تثبیت کند؛ چون هرمز هم ابزار قدرت است، هم می‌تواند برای اقتصاد ایران عایدی و جایگاه تازه ایجاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/676672" target="_blank">📅 15:51 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
