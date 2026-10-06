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
<img src="https://cdn4.telesco.pe/file/vITvtJNjeu5ybJ6rs3XbSiJr_G3Hon71mB-ORM5q3qRNzWsh_tOBw8B9k0SoZf4n-uq9hFVu4csO6JV2-3eiabOVwNxx5EH426FdDvx4FgCsSf8W_IvQfoK9VG6ds1tA7tEmQL6KnlHnwXGcpVMHC0AYDrupRoCzgVujkDRqiDrT7Jru17v7rpJAbmWLwZjJ0kofDv2ynUO1Xx3P21n9I7Urw-93nEbP8E_sb1GsgVSpAQrbkysjQNxiJT4x1gF4X8c_dGc7L7bxHRpk_Wp0WT6gFZNHuBgW3tB-J4HnyMATbHIo-Im6a7HCwcKZ9ZVItcS17xrc6onUS57fm3Mqmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-696261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psdj-DkmpkU55po-iINDgVjHMsyemgFmYd-4GNTFZE-B5Y7vikh4O-2kUVGasqDvXkGIbqT5ol_UEx47yDM76XOrA1bkhM6jxoqOMx6_rJ8I8iQ5EA6DwSbVohESW4QriibkgI974i1_HhR6dNi3bobhXSEWLFYzF3A_czD5tnXel-0Isd0Du1GAY-TvPsURbLYAeVOfZhQhrCz-cfmYCD8xDya_7w8AoF13KCU4edcMTdGX41tpNfCkVfkE4jnRPlp6cQJYyMZJcd4Prn0kN1hVNFh59XJd60XKfF07y_yMQCrG3Fo3P-kpyCOajAg1wIdSNhILTAkq0Wwh1MUsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول ۶ ماه گذشته خرید آنلاین داشتید؟
🤔
این پرسشنامه برای یک کار پژوهشی در رابطه با
تجربه خریدتون از برندهای معروف فروشگاه‌ آنلاین هستش
و هیچ اطلاعات شخصی ازتون گرفته نمیشه
لینک پرسشنامه
لینک پرسشنامه
ممنون میشم با صرف
کمتر از ۲ دقیقه
از وقتتون، این پرسشنامه رو پر کنید
❤️</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/696261" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c218f42d.mp4?token=kBDYYdpye0KaJbiN893dYUbcchlpVD3zdNt-IHhR9ktdjn4Qy-wYSwR8668AiQFI3hemcgnzAENjBxaWCuk2KAjkfw3PWhjuqD5tsURJ5EojVj_ObIdOAA8NV6n4CRFuoWQWFT6V8dQ9c2tdvyit1q3Wo9ZlbK7mKWV3g9HQlL7GymljwpAbMTLKAT7rPCfBnUqXtnKJslBUBB1ECpM1dcWMSwpSkHtCI1Rp6oFkQTaWI_n06CtK-RF5_sGvOl-pLFxUW9myhMJ4UCdy0e90zg13Xid3_AQx2Y-a-uyuVHk2xBHAZkDCmcSWeDiMn3rAtjmC0ZR7EAi4ieAXNB6KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c218f42d.mp4?token=kBDYYdpye0KaJbiN893dYUbcchlpVD3zdNt-IHhR9ktdjn4Qy-wYSwR8668AiQFI3hemcgnzAENjBxaWCuk2KAjkfw3PWhjuqD5tsURJ5EojVj_ObIdOAA8NV6n4CRFuoWQWFT6V8dQ9c2tdvyit1q3Wo9ZlbK7mKWV3g9HQlL7GymljwpAbMTLKAT7rPCfBnUqXtnKJslBUBB1ECpM1dcWMSwpSkHtCI1Rp6oFkQTaWI_n06CtK-RF5_sGvOl-pLFxUW9myhMJ4UCdy0e90zg13Xid3_AQx2Y-a-uyuVHk2xBHAZkDCmcSWeDiMn3rAtjmC0ZR7EAi4ieAXNB6KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔨
میخ‌کوب دستی؛ یه ابزار کاربردی برای هر خونه و کارگاه!
برای نصب، تعمیرات و کارهای فنی دیگه لازم نیست کلی دردسر بکشید!
با
میخ‌کوب دستی
سریع و راحت کارتون رو انجام بدید
💪
✨
مناسب برای کارهای DIY، نجاری و تعمیرات
✨
استفاده راحت و سریع
✨
کاربردی برای خونه و کارگاه
💰
قیمت نقدی: فقط ۱,۶۵۰,۰۰۰ تومان
💳
امکان خرید قسطی هم وجود داره!
الان بخر، هزینه‌ش رو در چند قسط پرداخت کن
😉
🛒
برای خرید، همین حالا اقدام کنید؛ موجودی محدوده!
https://memarket24.ir/product/fast/57235/180124/</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/696260" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW75makijk4afGbY6o_b40VGR0ALVVwl58Rz2dM9Zn1ClIjyANBOvEZ2Y2mTH8P40dzYktHPobgxbdMJ2ReUW2zU_NbU6dG1KOrippMtnESRApa7beOpnt0xmIu56lMdlpatv1_XgKIEmF6FIIBn06XfoZv3sdGq8qd1xTiXk2UhA_mTADxDUCBvdhbwL_mFnSv-giK_YOqTFQGBIkxX_rcfz-CDNkKQxEZxp2BWU6SBOZa1sYBH9qe66qbgNAXE0jrW2Tl1o-CHMuwQ5ZjCbbyrGeSDqS9oaun6nhTCC4yWNCAVpdynkkGeq7oY_p-bQ5ebyELyQaWbXbB3EIiGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در قطع ریزش و رویش مجدد داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان
روی لینک واتساپ بزنید
👇
https://wa.me/message/R7FMNSDOGSIXC1</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/696259" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f09f86fbb.mp4?token=s1l5NjQIdq7omNe7iJ_ScK9d4egn93QoqDrv6HL2Dg0FeItrMS-8V0Rl4vv1g_oyTCQME_l4EDiNvrE86BRIjDF6RheEMgQAHQAloA8day10EnhrMpEbHBMGflMrbdTu2hL-DsXzUmBbpEbjZVDRz31xIMHAm-FE2zTv1pI3tKhMSuO0geJkifb0vDcwkeluTpprwhhDUFsXQXHWhfRQgty_ORKexvKf_kY7Wvx8zvXMQDUEUY4WjJ7sv20b5AgwuKJlkxXTLjil98MTSi5c9WIXdMvNlg3LUaWmdHAzN-MR3qESHu6vV-M63t-32h3gk2do54NabjKtQjSxdHytcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f09f86fbb.mp4?token=s1l5NjQIdq7omNe7iJ_ScK9d4egn93QoqDrv6HL2Dg0FeItrMS-8V0Rl4vv1g_oyTCQME_l4EDiNvrE86BRIjDF6RheEMgQAHQAloA8day10EnhrMpEbHBMGflMrbdTu2hL-DsXzUmBbpEbjZVDRz31xIMHAm-FE2zTv1pI3tKhMSuO0geJkifb0vDcwkeluTpprwhhDUFsXQXHWhfRQgty_ORKexvKf_kY7Wvx8zvXMQDUEUY4WjJ7sv20b5AgwuKJlkxXTLjil98MTSi5c9WIXdMvNlg3LUaWmdHAzN-MR3qESHu6vV-M63t-32h3gk2do54NabjKtQjSxdHytcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: در مورد شیوع بیماری طاعون در روسیه، آیا با پوتین صحبت کرده‌اید
؟
🔹
ترامپ: قرار است خیلی زود با او تلفنی صحبت کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/696258" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696254">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نتانیاهو بار دیگر به شهروندان اسرائیلی: به شما قول می‌دهم، ایران قبل از انتخابات به ما حمله خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/696254" target="_blank">📅 00:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAeQI0dxTeDSnv_RnmVm0hPDYATcOBs8nRoWHniE4gYDTBbqnbED7MtmqAKolkvy5hrrhxWRon55foSjOpMbJjpm97r0of8tqn9l2HpBcEqpKChsKJFQ6FsAaE4w8RUIl1D4vQlmNBdnfUKIAd6z4KT2xJfJ-MzMFbvRzIihm8vMYa82B_RWpehtlbpchxvm3bUQQ3n7TvY3FZIIF-zwXm5jPkrHvebLef7_ebQNjAjZ_KMWaFfKxxnO6qmTM74uguoadWL8HtP1dTVMWM-4ipBPq_K_3J_Y0Qo9bWhqi7T9G0W02BxRlJOrxupYFHH87QRw912nzIjZ09XzM62h9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلوتیک امریکایی با کنایه: تعداد کشته های فرانسه به ۴۶ هزار نفر رسیده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/696253" target="_blank">📅 00:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6UXzAzUA2Gd8BaeepIb2ChJrQ5Bo2qbhHk76Fq8r679RFlxbjmF1Uvd_cccT3nhZ5sNHOMDx4XgJaaBMXF9a4I9ovHnucGpH3rGctHzmCPCELxmh5IPM72JrFRb-A27wETe2bp633ThrNWx-U445fU97xXuBNi1AK5LtRZjyF1lNI58Z52zHHUc9uledBMc55iFN55QLaJ_B0hnXPmS8UQkYj7ldWefgBsGJL_eyP8Lx0lmNmc5cq6eDCdTVmDSyFh_7rSfOIPMKdaeOMeWL1NotVJHOkWwFpEhP5P3QKurWYYdP1r6Rk0qsrzDCwu314lIgwv6dH2Bbdvaf7uOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تروریست وارداتی
🔹
در روزهای اخیر هم‌زمان با افزایش تحرکات تروریستی در سیستان‌ و بلوچستان و شهادت شماری از مدافعان امنیت و یک شهروند، وزارت اطلاعات از انهدام ۳ هسته عملیاتی گروهک تروریستی ـ تکفیری در جنوب‌شرق کشور خبر داد. هسته‌هایی که به گفته این وزارتخانه، اعضای آن‌ها آموزش‌های نظامی، بمب‌گذاری و ترور را در خارج از کشور گذرانده و با هدف ایجاد ناامنی وارد ایران شده بودند. این عملیات با کمک گزارش‌های مردمی و همکاری فرماندهی انتظامی و سپاه سیستان‌ و بلوچستان انجام شده و اعضای این هسته‌ها در خانه‌های تیمی شناسایی و منهدم شدند. با توجه به شرایط موجود و حمایت رژیم صهیونیستی و آمریکا از تروریست‌ها با هدف ایجاد آشوب و ناامنی، ضروری است دستگاه‌های نظارتی و امنیتی بیش از پیش نقش فعال‌تری در مقابله با تروریست‌ها در سیستان و بلوچستان ایفا کنند.
🔹
هشتصدوهفتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/696252" target="_blank">📅 00:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f062b623d6.mp4?token=VP0XSpdzNLr7NNFoxO3HaNRRercNcvSZ9ddcJo9iD1R_QwmDVcmSJ6jE2fkNcUzq8SGdgN-glJIY2xFHoX-VESZsOVnzIUgWAAv0k-fW5M1tgr5ir3j-bk1GtF-SdRW-KXgMTXf7JdXGJqo6l6nOG_K6hiagOk8o5t1Ht0uGkHiZu9XtvGqr6sMlZpjPM2ne5Orn9hIcf1hTE5SAtFCLgOpu8FVccFNOgqRsXOgI89rbUIaNYxwPcApRvntQnGaSpTiGsWhYe50UOFLyJbtYIzOduiPsMJH8X23f3w067Npd4J15-j4ztN9JxjNez-GYqiXKdkedrUyouRbOTy4YIXtebPDOhjqf13IzbpjWqalI5zLoNa4lSfisR1hyj94f_ikqLQizT353SOLoriQXYKbK8K4mSvjMq5QyJLLdKQQ-FCeAzLfP3rIeRABJr6QIwiDsapHtZ8FL30WBf_W-vx5GY6BaNku4ay8R3itd1AGCa4uPFqMwmhrUvLPLImJQCu-TppA1JkxrnJTGKxXUQT9y-8XF7mZ_X6xG5g03ZBKMew1W6tk3cSENIsBHo1svzUO3wcBxU1nPFzWOJCaVIeZrxKPbJNKnpVHYPg7Rwa-WN-Q420jICSLy4Jw6hQAlqX0wICoOOvQyDwk2l0g5ALWgbrixUB-_YjGMkefTGHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f062b623d6.mp4?token=VP0XSpdzNLr7NNFoxO3HaNRRercNcvSZ9ddcJo9iD1R_QwmDVcmSJ6jE2fkNcUzq8SGdgN-glJIY2xFHoX-VESZsOVnzIUgWAAv0k-fW5M1tgr5ir3j-bk1GtF-SdRW-KXgMTXf7JdXGJqo6l6nOG_K6hiagOk8o5t1Ht0uGkHiZu9XtvGqr6sMlZpjPM2ne5Orn9hIcf1hTE5SAtFCLgOpu8FVccFNOgqRsXOgI89rbUIaNYxwPcApRvntQnGaSpTiGsWhYe50UOFLyJbtYIzOduiPsMJH8X23f3w067Npd4J15-j4ztN9JxjNez-GYqiXKdkedrUyouRbOTy4YIXtebPDOhjqf13IzbpjWqalI5zLoNa4lSfisR1hyj94f_ikqLQizT353SOLoriQXYKbK8K4mSvjMq5QyJLLdKQQ-FCeAzLfP3rIeRABJr6QIwiDsapHtZ8FL30WBf_W-vx5GY6BaNku4ay8R3itd1AGCa4uPFqMwmhrUvLPLImJQCu-TppA1JkxrnJTGKxXUQT9y-8XF7mZ_X6xG5g03ZBKMew1W6tk3cSENIsBHo1svzUO3wcBxU1nPFzWOJCaVIeZrxKPbJNKnpVHYPg7Rwa-WN-Q420jICSLy4Jw6hQAlqX0wICoOOvQyDwk2l0g5ALWgbrixUB-_YjGMkefTGHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افراد با هر نمره از ضعیف بودن چشم، دنیا رو چطور می‌بینند؟
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/696251" target="_blank">📅 00:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Orbg9JA1l4JhiOD64zC_KBCO0v8Ft_7rJeq4h4tLQbkxKWCiYTyHQVA1JBal-W8D-Tmx8bQNnKC60JmD2h8zJttkczUINvrIMpmMfFbblAtg9la_e1E8UBmXfE1k3eaO2CAzfDdtKaebcGuvINRbvAtiDVwtRaypRC6SJcmrhS0MnsyEw1q1WQ_5aRAIzm95OWgaZKDBtu0MOsLcco_o_wmVhk_7X9i7izw3IVuZwEv_KeazShzirfvhNhrRYw1dEgs1HA3ja3n1U1GzGVTrSJ2V3ACEtU0v1eJzALV0MMj5pdk_Mgu-xalt-a55Rip1POuaJVoB9T8TS2-G2F2CVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA-XGqda8S2kITEa2qX_oXfpWbJ8XfaQV1h_FUPf1--XyiujFnZc9jgJt031Xk-6YXmli1BEihanxkO6pXe9AryP2sTngJFRI1MEsmbGFGUR1-oMxKhpedtPeciJ8zpwCgddjuYuWK5pxCBkDqdX7SeWxv5b71knQr7FjvMRJ1bJm3ZKfy-HZxLr6g5UmMjK_c6TynLz-mmYocBQpx3sEHYNmaJLU019KKv0rBK-D9tV0_iWB2otQN1xYH4Gb87K43W9kM3Dr6DYLBJQqU2bVRdApj3BSOQcA9Ao_HafG4Q1xMEya_8q7FbQRMY0vHT1xADLJ_L6xBp10DEAn6WZ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفارت آمریکا در موسکو از یک مورد مشکوک به طاعون ریوی در منطقه ایرکوتسک خبر داد که به مرگ یک نفر منجر شده است و از شهروندان آمریکایی خواست روسیه را ترک کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/696249" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4OhtH_rFQ6Ydm0zWwceUIP_YKnbcRgWdZb_Yr5IQhFKAqY4tAUnFkE_3ph2zFbjDmeybafjdSuubGo0qTqi4dYIDSVGeAup3RoXiQJMjlyxCpdlgMdsfQkIBT0ZdIx9t3oHixWWO8jEHP0XasAS_vQsuBIXHAnm7AK1jOInchRlxvLLZPSG62EyUaiUqNQpXhM--2Pn8p6rHqByBKDFyz7ffjnvebNgfETfBjkqGs9B8HBIib7DwXljCnJrtMKDWhqfhYGZ7P5oO0XTj1NANqg932KCwXcH34X44b0_BfzHJCC7I4NYQyydlexb_PEYdIKtk6pOrmS0_Wgeh1twmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۴ اسراییل: طاعون روسی دومین کشته خودش را ثبت‌کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/696248" target="_blank">📅 00:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59388c5edf.mp4?token=GYzWE-5vky4PfprMLNTTJyaHIqyjpqR5qmHO3t9xknvUbe4QggoG7eOpm83lp2XFq6v-8urIRqFrmmABl6dIi6_e90swcZiF0bph5vL_u1CHJQQ4JLJtaVrT5kokp7oaLQC918VpUyGulTCch4WBOPAUkAYrztwqFxoJaI8sFmClCR2nuWYUDXGhuDlw1ciy6u5RiClVhCOyWIJZp2_iat3nzGZBTn92vY5LgMMedfAZZ2B9CMT5bc84qKO-G3yx4NLZgPXkeS8094R8XlH4AiXFkcWflop_0Qp5s4IuVY4DzHYGc11ut0nYu7THfkGM5de7nne3pzhXdcXKXYWW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59388c5edf.mp4?token=GYzWE-5vky4PfprMLNTTJyaHIqyjpqR5qmHO3t9xknvUbe4QggoG7eOpm83lp2XFq6v-8urIRqFrmmABl6dIi6_e90swcZiF0bph5vL_u1CHJQQ4JLJtaVrT5kokp7oaLQC918VpUyGulTCch4WBOPAUkAYrztwqFxoJaI8sFmClCR2nuWYUDXGhuDlw1ciy6u5RiClVhCOyWIJZp2_iat3nzGZBTn92vY5LgMMedfAZZ2B9CMT5bc84qKO-G3yx4NLZgPXkeS8094R8XlH4AiXFkcWflop_0Qp5s4IuVY4DzHYGc11ut0nYu7THfkGM5de7nne3pzhXdcXKXYWW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارک دوبل بدون دردسر!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/696247" target="_blank">📅 00:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هذیان‌گویی وزیر مالی اسرائیل: از منظر تاریخی و بین‌المللی، پروژه‌ای در قرن‌های اخیر وجود نداشته که عادلانه‌تر یا اخلاقی‌تر از پروژه صهیونیستی باشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/696246" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c748440d.mp4?token=uxbN9TnkedHp2CCpT0UC6FVroLGg3pfsCfrNK-sh8HlI3KqKg3w0rYwi9xmNdsxreLoaCa5eSwofpSVX0yiz1MMVPPI6a-rUtjgZpXFtRuzUY9QGPxQWGF92y_G-vIvsm2FwhdSAYj4xGXV4rGJEYYzdAg6lZ4D-jhUz8B6mQPyenlfZB0QSksT-EWGCN8XzDcE7fOocDT1nppSo9R3PFB3ECjwW-j7DO62WPLuJJKNuyg0PSgL4EbeggWeRjva_NJbEtmXQoI8LvaoINkzyu_jTF9oboPNAJn5jcZ53Y0JGcfdTTTrN63SZ1FkSS0AgkH51t--3PHmclqB0Eb7eEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c748440d.mp4?token=uxbN9TnkedHp2CCpT0UC6FVroLGg3pfsCfrNK-sh8HlI3KqKg3w0rYwi9xmNdsxreLoaCa5eSwofpSVX0yiz1MMVPPI6a-rUtjgZpXFtRuzUY9QGPxQWGF92y_G-vIvsm2FwhdSAYj4xGXV4rGJEYYzdAg6lZ4D-jhUz8B6mQPyenlfZB0QSksT-EWGCN8XzDcE7fOocDT1nppSo9R3PFB3ECjwW-j7DO62WPLuJJKNuyg0PSgL4EbeggWeRjva_NJbEtmXQoI8LvaoINkzyu_jTF9oboPNAJn5jcZ53Y0JGcfdTTTrN63SZ1FkSS0AgkH51t--3PHmclqB0Eb7eEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیال پردازی ترامپ: ما در واقع ایران را به پایان رساندیم، به محض اینکه بمب‌افکن‌های B-2 به آنجا حمله کردند، زیرا این پایان برنامه هسته‌ای آن‌ها بود #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/696245" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a175aade2.mp4?token=NDUg2fd7d_oBWkE_Bmrjv1W6peVQjQazkd06bQyQpi_8s67Xgge6X_q0ay3I92j41uJCMoDs7K0yoMQojwXLg65OvNGVapTBbPFD20UscQraA6cuVF40Wisc_-lsNq6zm7tLIA0oI1285OVN_nzXPOvo4YsPI9D36ah2lCad0i9XBtbNQyvlpmfWMSRrSJY39dnVaDVnQ6Ed5nm5rfveSfSZThfrqhVJvwCjnYCYUKeTjRkWlIaYJDpNGtmKGgQmerTvNZk3jQ2QjDuUsElDo1pqslmByz0wk7KRL4iZIU9C60EEso2AHaGWuAZ3TChGSG2dFCaUOCM1MMGPwDguUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a175aade2.mp4?token=NDUg2fd7d_oBWkE_Bmrjv1W6peVQjQazkd06bQyQpi_8s67Xgge6X_q0ay3I92j41uJCMoDs7K0yoMQojwXLg65OvNGVapTBbPFD20UscQraA6cuVF40Wisc_-lsNq6zm7tLIA0oI1285OVN_nzXPOvo4YsPI9D36ah2lCad0i9XBtbNQyvlpmfWMSRrSJY39dnVaDVnQ6Ed5nm5rfveSfSZThfrqhVJvwCjnYCYUKeTjRkWlIaYJDpNGtmKGgQmerTvNZk3jQ2QjDuUsElDo1pqslmByz0wk7KRL4iZIU9C60EEso2AHaGWuAZ3TChGSG2dFCaUOCM1MMGPwDguUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: همیشه از رهبران کشورهای مختلف تلفن‌هایی دریافت می‌کنم که در آن از من به خاطر جنگ با ایران تشکر می‌کنند
🔹
من به آن‌ها گفتم: "خیلی خوب. چه زمانی قرار است هزینه آن را بپردازید؟" #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/696244" target="_blank">📅 00:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b24259bc.mp4?token=VKgRAil2crL3h_bWTtTecVUzs9DCKlEEgg_8HTYwaHzbyYja3tXPIaA_FGxP5ENoxtaM-ba_48JNDs_XQzY3TABxmpO5tIPjFW7DCuZa6eudejkzOaP2CIXUGTF5LPIhyijaAGwtjMI40NeUx_c6S7qwjH_Vpa-_BD6A8-ydxMBdUboxasy-j1ChEI7CVXPsijFLLbwBQpNmeu1GA-PCRyzOUk7bi05MoHiMJBbZz9UPpI6hEWrxAeUcScv2B9wdsHJ4AgNrwv6TJUBOeiWcft9AUISp3sDqJo5-mQKowqtbLaqLf1c3m1zMqFfgSqCTgMm8jPzlym3cCk4525LYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b24259bc.mp4?token=VKgRAil2crL3h_bWTtTecVUzs9DCKlEEgg_8HTYwaHzbyYja3tXPIaA_FGxP5ENoxtaM-ba_48JNDs_XQzY3TABxmpO5tIPjFW7DCuZa6eudejkzOaP2CIXUGTF5LPIhyijaAGwtjMI40NeUx_c6S7qwjH_Vpa-_BD6A8-ydxMBdUboxasy-j1ChEI7CVXPsijFLLbwBQpNmeu1GA-PCRyzOUk7bi05MoHiMJBbZz9UPpI6hEWrxAeUcScv2B9wdsHJ4AgNrwv6TJUBOeiWcft9AUISp3sDqJo5-mQKowqtbLaqLf1c3m1zMqFfgSqCTgMm8jPzlym3cCk4525LYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهمات ترامپ: تنگه هرمز متعلق به ایالات متحده آمریکاست #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/696243" target="_blank">📅 00:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
یاوه‌گویی‌های مکرر ترامپ: کل ناوگان ایران از بین‌رفته است!/ ایران دیگر قلدر خاورمیانه نیست! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/696242" target="_blank">📅 00:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knPYhYuROAl0ZWQeWFZ9YiYNFQOuar0TBdPuCyNQGinFKYk1o3pne-jjbci8zZtI6TVl-_uMhSQT5pdY1X23bH4T7qOMtordbW3qjglnZwkScyfGrACZ7moKmNEgY8oSpON2OUm1BNq7pkMlRcjwGyKcvVsJjMygC79GZxl_idh7qnTuxajnYFhaUNqc4AF_URenwSpYOxuBcXkUGpPt44sYCkj3dg4tBX4NIB70YqCadg58PyFucO4fFTGmHMrGLAv-rwO5FKUJBwFLaDLEiknzlDx4GNNzVw5CGDXTtVOabCPuiFeNb2-62GRNAMy9umVjdHpeXX3my4kPzJRiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/696241" target="_blank">📅 00:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ترامپ بازهم وعده توخالی داد: بعد از پایان جنگ با ایران قیمت ها پایین خواهد آمد! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/696240" target="_blank">📅 23:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ: به زودی متوجه خواهید شد که ما چگونه کارمان را درمورد ایران به پایان خواهیم رساند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/696239" target="_blank">📅 23:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبر عفو امیر تتلو کذب است
🔹
ویدیویی که از نسیم، خواهر تتلو در دقایق گذشته منتشر شده قدیمی و مربوط به یک سال قبل است.
🔹
نسیم سال گذشته در همین ایام در یک ویدیو خبر از عفو امیر تتلو داد که صحت نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/696238" target="_blank">📅 23:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106ffa55c9.mp4?token=S2BnLdTJ2aWy9SHi3H4BJrQQgnUw8Z90yTQGVe8d5uz3HKsZpwE7c2EPqNeVggXkpRoFUrm-RKHcxXUa3fdSTydt7ENcR3vu0SihQKs32W0I_7ky3qeeRZGunqpW_nTHmlLiK0Rxo8biAIOPXIkBH9LYtgbYYNCj6sNnWHsG5dDafv10pDBLcnzeoaNr6GLqru0dh1zv2xJO8U_89fawedbd5U47KRklBlO9NSNqLYcTH0YFGZHVsps7ltALv285bNEZncGjIf4Wprcnetv1QisVwyyp1isQA2W3tbhPSpxQS6b-alvYyL8AN2rrfOhhWqd5DRKTl-XAdKLb8ZCUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106ffa55c9.mp4?token=S2BnLdTJ2aWy9SHi3H4BJrQQgnUw8Z90yTQGVe8d5uz3HKsZpwE7c2EPqNeVggXkpRoFUrm-RKHcxXUa3fdSTydt7ENcR3vu0SihQKs32W0I_7ky3qeeRZGunqpW_nTHmlLiK0Rxo8biAIOPXIkBH9LYtgbYYNCj6sNnWHsG5dDafv10pDBLcnzeoaNr6GLqru0dh1zv2xJO8U_89fawedbd5U47KRklBlO9NSNqLYcTH0YFGZHVsps7ltALv285bNEZncGjIf4Wprcnetv1QisVwyyp1isQA2W3tbhPSpxQS6b-alvYyL8AN2rrfOhhWqd5DRKTl-XAdKLb8ZCUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: به زودی متوجه خواهید شد که ما چگونه کارمان را درمورد ایران به پایان خواهیم رساند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/696237" target="_blank">📅 23:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
خبرهای جذاب را به انتخاب مخاطبان وبسایت خبرفوری دنبال کنید
🔹
🔹
نشت آزمایشگاهی طاعون تایید شد | ۳ بیمارستان قرنطینه شد | طعنه ترامپ به شیوع طاعون روسیه: باکتری‌ها باهوش‌تر شدند!
👇
khabarfoori.com/fa/tiny/news-3250303
🔹
با آمریکا یا بدون آن؛ نقشه اسرائیل برای عملیات مستقل | تهران ممکن است معادلات حمله را تغییر دهد | تقویم جنگ تغییر می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3250265
🔹
نتانیاهو نزدیک‌تر از همیشه به سقوط | بی‌بی کمتر از یک‌ ماه به انتخابات دست به جنون می‌زند؟
👇
khabarfoori.com/fa/tiny/news-3250387
🔹
روایت تازه از زندگی خصوصی مرد شماره یک فلسطین در سپاه قدس؛ همسر سوری حاج رمضان کیست؟
👇
khabarfoori.com/fa/tiny/news-3250333
🔹
پشت‌پرده استعفای وزیر نفت؛ ۳ روایت از یک جابه‌جایی پرابهام | پاک‌نژاد چرا رفت؟
👇
khabarfoori.com/fa/tiny/news-3250353
🔹
صفحه ویژه اخبار پربازدید خبرفوری را دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/696236" target="_blank">📅 23:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پرواز تهران-تبریز به مهرآباد بازگشت
🔹
پرواز قشم‌ایر به‌دلیل شرایط نامساعد جوی، کاهش دید و رعدوبرق امکان فرود در تبریز را پیدا نکرد و به مهرآباد بازگشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696235" target="_blank">📅 23:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8751deb3a7.mp4?token=GCHq56cp7pQM0T5vVuLzIELNJ36Z9qfUGAtpICnsgUNj-Tc3YXZmiI9JBpcTbRLJHQw-1lwOJIcpzolvQ3GB-s5p6Dj3D4iH6NxdeToYFY2Lm3mozSEVFYZCKWCwGpiViuYpAwpZvxHrRqu7TMzseIA48Mn1-qM1jPHILLIlrbnx8flwsUkcdi2LuCR8Cx1DrgLEEOraetP2gBKRjpkUoXNqCPCorYagsC_9uJxnSap2v87p0njvdCKJC_z1IeyaAWAlV2frnUy0IK59Up4BXGDt2HAFxI7jTnmLRwEA1Crmwe2C3LYltlfI7fsJvqQvBXfR-wexlC3XtPmIzCtHRAgWxDHAUVsVTS6MhRwrkAyCYh7KzHUwOa4e2goo13TDwi8WAuBlFsXwq-FejEu4h5RCk3oDQI1YJ79hzQeRxYiTxi3JIyx8f75vTjHgIN_u9dtN93A_Kt80MaVfGzAzgzF-RDiLk_jAgLjiZPJLwMT5dretmXR7dTLWYTmQRPWK2mKHtXgI6h6X2IIeapu9GahKvw7RDDZqrYXVqv6WbAiPUHgsQ2IdDJhtIvktT7Tlpvf5tQvcECJpbQVgCV1xp_kiI6FVcikC8OEAvcoyMLw9wgx4df6DVxplys66AFqLDXN5kdV_fiDP9Pfi2ZYi0AWzYwt5_69di70VfN2J1EM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8751deb3a7.mp4?token=GCHq56cp7pQM0T5vVuLzIELNJ36Z9qfUGAtpICnsgUNj-Tc3YXZmiI9JBpcTbRLJHQw-1lwOJIcpzolvQ3GB-s5p6Dj3D4iH6NxdeToYFY2Lm3mozSEVFYZCKWCwGpiViuYpAwpZvxHrRqu7TMzseIA48Mn1-qM1jPHILLIlrbnx8flwsUkcdi2LuCR8Cx1DrgLEEOraetP2gBKRjpkUoXNqCPCorYagsC_9uJxnSap2v87p0njvdCKJC_z1IeyaAWAlV2frnUy0IK59Up4BXGDt2HAFxI7jTnmLRwEA1Crmwe2C3LYltlfI7fsJvqQvBXfR-wexlC3XtPmIzCtHRAgWxDHAUVsVTS6MhRwrkAyCYh7KzHUwOa4e2goo13TDwi8WAuBlFsXwq-FejEu4h5RCk3oDQI1YJ79hzQeRxYiTxi3JIyx8f75vTjHgIN_u9dtN93A_Kt80MaVfGzAzgzF-RDiLk_jAgLjiZPJLwMT5dretmXR7dTLWYTmQRPWK2mKHtXgI6h6X2IIeapu9GahKvw7RDDZqrYXVqv6WbAiPUHgsQ2IdDJhtIvktT7Tlpvf5tQvcECJpbQVgCV1xp_kiI6FVcikC8OEAvcoyMLw9wgx4df6DVxplys66AFqLDXN5kdV_fiDP9Pfi2ZYi0AWzYwt5_69di70VfN2J1EM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو هواپیمای آمریکایی و کانادایی در باند فرودگاه لس‌آنجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696234" target="_blank">📅 23:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5d01a674.mp4?token=WeoLzMDlBvk3OLMP6jXOSHVBZFiYTEws_SU-dNeLPuxuzzGKVTepiwRs_bmJyG9q2rRj3JCom5cETNZ2bAsbbMQUdDottyO_tDp6yoN0H1i8YMO9_47Gw79DhuBuOpjGECjGe3ucVzv569-soaA90SYXBdOFD3Xj5XcX1gZo8chHAqh1ybRCNioVkQvprq8q-49vWs_s5Icg9PAoCa_lSMS9UZc0g4UH4pJqTLCIXWrt0ImAxbylfzv6FhH_NB5t8QKrDlpKDDzmLtLrY6TC8ZkYI5ixTuGjD1WJWrpJv7ifqhJuDzofzDQfN1ShPqrsyN5DY0Do7acprddjLnt98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5d01a674.mp4?token=WeoLzMDlBvk3OLMP6jXOSHVBZFiYTEws_SU-dNeLPuxuzzGKVTepiwRs_bmJyG9q2rRj3JCom5cETNZ2bAsbbMQUdDottyO_tDp6yoN0H1i8YMO9_47Gw79DhuBuOpjGECjGe3ucVzv569-soaA90SYXBdOFD3Xj5XcX1gZo8chHAqh1ybRCNioVkQvprq8q-49vWs_s5Icg9PAoCa_lSMS9UZc0g4UH4pJqTLCIXWrt0ImAxbylfzv6FhH_NB5t8QKrDlpKDDzmLtLrY6TC8ZkYI5ixTuGjD1WJWrpJv7ifqhJuDzofzDQfN1ShPqrsyN5DY0Do7acprddjLnt98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید صفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696233" target="_blank">📅 23:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
کانال ۱۴ اسراییل: طاعون روسی دومین کشته خودش را ثبت‌کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/696232" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613b040bef.mp4?token=Y0J2id7fowLT99K-cmkDQxCvIfPxqvPr5sWAfmEPzC8MHmpyPj1Yn6qLQUSk32XFn1zNms0yvAcMgbmMmI9lxbJkKUM8-zj6busQ3gfyg_n2_Fc7opdp6-qlugUMnxx4IRHKqdtd6UB8si8m6JWAsYtSVTdgHGPFqjXGyuZ6I1BdLR2PFhnrEiBtbelbHOU_RmXwcGbs3k-f12ervrcAtsayAM9JqMEfRuMMBscBPYKmcOKEp4ODbTG5FAQ343hIVEpry4y0tKBWx-t2BGBKHOvLvgWZEYJgNqXI7JWQ7Nbb_fR7DWjj7qzfpRRMKDcmX5SjrEj2IB_8lkOhdtlr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613b040bef.mp4?token=Y0J2id7fowLT99K-cmkDQxCvIfPxqvPr5sWAfmEPzC8MHmpyPj1Yn6qLQUSk32XFn1zNms0yvAcMgbmMmI9lxbJkKUM8-zj6busQ3gfyg_n2_Fc7opdp6-qlugUMnxx4IRHKqdtd6UB8si8m6JWAsYtSVTdgHGPFqjXGyuZ6I1BdLR2PFhnrEiBtbelbHOU_RmXwcGbs3k-f12ervrcAtsayAM9JqMEfRuMMBscBPYKmcOKEp4ODbTG5FAQ343hIVEpry4y0tKBWx-t2BGBKHOvLvgWZEYJgNqXI7JWQ7Nbb_fR7DWjj7qzfpRRMKDcmX5SjrEj2IB_8lkOhdtlr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر نمیدونید دقیقا چه شغلی برای شما مناسبه، این تست رو انجام بدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696231" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV_XSgE-MkepC8YPfthi3Vas9FnntgLrK4-j9dv5REBs_CcQ2wu8PWYEVXEb8W7SF0uVhnY-MY7MnfVoXatIRupP6_5sy_mtUYnpHE5bFG_KvYgE8RyU72ASqUsXNcjoGa8kezbDt7cNL_Vv07ArBIlf1VFJYdh32Ou2Nhb49hT-Nz7h-I_sb6GqaX1BKxpC40rf1ifwf1LxcYs8ef-hv5-L0DuFsHvjpHM3daLwncRPb6-cxlT__GnHr9NYpf7oeCNRQCwrSG3daIeizZMPRwImoaRgw-k8Fm28VWKnihOSo8hLeRVhpUHGzrykVt5nuI59G4Oo9104RuYBHnmTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با آمریکا یا بدون آن؛ نقشه اسرائیل برای عملیات مستقل | تهران ممکن است معادلات حمله را تغییر دهد | تقویم جنگ تغییر می‌کند؟
🔹
رسانه عبری «اسرائیل هیوم» در یادداشت تازه خود مدعی است ارتش اسرائیل و آمریکا همچنان همکاری اطلاعاتی و عملیاتی نزدیکی دارند، اما هم‌زمان اسرائیل خود را برای احتمال عملیات مستقل علیه ایران آماده می‌کند؛ عملیاتی که می‌تواند بدون مشارکت مستقیم آمریکا انجام شود.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3250265</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696230" target="_blank">📅 23:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOH28cLOkqUkkdjmc59SbhxZuwJpWG-rQjsXEemo23cSwRPyGrahvw6BYKnNqy73J4Emqpmkpk5kWKU0gnHHZX51XndJZGae53GBY1eAqPqFgLIzrWzir0SIVWYPfs37Zn-z2ENFpQJ_-UH7WZnNymRdnkqnKKc9bJ-jXsONbvEmAw8beEy11DvxI4cyeDr-rQkBQMvc_4vmj-CgqfxYU4LT6JVAbQIqI2Z7yW5eix3tJoeKRFsWS28qMC0aUBNeDXuLgaUNE4zpwSwVgSL74zgpEBQ2dvXfuni7N39wnm2_byxolnGt18F07rHw7MMLmFKp-9ut39plYLijb6dYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل رایتل: اپراتور رایتل سودده و در مسیر توسعه است؛ واگذاری سهام، فرصتی برای ورود شریک راهبردی و سرمایه هوشمند است
🔹
مهدی فقیهی، مدیرعامل رایتل، در واکنش به برخی مطالب منتشرشده درباره واگذاری سهام این شرکت گفت: تعبیر واگذاری سهام رایتل توسط سهامدار به «ورشکستگی»، با واقعیت‌های مالی و عملکرد شرکت همخوانی ندارد.
🔹
فقیهی افزود: رایتل طی سال‌های اخیر سودده بوده و در سال گذشته نیز زیان انباشته شرکت به صفر رسیده است.
🔹
وی ادامه داد: واگذاری سهام، تصمیم سهامدار در چارچوب سیاست‌های واگذاری است و می‌تواند فرصتی برای ورود شریک راهبردی و سرمایه هوشمند به رایتل باشد؛ شریکی که علاوه بر سرمایه، فناوری، بازار و ظرفیت‌های جدیدی برای شتاب‌بخشی به توسعه شرکت به همراه بیاورد.
🔴
مدیرعامل رایتل همچنین از برنامه این شرکت برای توسعه ۵G، حرکت به سمت «اپراتور صنعت»، شبکه‌های اختصاصی، اینترنت اشیا و توسعه خدمات سازمانی و دیجیتال خبر داد و گفت: در بازار مصرف‌کننده نیز بهبود تجربه مشتری با ارائه سرویس‌ها و خدمات جدید و متمایز، از اولویت‌های اصلی رایتل است.
🔴
فقیهی تأکید کرد: رایتل ضمن احترام به رسانه‌ها، انتظار دارد تحلیل‌ها و اخبار بر پایه اطلاعات دقیق و واقعیت‌های مالی شرکت باشد.
🔴
وی در پایان گفت: رایتل حق پاسخگویی و پیگیری قانونی نسبت به مطالب خلاف واقع و آسیب‌زننده به اعتبار شرکت را برای خود محفوظ می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/696229" target="_blank">📅 23:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Fg_rJHWbtz6yi5AK9JRK5dDpo2Cxh3DabYTti6s9XmCWMqSHKsqK0vkc_bpHztUb5aIlhN29KrpSeLVUJ5E9FqsdVJ2r2pG8gj3bkUsIxpwnK-dNu6gNnpIl50l1x8PzeCd27ZojOgAa86IU_OduFBB7NDoh_RMMBXsnL-9OTw9befO5ODE-aI3sOtNJ6E5jvHpwj2sK1iT3E-SwoiwfcdtposqpG3hslduPVUFFE7ioqxcUtqwycw7fkV5WnoPWa8OwWWUnx99Io1oTZuMbopct1gYZg98HMgpFqArGoem8Gf9tAGX0k_iKIhWJVwP5cICmMnfg6CM0v2Ebpt5nZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Fg_rJHWbtz6yi5AK9JRK5dDpo2Cxh3DabYTti6s9XmCWMqSHKsqK0vkc_bpHztUb5aIlhN29KrpSeLVUJ5E9FqsdVJ2r2pG8gj3bkUsIxpwnK-dNu6gNnpIl50l1x8PzeCd27ZojOgAa86IU_OduFBB7NDoh_RMMBXsnL-9OTw9befO5ODE-aI3sOtNJ6E5jvHpwj2sK1iT3E-SwoiwfcdtposqpG3hslduPVUFFE7ioqxcUtqwycw7fkV5WnoPWa8OwWWUnx99Io1oTZuMbopct1gYZg98HMgpFqArGoem8Gf9tAGX0k_iKIhWJVwP5cICmMnfg6CM0v2Ebpt5nZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بانک‌ها باید از بنگاه‌داری دست بردارند و املاک غیربانکی خود را واگذار کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/696228" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کنگره آمریکا در گزارش اخیرِ خود فهرستی از جنگنده‌ها، بالگردها و پهپادهای آسیب‌دیده در جنگ با ایران را اعلام کرد
🔹
بر این اساس، فهرست هواگردهای خسارت‌دیده ارتش آمریکا در جنگ با ایران به شرح زیر است:
۱۲ فروند F-15
۱ فروند F-35
۲ فروند جت A-10
۷ فروند هواپیمای سوخت‌رسان KC-135
۱ فروند E-3 Sentry
۲ فروند هواگرد عملیات ویژه MC-130J
۴۵ فروند پهپاد MQ-9
۱ فروند بالگرد آپاچی
۱ فروند پهپاد MQ-4
۳ فروند پهپاد MQ-1
۱ فروند بالگرد امداد و نجات
۴ فروند بالگرد AH-6
۱ فروند بالگرد Sea Hawk
📲
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/696227" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
همتی: کالابرگ ۴۲ میلیون نفر حداقل ۵۰ درصد افزایش می‌یابد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696226" target="_blank">📅 22:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ: مقادیر بسیار عظیمی، میلیون‌ها بشکه نفت، فقط طی چند روز گذشته تحویل داده شده است
🔹
ما اکنون نفت را با سطوحی عبور می‌دهیم که حتی به سطح پیش از جنگ رسیده و گاهی نیز از آن فراتر رفته است. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/696225" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ: مقادیر بسیار عظیمی، میلیون‌ها بشکه نفت، فقط طی چند روز گذشته تحویل داده شده است
🔹
ما اکنون نفت را با سطوحی عبور می‌دهیم که حتی به سطح پیش از جنگ رسیده و گاهی نیز از آن فراتر رفته است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696224" target="_blank">📅 22:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e439ad57a1.mp4?token=IWN-5hUzKmYaHw9nOzqOCekrbKg0locEys1HvU7YkhG8MSOsit5jXyS2BNZZnSVswhv2Kd0QLNanFMR-T1baHUxqHGk28rnOSLETR9gj8ppCfJ7NreAT1AQ49AUwDaxaWJrr8acZ7kYtKgN6ylS9yU4g50B7bVhJ9dP05TXDH8QD-udAT5uZV2s0FiDEKsvfeM1CMYp1inUiskeFOYtHeUAeeQHqiQ0gqGZgErooKWSu-ciyRt73WkR2WBbfbKDNdX89w0FUG-3BNyRJgzDz_noz-TQkHVk0Nc8I_sIUPbWy9wuVFAuOPyJ-4osJS10ppMwBHm3iyeDigpqcrRGCuLOB6Qsp923o-PpaxUimxtmbC3Ossb40GuPaplJbD22hf-ONRVuDqG5EWNWysUzTxlzsUr2QXR2uy0AFHgGzc5jbBHhzpQHI9ow2HHswc8kHsigI_whJqRIBh8xl50cugelzXCKpbEf9n-LGhJ5Uz4GT1vLe2eIXKavqvkTRqswlMXAGua3ftoT4aO59g_ShWbByJC8i90xppM_8ihzRUFO-xU-BM2NF4xeDkfbf64PCLlBFzltsSm7sjn5XA-kfJ_Z80rEyPdI_CMNpizgtH8BuvaBUuK_DXUnrkFHI0sT6CdTHXExzCl_-l2ZSPfbXRamKl28lt80aJt0bxP5hy0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e439ad57a1.mp4?token=IWN-5hUzKmYaHw9nOzqOCekrbKg0locEys1HvU7YkhG8MSOsit5jXyS2BNZZnSVswhv2Kd0QLNanFMR-T1baHUxqHGk28rnOSLETR9gj8ppCfJ7NreAT1AQ49AUwDaxaWJrr8acZ7kYtKgN6ylS9yU4g50B7bVhJ9dP05TXDH8QD-udAT5uZV2s0FiDEKsvfeM1CMYp1inUiskeFOYtHeUAeeQHqiQ0gqGZgErooKWSu-ciyRt73WkR2WBbfbKDNdX89w0FUG-3BNyRJgzDz_noz-TQkHVk0Nc8I_sIUPbWy9wuVFAuOPyJ-4osJS10ppMwBHm3iyeDigpqcrRGCuLOB6Qsp923o-PpaxUimxtmbC3Ossb40GuPaplJbD22hf-ONRVuDqG5EWNWysUzTxlzsUr2QXR2uy0AFHgGzc5jbBHhzpQHI9ow2HHswc8kHsigI_whJqRIBh8xl50cugelzXCKpbEf9n-LGhJ5Uz4GT1vLe2eIXKavqvkTRqswlMXAGua3ftoT4aO59g_ShWbByJC8i90xppM_8ihzRUFO-xU-BM2NF4xeDkfbf64PCLlBFzltsSm7sjn5XA-kfJ_Z80rEyPdI_CMNpizgtH8BuvaBUuK_DXUnrkFHI0sT6CdTHXExzCl_-l2ZSPfbXRamKl28lt80aJt0bxP5hy0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از کنکور چگونه انتخاب رشته کنیم؟
محمدمهدی محبی، روان‌شناس و مشاور تحصیلی:
🔹
انتخاب رشته نیازمند نگاهی همه‌جانبه است؛ نباید تمام تمرکز را تنها بر یک رشته خاص گذاشت، بلکه باید شرایط خوابگاهی، هزینه‌ها و سایر گزینه‌های متناسب با رتبه را نیز به دقت تحقیق و ارزیابی کرد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696223" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
رئیس کل بانک مرکزی: تا نیمه مهر حدود ۲۴.۹ میلیارد دلار ارز برای واردات کالا تأمین شده که نسبت به مدت مشابه سال قبل حدود ۱۲ درصد کاهش دارد
🔹
این کاهش عمدتاً مربوط به بخش صنعت بوده و تأمین ارز کالاهای اساسی کاهش نداشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/696222" target="_blank">📅 22:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696220">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
عبدالناصر همتی: به بسنت پیام دادم من به راحتی می توانم ۲ میلیارد دلار اسکانس در بازار می دهم. فکر نکنید با توییت می توانید اقتصاد ما را بهم بریزید
🔹
بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود. ده روز از این دو هفته گذشت و اتفاقی نیافتاد.…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/696220" target="_blank">📅 22:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696219">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/696219" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/696218" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696216">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb-vSzpD6uhnG2Mq1-ntpe6XRTLvKEgGz59Hw7WtIzSddNyBmAvTfD9qFVVKW8TpSc63YgBqz3jpB8IhHzcTG43l1b2K0wp7ZNmjokD1giXDnPJ-f6XifMwxT1EjyhyTmwQsbfsM-bnl-b7hHV8vpUNSJvDpRk-abhZUNhzG3gbhMr8aLDL5W771Q3GQxC4rM0raGsjV-BVU3bTYWgJQeEqQyqUs-BWy5myy6EmhZHswYOxzj0Ld3SkDvimC6sVynOUSA_m9Z7DZprUaWZlgkm9c6Ae0xG2tdgFEjZ6iQlvE6pwiDPZXYlh1lvaAEQ6uMTalssKJEY-8rMlQvNbl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست وزرای مستعفی در ادوار مختلف دولت‌ها
🔹
از دولت بنی‌صدر تا دولت پزشکیان؛ کدام وزرا استعفا دادند؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696216" target="_blank">📅 22:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh1KdOJWxI259ZNL7V4kGPQXdEzawSNWcP-NIWTEGihHHLbbQAfZCrvfNmwuKDVTBmj89FhJ9lnoJMcK-1lScLRERdfPJ7B4Ok9ObXMcze315Jln6wp8aIDjW5UAG1adojpFrklf8Ea_YNe36FHzWwT27xe0MYcik3LIzwApfNFGU8Aua63qN3Kyo1TKdnUrOi-yW2zuaDMHucu9ZdJvRxZq_aXzU_19ezDOY6Zxf9tynXFm_0lHDieiQRuwD3Sh5sw8NKSPon5-rcbcPzvuWAPPyA4oTPUUrxs5HO5YEr-YxEopsHIvqk-UiEnkoD6mKu3Opx249t8DieGISBekCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/os2iErzezQnTYFtl4QQU_QrC0zibrn-IkdhdsdekBg-kuMQhXIhcwQ-exCNNtIanz1op4yyKMr07t5kwXmPcmLIk506v1m89Y8ImcUP2DDlIAcvFMC8tARWPdAJkOByG-NBXQNMst3Mo4eRTxeIqEI3yHteHGw94EAcf6ct5rkf4wevnPtNiZwg0IXnX-mrWAd3Tgw6hCTsU0wo55EzCIVlrTeTsITSJaAkfhI8b_PiY4sKDd6f-nFz9yEuz0V-NnBVUcT66Lbvexpt89TKxUY9qIcStQHorgo9V_LC5p0iik6vs3OKxRUqisEEVA9lf0sccIykfXTlCZ3c1OTEewg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل‌های iPhone 18 Pro پس از یک هفته از خرید، شروع به رنگ‌پریدگی می‌کنند!
🔹
برخی کاربران از تغییر رنگ مدل‌های قرمز و مشکی آیفون ۱۸ پرو، به‌ویژه اطراف دوربین‌ها، خبر داده‌اند؛ مشکلی که یادآور تغییر رنگ مدل نارنجی آیفون ۱۷ پرو است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/696214" target="_blank">📅 22:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فاکس نیوز: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696213" target="_blank">📅 22:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_9d9OLlayUM2sSpnuquQs2VFywMZpleVAmMgsFmY1tXUZ7v1BA43_bC5RgSj_f_XpKXh5xLgoCdHvx_D3NPxNdF8yWZzykXs6CuOEckMuLbSmrYJ-LkaL60NN5ArLPv0YcVMxkBucGU3Hm4BgRhCIjuNwUzFb-89qGhsANkd68bX7psZHNfBFcXd_jtLwOCcjv-6DXG75pp1jAh5xvNaqCU-iG_OMncWR09LsYmGbmEBl33MLy5acDBiaE7unK3ggK94Dz0n0wQ0t3XhCzPZl4jznV9KOeZBlgHs3R1Hnpm0Kj1AQeelld6qqamnsSV-_oimqFWkMkXXMjIrX8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام رئیس بانک مرکزی، نرخ رشد نقدینگی نسبت به ماه های قبل، کاهشی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696212" target="_blank">📅 22:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696211" target="_blank">📅 22:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoMCToS6fxHK30g91lTOGGuBYrMSS1Ujh5s2rBPEhgqKes104RSiXb7UnP-dMT2UzC3OKGUPF2aSDE9Lw-THKr_Wa3O2uPJDxHv0EZGoor3d7HiGK5ns-Zoxgo57IOuvgXvHXAY8LXOAytgBNEKlh3HZEjrNG9sS9of5y0enTO_0Lx2RTQAhrFvK9aekigx4C4lFhTUFHJSOINMucV6NQoE595kZ5cTpWKf343KmyKLsfZEjAtiV4wgarvoNWfoSYR8dqOrvqeq-NrPbHMMCqFHUfoXGBt9ue7z97NlViTH1coSmbuhOXQ1p7mjRyrlEbjb9pG6d88CHs4Al0sVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به اظهارات وزیر خزانه‌داری آمریکا، با انتشار یک میم اقتصادی: آماده‌ای تا روح تو را تسخیر کند؟
🔹
در تصویر دیوید زرووس، مشاور ویژه جدید بسنت و حامی کاهش نرخ بهره، دیده می‌شود؛ همان کسی که گفته بود تا فدرال‌رزرو نرخ بهره را پایین نیاورد، موهایش را کوتاه نمی‌کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696210" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف مسابقات فوتبال در آرژانتین در دقیقه ۱٠ به احترام مسی  سایت «ESPN»:
🔹
با تصمیم فدراسیون فوتبال این کشور، قرار است تمام بازی‌های فوتبال در این کشور در هفته پیش روی لیگ‌های مختلف مردان و بانوان در دقیقه ۱۰ متوقف شده و به پاس قدردانی از دوران حرفه‌ای مسی…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696209" target="_blank">📅 22:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ اعتراضات در فرانسه را به اسلام نسبت داد  ترامپ در تروث‌سوشال:
🔹
مهاجرت انبوه و از کنترل خارج. این موضوع درباره مدارس نیست، این درباره اسلام است که می‌خواهد کشوری را که زمانی بزرگ بود تصاحب کند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696208" target="_blank">📅 22:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6g3wWPVG_MJIGmLYxkB6-pU_ABBpm56hHGz0kxgIN3_jKoqoq4qLtP5TW4ZeRWnmmNUhjhqVXlugdQ313FAwABAwh4RYFudo6jIzuQ6nzXjHjRcbL-K4pmg6lg4sq5XvCXgKBvxt7Z3dZLVHxf_E1K-SxEPbyquYnh_GNPBfEWtqAjxQ-_mKhjRRQVACBjHjCEj7NyAPulrFUneM1PG-OsL5EONY5AXPRASN0vO_ss94AmNvFfoABnMK9RRBM3RB6sJZ31um2-V9Qe3REvbkIkhFv0hrzFZzEoevrU1jllxPinsr3xKNCaV8HLHrpqho03XlHcCXWz3CNhOmtZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت دلار فردا افزایشی است یا کاهشی؟
🔹
دلار، طلا، بورس، مسکن و اقتصاد هر روز با یک خبر تکان می‌خورند؛ مهم این است که بفهمی کدام خبر واقعاً مهم است و بعد از آن چه اتفاقی ممکن است برای بازار بیافتد.
🔹
این کانال رو به تیم مدیریت می‌کنه که از اتفاقات بازار زودتر خبر داره و همه چیز میگه
👇
👇
@EconWar
@EconWar
@EconWar</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/696207" target="_blank">📅 21:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
علیرضا مطلبی: سلیقه گرون داشته باشید سلیقه گرون باعث میشه پول بیشتری در بیارید/کسی که سلیقه گرون داره در خودش یه چیزی میبینه که دنبال بهترین میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696206" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
رئیس اطلاعات نظامی اسرائیل: از ۶۰۰۰ نفوذگر که در ۷ اکتبر از غزه به مرز نفوذ کردند، ارتش دفاعی اسرائیل ۴۰۰۰ نفر را از بین برده است؛ ۲۰۰۰ نفر باقی مانده‌اند و ما به تک‌تک آن‌ها خواهیم رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696205" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی یک بحث ساده به خونریزی ختم می‌شود!
🔹
هر روز توی شهر شاهد نزاع و درگیری خیابونی هستیم و شاید اگه برای یک لحظه خشم‌مون رو کنترل کنیم، این درگیری‌ها پیش نیاد.
🔹
امروز بین شما مردم اومدیم تا ببینیم چرا انقدر درگیری خیابانی رقم می‌خوره؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/696204" target="_blank">📅 21:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سپاه در سومین سالگرد عملیات طوفان الاقصی: هرگونه خطای محاسباتی و تجاوز مجدد علیه ایران پاسخی دردناک خواهد داشت، این عملیات هیمنه ارتش تروریستی اسرائیل را فرو ریخت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/696203" target="_blank">📅 21:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3K2yCv15JvgbAPC3jm25IUttDU4POIeBLhzACnqAjAcklLNmlevyTCb99PfrUyMnjKhVG2B5qUZcfSY_Lk2ps2YhxlBg9kYV4sH0QXEk0rpDuGPKx2pBDW7nyhpvxW4osl20eQx_QVPe7gJf-BRhHC-PjU3bvQWbH7jUPbMjmNKZRvzyp2Bg2aRTtLMpsdNq4O0CzUq6ewFHcFgB-FZXk10idavTdol5RE6-d0byYwqNQPMi7btbjlqRzbOTLCUOnN4mVhlToJnAR3RKJbFoU51brGdvm_BcT5v6J-X3ohyn3GWUadMSQT6aqoi_X0Xkiynw3TZhIMOzP3aui_Beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور اتوی بخار رو تمیز کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/696202" target="_blank">📅 21:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU45Pn7646AXqjIvgcnAtatBxPGwpMiFxtmBSsMEIH1v4J9onEAVueXoUTjL5yXbI2PwpJbXfSHzigg-fSyIUmHkLkct8_nQBAK1FXHeePyzXJ0N7q4pbAZKp_vlHAWQ8DKfa-OLAwZMuYk4a2Hfg7YRTMRkMIeHR_EHKG19cTz543o5MYUjmNqNxdxHqG9W39wzTYkgtcyFuZGJaqdfH4RNp8BR5lhCACQC-tkg7P2XNJ27Vl5jAgKjdUx1qkpHqnbIGcvB27jjuXUIIdAtAEspJGI70ptvAlrFKQkaa0eAmhWm4pP9Ct-YXn__xoVKKWUn5tqtKC7VqZIqUgjkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه نخبگان همراه اول میزبان ستاره‌های علم و ورزش
🔹
همراه اول در قالب برنامه‌های باشگاه نخبگان از جمعی از افتخارآفرینان علمی و ورزشی کشور تقدیر می‌کند.
🔹
اعضای تیم ملی المپیاد نجوم و اخترفیزیک ایران با ۵ مدال طلا و سومین قهرمانی پیاپی جهان، ۳۰ نفر از رتبه‌های برتر و تک‌رقمی کنکور سراسری و مدال‌آوران ایران در بازی‌های آسیایی آیچی–ناگویا ۲۰۲۶ مشمول این طرح هستند.
🔹
هر یک از این نخبگان یک سیم‌کارت دائمی ۰۹۱۲ ، مودم پرسرعت 5G و یک سال اینترنت رایگان دریافت می‌کنند.
🔹
باشگاه نخبگان همراه اول با هدف حمایت از سرمایه‌های انسانی و همراهی با مسیر رشد و موفقیت استعدادهای برتر کشور فعالیت می‌کند.
http://mci.ir/-NYKQCE
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/696201" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadeaf1478.mp4?token=FXxtHc8KKYc9VOxtmEaUJ2BcKKkUDd42X0x_oq44FOk8o9SFgspjJc3jfZTLr_aja96A4Gzhs62wKGaiPDwAjcYQ8_r0K5A6ShVeM9rp0VZ8F2vP0A2gGSAuIOEsyFfcANDL88YjHeiV07caOx3HF2mFIIYkHmJp5WJJrt2UI3DNIgkiSlliZl89_NO0yWdG36tbfdwvGTaLYNk5wmjyUG22JnDwJiQjlynnOGA6C56a8xfg_-H2ngYrD6Tz4g2LPdfawnUNZXKhnj6FHPHpcTud-AviQrMDNWISUG5Ty60G1K984ax4Z9BYphAhdpOz3bAMxDGVFZPDmudzLWeQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadeaf1478.mp4?token=FXxtHc8KKYc9VOxtmEaUJ2BcKKkUDd42X0x_oq44FOk8o9SFgspjJc3jfZTLr_aja96A4Gzhs62wKGaiPDwAjcYQ8_r0K5A6ShVeM9rp0VZ8F2vP0A2gGSAuIOEsyFfcANDL88YjHeiV07caOx3HF2mFIIYkHmJp5WJJrt2UI3DNIgkiSlliZl89_NO0yWdG36tbfdwvGTaLYNk5wmjyUG22JnDwJiQjlynnOGA6C56a8xfg_-H2ngYrD6Tz4g2LPdfawnUNZXKhnj6FHPHpcTud-AviQrMDNWISUG5Ty60G1K984ax4Z9BYphAhdpOz3bAMxDGVFZPDmudzLWeQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین زنجیره انسانی «جان‌فدای ایران» در مشهد شکل گرفت/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/696200" target="_blank">📅 21:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
عمان: یک کشتی در مسندم هدف حمله قرار گرفت/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/696199" target="_blank">📅 21:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696198">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3420338f76.mp4?token=Mv1foUbVoJEoaHba6p1jN8fMtzax82QNv1NIoHHmkwTd-JH7mew07nKfSaL0zCvcuXfLjtsZ1IOxe2q0QgApyUOs6bnUC2PPN8c6TgoAcWhHXOTXcsegVscSPj1btRcjIkR5QfWkEFw_SoDSRkMb7B1c312FLSntTbENkiFfj2dI8Sk2oWgsQrQUk9Ztg1GeuLuxCptHlMI8K9KSewsBgOEFnhdwU4-vsYOn-IWJakJFkqSTHSJDqbELxafMj3ehbYHNwHz5ZNUvcf7ajcVJVgDFZhUq2thZM7d_-tptJ4xhzd5JXzIzjFb_g8LlXHVUGBgAD1VU22EaDuN3RooU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3420338f76.mp4?token=Mv1foUbVoJEoaHba6p1jN8fMtzax82QNv1NIoHHmkwTd-JH7mew07nKfSaL0zCvcuXfLjtsZ1IOxe2q0QgApyUOs6bnUC2PPN8c6TgoAcWhHXOTXcsegVscSPj1btRcjIkR5QfWkEFw_SoDSRkMb7B1c312FLSntTbENkiFfj2dI8Sk2oWgsQrQUk9Ztg1GeuLuxCptHlMI8K9KSewsBgOEFnhdwU4-vsYOn-IWJakJFkqSTHSJDqbELxafMj3ehbYHNwHz5ZNUvcf7ajcVJVgDFZhUq2thZM7d_-tptJ4xhzd5JXzIzjFb_g8LlXHVUGBgAD1VU22EaDuN3RooU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا نباید ناخن‌ها را جوید؟
🦠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/696198" target="_blank">📅 21:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696197">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofw03zqV4yLbNfxi5MIp9rpEZNYazYKRQw_Xe1SftCjBFiAXSwE6N1qdge9Y2luytyaRUrqJX56DL_Sp5FMFRjwgpQKFYkLrfgGJ9hJTEOHGeKy4ehb0X1wN0_HXb9Flq0IveS1Tcq3HYdZtjcywarRFtbbQ293LcRGTe_2jH-emMHxA4e6sje0BzIIkDaWHtv6GJ02O51XdW2b1Jy42T4VmxsrI0tnkatiEJabW20eN1XxLHKJnlJp8NkxtaYUJG9hbhJ_WJwcHGfw8loxd8VKWRJm4BmauMvX6ZLXqZoTpvq2UZft_nwyliDPlQ9aheKkSAvTo-rkfw_8OG_l1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رایتل به فروش گذاشته شد
🔹
شرکت سرمایه‌گذاری تأمین اجتماعی با انتشار فراخوان مزایده، از واگذاری ۱۰۰ درصد سهام رایتل خبر داد. قیمت پایه ۱۳۰ هزار میلیارد تومان اعلام شده است./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/696197" target="_blank">📅 21:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696196">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY88vXPIlBYef_FM1Mn-vNqd1axRP-mXULcLPWcBzOnP9_4Ey-hTPZ5AWGFmYi_CeF2bHus_KfqzXHE9w7-DxB8M4RYUWgiZECel33nAycsGZZYmb9zEl61pnW_CfKH6RuF5r9WhaeymlgOoVmp1iRZxOfJyyAfNcdbG8gKQIPvamZY6PgZJRNMhv6U6eqIYhjuLSj9D-CCA1BRZ8wITBBkz9CMupz5ku2ZZBZJNwLmdfvHVUAJ7NUJlyZSpLUx3S97S5os8MSfNVYPcz_y9f1FKTmI2Ec5CWWKythgNZ8fQSMwpgnl5EevRXVa6FY4voXRKfU4zmSymYE0H__mrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شریفی‌الحسینی: تعرفه‌های قدیمی، توسعه شبکه را محدود می‌کنند
🔹
سید محمدعلی شریفی‌الحسینی، رئیس کمیسیون اینترنت نصر کشور، معتقد است ادامه وضعیت فعلی تعرفه‌ها، فاصله میان هزینه‌های شبکه و درآمد اپراتورها را بیشتر کرده و سرمایه‌گذاری در زیرساخت‌های ارتباطی را تحت فشار قرار داده است.
🔹
توسعه 5G، فیبر نوری، دیتاسنترها و شبکه‌های انتقال به سرمایه‌گذاری مداوم نیاز دارد و هزینه این بخش‌ها هم با تورم و نرخ ارز بالا می‌رود. در چنین شرایطی، ثابت ماندن تعرفه‌ها می‌تواند به فرسایش تدریجی شبکه و عقب‌ماندن از فناوری‌های روز منجر شود.
🔹
بحث فقط افزایش قیمت اینترنت نیست. مسئله، ایجاد یک مدل تعرفه‌ای شفاف و قابل پیش‌بینی است که هم قدرت خرید کاربران را در نظر بگیرد و هم امکان ادامه سرمایه‌گذاری اپراتورها را فراهم کند./ عصرایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/696196" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696195">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4857b6b6d1.mp4?token=b_7ShUeeTo3wslVNnR_JvRfS8V103IazayHXt0GZ0IC9fjWKF0NIi9v8t5L1N_ZL86Ihb4k9UAy_LVIJoR4cd-jWxiUNvAz93JeEdq3bch8jDeqoHlPhh0hVoH0JRvyO7CBa43sZCFbJUl7lSr83clIh03TPSMYtm4I9BtcGD6q6A1Qur8HY6BSJOWD6qT6vu5gMYngnp6jnDuzI0azqTH2mSGAb4YxdU_1Uo5PzQuAsiL83Pn0Dz3itguVi14jCGWHvFKKNI4YNFzzi_0YXTTo6Lhugwjn4BZZx_TLllDw0siOYmu6NLGBbCKQZ9NG4FNJs3dRzpUEXNUbTr-G6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4857b6b6d1.mp4?token=b_7ShUeeTo3wslVNnR_JvRfS8V103IazayHXt0GZ0IC9fjWKF0NIi9v8t5L1N_ZL86Ihb4k9UAy_LVIJoR4cd-jWxiUNvAz93JeEdq3bch8jDeqoHlPhh0hVoH0JRvyO7CBa43sZCFbJUl7lSr83clIh03TPSMYtm4I9BtcGD6q6A1Qur8HY6BSJOWD6qT6vu5gMYngnp6jnDuzI0azqTH2mSGAb4YxdU_1Uo5PzQuAsiL83Pn0Dz3itguVi14jCGWHvFKKNI4YNFzzi_0YXTTo6Lhugwjn4BZZx_TLllDw0siOYmu6NLGBbCKQZ9NG4FNJs3dRzpUEXNUbTr-G6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر گوشی‌ات مدل بالا نیست ولی دوست داری عکس‌های باکیفیت بگیری، این ویدئو رو تماشا کن #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/696195" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراق از ممنوعیت استفاده از اپلیکیشن مسیریابی ویز Waze از ابتدای سال ۲۰۲۷ خبر داد
🔹
بغداد دلیل آن را ارتباط این اپلیکیشن با رژیم صهیونیستی عنوان کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/696194" target="_blank">📅 21:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6c09a17c.mp4?token=Wwldph0sCV9yYrjo7LiqtcLPHSvPl0qE-HmBelrukpRPxbSttaLEWRjYNJhyMC_2miZ-pnrBrR2vZd_sS07lJVlLoPTNnrcud5apgjvzufPh1r0rQPYldwPeEX3DjVqgOgDthZAcOzw4OvqPXa5PBONseuCtpefXPvkUu8aRNGqWPXSmSNXprRkfJ-1yOownQ0pP8LWKOa8JMNgHS94vGH9LcdoW2LwlBw6nMuaCn7tsGHtO2l4CwQ-q5HcN6bwGzhjQohplYnMfjRpdmOegKaRxOnwRdhL8mMBM5i-oORScJYwOgpkpsbuJpgQ8tbrpZnUdQAtKYJjomzxQ3NYD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6c09a17c.mp4?token=Wwldph0sCV9yYrjo7LiqtcLPHSvPl0qE-HmBelrukpRPxbSttaLEWRjYNJhyMC_2miZ-pnrBrR2vZd_sS07lJVlLoPTNnrcud5apgjvzufPh1r0rQPYldwPeEX3DjVqgOgDthZAcOzw4OvqPXa5PBONseuCtpefXPvkUu8aRNGqWPXSmSNXprRkfJ-1yOownQ0pP8LWKOa8JMNgHS94vGH9LcdoW2LwlBw6nMuaCn7tsGHtO2l4CwQ-q5HcN6bwGzhjQohplYnMfjRpdmOegKaRxOnwRdhL8mMBM5i-oORScJYwOgpkpsbuJpgQ8tbrpZnUdQAtKYJjomzxQ3NYD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب بازیکن سابق استقلال علیه برانکو: دعوت به تیم‌ملی در زمان برانکو پولی بود!
سعید بیگی، بازیکن سابق استقلال در تلویزیون مدار:
🔹
در دوران هدایت برانکو ایوانکوویچ به تیم ملی دعوت شدم اما برای حضور در تیم از من ۵ میلیون تومان خواسته شد که آن را پرداخت نکردم، بازیکن دیگری آن پول را پرداخت کرد و راهی تیم ملی شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/696193" target="_blank">📅 20:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم از سمت دریا به گوش رسید؛ اصابتی در سطح جزیره گزارش نشده است
🔹
منابع محلی تاکنون جزئیاتی به رسانه‌ها اعلام نکرده‌اند./ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/696192" target="_blank">📅 20:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a00d2411.mp4?token=W892aZwvsVutZTptRXfCoHkgU78LrpX4zQMZVbUns-7EaBryIEOR8Zvq-wgktXJ6fDQ4IeHZmyw0bOI--nTsJ-CVFeEylwflTPVZvkBUu8CIyxSx9fCy3tmE2CV48bbl92HQxsrMAo06oHixVYQlFvqmBxrTflYDcHoQ1V8PdrSW0NIDt_13KBlEgQNPsCJYyxeywh-uV4N5ZCc3xqaelcbqJW-zvZ_4vBlJxaRgY9iUQLvGDOhERQf8HzhFKY6Fg93y26t-n_IG8OfMpvQce1v-x5oBugFgLXRpV_2NSLBWosiJ23DaDQSuO8k_KbgnIYeyjHXZL1J3FkLCqNP39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a00d2411.mp4?token=W892aZwvsVutZTptRXfCoHkgU78LrpX4zQMZVbUns-7EaBryIEOR8Zvq-wgktXJ6fDQ4IeHZmyw0bOI--nTsJ-CVFeEylwflTPVZvkBUu8CIyxSx9fCy3tmE2CV48bbl92HQxsrMAo06oHixVYQlFvqmBxrTflYDcHoQ1V8PdrSW0NIDt_13KBlEgQNPsCJYyxeywh-uV4N5ZCc3xqaelcbqJW-zvZ_4vBlJxaRgY9iUQLvGDOhERQf8HzhFKY6Fg93y26t-n_IG8OfMpvQce1v-x5oBugFgLXRpV_2NSLBWosiJ23DaDQSuO8k_KbgnIYeyjHXZL1J3FkLCqNP39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با سه قلم مواد ساده، عفونت گلو و سرماخوردگی را بطور کامل درمان کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/696191" target="_blank">📅 20:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5OwKFimjrRQ2EY6erSB_S45LbpHx7tjMMh-3pgy0NqfnuXeY_OeGqRLNlSBTgJLFFNr4Kk4h9W6rGeo3P_mnVxFkUctLlkEJc9xNw60NpnB3EN7VmdJhq9UdmCACt7UwRCJAQJqnPm4mBqCUlI6BMz4uiGva1wlZpuEFzUpPq-FCQ9VxvTaS8QxFPu_MBS2TXuN7CY17Ph-ZuWlCtJFssx41tjC64SZCwB9v5Wo9os69lY9LYb4ujxUOyRrtS2933q9t42uXpf5GK3OnzKIQLNZPN8qQBGcg2_MZiHEK5YYrHJamJEyaKVQZeyJS56hgJG8cnkeK-pw9z3XKapKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/696190" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
محکوم به مقاومت هستیم/ هدف نهایی دشمن تجزیه ایران است
عباس گودرزی، سخنگوی هیئت رییسه مجلس:
🔹
جمهوری اسلامی آمادگی برای مواجهه با هر وضعیتی را دارد که در هر سطحی تهدید شویم، در همان سطح پاسخ کوبنده، ویرانگر و فراگیر به دشمن بدهد.
🔹
امروز مقاومت برای ما انتخاب نیست بلکه ضرورتی استراتژیک و راهبردی است؛ محکوم به مقاومت هستیم و دشمن به دنبال تجزیه ایران است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/696188" target="_blank">📅 20:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f31cb5.mp4?token=d0Cg3zsXXeeYHRf8FG00iMNCpQEhNtd5-DZykEp5vkk1mXvxvQCAJPHPX6_dHDVYmdKXnCIr6etHtP681Zkye5fue3MEPEO40XE7hFSemNSJmERs9IALGUJOqkKsY7d0esbLxjDLdlE3fIkC9fddWTAisKExNdRZ0l7rYQyd-ZGkNnZNhCoCWFQPfpFi3U589W0pReYgTLuUCDv78WmCNUIHW4vQkB3-to1adMf9xgYQroh-AhgidwIEWZi1NT390cTIvftNHkPKK1-CyyeuNxf_hT6g7qHUF9Nzg5PScbFA2xeoN_7k1kamjJ1Mv2Leuf65z_9INmlwTtfbDc4fXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f31cb5.mp4?token=d0Cg3zsXXeeYHRf8FG00iMNCpQEhNtd5-DZykEp5vkk1mXvxvQCAJPHPX6_dHDVYmdKXnCIr6etHtP681Zkye5fue3MEPEO40XE7hFSemNSJmERs9IALGUJOqkKsY7d0esbLxjDLdlE3fIkC9fddWTAisKExNdRZ0l7rYQyd-ZGkNnZNhCoCWFQPfpFi3U589W0pReYgTLuUCDv78WmCNUIHW4vQkB3-to1adMf9xgYQroh-AhgidwIEWZi1NT390cTIvftNHkPKK1-CyyeuNxf_hT6g7qHUF9Nzg5PScbFA2xeoN_7k1kamjJ1Mv2Leuf65z_9INmlwTtfbDc4fXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز هنگام خواب استراحت نمی‌کند؛ بلکه به پاکسازی و تقویت تمرکز و حافظه می‌پردازد/ کم‌خوابی می‌تواند تمرکز، حافظه و اشتها را تحت تأثیر قرار دهد
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/696187" target="_blank">📅 20:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=CNrTl3eUMZ6tR0_29LX4oj4JZ6kKYZmal6yKBCxRYgPOQLaQxzsfhWTVmpjtAr0iEtW7auBiEYmH_C_SF_sqr09wp8ZyXRkD7NwonolWNXh16FGYv8fU9fzugAHij_IlrlG3P49s9l6gNySg8gpNyCF4O7T6mqh_NuHBoSbnUqZSJC1YbEN-68gxHP195vJLEiShy5xRx5tOQkJlxRDnyeM1v3-VEDs-9vW2h7jmprgGChylp_C5cW9hl66f0sFu4hsQUTM9v4y2zdrtdJPSJQADq7mzjjeR24i7YJydm8IWDFQhuYIppdpee2TkTXjVE4AlukkH5LOcVAZxigFSsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=CNrTl3eUMZ6tR0_29LX4oj4JZ6kKYZmal6yKBCxRYgPOQLaQxzsfhWTVmpjtAr0iEtW7auBiEYmH_C_SF_sqr09wp8ZyXRkD7NwonolWNXh16FGYv8fU9fzugAHij_IlrlG3P49s9l6gNySg8gpNyCF4O7T6mqh_NuHBoSbnUqZSJC1YbEN-68gxHP195vJLEiShy5xRx5tOQkJlxRDnyeM1v3-VEDs-9vW2h7jmprgGChylp_C5cW9hl66f0sFu4hsQUTM9v4y2zdrtdJPSJQADq7mzjjeR24i7YJydm8IWDFQhuYIppdpee2TkTXjVE4AlukkH5LOcVAZxigFSsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی وایرال شده از تلاش عجیب یک جوان برای پرش از پنجره یک خودرو به خودروی دیگر در تهران؛ حرکتی به سبک فیلم سریع و خشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/696186" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
از ابتدای آبان ماه قطعی گاز در صنایع را خواهیم‌داشت
احسان قاضی‌زاده هاشمی، عضو کمیسیون صنایع مجلس:
🔹
برق صنعت که قرار بود از نیمه شهریور ماه قطع نشود، متاسفانه ادامه یافت و کمتر شد و قطعی گاز در صنایع را از ابتدای آبان ماه خواهیم‌داشت.
🔹
صنعت ما بر سر دوراهی قرار دارد؛ یا باید خود را تعطیل کند یا با شرایط گران‌سازی چاره‌ای جز افزایش قیمت‌ها نخواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/696185" target="_blank">📅 20:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a7b92fa8.mp4?token=UkVk5mDcfKDJL-TkkSF8PgzTCqz8Hafk4A9JKQuu7aGsV1HRW8XRlcKiqL_fJD1XtEfWoEkpjqW07mPkuIksOuJY1AKomZGh_MeOjGleZHeq4b_njCnHsIVp1Ap_J0AqPvAaGbK68d3rTq3hhBN91qwF-2SKz5Gr4yq0eyYoXU284ywtQatwT6m34iUfb5KRu6NsIMBrCZwSt-6IT9Lfv2JXLqhehllYvLu8LvErJ-rJE3yi4snooja87EV4fxWMkNBfBBFSX2khPbBqqVaDuF8UvVr-ompZwU76kyKD_GMcZ10Iju4h_Tx6TrqU6g7SfIPb4A9J_47svEqTpXCRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a7b92fa8.mp4?token=UkVk5mDcfKDJL-TkkSF8PgzTCqz8Hafk4A9JKQuu7aGsV1HRW8XRlcKiqL_fJD1XtEfWoEkpjqW07mPkuIksOuJY1AKomZGh_MeOjGleZHeq4b_njCnHsIVp1Ap_J0AqPvAaGbK68d3rTq3hhBN91qwF-2SKz5Gr4yq0eyYoXU284ywtQatwT6m34iUfb5KRu6NsIMBrCZwSt-6IT9Lfv2JXLqhehllYvLu8LvErJ-rJE3yi4snooja87EV4fxWMkNBfBBFSX2khPbBqqVaDuF8UvVr-ompZwU76kyKD_GMcZ10Iju4h_Tx6TrqU6g7SfIPb4A9J_47svEqTpXCRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
​
مقایسه BBC فارسی با BBC سایر کشورها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/696184" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f3d37bff.mp4?token=EPaA7D9sDBKzTQ79Jc6Q-b7Bsgcn-x3UNFOhpFzewF83gq0_BdthfVI8XAm1gJG0njCVbSwcrPORm7VqVaLejdqFZ7_v4Nw2Xl6VuFB6EV7AyowemI87zhEDNgz3KvSD9LJ2zO2p-KLjDrDBkjoR5edt_N-LCw6_ZUntH9Gn-aZa3SAD-4y1n_TqDE1KkXOyE0t-Ox6CRhfYRXwDU_DLTK-ZheBZKPVqwNu1YNqh0QfyIybG0w6f10M9lAdU8RPOyHqx87p_-1uY-Upo9CPuIuZ4-ZgabLkjEQjGVbx_QQBoyrjGjunfwLa8mMeSKirnASoCMlsycpCWlt9j9D2PYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f3d37bff.mp4?token=EPaA7D9sDBKzTQ79Jc6Q-b7Bsgcn-x3UNFOhpFzewF83gq0_BdthfVI8XAm1gJG0njCVbSwcrPORm7VqVaLejdqFZ7_v4Nw2Xl6VuFB6EV7AyowemI87zhEDNgz3KvSD9LJ2zO2p-KLjDrDBkjoR5edt_N-LCw6_ZUntH9Gn-aZa3SAD-4y1n_TqDE1KkXOyE0t-Ox6CRhfYRXwDU_DLTK-ZheBZKPVqwNu1YNqh0QfyIybG0w6f10M9lAdU8RPOyHqx87p_-1uY-Upo9CPuIuZ4-ZgabLkjEQjGVbx_QQBoyrjGjunfwLa8mMeSKirnASoCMlsycpCWlt9j9D2PYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین درخت ایران با دو قلب/ درخت لور یا انجیر معابد
🫀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/696183" target="_blank">📅 19:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
بهزادیان: اگر ناوگان MD لغو شود، تعداد پروازها و بلیت‌ها کاهش و قیمت‌ها به‌شدت افزایش پیدا می‌کند!
سیروس بهزادیان، رئیس کمیته فنی انجمن شرکت‌های هواپیمایی در
#گفتگو
با خبرفوری:
🔹
حدود ۳۰ فروند MD عملیاتی داریم که معمولاً روزانه ۶ تا ۸ پرواز انجام می‌دهند و در دو سال اخیر حدود ۱۲۰ هزار پرواز با این هواپیماها داشته‌ایم.
🔹
حدود ۴۵ تا ۵۰ درصد پروازهای ایران را MDها انجام می‌دهند و این هواپیماها قابلیت پرواز بالایی دارند و در چند سال گذشته هیچ‌گونه سانحه‌ای نداشته‌اند.
🔹
ما درخواست کرده‌ایم تا ۲۸ دسامبر ۲۰۲۷ فرصت داشته باشیم تا مشکل تیغه‌های موتور را برطرف کنیم و همه شرکت‌های دارنده MD نیز برای رفع این مشکل تعهد داده‌اند.
🔹
اگر این ناوگان لغو شود، تعداد پروازها کاهش، بلیت‌ها کمیاب و قیمت‌ها به‌شدت افزایش پیدا می‌کند.
🔹
با عدم پرواز هواپیماهای MD، حدود ۲۰ تا ۲۵ هزار نفر از متخصصان این حوزه نیز در معرض تعدیل قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/696182" target="_blank">📅 19:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff3c118eb.mp4?token=H70yglhJMxQXPLP6aZ7I9-rlm3nV1RpuZXOPLVenlPglwbMxHAl3psMEJMBHYaExmUMMYRUfR_lRuOk6Z23ZKDvNajHPCHsNVqRik9mly3HWbgAnDQsE-pOSRwm-mui5Zi1jpRAuBkHilZIIr1OmokT5xm0Cz9Lvf0Zhd5yMe2mRy4Rkz_dclWkvEbVf_emyE4v-Ek8qfHZJy-OoxHGGX-nGvcE3JwORdc7gYXfAxe4efreXkFFaMVyxd-viYD-y_KDNQXtJBl1biGB8XMcNilef0fCoD-vVYxmEdP_KNJOSaUk18jwXiQc_MFEHY0XZMmd8T0Tc7mFbPHEQMTM1YKYlj-q-q5iUKzBOf1MOzIkE8bImQkqG1tXLwdLdDl0xt8y8UF1tSGvW4KBCssdhlv8OdLamtsaYi3ZGbEDTgur8l_GeDcoAQVDt4Ij5sDAYcz5B9G3t3jHPe8LuDpWJJQCZHw5QBkADpYiriaD9PabkUbmjuYoSaEFJ67aQdoO08NiUGInw0FQvKLqOrmxfkQ1fr83ZYAZk_u0-NrxmADcVn8UCrpGNMbO10yMQwizPMjlNYGe5K7h8FN_Oa92iuzXcv3tI9H22qwmkXWC3vEyE9zj2UrDDLxDycdM1aesF-as9ez7jWSUPiG3gOeYkRqN3aYCKncszxHjABkxJNgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff3c118eb.mp4?token=H70yglhJMxQXPLP6aZ7I9-rlm3nV1RpuZXOPLVenlPglwbMxHAl3psMEJMBHYaExmUMMYRUfR_lRuOk6Z23ZKDvNajHPCHsNVqRik9mly3HWbgAnDQsE-pOSRwm-mui5Zi1jpRAuBkHilZIIr1OmokT5xm0Cz9Lvf0Zhd5yMe2mRy4Rkz_dclWkvEbVf_emyE4v-Ek8qfHZJy-OoxHGGX-nGvcE3JwORdc7gYXfAxe4efreXkFFaMVyxd-viYD-y_KDNQXtJBl1biGB8XMcNilef0fCoD-vVYxmEdP_KNJOSaUk18jwXiQc_MFEHY0XZMmd8T0Tc7mFbPHEQMTM1YKYlj-q-q5iUKzBOf1MOzIkE8bImQkqG1tXLwdLdDl0xt8y8UF1tSGvW4KBCssdhlv8OdLamtsaYi3ZGbEDTgur8l_GeDcoAQVDt4Ij5sDAYcz5B9G3t3jHPe8LuDpWJJQCZHw5QBkADpYiriaD9PabkUbmjuYoSaEFJ67aQdoO08NiUGInw0FQvKLqOrmxfkQ1fr83ZYAZk_u0-NrxmADcVn8UCrpGNMbO10yMQwizPMjlNYGe5K7h8FN_Oa92iuzXcv3tI9H22qwmkXWC3vEyE9zj2UrDDLxDycdM1aesF-as9ez7jWSUPiG3gOeYkRqN3aYCKncszxHjABkxJNgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آبگرفتگی شدید معابر شاهین‌دژ
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/696181" target="_blank">📅 19:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پوتین و پزشکیان روز جمعه با یکدیگر دیدار می‌کنند
/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/696180" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884904d006.mp4?token=ood7i1tmXtvpbHXqMJtigj_JYiXKoIvVQ3aROq9wQR53CMHSCg79EiN5EiHmnESR-uc_bRpuzjKOXnrktf5I7N6xHO40RKmCQAyVhExLadqdlGAmwF-zCVEwf8yWMgOed5kJT4zrzTLvsn6azZe-UAZQjagx22qIn6jYLWJYgrnuauCddRGZuF6aZJALGBenPThTXYSmSTJEG_FbUp2sx1_udCrGHSCLp3f4Zl9bE_FxeugOzsgf55akd4Aa_ShyUw_S4GFMpdbe5QWFvWElI21MpRr5ve-FkbWGN3BhEx-QL_IQkB740coE4I7Ex3NKhsnR4UobA9yaIuo3gCKq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884904d006.mp4?token=ood7i1tmXtvpbHXqMJtigj_JYiXKoIvVQ3aROq9wQR53CMHSCg79EiN5EiHmnESR-uc_bRpuzjKOXnrktf5I7N6xHO40RKmCQAyVhExLadqdlGAmwF-zCVEwf8yWMgOed5kJT4zrzTLvsn6azZe-UAZQjagx22qIn6jYLWJYgrnuauCddRGZuF6aZJALGBenPThTXYSmSTJEG_FbUp2sx1_udCrGHSCLp3f4Zl9bE_FxeugOzsgf55akd4Aa_ShyUw_S4GFMpdbe5QWFvWElI21MpRr5ve-FkbWGN3BhEx-QL_IQkB740coE4I7Ex3NKhsnR4UobA9yaIuo3gCKq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار؛ روش جدید کلاهبرداری با اسم پستچی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/696179" target="_blank">📅 19:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696176">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله لبنان: آزادی جنوب لبنان را با چشمان خود خواهیم‌دید و اسرائیل هرگز نمی‌تواند حتی برای مدتی کوتاه در جنوب باقی‌بماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/696176" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696175">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEhgJBnRwpG1bgx476NdpEtVT619RsDtGKPs_MZ3t1w09QstG8V4uwvSv9u3Mce5bsF4qCptMa_ONmuiU4-uzTRXXRqNXYBrP6G3-e2TtbtxSWYPbP0lePA5aH7hJvhy7ZvS5pE_K5Ku2uSqkMYcLISo2lGgZQBcmjI_1cvNeLSxLKTJvXNPu5MblDvxnQBAN9Xs-FSiVDLKlkaMt1tDqXK5VJ_Ph3EMj1wfvACuI2FjcBX_XtGV_TKrAJZgV70FVfWalMRV13dUnd8Iep2j72MYDlCzCKhJ-OmuideY8OIRyBHI1RZe2wN1JmwmrM8hgm9BZ3K2an2UpS0Fci6dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان جهانی بهداشت: نشانه‌ای از طاعون در روسیه مشاهده نشده است و خطر شیوع برای عموم پایین است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/696175" target="_blank">📅 19:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696174">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آخرین وضعیت اعتراضات دانش‌آموزی در فرانسه
🔹
اعتراضات دانش‌آموزی فرانسه وارد نهمین روز شد؛ تاکنون ۶۰۵۹ نفر بازداشت و ۱۰۱۵ نفر زخمی شده‌اند. یک نوجوان ۱۵ ساله نیز بر اثر انفجار نارنجک پلیس دستش را از مچ از دست داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/696174" target="_blank">📅 19:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d7e3c4ebb.mp4?token=iLSH3zB6GUBJRRSKGp_ZUlyx-9CchDSasKf9uwVOm_Xt_YtcdTO8CYpVo11RtWVZVzC1VdV473Qdxh8UvRWJlPK1Lo4NuJqi1f1vyO8qzzR9O6G7AjPO_l88wvsGf-SalSYHeP6dj4Q8h1JpG7lShTW5_P3740M7mVk78tc2KtrItVOcnmX9XBJu8BbZW5415j4Ed5iEMFQFuF_wB43M71XwAgk32v2K8r6gfbdjzlpT8F1JAQ5n6eFHfAwNEEWV5pDhFkU0kda3NfWZWK654pkly63gkYUHF_y-Xxe0nzlCBO9JHRkiaJ_Yk6jsmxQDWgHnrR5viGSyVQiiptq6Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d7e3c4ebb.mp4?token=iLSH3zB6GUBJRRSKGp_ZUlyx-9CchDSasKf9uwVOm_Xt_YtcdTO8CYpVo11RtWVZVzC1VdV473Qdxh8UvRWJlPK1Lo4NuJqi1f1vyO8qzzR9O6G7AjPO_l88wvsGf-SalSYHeP6dj4Q8h1JpG7lShTW5_P3740M7mVk78tc2KtrItVOcnmX9XBJu8BbZW5415j4Ed5iEMFQFuF_wB43M71XwAgk32v2K8r6gfbdjzlpT8F1JAQ5n6eFHfAwNEEWV5pDhFkU0kda3NfWZWK654pkly63gkYUHF_y-Xxe0nzlCBO9JHRkiaJ_Yk6jsmxQDWgHnrR5viGSyVQiiptq6Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوست دارید عکس‌های بهتری بگیرید؟ ترکیب‌بندی (کامپوزیشن) واقعا این‌قدر ساده و البته بی‌نهایت در خروجی عکس‌تون موثره
📹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/696173" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHtAcdptojnBQZ4nH3EMY0HehiuiQiW9Kqsol3st8jU570ah_wW1Ge9-VXDD3nHYt04b48lmCyrIS5Y_v9yWxSiuhX85xRHzOODoTwVET86P1Mzn1tUbhjzisdwT3H4NknGEw4rrVgAWRU5cqUwYAj2hMeoPdm8X31EeVyCFEVdURz1swkD-5Me7phwtPkaBv8Zk3G5_Xjyi0LtbLsdUAygYuHWir9QKJytHB21mVh4DkEunwD-6nzXwmBuKdwmuZ782MlPV8J7SDaLzS-bArEyij7ExNeOc5__gjLk1H1EbZ7-nTLgK0qTFHwjflDuNmj6gWfXaSW3rG4BkAxw7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
«نگاهی به زندگی در روزگار جنگ»، جشنواره عکس در پاریس
همزمان با
بزرگداشت دویستمین سال اختراع عکاسی در پاریس
، جشنواره عکس
«نگاهی به زندگی در روزگار جنگ»
به همت
مرکز ایران و فرانسه و مؤسسه موج نو
، پاییز ۲۰۲۶ در پاریس برگزار می‌شود.
این جشنواره با نگاهی انسانی، روایت زندگی در شرایط جنگ را از دل
زندگی روزمره، خانواده، روابط انسانی، میراث فرهنگی، شهر، آثار جنگ، همبستگی و امید به آینده
دنبال می‌کند.
📅
مهلت ارسال آثار:
۱۸ مهرماه ۱۴۰۵
🖼
نمایشگاه‌های پاریس:
نوامبر و دسامبر ۲۰۲۶
🏆
نمایش ۵۰ اثر منتخب و اهدای جوایز و لوح تقدیر به سه اثر برتر
🔗
اطلاعات بیشتر و فراخوان کامل:
www.france-iran.org/iranphotos2026</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/696172" target="_blank">📅 18:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a75b37358.mp4?token=uel91dtZi8ppJkbph_87FhwF0K3egiGeuCp_FGExDTtiM6ZJranh9VlzhNQRQdLCtYxB32zoAEx0VS6h4TmxFUqOstEErt5hP1qN2Kh-McwZEs-BxNxkYCftenecJXKriSTYlDbb8TyASblH5lZ3b8MrPBL04Xuyrj9YpK-GRq1RCkC-MlN3DifFSMDHy4SOPNMJz7X4nP2KUJIgmJnf3kurTI0HLN4oe7Pq6kOryvLPDLcFfjuqLdnlRi0l6q1fmaC6hR74mDG7ev_CdvRt2IjR5snb1ax8wymkylWzm6h9H_vzZGTZ1OJ9QMg5rUdcXJAyuy8qEquD0EFQlEoAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a75b37358.mp4?token=uel91dtZi8ppJkbph_87FhwF0K3egiGeuCp_FGExDTtiM6ZJranh9VlzhNQRQdLCtYxB32zoAEx0VS6h4TmxFUqOstEErt5hP1qN2Kh-McwZEs-BxNxkYCftenecJXKriSTYlDbb8TyASblH5lZ3b8MrPBL04Xuyrj9YpK-GRq1RCkC-MlN3DifFSMDHy4SOPNMJz7X4nP2KUJIgmJnf3kurTI0HLN4oe7Pq6kOryvLPDLcFfjuqLdnlRi0l6q1fmaC6hR74mDG7ev_CdvRt2IjR5snb1ax8wymkylWzm6h9H_vzZGTZ1OJ9QMg5rUdcXJAyuy8qEquD0EFQlEoAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارگری در یک کارخانه تولید شیرخشک، پس از درگیری با کارفرما، برای انتقام حدود ۲۰ لیتر اسید را مخفیانه داخل مخزن شیر ریخت؛ اما آزمایشگاه کارخانه در آخرین لحظات این اقدام را شناسایی کرد. این حادثه می‌توانست سلامت صدها نوزاد را به خطر بیندازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/696171" target="_blank">📅 18:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هشدار مهم پیش از خرید ملک؛ سند و مشخصات مالک را حتماً بررسی کنید
🔹
سخنگوی سازمان ثبت اسناد و املاک کشور از خریداران خواست پیش از انجام معامله، سوابق ثبتی ملک و اصالت سند را به‌دقت بررسی کنند.
🔹
از خرید املاک قولنامه‌ای که فاقد سند مالکیت هستند، خودداری کنید.
🔹
مشخصات هویتی فروشنده را با نام مالک درج‌شده در سند تطبیق دهید.
🔹
برای بررسی اصالت سند تک‌برگ، بارکد امنیتی روی سند را با تلفن همراه یا نرم‌افزار بارکدخوان اسکن کنید.
🔹
اگر ملک سند دفترچه‌ای دارد، بهتر است فروشنده پیش از معامله آن را به سند حدنگار یا تک‌برگ تبدیل کند.
🔹
هنگام خرید آپارتمان، شماره و محل پارکینگ و انباری را با نقشه تفکیکی ساختمان تطبیق دهید./ روزنامه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/696170" target="_blank">📅 18:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9506fe34.mp4?token=O24MxGFkjBGGsqrdursNbebeZRrgS35RHOOtx_4nQl14ei6ZrcAEOWxASTI5_hcRwU_xG0G5hQyQYKbtjuDuu4CuUT4gjUOn1qDdb3Az-chYeUlQNWb_ivocr2M_Y03dMfXLAn6pR9DuX644VH-v4qDbSHqYOAcQ_aBkXiz1ZvZc4xann1p24d02PSTJL0ojJNvP8bvoZwz6PIAYG8YKXhQp2mEbFe0D6u_zY9AJLS3NSwCoENnOSMaBAMOiGofCcbcd5NyBfKPm3PGBgDzg3mdACde_5v7zW6tH2M5jhup27MdMVgkiVlLIUj3aCqu7q121lIXAJDZh0vj72JZI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9506fe34.mp4?token=O24MxGFkjBGGsqrdursNbebeZRrgS35RHOOtx_4nQl14ei6ZrcAEOWxASTI5_hcRwU_xG0G5hQyQYKbtjuDuu4CuUT4gjUOn1qDdb3Az-chYeUlQNWb_ivocr2M_Y03dMfXLAn6pR9DuX644VH-v4qDbSHqYOAcQ_aBkXiz1ZvZc4xann1p24d02PSTJL0ojJNvP8bvoZwz6PIAYG8YKXhQp2mEbFe0D6u_zY9AJLS3NSwCoENnOSMaBAMOiGofCcbcd5NyBfKPm3PGBgDzg3mdACde_5v7zW6tH2M5jhup27MdMVgkiVlLIUj3aCqu7q121lIXAJDZh0vj72JZI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون| بارش شدید باران در اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/696169" target="_blank">📅 18:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9148079cca.mp4?token=ZbJvF6R3OgDHIMS1DB1Y0HKI__C8YsU627NcjfdlxrlNzc2d8TEDNhdVkoO90lP_lp1YXoUpO5rMMlEKL8UGGflCCRKbN80gpndHXQoJOgTY1Zp7DVaSmxOStHC41grajIYlX8oWoEboD2J6n9t8LxByX_ZF6GjzBtPK37locXJLBlq6WtoNxQrL1oZJ-ZYqYDCw_Oi9OC_4bJL2fOXIzPh7h7Zbq3OpPjzXQhbyOWKiv8utEoTBATk5U5yQs_NzZDxibbnVbwx27oNckLTQj41_YerNwBhu_jbfK7gL3J591jjCKtaaPaJkqG06w3JkbPiVOdbeKEA7PtVeZxHRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9148079cca.mp4?token=ZbJvF6R3OgDHIMS1DB1Y0HKI__C8YsU627NcjfdlxrlNzc2d8TEDNhdVkoO90lP_lp1YXoUpO5rMMlEKL8UGGflCCRKbN80gpndHXQoJOgTY1Zp7DVaSmxOStHC41grajIYlX8oWoEboD2J6n9t8LxByX_ZF6GjzBtPK37locXJLBlq6WtoNxQrL1oZJ-ZYqYDCw_Oi9OC_4bJL2fOXIzPh7h7Zbq3OpPjzXQhbyOWKiv8utEoTBATk5U5yQs_NzZDxibbnVbwx27oNckLTQj41_YerNwBhu_jbfK7gL3J591jjCKtaaPaJkqG06w3JkbPiVOdbeKEA7PtVeZxHRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی غذا وارد مجرای اشتباه می‌شود چه اتفاقی می‌افتد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/696168" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696167">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN7EDa810aTD4Hs6FomKbHppRFaNxLrqiKa6tWX_2HXq3HZnRxm5fERKrzyCQLuPPZ6UxEKrZCeNe4X3CDxXndpkBh8dDoPyAVOixv1e68Iq7iFm_5MRZ8aLRsDfN5m24uk2d7vsb1uJc2j1olccOY0mStz5c2lwnXw0LFpiWUrhqnALBmsPHu7sghGotXIngwNFZ7HehYluIhFcqT3M0CmI55ylJyIYg5UT5FvWyEGtQOROAB_nqCMCjnf7NvBbfrVAGDKfWjEHmWePRzjajbii_lyP-WKuTb6R8L5XXARm9-wRoyxUb5ZYZKLa5gKROAiDXJDwhoO8qB38WO3nag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🤝
مشارکت بانک تجارت در بازسازی زیرساخت‌های علمی کشور
💠
در رویدادی مهم برای تقویت زیست‌بوم دانش‌بنیان ایران، تفاهم‌نامه بازسازی زیرساخت‌های فناورانه چهار دانشگاه صنعتی (شریف، اصفهان، شهید بهشتی و علم و صنعت) با مشارکت وزارت اقتصاد و معاونت علمی ریاست جمهوری امضا شد.
🤦
بانک تجارت با مشارکت در تأمین مالی این طرح از طریق سازوکار اعتبارات مالیاتی، در مسیر بازسازی و تجهیز مجدد دانشگاه‌های آسیب‌دیده گام برمی‌دارد.
🔻
دکتر اخلاقی، مدیرعامل بانک تجارت، در این راستا تاکید کرد: «حمایت از زیرساخت‌های فناورانه دانشگاه‌ها، وظیفه ما در جهت تقویت ستون‌های دانش‌بنیان کشور است و بانک تجارت با بهره‌گیری از مدل‌های نوین تأمین مالی، از این مسیر حمایت می‌کند.»
🌐
مشروح خبر
👉
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/696167" target="_blank">📅 18:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سازمان جهانی بهداشت: نشانه‌ای از طاعون در روسیه مشاهده نشده است و خطر شیوع برای عموم پایین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/696166" target="_blank">📅 18:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696163">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNZijNWVKRFGiQo6pG_f4MqsaABX9tNAln2AhLOcMSclApmFshBqI7LUAMHzzgN5Y_fV8iArTCgOOmvL33u43L42cwGKVqQFNv_zw_VVRxjgEuct8VrkPrnvHo-b22xsQnmZFVHEfSbOoRDzOjBIXK9cD0fZNnh4rtLTgSc9hhWUCz0f3DQgyDi0Y2MWd7Rhfn2R7eH9eoyrxqE3vS0gsmU9KnmMEZSDaYlcJ9IwwJdHUPQSq1kjRL6wXUXVXoUxuP9XQKtbsokPw4tyDXajYR6oQczS0Oh8jBzv8tJkKb2F6OJL_a1z5C7k-XPfxOSX9F0t1k_tRISXQ7XGNNTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/696163" target="_blank">📅 18:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37c23244b.mp4?token=Zun9FY0WPCKDED4RuYsgsM6JWLGudgNglK_TqG0gziDsCNukJTa-n9-UcC-4llQANr4_fi0TeiWilCkSeWHXBfFGmdTD2WZz21MMeL6jZth9z3-0XFJGf-lxRi6XFQcn_i02aqBGAsDcxF1AR10JzsRrkz0ik_0JdIMATQGUanE0H8xinOe_tH-lAFIhYxUs8I1PUsPMhUXl8ECQG_ri-Djmx_B3BSd-oPM2Al7z3hJgzYXnpS8D75c7WDPsk0xwPmIQtwYbOZkbaDkb3Sn9_ULBI58pzEbNSEctqT0MXlaZlAJceKKozi0JK5QGTIWzF51JioIL_I415sBo8Amf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37c23244b.mp4?token=Zun9FY0WPCKDED4RuYsgsM6JWLGudgNglK_TqG0gziDsCNukJTa-n9-UcC-4llQANr4_fi0TeiWilCkSeWHXBfFGmdTD2WZz21MMeL6jZth9z3-0XFJGf-lxRi6XFQcn_i02aqBGAsDcxF1AR10JzsRrkz0ik_0JdIMATQGUanE0H8xinOe_tH-lAFIhYxUs8I1PUsPMhUXl8ECQG_ri-Djmx_B3BSd-oPM2Al7z3hJgzYXnpS8D75c7WDPsk0xwPmIQtwYbOZkbaDkb3Sn9_ULBI58pzEbNSEctqT0MXlaZlAJceKKozi0JK5QGTIWzF51JioIL_I415sBo8Amf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت اعتراضات دانش‌آموزی در فرانسه
🔹
اعتراضات دانش‌آموزی فرانسه وارد نهمین روز شد؛ تاکنون ۶۰۵۹ نفر بازداشت و ۱۰۱۵ نفر زخمی شده‌اند. یک نوجوان ۱۵ ساله نیز بر اثر انفجار نارنجک پلیس دستش را از مچ از دست داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/696159" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رویترز: پالایشگاه‌های مستقل چین با کاهش شدید عرضه نفت ایران، خرید نفت از عراق و قطر را افزایش داده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/696158" target="_blank">📅 18:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2882a026dc.mp4?token=ctUGl2B2N49IhP-YT2pP6ryBMCjA2nfHCA_-XnpckTvC_avatwZEOdBEwr87hHWbjRqE5JR3JVobCgQdLUwnEaM55JOWy5Mfk_MK3NUioDeHOLZHPJQtC34wJKXVt9VRoXovnVFA0Md3w_wqHedmWk9aUwvCSTHtvLRYiIr8Q4PekvRgPSp-QpR__eG3erhZ5KIBfx1BawbH75CeTX-2zO3r_dpmHvybYyXi1Bb60fkt2RhSCQtWasb_BKCDV4D0AZmoh0AKNT-dROxM6nrZ5xLqYEz1ZF8lVnpKNhGPM5cKfZxap55DM4WiGRsmsIPd4FLTA0ByMw8ehYM68AkBJDGieUnpQvZkvEte90xg6FGrpfvJlKQk9uZf4vJFFDUg55DFahgjZL2mnzcK7x9LSsFgDhOsexqXW8spIp5yhq32Fw45bh_YBNIKRWNq8_XmsoeN62aJVUKpZ8yQlxEU83z4mLM5YsN_PehFh12SHS95Kiz9hBCDNgISWcQzFNHPXwQlLa0pQw4vU7VhYcDyTxiCKzBokwGTJCPlde6j-iK_ufv4zovrHJpbm8w_nhuGW3mp8Z4iQXJNFb5OqqUFxyMJruKKo7WfF4JX9K_yfnfY0oI61Qok_US4ZvwdI-2f3sg9Ilz7CFky9absA21ZljMz1ECOEj56NF8vbWYvJbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2882a026dc.mp4?token=ctUGl2B2N49IhP-YT2pP6ryBMCjA2nfHCA_-XnpckTvC_avatwZEOdBEwr87hHWbjRqE5JR3JVobCgQdLUwnEaM55JOWy5Mfk_MK3NUioDeHOLZHPJQtC34wJKXVt9VRoXovnVFA0Md3w_wqHedmWk9aUwvCSTHtvLRYiIr8Q4PekvRgPSp-QpR__eG3erhZ5KIBfx1BawbH75CeTX-2zO3r_dpmHvybYyXi1Bb60fkt2RhSCQtWasb_BKCDV4D0AZmoh0AKNT-dROxM6nrZ5xLqYEz1ZF8lVnpKNhGPM5cKfZxap55DM4WiGRsmsIPd4FLTA0ByMw8ehYM68AkBJDGieUnpQvZkvEte90xg6FGrpfvJlKQk9uZf4vJFFDUg55DFahgjZL2mnzcK7x9LSsFgDhOsexqXW8spIp5yhq32Fw45bh_YBNIKRWNq8_XmsoeN62aJVUKpZ8yQlxEU83z4mLM5YsN_PehFh12SHS95Kiz9hBCDNgISWcQzFNHPXwQlLa0pQw4vU7VhYcDyTxiCKzBokwGTJCPlde6j-iK_ufv4zovrHJpbm8w_nhuGW3mp8Z4iQXJNFb5OqqUFxyMJruKKo7WfF4JX9K_yfnfY0oI61Qok_US4ZvwdI-2f3sg9Ilz7CFky9absA21ZljMz1ECOEj56NF8vbWYvJbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش ساده برای از بین بردن لکه‌های بدنه خودرو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/696157" target="_blank">📅 18:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c97c9700.mp4?token=OHJa-PYpc57gNwS0_P_5hZEKKj7bw3FPAILGhZ0o3tuF2xcv_2IBYLEJXJ02ZdDQ-eoS91hT0pWmAwQRf7Jmis40Nc1TNExCrbWh9hIpXE80ybaKPajtW35FUQdZYl7SOmerr4Rf-YhIV0qj7FC57q8Qkf46IzF29KX7YJE5GqYNRFvAPDoEDtxcdZl4dtfCB3-nTc9_vXV_SwhZ2JOalASsJ-0H_VzdazjCi719r2II0-Jmu9UbLJ-CjeacRgzDYF7HXZfu_cYD37yybbaJghdPAEYsPPeyCxbXOeI2fAwJFxuo99g4JsK6rSxulH3QBG0REM2ipnogs-0KXwyZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c97c9700.mp4?token=OHJa-PYpc57gNwS0_P_5hZEKKj7bw3FPAILGhZ0o3tuF2xcv_2IBYLEJXJ02ZdDQ-eoS91hT0pWmAwQRf7Jmis40Nc1TNExCrbWh9hIpXE80ybaKPajtW35FUQdZYl7SOmerr4Rf-YhIV0qj7FC57q8Qkf46IzF29KX7YJE5GqYNRFvAPDoEDtxcdZl4dtfCB3-nTc9_vXV_SwhZ2JOalASsJ-0H_VzdazjCi719r2II0-Jmu9UbLJ-CjeacRgzDYF7HXZfu_cYD37yybbaJghdPAEYsPPeyCxbXOeI2fAwJFxuo99g4JsK6rSxulH3QBG0REM2ipnogs-0KXwyZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکای‌نیوز: بیش از ۵ هزار نفر در پی اعتراض‌ها در فرانسه بازداشت شدند که بیش از ۴ هزار و ۴۰۰ نفر آن‌ها کودک هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/696156" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مدیرعامل آرامکو: حتی اگر بحران جنگ علیه ایران همین الان پایان یابد، امکان‌دارد جهان برای پر کردن دوباره ذخایر نفتی که در طول جنگ مصرف شده‌اند، تا ۲ سال به حدود ۲ میلیون بشکه نفت بیشتر در روز نیاز داشته باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/696155" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0d78119c.mp4?token=NaxY1afWtnwD0G6S3b8wJcDjtcqudGjYdxTb9duC7npERubZekuG9CQBPAvReAHIEFPqlx86ZCxqUer9JlmMXP3oDdP9ij67g_FWJTxIMdPLbsxvBha8uBfDdmS_mmIXnHtLJTH--8vjiDSDd7j6cjb7YAKymxjqUS2NlTKx1hnxcTYMY6AycYQx_pPb6_VSuR8HcC39PHy8ccomDx3UAOGpGjJaMwaEbdEv8aYvdNjnYTqVS5MQOVtMASbieM91Vg3w7qlws3BnqOiBz4kvtu-KCugTytc1NYaM5ZAqSl0P_sJSjrVKn1f47o3VHpMXyEQSpc_TKOo7mfaVfQSDlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0d78119c.mp4?token=NaxY1afWtnwD0G6S3b8wJcDjtcqudGjYdxTb9duC7npERubZekuG9CQBPAvReAHIEFPqlx86ZCxqUer9JlmMXP3oDdP9ij67g_FWJTxIMdPLbsxvBha8uBfDdmS_mmIXnHtLJTH--8vjiDSDd7j6cjb7YAKymxjqUS2NlTKx1hnxcTYMY6AycYQx_pPb6_VSuR8HcC39PHy8ccomDx3UAOGpGjJaMwaEbdEv8aYvdNjnYTqVS5MQOVtMASbieM91Vg3w7qlws3BnqOiBz4kvtu-KCugTytc1NYaM5ZAqSl0P_sJSjrVKn1f47o3VHpMXyEQSpc_TKOo7mfaVfQSDlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان انرژی اتمی ایران در جمع خادمان حضرت رضا(ع)
🔹
محمد اسلامی، معاون رئیس‌جمهور و رئیس سازمان انرژی اتمی ایران، با حضور در چایخانه حضرت حرم مطهر امام رضا(ع)، در کنار خادمان این آستان مقدس به خدمت و پذیرایی از زائران و ارادتمندان حضرت ثامن‌الحجج(ع) پرداخت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/696154" target="_blank">📅 18:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیوپنا(پایگاه خبری دانشگاه پیام نور)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9bXZAVmaHA9F3fm7Djje3_J_7XdllGspDtO4Gfp-az8dKktwj_WHVwRpCa6afbziByrueJaRc91f4jnTj9MVrTq1CjHDwyT2zMpJn7YfBqb7-npUzB1BbYPREdOAPA0qM3fBVImfD48ohsIXqzl3R2nG1TzOO-4rnFNLkxHbRxnwdVZMbnn-MWbLRtmbYUr0AZ9RTzc7HBKhgwR25a9aAas15iXSu_8dt_9j6dYVS1Royrjf0bgZxiTM8WBRiZJLpuiOISODXiFQJEQaqv1vmDQ8qyicWBYpA-HRYEXOJsLqEYKRwT87CgIq7hj5PCNanbrFAMVNyOEg4-BrPBUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
از انتخابِ خوب جانمونی؛
📌
هرکجاے ایرانی؛
✔️
فقط کافیه انتخاب کنی
؛
▫️
انتخاب دلخواه محل آزمون
▫️
کلاس‌هاے حضورے و مجازے
▫️
وام شهریه
🔻
مهلت ثبت نام؛ تا ۱۶ مهرماه
🔻
سایت سنجش؛
Sanjesh.org
┄┅┅┅┅┄❅
🇮🇷
❅┄┅┅┅┅┄
اداره کل روابط‌عمومی دانشگاه پیام‌نور
@Upnanews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696153" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZPhi6U3Wb_z1mfrT1r-XR3HUuoGns5V-TTlwpKHCSbUKw6hz1UNX_dFI08rVzcAba84mWo5lvc2-yMjyvqMtreIl0XAE9cwlrFLF3P_KAbq-plkPqZkBU-Wki2DEpzIQ68tfTtbDp1IISOdN0gQpcaLxDoOVMMYSHmCbYnLrURlTPtcU6azye4q2QsJMFDHqXlZ7v6sdoB8Muok9qonerIv10SiVWeRWW9f4a0p1MmriUTrlfNK73rSK-vq67hFXgNo95b1ejhO2EC1NM9dK8GJDfJP5ocn5UWed-luWGPzlY6rOhBgdFhWLjq98IBqH3YFU9UP4QE-jAGw2KszmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دیوانه: راهپیمایی‌های من دوباره حزب جمهوری‌خواه را نجات می‌دهد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/696152" target="_blank">📅 17:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f0c1a81.mp4?token=vVWKnYOpkIM6i6cSrmB0FFcl29XQlPFd3MclwdONEv_WIFnVHlGwFGGwwRxGQLDegfoNprQVfVHUL73XEfxAztOvnIyH5UL-ssia4x-20icY5H53y_MopIqY3lzJ0DRSOiMfhY-1jCcXz8BA0jhyjlE539pv6bWlEfY3cFGsKe7BJcgC4CckQDh49Fv_qyaZYLfmsML3RmhtCfyuDgHj-OalGaW7pMCahVpcl2T4BckvR-d843r303ovHjY8HY98ZjTpODVpxM4todZuJfVeC9JcfNKZc34WB__VifOTYnK7y1PYkadDW45Hhmy6dCBK5eMkLA1oJ_0RKhx2Z1DSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f0c1a81.mp4?token=vVWKnYOpkIM6i6cSrmB0FFcl29XQlPFd3MclwdONEv_WIFnVHlGwFGGwwRxGQLDegfoNprQVfVHUL73XEfxAztOvnIyH5UL-ssia4x-20icY5H53y_MopIqY3lzJ0DRSOiMfhY-1jCcXz8BA0jhyjlE539pv6bWlEfY3cFGsKe7BJcgC4CckQDh49Fv_qyaZYLfmsML3RmhtCfyuDgHj-OalGaW7pMCahVpcl2T4BckvR-d843r303ovHjY8HY98ZjTpODVpxM4todZuJfVeC9JcfNKZc34WB__VifOTYnK7y1PYkadDW45Hhmy6dCBK5eMkLA1oJ_0RKhx2Z1DSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکای‌نیوز: بیش از ۵ هزار نفر در پی اعتراض‌ها در فرانسه بازداشت شدند که بیش از ۴ هزار و ۴۰۰ نفر آن‌ها کودک هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/696151" target="_blank">📅 17:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
به‌دنبال برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز عصر پیر کوشار سفیر فرانسه در تهران، از سوی اداره کل حقوق بشر ایران به وزارت امور خارجه احضار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/696148" target="_blank">📅 17:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91d320c89.mp4?token=PLDnTiRQfxobudB9uEQF3X6ik3CVh98xA9VmJtcIgys_X_bOOnYdeRVvPK5twQC6_HEXVxxMyO6LRyy85YnY_10_sok6WKWGoIYG184UDMdUZcx_1dkDJYGu5qK4RBIQRq96S9UBoDWiNso2QEwBlbF4oce4sAHpwaWSbaZz__Z16zIBNIWWeS4AlH-ucFagPZG_57H8cfRMpqcUzfIvfFbcGlL8gSXielhA0cpQ2F0bcMLg7h1gGONCgNm9BwDQY4RGGt7Y0w0sAgTlNVWlTeis3xz1bInR5r99T442bIXqUiyS5riBpePQzWJJKV3EB8yRXK6JcxzgTYcYhHsnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91d320c89.mp4?token=PLDnTiRQfxobudB9uEQF3X6ik3CVh98xA9VmJtcIgys_X_bOOnYdeRVvPK5twQC6_HEXVxxMyO6LRyy85YnY_10_sok6WKWGoIYG184UDMdUZcx_1dkDJYGu5qK4RBIQRq96S9UBoDWiNso2QEwBlbF4oce4sAHpwaWSbaZz__Z16zIBNIWWeS4AlH-ucFagPZG_57H8cfRMpqcUzfIvfFbcGlL8gSXielhA0cpQ2F0bcMLg7h1gGONCgNm9BwDQY4RGGt7Y0w0sAgTlNVWlTeis3xz1bInR5r99T442bIXqUiyS5riBpePQzWJJKV3EB8yRXK6JcxzgTYcYhHsnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکه‌ای از بهشت در لرستان؛ آبشار آفرینه
🌿
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/696147" target="_blank">📅 17:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با مفهوم علائم درج‌شده روی برچسب لباس‌ها آشنا شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/696145" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎂
برج‌میلاد‌تهران‌تولدش‌را‌
باشـهروندان‌جـشن‌می‌گیرد
🤩
تا۵۰٪تخفیف‌ویژه‌بازدید
وشـهربـازی‌بـرج‌مـیلادتهران
🚗
نمایشگاه‌خودروهای‌کلاسیک
🛵
نمایشگاه‌مـوتورهای‌کلاسیک‌
با‌عنوان‌‌نمایشگاه‌"پـلاک‌طهـران"
👶🏻
بـرنامه‌های‌ویژه‌هفته‌‌ملی‌کودک
همراه‌بازدید‌رایگان‌کودکان‌زیر۱۲‌سال
اجرای‌ویژه‌برنامه‌‌بچه‌های‌ایران‌قوی
🎸
همراه‌گـروه‌مـوسیقی
👬
اجرای‌جُنگ‌خانوادگی
🎭
باحــضور‌هنــرمندان
🗓️
روز‌هــای ۱۶ و ۱۷ م
ـ
هر
🕐
ساعت ۰۹:۰۰‌ الی‌ ۲۳:۰۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/696144" target="_blank">📅 17:10 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
