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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 532K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 22:35:21</div>
<hr>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=vj--5Nyvtw_Du_7uqZ0V-hOFp7bJHjuBp1ZwJKDTOvJyzFlTEclvmlwR8Yw1V5ILS7gyQKLJJcOj8LtFJUzsAkjX3rCXc9gKPxu6Y52L3XfxVowbpoxeX5Ial_eJo0nRQ1zUgI1c8vYYefHwOO2GUNtt7o-2Ggc3RjLvMQX-ED-t6cnFZnvwoFuN412UElg01LWRt_X6JOW2gTTvYV6gZ0FY_ILSloQvGG5nSHP36c4BFeQBalyQ4dmDaVEqalm1bqFgEw0GV0XJ1r_whHrpKfOrSB8LITLkCMw7IYPdXKzDFVagsibTdz7nDaDQpxmTIKiq26vZjt9cy-9o35emJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=vj--5Nyvtw_Du_7uqZ0V-hOFp7bJHjuBp1ZwJKDTOvJyzFlTEclvmlwR8Yw1V5ILS7gyQKLJJcOj8LtFJUzsAkjX3rCXc9gKPxu6Y52L3XfxVowbpoxeX5Ial_eJo0nRQ1zUgI1c8vYYefHwOO2GUNtt7o-2Ggc3RjLvMQX-ED-t6cnFZnvwoFuN412UElg01LWRt_X6JOW2gTTvYV6gZ0FY_ILSloQvGG5nSHP36c4BFeQBalyQ4dmDaVEqalm1bqFgEw0GV0XJ1r_whHrpKfOrSB8LITLkCMw7IYPdXKzDFVagsibTdz7nDaDQpxmTIKiq26vZjt9cy-9o35emJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=MCa_eMqxvizbrdBk1ju7nGQgIFn19uMTtUM-fuNovqNVvYrYXM_-NOcAI7irTQ5OEh6dYT2pI00q6kO0dfiaMldBYSat0TyBOOC_o7jK2Ohp7vsU_vegZ7f9SeNnKN96OKDxHDrne3Y_VLUWVVoo7nGl825MYFmMKBDg8bg1t5LzI_SoZ_83Tx7wLels4GQQtNqMkAKnZEq0A71Q1fqcY_n1TiTL7lPE-dZOg_j0iRwBK53-WSi4RHi8_FPjxzyUQYKT9rfZc7gCcYLMrRR1ZlGj90cTyrKoSHJIzkFV8bIcFK7uRxIK4FuRGbyRyigtpt_5LGObtaD0c8hanbJKTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=MCa_eMqxvizbrdBk1ju7nGQgIFn19uMTtUM-fuNovqNVvYrYXM_-NOcAI7irTQ5OEh6dYT2pI00q6kO0dfiaMldBYSat0TyBOOC_o7jK2Ohp7vsU_vegZ7f9SeNnKN96OKDxHDrne3Y_VLUWVVoo7nGl825MYFmMKBDg8bg1t5LzI_SoZ_83Tx7wLels4GQQtNqMkAKnZEq0A71Q1fqcY_n1TiTL7lPE-dZOg_j0iRwBK53-WSi4RHi8_FPjxzyUQYKT9rfZc7gCcYLMrRR1ZlGj90cTyrKoSHJIzkFV8bIcFK7uRxIK4FuRGbyRyigtpt_5LGObtaD0c8hanbJKTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oilq_DuEZemsLUN_eTs5fiMfr86yaHi-2gH10rhB50bV16swDePSZjsHrmzVdEC5o_yxnQvJK2RK5BoMzEwNjFAuAONusyypl047yKw3KOUymInItOeDKqCc9I0RutsDw8hnQjJTYVSYxSms3oJTYtXb-xJTIhmocW_HuLy-t5kNkvVKKaNlvMknrKBRdwS39wB2TN95L7TsaIXlp8LV0dOTGq21ZO_OBV-15bWqyY_Da9uZjawxK3fiWq0_qCDKdqA8L7kTHnJDk5IS3ibblMrnU5toCD1CEDGCGOCc6-9C2tGv7TaXb5XtJhK8HW78WOVn0bSfepx2_a94lSsZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6CKRAET_vMMOPC4JwyTIEA15YUevjD1XFiCJcpH6XnI5ZmTLmUjjw5tfqF8_2knAJAX6wMKFK8Mn42F9YQIZIVVuG0RRNAzRVAMLR4GLRrgWVnSkaFMWSr26hVAszJ441Ptpq4xedaQdyhuyZ7YFp80B-zOKtaOgwdJRHVAODBA9trVJrtOSnSco1-HWAbv9cCffXXMdbbRJ1FzukvwZLS2G6zJEFM_SJcNaIE4-i7hc6gSGVpE1tTjSWmgC2KfvUwp3VV6XZHLiPjfUJl4jRdz55C9PWql7j7a-cwW4WvYDZRx1l_OY12Cx-tGSRHUN22vt869wpkEzbooNo7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7mKsBkuQWcXH8h1mGbDhiknWPOGUoILKFdldNBNWWebfHho7tnG6RJIZZ7k3tO4TNOM_ouhK2nE-a3m4kfpsppO7-zmk9Im788JBdQGgJNgZJofI25AOgulrGwhtEWraHrxzXQ3bquCm-iPWae47Pjf_7GvGulWPq6KP49WElcNLYYk1A0OFAyNw8dco1LIMeISffuvVvncfP2ohHs75mrl_3Ygin5xUitiuvSAkxrfXOBBFRiXx0Hgn-z6XubMsnG7OsFG-uT7qaDvoXNydP2UUplAGBOZPSGmynKKJ2y1Tf5TSdZL4iyRjj9kSC-Bn1Jkh0rE0-L8nXZFGjnjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-8xRJclFWl-wKv_7MUchXEDpik8TOkcL2zlbzGibPyDrS-JbldX_9u7S_SLMdtefLcPjQG48ItihYcUB1ravfAlQjWIFIYRCO397KQh6Tc0qn2bGAOuPC-gHYTOL8UvRXpDH2jzTZ8Y89s8J2CJJmTP8giUWiYGCBybnmJTYae9UCKU8KG-UdFFdXi3yOv2sEzXnHtKQ7EWUC2T6NPtHZeD3Gsa2PpeXW6FPcS5nDZR7MXiqeknJuiB3IT7ioX7x4IUvsk7gaoxhAbftuflwGMpf3HVbCuCep4CRjJxYi7VjkgXOosOE_-UhPGqlH-ETYZhypXN1vxiu1ALqD6ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBaNRoi_aSkdk4kGTcX926Di2RRhftfU-u7nqXxhnHiaiomMAE4JMwPxUhWJz79l_-A7eFRBwFZrXSeiFhHTiqqff_C0rnQEk9dVHZfCYt-f29FtZkHBNTOl2yigl1fuwhdUB5xGvoa-ZLWGe4D-CfSaNkON_fPz7Dmo4KwULAvVgAbTqD96Pnx2QCShcWkt4s7EPvXJ8GHr8i723KYoAA19FZ7w7UNSn5UliTB_gZ4Ay75Efwrq-bvY0fGt4sRce9vqWcIcGs1m4BJazP1d4o62ra4nQpzOfM_S401cZ4hNVFkfF4OJi4V1SKx-nbrfWG7-QnzfRiRzYwz6KTbQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGDCrG6AljhxbCh_HMfoOeoaBouU7lhGIv8fAYk0u2dSyAHTdg3mr4guK45vnceEwKNBoI6p5i80muubGb_JnMRx2hRxk1yQaQA51sbSZZ3F9DCyX-lIHg3oUpjOlW1KpEEh0KUsj7OJCj5P_FBpUuzgILFGgyV416nCKrOIPlnQJiwE2Psi42vSRgWikh6EAYJSN6gINgwHKESoo6saIkVgf0F179lmF7vDlVF9lLzWu2o4hSiLFSYfV_5d3xKHKBa-R8PfNzEJzV-aHHxn25LcR8tqrdIkUN3fBWtDuh6dTeVkaspc4x7Wwhx-REpMEmstjZXyVcjUIpP4wFi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRAmecfDKlXPuYVlDIoU8MbdFLenMJyOr5AK1FQtCDHFtD9JxhSFOCUV71rsCbmQhQv25xv0z_X3odP7qmrG6LAa-bUEQe4-SBNlmI3ZxCbl7F29trIhyPNb5QHzYx-Cg0rKFseBJGh5W_pd13EQ0Olyboarj2tU5GB2Qkd_I4TCrb64ydmK8pJiStfgB8bbt-aLeOcJ3fKoXmSZZqME77lBx8b1urqv-SJwFCFxjwckIYj0Bf0rkeAzr4gmIvcqr3ebRYS1TUqfcNXDTD9wd0R51TGAH4oUgBDz3fzaEkx6K6evGnBi5J9bT8MXBPETibLCsMQA0XRbyp16i5zuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfa8C4ekVwGpgRLbqoE2z9XuNwn9hai3QNwSlzugT5E7lLb6BTWBHdlvDLq2iU7t-xoWmUg7trV2sNs5P239Q4b5l98aEPi1wq9hTGK2ADOpGa1KaKhcu5zF2ahvQgy7-uPu8Mfzva_see99eBQ48OvnoHYdaqIEber9gJRezP93Ag-lH9z8wJd04UqAA9bZXdBOJdCl6Dam_WS4rl0bNrkLjBAQQUCA2EtVrj5GMrlCKWjH1_-R13Y0E9fIhCtTC0EnfyoFXM-ZsUeQLvZAKs_xNnC0DU8YlNv2LHaSeSK7Yoo5UVv148XZF1ClzFb0uMmLna1cOjRsUE4ANuMaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6eQHWHApF68Roh7AkoHgplyBJYIWaqGSonTjik--AjJD9wigrs_cvRqZsiRbUc7VS4jlx_iDaPikkZ_GSfxEWia9V5OXmK6S1qRGOBV03-K-jYVRCUfDNh_JlujjZ0m2Tg5NVHDTOu3KpG-_ZACwyFFb2DCrOaN1qIk9CZmaYD67_UoXk2ewfA1TCzYZI_6jd15BIyBpDc6q-wlGLnUSPSmkhk6-oEWGH5Tw67tU2xlYrOrpL5qgVaJCpQ1p5p2w1pZ0QgunzPADjBOnxdC8tqRAESN2dwuEOASzYxAg3C_Gwvo069pqwTFbUeklNkDJH7j1dN_6JOO9_nS-_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfPLzcoTbVk2O5Lvep4sRpeLRKmFh2mf_ie-CiPq25W-CmwLtv_aBw0WiXQXIpYMTHglTXalUGg4v-U4lxNXXWRtETo6_lOEa8WSkfJIKZExm43p96MfVMrKY4t-G_yrvy3gmcxbbDWEtLyRVKN72QlADLyAxn8L8RoW1JVWuQdOJF88cyvo2-HEiR5BW0A-o2Z1-qYjsEMGDDScr-ivIXbwqUWf8A7L227-o_4KgHQxVLiVl5AhxljWhMTblxI_Baj99V58gQf_Nu5lWYYdpn50cnuytE1wPl7K8aklvBBUBUvWjcZdkY20uzQ-0j0GoZwESJkW_gjwBwkmR8BBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIJnh1lGly2nQMFfaOoZkqCOG5OSLVmK5pgp8hvUr72ji4jO8RVS7wnnnHaAt5LQZ_FgcPja1FIlj24a8TW3u38hD6j6DarR9TFXOGypoGKFI1rWFuc4sDrG9HZKwmRhmAN_S2P5CsnnPVjA1mfyy1mo55084LY1uv4G3gDuswXTdzJTOs4kdhyz1kMakGSLi4RpayGHxcuBnSQdEJ0KTV7hra3ASZxcVK1jl378GNfgK_fJejOjFm16z_Jc5mAcARv9Bj8E67eTrK80bMNNLWMKAAiXp-Pu_1T4F6wlLUIACiJyXX6Xu4CTBuY8TNtwNT7izz0KHrsqidnRj6xYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haYJuQGzFUGCjn-7v8tSzDv4ah6EOn_xGs7iCaot8Kgm8oXyn27s3vYKmCC_WICDgJko_dt0KY9Rb8wl1J3gLCUpbHR-X_UJUYS7GcR3TTKQwMhMbSIeGDxiumm0Qp-kEFB5_bJSg8hhJsH_frQ3zwwC_HnEDWAinqYt0kYZVc9RMiptrR8RHHMfLxCahhDU8UcYRz-DGHZCgKW-5DR2D4cG2fddLDa-9Io_45L1V6K3Mv8yedS60Qlqi7AV20cWfTCe2C-J0W0jAdg4GJ0MzxNpTL2KW1LT9AFvlGsU96Bgukvs_QH_KumynI13SisHTBYaU4b_nVcXyTxpBj3QJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mcx-SrEfdcONkub2sZRI0vhuH57_oiHI4wV6JXi8qxKU66HjYjU2wKx2JLZCEh-9CWbyASUxWlPFcX7uj5RZucObs6BAQfd1Vd0BUicj0bZmAzt_HM_ETdiBzKCcdD7LM1jlJjc2lI1NSgW1bw3g1bmIPg7zOILf0IeubxQL6k_eKq1syf8w18a_RbesD-927aZrIY8glQs7N4ONki3kcDh-1M6QrLv7Vl1GLruh7NzXYxolZjSKQ6XFK0Pzmcaostr5qu1gU9HrPIsfejmrIwc7mTfiMIFoAH7PHXV5Miuhu1XvPMw2erBokH68zihwE3OAp5QbeAvFbAS-xfcsxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxFdImJ6BHSvbMqfEMuhtepnbHYRR9aYsA-sx1sWYOTOwuP0o8jWk9RMfk8zMaPnRm3KgCVy97oXZ2QJXcl30NVcSYClHCoLg_nAmTS7R-iPPMbhsmZtFqA-jpPzprmI94-Z2dbI9LTB1kDTTBCBzOaR8KAo8ZsqUTvXFNUbnV08t3qzL5ZZSYJ8O2aV5REkIYMD4-urnnKeDFJ7D8pVm3BEFHrts6Y_6CcERTa7_nwkHkLPkXM4X6NY0VGdXgaPchBWFywzYamQlX9ma9m68BvSurh2n19dgL89jnJFAqWuePyO0YV90agpm5fmsA582qsB86fD-4dkYEsBeiKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaqzuBCRk3rm51hC_ZkvZpYbrZvbQtSrCiI5K7phSvpKOKzgiBOPNdr2vnkP1BVeVo2ZhlLEg5jq877HRMVM6DVQO5IPzZMx9N9AoclI6pj5OlQlkMNTN8a3-x5cxkRF9iAn8yGUEWv0kIJFBDj7vTFjsZc6w4do_2u9Xj8S1Xk1_ArQd-vxe2FA0pay6FUIzB5OWkFagAPc8d8MmuABgfcHvmK-XKZjWwx_3E2gFf_qixenuRhqN7UgsAP3xyGDh8p5O16mt-9cVtQyKsjSt5-0gASqKWGvy1WLIGKT11Q5fW1UEhsFJ4niCOvJS0RNQcQ6aOYDnR-3StaoBPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV8tnVDWoHBR9qW8VAENrC08hNM1RVcRripU6rpb7mVZ9GBNjADX1fR8un11hKi9-nC-4z3To3CYhEQjLbl_1a6TbC8cot8ah-B1O1F5YjJvlosJ-MTU0CtwKNPDSBuZUlcDn6HWvEtLj6HJCLcXJntcVkUzwZrr03qzJf0PeaI-7LfKEbR53Gc0PahKwPNWF74rA73mQKVErUfucUlkZubp36gHgAeOzMM7tbpUKal1I5B4nfnTv5f-CeP1tUzxYbp_6_kFSZFD1P3NXlBxtb1QrSiYjM17L8JVDECO6rFsDH3T0XqC4X6pt0EIb6ulX-qPz0WW_XxAlqBWTMeslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqA5-_1a2UUXEAqsbUKLdSDLOkvyiseDzqk_dXW6XA4eTfauHKVIY5Hqp5wEVqnvi9fT_9n3eu_Ail_d_rNKkLDGXCoPUPFawODGLWKaJZ1b9mIwul34Si3jDmGqPTJjLtHm7i6JZRhT86wQFCOeIY_WIS694v0nGf7CGpoBQXJnR4uZkNAoyJEYtGnT1RtCTS3VEE6HEQz2IMTC8PBF-fHcYOlA7BnzSXjt5Nr4nkrZDvgeBvL8w19dBz_zFQCcgl7lYUbX5nZ5hhEsgeSw3zmJHwx7616Fi_oKhjKYu7KgnJyGF-UslDCJXMH8yHh2Ar7rk7hhHLnpq7V6svh3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26226" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgGRecqPvkEfSA2uARHdVgQCy3Zu6tTVom70i6jrON1DoOtChpxS4tJCC0V5v9KsoiexePBFsXAaK7_yhy0QuLjPpOUdGr2llPUWu3ic-OsvEW9e3mNUMJliYqC9Ac0pM4_mqdsPOC7xXpGqms3oWbENquwz9syStdoom1k7sl9cGJgre105TRG5UcQ1-pprMZrasfnOhN5FW8o9oJ9B-4Er4UvNji2y6_FCEtjFF8FwO2se3M0Iyf5Y0pmQRSWuGI8FYAVaNqbevAfQj8p0r1fe8KkjYxy940wiVrkq9z27NWH-zzHEpfrVfFz2D7iclqpblkUtsHwRSKXo-Csceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afv1KEPeobz2-6_LwYbXHnUuB6kdjz4rGKzqOOUICG6VaTy6B0xXHA8stYDzqOfbFUyp9g5s5rZ3FKURJVTpKWZL6sWyDgveZvP9wL8nyoYbUG4FjCHrCunkC_Yvep-1jJj8Owpqo7SbfkWSZqonnHBf80SEq39aZlQWveNJWCSmAGE121y80irkWcMYkaFh3_qLEVnh1D4zjyNPLPPoNOuFXRMdmE9oWZAiqDf7euRSBH9MzLwUX01WgwcIbLDcf6mSK_OCdvbN-Zrhv-esKpu0ZR7mOSD4DoQjAAzF0wBZL51znoRfcebITH50g0Hj0jM0aknJYgkj_DliO5AboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEH1oAVtARzS5gez9pVVM5qkk7NB670GOryxtG_Nii5bFfkpk4S4_HEcXEg9VsKN0T6DNXZuJgrcc6ErZR2Pw8BiGcqU40M5tyBMmV_mYEvJ_6PeZ0OwKDNBBonytDCUgRHKy8y2U-d9ByocAKlOlC_cdapH79mg5OhS1ybMVGLY-UspGTgyppzkTiq82iuuE7F8fvcgLuNhva85atypNJ7COVDZ4zchf2YmJM_IQCHg_-tBZX-rzv4_LO7zE8Te-ujG2ifrSl55mcyQWXaKaRSujZkCRC-N4NDL4LIdXCJKZym43wZ2I1NYbyoudfKtfE9cTNWvzXOBv7-f8DE1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HndLgVCLy5P_TjJAHm4xxjZaGF1D_Cn1RpjQWQ0gAOzs-lAJu0LYIukvWbRJwnJy4lx3LQM6Rn5Igx0KL3wzkh0D9qBuiAVDcgFnVRjuWBjdleT4rQWl06F5LAL0ZLfNvXr5svfPkBdMmv9jPEC4sQV6jX1WM_u0od2rFNetATE6BzzuX05xqI3z9zSUFzfRIf9t7kxandAiduL_vwHz6OrTasmRgQ4KQXkJu3IAMOdqAZJHJfhtoyGETG2F_36XxoDhac_uE4hDyGzO-u_glPcwqiW71WC4aJgbjU0mq2kIeMOpYZKCEA3ZqsJQEOWtUC7sU97IqU1geL3iEJvKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6BweCzy2wVidYsAX-6EjPw57xGQ-j7Qn0jTQA8GIJ8QOWkVuDKBxQcN5rarok3lF-M2nxjb9mSw_43WrtIc-C265RccHzeVdGqZ4SX7TV66ZWHCJ2HnAcO5Do2RzEtfaEHvjd2ICf0TyvADAU6SraNTau8u1e43h80btXywegQK0GwpizxwuP1hRgLsJJzHtlWHagN09Ux7u_jGN0FFJkygFNB92OlTmQGZPY5-7JYmps73kM6IFukTSSBPIGRWtB9o2WATt00giws-hHinJZpETOdzb0iVSpFxBTlprg-51bTTIgX77jyG1Bu6ijXQ8D4A7OdPL2msfcRl_QKHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmpKLhRCH-49FlAgbyfcMTAE15LgubTPEX7qQZUOIBuLTO6yInG687WWeZlteiKiSXy3JruLHnx42HyJQUmuXNRIbzorH3_3Tx_TI1k8gd6ZWY6RnvA-MS5AIVyUFiN4e2l9-Z8VFppN6aPvi37U5LWRzwGdLnp7QC-k2OuAGWjvrBpS4GJyCiFiXeO_KkOuxKs8bTcWpHiucDHWAEIOSeqgJRTZd0OUcYTM0kd1VVcFLj1mW3e1iQxj6_VH4Gke7B3o7glihr43UEWv-t1SlD_A0UZ6ev2SY6WE0TYxLEaSjxd6aEnJAHlNrTdkrFfMOVLYv3A1TjH27uMaU6wGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYgDuWf4OusW5KzWZ0QBFSwiIU9Rx6BL9x3gYiBReF9Xzb3s0Xy8ybQVOqPrCWXpO7ccvlKPwOlpSd5X4JTNis9vWYjQ_h9cPQdAL4Gg5ltkOI3yZEZXTcvwIS9kbPgT9aDKXpX_JQEatxSTLDs6jcF0jaLg-BkDxO_pvQVKMEGVxi3QvH-yY5FPRUlrWxQ5M1xjOsjmHTKsl_SUDCq8h36SLtQ2RwWQ9q7R-ou-qGJhXFPwqm8aXtXZy2_EmF3og-o6P5TIdQ4oK3UxJ_QLNcevLuUhNMe3DuL6o3IYf-JgU6MR7rdAAYLVWNdbOGOpZQqd6Z24r-muNxp1v0uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKRG2yJTReAMzd5d_PO9ARlBPuWpWIweqNGbYUroHIspg7tZtdiBpyv_NZNjSzErrYi21Kr-X47snGCA_PRMzD_PhuCdeJC5bwChePBVjQENgDpVaFOTyyFBlPtPkBr0G5plEN2T2_9LTbBocds5SDoLDMz3gFNCJqYxja-GNfPO5sRQObx8_5kqpLmiPbkgXPSQj3lE8OiTLxkpx9sLzLO72SK18jMzWKNQx4FglJ_i38Gun4zF2utNH2UDU-y9or6E_HBRA4bKLjiOozG_qimVlChMFw2XLMcQTFVCC55aQBYM2864zp56TIHArFqgd3uV4s3qQHJMV95VzDCb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbrkH1VgTZrO_Xa-cWJKXzkuMklCGp1LadUg0L90R7MeWZLx4B8OpkKTmU6jO7aJEVCTpdgp5o2BXwE5_XkHdiIwEkCa5_e2aNhV79KagmVwXXi-Mgqm0r2XzAFowjOLgqT0cvtYi68Mhr113jGU8S3THwmlSS7Tf2VzLKUdHZinuaAS2369Fx0MBWuEXDcqBOCX3KPLAb2F_KNdltt7umozBJURC76xxZVX7Q1xVJuR7V0EiYyn5RgC4-Sfswfrm8pingL2mVFMt80nrX44IlBVrPYWG33PLTBdjd4ZBlljEJ0hZiX3Wa72F0yo1UWAuTi-4AbtiVgnhw83mgoGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxvKLDD9aAe2lB9Z7NwHpEO8jgHzd_OvJ03hPN1oSSlYF0buYCnxTwq7DffZjmb5iCEtibYKppnbGDEkqaWqDqhT_m5yKwh_UexqcjzmC5Wql7mxEOoeCKC0pS0tIXnOtQ74MfaEB02IWFUaQtaQ25DCH4W6MPj3Q148O6EHm5sCBU3c9Q_ApsUeAQlWOluRHGgk5kx-posu1R7fJr9QW-XA4vi4WX1bHUaSrewlIK_m_LdG1k1vCtnfrNAY64Va5KaEMAn6YUgzcY22M1_CYaC58ShEbkrQ3vYk7V7LBOGd9SwuHvnWZDWtANmP3Z-G9_6PFxD6Bi8Zt-j4YlD6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK4XaPcssBHJxLLMAwEXebTcJovJ_9u1IsZRiQg6d6bDSBjubMED8nPejG4U9wHCxhlbjzvEOQ5uPznrCyJTIQpnFayHxUirK24ax3JQAWEbaqtV8pzFu_oLaUHd0YvBYQXVczR0gEYZx04HnoU3B_V17vnYgY45xgB1neyH-HBVkXeUKaNFx6u-y5mio67TMQiSFHM9boVKAvMCKYT6U_NZeBWmi0W1vN17od71NqgJtbt6Z7_aqKGvX8KkyW2brODavgEn2LlU2M8OLO2TWZ_0I9gvtcCl3nGENCl3UIlBCXi0uoLQoEfP4JzezFe3yKvEQM1Lrbty3Gm8DCNaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbt4EjcwQXbSBsqmaT8AMp7rt5gXGp8rwHkBwfocWziVcJmOMvztdPPdyo5fs1D9pv-L7Qu7AFSQLQsGXKu_JUEf8N6OFu6bJpxYr0Tt6WkZP9R0W76Pryo2jrqpd_1X_ZIGKC2OTshboW6hOVSlyLr7Vh2oxxaTekM4mTbuFtX19aPS1VYb4SbAmH2tfArYwWe624wHgFmM6Q8OeoE1sOFHK39TrPZ1cF3N1e92Vy8fa2NyTW09BkFXyGrTnOMUPollMAUeiIzJQL04eODqzN5z4GKjZ0EH_7qMH2NwHLcVm6Ypjd_hhs_D301uE7S2qk0chlOu0JqbqMmx76MTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl5yqhi1fzcBtDenEGCMkzWPSsR0EZa2vFUNx8HwvarLP8dUohFy0czcBFXXz6tCpVqFHmR_4V0mq-Ja9vF2QcXzM_hBNjVBMQIRDWveIOCnpPA_8IuPhP2Cpjc1wYBEO8BKht0hvbgkpoAleOJMi0rJQ5ADNrZQgqftUQRR2dZKy1ZWd3fzHrZxmu69WGzSVbuvlLIxq5IxAfJJgBGFWcg44TxeXFfWd9_IyOTghAxpEko0XVbXPM7PbGqokrv7W8drM9wc3n8ZhbvlGCea7CO3yuMMUM3fdzIWiuh3sFK856gWjiEUoPpOztgwOWw4nx5C2LRnHb621U5OEznjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSl5fW67J3sgzFsIcZz7SqqNbBP2M7OvfQ-0iaODasNstv_wgc3Ia-DvxO98Sdm4ZbMizoZi2nzjV9fc41jFeNo1991OLa6LgOpSyK7miJLf0wQUJkYPmfAoIf-OM2y57kev4lleEc2lcjAXxCTwo8Bkm5CjwE67PCZlmsMjFQbOBquMyPCL3bhvf1qHpPi_26qJODvMuZC7LkUmM51I-NYRrpkQEcTwkd7iPGTZTC1WGAI14oi5tLn_kJzyAX9ux-9-E6F8PyRrIG9SjaqkSWV0eiesoEMwBSe1qkx4jcwkz3h-3CPF5-YqNRGY7QI1MKpBIzQ1OHfIGbqo8lWDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRB5tuY4D-y0_vc4lsMsJL-2LeAlpoKyoRnADLP3yRsnX4gH0aFJ_hxqULHYoiWOo8a7QUnrDalg0WFpSSNCx9ldofuXA16uc0N2PSzVg5aX8iF5zjoF7wn6EkI1eyikeq-7rnxukPrMLFhG_HN7rqEYlUc7skENY-8B-Goy8Oz_5TLoHEUhVQ4GdAqRUVZvj_qx1FPDQ1mpdTIKjEqblpNSggdeOm5tZRoTAYqfm5Iw4ESihco2x1cYD4vo7zdRo9yojU527aqHLw7Bwfqv7kML5WyqEj0qHhW1NZSeZLL2rO4i33PreYHTrz82wQOSUaF2E_SJBwKeXiRt5KYQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=WvbHR10bdMoF2wFOzJrtgoCdCW5T0pWS2shGvPg0p6vQQ_9y82SqAvgiv88DQvVoRK4ACzhnJILNhFJFcAy3XbuoMiPlbH7BO0knqorRtXHYR74xiRy1sOfJbLmt30ZE11U9WgZqdCF32SwBxBh7DFVSTuTBCzmzZm81hvrF91Cmig27efDjnkz1UeWnFBkh0a63v0YjfAo_vgm-IcGCvrP7mLzayC2zibWrlwn0UKOgVgARojHa4S_Z2E87vL8b9-Q-cnig_fpFY_l6X4xdiiIseqsFmgtUeGEYtqGxOupGn6Hymtu7JGpjitozO7DNEOGH9umoU5emGh7Yrf14Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=WvbHR10bdMoF2wFOzJrtgoCdCW5T0pWS2shGvPg0p6vQQ_9y82SqAvgiv88DQvVoRK4ACzhnJILNhFJFcAy3XbuoMiPlbH7BO0knqorRtXHYR74xiRy1sOfJbLmt30ZE11U9WgZqdCF32SwBxBh7DFVSTuTBCzmzZm81hvrF91Cmig27efDjnkz1UeWnFBkh0a63v0YjfAo_vgm-IcGCvrP7mLzayC2zibWrlwn0UKOgVgARojHa4S_Z2E87vL8b9-Q-cnig_fpFY_l6X4xdiiIseqsFmgtUeGEYtqGxOupGn6Hymtu7JGpjitozO7DNEOGH9umoU5emGh7Yrf14Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHNmVmO2yz6VRZkV9NTsu5mZAGg08Bp5QNYhif7J9g0dl_YI-Bt1U66DwxEOA2BR6dv-Ol73PPpW9FwiTbU_Lu7K9v1A0auXgajxLpkr4TTMAHDZ_wllQ2L1vk34s1eZcLunLTPH1J7tMGB1_370Y2ZLutT-FB-jpA4lLLopJ7CiZW1WYeVzpo56HnmOuwMgVR7WrsJsmGUWXq9_LC1ZLCusSoANDZCyn9h3HkC5wucUaLz732fjSf7puvx01UYQZl95_uVSo76YS_Ks0jNShQOT3dAfyA7cwxm7D47gHnJqSa0TcrHBkymLrai9Q9HGqQANMlp4y4QISrsPk0_lXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkQIjHOzL3b2f0JsEvn-2HYbQG5pM9XJV_U4x5CeYg7K3GjHdg6Nj2TLehyg9h1wqaqhSCQyfbIhmdN15TCtuXi6coIUW1DEnN7CHwrYldAMTvIr-2lzksk7dHT9Br89cjh9X47s0t93g8468wiSJNaxccmmzomMEhCUvk_2CR3iD0Gmbms1oMdzX1dTOV0xqcAIxjZdvY81U0MPGlw9Ye70TYgL_fWUlV0HwUSLZxPiIjzEhVrlT7Io97hV84caig9sAVN4wZw-TO7CATkbzRbyMEzWvWj5Qk3--_xucecIOPdQ-taToXLK239U0RsFj8kqhwIUFTiuOrva419izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8agrE6PkVcPPnzjG69wvwO412UWrzbrpX3G_-bgL8jhsREpnGQAoQwf2GOwXVen334lsoARH8TmtoqfpaZgnIIoh4WdO-xWyHENJ873nau_KUPpoIL2W7t9yfG8Mr9zJYzX6jM7YBp3H2Qs06DZqOMGY_PhNYBiDFxfIUywieJP_PZon6tONtlTHHELwlOtTdIzJiDDcN7m_TayoDGs5x36u7pa_n1uCTtvcxQbzc5NnxPWOGJCeck62IyT7QyqxuHbETEkaR6aZxHSVvdhmuI6nI5hpNDdPVJP0TnKPnTF6hCEfYGe5DeR7rcRwQAq9t5Pv_Uu-plYQIj0EOYP6Nwkuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8agrE6PkVcPPnzjG69wvwO412UWrzbrpX3G_-bgL8jhsREpnGQAoQwf2GOwXVen334lsoARH8TmtoqfpaZgnIIoh4WdO-xWyHENJ873nau_KUPpoIL2W7t9yfG8Mr9zJYzX6jM7YBp3H2Qs06DZqOMGY_PhNYBiDFxfIUywieJP_PZon6tONtlTHHELwlOtTdIzJiDDcN7m_TayoDGs5x36u7pa_n1uCTtvcxQbzc5NnxPWOGJCeck62IyT7QyqxuHbETEkaR6aZxHSVvdhmuI6nI5hpNDdPVJP0TnKPnTF6hCEfYGe5DeR7rcRwQAq9t5Pv_Uu-plYQIj0EOYP6Nwkuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=UUG4AzwlbTvSoyIClVZl7anqzS7dW4loDvG-canDxNiIanL7HgQnHh4-z2NwjBM4NkgsLinYoXQ7ujq59fKJGaCHKHpEv-DyxiYa2Q7T1LwQpqS49NstlorjmFLJyDLaYuzxeXocwuH4je9leRc3nYZqgaUVp0vdPiGSgDFnUxzzL5VoKPnuZgz_JWGwchp0Nx1HG84Xk80LcHeAHfjTrJxbd6tpmiETnM3uefSY43az5_f6H9BHJjVNpuJSf08ZsU73wAOgSGFL2gPv-ItIHHSgJy6ZGsyLhrHBQpWCGO4223Ia9lSvt67O7PKJUL47oL1YyXTPn7sSfKVkUzjO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=UUG4AzwlbTvSoyIClVZl7anqzS7dW4loDvG-canDxNiIanL7HgQnHh4-z2NwjBM4NkgsLinYoXQ7ujq59fKJGaCHKHpEv-DyxiYa2Q7T1LwQpqS49NstlorjmFLJyDLaYuzxeXocwuH4je9leRc3nYZqgaUVp0vdPiGSgDFnUxzzL5VoKPnuZgz_JWGwchp0Nx1HG84Xk80LcHeAHfjTrJxbd6tpmiETnM3uefSY43az5_f6H9BHJjVNpuJSf08ZsU73wAOgSGFL2gPv-ItIHHSgJy6ZGsyLhrHBQpWCGO4223Ia9lSvt67O7PKJUL47oL1YyXTPn7sSfKVkUzjO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=vR-9P2LRErQTgns3ktxtiAPfp-Jg-WgOfGcpwshwzXqd3IdCgIs0DQxGTRO5QiUYKrSlQ8nKIp3OB0w08LNO3TBsZSPcQumDZOtZj4e0HiF9eSLZWHVo1C3XNVSBBWdlYBb6elZimB2b6zDPcLXOVnbaxoMH9KiVU2szPO-66ED6r1AOHHvfFTOqmyQVTrSEyN1vFsz7Aqcck09B3gzNLozT0am1_8XHJumhKsliZoMCATmSEKJTbrbekGdq0B9nvmEx9MGuskXKZ-0Km8XkrdZBmpBsvu4qiYqHppGU9000h7GlCrJpMcC4zStAr4EABGgS187JrkluHg4AAI8Ewg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=vR-9P2LRErQTgns3ktxtiAPfp-Jg-WgOfGcpwshwzXqd3IdCgIs0DQxGTRO5QiUYKrSlQ8nKIp3OB0w08LNO3TBsZSPcQumDZOtZj4e0HiF9eSLZWHVo1C3XNVSBBWdlYBb6elZimB2b6zDPcLXOVnbaxoMH9KiVU2szPO-66ED6r1AOHHvfFTOqmyQVTrSEyN1vFsz7Aqcck09B3gzNLozT0am1_8XHJumhKsliZoMCATmSEKJTbrbekGdq0B9nvmEx9MGuskXKZ-0Km8XkrdZBmpBsvu4qiYqHppGU9000h7GlCrJpMcC4zStAr4EABGgS187JrkluHg4AAI8Ewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJh2OCii5oaHocuYinfZ3UNHv0cOYXRoIDsn3DAQjx76xdwVhyMfOuciLnYNrTRcjRk-N5rzRZz77UO5cm_9Pudii_vHJ8Run_vyuGNoAKIWQmLDDUwsuiGVqFW6N412iR49t7Bc0CAZYXCDk2gPGYRZ_cKYm_JPSK1KnB6CrYnaKlUxD09TrL7Kl-xRyXir5iFX1TS7lzf_rOPtPs4TSF8TFoIIHowmB26MZuczpuZAeCzAzLU6QiobBv0B6oOS1JPfQuysoYikP-THHLg_6jofOu55CKQrEy2VXVtJxyqdkz2S8Ho0W12H7Oz3P6jwhOrbn7IQOFdQR09VP1JnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5ymtbkah9Lo2l5T6O-1DWOXZELtkIOF8XRsS02m-BpPTR0qDvCocEa18NadY34gMEJDz_OgEtxpvkKJwYfdOhQ_kZGhlR6X0OQaWHjM0mlog3fFvxsh_c2uK6I80nDa-5aHOmQ4jr7ZpNA97Wk4uTgwmM3KKgjFYEju43P2SyxF2xKrRwY4MIKlSQ655flxYRe8AK2AtP3o-GI5P6QkYXGTjKo5miYI0Y7qyDOyY4Ou4tj9wOHkuR2ZV1oKeuZo1g_D5XLdduma4D5nKVE-CsvhgLqpGssnVUuS9xqNt-t19Ahp_1wgN9sb3Z8znP-ki7EpwzqQAAcPL4uvx93O_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=RQ-DLdpgRDR2iccRQRFBiE4gKExUva7cxyb0uSgImrgYe07YIgquSFdDOAYK3UYZedEZ2pr85EEJhiW631lc1_ycF3tMbG1TdE6Dn0oxUmDCL5IMH9AeoSk6oQhwmUzyd71_mIU9PRD0GwMgo2G7AXS-3_rCDnRLOa-dbIrdD5IIhJGK9oe9E0Ed0TGZGjPX0UUdw5q__8U9Ioh54mY-9DkjGc-XffOYnYGkZExIQ-huYVNe-ei_PXXPaT1gKK57lunUtgmkn4_lSxSPmqKZbHWd_GJiEuRku3zc9sc5oSt3qCBW8BUNbVuF8dg-D9xddik4ECNrCP7kFJk_vA7LHUYhVJlUtLPGINs4x7bgH5O-Bq0r2gHfoVI0Dt8kbVcc-4mbp7rVarC95ico12hPt6x7aLEE0W_SzPfFpUU5bUhsqpLxpGv_bkKAwc9sUHK-1iXamYcwyyiyD6Nl45guu-t779LpTE5tcm6nkoH08cvicrY4gZe6A50taXZ5ICZ7H2HIdPC8mO2w73K30PvApcnQh0viy1s-NE2kqQGCOnPWHIyAGCzN7BmAQTTv0qLF2ECtD8He8fGsvKdYrI8msW_K9JKOoUpq-mgiGRlOYj1hSwKY3netjqdYVHX7eVbvQoPnxqp0RP3WNu5pSQ5Fv2yA0WfVFJ9lLIk0D851seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=RQ-DLdpgRDR2iccRQRFBiE4gKExUva7cxyb0uSgImrgYe07YIgquSFdDOAYK3UYZedEZ2pr85EEJhiW631lc1_ycF3tMbG1TdE6Dn0oxUmDCL5IMH9AeoSk6oQhwmUzyd71_mIU9PRD0GwMgo2G7AXS-3_rCDnRLOa-dbIrdD5IIhJGK9oe9E0Ed0TGZGjPX0UUdw5q__8U9Ioh54mY-9DkjGc-XffOYnYGkZExIQ-huYVNe-ei_PXXPaT1gKK57lunUtgmkn4_lSxSPmqKZbHWd_GJiEuRku3zc9sc5oSt3qCBW8BUNbVuF8dg-D9xddik4ECNrCP7kFJk_vA7LHUYhVJlUtLPGINs4x7bgH5O-Bq0r2gHfoVI0Dt8kbVcc-4mbp7rVarC95ico12hPt6x7aLEE0W_SzPfFpUU5bUhsqpLxpGv_bkKAwc9sUHK-1iXamYcwyyiyD6Nl45guu-t779LpTE5tcm6nkoH08cvicrY4gZe6A50taXZ5ICZ7H2HIdPC8mO2w73K30PvApcnQh0viy1s-NE2kqQGCOnPWHIyAGCzN7BmAQTTv0qLF2ECtD8He8fGsvKdYrI8msW_K9JKOoUpq-mgiGRlOYj1hSwKY3netjqdYVHX7eVbvQoPnxqp0RP3WNu5pSQ5Fv2yA0WfVFJ9lLIk0D851seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGF1XITAF9vGin8Fy6GkYU6LVqf0fpmd9ZcXussr3BRpTO9vLDml9P1H6qTVbxp8bhaoBMwg7aZYBy97XQxF91FAO7uncb3ToPty-Brplhdm-zNlGQyAN4GAr8-sT7J0PbFL_juvD4mzbAe18VvGNqyWZ0FX9nsnKss24M8df60mmjbN3GHLUum19eTntLvfR_nLyAnP8I_T9jWOB1q0bC76UmKXvacx-eW1KpxrWU0Ilki1_ZFFBgoH1a60tTGKysNzTHjiVNl9L08lww5w1kcQyOG2WxxZxQxs8JrPOlHvUC_Ax30Q8ahzs1I_mImS0zPVvTngtcOz6K5Q2BirpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=rh5makv4ra1NiXjeAs0s4MnuSRsapK8-iU2n2zmYwPUJjimo8N3W77gRVk6BD-INwARSNNKfaWjnDTPc8hMaHCgxu-d81QcjZSTG6jSRi0lE13Uvoyb118GxTk3oDBViMawHCi5ar5ptsvCOgiKLDBguSEFsOrOcHJb2tokpbC7pKqF5bKUTLOR14fBbgNtYF_ksnqET64sfBYj10xCYpVa6ylYIMMcHDvwrOYjNeEo3np8x0nvZhSqLXN1cGw46ogKduDRrmzilm9FhdIzBz7cz2rTTJ8BDwKvbaCjfO8sk53RsP6Y8akg9cX5_ThI-r2xrOLBj_joFdDVQeheBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=rh5makv4ra1NiXjeAs0s4MnuSRsapK8-iU2n2zmYwPUJjimo8N3W77gRVk6BD-INwARSNNKfaWjnDTPc8hMaHCgxu-d81QcjZSTG6jSRi0lE13Uvoyb118GxTk3oDBViMawHCi5ar5ptsvCOgiKLDBguSEFsOrOcHJb2tokpbC7pKqF5bKUTLOR14fBbgNtYF_ksnqET64sfBYj10xCYpVa6ylYIMMcHDvwrOYjNeEo3np8x0nvZhSqLXN1cGw46ogKduDRrmzilm9FhdIzBz7cz2rTTJ8BDwKvbaCjfO8sk53RsP6Y8akg9cX5_ThI-r2xrOLBj_joFdDVQeheBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=QsY7VDhC-0xKdrCYa2zcReGpNX9N1PX_Nf44h3xVLF_oHBByhhjRY4y_7KuvQ9SZVKFIsCiJv4tKBCFjbY3isN_phWVyELLj-pTrAN9FgzT0IbZWgmSzgjVtHKCgSTAQDkKGsSt9higwKvhnvQ48FaPXfaIm4MyGTo75sORP_kA0QQt0x9enlc355ld4r8Tt45_YIaJ7WRzNrP6QBHgC3jAGEYDRuJlJdsl-fFXnqmODC34tjLKfg5m-X8x_iy-M3yBaLxd7d9RRds-sODD3Eg_63s2NgvLcN3Mv2tOfLO5fkKR5xNKRCmLbBphqz5erby1HYiIGB96Yq38agY-4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=QsY7VDhC-0xKdrCYa2zcReGpNX9N1PX_Nf44h3xVLF_oHBByhhjRY4y_7KuvQ9SZVKFIsCiJv4tKBCFjbY3isN_phWVyELLj-pTrAN9FgzT0IbZWgmSzgjVtHKCgSTAQDkKGsSt9higwKvhnvQ48FaPXfaIm4MyGTo75sORP_kA0QQt0x9enlc355ld4r8Tt45_YIaJ7WRzNrP6QBHgC3jAGEYDRuJlJdsl-fFXnqmODC34tjLKfg5m-X8x_iy-M3yBaLxd7d9RRds-sODD3Eg_63s2NgvLcN3Mv2tOfLO5fkKR5xNKRCmLbBphqz5erby1HYiIGB96Yq38agY-4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtxiYL5QEB2VdyNj7UaIv6s5xouVkgohwPY0tjUBTOZq-0l4TEei_iH3Uf9xvi02fWih-PaEOdEeZlrHKVbf1voP7NkGwP9lhE4zxoSpMTLy2kxYgdnSdfliXI_Q53whIloZ_TYsVDP21liemB4ElSfya_N2Be7ls5EoAf2Yds-hqbPGqMtAiwDMy4gBahG9GaUd4xotN4P0aETGwqqCrXTw9R1d_aIup6z0sHc0a5jAztIITTZ7LJK9XSUlHp6F4unZ7hqfVvpCPBtNZ0Yvke_Wyaq9VWznr4tF-BFjrTaNYp054PxUeNehuxxFnTKUNkebnSgmTfV6ipMHP68rWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqsAMBSJs4NQYgMT3ZdWhTYwqcwwr3SV-QcuB3CLkJEbowjetG42QO_H3qtoexoNZV7kRayVU64fEdTGU1Jn_12VWBCwdjsrDum-NOoNiSCXXEPGsR-5Hyr-c-57H6FAzk2kbGMQ3hWPbCkW2_L23wZDCXUkc3iU5pk7nSk9uaR2MvdYVsk604wFBrL29fpSa_RYedE-oxJ-G8Q81DdQSwhct5wfOxvyQnQjzxFBCgPRY8AOPrhNj_VHdEOl7pCNqrlYPSV13nXScrF97wjNJbdm4m2emPGkrWGeYtrib8w_JPPMKlqrElJH2XmoaNzVxNiKt6XbKZOFbYgGwV2KUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=twzAspjemL7CWmKc7vunnO2vqmZh2MchnzW6G3M98fKnKEJ8k4MRYhaL0uVyRs-mikFccEg6AGk66qdnaT8fxKyS-dACdAiZSCg6zSvFrDsuvHl4SbBlc6R3T36HpuWQgVksVVtUs8JernWRnIOHR0ONTIJh-zpMlB8BwKJ3seWygwp9f88R9YWTA2Vzf2OM1gGO5vuev2LIE_L8QJbgHOwVv_E30If9FWNO0k5U950pz0QApjdlp7VmI39H0vqi5XXiJv6StW3kldgH63Ff5Aoca1LgMYteht0eFAqSsFqhrdQW2WY2TncWKVvm593gsBBKQa2VpJUS5jUTjh86YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=twzAspjemL7CWmKc7vunnO2vqmZh2MchnzW6G3M98fKnKEJ8k4MRYhaL0uVyRs-mikFccEg6AGk66qdnaT8fxKyS-dACdAiZSCg6zSvFrDsuvHl4SbBlc6R3T36HpuWQgVksVVtUs8JernWRnIOHR0ONTIJh-zpMlB8BwKJ3seWygwp9f88R9YWTA2Vzf2OM1gGO5vuev2LIE_L8QJbgHOwVv_E30If9FWNO0k5U950pz0QApjdlp7VmI39H0vqi5XXiJv6StW3kldgH63Ff5Aoca1LgMYteht0eFAqSsFqhrdQW2WY2TncWKVvm593gsBBKQa2VpJUS5jUTjh86YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=GOl3-aXraE11StuxD2l5FNOPjN2UjjbqsuvL3T7X8WgvJEtUy_M1rhk-of0XMBoE5K5UvwLA12_43wt42b8MyV22_koUOu7wNpE3ZEXZTG4cUZZgJv0EHuenrb775pHARMvcwhHAzNgghRoRgBYUVHhYf06K7nICRQgji4xGGdgpzvq0WyfIT3A2f5rusK7l3e-HwV76xmyG30BrswkYhf3ejSUT8izhtExng3RFkIuyxD-i84wSavdMzEPDhcTCwqb8-2muXBs7grHBbI9K1lxHN-d33Zj4ZF9PgJ9jPCpBEuua4tNydkyUfSrMwZ_hFofAnEtMkK6w6dYK1nhVnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=GOl3-aXraE11StuxD2l5FNOPjN2UjjbqsuvL3T7X8WgvJEtUy_M1rhk-of0XMBoE5K5UvwLA12_43wt42b8MyV22_koUOu7wNpE3ZEXZTG4cUZZgJv0EHuenrb775pHARMvcwhHAzNgghRoRgBYUVHhYf06K7nICRQgji4xGGdgpzvq0WyfIT3A2f5rusK7l3e-HwV76xmyG30BrswkYhf3ejSUT8izhtExng3RFkIuyxD-i84wSavdMzEPDhcTCwqb8-2muXBs7grHBbI9K1lxHN-d33Zj4ZF9PgJ9jPCpBEuua4tNydkyUfSrMwZ_hFofAnEtMkK6w6dYK1nhVnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1AYc-xl065gCCFUVe_UAFhmEGvh9lrOBDG5IMeTaOnjTfLMwzsPN0OLDVMG_B4RW7HBD8INn5ZjQUSSRjUcZuAigy7XzU-lPOxXL_iI8zzwxCpcS1IXhOpSTQMp19SYtGAoBzZZ5Yo-E5LFB5Uyjr4oaIDnsD2i9ktm4G8cD2qjP0Cw97Jxx9nDSZC23diSuKhR9ZkyS5jJ6nHb55ZUtTofppxM2XZoLBhlVTpg37YTRXFctuztLsAo6zSzd5B9avdafwyYiLfYTs1plSAprCjYizp7uFDJsFNbBtUWc9Tk_Zlh6dwaqkcuxLgSZew7R44MQQ1cOjkEwX7JpGCt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcJ-RW2HgA71eQKrAzJGhnCI8o8evhKmTevbVN9_FF4b2mRwKJC7__gQt835sNIirmgK5-Wb4PXS7xYq4r_vKEBD4luoAE8suT0ywbAycWcGp8w1uQ-zC-uwBZqeE_oIjp3iNdqYJfIPAgkBVPuvMeDzKiOUmvmfVmWGe6QEL1ZJyyeJNd5bgUGg_ZsI7Pug3YPTgtPrBRggqNPQCawZ3rqFxu0ko87qpYMUYnaMmvaFEkoCC28LCocsYB2FqOn_G8fZgbtYJgiN5PRJmzJ78OV5aIyxogNEHTY7pI_nZIzh9b0cy6xqgIU6-VLAFvaAsKQJkKc98tt4HB7L2CMjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayyx2Vck8Lz-ia0fLKZcsGGpaBIe5r8U0uSDCmWd4NGzF2ShTC61qQR56JRebG5f6d10pB18xZm4kK-kn4NwquONaAu3PyVXsvYfVqPLJz9cyerUBuG__tE4aS31Zf-_TTUB4Q-BvIyZTXHFh_-yC98_UeHE2yXD8guKFBOMDvc9WwSLSlgpeTd0O51Ke63Dh3v1GYj0j_WSUBZPrMSirfWfvTP-fTQgk9In0JlUo_oq9mKE0hPqsGRMx7upm7k-gJIa-hq2Mctd4ftCZ4H9WwmX06nGnRSqitbgSCQ6RoJFtJFEsiVPGcW1dRnTjRqfL7lV5M3E9YUd6hf7_YPy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXc3gyajjYuDSdO3P-5YdW-5Ex0YuU7694Nr1z9dFzrxjaorUjYEK290E6V59H7GGnkfBFHghLf0CAqPQWxepMWLUdRBgBkMedxinyl8H1-T95DlPpz0QcwDC2P6e1AVsJvbzYB1XQJZIgydbwTK8sprR4XTYMYoQ4vixztBVTOOXMZOrg21_UfLkkqWQQjzZizes6JeynLtjwy6Y9hAsDQ8RL7ejYZpRfyEY1o7gVrhBvqcVrT3rqR1reWf0cyrGj3BWQ7gIbQQjyajPuJbtaVsoQvFK11grIUXHTSsPS0fm8udRsFIM24JptlBXlxWm94EtBUe9k1-XRgIE4hKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=WT9iM1T7BbeeHOHBoUjEdWRlSwdfaq2inp__iMOKvc4mRupJIBaLQZwwAoPDyVNw63yx3wSF1Hfsx42AbAJhzCxktB9PD6urFkIqRs-mVVJIXPKscgYW7dZrFe0bWhYxqPqfmQk1WcGEMoZuv2Q-Rx4B1MkFsOxgkvXtlLXkqigXGqdUgOkFa4nGOKKSpJ-9_JPZd3bVauNLFVUHQHPryZ-mmtqH1iJwE_--r1AuWSSkL0o0mu0IzldCmP1spPegv4_SSLx3l9WJ_b4erPgIHFIGBXKmCw9XVIhScjGREj4fp7g8H-YIQD-Qsrdp5iFatTqRk6gDKpAkuLjTgMbKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=WT9iM1T7BbeeHOHBoUjEdWRlSwdfaq2inp__iMOKvc4mRupJIBaLQZwwAoPDyVNw63yx3wSF1Hfsx42AbAJhzCxktB9PD6urFkIqRs-mVVJIXPKscgYW7dZrFe0bWhYxqPqfmQk1WcGEMoZuv2Q-Rx4B1MkFsOxgkvXtlLXkqigXGqdUgOkFa4nGOKKSpJ-9_JPZd3bVauNLFVUHQHPryZ-mmtqH1iJwE_--r1AuWSSkL0o0mu0IzldCmP1spPegv4_SSLx3l9WJ_b4erPgIHFIGBXKmCw9XVIhScjGREj4fp7g8H-YIQD-Qsrdp5iFatTqRk6gDKpAkuLjTgMbKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=q2oe1EGT5Yhl8p6Q3gaiw3-qhlV6_3SW_jdn7Ob4ciGSkcE8O4AE4DCgcNb1yUUo72GoVIkbnhK1jnajWs6FcINym_LwRgVFMJVINMrdQO-VPABPtEFfI58Lgkij28cz3oOwKvjMZdATEdJriUrNkwInKZMbhGFUWqe_6bxGKXuFKJHvo2sSoDNmZs3vfOd1KqjMMJ8TLMsEst_4V7S6UI0L2drrnjm7_S3Vym8r5V-1qJaGuHOpv9_KDAoC0p3QIrI75QX61H0Ax03xjL7iW6iMxhjXLoELioMsr_aCK26dv9gm9fAWe3HG6Jtg-gKrgFn7UTLBUERsALMgw7-w2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=q2oe1EGT5Yhl8p6Q3gaiw3-qhlV6_3SW_jdn7Ob4ciGSkcE8O4AE4DCgcNb1yUUo72GoVIkbnhK1jnajWs6FcINym_LwRgVFMJVINMrdQO-VPABPtEFfI58Lgkij28cz3oOwKvjMZdATEdJriUrNkwInKZMbhGFUWqe_6bxGKXuFKJHvo2sSoDNmZs3vfOd1KqjMMJ8TLMsEst_4V7S6UI0L2drrnjm7_S3Vym8r5V-1qJaGuHOpv9_KDAoC0p3QIrI75QX61H0Ax03xjL7iW6iMxhjXLoELioMsr_aCK26dv9gm9fAWe3HG6Jtg-gKrgFn7UTLBUERsALMgw7-w2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=SFBKkMtLpg1M7o7pKLYqqW9E7I1Y2moJ9UDadQvc_iMa1r9ERxARAHNb4JHlMybtD5-LFTbT2K0kqKmQuQcYt7jHwoNa4S5DSXEXylyWjEzneRPODVfx78sXQBJy9vLbHmuPO1ZwyaQRdEK3JllumCUxwhwagP9L6IJCecdcnTFKRyvgvDrpSjZlri0hcv8BrmFzmuvbA24njBhEV7d8GL46MvL_FAgepUdDv2Fp1BfF9fEtnAU5uZz3hBTFaivcC07O_z2TMOsk0q4fHayvqeXKgczUflDt9mRspLSUEV76kE3_0VXZqxEejO9KtLrOsfPYThEOJaroiAOvX-x20g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=SFBKkMtLpg1M7o7pKLYqqW9E7I1Y2moJ9UDadQvc_iMa1r9ERxARAHNb4JHlMybtD5-LFTbT2K0kqKmQuQcYt7jHwoNa4S5DSXEXylyWjEzneRPODVfx78sXQBJy9vLbHmuPO1ZwyaQRdEK3JllumCUxwhwagP9L6IJCecdcnTFKRyvgvDrpSjZlri0hcv8BrmFzmuvbA24njBhEV7d8GL46MvL_FAgepUdDv2Fp1BfF9fEtnAU5uZz3hBTFaivcC07O_z2TMOsk0q4fHayvqeXKgczUflDt9mRspLSUEV76kE3_0VXZqxEejO9KtLrOsfPYThEOJaroiAOvX-x20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=Chg2ubsF4D_BVDOG-sV53fkaTnvL9rh0R0NVt3qFQBARHbyxxofEqYtWtXg1dj-ErpnaIv89hVPBcq-uyeWPpugjMcg10wXR-Io14JzfNb_AvdXQ-WztpPO999OEGYoRuaip2sU4d68_c6eAph1dUsx3HvXi3leE9s2Pmxu8MWmB2Xr2T5ZGabjYN232Bl0Tb63otK_mBet0tE1JMpFHQ9xIPrq2UwV4vW2-h4ccWElb7RrsCDX7OND3iBZzAt3TQE-zTkoHBiOdZeBmlgwAzDCWbSbbsdKHrdFqw1wsbkx-Ylb7nRiqA11rBmnRnGJLcEtEyopYAfS60j2nqIT22g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=Chg2ubsF4D_BVDOG-sV53fkaTnvL9rh0R0NVt3qFQBARHbyxxofEqYtWtXg1dj-ErpnaIv89hVPBcq-uyeWPpugjMcg10wXR-Io14JzfNb_AvdXQ-WztpPO999OEGYoRuaip2sU4d68_c6eAph1dUsx3HvXi3leE9s2Pmxu8MWmB2Xr2T5ZGabjYN232Bl0Tb63otK_mBet0tE1JMpFHQ9xIPrq2UwV4vW2-h4ccWElb7RrsCDX7OND3iBZzAt3TQE-zTkoHBiOdZeBmlgwAzDCWbSbbsdKHrdFqw1wsbkx-Ylb7nRiqA11rBmnRnGJLcEtEyopYAfS60j2nqIT22g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkFcVPhnteWniLt24CJNeiGIlQw-vPc7gz2i9wNkRZ7roPdzzf4HVCMjgtnzLrGEMTj3i_jdwpQAor2si5lN0AH8iIZOfW5DSbLnJEu-hFKnKpksoQknkZikeFs_GUYav5NnHUDOvS4Pnx-aawcX2WUWS-AiM9aw38NutpYME3zDbzkpKYz-HBWKt3GsUtakScbPIM4sLqhriB-PqCZZxiHGAkXW_cKMKcBUrZrCOPwjR9xbStCf_NJvIVG7hh9ufFcpuLEbMIFavHlEqJy0j2ura8M1P3hKzBkus2XDn10oTWa_qL6lvdOe98aPYBR3Ad6PKA3unrRF0gmjpGzFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=V3xFURHzdUjjwkXrI53SKyw1_Po064GCrU7cZpzH2WMZG42wg7rwlv7JJLNotQr2nirhaVnaPTJUmkapjg1ytl6gjAoZDHQ-Xh_WZZPbT8PXPLX6ZpHaTt0Uj7kL2UeGRkUlloSTLcFd-cNQEoUPiWfQnHsuM6yS5wqFbE0Nqke6847qiunhxF_-JLSGvzrhVrAa3DLpWSGbjMy4VkGt3NkBvzvsj2NnSSALYiE1NYoDHusYWGXuuCTmjyNkp8t_3QUUgJ_QGigPBUKN_Lnb4ruvZ0T3G_WKUNElWH4-Vvs72HYztBPxQCQ0NpW0e-whU2dA3J-nKgb312p2-DprgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=V3xFURHzdUjjwkXrI53SKyw1_Po064GCrU7cZpzH2WMZG42wg7rwlv7JJLNotQr2nirhaVnaPTJUmkapjg1ytl6gjAoZDHQ-Xh_WZZPbT8PXPLX6ZpHaTt0Uj7kL2UeGRkUlloSTLcFd-cNQEoUPiWfQnHsuM6yS5wqFbE0Nqke6847qiunhxF_-JLSGvzrhVrAa3DLpWSGbjMy4VkGt3NkBvzvsj2NnSSALYiE1NYoDHusYWGXuuCTmjyNkp8t_3QUUgJ_QGigPBUKN_Lnb4ruvZ0T3G_WKUNElWH4-Vvs72HYztBPxQCQ0NpW0e-whU2dA3J-nKgb312p2-DprgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-F-Le44H5ig6owrvVk_VPcjwml8k2UIr9ZJ33vsZHE0syeOrmZEfl15AzrkhIgon9iL-1TegpoV9v4R1zAZe14FKFkWWNnh5-LD299OzNzzBVVOEID9l_uOHMrQyQVBFSrKdJUsGm9c9gZfNPsIhEZi5ZvoEJoNgL9poE2j52ru9pYING4qPflJRR7Rn7HVCHxTllMmVbycGiAbtF6jbPm6iBk4qJmuM1LazDM-e6NN634jbfSWbbqZ48EsYJQKM3BVon0B1bzGfNKSjbkYHtD-tZmtw_sifqV2-69KC0TsSylYj61U31-Duw-0KwKdZ38e-BvVWk9xNf_Zj0SafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5Dtc7AwbIJiJ77ZxpKmfPkiiCdWio1klvBOPxOdSup9Z2xezA6z3sih2WCxH5tvEgWzwmVoU3pubX0JFRXLghqoA5BT1saNQVxrhQ98aBuyYv2FvvtxeBittIEU6Ai5caz8YsV4OeN6TonWVtzAgV-j52HKQ5eT7JuzokPQbYNIOgfW8ioNPO-avhMG2LXZhLKH4zdFFxBaNhBMhqUWMkv_hGURvm3Y4WMzH1JMzGsT0Z-ArcNXQjONjOgxq7qKb0hOPXF0F6FYJd12BPBKEzbhm63Cmc30PHNZ8laCESe6ICU9utlkOupghGJLGsLQst0ohbPjhUAOdoyLIT_O6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLRuU2Rj1XOpxlu4m3qXrWkFoNiwCNVTqL-yLWz58EoMroxub5585vdI1yHih4f9-UBArDNZKGPQtuFbMbg2NxXiHIcZVT6MdYNj8hazX3P_aiS3uzKDjS8LtL1hpedPPgLy7M46AJ24DGJrlMAnVYQ-850zGr0M3Q8v7-oX6juiSA1FiOOb2ig4ly0xsZvoYWnvTAUDCjapxPRyATsSUdS075EF41ryHn6ellhDw5fnOiY9nJsPeDnS1LoCDW5gQ566zcSzVh0fcOwR1MRkVEHkH_k8S86sgriIud4ZMNB8loUoGUIYjBIfzAlRRpkj148M6LbwVU4B1o09D7OGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drianhHmU3ZMcgzzRuOR8lD8z76XYJRkmd-7trJika5Jw24VMGzncSDRglIxOFnfEkncHbX-wmnxc3rzWJwJ7uOkWBnGU_5JoEKHp3_Vgsv6uuTepQNWfi3OGnkaPn42x6mKwZbKwJGcd-4nvjJkeCGzRsuaWeen1D3BEhrm5qNXUbzV9ttGx7trR9AjIN4BBS2CjcCN6u6cT3xH1NthDflDi5k2v2gSxkeKr3jHqJjqKvoPJGSicnxmAmne5u3RVPw1Ias-3KtSQ9yIAI0kJE8PVhEqhmKCOJOy9ehpzzjgkDKrjZWLAv2uJ-8iVRIX8Uxx8tMI42VntxHnYuDMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=rgNKk8o01ZHRkbuUUpChaVuCzQrwkcH_WNk-uqJawagGfDcTsb7fEVXXXMy7rqomKJCMhAFKZIAlqmcZrD8E4Y7z3svIryX0weI3FkjwKMJLWtQvxjUJKa_bZBo6Bkf43N9DvPOxmDL2G7LyX_X_Fs8AWzegtEQYhbbQoqP4JDUPdNxM6DBwOamJdxPbgPHb9_SzB2o4dr_UD1S0UqylPVQhuhEsHv2f_nW3U6CV0ucNLaaMW_VL0hQVD5Bc64y-UaOiVPgQxK9ulaW3DPUB-Cos2g4lPSEhGUev_l-8XASy2U9GGpXCSm0qdJM8Ht3F8uoQQiNd_hArHHy2ydBqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=rgNKk8o01ZHRkbuUUpChaVuCzQrwkcH_WNk-uqJawagGfDcTsb7fEVXXXMy7rqomKJCMhAFKZIAlqmcZrD8E4Y7z3svIryX0weI3FkjwKMJLWtQvxjUJKa_bZBo6Bkf43N9DvPOxmDL2G7LyX_X_Fs8AWzegtEQYhbbQoqP4JDUPdNxM6DBwOamJdxPbgPHb9_SzB2o4dr_UD1S0UqylPVQhuhEsHv2f_nW3U6CV0ucNLaaMW_VL0hQVD5Bc64y-UaOiVPgQxK9ulaW3DPUB-Cos2g4lPSEhGUev_l-8XASy2U9GGpXCSm0qdJM8Ht3F8uoQQiNd_hArHHy2ydBqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6AqxlZ4bTIPz3AZMePvH2fa8hY3mWFip5kGCgNucmVTdUR2QDCvp8Z3bGVQm3HK7p2um2MaoswzZW3lKyFl4o731Qh8sKdIhaKNuk1t9HtV9FRx5Q2igX3RvvSSvKpR3Hyr_OXU9GU1wWLOjhQv3yccLDZAEHyUTksXA9JaUdau-7LOgZWGDumlqjzlVEQjjk9niDojH9wTHD11-15czf8JU4lwhjdHmTE9svLtgewwRNg0tENQ40VQTvHmYuDSxN7P9Y57ajXEJsVhGWg8yC9MRjAYibqaVd_-lBWRgJh5pjSNXl8xGhO-UkuVviJm25i69t9cKCkvtC6dcFWqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=JdTmTI4p2GylRkrrxjxratGk1nr5Z6AJBkiWqDaTje917YETDXyFpl3H0SvAfR3EQDyzbptRorn1B1f5ptHdwC_Ui7-9WhiCMOFUqWVtIErIzYKxEQclPXxLDZr4ZFMgP4FMUMQyodOuJtUNBon0xhNkc1veYmFXcegtg3EpZrj_zoNEPlqe9E3GT_NWMvuvXbffKEohBAU3x2W9DdnttXnDQb1EzQ9QDxED2PnJXawb7gCTOrj5og_Wlkw3g8unziRNIUYVf4jqZM5iu4Wk37-P592aF7ggGt00tc9JYY-WG5nAKNyNsY_Xo-_Fhi2TWM3fjRh64DX6AYPuyipsLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=JdTmTI4p2GylRkrrxjxratGk1nr5Z6AJBkiWqDaTje917YETDXyFpl3H0SvAfR3EQDyzbptRorn1B1f5ptHdwC_Ui7-9WhiCMOFUqWVtIErIzYKxEQclPXxLDZr4ZFMgP4FMUMQyodOuJtUNBon0xhNkc1veYmFXcegtg3EpZrj_zoNEPlqe9E3GT_NWMvuvXbffKEohBAU3x2W9DdnttXnDQb1EzQ9QDxED2PnJXawb7gCTOrj5og_Wlkw3g8unziRNIUYVf4jqZM5iu4Wk37-P592aF7ggGt00tc9JYY-WG5nAKNyNsY_Xo-_Fhi2TWM3fjRh64DX6AYPuyipsLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=aYphCH1Hb6-u3nEqbmsziVdJ83cwgmng63W3-KdnaTovp8fhDR20bcGCsQGeb32dczTNlc08iB7OwOruo3c_qfZnACXQ0M5KoGepDQFYtGe9H0fmPa1WU_FqfEyBWlL8M2tek1GGoQPV0-XPZSrAWyAd8cQSeiiYW6b9hgPAnvM7aTBgHzblC3YajE38019fwt8MtgTXy5jSLTFokfLq-uYKUJAh3MxnC6LKYfEG9KnhhHwxNU2M_jc1-vqdbWLvi-gwqNiBxKv_Hz3o9-7cdYFuHMqaifp-Ivc9RJpyiNQVGdA6XCwOj2PdPw8pUw5x-bfpL7UYQbzOvBLrJPKxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=aYphCH1Hb6-u3nEqbmsziVdJ83cwgmng63W3-KdnaTovp8fhDR20bcGCsQGeb32dczTNlc08iB7OwOruo3c_qfZnACXQ0M5KoGepDQFYtGe9H0fmPa1WU_FqfEyBWlL8M2tek1GGoQPV0-XPZSrAWyAd8cQSeiiYW6b9hgPAnvM7aTBgHzblC3YajE38019fwt8MtgTXy5jSLTFokfLq-uYKUJAh3MxnC6LKYfEG9KnhhHwxNU2M_jc1-vqdbWLvi-gwqNiBxKv_Hz3o9-7cdYFuHMqaifp-Ivc9RJpyiNQVGdA6XCwOj2PdPw8pUw5x-bfpL7UYQbzOvBLrJPKxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=r4IwgG3ExKIOoiDicBc5qNTPm8T0Chaokwu2cUx2pXFV6pinYlrSjcynmJbaTEKHtAdCVE8BsBNKUJhXDjKPXJwCIsNZyGBWlyB2lDt6m_ZidyVQvjM4aAz7q_xMqWC2ALj4fH-PjX3N3UYk2J-H4P_tzd53YAxVuKoN2_j9SGKJdOFK4RKQWVXNDe-ua6qQV_ltbNhd4bgCTSG8HNPM3hiLCaNaCIuQx7PCiEmRYf4D4W0OYZi2uBR0xq2NIcxIWh953DhmfN6n_cVM2E5b80QDxjIYW62IKnWkyCswS6pdnSTxMzRCOMKh3LLGILBVKuw2SDG7ZgO8hMFfAhnkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=r4IwgG3ExKIOoiDicBc5qNTPm8T0Chaokwu2cUx2pXFV6pinYlrSjcynmJbaTEKHtAdCVE8BsBNKUJhXDjKPXJwCIsNZyGBWlyB2lDt6m_ZidyVQvjM4aAz7q_xMqWC2ALj4fH-PjX3N3UYk2J-H4P_tzd53YAxVuKoN2_j9SGKJdOFK4RKQWVXNDe-ua6qQV_ltbNhd4bgCTSG8HNPM3hiLCaNaCIuQx7PCiEmRYf4D4W0OYZi2uBR0xq2NIcxIWh953DhmfN6n_cVM2E5b80QDxjIYW62IKnWkyCswS6pdnSTxMzRCOMKh3LLGILBVKuw2SDG7ZgO8hMFfAhnkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxFoEcLuMnZQXQCFe9DXblMGhKKFs3tOmnfK93iC7BG7xH641orR0WT4RHrlTpU8ylZrgS-8EUpDA2eeFqQu42v8HAmZ-TtKCGmRWJP8E1UIzmrz0V5sLGWgUEumAOH4zRUvdZTlp3UIewJk3Xl4VxxyUaCiYog0fKiD40ewxQc50UORzWRv-iLwNGhwf7NhZb1QbZjERglxUEIFKDg9gvDC0mnaGcxJDWkruQjmnDSKrjYyFk1eenC4pgpsh9rRp0LON2xngkbobwBP7Fc26pCaBZt9F-k7CUzE1XijEdjKz-i2es76NlZNTuujtQIh_PLAvm822gDiKHpmvr0lYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOj71Pd5EMLz2RvuZCkQRDtbXL0HFTLoWwzxfVpTNDSOjc5BFxJeHQ7_ijUBSbbFsn_htbkpfF88a5zooPzwN7cTEarjBXCQZgp42hQyv1ayoxTLxCiwqck4f-vrgTQMJIDr12ouVRm_gv6nEccit3gt1sA4EdV7ZgVvWjG8ofHbTCyTtiygi91SNvQ2hQnUP6kYMQFuCdAJc2cwngSUa6vcJfLxhkEs0MIDPMKjfkbL5Ne1QFO-Eu8rX8VBmNNtINo21u6zSR5N0v7g0gmr5YyhunW3Wi5QyX6v6rtrjCNr6-ry1_OWQNVZEeSK1BgEVXVFkrNCgzyki6WGs_wgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=kwKPI8aN6zrDomLl9aBkK14pRSNbIachvnvgwAvPuFzhmpF444JGsNveRq5pB0glAQ4XrOLu_cq3P9Vi06KjvqL5OdcRnKXvB5BrDDVsWhKPb3MULQaiBFIffoPAaRMAWuF3NqbOmpvwmt4hZcNAZzhCXAUA2Av2fkgYF6KNmgLbKq39QIb5Es5Mx6e5zEo4_cuSmOA7BFLyWfTAh5duVqnG2k1bZ1RneqHnHfURlVEjKBzXCKxg72g5E-j3Zt20jWdu3iROLIM8zN4UX2K_J28ClrxVjXOgkhFQSEzEpXpiBBswWePDx929y89vtWZ9V1g-Yaaq7Rlu6atydiR6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=kwKPI8aN6zrDomLl9aBkK14pRSNbIachvnvgwAvPuFzhmpF444JGsNveRq5pB0glAQ4XrOLu_cq3P9Vi06KjvqL5OdcRnKXvB5BrDDVsWhKPb3MULQaiBFIffoPAaRMAWuF3NqbOmpvwmt4hZcNAZzhCXAUA2Av2fkgYF6KNmgLbKq39QIb5Es5Mx6e5zEo4_cuSmOA7BFLyWfTAh5duVqnG2k1bZ1RneqHnHfURlVEjKBzXCKxg72g5E-j3Zt20jWdu3iROLIM8zN4UX2K_J28ClrxVjXOgkhFQSEzEpXpiBBswWePDx929y89vtWZ9V1g-Yaaq7Rlu6atydiR6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=GpJA9zgM7agMAFVd9Acb1r-kP9QoCha9VenppCayaVOLa5iul8V1iXjz0a8zW-8d2j-vgYamBp4ItyouCOcJG4uzZOjG7bNKOPBycDfwEIana3MFgovmV4iG9gJHzsPrY__Grm1uQhyJ00FmputCGVuniUBymZWdWon7RpQapqa6nNcZhEsw7sRLPxQ51Sst_MC15CY_lsZvlcutzWiKSRC3CSiocN3KRv45ZRBL-tGUATgdBr2CFrj19UsRhppDhHv5B-_hc98xZl12GKu0Shoaz3BUqgFIzUDExY_3MRiLAmR-1nebhZo05zEVHCVxY36L_oVDYAx7kEUvvmPsgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=GpJA9zgM7agMAFVd9Acb1r-kP9QoCha9VenppCayaVOLa5iul8V1iXjz0a8zW-8d2j-vgYamBp4ItyouCOcJG4uzZOjG7bNKOPBycDfwEIana3MFgovmV4iG9gJHzsPrY__Grm1uQhyJ00FmputCGVuniUBymZWdWon7RpQapqa6nNcZhEsw7sRLPxQ51Sst_MC15CY_lsZvlcutzWiKSRC3CSiocN3KRv45ZRBL-tGUATgdBr2CFrj19UsRhppDhHv5B-_hc98xZl12GKu0Shoaz3BUqgFIzUDExY_3MRiLAmR-1nebhZo05zEVHCVxY36L_oVDYAx7kEUvvmPsgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sacvloQfvT-_6qQ-ZQ_fP0bi5gyJETpr1J0bgNhSGVe3PNF2wgQqk1rzkfIh8-9nznGQkQbwgkFd2MLj6HkopTorWQoEn46zK3ikXeESlvpzhBfM-Ok2w4ji3T8nsektMOBMeEdYHJLkf5y83Y09en4119j2Cr01tFLBHrVRZb7D3Mfxbwr1TyDTk42vqI_CiNFV8fJN5iOZpF87c9w5rxwQ6lKX7_-cNJNybPQsVbBBfam-3jRj1a_GhRrCGtfxNeUdeVKxtyHoko8P1dhIRyMRM8km5PTRZcgvHljgJn6HEJ4kgDb_rUBdLdZhRG_KspzEssotEHBSP5Fki5QEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOt0yasatPn2MxLaIc8JeKH6How17ftTtJkYWVxQGvUq022IYiJJHTecPt5GtezQkVX3x5obtDBIq02ACTVyvOVjficN67S-CdlxG3wmqh3bJ4_Xy1UJg6ScQCwoCFrnMvvxEzp0JKUnNEenWPt1P-pprw2gpEVNKbSf4nE_IjjKEAQJKDIVm2gVQ2pkcfp982PGx6ZZfDntysYAV6wQnbnhBDp0SsVtUd27id7t5GMa3-uHlNkWvqhh6nE0mWRmqAVyuN8klRzgiXpVIgrgJ_NZwCwI9ddVLFIL6H7PygEwosQyyY1lmVn4lY95R_ASYWrM4Spqfb6-ADYXeWfgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=PCPhpI7yHg7PLZlKa0uq31y_8N6zbbYkg2_qHlrJqtejUohrjdhYOkz3zA238MzvYvavNRqxS6-FUKMkdI5QbGS8I4yEK4NDMeX6dWHlv96KWfD9517h2fNNt3mq9F-6olLRzfZvf_mYKdCsrAMKztRBIPwGPFi1ESYn35opDp314_yeAqwNTYHw84R0Hc3DqzZyvWlFPslJfYK5KvURvjnEU6mIB16-n24cTjPpG08B7OTKT7GiyIpqfNoa3e1my0k66QFghbaveFnAqWDXo-fuE9_I3T3lT2rCRD8r0oft725cgV3ISGgq5sP0hWzd6bUeuAJz9crxCfMsSmn3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=PCPhpI7yHg7PLZlKa0uq31y_8N6zbbYkg2_qHlrJqtejUohrjdhYOkz3zA238MzvYvavNRqxS6-FUKMkdI5QbGS8I4yEK4NDMeX6dWHlv96KWfD9517h2fNNt3mq9F-6olLRzfZvf_mYKdCsrAMKztRBIPwGPFi1ESYn35opDp314_yeAqwNTYHw84R0Hc3DqzZyvWlFPslJfYK5KvURvjnEU6mIB16-n24cTjPpG08B7OTKT7GiyIpqfNoa3e1my0k66QFghbaveFnAqWDXo-fuE9_I3T3lT2rCRD8r0oft725cgV3ISGgq5sP0hWzd6bUeuAJz9crxCfMsSmn3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-AZz30remAMYqFot0ZX6TjOoHBc6fPf0tfMsu6nOsqy8HMfhKJEP_lm38qBTxmtWE9XW8_YjeMJZVds_YOccG4jzyBAbq3jX6xtezVe2Z5K4Pxi33880Be_pu3IVV8qQqEGUnlf1WUgtBTzz8kFpg_xP32zjfWO8u7l53dRAyq76klMfOHa3jTCZklQcSPB3ZOMUBIfgPUUab-1RRHmMXOGII2mtHhFuQ2-pghTgwDsetNJug3EDLyyY5ZRvVn-mUNGTpKZRdiD9hjlN1mpZWjKIvDBWl0RCTN3n7d0HNXCasY8YxIlZt5U0q7MyDhBmqd0Atni1ghpPPfTGP4iEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPrxT6AY-FO-XLcNb4Enazgpl_Vb9BBxvi61DR1bKdNIhgL5H6fAqt4fZJTRUGo25hrHMQflgLoMjZfOQt6d_aqvsurF6Zf6vHgKZYpKUb73UFtZ7Rx0CJ9J4z17JqPHL4htrv35-rSct7iYrMhoyyQWwDfKypf6U5PIvXtzk3xg2F-l4lNu27Q4g-NlnxZJUtz-Qv6gAZRA_97tXV7JKzQQMXj4Pr9tWFtkF9-6mAmpcRTKPge3J7ORBruFVtle3N4PU-fRrPF3OMih81cxq8wvMKUIoTt4CkL2eBq3u8biLxB2iVpvM6fDy6RePypJVCaXwbA3E-UM9z5SPHFLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9vUaw5RFYZY_Mk6WrNctr07RGUekVgPgWsu4GZO2HzCT8-QkFlc95tknMNSwPMkP_oV28ArcfnF8i2XJGAbScKwcqnkTCHXeREFXtLCkPRlk53IVcCvIgwl0iHqzHm2ImMExPV4QQOkZb7IWo5N2It_IXdb6zDIJx9lOgUOfVNcKvMNGe1XHpMthrXThY2Tgzk_lsBqET2SYJgshjTZ4yj98YbWPytt0HJCnFxtLDq3oPywsLTCbAU--z4dRZbfbtCk1sCv3zFHBXN82rIw6HgCi4tu3HdPo1g2TJWyQ2KeGOoQAG6Zb11Lhe-Ttoc6w8ml4UCzkAsAcGeivQu2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moKTkkPnmHjT6bUHbYLnTGfF3FsXn4TllILfuzQsKL_-4fBj0NbV78H7uJL8MHUnxvXVWmQx0Suf-WSRNPx2aEm8aj3YSA9sjSsxGhwwjxC7eGSHYxi9aNyAiIDVoso6b8_C_LEclGKwlmsKZsumfHQRwREquMPftbUlcBVk1C-RHPqH9MtbToL8cf2gBujPA5aMEbsGKHY8k8XTmhp90CODIpq7CSF1gLlEnW0wz6plz3u-Q2MDbY-HiRA0uZTxlEBdSMkrtia7lFPv_hNGt98GLLOI3oiZNttgzWAfTi4wHqlR7MH4Bz1sggT2pw4yL5_5yWboo3-yOlKEuAIJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkOx4mn30QOQQTd5RMSdct-hGe3eyvldiKtJxBDH8SWdvlvEZ4RrZ7_le2BfebCkqelGtmfFuht-VbAYejXL3mTJHRWhgAIfWV5FySOn3Vc9PPHNYHC0YjJUeQXf5gtEdxI62t_jxRg1S58EN-1zpBiolM7cgcN5tWVFrg4DEDo6Ju46oSXYw4nGO0sPr-g3BejUn2gqpF0hCZcDM3Ms18Y8e4_FxqIcBzTCrr0BovhaJkYabKKLPuuAwetBSfRiOiWIYzOXzlhy22A1OQ9XPi5MkvIFcocJBrAg7o_Fwz8Ij2BLJAdsSR3cNZqCiH6ReKeBa7HigvByQk6JnghVBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXjqvHytzfp1u2nUP9rhLUEe4kvjm6vi0MDK2YX4cD1qrMy0xEkqsDlSOCDSaKhLC64q4WlzYkrWfn78PrvFMF-ftHut3QB0t_vdSWLuI4PsmwmioJueGcSqDY4FrT-oqmimUxmw72lLr5djB_-Hzt7iGTsKhJ3VxAA9e6LEowGXgyxSeAJ33hrheYq71rCzceCuSyXiyLfkkdXjOw8MJ73_E58xMb-i_GAiJM1pF5VEu2KIvoY6Z8t8qWMcJqp14G6BjGgyTcHscGNIyKKIq_fZjI1WydeJqqR3T1Ii5YF3WEAD2UzkLLInPOkZGG36eDgK6UR3ijCmDHNBNVzGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwqCPYttFWBnJs4fr33YR7DUsJk7Fhx4o-tINhwMgQ6TQCcvIDHmjz744Hxq5gCApKoUYSeiAaqkYOFoCYDuwDVGOFr45E7GwDk39uVLe8baFzM0Q9OUS2_CpyI6sZ8Ak77YUKFGxHTLWZKlIxg-qhO617b4wVg574D6e4Bf3fwdjI7tyUEDIj9BZnSWN4lh9VjCLo1dvfh8B7NW9FzVLOcAsfKb8yKfNbGxDutqKexujNJMIR_-QPgeX26MklaCrC5QI9AltLEGBeh4KxaB_cGBs64SSLrlwAAXhFp0ae_YmM-2ueFlq7x7_kVdEln08skUpUWBT4toY_WKJT-R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARwLwuF0N-73MaZsTPK5gi9vgwAtc0G9f3ozgO0wtvICHTEBKR75LIeXytz05qRzaiYjK8k1GpX23TYFaC-ZFdIXcw9af6BJ1dUgVuTcjkFnHBOUhXElIgWjuvgEAlB_vyc7oVxylbEdkaqK0wKQeE50NgyaDa3JBVe-3IqxTa2sGh0Ntfpenura_kVk7swRh7KWnA9EMCCNlb5fjfq6cqzrISlajU-qJdG9KKf0ldvrhNOy4tH3LoDCtC38k7mJib6Jq4urJccxgIjAFRPanx5cdrgysQVLF9PkiRCP5h5zDgNENIPJjW3h01lW7MTy7cJA5OdobJVrAAjcWhTzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=jq0rBlYyvQEWUXnnrdHCuL9at9XDWdfam8r2qyGzVBv9KltAdc1jKaEPfxr4tqp1xS0JP-F9U58I1nG5NRWJ7cE1sHmxRWEZCvakmz4gLgj5yulE4uSxm21nrM8hW16hpYYbFqVjFqwVD0KPmsINOkvfP2KeB-KFJhQXRJ5USi3bhI33CPwTaXCuQ51dUR0wjEAMrmZfPizqTMV07hAuj_Htyl7MC9CrcgykK3se3-8ksXvIdNV61hmAfiTZBKwLWfM8HtNLhCU3AzYNuIlNsXDiJgkC0soKRL09ocox5IxmxW-5EWio00Ff-GK0JnAKE5O2XJFyGh_8wx9PQq7s1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=jq0rBlYyvQEWUXnnrdHCuL9at9XDWdfam8r2qyGzVBv9KltAdc1jKaEPfxr4tqp1xS0JP-F9U58I1nG5NRWJ7cE1sHmxRWEZCvakmz4gLgj5yulE4uSxm21nrM8hW16hpYYbFqVjFqwVD0KPmsINOkvfP2KeB-KFJhQXRJ5USi3bhI33CPwTaXCuQ51dUR0wjEAMrmZfPizqTMV07hAuj_Htyl7MC9CrcgykK3se3-8ksXvIdNV61hmAfiTZBKwLWfM8HtNLhCU3AzYNuIlNsXDiJgkC0soKRL09ocox5IxmxW-5EWio00Ff-GK0JnAKE5O2XJFyGh_8wx9PQq7s1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdi8_QNEcjKMKIrolNFpluZO2xY8dtPXW3_x5oWrYUbFbqLaPKRRrtEXR5kjtDOgxi221H5JOrF0_4eMm6b_dx1iapUMY7VMyNs-qVDVeEqnuAdmevFSzfEPHBOgXPqOaSydWO9fpK1SQghqaAta8TOpfjczomfVTsvQGstS31sQQNVFUaQaOPv3PeXR9pvwDTyuWxHIvPjH20t82y-7eKEAGHpwsF0ocaqQF7W1w9VNFlF2dbOieh4fL5sMb7fnlgLmlShtZ8SUX2MOxSPyQmlBNQSwb3SIE3IOxiB6GadqeYmRY9c34n2FwqJHh7AoxxUeWGXV4WR1-8DMoU-Ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdZZAYHYyfLBG9kqFBPj4L6d9Uhhs8vO5EQebl9cCDZwsKGcHrs2kiY6sEXps4vOFqPNHlNM01BW89WmtglyXAnm0J1thaN9vQ1Y8zlcpSDJwa2UfPS20RV1QOgkv7DQy_Ipl2D_lsSYRCVIrogmWh9w_YVyk_F6ad5kyXbKPmOSiwPIceOEiqwUziVN39KPq7joETOmecAs5LA3Kx8uwZpF7FY8dCGud2Coi0VpCZF4jhEMxcfPa1XttR44Ff1X9dP1a-l6wR_4hKBFuu-BjJZu9rJ9yVN0qUKgY9DRmsSGlqddJgkpfsEUpvJyjCvVc9JdRE-_uptQxS6OUO6fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNcbGD8KfZ0zj_GEokyplCuf9zPAatch7jURg_7LOo__N0MNrtYp6dJAe8jPiocj-MVREcXbLlAEaC4oTzjYX4z-0fCcJRGUGN6ItjDqoOuu3s5sDhSeFRbJ-McZRgVaqAUSIIFc-6TnnvhCDmxXYlY1ye7K5PhTX4OLcjKdAVrQ4p8ZsNmSZP42gX4vo0zRpGRMi7U0wKhoED_wuvjc0-MM9DIn_UmUreh4rTT1Um8bo1qycKHx4SrSaN3PQQ_M-pRga0-ckoq8XG4l6uf9MQIXwQtpSgKPXPmNn2f_9NalV9STpT28_NugdP4DLeJX0sTWyywGjUE4P3dXEeiMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
