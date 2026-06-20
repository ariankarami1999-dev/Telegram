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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-661570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYbz70nUZrxK5sOaPTOYSUjlWqMRLguXSu8gPatuH7E_oqhm64lUmOqBkbsdRZTZBp680rtOQatqLBEZdY4E-XKtak250t9wCM_aUqwOTwGsPdTfjUWvEK6i2NH2_0ywcCdS4fwSuWfWv5iJb-lqEDiwvKIBRIhbkHHp1lVv8EwvBrW04We-UAQ9zhIMNSknSDdmLcKtB_alKWKeA7zd5aeIAeW8j7b11lQx7whP_Klx0xozlMG9-xHT9Hum0r2r67_8Ce41vSjbxYGKswDdKhOA_gMFmliaRw9cq8rVeFaEKL_ZW_ZuXo2iVLTYlK5a_RbnV05r9ATsA4nyHLEoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هنرِ هجرت؛ چرا نباید اسیرِ مرزهایِ جغرافیایی شد؟
🔹
امام علی(ع) می‌فرماید: بهترین مکان، شهری است که بستر آرامش و پیشرفت تو را فراهم کند. اگرچه حب وطن ارزشمند است، اما نباید به بهای عقب‌ماندگی و ذلت باشد. تعصبِ کور منطقی نیست؛ اگر وطن جایی برای رشد ندارد،…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/661570" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1qKtx7EwzkD644soe1VsEINsurXF9qNJXj9whdZqcq-JcrCHMMVitDkbhWbxGOL8IlZoX-Wlc1wblQimUuRDWk_8_Wnax340pOOxyO4x2jIrVFIxt1BbVY0tJcrwktEIAcVPT47GBfpWusdi-hTW2ahNYwibOWPFGDdMn0JgiERif78xHSSRtRnIWh_SXWBKfcZJO29TPU0_ZK1CZwK7uwzqYvxjUaidp58fg7fsN6pSJE1OWcH_cbtVLenKMKfqvqMlZa9eGoxfJ-0WdEJY77bOKeuNKHAqmjEjaAyyWOLJbN2DnwoHstcd9NCHEyhlut5RXppz2VlNH85tJdePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوکو غایب بزرگ مقابل ایران
🔹
به نقل از DAZN، جرمی دوکو به دلیل عفونت دستگاه تنفسی بازی مقابل ایران را از دست خواهد داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/661569" target="_blank">📅 22:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXmDItinVLk7Uhucd7tyLS3zgvMPyJWH4q7sjFxEQSLPKU-gClJWk3V6CHExZKS5qjjy3HZrie2SIMzRwmt1havvE-nHnY4EpWlpCxOcP6JEcR2Buzl7Rg7hLhIHd2y61umQaKQdV8hTEKZAtfOPeQxrp3LtyXJEIYx1Rb7P44ou2Pw1750GBGfGnI8UYyXxoFJBUn7t71NQPv_2RrgEn09I7o6iaG-w8TYmmK4nXb6E7euZ5z3kx6EqdAGo83iLd5OMOYIRushuyp1bo_X8saR4XBqlJ9ATlQbL48KmARJxTF6E6yc8ls9KfommZgUvAfUaklsOSw9dvtt8orNILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مروری بر وضعیت فعلی و نحوه شکل‌گیری جدول مسابقات مرحله حذفی جام جهانی فوتبال فیفا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/661568" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2tOTNe9MwxK0-_8PiRjq7V_AWqvavrshNvOlOINB5P9rs07Fr1NoTzdTmEibbnGZHqRcHNSbVsCJycgLltJ0yQZB3WYRfvOhS2iMDV82CZD1L6a6Nl6bFjatuppNvrkhYIxXOjfa5cvIuVrWHzEyDJcPiNewB75y55urjVorkH5_gAP-iFpBa3j60G3L2oNhTnUCjiRGvFOgB0vAacnEWgmnFqIKIOHfrrFNffzyt_plSCVAO-NZNntaRts8fR4v5mILeP8YMx_eFmgUH3MPMErxJXjKbVsGIXM6m_jrNmcjTDK1WJf-TnZ0SH0l0pM6FXuToCWTJ4VojTMSBbobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8nFFt7pl2jrvGiIQoa1zT3tpOGESWLHJG-ojNHOZxM8H-Txo3mR22hBxAYoO-BPiLsNgroVq0y083Of5MaIWBo5jGEyOLaJXuj6VuYOe0khn_sSIccvyTcYyRvQr1bYR75IydqzENbKuQtifTNO6-c8Cj1plo6DvUqWFYVOlVs_-1nbXROHfdN3KD7aS0hXdV8FChM6vahdBtdtjCocvwunfi0l8LcoWgJaG4SA2WGxBUB16yeaBZRm8xDOBh5dNS2fKPNP2M_-gqLLc1wkjnLHRxFTe2p6YhT3mA3cVgcNgG5qHows4a2c19bLQqfem_IkZA61HXb1iHqqrf08zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZvWOxehC-tXIt5r-zDwCwV1cYp3ees37-CDkZW-7ei0VjUjaw7B7GCDmTWBf3LOGW2-MuB2UYOjyoCqX9ZPj9HQ_yli6iAUklNosYEzw93hwF3E3nAU0dT6HcSMwhZ8bC_7z6QFnI7s1Z_dYC70aQOZyG7FTrn6C4AKFZ7OyXe6kB3WAnCMc5NKvB149TSaq5ybkHqpFnRCNRCSfGi-eGO7OJHignM6r9gInrTrDzuKHT7BmtIcayeN7xoFsHGktP7SUZmufvPFeR4S01Q4PITD6LruM9C8suLqkOPyocLDvDysxAIN3ALMQhGg56fxhu4b1kZwvU_esrxk6QD-zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چندین حادثه آتش‌سوزی با منشأ اختلالات صنعتی در شهرک بت عین رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/661565" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144d7341a3.mp4?token=W15KCkPfps9dpTPrjAi7f9x0VQyzbY5dQQCV7j2m__F9yaWuPh-Q94tHFyHwVu0s3CK1OR0m6_phgXIGlSUYvW8cPl5Uvp-3ihdsW3-9UUKBEz7eEhkgBOH2Fr01pdawntqxX7eZfn9Saw-m_I8XdKgOkCaRAz43_xQyLrxVnsM5bPf3_RxLImdKvqv49SIROccduIvWzhgdYB8JDrlv2BQVpW3Yn4Wkl26n5mD35F4qv9mS67k1syHkQP-4TL24pFYxRUXKmLtejaQPDzRI3xLzSaXy-GT1k7wmvy4fHw-MLjgETtoA012g5bV6SpQDsJq_QhaukGFpG3l0I4sVDi0RCRxcrFn-mESCq5J2cLDU37-Syfly3hZK4i_Imjtbz4odHjv2Nxf8fNeI0pqe0dQGdo6T5akNKf5pu5Y9VVBrPVK-xcJsLRq1_x5x9MFoFue1P4nFf_66FNMGjN9eyYxUkeASJJtDHh7IlgUIBzXJQvS2LNPl5piLQDPIfaxhFja1_Jy53A0GkqoMxARKFMPlW8ELsgt5XE4gm7UPZs9pxVkj3BSlFi-jDA_yqqKEw5v1lB8x9-NMxmn5RSoYHICDA8cJG2tgLOIrduRebc-aM8H_NGup5SLTx8ArPauoe6syJ-u7rS16PQB0K1fjvR9joq7rPeNCW8egn7-6koc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غوغای دسته عزاداری نوجوانان در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/661564" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5cdbc5ea.mp4?token=s8wiAjROMIcXTp6BFJTJq6jnCioTPuYbLjaYWUraXaTrnASXfM0u18CSQ8E5eFT-2wfCmq8V9g9QCHKzm_3vXJnS0vYgFiR4ZkYvwmiqNDBUXlz57LP9PdMZF5gu_8R1qnyrK2_IUfLj2Ag4F6iy7Lk0L5C38LyCEj86-NtD9KDo9rzycp-SoqFx4HTJXH0E3bIZf_L5eegs886PJGdo7rOCPQbz-Ry7AaPjq867sBl_yHrEkleuCEEVoMW4honbko7DoG7DKiND4FhGCj2tJjcZ4jVurT6fm6-InpST3-mgdnWp7ked1yKGSargnCM1QkVa78L_ulVkZ3kuBcIjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم هلند به سوئد توسط کریسنسیو سومرویل در دقیقه ۸۹
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/661563" target="_blank">📅 22:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdoizAPKzkjZUmptGiUgWJuBMptVcszvNdNrNHl6DU8GNm7ieeyz-A1Qzs7MyfVGCAehScCAhffSxwAosnr9MexCso7PpSShPxcxHrnDNZNG-he0FEneg5b9SFXlRd7yG9h7qhaLEISnBKq8sG8HvPa5irr0z0BaNe646S10PDTjwrTshSjo6xVR5baEHUXYvcojj-lZLuttJooSVJWMR8SmJ2IWC9L5ePyoDk1PLRtHUC49rhOr3joPl7IvYnBhFd3Qguk2MAIKxT-OUmoF5rT-VE2ZhzzTR-G3cDXkumVOYHWRDid7S8AJIVUIFhYwPLINJ_ckR9J5j0gzImHJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530fd80707.mp4?token=F0oG8w48BRyk1tUkdFhgT3XbLvUwlKDJh8dOBHzri2PvC2LFuP49q5xL487EQIgwSJTV2dLHOfpO3DVuOJt4OmhEqPYNSyGiDOIPRvlihG-rcyL538Rm8G6QRJFiCqQ76PKl4-AZWhFkNUoDh6dS-26pWx1xI2FfvRMixp7oYoRDaSdtbpoQaZ8cpTiwYIHFqA4CmRQfPxowzQhLj_HuWw2MkPgo-TTIIEAC_uqJLd2XaItqnAjv51NH2nxbQquMFUPXcPWJe9DBgVn_Q8hS_IoiTymNW7KMQTFW75N9w7421O3pSK1LTK1dm_kwSjlKKwSTpCqM09ieoPjO6piEsIIbROgFXqKjP6tt6KCTKjXkHoXC9FVE9Hgc4Og69pF50mvkob75wpezD0Rn-p1TtIVDwzCFY-ZiO-XLZJHpJZFZIDCbuGioSA2yfJv5AX26dcdJE-D974nU6deDLPVCUfB3_DSigqIjH6aRea_KuUf88hDoasC91OwNtIWIXBfKLu_V_JpzsnLGnTgUywJwI0x6yiUOQ5lXg5vUMd99ebTYOGdE7pG82m31W0GItxfcFwFPzgeVWTUlPhpqd4KmmDkacsm14SPZiuEeCy-4SLmfOf0YOSLi-_vyKASbfjGXBOxZoSE1amRxn3iiYg68eFaBhGqUYo_tlvFYERPQKUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب شب ششم محرم حضرت قاسم بن الحسن (ع)
🥀
این بار طوفانی به سوی دشت عازم بود
سهم حسن از کربلا غوغای قاسم بود
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/661557" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpFOWlt1W7PKPBAN1-2VrklM3qa3GzICJ6vDdsIrbsf1g0VpzxA0VybBVqPMAtqjgBBXwRghl5e5T8P09g6f01mjHrgsAuvuC3U2D4_5kir_PbNiarSGc-oI9DamkWRLTXPQKoBxVDEe1cdaRFDF-6GyaO0ie9IMx3cWQ0Hp47NmCZ3UstyuedS01wklG7eemmvxpzOog-UzdR23qis9g6VosL1XrDzGVvTKvJMY8P1HDBzm1Bv5V7GzMhOsbiNXIWOm1kBv0g83J9tWreM9GcZtBdlG7FXORqAfS2cWjDadBr4il25Aag1q-mWb2f-dPhcI-Sz0LC0yN2hCQXCKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNXfnfbJvQIgR3CqQZ5diiBSGZr05JY-jwoOhmZrMufFCAGGPbelkJ9UBO83Y4tFsRzg09UwUk7y2bg3cT6eAk2ThFltIQEeB1XWYhKrpEqlBXAUch_dudHudQCzZ66hsjD6jxEAjhP-5hzKDcX6XT8oewnyFNcviBu-7TsWR_NDDgNnp2j6Jxq_VK4nfFtj98S-No-yFGzjNGnpvm3Ivo5WbHzSX_vSQyHIosu3MBu5iwxo-_5T8MCYVV-N_WQjtsyVSCpGdM-Cs898Sb5f-UfUP7LZvnf-SRDvAmq0X9HzBX8eKW1RAi2ilLV4oLAJbBA2VKWgXdWpzqux2TIf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ms8zg81FoHIYM1DI1I_3MAG6TBRpV6gzUsXfSuO9hC5ZRh6GpT3-Ry3n_ilJRlZxF4qVVZJipuObFE9RkVOewBoFMXbQAQKFVcrvOJa_vyNgK92sFxMOn-a-BsCo-S51cZDXcHZf-oRZcShC_XA1Qg-ZXqMjcXE9Dqz2Wwc4EZFqaF4P-ZEsGNQQ2dynleO0z_BcwCpCBBt7HLzi8GXnf8sdux8443KF7v0WnScM0iVMumxePPyGHGAkxokbw-2QkDXcefY6Iy5WTRaf8Y3DnizN8GEzF379GmR_bK1yv4PjHeNsoHi4PsesNfNdx-KgDixhjjPwyGoP3TXI9_yyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLttIcjaLLuU-tCKQ32_1ueVeU2rTjL-QiMJuJiGLTE-Yn8lsNBq3SIepvh9JvT1gBo2Le96s21W2mu4adCkvJVOyXYkgK9E5_9yRJFY8F18tRAmsCqZYw43l6k7n2BSXeMXDg_0kUgwzlYhgOeTDpodqn2xgh57MqXJecFqD5M5EuCPI-QS_jidV2guxJRkfBTVGPFQOp1NjH-NXPSZlXhNFGqH1eENCyeWg8Wn-okhAjze5haGaRJ62xVSZciHZaUl9FUTHHPGCCfNh-H40XgasBaDuFdBaHd_d2afYTEFPy3faeFFy36laf_dbtvZyvKqJmo36Hc4Dkw7SvukTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDt2QrXZHC0zOl4QeaZkwoEzh3TslpSDgdHnznZohg2iyDrf-ZWQ0wsWAiN1aTixtDVU6CG31ofzbrof2S5C13Pr8K-Z-SM9QIhon267Zs9JINdxc622Zv1zjEPLtVaIZgyhoSXgxafj8oRJYY38DpXaI-9YsF7YfS2kLMy4HDcllg0vzUt6f3NS0KjEtQ9LObCCMvbW58Fp2EaXenZ0iXn_Tbqrhv1dxklqKLLbl5wXezgaucc8BsNLmGYtwZWdSgj6H_g2iw2Mxx9uW85nvjq4zbrkqxW7aXSn7W_h_QBsLG-RZZAkW_rb3rXwVJZ1whLmkRCMRoe9A71KSAzLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUNk5XCy0Uhu6IMbjOi1U6P2AABgW57AgumgwfV7kQmYbiS56tlb9xNJpmEkbcIrC4OK2NBaFfIZVoAw2zgspMyWyVV8dOeBgiaFhSkn9_qH2gPRhJdaY5CEacpPsqBTlkNdbqRirHY2c5LOgg2TYRmi2FH0UAJSZI4iQIFqx4GdGxbfUmQ3MdxsXfnVtya_sNbJUp1e_fbY4rCWGg9vPksK3_-Wxg88tcnb03qnZaegnvOyJWSLNaDDIwP86LeII_O6t8vu8MYnS2UMltMaSY6iea-3gU98644IZIsmBBYMleqQMIdnL3Lc6AKq6q3aQ7rhmxFELDy2wOL0UV8NnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترفندهای کمیابی که طعم غذاتو معرکه میکنه
🍽
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/661551" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc45e710da.mp4?token=JMU5MEEJYYhzB3_1TLquoeFtLTaNBt0FmrFK4NLD_EnP86omNvDLMpviNhG1JefdUPjQGS2t7c8OJ1ieBMuNfydhAn0YbxOFnACK3XRQ9si1EZJQoT2aFo7tejEVbLvnemQObOGWvdbg66wzZXGCeBqvySfJzs5RNGdAZWGVBPN4NcsSoxgmsybaDOaO6HvPzo-eeM6E4AbGiWBw7ypY40RVDoyzX-gstRlOqqF0CLU_UhqyCYkpi0hiBKFWlJKC0V4eai5xVJdYi1k7R0J6dtit2-WtaQqBntPKULLAfHnrEqjCksbFZ3-dKE_LoVuNfiBnhPLW1c0uI-xZocZZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم هلند به سوئد توسط خاکپو
🤩
🤩
🤩
🤩
🤩
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661550" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
المیادین: هیئت آمریکایی در سوئیس حضور داشت
‌
ادعای المیادین:
🔹
هیئت آمریکایی در سوئیس حضور داشت اما اعلام نکرد.
🔹
جرد کوشنر دو روز است که در زوریخ است و منتظر تصمیم ایران است.
🔹
هیأت آمریکایی پیش از اعلام رفتن ایرانی‌ها برای مذاکره وارد سوئیس شد.
🔹
حضور کوشنر در سوئیس اعلام نشد تا گفته نشود آمریکایی‌ها قبل از تصمیم ایرانی‌ها وارد شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/661549" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176d19b23e.mp4?token=Wp4jUOkJbS5IeDpg6xYre5HDfnnaiP370kUceYsWKBtVWx88UP8RWG3Y9RLir3wGs_HdEnuQ0qfmBl-5qYM1NYawnzNIvmwTQWV_y0jWPtcjSZTdFQEmOEse1QT-whZERVGwGR29HYEXkSWNjyxoTxeleDvml15Bjaty_0-Kg7YkcYIyoHS4y-JuKUi_C6mxirjl20D--kqik7XwpdLrrsIAQek1e_XtvuiSmItoRdDzYqiqadOu3bDnQEm0F0-fOS63ecb0e9imgvKJDzuYmcPxzY1ACDeAE-SqxyoxmOWKf9Uti3XGMS8qc_-vJclAQbJd9ucpO8qwEcHz-7DE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روی پاس زیبای ایساک؛ گل اول سوئد به هلند توسط الانگا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/661548" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRpdou9NA7oG8e1pclY3kB1RfFVIsP_0d3wlSkTca0E4oEkZMgkoKvQNlwdZfGL3CdifRcrXWktquRZtyp24PT1OkABJYxcPsXtLczZh8oRBUO7gKaxZth31pym19LejOUQIxylsVAwjHH3jOdAr2qow0SmBsxihltPwZ5yQjG7pdr9vA2tQX7RekaeVOr17sADtzKG8dv4tc7tHeK8ExQTykJnkvRF6XUNuqSQvaREK6T2nz59tcGGG3NSK-E8vSrxs0CMB93E9g_q8jd-zs2f6woH0ZPZvtsvE1j5-IJp84GTklZNtIIG_CXp2XvtaLD60H-GKZ0zh3W-L2mDnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661547" target="_blank">📅 22:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل به نقل از یک منبع دیپلماتیک: پیام آمریکایی‌ها به ما می‌گوید که در لبنان دست به تشدید نزاع نزنیم تا زمینه برای گفتگوهای سوئیس فراهم شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661546" target="_blank">📅 22:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGCzOBNeAUSNIBf581A-4eMFH3Ia_PjHk56zlyB8E5GebGqdXit7wdIMLYA5w-GL5bTCoLY6MsjC_QcWE_ZAlEucRShgiHi3UCbItnniy4k_OoJ4h2WydIryjYIJ9Y9sdq_YLOlZZmZn5odDV6agDx5nkOQHKN85F1G4EYx49a_ALABqcBwoGGDHKPslj7QmSu1aHsMWVvkRqxt1BbQUC4N8WbHLA18svcZtqy1BMzxsR5PE0wid3Aj6VspFqDJOcJ1DxpAwvESgkFK6uUx5jFc9SI3mPwCuXmQKXFICTzEwl4ZVVUHiDeC9Ht_2W-P-Py4Lg_jwSpRFFrgDn09wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرکل برنامه‌های سیاسی صداوسیما: از راه گناه به مقصد نمی‌رسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661544" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq0PHi3OLqCQyN_K2BaJt9ZzNW6WDfFlhpzx1Q42tCsewpoMFAFmp6szBcNNrtF2acsmt_PnajGgjdRSdkg0uj3-kgZ5SH2fkfBfh5bVNpv_dQcjuvnexmboIKklKjvA4TSmmgKMjrV1cBow-lG5cZMWsaOnj5B28jLpyhmpacP4pWca936Re5LY4rf-SNFviTUXr8eee0O257J887_J2E4IflDToIaboTezIyoiPPDOxNlzifhKy9GsIDwng6wkyFLUtVbfEsxycRKxAxbOMKVFZEY87L0whaKpqI9c5Laax0LLWcyf0JQwQLARBUASFrmVK1JGcjcI6IYMUF1m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حرف های نبویان صداسیما بابت اینکه اسناد محرمانه کشور در آنتن زنده پخش شدن عذرخواهی کرد و مدیر کل مربوطه شبکه خبر استعفا داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661543" target="_blank">📅 21:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp2FH9G36HcAW27E79yBHXPsjeTKTui34TE6T8WDtVS-oc2vsmSBsyylhLcdECGIyVk-MmpUxMUuvXzM9datP64HeUTGOcIy1OIlTMh6z6tIUm-vG60UJxjvoYt-QeN-z-BUpnJevg4oPh3XGgfY_w4r3PdAc3tjRCPXo0Cm4FMRtevwLsWKgFJ_luTJAzx5cc2mwqL5akvqJ9MDj67eTEZEjycevV5v2wh5l_8dcR2BFuf81ewquFVZSx0uBJj58GERJnpTL0_aYtt3CIQAAipN73FicCw9-yy5jKBfyWVAV_XEnd0fNU2AQt3xEF8HLZiDWtb6Vtwd-_dtw4PNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر بخش بدن با چه چیزی حالش خوب میشه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661542" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZONx85YFxI2p1XugJNuoCzLOn1cZmrIBxEOW76ka4ary9aQl5oujW12hrM9eedyq2uGWS6CR9c8gcG0ik0-C2OfaQHfbmn6NBlGa77f1UJ18nIt8Loc4VEP6-3JI9VTt1PQH4wGjx0r0nBOzDJvTKZGh3_NVtI1w_t9cJBPlGDCXjr5uJt9Z34BUMVcEWpEPCupFHaf0uzz-M6lG37JBLUAtu-D5blOxb-OZGOaub2py-M_ssNtSARBpXNMBURLUbqQaQPCflXRfIfFabkBjOB6x38M23DEPdluJJw7MYPnu3Aho4fFNUC4n-XR3smhPPafQ-v7cKhJqQy9JH-93jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری نیهاد مویاکیچ بازیکن مدافع وسط تیم‌ ملی بوسنی از وضعیت کارتن‌خواب های لس‌آنجلس
🔹
این بود رویاهای هالیوودی؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661541" target="_blank">📅 21:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKu0m05K6YHc6NC_daYYnsrrKxb9OKQPbvDC2YY33HHdM4CctWZQYlHMIcrQMtQZb8gjidztFwdgkPsDA4oF2r2Q8HMvT_FDLDHnytQWALBqCzWGk6F4xPuU0eracjphyayyu5qQBwy3bIcHMU4ZUaCtYMoZ3dEtxdLUaQcoVb4N23ipBRFz3H6a1GTOOBfFtCjPh3IDbY2WuR6VvT4T8caUF2fJKtSGPxGsEnzz2kxIwIhJHYJ52cBhVwe3lie78e-3Gp1VzuCxVliFUDtizkDqZRBtkyolN18DylllUi2-JQo86WKWHcTSILpYfKHKZYDQzc36Vqlji1bQ9CTX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه تورم جهان در سال ۲۰۲۶
🔹
ونزوئلا با ۳۸۷.۴٪ بالاترین تورم جهان را دارد، در مقابل کاستاریکا با حدود منفی ۰.۴٪ کمترین تورم را ثبت کرده است.
🔹
سودان، ایران و آرژانتین در میان کشورهای با تورم بالا قرار دارند.
🔹
در اروپا و شرق آسیا، کشورهایی مثل سوئیس، سوئد و چین با حدود ۰.۵٪ تا ۱.۶٪ تورم، ثبات بیشتری دارند.
@amarfact</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661540" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در لبنان: از ساعت ۱۸ به‌وقت محلی (بعد از اعلام بسته شدن تنگه هرمز از سوی ایران) تا این لحظه، حمله‌ جدیدی به جنوب لبنان صورت نگرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/661539" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اطلاعیهٔ صداوسیما دربارهٔ اظهارات یک نماینده مجلس در شبکهٔ خبر
‌
صداوسیما:
🔹
اظهارات یکی از نمایندگان مجلس که در برنامهٔ زندهٔ امروز شبکه خبر مطرح شده و در آن به‌صورت ناقص و مخدوش به برخی اسناد طبقه‌بندی‌شده و مکاتبات مسئولان عالی کشور اشاره شده است، مصداق تخلف قانونی است و پیگرد قضایی خواهد داشت.
🔹
صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار داده است.
🔹
همچنین شبکه خبر با ابراز تأسف از بی‌توجهی این مهمان به موازین اخلاقی و الزامات آنتن زنده، اعلام کرد مدیریت شبکه ضمن پذیرش استعفای مدیرکل مربوطه، به‌دلیل سهل‌انگاری و بی‌توجهی به ضوابط حرفه‌ای برنامه‌های زنده، برخوردهای انضباطی لازم را اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661538" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای نبویان: نامه های مخالفت رهبری با انچه درون مذاکرات انجام شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661536" target="_blank">📅 21:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bef3787bd.mp4?token=LucYWcnUlE3fhOHK09LkHKfCS-DxHDGdLBod60DsYm35S-yuTvvSE0QGpRaAkRL602oDguGIrB-OUPnOLryg-9PO6TEGswhb5B4IU0GK0G4NWAB5YWISEVgFM-aII_t0VRq3jElzmlscH8PfJZVdRn8lmoQLLsBIpvOh-6ZHtur0ZYnDrwvICSTvYueH5zUAUhHuf78mCKwiGRgIwAdrRMfaqpkXyX-O_F_XxL0c03hTQWowfmapVbwYspdu_S31C52h2eKjMZNovNeuHxW0kDCPxVtOTLYHyZVAtD2kgM4TzL_thWdjFht-IdtZ1IwpKuIZoLHtdo-RMubme8HiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bef3787bd.mp4?token=LucYWcnUlE3fhOHK09LkHKfCS-DxHDGdLBod60DsYm35S-yuTvvSE0QGpRaAkRL602oDguGIrB-OUPnOLryg-9PO6TEGswhb5B4IU0GK0G4NWAB5YWISEVgFM-aII_t0VRq3jElzmlscH8PfJZVdRn8lmoQLLsBIpvOh-6ZHtur0ZYnDrwvICSTvYueH5zUAUhHuf78mCKwiGRgIwAdrRMfaqpkXyX-O_F_XxL0c03hTQWowfmapVbwYspdu_S31C52h2eKjMZNovNeuHxW0kDCPxVtOTLYHyZVAtD2kgM4TzL_thWdjFht-IdtZ1IwpKuIZoLHtdo-RMubme8HiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم هلند به سوئد توسط خاکپو
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661535" target="_blank">📅 21:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpb9pHM5iokuenrxdR2mBSYDY4s-YjCbO1pnp8kZBjhMOMKLI6iin8pcjLTnUleAzFQ8psdZwHon6UbnNbevBYWTK1b5ecwO2AggEse0_MlzcbHPiGYPsd3RnfnJcbPWj7_2JSusItAlI7viaxKkziPgcx0KOBa8hE1PilZVu6WSajtW_RHsfKvrFcS-2fu-iBAdqX84q9PhNTVwXS4Y-LXbRfYtEohy2hNj-cU1P_CczfHHVKyVFfQyv5RYLY-ADHI6LyyCzKvNp_W0qP6T5YIgTdkknctQrYgOLgYpId7yk9MmqmVF7SVWUPW_i_bdR6SDTvbQQGQwsI2EzHOhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حرف های نبویان صداسیما بابت اینکه اسناد محرمانه کشور در آنتن زنده پخش شدن عذرخواهی کرد و مدیر کل مربوطه شبکه خبر استعفا داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661534" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac59ad1d0.mp4?token=M0195G0HhOg4DyJ8ituCMNWf4rMxMXZnJYzjxenNwFale2l8FCQ-oifk3HuypGwKU4xmUFJ3uFtgaGwMqbKzG30kCwep7YijZ1iqGUJAVO-l9AsqPK-Qm14kRcKJ-PLR_3JaLsrULqa_QbcZTZvKmMtqMmH4awTacjhsJYu1xBWuLLO74cfUkaVEqqr5l54ZMKicQCPXOn2eCp5VV5qYjQS3SaXtoI-tnKAEfmYqrFTzmk4BZOmIaBVVXrTz_iWbAoOch3T-L6RJAaKA8QF3EG3I8HEtpKm9unVGPbhqF6_yC6twiFE3KKr_cdO8ke15yktYC90vpoTtwxnp5o7DkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac59ad1d0.mp4?token=M0195G0HhOg4DyJ8ituCMNWf4rMxMXZnJYzjxenNwFale2l8FCQ-oifk3HuypGwKU4xmUFJ3uFtgaGwMqbKzG30kCwep7YijZ1iqGUJAVO-l9AsqPK-Qm14kRcKJ-PLR_3JaLsrULqa_QbcZTZvKmMtqMmH4awTacjhsJYu1xBWuLLO74cfUkaVEqqr5l54ZMKicQCPXOn2eCp5VV5qYjQS3SaXtoI-tnKAEfmYqrFTzmk4BZOmIaBVVXrTz_iWbAoOch3T-L6RJAaKA8QF3EG3I8HEtpKm9unVGPbhqF6_yC6twiFE3KKr_cdO8ke15yktYC90vpoTtwxnp5o7DkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام رادیویی نیروی دریایی سپاه در تنگه هرمز
🔹
به دلیل اقدامات اسرائیل در لبنان و نقض تعهدات از سوی ایالات متحده، تنگه هرمز به روی ناوبری دریایی بسته شده است. به تمامی شناورها دستور داده می‌شود برای حفظ ایمنی خود از این منطقه دور بمانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661533" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
قدردانی پزشکیان از نقش سازنده اسلام آباد در روند دیپلماتیک منجر به توافق پایان جنگ/ تأکید بر توسعه همکاری‌های دوجانبه و تقویت مناسبات راهبردی
🔹
رئیس جمهور با اشاره به اراده جدی جمهوری اسلامی ایران برای گسترش و تعمیق روابط با پاکستان در تمامی حوزه‌های مورد علاقه طرفین، بر ضرورت بهره‌گیری از ظرفیت‌های گسترده موجود در مناسبات دو کشور تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661532" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ade552e3.mp4?token=WKCBln8OWJBmuREFsY_01lkrLdAGWr_m4Re2EP4UVqXCNgYqcC5IOhPjkpLEiWFC1ubIEhgFva8nNg8jeJt7F5cEBtm7bhlP90kqOPFXG8PnnpQ8xorBkQYdclH-JMxz82z3s1E4lgT_ca0--LaS6SDhxfHngM9fdKJQJVlK3o4hBBNPGHXeTRWJW4K4E_oq-ksa7M7x4nboeao_HaIEHfnL9-W0_QORAHrdRpbvXkdtXJPt_us0ADYSbiasbVf7uG3sDvEWe5QJXwaxIi1GcyByVEgINKzq7jL-wq-4vF3puw8Y-sCn65ZlgAEoNmedg_AEPjj8vd4GBpnGSwn6fJ6UCK1rfNNsJHlMEUsvC6ump-nY2yqkSFBlem1d29zOQep19NGM0zREdyG4S6KdOWusg_e-CWS4Be2toQaq1nLr9v5aXsNiFSxeL5CQaDAqFyjvPvxTcUGn2TnuEzGcb9JN_bft_dA_5SeQC0mN9YgcKEG--kydQ8pTdZ5Q7_MKXidVG_vB4sHPO7ihWuufwUROj3KPllRNAujVA4zncpC_VvUqoUA5X_0KkuILoaw60aYCFD8_KfsCvCe7t3h5xznfcsjjP-L1gJB7zLSPPb_LqhKOlGtL6EBWubjyzX1KV_iH0L3PVrGbKkt3reoKUHedy_fIWPAXGIzs-5XqAQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ade552e3.mp4?token=WKCBln8OWJBmuREFsY_01lkrLdAGWr_m4Re2EP4UVqXCNgYqcC5IOhPjkpLEiWFC1ubIEhgFva8nNg8jeJt7F5cEBtm7bhlP90kqOPFXG8PnnpQ8xorBkQYdclH-JMxz82z3s1E4lgT_ca0--LaS6SDhxfHngM9fdKJQJVlK3o4hBBNPGHXeTRWJW4K4E_oq-ksa7M7x4nboeao_HaIEHfnL9-W0_QORAHrdRpbvXkdtXJPt_us0ADYSbiasbVf7uG3sDvEWe5QJXwaxIi1GcyByVEgINKzq7jL-wq-4vF3puw8Y-sCn65ZlgAEoNmedg_AEPjj8vd4GBpnGSwn6fJ6UCK1rfNNsJHlMEUsvC6ump-nY2yqkSFBlem1d29zOQep19NGM0zREdyG4S6KdOWusg_e-CWS4Be2toQaq1nLr9v5aXsNiFSxeL5CQaDAqFyjvPvxTcUGn2TnuEzGcb9JN_bft_dA_5SeQC0mN9YgcKEG--kydQ8pTdZ5Q7_MKXidVG_vB4sHPO7ihWuufwUROj3KPllRNAujVA4zncpC_VvUqoUA5X_0KkuILoaw60aYCFD8_KfsCvCe7t3h5xznfcsjjP-L1gJB7zLSPPb_LqhKOlGtL6EBWubjyzX1KV_iH0L3PVrGbKkt3reoKUHedy_fIWPAXGIzs-5XqAQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نبویان درباره عبور از خطوط قرمز رهبری در مذاکرات
🔹
محمود نبویان عضو همراه تیم مذاکره کننده در اسلام‌آباد با طرح ادعاهایی درباره نظرات و نامه‌های رهبری درباره مذاکرات مدعی شد که رهبر انقلاب در سه نامه جداگانه نظرشان را درباره مذاکرات مطرح کردند و فرمودند که باید در موضوع هسته‌ای به پیروزی برسیم یا اینکه برای همیشه از دستور کار خارج شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661531" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0421106705.mp4?token=aLe0bKjg7PYD_ouWwjz5qjdFb9YOjul5NKDsvEahVPl7ypyTorRtca1Vl-mOFYxDjztXwk5ccABG1hqYlW-8AkbQNA16MiSIh7m4f9BJCxKF--sz-Z-Ceb3qh2tZUGbKcverMbMF1DFbdOq09TMse7W-4l7uLcdcPAxfeFF4dF2x2LmY325G2vr6EsbDU9EsCwXTfhMVHAb7gMeF_1uYJvIFBYuP6Un4EQ2e9LBib-3UyKQArrvWTmEsQWJ0jqLtbe2l5u-eHrrm4Ox6xygU0JxjL6k_CI4RchVWxk9sK000_4mkfJpn1Bu3_bf-_dYDkaV6v0z_2sFOL1SIDJmWfncGsDFzTqs2epuOTlG8O5ggquldDZ4CQbO9z0-Q4azqUAiMGB1xW_g13GGYpO5ZiCMHx7FVNv58Df7yJLmfdskSLovJvFGUxX3tJEeIxNkqeEKoMWY-UzyPJl-CYiAOlf89kSizajEh9g6hTd8nb64XHuXHH8rl0vlGvCEXbxysW0wJMywZYXVuqwPIQ9c7ijrb7paEtTHXEwMYFby_5wBsEHSBe9Yw_TVW00gkkk-8kecyEYkhwXiUGsL7cqTnd6ZnL_SLWTzyBinMc6qAJkHCFHIuRRETCi7IJAapiTRx-qAR8X1lMC6E_slwT_ZSUBS_3OzlFOdI67kd5IMCS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0421106705.mp4?token=aLe0bKjg7PYD_ouWwjz5qjdFb9YOjul5NKDsvEahVPl7ypyTorRtca1Vl-mOFYxDjztXwk5ccABG1hqYlW-8AkbQNA16MiSIh7m4f9BJCxKF--sz-Z-Ceb3qh2tZUGbKcverMbMF1DFbdOq09TMse7W-4l7uLcdcPAxfeFF4dF2x2LmY325G2vr6EsbDU9EsCwXTfhMVHAb7gMeF_1uYJvIFBYuP6Un4EQ2e9LBib-3UyKQArrvWTmEsQWJ0jqLtbe2l5u-eHrrm4Ox6xygU0JxjL6k_CI4RchVWxk9sK000_4mkfJpn1Bu3_bf-_dYDkaV6v0z_2sFOL1SIDJmWfncGsDFzTqs2epuOTlG8O5ggquldDZ4CQbO9z0-Q4azqUAiMGB1xW_g13GGYpO5ZiCMHx7FVNv58Df7yJLmfdskSLovJvFGUxX3tJEeIxNkqeEKoMWY-UzyPJl-CYiAOlf89kSizajEh9g6hTd8nb64XHuXHH8rl0vlGvCEXbxysW0wJMywZYXVuqwPIQ9c7ijrb7paEtTHXEwMYFby_5wBsEHSBe9Yw_TVW00gkkk-8kecyEYkhwXiUGsL7cqTnd6ZnL_SLWTzyBinMc6qAJkHCFHIuRRETCi7IJAapiTRx-qAR8X1lMC6E_slwT_ZSUBS_3OzlFOdI67kd5IMCS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعاهای نبویان، نماینده مجلس از قول رهبری: آقا درمورد مذاکرات پاکستان فرمودند آنچه رقم خورده است با آنچه شرط مشروعیت مذاکره بوده است تفاوت کلی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661530" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c988a41777.mp4?token=KPRMmkOFsE3xuAVzB8V88ZW_zu28RFoO_d2SHcjnqRga4csCryUDGobY1bitUQ58BP6za9p4-_GU46ocXro9ZAb5nfXYv5_zzXnXfT5dV7JUOX6c8NGpUH4_F8rD__h6W_dyIB_inIZI_BI9hQzg6DoZYdr9UOtuKcgHfAahy4cdgCL6OtBaTZkXTnXBMAzKwHgBOduamMhGMnQ0NdP0Cf-iCwNSwsJ9Z8Y1vjkI_ET4OobPzUlSeh6_9SBRc02p9J4NZAok2EnD-Sk5cuceVGWzK3kRQbljrCd62GjNm-tbk0ZTuLY5DYwpeaKeUChSLPnexEsxHw6q3lZtEOYVkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c988a41777.mp4?token=KPRMmkOFsE3xuAVzB8V88ZW_zu28RFoO_d2SHcjnqRga4csCryUDGobY1bitUQ58BP6za9p4-_GU46ocXro9ZAb5nfXYv5_zzXnXfT5dV7JUOX6c8NGpUH4_F8rD__h6W_dyIB_inIZI_BI9hQzg6DoZYdr9UOtuKcgHfAahy4cdgCL6OtBaTZkXTnXBMAzKwHgBOduamMhGMnQ0NdP0Cf-iCwNSwsJ9Z8Y1vjkI_ET4OobPzUlSeh6_9SBRc02p9J4NZAok2EnD-Sk5cuceVGWzK3kRQbljrCd62GjNm-tbk0ZTuLY5DYwpeaKeUChSLPnexEsxHw6q3lZtEOYVkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هماهنگی خیره‌کننده عزاداران در حسینیه میرقطب
یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661527" target="_blank">📅 21:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5aa3a396.mp4?token=eS_JNZ8R82GzNEvC_L_Bm5lYjOLACGWaLAT0Deyu9MJG4PyHtvZ7mSpMh7KhWxdNh8wkfunq4BfOnH_dG-M-0neTqRS87SNPQePbqNSU2v1lgl4QmIM9jqGTyBKabREzUaVn6ZF8Voo6UzmCD8L5f_LfZQlswimeMEiR4oo29DzXabqSViVat37hDuo9cxVRlMVcs4nNE0Veb9bS_I6ozi2gc_1cXeDQxh57eTsGSuEyyMGnQv65tnYl6OpVcl5-5ouq48ehjwHVYJ-WrYleKnjrMgzh2940Imy9cT5ceqJCes36uTZF_yqKVluiY87StoQeEMzp-DT5YXtmdD28PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5aa3a396.mp4?token=eS_JNZ8R82GzNEvC_L_Bm5lYjOLACGWaLAT0Deyu9MJG4PyHtvZ7mSpMh7KhWxdNh8wkfunq4BfOnH_dG-M-0neTqRS87SNPQePbqNSU2v1lgl4QmIM9jqGTyBKabREzUaVn6ZF8Voo6UzmCD8L5f_LfZQlswimeMEiR4oo29DzXabqSViVat37hDuo9cxVRlMVcs4nNE0Veb9bS_I6ozi2gc_1cXeDQxh57eTsGSuEyyMGnQv65tnYl6OpVcl5-5ouq48ehjwHVYJ-WrYleKnjrMgzh2940Imy9cT5ceqJCes36uTZF_yqKVluiY87StoQeEMzp-DT5YXtmdD28PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی یک شهروند قطر؛ دولت هزینه هتل و بلیط بازی‌ها جام‌جهانی را پرداخت کرده است
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661526" target="_blank">📅 21:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اردوغان: آنها که قوی نیستند جایگاهی در میز مذاکره ندارند
رئیس‌جمهور ترکیه:
🔹
جهان در آشوب به سر می‌برد و آنها که قوی نیستند جایگاهی در میز مذاکره ندارند یا صرفا بندی در توافق خواهند بود.
🔹
هدف ترکیه ایجاد تنش در منطقه نیست بلکه تقویت صلح و عدالت و آرامش و ثبات است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661525" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
محمد عطریانفر، عضو شورای اطلاع رسانی دولت: پیام رهبر، بر مسئولیت پذیری رئیس جمهور تاکید دارد
🔹
در ارتباط با توافق، اعلام اینکه رهبری رویکرد دیگری را ترجیح می‌دادند بیانگر وجود فرآیند مشورت میان نهادهای تصمیم‌گیری است. پیام ایشان در واقع تاکید بر مسئولیت‌پذیری رئیس جمهور و اعضای شورای عالی امنیت ملی دارد./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661524" target="_blank">📅 21:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b5cad600.mp4?token=qibb_tkGVSxoJ32OAIYNhoxFln1QcH3cIjFknc8gkErZlG0eR6ZbfoBK0B4TQZaM8VM0Ec_Cn5apYJqfvgzPDIq92nRd8gQP2E0rATD-hMDm9A95L5L8w1UgYhY_Q9FnGoUApZIT3AACwqvJUaS3M6WfACTrSTUTyI8A50kZXGcuSR9iRzqoWXa3utuz0zP0MZBhWD3kLFhdKbY9AFAPCJ83cjLvuFOA65yo2Va8XZ2E20_HiQNgsTjG3H-M6akqyF7luXuJpc1-_qPLcTVOR2F83vzFRkl97SfL_qrJhzn7e0XJChwWRINSa3J1MYtLKISvm5Bdw_hMvble5fzrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b5cad600.mp4?token=qibb_tkGVSxoJ32OAIYNhoxFln1QcH3cIjFknc8gkErZlG0eR6ZbfoBK0B4TQZaM8VM0Ec_Cn5apYJqfvgzPDIq92nRd8gQP2E0rATD-hMDm9A95L5L8w1UgYhY_Q9FnGoUApZIT3AACwqvJUaS3M6WfACTrSTUTyI8A50kZXGcuSR9iRzqoWXa3utuz0zP0MZBhWD3kLFhdKbY9AFAPCJ83cjLvuFOA65yo2Va8XZ2E20_HiQNgsTjG3H-M6akqyF7luXuJpc1-_qPLcTVOR2F83vzFRkl97SfL_qrJhzn7e0XJChwWRINSa3J1MYtLKISvm5Bdw_hMvble5fzrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه تیم ملی فوتبال به آمریکا توسط هواداران پرشور فوتبال ایرانی
نوشته روی تابلو هواداران ایرانی:
🔹
بمب و گلوله حریف ایران نشد فیفا هم نخواهد شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661523" target="_blank">📅 21:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نخست وزیر پیشین اسرائیل: اسرائیلی‌ها نتانیاهو را هرگز نخواهند بخشید
ایهود اولمرت نخست وزیر پیشین رژیم اسرائیل:
🔹
اکثر اسرائیلی‌ها هرگز بینامین نتانیاهو را به خاطر ناکامی‌هایش و سیاست قطبی‌سازی‌اش که اسرائیلی‌ها را تقسیم کرده است، نخواهند بخشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661522" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD1IhF-samiiF_W0MRCaf2uKLic3a9PIobOa6LnLz1ff6vxmmCaASbiX72l_wEJx4ai4WY4x56Aqa4qI5lUkDFFoTO0pSC-XDFq-Qwg5nxBqDB1-V0PsqUNc4ft-bAZHPzPrlzO2lstR9WfIDl9XmupX7alePygJKcHIfTWzH67SCRUpO04kwfkoZT1IdEjxS5iXINbUN0wS3O_083-3FpiBN2oZs7bCq5nOl3jxZmnNIWbZ6wpTTjrzictgtJpTkXG9Sk5WnLedOYa5FvSW_V6il-3ylLVGpLmxX4WxKrztzg4ltBGqyoFL4xws1jKhylGm5JNS-UsD2Qb12lP-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمجا‌چوب مرجع تخصصی مبلمان تخت خوابشو و تخت های تاشو
✅
فروش ویژه تخفیف نقد و اقساط
مبلمان ال و تخت خوابشو
سرویس های خواب تاشو
کابینت و سرویس خواب
جهت رزرو و ثبت سفارش و بازدید حضوری
☎️
02122141020
☎️
02143000098
https://t.me/kamja_ir
https://t.me/kamja_ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661521" target="_blank">📅 21:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafb52f9ef.mp4?token=Ds9P8FgJZbHKIBcRK-eq1pgDlD1QmP7sMtEX_pt-kXY3AEy038sdYtFnDM39lAnoirZ9yUJLEaA0YknDJ9Jti4sEolPTaRSBKXrey-vzCvj3TtbwqHDGw1bxNGDpCoC6U3DjKH_VXqaYJVYq1jmQe8lJgFmu6LQ4GM75ICHcvrpz4SWf06SVaemlX8Jrdhi3IOgg_364xGXex8_zz6CkutZ4Cwqhxtt1LurcIsWDO68--a89PWMZoQbUKw36M2yj5XewHjBFB_j983olX8uHsQSSvd0FsTLr-ABhKeToSKyOZCqlmR5IAci69m5X9U6jfu5XC2JfppKABqv4qWMW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafb52f9ef.mp4?token=Ds9P8FgJZbHKIBcRK-eq1pgDlD1QmP7sMtEX_pt-kXY3AEy038sdYtFnDM39lAnoirZ9yUJLEaA0YknDJ9Jti4sEolPTaRSBKXrey-vzCvj3TtbwqHDGw1bxNGDpCoC6U3DjKH_VXqaYJVYq1jmQe8lJgFmu6LQ4GM75ICHcvrpz4SWf06SVaemlX8Jrdhi3IOgg_364xGXex8_zz6CkutZ4Cwqhxtt1LurcIsWDO68--a89PWMZoQbUKw36M2yj5XewHjBFB_j983olX8uHsQSSvd0FsTLr-ABhKeToSKyOZCqlmR5IAci69m5X9U6jfu5XC2JfppKABqv4qWMW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم هلند به سوئد با دبل بروبی
🔹
طرح
طلایی
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661520" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
کانال ۱۵ اسراییل: اسرائیل تلاش کرد مسیر لبنان را از مسیر ایران جدا کند اما شکست خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661519" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه: قدرت، تنها تضمین واقعی در برابر دشمن است
اکبرزاده:
🔹
دشمن زمانی عقب‌نشینی می‌کند که قدرت شما را ببیند، نه اینکه دلش برای شما بسوزد.
🔹
ملت ایران با ایمان و اراده توانست دشمنی را که تا دندان مسلح بود شکست دهد و امروز نیز جمهوری اسلامی به قدرت برتر منطقه تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661518" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عراق سطح آمادگی خود را برای مقابله با گروه‌های افراطی سوریه افزایش می‌دهد
🔹
با توجه به احتمال سوءاستفاده گروه‌های افراطی سوریه از وضعیت بی‌ثباتی در منطقه برای سازماندهی مجدد نیروها یا گسترش دامنه فعالیت‌هایشان، نهادهای امنیتی و اطلاعاتی عراق ناگزیر به تقویت تدابیر پیشگیرانه و بازدارنده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661517" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6603f5fdf3.mp4?token=VDl3RTWSIBq99vOCS_wyyrpPHboeh4dlkELrNCjBBz5vrwY_HBzi8y_ns8DP1Vy_h75-gEeSBr5PKg9prpNB_xZnztuaLOaZrLOTz2Pa7hwDWxHe_vj2pdK1CDcMbxKOmXWZUGJ7rp3KBJ8VBd8zHb-916DsJd6aEfeB4Lys-7Zf2_L2kW8stt1gby-m2yD3xkWNgkisYwILPfJclMHKXPCGnDfbRwQd_F1FnwNkGTqfpRY48cMqN0TuZ3tZ7ngg6xjY7t3gXz3R15YKAFEySWl2WVXz4t7HANf9K1mhpKbtHkM2G7SII82bTf3lO2RR-hzmIjhLqbJdFZDxycu26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6603f5fdf3.mp4?token=VDl3RTWSIBq99vOCS_wyyrpPHboeh4dlkELrNCjBBz5vrwY_HBzi8y_ns8DP1Vy_h75-gEeSBr5PKg9prpNB_xZnztuaLOaZrLOTz2Pa7hwDWxHe_vj2pdK1CDcMbxKOmXWZUGJ7rp3KBJ8VBd8zHb-916DsJd6aEfeB4Lys-7Zf2_L2kW8stt1gby-m2yD3xkWNgkisYwILPfJclMHKXPCGnDfbRwQd_F1FnwNkGTqfpRY48cMqN0TuZ3tZ7ngg6xjY7t3gXz3R15YKAFEySWl2WVXz4t7HANf9K1mhpKbtHkM2G7SII82bTf3lO2RR-hzmIjhLqbJdFZDxycu26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به سوئد توسط بریان بروبی
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661516" target="_blank">📅 20:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EptTAV0uH3BA37h0isVWL-pzfOcgdQiIIYj6VlaAoCvIdA2m4ZJnH0xceoOpZ2ZtwbUPJ355dYJ9Tq9cQD9vrt6c5Pb_OHSru43k_U_-rH4cjDuBO-GpkClHmSSm3HFOwAzNR2QNRuds5HD8mZ8UgtGpGNhAgJHPUvxgW3bGqWQ17H_hnoib9jiqplUfu7JE7QuTGS1Xppl71Ka9wu_IQlskSGPcYW6HeezewHeoZMhlXANk02VRaLqAhe72cvCYEyNips-gI1lXwL_jlBD-jFKowP2omvHw646beD62YIIikcon-G-LvcdO9otZPPOHWhN5PrblqKoEjwNY5ZrgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگت رو زنجیر کن
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا اعلام کرد که نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.  اين گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
🔹
هفتصدوهشتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661515" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
جنگ تمام شد/ مردم سیریک همچنان لنگ آب
🔹
در حالی که خبر تفاهم، تیتر رسانه‌ها شده، مردم سیریک هنوز با یکی از ابتدایی‌ترین نیازهای زندگی دست‌وپنجه نرم می‌کنند؛ آب.
🔹
پای حرف مردمی نشستیم که می‌گویند روزهاست با کمبود شدید آب مواجه‌اند و زندگی‌شان تحت تأثیر جنگ و آسیب‌های به‌جا مانده از آن قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661514" target="_blank">📅 20:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661513" target="_blank">📅 20:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTJ4g9CJltVcrmV0ZDxAuOwAxMjO9wYUMZZRR5NC_5s--wGAby-_7u4hpjPl7WN16JsOkMJj_o7hyM0-d6FbDWH_eEzONRghXsWeoPt4pLENe38j8PrS2ZrTdr-7LmYkktJp6zLzFnIhkgx-67VukqrwMJdp1TC2bVocKnJ_YjWrVkQnwo_nyTBG4e1I3rXeNWlFkmiDCz8bflv10Mln32v_BHsNiRj4tiA9s5sPe9a1nQuEmZL_dnETMc2uL_2kBdS0bSFYV4VCSX8SN0wFkHMpi5N11vAVeIAYptnov4kZdXImAZNOYZtsN9gjSZgnbn1RHFHAXE6j2muEJo8yHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e1956840.mp4?token=csaNd3COVACHBumTNfTh5FtFUWLc2IcX5l1IfUvU5zHiSN4jFEkBiXH-eyatmOC__dprxkhfEDoKyu9nc4-9Xq0E-Dn-9n2HlrRhIivefHysedp1nLilL-q36eb2MC-3csCiR_NOp0ax1ETtrNrScDu_8rIeyEURi1QU9ijvh8RKwQIG85E18sRtRwn31DQ5awoXHNXMWtYWYxM3LzsLbtbqJGJ2ZywwykeZevRAQr7bjXMcfa0SApQlQUsCDH92QNeebALH17e2kE6FWpqoQjbpgjof_7_6XNmhCbn4DuwYTz5Cn_-bJ0SiEP9hZrOr6K6z992uVBF2IVydt9ViAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e1956840.mp4?token=csaNd3COVACHBumTNfTh5FtFUWLc2IcX5l1IfUvU5zHiSN4jFEkBiXH-eyatmOC__dprxkhfEDoKyu9nc4-9Xq0E-Dn-9n2HlrRhIivefHysedp1nLilL-q36eb2MC-3csCiR_NOp0ax1ETtrNrScDu_8rIeyEURi1QU9ijvh8RKwQIG85E18sRtRwn31DQ5awoXHNXMWtYWYxM3LzsLbtbqJGJ2ZywwykeZevRAQr7bjXMcfa0SApQlQUsCDH92QNeebALH17e2kE6FWpqoQjbpgjof_7_6XNmhCbn4DuwYTz5Cn_-bJ0SiEP9hZrOr6K6z992uVBF2IVydt9ViAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هری مگوایر در اقدامی غیرمنتظره، فروشنده برچسب‌های جام جهانی در خیابان‌های نیویورک شد
🔹
پس از اعلام فهرست جدید تیم ملی انگلیس و عدم دعوت از هری مگوایر توسط توماس توخل، مدافع انگلیسی در یک برنامه تبلیغاتی جالب در خیابان‌های نیویورک حاضر شد و به فروش بسته‌های برچسب آلبوم جام جهانی پرداخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661511" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
از دار قالی تا دنیای مردگان؛ زنی که پس از خودکشی از عذاب هولناک «تشنگی» بازگشت
🔹
00:06:30 قالی‌بافی برای حرم امام حسین(ع)
🔹
00:17:00 تصمیم به خودکشی در لحظه دلشکستگی از رفتار فرزند
🔹
00:35:30 ورود به اتاقکی با پرهای ققنوس
🔹
00:42:15 همراهی من به عالم برزخ توسط دو موجود ناشناخته
🔹
00:49:35 تشنگی مفرط باعث تغییر چهره انسان‌ها می شد
🔹
00:53:50 دست به دامان شدن امام برای رفع تشنگی
🔹
00:56:10 خارهایی که مانع نوشیدن آب از نهر می شدند
🔹
01:02:00 تفاوت برگشت روح به جسم در انسان‌های گناهکار و بی‌گناه
🔹
قسمت نوزدهم (رشته به رشته، مو به مو)، فصل چهارم
🔹
#تجربه‌گر
: اعظم فکریان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661510" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh0jj_ccEi3n9igqrl5Cxci4vVnFS02ZQ2HDxtsb7M9FskwJ3WL2XLdu92Dy0DX0pGvt8LK2o_wkg-Pl7r5cv_k5SI60xNmDnP-7TuDhWHOlHEAvap_9yLmSdtAW5tGVj2ymv3Y5OrdmjERE0jK5MMaaFw2thW94XNaaOQinDZHsKX4ZD1-5gHaYAMuokogPkh6-vNnlYla5P_S92_-hjt6ST3LBKCaG3LSxiYM4rVYnonKV-f_msEH5zgjUl0HqQfWYgCwfe2lFVx6C8fmC776MzXRPAuGZxBvlmzeOZMxMPeHTlGFsqlFvGHD_zCQQTsG67g5NO_3QibYXxmXrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه، استاد تمام اقتصاد دانشگاه جانز هاپکینر:‌ در نتیجه نقض آتش‌بس از سوی اسرائیل در لبنان، ایران اعلام کرد تنگه هرمز اکنون بسته شده است
🔹
به لطف ماجراجویی اشتباه آمریکا و اسرائیل در ایران، ایران اکنون همچون «شمشیر داموکلس» تهدیدی دائمی بر تنگه هرمز دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661509" target="_blank">📅 20:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
دیدار وزیر کشور پاکستان با مسعود پزشکیان
🔹
سید محسن نقوی، وزیر کشور پاکستان که برای ادامه رایزنی‌ها درباره تفاهم میان ایران و آمریکا به تهران سفر کرده،‌ عصر امروز با مسعود پزشکیان، رئیس جمهور ایران دیدار و رایزنی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661508" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽️
نبرد ایران و بلژیک و هیجان فستیوال بزرگ گل طلایی بیمه آسیا
🕥
از همین
امشب ساعت ۲۲:۳۰
تا
دقیقه ۷۰
مسابقه فرصت داری حدس بزنی: برد، باخت یا مساوی؟
🥇
یکشنبه ۳۱ خرداد ساعت ۲۲:۳۰ همزمان با تماشای مسابقه ایران و بلژیک، شانس خودت را برای افزایش امتیازات و شکار سکه طلا امتحان کن.
🔔
یه راه ساده برای برنده شدن:
با ثبت نتیجه مسابقات جام جهانی ۲۰۲۶، امتیازاتت رو برای بردن جوایز بزرگ، بالا ببر
🔗
ورود به سایت و ثبت نتیجه بازی:
https://www.bimehasia.com/جام-جهانی
@bimehasia_co</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661507" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
هتل بورگن‌ اشتوک سوئیس کجاست؟
‌
🔹
هتل و تفرجگاه بورگن‌اشتوک در قلب کشور سوئیس و روی یک ستیغ صخره‌ای در ارتفاع بیش از ۵۰۰ متری از سطح دریاچه لوسرن واقع شده است.
‌
🔹
انزوای جغرافیایی بی‌رقیب این هتل، امنیت مطلق و دوری از رسانه‌ها را تضمین می‌کند. این ویژگی به همراه سنت «رازداری دیپلماتیک سوئیس» باعث شده تا فضایی دنج و کاملاً تحت کنترل شکل بگیرد تا با کنترل شدید روی روایت‌های رسانه‌ای، از ایجاد مانع در مسیر پیشرفت مذاکرات جلوگیری شود.
‌
🔹
از سال ۲۰۰۷ مالکیت این هتل در اختیار هلدینگ کاتارا هاسپیتالیتی، هلدینگ هتل‌داری و پذیرایی صندوق سرمایه‌گذاری دولتی قطر قرار گرفته‌است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661506" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مدیر تیم ملی فوتبال: ابراز تاسف فیفا برای ما کافی نیست
مدیر تیم ملی فوتبال با اشاره به مشکلات ایجادشده برای تیم ملی ایران در جریان رقابت‌های جام جهانی ۲۰۲۶:
🔹
متأسفانه محدودیت‌هایی که برای تیم ملی کشورمان ایجاد شده، تنها به یکی دو مورد خلاصه نمی‌شود.
🔹
از تغییر کمپ تیم ملی گرفته تا اعزام با تأخیر به محل برگزاری مسابقه، همگی شرایطی را رقم زده که به هیچ وجه با سایر تیم‌ها برابر نیست.
🔹
مسئولان فیفا نیز در تماس‌هایی که با ما داشتند، نسبت به این اتفاقات ابراز تأسف کردند، اما صرف ابراز ناراحتی برای ما کافی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661505" target="_blank">📅 20:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4728N0gQaex2KXspFAJm1bjpTyAb_stltu4REPxgdkfsdqTEAnZOzTIG7MHKl4eTxBAchlYpeA3OhiEcV9JOX1UI9y29GctBo_gGSr9Gy2mloFotizElXZhMHCFHdYUHJUTIWh39PG6aWoTF3bJXYSsxbRix0qBH0GCXVFieYHz4g5BC2VZe6V_dhy4rwzyazRkplnpCMgxdQ10jiV61nuHWLQhVMtOyySL0ZOR2S4AyhFlxrOw2f17gByZ_iqCZX4guinr0_bJY0f16V580f9Zv6Sw4h7bjwBRTMT9G0AM6LeyGj5cgHOhY6Pm2ylmgSqp0MbfXegoLzsrNWFGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnG25erurjV0xrMG7ZHq4PzmeW_jCx3-4sQW4wxkF1BDa8enp5u-2Z5i74KSX29vGX51JzQ4twEYgMZapJnLDrb-iF4UnGn4M09Hth5GifP52kYsc2NmRgIK_SuT4TjVxeMWumPJ0rh98Y-Aer5zo8kv0SI34ad1NdK99GQD09CGxn0PoMigu4BEBaLLyb02XSf7lzyX2rwZv421b9nWjVX3uESjgzPiejYp8jccTghxG_XH-uyaKNDRWX9YJ6r5ARNY9WcFkirRnTvUWYltMTyVZ4U6hiGBY38o4PM8l8W_EoyuLTXN6MHyksXZR7uUG77p3KtanLP5oRDXMDzg5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر کتابی می‌خواهی که اشک را از تاریخ جدا نکند، «آه» انتخاب خوبی است
🔹
«آه» فقط یک کتاب تاریخی یا داستانی درباره عاشورا نیست؛ روایتی زنده و نفس‌گیر از لحظه‌های کربلاست. یاسین حجازی با نثری شاعرانه و تکان‌دهنده، مصیبت‌ها و صحنه‌های عاشورا را چنان روایت می‌کند که خواننده خود را میان کاروان حسین(ع) احساس می‌کند. کتابی کوتاه اما عمیق، برای تجربه‌ای متفاوت از عاشورا.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661503" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661500">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbPScGKmfdmoVDXZ4ggXyurjJ-eEyqmQeaoe03cOf2zXJqHEQ6Eb3W-9hc-v82Qpi_4ouahDdccGjUYTktUX2ii_CYnNyxPtvRnU7zze2p0SvtPTInvvwjX6e8fwthr3BzoUSeWxY5LgG_JKOdZmxJpyrbxJDKLMkXoc_0oZ4knCrQNbjUimgDtCyIoio7IXJr9j0P6IACtmhne6M1KRlG5d06TEChUVA9YcsS-uy77EaRerB4iaSNBoT-HKDUGJpEbcArtdO1CyDJJz6zp3HmuovY2xgx-XWXBY8_F1yTBnmZpm7LJQClLOzMu10blpY7KRtY_4PnS7_wAGNDdkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_1oTy11naDJOKiiJ8R3r6jSEjuIvJg2-Cv5YJENX801ccA7U4v-Uli3tSGMXjVF5zXRLik4LDTXYLf_TWsS9WZCAonp_vKclg4PEwmayEtRmRV8grhY9qT4ztYtDWLM_Hn3YK4FSfsfbydWza0vOAx0XTeM2sJGZ3V0jrIxvicJlpfVxphXW3cy7MONgNq3fUD_J5O3ststMzVg5xjkfjvg3DgPc9u5b6EWfXtK4GUNR-XFuaLdpdhZInqaalTH1IMCYk3ZsAaVgogWuU3a_-FAFBFQ04fJRozaCccFcDeKc31ZeTHPGKoSv9rF4_sALf7B2JWqx9Y2sgfJ-wbH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU1fVNclBrN3ueVhHRKVeNxNWDfu155NTLt6c07zimJE5IYOTwfK42iiOrY95e3B6wLhdO_LWrseUIOiLtnC2EQBmKuRP5h-9WJiXOxh14b3qLs-iP_uj0hhx3iXQpV2e33xRCaKb_BXKhdpJbNHmloRgCq40mq8nASSXPE14hWvGBYF5HKUFGS_CSsHMABo9D816rxn-9DW2JtqMthd0annBCXCrCZdbwfBYacNMW64TuMoMpu2wNPAYDSMU2u24UPHuWSZ3h62tcbckKYlfFixohnnCk1dewTiMHPu5M6xbUmFnGhsbQxXT5gGXSYo9lak7K9SAkcYd5Wmn_XjwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرود عجیب یک پراید موقع رانندگی روی پشت بام یک خانه در اراک
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661500" target="_blank">📅 19:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مسئولین ایرانی: دوستان لبنانی خود را هرگز تنها نمی‌گذاریم
🔹
در پی اعلام بسته شدن تنگه هرمز به عنوان گام اولیه در واکنش به تداوم تجاوزات رژیم صهیونیستی به لبنان، مسئولی ایرانی به شبکه المیادین گفت که جمهوری اسلامی به هیچ عنوان دوستان خود در لبنان را رها نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661499" target="_blank">📅 19:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661498">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی مجلس: بستن تنگه هرمز اولین گام جدی در مقابل جنایات رژیم صهیونیستی در جنوب لبنان است
🔹
جنایات خود را متوقف کنند تا مجبور نشویم از ابزارهای دیگر استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661498" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661497">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661497" target="_blank">📅 19:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661496">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدود ۱۵ سال پیش بازی‌های موبایل به این شکل بودن
🥹
#نوستالژی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661496" target="_blank">📅 19:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cm7OGR1hKKtEmc-PjRRS4rtSYnphWqqdKZFWj2k5yRBgg8ZsB-Khw3xQ7wVoOMLxsbJCD8KXtVNsgCNcZswpsxKZ9vVE0w7_EbMT0qUNmyhhTOCxGp9FKG1siEw2lpCGz5F3aoZy4EV63ixK9eoqYNOMvWf-DGrcfSwxY0zsoa_RI4m9R49cChuZZsL6xVkUCr-3MiJQdIdYYckAcl8lV7ZblLFj3YOavwhg4TzlbUJbU7sXIJu7npfDNECuD6fwLKQIRzxmUYtGDO4Ap9VRqgMNjwVxzGK8zFyhsARmjPSXM2C09iiFLk2y7PHCBKRE4Fa4v340U5MW2kU1etEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661495" target="_blank">📅 19:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: بمباران در اطراف شهر نبطیه همچنان ادامه داد
🔹
رژیم صهیونسیتی در تلاش است ارتفاعات اطراف این شهر را تصرف کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661494" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRocslNlumfLtrNBeJXjwqdqS6OOj5WPkAM7G10yqFNKC3N5oqyeGc9drZT9kbI1jlZZGiPCa_ZPVu1KcRrHLoLSXAna6KCiNYXh0Ec4vrRHHnd8XjvQAv6gIwDaigsDtZJcFYMgS24tBOhpgEbtE9uTK8-FIMXiFRkFHoDf7CheljXKbwmXek6gYKcqJk2Ka7acoLA4ONEEwF--EsrdypfQ8khcvVsYBrJSoiI5S1NGqokHnZbrD0Ws2CYqCn1sHYHbrIhtpzMq1FZ0BXkwBCFGH3w9VbVndURF4oGi2ytItInM8AaAzPj1lTvfxG14F2nU5Lrf0JpeBuNWUV1ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661493" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6Ldhgza2cE5lsPOkLcrQ0dZ2U5WJLqgczCTDcNpokILJH0WIr8lwOEA_pVEY8-DCQ4Oci6DMK7KV8cBOTMt58tPUOxGimm357Jgq2TywTPqJ19qXI1Y8UmknAPS4hPj2onAMsKCIYIHz2L-z1Ee4HznpJBo7Pykelzturm8e--7rqGIQzQmzLuxvCvOeQuAxoi37dinG_vmFx88Ff2ffKxHOY5Mg9oUwe25_LCRH_6bLMIA3xY_yoN8PIbjB4dbGbNjlw35QbyCMrDoNc6htF544sKoDgKzG8jGiGcdSRGuACFB1zSVsmhGF4DhNaGbzt-kdOe--7ac6fVoJgWciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، فعال نشده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661492" target="_blank">📅 19:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردی اهل ایالات متحده یک Wall-E لِگوییِ واقعی و کارآمد ساخته است
🔹
این ربات می‌تواند حرکت کند، چشم‌هایش را تکان دهد، به کنترل‌های دسته‌ پلی‌استیشن ۴ واکنش نشان دهد و صداهای انیمیشن را پخش کند.
🔹
درون آن موتور، سنسور، بلوتوث و چراغ‌های ال‌ای‌دی کار گذاشته شده. او همچنین دستگاهی اضافه کرده که قادر به ایجاد تخلیه‌ الکتریکی و شعله‌ور کردن اشیای کوچک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661491" target="_blank">📅 19:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlPkqcUUeZLpUXri1pFA9PlXHGGjZ7WP371zW9Bv0luQWFF3BE4jO4LeXp2BkzgH6yWpsS8ndPsxTcDUIi6WvenFm6VK6slp8ziQ73RfW79E9Awlph_iUhvSt0BNyFS_Cpj2wDs1AYymajcrVvX4kR5_9Wx3-NT-92rl5ibAXzKFqNbWcoP1RV9ao4Z4kxHTZFD0uPKgLrHb6L6CyIAW5S_MpA9j-ZIFB92-za5Sry8syq_M6lIuKlK2qbtI0CCy0JYsjeh0utm1tejr_05qlT7mcMUY8kjCanjKhdizkiv0RD_UeQZ5GnGua7O-2nfpnUJX8lBd-s0UlKXpU249DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلیدهای میانبر در Word را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661490" target="_blank">📅 19:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFXojKgCtZNPpPg80tyyKw_ARefCQikYM6q44zv5d-OXySIz2Z4lS65LUb_MUxrIXN2ToHGOVqLxqNRdRVSTZnQWtPsCnd-C3SVZjtZ-tkMKErgfKn2mCibbQE4gM2KBOOopBknF8elnpsyCHuOyxCvnMuY86OUIUUju4mCbavv12B4ppuXJgNHPPjhqT5vrH1ZVp4LW7BWVbWwZS76aHWoeSlzXXegEojtGC3WaZuGJYgMcXWyp33aQfxJBDsZwlJg0vRghnwfgoI5mrhIkR9xVMS-98Pl9EWB_4p6nzQiPASWFNVglBN7AHg0-PJ9qjqFe2F72lkQ4zDC8yLBZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سقای شهر»؛ پیوند خدمات بانکی با خدمت‌رسانی به زائران اربعین
🟢
بانک شهر همزمان با آغاز ماه محرم از اجرای طرحی با عنوان «سقای شهر» خبر داد؛ طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا می‌شود.
🟢
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه خواهد داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می‌کنند. این امتیازها در نهایت به بطری‌های آب آشامیدنی تبدیل شده و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع خواهد شد.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661489" target="_blank">📅 19:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyIO1iJeANLJFkCtBS4TG3-9IO-MDIBH7Fb9C_UoTtIHbM3akzDjbzBBPiN8pK1pNOOHCuncnWjGlaR8vON9HCGfidw6toQ5NsHJGB30X6reNHnTAgOM56LtC3kpKuBkUAU9tVd_9Lg8ogN8hBjRoDtDf89Rh_wamnrkZkOAYHMpnEj27XHDg8PTeFJgEl9LAHBrDAZTl7Yf0WVywvUZLMBt8t7vS7MRM16QhFIQMhQA2esRhSiJJU6ncx_prfXtJ7siROvleZoGzAJu-ec64ww9nZTudp9Y1uoeiVkaoBpoxulm-H1aALZCuKpn7QMjojJQgGWjUc725BiyI_yGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران‌خودرو: دوباره گران می‌کنیم
🔹
ایران‌خودرو که ۲۷ خرداد قیمت ۲۵ محصول خود را افزایش داده بود، پس از اعلام وزارت صمت مبنی بر لزوم اصلاح قیمت‌ها، قیمت ۳ محصول را برای مرحلۀ سیزدهم فروش کاهش داد.
🔹
با این حال، این شرکت امروز اعلام کرد این اصلاح فقط مربوط به همان مرحلۀ فروش بوده و پس از پایان آن، قیمت‌های افزایش‌یافته در ۲۷ خرداد همچنان معتبر و قابل اجرا خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661488" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7H366pqXg7iFEWd4kYqtn0DPuC9G6Dni1SjK-4P7IIJZRoRD4hvqpfdN9U61wUMW3NnlWwcUyuE8MWT4R9YHMW32kH5UgU6dzISxlV3f4Gt4QzvghobBhq1KRZ7jmnS1OlbpcXfvFvE2ALX_M5s3uzUIWGQewmR3XrEOpqmxS2ilPv67ebZ0lJqVtA2QCBea5DSIQvdQeAeFe9zuoj2uasOL7bfBZh1_LHb8FjcS3Mc6nWsbd6VyPrlk3mLF1WRH9jKAJADFVEFHU627xgG63oA7eTpomXXDdK6ma-jaao6Mhzl0D4dQ4ksLBn5lTyQC0WhvfR_gtHthMNF8XOCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661487" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661486" target="_blank">📅 19:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661485" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مهم‌ترین حواشی و اتفاقات جنجالی ۴۸ ساعت گذشته جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661484" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد داستان جنگ در برج آزادی برگزار شد
🔹
دورهمی صمیمی اهالی رسانه و کسب و کار با نگاهی به آمار رسانه‌ها در جنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661482" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbWCq3Dz7MuNZua5f0kJXs5zPuMYEdqHRrQbrovHyhsxZYVOhcqHl2m6NzfOtIRqYnAEEXuqTbkIgcQcQLNYD9QxqEHAetGLsCTYJCKpTbnTRgjsDdATOvP1v9XCHw9aRbVkGzMciBTbKprccQGxAB5xcQSeEuExhh0qkAu1BzDlaLJjHj-CbEy7ILykJm-6RWK5pCV_OtNUPhiLHZFcDHHm8P9ce_Vxn_7riV13T3LTbpcpKn1VUHardizQoDDdV0qlA6IomysQxclMlkL581ea52HZg7AVkvnoq5NoYRCQ0h-vfIZ90rr0uN6DkvbAmODaj0aNtfTR6ep5I0QpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاج حسین آقا ملک؛ پاسدارِ ابدیِ شناسنامه فرهنگی ایران
🔹
حاج حسین آقا ملک؛ بزرگ‌ترین واقف تاریخ معاصر ایران و نبض تپنده‌ فرهنگ ملّی. او با وقفِ نفیس‌ترین کتابخانه و موزه در قلب تهران، ثروت افسانه‌ای‌اش را به دانایی پیوند زد. مردی که فراتر از زمان زیست و با…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661480" target="_blank">📅 18:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
هشدار جدی مقام ارشد ایرانی به آمریکا؛ مهلت زمانی برای توافق محدود است
🔹
یک منبع عالی‌رتبه امنیتی و سیاسی ایران در گفت‌وگو با شبکه المیادین اعلام کرد که میدان نبرد و دیپلماسی در هماهنگی کامل با یکدیگر پیش می‌روند.
🔹
واشنگتن به تعهدات خود در قبال لبنان پایبند نبوده و این خلف وعده از نظر تهران کاملاً غیرقابل قبول است
🔹
جمهوری اسلامی ایران هرگز دوستان خود در لبنان را تنها نمی‌گذارد و از حمایت آن‌ها دست برنمی‌دارد
🔹
ایران نسبت به محدود بودن فرصت‌های موجود برای پیشبرد تفاهمات هشدار داد و تأکید کرد که زمان برای طرف مقابل بسیار محدود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661479" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تعویق یک هفته‌ای امتحانات دانشگاه تهران
🔹
تمامی امتحانات پایانی نیمسال جاری دانشجویان دانشگاه تهران با یک هفته تأخیر و از شنبه ۲۰ تیر، در همان ساعت، روز و محل تعیین‌شده قبلی برگزار خواهند شد.
🔹
آزمون‌های برنامه‌ریزی‌شده برای روز ۱۱ تیرماه، به تاریخ ۵ مردادماه ۱۴۰۵ منتقل شد. امتحانات دانشجویان مقطع کارشناسی در تمامی واحدهای دانشگاه تهران به صورت مجازی برگزار خواهد شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661477" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF7ntaKtKpKEmn31JXFaY_yzY30oK5atE3JFyPCyAwyIOe3UcMhde8mblaUxdLEXLU4NScbnLifLNrV8qikNqpIXmNE0ukwI4rZU8NmRaGmod0is4U-U0wXZHVxzZ0M_CYPb1LzKzBO5pknot5qc6OgDv5HoFiDk_VduXozIkeM2eG2qU4gdSNrhBbUBxLQKJz1PYIKb8V6E8f1V9v2NUEayg_rFQkJxhf75_MQ7MI2g47FPiJXelAig_KzU6DaHeSFZcwkgL3CwoKKDDakFKRiLNqT8aNru3IT6e91kvqBA4Bl8UYNvPjfESSNKxGzYYyrbzj_rQoTDhxRhVRKAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین خبر از وضعیت میرحسین موسوی و زهرا رهنورد
🔹
میرحسین موسوی و خانم رهنورد، از بیمارستان مرخص و به خانه‌ای که ماموران امنیتی تعیین کرده‌اند منتقل شده‌اند.
🔹
وضعیت حصر کماکان پابرجاست.
🔹
طبق خبرهای رسیده، روند درمان میرحسین موسوی همچنان ادامه دارد./جماران…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661475" target="_blank">📅 18:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661472" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661471" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661470" target="_blank">📅 18:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی عجیب جاخالی دادن کامیون سوخت روسی از پهپاد اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661469" target="_blank">📅 18:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMG8Gy_iXwNB6xmUCWCMIB-kJcmzYDnnYRWWzgBMF1zwDXQsURIirGYLDsLE3muolcxb5vC2A2IFKsvoTFpMcYOtvIvHHglwwblq4OeyvEI6xB0318BNZSkp_6fREdSevp783Kq2xXPk9aVcLYIXumMK4VStf13pIxEdG8ltcCzJbGk7CTPBuEXq5nAVIk2Mud-vhxRwkn47V6ON91J0EDVsSBw_u2Xya-FuSkymq3BMOe4lIO_-927e4pUS1uyPD0_onGA2FE3ZhbV3uj-nn_SAb3Fi2S_jFWVSu3pIa3105P5xIJCad-Tn3VC9CI0Y7SLr2sjxqcMYrNv2F6Mxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج بی‌سابقه حذف حساب‌های اینستاگرام؛ باگ یا سیاست امنیتی جدید متا؟
متأسفانه در روز‌ها و هفته‌های اخیر، گزارش‌های متعددی از غیرفعال شدن و از دسترس خارج شدن حساب‌های اینستاگرام  در نقاط مختلف جهان منتشر شده است؛ موضوعی که صرفاً به کاربران ایرانی محدود نمی‌شود و بسیاری از کاربران در کشورهای مختلف نیز با آن مواجه شده‌اند.
امید مهربان، پژوهشگر حوزه هک و امنیت، در گفت‌وگو با ما می‌گوید: «از زمانی که متا سیاست‌های خود را در زمینه مقابله با حساب‌های جعلی، مجهول‌الهویه، ربات‌گونه و شبکه‌های فعالیت غیرواقعی تشدید کرده، حساسیت سیستم‌های نظارتی این شرکت نیز افزایش یافته است. این روند را پیش‌تر در جریان پاکسازی گسترده حساب‌های غیرواقعی و کاهش میلیون‌ها دنبال‌کننده از صفحات برخی چهره‌های شناخته‌شده مشاهده کردیم.»
به گفته وی، در بسیاری از موارد زمانی که یک حساب به‌عنوان حساب جعلی یا مشکوک شناسایی و غیرفعال می‌شود، ایجاد حساب‌های جدید با مشخصات مشابه می‌تواند ریسک شناسایی مجدد را افزایش دهد. استفاده از نام کاربری مشابه، اطلاعات هویتی یکسان، تصاویر پروفایل تکراری یا الگوهای رفتاری مشابه، ممکن است باعث شود سیستم‌های امنیتی ارتباط میان حساب‌ها را تشخیص دهند و محدودیت‌های بیشتری اعمال شود.
مهربان معتقد است: «بسیاری از کاربران پس از غیرفعال شدن حساب خود، از روی نگرانی و استرس اقدام به ساخت چندین حساب جدید می‌کنند؛ در حالی که این تصمیم در برخی موارد نه‌تنها کمکی به حل مشکل نمی‌کند، بلکه می‌تواند روند بررسی و بازگردانی حساب اصلی را پیچیده‌تر و زمان‌برتر کند.»
او تأکید می‌کند که بهترین راهکار، بررسی دقیق علت غیرفعال شدن حساب و پیگیری اصولی موضوع از مسیرهای رسمی است؛ زیرا تلاش برای دور زدن محدودیت‌ها یا ایجاد حساب‌های متعدد، ممکن است دامنه مشکل را گسترش دهد و ریسک از دست رفتن حساب‌های بیشتری را افزایش دهد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661468" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661467" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661465">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbHzUdSYnbA4DRv-P_bgIlZRT6hB7zKW5ODSZslqPi2LekroOQrmUpQFqQdHGmxr-yEhkOd-_0uMzVIdBa0GU3Lwpcf37tH_kjGj0_2h_-GxNRnezVkT_o2utIIVCgRKOKFxwg9NkDu5LuarQcL3-xBacYuChStionTY2X5ufd16UKZvP4_pX9B7rKXmT_P3sDAMZ0ENc4StelcIJE47XI7z9RAPR39_L8VZPpxqj3md7v6nc1joXcwxiVpqZc8jA3gGLAfvYHJaVV488oIkpLQouXvg8qlnZLvn1uHd6x9MEIMGywEvIEbXi5ay78j4StTI1mRsmdTtLwUgaqk4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام گروه خونی در جهان رایج‌تر است؟
🔹
O+ رایج‌ترین گروه خونی جهان است، اما در اروپا A+ بیشترین سهم را دارد.
🔹
O- می‌تواند به همه خون بدهد، در حالی که AB+ تقریباً از همه دریافت می‌کند.
🔹
توزیع گروه‌های خونی در جهان یکنواخت نیست و هر منطقه الگوی خاص خودش را دارد.
@amarfact</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661465" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661464">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد
🔹
مذاکرات با حمایت پاکستان و قطر به عنوان کشورهای میانجی برگزار خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/661464" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661463">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIP9d58TzwDeKv-PW1Q3ERuKf2eLvH0m9HVF0aMjAZSsqVqTSOB33LPcy2u8j5OqHIa1mi_KAZfionL2vhAnWuksob63bXoFXNpkK-o8OUT8dqowtY6PKk2wdHrocfWLGVUeBoff9xENcUPHV26eRaRUWmZp-69iKkYeEdFrPamWU52bBX6PTd_HH_DXquXOIX1P4Y3EnBEXM2ml7RE4ISpWxCjpdUJ7DutGRbxa9qCZHPOoyTWgrGbjNtbUxdsIeCroTApCE_l7jyXh5V4S-8IX3CAvJxyaJrelW27FDUa-0tvOTx-05uPpGGbD5JLJOgl5fwnXhdOXaCjWl1JjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی صعود؛ رویای ایران و نیاز بلژیک | نتیجه بازی چه خواهد شد؟
🔹
تیم ملی فوتبال ایران شامگاه یکشنبه در یکی از حساس‌ترین مسابقات مرحله گروهی جام جهانی ۲۰۲۶ به مصاف بلژیک خواهد رفت؛ دیداری که می‌تواند مسیر صعود هر دو تیم به مرحله حذفی را تا حد زیادی مشخص کند.
نظر شما چیست؟ کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3224518</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/661463" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661461" target="_blank">📅 17:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
🔹
وزیر امور خارجه ایتالیا اعلام کرد که بعد از چندین ماه تنش در پی تجاوز آمریکا و اسراییل به ایران، سفارت این کشور در تهران  روز جمعه بازگشایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/661460" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/661457" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: ما تعهد را امضا نکردیم که اجرا نشود؛ رویکرد ما تعهد در برابر تعهد است
🔹
اگر طرف مقابل ار اجرای تعهداتش سرباز بزند ایران هم با تدابیر لازم پاسخ خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/661456" target="_blank">📅 17:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661454">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درخواست‌ برای افزایش ۱۴۰ درصدی قیمت نان!
امیرکرملو، سخنگوی اتحادیه نانوایان تهران در
#گفتگو
با خبرفوری:
🔹
در حالی که نرخ جدید نان هنوز توسط وزارت کشور ابلاغ نشده، مسئولان صنفی اعلام کردند گرانی نان صرفاً به خاطر آرد نیست (آرد حدود ۱۲ درصد تاثیرگذار است)؛ بلکه هزینه دستمزد، انرژی و اجاره‌بها افزایش چشمگیری داشته است
🔹
با وجود ابلاغ نرخ‌ها در اکثر استان‌ها، تهران هنوز در انتظار ابلاغ رسمی است و نانوایان خواستار افزایش ۱۳۰ تا ۱۴۰ درصدی قیمت‌ها هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/661454" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661453">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس به فاکس نیوز: دیروز واقعاً ۱۶ میلیون بشکه نفت از تنگه هرمز خارج کردیم
🔹
ترامپ به ما گفت تنگه‌ها را باز کنیم، و حالا این اتفاق افتاده است
.
🔹
این یک رکورد است، حتی از قبل از شروع درگیری‌ها نیز بی‌سابقه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/661453" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661452">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس، معاون ترامپ: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/661452" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661451">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: اگر بخشی از تعهدات طرف مقابل اجرا نشود کلیت تفاهم دچار مشکل می‌شود
🔹
طرف مقابل باید هرچه سریع‌تر تدابیر لازم را به کار بگیرد وگرنه کلیت تفاهم دچار مشکل خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/661451" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661450">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mho1zYX_tewnTeKAFeIDBZBrigqBj2McKurzwC87E6P-fjia3O4PQ0fPyYZJejPezjFjRr4kH2cYTsht6NZV1ITWS8Jzj-f6jsLiBRU2YgFmywbPgUWnQhBrRqd8PR0GAbn-pibKmmLZrC8nYhWtjJH7w-y_VTxmykwpzLwYupUWerxs96x9vmn6naeJmUYw6WanfriXGRQcHCVUOV5WnMVyUQfYIZliTELOwE7yXhcyQ7xCW4O7gVu9D6bWzL_WIbRNB2S8qX2i8FFmm4iz7epf9PAeRyCQ4ejVS1FSKqu4rWxiqVDkogS9eftc5HUssxb0VtZrWwUr8AM5WMBlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین پاسخ ایران به حمله بزرگ اسرائیل به لبنان/ این اقدام تهران ترامپ را به وحشت می اندازد
🔹
شکی نیست که اسرائیل از تفاهم اسلام آباد راضی نیست و شکی هم نیست که تمام تلاش خود را می کند که تفاهم اسلام آباد را نقض کرده یا نابود کند. بهترین روش هم برای نابود کردن این تفاهم، حمله شدید به لبنان، نقض آتش بس و مجبور کردن ایران به حمله موشکی به اراضی اشغالی است. بدین ترتیب، جنگ، مجددا از سر گرفته شده و تفاهم از بین می رود.
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3224502</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661450" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritPiNDMhzL2AgZSZ2CCA0KMbL8XbjqrDFGUiCBPIonXYvnQ8cnEy07SF4g4OkwgQO_swZhHJ6Tn-Ae1lVPJxkxHmiE3cXH1L6HucRb3MIUxKUl5dmKYQJiJApPlNQe0zc8soFl5TBtc934rXV-mlC4Fj9vt4FSbehzi67kG5ZGz3tw5iYwJ0jWTkLQQ73H3U7SVEn3_7gW9apVSvumR-XRx944S0sViODORHwqeYMhZ5cf5ZUPC8naHq1PuDeUXzb3Gh7GE8jRftzKzBdNonNAkRksM9cNJkqnYsETTe40mFfrVTwUVAwkD6BSvbEz7PP_M4PSrSnyVGLcti5wuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روضه حسینی
🔹
همراهان عزیز خبرفوری اگر در این ایام محرم در خانه‌های خود روضه برپا کرده‌اید، عکس‌ها و ویدئوهای کوتاه آن را برای ما ارسال کنید.
🔹
منتخبی از این تصاویر در کانال خبرفوری منتشر خواهد شد.
🔸
عکس ها و ویدئو های خودتان را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661449" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661448" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/661447" target="_blank">📅 17:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد  ‌
🔹
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/661446" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/661444" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حادثه در فرودگاه مهرآباد | پرواز شیراز به تهران از باند خارج شد
🔹
هواپیمای پرواز شیراز به تهران، هنگام فرود در فرودگاه مهرآباد، از باند خارج و در حاشیه باند متوقف شد.
🔹
در این حادثه به هواپیما و تاسیسات فرودگاه آسیب وارد شد اما خوشبختانه تلفات جانی و مصدوم نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/661443" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWYt_ZoP99a80Mc4CK6UQmB4NSqDgtvuW_rlBRg9oGI_3H9N1MAeXwJpkDpXMQQXo8QfGJuWd4ACEuJC_SJTmysW1Zp0F9lYWDidzNC8XKiUn2MJgLaWrhLNraLerXHMwNUEL_ePRc5wuJ9mtIBaqfCxWhVPEHTlMOU-1Zmadq-LeUm6PRJiZdBoQ5ebwonCD19jz01swXp1sGOoSSb37MIpdLzyGWhOytHt1B52eMgDn6FOeLuBa3sv-2qtBo9T5gKt75rhUDT-l33NZW5MaV-DmUzjLJbmjza4Fe3xnC9RRbZR1PwJMUJBK0JW8OtoajSVNog86wlP3ArYTDYqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر ملونی، نخست وزیر ایتالیا را تحقیر کرد
ترامپ با انتقاد از موضع ایتالیا در قبال جنگ آمریکا علیه ایران نوشته:
🔹
او زمانی که بحث جلوگیری از دستیابی ایران به سلاح هسته‌ای مطرح بود، از آمریکا حمایت نکرد. حتی اجازه استفاده از باندها و فرودگاه‌های ایتالیا را هم به ما نداد که یک دردسر لجستیکی بزرگ ایجاد کرد. با وجود اینکه آمریکا سالانه صدها میلیارد دلار برای حفاظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند، آنها از ما حمایت نکردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661442" target="_blank">📅 16:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ونس: به مذاکره با ایران فرصتی خواهیم داد
معاون رئیس جمهور آمریکا:
🔹
مذاکرات با ایران فردا امکان‌پذیر است و وایومینگ و کوشنر برای انجام این مذاکرات آنجا هستند.
🔹
اوضاع در مذاکرات ایران خوب پیش می‌رود و انتظار دارم به سوئیس بروم
🔹
ما به توانایی خود برای حفظ آتش بس اطمینان داریم.
🔹
به مذاکره با ایران فرصتی خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/661441" target="_blank">📅 16:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661438">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه‌ پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.
🔹
متذکر می‌گردد این گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/661438" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661437">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شکستن طلسم ۳۰ ساله بوکس ایران در جام جهانی
🔹
مهدی حبیبی‌نژاد با شکست نماینده انگلیس مدال برنز خود را قطعی کرد و طلسم ۳۰ ساله بوکس ایران در این مسابقات را شکست.
🔹
او فردا در مرحله نیمه‌ نهایی به مصاف نماینده آمریکا می‌رود. #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/661437" target="_blank">📅 16:35 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
