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
<img src="https://cdn4.telesco.pe/file/Kx_TaKd4zrJt0i3Bomq0jeDAPV4aTL2dUUOs68iCJIJssZIquVcs6tUTbxxbOgHAD7L5GVLA7EG3XEZkjQZcb6UQxzmU681f2O2QvZ0nVPmYXYFRonebjHnHu3xLo7_EviWb8R4ANjcB-sj1K9_iikEnaDQdk-kifLIbtHJA9T_5ufRY99J3Xml7M5dexcUK3IKmva8aofAs1ADC8iP-p30xRO_m0negZHH6Ep33Xa3Mae2q6LLwEhp5MqOAj5P3yrnDaseinO4Bbji8ldEyyjeh3b1jcKeFBts9APGF9zcaIObFsQtNOiUME3Qyzr3aQG2cyaItXE8NqvSuvWTNGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=UbemSgIl42tRh9WnA1DNwy-nMABSS3z_GvdniT0YReGIxX3h6QiGiowy46yB7cupSkit1lcq4bswdbXMnq8MyfNGcHza30hzNy04cwVZspVuQwIql1eIuRWu74bn7IW16KoxsFqISsw3PJGgpNseOkolwzcwl2WEGpPoM5jULe9cIYmXtC37LIpl7dptdCJFc-4r_XtAOelXOVusVy834iVnE5BwztnNj1SS4Vh-NXdfdiVh_GfIFosbNYR-yuyb-CjN9uKATnUUm0Uf2qKWuDTssJubhh5SngMROzo1sKXyU6qtBkofonZ-ofGZ_c3tPgIiEVHj-B_WESAj2C7Ctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=UbemSgIl42tRh9WnA1DNwy-nMABSS3z_GvdniT0YReGIxX3h6QiGiowy46yB7cupSkit1lcq4bswdbXMnq8MyfNGcHza30hzNy04cwVZspVuQwIql1eIuRWu74bn7IW16KoxsFqISsw3PJGgpNseOkolwzcwl2WEGpPoM5jULe9cIYmXtC37LIpl7dptdCJFc-4r_XtAOelXOVusVy834iVnE5BwztnNj1SS4Vh-NXdfdiVh_GfIFosbNYR-yuyb-CjN9uKATnUUm0Uf2qKWuDTssJubhh5SngMROzo1sKXyU6qtBkofonZ-ofGZ_c3tPgIiEVHj-B_WESAj2C7Ctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرنگار: اکنون در قبال رژیم جمهوری اسلامی در چه مرحله‌ای قرار داریم؟
‏ ترامپ: «ظرف ۴۸ ساعت آینده خواهیم فهمید.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=QBA9sPDF5jmVT4e8YD3rMc8O2B7PQBFpiWRWcuC-XXQHaUz860ZMqmXBNM6bM1sje7TL6SpU85qKh6OTWwaKgVQuSACdVvxFZwkdJ_2zybHkXguykM4JYQLsVevc2W0UL735zohzkj7KrPCZfeYThoKQFt46USKJiTXWcAduKHpoE_YPKbYWljcaNyqgID14cGS13Fw8NljApdyqDzeH5dqVV_Aj6XuzT3vFimuZcJOwQyOl9UAkGBqLDy4CrAYglkb6yMv-0uMB1bsBJmmP0qGjkT2-rWeO681ZfyKADUWDKpNsSiGTxlO2bqXH9Oz7EJSqfs2DkaZfT32GSUh_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=QBA9sPDF5jmVT4e8YD3rMc8O2B7PQBFpiWRWcuC-XXQHaUz860ZMqmXBNM6bM1sje7TL6SpU85qKh6OTWwaKgVQuSACdVvxFZwkdJ_2zybHkXguykM4JYQLsVevc2W0UL735zohzkj7KrPCZfeYThoKQFt46USKJiTXWcAduKHpoE_YPKbYWljcaNyqgID14cGS13Fw8NljApdyqDzeH5dqVV_Aj6XuzT3vFimuZcJOwQyOl9UAkGBqLDy4CrAYglkb6yMv-0uMB1bsBJmmP0qGjkT2-rWeO681ZfyKADUWDKpNsSiGTxlO2bqXH9Oz7EJSqfs2DkaZfT32GSUh_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ما خیلی خیلی محکم میتونیم به ایران ضربه بزنیم ولی خب اینکارو نمیکنیم، صحبتای خوبی باهم کردیم ولی اونا نمیخوان قبول کنن. اونا به ما زنگ زدن و مودبانه گفتن: میتونیم مذاکره کنیم لطفا؟
ما به رسانه‌ها اعلام میکنیم که داریم مذاکره میکنیم ولی ایرانی‌ها میگن که اصلا صحبتی با آمریکا نکردیم. پس داشتیم چکارمیکردیم؟
تنگه هرمز به زودی باز میشه و اگه این اتفاق نیفته اونا ضربه محکمی میخورن چون ضربه‌ی اصلی ما هنوز مونده ولی امیدوارم کار به اونجا نکشه.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrkxahFiuoZyncwytOqtarkVZRAnJVxrgZt0KEZf7w16ZXSeP-Fw4LyeX9Qggb3hOcdHQa2g6EZSPEkPBHC4AZeaer04hzUFTvPAfYoKTfntBSkd88ABo3TkFlhztjn_oY8cZSbBmoRxHrYnyBk9pOsjRaokPZ0EBZCtsMQHkGpYC5x_mIULRrNRXLP3qjS7n-gf1bU8Lt4QtaCoBnrdq18uCCoQzGfZ-4Wi5H-N_xlusdoSWY_-rPWhhkEDA09Y5K8gn0hI6Pmpz1ozOWyx1EtHcQkglDopmgI6hdCTV3Dw54X8p_8C4ZVCIvrPLPjuHbP2IuUMcI_OCGSted0ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=gpwABD42asBfpAkPBhw6DL0sVHxqVz7PlB-8PBjmG2Ywux-2atoRiXR4HK7RsywY0zNHz9swZqghNBWx5_O6WGkb2zJhhiY841mJCd9Sqln8FKPE-Mb_79frub4RrhwqKm6RDOtQb36LX4HckW5sGK7qW2V_cCcziE714Puw00s8Yz83aF0FMBf2bu4eUBcAnhaDKyz7U2MjxL2TN25C_B7ESmpZAG1LnTM1QA9Q9zPWSUsuj2U9ksF99vgJlAtYMcRGNheT-NSacUiFfu0NF-9sAKTKd86ntg1CdEqCDCRzyYMNI0xhp4fMIqVO2yzdx4elS5vvSAl-EZ0l9YVLag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=gpwABD42asBfpAkPBhw6DL0sVHxqVz7PlB-8PBjmG2Ywux-2atoRiXR4HK7RsywY0zNHz9swZqghNBWx5_O6WGkb2zJhhiY841mJCd9Sqln8FKPE-Mb_79frub4RrhwqKm6RDOtQb36LX4HckW5sGK7qW2V_cCcziE714Puw00s8Yz83aF0FMBf2bu4eUBcAnhaDKyz7U2MjxL2TN25C_B7ESmpZAG1LnTM1QA9Q9zPWSUsuj2U9ksF99vgJlAtYMcRGNheT-NSacUiFfu0NF-9sAKTKd86ntg1CdEqCDCRzyYMNI0xhp4fMIqVO2yzdx4elS5vvSAl-EZ0l9YVLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbnu0cyxF39Httw8BYVtjIcrI98TiEekiKmH-hDEjyekEPIYEehKB4aGw3B3mOibaBPI5shux35vJVWkUjt0v7FXDbU7kMjeWS8WlB1XrwgoeOAWEAPS1UOzroDiEknwDOU-SePaR5riEvXa0J1hbib5YtuV9-PYgY023X74jhrizmpQMgRgvB1yJvrLh5VS8NOaHCjHyUAwCW9Um-vTBYprSJTGs-PLw3WYxIV-VLIfqdBk9TKks-4ITPYIXgVOsYZkcqQfB6vA443jreIqQuc44MyYTWGJnHd-jrU2YPkwMO4bYiH7hDtWy9mxM2hanucMcdHQ5pOVWtYtZJ41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj2kcd3VjLeM5UiDmlm7nOytO2zuritJgWspwV5aYWBpb0mFxpVj1ZhmEZj_TkOKmOPQcrLaktYId0rPvGNvy06i2UQJYgLs2EYCH7aqUpSBN-yCXUUAD7SOMQsXIGewfMOQxhZVUjT5N87X4SNhBnZD3PSjnvuOijVvZm-XOCVEYZUCYC_GR41XTESOoJvhCQKKcqjolyPtg7BSYpyLqADIjk4tH6mentSrdgccS_Kc81opREogW-O1zpUnEYMrw1V6QtgaTtnOwHq1Fcy7u9LRLKVrAHsa9MqejLfAGelw65gJsklYDRJDE2jSccCBIfnsEOq0uzZyaLMC1gBzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSMpiH_zLItJbGQElCPSIIOjtKdX36mbwiQzpDUP2icI44AGcw2l0Im44CJLgz9Pklgd3U5RACYzPFmVvLhKZ3I1nTm863PwguerDdrjTnvujmC2__pv_p2I-aBug5kiFSXJEdkDx6yrdzuEJ419-POTk-2Wv-8lqbHX2U-npOkj0U7SjD-ZxYi7BGl2q4UL3ArajhXIISJqfudKw03pvcwIoJieFEvfZ6z_JeAMbiO1tBvJdCYWXlIGp4LSvVk6-_F2CNGd8z5tQOTrCl0fBTDNFbk0NXhObVNsFG-YrwH4TaJAykJQt9ZrLmjxzIyntkndwjgeBSfGOWWDmQY0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfv-J9MZalTzQTfhV9_V-hJX4Qxhacr9k3QPHgY89vPXCJW-wN9W-ipA45FAq_EHDbDd48qzAui9QPk5232hdqsn2iYayPPSJboJQwng6QnJAlEz2tB3KBOEvLJhHGeLKfTq5-A2QWeF340dvLAmpRLst_4G6bzfXc5kvMeN9nYc45vq23cw4lABXyGXj0S3cN4fS030TQf7wlReBYAV5m3qruvXMYZ2w1miWwYyT_jtR3wuRvvjbfHm3CaArE7posxet0ojI8MTzd1JrQzCGN2tWwLU5lE7dNc_XgzVDEJArSe3PODhQHbfxM2c7oysz4FKK1tTmP8dH0CddhLKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Ead4b91G-CecI70shpFryuaYMqjCpN4gaJwGDwru3U8_oVC0UmWP4xxQjkS9gYOkZpOwAILCYobBtAA3y5ZqMKWypXLnJLektkKVlpnDz_iSxSV3AfJUpUnSUzmjUEcWexSvGi2UJGSkQsvQYreX4RLPDbE7pbCrPVapOFJrFHsUj3o0lxyis-KWcymUcmk1HyW5vmHLxcgegA8iRZW8uEM39IiEqnhlEMyNa6rJHyPMgBuRSV5ruSRAKOnX3ac-WxuJaHL0yKZ83XCr0ERxRUuOsXWkVDPQ0MAChEwaMQyLTr1U03-aknQ05U4oqnLbM51tRavh77QcWEMbyMKVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Ead4b91G-CecI70shpFryuaYMqjCpN4gaJwGDwru3U8_oVC0UmWP4xxQjkS9gYOkZpOwAILCYobBtAA3y5ZqMKWypXLnJLektkKVlpnDz_iSxSV3AfJUpUnSUzmjUEcWexSvGi2UJGSkQsvQYreX4RLPDbE7pbCrPVapOFJrFHsUj3o0lxyis-KWcymUcmk1HyW5vmHLxcgegA8iRZW8uEM39IiEqnhlEMyNa6rJHyPMgBuRSV5ruSRAKOnX3ac-WxuJaHL0yKZ83XCr0ERxRUuOsXWkVDPQ0MAChEwaMQyLTr1U03-aknQ05U4oqnLbM51tRavh77QcWEMbyMKVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCmrFmb9DZK-_c6mJeoLNrzLZFvfOq1GgUbYGvadorg8fAcqqfc0312fNAwJMdRYG-DAqPSv0buCrrtqhdAWHtF0lw-GCoFcpDVbG8RaDltYZT-iGWhE7jnppBzQT8YWnfLiswXacVKdsMKUr9cG7yoV5SMrxAke1uj8rF-mfJnzvXBQiv6qI_mlp54f2ZT4ZqZbvXlnwAYTio0TldJZVzV4T5RXz3L_ROnwH6b-Ln7jtuyMSEVj-a6MG1lvOiyoBEhHiEltip3NyBlABCElTOiriMS_ThbazTXtx8aZcvEAavCtcFekkwlhE4duVW9wZi-CSPH6W_tf2OrOF7Km0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=Pcu2oJ9Q9QiV4tD7IhCR6W3mHklRWrh2joJeoR_J8fMaH57ZS2PWuusktXC9oJh-gPE6v_5FelvLAlnlwnRQ5Yhwd0Pi40LzwiCOhEQZSyvJyvEvahiqF1TqV58W4OkdedFNv91ItzJcC8SFAk3RBzGE_i-Yx1prDlpqBUrptnzfiJ22G-5I-LHUgE3dl1MT8cGOt8YWHYXSaPjrCiOadcjwol-pMOU2q5oc24Up1FkQ8rgyg5-PVZm-ilx_hLKfVBdF0OqqhbYdS1mgc1nL-exznFn6Ja4F2LL-Lu_5GOZJS75gPHdHJ7srzE-YkeXwxis0hijgTwINC5bdd3vb3ix6QnTDxovewghGZliAUhyPcJRHkAneas4tbxhwBpBXKtJ23TFymcMjCqciv6Yt56egAI2YhZBnnt-QCh4jPcufMnt0mu-ll37PjCGR3ZZiq-2RcZxb7Oj2kEI4bFt1Vl3NJhur72MQjUQLtaNCTw3VKTbNO9ojVTQL2WE-ZwemYj_uN_D3BahO7O4q0tMNNF6s_VHNgdQ7LbQCrr-ndw09CHQcAwsBolUmqIg9hBvQ6IsbpbyNJ-PUQdYDeIoMZgeQJHPB7FAfKZyKIK002C2xZoQw8Ykp2qstRyghfJxdhsAZu8-4hxqzwBeId4UB59TS0NElatjv32BEtjlHPLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=Pcu2oJ9Q9QiV4tD7IhCR6W3mHklRWrh2joJeoR_J8fMaH57ZS2PWuusktXC9oJh-gPE6v_5FelvLAlnlwnRQ5Yhwd0Pi40LzwiCOhEQZSyvJyvEvahiqF1TqV58W4OkdedFNv91ItzJcC8SFAk3RBzGE_i-Yx1prDlpqBUrptnzfiJ22G-5I-LHUgE3dl1MT8cGOt8YWHYXSaPjrCiOadcjwol-pMOU2q5oc24Up1FkQ8rgyg5-PVZm-ilx_hLKfVBdF0OqqhbYdS1mgc1nL-exznFn6Ja4F2LL-Lu_5GOZJS75gPHdHJ7srzE-YkeXwxis0hijgTwINC5bdd3vb3ix6QnTDxovewghGZliAUhyPcJRHkAneas4tbxhwBpBXKtJ23TFymcMjCqciv6Yt56egAI2YhZBnnt-QCh4jPcufMnt0mu-ll37PjCGR3ZZiq-2RcZxb7Oj2kEI4bFt1Vl3NJhur72MQjUQLtaNCTw3VKTbNO9ojVTQL2WE-ZwemYj_uN_D3BahO7O4q0tMNNF6s_VHNgdQ7LbQCrr-ndw09CHQcAwsBolUmqIg9hBvQ6IsbpbyNJ-PUQdYDeIoMZgeQJHPB7FAfKZyKIK002C2xZoQw8Ykp2qstRyghfJxdhsAZu8-4hxqzwBeId4UB59TS0NElatjv32BEtjlHPLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=iC-u1m_hT-CHR0XrVvvjNhG-ZxSuRDj5UbgJ_Kb-63p4BU9Xy5QRxVB739QTla7p_1BOi74CXnz60IuphKIx6tsQtF0tXAOz5goICHDrVUSPBuZy0NUpojJssHYm0DuVfgVeomPeyS8PMaGhkCpU8GzLoZk2ryofwbFVa9pk0gnp-I9Idlaqv1T_daUj4G5CMsuBhWZ1_J-Gw2wOoFg54_CbbQfN8A0eh_qWTsg-srWaaFrazMbh365YZvLY5K3EzwaKxYrwWGKXS405-LnSWDfMEvBLr7Gs0V75FjdTbQCWnm3K_4mtxHXR2Z_SZ7XRl_ct6RTkhKlpDGYo9dC7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=iC-u1m_hT-CHR0XrVvvjNhG-ZxSuRDj5UbgJ_Kb-63p4BU9Xy5QRxVB739QTla7p_1BOi74CXnz60IuphKIx6tsQtF0tXAOz5goICHDrVUSPBuZy0NUpojJssHYm0DuVfgVeomPeyS8PMaGhkCpU8GzLoZk2ryofwbFVa9pk0gnp-I9Idlaqv1T_daUj4G5CMsuBhWZ1_J-Gw2wOoFg54_CbbQfN8A0eh_qWTsg-srWaaFrazMbh365YZvLY5K3EzwaKxYrwWGKXS405-LnSWDfMEvBLr7Gs0V75FjdTbQCWnm3K_4mtxHXR2Z_SZ7XRl_ct6RTkhKlpDGYo9dC7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH3AWez-0_K6d84JArPeY3g2NGbhj9W1cZKs1oL3APCM-8VDpX-DwUnplUUZAHSySRtJuzgs1ZAL-0Koh8rAZuSJjIIIbPcwRfFsXxR5etIcYWNFqSYeSbrHHkkHVdqmn97rL6yEGzVzX124AVURmmfdbjnjdrxHrfkWp4SLsBfRLZsBKPrGqASO5S8TDLK2cPnP8wywwYsgoN238Hr641PJLY3psS4cAjcs7QtujRKLNyHb7f3RLdanMrpwIxc60tokx1af-Z6TOjUfOntdhN3zsk-ua4kuYxQnHsG2rZ2esB2KTCTUd8rpG_Bjf9EUoFi5XfyXo8SNdq1hOHIOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=oqSrp3R3YZPMDx-E8lr35uLI7ffVqGDZace3tro1JQqgQ77rNZv9jmpJCLzb9BDynzUmDCPjaosfbolTUx71ALjw3n3fFAD99LaB2aYa5D7rhs1ipNEW6YLBtg3S1rCvXTJMd8roOJI85wX_MEAxeSrYi0LTCa82etpCj8998IGaob7H2AABd0cyHSbEGaJvrI0gt6gYExW7QgztUehtjduf7FR5gAfW1FdIDI-hMhrJMWzc0CHotMZDW31neEDZaPZPGFyfMw25n4ban6msutqiC1y4WvabPbvmQSXZZNIwEfj6hWs4PoC19p9p2iI2P_EG4pWoVrXferuSQEPXxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=oqSrp3R3YZPMDx-E8lr35uLI7ffVqGDZace3tro1JQqgQ77rNZv9jmpJCLzb9BDynzUmDCPjaosfbolTUx71ALjw3n3fFAD99LaB2aYa5D7rhs1ipNEW6YLBtg3S1rCvXTJMd8roOJI85wX_MEAxeSrYi0LTCa82etpCj8998IGaob7H2AABd0cyHSbEGaJvrI0gt6gYExW7QgztUehtjduf7FR5gAfW1FdIDI-hMhrJMWzc0CHotMZDW31neEDZaPZPGFyfMw25n4ban6msutqiC1y4WvabPbvmQSXZZNIwEfj6hWs4PoC19p9p2iI2P_EG4pWoVrXferuSQEPXxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLlidFBQtBIN_xyNL8Sd2FAk8xi1wePFrEIew9mRrJBE8AYsyuh3phojvlR5_g5xY82rXnuzIgN3IdOltEZyrKVO_5Tvmu-TzBMUjQ_grDBAoEtufCgmgFPEuA5alyqaUJTZuZOC_2XbVoep9NlbdMIRC9qUBZ2oA_-Vrd3qyhZOX1lrnp1Hpf72MewPCeyGb0TrEB5P8HPfk9Q7eJgXEREQ-q7JD53YK3TzCue52JaFgX29_bHDrTO-ZJYQr403m3NFvEuH9rFzMwr_k8al7F2z4htbvTrg_shJ_vKsDSayy9-dvT9lcm8TwEbA62iK-rV0d0vzOSy95eSjT1m4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=kYwG9EixaO9hCVpJYUGCe_61sopwhDlcrIoztmLEHU3MVGeI9r6ba2CFe0SDdjXBMht3K0dTlrsTBRsegc1BSDaSqcatsH6Sy6025_T--fqu_0xtEyWK25o4TLQ06jt5LuzZ5Ne6qlmjGpLYWc24ShqmWnGkedKcRbbn52QBOiC2FvYru3hCPwMrG3_XSdrD8PSoxbvcq8kMD1fL7Lrmmff2P4sxDVmzk7xpoyFjlk8T-RZvW1h5gOTc4qnJxWe4aT4O19lZbzCoXMGrn30YN1EF-E9oMPCEGOoaRNsVGQaREuP-fC5EtqcdJRWTty8Km4FHA_IVYeDH659_c-JqnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=kYwG9EixaO9hCVpJYUGCe_61sopwhDlcrIoztmLEHU3MVGeI9r6ba2CFe0SDdjXBMht3K0dTlrsTBRsegc1BSDaSqcatsH6Sy6025_T--fqu_0xtEyWK25o4TLQ06jt5LuzZ5Ne6qlmjGpLYWc24ShqmWnGkedKcRbbn52QBOiC2FvYru3hCPwMrG3_XSdrD8PSoxbvcq8kMD1fL7Lrmmff2P4sxDVmzk7xpoyFjlk8T-RZvW1h5gOTc4qnJxWe4aT4O19lZbzCoXMGrn30YN1EF-E9oMPCEGOoaRNsVGQaREuP-fC5EtqcdJRWTty8Km4FHA_IVYeDH659_c-JqnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeblJ-htkEUZwZ-zabF-LD4DvvUpLA0yKioyoIjb6ut927uCV20PWDML5dLqlVK8U4vvlfT6GN2Trb8RmidNIno1YBaNvgT_-qOhVk9Aj02z8GqQCKxRplNV5uLNC-alStNQ1E49qGU1Y4qRdWu_xPwDm5koLFcdL9AqQ6wQi5toLq4p9lLjp1RXLprre1IpXQbGg6h1d8tLVf29ZPmTrHHCVf2FvzA1nh1ML07gKouyC4vLOgdkClEt6WDwv6iZFvfhxJ7H5ML42vsnI1UsL8ejVNoOB5oAsDsgqsi_41aA6RpQzBzGaXkz-NKn2NGlN52rHygIO7_vliS8vUmVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=VUFiCHZ5m2afKq-b6Y_DvwolswnKStdunlkYxehhMPzWgO5cQ5rJLrrubE-bNYoWtb5QkSB8C5RSLlt7tWhS-hKax7Zv3aDhl4ifVqKrpXrvgxZpNXeQ_kZbWinhxxvpSl_63u9BN-x6wGgkYqOKYIxuATa70QhH77p-TAsWc_BodNwVrLHhgjtTNPGTnMRR45NcA6PIhXmFpK1RYJVhF0FkijSYatYXU7kii4u_L1NSsr87HKIotffQDP2iP0cERKz3w_pNSmI-7qZsyurHJQ7lEg2tuTizvRkA4XueH8p_kjw6ld1w-G6-4rMwfXArX0rSpAtALSG4OdxeLUGyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=VUFiCHZ5m2afKq-b6Y_DvwolswnKStdunlkYxehhMPzWgO5cQ5rJLrrubE-bNYoWtb5QkSB8C5RSLlt7tWhS-hKax7Zv3aDhl4ifVqKrpXrvgxZpNXeQ_kZbWinhxxvpSl_63u9BN-x6wGgkYqOKYIxuATa70QhH77p-TAsWc_BodNwVrLHhgjtTNPGTnMRR45NcA6PIhXmFpK1RYJVhF0FkijSYatYXU7kii4u_L1NSsr87HKIotffQDP2iP0cERKz3w_pNSmI-7qZsyurHJQ7lEg2tuTizvRkA4XueH8p_kjw6ld1w-G6-4rMwfXArX0rSpAtALSG4OdxeLUGyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdFmyGt9GO3zYLkQxIytHcWGus8Pw9tcIFIL8oses_kKSvzAS6vwtczIoMBUNb8TXtnYc_ZcyTYCJDw9hkW8wgpPwMsuwRBgjrf63FxxSk2djvHDy4bTlFQ0cM41J65OXos3ySyn4GQ3nOiRFQrHgtN0Q29qvvMblixOr0yAmAdmK7Eqz1WFksd4m2rw4782_jcaBVsZPnLrAz9xEAHGW4Wq9yy8BEIM6fFjwjPxEGmkVfx2jgUvREiCee7UR0s_00Vj_vC3RK7o0O7zlT42GhFFu-WJcud9ToFL0VKRIEYcOJZ-sz6O0dIBsWnMIGjO_O8ubYqIol3N4zIOjknxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=vdTox-1kr38TFDRkIfNvjDcE_hNW9Im1mCi2r4fTatISE-lsk5l2gLFjQhB3UdAV4vqz5B28tgT39XtFiuyNzb-e6wqtHudoyvKnHieWe8G7obQ8hTgfaag3aWVv1qifk5HwHI2xiCEMf--aWsDkurB4B17KgK94_WzNl7TraByf9XDbBs_aP74RHsfxj6JxOg47mpfuwwRl7DoG_eVyiYnRYpJScfp7r4zx3PjAABBZBsS_or2EsK79nxFBHxgMqriO7m5lRw00hxq6ZnLCMsfEFyS0_sSz2fLMQYq69iDHDp-1-pxlG8d_VFThHBSWWBciOJctdLI3_m8Lft_Aag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=vdTox-1kr38TFDRkIfNvjDcE_hNW9Im1mCi2r4fTatISE-lsk5l2gLFjQhB3UdAV4vqz5B28tgT39XtFiuyNzb-e6wqtHudoyvKnHieWe8G7obQ8hTgfaag3aWVv1qifk5HwHI2xiCEMf--aWsDkurB4B17KgK94_WzNl7TraByf9XDbBs_aP74RHsfxj6JxOg47mpfuwwRl7DoG_eVyiYnRYpJScfp7r4zx3PjAABBZBsS_or2EsK79nxFBHxgMqriO7m5lRw00hxq6ZnLCMsfEFyS0_sSz2fLMQYq69iDHDp-1-pxlG8d_VFThHBSWWBciOJctdLI3_m8Lft_Aag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2nuZKaZV6JbZZFQSV-jJpHquVKHDoh2CxRKsWEbNWiokC68RpW7jcAixRI_YZLt_1lGQEIFBu3_W7CcKAXdhKpLwBuKXfFVBfBKqrpnBR1zsrckKRNDyxppRj-e6c2GhZsbgISLljcGRssiOechiaI1nPQ4ADNnxh4GdFqoRq7wm2pxqJTr_pny3_U2fwVEx7ryCmQNLJrUh9y8y7QtBuQdr_bKJs1ay1eHG5p8tmSPicWYT7Vvv6XQwoh-zP8EFa-csvhKxzo8-F_Aj1opAKBZ-GWDsY_B01Z2JW7rPWYbSThYRTvYvyKQCrC--qJ6N_79l862Ixj3I2RD8LQ6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnjEus29AJAGZh_Iz8vpBJEj3vb-p_EPiRwHSSRsyeWb2K2OMHs8c08v5newvs1BI3ksYA2CMvWHt9Gai7gJHDzxwchtvScHWn1yx3p9PcBIh-D0ujmoaKYOmoXryCa6HbcgaxsNfmRl7oFzZlZWSbY1ByzGFdmovkzABhjwMk5gZBpeCOet-igB-rTwVr6zTnjjeCpOgL_OgOpQyzmQbgi3yXhX-1Qj-xjCDRYu04eFSuYY-mVyMqWfm1yN6qPyeaPSwo52FRKN9RljEQzu0uR_aHBTHdXSvPJJXd7LLa-mB7s6vKYhHLB6Qj6knbIt8D-KXSXhneQgyN4jenuu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMy3BukSdpVdOjvC1ekQYnFVXjS9CPuBQsRm4LjSvm4sn8ejumeY2xZfJxuRNyT4zaD1N1yOvBNs7SYBAbUv1T7QAtEVrNkM7x-8I9pGMXMVD7rlhKwAfgrCGGPAl4CvkIeUCgxvL9xRiaFclVuMbofPP10ly6-NWz5D6XhTowS888TWohVrj6lPiKsx00NlTqo9tOrl3CeXc5ZX2OnViqgw-7w9PObdImbl1ccZS_kxa24_cpUyz7CC8ADOqgv8Xt6s6oFhbMxWeethTul9V0o9cb2NaHFAVn1vE44H0YRiOH3qoYAcNmE1hMvbzLSR-XneA5tP8CkzmQYdnJ2nnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgGI0aisSx_g2qt5VYi7soGJamEKmbRivU1-u74HJ30KMGvhK74TH7oqIvCtmG3wgyIGhFeBfXjLAN8szWaDzFbFgoSbota57zJmfbHFd7-DTY2_L85Mp6eRDxHDX8U4We5a2KAoG6s9M494YYEdgnE_o37oqSZy9slhkSZrj_BMwp3r6NGa07_EkSnMqU2281h5r916Tbdpc-toraOxiEBNsSQLxyAaTEdq91z-H3IRUdVAj3y2z24v8AUQOXLOFmArIMJu603iDjnRAtZ0zXCC_84rpHt6x77org_IEYR4j32XTVWfpuAsz7RDQgP-1dUEdXBCfu4MHAfaBEuPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRTzr9sLSZb1VFV9cUhfJ97kjrdtIIsfnN93Z96o-sxpTXDxt0VTqiyCZDH-zMWtUe49jvOazpdm0BYasY6h-cgPzNt9s7o8eFQtKkc3FPn3oZfwAq8fMu7vrKzxKB1gJLmx2PmOGIUbsb04u9ujCFm7qyeM8CFY7ATsOOlcXijVLM9cvRad9Wsvi0UPQzEjBzNr2fBIbT32DFlCP_E4iqF4A0l5zh2J8vIM1K4P3BNIW6HO7pfmatvW0kOdwygv7twrJ1lwvmPRlg_P9M6pft8cnm_Y4j6G2ApDXZx6AoWkZLQHFpYDc-QzMREqaGG5MfM8sXM5i0w2yIIUF3Hbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwP5mEtA1J-p9LaYJ3w2Fqc-jp1-3tZHwD9HnSfIhsgXwE1mw4PKVYzZz-ldMBqP0KKQ_ucQEZ-liP-a2O3rFPHF476CwiP9Z4sbkfifTHOYgyTiJAYtmO4NOdTMp60cIFhoVZkCa9fBNlwvucyoA7xLtAW-aYlPT-kib6mO8Q2czu6HP8iLRR5sFAJBriwyl1iuopBDC1c-Kx682cSOJqRLSwwAW0z-b55e6jwL4I_z57dlw-LuX_vrSemq4hcv0HQI0CZowvItwhFBvo4-czXgOfN_XW-_ceOkjxVImR5tZdIfENvTm5ZgWAXZhlOdxC-zG68GmR6FU1BesCpFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاکهید U2؛
شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید
لباس مخصوص فشار بالا شبیه لباس فضانوردان
بپوشد تا در صورت افت فشار کابین، جانش حفظ شود.
با دوربین‌ها و سامانه‌های شناسایی فوق‌پیشرفته، از صدها کیلومتر دورتر کوچک‌ترین تحرکات را زیر نظر می‌گیرد و ثبت می‌کند. با وجود گذشت بیش از هفت دهه از نخستین پروازش، یو-۲ هنوز هم یکی از ارزشمندترین چشم‌های اطلاعاتی آمریکا در مأموریت‌های فوق‌محرمانه به شمار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20444" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwZXm5hKt0iO1XOduSbJtdou9hYzMPO2872XFqWMce9UlqQwjUdA7-w29yYmcUu8WE8RIbKGdr6DCP1_O8tjAY5hQlUMC8utGClwnyoeZr3gKwITZM2MaT2ovw71QIfSNeN5CzMx7ycZ0hk3QjwXWFXAdDUVSykqscxLe6juXDo6AwcrgNUb8OVAorq2_E0XxIVOGcwh0QmtcFbk5vs2Ml1D-GjwxJcRad5jVEN2Xp1tufyVFLvUlvi44Kr3bPmGXuMcCx19lEvZWTYcr2EpqfoRjoGKV3jke2dSbOQ2d_1m4M9vEPR_M_cvpRugxpUrZaLmvUmdhwU9tOOwDhe2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDUZtv0Hu-DtI0sShIT-v0y-z6IJI-PhMo5EMre1P4R8ddfu35JMZej76qABaILsmcRow4vNgVtO2m8p3X7lAbwyF6KH0sFQtsDDpWS39LjZl4gYggHs3i-ZubVivLMDoYGuQXAnXa8TkxZmmutd1kRIOOfKdBsSvn7x0x__7V7c162C7ip_TnfJicqKA_Vye3_SyAYuIvuGH7NrnKy6XCcfNUpV2dmb31FBlBY0xMCsmu_GsW0taspoEHb9_wvr6n7-QUfVpSPoCCuWy07-xzWIzFxXQBDpjqTSPTCtVcPM0FmUC9IVqoy7IOT7xfEOgSTunanyCN5EtQLcOW9H8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2E0En461Mg5Fp0lM9OLn5A_hjgHsK4Qx7U2hKg3GBvKmM30sGjL48iVsJwG6x5LuWBgaerYk2D9WVGvmouy1mUmM42q34tKA16ung_KMil3LXZUzP3tk53cUmHO7t7SZOoRS6yogVEnV7SOE6efPBX21_HdZwVkxgYis0pQcZf843Yresdyn5fd5CCwHgaYtePxFMw78CI-FZ4PPSEz4V2W2hFQWbeihj7IpSoDzPOm0iK8kEfKJ3MFYrHRej0PT1SvgFqfK1adtKC0DoUj1QOCd5H7ujSkn7QJqgXVB_DWg-rwzXABuG0W9XZFY3umI5USvCOOyy9hIDO3qIo19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2VP76vkb9v5OEz7Ml1ldHzxUEJZNNfNP7yhgbMO0pHedv13eqd4uHFvSf3t4h44n-zKjHWJ8V8-eKDeNS5meDYXoHMPmkNqehE1L1P1OIP8ZElh8N-XoNbgnoRVpkxH1qtN-3r-hXQEcldSoQccCPn56nQFJ7up6NmRcV99VrWIqf8F4jzREr7K9zhukwBD4EvjEDZNFF_4ANxUKrSvXzClCngg7AwCKiubhC4UIa8sTImtvbIoLryVrUhGArCykerF953ZSFS1HASPnZnV9NE8jWEDJcA3k5qqM9Y3Kp10R3Es05vNsJntlXfLLjY0eM4MAJrShEmJgV9LbEUXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=FHNca36WjzKt_wO7-obmBqeuJlyMRdThdaqsI_JeUijFLKWx47G-E3IPgbTUrIrV9adxoyElDM9oa9GOZqRQttCQa_ELZZAXzJuaLnj6wY26FLz0GHG3JNtGqyTe4STeNO9vWpNmNbBdr0OLxduEidyzcunJfsgjKgSFl03IP4I8187iISUHcyokRI3EMQKLlRESXBmnDTblXC7ieF6qww5in_n1RU5NHPOR8wBxbt6nOaulg58QfNFdbZV2uaEiy6eb33R3jzl5e8FwK8wF_jgywloLxAUspa0pvgc_5am7cvCoEUG0-EDO2w5Td9eUoZWrWjvZ0FgnZGhuu8q0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=FHNca36WjzKt_wO7-obmBqeuJlyMRdThdaqsI_JeUijFLKWx47G-E3IPgbTUrIrV9adxoyElDM9oa9GOZqRQttCQa_ELZZAXzJuaLnj6wY26FLz0GHG3JNtGqyTe4STeNO9vWpNmNbBdr0OLxduEidyzcunJfsgjKgSFl03IP4I8187iISUHcyokRI3EMQKLlRESXBmnDTblXC7ieF6qww5in_n1RU5NHPOR8wBxbt6nOaulg58QfNFdbZV2uaEiy6eb33R3jzl5e8FwK8wF_jgywloLxAUspa0pvgc_5am7cvCoEUG0-EDO2w5Td9eUoZWrWjvZ0FgnZGhuu8q0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=C4lC8W5P2x7F8v-SCHEDCzS8VID_FJxBGhfJlvOUz5YxX_DiET2j1-A2T24EUqmHOdqEoZztaOXgTmtzp4oqo1ds4JsGEmgzp_BgekU2368jGqU3J4W147vSEJR8mKMd3Ddjb9hEYUTmmnwCbo-hjNZkasIcfpE9LYF2Q2Js2SDEDFH43fg4Zil8tFzsnodKxLDrkU5WKjky53XjILBTC0siZoTKl-R6bxCEsXSQ-CeZWmXKw3W6gR8qKJEWd5Vw7005dq1hzBdkxpq3xK8JAQWwXmtD4uXM98sBlwTubs2q5erIoR07CYOuIU7OMDp-AhV9pYFCryJClJUfhZ_fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=C4lC8W5P2x7F8v-SCHEDCzS8VID_FJxBGhfJlvOUz5YxX_DiET2j1-A2T24EUqmHOdqEoZztaOXgTmtzp4oqo1ds4JsGEmgzp_BgekU2368jGqU3J4W147vSEJR8mKMd3Ddjb9hEYUTmmnwCbo-hjNZkasIcfpE9LYF2Q2Js2SDEDFH43fg4Zil8tFzsnodKxLDrkU5WKjky53XjILBTC0siZoTKl-R6bxCEsXSQ-CeZWmXKw3W6gR8qKJEWd5Vw7005dq1hzBdkxpq3xK8JAQWwXmtD4uXM98sBlwTubs2q5erIoR07CYOuIU7OMDp-AhV9pYFCryJClJUfhZ_fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=lLModi-wiKIZEyMFZYLXydOoRMs1RrF9clXrzoFqzdqQbDK0KHOhJNlYUYVHgZxQn5cg4jBBOVWAWWsIjQK9Udb-B7PodpLTAlIz2d6ycReks3zI52joufv-7-z7NDQG7BDbPdAtOpyfn5CRTj2nVZSiTpMg3vtMTNVuz-TyznWDpsBFh89xNfVXi_QhF3fdAoNkunPOBR_DXz94iN7gFWASQxU8VfWxKEbK_Gr3S_kr0gKuLvmMuiB6yIu3UEoYtxLjB8CN4m53qNhMjNYpEtgez3qu_2zB6ENSqmcJYASCNxveKh8kEPfUhpNPLMqFxRBcFw9SluJBIlyGcCkhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=lLModi-wiKIZEyMFZYLXydOoRMs1RrF9clXrzoFqzdqQbDK0KHOhJNlYUYVHgZxQn5cg4jBBOVWAWWsIjQK9Udb-B7PodpLTAlIz2d6ycReks3zI52joufv-7-z7NDQG7BDbPdAtOpyfn5CRTj2nVZSiTpMg3vtMTNVuz-TyznWDpsBFh89xNfVXi_QhF3fdAoNkunPOBR_DXz94iN7gFWASQxU8VfWxKEbK_Gr3S_kr0gKuLvmMuiB6yIu3UEoYtxLjB8CN4m53qNhMjNYpEtgez3qu_2zB6ENSqmcJYASCNxveKh8kEPfUhpNPLMqFxRBcFw9SluJBIlyGcCkhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «از همه شما به خاطر حضورتان در اینجا متشکرم، چرا که ما گام جدید و بزرگی را برای حمایت از خانواده‌های فوق‌العاده نظامی های خود برمی‌داریم... امروز، من یک فرمان اجرایی برای ایجاد اولین کمیسیون همسران نظامی ها امضا می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20423" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=qwQLNVaku6nVmAGRTmDnjRdvwSEiYHKIPuI18wwQ0BVpszmVtEHrgMofxVm_tgqG71bBCG8o8dgBNFEAv-s7eh1Bd6yLbt-1XIOVG_IdgTiC97DVMp2tQrAomuGZAyaelCXqjqwqdXtGigxtrNacX7A0y-FWHeXu2J_wunWyInlqIrupOp5rSCqYvmKMf4DdD9n9OPGgLLyVz_NNYlmiwySQxvKKu8kfhSPXzUzoWgmPyExlmmh9lF52UHY0-tFxVt_wC-mpWD-yjbOiomkwdigc0lJw4Ure0EueEqiNGQf946Tdu7jv25DR0cw4AvC070gwDaGe4CFitUm-mE2RYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=qwQLNVaku6nVmAGRTmDnjRdvwSEiYHKIPuI18wwQ0BVpszmVtEHrgMofxVm_tgqG71bBCG8o8dgBNFEAv-s7eh1Bd6yLbt-1XIOVG_IdgTiC97DVMp2tQrAomuGZAyaelCXqjqwqdXtGigxtrNacX7A0y-FWHeXu2J_wunWyInlqIrupOp5rSCqYvmKMf4DdD9n9OPGgLLyVz_NNYlmiwySQxvKKu8kfhSPXzUzoWgmPyExlmmh9lF52UHY0-tFxVt_wC-mpWD-yjbOiomkwdigc0lJw4Ure0EueEqiNGQf946Tdu7jv25DR0cw4AvC070gwDaGe4CFitUm-mE2RYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=LWQ1Ea3mvvi_MteYNtJUNe_neTZeFCiniRYbNsenz1TfUM75k6DcGdxKLveyoLp7V22Kx-Zn1zkoay3sN1r6EGnVUthjVkAm3nS4VxA1p-jq9G3BfakmuBbsjAPGQxNY8qgpBb_lR7gAORZaAh8loIFKaaNDketumHl3R9NPOXgyr-z2Rzl_lFyBpBncHKg-ueVPv45TGXf9Df09rXOMHvv0u6EiLuI6OvtW4qQOfmq0SYSjdItFgw77TBLjzNUrr8JVqGSNBSItzxOnX4KOQyVvAY_xkpWj6E12xX-ZSsDfoNcP50z17nLr_FpMB-Pi91BW7MMvbYjHcsSz_Oe3BmhsIYRKlsjKeErdg4EUZf0ZaE6TeoU2NRec4QfVcq97IGi7MUHFTugLubwyxOMOB0wEYwY1uiJwc8QM5oJHSA8QyVCIh1UIMqq6by76J9b1SVOP2lHMn8vVy2eoKiCii-amNWpS2oA7O5ipanz_MUHzUtZP2jdbvM6eytlgmPHo_6NLby8Z1V2F2GoccF3POHthI2fE55ktzfV-6GjB4ZsK4DT5VJKSOZeghit7JakQ7Je0WBJ6wPBEhOPEWTL7EcUTxqZS8JJiEtFrtCk1zOX7kWfjvgTAzqNX2iMsOX1OPKNxyMOWrDiU48up9ddrE2ZEu8nD9RINsJtHJV9Jxck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=LWQ1Ea3mvvi_MteYNtJUNe_neTZeFCiniRYbNsenz1TfUM75k6DcGdxKLveyoLp7V22Kx-Zn1zkoay3sN1r6EGnVUthjVkAm3nS4VxA1p-jq9G3BfakmuBbsjAPGQxNY8qgpBb_lR7gAORZaAh8loIFKaaNDketumHl3R9NPOXgyr-z2Rzl_lFyBpBncHKg-ueVPv45TGXf9Df09rXOMHvv0u6EiLuI6OvtW4qQOfmq0SYSjdItFgw77TBLjzNUrr8JVqGSNBSItzxOnX4KOQyVvAY_xkpWj6E12xX-ZSsDfoNcP50z17nLr_FpMB-Pi91BW7MMvbYjHcsSz_Oe3BmhsIYRKlsjKeErdg4EUZf0ZaE6TeoU2NRec4QfVcq97IGi7MUHFTugLubwyxOMOB0wEYwY1uiJwc8QM5oJHSA8QyVCIh1UIMqq6by76J9b1SVOP2lHMn8vVy2eoKiCii-amNWpS2oA7O5ipanz_MUHzUtZP2jdbvM6eytlgmPHo_6NLby8Z1V2F2GoccF3POHthI2fE55ktzfV-6GjB4ZsK4DT5VJKSOZeghit7JakQ7Je0WBJ6wPBEhOPEWTL7EcUTxqZS8JJiEtFrtCk1zOX7kWfjvgTAzqNX2iMsOX1OPKNxyMOWrDiU48up9ddrE2ZEu8nD9RINsJtHJV9Jxck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو در حال برگزاری یک جلسه امنیتی با حضور وزیر جنگ و رئیس ستاد مشترک نیروهای مسلح است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20420" target="_blank">📅 20:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=uZcXxEUlAGfxuScx3XTIOV_bfrvD-j6BJkU_mX7zrBWGEVLeQvF-779HW0FaUCp5sTqg0A0Nfc8tQf3KuWHLF5QB-haTjMQTQYkPG7B8c0qUoBGHx8HKv_cHa7jPmYJGxS0v0fyoMM7ci4Mu_hX3fCzFzCKzHb6fEpng0UY4idsay75f5KmvreH1Il-j5WBLErjlGtqRGgjcdvfme1BypG02CfDurRB12dJql42GihbS7qj5avETTW651V1mnu2-tbJK-3ymwmUBfS9Ab87b_OqXnYjuLXq7RxDA9RgN1rhtbgy67T1ZwH1YkHLJSRuiNIoWfPF8dHK4HOQgZozdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=uZcXxEUlAGfxuScx3XTIOV_bfrvD-j6BJkU_mX7zrBWGEVLeQvF-779HW0FaUCp5sTqg0A0Nfc8tQf3KuWHLF5QB-haTjMQTQYkPG7B8c0qUoBGHx8HKv_cHa7jPmYJGxS0v0fyoMM7ci4Mu_hX3fCzFzCKzHb6fEpng0UY4idsay75f5KmvreH1Il-j5WBLErjlGtqRGgjcdvfme1BypG02CfDurRB12dJql42GihbS7qj5avETTW651V1mnu2-tbJK-3ymwmUBfS9Ab87b_OqXnYjuLXq7RxDA9RgN1rhtbgy67T1ZwH1YkHLJSRuiNIoWfPF8dHK4HOQgZozdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان به اجرای دقیق محاصره اقتصادی ایران ادامه می‌دهند. تا تاریخ ۳ آگوست، سنتکام ۴۴ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20419" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr9ZNOHA2nFPjzk4yDi50JmWYk3rD19-iLphPpGMJyI47KDhBn_NYkdujvaOJWY-IhJ2ae9HKcIP9ttgII-zs17df3-Z3vRSq_iH7Fm7pthxJmy_3tIEzEJFIfOzewKI9lm1YYR0C8uWYm3HA7kCBmiFDkg-AqsMRAwyQ15MYhYMKBqhPHqwavLiKZLaLi3qgOpiYABqhQsTIL399fHGcXbV8S2iVIfUekEsMgX0oltfTJJDjvVz4duHnoPDrpcEp8UUD7DGEHDh0oqUxFlZuVwEo13invHh7SmMl16_IiYkuAo29JQKQ9mbf6onBb5J_ko2nAD7zRRmrSleag3vGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک چترباز ارتش ایالات متحده در حین اعزام به خاورمیانه، آموزش سلاح‌های سبک را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20418" target="_blank">📅 20:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارک لوین :
من از اسرائیل حمایت می‌کنم
من از اوکراین حمایت می‌کنم
من از تایوان حمایت می‌کنم
من از مردم ایران حمایت می‌کنم
@WarRolm</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20417" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری سی بی ای : مقامی آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
تماس ها صرفا از طریق واسطه ها جریان داره
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20416" target="_blank">📅 20:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20415" target="_blank">📅 20:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=cHcVgungkXsDhF986mwOfNbLs7ts9jxqJ4NnIfhAB6sjl4lB7tPwaa1tQNqXTLDA-HNG1eD6ElLl_L53r_8xG4xZ3CldtsVlNUlU2Mk0XM22nlcsWIiDLCOvACPvZDJJonKPY3zWHXq2Zt0tIGQbBJEtoNF4e2v3aHDMVs-u95XIWKPL8gj4_78LcEcgWuXVrTUbcLntBZjaMm4KrvL9Cd9seqGyGtro8xp9Xj2y2UCxvhbPmHWOkJ0qBwz8h1TSpvJ0UT8yjA0BiUaDgoej_EGk7dVsEm0EiIpnZMN2GdAPOoNTkbTgOv4cNaq1kBJI7YQ3KlFgQHi8bzydVOB5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=cHcVgungkXsDhF986mwOfNbLs7ts9jxqJ4NnIfhAB6sjl4lB7tPwaa1tQNqXTLDA-HNG1eD6ElLl_L53r_8xG4xZ3CldtsVlNUlU2Mk0XM22nlcsWIiDLCOvACPvZDJJonKPY3zWHXq2Zt0tIGQbBJEtoNF4e2v3aHDMVs-u95XIWKPL8gj4_78LcEcgWuXVrTUbcLntBZjaMm4KrvL9Cd9seqGyGtro8xp9Xj2y2UCxvhbPmHWOkJ0qBwz8h1TSpvJ0UT8yjA0BiUaDgoej_EGk7dVsEm0EiIpnZMN2GdAPOoNTkbTgOv4cNaq1kBJI7YQ3KlFgQHi8bzydVOB5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20414" target="_blank">📅 20:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXWaaGIHP74zwzzwu754upGRzNG_dgKfiNuAYL5XlGEquV8p3YfEWAyRw9eHh2s7mzdCDb7IjclD6JGph7P3Krz8lOiasobIAw5EXKZ7UXPKYms8O03R-8ChRiovFU4KCGkjULoHUgubbqvTVSSGDa9TMDmHAnPbW9MXOgtH5upd4wg_JT4LGhTlX4le0A_frbAVDWILxh9b_v8xA_Za9aU7iQuieaivjqr7jZBjhPNVddPIkQhkSGKzB_35Zw4WhiOxc0vG_ANpUeOdRu0SE9_7k_mYyjsTt39H2YvpU9bxmOoR9qpiNzlcE7-HqaWErGvQ90uMI5491E3LiLA5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
رهبری ایران به شکلی باورنکردنی دورو و فریبکار است!
آن‌ها درخواست برگزاری جلسه می‌کنند؛ بعضی‌ها حتی می‌گویند «التماس» می‌کنند. گفت‌وگوها آغاز می‌شود و قرار است در آیندهٔ بسیار نزدیک جلسات بیشتری هم برگزار شود، اما هم‌زمان آشکارا و با افتخار ادعا می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با «عمان» در ارتباط هستند.
@WarRoom
بعد هم طبق معمول شروع به رجزخوانی می‌کنند و می‌گویند تنگه هرمز را با قدرت در اختیار و مدیریت خود دارند؛ در حالی که این تنگه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و «محاصره دریایی» ما قرار دارد؛ چیزی که برخی از آن با عنوان
«دیوار فولادین ایالات متحده»
یاد می‌کنند.
هیچ چیز بدون اینکه ما بخواهیم وارد ایران نمی‌شود و هیچ چیز هم وارد نخواهد شد، مگر اینکه یا
توافقی
حاصل شود یا
تسلیم کامل
صورت بگیرد.
چه ایران بخواهد این واقعیت را بپذیرد یا نه، ما در حال مذاکره برای یافتن راه‌حلی برای مشکلی هستیم که خود این کشور طی دهه‌ها به وجود آورده است.
موضوع بسیار ساده است:
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20413" target="_blank">📅 20:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20412">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک منبع ایرانی گفت که تهران پیشنهاد اخیر ایالات متحده را رد کرد و تأکید کرد که تنگه هرمز تا پایان جنگ به طور کامل بازگشایی نخواهد شد.
این منبع همچنین ادعا کرد که واشنگتن بسته شدن مسیر کشتیرانی جنوبی را پذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20412" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20411" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لحظه نشستنش رو استورررری کردم
instagram.com/yashar</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20410" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=l4JvoHYmCO34liyWHLV8PfPAjx-9Gs4w0jykNUKJ-R4_jKHw3PMZBk-HBaLxz08UQJTJUktBx9ChsVDgvP5UUucyE7ClNVnBhjJtm4AQbRmOKGrLQHkr4Fvyw_F50M9na-aXS6Ix30lwMfU76buZ8MO_hCC_CB8_81LpzLgFwkaPUva0uiXsgSQhVpFaNG__dqlOFCUHyKFpvqaR2iAySBsQ-GEmxsAfYRfUfrXeJsI8B8SRJGrUH_c64Vy0R6WzT3q_lcBFliTO9w6z_gCQ9mQ5PTBCoc_5LTFBO6Lsgy7NfYKMc29BEV2CrBnevzdoVPfCMzR-L5_v-OMfZWWlOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=l4JvoHYmCO34liyWHLV8PfPAjx-9Gs4w0jykNUKJ-R4_jKHw3PMZBk-HBaLxz08UQJTJUktBx9ChsVDgvP5UUucyE7ClNVnBhjJtm4AQbRmOKGrLQHkr4Fvyw_F50M9na-aXS6Ix30lwMfU76buZ8MO_hCC_CB8_81LpzLgFwkaPUva0uiXsgSQhVpFaNG__dqlOFCUHyKFpvqaR2iAySBsQ-GEmxsAfYRfUfrXeJsI8B8SRJGrUH_c64Vy0R6WzT3q_lcBFliTO9w6z_gCQ9mQ5PTBCoc_5LTFBO6Lsgy7NfYKMc29BEV2CrBnevzdoVPfCMzR-L5_v-OMfZWWlOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20409" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
