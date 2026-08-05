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
<img src="https://cdn4.telesco.pe/file/TFs_PvKVOICHK2FN1Dm7zloTe-sSCAAnirBHEfXmxDofv43Jgwftj6os2WKU3jRltSAq2YO97A965EXvS3XNl9G5CgHAivyZWS2kDSPIj8BCWwe-mqQAksy3Es_XMHFFSlWoNh9dy-Khjvhbmhlv1Rjg4lg0Wof-eRAq61ySKNSY7Cn_kYfS9FFOIKS5eGKidmTWiQswMf5SQVi7qseTdJWwfzp8jdUwvbN2A4XVCMDYbExc4LoDoDMLgxzQ4l-tKeAuOEKrsocYCxNc2gZFGD4hSgtWOnVONXnRj_KTVZChMSjtf3giUqNyoMdTkUIKHrY0ghDvfsvD0ehJexKExA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHpuuumOeRsDXp6srhwZnx9cMFNOnkHVfk1_feXayRGLU584R_Sn3jIQdWjMxG6Dpd9dAKUr9NNVQ0wl9zBM9zS9pucRJzw-9FU76HBB_6-bY-N7ydcyLrdEtLStqKgktAo25RmwSNrZx9msDReL-HmHu27thmLtmmpmD_G6tc9Xf6GQ3CVC-5ZD2Qexv12wam_6-U2_d9ZGveoC1dXbifAhkUOYW8NNO4S0PP4Swd8IK_KTZrr1ZShjOd71epGU3hkjpoR8poPmauopkxDZgDEhjsJ3CmHBqLJwAylhZaAjsdROfQ_S_TYqvYhNECD_fXZ3QOKYkUFq8L52sihmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrkxahFiuoZyncwytOqtarkVZRAnJVxrgZt0KEZf7w16ZXSeP-Fw4LyeX9Qggb3hOcdHQa2g6EZSPEkPBHC4AZeaer04hzUFTvPAfYoKTfntBSkd88ABo3TkFlhztjn_oY8cZSbBmoRxHrYnyBk9pOsjRaokPZ0EBZCtsMQHkGpYC5x_mIULRrNRXLP3qjS7n-gf1bU8Lt4QtaCoBnrdq18uCCoQzGfZ-4Wi5H-N_xlusdoSWY_-rPWhhkEDA09Y5K8gn0hI6Pmpz1ozOWyx1EtHcQkglDopmgI6hdCTV3Dw54X8p_8C4ZVCIvrPLPjuHbP2IuUMcI_OCGSted0ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbnu0cyxF39Httw8BYVtjIcrI98TiEekiKmH-hDEjyekEPIYEehKB4aGw3B3mOibaBPI5shux35vJVWkUjt0v7FXDbU7kMjeWS8WlB1XrwgoeOAWEAPS1UOzroDiEknwDOU-SePaR5riEvXa0J1hbib5YtuV9-PYgY023X74jhrizmpQMgRgvB1yJvrLh5VS8NOaHCjHyUAwCW9Um-vTBYprSJTGs-PLw3WYxIV-VLIfqdBk9TKks-4ITPYIXgVOsYZkcqQfB6vA443jreIqQuc44MyYTWGJnHd-jrU2YPkwMO4bYiH7hDtWy9mxM2hanucMcdHQ5pOVWtYtZJ41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj2kcd3VjLeM5UiDmlm7nOytO2zuritJgWspwV5aYWBpb0mFxpVj1ZhmEZj_TkOKmOPQcrLaktYId0rPvGNvy06i2UQJYgLs2EYCH7aqUpSBN-yCXUUAD7SOMQsXIGewfMOQxhZVUjT5N87X4SNhBnZD3PSjnvuOijVvZm-XOCVEYZUCYC_GR41XTESOoJvhCQKKcqjolyPtg7BSYpyLqADIjk4tH6mentSrdgccS_Kc81opREogW-O1zpUnEYMrw1V6QtgaTtnOwHq1Fcy7u9LRLKVrAHsa9MqejLfAGelw65gJsklYDRJDE2jSccCBIfnsEOq0uzZyaLMC1gBzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSMpiH_zLItJbGQElCPSIIOjtKdX36mbwiQzpDUP2icI44AGcw2l0Im44CJLgz9Pklgd3U5RACYzPFmVvLhKZ3I1nTm863PwguerDdrjTnvujmC2__pv_p2I-aBug5kiFSXJEdkDx6yrdzuEJ419-POTk-2Wv-8lqbHX2U-npOkj0U7SjD-ZxYi7BGl2q4UL3ArajhXIISJqfudKw03pvcwIoJieFEvfZ6z_JeAMbiO1tBvJdCYWXlIGp4LSvVk6-_F2CNGd8z5tQOTrCl0fBTDNFbk0NXhObVNsFG-YrwH4TaJAykJQt9ZrLmjxzIyntkndwjgeBSfGOWWDmQY0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfv-J9MZalTzQTfhV9_V-hJX4Qxhacr9k3QPHgY89vPXCJW-wN9W-ipA45FAq_EHDbDd48qzAui9QPk5232hdqsn2iYayPPSJboJQwng6QnJAlEz2tB3KBOEvLJhHGeLKfTq5-A2QWeF340dvLAmpRLst_4G6bzfXc5kvMeN9nYc45vq23cw4lABXyGXj0S3cN4fS030TQf7wlReBYAV5m3qruvXMYZ2w1miWwYyT_jtR3wuRvvjbfHm3CaArE7posxet0ojI8MTzd1JrQzCGN2tWwLU5lE7dNc_XgzVDEJArSe3PODhQHbfxM2c7oysz4FKK1tTmP8dH0CddhLKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqDRstfOQ3zjTI7KtmLFCHWGZzX3tFlKunFENwZkRabgFb0YhGUBYqATJrZ5VgZETHaYYa5vIyXtwMfKm-5u3GHY0aexOo_iSoaH7bskc1p1h1ubtRp4HgAgavTRcy22hq2ygMj42m3v850PeSyvfa82pCe1-9pfxH4avOUoDv0zlOYdU_WgT5AIUpMpfLxcTd3fasu0-orcJliN42IKL45OP34L7sKMloK36YjSxA9gPvH7s-JBJnkLYY6s-KTbTcCu3XWfXb4MWbpBS9nL33T7Wg8KqNIjnuHhBijJXI2Mrq3czRajcTWiIqOALsXXZHAiwXYr1gwJUMzl_mpLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=iC-u1m_hT-CHR0XrVvvjNhG-ZxSuRDj5UbgJ_Kb-63p4BU9Xy5QRxVB739QTla7p_1BOi74CXnz60IuphKIx6tsQtF0tXAOz5goICHDrVUSPBuZy0NUpojJssHYm0DuVfgVeomPeyS8PMaGhkCpU8GzLoZk2ryofwbFVa9pk0gnp-I9Idlaqv1T_daUj4G5CMsuBhWZ1_J-Gw2wOoFg54_CbbQfN8A0eh_qWTsg-srWaaFrazMbh365YZvLY5K3EzwaKxYrwWGKXS405-LnSWDfMEvBLr7Gs0V75FjdTbQCWnm3K_4mtxHXR2Z_SZ7XRl_ct6RTkhKlpDGYo9dC7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=iC-u1m_hT-CHR0XrVvvjNhG-ZxSuRDj5UbgJ_Kb-63p4BU9Xy5QRxVB739QTla7p_1BOi74CXnz60IuphKIx6tsQtF0tXAOz5goICHDrVUSPBuZy0NUpojJssHYm0DuVfgVeomPeyS8PMaGhkCpU8GzLoZk2ryofwbFVa9pk0gnp-I9Idlaqv1T_daUj4G5CMsuBhWZ1_J-Gw2wOoFg54_CbbQfN8A0eh_qWTsg-srWaaFrazMbh365YZvLY5K3EzwaKxYrwWGKXS405-LnSWDfMEvBLr7Gs0V75FjdTbQCWnm3K_4mtxHXR2Z_SZ7XRl_ct6RTkhKlpDGYo9dC7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH3AWez-0_K6d84JArPeY3g2NGbhj9W1cZKs1oL3APCM-8VDpX-DwUnplUUZAHSySRtJuzgs1ZAL-0Koh8rAZuSJjIIIbPcwRfFsXxR5etIcYWNFqSYeSbrHHkkHVdqmn97rL6yEGzVzX124AVURmmfdbjnjdrxHrfkWp4SLsBfRLZsBKPrGqASO5S8TDLK2cPnP8wywwYsgoN238Hr641PJLY3psS4cAjcs7QtujRKLNyHb7f3RLdanMrpwIxc60tokx1af-Z6TOjUfOntdhN3zsk-ua4kuYxQnHsG2rZ2esB2KTCTUd8rpG_Bjf9EUoFi5XfyXo8SNdq1hOHIOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=dTJQ0BFoj8DIdgZCkdxR6fiYv_CbNM83SmR-Xz1SPdQ4eBbdz3aWjW-XZuNBKAO0J2EoPrHOGhvQ9ueSBEEW-eA6G4Snt36crqMHpIxmd3_tpSWjxE7KtneCivXvHv9MCnKTVBk5IiRwwp0hPkXosS6bY8s-gGr8JT7dKw6mAPsjrFKfskRoGO7KpFaYO8hArL2IK0RR_MpMaKp6EreBRLZsJp7tjvKPTWrWPVAjIo3F0aMv0C_GaNSBLldiecka1oMTopBKBBGEd6nOanq4BfKb6L5La50rgtfET6bJbqQFaeXNQ1htW9ux_MFGAYWkd5kyy2YOQrolKGMo42tsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=dTJQ0BFoj8DIdgZCkdxR6fiYv_CbNM83SmR-Xz1SPdQ4eBbdz3aWjW-XZuNBKAO0J2EoPrHOGhvQ9ueSBEEW-eA6G4Snt36crqMHpIxmd3_tpSWjxE7KtneCivXvHv9MCnKTVBk5IiRwwp0hPkXosS6bY8s-gGr8JT7dKw6mAPsjrFKfskRoGO7KpFaYO8hArL2IK0RR_MpMaKp6EreBRLZsJp7tjvKPTWrWPVAjIo3F0aMv0C_GaNSBLldiecka1oMTopBKBBGEd6nOanq4BfKb6L5La50rgtfET6bJbqQFaeXNQ1htW9ux_MFGAYWkd5kyy2YOQrolKGMo42tsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6NNDQx_C9i9N5laDk8jw7uHQzD9jkV5DqBCNwkjqvlCPxEfzhYDEUMcT0KcS3bX9RR2Plzeb1envgFNwA5ovkDOBAsh7g-fcdbyp4L86YntWCzVK1BYIMT-Xq3BS1mWrwnWKfeIJ7G8v13mVk5iAg1_axCkQMcpAHKfo3yAiskrqqImfSWdHlcr8TSv9fDBtn0D9mYgIjKqGGUYw6r1kixTeOU4r0P_zo4th6a1VCCD99Jyg3JfYFu4b2JI9Xd7lpHTmlZgZQXHXk4Vb-4V0bXfT8lg9JA9mIncVPfGeYtiPOHh7qIUk5lb5HMMV_c2wvXyTSNllnrE7oeXsJPX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=KTlQU7MDp9kZxzr1cFMVqLqT1vBABt3nh2GAoyW3viK-CrHQJo9p9pKohRdbKbXYG-pcC7hmkvmYyv7Mm15wUSY-v43Tv5yVbRJ16P0zwqLdu5a-pE-kg6y4a3OZUOHiLlcORVig6cPnzOvJQh9fiTDrGhMMJaxOwb95uon61Ag1f7cy1dOWti0CCDnJp5rkV9jhhAEHprD-i4JefywRR68QpnXNMY7uATHeGPAaICcLKbiig76KO7ES6JVRI7WTjy4WPoPd9wVsSi0dnSA_YrMgZgjb8f2mDupuHeXQDEaxW-z6V2l49hlr-tcR5cDE9OXV4zwH3P0IMcSeRVYVpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=KTlQU7MDp9kZxzr1cFMVqLqT1vBABt3nh2GAoyW3viK-CrHQJo9p9pKohRdbKbXYG-pcC7hmkvmYyv7Mm15wUSY-v43Tv5yVbRJ16P0zwqLdu5a-pE-kg6y4a3OZUOHiLlcORVig6cPnzOvJQh9fiTDrGhMMJaxOwb95uon61Ag1f7cy1dOWti0CCDnJp5rkV9jhhAEHprD-i4JefywRR68QpnXNMY7uATHeGPAaICcLKbiig76KO7ES6JVRI7WTjy4WPoPd9wVsSi0dnSA_YrMgZgjb8f2mDupuHeXQDEaxW-z6V2l49hlr-tcR5cDE9OXV4zwH3P0IMcSeRVYVpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEreAI4l_iWdF0N83A0QXJicNBotNNz_Tl9TdaO3e4yRnWQFF1Sq08YZpaKcvKFBJ8sB14U77WWZHKwsouX7wn1nWmaNzpMuojs1-_xqEZJBUM2hs_TLPFlhZcqHe96qaeI8NYOxAeriirjyYG9wvmjD7yhwUMDQGAN0Ed1GqmaCGBJoIG3S4upZm6HrnAaazyiLnWUogUHVBubaXlvWlOA07Fqhe6fvDwWnX8MifxU2wxw2mG6TWaIAAw-DI1uI-IsG46h2LwK1v-2fWPiGcMFw_dU8TRamhW_PMSjdEAfxwEWLWfhpiTf63LrJ1mgf_leK7kVEPGYou8-IRJ9x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=XrlJFT7HxJFJcwHu-Y7db0ZYvB-woG6NgYoSXj8rpdVZNSzsyS7vpwQXmXHbW9IAOXZKFr1wmn9UHeHty92i-vpmiAap3CpCMSBm1LKS0HZKgRXdbTL_oQ_bJzXtIfa2lHIPS5zfiKCDHi8nH3Tg874KwAyWZzeA3cHZ1BXFQ-v2rT3YGoq_1UbNZzhI9-dxp6TuZATldy-855ruYJlUBiS2OTlrvvxu6kRCL1PsFWshXlm2ixGf2Dui6OI2Q4hJ5dwDEZpgbtnTEnJK1IrYdOVhP8mcgXrJRXIeiokPqPHT6WeY8-wLxa6LwvJc1d3mvhLZGSOlAZ48f-nvmTOUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=XrlJFT7HxJFJcwHu-Y7db0ZYvB-woG6NgYoSXj8rpdVZNSzsyS7vpwQXmXHbW9IAOXZKFr1wmn9UHeHty92i-vpmiAap3CpCMSBm1LKS0HZKgRXdbTL_oQ_bJzXtIfa2lHIPS5zfiKCDHi8nH3Tg874KwAyWZzeA3cHZ1BXFQ-v2rT3YGoq_1UbNZzhI9-dxp6TuZATldy-855ruYJlUBiS2OTlrvvxu6kRCL1PsFWshXlm2ixGf2Dui6OI2Q4hJ5dwDEZpgbtnTEnJK1IrYdOVhP8mcgXrJRXIeiokPqPHT6WeY8-wLxa6LwvJc1d3mvhLZGSOlAZ48f-nvmTOUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqRlrFh6Hgst0iHPaEV2bOq3y-zmabBg85qfx1ko5K350cbyBqcCF-S9mxoMlKmmujvkwY5XBpEAivBC4_jQpDCeYeLYYaT8bunIR_rYQ90GOgQCG3zYjU65YyH8wQ7m61ycs0-26KxY1-_ucdy4c2Buz_Pj-6hc6n1NxHhYCSvvOSTQsGFISXo_tJCWcbBlTuw2KV-_6umrnJaVvTJGtKTjiaUxrqJZGxnfLs628FfDFlqkBpA3sggFkop7YOHAgk-xXlzn05HrYCVot9qomrBalQmegd436SBIxC4yM7rPNqROUDFBZL4T-0I0YqfUXkXSEGpn4oh5KKeI69Lxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=srwOQo7ktyvDzfYk9TRGAIH24NXoR1YaRlXEF6Fl8y_Y8IYldPDe4HSxbigtoVBpw4JUlVT65X95cYCWz3TqI3bAIdAd9aQdtvBXO1fvI_TiZHxYjge5M6cqzJ0TGOBcQsnOPEPGn9FLMQiKaBZwYS5F8noergmMDfBpUAt4W2NU8zlxpqhRvcv1o6lhBfPkc6PXCnV7xkgM6I3hkkDWTTURawZUmHvQgrbmqeDLK0x_UAwRbxOMgoNJI7s7POpE1-XPkC1e8LFtx_O5-kOCE4QQZI15_JETfHpVwc9CqCQefBzU_B318F-tWpGGkcdkTXqeYfQ4U1NkcGgJxWz-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=srwOQo7ktyvDzfYk9TRGAIH24NXoR1YaRlXEF6Fl8y_Y8IYldPDe4HSxbigtoVBpw4JUlVT65X95cYCWz3TqI3bAIdAd9aQdtvBXO1fvI_TiZHxYjge5M6cqzJ0TGOBcQsnOPEPGn9FLMQiKaBZwYS5F8noergmMDfBpUAt4W2NU8zlxpqhRvcv1o6lhBfPkc6PXCnV7xkgM6I3hkkDWTTURawZUmHvQgrbmqeDLK0x_UAwRbxOMgoNJI7s7POpE1-XPkC1e8LFtx_O5-kOCE4QQZI15_JETfHpVwc9CqCQefBzU_B318F-tWpGGkcdkTXqeYfQ4U1NkcGgJxWz-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0lBwBf7AaVPCnLpMd0kugqwFLQAZV5_Sd_TUcHH9FQRzqqDwfmQBH_GpvwB9_vacJJlruCoQuXBohmCVOz6ZFrXIILLA7BViKAn2lvY5OqnBJTihgUhTiRAk2B5xuETCasOC9TO5znCJvO69YV-6c0m1RcetXu2s_xhxm2nLP6P8sgRXktVHQBNUA3RDNOsInNG9W2UShy0TOPlj3OWN6sjmsoulD4WV7me_43URMLE1KlYTq8CEE_ty9q9hBiMObsikX21oN8VYa4QEN4Bgy3D7LsnZX15hxMHeKD7WaoLvBGvF5MLQIxXtN2hTDIRjy8dhKGgOprHYD3c6n3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxFr0eHSHcnfQLUQC8_or6mr539wtIJAskZEx2IVvZseHL1RkEQ9EPecOzCqb5gLtsGzCId2YJFiG9Bu2NLAhmjoUUmoSn022Z3nKth3llJ3PXdzTOieqYSkOgDN25Vs5i8mT8blLwxrBca8gWBBRJzNDhrRi7NSVhV2xRljJR8wSrwswBRAvcUz_2T9CEyXWvEYzMhfBdLg9N4yJwO2b3hulnJYtO9rr1FcpamyY_-FhyiOjha9paEeCXuqvnkUwX2p1mZjZ4bGNbpp9o5-E9XQ2XEgr9ekLOELG72EQzya6qVD4o5iA0RYOunpdKwgGwsedWvDrV8yNdEOvX0VJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxJdSDS2LnidEGFn0pTcPoFkzP4q7mQ1P4E93o5RlUpOkoKVOIGnxzUS9MfUeSbzZkVimRFQrOLVXjB_JreBNdq8pvUlM9Q3mtpK9p6nwclR3HrDu304MUSWNHtfdnZ9TQYMWF1HEhj22sVod-OhYY8jsPbs2wOqpSCzjzs7ri-pGS2YvH_q-eH24VVCmb8LqXgvTNVyVXTKm8KbY3-5sGw3N6GKUXvXGd4AEHkfbJQerhB56zRaRQIw1Ab-n7s3LwzmW1UTvQ3qpvdnPA3-jLKvjjBRncTlfHfifOPCZsPinOwgiCvOGBtyMtOBeT0nZOz-GV-wMvRcstuo_2axjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1EhlgRdCiW5yxLQDKyAiMuSMfEtQnV38sWlslSMl6K0yW3xYw1ulzr5qGhVEDK37dwDZmX6wv6vKiBE4t1rHSEgv3_H5SkOvIOxV3uq6AitST8WvpvmeTwNhWJyPv0G5H7Clu4vNU87qdxKngf1UZIBcQ9BuCfMHKRZH5H9gdnRtYlwiiVusqM6CIW_PPcoriGQ_IeQAO7jJOgBEXkukISMXqz76RcuMTcTjVQRSLk8TgJWx_urDYFtYE00WM1MLwzfC6tbJATbMxmNJ8oKnFjKz9pHZt0ye0cKhOREoy7wd0xEInaeKwxImL29zXSETQ8dfZKL7Hpsetm8QUu_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyTWRRk6VKkVshBef4bz0jlDC1RAvJ00gA4XEHOM-1afuYGtvRxDu9_Yq5oKqWIQZIeUHYquFYvKqkzV724d-xFXCuMivBVjVQIiAGsM5O8ZTOl0pdlBqv8fMUknAm7TGLTEgPAWAD3C04M0nN310DQ2hr269mlzX5SuSPj5GtHsbn55PnN5Ulw_n7BRo2TGPYggoIL1FfaBH41R5UU4Bv7ybrShv3GLMCyo_8MCgbOoYOeB_Fw8uVK7NCHyCCYdxm3tmAIWc5jlNfT-76pEAxfyB2pAtfID9Rtmg4eLDMqB_n3U9QveawGNa0RBVy4Hu80CTpC7HEbBB-ho3-3QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiT-KgHf-_Xf36xOP8XeqIdQTaGwSBlPMpQ1w0W5j4-HjHuCsy6Bhktdr8ZL8Az2dNah5NmpvDJh2C4hQvrcpygcJNMtiwzL-DDSONmS4YeZVkpJ2exGl7yHeBuu0oAzvmkPwVSsd3URpJaLQj4hqubdpaXX_NO3XIUt6nYTpw20Y4aavloTNp5TFHnH6152nHXVg8FzNgJcUiNEZFbBJUE8nCDzVBvnyRZUP7fPvOu_p3LttJStbOK5METwkqlUztVY4lD-Ztag3t_NtVHlLI3pAQEYdbDUejMjzZWof1xEYB5MOd-_yigE-AUOr0d73pSLV3NtYzf7Zom07C4pyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS5_UBzu0uLVoqiz91iPKFSBpxn95jyASNLqi5SGvMTSokVbeVu9_d15cMbc2aKt_6Sj2X-A21NDX4jZzEsdrcUfbVz_cOmzZ-J8IfSf8eM6ZrlEdE_b1mTGQw7-qFx1Gb8BBw6E6MZXKy-skiXW0HYcZ8TKAJuzAev00Zrgl1M8RECUALaZTgHFeYhd0iFRf4wEbz7EWxwwHZOXBsOdNOPnq9m0cz6UBsv4myMqXHqgOPJLE1K_1U5IBgTGYCpNb_9GWImzOVjXbHakTh0og9dQkXyZGp0tj5BubnKogyEnRtkf4Z0qDtR6Jlgyp3ZJ1csR9UyPl-VaFd038Mp0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtCikvz6fcEL39XY_e0pS37yucKP9hVNHx3QaacBe34U1v5MntisfJOlUdMD2ON0YNIIQUNxhX0_lCFzXota7B70cCIQ_OF-fPZHJdo05dtl3jfOa3R9fiMA2Fucc-WUYVCIZCa5tAl1DWatR39owq5JhBdqrM48EcbMFahlr4Sez11Cgr92tMWFo1cmNhjjHDUkIzewERgQW8U5cg4u0whFELl2tTxDB3xoduFX-HWvYzJHgfK9yT0xNny5EgFR1JjBIM-MfZSa6Y0xRYy4wCGhDETRAzHNbmKAtfCiy4zLeEsqMh6dV-iEqIiadOroJhESWvJhbyWhny-cl0tr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX3rBtqDZxqFYAMBJD1dCY-uoh-FOxMdN-3BEYY8tZn7ZkJoWnM2W3b0l1n12IpzRX-INBSzeme0h-5FYrdRE81QlDaLqhm4w8Uchz1mgHIQA1gkvR-jxRnzwWq_Qot4n0CUNn1ZKHer1k4mGNYPhas-ElwpxXW6S_Rq_kD1rKLsnlgY3WKyi7EzQ9oFLZ5PEKcLAaH5NvSVL8nCFmANahqplPsXbNrQmAmkNTYQeCpJxLxFYRapzdyV5v0aRsZ5Ud1qBAlZHvAU-le9NYKfsSU5jD0F7FilPBHjPK9WJv2TLzG46Kz_ZA9iPrxwuTvM2o9FU_xCvydeDkBq37dHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2M164vIHtVD9u9XckXBfvM6q_Neu7ORpPLFH2SnXjeHWMu7e9YaRzRryye7r7YfDFcFNieHGPmSNUB_QLzxNESaF61Q_EpC3aXuQn89Hf8tgP8_8jHo4yMHfOqVscfIkxlQO8_IIEhUJHzftf9WYzpcb-YN_O7Tle99YS6b_18a7wFq-T-zOzR7Rtg4D8J5a9OU4UjnXTgFpjXrlSZzxebiHnjpx6he0Hu7jn_Hfikm8HmbvBjEuwJG84iFvRtUau_om-GEyFexj9haieW09oIW96gHrvhChoWREJ9WkYVoafK44HFj2JLlpgShlXtFXHJymWSA-9GWbBZljIZB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=Guo65ar_dJ0kFHvZXT3wAiX2XGGK_nvHT0bkbhVVZXzSDYrKlsyAcntcoWLvL7UWmFLLMiyBDega739oK98KrSW75ee76FasbmyTvrgZamzbgnlj5BEFBkxSXvKaQo23_tY5Djri8nu2VGDIofwO7tG1PLI9h-UmvU-C4iqYof7e1FgYILsevmzER_T1QXYo2d5MTtjIdVHMwKPQTqi46gTXpLEO574CGXVK8RHEiFVdYeFKIuak8nxINxqtdEJHiLtslwAH5pLWcCY2jx7DMSBuaqxv3DAIAdc7FY1wuUXXvRjdMYRf7IqgaSrMCnX_ta8t1Rqo_HFNm_NX24FfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=Guo65ar_dJ0kFHvZXT3wAiX2XGGK_nvHT0bkbhVVZXzSDYrKlsyAcntcoWLvL7UWmFLLMiyBDega739oK98KrSW75ee76FasbmyTvrgZamzbgnlj5BEFBkxSXvKaQo23_tY5Djri8nu2VGDIofwO7tG1PLI9h-UmvU-C4iqYof7e1FgYILsevmzER_T1QXYo2d5MTtjIdVHMwKPQTqi46gTXpLEO574CGXVK8RHEiFVdYeFKIuak8nxINxqtdEJHiLtslwAH5pLWcCY2jx7DMSBuaqxv3DAIAdc7FY1wuUXXvRjdMYRf7IqgaSrMCnX_ta8t1Rqo_HFNm_NX24FfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=rlF-IdMqG9eImuRK1AYzuEUOmKvxv28Es2_DsD2WG0Vm68-XLl9Bc8K0FfiCPmwuAt1_YwD__wiRMqgLh_peRKi2SSy8BOrM6Qkrxn1WS6TvMB96hqzNm8HaLONxAJH0DhzCTu3UprYWXjSnZlHMmNEzs9NaHGsyFrxG2hFSpfBWoCFC_vv08A-4fQ8QQ2U3y7YA9y3USdWn-lF9X-sLAhUjisBr2EfdhSWZ5E8RPMkeQvU2uewWHR0aPrbHKKvAGfhFakEYfiw03I2TWrk_T0x6xiQzlcVkNey8U0rzXqkm24nQDg9FjjBMO3ZblpE2WOpngH7j_z2mMwSZFznetw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=rlF-IdMqG9eImuRK1AYzuEUOmKvxv28Es2_DsD2WG0Vm68-XLl9Bc8K0FfiCPmwuAt1_YwD__wiRMqgLh_peRKi2SSy8BOrM6Qkrxn1WS6TvMB96hqzNm8HaLONxAJH0DhzCTu3UprYWXjSnZlHMmNEzs9NaHGsyFrxG2hFSpfBWoCFC_vv08A-4fQ8QQ2U3y7YA9y3USdWn-lF9X-sLAhUjisBr2EfdhSWZ5E8RPMkeQvU2uewWHR0aPrbHKKvAGfhFakEYfiw03I2TWrk_T0x6xiQzlcVkNey8U0rzXqkm24nQDg9FjjBMO3ZblpE2WOpngH7j_z2mMwSZFznetw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=nCDiHl4YLZSihQHK25E-eg0kD99BaSAjhxbUM24GVI1lvXE04WRZ3vQCia2a0v6AUu-qKjqFj0-iViSELhlOOxOsk0pxIl4MASRa5AIWrBuJoVDtYndX2QP0xitZH58ydODNxH8tsgCEMhzEtQp1fmYaZSLL3yXO2EsSZrjbu0SwFTlTpTG18NYKCL_Vct-aEGFIlORj9mbmsWX_9BKHE0R5NGjQR1nF6Jo-ilinlrVlZvNCKVgzVOwFSOTLcToz0wsrLLCZM1JYWdSQbUbdg6U30Nzk1xtqQA9XdhTFH4csipixoNgHBw4eWR_-yISV3zrytsagYihhA-rWS-dN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=nCDiHl4YLZSihQHK25E-eg0kD99BaSAjhxbUM24GVI1lvXE04WRZ3vQCia2a0v6AUu-qKjqFj0-iViSELhlOOxOsk0pxIl4MASRa5AIWrBuJoVDtYndX2QP0xitZH58ydODNxH8tsgCEMhzEtQp1fmYaZSLL3yXO2EsSZrjbu0SwFTlTpTG18NYKCL_Vct-aEGFIlORj9mbmsWX_9BKHE0R5NGjQR1nF6Jo-ilinlrVlZvNCKVgzVOwFSOTLcToz0wsrLLCZM1JYWdSQbUbdg6U30Nzk1xtqQA9XdhTFH4csipixoNgHBw4eWR_-yISV3zrytsagYihhA-rWS-dN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «از همه شما به خاطر حضورتان در اینجا متشکرم، چرا که ما گام جدید و بزرگی را برای حمایت از خانواده‌های فوق‌العاده نظامی های خود برمی‌داریم... امروز، من یک فرمان اجرایی برای ایجاد اولین کمیسیون همسران نظامی ها امضا می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20423" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=vl2Bhwbd4P6LsH8Z5eiZXSJWxpASjT4Hjvyu0CkEY7SpP4AWgTgZ1H99Z0sqZ_dpMNLYFDRmCuZ8pKaOm4aHxsPvGrgU8B82yWM9obYcoAIjfHYurb3jdcxMTupU5fUNaYLt9eUw4CDnHGrdwDdPYt_NPXmBZlvasydtq8Af2Q5pSPuYAI7-akaV23Luf9XMudlzfXx_MPn7JzOCJojxdVKxsDJw3uYvD1ae0cEE65BZWdjzkZqweUjqqkCRNp6HL9UkbKPY-poPFkpaaLmP84t6PiAr8i06ho5NWzxV-i92RuuRITel4DiP_vvM8SECBY09UMHvV1g96fq8fz8sLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=vl2Bhwbd4P6LsH8Z5eiZXSJWxpASjT4Hjvyu0CkEY7SpP4AWgTgZ1H99Z0sqZ_dpMNLYFDRmCuZ8pKaOm4aHxsPvGrgU8B82yWM9obYcoAIjfHYurb3jdcxMTupU5fUNaYLt9eUw4CDnHGrdwDdPYt_NPXmBZlvasydtq8Af2Q5pSPuYAI7-akaV23Luf9XMudlzfXx_MPn7JzOCJojxdVKxsDJw3uYvD1ae0cEE65BZWdjzkZqweUjqqkCRNp6HL9UkbKPY-poPFkpaaLmP84t6PiAr8i06ho5NWzxV-i92RuuRITel4DiP_vvM8SECBY09UMHvV1g96fq8fz8sLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=njjvVLybnrQyW0ScLlDp77juZwwT0T3uUERChoA53V-ALIUKKq7WlKTU3FcThvhieJ7oNTnUf98tlBbAhnFwuVxljMjpUMAM0L3sbKMyeapafNYkLH5GKcUGsxDCvSZuz7uk35k5kkDALQXzvsMX4O8sDIGCiGo8apqyhA4xdcvf23eGaNZ0nATV86h-DvcQCqLy2nKrP5aNq231lyUQEcpa2vwvc-NA9yh5WbLMDkM8gjzseOsQeE_wgO572XnxBzfgZSsc_JHn3XDe3pqyEHt2B24zKgW6fKqW4o2CJkA0qTd2feDtLuaNgfV85S5lk-OnBKoLhfCX9D4m1tTaCop_busyLDy0yeWajLeqcR7KaL4oQM7fJQft9TA11V_enrkK9827v8VPNaFwqBh_g72U6d1ZLQ3Bl6CxicSaRLu9D5Z9A2Zi1UCD-yMMzPckU1O5QG39zigdf-ErEoqOnNWNHu5Dn9F91lna1QtBNnWjCENuXbkIOtFS-YqfnYuSiU1xBgKHcaBFiVPiEVovACcIl-SzSbfSibscxPnu0DyLFybewhrxZ44EPO_nKHRS4k6tpz-VQh72XCG_gDEB5OrmuMNE_vUI3bZcI4YsfXuQyNeQC8y3iADxxoPBNzDQxJ7PjuJIBtCY-gAv8HwzLeMM7H1HRzupkk2sjj4G7B8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=njjvVLybnrQyW0ScLlDp77juZwwT0T3uUERChoA53V-ALIUKKq7WlKTU3FcThvhieJ7oNTnUf98tlBbAhnFwuVxljMjpUMAM0L3sbKMyeapafNYkLH5GKcUGsxDCvSZuz7uk35k5kkDALQXzvsMX4O8sDIGCiGo8apqyhA4xdcvf23eGaNZ0nATV86h-DvcQCqLy2nKrP5aNq231lyUQEcpa2vwvc-NA9yh5WbLMDkM8gjzseOsQeE_wgO572XnxBzfgZSsc_JHn3XDe3pqyEHt2B24zKgW6fKqW4o2CJkA0qTd2feDtLuaNgfV85S5lk-OnBKoLhfCX9D4m1tTaCop_busyLDy0yeWajLeqcR7KaL4oQM7fJQft9TA11V_enrkK9827v8VPNaFwqBh_g72U6d1ZLQ3Bl6CxicSaRLu9D5Z9A2Zi1UCD-yMMzPckU1O5QG39zigdf-ErEoqOnNWNHu5Dn9F91lna1QtBNnWjCENuXbkIOtFS-YqfnYuSiU1xBgKHcaBFiVPiEVovACcIl-SzSbfSibscxPnu0DyLFybewhrxZ44EPO_nKHRS4k6tpz-VQh72XCG_gDEB5OrmuMNE_vUI3bZcI4YsfXuQyNeQC8y3iADxxoPBNzDQxJ7PjuJIBtCY-gAv8HwzLeMM7H1HRzupkk2sjj4G7B8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو در حال برگزاری یک جلسه امنیتی با حضور وزیر جنگ و رئیس ستاد مشترک نیروهای مسلح است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20420" target="_blank">📅 20:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=CQrKkBeY7OYsB-Ak95ZMbtAJMSr7fzQyDLKIgVoSqR3oE5ztKGq89b0aJFC9gwAsKczIHmCH_nrfI3HfLpWydsgXNdFDJvRkKH6KF77UTVANil1pYn6CtZQx73xiYsndz6cOsHr_8C5J2EvLK4dAh-sPeV9fnC-huraon8KZsEbJcfx13VesQEC2cf9c4esLLg-BExddyIhPM6kHJwGxGuCdS-7zV9XE5lb7U1v7uklSbcngXCqiFhyNRYWlal3q2ah4FmI_c3KU71TAL2VZNMXPm8nS8y_YNSV8qtbyPBvFO-Fg-dPVoift0mNi5w42xodxVUIAdCGuajDkwApcyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=CQrKkBeY7OYsB-Ak95ZMbtAJMSr7fzQyDLKIgVoSqR3oE5ztKGq89b0aJFC9gwAsKczIHmCH_nrfI3HfLpWydsgXNdFDJvRkKH6KF77UTVANil1pYn6CtZQx73xiYsndz6cOsHr_8C5J2EvLK4dAh-sPeV9fnC-huraon8KZsEbJcfx13VesQEC2cf9c4esLLg-BExddyIhPM6kHJwGxGuCdS-7zV9XE5lb7U1v7uklSbcngXCqiFhyNRYWlal3q2ah4FmI_c3KU71TAL2VZNMXPm8nS8y_YNSV8qtbyPBvFO-Fg-dPVoift0mNi5w42xodxVUIAdCGuajDkwApcyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان به اجرای دقیق محاصره اقتصادی ایران ادامه می‌دهند. تا تاریخ ۳ آگوست، سنتکام ۴۴ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20419" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbyx0kfvTw5c0xHOiUs8tgpJ4TkYedLHVxDhe9_ToJdc1NTGrUnUnm43BIj67nBEDjtEim9O5vk9qFbikFXRxzopYYV1kqgjUcnkoDz3mhdaL3JkQOSC7AElVP84T5CIeLEcyQ3GO487qEakxpA7u8lHdU2-JTsHNLoMdo-KEh5QwFUmz4NqeT2aSPsnL7o_N8XpCcqWyOtks0eIeAFiJAAAcxBT_WEfdhgPBXQZE06Bc1_JiUKiSzfDC8yqzfdK8Ra4VtzBl6jssHDTErxoWa06XlF8a5CdobPgzKmmfI-cqW7NomodJWMWn4DNuS_EnB-fh54qJRyPiqRN6nPCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک چترباز ارتش ایالات متحده در حین اعزام به خاورمیانه، آموزش سلاح‌های سبک را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20418" target="_blank">📅 20:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مارک لوین :
من از اسرائیل حمایت می‌کنم
من از اوکراین حمایت می‌کنم
من از تایوان حمایت می‌کنم
من از مردم ایران حمایت می‌کنم
@WarRolm</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20417" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری سی بی ای : مقامی آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
تماس ها صرفا از طریق واسطه ها جریان داره
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20416" target="_blank">📅 20:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20415" target="_blank">📅 20:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=hqXdnaC_DZdz_v_Wgs4EeYeTcoAMPV9_IqDQ0T37ASaWISQvb4Yq6Xx-NVWtgfivFBDMZO7Cj6V57YYz9HNqZJNRSaxt99EWzzK8jvKD8bcxeMj0u0BmFLZYREMA5bnS3bl0cZm9E17-UbUsL_DItGLzQtsKmVqu7Iug4Ar_FoiXiCpkEzytgLXuyob29HuvwMxJmjwsYm6Pyo5PfkhC7JUN_FE8hfs9UMTbxEBuhgVRQXzh0fb2gr5GvdeHyYyHU1mlAea9xlitZYmMJMBwNb7renSLInJrdCYcOzMUeo19PGXdAsLm7K_Hn8BSGaobZ-plq1mLr4WqRlB-pJScpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=hqXdnaC_DZdz_v_Wgs4EeYeTcoAMPV9_IqDQ0T37ASaWISQvb4Yq6Xx-NVWtgfivFBDMZO7Cj6V57YYz9HNqZJNRSaxt99EWzzK8jvKD8bcxeMj0u0BmFLZYREMA5bnS3bl0cZm9E17-UbUsL_DItGLzQtsKmVqu7Iug4Ar_FoiXiCpkEzytgLXuyob29HuvwMxJmjwsYm6Pyo5PfkhC7JUN_FE8hfs9UMTbxEBuhgVRQXzh0fb2gr5GvdeHyYyHU1mlAea9xlitZYmMJMBwNb7renSLInJrdCYcOzMUeo19PGXdAsLm7K_Hn8BSGaobZ-plq1mLr4WqRlB-pJScpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20414" target="_blank">📅 20:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGrYPX9jRWVWbWcQ0unauQNnNeVWU_fBRSPxO3jwOY5QyMv2EzpX-nqnAui2IbIUB-N-QTGsyvVMZBj9N8IHvaD3u6Xj9DpGWlGPH93FOEZXRnawe1zzMgmdwgnKEsXMG0Lk93gTXV0p1RcCrfwGwpZkPxrEmBn6ClZi8tezK89_8wJlIj0Tn48KPRKP65pynp5NcLMyasOGtfmc05GcnhQAojznRNCX7xZ02pRs5rSJD4j0MEZ9zOv7qhNGiaNwazx6tNFD05aWy3HxCTzHwC_djcIUrpGxbmvg7pVt9l44QTbKB9Ot3xGuZKzq-eR72o94xX2FY0OPmgAAnYsA4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک منبع ایرانی گفت که تهران پیشنهاد اخیر ایالات متحده را رد کرد و تأکید کرد که تنگه هرمز تا پایان جنگ به طور کامل بازگشایی نخواهد شد.
این منبع همچنین ادعا کرد که واشنگتن بسته شدن مسیر کشتیرانی جنوبی را پذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20412" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
