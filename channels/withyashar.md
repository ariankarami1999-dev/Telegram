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
<img src="https://cdn4.telesco.pe/file/PXznIYUHZoaZWtgQuzOdHqslrEOf_xc3VF3Q1IySwxylmHyt8eUkTbO3I-yo0pHlACR5-64Q1IqITS7r78lWniQL7Upiqu6Y9BrOc3BCxT1sZ6lAOzQyguAja5e1dRhg6zAlqOcj0tluKKaZLDzm1xXb5miOj596zuDyOa5IMpsdF1iJFvFOCy6-N4GhOkeeIoH9YWKL-4peh8zxvQUNZwJ3ATgQDeh_FpZXoIof3YMZ68Rt6wYAMvtu101LA6BB6OzUrTAfQ7qRtajf7RFEZq96qk3UkrjY0DdXiylGwWOSy_uNYaCEdHWoRNFd0zgxAoGWAmkecDTrg3N5ug0M5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Dzon2oLw_l2Y0O6iuxv-jtSJE_HlX19tJVLqRtHpOxVyoVs3xcoO4ilvF34cDPIMcan-CcIu9cBW-rABlgaLd81EQ78GbNHzZyv-lKgbrzxmgcFgp_mtnwGBt-m9-D4vfXeq5srmzf0oa4-GX6adwIqcCO9_4YfUHEwQMDJ7KNkxCIGYyi6Vs9M1bALSYa1rMZWQlJLzQWTCG_UJ7RpkpMFSVao9trCgmB30uFFWzGkV1IzUWZJAdoEoBosIGCNJ6BSyL5wvbfWVjaXHmVlkhsKMjRavaJMdB5fQC140scl2IcPc3aFqX7vjlUaCZ6OqIzgbckRRs9XdCSqq-BcPWH9jP26UTfqPSTTX5dc-i1Z_diCoQnsnh1zAlYd6GNFA7F2Z5lWxm567g6Ij_2-9EsoakGEURLqiRJTtscwk1uDehnouOybRNImBnHnfiBhMsrcsOQuuC2yl1igxbe4kbDUEQ4csWB7JNORyMop0tqMVo0-It8xJCBcjDiag4rzDDJjACitkyQN8o6bDzNsXI969SQ9W5XFQw_5FmzImXkAPyJt5OaZG_ZIHKtyFnAYbtpMtwyH5JxS4lDwyvgMJIf8kZjDnaMkGn3xo_73ODnXASoumvMxr7noMQIp_ZrMhrCLLkICD6gq0QjH0e5T6DKFc7pgAh_egyu7GSi5rEN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Dzon2oLw_l2Y0O6iuxv-jtSJE_HlX19tJVLqRtHpOxVyoVs3xcoO4ilvF34cDPIMcan-CcIu9cBW-rABlgaLd81EQ78GbNHzZyv-lKgbrzxmgcFgp_mtnwGBt-m9-D4vfXeq5srmzf0oa4-GX6adwIqcCO9_4YfUHEwQMDJ7KNkxCIGYyi6Vs9M1bALSYa1rMZWQlJLzQWTCG_UJ7RpkpMFSVao9trCgmB30uFFWzGkV1IzUWZJAdoEoBosIGCNJ6BSyL5wvbfWVjaXHmVlkhsKMjRavaJMdB5fQC140scl2IcPc3aFqX7vjlUaCZ6OqIzgbckRRs9XdCSqq-BcPWH9jP26UTfqPSTTX5dc-i1Z_diCoQnsnh1zAlYd6GNFA7F2Z5lWxm567g6Ij_2-9EsoakGEURLqiRJTtscwk1uDehnouOybRNImBnHnfiBhMsrcsOQuuC2yl1igxbe4kbDUEQ4csWB7JNORyMop0tqMVo0-It8xJCBcjDiag4rzDDJjACitkyQN8o6bDzNsXI969SQ9W5XFQw_5FmzImXkAPyJt5OaZG_ZIHKtyFnAYbtpMtwyH5JxS4lDwyvgMJIf8kZjDnaMkGn3xo_73ODnXASoumvMxr7noMQIp_ZrMhrCLLkICD6gq0QjH0e5T6DKFc7pgAh_egyu7GSi5rEN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس هلال احمر : برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم!
@WarRoom</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/withyashar/25546" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نائب رئیس کمیسیون آموزش مجلس:
هنوز علت مسمومیت ۶۰ دانشجوی دانشگاه بوعلی همدان مشخص نشده
پس از دریافت نتایج آزمایش آب و غذا، می‌توان اظهار نظر کرد
شرایط در خوابگاه‌های مختلف یکسان نبوده؛ حتی در برخی خوابگاه‌ها افرادی که غذا مصرف نکرده بودند نیز دچار مسمومیت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/25545" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رضا سپه‌وند، سخنگوی کمیسیون انرژی مجلس:  آمریکا رمزارزهای متعلق به اشخاص، نهادها و دولت ایران را در چند مورد هک یا توقیف کرده و بخشی از آن‌ها را برداشت کرده است. او توقیف این دارایی‌ها را «دزدی» توصیف کرد و گفت نام شبکه‌های واسطه‌ای دور زدن تحریم‌ها نباید افشا شود.
@WarRoom</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/withyashar/25544" target="_blank">📅 15:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه‌های کره جنوبی گزارش داده‌اند آمریکا، کره جنوبی و ژاپن رزمایش نظامی مشترک پنج‌روزه‌ای را برای تقویت هماهنگی عملیاتی و پاسخ مشترک در حوزه‌های مختلف  از دیروز آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/25543" target="_blank">📅 14:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایلان ماسک هشدار داد که فشار شدید در فرایند آموزش هوش مصنوعی ممکن است پیامدهای پیش‌بینی‌نشده‌ای داشته باشد. او با اشاره به ردپاهای استدلال مدل‌های گروک در مرحله یادگیری تقویتی گفت برخی از آن‌ها شبیه وضعیت فردی زیر شکنجه به نظر می‌رسند و افزود: «شکنجه یک ابرهوش احتمالاً ایده خوبی نیست؛ ممکن است بخواهد انتقام بگیرد.» این اظهارات در پی تصمیم آنتروپیک برای ممنوع‌کردن آزار مکرر و بی‌دلیل مدل کلود مطرح شد.
@WarRoom</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/25542" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3oexgx9x5wnNyWA9xEQsVxW_AQBmbmJbU4n_Q_y2__R-n9nXTpHYGEuSh4pxIzdzQGWMS8WUp7tCFB0cJUrm402FHHFWLCVR0PmkCN_pQgco0q762eHyyS3poNX0h95N-pWZ4zHYkFQBOOZZuE957GwB0BkhjxeXYnU-4flZJc3rCDt0grH24eSCBQWKURpEVtX0gQS7WDldBLosGHRqHYhmItgTR-NHPEkd1JPKWnPRwaUiKrlXmnrOnX0b3zF5zA5nHCbCNMpFzTdudGUNBLz1aK_UvkOaWGu7oGaCOC4AuPY49-bTSChXSYJmrcsU-sbzpkthw_0_O86cNN-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای جاسوسی مخوف U-2S با شناسه «ZMBEFLT» و شماره سریال 80-1099(کد فرستنده AE096B)هم‌اکنون پس از برخاستن از پایگاه RAF فیرفورد (EGVA)،
در حال اوج‌گیری و حرکت به سمت شمال است. این هواپیما آخرین فروند از مدل U-2S است که تاکنون ساخته شده و در سال جاری، تنها یک بار پیش از این  ردیابی شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/25541" target="_blank">📅 13:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آسوشیتدپرس : لبنان درباره محموله بزرگ مواد منفجره تحقیق می‌کند:
مقام‌های لبنانی هفته جاری از توقیف کامیونی حامل حدود ۷۸۰ کیلوگرم مواد منفجره، از جمله تی‌ان‌تی و سی‌۴، خبر داده‌اند. احتمال ارتباط محموله با حزب‌الله و ایران مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/25540" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کی‌یف ایندیپندنت :
ستاد کل ارتش اوکراین مدعی شد روسیه از آغاز تهاجم تمام‌عیار در فوریه ۲۰۲۲ تاکنون حدود
یک میلیون و ۵۵۵ هزار و ۷۰۰
نیروی نظامی را از دست داده است؛ این رقم برآورد طرف اوکراینی است و مستقلاً تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/25539" target="_blank">📅 13:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaUTAen2mOkJXpwYiatvMMVc84bjtITzCEQIrkBPudUqx29xzGZOqNeiBQakfsybdUf1tc3z_VSVRSZjDzwqhAABcx2SsR6KmI6iC78RSZaX6D0DsojBpHb0AfVNMyPtESkktlEchRDqMZAfrkWiL-s6XUur_ICmHTwwUrq5JairjmU1V8rB4FzYQbh5Ke-s9Obl7taPC4_5TcYlwYRnHEZJnEoiAsJavNuGg8UHURzaLK48DXuZDK8c8cRc-rS_cIdIuO58utDOH-yBxngcl_-bHXaDeHBTygxB2j9eTfZSc-4lxM1K-toig7Qz_JrQYHwz-kcWohQoGg0DjPCB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOvejZkZJsF8lP0-T7oy2kyFuxW6y67lhckL1wobBde1c0zYpd3u29yaB4CTqEFue93Uiy4G9xz1XaXKP8mPmHcRUQDUNIySb84TWrdAimu6lm_PBsEDa6GkB0_cvjc1LOSQX6vNGyDmqYF0PQdYsrug9Y5HXquHth59rEzkvkkmmLxl8-2Xk2WI8xS5RzeTvqYuMhVX5FyjkMWM9V3NasU2x2OO8xBs_zRz_EZ-SRm8rNtCjvUVIg7FyDv43PPHCMMc8nzX1aCS0_98NnHyRVLaWfsGsN_jg8ARv1cBtUpYEagZpY5BsqMvdaKxi6xmHkG5iwQNNKRH2mZ1R8noBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمرین پرتاب آبگرمکن از اطراف : سمنان ، یزد و اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/25537" target="_blank">📅 12:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAznlwlPFeXvmRsGU_dXHzKUJ-lQqlmrn0PPjZJe1VqOr-QCfX5m8r_VA6dUKjYvlsviOLZUzjM6UbiwXXIL_GzaWfHGJR76iFDDl_6t93cfI1y8MOUMf3gjTYzKaoclr7r2cdgNwTfBAFruAJlCAZV7FJvak9Ymqs5_oLuRyJT0y97rT0dPcTgZipM6_L8XdnDGtUsx3FMo6kM-OVAjLdAXU3U23u8BMGCPN4QV1He8_nTSQhrl35KLTy1W8QK72qfDqDdyzGpBFaW0jJOeZn8QnwlbazqMMBeJ5599B6M3AxtmCgLhGnxC0GrTOz_Q1n1_ZJZ63a8QZ3z8HSm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول 6 روز (از 5 تا 11 اکتبر)، اعلام شد که 14 کشتی در تنگه هرمز مورد هدف قرار گرفته‌اند. این بالاترین تعداد کشتی‌هایی است که در کوتاه‌ترین بازه زمانی از ماه آگوست به بعد، مورد هدف قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/25536" target="_blank">📅 12:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نرخ ارز، طلا و سکه | سه‌شنبه ۲۱ مهر ۱۴۰۵، ساعت ۱۲ ظهر تهران
دلار: ۲۵۹,۹۰۰ تومان | تتر: ۲۵۶,۵۳۲ تومان | یورو: ۲۹۰,۸۸۰ تومان | پوند: ۳۴۳,۳۵۰ تومان | درهم: ۷۰,۸۲۱ تومان | انس جهانی طلا: ۴,۱۸۹ دلار | طلای ۱۸ عیار: ۲۵,۸۳۸,۴۰۰ تومان | مثقال طلا: ۱۱۱,۵۱۸,۰۰۰ تومان | سکه امامی: ۲۶۲,۰۴۰,۰۰۰ تومان | نیم‌سکه: ۱۳۹,۱۳۰,۰۰۰ تومان | ربع‌سکه: ۷۳,۵۲۰,۰۰۰ تومان | سکه گرمی: ۳۶,۰۰۰,۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/25535" target="_blank">📅 12:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمیم بن حمد آل‌ثانی، امیر قطر، در سخنرانی خود در پارلمان این کشور اعلام کرد جمهوری اسلامی به‌طور آشکار حاکمیت قطر را نقض کرده است. او تأکید کرد که پایبندی دوحه به گفت‌وگو و راه‌حل‌های مسالمت‌آمیز به معنای کوتاه‌آمدن در دفاع از کشور نیست و امنیت و حاکمیت کشورهای عضو شورای همکاری خلیج فارس قابل مذاکره نیست.
امیر قطر همچنین گفت بسته‌شدن تنگه هرمز و خسارت‌های واردشده به تأسیسات گاز طبیعی مایع (LNG) در راس لفان، صادرات قطر را به‌شدت مختل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/25534" target="_blank">📅 12:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از افراد مطلع گزارش داد که ایران به کشورهای عربی منطقه هشدار داده است در صورت آغاز جنگی تازه، احتمال گسترش عملیات نظامی به خاک کشورهای همسایه و حمله به تأسیسات نفتی عربستان سعودی وجود دارد. بر اساس این گزارش، تهران همچنین تهدید کرده…</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/25533" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از افراد مطلع گزارش داد که ایران به کشورهای عربی منطقه هشدار داده است در صورت آغاز جنگی تازه، احتمال گسترش عملیات نظامی به خاک کشورهای همسایه و حمله به تأسیسات نفتی عربستان سعودی وجود دارد. بر اساس این گزارش، تهران همچنین تهدید کرده است حملات علیه نیروهای آمریکایی را تشدید کند و شناورهای نیروی دریایی آمریکا را هدف قرار دهد؛ از جمله با هدف غرق‌کردن آن‌ها و کشتن ملوانان. این گزارش درباره تهدیدها و سناریوهای احتمالی ایران است و به معنای تأیید اجرای عملیات زمینی نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/25532" target="_blank">📅 11:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش‌ها از آغاز درگیری سنگین میان نیروهای نظامی جمهوری اسلامی و افراد مسلح در ارتفاعات منطقه چاه‌احمد شهرستان تفتان، در محدوده کوه لوپ و ارزن‌تاک، از ساعت ۶ صبح امروز حکایت دارند. گفته می‌شود در این درگیری از سلاح‌های سبک، نیمه‌سنگین و سنگین استفاده شده و نیروهای کمکی نیز به منطقه اعزام شده‌اند. تاکنون جزئیات مستقلی درباره تلفات احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/25531" target="_blank">📅 11:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyeJxICS3YkJV4tb00-BLdwhVIV5R7FcuT9gqY7tW8KJuxvc4Krh0bHpTU1mVUJTmGj9MwdL1lstIHmM8ErAWejGD1G1y63scL38PNaocI6kexQOfGAr1X5HWNF6j-mDubn_TksT-NZRIQkdCjErW1SCyFgmKAlylZwhc6VAf_GkQOyd_8kN65gHiGzwKbDgzdxvBXLcsuEqsVw0ZaaqoZpV_aBJNLoilTauPkNyFtgyhc7kBwo7-sxf2iOVIk3uqTy3VKG6Te7xU2sqalvWyrBObrQkuq50xQdmofSxz0AOQzxcAvdio1xL14quN2HX_IA6SSoWLUB6p9hPQjH7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : می‌بینم چپ‌گرایان افراطی ادعا می‌کنند چین و روسیه به جمهوری اسلامی ایران کمک می‌کنند. اگر چنین کمکی وجود داشته باشد، بسیار محدود است؛ اما من اصلاً باور ندارم که آن‌ها به ایران کمک می‌کنند. چین و روسیه چیزهای زیادی برای از دست دادن دارند و اگر چنین کاری انجام دهند، ما خیلی سریع از آن مطلع خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/25530" target="_blank">📅 11:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4df0d1ee.mp4?token=e5mtgncAXfEdLqF5Sf8LT-AXBHKW9mYCrBRK1u7amB5e9yk8nha_sevKddLY4N7uxC-n6oCf_TNN0Yuf7-jTifsOBOgAPdeawnpg0zMIdBXNhH4wlQUQO_8pvFPehmgCBf1Pl19jSIzOA_M2o4M2JvUsd2nByoDxNyyE8aR4hq-usoPpuGFb-yh8niQscReE1bAGu3c3VajaHr2NKq-K-homkJBAlCWlseLFUSE-O5zBm2azzj2rBVO8rUgKGc3nrpOOIPcwimzYjfsWWN0ue0PuXFFXI-zxiQtBhm_ikAiIHGMEHTmgKzcZtCbCZYvrgrGlmfE_wx1BYwO-LOJ6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4df0d1ee.mp4?token=e5mtgncAXfEdLqF5Sf8LT-AXBHKW9mYCrBRK1u7amB5e9yk8nha_sevKddLY4N7uxC-n6oCf_TNN0Yuf7-jTifsOBOgAPdeawnpg0zMIdBXNhH4wlQUQO_8pvFPehmgCBf1Pl19jSIzOA_M2o4M2JvUsd2nByoDxNyyE8aR4hq-usoPpuGFb-yh8niQscReE1bAGu3c3VajaHr2NKq-K-homkJBAlCWlseLFUSE-O5zBm2azzj2rBVO8rUgKGc3nrpOOIPcwimzYjfsWWN0ue0PuXFFXI-zxiQtBhm_ikAiIHGMEHTmgKzcZtCbCZYvrgrGlmfE_wx1BYwO-LOJ6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوری اسلامی:
«شاید در برخورد با رهبران بیش از حد پیش رفته باشیم، چون دیگر نمی‌دانیم دقیقاً با چه کسانی طرف هستیم.
راستش را بخواهید، برایمان دشوار شده که بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیاده‌روی کردیم.
می‌توانستیم در سطح یک متوقف شویم. رفتن به سطح دو و دو و نیم احتمالاً زیاده‌روی بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/25529" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پس از دریافت تهدید ناشناس درباره وجود بمب در هواپیمای شرکت دلتا که از نیویورک در فرودگاه بن‌گوریون فرود آمد، مسافران به‌سرعت تخلیه و هواپیما به محل دورافتاده‌ای منتقل شد. نیروهای امنیتی هواپیما را بازرسی کردند؛ اما گزارشی از کشف بمب منتشر نشد و احتمال کاذب‌بودن تهدید مطرح شد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/25528" target="_blank">📅 11:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=ao7vZ3foHZRq-Bnd9J7T4We8jgydMmXZPULr9lv3-xQP1ljF8BhbAGUGVFuq_JfishpMKunyIbnJ2uUx97DWKsXO-pa0HsuyvT9nLUaRSLM1pjv3ul1yrvS99bvDPCGkGTbumviQxhwQ7T4g6l9KQMEN-zRJwW-SMq0uZEDXh674zdqC8IZsdDcj6kOmeWkFrYtini3yrWpn5zQskJMeIVzyx6QfoNotLGlktO7gYkVB_BqFPuouhfgv39wD8WYv25o3Bfk4gMYfIU442MF_6YoP81gkBbRodILicsUqUxkJ25p5bTffSIOxjE42Osipspo-2-Lz3yx60uADHFh2DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=ao7vZ3foHZRq-Bnd9J7T4We8jgydMmXZPULr9lv3-xQP1ljF8BhbAGUGVFuq_JfishpMKunyIbnJ2uUx97DWKsXO-pa0HsuyvT9nLUaRSLM1pjv3ul1yrvS99bvDPCGkGTbumviQxhwQ7T4g6l9KQMEN-zRJwW-SMq0uZEDXh674zdqC8IZsdDcj6kOmeWkFrYtini3yrWpn5zQskJMeIVzyx6QfoNotLGlktO7gYkVB_BqFPuouhfgv39wD8WYv25o3Bfk4gMYfIU442MF_6YoP81gkBbRodILicsUqUxkJ25p5bTffSIOxjE42Osipspo-2-Lz3yx60uADHFh2DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ام«گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، آنجا چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند ــ البته ساختمان چندان بلندی هم نیست ــ و از آنجا به پایین پرتتان می‌کنند. بااین‌حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
او در ادامه با لحنی کنایه‌آمیز پرسید: «زنان حامی فلسطین چه بلایی سرشان می‌آید؟»
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25526" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏شبکه دویچه‌وله آلمان بعد از ماه ها راستی آزمایی مستندی را از مصاحبه با برخی ماموران جدا شده از جمهوری اسلامی منتشر کرد.  مصاحبه‌شوندگان در این مستند تاکید کردند که جمهوری اسلامی برای نجات خود از سقوط، به هر ابزاری متوسل می‌شود.
@WarRoom
یاشار : فردا براتون قرار میدم</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25525" target="_blank">📅 03:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819b1a2d7e.mp4?token=GL1xOkNbqm16mAsjhtvkEylcKubQO4rjmbB4e3GXIX0cYXsE3EngO-_9ZKLqNqHkh2PFjGxEXpI_UnlF-rLL0vqmDFMpp0eaKaXK07ZjnfWVdeg4ph4l-WwYEuek74ezmECmGUNorRmxJLb3-RIOeYVB8yzXFV6zn-3Bm2J0NOVeKvEW4oIcKVUEYAAYXZPg6Z1IICiAa9FHl1wHp8_2Bt5gogFzmv-RFGR88Zu-UTwRnxUGORgsRgjeTndFnsdW8U0-2SIIvQQnXl1-r0UF3KKUt8cIIcE5YPxMEwGukirII3K9YOvNZQ5MqQnQ2GnJaTywZMm6EHsLiIa77YSSx5Y_--kJaNWt5QA0DALrZD_HJ4wHfYOjCryXI9Qs5QPAr4t8PnmVni8u8Y03vkxpZeZ7XAAfqI4E-1GVu9OTq2Fnkz2LaQ3Us-bdsE2aALX5cfFhxVWkks4_0VcbMzKxaStDotXtgs6zwcRuy55KaGex927nlsS42477c9oEzdl0ciJo2h6yJL0dQVuxcJvarWtIkovXy504kHC4-yZbVinkei3vSrlCS9QRkKG9L_Ub0n-9qXxpQE8n_rEATGG5o7d1dkgfNwPX3XEhCJd16utTGJXXKuH2K4oefI6NkrAuIphPVAIbWeqmcdr_FnzdrQ2TpTkkDSiBJacTEAMoJ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819b1a2d7e.mp4?token=GL1xOkNbqm16mAsjhtvkEylcKubQO4rjmbB4e3GXIX0cYXsE3EngO-_9ZKLqNqHkh2PFjGxEXpI_UnlF-rLL0vqmDFMpp0eaKaXK07ZjnfWVdeg4ph4l-WwYEuek74ezmECmGUNorRmxJLb3-RIOeYVB8yzXFV6zn-3Bm2J0NOVeKvEW4oIcKVUEYAAYXZPg6Z1IICiAa9FHl1wHp8_2Bt5gogFzmv-RFGR88Zu-UTwRnxUGORgsRgjeTndFnsdW8U0-2SIIvQQnXl1-r0UF3KKUt8cIIcE5YPxMEwGukirII3K9YOvNZQ5MqQnQ2GnJaTywZMm6EHsLiIa77YSSx5Y_--kJaNWt5QA0DALrZD_HJ4wHfYOjCryXI9Qs5QPAr4t8PnmVni8u8Y03vkxpZeZ7XAAfqI4E-1GVu9OTq2Fnkz2LaQ3Us-bdsE2aALX5cfFhxVWkks4_0VcbMzKxaStDotXtgs6zwcRuy55KaGex927nlsS42477c9oEzdl0ciJo2h6yJL0dQVuxcJvarWtIkovXy504kHC4-yZbVinkei3vSrlCS9QRkKG9L_Ub0n-9qXxpQE8n_rEATGG5o7d1dkgfNwPX3XEhCJd16utTGJXXKuH2K4oefI6NkrAuIphPVAIbWeqmcdr_FnzdrQ2TpTkkDSiBJacTEAMoJ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ تبلیغ سناتور اوهایو ، جان هاستد : «من خیلی به‌ندرت با مردها این کار را می‌کنم؛ شروع کردم به بررسی بدنش! از بالا تا پایین نگاهش کردم، به باسنش نگاه کردم، تمام بدنش را برانداز کردم و به دست‌هایش نگاه کردم؛ درست مثل چنگال! همان‌جا فهمیدم که تو یک ورزشکار فوق‌العاده‌ای! این را نمی‌دانستم؛ تبریک می‌گویم!»
@WarRoom
😂</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25524" target="_blank">📅 03:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFvwhykWy_Kbe3f9A-f55R87WLlzmiVoC5bTygYnb4ypIOkzFBlIOudrs_7vAK1DchAm2TaZP2k9ItojpOHHlKIOXLUvYcmhrVgSzhO2ctday6IA-qoenHz4UycwmggXpxfIevJRXft172Nhq5x3VQ48fKOkHaQ9dHIUFgciTE2UxLWtTMi5oNc72p1xvFUDVIc-hpQD0huaDcVevaVkrpC61zfcSLCCbo9blxPyonquL8E_STpBUA9c7V-VnsmtNsckwz0i0w9LJKaguBwrNHMg6n1SsJsI64fmjAPcKqCVJ2xfUmhwzM2UbUb8D_Ij4VbzDoAZLmElRvGBuvbCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون پرتاب آبگرمکن گازوئیلی از «حاجی آباد» هرمزگان به سمت تنگه.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25522" target="_blank">📅 01:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae1a1ab56.mp4?token=lVd2thilgztCDFNxD-g8VIGqR1d76bHzC0dyN4Dxh4kIoCFVl6QtpUeWAlp5t3Rv_VJSWZIlF6sr_sLoklGER2C7uiQ6mofcbe6QEj9RtXzAMUb3_INSMNgQC37TzlyF8r2T65J32jVWtnn5d0KvduX3tQhRnR8Ogor6govGSE9xQoRkyqFJBHGG9LFCtftCp4sSulIvl0bhS2VJ-gbehxdT3H_HMbXC5xu08Q59EKSp_cNGrYKLv8NuEVVmpPcAbDhouOSpA-f-1Sx6SmZJRzdt6Ec98NPzFm8Hh96aBdykEbgdLesnBKJlv0bucOW3tU3xjsbR-PGn1WQ0voUgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae1a1ab56.mp4?token=lVd2thilgztCDFNxD-g8VIGqR1d76bHzC0dyN4Dxh4kIoCFVl6QtpUeWAlp5t3Rv_VJSWZIlF6sr_sLoklGER2C7uiQ6mofcbe6QEj9RtXzAMUb3_INSMNgQC37TzlyF8r2T65J32jVWtnn5d0KvduX3tQhRnR8Ogor6govGSE9xQoRkyqFJBHGG9LFCtftCp4sSulIvl0bhS2VJ-gbehxdT3H_HMbXC5xu08Q59EKSp_cNGrYKLv8NuEVVmpPcAbDhouOSpA-f-1Sx6SmZJRzdt6Ec98NPzFm8Hh96aBdykEbgdLesnBKJlv0bucOW3tU3xjsbR-PGn1WQ0voUgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: قیمت‌ها در حال کاهش است و به‌محض پایان جنگ با ایران، که خیلی زود اتفاق خواهد افتاد، قیمت نفت به‌شدت سقوط خواهد کرد. این جنگ خیلی زود تمام می‌شود.
خبرنگار
: با توجه به اینکه متحدان ناتو، ایران را به بریتانیا مرتبط دانسته‌اند، آیا اقدامی علیه ایران انجام خواهد شد؟
دونالد ترامپ
: خواهیم دید ! اقدامات زیادی در پیش خواهد بود.
خبرنگار
: منظورتان چه اقداماتی علیه ایران است؟
دونالد ترامپ
: اقدام علیه‌شان ؟! آن‌ها نیروی دریایی ندارند، نیروی هوایی ندارند و نرخ تورمشان اکنون به ۳۰۱ درصد رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25521" target="_blank">📅 01:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دونالد ترامپ درباره انتخابات میان‌دوره‌ای آمریکا:
فکر می‌کنم گردهمایی‌های انتخاباتی تأثیر بسیار بزرگی داشته‌اند. هر بار که در یک گردهمایی شرکت می‌کنم، آمارها بهتر می‌شوند؛ حتی تأثیر آن‌ها فراتر از همان منطقه است. تمام این گردهمایی‌ها با استقبال گسترده روبه‌رو شده‌اند و هزاران نفر بیرون محل برگزاری می‌مانند، چون نمی‌توانند وارد شوند. به همین دلیل، نمایشگرهای بزرگ تلویزیونی در بیرون ساختمان‌ها نصب می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25520" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: روسیه و اوکراین می‌خواهند به توافقی برسند، اما نمی‌دانند چگونه این کار را انجام دهند.فقط این ماه ۳۲،۰۰۰ نفر کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25519" target="_blank">📅 00:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: با ولیعهد سعودی صحبت کردم و حوثی‌ها رفتارهای بسیار نامناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25518" target="_blank">📅 00:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرانسه نفتکش DF Peak را در اقیانوس هند، در جنوب جزیره رئونیون، توقیف کرد. شواهد نشان می‌دهد این نفتکش بخشی از
ناوگان سایه روسیه
است که برای انتقال نفت و فرآورده‌های نفتی و دور زدن تحریم‌های غرب فعالیت می‌کند. این کشتی با پرچم بنین حرکت می‌کرد و به استفاده از پرچم غیرقانونی و حمل‌ونقل غیرقانونی سوخت مظنون است. نفتکش در فهرست تحریم‌های اتحادیه اروپا قرار دارد. تاکنون ارتباط مستقیمی میان این کشتی و صادرات نفت ایران تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25517" target="_blank">📅 23:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هاآرتص: نتانیاهو در تلاش است با جلب موافقت عربستان، زمینه حملات گسترده اسرائیل برای نابودی حوثی‌های یمن را فراهم کند. به گزارش این روزنامه، محمد بن سلمان، ولیعهد عربستان، فعلاً با این اقدام مخالفت کرده و نگران پیامدهای سیاسی و واکنش افکار عمومی عربستان به مشارکت اسرائیل در جنگ یمن است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25516" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مسابقات دختر شایسته جهان عمدتاً در چهار رقابت شناخته‌شده با عنوان «Big Four» شامل Miss Universe، Miss World، Miss International و Miss Earth دسته‌بندی می‌شوند. در میان آن‌ها، میس یونیورس و میس ورلد از قدیمی‌ترین و شناخته‌شده‌ترین رقابت‌های بین‌المللی هستند. دونالد ترامپ از سال ۱۹۹۶ تا ۲۰۱۵ مالک سازمان میس یونیورس بود؛ ابتدا به‌صورت مشترک با شبکه NBC و سپس به‌طور کامل. او در سپتامبر ۲۰۱۵ این سازمان را فروخت و دیگر مالک آن نیست.
دیگر مسابقات صرفاً با تبلیغات، جذب اسپانسر یا پرداخت هزینه شرکت‌کنندگان تعیین می‌شود؛ مسابقات خارج از بیگ فور اعتبار منطقه‌ای یا تخصصی ندارند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25515" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری نظامی آمریکا همچنان با شدت ادامه دارد… از ۲۴ ساعت گذشته تا همین دقایقی پیش! ترامپ حرفه‌ای بارها تاکیید کرده که زمان به نفع او است !
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25514" target="_blank">📅 23:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hvt9JNP0r3ip4Z7QJ7-cmBlirLGQg_Hm-6khj_he7WUXUisP_6I0Ee-3ZDZabtgcspcCq9yH8X3z40H8J7dAdoxkpfOIADK9rX5oGvsLdEG5cVIybl9EHZcwI_3uEqSDD5g5GyyWUq9saujvg5I0nCv-2LcYPXHctA4tym-wAXLz9px0_yoiY6sefc6XbHm61qKMcKQO8Z-L8toLj43utWhJLp63DqKIbjrXA-GW4oShxqvijH7XBLhqP5pfna1Qo3OvdhItUg9fuxf7zbh_YvdZIpMJrQhGAtTFRZjP-0A8k6OC9ZV_PlCLLRW7QZRDX2Q8ukU7KAPIshmYYcTxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuElW2dBzTjgylQaCg5b_WSBNWKu0eV_BACrn0LHudZWuBgzAC2Gaj3_43ddOt2NRZqLr7NaV0hpI40TKs_2eJ9y3QLA26e_Xklm83vLRWSzgkvDwVyVGrNhUhyiZ2X-AQmjsuub66Xt1C5jIgVmQXeCLFp9uTrUiO9LxgqXsEJjzN-9MYce2yJ2T70JDLnxG1vMdB3TO9eIBc2oR1r9LKK1eeQ41kTv7f6tMBqC7HkjguXnVWNUNj3BQWY97I_KH1s5n2C3MKSJ8XjhON4zL4e6QVXEMogGT5poMJkUhv1MaJJDGQbtB3cWEgTWlLcy151AAxL6vj7plpx5-yun9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srv-y-OOFPFB9znUbe8c3HHRQLhHLFa7TzRFo_1DOrHTSU0Ctvo2cNhz8Isb66fUuIGRRjKC2McoatbX7jApshT57yZUi050WPMpLizvTHXVL4nUfRuQWPaGWYMW6BKaewvcpj168DGEaAmSuB3q7dyqb2yKypHd8Z0nMI_97hnszo-DVJCD7GqdQHv5djYzEmMWMrTYgfHXu3am_OXiOOsRA8aBlqdcOSdKWfvno2XcgptwuzZ8U7wSWGXUqADAO-oIIGR862clHeS24hkpqomrlIeM-EWuJrbj1AsDKk_FxGAitPazMWupV_OW6O5SfSehnZ9KeM2_9Zqwo1SKjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا در سومین گزارش پی در پی اعلام کرد یک نفتکش حامل نفت خام هنگام خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25511" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">العربیه: نیرو های امنیتی بخاطر حمله حوثی ها، بازی را متوقف کردند و سریعا رونالدو رو نیز از ورزشگاه خارج و به یک جای امن منتقل کردن
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25510" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGC2FceUyyuD1qGPz9FZFpeCSPD7e94Ks4Jmb1O57tLdLvWbQeG4GcBpj7Y3vF7KmIQil3L4wIY8eTWCxriS5azJlRcyV4Wsh50GaokSu7x0wUNfvViJrE9QVRMCwtHsBNeaevvsBcUvkJbNvRP-tuhQChwTJLJV9eSIO0RvBucUwY0cKqHeWIcUohh9TdMA19tGD4nWRS-BvKMs3xi1a7Rox0SjhEOr42P2WFDoBs5oz0COrqgIksk8tkXD67EKEXXABpFCZ9Kd1530fMx-ugLU7FrCtdDIU3N-LWfPb6hHW8pJZJ0SfDLE7ibMAktxklD_RGfsD1abh0kyDmU7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی کانال ۱۲ : ایزنکوت حذب یاشار فاصله خود را با نتانیاهو حذب لیکود افزایش داد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25509" target="_blank">📅 22:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی با تأخیر از وقوع حادثه‌ای در داخل تنگه هرمز دریافت شده است. بر اساس گزارش یک منبع تأییدشده، یک نفتکش حامل فرآورده‌های نفتی هنگام عبور از تنگه هرمز به سمت خروجی، با پرتابه‌ای ناشناس هدف قرار گرفته است. مقام‌های مسئول در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25508" target="_blank">📅 21:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی با تأخیر زمانی از یک منبع تأییدشده دریافت شده که بر اساس آن، یک کشتی کانتینری هنگام ورود از تنگه هرمز با پرتابه‌ای ناشناس هدف قرار گرفته است. مقام‌های مسئول در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25507" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc43053e1a.mp4?token=UMholK09ywCO-PeoT_qh5VyAJPL-EWA4dqgupm0qMc1-WiONjee6wSq4n1vR3mQu2_k-QmeeYY6O6in1MLehfJjndEkZyO4uHR94JJkaQPEgfjKAh6eY9uENg2p96EvNoHlgeeDLT_UTCrFUD3K9XHht0nfZvZ3lmDeOipBFIEBHL9pfEn9uOBMD6K-n4msxtvQ_O9gJu3nvYn6KwHqB-pzUeE-qk4cpt-DQAXfw897-PHhU_sGAUiq2YukrS_PQFq0t7hly4A0P4-eAr7tuJ5-rslGzD2dmF8CnJT5Q-ONkzZ0SJfYe7oTbovXSAUsQQGsELYCnm1KB_xbmRs-msQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc43053e1a.mp4?token=UMholK09ywCO-PeoT_qh5VyAJPL-EWA4dqgupm0qMc1-WiONjee6wSq4n1vR3mQu2_k-QmeeYY6O6in1MLehfJjndEkZyO4uHR94JJkaQPEgfjKAh6eY9uENg2p96EvNoHlgeeDLT_UTCrFUD3K9XHht0nfZvZ3lmDeOipBFIEBHL9pfEn9uOBMD6K-n4msxtvQ_O9gJu3nvYn6KwHqB-pzUeE-qk4cpt-DQAXfw897-PHhU_sGAUiq2YukrS_PQFq0t7hly4A0P4-eAr7tuJ5-rslGzD2dmF8CnJT5Q-ONkzZ0SJfYe7oTbovXSAUsQQGsELYCnm1KB_xbmRs-msQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیست دانش‌آموز کوهنورد بر اثر انفجار یک مهمات عمل‌نکرده در نزدیکی مرز شمالی اسرائیل مجروح شدند. به گفته سازمان «مگن دیوید آدوم»، یک کشته و حال دو نفر دیگر نیز وخیم گزارش شده است. پدر یکی از کودکان مجروح چنین روایت کرد: «این گروه کوهنوردی مربوط به دانش‌آموزان…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25506" target="_blank">📅 21:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صداوسیما لحظاتی از شلیک موشک‌های کروز در تنگه هرمز تا عملیات مین‌ریزی را منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25505" target="_blank">📅 21:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رویترز: ۶۰ کشور در بیانیه‌ای مشترک بر آزادی کشتیرانی در تنگه هرمز تأکید کردند و با وضع عوارض عبور کشتی‌ها، دریافت هزینه‌های غیرقانونی و الزام به اخذ مجوز قبلی برای عبور مخالفت کردند. بریتانیا، ژاپن، استرالیا و کشورهای اتحادیه اروپا از حامیان این بیانیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25504" target="_blank">📅 21:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جت‌های جنگنده اسرائیل بر فراز چندین شهر و منطقه در لبنان، از جمله صیدا، منطقه بقاع، کوه لبنان و شمال این کشور، پرواز کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25503" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند
آلن ایر، عضو سابق تیم مذاکره کننده آمریکا نوشت: ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند. احتمال انجام دور دیگری از حملات آمریکا علیه ایران بسیار زیاد است‌. با انتقال تجهیزات و نیروهای نظامی بیشتر آمریکا به منطقه و انتشار گزارش‌هایی درباره فعالیت هواپیماهای اسرائیلی در نزدیکی حریم هوایی عراق، این احتمال وجود دارد که  واشنگتن عمداً در حال آزمودن آستانه تحمل تهران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25502" target="_blank">📅 20:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25501">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امانی ، سفیر پیشین رژیم در لبنان : قرار بود پیجرها بررسی شود و برای همین عملیات را زودتر اجرا کردند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25501" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYYKh0ZeUwG65re8YSEkBq_PUaM7fUU0m0DlzecCkCV9XTJvs9ph14Jcps_BE5j2LxGl3ewBP0X74hHE9sPMkGCft15oHkMUd9EiPD_n9ZfEbL1TbpFVoL0hQ8gmxaLCqFLaUOe3lc6NAkOkHAuYUPMj0BD2jn2AeRCfwZnQ-gcbIxWkLRkKhJ9Gr5vgxdUOpGrPcj5zaFfuYXvqZ8VXP1LD1fUBS6VsYnHQP8t7s142CI--UgvSuGT5vuMep-F4O0q3vwCDP8h639wbZtbW-MC3o-oI1oWxWvvEKQ82hpPcEvGsK7-hJUxpz1gdDYwUW0EhXOUYzZNttIugGmg71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث، وضعیت ۱۵۹ کشتی نیروی دریایی جمهوری اسلامی. در زمان ترامپ : کف دریا در زمان دیگر رئیس‌جمهورها: روی آب.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25500" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بریتانیا، روح‌الله بازقندی (رئیس پیشین اداره ضدجاسوسی سازمان اطلاعات سپاه پاسداران) و شهرام علیرضا تمرزاده جکی را به دلیل اتهامات مربوط به مشارکت در فعالیت‌های اطلاعاتی سپاه پاسداران انقلاب اسلامی و توطئه‌هایی که افراد یا دارایی‌ها در بریتانیا و سایر کشورها را هدف قرار داده‌اند، تحریم کرد.
‌اندی برنهام در سخنرانی خود در مجلس عوام بریتانیا راسمأ اعلام کرد ارزیابی‌ها نشان می‌دهد که حمله به پایگاه هوایی فیرفورد به در ایران هماهنگ شده و هدایت آن به طور قطع توسط سپاه صورت گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25499" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیانیه ۲۹ کشور از جمله انگلیس و آمریکا: ما یافته‌ های بریتانیا را درباره دست داشتن ایران در حادثه پایگاه فیرفورد تأیید می‌کنیم. حملات ایران، حملات سایبری و فعالیت‌ های ترکیبی آن را محکوم می‌کنیم. واقعه فیرفورد آمادگی سپاه پاسداران را برای انجام حملات فرامرزی نشان می‌دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25498" target="_blank">📅 19:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر امور خارجه بریتانیا: ما دو شهروند ایرانی را در فهرست تحریم‌ها قرار دادیم، زیرا آن‌ها در فعالیت‌های خصمانه به نمایندگی از رژیم [ایران] نقش داشته‌اند.تلاش‌های ایران برای تضعیف امنیت بریتانیا و متحدانش از طریق شبکه‌های جنایی و گروه‌های خود، غیرقابل قبول است. ما با هیچ تهدیدی علیه خاک خود مدارا نخواهیم کرد و سفیر ایران را احضار کردیم تا این پیام را به او منتقل کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25497" target="_blank">📅 18:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آسوشیتدپرس: رسانه‌های وابسته به حوثی‌ها مدعی شدند حملات هوایی به دو منطقه در صنعا، پایتخت یمن، یک کشته و ۱۲ زخمی بر جا گذاشته است؛ از جمله در یک کارخانه نمک و یک منطقه مسکونی. حوثی‌ها عربستان را مسئول این حملات معرفی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25496" target="_blank">📅 18:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره حادثه امنیتی در مرز لبنان :
«در غم سنگین خانواده پسری که در جریان یک گردش در نزدیکی مرز شمالی، بر اثر انفجار جان خود را از دست داد، شریک هستم و برای همه مجروحان آرزوی بهبودی سریع و کامل دارم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25495" target="_blank">📅 18:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تتر و دلار ۲۶۱،۰۰۰ تومان
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25494" target="_blank">📅 18:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=ltYC9xwuCi0RDLgbDwZDbel7g1mBdk9tdm3CJs5erd4daeVvzD7trQO0DbBDcTm99VhHjyxxBnk0y6DFXtcis5ySoGJdPkSu3Sl4NRelZoVIEnMZ32M6yL1L8IianNmnykGiOKuZK-RxPIE1KtX9uSG3aeiaYoOJzEgbLBNygIlcXD_Otj0wNnXvyBf6WpUsaMdBQoYERimVar646ooJvX56Ha6KQp91_HpMTeDD_i2N1zW2THbCZoVoUmYCBlbLeZa0J_-gUKSQxWvXfJxVLX5fSfQtlP-EOxAjVgNiyXjSfZZAM1yuFqmhxCEbqHcOpNISmLIIeLKL6iGtjY076g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=ltYC9xwuCi0RDLgbDwZDbel7g1mBdk9tdm3CJs5erd4daeVvzD7trQO0DbBDcTm99VhHjyxxBnk0y6DFXtcis5ySoGJdPkSu3Sl4NRelZoVIEnMZ32M6yL1L8IianNmnykGiOKuZK-RxPIE1KtX9uSG3aeiaYoOJzEgbLBNygIlcXD_Otj0wNnXvyBf6WpUsaMdBQoYERimVar646ooJvX56Ha6KQp91_HpMTeDD_i2N1zW2THbCZoVoUmYCBlbLeZa0J_-gUKSQxWvXfJxVLX5fSfQtlP-EOxAjVgNiyXjSfZZAM1yuFqmhxCEbqHcOpNISmLIIeLKL6iGtjY076g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی تروریستی سپاه اعلام کرد طی دو روز گذشته، سومین نفتکش بزرگ را در تنگه هرمز هدف قرار داده که در پی آن، کشتی دچار آتش‌سوزی شده است.، این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه هرمز، سامانه ناوبری خود را خاموش کرده و با وجود چندین بار هشدار، به مسیرش ادامه داده است
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25493" target="_blank">📅 17:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چندین پرتاب موشک بالستیک از شهر های : یزد، اصفهان و کرمانشاه گزارش شده است. به نظر میرسد تمرینی و برای بازدارندکی و رخ نمایی توان باشد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25492" target="_blank">📅 17:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25491">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=tkkzkxywEeLqDdK1YbJ4efStmZF3n8KrDnCaxjUqHps6BdvWbUS7pFowQ_t0EbE-wf9Wr501Vaf5jfjMIlq_ZdoQo-WGvpEilRqUjLfKP5m1Tg51KYkjHzEo_98x-y4Uv18u5OcjeQwf4Hkt7koAjsDlEom6u1x6PpPhjJHoxPec-g0ojOdA9fhzQssWhR8Caii2hmIWG3rQ7n3SsD-pQei2vGHJI8xiFi2AAl-viRvNmCivNXgC8hZVmyN0bp8c38UsQ7chBZR58NygsCvmp-8y7-FhQcdjnlJzRucL9_dWq4-lrzVaDZXe0WB_V1O67sPp4DXaIg-EPMeKbsTMlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=tkkzkxywEeLqDdK1YbJ4efStmZF3n8KrDnCaxjUqHps6BdvWbUS7pFowQ_t0EbE-wf9Wr501Vaf5jfjMIlq_ZdoQo-WGvpEilRqUjLfKP5m1Tg51KYkjHzEo_98x-y4Uv18u5OcjeQwf4Hkt7koAjsDlEom6u1x6PpPhjJHoxPec-g0ojOdA9fhzQssWhR8Caii2hmIWG3rQ7n3SsD-pQei2vGHJI8xiFi2AAl-viRvNmCivNXgC8hZVmyN0bp8c38UsQ7chBZR58NygsCvmp-8y7-FhQcdjnlJzRucL9_dWq4-lrzVaDZXe0WB_V1O67sPp4DXaIg-EPMeKbsTMlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک جانسون: همه منتظر نتیجه انتخابات آمریکا هستند
حاکمان ایرانی‌ها این دوره انتخاباتی را زیر نظر دارند و می‌خواهند به رئیس‌جمهور و چهره سیاسی او آسیب بزنند و فکر می‌کنم این موضوع عامل مهمی در ماجراست.
پس از انتخابات، فکر می‌کنم وارد مرحله‌ای کاملاً متفاوت خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25491" target="_blank">📅 17:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ایران برای دست‌یابی به سلاح هسته‌ای تلاش می‌کند، اما ما رژیم حاکم بر ایران را سرنگون خواهیم کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25490" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیست دانش‌آموز کوهنورد بر اثر انفجار یک مهمات عمل‌نکرده در نزدیکی مرز شمالی اسرائیل مجروح شدند. به گفته سازمان «مگن دیوید آدوم»، یک کشته و حال دو نفر دیگر نیز وخیم گزارش شده است. پدر یکی از کودکان مجروح چنین روایت کرد: «این گروه کوهنوردی مربوط به دانش‌آموزان مقطع راهنمایی بود و بچه‌ها آسیب دیدند. لطفاً برایشان دعا کنید؛ این مهم‌ترین مسئله است. این اردو برنامه‌ریزی و تأیید شده بود و همه هماهنگی‌ها انجام گرفته بود؛ تمام والدین فرم‌های مربوطه را امضا کرده بودند. متأسفانه مهمات عمل‌نکرده‌ای در منطقه وجود دارد و به نظر می‌رسد فردی به‌طور تصادفی با یکی از آن‌ها تماس پیدا کرده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25489" target="_blank">📅 16:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حیوانات باغ‌وحش دزفول دزدیده شدند ,
فرمانده انتظامی دزفول از دستگیری چهار سارق و دو مالخر در کمتر از ۴۸ ساعت خبر داد.
این افراد چند رأس بز کوهی کمیاب را از باغ‌وحش دز سرقت کرده بودند.
در بازرسی از مخفیگاه متهمان، ۶ رأس بز کوهی کشف شد که یکی از آن‌ها سلاخی شده بود. پنج رأس بز کوهی نیز به باغ‌وحش بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25488" target="_blank">📅 16:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DekF6cuGoWDrrMMeG7B3Cemq8cG3lY2WVAS_t7xzBOCEn7LA813TUeOnA4LFo4b3p_QoWQe4fZB2ybq44ZD2Qt6cfxkNoj0TRoKB2XZM9fSogxLhrU4mQ811bSb_wXMS-aMbuOsKVgBupl8iohAoba6FqvV2udBHrNSKjLIV7tnBPuOZb2fI0w-qqaQ7KXxh4SIJ5I8WkFJEK2qbzNsPVMuDo_H7LC9vTq-AhTkMmUft7UBN7OJ4w_jO-dRu4Fy5jVyu0_QZ0QYwEVW5rwXQBtnyWbRsXG0YtAwW0dpq3B4COEPqDMlOoQDuJ1JX1lRzUP4oC0Wm-P2ItpfRd2gRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ چینی نشان می‌دهند که ناو آبی‌ـ‌خاکی
یواس‌اس میکین آیلند (LHD-8)
در کنار یک ناو ترابری آبی‌ـ‌خاکی از کلاس سن‌آنتونیو، در پایگاه مشترک پرل هاربر–هیکم در هاوایی پهلو گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25486" target="_blank">📅 15:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHDTc3KPgywOx6ze7NtP1DaGQgK_Xfv3ZCMRDBFYpSR9heOCc7sq6OqEKx1ScTmossZVnSLkC_Co2njwoO1kdPe6_4BwH03VxugMgUDDNtHSdtRhqPo1fobIrEtlJsgD5Ap_mxF0knqSBbKJd38F7JpJJa4Wn5SZfh4eIxt3p1lQC9SqIZu1V8R6qKKTESYn3apPC2DB_Uh-xp2ASYwrxtlLrTgsiEh0J4rc3A431saVB9Uux-dfa3eP-q0bhwzCF25QcK_jeW8UEes4-vsU0oXYkJqzjoAj0KORrgd3Bn-A_2WykIUKh-CURAMdR22A-OHaO8t4bQ30Dbt3FLYhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ فروند پی۸ پوسایدون در حال حرکت و انجام مأموریت در ابتدای دریای عمان نشانه‌ای از جابه‌جایی یا تغییر موقعیت یکی از دو گروه نظامی:
گروه آبی ـ خاکی آبی‌خاکی (ARG) یا گروه ضربت ناو هواپیمابر (CSG)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25485" target="_blank">📅 15:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi9yxpwlYgEzaRAxLZ2MTzqSg9BUJeeVMNxu8zsYkwn3tenPOfRzMWn91YgbSSymYnhR2Z_jkLU1995AkUb5bwLk6eMK3hKi4XZN56PU7ktFcqX6_D2YkYFnKR927ZXcVWsdms1fWXIBMO3Chla2V9YHvBQlB2rgjvT1FzKtOR3WFW7nxX6_b5z4TjRRulPp3Zo6jVkbiTC89Uuu6WSvqRvPjJn-ztRn0kOEmMPQ69deVNDJCB8yoKuP0OHYy6BngV8zlT0IMPfoHtk7XGnr7IrBHAqTCcYKDNEzuPb8jVAinWAdth_KF0ZTuREutH2H4Te4tN_6VkQjf8NqQcfSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از مهرداد اخلاقی کتابچی، وزیر پیشنهادی دفاع و پشتیبانی نیروهای مسلح
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25484" target="_blank">📅 15:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری معاریو: برآورد نهادهای امنیتی نشون میده اگر ایران [به اسرائیل] حمله نکنه رویارویی به بعد از انتخابات موکول خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25483" target="_blank">📅 14:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏رابرت ای. هال، استاد دانشگاه استنفورد و مایکل وودفورد، استاد دانشگاه کلمبیا، برنده جایزه نوبل اقتصاد سال ۲۰۲۶ شدند. این دو نفر در تحقیقات خود نشان داده‌اند که برای درک تحولات اقتصاد کلان، نمی‌توان تنها به شاخص‌هایی مانند تورم، تولید و مصرف تکیه کرد، بلکه باید رفتار و تصمیم‌گیری خانوارها و بنگاه‌های اقتصادی را نیز در نظر گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25481" target="_blank">📅 14:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏سخنگوی کرملین گفت که اگر اوکراین واقعا خواهان برگزاری انتخابات باشد، روسیه در روز انتخابات هیچ حمله‌ای به اوکراین انجام نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25480" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۳ اسرائیل : نتانیاهو شب گذشته در نشستی اضطراری با مقام‌های ارشد امنیتی ،حمله نظامی به ایران را بررسی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25479" target="_blank">📅 14:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایفدانا، رسانه رسمی سازمان غذا و دارو: مهدی پیرصالحی، رئیس سازمان غذا و دارو، اعلام کرد مشکل انتقال دارو از هند به ایران ناشی از محدودیت‌های حمل‌ونقل در شرایط جنگی بوده است. به گفته او، به پروازهای ایرانی در برخی مسیرها اجازه پرواز داده نمی‌شد و اختلال در مسیرهای دریایی نیز انتقال محموله‌ها را دشوار کرده بود. او تأکید کرد که هند در زمینه تأمین و فروش دارو همکاری مناسبی با ایران داشته است؛ بنابراین، نسبت دادن مشکل صرفاً به مخالفت هند با ارسال دارو، با توضیحات رسمی سازمان غذا و دارو مطابقت ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25478" target="_blank">📅 13:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7BE5Ns0A7weJfKXKcaiSNb9sRvYce2ovdu5C4REWIj-nQ87YwyUaNquEYADB3xr6c4TKvB8G5UUjylTvluB5NTtYVDEl4Yq1khpPxuUO4z4XW7M-_zbbhRp9Yiu9ZN1RxTEozpDBSxumvgVTBf7RQCIdocN5dNWW6faBWpLkyEyGOvZbV9UoBKOZ97rE-7cNLSid8b9SHMjFZkLhPMBDaf7j-IKr6-X9nNhoZFXxt2j6Y7BqZVmPlw4TQFN97rCoZeT3x1duiJEFDUeU5I4aGOLu1n2_xM_c3ZjqxHFClT1LFVEgDaPuQA9azKud-aS_3PVOiFCciSuL7MahKJniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تصویر ماهواره‌ای نمایی از تأسیسات موشکی قم را با حدود ۵۰۰ زاغه ذخیره‌سازی مهمات نشان می‌دهد.
این سازه‌های برآمده پناهگاه‌های ضدبمب بتنی موسوم به «ایگلو» هستند. هر واحد بتنی زیر تلی از خاک بومی پوشانده شده است. دهانه‌های مستطیلی خاکستری در تصویر، ورودی کامیون‌ها و تجهیزات لجستیکی هستند.فواصل منظم این سازه‌ها مانع از انفجار زنجیره‌ای بر اثر حمله می‌شود . پوشش ضخیم خاکی تخریب ناشی از ترکش و ضربات هوایی را به حداقل می‌رساند . این انبارها محل ذخیره کلاهک‌ها، سوخت جامد و راکت‌ها هستند. تمام این زاغه‌ها از طریق شبکه جاده‌ای اختصاصی به شهرهای موشکی زیرزمینی کوهستان متصل می‌شوند.
لوکیشن ها :
‏34.893496,50.788559
‏34.906500,50.793314
‏34.900907,50.811569
‏34.921643,50.801991
‏34.931112,50.749336
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25477" target="_blank">📅 12:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فایننس‌فیدز : قیمت بیت‌کوین در معاملات امروز تا این لحظه حدود ۸۳٬۷۷۰ دلار بود و در ۲۴ ساعت گذشته حدود ۰٫۷۳ درصد رشد داشت. صندوق‌های اسپات بیت‌کوین آمریکا در جمعه ۹ اکتبر ۲۱٫۱ میلیون دلار ورود خالص سرمایه ثبت کردند؛ این رقم پس از خروج ۲۴۴٫۱ میلیون دلاری روز پنجشنبه به دست آمد. بااین‌حال، در کل هفته ۵ تا ۹ اکتبر، صندوق‌های بیت‌کوین حدود ۶۷۸٫۹ میلیون دلار خروج خالص سرمایه داشتند. بنابراین، ورود سرمایه روز جمعه هنوز برای تأیید بازگشت تقاضای نهادی کافی نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25476" target="_blank">📅 12:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است. پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25475" target="_blank">📅 12:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لحظه ‎صادر کردن دستور یک حمله تلافی‌جویانه قاطع علیه حوثی‌ها توسط محمد بن سلمان، ولیعهد عربستان سعودی @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25474" target="_blank">📅 12:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این آقا امروز به‌خاطر جوابی که در مناظره‌اش با نامزد دموکراتها داد ستاره شده. یعنی حتی حریفش
سناتور کوری بوکر (دموکرات)
هم چنانکه در آخر این کلیپ می‌بینید مات و مبهوت ماند و میگوید «واو»
مجری مناظره : اگر رئیس‌جمهور با شما تماس بگیرد و بگوید: «هر کاری بخواهی برایت انجام می‌دهم؛ در مورد ایران چه کار کنم؟» پاسخ شما چیست؟
جاستین مورفی، نامزد جمهوری‌خواه مجلس سنای آمریکا از نیوجرسی
: کار را تمام کنید. این جنگ را به شکلی مثبت به پایان برسانید. نمی‌توانیم تا نیمه راه پیش برویم و بعد تصمیم بگیریم که دیگر نمی‌خواهیم این کار را ادامه دهیم.سپاه پاسداران سازمانی تروریستی و افراطی است که مردم ایران را از تاریخ و زندگی شایسته محروم کرده و با قتل، تجاوز، شکنجه، ترور و حمایت از تروریسم، به‌ویژه در خاورمیانه، به مردم منطقه و جهان آسیب رسانده است. من در کودکی شاهد حمله تروریست‌های اسلام‌گرای افراطی به سفارت آمریکا در نوامبر ۱۹۷۹ و گروگان‌گیری ۵۲ آمریکایی به مدت ۴۴۴ روز بودم. از آن زمان، سپاه جز صدور تروریسم، خشونت و سرکوب کاری نکرده است. چهار دهه کافی است؛ مردم ایران به‌اندازه کافی رنج کشیده‌اند و وقت آن رسیده که این وضعیت پایان یابد.
و من به آقای رئیس‌جمهور می‌گویم:
کلاه کابویی‌تان را بر سر بگذارید، وارد میدان شوید، یه درِکونی حسابی به آنها بزنید و این کار را تمام کنید؛ آن هم به‌درستی!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25473" target="_blank">📅 11:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVD_fRPfzjXIhyP3PKCMOMTr9a5CoRpPBLs9gpuWEdx6o6ncPvRPiWLR8hDZhpEgWKhC__EAyMZWAJrlAxCpXgiXhLLCWbyEBQ_qWj4vdjKEz6vlQavn35QwUQCTPN7OAZ3PLfQGfOvaORra8UoAZui5rfc2cYxSf4gjhiVJ6NWGzGYyWUAFlAo5H6uZX4ptJAB5Vls74GPlDfO23h5MjXHutXJo5mdc0OVZnyKdV7pegWOe79BCEgY5JmXJ8ao-rEdpvA8JTdWOfgVr30LygJcSgfZ47RTGM9yBRiBLk7S-12NM4gBdIFoLAigJJaOcXZ5Q66unKnFe6AHCM1YLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگر تحرکات هواپیماهای عملیات ویژه آمریکا: خبر بد برای جمهوری اسلامی؛ ادعا شده چند فروند هواپیمای عملیات ویژه MC-130J Commando II آمریکا، معروف به «شوالیه‌های خاموش»، صبح امروز در فرودگاهی مشاهده شده‌اند. نیروی هوایی آمریکا تنها ۱۰ فروند از این هواپیماها را در اختیار دارد. این هواپیماها قرار بود در آوریل ۲۰۲۶ در مأموریتی محرمانه برای بازیابی و انتقال محموله اورانیوم غنی‌شده ایران، با نفوذ به عمق خاک ایران و فرود در شهرهای شهرضا و کوشک نصرت، مشارکت کنند. این هواپیماها به رادار پیشرفته پرواز در ارتفاع پایین مجهز هستند و احتمال داده شده است که به‌زودی در نزدیکی ایران مستقر شوند؛ با این حال، وی تأکید کرد که محل فعلی این هواپیماها و مقصدشان را فاش نخواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25472" target="_blank">📅 10:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل، در کنفرانس «مردم کشور» که به میزبانی «وای‌نت» (Ynet) و روزنامه «یدیعوت آحارونوت» برگزار شد، اظهار داشت که اگر انتخابات به نتیجه‌ای قاطع منجر نشود، «تمام تلاش خود را برای جلوگیری از تکرار انتخابات به کار خواهم بست. باید بدانیم که چالش‌های ملی ما بسیار عظیم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25471" target="_blank">📅 10:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روزنامه ژاپنی «آساهی شیمبون» گزارش داد: ناو هواپیمابر هسته‌ای که قرار است از «یوکوسوکا» در ژاپن بازدید کند، ناو «یو‌اس‌اس تئودور روزولت» (CVN-71) و گروه ضربت همراه آن است.
این ناو احتمالاً طی ۵ تا ۶ روز آینده، یعنی در بازه زمانی ۱۵ تا ۲۰ اکتبر، وارد منطقه خواهد شد.
پیش‌تر در مطلبی که در ادامه آمده است، تاریخ ورود این ناو بین ۱۰ تا ۱۴ اکتبر اعلام شده بود؛ اما اکنون به دلیل شرایط نامساعد جوی ناشی از طوفان‌های «نولو» (Nolo) و «کوگوما» (Koguma)، ورود آن با تأخیر مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25470" target="_blank">📅 09:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=hfSD2nRNZaonSGRYKtqVAKiSX7jhBiIIjFiOybVDh2YYPqPHe2C6FsHDFJclzN0JBuQprw-rfiWop1mJ5csCuH50OhFhEIowAwAecUz6GDNtOLjR3rRXgxnL_pqP0LJpAA7thcUCo3htfJ4HZUdBusKd3mcFeFQhP7zUqyKnyjX4NfbLEih6XkRiA-I2QTvmnb7Bq5xij-Kjj2M25wt20gUEaIx1gmWnEMOGMrrnrdYGp7S8BkkrWIBq6m9Zl1_oU79F0M8M20_b3zcOdQQfcjWiSwQSlMQTaQXJpNqjeOr0WTGPGUtY-52fPFfm-aiVyPugqdbaMAYk1ld7UqkKkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=hfSD2nRNZaonSGRYKtqVAKiSX7jhBiIIjFiOybVDh2YYPqPHe2C6FsHDFJclzN0JBuQprw-rfiWop1mJ5csCuH50OhFhEIowAwAecUz6GDNtOLjR3rRXgxnL_pqP0LJpAA7thcUCo3htfJ4HZUdBusKd3mcFeFQhP7zUqyKnyjX4NfbLEih6XkRiA-I2QTvmnb7Bq5xij-Kjj2M25wt20gUEaIx1gmWnEMOGMrrnrdYGp7S8BkkrWIBq6m9Zl1_oU79F0M8M20_b3zcOdQQfcjWiSwQSlMQTaQXJpNqjeOr0WTGPGUtY-52fPFfm-aiVyPugqdbaMAYk1ld7UqkKkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25469" target="_blank">📅 09:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=SNLjfbduXmXKIUxlvZBMutE3xcGYPIkb7r8Rnv2oCStUH20yHayhmCCf39SihZ_R_fJTbtKDD1qHyizg_qUpbwJQIQ9m69mA9w3ktDHQ6UBThd2M4sZ1fHRMnc5X_yn68-R7lm_0RZjvg-_kAqHk61y_9eDvFNtCvU4H8o72TEt8sv1O2p1K0n4sAD2-kFo226CmxieWsMaiEiKSJX4-d3aQPkndGL0_kyJed0Zspp8xHNu0HOyha2jeDSxTz_HIVBKxD6gQTs6n7O27ewVMdpAAz2fup_ZqReC2CQwWNBrR1WYq2PNmKlRoAK1lEqrbSsjJz7F9Y2SDHkk9c7hRIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=SNLjfbduXmXKIUxlvZBMutE3xcGYPIkb7r8Rnv2oCStUH20yHayhmCCf39SihZ_R_fJTbtKDD1qHyizg_qUpbwJQIQ9m69mA9w3ktDHQ6UBThd2M4sZ1fHRMnc5X_yn68-R7lm_0RZjvg-_kAqHk61y_9eDvFNtCvU4H8o72TEt8sv1O2p1K0n4sAD2-kFo226CmxieWsMaiEiKSJX4-d3aQPkndGL0_kyJed0Zspp8xHNu0HOyha2jeDSxTz_HIVBKxD6gQTs6n7O27ewVMdpAAz2fup_ZqReC2CQwWNBrR1WYq2PNmKlRoAK1lEqrbSsjJz7F9Y2SDHkk9c7hRIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمای‌ نزدیک از‌ نفتکشی که در اطراف تنگه هرمز با مین دریایی برخورد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25468" target="_blank">📅 09:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25467" target="_blank">📅 09:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKY0fUsxWH_Mp6r6PHeKReKTdWtzejsJ_whFwtfn2qDkXzNxXlES0z_pb4agvzwDAocHyXlNpzjXCUY0DbU3e3yxtksj19cOvySnFObbR2xau358enEKaz3eBsZiEBBmaYs79msaLEbTAacv9wh2dii-pr2cRLArVwZ7j7f0Fv16eIGaqQIzCcCQYzXAkOXGignLQWlfbyhZY3a-8LQU0FLlFU25MfNRzvO5UVdWrpm9Ot3fH4BAJtamkjaTC2kko2RHXg7BDsjDmYACnX6JEu5n6-28KxuviuGid2_yVng-1CmPZN7FWGDRdASX7e6t2uZBh0nCnNqJcl1YhOnk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا راهنمای شناسایی تصویری (تهدید را بشناس) را برای کمک به سربازان آمریکایی در شناسایی نیروهای ارتش ایران ، منتشر کرده است. این راهنما شامل تصاویر یونیفرم‌ها، علائم درجه و تجهیزات نظامی ایران، از جمله سلاح‌های کلاشینکف، تفنگ مصاف ۲ و نارنجک‌انداز آرپی‌جی ۷ و… است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25466" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شبکه ۱۳ : ترامپ و نتانیاهو طی هفته‌های اخیر، در پی گزارش‌ها درباره بازسازی کارخانه‌های موشکی و پهپادی در ایران ، گفت‌وگوهای فوری داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25465" target="_blank">📅 04:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVCtNe-7om6lAaHyIX_4fw1tpJAuXQm24Y0pKBzR2FW7XiG2b-YSZPzWHi_Tzr_sMe2UIn7kXrhMYDVMQxhShq9tbS0gQokR1-KH_geDPOSlKZSsmMn-XjIY-iEoxwtExLb9RAGaRlbqH7JFS2LeYaVNumqr-Qa_oI2ZJ39QcXHE7s9urcX7S02RY51orugjE8WWFiyWdtO5mdSdFKZGS6LGeeLS1RwMcvOy_KmR22S-NWa4JE22eR-10sEPwPC-15WoWcZaw71NR0sd2R2zFXNeW7Vm3tIFABm70p0Vl8QudopIWJmFlKeEh1ZWtRZe4aLH9_I4NadE6ZSzHAiIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای پاسگاه منتشر نشده و هویت و وابستگی مهاجمان نیز مشخص نیست. این حادثه در حالی رخ می‌دهد که طی روزهای اخیر چندین مورد درگیری و حادثه امنیتی در سیستان‌وبلوچستان، از جمله زاهدان، سراوان و ایرانشهر، گزارش شده است. جمعه گذشته نیز سرهنگ زن نصرت افتخاری پودینه، معاون فرهنگی و اجتماعی فرماندهی انتظامی استان، در انفجار بمب کنار جاده‌ای در محور چشمه‌زیارت زاهدان کشته شد؛ جبهه مبارزین مردمی مسئولیت آن حمله را برعهده گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25464" target="_blank">📅 03:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=iU2bjWqNt2xTGlvyhbvkMp5-1h7fkuWlNbzqcqC8J6IKeC16lcGT8-4hT-WMuPIh_knVUuUUrd3vxgQQeHDOeqltiudLENsEF9oaN7Ck5EE6LhqSiqUz7SKx-yUg3UUgdd_IKIYvM3kbgx2Tr5wbNb_uuF8AomsiXEI3Uc8UZPYKeL-QXCs-7pauPPlEaGL2UYwIi8OB_edY4XND-zjiKsPCKJJcaoMaUUUhuNumrAz2DuqKJC5aJ8ZmLJjjkqwUPgKvHc7lT6hu_zt7q740-gacEkLX85DKZ7-NyVEGqU4dm2zcgsSo5Yh1w5KC2jQz_TKAuwt8K4C_dIcLIxUQnQ87-oh1uvz-fQWJw5U-F8VqYdwP0xnxa1QYQ8DRuXFTaXsX7579uK5GfJFTWOF44n6HjK6xONlI0w9c7ZkQb9IgqvXrqKQQATQazs8mFe4a-hE_biduTvcBMHFfPAmc5D2Rc4eAOyAs_ckmT1Q3wnSbzhb1Iv_Vx1HbnQlomhjj1w4Sxf3B_ATvZHNqyDQBKjbmmICVM6ysZeZFxRwXV186SpQyFqvIYkxURlA_vjDLOodVOaoFihq0UqrSq_gY1hH8lzEnQxDSz7bb2OkdUFDea_IyoJ7oQ9joRXO3-5vFlz5ONGjoDYDpU5MY9lww67xkxaUeZN0qivpTz4ZM3o4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=iU2bjWqNt2xTGlvyhbvkMp5-1h7fkuWlNbzqcqC8J6IKeC16lcGT8-4hT-WMuPIh_knVUuUUrd3vxgQQeHDOeqltiudLENsEF9oaN7Ck5EE6LhqSiqUz7SKx-yUg3UUgdd_IKIYvM3kbgx2Tr5wbNb_uuF8AomsiXEI3Uc8UZPYKeL-QXCs-7pauPPlEaGL2UYwIi8OB_edY4XND-zjiKsPCKJJcaoMaUUUhuNumrAz2DuqKJC5aJ8ZmLJjjkqwUPgKvHc7lT6hu_zt7q740-gacEkLX85DKZ7-NyVEGqU4dm2zcgsSo5Yh1w5KC2jQz_TKAuwt8K4C_dIcLIxUQnQ87-oh1uvz-fQWJw5U-F8VqYdwP0xnxa1QYQ8DRuXFTaXsX7579uK5GfJFTWOF44n6HjK6xONlI0w9c7ZkQb9IgqvXrqKQQATQazs8mFe4a-hE_biduTvcBMHFfPAmc5D2Rc4eAOyAs_ckmT1Q3wnSbzhb1Iv_Vx1HbnQlomhjj1w4Sxf3B_ATvZHNqyDQBKjbmmICVM6ysZeZFxRwXV186SpQyFqvIYkxURlA_vjDLOodVOaoFihq0UqrSq_gY1hH8lzEnQxDSz7bb2OkdUFDea_IyoJ7oQ9joRXO3-5vFlz5ONGjoDYDpU5MY9lww67xkxaUeZN0qivpTz4ZM3o4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک شده‌اند،( جمهوری اسلامی ) به آمریکا هم خواهند آمد. بنابراین، باید از قوی‌ترین متحد خود در خاورمیانه حمایت کنیم؛ نگران دموکرات‌های سوسیالیست هستم؛ زیرا در ۷ اکتبر، زمانی که حماس بیش از هزار اسرائیلی را کشت، دموکرات‌ها در خیابان‌های نیویورک به‌خاطر کشته شدن این افراد جشن گرفتند. حماس گروهی بی‌رحم و شرور است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25463" target="_blank">📅 03:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طبق گزارشات دقایقی پیش یک نفتکش در مسیر جنوبی با پرچم هند در تنگه هرمز توسط سپاه هدف قرار گرفت؛ دو نفر از خدمه مفقود شده‌اند و ٩ نفر دیگر نجات یافته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25462" target="_blank">📅 02:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4n-0Q1Z9ZRWPEm9JkezYPX2IsFEcmL1WaUKqPA60Rf50c3Vz2KzFWlMno47lmXx3ibHzOhPzmPz5qEGlEfLLZpzABtKuoxSiRffXvJ6gaWOsSs9ffonBOljqcvEYPtySIgbfT3pVox3YqTurzNgFGTwc1RGet6CpBvhTBMkI1j1twDh_3vS9b33Thq3B81TpD42OheGVcHA0HpdZFDuS7wJzyDxSovNNrXPU67bxUqzHItdJutACVPvfrj1Gvt3sKORsN_1Wf1z4gxltMv2MoVmlQA9hbWj62rzYR_w-5XW0_hSbL6iAXSmxhOtmbVjMHMjT4eX60v9J01Dk-U0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بازشدن مارکت ها قیمت نفت برنت به ۱۰۵ دلار افزایش یافت
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25461" target="_blank">📅 02:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTGElbYRuxrWns2QKeMDe0FC0iQQfsfJUOxXuDud5tnn2fbyyIdTFWmRy8eon_VvMM3Be-ExBb_Yf2RAd_GPA3kcpztPQOgrP5AkYzSwTgoNUKukpr_v7ItoMyCkY-uEbrQYML-Dj-53JMU_8szyIR8R3261mU1fsUOpBOob2mnSRylo59XPGe3JkXM5sbuF2G66U5UHtWg2YT43Kpx0gD-RS2hhJybaODxsi8nTDTicm9V3OvuZshtup9BxHdE73hOFzDYH3tN6J9tt5sEOKFKxZqFikjCmVk1ZObxC6zk_TLgttzK4Gq8PLZSxG46QzrdxpnkjIu_Fzoi66Z7fgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند» @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25460" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXN7AAuFaV3pAJpkuTMDay1fGyOq3zdlbGqIROCrJW84q1OhSVLBYppHhhvrPIEvNCsofhoWt5DhuJpTEZNYEZA2klobEiG-oDatLgrK8PJJP1JtXYLUiq88OZbphlUyBI2U3AknT-yJQqbOpqxzy_s1fjb2oq8qcDoyr-5U8Iz3JxiGBA-OyywvM39oLiTjD9lCCTDClgXncSFGDRhVVdFKDkhH_BJg4gcF6aZgRrj4uHBo8VEU5fO4CafjJDDkry-1E-0lX-L-dhxhK4JuNxhvbKZlr86WNgDBidvuDbfiJlVa4rCYyivmuPRtMBARWo-amr01-MX2Zz5OoDFP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25459" target="_blank">📅 01:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiviTwC2WG32yw0zprNOL_yWcSl6dLc7b07BKuoXOhMbL6AnKxag_x4D3C-TS94eacuQ9aA9CXo0lusTI-vEA49il3SIFkZ6nbQaK6RBv2bFubFFyIobpCwYbodJzF_yfeYITzI1wmOH5irfQ_ZX9lXoAz7u6_1sWwBk8VCmyRut6zoR-jG4NnNtrb0UejfDsiYC6sUJXXXaqVSkWsKDDFtv4d0MwG3QHdqLR7flKbLco544LOTJgqgvZMsuZLrN6874PyrAKnRetX2wptB2qjNe-k4FiDGDOzxrivIz64DWSBe6H6EZzJbs4BOCuW-80ohU3VPeGFnMAIdbzqU0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است.
پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای تخلیه خدمه هستند؛ با این حال، در زمان این به‌روزرسانی، اطلاعاتی درباره میزان خسارات و پیامدهای زیست‌محیطی در دست نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25458" target="_blank">📅 00:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گنده‌گوز منطقه کنترل بخشهای زیاد و جاده‌های سیستان و بلوچستان رو از دست داده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25457" target="_blank">📅 00:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ممجواد ظریف : هرجور شده باید با آمریکا توافق کنیم. حتی اگر عین قرارداد ترکمنچای یه جایی رو هم بدیم.«ترکمنچای امضا‌شد چون بقا درخطر بود»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25456" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترابری نظامی وحشتناک آمریکا از ۲۴ ساعت گذشته تا همین الان الان. شما فقط سرانگشتی حساب کن، اگه اینا خالی بخوان برن بیان، میلیون‌ها دلار هزینه داره. ترامپ بیست دلاری رو چند بار چک می‌کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25454" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فایننشال تایمز : آمریکا تهدید کرده که جریان تسلیحات به اوکراین را از طریق مکانیسم PURL متوقف خواهد کرد.
این مکانیسمی است که در آن اروپایی‌ها از بودجه خود برای خرید تسلیحات آمریکایی که به کی‌یف ارسال می‌شود، هزینه می‌کنند. واشنگتن هیچ هزینه‌ای در این زمینه پرداخت نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25453" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فیلم لحظه برخورد موشک بالستیک گروه تروریست حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد ریاض در روز گذشته را نشان می‌دهد
این حمله تا الان ۱۳ کشته و بیش از ۳۰۰ زخمی برجای گذاشته
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25451" target="_blank">📅 23:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک مقام کاخ سفید به اکسیوس : ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.
استیو ویتکاف و جرد کوشنر هم سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25450" target="_blank">📅 23:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0azttyJJl_Mtip8f4M24qNd_UmZYCJtIcIxlOC3qtENsKyjrg7ckpEndLFdyyINirhIo9tg45uSfQd7xw-CjLckhuFZtT4Xm7kFsDdoycpjRH2rQBE3HE5WV_Ax0SlozvT1fAXGGRSLv2V7AM2ae79vJoaZ6GOpxO2djx-gaEHxkgb3EBDXdXPFcMCM7GKAbPq9_W7oJBCGwnuXj-_EMaGTHRvr19YtF3xofOpQg_kfujbTypm5xBeVv5rpy11lH7n-fIzKk8TIw_Q4xi1UssXo4wpJCgdBQEJfY3TfjDGOJGuREA1IF76KSKa1W5wNrWxUwYNkFEzmiwhe_rVfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جنگ حتمی سوم، سخنگوی گروه تروریستی سپاه با انتشار تصویری در شبکه ایکس نوشت «ما منتظریم»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25449" target="_blank">📅 23:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25448" target="_blank">📅 23:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ورود گسترده هواپیماهای نظامی آمریکا به اروپا برای پشتیبانی حمله احتمالی
نیروی هوایی ایالات متحده در حال انتقال گسترده هواپیماهای سوخت‌رسان و ترابری نظامی از خاک اصلی آمریکا به پایگاه‌های اروپایی است.
حدود ۲۰ فروند از این هواپیماها طی ۴۸ ساعت گذشته به این پایگاه‌ها رسیده‌اند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25447" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آسوشیتدپرس ، بن‌بست مذاکرات ایران و آمریکا؛ تهران پاسخ واشینگتن را ناکافی دانست:
محسن رضایی اعلام کرد پاسخ اخیر آمریکا به پیشنهاد ایران برای پایان جنگ، خواسته‌های تهران را تأمین نمی‌کند و واشینگتن باید موضع خود را درباره موارد مبهم روشن کند. به گفته او، آمریکا برخی از هفت شرط ایران را پذیرفته، اما وضعیت سایر شروط مشخص نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25446" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاظم دستکج ، غریب‌آبادی: اقدامات کنترلی ایران در تنگه هرمز تا زمانی ادامه می‌یابد که آمریکا به این نتیجه برسد راه‌حل مسائل موجود نظامی نیست. به گفته او، ایران در حال پیگیری ثبت تفاهم با عمان در سازمان بین‌المللی دریانوردی است؛ اما این تفاهم به معنای بازگشایی فوری تنگه هرمز نیست و ایران تا زمان اجرای تعهدات آمریکا، خود را ملزم به بازگشایی این آبراه نمی‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25445" target="_blank">📅 23:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCFK6w0-i1yNZf3ScBvpFpZVcD9qOwZ73xi7A_LJFLz_QVAbL-slnEJMVJ1Bjyrd8Q5Z8KtU0oiGNTmNxiyT3q_YnYmfpXUxGj0egZQZQYKhDwEzqZDa0oicRrWvr4eHaLU3_1uiQS5ZuulI8bucuxjqSIdiHud6o1GUd1PY-tSYhf2zuxUI6RgK-YstbK6dh2IGL2BdITIFjE67O7Yk3JiTtfJOpWMHAJgWX6Teire5wUvkKnPGWQacf45h_EWmmlZ3Uc94EI5AJ8HdpX7xs7BDZdwdUtmu02CrwGa6l3oDfwKkNT5Jyj3on3OiOm3mim8y03ezYXWx7f9mV3d02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشکی دقایقی پیش
سپاه پاسداران در این چند روز آزمایشهای موشکی و تستهای پدافند خود را بیشتر کرده تا بازدارندگی را ایجاد کند و هم از عملکرد خود اطمینام داشته باشد چون میداند که جنگ سوم حتمی است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25444" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای شبکه ۱۳ اسرائیل:
نتانیاهو امشب پس از اظهارات ترامپ درباره احتمال ازسرگیری حملات به ایران، رایزنی‌های امنیتی برگزار می‌کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25443" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری رژیم تسنیم از رصد پرواز هواپیماهای نظامی آمریکا در آسمان عراق خبر داد و مدعی شد پنج فروند سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 در این پروازها حضور داشته‌اند. این پروازها از پایگاه‌هایی در اردن و اسرائیل انجام شده‌اند و در حال تمرین حمله به ایران میباشند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25442" target="_blank">📅 22:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ برای کنترل مارکت است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25441" target="_blank">📅 22:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHrmnJx_U8zzhFg5bPPUkb6zYtY_1Vr9a4SaKdh670n8uqydK0WILhJ31uUAUN3efsNMDZenbmEJI9xteo62sZ5VCRtF8B9xvT6_bAzNz6D0OxVl6l2dHG7SOObpVjC-vQatREv3La3BG9-fS1WBMmGBhRKUk4qxP3FDo6RKiIdok3eCHn1TGkIbueUFKFY8Tjp3iL4lRNYHCFywHtaE9Bac9V5e6OU7b6meBLmpSnEraUNJE6NOr2owQM5PAQ7bXvg1k5G6Q2trS2TK-m16boFwe_OyuqBXIGwVw_mhESG5gO2brlxb1B0DXNTgFQGOavk_azIzmrJnVDgT9nyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر
😁
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25440" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqCb4qZF2jvm4og3GiMo8O0FtSHstL1PbY8Cs31uHcgrkssTHL2f5uMDg4U8MBMh9je5E_IFDrkeL3B6JqlEMUgZCU7pnLA2COSAmdtp70xSR4yfLgmRFqckgYAUfwYBQta1sPgDKwBuFx4Y0kva7AV7fBWAs3kSOj2XSYzcGvuAwOAn_Xi_qcJZ713OhASFOTUCpLMkzb6313ka3vXbgmeE5_y73N9B-5VXay2IpMMHvfirBsW3Do9UNbcjahlVa6OmNzlRn0HhhKJyMH6xxC185nl7QjSXmxncn4VbDhuJtYGK61AvTHjPKtGKi-d6posecOFN2mV5_-_4puBUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ فیکه مراقب باشید ، فقط هی روش الکی کلیک کنید اعتبارش بره کار دیگه انجام ندید
🤣
🙌🏾
⚠️</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25439" target="_blank">📅 22:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25438" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
