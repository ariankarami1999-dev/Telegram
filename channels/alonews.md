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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-127891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت:تصمیم‌گیری درباره تفاهم احتمالی با آمریکا در سطح «نظام و حاکمیت» انجام می‌شه و حمله به مذاکره‌کنندگان، حمله به یک «تصمیم ملیه».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/127891" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edV84_3o6K6Lqd-pYk9BImb7oAc3aTGPkmgtgZz_unbxUW9VBSlchz-qSlT6zHpBcdS-QFs2zGtVxCr63BO6f9zDWjn4MdHwUwGMNjOwbfhS13uAin5puInIqzNYkxCeD88beC9QQlfwKg6Nk9ZIbLImuHI6BwsjZKJm75gLdxZp3qtmJhyAbKpQq4-srxHjt2q7_vpBkRtcejWRuW-xNtMeDn2YEdl3kmLE-_Mh1lZz3eMAkhC2U-AuePDhIHZwXibo2VrZYvph8N27b_BgpAiB4k3FJBmeZA-q-bojWmigloJzk6mRf5j-azg32k1bQhF3wFpMnRYr86exavx33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده درحال اعزام به تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/127890" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4897b39440.mp4?token=R0i0j0-4PI2Y_4jinyJqysGzE7ppyc1iLBsh9HXePV_GvKhHlCv7LqVIRpnqcvJB6nUANp-Yp1r5byzQvLu7yxs608iLtanZpiMP9txyu4owLsSSIbgSXqDVmcdxxpr2vfwPWbfy0YNCUBtLfrpwHzwUZ3JfBBbheS8iIy1A1bqh44H_mtJv3RB_OVr41WGGuDV__CiLSSHO0NPHAM1ij_wZI4Ct1nbdek4Y0ShtSXImFzClKGb4O8aXiiDsVKvy8EQJ4Lmd4qM6etOL-1nS1V90ca4EcMrFqDQpYaEeld8VUdqPdM9rJg7emSm7q8wda50Q8y1hBPhQCPjz2XMxWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4897b39440.mp4?token=R0i0j0-4PI2Y_4jinyJqysGzE7ppyc1iLBsh9HXePV_GvKhHlCv7LqVIRpnqcvJB6nUANp-Yp1r5byzQvLu7yxs608iLtanZpiMP9txyu4owLsSSIbgSXqDVmcdxxpr2vfwPWbfy0YNCUBtLfrpwHzwUZ3JfBBbheS8iIy1A1bqh44H_mtJv3RB_OVr41WGGuDV__CiLSSHO0NPHAM1ij_wZI4Ct1nbdek4Y0ShtSXImFzClKGb4O8aXiiDsVKvy8EQJ4Lmd4qM6etOL-1nS1V90ca4EcMrFqDQpYaEeld8VUdqPdM9rJg7emSm7q8wda50Q8y1hBPhQCPjz2XMxWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی از یه حامی حکومت:
آقای عراقچی شما گوه میخوری وقتی رهبر چیزی نگفته حرف از مذاکره میزنی.
اگه می‌خواین مذاکره کنین اول باید خون منو بریزین، خون آقامون هنوز خشک نشده، بیجا میکنی مذاکره کردی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/127889" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ما برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/127888" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال 15 اسرائیل:
تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/127887" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اسرائیل ارزیابی میکنه که ایران در واکنش به حمله در حومه جنوبی بیروت، حمله موشکی به خاک اسرائیل انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/127886" target="_blank">📅 17:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwyiavCfM73PBj3LtAjS7l3tvd2v9dieim9g_AEN9diziNqAxy8EN_yq7C5H5cISlGxMXWjQTyJ0LBqseMjjE9ssR_3rTS4A4Kdc0V76PVwU8FmZn2o2TTi-BosgkJqE8oiq8zAra57-D6euk1JDz_0Fa2hHZBPGF_Fcio7vDFuGLiK6jKbDr7mb1Ml7u2QP6Mz60T13aiT1sLywQ4y6uBBgSgn5j0WAFd0N6JT6swQ8ItJHNq6aR2ObvlziRkgbza7VIDLaRZVhw5fosXlGQgmMG-De_jXDJnR1AQ7hLi6nPIhpWQvtRWeLjHHujIEYhNLArH88QkeKicSPSIMDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/127885" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4QPERifjeO-6C6xvAG37p7WB9gdDlQtTD4bIRMBbXaG5fTd8-h1TAqeMG-EHWXM3RyFcfo4aq9VCZyHX050fvKaNsYm-o5uUP2To78w2n0crK6Q3vc7FvBLNLqo9fHJreU3ZW3pcF0SVsVsq1B_1OHM2GAlHD8Glh-L8l6YPTTP4A39YXdsyCGeIooIvt2xyjbiORoXRn9IKxYFiFC56iIBZdkvWfrWsYfaL6awWu4KHt1kutO7qxEa8US4eo12b9e-0ahcY3cNKtUBLohDgp8v1lnq7nwCnoPuStLLf91R7r52Xv5hJ_X5YH2aF-PHKSwJFQ9bvhHQL0amAdVDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
بر اساس آنچه چند روز پیش نوشتم، و با توجه به ابعاد تازه لبنان، افزایش مخالفت‌ها در داخل ایران با توافق، تردیدهای مداوم در مورد تعهد واشنگتن به تعهداتش، تغییر مواضع دونالد ترامپ هر روز و اصرار اسرائیل بر شرایط غیرممکن خود، هرگونه توافقی بین واشنگتن و تهران بیشتر شبیه یک سراب است.
🔴
در دوردست‌ها به نظر می‌رسد و نشان می‌دهد که رسیدن به آن فقط مسئله زمان است. سپس محو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127884" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تتر هم اکنون 173000تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/127882" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127881" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9U-fH57KY4qRWFbn6NWQL5q5Hutek9l0RgnVgS7eAYFpePEtni62G7stoVuU2pgVTmgmfGkm8YD_LK04Go-5ofERM7S3rcjYimIYavzseZA_Nr4ZTgef3NylsgEuB0L0apuXj_6w-__P0BwE5acADw6dVvGn4punKdlFcSLu7aULCM1Ul580FULVqoeCyeOZxHBcUQqoNCJBC_GZHKP099YNm8hv4DsPf374vo1jJ4N17BtfJ9uERKfattwOpnzuwJKjFf_HUp6lOaScQGdc0lZcMwPRD_MHQL5iii_vDqspbAALTook89QsgggIWHUk82WbW-yZ8GusopvJjq8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل: هدف حمله نعیم قاسم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127880" target="_blank">📅 16:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/127879" target="_blank">📅 16:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی: https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی: @exovpn_dl</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127878" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXoCSqlZnp8UBSPnzE1t7yqScgnBICDcxrNQqZVc8IpH71q__D1OXVD8WM7RBxFTUoy91SEXnk5jpVsItLXrmbPkmLVqHWdPYgAhbOE8wcY_EC6WHFtTROude9IJyqOOHqHM-3zCxsMTHhwIT2Oowr19VyZZwkXUNgyhwg-Sz5U5uCbaFSLeco24mgPhHCmIl-v5sdpGOcafIM4pcGDoELIGObyiIMEyAPrPbUcPH5JteeOGiXqz3cX3OZ-C-wb2wOT1RFqhZ5YXsWEicU_a08mx_9XKvV1u-JdDXJ9gBjIxe3VqOwSyDZU2HFOuXMm5V4Tqqh3NfI9xiMXYHKrWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی:
https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی:
@exovpn_dl</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127877" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=FBm_zWRFG5nfpW9rFiQaEkvkkEgl-Un2-BtniIndbHU8LD3aS7K9XUjCBiwsJ4ITba2pfroAaRCyAaehQ0oYqI2B2yf6_bg4flR-wxvPnjHNVcW_6ibsloJ-OglLjRuTbQ7VC8Ta7A4rK7YM6Ye6n3gytU1VfIupK7XFDPHL8rRADglr2xluuE5Ob4AMzT2w3FU0eJgHkYASK0wX7kegeM8zhuvB9Bd4FvF-tGL-5dpz9_5hkLXr6uBX6WnhTBlYdSePQsL_cjfUWZIs2VbNBPmgP9s7BzDv91OFL4vB5WtTMGATxHHMpK_KOP9zs3GDn3JLx-EUIbfJXM_Rkw6aeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=FBm_zWRFG5nfpW9rFiQaEkvkkEgl-Un2-BtniIndbHU8LD3aS7K9XUjCBiwsJ4ITba2pfroAaRCyAaehQ0oYqI2B2yf6_bg4flR-wxvPnjHNVcW_6ibsloJ-OglLjRuTbQ7VC8Ta7A4rK7YM6Ye6n3gytU1VfIupK7XFDPHL8rRADglr2xluuE5Ob4AMzT2w3FU0eJgHkYASK0wX7kegeM8zhuvB9Bd4FvF-tGL-5dpz9_5hkLXr6uBX6WnhTBlYdSePQsL_cjfUWZIs2VbNBPmgP9s7BzDv91OFL4vB5WtTMGATxHHMpK_KOP9zs3GDn3JLx-EUIbfJXM_Rkw6aeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو دیده نشده از هوچی گری دیشب تندروها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127876" target="_blank">📅 16:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=NgCjdnBDn7osCnkty4FislCdn6ciVTl8vwm9mqnimxvS1Vw1_FYiHoUQNJxDOCmTQvkLhQ0w924Anyeal2dfS8g5M5tggfYdk6FRWott7-wOcrbhcBZ-RB3tyIy-ac5KvPGV9eKOfmrvX0IjUrclUMfElgt2lPjY859b3h5gsuvDDvX2tBWHMkNoEs1E9GsLzmbuH8K9-vAwDcQOR7V4g0qQX94HriUE4ot7VELdzs81vV0_aERIpckaNErcl_Va0s4CQleV2_5MIKlqA2Dk-ZMGdnETxfJKJVS9CiprdndX8TsEHCmgwM62tuRWuZbCSNJkUDQC-jWYW61iT7pHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=NgCjdnBDn7osCnkty4FislCdn6ciVTl8vwm9mqnimxvS1Vw1_FYiHoUQNJxDOCmTQvkLhQ0w924Anyeal2dfS8g5M5tggfYdk6FRWott7-wOcrbhcBZ-RB3tyIy-ac5KvPGV9eKOfmrvX0IjUrclUMfElgt2lPjY859b3h5gsuvDDvX2tBWHMkNoEs1E9GsLzmbuH8K9-vAwDcQOR7V4g0qQX94HriUE4ot7VELdzs81vV0_aERIpckaNErcl_Va0s4CQleV2_5MIKlqA2Dk-ZMGdnETxfJKJVS9CiprdndX8TsEHCmgwM62tuRWuZbCSNJkUDQC-jWYW61iT7pHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تولد ترامپ
/
حرکات نمایشی موتوکراس در چمن جنوبی کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127875" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFJ3ga77Nl0USlIYQ158zNtc9kpBBkXZ6pdYKaCrIEBxLynNuJlFEHn9Zq1-Culgqevg48FOMbXVDgEBLGIMayJ2kJ4_jAqtBZj1rYroemeY4meTeYxuVpaN21SgnhC-jHMOcSbEWeBvXYtHQB4kTN70kBuV2lRAbTK-CvHpxZM1I5Lss-RpECIAK4bY_zvzW0QEK_AW9fP-6EEyCOFU_9lTTAQJ0yr5YWsFIECIeoelWvhbC2NaP3s0h4Jn5vu4OoRzw3QEn1OgAHwbutgcAxSW7hAkqc-yWSp6bUwSMWj2x1e-iBCLJ-E2skI_yLF36GVUyj3VLj3KJrZhbwsTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUbOGN7Bq7tCVlz6k-oPgTjTrRdoEXB8q8jIsRcyn-qQzjiS76YguT6Amtg_F8CK8dvc1CCMqr66jFR6OiA-EFDElcQZLArkgDMVVqGWKw70YkKCzalS9laUwgkgUQW8lwPPuZEoEcq6S-G7zDUvrmCoYEL9dOIIQu80mc1_p_BpbeBQ-H7VtJTOQTo_HpEoAZx-dLX4oX8Nid5HkrcRbAI3eu9m96qFJeR4pW3JqDcz0_oe5boicyVk4Jwr9aKuEKYVj5xZPvF6S-XKjrk97cSJfmwNHKKVsDDdAvdeTJdnvxoehbdmWEjfBiugqq6hsLAexKt_KRMua2JTkFrPqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نتانیاهو ابتدا تصویر حمله به بیروت را منتشر کرد و در پست بعد تولد ترامپ را تبریک گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127873" target="_blank">📅 16:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvtxhqPTsLPZnlev7OkMRzG0ybqQMc1YNpan3D9WVV6kraQoL8qwSBC3Lo7U6YuP79wIgxs67rYae5WsCSuzAPYump8gYJJYtatN0asyOfMyP25krYhrdi5-8kvnlnQQHQG9_UgveXx3ZZGOXJhzCwXOx2Rbb_980qmnRNtRwPdEtCMDKlmULl16KcTITJYpnZeZe_AFS2nsRj8hxod6vSsApLL2MIADfuk2P7qjUF2dcnDNlY454rY3uqQf1xLm1K8Qu1Ufq5IKifO7cWp44j8YN95zPTlAVf58Ew0nCo-tAsbTC2bKUXl2pitZqi-US0Ur7dKC74sZ4dEYIopiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127872" target="_blank">📅 16:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قرارگاه خاتم: پاسخ کوبنده میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127871" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تندروهای ایران
🤝
اسرائیل
هر دو مخالف توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127870" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfXLqFU5JptvVdK1EY8CC0WwNIMnkLH8tTdOSaRIl8VgBv9Zlaq_uOKLfi99owX0aS5-o6mA54uM9EDV5EX5c2buBuwEdE_6SHeY2RSEuyq6Vwtc_XRjx3W9jt8FALGiTp_R6hngLCtk3E-H68tKxVYtnHoNMiWRcFR0760i9ZrTeWXaLvoV0w7DHjF9Ppjesgfzadi62UeHA2oB7xb5Zqt79U8EbEQXyIdmY2fnY44JEDy2TFv9V0H7klo8tdWQ6yNkXsDd2dRF_FP_MeXdqmRSenBrMr7X38pJ2nP_Wyyw285aVE9eBORVvPUmuMcWUFSIsqOrJ0cy7w8jD0sFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر عجیب منتشر شده از عراقچی در ایتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127868" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT2reubzUb4qNQG0P8GQAyD6oGuqno32AOHSc_VpGPW2T3zBzciYe8iHB1z8nIU3VRITDSet4BibK9yVhEsghw-t2m4hAjEWhcpkoWCiJYxuqO9KE9bNpBl3jP2f0-cbcqyfhsCJbvcid-XCjqOQPBqJiasqnqjrYTMoej7gm23NntA35GzcHQ1Fp1jd0OFUSzGGt9_SpEnVHya_7iP6lugVMZFg-zoHzPT3zBYr56jczOn-EQbB4Wdrymxq4XPZGnz6Z97xzjKy4X7idwm2No0mXWUv2dCXjg7VFIYZ8LIxVRohqgbGohR29LamXRXF18805u68ngbsW9z1p0x8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف : تجاوز صهیونیست‌ها به ضاحیه دوباره ثابت کرد که آمریکا یا اراده‌ای برای اجرای تعهداتش نداره
-  یا توانش رو با چراغ سبز دادن به رژیم نمی‌شه امتیاز گرفت
- بازی پلیس بد و پلیس خوب هم دیگه قدیمی شده
- اگه نه اراده دارید نه توان اجرای تعهداتتون، حرف از ادامه مسیر بی‌معناست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127867" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0e8d393.mp4?token=JvTMQPvnXurjhlg8ttz8O9Ik8TswI51vF04-wRzG_SD94b5KlZyQU3RUxvkK3mraQGPo_IoI9ufGmPddexJS_uQ-8paw0cz6kaoBcDvu6ikhTAbXdk5e4LCkmHGayyv1Lxe-o3ezCnj_MJwiyzxXQrBQTcANg6c-mgtiX4q36-OOJ3Bq9sJsYWJOjgJcropdKSncJga7gVxg96Jd0l2jaLaGoQyR7F5uX5sCMF2Z5OAkhzDNuJC90G6qWN7W9bIgnqw-8qIfsOiZNgdOFoGtpG6LE5z0W_tdeBFlxmnZNv7zJsjlfX4QWSLwjRquNXgzYfZ50v8e2XhzsbnMTOiYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0e8d393.mp4?token=JvTMQPvnXurjhlg8ttz8O9Ik8TswI51vF04-wRzG_SD94b5KlZyQU3RUxvkK3mraQGPo_IoI9ufGmPddexJS_uQ-8paw0cz6kaoBcDvu6ikhTAbXdk5e4LCkmHGayyv1Lxe-o3ezCnj_MJwiyzxXQrBQTcANg6c-mgtiX4q36-OOJ3Bq9sJsYWJOjgJcropdKSncJga7gVxg96Jd0l2jaLaGoQyR7F5uX5sCMF2Z5OAkhzDNuJC90G6qWN7W9bIgnqw-8qIfsOiZNgdOFoGtpG6LE5z0W_tdeBFlxmnZNv7zJsjlfX4QWSLwjRquNXgzYfZ50v8e2XhzsbnMTOiYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این هواپیمای روس نیروی هوایی هند روز گذشته حین تلاش برای فرود در منطقه جورهات، سقوط کرده بود.
🔴
ارتش هند با انتشار یک بیانیه، اعلام کرد که در نتیجه این سقوط، پنج نفر از پرسنل نیروی هوایی هند جانشان را از دست دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127866" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127865">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سه کشته و شش زخمی در تلفات اولیه حمله هوایی اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127865" target="_blank">📅 15:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت امور خارجه لبنان: ما به دلیل هدف قرار دادن یک خودروی ارتش و کشته شدن سربازان، از اسرائیل به شورای امنیت شکایت کرده‌ایم.
🔴
ما به دلیل پاشیدن آفت‌کش‌های گلیفوزات بر روی روستاهای مرزی جنوبی، شکایتی را به شورای امنیت ارائه کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127864" target="_blank">📅 15:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgPJb6iv4mx-jX4YJW73R5wrbLvg2MJmmB1tAU3sNRmMqIPmN9m0_mA0WsR4ZqekgDdvStX7FUZAStOvymLM-AiWd_nan_tISEdev7oy-J26o6gJoOH0gsG1iex23Td3RzMx-oxZ8LhadSmuwp2N9ejLLTv3ZPjOVW0ATU5xdzWlqWTxLqvaX0ADLXxMSQpU8WHsTjtc6loxaljhV05fNLJgFeNlPCNXdggKJAvDI5zs6l9YNHBED0cdKGHEdn-mJDIQR_XIMfqi-5toibGcRawghEyEwu2UkX5vm3il1x99UAVc6VBo-yIGBDOPob62claQfR3PzCC1wNiUQfxXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: مقامات اسرائیلی و آمریکایی می‌گویند ارتش اسرائیل اندکی پیش از حمله به بیروت، فرماندهی مرکزی آمریکا (سنتکام) را مطلع کرده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127863" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عراقچی: سرمایه اجتماعی و انسجام ملی، امروز یکی از مهم‌ترین مؤلفه‌های قدرت جمهوری اسلامی ایران در عرصه بین‌المللی است و طبیعتاً هرچه این پشتوانه مردمی تقویت شود، قدرت چانه‌زنی و تأثیرگذاری دیپلماسی کشور نیز افزایش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127862" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آی۲۴عبری: اسرائیل در حال حاضر از اظهارنظر درباره اینکه آیا هماهنگی یا اطلاع‌رسانی قبلی با واشنگتن قبل از آخرین حمله به بیروت وجود داشته است، خودداری می‌کند
🔴
به دنبال حمله قبلی در تاریخ ۷ ژوئن، موضع رسمی اسرائیل این بود: «ما در تماس مستمر با آنها هستیم و آنها با سیاست ما آشنا هستند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127861" target="_blank">📅 15:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127860" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نتانیاهو: ما به اهداف حزب‌الله در حومه جنوبی بیروت حمله کردیم و حملات علیه خودمان را تحمل نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/127859" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkx6vxj6S1IMyu5bP7gC4Ur2SVCW2fdgOyzxZ19sirkcAObpnTur2C9PsM9ho6Z_wCicnqtDf9GhuCIFjuO_VyHbm5GzN-IJgQefca6pnr9uWaf7tNpBq-fNXvoWEBxONWYnZMarH1pzD3JtvUdJHWGyEvbavyhu1lCN_0j5xm5_ymH3THOmxQtFngCiQroWqda09wP-lVfQCyj2--oVp2roOqhN-F9koXIPFagjtzHlBmM9Dv221OlxMPWxuflzXRX6tMbWJLMPlcRCQC8hTyyh3IhffkVXE0HrdF_79gGhw66Gw1IPE5ekV00kHKk0IkmUSgUWx32tXHCrdGxgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اکانت اسرائیل به فارسی !!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127858" target="_blank">📅 15:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/127857" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJJHs2c3aQ5Q_0ut3hVggpbbRrPIF3LWZUf0DX7YvwuLfQnSPnaI37sVBndE88JBJkKVMGVvvxj_CRUWe5Y2ktnjJ_VMb6er0gKBPHstrvLWjZU-aZbtR1scUecfYjMp414-ocZbMyAa9weXafLKeUSLvKJXTpM9CykVyeWYE9d-Pm2_p9E9HumqRTTJw-1FNEQm1lwd5p1cv8PCBpmvAZiYfrGRpRHzj3Cmf5Ivba7T1AunsNye2Tqbk_OMxRR0JSsZzZfcOVWN6l72qun2YOD601e1gUkT8ST169NVjG-8vtZKwzoL5r8azkdebvQYHIRpFD39PJgE7o9W3TpdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ سخنگوی کمیسیون امنیت ملی:
نباید اشتباه محاسباتی کنیم
🔴
حتی اگر بخواهیم به توافق یا تفاهم برسیم، راه آن انضباط دادن به رژیم صهیونیستی است. اگر این سگ هار کنترل نشود، امضای تفاهم خشک نخواهد شد و پای ما را خواهد گاز گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127856" target="_blank">📅 15:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127855">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127855" target="_blank">📅 15:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127854">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEEvyTxIC7TnbRjmMTD2XHGu11EG_RSYkXJ_iam3v2dvrf2zMHCoTOVFRUZSep4Q9aGfG8T5NfOoobcqHjbyglt6PDt_y-7Msu9iMtm7IC01cmQQSpo75jSM99MTlhoW4t1EUJXTZjJ4wg6cEZwSXTJofCWJwoUY6XmNDRdvSCM_wBqdDeLK1rzb6z2CUTA400TqvTPaJcpj6a2WFkL-NJDbqIQUE_QTtdvmx9eSzrIzred_h7xwKjX5eg5QNR1knnzYm3DPb0aZkt6XDUY2IKYDVecWjC8o-j34fBvcaKVXFcn35IElzqUdF_pdR0dDXLQk1I4QTlC3PcHFC33Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید(اکسیوس) : ایران همونطور که گفته بود، حمله به بیروت رو پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/127854" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127853">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرگزاری العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/127853" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127852">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/ منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127852" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127851">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/127851" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127850">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: هدف حمله هوایی در ضاحیه جنوبی، فرمانده ارشد در سیستم ارتباطات حزب‌الله بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127850" target="_blank">📅 14:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8K-NqQWxc_OmrMZatO9JS2HU3wQZSi87CtSB6umTIpJQpq9cs5fz-8YFHkMD999MBhJ97FfUhZKr2UE7511Wj9XBmlAxMMd9EObo9PPZD-9iRl0kTjMtpMPBa1QyWzhnkJTMuwiwiv906NpAYP9hR7nGA5GrCYuxvf4_3w3-4D0RoR7LVIOsbj6MZg2dqbSOIn5S9cNmJtNM9a-YqNcDB2PsYMbEDMaEZAnkr1ygmB_Khap3DSkF0xVI_GvBcQxqZThasgLpLV-V1s-MwzNzy6qD26Epvp9sQKQCr-5Yi9iXTTqiF7h_uBc7vOee-d_0BmutJeEu05LtaLC1NTdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127849" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127848">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بیانیه نتانیاهو و کاتس: ارتش اسرائیل اهدافی متعلق به حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد
🔴
زیرساخت‌های حزب‌الله در ضاحیه جنوبی را با دقت هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127848" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127847">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه های اسرائیلی از اماده باش کامل ارتش اسرائیل برای حمله احتمالی ایران خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127847" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127846">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : ما جشن تولد ترامپ رو امروز تو بیروت جشن گرفتیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127846" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / کانال 12 اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
🔴
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127845" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل ویدیو‌یی از حمله‌ِ به ضاحیه بیروت منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127844" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWT4nW7uf5FLg2408AqQuvLSqD5PdMkDv5wMpK6Cx0mHHMDW_BdFN_W3ZKQWR5QIynRB2S0K_ouQTbizK9mgvOCkmjsmeTWZEf-1G7o5FaE-noe8S1-ezWzEf2zp0t4RrnkQ37VAKEDWZ7m-q5W6YQ_JRT9Ds9FsPxnIPAzpWCyskSbGvRMWiSEXnmwjAiTXIZzqflh4SSdDtBmWJk69nm_9q6Uv1e_YVTbZ1ftpVd9KY8-1YuOuZgX8v8Qt_AITXCoAM25xLJy-l7B3f2y3rBbfDmnqvfpJbe_7eV92_QT_AyKmNy4KnA__20rtFyNYTDKgLgCxSMnCnT1_jtFP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارات وارده به ضاحیه بعد از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127843" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127842" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری: اهمیت این حمله در لبنان این است که ایران قبلاً تهدید کرده بود به هر حمله اسرائیل به بیروت پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127841" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbQWRWWMgsKsEDFyA-T-7smcbewBACDDy_E7gxeexmNz2ko-Cnq6zFvXGOSsOgsKeQbfnpqfWt9sGpcyMPX3kqHfZfIwQPdm-p0l7B4aj0TFQwYQu-LUpd_d5hVGGAIdjkt62WVxAPmro1qL4ikvGVNTzY0mH9TGTjAOIYLoIFzMZH0Fjwd5Azxje0H6QpqUBpIFTOb36W0fVHuBMcjl6UXGWcvzRz9kj47-O1E6-m88NSzwjMvCn5DKIktYzH2B6tdlGiuYgmeBzBtG0GHFRjlH90w2oFgzPsTPyjy98r1FFzalHmQyYGpmbd6bZ8plsDGd5CcX7qqbNUiZplDWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضاحیه بیروت هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127840" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=hED4U0yEVpqPt4g7LOyoXtJSjIigaEIn1JTSojU7JD4p2xELTWTHIuLuCCvSBMLKOUTAE5UMWtmstAxG1S8EWGVOuBhlJVK1-HnzcVpBpyr-ynnLW4RThvXKQhR9x4eKYBp0kCzi3K-1LUTbREiOfj15NlDmWBg0BXzuB75rD2i6rn_f7WgzuJ30wqekhqcG9ITbaWOBlmWyC0T-wjydCRedAxObMNM0E_gWHr3POJyufiiz0bfCQdz4I8aS7iKbf-9-x-LTiUM28gYfskb9A2IQkaNFSULmhAevS3JwYDcK2bWtn5AJIfL5uYhcf_Q3RuhD8coltpmqJMdftI0JTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=hED4U0yEVpqPt4g7LOyoXtJSjIigaEIn1JTSojU7JD4p2xELTWTHIuLuCCvSBMLKOUTAE5UMWtmstAxG1S8EWGVOuBhlJVK1-HnzcVpBpyr-ynnLW4RThvXKQhR9x4eKYBp0kCzi3K-1LUTbREiOfj15NlDmWBg0BXzuB75rD2i6rn_f7WgzuJ30wqekhqcG9ITbaWOBlmWyC0T-wjydCRedAxObMNM0E_gWHr3POJyufiiz0bfCQdz4I8aS7iKbf-9-x-LTiUM28gYfskb9A2IQkaNFSULmhAevS3JwYDcK2bWtn5AJIfL5uYhcf_Q3RuhD8coltpmqJMdftI0JTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از محل حمله اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127839" target="_blank">📅 14:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127838" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW_gkEqCHw9PY5oW-zyS1iZPJ6aRqSfwae9heVEKyoKHS210ZpKj-UQ2jtqWqQvGsVBXNgz6RdSyZ3S3cTlx_WHJYNMvqbvBua3ETUZvl4l4YnS18hUS8rk7ctx3Qq9JAJKQUBI-BKajkbvSJYJtshujA1Xo55pjK3GH6CK0AtQnucM8UDjUT8QeIn5S9ypyHdiip5MyQ7L2XMqsCrDl70UT_3WjHyxkM1ZQKPitGzUN86Fqew5cXmbPL_idXIsgDz1zG0iI3ZlTk5aAaWc_uYw9PVoNwg6aixUTQ3MPGzWnup6RVuAr1lDjc541iLnLHN2EVr8d9I7WxwiQILraXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127837" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=IEs7gE67KIfJX7ckWlYMzitBJv6Bv5odGmVt6gz3oD3yw_Gfq_b6gIWYOA2k0Md0GOkcUSC9ixO_py9edJvsar13atSnrJ32LI_qT1vSEzbTyshyORvFqMHF_N4ijq36DLfdGkuA_ODuVrsg-I4wC0NOMnbJlgWE4owzdRKSkRPWjm2F8vJC4d7t9w5P3dKOlZbtvfPyjA3tDXr9lQ8_T0_PtEytnlToh7w16TR2L1zZBEufbfGvMjCoYdrSV6LIy0IBwovslsgkTan231v0-I6fe8REk_-onIcV7qJHW-cPxjHCfKw41TDkjAUo-FfsuayXz6VHcIrsvJYwp91gTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=IEs7gE67KIfJX7ckWlYMzitBJv6Bv5odGmVt6gz3oD3yw_Gfq_b6gIWYOA2k0Md0GOkcUSC9ixO_py9edJvsar13atSnrJ32LI_qT1vSEzbTyshyORvFqMHF_N4ijq36DLfdGkuA_ODuVrsg-I4wC0NOMnbJlgWE4owzdRKSkRPWjm2F8vJC4d7t9w5P3dKOlZbtvfPyjA3tDXr9lQ8_T0_PtEytnlToh7w16TR2L1zZBEufbfGvMjCoYdrSV6LIy0IBwovslsgkTan231v0-I6fe8REk_-onIcV7qJHW-cPxjHCfKw41TDkjAUo-FfsuayXz6VHcIrsvJYwp91gTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان تو مراسم امین ایران : رسول خدا و اصحابش، تو جنگ رفتن لت و پار شدن و شهید شدن و برگشتن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127836" target="_blank">📅 13:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مقام ارشد ایرانی : طبق پیش‌نویس توافق، آمریکا قراره حدود ۲۵ میلیارد دلار از دارایی‌های بلوکه‌شده ایران رو آزاد کنه؛
🔴
از جمله انتقال مستقیم پول و همکاری در سطح منطقه‌ای
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/127835" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
العربی الجدید : ایران هنوز تأیید نهایی خود را برای یادداشت تفاهم اعلام نکرده است.
🔴
به گفته یک منبع آگاه ایرانی، احتمال امضای توافق در روز یکشنبه منتفی است و بررسی‌ها در داخل ایران ادامه دارد؛ هرچند ممکن است تهران امروز نظر نهایی خود را اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127834" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAWhs_2UQ-W4oXWyMvJzfgJjIRWTC2BN6tVlmyoCKIVqxuHXnte8mA96_irbVwv9kkPcsKMg8HOt4w9efmmi5AbojS9Z3KWWOhIHjcEsU-Yi8fhSpud8mHXJGrQ7FGdTy4E0k4lKQZQCn08wnPluebpARa_pInp56jDpa1nT-nUbcfqlITT7WV9OWQo6lbM6TUemDbaNu5AC575vjl9SEerWzYGeVu340GZs-3oltLR1eOjJDOHPpA8gBdAdeEkE4j9sVWFKI5i3sFwPT3j3suyJrI-V_-DEBb7IWAHLgnwLG6ayz0DXZQ17ByS_zCCeJ3T89_J0Hu7QOyLzFAYbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر فرانسوی «شارل دوگل» پس از پایان دوره مأموریت ادعایی خود در مدیترانه شرقی و دریای عمان، در حال بازگشت به پایگاه نظامی «تولون» در فرانسه است.
🔴
بازگشت ناو «شارل دوگل» به فرانسه، در حالی صورت می‌گیرد که پیش‌تر گمانه‌زنی‌هایی درباره ارتباط این تحرکات نظامی با فرآیندهای دیپلماتیک مطرح شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127833" target="_blank">📅 13:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
👈
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات متحده عربی: ما هرگز طرفدار جنگ نبوده‌ایم و همچنان طرفدار صلح و ثبات خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127832" target="_blank">📅 13:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/127831" target="_blank">📅 13:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127830" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=HoHwqf4GriS-zRk-oQUSN2WY_KNlsdRhVEyvRtgPqM_CBKLQMIHDY-ANwEoEVFM6xw5YfdS7IRmiYQmIipaBPAtUkFi_b-1crY4YjhW8pKrHFDZVmdU3qCVwBpn1HVSuAq0LmI-XtoWiysiLqyS2bX87Fc-3BKFhzKTAQ8Yzcb2vunRdo4pUYVxQ0sI0VdiyJd30r5-MechkhmdXFXYBoYEWBlTCh-frnmvmJ064FJ6CNEtsMiLj04bVAnSFSybpM-epq-fE9aD5bPqxyY0HjZVUAn2HmQ2vNoLfODhJnLFYRamBQE9zTNDikEvb0NGpI_7_NeJQszQaMqpZ8ItygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127829" target="_blank">📅 13:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFbUzisM3rspx6KVrBM9UOfuK4xk21seAarxGKt8j8k4YnC8SVj5De_Vz3JgzzhTGEpXzjnBH5uPmclAaXVc4U_19ejVw5Pmnlv4tP-3lbKa5i-bl6e5g1OH2TllSaRUZLKyrwO5Mf88e_FRw_-XLb0aVODrqFpoihFETRrzLgdlQS35dV57-oQjIMp-9uVW_LrRv4muzTxxdV7FufWNjiE6pneNxBWTpm968S_hna1IW5-4NcVgO7xYU4qVuH2uzVJdxLLAAZuxVZIICnU9CL9jLvyaEzCcHjfs_C2cji7v44btl7Wrxu0SA0bFahL2AzrlG2Fh7lQ1hvj_EykAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXE13sSTfAiOJjBPaPjm22PTLnA3uJ3lRiAf1vlaVPsamcsG7EdiKZfhnkh3CXPz99hQO0xUQeC6invNwKj-e-6J8H53eUbOV48ZcxX0CKW6PZIg5eOxMNg3cY98YwKEVTIEq-vPFaN410X0_798r_52V4d0fPYG4AztNNvukuz4G5O041bWLkgRFdOu1O1JV6ncx1oNYKYUO05CvcYddLJ6WZO9QFhWJR1AMvQ_unqKot8GTjGbx9Cder7ef1f1feKzMFServkMYhFc3uI3tf-zA6AnNzJ5Tyez_CU-DpqPSS6a8Clu-_KbnZGdupvc0khOULh8orKRhPAlsN511Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صندوق سرمایه گذاری قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ ۹۵ به سوئیس زد، ۳میلیون دلار به همراه یه رولز‌ رویس فانتوم آخرین مدل به ارزش ۵۵۰ هزار دلار پاداش خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127827" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شرکت نفت و گاز پارس: چاه جدید فاز ۱۱ پارس جنوبی وارد چرخه تولید پایدار گاز شد
🔴
افزایش تولید از فاز ۱۱، در بالا رفتن سهم برداشت ایران از این میدان عظیم گازی اهمیت ویژه‌ای دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127826" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
جزئیات متن تفاهم ایران و آمریکا از زبان مشاور رئیس تیم مذاکره‌کننده
🔴
مهدی محمدی، مشاور راهبردی رئیس تیم مذاکره‌کننده جزئیاتی از متن یادداشت تفاهم ایران و آمریکا را تشریح کرد که به شرح زیر است:
🔴
۱. توقف درگیری‌ها و تضمین‌های امنیتی
🔴
در گام نخست، توقف کامل عملیات نظامی علیه ایران و لبنان و جلوگیری از هرگونه اقدام نظامی جدید در دستور کار قرار دارد. همچنین طرف آمریکایی باید تضمین‌های لازم را برای جلوگیری از تکرار تنش‌ها ارائه کند.
🔴
۲. آزادسازی دارایی‌ها
🔴
براساس چارچوب مورد بحث، بخشی از دارایی‌های بلوکه‌شده ایران در ابتدای اجرای توافق آزاد خواهد شد و همزمان روند تعلیق برخی محدودیت‌ها و تحریم‌های اقتصادی آغاز می‌شود تا امکان افزایش مبادلات اقتصادی و فروش نفت فراهم شود.
🔴
۳. رفع محدودیت‌های دریایی و تجاری
🔴
یکی از محورهای اصلی توافق، تسهیل تردد کشتی‌های تجاری ایران و کاهش محدودیت‌های دریایی است. هدف این بخش، بازگشت تجارت دریایی ایران به شرایط عادی و رفع موانع موجود در مسیر حمل‌ونقل بین‌المللی عنوان شده است.
🔴
۴. مذاکرات هسته‌ای در مرحله بعد
🔴
در متن مورد مذاکره، مسائل هسته‌ای در مرحلۀ نخست توافق قرار ندارد. براساس این چارچوب، ابتدا باید تعهدات اولیه طرف مقابل اجرا و راستی‌آزمایی شود و سپس گفت‌وگوها درباره موضوعات هسته‌ای وارد مراحل بعدی شود.
🔴
۵. لغو تحریم‌ها و بازسازی خسارت‌ها
🔴
در مرحلۀ نهایی، لغو تحریم‌های اولیه و ثانویه آمریکا و همچنین پیش‌بینی سازوکارهایی برای جبران و بازسازی خسارت‌های ناشی از جنگ و فشارهای اقتصادی مورد توجه قرار گرفته است. این بخش از مهم‌ترین مطالبات ایران در روند مذاکرات به‌شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127825" target="_blank">📅 13:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نیویورک‌ تایمز: تهران معتقد است ایالات متحده آمادگی ورود به یک جنگ گسترده دیگر را ندارد و دونالد ترامپ ترجیح می‌دهد به توافقی برسد که تنش‌ها را کاهش داده و ثبات را به بازارهای انرژی جهانی بازگرداند. این موضوع به ایران فضای بیشتری برای مانور می‌دهد و احساس نیاز آن به دادن امتیازات بزرگ را کاهش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127824" target="_blank">📅 13:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آی۲۴نیوز عبری: امروز ونس و قالیباف طی جلسه مجازی تفاهم نامه را امضا خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127823" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نیویورک تایمز: جنگی که آمریکا و اسرائیل طی ماه‌های گذشته علیه ایران انجام دادند، به اهداف راهبردی اعلام‌شده در آغاز آن دست نیافته و در عوض واقعیت سیاسی و امنیتی جدیدی ایجاد کرده است که ایران را به کشوری مقاوم‌تر و آماده‌تر برای پذیرش ریسک تبدیل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127822" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایوو دالدر، سفیر پیشین آمریکا در ناتو معتقد است که ایالات متحده در شرایطی که تمایلی به ورود به رویارویی مستقیم با روسیه ندارد، به فاصله گرفتن از اروپا ادامه خواهد داد.
🔴
به اعتقاد وی، آمریکا آگاهانه و فعالانه در حال جست‌وجوی راه‌هایی برای ایجاد یک نظام امنیتی مستقل از اروپا است.
🔴
دالدر افزود، ایالات متحده از بیم واکنش احتمالی روسیه، نه تنها استقرار سامانه‌های تسلیحاتی دوربرد و دقیق را در خاک کشورهای اروپایی متوقف کرده، بلکه متحدان اروپایی خود را نیز از تجهیز به چنین سامانه‌هایی بازمی‌دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127821" target="_blank">📅 12:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127820" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7aC0ZM0LJ1JxJzr9rosjrXcNLWjCWY-EH6s_6IvQJfNIFTQ_yBIr7ukKzSz9lTxrBkaOCjXrLlCwg6rLFN5kNAScDvUVLqrq8AzTf5zMCKrvvCdyfk1wGJ82m2S3gYAdgnQ8A4KZHRvhpAryyuvOI_DDcIabwuKg8jj5erACbT2WH_ecBHgrCxSPOPh-k6qEm1EK7uU7t8mQMf7ahsYtezROJxYtFb67-KuhC_7C_TKtbFubGrPFgPKTeXlg72Kn_oJnNtUWcsmWtkD8rLTKTEIaqaezN29XGo28S0BgGaUivOpFLW50dwQkGLASvF7LkLuTjk5r2an0UPnNfngzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مانوک خدابخشیان - تحلیلگر سیاسی چندسال پیش، قبلِ درگذشت :
- اورانیوم رو میدن توافق میشه - بازی تازه شروع میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127819" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال ۱۲ تلویزیون اسرائیل: توافق آمریکا با ایران، اسرائیل را به حاشیه رانده و موضع تهران را تقویت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127818" target="_blank">📅 12:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLoFj9UuVa9lR4pUmuoEHKu-oZQ55fEsL3D-29EwdenQxyIW6xAEV8cir8OeWOvt0Bl529c1prxWtOuDUwoU9K9Y0U59xwsM72BQ1zl7GRTIUtslHyoAQggaCT17NJaTZS1CRVCJtDlJyDnyrfGKNHyZGTaUD88NyY_gj05jGmG7WC_mkh6IxykYJE4_2hHzCKm9zvzVAz87RY2px3UPEWfkBsfEI5-wNM5mwjOOvbghExc5ewQfUdS7iogIHWn01FYQ4xm3mGDTjiwRlje0VthLtpAV2mOyW6Mtc6gJYK8YUEHIJSYwaoFCDa-WD4KDFLeoqss3pGJxJ5ke2n6IQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127817" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یائير لاپید، رهبر اپوزیسیون اسرائیل به روزنامه بریتانیایی تایمز : اسرائیلی‌ها در وضعیتی از یأس و بدبینی غیرقابل تحمل زندگی می‌کنند.
🔴
نگرانی در اسرائیل به دلیل عدم تحقق اهداف اعلام‌شده جنگ حاکم است.
🔴
روابط ما با ایالات متحده به‌شدت آسیب دیده و دولت آینده باید این خسارت را ترمیم کند.
🔴
ما از زمان ۷ اکتبر تاکنون این میزان یأس و بدبینی را در میان اسرائیلی‌ها مشاهده نکرده‌ایم؛ سطح ناامیدی به حدی رسیده که قابل تحمل نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127816" target="_blank">📅 12:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127815" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=g3aZup1pS-JlUib_2IqWmmQrBH2r247vVIf1QCOm5WXIq79QDRyguCFbyJKsFHehni5MtN0OoroIKlosKmyBnBZRfmuW5QKEvc4Z9Bie5jQF5uGSmLdtcZyCwahnjLKuH6hB2BtnjO-ElpPe9wDH49kzL2SI6jqugglaa5lFy4jtEuEivWgxQm1prrp_BC8SQTQtrVQa9B-K7OjIwjVLkADTknUV6_qkhuN0NLwuoYG6S1xDBKI2l062qp-z64qEsTXgvD_wxDQJTzhUpJRFI78WxOU9hKQHoIE3xqUYUK1xfGp6VSYK2zJwKDGYpPq1pZwON1Xt1zhz7TveHb4nUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1101d09a88.mp4?token=g3aZup1pS-JlUib_2IqWmmQrBH2r247vVIf1QCOm5WXIq79QDRyguCFbyJKsFHehni5MtN0OoroIKlosKmyBnBZRfmuW5QKEvc4Z9Bie5jQF5uGSmLdtcZyCwahnjLKuH6hB2BtnjO-ElpPe9wDH49kzL2SI6jqugglaa5lFy4jtEuEivWgxQm1prrp_BC8SQTQtrVQa9B-K7OjIwjVLkADTknUV6_qkhuN0NLwuoYG6S1xDBKI2l062qp-z64qEsTXgvD_wxDQJTzhUpJRFI78WxOU9hKQHoIE3xqUYUK1xfGp6VSYK2zJwKDGYpPq1pZwON1Xt1zhz7TveHb4nUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو پهپاد حزب‌الله امروز صبح به یک منطقه نظامی در شمال اسرائیل نزدیک مرز لبنان حمله کردند، طبق اعلام ارتش اسرائیل.
🔴
ارتش اعلام کرد که در این حادثه هیچ زخمی گزارش نشده است و موضوع همچنان در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127814" target="_blank">📅 12:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
داداستانِ استان اردبیل :  یه تالار تو اردبیل به خاطر برگزاری عروسی مختلط پلمب شد و صاحبش هم بازداشت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127813" target="_blank">📅 12:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عصر ایران: کسانی که با مذاکره مخالف‌اند و از جنگ دفاع می‌کنند حاضرند لباس رزم بپوشند و نه در جنوب لبنان با اسرائیل ، بلکه در همین جنوب ایران خودمان با دشمن بجنگند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127812" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=aA6uhSfofwRre_yB1uSAIOsyyvyPWig-JR0eYqCjcTwnB22zmJf_qqVXNfV8LOUCkypUoH4-sjVCCsff-J8rrCDmje7S0Fe09He-b-AxD_hI5JlpcS1PGcfoZnnsbr9e-eCaO8pLp8hJn5m2VHLcJqo6lc2k7B6hN1LJ7IZ_DOmXw5d1M6qSZE0L9g8qRXpXUBbFP4lSA8pylXdGapTCBxMmLis1DfyMD2DTcYTV9ZThcKAz7PA8jXoaDmNts4mrcOip5rmFP0613K0aABIXf2g8NbR2uUYA9LFOKe8WqMQ2KBvAVFCs-2cnGVfpDKXzCKvAe96HIavLg8KhOKuvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=aA6uhSfofwRre_yB1uSAIOsyyvyPWig-JR0eYqCjcTwnB22zmJf_qqVXNfV8LOUCkypUoH4-sjVCCsff-J8rrCDmje7S0Fe09He-b-AxD_hI5JlpcS1PGcfoZnnsbr9e-eCaO8pLp8hJn5m2VHLcJqo6lc2k7B6hN1LJ7IZ_DOmXw5d1M6qSZE0L9g8qRXpXUBbFP4lSA8pylXdGapTCBxMmLis1DfyMD2DTcYTV9ZThcKAz7PA8jXoaDmNts4mrcOip5rmFP0613K0aABIXf2g8NbR2uUYA9LFOKe8WqMQ2KBvAVFCs-2cnGVfpDKXzCKvAe96HIavLg8KhOKuvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قابل توجه جبهه پایداری
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127811" target="_blank">📅 12:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/letbHIE-wD_x9MX-XP6xgIPXjS-RGgBi1t0TpWZLK3isFZc2ll1_SZIuWs-wU9xKeHi960d-oIU-C3_dpqW5j4kTDzDPfjcw6doXb7KfZM-ha6WbGHwgcHXyYX4aaRyYTwMNAHXDfF0spSfM73IzI5roIlTlMNd4HubocX6FUDiifzCFe6Flnb5kSurydIfx0faHIbs-TrMIoSAtuuZ7v4RPuLLWET_WxS_wdi6sFhSmxjxG-dXAMFVG49h9_rd5VRPbeutnbDb1hzsIE0gjIKaVq2ixdNjgYEd1ai51VSyOaaIpJt4KLCbeQhAJs9UoVO4L0Ut2mslhADWpzn8jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کودتای تندروها علیه مجتبی
‼️
🔴
جلیل محبی: اگر رهبر هم قبول کنه ما قبول نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127810" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=GDiew3CAv97CKkTauN7UUtzh66ZIeGwVlv6vBzCufMjc7FB7ixpQ4mA0RgYB--HCMX7wyapW9AzgmACZk2EB-upOEnyBn1456f0UDo_ElfAcBhfU6dB-3c3FhHVUZepE46uhH7-yaG0WAmzMUV7AFMCy3uWJNO55v2HZepr7arZCeCOxbQrmhUo0bzTZpz3lrXeYYq5pBLbQD_l_JlsFqkjCzsPcPBwCZRvMWOpYkLqmclAAyS_D1MUuPn7ClWiDf7lquDm2I4gxcXNoj6WaaMVpbD12T5r1HJCTsH0EJuidVc3rurNnXHvR0xpSzmvsKmnwuilAeFMVT0dsgKBPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47e6bdbbb.mp4?token=GDiew3CAv97CKkTauN7UUtzh66ZIeGwVlv6vBzCufMjc7FB7ixpQ4mA0RgYB--HCMX7wyapW9AzgmACZk2EB-upOEnyBn1456f0UDo_ElfAcBhfU6dB-3c3FhHVUZepE46uhH7-yaG0WAmzMUV7AFMCy3uWJNO55v2HZepr7arZCeCOxbQrmhUo0bzTZpz3lrXeYYq5pBLbQD_l_JlsFqkjCzsPcPBwCZRvMWOpYkLqmclAAyS_D1MUuPn7ClWiDf7lquDm2I4gxcXNoj6WaaMVpbD12T5r1HJCTsH0EJuidVc3rurNnXHvR0xpSzmvsKmnwuilAeFMVT0dsgKBPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تأسیسات نفتی
روسیه
رو هدف قرار داد
🔴
حملهِ پهپادی به یه مخزن بزرگ نفت، تو یاروسلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127806" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آخرین قیمت دلار: ۱۶۹.۵۲۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127805" target="_blank">📅 12:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نخست وزیر انگلیس کیر استارمر: صبح امروز دستور حمله به یک نفتکش ناوگان سایه روسیه که قصد عبور از تنگه مانش را داشت، صادر کردم
🔴
این عملیات موفقیت‌آمیز ضربه دیگری به روسیه وارد می‌کند و به کسانی که به جنگ اوکراین دامن می‌زنند یادآوری می‌کند که ما اجازه پنهان شدن آنها را نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127804" target="_blank">📅 12:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بلومبرگ: ایران احتمالاً در طول آتش‌بس سلاح‌های پیشرفته روسی را به ذخایر خود اضافه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127803" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=Q0Or3u6rtDU_2Hj8HH5gHfGTGgl4qDwQ914TBcaPjL5SJOGm_HGCpc97FVkWCjfMS6Fn40XyiyYi6H7m1y5sGWEwzMeNDJD8eIpH3gtHUDMgdjjsqimij_DjEMG_Dtdq8ch012sBDxAMPcmZ1OI61T2auo2rF9xjJAIoNwvqFjkNKQWya3T1gCZP4upnWefiR9Sh4HCqVUtvMAJ2RbOpOscCganuBCpKRQiK6lChvTNqtrDxXPqdKEC73At7xuICluyx69UPvnkn6veoI_ThxjOxt6Gn8kqmFVoyJW8aBWWwe6b8eAd3vOl-GTrX5N8F1ExRQVK3wRbeNc5xr1Wp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fd105e87.mp4?token=Q0Or3u6rtDU_2Hj8HH5gHfGTGgl4qDwQ914TBcaPjL5SJOGm_HGCpc97FVkWCjfMS6Fn40XyiyYi6H7m1y5sGWEwzMeNDJD8eIpH3gtHUDMgdjjsqimij_DjEMG_Dtdq8ch012sBDxAMPcmZ1OI61T2auo2rF9xjJAIoNwvqFjkNKQWya3T1gCZP4upnWefiR9Sh4HCqVUtvMAJ2RbOpOscCganuBCpKRQiK6lChvTNqtrDxXPqdKEC73At7xuICluyx69UPvnkn6veoI_ThxjOxt6Gn8kqmFVoyJW8aBWWwe6b8eAd3vOl-GTrX5N8F1ExRQVK3wRbeNc5xr1Wp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترافیک تنگه هرمز نشان دهنده عبور کم تعداد کشتی ها از مسیر جنوبی تنگه مطابق مسیر آمریکا
🔴
نکته قابل توجه گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127802" target="_blank">📅 11:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJx7akTNcoGF5xxuEt9VcH45S30liVM12O29TDwWzXr3lv5y_DY_9_oW9E_X84p5RhXVcWcpCPSYCA2nvEiDZlmaEJXbj65McBUGa8XL4HWfh1P7nCCHe0YSIukHJ8e1rLG0z6Aetbix7QjTI--Bq_mKnB4Ru8yYTd8d2EsRXfOkJrxBvK0WiFVzpfadVvwg3TfJiRzFzd-WnVPqRgQWQ7bp_OIYRfP0I2Fc6ZbP1R-Y4TcJEzzvV48Z3rp983ckAuuIXVKySPpq8cY3TLuqjjftKWB3BnT3VlvP1VGF6j89D7oMS2SAv4sueQiXRVvxgaPkpP0VVT4gRqi6fT06sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ امروز ۸۰ ساله می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127801" target="_blank">📅 11:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQbrhBOl_Ei1ipQ0Wn5ABoK-nkqJYUJ4GuX4Q5cXMMgWE_aEgjty_R6HbL9yPN67kF4p7QmHwHjwFMYjI0HBahooG5eqsvBm6UNIQnLy4h5ARSABLjZ9F0GFgD36d3_wcVmMNslXsC6NCGqXK2hDxri2DpMMVjRHMCIOlILbcVUHGYfopNu9R4JSX2_OxRyu4Xz-aWNr1mXuCq4PLhLzjUtpS7hRkEM1ckmxsHDLOadry4D4YNZXhXqqc__FiVmGGEoUNNvx7vLF64ngNms80hgw0VCpf1i9h-cvoTlY2-z86FyGqboD-NP89hbBXUta2XUiRFFAHXPrBGCCDEs6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایندیپندنت
:
ذخایر نفت آمریکا به پایین‌ترین سطح در بیش از ۴۰ سال اخیر رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127800" target="_blank">📅 11:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مشکل خدمات بانک‌های تجارت و صادرات رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127799" target="_blank">📅 11:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127796">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-Au_zsHe11pq8eMV9FCSd6jZwsgdHhca93pO-uAHeCvRQs7-y4ubW5K5166MLVIMATm9G12ynTOnc4ECOKpvS2cORWmm4h7fmVM3m7EAwUJPzdeRZPuKPMmThTrgKCWOlPEk7tYi4iJYBRhIFP1zmeaQioqYC6o4em-9pryJSWY-I-qAzi-_ppxlLwerVgab7siuSY-1hZxnbBy5oXA0Fn-Z7ghuG1bG_r5fMIIW2wbTbLOv6vk3cGqF_2LaclpyuA8kQBAOaITFhzf8i9l3nZKp-ZVHB4XB74nFZ2HvBmE_5uX3-I4_0tjF-DU2hcnWrmr28pIvPCTYLADselJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTWIVtz-p6FYKE3y4wE890BV3IyLM7NweLmL_9ohLLPtrEdgRpGLtf5Kt-N7o6UvQbKhlXaj9EYXQ8yMl49qgdLGJ0uIG-1xEE13k3YAKUmeoC2s-6zIAMr1voCL7SV0h490FJn3PxB68QuzW-PYlSm9KNvnGD0j0wqzkqomLDehkHC7WtC_a7C60nWfKzz8tcz8ucHBjvWBW4gAVbHT-Bd28jOg1KqZPfYnU1iT5xzYRvNIxmV5Y2gOLNZTK5Iw8AYlHsgMy70ga8Wj0LvVdjqz4St7eqbxgM03EPARnzIRzcZyLRChHKlRSXo0T72vmBUXOW3rn_dXqgBjotvlCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=hQrVC1uoczxu_1DQejPm962_0nnKLFy73OLWZH0m6lR2PzFDgQHdIvY4i8epD4mpABkjeC1bo4cK5-Nr6vbQeI4hkP8nGw8pdAum7DxZq6AZqlxs7IIi7WRsC9OsGnOMrFkWAj7pUZ1RQY1lCLfBT19ylbFUI-ZcocBRR6pLBUdDeRRi7xmvx5v2PI_H5tS8JDmCACURbk7bLLiZXPy02WGNgYw5RZIjMoa9W__PZmPDZ8_Y4fV6AVY46Dc0tKeFNAKXnvV_c7-K8C-1NHx0EB9iMt6Va_Kw2OHh1C9SDW9LIvvIKYAWboxEUDijZGcMjDstIPj3VaBGeSX_-4CIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86af934eb1.mp4?token=hQrVC1uoczxu_1DQejPm962_0nnKLFy73OLWZH0m6lR2PzFDgQHdIvY4i8epD4mpABkjeC1bo4cK5-Nr6vbQeI4hkP8nGw8pdAum7DxZq6AZqlxs7IIi7WRsC9OsGnOMrFkWAj7pUZ1RQY1lCLfBT19ylbFUI-ZcocBRR6pLBUdDeRRi7xmvx5v2PI_H5tS8JDmCACURbk7bLLiZXPy02WGNgYw5RZIjMoa9W__PZmPDZ8_Y4fV6AVY46Dc0tKeFNAKXnvV_c7-K8C-1NHx0EB9iMt6Va_Kw2OHh1C9SDW9LIvvIKYAWboxEUDijZGcMjDstIPj3VaBGeSX_-4CIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ به لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127796" target="_blank">📅 11:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127795">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
منابع العربیه: قالیباف و ‌ ونس توافق صلح ایران و آمریکا را آنلاین امضا می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127795" target="_blank">📅 11:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127794">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه کویت ابراز امیدواری کردند که واشنگتن و تهران به زودی توافق را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127794" target="_blank">📅 11:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
خبرگزاری فارس : جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه، اعلام نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127793" target="_blank">📅 11:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127792">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
توافقی که به‌زودی میان ایالات متحده و ایران امضا خواهد شد را می‌توان در یک کلمه توصیف کرد: بد. و در دو کلمه: بسیار بد. و اسرائیل بهای غرور و کوربینی نتانیاهو را می‌پردازد، و حتی بهای مانورهایی را که او تلاش کرد علیه ترامپ انجام دهد.
🔴
ایران قوی‌تر از قبل بیرون آمده است؛ در مقابل، اسرائیل پس از شوک هفتم اکتبر دستاوردهایی کسب کرده است، اما ضعیف‌تر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127792" target="_blank">📅 11:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127791">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع آگاه: تیم مذاکره‌کننده قطری صبح امروز، به عنوان بخشی از تلاش‌ها برای دستیابی به توافقی برای پایان دادن به جنگ، به تهران سفر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127791" target="_blank">📅 10:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127790">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFkYPCi4ednfA4A4lBBA5XxR7SQ98Cun1HQmkYfCVmZVkbx2dh4Xh_f3SZlBAM3G97ALIWpfBNnYwQdUqv7iIqOspQCtGrxaRg-LPkr4WgRZHZjsDW9_-sgbHR3D_Wvrazt4q7Oe0JAoZ4YyW9k4ISnod-FUrZM3mLMpnYanWB04Ry9GXg4mYsPcCSHO5P3iDu5wrRI6HtmDndsPWrSgy8aV9lxFDIyMLb8bHrCKEkUnmGJgOY0YXDpylYiJt0ltDrF7jjf-J31vGDdju_HFU5tst5gzUVigfsewgHJcOXvjUR998lHhz8uVcgPIOtS_mNywOIMrvFYXXtdh5aNGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس پس از تهدید مسعود پزشکیان به استیضاح: آقای عراقچی غلط کردی دور دوم برای مذاکرات تعیین کردی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127790" target="_blank">📅 10:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127789">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
🔴
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127789" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
العربیه: امروز نشست مجازی میان هیئت‌های آمریکا و ایران برای امضای توافق صلح برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127788" target="_blank">📅 10:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الحدث: پس از امضای توافق، محاصره بنادر ایران برداشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127787" target="_blank">📅 10:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الحدث:یک نشست مجازی میان هیئت‌های آمریکا و ایران با حضور میانجی‌گران پاکستانی و قطری برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127786" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127785">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: به ازای هر حمله‌ از لبنان ۱۰ ساختمان در ضاحیه باید تخریب شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127785" target="_blank">📅 10:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127784">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت دفاع انگلیس اعلام کرد که نیروهای انگلیسی صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127784" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127783">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گروسی :نظارت و راستی‌آزمایی آژانس در هرگونه توافق هسته‌ای احتمالی ایران و آژانس نقش محوری خواهد داشت و این نهاد با هماهنگی شورای حکام برای آن آمادگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127783" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
