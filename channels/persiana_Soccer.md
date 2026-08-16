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
<img src="https://cdn4.telesco.pe/file/dEl35pfwlg1F4LSQuI8hgdiPJvwISqysML_1w75rGhbUaL8aw2ML578APf4FxeF6PU-7jNYEH4HE9lSHDzYoESYkpVnxECFtIH6zfMIhkdZKxgindDxHPHTCfvIvID5YELFCfqCpIT2aRsBt6T0SrHiRWBP1JLG2Tfz5SOsvqLRt49IQa4F8I_EDVy-ag6BiQ1RDDDugrAhfd7iunGkYNS1SLdsl7de9iKMhAk9F0JGPF9PNsRwkaL3rrHMXxuz41Rm3PkTBu-4YbZfvG1S2FaUpneZpHrfWWLmQnVbKa_2tY77CgsR0FvcfFybqrQ7KFAPapvB9dYg-fcqo_boM3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 631K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 02:41:14</div>
<hr>

<div class="tg-post" id="msg-27898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX-lY8uqZuDK0f8c0HKw0mjXvK7hKOG2WOtYt9ZvNbmKrYjGWgvgS_Gc1gENq6tPhDRBLAUbN8qRZ_ywG8qEmAv_jVYeRL9zz_UhNF7qsQKgDa9iFL0rOt80822zUWlB8j0SEAX5PWJGEILKlAAM-ml2K3WF9k7dsLl-RZALgpfLb-VXqXVViwd-48ADCQqcg4Fxm5TLa4L3EJFKBd5TRi9Wui8Eins9r26mt2SbarC0yBdbHmtHrngofphtvUKjRGbjhNQydaot9pM7QP4UWk2wclybL_I6UXmFDqsUpMRiPpgCs4mwSw0jptgHhdyJfHPz7M4AciqZ6CwW4KpdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/27898" target="_blank">📅 01:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4B_GtgJJpiMo_Bqx-FKbhFHFWKmykcb7l0m9KXmLi18rIFgPmdHNmH2Qt5TN09HqKkTBQTGMMHcQr3McsNZ893j8BWRti3XsxAJ7WXSwA4_GlZNuPUnmh-GX-uX-OHlfctYltueOkMKq9dSVAiZQGqiZdK-VUyCiPXFEI5kdCZKsgWvTiuJz7Ntxw5bM33N4gvUTrgo7aodTFsW6GIJProXEGmW0bulCzGVbKZh4EkxLIzV3gh3BfQyIC201Tob01-p6_esbaZeqV-IXXd04K0Jju4uMpbFHKBG7826zgwawTy1Ng8sU3rUVIOBBTpaNelbELHaAw_DR6PqKH7moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌تنها‌‌دیدارامروز؛
بازی یاران کریم بنزما برابر الرائد درمرحله‌نخست‌رقابت‌های جام حذفی عربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/27897" target="_blank">📅 01:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvMdamOt_XvfNb_4Po3ynqVPMHP8gL5994TfdL9lgwSa0pFLCQgQy08gzdMRViZB11D0_Wl49tQ9_gC4qT_5LwpfrDqIVD5lKr1GM7xMSTvBIzKgPGwRKlCKiaoGL5JBtmeFg8xjMbMDHnMPJldSvVo0s4x3gDeHJMrmpWQuQN_XtecwiRv0hQZ9y6KIulr4SZ0fNmdR91x9IKo2Y2TBnh4MHs1L_h1bj9syQNzGxRrpACT6h44xiAY6d54CkWmxDjBXMTkCvhV8b_mNqcDEtwpP7JN80QW26lNqjda8j4DTxuj7Mp6pcQtFLT2JXce61R5InFkWb-fm_7a2V6kO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
ازپنجمین قهرمانی آرتتا در آرسنال تابردپرگل بارسلونا و رئال مادرید در مسابقات دوستانه و از دست رفتن سوپرکاپ برای PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/27896" target="_blank">📅 01:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvbRDpBN89HhMFOs8rSVGXde1BqPnuwqXl_mPzStY6z6YVY3fpcqra6q-IckBBjDqGfQzHxctceJQWUycOtTjeBjoK08BQY0Ok_aBmNacgUDTxIj4CAoIJC5GWAmujel_-FmgBo9WBuEsnm3HFsNY8rXJd8_2YDf0UnG83bJZt3GaZOM4Dr52J7SB8TE6FHdvtW6W4fnwkqQ-JcMFccLu4FjcDd3cPPsR4NdDzjlyWur2DgcXTjmba-SVwZwZtcEIl0oTSQrv39HUNmvi9yXPXaPbeh40yiyBGonOc1-722YooVZhCoTX7TVUvZKFucO4Ea_2Y7XcEdT1eD0jgUX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/27895" target="_blank">📅 01:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPv6MzJDdzdkZA1mlpR3jL4Xx2_WvHVtv7vIRovyRqxgp0cnH4SxLMj-KcVZUJBuSehBrDgiMwOsTyA2bNlmD8NFPlMvirbKSyNurbPgaGOHBXU6c0oJ12_4pWsd_dqfg-J7Kcr74i6YYMHO_WHDw0thzMcYQJlBsIOsuxoaMcK795wmKpryp6fky2MFcYmcjV-4EUMO6T9vhuzO62y9It0MqFbDLZ_k8U12xoy0a8iRxhPNVjHMvM2KVcwXNNRrMYNz4qU9QpPtrYc0pBvN9pzywnWyc6hfi-vgDqZ6XLTuSDPi9g6k3RBsl3HYy64k4OPKXzQ8QpCaXaRoAWJkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردین رابط وینگر سابق تیم فوتبال استقلال در کنار همسرش در تعطیلات پیش فصل رقابت‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/27894" target="_blank">📅 01:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhQu489d26tFSddtlD7M98BPA4QmV1Y_lh900VHV077oqjYJbW5izcrYgStxCrIb46f1lqMTCrm10BF1YvJTDZkmB-qHHTzqfqi4W6nnk0WWa8EVROTf_9iSrfyQ_T3fLNRhMfbO73_4Jf5YBgKAeqLx7hJgb0md-5HvMo5ihLWL8lrPBj-JAIGrqbh-CFK0d2tQxRIPJGoe97WZJTJJIASadjNG0IeABHgZu9fZoVR3ZPFBD4eRE8Rifubs7QWHG4PFtPvNL_D7Mu7X-dMwa7gJJGvDVoLW7MnIS5XYKgZcyGg_MrbkuuXX92DMtA1BFl8bVDairWABlWX77S_BhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرجام‌فرانسه؛ شماتیک ترکیب پاریسن ژرمن برای دیدارمقابل لنس؛ساعت22:15 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/27893" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osdybS4v7KF7IzEZy_eYnJaiVnH-u_VxDioBkJlC8aHBp3BUU29PtGiWqfehzXGxuDcm-DTtomMjZHLl_bpxueoRvAZR-hd8k-d-mKGH-ektBDgitaew521_yn3CotWVvi89a8MN61IU0vOzxt3jr5k4rLALs7UmlAea13VYgA2vkzCF-YC-kho1uDipDAb6oA7aJXoadCrppaBrAsKwtZUw4p0UQBmdLj-9YP3ExeB1StL_nQdOsD7UFnj8W3PdRf-_lIjTCQTl_OBfEMHaI9NcmC2CboLpdhPAcTb0AZ-PXsQ6svdn259xSbHEXQfrd1IQTcRMNxC0uwvvRtZKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بعداز جذب محمدصلاح؛ باشگاه ترابزون اسپور با عقد قراردادی قرضی تا پایان فصل داروین نونیز مهاجم اروگوئه‌اییه الهلال رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/27892" target="_blank">📅 00:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSPB6hwQ_BgMRfSGMCvpjDaDLgl898omZhjc4K0GDOCSGN2PTghRr2uyxe1wspvV6Pvh7r1WWF81iBlFADZq6LntovJ5STd1OBbWnKF0N83EgoP6QWWxp8bLrhscmUxJ_EP-DV-0UXaHKr3YaqVtaLxtZ8g2p0ZIlPwYvYBsIMXGhXIrKILlcXr6yY4Btx0y_8raEZojv4vJGuz6Rrw2MtqzayLywFjIk8E-_Kp7WDrpeh_FAvCMyr1w46qXEFY0ndlepBmleggUABGECTqrg81K15gGbYvTzSLt0n30MthIdiIyfdoU3BpqSwukzx4lRu_NdtVNqH58c2A53vX0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0O0SZmaivxlIAn_LXp3PgaybXDFCg87LfYZeNMiypMxLNvX8g570RYnwB_PPNAM6YSO2dhj1Qrkvt1aKGbm5AkZfD5j25drZsl_ybZyBXXVCbZDZh7iCiwfvZ6PDTUDFyZm4hMPsF8gZOB2BEHq7a72g_sdFn2_c1vHBMwt--NMWT9NvilCOh-G8oi7Je80nD5Cv5ZbPmsB_oOXAXbgb77Zv4OdtZb6xtlBSoFBjduhknQCjR534QtMiryVayR2d-7SFr4ajiNc79gSz8HdO5UwOAGRNsGOkHLh76aEcZUQW7sQkiD0qoLsXUGyU015kH6Q67Rb4hjaz1DLD1LGJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/27890" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtJ-XQ59aN5dQvr5Jb6mLe5hglIwFmB0vX9T3ll3Vc_rGJgrnwQFUK3Zsw-JorUExO3EAl93oneru0STYMIQ6bvI-n4j9QMFQNHf8wZD804_KZNF8vo2WCyosP-c03Rf0qe9UNEQn9vPm65y5eaO2u0cFYR2TZ1_qytk87728mhMyDurydxPCnHdcLV5SPRilG3nyW199ka5P4Jm_WwenUU_qs6gfg1xAsNJs7bYZSvh8PjZti3fhMrmE3UCcVxKXvIESNnpWSelOsLpQzAx3uNUf98FPbkfK6oGizqEd8XsvUvvsRM-t6WN1W9vYqc-sr1BanaNnhRksFkxVzvv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ سازمان لیگ و فدراسیون فوتبال بزودی درخصوص وضعیت یاسر آسانی در استقلال بیانیه خواهند داد تا هر هفته جو مسابقات لیگ برتر با شکایت باشگاه‌ها بهم نخورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/27889" target="_blank">📅 23:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGWTsaCsJGjwE8HtkoGtypJJCmIAvi0nrDLNKuC3DeEj44iwIJgnHZThk1tx2ZWauJa6s6wuB93yp539P7DQqiSVokd8n4aclMjp3zhtVwsHvOV6yGwd3hLP8eUMiN5uG_soVwOI4Y9rBAUZ7k-wtA1e5MbPylbkgNGKS2ntn13gxSj1Iju-RoVF-pRk1hQgb6tybtboQ0Rl5nx_vT1z9PPH50TJTAw1gLF2nj1epLr-QaOCpDIGTG2fs2AZNpPt1BPVYN6QvEFBrXdGpqFoTzPgkz9EOmqrgGW0bFP7sZtXFpWN9Cy4f5Ui8aBlCa7PwZUbB0H3dALJAZgZYytOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
دوباشگاه ملوان انزلی و استقلال برسر انتقال ماهان بهشتی ستاره17ساله‌انزلی‌چی‌ها به‌جمع آبی‌ها درنیم فصل به توافق نهایی رسیدند. بهشتی در نیم فصل با عقد قراردادی 5 ساله آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/27888" target="_blank">📅 23:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1G57u3rkkC3SFib2SKkcg7phIq-vAvBnN2rM5Ng8_DMkPE3zKcnT1lTUmLRT1hZFcOZX0VWVqqHT8SczOV7oCBOT0jlmv-NbVl4-xzT6mqV38QvxxLZU3g50BFPfSOmU1PCKjRP_wJy4T6458Lv1PupPfjoQQE2P9L0klevEt9bzewA-hbTaOAuDZj_l1SsJuwxPHv5ebTCpZ39XLI6VyFxMhd5SAwVTJyZ18HXcYiGfks28jxPURnr8og-yF-eblmSHY4o9Ws6OAG3WIFKV3imD_462AMTEsOmGx4ltd9XPf1FbYAVIWNae_QBNlHymvuqNubrfjhAw_CU5KSF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
بااعلام رومانو؛ رودری فوق ستاره اسپانیایی منچسترسیتی با قراردادی دو ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/27887" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=Dmji1rKKslF8rKAPOaWZQVhJlpl-z5iKAZ38nfw04b4wbe11fG2nXIk9iZkNs4weGOVTzHoIEeHHbmrcmyckZmb0T3T5Gatq93Kk3pw5QSmaARUAiqoXbLKjLUKrp73uHxivZ2cMr8hd092kefMVhONHatloWzJoVsEbkxYu8fvM6y61F3HdLCQ3N6NftGDYspA1oJYzsZ0y7KzeDzAwaMEeesYTShehOSgYD8vUVu34P32Enwv5RhvfDyQludhaeveaw8CtFx-QIgdKIrEX6P1KS6CD9j-b7vDowYBhXgr7zvnhLZViBSQ4FcVvSBCYnyTzWitb64OTYwGJTxlORw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=Dmji1rKKslF8rKAPOaWZQVhJlpl-z5iKAZ38nfw04b4wbe11fG2nXIk9iZkNs4weGOVTzHoIEeHHbmrcmyckZmb0T3T5Gatq93Kk3pw5QSmaARUAiqoXbLKjLUKrp73uHxivZ2cMr8hd092kefMVhONHatloWzJoVsEbkxYu8fvM6y61F3HdLCQ3N6NftGDYspA1oJYzsZ0y7KzeDzAwaMEeesYTShehOSgYD8vUVu34P32Enwv5RhvfDyQludhaeveaw8CtFx-QIgdKIrEX6P1KS6CD9j-b7vDowYBhXgr7zvnhLZViBSQ4FcVvSBCYnyTzWitb64OTYwGJTxlORw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/27886" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIuGNxOygR-LTOhFWRc2yhsJckyo4b0InAj976MIaLlavAqU-yRFyCSqUE4NRYnB6l1wY-vZkq2GvZuYFq2pCGPMTr6VQyj9SGdFPN7y7CzVMj9EyeQQ6akxfgOO3wuASOehUumW2vZUXrmpbdTl9z_7jmUqHgKrdXCmaKa3BiE7RMzE3gqV8rGnN-X1FHUy7IISM3CusY_n0mNMT1KDSDTdU4BPPg8-bkgYrVSpNiJgv4HauMRGwV0CeoEI_Vex9GwtsK0bMHOuaPJ7uFCftUYPuRYO2UgUxw47gErM2bu3h7Ms8FUN9eSZHBttNM48zdPTLEMQ5cjrpi_mqOoLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی و شرط بندی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
تا 20%برگشت باخت هفتگی
🎁
10% شارژ اضافی روی شارژ دلاری
🎁
و15%و20%شارژ اضافی نقدی برای 3 واریز اول هر روز
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
g25
🎯
ادرس بدون فیلتر سایت:
✅
https://mafbet.com/fa/?btag=260368
✔️
کانال تلگرام سایت:
👑
https://t.me/+8eCDvbzSV5JlZjlk</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27885" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm2TKI324l5Gj7oQrUy_0icydLcCKXJUeXgEdY15HlXWNuGbS-2QA3o2SZYLUoPflUmEFmFeG78eBjjIui7ZIEc3T2gUn9OxusQfZAofwrZUu_iiJ0EfwKcFJRgqUNWpkfDom-Fm1Ps7rLoliPmeBGBKY4GeZ5LxaC3tbBr6qpRkBTTBLNY5upE_r54Bn7DAaIR25JhHcCtgzS7MhXnCZjLWjrxm0CktkIslQO1VgimHhTXRg_wsP7MfNk0wIUT7UD8L9S14ugPPUHBKaGMCm5wo_1oQ6fADwbdItBomFrUjadDdSfmPqk7fi1OGdz35edOl3-fA0UwiT2M1_w7IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/27884" target="_blank">📅 22:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnv1pdihnzTPvEEMMV_-gTFQa_PPdTTcZcLIXv3b5feDy-MD9W5ytryz30O-FxngBX2x-ElXb_hFh6EmuYOFXluqqnmOaaIGpnhX5E-K6IYQGXzgXrcL3SsBmzD0cK9zmwdQV0XpKhkQ_JEQxdtSoplNNrkaaLyym7G381F7mKlq2f-SFR6BVl1AKzAvYlZlcqX6HOTxhjg0ZFrYFyz_z3A2KrWdPaw5OImI5DwBhqPXRhbEDgLGZ4XcVuBUgwEekm5sOgPfgTo8VlSAOJvo4Tdw3_Kap11SC_a1xhZ83s6am8NMyuNrWkPXr57JETMqyS8Z_JYhJpSWY-vJaDH5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/27883" target="_blank">📅 22:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkN3vaZAOXnAi4HYs3Moptv2uWAygjFmzQra3-o-v9qxRhdDrwVZHp0iywRA1AI-ZWvqHLZpK31PIbWOdb56PhgrBQDdrIcZ-pqoOnvA993wULOx9nqzCeoTmipqHfhT71aVd8t-ldGAZYF4Zp8StcbW-Da3AdqTMjye-HS0RbIad6X55nvGmWbULOphUcj-pAp23GJb_gnBClV_6M7Ymrx74euf5uqWOeMsuRcsZ7chQMjrvQ47HXrvhFvXYJK2ndLPYXzTD3LqKb609lCBuC2HS9nepSmbqHZ1XUsh0Mf5vTGwkVO1ppZV8MxEiYaBLGXUCYXTrgXhDTa41pgPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیروز گفتیم امروز استعلا فیفا میاد و اگه مثبت باشه باشگاه‌سپاهان از کسری‌طاهری رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27882" target="_blank">📅 21:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH8we1siwlRoiUek9jnb7dSqeWMY0P8igvZoRNaFlRjNIDgIgqz_2rTpNj44DcWXi57uY-HHXt5dKyhAlzduwcFSZpNEWp6tCMeKVDFZiABiT5k1cGRLdZM7_JhufK_FlWh9QPLVq1_gSuXY2NkolKfzXt0FA4LaM14C5Pd6vN46iqVH2H7aW8SUYLE_GgYzvYgIuhCeqyeNGTNK9xiOUi2rI3y0lq7svAgWOy_JaKp5rc_yPxyNE6QioHL9JDEsdbtU4uJ2C4D-rnmYubZ-XrUTs6zZDr9AQEqC67JfZEPnHcAnYsWGGfcBhsmtTSnwnh-krN4clHE2cI_swek1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرجام‌فرانسه
؛ شماتیک ترکیب پاریسن ژرمن برای دیدارمقابل لنس؛ساعت22:15 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/27881" target="_blank">📅 21:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgpSYrydI3QWg15-oq_4kbcXXdzU6GQEQjweIyrIya2vVy-5ysAF4NGKtttJTZJdwa3zEW71-x0mjg4W9DUHQuPDUySu4hsnMAuJKgyGA31IKPyv4sXxhh15WxlCo-WLeCm-ZOkVikRnGDlGYMIkEsd69y3I7kbO5y2xjf4oZURlcn6RoP51qAT5gz-a5hFonJlqAbK3ovAdQ7MLwwR0wmwjV9BRVbw3GIkfVANTEZFeor_z4EzITcTdVUOQo22WU5ButRKMJ8nbDiLaZ416OVVvCxV8KNDROxZzO_cCy7Jw9UcnlFpBzELCjciV_3-wZTpDT4BR2eLPvcU0ElI6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژائو کانسلو مدافع راست الهلال قراردادش رو با این باشگاه فسخ کرد و بزودی قرارداد سه ساله‌اش رو بعنوان بازیکن آزاد با بارسا امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27880" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smV1KeQL_V7PT3Ek4wAryDbnzA6GeHdpAO6XIBaQtk0vvJhiCEShrI-z3cL8UMcp6P7xGu6XV-3DrmI70LR-ZKn667CHcX1r5Dz2oOFlakmzKsaNcoN5TTUsh9v_wLD35g9zMbupOT_KHn-nKpoT_jNoG3DmqnWq03DHeswYt5HJKRdUouqDVVRTlyXjwFclxKBuPuvmKlPTIzbinTG2Cd0m8wDixHOZgo9gFt7fPsifbVyWqYEwS8oEfa9MH0T1pW6uchkZ8POGEgX-jWBGS62TIGYGWnM8488cb35-2aW53d8ifnHF8F3Utf-SoswwosF8bYJo2tLVlMdIC66zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27879" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYX-xpmhRAeD-Zvw45-X3pAxycr32uTkhxu_BwBYhAhwZtqMq9rLvvF2lf14Ia4_HeDdQyksqrbs5K-L7nyhrVvpf9zKXOyUyBBFsgOLhrJDUMRVMxDJVEmD16eWu7ESyzyTmU05M6JMq1CMhfbmxyOrTETcC9QlFUkUwkL_ZeOJBbIZbMxUj3gsQu6ECWOn7ziqSnvA3PoYlPBCd3AexUfiFArCPl38M-Ry11RSX_USqhMk27ee3F5zhvShJj8Y0duTztpK2OB1mwZsa2GtHOhqDU62lgTjtpWlLMfAslQRRyV6KZ4frpZq0jpvwGx4MFEXoHVqGGvrAX0y7Tnj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6gMXIhGA7P9sZTt2ooShK7tSAfGMJbhP9_4hDkyyEbXCQs-gktpvEOQQ_p_WVEfrVrIeaoPZe8XGCXLxqyzuRJTJen547KmPPoBqGyfPW-ji-_dD76mPCfDMrUaydwM2x7zN8h8HvkEkBqyroeZ27pJr-8gfD2ZOzdFeLqHcWJ530e-e8vMAenR3Cp0Ue5gq-1KEYabAzqPIUFSiswt3ac86zJlmuiUpLprtCLu2zsEXGk0KKOcE5zRpss-SZiZeexB4il9k9k8K_tMTJZLAz1nxPl01Mc-zShFrahUbbMXllrAPjeMVsVgcqt6IFI_7ONfUQBZnoCY28BkzcpiLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
دیدار های دوستانه پیش فصل|ترکیب دو تیم بارسا و رئال برای دیدار با بازل و شالکه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27877" target="_blank">📅 20:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OONfAeNbDTkjK6dTNK0PRQP-c80tNv3mgizFgwrdmqMU4JILQ14lqjiycpdJwu0JG6Pn4ysbVtaNyXSWQakfs-ThyOpfbgYasyf6uw_kOHJtJlqOfQ-46xNeHuXLMIv9AaVMF4OiZDgEeG3taM-2mI_-Yp2tSjmJaa0Oh1v2hA6w5iKoxYcZHGIoZQcuDbZgdsDjZH8aAhQDGa9y-z05nMCNktK6EmzGIG78MD8ZmiTjRQ_3sME-4ax_u8OmhEHNp5nM_1IsV9QCwFOlWyv0tPZ8atC33lhgKJ2AynVuGRtr6L1zfQ5eVecUE16wC6btHoorjBtciwSF9-FWTsZKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27875" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Adarhepuv3zVGvBt1BA-Xxo4JMXnpDGeKZrxB8fmoidGIPG4z0vvX7wQyoev4dVqM5iFq8i9ClJq47Z0XdJlIigLd8ZI_U2BeFvI0KTCB7LCjGsZvH0cNCDg9ZgRJnaSTRUHa07EdnQY9cUYOzR_0ZJNAMe_CBSgzFIiTaoTiMiJTvQVom3sjVLPwler_21y5G3rtfSqPkOwfNwkGcE8AeaYHxdk1PGAVmVMuzxL_bWfYgjowtEYGTu5fXMX14a42xHnJPwF6h_n6Wstlwc-T5wneTfryWrmF4RWICfnbIZwalj9DMg4EPv-0b2LifBHrcEMLq4G3KNbaHvmC2QP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ فرداپاسخ‌استعلام‌باشگاه‌سپاهان از فیفا برای کسری طاهری خواهد امد. در صورت مثبت بودن استعلام طلایی پوشان از خرید جدید خود رونمایی میکنند. قرارداد منعقد شده و طاهری بازیکن سپاهان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27874" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
کانال‌جذاب یکی از رفیقامون که تو حوزه میم فوتبالی ایجاد شد. خوشحال می‌شیم که اینجا هم کنارمون داشته باشیم شما رو مثل همیشه:
@foodbale
با رخصت از فیلد مارشال قلعه‌نوئی؛ اسمش رو گذاشتیم 《فودباله دیگه!》</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27873" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Gz-GMpFgnGav5sKzZ3yaJauedTlcB1KC3VXDZh4J0kjywbVUIiku9yNJjdLEXIvzFa0jemOiDVQZH1tA0IRz3K4UDt9CZmLeweDDcTniXDR2qCssvNw9uV2UbztFQsgzCJ99fm3d-7QzFxyHhTKOdJrTJf82FuhbFZ_DyKMg_lZO1q1nnj7i5A6ZQwb2ES_9aI60oriibVs5oJjXWQrW-gt4uatrICA-uFGTEayi-x4cO4YTIIJ5SQQ1HdWqgQ5s2MPcFJEVD45Il9cSs-Vsrqtqr5n5EyvpF8pnMM66WbhIru4DyRupE7ce5slhsIRgOujm3eYqWLd0H-w_SZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27872" target="_blank">📅 19:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvYiWEypJ7u7J66CbWS65R2BUJsfMmHVf7YU2p_hhZSbB3smEe6WFYYQZzX_TVzfe9H6nznVFz_dhBmIvewgb-ICqM24T-P5mpDXL4qQeUKXTh8x1OFKdPmKSUbqSduCvIBtd7sDU5Nqdoxh42NJJaWF9G9IVi5nDsgZLd3j7adIRQ659NTgALc5eBRk5VMigslWpAKssfhPcwBITuPUn_h9bsSe4vgkTWYzhp6p5PC3UPRn-HFMOTThIo7lX-gMcw3mPjyNT8FVP93_ZmDKoNPy-HMwpi5MssOuyS8I0emaAaI8RT3JeOdCdrgSvKqhW03Bz9xBmI2Avq8KuBV_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرکاپ انگلیس؛
قهرمانی ارزشمند توپچی ها پیش‌از شروع‌فصل با برتری قاطع مقتابل سیتیزن‌ها؛ آرتتا با بردن سوپرکاپ برای رقبا خط و نشون کشید.
🔴
آرسنال
3️⃣
-
0️⃣
منچسترسیتی
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27871" target="_blank">📅 19:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHT374ijaZELMLf8s3QOo7sYcPWk42TNwq_2ojIxGI9q7HpWLimakWu6JylFHJG5cVz8MwsBeR18_xRHhGNY9OLx3Iplkcbvg7sg5Jh0T7NVfpxLpw8gwZfF4Vxqh6kRFJIIcT1njoZJkFBntlB7QKyaiGMx_29HVu4I-2lNWAk46NSvEDQmk2Nki-J8zVnlJ3Q5LO9SA03E0LUqmuCGxvWDeYt553OErCOYF3waaVqb8QPCr9syTENTbwurMPGbV4oYyNHkHUFOGcjHZjPEb2_Eu43hNfAq_xHHHXMuSHs9HlxN_2-KG433yROKlbNejNb-8AR1rvozToZUe_vyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه الوحده تا دوهفته پیش حاضر بود با 700 هزار دلار قربانی روبفروشه بعد تراکتور میخواست با 500 هزار تا بیاره که مخالفت کردند بعد پرسپولیس اومد گفت ماحاضریم 800 تابدیم یهو این گلی که زد و باشگاه پرسپولیس هم‌جدی‌خواستار جذبش سر این قیمت رواعلام کردند. قابل…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27870" target="_blank">📅 19:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWYHTRkv1n7aBbse6J27FHR5nkD_xAIZQbsPqpfnnlBqKMMJmNbShOXuZ3JclcHCXZUqsom1_Mv80MS1FaQ6MY1sBFJ6wy_maSfsSlTrc4a1gLY0D2npuddr75ufr_dbjGW_1XhdU9Lp402pnCzvEOil4zr4IYPo3GFjfdoeNpKIPRP_M-z4rBHR6ZudCJLa01JXWNWszpvrn8HUtBTcU4_EOeySpR49Nhsaxh4ZgwZEl_JtL2FU1dWuUbVsOER81_chQTmboFOqolbk23hN6WWt1Q7F8gAfktuDk9Jc8lv8Gi1vhBPsqKEhKo8tR8PeUVUD-PDO_u0sxZ0cRYXlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#فکت
؛ باپیروزی 4 گله مقابل مس شهر بابک؛ تیم استقلال به تنها تیم لیگ‌برتری تبدیل شد که مقابل تمام تیم‌‌های حاضر در لیگ برتر به پیروزی رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27869" target="_blank">📅 18:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrpBI-ml7eFCgqf_Sp-xyd-9M3NFykQKXLwAXdm0AEzbecE0K5ZcuQfWqGAgfuy-TCg1y2VMNsn-vXduEEq5yM07qP-lLID0T7I46-a9mWszsdTN9RZQClvqCsbW0a00zmar3gzJA2Ca1w7JpgqcJ1KyzTlsPVoia5Y6x1YouygsnXNkybByw6NSsuoOf_B_DSgP2-FQVnvtpMAQznNehS2H2KBGxk1XjzeyalzePQpYlYrwZIE2YzHUnyJd6W20Ob_EmiU7NBJ4HVNzYlyqMQ9UwshHk7TBwfMqLn07989ADbbhylzVKskdsRtMiJZn4T-9E9y7yNsQ8jvJ9wEMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان اسماعیل کارتال در هفته نخست سوپر لیگ ترکیه باوجود تموم ستاره‌های این تیم با نتیجه دو بر یک بازی رو به گنچلربیرلیغی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27868" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNWNPruIWHuWVozirvt_meRE_SPIvrQ0yEua-fzMJOSagH-xR1Csr8Z9kc2NO3RLhvFRuhKHVAkDqkx9_h8srtevgFSCesqF6s1eJu71zLi8mIK362FBtUc7xXC6gPxA1AP79d7SjeraXTnHnOBrMMibUMzpOh4n0H9mbg7IOSMqfB0l7bYooqTu64ZWntO8LpGK_2R9LiA9Dyo9lur790XxdZgH-WqvXBVJLghwtJHM9xKuc_A86Ubq4Ah1BrLQ0LHKE8-KRRwezlEvIwbER9PHZ6G8NtIwSSurAuFjoZbjIKSD36O3LpnhGkn5k4A4qNhsWE2gd7SwziZJo98GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فوری
؛ کریستیانو رونالدو اسطوره تاریخ فوتبال:
احتمالا این‌آخرین‌سال‌حضورم درفوتبال باشه و میخوام یه‌میراث فوق‌العاده از خودم به جا بذارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27867" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ_Ed3v8pd5Pu_dKc5V_1E2FpOJRsT35di9aJlPx2f29LQ6JAfu47MTDju4DKRLa23HRRzdyYz0sglNxO9_WWqum2CdVU1JrapVWJ-vOlolxVXxLeo3IJOHop1AA3NhWySYuD8mq_x6-RJffR9DH7AM4J9wFKLQK82XqzgtpAB1ZasyoPKYrrTJboURV9kYRU_PP9a3bpsCVpIDY_o3uvw47Ujyv7c4dC4UUpyuzS-1X8dkOEO9rvsLB6HhpdZ11w8slkGhUIHSqMsdRHa0PTedhAwOXdyGZrYmhhZSv9TOgeuY2UYggmMYFbTR07o-3_Ln5JNLPBiLmfkWsrYqe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسامی داوران هفته دوم لیگ‌برتر
؛ بیژن حیدری داور دیدار آبی‌ها شد، حس اکرمی هم داور سرخ ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27866" target="_blank">📅 17:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHA5Ny3WTyfy-_WGb0EI9YqR_ZBA1dhcSnQPt6aoG4iY-GAyqpjia9k6J0HNqouREN3TUymRuvcMmDWUTDTyZP7iipgqrwDBUFYOLcd64lC6ujmz0-IsWZRdhqGDyR1MUTQRE7j1KeFygtigv83tslscaxfVKZTIXNwp7EQ9FGRbCmWYtwApQ6iPGzuksTz1anNn0f3GXOQO3rYbYSOJekqDuqVIlybQB5FhhTZ5v_VypiMfBSNYobkMHSiczAbzSGbdspMiMEX1pUTU_fwCxG38bdxZOPRbzdO1XibOf1frgwRnIrfdw-CDX4ink_8m54uDN3sCfPRkfvrNtwg8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27865" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zy4_mPIdWjncssuJFjqMk29s2mh1lCt9zfs4NFmvO7CiNaBF3FiSd4xPebkGcTF1IQ-16GWR3n_6I5hYM3CbHpbsF2PdHpQHD3uFUoD7ppwS9z2Tp3Kq2xMK4FyXTCAH0bRYIErPZHjc6nxMmQr9aUeDrfLGrIXWRejLKd2yeJX4ocBkTK2xt7zUmwdQ7e2duzMUw9ENF3qQ9DSo0rEPBawRq_8orYNQTVOgRz6f7vOQsD92FdRZ4spWxhd7W042rYVsc455-e2t25eHlFLB7tJJ8Kn1b04v7cL5svehkS2_kzYrDN9z0Yy_4fcqCkZB7L8XrH0hofw6ksX0PhuS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5fN-UlWESAyN0Bhp7f56tmvAEt4YGTIvU5aLg99v21_RV6L_N6cJ_g0RTKlmIT0UyPXDQlEw-5VLaNG_eyBRPBa8c_F_5WuJ1cyhPpNE-qGM4_iTbklXQcspqLX7m9ZLLm4qUa3FFw-lJk_RZZZ_u-4HuRdG9T_qvhkFlFZRog63YavKZwZgkvOQAGm2K8MRFWbECgL0Izgessxcdx_3pHwUn7g4sPjoMW-V23XWlk1d-XZJdiaE2MJIiDnYhdluVMHYzAcU1v2f9cbXIH_Di1XskFzoz1NZeRyPKiCMMBltwZE-va-iMF2QGU1jyEpJKq40NR-QEdpwKn-PBiF5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
دیدار های دوستانه پیش فصل
|ترکیب دو تیم بارسا و رئال برای دیدار با بازل و شالکه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27863" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBUAJrh0JZP2DcwvSfcBW3mSC_3WRuZZ9pL2yGQTJB-rktYjD6YQkKPsnaIE31Hq8P6vpw1qvQ9Luc9hqE_xSh8R3FA67yr8Kxu5QAxsO0fdxIh0jAw2iQ6_gay8MoNLiun4lEPHiXDzx45mVN5rQbbloeCZ5aUsr_3Da4Jl5Gd0Xiab9d9_I8LXi1whr7ybEaY4OVRQ9hLumWqkmPYXYDDtybnDbypTeHhGhQLzOATG8l5pd5thyr3HyRb_vKa6DZWUkKUrtNwktmDgESExrEKYCDfptraFiDnkyJSy5P_3bXLuZhw5ojZdYKh84Z17R5jKztbC-ZjGjFY7vRa0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده امارات دقایقی قبل به درخواست باشگاه پرسپولیس پاسخ داد و اعلام کرد برای فروش محمد قربانی رقم 1.2 میلیون دلار تعیین کرده‌اند و حاضرند با این رقم این ستاره 25 ساله رو به باشگاه پرسپولیس بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27862" target="_blank">📅 17:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWRL-NnANgHEAtlrmC94FpMGKJeOrWbjfxdO2f0nrvMshPmsl0jQRg8oazcqMvNFa_aqHXlQzggZJu3ESC1iHcrivcIjHrhvxJcL3dtDGrbeJ2ypOk2jT7kBn4ZP6y2xThwKLDFNIsNmVYT8Npc4dJ_erylCV0gX0GOKwTF94f1wl7LnEmgCpZbU_eq1Su8hCFby2oZ3RlwOyhpJ9ZLXwCD5yt6OPOF5MkZ_yEr1opLfWvmGjmd6qrUTxPgU44uFlJ5ukUpKhg47gf3DLCVke4cw0C5O19Zl3CHSt2yv6tiFskmHM9d2CvLuKn4oD2zsuWjskKxzslAdeM3ai5ygMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛مدیریت تیم پرسپولیس دقایقی قبل بار ارسال ایمیلی به باشگاه الوحده امارات خواستار جذب قطعی قربانی شد و ازاماراتی ها خواستاراعلام‌رقم رضایت‌نامه قربانی شدند. ایجنت قربانی مدعیه با رقمی بین 800 هزار دلار الی یک میلیون دلار میشود قربانی…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27861" target="_blank">📅 16:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
تمامی گل های هفته اول لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27860" target="_blank">📅 16:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGVej5rz3Sw5A04DCAt6cE3KIZMbu3KhpXNDlatEFSBneMdXRTh_yT9WGZmnWLuLx73LIQsplnqDdeQfJG0CXpx_pECOoDSITOvYzkbbihsoUCaRFnj45YEVWKGI7kp7KVk7G99hKxqDxux7K86xvfuh6cDRZC3-o6EeWmPKtb4vv347XLM4PZhnHg1qyomRMQ246I2rc_d6_yXj6b2aE2A6FrBRwptkWHz7OWvNovRrNIA1753WmAFTB8KLz4P3pzlHS78GynE5DT7uyJDYe1k6qGRbbCfibxlAJbJgEK5N-kNdkPlE3IGulpx4EjoiysXVecUugtrslmR13q8ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری داکنر نازون مهاجم31 ساله استقلال بعد از پیروزی آبی‌ها در گام نخست؛ همانطور پیش‌تر هم گفتیم نازون به زودی به جمع آبی پوشان برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27859" target="_blank">📅 16:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Wd9XCH3xnSZrrjdgjZdLCMxzun_NZVlOjvMPVDKhR4FIay6_BOMj2i1RmQxp1ET6FSbN7z-9IZRn-ewfHHR_nfLW0HJ08jP5_RCwmnZ8BAzkHgvgA6Kwn3--dTv1bTSwVCWJYIyKBuOh4MhObcHsN7Ztxlc5_g7Ctn_WvkEiNkqjDJU5BWTq4pffrkk7Z1ioWZXArx6aiy6PnHJkMLOMJLSbMRfTl9kBC-vxu6Y1ZarrfEI4enLJRY78GP5qHSm9QKAknujHj1PLsOIfY2DP2LON6sXsvJNsMySxxuHrCoxCFT65Df95rVBecyiksvf72xGuPpxlarn18bbbtwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرکاپ فرانسه
🇫🇷
پاری سن ژرمن
🆚
لانس
🇫🇷
🗓
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/27858" target="_blank">📅 16:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34645ec54f.mp4?token=kDLGd0Or8lQfpROL7dGXiXp_mwq3LX96rQQYjXjyih7WAsNgSMIm9-70LRLOqubtrN259KoINbX-GQqFCvQMNL-zC1mpP8DhQ5S7QnBp1qm2YKVGqVG6ydOOr0ZvmpC1N0UElZhL6vEJUPqzVyy46IT_LLDrAPnL9uyZskECRyLJ9G4G4Y2XMT3i9a0JGuSX8g7VKOgXJcHAvoA6Pui0nYN1es0xBJ8cWHKsjWOgqRi-mwqFh_2bh8pPj9AQLmoZkPCKl8oNqvYLtqgwKhTXlCXMHQy47RfjUKGp3whRUZV0wJa4rK5IWQyXpT08heYCqt5Bf3NZxMbQrmapHlzsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34645ec54f.mp4?token=kDLGd0Or8lQfpROL7dGXiXp_mwq3LX96rQQYjXjyih7WAsNgSMIm9-70LRLOqubtrN259KoINbX-GQqFCvQMNL-zC1mpP8DhQ5S7QnBp1qm2YKVGqVG6ydOOr0ZvmpC1N0UElZhL6vEJUPqzVyy46IT_LLDrAPnL9uyZskECRyLJ9G4G4Y2XMT3i9a0JGuSX8g7VKOgXJcHAvoA6Pui0nYN1es0xBJ8cWHKsjWOgqRi-mwqFh_2bh8pPj9AQLmoZkPCKl8oNqvYLtqgwKhTXlCXMHQy47RfjUKGp3whRUZV0wJa4rK5IWQyXpT08heYCqt5Bf3NZxMbQrmapHlzsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیدر معروف باشگاه پرسپولیس شب گذشته تو قزوین خواست به سبک هواداران تیم ملی نروژ تیم رو تشویق کنه که این سم خالص رو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27857" target="_blank">📅 16:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s45tI9vEZpw6pC_mD5FtPrS9VRd2HqwpenxzU5M2Ga4W-v2RbxcAb50oSNAwdvn6ma7xuXqF70Hqiqy27FIg62OQIljze5j3PV0X5fb_gWGlEaMXrCJ1-xRf2P3MmQwqaK28EFEN3FBcQy9_qKNLPkd-t7SOCSPPhHbfH_h42xcXYHHcWUNhqzH90INv0I0W8_NGTK6KRr__wda-VKrbbGAADFtPyY6lwGmGGXAq_SuPenskRKcCl1aQvAKmBkxzbmiMG8y4eWXLh56FN9Zn08nqvwlWvByJjfJ91-YVAXxH57-RtXFgAerxfm80nwYKNGVE_tyX-cwXPWRzzKzPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
سال1998 زیدان مشتری رستوران ایتالیایی رابرت بود. ‏زیزو اونقدرعاشق‌آشپزیش بودکه اونو به تیم‌فرانسه اورد و سالها برای تیم ملی فرانسه آشپزی می‌کرد. جام جهانی 1998، یورو 2000، جام جهانی 2002، یورو 2004؛ ‏حالاکه زیدان سرمربی تیم ملی فرانسه شده رابرت رو دوباره برای آشپزی فراخونده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27856" target="_blank">📅 15:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLQ_FuI9LKOOeytV5ybgPslvd2N_x5q0ahL7jhKVAwN0LguHQBE0cKlYuKyoHYLmfwdlPrnjUEIo2uZNj_qsgVHpbpH5qowlbPbRpr_FlrHylp2UjjS6D6TTy-tullLjFzIPQaDV2WKQ-oe2stpVANUfHu77ejtaZ_NfOcgazxBFBjDuG3bvUDgvyVmwr9R8KMCFG3WAJL2p-ZBB6qYlcUnxU0S1ajQgU-XGPET8HflI-SV5Odb-CyZQoFS2MLia-1dHxskcWeqVOYJQROgVqm4MAgHoCavtMekb_vP6AwYp85VnFretIYUQ1oTJionaKLcpYr5QR8-mTd1nQnSQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi_Hld4Us-7YgTPG1pKQc_6D4Z6I5Keo9GDF0OhBbyX0YX6x2Y8TrKP68i0oL-lju5qWj4_lw_KQmFYV0SxLugF6NmkRIiJ_l81Y3s0g17g_bES0mf_GZ26XTOvgn8-bCU3Q_JHoULZauhRuI5fkYQl1QWgn6eaFnaYeCms6jWg4WsARCgdM7vmECMd3L0kDoKJPJCwlPqYVrvMdnZywT37sBm18YiJTVNfk98FTebj1XcJEfS2EvJSFJD17F9X5CqcLKhr-tThXLV8H_M-UshEFik1ysdiuFN0a4-0zFTmFMOLYRppHu_G_Kb5ivNcjordrSr4SFv2_cBIQY65eVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
توی بازی دوستانه بایرن جمال موسیالا از شدت‌گرما ازهوش‌رفت و پخش‌زمین شد. حالا استایلی که اولیسه زده بود توی بازیی ای که جمال موسیالا از شدت گرما از هوش رفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27854" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27853">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-4hltyED3ubFyoeGbRgnAxFuxzRW2MKFYhXWH0tmDS9UKnoC3zdCuciZUFjhQHFTpHTPUHaMzAnHnqdJjyxRlwH4H7LxL1V6g3Us528a_3_YPL0r0PDevXWnjPPMuyFYrdCTWvFZJ75_bgG9HANoToJbkz8_psgwLgYcxfsx5p6QmcAI7RdvnTR4hCSTt5ZcANhEm7rJYTYjMwjwzXUvQZS98M0KWEFVLaqTm5ifP_Bdzh4F9rAMYVf46soJC3uj6wsfPXnImPASGZ3ggobszt4mOxbdQhI5WHZbN6YGpLBGi2UPTGkpiM8Y9yQk7fVr8RVMzujFn-UJ2E1KI1ltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27853" target="_blank">📅 15:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27852">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK6NP8kiZDiFSh1dykurvWw-PRyfLGfy5DNdYfdDtI-Xi5fClWcQZVUQYk1vZuqn-zTCWHdzY2K6qTvl7camfqJjU1wc1P0d51lumEq56_YBb26RisXBsoHGb_43Z9NS-ohceXcMYcFseNf3gq3JYKDWiKma3BHtP5d833X5-R002gkwKbbQet-BATicc8FvO-Gskyy1MgePuZMIjx-_foSViYHr2Ea5tB1hi6U_tfGIW6DGcpvx2qPBLoPvtysugNqRN0yxCxIa_j55ZWMrKhNirMc60lzHcP3Q5dly1NJJl7hvc245JauwqTKRMqfSpMWWlIngV4klYmjVP5LkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارکامل دیدارشب‌گذشته پرسپولیس
🆚
شمس آذر قزوین از نگاه سایت معتبر متریکا؛ محمد عمری وینگر سرخپوشان بهترین بازیکن انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27852" target="_blank">📅 15:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27851">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzBij8795qFtbdxDxAopZcB6cCS_mhN8A2Ny8QxeCPpZq-ovPK_R9Fmv0J56y-1muY1TbNkOPuTh346Bh7t9Xn-m-OYjPASlzS_w-HSN4fQjZDVWPBYfN62HE3Q3GvYKXvmCXNlMp_-LQ_F0cTeunmyOkpbUpiyNY6VQ3v1QEMRQipCxBhrDEYEXY_pDQIuP3PejBOk1mN6zGeiguPMBytLgVzTenT9VQ67EDoD8a9QcaIjbdYEAMpjiZ7mWTREJ9LoDDmUqiw6u5eZKVxyODa0CNa22292t2CSsea25F0jwa81sTj2un1U7rdM1KIBHeVaZnbE8VjwLeZ52HDb0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ سوزوکی دروازه‌بان پارما با قراردادی به‌ارزش 35 میلیون‌یورو به پاری‌سن ژرمن پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27851" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27850">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmkHAx0Pmeve4mua_Q0m5JSFbZl-dtVlnD0Cdp1WW9tiOCcfa1kwL5tR0RnT_uSO7Gj-kfX2artMf6OWHoerq8XtRKS1VeReEC2BfLCvvCAPpyqmLY-ThSqo2WmZePsbK3qJ0A6uVZkesJUni6ZoI_EZ1-zkDC1BBdyZE9nihCUoI3WvPDHeunn4ChQYO2fAdaoLiK2PAB_fy1Rim-SHH1brFJpXudbspVEkAMR0yYvKF_KiOMCo54sl0ds_dzaLeAGlVE6dG68GDCQBtHphoDjVZu28tPSPes-tz92ivDzyWWjl7oYPoSCsdGhMsQF9jOmyY4G-UFxG74U7uAbo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
📱
🇮🇷
استوری‌جدید رامین‌رضاییان از صحبت‌ های مهران مدیری که گفته آدمی که افشاگری میگه "منظورش گوهر فرشاد" کثیف‌ترین آدم روی زمینه.
‼️
بااین‌استوری بدتر اومد به شایعات دامن زد و در واقع مهر تایید به افشاگری‌های امروز اون بازیگر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27850" target="_blank">📅 14:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27849">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31636a1eaf.mp4?token=UBsf-CL4bXVrXTJ7rcfnMR0pV9_42ZWn-1cmM8mgRDJIfG_h_p_MKvIEuleEBArEOYo8FvI7LKXoJPrHSjOkfWOFSxTE52f-yyyIIe49h1PyOEHY3JMRCF825O6vru7HsKWv7kuaUN6hD2o9pTaHV5Jl1S2Fc_aF6GZk8ARVr-4jJP78lo936n73qHKmaa7G8icWzbJaukcp-Ic-fqmp73Pa43fhGJNXK2iL9d34fK8revl7Mi3KLvtOez4-RGmbI1ySNBuaI2Wq90F0yVtf0boVlkvJ56U_OWRGH-H1cINGc6unRuISf9_9EheYK8sDDNa5YUkmK0fEqrL_3P2MDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31636a1eaf.mp4?token=UBsf-CL4bXVrXTJ7rcfnMR0pV9_42ZWn-1cmM8mgRDJIfG_h_p_MKvIEuleEBArEOYo8FvI7LKXoJPrHSjOkfWOFSxTE52f-yyyIIe49h1PyOEHY3JMRCF825O6vru7HsKWv7kuaUN6hD2o9pTaHV5Jl1S2Fc_aF6GZk8ARVr-4jJP78lo936n73qHKmaa7G8icWzbJaukcp-Ic-fqmp73Pa43fhGJNXK2iL9d34fK8revl7Mi3KLvtOez4-RGmbI1ySNBuaI2Wq90F0yVtf0boVlkvJ56U_OWRGH-H1cINGc6unRuISf9_9EheYK8sDDNa5YUkmK0fEqrL_3P2MDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27849" target="_blank">📅 14:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27848">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVwmayrVhi4tY2egytMzmuFYjhtNUvx05gDB700WDChPTBf7Y8qViNqjdO88a0-g1Ue7q8ttfCrhIX-cWqVmDuMlfo4zjfsLnkblfFCOdwrLIrBs6Vh734JE5isFn2b6OKLhb-g1PIx9wczQ0nkxlbUoy29d4i6yMuAIQMtsvPbx43QTRfM54Jc0vgPEX8bBuKRp6TaYya-jR6A0-dhJgcoIwvc2T13KtLyUFyvt-oJ_ZZQK5wlCR77FxOPKFhs73kK8OLoi7FZbnAD_QBbyBkcBz6SMJppxaaIPBUU49EcxixGwRzijibtLYa9S7Ewyijxro3R9MKFnC9YKesKyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس طی 48 ساعت آینده به شکل رسمی از دانیال ایری مدافع‌جدیدخود رونمایی خواهد کرد. قرارداد امضا شده و فقط کارهای عکس باکیت و انتشار پوستر باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27848" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBJI87U2CpiisfZ3dAot8-oACD_uJ5WtnTUfbny1lENnlwaXY92kk1m_49a6JZtHM1EvZfAobssI6tyU9K2Na2TmzBqiRp-QtyKctzsIPkhvQyGbRaosMUuAkl-5edJjHmMVSUkZUmtx0riOOUhAC2h2aWUNTViUdAGLbF4exVxE_i7bBrAi1HNVdidxEE2X3uSHyIndUGca2RNfTzwf5h5qi5TYbWaMYO4kpZuOuxTdniRkSI8hqsKAOOPQrV_5PEf2_YUKs5za-3IvgSO53coDZUuic5g9yfq2gWJuWiGCgwam6cUAAJQNdT3ka_esXC4LxivuDUakVPdMkWo1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDbbGBhQYZookFe36Yo63cUDq0wcl0HxQx1qqQCjOPsdpjPRuu88SF_lkDGcPxg7NrydNAJRCkCnvrsXcbf1T9ue79Yl1PoVw8Ngw6a__yObRZ8K3z3JKJz9B9Gyk1woVYXzSgF-JCS-HfRU9xriDSXdNpxK75IvWiV4rqlHrzkFH3Rd9q2_s2YNOtOLwNjlmeLeDBni8y7opnctQE8-AVQLwFQ_PUB6VCnpeZSgxkQjhgHnOTPRlSLac73JwGt91FSqHxFLtypbbLkIf0s7vQRpnbpcYqbsfyYIV6mH-tbDc3MManiELHI82WE3Eu1t-x-Q3ufP7wPm5R1f67BozQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
از هواداران تیم‌تراکتور درحاشیه دیدار این هفته پرشورها مقابل پیکان دررقابت‌های لیگ برتر مملکت
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27846" target="_blank">📅 13:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7268cc3cc0.mp4?token=ieBaqHgx_hnRctieRsV6MifMe4BRx3J1Un5Eaqri56auG_f3d_A5FWb0mjtYNQ2sdiemeIZ9BDKJgJm9ke1Mv_jKaH2Sx-48AwBdO-3utsKVZG6TWpk1GmLE1KFWeCz-Lusj8mZ69ioTUvxazFdvxEBCuzzfJ_4OkZv8KIE97DYK75IlZe5LtCVSTmieINwoU8CyIxxkc7BVSdFIKo4RbdK-QidS-OnKZ31on5XxI0Eligz0qpYGYI9Q3nP_JK1aXVLHbGIId7JAE6LfK1RUHljE6jBSYxXJGTfeCkX5PQDZemoHXoUSrTYjBS2N4P90cT42r1zjWuo59NrQjv-QLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7268cc3cc0.mp4?token=ieBaqHgx_hnRctieRsV6MifMe4BRx3J1Un5Eaqri56auG_f3d_A5FWb0mjtYNQ2sdiemeIZ9BDKJgJm9ke1Mv_jKaH2Sx-48AwBdO-3utsKVZG6TWpk1GmLE1KFWeCz-Lusj8mZ69ioTUvxazFdvxEBCuzzfJ_4OkZv8KIE97DYK75IlZe5LtCVSTmieINwoU8CyIxxkc7BVSdFIKo4RbdK-QidS-OnKZ31on5XxI0Eligz0qpYGYI9Q3nP_JK1aXVLHbGIId7JAE6LfK1RUHljE6jBSYxXJGTfeCkX5PQDZemoHXoUSrTYjBS2N4P90cT42r1zjWuo59NrQjv-QLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
👤
در پایان دیدار این هفته فولاد در لیگ برتر؛
خبرنگاران ازحامدلک‌میپرسن مشکل داوری مسابقه؟ لک هم با لحن امیر قلعه نویی میگه فودباله دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27845" target="_blank">📅 13:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toyd_a3L9J3NPu37054qbMS_rcEjzR0Paks0GKFJ_tcRlaAKlKXB62y5hc3-ymYpJQo6iNl9FOGSUgTdcJnmryH19z8ZJBaB6nvJLXwULxStu0_14PIIBGopNABBdo9IFvZbmuyDWGOkhV3P30s4d3IiSABZ2UllXm9tVb2RyFn2uHwluiT7BlCNnEvcsE0ae914eC3EwFhAzIT0WYnfxzT3dCwM0aleOxzDxNYfGkAsna9mBL_8HWF8jBzF26NNnQIDvf__hB5pxHaufaJ1tHLKuomcezB5MhbrN8QLyMCo5XRmTG2vmLyBNppXcjUKtbyOs3GgO3C3w5j1f9qPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایرانی‌بس‌کن؛ بعداز نیوفیس کریس رونالدو از طریق هوش مصنوعی این ویدیو سمی رو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27844" target="_blank">📅 12:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03eb44360d.mp4?token=U63RpowTrWYpV7wPfUA4ZdGC7tjP6J0VjdAFcY7r8Eu9QEqMYQ0wajwkzrqfkz_7gmWhJveLz0ns3GS1h7y2zoKbM07AGLJFofYU5f4KC3sjnroAQviOibvcu46CyYoSjMiy6L8RWZFrHh2eUYyAeYTN-kALejojAlcC46NbC4rPgJdixYL9ZErdXHWNR_xS5yuDoFVZYJ5h-P4kVI_JFW826m2GzamDhchFdO76meDcMKZl-PsQ1n0ZvDCRxUMy4I7NfFGLvYLCqfCuzJig2BQF96XYr3DaPsMbtkqnJBa5EltXTxUhhCqkJa1SqAw36yIa0QPpA5Rta83_C7AshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03eb44360d.mp4?token=U63RpowTrWYpV7wPfUA4ZdGC7tjP6J0VjdAFcY7r8Eu9QEqMYQ0wajwkzrqfkz_7gmWhJveLz0ns3GS1h7y2zoKbM07AGLJFofYU5f4KC3sjnroAQviOibvcu46CyYoSjMiy6L8RWZFrHh2eUYyAeYTN-kALejojAlcC46NbC4rPgJdixYL9ZErdXHWNR_xS5yuDoFVZYJ5h-P4kVI_JFW826m2GzamDhchFdO76meDcMKZl-PsQ1n0ZvDCRxUMy4I7NfFGLvYLCqfCuzJig2BQF96XYr3DaPsMbtkqnJBa5EltXTxUhhCqkJa1SqAw36yIa0QPpA5Rta83_C7AshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌فوق‌ستاره‌آرژانتینی اینترمیامی با پاس گلی که در بازی بامداد امروز داد تعداد پاس گل های کل دوران حرفه‌ایش رو به 420 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27843" target="_blank">📅 12:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3iykrlnV58B-BwqZ8DVvoT731QlcaBc2HC7BXIfBqsFhCs80BoqHkGctB1qrcVN8z95QMF3Ihzsw2ThjrKnKEYeg1q16AvKIR5E6S_EJ_X_2PhMCUZR8cIJASuvn1WAu_rq3ju1-Pk1cv15t1Sgx6UqBU-7sZTjVmBfcpJhXZ53ZxzCnLdO9Am969yELhTln5AzCMumS0zx6oAxuomkS4k5nG-ENnl2QbTXXhWV0C_sknj74RDLqtZvdWZ-QxZDdRufMYhbvLt7NQXMmw_TNMlFKqfWF0FDWUeDnxFrA2T7SWu8FM4fkcAX5L1JBGih8Lebs8ouXkLBl0sgYmCaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
باشگاه استقلال باارسال نامه‌ای به فدراسیون فوتبال خواسته که بازی رفت شهرآورد که آبی‌پوشان میزبانند درورزشگاه نقش جهان اصفهان برگزار شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27842" target="_blank">📅 11:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9833c653.mp4?token=vatTt6UkNDiHuGNZz-U5Ja8asG9i05TENLwnRPElOmzttqP2DsNjXEqeE1U616edgAU4uOFlX22PZXakWx4P0kNmW0RBjjXRRiD-gDtm2341iwlruqZhHtQyt7or0C-wjQXV6f8OuYPQiD8CpmSHYfKy7koYPTJ4z0WEc76nhAgWVv1lMEceCsfZTVBnqrezwfavjyXca2H02DYkSWkd5x0n4BGdDl9rPWuL05vBeZ_oFBrOw2J-fBqnWvIQsDF4ZNfflqTkhvMaXKYmj9chSDGCEdoabx5Vyj7s3NFLKRJzZ8tYjN5i5XxEE-nTC97tpQ1hSE7rIWdNVKPuy0rbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9833c653.mp4?token=vatTt6UkNDiHuGNZz-U5Ja8asG9i05TENLwnRPElOmzttqP2DsNjXEqeE1U616edgAU4uOFlX22PZXakWx4P0kNmW0RBjjXRRiD-gDtm2341iwlruqZhHtQyt7or0C-wjQXV6f8OuYPQiD8CpmSHYfKy7koYPTJ4z0WEc76nhAgWVv1lMEceCsfZTVBnqrezwfavjyXca2H02DYkSWkd5x0n4BGdDl9rPWuL05vBeZ_oFBrOw2J-fBqnWvIQsDF4ZNfflqTkhvMaXKYmj9chSDGCEdoabx5Vyj7s3NFLKRJzZ8tYjN5i5XxEE-nTC97tpQ1hSE7rIWdNVKPuy0rbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
متین‌کریم‌زاده‌مدافع‌چپ صنعت‌نفت با این شلیک فوق العاده دیدنی گل اول این تیم رو به ملوان زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27841" target="_blank">📅 11:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcnGifospypZtjCmb6oxh9r7FAJsIp1YMNtG55Aln4Ywp3TOFqfVeLkHhseg24dq7AM13uaFjUst5xrOkm40rqmLsloRql2jJbiat-VcthaxfFesz6vzsaZqa1onzxX2OOCzU9yUJvIxBvIrCI4w77Le3nAWXHaafRm33rVuxINQwfyZ6nu4ouuI8o5WXbJ3qESz54JjNvAxJGGcW5B6W01HBQwQJOUJLqyJ1T-LOhmRJZ0USt1akhHznM34Pvset81U-4TaKKvRhMudoHydD7jCTAoYmdN88A537_NPemgA_vI04cQn1cZgePXusOoVuMAcYHNhTobDIL6Da_43Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27840" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067b53ca3d.mp4?token=nNQ73HKBmzSH8jBQfp5Ygh8ygoAxePE1hD0IXq8DJrjmaZAlzRpzD-OxA7kdSyIOy6H5fiDJA4miZcJ-bj_AhbUOubvfRZRA0Lw8RKX6Xn9WjBUwT5UpLgl7niYWGgy2CGp-ruKDkBnfYkCkP73lxf7NzPbILfMtsvS_AAYN23_Y-PcL_82pY8wuoqbqEZVjpWuppQUKXm1aHFPKIcNwmUaJAgMCLV5jUKewQwgKRH-CwGMs7McudtlQZDXM4sC7nOmICwPKFA347oQFaELxSPD0G_Dok-AXoDAPmzCq43t6kp_vBxOONO7Rzn4wCKr3WWy8aMFS2lGiMEKVDB9IEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067b53ca3d.mp4?token=nNQ73HKBmzSH8jBQfp5Ygh8ygoAxePE1hD0IXq8DJrjmaZAlzRpzD-OxA7kdSyIOy6H5fiDJA4miZcJ-bj_AhbUOubvfRZRA0Lw8RKX6Xn9WjBUwT5UpLgl7niYWGgy2CGp-ruKDkBnfYkCkP73lxf7NzPbILfMtsvS_AAYN23_Y-PcL_82pY8wuoqbqEZVjpWuppQUKXm1aHFPKIcNwmUaJAgMCLV5jUKewQwgKRH-CwGMs7McudtlQZDXM4sC7nOmICwPKFA347oQFaELxSPD0G_Dok-AXoDAPmzCq43t6kp_vBxOONO7Rzn4wCKr3WWy8aMFS2lGiMEKVDB9IEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27839" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=ePAbk0AKipg9M0TuTpWVXHkrbN3U1kR9aZP5Jem1ES6rV0OyNCclKIbX_XVAp-0GdB3bNaDXKdRvrPj3zZJQ_A282j8FseaoM7aD-l0YcdoxN2keuTLlpTjkVwXmkwsTrAbom8iXx8MIYPJO7SFXP0qseeNv_KirRzF8xMsbKNrKAH0-IqJXDIucpUkTp_uL16GHxFGm9r2zcmTyyV5DsK_0gUnu_LuQeM6AwHmgI8MSvjuzaduwzeP1bHVdfU-sUcRGPSVb6SUz1e3pqCgv5mA9kRXNduKiVwgm9kVyYmGBVc-nwjEZCqn6fSxMeNBfiF1gjnS9fsZW_o11aZXjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=ePAbk0AKipg9M0TuTpWVXHkrbN3U1kR9aZP5Jem1ES6rV0OyNCclKIbX_XVAp-0GdB3bNaDXKdRvrPj3zZJQ_A282j8FseaoM7aD-l0YcdoxN2keuTLlpTjkVwXmkwsTrAbom8iXx8MIYPJO7SFXP0qseeNv_KirRzF8xMsbKNrKAH0-IqJXDIucpUkTp_uL16GHxFGm9r2zcmTyyV5DsK_0gUnu_LuQeM6AwHmgI8MSvjuzaduwzeP1bHVdfU-sUcRGPSVb6SUz1e3pqCgv5mA9kRXNduKiVwgm9kVyYmGBVc-nwjEZCqn6fSxMeNBfiF1gjnS9fsZW_o11aZXjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ویدئوبازی محبوب Chicky choice
🌟
فقط‌کافیه‌مرغ‌ازخیابون رد کنی و پولت افزایش بدی.
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
betinja.bet/affiliates/?btag=2760677
⚠️
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور
⭐
کانال اطلاع رسانی سایت:
👇
sr25
💠
https://t.me/+K0fAOE9hCUo3OGE8</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27838" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚪️
🔵
دوباشگاه ملوان انزلی و استقلال برسر انتقال ماهان بهشتی ستاره17ساله‌انزلی‌چی‌ها به‌جمع آبی‌ها درنیم فصل به توافق نهایی رسیدند. بهشتی در نیم فصل با عقد قراردادی 5 ساله آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27837" target="_blank">📅 11:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsnDBfrY_bQYLFWj1FFSvEuoAyqKVVHl1ajmzefBCjfxy_As8vDyI3QIIKraqcM4EwpfIEychnQDbNAMbtUIarCFCsjo7deldGOiKHxEGRr9pewUenWqsTettyv38Tycug6GOjL060BxT0EsdGA0QO6E8Laf1k2-zsTZ6DznAcnRBEGWWHGpDlSLq_YAl-hDJazi3qBzucFAeiSe-7e9owt7NjgD1ISmqOpdI2xZxi1yGAuzdyffmpiMfWt_A7AHOG5dYBVPAqypRKrgF02WjUCEntAQWzDHV2PeaA9i-0l620omhm5gokc8I7JkVdjFsH_7GxVmlSptRc8RMfye5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚪️
ماهان بهشتی ستاره 17 ساله برای عقد قراردادی 5 ساله با استقلال به توافق کامل رسید و قراره تا نیم فصل قرضی در ملوان انزلی بازی کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27836" target="_blank">📅 10:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2GKDnELiGjmozW60hTqxqHrBCrI6AZGMpKPG-16C6cUXBHALrNgzOVYOGdQtFssuTSmBCtMs5HezBkoOINpLeZs4tk5Ckd2s5PbdXF3GgChGRHthEehPIoZ-R9vyMBEe1fdHVgmQdm5n6cagQMGrrLpUPnAjVRgi2HnntDhDnLTBU2jJDPLlA5vCglD_d0_FSJJFZgaaslr9ChczPN_CT-EHv3mv4neEcFrQQ0NiWBtSByo_lKGe5ev_e733WHmcLn9kQETHjR54HFBmYy59qVwXr3y5bH4MoY6y86hTjbrMHSTGLZ657eUG8kXiSAFSdtJ5ja_IzauYxF2LloDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌فوق‌ستاره‌آرژانتینی اینترمیامی با پاس گلی که در بازی بامداد امروز داد تعداد پاس گل های کل دوران حرفه‌ایش رو به 420 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27835" target="_blank">📅 10:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNABSD8ZnPplnHcehVXy35o-DrLvNtzYSdMqeTpOrmFnIygbObtuh_5ShG_44_XxBFS5SDU2gpPvHURQi6QV_8YiXiAODEumwwNhF9ccJ82cS5s6RgMJvRVHmBAIQgh5YW3KH3GDsjvqspRRAG9xO9JYopn1qDSMaVbxZQz3wsVtyF0SmTgCmsnlMcKI_WkRgT7_XFtzWyCEXHWt_f8AjxUIz9rSCjtAZNEwRu--45PgMNvcFr_-t2dK6CGnP0okJh0ZAx4N0UNeh__os8zYwQ1BTBg8bU0BN-MEFuEEWR8eLB5qYCvhVdCbDoLdRWApHimrwoU6C5ncuDsngduD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛سهراب‌بختیاری‌زاده سرمربی استقلال: اومدن خواکین گیل اسپانیایی به ایران بدلیل شرایط منطقه منتفی‌شد. یک مربی خارجی‌که پرسپولیسی‌ها خوب میشناسنش و روی لیگ‌ایران نیز شناخت خوب داره تا دوشنبه به کادرفنی ما اضافه خواهد شد. من دوست داشتم رامین در استقلال…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27834" target="_blank">📅 09:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27833">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqiXPZXDOElilrva1KL8CN1yMm3TVLtD9RyXFPBNqMlZj7am_Bq2LYWhCYOHXm4sMOJaOhh-oX8D6b4BtF_aPEWjaGAwbXNst5D3DimSmWTaeA4-Wou1EmQm5nrZTjZn67l0rxJ8soUxp_IzsxBED0E4uBvXHoWYrx1YKq9ZnsB8NCufqRUnWtyQqjVP6hp6tG6rOhtkeXEZco3RB4UwsXXDfD53YALiKTZ1FQoUAAuYOMRjMdZNmbqTfZY3SQeiIBvMARQm5Cl9ScUR5RNUtoKfdVPDqqW-HWYvWf0JORHQ8lRGMnGUylBF75Q-F1E1mRQPoxifCi4qQ-tYHe2IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27833" target="_blank">📅 09:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27832">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b267889106.mp4?token=T_s-76WfyOD8WAYwCwbThSe1iPGPMllIZb8f6JjSNsgA-bvNA0aXwJW4cP_aBttrtorAykGHZS7zznXpjN3afB9oOquN8TZ3mYGFEu1qR8d7u7Zf9KhnKBdSfk4fwEU4GtxBNxIAgwm36ow0BJlH_vQn_Y_P5ur3wJuA_by_Ffk4WGJTPkd7VlEMTlQdKXH3qlx6TWgvmOj-lPVJAj11T68WoJya9IlaTydxb-UWeFNzzWo1aSscZWZXHFk8NyV8ht-8NTx_6RLClgUwkzG0_KQIDrCvoXVwaNOz1BBK9_eDnRY_HRz399kBWti2HvaMGy3F-8xR2rydFJXA8xF72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b267889106.mp4?token=T_s-76WfyOD8WAYwCwbThSe1iPGPMllIZb8f6JjSNsgA-bvNA0aXwJW4cP_aBttrtorAykGHZS7zznXpjN3afB9oOquN8TZ3mYGFEu1qR8d7u7Zf9KhnKBdSfk4fwEU4GtxBNxIAgwm36ow0BJlH_vQn_Y_P5ur3wJuA_by_Ffk4WGJTPkd7VlEMTlQdKXH3qlx6TWgvmOj-lPVJAj11T68WoJya9IlaTydxb-UWeFNzzWo1aSscZWZXHFk8NyV8ht-8NTx_6RLClgUwkzG0_KQIDrCvoXVwaNOz1BBK9_eDnRY_HRz399kBWti2HvaMGy3F-8xR2rydFJXA8xF72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
برگاتون‌بریزه؛توبرنامه‌زنده و صبگاهی شبکه سه صداوسیما مجریان‌برنامه به مفاد قرارداد ازدواج رونالدو پرداخته‌اند و میگن رونالدو زرنگی کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27832" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ17O_z1-eCN4u4UoAa2oecQgkBFFE-2RzCa1ApVgB-PYOiUKFaDxGWGscJPc2uEIsrElxDSMKmK5ukQq1K4K52YgK3o2nA5EenawJPceGOapl15HmmRp0HDFKLGmOwtxOldFQOsLWQ_B4dNJ-ysKqSljjMIEglV9FgZwyaC5zLh3vSij9-5e-37HKwyB1MBqnTeRsF9svu24YpC9ZFJsAprYA1pAz7wmhYzFFE1ToCStZZtiBAWrXE1ueDjyyogFQwbGVGt5BqxsWzU8JD7sBzwE_a9NnSZuBOPX087CbOMA3S1iBtA0peEr55oH28nUtJCkaaC_KLjjDb72BzEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27831" target="_blank">📅 09:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPB2WFP6BFI7n5mpFxqS1AHX6v1b2UcRnJcbB7Amkt1JbE4nVlGTnj1ArAdBjkYwUJ1UBhiYdPeUdcF9T3UHNUaL6cPiETvfmaTZe55Td8rdtJsBar3R2zk0WYNq3Bx4qo3EdOIvFpPZJqrBDMF3fhq3x42ZjIsJOCp1sj7wN-ZKOWHF9bDJ1OXLwcZZ8hKz0gJk1qsD6Lu9B_RSmAU9rGDYfL9mOhuBX_JiT3E5Opf9rQseosRGbjtQIgJzUOmvooYgItYkcmYqSUIdmdiyJCWn6RlkzGdYi28bEYEWIRNWczunDd84zTeiHmzlEfdmX-Bt39pefXhPHmIXYdBeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7asnPEipCe0UZhtuTJKM5W38NM6s2wBupVB_qEsLRpiEb5Ln3K_G-Ta0J4qSiDxK_7tYfQ1esud7pjiUkutwBTLAGUT4I8TCARA3dE6oEcIGXQw3_xMzO_CCQZgsXTOKE6qSCdd6uKTdwEH2PMeBsssOWb2Gs_uyPxgVMBH_byafcbXy5_o2PPfHIvaPKhFDtN6hRcDRmshs3bzdjelC9K3l4fmZvaOwpZzDWAxIvq8ipSRYT4Ggk2DzSquXwaIsaDzpOj1TRlw07gR7drxADxIH7HnDWL0bw4wjm4U3GZTaoXrRzD_GEW8VZvOvBcJfcBBfP39pEcOhyEVhbVUxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جالبه‌بدونید با اینکه رونالدو چند روز پیش با جورجینا ازدواج کرد و ده ساله که با اکسش کات کرده ولی هنوز عکساشو با اکسش از پیجش پاک نکرده و گذاشته‌ بمونه! شما تاریخارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/27829" target="_blank">📅 01:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1915fbd475.mp4?token=ZtA_qJnRDzDfh5zZWuvuy4i8nY0mO0rwMnWqCSbb78Gl_aDTmYfO2tPjI5NEoiJIoznkVpMoYpBBDmbLaabBpEMombqanYqGojIuCm7C1O_hdL0_hk--x-hIM9TQvrBZNPYXSoiSHBJQO_QsUjSZyhFzIg2Bt02vXZtgf0N4H1dQcK5719u1MwmG3DIgkcdD3ONUO9iO5XbRpOir4HK2mnrpIWb1ljlXUKz0gnUmcK2VtAlK696Za4rUCsjL3v406fXMsDz_3rHHNxplKsI1wa-x7v1OiJeOXL00Qo-wWTnZFoc6z3zm7_G3PeytHmbBaOH0pzTbGwk7ifye3YlqqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1915fbd475.mp4?token=ZtA_qJnRDzDfh5zZWuvuy4i8nY0mO0rwMnWqCSbb78Gl_aDTmYfO2tPjI5NEoiJIoznkVpMoYpBBDmbLaabBpEMombqanYqGojIuCm7C1O_hdL0_hk--x-hIM9TQvrBZNPYXSoiSHBJQO_QsUjSZyhFzIg2Bt02vXZtgf0N4H1dQcK5719u1MwmG3DIgkcdD3ONUO9iO5XbRpOir4HK2mnrpIWb1ljlXUKz0gnUmcK2VtAlK696Za4rUCsjL3v406fXMsDz_3rHHNxplKsI1wa-x7v1OiJeOXL00Qo-wWTnZFoc6z3zm7_G3PeytHmbBaOH0pzTbGwk7ifye3YlqqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌ اکبری تو مسابقه امشب‌ در عین ناباوری مثل n دفعه قبلی تو راند اول ناک اوت شد و باخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/27827" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQxSEB3_TIzbaFxURoZ4zXmiWe58xHCj64ptq3KjEFPSCsnwtwI5lDgIs6qekSef5GbrXzrLND4XuOsmxUPvakvJtDtZdOjE6PTtUf__NivGTAPWbNrTX9uP5dkhoLFF_agf6j5NAjzJ9aO1KuPvxzQzEUk7S8ApVV-Z2HWVgsdaMNNg6sl7w_HIAEVFhDRowi1OuK3eNd7DxbsSIdhQryr0-1Bd0-4LMSYXThokAcnn4AWLVeGhnCh8vgihLo-CoWpLbEqK_miMOJachtfiuG4PtOuC7lbjkLHXzy41F8E8dgySDK7GlVIre-dL4yxb6PAMMb8SxwVP5IiF_wQ4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌ امروز؛
تقابل تماشایی شاگردان میکل آرتتا و مارسکا در کامیونیتی شیلد انگلستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/27826" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8NZaMDiP8cCsUti_1aGV4xMJrKU5cLVSSsGoEn9Xk00EFamXrkaJUs-rNcuhY9j27veowkZ4ex_uCfvjVPnOJxi9ULTTNvcaeYIMafghjAZBwXNFlJutJYHvu4_qd0w6gAs7gNNrSMkag0mnrKQ3GJDvIwgs4L0dIOwA42FO4ZoX43AnXUm0OAR4D0WHebtss6u9Tq_olhjAQmWBBW0rDlvNjON1rlEc_fMSkdQONW6l53b-765sOUfTJHGwqC5t2-qjoCTakHMppEoZ11Td4HSB_LYSxUcnUsJ6nPU4E_1Rmt1k8Hce7LXniY1E3TY5TDce_QF5_E6vYJXFUto8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
از برد پرسپولیس در گام نخست تا شکست یونایتدی‌ها برابر سرمربی پیشین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/27825" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac9dd137a.mp4?token=UBPLqDMhA9s80u5nYqfz4HX1UkOPzw6sMDLf_4ls168xKsB-T1fcSgfgU-skpfi6ZAdf8q70s8mJodistE44A6oVON4ugQ2fwSOxwUV_rsGUYsZNnD4iLHivTohw-20PpEdqiRZuieJycOp9EC_pvLzQOUXfQfP68ug7N8GZy9wus_Z4R06HFt9Ekit2yc1SdB9jW8hXskYIcNY2xyPO7hjo6PZ_lCHm5FmEKH3vYLNy2eCmzwortLpgQvg8Uq-x8C04u3LLWW5MLYolKBrRDyVNi9H_EhjWDeu6FTeMdULXK-THNiGHs75EG-t9mIb_-oyE2W8tffizHg3gQicRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac9dd137a.mp4?token=UBPLqDMhA9s80u5nYqfz4HX1UkOPzw6sMDLf_4ls168xKsB-T1fcSgfgU-skpfi6ZAdf8q70s8mJodistE44A6oVON4ugQ2fwSOxwUV_rsGUYsZNnD4iLHivTohw-20PpEdqiRZuieJycOp9EC_pvLzQOUXfQfP68ug7N8GZy9wus_Z4R06HFt9Ekit2yc1SdB9jW8hXskYIcNY2xyPO7hjo6PZ_lCHm5FmEKH3vYLNy2eCmzwortLpgQvg8Uq-x8C04u3LLWW5MLYolKBrRDyVNi9H_EhjWDeu6FTeMdULXK-THNiGHs75EG-t9mIb_-oyE2W8tffizHg3gQicRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
برگاتون‌بریزه
؛توبرنامه‌زنده و صبگاهی شبکه سه صداوسیما مجریان‌برنامه به مفاد قرارداد ازدواج رونالدو پرداخته‌اند و میگن رونالدو زرنگی کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/27823" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAOmjpkr7zijzSaUr_bWfCibXj9ouzUqIrISlPzxOZQVykh4GMUkjrFJCy4DjzLnCF57qJIF2OkdvfJfRtLynkgwIXs1lOFr0aEeRu-pHgNNmd692o5Pe5VkTK3XHEJVsl2XEO1fdCr2VKAiAVtZs13rp1ISTX_om2mpgQjBkaNEHTOjOvEB6M-q57rD_iHpdlMoKake04giPbEcfN31E-BWm1D-QlGeo80W0JVUnMc_fKaXR4xWP8G9mUsbYh2gvINoVhcEh8BSokzr08g7HdzlZ7pHgEY6tT3ReNIs4teMRrYOrEWb1YcUTiWwYbHeL5wWX1LWM09X-G3m_Bvo4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
🇵🇹
جرارد رومرو: باشگاه بارسلونا در ساعات گذشته برای فعال کردن بندخریدقطعی ژائو کانسلو با الهلال به توافق نهایی رسیده و مدافع پرتغالی الهلال فصل آینده نیز در جمع شاگردان فلیک خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/persiana_Soccer/27822" target="_blank">📅 00:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6yESxtdVCmXBdDJCMMu7z4tEgbzMAUZLh97-iD1VxDBE0PFXl3MWg4LYSHs35-fssWltbEj3gS8t8T01eTvyTMPsGZuljTy07U7zRAkdaTN-mk05Xq7zGH-2QvYF6l3Fj1m1PoGDNdPFDM17vHEgAP95RJmy5HDOAR-iCk85rtpAOqHCzDOiWEuxfwfbJ91Rqw0DLU9HRmcfse5G4vJofPKbC76ZIQK92b_jYDuQxTC_Szvdy8xfHaauV3n1f9SEg7XiIcpw_HZTGUJ_hyZ6sfjsJ4e3EXRb5VMYBc8oR4xgiTpaKcXh78j6eiNfIjHxI0FGup2TLzjXLCZCOsbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ پیغام جدید محمد قربانی به‌باشگاه‌پرسپولیس بعداز درخشس در دیدار امشب‌مقابل عجمان: پای توافقم با شما هستم. رضایت نامه ام رو بگیرید به تهران خواهم آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/persiana_Soccer/27821" target="_blank">📅 00:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt056hChjiJ4M5Ti2aNrR0hrMaYQAoNJUq88LfjW06p2_VU41HzaHF6CJ6EhtyW5jGx-VGZ2TJouI8kOGoe3oHGAkHSIZSJi7KOnD-BB_HDw_TqvzsBVBBdZES503kPx7_MVTwpwsmk8YSPuBmfYBYbLsp9COcSd3RlE70CYxJlVFs3On7ZiEZRkihUwlADBZPPiaEczc681o5fWLsFpzeAQ6rJph6d6l6BT9XbC4M7IXFa4Cc6htmtH3dLmOElaEfGhfJDdfMs1TqDNPniHUc4mleb_67lh8COrgahFf6pIskC1DLhM6ArpBk-D6I9zEYkhXzoyAC8kELZfKbsgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/persiana_Soccer/27820" target="_blank">📅 00:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQr3XemIm95wtOLApj8s99usGc0Cq2IDq9sxX_YlSbg4Dq0UAHnrmQCkn3_uMsLZ_euCTLrVZxOQihYg52O3F_XDzU9Z3jjLbYHISfd1a8-popZmmb1VqHH7A7BVjtFJsucyRkt_1_kDZU55wrBb2iazMtMaNkNWm6TDaD_MAkVJc61ncZv3mwNZ-LGO0uUy7P1acn-XKyKwOgtDt8q9bRKeZ10M-JWyt8bqJ7uQZfX3_xZt-j5QKUSog3zbJuD8L5KlpC_5Nk9vzDs_aLhFkM-U_lcQMfpksf26-lf3XXEBmsAu_ukLq6izaj_QyMwFyg8w-84izJrFmRFc89Slnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه پاری‌سن ژرمن با انتشار این ویدیو شیک و خفن از فران تورس خرید جدید PSG رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/persiana_Soccer/27819" target="_blank">📅 23:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IipjXley7dSREU3kYoRdYpe-Sw_wKgxi6jKxcd7dZShBjbpFWziwgMhliRa4An4gNUi4xkr4ba723D05jkt44jBk7oZ4WFh9QZSrrMWn2bXtdNLJncHyWTAbsZFJtfotBhz1-JQDqTtMwmtlfuPradKALWBDE6FJ2SGjnylOyUMJrFZZJNrG-xURX4vVs9ES-Y4nwmroTDD92sUd19t4sCPxMM4407z-BJ1arCEsj-opk2XU9DmWqpAsP4AAc3JzOBzGfIs6TUi8rrbLlOQkM3T2zeF3G1KElsFS78d9ezX5OuoYVcASjcGF7a3ejDQIv8I1aaN_fuVuwAizWTgnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/persiana_Soccer/27818" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-3gBX9aR3IyatnNaxYxqs_bD57GAzF9lD71ljMCe4FiY-LKUAyJ51qL50s1NXXa5cERk41fA4Qpk-xRlDX9PaGn1UdCgc9OoEgBX6F4FvQOkzhCqv-KLReIm266-NkjSHBOeKejdIZE5E_CkawfW9uDZsYnA2PR12YPoqXqFFwYdTpS3vA_nDM0k_4MCcRJL73MxxDMUA5w9hLFauW6qIhNA3K6BK1mzDi1QjDkx38t7qWLgCsid2gI-5ysCKKQ1_76d0cqUi2aJk6vIbmWCuD2dam2HJRmFgckBxX46ApvGUBAnMuxv0yDnvBBNytcIXMQdWuH8xJ3D8qDuCZ9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جیف‌بزوس‌بنیانگذارشرکت‌آمازون‌رسما سهامدار ⅓ باشگاه لیورپول شد. پشماتون بریزه که جیف بعد ایلان ماسک و یه‌نفردیگه‌سومین فرد ثروتمند جهانه. دارایی‌های اون چیزی بین 270 تا 290 میلیارد دلار تخمین زده شده. میتونه راحت انگلیس رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/persiana_Soccer/27817" target="_blank">📅 22:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2y57n_jra3_gd0jrwDvPj-tfzVPvJMtf-TvqobT-yz8qAS7vo5z-a1XVONOvaZ8s9NNcKclXMUMMvHRqP039Dxvs5ZgBhTI_RRkAmygbENfQ1W-IdIxHiuCd-eCrwT0LvZgwdEHAU4EZRB6Wc40I98MNhhT1NklewpZnehdYqP4V-ACp1UKBedJm5SwjyQvxPTFDhNxV_KoF0bPjpDJn51wvLiUTLuJB9ku7fI9KkYOyCE6Nj2_Id5c1latd4XPh68IC2N4_rpcjiyF69j8Z_LDFWYyt5-lOiyW87qRIDPvm83Hoip4apQo-cISSXdP213xMy0X4fOo1mXl5EBvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/27816" target="_blank">📅 22:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f616635.mp4?token=e53nL-6BCATW3yjEQUECag5YXtldRnbDCiojNP_9SuGE4ZXEJdTe22eBiM2oNkF7CTbb0XumgAW0NhS46Tv3n3cZMK4--5MjP6W_obXmE_5-3GeKHhT5sbUlpvdJSJp45tAs2KnaSi01MdWWtjoIk4Bl3hWujsD0WSKNOmvr5afUB0WvUlgAqb4fKC661QQvD4X6-jNJK1fXmDsB2-jHQytkFiYTQwm3rOwSeCkpIebtAT7OVDUq1nXT4INhSele64COr5Krrqja6xeCXRYa0a4tBBim-OMwdLcU8f_Xhu6_0kXNtVUYr0J-a35wd3kXvRl0TrzkTSg7EVVkEKzG5kKkTlLiqQrYpUR-vpaUDXc8znjhLZcZgBYxHqSf4G7WUsMUnxrSsQbMxwOh9scSXLy56AzW7ahX01HGdmehpUV_3DhPbOkBpZX_Lf-xVntTi6jFHi4AGfccsMDDY74QalLg1_A9FchxPtTfTlR2kZ4SMdVKNVELHnR1LvpiI-W0Cryv8doKipKVfjGHhbQaVEG-mZNX3zI88oIge3_fMqQp1y5EoZIrnvPt6XUuz1RaB9_oGXhphy2QJVsOMEXOyDucG1jx4n1lKXuwrJHrmP73eUy20FLsLTrjYxJ5hKYS-WBpSG3iSIwRF97CSMOfD-aHUjO3LPZ_I3bghNfjZ-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f616635.mp4?token=e53nL-6BCATW3yjEQUECag5YXtldRnbDCiojNP_9SuGE4ZXEJdTe22eBiM2oNkF7CTbb0XumgAW0NhS46Tv3n3cZMK4--5MjP6W_obXmE_5-3GeKHhT5sbUlpvdJSJp45tAs2KnaSi01MdWWtjoIk4Bl3hWujsD0WSKNOmvr5afUB0WvUlgAqb4fKC661QQvD4X6-jNJK1fXmDsB2-jHQytkFiYTQwm3rOwSeCkpIebtAT7OVDUq1nXT4INhSele64COr5Krrqja6xeCXRYa0a4tBBim-OMwdLcU8f_Xhu6_0kXNtVUYr0J-a35wd3kXvRl0TrzkTSg7EVVkEKzG5kKkTlLiqQrYpUR-vpaUDXc8znjhLZcZgBYxHqSf4G7WUsMUnxrSsQbMxwOh9scSXLy56AzW7ahX01HGdmehpUV_3DhPbOkBpZX_Lf-xVntTi6jFHi4AGfccsMDDY74QalLg1_A9FchxPtTfTlR2kZ4SMdVKNVELHnR1LvpiI-W0Cryv8doKipKVfjGHhbQaVEG-mZNX3zI88oIge3_fMqQp1y5EoZIrnvPt6XUuz1RaB9_oGXhphy2QJVsOMEXOyDucG1jx4n1lKXuwrJHrmP73eUy20FLsLTrjYxJ5hKYS-WBpSG3iSIwRF97CSMOfD-aHUjO3LPZ_I3bghNfjZ-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گوهر خانوم داره تک تک عکساش رو منتشر میکنه. این بازیگر دو رگه عصر امروز مدعی شده بود که رامین رضاییان دنبال رابطه با او بوده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/27815" target="_blank">📅 22:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC2mfezhAfs6LdzH8x547N9-8gwDUVo48UhfUhZ0ys-6EeevYNpjvXOEMcc4zqD4UgXu2u29B8yvwSIXkUrr4-3vDNSr464bHF4oQB7-aRiY1FVJ9FYLFOHkXLBQwl3hLAz67qNVo4xwDSQF5kWj5mKesvcQilq_Z51ZsgHHJt0skDiT_bIhhbNBZ_XO6qznL5tMXoWwm9-IY-JXlecN_df74ofiWtixpWJkIIzi-ppzR7QTkz6vLlSJSx17wm9Q3saceC3fa_m9RIgT3DcW_WByB9ZX_F0QST3IlPkbphl4NXMUhqhUsYM8gbpAtPKdio3dJdcMCPeqQBpIJGwF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت‌های لیگ برتر؛ دیدارهای این هفته 27 و 28 مرداد برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27814" target="_blank">📅 22:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufvdF87McHm5aSR9UJc0v5rutHdTTYhXKJo72mO4-9Cugj2nfFNmQkaGmSQGkodhE3MED9oYJYurUWMAIZUHmexQjWVA8fHu4yfvQiXTO1xAiNuBaSRPEYfxQISk0WXy36C-fQCIb4VdFxrlRGGrzpTAbhTWoL_IkhgGkDxAVscmEnc-0U77GDvcLijZpsz1ZjFO8B_GrDgcC7rf3BOPwSD75UaDruNXnkM8-Q0dmlSKALZr1amlT2T46vGqaFR5NjYQ9j7NktSGWx7DbRCC9TYTjE3kWulwX23Ma2YeFB8-k6zWGLFTDbLJHwUrAm6cie6G8LWdjm-sksAsjCv_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت‌های لیگ برتر؛ دیدارهای این هفته 27 و 28 مرداد برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/27813" target="_blank">📅 21:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsgovLRCkdhNEn6YC7tIZiZt-cHQaa5GRRfkjR8FrbrGdueALsvNi9pZtWHYIrd-5wm4QU-9UC0wIJ8zfgoDgc--3_AbQTr0Gq-OY1XsWKf3Btr1yKdG64DBuVXHF-BnBr6L7YjEM_uU28DhMSL2ss6pClaYFndWZMR9cqtgOBHosvTSlAgBmwj3zcHt5bBYU-_Fci2uuV3Mcdip61B4R25_gAdkAp-C7J4LaRTubhWzCTwy6A6QJhaqyldZnfAIcc6QRYwV6AxygNjlu_g2zLTltXaKf_t4GIQXEMYUcpgUv4V45BNsiIaqjqLeCTe4mlu1ahcuZ1GMVju7xKpJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
#تکمیلی؛ دیشب هم گفتیم ممکنه یه مقداری مبلغ‌رضایت‌نامه محمد قربانی بالابرود اما اینکه گفته میشود باشگاه‌الوحده‌گفته این بازیکن رو نمیفروشیم صحت نداره چون با جانشینش به توافق رسیده اند. مدیر برنامه قربانی هم امروز گفته 800 تا رو سریع واریز کنید تا رضایت…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/27812" target="_blank">📅 21:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c41r3g8x0fRdTUmVwdnUossDPIo_eYuHQaP-BczU76IOK-OiEuwryIhX1qr5hFv0fXSs7cjFv-K07VYXfJ96BYPYWzwVmiEMgMbRlGy-ONaDy-Zb4TjtbEo8rp1o6QqFkclLYjcAOCp5yhp4uk4wIIYQoxt1k16YRT5xllkMdQCVtw2v16ig3zs6iv-jyGNlwvU97ZrBN0aDKJ_YuEQOa25UMT-7jT2YhBx5lwEz7D6_bRUWXXA-m2PkJ8l0zv2WH-hO8lEwhSGiXyrqftduSxCkA_RBJiLPQ7W9F4JOwyckt3AZ3YO93zxZ1LEjWk_ASXNw1jTCvSKwFE0JHX17Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27811" target="_blank">📅 21:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0mW4IOFq1BdNpYUlH7qjyfVyhJi8cVmmpupP0elnDC_f6ppChA1SblavKIiiyAGDz4qaw2MpbGg83_1XNN9_YdGHmVp-vlwAvEXMdueR0Proba8mA1k4KOm0y6ZnmCBseJ6dPUkHzR968rqIGF9-j7sz7UYyW5Sady8BY2De4aALAzzmQv2Um7ZEnsmZ9jI6out8Fzc7vEa9sH_4ahEjL6y_u37GeMFCHT3Zaou_Y6uGjFYFkOE0JOivpnx6FDL-mbno5cuXtRc1mg1cGLRhqiTi3oVxAcp7Um3cQX1WFhnTtfUEx7uwRMCGUJNwRkgZUPvLoCpvdQSEnINmClWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به شمس‌آذر توسط محمد عمری در دقیقه 15 روی توپ گیری خودِ بازیکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27810" target="_blank">📅 21:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=RSFKtWrSmfJ05WxmoZl9Oqb8V3zUhSkUwpPUubbMkRXA0_XomRLoXcDfSlOOGpahq3_8XrPQyXQSHIEvqUBEZ7aauCnc2Td7yegxIjtQAb1TpopeoVv_Q8FoMhQWf6NlrT-Uz7vXzCJLYcdXoiqv9QJBMDyoAG69LrTzMgBo107xBnzVH2O6ebt2iAx4JDbK-We6hhDqtv069s5mW1TGdUoD17On7KD0sUx3z1n5YukHmnLMaeOKAqjXYdEDS7dqaWExByGqWQ4fitdy1DyMzdc0bHVwv15tTpgy-oJG-qkA9TQJDEqDHgNAdNMlzqiWnVCW9PhmO7PtFtcI_e1Taw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=RSFKtWrSmfJ05WxmoZl9Oqb8V3zUhSkUwpPUubbMkRXA0_XomRLoXcDfSlOOGpahq3_8XrPQyXQSHIEvqUBEZ7aauCnc2Td7yegxIjtQAb1TpopeoVv_Q8FoMhQWf6NlrT-Uz7vXzCJLYcdXoiqv9QJBMDyoAG69LrTzMgBo107xBnzVH2O6ebt2iAx4JDbK-We6hhDqtv069s5mW1TGdUoD17On7KD0sUx3z1n5YukHmnLMaeOKAqjXYdEDS7dqaWExByGqWQ4fitdy1DyMzdc0bHVwv15tTpgy-oJG-qkA9TQJDEqDHgNAdNMlzqiWnVCW9PhmO7PtFtcI_e1Taw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27809" target="_blank">📅 21:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXyZvQrolTg36OXFKvohZqO_djHwanXbfeMB_GCrBSwQELWz87iH1AKREKmEjvaJKK_KLwBtkKt5MlkjHxnVV3VuET28yiPt-w2O7HLhUi_McUshCvyYDWcZ3BzVacEExVjx4PTBl_pYvbmc7dU0KbvoZ--jyS9Xt931BKp4WUoh-QEodBbE9FHC_1XYHILd8qZLAfa4RDeXTAl0F0QTkK6fStZo7nc4ROrg0NLuRO_cByFErDUZjtxTYbXS3NMGQGuC1pz6DlnNONgUvbf07LsApnTHHHUJ9y02iuR8yMGGdWFdg8DW5niMhTVHv3rbBTCl-qLHPG7U65tos6Dv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27808" target="_blank">📅 20:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📹
خلاصه‌دیداردوستانه جذب و پرگل امروز دو تیم آث میلان
🆚
منچستریونایتد؛این‌اولین پیروزی میلانِ مدل روبن آموریم در مسابقات پیش فصل بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/27807" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=jMW2LMrDK1i4LYLZMTW_k4-kN4uTZyUmKadZDvmKq0CuXqbtldKnh1N-kxWkNinQyfYDGlt9pTuYATWVEkYLveqhkOYqhybxNhh-xE7pLUgZk0UWQX1m_whE1LnEHmQtXYBoaTVv2iV-a_X8uItULjoaFlUpnnnCVYs3uMfF5fAKcAoHxQqn19BBJJh6sxotq5WlJ-bvsdMW4vZnG0Gzh7wo6X7j5oeOfLt541feSJ2HyNiRq1nolDhnqZIabCzUmw9W5WZ9OAGSzWYAOhcTtKZvV7w-6bBZXnrUmM31pMolT-Q7GLHEQE8nYoHVqKCqW2Hm8TheKgv0OYzcsGe0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=jMW2LMrDK1i4LYLZMTW_k4-kN4uTZyUmKadZDvmKq0CuXqbtldKnh1N-kxWkNinQyfYDGlt9pTuYATWVEkYLveqhkOYqhybxNhh-xE7pLUgZk0UWQX1m_whE1LnEHmQtXYBoaTVv2iV-a_X8uItULjoaFlUpnnnCVYs3uMfF5fAKcAoHxQqn19BBJJh6sxotq5WlJ-bvsdMW4vZnG0Gzh7wo6X7j5oeOfLt541feSJ2HyNiRq1nolDhnqZIabCzUmw9W5WZ9OAGSzWYAOhcTtKZvV7w-6bBZXnrUmM31pMolT-Q7GLHEQE8nYoHVqKCqW2Hm8TheKgv0OYzcsGe0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
با حاضر نشدن بازیکنان مس رفسنجان در بازی امروز مقابل صنعت‌نفت درپلی‌آف‌لیگ‌برتر؛ بازی سه - هیچ به سودصنعت‌نفت شد و تیم محبوب آبادان بار دیگر به رقابت‌های لیگ برتر خلیج فارس صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27806" target="_blank">📅 20:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYtx3M3FdGwU8t4DEoUIbhErMtswklsq0ACVxFmRBHZhAfkeNBu_DTh7nJKkydSkdByl5v5zibj77RfnXj8erszvBMG35qK8hwpGb6z9P-rdhWwb06q_dil2nmFYg8e1sKSeYL6Sdf43oiG32icY5_nJBym0LdbDux8xFRWcgkPg0Z9KTz0bF-oPgzKUO2gjSAjDaVx4CFf60la4NQkK6DolsAsPyPhNT1BMzGIDNpMt8NdpZCLfa1gaaRTB8tS5vLc5zQdOrxSjyNt_SWwqhNkrKgeuP4KWnH7PLgOHTN-4WeNnBObqgv3G3uyfF1SX4YxShvTeczAKXXFY2_Y7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید خبر پرشیانا درباره‌محمدجواد حسین نژاد توسط‌مدیرعامل‌تیم‌پرسپولیس: مذاکره کردیم. رقمی خیلی‌بالاتر دومیلیون‌دلار به ما گفتند اما چیزی که برامون مهم بود این بود که خودِ حسین نژاد هیچ علاقه‌‌ای به این‌انتقال نداشت و بما پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27805" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kumi0SDmNPRgjDYTNEX2ErIF9F8i1qEpuLepIOEwV6lpX0pgFx_ZvmSE2qFFQQMy13TMvr6u7kTpO9UwPsWmyv8seOqMb01s1WqDzHvtCS4tnCkyj--sMVfC-VyVe7ulOyVvaE_3PdMA-hU48px-vFP3_jEoM5L3OHmoKkzbEskPAa42PcCtFt5b6C2PUfslL1IC5h1IcxMg3UbkyXeqfvAPF0_YXYghjHciVuuGyCtMD-myIxQuY-bZd1rBKl1JcO9MzeWJdmeSzsfdfVNLdeLEP7IUGVXY5Rk27mKME3LIV_g1vHjVWfRlfXicSF7FjLfL60NavFwOSV-ZFUgk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛
تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27804" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=s88rIeMyLN-GL5MtsL_9MFFQH93b47MqcJHysTshkEOXC4xim3CAbgQY0-9gi2kzzBsfgxtWT2MsHmlL8jG61hNnLje3PYzF0PDBanwTLfDijpHqnzHlqTapCd0w1myEHq7We9K7fPcYegpxhV1ZJHcu8ytAeDEOU1aGtvlk-8Cqy1NHpkNaZPDVDf4Lx0DMDgB6xC-028e8OvlfEmjBALbKcR2W9g_LaR0gGUE3Ypb2TZhyAhxFf_p1C3Blx2RotQC41jkYX-w-K9Sfr4pyLVAUcayDyFxG7zJLVKYalFoko-uXZTM_-ARHGFyRaVp3PlI4wfgyGrEeJzbbl4posQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=s88rIeMyLN-GL5MtsL_9MFFQH93b47MqcJHysTshkEOXC4xim3CAbgQY0-9gi2kzzBsfgxtWT2MsHmlL8jG61hNnLje3PYzF0PDBanwTLfDijpHqnzHlqTapCd0w1myEHq7We9K7fPcYegpxhV1ZJHcu8ytAeDEOU1aGtvlk-8Cqy1NHpkNaZPDVDf4Lx0DMDgB6xC-028e8OvlfEmjBALbKcR2W9g_LaR0gGUE3Ypb2TZhyAhxFf_p1C3Blx2RotQC41jkYX-w-K9Sfr4pyLVAUcayDyFxG7zJLVKYalFoko-uXZTM_-ARHGFyRaVp3PlI4wfgyGrEeJzbbl4posQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27802" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=cAd-8kwIZvye3_zCx3gMTogaxPTa6p_8S0bXwxRuU4wb5cQhLCaJMW3uORroLeji8HUAP_U32Dc80gbdwkHkDtFWhcw8MdKw_tiKybREoyRSRhdX_FpevrsW6_x0WNfABbc-Mog3jMUgUR2C6TyYBdAm6UawWQCppYU0uWlE20AHE8FSL46tUDeZks12Zp4ahjyZAeYyWM5fN2irwVWbMtacfJrfHTRlSeQKPWoySA2-xZFsozohj4vzCvH4bIpYbpznXvZqEP5UgRgB3AYQVwx69H2V93b3qIUtjdrOxW-go_dF8uJvTpF9cIHN8pW5ekoZ8xZ_IxuEwrjCXqw4SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=cAd-8kwIZvye3_zCx3gMTogaxPTa6p_8S0bXwxRuU4wb5cQhLCaJMW3uORroLeji8HUAP_U32Dc80gbdwkHkDtFWhcw8MdKw_tiKybREoyRSRhdX_FpevrsW6_x0WNfABbc-Mog3jMUgUR2C6TyYBdAm6UawWQCppYU0uWlE20AHE8FSL46tUDeZks12Zp4ahjyZAeYyWM5fN2irwVWbMtacfJrfHTRlSeQKPWoySA2-xZFsozohj4vzCvH4bIpYbpznXvZqEP5UgRgB3AYQVwx69H2V93b3qIUtjdrOxW-go_dF8uJvTpF9cIHN8pW5ekoZ8xZ_IxuEwrjCXqw4SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27801" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=E9M-G1CzpNS2ggyyhj7kL6FNoOg0ZxnrwCKzuxThToInoQ3i0iVStrRniilV2Y8FcFn3W8v-MQEqiFSC3UEbjnj85sRIYrmXNOH74ZiRDZyh_3OB88sUEplnDV8IAp5YZflZ3_7nJopYBuC7Tyqth0ffvF4bk4JJVOT0TSUkurY8ss40OVc_aAXqUFB4_vgBgwczR7gtmvRB-mzto68kdAeSjYHmNHmPHYWrsS5QwCqsqYhO2ujlJrOWvDy7VlAiG3zap3RI520rl-DcdE9a7JK1moVLAEYfNeSY-YNdOapOgQt40z66pvAKQUegUezcP66ssy--19CkFk59zLW1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=E9M-G1CzpNS2ggyyhj7kL6FNoOg0ZxnrwCKzuxThToInoQ3i0iVStrRniilV2Y8FcFn3W8v-MQEqiFSC3UEbjnj85sRIYrmXNOH74ZiRDZyh_3OB88sUEplnDV8IAp5YZflZ3_7nJopYBuC7Tyqth0ffvF4bk4JJVOT0TSUkurY8ss40OVc_aAXqUFB4_vgBgwczR7gtmvRB-mzto68kdAeSjYHmNHmPHYWrsS5QwCqsqYhO2ujlJrOWvDy7VlAiG3zap3RI520rl-DcdE9a7JK1moVLAEYfNeSY-YNdOapOgQt40z66pvAKQUegUezcP66ssy--19CkFk59zLW1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27800" target="_blank">📅 19:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=OL6KUJ0Cffi_TFEP_W29vewzqn-SZZoZR9tsBzMd5CzTgfhYbrvSQg6k2OPiGmLmBmo1oziN_eu5SXxYs4QZjCTqbVzb78npLQrsmOHLKFr0rX-oWXfu1K9qLJZCNEY-e6V7mSIHEq6xYjS8xwhCdO9eLYnaancQCnYIC5LQIAcCgUtTVfgmOKSEw0KoFEyfrwXeRSmOp1l34ITB4LVQX-y5xVwkiFQfujI4KpK6XgQC3FHS-HpYJ54y7y0LlOldPclxPpP0kXB5N_Q3JZJq36Mh0HGPx1PFMPfQ1ggTlSGxycrQbX4PclrwhYKYsDSC6uDCiQG-jAlBoAN0kj5ESIxUaMQB4YIeDWsC_GQHhzJxIZo46Fb2GaTkdkLMLjCc1aatWabdL7ynAh7ekXnKdAsi_U0zi0Phm0ocxpalpdVwF91mgOgqc55WGK6W90vw0YQkf938LMqpdbAk_OQjbwaj6t5IEjA_RmU_iTQLR3m3oJe-8yJOcE2dlERhpWX93WpJDXZthjtu0RKSALCmMddvZa-zQrmGuEXncbMy1ZgZzqlvT3_EjuQI8dDMOFZPntU4uQzgPopOvPd7CmCHI5rdJJYz21dItGbwZLMa68PO6EyMGomlxkIu1F9kgXrU9ru2pRwZe1OEJuLSgd5UqvcXalQSVQc312MBNOP7JWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=OL6KUJ0Cffi_TFEP_W29vewzqn-SZZoZR9tsBzMd5CzTgfhYbrvSQg6k2OPiGmLmBmo1oziN_eu5SXxYs4QZjCTqbVzb78npLQrsmOHLKFr0rX-oWXfu1K9qLJZCNEY-e6V7mSIHEq6xYjS8xwhCdO9eLYnaancQCnYIC5LQIAcCgUtTVfgmOKSEw0KoFEyfrwXeRSmOp1l34ITB4LVQX-y5xVwkiFQfujI4KpK6XgQC3FHS-HpYJ54y7y0LlOldPclxPpP0kXB5N_Q3JZJq36Mh0HGPx1PFMPfQ1ggTlSGxycrQbX4PclrwhYKYsDSC6uDCiQG-jAlBoAN0kj5ESIxUaMQB4YIeDWsC_GQHhzJxIZo46Fb2GaTkdkLMLjCc1aatWabdL7ynAh7ekXnKdAsi_U0zi0Phm0ocxpalpdVwF91mgOgqc55WGK6W90vw0YQkf938LMqpdbAk_OQjbwaj6t5IEjA_RmU_iTQLR3m3oJe-8yJOcE2dlERhpWX93WpJDXZthjtu0RKSALCmMddvZa-zQrmGuEXncbMy1ZgZzqlvT3_EjuQI8dDMOFZPntU4uQzgPopOvPd7CmCHI5rdJJYz21dItGbwZLMa68PO6EyMGomlxkIu1F9kgXrU9ru2pRwZe1OEJuLSgd5UqvcXalQSVQc312MBNOP7JWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27799" target="_blank">📅 19:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDgygSfjahLuKtiuYmnjfTLpYIxh_ZxnxzrggYOg1o7URoebtJ2B5qdleTVRroma9f5XieE-XHPTt7_wSCmt6hdy0Hm74DiNv7k26WNHg1cnNQqJ5kH5hmEa0lRV2ELo9LeZSz12owcra-cSI_mAtltksle7cENFddhGYGSDTmRhGtRcL8j0VT15t5F1seKQGcxrOwKl23TCkA2kWyOviZa8JtHduWYJUSUMDTT4qCgDh77fWYHYRq9dzXCht31Mhi8gw_GhgZyrviGI14ds0GaRVXoAweprf--sbcJmk_foDSWWo_eGgSeHBT7fIEcTmFT62-EdGcsVcBuUliTA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب با شمس آذر؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27798" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYXHsqXViQ2s8t_r5rQlO8GnZrLHlzyNmFwK1GJbBOZy2251peAYI-qWbRmwmqYTxiUM0034_MpWmup1O0y6fpTWR9VumAl9WeM7u1LoeMRW5HuqcVhWbiih7km_k_fIRD7N9FkFbVd29yHPIYxHsHyOaGGIH3GsuE8BvWJ31gXMNH1pKSgpnTW0NPPMsdEaWywm8hnYCmHvyuqUZucSwFMNr88dl5Cfx4U9WhyxMybzmy8K3fiTf2eMlf27-LZjIHApWP68shhtHa-wmU2uidfWcsM2hS5ouxTPEgO1FMiCFlK0ELM0X4ilWjEznnCKIvt_HGaYBkChpUXLVK2hKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27797" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSFUTTYj0nbKZN9IsldrCyIfgFsw37YjnM2Q-K3gpebeFVkX_L-48u-v-uMDAWChYHDLsJrX-ZpOSekNOloZj9UWpP71hNuJO-Lv9zfU3IfC2tJr0-RJTQKIsPD6o3Apa5PgrbyaBiyBnoPGQFfzA0fVMUKQYuun73XrU5nqXPUWb5uxJrFD171eFHbWp18cyVLfGoX9AQrWcQtYWxUMkfa9q6TYfq7omf7FrkuONlsA0AH4RH5AJ5P27jNt1gZLG6QwjGT8iS7rat7eaPzrQLHEyDNdjSbOwNIF2-1gAOggjwrFqBzGQKw80ooJhwZ9TKvmniBjaNMeNAfQZc3Pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27796" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2FyTFhHM4pT7Gkr0L3ea2V6_eRAGdeyXtcqRhvEagSWGJFuPhR19A5-ELLZeVVV0kCwZEioGHM6WmSdoudalNFjGG-g4NlWlr0_6FHm8yURV43Df7z-g5ommgO8UfarsHcbGt1y3H6kijNNt_r3AjDPuZzVGdoGzi0LsUPLiQkUAc0v_sjqpKM7AELXqlE1n-kHgaZfdLf0ZiZYS3KdrH5xNM6U_dpsJZhxnPV13veMUATBjN-O0CsDwMa2i6KHpjMmAr9RIm_mQcwgPK63Y6R56fzvC2kW5lsSwur18F77MiT-f-_abnDeGCIRLxRb6CRfoRDYHkA_HHVywxPFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛مدیربرنامه‌های‌محمدقربانی دقایقی قبل به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت نامه قربانی رو بگیرد. منتها این پول باید همین امروز واریز شود تا کار انتقال سخت نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27795" target="_blank">📅 17:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeQLAsVuFeZMxQfnO6xQr9N84In705n_36Z2GvcIo5pcCtmATpI-tjwAE0HuQUneEWrjG7pL_fmygzkqCDAzaZe3MOJyks2oz6eP-g8sCBqvv13qrTTfsdDdLAU5fyhkmvrO4bgVm62fyYmuSBvr4avcNkLXOGwkoBrb_8fHZrY-_dME3p_j7KbrZsHgkuHe5TQ7jTMVI2npbGxXWZR4w4lJrjoLEx7gaIQWFyq-CoT5QN2KyXJAXZmICKSWwBWQjDu3HjUYmseqfcQuF9xsGiNHRjRrIsAStDTnyEpQM54-NE1YgDqd8PAVvMdUux2yIXpwfSmgH-l_4PZysQaoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBl8fCZvvXfHMHeDJNhu5W7_vZLUUhl9DmTebXWv91he7vnOfoCODq9-cwjn4JJiS2rlxS6XurHfuUarGfCRX-GJ0Zyh239GAZeOXONpZQpj7hA0W15eWKaXSyExjExoQxYqcGNcsmPnAHgwpEKVMdW6nHZ8E3cmmY0A4vX6QbYpHlSYO3f2orXv_K5svmcPolxDoAYnlBUBSN6GfDHVzB1swiiX2boBQ_Qv-FQ99_bww-REANtTWOcTLpM9s62Jrsv8YqnEGqFvVx2XiL6hi7GykWbl2a7gLHKlbZ73Ps3m4HsNXRPrfjdZ-XhMjghfXv9Vg6dkOHs9YynJaFxWCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویدیویی از گوهر خانوم که رامین رضاییان بزرگ قصد داشتهه تو امریکا ترتیبش رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27793" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=UML4uwfJ868plKgPtFxmf2MPX-26RcirEbc1gPZ0gkjbPieF_OCuxJRABZaLpRLnvDHdyVx7vsAW8IxaZwseDexRSxO2Fy4_-uFsEv4IoGp8fPmj9uNnYamf4eKM8qUiu-_4MlW42zMk3QR4-7EYPnZok2pPCKroJQN8aQgIkZuzBcSjtlKi2d08oImk2W3Yc1NJDPXVkg4vGO4TNRWUUdK-A_8Dbm6LZ2Bmd9YktX2m6lF_dvZfXOw0haxplwF-rQPeDv6D0Ol-4PiuoyxduQJH46B2IghCqv0MR0lxNwkqtEyfS5uUDwgLBFHzPiw_6nI_h0X4vtJm5nByJBzDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=UML4uwfJ868plKgPtFxmf2MPX-26RcirEbc1gPZ0gkjbPieF_OCuxJRABZaLpRLnvDHdyVx7vsAW8IxaZwseDexRSxO2Fy4_-uFsEv4IoGp8fPmj9uNnYamf4eKM8qUiu-_4MlW42zMk3QR4-7EYPnZok2pPCKroJQN8aQgIkZuzBcSjtlKi2d08oImk2W3Yc1NJDPXVkg4vGO4TNRWUUdK-A_8Dbm6LZ2Bmd9YktX2m6lF_dvZfXOw0haxplwF-rQPeDv6D0Ol-4PiuoyxduQJH46B2IghCqv0MR0lxNwkqtEyfS5uUDwgLBFHzPiw_6nI_h0X4vtJm5nByJBzDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27792" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAcQpz9RkV2ib0qTA7EBv-fPRRPNtsoS1AnxWHrVM6oXDqiDmRQSN7hyDBKht_PQ4-5g5Cq-8KK7L1gPZwOf500msXaquhd7acm-mMtb0WaszvK0UooXMikrRTsbcjnzXTVqXcR8VRSi9ZJfGIBaAl6a0Y7fUur65PK2HExn9J9SdWS_dI9_vO5AU9tKBI3U8W76BVk1tLJK208-Otltrodcq2frfzbVkX1qQWhRAENmqUZnXdirHbUwD0fIoSwX34BC0x1O62BdICiYBKW9N3xPVtoXCiP_1oYMaO-ebi3p81IrT6nYkNEc8u5i55Q8TqXyIrm6j3teDaMhZbuAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار ستاره برزیلی:
من آدم رقابت‌طلبی هستم. همیشه دلم‌میخواد برنده‌بشم و تمام توانم رو میذارم. گل میزنم، پاس گل میدم، به تیم کمک میکنم، بحث میکنم، در نهایت اگه هیچکدوم نشد فحش میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27791" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=GMNPLKvhi008oiafeMqIIoecXw4SWMWOmg9-kex-u-UXCf7VprmX4xes9EvWthavt9tvzLGyRLECt-G8hbLs9tWeNmcBZ51pAGFxG8lYNA8Czo3YKwHX5ZzoGwk6o3fS6bw_3My0wELHvn2SEJmFJsUv1vrsXrHaG9A3KHQYMLUnhaTmYdsiEnh4gJbF_-PHNMqIFF67DGDzyNT67PTrOjHcNXE1xoL5RWoMNh9Itb1kKjb870tvKetD0JxkmErQAaYI63HNAizstfr2X7-IJowJzaf2FH7f4TGlydBTnveEpf0-e0WD0uVUqT8AIm6IVrbyvObeCusjTN7KlsL5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=GMNPLKvhi008oiafeMqIIoecXw4SWMWOmg9-kex-u-UXCf7VprmX4xes9EvWthavt9tvzLGyRLECt-G8hbLs9tWeNmcBZ51pAGFxG8lYNA8Czo3YKwHX5ZzoGwk6o3fS6bw_3My0wELHvn2SEJmFJsUv1vrsXrHaG9A3KHQYMLUnhaTmYdsiEnh4gJbF_-PHNMqIFF67DGDzyNT67PTrOjHcNXE1xoL5RWoMNh9Itb1kKjb870tvKetD0JxkmErQAaYI63HNAizstfr2X7-IJowJzaf2FH7f4TGlydBTnveEpf0-e0WD0uVUqT8AIm6IVrbyvObeCusjTN7KlsL5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27789" target="_blank">📅 17:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27788" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGqagMK338NVB333WqbUqq1R4iRpiSLKX_YCZXqSkmoz9qlM9TFb7_jDCTO1qn2Y1snNhd8tb50pd6CbHkCYl25y3wTR5GME4H9hN_NC97Xudof0neNQLojfE2ha6-kBEwDPKm9wEtsx1DdYrQTyoVxhrEFyJETg3RmrWuzfAgHl3sLuo6h0zT3rUhM-s4sBqcls7MZCi-RbomQBkn7dD3D8Oqz2Q34MKICzEaCHdcu8BNAWXFR1Q1iw5BMqlp7WFH564D6EIXehwawlx2JE47DqbhDV8jCBF_m7d4dYvj6CEnYo2ASvGvKS9nBvtOab8ctzUjW65ZD8EUoRilHhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان بزرگ تو آنتن زنده گفت تو امریکا حاضره بوده که حتی برای مردم ایران جونش رو هم بده اما گویا ما بین بازی‌ها بفکر عشق و حال خودش بوده و خواسته همونجا ترتیب این بازیگره رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27787" target="_blank">📅 16:43 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
