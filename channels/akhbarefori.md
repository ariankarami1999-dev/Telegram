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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-668928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a547a39aa3.mp4?token=JTljLKvEHEF_Xf8KVncNwWIqguGEstB6a2smIXSrXyKZPGSoM9vTYg6U2N7ReD7fT1rg1Rtd9WwNcHxVoZRyVQJ77xfMgi8wumCIujSX8QHc-53BtrYhBNd4KjsocWI0nwKx8JF6-xSL66dUXlUPYQHhCcItlXJ5sY5wgwECBDCZziJr900WnwoixWYtRslc1JgS1kbL_NzmkYk89sJkyqp-J0ujgx1UsKenJexdinHeHCahjHS6VE5utXA3SkeN7fmFwte0Iv-W2zgUz-PQSHNMBl738Nw3Q2--3-XGbWVjhtnrgVPoicIHZDqNULGgh0CIxGrdoEA0XP3ojYTvIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a547a39aa3.mp4?token=JTljLKvEHEF_Xf8KVncNwWIqguGEstB6a2smIXSrXyKZPGSoM9vTYg6U2N7ReD7fT1rg1Rtd9WwNcHxVoZRyVQJ77xfMgi8wumCIujSX8QHc-53BtrYhBNd4KjsocWI0nwKx8JF6-xSL66dUXlUPYQHhCcItlXJ5sY5wgwECBDCZziJr900WnwoixWYtRslc1JgS1kbL_NzmkYk89sJkyqp-J0ujgx1UsKenJexdinHeHCahjHS6VE5utXA3SkeN7fmFwte0Iv-W2zgUz-PQSHNMBl738Nw3Q2--3-XGbWVjhtnrgVPoicIHZDqNULGgh0CIxGrdoEA0XP3ojYTvIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر پاکستانی: آقا فقط برای ایران نبود بلکه جهانی بود
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/668928" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031e2575f2.mp4?token=b3eP-4RqlsynqAeCvatSocDEIrVzGWvoYdE4uL1af7yrYh1Z4miGuJ414MCwRwmToJQuZZeoDrMoWde6B9ffv3cGTd-09esdplaoh09MH4-O7j3OIgd2OXFZ_UT8tVQQoX_pjWgioPkRM6bcEFq-NxDiuG2I01aqctjJTOFb__CKfprgU0ttauOz7Ok1p60Dz-iGBDCi6vz5ZH1B_hBgDw7l1v0q_xdYrfKqPA6dbkzNMmVrkVixAT8z5chNI1OtO8SInl7rJpVvIL7uMtgixZHRhZ-Uk8ZtFx6LiJMRkTQDKv6TaSCmlPgWwH5Zsv5x_r0A86OM1b4XOT7GWNZdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031e2575f2.mp4?token=b3eP-4RqlsynqAeCvatSocDEIrVzGWvoYdE4uL1af7yrYh1Z4miGuJ414MCwRwmToJQuZZeoDrMoWde6B9ffv3cGTd-09esdplaoh09MH4-O7j3OIgd2OXFZ_UT8tVQQoX_pjWgioPkRM6bcEFq-NxDiuG2I01aqctjJTOFb__CKfprgU0ttauOz7Ok1p60Dz-iGBDCi6vz5ZH1B_hBgDw7l1v0q_xdYrfKqPA6dbkzNMmVrkVixAT8z5chNI1OtO8SInl7rJpVvIL7uMtgixZHRhZ-Uk8ZtFx6LiJMRkTQDKv6TaSCmlPgWwH5Zsv5x_r0A86OM1b4XOT7GWNZdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچه‌های پر اشک و اندوه شهر در انتظار وداع با رهبر شهید آزادگان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/668922" target="_blank">📅 12:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udd8hVfemCKUDdeb8ICEZMV96ep2ci4ezqDzu1OCWxhpjkuZ3529nHEaVN8jLfH4TBHvV_bE9H8n85Vq0wzkcxpJang1Ogb9j2tdIIebN86kUsV55s4U1FwbKSudk2GDwc2_RcxcZPv4qPiImjQeoSVTaWMRhK0wS8v8XBEE9Oc94bGOnovapiIgFf7bONOR_9ZNFjQyhoA27erwqjMZty0HI4HA_7VreIrt0n9NXcm8H5iuxZg4DNgXgH11-wIgPRXGne0e96PSyUM7-ESiccNm9wQ51Mm5TR5qMpv4eRXJGAAYH6PxkNGJcf_O7CyzMBL9svUSfrry3JdubXUXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/668921" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAfn34cXn2_7sdP3bmatsQS2XRtBnlwQNv07g9A3ZYtqA5AFtRvsyy2NJY5if60-BIRYv2ncnHkZanO3lSPHVyR9ryZjMXhBVYKp_zuNaCIwkwHmDdnl7MQSOsHFReCDR39EGzmY7zPh3KTVcl9fMV7OQ0Mv_gtdTOEIDJJspi0oikvI4tg83rqPqZoh8093Ifdfw3ohl0ks19YP8y4IJAkmeIS9Gva7x_KtVt_9gHG41ibflw_bkXOZZj4IJ54ND2ExZASas3npVlXWI67H5Yr8mUxfAajDizZrBIgpcqeZyqVnRGY5nVjGOntCiwYBJ4NIqjzPtdcS3hsCl-J5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-O7Pus0zLIEExGLZd9EmBD4hU_5AveanRJNcFoFM1gLFO0r0VX0fQfgpcrr2it3u_qjUPCqtc-JkHsmGqND4gnQtUVlUP1mSknQCHB-vpngBNfl3v4G7lX_KVTusEhS1_dLLUKgMbsVAR19SKNjt1A_Rp3YFZvXVyG4gtSsnHnH1PnSnjDyKOUaRvz1kN2UlEpP85pX5_Rxf4Ef-noHEJ1dgtKfGfVehlSFfokwnIWu9njD7USsHlkepFaNB34l3nWXCVZRiUkrrnE_iFwOgIPjhxVM0acGfYfkjaVCHwnYloqz5pqBrdV6p5q-cuYtxSCJF6491iwUbGY_sAgVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnIz8vp8jKKkJU4krufUqR_Svsf47oDUjoUY4qS0ukYX03SfcB8L17cHwgoY0IX9eVjKIld-6ehhoC8WemNToNxB8TOZH0UiNU1miGr9l5DadA3xtkoFrgNgte1_8PNeaM2AjF8__PgjGNh2c0L7IhQIdVJi7ZFE7pWVOOCYE0Ku0wwDLbn2rnIas8sUrDI5A8Bl2AABmZsHi9kNeubkeDqr-XixlfamcZQVNhshYpHCLJGXvHPdFztBDigW3DiCfAT_NAVMltPbBj85DlkI5WOwQPDwoSIBSKzDwICa-UUlSAMwZLSFBmnJhMwxLoe470ukpHZZZiBlo3MFT0xo6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cb8e8b1b.mp4?token=fXUR7SuYJxdv74VPaitoZOXmRCOJKVudbXtj2UFQz23GDjyhtBz7xTu8nU2GBfkYohJbPSut_8yiChGSqy6tCTWa4-GjymZGWUWgDdD6gy1ItVYRxyM9ON6mfqMFXJE10Ilv_Rhvu8K0743i_mQg_ILuTcKf08e6ArwyRtfHD-V0IJXNGtTtxAISifwQE8DvJeEyEveH7hssgphfQlDr4zz-vniqph-wkqPROG5GALJb60b9a4H6xTl0vExnnFFKFMRaoIcIdc2gGm7mqLtpRehlylLkLtHeWXq4f0HiA9L7LwaTkBBN0TJssXrGSN_v1TYKzMg2GUogKHcrAPKdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cb8e8b1b.mp4?token=fXUR7SuYJxdv74VPaitoZOXmRCOJKVudbXtj2UFQz23GDjyhtBz7xTu8nU2GBfkYohJbPSut_8yiChGSqy6tCTWa4-GjymZGWUWgDdD6gy1ItVYRxyM9ON6mfqMFXJE10Ilv_Rhvu8K0743i_mQg_ILuTcKf08e6ArwyRtfHD-V0IJXNGtTtxAISifwQE8DvJeEyEveH7hssgphfQlDr4zz-vniqph-wkqPROG5GALJb60b9a4H6xTl0vExnnFFKFMRaoIcIdc2gGm7mqLtpRehlylLkLtHeWXq4f0HiA9L7LwaTkBBN0TJssXrGSN_v1TYKzMg2GUogKHcrAPKdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشهد با پرچم‌های خونخواهی زائران تشییع رهبر شهید سرخ‌‌پوش می‌شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/668915" target="_blank">📅 12:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=imfI_smVaCBvvrGzvvZY9DaU4qOpenEZAl9YvtkQ6P_wzb74bOqwWYHHG3woTpcKt0R7O401hXhgELPOtfRc5Y5ZplDXb9LEtWBdWWAQiyMcBETslHWaVLsfGEPvDBkZiXh4wS-jmwsKtSVk_Pw1vnnt_QLn0aS_Ue2tDrMY0aD7v5ropondlVBEeiDfC34CnYfUVooc3iNx-uxNhDIuHA3dq8p19pek8SL26CsL5VrTp5KnosZtwpo76j-Czj35vctpsCe-VkQERUlS7zgGOrOK-gKJfdwenkO1eE2TtdxTPgHqpq43FQEMjZGUY04Ghw5qiKYrQr3oatQmuADjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=imfI_smVaCBvvrGzvvZY9DaU4qOpenEZAl9YvtkQ6P_wzb74bOqwWYHHG3woTpcKt0R7O401hXhgELPOtfRc5Y5ZplDXb9LEtWBdWWAQiyMcBETslHWaVLsfGEPvDBkZiXh4wS-jmwsKtSVk_Pw1vnnt_QLn0aS_Ue2tDrMY0aD7v5ropondlVBEeiDfC34CnYfUVooc3iNx-uxNhDIuHA3dq8p19pek8SL26CsL5VrTp5KnosZtwpo76j-Czj35vctpsCe-VkQERUlS7zgGOrOK-gKJfdwenkO1eE2TtdxTPgHqpq43FQEMjZGUY04Ghw5qiKYrQr3oatQmuADjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/668914" target="_blank">📅 12:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
فرماندار بوشهر: حمله به نیروگاه اتمی و جزیره خارک صحت ندارد
فرماندار بوشهر:
🔹
در ادامه نقض آتش‌بس از سوی دشمن آمریکایی، شامگاه گذشته چند نقطه در شهرستان بوشهر هدف حمله قرار گرفت.
🔹
این حملات هیچ‌گونه تلفات انسانی در پی نداشت.
🔹
شایعات منتشرشده درباره حمله به نیروگاه اتمی بوشهر و جزیره خارک صحت ندارد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/668913" target="_blank">📅 12:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668909">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wpgc2rwZI544dc5IVWNB-9E-TbovLJKDWaKiGoTdRsgbeh6S9IzlNInm7blY2VlWQbMPNSh4xThzCXhkYlcSIZywJTFANFpF_UzPIVkCbD6Eh7HV8NTdDsjesd2-YBoXtq0II_TZ9TMzNLZn1OhUT4zlQB8oPa2u8Lm9oDfCzNq6Fw1XAMA_epj6gN6aCHTYPd1nViAk1LjHWxy_uHls1eszuFQ-ASzspgm87ah12RUaVlR50Y6k2eT9DpgAqrQ34srQ4aa0-ENqKSW8nBjwY5pjozM2ci82a9CY51ctK2JJGGjHa4eoP8s2qQiAHBzTKWcwF-3xHZ_EtCWAQ73ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-xn9eBny19oZ4CNDe13WRMz1L01vuvyzf3e2N6xWEIGx18tLoVnWSDAEm6QgUjzgeJuhJ944v0MuE7tTACg2kegqLLJPe-hApRppZDblrTGbHb_-ZdvNy9FLcdssLe7a1JcHwZKXSr4LPuJM0Wb4l45J1g8aZmijfCDs7Xc-dPtRnejeAkA7D3T4BqjSGK2L40jFBHBv_hgGEiwOt4G3c6ZFgb5Xhz2_2S5bqKAmrJ3yUxjmDW5E4R7a9zYDIODJbIGW7u6x63Lj5yKW46f0VF7bhs-ehnAIz3b4rNCJ8mGnblwx5KzLGtOAp1K7urOPzx-GSbEkebIN_MMyYnzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZNqF9WdmA1J-8dGV43tdFnpU0v9xjXA3-bzGpmgtWVn9_AjvmdA3XpdOVhi-paMWSHZZC8F8zSoNyItfsLceWrJWMASVA95vk7o4S9hyEfdVEaSvH6S7Y59cm8RTXf9IXin0atVH0ySezfxAGnWwtotOy9bxeN56-5XbapppOd-NaQfHKs6sIIWI9xBu4bXFSjHUi1NZ5uDaCsSeIR__2yofuPYTkCJ1yAR47mA71nc4sogNY_NKoiyDQU1Gs1r0NWVXOiedDMR-bffqyph829uX-ToRiDx6IJRoa0dKOcaCP0b628n4Pmx741qygSb3lhbZ_Roa6RBxelPzIdMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psb2Jol2tM5g1NCVMzbAj40th1I4cR-3jn9cV3iXI2yMoK3t7yqoTB9qOlHdKr4do1yD6zPYm9QAKqjnITGBhJffUas3eMTJkC16mipujObtWBCnHNWes9EcfzitAdIaIQHthJClxaK0P-CwVt2Q25a7RLTvzbTMuw-l11LVVTyx3dmpV1Ha3XfuGfnpfBsOyFusM0nlowTIkopCX6pNYzI1VhApH2CJqmEWD_u7-QjV1eWtPDPDbH_4nNqZzHq_ttHNk38vuhpAsu4_VOFlVOmu-3v7Q4snM5eDTMx0ggDXXF8Ztd7dQpO8A_DWPXrcFBIkoKLtu1sU0AXMDRAmYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامه نماز ظهر و عصر منتظرین امام شهید در خیابان‌های مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/668909" target="_blank">📅 12:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668908">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43fb1c4e7.mp4?token=JEvZ_GrFB4DfSaQHOd-MoPraHGPx27VNdL9u6Dc_qOeXEMFfHG5fKgin3zfhwA2d4yi2TXzKbuYt6aKxjIyztqndilqB_-dK3XZZcGAX3CuoKSFq72qfAXvcOWd9zy1mEeExUe6VhPsETxA3oNgWSfTDLB7yhdueHGETApGWlhfOYFzTwXs043IY9CBZScZefVSSVx73nsgvR0AH26mdCTcdG7mXZRAOEIHB0shXT9uCMtcd9-axWh31YLf4r__ucAQo9s3Ss4Ogg2pqImj5of5LzmzbZfb_6M42qD6sd4BEY4l4mcERKHELCwJ7gq6vp9DFe63RlrIQOHvZaI_MUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43fb1c4e7.mp4?token=JEvZ_GrFB4DfSaQHOd-MoPraHGPx27VNdL9u6Dc_qOeXEMFfHG5fKgin3zfhwA2d4yi2TXzKbuYt6aKxjIyztqndilqB_-dK3XZZcGAX3CuoKSFq72qfAXvcOWd9zy1mEeExUe6VhPsETxA3oNgWSfTDLB7yhdueHGETApGWlhfOYFzTwXs043IY9CBZScZefVSSVx73nsgvR0AH26mdCTcdG7mXZRAOEIHB0shXT9uCMtcd9-axWh31YLf4r__ucAQo9s3Ss4Ogg2pqImj5of5LzmzbZfb_6M42qD6sd4BEY4l4mcERKHELCwJ7gq6vp9DFe63RlrIQOHvZaI_MUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انتظار رهبر
آزادی‌خواهان جهان
🔹
حضور گستردۀ مردم عزادار امام شهید اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668908" target="_blank">📅 12:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e5f784f8.mp4?token=ggHi0mYJE3scBaUEGM_5cMLBtIR_LbtLgQNWs38v1qkO8RlCGbjSeNKWRnXs0ZBpGQOQjJOePXFaFPtnnHiaO3v94QCbfE3iqNdeGmanelE8Kx8osD32AafPFwebuX13aIoF3VOosgHLB4XnJpoRHeUxFSH4ioxdZarQ6uPflXNBUaLL_QKUFGBqiK2kV0zjiCp-SSEIBTB3WtMpX-hiY3Hh6THIEoCX7V9wdRIMFYY6wSG8SB2GtqqKM8TboQrsZjIHem9AhXFcCXDyl-LlsKGvQh1QDLflavrMBa8EgyPv8Mhu6lInZGXtT6SsxscapyUbNbFg5VlJCWdRNLhyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e5f784f8.mp4?token=ggHi0mYJE3scBaUEGM_5cMLBtIR_LbtLgQNWs38v1qkO8RlCGbjSeNKWRnXs0ZBpGQOQjJOePXFaFPtnnHiaO3v94QCbfE3iqNdeGmanelE8Kx8osD32AafPFwebuX13aIoF3VOosgHLB4XnJpoRHeUxFSH4ioxdZarQ6uPflXNBUaLL_QKUFGBqiK2kV0zjiCp-SSEIBTB3WtMpX-hiY3Hh6THIEoCX7V9wdRIMFYY6wSG8SB2GtqqKM8TboQrsZjIHem9AhXFcCXDyl-LlsKGvQh1QDLflavrMBa8EgyPv8Mhu6lInZGXtT6SsxscapyUbNbFg5VlJCWdRNLhyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظهوریان، نماینده مجلس: نابودی اسرائیل و آمریکا و خروج آمریکا از منطقه جزو اهداف آرمانی نظام است؛ اما قصاص آمرین و عامدین در پروژه‌ها دستور کار نظام قرار دارد/ خبرفوری
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668907" target="_blank">📅 11:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f36ee3ed.mp4?token=hCxXVIoyqQ8dXWlId_HRr-4Vz03SJyU3AeX3K5C5tmrRMPvmIKvxXS-3R4S_W0OZKpBx1yrWFlVjWqe6eTtYoC2RoE_DNIHVKxGDcSiOpj67u--YsUwbPm1u3-BOKJb606tduUNPp_sTnJY8jTxd8JFwnVA6HS-QeSFlIb7_8jQNCskb57IqEWEW3GzP8E_FiU4uy18iboe-z56e3tjK42f-Gv1C5QDxeXUmON8Ja0W4WlfCYxpS29EHnn1nt-FjjrlfxhVC7qrqIfOOlHBlAp14qShTE6Ac12biFPiAb9Doerd_sCS2PgE42JwyPC16kOs7ll5a2LBzKW7TxUiAEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f36ee3ed.mp4?token=hCxXVIoyqQ8dXWlId_HRr-4Vz03SJyU3AeX3K5C5tmrRMPvmIKvxXS-3R4S_W0OZKpBx1yrWFlVjWqe6eTtYoC2RoE_DNIHVKxGDcSiOpj67u--YsUwbPm1u3-BOKJb606tduUNPp_sTnJY8jTxd8JFwnVA6HS-QeSFlIb7_8jQNCskb57IqEWEW3GzP8E_FiU4uy18iboe-z56e3tjK42f-Gv1C5QDxeXUmON8Ja0W4WlfCYxpS29EHnn1nt-FjjrlfxhVC7qrqIfOOlHBlAp14qShTE6Ac12biFPiAb9Doerd_sCS2PgE42JwyPC16kOs7ll5a2LBzKW7TxUiAEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادعادل: محبوبیت رهبر شهید انقلاب فراتر از مرزهای ایران است
،
حضور مردم عراق پیام روشنی برای دوستان و دشمنان انقلاب داشت
/ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668906" target="_blank">📅 11:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c262c988.mp4?token=cUjD7Bvh0jMYoZ50eU4bvsC9G49JSTbebg7YK0lv4MYpAfZaz1ivNOXI_vIuuoRIJKEv_0CwlSDxZF7nWn5YmlAhf23SEPcdqSVFeYPYtfROSrPWkzARBqVEzA0K3gCaL_sTeQOf-gD6Dhj14GDpK7b-hi4c_0colSoEB6o00tKAT1yBnnyUR2cIhFsDyYZCnaTf7PayM7fsuREdelHd6mQBGt8wQ38vqKlXwU_WW7TRaBW8JW5NEEfQZ1YPljjSffRNzqQl3MvB21L3BJ-w_vzs8MnHzvSM359GhQINiwmuSHyxCx92fE6TQsCKhQIUyN6s4D1s4lAW7osucMUdh2xYGPOLv2ciOjX2gS2UDU2sDUyrqUcQBrKhFFgp4c-_EMaxiwR_8fXgpDwChg9YXFXgEdrRhtAP9ZVJ1WQ9yrNSvdv93894Q-hiVdIWdbkC01z3ARAnFjb8eIRWtMLq_vPufqyMkhGpcpsbkONOYpyN7gm4-2zrvfi4G7bAwxlzEdpGLARrT6hFpDsjPKCqH3MFxoriw9JIOulZluSI5kYcPG0NZpGaM1gDvYF2x8CGEtZoDFTdf6hkjSiNW9kv6vPGXiRW2Sg4g2HS9zAn186HQxYHUa2QTlwjU4XBGo9Ifhk7K8WZF38N5p6NpnwfuCic7vKKr9zgdOWtHNgVYpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c262c988.mp4?token=cUjD7Bvh0jMYoZ50eU4bvsC9G49JSTbebg7YK0lv4MYpAfZaz1ivNOXI_vIuuoRIJKEv_0CwlSDxZF7nWn5YmlAhf23SEPcdqSVFeYPYtfROSrPWkzARBqVEzA0K3gCaL_sTeQOf-gD6Dhj14GDpK7b-hi4c_0colSoEB6o00tKAT1yBnnyUR2cIhFsDyYZCnaTf7PayM7fsuREdelHd6mQBGt8wQ38vqKlXwU_WW7TRaBW8JW5NEEfQZ1YPljjSffRNzqQl3MvB21L3BJ-w_vzs8MnHzvSM359GhQINiwmuSHyxCx92fE6TQsCKhQIUyN6s4D1s4lAW7osucMUdh2xYGPOLv2ciOjX2gS2UDU2sDUyrqUcQBrKhFFgp4c-_EMaxiwR_8fXgpDwChg9YXFXgEdrRhtAP9ZVJ1WQ9yrNSvdv93894Q-hiVdIWdbkC01z3ARAnFjb8eIRWtMLq_vPufqyMkhGpcpsbkONOYpyN7gm4-2zrvfi4G7bAwxlzEdpGLARrT6hFpDsjPKCqH3MFxoriw9JIOulZluSI5kYcPG0NZpGaM1gDvYF2x8CGEtZoDFTdf6hkjSiNW9kv6vPGXiRW2Sg4g2HS9zAn186HQxYHUa2QTlwjU4XBGo9Ifhk7K8WZF38N5p6NpnwfuCic7vKKr9zgdOWtHNgVYpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت سازمان مدیریت پسماند و استقرار ماشین‌آلات جهت پشتیبانی مراسم تشییع آقای شهید ایران در شهر مقدس مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668905" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb_3iooVFvwaCGDl0W3oUr1SJvO29BKD2KzRSr96Xstg_2L8kMm4IICWpRQB8Hgjj_BT6f1hF6qv7CswlRW1dzNVx14ZuneJ9-iXr0nhpPyNvjuHNbe_mZ9WlGm_ZslR_gFkRy9CVLRJAnOwMGhMUkD7NHAQDa-xGfsxv4zqDN3EIcYYunR1sUGlGWJMYwSqTad_vC57ofZA3fLXWQW4plFDdd5B-ez2y9hRLZ9X0IyjS6uXyOD6iP6BTstx2hS-yk38Jz5COzXTTpYDk8e521AENxhXkeo4ViGTqSXh-j2AcySzRtRiM0BBbzhjVkfh7qvf8wlxANqkVr3qpGSK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت نفت برنت به کانال ۷۶ دلار
🔹
با وجود درگیری‌های شب گذشته در جنوب کشور و پاسخ ایران به حملات آمریکا، قیمت نفت امروز کاهشی شد و به ۷۶.۹۵ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668904" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استانداری همدان: نقاطی از شهرستان کبودرهنگ مورد حمله دشمن قرار گرفت.
🔹
شورای عالی انقلاب فرهنگی: تعیین زمان امتحانات نهایی و کنکور در اختیار مراجع اجرایی است.
🔹
فرانسه خواستار خویشتن داری و ادامه مذاکرات میان ایران و آمریکا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668903" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854d7fb85.mp4?token=mVOiWP65dMNHS0JD8wqwiewaqrmLzl3Pl4ZaMpHyR1ysFoVjvqXUh5c_os4Iq3u4BfdyXVFRuB5tbVRNoD8IfZhjSNQ7TAAbZWC_xbPhwZ_S_wYNIMSKsCu5mCzO3WMisWI9KM27cMyFKVd-J9f1SBJBS2pmLYg_YrA9fpxfzkK1LbxICJeLAvsDfPhSI7WdqgHuBQdWpfjhSOjA09XZ0tCQmybgc35t7P8QgJTeltCBhmFWvehUywHWlZQsEnA1OF26y_ZD1KRO-jqQ8Br6q9zEl4dVYrPWn5hqKyg2VLbX6J96tpR-g_Mq_B1WcLdYjkDTNfq94ja-m5VEqGq4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854d7fb85.mp4?token=mVOiWP65dMNHS0JD8wqwiewaqrmLzl3Pl4ZaMpHyR1ysFoVjvqXUh5c_os4Iq3u4BfdyXVFRuB5tbVRNoD8IfZhjSNQ7TAAbZWC_xbPhwZ_S_wYNIMSKsCu5mCzO3WMisWI9KM27cMyFKVd-J9f1SBJBS2pmLYg_YrA9fpxfzkK1LbxICJeLAvsDfPhSI7WdqgHuBQdWpfjhSOjA09XZ0tCQmybgc35t7P8QgJTeltCBhmFWvehUywHWlZQsEnA1OF26y_ZD1KRO-jqQ8Br6q9zEl4dVYrPWn5hqKyg2VLbX6J96tpR-g_Mq_B1WcLdYjkDTNfq94ja-m5VEqGq4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ ابراهیم زکزاکی، رهبر شیعیان نیجریه هم خود را برای تشییع امام شهید به مشهدالرضا رسانده است
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668902" target="_blank">📅 11:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668901">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2cf8e67.mp4?token=lNxTftwEu55FrX3fWkvl1Pxlm8JnVKUnhUerBLE1yBv8sDuekL3OfIvHVukuCthf9_IDMPL1xczwQY9eXtbMj9Dym9572AJ3PyUGrYQtv-BgvxJBchvp0RA3jwDoKqvu3b5u-7BKRuLuR6Au285VDIUE9t-zC3hG30pwoL-qjt9lKuGr8ie0R8AQSKGBRKDPFN2j5iqRD3jFTNIrOOa2kEzaJLcw5_roKKG9u8s4ZsTRQVa31i-_rOey2CueVWGSoV_ThmjEF7uHjJvSa8voF0M2vRMoKuE-B4Klsj5PpBavAwfezwKBRhDcR44G7NRMuJVBwXEMui8p4We1JFer0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2cf8e67.mp4?token=lNxTftwEu55FrX3fWkvl1Pxlm8JnVKUnhUerBLE1yBv8sDuekL3OfIvHVukuCthf9_IDMPL1xczwQY9eXtbMj9Dym9572AJ3PyUGrYQtv-BgvxJBchvp0RA3jwDoKqvu3b5u-7BKRuLuR6Au285VDIUE9t-zC3hG30pwoL-qjt9lKuGr8ie0R8AQSKGBRKDPFN2j5iqRD3jFTNIrOOa2kEzaJLcw5_roKKG9u8s4ZsTRQVa31i-_rOey2CueVWGSoV_ThmjEF7uHjJvSa8voF0M2vRMoKuE-B4Klsj5PpBavAwfezwKBRhDcR44G7NRMuJVBwXEMui8p4We1JFer0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خاص خونخواهی رهبر شهید در حاشیه مراسم تشییع رهبر مسلمانان جهان در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668901" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668900">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNyER5I8oIegEM8a2uM1NpLMqR3T_1MSmK_m08e4FYG74tiLKdFtCu7JorC5ekdQ4ZTPkW-MsMFDFzHbZ4QB0hcnYTN6KbECcvef4B8tDbScF3Ihgsy8S-UTM25cDXoQ6BeZTEAaExGtf_s0L7Gy7q3-LZytgUb7D2LuQxcCPGflOnQ7gjAdTFMKFirYLkkqNVYNl0tr-wEwDzLmMhwvdy8GxQMAej1fGyqF6tHiBf_Nqe0ZHn-3Z3jfG937ra3h4t5pnZQ1MPZCYl8UjQONv80WSqdZ0B2Q1MfdNIKmz7HZK19lPIc53cv8kVyErPr1uOlDVw1PchDDAXkTUDuGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره اقدامات تجاوزکارانه ارتش تروریستی آمریکا علیه ایران در شب گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668900" target="_blank">📅 11:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668899">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d69f5bd3c.mp4?token=SRkGcT1FhDnn1M9CGMcSnmbKBG5Md29p6ZRcZfyT2OadpfDlq3rYg3qva_pC9EFjbghIN5qv-JKIxYFO60872UJPamxg3FpOonKRMYIWwqc8JxWChPB2WwIVutGaFZ_7siRODVeY7Y0MfyID2-ninh7_kEv3BAcN1HgwwnoXoOm0CkvN1u4ty4rh8Z9dnH_3oGQu6FoDFxXzhM1_TqxX-wu9yxFJ7wO7Bt2JCuSaZd6zTQOni-SD9SzHQzClEG4Y-Pgk4oX1eWBWSAJKCXj3tdWBMc3IGVKzsxtuMxVSQJzIK1HGOmeVOh3Ugl-DDJpuRlsb1e147b1GGbPt24kE_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d69f5bd3c.mp4?token=SRkGcT1FhDnn1M9CGMcSnmbKBG5Md29p6ZRcZfyT2OadpfDlq3rYg3qva_pC9EFjbghIN5qv-JKIxYFO60872UJPamxg3FpOonKRMYIWwqc8JxWChPB2WwIVutGaFZ_7siRODVeY7Y0MfyID2-ninh7_kEv3BAcN1HgwwnoXoOm0CkvN1u4ty4rh8Z9dnH_3oGQu6FoDFxXzhM1_TqxX-wu9yxFJ7wO7Bt2JCuSaZd6zTQOni-SD9SzHQzClEG4Y-Pgk4oX1eWBWSAJKCXj3tdWBMc3IGVKzsxtuMxVSQJzIK1HGOmeVOh3Ugl-DDJpuRlsb1e147b1GGbPt24kE_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون حال و هوای حرم مطهر امام هشتم علیه السلام
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668899" target="_blank">📅 11:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668898">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668898" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668897">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01590978.mp4?token=nf9S0eLlHbi4lsMsr83MrOI6d1lM2wSlEzyHaVChtbqSjWDrhaLbkNCKN-KfC07woA1MrTaBEM7FvOVz902wP9ugqFJ50mFQ_Wr18BEB1pOBfb19J2jiePxR1rjgX-lWd9k58vHm9DivVSB2TDBxeSrDxszrz6Nily8XB7Y4nVxS9idfbVr8V7xHY4K5TvuM4CTzgIDBDTD1ZkU11a3ymwJldz-Ai19wtbhWhSp7zQIaveKtYUe7Zebv5IOV5haZF6ysY45mhE4yfjhqAo8h7UTDKDNzRg7RA8HKBMeFeYPPyfFqn7-ZcFZhSu-8C6pLJYE0iRrOnrONRLx6vknDOqjoI3As2cM3C-BorehLWJw6sEm3WEZM7fKtpxzhN23xywPEWpsqNFTn0E9qqiP1hu7p3gHGR13B8FwMN9AO81WxJNAUhQnMeV9w_XlSSchOEUQF9ED_bR4uRkgiuTa6igV3syxiGOpTZt8S17SVcMK7Ca8x9V-ALFro8Lq8xfPl7Mffl_l5o6B711CdtyovBL-DD3RZ8zSq6o2xG0F1AlRoGREV1YI883gSekJ4lcW5t15ExDw08KWSxdeLPkJZjPmd-HKxWDzap2dZifLkyqjnkpTq39ZVEOqxbXvoBY7CIPL3lSlPBVtY-3xJHcZvot8Sg2oBK74o6AUZQQXPf3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01590978.mp4?token=nf9S0eLlHbi4lsMsr83MrOI6d1lM2wSlEzyHaVChtbqSjWDrhaLbkNCKN-KfC07woA1MrTaBEM7FvOVz902wP9ugqFJ50mFQ_Wr18BEB1pOBfb19J2jiePxR1rjgX-lWd9k58vHm9DivVSB2TDBxeSrDxszrz6Nily8XB7Y4nVxS9idfbVr8V7xHY4K5TvuM4CTzgIDBDTD1ZkU11a3ymwJldz-Ai19wtbhWhSp7zQIaveKtYUe7Zebv5IOV5haZF6ysY45mhE4yfjhqAo8h7UTDKDNzRg7RA8HKBMeFeYPPyfFqn7-ZcFZhSu-8C6pLJYE0iRrOnrONRLx6vknDOqjoI3As2cM3C-BorehLWJw6sEm3WEZM7fKtpxzhN23xywPEWpsqNFTn0E9qqiP1hu7p3gHGR13B8FwMN9AO81WxJNAUhQnMeV9w_XlSSchOEUQF9ED_bR4uRkgiuTa6igV3syxiGOpTZt8S17SVcMK7Ca8x9V-ALFro8Lq8xfPl7Mffl_l5o6B711CdtyovBL-DD3RZ8zSq6o2xG0F1AlRoGREV1YI883gSekJ4lcW5t15ExDw08KWSxdeLPkJZjPmd-HKxWDzap2dZifLkyqjnkpTq39ZVEOqxbXvoBY7CIPL3lSlPBVtY-3xJHcZvot8Sg2oBK74o6AUZQQXPf3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشتن پرچم فلسطین توسط یک کودک در مقابل پلیس آلمان
در تظاهرات همبستگی با فلسطین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668897" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668896">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5qkPBAOWPtPeq8kcVb37PYy10SXqQ90Syrz30UaMhc8_0qc98HHCAEjDbBSVo9Am01i8UaV-PJFUlRi-ep24kNxAYiw4DonYMBkcFfgAKqPyGzisbfOgU6AogWCbGcbn1AD7SleVYgHYNJ068YA5LG9gY2-yrILgC6-NsQ2OCkTcgieqaVOu3J1sNM1TuYB_9HLr3xGLQAqC81uD6smOrpzGaZha95AiYN8iHdaRjz6_dHRhqrODRHmhnijb8QOiRsZFdPrLy_pfa9tmFGaancxAuuUc82XfHGEE_3v4rnJM4Xe6ja5PtVJSVciqweMQwbj8We7h9i5lB8qZhdCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش مچ‌بند و پرچم سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با مچ‌بند سرخ و پرچم سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ و پرچم سرخ، نماد عهد، وفاداری و خون‌خواهی امام شهید است.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668896" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668895" target="_blank">📅 11:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آموزش و پرورش: دریافت کارت ورود به جلسه داوطلبان ایجاد یا ترمیم سابقه تحصیلی فعال شد.
🔹
جوزف عون از آمریکا خواست اسرائیل را برای توقف حملات تحت فشار قرار دهد.
🔹
تسنیم:
تجزیه طلبان بلوچ شهرستان چاغی ایالت بلوچستان پاکستان را تصرف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668894" target="_blank">📅 11:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e94190b053.mp4?token=fJvD-EWRDOyjOVFsjysadEWi038wfluLgMjigz_IBpTy1iKsjHTOxPCVa9C9gQpTwtP7iPuA0Qg8L3sXv2UOqvaEZvT7dOY1krB3hEgyUYm-VoAnaOSMbIk9NsnXgRd0DY0ZeJYhwPGfKO3KVxzyiQdboODXhmh85bs9Hq6i0ejwk0op5fAP82uazfmgqnfpYra_se7FQUvWshq4c5N2V7ic1pDOXKcucKWUUSOs75YYxOmw-jQUq37fP6FYO7ZLuuZZmdSc16H4XhT6QXn-r6T9pFMTeoEfoUK90qO5DUWt2-455Pl0XJ4IqOv2XyPn48rST3je2lvu9-g35YlJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e94190b053.mp4?token=fJvD-EWRDOyjOVFsjysadEWi038wfluLgMjigz_IBpTy1iKsjHTOxPCVa9C9gQpTwtP7iPuA0Qg8L3sXv2UOqvaEZvT7dOY1krB3hEgyUYm-VoAnaOSMbIk9NsnXgRd0DY0ZeJYhwPGfKO3KVxzyiQdboODXhmh85bs9Hq6i0ejwk0op5fAP82uazfmgqnfpYra_se7FQUvWshq4c5N2V7ic1pDOXKcucKWUUSOs75YYxOmw-jQUq37fP6FYO7ZLuuZZmdSc16H4XhT6QXn-r6T9pFMTeoEfoUK90qO5DUWt2-455Pl0XJ4IqOv2XyPn48rST3je2lvu9-g35YlJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود هواپیمای حامل پیکر رهبر شهید به مشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668893" target="_blank">📅 11:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تجاوز مجدد صهیونیست‌ها به سوریه
المیادین:
🔹
منابع محلی در جنوب سوریه اعلام کردند که نیروهای اشغالگر صهیونیستی به اطراف روستای صیدون الجولان در حومه قنیطره نفوذ کرده و یک ایست بازرسی موقت ایجاد کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668892" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1348bd0520.mp4?token=OtBLqAbBZDaQCh4GD8SmAR8zMfz6ULUeaHYSNpDkBVhCgll-HFUWei1xReQ4X_o_xPzb7-xHURBn72pKTytKEqfKDJfiMDWqum-LYDovvGv03FHxhBQF2VMD-ib55zjpfQxYD4SoBd8RJrEew6aZNeQchjhYd5IPkPJmOHOmkjeBcAaBny7aYAWtdtMkmbcKVFcv7BBHywWw9082A00dvmAwpHHVh2lfRf2ON9Pz4ToKbZVs1AEJRtzXKlJQKrPPJsbCaC0nXdldz40ap6mctBcBcc_zAJfjUxgad1vL3Ui8OO9CLrS5tOLkLF2hdCUP1g7pKx2sWDNGIAFKn6FXbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1348bd0520.mp4?token=OtBLqAbBZDaQCh4GD8SmAR8zMfz6ULUeaHYSNpDkBVhCgll-HFUWei1xReQ4X_o_xPzb7-xHURBn72pKTytKEqfKDJfiMDWqum-LYDovvGv03FHxhBQF2VMD-ib55zjpfQxYD4SoBd8RJrEew6aZNeQchjhYd5IPkPJmOHOmkjeBcAaBny7aYAWtdtMkmbcKVFcv7BBHywWw9082A00dvmAwpHHVh2lfRf2ON9Pz4ToKbZVs1AEJRtzXKlJQKrPPJsbCaC0nXdldz40ap6mctBcBcc_zAJfjUxgad1vL3Ui8OO9CLrS5tOLkLF2hdCUP1g7pKx2sWDNGIAFKn6FXbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل مرگبار در جنوب چین با ۳۹ کشته
🔹
سیل و بالا آمدن آب رودخانه‌ها در جنوب چین یک سد در شهر جنوبی نانینگ را تخریب کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668891" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668889">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjGM672o1spAmoG58-19b0uI7br4febKKvNjJBAyMMQr-uI1jy9vh4lBH_yIdnHlHxrYiXbtFZAXvXeuQpGa4K8dkLivftgXGZay-Q7I7NLX0lGCnU-EJnyewYZ4uxYFMCiA_2q4G1mVSAqeQ02l9hUUv3jjmFYNEZR6gcO1ONhEnSNrQSsMoJC7qfuXPSyoahdLJKYfkmR4QmXYfKuQdHUn8vuv5rBxbbaCxwzmqhiBoRkvn__9e4W7sSNQTyriGo_7es3FjUNqcxsb5XZ78Dkb_ky_JKgQdaT-el4YjDKkEGXDpwryOhQ4skdD9lT5i2S5e-7lHSGQdKOSJt8AoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر جنگ رژیم صهیونیستی: برای ماندن در لبنان از کسی اجازه نمی‌گیریم
🔹
«یسرائیل کاتس» وزیر جنگ رژیم صهیونیستی در واکنش به اظهارات دونالد ترامپ، رئیس جمهوری آمریکا مبنی بر اینکه "اسرائیل" از لبنان عقب‌نشینی خواهد کرد، گفت: ما برای ورود به لبنان از هیچ طرفی اجازه نگرفته و برای ماندن در لبنان نیز نیازی به اجازه کسی نداریم./الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668889" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d1640fe5.mp4?token=RBaoaU0IEw4nJyldLQ_UQ0otcyEgWqsmgC9kR6t2dwsT6BgXk5gGkbrbZ8D-IOGnpDFyq9HGWOt1MQQO-ajuL7xmBn95xr9zkaihsrzi_CsV1Qu4FJmK5MGGcWgvFsusHocLty20bDWpqHZC8JpH1xtDbtJZLvYS76zmus5caSJuz6dzYsERp-PIIoosr9024m8JG1aTA7czA7AOtLzjitqWpl_c_lFaMtVf6sbl5qXlOB2pbuQfc4y-2TrrwiGNBR_LR4i5u7Ee-u0zG6TV1RIhJzuHha_yCwayZixWNcsNdFoorz-ibXLEsINocqwJNWKr23TyldizqbYw3XfLu1Uy4riV-NSXS6zAl29dHFLRxjabKZG3Bf2mWj8OS9uk0LKxHZl4135vhI03xAjeJpbVgE2M7-me-rIpgT2fXpJ5BIn_SO0yOPhYoSQ0eQLeCerBlECQpitM0G7CMkz7eauPR9BV04PhO-1sZTIqabgOsFTHXA_XBQYHKebQnr3K5nMLKMHt6b6ncoxYd3i2klHaSnr1pZmxCPIwFVGC5mgc7agVjU9pbWA5bV8J7rVybfqH9ZCJywPjUjm1eISXM8qu9qH7K_hXO1L0P0aXMtPE1un9wazo_y_fl_1Sq0KJRnq_tle4agclUZ1FKzsqIgtvCVQM8isR72SAXtmcZKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d1640fe5.mp4?token=RBaoaU0IEw4nJyldLQ_UQ0otcyEgWqsmgC9kR6t2dwsT6BgXk5gGkbrbZ8D-IOGnpDFyq9HGWOt1MQQO-ajuL7xmBn95xr9zkaihsrzi_CsV1Qu4FJmK5MGGcWgvFsusHocLty20bDWpqHZC8JpH1xtDbtJZLvYS76zmus5caSJuz6dzYsERp-PIIoosr9024m8JG1aTA7czA7AOtLzjitqWpl_c_lFaMtVf6sbl5qXlOB2pbuQfc4y-2TrrwiGNBR_LR4i5u7Ee-u0zG6TV1RIhJzuHha_yCwayZixWNcsNdFoorz-ibXLEsINocqwJNWKr23TyldizqbYw3XfLu1Uy4riV-NSXS6zAl29dHFLRxjabKZG3Bf2mWj8OS9uk0LKxHZl4135vhI03xAjeJpbVgE2M7-me-rIpgT2fXpJ5BIn_SO0yOPhYoSQ0eQLeCerBlECQpitM0G7CMkz7eauPR9BV04PhO-1sZTIqabgOsFTHXA_XBQYHKebQnr3K5nMLKMHt6b6ncoxYd3i2klHaSnr1pZmxCPIwFVGC5mgc7agVjU9pbWA5bV8J7rVybfqH9ZCJywPjUjm1eISXM8qu9qH7K_hXO1L0P0aXMtPE1un9wazo_y_fl_1Sq0KJRnq_tle4agclUZ1FKzsqIgtvCVQM8isR72SAXtmcZKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید به خانه خودت خوش آمدی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668888" target="_blank">📅 11:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e0d69b43.mp4?token=Ee-KLMSiFN7xYhL6nz0ZmTT4aRfUqGLz5VSZuZvF1NX5ELKrucXm33H7erI6eJ-GCsjWPMxC4K8j0hR0lswEAlR6nPqQ6iNWRE1GDWBAfXNQ1NpLeFv8F6lk30-cgCcKhXyedc4DkwgdMzvUIb6nyClvhhz08epn3DJDetDlNE9144CXSB4mwTgjzUF7luATDqhLBCbka47vPdvUgS3qwpI_5KdNIhPHC2rODT24wpKwgrzCmzZB1Hu35GNQmVz19OgmJF6JaqrSmtzHua5PJ4b9fTiQEVBS1EqErzscB-b6XF7KOH5ieQ2HIS5sMuIcCL5bmirPdTjT-Nfp2BbhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e0d69b43.mp4?token=Ee-KLMSiFN7xYhL6nz0ZmTT4aRfUqGLz5VSZuZvF1NX5ELKrucXm33H7erI6eJ-GCsjWPMxC4K8j0hR0lswEAlR6nPqQ6iNWRE1GDWBAfXNQ1NpLeFv8F6lk30-cgCcKhXyedc4DkwgdMzvUIb6nyClvhhz08epn3DJDetDlNE9144CXSB4mwTgjzUF7luATDqhLBCbka47vPdvUgS3qwpI_5KdNIhPHC2rODT24wpKwgrzCmzZB1Hu35GNQmVz19OgmJF6JaqrSmtzHua5PJ4b9fTiQEVBS1EqErzscB-b6XF7KOH5ieQ2HIS5sMuIcCL5bmirPdTjT-Nfp2BbhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از تهران تا نجف و مشهد، یک مطالبه مشترک شنیده می‌شود؛ «خون‌خواهی آقا»
اخلاقی امیری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اگر صد نفر مثل رئیس‌جمهور آمریکا به هلاکت برسند، ذره‌ای از شخصیت آقا را جبران نمی‌کند. ما باید تلاش کنیم در منطقه، اسرائیل محو و آمریکای جنایتکار اخراج شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668887" target="_blank">📅 11:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c47bada2.mp4?token=W24o6NWn_bnPlGBhcJYl42-OXV8Rr1yRdS1QXXcyTg6SW24wgCWJY8RZ38OWYKBEmG3RR-TkXNaXd2DIfaUQ5P6xKDfObIeOXBUrU9ATpk2VNcsm_jXeOWE6JvJqLMPmnmfGeBxeKMNx-hX-vIow989A4yeS33wnvtDLYmT5k1OUKIs1EbPzLc-HhCQtIRy-F7AkeFC_k6ODmvgTlhCXkIc4-dvVXr-A3xsoGM6S4TTVWgjfXbnjKm7hwT7nl9tY5s36lf1d1k7JT-U4T_7TXmYAwzOzcaN0413Uyus1Set3d92bJnYuNpCfpt-dlR5Nzh8BFsQ5XqINTdgH-JuhOE36Dxb3tWvWO_HN2zVd7IsntxlwaSZ7FP39S8tqdw-pDJ1h_sYO2etw5B0qxIJLSVTiKAy5WhflEuLzOnS0iGIa6iAntCEdVKu-ViI8UMmxCqYcoOFgW_AHMo_8t9pUlFmpqS9N1ijjAiIdmtMYeiQb_CYn3fYrw31gf2Ljj9OOvaN_QBu_oVlQq6YWFZVtFehHPxtsH_HYwdIMjg3N6H4r3aNsgWie-2NKEKnbNfffVLUFYorEboAPiU1Dt7NZDpu5NSnZcaCbREhNCAGmq7PougJbUdLdWZZWgbRINVr2c_2o5Lpv9jVxdPTFrmbOy7uprL72I0vsQjWYwoeqnt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c47bada2.mp4?token=W24o6NWn_bnPlGBhcJYl42-OXV8Rr1yRdS1QXXcyTg6SW24wgCWJY8RZ38OWYKBEmG3RR-TkXNaXd2DIfaUQ5P6xKDfObIeOXBUrU9ATpk2VNcsm_jXeOWE6JvJqLMPmnmfGeBxeKMNx-hX-vIow989A4yeS33wnvtDLYmT5k1OUKIs1EbPzLc-HhCQtIRy-F7AkeFC_k6ODmvgTlhCXkIc4-dvVXr-A3xsoGM6S4TTVWgjfXbnjKm7hwT7nl9tY5s36lf1d1k7JT-U4T_7TXmYAwzOzcaN0413Uyus1Set3d92bJnYuNpCfpt-dlR5Nzh8BFsQ5XqINTdgH-JuhOE36Dxb3tWvWO_HN2zVd7IsntxlwaSZ7FP39S8tqdw-pDJ1h_sYO2etw5B0qxIJLSVTiKAy5WhflEuLzOnS0iGIa6iAntCEdVKu-ViI8UMmxCqYcoOFgW_AHMo_8t9pUlFmpqS9N1ijjAiIdmtMYeiQb_CYn3fYrw31gf2Ljj9OOvaN_QBu_oVlQq6YWFZVtFehHPxtsH_HYwdIMjg3N6H4r3aNsgWie-2NKEKnbNfffVLUFYorEboAPiU1Dt7NZDpu5NSnZcaCbREhNCAGmq7PougJbUdLdWZZWgbRINVr2c_2o5Lpv9jVxdPTFrmbOy7uprL72I0vsQjWYwoeqnt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر مسلمانان جهان: اگر مسئولین کشور مقابل دشمن خوف داشته باشند بلاهای بزرگ بر سر ملت می آید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668885" target="_blank">📅 11:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6c05a4f4.mp4?token=bDp2YG-TSOBz8M-1cvGUFDTknWc-0eOaCMlafkFsX98XMts1SbPCTqPSzxxLJmEntDNy9SsoSXtIV_I7HFBSsDTkDq4JZ6wW_70JOnoCq7-0_UnKtJden_hhyZ1TXoXlgXYuVvnJtlxgp-XMJCc3mPgp7xiVMWlvrFDXMhRMIknqYkn_6XzJDjIyxbRZGfD4wMyCrcErjoFU5xq-LdUxq87WNzLdBJW81Mqq6-N6T6bf20yo10Y7YJI5Ts0PymR33nCvAa9pypoIOVh3ehtoNGzYRieqYQMLaPUkAqDuF0N-dLxhA7Mc699USEgRKGm-cPJyztn9Xd1ReXHnh2d--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6c05a4f4.mp4?token=bDp2YG-TSOBz8M-1cvGUFDTknWc-0eOaCMlafkFsX98XMts1SbPCTqPSzxxLJmEntDNy9SsoSXtIV_I7HFBSsDTkDq4JZ6wW_70JOnoCq7-0_UnKtJden_hhyZ1TXoXlgXYuVvnJtlxgp-XMJCc3mPgp7xiVMWlvrFDXMhRMIknqYkn_6XzJDjIyxbRZGfD4wMyCrcErjoFU5xq-LdUxq87WNzLdBJW81Mqq6-N6T6bf20yo10Y7YJI5Ts0PymR33nCvAa9pypoIOVh3ehtoNGzYRieqYQMLaPUkAqDuF0N-dLxhA7Mc699USEgRKGm-cPJyztn9Xd1ReXHnh2d--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خونخواهی تا دلتنگی، حرف دل دوست‌داران ابر مرد تاریخ ایران به گزارش خبرنگار خبرفوری
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668884" target="_blank">📅 11:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5cafcd3a.mp4?token=Sx_G98-Rr_Gf88mJulUaDMozBpfgMbhtmshgBdkkwoJGNdymVsqabC9flkyAIqLS0lcoSkX-h9rFAX9rP4U8WyHA3TYCCveqEwIPbZrpg26ypeqahc2TyIHy6o_lm0lhsoG39KzVdo2_-cYPubMCGqaOnPsf3s3GMXCSWLvp6Bbl_gvkvimGKF8oc9ZqJMcYe4jxV-idXTTu8jv1qXey3NY6b6BGDvcQfTZLwMDcs7KWqE-oy1f5hRm63kYydUAriQ6lyXtXiMZdPj1zqMa2Sy8TbWFFoQWRGbkF1vGZBiibDzUzo9yMiCbDhW-d8VZxbsNHIqM5kwKCnI1scND74IWsgz8nHWcghI-pDGUeVabIWHydUNoSim-mbpzyjGgy1OrKo82kYO8RjTuEMFnIjsGvSxsC0Ix7vDMTAn1WGFLChr5L-gIlwTlmuGLz5sfknzOf08Qu9Z-anRq3kl00bEohDPNy6O-srMlEG9kkaqX9Oz58HCJ8F--SlSkCgSYmRLG7hLCJU6ZKt-ZOXL3dELu-2INeZHD6lDsZrAQVn3scEmsNaBQzzrHclYuoXh-5yduymkAPnzsDTIk6kUqCa0iLoJRImmSfqrhs2eYLqbpujh4jr46047G5WA45YV_H_WaBfNpyg9FsQZBeFIu-ONulXLXDtXytfSo9BXSlBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5cafcd3a.mp4?token=Sx_G98-Rr_Gf88mJulUaDMozBpfgMbhtmshgBdkkwoJGNdymVsqabC9flkyAIqLS0lcoSkX-h9rFAX9rP4U8WyHA3TYCCveqEwIPbZrpg26ypeqahc2TyIHy6o_lm0lhsoG39KzVdo2_-cYPubMCGqaOnPsf3s3GMXCSWLvp6Bbl_gvkvimGKF8oc9ZqJMcYe4jxV-idXTTu8jv1qXey3NY6b6BGDvcQfTZLwMDcs7KWqE-oy1f5hRm63kYydUAriQ6lyXtXiMZdPj1zqMa2Sy8TbWFFoQWRGbkF1vGZBiibDzUzo9yMiCbDhW-d8VZxbsNHIqM5kwKCnI1scND74IWsgz8nHWcghI-pDGUeVabIWHydUNoSim-mbpzyjGgy1OrKo82kYO8RjTuEMFnIjsGvSxsC0Ix7vDMTAn1WGFLChr5L-gIlwTlmuGLz5sfknzOf08Qu9Z-anRq3kl00bEohDPNy6O-srMlEG9kkaqX9Oz58HCJ8F--SlSkCgSYmRLG7hLCJU6ZKt-ZOXL3dELu-2INeZHD6lDsZrAQVn3scEmsNaBQzzrHclYuoXh-5yduymkAPnzsDTIk6kUqCa0iLoJRImmSfqrhs2eYLqbpujh4jr46047G5WA45YV_H_WaBfNpyg9FsQZBeFIu-ONulXLXDtXytfSo9BXSlBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاد دانشگاه صنعتی شریف: افزایش قیمت پلکانی برق، فقط قرص مسکن است/ اطمینان دارم مادامی که تا این حد سیستم انرژی دولتی باشد، چالش‌های این حوزه حل نمی‌شود/ رصد انرژی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668883" target="_blank">📅 10:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سازمان راهداری: هموطنانی که برای زیارت و مراسم تشییع قائد شهید امت در مشهد مقدس حضور داشته و قصد بازگشت با اتوبوس دارند، بلیت برگشت را در اسرع وقت به صورت اینترنتی تهیه کنند
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668882" target="_blank">📅 10:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWa5rHMdeXbNMEmIs9M3CpdUrf9b-JWmevR-aDfgy0DZvq7lqEkMDXTf024IFcBUMXruq_FqbxZAdIOzbDQafax7QJwxcNyfO-utexa9pZMfdGW_J38DgxzUumynC31umVi7zwP8gLAN6Rc2P73SxEcDh5xMeru0mVa0hsR1g4oa3Hb6CyiiRsWyLTiKaCSsntgC-BA7ZQeDSZNUheCY5peWftVGqSkFxCVmz522y0rcY2UL1IHlk_kzitxAwUsSiBUva7yyJEdnR_05YNK5YVydAuLCsDuI5MDjn-8J-8l0sJdddup_txIFm1Wr6fPdec137q5Vb8oI0qU-yKH-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5vSIqOfyyxli4_OEbhWjO8wVn6z5SlwYXB6YqmujRUSM-OY7zmkW08pPCnN1tRglqrbcjrhGHETl_Mpz9pUshc4Qz7ugoQaxvHMrTOUqKTe7s7fa077ox-BuKsaxx_AT5-CkhljVV4LBh9iuzdZNEWnsAjkLBQEB8MojDkuJ2yKMJofBstG0VZQlP-Y2uqNFhj5-V2hDthGwOD1LGL785Dmq7LMzgfxPcFBPMRs7z_OIGlSPVb9qeYlLwptA5ROsc8LI9H5-WrTSeS34-h30yYVIbOaz5PGmeidsJgIW-nPOYDAd5BSGzJEiSCJoQOPEM3QoIq73cDbqSh64jF9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jD1gTV5SKU7qVlKkDO5XBzaQyxYq-c2u25pntdpgixOTWAV1KRWpYAgMFBkSkTo5VkEaGNgNaANGNj49O9cq2DoGuE_XUcWOM21oXpfJAsVQnxZKLiNKqU7K4jUcyY4IW6tLReuxHvvqGXXhAuK-eY4TeQzCeyGvU3M7vtkqunQYJUS4SSRrfmvHHQmLJrYGT4kAdCXr_dGE41ZdFxF_Fw2roY9ajD-mOnN8QG4jOMicT3PpU4MYCmxJsUEt1ddLlLHBJKpXw_kVnpztA7a1u9cDirL_WEZqzmZfOwO2oT1mx57Y2vuufB60_k5w9qELI51yJYqobIJ-L1imfLwU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmsCmREbZpRi3gvJjQV4pc1SphNmMJNsV2pmB0Q_3O9hPZx8XhzTmcijNLTSH2l_Nac6W0GQo7Zvsgc-Zc34liol0foKQ6hD538KgFjzdcxNNnndwqLl_X_RZR5eOYfPRRdpAPh_3K9lARyc5yxzVmS2gUqeVrqvdOAKd1lderGeaKLRVXPRY8NsLBvzzLJEdC0IJxkYg315NxPNUeJfuh83xDRObAjDyx5vZt2N8KXokwrRShSYLpprg-Ss3POWjl7Ab3oon0_QkoHxGZXpe9TLRfK41aRJU6jLDrz6L0dPtIxRJxZDUO-StuUuKez485Auaorj_QmR1mBClApdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnX5_Z936DbQWa0M2P1n-s380GczLbp3hndMBXayqMPquvUHleFu_yuS_ZhvUYOHNNLteTO5hmM_fLayCs2UXavAiJjwYgTbp4MS-XdQ2sWP9ESGo-FWC6KEFVoHSYwQtLPc1XXZebcTCPF24v-p3GR162f9cU_eVD5tBm2HM1h_zdCaDBKoSOPP-6nlSHrIL4lMSGgChj0sTKakgqIMhVmUE0RAzBZlhArv-gczTmis4pmK6dwreyQNEYTRyaz75gYw9--MqDvOGJvx8Ez1Tx7VXOduBlE4ESFbg8lEjeu2XHocjCb7wIBL2UyDwn0mHBLxToJiL4XzzDxUwTC13w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گزارش تصویری خبرفوری از حضور اقشار مختلف مردم در مراسم تشییع رهبر آزادگان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668877" target="_blank">📅 10:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748fe9e2a4.mp4?token=YOXr0XU6wkApB58gc1igCeZNrAJTJEtqOlfZyTd5sOG2HDm_QUTg3KNcNcKAzIvwB7ty7UlEqNp8nF5WId4kc6COe5NPNz9W4OD5aLW5WzVA_-8x8dHmhCOfZ92GHLSyFbXvW_A7b6rLhF6gujWAeXyaCiDqZHxc7w-3l8UlV1KPIU65344cNr8O67awXwhXB471Vn2FfsZMV6EN6thkvQUFJgljXaNO7c4VW3VdHQqnQk0iK6lT5i13yRcZvgJCaIjvVpVVrRA0KdC1WwG21lLXIIbahgpMQWK2Sa2P6EE5xrbjq1-zi9oyllNvfsyX3NHw5NhkAp03KEIRBz6s5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748fe9e2a4.mp4?token=YOXr0XU6wkApB58gc1igCeZNrAJTJEtqOlfZyTd5sOG2HDm_QUTg3KNcNcKAzIvwB7ty7UlEqNp8nF5WId4kc6COe5NPNz9W4OD5aLW5WzVA_-8x8dHmhCOfZ92GHLSyFbXvW_A7b6rLhF6gujWAeXyaCiDqZHxc7w-3l8UlV1KPIU65344cNr8O67awXwhXB471Vn2FfsZMV6EN6thkvQUFJgljXaNO7c4VW3VdHQqnQk0iK6lT5i13yRcZvgJCaIjvVpVVrRA0KdC1WwG21lLXIIbahgpMQWK2Sa2P6EE5xrbjq1-zi9oyllNvfsyX3NHw5NhkAp03KEIRBz6s5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ ۱۱.۵ هزار نفر در اروپا بر اثر گرما
🔹
بیش از ۱۱۴۱۸ نفر بر اثر موج گرمای بی سابقه در اروپا به شرح زیر جان باختند؛  ۵۴۸۶ نفر در آلمان، ۳۱۶۱ نفر در فرانسه، ۱۲۲۲ نفر در بلژیک، ۱۰۲۹ نفر در اسپانیا، ۴۸۰ نفر در هلند، ۲۵ نفر در انگلیس، ۷ نفر در لهستان، ۵ نفر در ایتالیا و ۳ نفر در رومانی./راشاتودی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668876" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d862411b.mp4?token=g1VQLbVuXAAmQIJvjmLeOQCapX5u_Bo7Aqrm25XwtQmMqE94WbiLb-qvQwGV4wQAkxpfeZPn4tjjWoELKpYG6k56OLDZxt0Mw_xh4BeZWC4ShgbfkyR9ecwOudW2agW90LnGYyqaBy4CIfvQhMOiFLKR9CLe7Vo4zlXMW4IE2tJpdbioLX9NROp_XhCXH53ph-dEUpGseuMoLjs88LBYEIJrDt9_dnWL2Fh3ZUFb1n8UnorkfPmGnphDchtmfpP7fdiz3_iWbfai2pCzw_7gMEF_WwQ2OetaKb1Ahq12Xd4ay9e9LCCey83izH1jq3_O9tF4EuSeWgg44DJ1rlmO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d862411b.mp4?token=g1VQLbVuXAAmQIJvjmLeOQCapX5u_Bo7Aqrm25XwtQmMqE94WbiLb-qvQwGV4wQAkxpfeZPn4tjjWoELKpYG6k56OLDZxt0Mw_xh4BeZWC4ShgbfkyR9ecwOudW2agW90LnGYyqaBy4CIfvQhMOiFLKR9CLe7Vo4zlXMW4IE2tJpdbioLX9NROp_XhCXH53ph-dEUpGseuMoLjs88LBYEIJrDt9_dnWL2Fh3ZUFb1n8UnorkfPmGnphDchtmfpP7fdiz3_iWbfai2pCzw_7gMEF_WwQ2OetaKb1Ahq12Xd4ay9e9LCCey83izH1jq3_O9tF4EuSeWgg44DJ1rlmO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت کویت پس از رسیدن موشک‌های ایرانی از دوربین های مدار بسته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668875" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پست بانک هم به بانک‌های فروش ارز اربعین اضافه شد.
🔹
العرببه: نخست‌وزیر قطر و عراقچی به‌طور تلفنی آخرین تحولات افزایش تنش بین آمریکا و ایران را بررسی کردند.
🔹
رئیس سازمان سینمایی کشور: مسیر تشییع رهبر شهید از تهران تا مشهد مستندسازی می‌شود/
ایسنا
🔹
شمار قربانیان زلزله ونزوئلا از ۳۸۰۰ نفر گذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668874" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
احضار سفیر انگلیس در تهران در پی اتهام‌زنی علیه ایران
🔹
وزارت امور خارجه در اعتراض به اتهام‌های مطرح‌شده از سوی مقام‌های انگلیسی علیه ایران، سفیر انگلیس در تهران را احضار کرد.
🔹
در این دیدار، ضمن ابلاغ اعتراض رسمی، از دولت انگلیس خواسته شد ضمن توقف میزبانی و حمایت از شبکه‌ها و افراد تروریست و خشونت‌طلب، از پشتیبانی همه‌جانبه از رژیم آپارتاید، نسل‌کش و تروریستی اسرائیل که بزرگترین تهدید امنیتی برای صلح و امنیت جهانی است دست بردارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668873" target="_blank">📅 10:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eebbf341.mp4?token=Q6c5uGVU-q14og-FfdLNT_9zJcSGJh0-ENWb846-2XGt49sOET4MvQTjsTQ3D-jHuW2WFrwme4a_SsPf9WMxi9I4nhN7tFUQX5F1S4sL9nOP40Aa_niMxPiBh67tNgVB1GfpP2YYVQzrdcBKoLsEZ5PsWrBir772IQy5Su8hSUaS2DpBMIf6TISv7vlg32B7w5EEyIdhKFbThFcIwXEVnXPjw2ZC104zNFPTz3zgutVni-7J_Ua9v5SYFXdH9AihtUw1JbpgJ0AFzzVeJb6p_53DDKMPojC8ctvIS2hFUh4DOnVX57l8vi6M_KD4E4TYZy5id3CJ-EiqlyhYjX_PqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eebbf341.mp4?token=Q6c5uGVU-q14og-FfdLNT_9zJcSGJh0-ENWb846-2XGt49sOET4MvQTjsTQ3D-jHuW2WFrwme4a_SsPf9WMxi9I4nhN7tFUQX5F1S4sL9nOP40Aa_niMxPiBh67tNgVB1GfpP2YYVQzrdcBKoLsEZ5PsWrBir772IQy5Su8hSUaS2DpBMIf6TISv7vlg32B7w5EEyIdhKFbThFcIwXEVnXPjw2ZC104zNFPTz3zgutVni-7J_Ua9v5SYFXdH9AihtUw1JbpgJ0AFzzVeJb6p_53DDKMPojC8ctvIS2hFUh4DOnVX57l8vi6M_KD4E4TYZy5id3CJ-EiqlyhYjX_PqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از مشت تو تا آسمان...
از مشت تو آرام شروع شد...
بر مشتِ عاشقان نشست
در حرم‌ها چرخید
و سرانجام بر تابوتِ سبزِ شهادتت آرام گرفت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668872" target="_blank">📅 10:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرفوری
pinned «
♦️
حملات هوایی آمریکا به ایران ۱۴ شهید و ۷۸ مجروح بر جای گذاشت  وزارت بهداشت:
🔹
‌در حالی که آتش‌بس برقرار بود، آمریکا در روزهای ۱۷ و ۱۸ تیر ۱۴۰۵ پنج استان ایران را هدف حمله قرار داد؛ حملاتی که تاکنون ۱۴ شهید و ۷۸ مصدوم بر جای گذاشته است.
🇮🇷
✊
@AkhbareFori |…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/668871" target="_blank">📅 10:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b40dc471a.mp4?token=W03VEdaw5FCMGB4rWwQnbLpM_zBmb6RkGtmPTIS3gSc0Kuulkru0mEquE3VQfJ9sUpMqLwRg0Qn2ibymKXvTBX6T0MWIweAaFnJBO7kGK3YBjICRaocePH2rSyyHR5n3IMQNUvo66txlZ49fSbhXqWomyWNw5YePewT7svGWcRQnKGQO0Ys3F2UHOlwN1zA7LWJM2y_MJG4nHWyCLSXg-k5bN1RhZ_9PkDN3ougePF533vzK8cjTAUjDCLbITRQqr6-8D4UVBZYSJvU5WZZRB_SMlA8-KAY-Pf-aiD2pzNZihBmxvIMyM6uc5KWYvRYxmGGH97cPSOS3KDt0pgF0lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b40dc471a.mp4?token=W03VEdaw5FCMGB4rWwQnbLpM_zBmb6RkGtmPTIS3gSc0Kuulkru0mEquE3VQfJ9sUpMqLwRg0Qn2ibymKXvTBX6T0MWIweAaFnJBO7kGK3YBjICRaocePH2rSyyHR5n3IMQNUvo66txlZ49fSbhXqWomyWNw5YePewT7svGWcRQnKGQO0Ys3F2UHOlwN1zA7LWJM2y_MJG4nHWyCLSXg-k5bN1RhZ_9PkDN3ougePF533vzK8cjTAUjDCLbITRQqr6-8D4UVBZYSJvU5WZZRB_SMlA8-KAY-Pf-aiD2pzNZihBmxvIMyM6uc5KWYvRYxmGGH97cPSOS3KDt0pgF0lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر عراقی در مراسم تشیبع امام شهید در مشهد: رهبر شهید با شهادت خود و خانواده‌اش اسلام و شیعه را ثابت کرد
🔹
آمریکا و اسرائیل هیچوقت نخواهند توانست اسلام و شیعه را حذف کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668870" target="_blank">📅 10:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765487a4eb.mp4?token=OdiE94iRErEMXiOGZF422P2cBtkrJbadc7C370da5GxbNojbSpvo03Tj7QLrX4cBquuucD6pGRDoeWTG3MMiKOG0el6MH59D04KbkP9EgA3EGuhTiP4jQgwqM-j8o1BWQ2fEqsFFIEc9WIENS8tByfN9DOPzl8qPgPl_F9t0Gxb9eddPIvgFUt4-qmtKzHlpvXUagKAH9ukUWJQBMIP11ZIk_qELfeka_hb_u0EtKW_viUugoPwO0UFVdnBrVLgQnh_MeNekY5amgJLQxR_ACpn30aO8cMSQLpcUqB_LTmd_FqKMVwhWWxaYfK_ycfK1FG2LDJDE-UPWsRqd-TWvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765487a4eb.mp4?token=OdiE94iRErEMXiOGZF422P2cBtkrJbadc7C370da5GxbNojbSpvo03Tj7QLrX4cBquuucD6pGRDoeWTG3MMiKOG0el6MH59D04KbkP9EgA3EGuhTiP4jQgwqM-j8o1BWQ2fEqsFFIEc9WIENS8tByfN9DOPzl8qPgPl_F9t0Gxb9eddPIvgFUt4-qmtKzHlpvXUagKAH9ukUWJQBMIP11ZIk_qELfeka_hb_u0EtKW_viUugoPwO0UFVdnBrVLgQnh_MeNekY5amgJLQxR_ACpn30aO8cMSQLpcUqB_LTmd_FqKMVwhWWxaYfK_ycfK1FG2LDJDE-UPWsRqd-TWvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غبارروبی مضجع شریف امام رضا(علیه‌السلام) با حضور رهبر شهید در سال ۷۰
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668869" target="_blank">📅 10:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss74xaqyHzR7-UFP1zpsZV6IQN2xd5ceKT1Q5PDFnyerf0TBNJz-zhlbahzABxcNUyMoxAepPYI70b8eDq13HTzf0JtED9kbQWofTfiCvpONJE_L9f6ANgvBc6yF0ct9WLcquSxxeazCAmpWp24CwFnlTnrTAYh-bGdkuFW2X-k4D3Wh402dYEekbuWNZoGD2wptaNw-lXXsUDMGfMP2oqkENJst1TCh5_HhskxqJwxwhS-6HnvsPfJdyY4ZsD6GV3_LuWPkOs0HmlIXo_ua2u6umBYU3fTqQ0Y9K_V-WTwDG00cWw5ZmV8NIjGCzgFD4ILWxOXkDz58ptGnisLtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ما بر حق خود با اقتدار ایستاده‌ایم
رئیس جمهور در پی تجاوز نظامی شب گذشته آمریکا به ایران و نقض آتش بس در مطلبی در صفحه شخصی خود در شبکه اجتماعی ایکس، نوشت:
🔹
«رفتار دولت آمریکا در جام جهانی، نمونه کوچکی از همان الگویی است که در سیاست خارجی دنبال کرده است؛ زیر پا گذاشتن قوانین، زورگویی، ایجاد مزاحمت برای دیگران و تقلب کردن. این تاکتیک آنها برای MAGA است.
🔹
با ایران نمی‌توانید اینگونه بازی کنید. ما بر حق خود با اقتدار ایستاده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668868" target="_blank">📅 10:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سردار کرمی: سپاه و ارتش نگذاشتند تروریست‌ها قدم از قدم بردارند
فرمانده نیروی زمینی سپاه:
🔹
دشمن آمریکایی - اسرائیلی گروهک‌های تروریستی را در جنوب شرق و شمال‌غرب ایران برای حمله به ایران کاملا آماده کرده بود.
🔹
سپاه و ارتش دوشادوش هم در اقدامی پیش‌دستانه مواضع این گروهک‌ها را درهم کوبیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668864" target="_blank">📅 10:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqZwJ1dB8_oFklLN_aB7AaS0Qm0144zxZFm22XlmKu7IO6108yoaQoNVq1d8bFdpGQcCnu13MP7oO81gipDiYEIKHoMQ0iV5K8UNuMw-ss8OEbheAFGBvTsaTsB-_4u1vnLA-CLMB-PBwzM6GOdBaYr8Fd3QCOslBZujUE4Mxhgy7yQc_lLy-lmyH3l602pUngjj3jCm5vJDUHgVRju4TUHOoFV-BQ0VJZihw3sj34k-w7F1ccFRKARiF0tFyBalqWsKsdN6DU7PUx6Fju72ysKBw-V5FKWecjEVTvCrIWcaYrku0dWBsyugj03-RQ4EboKO4-aYSLqo7V9Z0uvD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد در مشهد: به سر بریده ترامپ نیاز فوری داریم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668863" target="_blank">📅 10:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk3mWsUP55qDE70fyroAaUf1eMKM97YZx_SK67vhikUwSgmaW1g7SF-FCIjnGe_ueW7t5J7n3Ytrq7CZqJUMkfM3q7ScGSE7G3IAJbSslaFtUjrWuePqS8pM1VT2uDQKDp79-ZnT9SDNGCF2jCRMX2EewuHqFOwteyiTdM03ecuYTT8Vk6RE-METrh1hxqwj_Pt5UUw_Nq8L07ixMQsSJa8v7nsyYWFZ05QbTNr5u4ig5VBTap49tWGyn-BKd5nbN0ii-SzT3b68h8qXp_2L5x2-GrZCOOb-lg7asrjgikPGbZnrcavPA2fU9M0TgXWaJVuNZfYu1VnxGdLqESlW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ شانس اول قهرمانی در جام جهانی ۲۰۲۶ از نگاه اوپتا/ فرانسه، شانس نخست
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668862" target="_blank">📅 10:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a9e37ad53.mp4?token=tZEVUPgNdQZ1F1CzBxCYtoH5CANukg78tNvGXY4jq9-iasTFVYjBR_-YDf6hfMvHR8xro5l9DsAXOthpKBG7EXiaV6OOfCmMJH1r0w9WWQtEbyoZRWkXWFkxZwTKHQpEWfaBk_4K_HwaxM_x5l8ZUd3j5lEQRfY7Iy2GfR3Az0MmLJeuuXO-ygLMW60hTdKWaQEoo5Y5nN8KmeDa7JO4-RyKTmp_EXG-sh5ERLoWzKOyNDo2u66-PiQmgIYAr9o7p3FJpgWT4lPa6RFOW8Q2YQ7NZlljRPtRmwH87tg4JmDX_TpUWYj5WmuD_XZ99N7mHcQp8j63uX0No7cwzcoNi3tF9fOxTAwn7LiYLv2hxOmuUmE2FpfRknIsN4jdlRRXKebrVxVExl97GSSqDQ2uAWYKVmSh54S-nLp40ZT73axQ3HI-fc9y2mTwG5CYmo9SKWqmLhlUPaUCjeu6zfNDLxKFzHwsFOChiFYN2aygmjXaGytwb7irKsj5aOLVm9rkXlk6DegRevoKHUgHZdhnE-iy0S1ypwF29CoiGPiWY2c7VRFEUqN5j1-kd6l2SBW_HCLtkZK7ZnmWf8Ojda5LJRByme63WzvqfIxRLVzYgE5ewKQDVQkmTb-7g-eI3ROnIFcLrqoNDnGY51idTudw_G37fLNIjEW3etJfTvLkwUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a9e37ad53.mp4?token=tZEVUPgNdQZ1F1CzBxCYtoH5CANukg78tNvGXY4jq9-iasTFVYjBR_-YDf6hfMvHR8xro5l9DsAXOthpKBG7EXiaV6OOfCmMJH1r0w9WWQtEbyoZRWkXWFkxZwTKHQpEWfaBk_4K_HwaxM_x5l8ZUd3j5lEQRfY7Iy2GfR3Az0MmLJeuuXO-ygLMW60hTdKWaQEoo5Y5nN8KmeDa7JO4-RyKTmp_EXG-sh5ERLoWzKOyNDo2u66-PiQmgIYAr9o7p3FJpgWT4lPa6RFOW8Q2YQ7NZlljRPtRmwH87tg4JmDX_TpUWYj5WmuD_XZ99N7mHcQp8j63uX0No7cwzcoNi3tF9fOxTAwn7LiYLv2hxOmuUmE2FpfRknIsN4jdlRRXKebrVxVExl97GSSqDQ2uAWYKVmSh54S-nLp40ZT73axQ3HI-fc9y2mTwG5CYmo9SKWqmLhlUPaUCjeu6zfNDLxKFzHwsFOChiFYN2aygmjXaGytwb7irKsj5aOLVm9rkXlk6DegRevoKHUgHZdhnE-iy0S1ypwF29CoiGPiWY2c7VRFEUqN5j1-kd6l2SBW_HCLtkZK7ZnmWf8Ojda5LJRByme63WzvqfIxRLVzYgE5ewKQDVQkmTb-7g-eI3ROnIFcLrqoNDnGY51idTudw_G37fLNIjEW3etJfTvLkwUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرفوری از مشهد؛ آخرین وداع مردم ایران با رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668861" target="_blank">📅 10:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668856">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh5eEPCLc8F1jQ3f6PYOk13_vWKsL944iVsLMU65U9Twh79vC5GnwrJi-_0ED_CdDeMiF5f7QUq0cfI_jS3OT6sm2i5fOvDfWCUCAW3K-rRr_5NE28DkgOUPob6hBf_PWZkUpARJCzHZ2sRisBG78UPrd3pmYgV-OG4Nfz5w56kmt9Upd5zEgI2yDu6aUmMtiQwGRoNrHqiNFufRIAcu6IvBOiBKm8LY6R4oq14pko6aD4ArYKDtF1s2Vy2ZhWcbcX4KJpqtalzqG8Mn1n3RmMg2LEc4nhzQB0DCJEygvNaBgXNC_eEw9kMeNDwbK3RwK1FQu1MrxvhRJJd15XguQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8yVlz9Hif6TzhQrad2uwD95J0qVRGchnehuTqEmoGFXdLx_8DPYpCii1c5mQL2EF9Iad1lSFRTRyv-0j04ZL6XlEXVryDqtVL7tlbK_TEmLVLIMVW5m5ZWKgHjg2zc-gJCaYofFDECh3Dp371GyX8ZOrGCGV1AyjoiP1SK6z-gN9sXABx3RlzGd6e2X28aBZBHG0m_Vhkki_tpEGyqpZefHpT9huYXDctxq2YfvugMjZwKxmjA42IArEQtdQWqMrocpBSZyGp8FVOVjT8YZy_CZsr4M492S3xAsnWFIYGbEp_h50gLT7FxQqrsRP7rLjoLpyOt8Jpn3AhRDCvRKaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2021ebce1.mp4?token=P8eRJ_VnC4GVCshbOVRg-UTp1ATw2t3uz6_mCEJ1-jv9EILDdg3ciE-T1YXG2qNJr4yIMTL5rMPPshkxykw_o6D0kYXViElxd9Ws6H9yZ_6FfSN-EJbZLVQzK6kkNAgaY-gaVUHABujXb02U62Bwq7DYNucJPU2M34IpFVpOjd3zk4KSb4iiPkH3J09oTnPikSXkxRi0DpfF6hVy_1K0D5Gnj9mVQvGA-cng4xiTOc834aaHBNYMvSb6D4WeonTx5XqhuJFK1pBrsIUfhNOgrrQZd6T0YpwvnLovmDURQyqB-B2Pu54ZcJwwjreDsf7ITSU8D6a_vLtE0HP0jLKtPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2021ebce1.mp4?token=P8eRJ_VnC4GVCshbOVRg-UTp1ATw2t3uz6_mCEJ1-jv9EILDdg3ciE-T1YXG2qNJr4yIMTL5rMPPshkxykw_o6D0kYXViElxd9Ws6H9yZ_6FfSN-EJbZLVQzK6kkNAgaY-gaVUHABujXb02U62Bwq7DYNucJPU2M34IpFVpOjd3zk4KSb4iiPkH3J09oTnPikSXkxRi0DpfF6hVy_1K0D5Gnj9mVQvGA-cng4xiTOc834aaHBNYMvSb6D4WeonTx5XqhuJFK1pBrsIUfhNOgrrQZd6T0YpwvnLovmDURQyqB-B2Pu54ZcJwwjreDsf7ITSU8D6a_vLtE0HP0jLKtPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور پرشور مردم ساعاتی پیش از آغاز مراسم تشییع رهبر مسلمانان جهان در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668856" target="_blank">📅 10:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668855">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtlVEXBxjiIllacGNyr1sbwkp5dofWhDhWWTynY_0YpfHdr_rdI2jlr2Fr4rci2IHp8G1D0NpIvYLFBQDR4fpRyBHD_iWOBlzbj52yK5egRzLMZ8Q50jonMa-Q19aag_ZonswiVFdLDtsusyKylyeDAcoLTbpGqK02k8GWPtrpkAp7coFL66fCwWfLOmQhw3bqYtJPh26hkuXG8ZxMAbACVqddkkkaWC0KfyalAcm6ir2MIWGA64OpAWuvttQj2wSv7HUKTE7weow_MKSbj5Xtp1Zskf0w5Z5QhbmVGwxZ_f3_Um69PxEgiaR9lXIyq0lWf_vRj79szzMOwDDteGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/668855" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668854">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f33312e2.mp4?token=j9EsWGjZR5NFcAl6E9VWEUXAZuzwOxUz3KfoAYWo3mg0qbS28UCpIlrfbcr19Dz1da35MClsCxS7QMH62kV8X2L3Uy9JY5RVzlBSo4kYNtOgP_vAtaNEjg_nZcLf_RPJEcLqtTVv2M0AQra0dR0VEV_LawJbN7wq9In7ZA9fZoqOOPmD3ju9v-IRjb823Zch0iQEALG4OiwYGyHEGlCcr2baLWgBejhQ3r4a8lYGeGMlbN4qE8hw-cBoNsDkwvAe3hToROkyp36LzBC1pq6gRwhBx56-StPLIAahS99nvFr_4gHaKH22GIhUREi2rV3aX8dSkBKS68iryrM-l0bltWxhPnkhEkv7fSdn3huoAd-mgorFyBcIMcD47XEHzuIBzzWdUURbvAKX-aKF49_aSt-CGuB-fD2vzHkKhthsyhvyC5y7gL9gb8RbwaqUJaKnlcj2Crb628Uym6f5wAPiIoojIbo9OkGwtLSoNx64_haAkj9CGa_X2L1qBbqpmxpNovf3IkHqO8mNL8lYwhVWV9Bo3HiPLd5YS88cmphxYjlr8LtNe45LSGSkDaOQXt3EYW72M8g4u_yGi6r7wT8oAKcikbs-uydoSqUIrCGurphrt2QWKuiMNB3VMsI7CzzWDFNHYTfi2pAS4S8GsWRBPfsBJJ1Dtdt1KkRTlEKNAKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f33312e2.mp4?token=j9EsWGjZR5NFcAl6E9VWEUXAZuzwOxUz3KfoAYWo3mg0qbS28UCpIlrfbcr19Dz1da35MClsCxS7QMH62kV8X2L3Uy9JY5RVzlBSo4kYNtOgP_vAtaNEjg_nZcLf_RPJEcLqtTVv2M0AQra0dR0VEV_LawJbN7wq9In7ZA9fZoqOOPmD3ju9v-IRjb823Zch0iQEALG4OiwYGyHEGlCcr2baLWgBejhQ3r4a8lYGeGMlbN4qE8hw-cBoNsDkwvAe3hToROkyp36LzBC1pq6gRwhBx56-StPLIAahS99nvFr_4gHaKH22GIhUREi2rV3aX8dSkBKS68iryrM-l0bltWxhPnkhEkv7fSdn3huoAd-mgorFyBcIMcD47XEHzuIBzzWdUURbvAKX-aKF49_aSt-CGuB-fD2vzHkKhthsyhvyC5y7gL9gb8RbwaqUJaKnlcj2Crb628Uym6f5wAPiIoojIbo9OkGwtLSoNx64_haAkj9CGa_X2L1qBbqpmxpNovf3IkHqO8mNL8lYwhVWV9Bo3HiPLd5YS88cmphxYjlr8LtNe45LSGSkDaOQXt3EYW72M8g4u_yGi6r7wT8oAKcikbs-uydoSqUIrCGurphrt2QWKuiMNB3VMsI7CzzWDFNHYTfi2pAS4S8GsWRBPfsBJJ1Dtdt1KkRTlEKNAKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورودی صحن‌های آزادی و انقلاب با عکس‌های رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668854" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668853">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR6YF2UOwueDCxCYEav2IPKPBfxuMpuOFaWKaMP25QQfj7V-XUZ_t7SMjQbap0yDyx8x7pOqCsxeAip8xNG3lru1mZwmVjKW3gXr33euWl21F4aUAHaDIdxb0AM7xXx4S5YbDGhqUQrABH9Ojk383VCK6i1oxRF9X2Yjw2krtvfhSDCnXUHqH7YPKu-iQPu156apeDZrJgCqDO5kjVD6HFoDDA6AvrWjJliWkr47FnMcP48cMS8vf3bxb_ujbAWhcipvejcByczHO2GTo0ECuc82ZN_ZPI_5-hbH2iGuNwwWAxh6x1XaxOkQStJikxC6s6M-8n3eF249lRps41UWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
فرقی نمی‌کند؛ روی فرش، روی خاک، یا بر ویلچر...
ما را داغِ شما به اینجا کشانده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668853" target="_blank">📅 10:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فعالیت موکب سازمان منطقه آزاد ارس در مشهد مقدس
سازمان منطقه آزاد ارس طی این روزها با برپایی موکب در مشهد مقدس خدمات مختلف پذیرایی، اسکان و تکریم به زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید انقلاب ارائه می کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668852" target="_blank">📅 10:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حملات هوایی آمریکا به ایران ۱۴ شهید و ۷۸ مجروح بر جای گذاشت
وزارت بهداشت:
🔹
‌در حالی که آتش‌بس برقرار بود، آمریکا در روزهای ۱۷ و ۱۸ تیر ۱۴۰۵ پنج استان ایران را هدف حمله قرار داد؛ حملاتی که تاکنون ۱۴ شهید و ۷۸ مصدوم بر جای گذاشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668851" target="_blank">📅 09:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668849">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br523zMhZjtjJ9ghmj5PQO91JLXa65DaHvSJBA1vfTs8bzLFqPK-JmIZJydIoj96HGg-jqwIwhSOmtKLiStVue-d6jAF1VLR-t-bMcQW_MFTBmz8VNxrqP_wgX8eNsE3xWPntMrRu6wgcKIhjuQDYk0Hyg78VOdDTYp18DOsqNbdfakoqBEf8dLVRe0ipsY85txg77C4wGXE21xUM5FKfFWUtLxtAXJWuHELcCjlYH20fOpisWrfihtosJyf4lwus5F3Dw_3pIhjcBk5R8JoapyQ5FGHGG1ayM-JTG50ny3msihxi8ajD1RKqgqGiVyWxSvZ6zY8xKPB0oB2ZRuMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvdxuR207NfB_nPh21HNTwOzKByo8Cv8-4CwL-nvg_zPMkSUMQZ7pSAVNaeHhlBXNAucSMikrzLJGG3oQsn5-_0ffdeETLgXDy7v-fdoWPaeUK7inAp8xr5jv5fjW58Yqf-lZoPV-lR4JLejsZzMIKldScrwVFngOaTmnBZ5ivHOSorHOlDH-97mCPlzTka1INxwqlOxlzDDV7-81wYGz7U74m1lUcR91nfZAwJzR-Jl0Q9fZknqD9OA-X-qncNqe_VbB3qqvJj9wAt539t_XOzm4e1UnoMZlUWTO7sQtpXSAP8BvYo1zQu7ULL_FrRogaW39lb64BGnJUfO30jXiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری از برج مراقبت ترافیک دریایی بندر چابهار، قبل و بعد از تجاوز دشمن آمریکایی
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668849" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668848">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9d2cfe2c.mp4?token=n82lG_z1G5iCZEn63nWYy0BS699g7mW9VUNaYS3fCwxBZkWqw1im4aklxzNoPTJ_RETnyB6cAqCHQtWp0YJo9uPqqldynDT3RVhJRDIQFEBUZ2XKBgI7z-Uheoi01gmSyeTQjOGnYFRMig_BAWJBsNf4X3IdLru7o2xhhmDqybTIHPW_BXcgLYzbmbif-ZE9T7eZNWA83XV9pxbLIWCx-lD4sVyCy9vv8X2LVETnl8g5NAGuAZrqshko-g_fhs-fXZgDKx5SkSEKX8Sgonx-auAASMvvDruEDDP6uisR7mOgUIFbQZGC8Gzj5dODslZc11fbvT6a57L44jdVeSemXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9d2cfe2c.mp4?token=n82lG_z1G5iCZEn63nWYy0BS699g7mW9VUNaYS3fCwxBZkWqw1im4aklxzNoPTJ_RETnyB6cAqCHQtWp0YJo9uPqqldynDT3RVhJRDIQFEBUZ2XKBgI7z-Uheoi01gmSyeTQjOGnYFRMig_BAWJBsNf4X3IdLru7o2xhhmDqybTIHPW_BXcgLYzbmbif-ZE9T7eZNWA83XV9pxbLIWCx-lD4sVyCy9vv8X2LVETnl8g5NAGuAZrqshko-g_fhs-fXZgDKx5SkSEKX8Sgonx-auAASMvvDruEDDP6uisR7mOgUIFbQZGC8Gzj5dODslZc11fbvT6a57L44jdVeSemXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی دیگری از شور و حال وصف‌ناشدنی عراقی‌ها در تشییع امام شهید؛ دیشب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668848" target="_blank">📅 09:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668847">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
هیچ تغییری در ساعت تشییع پیکر رهبر مسلمانان جهان در مشهد ایجاد نشده است
سخنگوی ستاد استقبال و تشییع رهبر شهید:
🔹
علیرغم موضوعات مطرح شده در فضای مجازی در خصوص تغییر ساعت تشییع پیکر قائد امت در مشهد اما تاکنون هیچ تغییری در ساعت تشییع در مشهدالرضا ایجاد نشده است.
🔹
مراسم طبق برنامه‌ریزی از پیش تعیین شده در ساعت ۱۴ برگزار خواهد شد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668847" target="_blank">📅 09:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668846">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4618fd4290.mp4?token=iaaW0iNloHc1QvyZB0NTMM0VEWMTB1Qj5-anaA4pPmO9q-ImZvSNWBysMZ7Tj4GBMQPWgcF6q6P-Iillju9i-ARof6Mclw2oeGIZTCgPiCPtzEzNrTmU5iKaYMYMYMtqtA2hj_ILppPEJd5_-Gw0t8CjfrF4syWOo_e7qaDylgP9Z5wVPsE7qXH9ZwubhRhyGDJ057ynod4_HacBhPFG-Erf1s3AckO-Z1JoLcZ44Vni0Xg-uofCiqbDAi2kif5aSjhPFttfIcLYxmdr_XiocA-BC0eCYG9-pZkNiWgO9aJXo0rag3pSLX1ow-HLWatt2FDQi4kRVlhtoOIEQZv8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4618fd4290.mp4?token=iaaW0iNloHc1QvyZB0NTMM0VEWMTB1Qj5-anaA4pPmO9q-ImZvSNWBysMZ7Tj4GBMQPWgcF6q6P-Iillju9i-ARof6Mclw2oeGIZTCgPiCPtzEzNrTmU5iKaYMYMYMtqtA2hj_ILppPEJd5_-Gw0t8CjfrF4syWOo_e7qaDylgP9Z5wVPsE7qXH9ZwubhRhyGDJ057ynod4_HacBhPFG-Erf1s3AckO-Z1JoLcZ44Vni0Xg-uofCiqbDAi2kif5aSjhPFttfIcLYxmdr_XiocA-BC0eCYG9-pZkNiWgO9aJXo0rag3pSLX1ow-HLWatt2FDQi4kRVlhtoOIEQZv8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمای حامل پیکر مطهر رهبر شهید عازم
مشهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/668846" target="_blank">📅 09:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvQI3isCujD6Hrx5Ax8OswjAKkrSZUOcLNqEzKYmek_XvZdLUWdgmySu6iWkuFGn-ngOndGiqG4CHvfnkyIgRD-GDbRCz9nTOy-xRwvTxCRtK0LFsbSUaQbO46CqKIqabH6IjuOIlyIgiKhqV3BoyecerXk1UsqX5mPTZVfIz_Vda0HdzVR43OZxyNMNBAqbBL71GhvrGZREf-rrUyn8axSpMO_K4F5asu_qTHXJohDc_J4Eixctq4YWXqSP1GRCIW8Hx7O1B81xqoWvADTIGtjA8u3ewvM0UwEPM1SaAmP0WgK0j6rgsuqVZj5OKWvoyiaISERKG5PDiypgBUmrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3BHCfLZgOSd7R1Ejxkrniyf1qbNyjZi7AwHO2UApCEBbu-9jdiA04ipcdAmDQsEaLBLIhnoFptFcYMGXhEMtwf-ORChorprR-XlmMbNhIyoD1KDZPodjjwj0XnqYW2-1ovaSUdRoviCOrSaTtcwvW3flmelASI3Kh73kJkj7cPqE_N_cCA_BinPo4dy54rzbrOK99P9pwO7Vg3xsWii0h8KkDu9no93SdLzzIbUQa_fz4vmr0pFtFqPcXGgdJpL8elQfxfEWkAFom5PVuKU_uk337cuMsnpey2OT6YU4BSB7_FnjraDHtHyCySmveOR4UjMWcDJBrQTjr-iAgvKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKgVRlh9Z9fObxDkbRfrkKLQu8IojJwbGs0p4YBNMeAtBPf3ZlZILgSYdivhn4NN4f6tm2Br5QPhLHQIRmyMtUmmf92vEonSoh065LT8AX-xPJFYI-S32mvb-ubBQK49h7kzB2FrDQ_71cbskpDYQFXlyGxv_R09QTT76Ag6yi5DdNI40Vu7EQvnJStRW1l-6BMCjgN6ybwhZ469N7LOXsB8VUzx2gF6Xgpv2y5Bk8EQh_yoTLqMp2nXuY-jK43v2Co__z6v9SMp_7zBuR1mft_oLl1I-jwcFk6rZHNqChElCQe0Sjmguz3kbi3FThJZp1lrQpCp4Vj9oF_CWTNrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evukdX8wP603831CtFtJ1E60InlsfEwL2wa1pWexKO2uq4XCrBmRIyyP44uvqjVRmL08bEWz2aH65v5McNae5lfQv51zt-sJtrYyea5MJyfNQCTNDQn5TGYJF437FGKX9qf0D8aMPJ27NH_cVuGZ4iqNoRf5ZiMr66zb4cZltzfCqnQRjUtSZVnjFxHpbqvrLxJsBAhtMl0bb_WDQnGHGVQvZTizauba9TZj0kADLaNe1w1jG6gz4GYdgLqlMmbod0e9n6p7fBwDd_RgRsujaDJwNPkA9ydvbNuWgCyOahtvPLSqlaXU0QasbUx1ReuKyqobkFGGoKd7J9-870NteQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045c681ed.mp4?token=OhFrfO7x1O2Nau9_aNzeU6iEkEI7Ha9PPmLf81pEAlyWhyQGRyKPb1BX5c51pHnvm55dXI1L3nZYMuv4JSJCq6fKpLYoG2S6D0BQS0BACTY0GVef0TiYMqSeHLB5tbF20S8gaN4lF5t2B5cqF-Tlf_y2lp3qxlTN7ZJXWoKtL7GWGlGqbw4_B_Kjx6v7QVatGoSzh038d7RIzlJOR3ueWFue0ARmx6gJLUgPcru4BFy-7e09rQxgPDkKJr4RbHzoUsymdnGRW7b3ipMwtDzJfqFJz0skZZjd5KhpojpeVLur-AjGDm8wIl-JWnG8NmJQYuLtCw1X_kF9Mi2zVW631w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045c681ed.mp4?token=OhFrfO7x1O2Nau9_aNzeU6iEkEI7Ha9PPmLf81pEAlyWhyQGRyKPb1BX5c51pHnvm55dXI1L3nZYMuv4JSJCq6fKpLYoG2S6D0BQS0BACTY0GVef0TiYMqSeHLB5tbF20S8gaN4lF5t2B5cqF-Tlf_y2lp3qxlTN7ZJXWoKtL7GWGlGqbw4_B_Kjx6v7QVatGoSzh038d7RIzlJOR3ueWFue0ARmx6gJLUgPcru4BFy-7e09rQxgPDkKJr4RbHzoUsymdnGRW7b3ipMwtDzJfqFJz0skZZjd5KhpojpeVLur-AjGDm8wIl-JWnG8NmJQYuLtCw1X_kF9Mi2zVW631w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
چشم به راه یار خراسانی
🔹
درحالی که حدود ۵ ساعت تا آغاز مراسم تشییع پیکر رهبر مسلمانان جهان در مشهد باقی مانده، خیل عظیم جمعیت مردم مشهد، ایران و آزادگان جهان در میدان بسیج مشهد چشم انتظار پیکر ایشان هستند.
#بدرقه_یار
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/668841" target="_blank">📅 09:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668840">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuIsRAQZ6Fe7_2UJcIcnB3i6dtkAQnkAXQbTuTVR0tXi_yHcVogd6d92w1McnLCzrwboLJnsTjpf-dEZs__JOqOKA2MIratG5x3nsAekpB52oN2kIb5gMDfUETMRk0Sh4CvgKHLP2xJLAvkcIYsN_e2-mgtM8rPcLVkdKKOWd9_5_7IehP26H40DcbgKJSr2CTsjXtQq8lbjwXnaenJOGAcuM9oBY07c4n9eYvT5YIXtfTF_I_3elhEBOmpqpzyxjhp6t2mHVSHoi2-fu_pWfxz3pzhR0h_bdCOhwDIpw09lVepbZ_KPD7oH57wwxCGeIWnUtr2FMZPak59nNvaMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴ سرمربی از ۴۰ تیم حذف شده از جام‌جهانی توسط کشورشان اخراج شده‌اند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/668840" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادامه حملات پهپادی ارتش به پایگاه ها و مراکز راهبردی آمریکا در منطقه
روابط عمومی ارتش:
🔹
در پی تجاوز ارتش تروریستی آمریکا به مناطقی از کشور و یگان های ارتش و در پاسخ به آن جنایت،  ساعتی قبل و در ادامه حملات ارتش جمهوری اسلامی ایران به پایگاه های آمریکا در منطقه، سامانه پاتریوت در کویت، آنتن ماهواره ای(سایت اخطار اولیه) در قطر و مخازن سوخت ارتش تروریستی آمریکا در بحرین، هدف حجم انبوه انواع پهپادهای انهدامی ارتش قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/668839" target="_blank">📅 09:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668838">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1bef4c35.mp4?token=XeG8xAULkhZPV8xPZtjaBBozfx_gJYrXNE_XqTp-lYOOZWf68i6V80nyHXDopSRbtf8RFQXhkbUpyehp5ElDvqsAYHwPBi0lCuNdAjupUKWHvzvRs0qadIhSJ01FprgF97M6qnomWDGDYGfpuz6Czve3qlquhZ5mFdGB5BBukGTFobGaGSdEsmFqQ4LnfLMwL1s-WFgigZ8tUNnQDwKW2j6id3rJ-eCnOohpcaehT4L6jB8ubMYvXazRQr0MNm0rz2uLnw1xIiTxzvnL-XBcujGOeqkNpTb1L5xYruoNShaM4xzOlQ88-eNVAXV5MWfKaR-MOAURMim4h7Xf9KbqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1bef4c35.mp4?token=XeG8xAULkhZPV8xPZtjaBBozfx_gJYrXNE_XqTp-lYOOZWf68i6V80nyHXDopSRbtf8RFQXhkbUpyehp5ElDvqsAYHwPBi0lCuNdAjupUKWHvzvRs0qadIhSJ01FprgF97M6qnomWDGDYGfpuz6Czve3qlquhZ5mFdGB5BBukGTFobGaGSdEsmFqQ4LnfLMwL1s-WFgigZ8tUNnQDwKW2j6id3rJ-eCnOohpcaehT4L6jB8ubMYvXazRQr0MNm0rz2uLnw1xIiTxzvnL-XBcujGOeqkNpTb1L5xYruoNShaM4xzOlQ88-eNVAXV5MWfKaR-MOAURMim4h7Xf9KbqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر رهبر شهید از فرودگاه نجف عازم مشهد خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/668838" target="_blank">📅 09:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مدیر بنادر و دریانوردی شهید باهنر: به شناورها و تجهیزات بندر سیریک بر اثر اصابت‌های بامداد گذشته آسیب وارد شده است. یکی از اسکله‌های شناور بندر سیریک دچار آسیب جدی شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668837" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9hncS0xHJ_fuS2W-XreNdiJLtznIc-i-8JPUp0DzIPZirfJHoWSHL226WPdi0pGHh1ATT04dVmfKYP2urQu8id9E6G5j8iVF0-RCNQL6H7k9KdwMc0BIGWMRC_Q-XBig5e25xJqOG6OdwjwTLVffJAqGR3h3DSe51wY2K0qNfA-WUNMpqyqjvpru8p_Z71vcVgA8qDzxoTVFVidDXHGYbjG_fRK0v-EtVWEk9GO8iYKJwjuZiu5SUMp_dZfIeX8xve-_zSKEe1kJe-HpZ3YUhZE3zr6724dlaCoDyWo9bzBiXGajNlFGtk57nV2ZvNHowNcbcVEjo6EKc1680EkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقاطی از کشور که بامداد امروز مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668836" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdqmp8hO7Y0xV6Gt2JT-fGkNqfd7a3hv2lr5mQ8JfuiDD0Vv41w2UQZw2d6xPn3eE64NQu859N-phL3x7ZiQEMU08BGNxMn69osy9Qeuw7_xfxkKJ-GobEaJKIP9hLlKnGQxS4mzSIJxoQPiYUOo-WvD63K0qdrCdwE3pz1tzpjLzODEZ0OPXw0tZ8IoGpOMCeAgc6nlOli4GXTg9R2Hjzl9anmSQ-G1stsG2_sqo8df1KYVAoJ-4PcGdRo8v3C-FQk2bKyRigxZguncNVl-UkVRILBrxtbbwvOQWlxFCqC--VgKLHUBsbq3LctwjEelL7Dp7xumHlJYkRZrKMGylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیر آمریکا به سنگ خواهد خورد/حماسه مشهد تا ساعاتی دیگر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668834" target="_blank">📅 08:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db584baa4f.mp4?token=ohkfLyVdpQsdIWXH7ywX17TWf8KiNRDeNDzCHi_D1KLg-aly8iuKb11j_XDnJq-CfJaMCN-1j1rU1zq6vfWLV9ays3fUUhIcHYTpCyfXikcX1M7KJI6RoQPdGipIDmXqg8ZAmyrp9pd1oCNHR8-CxyYdvFJBa4bYo9NWY-jkEP4dqcgTj1EG5AfDhTM0y2_6AoXvR4JHydNQWb9yh7r7LOwkZ-FwwhLrGeDbuluWnxjlgy39YuW3t3NJ1c3Icj1fR0fAht8Bfm-U2zIpMno2Z4R9hLw6Vcfh4d025470-hXi0qM0YobwKusOXa6kJ0lNuJ6jYgOTsuLVTrViB9_oXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db584baa4f.mp4?token=ohkfLyVdpQsdIWXH7ywX17TWf8KiNRDeNDzCHi_D1KLg-aly8iuKb11j_XDnJq-CfJaMCN-1j1rU1zq6vfWLV9ays3fUUhIcHYTpCyfXikcX1M7KJI6RoQPdGipIDmXqg8ZAmyrp9pd1oCNHR8-CxyYdvFJBa4bYo9NWY-jkEP4dqcgTj1EG5AfDhTM0y2_6AoXvR4JHydNQWb9yh7r7LOwkZ-FwwhLrGeDbuluWnxjlgy39YuW3t3NJ1c3Icj1fR0fAht8Bfm-U2zIpMno2Z4R9hLw6Vcfh4d025470-hXi0qM0YobwKusOXa6kJ0lNuJ6jYgOTsuLVTrViB9_oXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شور ولایی مردم عراق در بین‌الحرمین برای تشییع امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/668830" target="_blank">📅 08:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXzsWSk7k55vVKtdhHS08A9QHuYbOsvic1L0HlI54rhiO_HpY9s27VxzJBUjlLs_o5Thy2HSsyMxl8T3M3p2guXwIZDM6PScstuy6BJtWDHyIhV35DTdaQSxRYuyDWrmZNM3fgX8kxzM7gcPqQpkQ1mVJwwLPckcNcIJ3wg_sDwLKFKveVFR12W8_-7gLyPlJDlRz-dsK0q-0jJ8lY1uQRDqOevb6tQKVZAsNbpJCB3Pl7tNotuJgxOw32ncuIUJaslPBP0ryK8JLmPNJXhjcK-vCU9caWrO5B4IcrD7xSoALvKtrwa4oCsL6YSjDtEWcwsG2UfoBb3y8VPC2iC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران، دیشب چندین پایگاه از جمله الأزرق در اردن را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/668829" target="_blank">📅 08:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5r5LUTBuryxImSBwEjgKh0nfG1VhnHFQ6dp-fkgENWJ3TmubodMCHD_yOVkutIcLlXN18DXye2ydcd9C3BV2lD4WbkOY4rF1vIEQgrFry-4IvWd4nPPn9cv5svlZiJlBZYd9S7y5APLf8hWM_v1IneT-6Q6D7V2v2dKFL6LPiRqAzcLKmpqrssTb7L1AWKzoOXRYmLwKnZjVUegsz9PTU77ePlIMnh44JC-NmAygtSez8k-5UPlrhNmBQD4A4T43c9I8sODgvqgCyHllQkfz08hWPA5dP2hx68Xa7csUDB1twieoNSXgZd3KvSDOoWMGoIJbWWnWnlZiDvYu2y1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پناه ابی‌عبدالله
🔹
٦٩ سال انتظار به پایان رسید. پیکر رهبر شهید انقلاب، پس از عمری دلدادگی به مکتب عاشورا به بین الحرمین و صحن و سرای حضرت اباعبدالله الحسین (ع) و علمدار کربلا، حضرت ابوالفضل العباس (ع)، رسید؛ جایی که سال‌ها آرزوی حضور در آن را در دل داشت کربلا امروز شاهد وداعی تاریخی بود؛ وداعی که با حضور میلیونی مردم عراق زائران و دوستداران مقاومت به حماسه‌ای کم نظیر از عشق وفاداری و قدرشناسی بدل شد. اشک‌ها نوحه‌ها و گام‌های استوار بدرقه کنندگان روایتگر پیوندی عمیق میان خون شهیدان و راه عاشورا بود؛ پیوندی که در سایه گنبدهای نورانی کربلا جاودانه تر از همیشه به تصویر کشیده شد.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/668828" target="_blank">📅 08:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3f576943.mp4?token=iY3chlT0OUKYdu7IYwjZ5My3G2YE-5APTehCvF9Icky5FEoEX_u2q_bRiPiKcMDw1vRa6DpFEqDvjA0fGes5Nc-tJFOiVNtpzM0UiMjqfLseDnrJooALTBp_jsKHzuJ2RmidyqF7bRO-Tkm9qMW-6Kx30fCJBJO99k0OFwjeMmLo85GR0adjaQo2OSL_bhrAqf_rqPVvoPsCZwMobDxDm2z0UDNpC-qucWqcIoNKd3-a7CJZ1uM1MKaQ15_D_NyghIS7-wvLoggAvAUroPcHT2aPnJb5hIKPVoaIH2LZpPydHDDGzV9b6XalPcYUTh8Z3cwYHmeGufRMyD4jaI8OTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3f576943.mp4?token=iY3chlT0OUKYdu7IYwjZ5My3G2YE-5APTehCvF9Icky5FEoEX_u2q_bRiPiKcMDw1vRa6DpFEqDvjA0fGes5Nc-tJFOiVNtpzM0UiMjqfLseDnrJooALTBp_jsKHzuJ2RmidyqF7bRO-Tkm9qMW-6Kx30fCJBJO99k0OFwjeMmLo85GR0adjaQo2OSL_bhrAqf_rqPVvoPsCZwMobDxDm2z0UDNpC-qucWqcIoNKd3-a7CJZ1uM1MKaQ15_D_NyghIS7-wvLoggAvAUroPcHT2aPnJb5hIKPVoaIH2LZpPydHDDGzV9b6XalPcYUTh8Z3cwYHmeGufRMyD4jaI8OTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرچه دوریم... به یاد تو سخن می‌گوییم
🔹
زیارتت قبول آقاجان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668827" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
به صدا درآمدن آژیرهای هشدار در بحرین و قطر
🔹
منابع خبری تاکید کردند که انفجارهایی پایگاه‌های تحت مدیریت نیروهای آمریکایی را در بحرین لرزانده است.
🔹
همچنین گزارش‌هایی از پرتاب موشک‌های بالستیک به سمت اهداف نظامی در قطر و بحرین منتشر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/668826" target="_blank">📅 08:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تردد قطارهای مسیر تهران-مشهد متوقف شد
راه‌آهن جمهوری اسلامی ایران:
🔹
به دنبال حمله جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می‌شود در کمترین زمان ممکن این مسیر ترمیم شود.
🔹
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/668825" target="_blank">📅 08:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
چند توصیه برای پیشگیری از مسمومیت‌های غذایی در گرما
🔹
نگهداری برنج پخته‌ شده در خارج از یخچال می‌تواند سبب آلودگی میکروبی شود و مسمومیت غذایی همراه داشته‌ باشد.
🔹
کنار هم قرار دادن غذاهای گرم و سرد می‌تواند سبب آلودگی غذاها شود.
🔹
برخی بیماری‌های منتقله با آب و غذا ممکن است خود را به سرعت نشان دهند.
🔹
دوره کمون برخی بیماری‌های منتقله از آب و غذا در حد چند ساعت و حداکثر ۲۴ ساعت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/668824" target="_blank">📅 08:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
دانشگاه آزاد استفاده از تلفن همراه و هوش مصنوعی را در امتحانات مجاز کرد
دانشگاه آزاد:
🔹
همراه داشتن تلفن همراه در امتحانات پایان‌ترم تحصیلات تکمیلی، با رعایت ضوابط و تحت نظارت مراقبان، مجاز است. همچنین استفاده از ابزارهای هوش مصنوعی در آزمون‌های نظری دوره دکتری غیرپزشکی نیز بلامانع خواهد بود؛ تصمیمی که از ۲۰ تیرماه و برای نیمسال دوم سال تحصیلی ۱۴۰۵-۱۴۰۴ اجرا می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/668823" target="_blank">📅 08:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668821">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
آبشار گدازه آتشفشان اتنا؛ فوران سه‌روزه پایان یافت
🔹
جریانی قدرتمند از گدازه داغ از دهانه مرکزی کوه آتشفشان اتنا در ایتالیا فوران کرد و یک آبشار گدازه دیدنی ایجاد کرد که به ویژه در شب چشمگیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/668821" target="_blank">📅 07:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMRe1vMGjA5RDKEiKU8bNwYsWBmsPfw_0SqzB1b2nC_Oax0y4LxiqGGd9tHCXOaQHvNwh6qNo-nCEGtuf97BOzTfkdn3fVlgWOSZUSt7UA_af6QHgWU6bzURX2prwravG0fQqSK6j-PJW2Zr0NYv7ilmjLNKmCX74T9ED05h6z0mlkOIOGrT_YLXv7-rmMrL4gGmRtxmn3GaW_KieL_HI5N9L65xinsNdksja015zW-sVdYugAbOxw_gLu9rwc5XjHQCuKx9XVm7Vggo9uXKRObjWDHHhZemaSHPyazy-sNL30IwX0HAF67uGnU8kNxjnYZaLyKaJG4AcEfJjmRKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی متفاوت از تشییع پیکر رهبر مسلمانان جهان در بین‌الحرمین المقدسه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/668820" target="_blank">📅 07:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d057128a.mp4?token=u4gdeV-v-sVtI53lGZHkkT1wJWIr82QTQ0jdZgoaPgV4wx50ORgOIJ7-r5ck5MVg8yjefhoGehjPE_HKXKb6SPAK6VCKDHYjh5rdHHgXl3dXjnm8tNO4O3j-srBc3ldOGjHmV2O16Gvbh6kIPhTU4i19SLEiWS5oy2Q9rY8ceM3UKWbVht-bS9egxFU8MmT4uxIzzk1snsQJxWdDxdN90N7p0hXqs6UrxgdEbKeTNnawZgHMt9omNjYc0FFmxkWHP1GjzNzavAE5JIploe8XB_Tt9SNrX5pkgSHM_NCWS753SXxAOpFfghLnapVdNEyERYAF1kgDmCvlrIn9VdCDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d057128a.mp4?token=u4gdeV-v-sVtI53lGZHkkT1wJWIr82QTQ0jdZgoaPgV4wx50ORgOIJ7-r5ck5MVg8yjefhoGehjPE_HKXKb6SPAK6VCKDHYjh5rdHHgXl3dXjnm8tNO4O3j-srBc3ldOGjHmV2O16Gvbh6kIPhTU4i19SLEiWS5oy2Q9rY8ceM3UKWbVht-bS9egxFU8MmT4uxIzzk1snsQJxWdDxdN90N7p0hXqs6UrxgdEbKeTNnawZgHMt9omNjYc0FFmxkWHP1GjzNzavAE5JIploe8XB_Tt9SNrX5pkgSHM_NCWS753SXxAOpFfghLnapVdNEyERYAF1kgDmCvlrIn9VdCDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون، فرودگاه نجف؛ پیکر رهبر آزادی‌خواهان جهان در حال انتقال به ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/668819" target="_blank">📅 07:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بلومبرگ: کشتیرانی از طریق تنگه هرمز تقریباً متوقف شد
🔹
تحرکات قابل توجه در تنگه هرمز به یک مسیر تأیید شده توسط ایران واقع در نزدیکی ضلع شمالی محدود شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/668818" target="_blank">📅 07:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سه شهید و چند مجروح در حمله رژیم صهیونیستی-آمریکایی به اطراف اهواز
معاون امنیتی و انتظامی استاندار خوزستان:
🔹
آمریکا صبح امروز در جریان حمله به مناطقی از استان خوزستان یک نقطه را در اطراف اهواز هدف قرار داد. متأسفانه در جریان این اصابت، تعدادی مجروح شده‌اند که اقدامات درمانی و امدادی برای آن‌ها آغاز شده است.
🔹
در پی این حمله، سه نفر به شهادت رسیدند و تعدادی نیز مجروح شدند که اقدامات امدادی و درمانی برای آنان در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/668817" target="_blank">📅 07:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
صدای چند انفجار در ایرانشهر شنیده شد
🔹
دقایقی قبل، صدای چند انفجار در شمال شرق شهر ایرانشهر شنیده شد. هنوز ماهیت این صداها مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/668816" target="_blank">📅 06:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668815">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقامات آمریکایی: مدت و شدت کارزار جدید کاملاً به گام‌های بعدی تهران بستگی دارد
🔹
ادامه تشدید تنش به این بستگی دارد که آیا ایران به حملات خود علیه کشتی‌های تجاری در تنگه هرمز ادامه خواهد داد یا خیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/668815" target="_blank">📅 06:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668813">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8734f9cfbc.mp4?token=qsEL_E7bsvvXjWmoYzODuPNg8iWopFcXoHf1JzoGcTB7l-y7vOt3WfWLLikmJRXpSXeZz2QYdmiyyr0JSowcmn-pZQ8H23-9k9-1sUpd9uIBuJFBrJ7eaitsRoCt_e00c267ncfMHn8QXAnFBffert7zie-bxwmTaV8ub-9BhFcMhYkRvZt1fPVIhkYYZnOw9t1w8aVH4b3uOicvaBeCLGwL192EU0qMk4D4sf-uLScjMAM_Rk6XXlsL8VCM4uEtDBYIsy_-9jCi4tNDfh_IJahj5L6cfYynaZMTw6wu04A7szDeATa8v2N7uQ6FmxiMhg8YoIlO49srzSOYrK1dTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8734f9cfbc.mp4?token=qsEL_E7bsvvXjWmoYzODuPNg8iWopFcXoHf1JzoGcTB7l-y7vOt3WfWLLikmJRXpSXeZz2QYdmiyyr0JSowcmn-pZQ8H23-9k9-1sUpd9uIBuJFBrJ7eaitsRoCt_e00c267ncfMHn8QXAnFBffert7zie-bxwmTaV8ub-9BhFcMhYkRvZt1fPVIhkYYZnOw9t1w8aVH4b3uOicvaBeCLGwL192EU0qMk4D4sf-uLScjMAM_Rk6XXlsL8VCM4uEtDBYIsy_-9jCi4tNDfh_IJahj5L6cfYynaZMTw6wu04A7szDeATa8v2N7uQ6FmxiMhg8YoIlO49srzSOYrK1dTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنتکام: نیروهای آمریکایی دور دیگری از حملات علیه ایران را به پایان رسانده‌اند
🔹
ادعای سنتکام؛ حدود ۹۰ هدف نظامی‌ایران، شامل سامانه‌های پدافند هوایی و تجهیزات نظارت ساحلی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/668813" target="_blank">📅 06:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668812">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
🔹
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/668812" target="_blank">📅 06:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668811">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پایان مراسم تشییع پیکر مطهر رهبر آزادی‌خواهان جهان در کربلای معلی
🔹
مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی ایران در شهر کربلای معلی، پس از انتقال پیکر ایشان به حرم‌های مطهر امام حسین (ع) و برادر بزرگوارشان حضرت ابوالفضل العباس (ع)، خاتمه یافت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/668811" target="_blank">📅 06:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lY8X6tdRsjmlx-1l4_64By4kjPBJ3Hjb0tc-tGowEZ2b9ljPhbjwvswh9t6ojgunVpKUtr8donqrUY2AxG819zdCUInoo4wl8X19vIP8eIH38NcCH3n19mMsKd-htKU1ssJ5mLy6SSjQru1r5kFZJNCiWgrZmLa_Y-wSiEnjax_pJO3WIsQioPldvuo4aiLnXiuvk005JqeLK3oM7N787CGa2cWMOsEqpSuf-1upSjVHwWq_FzQqPDKC3pfnY1l216udyLQO2mlqvLZVMPNmWEQZ9xFsptqeOB34yGn3tmHuJJHXodrQ2ObJZI1zivxXmyKvL_iaevx2Mfjzf7ZN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xfo1E0M-HhQiahDj87deGoV_a7qkLiF0lBq7sJpsVLBaV1UB8Jz7FFqX6Pl3VmK5an4g3f5GHqTpxPh9erWdbEx-UNb4KgUzKD_w5rgNtvDMzRk5U6M8lOeYg5Pqv4wpkc8MZH_BjWqCZNxlPFEjQFzQ92pIKPkS1kNCBxi_UAOmQ2X-pepFp9j804NB7nsdDXvXub12SRGZUOZ5RjGSSqP7Zl19ZO-fJy5KjQvTNC4SZd8djs6l0o1E1o6DN3CISOv3iShbrRc6_KYgkKPlOzKJEmHcR7rSYro4CxyZdB3cnQ3ZgbQ8Thbd27KJXnznTXOXyO_HzM5WEQx7gYpBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxayOhY2B5VZ243AT9kJHVU7fFKoWAeT4lLhwa86nOOOiz6yJpJf5Nl52i-dNrrEOXzdOlyuZKKA9tLn0qMCUeBagBEZH5mX0W8ylPoQEJDrbpahwcfjY7ZZ5WsV3WpZHYXw0GssqhgrYBf5BbZr2rYdG3mRqROwqOylubOkOUy7Ox1Ik_o-y3w1ebtP4Ov9K060FVXWXtUbx1Bk2QKytSv-KEJxsmi5KuUhZf-fOz6CKZtd6BTgdtt2I7gllW5LbOxTgrfjWUldWDGuGFMJK_7gvUQpgRnSmdz0sA7LbJfreoZoF8I5ALnHZKZt2gYHAIvCLR2oc-wzfK7b0iO1qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بدرقه حماسی و تاریخی امام مجاهد شهید، حضرت آیت‌الله العظمی حسینی خامنه‌ای در حرم مطهر اباعبدالله الحسین علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/668808" target="_blank">📅 06:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
بیانیه سپاه پاسداران انقلاب اسلامی در پیخداد عهدشکنی و تجاوز ارتش کودک‌کش آمریکا به شرح زیر است:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/668807" target="_blank">📅 06:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvVZeRa51uamXv2F3YavCrbE-AGOMQxFqyVztF_8hdh7w3dUp54-HQ8oh-eyUo6i-L7bqQ0SQfI_Cwjbae52rD1Blc3WWZcCdwUVcHa1d2uFtZjYdnXo3-cbUU8L9YhYgHtcQ4f0sIQncsoOoGIEdujxo1GzbN66DXifhOqNZ1HiWVbmaW9d_44LpHyo-2tPQAZAejhyAtKkhMkyqkUsxRbHlPpuaq-VZdIIR2Nb6vvp-LerZPk58ESODB0cYuVh3TrjGwqbRFH2f7fbMyj1qP9iRW8MNUsCrgD_m4AMiVEY8EPFNQZaDfDixp7XbGQnTi-BhMRISEuDR7J1iPLLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اعتراف‌های مکرر دبیر کل ناتو تأیید می‌کند که اروپا در این جنگ تجاوزکارانه بی‌طرف نبوده است
سخنگوی وزارت امور خارجه:
🔹
اعتراف‌های مکرر مارک روته به مشارکت کشورهای اروپایی در تجاوز نظامی علیه ایران بار دیگر تأیید می‌کند که اروپا در این جنگ تجاوزکارانه بی‌طرف نبوده است. طرف‌هایی که قلمرو، پایگاه‌ها و زیرساخت‌های خود در اروپا را برای تجاوز نظامی آمریکا-اسرائیل در اختیار گذاشتند، نمی‌توانند از مسئولیت همدستی خود و نیز پیامدهای ناشی از آن شانه خالی کنند.
🔹
اما این خودستایی بی‌وقفه مبنی بر خدمت به قلدری آمریکا و جنگ تجاوزکارانه آن، بیش از آنکه نشانه قدرت و اعتماد به نفس باشد، ذهنیت یک درباریِ چاپلوس را به نمایش می‌گذارد که می‌پندارد با تملق می‌توان نگاه تحقیرآمیز پادشاه را تغییر داد. مشکل اینجاست که چرب‌زبانی نه می‌تواند سازمانی که در نظر واشنگتن ناکارآمد است را کارآمد جلوه دهد و نه می‌تواند فقدان عزت نفس تملق‌‌گو را جبران کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/668806" target="_blank">📅 06:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26234f34a7.mp4?token=hz80NLOShJcrcbmFQPrOkTAEPNUVH58EzRlp3MURlFXtaXYXjCMX8Su0uvtKWgB1ZbPvAFG2q0o1_GpL8MOUNruhyILUsT-SFyjdR_rHvASdR0NOqql6FOHM_Qe_m0gd_YyIcREIcX0Y9N5AnMS-wRZoV4N8zuTuvzGvR27-q7mIKCRxVFyjoZ2Lr7gtowdJjxaEJy9chKroesifkH6iZw0Lzi-iBb0cvbZEz6LQ1DcjZdSu2EHTj5W33kzfGgeNkSvQFujMQhiLfwWqQVsIUsRZeZLt6yeKIzT_bgxiS3LTZEgkHr_IUL_e1uolDBxacF__TtI1Wg32XDEAlQO28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26234f34a7.mp4?token=hz80NLOShJcrcbmFQPrOkTAEPNUVH58EzRlp3MURlFXtaXYXjCMX8Su0uvtKWgB1ZbPvAFG2q0o1_GpL8MOUNruhyILUsT-SFyjdR_rHvASdR0NOqql6FOHM_Qe_m0gd_YyIcREIcX0Y9N5AnMS-wRZoV4N8zuTuvzGvR27-q7mIKCRxVFyjoZ2Lr7gtowdJjxaEJy9chKroesifkH6iZw0Lzi-iBb0cvbZEz6LQ1DcjZdSu2EHTj5W33kzfGgeNkSvQFujMQhiLfwWqQVsIUsRZeZLt6yeKIzT_bgxiS3LTZEgkHr_IUL_e1uolDBxacF__TtI1Wg32XDEAlQO28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خصمانه جی دی ونس؛ تهدید آمریکا به تداوم حملات در صورت بازنشدن تنگه هرمز
🔹
معاون رئیس جمهور آمریکا شامگاه چهارشنبه مدعی شد که اگر ایران سعی کند تنگه هرمز را ببندد، با واکنش نظامی ایالات متحده روبه‌رو خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/668805" target="_blank">📅 05:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLmV-SO9A989Od7SSoAEFBpMWJu4TqgUhrOYw3yv4NK15STdvNSIASPE7c9t1TTcn0yt8kn9FwOwQRR34RlEzJ9LxeEiZfVWidi3ymgwi8khgHqJ828Saz1BiiZeW8IFWanRuYsZQc07K4YHFGVDhEAyMOPDeX31Paw2P6j2CIMVCAp7git-S9maK4TIa69tA2R9s7_CdcWDOeixQ-6wA_e3pkkGCXwmB_GMBa_ZbnycalzsMbRsQqxBxJfG6FfOcK5sWEaqtBxU_HNB57nplfR208SqJLdcmjCgfSCkZQQf3XQO8vsOO1imVhTjRBrDnKpQUpzJsYGbjo4UYbfsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJbzqITKRsDnM1Uv6krv6LMPVeBx1nBOZKBiZmnLTJ1xNbzSxjtCIZcwOanSHabYrMPIOuasN6v6AvPx6IU2GCZTKdtXw_ieXLQo4mF1mMLGRbgIAk0au_eCCftMGSk4FhPHZ4ojtollsnNANTaQtycX9NO61gmSIeecfJSf45rGNPkKk6S0lYqdLUzkHIPGU5ILvUEp2f6NscS1bt1cGq3f0EzQOk9r_WdQes44b9MyLXV4iUt8tyi_IKYkm0vdHLYuUkuxSEQsV_tomaVxaYJgwSWsGaKZTuv-WO_qe16RmtquEtVvV_RgDBcrkTrmXoTEgHp1jFc688qwDHUndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqgpX7KT_kLnUMMDZXMwFIbuwkj5eBLk2gA2yI-jjpL6uU-dSZGJuCzzufRCYe1ZTkggU3laxKnMBgDh9BcqoEJUMD3a5oNt2Lr9NOc4EBCst0PCnd3sfXgNPF7nF7onM-y-zbtIRJPRhHy9BYggVfklX1Zqb1T5ExqOA9bMq2npkeQZpleapC_aH48psE5lGZ9CYjdjp4_nqLZpnHwDARhLxlGNCuZpyeMsz1fFbzCVsk6O3tCVOiK5zJKCCCdQrdWCI0IMJIZHNtiB1lZXEB2NPYWfaEQzkRniLP139DrmbskS6vON-WinmjO9VdGWkWXdF3WBiuGbC24qfesvkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b347b90d6d.mp4?token=pfj-J2mRE4BltGkJAgWjMWeaJcPs5OaecAtQkm-QHYC-LL_5mMuwCTENDsjdvdB0UTYAiy6PY6yvp4DpyFThAZYwJ2B6wshEBBdLHJ-KaxukDfze3qVV6FGGFztHTbDtVySnOy2As2UKMXLdEqEVgHOUPDdnsQNc-XqhG7Z3ehn_27O_b4WfwinzkU-RSbZmk4Ra8hHr3eQMwcOG8eM78uRjhVZJ5zH7lM3aq4uZnE484PswHsTVNYqfdhqg_boYTnbr500nU6pazbY2o7BuT_FYT4_qLYJvWV66_ivEHosKvTtl0CU8WRnRf2l3ggVb4a0CACgJtr8vhaY6WbhfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b347b90d6d.mp4?token=pfj-J2mRE4BltGkJAgWjMWeaJcPs5OaecAtQkm-QHYC-LL_5mMuwCTENDsjdvdB0UTYAiy6PY6yvp4DpyFThAZYwJ2B6wshEBBdLHJ-KaxukDfze3qVV6FGGFztHTbDtVySnOy2As2UKMXLdEqEVgHOUPDdnsQNc-XqhG7Z3ehn_27O_b4WfwinzkU-RSbZmk4Ra8hHr3eQMwcOG8eM78uRjhVZJ5zH7lM3aq4uZnE484PswHsTVNYqfdhqg_boYTnbr500nU6pazbY2o7BuT_FYT4_qLYJvWV66_ivEHosKvTtl0CU8WRnRf2l3ggVb4a0CACgJtr8vhaY6WbhfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/668801" target="_blank">📅 05:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cbc7b457.mp4?token=DNW5aNVMpZFJ-5R67f2ZJchsUc95kGFqxK4jOSrjrB6_b8CqMI_GVh1qdDgFmtzQN8ie2wYLgFR_-DwNkygb1askdA2nX2seTkNEEGmbEs63Z5h_yNRx1Z_RWyt1xwW_Ml15LHkF5-XuNB9hedzdGLLwRLwMIfyw_iE9QkZ2PDYnDvh8agArxz3m1xBXnmU67CxOZWpskEx0mIWFmAJO9G1_kPUodWOTSp9PHJrdiZXdWZPG7kvzIYTsCt_eCmwF4L5GiZR_ueScH6n7MYKha40A3MjwX3ZvcLCpb0nWl7o9p4rP_qRbqQnQCOCC7jKn8U6KsECslYEMy_hEuX5OfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cbc7b457.mp4?token=DNW5aNVMpZFJ-5R67f2ZJchsUc95kGFqxK4jOSrjrB6_b8CqMI_GVh1qdDgFmtzQN8ie2wYLgFR_-DwNkygb1askdA2nX2seTkNEEGmbEs63Z5h_yNRx1Z_RWyt1xwW_Ml15LHkF5-XuNB9hedzdGLLwRLwMIfyw_iE9QkZ2PDYnDvh8agArxz3m1xBXnmU67CxOZWpskEx0mIWFmAJO9G1_kPUodWOTSp9PHJrdiZXdWZPG7kvzIYTsCt_eCmwF4L5GiZR_ueScH6n7MYKha40A3MjwX3ZvcLCpb0nWl7o9p4rP_qRbqQnQCOCC7jKn8U6KsECslYEMy_hEuX5OfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت های تکراری شیطان زرد: آن‌ها همین چند لحظه پیش تماس گرفتند، آن‌ها به‌شدت می‌خواهند توافق کنند
🔹
اما من فقط نمی‌دانم آیا شایسته انجام یک توافق هستند یا نه. نمی‌دانم که به توافق پایبند خواهند ماند یا نه. مشکل همین است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/668800" target="_blank">📅 05:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3042427b41.mp4?token=Bqqau9JQC37kcgL00Pgfi1i59JozRPVaiDS7vfKihPixhWxhkFqLbfqVTv2r7hGmDQsEk84LxyaaomRZHivqdOgWp0uZSfr2QxS5ePQ6beRefN2UC9-3VNRG0wT3Pxkne_Fofi4kLkGniylbrQIzRNEtbi74jVx5kcTu7CpwXRkC9KTmP4xftHeR6EVGWsn6cl5Q7pJvKUbomj1iPrA0zK0hDYg4keb4O6A6vgv7uRaBSTLb1yuP7lVUbuAcJ21W0odlfzgKfuBoNSha3134iNIQe0W6NYaePRon1afauag14E03sY5DehQ5ClRunCgayzlyp2Iu77SE3NVKG_t2jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3042427b41.mp4?token=Bqqau9JQC37kcgL00Pgfi1i59JozRPVaiDS7vfKihPixhWxhkFqLbfqVTv2r7hGmDQsEk84LxyaaomRZHivqdOgWp0uZSfr2QxS5ePQ6beRefN2UC9-3VNRG0wT3Pxkne_Fofi4kLkGniylbrQIzRNEtbi74jVx5kcTu7CpwXRkC9KTmP4xftHeR6EVGWsn6cl5Q7pJvKUbomj1iPrA0zK0hDYg4keb4O6A6vgv7uRaBSTLb1yuP7lVUbuAcJ21W0odlfzgKfuBoNSha3134iNIQe0W6NYaePRon1afauag14E03sY5DehQ5ClRunCgayzlyp2Iu77SE3NVKG_t2jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دمام‌زنی مشهدی‌ها در آستانه مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/668799" target="_blank">📅 05:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ba6f815f.mp4?token=AThK1MFKfEy2Pm5VZLniMEiC8_E8MxI2x-35T1EJJTolXpfNN_6Fmap0m_5os0DIYYWOIWLNE9JmWn3tectDo-nXyOmAfDUow_t5UVbMRSLzY8lsKD1JGxUhBtEcGiJMndPE7Snid3Ux6f5yQDlbIB1AKTaadSDG0sKnxuDd4Xb1TsOU9ke_ynpan8nIIWfrFy1Z8oxW9rs7TiTUtDQu9JX14BMZWaXSdz5fwdK-xtXJ8K4U1JlMBcq19LV7XA0gQybXwYYiBdlocESrJf4r5lMIoC_Cmuv2y1ES_jr-Eqfvo64TLzenfW-Rb1eITdr4IDvmBoKFaGbO5sst-xwDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ba6f815f.mp4?token=AThK1MFKfEy2Pm5VZLniMEiC8_E8MxI2x-35T1EJJTolXpfNN_6Fmap0m_5os0DIYYWOIWLNE9JmWn3tectDo-nXyOmAfDUow_t5UVbMRSLzY8lsKD1JGxUhBtEcGiJMndPE7Snid3Ux6f5yQDlbIB1AKTaadSDG0sKnxuDd4Xb1TsOU9ke_ynpan8nIIWfrFy1Z8oxW9rs7TiTUtDQu9JX14BMZWaXSdz5fwdK-xtXJ8K4U1JlMBcq19LV7XA0gQybXwYYiBdlocESrJf4r5lMIoC_Cmuv2y1ES_jr-Eqfvo64TLzenfW-Rb1eITdr4IDvmBoKFaGbO5sst-xwDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو کیستی کز غم از دست دادنت
مردان ما شبیه زنان گریه میکنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668798" target="_blank">📅 05:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7569abb000.mp4?token=vTJkvv7ukMzwltUoXVtp1_nqyjM5YmmrPXwN8QFYedY-H0Pzzhihu4LVpU-wQaUyVG9ShhSBTce9lIh84d_T_MVczIO33xISMVe6gXEjNFdUVtERCvCUg7IttKCtcqoRzp12Q0khBRg1fEFY8CXiz9etJUjFYwqXUTCC5EjwT67aqcEcqGuWk8GUkwCheeUJxDXpdlpPg_UMOIJjYIfrvFz5V6LTN8Yb9nCDDguIM_9xDFov64DTm0wKzqnK9zacaaLJkQnwvyIQnOHlqn63bUIDK9ht9cIKYXvDJ0UuAcDIDNqm6fQS7OLgfOOaOcf3sUPveW3XO88uGaVBdazqfQnA9UL1IW7z0m1UXNboO9d4s6HAu3hYqql_4EbIxe-tOlIXVg-suQa5e7Z-C5vecGq1_TkO06ZIg7hYIL-DvsYp8Xns6QFnddl4O2qHjmDeeDHi7n0kaMPhmHu2KEsNn1ksc9QHjxU3_TdGylQ1zHe-janKNk6LzAh-aadZCf3HsndS_Gky5cmLlz3IUAvSMecTsB_odkaISytWP1QbuCcpKcc0bIYjz08Cjle9zy8nHb7m6b8e3MborOfxtcTEg-mXCjboGpi3tmYeZran-Y87jaDQHGTwfDLMuheZgnWZ0htrbBJndIksc-gc8MBM8arQn3z0TDSVV2OQWw1gRAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7569abb000.mp4?token=vTJkvv7ukMzwltUoXVtp1_nqyjM5YmmrPXwN8QFYedY-H0Pzzhihu4LVpU-wQaUyVG9ShhSBTce9lIh84d_T_MVczIO33xISMVe6gXEjNFdUVtERCvCUg7IttKCtcqoRzp12Q0khBRg1fEFY8CXiz9etJUjFYwqXUTCC5EjwT67aqcEcqGuWk8GUkwCheeUJxDXpdlpPg_UMOIJjYIfrvFz5V6LTN8Yb9nCDDguIM_9xDFov64DTm0wKzqnK9zacaaLJkQnwvyIQnOHlqn63bUIDK9ht9cIKYXvDJ0UuAcDIDNqm6fQS7OLgfOOaOcf3sUPveW3XO88uGaVBdazqfQnA9UL1IW7z0m1UXNboO9d4s6HAu3hYqql_4EbIxe-tOlIXVg-suQa5e7Z-C5vecGq1_TkO06ZIg7hYIL-DvsYp8Xns6QFnddl4O2qHjmDeeDHi7n0kaMPhmHu2KEsNn1ksc9QHjxU3_TdGylQ1zHe-janKNk6LzAh-aadZCf3HsndS_Gky5cmLlz3IUAvSMecTsB_odkaISytWP1QbuCcpKcc0bIYjz08Cjle9zy8nHb7m6b8e3MborOfxtcTEg-mXCjboGpi3tmYeZran-Y87jaDQHGTwfDLMuheZgnWZ0htrbBJndIksc-gc8MBM8arQn3z0TDSVV2OQWw1gRAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر آزادی خواهان جهان از حرم حضرت عباس(ع) خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668797" target="_blank">📅 05:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed255f4df.mp4?token=h1t3aUPR_h91RhEjbp-rjHZdFIy5jLAba6oUJXAq3PQgAmBpksUXkhMp2paPxfP-hoI6VJAl_sMO9YQ27KjeXRdEkG7yeYDC_yfPqdyK061TtiktgAiZdIynDGotAtUEDgd_48aObo5-S929M5xtgMiRoK01rM7XhHf1PMOtOPyNU9DSAHPYxx_MnXl7k8I2MkxRPrOPlsnpVMSCKeIA07OKHuOS4qBCpZ6ezbHxGfyUwqkJOfGKLEuHPuUUkoj6M7tyK6kRQRloFzFhHjQWxwQLseDakHNMh0kNMtw-RFAGMePH61XgaSBw79DfOF61g6oGBynZ7VOBu7NWOkVn96H6FnZW663Yb69qXEHDQ-WAQQf-fSgumXmOdYESvzBuPvR7YIcBhz9RbwroSeTw4PS61AJpvKX6QmIFeF6tNLaiKTe_V5eiJILDW21V9acoIxG_FDJaTigQzW8bceOPfUt_JTHjgl5o5DKXPWdZxGzZJDH-n_0VGba-kU6uTNs5Qm9saRMa0CT_5QBBV9YqX7ku3Uyh7hzc380qDF4kZx7JPVNtRIuxTpeYj-drAHfwfQZtjOcfwuaVmHy-cHsz2C7Guc9sYkzCQR_Rni1kBXyyD6KwYiTTPshVcD8Xj5DjnZ0MKNxb8ZuH2q-wDLpI5xHDrcaqtJvp5BaMlDDdmiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed255f4df.mp4?token=h1t3aUPR_h91RhEjbp-rjHZdFIy5jLAba6oUJXAq3PQgAmBpksUXkhMp2paPxfP-hoI6VJAl_sMO9YQ27KjeXRdEkG7yeYDC_yfPqdyK061TtiktgAiZdIynDGotAtUEDgd_48aObo5-S929M5xtgMiRoK01rM7XhHf1PMOtOPyNU9DSAHPYxx_MnXl7k8I2MkxRPrOPlsnpVMSCKeIA07OKHuOS4qBCpZ6ezbHxGfyUwqkJOfGKLEuHPuUUkoj6M7tyK6kRQRloFzFhHjQWxwQLseDakHNMh0kNMtw-RFAGMePH61XgaSBw79DfOF61g6oGBynZ7VOBu7NWOkVn96H6FnZW663Yb69qXEHDQ-WAQQf-fSgumXmOdYESvzBuPvR7YIcBhz9RbwroSeTw4PS61AJpvKX6QmIFeF6tNLaiKTe_V5eiJILDW21V9acoIxG_FDJaTigQzW8bceOPfUt_JTHjgl5o5DKXPWdZxGzZJDH-n_0VGba-kU6uTNs5Qm9saRMa0CT_5QBBV9YqX7ku3Uyh7hzc380qDF4kZx7JPVNtRIuxTpeYj-drAHfwfQZtjOcfwuaVmHy-cHsz2C7Guc9sYkzCQR_Rni1kBXyyD6KwYiTTPshVcD8Xj5DjnZ0MKNxb8ZuH2q-wDLpI5xHDrcaqtJvp5BaMlDDdmiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در بحرین
🔹
منابع محلی می‌گویند که انفجارهای جدیدی در بحرین رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/668796" target="_blank">📅 05:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07ecff9c1.mp4?token=lfdpxaFOT8ktEUhLfB7TyGrpViupM416OlxLns_0Bt2rdgVZDZLs3cw0liE2gXLDmEYJ1NC5fnXQtNcBmyoA1ZxDNLKbvCBNrwvkYMrfYCVdPhR9lNNJkhT6g6T_TrrBFNVKIFww4zHlry_g9jlFK6R5Em4GdqEYinkXi0DIlBtVZbXigZQxojnnpEZP-rYF0LbKxST4OdCDwY8-yZpsQpvPHqmqCid2ISpkV_b-_otBKQbNJdZtoV0K9vYtwatCSLNA519Xwy8nS2zNP-DyZt5DtmTBLfwE9J1dMmn0uaDbdRg64p9AjJ3SmhpUz7g91ps1oO8wy-GE_f5LqVGnYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07ecff9c1.mp4?token=lfdpxaFOT8ktEUhLfB7TyGrpViupM416OlxLns_0Bt2rdgVZDZLs3cw0liE2gXLDmEYJ1NC5fnXQtNcBmyoA1ZxDNLKbvCBNrwvkYMrfYCVdPhR9lNNJkhT6g6T_TrrBFNVKIFww4zHlry_g9jlFK6R5Em4GdqEYinkXi0DIlBtVZbXigZQxojnnpEZP-rYF0LbKxST4OdCDwY8-yZpsQpvPHqmqCid2ISpkV_b-_otBKQbNJdZtoV0K9vYtwatCSLNA519Xwy8nS2zNP-DyZt5DtmTBLfwE9J1dMmn0uaDbdRg64p9AjJ3SmhpUz7g91ps1oO8wy-GE_f5LqVGnYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی در کنار پیکر مطهر امام شهید در جوار ضریح حضرت اباالفضل (ع) در فضایی از اندوه و ضجه‌های عراقی‌ها
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/668795" target="_blank">📅 05:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
روزنامه وال‌استریت ژورنال به نقل از یک دیپلمات ایرانی: ایالات متحده با ایجاد یک گذرگاه کشتیرانی بدون هماهنگی با تهران، توافق صلح را نقض کرده است؛ نقض این توافق از سوی آمریکا، تصمیم ایران برای تیراندازی به سمت این گذرگاه را توجیه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668794" target="_blank">📅 05:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWMlibncuYDtnAK4zxAQmgrySIiPFuLPYBrPq-ABQRvmOlOTZl-hXEVO1RJAfo56TGHY-Y3aLr5R2N2arZ5MiWZTMkw_XqqKV5iioIl_VEFe38XKoJEyXNBUuf_aSVjiRZ3wxxbpwFc_EuyBD2yCx_V--2-80r7Vl8zf5aGVjTR92XWF_c5yGCwTT_TKdHS4vLkl6RtGKoQTU_t0_Xfvtc_Afs16YuMPz22yTTVr1_etZp_KaPElUdG4ibVyNJGHk30rai8Si72l4bBU-66ve7IV65vT4tISUIhodm0YNh_j03-7iwCHqBrkxsFKKafsTlS9JOpmeJaYqpPfLK3_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایمان عطارزاده، سخنگوی ستاد تشییع رهبر شهید انقلاب:
زیارت کربلا رهبر آزادی خواهان جهان بعد از ۶۹ سال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668793" target="_blank">📅 05:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcF4PMjwX67mkHcfEC1vp3wnuJDPQJew6NsDeMB8nrlfZwJlkkwnox-hwFesijWMN7yh2vqIfqH9c9LAZUPzUleIAOYxtAtMYKywTbysIjEGjl-rY4QuSHiOFX5PZjFhFMzDiZ_ax6okuwD-Tx1sbTS9AoiePvdWXiJ8WY_SEJj4Kgeh2ZVqdCoON9R1NA6C_2ZiQNtkOc5Gc0ilafxUDa93-DNA9-DlsTse2YjUVvD_8hgPRJXQvjJX040xEXQmFTgy0R6T4rqn4xVx1YoSlAsVd-961sZhiwDywCF3zgsZSO4YnZ1-uYkVMLPTT5IKLmsllCQrHgtowNeRSsgHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/668792" target="_blank">📅 05:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
انفجار در بحرین
🔹
منابع محلی می‌گویند که انفجارهای جدیدی در بحرین رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/668791" target="_blank">📅 05:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cf4ac29c.mp4?token=Ql-hX3lnTxwR1itoW4etWHd7wvqVwkZdh3Oe5hPnpsajNf5LaG0xHLAb6_D6t7uCuU1Qq6AmFKM7dzSzv5gHZ2wZzAGoCBu35cM93N8nZ9XP7UCCRL69-AAwklc7zTRkOjHvwlsH_cOxTYt7FKi1wBPQ8rY9LlR_RFSfxUu3KLsJNiCWrmAG7sDQD0w3PrfSswS5DeBdQOrO-9Mghvc7VUIdv8YbQPg1qk7Y_7n5Us2egV_EfUvPLyJ2MT-auz8VLW9kxRPs_FPSycnxy22sjU22h3M8xlNNeFXV91Z8o8miM6IefMGBmNGzP5GK6LgCeId5QqaWJ_ZESX3ZM-XcZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cf4ac29c.mp4?token=Ql-hX3lnTxwR1itoW4etWHd7wvqVwkZdh3Oe5hPnpsajNf5LaG0xHLAb6_D6t7uCuU1Qq6AmFKM7dzSzv5gHZ2wZzAGoCBu35cM93N8nZ9XP7UCCRL69-AAwklc7zTRkOjHvwlsH_cOxTYt7FKi1wBPQ8rY9LlR_RFSfxUu3KLsJNiCWrmAG7sDQD0w3PrfSswS5DeBdQOrO-9Mghvc7VUIdv8YbQPg1qk7Y_7n5Us2egV_EfUvPLyJ2MT-auz8VLW9kxRPs_FPSycnxy22sjU22h3M8xlNNeFXV91Z8o8miM6IefMGBmNGzP5GK6LgCeId5QqaWJ_ZESX3ZM-XcZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکر پاک رهبر آزادی خواهان جهان به دور ضریح حضرت عباس
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668790" target="_blank">📅 05:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اعلام وضعیت سفید در کویت، بحرین،‌ قطر و اردن
🔹
با پایان این دور از عملیات ایران در واکنش به تجاوزات آمریکایی‌ها، در کویت، بحرین، قطر و اردن وضعیت عادی اعلام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668789" target="_blank">📅 05:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyaFQtyKJOn693RVZ7iGcVt_oDpg_LoSW_AYwUdBorJM4rDgoEgtKsukwPYPaQMid54mFMBZz9GKKG33zEe2DYSufQtfEWJxj_twTF0GZuT_9mbXkXz_TEehRn4NKo_QfEXYypPRboN8v5rRBUIiEfjwzZBhEwByjc6v_OhKhqquHwhNWYiUxcfMBWjeMNykiRfBStq2O9mqOf4Lq4yutuuAYwqT591U3zS0kmGmCzpcP8Cx-c7f0SXNdu1pE1TvlLB5LJs_Jrv9cWTyV9YoZ1RdZubTUdRIQkBvmcmrOFm3jGASa3K58ua1KSY6z2XxlQH9WBx0Bue5ICBX8LObtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۸ تیر ماه
۲۴ محرم ۱۴۴۸
۹ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/668788" target="_blank">📅 05:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
خبرگزاری رسمی عراق: مراسم تشییع پیکر شهید آیت‌الله العظمی سید علی خامنه‌ای در کربلا پایان یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/668787" target="_blank">📅 05:03 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
