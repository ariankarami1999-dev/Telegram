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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 18:13:32</div>
<hr>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسکای نیوز: وزارت خزانه‌داری آمریکا اعلام کرد برخی تحریم‌های مرتبط با ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/20523" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHpuuumOeRsDXp6srhwZnx9cMFNOnkHVfk1_feXayRGLU584R_Sn3jIQdWjMxG6Dpd9dAKUr9NNVQ0wl9zBM9zS9pucRJzw-9FU76HBB_6-bY-N7ydcyLrdEtLStqKgktAo25RmwSNrZx9msDReL-HmHu27thmLtmmpmD_G6tc9Xf6GQ3CVC-5ZD2Qexv12wam_6-U2_d9ZGveoC1dXbifAhkUOYW8NNO4S0PP4Swd8IK_KTZrr1ZShjOd71epGU3hkjpoR8poPmauopkxDZgDEhjsJ3CmHBqLJwAylhZaAjsdROfQ_S_TYqvYhNECD_fXZ3QOKYkUFq8L52sihmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=Nq7wBFOzYGwemfkVOIZh4odPUxSyfFl3XArRUMKlVOZYv4ZilFz1BruiZ6VCMJ5yDlQMCXfPC5xJNqFXRu81fQryXM20_EulxLv7T8Yw3bN7ms9DqMWJX6d9y14NqmU09VooMD7UPfxL0P4IDREln9r3hZQAUMZLqgwRVVtBUKpzPlSdHN17wU6f2kDSRkCQI5T38WjSNcfu2l6GG1fo2_yFCDo3JkSL-Jx0TVMaJkgRm4BTOrCe1POskljsT5Sa5So4rsg5gjByoSZU2u2B9jDU-TKH_xYaNjzvb2bQ8sL8zbbKRjtTJLvQqogeS9ulRqoMbSaMZ59aDRm49_zM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=VENzFfhla2gWYvDWmxvrE2Q_IXhbwau97wSNgy2JLj5nMdokSzx6kbpxTp9Vt_o3ujQ2d67f_Om_Cp-4_lIhnGr27Mo9KOC2y1YhtrVz7T8Uy_42iyqgriy142jrj43wQUA2l_UKUvKdwZTrvo0rLmtBsvxHGAjrpGYZdb1el7e8Y-RANEltGSxTx3CzAPNfPF2dupAL7b9bBxac30mPTCcm2jEM5PKaReGZLLjGAHntFn99ZWyOVdD3En5GX4JMKAYoaSPKDs3PCL4UDEsNrO11UFqAa_SZpF8j5XZOh8l-TMxAtjubAlNCT2oQAUAX7-FXwUxVNlz1CAR9Kz2dPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrkxahFiuoZyncwytOqtarkVZRAnJVxrgZt0KEZf7w16ZXSeP-Fw4LyeX9Qggb3hOcdHQa2g6EZSPEkPBHC4AZeaer04hzUFTvPAfYoKTfntBSkd88ABo3TkFlhztjn_oY8cZSbBmoRxHrYnyBk9pOsjRaokPZ0EBZCtsMQHkGpYC5x_mIULRrNRXLP3qjS7n-gf1bU8Lt4QtaCoBnrdq18uCCoQzGfZ-4Wi5H-N_xlusdoSWY_-rPWhhkEDA09Y5K8gn0hI6Pmpz1ozOWyx1EtHcQkglDopmgI6hdCTV3Dw54X8p_8C4ZVCIvrPLPjuHbP2IuUMcI_OCGSted0ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbnu0cyxF39Httw8BYVtjIcrI98TiEekiKmH-hDEjyekEPIYEehKB4aGw3B3mOibaBPI5shux35vJVWkUjt0v7FXDbU7kMjeWS8WlB1XrwgoeOAWEAPS1UOzroDiEknwDOU-SePaR5riEvXa0J1hbib5YtuV9-PYgY023X74jhrizmpQMgRgvB1yJvrLh5VS8NOaHCjHyUAwCW9Um-vTBYprSJTGs-PLw3WYxIV-VLIfqdBk9TKks-4ITPYIXgVOsYZkcqQfB6vA443jreIqQuc44MyYTWGJnHd-jrU2YPkwMO4bYiH7hDtWy9mxM2hanucMcdHQ5pOVWtYtZJ41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj2kcd3VjLeM5UiDmlm7nOytO2zuritJgWspwV5aYWBpb0mFxpVj1ZhmEZj_TkOKmOPQcrLaktYId0rPvGNvy06i2UQJYgLs2EYCH7aqUpSBN-yCXUUAD7SOMQsXIGewfMOQxhZVUjT5N87X4SNhBnZD3PSjnvuOijVvZm-XOCVEYZUCYC_GR41XTESOoJvhCQKKcqjolyPtg7BSYpyLqADIjk4tH6mentSrdgccS_Kc81opREogW-O1zpUnEYMrw1V6QtgaTtnOwHq1Fcy7u9LRLKVrAHsa9MqejLfAGelw65gJsklYDRJDE2jSccCBIfnsEOq0uzZyaLMC1gBzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbHA0j8LKj4wTZHj8rkK2SLhwRmUkvonr7IQR25bkHGQr8dtXSjaZx9QDnTf2RhkqdyLfUtflt3cwW4bQ3RseKr5ERp3JyF19RqfEkV_qDtQWP7JSiaRsQCkg39eqHEVFqulvtYYngjuAsR_y2rKMm0bMcYs2Bxdc5e-JaN2HS7Jxk4ugYh7kEOObf__tPh-bKoJprQQSXOHhGz4GVUagcv4gf98XZBAk4PvUJ4XjeM4x6suSLKs7S-WDYOrK8dzSoMPk_Us1uuEdNLfjXSBGty7phRT7KZB7XcUsokIzNenhnXHoCr1CmEVtJpK2kouVkdCTbOkqUbdEbrjEaKjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmsG5lE41Yr9RVvPz3NMZCWFdNvuXsfH0YlzuyjtKn7Fcf5miht_Zbvj_8c-miibg1Xf5gex08d1MEBOXtHtIQ8_nBkWSsulJjhksVwFv2ab2Jo9bCbhLqKaYoMcqv9plhxVNJlX2rFs2aI1ng5E0VLtHjyweBxMI_1RGxSIu9q4ApfP4mAe046Zlfm8LnztS_ncMEAKYTmsIr9OJVIo_FOVVIdEmj0L-gCX1ImkT3i2NxfXPY4u_23-H0wgSdZiDCLBeviiYRNwxK61f4oEYdCUVF3-sVop4tYkgIN4NELS3gHQxccRzRPBZHdZq0KDH_tdgOkQrBj0C6qh-qyaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=pQuC1-23aXxdmMoKkq2w6i4OgrG7xXOYebKkznL4Yos5f4grncrYvpcYv6L401WdvQcFDKWDDahRegVwlkzykyBS-03QmxkVV0P-KxiTyl3h4_83-wSCYtOYtgh6mD4LDlTqVXinXzZh-oF4zdJIJtwz5dWHaDcO13cYHv29Emwt4YwX805WLvXrD197OK11v8JC14P9ryCOQCxmaEHIZThyCCV1YMZPBGT0S59F-Qg9O3WEDKUN3qlYcFoRb3pI8dsXod9M_YtrDnRhWrgqJ8QbMdiLQ2vFA5xhJWI25ZXrSahZyOmERwuCaw6wVOXgNIz2oOL9wlAi8ahdDIZ50Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=pQuC1-23aXxdmMoKkq2w6i4OgrG7xXOYebKkznL4Yos5f4grncrYvpcYv6L401WdvQcFDKWDDahRegVwlkzykyBS-03QmxkVV0P-KxiTyl3h4_83-wSCYtOYtgh6mD4LDlTqVXinXzZh-oF4zdJIJtwz5dWHaDcO13cYHv29Emwt4YwX805WLvXrD197OK11v8JC14P9ryCOQCxmaEHIZThyCCV1YMZPBGT0S59F-Qg9O3WEDKUN3qlYcFoRb3pI8dsXod9M_YtrDnRhWrgqJ8QbMdiLQ2vFA5xhJWI25ZXrSahZyOmERwuCaw6wVOXgNIz2oOL9wlAi8ahdDIZ50Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqDRstfOQ3zjTI7KtmLFCHWGZzX3tFlKunFENwZkRabgFb0YhGUBYqATJrZ5VgZETHaYYa5vIyXtwMfKm-5u3GHY0aexOo_iSoaH7bskc1p1h1ubtRp4HgAgavTRcy22hq2ygMj42m3v850PeSyvfa82pCe1-9pfxH4avOUoDv0zlOYdU_WgT5AIUpMpfLxcTd3fasu0-orcJliN42IKL45OP34L7sKMloK36YjSxA9gPvH7s-JBJnkLYY6s-KTbTcCu3XWfXb4MWbpBS9nL33T7Wg8KqNIjnuHhBijJXI2Mrq3czRajcTWiIqOALsXXZHAiwXYr1gwJUMzl_mpLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QBGyR2-QKnHpkc4pD6Z1fO-eBFgwk2hUNbUm92r6Vm64o4tbvUfodHyGTTblIj568EJPqPiAI9YKa5bYz43pGplK9KRDymEPQ6M47WaTyph49H30EFkDH5DwiOwkDs9IECnyuBHtztDL7uwknKGHOZAC29t2dLX6DS_neU8-6LoKox7Pc4yqvXpq-_Dg8-hoyC157lgExCYyWvddE1SEFOXMDflj6QnsA3X1CZB1Juiq_xiOL3zDP4LhlOm3rx-RNhOu5mB0BwsPRYDSXXgzDJGZVMovkACvBIW03Ci2h7X0NbIuNgbLTZoNBCxXmkg_OAO15MbKBJzyYz_Mq69jN6GmIl-RPSx0eoW-T2JACKnfAO_dQqaMxuV2EmTGRJqVZJcMtr_XVjijHKviCBakaDYPgb_8XsQBT9p4CEa0f7Xx9y00slDBPyF3EvQWiI5HTgeSAFCX6Xn5XitxP8kYdazeYpp9UZdK6vy6zSLG6YizIjPXh9yOpV0lOjpEXwAdTnzRGzVK_3E-RLeQ6AIDziyn5ADyZ-GGf_tlvRtMyeBJOmLrH1c2zWa2AA8SVmGxB2VadFaktNPVkbN_f9xtsucmpLbSkbH4CEwJ8wAtUP__37bVVjKPlW3DJ2-hhkZJQ7qicQ2EBb9pFt7KxvODkf6GGTQa6rpazzFRl5q_ujc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=QBGyR2-QKnHpkc4pD6Z1fO-eBFgwk2hUNbUm92r6Vm64o4tbvUfodHyGTTblIj568EJPqPiAI9YKa5bYz43pGplK9KRDymEPQ6M47WaTyph49H30EFkDH5DwiOwkDs9IECnyuBHtztDL7uwknKGHOZAC29t2dLX6DS_neU8-6LoKox7Pc4yqvXpq-_Dg8-hoyC157lgExCYyWvddE1SEFOXMDflj6QnsA3X1CZB1Juiq_xiOL3zDP4LhlOm3rx-RNhOu5mB0BwsPRYDSXXgzDJGZVMovkACvBIW03Ci2h7X0NbIuNgbLTZoNBCxXmkg_OAO15MbKBJzyYz_Mq69jN6GmIl-RPSx0eoW-T2JACKnfAO_dQqaMxuV2EmTGRJqVZJcMtr_XVjijHKviCBakaDYPgb_8XsQBT9p4CEa0f7Xx9y00slDBPyF3EvQWiI5HTgeSAFCX6Xn5XitxP8kYdazeYpp9UZdK6vy6zSLG6YizIjPXh9yOpV0lOjpEXwAdTnzRGzVK_3E-RLeQ6AIDziyn5ADyZ-GGf_tlvRtMyeBJOmLrH1c2zWa2AA8SVmGxB2VadFaktNPVkbN_f9xtsucmpLbSkbH4CEwJ8wAtUP__37bVVjKPlW3DJ2-hhkZJQ7qicQ2EBb9pFt7KxvODkf6GGTQa6rpazzFRl5q_ujc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=YQQ788R5huCrqjFHUi9hojxsJyNrOH2U-n-cQNn6p3H6VNK1YlEeI-GvjHRWf8q-m--CxjQEcUIddgc8xrsVEwP8SQF5djpQwqBHuNxYufU9fdf0vlkuRGdjMqeTXttyVs_gtcmlVDcB9lCpLZGjZN1h8YIxHY1MgNyMPfN0hBQtggesVW-o059XZSUkEt5MRtpKnAHjd989oK1-HrOanZyKrSc7MvxMgYKfu2I0d16aMZT4Vc1KXjCNhOvQEm2QBH_Wq2N_1mtcMpH_16PPSoNPCMwG0x9ioyf-t95qqipag3T-HW7PxcplE--sxYrS0iBSwQYgeFivXhWlasHFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=YQQ788R5huCrqjFHUi9hojxsJyNrOH2U-n-cQNn6p3H6VNK1YlEeI-GvjHRWf8q-m--CxjQEcUIddgc8xrsVEwP8SQF5djpQwqBHuNxYufU9fdf0vlkuRGdjMqeTXttyVs_gtcmlVDcB9lCpLZGjZN1h8YIxHY1MgNyMPfN0hBQtggesVW-o059XZSUkEt5MRtpKnAHjd989oK1-HrOanZyKrSc7MvxMgYKfu2I0d16aMZT4Vc1KXjCNhOvQEm2QBH_Wq2N_1mtcMpH_16PPSoNPCMwG0x9ioyf-t95qqipag3T-HW7PxcplE--sxYrS0iBSwQYgeFivXhWlasHFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_t3QJDvcYOjdzyYGX_wr0vSJZcC2AFYNmldjaJZxlOsWF_fbmBWP39L83BHrMhai_i8l_mBpqbRK2oIzWAc7BaWKmGwtTaKjfqjGF8U21P_zNtVPPKWXsJKo3NqOGc_HV_23eNG-d8KTtkjHXHlxTsO8f-vy606a32aPICuKZgQS1mVykaKkf66Ou-E2qWOLtwdk9Cl27yD9G0i-L2kBkhM20crS0-KgznkeHTopzx3ZHUypvPKZ-_Qzds82S84DD_2VDD-PgzMJf2PQ6F0vwkUJuyG77k228UVuBoxOJRNfuBgM1AGW4b3uT6unTzP3BOsV9ksoh76zp8Ad04WxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=IHhJIU8uJSe4s_htNRaXa_thBshrkFLrgcq7kDqYr5bcPwMxDmjlfKxecl3RbHl2KZICzl-xZNjig5zEQ4Gr758qp4cui7BQ9C_h68Gc51WeWMRoQKPC6DJeIYb6At7TQg1S9QuHgkB98y7vW-4dyGXp_QL8y_B_PPfn7BqU8lVGeJHTFcObmI1tijLVTLqIIj5b8ZK63jMqfh4BuB22yc58cQesYRNR-WkgA56ILPoZWTWFyAPnqQzWD6o1WD-zcSQ0A4A7hx3NmRUOAbWv932E48tKxd4nihE84BLqftEZhmOdukcIf0gd41xQZjJuRPWcp0ny5NgKOIprXP-J6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=IHhJIU8uJSe4s_htNRaXa_thBshrkFLrgcq7kDqYr5bcPwMxDmjlfKxecl3RbHl2KZICzl-xZNjig5zEQ4Gr758qp4cui7BQ9C_h68Gc51WeWMRoQKPC6DJeIYb6At7TQg1S9QuHgkB98y7vW-4dyGXp_QL8y_B_PPfn7BqU8lVGeJHTFcObmI1tijLVTLqIIj5b8ZK63jMqfh4BuB22yc58cQesYRNR-WkgA56ILPoZWTWFyAPnqQzWD6o1WD-zcSQ0A4A7hx3NmRUOAbWv932E48tKxd4nihE84BLqftEZhmOdukcIf0gd41xQZjJuRPWcp0ny5NgKOIprXP-J6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba08IiInS0lmYu6v4s5LYZMQAb9UBVQo6xJNrPrGMJ8O5mQ1K8MIhOhU_55-9YvS_lZDgdXX2SZvCJn4203vJjQCX9YP6uQhiVWLgAf9NbMSWYEYs2MsIZ2kAChnAPcyOTOfLTv5ojzbIO7hGXifWE7HwXY5wkteJWrP52FpZ9IfcFtQi8dqY7fl0T3qcxXm_gi5C_aS5I0f3N-zbE7u9YQtfGsutqFWjX42IPMLvOqdxaNAOQ6Hp41C8nDL087HfkP05eJrHiTW-hEpA_s2K8poRfeovho7zogJ3JDXqTCs86yqvOZFt4KEyka6fAYwwcmXoy6WcXrJhXF78Zqp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=LagDja3sWPjCgfkh-aH-oBF5JF767D8xTGo4B9hQQCoC51Hjz32Yz7c2WwwwDdEWt45PAPDhC0fQQ4srBKZyfHSn-n2iVFxo6HWUkDhyLgdWCNedppZej5Odu3GB7qEuzywYoMYpdVp0N29XNjV9O7ANE_lnqYfL9LX5LKYDeRAVhYRLsOPuLchljmCjhS7z_8WCvAbnht_K4L5--uB1MNypCC-TRT-To3LNdBDhD-jVK8LZ3t6PjifVT_kSqjE85b4nDaC66JcDiSCKvf1ByJUdVUNZZ3KzhqfPLtbwTlJNNfkFHOotHzskwt9_zEEh2lWZ29k8Kiyfk0DMcAWW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=LagDja3sWPjCgfkh-aH-oBF5JF767D8xTGo4B9hQQCoC51Hjz32Yz7c2WwwwDdEWt45PAPDhC0fQQ4srBKZyfHSn-n2iVFxo6HWUkDhyLgdWCNedppZej5Odu3GB7qEuzywYoMYpdVp0N29XNjV9O7ANE_lnqYfL9LX5LKYDeRAVhYRLsOPuLchljmCjhS7z_8WCvAbnht_K4L5--uB1MNypCC-TRT-To3LNdBDhD-jVK8LZ3t6PjifVT_kSqjE85b4nDaC66JcDiSCKvf1ByJUdVUNZZ3KzhqfPLtbwTlJNNfkFHOotHzskwt9_zEEh2lWZ29k8Kiyfk0DMcAWW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEreAI4l_iWdF0N83A0QXJicNBotNNz_Tl9TdaO3e4yRnWQFF1Sq08YZpaKcvKFBJ8sB14U77WWZHKwsouX7wn1nWmaNzpMuojs1-_xqEZJBUM2hs_TLPFlhZcqHe96qaeI8NYOxAeriirjyYG9wvmjD7yhwUMDQGAN0Ed1GqmaCGBJoIG3S4upZm6HrnAaazyiLnWUogUHVBubaXlvWlOA07Fqhe6fvDwWnX8MifxU2wxw2mG6TWaIAAw-DI1uI-IsG46h2LwK1v-2fWPiGcMFw_dU8TRamhW_PMSjdEAfxwEWLWfhpiTf63LrJ1mgf_leK7kVEPGYou8-IRJ9x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtmvBrMI56v2Hmh-PB_TA0QVEwK4qhCURJyeZsjjAAVx3jNOn4zlGt4oNzGRGx_M8C_XPxa23DIvBYj2aeTtJieQOruBG5pvqkuK-JE-pzbw6Pay-uiRHSGutd8hBM1pfC-i7qSoXELZZ3geMm6-ZomxNQdKM3DpKZn82R3vnZ_mYgIgSbNX8MUScTSeEuDzxHqJZCKQUPNnVMKOCgpmlad-XA5Q9A4W3ZVPI_7bDqCOHLPJtxJEFN7USH7IxpNKBixF9ux-tIs4ZjyzMnVu9YamquNf3GH27l8uFWFxYZjZZwbeu37dkx5bsqNgdXVOxoyyZbw_oSYZHYOBesHJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=P8kohplVOyGhYR5TULhU75Yo98YWBHtWLOHflcuE1sXu_e09jbJvbPTTHQVqZ6i--BLlgyFQX6aQir08cyJmEIYXUwD0yaewOD0mxb0Y70ql2Ddpg8V9uK9aWQPg5yv2HtELsj4oJvjDFMo1wKuxcl_01jmB25tDzKhGRKdiGRvvfSvf2PA-BER4iMSy3mzDuH4Cf2SMrwir_iuFMHnSA1sIbP1YWCK7-t_B8Yoj7k1FTttftEYpzP48C_4ilCckqi2MSGxetW_u-QD5Q5Omj2IEV81We7bJaEW0duH0kf_TVgvBWIc7mxDO-BvV_MskIb0MsPqvrTe3Tf9b287KVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=P8kohplVOyGhYR5TULhU75Yo98YWBHtWLOHflcuE1sXu_e09jbJvbPTTHQVqZ6i--BLlgyFQX6aQir08cyJmEIYXUwD0yaewOD0mxb0Y70ql2Ddpg8V9uK9aWQPg5yv2HtELsj4oJvjDFMo1wKuxcl_01jmB25tDzKhGRKdiGRvvfSvf2PA-BER4iMSy3mzDuH4Cf2SMrwir_iuFMHnSA1sIbP1YWCK7-t_B8Yoj7k1FTttftEYpzP48C_4ilCckqi2MSGxetW_u-QD5Q5Omj2IEV81We7bJaEW0duH0kf_TVgvBWIc7mxDO-BvV_MskIb0MsPqvrTe3Tf9b287KVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8PAHNrssMROKdT5ntMgP0PUZjjz8f7WplJIeFTV_rJLF1rouy5veIr30PmDWpTGaEeOON-Ga9KV1I-TQlLlcXR07p-bY-MafEG4a3RhNqcyzmQt0BEIiK1pI7TTpRo1lIghb7XH6miP0QzyleHtTA_-e2wZye9bSIDKJ_w4L3xGaPI3pKHPmN7wAETbIFH3-kARnVRdYy8UFu9EllnNuGG4W5sUGmS9zibpIahP166fSnfV50_kxf3JNf2JxNLe2BBFEv4Jk0ORab2CMP1pL5WF_rGufpiOGwoJNvgqK2UuUyg_NHjsulCULQlaBXr9JtW6rgfeB5i92LLpXvOpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnHfWcDfUoxGLwgpHyhfEkla1equFi4IRtfaZkvna3j-2biIZxzPIwEUyXO5hqtvIaJHtai40ajx7Y7hQGguZ-JborhJTCMziYlWSP0xGRgufNsYtqy5Y_pOLLuTfXICLU6siYisDR-mgsjknZLmS41jZDLfrNkSVBmfrtmmlfb5MskIrz66ujORALAFYUTP4WmyE_MZEYtM0Ef4r3m5I11z_LKV5xFkiwQ7rWaKCKYfgRuLO4BSy4sPBqLEZfOr53bH2SDmwze5_X3RQ-y0J9Udlu2yax-9XD3msNp8k4Fi_EipO5P0K5C7NZzLxADoc1lz9PGjuP-zejUAO1l5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM03O-T96icQF6wtt1lpznZKNjYRgCe1BVx7MlpAMjVvDDuQ30NnHc5ZkiuGqEjZ3anm0m2nXB1jKqKmwBeF_OHZE2SsEHrgVqqcLp0aWOwtOkZ1TaXD-B8RkmdJ00CkDulbk8imHqyGMzGKm1P3uzGsOd9VSg2AXrTbgfzgK2Zdh0ivp6AOBCxgvFv570a0uZv0iuZM7gdZ7hhpy_AZHmQpod1jg9Tp25gUnYFzgUHCbFZUq2FeKGmtwown8l7StthPDpdXVR6rGN7-3oVXqOlZ6ba-oczpaxNaw94oV1ic4fCp_ywKy2QCnr5trOMMp-yWPejVDEwMl_mXp1cdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWpN8NFc4u4-ys0A9xSQ5SU7B4pEgsM-CG0i_GX-PtRldntVC2gn5CLk-wtuoQydUkWpb5TgzbYA1LLZygbBCwaP0o8Un7Zigj0nd3XxAQ5IgKgbAsyWhPClOGGP6E3Z_oJgvLzsmwFEhnwAOk3G31Ei6cyDfRqM-_ThWOu8mnlVBi6pbrTrVp6dZpG8-5eJ96xw6MWOLzZbcpm2A9VFsG5ZjXO-LD4ARPcmbBDFZcP9DbG3Pqf_3lsEyomRNarlpL3dYR3OaDDsTnYXNPwQtYgY3mWOXBWptFMvHvizjO6fT2oAy23ki-j1OfWnZ3hZV5Vud8K-FstFo10B8PcjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl52Fekz7na98pKkKgSbZ_p-_86l6nVSuERPTV1URKSc5BDVokUO6DRpg3L7oevupowFtMiPACWpt9wg0ZcAVFnJNeWCdmYbIcF7ZAiTN7Tb9rMHpdiz3ZbEp-vycJ40I6EmBkENSbhnl-DQ0qP0saEPf4CL_fC6qBSz65mfCjrhhQIyEnBROxIU49ysyULGmdN94iiDNR2hOA9j7fRbUILrH1eqcmXslWAz_cbRPzGRk3phLZvnEROZvatuDBcfzPdsZnOK8PjlDoYOmkII0FcQMUj5IBYL1cM4Ak0Tmq8A1KoQaS30FfGk7Q9albjREJw6ahsWMWB-t5udhj9zbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmzdQkaKoRTBkTDF3eDhgchHUl23kbnn7dPLjxttg4BwvCEbVv6Bb1DCH5ea9bz1xCesnhcuqoQgMoGJMBE_5uCl6gNJFVbok9eiWMWsY3RhgOxRN5GtogpbhSoRtsvvMovkoiCgz23sz1vVTs24U_tdU2ph92AIURF79U5HFPVF7P9X9LJlxF2tlQr-_8YcLpH7ZKXJkLO0LfNfZcITUt8JjxRPzkTfPC9Zo4MOe0x1a8Z4jWZry-ibj5QRat-w2B6u9AeEvpUsPCA3FokWYQ9qc81HsOOJs6HpvgyDUxFzOMuyrUNIXa6PxooNjzUyp10T5ivnQPtsNfiAz4w2Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjcuUzDLy01fY1asV_4MOV6M6HaCtZ_lLpfYiBz1mwYOeuxwYCrISWkExSGFrnSnurCrgvlEMa4AuL5-lP8aPSZ6GA9cOfXYcZsXb5-0H1u7FzR__psI-WiLMUHJghls8XxHpPuayzEsvISvZJjwTw1QeWVQ7fbCNzauIqtguG-cicWPskeMO9qzY5Y3D1B96XNm8aB9duE5g1B82GbXuJ_qKZpnp7LD8BSa-_RlLQbFo-MCUZOXhzIRXYMR8ZMqDgv95KRgIVhBHSOgkleID3sE4B_1YPntTQRpH6IQlqoTjjK9YS8IQJ82JR8a4EEyBljH8GFeBDXyNi3GpEgJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1xEf9-xAJM-3eNE2x04JF6eha-cCk_kaQlWc6I652Q-zAmOgPQVVeAXdH9fguJN3dS3usucdSopreo4kxR-EMkhHbde1ZlMgvdTIC40zDSUmstxHwhtUkGgwk653iWnnRauustD1hV1d_4l6YphAKmL1UxgrJatMutHokGRHojSR9xBKT496hsFYZiw-3zS8IIedTpX2qRiOPs7RNxD7KfmBgM_anV-JASaqJDZ39EXfijy8L0KPp-d5xRlkjcG2lX74QLfjZJajOfMfiC88x46_PXACW9Q31OnMQhuAcdKYvgRQwiYAl5QQNHQBZBflWJ9NER6rHaNmmdSyMi2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX3rBtqDZxqFYAMBJD1dCY-uoh-FOxMdN-3BEYY8tZn7ZkJoWnM2W3b0l1n12IpzRX-INBSzeme0h-5FYrdRE81QlDaLqhm4w8Uchz1mgHIQA1gkvR-jxRnzwWq_Qot4n0CUNn1ZKHer1k4mGNYPhas-ElwpxXW6S_Rq_kD1rKLsnlgY3WKyi7EzQ9oFLZ5PEKcLAaH5NvSVL8nCFmANahqplPsXbNrQmAmkNTYQeCpJxLxFYRapzdyV5v0aRsZ5Ud1qBAlZHvAU-le9NYKfsSU5jD0F7FilPBHjPK9WJv2TLzG46Kz_ZA9iPrxwuTvM2o9FU_xCvydeDkBq37dHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFv7pQs0mDbSxxfyU2gCE1Enn2D6Nh-CzJseCVnnSRPiWyW601w6Sk-udPIxGMVBNMc5J9GJurh5LiGJpYlYXmMrIvrg0qcxA5yrUNfOS0iDdtKzp4OfD34HrPNhvOMNW7ieSofeilazAgpUTdpONEADRsuQO8PNXMxPNSkup6HcxkpvrCqNZOcJzFgn3bvMFhi5zUxF90VAEMknnfVdqCsJhQoG9YrvnrsTMsiC9Uf6mJwAbsPECwlCaEGlB3Qz2g8eq-ops0YjfHld5L5fiPpIPQJQQ9MeXBSSplcd0tKj05QEzA_PZaVorLCPd4oJHiCmLMYOC4WZ2cJbqEEKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=XKpZABfD6xNfp2Sl7CIjEjrUxD9MqsJKKDGcto1QnCOb6tTBoV3dHtXaR2tcxYUXQ_xlz9bsexCKLuTJXrvBwMsAYr1MadF12yW8woJ7itqYK5EJ8W5uPFPGhRw8PSVHmlrSWJqVfok3IY1Qx_W-z-ZMZOIs5Mra9k7jwLpTycS8hkL34WeJb1rsj4RlL8EwWklBp9Hpm7akLkpgoapnjljYQDwYzV9cbMqD8jUjYixbnKu2y94hccCNnZO3OkQVGui3wkJencLz_QisphvDfo9TAiBcjvdTly4rNmHZOHNUV8yfa7J49WuRRG4YGGeUkcbIJJ8TXmT2sYzlcKHXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=XKpZABfD6xNfp2Sl7CIjEjrUxD9MqsJKKDGcto1QnCOb6tTBoV3dHtXaR2tcxYUXQ_xlz9bsexCKLuTJXrvBwMsAYr1MadF12yW8woJ7itqYK5EJ8W5uPFPGhRw8PSVHmlrSWJqVfok3IY1Qx_W-z-ZMZOIs5Mra9k7jwLpTycS8hkL34WeJb1rsj4RlL8EwWklBp9Hpm7akLkpgoapnjljYQDwYzV9cbMqD8jUjYixbnKu2y94hccCNnZO3OkQVGui3wkJencLz_QisphvDfo9TAiBcjvdTly4rNmHZOHNUV8yfa7J49WuRRG4YGGeUkcbIJJ8TXmT2sYzlcKHXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=eiZDWqvMUnvuSxXLuU3tR5-fQT2raDjElAmBznMsXBWy-Du3uXAgJGSOHTPhihZhUfFPPlutJuqt_aUy8aYTTGeb3v8FklyudkQycY10WS9_5K7yWuRPE-P8LclN9dA0Pg_cTxxVvBLk0QLjcj_MlcN9-0zSalfiSsowFWmIB8zmGgRU5PDzOmknfCE3eIFyYKzHKWUR3hpnZe7jFOFIMQXfwCkDeYTH2xjOzuUG9lGI-Xzylz_EhPkSUZASwK4dKVtHUzX4YbQ0fJLEuCWu45HQdawncL60A4JYMZbILZyl3k2xoALDFBIuzF9XTUeoYVOYQw_CUTtF7qV2PApSpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=eiZDWqvMUnvuSxXLuU3tR5-fQT2raDjElAmBznMsXBWy-Du3uXAgJGSOHTPhihZhUfFPPlutJuqt_aUy8aYTTGeb3v8FklyudkQycY10WS9_5K7yWuRPE-P8LclN9dA0Pg_cTxxVvBLk0QLjcj_MlcN9-0zSalfiSsowFWmIB8zmGgRU5PDzOmknfCE3eIFyYKzHKWUR3hpnZe7jFOFIMQXfwCkDeYTH2xjOzuUG9lGI-Xzylz_EhPkSUZASwK4dKVtHUzX4YbQ0fJLEuCWu45HQdawncL60A4JYMZbILZyl3k2xoALDFBIuzF9XTUeoYVOYQw_CUTtF7qV2PApSpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=B9vPnBK4Z7oO3XxAC-TSoasv9qSnLuvt4RPhORdRhk6GTXUggP4LD-RKGkxfsOSuQ_HWdUlxN3M0thMHhrWHLSPt4bF9L3tuS6-YertHkJMUYMQzj-Z8ae3bKgcabFxWhPMRagnSRtZaaERIrwYrr7OLRFnE8F2mBdixOIwXUfxPLSUP8ek2-GnVHzByvWLVBTLZRNj1taJakqyHt2vu45iETYX50j-rGOSLVm6_YZtXgXkQk5knmOZ6P8FfcRNHDA2vtaKwbUmI0vctX2dT5G2gRWyXyXbAAZ8_UsEWPvEyZhTKNUC8enV_shIu2bHoN6-tRrX9K13E0yTJVsYEvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=B9vPnBK4Z7oO3XxAC-TSoasv9qSnLuvt4RPhORdRhk6GTXUggP4LD-RKGkxfsOSuQ_HWdUlxN3M0thMHhrWHLSPt4bF9L3tuS6-YertHkJMUYMQzj-Z8ae3bKgcabFxWhPMRagnSRtZaaERIrwYrr7OLRFnE8F2mBdixOIwXUfxPLSUP8ek2-GnVHzByvWLVBTLZRNj1taJakqyHt2vu45iETYX50j-rGOSLVm6_YZtXgXkQk5knmOZ6P8FfcRNHDA2vtaKwbUmI0vctX2dT5G2gRWyXyXbAAZ8_UsEWPvEyZhTKNUC8enV_shIu2bHoN6-tRrX9K13E0yTJVsYEvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=kbRdmlQxxm-LItcij2LHWfQIbtDyfQZ1m_si-FGah19yKbLglBeLZ7aI01ujcLcDWaI17qoIRZH2TLbCjafFg-PKPxcD3nYW-f8TpVNAPNW2rJ8_mgdwZbkf13zJ2cPFwUO7FChR8nglhLogpJNkisvs8q72o1KSiowW4_unT4mRwoHGOdXlxUjs0F_NFa0aZZkZq9tIe4olDRCgJIUkaQZKNVxxDe-xxWs0f7ywmv1Ua9eoq23pdkxATsTTGFVx1pIxHp0lKXhlzwouIRgHQuK-3KK-6jVKkk-Oba9ls6eDNG_ORT6xNnyyXsVewFXac2R9mC1xqKbtJ10hS1YjC00-fPwP4ZfWjQ_EU7up9c4LIg601BfMJgYMKiPo5fkmjgpsgeS827cdCggm23_2aj9TToMRQw_B2pIeAxOmoFVr0cj4Jn6r-fOAaw65Xsv1b_n_zwnEVDW_BL21c-qMh3tNB-8su4c9PYzNYg3H6n4EyXv-bF0R2c9MAeogURoQARJ3btNExAh45LONDX7V5wNiq2R8ICxn-ed4bX3ZAwc0HiOdzeOgEAz9wuSiSmkyu1hq4Yk_IqmH0SEgqaxLmu-PLoS4VTPabbPoMCckbsyrJUM088zulPDU-UFw9YqTT8FHkp_QgBEcoZ6sqQ9KLTaCZOauffhxeuvkwuAYXJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=kbRdmlQxxm-LItcij2LHWfQIbtDyfQZ1m_si-FGah19yKbLglBeLZ7aI01ujcLcDWaI17qoIRZH2TLbCjafFg-PKPxcD3nYW-f8TpVNAPNW2rJ8_mgdwZbkf13zJ2cPFwUO7FChR8nglhLogpJNkisvs8q72o1KSiowW4_unT4mRwoHGOdXlxUjs0F_NFa0aZZkZq9tIe4olDRCgJIUkaQZKNVxxDe-xxWs0f7ywmv1Ua9eoq23pdkxATsTTGFVx1pIxHp0lKXhlzwouIRgHQuK-3KK-6jVKkk-Oba9ls6eDNG_ORT6xNnyyXsVewFXac2R9mC1xqKbtJ10hS1YjC00-fPwP4ZfWjQ_EU7up9c4LIg601BfMJgYMKiPo5fkmjgpsgeS827cdCggm23_2aj9TToMRQw_B2pIeAxOmoFVr0cj4Jn6r-fOAaw65Xsv1b_n_zwnEVDW_BL21c-qMh3tNB-8su4c9PYzNYg3H6n4EyXv-bF0R2c9MAeogURoQARJ3btNExAh45LONDX7V5wNiq2R8ICxn-ed4bX3ZAwc0HiOdzeOgEAz9wuSiSmkyu1hq4Yk_IqmH0SEgqaxLmu-PLoS4VTPabbPoMCckbsyrJUM088zulPDU-UFw9YqTT8FHkp_QgBEcoZ6sqQ9KLTaCZOauffhxeuvkwuAYXJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
