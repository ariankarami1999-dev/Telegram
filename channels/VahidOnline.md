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
<img src="https://cdn1.telesco.pe/file/KJ2Xs808TcXWAs_RBnT_zKtIBhatHNpZyLPRCLdNy46hiSc8kI-I93OkgRLl9RcOgP41pFNk77vfr4FEGhKb55MckoDU1uNg2XSVcwomzRX0qAmGYBX_N_CWARHE4b6cwkUonbvvl2SJhViVZUM6vCWf4SRQx3P8CxqC71PTR3zBra49qVb-w_ML6f88mwgzihpnkIfaCQAa2jAklnPvtHdWSQbCHxDdAasWSdE_sGSbtvl5z976JT_NbE1CH0uMew2jtSBk1qNSiqBYV7JTb49Fi8HG1OMh9sNmcRn_YP65UhWnsH-uVtZmhBFLdDQewbJd47b3OkGx2pTqdoCS6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqfnfUNJK-gdAINs9AbEaCxEF4EsA04HxKtPqAGS3p40oib69P1FtX4FQhLRwwlyqxC2Iqljv9oyyp_1dMoy6An_Qc3jBbESKhcZ7NYfOtLxhlLFphcmoM_9uL7yRJJmdJ7LeLYgjNEx8Yiraa8b10qedK70TgmFB4pf4Qicli09iXk_4pDQ6w9dpeio95VMWZdAeKvQkFcrU2X9mJJhZC9vXpNSXuoJAYUhU8VHTu90nLJEto2MU4CIaiMNqvu1ZvblwznNmwgVOZtvhPE7Yx9zkHxgWw6ymuD_QPyxSJuZLu0qsWDxPKHObiu0QGP7TR7voq28NdPn-NBoJFzuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esRLnxSiaYwAS9gsZpKqAcav_BSl711JoNBbE4uNVqcKOh2KnfjYEmpii6Gi7Rd8YmR_nX1bvIUNuMdtp3IFDX3UNONKdtrZ-ar7dE-3iVbtbp_Br0aoIKv0dH2_2zJKVYnQZWaIZUTPLTyoEZ6o9piEXqnumWUQrmCSmHXGxNs2igZC15AgE4W18kXtOAZ8IZdalxeqOz5BPXyNkPTRrLN48E-KzDdno6h7Ei3ko-bgntjuv3On9B4AWNHzWVHKTEhg1cHZAviWpvxJ_an4O2bgfueAAG896FPrWd6Ynzkx9ejUol5TC09RkaRR9E31w2D4eJ7urO0lpQUOj6N2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIw5Bei9PGZ4SjiFJMNBemRO-83iGJuTVHn7us84sDJjr2CzMTORnNAxo24r1oUtaN5oeMOIjMruHSfBl0c3ZbwmIvSri7O-OGq_EsvHVe1IRUif4ayuI1PuFtb86f3gF2K-KUwrMf6gSZnYQrYLjFbrfaW4-7yFdctvvmX6zjLh6g-jxn1pwoKk4amPSy8a7eCCpjWExrzDqyQtdM5UNbJFqMCwpJVv2wu5tQLuL-t87Z4gkVWikB5N3yMtG2PuQ2JuyE0Tkop2wJ5N09JKbb7XuYAfR6SG6SCJxrSumpfvYtzO72CTPPmCYFOX-TA5fhGAyomNQlyXDkLCo9f5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frd8pBLfem0FI5iHVupHvNUdl6dYRFJCNgNsZBqe3xiw388HW6zeLj9vPRSp1yMPYTh95o9k-zFZAXA-uY1QB3ndj2KDlDVGqTbXoI6PpbwXGHnpw1kqdOdtlwdeGp08GCucEWuLf6K9tqXg_-S369iavXTNm0oJ4iGdTbsXQy24LKKen6qlBdEMvsL-B9c-xy_x_G5BvI306giEAKnu5vRXfQ-6TMddHApt9es5k0JNAnW6M2oXpHcKW1yr7U89OG0u5tuYhdf-QS5CcEowLDjtmW6pH3Ie09V6aTK47zCvis9O_pV6IkbmrJ0BTBVZpq8vqYKFvirLoC4rjmbTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3uaUPUPSz54dEcjN0p35iTImJ_aImXXwLp_woHJWyUts7ZknRyInzhcPr-Tp9URkqecVaE0ctnJZJHDYSQcOBknxz79U3f2YKgc-NHFR6WRxu7noAUj2bIyzgpM4Nn67St--U0q13rnxZTR-LOi8BNpalznZbzZfya47Zesgz2gb1dbZsTuzn91Pcn1m2bzH8ymQ8XiU0cHJD4Yb4qK3e9S25lb9waGvmRKlFrFsD-KEyUSU5BIKfJV1uY43uvUXnj7Inwc4Oaxz9s87NIqfvma-SUFlCHLi2L40S03m7FBS9RL6OeldaPS7_4DnWKWZaIM47F1oXxMWsRiDGwDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfFafcSTSwDm9ADfnKZaCNxX_qHETmxeDu_jl8c0O5-OSmXxdV_ZEf-DnC6na0zukhQZsBf55yjfEpMGu3A6PL_cJaimBQFfPV7Ie131XlpwrS_3VWIL2c14kVWMcUc5-cADgOf1S10GubLFHVdhD-o1HP3dmn8uK3L6cjsi7sZ-mPFrnjq2ie7Ql_1aQS3YhEmc6xMm0hjOL6uXz31FznlC7OZW9ToXhuy8tjN5iZq_muBjRB-ZPoXbyn3shrHy6MhERWhv0_OMJLvSYK2uHfgF8hYjL34C5-eKuTZabxx-Zg-60CQ1SPh5DUuFJ5a8s9MdA7Qxr8IYekYwQcOhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyZWpGdGA1HAIg2Sy5R0aI3jHb7sh-BYRCDZQYQl6ued2VfRGCvrF7AoNWI7FpTnowrs0DskXY4HMEXDCoyrp1y_-sP9dazQdwLyKLbMHGmVLzg2mNXgXSs3EcSaZ0YA82FNO5Mj2wwbKfkRNOB7l6QJ6K7-JBBEIRie3kmp9XiLUdQ3IrSsWx7TKQbSAmSdpwfP92AYDiPvR6LLno5F4fhCEqbgWr0KMQaNKIjVyJQTP6M7xNXr5Xx_fW0EX2G1f92M6hogfeVcaDiJ4OEJYx8ATGCN9tP_UsxLJf4W9ARliQguxxfeSlHj-1pPN8vh2yw52jp_fSxICV1rzOhtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNt4Hx3e0o3iFxPQRLw-htpad2rmiUUiXRSLIUzr_8vJo7h5qF8muw0b0eB-FvAYQB9W-CB_32MVRT-Q2aFj47wekPw6oiYvGq0Xk-XOCo8UvmOahlOb_KZbeISUUp3OEoiRhPItKDBtYlktlDV4qRnwkkO5VOj_w2lFt-yyvQtZJr5fsUj_-nA_ck4GYUA5djoDclwJfnAQjafv8pVT_JeKR_ywaAKrWTJK7FVXhGDNZ79VHDsP_HmfDD5RzIkCDu8eY-RRQkvXoNfvI9Exm9sECbc_bH9IPbJvIwXASmFj7w-4MSRgofXsO25eyrfWcxDAe2YE_gMbowxKJw3ngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzPuBkrKi5-Ct4vqdOis8HSlJFPG0rNpmYJ3ONn0F-gB8RrtWJGOLda5X1tdYzdQIsW4BRj5Tqyg3-m9xiKHssVZ8f43MI-_kLddQEumXl-BoiV1SploFmbfdx6cCM0l__eOZkPIIS8cLCDyWkDhhbtxnhkSQgOVT0nVvMSnXuFflFa_4lW_8_3p_sMjnExDDmwV6KmGTJXC1CBY_obPslW2acq0duAozu3pUnuPleRkMA4yeE4R1fsh3E1DV4AvPyRq9zzatzfn_cTUIDTtH6N8jeg67KxroyMvpUIjci5_gg64XTq9Dye_3xOzbQxHiXSZeyBvtghtckPCnp4IyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=dXfL0II7x7DRW9qLloSmcfoq46tFuLrA065vMPp_jfyCYdLCaxSMRqAhxt5qGmTdyNrkvrnHGbsQihGljr7VAQ2E938uZao_qJuXxJLCxGLWbleqKclNEmkvw8NF75DhaBJaxVi3YPkNjWjmPsKCRMX2uO0CUd8UUt6M1ekCgQoVIJoTSc4G1FCsqcKO6utG8VqkLygJDZQ9MO9fDznTf-g_N-wmIrWmyUL_e6hn8IoVd_GT_14N9Fl140SELLNFVQBWbjQRX7RuKvOA6pcpJ-TABaD8aeZu3W6D3B117EJ83dyCdMXlu_tnTy_tQ9lyb59nETT-WyuLWV0_1RH-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=dXfL0II7x7DRW9qLloSmcfoq46tFuLrA065vMPp_jfyCYdLCaxSMRqAhxt5qGmTdyNrkvrnHGbsQihGljr7VAQ2E938uZao_qJuXxJLCxGLWbleqKclNEmkvw8NF75DhaBJaxVi3YPkNjWjmPsKCRMX2uO0CUd8UUt6M1ekCgQoVIJoTSc4G1FCsqcKO6utG8VqkLygJDZQ9MO9fDznTf-g_N-wmIrWmyUL_e6hn8IoVd_GT_14N9Fl140SELLNFVQBWbjQRX7RuKvOA6pcpJ-TABaD8aeZu3W6D3B117EJ83dyCdMXlu_tnTy_tQ9lyb59nETT-WyuLWV0_1RH-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1jYFw5lvUADfCXXo5A7q2rXoXlm-amrJwx5GZjOEjc-JaGoLqm35jDHcb_vqhCaHfBIHmjDnKu9uPR1ZC1wLv-bzkAi-VQNqHIdw4hNbpTH3rOfF2B9tCA9GaRXFmawJAF0NlYwQE3K_n_Do4XKnVGuKS4lzx99XWgTy-D9Ar8wSpAM-gKpr6K1ssWld7MYIddJKUeW61lMwKRe6jVlDs5eFDAdRt-bzIwtGz-BLgId8PKprigPrjf98-bpapeFsaXz5-xGOuVbCfdBpQkOYdaOVO2uBjCCsIq885DSfSr1p_-4VgVwLHP8j5NxVHeIoFxrlKW4jOwvTsVNEQYgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=rq42MmofOyufwHyhTVsUFuFZXkmXV2Se60trhUplFbysQu2OwdMys0RTdf2WZmGf3d8GmlSnZmHKs0jm82Q2VYAXHQnPHIA5W9dRsFJMe30WD-ZvNrFqh52Zms_MjKDzRXsU3BO9-AczbaM3gjP7G3oZwu1JZ12Y90v7s7z_EURSL2W0NUKSPV-u_jyM9_hcmiqCV44MwA1OJRzXTZFy9nk-S2NWvopWS5wZQEqJXkd_2oJV6WfUFN7HIFWhjk2OGjCsCdYEajsKgQFCysYMxur9GPGFgBKjJhRGJcEutgm5PQNnJSHqt9gN_1wha4F8uoOgZObPlVDISGQV1wK8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=rq42MmofOyufwHyhTVsUFuFZXkmXV2Se60trhUplFbysQu2OwdMys0RTdf2WZmGf3d8GmlSnZmHKs0jm82Q2VYAXHQnPHIA5W9dRsFJMe30WD-ZvNrFqh52Zms_MjKDzRXsU3BO9-AczbaM3gjP7G3oZwu1JZ12Y90v7s7z_EURSL2W0NUKSPV-u_jyM9_hcmiqCV44MwA1OJRzXTZFy9nk-S2NWvopWS5wZQEqJXkd_2oJV6WfUFN7HIFWhjk2OGjCsCdYEajsKgQFCysYMxur9GPGFgBKjJhRGJcEutgm5PQNnJSHqt9gN_1wha4F8uoOgZObPlVDISGQV1wK8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبران دو اقتصاد بزرگ جهان روز پنج‌شنبه، دوم مهر، در کاخ سفید دیدار و دربارهٔ موضوعاتی از تجارت و تعرفه‌ها گرفته تا تایوان، هوش مصنوعی و جنگ ایران گفت‌وگو کردند.
در این دیدار که در کاخ سفید برگزار شد، شی جین‌پینگ از ایران و آمریکا خواست که در اسرع وقت مشکلاتشان را با گفت‌وگو حل‌وفصل کنند. رئیس‌جمهور چین همزمان از میزبان آمریکایی‌اش خواست که به‌سرعت و از طریق مذاکره، جنگ با ایران را پایان دهد.
رویترز به‌نقل از منابع آگاه گزارش کرده بود که چین در گفت‌وگوهای پیش از سفر شی جین‌پینگ، در مقابل امتیاز احتمالی آمریکا در زمینهٔ فروش تسلیحات به تایوان، پیشنهاد همکاری در اعمال فشار بر ایران را مطرح کرده است. این پیشنهاد به‌طور رسمی از سوی پکن تأیید نشده است.
تایوان از دیگر موضوعات حساس دیدار روز پنج‌شنبه بود. چین این جزیرهٔ دارای حکومت دموکراتیک را بخشی از قلمرو خود می‌داند و بارها با فروش تسلیحات آمریکا به تایوان مخالفت کرده است.
به گزارش خبرگزاری رسمی چین، شین‌هوا، آقای شی در کاخ سفید از دونالد ترامپ خواست که در قبال موضوع «استقلال» تایوان، با «دوراندیشی و احتیاط» رفتار کند.
این دومین دیدار ترامپ و شی در سال جاری میلادی و نخستین سفر رئیس‌جمهور چین به واشینگتن در بیش از یک دهه است.
شی جین‌پینگ عصر چهارشنبه به‌وقت محلی وارد آمریکا شد و دونالد ترامپ در پای هواپیمای او در پایگاه اندروز از وی استقبال کرد.
این نخستین بار در ۱۱ سال گذشته است که یک رئیس‌جمهور آمریکا برای استقبال از یک رهبر خارجی به این پایگاه می‌رود. آخرین بار باراک اوباما در سال ۲۰۱۵ در آن‌جا از پاپ فرانسیس استقبال کرده بود. موضوعی که نشانه‌ای از احترام ویژۀ دونالد ترامپ به همتای چینی‌اش به‌شمار می‌رود.
کاخ سفید همچنین برای پنجشنبه‌شب ضیافت رسمی شامی ترتیب داده که شماری از مدیران شرکت‌های بزرگ فناوری آمریکا از جمله اپل، آمازون، آلفابت، اوپن‌ای‌آی، تسلا و انویدیا به آن دعوت شده‌اند.
شی جین‌پینگ چهارشنبه‌شب در بدو ورود به آمریکا ابراز امیدواری کرد روابط پکن و واشینگتن باثبات‌تر شود و گفت دو کشور باید «شریک باشند، نه رقیب».
پیش از دیدار دو رئیس‌جمهور، مقام‌های ارشد اقتصادی دو کشور بر سر تمدید آتش‌بس تجاری به توافق رسیده‌ بودند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از گفت‌وگو با هه لی‌فنگ، معاون نخست‌وزیر چین، اعلام کرد توافقی که افزایش شدید تعرفه‌های متقابل را متوقف کرده بود، تا ۱۰ ژانویه تمدید خواهد شد. آتش‌بس تجاری فعلی قرار بود در ماه نوامبر به پایان برسد.
در جریان جنگ تجاری دو کشور، تعرفه‌های متقابل در مقطعی از ۱۰۰ درصد نیز فراتر رفته بود.
مقام‌های آمریکایی همچنین از احتمال اعلام توافق‌هایی در زمینهٔ کشاورزی و موانع غیرتعرفه‌ای خبر داده‌اند. آمریکا می‌گوید چین در اجرای تعهد خود برای خرید ۲۰۰ فروند هواپیمای بوئینگ نیز پیشرفت‌هایی داشته، هرچند هنوز سفارش تازه‌ای اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=NdQX9YLb9jIqluF4Ler3HD_GE43t1zz1xwD_hkHuG6Rs0fRUJ-Ln1Ya5mf4--VKlu1pnfNKKWR-S8eYcMqC_E5YqbmwRC2pqGGqLAWKZGyZ3chsHCnMR8JZXbHgD5ip7YL8Dj2NplDAdrGbs3o4W1_xedjLAqJFSATYzZQoUT3m8lD_TfYNBKr1l3-cWGTsgsm01b_h8oa7RsXRqjKZ-wBEmPsJQy_NnYMpHSYaOf75M5AsjKw-4D-KU1Qjw4TlS6NmjPr906Ub6dBo0-Xipz0jvufJxG7J8TiEar9GiRJD1kLait5TAc41elK9rjZecFJMMjVeRQ3Whr1uOmEPP7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=NdQX9YLb9jIqluF4Ler3HD_GE43t1zz1xwD_hkHuG6Rs0fRUJ-Ln1Ya5mf4--VKlu1pnfNKKWR-S8eYcMqC_E5YqbmwRC2pqGGqLAWKZGyZ3chsHCnMR8JZXbHgD5ip7YL8Dj2NplDAdrGbs3o4W1_xedjLAqJFSATYzZQoUT3m8lD_TfYNBKr1l3-cWGTsgsm01b_h8oa7RsXRqjKZ-wBEmPsJQy_NnYMpHSYaOf75M5AsjKw-4D-KU1Qjw4TlS6NmjPr906Ub6dBo0-Xipz0jvufJxG7J8TiEar9GiRJD1kLait5TAc41elK9rjZecFJMMjVeRQ3Whr1uOmEPP7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=lFo2QN1cRUk2NGk18IuM1qUVXo9f9jol5v1ovqqnVFLDM-0ao7hRNj4VzfaWyQvNLxuE4ZZ6CHAndyOjAExOAWYrNBbX68YWuz4a6NWMGDIhSE3AcZmOVtPLi0baTWznYmUYyp6kB9A-GDZxa912LyN0CWDU7sRgMPPW1miQvRxy3qeBlFR5DEXxHBaLTMi1d--z0hzqK7qhZkHZXHe77lQrzxFpbUSepH3arBm0qiTb_9pi5da4J4Y815V4bg6RQfj7y9C6De__f4ucfb9UbyJDh5VjkBEr8L5z5AV5hlXOvevIcFSBJtLgcu5RyaJv1BgzRR4l7RJlepqMz7S6maT0yGQnJ5oXjR2Aj_UbMMFG-1Jhfe1G47x8nN8zAQ8vgUEj_ADnSG44NkkE2sCj3gqXS66HhL4oJsy_kuU4UrXEjsO-soTl_AogL15tZzJXgkRo8hdWdlavz9h_5OQvcp8-UNkEnrVu6ZHiIy5Gvoy32C1cRZem4J2Oe9m-Iyz1XKdpxohYVLKAzqn77JY2ecnd8KuppWsO6EPuQUpBcGwag1ptcuGXRffplYpJzBcYsvUw-uM0ACnIChJ5dp-fQeMkRaCIAVMdi2dAAeDGTG6CR9dMEM03ynZ5kaErTkElJXWDpx8DK3xjd-m-U7LEQ8mh8IHwti5w7tUVg7bhJP8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=lFo2QN1cRUk2NGk18IuM1qUVXo9f9jol5v1ovqqnVFLDM-0ao7hRNj4VzfaWyQvNLxuE4ZZ6CHAndyOjAExOAWYrNBbX68YWuz4a6NWMGDIhSE3AcZmOVtPLi0baTWznYmUYyp6kB9A-GDZxa912LyN0CWDU7sRgMPPW1miQvRxy3qeBlFR5DEXxHBaLTMi1d--z0hzqK7qhZkHZXHe77lQrzxFpbUSepH3arBm0qiTb_9pi5da4J4Y815V4bg6RQfj7y9C6De__f4ucfb9UbyJDh5VjkBEr8L5z5AV5hlXOvevIcFSBJtLgcu5RyaJv1BgzRR4l7RJlepqMz7S6maT0yGQnJ5oXjR2Aj_UbMMFG-1Jhfe1G47x8nN8zAQ8vgUEj_ADnSG44NkkE2sCj3gqXS66HhL4oJsy_kuU4UrXEjsO-soTl_AogL15tZzJXgkRo8hdWdlavz9h_5OQvcp8-UNkEnrVu6ZHiIy5Gvoy32C1cRZem4J2Oe9m-Iyz1XKdpxohYVLKAzqn77JY2ecnd8KuppWsO6EPuQUpBcGwag1ptcuGXRffplYpJzBcYsvUw-uM0ACnIChJ5dp-fQeMkRaCIAVMdi2dAAeDGTG6CR9dMEM03ynZ5kaErTkElJXWDpx8DK3xjd-m-U7LEQ8mh8IHwti5w7tUVg7bhJP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی قلهکی، از منابع "نزدیک به حکومت"، با انتشار این ویدیو نوشته:
'''
اختصاصی: «تاجیکستان» و «جمهوری آذربایجان» آسمان خود را بر روی پروازهای «ایران» بستند
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه» _پایتخت تاجیکستان_ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🔻
پی‌نوشت: مسیر پرواز هواپیمایی وارش از سمتِ ایرانوبه مقصد «دوشنبه» _پایتخت تاجیکستان_، ورود به آسمان جمهوری آذربایجان و ترکمنستان بود که پیش‌تر آذربایجان و ترکمنستان آسمان خود را بر روی پروازهای ایرانی بستند و پرواز نتوانست وارد آسمان این دو کشور شود و بالاجبار به کشور بازگشت.
'''
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JepQtAzKkJijA_iPwYXbzftUr8VVPJyFIKaqHvC5eXFwvSDEXoW_Qv02Jev6T7qUt9KChbLIzqNf_p645lUtCpZehNsBXzA6HP-w6ivojB1bznbhBHIYypiBXF7oO7V3Qk5ojERzg2VK1AiDlS-zCm3fYhnxHD5WOJiQEM50i2nJXn-LO0ElldjK6RDb33ft7n3O-ybjQYBrSoBxlV-nCOHpltYNQpJGL00l5XIZntQpt-GfcwmkIHiB4GcHqEw8AZlQD-Mlid7SGdWLIiltR8qfA8bDaFgEAh_gUxtuCu-RoIGCnZDbD4Roqb3TRUifD6qFoUJ6VEaGg3eCwfawvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvA6Tzq8hiVo695JHR7h0OhdQRn6gvASA7USc91aR4_yoB6GN6sUlisYir5T3gn3PD8M4pRpmdmG8KlpF4GfRQ1bSoZhhDVmadU-lSQFCLNAj-Bq7HArpnFn1U6Bur4rE6J5eLVDjLVj90mL8k3gSdvzyHnkN9M7d9Er-uMYrsxZ5ym7eKzkAE8tGhX2tmm_SaT6CYBC_V0GDcTWwN86ogj9nJpisnnA5AHwDpwaCY5Gmsgirz6I32G-t3yvt-E9qDQI_eInL1Pki9-_NAsFY4Q-VtSXbv8YJHH_tyUSDUVkz6fLJWjt5Sss2BfpUVDQqk5ZXLHYVaL3bgeC_ZL_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bERXGsiByqmZfOce8nY69NTQosQLDtyeMUQeSiFUby51oG3BGAaygyEzy4R49hmpYU5lkzARwAEkGpAgYdN5ibyIqp9mfu_hN9ExtNyXm1MNhIiNhSyWoKnJYXQ-_DcLfDl6SLA9gYCGkqrVBlJs3Z7Bw2CEWT1ar9THDlLRrFdrDJiiKXF2AA3EP6L3qG9Ola9srY4Bc2b_WmXo1rNlUK59BYpyZq-epP62WEymQ2XlDGAcqAUovvSl0-r3pee-EcqnKVzpg33Liowyw-s4SS30VUro6Ld4lH882gLRRzcg8N840ealIEVEn5ds8ue9rMDho0k4P5ivXheXsu11Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdDuHCMN8w_LHYLbsLYFWWDUMM60iRBvBljfjfdKSw91u5fwnKlhn84symKVYI2gD1TPdree305teZSxCN7czsYbDOZTBOJp1AAlCaYGtzlck2Hu9PFStAr-tv9wUTmJuo7Vzh77p4pcQFYRUmh4Sl-YfpghKfZ8SBhkoqDOBZ0UpYsx6tbCAwtcqGuvM2-PkqIZ3MoyHzuDrspkvGjZ_D6-NYUiv2kmDIQ-x524Yl30d-8sTxZa_UuIJvrdkBd8ssXOxAfkZ0EJakTLe3vrr8h2PloKZ58lW3IUPOWrZe-yQPN8Y1n1pK1PUSVKBsl0jm6J9-G4pUxhW1b3feGg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPpMnMVV7JVscVd9upv1D8A8tao7qpjaEAqfoYjHQ2T6n5BJiPrBtWOmOg2nv75uXwzo-krF6xIP8nDUPrNhQTXgkpOGcsZMmrYSumRrIMBYSbss5OXp-glihlz312s3vjmuO9NV6V-6e4opOEAeDmCvwk7PtNjRzeKLnLodpSKuuA2Fn3jbeoWyTr6BwHqdZ6X_LA-h-647Up32qtQRh_uaA4iOYhqnGUrYfk6tF-OTSKAo2hYISQS8tLPDveyO4EOkJX3f8rOv5kKbER3HsLZAfzagwlmH91Yv1rRvWiM4g_fsrt68Beh99qFXvWK-u8yR0gyhfmQ0ME78fqeahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqgpLHb_lH7lRjsRlfFpMQjWRT9qqVvFYEeQf4o1bqcIs8X0ALwVhgg3XRI1Xjd91lUz-XclrxBVin-RLwrLuqGwYT5IdLlrsp968YcQG1zj-5p3BfVQBaiZPt5uR1Rd22xkMqgaJOK8fZXqdA-AYNz2mTmne36hegFux3tnR1lYSzxrT4JGB6NDKSM-gWIUxX3RVVfgfLOeEr-Se72xSsl0pI2RAzM7Z-KPKsJkSUB4GUdzwbes1LV3h3LzdV2dDI5jfzlXQhh82WSg1ROm9J6bTd1q7dG4V_YilLFq-3DwlT969XTYw1z06PUqeGIsVAsByt0_3uP9MxKL8zef0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NycarhnowpGF3ovycV-NAruetzQA5LzA05IofKfvFvxng-vMQ5NamRE-jdnrkEWgeOpuLZMf4QGmlllXVeshhkkft4V_BsEKNW9yw6LBOK0GNI6UYdu89K30axxL-6XWdnga-VfpNttqrTREopKfAwr5VOMb1E1cO1-VW3J-VBFwXnneSsln43siG5GYj62Du5o8OHxTbfAZyFZ_tUfY7QzeqDo3Bvq6gbQC72iEQh9gAz1eG2ugauhsnlmIw4mmTDllE-IZzhORGnsIsk2v_juSMQdfL6wUnMBgrP5FevQDPAwsg26eDxpZOFa6d6Zwx-IoLCmTLPGucHKBp6yZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=kw7vWBK6UJZibN8oAdj_kVVI7oJ-l006OV3t6P48ce7io7F1xvajcyvgA3-FniU2cZNoHng8gYs2PO7WHnwpBJaUXPpClWDCMvjkRfHCcqREs8fiqECKM9l6DIM4h-L9hFc1-pfBI2S35eZvTqfaL3U3sxH0ylVNeVM_H6-Go4k__0XKFwRPoxYYKsi2kdTrttykgv9eqFnLyArkP2Wt4UeY5T6c5_4uB0iel6k53VU-Zap-ebYmb7F115aVRE_fYy3KfAn7B8V0ZCR1KwOgC9Gp52qQtCgR9U1iNL8PzpNOypny3amw_HbESN3zNKp3NKgQCIPgyjWEPSr9_yOm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=kw7vWBK6UJZibN8oAdj_kVVI7oJ-l006OV3t6P48ce7io7F1xvajcyvgA3-FniU2cZNoHng8gYs2PO7WHnwpBJaUXPpClWDCMvjkRfHCcqREs8fiqECKM9l6DIM4h-L9hFc1-pfBI2S35eZvTqfaL3U3sxH0ylVNeVM_H6-Go4k__0XKFwRPoxYYKsi2kdTrttykgv9eqFnLyArkP2Wt4UeY5T6c5_4uB0iel6k53VU-Zap-ebYmb7F115aVRE_fYy3KfAn7B8V0ZCR1KwOgC9Gp52qQtCgR9U1iNL8PzpNOypny3amw_HbESN3zNKp3NKgQCIPgyjWEPSr9_yOm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nCtgQFLDKB_x2CjwGHGt35R9iomdndF56FVdh0Z-jcRBbjTFYYyJMqSWB0FHBXlT3kHO6MopAqV_z6QlxJ1HeGdKQcOoDr4nuVj4SqoOhvVZ-b6a9Dn1TQ-Lbh7GwRImiuVTmDjvVEOzKndIyLZmW3C8-0_48GC79NbcfSt2chMVaZfzKIRM6CSiLdY4TMXJg6tCEMUbUkTxnccPe5YyDvn-4m9pb7GLfmQPXA8UkK8T-fbdsd4pl-hVI7ttuvJAR7BqOA3-CsbIOh_Sa9p5yEqHbkpkOe9AW8uFQU3AZxeFqU0XeyuspS8hjU4ifStG63fypqNEQxlFQom7ps1ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=SiyomCNAhw5appE0xCkjqazC13yeny_9B5AgtaixqbWbbp3UCzyEik7tqFdo1mfiuJZBsSNF8qz59v8_KFV6aPvJYrZ_pxmjR7iy6Jj4p8U03VQMH9HJoNmwPL5PoE_Mbg0BkhrvraDMz5U02Mg5eZhdOdnvgKXoMIJ6dvDTaEIFF3GLpUXy2YB_G7kVxYCizr372tilt7_dskKRfsdtmMmGmdSag69AoBrpCjyE3c729dFESXxH7Y0rff1NCWeP72gygQOY8_Ij9oOAl0HrZNrh-z9trpiZfllhS_iIfw9pdf00K86--YAas-DsN10TLhiXdgpuivM2yJ5lqX9LiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=SiyomCNAhw5appE0xCkjqazC13yeny_9B5AgtaixqbWbbp3UCzyEik7tqFdo1mfiuJZBsSNF8qz59v8_KFV6aPvJYrZ_pxmjR7iy6Jj4p8U03VQMH9HJoNmwPL5PoE_Mbg0BkhrvraDMz5U02Mg5eZhdOdnvgKXoMIJ6dvDTaEIFF3GLpUXy2YB_G7kVxYCizr372tilt7_dskKRfsdtmMmGmdSag69AoBrpCjyE3c729dFESXxH7Y0rff1NCWeP72gygQOY8_Ij9oOAl0HrZNrh-z9trpiZfllhS_iIfw9pdf00K86--YAas-DsN10TLhiXdgpuivM2yJ5lqX9LiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=Yh18KxeuFChQKzCitWnNsGbBVx0AGLU7YBc1Xc_fLKyRCQpCgc7BUEzclkjJyJd-Tf9V65t7DVwlj9aqUNaz6nVPvQcdjkffSkOfCUtvO09SP0a7nq8TlhboTlquy4yKB_sJlha2Y3mSjRtcXe92WDtmkJqEWN2GwTcUWtUAbd0C_j2snDXiYNyzM7d5cPbM4cIo67GZHGzEZsPcFNYiX6AtQQQfca5GTTDVwnLFkxZ8PX23xuwAOvfK_mrAWfC80cyITfMiuITwbNSTZDTdLmdGu9RsMItQPfpuPlJcp3bfl-YqX2VozLs3ILf1ohm7kRgHNejN28p74NaHvuC-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=Yh18KxeuFChQKzCitWnNsGbBVx0AGLU7YBc1Xc_fLKyRCQpCgc7BUEzclkjJyJd-Tf9V65t7DVwlj9aqUNaz6nVPvQcdjkffSkOfCUtvO09SP0a7nq8TlhboTlquy4yKB_sJlha2Y3mSjRtcXe92WDtmkJqEWN2GwTcUWtUAbd0C_j2snDXiYNyzM7d5cPbM4cIo67GZHGzEZsPcFNYiX6AtQQQfca5GTTDVwnLFkxZ8PX23xuwAOvfK_mrAWfC80cyITfMiuITwbNSTZDTdLmdGu9RsMItQPfpuPlJcp3bfl-YqX2VozLs3ILf1ohm7kRgHNejN28p74NaHvuC-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzKIqebUKSNVBf5eBfJSkrUdnMjLRMwdRGfjGOdVMyStKPtorctAP094N-gTEdweuDEHKaFOlfL5mJ_aYhf5Mto1GSn87lcggJV1gaqBJBRsMIUBXqpyZIyOLEJsWYKhgp484eL9AdhpQA56y4m6aQyaGaG0mnj9D4mFvg7vxE1Jdln7m80ba1hDdYp9nSqyfSmN1RsmS0gXiDEY7wy5xVEHPL0Q4a2iTPibLhgmyuOVA5sz2OGS7CpEd9EMhs_kVw0kQOqD8aDmDD-05dRojp0KpgZVJ8s1k0iN2JMH0k8zNWgBh8ZDLmnnuYvPv2ikNKu35QvD97rdF2-jLZr9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=JBLLyAKhJb0nu3WLN2rcJQQeB6omd64edAOKqPBuAGWFEz-wxmjdEMbb4hW5s_gSh21uokVo_hdy56TemYONHj6hB3k-ZSXlroNQrtP4OSNMuAhggYVhhnRceI7QxOBYuMsfq5jQN8D8r09_UTNQZaUDli9H6JtX3Ju4-LTKvod5PXM3V1ogPVb50va1sahky8fz-hpUlGRCVuUVW61Tlpi36ee099uJJQC9xByTiRxHqoiHksWc3Qd59aMmu07dmLI6zPftKgSu59N8s8N4qvNf-bPo7fUEcQFpsx4WeQnDvu2Ftz1FVWVWmGd-aTmlmu5oLJ8pFwHqqyuPqm6NSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=JBLLyAKhJb0nu3WLN2rcJQQeB6omd64edAOKqPBuAGWFEz-wxmjdEMbb4hW5s_gSh21uokVo_hdy56TemYONHj6hB3k-ZSXlroNQrtP4OSNMuAhggYVhhnRceI7QxOBYuMsfq5jQN8D8r09_UTNQZaUDli9H6JtX3Ju4-LTKvod5PXM3V1ogPVb50va1sahky8fz-hpUlGRCVuUVW61Tlpi36ee099uJJQC9xByTiRxHqoiHksWc3Qd59aMmu07dmLI6zPftKgSu59N8s8N4qvNf-bPo7fUEcQFpsx4WeQnDvu2Ftz1FVWVWmGd-aTmlmu5oLJ8pFwHqqyuPqm6NSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxyQfxFPKXWxk16f2H4w3D6BYTJuVxjRe_fK9pv732tAAzafuz1xQhwh8jMeREflCrT3K5mVPa-XVq5OVU3kWHWnMTTIIWKulRNakVHURC2kMcg-h3AOaCJhBm2HfPY1oiYsso_b7Xk1Iyy5KHmTwnbeFn0jMzFwwxVNWb0r6Zy0Iwg0SW7CItI5Q9Rl8wiU2etgqOaWulZm0n3trbw9PvCTVjPeXV-BATeA3oW2V2b5_EW6SmUAgcGiOsSDtEEud1yYtgFDDuMfnky0Xl22J40F0oVO_khbUgX1PUHQnNlYc-TbCrxMEZGITdj2xwLBVeOCiud2lm3VFMVoqDXZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=DrWlaqvNEgg4f_PUkRoh_NyM9IXDEOy_j72dQNW49o40wrjcQr7P2Htt_URsnGcJDsBq23Tnub9HvEjKAcTkYSFvgoGML39IRxCpLTc11cp5oAUUQU226yAT65t8CLpOkT36E17c4ACnYnhpV1QBpu698H8R65Pb-Iqklxuyva1-ZUAa8CTCfo9N3lI7ehMVXfLa_jv9dfvQY5ITlrfnO9tjUQdtOGP0nWqTxFBwaLv18mSkqG-ruMgGSSne2A2lG27LAFFMA1nwoAzvafEsIfJX1XnC4_UbYI8IUaXdd2VSXDSo2ywiR6O-sgjUCk_37hHlMq5QNYzAy1YV0mAo9BE_3gR5VMtvzhEjkzlkHJZZNJjJ-CR_fVA07U9sHwTeqnmPJeddPXN7OFVwi5eIq5ld9v8pV1Wmv_61g99jP1rHIckxHpxjOcGs_cizTGt2T-IeMGDEjvLB5T9Gf7b0tJ6wpycbpC045AulIR7ak9G2y2zT91W5rBt6Vyv_IrfPPOjd7YAvywzbbvkruBAQVLijL29XRh69Ml5kSWs7zZK72FPKHqHSzkihjTbzBU1BnJxLAETnVPZv5bJ-Ev2tUaN51ATlPcz_-sfayBjzmMXOWw_MoGo4e45ZPRyoPzAE5DyLyTptE8DC_xC5kQVCIa9rfoWZPfXwfz8FYUHIEIE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=DrWlaqvNEgg4f_PUkRoh_NyM9IXDEOy_j72dQNW49o40wrjcQr7P2Htt_URsnGcJDsBq23Tnub9HvEjKAcTkYSFvgoGML39IRxCpLTc11cp5oAUUQU226yAT65t8CLpOkT36E17c4ACnYnhpV1QBpu698H8R65Pb-Iqklxuyva1-ZUAa8CTCfo9N3lI7ehMVXfLa_jv9dfvQY5ITlrfnO9tjUQdtOGP0nWqTxFBwaLv18mSkqG-ruMgGSSne2A2lG27LAFFMA1nwoAzvafEsIfJX1XnC4_UbYI8IUaXdd2VSXDSo2ywiR6O-sgjUCk_37hHlMq5QNYzAy1YV0mAo9BE_3gR5VMtvzhEjkzlkHJZZNJjJ-CR_fVA07U9sHwTeqnmPJeddPXN7OFVwi5eIq5ld9v8pV1Wmv_61g99jP1rHIckxHpxjOcGs_cizTGt2T-IeMGDEjvLB5T9Gf7b0tJ6wpycbpC045AulIR7ak9G2y2zT91W5rBt6Vyv_IrfPPOjd7YAvywzbbvkruBAQVLijL29XRh69Ml5kSWs7zZK72FPKHqHSzkihjTbzBU1BnJxLAETnVPZv5bJ-Ev2tUaN51ATlPcz_-sfayBjzmMXOWw_MoGo4e45ZPRyoPzAE5DyLyTptE8DC_xC5kQVCIa9rfoWZPfXwfz8FYUHIEIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LHMKufKOW8qgIVTghMGR_2PEq9AjVNxQY2LybHfek6qXiYPKfrdBuJKv9-sr0zDAcZ_ZxDr5vqkpiRjBkZ63y5DP3ZT55jYAjoX7rPLGbO2GPyyMF5JJYPeVk4i5QJ-z86UK_1pmMlIKnzuonggBduvtHLESf_PeMujn6oO_v7Z_60sQyKWcmASlzPO9RG0QtUOW1fqYdLmUnXAJjPkby-pHVgf5mtGGPLKp2D2xpDz2N-sVv0BXzAII-W_rKbkMZccKwq3tJauuOCzUsgjzNQuNnMZLUJDOE52pl3a7Snf-CldPyybp-t9ow0alc9LgGy2EeSp63GmRPm-ryf0glw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=AC-TxST7D91ZHzZTbe8P3rQzKG4e3Xz9DxGpOvBxk-KE5V7oaNeS5AzgIv5le5ph1S8jbbNeRFQOG3VajkORgJu-CrqCLdMMbzqccrV_uaglWoo2_BGPAHPdsfRagFTQ51SzBmGPy0L3mqT9AzEuQbZ6y3dsugHoR4A-ZYAKuVgv15071AGHq76xRPItxA-yebpA-T6Br2oFS-0D0TwHxpjwlb5tfHRb7Z79XkzaUidMBHcZEt1vYOLj8GmK59Ix8shZ2ze9lnNLpTrpzLHZduooFo2O7EmBm3mCQd8oyQEonTRM5L3yUF1-5508bRjTFCIIvfZOxNkXuLIKaVsNuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=AC-TxST7D91ZHzZTbe8P3rQzKG4e3Xz9DxGpOvBxk-KE5V7oaNeS5AzgIv5le5ph1S8jbbNeRFQOG3VajkORgJu-CrqCLdMMbzqccrV_uaglWoo2_BGPAHPdsfRagFTQ51SzBmGPy0L3mqT9AzEuQbZ6y3dsugHoR4A-ZYAKuVgv15071AGHq76xRPItxA-yebpA-T6Br2oFS-0D0TwHxpjwlb5tfHRb7Z79XkzaUidMBHcZEt1vYOLj8GmK59Ix8shZ2ze9lnNLpTrpzLHZduooFo2O7EmBm3mCQd8oyQEonTRM5L3yUF1-5508bRjTFCIIvfZOxNkXuLIKaVsNuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEdrZw_XbkUy1jZAmQNfPlCgs2XPgcrBLOQajLBqYJjUGhAgX4b4gwU-A9QkYjyckME4OBh_pQ7f9MARNVCDW0Pr7Qlmo8Si6CTQSpUiDin7Bb7wbUg24s_6g9k5g5gKNntM5L2Fyo6FKfsTK0kVcgjhP-ekXwbGSbff2TWBP1k8Sh_R_4rhgEg9QIJ-5v8OKQP5mjTIOCKHxhDerrrtB9T5F3l29rWvy0gIk_ESo_U1e2KQ4NpjXXhD7i6v542lkFk6Z1m7xh_fUBtYBIG_2UskRU5L9-mWHpQOMhusl_09CSjZdksSxt6vQg7qjkcGka5N1rPFOZ4tgiGoIlUKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWEglqlo7IY9cWemClNx8EQju6t9mc_mDtA_BJ7I12pHoAgyJU2meWxhJltp75aiNv1FPDGpaz-P5pFDrcyJi4XBAD-OlrQl4yqDB31l0VStwFH1dz9EUyiTK6-2CrleI95Bh5JWj630D84bSYDCiV9_FDWYjb-2c9UaDgWN_lL_e5jJKrRuD3YfrQsWumMeMGWxg6fKTwDOVnpYrbIxHlgsrmsyrbjx17vpEk8oiL0dIEjdX-wgw-b3OFfNj90ekG73ggGxKzRB-q5q2TjW9o3oF8fuhM9gpSDoCWYggRoVSsxL5CCV2N4vZ9JZat3gqbWLCcJnaul3caUNTrNoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH22afeaFKC9vvfi_bq0kQufR4qDHeWrMg60v8Acrcv1TPu5jUb593C8A9JsKjDbj20a4Dyi-xwBWw5tni21mScA1Wxfa5wRL9KnU2QqCuGYGz_7xe5FS0hNQ6kojJ-0kMIF1JwsqkzLMUsUtG3uiCIfyHVjuhOCusaNDhliv8VpzpNugprsJc7sumX5bYZPbABhdCXJIhqfz8aVFOc0Rz0puf4yeavq6RyPY2qElJT_NGIb0D6SOmiukJgIR6uRuiVAJLK56QLokx-uOwMVZ51rYIDVA_I4mzY10yj-iEUyVs8EULcCFVOB9dAKSY0GwC8BBpqpC4noHnaLq1lN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PprXQsCkRB1g-_L8Ydp5tHc7Ir8f-AnsGrCOOZXcwVQz2-NFPSHYOxn_U2bcBq_nBrVnm2y1LQ575sOja09gxh4IWqqXd6YA134zjwtbvTYeu_aFsKFFNOmqHT1xZ6ptPw_FLGO1ZJ2eNk6pDPuuOdbt3XRal-wA0o7uHYEbSZ6r9haRGgVfAflYjjo8nNoQEhlq4zWCyYJUxjY8-ZJ5w_keFZDu6Z3oHhe90WNbk3ep0CvUCesF8XCOlyv8I-KI80kL2Qs4BYEYknkKNXp1mZx5JqWGRRgHJj-qO2vedmoz18qkhJxP_B-oKL0VD5X_6gbiNdo19WHgoBAqLt0LAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoL3xoSyE77A-3VjeJ76h5irxYbEHTzx9kVmBove6wUghcvRq-05Tir9cPKYcIV24yXJZ0ymyUzgsOgSITOCi3TFFo6GO7vNImiioLAMgKeJFY3Ck3SAUgkmz3FE5pbthNLdBeAa-p6K8PTSuIqC8yYI_8VJl2_iXiOpOM33q4qFtIrRoti8hRCaM1SulUNRyo__gGz6lop4YOojAYedwRx3HoyEI3wRliCd64lxwDtN0YLsps7f-P31uml7IIS-UleqLaWlb6DsfBfxGRLly4YvN5dbZYLPORcyzSpl79B1A9fh6ty0gBCnJLhFD0sTy2pQmLXIlavjREOn5QaflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpweimWNvdAxvUgLIgrTlQasrYwzUU0ej3byIPpXf5Jvc727gAhP4TyuBLS0b4I70QyPuEj7yvlIMqz99SlitkLLXljNlYxx_f3EAvL-YL4nnwL9tFbCmZTcA42f8qMmmOBSFhob7f0KQ3xcC_fj5IsltSh8UAQnbDoRaaJzVV0JSrfzOfJQdsJYLbjBWUcn_V4STae1aMHFgG4ePMoTe-bQpbIpSiTc8CvdxWaX2z9GdEvsUMXs07BwXmzRBdzYwzGwD0R8vuLJbepeaR0vm-1B0UGuasUAxUFwQYeOoG7Eu-Y1Ml9lEz8TXAR6HnJ9cKeEBPbPENcJexiQywKNka08" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpweimWNvdAxvUgLIgrTlQasrYwzUU0ej3byIPpXf5Jvc727gAhP4TyuBLS0b4I70QyPuEj7yvlIMqz99SlitkLLXljNlYxx_f3EAvL-YL4nnwL9tFbCmZTcA42f8qMmmOBSFhob7f0KQ3xcC_fj5IsltSh8UAQnbDoRaaJzVV0JSrfzOfJQdsJYLbjBWUcn_V4STae1aMHFgG4ePMoTe-bQpbIpSiTc8CvdxWaX2z9GdEvsUMXs07BwXmzRBdzYwzGwD0R8vuLJbepeaR0vm-1B0UGuasUAxUFwQYeOoG7Eu-Y1Ml9lEz8TXAR6HnJ9cKeEBPbPENcJexiQywKNka08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Kqikwofmj52HmE9B3gY_xb8zCBK1WTyM17_ORpEv2zKdnazjXaEBrVyfjs-efQZbmB6l8zqR8A5QwRfaqiEtccQ_1KrGTul9xpAaYTCqrhhUy2iT7IzLPErPl6cD1jhizSVSbiLyc2UCKKkYTzi2NB1IMZa1CRDci79pGDr8f389M9i5GUw1urEZpjJMDrs3LfLHoDYteswmwLYLdouhnAhCFGXyLNiiwaPgfxWjH837ZfJaQT6wPwvo5cuxJO2sOLXN2dpY0udBexFQsxhvH7zSMJRuPyO-EzZrMMIFDgcCgocoYQ8dcCQ1JHOyqZHA8SuJv43qSQPubuW-nVnW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=Kqikwofmj52HmE9B3gY_xb8zCBK1WTyM17_ORpEv2zKdnazjXaEBrVyfjs-efQZbmB6l8zqR8A5QwRfaqiEtccQ_1KrGTul9xpAaYTCqrhhUy2iT7IzLPErPl6cD1jhizSVSbiLyc2UCKKkYTzi2NB1IMZa1CRDci79pGDr8f389M9i5GUw1urEZpjJMDrs3LfLHoDYteswmwLYLdouhnAhCFGXyLNiiwaPgfxWjH837ZfJaQT6wPwvo5cuxJO2sOLXN2dpY0udBexFQsxhvH7zSMJRuPyO-EzZrMMIFDgcCgocoYQ8dcCQ1JHOyqZHA8SuJv43qSQPubuW-nVnW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXaMCqxsnIXfSLMFQ51ip3cNWs2038RkwEIwGiPm-cgbYkrQdPe9SxbGfseTkzTxyspbhwwSdvztaDaqaa4ZSrmw2zr32UCyqjr_A21uN9_qKCD_EacgH_tYif8vrPG7xcWQp9wIDAG5GM0EANEh6V7nNiHa33b9L5HEPP9DPeJ7ZEpQTrNy4B9cLmYlEul4x3qwDDvhLggaf-sj83p5A2gyF4wclqXfr5ddSn183wQdQ-9NCma5yZV8wa9cKaxeZNs3XMoMyENInGxXRP-tjDaNGR8ydaVCmJy_2PxIeA2hSdkHVCSA9ZkhmfS7KWiDqh1JkCwh7VaghcMj7MiGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8K_NcH-tH7u1jXZFglfNRQGMIg8-HRsMxSoosACw3wiBFrNwFag9N3Z-dN80SYknVMAezn06DZfX07H0FiZe1CWX8vgg4bf3bnPrfbuSJO952-rrS8fqgOMQJa6l4qbHAF1xMB3erCo6crhyvrMvYXPfxtiF7Gy-_W4sPtCDT6ljgPq3hglx-c-xfgTHWz3n2GxM79rI1waIZ2i0dvcPVyOZcHVL0_vgqKowgor5F8Aws3dNdMM1ij-SnnQkuIgRq58Wir9y3BWeFb-rcID33823Hi43BuivTD3BviC89klGpIt2o9Fo6kmbhkRJtemK_wNi8GGhrERhJvpE8Jykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qZs7w7eEZ7BNAl7NMoYJfP2MP3cafhngsSMSibf8oVxxziS2P34vxG5tQZTjqr2PEQgv81PkyZ1c6zgxw11Be6eprEd2fNNauvj4gYmiML5tt6zCiZ55Y7nRcmuLfSLZrfK338JQjN5O4d2KAhazCrwkSiM81Vr-NwqtBENBCYksW4sGM3tF0aTZvJ_TCzTNC2UlMxNOOr57AvpTSHK-xBcH5DaljE4sMXz23_0XckXVUe0U1TE_-m1tB6Ab5GdvnfESXvHdzNu5FqDc_aCPwielC1EZTv2vytd4mYdJPNmRDcLxZ77_vDcacTrGZlgSnQH2Y-ablmhxEdGvuuWktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed_YOXmaIaVdlEuYa2shYompximvb5AjXyZeB3vES6f3YnskkRAN-otyecNsP8eSGakph1x5u_hUmJjRISAaECgXCTpzpSwbDJMoRv2vApkooKy8ZIRLZMfnWKzEc6tdd57Fmcbi8VLtEWCcd0vJeF4llGax9QlEz7BhXA5_nSrLGSlYUdipTMxZAe94tBbNlGlGgXFGuaxJFp667ugRunMivpb8LDTKIE5gM-8wLR4kIvMupmCTx4zPLhBvrkW6bgcSso29t5oM-dxh6_wRnYhZ1841TLry2tIWL4DXRAGuTVgxAAuzW4iXo3dbID6TKaRRnbtAqUqB9NlAqbwM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0g7ZxyE5BZw45EvssBvp3Aafi8aFB9RNay5egW9lbHSqjY4o3Nax0TpfBq99wEx_vdgOQvWzgx7BW-7dAEwsA5r74l9HM7lCHLXLOMztts43SefVHJL6Ze3z1Ma0UplY-kZMvQC4b8hMIFZhmvDmEl82cxE8-r6K9ShH7tz7NVpoOSwJHxo2DwyC181bkr91cp7fPmNYoMnid32zN7xOuD5ZBelf-8QID7DyzLur8OX5ZbYPOBXBqkGlJPettVDGaetBFiHuf1Fg8TTv41v_fHTmxdPtJYO4C-AwKS3feKbqZL2ro2cSrBIHqE3fdnkgdNwQPatnxTfJTCfYfLAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-aqDyVLZD3sCYQK6prtsHcAHDlEdXoaeK_FidBObqIChhO5Mya9AeGmQICW4txfq9Vr4Tbf0HPze9lwaOnTd0yDAkhksIeLLAVy2wUinwq9abvixwUvUydJE_w2hqme7qzVurzWrZYig2AcQKTI_p3FiT5G3LSXZvaAUDpuQ_FIaAlBIohdiDkp1T4tjkNKxzZlpTvKYUsEQMZN6kCGhAOZpjpawl2KcQsJjbA0cZCFERhkEE7bRzwJWmoL1_giqk28GQcWKYgp8hsk2HXMu7jsuigbajc3pclfCW4laBQ9dMKaehE3epW59Op1rfzhPR7pOatLbFWNrN3p07WAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqbQLLCz0-auRgRj4N_t10m0vVpUN5rgeZ2TYW7cMS27w9_x5I4d62zLoa0tUfxX0lIymM4SxihPhYACumgE6C2rV42voj2rz-xz-tgKoAVC1JI1E8oAZTYDSq7UJwJVoVfpTBRrr9qlzR0xhEC75L1Ta8ZQ4YtXwhgIyfpgjF9vRsfZEveK7mH9Vpx38IvDG8ANgSsRJnzdjKgFcGDb5faJyLiTrbvatFnPX2uDmb75kMR4AwD6fS7wiHMybO5q99oFXMMFcPlUjpyG7qjyaNkh3zUESScfbrVjsPtfpsuEjkMW_X34c37c6pYeU-4Y7okECk9opMZkLR81CFEI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjHSEpXQB09KBiBQotjGKaDe4aMiOPnF5jkw7JydoS9rOIM4vc07WXlTBjIojNyVe7wn7ASS8FUn7Ne6Cd11u_NTqyO4JlLySpZphmzJB-1RvbHdnyCe7qWSrV3JYtMXsI42KZfSyk9U-MqAcQVmpV8CixHAKTRXY2yUDC1Bl4wmYnQBjk5hwuZUzo8nBJJUpnqHW0L30YC4YF4NLy71LhP_OHa3RecEWdeHDboWyfkhSQmzu-clD4YWjPLc6bWbDSwxhQcUNj8Il-sgtVMke24oHCQZzvgnWWx8CszlDa4DX5B9nzf4LvoZzYvikiC2BxqI5I2DH73M05UJzJQCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmV0mBQr7nSLsuHN6gjmiBe20V_0zrZV_dC55_vXDKjM8nNzO2Ulzbqm05gnhYlNKP1LEK_pnuOhnfWc2TJ1rQO1tXCuelSj7lzEhbkEsULrTtRqm4FD5EX0oCvD2-1Ko1RzxG9PKpslF2wAW3QWxhKFCYYkevf_9_xnCWdSYgbsQntEkrwLMIIpUox0bumdg8x70ASZd1X5blNBZSy29ohaPzaPDfkgi1ZlniqmE5HPK4lWibaNj6oFAYD9GKHPdQ5bKJO9B5KuIywuNs1lIBA8p7rqZJkER-oiTg7XFnEePhIfN079Nrg-Ydynhk28Hfc9QDZn-oSkwggMWVvH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0v_UwzRzg6L9b_IWrKHfX2Aj7LJNqm-5ttHoWpHgnWdgAr1Dw2bhBoh0NMJYlpKwzF1P4xeI_3MQw6B0hlPkmJJbx797BXQYK1pHCrTU1LIMejZJ3KSa9N8Pa1Mbq_rtyrgfbrhRnSolhVhfejuTovI6mcmGC8vPuvbbTaKjaY3F2oHcXecHC7aXGm6B0sa0HmRNfiHPUv1sB9CqWvPg-MC2y3MWAVhqlKwDP26xERz8hb0zt1TW7r_ZM4a9gYJNK8cuRFwpObiKlttq8eU4-79SWx6huhKmrtCWXRB6h52CZ6MNi05rlKp8IkbEAMwNCa_MJ3DBj2WYR0Q9WpYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWZMu33jQv6v-Jk8bSOxo3eQmwfT4OPR8lPdZAvBys_bF7OG0160G687JRj1xir2MT1UyyAGCkLewHcS-fbigYXx8-FQCQ-JuC2rzK7A2F3SVLk0OtYTTbctY5Vv4Pc7uduLlbmzlWwT27lmKjRxbUhsr9ZvREr2-JxV5OX1CCcbnisg2nR-fELTYZgJ9oERizrFVxoHNodk4stboPDiR0aPiX_dfE--LbGmV_vDbDB6fXaSfls3z7DfvQscKc4WQ0xKiyfOA8wkFqLlSraQgxgM5jUGhcJiwF0nl7XKui-3BakNfxelUK7oimNdF8wex2Tg3MXsPn3KgmiOUsMRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=dO3cRZ77YtLVOJCLiDF8d78J6rgLRy3db0kz1OsbWtFTZDKVgEyui2-OtE842nHEFaWt29m0hq13LsA-ZfDNwmRFbf69QT0x4TXpVwduGHsJWuIxqsmmd2Ah8X9OgjJ0TlOiVL_hqlHQKDNURf4dL3S29u_KHpwZBxWR_vDAZCH8rTyKp2iDcqomay27sGTGCK2jY0QPOaJ-MOqkC0tmC1Mz5CRSK6-YklLxRfhP7QBXKJIr7BS0V9hZR7qRZmIB5U0NhD3RzEC0MJeABcmOtGYn0OZQkjrJoG5mhzbomUsAr_QdKfGJxltSbw_JX4ZPIl_xuYm135mVT8-cp7Vp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=dO3cRZ77YtLVOJCLiDF8d78J6rgLRy3db0kz1OsbWtFTZDKVgEyui2-OtE842nHEFaWt29m0hq13LsA-ZfDNwmRFbf69QT0x4TXpVwduGHsJWuIxqsmmd2Ah8X9OgjJ0TlOiVL_hqlHQKDNURf4dL3S29u_KHpwZBxWR_vDAZCH8rTyKp2iDcqomay27sGTGCK2jY0QPOaJ-MOqkC0tmC1Mz5CRSK6-YklLxRfhP7QBXKJIr7BS0V9hZR7qRZmIB5U0NhD3RzEC0MJeABcmOtGYn0OZQkjrJoG5mhzbomUsAr_QdKfGJxltSbw_JX4ZPIl_xuYm135mVT8-cp7Vp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsG9VUEzlYxlKkjqFRq2kdB07z6ENnlqI_Almh_6OR3DTxTJspQ6qkTfGNeA9i3R_Ju7wBs5YGassINk_VB_pUCIEj2Ofz7EtNtu1lv-s5Xcn3h9PX_b22idYG1rG_1iSumEgtdHpbKxL19Puuf9pVbpf_yFMhNam7B0zNC_eYifM40zFrmjbBzHjf5tQp-LtnUCFqE0zHli0kLfzx3z6mC9xSSJ-5yKLqOq9dUr-qFWSVUSC8jhuNPjXfxI6oXmI38QLJ4gadbfYxsW9ZjQEFXBso7rQM5DHW32KqkUNOf2ONjLPh-Vk-Tj6aSxPW8iTUFi4FvJx4d599PkBDqo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OZfCkL0iDZOzg01424Ahpaia9S4AgVzn8MybY-nGUXfb96BPdNMG5vAlCG99DifjNvXcp7Jy7Wif_3ykIt8DE-ndbLjS55LYp0yp26dZRc3SspMdbQmqgyqh3kxZG2CMfIh6kodeJ4loAB1ZjQCvFzoaHQ8sKUKQEinGa_DvaEv0qdfQofg5nkZlruyXcAG5OYef07oVBA5DDT8Q1goH7Cq3TLd5VNbH5NxdubszpZ18NbmIAObutm3jXnWylGoqsEEqwOg2D4J4TGGdR2kDetYjZBmCkI72ygWV5HSwICi0LVd19Rvz0lcdHW9xqAhTiiTSHBl3uG2CV9ZZIpQ2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RnnbLds7Ychcik36DJ_kK2sAMo4p_E5AkbxvIqxkGS4anwkrpiIKEccp8U2_Z1EKYZZYqo7gO2wGzEWuRtcadNoVJHcy02VmSVMKxO2k_6gar8vR7LuBvcAlCcCNZ0HWIiZsGXUzSeFm2LvdutvlncO2U5FFj_cjmssT228xx4ua42eGYJml4Dtzl8VBTqlxk6c-cPAOtlvIQ8gEobw3W-YN5iWs4AIzkNATKyCcB6oHexbM9hPFYhseFpzpOBCfthhZZEufJdznjj9_WJA40Idw8vbEiyIhLVzEERG08uvbAuE_S1B36dKrisyqPcN6bIqiVEEZuk9GJp5i4HkCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QUmUpqS0_dZO1SjqiZEeM3QVtvgsDdHgVwtm2K99yGLOzcM05Aipv64YoA9DGR6nH3kA5KzZqDwuPTQq-dekR8BKQRcUUy1sH1H2SD_rWuFsEhDhyCU4fKeO0dlZQIOPK9vEhKeOR5NIYgCW8bzMvxxv7XCGbJwAP-eRcvDeGISB1LoHU3KKOudfjLORQE2H6CZ2ZCJYNespPcuMRY1UGq7gfewv8nRbxHKyyqOJSLlgbOfyf3Lj-R1faYvcHPZI-xEAl-SygpxXoL3Bb4AFDZH42skSohaglzXKcC8Y-OPGRm8mvmzIxsbDaqaTj7i334L9KagfnA69Lm87BuVBFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aco9A9VOSF6Jko1qYVJq8P41NqRh1baRef-KDhyAuEB4rP11RZg2_n6oxulFgHsSbwUEO237wue99X2HggIEB3bPPLi8WUtArP7bDRME8bJyU3upzrtyCK7j1u_smTlYWxeoPSmPA6I3sZIn98s2UA43hGb9mvK7AW4nJfxehfgdqoRGX05xqD6JwPACF1IPAO7rX0K-XCQyJzwePEEUcQayzIeCZZOEjabXQKPiOsbAuZ4kk9_dw_1lcWoP5n8bCxLGUjPWi_E6RPkbQgOP2i5eQ4RqKLaa5ZuKYn6VgxIZeF4M4UXuhDB-osFZpAVThamjREDLU0Yl3OQ7DIc5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFaOUgxClTk-US0OY2l8AjN3AJS6TH_WCnwBToazwbp4UG7fwvqE8eb3AdYS3NJ7q3xqMntmqQH-cr-PcO97qNFiPOeCe-kDX5_gmR7yX_aA98dKqYXgjp349O9nvjEGBkMB1bQ4YpNkzDFM6Ld3ijCKWYn-7phstVYweirnhlYO2GNnoLZcLa4F105rcj3CQTuQw0L4rjchnfIq7Kdd2auGyHoSbWn04VvYVKmVR7albVGaxMZxWKCYdrXvuYAMsNzdFARI7f1jFzvbPX5nfm7QifpOytHHVk4ykpKJ8dTnSTf_XNT2TvluZJZm4IXVll5nxAlTBDfDD5-5vqmVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG66gDCg8RVXtlZZ9Cb0XSBAPLkYy_wNlZj5C-jx0QXnwYPMXwe-FHJ-6uZwl6S6yN8GSjf8fSMowYtLdtH7bfIwzBVmxYIAEvodjHE7HvyUE8BQwjBz061naoyApPZ2lCusi-1fLkj4FekRt0UQR8mXdj4MACkh1XeXaxqY9sc-mqOejtizfwTtfNaRqv4S6mz1Zf1hiC4lyXp_TvHtGFx8TXuu-S0xWj45W1N9U6XTWTDqj0rsCIeIgcq0668P4lzOsdgk1cu6s-5mGNWpzgoUo5IZ5NzRVJq7oQw6xuBZLqGQmzWGgJrkJ4CVJ3vIn54UsJETL0oKkEzD3L_JFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6G1HeqXohNpKOfQDxnKSCOLY8MGIXHF1hGC7bNK_6rz-xXcsdEhJ6DbvLCYsDGTix9OozWs9ZDM66flllmf6F8ncKsu1FJ9KYdLgEIFMkg277uIAdbeVLBuBj8VQgYr5rZ9Q1q1RO6LhEL0A07M8b7Ca50z2JGebUAgI0p8dIxf8PkH_gwl7McHUXHtyO8M41BsjFIKr4M-PfRZ7OVdK45KlZXpoRPb54ssqF_FfSlCv853UFJ7G7PBziEzuLMd1ffz55ZLwIdHemiVsvOWszYRyi2ZYCQbZI9nS-tBUFoxPaVguJFik7hwA9YfZTbQF4vR77J_kPXmmi0JaO_eOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnsFo1fN4Vt7hPdHBCigRjyQtfPSAe2MIIjvyFHcm6_NOKAOIowUSF9QlQxHSSgsS3IQfWi3TX_RZHf4ZMFsihRPCPO0VoCvClICAh_gBxlCtWeHj_YxAryhTfKW1odiEf648tAErmRrkkNvw8CXLQIZEesKG23RaBSfVsv1TeWudkfNSgoy0xKRGutmnMOJ7yDscIygsTPJZEwAxtMw4j4Tg8YsgsO5lVp1vXdZb_x7ytDQ5vrXdleuFULvCAUiNJCoDW24lVcieoOVpymth8nMT1oDKx-uiZXzZoZ-aJPQzWajAIuBkcO1s45BSWQsIcQOomnpKO5o6PPxbcXF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8GBnW13HK3gF5zRJ2tlsmdeHQhtjjQhAlpivcSGLvzSNfTM4Tpu_TkywIrzYZtuCJahYCqfCzBIEX-Nvx-NpXd9e2UTx_4EIiWsbt76psQnJeF6gneQB0mYzw-1Z5BDfaiegeUecH-Ib2fda-yDK2l_xielKzqp5syAcYo7c490vB1J0vpwHT1vEjEBvVpaiZDGupjpQriaVATQGMCZjmumGlO2a0zzFSwVspC8e37ew03Ibc0Abs2r8lAA4MeQ_UMCJH09hf-V4AoLX6bOm77V8YmN0wZ4q-g55M28-vwDhPQy0DjQVQbPqDzUL7IIPZnSnA3HaAn90S_duUHs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITRuLPYcS231stg3k8qpXZl97PKk9yTbTal26mDgXqfApA1HJ1VO5__9wvZdP1jV5B1Uk2VhUiWMzmT0w6Ke5hwz8_rFs6_ckAfFKvKk5As-PlkUmbDz3Lkxr2NerramPYbHKTCwYhIxNopXEw9CtM4BshPy5RRBt2JGF1zu4qKwCZzpPV1LLrkOfcIyca4JsiIfQX2SN-tsVmJGbEoYVy9jyoOvaUIUDaYRCMGVgTaVE0zSVv5D-Ot-j7iGxz8PrB1NzmS01vYf2wEz6pDLalkFPsohnZe_-G9KUq8MtXlhYby2qoC8R4ivbsXHHDfDAzO6rxxZYLkkolyZ0gI1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpV2nNFkK-WVe4eYZ0qwYNk4xbGVvzmXPmPmQpIuw5ZWuO0OlGVXIlFwy56jbQxypQuNfutwUD5c1iqnqcko9xUXcgSzFPWbWRpgo2ski8t8c_sTjIQHJ9QUTrz9t48OHWM4uq8mNKJQApOoOd_mYz_WmU2F5Jy6hkSbdxCwamt4cc6_FliHKraH3_7IJHdCdJyUzZDYz31betTNAaxTh9Tdt_2-CTxdyC0RVhFdQ-JeyV5ThLiv3xGp35V1ZiXtXAGSRZrzmxH50-0XBnERClsLjLOGbKYf0jIVOxIZIsFsCIlUMiqqZYRiMOr47f6U-z1xaS86VhWuEnghxEPbgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7EhtyZ2ZJ29A5U6tn48Y8wgHoLqftiyztXxQDYBmCis367EdBS7vs2-Ri67wIDRCj4Ph4DNUjrgxLcabpNEKgd3L1wqPYm-UV88mLZsQrxgiEOWqFTT1fCsXEgSvOhSizB5QV4XuWXY8GyvnLuH_5Y33xxkiSVVRddUd4WAx-CHVvArfCxwKEzd6_EMaqiC0A13-T29eBwfGRXTpfPUOjha-vh_quNYOLmBfmFHWJQir5kqkQ0bjF8t2gCExSBt6O6gQOnAwwszSu5QDZzGKGktfIgUEltXoZyZia9s-H0LcwOH_vJ20eqKwdMzhaGvr3_bsRpe_B1bWand_R1JDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slpQ73JqOM2zOetiDquGxHpD-wKirT1IH4uNgXX-bY1f_C2tl9zE9vNR7R3XGInShJobB7A25k4LqJfOsb3w7kiGvMyzuJLIhGDJl1ctUZRGifWOYnzwiiT_10QjEma0XBz4ZppjEoLPfGIKWXmxrybw1x0Xsr_qRUgqB9VFQ3SSbcHrrfC6AAi422Kiz2PfM-HMg4eVlGCHJ8WSKgWvNY5oejzJ1XeVHP5uRH-U3EC0Q1wSLona7bNhmuXDH0imgH4ktHPc3eQ8_IstXas_0E6sRUfAhxAsmrlzIJ2z5No7yU7q2pIFM_xKgaovL4SjhK0rndRvCHxrwfpQqYMOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=q8mm1UCgPqHBfhaoq-rMooy9Tc4bcu0F-NfklkPnB_FWMC8J79Joh3HjZGl2RFrKBLHkS3vvvQQlqW8GsuIwH1F0CNKTihXv8BkwxybHj4ieuIJSVDVPddo3JH70Pi8kOdwheObaCKbAEuPMI1NzekZaJTKi6Mgnt8EjeckW7aCm78CgO43GJX51n6jWFURcQLDQzNwdb3JhOI4a4OvOYPhE6cmYaLOciyoYBuZGnEWocsHLzWHLw5WOe_ipyahYchQ_d67pk1T0M0SjSE3UckorHwXgaHS9mrllp7Nrediez6lmbxo7KDg20A7QqAl-mRAnNKmTEIxgeoJtbDI9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=q8mm1UCgPqHBfhaoq-rMooy9Tc4bcu0F-NfklkPnB_FWMC8J79Joh3HjZGl2RFrKBLHkS3vvvQQlqW8GsuIwH1F0CNKTihXv8BkwxybHj4ieuIJSVDVPddo3JH70Pi8kOdwheObaCKbAEuPMI1NzekZaJTKi6Mgnt8EjeckW7aCm78CgO43GJX51n6jWFURcQLDQzNwdb3JhOI4a4OvOYPhE6cmYaLOciyoYBuZGnEWocsHLzWHLw5WOe_ipyahYchQ_d67pk1T0M0SjSE3UckorHwXgaHS9mrllp7Nrediez6lmbxo7KDg20A7QqAl-mRAnNKmTEIxgeoJtbDI9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klqKhq5bSYfmvWuZNjud-5DLfGuyIgbKmX3SaQ8P945YwyY6pla_h8JrfxyOlHt4PyJlk2sbpV3OnOAq6-MUqX6tr8GlJyeCicP9T6M9D-Z8uaQ_diRU-4B6HrKQy2uJELUKqYmLYzOOePZlhgbVEXrXZTHPUUxrvZ84Kne9ga96nFQIq48fgFO6j0Cta__K3xdeVb58U9TDq76FSnHuzlZuAESLUGBPDxD65fuXJQ7hi-Nptg2o-_El7MLoUw9KOp-sBmuRYtnQm-V5OPwui79aSq0WeItlOrDYQaWoxTujcmBMMzuqenEY0EIgr6xJsBNlh_T61feE3gOierkZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfsbHVJnKZMhRCm6a6yz5Sb9zxiXULsNPZ7LGEbgBKOtqFrarqb3ybIwb3rPfgsdf5lxBKkSLK0jRPNcHrMIpmPons5pGNXWWqMdExk95_J0wQl1ulS7mzAxw-tRO2oGyUZCvJj-kN7ouri2hpwmaWr0NfDn3nPrtV0RwhQ6qYlqW0Pm3WWW4zJa32mGfZ8M3uqf8G1lj7O6OjHyV86EJ7t4WX-Nsxvw8kjgXjdREtDVxCc0jJgOqbeI2V-m7y7Dq25nYDcRVJIpYomW9Fk837gL5MzZArP0EMzOsEcgiqZLaSL3W8aVE0_nBLFhI0u_BVV6EIhTvV88MqjfEBg6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWF9ogKLWz3CBxlXJ8WWED-qAkIC9r2TGKxI75yfZH3sUhfRoZdkA8HHYXX-v3Qx_Fa1y8VWdc7fw3dUIBIeVWYQ1LU8n-mvJa1eoopHj0_oa184N7IfbKOERKzCAiEnZIytfiamTjOJfg7ieEcMUweTrp7ddVHPR30AUInreiAtk11bOpAFnnWXHbf3_snASvZsxSGg3ry5x1eC5BGYziRax2fjwmjruRYyokDOLcjdqhUTO4c80ZsQaDHo6zTMQ4aZrAnkJ-PPkvbFCJx-ldCNNQ2wGtQh5yxcnThrHRFgmgpdTCA-3VZvwTDpWW-Tsf0n9Qzia85JFi59djmKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsZ7gwrToLoMgbO1HoGAj28fj_BoLvypPjhhPWb_qB3gsjl5veGWEL3_8VUwrRXNs6MH_18aN_x00li58Q7O0mlu7-1sO2bKQZHkys4OZzec_hy6SGlSKvA253SFhAKLVZPVl9PW7x_vt5hBuchPnQlAnTGmn2NKrGo5rXqe0Ey5rsP05EQD-5JuCNYL9smP0XXq_YJrMkEd1R9dzC10igc8JETB_skvI2AUQdDqh6q6fgzMWrtgRm_sEN7tREEXfPg3uYB57Y0PnnLM6cztU2e6ECJXxP3ga_JUlIskkmDxAlkEXHCzLIwXN4HNkm7UhDN6iqq8fxzHNhITYQN_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=mZPDs4FGbJtURQKse5ciheD18QM5l8laZXoDyr9oTX-740tOjK06wEPzwFx9RSLLYuoapuFChxXa-di39GbsJfl7h_rJsL6Uh4RngVLlbRIpe9r6hHx61rzSOZLu462A9N_mKdICi-w2jkFrYH-TjOz6pthzw_1U2MNd6Fqdk59DCSbTTLvTNtl6fMr4tmqQKtiEzQx5w8NJPIOxGL41MiqxwBrjJTrgYC5V6_13LepZgomH-HWLNiqy6gFgQ_0SxQSlAuLQfpl4SxVOkgYISZ49ByCedZB9kVEvuXsMGv_ovJhWwqbdCZS5W8iTDWZdzZu3MskAD_vM1o_9noB6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=mZPDs4FGbJtURQKse5ciheD18QM5l8laZXoDyr9oTX-740tOjK06wEPzwFx9RSLLYuoapuFChxXa-di39GbsJfl7h_rJsL6Uh4RngVLlbRIpe9r6hHx61rzSOZLu462A9N_mKdICi-w2jkFrYH-TjOz6pthzw_1U2MNd6Fqdk59DCSbTTLvTNtl6fMr4tmqQKtiEzQx5w8NJPIOxGL41MiqxwBrjJTrgYC5V6_13LepZgomH-HWLNiqy6gFgQ_0SxQSlAuLQfpl4SxVOkgYISZ49ByCedZB9kVEvuXsMGv_ovJhWwqbdCZS5W8iTDWZdzZu3MskAD_vM1o_9noB6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itrx68dHmIbdCrsEWokx5Gq0asJ3SZSuoXMkfr5Ky4KAOvhrR2AzsTtg88z-tPPwAByDmgb2JPHFy8-iOOTVD_KQukITKoUiW8hDLxFD-bVnJ_RVoEfc9BrtDrzrHRAXORzVnMz5IHMBTbYUnM1TVYn0xdLQ8VhtYnbPHDvmGdIUnCLot8UJTLpOoVYPiCihFjzrW0ZSTdI8FfjNK1YqCz0VmFLBIk9Nt_Cq1zj3QD4BJvMFPLGkrESINkQ-gy5OwjphynWmOkMP95HpQKLdszYoTQLDdcw3mDAkeK-wPdcBUGqYBqhPY9WuIMIRnMGoFeWGWyuALg7Y9h9jEuDyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OhxhEIW7cW9ni6qJiVnUalvFB7zGBWYb-lwAgJ-e4CdVV36vJpeCzjGUEqZ8M4N_VK-pNhiqHkvUmumkbZDzsHApc6tKweq56CmHmJwTwSpe21931JkDKtnNt_WLufIo9gQiM-GUu2uc3jzw-rH-e9x1oRZxOYabW4G3PHCNxxloyr3DzsianjGmRDuSAkufB0SidCxKxoZmJEfTPM7iBIpHlQOg3_SfIS7CkT5Ko6oGCXDAngSfl78D4EqElgrfkMRxi8qPg9mDNCDMebTyDk5pPqoLnNypJXQN3NkwvWSJL5f5i6ADLdzbUYugtFkfsw5pxFro5QzOAxtXcLD7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=j1kfzyRIMN0y3pKvRr6S_JX3-NQHP2bKRR9nlZaCuY1AVkulDxjMlhE-5III6JPtAjET9GlRN2LIiQmp64FCs_H-1aH5wrdp9g-wIrWEWfaYfbAY_dwtiafzkTBQQDxwqgO-nLdCXbEAd5mFyUDjAzk6BE2B_WBQm8DjoU_2ZXy-MguZBi53gxdCmIOVur-fDTyreHGFQSyWL37DL_SexhZEev1sd3Gp9VBFwEO1FsGFsPkSoK1C178C2LdjnPQqegl8zOeXc_L7oVnShbtxNDc46SooD4WLn5wI1lN0X1P2JyrM6sC-2bNrObJkhiQS2wSBuCPHyYmZmodKG57hXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=j1kfzyRIMN0y3pKvRr6S_JX3-NQHP2bKRR9nlZaCuY1AVkulDxjMlhE-5III6JPtAjET9GlRN2LIiQmp64FCs_H-1aH5wrdp9g-wIrWEWfaYfbAY_dwtiafzkTBQQDxwqgO-nLdCXbEAd5mFyUDjAzk6BE2B_WBQm8DjoU_2ZXy-MguZBi53gxdCmIOVur-fDTyreHGFQSyWL37DL_SexhZEev1sd3Gp9VBFwEO1FsGFsPkSoK1C178C2LdjnPQqegl8zOeXc_L7oVnShbtxNDc46SooD4WLn5wI1lN0X1P2JyrM6sC-2bNrObJkhiQS2wSBuCPHyYmZmodKG57hXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJim2Zqp8VurAog6hdDmf53dSYoASxTH__1MB6zUFVHBoItDYK13PpxFc6kyvZa2J4GW14-pEUgeAVFo_RKRTSo53KuV0fVMySZPfF5L5KY6W4EMlb7h2wFgMXuh5YAsbVddZHQQsR8AOxHU4GNzlFyYFFCQEEWsf-KpnmN1SeiE08bwM9C-arad5lUg2eSc_wwGs3pzI1fUHa5AB4Tr0QO2BGEJDs1rknSBimKBroIRO8pTDFGVokE0d2CXXYxZ_euanrmgBdZeu980GSUl8OkQKfBe1koMGjTiJi3TecFXw--zR2gHxw9HwDDVGQEp7e1aZ6S5Of_8duIscPY5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtwFo94W7y4H-XYGQjWKfBchxm_oLLvlJBTIfcEab80Q3nLSIk3Eo9DF6vl4Eeyf1X4oYMAgXVXXwc1CpyqQpOMQKYgeC8N9Jzml7CLj_BXJNfsW4kNU9L2j4aPOh0cSjZqQky7PzUv_AeVhJJK5uNIAG_ghwe7UEeW67O9Mv17c4HCIX6__SpqUQcSFmJgqN_sskCGzZ69LLyqTrGTbwiJCoY7ZeaKxHdr6eIqSYbz8t_06Ji6fy4ZUGucUPHSRoDG_gMG-yOP36eP_x6REpUyaNQfGJILBKbuTHOG69peaG8plxCrahFe4PZ-FWfTJtBuL3XlbBbQSvc4u-oNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgT4oXA67hBQCPMmsTxaLxZOqUnZ6g1wadhPt5g3RI8dCeQBR0bFmxsrgxd-z-2znsK9cvW5Tp-p_m-sOTQIRASB570H-udJyiAtZOi-Om6uyKpAJYXhG_O4EVlWXdL_fJeSfBnfBoce7RUINVN0jIqlRcsqqgan6z-vmiKHE1NSZh7X7ZUkpbJnHfhosFfkokoX0e8LgUcUH-7hrFubBarnEs5eHPEEv5hVjCwDFj8TEMcL4fMPmkWgNzrLIeiwbucPc7z-kTO8MUqL9OLWAb9Lv1zTXRFrqwvRwoUMfmZanV89xU7wxTjtF8C4cl4CSkxKgoYDaL3QhTfRimJpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqknIj9seZ0GNCkaPuXI5R7N_k7-LKatag5Zv_k9jAQSitPTjfkEF9U_y_5znI5e4y8Ynt1QGFAlwMRAKCQSUjUSuW4Dw67OypY7YUGFEeyuSU1HBVpSKQ1Wea5HAYmoGJt2ykfLDL4jTTJLIr_c8ox6DU-6h6bB-8oE3mvg36YCXkhMVa6kvf0MIheclPb2wIV9ZXKAgRJkSrSaMXAiWl6kypPwb64A6k6yEurQ1lPuqzk_k4ZfgvC-rnX7ICC6zl-iIhq-uT-xhU1jWLz4sk8zht4yhJCux1NrDwk6fy9roJi-Ou8Q0mO6pTGvzunpvSNDhGrwxHjo3TRHfHK49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZF-MgqVRD45-ES-uSWlJw_wGTh3kZXSaO61HPasFODS7GP2Uvc9o06mg0OKvSs8ROfLJc_ib3LSiV1Eml8bFYGG0fOBWTuSFEmfntMAcFhBZonIWHPIu93VDkJSQQsjm1jz_mhkPaqDFOaipwAFATOd3CdG4xFJf2jv3wJHoQ3zFMA0-NSS34VU0sHJDEaTRFMjTzfRrHtt2Bj7qjlVuwl4-tq-rQ8OF0nUzQcsMxjhwOIt0YDqYiWbJwBUnyvrGNy3DfnQCfjJ5rlrSpuEEqrUFojZETeSM4F_Ze3BnidsPiZRJ5q7EbG9zIgFiBaxhBAhotxCYLuC1yGkCsivAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=IwbzkfvnD2_nF8WOEOFucGPyBqUze4wtKBpYzpxyPJ3IwVELrQ9G4s0l_supNa_y24AF-3MtVeFxGjPMXj0RNksKwKN_fWBlPflJ4nj5l1Lx7ppg3IhW0_zvIUy8Z2LcWF0xT-tfj57Cxr786GgMLmOqnigObOpxJ7Uza30QuzO_BkQc813lWYlfBlBVavgwMzwxSpPsWhwcyujmZpW_fquPrJHuZMbGfu8dXd3JrH0o6zjQr3KQQiZ5lpTRDuAJcuXZ1Z2H2lubcvmooPErj8q-7f0u5rLz4TzRKRDsm2ECGp5aGd-02eEbxu0U6UZY6ygPHKowtRpAM03t9ZhjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=IwbzkfvnD2_nF8WOEOFucGPyBqUze4wtKBpYzpxyPJ3IwVELrQ9G4s0l_supNa_y24AF-3MtVeFxGjPMXj0RNksKwKN_fWBlPflJ4nj5l1Lx7ppg3IhW0_zvIUy8Z2LcWF0xT-tfj57Cxr786GgMLmOqnigObOpxJ7Uza30QuzO_BkQc813lWYlfBlBVavgwMzwxSpPsWhwcyujmZpW_fquPrJHuZMbGfu8dXd3JrH0o6zjQr3KQQiZ5lpTRDuAJcuXZ1Z2H2lubcvmooPErj8q-7f0u5rLz4TzRKRDsm2ECGp5aGd-02eEbxu0U6UZY6ygPHKowtRpAM03t9ZhjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=DRCFCMG1pFRpwxER4qOokkS0vP-abgofOPpiTKb-Z0vF0oRx-g8yQ56ienxT7bZ1z5KLqitwH1ITYeKNea-h9TP97LwgjDNKHaD1j-z3jstNj8tPvnjISF2BGKfQyutvQJY0GhIM45Spz4p4fIYeUnHwT1Kx67uQRJwCS0GLP6LdvuNo-lfeTl5B-6WafTtpGcrzSNCbcarPpAJIdtyOTLmnr6tD0bb9Zm4UCY5yKQM_9mwV1Vu98xCb-7BxzHYOGFD_T7KFwrt6yUI03AJaykNfZsM2qFyRvNYkddchzsRwPoONliK-FkXLdaQpCHS9ZVu8TJ24FamtTnVaYBeXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=DRCFCMG1pFRpwxER4qOokkS0vP-abgofOPpiTKb-Z0vF0oRx-g8yQ56ienxT7bZ1z5KLqitwH1ITYeKNea-h9TP97LwgjDNKHaD1j-z3jstNj8tPvnjISF2BGKfQyutvQJY0GhIM45Spz4p4fIYeUnHwT1Kx67uQRJwCS0GLP6LdvuNo-lfeTl5B-6WafTtpGcrzSNCbcarPpAJIdtyOTLmnr6tD0bb9Zm4UCY5yKQM_9mwV1Vu98xCb-7BxzHYOGFD_T7KFwrt6yUI03AJaykNfZsM2qFyRvNYkddchzsRwPoONliK-FkXLdaQpCHS9ZVu8TJ24FamtTnVaYBeXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lsDcWYPqdPMfygy5MzDCLgUv0dZ0DMaD-S6AzE7akgxeVMnrBU8gh1tdPGvgcs6W7FgbrARpHu6b-fIjUUTVIjUZuaWyMzAgdIKjq6RZAp9cV92cNlHGWpaEfmEYpoJY9CxS0BbG1YFQkD3utnQc_fte9c3GtolUli817oHygV4brLbNWrZHUg3Y_dDq2XNkJmFzxjkBpQldfyA25NrIE6Q--YDEMCZ0dvcdLeCXP15YSsvDsYkTA3X-aVAhyDhDMf5x-MiMNR3PhNHTeieQgI-puuzAc9KdaJoeihzKcnraL4oKMi6FTPR0aSNAQUlBWbVzgTFuaNikpceLE7txkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F45B5sNqsXg12JrEdpfVpcir8jyjcuK583jyWCMvVRnQSauq6Zb0RWwIReXUAYbcKQDChBto6hiFfXnJCPjYG7Dlbi1-B2CWrPmkIAmKod2SG7Elt3miDFQVl5-pkSsZYsTjVbhOz1OgKc4-DmgQyAyIHngp2LUJcDfV1r9toPxIdIb0NOWipKyFuXIXvr34MIai-wAXA_x9dqDmbH6tzjyfxB-nAWEqakmhgkAdd56D4Tw9um-zMOOR3MVkcuTv9pg33em8411DNMqFvIXr5NxY_sOfCdwBnCToL1mWDZ9X0HcBA3M87NAmetzvthp2eQeklooe1VG8BCJQ4w2xAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BTBs96N1aPNDCKX18wCcyZ2J4CxOXfo6VUxm6ncSQ2vrkl_XawqEWBM8MGSaBCmIyMEJCtN5X57X-SAggrFUPFlzQILgJacALHN5UqMQcNxVFunTFndLyxv4FZtmREdh4LfwILi7YyFlPAJY3SS1E7tUjy-mXKeAMsQgwmV4R9uIYXTIUfjfAEO715_HpXGte9ZZzH2dOqba3k01KgNtyU1wDKqXpVZX5xDQD9xMWrPopQ7GEsBxTNXtbbCKUNJW8WZhaSm9Syvu0XioF8QMbgK9s5N-5F9qToBrpABoZXgFMnWgXTLKmPrrDc_6ZFKGKdS2259ZonNZyfEBUYLLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SEIQHwWuXRbN1Eu7Lia5xJUwLQepwgMU-prF0eDrc8jwKRV65r7Ay0yFUEXcpi1LSvNK9vmEHCHx_qDUrdLD8vlbUqty3dP6NOM2wre4rvbvL6sLiasGE2_p9EatUjo6g_SRHWehbtJ9uZ3GcE-_EW_JGarpdWS5rFCtB_ZMUajCMPtpXGRkAt_R3i9Bkhg6j56_lNXWVNorJGwG7pjAVYQ9k1LxrpZxD1YwLjLGb-hFtxuz803rFX14sq4tHLHWYItqP_4az_n8LgEZxwJFTtOMWoDS_zfELDCzTfsXkxHK0rN3Q8_D9whvx7Aw_WZ5HLrQ74NLqDbsuN9Tax47Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LuDMBv18EY-IUVOMPdThtlCmCJ3MlRHYKruiBYvEj2VNSBC-2sr7nFgz11iVgOblEdpo5NyzXh8UkHWHVbPTgusPzEdBmtDi0vK-H6ZJcOGDFbpUxp6qlsHurJFn92fAIqnOz0xbHANF3bvSI9ZkwldlcLmc0n8WiPsVfokCNgqR_vUViEQL2cfbT3isYtNVt8yOF-gB7uepGwcCGfe2YkUqjErNyXePzf2ROdoLMjy494RwnNAyGREygBeJ5O9I8INbN_B3xYJa6EBYhv__e_XddWKz1gj_1mmJhAnhum1JCHJOHUOZXB0izzNvFnACgL0a6pFT8DiNI4PHd4Ggig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=BzrdsLxt5KYBOGkTyqrHUwUb8cdeDTDl6uq62gF1xpHrKctgpf8HdTv0gzkAfYWSZhMUNUtLffnBI3a9vMXjCQeFnhdC8Uo9t0k1d0owH3dGBNn_Y6sZPB44oX89SA58WQCCkXuCkLZ8Uzkipp7k4xjC8emC4thp6vYTuPIveeE-4GyAxdEgLSVZBbWaaOtGGYcbpiBJFXTVNN-LXR3EIYyUS4AXoTMm9U-_VLdDt4eFSNFxML8ITnDhqt49dGBOwv6dhVbmuc93D2scjGd8qvWugV6O5r9Jh24WmIYA_uATMhVaZuI9xAZ8yiRoGMHCMG-l4LCdoEocsE-Ik9EtPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=BzrdsLxt5KYBOGkTyqrHUwUb8cdeDTDl6uq62gF1xpHrKctgpf8HdTv0gzkAfYWSZhMUNUtLffnBI3a9vMXjCQeFnhdC8Uo9t0k1d0owH3dGBNn_Y6sZPB44oX89SA58WQCCkXuCkLZ8Uzkipp7k4xjC8emC4thp6vYTuPIveeE-4GyAxdEgLSVZBbWaaOtGGYcbpiBJFXTVNN-LXR3EIYyUS4AXoTMm9U-_VLdDt4eFSNFxML8ITnDhqt49dGBOwv6dhVbmuc93D2scjGd8qvWugV6O5r9Jh24WmIYA_uATMhVaZuI9xAZ8yiRoGMHCMG-l4LCdoEocsE-Ik9EtPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJF2EHAf4nDN5OM7NW7C1S3zR5unQ7IHUX7fT4u3d0YCYZEQ-vSVl_lfkNQXCBXfah-s7AoB5B_OJfDnOtjFO9C_v-8mIMOO4p60JCGvqhtCGntnhRO8auIoqKEBhltC9paVHbt4pqom26cspZTyki4MJ8-lDfR_lrsFGqP0U7ztg_3g9SZkeTUN5dgeRNHNVh3nN86ZbFQ1A8cpmUTZL4EErh7VgWvQAiDYTOnmAybRu0FyOQBtUbsBBOmFCJNhqNEkTdnOCMfUcyNnE09cdrkQzHlIcyEumS2gLY9JIUeCDKmFT4Eyo1wFsvE0-pHmRLvH6ETqCtOpLK_1n4PgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyiCnBNmZPOi6ESU4T5RruJvU6zFWQ5DUjGSXXMn2tzwU8312W_YqGYQri7VxNb3SBm_X8J7tXf9bFXxSs_LFTsF3SuGOMWJDWgM7GOT9jEop2ZlUZS_BteghHDdn0ntMBGG93clGkOhU1Kt92SoMuKRwPXyoSCuPrXFQexffLJqemXnNbBqlbMfIEswAHFZGQPWc4eUsyO3RMakjxsVewzsE81LE610Avu3GvrJBH49MYz5Rs8-exh-XI3tWL0f1UpOhXPZAGIh8KUl2ZCbrIQtfpJsMOV8lDeR7JascGvQjIiOFrr7cAdDl_cI5d01mjljzJ2-gskvkFQHdu51zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwhacRkOdtOdtmm8itVASJx7MTRM0IVa5qMpz_GkqHbEEcpua6uJHWKPl782CIav9qlvENUw3XmIHmcOwX3EYKTyftMefcVW8gy6w8QShPxwCBJYby4AdQavLK0GUe170mu23L4KlNFgnk7xbU4bD-pWxcO6A4u5mtuwg9FRl9ACb-CWHgweYnDVadDZfzf9uEHvncYg_yawEbws62nU8ta6xP2cE1_rwTdJEHXz0h2YRQv-zdHPWAGoCJcINgKouDatgZ5sxWvRNo9TiDEhx-3jq1ZSFyuhHRjOR7z6v3GDctZj_FYo48GUiBWAobpN-7NFQhm0xQcYMbpQSiymSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R-zWPqMv_cJRD53SCqPpAX4TmhG5mgHAGqquX7_VHKyluR018Ag2jjts9F1rmvYmc7h1UDZ8It99HuY2qBF0c2Y2RJiDraLBev0UCdTi-sDvnvOLL_RBmIHIg_pW_mRQD8kdIQkNR93mLCkFXj9N8tBgA3AybNDG2udTDNqpzfK9e1qhiYcYjdLOCx64488F2_Rt45u5AE6iWfr5Dk8EypLuGufA4iotq4Vuv820Hz-yHQ8ECkSbz9Qbt8-UNbDewQCQOlYNgn9A5wmKUi-WSOhWZl0qbcmOufFHinaz90dFI697FPd0-vuBA2m8fwXWzHzU7wK2ZlBLU9aTv8v5fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Y9XP1lVXkgGjVoormZdAMWbNH1D9fUM9fA_XCarWYFxocvha1JvFCmYgryD9LaZP-yhSBqia8C-NPk1SPiJUXNL3OIOX4EaCuAW-upIVcOKdTMz9jniD-OqAIJary2saYBTqW03fzwGxPyxEoIW5dgyEP81j2LBNNa3p3X4mmZTOaYrFCB6skBsYLkqDTPQ8-12PsckTUKG3qak6HwAIZdEqLH8PgXPx3zEmxhVolqI1PHV37LXEPsVfQE7aQ3xKfPlDq9mmMgYt-MmrDsnrIuGOfDJxYqKjU0W2RtriR0nUlw3cA4foI-Ra-NP4PJFPNoHCvZtkVvRJJid_2lng8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Y9XP1lVXkgGjVoormZdAMWbNH1D9fUM9fA_XCarWYFxocvha1JvFCmYgryD9LaZP-yhSBqia8C-NPk1SPiJUXNL3OIOX4EaCuAW-upIVcOKdTMz9jniD-OqAIJary2saYBTqW03fzwGxPyxEoIW5dgyEP81j2LBNNa3p3X4mmZTOaYrFCB6skBsYLkqDTPQ8-12PsckTUKG3qak6HwAIZdEqLH8PgXPx3zEmxhVolqI1PHV37LXEPsVfQE7aQ3xKfPlDq9mmMgYt-MmrDsnrIuGOfDJxYqKjU0W2RtriR0nUlw3cA4foI-Ra-NP4PJFPNoHCvZtkVvRJJid_2lng8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfU-dubNz6DJQgn2zbkGl1LaIVuIDdyjoh4VMc_hm-NLAgBsu04yo4ww6Lf1PG3C2YkN4oLxcs-qpY3O6ZT7eA4ITVlUdTSO2gH42R158yARZgKPEWAHoUt5c8CZrYr-vcvE33yNe745gG8s6YnTJSjChonCFIVafF-JHVCKSSmgdixTpC-fTGyvzit5akXoMVWwiGGTesYBUh7PcSY0MDKzi8S07MOT2xMrgPajt6pc1XSUIWYvpxZUh1cGuJi-Se4Gpi_QNjrutl6MWlJD4kqPIIe5I2EeQm-TV7TSG2W0UvLDDc97bX3-yWFQ8qSp5Gmp6X5BR2Cya8bT30mm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rofk1jltnKWnrpHxibijx-sfK-DwFt_8AtJFDpcJXxSE_hwMkKvrtAPJhIDwrMxUtB8rIWz6wqhIRo_d_ogsclR4GBIsQRHgN4lc8RTRKr3qDzX2m5yv9tu7_XxNZdLhZ8caWz2v9Kr8WUEMNnb9NxHS2STZaa3__cIIAd6AmggRo3sFNCTotcFv1hVGaGPZC6upOZqu_N3raKOEIbVoo0OaCDuHJay2iC5m6YOqpYIi0zAKHZAV36v27z_795pX7wSlp1Vs7Z6mlsKB3R3cCLSyOvDIqX3xWt2SQa2ulgBlCt_F2nE0XC4wPZm88NCrNU4MyIoxBXZkzVXw6TDQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sZMR7wsw77cNSY0ntZXKu3pNEFDN-Kiawd7r6UmKkwKv2_4QBSzFpvAGrYWGECaRfqoqotB0EM7_gVxDjZEG49d3d38A005OTSgL8NasaZ2e_PWAbJ3OMW39XjV5qjyGhAAGcb7NSmwtyEIbl-j9kvv24DMXmSYnaPD5rMXOzNOLeXwCQAIpW5kJ1MpZkDW4VsjEyl8vWmmWHwQCITmE7GEIOtlpOYTee8wnrCegwChRBDS82fx6NvIses1i7TjxfL5bLXwKuukC4kn2FTm0kTpdzVVzuCTybEQ1hzYKa8ZJeHf9B421W_AYQPGKftk2gKIALoNFIJjIEsfllhVTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8ZABe7SJc14tl4V831fE-2cn4NQdqhiNA-0s-MJ-3Q9eQF4e64I5ixJv20bWqa9vOVJvvPjhZgYHtp4NfMLOgJ6u3hw7xGOPo6EutLyZaXZa2UYP4KjkewOjln5FOYt_mu8Uv7XXsEs88vLdoOq-wXzUv0I6nLjqNJyM7MLKiqC--QHuDsEsz9unlPyBBjOe91gcHXqkfPc0hkBxhUYiZTiiKPYrEP59K3YLqS_O0eo46MjGtpy-PzMdNT5fIbmWDNLCmHr6daSYVyH-mMl9JjUGx1lBHtApPP-kqSd4ElfkR5NCcqQ9naViZ4iHeAEXSOnlGoOz_I-zAFM9rezpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DnQtyoIbsEMOoeLPYTPj08u-Ss2BJotS7MipEzQO-3VaGC6Vg8AeqH8Fy_3RXsiUBUUpcPjphwTBzXEcbylmPQqVdFLcg8sOjxVymLaJ9Nh9sJ4h0XuZ3fM5puWmtYm27GQFm-4tCsY6mhk0EtSANQmBZBSpiNPLPed84FpkWCkyJ5_u6vOnLxB-ZdPrzNzNf4RM1CWIRA9dwrhOGgD6Gl6YmKcqLUzn_EEcmIASMkIsnxksbv6WLFD_IyLr-ci0R31h83BwMxaOBUDfrSVJUI-nfT76zNx38I_G9kUspJi9TgGn4wH4MI9BiokNdsgxcZ1XwmmIN6K9hmAs1HvBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=TDpzg0UCSSlrM_bZ2yfhkhe9lnqnSA5qCXamDxJKbPvyutZbUnKANVWVgXS8CZtcEJwnBcuhVr9UjlM2g-z7YDVoPZrhtrkVuhWbguxLAtiuH4brs9hB0r2ka00ACuIwJVkZLlm_m5XhzE4jQ4eiN2BYYGa4QPreh2826usfBpQFc0r_gMrkUpO3bns1cAS0NmQCgt3OXQ87U-SYZ2kFQNrH__2UUiqs1itpaXtUkp5eH00pw0Mer0H7g78wM7LQacNxLhSPafOmiNInqdINDsGP3e8EUIfjtaAUQLRgzx-JhmZ9Ir4Izo3UuLK7d8EURVeFWBZeTIyBvzGTRSnTqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=TDpzg0UCSSlrM_bZ2yfhkhe9lnqnSA5qCXamDxJKbPvyutZbUnKANVWVgXS8CZtcEJwnBcuhVr9UjlM2g-z7YDVoPZrhtrkVuhWbguxLAtiuH4brs9hB0r2ka00ACuIwJVkZLlm_m5XhzE4jQ4eiN2BYYGa4QPreh2826usfBpQFc0r_gMrkUpO3bns1cAS0NmQCgt3OXQ87U-SYZ2kFQNrH__2UUiqs1itpaXtUkp5eH00pw0Mer0H7g78wM7LQacNxLhSPafOmiNInqdINDsGP3e8EUIfjtaAUQLRgzx-JhmZ9Ir4Izo3UuLK7d8EURVeFWBZeTIyBvzGTRSnTqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usjj7qZr3c-NnoAxJ-FoGO5h2KHACZdCJ5BbrvSKve9xyS0XYbRhGSi0mh9a-9HfEuuvbSey_uiK8cI_2-qFBxSwkYk1KdqcZwN0aNKyONtRrXIyjdke1DXhvZbPuiXNHLfk6lqLUfKZqewI7ywc-rHaAfe5AhmBf9Q7BwKduVTVWNYSzZP_l0rZPyCeYdIYhJPZYuL9FuA7JlDqs59PbXK9_iHQhNeEudiylHzjDLG17rB6b6NYWk7gT2Hf8tWKpor8JkjD1UuyzwINJtxpARdO9zOQAsXmaJ3g6Asd8vJMLqcXjfm65LvTKT9Sulevi--ZyHrez3IGNOVqBy3V4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUrP8RAyTG20Lp0sddgE-_bbywItLUlSQX7mJq5YxJxApSGRKpnDojk37VGDqUjR11ZoCitnZSQ5PCiTTzAUvILErwwM0vB4Bum79Kei35oVtVCw4rCnCWDXrHhssl2XxGLxJul-6vmk4WPhkdoWgkxXhSDD7BuZDGu9O9ya_6yIPtKwnwdV3foUjQKyTgBgsUD7uELqlit4nZXbELpvTC7PpBGN_rlyRIZT_RvP4F9kZ2Eax4zGBE8krccYVO1Wv0nSp2-7ITsZ-yyHbWdPA64N5dQ0IudWuKzskcV6-ftktwfnrfwXLWYuZADQCgAEFaW0ZKJDsuA-blIdatqcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=gUngqK-W32-yuSShDEYLf2VbAByNe0k00sg7TpbbQX9HRDajdwkcYRgfgKSlL7VFgP6y2TZ8bA4HHyzg-U7qghZYRkdRIjNWyx2kBavmwEfY3MgeB1ij2p--Y4HZkHKmaaUM7OthQjPknq86YQNujMRq9SlzzHeI66amo-8HpYq5_qHRMWRITvpeWRxBN4NSryfVyZK2k6Lc1Rj4UDrY4DYuR_xDabc_ea8CLILQ2xVDnyKXJEvB_9ShqZNEtXvhXtQVF8Bb_MIIEvTYu7D1hQ_shMk1aLe7g55xh8Jgt3Hvpbq7oItoctt037ION4-vIpTnj-6qlDSWHjnwi4OC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=gUngqK-W32-yuSShDEYLf2VbAByNe0k00sg7TpbbQX9HRDajdwkcYRgfgKSlL7VFgP6y2TZ8bA4HHyzg-U7qghZYRkdRIjNWyx2kBavmwEfY3MgeB1ij2p--Y4HZkHKmaaUM7OthQjPknq86YQNujMRq9SlzzHeI66amo-8HpYq5_qHRMWRITvpeWRxBN4NSryfVyZK2k6Lc1Rj4UDrY4DYuR_xDabc_ea8CLILQ2xVDnyKXJEvB_9ShqZNEtXvhXtQVF8Bb_MIIEvTYu7D1hQ_shMk1aLe7g55xh8Jgt3Hvpbq7oItoctt037ION4-vIpTnj-6qlDSWHjnwi4OC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBiG7qhYRkvngkAv_QkiRqVsUG_0ICc9-sQGCw2Ixu1jNxpUPpOzA65GIOIL9XEU5YIADFmj9AYntgKsc9rd5wfMT5wawljsNUUsz4f1G-1BuHtcQlb15ukyCSWrWoCBiyzp-_PVT9MrgU-CHzMmDSbZUMyNm914V2ZA-fm3L5ZoQPg_XO0HZWsPxU4O5p0NzlfEl6YCv6ly5OzDVN26kf4D4u4FqFMVlH2tkm_i__JeELwS-VgDpD3zd08xLY4tfGK6n8efcOvWCFMwKIUbB4h3bgERJtG_k-OMGW-LAsU1NTgC2s1D4l2lVZNAVNfvRRvs6K8MoRR19DAmo7tQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBf11S2EIlX3RNIY_jS1QNShYVHoaUZlgjGjg0mqCBB036bqaEWhfa0P7j1Uq6DYOh-TJVHBfJ2eYdNwODPUUMXlqTGJXOE5tReboWebzuXKGxhXSQMOOv3YZEXPUYatmrfb-WpcNJLoR9LSsqKylCX4RchtVZC6PQCAhB2dFBS7MYCvq4Ym94DZl0TBzVK-f9fcNyHyVGfW4UtQZ-hqKC1CfYA2l8S8W_kyNQso7wgxITlfNVtmQeXB6bngBBnEATGZ03SfsuXWhwPNrqI0N7yrEUJpyaBUXXb9BeZNu65Bo3gusyV91wn5b6q_o7jWhqQmxIBwx6VaoTQDpjDxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t_W0BMYEQ3XSFCA85czQAUZ_Xx57enMmCwKT1ub0-whe75d8C3tPb26MVId1g07QtxlX4eBe2HZpUOsGWYDAlbI-lL1JLIP2pnPqpOiyD3A79KFokkDifgYO5j2wJZk_yVYvraxhwxqItBPQtSLxmO77kDyHEMmWsy76B4XZyZ50_1V1zubADZWmRQJyEdLzt5kY_ulf8LiKPLi63EeM5z1jaWadvHysShINe2HfkA111rjfoPUyFEVbCqjioYP6UlSGpLr2AZ19_9HS2RW8JlEd1LtxTgJ7qugr6-w6Mz8nYiGuxpVKOCkI19trsek_q5JKRAHe66P53_BxBb6F3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGmtS6cOQ5zZSaeQq6Im1vWRUnHZrrg0cP-fqmy9V0v80BP3EE8QaMyi5O8PxEYoSQwP71y495BC0RKbruhYekG98-iJ5OjZJtL8Tefb41P7tAeYk61Al-dUrhNaLadwIBRNCud_s2WR0kVxDutPf53Ea4y_5Omelhr8EsilkjIGKBscT9bEZO4TyToK86Oj5Zd8Va6RMVyhCI6IlvLxIVFSiQo7E9tNgvc8V-jsI8VZVJVUeXnCZFvqZnpmv8R5NRBuLXkBSPATjHHeetGqU_MotudM9kaEVj7UdsDKDs-qQ7rbxYL5FtZbieqNd-uUCNqaLykECSwf3i77TINLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dh2GeM_913oeLBOOks_Wkehb6CHng7-mp04jZidBFT0dEWVzefcxtWnSnFC9mlmg4UMejlw5WmQqQWOevAnD0gP4g8lSBfuWz41sbJTAYXzhaozpLVUyWzkLwVvQU8Mb6nvlM5DG_G7R5nuGgnVlT4fqgX0eHH6EBGKt5rWA7zrk6mE5DHpcrHW_1YZ9EYr4rH5xFhQnOBSjP0_5hWOegM6KsSmzfJjP1ulGSiqyUkE618eEwNd3GgBFUg1NIUbPkbjqvoLoQiHQeauOhlvrd4OeXa89W7-ufAxpoW1grMq8LWpYydOmZxJoLxObQBuOnXHB0e_bOcCp9nUhApcevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnyhxvgX0b15DJnji-H5yyZtDcheKCNh_e34pGOegoZK0RuDUpu9dn814hGFvnX1CjPjrysdsyVZK6KOnmZuNOXuMP12eFUK34lNj9-8HpR5f1Dd0pxmhXYCevs3cFSSn00vNcNl6db-hkOGRCpJv5NGLQe4nhqE19jWlYMHOmXDqb2arGBtCRaKo3Jb2HTAh4Bhp8jFzs0LFT9_TsaRx1BWSTYQRtlJRlSkT1HF9YQL0WgvaC5cvP8Z4vMt3ZCmosq1RgbvrA6HxaeHun-HCIc1zaKnzNDmHmtxuKdhMpSJfSU3lZQf6IKd07BZk7K62XEDuy3f3uUBlh45lk2ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YgGdwW7n-e9YEiNyz-Snyab2ptt3KeKwLdyt0CJMeiYjkA2HA8IOQUiyO9suARMpy9FiME3MxugFvERgTt_T5HI6KmBqitrjdhb7lHjs-d8Zn1AfCaY0IqiosacKb57A4mrU7VjGEA3MlMnJSLqk8YIF6g4MeiGbfkAvZrrNG65QJ8NTiR1nWCX2BJWY3afgD7-BuuMvfin5D9yUM0DEBFxA8FyQhqNeB1q5rgy9YnJ2JBtA1qvEapgsP2QCa70sLrKnFgWMd-rtk9RlKUH6bIF6PN_IDjQBq-n9FMJNtcMRnigU64i3z3Ik6qs5tlEs2XNgq-G341S3qUfgIvlVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=rcdwfaEJ21hK7uFKLZlN9AK9C6lFSeKgrXZ4_60_XVm5Fm7OhQB_ZLq-WMq9smazEM_rRz4D5c_ydNv08lXLkax6FrTx5E5SWvaG3EatsVRW-pJ2dXbnSFFhUG9aV0KlsjVOE0dQ74MXNtH883Mt4wsbCDoQuNgQMPVBeVlkPYqaQ4ocOn4UP2YHPjm6FzdWAhBYwDclky2LmHfzwICVkSho6uyRKXxmGQkmTeW4B4ROcC8ImiSK1fwqBYl8JvmFw6_TGfWifpDObQG01bUxpzEY5qYs29byVB_L6t3Etr7EV4TNH-wlgtXGwF5EdwAobb2jw_WUYET4b8gDlrj3-mgQH5LEum2Qirw4F_yOuGtRIAnV9fO2JTTNeQHUK_L31oJEO80K2ij_BfL2XxODkGFp9eRrxjydqSHK-f3vkKC8QuLxdQbYskBLi4IrTYEwChNOyYmiyV3E4goka8_7sF0XggbK6uPKI1VfiRynQmTd9LDa1zoOn29r8xXdb4cBxGU52wkMCiJYESTZBoNk9JruxAfFKvEi_6e4hU0IgN_AXFL2RRgXaPIj6eCW8_UW9BAaEfjQKEO_o6NCixVuSHbRtOCrKDMH-s5x6fYxdsMzyjavlTzu8hMfmBXyoFUsLOve_66ta5z5tWOXgstf2Y0Neo5HPiygx_TH5U-rb1M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=rcdwfaEJ21hK7uFKLZlN9AK9C6lFSeKgrXZ4_60_XVm5Fm7OhQB_ZLq-WMq9smazEM_rRz4D5c_ydNv08lXLkax6FrTx5E5SWvaG3EatsVRW-pJ2dXbnSFFhUG9aV0KlsjVOE0dQ74MXNtH883Mt4wsbCDoQuNgQMPVBeVlkPYqaQ4ocOn4UP2YHPjm6FzdWAhBYwDclky2LmHfzwICVkSho6uyRKXxmGQkmTeW4B4ROcC8ImiSK1fwqBYl8JvmFw6_TGfWifpDObQG01bUxpzEY5qYs29byVB_L6t3Etr7EV4TNH-wlgtXGwF5EdwAobb2jw_WUYET4b8gDlrj3-mgQH5LEum2Qirw4F_yOuGtRIAnV9fO2JTTNeQHUK_L31oJEO80K2ij_BfL2XxODkGFp9eRrxjydqSHK-f3vkKC8QuLxdQbYskBLi4IrTYEwChNOyYmiyV3E4goka8_7sF0XggbK6uPKI1VfiRynQmTd9LDa1zoOn29r8xXdb4cBxGU52wkMCiJYESTZBoNk9JruxAfFKvEi_6e4hU0IgN_AXFL2RRgXaPIj6eCW8_UW9BAaEfjQKEO_o6NCixVuSHbRtOCrKDMH-s5x6fYxdsMzyjavlTzu8hMfmBXyoFUsLOve_66ta5z5tWOXgstf2Y0Neo5HPiygx_TH5U-rb1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AEz7Pe2_bl5sM2lIDP5nB2X9QCBYvLZTdBXz1LIU9W7FksqR9ovrhcOnNWGU5bFzMkQHqqZQeyCVIUuRo5Kkc3q-QyV61xZaAbVk9tSgdPKHl5O_NbrYFOn_wgycX5zU1GgtCwSCUmx3fdCRAa3JLIw0-CGg72w0qTpGu1J_LZG2jKhlRVjV74dlHbnehFQMtWe08KekxPyYGi4FWDlmtP8yZFpr_TGYgM8TO-iBKavdAyv7okhKoOVT2g6AGnhna4S7MkihaEckKWqd6WuZlbkMGFv842sLzI_TTHanNG9VJliJaVOnvFHFWwNMrdGh_8BUElZ2h3x8MvLyN5g2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tl3x8-thXHPGWU3MSyaoDBQAAuunRfDeH1Xe0b9qnzJ02gsQTvKQI4BwpBD6Dmcs5qB_TttnrEfI-uAwSNbW0BLteZoMWdu7rdtMGtMNDabwocteSw6A0nBQSRgh6oV-AecXp-dUYqWSyjGT6eiQyvoMKDU8rWIES4teNHgacnFsAlaihzC7HuNo6_cyby6Fy3Anwxq9NS9hViMihMSuEsZBeVn53aBvkI6LEf5VoQiikMxH-l1Ws8bDx11JT7etLnimuoVjz462_OgeZdgmw3oAyWvghs_27ytYTIfTXmZl7m5uxQqTKUIbrWC3P6KCESlezIy2yaxSc_8vtCUSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jJEdrpQZQ_vP9Mvksw1eyPzgM70iWPqcUN9C0cO1_btoXL4XozagH-hZm6guwFrKT6dvLDDUx9ac97aReJVIyHl9oR01cusSg17_dfoYsMzkI1EXLP7Q-upV9xduN03WQJNTSTHTHTmu4Q8R5MVwJmyr9M7gQnFnFWtzr0eN-fmZtYNqaWQg-blufhqEp4NCW5EEmQrAVaGcJ7lxVnUnl6usHfH8IVJZK1gU4-SED0vW45yK13HEXcbngPskQ2vN5-JE6qHeqZAMRdxp9xgPdScP7dKk3Xg7aT08AW5rQuVGp_YFcNw-tP-S9AP27-yGs8D_z2Bo3gGBBzxdDOjY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M7YqijRIfDTRKKpwjS3WCgmWCD9E0GLFRNg-4Ut_oDozCoCTRd4996wAq1lHmcjSsj9hANZgOwkWRpz65Jo4s1sNsbLD7r-7qx43MNm6qMZyZfuXph7jWlQxWPe3rj2dHfyFBGEbevlmrnt537K2U91-76pFxcht9rIMICjx0_NsVtSQQ9o89w4g2i4-687LmRQipGqVdKm1Q3V14iLKfiJSBfrqqZGX9NmvwBfdkSwA72EFZlVI2XF_ub6XVjzspIns-om7PIRHblDFWMTqtmIDoDObfjyX6WQyZLkmBWwWhlTV8u6LAIEnrYOSLB1ewcEPpiWMse_yaBxISBk_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mpOKP1QRF8gMqIAgNPc7V7RldsS_fSNg7XOnmDAnBws2_YogDaOgeCOthxktPg-IT1HQTjLo7ThVD_tU3MBAB4PBARGjoPFiWoKi_yJRD1xsByczfdPqh5P04TKpHCNeuzWC1JtYv4vFSKToF3AVYbaPEX9D2_MlAbdkB5tmXiymbtlNImU2V1OPDMI7CJptsyNqUoI3PZfT95Gh6v0yJgr67nsuyjGue53ZF-EmfG8yXXskbRonKzPVXHaXUEul0QfJ7gyA6XnX5qnjX1iZcZSBIdzouSYY1agTPVAswZz6V83eMiLlCh_JnpG1YgiTOxAHR6A35kQC2_b_EwCmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B9GIOMOTjl0pnR5DT6x_na-bUCBLq7_YIYldNo_q8tEjaIVDJJ_c7L8_nLGLOxXRFQq_KRUMTHel8BbGFOux4V13fN7rSE8qmFCnkuIXtFUFAIXlu6OAiKZ9rXRpmBvUnCXaXWnA08uy8m_P3z9omSgDRQ_dYs95tQMxfeLJLPf4ahsntX-Li_-Y877rCprr5jP_xDIleX8uCP6NN2osze5yc0J3mRsbLpp3dT8P7KDowqpTtlJyLD2gMpDoIGFrjQ-GHiZoA56EUvtQzSZIhaDQHy5JDyvVlK1pZkw3uDDb_R7Zs_IZTA6sCqifbKA4k8Tx0exFDd-WStKdYgRyAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
