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
<img src="https://cdn4.telesco.pe/file/bsefD64zyA_telpyIfSw1n9i2_-5OwxYgsMAAAKWErA-umviJEOkebZILHe6RU5gOW2jx2GOOwRRD6SQg6nheD6wqsxu9E7Co-NVCgea7Suk-oFjFiPYgmb0vi1MW0oH1P_x7NfMtTTpfY-Bqzi3XoekBw-S51qFrs2ehtnTct5TtOVQ1yF5RJitI252DYc2ib8aJR3rxPdAfnnBc9PVBuPe5pnJudlsL9pIX10WXNNaHZf_JKaMBk-miAU2K33I9NhI_W-KnP2F4XlsqMNsWM0Di7t7He3VbceEk9T-LMOjnjwhLBvfuGbEjSzHC5M03Z5c_cN8MEPSryIx4RcDMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-442009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buRbKm85KJiHOhwVwOtfgON-WOkmRkvzXWnKNQHGW4jzY4Vxr4ru3SzwX7-gy8T7hbbjmclpVL5T661jQfUJbb5RKE7RZ2KgIkRxMp2MvaRpXlxJHgO1qMHJrK_2YppRiJm4JOc9DkxLQwCtUdd7XxeKM-6L1eaL_FxrNVU24_QDMT4PKdfx_E8gAlbfsfT56RGIV8IL4Qq4zDzNHlUlRLTiimjkrXZjUgNY_f1UsucayUvdyn7VZ1_t2rY26YXEuv1wU9MikF1q3DlJai5UdAM2S0Urm__CY0nr8FYQ49OVfIId2iHcB7kMOUOPnk8U-1faCBOFxzbrbj3U2TSLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ قطعی برگزاری کنکور مشخص شد
🔹
رئیس سازمان سنجش: کنکور سراسری به‌همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد برگزار خواهد شد
🔹
بیش از یک میلیون و ۸۰ هزار نفر در کنکور سراسری و آزمون پذیرش دانشجومعلم ثبت‌نام کرده‌اند.
🔹
آزمون پذیرش دانش‌آموزان…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farsna/442009" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442002">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGE9jacaJoLtQMG_jhPStlvWaAHFii61R7S4sgYlbPfwPzDUyukCbbmRqWQ_pC8FMDjssDuXC9CR8MNjH4-xX-YMiLysF0JqMR06oczrVSQDsFHOysY52gKdG3PRA1KuY45qPraZh3pIB3wFOz0i8marlg-3LnQaXH509cgwGpgNXSlFGaw-InwpVDh5c5lNivxd-fnX7st2AdOOMzbSzHVwEEjpTmofwqYJX_VL4oDSxO34SHXirtVwHhQghcVrOitHEMRHIIU1HPBTAWhLdS-c4hclGu-nVDLxUDSTKeOcvNdOhsa3VR1JDfo4JEMIdrUgE2LDswibYBDe-A2zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEZxvHHceiqvLf_Kg8zzNiCcbfiyWypNMzMpXcXRjrjvCyJxNHb-XUPUOnGyHRsCQjQpQHo6uiYoWMxxK845PIzXA9PjL0BQ-dQvxhgg88YDOAKgBpnn_QiOzZAK8Z3Ro4pVj1N3GUtMNCHmCcRQZTcHlug8j5Am17I6D9KBJUBaYMA5w8DQ3pAcQq2d2USEPKqM-U_wyauk8E3q8Crg6Vw2ESdOEJtb3XHZKAQXB8R47K5tGAG6l189Rvel6KDCFFe-mILOJVq5eCzkK96e58D3oSuFk8ky1fil1bfMS4ilGDnqfy8-zSzdlZroe_ajxk4oBRHx20CBtZ5byFuqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFfdPHTPfJz_x0ATBlYPLEiEiCSuycHcK505f3y8yfFXsQHbgrCFCRpUNF9vOCFgVaZOiBkIqm3_F_JEbePPkJIE7bztO7IpBrK7vveeeGl6F5-HJtq2hcsB6Ksw5-HXAuNiJ7-wtujZCeAPvacH_YEPLgCROgJ_Qa7lDSSjX_dP6mbnRitw1vH6tK9r771GI8uf_8Ux2avPy_VWXlIzc5FnBvJq3OtzbAE6oYY2c7KyPZBT-Yb3wnSb_otvY1fRID2ESSGIDZRVfOL07zO4oTmKXpFTu3xrmXhntbaNQ-Irs0AZ5F6yefINJzfEeFTFHEQsVuRURZt0YVgqvv5nIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-FAB0Jrbg64GURoHXHkTsitJC5nDEaIWFj_Kmi44jNy-cwr7gC6v3J9W-Q-v6aDjrJ58pPYdTk9k-0OqnE5YuqYmomJO8rEKoy_R-IpZtu24AalupLxf3SnG8W6a6zB3QPbsBjUztRwZuBooq4xRYPB9zQh2UxplovXFaYr5-qOU_giHrn_l7sLN8B8pZ4NOGkTgNZ3j8VjzyzyuXxxoE3zwWAfL6kvh8RzBgbFqMCYFikE8sA7IpdSt_mKBY14CtY2m3f-l9FM59lAhVNTZ6v2BfFpliwik2f4oaek2mFghZspjG4r31zzJDN_MGjqVkH-tTvwUjmQ9qA7rs8M5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLE5bSgDYJE3ZlrViJ34g8fmuLrUmQXfWtP6U1w8ZyqonII4DPxJOWIqYGPclsXCshf4-XlM69mMRau1ZC1gL7YAESKXDlW6a-7i5kutCaCGCE2CoXnvI6uWsIargt8GV9luIuC1u9OnUbUp1-weTOEFmjad7XEsLsOpheYSoIe7L1axIUboClnL_uKMt2sAOfGE_rQhz75tILn7DtjNxyPGorrmUnolgpD8BKjl5D-w6qt2wfR1ljh7WOkYqgv-j4KHj5nFsfJ6jeOyZuDSfVgra_qFGBwCotEDU9zxlFc70f5BEGrH-p9m2iV0eHsg1Tm-P_ghnmm3VaukGBPfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8EiJ-t4l6NvqSgZLr7LR8__stg2mYaEBWwr5fKU3069HdRKYeqU6ZJaet9S3FNqxxxiqVJxqebSpejyH13KxQbVH-6q3i7nSWfCva-jzUr_ccIX0qzZVPmDh4tEOblwm1LT_GkuntwwPaxVIgABqdCydiNO3gQxZbI5o78ocDLLNBf2j2Ss0tbE-UpMse1r2napg_5rnKxH0fl_xKIMAuKOm6c6EC8SKe2CEM72Go86NdDqkFQEN9msYL3hBBeDd5KbsOdDNS7nMVpjEZFZBlJULCHhFxHhlqdBIZudzt8b8LlI_GFK6gKKpNlhkHVlA-oERo9SToekcOOp4KRDZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مجازی مجلس با حضور وزرای آموزش‌وپرورش و علوم برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/442002" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442001">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd-8MAdOPCGu8TN4oe3EOfLqBdtdlkkx6aYnavAh-3mejwLFD5c2NHvRfsRXKl9Ybp8_NabDKEkYdhDvLX53pal2Qygf43vdQO2aE7Woxzq1LvcDrxfdoL1u7DYl01Ox3Z1Va_S_HKmw-4ELMFseBXrZIBEDLz2YJgs2cYD2VExIX4UsSsAunx0ZQuDSMe595geICr89ns1T4jN2hkpBNnExbd5bKmEFEccmyIFW_7huaXHRDNWZYwTSZJVn4cWUZ6KQ95CuUDxE_2MPmwxSYkRs_W5MrmDvD6FlcqMlEBUSXZ58Wulx8WZLF3q1oYRx-oVJQfPYu7mAbvFD9dQk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدیدش از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و مثل روزهای گذشته رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/442001" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442000">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ زمان‌بندی امتحانات دانشگاه‌ها تغییر می‌کند
🔹
وزارت علوم: تمامی امتحانات دانشگاه‌ها و مؤسسات آموزش عالی کشور که زمان برگزاری آن‌ها با مراسم وداع و تشییع رهبر شهید انقلاب تداخل داشته باشد، به زمان دیگری موکول خواهد شد.
🔹
برنامۀ زمان‌بندی جدید متعاقباً اعلام…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/442000" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441993">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txvOt0poIkEsDXlVzPf-8_LlJgQk_Ly8lOHDkk-BlAawIN_whIAqwRlbEfce6ZMAH4SqE-U4S58xFc7RQ0Eg9AfE6_bjDyhwSsp4dHNYz16_DagI2W_mUZOiUcVkKbvJspSpDDGkCR7ggBADnJiC8EKHnRbPy7hRQHNkqIzm12c1RIOg4GhJ7VOLSFTe8RBUsH4oWd69Bhi6gdHUajddnKhhPzNRHAvWM6Wa7IOq9psAeXozmAdscl7kqFVApP3HCT67MitGBbFh3id3VDZBEShL5KJYfA73QgchrLoe2Mdare_xLsQZWvc1ugNz4f33_GLANIc4qcMrSarYKFmauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGUjekvw0p77mgmIkkdodGNhhaapzaPAdY-sU-H9Mov5N_NcgDLkb3jxbt6f-BT_-mPChKKqdm3JfwuNb0DPzrPX3ySnWEKjq9En7tvu2XfcZZWjx_xT11mxvBqnlZdBiEB8pDMJjF8YLVOZBIdFs6GuhOYW_qREBHZdtx6v_2TY-xj2c6gIfYvMTo-VOcmc9W7bmZjmI4dHgBGrLLt4XJmFasDjceAomMoAz41RsW_e51wOcnvpvT6VmAoWdKg4f_Iw7XjRw7FQqYVD801CCd-3sLa0KmDVvoUO9dea3ZqxRPmtDk8Jn-OhsoNNk0fPR5aZNU5RWuA36xUyc6y48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssNjoOqrxABI_Bv66gxuMNLz1uCNBqkaxLnJ3oMnxOZFJFazTQzbUBe7_h2f3AQZJ4ETGU2dk4oLl9Bu9CMgqhi5wVtZ_gGJRic39XsSYnvykyrqJmZZx-aAA3EvXNKpec1pYMPzWVLXCklQ4HWZ-GpiyhloR5oVlcoH6IGkft6WbzP0x6ZoavKMnLV6ygh-7YzK_Kk5EEGbwHePj4EpDbPAwClGTCmEdwzHakSOOMF5rt5vt_cXQvORIaTpWmtmR5IWusXA94zJhnqBUWuBNTnMlzMkDwmvoV7K9I7MVcYMQJHe2TSYcnLrz4hdhNw8oC_NfBdE46CWITxEie9K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H113zx7EVIU1LS5JL691VeahYHf48e4n9oCQbnkJfc7fhEzaAR253DayKUZU8W-H9Reo_7xEggRilpV664WYs7rBISkhDuSLqzFjq6PZV8DMgF7XeCxWF1EqHCpe7woYurOXCsZuyptiG4OZnRHA9wpkDQOvgo5qqjTsGHpvloG60vI9MTdUEPAgR7NRYWBJfjGdIpeBDseWmkdPPwpHijJBFvqpwUXh3igKdTbHioJJZaq-9oQ-m6L4u03i2yFW0vQwfpe5Aok1I0q66OyDNIj6mnTRZ_6FavNhWle5Zwv28tvC8G9Zpvj1rMPixLWs0wF6hodIl_Jg6ssbSP7NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7-thi36Y3MBVW0f3lL2926ukyfL8SSKAA9IN9N08xSpVuiXKgPt9_Guo5UK8p4NZqdNTl-kB9FpFWjz5SMwZKFBALJKEaAqy0D0hq6NVYIC3seICmFcRxQ11YYkfyBl3twZSHdZiHFPcl_RVDVadQ7mr1EicmtTDfWkd-7kQJ7XDb_aTtqXkRrnohLy_B3FbW1lA3iWoEePDOzbBh7Uko8jFn9HGKyZrhZD8YEuNtpKdlMtgqcmQejqst660xDkeDK824pO6QmmqjyTYDrhbdeK0tqkHyG6wfzvwozIEpuo7t0wsMuOVsbkRlfuhklRbmDpDF-CCZ-a4LNV16x_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgTJ0ACqfbqw5I5k66xHxmaIo0De9Mai9fD-7iOJcFfxDIagxWksSXTq5B0vHM4Piwjx3NbFrL0f0EVLEB_jsO3AugtBns3dSWDXEyN9_XIKXv6CD3j2yZVNB3D0G5_aRzRuZp3rA4BAbOum04ozs8Nh2z0Wgv6t8qe3VJb7zlTBKfREXvqIw5krBxScfBlqmB-wrnMTEe6cxXv2LW-QrvkeEPOTkzlStTHHInj7HFOC1LOopploDq2f_o38sHusiztqBD0v5nhcSmEAG7K7Ou7C1j0cuMri-yQiJUlqV4UsZjRXxBqqmOB8HD77pt45XtNIb0KyY1Tt419WvIvkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDxJCcV-toH7viiIGhpXcDAWy55VNs74bWiOMn5_yQkMGjxTuJEgZF8656Hhy9dwyQLVoibwO2X_-ku8h7DYJHXzbXO7eF9l637ePnn4mkRyWT5AwG5-gkccWcxueS6v6WXJBfzDtPSgTiK5MpWq9_YaYsGGasHBVXLm2dHCdWo5xfQB-MchhLjvo0hoPlA5Ocb7ntwhkxTSW4q16IFvqS77hUgShF7R2H3apK89ryi5R9a_A4_WWeTmxDKuU3sknfPQFpN9gAqAXy9GhdlCSBKmG1A95xskm-NT9Oa0AOJ78-EczgE_nj6umVZUcBHMdlZSoQt78y_4lKwTpIIZ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ننه میلاد در تکاپوی استقبال از محرم
🔹
بانویی که سال‌هاست در مرز شلمچه با برپایی موکب و مراسم عزاداری، خدمت به زائران و دلدادگان اهل‌بیت(ع) را به‌رسم هر سالهٔ زندگی خود تبدیل کرده است.
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/441993" target="_blank">📅 11:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441992">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون خرید و عضو کمیته راهبری پروژه بازسازی و نوسازی نواحی آسیب‌دیده  فولاد مبارکه:
📽
بیش از ۹۲ درصد تجهیزات بازسازی فولاد مبارکه از طریق ساخت داخل تأمین شد
▫️
آرمان امیری، از تأمین بیش از ۹۲ درصد تجهیزات موردنیاز از طریق ساخت داخل خبر داد و گفت: راهبرد بومی‌سازی و همکاری گسترده سازندگان داخلی، نقش تعیین‌کننده‌ای در تسریع بازسازی، حفظ کیفیت تجهیزات و بازگشت سریع واحدهای تولیدی به مدار بهره‌برداری ایفا کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/441992" target="_blank">📅 11:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441991">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHrjAf_edo8fB_hirN72zUqEB5IXCzKrx8Uh0wM83xLdvjWjc-JurrF2BuBRNQn1Eu-d_83poIq6u_lPXqJXrn_PjUm9y_yRlAivwfYYAhgas40Y0px982GNmuML2bhs8heQB-I-TfQ_WA06ENdGPk5tE5fNXQyBpWyNPnEQnrFTY3GUbDjVu01AJ62jxD7F2y8cL2tPtmdfrAqmQtZ7d5uKHSOcjUGZBg6zeuRdtk0Lhwmwcd28HFU2Pz1czysdee9VpkKEqf33uKTEWukrFrBOh5-N55ublzOmqiv2PhfxYTKW3Z9WLfPCmO6j7oXew214_tfIV4Eo-mviU58pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت بیمه مرکزی با تمدید یک‌ساله مجوز قبولی اتکایی
#بیمه_البرز
بیمه مرکزی جمهوری اسلامی ایران با تمدید یک‌ساله مجوز قبولی اتکایی از داخل شرکت بیمه البرز موافقت کرد. این تمدید بر اساس ضوابط و آیین‌نامه‌های مصوب نهاد ناظر صنعت بیمه صورت گرفته است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5046</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/441991" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441990">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/441990" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441989">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9Yz-fzoUWbZVs11i9TKahEZvyOVPt-b5_fempcqwMoKJM_oVpbIqkVfb6DPAKMJillrL2wDDEJ3O2J5a9VBgd7Ckch3ixv8Wn6AmYSDn-m4fXCdCMUCxhiXzTmmr1mrkIHlF4nyWjdUf4m9BgirLLbWoGAOMld0ZQpUyr4o98otZSaLwtsZXQpzneaX9YgqTXt6LvNDwHI0tL5y8jY9egJ0tD3CM38GFwsrIumx65hNePeDnCtaERKjF0YVITkIOGe0xG9EEsHyvVtBnSrAisX0bjZAANjRG1tiX0OhkvlLwBN6Zm2VXkTDjbtdEiVlXW6ISAsb6oPeE_zQ7DPyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک‌های تروریستی
🔹
فرمانده مرزبانی آذربایجان‌غربی: ستوان سوم «حسین رسولی» از نیروهای مرزبانی هنگ مرزی چالدران در درگیری با گروهک معاند پ.ک.ک به شهادت رسید.
🔹
در جریان این درگیری، نیروهای مرزبانی موفق شدند ۲ نفر از عناصر این گروهک را به‌هلاکت برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/441989" target="_blank">📅 11:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j02o31zF48SIRl1ifsN7JQ7ZO2zGJiK7zSN-twVUx5cBk_sONJaK6ogiPqHJ66_SeiHIGaUWj-ObWl6vhm2ozhplCc2fc6wr7-Mf99nPO8sSB2EpPSA0OZNQAcD-XuQ36ooia7M3gJq1imBdFcwHbaleyA3tbcLIJ5ud_P-11BVW7A0jko4cpEoJmreXx6Tli20jl4MEiEnEax0TzpnaWHaDVoqmF1fICBFpgNEh8vGHe8OM1ha_7slfitNpNXyZQ55qRqyY71Ynpsi6oC74V20uE9MBIEex1ti6g6p-xoBE9u_J39-GiwT0b4WQmRey_YryChFpdK_y2ic-Xn85UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه شهید شوشتری تهران افتتاح شد
🔹
قطعۀ نخست آزادراه شهید شوشتری به طول ۹.۳ کیلومتر به بهره‌برداری رسید.
🔸
شهروندان می‌توانند از مسیر بزرگراه بسیج، پل هجرت و بلوار هجرت به سمت جنوب و بزرگراه امام رضا(ع) تردد کنند؛ در مسیر برگشت نیز امکان ورود از محور امام…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/441988" target="_blank">📅 11:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jY_YYP93Xp47aJbFiT-vBjIBn7JtuUOsbTrLNHSFOnuXKm76mkl8lj-F_ecxRd4rS_ToRfwki_4qCqncF9-bWfI1oH1wGaNdtDXbzuAHUZ5eytt039rEPkrZn4Z3qVCdLdlBPSI3MGbUmzI4Knci1au05VkmL0F4Mo2Mf_sG_4G7lDRo5gHELVydQnGstrnjJR86HBUlog2ET8q1sPRoe7R1wcOmqHU_BrqXy-VN1dyeefkTAmO92uKfKfJLZ53ohIpSabKTd3IQrxQr60QpLxFiaRs-VJ0igLh-YG9jSGekdq95LS7-NBMPif4KnsQk6XB_OAEcTdWGXpepsdJTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعار مشترک هیئت‌ها در محرم اعلام شد
🔹
سازمان هیئت و تشکل‌های دینی شعار مشترک هیئت‌های مذهبی در محرم ۱۴۰۵ را «در خیمۀ حسینیم، خون‌خواه و جان‌فداییم» با هشتگ
#نحن_المنتقمون
اعلام کرد.
🔹
شعاری که قرار است در کنار حفظ استقلال هیئت‌ها، پیوندی محتوایی و راهبردی میان خیمه‌های حسینی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/441987" target="_blank">📅 11:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ad505547.mp4?token=eWCKDP8wPQblqyM3HFpGBL0RVPEKNpDr1Wp_sD9DRsOyjinNB12qznzdlwBi916SSkMqdAgOypnH3nZXW6SiXjOnvCCQ9tygz5-20VQ9-stodBxTOOx1PPye-_gE1ZlwEaph6pqnyYIFStzMgjuFhqCVNfmpEgrC6_nZ-3V87vHFpKw7Gz8GL4ZOBAWLytXNXqtMs4KwsXyT8nAE1xSWDcghPKnV1UGhHCqE3z2FfNXSoy_w1L_blm9k99K-JuI0vgwO-qvYF18TnEuLcleja3NCEtPoD5Zo98dJrpx4tWQ8L8JHp_im-0pvauigNpwIS-RIenWe4UNVvuyazNkMNr5qwRjNhYw-_fm-t3VLBhPVWob0Ujw3ZaiBKFF8-UQrUno0QdFvd0ciFI21cQ7eaXCwLt80mUhD5Zn5Znut__OQV3wgqGwvDJG4WpJ9i50cgT76hnSRtVq870YrAR-5nx2tvyF95-4kqNB_typcOIYfZqpFnrq9-2G21CnKhFw7voK02cas093Y5TrxEvvUdMrgIittkXrQnJo0Bb7UuT0oZrDqVwaUfxnsg45AJrEk9Udw-3loH-Wxkj5IHDk5yWJVvA278X2DwcPfm3rDtGpGPL_hUPbcA8C6tqQdeooyp9vnX2eJWcr8c00Fxg1QurcInb-hpJgMbrjKlVQS0LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ad505547.mp4?token=eWCKDP8wPQblqyM3HFpGBL0RVPEKNpDr1Wp_sD9DRsOyjinNB12qznzdlwBi916SSkMqdAgOypnH3nZXW6SiXjOnvCCQ9tygz5-20VQ9-stodBxTOOx1PPye-_gE1ZlwEaph6pqnyYIFStzMgjuFhqCVNfmpEgrC6_nZ-3V87vHFpKw7Gz8GL4ZOBAWLytXNXqtMs4KwsXyT8nAE1xSWDcghPKnV1UGhHCqE3z2FfNXSoy_w1L_blm9k99K-JuI0vgwO-qvYF18TnEuLcleja3NCEtPoD5Zo98dJrpx4tWQ8L8JHp_im-0pvauigNpwIS-RIenWe4UNVvuyazNkMNr5qwRjNhYw-_fm-t3VLBhPVWob0Ujw3ZaiBKFF8-UQrUno0QdFvd0ciFI21cQ7eaXCwLt80mUhD5Zn5Znut__OQV3wgqGwvDJG4WpJ9i50cgT76hnSRtVq870YrAR-5nx2tvyF95-4kqNB_typcOIYfZqpFnrq9-2G21CnKhFw7voK02cas093Y5TrxEvvUdMrgIittkXrQnJo0Bb7UuT0oZrDqVwaUfxnsg45AJrEk9Udw-3loH-Wxkj5IHDk5yWJVvA278X2DwcPfm3rDtGpGPL_hUPbcA8C6tqQdeooyp9vnX2eJWcr8c00Fxg1QurcInb-hpJgMbrjKlVQS0LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سال بعد از جنگ تحمیلی ۱۲ روزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/441986" target="_blank">📅 11:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌ حمله سایبری محدود به ۴ بانک
🔹
شورای هماهنگی بانک‌ها: اختلال ایجادشده در سامانه‌های بانک‌های ملی، تجارت، صادرات و توسعه صادرات ناشی از یک حمله سایبری محدود بوده است.
🔹
تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات حفاظتی و پیشگیرانه لازم…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441985" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L10gMKTxTh1a7M03jd214DZ_Y12u6f61SrUZ10rop93zh1_odkp35FYFRAnJFhmOh57Cag91i3btZezrW5guCaBYhHc51fVhcqJfsRBaOCQy7h-ZnDn6jlhRpUORg2DeCNUjjl18fb_bidKHp-la0SAoYr-J1QVtXcBu-n5PvBZPlwKEER5qGDpU1QC2ipNWKpT522TlCAWGDXtZc5lGg3oL-ZlsJVWZXsmdB8CDv_o0-oCGThKBnghX0vcGkD73I4iMXXmprZGPij6PNJleLmv8NNqcNYuGtFjA7CxKNRcO6PrgdVZn60KzYJwxjq5cVvzLi638u_5iDwrqt6rrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش صهیونیستی برای ساکنان حدود ۳۰ منطقه در جنوب لبنان هشدار تخلیهٔ فوری صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/441984" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUp8i2oMHOrVTzYCSSy7VgvHgwjtfdrAWRBMJP6XHZxZjskA4NOsheoSDX6obY2PsI-qhLk0SavyyWKHlwlNGFuYWnHyCGgRwNSF3JYQBnDCTyKXAugcEkrT1swbeQnFOOJmwpHFQSTl3c-bp1kWDDWBEkbmBVZujTJc2uLFTJRfo_I4MdXw070xKsoL3c7pSX9CbKnBdbFTugIYPHHNQgbNffRuRrcdnXWWD34yL8IUU7n7xv-y68fJTGFi6LYuJ4r47_S6kBIdcsRY7Sfp8_eoLtunBUR3AL3co6jnQKlp-7prKkcvn8OuwPMplLNsCufE0Taag2QuM2JA-0J3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدحسن خمینی: تخریب مسئولان عالی‌رتبه کمکی به حل مسائل نمی‌کند
🔹
کشور با دعوا، اختلاف و سخنان تند به نتیجه نمی‌رسد و باید به خرد جمعی و تصمیمات کلان نظام اعتماد کرد؛ همان‌گونه که در دوران جنگ با اعتماد پیروز شدیم، در دوران صلح نیز باید با همین رویکرد پیش برویم.
🔹
تخطئه و تخریب تصمیم‌گیران عالی‌رتبۀ کشور ثمری ندارد و تصمیمات کلان نیز با تأیید و نظارت رهبر معظم انقلاب گرفته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/441983" target="_blank">📅 11:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده: ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد.
🔹
با این حال، پیگیری‌های خبرنگار فارس از منابع مطلع نشان می‌دهد بررسی ابعاد مختلف پیشنهادهای مطرح‌شده همچنان در سطوح کارشناسی و تصمیم‌گیری ادامه دارد و نهادهای مسئول در حال ارزیابی دقیق جوانب سیاسی، حقوقی و فنی موضوع هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/441982" target="_blank">📅 11:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNVEWwqoGeU1R__zOix3bdml2vSd3CXUFFfo__pDxdw3vDNQ4Vh09j_2gAK1R8dqep5ZsRHxf55JMgO-rUG-aK1cFt3kfHiGv3rvHLX6cFkTwoI9J8f7n37leK3bqQHAr2koln0ZrTM0s9iKJ7MjjTI6HXPcKZiWbb4JqN0ZB8soe8zZ0va3aXk_DWm1UVd-AZAPB0RCRC-Nzw13LFWqQrmVTKYo20XX135DL1iyNo5hfnqttiWgj0noNBjfsz9vAclUSUhT7QuflAmCLCuPqTLlpAJlsT6DdkO5yIZnz2E_YMsLh17NTp7IR_fKY1n7ZnMRbOY1wnnT8tZDQ2I2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اورژانس تهران: از ۸۷۰۰ مصدوم جنگ در تهران، ۹۲ درصد غیرنظامی بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/441981" target="_blank">📅 10:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60b6373b4.mp4?token=UkUXIyFykbv9OLtA94ETklUkF10f0sg29ES8Xu_y8FWkRVkt5W13v-rq75uUKi9n988rZkVyEGHQH3tI-l9rdkUxDmljuNRZ6cEVZFrDbx97PwK7jnip1iAazCVW6oZCmp6DbDCoiYhVxDBVYeE9vhtkvbI0drZ3EEBy1Ai7vacqIRoaQYu42S7lVrhNXjyaNp3cuKmevTEhX2jf7v_-39r8RM7cyMxQ5yxsh3p7iD5umGB3TBrDAP933jWlwhRp9jf0sZiuWmS06oqibxVWMZO-FsH-XosMGsQeR7XMEvZDwlBExLSnj5DDl1e0SBxpXGKyCp1T02b5kPCDteS6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60b6373b4.mp4?token=UkUXIyFykbv9OLtA94ETklUkF10f0sg29ES8Xu_y8FWkRVkt5W13v-rq75uUKi9n988rZkVyEGHQH3tI-l9rdkUxDmljuNRZ6cEVZFrDbx97PwK7jnip1iAazCVW6oZCmp6DbDCoiYhVxDBVYeE9vhtkvbI0drZ3EEBy1Ai7vacqIRoaQYu42S7lVrhNXjyaNp3cuKmevTEhX2jf7v_-39r8RM7cyMxQ5yxsh3p7iD5umGB3TBrDAP933jWlwhRp9jf0sZiuWmS06oqibxVWMZO-FsH-XosMGsQeR7XMEvZDwlBExLSnj5DDl1e0SBxpXGKyCp1T02b5kPCDteS6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقۀ کشتی در آمریکا به میدان جنگ تبدیل شد
🔹
آمریکا از سال ۲۰۲۵ اقدام به برگزاری مسابقات کشتی آزاد تحت عنوان RAF کرده که در آن خیلی از ستاره‌های مطرح جهان هم شرکت می‌کنند.
🔹
در یکی از این دیدارها چیمایف از روسیه به دنیس از آمریکا لگد زد که منجر به درگیری نمایندگان دو تیم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/441980" target="_blank">📅 10:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f0f2da19.mp4?token=e9bqwb65XtBsAY6k5nT6-ZR7m0JwV8XursU4iuiVICjc6vyOwr4v7YaPIlFuAYDn0nxwIZljav1h8mOqkMLHvXXfj7JocL1xG0YU2I8JVuyZiUHDN18MjhaFyc8HE_lVccxXLE1t25s7xhkb-V1EgQ5Bh3PobXp4qkgiZ9_bkmdBLTazryKobuqP5C-Y6U4cvNeeH1QQDvbTwYqum9Pckc_SSAScZ8bGgHWhZoJy_sFBjN97sPDGIOr67V-UmCoUsJX-efNjQSEIYiAOkTTiNWARQhQaFv3wWjhCMrnPSSMOefK6yaVBbNUTA9KjCFC7aUA45IzGz4fOX75biDSSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f0f2da19.mp4?token=e9bqwb65XtBsAY6k5nT6-ZR7m0JwV8XursU4iuiVICjc6vyOwr4v7YaPIlFuAYDn0nxwIZljav1h8mOqkMLHvXXfj7JocL1xG0YU2I8JVuyZiUHDN18MjhaFyc8HE_lVccxXLE1t25s7xhkb-V1EgQ5Bh3PobXp4qkgiZ9_bkmdBLTazryKobuqP5C-Y6U4cvNeeH1QQDvbTwYqum9Pckc_SSAScZ8bGgHWhZoJy_sFBjN97sPDGIOr67V-UmCoUsJX-efNjQSEIYiAOkTTiNWARQhQaFv3wWjhCMrnPSSMOefK6yaVBbNUTA9KjCFC7aUA45IzGz4fOX75biDSSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا در زمان بحران و جنگ اولین راهکار ایران، قطع اینترنت است؟
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/441979" target="_blank">📅 10:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌ آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
روابط‌عمومی آموزش‌وپرورش: هنوز تصمیم قطعی در مورد تعویق یک‌‌هفته‌ای گرفته نشده، اما در بازۀ زمانی ۱۳ تا ۱۵ تیرماه احتمالاً امتحانی برگزار نخواهد شد.
🔹
اطلاعیۀ قطعی و نهایی به‌زودی اعلام می‌گردد.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441978" target="_blank">📅 10:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8339d1f7.mp4?token=fKkDqc7rpUBkOJSissoLs9NKy3SAci-AeckJM7I8tBc9Tb1xT9RCO9NmJURsPh4hdByOoBZdfmP3OqjFbkcvirJjkBn3O628Cy2dLV-KvJKoqMKbgKrHx2TW7Te_BmLv8XSYUqa-hF-jm-k5lOuJihj6rNIOwnWXBB2FP6rZLY99hFmVn6HsyJCHK_Dj2nsdX9XjZq8L9imsz5HD9cxqBoEh2cslzCWYl4McflwnHXWvROneDWWvKxtUAqBsSAAjz0OowqaHXawAEkqcCp8rlhbdvAckeysx7lRPjqgHRtIf5mfF4sbWZgzEB8zHsxO_NuLbTz81eveyMZT4XzySoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8339d1f7.mp4?token=fKkDqc7rpUBkOJSissoLs9NKy3SAci-AeckJM7I8tBc9Tb1xT9RCO9NmJURsPh4hdByOoBZdfmP3OqjFbkcvirJjkBn3O628Cy2dLV-KvJKoqMKbgKrHx2TW7Te_BmLv8XSYUqa-hF-jm-k5lOuJihj6rNIOwnWXBB2FP6rZLY99hFmVn6HsyJCHK_Dj2nsdX9XjZq8L9imsz5HD9cxqBoEh2cslzCWYl4McflwnHXWvROneDWWvKxtUAqBsSAAjz0OowqaHXawAEkqcCp8rlhbdvAckeysx7lRPjqgHRtIf5mfF4sbWZgzEB8zHsxO_NuLbTz81eveyMZT4XzySoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از سپهبد شهید محمد باقری در جمع خانواده
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441977" target="_blank">📅 10:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3cy9qXIrl1KnIaS3OiYcJtvTzZTUfdG76YFmY1l0DVa7WsMvRpq_ako9mTLN8HcnbFKXB0SWolGDtY5c1oppzRCJ62aJ6BNxgJ-ZqjG4YyvsWkRrIr-m6cVVdyN1IAKoyYW95AxCdmKZlGt5Ml8uzw1bvATCQ9d6DW6BR-yeUelo16Smf4AmBEedVuST-mp5cvo-iMcNnJLuO1PrpgDRlN7XFTW0tj280UlRC9VIe1aZTEjRr9kG6Fu2g_oqnwerA2g5O7js9NtxYAIjm6HswTlQRQ3CT9DQzChSd5nj54aE758M5upg3RR_JBMNACVBHLgLJR_kd0DKvC7DN1EKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Up7P_64CUZ1g85Xa6znxo0DZkopqVofWkWckttGsValtTcIr6pARBKyOcy63iPP2fuLNu9uWANE3MvsAWM0akfi-vGx-KOeVoqL0cTBVivTFKJhJfu6S_773i0_47ym2xZAdgZz4z6uRhK75dJAoU7nIdntkKibu0KWrTGUctR3cz2-Gfw1l_6j5lWAYfpeHkVGD-L5iBHnbs2koZagJYBhKFyCg__L0Jt4k8eIBk1haRh-B8kvbXukg0DVB2lOZ_DCfbTEofBdTFhBUb9r7hp7lkFtFkjDYXgxa6QLGfqdQjstAsUEcg_PNhEoy4ukGPZrQmLoArM5MOM677q65HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1-jZwRMEr_eZYwQc7I8tbRAzC3yA3v06TSyqc1nwJw_ESViUCuDSku2CyykwOQ1b8p8sbXAjlCbPI_YSbJmgoA8mQuJm7k_UGUXNn2wW_5LFLOBvHJ5FGdlCKBRNmKAabjvfMc78XzdYQeOyqEvMKNC0IvMyOhnq86LVYs51ZZm6tnSXdzIg1wtKkwQSi5PGj_w6pcY-cRwiOzpLIh0WgjgvZRUvz7EqB5TnpfSpYTcbuIBsnnCWw9x6QY72FzJnsnO9pT-4ePsJDVuOcmfhqQSOz-iMLyQELvFmI085HwP2Zp9rZed9CcnwAiqiIX0Co4823ULKgXB3Mru3IhJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLAYdDFtwMb-r2xMk3IfRwuEH-SPz01La3A_eCBKR1WbUwuMKY-7jv5Pi9jvBYGWoPBEDrMrA7NczOJOyymqykGcaXuaX4pVl8M70WMRhR7hHmI0-Ma0V3129Q74ZXYa66t4hz4JHeFdZNUctutRy5mx-vhATMIIXX2VqGaNrPyi5PTaV33PTe6fCYVYgeB_gKDT-1cUrOi4VTYAvSHhSNbE41PcfiLSYb_E2g5jutjoOCwE_pKKZGJrokydRZ2ldaVuTUM4mgHQcr36n4UQB9_XnPeQ3YdwvzdTa6LPLnjQPRxcwk4cwMRpAgusq_43a2o2KkMUYH-gD2HNUy2o7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXWqF2MZHhoF1sZbyhAHl2db5NW6FLdrMGZ7X0FY76mcmr5QF_trJzuF4oEJjOgB5CL0jGzY4Hjji2h2ZTMEujkxsOzf-_2Diu5HiG3E5B1vG-_BJyy0LLRv_MerwwEOjHgIJedmojNczZXxCZSdtIPuBqwWKnkZR_uRMg71gVI6RYCA2S-xAP7Hz0nK5ffafaxH-m9TQC6FcjoSnLvf98z4XJ-ei5jz1hhqD0jg_j9lesXaZxbw9gm8-Jcnvt827ycxJVVxVgOMKHHofgUzlqU2Ya2EQow__1_807Vf30YmP49QZotwrsiJuIwjud9yQ__exBjT9_AnTDuKCsx8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKSvfTyO41s_6mpqb4A2NCjUToNmc3APrFKIvVP0XIms0Y5org-FPyXiEdNiVQQ6O_KzlBASiLOC-Kfax9--8FSiEIM-uHGHjuYacRmwg1omtWzDFzkCkBrIm713VpMfiu_IEgfz-quVprBfMM3x3nm84eS2bD_QyllM8VGiDWmolopd7ozwuVsBYt1LKXUVkqnP_Hee6zlFHo0DIPkG0GGTWXkdf3cLfst3-YOwZCXWxh9B1NoMRhkXNVa9WwbNCoYGB_YHCoR9IqacYC3UBUUcFQa10bm8gZ0I52j8WNjhoGKnysd2pKnsHzMrrHFhPLQ3yfsrl8M8eUVnww1P_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZJZOJLIAw2qOyCm4MtCfkKZCr9k1dcUW_oFmixMXKcspVfxJacFOZAexnF_t3-uYNyRamElqH0DTe9wyBnKYTJcVC--dhKlYsPKAHXk9rAo0tHVJWKoPrGIu2f6y-Wy6ioce6IhKUop_YOYzWNe1C-cLcemvMKxdSJaoeSWJxuMVxeFIMU9jPoc2qk1Xzfslzy-_KhuWNVCXuJldxJxHfT1pM6nVXBx6dLxSdacc8N40s9lLpSvpQdIHCtl_uMMhMF5SsK0NfCjAWOElIkRUJWvdUM3DS0DojQb7OfCeZJsOqxM9VzHr1MPNdFemoPdwPMUKIHNI5LSBVWIrMSNoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غار کرفتو کردستان؛ شاهکار باستانی ایران
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441970" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f835aed46e.mp4?token=BPtKIjRIwc7BY6WQzS87InZqVU3ADHPzomrQJO8_aMeWi8pV_GFhksUMWqtENIF7OhrBI4EIRvjm5DwAd9v1zccMpwU-B6972z0XH5T1lz1KlicM1w93DVpQAXE52Bkrd3-3ovBW_DspNuNe9GlKatj8D4ofyMl0h2hZJKTls23cH-ieqEH__arx6WO9_15IGSz1audlPKmf-X50gyIF2GDt8b1bG2bFtfUuOvzeRsc4ZTywdWBf0c5AqHzm_ZYEkG7LudVDFQ9CH5InB8ZoA3RAgO3ONZ8-CpkRLkM8plArIj2qXniq9Uo_UacSmfuVO8y7py9xFbAolUUOGbKbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f835aed46e.mp4?token=BPtKIjRIwc7BY6WQzS87InZqVU3ADHPzomrQJO8_aMeWi8pV_GFhksUMWqtENIF7OhrBI4EIRvjm5DwAd9v1zccMpwU-B6972z0XH5T1lz1KlicM1w93DVpQAXE52Bkrd3-3ovBW_DspNuNe9GlKatj8D4ofyMl0h2hZJKTls23cH-ieqEH__arx6WO9_15IGSz1audlPKmf-X50gyIF2GDt8b1bG2bFtfUuOvzeRsc4ZTywdWBf0c5AqHzm_ZYEkG7LudVDFQ9CH5InB8ZoA3RAgO3ONZ8-CpkRLkM8plArIj2qXniq9Uo_UacSmfuVO8y7py9xFbAolUUOGbKbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هشدارهای نفوذ پهپاد در چند منطقهٔ شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441969" target="_blank">📅 09:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuwyt5J1ycPSG_nikzoAWz4Y3_VrY7TBYPBwXNgNzYMJLz_YnmlqU1k2Y1Ftq2XoYpN_WLsGy7E45uUNFyO_bYICQt0A34kJicHhvzzcSz4EPFcN-W9saH08ZaQtuaHfd8prohN1aOUf2xLaiFXEMHoDvUGkdjiTp2_DdtS9MKhAgWxiF0m9VfuMF9KVUyP51w_XBmytXCcLANdWJ7LpEBEGUqnND49Holpd7oVReuBcDwoiI8mGY6mTXblWnoMWFe07H9RyVw_LxuUfq29_Ze7S4cBRf_YdEFD8ISWu71V2C6f1CAbjtQ9ee9LKhiYzj5yMVo655xyQU3KuSgmUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استرالیا با شکست ترکیه همه را غافل‌گیر کرد
⚽️
استرالیا ۲ - ۰ ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441968" target="_blank">📅 09:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPPTXuGk_zQjo0qCNhoFXiNJmIQmXg-2BQuahjLSNi3R9UtOU8TbW-F5Q4wLYyKm2FR7iNwp2Yldn_aBixEvbEaXkrLubU9KTj41P6NsGhiXgZxuXM_C40sCrwthr8qv7oIN6E2Qv53af0fOLBHYzyxUzqNXhal-9PNtdFb5F4jO3AvSycvNr0FjkPxyn6mHWBBqrzNXidzK2yQ5n-YK0udswB6ZP2nPV3OP_t_3mKVotroT7LXVYOtFLbGjTp--txI9Z6pz0N8B67d1keXbOJx8GiIOves2pj4Ece_Pc4ZGE2LsejNjoXV8b6cTZCx-oIhLPEjbNDKEklfgL10KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای نفوذ پهپاد در چند منطقهٔ شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441966" target="_blank">📅 09:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugFPVGZM8NJmzDcvAudJip9hhbqrSJeol9hOu9uXDm7NAgV_cVfWiW7hENFP-FabyfpWcVpFUVnWbayaD8blIRTSHl6hPMmSt31F3LzxUfLdbZ91VbAGYlB7bT9VCDI7iy4pD_F3DaRzJ8CpNxrafcDnombPVuZBIKqdVbNoTuyGe6tk6tSA0mePlHBUmLJ7bE8nHVG5AeafR-ZsYfAAne9AB8ofMj8h4dCGJlROvT_oo9oLPJcg5JwkVGsqnxvGpQPtxfVnF6iGtOcuv6bxCoJP9DVSGvZYA_mQ7woIk-0a4z7feBQUZpzArXbFPlI1JGswAyLWXab1aNHa9z0_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEvS14a-TB3M9bHwQKH1IAHcrtR83_iOqGVLKoTLL92iF1oyGg1i05CQNJywyM_LfePJKwGW6Y9i9wxZbuZMIClePF-8mY0vgGO4U9FFEodSGqAXdSjxzXKuMzsSNEJkZMXsiMGw2hYDLSDPNCoh6niodhrHrHPPI_y25S93rij-tMAsiAjWkw9qaaNM3TZfZ0Jvz5BuUl8--jRWvy7v4UBSY2-wwjzLKhcuiKZXsYZnrTDSXRndOn3pCibOxvwqzZU1WWazwhfdd-_Lb3vpedonxWG_Yk32_DwS1yNZEbSyO8CWfvo0IdpKmUKdeIoSFOPRY_FJ45Cgzjpg55Ao1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تاج در گفت‌وگو با رسانه‌های بین‌المللی، یاد شهید ماکان نصیری را زنده کرد
🔹
مهدی تاج در حاشیۀ تمرین امروز تیم ملی، در پاسخ به سوال خبرنگار نیویورک‌تایمز دربارۀ نشان روی لباس خود «میناب ۱۶۸» گفت: همه می‌دانید ۱۶۸ کودکِ ۹ یا ۱۰ ساله که سر کلاس درس خود بودند، هدف بمباران قرار گرفتند و همگی به شهادت رسیدند.
🔹
از پسربچه‌ای به‌نام ماکان نصیری تنها یک‌جفت کفش باقی ماند؛ رسالت ما این بود که تیم‌مان با نام «میناب ۱۶۸» در جام‌جهانی شرکت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441964" target="_blank">📅 07:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkdqehdObyHiG4uDdMYWC1aLgCSuGzSS4ijVpZsNRlb53K9pgP9TCc6Mtn_Llo5zLMkXUS6RPIN73fqaLNjgNJaUw4-IDGWzDbZX9hj7oLgXdFdBQYhBBjpQQ4dm_talRnzX8oobqx0BypBL6E_77PMqfBsZwhXKVwXN0Y5r6-zSjNmV68QsklPCyyKksxAtRIAnGUHuY99cZX1MwymEeG3XUQi6USxxurzfx2J91iCClruqSAUIuaN-oZypBivmQF6i-t27gzDvFg8EYXHFhR1YeQ8NE1j5ToHfgwyrqu-OyMl7RLDV8eYjQanAnmfoIn68q5zakbIRDO-p6zUaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایۀ موشکی تهران به واشنگتن: ارتش ایران نابود شدنی نیست
🔹
سفارت ایران در کنیا با بازنشر آمار دقیقی از انهدام رادارهای آمریکا، ادعای «نابودی ارتش ایران» سنتکام را به سخره گرفت و تأکید کرد که تنها چیز نابودشده در این میدان، آبروی ارتش آمریکاست.
🔹
بخش اصلی این توییت، افشای آماری دو هدف زمینی بود که به گفتۀ ایران کاملاً منهدم شده‌اند. سفارت ایران با قید «واقعیت ماجرا» نوشت که در جریان عملیات موشکی ایران، دو رادار حیاتی آمریکا در منطقه به «تلی از آوار» تبدیل شده‌اند:
🔸
۱. رادار ASR-1000 در پایگاه هوایی علی السالم کویت: نابود شد.
🔸
۲. رادار TPS-59 در بحرین: نابود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441963" target="_blank">📅 07:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌ آموزش‌‌وپرورش: ۱۳ تا ۱۵ تیرماه احتمالا امتحانی برگزار نخواهد شد
🔹
روابط‌عمومی آموزش‌وپرورش: هنوز تصمیم قطعی در مورد تعویق یک‌‌هفته‌ای گرفته نشده، اما در بازۀ زمانی ۱۳ تا ۱۵ تیرماه احتمالاً امتحانی برگزار نخواهد شد.
🔹
اطلاعیۀ قطعی و نهایی به‌زودی اعلام می‌گردد.…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441962" target="_blank">📅 07:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمال تغییر زمان امتحانات نهایی وجود دارد؟
🔹
رئیس روابط‌عمومی وزارت آموزش‌وپرورش اعلام کرد به‌دلیل همزمانی برخی امتحانات نهایی با مراسم تشییع پیکر رهبر شهید در تهران، قم و مشهد، احتمال تغییر زمان برگزاری آزمون‌ها درحال بررسی است. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441961" target="_blank">📅 06:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDT95BX60OFMzsvdkia2Z__8Zl5P1gGgnJteuoOOtqfzkyVZC7BematBFxmnI0X6PyWp8h0MoN7lPX9pgsi7zAAiq9p2oaI98gx-gr2gMRBiXdKpo4Mn9mP3u4i6Z22JU7y1vpEMM5wSdGekj7GDkV_F6aWTVXs93fSTX7UvDuJHFpxrlh6MAzx1aIrs7HMBZj2JNcus3V1FI4JkWlRZl-3cj8HGXK99BhJDuZvLE3lqXZCpZL796htIFu6fLYa7qzHy2ZwumczjrkMTCkxOsQ95sDcoSWTQaHxcCHXU7hC1-U2SFem1yJNpRHzQ_IR3AGHVg3BvAfN9YJy4aqTbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسکاتلند با برتری ۱ بر صفر در برابر هائیتی پیروز شد
.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441960" target="_blank">📅 06:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f558957a.mp4?token=sQ1cLNAuSKjvCiHHp5eQ0VmH9Bxvw7ilFojvRYfQTXc39Sr0K9GzVkxFfI15C28NRcCGTDjoXCrKqXU8Cu3UPiTLO8B5yZXavwY92czNWTTFZkA1v7xlG6LC04g6519CGwh_m_gTAxh_e76svMzpVYrWC1MFeyxsTp_HBUP4W62Sd78ovSZHMcOMqTRcVkpi7AoIZ9rFl7I1VjATHeewRZHVhORU-STjHuVgqL6_f5ZglvKxZQIINPo8IwRYJIPri42nFUENN27dGf4oeC8lhTpiTgo4aRTnh_TaSgunvk7r9rMpr_rt5NVUen7NyTwHHSV8kOSwhGHcCx_wDXk_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f558957a.mp4?token=sQ1cLNAuSKjvCiHHp5eQ0VmH9Bxvw7ilFojvRYfQTXc39Sr0K9GzVkxFfI15C28NRcCGTDjoXCrKqXU8Cu3UPiTLO8B5yZXavwY92czNWTTFZkA1v7xlG6LC04g6519CGwh_m_gTAxh_e76svMzpVYrWC1MFeyxsTp_HBUP4W62Sd78ovSZHMcOMqTRcVkpi7AoIZ9rFl7I1VjATHeewRZHVhORU-STjHuVgqL6_f5ZglvKxZQIINPo8IwRYJIPri42nFUENN27dGf4oeC8lhTpiTgo4aRTnh_TaSgunvk7r9rMpr_rt5NVUen7NyTwHHSV8kOSwhGHcCx_wDXk_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط هواپیمای نظامی آمریکا در ایالت واشنگتن
🔹
سقوط یک فروند هواپیمای نظامی در منطقه‌ای جنگلی در ایالت واشنگتن، به آتش‌سوزی گسترده و تخلیۀ فوری گردشگران منجر شد.
🔹
طبق اعلام منابع محلی، خلبان این هواپیما موفق شد پیش از برخورد، با صندلی نجات از آن خارج شود.
🔹
علت سقوط این هواپیمای نظامی اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441959" target="_blank">📅 06:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a18TSaWwRstszt-u29Ivq2WEWUOPYKThQWb3zdFO_EKzKEp11hT_B0Z56NGj_h61Q7R1UaXOq5ZVWSqPeCqJ94p8uKyChjlWuLiCvTL0UJ7xAyhs8E9IyFU0j0p2gpnOYST_oXW6gmmUe7fMH7jbfQrA8C13rRTiKPs9fbwUF3xTrG6XTJbzIUFZHl_-8zpgbhl3pE1dSpd8w4EYD57ZVrKqpNqzVZV4R-w7z_0VbNozZyfitxqIKcs9DdwZ8oxODehC4jRx-feqYAKXdcgZoiP2XA7Qm1tb6S5HOy6gz6qUarcZSN0hD7fC5o-vaPHY2B7zuBkG54ULROJ28-OLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۳ درصد حجاج به خانه رسیدند
🔹
رئیس سازمان حج‌وزیارت: تا پایان ۲۳ خرداد، ۹۳ درصد حجاج ایرانی به کشور بازگشته‌اند و عملیات انتقال زائران در مراحل پایانی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441958" target="_blank">📅 05:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما از ظهور مشکلات خودمان فراری هستیم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441957" target="_blank">📅 05:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441951" target="_blank">📅 04:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWTOpr7yny19wNjow4oT8d66qQ_z2-n58KNS9Wa9vxCqcGz38qJJzdobOL1-0fIJXrH7fQj7Om3FPJapd5U7Icx2HS5TlnUx4irYDvd2ChBkbwVhBEkH414dkcJtEd6ExRuDFzq_o9f5wqgl1_KNu8LThF7Lvjpe5mQqS2KpSTeAeJpI-xbJV6uMwIV4zqjS-TdGvxsY3GvWD1ewIUmZ_nblbsYhJ68dv6w1yyhTAYvlfsl7AMXSMAMd1P6rUAnvbSgj_YL9Pq-pp9rwXnt3lWSjYrlVQ8H4BkFSpdCdVdSosa6UmdKskJZBymlzLC5wJrrEm6R-XmJYTNAlePTj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441945" target="_blank">📅 04:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLskYtia2cuqzFab3cL55lEsqWHDKd8uYg70H8dPFYpEOnHMOcMoTgeVqJWU6o7nob41OVmowDorXON5zqQzFlJCSK5SbdwgI_ruStvTj5NK0dve9YMIboFps0milOTRF7qAE4tSEJfnmIW8aMikcvDyhMh3a6t2LRMERW5ypApfo2ks452eFGHcA_nn1RleD9E69nQhEUfvBYretnW8aDaylnG5NoSwYfbnwumbXarRBosRaVjiGL1M-NhAK6V8_9cgBVOhOOVqCiF9ToVdHXA7pZjUcT3wEqC9QZoQdSyPOiR7jY2Uu6hwaKtHDQCEaWe21-sSaR_vUD1qNQRElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
زور برزیل به مراکش نرسید؛ تساوی در دو نیمۀ متفاوت
برزیل ۱ - ۱ مراکش
@Sportfars</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441944" target="_blank">📅 03:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
رسانه‌های عربی از عملیات صهیونیست‌ها و انفجار گسترده در مناطق شرق جبالیا واقع در شمال نوار غزه، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441943" target="_blank">📅 03:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37D1ivVithFzgbJLWI6EIi1Pi1F0WmVsf1idsvtVX4GCFcNrvY4IiL_MnBgFuUoag6bC6LhAudAGAlK6nw-Jn6dP1AbrA4PmKRh1Y3lzoklvN_N6-yi9vSJbWYQIqJ8Tpu4k_xD17n-d02p2MDd2FsRyQVgOKuTAwYkwQNPmdpCV2CWEf_OO7iSQEAJQ8j68WBhfXhIouGdJhJ0AHpqZcoA6JlqOa5e3ENBEesUOdysWA8-LVDnm4xVTI9m2qs_-bLPuQFd0L1rRBOBUOaX9tKKmC794pAdJ3C3F68OtQnNZHXAKAqvgnqY3ANq1te4XOqAANDrjndQlnSAn3Hs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفس ترامپ وسط کاخ‌سفید برپا شد
🔹
درحالی‌که آمریکا در میزبانی جام‌جهانی ۲۰۲۶ با حاشیه‌های زیادی از جمله صدور ویزاها، سرقت تجهیزات تیم ملی انگلیس و نگرانی‌های امنیتی روبه‌رو است، اما دولت ترامپ به‌جای حل این مشکلات، روی اقدامات نمایشی تمرکز کرده است.
🔹
تازه‌ترین نمونه، میزبانی مسابقات UFC در محوطۀ کاخ‌سفید است. رویدادی بی‌سابقه که با نصب قفس مبارزه، صندلی و سازه‌های عظیم در چمن جنوبی کاخ‌سفید همراه شده و قرار است همزمان با هشتادمین سالگرد تولد رئیس‌جمهور آمریکا برگزار شود.
🔹
از نگاه منتقدان، حاشیه‌های متعدد هفته‌های اخیر، پرسش‌هایی را دربارۀ آمادگی کامل میزبان ایجاد کرده، اما در مقابل کاخ‌سفید ترجیح داده انرژی و توجه رسانه‌ای را به سمت رویدادی سوق دهد که بیش از هر چیز به نام ترامپ گره‌خورده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441942" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات سنگین موشکی حزب‌الله علیه مواضع ارتش رژیم صهیونیستی در اطراف شهرک «مجدل زون» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441941" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
در پی تیراندازی صهیونیست‌ها در خان‌یونس در جنوب نوار غزه، یک کودک به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441940" target="_blank">📅 02:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgbH94W-Fb_FG7R23rxpK17NxSIFKQzQEC5r5iSHWV923dMkm56mG29Ic6vAt0AsWqfCPliEU2xwptos2lHipNDIb0tm4r9ZQdf_l-hN46KPlX4uuhHU2aA48SL9VGqXUlFSZtT1qNR0EgjlOsztPo4vQKxEOqKC3tp2WwmNhLB2mcWA2L2RYjiP6JkfObJOZj_Jrg3WVtAGikgWQqg9cngiZtdSNN5OOpOY7CQHZP5VeHKPGoGpF4Z7L4xdkQdDjTNH3G2Gol4ZzFYMutjKL9BPp3J_AI3zzA0QR54R7x8O_eOYrW2AzlhAGiCUGQ5yIWc6p6uNMea1Au7wvrX0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJAedZR2PrRpDAUdPfvmF_cjSrdZHxBm4IBUR8F9gmQirbJbOB4KrVDRRzN36wo2UaJbp2cZe00j3-X2uDcKME8GgM-3_hkNexvyuxnizk73ZIYNFjzqLy1pn4IX-ABWmkuWUeiJbFw9BF3-0QQRpfr2UcrTDUyIYg0YhkcE2InmhyIArrnWaNOTpf1aScJUOqM-ylhzFiCs5C05E_soOHX03EILOdjPEYAt7KCiTCRKKeAUMeTN7qBzA03QuHB6lYWKkWmpyHnlLYWV8AFm0rWA62PJei5JunZktgmq_Hp7eFx0UD0Oz_oHne5GdvNiMGIxdgzR6mJQYtHYsoqJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muzq1tYhk0R4KaiQmYtbFO2M0Noll4v77S3VBgLuMOBOGx38X1jXMJhPNBMwu-Wxl4M5FrBHLxFL_TxruHXljfwZ0e2w-ESgr8TSsHnWIfPad_-f_EtrUTj6ZHLR9Y7i5N0-ZFW8K01kt8WGErN5OCU-bxHBTPEGx3Sh3ieLGS2ZDzl_1E89uvMpXs01lrPU6zwM5jUOZFs84p4YctOx0uTGImubw85UUIkzVPpu06zIx3CIBEPbNSwcwVXx6VSMCZHMcJ2tZYqOv4zTeFZJ-VPDxCiRqD3umBGRYxUY51VwZKnK-rKcSbgNdrkNUeENxKJ24_auqFhROsGK_dRfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiuM8K6PeQdzibdUiwg817oTeyr8QnLwfWhi3R_VvAwJmD9P4_DmTWY56sYyATrFQElvA8Y4VS8EPHgeOoR39Bj_J0oT9_viPpkwXhBSfgehGmHaTT_B8FCEm3ac_izVObJcfoZHnBixvQ0uv9vGZC45SCoZg88fGVDuY1X56umGghuAePbE5Lbyk0VulMU9v7sAC_LUkmjeVrCjKpQN8zPvKMNtOTP1GgCePbsZ3kRvPYx3OApZ-Z7tjMra142hSCWQBhh1wpc6ONNr0bqk7Rxtj_li9ZBIfFkw53mZlOvY5RlLhYhCp_F_ij6irEzU9e_IBb3GdQJuEhzziL65qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_5__EfyXMSA5FnEZ8F9YTAlLRYOTZdf7piQF8DmATwWvQjKmhfurXSinufpYtYEUqSErh_Ua3RB4nTLceKCPa0ZxIPUm0y066926eXGPxKk1VccdkaPT505eB1nRc0BVOYvqWl8rV3mLgt1n9djN56Rs0QoZdmOE0E3ms48wQ6V_BEqplVyW-Vx8kjOFrusP6jG6H1UOy8GIXlQcF8sOsy9_oEBIkbFkA1NqkmkNi9NWlOneyxhm3LIMU1Rvx4ZOKCIkkox3mlgwp0L_eYREM7EHA2ij-JiXYZn-h4dkp0ok1bTwjZxLklw7Km5_ay464gVWatpxksep2CPByanbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COHbylfNfcpqMFZk_oN2-qr_IXhnNWE9At_ne5WwRP20T6hFNely9DtigIeKq7Ds18Ygj8Kob4W1bUY3kGSIqrkfOXqpYFdKpNM8Alj0-tFPW4nQRgyPXDpehuNOx6Ol-zRLR2Iga7C4kgxoq9jRwcWAe-KjVJldzjyGDT2WE46y6nkhQDDkW8BgHya6GB5L1IaTPsR8tM9ZOUR1OQ58IU_huMn1INyB7leOqm68nBjodOdQFnk6Xn41O5T-dGn81S1nrRY4oM5qiQ6vIkvw65S2oGTqTIJUb5yz__TknJyPEQLqraUSZ7EZ9BRGbfBblcRCw-FqtmdRoY62s7AGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpEkGbcJvUivLGA1vrQzYBVKpA6MT9rRn5Rsc-Q8GaFuMtjFfEbFKkRN-aqZzIWfp6SVwsuBW5U5dpzT5QsySOqiQcob4TABM0uDH0lxlsRm3QGbpRrtzaQo2DG4SrX4GAK72_Ud9Y2Kr-viON7OVI263aPzOK3budhPFenr8_-uGA46Sa9VSxioFNiNSGAeRxSjGdFZvsw0qa8gEDYMvzo7uXyiFB-lUtz89gPTNuYm8jWJmQJ1Ot2rEG9swZ6612Gt6MRDYxnk6e_kCY3sgmOljt7__hjIFBOW9OIFiuEDyeZEWykwT27U-HBeuU_Ux5YuZvsKtOrb2FOSDyhsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA2J5yKOcV0sfmHxDj5Alqc4npRkT2ddThPq285iCp7Pv9XVTFf8fHPR9MnNYVSVhLr0YxGrcZ6eMJBYIo8tGmmx1OjvOZ1FanlRUuZ0ZJe4KgL-8dbk8aKAa3UrRX_jVjEm6Xie1ferXNDxShTDWMrWckpMhVB7vnjrrRJUA8euH1CX4TRdjU_uURr8fzShZWgdpTWBfkWChx1HN74hoku9MigwQnjTzphRmovtAQ7rgqBLB4Ajn7tF9dDp49Hasd0aEB8A_Tv40RpzfiDpryXeSijlaeHOEUlvNDKnlYRUVO8BakkLu-ThQ3J3wLcLqAQ4UyVmzBp-sgdE30ETBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاسداشت سپهبد شهید علی شادمانی و شهدای دفاع مقدس ۱۲ روزه در شب حماسی همدان
عکس: مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/441932" target="_blank">📅 02:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hesHZUR0wxnhL4cNLnEgIQbsAaBOxCkZhnzRZp6m1TsSS1y41-nTMaRckunLVIfXQYrKzcxgfexV03PtXV_4COBfxghYF8AojJvaVHbeN1Bwipy69bEhkIHNrNf6qkWHore-VFRxpG-UoE_VaokaYSAsLRIQXhlYokX194mHiPGiz0VhYohsSxSeCYolnce4zPVDYdrcSBRAkPOY3OJj25fmUIFWhoHxnG88uDU53NonNWeus-m4ICDEs_povv1Yder_ssFqetb8gruG_3wEaD3uzBOhNYT_J-xee44kmvllf63z3JADjXapRGcw_AHWA156cTS88y5Z1vJBLaf4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان، گورستان تانک‌های مرکاوا
🔹
منابع خبری لبنانی اعلام کردند طی ضربات حزب‌الله و مقابله با تلاش نظامیان صهیونیست برای پیشروی در جنوب لبنان، ۵ تانک مرکاوا در شهرک مجدل‌زون در حومۀ شهر صور مورد اصابت مستقیم قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441931" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fP0lxAROeJAd3hMyK7DvtjXZwV5fwtorHkhlaFrRRX8wbW0yQjtk7hITSn5ox_L3uhNXORPCTIrUkyX530AiFJPBEq8O-iVJXxob6MzjOAsj_jsN3_4BzUgnsUKMBbfHmM1Et8LXELuS2RLTxkZMm-ZWOyX49dp_q9B-oPfelujEoghaz06ldyn1DXrVDKA-4hk6ErlQMmVX1jDcN0Hu6mFv-HbTgZbud6v5ABGxwML7OVfzK7gl6aXbnx52R2vsE0PrwZ2aND_P71uj68PIUP1VUODQref7Rff94BFQgy0oTVpV-7lJ5wGowzExXprI-PEPx0WHr24-nu04i2IfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afdX72UnPSRqL2aW2ZgVpx5DewKEGdalP4WlgSD4Sjis-lyrGWVpBrZoh25SICWdmxA-uiUJQNdKx0CaTNnIahE8BWkZcRqqdPeh0JQz5Jz7gsX4GLg0VQ-6C_t8MsDQtH6reCM8BF8x4BbVWGpBMxIenmUhxBfVo3eq8LIZDUPZZhSTfkChVejyLpuUdP83lvR0xIFBmh54rCskVi1xoU0sH1VOYjZZOEBqf6sCuU70PYrzB5T7iQmg_CNgxceyK1BhQYonU6ZN3woz8ebH-6xgv4LZd9sEpGJGmQGnB4LELlRh9a-WazsfYKkK01Oz2ZyxEIOeK3sUygkKjUYKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFeLmg3e8Ethn7Z1Lu6DI_t3HBMF2nNgQwBopMHa9jVnWSGEfAN5_rGtLFYrga4JVS_O-TxX75L4gCDO0dYCCg18SfZqTKnV-JoDndAvqov_0xe9yQgQdGQdmqJquUI_6b4-EGUFmIqNj9f4k-HlMoqZxT7O3CKZqc2TbwziWwH9iINQxhmpQzWEvg8LCBYAscpsPPpj59AMigTNmeVt07tMp3IDRm8eJh3CBNY-V1Q1F2976OVxlFMkC8YOYcRW9jpYV9nnaCtW6E3CG_lvc7lCQoC8Ztjl3y4SfMal7mwL2lhWMU9Z8Gc60EiWkj_AD2NAWYbl1KRaBexyNhjwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFG40IuYvljIcyESediW4NDb42swZrnLtQ1mMfEoo0RjSmzCUfnyTjQCMjrHJO3Tcdg5cdefi_QA0bQxJwP_uq-uXtHnd_hVfQ-vNlY13zwoLBPV0D3W4oPa6rPnaXE_3coSqtYaE5uZCrAXM-yvl1wcjAWhrV6dipCZ7cBhvR79mngySpfbB9fn2wOJBycOpxzcpGjSZlPJSwciE9-ZehYc4NTJ36pj9RDebsDvSTcABOdSUnsTtsqsGd4ckGE6PPYlfnNrTKBFtonfIXyCxG1BGP1Wg5Ip6wJSR9nVrt8bA6kgQ-fPOTjF20yTDWE15kAMZqFdxFTjKABknR7ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SObu3lJsEPrUdkiOxua5kFpHrCpNCZgd4gwdqywXSMLuAmQPEc7WuvH7zN9T5SCimdrwXZ976vF1QzqU0KO3XhaXQvt_1c9u7_ttgggx4G-AtSnBQxWdXgex5lyDmUc_FVIMs2hj7ncnVXkk92pT3a_JyicbeFlS6iD3L_DuJEcYBf_4-fEydLippI4_TFublgoCHkVxiBhH7HC6PsubKwNiBpqSmsi5hAbQ_HPoeGrKjZbKct1Do4Vq1MiqeSfW0iP_aY0jNy178LyJngu_0lH5tehDCg2MqbFOgxXU5FfBQ-Mh5nfV242NJ0dEu6k5A2Ao3BFHg35COOgv8HtvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHrN0X1m-QZR3PUylAc0JZc3W1TkOVvhhUgSw72jtXxGfHOctYJnX3VGXexpzEdR-M6L7lBE51m0FkmdCTDPzfRcMe9WugdZYsKIlxu2PhVn7btxpwIQePEXdLF-fdFFRsfn3UqmfOYXtcBw2qr2L2qjzAfVirx9-TTS5uSS0AdqWIMkbHBDnqsF9Guy46q0AXc7EYLSXsZvit4pujsV01RAQQBuAwlRz7_dYAoG0zyyfMKYYTfrdp2dvspyKSk5vAtxQ8rWOV6xgskOy7MhURlnmdE84jkyQCV8ghFU_25qpX0Dfr0j45uaAAYpTUyNIhetoe8SA85yzEjqEn-FsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۴ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441923" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441913">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3-yfk3KNOeET42diCerPL_0BP6spVIJsu40LBmSXiMLNFeFPkMvvWRjRPxPaws_3VdCt0WsFTP-cwMwM8sqNTNZkg48vUxBs3yI3Z6ncP3s6H0JqzeFfOlhjHVwUrNZMFEoLrkSe393tCtUCljtwJtLmSYJiSTnYkS3n1FOwuIVSCGwEiM32EZQldX2wRZFlcpMJNLPiYtfFBU3bL3Ssbhnc-jOBf8BbdPniHRwLoIaqDfgf9xCgryFjblsYzzPHtAZ1qZHOU5SYhTzBxqZAqSbdc_gH7OglOEBtyWiaFUDHKsBJd5id2UH04Gg4SinXSHlBX9GleqpTyYqJYLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNhX8R3pszdT5tLsqyXUSiY1TN-E8TXDd2y86fXSo6LHrf6mQQax-t08RGa-xpgfZmC26n65aEdp376jcSpltbdk92yMt4vtpuUB1TCt29_Y2SzMRaxrZ22j_5vFIyTMqs1Q9BkfL10q3BwO6zkeZc3AbthrYOezAJmEJ2HC46Og8cPvidCIFDtL-sKcaQrI7ujT8McaL5n60foLAvXWIXm1QxUJ-0tL_mx7Ro0Y1kMNHGIwGEuLObIK6N3Mk6av3OWOWobfkUSb8FMlbc6C37ciwGP8yM_M9Vz8yeYcOpeLPaQKCYfc7DZWjcX9Lhuk5i3qvO9F9KAWskYuO0BAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL_BewdcMyEVbQje392MNLP-Z3CHxJUK3qZ_l3kCjNjSk1r2v7tjqfCf0TKTCFnSDhwz2NBWSyYIE78h-bh2hp255azI-quXIUMgImqqtdFOADb6V_VeDy2g7vjvKz3jdyy7TPVQu7pbHN5sCM8BQmgikCXQ6FYXAOmxirOR9sRUigLOwfbMiHLRy3HNIeOTskhC862yBtUoetwpaMlw-IMZ3uQ_GVp9TPcJIFw1RvpSusdqnKpYu5qwSsKtUtKTaqlUzosXEWT6dj-ylHgdK64_nOIy4f-zQS2ce0b2J6JnykX0-cI8EAwvbE9fXRNzrUYIaFjivqMRNihrTnxD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCIv5bf5TC2Oy1nBCCETejlMPQZZ85NdF-cWUTgacsPpaYdQF_kaYfqDQHr0_-lkWnOcJle-N4i9IMpsn0JoLKLHtcurRfoP4erLKIzmVYk-72bxW31u5S10CO-QdyNYKNvjjIMicx2owEZlrIufpjyQ3vCtnvDBcLTRnOaqmqkREb_p7iut6Pmfml_DLlCrzecZRWvipw-uJuOanO4lhEVbFQWqoXAmI4EveCIH5Y9Y3xnAUZnr1JaAqtS-vZwRFv71lZVDqYTSBEgFqPpqwKz9Hi4iKBYgqF7nLYLx6_QZGY0CYKuw2T0xYxVe6xngZepYN9iFxPdK6C45maJAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a00KH0GMOwFeg3UgsGihEETyzXBO8ZRg4KAE6mMzu0m1DO_ozqa6XWiITYr3UDuMdbClQh8-L-th5iO9BltKla6nkqP8IY1jIx4exhK5i9QmCM0cLcG8nBU5faZispt4maFOzfMqRwIUbmJB0xmt912nnA11stllNvBWt_tUh73UtuTcJsx23nyKiYtNXqj2ABKiIdytl6A7IhyTQ4TSqyS92UYGjMFuiSfp8C1macRuS4PLL1Nl9TW9faLLDTQ8EDEk42NG5y8MWAp44iQCurDBGRpnWFPm-9Z4wPKtmErZiANA-ruenVRnfXUGWpsyTu5SZzTK_hhPVnvDcaYYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU94-bqbr4FY1xc5GzJy2nsQDERAqbknI6lMYe7Ac6Ie1fpoc4Is5vbSwG12cRQUXgOp6mDvQPSERdA6dQZqO_s4Ip-P8813FN_23mh59sF1oYgKC5fwwQKKcqGMUY4b-C8JsTtruoXb-JbBLZ4L6XC26mh2dynlYp_AZZaUDeqvdYhab38AYmoqBuGeXo9sDbU2LjaJ_ERuSLk0bhg23WfRMtNrG9gYWP0IFpKdp_pGL3mQVlm1SL95r0-7r_atEu0Mgy_qAdGgQKfCR_A7jaIi3HA91OS0pMo_8jpCRU3ijCo98tzBKdV94M0oKCz9TjE_ZidlYe0VmTn1s6uNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ondJEo3SBKentoMIb-rMTh4I_2oMceydrICcj1edln8WAe_1lTdZw1Lnqes76nSEiOmS5e2pqTRM6pLD_1L_DCqUjx2XqsR7ZRx9u_6riIn3ppNYnKKRmkbubYzBYuYsEHVmok2IfyQAfU5T7JXpWoS670ZzGkEyW5plbqdkOU91OldGhYfJAjAYp6jZkDD8DAWkWG7S1eoLBPpt3Wn49O8UpCM7lEtrfZhUPwJFgtWHdwEyhVgXVnlK8AMXZTo1JYJpTexoVqA6Je7RM_S3W0NvuLdVXTo7d74Z6RcjwcKGJDg2CzWHdfAIrFGkPN9k8VL5AHO8TCp_AXx5LOeY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2dAQOYO9pKSUof0dHS5s5T-etWFxn-fL6s7xtszz3ClbEgBWH0561aDTJvHGmiYPEnBML6zEt6SlLWtGBv4EhIGl1l9sgxpBpZuxsaImqp7akLI7uZ36S2n0oQQyyVIhxGJNebMVZ9KtO2Z2DnmnMjsRY-EZXdhPua4-z99WcP5J_kDrAlVWIxWEgkblehRhRvpsucPDmOUCt69efWE4dD9Ah2nuxmJiu3dx5-cNDqGZWOpeuxSKsns6iKVmX-Byxu6bgh8OcYm_6pqbncbj7epApecAsyI4FsPCce4GH1u--cGm-x9W5kAw5KPLE96O4nlWMV0B9mQ9__BaTAa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdzN_aaq5dfK5BmFnrfj-QlfTC_txZVesehCAkVu9XwiAYCNA1OFU2m-WiGqvWwmW1b4hLYYRfLyrCByL4yAcxBENTjXmdZkLzFCkJFh7s5CZXkF3J3Bg9vSwiMHTbhNJs44fLJ7WZliJD1PWva8qu1Wf3cgfdudUOxYXTadLEGzQENY5NRiA9T7XtXw4lS0rtr8cssfMfc4oXjohJzhtIQ2dd6t6bnZQ6viIPSESrm-Bl7R46B2M0m1EZgwCfoXHw8hF-ttV3gE4sLZ_w40tIX3VuSZtAHLbS18efVxhcibVbaQ6dp85VTuYSxbc17snx1gBkHotQmlVBALR3GAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eG4DX8C1KH6gbmuWkqUVRw56DKahMfRddoM8zxH2uFndlKGSHS8w2n25lmQYX_9ylm1JLCdrDEjLyiUdkb4Fj6gv3Ha9cZatgF08YS7Q3FdfhmTA6OOieQIliXFa2w-Rr23V6V_L8uFU0aRK0p8roF27sKycYYehagTyK4n3WLc_wVD0vHQWcfCY5oLsP3UHXmx9Unu1dX3XUXNw2a3_xi9pSv-j-Jbjc8V8-FKk51P6PvT8yuDxd17NzsmE60XedklpErmRd9briyes07u9RPclsT0c5bDdXm_GJgctTolbVoCOxyKSuvsnqIcBzkyYPN5MDXP-2kHv_vxlsZR3cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441913" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441912">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۲۲ عملیات حزب‌الله در ۲۴ ساعت گذشته
🔹
مقاومت اسلامی لبنان اعلام کرد، طی ۲۴ ساعت گذشته با ۲۲ عملیات مواضع نظامی، مراکز، تجهیزات و ادوات زرهی صهیونیست‌ها را هدف حملات موشکی، پهپادی و توپخانه‌ای قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441912" target="_blank">📅 01:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441911">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
حزب‌الله: تجمعات خودروها و سربازان دشمن صهیونیستی در شهر مجدل‌زون در جنوب لبنان را هدف حملۀ موشکی قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441911" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441910">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHm80taDjMNHxOKrzFCn8rjNGhQqg4vYvY3sqhjQU-RWIWV6nNQQnqjex7ZP1DqOU1rOdHifag5f8kWcSWhJ3z7mt2UlAMABPjggEjcepZE0vR0X0KlbWshZ0ZoEI_SLCjwjWTpkTWUtmSAe8FcuW6a_647h75p1vW99luGxIMP2DNFseZJ42Buh7yyk4jmY-YSHZ0SVgPM477CWnuVN5I_V5y2nRwzbFr-PIbBYXqEjYWXU0HrBegsyVUMV0JpjkQbKwf0-mBNwRXViZpQmpckyogPb6hIOhfm2z8gbOZl6tZ7qj3343T8UVetd9Cv8KBsjS3uNNH15stHnoH4h_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پایان مسابقۀ سوئیس و قطر با تساوی یک بر یک
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441910" target="_blank">📅 00:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دلال‌ها برای بازگرداندن امارات به تجارت ایران فعال شدند
🔹
همزمان با حرکت ایران به سمت مسیرهای تجاری مستقیم با چین و روسیه، گزارش‌ها از فعال شدن دوبارۀ ذی‌نفعان تجارت واسطه‌ای برای بازگرداندن مسیر امارات به مدار تجارت ایران حکایت دارد.
🔹
طبق آمارهای سازمان توسعۀ تجارت تا پیش از جنگ، رقم تجارت ایران و امارات حدود ۲۵ میلیارد دلار بود اما فقط ۱۰ درصد این رقم به تجارت مستقیم این دو کشور مربوط می‌شد.
🔹
۹۰ درصد حجم تجارت مربوط به کالاهایی بود که از امارات فقط به‌عنوان واسطه تجاری برای انتقال آن‌ها استفاده می‌شد.
🔹
اگر واسطه‌ها فقط ۲ درصد برای نقل‌وانتقال پول و تسویه این حجم از تجارت دریافت کنند، در کمترین حالت ۴۵۰ میلیون دلار در سال برای آن‌ها سودآوری دارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/441909" target="_blank">📅 00:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
برخی منابع از حملات توپخانه‌ای رژیم صهیونیستی به حومۀ شهرک‌هایی در شهرستان صور و همچنین منطقۀ «وادی الحجیر» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/441908" target="_blank">📅 00:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
کاشمری‌ها صدوپنجمین شب اقتدار را باشکوه رقم زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/441907" target="_blank">📅 23:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشت‌گذاری سنتی اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441906" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📷
افتتاح قطعه نخست آزادراه شهید شوشتری تهران   عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441905" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خوانیم تا پای جان، جاویدان ایران
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441904" target="_blank">📅 23:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهتزاز پرچم فلسطین در بزرگ‌ترین میدان نیویورک
🔹
هواداران مراکشی جام جهانی پرچم فلسطین را در میدان تایمز نیویورک به اهتزاز درآوردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/441902" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بارانی مردم بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441901" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a44fe66cf.mp4?token=fxd-rCaJWu8I50bBHVMZpYmdsQvU1fQDE3pXXx84QtfTc5fdeOoA9sZdeKMiXLGrFZkv2vdqMde0Y-im-9eqKauf-LLD7RGuUQYigha4wlkZ8CvYUg6lzwvvdqWITpOCXY5QFWF4SLxL65vmhnRHBUxkoq3uAWXdxQLZnyJFRQJsFYsChmE5dM87Sp6o1c-p9FzRdEwQ3moLXQel2fse7k-valVlRILXcrWA4OpVWvqaK-eGJZ5_Ai-06P5jMXIRmrrjf72vGmCMF2625J1azHUWG4ere7DYfaOtKJmtyKOKhdasBKyaDyOLvTKP3LjKJRywcwuAsaY-OiVFndpVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a44fe66cf.mp4?token=fxd-rCaJWu8I50bBHVMZpYmdsQvU1fQDE3pXXx84QtfTc5fdeOoA9sZdeKMiXLGrFZkv2vdqMde0Y-im-9eqKauf-LLD7RGuUQYigha4wlkZ8CvYUg6lzwvvdqWITpOCXY5QFWF4SLxL65vmhnRHBUxkoq3uAWXdxQLZnyJFRQJsFYsChmE5dM87Sp6o1c-p9FzRdEwQ3moLXQel2fse7k-valVlRILXcrWA4OpVWvqaK-eGJZ5_Ai-06P5jMXIRmrrjf72vGmCMF2625J1azHUWG4ere7DYfaOtKJmtyKOKhdasBKyaDyOLvTKP3LjKJRywcwuAsaY-OiVFndpVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاره‌کردن عکس ترامپ و پرچم آمریکا در هند
🔹
هندی‌ها در واکنش به کشته شدن ۳ ملوان هندی توسط آمریکا، پوسترهای روز استقلال و عکس‌های ترامپ را پاره کردند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/441900" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ffff4956.mp4?token=OaPdgr-f8zlcMJwpTSVdOFtFYbxyfPfddQXUr92WrXDe_VUsxao2TbpgBUJRtv9pM62GFVSqP4BidoDnYrN0UJHJU2n1cS4hHPab1F6UBoDZ5HrTn9q8rzZGVkQVEcj6PLd3ZCgq2gGRYVBi-M9NbPjawLBz2XJSL95QMV4NFkUTPltPRiP51SHCLwX4_Fw1YHcTsmeS25LmQqGgmFY7LXRceEqsHZzTBJt8HFPq-sxlaiFa0HDA81CGgmc0Z0PqeOZUY837TsLSbFXzJ3fI8vwF4pwR1JiuD4r4yre1NT1pKVOhLMaJ6sUEhv2FmAZWXQ97wMtb3774328mgkYlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ffff4956.mp4?token=OaPdgr-f8zlcMJwpTSVdOFtFYbxyfPfddQXUr92WrXDe_VUsxao2TbpgBUJRtv9pM62GFVSqP4BidoDnYrN0UJHJU2n1cS4hHPab1F6UBoDZ5HrTn9q8rzZGVkQVEcj6PLd3ZCgq2gGRYVBi-M9NbPjawLBz2XJSL95QMV4NFkUTPltPRiP51SHCLwX4_Fw1YHcTsmeS25LmQqGgmFY7LXRceEqsHZzTBJt8HFPq-sxlaiFa0HDA81CGgmc0Z0PqeOZUY837TsLSbFXzJ3fI8vwF4pwR1JiuD4r4yre1NT1pKVOhLMaJ6sUEhv2FmAZWXQ97wMtb3774328mgkYlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها در موج ۱۰۵ با قدرت به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/441899" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbQIQcz_rvAbYaenK7cb7S_irk3zTI9KWUFL1BWP23_wMRMrZrbKABLJ-UH8J6g9R2XY7oYdO3HyLHfC-WauPofzdfQB-pDoXJjLRIpldCZnHRQAsPo_VNTztJNMyKAjSnSZlgsc7E-wp3MBNZiqBYRZeCwoWjB01j6ZiEhBlCjbegJmkxSE8Vs--zPrrHWZu2QVvxozDT-0MtrNN6q0RKIAYW9A8DkHH8B3x2fMd0NcYr6Qj4u2SClM3Jn51IIlcaTNBQjQWJns4CC9qi9UhFeZlxnzIzozc7C4RL6Y0AEo8UjnwO5D6mIyTZsNAusWvmAYmzwIWNCbCWmB7FNktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS_U1AfQ4J0ygA5JQYRWQDxFt_cwQhoeVuyvH7qBTLrFFTNJOcyOj9iDZ2LwXLJBSgs7IJ5PgUtnX8W-AuZ13XU70PF0YQIr-R08ACd1jgNcmg8mLbVjRAvtf6-novqJFWo7dZ0eRjsIt-TEcRPXnTZ-rJjA0Lh_MwOsTNm5lJReVGGvypj8hVbLfq_9_Vf3D3o2byBK_hegiGltbsSf7LN7iIXBJzfBZSfwgS_XGF9PZg78-p89Iuj7DKIGS4U2YjvQcb-9cB3gXvz1oEYV_t6NO6I0l0r2KU5D5qLFeITgvVhqe0Jla8Do4GaBdknMHSKNtILLDD-ztVZ-5hG28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpx_MJB_hkTrAGQQTwpwjZd9N2NjvR8tWxroLGR1Fu02ePiOQiZpX4CUKw6-62hNLV6jY99ct7o-ppt4VnWaVK7zp_xF0-iVHw3BDqHT4tiarPBLpCr52VyabKysUCj4E5xBvOF4NmVBAhOLwiZYW0rRwOP7WDvBwWq2N7A95piej2IqN1UwNDrIErH4v8ncsxSPkItUWee4tWgFsk9jdwxdOm2GsYfFDt3ofzRTTqf0RbNwiHJob8HqZzW9MEgU_vkN5cHQOjMwOYmhgXLb4Hvun0CgdnHWcy1uTFx5_7TBrfvPS9rPaWiO5nHGwoQqe40Wp2G74Ww5Traq_kgjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wn93a_k1jTyR-I0F1JHoieb4FSDaFg8X9Uk-OF-wFWLuxfOU32mrQ4atD2WVrZA96VEZ3Ma4Ocp3y8TVROENIHyd3rNRcQ5f17zzvztHfQk3o_i0dyFlVzpSWg33aPxxPsb1Rz3KQugLX3vmbNh5r7kaOQamGAwZL4cdnFkrhG2ogKEAW14oJeHhInx2Ah3YskH6e8VCfZudf0zIQP0onBcTDp5uwT1HPLd4KqnAtr_Gln0Ax5DAX1SzjGoIy_rxuQoxtCDzdMqAPiec2-pAcXl7W8MLTR8o8lJrkD2pAwzSC5ikj9SWjmRUa-rFBZkTxzqA1pZ0jKdGmxmDVjnG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNtwpjhzFyqekht1DKJMzyunnbFuf9udZjNkzbJr7lSXidygN2aVFaRROo4SJvW89hLmjUA0iZ0d82-FbCypC9W9Vw_pbKyrcuD79T6BPHDV85ga4LDuPz6P7-CXOoiB8-aPNF1tTlNy8y-PMitGOTw_Bv3F3_QoP9viDhQZcl0tFdfD8T1SXKcKDSTN0KdNlb3zg73ldrNzPPfi2u1Dl8Xmm_SLKUaid5BiQ7txqj_eserELAYGdQyY8v-mfKvBEKB2J0yBxpDJsEmDwuCOD_WWRgh1ebrPOiZ1SjFG49Px1GupMu05QXxdSewck0vn6ftraZdlJTcgJfgpy80Z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mugUiw24x4WkhBA49dztj3qTNEE5r5Ddp8cO2S2cdKgkT9tyIHFp-RGdnYZD_-kHDR71oydnAEhKfzuZ6kSEQkPbSvk4MPsEk5KoIzGZhiP9hT46uKm4iLsyHe1jn3pP6QA5NWGf74Fr34t9XehRVb2-cqhFsTtcnoFgdY2PLIaLTbZPxyXnTaNQ_r9bhPoZbaRdAaaOafgwIrnRXNNGsscvi42J3RLMobfjDp1ZP2lab1xsWSS8tv9kwEHE3mrBwyCkl6mfYWg4RJKCV4uUyW4AZsrJTd1Ywo53viNOVsvPet9w4KnEfdqmDYNJ6obvRpvpw88pqOWjzmx6YwdfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMlr7OfQSJrrXO73zXOnTy5XaCEUcRiDW8QHoH1e-m5pBVS9kPFfHxKGC8EBiF_0NeubT3gSv2B_oEaejPPAB8Wpvx_aD4Ihl6FsFkox6x18m_E0uBZhHI-uYxkwfxl1m4CrWGifO1oZDtiJxm9NX6YQUw5YB4YDwqG0z2wUY1Ize3oFsoviHq-eKRAQR1DKClZwZXq_lJsFcNGWnG3oxmSXjHjAfR9blHtK2xlD90ekD-nC9JW2IY8xdnJRz5PCO2pDRRhNidPbGLHZwNnZ4K6ltt1GJ-6DSGcJcCos7hvjAE31XIHaVxgWEbWE_GSqXs5FTGYf9EfG9_bm-7lL3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین سنتی تشت‌گذاری در اردبیل
🔸
تشت‌گذاری آیینی مذهبی در مناطق ترک‌زبان است که به یاد تشنگی شهدای کربلا چند روز پیش از آغاز ماه محرم یا در روزهای نخست محرم برگزار می‌شود.
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/441892" target="_blank">📅 23:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3ac65e4b.mp4?token=kvb7anPbiU-4HDj2R47PAJDjVxxob8b_ODCgkaHkqnFRpcY9zWTFaObBPdZIuX8Bz4pe2OUrZazKTkeyA3CArgRrd_MiNHPxbGsYyN5lv6uXcFzNiKmUHEJGfDCPKxH1FDdqlsGImHJf-S5yLpcdCJd-DZPyt7mEdFsijfRlN1isfW_vQKMHQ3ejCfnq42ZL4ghkzPPcjXDmYN9XEypfKNYiZmOAvtg0dniEboHQnKXXO1vmJn77bCETW4B8tW0Gky-6jJYB0Amqy8YSEuE8rstBvdH96hxb3BPP9-3Ztpvs4jySF0000gTAJNa6mhl-TtUyxYxSm6XLVA9ppuT5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3ac65e4b.mp4?token=kvb7anPbiU-4HDj2R47PAJDjVxxob8b_ODCgkaHkqnFRpcY9zWTFaObBPdZIuX8Bz4pe2OUrZazKTkeyA3CArgRrd_MiNHPxbGsYyN5lv6uXcFzNiKmUHEJGfDCPKxH1FDdqlsGImHJf-S5yLpcdCJd-DZPyt7mEdFsijfRlN1isfW_vQKMHQ3ejCfnq42ZL4ghkzPPcjXDmYN9XEypfKNYiZmOAvtg0dniEboHQnKXXO1vmJn77bCETW4B8tW0Gky-6jJYB0Amqy8YSEuE8rstBvdH96hxb3BPP9-3Ztpvs4jySF0000gTAJNa6mhl-TtUyxYxSm6XLVA9ppuT5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در یک مرکز خرید در آمریکا
🔹
رسانه‌های آمریکایی از تیراندازی در مرکز خرید هِیوود در ایالت کارولینای جنوبی خبر می‌دهند.
🔸
تاکنون دست‌کم ۲ نفر در این تیراندازی زخمی شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441891" target="_blank">📅 22:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7794a1c2ec.mp4?token=l5QJazhqa8iUCZCR-kgfwy3lrh254u1jB_DjxDWUY57Da_7R6qwEa9s7APZz3UIB2FzVc5h6fznVWK0CxFa8zIqnySqZroSvKnFZ96ySwKa1t3iolqkyRU1iMtML-Oiu-nIZYEI2NlOq5ETZj7Uu9_Fj3l_NNOx1usO6S51r-dXy3HpyUk34J-AJaBfsjlHpx0mMwa50QZiiLplwzwJOyU3I6NBZs9oEGMC0UMASwmphLK7TqLaGrjmge21bOmf5MrnO5WohDilYnelnQGEEIJELLBnHn49Y_XDhagDNbvB1vwbiHhqC59LQu22gDNymu4egvSnjM882a590mxxf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7794a1c2ec.mp4?token=l5QJazhqa8iUCZCR-kgfwy3lrh254u1jB_DjxDWUY57Da_7R6qwEa9s7APZz3UIB2FzVc5h6fznVWK0CxFa8zIqnySqZroSvKnFZ96ySwKa1t3iolqkyRU1iMtML-Oiu-nIZYEI2NlOq5ETZj7Uu9_Fj3l_NNOx1usO6S51r-dXy3HpyUk34J-AJaBfsjlHpx0mMwa50QZiiLplwzwJOyU3I6NBZs9oEGMC0UMASwmphLK7TqLaGrjmge21bOmf5MrnO5WohDilYnelnQGEEIJELLBnHn49Y_XDhagDNbvB1vwbiHhqC59LQu22gDNymu4egvSnjM882a590mxxf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسوج یکصدا: پای شروط رهبر ایستاده‌ایم تا آخر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441890" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61f906f05.mp4?token=Uasmpl5Fk4cuBvZlhMkBiUDBwZyUtY1iJfM4OEr6NLnrZGuaA9rRu49Ef7VRNP65tsOe6DSl8JwBp7oykeCKKnFv8ACwzsaOZuFLndaE9Xkuwh6Y0Q4UIzlXNYxYEjohVtKSvycQ8atvv7L_83yWYoZaNaA7hJY8wkQP873G_tqassdf3NBaMrp2vV9WlP7d1i-MZJd1EEPMdVqmbHQbjs5-SGaRB3BsylWyz_tyNUxkVRS6vhiSM4Rx42rRZtITSdLP1FYEl3BJUrw3JbJ1ooBH3h5d1Fhf6g_vZCkTxwIgyhFVGcGWZ49f7BzTYRyJUDVwhG-yqr7gF9THrv6NGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61f906f05.mp4?token=Uasmpl5Fk4cuBvZlhMkBiUDBwZyUtY1iJfM4OEr6NLnrZGuaA9rRu49Ef7VRNP65tsOe6DSl8JwBp7oykeCKKnFv8ACwzsaOZuFLndaE9Xkuwh6Y0Q4UIzlXNYxYEjohVtKSvycQ8atvv7L_83yWYoZaNaA7hJY8wkQP873G_tqassdf3NBaMrp2vV9WlP7d1i-MZJd1EEPMdVqmbHQbjs5-SGaRB3BsylWyz_tyNUxkVRS6vhiSM4Rx42rRZtITSdLP1FYEl3BJUrw3JbJ1ooBH3h5d1Fhf6g_vZCkTxwIgyhFVGcGWZ49f7BzTYRyJUDVwhG-yqr7gF9THrv6NGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقاومت جانانه مردم گرگان در شب ۱۰۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441889" target="_blank">📅 22:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690182037e.mp4?token=n475RLnt1eUpo_xj7JpXHQw6hU3fCWysfLqrrpBfUvL608e7e0of8yUFLn_Zkhm_mdWYfgYl4hTwbHdXQDYUE9C75acFpcs406VYGww9m5ipBtlc6eO9Npk12Nr-L-pqeeSoH-X4J7GGI1pAQcbr2hguOLB82bi8G5XMlUb08Mb9lcj9SscItR6-LknqowKMwpzmbbmNLLc8D6mODP0apctemtI17wpxqsJ6MMKZuObav9YIfA5M_LKrVhNbCAjnOA7LrmdyLmyJQyp_PLw0REf0i49YqgeIdWCgaSmVXTcq5pOlC2QXmR-1oHTv9s_FmDq1Mhw0T4B07mV0YsKq74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690182037e.mp4?token=n475RLnt1eUpo_xj7JpXHQw6hU3fCWysfLqrrpBfUvL608e7e0of8yUFLn_Zkhm_mdWYfgYl4hTwbHdXQDYUE9C75acFpcs406VYGww9m5ipBtlc6eO9Npk12Nr-L-pqeeSoH-X4J7GGI1pAQcbr2hguOLB82bi8G5XMlUb08Mb9lcj9SscItR6-LknqowKMwpzmbbmNLLc8D6mODP0apctemtI17wpxqsJ6MMKZuObav9YIfA5M_LKrVhNbCAjnOA7LrmdyLmyJQyp_PLw0REf0i49YqgeIdWCgaSmVXTcq5pOlC2QXmR-1oHTv9s_FmDq1Mhw0T4B07mV0YsKq74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران‌زمین در شب ۱۰۵ هم میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441888" target="_blank">📅 22:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">احتمال توقف عملیات زمینی صهیونیست‌ها در لبنان
🔹
سازمان رادیو و تلویزیون رژیم صهیونیستی به‌نقل از منابع امنیتی گزارش داد که ارتش رژیم خود را برای دریافت دستور توقف عملیات زمینی و پیشروی در لبنان آماده کرده است؛ اقدامی که گفته می‌شود در چارچوب توافقات و رایزنی‌های جاری میان واشنگتن و تهران مطرح شده است.
🔹
براساس این گزارش، رژیم صهیونی قصد ندارد از منطقه حائل در جنوب لبنان عقب‌نشینی کند و وضعیت این منطقه یکی از محورهای مذاکرات و گفت‌وگوهای پیش‌رو خواهد بود.
🔹
این رسانهٔ صهیونیستی تصریح کرد شاید روزها و ساعات باقی‌مانده می‌تواند فرصتی تعیین‌کننده برای گسترش عملیات نظامی و تسلط بر مناطق جدید در لبنان باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441887" target="_blank">📅 22:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyrf2QbOrgc47SImsZdccIpLvp23Mu-jqmiQTG22_8zcB3cs-uyrtrXrM-ooICYM-lSgcDPTGizhwFjLUlqGkXNjtEUj8yaeV7SXKIGjJffAfpCga9ph9XdL8umg6gkjxOowy13lpvniXQuC0hk2yZsSsF40pgS5DbMueXj1ew5F1hBqGQ6X75ROPXSEsWksHFjxITrd_HS-ZKnncs_ems4klAki-6C3VwlBdx7Y4yXCD3Z2L7uFNmmXm7I56cn0ptu14L4ifeYRW9o69vyqvUo8KvS34pYD0azBM7M3czgnSck3raifiD6O8Kea2BXJ60mbm6LsRoAv8pgpPOm5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی قطر: ایران برزیل آسیاست
🔹
لوپتگی، سرمربی سابق رئال مادرید و فعلی تیم ملی قطر: ایران برزیل این منطقه از جهان است؛ تیمی بسیار قدرتمند. اما ما آن‌ها را شکست دادیم و به پلی‌آف رسیدیم.
🔹
من آمده بودم تا قطر را به جام جهانی برسانم؛ حالا ما باید واقعیت خود را بدانیم؛ ما در جام جهانی مجبوریم در اکثر دقایق دفاع کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441886" target="_blank">📅 22:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_vEab8Q39HiCT0BQoBMYevfcYD6uvf1kyVj7aNZabnLI0lkPY_aY2mbAQG7wT7GqQlsXbjUntEEOI6t4vDcbi1H6rjA1tKJb4aoUxnWhFGdorQUfLE72jL-RtHPBduDLuzwsxrnJelcP84rw0iJq90dDSjhnPPfHcNRnQfqTQ4qk-mCnWrH38HjUEdWLsll2MJO-GlLjn7UGrgmUzPWi0BLgT5ULu3Y0i4YdFUJf6ara5SORk0rqe4cS-ODQrkyuzoyRcofd_xxMs6_yaGiwvnnbOunPYnIHlTbd_yz8Pz6XGF6FlF2AT5QFRamVPUfgvrm4dHsATBwP4Kmc3wl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#ویژه
| نگاه رهبر انقلاب به مذاکرات توقف جنگ چگونه است؟
* ۱. حکمت امتناع از ورود علنی به جزئیات مذاکرات
🔸
نخستین نکته آن است که ایشان درباره محتوای مذاکرات، الزامات، خطوط قرمز و شروط مدنظر خویش، در پیام‌ها و موضع‌گیری‌های علنی اظهارنظری نفرموده‌اند؛ بدین معنا که به‌طور مصداقی دستور نداده‌اند در
#مذاکرات
چه اقدامی صورت پذیرد یا از چه کاری اجتناب شود و یا تیم مذاکره‌کننده چه عملکردی داشته است.
🔹
عدم اظهارنظر ایشان در خصوص اشخاص مذاکره‌کننده، نحوه عملکرد آنان و همچنین جنبه‌های فنی و محتوایی مذاکرات، واجد
#حکمتی_عمیق
است. ما موظفیم منطق و نگاه رهبری را به‌درستی درک کنیم. دلیل امتناع ایشان از کشاندن مباحث مناقشه‌برانگیز محتوایی و فنی به سطح افکار عمومی، خیابان‌ها و فضای مجازی، ریشه در همین حکمت دارد که نیروی مؤمن و ولایت‌مدار باید بدان توجه ویژه داشته باشد.
*
۲. میدان مذاکره، امتداد میدان مبارزه
🔸
نکته دوم ناظر بر دو گزاره‌ای است که رهبر معظم انقلاب تاکنون در یک پیام پیرامون مسئله مذاکرات مطرح فرموده‌اند: گزاره نخست: ایشان خطاب به مردم فرمودند: «فریادهای شما در میادین بر
#نتیجه
مذاکرات مؤثر است.»
🔹
گزاره دوم: در انتهای همان پیام، با توسل به ساحت مقدس امام زمان (عج)، از آن حضرت استدعا کردند که برای پیروزی ما در «میدان نظامی» و «میدان مذاکرات» دعا بفرمایند. این امر به‌روشنی نشان می‌دهد که عرصه مذاکرات نیز خود میدانی از
#مبارزه
است و نه‌تنها در تضاد با مقاومت نیست، بلکه جبهه‌ای است که در آن تقابل با دشمن جریان دارد.
*
۳. تفسیر صحیح «تأثیر فریادها بر نتیجه مذاکرات»
🔸
اما تفسیر صحیح این بیان که «فریادهای شما در میادین بر نتیجه مذاکرات مؤثر است» چیست؟ متأسفانه، برخی از این سخن، مجوز فریاد کشیدن بر سر مسئولان داخلی به بهانه
#نقد
و مطالبه‌گری و به‌اصطلاح «باز کردن دست ولی جامعه» را برداشت کرده‌اند. این تفسیری کاملاً ناصواب و در حقیقت تحریف مقصود رهبر معظم انقلاب است.
رهبریِ ایشان مبتنی بر
#مبانی_قرآنی
است و فرمایشاتشان هرگز مغایر با آموزه‌های الهی نیست. قرآن کریم می‌فرماید: «أَشِدَّاءُ عَلَى الْكُفَّارِ رُحَمَاءُ بَيْنَهُمْ».
🔹
رویکرد حضرت امام (ره) و آقای شهید نیز دقیقاً بر همین مدار استوار بود؛ چنان‌که آقای شهید بزرگوار پیش از جنگ دوازده‌روزه فرمودند: «ما به
#دشمن
بدبینیم، اما به نیروهای خودی خوش‌بینیم.» این بدبینی صرفاً معطوف به خوی استکباری، عهدشکنی و ذات شیطانی دشمن است، نه متوجه تیم مذاکره‌کننده نظام.
* تفسیر ایجابی و سازنده:
🔸
تفسیر صحیح عبارت مذکور این است که حضور شما در میدان‌ها، حمایت از نظام و مسئولان آن، و پشتیبانی از تیم مذاکره‌کننده، موجب پر شدن دست نظام در برابر دشمن می‌گردد. این
#حمایت_میدانی
به تیم مذاکره‌کننده اعتمادبه‌نفس و قدرت سیاسی می‌بخشد تا در برابر زیاده‌خواهی مستکبران ایستادگی کرده و اجازه عقب‌نشینی نیابد.
*
۴. لزوم فهم منظومه‌ای از بیانات رهبری
🔹
ما نباید بیانات رهبر معظم انقلاب را به‌صورت منقطع و مجزا از سایر پیام‌هایشان تحلیل کنیم، بلکه نیازمند یک «
#فهم_منظومه‌ای
» هستیم. یکی از توصیه‌های پرتکرار ایشان، تأکید بر حفظ وحدت و انسجام است. ایشان صراحتاً می‌فرمایند: «انسجام بین ملت و دولت و دستگاه‌های جمهوری اسلامی یک نعمت است» و تأکید می‌کنند که حتی به اختلافات موجّه نیز نباید دامن زده شود.
*
۵. باور به اقتدار و تسلط رهبری نظام
🔸
تصور ما از جایگاه رهبری باید روشن باشد. آیا رهبری را شخصیتی مقتدر، مدبر، باکیاست و مسلط بر امور نظامی و دیپلماسی می‌دانیم، یا شخصیتی منفعل، تحمیل‌پذیر و تحت مدیریت دیگران؟ اگر به
#اقتدار
و اشراف ایشان باور قطعی داریم، هرگز نباید گمان کنیم که اشخاص یا جریان‌هایی می‌توانند تصمیمی مغایر با منافع ملی را بر ایشان تحمیل نمایند.
*
۶. رسالت ولی‌فقیه در صیانت از آرمان‌ها
🔹
مهم‌ترین رسالت
#ولی‌فقیه
، صیانت از اصول، جهت‌گیری‌های کلان و منافع ملی است. بدیهی است در صورت بروز هرگونه انحراف از آرمان‌ها یا سازش با شیطان بزرگ، ایشان شرعاً موظف‌اند با بهره‌گیری از مقام زعامت خود، به موضوع ورود کرده و مانع از انحراف شوند. لذا، عدم ورود ممانعت‌آمیز ایشان در یک مقطع، منطقاً بدین معناست که مسیر طی‌شده مصداق انحراف، عدول از
#ارزش‌ها
و زیر پا گذاشتن خون مطهر شهدا نیست.
🔸
مجموع این شواهد، چارچوب نگاه ما را در خصوص نسبت میان رهبری و تیم مذاکره‌کننده روشن می‌سازد. البته هیچ‌یک از این موارد، نافی ضرورت هوشیاری، دفاع از
#منافع_ملی
و توجه به هشدارهای رهبر معظم انقلاب نیست؛ اما باید دانست که مرز باریکی میان «مطالبه‌گری فعال و هوشیارانه» با «تخریب نیروهای خودی، ایجاد اختلافات داخلی و تحریف بیانات رهبری» وجود دارد که مؤمن
#ولایت‌مدار
باید با بصیرت کامل از آن مراقبت نماید.
@rahbari_plus</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441885" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqXUQUCRLdAkirp75HqUfDhT_8IEO3lhA1PHcUmZSBWpM7ORjmw3LOhKWKtLnmXBEGhnz9BFCggQCFqnl4Pnz_zcHVL_kdKE9QJGY9e2vDA__BoEPBfsaOR3QhYvmMllH0eu6KhATFo8Id-X1VduqZHYO8q9xNfkw0ADfsqtysptA_E9LUpQ8Nqec6yFHvGNv1AnbCIGN-u7TeNte4__Z5aAr4xPpboWZgMtzRSvhwIkbzf8M8TLHr1D9LSovSN-1fWsq-JoTWH8mnwGaSLngZMMk6n27zQTrrBVbEHBndRDacvNC4eqi-p60tu_w48Sjl9kksbfFKrThP7pc24HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVarHlPCcpCoLlar2pSMmurwz1TdUEvoEiXyTtGXTT8U7Klb46FxuE4JZFPOT4rLbuZd6jt1VHXRZAMH4ekjqf1cG2a5w517F7yN76Ge7N4_TfgNRc6T6EB0mKBIgWFDPPWar8miXjXcnlza351jw-p5t1LE7BD-9CCWyfOyE7IGrEKDoqgGrSglivOesiBcMAsyXthIGtys5nCrJ7s9vbBDhqeSwwSQ5FUwB9lAxmo_-GIltISdMsLMpOfp_6I5c8UjqtqOlkhSjKLZfsoMcBNEmu0zX6NcP4LHrj2QsRHz0NGZVCFKLh1vFXiErHteZKHUWOh7V-1yQXpfArma_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBhbvLQ4h6ux9yoYEik0QZdoQMaKKkLH3NMkzDhS2zHbyT6eaxqSK8laUTd8ben823fKZSL44nnIeVnLWG0MH9VGxc3jhKeEUAlacc_MJd1PXnj396oPWkKTZ2mreLko4fxHJ9BUloC0NmkY6WeyHZtL3h72bI7y2X0QtU-kCeBV2IeTAexXGO_RSOHCNrcrc5tDDX5zL8LD3d-_Kelys_hwqP1c-XV_dlpUsh8b85xAuVoZkBtRNJWSVEMsJehNjAXU8f2AwYFYvHwHU9DcTjx2hNOzHr6QFS5Ui0PKmr8Gqn8bMhsGBjhtH4Yn7gCZzRBSoFlDdyyHkKjKVf9w4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یوزهای «نیکی» و «نیکان» شناسنامه‌دار شدند
🔹
تابلوی نام‌گذاری و شناسنامه ۲ یوزپلنگ آسیایی به‌نام‌های نیکی و نیکان رونمایی شد.
🔹
این ۲ یوز خواهر و برادر، متولد سال ۱۴۰۲ هستند و برخی اخبار منتشرشده درباره تولد آن‌ها در سال ۱۴۰۴ نادرست است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441882" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed2e032c1.mp4?token=IOTlYmDV9OxMNOaSmHLG6w6wjDcCR3mZcVsA2VYzn-4cVzn00FN4HVY5IGuhg9tTbRL2OqG4ZAnA1wkbn5zSRcD7NwCXqojBYFL1orSB7TFMM7CiZ0YT-GrlzlJF1BvhF4IpNf5n-Y9YNY9e1U0nYtSuWiuH-oYEAHA2MrD475Ww_3IDz8ffviQcAAj_3VE2h-oPJsDOaq0jlVPIbwUWYtWAqdnrbaJesucU4OSvJ3K9GsKd3pwych93DWChVbtt3cu-5bbxN9SnVn1dd8iST5hqGXDLWNTuJwfwX157Q2r7cifGAC7tCRXCKu4oalEGovGNVOibL2Y_Cr9sO0jMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed2e032c1.mp4?token=IOTlYmDV9OxMNOaSmHLG6w6wjDcCR3mZcVsA2VYzn-4cVzn00FN4HVY5IGuhg9tTbRL2OqG4ZAnA1wkbn5zSRcD7NwCXqojBYFL1orSB7TFMM7CiZ0YT-GrlzlJF1BvhF4IpNf5n-Y9YNY9e1U0nYtSuWiuH-oYEAHA2MrD475Ww_3IDz8ffviQcAAj_3VE2h-oPJsDOaq0jlVPIbwUWYtWAqdnrbaJesucU4OSvJ3K9GsKd3pwych93DWChVbtt3cu-5bbxN9SnVn1dd8iST5hqGXDLWNTuJwfwX157Q2r7cifGAC7tCRXCKu4oalEGovGNVOibL2Y_Cr9sO0jMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله برای نخستین‌بار پهپاد «هرون ۱» صهیونیست‌ها را به زیر کشید
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441881" target="_blank">📅 22:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124b0c8a54.mp4?token=pB9FRC0hF4wP0pKhvAzh_lEGVgm3o1Z6CpDeF_ZnaRM_rCRwHWluTiLln0jP6cUgMyCQxZkrgHvWN94ekjYvE93M_zJrRBYWLX-SekLf_CXfuV46xIEqYrLHZulGr3UB9eAUzrwwa9J5Ny5vu0rAH2N40pstZO45-ANw7OgWKdN2UMn_ZXEAaa0QulFBubqHd19F9GTkpdzfdN4zDLDjhwmKsyzN4Tq78W_sOzPwmrlFMTcttCV4LJgyaLv1jJeroo3QCEXUgy2gfEw18jJpG15g4vW49aOEG5Ytnkw7Dc8nCudCMflReK0n_68hxJ4vgYfJ0Pyg_QvBbwHq45rh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124b0c8a54.mp4?token=pB9FRC0hF4wP0pKhvAzh_lEGVgm3o1Z6CpDeF_ZnaRM_rCRwHWluTiLln0jP6cUgMyCQxZkrgHvWN94ekjYvE93M_zJrRBYWLX-SekLf_CXfuV46xIEqYrLHZulGr3UB9eAUzrwwa9J5Ny5vu0rAH2N40pstZO45-ANw7OgWKdN2UMn_ZXEAaa0QulFBubqHd19F9GTkpdzfdN4zDLDjhwmKsyzN4Tq78W_sOzPwmrlFMTcttCV4LJgyaLv1jJeroo3QCEXUgy2gfEw18jJpG15g4vW49aOEG5Ytnkw7Dc8nCudCMflReK0n_68hxJ4vgYfJ0Pyg_QvBbwHq45rh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بارانی امشب مردم بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441880" target="_blank">📅 22:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f3637faf.mp4?token=nNwGWi7w20MsbQIf00vf-XMm1T4MA8q_FdQZuqe4HsdPErM8g4gKFN-3DptQDwnd22rEemIJCPLmIRBAxoB7KqakgG44K8xLzLuZIdqoSHxxZ27sPxN4OJVRkVdCCuo-OLZiIS3gU30xpZOky6LZlraeZyeRHZrmp8KYRWkOOUlEZxhE0nh1zF1wc2bx4CigRCVJ7LLFDXV8Df-XwUvB2ShJBszFpOWxs2CYj3Zvz3-Di5GjJpp5vd2tmUU4IopUlOC2_lLTUUTQ0F4rNLLz7z8RQuWGsPk2ZiLXYcs8XtI1kM__JpKJkyRjyP2yhaU0Sz38U-sGBjTIxgBNE92Y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f3637faf.mp4?token=nNwGWi7w20MsbQIf00vf-XMm1T4MA8q_FdQZuqe4HsdPErM8g4gKFN-3DptQDwnd22rEemIJCPLmIRBAxoB7KqakgG44K8xLzLuZIdqoSHxxZ27sPxN4OJVRkVdCCuo-OLZiIS3gU30xpZOky6LZlraeZyeRHZrmp8KYRWkOOUlEZxhE0nh1zF1wc2bx4CigRCVJ7LLFDXV8Df-XwUvB2ShJBszFpOWxs2CYj3Zvz3-Di5GjJpp5vd2tmUU4IopUlOC2_lLTUUTQ0F4rNLLz7z8RQuWGsPk2ZiLXYcs8XtI1kM__JpKJkyRjyP2yhaU0Sz38U-sGBjTIxgBNE92Y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از دزدی‌های جام جهانی چه می‌دانید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441879" target="_blank">📅 22:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5F-fJGaOKQJFFzpSqLy4ecKZCw9OrRUaJiKGXj4nP4eUMq3owQjmyBh7fgkcpbGNrOqBE-ITefKJGQkq_AE2qmlVIR_XkycZ3F7q1yCMMvv9RTGdqtkEkreMsxMgvMtgNvdM4cPVpzBmP1KF1tD0ssvhc0P6lUgsiS1EXsayzqNSwhB_yhCBcfVnRA8SGFMGAqV79eI9niZf997abTbJpP9OqJK2gwxhwmVE6tAaArJtDOlvqYu09Y78Rfx1BWQ-AB4m7SuJMMLS0RM3xc962ufwBxfsLinqpMhtv-XxLmLo_5MtKKotTz7D3jCOk91wtlmHPkrfugKfXLsyTxpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG_rcJEYEHoxfaf1nZkjenE6WJm_k6aITneuEp2Pnl0Ht1Z9CPQkI3JklBe1p08d0OjU3bo9N7JgE2-I-B4k_RaCZYXjYMSBWFh-gCXueT5UhtGDfCnjsXHKM0GnfOJOEQshqqETo5arFs8387fum7y9qPjnp4Pd7x87SnzoZjAC9l_8CWH69EU6dTPQAhsmIiAl3NiGJQ6AkNMpHy0sck8ShgHzVkFp4-lahGqcNWyV7Mu0CAdSiaZoDwZto_6gHRPbTNoxcJ8HKSYgKmXnynqqW_PInzsUh0E2HHCZhNwnrNG3gEeXgpRgrpSqKIrIs_bp9W-GJET4iBENeTlrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ6ZInr8ll4zhVj4umkpkKqtbKS1sft6rq-cbakpxQ-WXBPJiRpa_BbG-vZWJ5vmFAmjR39w7GCOtdz4bBKKVdQ2SXBirt-vJro60TZ4zgo41Y66jXEMuQue0eBGwgECgSr6iplBJcfu3YhkFFE74Xk72zTOZnr7lgZXCrbRgyyyN9jh_JckqgDd7Fmm1TQ5rtOqYlYI5hPxMWFv2MZSeH_Qj8xS-3bV5nimcpMt15ZCpkIFlQPOFDVrnfeVLD0yWRnU_lpQm5klIGP9ZFeGDiMaDGFcZGMsxdnJTcWCFEVaNtGsKqtNrhfrH12gYV1EmCDHnN-xaHi6eYjCI5BgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZdhz_9vaa5chQo0iIXYO02KZ-AzGie4by12H3xoGvqpamf9TyVwJOChcPZcn4hT3R4dVVN6O9D_fkeke-pn61qNem6P3pu6hi05z-xy-q6cY-6cuUZDenNOHPxDj7TIaKMxqqXtcbTWltZtmf_OdIbw6vplVme7hC3mIhi0iw_e6Z1TAeTadQJraBCQTBkfpUpkld8tp2IX_keORwDf8KtpaQWDSYb8eoH6ShVDbyjyQB-QN7QLXL6hnFAzjwYxtfoo9o8fGsrHCkXDSrkglFCjt4Tst46J2411FT3mYxEL4KKcleL4SxM6HUsrvWigAtNdIsiaTA5TaXBAbKuqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qtqi-p4CkvI6c47iU5BF_YjHJqJiBaTirsQSgnz598vEf846Lpi445-n_4rtTVllbBsQnmgsxl4odK5jTh_FNP12Ng_q1wmjz8GwoBYzWRgXdXY63BQHfrgIFEptj0jkJ32xsqIiLBkLNbuW7I7sPusb2a9z_UMoN9XBKsb00Uq_LN1sRM8NTCmaGiPTmwke6SENOzKkuG01pc5Pf3sx2b3saDOK-_ONsALpR4RVrEtmWBtvVHPbe80LpBVFoxHUhcwrWPbh7uE2GVkfmBqfBl0Jc3XdiB8fYMp4b0Rz-wQCjYjHIHcCbeu1GLBvlXTdGwQpGU3UOs80Ujdx9ewINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIO1-XVFikgS37DnCwiQ6fVFtexLaY4Cjhm6ddjjiayW-3xChnxutcPL53Y0on3O35s05xFWiGl6qbYylSuYA-M8XNA2TYYMZyOqBi5bFiuBCUKO-D76Egx9CcQ69i-oNWnvaxLDx_TB5ZoiMZxhzUImFhF9aKkP0pwqX0yYo9f56V1ZEzw3h5JwDO69u2N5MTVFKkVDSfZSq4tcDyt1b2t_E4Fqn-kXaPnz96JUB8CXi4KEcWprvEe8K-h7uf-UNhINboUD_3jkeLOsyxsGgAPfvDTbkL-PCJ4KefSyYnQbQVwIQNvy8KEEDQ9H1swrhJr4xKR7Zy2Boe8JCYyTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsbXjkmw1mngXpy-QTq0yhw8GCnIe1gGGTVTysTYetbUwEqGEGL2k1exrUbhUD3OfFR98N84I1VJfiePcEMWSXH7sac69ikuAh0A3RBjJsONA7MOU3l1IzeaJoBpylQ8fQzHT0MN3aWjoG5VB6hMKKP3Q_GuOr2kv1XMHeCVt8N1wSf2Ve9pch4nZA3IVqlJj2AV5PzM6SatrDwR2cJlz_v4wIE3x8iTCBGm8pvYcnDIlO5Amdvi39pjb-iAhXiaAan0NpZHcnZ9-Y8BY5jwzbm68JzaQ_XqvqSONSm3EGjUyks4n4Oh_2dTVHtygcvUpbZ0xt0iMvl6Ai96qRaDqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاح قطعه نخست آزادراه شهید شوشتری تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441872" target="_blank">📅 21:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌  حملهٔ حزب‌الله به یک مقر ارتش اسرائیل در جنوب لبنان
🔹
حزب‌الله: یک مقر فرماندهی ارتش اسرائیل در اطراف قلعهٔ الشقیف مورد اصابت پهپادهای انتحاری قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441871" target="_blank">📅 21:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWyTsqweCXzLCdJzWFJkpJR8Gk5h9Rv_qSEIRRQluLpaUOcMmrWOets-U-wGe6OAYMZ4O1_GlImhFD0yxmDyrmyU1Wz2oH-6072QIIoaS-b7bV7B2cFK9k89U1Ek1RlDMefJEvhPrW3w6i4PotjSCnwB3aoS1vHtKK0ldSLxxmzfTbwO4IZZKOtuTrWTCCrP2GzDcNL_XEn1rHE9TapAr1Caa6EA3q-5le5ZbDw_kBLg--RuzOVKAx_V-hxCEzaD9sTvMK8EujkdH-U8292T9WNKNvccNzGkEVFghNF9w4wqbIuizS5wnmLLWzTVY93Np153bw0Ep-EG2508o2Lttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نظر شما درباره امضای تفاهم‌نامه با آمریکا در شرایط کنونی چیست؟
نظر خود را
اینجا
ثبت کنید
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441870" target="_blank">📅 21:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441864">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
دبیر شورای هماهنگی بانک‌های دولتی: رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.  @Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/441864" target="_blank">📅 21:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441863">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58b11fec2.mp4?token=MWbgXp7-hOQVCqNQFWItIpqCie5ryainODK7uxcdfR1JJXG0zB-zeZ5QaId1NG6dvx3nk4p1Ikz8psjI7ClHuseBdygRr2_6V473es-A-WOacQ3tX_6Rx9YXZrnexttCWK8NuqOm0I026raJpQRQiGbHFdEk4NS3VSPJY83M-hEDRAI3-v5sYQmsp30iRNSba_oZHI02vYKqHS9mBAqF1LnLyHM4rgc_Xg3_G_Sk4EmbYAnN62FG5d6pEhXB81z3JQBVNv-xrnxkeXq6wiJHyJhfbO4nTRAhtnWh-kKPribd9PSyGzllPl6GM7Z7FkaDFQB_1pkOBUeu_Iy-ERJVsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58b11fec2.mp4?token=MWbgXp7-hOQVCqNQFWItIpqCie5ryainODK7uxcdfR1JJXG0zB-zeZ5QaId1NG6dvx3nk4p1Ikz8psjI7ClHuseBdygRr2_6V473es-A-WOacQ3tX_6Rx9YXZrnexttCWK8NuqOm0I026raJpQRQiGbHFdEk4NS3VSPJY83M-hEDRAI3-v5sYQmsp30iRNSba_oZHI02vYKqHS9mBAqF1LnLyHM4rgc_Xg3_G_Sk4EmbYAnN62FG5d6pEhXB81z3JQBVNv-xrnxkeXq6wiJHyJhfbO4nTRAhtnWh-kKPribd9PSyGzllPl6GM7Z7FkaDFQB_1pkOBUeu_Iy-ERJVsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هواییِ تجمع مردم پاکستان در بزرگداشت رهبر شهید انقلاب در لاهور
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441863" target="_blank">📅 21:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441862">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
روایت سخنگوی عملیات وعده صادق ۳ از جنگ تحمیلی ۱۲ روزه
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441862" target="_blank">📅 21:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441861">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1615fbbd2d.mp4?token=KMZAyzCaVt-clNOOeV6pI8az8C76-SZCl1Q5pXIYpeK3Aki3dGKTAri3UyslGYEazFLy39xiN2_nt29cb90UHoeIHjMHcbyKQC6Nb4Jr5-7k0guM3Nj-Y7ujSLybdyFpssem9Ft9S8s0GnSW-kJsUnfNQVXMHf_GISuDubpF3tsrZWztZF3gXp-hNmg036lCZmMkUi9-tfRPvcnRVpgZxTcxnDf2ljnsQNDPz7SQdO8shr9UQg_IrzmSM8g2nQOBU5swbtBStcAarTaaK8-nh-FUUVa16yOtp3VYWZ5J-5dzZGLGhlQUD5BPJA6vITc1O5dK33M3mL7vp16u-Xbm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1615fbbd2d.mp4?token=KMZAyzCaVt-clNOOeV6pI8az8C76-SZCl1Q5pXIYpeK3Aki3dGKTAri3UyslGYEazFLy39xiN2_nt29cb90UHoeIHjMHcbyKQC6Nb4Jr5-7k0guM3Nj-Y7ujSLybdyFpssem9Ft9S8s0GnSW-kJsUnfNQVXMHf_GISuDubpF3tsrZWztZF3gXp-hNmg036lCZmMkUi9-tfRPvcnRVpgZxTcxnDf2ljnsQNDPz7SQdO8shr9UQg_IrzmSM8g2nQOBU5swbtBStcAarTaaK8-nh-FUUVa16yOtp3VYWZ5J-5dzZGLGhlQUD5BPJA6vITc1O5dK33M3mL7vp16u-Xbm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نفت: انتقال سهمیه از کارت سوخت به کارت بانکی طی ماه‌های آتی اجرایی خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441861" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441860">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29aa54312b.mp4?token=WeulA38THHbDyynjdwXokOSgj0BrG_tcp1ka8JIISo5EC2gqi8XWK920j0gUF1sf6tozjd9FO11lF8HFFnZVFclg3dpz83Z2HUkbilDec4SWczSqKy9oALsxZAZ49SUpWMwtWWMWvnnqSo5Q8JvBMUGcfxXPJ-fLbV5YrISZwf_UNdDeakV0VHGarFR8XtIWauIQ-eg6iBpxs9do04YkOG8wbIomn56AFoH5p8Fs8_bus7LwonZYZleHFzr7-9ZvgWvRvxDmzuPLK9U8xEHbaaUG7ULIGs3mJXNqgL4PMxbbmvBGGThNuycxmELgV8SD-fqKiqWBSeQUx_MDw2_bSKsZC57XP--rgsoGvG2VSjnDIt8ipLyznMdmSVguib8VkKuuuhrTgzPCVymqgCWo1RENWpDKKFsJDc3bz-y_0G8_ednqQaw2wToTAu5CC1wEQAiHc1kHivKFqB16acOvcsxYd9sYsWrwcEt97pkt4Qe9qbRJEtpAtwth9b7IpzAXrlh3XHulGvGuAnBSIQwQUXUwi8rig4IheKgXN5S6-4YYiiix9pSgR1rHiV_ZzKAOyRxve1w-8BSWfHwHzIXH64Yz2b74JCJYypFN1ok8dMKwfQfnwyzy4y5l1cEhxdyLEad1yJe3RioJvhJ4II8UOA7sXzpis9wuOBjE6RntyZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29aa54312b.mp4?token=WeulA38THHbDyynjdwXokOSgj0BrG_tcp1ka8JIISo5EC2gqi8XWK920j0gUF1sf6tozjd9FO11lF8HFFnZVFclg3dpz83Z2HUkbilDec4SWczSqKy9oALsxZAZ49SUpWMwtWWMWvnnqSo5Q8JvBMUGcfxXPJ-fLbV5YrISZwf_UNdDeakV0VHGarFR8XtIWauIQ-eg6iBpxs9do04YkOG8wbIomn56AFoH5p8Fs8_bus7LwonZYZleHFzr7-9ZvgWvRvxDmzuPLK9U8xEHbaaUG7ULIGs3mJXNqgL4PMxbbmvBGGThNuycxmELgV8SD-fqKiqWBSeQUx_MDw2_bSKsZC57XP--rgsoGvG2VSjnDIt8ipLyznMdmSVguib8VkKuuuhrTgzPCVymqgCWo1RENWpDKKFsJDc3bz-y_0G8_ednqQaw2wToTAu5CC1wEQAiHc1kHivKFqB16acOvcsxYd9sYsWrwcEt97pkt4Qe9qbRJEtpAtwth9b7IpzAXrlh3XHulGvGuAnBSIQwQUXUwi8rig4IheKgXN5S6-4YYiiix9pSgR1rHiV_ZzKAOyRxve1w-8BSWfHwHzIXH64Yz2b74JCJYypFN1ok8dMKwfQfnwyzy4y5l1cEhxdyLEad1yJe3RioJvhJ4II8UOA7sXzpis9wuOBjE6RntyZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مروری بر ۱۲ روز ایستادگی برای دفاع از کیان کشور
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441860" target="_blank">📅 20:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcsU0jRhES4mONt4nJjmyX-JP5vCotrF92GCcr5UVeaEQFZSk9vpoO5RZfCm5bB9wt9S4OgOFGJ3NkvkAklsXVpte0njGX4JdqiHztB5ZPV4LyOgXAPpcc3XTRnMabQEn35Sf2YdTntLnP3raceHs6bVyhBJRfaoQmKVAEzM69diWav90HTvL4_62HHlPZIBKFCFsLsgJJdrmZUxKUe_RtLh3K_gPAkq3cuToSwTsIhCGxMFYVVVr5RADAPzvS3tV7TV16oJDCqGTPlvmxy-en4v19_cbyGMt_xsF-3poLpYTmEZ5cv0HvAOpqkYqcDduHv9PMnp3gwTpRnz8VqK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش غول‌پیکر ایرانی محاصره را شکست
🔹
طبق ادعای تانکرترکرز یک نفتکش غول‌پیکر منتسب به ایران با عبور از خط محاصره وارد دریای عمان شده است.
🔹
بر این اساس حدود ۲ میلیون بشکه به ظرفیت ذخیره‌سازی نفت ایران اضافه خواهد شد.
🔸
کارشناسان از ابتدای اعمال محاصره تاکید کرده‌اند که محاصره آمریکا باید با اقدام نظامی بشکند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441859" target="_blank">📅 20:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUOes2maMarWJJl0YIP32GMS_J1r1quxeNM6pOMNHcQoM4sy3dlkkiraoelFM6TZ746i4gz5tXygS-JMs5tTtXpFdumDGvTPW8adGk_o7YLADPPnbN-qdRtuBjU1fS7PBnVjNPHioPCqxE_SSKRNv1TreQm7vuiVn9wW6n-fBAd4j7Ku02VS-xhwdTjgTB8FshXu4YrAKcv_d1XjIIMn5aCMwjqRJDL2TQENqxiGnW_wMVuNfdP5beOF1klTPCkbaPDznlpvaCyUkx9oL94gV1XLPtqrqR15G_Hc_nTNSxcFFJYYcq_bHFtpadxLjXKC2hiPwKdSKtrJMMbLIn_bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در بازدید سرپرست بانک صادرات ایران از شرکت پارس‌خودرو رقم خورد
✅
آغاز پروژه چند وجهی نوسازی صنایع با مشارکت بانک صادرات ایران/ تاکید قربان اسکندری بر تولید خودروهای باکیفیت و منطبق بر استانداردهای روز جهانی
🔹
بانک صادرات ایران همزمان با آغاز پروژه گسترده نوسازی و بهسازی صنایع، تامین مالی هدفمند و کارآمد صنعت خودروسازی را با تمرکز بر توسعه خطوط تولید خودروهای باکیفیت، در چارچوب‌های نوین سرعت بخشید.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/441858" target="_blank">📅 20:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4b-ajHui-5xw9iRVpsOEmUy7aYyjWfrpRbksscdZEYzx-J8DDSzdybpD4lEjB1fTE4oZZzp65I_PBZgHxMic-uLVure0hXX8NDSv4-0RW0eTTxcF7vyNAsVrEZxAH9WY9WEh_-FLXqeJCrdjC1Q5r1DsOvJwpvkNpCxlznvtMVfmRVOLkxcB-_OzXIgRW_y6EyTZtfryOLxuev0ukaq9BvNt_RCPS87GtEUGjKpoR1ExA9lycdycKxtx-OHe072BTO6l3EwZs0TnWBqjp1UkFzP9BkvXimtr12wDXafLgqtSzXjA-5YBXbmAzhIIoPeWIMpHF5o3H1p-LESMO9PMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوایز میلیاردی با پیش‌بینی مسابقات جام جهانی ۲۰۲۶
✔️
«کآپ شهر» تلاشی برای پیوند بزرگ‌ترین رویداد فوتبالی جهان با خدمات بانکداری روزمره
🔴
بانک شهر از راه اندازی کمپین «کآپ شهر» با همکاری شرکت آسان پرداخت پرشین (آپ) همزمان با برگزاری مسابقات جام جهانی فوتبال ۲۰۲۶ خبر داد.
🔵
همزمان با برگزاری مسابقات جام جهانی فوتبال و با همکاری بانک شهر و شرکت آسان پرداخت پرشین (آپ) کمپین «کآپ شهر» برگزار می شود. شرکت‌کنندگان در این کمپین شانس دریافت جوایز میلیاردی، کش‌بک‌های نقدی و هزاران جایزه ارزشمند دیگر را خواهند داشت.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441857" target="_blank">📅 20:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441856">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441856" target="_blank">📅 20:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6FBsdUlcZkOvCnUDegwrHwqAo3pBGRvwm3IloLldmRTbhimz_yfEEbOAP6FDnzp28wFBoOOdPP5zwdpa7r1HwD-iJY-C7LpbODAVseFCSUgoYZg2WCPFCks97XhPwOFIIhmc8SXMJ0Qe4mKNUqJbjk0M1Pc4yyxjWASeIL6rI0S7ZY8jHTSdhcAFRzhe_oM7eSy_CaxewsF39_CPeLzk_t8CZKPZEpRZCDUeRS45Ct70W382-uKQ2lmdCN3Op48Fz19Uu46o4Gl-CNiZqW3ZaHdXrULSHi2ke8bWBFPeoeUyZrKICXBS4ZLRDtY6965t52qdZzW6dn5EBroJAselA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUk7ngP4tve1J6_XtXw-0mjg_drcWKh1h-lp8_PT_FMJZlkuqmOsBMmKINNPQUjqnT1bDHXMxtgUU6D70Zprvzi-7lyOmRgmB_M4nLjZG0JBaX-mVoVmw3hK-KfXfNpdJCYMfaPwWnYaUqOHIuyiGbTVyL0WdNxsDlyCVn0bG5fRciv5j150X3R6gboQkinRlF7TH7LEbmvcs5F3JeULFUIVOK9PWQiGgunVai_o_96UgbF989T_81yEnxr_wENMxvFpbOXj8pTPxwXk3jpEdSN9WZP-jKrnn-zWVeLh3Ou8R9rWKFqVhuHeJHIL8yUkpSSgYUhKpLx9m1_hHq1OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajgI-8eMtZMDsST1-jihprhxPQJBKwNPBjU1_ist3hGzUjSmdkyeCVFSJW9bBxIlrxJ9lh7zntPjeKBs0woRsSSLKkVh2wCR9q4uRsS_xGBVQ9SlBJkA-bSDFwJG6qdN5d5sBBhFV0uoBqzliRD8mAWf6dpzKUS2CLLRGEP3LSDn9j1Gdl-UWk7vyTjXaBHlb5yK03Tp72R8P1PwMyUZMNzFjs6RoBa11_CvLozhedbPcamKmiNdWbUlAbIzry-NxmeAj6lIRcP-8KQ3LRLkAKhs5UCw9h8JCkORGSAYGQDOVAptF1rpGeQehsPr-lLMlgY-efYMYJxjgAxK6byMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHmrthKLuA7w8v9O3UunWafv3pVid4KzobuQ1nbFgr3Fqf3ee8_fOg9YSOKxuBrgy0-4fcHv2C3JEFMVA5enFmnS3bJvhjsW_PsWxK1-KiqqjTmZgMx6tv-5z19ekkWPS6VtmPBUDLH7iWUPUuvzynsuu4WKzs_yR4V5ATTCpCEmT3z78ApF3ucyb1yJF1R1zeC-SpMCN6alsa9i8XV4YB_SfE_5XRuKL7FV9xHx9kwsZhNAEOTHXA7BfdGdwFIRc6ZMnA-GLLrWreqlY6fvQR35P2r2RRJb_9ctFZECPr-6ayKELz8MHnaekX2sUAhMr9wz0EyF6CXuUWNyss8vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnRu8rmi7xhWUxkJY7lRrFCbwnNkINYORPLrPCBfeTH2_Y-PhtItK_9rRwzN1FhpSONgZoUJkvAC0Ipq25kjAFOpHm6F4cGdp12HrOTLzCXs-mMui0RonFrMAXbTx0y6th3nEiG2f-QmGte5JGTa2KBkTyVD2CKl3ySULUAjwAzbFX78sjtY0jzqIDQU9eo-k0uQSkhNecn1UP26qWM_YVMAKXmcEyV4lEgRNY8GUOjlPW0yNTgN1-Bancu4nlkIsO41TmzoJXvH94-rVkJOvOAqJrczq624szTNJ8r4GryTk5GefcrO3jjvwJ6KfoZOpCE87SRddnkFj1bJK_w00Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر سخنگوی وزارت خارجه به همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/441848" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441847" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441846" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWpML9A3mXC27Jp3T45jvPhJx5QckY16p_cm5_C_REp8x5n3RJFY88F5-KR2c-Ft8xt3MN1sD-DN9iVXbMukQw5GUKirYKK3bGqEykOoYu-cvMSPruSWHKAH_4ReH2maO3Uafco920j0D3fU8dbDLLgCwf9Aq6T2hFqN0bEpZ97FK_7t2GcNKXSF96LIEOlXS0O5ktVV2mp5oU_FZyS0yCoqzld3ytw4lXy6BooX-iZlgD0zNOEz8SoICGebrIOvF-wWPngJGCFQcVTkTX2WQWjmEDpbGEK-qrWpRcUlJRDPtUGtECRQq-XeoHK3Nd4xo0FT3E3C2Fl01j_mfk1Fmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441845" target="_blank">📅 20:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نظامیان و خودروهای ارتش رژیم صهیونی هدف حملات حزب‌الله شدند
🔹
حزب‌الله: تجمع‌های وسایل نقلیه و سربازان ارتش دشمن اسرائیلی را در موقعیت بلاط مستحدث و شهر مجدل زون با حملات موشکی و پهپادی هدف قرار دادیم.
🔹
همچنین ۳ خودرو و بولدزر نظامی در جنوب لبنان هدف پهپادهای…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441844" target="_blank">📅 20:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Rp6m0vaPuuKBiIg_BLv9X1Tqp7SZnyZbAaIS01CvoXWykMcrBprG8320e4nqvxPPszmOUZ9vx3TTXO3UWY2RpRk4QVzw4Y_62iLFWBrX1GCICbovMqjqgvFhslGKwSNlPI9YSuiu1OotRZT7d4b3dlhjuG0f2f5r6tei_9hJksiJRiA0iBECex_LFOjePWrRyylmLaoEhAk4vaiNQPeDgs5Cj1LF3dUO5ZygZyVngCOmL1Uuvyq-oXxGMrhHTFpYrkVxH_Fwa3cZQ50y-il8dPEnu-h4wX0dB8x9JDn5OB4opzQ3S7ImSBkRtNtpgu9su-EksIbFN7FhR7rgTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: جنگ تحمیلی ۱۲ روزه، بار دیگر اثبات کرد که فراتر از هر سلیقه و دیدگاهی، وقتی پای ایران عزیز در میان باشد، ما یک ملت، یک مشت گره‌کرده و یک قلب تپنده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441843" target="_blank">📅 20:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال تغییر زمان امتحانات نهایی وجود دارد؟
🔹
رئیس روابط‌عمومی وزارت آموزش‌وپرورش اعلام کرد به‌دلیل همزمانی برخی امتحانات نهایی با مراسم تشییع پیکر رهبر شهید در تهران، قم و مشهد، احتمال تغییر زمان برگزاری آزمون‌ها درحال بررسی است.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/441842" target="_blank">📅 19:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyS9pbKHTBNJlo_KzaSUH8oZFCleSlEDrmr7jfzHAuMKz18yAZXILQkZljo3646O_10BmUcQLYmoLwZTgKNmccipOl9abjAHUFGQn72g2qLz4PQdEnRQgObFludOflK5bYYoY50k51mVd8SL0YRxlGsc4-vywY1BtsrnRV6hu-JXFFaq4SciyN8WAP5lxtw56MS_GT__HzglYjMF7Js_vlWcvGNnXqlcEF0wlliNGN8ctFlfiOK01k9TaC568yeDYb3BPfpNaQCO7tH4Gn6vptO0RwAyue6OObrUgjpa79ZIq9cj8thCpgchkLNFbxf4mDkwvYRjgcgHhe1RD8ZyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهدای نامۀ سردار موسوی و انگشتر یادبود به فرزند شهید سید مصطفی میرغفاری
🔹
همزمان با نخستین سالگرد شهادت شهید سید مصطفی میرغفاری، مراسمی با حضور خانواده‌های شهدا و اقشار مختلف مردم در مسجد جامع مشکن‌دشت برگزار شد.
🔹
در این مراسم، نامه‌ای از سوی سید مجید موسوی خطاب به فرزند شهید سید مصطفی میرغفاری قرائت و به وی اهدا شد.
🔹
شهید سید مصطفی میرغفاری از شهدای جنگ تحمیلی ۱۲ روزه آمریکا علیه جمهوری اسلامی ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441841" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
صدها کشتی منتظر مجوز ایران برای عبور از تنگهٔ هرمز هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441840" target="_blank">📅 19:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441835">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUSgQWGH_ukZf6yA9Y8uJhOr5TYn7IcXsmpSK3xnzsVrCbTJh4k1k_-pJ6D1ytMPGFANVaXwnOWZsd-REczwUkjQHNjZNxtk5XY1q0Ic8MhPde_hA4bw03kRr_Ov8K86FvNZDbSCpoliSmk8dolxubsoR2JsFzCCfMZU771QRmYsnmYGcIi_Az6gzTKb2hKHxGRcEnRqf922YRgz7FqxfAeRFSAnf022Pdtd8AYuBLe95Fc0xl3Z-9H1wBj9TOeYa9SnA2sFhjHw16Ci9028gZ2C1Ea0UxzGqgyU-TVDjq-NLZxdjgDZvS8vWEy2S9YD2xkmUL-nDURYS--9NkeYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0Cx934UK2kuQjmj2QwCC0tbpthgxMlwuDL3LbMuin-3umD_ZNIzOU1VFZn0yfKWX1vZnUa8WSjfkHe_SjGx1W8nH9UEQ1RUS43sipiuC_Nm9Sdgcs5jK--AqSA3Q-8dt09EUjzKW84ERnN20Bc2tGEpVeHgVT-zg6gPLnknb4CacZpwwv79UkS5ZVJRdy5o8-YRjqcXT2cjgHX6JQQ9rODyLjVLyv0PD8xEk30E478OJEerRcRX64mdyr_e6JtmZ6_PG0QB6-rcAWMuBG_Wm7f6nFxtyLfrzG4PICvGTzewxHfJSvAc9TNAjW5ohN7SkRxdGkmEg7lz6m__z8vWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0yNAffNZZMsbB2BJ1ma9j7y9pzpgbSsDHvhS8lM2zSCTggieoJZHnu214JEjUhK4DFe3pnzCRArPxIobWze1Hf49vuliPrOsyJ5IK_l_JbUQzgXeXnSTSj9y_qef4X9knrRz3lFNCwmX1uLl_hV0Hu-xmeQnxUtKnvGR_T7i_cnhhohMjj268-BtL9XsLyrPN9MgHRuT8IcIUVxsTLEi7UBP4ZnHH4RUnBX9J-OwbVK-AZlgLS0-r1c2u3ZllrxMSCdpHmJTIoRHFu42YIeGtTLRf0obZB_756LiAxZUZNNm9QCOXmB5-8dAajkZ_m5Tw4cG38MTX4wi8-6wf9Rqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d02BT6B-AkawD0Aq9Id1t7Wq_lD1tJtMOBEW0qF_NK8xqsKTLZHZewYE1tfFJIYrT5K3OayF6s6SdmuomaJhOOa49R8pivoUBwZ6-mIY3K9elbViusPwzIcIGWwqCA3RTLLk1cYHrDkLo5p-WRatI6rbwIjiNzybbIEe9dHrj6RSfhZXuqGCJeWiIi9P1qVIQF_cL7l8ezGbrFb_NlQiBQfnSxk0GW7vdRIxXb4k-NpbcBN09Zl6Q_y_T1XkGo7eOwQJzeKY_IrhSdRYCA7GOogfHA46TvnQ4xXasyWsLEc6HlrEaJB5K6K9te-bMSjl6ywL45zmdhJSYW9eGC7Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmZNXeok1ClFVO5ZkZKblwZApxDPdShWDQLZ9BPLX3-NNhk2LBTcgFZrTaMmYNmRKsZGaLpYJ3Gr0X_4UdfIfJZqyk0964zGdWMPluqYP_8D0NlyqdExgRR-RRVhxi8qghwxJyTHmtlTDUdPQHdvNsV1K0CLSsckYGq_KNJp50CsSQyNCMKlNUhhXWU08M8yF9LwZfv351vsyzhRk8fi2Fxz4CudGpASMSgGvM5sslZtX-NfdyAThXM0fbn_pMWXAc7EER_ArWKRa1uOs6aFUtKLY_l1upVDJGzonIBGC_FufdahqTajoA5O9WuybxT2X6WP5_ppPu0Hshi7gi3SqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصادف زنجیره‌ای ۱۲ خودرو در خیابان اشرفی اصفهانی تهران ۳ مصدوم برجا گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441835" target="_blank">📅 19:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441834">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0Gm4IsJ7UYzG2mEoqQYlBh74G4vsAsLsO175a9Hy6Hg0xS0gZHErEQ1uNgBrQZiRsjyK1yr6tfDY5Fq4MCvUnI-OjY386jZlHgeCT2-j6UHnX47mNUhZcvEiNkNHkBEqiObEVex1BdcSNeE-EOColDi14AJ9wT-ViMqifjUFph4LPiZaJJDn6HGSaCqMtuXiRlI32JRAAyqdgZ1qYD4Bbpw7FZc-hW5mg8_M4LA7hwgNfvD0mRuoYMJ0rXXXp8YM_z5VX-eNGMzKcZqDyqj71QbfBNBKFMHykkCytBkAU5t3ftBZvCVlt8JkEJzgqjgw3dOH4hzLZfBISVTbLlIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۲۱ کیلو مخدر شیشه در بندر چابهار
🔹
فرمانده مرزبانی سيستان‌وبلوچستان: ۱۲۱ کیلو مخدر شیشه در بندر چابهار کشف شد؛ همچمین فرد قاچاقچی دستگیر و یک خودرو توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441834" target="_blank">📅 19:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441833">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
کارشناسان عرب: ایرانی‌ها موفق شدند با صبر و استقامت خود معادلات منطقه را تغییر دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441833" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfAER47lkYZSwE_Q2V29AwQPsfTYlxA9cYygzQqGYKcEp3qSVY5m3aYImErGxt6IuEbeqG67TiBiiUhtfF7XKCK8t52dTHggApxb1JxooaavGQELpTj5G2FWa7_QhVTYrBb5S2XB1_4UgVQNXtLD4oizqYSyXly7fM4XtFLds4nT-GL_VuQ1haxie6oJLzRt6jX-2NhQ4qBtT070wf8T4LXgUCL16sN-whhHalv3rhySGPPR5-kFbbqZKZimveax8Ln7jCSpQe7uPx45V2vhMhRiZ0Uqyzp_odNK8ZakXkSTUmMMQj4xeiiJaqMDhZMQhkvaSgevhTlH6Ynhw8c4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uv6nofMd7sMgJam_DiGPBe9igVSKLBlIXJ3DJmtmkO9c-FqiL9y7dpib2HwYZW6fKs8HfOwpk4X19plVwp99TLHGkKcUdNnrdv9Go6KA-bddzzAfrq-4BHrGBpljzRdb4sGXRvzdfJb5LdEDovEKWhPNVy32XaJsFCO5u9bkVkwbuVUQosqrhPJI7dH895hO1VmzaDuGVqVOxqLl1QRvqhoSyShPFYKuEdhUX-3R32gtnKoa79BJZu-XH7g1dGVTuT-9hE-e1ZJyXpiJwmnQRzsHsghjGkklSOks1fHyHtYyAbnGH6HnC8eIusSJFxSn3_8pwrIB4DPWy1PbtKCSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHcMv-ee6QR0Iqi2gXOlCn8v5e7xEehyP-J8HkZU2TmcP459G8eK_BqD5mYM4VnniDU6fhV95Xx-0lwX-vILL7V_eV8eu5JTaCS5eCMUuLv5wFbkgco92rlqmin-H2_8Szv8N3m39NwwLOPQX8OXgipyEH3Cjw4rvAkDHU2ckZjF9iAFfRiAw2SJOIZs6imR7LkBfJHWZyHZEyGWbi_Lc8aBk6W0WYM6hiGL4XRloZTIwwlRp6yi7iLlrp5UwU1rsnPlbV7iJ9jeM2Xvy70vtgw4XOYnsdJy-bYyW-jQLApLAHiZyfOamceNro-BryxISDVfmenX64MSiDW6mOuXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV5cOaFh2Wd3e6jHl5oVoSBdBOLrsU-jMVBM0OKgOkD2iP28uBFgVZ8wtRO_zKXyze4cdhZt1-_tSxb2unwP5K-xUI9YmX1YqWF7oU24j-gCXM7UgpLI-l7Bx1ltbr1z70Eye1VQK9zZ4oWvcWDAsZ0LRbB2zcvSwymQYPWQXRTxP1YN1qBLEvn-rSe5vhi_MG-dL8Q-XEgvRQ0Etcf6tMXAMhxRto7nZB5ryVh499TcP7j2MlNNyv1UgsS-DEbROvmNsjhQEvP7iJJtNCpYQXhpJQ_Dumm5VFNYo-26q5cL5ckKNbJ8C2x73MiVBJKxX7pjGHyV0EB5_hz4PcBB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNMI70OjFftfY3xgxDb4sBq-0yq9evLT2b8DYkcnd0_sXtT8mnfyaRi3U49l0DoSLz_ntI-uBb2L_djQiJ98TPHsUtaI1oxisXB7GYPS1Gt6iOhlDeG4z6OfxqUvHpkky-kQ7fmTDxNVeBBPG2xnOhYdI8f51kcxKzLuIbo792W31dcNJJ-JhvMWwnqS6BZEiM2u5cmdRxTv_6pIBKBcr5FqN228pOuD10AJ8S10jVMZ283y9qWPM9TKvc616JMVkm31M8alXvC2ec1Afz2Yjx2y33nV09D13FKxZhw9vocLL8DtTHHSoKKLlkypv3PebAkZWAcVb2BvAN28SC7NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao8p06ngd0hgcUMr8npBHryunRRodBPKqShYitl6GfTDc8q4Uq8MuyDZ8JU5y_FrgdswVL40i12_cwoeQl-muKN9E0SddTxNMbxrW97CIQ6CHsBEt63eXPSf177vBMWwls-J4eOQxOsDSTCCiT3lMlqMlCEY1uoBjZEo9Ly8AG_IzRkO3ZQ7fyORv5A-Erx1VqC2fPZroERwq4-J492Cx6bezfwHzypb6PHo0u3ero7R2p3Ao2fNq7wXt13EDN_IuaBZBRm1AuVdZU6oavpc3NwN4wX-RTTbjGe3tHCkYWym_uLIkJHB3olF-O9dgpyO5wHn5l-FhZv7xIpycraU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcvRnb6IaaQ4mD2k5Bg6aXJGyvAp3eFDjReYfZXDVBvJ5ImS9wQ-AjxuV_dWw1rsleTkMu92VVuZdFGYY3bUXusNAzQ0-FpZb5WQqRWWDcRZCuMUwFBalAhHAdunKwioK-iLw29VyObEC7TT3us-tq2ILyDBIVmjrAdyzwFVeLvW7AUlYSWBuwOBvW_6Zx5siml1XIdwT71pP1fKBF46sUuNYw_LndFerhxiV8HNh8khycKxh-Tnl0gHtEy63eIPp-JQDWt9LqpDX4X1ppGTCZ5Fv-vK4_P9mugWEVwInhv_-w7gW0-TsYbfCIXdCWhaM8Eo8zDETaq8wtBsE2dq8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین نکوداشت شهدای اقتدار فراجا
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441826" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luQyU6l8gQvMN4-VrgaiXKlI2vF-v0wp85F6-b4rkSt60hIJ9AfUqvm-PQy2p_8-a9NSzsIpOd0HUvWyQXPoVrJW_n55rlgaImPyX2HD-hxzSd3vg3eBwX-8La8N4Qgh2qlFmQbz3AlZ3CjCZoWmTgb-6bARXJlzB4G9UwMGXaxKtY9Iyr0RC27wz8w9XYCSkYrriSxY81DLBkzLg8MHtIef9QUNcG13oD1iJzgtRNDMqVfKK97kQ7diNqn2MiqIZQuTCIDS2YCstAcJxMUIKiQ2xg5M0HBuV252u-N-hVplNQShdEdvTPzCZRd8IiliYnzMhz814Z-5nCxLNhN94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بسیج سازندگی: نیازمند تشکیل قرارگاه جنگ اقتصادی هستیم
🔹
پس از ناکامی دشمن در عرصه‌های نظامی، تمرکز او بر فشار اقتصادی و معیشت مردم قرار گرفته و ایران نیز باید با فرماندهی واحد در این حوزه عمل کند.
🔹
همان‌گونه که در بخش نظامی قرارگاه مرکزی برای هماهنگی عملیات وجود دارد، در حوزۀ اقتصاد نیز باید یک ساختار متمرکز و فراقوه‌ای برای تصمیم‌گیری و هدایت کلان ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441825" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۵.pdf</div>
  <div class="tg-doc-extra">8.1 MB</div>
