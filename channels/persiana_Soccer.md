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
<img src="https://cdn4.telesco.pe/file/K7JEMbDI4S3D0s75jC35Oj03MbfFijuxTTrM_EE7ZJpJbo_8AjqCY5FeA7RrNoqBE0f-eeVnLxlxIGx1789CaxVXtOYwTjPE4FcBfO-ayUQqf-QKPuFxbGic33ityymom9X4Kyo8spMShEFGxl_5Sa59n2-qdr9o-zxtKxNrG5_17xzk27m6O7WTeVbu77wU3XnmfKYNxsyV1-xfGs5TZ8Y4IQNJ1baxPs-zxdXTx8M2C0WdXfNaOs1_YykNChwS1dYpuabmAnor3QQD_rMcXO3S1e7T16BW06C_L0bGvwISZVGjIhdssU8jHtC1qvir9CDn5cBehWg1Hy7VFqjqzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 438K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4PUbPaDTT94eIzfwj_F-T35uImPOPJGkhIxse7fYOYnJkCPUxrdrWoJCO4LyVQO8NDWD4zdH69p1fXpQ-kKotlq7ecP_B2ONbA4CFTchU1yJAPQNXSLRdEeupcSLvtq_33NVyVI0riQJn3g9o2pUfHNYKBL1RubFV9hCj8JfxppJJ11fzwMy8640PP-tkpibxDWCtA655up56yJm85Vgu7Oh1uC0-MH3sGY2CMuoStIcHD2eIgZDE0gPJ3E2gLbqj-KMTlxX77Ohl00akhRqvl2_VvzoeKMsEE1-CH-AQOzwL-eUu8jT2Etlf89FxZaEEyY7fO8mUEeHz8jE0uPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi_tOKOcmJ_qzb2jBjkSavZlHduFXCgcyaXjf3htxne0WxPpUratuiXDeyJrdMJWLAVbWWq76Vy1euNZcLa16neHbXVKwfCGcEXMI8OEVtbDddLZQM77XBSc8aKmRwYsUfPleBvdMbT1g97LoMWp_GBM8Qh88rP12A-2uupk3PUic8gTfmAHDDQ1uBcpyD0ZVTnYMppBhq80MRSpCGQmI0_0_9-r5H2BzPgWKXP8Z8RUekAJ8_jhiVtpiQPARHhS-d1qQ2XtSf3YAW1qh-Smlmo0smORX-0EKZq3br5fpDP_A26ud1kAMmPKoa6Jdd60WEYJVNLKQ4SJmGAiEqKa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVgPu5yMFpDWwmIP3qMVBZbZWrg58LIgsi6Tj9M03Lzzw9XL5MUq3gw8onxhTkD9V3QACbMTHyF2IWwqRtX7g9emRLnPd5r4HQR6NPqykjz7DYgBP2V64lT4vmITe6du9DUI5FMzXqYUDR0YeRayU2NzDr8EidzH0lhSR5jjBnyXbIpp0MCS-Mm8LXCMfLTdVlVERAEXfykSYnZzqQ8TW9e4ZYvLZf31lXRhC5xLxA-QqaF4uY7-5ZEV1wF3yODY8QLBMXCH804K7CdvhBCB_np82GvZ8zqGZgeOVkCilltFq_aFbu7suEggJpis7EYQUL9FGpmW5Ypt6WeyMNFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZkKX9KIQvov0Td0ktNAReet2THfmlVTg4dO434VgMErKluDHkH13R_V5d10hUeAPLa5OReM9SpEwGmowyKZXyt1zeqlMVckXRBd9imrv_FHGT2kpseuV5SeTYaDlBawPabk6DZ6hGiE5_4drTzA_oM5H_7hd56Xc4VPQii_TPwGcDxRnyPShFPuuHr8v29JNwYLlNfKvAF5JZMgqHRQZI6we3iS1oBAZKSfYYaRmFLA3sH5X7Htjj5XbnM2UyxeEskFmFfBMC_STX9brSLvIEPRsT-rATBRKdMBsVbNW5iopWGVX_lsR_rcO81tE2pte5Gmlce9T58QGrZIwoBjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCAygj28hWv-0Y0KJMX6P0pBjtqYNMDa3aLQcBOwNTFOInsoiJlQCTquEtMuC9rZB-l7MieKzVmTiEopcfK1-DIr3SRyjN9LO0Z3TbVj32nwJkoFgEICFgGOuZt6FBUeXGwoIPMfNWUH-iVgDoAQKSurhrIeG4VT4-xphwz3VzGhCAMzhvFdDf4ElcFNGNLzP6E07lzZH9qgOse_hxhUIbsa6OurvLX-qCO972ezNeckmH9GfQn168LK5GoCOR70NI4_Ur4Vg8JE10nj1vTOTcds-BvcDbzfyfd38exW6iZtSSIZwMw5nw7cdl-ZHODxy5geaAG-XRDF319vwDDscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JejV5PSQLXN5rRO_9_qIkpXSZl8_Wq11oB9hCoiDhrdWO3NjLjH_gOj_N4BVMVtyOonioLPnpWs31buYitqL21DyN3Pq1tk-P4VBFDDg_Fqf6lABuI8JfRhcFjyVpLNgn6Xd8HMS0WHQGMTNR1GsfyoexlBiW9GxeG9WMKKHZLlDsBlEqvRPK6PvvYXEwdal0UowS0UgSMIPldeW98nqVRbcaWHQ9lQ3srsWNqGyhwqS3VyHXU6zpM4glsuUZG1gtwKjcHIj2o21o7UGETAb2_QY53Mf2S1Z83GUwxk6Jyu7N1-zU-MkrUqPKWwhOFCgNe23ievIOsDsTsmPMUNROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗮𝗯𝗮𝗻𝗶 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl7Evj4qZpKpVIJW9MpcmEG07YqD3K2AEDGsj81XDFV_n6CmMBsUYX8tF43hnyqmVEqLq8BRr8da-cDwQ4Sn-dByiSawH9rVtqgc05W7_mG6byVK1rQgKxm2HWzYh-zcQnRZ_6JSCnvD3bAU5JtjvKa29zy93GSrKbGPuRS_GEPgt5H8vs_bOpYYcp2vdc9w4FflbS8FBF8IoyHyv01BQKVKofEmZynBviFzaVI2PGK2JiZGWRr_WL-PhK8Ul_lp5ckfUic_jHKRGJeaPfY0Xjs_B9C6iU4QU-TGrzzCjbZ5u2CCOBVrXFhcNXI3cnw4Wm8vSQz1CxJ3SGpC8f4kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30690" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHmhuyUJRH0dKi4cdC_Pr7kcSS4-8Wzsco1YiWwFpGqc3yPihDjNA0ZJSmdFZaAxmbAb-UjwRVZyHBsci99L7kRE255fh4DsSf1YotJdOZIM26QPujwixCOGxEHHTDGH51KkcTCAsVZHaMBWjGgwtxKbBbuShHgAXa110EixRb8NYmkXKBgkdzfzZ9uAmf7yyAF_d5QftVX2q_gjsUNy95Fus5rHV1TZtkFOLc8nnsB7ugBWlF07Sxozs98fdvpJCytPX_X9_rywl6fRCZMnObJMYzYzn2Bw-YcSS-VRZtEl67jPjERmlBguxYLxJVBiWHrGVtwYmRQ59wpmaHwhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBSw9dZij9YjG-jp1txJ2CFWcAyK9JZaVGmk3ADpwx2PATPvyoyBAieHqexoang5RiEETaagfrtnOMSGt9w2smWtfryv3AUb75CxqtGPhzDZ9KupQt-FJVdjeTzrWGOWYPlTNrs0Ye2f9sapwIbE3c6chCU18UgaAnhc8ah4ETRMTO1tbQC7OczVGQIQWvPDiMIugVq9DriYDOvQM_-Vrvx_suZBT3X7lLLBJJxoohligrHHNRBDrFKHtPfvkb38RfbEkUlk5qH13UjgsmJeZbxomOxp-Y0YDdFmzfAx2qZlfrLKHmVtHx1QfKZ_FB3yDuVBYWBO6k7m42C1De5h_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKHDarsg67XMb08l7RdtjCmJq5tljUYf5ICE3sYGSafPPOEFfzc8hDetX7dvCU0-nxW944NRfTunq-0e7Wmcb_jjQvSKmycyb29BiK_tWoHB5drpYdkdsAU302grjUTugXlxAe3L9rgMY7hrDvDo9fdJRCkFMwm8nNVw61COmvECL0qsY66m4iYr9LpZtLTFpT96ILmxAQxZU34T_60NgO5LVD4RwGc1JQRhyAIiiMIKzquhiYGXqqDpvXzGO6XNhPjxF1ThWLn6aCqrs2ZW406Jvck8hkFSdPfHEgnjNEM_Gj9QJ-5BeY4Lk4KJ3UrRGV2C0WWISc0I14rpO8yyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn1OFM7CODKMzdomTnBrjWsqJfiTLFthHiR0B_QHtJD2QDUunZ6478QbtdrZYup8U9H9t23CAt5Vpm-5YJtx5TnpceLPx1GVUKhvYrat5XCAIpoyMliydehBnKDLT1RVRQc15OYAkIP14iBuWkXxUYn0gl1MifqborchzGABpKBranfzJ46-ZG5O7S3_kBIoh61F5ABPEi9WhW8rg2CMqDJ3g2ZtJJxQP8h9k3bW0XYYBCkSGB9YYkU3NPi_OI8UZ_WgTfI_S8WDq03GyM9l1i4qCWzwLr2S2_Q215hrDlNqN-BD61SndkTzVuLSqE4mX8gRCunREaMop5ZSKBzdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_oUjQik2GOXQxhER5QH4PS5z-KMPkEJkDj8ESl_ZDNWOIEbgbr_4mtGVIkckopGuqK48Uev60I8zI0pemSajijJ_30puWMdcnlGQfoFv4BWBZMYHRVYKnO7lhx_ICcknn58McaTsESralrBq47du42t8IU81Wtu0A-_kQPhPIm6yj86nsckTqTI7b-BEYVPr0UKzcMSC2_jtGkXxBuAxVzxVLDUo194CJr2FIDT-XCYDAZXJdpq86arGu8De-v74ZevBoTvqNhF9MkcDa30oVwZmeuCLGc-PZg6u24UHWHSVtaN7l3azq2n-fpBEf-jUmhEzgIqglEobcGFWLZKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1xsMPhE4GeUuZWkJFz0qFRkq8-TiZKkHwOJdicL9QkOhmnEH10WySPFW9INWbKk4o6JRu9oZkCVjX8X2DNRQ_Hdul0aDhyaEdEjJQz9b2ycgZBTXfkr_ZarXpS_s_fvZNbg1BqIY7bHxUoCPPCxvURKOnDgO0D2gaTSokjnyBRyvgraQvGPoT9CcHQGfSgE-Y1NWsyXMvq4d92-_BgF_rozfPI8ZeH-ftYRtfLXP83WUODpVjBgAdbJtOaBXo9sdhpcHCIBoyuB4AJTXDpPTyVG5jiNQZpfhXeqllljTES-8-yLNOZhxSMbkYxm7eVSnMHbwDX1W62JFTXGxr3gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZGpV6dKE7ALndG9hEuNnBSOLN8ZX6GzSGFRF2QX6QPUmAQW15HcCIcgwEAY06mn5AO2rXLMReaflT5oiWFKWEAXFZT-DG-WDUB7pe-KQcwcULqxsAOYU1SV5bD8OYz5w51AHxpYlwk_qnFAv20qlxkqef1JYdx77c1844CDxydMKvYC7RpSV7P00Nzi74spf8pmmf-1_oyhGK07_vk9jNk56zFu29eXMju8IllAkScRsoPjnF24pCwppSveP_f_Rt0LHkckTyax-ZyNvqYPOy3m-hZom8MGmgnK0scXhuItwpirnk-ZQ-u7uwt8jxKlHFzQyNWvNhVNU5SY6d42JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKny-cjtOHc4X1--BcqEHlBs27Bi79pfKSIa_N5dSxDu7lAo0mzBBJiLGjeb6EkTetPGVC6hDaAYaO0g-mAFddt7Iu2fnDAT2CbKpVNTLVkmJyu_hDxxEH5iPFLvsA5RthGREvjmuLYg9KMfxKN9iLKHXqU7_-KP8oeoiKfEXv4pJ2gcAwzOJiy3bkEI81UYL4p6z3dgZFt1HojVUheUls3BHFyF-g5rBzx8bvjLw92OXqykv-SWBZp1eSyfeKLYKyiW_DFSrbB8VcuXMXo2AfXC5jIhgpRR9uZvJtQAybX_Ey1xV3ysn_WiPsWMGVIJAcG0VRxNbF6OitZ3EChjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-llfwoRKibYtMVx5UecwAP4RALeBkzA2LXP8quZr07x4EJ99Amvkn_yFb5_YRH16Cc_ACRrer9Oocf1TGX0owklR-l-AA18lyC-OqgMbU34qYZAd7aO4Xq0lITs1ORAvAaC2AbTFTL0EFwqy3j6dyhaFc3QH0BcC9bNjVfR7seJtjMSexYuJJ7mJy29vbZ-VMUprQOAoULBMMNeKvxHR0ApN6qA_KLmL_eVuSxfeEMO0D5wBqdb7dF2Al39cAmBcKixF8OByxyFA6TVhvlu_qVSHlL0cTkmv2_IqCLT2QEYjGPtJIh-eVsmkxQukWG50ScZ7o5PxMjKP7DAL3cbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJRt8b5KbkimJsFo8b7l-jICKQNlTCFap_ppOVlICx7EW2OBKbu0_rSg5H8KpHKKdMVR2CTKPaSkn6M_gbqRToQjUmxztpvdgPFfibd0FzwB4oCS1WjUrN_WY3_s9ncX6vgrBhrpo_dudlHMZRyp1FT7WkkrJpnPEUU_-a5bI5nhHtE0c3qkegeNtkBvzpqgABTH6-y-9v6a362Y0RhAfQTwf6d041dMHvlVtcACQMbJBQ4hE-JEMFZps_nEhuXZ9yj3qLxC1gPXaisWP7FnC9yQLIOPyEu4OrINbnuEQfO5jdtRA7hQfy0jhOnYxUejLCXqXZ7qGiBjC8b-BnUTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGkVKWMsWct_ZgODx_VWSGh2hD8Qv6VvjHGDbJKtofD1jio48OgYH8DvrJwnZAoFWhwsIuA4Br2Cvy2RWNOoNFJ2O4RlO4wqfF3QrHYIRP5c_VKKnj7b8x86UpcOn6pfMyYLNxLilRzVNtWMNW_bi_vf9Vf_wDRSb3cu8mGzuO8yVfVMBYFCpEAiMlK-1rIJHfOTc3rxtA7-01mKseDZ2ex0qdJ1NXHuPnOTKpY8fkm9GB_MgPfugrRFvNwsKXqBc0-3AGjitDa03QoTienfgJ7fGf5HN8TUXrrCj9wbBX7UT1dvE_3CUx8nDQoWyGhEcoHS7k5lKj5xpHrmnziulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNfNhREIXED4GvXZFB1Wo8xhnwN5nZnkQef9VHuBuA7_oBgNCrkKENhBTTiHFGdBz39huOCMeNsj5_aCP8hcX0W6yeqUaJhaolgpGnAjyA5i47ORhsiHLa4-1GQYU7p6EjG3ycJ6cMHMK2MeqvRWIUvTnII5Xecb-OPM21zG2z70hyaPAlqPzGB-xhEbiNY6UZ4BQLhLoMHN1UNzzAKVp5cHINKc1Iiu449Jh2XT318ki_TDxjyHIwm1o8J2buoeEOGSH0ed08lcJBueOp0h2mQGy2kneIvQ-jaI18No9sQHOpkqJD0SpGzbiwYf_BiOO1IW2WEtHM1X6oQLzGpuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-gI_r3kBSHI96aW-mbe9Axl629K3gL0Gi93k4g3gZIOG2caH4qLX6j7hGpZdhTush5lxHjVsVVWlGF_TIySh-38-LdRBOGiF8ryCHRQS2Irp2KXvUIYy4Z8uiQyNRhiVZjt1XfQuX39ab2XlmFDfY6SzSCvbu0tWzZMv2gsH8lkB2sNUBUOSw4LlliJxR6Z__cZc3eElYZ33I287FMjhY6Z95i_Jo9pKptC6N8_DVh4vUE2NfPmtEwVm9WVgwMFp6E0gBkSMoDpqENZnRJuo_SwxZdmxC6o_PCSGCUYmS9q_teegJ9oCDBg_2Dm9rSkO3zgzqEPirgKm78DNxZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEm0zFm43HnrG7tGcsfksSW60dM54pOYqpFd8lwuD3_s27S2jfPdxE2v_BzUdeWkS5_l2OJYcGq5KcyjVQZdcLm5cdEZaMWYduUbu_oPdh1lhBQOXUf1TQ61CD7r9uPbMTRCJ4T0DQuLG8ycSB4y2HD9wp5KJYaOvawxJC9e5pdAd5AzbqVcl_tnwwfCgif7I-2pzk6pPOBTzoyULbeiqMkrChpLiZuV2YdtnTGn5Ob5NGx5_Y6TaK3HtnVb_GWoYW5NLL2Acdn_5YlX7bWd7n9cgtN2a-rpqlFMuwDm2w4bCkfkuG1xjJuOCL9O_6B1id67ejKyL9g1l0pzzlOQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6x5i6FoYpcPCjLln5j64keiOvdFeVjutKYT4ZjcgJSDW-Eev3TqgGky2Lwbh8FRy7UU3yJTN-FBnjbr1G2eHDll7z65s62cpzDy582VIRMs8pDeT4cLXvbn5siXVxbBVEvqmqTJAvWla8S2-7JGK4dDm4WjCTzA3x_TWAh8utbn-NEcUPCPXYYGlFglwe0MwLa7Lwpu3yvH4gi-R9DzMeohjQd9ssEgveM8DA6MMefTSuNrCk5jz-zdLNZSyGriJIQx1cyuivCqM2hFFfk-vcR3VA8jOfznz7buhmp3kbibnKLJ5nNuBaT7pWmB9yHmDAfr8zwxzKuHCsAv3gQmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APD2MmHtwqazxcFgyjEUoqTvzcMkQegMIztVBy-qWSu7Uro6X1_SByWuLWkqCo2YbFpjD4auaEqy-eJmwywCpYtnZK5H1NIPChZpX9KdJ7Seu_hGlMSQBqgeIrRhfufYe5XwIwTehAL8HFMvgIICQ25c3jMBE2omJOKXgWbbXL7GDNa0PxVwBFZOfHvhBrEYyo5OecNBmgvGbTukmEBdEKsz-tCPtJc1rF0asiLS0nvF8afX8wRCjFqCOulvZSVGMlX4bTnxkQfGkf3gTdsLm9EWTQzubbMkOO89_OY3hdVzzDqu6tY2kXo3jbVntOiwnTx0TN0IJtMY9xqZdU8-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmFBINKOgV-Cti53k3NFIriy8wAAz2JOpCxj1KmJk7ifxUdJTCA4FVR5Y6oLlGVR2JdQztA04P0FEwF5KM59WuvgpWITbM1lK7PI2GV3QUafnUHrBiTEoDUpvVvOGL1ywhvlpiJtElT0PJpBaFNzPOW8Jlo1C_UXcjbktUJVRqC6VioRyl72NcdctetUCejUTCu66yMdZ7n1D6HeYZqMQkVsr3qbVKU48h9-WbLVzwXGLw7cIHOblUikzYgkAL-63m4xiHTAPxqvpI3JcwfMru0dMtlDc-qLQqUQFgPujPGKdE1L6NSDO0MioKqf_9EYbZum4o8r5fVIChoE8sgxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkmLqkYaNDmLFA8XFj3esxcLl5CGd5RlGJ8kQm2PZvQfMuoTfF4grjtBYiDEy6KcSZbb9kUz1d3l_uDmhsU-AgrauX_qam4A6S76qX7JjRSR5jP-96673hLeeCt24WsXOKC-rTOOIUFQBNLf5k1R5t2ZckxZkqQNHRgHbRAFKOVbxvlRrz1JWPdn5GQFinnThE_TDvMGJOjao_I8MTq1UDRUENNNqXP9mibhgOxupQ4dxISdxZMV4oSA4Ec8eze56B-OB-CNBtiTkJs0GkpW3tQmCJv3Eandh_DDz7ZzJro80xPtJA9IGWPNkGEdkP5ylJQHb6lwmwunnMUZpCdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX-v53cPOqnG2FBxMbcGmeT1CBBCPyznz1mbxEWCMB4T7pBXTQ1uxTugLHWWfdckpCN-BQ0Q59fiXIkNBN88JNLmmIjY2KVM5yW6nTz-nDZHiZGMIjatCx1xV3X-FdK93e3rjXo7UGmQ6ahJ5F0qOSQrTzvuZ2aUpdwdIfZBMbe374_c5Ybi5seOMwGAvDOwxbsWq_uwa6w7hk1H1PnWaJgK8w9wg_-SQBif09Ipke5ipS6PdtYBkv3nSyJAPWeQhwff-kRi11twGZ3cTsXbq01JrdoOici6-rlfYmACmqTra0dc2GraP5YkEYnW0MyIfRgfW3eeKNt29KHfL8B8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=EW1aMJYYYco9nk5EOzf1Dwdx5pQCMeabwwp-zHtpGrkjZLDUb2M9SGVqPkdyYaqxJFT5IGLqE7RCpPRjUhkeyq8fjvvBj2dAKI5f6q_vink3mml4vytm3OoKeAsSjFp3OU9M4sd-2KoBPErd0_Cq52CbjbHXNgnrirC7DBYMIPSTtDlKkCaz7_mcA6Vankd5cd3NT992RI8l46K5o43d1OUekEzqlSzgX6lU62ohlvrrX-dsYVOfu77l2p_taA5BbkQ2TFrqY5l674zjrr6KIFmID7Poo7eaXAcro3420--Jn88Trg9ndtr_vg6TigQMpGfdUvE7K7-UhopTTzQflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=EW1aMJYYYco9nk5EOzf1Dwdx5pQCMeabwwp-zHtpGrkjZLDUb2M9SGVqPkdyYaqxJFT5IGLqE7RCpPRjUhkeyq8fjvvBj2dAKI5f6q_vink3mml4vytm3OoKeAsSjFp3OU9M4sd-2KoBPErd0_Cq52CbjbHXNgnrirC7DBYMIPSTtDlKkCaz7_mcA6Vankd5cd3NT992RI8l46K5o43d1OUekEzqlSzgX6lU62ohlvrrX-dsYVOfu77l2p_taA5BbkQ2TFrqY5l674zjrr6KIFmID7Poo7eaXAcro3420--Jn88Trg9ndtr_vg6TigQMpGfdUvE7K7-UhopTTzQflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzhLRyo-WgR9wF6hgf6NiQQSPxCST4QGK_yxviJVjl10HwxEkAkj6pBG5lw15bvJwlWRiSriO48TMgaFRz-p7j7GHwHBg7LeB-APAVrMikI914Lon4BWpAWufDRgxvRXGrxvCzmm3_wb_IaEmit951BTJI1IdgNxLPY7HfOtMGf21tkeRjs0M2b9rPlQ8kmisfFO_weR81dIjOaYBZdqVW6vnaOXYe5ErAFR42hkavp1tO-MfEljOKFRQiWKxn3ZgGNt3yCuOpizJTXHPx0tW8jqFHBcT6n6OAgVF4AN1AXUjBKZmgAHjCO8dT9uTzUsQQptJRBGS0QwmnHGW0iOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=A8zRS6TjGtWY8bOvwrWISB9l2ET9FvmtThvotvfATBmQCksdWoSspUrNCLv7y9lYcLgleq0tWJQe1QdTwrar7SUwsymVziULgZxhG1SKAC4DOKmyBQCwtoosseMoxENsQFk-6pFugXlKq1CAFm0gVA-rzp9Dd_SH9_blnoOXvLoKIghLPnF9H8gReBkNrqiwdzWqAEGC5vn73sia0aHq4By6VrQql0OFLVMmDiuigPmyw4txU7oOmpm_E54JZorY5sub8VFKxyrjBLTVrHfYJcWq9FMBf8rq8GRtjLWrJSA9F2Kux-L1Bt0cpAlQx5i1avab2patUF4nFW9rC9N23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=A8zRS6TjGtWY8bOvwrWISB9l2ET9FvmtThvotvfATBmQCksdWoSspUrNCLv7y9lYcLgleq0tWJQe1QdTwrar7SUwsymVziULgZxhG1SKAC4DOKmyBQCwtoosseMoxENsQFk-6pFugXlKq1CAFm0gVA-rzp9Dd_SH9_blnoOXvLoKIghLPnF9H8gReBkNrqiwdzWqAEGC5vn73sia0aHq4By6VrQql0OFLVMmDiuigPmyw4txU7oOmpm_E54JZorY5sub8VFKxyrjBLTVrHfYJcWq9FMBf8rq8GRtjLWrJSA9F2Kux-L1Bt0cpAlQx5i1avab2patUF4nFW9rC9N23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارتاکاشته‌از لئو مسی فوق ستاره آرژانتینی اینترمیامی از یک نقطه در کل دوران حرفه ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXyUNr-tZXQQkC-LqhUpjBDpfPPhtrm3D81rgpnsimBYYe1_Ne9Dzji8FwQQg1dTHJOpGbVKIFuidZace2SKe05G-xOwppGo53D6Ke0mAPkrvYuhQ2KW1Sg81fNcH8SN1nOuCHn5i7FNdyt1mL9eoBCXphzt4CHHOmjaCNYY3bDZinqxsix5pIwuqWrpFntzvKPio2DxEio8LuDT4DjrP-rr6zQsIVFQWjTHDS5m6uG_D11YG3j2rJcx5Seh1R0Hk8RoZ_zeCoQHDn1qPtm-RDn1L9nyUiOW6nOVRP0dUkEofAQFRxVREg739hD4Nz7R99aAFZmGA7axsEIizDxpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm0RQs8S_BYsGV7fOKaGOkZRy6jm7Nbojq3br1yecF0xexcxRCLO4cM6qvbU2QQT4RVW1kTdDHp2wFVqGjLJ4ONPxqAftClbktqXRg0xZsRWclBSBSXOWFezMXmPYZoSHTOoVqzpQv9dl2cpuLdaqZqiZNiq_58cJx10s3dGBeIk7M1Fj6XNrOa1XxkPbq-ry6qf3IYf0Ei6S_dKxHBOXvRqImur-FL9djCluuxkp07hUaosjW42WngKHZVWGYoVf46ObL-cHTQUx54m3zDlpiyOkI51KgvifSLtysYlA1c_iNjwl2yD6BWyaKJzBVY9CujC0kpTrNWSMTOG_xGdCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30656" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
WePari
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن وی‌پاری
💯
ورود به سایت وی پاری (فیلترشکن روشن)</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30655" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOa1lLp21vPPri_Rz5t706UQw6XHL_bMnecqZ4oejkAHL37LhcOeyl4YyqyJrD0MKjyLTsKq7y432MDYifd21X2JFM3AyNy-cG2g2MilCxvZoZ8J40ndVa4iKCtqs_jWGJHXsVUrt2mH4F3U37cnGYQbGuK6CiM0oIDnLsCd2utmw6EnN1VmH_12QWX2xvYjC7dTaTdCH66uelJVm0236k6L_843zMYm3K09vD0hewg1QC5jCdvnYwRyE7tSrznorwIqXNWg0jBdiNP9WERUHQ2SAjGD9HBndG2Ef6L6OpnwDEACrCyAJVAafeKl-glWbGYIp1M_7sfLp9esFb8OIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-WKvc6fOuqB-hIF3Kj810pWs767ba4fszCz3hyCYfx8Iy1s09AIAa12LBH80EJjnczAX4As0BYOqCPzS4dcEIi3uTNJKzq8sZc1Ujiyzm2OKdj9KLEG-0z1LduwpFSYPNH9lOT2S9Bwkn3e8MIvWDY0a-czWECaqSaZtCcIN4__NgNY6JFd_c1S_JuOv2_f4cbcb3Hiw_9y5GZqGJvYsPJxJiAzCMCltke9oqzGaS8hvEU696B1r0x6-wxuaKp2MAI2j9WxPe7FBR_JBzrhtnUAfQsQJCKVF-Wh-NaQaOuArGa3mqfsCxangF6PLSMWgpPEaMzAu-utnBP1FYXGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmkiJEGGtMjUg0oS0D9nycSMAn0VVBMF10Yy5FlZTjdCHykI-kl59q--SvudK94LaTFcIqEiHdZrHzuqL6E5TIZuTvum9Dgy7lC1rm-fkmG6ug06uH9WpnoMsnzPfE0K_HALKbTkSGnm38xpQYqcNpBm9luBmZhoJzMP8vEsfVplmhAAiCTp7SnsBAhDQ32SoX3oHjOpIFcbyXWlteNrCnZZNv3JaQxdyNMiJ_6GW3qUgTLoP9Hc4XKWtb7UnxXNXF-VL5G4rVpA9uNgHgP-GeGYaUkXvZHuY-OzqN6K1DE__kvCSdgnJE2xr_DvZqDISPaeIjkMu0DyYzhoUcD_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD9rUY9V_F_JROz2vt6VxsPG5dR9ojoNOKRzz_r5RNBiGzZS1qT232MBg8KAsxLqpleimYp93a01yaQ8jf-Jeayjuoq5axSZvEBLZXWod1efghQYsMcB2JcYOo8lKUKvoMcAxDiEkH728atihOYlCzxr7rT0T9UvrgSy_p1WpW_zBOSU4FCTZyKDoEzhJhLnhT9Ps1d28EfiJvyLD4AAe1PzDtMCBfkaI2vskMcCjlG3o3wrYIHNz8ZpiSF6NONKijWbkD7GzG5iSMx_Hpd3VrYFIQnAJNV7dMhTo0q3ntbRlCByB42WfiVgnw0firCm4KbJFTJjr2ZS6meLhxyhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2pTab5zXvBhbt36UcBNCE4Z9BvV5rGcNHKLqqZ2bQH7fhfC5q9myPqLgLxtVraXVq_NlcOUDdbReflNjtIMdJbOEvpMn6Iy_ZCbEartmkZI1-MiSy7dYvFjV5AGXlbEptHa43K66UoGvLmQJvyIOLDVp2e_tmQ1TeZ9pJGQ8YKyB7NnSZeEHxfaOgHcPJQ0oRbTMHDiv2f5byIAuhc6wH3nJovAla70bhcO-fPqeIopigH7bzXzHDdLfmwqTE-QT8DU_TkaZMNXQL8CgbmKzp4ygVOt3Tujj23XTq-49kKT2m9GBsxmoeR4dE93D4_sZ1XARKJUcL62uUd5LGSjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFGhRN8aInTiZHUoDvzyW9pAovhjtfz8TW-Do5f94ajmm2OFIJW-AxxVi_SUpBVrGwgylz-12aIjs5D-1OT7_VeccJJ0wZu_qCyEneGj2fa05jggB-1A9f_wcWjeJX0BqK7lFxp0A1Q52mUES39zriFlVQurK-L1aZ7pCSbm802QqsekXHAWXOIXvpf1tSCXYN_PNyBBEBZEyzLcuoBaDLVqdPbI5Id0BqwxjIlDYqRRg8ZDhyFy6ZSdbWZtIuj3QjIFeG0dxdAQtOn6DIxZ2A_diy_VjMjoH9_gGqoGiiOk5W5oqVQ3O8JD3el36HCYZtny7_Hpefi8BGzapu1cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=ebDUquzQSD2VDSbURqB_7dlY-oEVwRlosSiS2cfFslIVdO8vooOdE6faT_0XEEe0XCrbuoREix6cAwTlzB6K0ytHQZQYMMTRL5PKYJFgdJSdy5jqYdb1XpTehorpPp3Uocjdnorqq8zbaWhIzMz_tDcHKpdhxLfWZtSbHqtf3yuLwYOZ962HkfB_ThxJp3F6aqMjWT9OEAq5ISxmgbaKsVyw742XmMI9FzA4efyVCPMSiFG_kKrxcBO0rPdzoZXHUcx2yDO-dPwcbqzKJX3hlb2MnkynOcdihaxhGcVnJNuHnf8dOqe7fzmPO6TKLB2CXyfc_jbHq-nnEs2aCoqa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=ebDUquzQSD2VDSbURqB_7dlY-oEVwRlosSiS2cfFslIVdO8vooOdE6faT_0XEEe0XCrbuoREix6cAwTlzB6K0ytHQZQYMMTRL5PKYJFgdJSdy5jqYdb1XpTehorpPp3Uocjdnorqq8zbaWhIzMz_tDcHKpdhxLfWZtSbHqtf3yuLwYOZ962HkfB_ThxJp3F6aqMjWT9OEAq5ISxmgbaKsVyw742XmMI9FzA4efyVCPMSiFG_kKrxcBO0rPdzoZXHUcx2yDO-dPwcbqzKJX3hlb2MnkynOcdihaxhGcVnJNuHnf8dOqe7fzmPO6TKLB2CXyfc_jbHq-nnEs2aCoqa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30644">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6-rKj64RjdOIePkJTrgDW3rVU2qIUSKfPY8rYI40xaysdLFFkc84a1BIbiP6TCfMHEjiTb3EEptuatrYKjgOcN4wKQezx8l60XkLPiKglneLaU9PK-h6xDM9taa_aATydd4gPWIyPTfkk_WnyrPgyNqOMHqmuJwVCDRWSCNdoLJiqZKey84zohigc4Mt_sppAJPufE-KkZvnzqB4qub_tX5T3zwbzzdCqRm5HsrywXweY1aHulygkPj1jGGgNhouWxDtYwe_uAohdVWMChlkaKalMsWKTSJj1jJEoJpwdz2fjzY5lKavwen0RKAzbyEAw2HeVlcFO3O0egnK16yfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
داداش فوتبال می‌بینی ولی هنوز ازش چیزی درنمیاری؟
😏
⚽️
یه سر بیا ایرانی بتینگ
👀
👍
✅
تاسیس‌کانال‌سال2020  اینجا خبری از حرفای الکی نیست؛ بازی‌های جذاب رو بررسی می‌کنیم و فرم‌های روزانه می‌ذاریم
🎯
📊
💰
اگه‌دنبال‌یه‌کانال فعال و رفاقتی برای پیش‌بینی فوتبالی، یه سر بزن… شاید همون چیزی باشه که دنبالش بودی
😎
🔥
👇
بیا داخل، خودت ببین چه خبره!
p6
🆔
t.me/+3P2wZvzhZbsyY2Vk
🆔
t.me/+3P2wZvzhZbsyY2Vk</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30644" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9feFfKU4IXVJXo2BU4bnR77Pm7m6sgN4f4c-8o7dH9RJi94MsuOaUe1FsDCkTz5SrY7M5GFCVy98GS8OvGG-MIEL7usZqCBc98rLDZUr95QZQ7wPGTQwhmsOhdVNBuSmuGFuQDhWC9OpYQlKYkbYeDau9aWITe_7hU82tR_nhxStULoUrJZbe_ofFetrST_EbtRcvnMz_HmaN4Z50NX23NcHz9JtrddUef76jsXXtVrxI1WpaE8EUTdGpO71uO0myHmM0RUAOxeQgjyk8MEtm5mcT5DFVJq8r-8BuYTmbaAiwBCHm8zj8YBx8Cw4vWTUM-yu0rOseyujK5rVpz_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT0x4254ew4Q7mv--XICkOuRkzYMZ1EExCrF8-WGo4W4JsRGi514nxpilMyE-naVOaAjViVabCh2spsy8ZC8LE3LDQT0yoBbkKAXUBBi0W_aA0RefUed3mz1rf4WU6lENUXc4Di79htWJFz1OGVabKB5gfJbxuaZrRRNS2S-BqDDoTREiJKUGr8pDSxSatAWLvj3lGLfpVidQavms20glbNzD_QuiAtnW143IZvTmrAo6ZiFAvTGh-lpj1_ZWn3FnPy1UA1tltZ4UJVBKGMtlxfFmNyUXIkNloMQ3jOpLuMxPCx9rqn6FuM1qgfOgBDP-czkO7RHA11QOqXDp4y7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSnURJSJjhxqfm_hPeiLBhF4fp45H7DNCkWUnBYgn91ca17OyZMSWQJ62MQsD4v58oCk5oORMf7ACmO1radE-56romdUQ0W-qAUgxsJdCguMPAvHAy70g56EhrLbyD24KiuDXhCbAMmfB5QDVScb8IJq3FBL8USEKTqfIsnCPDbZHLANLXSaByaxe2P6TtkGj9qgj7eSrskS7EVmRMxCCMdC4ZZPJarZKDpY2Y6yJ9lMeFkqH4K4MD9VtP_kbwsvKqK1qRMSUvxG9nzbgrfjPPG4MOwc0vhURZkGbvOh63EaeHMicYuy3NonCf6FMWwqHAwWZ6IVjV06f3K7z42j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=NQnCMKsHtT5xyIaRWRGT202hlJcAabgirfhYk2-Ljt0ZteQP34Lhr7c4vitbEv6eJXvOogaKE3_55Ap3CxH_TqP78-uKY8AMBeyJXRL2E8d64w04vGje47-Ox02Pl7xncZgB9iJzSjPRn6m6cWE_rsFE3gvhmEDtJIQaHkwsfFPmigKAzrw9c0CrMfZFAJJhAESAlUAafALm8642xq_Xqyd7dUuQAFbk9kuPGSvypk-R9xyfCyVLj-MBjs8QdMB7DM1w-0vmNO4E2USzy-lhkf5Eg0CHkLqetrg45a_arSmPlJRPega_4f7ZQkIdgmTiaC-NCt0YX39AdyvfgpUAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=NQnCMKsHtT5xyIaRWRGT202hlJcAabgirfhYk2-Ljt0ZteQP34Lhr7c4vitbEv6eJXvOogaKE3_55Ap3CxH_TqP78-uKY8AMBeyJXRL2E8d64w04vGje47-Ox02Pl7xncZgB9iJzSjPRn6m6cWE_rsFE3gvhmEDtJIQaHkwsfFPmigKAzrw9c0CrMfZFAJJhAESAlUAafALm8642xq_Xqyd7dUuQAFbk9kuPGSvypk-R9xyfCyVLj-MBjs8QdMB7DM1w-0vmNO4E2USzy-lhkf5Eg0CHkLqetrg45a_arSmPlJRPega_4f7ZQkIdgmTiaC-NCt0YX39AdyvfgpUAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmSkNVHdvXhTLj740MgoKTJk6BaSBjBIUN_LA1j4SQ0ATFQyh2mXjMFFQsGrWo6O-H8CWnmR_vSaBmwCicDeYDmY7fVtmGsfJZwxjWGA-fwWnwP3hN8JRnrB-LIoo0CZIiHlWUHQWYnvr_HP78YipqJA022jyWyB9Kj-qIAG4zaaBwcEXTaHdMBbWw0Of3vuTECKPzvsQQ-lo5xkzvWP8Nw59Sn3YpizkV1pisUekeiA0IKWvkQoQbj4cZVxZSbCGBmLI9UodZML74gpWpXaZCFCEwjszOY54mDCky1EIOCKKTWS1fy5fr_fKhEv_1RvMqrN0s6UzabjI3pKBiB_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=Pgm9CMCUcDGlYotHs55jdZKMrdd9NNZUEU-417xd6AFv93_nqVcsTh9eriA_SMEgtSddmcyIczXEJpnTGjlSxU5hmMjck7M6S_hFyxeDx50Url3cdRbs13_CvDzpknw-7HAITubtTjZBN7per8SKMT1RNYmSP_MZoePSYICCzEL16H_rSf8dKvHAgbOqwT-1kMsw7-4W1wyCUafl5jAZcxJEHuFjFrzTHjgHmaGTUz48JlyL5ozPGHel3s9hDBEeb--C2EgSdE2MI7hbtAPJ3kBjHdhqjeXjxzIWAvWcJ36VWq47NBGywg_asvBBcqQKNPWH05Y6bLDoHG_wyA9YeD-4JctrRS3Q3LSrQ180N24jjv4edmJM-HUf-vr2MDeMQb5l3zz5rd0bKdv2b0AUZ95YMVdY-qjhBsvG01KAtF5Z64we5V1c8mLvX33HdnoCWutOI_zjC0pyy_q3k2OemwzYplACqhWaTknZP_4g4mC2AGp1kBn7JzScyzgoeZ_udzD-MtFVcqg55TaLBG3Ln6Q2dGJo5GYuNCWlbZYiAb85dAK6d6LnxDV_Xn9iiNT5UvbPri3TBjuYY87YI5RPxT2LpVmGVK4faWn61eoVrUkghw7WsVXcFASHIvGzWfio0_Uq70P5kVcClA_VQEBXSkMDuyvvpmQyN4Zm70qunmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=Pgm9CMCUcDGlYotHs55jdZKMrdd9NNZUEU-417xd6AFv93_nqVcsTh9eriA_SMEgtSddmcyIczXEJpnTGjlSxU5hmMjck7M6S_hFyxeDx50Url3cdRbs13_CvDzpknw-7HAITubtTjZBN7per8SKMT1RNYmSP_MZoePSYICCzEL16H_rSf8dKvHAgbOqwT-1kMsw7-4W1wyCUafl5jAZcxJEHuFjFrzTHjgHmaGTUz48JlyL5ozPGHel3s9hDBEeb--C2EgSdE2MI7hbtAPJ3kBjHdhqjeXjxzIWAvWcJ36VWq47NBGywg_asvBBcqQKNPWH05Y6bLDoHG_wyA9YeD-4JctrRS3Q3LSrQ180N24jjv4edmJM-HUf-vr2MDeMQb5l3zz5rd0bKdv2b0AUZ95YMVdY-qjhBsvG01KAtF5Z64we5V1c8mLvX33HdnoCWutOI_zjC0pyy_q3k2OemwzYplACqhWaTknZP_4g4mC2AGp1kBn7JzScyzgoeZ_udzD-MtFVcqg55TaLBG3Ln6Q2dGJo5GYuNCWlbZYiAb85dAK6d6LnxDV_Xn9iiNT5UvbPri3TBjuYY87YI5RPxT2LpVmGVK4faWn61eoVrUkghw7WsVXcFASHIvGzWfio0_Uq70P5kVcClA_VQEBXSkMDuyvvpmQyN4Zm70qunmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhfCRGpokqmJzREaLJuVka5IYBhPs9uB0uF3nQtHwP6ZW0_QkvQwrnJcRHWr9VB9zm4ynjR1bXkrYXt3Zpbwx5imcCrfmCMSW2e-ELYlLghPrQ-ZnnKJkGYxNd70AaXsV_G1TFrsvHsomyS5AqJv7Nac54_sWFWHmyxnC6ITMW2Y165_nfrLArdqoamy-KuXrGYn-dAGqGnThcqJYCCP96rdcJKXjBY8bZLSI2qUKXV8_5h6O9ILpNJnZZMK-gVAABrut9sm8yND6J98nnGOsQnqnhKab3LQD3lvT3fuv1Hfa3Jngrvfaj5w0fxyXfx5hW6j_TrlIk9ytu6FBILg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC_i8xn5FZQx9Yp5InZb4hfmanRwde4ulTYvKtxDOQWa-WQ-lH-nRPYst50kfVILzZZBAuM59e9FtYBRvi427V8aUZEEY8_OZpcVntktjkSzWnMrXfyfTuTlPtqiE_Hlmd4ygIVz_VH6fKDMQhhsC7WJKRY68IIjPgkXCEVV52BMQMcDaxnyvdZ-niVYYvjUgQiWhMGftyoHbW0dqPKSwDwo59bIaSjaqc4JhaqLRUZJGDUyXYNArdTfvxYOWT4k-mwFssXGPTCr5U-ifbuf24WaX88sjbN3ySKUEWpnXgoi3CpgPKxS_n3T-OSyYO_KI5zbf0B6isuvBamjQ3M12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=hnZOx0PNQVGz_XsVEZ6IZUMpqu0nNQ-au3pNSsOJcK_HKWSUhDKV11ZXrN2Bf6lDrtZbeOuT83JSxJewyT2wNud9E-zsIzKBLImP5kJgkzXJCz9lLq6nce1JDcuPoNq9aEPAJ54TmE0J6VF_vAyhGDVsj5BAKdjpYFYvJPzxl4IZ53QSpghdtRnjmxym90NAmVr-v-no8vRarVZg6hBqQlv58c_ECA1v0YNuto-bh_CGgfkg1fk5hACZ-MfpGW8EgLTvEguzo_yl5jOl1kFbDx4JQ3a3A-XF-eleIPgQUQgrkdOksNFQYPoAEG2z9kbICjlxbomZAUtFWwzZcJQXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=hnZOx0PNQVGz_XsVEZ6IZUMpqu0nNQ-au3pNSsOJcK_HKWSUhDKV11ZXrN2Bf6lDrtZbeOuT83JSxJewyT2wNud9E-zsIzKBLImP5kJgkzXJCz9lLq6nce1JDcuPoNq9aEPAJ54TmE0J6VF_vAyhGDVsj5BAKdjpYFYvJPzxl4IZ53QSpghdtRnjmxym90NAmVr-v-no8vRarVZg6hBqQlv58c_ECA1v0YNuto-bh_CGgfkg1fk5hACZ-MfpGW8EgLTvEguzo_yl5jOl1kFbDx4JQ3a3A-XF-eleIPgQUQgrkdOksNFQYPoAEG2z9kbICjlxbomZAUtFWwzZcJQXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2D71cYKr5dOhqTKZTKBVDsNpUi7Bo3BUvF2CnM0WCwPsu7870pWbcfGOe71WircWK_QGH_-oCVXPT_XUPIWEK8RKmSUtG9WB6Ig2to081B85ac23riKtSk-MiK_GNi89P-qFwr0JrpRZdt346db3CN_gFjqet60rjr0a89Qahl907apO_RZRVk0UPAct_rihicS0POowKgUTcSJ-2hzdzrOhvVQSNxd14ha9mBjRDtT-x6CmX_BDYE3UyMKztPqvCHd81AT3_9eGdkt2peL46VDxQjPemTj06_ykLrJqS_K-2JmY3358vtahSf6EtdS6FfELkW2XD0LCpOn0dy_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdRWIMqljzX1XNP1wRinrXC_CVnDlZ7WNfBuvK3jFtb-HObTgg-ceSD2EX-dXIikOXGiUtViSgUTquIIt4ZZhMSyJiZOJ_F12uBfB1DemcYXLFo9ks7Y4RQt3fIeRSUQyiaA2Nv_QF74enuFSXywD-L3SkCJUT7OAT4FSW5iJsK1OofJmt4E0_28XpLUiNPWOEPgtRvnM_2sa2Reua9ILOFfcP81pkzstUb1Mt4So4-wQKUrXeOkY8-86OPGcggCgkoRk56fjZeh8EXlOEq8yOBh57PX6piG2uOgdI2PP6kaqP1qU0xwyi1eH6adqC7KdQiKDH9sA1t8V4cSeYa-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_Vw7aIHabJLbuW2FAVUOb62xa9zvOt6kYbxNLBWlZ7xot7Svon_SnTR15IJpHqN9BEyWRpbq-OIv3HDelvRpzfh1NBJVBZPyGvUbd0GB31NCSm0MtBrWmXQ4LzEho3-e5BSHefPXduiBbYK2mbPGgIk-QkUMp_zEZ_P83uGUUzBGpF86797sogxGnhCPhkfnu52MsGR5qNyDlXUhVtpJ-I-UcR68znsYnc2vNBkstnEvqOxG8xMBgqrH24eGLDyMu6FQfoBERxpw-j-rrQOlrYm0lPEnH03zLGlQOnIhf5_JCqWB1pfcBxsOZMOGAocHTXQQ06NQsdHjbEp-0zLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTEMDVRh5ll3yiuBGaSb25to6hiMrs92g7sXVw5GawpN9-nnz-kk-_Ct3qLTMsGmtW5KmccZCFwBxnEiLEUvnNJIsi9ndAEYrtqdIzppVwL4qvwwKwc2Qa1GntnCMrBsHR8VYr03xyosIHHQpK2-pa-O6r6-0VWW00rDEW80qr4KGQtV5kPOACLCXd-zwUkevsjI7tjbnapgsPPurHU9Tit3SqlcFoajL-8af0MENpM0g3T3ByWfrCkE_Jcc1rBMU1L7yKgJ5tuOiTdg9T_TMQUS9sWQTpRls7O5kC5fCBTNkvqDEdk75OlIr1CkaDSlzks19oXkgMk8TgmK4FBADg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAQFn0STWFVlBo-AWEthZ5bWTdvx3Gvvsy6YgVC9usvRgi5OGWrzBFS3TLZwtDA9jMzCjopb9x3G0p_dX5xzVU3vCq86P7wpGu7M163TkypgOfw3y0UkZCESzOmEaF6OzrQUQGcWW-6RTmMf70uDLTjAFUzrohOUUPw_BOcz_l0D5KVia5C99M8QZzxBK4gl7BZBW2pC_z645_MthfeQ9R3q-hPCNstoRx8YuCabAPlhbm7QEu216zqaAiVYFys_zwealnSliLG0Z687v4_0Pyd9XtkIRek-Gq9fYXd4M6B6TYg3DklBQg7VewGB-7kEx0uF_lKPp2fte_TsiKUhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0nTFaUmySJKM8VxciKA1OeT3ydrCNvZoXuaVzWWlfIZPtpr9JfN8IhysctyD5CFIF0NGoRgxB0aeoIpdMXOK_WBx9mw7zoO7tRomcUe69xLLKCmrRrxfWltDc5Ut6EbJUDXf7u508ejiVeSGLcDYOLOVSAuxe7KuUGGjSOINXZwMdj0BoxCdAdbmz4V8hyi5aBXhLbeZWu_S69j6eAS_75-ozWnVwAE7QJ4vIE4fzO8V4WHXLWu0sFMGJiWpVE3THP920p6rZeBoDo5G4aG8hskVwYReBBN3SvbWt4DRwELSv9n9bhPHdhuqcb-4b0ikcBVhSmoSl6ZnvZPcSpB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=WGNp2kZXkG-AfBNLbBuREpoup4CqOksk-KhPtrm_PD3GGVwwhBMAr7-jboHy7YTJ26jByP0HeTgRYFJWN6Lyqa-i5VQn2aBpeVeQz_4-3JCI9VFR8Cnm49JYOxndgC6L3VAPAHWpybQotJWQHw23NyrzTscUmBKEyk7CRTdS-sasLGzLyqTA6WS3XQFsDV58ODH2nlQOmO_hs9EI-bK8UTK5i48AXVNJSaQjsTjHclTvESoS3xWerK312rDN6ug2JG3w97PUiW9n96kpWLWOhey6q6-KmrMpiRlqgFEOWR0_QmZah0kaR4JQy0typcDKZwf6u8mBvi2Gyht4VRTunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=WGNp2kZXkG-AfBNLbBuREpoup4CqOksk-KhPtrm_PD3GGVwwhBMAr7-jboHy7YTJ26jByP0HeTgRYFJWN6Lyqa-i5VQn2aBpeVeQz_4-3JCI9VFR8Cnm49JYOxndgC6L3VAPAHWpybQotJWQHw23NyrzTscUmBKEyk7CRTdS-sasLGzLyqTA6WS3XQFsDV58ODH2nlQOmO_hs9EI-bK8UTK5i48AXVNJSaQjsTjHclTvESoS3xWerK312rDN6ug2JG3w97PUiW9n96kpWLWOhey6q6-KmrMpiRlqgFEOWR0_QmZah0kaR4JQy0typcDKZwf6u8mBvi2Gyht4VRTunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=TktnMPrSMGKtdk6Mu_G9yv83JBYj-mSuShsVjaiBlXPLOgaPqClYBkDDGdCfoOCqOM4x3ybE_WmBKyo1La0xHilqO2Y0jwbAzbNpaL2Vwjawe-y_OXvg262rREav29ZadtdcDRPg2BMKCFCFwv5MyacvKax2eZOGfcncX9uSXvm8qd2Lk09gVvpdRWM8ASORNV1cCp2M_DmyI7EqjkijHRMe8aUrgDV_YkhBOtBiUZ32jq8H5YHeX9ly5PagaFZTr8NG5enrL0azec8kNtxTCocw_M32mgbhLTfKY8Rx2gDBSyFtihcaRLNpqkEABP6cmnrPyfaEs_P42BaTDo0ZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=TktnMPrSMGKtdk6Mu_G9yv83JBYj-mSuShsVjaiBlXPLOgaPqClYBkDDGdCfoOCqOM4x3ybE_WmBKyo1La0xHilqO2Y0jwbAzbNpaL2Vwjawe-y_OXvg262rREav29ZadtdcDRPg2BMKCFCFwv5MyacvKax2eZOGfcncX9uSXvm8qd2Lk09gVvpdRWM8ASORNV1cCp2M_DmyI7EqjkijHRMe8aUrgDV_YkhBOtBiUZ32jq8H5YHeX9ly5PagaFZTr8NG5enrL0azec8kNtxTCocw_M32mgbhLTfKY8Rx2gDBSyFtihcaRLNpqkEABP6cmnrPyfaEs_P42BaTDo0ZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tolxhRmNmUG_DWnaWDPkBpd1K0EoaQT8FAZzCikzVjOnQCHx8ETWLWJboHGhlLmrCt5haxM24GNqe0thFoZnhp4Sn5XxyQDuxswn0Fj1opmHYhYTWBpH3ea5GIyOS4QVU4ACzofRvGV53Q1J7aVd_SRTHSjJf3-xEEJjPv1futi-A9D2LaN3A38sxHWwIOpWgWmOgrTzQ4nbsGfw7gQtpLeXLB5FaWEJzMdIg_Qw3MzUtQKBjNulTe5fSJpV0RGqlj0aj1bUfiEwOvcQOY2ufltn7X0Auczb57dKOlbeCtrsykWvYdHFJCSjVcLhLPOUdDklGpc3RorWVd2vklnX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJTzFvR7AuzoRzgDt_wJRrgrOIKvCREF_TcSZtY8WP-ynB5VTH-RbW_HPGE6t_m8ljGWsBSFbtkl0gqMrfLaRJN1MIDWRBVnYDJdGZZ9V1U5uw7Cz2Jr1ptOWwww2wdyQ_DsZFoQoCtEo6WxnL7kVm50stBBo6t3F1-oXaJ7-cQBma2FyAXiWRdKrXVlUEndVWtQw1YuXQwtQKBL2dWdcNvEoMVfkf-VCwbM-NDAohauSP5EvXAfu_dVmOAM8QCK1hVsWKxGQoweaMk9DdqWHpuw5s6zUMdRdnddq6KbkcWx24pa4p9-Krnx92pxILvPudxb-OIkFFbdNV__NMcnik78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJTzFvR7AuzoRzgDt_wJRrgrOIKvCREF_TcSZtY8WP-ynB5VTH-RbW_HPGE6t_m8ljGWsBSFbtkl0gqMrfLaRJN1MIDWRBVnYDJdGZZ9V1U5uw7Cz2Jr1ptOWwww2wdyQ_DsZFoQoCtEo6WxnL7kVm50stBBo6t3F1-oXaJ7-cQBma2FyAXiWRdKrXVlUEndVWtQw1YuXQwtQKBL2dWdcNvEoMVfkf-VCwbM-NDAohauSP5EvXAfu_dVmOAM8QCK1hVsWKxGQoweaMk9DdqWHpuw5s6zUMdRdnddq6KbkcWx24pa4p9-Krnx92pxILvPudxb-OIkFFbdNV__NMcnik78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTMALZCLX2sZEmxvCJngpoFtH1kcfg0TkjwiQSLj-ESIK4tvcT9J14sY5rhibRNZyAc9uIU2fE6zS5JF2EUH_27Q6fMTD_Dyf6P5pHXR8Jl2iPnCUNWvRT4W3Wl5NCiets0EXoZHgVcgfCtnBGYWf2q48XEFem8uoSWXTwBekT3Td-KaLpLzDaxkK2AodZWVBCfIg9guv_SahS8cGsuK04KxEcmwfs2taU7wMDto4M054TOcg1E6JHLDNoTa_tja7OTaNQtbjaFLvqdQrJe_RkWRGAd6mZEkWPEM2-DSoFS_QuGE-8pDNZYdL0yXet6JVTDCFfaL1G1eOfjAF5xGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIzv0ZCC0ILG3ANcut3On6mmjtN0WaGbSIZQgq0bcYCBjIxdIKp15gjGkTg9KL_vqDZWQIoi1maJQYwWI1I-UwoQ3tYm318JLJIaTNzU-yLfWAleY4KXVC15XRE7cGjuGAmvT-cgznykVvC0KFVDev84Z6HUe6p92CAju5rR24NuIt1eXaP1eyCLlrJ3BL1-5FjBTeNo2wqdnOghGoM6SkPFmsxFe8Gj18tenhvPD5-VI-XZOKUueUIRr7ytYAv8vaN27AlwlMZw6-QAzmBhUnejNPYSnInjKg4jkQMLJ7sNytK_aj2wCGPycF5jPWztAKfLwu_G6uhlDnQ93Ll69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cv3yD4kGtZAx_whScbCnnpYEigbHWpMojruje2P85LC0xkTXQg_7TE-q3PjNKSzIkRKCsZin0eePz2MWvyvvj7xPA-zhp9EScWvDd7hGnKZJAKh2-a80vlvdZQdE1mcmNF1II6LImSXY4fa28lCgfAj8qsqeKN6cbDP5sq4KiVsXbgJzPkDGgIG2nppZx28dp4YrakW3TFZKc76spdWfEPAjSlQnesophzXi3Dxw7GZdvYX7N1fQVTWgrJzwUDYBGI9HhWU-WfsewXZ2cc9XuKg77blS4J8nwZNiKDa9h4ng2CkNgLPerMe6Vsg6RmTNvyym5BpNUqXAasFrkNe2Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=vNkPqCsVT67032T8N7pFuLST0N_eE3lYH1nKSUzH7aGkwW06G4F1OuMF3NL1XzI8ADWrJwk17r9XqeAoyO9ISLEuBdyZ7OZHxb9cU2-pzVeMk1iJZq7ckrIXLmZg0zA1HdUWTM7_NS7u7tAAGjNSzY72w2iDhjI-TVHyT0b4cYXg903vtJqVsMkOGiDRqsq4T7mvdozvwNueXZlqtm7BSqFjX_aYug1PmUHSwNVERDtlKrdd2MUlQk6q3eiciQ-OpJTtv1SiytwbcECLxBWU9QgBLyvYa0OaPHbl23AJ3cw0W9AUEGIoBG2UvmS1vY6tbqR9k-jeUZResyb2Nl6xsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=vNkPqCsVT67032T8N7pFuLST0N_eE3lYH1nKSUzH7aGkwW06G4F1OuMF3NL1XzI8ADWrJwk17r9XqeAoyO9ISLEuBdyZ7OZHxb9cU2-pzVeMk1iJZq7ckrIXLmZg0zA1HdUWTM7_NS7u7tAAGjNSzY72w2iDhjI-TVHyT0b4cYXg903vtJqVsMkOGiDRqsq4T7mvdozvwNueXZlqtm7BSqFjX_aYug1PmUHSwNVERDtlKrdd2MUlQk6q3eiciQ-OpJTtv1SiytwbcECLxBWU9QgBLyvYa0OaPHbl23AJ3cw0W9AUEGIoBG2UvmS1vY6tbqR9k-jeUZResyb2Nl6xsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4Cql2cx1WCZ8YsV3q2jVyG5hYMJL8hcCXRWvqeSMoSlr8Pgs0fYSRiflk-CPsA0nsHnJsMKkGvIAAOzlqUmwvTPpdBkiNLr7HHEp2fVDJEB8SFmegxkS2uh-fBXXpitJWYZCiZWwUy-GfIHUzJtaLT-aHNUXJ5tp-JNWaEmaQ1vKHGyzMyrI4wgYP33E4K1_DxWma_zoKyvkx0HwSjKGR_M6_tDd0SBLs0MZTQfZOhDk8-WSQHLy1-x-9NKAR0S5Z58xmi4wgad5IOhSy23Naq6gALSUjRy-FH2HcGJx6rlXCjnSgIPVZdxSHGv9rj2PvurVPUMgv2CAg2u_uKPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7kSQFa2bM8yZS8ilZQy3Tb_MojeweXye0FbPoGB40uivtbUIM_gGF9_alLT4baDDJ8ramD7ucAS6CTXz1Gj6IK9s20wjQQZ8OB9fQUViG9OMpVX2wNlhU0zA2PuUsc3bQHXEGo4es-Cp-evDTo1quCyIXPF_GLWTC6EVN8ZU68h2pblPaWTLTfDfqin4wwCv5i-wGCG7xhZF60xsSw1GQDv-1nJJAak50C9I5AEQCTVjylacwoIpYelAgi682DG--KR5d84MkMmdaI8nvRUzh5ig048-IrCQodI-o2bFaJfS-UP1-lmtYcivUp5lC01OoFe97t8pUISFDkX47aBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=I0mH8sdTOBObxU4ow_LeiFkBHmoJGeUenXeF2VIQkVKrDye9_9D50JkAN10TbvHder6g4UGmjHW6pr1-3fk6aH7EnwD_v3UYms22TMkjhbkeS4P9T1Qvj-ZqwgteihN-POrMfEsVkWm8z3RgkGWh6m2BiK-FGiLPYy-Wfst4v4OlAu6PWaWXlCTIfXeLqam4-VeszbIgBZJniG3R4FxB6V9qSqp9GWYBpiVPA-gfs17qPbsaEUQzzeitvbsWzXq7DIVZ3UYjKfV3JeCPdK2SbkFhDEo5ESvRJbq2nVFp-aiFl2JupdkbrYfEtGTOmyJhIrHWiLDYaVSXXLVGVLi_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=I0mH8sdTOBObxU4ow_LeiFkBHmoJGeUenXeF2VIQkVKrDye9_9D50JkAN10TbvHder6g4UGmjHW6pr1-3fk6aH7EnwD_v3UYms22TMkjhbkeS4P9T1Qvj-ZqwgteihN-POrMfEsVkWm8z3RgkGWh6m2BiK-FGiLPYy-Wfst4v4OlAu6PWaWXlCTIfXeLqam4-VeszbIgBZJniG3R4FxB6V9qSqp9GWYBpiVPA-gfs17qPbsaEUQzzeitvbsWzXq7DIVZ3UYjKfV3JeCPdK2SbkFhDEo5ESvRJbq2nVFp-aiFl2JupdkbrYfEtGTOmyJhIrHWiLDYaVSXXLVGVLi_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=VxwdWDHZIc6hlRiiLXpKQ5GUd-7FWjDo3-jbWvLaiOP9jX-tIMIONZ19ht2KdpwqH9QymLCq34EC1gqRo_LS8C-iX-YdsQSQkD1luLhXjnguXAaBB4qcuM5xDbRJ-WVed-IX-aAyqXyqrbN7Jcm2brgZKtCHedWSiX_Z8ONrvmyr7a8xOCvnP3_1OiVjUdafPuCdfQJNqO7n1Bq4zS4D9y2oSWjQfidpqM2gnag3gbjvVn_ElloR7WqCRS8Sx5M4ZZbLxtyjSVo3JZ08QRyyKXxFm1lzNQNIfQp9XEsBlQsJFPRBoCSYlNv-lFq0wV19PdaWaKoRi8hlLMH3r45jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=VxwdWDHZIc6hlRiiLXpKQ5GUd-7FWjDo3-jbWvLaiOP9jX-tIMIONZ19ht2KdpwqH9QymLCq34EC1gqRo_LS8C-iX-YdsQSQkD1luLhXjnguXAaBB4qcuM5xDbRJ-WVed-IX-aAyqXyqrbN7Jcm2brgZKtCHedWSiX_Z8ONrvmyr7a8xOCvnP3_1OiVjUdafPuCdfQJNqO7n1Bq4zS4D9y2oSWjQfidpqM2gnag3gbjvVn_ElloR7WqCRS8Sx5M4ZZbLxtyjSVo3JZ08QRyyKXxFm1lzNQNIfQp9XEsBlQsJFPRBoCSYlNv-lFq0wV19PdaWaKoRi8hlLMH3r45jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agMBXUVIgd_t6ZS3pD5eDpeIAjyrwkQE-8fOCJBbdRrH7xZogqYD2PR_na_gAbZmBFS_-3_jY--Yp2yyyH9Xh8Rhf30hCoOByQHXFsZuFzlBrjUAg3z-EQnufrJtfVweEB6IP3CWgO-iBzK1k0RH9sGBugCjuxNpYpFRdvqkgA7oAfW4QSX3XiwUMbpfEwqZrfLM8seQcI72tXPZRybU31vmuxhgpkFpzDS762qa4jZYzed-Kfm-csr14Uz4NBF5muV_H1IzZd2TbmmfucYXfsb8-oyOT9m23B2lneA8xNkrn2xigfALrMtzKoqRQE_sFlCiIhtu13rXqDtcpP8yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqMkXC81_IUtVNDTYtorrmqVBhM2ydUmblw4nfy-NoNTaZO-ve1EVQANbvMWnCduXqBSO6N15-AxLm1iWRXJdvGp0RUbxcMFQX3UMShDmUAHXqv59ZI0utbwBrVA8aSV30vURMGb7PIi7X4t1YDfEAwIs3xehJx2-sq2Yj0GygF45VeoaW39rMiRA-n8q3CsqLhDSIS6HDeGMachP2VKTF2wpVJUr8voBuSGG4qFGgKZgRXehZz1Rog-W4pC28QlLMPKY3PnS_wttAJBmaoDW9h24JGi7prrcncIGiggU9jcucFo1L9HGI4btwOaO0QzJn0nmZhBG707sLwTlMbA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSxyhLVagGD_THy1lBTXYzfN0xHyVn5LVZiK1ld5jDRPRhhTNq0CNyJv3sWL4Je4n2Ss75BTZZTlWRT5u_JKGiz6dzrHJZAv1mhuynz0jPb-bNZPD0yQ5K-N7FI61FXl5GCLnjOIaARCj9A9uWwNQo94uJFMkEptDD4oKsOW0fOkSb9_OKSuG-bdrMZv8XLNii_Dc0guOmSnEaFm2CZZ_jgVH6w-qdc_XHXxpGZklAKWMbwqHrfDmIo7zmaKif530TY8Ky5sH2wt_SYZnsbDoo5wFlHvtuAoHmEYO2rM61qnysRvxGE7AvXBsEQaehkRXFl4XTDdUHnOw3i-SxVc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXvZfzas85SEcBt5u43TOL0g64srKOmiqc_PyUMNE8Bm-ZhhlMqNY4VmpBKUitf7drK9oOQWwZLfEL8Pe40Gs4fxPon6xm6S8yrON_4O3wWZHIq2zRV1RGfCzcYsLBh2hMxM_2Dyj8jI4BSCJ0jNUab8w6kuvUQ6rcYJOpuCrvjsm_itI3VpY0BHEX4c_lsdvUJRGEa820FPiwY-2xAsLWR5zhr2-3LtdocpvJhizDI1bgZivuWm-FrKNloFcoPcP-0itF_lswUCXUFtbo0woWZ_a75DYGiZH3W_qErPyePOowzwnodHGkgK4AijqCAB-8-N6MnbIzRWLuAdlNItwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRNhOW92eDg3a67EmZy2gfKU7-DLkDhJ7g2vVNyzIiLjEXV1gkBP-kbiZjxxfgAid3S4pPuj0fTsUk3jwcvltzLwtQAHhO4VDv1v0c203vdgqoEjUrSRvSm8C3gpDtA7z6kNuG_PPwqesR3dsvLZB514NoY32GiTeniC9U8_9DznBQMtfcwy4tYejD5f3dMo2TZDcGveHA-vwuRonn8IOW3BGEGL_s3CmHCgqNGsNIo48tXWbzL1JdfFsVBlkDmXTk3XL0OvmNOnp3IplT50ds31l6fzzVxRrMX41dUZO6lei_ps7NMMsTK_geKF4cOrEaoAxy2jjaKUEQZc_opdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=NY0sO_up9_gva6dbvO3MgK1JZetTntcbvInrHfNcNEAet8KIdpE5BvLFAA1V6EPLRSCQXQ-yo9bhPhYT7anfJF3joTbWWksb4wCJR7BpuuCQ1KnS7_essznvSIXBnjZ2nSYrNWZljcZwCbDu4LsO-TAfRFPuDCQnxbPqyvbd14lnsnVt1BfgcWgVUp4acxK60bDLnmVLToTPrIxhD0aYwvtdalWAsB9gz_sYmq2dhJHDyc301FKZI58fvO83UrsLM_RccQ1sH2vEW3phxKB6bVCTw3gr1PlP9Yzv3qvurY1ut1ivqYywa8RqzsfHs4KiYAVNqP4TWwlLIOMzdYjKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=NY0sO_up9_gva6dbvO3MgK1JZetTntcbvInrHfNcNEAet8KIdpE5BvLFAA1V6EPLRSCQXQ-yo9bhPhYT7anfJF3joTbWWksb4wCJR7BpuuCQ1KnS7_essznvSIXBnjZ2nSYrNWZljcZwCbDu4LsO-TAfRFPuDCQnxbPqyvbd14lnsnVt1BfgcWgVUp4acxK60bDLnmVLToTPrIxhD0aYwvtdalWAsB9gz_sYmq2dhJHDyc301FKZI58fvO83UrsLM_RccQ1sH2vEW3phxKB6bVCTw3gr1PlP9Yzv3qvurY1ut1ivqYywa8RqzsfHs4KiYAVNqP4TWwlLIOMzdYjKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJsVdruyTCMGWZ0ZfSGdaJfYDQbNo44ngkD3IMhQd6H5ZYhX2bdGEn4Ay8RvPX0boM_DOd3zqMUaojCtCStxM96rqfyIts1nOw0QMJapiW-L2butry7XocwnX9kaYCVNqjwH4q_574in05dZUS04asVEp-lPQQBbkqx0hxgpNHFpJWoT9GvE8b1jI3A4j4oGw5-emqsQGI62M6JfXdW7RyHmbwbbVxEF7RIKMRJX5j6XEBhO_QuTfnVAYp96w3fjMLzL9hcshGiyNwgXexA_a8AUuQypbWulVkyG5J6t1BKFc5vuz9RJGFW211qezxnEVUVrE1mIudlRhFbJaY9EiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT-OXQEDfcx2moEcsAICN0M0Fx7fXWHlRelAWmHeWuTWmC8IYj6HzE0pIYnhxyNDawbWwg5ngyrufFkflzFojzd9r5AO0yAcxlxt4c7sYTKw6CxkJCKWka_fEYbpZFeukAlaCJi4EE8_O38m_qdVFSk3bVpRcgDMI1fKbqC5nApzKyvsrUaoxbumce6csrtMGAID1S-z2mfrZQaNlEPwRm2g7PywXqbZDtFQJ2CyizmKMAeISkzd_Rf1BedUyX3ickG10-Tqdn5pNf9uziqvygOm_J0oswyFyO6TJo28NAJvk8arQ9RFgBjSztp1rDO4ObXNvq82OZpWt8ONlFBxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJbjSKcY-XIrKntDCCKUxtA_DX6AD_Azk3qi4nnsMcrBdwxUeHSXaeExfWvb1hi9UybF6w8HwU6vaLKOKngfXT47zIN5sif02f71D1A2S6VTj_nLge0hewWVBMSp9NZOm5R6Xv-wnYCLkDSMvBfiaM8Z4dPzRTAbaay8JX_9kwgACGr7G90YkzIdfkwy6k9jqUxPKwt4njl7EUBV3tC_Y0ngmHXy1Ehy4FHEKZMWfCzAMmvnsD3rUxqFEMZ_w58uq39qr7w6KvBUEPJ5pEPzi3IY1LwB4Em9n-BlIu6SWG3ZrTQ6y_ExvndyUUgnYx-NHIa8ohTljVdpcV7lt5I9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4FfQIeb3_Ro3k1q74JTzyrz5GB_bc-cnOTwk_UEr8NWordspBdvKqzTec1S_q5vWhRPNv5Qif7R-TL-2BcEVGk1PY6zt28F3HlI_G897Nnm6w84gx8XQa7c15e7AFymNLrZXV4NA-1QVnKe1T3Isr-7uDzF_rdHZlmWWyCEPBa0SjFWdfjB7Ud-CvZ0tTK0-hCN1_Ke-blSAXh27U3RQfUKl6nElZNkAPfl45q6Nu5WThAo-TXDXGrA4uInEINXcl7qQKO3V-9iCiT81eNpu7FWOLaX_wLB5XCBmxMkLk6QqBAPhbPLQJsyCa-FpfDzyTJiOwwCH13gQOzl6NbGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30604" target="_blank">📅 12:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDEVmfVNDOig1tzjFo4jEoH8-uS_Uh-XmafQhRfdsvf_a3Now9icl7FYbkzWPQrHAMP5cwBY8HJx6_I9uqtkEZdnmRHyKu8YpuIdEn6lXgL5RPb6xbQAH09r1KkkbwyJfsNG3UAukRr1c4odTOJ39BLCGQ2KKpJAXXuzzysTMOviLjZ4UgiO6Xp2ip-3_VbheYFaxW-iwZ6yF_ddX2RoZ90f6n985fTlOapet2oVRiKBapDEMAbmnkjGPR41GBc26hDNajAPFY37PEwGCuAR9vlL6qpzS5qBGp3qIGc4Ae1VZX-p5HdQZpk9r1DRkbrfGlmGpcg_3N0CcftGQJPW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy_afn_Q6Jp-AJOFOLHR3NRldTOU5QUKqzEirZE_OczFLPsglSw188n4IGMK7dlt-UlHIOQIPfRNvV4PEE0TnMG-hiV7nydjKJfbagPsB1lbB_jVzkb_Kqzylx_ZKQ4rEzZWAi1HSCJbFtMmMoe1HbZR-u7X2PkPmcdX86ZtN77m7JzJgVI8sojked7GiRPb-rkQkjDwbYXEtTic5LRjRlnheOSHM7Pt5zFi7TkgcXpPBAanvgPPvIAPpO6vF98g-uXYByDmFUhnYBwSbKcwpI_fhTMllZrVl_uCa_9vtIKoQQVxFLMDsROnJcyK6YWeBzaYoS9Tk4Gvg8Y7AUHpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfbfBCMXudxwjGwPknN1-Y_D12IubIvkdb9aHdHKsW8F1AefeJUZX-yLQD7Xmi07fMjPmR7zM1n0Uwtve8uU1OargsNf7KRaKjVPyvbT7i0gK7_qt489UYETyU9vDrXzRX-Dmk0ct8nXQm8z0wRYltw3r5NN7uH94BMo3YHuMhYMz79bZijBmjdLSkcP2A0mFpIbSnoJzBNEZQuHkB-n2VVnyMjn185oB8Mng2nCk3NfFlN3k1ZvCLzjUQNJVd3Ra7-L6YAd2hrnkNxi0ULBU8k8qIn4EyQNcBH47y4W_ut92vr22kI2J1-aweQOiNr5CGj2_CY6QEw0fUebA1HM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-sPVPYlIPbWlvqFB35fwYxvI1o0j33iMeWZUfWAOZbiPzO3wtbgHqTf7b8gFFIDicTJduZIO1TDuwVXviqfZEPJgJ_jLfTdv7xnIqK9bzFaH6Gf9Kh3IMjHLaw1LOXlKNDGwOlxiWpPJi4foPxjhPoT8Ru4e25NwRS87niLjJtRJCLFQzHeFWR8PJ5mwW46DfJLyVKvnhdQmb1JvjQrn2blP1q_gvzuPoZZSfKVAC0BFIFLjL1QAvzCoRSjn0wza31p4Ao_2AEV23PezKpxtkR9Df3rKkxsPGTIGBRSJiTS2um7Uc1vHG0MhOOjEb9ueZAZjIQcTdulCnvrdFIN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpQC951uJWDSxrt4amrOuw4wVuI3HRDIksLAkEX5wUCqqHbjKoX5zeQwc1fGHk6sAmzjmvQtN1GRAyINFTuPQH1DgkY3j58sj-ViuPys1BBRFYPq0S7UZv4denx2VRf16UgC9UFoGoOU3Mpn2cDD6w8egO4Zgkx0SL9900l6z6_lNBEb4d7U4YlwLoUEhSjBO5fYd9zUtJQ1DcIs6QsymbhpKMjG3oBi8r5IUhvJXzIsRukdNIB2cLaWo2xx0n3UkSomy7a8J32GgL_8Mc6s1-QXKx8c_WtuYWc2CNHGQRVQ5bYLy51brjoMTSTQ2_evoy0wjeYl7vROKpIKuWhyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
r6
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU_xX8niF1bsDRTT-15rpAausUaEBj8fbtzy6HaVzPypAJg4UTegyuT-YRc48Ff8UtuG1kwVANTIA-8xqHkmAlQGASuhgecuIMDqd4fQQQT3av8XNvQJSySmKOvglmOzPX0KTrkSvlxHyu8wi46CfOvWjGybY7Jp3AeKG-sKmZqeh6qPl117WcY8_dAlUMaAwx6BpTaRLnkk5hje9WoGJ69jhPsIYbAd8C3EGfKsPNnhN7fjCnkTut1BCJlGK4TAooUzSSSwqUQhKskxS_ewxdCNnJCTwX3rrzGkH-7TPOr-JEzsUiRbgKcMOQJgqein1wXw89qBgP9Riwk4e46u2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYx3bF7WmSCa40h1awsN7zLExG2pLpmAWZ2pOMh6skiFaA6f_EC4mQDPWksiiTp1fuEk3YzzEoLhJgSvK7Y4e-HDnZ_hs21b0fBS_Nk4zodMHFXZod9rUn69X9C55J0hkXxnSqE-Kfh5nK3g2r0ISU1Y9uK7ZrGEzTzYp_nPinajUpwo_KondpEy1jMFxB9BMKQlgY8PVaeBqhYiXX0bRbzu2-vzYkj0FsIjdRbDcSREcZzuivkMrmC8aLXkOCoa-uyLF9w829inHFZD6GhjhwigHDbehx48n9nkUbKOgCsEE-lmmW0h5MpmlYxmUEOr9s9KEFT91Wkd7uAGyJnrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-T7SipFnJ9M9sa0BX408xlX1hxbxFdiCZgnvKnqNyzDZnv-xIMiV6AZ3A9lJqIA98NV52ej5QY_UhCrxBBUIfCte9zgNkemUsfjnwGOO2ACQE2d7SVzFuwi5LD7Z6DD1IgakqzPEhlCtIeCUDUzjOVbqv3wkfTf4Hsbr58IKd3DDBqDfb587QwTepI96-FbSM6qmBE1CcKt_N6PI8AH_Nn5fbSeMNFYpH7eiWL4UKoHYRj97Yxvd8ZXVDJZofaCaYDf7Qe3rbPn5nUtzO7lE3-Ug3LVjG4y39tsjYnDZlO1lshDkmbJ0Dp4Pnck4c4-m3wtdwDCfY3GSzS7cMu_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=fRBMgshJzot7ixzBcQy-icfO6ATmssLARj8oOM_U_AidSt1wv-hnDLK8onb6i6YSLSxZQGUBW-UzVguWJcHEjQw2vhm_A5ANNhThmzJbilnS5yCB2ORNiBH1XZLL6NAycBPRBXkebl7SEooYBAiW7Kbu0LbKg7DvLPutjD4IF24mVYMk6tGjj80L2BOm0FLAA0tKcUnn9buF2c937Ts8H7zJlqoxcMIeTHW3elByeEyvogc6w8ew4AJbJSQJpUzXmka0pbNQQlgMx29T1ZVc1MAu3BcZ9QilbmpQ7hs1lPzMca_SL-QEwyZ2kv_RIZDR1yZPlhQBrGBCwtS2Z4AmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=fRBMgshJzot7ixzBcQy-icfO6ATmssLARj8oOM_U_AidSt1wv-hnDLK8onb6i6YSLSxZQGUBW-UzVguWJcHEjQw2vhm_A5ANNhThmzJbilnS5yCB2ORNiBH1XZLL6NAycBPRBXkebl7SEooYBAiW7Kbu0LbKg7DvLPutjD4IF24mVYMk6tGjj80L2BOm0FLAA0tKcUnn9buF2c937Ts8H7zJlqoxcMIeTHW3elByeEyvogc6w8ew4AJbJSQJpUzXmka0pbNQQlgMx29T1ZVc1MAu3BcZ9QilbmpQ7hs1lPzMca_SL-QEwyZ2kv_RIZDR1yZPlhQBrGBCwtS2Z4AmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
