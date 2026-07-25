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
<img src="https://cdn4.telesco.pe/file/FHadioX0GrbajPg9EV7dJdGyH5-KIOqcUbiMhmHC9gRh-FTSQVeZpppE9G0ADWLYXehZKjpSzvcPxbKfmc3XtOCnSlFXsXfymYTJ9dE8Vw2B-x133CPALaBhHEZbuWXHUY4QMsAqDXPZ7EZrAgZMnmPotxeutskqHbQGtfORB7JQznGB9ny1NP2raqffJBLquzvqgFjt0WSN95jqPZm02TeGSQFvKv3vxPaPYHRoVxV26OT72x2qVakmigMh5tQHvbH2hLIvH_4-hGT2Cot9xAczd7v6_jJMi6tWyJ1jyvb-0dvXH8BNOo76MtUsNwEf4pj855Vg--OTEpVaqAn0gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 22:24:25</div>
<hr>

<div class="tg-post" id="msg-675258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای کویت: هیچ حمله‌ای به خاک ایران انجام نداده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/675258" target="_blank">📅 22:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn-2RKxEVW2uQmsCxOdRyIQ2V1gt2cIDMPBo_Mm8CyF2P0G2m8IsGOkOcW5kZNcZbdTW4mKLRerUEW16HeXWc6-miMYy92e0UQ4yu3tAZussKFVkULezlKkCVBjCO21CdymIyT18wt1Zp7owG7CrH8L0wyAs-6lDIEbaHuppykOq_dJFBkd1NrsrMjFYCpA6OaHGLE2RKj1a1QMSnckd9tIrAe_BGwJEIbcBkDGGK5t1LsJG2AQKiO-W7ZLIx_e2Q1Y5-E8yWYDvTv5qWRrVIV41XG8BmxGU0r_wi4k3ANxhW8As4c7Kkg-B1f7k-7FHhTOYG0WAlOlu_zeymSIh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKsEu-fnruufu9i9T0jg-NXad0K4YhJPotFt7u1iLp7xbijBtaYok8IleIixYsToROYf8f3K2W368wl759PNQSxXTQb4fvJ-SRO_sT046fIqFQ42v3aEpXkA5sawQ2VYcb0eBLlNRnHXshSyWJ29_Yny2JgxKxlfUhWA59CyGzoaAhCjMO1Qgvy1ffxmiOmMcShTUVoHIilq0qS--KbiiU48Ju29PexwbOkXL_62rCxZZh7knfVxSnfdsfbVX5f5ydvpKSSXxFwz1ag1ubbEJbgI6rK0twCUyCdb0DPD95ECLbpvGaXZpqB4aLjXT0OHFyzdAAxGfnS28okKH0_6tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان وابستگی کشورهای حاشیه خلیج فارس به آب‌شیرین‌کن
🔸
کشورهای حاشیه خلیج فارس بخش عمده آب آشامیدنی خود را از طریق آب‌شیرین‌کن‌ها تأمین می‌کنند.
🔹
در قطر، حدود ۹۹٪ آب آشامیدنی از طریق آب‌شیرین‌کن‌ها تولید می‌شود که بالاترین میزان وابستگی در میان کشورهای منطقه است.
🔸
در مجموع حدود ۴۰۰ واحد آب‌شیرین‌کن در کشورهای حاشیه خلیج فارس فعال است، اما تعداد تاسیسات بزرگ و اصلی در هر کشور محدود بوده و بخش عمده ظرفیت تولید آب شیرین را همین مجموعه‌ها بر عهده دارند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/675256" target="_blank">📅 22:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: امسال استخدام گسترده‌ای نخواهیم داشت
🔹
در استان‌هایی مانند تهران، شهرستان‌های تهران، اصفهان، مشهد و شیراز کمبود نیرو وجود دارد اما امسال برخلاف سال گذشته، جذب گستردۀ نیرو انجام نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/675255" target="_blank">📅 22:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رئیس کل دادگستری استان هرمزگان: مسیر تمامی تونل‌ها، پل‌ها و جاده‌های بمباران‌شده، ترمیم، بازگشایی و آسفالت شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/675254" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سخنگوی ارتش: تمام پایگاه‌های آمریکا و ضدانقلاب در اربیل عراق نابود شده است
🔹
دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد.
🔹
در جنگ جدید از پهپادهای نسل جدید علیه مواضع آمریکا استفاده می‌کنیم.
🔹
پهپادهای نسل جدید از آرش ۲ قدرتمندتر و مخرب تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/675253" target="_blank">📅 22:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
«اشک میناب» منتشر شد / تازه‌ترین تولید موسیقایی در سوگ فرشتگان دانش‌آموز
🔹
همزمان با تداوم آیین‌های تشییع و خاکسپاری شماری از پیکرهای مطهر دانش‌آموزان شهید میناب، بنیاد رودکی قطعه موسیقایی «اشک میناب» را به همراه نماهنگ این اثر منتشر کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/675252" target="_blank">📅 22:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فرمانده نیروی قدس سپاه: رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است
سردار اسماعیل قاآنی:
🔹
رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به‌حق و انسانی است.
🔹
عربستان باید از رفتارهای پرهزینه آمریکا عبرت گرفته و به محاصره ۳۸ میلیون مسلمان یمنی پایان دهد.
🔹
شایسته است عربستان به‌جای فشار بر یمن، توان خود را صرف حمایت از مردم مظلوم فلسطین و غزه کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/675251" target="_blank">📅 22:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای سگ زرد: اگر به ۱۰۰٪ خواسته‌هایمان نرسیم، به جنگ باز می‌گردیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/675250" target="_blank">📅 22:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تظاهرات گسترده در انگلیس در اعتراض به همکاری با آمریکا در جنگ با ایران
رسانه ITV:
🔹
معترضان خواستار توقف استفاده از پایگاه‌های نظامی انگلیس در جنگ آمریکا و ایران شدند.
🔹
معترضان ضدجنگ در مقابل دروازه‌های اصلی پایگاه هوایی نیروی هوایی سلطنتی در «رف فیرفورد» (RAF Fairford) تجمع کردند و از نخست‌وزیر، اندی برنهام، خواستند تا استفاده از پایگاه‌های نظامی انگلیس را در جنگ آمریکا با ایران متوقف کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675249" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW64CMA86goNged9MPIascjrbukF8aFaAD0Zu2YjRtPEKHZrt_w24DbVGS2epwFNUyex4e9he-ap4KiUaeHqIye0c-BQMALCwIY-qABOdxwohCvG9vfMFHQ535v7h-whNTX3Ub83i4El6doXM10uynd9DOct0dQnNKuDMcRLPK1QlQUC7tM-tQTDjfqIfnp3lxbQ5Fe-4Fw_x5ULp-BqTirVU0bhXyehsh28NUL8VY7R7rlVpgOdhfZk6lSkAIO2a5HAfl4uoUrMFFvJOxFuwUivx8jo-UsH8hggDvOUWzu9iFa6KCBGXOFZdHXTKkxquV9tB-C5OzT07vbjBggN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مام اسپری سورملینا
💥
هم خوش‌بو، هم ماندگار، هم راحت!
⭕️
داخل هر بسته ۲ تا مام اسپری هست و از نظر قیمت خیلی به‌صرفه‌ست.
✅
کامل بوی بد عرق رو از بین می‌بره
✅
بدون حساسیت و بدون لک روی لباس
✅
مناسب خانم‌ها و آقایان
✅
ماندگاری زیاد؛ فقط یک‌بار بعد از حمام استفاده کن
🟡
🔵
رایحه اسپرت و دلپذیر
🟢
ارسال رایگان + پرداخت درب منزل
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675248" target="_blank">📅 22:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RDes5ia53W0PmXt45IrsLoClsd7YcCIsldWX8ZQm7UImaIa8VyiSIT27j6I_V885knu8eihsSYhjASkCgRVgXi8eQL_pCaQMgEgBY2S_wl8iR5d-iJacEeoWqM1DE85dprYaZStcc4wRsI943mwrGK2KeGKOJaP3aQnxtAN_gPbJ5KgdFQiOPBk-E4a3mcijBKQz1fAmHJR_8ysBZURKfw6FReVnxBn_it9dS0DhNnnZqDU0iJIVE0jUoY3hDghOqv5FFOz03erHJRPBPDrlf3M0THZ_26OJFwfa6h6T_PRfm05QXh1gFhmsh3hHRTFy3acubw0-R4v2_1mBrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل لَتیدان؛ شاهکار مهندسی دوره صفوی و طولانی‌ترین پل تاریخی ایران در ۸۰ کیلومتری بندرعباس
🔹
این پل با ٢٣٣ دهانه و بيش از ١٠٠٠ متر طول، ۳ برابر سی‌وسه پل اصفهان است.
🔹
لاتیدان روی رودخانه سیلابی کر و با سرمايه يک بازرگان هرمزگانى مقيم هند ساخته شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675247" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOxhafBbJG0U1BrAxWa1lj2Lea43WJn4BcZeAkmXc5J4eseAXS9Ys3qKctNBpyv5bhg8fVMjZeTtxr3lO6reEjIWgGZK_K-faCwbGc1FHGMRt-yOKoHbfR_ij4UHrkRcjoysFJ7Q5TljtaRJMwYlbVzvS7t-XGan_HQgg99g4Wbe4X9hDY6Gfcjo3sU0YYB6y23c80FyeJT-7qOFzpd0o07R70CQ316DGjTMB9TM6IH1NgdeVa7IMivQ1tJUHRte_wUPwj8ProJg5UVduNbUCeQ_dtYJNINqrKUniRuaGn2R-NIFgjdAQaNPLrlQandy_xVcMZgL8gGxdSZYVMGxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
زیارت به نیابت رهبر شهید
◾️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲، شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675246" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عضو هئیت رئیسه فدراسیون فوتبال به پاداش ۱۴۰ میلیاردی قلعه‌نویی:
این پاداش‌‌ها نسبت به گذشته خیلی ناچیز است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/675245" target="_blank">📅 21:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsDtwx47MK03kSgm4UIJTrLkTLCH386yArQSYEbspyZinUsOukTrpod5IPW6SUjPfM9qI1gRoCH5MF3MO7E7bHeRPvSpzYUJ46HKe0c9me_eVoU5zwS-uoRG7SGoH9u1UPRqTmSdskZ7ujtfba3IVd0sxU9YxEmaJoXrrYMzsZ0BS3e4UcDhPRioIqNsx7HBqcacWzDsr3pxArk453x5eX6J_cGpDm8Aid04HNES13V1krYOvKh0jxTFIwHH-WvR0L9jKOs8WgJ5OWVkt0COBhifDYqqADnOGAnNAtOCL8WtI1vMQZ-HgG-_O5RriREoP7KlBmOfYzJCNDCtNYotlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زرشک سیاه؛ یک میوه، هزار خاصیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/675244" target="_blank">📅 21:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند
ادعای رسانه اسرائیلی وای‌نت:
🔹
قطر و عمان فشار قابل توجهی بر ایران وارد کردند تا موضع خود را نرم کرده و از آنچه به نظر می‌رسید یک عملیات تقریباً حتمی و بزرگ آمریکایی بود، جلوگیری کنند.
🔹
اسرائیل ارزیابی کرده بود که یک حمله بزرگ بین شب جمعه تا شنبه آغاز شود که این امر باعث آماده‌سازی‌های چشمگیری در اسرائیل شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/675243" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxOyZHAfvsssSZ-QN_2FjU0OSqZa330KZYWKUgeTihinN2GXS9OL0Hukz1Z0m6i9eUFDJdcoI8hqJmWigOnL1P5PV0KigUGNlpT5eaPDGhFT5gqNWZE1R9kWQIC-2MyV08ljX3dDnUJj0aiPz0VtPOrbU3kAQvGc4HArNJsyyCAhlrmKbQRzxeyu2zx9v5B_3f1A6TUQm9uEzRMf1ftvb2j07NGy16cklqJqqlV1DUuU55ZeWSuOAovFhPSqnESBS_1wUlK8jJIUUIsUETnZPbt3cagq2F4qmC5Tlqb63nYqniiubgee5bH7i67n2qgljCJzZ4OZZLbNRjovzfGTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
🔹
کیتی پری، خواننده پاپ، کاخ سفید را به خاطر استفاده بدون اجازه از آهنگ «Firework» در ویدئویی از حمله نظامی به ایران محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/675242" target="_blank">📅 21:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/675241" target="_blank">📅 21:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4729e529f1.mp4?token=WgAiARhiI-9wwITo-YfFJxaQDkpNaPK-knGNL5EfVOZS6YKuM8Qe6y3k_wWdMhWw9bEgbQ_p14du_MH4CKKKkDOb9uXQx5tbTA6cTmy5sKXVRNGFiBDC1gA7yfvlTmExnGybvqZIk5poUd2KXgpn2xt6I1VP8LteSO69BUqOEOoRE49PxUXfVsz_h8ODi11nqV8CTolno_2ZVUtLxJCbmcUFNFz6XTYhATDZBbToeo2gDGiHwxaUZ5vJjLM35XNnQMwicA84s_HegVPd_EQcixRlNmRIDuAeQr-cN3mj6FdgAdJlFKs25z7vsJEGQg2KQZ9EHzKhQB6Hst3CeMI7gH-hxN5SAns4EsXouW-jODchCSUjMoWP3G79lkflpFSUgxwhmHP_phIsTrKW4_Lp45v4Wq2Kgkbc1RGpnkudetpPEWMlhdXdB_APG3QSPGzr1rWcsSUnjnbNMpSvTQIw7oP7W1EIlgrYSRQOJNRcwfD1shXWJdj57bogBc4ugdWRJ-r8l9yBlVPOiMnytRmxZozkYg6xQOjmWglI2Q3X5qFYVpz-8Q6r0I-7sUEv5XzcWVgxSpNmyJ8L5_ItU-yidMSq9LlYenwDvxYoO6aNDMm6u2LdlTL0qSn3oz32nJtNwtZlMmJHjNjSaYzG70wfJrezRPWsyeGKfGYlCKH9jic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4729e529f1.mp4?token=WgAiARhiI-9wwITo-YfFJxaQDkpNaPK-knGNL5EfVOZS6YKuM8Qe6y3k_wWdMhWw9bEgbQ_p14du_MH4CKKKkDOb9uXQx5tbTA6cTmy5sKXVRNGFiBDC1gA7yfvlTmExnGybvqZIk5poUd2KXgpn2xt6I1VP8LteSO69BUqOEOoRE49PxUXfVsz_h8ODi11nqV8CTolno_2ZVUtLxJCbmcUFNFz6XTYhATDZBbToeo2gDGiHwxaUZ5vJjLM35XNnQMwicA84s_HegVPd_EQcixRlNmRIDuAeQr-cN3mj6FdgAdJlFKs25z7vsJEGQg2KQZ9EHzKhQB6Hst3CeMI7gH-hxN5SAns4EsXouW-jODchCSUjMoWP3G79lkflpFSUgxwhmHP_phIsTrKW4_Lp45v4Wq2Kgkbc1RGpnkudetpPEWMlhdXdB_APG3QSPGzr1rWcsSUnjnbNMpSvTQIw7oP7W1EIlgrYSRQOJNRcwfD1shXWJdj57bogBc4ugdWRJ-r8l9yBlVPOiMnytRmxZozkYg6xQOjmWglI2Q3X5qFYVpz-8Q6r0I-7sUEv5XzcWVgxSpNmyJ8L5_ItU-yidMSq9LlYenwDvxYoO6aNDMm6u2LdlTL0qSn3oz32nJtNwtZlMmJHjNjSaYzG70wfJrezRPWsyeGKfGYlCKH9jic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت چینی Unitree از سگ رباتیک As2-W رونمایی کرد؛ یک ربات کوچک (۲۵ کیلوگرمی) و بسیار قدرتمند که برای محیط‌های سخت و صخره‌ای طراحی شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/675240" target="_blank">📅 21:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: موشک خیبرشکن، اسب بارکش زرادخانه تهران است
وال‌استریت‌ژورنال:
🔹
سلاحی ارزان، متحرک و دقیق با برد حداقل ۹۰۰ مایل، ارزان، دقیق و کشنده است. اخیراً، ایران از آن در حملات پیچیده استفاده کرده و خود را به عنوان یک دشمن سازگار برای آمریکا ثابت کرده است.
🔹
به گفته مقامات آمریکایی، ایران از ترکیبی از مسیرهای پرواز، مانورها و سرعت‌های مختلف برای گیج کردن پدافندهای ایالات متحده استفاده می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675239" target="_blank">📅 21:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq5rGsEPUJxnzqM5NmcZk8p4KBi4YmK0Ue_7K0j9Z4Qsc_jCHp56BnpzRXWIiz8fc6QIh8OMbzA3F74sH3JzPuZMOc1l5DDHh5llxxuXaHtzcl7iSpcL1QK3NGH1OdVtG-QRyfUkpx0WhXDWixBAujePOPyN7BEjRC_KBwbfrrTCjDYx8cbatKOzsAEIHYuFHfBnYOBIsojXALQ7qi8ZIwpgPwveFAdxX5CmgAHjCbadptT7N17dhkIDICLQxkdysvePC1PxxKHr-iFC7L6a_pHoeDWHESFMzNx0il7IHLj_Rp6SLQ9tnBotAn_jmTOuDFzFI3-2z7V8616d_fbISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجارهای جدید در جنوب لبنان
🔹
رژیم صهیونیستی در ادامه تخریب زیرساخت‌های لبنان، ۲ انفجار دیگر را در شهرک «مرکبا» در جنوب لبنان رقم زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/675238" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57794715bd.mp4?token=FRhBen0j_cS-2iBrY2NWv-vL8NXMbOmD0zG522SIH4lKNv8rfkXNy2JY0Fe1emOj0dw3BrCgzA8Of0CDI5908a7hCmBAn9yk_jJWDKywtRFbjPA27gqDOhWepM-QmZ6Jce3IXwlsOBZtukltBNaFphuBiIpSY-_S3hUw3YqX8qsEqZ80XqCEOY8TYH2kth4VqGl_ZP08o-pqLUyuoHSOmu8HzpY3BX7K79GPYoyb_SNdwSQrqgiL6lYxSPRYnCEDDhsB_byhxLGro5pgXwxK3G4yZI1iqdjpJKCE0HxEZBn4b83a8H33V8ZWJOb6A04SCGyGIGXKm8toxq0qTrzonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57794715bd.mp4?token=FRhBen0j_cS-2iBrY2NWv-vL8NXMbOmD0zG522SIH4lKNv8rfkXNy2JY0Fe1emOj0dw3BrCgzA8Of0CDI5908a7hCmBAn9yk_jJWDKywtRFbjPA27gqDOhWepM-QmZ6Jce3IXwlsOBZtukltBNaFphuBiIpSY-_S3hUw3YqX8qsEqZ80XqCEOY8TYH2kth4VqGl_ZP08o-pqLUyuoHSOmu8HzpY3BX7K79GPYoyb_SNdwSQrqgiL6lYxSPRYnCEDDhsB_byhxLGro5pgXwxK3G4yZI1iqdjpJKCE0HxEZBn4b83a8H33V8ZWJOb6A04SCGyGIGXKm8toxq0qTrzonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مشایه همه به نیابت از آقای شهید ایران خدمت می‌کنند…
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/675237" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0c70e5af.mp4?token=IkWevTq7RygI5c-gZz_9uB9g8uZrBRcGvv5AU6gETqYoxT9-2yoqNng3wplI5y3bTt55U59JPqpTk4-fflEXjipT4JGRd4BVKx5nO2UjKnpaX_PWUyOFOLuYEsvCxcrlumaJcCTZ_mUWKxTD7xHq7W14JdQUJlfwwK5qjYvzMENKiqNAkImWY6nVt_8wL8YHGv-qYR6tR9v6m6y414_UsP0Eo01Rr-4_HrcVSqyD-ydBRIdIJN0HytKFzPNt_unLU2HtAA_MI53Sfr9cc4RPEMtOHGb9uAQBeXh2JI23PEMxEPTDguY2ivKddb1KCXjWewHv-KyJPmgEGpBPDXgUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0c70e5af.mp4?token=IkWevTq7RygI5c-gZz_9uB9g8uZrBRcGvv5AU6gETqYoxT9-2yoqNng3wplI5y3bTt55U59JPqpTk4-fflEXjipT4JGRd4BVKx5nO2UjKnpaX_PWUyOFOLuYEsvCxcrlumaJcCTZ_mUWKxTD7xHq7W14JdQUJlfwwK5qjYvzMENKiqNAkImWY6nVt_8wL8YHGv-qYR6tR9v6m6y414_UsP0Eo01Rr-4_HrcVSqyD-ydBRIdIJN0HytKFzPNt_unLU2HtAA_MI53Sfr9cc4RPEMtOHGb9uAQBeXh2JI23PEMxEPTDguY2ivKddb1KCXjWewHv-KyJPmgEGpBPDXgUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فهرست خسارات بسیار سنگین آمریکا در پی حملات ایران منتشر شد  سردار محبی سخنگوی سپاه پاسداران:  طی ۱۵ روز (از ۱۷ تیر تا ۳۱ تیر) آمار خسارات وارده به شرح زیر است
🔹
در حوزه راداری و پدافندی:  ۷ مرکز فرماندهی و کنترل  ۳ سامانه ارتباط ماهواره‌ای  ۶ رادار پدافندی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/675236" target="_blank">📅 21:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da6aa40f0.mp4?token=bZp6iNXysdbJUTBYANuDCZZtpM1cs8yFcHWBhJehU6xx-G9BvwHKh-1zkkLp0-UeFUFQvdCEjtohMqjOYbS1fQUMxH2UrreDjWCk-Lmj_pPjXkFhMekNXSaBCX5Sl8hhOmrBvTmL1EnMt1NC1qz36GObkes5Vm5adAiOD9NCiVeaX7B4BeRKPMkb_lgWutYKdi5HR8l7VbsoiHndb9NGz0PEvvUKaeUdXWl7Tyxc0MK9TJLXfRy4DfS2BUN-4MBpkVeUtO4vYjCC6QVR01LhDRl6OjupLBBUBLjbTox4lrf1998U8TYLN6-rRDMkDMQ6RmDy2TMNPpZHB7w8eKkk1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da6aa40f0.mp4?token=bZp6iNXysdbJUTBYANuDCZZtpM1cs8yFcHWBhJehU6xx-G9BvwHKh-1zkkLp0-UeFUFQvdCEjtohMqjOYbS1fQUMxH2UrreDjWCk-Lmj_pPjXkFhMekNXSaBCX5Sl8hhOmrBvTmL1EnMt1NC1qz36GObkes5Vm5adAiOD9NCiVeaX7B4BeRKPMkb_lgWutYKdi5HR8l7VbsoiHndb9NGz0PEvvUKaeUdXWl7Tyxc0MK9TJLXfRy4DfS2BUN-4MBpkVeUtO4vYjCC6QVR01LhDRl6OjupLBBUBLjbTox4lrf1998U8TYLN6-rRDMkDMQ6RmDy2TMNPpZHB7w8eKkk1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: شب‌های روشن
🔹
ژانر: درام، عاشقانه
🔹
خلاصه: اقتباسی درخشان از شاهکار داستایوفسکی به کارگردانی فرزاد مؤتمن؛ داستان استاد دانشگاهی تنها که در چهار شب، با دختری مرموز آشنا می‌شود و میان عشق، انتظار و حسرت، معنای تازه‌ای از زندگی را کشف می‌کند. با…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/675234" target="_blank">📅 21:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تیر تا ۳۱ تیر، نیروهای مسلح ایران ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردند.
🔹
همچنین ۱۷ پهپاد…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/675233" target="_blank">📅 20:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fd1feb15.mp4?token=UIpnX2AXzIcDb11hWzyHfbqBx06VidJJ5N6EopqQgrulQOtFUAdb5OW8aFC2Jrhn_4BVCYdvyDEJJkVCyTLQ5mXEbcBqD0Js5oxVkBIJ63EC4X8Zlc34RMCphoYO-hIpcnwdcG8BvtYm7hvSvyQfuassuLdxRP8dJ5amYagBZ0zCiB24alPg5Z3rV6TjcjwjTI1PREyh8EppSzofO5eTUeSfOX4S_tlP8QDXHTyQGSQ3tXniNAGraF_BAQBoD4NqlBPk-PA7NRMRC3cYFtCN2g_VNn__f5QWZ8imuEoqjN53RVas6vrFFMoFS1fULXL28gdlbEGQssIBWc9zKwmojA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fd1feb15.mp4?token=UIpnX2AXzIcDb11hWzyHfbqBx06VidJJ5N6EopqQgrulQOtFUAdb5OW8aFC2Jrhn_4BVCYdvyDEJJkVCyTLQ5mXEbcBqD0Js5oxVkBIJ63EC4X8Zlc34RMCphoYO-hIpcnwdcG8BvtYm7hvSvyQfuassuLdxRP8dJ5amYagBZ0zCiB24alPg5Z3rV6TjcjwjTI1PREyh8EppSzofO5eTUeSfOX4S_tlP8QDXHTyQGSQ3tXniNAGraF_BAQBoD4NqlBPk-PA7NRMRC3cYFtCN2g_VNn__f5QWZ8imuEoqjN53RVas6vrFFMoFS1fULXL28gdlbEGQssIBWc9zKwmojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارلینگ هالند در مراسم عروسی جیجو دوناروما با طبل نوازی به سبک جشن معروف نروژی‌ها، لحظات شادی را رقم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/675232" target="_blank">📅 20:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f68c4b9b6.mp4?token=BU3ZV0ku-OdgP5fQLMUQjYVgz300iWIcUBIwZadssHfS_AeR15mBDXTsge6T7tIBR_8VxXtN-UDxVev8O_xfW-wUINmG2uw-SMjH__KMKY5Fk22WwkyEIu0YTdZdCRwNymFWQpSSKy2eYuZxPH4q_rNu5cp7tfnYG3AF2pQZ39_i2kKizZUCDwf-jxIwiDr5ORULCMeBNCSL_F_twe4TF3wMWQgDJiMbMNpGiz5zMQl9Pblu-R-zxuouxSMrSgO8dHnnvb-0cvx1EmP8Sp82azUEe9QoTraIXafkQMgnzTnlufthuccMHPjNOfZbrkXRXz9owq3E_NrjmmHR301IlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f68c4b9b6.mp4?token=BU3ZV0ku-OdgP5fQLMUQjYVgz300iWIcUBIwZadssHfS_AeR15mBDXTsge6T7tIBR_8VxXtN-UDxVev8O_xfW-wUINmG2uw-SMjH__KMKY5Fk22WwkyEIu0YTdZdCRwNymFWQpSSKy2eYuZxPH4q_rNu5cp7tfnYG3AF2pQZ39_i2kKizZUCDwf-jxIwiDr5ORULCMeBNCSL_F_twe4TF3wMWQgDJiMbMNpGiz5zMQl9Pblu-R-zxuouxSMrSgO8dHnnvb-0cvx1EmP8Sp82azUEe9QoTraIXafkQMgnzTnlufthuccMHPjNOfZbrkXRXz9owq3E_NrjmmHR301IlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره مسعود ده‌نمکی از انتخاب اکبرعبدی در نقش روحانی فیلم رسوایی
🔹
کار به جایی رسید که رهبر شهید هم پیگیر این نقش بودند، اما مرحوم عبدی در آن درخشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675231" target="_blank">📅 20:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8910d6e24.mp4?token=FH6CA7c0gmEhTlBykMyNCeHGIxqMLpXLVlUzABMSBJJW2tLFpPjhR6fzK92AdHNjZcEt1l95sv8EnKPUMfHLraJHGnrzRAscZPL1nAKpIV7lHMwL-UiTndibILmg3GWFTFYFY2qFcy1vgbD-8a5Sw7FzGecAnm2gtyqr9VOqI4WJgNGq9KCMEiv7bwwD_gfDdSG4ulpH3kOZzilFAuBEGXyGC8JaU8gwIDaINFdfaOJtwyZM7lt0W7OsG_k7D5_-QuNg4sYfv50GSvkLBlUIP4uwNIo_-Af7xEKO71RSncecKFkyh7vTiL4xk4ALrSCh38ndfKx2w68oLPzIdAi5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8910d6e24.mp4?token=FH6CA7c0gmEhTlBykMyNCeHGIxqMLpXLVlUzABMSBJJW2tLFpPjhR6fzK92AdHNjZcEt1l95sv8EnKPUMfHLraJHGnrzRAscZPL1nAKpIV7lHMwL-UiTndibILmg3GWFTFYFY2qFcy1vgbD-8a5Sw7FzGecAnm2gtyqr9VOqI4WJgNGq9KCMEiv7bwwD_gfDdSG4ulpH3kOZzilFAuBEGXyGC8JaU8gwIDaINFdfaOJtwyZM7lt0W7OsG_k7D5_-QuNg4sYfv50GSvkLBlUIP4uwNIo_-Af7xEKO71RSncecKFkyh7vTiL4xk4ALrSCh38ndfKx2w68oLPzIdAi5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی از شلیک موشک از جنوب لبنان
🔹
منابع رسانه‌ای از شلیک موشک‌هایی از جنوب لبنان به مناطق پیشروی ارتش رژیم صهیونیستی در شهرک کفرتبنیت‌ خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/675230" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3NnBWSGTA7-iYIxWZGhgF-8xaKAHSAf3qUC331WplQNxPMMVbpy8H9HpAF_lkAiUVl-fwEo10lT0siBjO9b1ZjGLfnkEXasETlrMKXlTcBuuK8Jl29KjjPcAgU7BD68BTxNvU2eBIl1odUqB4GbImcKsCB-4xDstQq8JpBocRaFvL1yOOXK9iWN9ujUvVK1nWgNvA82Q8aF2qCpUbX_T6NXOAjjCRgXeeirOGD6KXziVsDDxCdKJMqbVKTop5RXld64LUz92hsnZytiqfFlNzqXUaGrTnmKMICwBBQ4l2x86CQvNHCaFCaVoItpAJML_KR_Js5rbbhKDbi9StHzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان ذخیره گندم کشورهای جهان
🔸
چین با حدود ۱۲۵.۷ میلیون تن، بزرگ‌ترین ذخایر پایانی گندم جهان را در اختیار دارد؛ پس از آن کشورهایی مانند هند، روسیه و آمریکا قرار دارند.
🔸
ذخایر پایانی گندم ایران در سال ۲۰۲۵ حدود ۳.۳ میلیون تن برآورد شده است.
🔸
ذخایر پایانی گندم، میزان گندمی است که پس از پایان سال بازاریابی در انبارها باقی می‌ماند و یکی از شاخص‌های مهم امنیت غذایی کشورهاست.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675229" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
روایت تکان‌دهنده از برزخ؛ وقتی پای «حق‌الناس» به میان می‌آید
🔹
00:10:00 همراه شدن با ندای زیبای مرد جوان
🔹
00:14:50 تفاوت خواب و رؤیا با تجربه نزدیک به مرگ
🔹
00:19:00 اولین مکان سنجش اعمال مرتبط با امور حق‌الناس است
🔹
00:23:00 عبور از مرحله با احترام به پدر و دعای خیر مادر
🔹
00:35:30 تغییرات رفتاری نسبت به همسر بعد از درک دلشکستگی‌های پنهان‌اش
🔹
00:48:00 رؤیت حق کتک زدن شاگرد در اولین سال خدمت معلمی
🔹
00:58:30 پیچیدن عطر خوش در فضا با ورود و حضور کودکان
🔹
01:03:30 ماجرای مطلع بودن فرد بیمار از امور احیای او در زمان نداشتن علائم حیاتی
🔹
قسمت دوازدهم (حق)، فصل پنجم
🔹
#تجربه‌گر
: نرجس اربابی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675227" target="_blank">📅 20:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko83BAyujJwgz_84xuSRYCfgRyNDdlO7wM3ZfcM4P3rdwnLwf1AHXBeGcSoS3hr8XUufcoJprE53IGdWYpvl8irLZD753y3kX1Kmq_a_1c2URVWqMTMY4Q_4LtIy8GIcMGLNIKVsfUzHD_934DQsOMW2Mlc1uk7QXaRMZbDWS68YUjpNi5Ai0zwu3aDZW7LFZ5apAryPThQ3kDri1I24Mno4ulnWUZHU5d8Cv4z3LkUYKVOW5vWYjbj7SxhjgTu_f-ols2L8GzxVwrSxoP90IhQzy3utdmAtxBOx5mCjroikYvZsMCzGiHqY2JQeuvx6Lhx3__akRABG89MeHCCa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تیر تا ۳۱ تیر، نیروهای مسلح ایران ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی، یک جنگنده اف۱۵ در داخل شلتر، یک هواپیمای پی۸، یک هواپیمای ترابری سی۱۷ و ۸ هواپیمای سوخت رسان هم منهدم شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675226" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a26a310e.mp4?token=K_f6zN7MQuDsotcOV9-FTx4of7lewGr862MciOgFDR7yQuGUgRweLoY6hEnpJffca_E_-F7TXpv2BnC0ydTiOhQ-yuxqMLu1tclG72YybDk82-IyTxjvF62DPtq92Ppc3QgBy5clIYJI2s4wkfUeRtkqLu8NunhJ67ymmTDynnIccWs8TevYYNLAHPrCBJENuW6wAWDxchhV4puhftLueo1-uwLE89TMdW2xxIi6gVwS6WldSOjzyBHGmuM8IYmraaq0mTZa7zJE2vw8e67gnz0nc-2HTJ8OCPD4EOYF_PQfpiJUWoJoxnXLpwe49Bwp6oO4BfVFw0X0HiLyVBMh9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a26a310e.mp4?token=K_f6zN7MQuDsotcOV9-FTx4of7lewGr862MciOgFDR7yQuGUgRweLoY6hEnpJffca_E_-F7TXpv2BnC0ydTiOhQ-yuxqMLu1tclG72YybDk82-IyTxjvF62DPtq92Ppc3QgBy5clIYJI2s4wkfUeRtkqLu8NunhJ67ymmTDynnIccWs8TevYYNLAHPrCBJENuW6wAWDxchhV4puhftLueo1-uwLE89TMdW2xxIi6gVwS6WldSOjzyBHGmuM8IYmraaq0mTZa7zJE2vw8e67gnz0nc-2HTJ8OCPD4EOYF_PQfpiJUWoJoxnXLpwe49Bwp6oO4BfVFw0X0HiLyVBMh9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا آخرین لحظه عمرم با افتخار سرباز فدایی وطنم و ملتم هستم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/675225" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB-4aze0fNY1LbIu7ERNoLwjfZSj32T8MOIhfdWcY9yoQ4EoOXEhvzu8mLH1RMst1GPRb6B2jI7By5YXuhMlnJk3aQ820fYP_ArJBCzkRn9APBU0cg8hEszrU4mLNo-KaDPp7gwAOKI0JP2GA15P_Yf82j3lOrqt7hCGlrqPfu01Hg1HWL-qQKsx27ZGFKwsmqj-4OkK0sR3G63PTQC6vkYOcojl5eNXVQERMeGleFCXZsNmTWO12ARJMRVlwsKhm9IlbHK1R2ooVq68dfB7e7J31EJvIIqIb15Boz_GhtFO4KlEr3d_An53A94R3zmMIyZiXk7Yfgc467eqiwyn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت آلمان در تهران شایعات مربوط به تخلیه کارکنان خود را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675224" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e7e43c57.mp4?token=RgHXzZGu8HhafpsN1FHjt0nabyGm-0GYpXePY1cK_-BfrNIT1VlAKyUVpi_O77TnBetHaReLMiiicLtq5nwS621JQkJcpKaYJWPkUy3y6slL2J9uG0nY4k_TMmmc5OIhyrFT4IAtOhdVw77LIilNGTroKG5nRUikEmSGX-2m4fmqBZNVsdekDfLg2cPS3PDDdt6vbDzyWwN1_gatlVenTVFpOIttWEjzjstGthnsEY86J8-ZjDL_qisoGbH6j1CkOB8RfXfWV9hGOcuSaAi_Y8O8LFuw3miISF7TBHfTahSJhqgl_ovlQPxV2NNmm_tDBkrT5htE8PskMnSxi0HUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e7e43c57.mp4?token=RgHXzZGu8HhafpsN1FHjt0nabyGm-0GYpXePY1cK_-BfrNIT1VlAKyUVpi_O77TnBetHaReLMiiicLtq5nwS621JQkJcpKaYJWPkUy3y6slL2J9uG0nY4k_TMmmc5OIhyrFT4IAtOhdVw77LIilNGTroKG5nRUikEmSGX-2m4fmqBZNVsdekDfLg2cPS3PDDdt6vbDzyWwN1_gatlVenTVFpOIttWEjzjstGthnsEY86J8-ZjDL_qisoGbH6j1CkOB8RfXfWV9hGOcuSaAi_Y8O8LFuw3miISF7TBHfTahSJhqgl_ovlQPxV2NNmm_tDBkrT5htE8PskMnSxi0HUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔹
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/675223" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عملیات ضد صهیونیستی در جنوب الخلیل
🔹
تمامی ۴۸ گیت مرز شلمچه به دروازه های خروجی تبدیل شد
🔹
تیم هاکی پسران زیر ۱۸ سال راهی نیمه نهایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675222" target="_blank">📅 20:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PCNxUolnO_On7pRatFkvPRPEQLXM2jGViH_DEFaVkY766JjdfwrNaCfgPVfQxmPXVKc5mMoJKQW0ih5Zs7r5V_QuS4H6fULRlWbL3DO2XMINhBUpkaX5zdWVv7K0Qe1408MTZ-BsCd5Z7XJZFzMooJPV5coPlOnfaAfqzNqfZvGZ_IVR-PrlT9KSSz0_XE1mTAw7p5fEKnkj5lbZCeykyeNi3AE1fLmPutdaSBIOnGSvEcqRe7osqe0BWTAXFLIGKcrw2M0TqniNQnt2oa29nmw35vDHEcrwlXZ1c0N0ZlgGmnZ_P6KD33Pekee8SVTnFAx1XLOGGRzDPGrQEZnfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aerhIU_W40S_pms9xfQt8-m-zGWuYmJDDdY_BJGPGWZEsKhDzZSyPczm5pqLdaUhu3Q0Io7g09cPBuJuqs8RowViYnShFeqsrkZz-Oua3ZqihraTvVNyxySCMbNOA20PfIrIAaviFKa9ohHDH2TNfyJXdnR2D0KMjYqaYiN8mCWpEsCHkkH7jW_muiD88XSatLrejv_9DWMfGsQoHdgeS7t1mJ1xfnQLPVWBF0n4Z7d2WPRvXQEDpGhYsN_JwrQ_xiNpvnX9XHVjzQAz1NLm0qoIbhSh9Z9JIo6tG6hcNkg5iAFWW0_RXeXzgNVqWtE3w2hnepWx1jBQmXKjr5GebQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۵
دارویی که بهتره همیشه در خونه داشته باشی
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675220" target="_blank">📅 20:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8Hiw15vq_o5B7WYfl5V6sHyDinChBNG0nfNF5CUeT_ZaYF8C0C2KSDCsmgINkYF_6tgNDZWvN0M3PK4ysij7_YnRo7fJZfLXqNCVFJV8gcR5f2axqXKS290BSB709KRU0dEKhcInB3kUfnjnYbEqy7j6j0bvV0VvDiIDZCvNM_3qrFU_K5X1RCUvcQlXntrRuKj_p1TUPKYA-Nla82VHzWeiUbAMieoFMajiuQPzbwXyPjgl4PzzshHRvp-C6oXGDid-6G2TuG9TQHUpdndkfFaZvhAhD2PiTi40hOmtFJTAjAWRDX1C25Ax1I7CoIatROKBR1RXKw-2jx1hCBwow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675219" target="_blank">📅 20:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE4NL106Hdk3xJnDLsoGEqWWS2cU1YfZ4RuN59QabT0pyro8hervrYZg0vCeYkng1ype165xzcdp8GKEczmbI8Wnvb5dfpzMA3mWF-dTSwpJbMXEPxGbrB6eM3dlw8lYFioFeYoUMjCEFIZrEB2VPyoDaVg7mkVKMBCsX2gTGaGBNSf4GKqwfP30WX3of8FY6UW3ENrlEhj-Bas-WGvbireLz281JiBqDoSATzeiBTvYDhwl6crzknh9IavSyzvo1QHgHqhnExf1H-YBOB5p-Q_c8OeecNPMfnJD_Z7k9CAuFJChwwbXLwn9SSfcwgRkwMWLzVqT1R91jIfuvPxcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwLK_WAXXZdeB6Ch8HjSHq1MVdxDUd-Lvei6cjaQy09BTBPVeeHOC7_X0nNa1y5u1yAZafxPwKQ1lL16fhqfLVqFRTlpnUXMz1w3E9tr4rj7tWqfJpAdEUViUVGQ5smOaO9s71qETr5GNNSZec2IrmedWUp_b90xxfbFRblApUOOz33ApNN14xS0_6n1YQDnqw0CKZZJaXVvL2cQaczDvWP4B6N7lEQ9mWE7dlxJZeRd7qji4os44KIcRglt3Lxs6WnSiBusRJSAXcsQaro3mftAjtfwNVugd6XYrGW5jfn5RMaLkC4O6i8SW_jByvrlXnRivNZFVsANMrjhOmQ9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی دی، کتاب پر‌طرفدار این روزها با ترکیب شگفت‌انگیز معما، روان‌شناسی و داستان‌های پزشکی
🔹
کتاب «بخش دی» اثر فریدا مک‌فادن، روایتی انسانی و تأثیرگذار از زندگی در دل یک بیمارستان است. نویسنده با زبانی روان؛ اما معمایی داستان بیماران، پزشکان و پرستاران را دست‌مایه‌ای برای پرداختن به مفاهیمی چون امید، ناامیدی، روابط انسانی و چالش‌های اخلاقی قرار می‌دهد. این رمان، علاوه بر روایت داستانی جذاب، نگاهی عمیق به پیچیدگی‌های زندگی و قدرت همدلی در سخت‌ترین شرایط دارد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675216" target="_blank">📅 20:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fabb55f0.mp4?token=h8qevlKgVOcl9YqvkkG-54ikcGkDdxEfICjlZdY8G7kIwZUrgYqHXWM-qrAKkMQUDzACztp4LxkPsHkI3joC-kMb5Pufq8Mh5Z8_qYL54zA7mdcLULA7HYFtxjLsm3p_hylKeFX7aeQGmWrpB7VBlUg9Kk3VZXgo9VmalSPr8o6F0LIDgfOgjYYPCWqqOXCxmYfGXeEb6HlkGzamMTHhsqELwasme51xdnpV9AT3fTaZpvfbvQZzOOxgcbFw9RbRDC1DoxmSoVxSPYBvHJDlw9dtzHUrWynklRmhVRvc2r7U6DrLjaucBpYaGwW5TC1DRxzViCFSnFqLfaIGkIdQQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fabb55f0.mp4?token=h8qevlKgVOcl9YqvkkG-54ikcGkDdxEfICjlZdY8G7kIwZUrgYqHXWM-qrAKkMQUDzACztp4LxkPsHkI3joC-kMb5Pufq8Mh5Z8_qYL54zA7mdcLULA7HYFtxjLsm3p_hylKeFX7aeQGmWrpB7VBlUg9Kk3VZXgo9VmalSPr8o6F0LIDgfOgjYYPCWqqOXCxmYfGXeEb6HlkGzamMTHhsqELwasme51xdnpV9AT3fTaZpvfbvQZzOOxgcbFw9RbRDC1DoxmSoVxSPYBvHJDlw9dtzHUrWynklRmhVRvc2r7U6DrLjaucBpYaGwW5TC1DRxzViCFSnFqLfaIGkIdQQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ دردناک خرس سیاهی که از تیر برق ۱۰ متری بالا رفت
🔹
ویدئویی دردناکی از گرفتار شدن یک خرس عظیم‌الجثه در بالای تیر برق حدود ۱۰ متری در ایالت نیومکزیکوی آمریکا به‌طور گسترده منتشر شده است. این حیوان پس از ساعت‌ها ماندن در این وضعیت، سرانجام بر اثر برق‌گرفتگی جان باخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/675215" target="_blank">📅 19:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX5nAI6FhyFXMOyw1dheohDezpLKQ6CSPLhBaQfOuIAkQKUdLM3vimIbie0GkW1OP1PKjYAqqlRKKWbiaV8JYfJ_-qh5YsgrDUprGl92IdaBS_2XYAIET5E9AO9lA_Dlbb2aSCVrOS0TX4uzDjeHCt4wVBeCnOCIJYx5bRsFe-LAXsQri9zq64IFitQFkzZBpePbcOChd4N-qyopBu4Gptn4IMc-eicKUeaN4S415UC7WPdGv42vqGl55Ht_8A047BL2zECm3_ShOy6hMVJ8dtESb3qRf-5NhgsQKE4X0mKNvbebkVk-buFASu7TVJx3G-KJTqngm1FODl8T7QgIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر: تردد دریایی به طور کامل برای تمامی وسایل نقلیه و کشتی‌های دریایی از فردا یکشنبه از سر گرفته خواهد شد
🔹
این وزارتخانه در اطاعیه ای از «همه خواست تا از مقررات و دستورالعمل‌های دریایی موجود پیروی کنند تا بالاترین سطح ایمنی و امنیت برای همه سفرها تضمین شود»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/675214" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsaR1gbyOytSCkTZyZwENymAkgZu1MqaacSOQghRWFV6aMnSDh1mtBb6rfcPazyCkU2jAAGUIHxId_zpLpscg-caAI6_ZCP8Gq9fIXP4vNPcfJ8c6ZI01IJxY4ZKZ0G-7RvMEHoDejPEqha8O6HsGDaD_ZAUr2eFK5AN6LkswEKp90mtMFqEIXzYn7N5gwjxJFe2aMksn5MDsv-aBhLZWtNRix8GedHlcLAur0uKwYd-Ozz5MJqc_Ade_wOX_12mjLaYAWuhBjh8Kj8gafVf9KPhZhEvLj7b79XKFwsluoPpo8qATgtcOkW-rRZ4cIz2Z23M5V_SwYYWQLPa2BVQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حالا که رسید به ۱۰۰ تا
🔹
حملات جنایتکارانه آمریکا به ایران متوقف شد، آن‌هم زمانی که نفت باز هم قیمت ۱۰۰ دلاری را تجربه کرد. این اتفاق نشان داد تحولات بازار انرژی تا چه اندازه بر رفتار سیاسی واشینگتن اثرگذار است. تجربه جنگ اخیر نیز نشان می‌دهد هر زمان بهای نفت از سطح مورد انتظار آمریکا فراتر می‌رود، دونالد ترامپ با طرح موضوعاتی مانند «توافق»، «مذاکره» یا «کاهش تنش» تلاش می‌کند فضای روانی بازار را مدیریت کرده و از افزایش بیشتر قیمت‌ها جلوگیری کند. هم‌زمانی توقف حملات آمریکا علیه ایران با جهش قیمت نفت، این برداشت را تقویت کرده که کنترل بازار انرژی، یکی از مؤلفه‌های اصلی تصمیمات سیاسی واشینگتن است. از همین رو، هرگونه پیام یا اظهارنظر درباره مذاکره را باید با دقت و احتیاط تحلیل کرد؛ زیرا در بسیاری از موارد، این مواضع بیش از آنکه نشانه تغییر راهبرد باشند، ابزاری برای مدیریت انتظارات بازار و مهار قیمت نفت به شمار می‌روند.
🔹
هشتصدونوزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675213" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5afb5b61.mp4?token=qNxOECqevz8muuPPphiY2nAYet6jbPcmP5eLGXRdMvKWC3-o-VqWXvUxCXoqV_XGcsEtm4VXum9pLfpU-VE70hePxej_qu0tQbuhtomX4SQ5pEKInVATcWQlFrTsBToUoj0Fd80daM27ojQW2-Ln_bGCbzUhGOBpIOkz3IRLLAojo2gVHC94UDvpHSI_c-rXr-9kmgqv0HXtslxSsWMXlPDxC2bxwT-CBsTebtQVOWoc3kRf_F3UgCC5fWljw7ARTMCqwZ2stvuam_bY2gQmmDcy8AM61p1lhWyLw-fsdn8ewJf7CCwKvjabd3WVwadQRV34JYmWD8nTsvQm_YcN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5afb5b61.mp4?token=qNxOECqevz8muuPPphiY2nAYet6jbPcmP5eLGXRdMvKWC3-o-VqWXvUxCXoqV_XGcsEtm4VXum9pLfpU-VE70hePxej_qu0tQbuhtomX4SQ5pEKInVATcWQlFrTsBToUoj0Fd80daM27ojQW2-Ln_bGCbzUhGOBpIOkz3IRLLAojo2gVHC94UDvpHSI_c-rXr-9kmgqv0HXtslxSsWMXlPDxC2bxwT-CBsTebtQVOWoc3kRf_F3UgCC5fWljw7ARTMCqwZ2stvuam_bY2gQmmDcy8AM61p1lhWyLw-fsdn8ewJf7CCwKvjabd3WVwadQRV34JYmWD8nTsvQm_YcN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک یمن به قلب نفتی عربستان
🔹
یمن با حمله شب گذشته به بندر ینبع و شهر جیزان معادلات جدیدی در تنش‌های خاورمیانه ایجاد کرد.
🔹
این دو شهر قلب‌های نفتی عربستان سعودی بودند که مورد اصابت موشک‌های انصارالله یمن قرار گرفت./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/675212" target="_blank">📅 19:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIkfURP7Nc6qdPU05cmoxyR1af3YK0j-pWzC4VrBExop1eJUqtAIrbn1h9SzY1GTyHttYXiWanWauisfek0uF3LGkjnmOAt7DTsUq8_sI1QdCIsXAMEvFj60s-V9x--HnbjSaceEoeHXujW9SF9j3_63Bx8V7ZNtUXyWV6a-6jHDsMmsAEU_jQHE467E_4DMC_HmGISj6eIVt2xg4pkdXQlpouhCbGCdtL4olYkbyQzLWv5sI-4qaS9_KfteTCnIQzxTYfux5QmpR1hDBcjFCzxaJOD_FpJUBrH4sVesfUZize2UCB6kvuXsX6AUO1hpgRbO7ZydL6W8mdthKC9o5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارنامه ادعاهای ترامپ درباره ایران
🔸
ترامپ ۱۰۶ بار ادعای «شکست ایران»، ۹۵ بار «نابودی ایران»، ۸۸ بار «توافق قریب‌الوقوع» و ۷۵ بار «باز بودن تنگه هرمز» را مطرح کرده است.
🔸
تکرار این ادعاها در حالی ادامه دارد که تحقق‌نیافتن آن‌ها، از نگاه برخی تحلیلگران، نشانه‌ای از دشواری پیشبرد اهداف اعلامی ترامپ در قبال ایران است.
@amarfact</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675211" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMDbJtH9-h0wnXSSGNKEBBwKWi9uZIgb94bg2n7Cb9F1ner-t23w9rd-cB6RT34jGElKAltFqCL82I4NBKrlaNFq2gYybx0A8sTyWlEEVbuko7G1sJ5va_uow6c8-KhfZSNrK_9KIPpQrl0HA0Jn91JMDFPUIxcSxprQRWvkhgIhH9gWY8CwQ10Q_Xlhy4e5J5aaO5feQptWLMfXM7s5qIAsY3Zq1lPWQbPhKJjZ2mKYly7ez_6pAGLo-YIZECm7lkmEF_jeAULt0l2iO-Foji5TDskPjNTGv2hsQDm-E6xSf_42eeYAVZqS2_-qs-WMGk3Xq9ZP2Mex7jb5_XxPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhB4UybjBxZkrx1ldIAcrr0Lseu_z-fhuuFm5vuY_FYYpqZe589wyps7c2gDYG3y-qtiWt78fq1dZ8lcqufOu8so9p--XpmrTa6EiCGnrpOWrU8PPDyAexQU72uTXNtFIGwF4q9p_7AAXuaAdHytFyADbDAnLisxVuHgDG-QAVqpGW7loe0UzPl_NkMM-wQJjcZHBdu1-bvskpozeUTbqpjU4fEFMhBfUaMVICvYS62mB_LiG2iwGEoWB3vdteNYW23Ehxn2tF-jM_DSgNCd6swLib96z3l02hPhM27AB3Cbl6qDvgj444BX4kmeE3MD41a-8g0Dv__6tWiqgtJhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLvam_eU-I2Hz8IgfGxtQTVQCJx_pfNO6YaLBn8lB1Ko4gSmc_xsYi5xaOXgaODFCnSo2cCUOCcZaOqHi9X9NCjv8527JZhma-8r7ZKtecT52S7ws6wUDO_OeywjznsbuOBzUoW35-wl8oRlq6x6AYmPRUkCPWqeUxGOp_4MTO33R0FSCdS8bIZbIqgQTEeMTWoFXVjlaQb0j3yzjUSp9aKdS7xKdpRyWLiM_8P87LmbqINin0R53dfKDOjhaxjww3HNeV-I9XF5bI64vQ8aZg7AmuMcmq2eOydzQzwN0AqnqX3aEIm700IrwP9dJoIFfu3VqSRtNsu0TfMUfijv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRgkGLeoIOfGw9gt3YqRcN6AtFi2rpoVQzhBdXN-pd6tf_C-Ewc89w3hG4JTvmF05-Ota2uRW_qFhpwwTK5LUc5KWtX1QftAG-BgRswHkTb0RUkwsx7nzUOzLGAow3po-yTFdu0tSG9e-_mrZ_xg0MvL0kleE0uWDbMpAD_dZki9ByTXYZbrMbJw6-jxONEee4kS9zakHdresCZB0Yq6hm7nE3T8iUhPi7JhEqLBa-pWz01DVdsw3VpKmgkGztHse9f1MPGuLGyRoETYJ9LjnHIHWFCc5bZfwDU-cZVdN1izLTH02Le5-et-JYV-Jy2HTeLHj5CSvAVIq1oOi5RS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfD80YsUnvt9BoNXc9dBH2ZR7YJo5EMueYqyjzpLCdnkCzf7kPxHD0Uhd_m35T9Fwpep3i5WUHaJ3cEn_mdkZkDHSHWZbizz6H0ahon5IWKDpHwEjyyz48GrKfH8tgxxQFGWU8QAuKVsxb-BhpFBZjU3ciGF1thS2xqsCMMPgyq--micS397mc91XAQhGig2v3jZTaZzyu42C1Qg2bKyBkjN_47u14WLpopxiyT7sFhoSj2K20E6CAXRcV9VSsbEiaWiao0mDSeZ2xZuVvhPwkzmumnzLTJCLKnzChkoniW4qlsQHEpEy7EqOz3W6YHmAqqmXy8JzR1DDMB31Rcq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAr5hW3Y-UC_sL614fpchsMbMNiHDyvJx2PX6m3HtQfW-V2SroRystZxQ9_JNG2hJnyP1m_ZFCuZFS0Lob3tPq-f7h7AlsMaymgZiHdQn-_kWRjK7Eax36hBh4tUmWMG--AWFRw231s3Ojz1EZeHIfPvQto54YbdwqYHJbbngBVrFXRqXp1j5_Cak8jIURMLgPswuDav4VO-uQ_Jfix1IPEZgRR5qPodTZubBAzTBkPWa_-YkX9zovMvwpDIDtQVeKWN9YdQhXD-RgQuxg7vi283u2ilgnEE3bhYYyS6YSCfgib2XL1xQHCxizFa3sbC7EjU5HC9eWrviT4lI75k5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه عاشق دسرهای خاصی، این ۶ مدل موچی برای شماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/675205" target="_blank">📅 19:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCz_kuOF20h7vXhw4WvgjyO7FPohFTuvVxmmswkfpok_2I_PNCCGvJ_UMqys06jNJc0p9wQdctQfq4AOdhFKsux3ih0FxiFUGFA03njP95kadqDZ1ju1VESte6Uh5ncmx8U-shJrFG-2LgFppil8Pd7bMS4SQ0YMaFovH3SSHd6PNU8eg1yV-5TfOvmqFnEKLgm3lqRN45830R4SXz9dkDpQOJ-IkY9ksi_U_OGTpOAhpslaEA6YlpkzNzQEOZF8H4p4OYDtJEDeCPI1QSM-X2PhBvfw_dIbiPsh8V7K-4RIW0KPewCxaXYQvikmzX_F61VGwj3BVHfgswmMO7HZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمتی که برنده نداشت؛ مسافر در شوک، راننده ناراضی
📊
دیتاک با تحلیل بیش از ۱۵۰ هزار گفت‌وگوی کاربران درباره‌ی اسنپ و تپسی، واکنش واقعی مسافران و رانندگان به افزایش کرایه‌ی تاکسی‌های اینترنتی را بررسی کرده است.
💎
این گزارش، علاوه بر تحلیل داده‌ها، یک سناریوی جایگزین برای اجرای این تغییر قیمت ارائه می‌کند؛ سناریویی که می‌توانست از شکل‌گیری بخش قابل‌توجهی از نارضایتی‌ها جلوگیری کند.
🔗
دانلود نسخه کامل گزارش
👇
https://dtk.sc/0xgmj
منبع: دیتاک
@dataakcom</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675204" target="_blank">📅 19:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE389mYu7OfGRdigaoOCPPmMX56aXnd1d8egGoP-F72eLuwbzOmWCXZ0WWqpUOUAUEP7HSlzkWrIrlz2irAghse7W4QCRuClWkpxpHLP_njH_ezS-cHCc7zwZga5S6XUDDIRI9UsDbvNdxW-IlDQ1CvXP0SeBddJU1JXrVvibmr71vVocMUw9qLCOEAePHoO23-aQCrgb9bhvhETgaj0Cy3kOqNLZ71mp-MQ4l-PfgELYBr8Vtf1L4GHAKHBnmkVw_cC84qkcK_j5ikEIRiOgB_UrykqDfTnEkknv_9ZrszeXS5PR1EXkQ4dEbqXToBG7h9Bt-h-E_qXWUxJwkNTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت‌های جدید واتس‌اپ؛ ویژگی که برای کاربران ایرانی ممنوع است
🔹
واتس‌اپ در تازه‌ترین به‌روزرسانی خود، امکان اشتراک‌گذاری موسیقی در بخش Status را با اتصال به سرویس‌های Apple Music و Spotify اضافه کرد.
🔹
با این حال، این قابلیت برای بسیاری از کاربران ایرانی به دلیل محدودیت دسترسی به این سرویس‌ها، عملاً قابل استفاده نخواهد بود. در کنار این ویژگی، واتس‌اپ امکان ساخت مستقیم حساب کاربری روی آیپد و بهبودهای جدید برای نسخه CarPlay را نیز ارائه کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675203" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حمله به یک نفتکش در نزدیکی عربستان
🔹
سازمان عملیات تجارت دریایی انگلیس از اصابت یک پرتابه به نفتکشی در ۷۰ مایلی ساحل الشقیق عربستان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675202" target="_blank">📅 19:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3uzE6JuCaD17Oc-g0N9-5j8nSRkqhQ-Q4D82_mVPDHQayhPkP-4RnIUOWh4skhwFtg-604nocmMbkVhS4ylw8qyrGh_fCA9IbEyq2QwmJbfgzfeDtJqcX5gUtFch3c3QJ0bN5OSm9JN5iVsz5ZRZ407JSZ5UAoI3lpETrIZ_lqVyuVwmy3zGfSAjnZhCWak0SmkN5iiPqPPC03E0hMa5jNdmF3xSAIxEr7m_sHS68__nmRwSCic8sP0nHk5ryI25Q7S-9L3qxx-pb51g-mBwp9YWiEluLaryy3HKblW1JKRaUiufDlkeBqLrP_-LQuMfZf4PGfJSV9obniQj1l6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0ZyhHYOHGblY5FVg6SytTL8f08rJUNIG19IWrleGY8HgPAwJf6U2PksDAC_y1V_zEGnhX0CfkzaXUZ77iDoIYBvUGE_SWO3Dl9tS2ZhSZ6tUq59VBipjKP-0sgLpDjMUH5rxOD3eKLBa7dqcDg-7tPGv-_YvEjsPA1JI-0IVeLWsRLGGBg4PC00Xezgzzv7O2D8UC5HNzk7MiaNGqnZfBCqU0B6vSeAit07UfPqbOmM6dAyCiVyrAkCeT2DSMAHS1H_WhI3HT00qbIPtZteS3OV0dlMIqIbYS2S6M4ZrF6NWkyhMgSkvi2GNnr6fZcHNirMizK3t-i185r4Kd8uGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhER0-0PE_5oohtZgEC5AZTSv1NC9qCdl_TRN9H64DQ2JVW_2cjMNKYLhHlVI_GG4GTNKsGng8j_cyz_jNoQQUheDRWjpQMydw4CzqUP27SBwsGrN_qdPt4DQ5X5n1-vu3E0Zb1uA1Hdix1GsQ1_-CjH0n-EyBo15OHVkd6laH1HAPrSIuRQ8gYEpSgnsBCpMLce5j41lDWM2FdDuFzlMiIpF5iMLjNhGSuPyJpciKBUPZGK9lB2nqngCePNa7z3VW-zbNqyD5CmNTUvi2WDUNCqiu5v31fgfOFLXR_M3OkXRE0NdtCQODukNrgTebA78qS6TmWvYjn8nukFiWUYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUGkIA1HKke9OJ8ciu25oPy0E84p7lV5zSn6YSpOD43jwGysFqKiBeNuplA3GhoMqcyRKRh-WY86Bz4EsBGwh-omliLZFiDgQHCj30UgZWlvsHQkZ_SsusR90Glg_7RKbcqe6g0bBgYEOOe4GTzAvuEhI6S6qVEVtIG8nJClvBStk4Sgpm5FN3r8lS0-cIgKclPXpE8xl-UP955y2prmcDZpTp-F1z8G7AlqLXazjhm5tbeuDNnD3Lw8m9h0ia2VnjzwwI6hVyi0_w6zM6450s6cNvj3ozxaStMtIuu-RFUR9Ko9mmc7FM4VQ8FOflPk1Ty8GkymLCD-iMNCf0ZBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MY6OWsKJf3zd6vhtYAj1E-Fj-Ae60lN2a7i7yHD07yjvSXDK01sKvfrwIKgpzXcT9Yr4J1NkL5e5iy2cWk0hn4ThEqA5UXTIZTLr6b5PhVCFBLdYCDfN-jxAZxX9t9C2dCdxt_Tef8HGUaEw-Xq2C14ghuwOq_pphDCF5VXPFLGmXb8DXaUkykVFXEaYDtl7oKGyeZguOAZC-ioYBjlWat6Z2VoBNhkBsuMTtLJQOV56Gc8OrQamiacrOtacnUslmht3OU7ZSFmRYbSgWVr1id7WyUmXwanj28BgtJUtFmoCzn9uRdcXhJUvtcWtKNOeGTmpbOhzwOoFb-HwZJlNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwZdcCoCnT3x9MgqErOX3KvMLTKp-DWIVEDPsGZXwRns5fesK4lLy1VpBvWsXppzP5H0LvYAqJ4asLkNWNRUPW-KKLWA5NSkTkYNqoLBYsAqJEPAxVtFQigX0oPEIT08_uIqhQdf3w4_5LspXFOqubTU2KrZWgr4AHynm3JKXZRS_vQyqP75V_UIiToC2AaMl0Rf9eXMs18xM2zLqoJY2ZvBAJRqS1fziRs3Nh2DU7jhepF41Zj5MCn190dtS5EwW4Q0h_3Prl5IpyZyf-aeSiASpmU4ztQSSunel5ljn5SO0jP70AjrOyeoH3e4O-CRNLCGHpcEPhLcru_RGew_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg7oFHsebkAkE6WzW5cQNftp3mJKEyW4lpbRSqvMZA7etkQmpFZ0s0iQqICifuHkMepyUp-MxaTgheF2enF6HYzes2EdZPfHEsxiECsY_-aVTwnZydgsut0csL0sPTtHFsa5eyH1DPwcui36j_nPOH9dlaYOvyNuf4UV5CBpy7A-3mvEwNAM1nDOkY0x2wMq3Q-p3CwVUNx-fuK1GKzKp_y1CRxnicDUG0uZY3JSFtLu6kobho5KPaxI2WEEpVYZ-rcQk0huB3LyU1sj59kVdLh4N4fakbvmh8xOYjAWbBeR0S_QkSR2XCHC64o--iSdszU3VjQ8l2xUL6_81dOKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OampnMp0NtG6S0YemwNPajfROP9X2CRBAEmJFxN6DUmrp1bWTVxBRuXR5UuyGjqqmGpmQj2z36soR2fmwen4UZD1ottn0rSmY7vqkmWb1vr4SfuO1mc4GirnAKv_8XTz8DzQaWJilazPSGova0sngfHUmev-XU_xYyNUmn7bqnSb1lsUc9PVTosWtKuZyIc3TDJihbqNZTM4M9ASn-ngxDU74Mkj3UoxOHRicwa3kTtYZOvJKm-RCFfyHZeqsRrKI1PasfZjtoNGS-eMFDAwBg-jqXLAKQxaUahRb1jxpXRG0p-Ia4iGy-zPydXahwMAz_kvlLgIlvYb-i1535b8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZAwHs-IaQanv6aqtJxyiI6CTHp3R3pCCs5Jd3CaZxMI830bT558vqp5i7_rOuMbQURUDTOFtr5VElJbyJAUILELSxsSMDv_VuKAK-rgtJr9SADUFZ4wqYpthCk93TvoiZDTbzzxVIuuc6VvUXEMxwLCSKBfwRxyGxrcBjhGK4hCXC378NDE8oSIb71K8nHAtRkvVKJPhqCrV0GdILIg6E7Kb6hPU5cgntIbYeowz4785kFmVeM9iFZnbynknUMx10xERWAgXaxWEuZPuirDM5Ekd5UnNGenR1Y2hBq2PGfhD67Rrjcpb49EY_RB35-g9H5kHTqdgUpyKWxmWP1-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلخ‌ ترین قاب دیشب ؛ وداع مجید صالحی با اکبر عبدی هنگام انتقال پیکر به سردخانه…
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/675193" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfhJo9fV7pO8pJd-r9WYfNYUICEgyCcGauRZPKAknpLTahyQrUg2PtUTLyqKOnhhd64AIPE7KGXAZQ--HxT_b1rkxEZ9HNxPfW0X9BzP51bIGCeuyWBfXJiuAvPs82CdXCWvxtjU64iFA2EnjRJ018Zz2I_83mU4DZxJSMAGHW_Y4UIvDqhY1HxFN1AbKvaadArnhgr48gk-8IO9F50KjOpQOvWZQLie2hrInQXEM3ezYCSVbUPkynBaHAotcnsCzC60IX-anvQNTsFcJSU885w4i84PHzQUxzzsrHn9tNl4JnALJcixzIuCYXnNFjLoOhRo6EAyakdMLqZtF60O8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از برخاستن ستون دود در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675192" target="_blank">📅 19:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8fb9157.mp4?token=gmuM4QJMNqSJOcA-PFlQKnDfdSGOtkZV5PpEL8-lZvTq5bSFr94-JxhXPIw9hfrvqwWV2Zv9mw9CKH4YOhdNwxjvlvfNhSGmhQ345IFRVQJAlGEqyy284GTGwdLNyBZHBIeIaxIXTPVDSBYfpT07SSdhsALo3InelAwFOZ15Qm1ZN2zHQrwzzZxwKo4pq171axK1W054PBdd1waKCcoJjkG78HjUEOEzjgrs06KxzkhFP-b8DhGQqDiIFJW7vi3vYA1TGO2NaQjXPG2KwDDtmKEwWz66FfcPaud1QaHIDijgToR8--hXBXykkoblKiRQSuli3YSEXE8-VZ8v66J63SHfOXfjdI9E37YirhhXUhzAg1hCHJy6ANBYO_eGCmlkU1CS872tf3PIPZVSPvAYNrvG5fDwjxDnfucH3ZKrt37M76ojZmRo2_B0rcKjiCUm4z1aE6w3GOgG2nGmwqJ1_QWGnAGLkDUFg78eE1-oLUvT6NlTEOY6ujFlC7X9uae1sHSiuvpZ1FnAkmlCwk7Jt1mRf36OJ6Mbm3yJttx8uSyRN70bM2vhB253TJFaCzsrDDXsB1vnyVFLaYVBkZ0RLuWH5DvXAsTE-GzhQAMElkARD6aLspLVO5HZSQFCtj59oCJPBYufHERBAT4XHaiGne3TGth26xZP04lIqxMyylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8fb9157.mp4?token=gmuM4QJMNqSJOcA-PFlQKnDfdSGOtkZV5PpEL8-lZvTq5bSFr94-JxhXPIw9hfrvqwWV2Zv9mw9CKH4YOhdNwxjvlvfNhSGmhQ345IFRVQJAlGEqyy284GTGwdLNyBZHBIeIaxIXTPVDSBYfpT07SSdhsALo3InelAwFOZ15Qm1ZN2zHQrwzzZxwKo4pq171axK1W054PBdd1waKCcoJjkG78HjUEOEzjgrs06KxzkhFP-b8DhGQqDiIFJW7vi3vYA1TGO2NaQjXPG2KwDDtmKEwWz66FfcPaud1QaHIDijgToR8--hXBXykkoblKiRQSuli3YSEXE8-VZ8v66J63SHfOXfjdI9E37YirhhXUhzAg1hCHJy6ANBYO_eGCmlkU1CS872tf3PIPZVSPvAYNrvG5fDwjxDnfucH3ZKrt37M76ojZmRo2_B0rcKjiCUm4z1aE6w3GOgG2nGmwqJ1_QWGnAGLkDUFg78eE1-oLUvT6NlTEOY6ujFlC7X9uae1sHSiuvpZ1FnAkmlCwk7Jt1mRf36OJ6Mbm3yJttx8uSyRN70bM2vhB253TJFaCzsrDDXsB1vnyVFLaYVBkZ0RLuWH5DvXAsTE-GzhQAMElkARD6aLspLVO5HZSQFCtj59oCJPBYufHERBAT4XHaiGne3TGth26xZP04lIqxMyylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهه نودی‌هایی که عاشق حجاب هستند/ روایت دختر دهه نودی از باحجاب شدنش در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/675191" target="_blank">📅 19:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghCg_uhxab_N-DBo24nd6zb_-JeANOuZ74A2RyDw79ydNf0cfXINh12x0dSnmYSly0LUSG73nYpv3GPY5_s1TOFBLtD4ciwewgvkyVNvK3Jxtjeu_zpdN2bhU7GJ-OiGyM_5_QdvNAH1jjSDvFCHv_GRTK1kFwC_Y2rzvk9dN_tlCXlgo06og2UuuYfCCvClHEJ8LeClzK5bPCmU1zLdjaJs2ICQY_snWnKr3yLJKXJxhb5lb6ITg6VQsLs0H99FPqMtJRS1-d3Zwty9CNoicGeJ-uI_QIzluop7cG8j9GJERGmnXMtYr03vXvCW3TbO01CQ9VY8TDsUlAdCXyjnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/675190" target="_blank">📅 19:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3vO1ud3C7-fvTo8xwxhBaqlxNIGRZDrTs6te7CjA6q-AViQyL44ExIxND7vyvz70Ffqz1zeGQOFoMtt70FdiF0RedOpV_po0opTKQdYFIoS2jDLull72J9bIBG2xjTzCxyhu_Wvc3Vq2ToKc8ZVZ2lJ2Z_zctbzICV-9_G-wIRWfhpoKMOblvMT3a0vY5EGfGZXhfuSQQN8ZuowDMseRGF-K3CltM1iYrQDycsqJJt8NMVfZoZTUt0QBMxYpX1d_1gj3edE8_mGTfVpXvShXcp4xMYTDwezF3pvqSEtoKUy0vA7O96QdVkrpKs53_O8V0PdE89dHcb1JCB_LCMXJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگِ سطل؛ کشتار برای یک ظرف آب!
🔹
در سال ۱۳۲۵ میلادی، دو شهر ایتالیایی «مودنا» و «بولونیا» وارد یکی از عجیب‌ترین جنگ‌های تاریخ شدند.
🔹
همه چیز از آنجا شروع شد که سربازان شهر مودنا به چاه مرکزی شهر بولونیا نفوذ کردند و یک «سطل چوبی» ساده را دزدیدند.
🔹
این…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/675189" target="_blank">📅 19:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUwWETH4rm7HMHql-9iuBti9W_27OLbEinubrnn0-s-YjChT-rOI70hh2_aAxRkRYhV3EkhmPLw8z8sCm6-YPMYi2yhplsYabjw1BNxI02vy9u0NXXuxC53tDYYLxU4FbG1sIdRimXdMaM2c23nroWN5S9VR2R1dzc783vkvtFOMof1G3ysDokPUFfE6CO2AoqV11CFXobewYgkUaq10fGxuoV5i3xJ_3FzXWmRv8c9QuR0AEgrn_KnxZhXSWAv4aGrNwx4FjL2vCmGkJ5mVrgTNWS_yAw15C2HezNlfPLp7ImwrINEayWcDwWW-AEin86XKl-Nx9t5kBq1AcSrcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
ثبت‌نام محصولات GAC آغاز شد
اگر قصد خرید خودروی وارداتی دارید، اکنون فرصت ثبت‌نام محصولات
GAC
در
سامانه جامع خودروهای وارداتی
فراهم شده است.
✅
قیمت قطعی
✅
تعداد محدود
✅
ثبت‌نام آنلاین
🔺
آغاز ثبت‌نام: ۱۴۰۵/۰۵/۰۱
🔻
پایان ثبت‌نام: ۱۴۰۵/۰۵/۰۵
‼️
با توجه به محدود بودن ظرفیت عرضه، پیشنهاد می‌شود ثبت‌نام خود را به روزهای پایانی موکول نکنید.
🔗
ثبت‌نام:
zaya.io/TGrun</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/675188" target="_blank">📅 19:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5fd88f97.mp4?token=b3fXSXC_ARlSHXMq-f4QqeLssTep59f1mxHatmlKSsJxVkOWsqZP0wPNJAaVkkEu1SahzKzaX2kQY5rWjvCFtT93vl5qb9GeMYSNnNbi9N35AZTzEUeo3dCMQ43YyLuCErxyDKtd_ARCItSDVGJokpgtChPMG8mWBfvRtR6omu12KHlECRCS0Q2rzIox50tZRS-9JAkVtXd3gPaZvh8PhoES0y6UG8TtdF30Twyv9QkH1T2-OTVAvkgjgtxzQtQ0ZQBR0G-KCqva_6ZtYlFDjU07ucV3ZatiHziYmiboPPpI2dMX89E_zIybFoipYEMjTz6FTIQm9tLrJ-UkzhibQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5fd88f97.mp4?token=b3fXSXC_ARlSHXMq-f4QqeLssTep59f1mxHatmlKSsJxVkOWsqZP0wPNJAaVkkEu1SahzKzaX2kQY5rWjvCFtT93vl5qb9GeMYSNnNbi9N35AZTzEUeo3dCMQ43YyLuCErxyDKtd_ARCItSDVGJokpgtChPMG8mWBfvRtR6omu12KHlECRCS0Q2rzIox50tZRS-9JAkVtXd3gPaZvh8PhoES0y6UG8TtdF30Twyv9QkH1T2-OTVAvkgjgtxzQtQ0ZQBR0G-KCqva_6ZtYlFDjU07ucV3ZatiHziYmiboPPpI2dMX89E_zIybFoipYEMjTz6FTIQm9tLrJ-UkzhibQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط هواپیما بر پشت‌بام یک خانه در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/675187" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035057ce0f.mp4?token=oMCr3_DcqwUuCC773_HsedgOF67_2AwzfAPBSizYYze022db6AU9EsilXheujFnakZp16PEEAEIEUYrQVIO3A_phy11llXjhNgI_S7zxTVjn18MUQ8KIbNn4cVV1cLpJE7NHwaCjxERQrN5fAyJ5xeK2WRLQGYFJlg4rsyJGssnk81OOR_LR5Xso5lrTrN2N5bWVsIffNp7_e7GTAZH27cyIHKq-_Hmn9-mSXexp8DAI-QIOoNNIwn7UVzKERMGS7w-XhGmAtxFg_3SUa-t5NInQebo-5sVZLcTodTULgoDWXvRfIdv4I99m-tfYTtnjaeXYnF8_DpGUuBn_2pOgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035057ce0f.mp4?token=oMCr3_DcqwUuCC773_HsedgOF67_2AwzfAPBSizYYze022db6AU9EsilXheujFnakZp16PEEAEIEUYrQVIO3A_phy11llXjhNgI_S7zxTVjn18MUQ8KIbNn4cVV1cLpJE7NHwaCjxERQrN5fAyJ5xeK2WRLQGYFJlg4rsyJGssnk81OOR_LR5Xso5lrTrN2N5bWVsIffNp7_e7GTAZH27cyIHKq-_Hmn9-mSXexp8DAI-QIOoNNIwn7UVzKERMGS7w-XhGmAtxFg_3SUa-t5NInQebo-5sVZLcTodTULgoDWXvRfIdv4I99m-tfYTtnjaeXYnF8_DpGUuBn_2pOgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این نون‌ها خودشون یه وعده غذای کاملن؛ حتماً امتحانشون کنید
🥖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675186" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a67650241.mp4?token=DVtYROhBdZ8e4BGC0fsq1lEH2-uKzfbrc24hmEFdIDVgnBe7ZnSZOkSDCeZjFKaEsBV-oJEKOHOl9yPi3_Vh6c7xult1GeHlFYjkbA2b_qJiN0k-dra3mNnBBZ59T3V2o6k48PUBF86-v6ejQePqc_21z9fDCQlS6o-dMe0g6YcujZ6GshmEZQi4Mn51eAEb3cDT5kh7GLUgllsrCfn509zuEfKG5bMa8VfKAz47e3ehem69gBobwSufQ_FqXqNfpcCDeJa5rIf5ELiXAxFQqWcRFXS3Q-Y0HjHEz_XGAManpEvorN-RzFfaiKPnDkr-mH_2EwsRnz2L07XRbEYLww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a67650241.mp4?token=DVtYROhBdZ8e4BGC0fsq1lEH2-uKzfbrc24hmEFdIDVgnBe7ZnSZOkSDCeZjFKaEsBV-oJEKOHOl9yPi3_Vh6c7xult1GeHlFYjkbA2b_qJiN0k-dra3mNnBBZ59T3V2o6k48PUBF86-v6ejQePqc_21z9fDCQlS6o-dMe0g6YcujZ6GshmEZQi4Mn51eAEb3cDT5kh7GLUgllsrCfn509zuEfKG5bMa8VfKAz47e3ehem69gBobwSufQ_FqXqNfpcCDeJa5rIf5ELiXAxFQqWcRFXS3Q-Y0HjHEz_XGAManpEvorN-RzFfaiKPnDkr-mH_2EwsRnz2L07XRbEYLww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کامل زانو زدن پادشاه روم در برابر شاپور دوم قدرتمندترین پادشاه ساسانی!/ مدار
https://youtu.be/wGPuPBpm5AY?si=Z2HXd-mzpNNvhg4K‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/675184" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=QJCl0WAWMuCYsq4Ns9p5RY_a7MS1e3x9w1RpSpeJ8sNd1Fh3irryvzD_ePHu0SlDHH83fyNjFQCZlY-mmCGHbTWUgVz8ICndJcAE0H9LUI4LoHoNGiLMU_YtlKysh0HM4ePy6WHw8sawHf67w5xDNhZwonObQL3oTt28xvojgBPmq38iwwNvHaun1KboZmDscznHVxEv4yZASd38W9IudrkR5hqZzHpgGE-BhV3HyWstj9Od431reuyKOS3IlzHSwhLf8KhdStDXQiyoHj8IzzoP9xsgl6IRYk2DWbu-p2QjJac2TpbYeALFDClv4_r4HTlJv1WqoKnqb6Po1Ww_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=QJCl0WAWMuCYsq4Ns9p5RY_a7MS1e3x9w1RpSpeJ8sNd1Fh3irryvzD_ePHu0SlDHH83fyNjFQCZlY-mmCGHbTWUgVz8ICndJcAE0H9LUI4LoHoNGiLMU_YtlKysh0HM4ePy6WHw8sawHf67w5xDNhZwonObQL3oTt28xvojgBPmq38iwwNvHaun1KboZmDscznHVxEv4yZASd38W9IudrkR5hqZzHpgGE-BhV3HyWstj9Od431reuyKOS3IlzHSwhLf8KhdStDXQiyoHj8IzzoP9xsgl6IRYk2DWbu-p2QjJac2TpbYeALFDClv4_r4HTlJv1WqoKnqb6Po1Ww_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/675183" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران راهنمای کسب‌وکارها در حل چالش‌های تامین اجتماعی
🔺
اتاق تهران با ارائه مشاوره تخصصی در حوزه تأمین اجتماعی، فعالان اقتصادی را در اجرای صحیح قراردادهای پیمانکاری همراهی می‌کند. آگاهی از ضوابط بیمه‌ای و تکمیل به‌موقع مدارک، از بروز اختلافات و هزینه‌های اضافی جلوگیری می‌کند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675182" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ده‌نمکی: اکبرعبدی یک وطن‌دوست واقعی بود
مسعود ده‌نمکی، کارگردان سینما و تلویزیون در
#گفتگو
با خبرفوری:
🔹
اکبر عبدی مردی از جنس مردم بود و برای مردم باقی ماند. هرکس که ایشان را می‌شناخت، می‌دانست که به‌صورت گمنام در حل مشکلات مردم، رفع اختلافات خانوادگی، آزادی زندانیان و بسیاری از کارهای سخت دیگر مشارکت داشت.
🔹
مرحوم عبدی همواره در مشکلاتی که برای کشور پیش می‌آمد، از جمله در دوران جنگ، در کنار مردم بود و می‌توان گفت ایشان یک وطن‌دوست واقعی بودند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/675181" target="_blank">📅 18:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رای الیوم: آمریکا در پی کشاندن کشورهای عربی به تقابل با ایران است/ ابتکار فوری قطر برای جلوگیری از جنگ
ادعای رای الیوم:
🔹
همزمان با افزایش تحرکات نظامی آمریکا در منطقه، واشنگتن در حال اعمال فشار بر برخی کشورهای عربی برای همراهی با سیاست‌های ضدایرانی است؛ در مقابل، قطر با حمایت اردن، عربستان و پاکستان ابتکاری دیپلماتیک را برای جلوگیری از آغاز جنگی گسترده علیه ایران دنبال می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675179" target="_blank">📅 18:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvJPeB3ES3kMueCClvxNXDPCAdEMP3q05zDRwMBeA1kzjMaJXjnlhBTze6p4xksucjgn8rxu439dcLcZGUc9hm4tkPy8otecosaFbUQ4lFCFom0ar9Mk-Y_y7z3n3Dj56hvh2uXdTU49zrVp3kPjru5wGJ7-6QAp0_7GUyMAM6vSYbdcnhfktzodpj1HcM_7CDKdBSI06ivSy6QTvZ7QlgQKqkxPMMGwU02lAjEYwGwklc9Vv4yZLsUR0I6lmOGVXUi1zZFloKwj5saM6puFUxznmAu0KRRo4ygWYa6AkT2qeVO1Czo4VgRy61wAOngGZwSSArdxiOtjvndghcKQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-XR8G3EIS2JNKOORUPM-bWDUxamLc1Yho1bmkMg7D4iZC7N2MdbHgL4ANiZD-qq6NRRk1N5J0xxV9XR8iZDOvrDQIFrA497P66sdnQceNLjH_r0uqAmLUxtNPlJyq43_uEMzyp6B6X1Qvr-oM9eHPyyjWRZFDA6saEkGcPgPB5NIt3cOW4Q4oRh5R4JEDOw-2lU_TwR1JzzaMEECpaQ-lGBmcd5Bk4dIzYFDnuvcxp2z9Mg9MQuOgIdA1Csh6ihDZ0kj4GNB0MSq7-HeoTU55LggcUSfN5Vk9EKBR8n6nZTKSOSm6lWvunK_bycArfAQ-QXKVG8O9sonQZO1_Zpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت احساس تنهایی و ارتباط اجتماعی در ایران و جهان
🔹
طبق پیمایش گالوپ، ۳۳٪ ایرانیان احساس تنهایی می‌کنند؛ در حالی که میانگین جهانی ۲۳٪ است.
🔹
با این حال، احساس ارتباط با دیگران در ایران کمی بالاتر از میانگین جهانی گزارش شده است؛ چراکه تنهایی همیشه به تعداد روابط بستگی ندارد و کیفیت آن‌ها اهمیت بیشتری دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/675176" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5r9EeJGQuN-2-aYfb5MdPbLoHcWv--pprjLcLS2L5PIw-Jn2kN7HLakMfBPOE98LDR-px43Hi4UXquZiyMKZImyT5wLr_nJgcazdS_iQy7NEBwDGRS4WI-WwFnyt_85fN5k55vbYccVo2wX-fPxfq7SR2AosqC6aqa9urxSdJxgKN6ssgVLqb-sEFnBeCZyMakRhQ4I5wa7cYkxl6Pk5D9KZ_52x_1cnuDfWDQxvONqpXLYtXBPUaY0V3e9Fv9ZC1OYJtR82ruU3txQh2IoqxcMy0v5l86DAS-d4ajvYSzmylqyWQ_tzkPuSNorxl6x1kOVQaul-2PK6B3-MIKrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش معین، خواننده به درگذشت اکبر عبدی: «هنرمندی که با لبخند و خاطراتش در قلب مردم ماندگار شد؛ باور این خبر تلخ بسیار سخت است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675174" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ1AVcR_Um9ynfuUQEEZFZpyOSywuxX9dtD-9NPQxRGMDlioocZYpGVMCFwRhxvvicc3t9DSxAZJtWVZ2BSs9HDL7V7Suu_WCCtY5Ho8G5PKl5Zbi9JtcTPzfRBNs2OTbIzieDhNLDst6Y7-4zlHUtwnphmEF1U1NjGA8w0lsWeN3qej5fIZtIdKxSrANsTcV7-nitgLg1NtjooiG4o99PVFi_06RyXZEZyXGQ8FiM2xd4z2r3pTXjG6BGrxYBrMujnGxAVLMc0V89EzM0dGJDov_vrwkNLFO60V22DKqzvFBu4Q1FwjlVpqmjX-gItIwkmqo4zXpfpnrGZAguJSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهزاده‌ای که در دو جبهه با روس و عثمانی جنگید
🔹
محمدعلی‌میرزا دولتشاه، فرزند ارشد فتحعلی‌شاه قاجار، از نامدارترین فرماندهان نظامی ایران بود. او با فرماندهی سپاه ایران در جنگ‌های عثمانی و روس، مرزهای غربی کشور را تثبیت نمود و با شکست‌دادن نیروهای روس تا…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675173" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KckcIWTkVTt3vYvXqlQyScTjoluyy6AWWu4L5G2cHFs0HMaH2zCp1tHH7cwo_D7wr5ene8PIFa9IvJq2rtJvVWq_Ej__h7yOrNX-aJ39B9NNa1xuIZxtGpZ44RsQB9ywZ83UlllU1avrCWA0AGBEjT7nCe72_t2WhiQs8E6nm08aVyptSR4nnXwgrZ764hG1u8RXjtMF1nQ6MOqflpzw4wKFreEvt8K8JTwstDiwGQQ8DsR1-4cDvOfQoS60Vmb9o6n64C3QiUr64vIbTlE6Q55kxopwRG5wNTrek1yslUzgGXtusHRAvgS-2X_QFis1-30NVzWpPdu2PlDvmc44Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DL87WmaRk7_71uQ9XIUyhkHdTdIq5h3kaHV-gMeWPmfJV3HRiMmn-G5Gv9PDFYZATcrqpCZIBLOCc3MTTuqUGXE2bMR7YY2ep0J0MHskJ28m10UY8E9pWAnbYAC0YO-hY5hV1R5bq4TeYv5wmTzMxLzgbRx7cC8a2a-3QAsHzwT88TRNfadEsHughm5BPP9iZgUPiJHnMWMX43Af_LHXemwH5UcpnRJZxY54TygnpfRk6VFtUJ-_EUuo7hfXBVWU3JMZZtyTd9WF_uURznF8qxNgM-NTfNaDgSYFjM5qhnzg7dSZro9qilCcpyYe8tMdsEXVrAAwmgtX_m_T9eP9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYy4Gv2fkR7yAD6pcXF5AibYyKthcQuoynOiAG37r__xn3bXE_xE55grIi_pbYxKsPSyk2ya6O7Fs9bo5QoJVCnGys2ScjoAOVkgwITXnzKdEz8NNSWXHZPMZJYwlsgUlXOO0Apl6TpWd9mHvOPOEXN0EziRVttR_WJlPh5blv8oObgLtc_tJ58ZYfAiF75tEmliMOmvvJIl1h_T3b0Hnt6VgvfYJTMjJaXja-zEJnnuy0wVtmRPRJb6SspVAnidkU4Vq085jMIKHI5qdNaNi_LqsoVcgiae27hqd7IQv5khAe6eTPAv9CPW5IHLR4lwrgQSfgZ_e9sKWOe_QHUSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-oOMUouVuQDQEWNm_ddtmxW37HZETOgojZzxu9EtxNEdbGIG7qMq7Sbgm-h6vOwIxBCdP6yt7CWkZvSPVoYbX4oVeYkGnRty1N073uOgpl5K8wT_dmRa6EoJDDhQUCzO5BR-uLAgq4tqIJy6kcXhTGLx8trGzU0yf3T4nathHSJlNCIVCMzSjiALOExWoICMPhSkrwJpoCynA0QUS2M-b166zyODquoDMWRkhycenbYSPO-Rtm8nESu4tN_tjCuO-WxZEnTEufNzhrdEI6cueR18J1QUG6bBYIBaKd0qPaxQxmDfw9dBgJhcWMotJAwOGbPytnAELmdDM0WeG4NrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4jjkhbptF3z8FzU_zVKoYSgAW8fa5-LB6FcQwUxq13gQkbJHoOVMWK-hxKRych2zdpJzeGRVBu-MtSL94ktVfIhoIGRIF7Z-zsJKAX9XDytAfN6T-sqxtHa9fHO3PCrCf809OOgWqYt8o58UK622PSZ9ez2eXV9ZhdI_pohYmW46zHSGgAJDs-KSoihEODWCQ4sCTjDZqbQ5etQPYANjZZ0CJoedqipQBFfqW8JhITL0RFiU9WqMfOyX6vM1nFJou8lDdHl0spCyZlTYHwBgPurbSKFWC3LH6Qsu_jYeEPrLoZsTnOAFcu-OYc7-xpHFVuJOU0VIUDtyMnj0iQ1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzgLfAumJb7XrGfejvDWybUY8j3S1Xc56SRwOnykIswpHqWIRokW1TY0weAw12K8C4Un4S9LaB5hWyWYtPMB3TRVRzr0SphdiOSFW3Kakd9M48mwNPpV5t6lWEVZ5-X9Ti36KGBSCthTsF6AkbUOThUVm6L4SkI6RVSHVUDDsqev68W2FwrKzkuVYItxjXWezxsG1dQj_vHQRTNDLnGQuHRe8OhNS13KqtMdeucuDLHcyUZROd3_Kc7M3zlBOkZnqVidHQRWqTbl0kYwq8UpWS_ihoorlue7b7Kni1WVSP671uTLC6fqQlUtwKbh-GJSyWhjtVMuXuwR8IGNB-b6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg5s2_VZwbpZV8fKNjDxPu3GSRBVugnUz5DWjvK_O4n187_gLNV7Gh5VO7Te_6dwuq9-XcwNHYd9AG1uvM9cNYhGK5av-PbgdxYUiRaWWmHghTdwM-faRUcmFt2RPKPURYfSk0J4gVr3DMDcI_AXCk6koJaHtZZ_5AliJsNPRifg3ZlQVCaU84NTlhJsMD4uMa1BbbzWQ9xbh-4Miln9DEUz5w6DBPQLXpBJQaBmQIkfGm2GqIvd3jFMvHAIfuADg1y71gwuvg0Z6soCFasJmJueuYyJ8XokKqikuHS0vCSWwtCcdZQDeuWdpGd3Un3e11j6vrdamaH0NsnsKb0Tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd99xFSb1S6_mas--kZjIuTD4qtY-_5VNXnl5swyhVZTac1TZ1fEX7rtYDP1w0Y8GXcFQlDqX603-o6h8W6Qma6ac8w0NYWq7CAOK4Mj0XED4L6I8LyhmxO6xSBIQcHFyyQLTGSpockthVQHl9Z6u_D9bnYcAsUqYyN3a6d7DIJrZrsRvNqOkgnUCZyZAe99FB88bEfLrY4uGXmrF_1pOyo05UoGUwq0Ruio7T7noQvvdhufPozhaGRqxz951TM52VVAYy9_BQvAyYV-IrzTvP1e-49snxMw4jcwcE0gK5WXZefXn5xGQw_wXa2RxlH2UwQL_TTmphVfFiqp16v8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cinmyiao6GTW_oNuLJzXJLVsaLUep0_K0q0rVQiR4Wxv_viR0Xfr-7ij9ApCzDoJS5bWMNqFdxpELrqQg4ZRgF1_H1WusazqVUA1RdIgaqr5BE-0IUbZVHcWPE0KBCZeB-USYZjBbJ9eNLhVgiD1WA7Xizt0z2rK_z-KnRNo8Qn-WM97pMGm5DXNbc58LWyxM6Q8lm5GzFX4mgz4f8y1_mb7TpZQkB0gDrn6g57SlBJIWZWa6YzpfATJTZ_tOw6TfrLFj-JD9Pe7j3FKJsH28SO0Aq87k2Pt-QavUV5NejS2CPCjZWqYlm7k_mpHBdi2vqXjKohbJvR0CxSDOAAtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpplI54yOQ-PGidFyhHuRr24v3qe_FAkUzs-ZF5Gzz-sJRoOFGk20X0NGFwP63P8Ok_EB6JXWd9YvB2x1MexdGLzkDkXwukHnrhxZgLbnAJNmsqmHu2OIxnEOmy4XpXoEmWmQ2vqA07jIfT66VqXCQaJtbesPuY5UNT-VJlQ-7aC71CEKKsQziPiIQ__V8P--tFDe0cP-aiYEq9RCcR4Qycmkq2Ap5rCZhwcXYuMXA1UTDtuBjDd7nyxJNH9P3s-GoqXQIEYKj2nXB3DE8t6jCgSfZuhgak2aOd-sK5w0H2AKNLf6r2ZumUJ-FoCTqDb-WLca1lRQGsr9mLAk1xgig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤌
کلی ویلا با قیمت کل توو کانالم هست عضو شو ببین
👇
👇
📱
[کانال تلگرام من]
(
https://t.me/fafamelk_68
)
این ویلا ارزش واقعی و قیمت بازارش حدود ۱۳
میلیارد تومنه
،
اما مالک به خاطر
نیاز به نقدینگی و انجام یک معامله فوری
فقط تا پایان هفته حاضر شده با 8/500
میلیارد تومان
واگذارش کنه
همین امروز برای بازدید تا پایان هفته آینده زنگ بزن
تا ساعت بازدیدت رو هماهنگ کنیم.
⏳
📌
#چمستان
❌
دارای 250متر زمین ،240متر بنا،3خواب مستر،روف گاردن،سند مدارک کامل
💰
قیمت کل:فقط
8/500 میلیارد تا پایان هفته
فروش اقساطی بدون بهره
🚗
معاوضه با خودرو،طلا و دلار
📶
خانم رضوی
09194565022</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675163" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKbvWG-DthQpBYqr38-RWbX9aTkH9k4vaN29lu5ob3zOsCs3nXGuXRIsb7u5fTCz3zNxl1gXahumDrRpUsM_CnU4SpuLlDPzuqxrLpKwMU4iGCQS1E-jnPLwJ3SSPk8bczBBrGGeZuaMdGsvMYjFBf3BHQs4D5fmwBKK-_YLDVXcyh-Ik2guUomN2qL_GuAq2PrNr1YtI11I_7Hm98aekg59ux9xC2dJS1nFSYKOO82DRZNaCV_BRCcslFzhq7UCtK7WLWZfbHcR0XSlVaaHRzPCvfT9sjHMeYjgjECtGIETGSllUO-8aQKUfUI2zDRCQ7hpUiRdGRSo4OqoWGwNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTZ1L4aVhAwQ-IFLRorD1nojPY7l77sy-Wk30I7rpKgCemJAmgi37nWhqsrP_-pC_gpbxfxJrewhGrjgs8GnG5P0F2VLn6KbwhFnDg8ecHNGieaqxmkm3RoU7p2D8sUne0O1rAev8-IG4fRVQr92SaOTuG1mPcxtjsVMNrauO8WX7d4Wh_jknWSyG6lBpJag6PRB6j2gqUy1fX9TZ4VW9geaLjIy9Ptfliij89479eWsfVFOYAMVxjksbTYw_JTUHTIe48Qge1sCLGL7m-L5st4HdaNFyGnl8J4bIEqLIPIb8KAD5ovQDfbDGYset_c9j8oMJEOWixg7PMz4zku_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvTa79rkca1FjEKoWx79HGqlT0qyCIongmBXkfUthcY33cwPiLpBsYcTxWNzpnxUFd2T_OisLNwfY-SK8fAxfCGhI30rTtUFEboLYqeEZQSIgyuPiKEhsXjP24akNRjTv0PbQk6yuvK8hzEGg0coKXvwJfOyTH-ggpue1qiBWGGB_5ArdDmkaS4AeXKDYXB6s6uqcbqN4vIcJ4MByxHOrAi_kGE_kg5rHenv0FEARfZvabvJlk7M3USgY_fHQbg0izLwhb1XgSST8kRGp4oLf4JAfoc4cHMims2uPGD551diqdPbXgZG_oBuun4_dGyPtgf8nLxDRjAGuoxpcaBriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CotYOYy3Lgnv0QTyE7OrNxKbxJv1qFoNE9nxSwwqF3EjV_Yb3ZUk6Ilz4utdmUsKnTS6FDFwPX2am7JBBdJCUPAGI_lR-6PpB_aq8eq9g6H7FF6rmps5QN6xxwglmWsrlBp5ct5FiJ7iEYZC8Yrdclahv1vA4EaulhBXq6uEPXdsG4AUj_XEA0JanyAgNskPAiFy8TgUWMWACMfQdZRbwZa-HS31vcGMEs0D5PkIeYg6dK9DrLaOJOmY4NTdm2TbMmHV0Fa_trGRpe2f214Wf2_pQTe43-nsEPnw0Wb8_6FCyvIX0VrsAIW2ZxeGpzOIQ_VFo_11A9FY2zep7PIahg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در مواقع جنگی آب یک کالای استراتژیک است؛ امروز مدیریت ملی مصرف می‌تواند سرنوشت کشور را تغییر دهد
#همه_باهم_برای_ایران
#صرفه_جویی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675156" target="_blank">📅 17:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
قوه‌قضاییه
:
ساعدی‌نیا اجازه کافه‌داری ندارد
🔹
بر اساس حکم بدوی، صادق ساعدی‌نیا از فعالیت در حوزه کافه‌داری محروم شده و دستور پلمپ تمامی شعب کافه‌های او همچنان برقرار است. بر اساس اعلام مرجع مربوط، در صورت فعالیت مجدد واحدهای متخلف پلمپ و جریمه خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675155" target="_blank">📅 17:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675153">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj6nn0k7SPpm4E9AvHtCtp0By8UWCVJKddDovcrnmn6x6q9j5csauK6FDtFpHM3mMIv4yjNFprHiSLZAtbeh5y_MJ_aIBXRV37oKQ4EeS9VzqxjlxbBZcNFeaY2avjqQTKR8kV8ZKA1ozWkGqrFUFvf5DVJFJIUzZdaubi1c0U99KtzHsEx1a8plRKB9tMRvm8tpBoWooPuu2hO9LGZmI2UpcTcGFsENISfiCdZP1hDfEW8JuQ9qaUqqbckHx437PuUZXqvYRVD7fW44Sve6z2AwJQaaqfAVSuzcQzvTIEkYMgRL4vRGOk-xnb86nWomhZ-fh1eBpMQlPNmTwHzjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ کاهش بزرگ قیمت طلا پس از رشدهای شدید
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675153" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
🔹
آماده‌باش در سطح بالا در اسرائیل برقرار است، زیرا آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/675152" target="_blank">📅 17:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czl-qApsn3Mt10TQSxxnzzI0wrZpLCiCYREMiz48nstdKMyJC3AHvESIqeFuKg7vFo7pa7Nhs7YMwy_C_wNZkLdqBVyCYkGgvjNkFdbry8kgJMOohGV0w3oURenDSGWzKYwSliEXtg4phlKVBh1EtGfMzaibp0Qw88GQw-0nxth3VOPaMI55nhMhyO00OhhxYW_Pw18HsdAV3PJyFUFFz07WVwF26h0iJhFnbvkMRor5Bwmb0lP07In2SMygUZliQDEePjg61slAONs0pH768-aXCjIonCPsuVomNWu7xwTdZ_hfVFFNX7gulnfjqwB3KGMBhnUM4xHvlBYHitBVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوچک‌ترین اسب جهان؛ فقط ۵۶ سانتی‌متر قد دارد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675151" target="_blank">📅 17:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675149">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f4e5c1a.mp4?token=N2CBjpyE_m0nTfJ6U1QxEnScNMPPuJVpjCIDmPnlOPgwqIvemIZwRDFaerp_KNtF18jn1dl-eUxIgJMfPFMXDycY2f0LlcfJ-zOqXJjOaRPJW4LyOESnaM8l-bHcBj-tERHe3qKhLkL8rjkh_dHUrlAqLRKROokRlktVIcJLx3NskAEXp4Xu9bshxefeiGliCkwP9nPvvpYXOSIT96MmuEFLZt34PkOPO6FJLNiM2LjiApBGuqHB8BV7F7n51JNbzOPsAoSTGeMuAbYv99xnckPCgm4fIkZEt01dCtY5hC9HVi1dVoB8d1kUaAvBH-OuRd1tZSDNQkvW942j3RGipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f4e5c1a.mp4?token=N2CBjpyE_m0nTfJ6U1QxEnScNMPPuJVpjCIDmPnlOPgwqIvemIZwRDFaerp_KNtF18jn1dl-eUxIgJMfPFMXDycY2f0LlcfJ-zOqXJjOaRPJW4LyOESnaM8l-bHcBj-tERHe3qKhLkL8rjkh_dHUrlAqLRKROokRlktVIcJLx3NskAEXp4Xu9bshxefeiGliCkwP9nPvvpYXOSIT96MmuEFLZt34PkOPO6FJLNiM2LjiApBGuqHB8BV7F7n51JNbzOPsAoSTGeMuAbYv99xnckPCgm4fIkZEt01dCtY5hC9HVi1dVoB8d1kUaAvBH-OuRd1tZSDNQkvW942j3RGipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
خودروی همیشه تمیز، بدون ذره ای گرد و غبار!
جارو شارژی خودرو  با مکش قدرتمند ۴۵۰۰Pa و ۲۰–۲۵ دقیقه کارکرد مداوم
کم‌حجم، سبک و قابل شارژ با USB — همیشه همراهت، همیشه آماده!
⚡️
🧼
از صندلی تا کنسول، از زیر پا تا گوشه‌های دست‌نیافتنی…
همه‌جا رو در چند دقیقه برق بنداز!
🤩
🌟
قیمت اصلی: 1,598,000 تومان
🔥
قیمت ویژه فقط برای امروز: فقط 1,089,000 تومان
🔥
🏠
پرداخت درب منزل
خرید
👇
memarket24.ir/dirmob/180124/g-en26903</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675149" target="_blank">📅 17:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeCdVBJ0o0Z8js9f_D-SjM9JV-SVsf94azPVzEwljmiusX5JlmoZT_beL87vseKAKNLefUIm9oS-Mc16RyLdkFZiFa4YHWnuvrU1cX19vDB-cg0csHcHCABy14PAr6EmfzNYJrmDgM3rpB-Dv-PvkOTix3xvV7SK74r1d4zLZTeqrjlku9XwwTVYYdJgOGzouHGnr8-Y4UXVdQRRVQ0hFz02t6Hm7pWEciwReJeEN9eNmqI6jQ7TMGIBldsDJPZklwWhF24SsTf3YoW51CQTBeqqal3pdmXqF6jHljrvuiCIDcJEqHFgu7cWMVGmo44EbuQ3Kv3sJ9XQFe4XUvMFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند روش نگهداری مواد غذایی که عمرشان را ۲ برابر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675146" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آتلانتیک: آمریکا بدون برنامه وارد شد، با مشت ایران بیرون آمد!
آتلانتیک:
🔹
یک ضرب‌المثل نظامی می‌گوید: «تا وقتی مشت به دهانت نخورده، همه برنامه دارند.» آمریکا در جنگ با ایران دقیقاً با همین واقعیت روبه‌رو شد.
🔹
بدون استراتژی و بدون چشم‌انداز روشن وارد میدان شد، اما پس از دریافت ضربه، ناچار شد توافقی را امضا کند که به ادعای این نشریه، جنگ را با شرایطی مطلوب برای ایران پایان خواهد داد.
🔹
اکنون آمریکا بار دیگر به میدان بازگشته، بی‌آنکه توضیح دهد این بار چرا وارد جنگ شده و چه تفاوتی با دور قبل دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/675145" target="_blank">📅 16:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای اکسیوس: طرحی جدید از سوی میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین کشتی های عبوری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/675144" target="_blank">📅 16:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d18d97ca8.mp4?token=rJKhNtqhZ2HPeOtc4XsAbjngF2RobMIQtFfM49Qi-d30M9xZutwRXe--n74DKWkC1sGMs2NIbljWFeM42_ex7NiPnx9aIwwkQw1PFtSKzPJtdYjugv1Y_d9MeZ_ubPu8CLqURMkePsWFFhNY1B0Z8JjEm29YuZViJ60ow4-crLM1FlK1A1issJqLpGHtuXPJ8z_TMmHaeo0UOQ4PN3nQ9O7WDEKI6SNlnqLRvjwacxcMYwz6viQahD2X1C0gGLbzZOGegqoPdcDvpV3SAM-l5sXMFc6jVNWmMfNeEmCgFvCFejG6CaumncXjoeG7IoUeQJQ1jZtd3WLBrs5AkEaJTUfX6wy6mwkUcfxLey4KvGU4ICQ0rYZ4eZ4dz_Xap3i-rvoIssMmnMG3uPk7Ut38XQjmhK9XGNaO-ZS4MwbeA_BtMV_G6HM3TVoupehavWSwkM-G0miv-Y80zEvNeeLoHIR5vCMOmCF3paWhY0ZZPAv67GeF7_ca2kN_VtwtbxNpBjU956T5ut8QDVWXlkRVA8_hL8msOxEKct5odKCPNRyBhzXcuRHLe59HbGrgeyKJdvw6wzyRlOU6bHlqFIllXn8uN_UDnDGnGekV2oQlGtAvR4L-SJcyFZhbkRYzTU2zBdQ2H3UxUOgt_0K1VMM_8kdSOIP_-4Q5-40ds7MaZXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d18d97ca8.mp4?token=rJKhNtqhZ2HPeOtc4XsAbjngF2RobMIQtFfM49Qi-d30M9xZutwRXe--n74DKWkC1sGMs2NIbljWFeM42_ex7NiPnx9aIwwkQw1PFtSKzPJtdYjugv1Y_d9MeZ_ubPu8CLqURMkePsWFFhNY1B0Z8JjEm29YuZViJ60ow4-crLM1FlK1A1issJqLpGHtuXPJ8z_TMmHaeo0UOQ4PN3nQ9O7WDEKI6SNlnqLRvjwacxcMYwz6viQahD2X1C0gGLbzZOGegqoPdcDvpV3SAM-l5sXMFc6jVNWmMfNeEmCgFvCFejG6CaumncXjoeG7IoUeQJQ1jZtd3WLBrs5AkEaJTUfX6wy6mwkUcfxLey4KvGU4ICQ0rYZ4eZ4dz_Xap3i-rvoIssMmnMG3uPk7Ut38XQjmhK9XGNaO-ZS4MwbeA_BtMV_G6HM3TVoupehavWSwkM-G0miv-Y80zEvNeeLoHIR5vCMOmCF3paWhY0ZZPAv67GeF7_ca2kN_VtwtbxNpBjU956T5ut8QDVWXlkRVA8_hL8msOxEKct5odKCPNRyBhzXcuRHLe59HbGrgeyKJdvw6wzyRlOU6bHlqFIllXn8uN_UDnDGnGekV2oQlGtAvR4L-SJcyFZhbkRYzTU2zBdQ2H3UxUOgt_0K1VMM_8kdSOIP_-4Q5-40ds7MaZXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوش برای موکب اسکان شهید ابراهیم هادی
🏴
برای سیاه‌پوش کردن موکب اسکان شهید ابراهیم هادی، به 1000 متر مربع پوش نیاز داریم
📍
باب‌القبله حرم مطهر امام حسین(ع) | حدود هزار متر تا حرم
🔹
هزینه هر متر
: ۱ میلیون و ۸۰۰ هزار تومان
🔹
سهم مشارکت: ۴۵۰ هزار تومان
تا الان هزینه 500 متر از 1000 متر جمع شده
❌
این پوش، سایه‌ای میشه برای زائری که زیر آفتاب سوزان کربلا، کیلومترها قدم زده...
🥺
اربعین امسال، به یاد رهبر شهیدمون
👇
باید با شکوه‌تر از هر سال برگزار بشه
♥️
پرداخت سریع و آسان
👇🏻
https://payping.ir/d/j47J
💳
6063731266068221
💳
5041721113831557
به نام: هیئت علمدار کمیل
📱
09136729200
@Ebrahimhadi_Yazd</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/675143" target="_blank">📅 16:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ahdkdCqgWkxajuTXJawZ7kCAkm4-KStUgUxT4ygjODs3d6mvpySroAYbrmIye0NV7qLu88Q4nwjzUpcQMHmffrAYU78u64NNSR1YLxCyYXQ-rVoiqcYEG0YOLzGn6JwN_4sxj-Gby0k77FUX8ld8XKHfIZrd55PEOiKmO6yKANTht8E0Uhq_ax54kBYMme29LQzLuoksaNImqY9aw8vNDVg_i2Zat7Ojz53TeByBFNugUW7PTfYj2vzlLzD1OtWpGUZdBqYNTQVWsMemLZiTBw7N0uS-r0lY6gJX5Y6Ex9p1EUlBYme9lQhQFfL_W6XEj9qD0GgYg8p6hEh66dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منقار تیغی Razorbill؛ شاهکار هندسه در آفرینش طبیعت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/675142" target="_blank">📅 16:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_670BarEI7wlMa_LmzIYwzH_66I8oYc1iR7RTohl0hSIPQfIULrB-UhFUL-G_TZGCpNyWTsJp7Lnq3JArTpMwihCARsFSt-55APovLwpLBYDe0mHL0NrxhYg-Ac8hENNSpoboJ2TWDYxvf0DzHApI7mMd2LrJ6r5Lq3ezhtPnMTwvSTqyr15Fr0IDKzBK4T8vPqO0bM7SNjKPL4_O1qzb3iAtZhqnD2AOsISdDR2CSZAgg93Wp4q0DZMRFwDt8AvnS0N1vU33DZ47Q30FlzmlQJCysRi_cHW8rKmgOItPHID576mUktzY43WFHthPnJqCAErPEfeMp_HUmQEec92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص ۸۰ درصدی تمایل به خرید در بازار طلا؛ بازار خود را برای «۱۳ صفر» آماده می‌کند
🔹
هر سال با نزدیک شدن به ایام «۱۳ صفر»، بازار طلا جان تازه‌ای می‌گیرد. اما امسال اوضاع فرق دارد؛ شاخص تمایل به خرید در پلتفرم طلاین امروز به ۸۰ درصد رسیده؛ یعنی تقاضا برای خرید طلا نسبت به هفته‌های قبل رشد چشمگیری داشته و این یعنی بازار زودتر از همیشه به استقبال «۱۳ صفر» رفته است.
🔹
اقبال به افزایش نرخ طلا در حالی رقم می‌خورد که در ماه‌های گذشته این بازار دچار تلاطم‌های بسیاری بوده است ولی همچنان مردم خریدار طلا هستند و طلاین به‌عنوان یکی از مقاصد اصلی خرید طلای آب‌شده، این موج را به وضوح در شاخص خود منعکس کرده است. عدد ۷۴ درصد نشان می‌دهد که تقاضای امسال در آستانه محرم، از سال‌های قبل هم بیشتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/675140" target="_blank">📅 16:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675139">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آخرین تصاویر از وضعیت پل‌ها و تونل‌های مورد حمله آمریکا در استان هرمزگان
🔹
روایت خبرنگار خبرفوری از استان‌ هرمزگان
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675139" target="_blank">📅 16:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad07b266e.mp4?token=CcsA2etGohfIm1JwhSrTy_jKctBGIH0OA9geL6v1yBXDuwfAifc7Z-lHVwwxeyN6FAlg6H6uvfQVSTu_licmN6arsRosII3sX80Q66_--qZsfvAXk-aolkLA3ARDgSx0qgln-rZwYMW-i88wrAVsp3WC8OWKGBs5tryr3zMXFPkSW2wNWxuprgqOrkh9s819V0dw22M9tUgdv3sEl-NBW7t8RRsLhWSg3U3M50AueCXaiCcJ29w-8MmzWqt9g7kYeiBVKJOeRmUjgAVr2EKzA4p-rfAb4NiWxR6go8UnryFbf8RIZlSGa7UznKPM8kPFylVVSj-zVbnR3WHojIGGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad07b266e.mp4?token=CcsA2etGohfIm1JwhSrTy_jKctBGIH0OA9geL6v1yBXDuwfAifc7Z-lHVwwxeyN6FAlg6H6uvfQVSTu_licmN6arsRosII3sX80Q66_--qZsfvAXk-aolkLA3ARDgSx0qgln-rZwYMW-i88wrAVsp3WC8OWKGBs5tryr3zMXFPkSW2wNWxuprgqOrkh9s819V0dw22M9tUgdv3sEl-NBW7t8RRsLhWSg3U3M50AueCXaiCcJ29w-8MmzWqt9g7kYeiBVKJOeRmUjgAVr2EKzA4p-rfAb4NiWxR6go8UnryFbf8RIZlSGa7UznKPM8kPFylVVSj-zVbnR3WHojIGGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با حقوق‌کارمندی مدیریت پول کنیم تا آخر ماه کم نیاریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/675137" target="_blank">📅 16:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5194524b9.mp4?token=MGLHiqExa2fjoMATcnIKHdiXrp9OZelb_syAC859mum6gwNI9cOeb_gztT9uJrmHYkmrZBnJXIzAcYnffddhA1PPL75n-lz5Kp9JRkyI6jYIr6-eX8h7j9-QFKs_9PRi1yVbA8-iraPmQWXVZdddcQHgdeFvFNzJtRyOSjDjf6Icqj2WE-ORfOvIzZbAkuCS5IiJ_BksD7jVPL3HKAKt936l41wTLk5E5DFDRKnmHf81JDXhcDeF5R9GHzcODKDLURq3Mzrusris2yfjdGhJpr3XhFmcLC9wBfe-wFnLFm3Dmpl3Mkgo9US-9ORda3Rd4bJbQmYpMHSSir6uVvZy77D5q4YWklpn5Pkl7jldzu8nUUWy9k4rBkxWzmy43CueK-MjIf1UGvfP1Ez4iqOEpC4NDQkov6z5W_rc0AH0yyTcKCYHjv65nupiW3f_9N417Wb7i6Qyc440E_5ohLm_NpDM8Mcyp8BB1wunpF6BZyO8aSzWGDydAZMOjCYWfXQIAtpQoftbxLNSflaaoNiIxvTosc029MrwydPUV37KuqZ_kTlWO8SnbnT6lVswC1DZUXrXgzMsd3YsYxRvB4KrAytHskVPT45vsK2y3JGt9pu8sxzJ_vM1iGAOf84y5fbIVhLcg68AtnidTfxOaUzH_akvoUKatB0RvfnduS6xdIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5194524b9.mp4?token=MGLHiqExa2fjoMATcnIKHdiXrp9OZelb_syAC859mum6gwNI9cOeb_gztT9uJrmHYkmrZBnJXIzAcYnffddhA1PPL75n-lz5Kp9JRkyI6jYIr6-eX8h7j9-QFKs_9PRi1yVbA8-iraPmQWXVZdddcQHgdeFvFNzJtRyOSjDjf6Icqj2WE-ORfOvIzZbAkuCS5IiJ_BksD7jVPL3HKAKt936l41wTLk5E5DFDRKnmHf81JDXhcDeF5R9GHzcODKDLURq3Mzrusris2yfjdGhJpr3XhFmcLC9wBfe-wFnLFm3Dmpl3Mkgo9US-9ORda3Rd4bJbQmYpMHSSir6uVvZy77D5q4YWklpn5Pkl7jldzu8nUUWy9k4rBkxWzmy43CueK-MjIf1UGvfP1Ez4iqOEpC4NDQkov6z5W_rc0AH0yyTcKCYHjv65nupiW3f_9N417Wb7i6Qyc440E_5ohLm_NpDM8Mcyp8BB1wunpF6BZyO8aSzWGDydAZMOjCYWfXQIAtpQoftbxLNSflaaoNiIxvTosc029MrwydPUV37KuqZ_kTlWO8SnbnT6lVswC1DZUXrXgzMsd3YsYxRvB4KrAytHskVPT45vsK2y3JGt9pu8sxzJ_vM1iGAOf84y5fbIVhLcg68AtnidTfxOaUzH_akvoUKatB0RvfnduS6xdIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
قرار همدلی؛ برای ایران
🤝
این روزها مردمان خونگرم جنوب کشور، گرمای طاقت‌فرسایی را تحمل می‌کنند. بیایید با یک تصمیم ساده، سهم خودمان را در کاهش مصرف برق ادا کنیم.
قرار ما: کاهش مصرف برق، به احترام مردمان جنوب کشور.
🤝
💚
#مدیریت_مصرف
#پویش_۲۵درجه_قرار_همدلی
🆔
@tehran_roshan
💡
قرار ما همدلیه
🫶</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/675136" target="_blank">📅 16:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f91b4907f.mp4?token=uSrgZr47AWZNdaG7Zm5Ljyg_NvwA0v94d1V-rVhEG9uGp3oN9vjMI3reWG2avt0Xh7l6rskr4ceocr8bG8h4IlPEJ9zHSG4bh_ibs1f-F7ZL-uy3jxzfCv_O1dvNOLd8jxOLiQxwMNGPtXg9HFTkl9jdsAe4ptWIEsIX3fyTi371ouCqwMUzIfxBkDcC_kFahwI3TPH3xBTaqIbXePTS1rnmGAy3dCo6WE1efjX1GRefZ-HW3H1SJpoMLgKErbCBpiqCobaH1-e0W5pdOYNp69sWf6jk61KCoSN5akjymnUFCk9WMhxz7hmA6jIG8Yvs5-sp1YLv6fPv8jf2pE3ZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f91b4907f.mp4?token=uSrgZr47AWZNdaG7Zm5Ljyg_NvwA0v94d1V-rVhEG9uGp3oN9vjMI3reWG2avt0Xh7l6rskr4ceocr8bG8h4IlPEJ9zHSG4bh_ibs1f-F7ZL-uy3jxzfCv_O1dvNOLd8jxOLiQxwMNGPtXg9HFTkl9jdsAe4ptWIEsIX3fyTi371ouCqwMUzIfxBkDcC_kFahwI3TPH3xBTaqIbXePTS1rnmGAy3dCo6WE1efjX1GRefZ-HW3H1SJpoMLgKErbCBpiqCobaH1-e0W5pdOYNp69sWf6jk61KCoSN5akjymnUFCk9WMhxz7hmA6jIG8Yvs5-sp1YLv6fPv8jf2pE3ZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیرعلی جداوی، دومین جاویدالاثر مدرسه شجره طیبه میناب
🔹
دلیل عدم انتشار نام او تاکنون، درخواست پدرش برای مخفی ماندن خبر از مادر باردارش بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675135" target="_blank">📅 16:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: رهبر جدید ایران تمایل بیشتری به دنبال کردن سلاح هسته‌ای دارد
ادعای نیویورک‌تایمز:
🔹
سازمان‌های اطلاعاتی آمریکا معتقدند که آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، بسیار بیشتر از پدر و سلف خود به دنبال کردن سلاح هسته‌ای علاقه‌مند است. پدر آیت‌الله خامنه‌ای سوگند یاد کرده بود که از توسعه سلاح هسته‌ای منصرف شود!
🔹
جانشین او هرگز علناً خواستار ساخت سلاح هسته‌ای توسط ایران نشده اما سازمان‌های اطلاعاتی امریکا معتقدند که او جاه‌طلبی‌هایی برای توسعه سلاح‌های هسته‌ای پیشرفته دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/675134" target="_blank">📅 15:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رسانه‌ها پشتوانه‌ای برای نظام هستند  حسن نتاج صلحدار، نماینده مجلس:
🔹
نگاه ما به رسانه‌ها به عنوان پشتوانه‌ای برای نظام انقلاب و جبهه مقاومت همواره مثبت بوده است و رسانه‌ها می‌توانند نقش تأثیرگذاری در تبیین مطالب نظام و انقلاب در شرایط فعلی جامعه ایفا کنند.…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/675133" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای المیادین: کویت و بحرین از جولانی خواستند تا در صورت وقوع درگیری زمینی با ایران، نیروهای جهادی خود را برای کمک به این دو کشور بفرستد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/675132" target="_blank">📅 15:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=HzKfe4DoPPvO7-lM3c9JQbO3AeXv1LCoIrqJefPSleWArt-JGlYE6ikqSoApEt7MfxigsXr9OjPqbbuEEjRHpD_EZxURXFXzUEhEtrac_zhf1UL6J-YCiQWtIV1GsIhSaqBmRAAW42NLrpuA18i-l_WtQhSqIH1PzszdRkOheiLkhvqK4rEdg-3QETeEF5kvRy5oRllskbKohrSx4OZnhRFVgirpSUcY_1FgIMJRgblzzJ5T9KdVmh3jdQYwAu66OLJGIfu8EUEgdjOR8e2S9-XLZv6afbDllWRkRrpz5vdXxciAnGNXbfnXkNVAJQM-j7PIlaN3y1R4Xd0TkS80rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=HzKfe4DoPPvO7-lM3c9JQbO3AeXv1LCoIrqJefPSleWArt-JGlYE6ikqSoApEt7MfxigsXr9OjPqbbuEEjRHpD_EZxURXFXzUEhEtrac_zhf1UL6J-YCiQWtIV1GsIhSaqBmRAAW42NLrpuA18i-l_WtQhSqIH1PzszdRkOheiLkhvqK4rEdg-3QETeEF5kvRy5oRllskbKohrSx4OZnhRFVgirpSUcY_1FgIMJRgblzzJ5T9KdVmh3jdQYwAu66OLJGIfu8EUEgdjOR8e2S9-XLZv6afbDllWRkRrpz5vdXxciAnGNXbfnXkNVAJQM-j7PIlaN3y1R4Xd0TkS80rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه سه: ۱۰۰ روز است که هر بار اسم بچه‌ می‌آید ناخودآگاه به میناب پرتاب می‌شوم/ کسانی که دم از حقوق بشر می‌زنند، کودکان ایران را به خاک و خون کشیدند. ما از خون کودکان میناب نمی‌گذریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/675131" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
‌
سخنگوی نیروهای مسلح یمن: پدافند هوایی با یک گروه از هواپیماهای دشمن که وارد حریم هوایی شده بودند، درگیر شد و از انجام جنایات بیشتر علیه این ملت بزرگ جلوگیری کرد
‌
🔹
دیشب ۲ عملیات نظامی مهم علیه تأسیسات آرامکو در جیزان و ینبع انجام دادیم، این اقدام در پاسخ به تجاوزات سعودی علیه شهر و بندر حدیده و جزیره کمران و همچنین ادامهٔ محاصره مردم یمن و نقض حاکمیت یمن صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/675128" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: آمریکا می‌خواهد داعش را فعال کند
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا پس از آن‌که در مذاکرات، حملات نظامی و هدف قرار دادن زیرساخت‌ها به نتیجه نرسید، اکنون به‌دنبال فعال‌سازی گروه‌های تروریستی و تهدید زمینی است.
🔹
آمریکا روی نیروهای داعش و برخی گروه‌های مستقر در آن سوی مرزهای غربی حساب باز کرده، اما هر کانونی که برای چنین تحرکاتی شکل گرفته، توسط سپاه و ارتش درهم کوبیده شده است. اگر آمریکا دست به تجاوز زمینی بزند، فرصت مناسبی برای وارد کردن شکستی سنگین‌تر به این کشور فراهم می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/675126" target="_blank">📅 15:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675124">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCP3mISzlHHX5UG92ao9aMKbAyOAGqsmqwJEO2Xhx6wp0kpUAX39m7t8r_FC0rOQ_0ijDCXSv02vk3txdSVZ8I_tggTbWTFJdbSB15vhgK4iSvTGVJrjejbFaPa8WOAGR6KnWvBAjQLy-aaQWiVxvMlkQX1kENPv_tQgRSKxfydxMIR1RGbsEM6KxY5udkEiA6ZafHUXfR0eRgXcp9dN8rsCJCSyoKlq5aBrqnfm7AHKwd2cFafFp2oT9uoEhsslHmy8IkGHuqK1uLL06v6ZWerNpi-c283Z5YuEiYQxKYjNi9SfT4Eg9z7iv9uQk2QxFug6Udp5CsSOgJPj3wkTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد دریافت «عوارض تأمین امنیت» از کشتی‌ها؛ طرح جدید میانجی‌ها برای بازگشایی تنگه هرمز
🔹
به گزارش اکسیوس، در پی تشدید تنش‌ها در خلیج فارس، طرحی جدید از سوی میانجی‌ها پیش‌روی ایالات متحده و ایران قرار گرفته که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و مهم‌تر از همه، پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است.
🔹
طرح این پیشنهاد از سوی رسانه‌های غربی، نشان می‌دهد بازار انرژی برای حفظ ثبات خود، راهکارهای عمل‌گرایانه را به استراتژی‌های محدودکننده ترجیح داده است. روی میز آمدن ایده «پرداخت حق خدمات»، در واقع پذیرش این واقعیت میدانی است که تراز کردن معادلات دریانوردی، بدون تعامل با بازیگر مسلط این پهنه ممکن نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/675124" target="_blank">📅 15:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJoYLH8QMSbK0azvDbmVZVR8w_RkjGXAVPvgSfmq6bBeNrzeuMXvUbP4EcOWyJit9yQ32dxCoJbk8P5mHVrWuSqIGp1YxCraDhSSOxjI2BAwh1uOPNrR1OLD8SjZ9e-zU4exqN8bV6KJx_oOGU7UD0TkhV5diOI__-4Sun4ManZtBzRi0mkHTGwJ90AOLjc67R3e83MFi-sQOI4ehxtpFt4yOqZfIngvnr3H4_VyCISBIdfzz9cqFM0zDRcmvY42jrqcKAJDCZzscJacstdxQ3Izn2PlmElQoh2zrNEMCBbRIA77sRQBymv_cuNbpA53jlbiEf86QONJh3OiVqeoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivkG3GiJqDoyWJGkbbnNij3eUoMiVEAvVl5pMiHvWaYyFSG8ckngnefHx1qBc8u-88jvdO_JvBwrsc6mYQNX3rBtLufLXbKT7Z_2J3CTqC3W7XIq_rghsuu8O22eZsjw5FjOqR_h6sEY8zo7uWtfGCXJFHvbJpmVVJ55CAh2sYJmuDOXk545yHnzUH_Ory2nUu6yESpj2yNXtvEhqVDHMA4eoaKxQpK7GJiZy5opd2XqEj3QjsC9ey5A60oQi7Z6DHVMRFwiN0-Htat4azw8KUOp5j-k3cnqfpZx4MQI7ZFzyAhGZQWWTeVfK3HNTZKXcKVMIbNSpo0vAGy0-5i8NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صادرات ۱۵ محصول کشاورزی آزاد شد
🔹
وزارت جهادکشاورزی چهاردهمین فهرست جدید محصولات مستثنی از ممنوعیت صادرات، شامل ۱۵ محصول را برای اجرا ابلاغ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/675122" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
موشکی که پدافند آمریکا را گیج و سردرگم کرده است
وال استریت ژورنال:
🔹
موشک بالستیک «خیبرشکن» به ستون فقرات توان موشکی ایران تبدیل شده و تهران با به‌کارگیری تاکتیک‌های جدید، مسیرهای پروازی متنوع و حملات ترکیبی، تلاش می‌کند سامانه‌های پدافندی آمریکا و متحدانش را سردرگم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/675121" target="_blank">📅 15:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISuu8txOs9aEvedJNajVoQuNDkJABBLJJr1G26pHRhmBLmqCcHmV0lAY6AtW7xZg9u62fTB_LnwjvsRqAl6_xMAMzsJrge-TbYN_LGMfBILyrjlj0yCA_ECoC3QMm3l5XcjPQNZBJGK_ijm0-6ucCZFzCyyXiBQk_nsWmgLiE3Y80x6xOBKwmycxQx9ESUKUwPZkPlfBk5Wbwv-5TW2I1G9AwqwOg_E7OGwy5Uf7BdpTc9f0SHZ_TB1yilJrAziJNbFq6Vxa9speu5E6HDSdK_JdiDk2c_f-gFvu2E-2GU9v_Z35sVDCOZlon1VV2uMOatiSrTwJ_kS6CHG2A03Msg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیباترین شاهکار خلقت؛ شکوفه‌های گیلاس‌ ژاپن
🍒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/675120" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675119">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLXYNZD0HHEjD9ZhHPvCSH4BsXHQr_d9vVJKsZvP0tgXVc5MY74WC3tVn4ogi5OC9ZSo4-t8FfCxkyja7wXOHmal0lXt1A_mdAj3EVSqVkYKUwPqYEGIdlzmp-cpwYCr2PzitrdvCh1tj39dExkBidO3MSZNc0-p_Cj1VxEHHDSAn5FXtnbM5t8-ciGR42oTtdsdFfS1QWE38eEi5WnAxYMU4ZsggLsmKzNCH7FF5qWs_3B_WNCOf53tfEqQy4p0sf_NWIJQx3Wdu5vq9x34Uk8WmHHC7VCRcJ2SxpF4jG40X-l9Zg-A0J7MkmE7FsuReSD5aHWTZ8Odf_8v75q7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحاشی مخفیانه ترامپ علیه مقامات ایران
ادعای وال‌استریت‌ژورنال:
🔹
ترامپ در مورد جنگ با ایران بدون پایان روشن صبرش را از دست می‌دهد. به گفته یک مقام ارشد دولت، رئیس جمهور نسبت به دیپلماسی بدبین شده و در «حالت انتقام» از تهران قرار گرفته است.
🔹
به گفته شخصی که نظرات او را شنیده، در جلسه اخیر در دفتر بیضی شکل، ترامپ به شدت علیه رهبران و مقامات ایران سخنرانی کرد و آنها را آشغال و دیوانه خواند و مجموعه‌ای از فحاشی‌ها را آغاز کرد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/675119" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675118">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f2466bb3.mp4?token=tYZzYcrBtetrZxCWQUQqW84cCepQziF1PNJT23AoEK-GeiXtT_vvLU62ZLCbwPsT9FwryHkOwbkPFpn1-AvWRlJdzIqZn51RwYJlvfF3MEedhahL8Hw3SIzDZ75LpNEPLdtNF9XwrrZ4CPkRU5aqYIHV9TjpIjamJuLxZ4RmneeC92X80c6nek4Kwbd7Qj1MoF1NcYlq5jmpPJ3llPcawJ_ALKrsXoBvxsgkyuPJOr7UG-sDCeR6BYugr76V9fR-NfsB5AzXnRGbLfviedHRfhA4ZJ8LMPwA6OBTMDuLfAXKsYYWAqegb55E0nNNaNwMjeWq2VTkfs4izZ6vMuPYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f2466bb3.mp4?token=tYZzYcrBtetrZxCWQUQqW84cCepQziF1PNJT23AoEK-GeiXtT_vvLU62ZLCbwPsT9FwryHkOwbkPFpn1-AvWRlJdzIqZn51RwYJlvfF3MEedhahL8Hw3SIzDZ75LpNEPLdtNF9XwrrZ4CPkRU5aqYIHV9TjpIjamJuLxZ4RmneeC92X80c6nek4Kwbd7Qj1MoF1NcYlq5jmpPJ3llPcawJ_ALKrsXoBvxsgkyuPJOr7UG-sDCeR6BYugr76V9fR-NfsB5AzXnRGbLfviedHRfhA4ZJ8LMPwA6OBTMDuLfAXKsYYWAqegb55E0nNNaNwMjeWq2VTkfs4izZ6vMuPYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقرار استارلینک نسل ۳ با استارشیپ و انفجار بوستر
🔹
اسپیس‌ایکس با استارشیپ ماهواره‌های استارلینک V3 را مستقر کرد، اما بوستر سوپرهوی حین فرود در خلیج مکزیک منفجر شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/675118" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمبود پرستار در کشور به ۱۱۰ هزار نفر رسید
محمد جمالیان، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
کمبود ۱۱۰ هزار پرستار در کشور به علت‌های توسعه تخت‌های بیمارستانی، بازنشستگی و ترک خدمت پرستاران و مهاجرت نیروهای ماهر است که شیب ملایمی یافته اما همچنان ادامه دارد.
🔹
مطمئنا دولت مقصر اصلی مهاجرت پرستاران است، وقتی درآمدها پایین است و کشورهای حاشیه پول خوبی به پرستاران می‌دهند آنها هم به آن کشورها می‌روند.
🔹
دلیل اصلی مهاجرت پایین بودن درآمد پرستاران نسبت به هزینه‌های زندگی به‌ویژه در کلان‌شهرها است، کار در بخش دولتی جذابیت ندارد
@TV_Fori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/675112" target="_blank">📅 14:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe30add31.mp4?token=QZ5KZUt4b_amHqwyCjtKKDNVNQJP0Pzi05FcA9s4Ibx5fA8_pNIUJaiG1afBAicEU7xVXvbN_B_oKfWNbxUhP1ZVrufiMlqh2KhanaquY0T1i_1BOvsptr1AoNUucDqxvJ4QBLc-laE1r_pNmVpsTrBZJOgZepJklPy1c21gDD_-4GK_fkYHZyqMym0KvpWCTm5LXS2pmy-mtIXfguVnewNksludFK7OOa2vkOCkkPkWzIVnwFDkqrvfFGqF4jK3sdqtvSYd0tbRTt4882xzN4ri7KNwTzwEyRAcUH4oY-039lLIsP24sbAFD4rCVXKquQ8Z7a6712_b3CxaxT4iIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe30add31.mp4?token=QZ5KZUt4b_amHqwyCjtKKDNVNQJP0Pzi05FcA9s4Ibx5fA8_pNIUJaiG1afBAicEU7xVXvbN_B_oKfWNbxUhP1ZVrufiMlqh2KhanaquY0T1i_1BOvsptr1AoNUucDqxvJ4QBLc-laE1r_pNmVpsTrBZJOgZepJklPy1c21gDD_-4GK_fkYHZyqMym0KvpWCTm5LXS2pmy-mtIXfguVnewNksludFK7OOa2vkOCkkPkWzIVnwFDkqrvfFGqF4jK3sdqtvSYd0tbRTt4882xzN4ri7KNwTzwEyRAcUH4oY-039lLIsP24sbAFD4rCVXKquQ8Z7a6712_b3CxaxT4iIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنوب؛ قصه‌ای كه موج‌ها هر روز از نو روايتش مى‌كنند... #همه_باهم_برای_ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/675111" target="_blank">📅 14:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675108">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای زلنسکی: شناورهای مرتبط با ایران را هدف قرار دادیم
🔹
رئیس‌جمهور اوکراین امروز در پیامی ادعا کرد «در حملات دوربرد خود در دریای خزر به نتایج بسیار مهمی دست یافتیم؛ از جمله شناورهایی که برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/675108" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675107">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تیزر قسمت دوازدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نرجس اربابی که بخاطر بیماری زمینه‌ای، در میان روزمرگی‌های زندگی، به ناگاه روح از جسم جدا شده و در مکانی از دنیای برزخی پاسخ دهنده و نظاره‌گر امور مرتبط با حق‌الناس از جمله حق پدر و مادر و همسر می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نرجس اربابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/675107" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675106">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwfiD-SS3LZhdfaFgv3zNS3oz6Ee20Z1XlGsfEFxhtpPJrn7NSXvzkvz80s9AEsguQZ7YazIwrJ9CUEJ3dgVoB08JhIlEqKbzY4_OQEoSjes3aj6xHWv6drJYy203Y9sr4GZ0eEnOp1GCvug8Rh010hc_0_gp-AgI-fHrpLF2IW8dodF-iiVMyuRaMNXiMdaExva20yMdlW3CT0acw2x-cd0YL7NRLMoSHzA4-P6SrEufAQlbECXHUOhjD9RZOVdbH3ZCHAChBtgVaUqWS-qd-aIdNSW8j7YO0NoG_IZ8lYkvW01hv99t0pSYjZmSomizmbrGtM5H1sX8iRgsET2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ کد کاربردیChatGPT که هر کاربری باید بدونه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/675106" target="_blank">📅 14:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675105">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iq_wi4Pp0N8QNH5fvI1pRgBZzYVp9QbQe_ZEgt1doVQ-9ZPwmtz9hZ0WutBfJBs9dkfCavky56O6HdMLOakfqav9nWuGojrIb2Kd7u8bTp9bxqESju60qmoCWQGtLyC4UkJA3zoE9XShpaV_eEPZhURn1sftdpVmPbGeN_zxTqfUEsH4giI6XVSK-MJ6A3FXNDIul7FU7K211ggoSOMJWN3aIVZeoXIZUqw6ll5PYmfnCwF6cYtMSTw3O3YvSiFG0hvSweIGJe4uw2CxA0HnDl-8IeZre4Ve63tnbqYNUe_fnQHP1EYFNDRNCyXLc13a-QVuJMR-EhRSOWiXg3Hnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر از این کتونی‌ها داری، این راهنمای استایل رو از دست نده
👟
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/675105" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675104">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEMhEuh9RalwHYYQMTVvqADOXLWEDGvBMkhc0nDQbv71_SEVz-2vK9rrQbKetWLaBPbkfDx4lCvKyQIgvx5fqiQOE4QlHQ9hNl4v7pwMHuuCKENEpkWKzP1r70Vs8PuYAgbkl0SeXEr0e55rXoKF9oczSw2Qm6vMMgH8E7YAdLJJfUbfgJhPRZfqq_KRafnTb3zGjjDDW045t_868-k0CDlWzYQQ85-IF_8xnHu40F6Ip0tSbRkFHE7L00naOOsBs7eOVyaIylFHJF6oXhyjwBHPQKIu8i4qD-UIHSevER6Sslui3C1v4yoFqK-_q6gyyh86lAL_3RNv-pxYRqfxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب بزرگ دوروف؛ تلگرام ابر برنامه شد
🔹
پاول دوروف، بنیانگذار تلگرام، رسماً اعلام کرد که تا پایان تابستان امسال، یک کیف پول غیرمتمرکز را به‌ صورت کاملاً بومی درون پیام‌رسان تلگرام عرضه خواهد کرد.
🔹
این کیف پول که با نام تاریخی «گرام» احیا شده، به گفته دوروف بزرگ‌ترین عرضه یک کیف پول غیرامانی در تاریخ خواهد بود. اگر این پروژه اجرا شود، تلگرام از یک پیام‌رسان ساده فراتر رفته و به دروازه ورود کریپتو به زندگی روزمره صدها میلیون کاربر تبدیل خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/675104" target="_blank">📅 13:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=cRsq1acM2lStKQX2PCE0Baf7ejX1Ahu6OUTxRdfCiDDy3Fx-tChNP2eMiPRSn4VX2Jl4vJRaThDloUty0ZHjUGzBJBI0OnFaAoG6ga5YyGgE-GjYZ-3O6ztgrO7b45kLpGwxSJQc0fDenVctsNb6RcdgfAdAeH_X9TDURF1giVIKwXrTLSgHmxO9ze04j04zQO7LfZwevvCU2ZaRIcykU-F4V6uTFzyaV7Tiub0OVK5GbaRDMuN_lLu-lo21CvOQrJtkyPrzjzktKtYErI-aMAPxihxC_QAf1n1y9cf1-bmKtrURT9LTLPy44ML6MPPIRGUWNbJGGjCYonK8CA4ZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=cRsq1acM2lStKQX2PCE0Baf7ejX1Ahu6OUTxRdfCiDDy3Fx-tChNP2eMiPRSn4VX2Jl4vJRaThDloUty0ZHjUGzBJBI0OnFaAoG6ga5YyGgE-GjYZ-3O6ztgrO7b45kLpGwxSJQc0fDenVctsNb6RcdgfAdAeH_X9TDURF1giVIKwXrTLSgHmxO9ze04j04zQO7LfZwevvCU2ZaRIcykU-F4V6uTFzyaV7Tiub0OVK5GbaRDMuN_lLu-lo21CvOQrJtkyPrzjzktKtYErI-aMAPxihxC_QAf1n1y9cf1-bmKtrURT9LTLPy44ML6MPPIRGUWNbJGGjCYonK8CA4ZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: آستانۀ تحمل ما در ایران تغییر کرده است
🔹
توانایی حملات پیش‌دستانه به دشمن را داریم و آن را در عمل نشان داده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/675102" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04ebc19f4.mp4?token=osUMpzTyzrhk0Ew__uFBuCx1zKAumKIPjOOq-miLS05QT5MsPWTwXTBANcA5UVlYliDDXdTK4ZKogNiLKZ1zIUTd0x3p1Gu1AlA4MUo8-EHlLuiNJW9N95UZ1QAUBNjputybZ9WsBp5rO53A5jU5HPdjyAj9jHlHJPkoVvPq7QTU3X65VhZZRgzYyCqFV1RREt5IClyerrp4RBYKadbd4DuwoNUtSD6tHUANEu33B-Xb3l8KvK-9UzFUlOF09Zyz1sSBXlL1l27HLyYZwDXtVq5e-L8tZSlWEIl-DrXsbH3sfOwJP2eQg3MRHuUjiRr-Wk4B4TBSePLZJe7h1K0Vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04ebc19f4.mp4?token=osUMpzTyzrhk0Ew__uFBuCx1zKAumKIPjOOq-miLS05QT5MsPWTwXTBANcA5UVlYliDDXdTK4ZKogNiLKZ1zIUTd0x3p1Gu1AlA4MUo8-EHlLuiNJW9N95UZ1QAUBNjputybZ9WsBp5rO53A5jU5HPdjyAj9jHlHJPkoVvPq7QTU3X65VhZZRgzYyCqFV1RREt5IClyerrp4RBYKadbd4DuwoNUtSD6tHUANEu33B-Xb3l8KvK-9UzFUlOF09Zyz1sSBXlL1l27HLyYZwDXtVq5e-L8tZSlWEIl-DrXsbH3sfOwJP2eQg3MRHuUjiRr-Wk4B4TBSePLZJe7h1K0Vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرسی که به‌جای فرار، بغل دامپزشکش رو انتخاب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/675101" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