</div>
<a href="https://t.me/farsna/441824" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۴.pdf</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441824" target="_blank">📅 18:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBKsSEm7XSciVkLf2uhZUn2T5SJY7M-flnz2e8Ru0D85i6gDjO78_m3EQxlqGyJVHe7O3g2bIFQ-efLsNjKZVjBvBygLDSMzRqKUSYikqc3klt14BICd_RoIW9vSKgKO2cvPe7bjuPdAhJwhz3zqeIuGwPsa9Abo7bkVRZRvzB8G3nitmnTBtWZgz6yxu3snsjWxiXEk3XE7gz12qVjEjLTx6fKdRl3b_iTPJVJO9Non56n6JIZc4zSUkkTmNnIR1xuTTKzAJ53KGmM1kHY2X-xX27mIytUxsGmvCSUWkosE7oq4DLlhA5n4sthUuBmPwUOy0LDZWfSinxDzX2k6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به استان نفتی «حضرموت» یمن، نیروی نظامی اعزام کرد
🔹
پایگاه خبری «وكالة الصحافة اليمنية»  به نقل از منابع خود در حضرموت گزارش داد نظامیان آمریکایی با بالگردهای «شینوک (Chinook)» وارد پادگان «نحب» در بخش «غیل بن یمین» شدند.
🔹
این منابع احتمال می‌دهند که این نیروها از فرودگاه «الریان» در شهر مکلا — که نیروهای آمریکایی از سال ۲۰۱۶ آن را به عنوان پایگاه نظامی عملیات خود استفاده می‌کنند — یا یکی از ناوگان‌های مستقر در دریای عرب حرکت کرده باشند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441823" target="_blank">📅 18:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0G-FuMoDeujeK9-lG3mkjbV9HHrK4k_W4ii5InAn3Flp76h11hcNRux9VigQ0H7uJ_9Aw7SGtszz5WBcEjlR0AW589XooyyQ2HU5fhswAjZlkfY3Rqdga0MLyHNuqVy8mZeaKMn-qU_zEG8gJ4g_Z7-8Z-lez2MYzxo49-ZY6cS9iSa1AAztENRCzKyntGhQesejWWa9lr9mk_PG0te0iKXlT9ZyvpsvCOrpY-IitxJazmwb-ukykD5GBAw02xf-k8RxhFWVO7-vsftobXoohT4KIMLAs0NawLJxFKS0PSwpz1qGTkj6nWe_uiZ46L-F674aUdYGjVAJFUX_BnVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح آزادراه شهید شوشتری تا ساعاتی دیگر
🔹
آزادراه شهید شوشتری، یکی از مهم‌ترین پروژه‌های عمرانی شرق پایتخت، تا ساعاتی دیگر به‌طور رسمی افتتاح و وارد مدار بهره‌برداری می‌شود.
🔹
مدیرعامل سازمان املاک و مستغلات شهرداری تهران: پروژۀ آزادراه شهید شوشتری که از…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441822" target="_blank">📅 18:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHyhzEr-64roHv1i2V2RvFw_dMkH8fhoF4_lrY-LUVnIbThklM4rMgRzNNdLDnCENDzFLOJUOJRl6HzGKbzAs1YUtmG4alRQFEvo5mZfwYEMjS3eE6cpOdBi5Ul_Xx3nla-vUaZnteFBVMgn32wv17-snCg2_hdooCADo3Zq44zS7g_KtFSbu465LVbnfbBND3WOec9RDJCBD2kZQUTzj55oaiL-ETqoz2Q1d7lRqvRWkn66UckGXIleBRDCZSPqZs4UZsvSEHrNIkkuWMTgHb9uM7YQAnB8mpdXPcfH0x4SgBZgXkyNI1zq6wM3EUoHnLnmmIaT4I6QFgsoYrIQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم
🔹
آزادسازی پول‌های بلوکه‌شدۀ ایران بخش لاینفک توافق خواهد بود.
🔹
قرار شد که در این مرحله موضوع هسته‌ای و مسائل مربوط به آن مطرح نشود و متمرکز شویم بر خاتمه جنگ و مسائل لبنان.
🔹
وجود پایگاه و حضور نظامی بیگانگان در منطقه باید پایان یابد.
🔹
اقدامات ایران برای مدیریت تردد ایمن در تنگه هرمز هم در راستای صیانت از امنیت ملی است و هم در راستای خیر عمومی جامعه بین‌الملل.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441821" target="_blank">📅 18:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPOtbEfrMQdNpnb0Hnjdy0HoT4AB662BfSLRrVGqXshCSChPQunIjhgyimwbcA9vAzi5UlCD4gShflb65MjxS37zlJ8hHK7xlgWFkzBgBVmjAXoxvsG8fpCht5ZqiMJ7BkG-eZSI2R0lb5gQRsWWk7goRA6vFWuAmVScgjvOmDdPkE8WOOC00MBDzmCunHYAVCwnfPAb2M61FD-fN4-oA8QDF579ALT54lUQEGbqrhc7M-ejA3r6jG-JXrHgelLN9s2G9Z-h1VbfUtGVMxnHXRglnvpE8LIcVTFcZA7u-UwtEw1n--rzY_Eu1vCcpDLJQ8tNYZpIzaFejAcAAFRLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دسترسی خارجی‌ها به ۲ مدل هوش مصنوعی را محدود می‌کند
🔹
رویترز: دولت آمریکا قصد دارد دسترسی کاربران غیرآمریکایی به دو مدل جدید «فیبل ۵» و «میتوس ۵» شرکت آنتروپیک را به دلایل امنیتی مسدود کند.
🔹
این مدل‌ها برای کارهای پیشرفتۀ تولید و تحلیل متن، برنامه‌نویسی و حل مسائل پیچیده طراحی شده‌اند.
🔹
آمریکا نگران است از این فناوری برای شناسایی آسیب‌پذیری‌های نرم‌افزاری سوءاستفاده شود.
🔸
در صورت اجرای این سیاست، تابعیت افراد می‌تواند به یکی از شروط دسترسی به پیشرفته‌ترین مدل‌های هوش مصنوعی تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441820" target="_blank">📅 18:31 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
