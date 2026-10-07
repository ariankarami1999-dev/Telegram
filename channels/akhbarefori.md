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
<img src="https://cdn4.telesco.pe/file/h3iGs57JPlXd8JFw4KYoHB4JV9MJn-8cqWkcvL18Y3gfA2ZoQtlay8ceD83V2Z_W7zBr4JP8R8jWN2kLuN5LxD4jYdFst6T9Wk8p0oolRIwv_JHoDSNAQNL57V8PB3i7Pl5uwgBUJHVFyitnjtQ7nBa1thoTjNT5oeNE5ZeoIFMANeoLjlsTDl7svl180DJWTLh0N-jYgHuFRQ4y0TB9vHhOkVjGq2b7pqc0fKI8nAyn5eNJ1WgMJ4KBnxpMhKFGVYvzeNK6Fw8N5kyXZPGnkP4CxKmDT6bVOe4vofgfOZYO64Px06QGC6lQ4MIYhzyf5uGFaqeS_FuXK72Otu9vZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-696520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0SchuJoy8eIkdsOD-e-zj-YY6sm3yhVpeSB5SDomdhBY-cX2vA9zscRFQtaZ55gtN87gIFRj0M76_1227nm-EfzEIaFJslFFIEkQSjG3sAOU-bHSicC16ABH8Cmhx9FwOITsvMMIpEB9e9DnaCYzmsVujTRhaR4TG_nCMZF8tZJTmtq14fD14md1W0bquTg4eTSZiWOYgqXu_lk33io7mJJ_DK2e1Y5z6nr6PyNEYYPP6ljC97jA4_jdr4TIGqQ9SXAPZkO_gHxNzJoBne7S3MWRMZArWqf4bz_N6qqTY4AbWGUu819jVa01m7omlqecM4y_l0nfNh0DRmzK7dJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تک رقمی‌های کنکور ۱۴۰۵
موسسه عارف
🫡
💡
فقط درصدت مهم نیست
💡
جایگاهت مهمه !
🎯
هم مسیر رتبه‌های برتر
🎯
از همین امروز شروع کن
💪
موسسه کنکور عارف
🫡
| موسسه رتبه ساز | کل کشور
کنکوری داری؟
پس این لینک رو براش بفرست:
👇
https://t.me/+xVKhaZN3zi41OWZk</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/696520" target="_blank">📅 00:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG09MRnSgGZtnVOuFxRJDowGsRia97fYhHIsJNYSnbeBUFeMA7V_bSTD-wIQUywn7hMXhN64BERCsn03kHYdwvq_puFVK3oMKLz9drni7t80Y6ronLRgwr_akdlqrYJ5G3JLZhmuYGSoW6feBBtGLGHyDshjkuTOsH2eqjnWLfQCRIuUy14OfRM_VTWPXT98ii2aunMY_KNoNQygJTJc6u4ihSMVTD762IExX-LeCLi3lQjuPJHLXeSJ4FPJ9AITQIWNj1hiWoXA3_ulzKe0qoYkU-dO85qn7FQrLGxfECCxZjwyIjDLpWbXaqUFaGhXLENEo08RWX7VdLtepPyQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af97c4e9.mp4?token=oFVjD0ep9YV7Rw1s6rGz_Q42Dcp6T_NF1ZVl8XgA5wvE3SPnDizVX5_1alYyTZwhkf_i0j35AFHfTZ2wCvdlszf9oc3b__85JzISnm3IEOQ94_0smEjZ9QTODtJOymHSFKAjyqd45zCw3nouIGbhs8Nthl3s2elIVNIPYkRXQZ_5y5IelDQ4T1EalPJfbzFrvFhA1kchMmhcar4M1OAjN867zLp4-B1xclU3bse9GX9iAe-PQPN_JqDs-h9mfVAwwSIUfo06_Nw3TAyYw-vhgEDJRaCPCcMtJCt58JExnZLksTgmEAXcQ_h4cdfth82FZLrSBUSxcnKOgNaIXQVqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af97c4e9.mp4?token=oFVjD0ep9YV7Rw1s6rGz_Q42Dcp6T_NF1ZVl8XgA5wvE3SPnDizVX5_1alYyTZwhkf_i0j35AFHfTZ2wCvdlszf9oc3b__85JzISnm3IEOQ94_0smEjZ9QTODtJOymHSFKAjyqd45zCw3nouIGbhs8Nthl3s2elIVNIPYkRXQZ_5y5IelDQ4T1EalPJfbzFrvFhA1kchMmhcar4M1OAjN867zLp4-B1xclU3bse9GX9iAe-PQPN_JqDs-h9mfVAwwSIUfo06_Nw3TAyYw-vhgEDJRaCPCcMtJCt58JExnZLksTgmEAXcQ_h4cdfth82FZLrSBUSxcnKOgNaIXQVqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💆‍♀️
خستگی عضلات رو به دست خودت بسپار!
⚡️
ماساژور تفنگی شارژی
JIHAM
؛ یه همراه حرفه‌ای برای بعد از ورزش، یک روز پرمشغله یا وقتی عضلاتت حسابی خسته و گرفته‌ان.
😍
▫️
۶ سطح سرعت قابل تنظیم
▫️
۴ سری ماساژ تخصصی برای نقاط مختلف بدن
▫️
شارژی و قابل استفاده بدون سیم
▫️
سبک، کم‌صدا و مناسب خانه، باشگاه و سفر
💰
قیمت نقدی: ۱,۵۹۸,۰۰۰ تومان
🔥
الان بخر، بعداً پرداخت کن!
💳
امکان پرداخت
قسطی در ۴ قسط
بدون نیاز به پرداخت کامل مبلغ در لحظه خرید
😉
🚚
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
اگه دنبال یه ماساژور کاربردی و حرفه‌ای برای استفاده روزمره‌ای، JIHAM می‌تونه انتخاب جذابی باشه.
💆‍♂️
✨
https://memarket24.ir/product/fast/64852/180124/</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/696518" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4xBWIFzFabFHq1jKFQFIZ_rFaIZVGV_ixfpCHnsfiF-C7Dy_VbKFVuPlnYrzDNGlowPuR3m2LoToob55k8OtO_KhAZUTp0710SQKNxQMlX_PjPvMtVyIKqRM6DHADjmQqi0JRYTaguHj1Px7247unou48PBRFvX3kHRkjLWZVpQ4gRwl4-t7VvPes2IWfnWpnXW7dwrBcOo49GWboI3w3XQ6BmHfELDeAf79GoohQieiuWjSZ8rHoVYXiMXHNFZJF8h8Nj84IR90tMh7snLdny0NLyQ1Llrw41A1X0VhqdBc-eaP9Yq5bsC1S5dWNBLqM0-LPkjjrk0Cmx5rHvYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اشتراک پلاس بخر؛ آیفون ۱۸ ببر!
🎁
⏳
فقط ۱۵ و ۱۶ مهر!
🛒
هر خریدت از
دیجی‌کالا با اشتراک پلاس
، یک شانسه برای
آیفون ۱۸ پرو
علاوه بر اون، با خریدت
۱۵۰ هزارتومن طلای دیجیتال
دیجی‌کالا هم میگیری!
✨
😊
پس
وارد لینک پایین شو
، هم تخفیف اشتراک پلاس بگیر، هم تخفیف خرید کالا!
👇🏻
👇🏻
👇🏻
➕
از اینجا خرید کن
!
🛍
✨️</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/696517" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu0YFvZEArpXoSVD80H6mkMAivegjCFoooYXSIH5jmmCiTuEArDe84UwryMtG-tFnvO_a8wNeKUKaZ7UraifeQnYfmeV7W9zyK88tHy-TS8frKlDc5Xbc7pIt3GVeVgrnf215hPPQ78PnCVd52uNY7hDcBTqkI0P5_dFmsvVVEdAnjKe0z0bAzjwNt6ajLM2xjfDJxtDEVqkvTOpSkTITsf9dIbQ3f_CUavV_DqLpukTTmlop7-gkETGugZOXoIzBGTQolCsEQ9Cj6NF0ZtaY19wUHjciNspPJMN9qQ_a8Q1naZTXHEO8mzboNtriNqmuaGBSwD0l2QfieX3LXI42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با دکتریاب، دیگه توی صف و ترافیک، نوبت دکتر نمون
🌟
تا حالا شده برای گرفتن یه نوبت ساده، ساعت‌ها توی ترافیک بمونی یا پشت خط اشغال مطب کلافه بشی؟
ما توی «دکتریاب» اینجاییم تا این مسیر رو برای همیشه کوتاه کنیم. فرقی نمی‌کنه دنبال نوبت حضوری باشی یا نیاز به مشاوره فوری تلفنی داشته باشی؛ با دکتریاب، پزشک مورد نظرت فقط چند کلیک باهات فاصله داره.
✅
چرا دکتریاب؟
دسترسی به لیست بیش از ۵۰ هزار پزشک متخصص
رزرو نوبت در کمتر از  یک دقیقه
امکان مشاوره تلفنی با پزشک، بدون نیاز به خروج از خونه
صرفه‌جویی در وقت و هزینه شما
دیگه لازم نیست نگران شلوغی مطب‌ها باشی. همین الان وارد دکتریاب شو و سلامتی‌ت رو به زمانِ ارزشمندت ترجیح بده.
🌐
همین حالا نوبتت رو رزرو کن:
https://doctor-yab.ir</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/696516" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a492ad0ba.mp4?token=p7SlpYvWF2p8RSdAQ3uRqc3t3em4bf3v_3OpJNr42AwunJAXmBdeIvAv4YrDvT6U-PParOxHO2Lsi2QOMMjWj5fk246A0ObOX66-aTwE8InkxgzEITcEBmL4358_WNOmOUZP-mxuEAkOuzPcipwRvAchDc9k41hXPR1gEzdh209nAb89mSwE9TbjY2R9fHqxg17yNkBUWfvp2jKETcXGmDTKoyt81lzkjIKv9jYg7NQbEPWTA19RiBlmYmjM6IHAcF3zJdmYgWvL9E7ZH0vxkhJHFSe6XYGimZd-czfL4X6dd6nZUZoppiElcqCiVgVjI3wszkQALZWOzfCLLJLyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a492ad0ba.mp4?token=p7SlpYvWF2p8RSdAQ3uRqc3t3em4bf3v_3OpJNr42AwunJAXmBdeIvAv4YrDvT6U-PParOxHO2Lsi2QOMMjWj5fk246A0ObOX66-aTwE8InkxgzEITcEBmL4358_WNOmOUZP-mxuEAkOuzPcipwRvAchDc9k41hXPR1gEzdh209nAb89mSwE9TbjY2R9fHqxg17yNkBUWfvp2jKETcXGmDTKoyt81lzkjIKv9jYg7NQbEPWTA19RiBlmYmjM6IHAcF3zJdmYgWvL9E7ZH0vxkhJHFSe6XYGimZd-czfL4X6dd6nZUZoppiElcqCiVgVjI3wszkQALZWOzfCLLJLyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معین در آخرین کنسرت خود نه تنها اجازه ورود پرچم شیر و خورشید را نداد بلکه قطعه «حماسه خرمشهر» را هم اجرا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/696515" target="_blank">📅 00:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdkHRtj4svaH8QfisUAsFQMdOExtAq2HqjJMLO1lbj1F8t53HFvGIyAKe9KQmO6irZ0oBNGb9A3-sgJYI1PdLPGJenByndEx5kLFymHLzWKzXqaCGdOFo84_mNb7PYkfsinyXKQ-9c5Urt_vOLO0P-7Um7uAjZdiAgA2-oQcXRHhe1MRsA2MQ4_ucdK9wXYqCi6fxfbdwuaJwWa1At_uuisKyX5f58LHG2_4Ss2K4oHDOi9w7Q9tKnvsZTeP-uHqwmtmEPQcU-vRjFwjvhIfA5qxsHrYzgcQZo5UV8pCNGk0bjSZS48qs-mDPU5jQMYExyGV7M6hM-WSaYbTN4bAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoUBlOyK9_QFqpMT8QY5clBU8hIiFuIIHZWDT1rU5lrvuFCT7WWN9ikD2qwYAADC5i0suZh6kT-Cx-gH5xgLsp4u5yAR3tQOBSf345XFG5HlFv16l8JmL016CmxvSvkb0BmdUA8Tg7LUGNLGxBWSvUQe-ZnotodAurxhJvjAfE-XuKX4nMdf0gh_WlRNx2yqNRaxUPLPn0OpOISYgJNUHIzpmbkvvFDJZaHK7my4x1pAEik3beZW5S7ySdWQE-29UWaeuFTfm2aGx4E-aiQR3mW164Qku84vX-jmI6xh8vQtZwbfneiHFyUBgaaAHX013n2QjltN-d4INUj0Ye1emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZZPJLrQyCtwijk9TTTt9Jevdi7LkLy3scL3AjQRoiPzBKikudOGDRhjwjqg5Tu7JTpEH1ePEqXVqdT44D3v-3OubdwsSoXbjLx_y0jfyuRU3s2q0HUw76VZ12QtbTbo1VSmer7fq94iBcxa6K4qHGJh02mHDPH4RERzk6WAWxLRCZkwpz1nts2R47-A1aMJIFIsE2KQsD3Z-YYIP97GkH40mAceNKdRj4HMosvSmiOXvHxd7hitjnLrYb4ZbgmSmK58n04PhQizJ5SS74ZNTl49nDca6jRwgcMVQEJJQnSSAAbpySfKb3qiNZ8aKh6nQdh7XWQDgJJ0pBmT2Jb4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkNfkpLP8RzlXhKcGjEBDSJNw1ui27wB7gE0Ugv03j6tbazikkeCM1ZYKMNBmYq31xCUypte_U120XHoOIBzR9ZCrzlx24bCkOS4XEhjPTmYhwm9h_pb-ai4NTZasKBfhGDxcK8jcYj7uVa9yqO2ZHBEQ28XK41GRcxizj_LPn_vQ5vJTqvDTiNsvhdSDNgQayeiRvIKZJ7hnoZMKBDgEuX8bS3axfOh5rRzCR8naTmZUmurWKRQHn1qcbqoI_jN8KZmg59k19fhW4u9BMvQrtVTJstY67sr8S6U0bKbEZawnPQD6LX5a3aK-fHyXU-NKGJZ-zYqxzujp47VhW8erw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناسا یه سحابی بزرگ به شکل قلب پیدا کرده؛ این سحابی حدود ۷۵۰۰ سال نوری با زمین فاصله داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/696510" target="_blank">📅 00:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: شروط ایران برای پایان جنگ و بازگشت امنیت به منطقه به‌صراحت اعلام شده و پاسخ تهران به پیشنهادهای آمریکا نیز از طریق میانجی‌ها منتقل خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/696509" target="_blank">📅 00:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ee5495d8.mp4?token=dP6wMby9lGSqALwdXLs3esEP-oaBk4GHgRPMwP-i8EcpX8Tdq8rSILwghv4ABSkh5qJHulrvcn8uSHduvA1c48c_p_Gf-_4ZkDfcdQc1reGAxOLYuwFVy-uSOc95PZUhBCsscsuBRntGFjKS2GwaRyUwT4KR8OPCjFLYaHqK53bMYJHQr_Q5U7NPoGC4clBX7wX3emGj7aq3iPZdkZdFGsSk_6oOZbI7NMrxSajy4r2rLX0hKgM83R6i0TXKNK26XC5-7YuVRT9RpQCcRFl5Rv64xLTzFGvniMED9iDWcrikLa7KAyVG5Y2lGmxp3BLXgKzIcOEg9wURtqLA5ELvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ee5495d8.mp4?token=dP6wMby9lGSqALwdXLs3esEP-oaBk4GHgRPMwP-i8EcpX8Tdq8rSILwghv4ABSkh5qJHulrvcn8uSHduvA1c48c_p_Gf-_4ZkDfcdQc1reGAxOLYuwFVy-uSOc95PZUhBCsscsuBRntGFjKS2GwaRyUwT4KR8OPCjFLYaHqK53bMYJHQr_Q5U7NPoGC4clBX7wX3emGj7aq3iPZdkZdFGsSk_6oOZbI7NMrxSajy4r2rLX0hKgM83R6i0TXKNK26XC5-7YuVRT9RpQCcRFl5Rv64xLTzFGvniMED9iDWcrikLa7KAyVG5Y2lGmxp3BLXgKzIcOEg9wURtqLA5ELvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی نفس‌گیر از نجات یک غواص که پس از شیرجه زدن به زیر یخ، تنها چند ثانیه با مرگ فاصله داشت
🏊‍♂️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696508" target="_blank">📅 00:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Live stream finished (14 hours)</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/696507" target="_blank">📅 00:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcqFa4ahfOSZXKhCNBhajbB9EkXsxmN5wjeuy-1JsgNXlVQrRzCBC2KBLC0sLnPExLOcQg3GDPJ6SFtDzGiKm29g0LXEAAEODBM_sg1UZkOkEgCodnx3UpBNX5cMdgsQdSFwFxb6_CAThXF286mhPjrkdBm0u_rvPG8x638X_722is-ndPLyergVSccC7k-8r27TlDjUf693QIefIBCgcyXPlXA04qCTYw5MuIRcGuEujhfrOaqiiWQ9QvB8eXXUJ0spmgm23qKLKYvVTAIwKT7SU12lzrBf9iXk5RT-U3Shqo_ZNDY77ZwGSnNOvK9qwqAdDgQj3sqLS9AvfjKRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/696506" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696505">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: شروط ایران برای پایان جنگ و بازگشت امنیت به منطقه به‌صراحت اعلام شده و پاسخ تهران به پیشنهادهای آمریکا نیز از طریق میانجی‌ها منتقل خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696505" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
خبرهای جنجالی را در وبسایت خبرفوری دنبال کنید
🔹
🔹
لیست ۱۰ نفره سیا از مسئولان ایرانی؛ اسرائیل نباید این افراد را ترور کند
👇
khabarfoori.com/fa/tiny/news-3250587
🔹
آمریکا شروط تازه‌ای برای توافق با ایران تعیین کرد | ونس از غنی‌سازی عقب نشست؛ پنجره توافق با ایران باز شد؟
👇
khabarfoori.com/fa/tiny/news-3250718
🔹
رتبه فرزندان مقامات ارشد نظام در کنکور؛  رتبه پسر رهبر انقلاب چند شد؟
👇
khabarfoori.com/fa/tiny/news-3250579
🔹
خودروهای برقی در چین چطور کار می‌کنند؟
👇
khabarfoori.com/fa/tiny/news-3250764
🔹
زنگ خطر «مرگ سیاه» در ایران | طاعون زیر ذره‌بین وزارت بهداشت» | نگرانی از طاعون روسیه به تهران رسید
👇
khabarfoori.com/fa/tiny/news-3250513
🔹
صفحه اخبار داغ خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/696504" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT7tqOiXt64su7SUlRJIVCHyMTrFcXpT44aUIMir4W2K5nKJhzV0MEEfl9KVLI2jkMe7zlA3tGiGByIE3ysWtZr7p5n82BycEMjrRg6Cl8uxex9gXKSemCnV3099n9Wr5jvDL5jYn_XRpeievpAvp-Yzli4kjEiFmwQ2YFm4SnIKM68M0tQ85zZGow3OSzAxu9H61H1pCg-5jQu_NrldNT_-gq7GxQlT4vm8dHl6gpkHtnTFXojnb_vcKKKM4n2ICE5bi0SN1caqxstTA4uttBZRvomLq_hFUPQ55KOrOz_d_4zpkxuC9Dnn6gIgN3tqnVzDdd44SN0ETugVdTv8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/696503" target="_blank">📅 23:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=l_MQ4Z7-hsZf-I3ak3AoBmctAHAJsYvMZl2TgqUy1olbWY2ejIVZHYkNwZXbA_1YeT-KPAQ2ZmxZq9aMNM4B85_Fp5mV5AofH_Wyqx-1ONBxIkRtso40n-T6Oh8lx5YedaEefejDaPpOJLUZvR1dRpD-CGOakhdcihAJL0kKjEBKycFpBZpc6XyZU8MDjVja7WAi-38qwgP2dhayp_boYXS6Qipc3IqIWzpeHt1RtB-sdgA0RN-I8Grrt_Nqb1yvl7qD_4UqPSKe52EMyhnqa9NpgtVzOPfWVj9KmiOOi3BSD0pqzmJLHGrXdjrHyyk9CtFK3UJ94kElZzVsFrO0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=l_MQ4Z7-hsZf-I3ak3AoBmctAHAJsYvMZl2TgqUy1olbWY2ejIVZHYkNwZXbA_1YeT-KPAQ2ZmxZq9aMNM4B85_Fp5mV5AofH_Wyqx-1ONBxIkRtso40n-T6Oh8lx5YedaEefejDaPpOJLUZvR1dRpD-CGOakhdcihAJL0kKjEBKycFpBZpc6XyZU8MDjVja7WAi-38qwgP2dhayp_boYXS6Qipc3IqIWzpeHt1RtB-sdgA0RN-I8Grrt_Nqb1yvl7qD_4UqPSKe52EMyhnqa9NpgtVzOPfWVj9KmiOOi3BSD0pqzmJLHGrXdjrHyyk9CtFK3UJ94kElZzVsFrO0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فقط یک چراغ‌قوه نیست؛ یک ابزار نجاتِ همه‌کاره‌ست!
🔦
⚡️
🔦
نور LED پرقدرت
برای روشنایی در تاریکی
🔋
شارژ USB + قابلیت پاوربانک
برای مواقع ضروری
🧲
مگنت قوی
برای نصب روی سطوح فلزی
🔨
چکش شیشه‌شکن
برای شرایط اضطراری
🔪
تیغ برش کمربند
برای مواقع ضروری
🚨
چراغ هشدار
برای افزایش ایمنی در جاده و شرایط اضطراری
🔥
قیمت ویژه: فقط ۱,۱۹۸,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
✨
امکان پرداخت
قسطی در ۴ قسط
یعنی لازم نیست کل مبلغ رو یکجا پرداخت کنی!
🚚
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
🔦
یک ابزار کوچک، با کاربردهایی که ممکنه یه روز واقعاً به کارتون بیاد!
👇
برای خرید کلیک کنید:
https://memarket24.ir/product/fast/30291/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/696502" target="_blank">📅 23:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7750f552b.mp4?token=Dk4Fho6R4wkA0Gwm6HhW2eJn5TR7mPYMJE1pIAu3jJct8ljsj1vfUvO51qloFZXxM300Zt10otgn7NXRTHh5Q0kzlDqnylZMhQseQhGeeOZsxz4ztzxM1JsN2Ognn4K76Pgfeh8LW_UkwU9cokhQF-idiNt-FkT9blsvPlgCXM3EVTvy0pCcfZyTp6lTr03BSkc1yZiI8nNMPLbClbjJKzY7ScHeENnZ5VwHKV2-kFYDSlH_NK51XBnX-OoTikKoxQI-m5XV7a2KhjIbxV2JqIpE2cnDOPBmnxMBPk26sJ2D_9O_f8rUWPp9WeB4PrVEDrMRlAQW7rCFY0wrAFYEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7750f552b.mp4?token=Dk4Fho6R4wkA0Gwm6HhW2eJn5TR7mPYMJE1pIAu3jJct8ljsj1vfUvO51qloFZXxM300Zt10otgn7NXRTHh5Q0kzlDqnylZMhQseQhGeeOZsxz4ztzxM1JsN2Ognn4K76Pgfeh8LW_UkwU9cokhQF-idiNt-FkT9blsvPlgCXM3EVTvy0pCcfZyTp6lTr03BSkc1yZiI8nNMPLbClbjJKzY7ScHeENnZ5VwHKV2-kFYDSlH_NK51XBnX-OoTikKoxQI-m5XV7a2KhjIbxV2JqIpE2cnDOPBmnxMBPk26sJ2D_9O_f8rUWPp9WeB4PrVEDrMRlAQW7rCFY0wrAFYEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از خانومی که بخاطر عمل زیبایی ماشین خودش رو زیر قیمت بازار فروخته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/696501" target="_blank">📅 23:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AicZW7m6qhz8eZwJfluGXHEEgPQHtR1ZStnGrJLN23jt6tc7X5eDT_oc9Q-Jx1CmvV3hWxLYHjeZQK-HNCYynHkQLZ9UNm_Zr0ywodXU6Xd9Hws3kB5IojJ9hvD3NtFRGD_Ujt2u0n8R_pAaKCSXwkvF62A2k1pY9nMMjDuy0rKPi2xF-fXSTJKEAIhQVYor5J5H1uqbAchf66If3GRD82Dv-M2lRlmq9GYfZHQbfdSZz4aAL2yxQnNrXr0Gbp1oAU2qxkEChkI0XYcYTY8BDQut0EdfwkUqERjpmtYLFHeC1ZE9ZfeiO_OLfWXdSBzA6Vc2HkgnvzC7qA6HCJ3hnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمای زیبا از «نوشهر» که بارش باران از کیلومترها دورتر دیده می‌شود
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/696500" target="_blank">📅 23:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U18-S33fFkFtNSCaaqn23lnXc7jvUNXyEBJC-ymYveoNk-dRHgLf-ANIzHOHKuSrFGBai5PlfbhLF42K4nMmOZdHnowmtwGUyolKGYi__aQ91s4vJxyP6uQByMdbStpBZPhXDRfGsUUKOM5JtsAPqYs2jSizDYWrcEfhFo9GiBlfqzOOyyNj-Vki1adKBJLCKZhzpl_otZum2mYjCl1c3QfK1h7J9j6xrji2VALrxXgu0ctM8PxOR4fq7TCDrrRkLlVhMZOHrHUOD-62QFQ0HvzPkouANDOtOuwJkxQouFhpAe85yU_NTqki1V2Lj5WHFrQ_Hv-wMnFMgVAjPxP0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل اصلی آمریکا با ایران؛ علم و رشد فناوری است!
🔹
دقت کنید در جنگ، مراکزی مثل انستیتو پاستور، دانشگاه علم و صنعت، پژوهشگاه شهید بهشتی، پژوهشکده نانو دانشگاه شریف، مرکز فضایی کشور و تأسیسات هسته‌ای هدف قرار گرفتند.
🔹
نیویورک‌پست به نقل از جی‌دی‌ ونس: ایران برای پایان دادن به جنگ هفت‌ماهه باید غنی‌سازی هسته‌ای خود را کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/696499" target="_blank">📅 23:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1e56a10b.mp4?token=toFadZT5X9Rb-I4v4PrV1S-QA5h5v3Ui8WZ28E50R9x8evlYiXKsMXmqthNy1sDx2F0lDNMzZouI7xvB_yWyY6PD4V6c-SWtmv9v8al3DPjqyPDC7Dl6XLG7501ZoKe0IGWkT1-lJmMOE42nglx1X1quBaQNR_50ZFUBJ-tFaj4ecEEx-JpSEV_mVuT93pMhoigwXEZAd_mkGvkkAsx1pY98uKJp0hkKsdwEdRi0VhN8STAEZF_67aBN_Yg3qGcR4X1L369BkmkHHJp4NbYPvL0xLbbZ-4mWlf01rmLQDe4Bf4GYdjku28X6Yp28gM6zm97CEI9nsC6n9uZVYseHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1e56a10b.mp4?token=toFadZT5X9Rb-I4v4PrV1S-QA5h5v3Ui8WZ28E50R9x8evlYiXKsMXmqthNy1sDx2F0lDNMzZouI7xvB_yWyY6PD4V6c-SWtmv9v8al3DPjqyPDC7Dl6XLG7501ZoKe0IGWkT1-lJmMOE42nglx1X1quBaQNR_50ZFUBJ-tFaj4ecEEx-JpSEV_mVuT93pMhoigwXEZAd_mkGvkkAsx1pY98uKJp0hkKsdwEdRi0VhN8STAEZF_67aBN_Yg3qGcR4X1L369BkmkHHJp4NbYPvL0xLbbZ-4mWlf01rmLQDe4Bf4GYdjku28X6Yp28gM6zm97CEI9nsC6n9uZVYseHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های مضحک نتانیاهو: اگر ما علیه ایران اقدام نمی‌کردیم، بمب‌های اتمی ۱۰میلیون اسرائیلی را نابود می‌کردند؛ ما دود می‌شدیم و به هوا می‌رفتیم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696498" target="_blank">📅 23:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مدیر استان البرز بانک صنعت و معدن: موضوع فولاد بافق یک مطالبه ساده بانکی نیست؛ ابهامات معامله و شرایط پرداخت باید روشن شود
🔹
فرزین سمایی، مدیر استان البرز بانک صنعت و معدن، در واکنش به مطالب منتشرشده درباره عدم پرداخت تعهدات مجتمع فولاد بافق تأکید کرد: تقلیل این پرونده به امتناع بانک از پرداخت یک تعهد قطعی، تصویر کاملی از واقعیت موضوع ارائه نمی‌کند و تا زمانی که ابهامات مربوط به معامله پایه، مستندات و شرایط ایجاد و پرداخت تعهد به‌طور کامل روشن نشده باشد، بانک موظف است در چارچوب قانون و مقررات بانکی عمل کند.
🔹
سمایی در جمع خبرنگاران با بیان اینکه موضوع در مرجع قضایی ذی‌ربط در حال رسیدگی و بررسی است، گفت: «در این خصوص دستور قضایی نیز در چارچوب موضوع مورد رسیدگی صادر شده و بانک صنعت و معدن خود را ملزم به رعایت تصمیمات مراجع قضایی صالح می‌داند. در عین حال، اجرای دستور قضایی باید دقیقاً براساس مفاد و حدود همان دستور و با رعایت الزامات قانونی و مقررات بانکی انجام شود.»
وی افزود: «نمی‌توان مفاد یک دستور قضایی را فراتر از موضوعی که در آن تصریح شده تفسیر کرد؛ همان‌گونه که نمی‌توان مقررات بانکی را نیز براساس برداشت‌های متفاوت کنار گذاشت. تصمیم نهایی درباره چنین پرونده‌ای باید مبتنی بر مجموعه اسناد، واقعیت‌های معامله، نظر مراجع ذی‌صلاح و الزامات قانونی باشد.»
▫️
مدیر استان البرز بانک صنعت و معدن با اشاره به اهمیت بررسی «معامله پایه» اظهار داشت: «پرسش‌های موجود در این پرونده صرفاً به عملیات بانکی محدود نمی‌شود. زمان انجام معاملات و شرایط کشور در آن مقطع، هویت و سابقه فعالیت شرکت‌های طرف معامله، چگونگی انجام معامله و مستندات مربوط به تحویل و جابه‌جایی کالا، از جمله موضوعاتی است که باید به‌صورت دقیق مورد بررسی قرار گیرد.»
▫️
وی تأکید کرد: «طرح این پرسش‌ها به معنای صدور حکم یا انتساب تخلف به هیچ شخص یا شرکتی نیست. اساساً فلسفه بررسی کارشناسی و قضایی نیز همین است که واقعیت معامله و انطباق آن با ضوابط، پیش از اتخاذ تصمیم نهایی احراز شود.»
▫️
سمایی درباره استنادهای صورت‌گرفته به کد تأیید بانک مرکزی نیز توضیح داد: «وجود کد بانکی یا ثبت یک مرحله از فرآیند در سامانه، به‌تنهایی به معنای پایان بررسی تمام شرایط یک تعهد نیست. برای اجرای نهایی تعهد، مجموعه اسناد، شرایط معامله و فرآیندی که منجر به ایجاد تعهد شده است باید بررسی شود. بنابراین میان ثبت یا تأیید یک مرحله از فرآیند بانکی و احراز نهایی شرایط پرداخت تفاوت وجود دارد.»
▫️
وی همچنین در واکنش به مطالبی که از وجود دستور قضایی برای پرداخت سخن گفته‌اند، اظهار داشت: «بانک صنعت و معدن خود را موظف به اجرای تصمیمات مراجع قضایی صالح می‌داند .آنچه برای بانک ملاک عمل است، متن، حدود و مفاد صریح دستور قضایی است، نه برداشت یا تفسیر رسانه‌ای از آن.»
▫️
مدیر استان البرز بانک صنعت و معدن درباره طولانی شدن فرآیند تعیین تکلیف پرونده نیز گفت: «صرف گذشت زمان نمی‌تواند جایگزین بررسی اسناد شود. آنچه اهمیت دارد، احراز شرایط و مستندات تعهد است. اگر شرایط پرداخت به‌طور کامل احراز شود، مسیر اقدام بانک روشن خواهد بود؛ اما زمانی که درباره معامله پایه، اسناد یا نحوه ایجاد تعهد ابهاماتی وجود دارد، رفع این ابهامات بخشی ضروری از فرآیند تصمیم‌گیری است.»
▫️
سمایی در ادامه به نگرانی‌های مطرح‌شده درباره وضعیت تولید و اشتغال در فولاد بافق اشاره کرد و گفت: «حفظ تولید و اشتغال برای بانک صنعت و معدن به عنوان یک بانک توسعه‌ای اهمیت جدی دارد و بانک از هر اقدامی که به تعیین تکلیف قانونی و سریع این موضوع کمک کند استقبال می‌کند؛ اما نباید میان حمایت از تولید و رعایت قانون یک دوگانه غیرواقعی ایجاد کرد. حمایت پایدار از تولید نیز باید در بستر قانون و ضوابط انجام شود.»
▫️
وی تأکید کرد: «بانک صنعت و معدن نه به دنبال طولانی شدن پرونده است و نه از تعیین تکلیف آن استقبال نکرده است؛ برعکس، تعیین تکلیف روشن، قانونی و مستند این موضوع به نفع همه طرف‌هاست. انتظار این است که به جای تقابل رسانه‌ای، فرصت داده شود اسناد و واقعیت‌های معامله در مسیر کارشناسی و قضایی بررسی شود.»
▫️
مدیر استان البرز بانک صنعت و معدن در پایان خاطرنشان کرد: «اگر پس از طی فرآیند قانونی، وجود و شرایط یک تعهد به‌طور کامل احراز شود، بانک در چارچوب مقررات اقدام خواهد کرد و اگر ابهامی در اسناد، معامله پایه یا شرایط ایجاد تعهد وجود داشته باشد، ابتدا باید همان ابهام برطرف شود.»
▫️
وی افزود: «حمایت از تولید زمانی پایدار و قابل اتکاست که در کنار آن، قانون، اسناد و حقوق همه طرف‌های ذی‌نفع نیز رعایت شود. بانک صنعت و معدن نیز در این پرونده دقیقاً بر همین مبنا عمل خواهد کرد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696497" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
علیرضا دبیر که تهدید کرده بود اگه حتی یک نفر از اعضای تیم ملی ویزاش صادر نشود تیم ملی رو به مسابقات جهانی آمریکا اعزام نمی‌کنه، امروز ویزای تمامی اعضای تیم‌ملی کشتی بدون هیچ کمی و کسری صادر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696496" target="_blank">📅 23:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6z5ELl9gYMgD_OmmCCta6tydRavVNtigZDubQBHQy2s0D981O0Rj08EQdnW4d4EDmt3VuTEVCrsSAa9R4yLmIo4dbxRlr2jE9YBtP-3CG76eN1mYn9d3xjqajB0q7z32_xDHgjXSV9F5sFWxUF_NHhiZ7fNFqTM2QvTr3n6kH-ZOBtnAAJ7GfBenr0-CmfB5M5EKpUPxBG_XYNFOFTsKdGMyde9_2fX9U1fpTOchdofR2RDTFaM_AE5CSc3IlVevtFVhFQPRDaxZJYNAlhRS-aw50_LSRqeaUAPR26L3u01HuhFyFB1U99lpjtlymDp3Peai-fdzAkkpYS9-KwvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غزه پس از ۳ سال؛ جهان چگونه در برابر یک نسل‌کشی سکوت کرد؟
🔹
سه سال پس از عملیات ۷ اکتبر ۲۰۲۳، درگیری‌ها تا حد زیادی در چارچوب یک آتش‌بس شکننده فروکش کرده است. با این حال، دشوارترین پرسش‌ها همچنان بی‌پاسخ مانده‌اند؛ اینکه چه کسی کنترل این منطقه محصور را در دست خواهد گرفت، آیا حماس خلع سلاح خواهد شد و اسرائیل چگونه محدودیت‌های اعمال‌شده بر زندگی فلسطینی‌ها را کاهش خواهد داد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3250763</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696495" target="_blank">📅 23:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgAP-VkkfVcPvX9HTp2CEXD3VUMfjTo084UjnGAJXGSxGX05frwWLlEPJaWtd-M4ML2gTB9Jsb1W-bUVI8IpEniRVtNgBrOdLOt5Tqf4ClBqkjYSnUFEB5StJcKcGSkwBo1RFf5m2YBTCg4k_zuAztjlxU9KkXqG2LRwTKuKWTNPrwwQdwcPniKqOHXLm7qCHRBQWt5KFd2XMHqsCPfwLAzAfOWd6zXvgn43sZ2m9orHf2L9edc9hL0u_0IYNRgrwCIytQMo81pEFBpwtV5MIUfU4mAFRuRqrQQhJfW6C31i48ZTlKJJvQTmxRwj1lYGksHcbqwTzhHSw_1aVN-N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار یک نفتکش در نزدیکی قطر
سازمان تجارت دریایی انگلیس:
🔹
یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است؛ این نفت‌کش گزارش داده که توسط چندین پرتابه هدف قرار گرفته و آسیب دیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/696494" target="_blank">📅 23:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 8- میدان هشتم، جهاد</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696492" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان هشتم، جهاد
🔹
جهاد بازکوشیدن‌ است، بدان معنا که در مسیر سلوک روح هر فرد در حال جهاد می‌باشد.
🔹
می بایست در مسیر به آن شکل که شایسته‌ی پروردگار جهانیان است جهاد کنید، بدان معنا که به هیچ وجه کاستی پیشه نکنید و از هيچ کوششی روی برنگردانید.
جهاد سه قسم می‌باشد:
🔹
جهاد با نفس_جهاد با دیو_جهاد با دشمن
جهاد سه رکن است و ارکان به صورت زیر هستند:
🔹
با دشمن به تیغ_با نفس به قهر_با دیو به صبر
مجاهدان با دشمن:
🔹
کوشنده ماجور_خسته مغفور _کشته شهید
مجاهدان با نفس:
🔹
ابرار (نیکان)_اوتاد (مرتبطان به جهان هستی)_ابدال (جدا شده از بندهای ذهنی و نفسانی)
جهاد با دیو:
🔹
مقربان (به علم مشغول)_صدیقان (به عبادت مشغول)_اولیایان (به زهد مشغول)
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/696492" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b31ff4edb.mp4?token=Jb5zqWbIwFMyhWpS3fQNUCtT789uRKyTC27_Hpcc5cjWQaGGirXeMh1G7u3JWqzSduvIlrAldlwzP2jpSKs0gcTiIZCMw8Nz6y244uOmhk7vLhRc_sXdMM643BI-BAyXG0VF6BPcfAp96YBd6MBnEMbkiccnp7C44_RsfXn60v_PJI2_swroH_id-pbJUuHyQG3c0YJA85OMlXrO3IJ5flB5NIsGz5lwBPbBVM7JgAWQmjZ8sIy1aaIQ46nCgYdzPe_FOG47Xyf7fDic8yQTXKGo8iROtg0nlmxQ0iNjMm8YX3qvui1RbIH8bN4EgDSaok06C6E4Rd2aGbOyB8Av_g9HOfiNklKMg4OadHTgroberApeFnKSPCsJGMfh_h3BET1LKuLVufbrGE1g01AsoMoCj2r9KBAGYwxN-xcnJP7b3MA2_YugH7PfsnP3XyBGLCUs64z-Iv-kwi4Xv7D4AySaWzWH58lJT3i_N5LTBKsUsvzq7tdUZzVmu9pb8oH5gP4aUq2CuQebW8UCcAPuUGK4kn_PIUK2S-t6D9vEU34HcihMl4tawdS52zvtLnlDno-44fjYOJnpqK9yPjK_d_BllW4MRau1b3kDi08ZZ-HFP5NkXcz0Dk_PfT61slY-kxCKdTIVtpa2kEcSp2nxYJdpNmVDFCK1yLxV5QFoBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b31ff4edb.mp4?token=Jb5zqWbIwFMyhWpS3fQNUCtT789uRKyTC27_Hpcc5cjWQaGGirXeMh1G7u3JWqzSduvIlrAldlwzP2jpSKs0gcTiIZCMw8Nz6y244uOmhk7vLhRc_sXdMM643BI-BAyXG0VF6BPcfAp96YBd6MBnEMbkiccnp7C44_RsfXn60v_PJI2_swroH_id-pbJUuHyQG3c0YJA85OMlXrO3IJ5flB5NIsGz5lwBPbBVM7JgAWQmjZ8sIy1aaIQ46nCgYdzPe_FOG47Xyf7fDic8yQTXKGo8iROtg0nlmxQ0iNjMm8YX3qvui1RbIH8bN4EgDSaok06C6E4Rd2aGbOyB8Av_g9HOfiNklKMg4OadHTgroberApeFnKSPCsJGMfh_h3BET1LKuLVufbrGE1g01AsoMoCj2r9KBAGYwxN-xcnJP7b3MA2_YugH7PfsnP3XyBGLCUs64z-Iv-kwi4Xv7D4AySaWzWH58lJT3i_N5LTBKsUsvzq7tdUZzVmu9pb8oH5gP4aUq2CuQebW8UCcAPuUGK4kn_PIUK2S-t6D9vEU34HcihMl4tawdS52zvtLnlDno-44fjYOJnpqK9yPjK_d_BllW4MRau1b3kDi08ZZ-HFP5NkXcz0Dk_PfT61slY-kxCKdTIVtpa2kEcSp2nxYJdpNmVDFCK1yLxV5QFoBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی چوب، سنگ می‌شود!
🪵
🪨
🔹
این فسیل یک درخت باستانی است که به آن «چوب‌سنگ» می‌گویند.
🔹
هنگام پوسیدن چوب، مواد معدنی جای مواد آلی را می‌گیرند؛ پدیده‌ای به نام «جایگزینی معدنی».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/696491" target="_blank">📅 22:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
«باج‌نیوز» در دادگاه؛ یک رسانه در پرونده شکایت میلی محکوم شد
🔹
یکی از رسانه‌هایی که با انتشار مطالب خلاف واقع علیه پلتفرم میلی قصد اخاذی از این پلتفرم را داشت توسط دادگاه مطبوعات محکوم شد.
🔹
در پی شکایت شرکت سرمایه زرین ماندگار (میلی) از پایگاه خبری «وانا نیوز» بابت نشر اکاذیب، شعبه پنجم دادگاه کیفری یک استان تهران رأی بر مجرمیت صادر کرد. به گفته سخنگوی هیأت منصفه دادگاه‌های سیاسی و مطبوعاتی، هیأت منصفه پس از بررسی مستندات پرونده و محتوای مکالمات ارائه‌شده، به اتفاق آرا اقدام مدیرمسئول و روزنامه‌نگار این رسانه را مصداق باج‌گیری و سوءاستفاده از حرفه روزنامه‌نگاری دانست و آنان را مجرم تشخیص داد. رأی صادرشده قابل فرجام‌خواهی است.
🔹
گفتنی است در روزهای اخیر نیز برخی رسانه‌ها در فضای مجازی اتهامات مشابه‌ای را علیه این پلتفرم مطرح کرده بودند./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/696490" target="_blank">📅 22:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-VW9eVklZLjuAeFKsCIwNwKMQnOpOfpJt-_oMB2HiVCKxmnz6-IN_vuGFFU8sa6GqbgNSzrFaQdlCB-IOy5-TNOh-E96Hb-9m8dWrgvwRDk5n07FXrjQC9nBhO3ApKSSVizUVCAcR5-ZPtpmpKCLHhPpcc6eBiY3g6EE9caVVLlAXsaUQh_Kyf13w-9ehH1v0q8dlaFoJJpnM38fPjH67F24cswhMTuFyz-Vg4sJRQD14GPhQMXVxC3n2gZvdUvFaT-Z9WAXk14YAzPyqEaQw6hsEEvHkKxy88F_lnimA2yENQJi-LKocIUtCpSegvS3eTFoPgOMpMO9fslfwEZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس: فاکتور گرمایشی زمستانی بی‌رحمی در راه است برای خانه‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/696489" target="_blank">📅 22:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3yVaqUvzyW_EDnaqYJ5XQtaprcKDtA7195aRVKQYS6NVPdQo976gpbvw5IBi-M-PNQLTZizgadVcb3H-4RLnpOQKdvt9YZQcKugYhQpY7YKpCVl2DRvfYX1mupTuy7tEnImHijBwl11qjtJDyiMQYATmRXcMpZdEOGSEpwb71aRhD_CkJ5u5KAhcIoayCeMdNDpzQQCSycv9gTbY-TQnPePBPLa5BS52fozZV6iaqiHKVHqbJhaaU5eKmna9UKnhmBHydAmf-jGPb0sjUCnNivS81vpkWH5RPDd0-GQePRvBqDJxitQWiPZiQh0QKSyOGYpwWvbyyYhtzTXbYY5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتلانتیک: ترامپ پیش از انتخابات میان‌دوره‌ای دستور حمله دیگری به ایران را صادر می‌کند
🔹
کاخ سفید از پنتاگون خواست گزینه‌هایی برای حمله به ایران قبل از انتخابات میان‌دوره‌ای آمریکا آماده کند. تصمیم نهایی هنوز گرفته نشده/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/696488" target="_blank">📅 22:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده شدن دو صدای انفجار از سمت دریا در کوهستک سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696487" target="_blank">📅 22:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
هشدار آمریکا به شهروندانش: ممکن است بزودی فرودگاه‌ها و حریم هوایی عربستان بسته شود
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696486" target="_blank">📅 22:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7Jw-zbkhdFfmGt2oDhmp4TWzooYOwSbcWaHoPZAH1fmEV1uPsFRyYm2BveA5FaJ2vLkFJF0Pgb9HH73BoxkNmyHh3jq6oVt22m51L0_GW4j2-8rr6ql4J2YnVHl98UX3P2-xKiR9PGq89MNPcFnRIndtm-bq3SIPe25IXC1CNieIF6_0o6KCKG2VTjNZZROPJnfkmG_gKGmUVRkdbrpf7MZ0qvVaQPmCwnKIM-DCuTmtY8rORQULlmpkNziKqE2wDduJy6C6Awz_1JlOvTRPlr_wZ4ukVguq9U3voPmD0PSMs8wFNjMDaZc0A-Z1e2Vcwj1rrpwcjUGWdrjvqakFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاهوتی نماینده مجلس: مشکل میلی خالی‌فروشی نبوده/ فقط موجودی طلایش از خزانه دیر تحویل داده شد
🔹
کسی که طلا می‌خرد، در هر صورت باید از اعتبار و اصالت معامله اطمینان داشته باشد و حواسش باشد که فروشنده یک مرجع رسمی باشد.
🔹
در فضای مجازی اتفاقات زیادی رخ داده است. در سایت‌هایی مثل دیوار هم موارد زیادی از کلاهبرداری دیده‌ایم.
🔹
میلی گلد هم مجوز مدیریت و فروش خرد طلا را دارد، هم پروانه کسب‌وکار و هم سایر گواهی‌های مربوط به فعالیت در حوزه فناوری‌های نوین مالی.
🔹
مشکل خالی‌فروشی نبوده؛ طلای موجود خودشان را از خزانه دیرتر تحویل گرفته‌اند و نتوانسته‌اند آن را به‌موقع به مردم تحویل دهند./ جهان‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/696485" target="_blank">📅 22:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تسنیم به نقل از منابع امنیتی: حمله راکتی در جالق سیستان و بلوچستان کذب است  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/696484" target="_blank">📅 22:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
حمله مسلحانه به مقر انتظامی در گلشن
🔹
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت./ صدا‌وسیما  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696483" target="_blank">📅 22:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq51fiAONJi1LB_XMrXsaEhqb5xSEYzLvhm22HJDU7IWtsFR4x6s5n4KUfuKEhy1SE460jN24nVojcbV0apTbOjJVtGIN17g4d76BEyErn3S3LVh5scjJwBKMJfJaHiy4zdZaO_xQm_vOTVDgQlboRB53wDAMnEqLSNOkA6y5lLourI3UdQKDv3siGmlMoBwDmAKSZhQGCIp_TJgxpjc1pOVWuQbx69i8sx5ai25xZ6oOzK-6rm3DL_1NrTEA4-g2ULvW3Okc95Rf5O5C0N--U64RKJBvh-ltQAXu9xusyHVT1V2TSn0aV3NRJekrtWHo-_jY96Nmgh5w65SGX4h6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ تیم ملی ایران با یک پله نزول به رنک ۲۳ ام سقوط کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/696482" target="_blank">📅 22:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پزشکیان: من یک دانش‌ آموز شلوغ و بازیگوش بودم و درس هم نمی‌خواندم اما وقتی وارد جامعه و نامردی‌ها را دیدم تصمیم گرفتم درس بخوانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/696481" target="_blank">📅 22:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696480">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سخنگوی ارتش پاکستان در اظهاراتی حضور بلندمدت نیروهای نظامی این کشور در عربستان سعودی را تأیید کرد و آن را بخشی از «ائتلاف مکه» دانست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/696480" target="_blank">📅 22:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی انصارالله: فرودگاه ابها و تجمع نیروهای سعودی در جیزان را هدف حملات موشکی قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/696479" target="_blank">📅 22:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای
ترامپ: درگیری با ایران به زودی و به هر نحوی پایان خواهد یافت
؛
ایران در شرایط سختی قرار دارد و هرگز به سلاح اتمی دست نخواهد یافت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/696478" target="_blank">📅 22:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0482c0e27e.mp4?token=W6yWhBjdoE2V1aXIeERfvhJz19RO42Var3BYzC4xnEfG_cPkzXEeKjroaZENsOT5ZaSmGGSXKE3Qe_w0_m2kF6tWb8Kn5Lm_0GIhIPwR2zVzr_dqj3fQc6kEaWA_XBUmUMnDIkwo6m6g63HrVGe0Y_XLZiN1eWrvgI_4-4UhvToxNU-cVxKXzHBaPO1krG8JeXwY-gZUWEZSoZXIByDZhLsFkVHxvVBc3F44fA_C3U38Mo-LoezWPF_IrgJhZpSSV9GOPveAmWimM1lHx2uY32Ml-4vgATlE1mKfSwogBsUo4jviiiUonukT2V_oYqWRY0fuZDy-bXuBwsZJyfPCkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0482c0e27e.mp4?token=W6yWhBjdoE2V1aXIeERfvhJz19RO42Var3BYzC4xnEfG_cPkzXEeKjroaZENsOT5ZaSmGGSXKE3Qe_w0_m2kF6tWb8Kn5Lm_0GIhIPwR2zVzr_dqj3fQc6kEaWA_XBUmUMnDIkwo6m6g63HrVGe0Y_XLZiN1eWrvgI_4-4UhvToxNU-cVxKXzHBaPO1krG8JeXwY-gZUWEZSoZXIByDZhLsFkVHxvVBc3F44fA_C3U38Mo-LoezWPF_IrgJhZpSSV9GOPveAmWimM1lHx2uY32Ml-4vgATlE1mKfSwogBsUo4jviiiUonukT2V_oYqWRY0fuZDy-bXuBwsZJyfPCkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش هگست برای حفظ آبروی ملوانان درمانده ناو یو‌اس‌اس آبراهام لینکلن
وزیر جنگ دولت کودک کش آمریکا:
🔹
چند نفری در رسانه‌ها سعی کردند ناو یو‌اس‌اس آبراهام لینکلن را به نوعی نمادی از روحیه پایین یا مأموریتی شکست‌خورده جلوه دهند.
🔹
می‌دانم که این موضوع دقیقاً برعکس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696477" target="_blank">📅 22:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDFwkY23vkNKWe2HBTm8RB7nDaHN9Zk6NFTS7i7n__FxitSxInSx_uQGkV-aBkn6PovcjC03Dou2Etcypl4kJlKPzKBRx3IlgesvOnLCJrP7PfgkXpJDWRFUXQiAXlN3F-Pb8yl6KdI6vHQZ24woeb4ZM3TitA1uA13sY3yseN4DN3Mum_jQO4w4hvb_OGjj2JoLdrGCtPsowNW5ovCT9jnu4RZTgx1sa2RfT37IuKxuVTImVQXogdXNH0hA2ltFThgqLj2P5U0EaQ6-EdtgmfkYCHcwh7fm-MsGFeGaDJk2woNczkiOHQKSkt1zqaB38MNzUpjJ9rDA9ELNiDMMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۴ آنتی‌بیوتیک رو خودسرانه شروع نکن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/696476" target="_blank">📅 22:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
این ۳ تا ویژگی که علیرضا مطلبی درباره ثروتمندهای نسل جدید می‌گه رو باید جدی گرفت...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696475" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای یک اندیشکده پاکستانی: عملیات سپیده دم یمن با مشارکت پاکستان و دیگر اعضای پیمان مکه علیه یمنی‌ها آغاز شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/696474" target="_blank">📅 22:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تسنیم به نقل از منابع امنیتی: حمله راکتی در جالق سیستان و بلوچستان کذب است
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696473" target="_blank">📅 21:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fb18cd4.mp4?token=cROlrvW9n1D_Tm7DzXBRygLuA0d0fCddOK9e0dXDdA4CW5uxvv0KiBfw-R5P_37lN_mMzLbUMGZgCIt0pAGHn8120_2OSsmMZt2HHS9jWfWFa0uG1TnhbhiJm1aRYMY7LYnU7p--sUHXtPjaKV5pLo57UKDA9EEkAewjyzxSAsT_sFAmopcrbJ7s7DS-ZfP9jj8Dt9qVZ10EDk21bG-rPtgm-a-iVn7UbpUdhTYqFNJvMf7cL_b-XbQPauaVEHITgYamPna0foZTWIVk8Ch1x1yzv_shyZrgqPEvh3gZnr9vSpBuBknwhHoCkZnXN_2lJR3tW-7LvX23BmCtQs73DQ4ddghSY2fkYcjMSeMLOwi9Ac26nqw38JDKqyQ9PczFuPmB37zTAkxIam4UWOZYfQVLOKPCRM5RVU7U8WZYkmAOJWcl-hWIncbbTU-Xls19cjB6zBCI_Hl9pHRF9ihEmMrGtefI5mf8F1WuEvjgowJ1g1gUyLa3QljenepEiqEpyxzqlCar9Us_vQyoFaGxVzzEbgNu-6fRCbypo74k08IfE-rZY_MkArUdhAOpBR3HvLJvieoH3DeoWs3zKghnbWwCew7Vk5znjCBJtM3DlV8tl833wKaioSACXbHORpABGhQJ524WreSS5LZcJ7HMaEY9PniKXiB07M4HjbfCwXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fb18cd4.mp4?token=cROlrvW9n1D_Tm7DzXBRygLuA0d0fCddOK9e0dXDdA4CW5uxvv0KiBfw-R5P_37lN_mMzLbUMGZgCIt0pAGHn8120_2OSsmMZt2HHS9jWfWFa0uG1TnhbhiJm1aRYMY7LYnU7p--sUHXtPjaKV5pLo57UKDA9EEkAewjyzxSAsT_sFAmopcrbJ7s7DS-ZfP9jj8Dt9qVZ10EDk21bG-rPtgm-a-iVn7UbpUdhTYqFNJvMf7cL_b-XbQPauaVEHITgYamPna0foZTWIVk8Ch1x1yzv_shyZrgqPEvh3gZnr9vSpBuBknwhHoCkZnXN_2lJR3tW-7LvX23BmCtQs73DQ4ddghSY2fkYcjMSeMLOwi9Ac26nqw38JDKqyQ9PczFuPmB37zTAkxIam4UWOZYfQVLOKPCRM5RVU7U8WZYkmAOJWcl-hWIncbbTU-Xls19cjB6zBCI_Hl9pHRF9ihEmMrGtefI5mf8F1WuEvjgowJ1g1gUyLa3QljenepEiqEpyxzqlCar9Us_vQyoFaGxVzzEbgNu-6fRCbypo74k08IfE-rZY_MkArUdhAOpBR3HvLJvieoH3DeoWs3zKghnbWwCew7Vk5znjCBJtM3DlV8tl833wKaioSACXbHORpABGhQJ524WreSS5LZcJ7HMaEY9PniKXiB07M4HjbfCwXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام تصویری نماینده جنبش حماس در ایران به مناسبت سومین سالگرد طوفان الاقصی: مردم غزه ثابت کردند در برابر ابرقدرتها شکست ناپذیر هستند و مقاومت با وجود ترور رهبران و کشتار مردم همچنان ادامه دارد
@TV_Fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/696471" target="_blank">📅 21:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حمله مسلحانه به مقر انتظامی در گلشن
🔹
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت./ صدا‌وسیما
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/696469" target="_blank">📅 21:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8nnRDnsC-MwLkWV4KMexwUw1esLKrIxDTP28UpF3r6QhNpi2-mgSQd3IpyvWFye0tlhVrzpYcMKy_cysvL0c5CLw9DU21ViVV6tEvxiY-EBohmjDwH2PTWpQSVMsf10k2udZlyko4Ck-iBtplS7PVE-mHqQ-ZikHYPpn63cmZhGg4Aol0o1de5FzlU1uC0zdzHzddDL7w03XuqAloRGK-XlRzzs-9FO0zKv3jfM-LGAMNJ9T1Lq_EVG53v_g_z19z5rtKCTa8QANyyvCTGP9L4SUwJOEbl6NF54aIHhQFfUeuoJp29MQD6QK2uhgOu105LLzE94JJfwmsLcw1DONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نارین پس از روزهای سخت به آغوش مادر بازگشت
🔹
دو دختر سنندجی بعد از مداوا و درمان دیروز از بیمارستان مرخص شدند و به آغوش مادر بازگشتند.
🔹
این دو خواهر خردسال سنندجی پس از آنکه برای مدتی در سرویس بهداشتی منزل حبس شده بودند، با حضور نیروهای امدادی نجات یافتند…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696468" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRNOb_dqGRF_-B1GB-P7ijnix25qZX26walZqefkPjsveNyxdqevO3dXJ_g6HSQ19UzPHgeTmweqQeZRtbG8oxyxyWd758lSc90eIE-7FLDEAdsDOHfQ1d86WDtAVrGNj3K5Ac9ST6m9LPxWxBqR24wpOnYT3zZiun3BqJbCwsrWv0ZNu0mi8ieDI3NRVl6R3aMkAuX4whGbRh08OInXwewxLE81tLszC_ptok0QQ84wg4St-nAbjJCIDWcQHLeX5pwQ63_4HdU8jVHwMnLzuk1FXLJsy3iIlNtHIlD2jB58V4HR19X5NzLWxArs75-kaLRWMygX-iyVNJZPSvlXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از مدرسه تا بازداشتگاه؛ برخورد امنیتی با دانش‌آموزان معترض
🔹
اعتراضات دانش‌آموزی فرانسه از نارضایتی نسبت به کمبود معلم، کلاس‌های پرجمعیت، فرسودگی مدارس و فشارهای آموزشی آغاز شد و به سرعت به جنبشی سراسری تبدیل شد.
🔹
تا ۶ اکتبر بیش از ۶۵۰۰ نفر بازداشت و دست‌کم ۲۱۵ دانش‌آموز مجروح شده‌اند؛ همزمان صدها مدرسه نیز تعطیل، نیمه‌تعطیل یا درگیر اعتراضات بوده‌اند.
🔹
برخورد پلیس با معترضان نوجوان، استفاده از گاز اشک‌آور و سلاح‌های کنترل جمعیت و بازداشت‌های گسترده، انتقادها درباره تناسب برخورد امنیتی و محدود شدن حق اعتراض مسالمت‌آمیز را افزایش داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696467" target="_blank">📅 21:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdPSKthEpgjsiU7X5sjlTp5xamZFO0-vcguTxNi2QCEIc-hnMO2LjculOgnl6PVN4f3kDR1OnG6AGbmF_-k8tVyJ8ju1Z-HKSpUnBFOWixU_ZXxCuAdL8KdWFp96UaELXjnEXf2ubY0pnfWMjMkr4NE0-aVSBEzWXPC1bzOIMgo5KvvN-l7qwtxBBuKNc8fI5zAaoHcIIMjo3oigulk70IsxGF2yn4DChnRUI6bw0TPZI0_bq7HmD4LiidGNAYRfv981510Hh0T1tov9sHABEbXFFTmPNRT7bSHnwKOkfkMZ8GDHAQtmWkWzKkfAz_SBGtxeOHTGwK82skUYxFjDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پچ روی یونیفرم سرباز اسرائیلی مورد توجه قرار گرفت!
🔹
مناطقی که میخواهند و به رنگ آبی روی نقشه است از نیل تا فرات است که حتی شامل عربستان می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696466" target="_blank">📅 21:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696464">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">23-1 Ane Manaee (1404-02-10)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/696464" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وسوم؛ بخش اول
🔹
تبیین دوگانه "تدبر در قرآن" و "دل‌های قفل‌شده" در آیات ۲۴ و ۲۵ سوره محمد [01:00]
🔹
توصیف ویژگی‌های قرآن و اهمیت تفکر و تدبر برای فهم لایه‌های باطنی آن [13:05]
🔹
تشریح فلسفه "وحدت وجود" و خطای بزرگ انسان در اصالت دادن به ماهیت ها به جای دیدن وحدت در هستی [22:10]
🔹
نگاه قرآن درباره وحدت وجود و تجلی حقیقت در هستی، و تفاوت نگاه فلسفی و علمی به مراتب وجود [29:37]
🔹
بررسی شخصیت ذوالقرنین در قرآن و تاکید بر منشأ تمکن او در زمین از ولایت الهی [35:32]
🔹
علم واقعی در اتصال به حقیقت است. علم به این حقیقت که اراده الهی منشا تمام صفات و نیازهاست [49:47]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696464" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696462">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIk2HRjbosgzXBLymTum8P0OECJvUlg11ZJVWnKwG4Qda-8Q1pr6ZE7BqIbsraip_oVm73O8ozqpsNDU-hmtL_NdKFnI60hp9dp_xrdkrC7AGpfrpXdb0oAf3jmRxzmUEIpWka_gCMygi3hFC-Ou3I3tvUcw-dUOQxAtToOeas7ry3uRqP7plbVL3_QmjZJksykyvQSdTOP3AcFF9EE5qvd2wAiVVSfR91KkbIhBFpEzGhIQD2Iuf4kkcsy5nBH4gFX0XX08CPdCkvZR3exVSyGrHp3mrd-PXHfu6wFZ6tfqXqnRzjZvUcFY9YKfERNSY_twz_b4LovmME5a4-LFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر کاری، سراغ کدوم هوش مصنوعی بریم؟ #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696462" target="_blank">📅 21:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696461">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL7sh-eIg85iZtgVXRaYcdUPqeVUjvvALQK1URAM_jqhgCt4uXX9eQA5zJ6916hYnRyjJKdsT7i5ItpW-RIlEhaNGz4SNt6f1uouMQvyzH9OpHX8DMk8MThoEcwTlSTE9YA7W9oZrfZUT9ROrms3wlyqPfONeCkVioIRlVWze7KvSSY8RDXPy5-AxLXBbnCElxtoqjHwc4rC-8GTlUYLJkbJ1gx0n-Jx9iTbjYxJyK9sY7u_VwFTXUGg-B0lBsbx08Y8S4txGotNNROJI17JhxkcuRKIHvAEVRjlSyW-e6IWrvrwdrONda0inZDysL4cB54X73cTITuG6wWWVIbpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه مهم برای همه رانندگان و مالکان خودرو/ فقط تا ۱۶ مهر برای پرداخت جرایم رانندگی بدون جریمه فرصت دارید
🔹
اگر جریمه‌ای داری که به‌خاطر گذشت مهلت پرداخت دوبرابر شده، طبق طرح بخشودگی جرائم رانندگی فقط تا پایان پنجشنبه ۱۶ مهر فرصت داری آن را بدون مبلغ اضافه تسویه کنی.
🔹
مثلاً جریمه ۱.۲۰۰.۰۰۰ تومانی که به ۲.۴۰۰.۰۰۰ تومان رسیده، در این بازه دوباره با همان مبلغ اولیه قابل پرداخت است. کافی است پلاک خودرو را وارد کنی و خلافی را استعلام بگیری؛ شاید بخشی از جریمه‌هایت مشمول بخشودگی شده باشد.
🔗
استعلام سریع خلافی خودرو و بررسی مبلغ قابل پرداخت
🔗
استعلام سریع خلافی خودرو و بررسی مبلغ قابل پرداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/696461" target="_blank">📅 21:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696460">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5796842fd9.mp4?token=NN-Ly8uls_RguEaKJ7jbxZK1S0Ph_OkEZnBc1S93GE-0VC8_WDSjSMSq3LsKGxFnffG51hSmN68vOuOD_t5eNp_GDd0Yg1KXmvUifYP-GunMW2kdQlFbwJwfmKvrUE_fdOL8nUTduUNPJetFZ8ns2UyRSDPhIYxjJSLUUwkWnFtIT7SNaWnECyATp4OJPi0Foh-Uq8jVig7v9EyOZy6R134Bo5Dw3a0R5uogykYFzmusfYyutjBa6acQMRf5XDhhYaXfzUaF0t7F0j0HY59xEmcyodFEMqNMUpOmuh332nsOPjs4lBdsRh6BZXYgz4qYbzkwp_mMF9-7iB_bZyslxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5796842fd9.mp4?token=NN-Ly8uls_RguEaKJ7jbxZK1S0Ph_OkEZnBc1S93GE-0VC8_WDSjSMSq3LsKGxFnffG51hSmN68vOuOD_t5eNp_GDd0Yg1KXmvUifYP-GunMW2kdQlFbwJwfmKvrUE_fdOL8nUTduUNPJetFZ8ns2UyRSDPhIYxjJSLUUwkWnFtIT7SNaWnECyATp4OJPi0Foh-Uq8jVig7v9EyOZy6R134Bo5Dw3a0R5uogykYFzmusfYyutjBa6acQMRf5XDhhYaXfzUaF0t7F0j0HY59xEmcyodFEMqNMUpOmuh332nsOPjs4lBdsRh6BZXYgz4qYbzkwp_mMF9-7iB_bZyslxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: من می‌توانم هر کاری که بخواهم انجام دهم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/696460" target="_blank">📅 21:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696459">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ترامپ: ماریا کورینا ماچادو(عضو اپوزیسیون ونزوئلا که پارسال جائزه نوبل بهش اهدا شد) به من گفت که در طول تاریخ جایزه نوبل صلح، هیچ‌کس به اندازه‌ی من شایستگی دریافت این جایزه را ندارد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/696459" target="_blank">📅 21:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696458">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ: ماریا کورینا ماچادو(عضو اپوزیسیون ونزوئلا که پارسال جائزه نوبل بهش اهدا شد) به من گفت که در طول تاریخ جایزه نوبل صلح، هیچ‌کس به اندازه‌ی من شایستگی دریافت این جایزه را ندارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/696458" target="_blank">📅 21:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696455">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXTzExl1Ip5XTe6T6OWeXbzvEgJcW1kdce3wnksFKr5XURSCmjhptxXdYThXxxa9h8LYvg18pe3dSfs57X90EIh9hLOEeL0twAEyvd_Cm9jdI7VGhckjQW8pA4Cvvv_HvCoVqH7CPNk620_KoMhM-G8znEM4HXigV46PfM7ECiR1S3Qb_7-xGUJTvaHgfSPrAmF3wsHruLNJlfgmr4H-1DoMKdJD4L3mdiwzb0zGumFo2yXkVYcW7wvlmy_yzvqmwyPz_oQXFDuPhmSMyf32Ye9vjIGscDRb9vbvXXZtQmr2YrbhZQRzzmp_Kh3KOR1SSX0511coeqYPgsETkTEFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در هر دو المپیاد ریاضی و علوم رایانه مدال‌های طلای بیشتری از مجموع همه کشورهای مسلمان جهان روی هم دارد
کاربر خارجی:
🔹
ایران تقریباً تمام کشورهای آسیایی را نیز پشت سر گذاشته به‌جز چین و کرهٔ جنوبی با ژاپن هم رقابت کرده و یک‌بار برده و یک‌بار باخته است.
🔹
این در شرایطی است که ایران با ۳۷۰۰ تحریم مواجه بوده و بودجه آموزش آن تنها یک‌سی‌وپنجم بودجه آموزشی آلمان است؛ با این حال، در این دو زمینه یا تقریباً با آلمان برابری کرده یا حتی از آن پیشی گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696455" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696453">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe26fe14c.mp4?token=I9FQ64Psd8DxpEmsnn9EUx3Kp67bkOfpXNuyVYARxRU08dQZ3haT1mulrAc0MCNPwgyImSJUUYIfC4MXctIbNGDBUTALKyIXgCLEvZb3HK24WA2H5CBF7pa4UMXXG0AeGA5S8trzcmxuymbOM5MGAY8-oB6ZBc6STtEGNBANAuTJTScmAWoVqerT4kDQCcICba0rngfPMlWulywZyxmaQF78ysx6eedvRm0PqAHwbeJBwIeybZ_VKA5E3BJ02HYEj_sul5d9Y6OoTQcewx5JSCxtrRCjiofJHT2FyHplSkOdATs08988QIdJsof23SZzq48AaL136w2jMRmWdxFbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe26fe14c.mp4?token=I9FQ64Psd8DxpEmsnn9EUx3Kp67bkOfpXNuyVYARxRU08dQZ3haT1mulrAc0MCNPwgyImSJUUYIfC4MXctIbNGDBUTALKyIXgCLEvZb3HK24WA2H5CBF7pa4UMXXG0AeGA5S8trzcmxuymbOM5MGAY8-oB6ZBc6STtEGNBANAuTJTScmAWoVqerT4kDQCcICba0rngfPMlWulywZyxmaQF78ysx6eedvRm0PqAHwbeJBwIeybZ_VKA5E3BJ02HYEj_sul5d9Y6OoTQcewx5JSCxtrRCjiofJHT2FyHplSkOdATs08988QIdJsof23SZzq48AaL136w2jMRmWdxFbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبدالله سارحادی، عضو دفتر طالبان: زنان فاقد عقل هستند، آن‌ها از نظر هوش کمبود دارند؛ هیچ چیز نمی‌دانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696453" target="_blank">📅 21:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696452">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyGv_ahWjkkOYdOMkub13NITMvOvzBF8jHQ69smfgRPVGcka-__Qmat8JQg7co1SWxzmyPOreHb6xZsLJIvAlRfdTQvaZmajn2cJ-aq0XnpFrzcxTdPhqO3jblX5M8HFG0xE-qKys2TU6-xAMMsmxmrKPxtYn_8q0al7fEyo0n8RNC7FPcP9dE6vpXGPbXGO-KmZu9wWFpCM2bgbInzVrIpfIZ7twHU52MmXzQuWluqzAEqNT7weCHfWnDbRh4CWtdrL5JMRkE3WoWfVsQ68Giy7D80eipUAOlqLONR5rCVmzwJ5Q6sVw5QxlYkp6WGLIcrdi_NvegG0z20fJOPerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
‌‌‌حرف‌هات رو کوتاه نکن.
بعضی مکالمه‌ها حیفه که زود تموم بشن؛
از یه «سلام، خوبی؟» شروع می‌شن و می‌رسن به هر جایی که دلتون می‌خواد.
☎️
حالا می‌تونید با تلفن ثابت به تلفن ثابت، استانی و بین استانی، رایگان حرف بزنید.
پس اگه دلتون یه گفت‌وگوی طولانی می‌خواد،
دیگه به ساعت و هزینه فکر نکنید.
شما دلتون می‌خواد با کی یه دل سیر حرف بزنید؟
🔵
شرکت مخابرات ایران
🌐
ارتباطی فراگیر
@tci_iran</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/696452" target="_blank">📅 21:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696451">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD43l37vGwCamKEvYfoiTmW3uzTy3TndbhUuDjpbucFJOSyDXSvciMm2z0zUKGT0DMOw2GxHX6lWcCPn_yejlEkidCk9LAE8r32H9hmHfadlQrCYszXoY0H_t28t5AlptH_BnQcdjCwCFxSVGHaEGJWZuWJk155df8z7bM0iNEYEfm0073wBgOYZUd5s2alnh6gm9hdPOAEC1qVk4aCsE4IvnxUmvB9w47vXkG6e944oxia49ut2ZcAnLu6_zCOP2-Xt7AM044cajb0mzBP2Kt3qqk43INMj_z2bVCHq07Usjy0MDleYd7u08iceAhU79UI95wxNI31CNVuZbJvPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون
راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه مهرماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و درخواست شماره‌ی دلخواه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696451" target="_blank">📅 21:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95994585ef.mp4?token=gCmIYaPK7Nf_k3kL8pAAZVtG37xEcoFtkaSiWYkLoPJU3IWL1dlv0OwkOJekD7KZrBE9Jztvp3U529zmn8HaJ9WXTBHwQGTaEQOxacuCAxowL-3cOsOeA4bEaLsYEvTr9spmyFTntDFnqKzV3594g-Ya9i1tYjMLeuT3YpgJiJA_nnWnyllVGhJ6DIYtxFHPs1XbdPrDAvnJUBmNPsc9xvnzMGo8eQ4rKDdZdUuxR9ulloXtqwPHmFPDTGK3O7ihiSGUFJSa4Nfd1CnpEVqYDdAYUmK5HIYdwOhW2CqklH1zXJVEIXDOX2wRY7me24fOu4xCkECeDnRoGpALfSpOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95994585ef.mp4?token=gCmIYaPK7Nf_k3kL8pAAZVtG37xEcoFtkaSiWYkLoPJU3IWL1dlv0OwkOJekD7KZrBE9Jztvp3U529zmn8HaJ9WXTBHwQGTaEQOxacuCAxowL-3cOsOeA4bEaLsYEvTr9spmyFTntDFnqKzV3594g-Ya9i1tYjMLeuT3YpgJiJA_nnWnyllVGhJ6DIYtxFHPs1XbdPrDAvnJUBmNPsc9xvnzMGo8eQ4rKDdZdUuxR9ulloXtqwPHmFPDTGK3O7ihiSGUFJSa4Nfd1CnpEVqYDdAYUmK5HIYdwOhW2CqklH1zXJVEIXDOX2wRY7me24fOu4xCkECeDnRoGpALfSpOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه پفک هندی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/696450" target="_blank">📅 21:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696449">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e193445acc.mp4?token=J6Sq_4Wru_GIh5djXmJg1mDiOQCP7oOYcNgnHrFqxJ1OTi6AYhYjSHSYwAzNJViDWnsYE8T9M9N8Yzu9b-AaaPngLDLSdfE-Cs5TDAlSPembNhZ7nSdt2uTz7ItmY4oHrWDbWfIwJCMttQnGhBsoTbO1ECU0xpRmCuWimA0hkummUbTfnnXefre5goqIUvhYrRJRXQND8u24Gyy8hmN-0ab20XX-IFNQ4N4asA4uqzM_2f_Tt7f7NIxz3UWSyS4I9XBx86KMnrqLSPyJt00KJRD2kA7tC97O-IqOTwN5kwfhF2LtPgvib8CRYCTd_DSxPI3iZVCVLKIEWRkRGybopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e193445acc.mp4?token=J6Sq_4Wru_GIh5djXmJg1mDiOQCP7oOYcNgnHrFqxJ1OTi6AYhYjSHSYwAzNJViDWnsYE8T9M9N8Yzu9b-AaaPngLDLSdfE-Cs5TDAlSPembNhZ7nSdt2uTz7ItmY4oHrWDbWfIwJCMttQnGhBsoTbO1ECU0xpRmCuWimA0hkummUbTfnnXefre5goqIUvhYrRJRXQND8u24Gyy8hmN-0ab20XX-IFNQ4N4asA4uqzM_2f_Tt7f7NIxz3UWSyS4I9XBx86KMnrqLSPyJt00KJRD2kA7tC97O-IqOTwN5kwfhF2LtPgvib8CRYCTd_DSxPI3iZVCVLKIEWRkRGybopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای دریاچهٔ گازوئیل در جاده آبادان-اهواز چه قرار بود؟
🔹
انتشار تصاویری از تجمع حجم زیادی گازوئیل در جاده آبادان-اهواز و شکل‌گیری ترافیک، در روزهای گذشته در فضای مجازی خبرساز شد.
🔹
مدیر شرکت خطوط لوله خوزستان علت این حادثه را سرقت مواد نفتی اعلام کرد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696449" target="_blank">📅 20:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696448">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز: ایران به‌زودی آنچه را «مسیرهای غیرقانونی» در تنگه هرمز می‌داند، مسدود خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696448" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696447">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_tLrH7hidC-GSKdfckinbmG1ljp0EoMfcTqKPnTQ7oxO2X0uhYpjykOopMcgUz2j1MF14gVB9a1YOgnoBCgEZ_2iLCL8bTfYi7YmuGt33JPGZPrYgZY_8uNTquL0JqzV8D8xQMzf1wZK32dXqNrPHEzXp3JAHBYoItESGiclNVHd9UZ28Xa08OzVnQmz7pA1BLylVOfjhuiLYEFPNxJQkEyzSHMZBuJao-9aotd46ncsdJue3Wg7JT20hYNNS4UPSHFj-tFVy5cEcokPzsY7LwDx-PkNX_eRK4HOIxcKoFjBhXv90cIchYS5ZS_N9lUovm2cup2ubAoYcFefA8ehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسل‌کشی اسرائیل در غزه؛ آخرین آمار قربانیان
🔸
از ۷ اکتبر ۲۰۲۳ تا کنون، دست‌کم ۷۴ هزار  فلسطینی در غزه کشته شده‌اند؛ یعنی به‌طور میانگین از هر ۳۱ نفر جمعیت غزه ۱ نفر شهید شده است.
🔸
در همین بازه، بیش از ۱۷۵ هزار فلسطینی زخمی شده‌اند که بسیاری از مجروحان با آسیب‌های شدید و پیامدهای بلندمدت جسمی روبه‌رو هستند.
🔸
از زمان آغاز آتش‌بس در ۱۰ اکتبر، ۱,۴۶۰ فلسطینی کشته و ۵,۱۱۶ نفر دیگر زخمی شده‌اند؛ آماری که نشان می‌دهد حتی پس از اعلام آتش‌بس نیز تلفات انسانی در غزه ادامه داشته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/696447" target="_blank">📅 20:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696446">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c60bb30fe.mp4?token=nondNUY8kEmOuuXZuUu_6Kq4uuy2TCcGEO1UvE1amVD7NUjlyTUfaO_rvfDgDzfTfKZgkv3p4Vm7CPrJY37dcpz2nU1BjfouIGUkxsRQjJTkadXTQjV7Jwp0bJm4I91k9q6YonVdyS3G3hQiPxI5EKgXEUfRAK6wVWse96yGKGl6YEB6GNXAk_1yJzQR9EzpX7v7tPvQSvCCrvnMrLDJxOcD5CREFYYXvure8KguwiGy4XWaX_XV0Hq7U0bJwgCHGaL4FCEplTwTAZPWQcI6mIfOiHMndhJa1MmK_3RGKhhD4fT4BaomUHSkkG7LpGHJ3RDh5SPfQJhi9f7ai1-M7WChMGEjcWutCw5Ge1ligqtyXh0YIXKTZ7r-UyMF7rT7KpUa4CgmixsFBaiiK4f7sNM_1HIN__n6AxXUGBOaIdOj5Cxvskncjz7SM9nDvLw-veSvDFEyAKI8gVfxbXYLXXYGI4ObTCFsJsWl6LOYyQkscndLfEAaNrnWtxVSkTmnHvF-Rpwb9-6_GfzggYCWJy01A8V8K6GhBIMCGSu5Vj4EBwwQmtI8aXjwNCR2LEGVwupcnFUFs6X9n2MQWfEsM0kigr2xwou_3G_05Vy5juc-YLxVT67K2O0naI1i_lhAoIyKeyPHEMfAElHwWgNq3UFptGoLjuQPnRIM-bj2Qg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c60bb30fe.mp4?token=nondNUY8kEmOuuXZuUu_6Kq4uuy2TCcGEO1UvE1amVD7NUjlyTUfaO_rvfDgDzfTfKZgkv3p4Vm7CPrJY37dcpz2nU1BjfouIGUkxsRQjJTkadXTQjV7Jwp0bJm4I91k9q6YonVdyS3G3hQiPxI5EKgXEUfRAK6wVWse96yGKGl6YEB6GNXAk_1yJzQR9EzpX7v7tPvQSvCCrvnMrLDJxOcD5CREFYYXvure8KguwiGy4XWaX_XV0Hq7U0bJwgCHGaL4FCEplTwTAZPWQcI6mIfOiHMndhJa1MmK_3RGKhhD4fT4BaomUHSkkG7LpGHJ3RDh5SPfQJhi9f7ai1-M7WChMGEjcWutCw5Ge1ligqtyXh0YIXKTZ7r-UyMF7rT7KpUa4CgmixsFBaiiK4f7sNM_1HIN__n6AxXUGBOaIdOj5Cxvskncjz7SM9nDvLw-veSvDFEyAKI8gVfxbXYLXXYGI4ObTCFsJsWl6LOYyQkscndLfEAaNrnWtxVSkTmnHvF-Rpwb9-6_GfzggYCWJy01A8V8K6GhBIMCGSu5Vj4EBwwQmtI8aXjwNCR2LEGVwupcnFUFs6X9n2MQWfEsM0kigr2xwou_3G_05Vy5juc-YLxVT67K2O0naI1i_lhAoIyKeyPHEMfAElHwWgNq3UFptGoLjuQPnRIM-bj2Qg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز عربستان سعودی در محاصره جبهه مقاومت است!
🔹
کارشناس مسائل غرب آسیا «یمن اکنون به یک مکتب و الگو تبدیل شده است. عربستان سعودی بخاطر یمن، از شرق و غرب در محاصره جبهه مقاومت قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696446" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای
فرانس اینفو: به دلیل کمبود جهانی سوخت ناشی از جنگ علیه ایران، فرانسه ۱۰ میلیون بشکه گازوئیل از ذخایر خود آزاد می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696445" target="_blank">📅 20:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696444">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعشقه ‌🎒(Seyed Hashemi)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f62cb6159.mp4?token=Ew6wulCH6ZI1h4-8VXzSB-0DSbhVDet9bqsE3jBZmVrN1QYU54lWdA9qbbVSTRwcukuKEWBOvJVnkvqKuFykjNHY7oMZXvNGsiX7sZ5sfCgNU0ogKvR9tfOXV4Yi_mGbIBhn8F2SRNbNwhPhFSX6RjemjVIVo0rTcDTNSDp4QM-nqc_7smk-WQpbH5K6HWEbsnU_dE3UAh6ZNP7rQ51HtK69RbZhoe34ExUbYv6iMy9_O4OINcwzJY2-F5EZipK2UNrWf9SfAJSRngTdOQIwyR5YLMyQsC26IysKpDCVJK26O88EeXMsO8fck3rtm4iWSJkYUB9SmXZyNc_Sv7ubsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f62cb6159.mp4?token=Ew6wulCH6ZI1h4-8VXzSB-0DSbhVDet9bqsE3jBZmVrN1QYU54lWdA9qbbVSTRwcukuKEWBOvJVnkvqKuFykjNHY7oMZXvNGsiX7sZ5sfCgNU0ogKvR9tfOXV4Yi_mGbIBhn8F2SRNbNwhPhFSX6RjemjVIVo0rTcDTNSDp4QM-nqc_7smk-WQpbH5K6HWEbsnU_dE3UAh6ZNP7rQ51HtK69RbZhoe34ExUbYv6iMy9_O4OINcwzJY2-F5EZipK2UNrWf9SfAJSRngTdOQIwyR5YLMyQsC26IysKpDCVJK26O88EeXMsO8fck3rtm4iWSJkYUB9SmXZyNc_Sv7ubsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷۸ سال جنایت،
۷۸ سال کشتار،
۷۸ سال نسل‌کشی!
آره همه‌چیز از ۷ اکتبر شروع شد!
‌</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/696444" target="_blank">📅 20:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9fd2bd4e.mp4?token=XgVOUn9DIoM5Aj8j7nN1XdEQAAReVPSfSxJpC21iMDh5SouuRTV5guOgkBxqGutdmLlC26Rr-_84-TRXcubyeKP_9-oWfl63pz43Tlo-TiuC75H7qej9_MK_i-t-C7g9eoU_qqVSg8q5MyuSIVJwPvRRCer4DAf6sdxU84YR6jPQWN__Iww2-7lmFAD_qFBzlwZ-Nce_zkCjP-3obCX8LXjsJ_31vZFNUF77wX1KsM9e1MmZThZg9FGtQuCawC2YlMc-Th-3N3NP50pgCQH2JLn1t4IBrpUYdacIqyPgok9pH7ULcWY6MLJdIZBHYKyNCAkszSRgBrMjISQY1FZ5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9fd2bd4e.mp4?token=XgVOUn9DIoM5Aj8j7nN1XdEQAAReVPSfSxJpC21iMDh5SouuRTV5guOgkBxqGutdmLlC26Rr-_84-TRXcubyeKP_9-oWfl63pz43Tlo-TiuC75H7qej9_MK_i-t-C7g9eoU_qqVSg8q5MyuSIVJwPvRRCer4DAf6sdxU84YR6jPQWN__Iww2-7lmFAD_qFBzlwZ-Nce_zkCjP-3obCX8LXjsJ_31vZFNUF77wX1KsM9e1MmZThZg9FGtQuCawC2YlMc-Th-3N3NP50pgCQH2JLn1t4IBrpUYdacIqyPgok9pH7ULcWY6MLJdIZBHYKyNCAkszSRgBrMjISQY1FZ5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت تأسیسات آرامکو در شهر رابغ عربستان
🔹
آرامکو علاوه بر ۱۰ پالایشگاه در شهرهای مختلف عربستان، ۵ پالایشگاه نیز خارج از این کشور دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696443" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696442">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای بلومبرگ به نقل از دو منبع آگاه: آمریکا به سعودی‌ها اعلام کرده است تا زمانی که جنگ علیه ایران ادامه دارد و تردد کشتی‌ها در تنگه هرمز مختل است، نیروهای زمینی خود را وارد یمن نکنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696442" target="_blank">📅 20:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696441">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfdf8301ec.mp4?token=s51j0h17GfVF_QYCp4o-hLCV-uQ8SDKRBqxlvrT0SAWnnunXbWXBrmNJkg0etw_gyAsO6EqEU0rwGNNS09HVAqd9ofT_C4IEoKcoTkTV76I34woCNW-FRslbUTWOZuAmzDhZ0HlyoCMUdEWIJpGlHvnCweDwui9yHCe8_2Ghi58BfWwgle-jES68LaO70KQF42gh-dJ39jP6hujZyE-1tyjP6gjeQAmpf9888xCJbrxOnjvUxH6Ul0w7HweMCV34gsuxn6w6ICkRdriJ-6CNEyJPDhsWMUIF5pZ1DwQP3TTY2dtncK9QWbWBNaqpCcA_yTqEuvZDwtTqEFvR5-v9sl5pGxf1OQh7D7Buq1p1fhT_JnS5R8TOxcHbIO8E_Hnila8zyRvDRr0YoXKfb_7hZZsYRznbNfpCaQjypbLC-9vg9Np7yoMQAvqfBUZtRsO1b2a0yXkB8HiIVjhH1h8Fhi4F6b-Vrn9_IMDqppYfdWojTZZFt5Bs8_szE6ySIUsFAkDg0vILMuEg9iK8b04qbPG39dgQ8UlIh9tVFvvaHTikeDJ1_G8uF12MDz7xJqZuna6HVt6MO6IVJURUj5zq6WHd1z3v_6BkFJ4xMEj9YLPgO_YMfQmYw6thvyvsvknfk6LUZVuLkaRsySsThN9_e1aE3Mjthf4i25ebeWsVM3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfdf8301ec.mp4?token=s51j0h17GfVF_QYCp4o-hLCV-uQ8SDKRBqxlvrT0SAWnnunXbWXBrmNJkg0etw_gyAsO6EqEU0rwGNNS09HVAqd9ofT_C4IEoKcoTkTV76I34woCNW-FRslbUTWOZuAmzDhZ0HlyoCMUdEWIJpGlHvnCweDwui9yHCe8_2Ghi58BfWwgle-jES68LaO70KQF42gh-dJ39jP6hujZyE-1tyjP6gjeQAmpf9888xCJbrxOnjvUxH6Ul0w7HweMCV34gsuxn6w6ICkRdriJ-6CNEyJPDhsWMUIF5pZ1DwQP3TTY2dtncK9QWbWBNaqpCcA_yTqEuvZDwtTqEFvR5-v9sl5pGxf1OQh7D7Buq1p1fhT_JnS5R8TOxcHbIO8E_Hnila8zyRvDRr0YoXKfb_7hZZsYRznbNfpCaQjypbLC-9vg9Np7yoMQAvqfBUZtRsO1b2a0yXkB8HiIVjhH1h8Fhi4F6b-Vrn9_IMDqppYfdWojTZZFt5Bs8_szE6ySIUsFAkDg0vILMuEg9iK8b04qbPG39dgQ8UlIh9tVFvvaHTikeDJ1_G8uF12MDz7xJqZuna6HVt6MO6IVJURUj5zq6WHd1z3v_6BkFJ4xMEj9YLPgO_YMfQmYw6thvyvsvknfk6LUZVuLkaRsySsThN9_e1aE3Mjthf4i25ebeWsVM3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیر ۱۲ سال آموزش در ۴ ساعت/ کنکور چگونه انسان‌ها را «ناقص» و «کامل» می‌نامد؟
🔹
سنجش شایستگی انسان‌ها در یک آزمون ۴ ساعته، باگ بزرگ نظام آموزشی است؛ الگویی که در آن برای اثبات «کامل بودن» یک فرد، حتماً باید مجموعه‌ای از افراد «ضعیف‌تر» یا «ناقص» شکل بگیرند تا رتبه‌بندی خروجی کنکور معنا پیدا کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/696441" target="_blank">📅 20:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696440">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
منابع عبری از شنیده شدن صدای انفجار شدید در حیفا خبر می‌دهند
🔹
تاکنون منشأ این صدا اعلام نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/696440" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696439">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع ارشد: تلاش‌های میانجی‌گری میان واشنگتن و تهران با بن‌بست مواجه شده است؛ تنگه هرمز دیگر اولویت واشنگتن نیست
🔹
پیشرفت مذاکرات به پاسخ ایران به مطالبات ترامپ درباره توانمندی‌های هسته‌ای این کشور بستگی دارد.
🔹
واشنگتن از ایران می‌خواهد بپذیرد که به توسعه توانمندی‌های هسته‌ای خود ادامه نخواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/696439" target="_blank">📅 19:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696438">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3TpcxMWfuvLByospwCAI0FzKihNRsDOYE4sXugSMiCxODL2rtGCRgSZTCxPIeCVl70_co4QWzx1yTNgYkqcHX2pJVszak_NdLDNLhElgzOeLQxpqJ2GRm_o5jiV2BQVNYe2Spd1IZ5rpS0XH0atVLAHlIJTz-5DSvx2II9hLW-S3bNQw0i8pE0qjI9XdKVHgBB5BQE4dkp3ooCCUFHsVAgasI1UkBODdnsGunq0FXS2rH_m4Oy9Qx2-N03TG_p_s19ayWOW2_Cwu7YXmo-lgFQJ_bfox5tTtUzNr1iLC2jt0BbnnY3DSy5J2wElJYzcmCzvskX-brL2gzfycWd_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهمترین شورت‌کات‌های ویندوز
❤️
🔹
فقط یک دقیقه وقت بذار، از امروز سرعت کارت دو برابر میشه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/696438" target="_blank">📅 19:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696437">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ7Q6ziL0-9-tecBTFfoe-nsbZPcr8pzQuJbEU5YqzAEmVp0r9a3_iEaSTVDCc4zJXcVC0iGEdrSGvpULpNXa531TTG2joidwRAIu0yBpAG-kS82J-UGfE4_aamHWo3QZVPskZD1U5WE6nN12vW7lZP31odxE7nUlV--gCGXxGBZ5Qrx2BZrBL-D56sOhDgTEgfA0QmfmpexuppHpgA8vKBShshrPZGs5pzVKgHtUczwzrLlmA8fk2pzhFPmGmUx48Hft7Z5nmBTeJq_aN465iU3IGeiVJp65oc9EL79fKlRprVdYxX-wCHsSAGk_YCMLi5-SSS0TnBSeLXIzOF4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا آخرین نفس
🔹
مسعود پزشکیان، رئیس جمهور در دومین رویداد توان افزایی هوشمند گفت: دشمنان مردم ایران اعم از آمریکا و رژیم صهیونیستی، به دنبال ایجاد اختلاف در داخل کشور و زمین‌گیر کردن ما هستند. تا آخرین نفس تلاش می‌کنم کشور از وضعیت کنونی، سربلند خارج شود. اگر شما جوانان تلاش کنید، هیچ مشکلی نیست که نتوانیم آن را حل کنیم و باید با تلاش و کوشش ایران را به جایگاه اصلی خود برسانیم.
🔹
هشتصدوهشتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/696437" target="_blank">📅 19:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696436">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رکورد نفتکش‌زنی در تنگهٔ هرمز شکست
رویترز:
🔹
تنها در یک هفته اخیر ۱۳ نفتکش در تنگهٔ هرمز هدف حمله قرار گرفته و ۷ نفتکش هم پس از هشدار از ادامه تردد در هرمز منصرف شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/696436" target="_blank">📅 19:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696435">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: ایران در حال نبردی بزرگ برای مقابله با دشمن اسرائیلی و آمریکایی است
🔹
رژیم سعودی در ترور شهید عماد مغنیه نقش داشت و از همان ابتدا از تلاش‌ها برای ترور دبیرکل حزب‌الله نیز حمایت می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696435" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696434">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وقتی تسمه هیدرولیک پاره شد و مکانیک‌هم پیدا نکردین چکار باید کنید؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/696434" target="_blank">📅 19:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696433">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
احضار سفیر فرانسه در تهران به مذاق الیزه خوش نیامد
ادعای وزارت خارجه فرانسه:
🔹
ما سفیر ایران را به دلیل کمپین انتشار اطلاعات نادرست در رابطه با اعتراضات دانش‌آموزان احضار کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/696433" target="_blank">📅 19:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcjRj5VkPiODkUSjc0YUKdFgadigiaExEgxG-sYM2a6Jl5WrRIlN0XDT8hzaQagFfodIe2AV3TkAA8m745M0768Och8BBcVrxOSk1IoNbvI33bePpMCVqf0rvIFSGYDObiiPA0osFZqxP36J3volOB5HVNB_caA-Xvwxuiz6djiuGvoQnlWi8C-TK11UOx2rmQnkdCg4kJlfbaIczdwSXe47iWUPEZ7zWnzbMH5jVqNhuiyNjcOpiIYNe0LmAXjh4z_ImX33HEKPEYvbBVtUtriExMBmpZOxggaKuuVCcewXzocQsF5_1NNlZbIqsQRzeDTdiiKM0fO_RiNs98tJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه تراشی تازه ترامپ
رییس جمهور آمریکا:
🔹
دیگر تنگه هرمز قیمت بنزین را بالا نمی‌برد، حملات اوکراین به پالایشگاه‌های روسیه باعت افزایش قیمت بنزین شده‌ است
#کمیک_فوری
#Devil
@TV_Fori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/696431" target="_blank">📅 19:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696430">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Irf9JbEaiQoabpzjpZ2KdvIgeXJ0GJ66Tvmopw7fkqv6Jjo54dtcLmf1rL_j_S0ljn1QBDcV0EodAddI0qiHlJ5Ppf1qy5RJkShVle1331RkFvhhzLFh51lon1lSVci-AqqLzKqwX8gmQ28eisroP6t6be-uWAF4fQjEGWIHgIfeTzUh0MM5m2g4KL-s5LPZpMhmC9PEEKeb75S-j0oPdfJmJHfzOMOdmGw_7poBsXVfV1jDzNUygfT-jFuiUCCCZtrOB8PwimZyKL9rAzk7U3GRlYqUjVIrBvgzG-M0kyLqFeAHEJS1Ik49-veeySvpnp2O5_aEBk4-GOk8AxRwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میخک و کلی فایده سیو کن یادت نره!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/696430" target="_blank">📅 19:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696429">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds1R3Cu-hIh4acP1lH18qv4Ny8MICcixuXPP04BKQLsrhbLqk7k7IbVaFnahRHsDG7p47JeU6JbqJlb2E15IUeM5wwfheSYLUcKQ8gQkVWQNYFs797XgT1L-r_dKvsWG95qUZbKOfINC35IQmtXbS1tFW7tYh0C2t9vN3MWcf_52duVdmPlzb2BxlipRfIlj4xjM5hb0Y_BE2gePrpoZ4_l6FWMEzqhr-bPwMhzp6OICAr1tok_U7gk2KJsIvcW5suTzlzWMn-znROCZKDXT8kzntssCcsjLCLZwKbMVBOJ5E6q3__SACdTO60GpGp5ojnc65kYTJXjJTLmvtnJbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌گلد: خرید، فروش، تسویه و تحویل طلا در تمام دوره فعالیت در دسترس بوده است
🔹
وال‌گلد اعلام کرده از ابتدای فعالیت خود تاکنون، سرویس‌های خرید و فروش، واریز و برداشت وجه و تحویل فیزیکی طلا را در دسترس کاربران نگه داشته است، حتی در دوره‌های اختلال اینترنت، نوسانات شدید بازار و تعطیلی‌های غیرمنتظره.
🔹
بر اساس داده‌های منتشر شده توسط وال‌گلد، در این مدت به درخواست کاربر
بیش از ۸۰ هزار میلیارد تومان تسویه
و
بیش از ۱۰۰ کیلوگرم طلا
به‌صورت فیزیکی تحویل داده شده است.
🔹
وال‌گلد همچنین در صفحه «
وال‌گلد شفاف
» وضعیت سرویس‌های اصلی خود، از خرید و فروش تا برداشت وجه و تحویل فیزیکی را نمایش می‌دهد تا کاربران بتوانند وضعیت دسترسی به خدمات را به‌صورت شفاف بررسی کنند.
🔹
در بازار آنلاین طلا، دسترسی به دارایی فقط به امکان خرید محدود نیست، امکان فروش، دریافت وجه و تحویل فیزیکی نیز بخش مهمی از تجربه کاربر و نقدشوندگی دارایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/696429" target="_blank">📅 18:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d8a91ad7.mp4?token=AAw1BqQ6Jhl3x2gad8AMHGPkIctIsYdnZqyLmRmoGsY6Ab6BRQcofxXL8XOWkrX7TWNFmEaBF0b9qW0X1upCgRiAuUfaATXTnx9o4sOUnwdV7lQsxRF30p4VIUUrMnlFwnXubPdAH7nXF8aCZ2L-mNY3qNOeTVIwEx7HPd4UDoCpDvHaWuDEhA6n7jcnKNzyzdUVQUWpYozy52dYNNRrOAAOHKpAChwWwA1_Lf--qxuXl9sen0j_31_BqJFy2DZStxuV77XqZ7yoDHM5up6SHgOuiZZkRUa6zKIuifUVq5pBb4qAVaYSD2SOEtcilBUdqnCu0-mw6zu_5T-_af0dlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d8a91ad7.mp4?token=AAw1BqQ6Jhl3x2gad8AMHGPkIctIsYdnZqyLmRmoGsY6Ab6BRQcofxXL8XOWkrX7TWNFmEaBF0b9qW0X1upCgRiAuUfaATXTnx9o4sOUnwdV7lQsxRF30p4VIUUrMnlFwnXubPdAH7nXF8aCZ2L-mNY3qNOeTVIwEx7HPd4UDoCpDvHaWuDEhA6n7jcnKNzyzdUVQUWpYozy52dYNNRrOAAOHKpAChwWwA1_Lf--qxuXl9sen0j_31_BqJFy2DZStxuV77XqZ7yoDHM5up6SHgOuiZZkRUa6zKIuifUVq5pBb4qAVaYSD2SOEtcilBUdqnCu0-mw6zu_5T-_af0dlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجسمه
"
شاه ظالم" در پارلمان اروپا رونمایی شد!
🔹
مجسمه طلایی و برهنه دونالد ترامپ با عنوان «طاعون نارنجی» و نام دیگر «پادشاه ظلم»، اثر هنرمند دانمارکی ینس گالتشیوت، در پارلمان اروپا در استراسبورگ به نمایش درآمد و واکنش‌های متفاوتی داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/696426" target="_blank">📅 18:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqhq_sY5EqLeiGKeSAeh_zunSjTKHcZQFZIAozEXShMImuiZ76bNa0OxFLwRmRCdpeqtH4IwNLpBaRfDhLdMueXL286ZQW4w75bw4fsUGN26lNBKIQ6mt4TxD205e9H0EKkAIaiZiQhfWKjJwAAddzdVl57bTfcPMJD9zMEHGLDpLeSc6oarpXyWmJ9zW9ZFuUUYQd4Hh_iT38RnoN9D_Z2utfQqd99T03hzDm8Bn00b9JbPRJAJwrJ7CAKe4-9N3_Vqm5aDBOHLMVKeo-nFqpeUYf-8Jh9lqQA7thYbvia_HjUsCJdgQ2hx8FfZF_2XRCqg7spH6fo3BbMBiC_MyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویتامین‌ها و مکمل‌های مهم برای ورزشکارها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/696425" target="_blank">📅 18:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/696424" target="_blank">📅 18:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
،
چله "چهارم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
|
محمد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/696423" target="_blank">📅 18:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای بلومبرگ: سوریه قرار است به مسیری جدید برای صادرات نفت خام عراق تبدیل شود و امکان دور زدن تنگه هرمز را برای محموله‌های نفتی فراهم آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/696422" target="_blank">📅 18:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6ZAZT1lPQQdk4n37CEiBvXpJgk5WXmoutc8scm34gTxEvah0oqeuBaz4Ic8LUqxe3d-0MSJFzKx3S31zBCFvPXWPLrQjBvhUotWctAISA-zVYzofHfi16mbnvHA8WrNTNg-VYyyLdJ0cl0L_7b1x0jBJr6wjOx1UYCLyg7AS5s9BMUMJpvWDHgf0whf1NXINrp0HV3NQocmRSH6-uVw6DfCg0Ds4BVaIaufEie5Z-0ZE7C9AIkm5ehSkQeu0fCAr9rzDHbayLuqrQSM1wdYbZ3NA4mY3XKoknaE4b3xYaYfloNHF6hH1TtxIeLG5VkuJyCFuitCb_u-grGSzEJylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از پرداخت نقدی خلاص شو!
دیگه لازم نیست موقع خرید بیمه ثالث، هزینه رو درجا پرداخت کنی.
با بیمه‌دات‌کام می‌تونی همین امروز بیمه ثالث بخری، هزینه‌ش رو تو
۱۲
قسط
پرداخت کنی.
✅
بدون هیچ چک و سود و کارمزدی
✅
و بدون حتی یک ریال پیش‌پرداخت
برای خرید بیمه ثالث با
اقساط ۱۲ ماهه
، از لینک زیر اقدام کن
👇
🔗
bmeh.me/kfd715
🔗
bmeh.me/kfd715
🟣
بیمه‌دات‌کام؛ موتور جست‌و‌جو و خرید آنلاین بیمه
@bimehdotcom</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/696421" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFAKOOR | فکور صنعت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbf4_BR9VP_yTa6XzlyEbs2WenYEQP0QKOE4ImaT4BI-uCJowdaWI-u2fjM9CTj56HMTPENcdjOlMeNK-zU5v-ExrWTA7tpBnbA4UgqnvgKwE9Ur2e9iyKdEODyDQzuzbQ5TCjdj8fvMv6PvsnBT_5b-RFiSSjf0nMRMU0tFLjlzh5k3V5R2tcCUTgHzT8Ru4g0RF_q4BFWybzW72fv5sYtibKvn3V9UhlMEw3IJ1NsKacpgPDr31L23-2cDSR-ZdAwqJpSReyMh24341gh_lddK5hjZphAcpemF1horQY3o5SLZTnYHRpAg7omZAmGgV6O4aX8OTW2_Fzv3lFLbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فکور» ۲۱ مهرماه عرضه اولیه می‌شود
🔹
عرضه اولیه سهام شرکت مهندسی فکور صنعت تهران با نماد معاملاتی «فکور» روز
سه‌شنبه ۲۱ مهرماه ۱۴۰۵
در بازار دوم فرابورس ایران انجام خواهد شد.
🔹
در مرحله نخست این عرضه،
۷۰۰
میلیون سهم معادل یک درصد از کل سهام شرکت به روش ترکیبی و به سرمایه‌گذاران واجد شرایط عرضه می‌شود.
🔹
قیمت ارزش‌گذاری هر سهم ۳۵۴۴ ریال و حداکثر تعداد سهام قابل خریداری توسط هر کد معاملاتی ۸.۷۵۰.۰۰۰
سهم تعیین شده است.
🔹
در مرحله دوم نیز حداقل ۲ میلیارد و ۱۰۰ میلیون سهم معادل ۳ درصد از کل سهام شرکت
به سایر سرمایه‌گذاران به روش قیمت ثابت عرضه خواهد شد.
⚙️
@fakoorsanatgroup
🌐
www.fstco.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/696420" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2205a259.mp4?token=cOVwl-gxDpJ-n7C9cFH4q_zz088Bq_6drD4i-AdBj6-nqTerONBudF7ENe1xvsJc8QUkl20fprE0HB7wBpaq7Qm9X0lmuUuKn0qx7pDdZaZ71p2OdlD20uGsuGf9ICzk4pNZLeFijb3MZ9_n4ftVgxO2VGRw3BoisRV26vBAB7doK3UGLCWniOchHK_OeG_fL8p0L7jscqXnthFg2VN5uFhGVS42tLjCy7ZKm00YKIAKJV-k1OC_wy0z-sXA0iDvh8xkiWfrnqnw5YwrxAaWHvWJRiuoOwQ9zhAXlUKwAC98DFf5RS1EK4H1U6mMYG1MLKwG3CNCO6TPFcXPNp7CUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2205a259.mp4?token=cOVwl-gxDpJ-n7C9cFH4q_zz088Bq_6drD4i-AdBj6-nqTerONBudF7ENe1xvsJc8QUkl20fprE0HB7wBpaq7Qm9X0lmuUuKn0qx7pDdZaZ71p2OdlD20uGsuGf9ICzk4pNZLeFijb3MZ9_n4ftVgxO2VGRw3BoisRV26vBAB7doK3UGLCWniOchHK_OeG_fL8p0L7jscqXnthFg2VN5uFhGVS42tLjCy7ZKm00YKIAKJV-k1OC_wy0z-sXA0iDvh8xkiWfrnqnw5YwrxAaWHvWJRiuoOwQ9zhAXlUKwAC98DFf5RS1EK4H1U6mMYG1MLKwG3CNCO6TPFcXPNp7CUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین بستنی بهترین درمان برای گلودرده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/696419" target="_blank">📅 18:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: ما سند داریم که رژیم سعودی به اسرائیل کمک مالی کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/696418" target="_blank">📅 18:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696416">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxIWsxYqkWrLw-fjmcbzG3pjTggxy9H-KrPhlyD00mk-TWO6IeNYKb-aWp9Wfk_A4EH1uK34dsQn99s30WrTEdyHXeia8-5Bby66pookiu63Rb1WvGX4bPCegMXQCDU8zWSEmWI9mmAvMnyXz7i_-QoodRJj3XqvjxfYlT126Ol42eCW9plK9MgBSVSU0NNfmZMMRurznPudKB1KWTHefQBTp0djT1DF644HobJc1jDXSxGFumvQ3exTqZ5VYLjBhsL70O0VPYrGGHfihQ6xQitODjqTcee38KRL7MoO08xi-gYCI2FL8JwgDVXa5-6uYMfFdcqJVeDOzMU7p1of_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر همراه اول از افتخارآفرینان علمی و ورزشی ایران
🔹
باشگاه نخبگان همراه اول در طرحی ویژه از جمعی از قهرمانان علمی و ورزشی کشور تقدیر می‌کند.
🔹
مشمولان این طرح شامل اعضای تیم ملی المپیاد نجوم و اخترفیزیک ایران با ۵ مدال طلای جهانی، ۳۰ نفر از رتبه‌های برتر و تک‌رقمی کنکور سراسری و مدال‌آوران کاروان ایران در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا هستند.
🔹
هر یک از این افتخارآفرینان یک سیم‌کارت دائمی ۰۹۱۲، مودم پرسرعت 5G و یک سال اینترنت رایگان دریافت می‌کنند.
🔹
این اقدام در چارچوب برنامه‌های باشگاه نخبگان همراه اول و با هدف حمایت از استعدادهای برتر، توسعه دسترسی به فناوری‌های نوین و ایجاد شبکه‌ای از نخبگان و آینده‌سازان کشور انجام می‌شود./ تابناک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/696416" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ما ماموریت را تکمیل خواهیم کرد و همه کسانی را که در حملات ۷ اکتبر شرکت داشتند، پاسخگو خواهیم کرد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/696415" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-dB5rzbccgxHhN1afG3bdWQ0NSy2-eLP3pi4x2EAnky7lutKVR8vS6hM--JYjIoVcE7r76Cz3bN1-rCQX2gKLDqtGEnZcvQtaUs-siM19SDtuQHjv3I62SITVpptMas9ODEQ95p3W5jbVglRHguTD2ey9aXrHubQl-VNeZc6i8U1TqaZHsxvzq8TrcJjDe_saDzKKVsx_TKdSfgO8j5u_INrkepSHiK0joMbtraaCQax85ghQFEIoonmLhTeKamunnvuknJhspxVVmSYpXxcM2CSONR6mtGW-sa0qWFOuM03JWQ1l6g8q0OWsljTVg8SjclzAuec1lxRi2LSZeh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سبزیجاتی که سلامت شما را متحول می‌کند
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/696412" target="_blank">📅 17:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e761de150.mp4?token=UFiErfs7EYGy3BRnjyg4wHF2o3bXTj8gUR8JuSUSC30wQTONMUVTv2LJZLyvo2dkjlJ3Pccu6LF3Lnr0afM9xpiy_WUnEdN7-RYU9RJT1sjSsY12aLwVsm94LpheGjuYl9FVcnUUb_fUJ2IxLEbgvQ0d86jODh20xLWjM29HkKo4MEmviR8BDXT0Ew-a7mJ0mHocZUDIDP3DYjUzvyYjoGXLgwsRK2Dwr4NKrgDqLBkTKlUvdaRvfWjfsgkNjzzlyS3_Xyc2ODDUZ3kSHHD3Ug9a1oNI3dnRu8f551lrezoGW6aHyLG5spe-s4ehdX3PN7OjBjm5pkEwuM6TwSD1S0D-DyQxTUunQyck0Gi3-YJapHrOg8xlBbSvzxV4gU3DiMKggdQ2K_IHDLdVoX5G-bzgVypF_pZ5D_7ply_bJap2y8sQe4-387992HbMhvVI_uMw5cWcuHhhjcWs9ktS0M4WFQMD0NPrqoq0n_8S18AJYRR171R6IbfOznKIPwC31D8KcK344KmXzyCSBJfs10yWlai4r7aR1e_oDc3KCjhC_8YSnlnpdGB3G8pv1zZ8movsta2GGiQSGvpHP5aBxnVRqXS0RkwHy_3KCm-IyHFl3zESELAdxZ2rOAO0AtMyT36qtqLKhf01LcCjOHsQLBfbkP_sveMMpFYeskYLQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e761de150.mp4?token=UFiErfs7EYGy3BRnjyg4wHF2o3bXTj8gUR8JuSUSC30wQTONMUVTv2LJZLyvo2dkjlJ3Pccu6LF3Lnr0afM9xpiy_WUnEdN7-RYU9RJT1sjSsY12aLwVsm94LpheGjuYl9FVcnUUb_fUJ2IxLEbgvQ0d86jODh20xLWjM29HkKo4MEmviR8BDXT0Ew-a7mJ0mHocZUDIDP3DYjUzvyYjoGXLgwsRK2Dwr4NKrgDqLBkTKlUvdaRvfWjfsgkNjzzlyS3_Xyc2ODDUZ3kSHHD3Ug9a1oNI3dnRu8f551lrezoGW6aHyLG5spe-s4ehdX3PN7OjBjm5pkEwuM6TwSD1S0D-DyQxTUunQyck0Gi3-YJapHrOg8xlBbSvzxV4gU3DiMKggdQ2K_IHDLdVoX5G-bzgVypF_pZ5D_7ply_bJap2y8sQe4-387992HbMhvVI_uMw5cWcuHhhjcWs9ktS0M4WFQMD0NPrqoq0n_8S18AJYRR171R6IbfOznKIPwC31D8KcK344KmXzyCSBJfs10yWlai4r7aR1e_oDc3KCjhC_8YSnlnpdGB3G8pv1zZ8movsta2GGiQSGvpHP5aBxnVRqXS0RkwHy_3KCm-IyHFl3zESELAdxZ2rOAO0AtMyT36qtqLKhf01LcCjOHsQLBfbkP_sveMMpFYeskYLQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس فتا: فریب تخفیف‌های وسوسه‌انگیز و فروشگاه‌های جعلی را نخورید
🔹
بررسی اعتبار فروشگاه و حفظ اطلاعات بانکی، راهکار مقابله با کلاهبرداری‌های سایبری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/696410" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klma1Zp51_naL8ovXZBFmNyOUQOTTqMI58i1vSFxDHu-Xzeg0o9yjpopiCmH8yA_KH1yhJl0A7YeATMvtitttqRNBQogfPsKPN_rTXeh_9zTnoVWP1gBsK0wDCFHzF6l0knlvS0GQw46rpHRrxwczkNubT0hztdD8tIpw6CeORlOsuvnBXcjviaYnD4OXjBjHu7N3uLDR9jaD4XrGMVI4RdJSd3hvsuu_s1pSnsgcjNkFv8HcxcsMcyFPcf36yng_YCNBS21sND7iITD0rNCxktuPUo6OdTBt12IusJI_F68R6A8fqEsFNvD5QS2mQg6Vf6OojmDx6mWtdFY-dahAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملّی‌گلد داده‌های ۱۵ روزه تسویه و تحویل خود را منتشر کرد
۱۲۶ هزار درخواست برداشت، ۶ ساعته در «ملّی‌گلد» تسویه شد
🔹
ملّی‌گلد در گزارشی اعلام کرد که در ۱۵ روز نخست مهر ۱۴۰۵، ۱۲۶ هزار برداشت موفق ثبت کرده که میانگین زمان تسویه آن‌ها ۶ ساعت بوده است.
🔹
در همین بازه، ۱۷ کیلوگرم طلای فیزیکی به ارزش ۴۲۵ میلیارد تومان در قالب ۱۸۲۰ درخواست در ۲۸ استان تحویل شده و کاربران ۸۷ هزار خرید انجام داده‌اند.
🔹
تیم پشتیبانی نیز به بیش از ۲۱ هزار تماس و ۲۳ هزار چت پاسخ داده؛ میانگین انتظار تماس ۴۷ ثانیه و چت ۷ دقیقه بوده است.
🔹
ملّی‌گلد همچنین اعلام کرده که تمام الزامات اتصال به سامانه ناظر بانک مرکزی را گذرانده و به این سامانه متصل شده است.
مشروح خبر
khabarfoori.com/fa/tiny/news-3250699
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/696409" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: آل‌سعود نقش ستون پنجم استکبار را ایفا کرد
🔹
عربستان دوشادوش آمریکا و اسرائیل برای نابودی حزب‌الله تلاش می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/696408" target="_blank">📅 17:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
معاون سیاسی وزیر کشور: شعام هنوز تصمیم جدیدی درباره انتخابات شوراها نگرفته و تاریخ‌های اعلام‌ شده برای برگزاری انتخابات واقعی نیست؛ هنوز هیچ تاریخ مشخصی تعیین نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/696407" target="_blank">📅 17:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
کاخ کرملین گزارش‌ها درباره دومین مورد احتمالی طاعون ریوی در سیبری را رد کرد/ العربیه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/696406" target="_blank">📅 17:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e059daafd.mp4?token=amqswYB0gCDtGFe9LnTxJCdTMkn5UzC7wJBz1npMmKtiQsn1zBt-skjCgVLmt_aQcm5d4PdcHosAsI-CfdBmyK1He_Y03VyAQTZ2Qs0isihQ7MSLQ1skyZDJZcl3H8_uuyeb4CybTEzG2gFf3sEauGCIVIG5aC2BN3zWmwDrmUI-r8MbSq4fVih8WDbZhbTRvOSmQnDXLL6X-sYE1EpJ87QO1WC3RK-U5bgEA9rQGncTtgJSMZBxxASfupcdrTpV0zrUWq_s471sXExSAB40WE5O-fJRT_VbzgSNHlPUt9iNnfie55hPYL5ixaYaM6mDa2p_34lbED9COEn--d9NbE4az8YreSa1BtiMG7l2uuil8f_PTL-PMYH16R6EAb9qjm9aV_EvkbLl1lw8tg-BMkaRYXLGV889nTNPOe-9Y-MSTsi5Odjua-1vjwiD7QVtCVZSp5z16lQ_RpKA3AaIo_zlrQFJQnGxc7bq5ztxT4D1RwmL6X9R6ymSJ5JkjIr5MMmNJbRw-osaeWVc47-Vi5RJTKs4gquAaULKfk_O8wxTfsd0JxxpfzA7ZkRAM6Wc9C99HqXLqkEOMqqUEFeRROeWLBudt54x8OqU1w8acZYm_v4doEc3TfGKNZO3Fxc5f3oebV6hg5_eozmWIelxm5KysyKotPEI78cxYkzNxtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e059daafd.mp4?token=amqswYB0gCDtGFe9LnTxJCdTMkn5UzC7wJBz1npMmKtiQsn1zBt-skjCgVLmt_aQcm5d4PdcHosAsI-CfdBmyK1He_Y03VyAQTZ2Qs0isihQ7MSLQ1skyZDJZcl3H8_uuyeb4CybTEzG2gFf3sEauGCIVIG5aC2BN3zWmwDrmUI-r8MbSq4fVih8WDbZhbTRvOSmQnDXLL6X-sYE1EpJ87QO1WC3RK-U5bgEA9rQGncTtgJSMZBxxASfupcdrTpV0zrUWq_s471sXExSAB40WE5O-fJRT_VbzgSNHlPUt9iNnfie55hPYL5ixaYaM6mDa2p_34lbED9COEn--d9NbE4az8YreSa1BtiMG7l2uuil8f_PTL-PMYH16R6EAb9qjm9aV_EvkbLl1lw8tg-BMkaRYXLGV889nTNPOe-9Y-MSTsi5Odjua-1vjwiD7QVtCVZSp5z16lQ_RpKA3AaIo_zlrQFJQnGxc7bq5ztxT4D1RwmL6X9R6ymSJ5JkjIr5MMmNJbRw-osaeWVc47-Vi5RJTKs4gquAaULKfk_O8wxTfsd0JxxpfzA7ZkRAM6Wc9C99HqXLqkEOMqqUEFeRROeWLBudt54x8OqU1w8acZYm_v4doEc3TfGKNZO3Fxc5f3oebV6hg5_eozmWIelxm5KysyKotPEI78cxYkzNxtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای هر کاری از کدوم هوش مصنوعی استفاده کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/696405" target="_blank">📅 17:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: آل‌سعود نقش ستون پنجم استکبار را ایفا کرد
🔹
عربستان دوشادوش آمریکا و اسرائیل برای نابودی حزب‌الله تلاش می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/696404" target="_blank">📅 17:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60783ba4b.mp4?token=GOBco2xHq95WIIIeiKkA1T3XKTDta233oDv-aJB_sd8ctC5C9n4yUwseUapkdt13VQz76nuyGc2s2Sm28mYitthrhi22z3DcJBohn6yAVH1FfGGKdJ0WCM8Hj7UZWB2F5TB7niYG6JKW_2r3Y3UJpW1XtaM5yRitORu-2t-FrG_JZLOU1t2DRpgzySMlYg_p4Erd0aI1cwAVtcF2aKVXECCS_4PtoqqJJbZy3H47lN19lzmPJvyXkVAtxU8zNcRn-70QlWj69iUu4sXo-CuHox-s2jnl15L-ZGiLeyYzrIArnMcBVAQ6SGaDPXC4b9b64SAh9Uk8ZjJfOLDSIkXm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60783ba4b.mp4?token=GOBco2xHq95WIIIeiKkA1T3XKTDta233oDv-aJB_sd8ctC5C9n4yUwseUapkdt13VQz76nuyGc2s2Sm28mYitthrhi22z3DcJBohn6yAVH1FfGGKdJ0WCM8Hj7UZWB2F5TB7niYG6JKW_2r3Y3UJpW1XtaM5yRitORu-2t-FrG_JZLOU1t2DRpgzySMlYg_p4Erd0aI1cwAVtcF2aKVXECCS_4PtoqqJJbZy3H47lN19lzmPJvyXkVAtxU8zNcRn-70QlWj69iUu4sXo-CuHox-s2jnl15L-ZGiLeyYzrIArnMcBVAQ6SGaDPXC4b9b64SAh9Uk8ZjJfOLDSIkXm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهواره هنوز هم ممنوعه؟
🔹
اگر در خونه یا محل کار، از ماهواره استفاده می‌کنید، این گزارش رو به هیچ‌وجه از دست ندید!
#قانون_متروک
@TV_Fori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/696400" target="_blank">📅 17:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286dd422b7.mp4?token=dgaKB-TwauyyPCtRBl3f0KjsTYUJOWnGGyo8Gl71XS7Coc50NjeGrtjSNuYgKjmtcyNKT5z2vZD-PcETELsmABt65uhh4YajaejQZbWoQiKdzf0q9kuyDPQ6tGEmCikiKjDaNaY3GyKT9Q8Gm3KI21q-JsV1BqIZqYqyDw6fBZ0lbq7vIuwX9qmQfAAlfmfbTD42J6VX-E2E-kA-_nrwrTsEs41tyuPrQ4AhtQfPk4hiDw8p_zWj2-EUqRkrd-_mIBtkpZq6CHUbSXipYZenn4N3-TOWam6LdbDUVVD7W4xtLDunMKxC-icS0nRtBgH5Fw3BCIHrv1KU4bOW67n4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286dd422b7.mp4?token=dgaKB-TwauyyPCtRBl3f0KjsTYUJOWnGGyo8Gl71XS7Coc50NjeGrtjSNuYgKjmtcyNKT5z2vZD-PcETELsmABt65uhh4YajaejQZbWoQiKdzf0q9kuyDPQ6tGEmCikiKjDaNaY3GyKT9Q8Gm3KI21q-JsV1BqIZqYqyDw6fBZ0lbq7vIuwX9qmQfAAlfmfbTD42J6VX-E2E-kA-_nrwrTsEs41tyuPrQ4AhtQfPk4hiDw8p_zWj2-EUqRkrd-_mIBtkpZq6CHUbSXipYZenn4N3-TOWam6LdbDUVVD7W4xtLDunMKxC-icS0nRtBgH5Fw3BCIHrv1KU4bOW67n4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
کد پستی رو چطور پیدا کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/696399" target="_blank">📅 16:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وقتی زیردریایی آمریکایی «حامله» می‌شود/ ابتکار متفاوت و دیدنی جوانان ایرانی در یک انیمیشن جذاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/696398" target="_blank">📅 16:54 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
