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
<img src="https://cdn4.telesco.pe/file/fogeeeXndhxjkGs-GzOht5B7gFZYrvaeD_tkztzLFC_YSf58gBERtqi3c59FvbhdFgjMIxv6igspPGf97tRaHtwIo2WHX7BnGwAvFnvCpBEPRa2HcZFHNpYbDwMBiqM75DnE9zLfFbAnm_jfro79RU76rxPfXVo09ZiJi8dMSEMoodgFPtuttikzBWgipQOH21TOm8lwHQ1xQkP4fTjZmMa9gg0pFUOi_cpkYApy0DCSbtYY-aobFuImbzJiRYtQ7Xf_ccDLlpZcYGdNF2CDqi3FDkoywQy14IyJIUYsZ6MfMq-gUHobi8kWWHqcR1IWX3PkWROIahWRbLuwqngV_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-442179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuP_NbpfYCYTIf5UGgZPnp0hlR22oplWSXlwiA7oQ3Q_FNtX3wN2-IjnTCKWTy64jjO_7KM6rEgmn_otHvIUPEMqrfp7-LFZgzUTTSMEFkZZVW0PHrfIQBtw_E-6VarmBfBS0ET890ZVNcpRrAk4716Epbo8wPnRXypiw3_hw8Wj-QDGduMUVTL9cgr9dEQDCanyBXq8YJpIk8Z_UP-Oio0B8AggwD21c_7vl6DFX3U4MxrO-WwmzB1fZxT7HKTqd_GhGEEZhlSuPI7km_xjG7TN8YwCBIgFQ7gKgl29gUpA5oIzaPiQN8pGXrE42-4GJXchsrrX0NZYHXWN3q7glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بمباران‌ها خاموش بودند، امروز برای باخت تیم ملی فریاد می‌زنند
🔹
طی ماه‌های اخیر، گروهی از افراد که سال‌ها سابقه فعالیت در رسانه‌ها را در کارنامه خود دارند و در جریان تحولات تلخ گذشته، با ریزبینی تمام، هر گزاره و اتفاقی را حتی در کوچک‌ترین جزئیات بازتاب می‌دادند اما در کارزار جنگ رمضان و میانه اتفاقات تلخ خاموش بودند، ناگهان هدف جدیدی یافته‌اند، تخریب روانی و ساختارشکنی تیم ملی فوتبال ایران.
🔹
این جریان که با هزینه‌ای سرسام‌آور نزدیک به نیم همت تجهیز و راه‌اندازی شده است، با برنامه‌سازی‌های فریبنده، مصاحبه‌های جهت‌دار و تحلیل‌های شبه‌کارشناسی درپی افزایش فشار روانی بر کادر فنی و بازیکنان تیم ملی فوتبال است.
🔹
آن‌ها می‌دانند که فوتبال ایران دارای عمیق‌ترین ریشه‌های مردمی است و ضربه زدن به تیم ملی در مسابقات جام جهانی، می‌تواند بزرگ‌ترین ضربۀ روحی به جامعه ایران باشد.
🔹
به همین دلیل، با صرف بودجه‌ای سنگین کارزار وسیعی راه انداخته‌اند. از تولید مستندهای جهت‌دار گرفته تا مصاحبه با چهره‌های به ظاهر بی‌طرف که هرکدام سنگی در مسیر تیم ملی می‌گذارند.
اما هدف این افراد چیست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/442179" target="_blank">📅 00:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0d096897.mp4?token=JMDWimDMFf73soLK3zVLH99uzqOAJIqjM88dRulp_hga0IF4R_FsRDcSObrONeq-MwCG-leRzXAsVJlo4WvDi23fIKTmhffoCUYr44q_faTlzYnnA-DE93Jd-rcCHazHbHbc7kZdEq0_0Fnnn96w2xKiT1L1SSsST_hgqXwRMkCQHPf8n_LoX_I3Uw8m1MYDQ-7FmfN6P_m5qX8jiOHSEgkEEDIij_YJ86Q9MUMqCjQ0j64j0zxPm4z-Vnne11Ln26S3Uirygh0cJnMwZt5aVJ_FQ_gi-RSg0YpHxVEm-J7te0gdWd_Cj8a4M1Y1ZWvxKu5I3F1piLBFoY0oesda-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0d096897.mp4?token=JMDWimDMFf73soLK3zVLH99uzqOAJIqjM88dRulp_hga0IF4R_FsRDcSObrONeq-MwCG-leRzXAsVJlo4WvDi23fIKTmhffoCUYr44q_faTlzYnnA-DE93Jd-rcCHazHbHbc7kZdEq0_0Fnnn96w2xKiT1L1SSsST_hgqXwRMkCQHPf8n_LoX_I3Uw8m1MYDQ-7FmfN6P_m5qX8jiOHSEgkEEDIij_YJ86Q9MUMqCjQ0j64j0zxPm4z-Vnne11Ln26S3Uirygh0cJnMwZt5aVJ_FQ_gi-RSg0YpHxVEm-J7te0gdWd_Cj8a4M1Y1ZWvxKu5I3F1piLBFoY0oesda-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
🔹
وزارت امور خارجه یمن امروز شنبه در واکنش به جنایت امروز رژیم صهیونیستی در ضاحیه جنوب بیروت، تأکید کرد که تجاوز امروز، گواه جدیدی بر این است که رژیم غاصب، خطر واقعی برای امنیت و ثبات در منطقه و جهان…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/442178" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baq0hdXZRGvUzaKLnCSsQydRIbqIViG-hKzQUxWSVASsKWorEu1oRv9kZmrAwCKb-Kppm-ngVcI5pGxruLSU1jGCNyom9BHM1LdsP_eJEGeGAMtyoArXVVDf2LdL1DnpG_wuIbbcq-4J7gFP0NooEG-D9zJPGiXSVXjdzioFTO1kQ1-1aZz7RwAyWg9eqLhv2ak8gpN0AD2rk_3Prch3BoFlYK7ssEKovN9Hbx06Z-D66fLRqVKryCFvDmg1myz_ppPFV_hIueClURkeq0_5qpLZNlo5Rq3DjQgDCQryxopZ_v7z5XxUKYAzeDZoB-gBN3ZqpObovFTKqNVnTOnP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFVBwngFiNDS-lA3DKoxjsX1YNlJxnHf2T3fN8Z5oEaToi8j7uKaK3yo5R8rj534REmPTxMWvYbz0y0vxTKIoNNVUJDyoyA7AY6eBoEak3YtTXP10BD7TyOmlw-4K_uBLXzJ9nfs2pTXnx88DWeOPMyJuhn6WYTpOks81QvFJuKcrXL-qz6tEDaRiAnoY01xd42lnglV6PcevrPnLhhKT7p0-vwv2eijqaK5A40rEjb39QaMvxM9nFnB7NV1MCmcV6olmkOXDbrWf2pMuyOgfmp_fZAPqbe6HU0rjxub0_adDARWcAJBJDrQgIA6kUusjroDGZzo6wfsNa5LSd_3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6X3jxg0EbaHCvG8enuFJbT5qthxlRlVE3Km5Q_TRr-Ynawdekv0XNpy7oBT9hRYpVZiQWjTxHmYj29gLBNAaptyDPRST4YGa19qhvD-rWOB92xu6q96U6LIvCIKjR-0qbP1W0q_T7vaHI0P4XvMhIIsD5VIKQ692JxSUFb8xJzg-lDLfA6sTMg7tiJF79qkp1KMMixUbrEQErqFb5qRn4Vy2KrZyL-jzhZTUmZLotvouRehsybnUHhHJ0QuWWp09IkSNQOohErmE47tMGafveJLCTg0W6wZzuLIA-RgdkCRz5EDGRhUg2D0pj8i9SEl62svglMmAaSJzbwYvDUFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx4SppWdHTsIyj0X2uqTD48OOm5W_jjMad1Qp3ONs7kmakdLgND7iL3p3r1EREdw1Ppk7iPa5U6-t-Ssf1dtvcD3PDBopW7YrRKIfwbAb5gGITDO4ZsLgIIwjtn3ug7aLqbJmz_ag7xtgNmqAsvyVOXJLQ4P62hm9rUuskzKkRCWWwkIRFO3CZantvjfuygfxYFBrG2R8ute8EEa_Sh7AJgocpHikdDrVzWiFUD1HEVo8hEicY-kDb_-Y4tZuNnIiGT3EoYa5ReLHF47JMW5HR7i88kZYSt0kYhRq8KFANRApRyPdHrIXs9vcc5MU9xbTiDxW9BGRFxj8CshxCdY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pw9m_oNsvb7E_S7DJMsZUgR-BBrKI1PSN_WQyWuHQZco8HujUnEF9-huR7UjaWEA3ZIGvnH316-NCk9wh2xJWXN_UCF4QROd0SD9dfAKIs9tvJZ_5zvQmnK3nJcqWS4c-8MWw4IBX4rJSIRevL7cH8rzUCLo32g8hIiqq6Xvs-vUDP4-dQt1GQkkJMMAQs45gMaiV2rhcwF-lzboGR40EaJT9KfjkevpIkqAhCkxYhFuPO_-zlpT2j8NaPz6uaR1N86PCFoXHiW-eK09LvjmsB8EzPSm3AMfxTUNGF8qWUVAKkP4T62jBdplIxpXp4bzhY-Wh0WsWJaJkbfssVqXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItXn89iZepTMb6XG9jRgMVVHKbZb4QdPtV_gie1RCfy4gqsfp_R0xe8oilDjLNgq-EQR5WLkmO1m9_T-afAllq_AuWev47Rr76leNezS3alfYejD7M_8yZDGJl66cqLvYdhA4zqhXypxjX0CQHNFB3OxbZMseURxs51ik99hyi0U2mYJ4vHOoOI9WpaPD36muyLKF5qn0RqO8elBg6CotPP3LSpAelEb0k8_I2kCF7MCKmUv_Dt41SvIrDAXCu7LCgrahm9XL5moEfWM6X9DiMYEzqdWLJXUV5kLen3CXBsBLHsQ3qsk2NcT6A-JJ8O4aMc0cd8yXk56emaHmUX8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Juuo71Xc_3vWvUiv4rpmbq9fzrvhm-xZRYfqAOXlrCTctRicEljqrL3GiYQbFVBOELosFCpesoneihOsUUZrEeQhx1t0wcwUAikMax0YpbDOYrp0e-jCuilbVfeKKcgSuarnyZ8cw3A0xNag2PYrmT4xp-Tw6ZNKkLBq2XL7o8R7VB5ASL0xB3ZY79UZWaFX6tYdNDyVkKaHrnS4v-c6xrRrgiREaHz2jridUkDuE6h3WRdSER2xmALmz7AG3tjh9g82bzn_5mlvfW3J7Mn276AJOdFl8Z9zDto_EDPhUFpiT1KFFNA5nd7XmjDLOR_xD8KcOhJJZkaB0sayJnqVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPYZf6nIabZLYr6rNrSY5my1XJvKXpsYsMl0scqN_twpB325UbC7fC75m-vr9G3FowSKQGchqs5ARAhGijdl3nP59J5NkmZClXt4e4vxaIIDfJU5Drq4ZqUkEO0qL-nRvxdgzcAE3NL_qnsf5X_4Hbb1azYyu20x5Vv0_KaXbIaK7vi7a0YWKIzfjXu--V2DBswjviAi0uyJ9bn0rzbvD95d0ytQgMRIHOFePtmF-dQAJEb1pcRTL-ulbCyAsjp61zQ_sYiZ7-1gbQgWr9XVxZii5JSuVmNKK49BvkbNCfNML8w3U5dlPeU7XiX7zdlFcHbPTM_ADQfazQqCo75goQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra7oh0kqxi3wPBrBCzzx4Cc0VYJckzANLERpwKym9X3RdUFRWGA__khCojPlRL-VELCkHm8p7ee0EIA-eek4LGR-8tZPvW2Ky-uvxjEuHI9-MJRaanjCTIufccbSrTMFFnD9WIlVGvkfmgt0pH_-pWzKEv6CzrESu0XjccetJxZEuSFX1i5CAJ55mOjD2Z7iLXELb492QmHlzWkauZP-f1qMwsjr25c-YiRFg0glTIIgE-3bBM2WB11E0_Qv2Wh1b_w-T1qW_IZwLB_PQrA3G1FweyXzifknj0RtquMefMfTeTnum1T9ZJ1_Mgo3L3UTM3oWChoNtqwj2BkoZLmJxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های ماندگار به‌جا مانده از روزهای جنگ ۱۲ روزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/442169" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-text">❌
تکذیب برکناری سعید جلیلی به نقل از عظیم ابراهیم‌پور
✅
عظیم ابراهیم‌پور، شایعه منتشرشده در برخی کانال‌های مجازی مبنی بر نقل قولی از او درباره «اخراج سعید جلیلی از شورای عالی امنیت ملی» را تکذیب کرد.
عظیم ابراهیم‌پور در گفتگو با فارس:
✅
اولاً: بنده سردار سپاه نبوده و در کسوت بسیجی تا سال ۱۳۹۸ مسئول ستاد قرارگاه پیشرفت و آبادانی بوده‌ام و هم‌اکنون از خادمان ستاد جهاد تبیین هستم.
✅
ثانیاً: خبر منتسب‌شده به اینجانب درباره آقای دکتر جلیلی از اساس کذب است و چنین مسئله‌ای هیچ‌گاه مطرح نشده است.
⚠️
دشمنان و معاندین با طرح چنین شایعاتی در صدد ایجاد اختلاف میان نیروهای جبهه انقلاب هستند.
@Fals_News</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/442168" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXHfTTvy6vL_VBjcC-JxElHt0QtzLMMKm2S0GKdqqmzL_CymSNGuUreH1zxRc8DL-vLKrTLExmTxnQA2ruiQYHAl7fZgLE__9Txqy9zeEVhpHPi353oUruTqoR3wRG39XfJLCHNMhsGpEd0ldUGTtjLLgF1RmaD39PZevZAglPnRwEEA_EfYvzDODm8b21sjtVfnA1gxRuXYEIEM0TELvm6a-p3rdpONgt1oXHyxOesMcwemhCAXAHGr3nqnjFtEnaVE7GlxxMxmFQVGRwKMAhvM2d27IlQhysiaN1eOtfJ18Ntz_ylQOzhXqFT4hN50d1nRG6uwrlM3vTEGGfrzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی : ساعت صفر فرا رسیده و پرتابگرها درحال آماده‌شدن هستند
🔹
اگر آتش شیطنت در لبنان خاموش نشود، ۲ بازوی قدرتمند جغرافیا یعنی «هرمز و باب‌‌المندب» شاهرگ‌های اقتصادی‌تان را تا خفگی فشار خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/442167" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inNs8MXK4G_IqQ-dMobhUMySDeQKUJcM5hSPcJQGGrESawH1DVxOL9gKzTCqwFM4rEwB1PLWy0DJeG5p2GhG3xlgjkTRvJgDJ_cbIAeGHRLTzL9UslfQHWinQPiLuvBzkHJ3RxZP41daq_v8hvF1RMGFhLeBK-bW689uY8-b4G0DUHqwa__-xcIKdUazZilgXvCdvPEp0w1FM4DxM1jhdH_Beqmxis6MEp_98jpyhOSGdyv9DbsDg9Tn9DS1zlOkH9DgAMlNi1xtTvUHEqU6MLjsWdR_djSboRr1vbp8yH0z1LyVhR40pLFVbUN_YSYDQqZIlkAQ0e69r6bzI2AAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حسین شریعتمداری: اهانت به مسئولان، در شرایط حساس کنونی قابل توجیه نیست
🔹
بدیهی است که خود حضرت آقای شهیدمان نیز نقد منصفانه و خیرخواهانه را ضروری می‌دانستند چرا که اگر خطای مسئولان مورد نقد قرار نگیرد و درباره آن روشنگری نشود، خطر انحراف در پیش است.
🔗
متن کامل یادداشت را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442166" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b055d46b.mp4?token=OM9AuqYyQ26At0ZgIDuP0xAtY4HwDqiAy5JFGOlc7vPOjinFS_raUivRlOMs8TKZ_6IFCzCo18ILMbRnVqgZBsEe3HyNeDBHtVav5DDmZejcchk_2_nyWEw-wYHh2ybgo84pwgd4mhS_6YlFJNb97x_MchNnmTS6BhWiMGLPM7SuAJ51VpJzE2i00p56KXvuYE2TG7sdKEfSxjm16QsXY2J0g_WIwoLM4-o-07hQI22k40hVGN-U__ei3WicH6ooYdpV2VEh3etKeYQD7Ya_-pf6YXUTbDa-OMGrEazVd8Q9OYSCpSwmBoMQjaV0TxxZ6ph_1iH5fHnYr3MK7gLxRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b055d46b.mp4?token=OM9AuqYyQ26At0ZgIDuP0xAtY4HwDqiAy5JFGOlc7vPOjinFS_raUivRlOMs8TKZ_6IFCzCo18ILMbRnVqgZBsEe3HyNeDBHtVav5DDmZejcchk_2_nyWEw-wYHh2ybgo84pwgd4mhS_6YlFJNb97x_MchNnmTS6BhWiMGLPM7SuAJ51VpJzE2i00p56KXvuYE2TG7sdKEfSxjm16QsXY2J0g_WIwoLM4-o-07hQI22k40hVGN-U__ei3WicH6ooYdpV2VEh3etKeYQD7Ya_-pf6YXUTbDa-OMGrEazVd8Q9OYSCpSwmBoMQjaV0TxxZ6ph_1iH5fHnYr3MK7gLxRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۰۶ ایستادگی قمی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/442165" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbe4213e6.mp4?token=uFmk7OH6DdnqtezjFn3GvsItAiyPh9WtZMNlDfdjsCHWjQYUFJJJldUmF19VPeq4LzZ3XssKBnHRtNDbgAS57Bw1GMFaKZJSQ2MLCf8lCVqnwhr08IQ7ZVxe8PApVGpk7FMLBLR_U12s2p4JQhbaT2hE-OgybrAGsTzBwngDpOAVK2GsS0x7GQW62mHB_5Q-tqVOT0NU0FYj8l4RBbYz6_cV-tO7o6bMPDXlQ82PqNg8-tlD7SkudC5Zo7ypbo1geQPkL2S3dzFPcHpgKMnrCm0BqCyCIyCM9cRWLrgzksaZKbUewjnayAS0_xEzDsNb2u3JBDzNUPiKZLaQkVjs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbe4213e6.mp4?token=uFmk7OH6DdnqtezjFn3GvsItAiyPh9WtZMNlDfdjsCHWjQYUFJJJldUmF19VPeq4LzZ3XssKBnHRtNDbgAS57Bw1GMFaKZJSQ2MLCf8lCVqnwhr08IQ7ZVxe8PApVGpk7FMLBLR_U12s2p4JQhbaT2hE-OgybrAGsTzBwngDpOAVK2GsS0x7GQW62mHB_5Q-tqVOT0NU0FYj8l4RBbYz6_cV-tO7o6bMPDXlQ82PqNg8-tlD7SkudC5Zo7ypbo1geQPkL2S3dzFPcHpgKMnrCm0BqCyCIyCM9cRWLrgzksaZKbUewjnayAS0_xEzDsNb2u3JBDzNUPiKZLaQkVjs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۰۶ میدان‌داری مردم بندعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/442164" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El5sxq7c1zI2cSSSDKV0A338CuY19tw9LTaPtV4gnk1a3K2vweLU4HBW7VokHHU1KeZWNzhzdhanEX953QXjCTuxsjwyxdJpq2imkSyAKqFopiuZyKbd3Zl5BCdG4bl0GifVof0OdjYTihaU3pkJ417TGc8yunZvnri6291zJ4mR9XEaguBlJgN5JxvY-PeU_qLpkrIOv_H7zGbsPpnyxSVlVgLc_za-d0PWv9VM8JBH1npSIA4UrFYwqTiPNcMlvueYLYpXZiBqnY6ZxM5zsgYA6tBzlXPUrLAkWOIdqb0tlBsooYwvlPwp9cNwKiiJ4_f7JIFxIwaJRInQ_H4y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVNUDzA7Q44wx2VyuXIZnSAHfZLnRoorwHLKMrx2l7Qlrt5EYUh_B-TZ31edFUcgHsg9ZzmkOz0R8WUVCfn1_b6PZWVwStRNe-DFuRU3d7wsY6tiVxptCOyZTZfQ_1DgOsJ8xpB5XVR2UFCeLEDSQ8n2zT9ci-3oZb-hN0JKA-vqprx-84DCoAWh8GPwdnmSUmtHbkLk6AOsL0bWEoJXOV4L--wXBGSnMhSme5lHRxCxR3eEfbZLItVc64EmwjGm-IhIjXuFpQeLRxh-l0IAV-Gyr__EvCtEAi1SpZYT3VlH021FYud71cr65g2XSFgOgkqeA6nbQ2sRx15mXx7JBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULWNu0JeuR2XBcIsJy6KZ1O9n1YcRSpX7FY8zVX1IVqWrKL2MdVfSejk0R9f1y3oEl65RQlXy9Seh4WkGQxvUssQ2u8CWfD12Z1wjK-n3vQwI8KFU7p4UghF09hc2QUZdu81soiAVwxMEMq4JuMeIp-UY-qtNiCqr61NDf8cWoH6FQLZVS93qxbvGhDC3Sb_bGVgPc9qDrZIjMd8zKDuo-mqUtfdbW_FGF8Tm5QpteGj9AZej1IiMZYXcy9oYKlohNKeZh5QLEVBQ9-qBLJW1bY-sn1daYixekd1j8nQoW9It0pvmhZjrVB1yOPMBj3YNCvPZbqv27b9Dwu3oFfoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaLNwuzN_rL2XdjABWKXRH9IahBoOAFrw2v9x-8kqnnMBhZUPPS89mN2q9Eiqs2GC_24Qet3yALZkCvtiTuNV0QggPzXAGXiYyDdycPyfMIyW-O-Q8bsRAng90m9_qrpssKLDPhEgy_b6F97kGHU-uBgFSFcnzyJxwdHWidppzRH7qLALykSqSAFIzxbtq2Rt0KWEdg9NZq7ZrcTx5INani2SxmOXV7xBo24oDfTnIM3ZUDkqvjGCCOZxAyVeFRrj4eRGn8Ta4wEisq4GXJmKVCkBHdfJT5fwHjrZwP6xyoobyCe6-RHPsEJpeGExLoTaDQklineFYLCcVaMF5-80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAGFYxAqUBqBKLcSOH5N_dBpCu-u-OR86A5VkivZAhzN-Qs_-Ay8NwMVXfJgj6rEnbqK4gFpZ3p4-Q5_TilvcrLJ0tVtxURW32THeA6h3_1A-sSYiwPusDTWjosBWct051aboqlo9hIupT7-ctaRORd1q3RdeLLCYiqhmEJMEKYTF3-EpMgMlnGU_bkfRzFrFFCsmCmc7tIslSR-f-CTkszNRKlo94Wqr8MqVvhngo--wS-B4qd1FiP5O8TJ7mcY-rkVuFnK_gpEm0tiQlphiWfM72wy8hhgOHsM4_dmbybrEiADU9H_bp2rjKy4oTbLwoxFvLftSmDtFO02Clo8bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با فریاد ایران
🎥
بدرقه  تیم ملی فوتبال ایران به لس‌آنجلس توسط مکزیکی‌ها  @Sportfars</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/442159" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88aa74817e.mp4?token=ijx2oZwiWwnx0jpItnvb-chcEB_aHrsKcg70YujEn3S-G-pN09qd9gZ1V1sMgP0rmVtJrjO08bts32IUR60dovoIcB0ZzDRHtz8zr-9J8qX1KJ0ytT2eoD8ffGwO-QZljJwlfT7QFA2gNHXSNy1B4oq0l-f9epn7YsLGd_T8v3os2uorZjekV66iAI8JrANWR-S9uhLARbFBNMVkLKRqYSxYPl0a_cPSKV2sYVi2FeD0EEd-He0cQ31kfg_CYwMHmyYGlTwhGvJN8dZsRvDH02OjF1nMJjRUUbKhG-cjgboxHXK3a6HP3yRX-w-1eO2Rv2OfjDtIXU4EjWhm3EoQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88aa74817e.mp4?token=ijx2oZwiWwnx0jpItnvb-chcEB_aHrsKcg70YujEn3S-G-pN09qd9gZ1V1sMgP0rmVtJrjO08bts32IUR60dovoIcB0ZzDRHtz8zr-9J8qX1KJ0ytT2eoD8ffGwO-QZljJwlfT7QFA2gNHXSNy1B4oq0l-f9epn7YsLGd_T8v3os2uorZjekV66iAI8JrANWR-S9uhLARbFBNMVkLKRqYSxYPl0a_cPSKV2sYVi2FeD0EEd-He0cQ31kfg_CYwMHmyYGlTwhGvJN8dZsRvDH02OjF1nMJjRUUbKhG-cjgboxHXK3a6HP3yRX-w-1eO2Rv2OfjDtIXU4EjWhm3EoQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواظب باشید هنگام خرید لوازم خانگی کلاه سرتان نگذارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/442158" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf32fb4c1.mp4?token=um9bz7kVWfyKMnCT1V4cg2w34sZXA450vDDCSQgAZG2S60mBf1jPE-__NU5lyybm8MpIBvjqYLOJDHjhBsqfydo2NZWdV_L0OScRhjM2jJHp2z6YNMxwYG9ifFaYaEl7GoMN70Vx-bzPl6fZqDvsnnSCcuOC6CYS3D2k0gj59ndXdlqux6Yc6RIaChVw0GxgwLdxsLnXBUJ7wKQ_g27dQPpv5Kp0Gnn44TjCpGBuaLjf0vowZJLc-taD4ZfWci2bFL47LClZnn8-hH8HE2XKZoyQrAQf6uH4dF7NNI9Ee82bOTRK-IAw6yjxP_bPhUuyj6UF_RCFJ-p6ZaaVCWnfmX46LA7PFvAnvSBuMFlfyu3JKaGAITFYkTnGNCcZM1PfbrZxc2cAJ1efeehaJJy9g58MfJmZmAsQjb9O3EvvqsjLjVJyubm_UOA68C5Z6d5c1Jsf4MtVWgDcVsjtZS9gcIrmMvpm-jPGPgRulPAGHy4eUQ-D1MoPosZHZkA6jk51fEnRWvXc0DDrVYeBd7bwyXmTS-c9CX8T0Qsb81Mw-xjYG1_g6v2HKgcp2OwHcVIV4OR3HtW3R7m2pbiRZfe4WF-__WM5zHVZTY0bRPtHl8UMwFtCpBUJFdO-Wspihnv37g1kNZk6B3hfY4yg_WRbJKCMASy_-pxt2tILlrlgURY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf32fb4c1.mp4?token=um9bz7kVWfyKMnCT1V4cg2w34sZXA450vDDCSQgAZG2S60mBf1jPE-__NU5lyybm8MpIBvjqYLOJDHjhBsqfydo2NZWdV_L0OScRhjM2jJHp2z6YNMxwYG9ifFaYaEl7GoMN70Vx-bzPl6fZqDvsnnSCcuOC6CYS3D2k0gj59ndXdlqux6Yc6RIaChVw0GxgwLdxsLnXBUJ7wKQ_g27dQPpv5Kp0Gnn44TjCpGBuaLjf0vowZJLc-taD4ZfWci2bFL47LClZnn8-hH8HE2XKZoyQrAQf6uH4dF7NNI9Ee82bOTRK-IAw6yjxP_bPhUuyj6UF_RCFJ-p6ZaaVCWnfmX46LA7PFvAnvSBuMFlfyu3JKaGAITFYkTnGNCcZM1PfbrZxc2cAJ1efeehaJJy9g58MfJmZmAsQjb9O3EvvqsjLjVJyubm_UOA68C5Z6d5c1Jsf4MtVWgDcVsjtZS9gcIrmMvpm-jPGPgRulPAGHy4eUQ-D1MoPosZHZkA6jk51fEnRWvXc0DDrVYeBd7bwyXmTS-c9CX8T0Qsb81Mw-xjYG1_g6v2HKgcp2OwHcVIV4OR3HtW3R7m2pbiRZfe4WF-__WM5zHVZTY0bRPtHl8UMwFtCpBUJFdO-Wspihnv37g1kNZk6B3hfY4yg_WRbJKCMASy_-pxt2tILlrlgURY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت مردم بجنورد با امام امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/442157" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e105871c7.mp4?token=Z6dYavOJkv5chBcDxZqZFXlm5pBVSP2JYwwkT17FczyirjaCqCzH39MzG1Ux0oTeLDgqgQO4LAdXMvPOxUmh1ifzR4VNMzjr4coPGHdG2HEzqaWg7XOKdm8sP4AedYqdN1VqDzYtHBflmFYtQYpOCkDODbqslPhqeyo01c9TM0KrOrGxVe1K28So_mR-MmGI6L_BTnQns3e_qHmSe_vJMdWgZqb95_kWWu28b98hVS-G4sJZqCOfHLGFqMw6erKqrS8izJ-bAo5zgNVJQ1gGTuI7zze1ZmwVHOYJwwMtmUrHTjzn0ew5KMuhuhM6A2Y03D4wScEfJf3ElbfHYhVOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e105871c7.mp4?token=Z6dYavOJkv5chBcDxZqZFXlm5pBVSP2JYwwkT17FczyirjaCqCzH39MzG1Ux0oTeLDgqgQO4LAdXMvPOxUmh1ifzR4VNMzjr4coPGHdG2HEzqaWg7XOKdm8sP4AedYqdN1VqDzYtHBflmFYtQYpOCkDODbqslPhqeyo01c9TM0KrOrGxVe1K28So_mR-MmGI6L_BTnQns3e_qHmSe_vJMdWgZqb95_kWWu28b98hVS-G4sJZqCOfHLGFqMw6erKqrS8izJ-bAo5zgNVJQ1gGTuI7zze1ZmwVHOYJwwMtmUrHTjzn0ew5KMuhuhM6A2Y03D4wScEfJf3ElbfHYhVOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدی‌ها همچنان پای قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442156" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7mw3iuKbj3Zeo_q_ClcOeLOzy9106Cf3yCgU3WSm7rzpq_h5s5V_Y8qXXqt8nhUij2aa9r5lIyW17rOpu9SFLqrEMsw1F7I9OMC0JkcoxQ4dPO8Tl-e9iNCeZLEhO9QaGnSvkxTWnFgyHq-F6912CV90yXUkMZttSD9-eJDZPpQ_hYQG2Lbfr85CdTQqjN9komti2JCq6MBAsuNWnq-EndygOv2XOp1vthoojwQ7O5ip_Isan_yH2uAt6Fm1Y0xq5JlENutOmfitS9A_uHQNEJJkqj6weBtAJIwcJVs8HDCYyFaB-9fUoaNLlqgze3R4EQOEB0m8dUyZ6b4SmT3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه: پیامدهای آتش‌افروزی صهیونیست‌ها برعهده آمریکا و اسرائیل است
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442155" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محدودیت پروازی تکذیب شد
🔹
سخنگوی سازمان هواپیمایی کشور: هیچ نوتام جدیدی درباره محدودیت‌های پروازی در فضای هوایی کشور صادر نشده و امشب اصلا پروازی برنامه‌ریزی نشده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442154" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddbf1f2af.mp4?token=J4VDllwt7sZPehlx-TuUpWfvrF9DZxmIRWrKibr1O2TX9Q42UOB2CWbUZj2F20oU8yrYBk8vsEnwj-AIW8SBs74XYNp587lpihea5Nf5RJP5Su3vXFX2i13TdXDPdOLf7ZDoO4VEsC2qtYK4PpqVMORyuwM_ZzQeI-AAiC_L1Z9o9RDEFSmOFuProxBwudjgOYlHrAJnppc307q1P_1yYnpl8nnHYDv4BXOkTix2q8-gEC6u7JpEWPKgz4jAsQA8x358PW2H96eVRK0VAV6bwN3c1DK2rtKLrTwdacltv5B7H3ew7xHcGfHk2UPPiSVxfs8nSQ4bG20PZTOxWDQH_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddbf1f2af.mp4?token=J4VDllwt7sZPehlx-TuUpWfvrF9DZxmIRWrKibr1O2TX9Q42UOB2CWbUZj2F20oU8yrYBk8vsEnwj-AIW8SBs74XYNp587lpihea5Nf5RJP5Su3vXFX2i13TdXDPdOLf7ZDoO4VEsC2qtYK4PpqVMORyuwM_ZzQeI-AAiC_L1Z9o9RDEFSmOFuProxBwudjgOYlHrAJnppc307q1P_1yYnpl8nnHYDv4BXOkTix2q8-gEC6u7JpEWPKgz4jAsQA8x358PW2H96eVRK0VAV6bwN3c1DK2rtKLrTwdacltv5B7H3ew7xHcGfHk2UPPiSVxfs8nSQ4bG20PZTOxWDQH_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات‌یافته از نسل‌کشی، اولین گل استرالیا را در جام جهانی زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442153" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdqjh1xCeVU6I2x74-bijUwnmbFFIO58Pg40_GOOkF0kHGxwCGIlZB_SL3VLRv7Xx2eZC_xD-cao1CMHyOGFvy9CmeoIHcTx6rdqXUlMhTjGCiOpC59CaD1Wb0FQkc_BeF-xu5Gs07bGgU7efcta39CLT4_BFr5joZHsb-G-Xg_K03vrQplX4bkrQfdPzLPIT5uBt7AElzTUgM4kWKthcnzo0Fw1XwDNt3ELTBBYy0OQnriFOPhlRspEnA5c0XBozOKheMznCGe2ZAISkpQYeULxe1nV3H_58iJ4gOqfm3mybLvdaBT-Qb0cUugw9INMHPJ7UjSxkh8F25SzeGMtJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژرمن‌ها کوراسائو را تحقیر کردند
⚽️
آلمان ۷ - ۱ کوراسائو
#جام‌جهانی۲۰۲۶
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442152" target="_blank">📅 22:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a155cf709.mp4?token=IWwjQeN-4y1nZbUwlT-38rxqGxwNWuGffxBkEJuXVGpO0aIZwGsXSuSbqhxSyn8SqeyNUTlu2mWLsgpA-xAR0fIBIxw5Gt-DxcuAUh333UtjbXW72hqatb0YDLsqcJJwNRl3zYvGcH0sEil98j0ScHbB8Ja04PlMGnKjAhwOFCXPdtZWrGrud0bjh6--NEUeMZg1dNU5a_RMz0KAL0Upa44DbJnjmN5kF66G27eIrmZtgFvx8CbbVf-sUrAwMtcj0AuAR7yswKnX5GAzgCv1oSFpj3-NHEQBqwkKnYaWXSOGi9OFfcZNv40FEYJS4IwrwYelC4XLv77C0r2nVMxulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a155cf709.mp4?token=IWwjQeN-4y1nZbUwlT-38rxqGxwNWuGffxBkEJuXVGpO0aIZwGsXSuSbqhxSyn8SqeyNUTlu2mWLsgpA-xAR0fIBIxw5Gt-DxcuAUh333UtjbXW72hqatb0YDLsqcJJwNRl3zYvGcH0sEil98j0ScHbB8Ja04PlMGnKjAhwOFCXPdtZWrGrud0bjh6--NEUeMZg1dNU5a_RMz0KAL0Upa44DbJnjmN5kF66G27eIrmZtgFvx8CbbVf-sUrAwMtcj0AuAR7yswKnX5GAzgCv1oSFpj3-NHEQBqwkKnYaWXSOGi9OFfcZNv40FEYJS4IwrwYelC4XLv77C0r2nVMxulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۰۶ حضور دشمن‌شکن آبیکی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442150" target="_blank">📅 22:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxx6ozDV2An8YPSugLkJm8NldYSWVgqJVl_m9bfAIXfUJLYZg-yPY1LmjB_wNGxuUCp8Ov3IePziScQbVPbbOuzlHt8T2DITtOa1mLva-7ewZvAFujoerLspQWknvJtrtjZ4wp4l1_UPRVpv7GQQc2eH2TeixPaG1krbB6-Lw1oBijXPLJa4KsKIbgXeSan7tqjFuJEJEnhDVqi0ArpbAUas13yT8XmlyWCXkM7a9S1JsCeCc1MQ7W8T2OA3oESv0OAYr5u8upzcht7sRhM8_4SDu6q8Lrzx7-F3f0ctw49YYzP6WBBEcZ_7uYD6wN1OMDHLdtbKU9z97q0mS6uraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: پاسخ رزمندگان اسلام در پیش است
🔹
ذوالقدر: وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
🔹
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442149" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e401ab5a88.mp4?token=e5U8cGXkJSTLRb_qL8Ky7_7sjN7CuOaCZpCaQlYaxm_TjFEqjhsfsU0ROxjGr8HXNQv4CV9JoYUj54a-QwOY1L4ojr7rTxvmMER09CBTGJ08J1IofScf4723JMbruwJ2KuXjIT1lRWqwLfTIgBGIzlC8mkD7UEwS5Vib5LdaO1qRhsGK_o-xLl4VJB4ssQBlMj4Fd9KblLHSrwHKvJSoaXOyJoL_H3B_uKgoTQzgCxQE6FpfI8sjvGTIbitplgAVd2PUzKMlS6V_ARzSoP67-MzOgYVh--rlcyIIEYOE1vW9C3s-iseE0LikobAL7C0r69eGSEmRDkFfMgW_XPIKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e401ab5a88.mp4?token=e5U8cGXkJSTLRb_qL8Ky7_7sjN7CuOaCZpCaQlYaxm_TjFEqjhsfsU0ROxjGr8HXNQv4CV9JoYUj54a-QwOY1L4ojr7rTxvmMER09CBTGJ08J1IofScf4723JMbruwJ2KuXjIT1lRWqwLfTIgBGIzlC8mkD7UEwS5Vib5LdaO1qRhsGK_o-xLl4VJB4ssQBlMj4Fd9KblLHSrwHKvJSoaXOyJoL_H3B_uKgoTQzgCxQE6FpfI8sjvGTIbitplgAVd2PUzKMlS6V_ARzSoP67-MzOgYVh--rlcyIIEYOE1vW9C3s-iseE0LikobAL7C0r69eGSEmRDkFfMgW_XPIKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: قسم به آن مشت گره کرده پرچم زمین نمی‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442148" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f707aedfb7.mp4?token=QCG3DXlko4Vab0Vv1Nod5WuuacRDQPtooT-SAsAsq8krtP5kDzGlALzmCP3ncXPcQeIrh_7B2BplcxgDXu9sVwimyTic5wmYNARa4fmi_DKKB6l7ZgErtvlQ16VuCxJ1n358U-9sjn-D3Sm3AJElYyxN9xmBge-4uL7fcBPBGzqFYh1DToLvjBWk90BhL1ZLEC9kjil6T4dFE-LhZfzd3NmbQyzq6lTnZt-z3cbekrlcVto4XIRa04ELxVpUu-7lMeBZ8D4nJO4QweqLDKY7hsszm23cRNt3urX3n2DPN6U_RTZzaWnaZ6qaKceSTjkWOzVQ1bkzn3Jv97PEtOvSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f707aedfb7.mp4?token=QCG3DXlko4Vab0Vv1Nod5WuuacRDQPtooT-SAsAsq8krtP5kDzGlALzmCP3ncXPcQeIrh_7B2BplcxgDXu9sVwimyTic5wmYNARa4fmi_DKKB6l7ZgErtvlQ16VuCxJ1n358U-9sjn-D3Sm3AJElYyxN9xmBge-4uL7fcBPBGzqFYh1DToLvjBWk90BhL1ZLEC9kjil6T4dFE-LhZfzd3NmbQyzq6lTnZt-z3cbekrlcVto4XIRa04ELxVpUu-7lMeBZ8D4nJO4QweqLDKY7hsszm23cRNt3urX3n2DPN6U_RTZzaWnaZ6qaKceSTjkWOzVQ1bkzn3Jv97PEtOvSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی مرگبار و سقوط ۲ بالگرد در برزیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442146" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b40936e07.mp4?token=Zv_-DCspf6fCzTJd8B78w-3AgiKsJzxDnfJWcbzRBTbUAT3XOS0T5tPTRcwmzZiQicz6hlzv88BXpTkXiTOTgQFeMYGMxxh6LQ6dw4Y9xBtSqZU-XDnyseQZONUq2z-Y2l9U4rLRZ7bSCC8uXxgXYjxgs8bIFmZEc8WAE8jPw_rFlAVEe9-5SpVEMugmz4IHJ1UeaEPK2TBkCgleap8viIBEcqyxPoYGnNHjbX9lZ8vkS85hZZh-zVZEa032CPkPUNadaqZZvnEhJAcX0y4EM--akFZLOhCsfYr3tUDklNdNIpWhGexRHgchen6F5-dpzX55Bvtahna59vaT7v1_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b40936e07.mp4?token=Zv_-DCspf6fCzTJd8B78w-3AgiKsJzxDnfJWcbzRBTbUAT3XOS0T5tPTRcwmzZiQicz6hlzv88BXpTkXiTOTgQFeMYGMxxh6LQ6dw4Y9xBtSqZU-XDnyseQZONUq2z-Y2l9U4rLRZ7bSCC8uXxgXYjxgs8bIFmZEc8WAE8jPw_rFlAVEe9-5SpVEMugmz4IHJ1UeaEPK2TBkCgleap8viIBEcqyxPoYGnNHjbX9lZ8vkS85hZZh-zVZEa032CPkPUNadaqZZvnEhJAcX0y4EM--akFZLOhCsfYr3tUDklNdNIpWhGexRHgchen6F5-dpzX55Bvtahna59vaT7v1_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا خانم‌ها برای اهدای خون محدودیت دارند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442145" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">با فریاد ایران
🎥
بدرقه  تیم ملی فوتبال ایران به لس‌آنجلس توسط مکزیکی‌ها
@Sportfars</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442144" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afa7a9107.mp4?token=Y0i8Ya451X_uhUVhpOW0B6QfOlwiXRuE7IPFmJMgrdNlOufr_Q7UfmOMIYF7YwZIiQJVZAOQDKT3WB7z2aSzrHfAiZkEPnSqTDBl7PeVOPrHDhFMnr1TKIlepY48EzVCTh_odA2eYn6loIiJkyDpL7O6gaBAy2pWs0lQOB42DOalHtz5Z5fe16GlTBfvEbtUrrqgw2ZcI7dE2r8x-z1EYaAm3h-FmbrhI1Fzr_F8LHfBHzI3O0jwSkBomO_cFNPuPz0r6uZ8Qq_jRV5iUQSexNefgPU7-xifgwAH9piD6gJ1Ktsg8i6Q5KFnFcVWr0DMQ9FCVhcCjSSLHY3Je26UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afa7a9107.mp4?token=Y0i8Ya451X_uhUVhpOW0B6QfOlwiXRuE7IPFmJMgrdNlOufr_Q7UfmOMIYF7YwZIiQJVZAOQDKT3WB7z2aSzrHfAiZkEPnSqTDBl7PeVOPrHDhFMnr1TKIlepY48EzVCTh_odA2eYn6loIiJkyDpL7O6gaBAy2pWs0lQOB42DOalHtz5Z5fe16GlTBfvEbtUrrqgw2ZcI7dE2r8x-z1EYaAm3h-FmbrhI1Fzr_F8LHfBHzI3O0jwSkBomO_cFNPuPz0r6uZ8Qq_jRV5iUQSexNefgPU7-xifgwAH9piD6gJ1Ktsg8i6Q5KFnFcVWr0DMQ9FCVhcCjSSLHY3Je26UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای دین گنابادی‌ها به مجاهدان انقلاب در شب صدوششم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442143" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e45b95dfe.mp4?token=LS7xBFDDLdt5uZ5EfJVP9lT2lWnhfWyWLhjG_oQVW43P5ZrsJEHiV0JC6Qb00kWWHh-CA8c4B-1VQl4bCjHZ3tVq_KyBVjVxij1-oK9CEr5t4suDgJt3sP2yvnjiiyaiAkmBcqFgTgqij1zw3sPI-O8FaurWRPor1w0wM4yC2BrWv4jNMkn2h3sKQRkqP0sZdCWNdeh_eE7HAoXhPUBVvz32WtN-rcgQBomLT12Du2ZSoDY9AN-vRondBte4cEHUKqDaGTi11ex__3hBsw3fbUjduVr1efWUTuuQ-LJKcULpE5G0SSL0Lr5EIV-ePgKItgGSSvnYGkjYp7x2qBb_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e45b95dfe.mp4?token=LS7xBFDDLdt5uZ5EfJVP9lT2lWnhfWyWLhjG_oQVW43P5ZrsJEHiV0JC6Qb00kWWHh-CA8c4B-1VQl4bCjHZ3tVq_KyBVjVxij1-oK9CEr5t4suDgJt3sP2yvnjiiyaiAkmBcqFgTgqij1zw3sPI-O8FaurWRPor1w0wM4yC2BrWv4jNMkn2h3sKQRkqP0sZdCWNdeh_eE7HAoXhPUBVvz32WtN-rcgQBomLT12Du2ZSoDY9AN-vRondBte4cEHUKqDaGTi11ex__3hBsw3fbUjduVr1efWUTuuQ-LJKcULpE5G0SSL0Lr5EIV-ePgKItgGSSvnYGkjYp7x2qBb_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار هواپیما در آمریکا
🔹
در پی سقوط هواپیما در ایالت میزوری، ۱۲ نفر جان خود را از دست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442142" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51f6432ac.mp4?token=HRgLJBxWz2nPNJCokv7GuCdVucNwcheOkAiZ0TuCcOvQelDMf-Chf9aWb841zM0aSO458NLumsZTJ49nOBWmuo90fz8ZzpgneT3z1oWIm5HUPfhGRnajxuQ0K-rZX_aaaGIArKAn6j3yK_gb16zivt8vVwg1ZppA_q1Znn_gPd-3ET0J5TXY8MOCT-UVVeTAwVn0xG0rHrAQTYPF1NMsR6corYy6G5IKcwNQvm7AOhyE_xh-EKcjNT3HcWytsQQ1RXqET1sfnRFUtkPJKSQVe4F7DkQ2Jv-WtfmKH9KMofbRevYty8w_HtpgBlYLzeXTUPLxoaJpWB4MeKiN40LCAyj_Cq8Wtn2rO9M9JH4zqwwQKU1qJKDbAypmLUO_IpwuEML54zFqNeWtr8JTP4YU9UJSTanVHLp6idocTC3hUjy50nTWr-ryczjYGREo7Uv2OkZtz6-ISi8xP4ZsYg-MYXNUPb2vSZQ-JtySpdSUzwITIp-jEBAof84_jM5CubiJWByGblas1TiJUNZj5mt2Mi1wGiuGWALhQB4SXWpFDn9TZJZCjzIpgjSrua-1WHgjMFJglhjuWciYy2XRDAfk43KFtLIKFa27e8kwwxITTJD3uc_TurU6h-t_q3Mv4vUarTldo7Kg-d3IW9Tmu1VLhP0sMMQz2kDmzRO2QEugLF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51f6432ac.mp4?token=HRgLJBxWz2nPNJCokv7GuCdVucNwcheOkAiZ0TuCcOvQelDMf-Chf9aWb841zM0aSO458NLumsZTJ49nOBWmuo90fz8ZzpgneT3z1oWIm5HUPfhGRnajxuQ0K-rZX_aaaGIArKAn6j3yK_gb16zivt8vVwg1ZppA_q1Znn_gPd-3ET0J5TXY8MOCT-UVVeTAwVn0xG0rHrAQTYPF1NMsR6corYy6G5IKcwNQvm7AOhyE_xh-EKcjNT3HcWytsQQ1RXqET1sfnRFUtkPJKSQVe4F7DkQ2Jv-WtfmKH9KMofbRevYty8w_HtpgBlYLzeXTUPLxoaJpWB4MeKiN40LCAyj_Cq8Wtn2rO9M9JH4zqwwQKU1qJKDbAypmLUO_IpwuEML54zFqNeWtr8JTP4YU9UJSTanVHLp6idocTC3hUjy50nTWr-ryczjYGREo7Uv2OkZtz6-ISi8xP4ZsYg-MYXNUPb2vSZQ-JtySpdSUzwITIp-jEBAof84_jM5CubiJWByGblas1TiJUNZj5mt2Mi1wGiuGWALhQB4SXWpFDn9TZJZCjzIpgjSrua-1WHgjMFJglhjuWciYy2XRDAfk43KFtLIKFa27e8kwwxITTJD3uc_TurU6h-t_q3Mv4vUarTldo7Kg-d3IW9Tmu1VLhP0sMMQz2kDmzRO2QEugLF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بسطام: ما ملت حسینیم، ذلت نمی‌پذیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442141" target="_blank">📅 22:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
گروه هکری حنظله: طی چند ساعت آینده، غرش آتش‌های سریع و سهمگین به مکان‌های تازه‌شناسایی‌شده توسط حنظله در آسمان تاریک سرزمین‌های اشغالی خواهد رسید.
🔹
فوراً به پناهگاه‌ها بروید. چه‌بسا هنگام فرار نیز حوادث دیگری رخ دهد.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442140" target="_blank">📅 22:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ce3b0a1c.mp4?token=fVHm5wOoSiTk3TjRB7hUp2swlj4dyzx-mJ24qM48ZBgsM24gf7lRusX7jMt7IdUJW1X3W1N4-6qKNTAHab9Out5TlnoS3gLF4DJ3VQJA8J16h1rxtMoU9pUMjRzy8Pn3U8WvSIYviV-Q4F2IZEQeGOBf324vYoVi2Qqq532YzfEpdHJnnkr3hoqTgmXqV1WQVLcFhzHtEl1IzNkSvZsmadBariUYubOe2WqjuokxCvBysuA9MeIjXZLe3XXH3aQ7_UmgIKUXe0jscMTWWkWtpFTWtSv4pmiTHAD17Kwdoink_z7TTriyz8c5LfIP7Ew4MeL7WKlPHlZeGQAyk7GWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ce3b0a1c.mp4?token=fVHm5wOoSiTk3TjRB7hUp2swlj4dyzx-mJ24qM48ZBgsM24gf7lRusX7jMt7IdUJW1X3W1N4-6qKNTAHab9Out5TlnoS3gLF4DJ3VQJA8J16h1rxtMoU9pUMjRzy8Pn3U8WvSIYviV-Q4F2IZEQeGOBf324vYoVi2Qqq532YzfEpdHJnnkr3hoqTgmXqV1WQVLcFhzHtEl1IzNkSvZsmadBariUYubOe2WqjuokxCvBysuA9MeIjXZLe3XXH3aQ7_UmgIKUXe0jscMTWWkWtpFTWtSv4pmiTHAD17Kwdoink_z7TTriyz8c5LfIP7Ew4MeL7WKlPHlZeGQAyk7GWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرصتی برای تثبیت یک معادله در برابر آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442139" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJim-X4hSbOzb0a68IdHKYPKTyxn8QmeFWJ3g4wyRJaunBGY6pP8pUkeuYl_gFIsfuLMdJAqsxKPZdVJkp3P40-7w54MBcVot_XT-qjvMBZINQIrujiGfMGBe7khbWy8fOe20VBrBGEtMpPvAc8qyC6swvUSRxAi6-_5vqk4rCQcKGPN8CdztXwU6kUdsgKJ4kxV7ME7_WIhZouy9JUxvc6ZfFO6ZD0xmnjpbmzp12sQZ8iX3mzyCzCbrEw86zCETlNAPGAUHilWJ0fV3ZQPTcO7pZe3nrY-zlLGIepwLr9Sb0mYrbGQZJYxUKyWtFRyGpJON-mFnlcU9h-PVeLSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0HRQskC2g1LxgB4FnO4g5KyXSfLGzGJEFzgY5Fp2QhOOEdySOB_G9A8vxsM2gs-YxtMyIC9jM9EWrO86nXRWJj-mbWgwll1AbU-M6ElDwV4ktz8VIITwBQQR13tHtcFBjyIiKrKpzkKoF6D6NICBAbvbA6c9NWACNqn6nu2NSb4b9EM0aMHw40JMb_rL1CzjYii5ORjmMOCB_sxYEKpPnOXI0ZfODd0Sue_Wdb83YEeizT__rXBhADnjnGXUqZF-u4KbQmVoie1k5LHEhGRt2IHo97yW0CWVTifxm1fD9OCftjtEc8GQ_Bi5iGSJHOGLSU4_qNJem1qshefY0zcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3xKg1UPGudnsdvlp4x26_XdjMVTIO83Fj-FPosPTjLyqBH5pA33VlJAJ1OhS7Kf-VLnJtpevVbsLKlzy3o00QQDKK8y1m6bIGGpirz0eenodO9SjZ2Xu072I03hPt9PSwXwKRWuGcEGsSAGClwfYPCD8K139E5JfWtecBtlTf-RP_QQh9XTercLEb9ec2vTa6yLIA4jOo3HHH_KWIzDV9Q9qaeK0eTeJ4TtrcSJURKyAUC_CVbOkZVAsghTkFCwvYrQ3DYcTPMKtA0a9DlNWlIJl_g29VPTZdfNlbun3hi8k6tic9jzLUN8y90F46r41zAvON88WqjiXyIU0gZJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HT97QrsB9dNF85l0gOCeFPVn22-YyMIBhO7dRO6Lkqyjbmjmdr_kooRetQOaDTduXmsDBTPYsSzVoG-6ZBTvcUJHuUJVGbqi6O4SNpildIzf1Tx4La9NH85pMwDwWbXiYWDqAWre2nmSodOC_CrQDFYYu-_zwD0p3nB_nJW9rHz8hb5at9tjM0hOiPB8scBZW0n1FCMEf1ndM9BhuJ1ogh_jYCxwAQUFoySLTq36vAxf3KQKJRcFhuoHfMTR0H5WpdGf2tMaF95j8DGrkDafW4ze48ahzx1o4Gr6ByGWy2DrW14f1DC-RHwUxeUSOR8NIhUoZCNaO50MUMPfTn_4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYVFHJX9WgztKVDjGdlX-jVQnOV8Tx6QWVDm4EDDqT2vUv21iwVl027JMzR9HVLUY2jTRixwTc47Jz5Uok5432d58fx8_uxQl1GBnKHZE79AWzkdHbL0EH7QbFQJUSHcQFejJyz1vHYISYj-JdnP6jHSrimGBwHxw0YKxtsbXl-IjNZ2QLfeEDjfeQhaFMykKqFQqK_CkKN569b4a4-BYLt7-uuRzDIbcahnjUNrSkC65B9SYCq6bJ31iHmh-9bHRXI3HFhELguGUchVNGBitk7dI_pTX26T63RAiz5t4PAWyJ7uWQ9_iUFMZ-nZZZ-M7ffutw1OiBym-iSWku98nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از کتاب‌‌های زندگی فرماندهان شهید هوافضا
🔹
به‌مناسبت فرارسیدن سالگرد جنگ ۱۲ روزه، از مجموعه کتاب‌های «آسمان‌دارها» با موضوع زندگی سردار شهید امیرعلی حاجی‌زاده، محمود باقری، داوود شیخیان و محمدباقر طاهرپور رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442134" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWtPVzusp42VqYl-RvgnK7DLRZQ01EFM08T4jlrU3uhOZdmw2I27CTn9NrFxtf1IG55aBq91V-Cies8lQvU5jU49DwtCpeh_u6R3eBIriP1CO6smcT2lJKrZsTj_Le7uuzN_7f4bmTIWLeKFTCRrSYe-bnPhXMV51qEB1jEtNTvV5XawqMNNHISP8mD9A1uDMZOfRh0WEwCdEe0C3Q5vWWNzen7NIUw8E947p6czcDoTTbsombKejpXmaOO4O-6KUdDAYAJuBLmDruEj9TncDdt13o7IZFlBmCRiBqfGjGL2L1hM3GZTXQkKmFqG822cX9GhV6zBacPfb6COzH5hJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: پیروزی مقاومت عظیم حزب‌الله در راه است
🔹
مردم دنیا، استقلال لبنان را با عظمت فداکاری حزب الله می‌شناسند نه با وابستگی بعضی حکمرانان.
🔹
همهٔ دنیا با چشمان بازتر نگاه کنند؛ پیروزی مقاومت عظیم حزب الله قهرمان بر پست‌فطرتان صهیونیست در راه است. ان‌شاءالله
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/442133" target="_blank">📅 21:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr3wfyUviT0QgjXuSP47fZnxOa6Q3zt4TVCJtOBc9qWwaQo9JXFuui6lRz9Kh-HFsEb5y01v4IHnLhSjOVy99zOyT1EJ2AJY-4HGjUnGvancMuMF9_l1qNnb684f2lLwIA-qtXieOoUF0rNA9OIBys7uwhB1zICQrqAu9darDYCMqHQX3xNYRxuo3chP1orpwi_D1k0YXYmST-yVvkp_x5f9ZkTuMJdDfUPjec6iFhP8HoSLNSEPD0hJsv7EVrJpTVwcBciZTLQt8OBPVninqWbmZNwTuBvf1iFRR0E23oso4aQ6tCZFSahD46HGgH-uGQoRUCMd8MkBEKNR0ETa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
🔹
وزارت امور خارجه یمن امروز شنبه در واکنش به جنایت امروز رژیم صهیونیستی در ضاحیه جنوب بیروت، تأکید کرد که تجاوز امروز، گواه جدیدی بر این است که رژیم غاصب، خطر واقعی برای امنیت و ثبات در منطقه و جهان به شمار می‌رود.
🔹
صنعا در ادامه گفت: در حالی که دشمن از امضای تفاهم‌نامه‌ای شامل توقف حملات در همه جبهه‌ها از جمله لبنان سخن می‌گوید، رژیم صهیونیستی بیروت، را هدف قرار داد تا معادله تجاوز افسارگسیخته را که پس از امضای توافق آتش‌بس در غزه در پیش گرفته بود، تحمیل کند.
🔹
صنعا با بیان اینکه نتانیاهو نمی‌تواند بدون چراغ سبز آمریکا دست به هیچ حماقتی بزند، خاطرنشان کرد: تنش‌زایی نظامی صهیونیست‌ها در دوره اخیر تنها به لبنان محدود نمی‌شود، بلکه غزه، کرانه باختری و سوریه را نیز در بر می‌گیرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442132" target="_blank">📅 21:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqEfkZQnpXkMDFKeaGQijW4IXzFH9Aw4fhcLbxi5k6cAqs5vIPwp8A6B16VY_Ldep-4hFLPswkZhm-P0ZuuYKDhk2Rw5vXJ6EUfDnak0zZVUHZI1de-vj_tbbq-ppok8Pbsu_5-vASoIA3GIcY5GqIbMokwNKJPgBQZLuNvZKtiXmOUnMx3Pq7cc_ltkU1MzQ-luoiUk2WQ0k_pN1DDnDKoyN-UtnTEqOT7sdojkumrR8b77VJh_Kl2-idhgX2XLg1cT5e35_RwnSoy77REIhcs7ZsIirbJr2oy288r3cygxkbbH41aBmK6z7rtCU96YqcEiWs-YaLFpD--Vcapm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۵۸ کیلوگرم موادمخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: ۱۲۸ کیلوگرم تریاک و ۱۳۰ کیلوگرم کشف و ۱۲ نفر از سوداگران دستگیر شدند.
🔹
۲ اسلحه کلاشینکف به همراه ۹ خشاب، ۲۹۶ فشنگ جنگی، یک دستگاه استارلینگ و ۹ خودرو نیز از متهمان توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/442131" target="_blank">📅 21:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازی‌ای که برای ترور کردن ساخته شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442130" target="_blank">📅 21:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzArSgkzJ946fsC9_EDloYmlBSiTwNmv6rxBZO6im9ejEqU7l7rbVumuUZq7aB0SnxsncPwt8P7pW_RtO1JVPE5NfkSc0PWYE7N2Yg8Tj1y1W41EuT-WfzNEBNZK1fgYhRjKhABmI35pmmPeGMv21PLD6uGV6a5tklPkxVgD7KnYSw9msr7_axYutRm6enjYAunmDS5QWzbMwsvtEW67x_tmZCPvckpMJbtFaz0S5LSGw8T8t-e1k4_fwjKCEnZabHTH2f3fTrYEfmA9GLuB0Yn8OtWeNLsi47piMI8jz9P70-AdkzewUWZ5AW4eNl2Z4Db9dJKRWeLEWE1qYPYN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: پاسخ رزمندگان اسلام در پیش است
🔹
ذوالقدر: وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
🔹
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/442127" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6wced02vbh2m77pGrIyCvGIwru9FLnLNhudFDNyuKZ-BYA0ObQbB9_juiwHNAM1-9pS4Xah2NLPGH48g5rnWCkomuVEYdGFWyvei1BniIkng3dCIoz6JPdGqaDj7ZeF35fRGCJhRcan4uN0u2asO3UgxDQExXXwzdSlwfWG_giTahyHP91X9UOwnSr0g_vdcF6v1B1O_r_Pb_ZhfFdvWl9TteEiyEl75FoPTV2phwZYRAZ3xVuG8hF8auvxFOZX4kwgjHlHkyheeW8f_TSiHhk_FCU7yYH6CUv-pOYx7yXthnQPQrkOQ2TgGf0LskOiUVqPHfrRiQgXbObbFn6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر روابط عمومی شرکت خدمات انفورماتیک: سیستم کارت‌خوان بانک ملی تا ساعات آینده فعال می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442126" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442125">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442125" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
امروز به‌صورت همزمان گروه‌های سرود جان‌فدای ایران، به‌طور نمادین سپر انسانی در اطراف زیرساخت‌ها تشکیل دادند.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442124" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442123" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442122" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3o6BuduX72mYvYnYEnO44a5dU4axRfJ2m_en5jt8Gzhn0c_oC2vrdloQ18rToY7j5nwFmBBTfCoeJNspevRajQtGWOpn7s-lBkeZCG1F9CYPYqKnbv1-V-JSvXdWA69gTfHlNZ4D7is9dyZWTL29crjRIFH6SAVg3Wh0eBlBbpO-cYkEjoedaiJr_elz5iqAGdWjEaVtCCudZ5M4DQnZphFJvr6Xxxz9Ecah5ihlh8rdzb097-PgKBVZpgJ8YFb9e9GZD9jFEnbrape747-1_zhttd1o5keXDNJm8QHVDWvyv97QYQUCwwexzVADg80YqI5677UFCjM1-FJAY9UpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ9aVNk_-5wefvNglk3tZZPCDtqewLS_8-CI3JFDAhwaMQFtfqo_eDXS1H4CbSTHGoPsk64MUV-XHS9sc0nTm2xbwy2BQ8C0INeeJNhTV-73jricVrdtatIrECZ8meXEfpoVQT1q120jyWAhtJhq8jHSvb6lly5Z98fk38m7ILU-d5dlv1jf_oWmM9_BS6EsGP8168jSgBv_ihLBlUFjc3tefbiP6KH7JDXHcoiA_1_-nxQC1rUQdNlSMM504lMY84jqeUpvFiTXxMEwgNcCtYIShzgy6QMvqqsL71qdVVJYyCLthrR7XvfAew1roTJ1KNIgjuflCFhrtfx7Kgs6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofbSOlNqDrb0I5nUmy1X8sR5pSVXzZrMPMwT-4r_WFSuYIjpPml7mjFTFizIVCKEisLYpArVRFBbMDLTfkqEr39Q7DqgdHXRsQTEDsMUhuWks9PgpvZbUuI7OxYbkm71g-7BPeLnq99MO-HuqShJtpXTetmS0v4QonGzL-Gx4Nxz0tRYVJnu7qPxsnSsE3FDUMzw1Hv5iDfE6a9SAUQHNcE_2_-jLlb_1RG2Ip0bt33ByPMCfcP7fW-a0BHgjpItK9ooeIp3DjSerHnrGr2zSUbxZomhAL9NHgS2ctpxJRgQ-QFDFUkSYgTN2jayZnSdlkXg-dLlmZNCAZjWAymVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDn7PusdF1D6pVGCQgKGfpqPMOaeI9X4LoE0HKBM4BJQ5XnXCMlO2RWlO8O7cQJIlRS3LnTS6kTuNymo6PdSNDbYTyNZcCwlRpdmnUni7uyeGGJGyYZk-YwYd6eC3l0sU_T5ZU6ugTBK4zF3h4yq8MeWQdWdoyJemwywMwp5YdfDBgKvqezXEvB0S0CXRMc8qRpRjZjAWFr6oUwHG4QzPQRduccpKJLpLVwJ_j8sl38-2ZUm3e83T8trzzGpwcorNqftdoqUlAInLixzkjqq99fgi0e2-FkSruNJQ31nTh0pRJ4jYt5Sw_oQV37lxaLZKbpwKMrFPNGgoiQJwXbGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیاء: فرزندان ملت دست به ماشه آماده شلیک به قلب دشمن هستند
ملت قهرمان ایران
🔹
مقاومت و بعثت دوباره شما، فصل نوینی را در تحولات بین‌الملل رقم زد و جمهوری اسلامی ایران را در قامت یک «قدرت جهانی اثرگذار» تثبیت کرد. فرزندان شما در نیروهای مسلح، به‌ویژه فرماندهان شهید که تربیت‌یافتگان اصیل مکتب امام خمینی (ره) و امام خامنه‌ای شهید بودند، از روز اول نهضت، بغض و عدوات با استکبار و صهیونیسم را جزئی جدانشدنی از ماهیت انقلاب اسلامی می‌دانستند و می‌دانند.
🔹
اتفاقات یک سال اخیر، از جنگ ۱۲ روزه تا «جنگ رمضان»، علیرغم خسارت‌های سنگین و داغِ جانسوزِ شهادت امام شهید، فرماندهان و مردم بی‌گناه، یک فرصت بزرگ برای «تسویه حساب تاريخی» با جنایتکاران فراهم کرد؛ نیرو‌های مسلح به پشتوانه‌ی مردم و با عنایت الهی بر سر آن‌ها آوردند آنچه لایقشان بود.
🔹
توان رزمی، دفاعی و قدرت موشکی، دریایی، پهپادی و پدافند هوایی ما پرقدرت‌تر از گذشته و تحت اوامر فرماندهی معظم کل قوا حضرت آیت‌الله ‌سید مجتبی حسینی خامنه‌ای مدظله‌العالی، ارتقا یافته و فرزندان ملت در نیروهای مسلح «دست به ماشه»، آماده شلیک به قلب دشمن هستند.
🔹
آرمان مقدس فتح قدس و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزشی از سوی دشمن متجاوز هستیم تا درسی فراموش‌نشدنی و پایان‌بخش به آن‌ها بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442118" target="_blank">📅 20:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای ترامپ کیک تولد گرفتیم!
واکنش مردم را ببینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442117" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex9LI-gOF9VVxkNY39vVF13B1CT17dsdTNP_X0fTHwvwbSE1mlh7k87HUZcyvlm7I4PCYHezc7aDMnDqxL4wNgl78EMpbBLrxTQeZ7T-SBqSLdW098DQOkivd7UgJD4ZtVaKUhTdJjkIg-2Pl4bhSNjDhgHMc5f8dnFhjy5DReK5efwn-smeACO9gUrILpzfgXgB83kCLUEQFs8zbJx6rK_0NupKsNO5Ptb5zaP2ACuOYbffTCtn6cTSbR8Tanmlhq_VivleLAlOi91lElHVsb_RcPHK4SnYnzSsQeUIeDQ_8UCfXqR4aebfJJysEvuYdfOKFgqlYohKEUpgRXHRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبک شاگردان پیاتزا تکمیل نشد
خطاهای فردی کار دست ملی‌پوشان والیبال داد
🏐
لیگ ملت‌های والیبال
ایران ۲ - ۳ بلژیک
🇮🇷
ایران: ۲۳ | ۲۲ |۲۵ |۲۵ |۱۲
🇧🇪
بلژیک: ۲۵ | ۲۵ |۲۳ |۱۷ |۱۵
@Sportfars</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442116" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442115">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442115" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442114">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ دندان‌شکن سفارت ایران در کنیا به سنتکام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442114" target="_blank">📅 20:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442113">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
پزشکیان: هیچ فرد یا جریانی نباید خود را فراتر از سازوکارهای رسمی تصمیم‌گیری بداند. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442113" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442112">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
پزشکیان: برای من پذیرفتنی نیست که در جایگاه مسئولیت قرار داشته باشم اما بخشی از مردم با مشکلات معیشتی جدی مواجه باشند و شب را با شکم گرسنه به صبح برسانند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442112" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442111">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
پزشکیان: رسانۀ ملی درحالی بیانات رهبری شهید در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی «نه جنگ، نه صلح» گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442111" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442110">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
پزشکیان:  تصمیم‌گیری درباره جنگ و مذاکره برعهده شورای‌عالی امنیت ملی است
🔹
در این شورا نمایندگان تمامی ارکان حاکمیت از جمله رهبری عالی‌قدر حضور دارند و سیاست‌های کلان باید از آن مسیر ابلاغ شود.
🔹
نمی‌توان خواسته‌ها و برداشت‌های شخصی را به عنوان مطالبه…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442110" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442109">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
پزشکیان: کسانی که خود را مدافع ولایت و رهبری می‌دانند، بیش از دیگران باید به سیاست‌ها، چارچوب‌ها و تصمیمات رسمی کشور پایبند باشند. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442109" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
پزشکیان: در بسیاری از موارد، ملاحظات بنده معطوف به آن است که مبادا موضعی برخلاف نگاه و سیاست‌های رهبر معظم انقلاب تلقی شود و به وحدت کشور لطمه وارد کند. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442108" target="_blank">📅 19:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
پزشکیان: انتظار می‌رود رسانۀ ملی منعکس‌کننده سیاست‌ها و رویکردهای مراجع رسمی تصمیم‌گیری کشور باشد
🔹
آنچه گاها در رسانه ملی درباره جنگ و مذاکره مطرح می‌شود، لزوماً بازتاب‌دهنده دیدگاه شورای عالی امنیت ملی، شورای عالی دفاع یا حتی رهنمودهای رهبر معظم انقلاب…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442107" target="_blank">📅 19:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
پزشکیان: عبور موفق از این شرایط نیازمند همراهی مردم و مشارکت عمومی در اصلاح الگوی مصرف است
🔹
در ماه‌های گذشته، وزارتخانه‌های نیرو، نفت، کشور و صنعت با همکاری و تلاش مستمر توانسته‌اند با وجود ناترازی‌های قابل توجه و همچنین آسیب‌های ناشی از جنگ به بخشی از…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442106" target="_blank">📅 19:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
پزشکیان: مردمی که در در بیش از ۱۰۰ روز گذشته و در سخت‌ترین شرایط از کشور و نظام حمایت کردند، اگر با تورم و مشکلات اقتصادی پی‌درپی مواجه باشند ممکن است دلسرد و ناراضی شوند
🔹
دولت خود را موظف می‌داند تمام توان خود را برای بهبود شرایط زندگی آنان به کار گیرد.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442104" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
پزشکیان: اگر امروز کشور توانسته است از یکی از پیچیده‌ترین مقاطع خود عبور کند، این موفقیت حاصل تلاش مجاهدانه مدیران، مسئولان دولت و همه کسانی است که در سخت‌ترین شرایط، اداره کشور را برعهده داشتند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442103" target="_blank">📅 19:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
پزشکیان: مذاکره به معنای چشم‌پوشی از اصول نیست و جمهوری اسلامی ایران در برابر هیچ‌گونه زورگویی و فشار غیرقانونی سر تسلیم فرود نخواهد آورد.
🔹
مذاکرات تنها یکی از ابزارهای تأمین منافع ملی است. دولت همزمان مسیرهای مختلفی را برای تقویت اقتصاد و ارتقای جایگاه…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442102" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442101">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
پزشکیان:  دفاع از منافع ملی و حفظ اقتدار کشور در چارچوب مذاکره نیز رویکردی محدود به دولت نیست، بلکه تمامی ارکان حاکمیت در این زمینه دارای نگاه و هدف مشترک هستند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442101" target="_blank">📅 19:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442100">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
پزشکیان: بخش مهمی از تلاش‌های دیپلماتیک کشور در هفته‌های اخیر نتایج مثبتی به همراه داشته و بسیاری از مسائل و سوءتفاهم‌ها با کشورهای حوزۀ خلیج فارس در مسیر حل‌وفصل قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442100" target="_blank">📅 19:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442099">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
پزشکیان: پیش از این نیز گفته‌ام و امروز نیز بر همان موضع تأکید دارم که از بابت قرار گرفتن کشورهای همسایه در معرض تبعات اقدامات نظامی ابراز تأسف می‌کنم
🔹
البته هدف عملیات ما پایگاه‌های آمریکا در خاک این کشورها بوده است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442099" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442098">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
پزشکیان: تصمیمات راهبردی باید بر مبنای عقلانیت، محاسبۀ دقیق و در نظر گرفتن توان ملی گرفته شود
🔹
در کنار حمایت از نیروهای مسلح، باید نسبت میان مأموریت‌ها، امکانات و ظرفیت‌های کشور نیز مورد توجه قرار گیرد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442098" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت خود را موظف می‌داند از نیروهایی که برای دفاع از کشور و امنیت مردم در میدان حضور دارند، حمایت کند
🔹
نمی‌توان از رزمندگانی که جان خود را برای دفاع از میهن در طبق اخلاص گذاشته‌اند انتظار ایستادگی داشت اما در حوزه پشتیبانی، امکانات و نیازهای…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442097" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت هرگز معتقد به شوک‌درمانی و تحمیل هزینه‌های ناگهانی به مردم نیست
🔹
در عین حال دولت بر این باور است که تداوم برخی رویه‌های ناعادلانه نیز قابل دفاع نیست. رویکرد ما واقعی‌سازی تدریجی و عادلانه قیمت‌ها با هدف برقراری عدالت در نظام توزیع منابع…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442096" target="_blank">📅 19:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
پزشکیان: تحقق انسجام اجتماعی بدون توجه به معیشت مردم امکان‌پذیر نیست
🔹
پیش‌نیاز حفظ وحدت و انسجام ملی آن است که جمهوری اسلامی بتواند در حوزه‌هایی همچون معیشت، مسکن، اشتغال و رفاه عمومی پاسخگوی نیازهای مردم باشد.
🔹
بخش قابل توجهی از آسیب‌های اجتماعی نیز…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442095" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442094">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
پزشکیان: مهم‌ترین اولویت دولت، بهبود شرایط زندگی مردم و کاهش فشارهای اقتصادی جنگ اخیر بر خانوارهاست
🔹
امروز بخش‌هایی از جامعه با مشکلات معیشتی جدی روبه‌رو هستند؛ درحالی‌که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/442094" target="_blank">📅 19:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
پاسخ پزشکیان به دروغ‌پردازی‌ها در مورد استعفایش
🔹
بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام و اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442093" target="_blank">📅 19:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442091">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌‌
🔴
پزشکیان: دولت برای حفظ منافع کشور و مردم تلخ زبانی‌ها را به جان می‌خرد
🔹
ما با تمام وجود برای خدمت به کشور و مردم عزیزمان و همچنین آرمان‌ها و ارزش‌های واقعی خود آمده‌ایم نه ارزش‌های کاذب و غیرواقعی. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442091" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442090">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ ‌
🔴
پزشکیان: [در مورد مذاکرات] حتی اگر نظر شخصی بنده متفاوت باشد، خود را موظف به تبعیت از تصمیم نهایی نظام می‌دانم؛ چراکه معتقدم ایشان براساس دور اندیشی و همفکری با عقلای کشور و در نظر گرفتن مصالح و منافع ملت تصمیم خواهند گرفت نه تحت فشار جریان‌های سیاسی…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442090" target="_blank">📅 19:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442089">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
پزشکیان: دربارۀ مذاکرات، مصوبۀ شورای‌عالی امنیت ملی ملاک عمل است و هر آنچه مورد تأیید و صلاحدید رهبر معظم انقلاب قرار گیرد، برای همه ما لازم‌الاتباع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442089" target="_blank">📅 19:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
پزشکیان: ما به دنبال آن هستیم که از مسیر حفظ اقتدار ملی، برای کشور گشایش ایجاد و منافع مردم را تأمین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442088" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
پزشکیان: نقد و مطالبه‌گری حق طبیعی جامعه است، اما تخریب کسانی که مأموریت مبتنی بر قانون به‌عهده دارند به دور از انصاف و مردانگی است
🔹
مایه تأسف است که افرادی که در چارچوب مأموریت‌های رسمی و با هدف صیانت از منافع ملی و عزت کشور در حال انجام وظیفه هستند،…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442087" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
پزشکیان: در برابر هیچ قدرتی سر تعظیم فرود نخواهیم آورد، اما در برابر ملت ایران و مطالبات مشروع آنان خود را مسئول و پاسخگو می‌دانیم. البته منظور از مردم، همه مردم ایران هستند، نه یک جریان یا گروه خاص. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442086" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
پزشکیان: تحولات اخیر نشان داد که هیچ کشوری بیش از خود ما دغدغه منافع ایران را ندارد و به جز خدای متعال به هیچ کس نباید متکی باشیم. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442085" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442084" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442083" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f5decafd.mp4?token=DHwpueEYJIl_Fm5vokZJcf5vRc7O3ZyDg-oqoA8tGGhkj1GbFHV6nIkWEaZmCtbpsmWQd6BEk7AzIiBI9RS8vyDIKcG5eGjmrxSoMnEydJIDvu1NHKIkaXaaC_HhtT55TWXwhHfjreMq6lrm7_LMWEe99_FaPxjPKHCJEa0Z_agqTghRuMkr9jj3FVdEUUVFrp-fJKuk7OSXsQk5YOPTHRZ5rVPYDjebvBS1YNCZR_RsF7hoLChtbYB35IzYeJcw0844JacMTlhSZ0vuh3FAvDmt6GWXXopDgfZXSBLe2cm0uZVFv8SVtGy-R3krGCRd8WEEqf2oAR8Gn-kj0P0j5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f5decafd.mp4?token=DHwpueEYJIl_Fm5vokZJcf5vRc7O3ZyDg-oqoA8tGGhkj1GbFHV6nIkWEaZmCtbpsmWQd6BEk7AzIiBI9RS8vyDIKcG5eGjmrxSoMnEydJIDvu1NHKIkaXaaC_HhtT55TWXwhHfjreMq6lrm7_LMWEe99_FaPxjPKHCJEa0Z_agqTghRuMkr9jj3FVdEUUVFrp-fJKuk7OSXsQk5YOPTHRZ5rVPYDjebvBS1YNCZR_RsF7hoLChtbYB35IzYeJcw0844JacMTlhSZ0vuh3FAvDmt6GWXXopDgfZXSBLe2cm0uZVFv8SVtGy-R3krGCRd8WEEqf2oAR8Gn-kj0P0j5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگزث وزیر جنگ آمریکا به CBS : «ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا خواهیم کرد یا نه، بلکه کی امضا خواهیم کرد.»
🔹
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود.
🔹
اگر ایران می‌خواهد این موضوع…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442082" target="_blank">📅 18:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An_2lF_k7sX97HDxvJMY8kjXBXCEAeeC9cv4-yMC7IEzt-W4wAx5DFKXJvOdfgXJygxGkPpihtpgUSmU2kChZAZ_4Irf1U5_gz6PUvVBjcrnc5z8DNHnR4b9gxY5c7_GzwFZ5Nb8HMS-64DzH-6CrJm05DSe_LgF4NGgZ9sKlB9IRTr7ld1owFH1CM8T14TARFHoFxyfnv34O34G2XDHJzet7MlbgF-uJp6btg7_Ae0H2wb_TgHKcTjjqwx4Bm_mSwfyj8FqH2fFkQGrc8x8nI5KdOtkwz5meIStQPyYlkPyqzCaJiUaPWzq725YiAiLQgdpg4Wr1jLSJw4IUZOwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده هوافضا: گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
🔹
سردار سید مجید موسوی: ملت بصیر و غیور که در خونخواهی امام شهید مبعوث گشتید و در راه تحقق ارمانهای بلند انقلاب اسلامی و اقتدار و سرافرازی ایران عزیز، با امام حاضر عهدی تازه بستید، هوشیار باشید که از شئون متعهد بودن تبعیت کردن است. پس نه یک گام جلوتر و نه یک گام عقب‌تر، بلکه همراه با ولی خویش باشید.
🔹
درست در مسیری که امام خمینی کبیر رحمه الله علیه فرمودند: پشتیبان ولایت فقیه باشید تا به مملکت شما اسیب نرسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442081" target="_blank">📅 18:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به صدا درآمدن آژیرها در شمال اراضی اشغالی
🔹
رسانه‌های عبری اعلام کردند درپی نفوذ پهپاد از جنوب لبنان، آژیرهای هشدار در شهرک صهیونیست‌نشین «عرب العرامشه» در منطقه الجلیل غربی به صدا درآمده است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442080" target="_blank">📅 18:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgW63P2Yy_4iWb-SUKVQ6zCreEcyF62EglBlCfMDwR7MdtfGwj0Ec_Bq8tlxVT3dZ0I4ynY5TOOSP47o9QV7cgBXQ7_GcptVKPX9SDc6zPDtz0Sf2xsjEOVMA8_hXa61kfkSuCpgA589ZhvqlUdQ2Td98sXC4Rt18fFw5-VUgnObzX__wlr-6sVVwyQQaM1928pfvhUYpdTKVI5pVXjWHm1nm4xFaPkQwrP9wjbtX0Obx3AHjACpNHc4cYmnsAidWW7hDEVuyBe90yy_cCZRHQSkfVVNPIC2OocqyA9eAVjTAza-uRWqVBXiv9nRW9UVwzyeqSgN7pcon65jxN510g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
خبرنگار آکسیوس و شبکهٔ ۱۲ رژیم صهیونیستی: اسرائیل پیش‌از حمله به بیروت، به آمریکا اطلاع داد. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/442079" target="_blank">📅 18:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I33mgbvW2Vh0RvipUqKzjo0U-8u35UanSVKeciJBSNAgqQSP8b3PfSBfRZecNlbLKCqvd7yTw2T1rX993wmK5cPNWPjfnD_yDqDc9ayysC_UfY1dlSMP2HP8lJOCE7nEIV-4nhQekrWLhpZ1y2zy57MhQGvfAbhAr3gVM_ZKIvtIyG4VaKLF-C_k9oTR5nH1lXElN7bhkUOVp47gzZGO7zsq6SoE-Jog-hEDRdi4pZ8XeFhrf4W3w6ZGvx8TtEJ8HKZgmQCNKlBXGsVjdFLOVojvWcCAKD_7Y_Wr2-nlRb2zFN6tDFGiotER4flS7JHnpSrB0PpYkXRkw0nGofHbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگزث وزیر جنگ آمریکا به CBS :
«ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا خواهیم کرد یا نه، بلکه کی امضا خواهیم کرد.»
🔹
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود.
🔹
اگر ایران می‌خواهد این موضوع پابرجا بماند، باید حزب‌الله را مهار کند.
🔹
انتظار دارم مذاکرات پیشرفته‌تری انجام شود و معتقدم این مذاکرات ادامه خواهد داشت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442078" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5fdb39a7.mp4?token=RvPgQpbMFgsjOAzy1XJSW3ZNWSb6YgDWMukjNavG7yIn_WH-0RS0k8lQAAjJlCPBrycGX6iMmHjIoM5zvim2Lm6NMKFu3NcV5FdJJRw9uqTBMD1-MrGls2l-m6BsPKmoYQ0AT33_5wtGw0kbmGU4rh5_8SNEla56cTd5msNtkecGAoiyZLswqc6okMGTlnIw26eC7SBP-LYm9AauIjvmDddwSs16Qvdgz5zYS1pprGaoVrkngyKMtT-xEojdTgrapOMwMGfYwL9t4JXor0jGZB4DxvacPzQY6dRevpqgsjCNqW8Yapb8MvrU1YagijyPrCgjJFC7hGzFY-dE8vnf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5fdb39a7.mp4?token=RvPgQpbMFgsjOAzy1XJSW3ZNWSb6YgDWMukjNavG7yIn_WH-0RS0k8lQAAjJlCPBrycGX6iMmHjIoM5zvim2Lm6NMKFu3NcV5FdJJRw9uqTBMD1-MrGls2l-m6BsPKmoYQ0AT33_5wtGw0kbmGU4rh5_8SNEla56cTd5msNtkecGAoiyZLswqc6okMGTlnIw26eC7SBP-LYm9AauIjvmDddwSs16Qvdgz5zYS1pprGaoVrkngyKMtT-xEojdTgrapOMwMGfYwL9t4JXor0jGZB4DxvacPzQY6dRevpqgsjCNqW8Yapb8MvrU1YagijyPrCgjJFC7hGzFY-dE8vnf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442077" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjI7621oE3eUvWM4bC89NIVgFzQjyFugtEWgOKgyZWPk3y_17oiuqcoB2Uk80iIVOvXqWXUOHaxy7tFENKPkyV9wkcDPMSRYJKVjJrvWgiMnzen5FAoRtnWiaOuMpSJzz8-8EN-txvzn8XiG2uXEJmoxv9rlZ0mM9nLA_DUdsons_KDbKyXWOy3uE81hjPNwTWjsHyFuh5K8Zl9oobWeuAFrOOuVzhzcfoeoZqMZ30kr9DAlDVOYnQC6cwu42aOe_YiDnNpoSj9bbLPkNbYAkmQ445RipzXgitwJCwDbgNAY1TgSBP1NmxEWMtgXgTUnUyDsTa9Ww8Ux5fobWR5tqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش جدید سایپا از سه‌شنبه
🔹
سایپا اعلام کرد از ساعت ۱۰ صبح سه‌شنبه ۲۶ خرداد، طرح فروش مشارکت در تولید دو محصول «پارس نوآ» و «کوییک GX-L» را ویژه متقاضیان طرح عادی آغاز می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442076" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آماده‌باش صهیونیست‌ها برای حملات موشکی ایران
🔹
ارتش رژیم صهیونیستی اعلام کرد در پی حملهٔ ساعتی پیش به ضاحیه بیروت، خود را برای حملات موشکی ایران آماده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442075" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpStclVXoJmNALLvWRgagBpPAvL9p3yodJnecrPdIiZbjIexTR1qntQlbNSqqPF7_PR1OC63bh1tMjXbBFVOw5tP_HCGLsrcPsZ2hVHt8zWceKOIZAt6WIknwWFmS3_QqI1qZaKjIZvdWjvVfTVP-o-D8jnbeE-D8evRrL1Wz__KYM42kOa7QmZi_G4nAaArJlg038wxToAJWslYY7sPkXrABfz3yU1RgvOHpfK3AkgdPl16oLd8JtU2MSAI2wXbJZQeOGizsY1FkwY4VP4I0UKMggRNe0Droz5dZS0Sb0lci8mZ9GVES0ni2lV1A2scBiqaKZ60UOI-a_3zzfz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو شهر ایران در فهرست گرم‌ترین شهرهای جهان
🔹
امیدیه در خوزستان با ثبت دمای ۴۶.۴ درجه و ایرانشهر در سیستان‌وبلوچستان، با ثبت دمای ۴۶.۳ درجه در جایگاه ششم و هشتم فهرست گرم‌ترین شهرهای جهان قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/442073" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442062">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آخرین جزئیات مذاکرات غیرمستقیم قبل از حملهٔ رژیم صهیونیستی به ضاحیه/ حضور تیم قطری در تهران
🔹
یک منبع نزدیک به تیم مذاکره‌کننده ایران، ساعاتی پیش از حملهٔ رژیم صهیونیستی به ضاحیه بیروت، آخرین جزئیات از روند مذاکرات غیرمستقیم با آمریکا را تشریح کرد.
🔹
براساس این گزارش، تیم قطری هم‌اکنون در تهران حضور دارد و ایران بندهای موردنظر خود را همراه با جزئیات دقیق مدنظرش، از طریق همین تیم قطری به طرف مقابل منتقل می‌کند.
🔹
او با تأکید بر اینکه هنوز هیچ چیزی نهایی نشده، در خصوص فراز و فرودهای مسیر مذاکره گفت: «حتی اگر در روند مذاکره پیش و پس برویم و به عقب برگردیم، شرط اساسی ایران این است که در پایان، تمام موارد مدنظرش به طور کامل لحاظ شود.»
🔹
او افزود: حتی در صورت اعمال همه نظرات ایران قطعاً در زمان اعلامی ترامپ هیچ توافقی امضا نخواهد شد.
🔸
گفتنی است این اظهارات پیش از حملات اخیر رژیم صهیونیستی به منطقهٔ ضاحیه بیان شده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/442062" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442061">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در میدان تایمز نیویورک
🔹
آشوب‌های خیابانی در نیویورک پس از پیروزی تیم بسکتبال نیکس همچنان ادامه دارد.
🔹
پلیس تایید کرد که یک جوان ۱۷ ساله در این تیراندازی‌ها زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442061" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442060">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم حضرت عباس(ع) در
آستانه حلول ماه محرم
@Fars_plus</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/442060" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442059">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
بستنی فروشی که مدافع اصلی تیم ملی فوتبال شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442059" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442058">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh2mgjbDhwWOA55WEJPq_zzJQ0GrzC9EvTi1HDXDt8qbqQZYCC3g2l26B9aaqJB5uEE6p2O2hHacpGPe9o0NiKMuv5nMKEFvi1tZu7kSoWBq_6Nl_GRTI7ciDFkdfVDmnKLl6nRiu_BCc75GGDLjtNNb2PUxRujfGUgXNhrUbqIVRDtUYrnUYZjpTCfGqu1m83dweT8hHLfSsS-N3CEIetXYzo0jlSXXNhsmOil2noZbm2MIzT2zgzmJ37MM78stxlQseAiicw2QqijuZh7JNydtXiyoPDEC1UsUFXKU9X7Cc6vMKpB4BfHx6Z3UjE2I6xq7znozZcqjo928X2XUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای شبکهٔ ۱۲ رژیم صهیونیستی: هدف حمله به ضاحیه فرمانده واحد ارتباطات حزب‌الله بود.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442058" target="_blank">📅 17:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442057">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndf-As8iAg5WKVtgy7OKDNNSByE8CJPn9_JBePrd4Rq_qS_GbhcwpFSW01MuuyXbeeNiNya3jW-QkBYfb4X4lFBqtTj522y9puOxboJUcR7qFlFKcYrGblnfCmj35Ex4OXyS9dXNtoPb6kPg8jRrERr5y0fxPp0NlNYInD8t9nHIWQEFjK3ECtc3iqyON4JvD-ZfrpBzv5biG9awwHkdfmUGcPiVKPpRmzArCfJ2Ip3D8mW5EMUNWdRfDeP_tT_cGAnjodhIV2roXd2vbKa5oXiCLMk8RtNHRpv4D1Pb0yhU_6ZngJezDFh9-HBV-QY9ifDBRDFI26Jms8fQ3EaJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج شمش طلا سه‌شنبه برگزار می‌شود
🔹
مرکز مبادلۀ ایران اعلام کرد صدوپنجاهمین حراج شمش طلا سه‌شنبه ۲۶ خرداد از ساعت ۱۴ تا ۱۷ برگزار خواهد شد.
🔹
قیمت پایه شمش‌ها در روز حراج اعلام می‌شود و معاملات به‌صورت حضوری و نقدی انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/442057" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df5L25xlKwm5vNazPUDjMW04NanvbYMGuSKDitwoUnQokI9xGtk_QYs_fDse3zoiP5uS8BMhfPuHgFSn3v0yuzxsC6lIN5LWIaaSIUox4IVC_l5sC6LX2MIpj9_d3DdR_tVYT4PQnACH0F3qbVDuk6P1rpG4uUZ-g4TygIHqAsMofgI9Df5PBXamfKEJoRvqQskQvrMvIecnuqDyHJTukzXxou8pwSMkumwbezntAJSOguuqbRXDO1nuQEdHhNGNJT5wjj2CJRmwHG0IywXZThutbTSrRtGhB7qFfWozTMT-qZ08Ctq8PnzL9OfItqPfvIaUa0jsqJ6W2Z-wGMmF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در بندرعباس
🔹
سپاه هرمزگان: روز دوشنبه ۲۵ خرداد، عملیات انهدام مهمات عمل‌نکرده در بندرعباس از ساعت ۸ صبح تا حوالی عصر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/442055" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌‌ آمار اولیهٔ دفاع مدنی لبنان از حمله به ضاحیه: ۳ نفر شهید و ۶ نفر دیگر زخمی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/442054" target="_blank">📅 16:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442053">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پلیس: فریب فروشندگان سؤالات سمپاد را نخورید
🔹
رئیس پلیس فتا با هشدار به دانش‌آموزان و خانواده‌ها اعلام کرد هرگونه ادعا دربارۀ فروش سؤالات یا کلید آزمون سمپاد، کلاهبرداری و فریبکاری است.
🔹
کلاهبرداران مبالغی دریافت می‌کنند اما در نهایت یا هیچ سؤالی ارسال نمی‌کنند یا سؤالات سال‌های گذشته را در اختیار خریداران قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442053" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwh6gz3WBXUEC9wHRu7yf_URU2X9yJDXp5GGSydgyOttaBdOFxL0nS0ZkNSlIctDuwVm_L-XBSPDES4Fc0K3ZldzRwyBzTIlJWbg9k7Jrt4vLy2h5p5HpnQiBH-FRQ6Acsxw65oM0u1hK2I2b_cVNyqw4X3cgmRmjYeVBRHa_ja7_PcxlN9CcZjWCEWuXX23_rMuASt8vUW1uD93MFGmX-fFKlDsP2oqoMCFNKE3vOWbKgEbXtxkjLpD9oQoqiqfsRi-Dtr4Ny8Oom6blloWkNm76tJjIYLccdnL7x-oTEUNYn-sxRnYyvZ_b7-FVnj70psPpOpVy1SbB2Npswil_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات وام جدید بازنشستگان تأمین‌اجتماعی
🔹
مدیرعامل تأمین‌اجتماعی از آغاز ثبت‌نام وام قرض‌الحسنۀ ۶۰ میلیون تومانی بازنشستگان و مستمری‌بگیران از تیرماه خبر داد.
🔹
حدود ۳۴۰ هزار نفر مشمول دریافت این تسهیلات خواهند شد و بازپرداخت آن با کارمزد ۴ درصد و اقساط ۲۴ ماهه از محل حقوق بازنشستگان انجام می‌شود.
🔹
ثبت‌نام متقاضیان از طریق کانون‌های بازنشستگی استان‌ها و شهرها انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/442052" target="_blank">📅 16:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
خبرنگار آکسیوس و شبکهٔ ۱۲ رژیم صهیونیستی: اسرائیل پیش‌از حمله به بیروت، به آمریکا اطلاع داد. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/442051" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ ‌
🔴
قالیباف خطاب به آمریکا: با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/442050" target="_blank">📅 16:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/442049" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442048" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه سقوط هواپیمای نظامی هند
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442047" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX8v4vPAvZVT0pOpX-QvMTwGOk4a_cRnIw0ZITzzE6SDR52zysuntL3xezI-NXHezpUh3emBOeJYU7BlRl63e-jk3GM7iXRBonWz973_hSqX_y8gGqFtft9eFqf5ca69shU-RpnSrCdMWOn8N2rZMkIAY8G3uhHUCU1Drlyt9rxaROR6evc_4kBl0c_yuBQ4nCgljZsvUFXxzlQZOcke8wcrNUBJcgdnjUWxzZ3Y8wL_2_VfAvB9Ga4ygSfi-RA8oU4O7eN3GEcjZCw-B4Rl1y1FfKgh3JxGawz9JLv2GIrzNUNQHBP0zLO7LTsqMzzh81idV4q4_MVj5diIpJJw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروی تهران به بیمارستان‌ها متصل می‌شود
🔹
مدیرعامل متروی تهران از اجرای طرح اتصال خطوط مترو به مراکز درمانی خبر داد و گفت نخستین پروژه، اتصال خط ۷ مترو به مجتمع بیمارستانی امام خمینی(ره) است و احتمالا این مسیر تا پایان سال به بهره‌برداری برسد.
🔹
این اقدام می‌تواند در شرایط بحرانی مانند زلزله، حوادث گسترده یا ترافیک سنگین، امدادرسانی را تسریع کند.
عکس: شایان محرابی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/442046" target="_blank">📅 15:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/442045" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442044">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«در همسایگی مرگ» زندگی کردند…
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/442044" target="_blank">📅 15:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
🔹
وزارت اطلاعات: یک هستهٔ ۴ نفرهٔ گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکهٔ اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442043" target="_blank">📅 15:43 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
