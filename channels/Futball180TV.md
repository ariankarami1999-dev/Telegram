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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 698K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-96431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3cdee6b.mp4?token=bY1H6bF3M4-FSbbD18RN9pACcZv_NaK8nY4I3uucTYkL7VGQcucG60SvJkQ9n-13xsHsOM5XrjWWJ0hYNPzzXBRd4X4GTQNDy02ZojC8sz8W8sIw5hkOmLAc3_M1W_ghIF7nv0X5OLER3m2QgkYD-7jMVuJ91o9Th22vg3mJx9UBFKAy6lWmnTD-hTj9prWWRYjOYD9zprDia3jVRZvNBXcKrwurabB91MTSCbfdpmaDEmK_kP4D62pBkfyByJwxHb2JdfCRqimO7C4geTnYSckTkT8dwpAT4fMRCp0wdFnF1Hye76dOzVydWDOKIvhrZWER0bYo-BrgpIA3FojDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3cdee6b.mp4?token=bY1H6bF3M4-FSbbD18RN9pACcZv_NaK8nY4I3uucTYkL7VGQcucG60SvJkQ9n-13xsHsOM5XrjWWJ0hYNPzzXBRd4X4GTQNDy02ZojC8sz8W8sIw5hkOmLAc3_M1W_ghIF7nv0X5OLER3m2QgkYD-7jMVuJ91o9Th22vg3mJx9UBFKAy6lWmnTD-hTj9prWWRYjOYD9zprDia3jVRZvNBXcKrwurabB91MTSCbfdpmaDEmK_kP4D62pBkfyByJwxHb2JdfCRqimO7C4geTnYSckTkT8dwpAT4fMRCp0wdFnF1Hye76dOzVydWDOKIvhrZWER0bYo-BrgpIA3FojDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شادی مردم از گل مردود شجاع خلیل‌زاده در یکی از کافه‌های تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/Futball180TV/96431" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96429">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWmMcUkIMDsfCAGs011Xq1PX0JRUQJ61XIEx665tZgnUAXak69zpQw1kx8QHZETmPldYgWVhUiqdi0IM7QvrUGcGTFhRD2egftYUdhmFzPYMfOHyO5zt7PkWD35ANGXIUdhssvBbcf9xBR0DMa7HFf_4GIJ1Osngb_36ewTLBFrao9T7fod-3Cv18d7V379YGgctmslsaR0m689xgE226yykVGyEj_-FbyqfL2RSZT3RMmon_dS4I2du7BWDqi1UhWwy-IL067WzEqaHugJG4oParmdG7NSRsdoMP7o6fzHk9BUI-sBADCqmg5TS0xxb0zV9P8sYhaxXPzLekym1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0nu1cVF7Kqd2veXnKUK938JhLb89N_yuK__onUBprFMHa-Kct1ilNqab_6GDtw1PRhoD72tX7Ue4kHZ4gZvvgMIqnBtabH1uRFRH7kuX5sdDbhABc2LELR20o2pSnkPj3KYcnznVkONZJOWWVTlI9aKuM6Rf656QnPrmm75Q6kt_t7LbNJu1xpQUfU3g0pc9XrFxxvYq-ioZR_oUB8OupzG1SWQWZCXuhHJDNLdrLF3ZWYIfl02B-qvtiY7BUYmoNjc0LHNNv4HGHMCwtil6RVeKv_cTo0Db4KHwBgEBT4YsWxanIbrAzPLJdgBsEwFq5Gfpc8Jkf0viUs3PBW6gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇭🇷
🇬🇭
ترکیب کرواسی و غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/96429" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96428">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knpJ7i9Cw4vzqW7bF70nQzm7SsTrcSFQLxaa_E3JJod4xWd0_w_vh65xIu6LKmLRKYvoc8chiIrrl6SGhUKpldU32mIhQAmJQSd9iv_tWb7dMGq50KIifxurJm9tPwMZHVi5078z3gCjXoLtVwkozJPRvtcM9oyqmagGKziRSlMeK-UmJknAKPn4GoRVawv1jI2oaDUIrDlTPMpLl8m7Yhd5tnNZG8xCHWzIufgbgV9y9nQxSVZZeR-tr5p7CBshElsU8e_QmKh7c402XuxDGloeXCHZOqHgCvUDdWyhs3rKNvfvdDfzkr5GOxdFHGixCkqamjKnrqUhljU7pUBMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس مقابل پاناما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/96428" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96427">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0191009ab.mp4?token=llF8udgq78BWIQkTxmgXioxj2icXtLWw8IPSfPKKMAtN9jFY0q5OSOD1fUl9pJvdvi1MU_OIEJ7kLWFX7rOKJuMq7fEHKWEmiGRCCvHJN71tgsXCF1qmOmQOMxo6-ILl1tRszQAbVZOVMw4n2B9-5dUONoL2RKKKaJkMEEYhtyOYpFRD6yI99ODwFOxDu3C_faxVgQgjBoRHapvGRp52jkF1RbX1AR-dzn9G_CVUqgaBbT7yauAHgp2k5vF1X3d24OeftxOoDiMgVvSQ_BhIuYmp21hh9MiBGC9bj-IWSJuJlmgI5m4TBsNh8i60WcXeU_mpoVH5uoEy-ArLsLQn4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0191009ab.mp4?token=llF8udgq78BWIQkTxmgXioxj2icXtLWw8IPSfPKKMAtN9jFY0q5OSOD1fUl9pJvdvi1MU_OIEJ7kLWFX7rOKJuMq7fEHKWEmiGRCCvHJN71tgsXCF1qmOmQOMxo6-ILl1tRszQAbVZOVMw4n2B9-5dUONoL2RKKKaJkMEEYhtyOYpFRD6yI99ODwFOxDu3C_faxVgQgjBoRHapvGRp52jkF1RbX1AR-dzn9G_CVUqgaBbT7yauAHgp2k5vF1X3d24OeftxOoDiMgVvSQ_BhIuYmp21hh9MiBGC9bj-IWSJuJlmgI5m4TBsNh8i60WcXeU_mpoVH5uoEy-ArLsLQn4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
وضعیت صبح‌امروز مردم در مترو تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/96427" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8xcwry5TqHwkqxBqAo77ZK8EA_0KeKK_ynME5iXCmbGQZaqDB6I30z-jfMeHy08Y_2dMQFq4nI1UanFy6qp0ZtGSLVb1u885AdU2XHaaoPoMfexGCxAO23eBoeRjxwiAak1qRn6f4dIpJYVt6-7QtprnnkYlBdusyKQ91NeQTGLCY_IYpf-nq_pX6xpiK9E8OeqNzqUn9ja1J-UtdTVTmUQTwXhsgY1dEYKdUd3G3jVFtxLgAMDHph5LPqAqMqNywmmihQHJxS-ETyx048dtYY1Mo5eEQHHwGBGDwbRd_2A_0fKogRnXQqSsh9Dp5Kx5yfH2IU1pYbUrO5EzfMUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فدراسیون فوتبال اروگوئه به خاطر نتایج ضعیف تیمشون پرواز اختصاصی این تیم رو کنسل کرد و بازیکنا با پرواز عادی بر میگردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/96426" target="_blank">📅 23:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6750ccd1e2.mp4?token=cbKoP3oCu7RPmAhBJhagVJS7X3WvF8qAq8IgsS9H2TTSsU_s2F6WXfotUJE0ktrndqzwzi15S5PRzCk4JBoy0HQ1m0hRCGbYmNWFjXumJPf5hwfqzFPTiZrfTOKUPkmrpZy0JOirs2MaNsci-LrzsY1UlfTclQGT3bCzL2y-Rw63ZLCv_qLHzBZgsclZICCjZUTQh9hLJBGYXnCW4ljRoULAMupbhQEsW3Mq3eDUlgYWNfbaoWLdGpUnnmPnxn3TCCwL2_WERGwNCiQQoljykeImSt8yQVCUCz1E9FYQotfnhDyHDRORPME65rFLGhIzb4FETfPR_QKpxAFe_BnGNlleqC5Hav3T-ThOG9odoB_Aul_Hr_TB4jFDVs4zSL5buPNeEHInc8KMTIKymPAWBVAUlDNinIYBkFiNbYx_H7tZiktQBYpYSI9uUOJIfSMxdKQz5LoPrXOhsXcueedI90Jj2Pi-S-D8v9I-cXXBs_b93usSQSswjUwNrI7IpzRqHdjDC5i7c-qnz3XlssJ2Hs4slN6IiuLUyhDsMuY8QmZCCVmJgPCE_-foyMSrTEi6PM2_LLv5UQNuk5_up3NfQYqccK2furBhYFmrWb6tS4-M5dr_MOUDoFbNbjIkeZ7s_Xg7addZ9pNuzj8HFN-FFnCuQemlDMRlX1cEbpBBs6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6750ccd1e2.mp4?token=cbKoP3oCu7RPmAhBJhagVJS7X3WvF8qAq8IgsS9H2TTSsU_s2F6WXfotUJE0ktrndqzwzi15S5PRzCk4JBoy0HQ1m0hRCGbYmNWFjXumJPf5hwfqzFPTiZrfTOKUPkmrpZy0JOirs2MaNsci-LrzsY1UlfTclQGT3bCzL2y-Rw63ZLCv_qLHzBZgsclZICCjZUTQh9hLJBGYXnCW4ljRoULAMupbhQEsW3Mq3eDUlgYWNfbaoWLdGpUnnmPnxn3TCCwL2_WERGwNCiQQoljykeImSt8yQVCUCz1E9FYQotfnhDyHDRORPME65rFLGhIzb4FETfPR_QKpxAFe_BnGNlleqC5Hav3T-ThOG9odoB_Aul_Hr_TB4jFDVs4zSL5buPNeEHInc8KMTIKymPAWBVAUlDNinIYBkFiNbYx_H7tZiktQBYpYSI9uUOJIfSMxdKQz5LoPrXOhsXcueedI90Jj2Pi-S-D8v9I-cXXBs_b93usSQSswjUwNrI7IpzRqHdjDC5i7c-qnz3XlssJ2Hs4slN6IiuLUyhDsMuY8QmZCCVmJgPCE_-foyMSrTEi6PM2_LLv5UQNuk5_up3NfQYqccK2furBhYFmrWb6tS4-M5dr_MOUDoFbNbjIkeZ7s_Xg7addZ9pNuzj8HFN-FFnCuQemlDMRlX1cEbpBBs6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
سوال انریکه ماکایا مارکز، خبرنگار ۹۱ ساله آرژانتینی از اسکالونی: مسی بازی میکنه؟⁣
🇦🇷
اسکالونی: چون تو پرسیدی جواب میدم. فردا مقابل اردن روی نیمکته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/96425" target="_blank">📅 22:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6c6b7b11.mp4?token=c1rTEZPu5Ww2l5tJlPGCnOwePVs6MtkUbxNHnXZZ1iIGO8z21kYQVHTK0qY-mCk-GqtYFGPmaDwougeu1LnZW2r9KYVMLzZ6r53wb4vFIQQH9kIMcjSiKC4tRdFSf5BSqqliuKSCQrH_yFfAbxiJtMNbrpbKxr1SA1tZl5OJGwBXlX9mP_SRxugVDu9FhBOQblKgsJf_U-OZxVv7vJMiaRXmV8f5hOqxkKQcQOZuzK-HG7oZb8hYj2HedbvA-iLxG2cRSVO6GBced0A1USKS05Xpa5wtaGQbZUmWI2WdC9euXeF3m5suJRZ94EquGJ1I1A5uRnfc6zcDW16AAt8rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6c6b7b11.mp4?token=c1rTEZPu5Ww2l5tJlPGCnOwePVs6MtkUbxNHnXZZ1iIGO8z21kYQVHTK0qY-mCk-GqtYFGPmaDwougeu1LnZW2r9KYVMLzZ6r53wb4vFIQQH9kIMcjSiKC4tRdFSf5BSqqliuKSCQrH_yFfAbxiJtMNbrpbKxr1SA1tZl5OJGwBXlX9mP_SRxugVDu9FhBOQblKgsJf_U-OZxVv7vJMiaRXmV8f5hOqxkKQcQOZuzK-HG7oZb8hYj2HedbvA-iLxG2cRSVO6GBced0A1USKS05Xpa5wtaGQbZUmWI2WdC9euXeF3m5suJRZ94EquGJ1I1A5uRnfc6zcDW16AAt8rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
واکنش قلعه‌نویی به شجاع خلیل‌زاده بعد آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96424" target="_blank">📅 22:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cS4v1PSio0HUJOM71D0G3Cj5bTo2UjdZr3tSUw5Ai_B-Jx5ZJye-PT-gJYY1EOQImooB182HgMnM5Jrb605EqxgTwHOlmfB2unIE9reF3M6AFB07PraVd1WdxNVUU8Yv9dCXGK5Y-gE-NHwpsTe6fFPY1DRZxy4zU4KjIOzUnBqZXDzZn_PgkONUnCyqsUtvO3wBd1ipBhoLH6cEmK6P30cNZdTfIs7ffWyI4lp_qWNbIHDUbCu_Y_Q0WxmO7OiVc3TZ3LZ_LnVR81oGxOsnRcSj8d3gv-l88QHpo7OEXO1hDer2eE2XDqUm_ZJc66oGjestJQccxFHOPD6mpfR3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی ژاپن مقابل برزیل این کیت جذاب رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96423" target="_blank">📅 22:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
🔥
🔥
شادی وایکینگ‌ها کف قاره سیاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/96422" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96421">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CboPl6xnPe2mGuBLzUD6jkorC_ZF7P9PHQjr8uUR99m9ZvWxKjFLLWoMQN4tRVHrF_FQbd1KugR2iqD5cclPTjZV-AoeRxgikPH0qFgJNCf6KIh8Dhk6NrpSAEHNNXgw4VrA1Qt8I9Iumi86veuhrSSVin4w9AXA8pX2IqXJqFWmoW0WrGTXTp8k8bNQy_vlCp9mwjTaAmVKtjdbT98Ml4mY73q6Qh1Razdv6XI-JqipcwpywHPRi8EIGjhzxPFiPlLj8yC39fRsFsIYD217uCDbACumiajYKXFU4vjdJWidyJZWMuhfWZJ_TLncPmR3a-L95xTHjtedL3-BzTyCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شیوگای، بازیکن ذخیره ژاپن: «برزیل یک زمانی قدرت بزرگی بود، اما حالا چی؟ من فکر می‌کنم فقط فرانسه و آرژانتین قوی هستند. این روزها زیاد درباره برزیل نشنیده‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96421" target="_blank">📅 22:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAffURI_WOnmqag4dME2crBX9Sf7g2Kb791qWo_cqBB86M1BZChjBWLLquou9LSYt_U81TZ-Fc28FXoh2yGyjJOZtpKSsjcGNlyDDojd3tsN9xd2YL6_hamPfPTE-izYms9EXnsf79Exrf3OqwtQ3oVFm2Cnt7UVwbzxwOafSkZfkX608umG5Pli0s7RVGvAaDDXYv6qM7KWbYp_2t0UOsATRCQZdsFlsNxmzN1-V1-6VJf9ECczvpyBnOaRHUM_ZpVAqWXgh7MhNZktKofp4QoJgN9wmLzMSnS8-oxyZgqAHxYjS5aGN4tGruQRIOMmof4undS_MGnVLO307rjqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
کریستیانو رونالدو امشب این شانس را دارد که مقابل پنجاهمین تیم ملی متفاوت دوران حرفه‌ای‌اش گلزنی کند. رونالدو تا امروز هرگز مقابل کلمبیا به میدان نرفته و اگر امشب گل بزند، این تیم پنجاهمین قربانی ملی او خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96420" target="_blank">📅 21:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9ajYDFwt1JGAUKFYXcy9I41zJVCQsgnuT9gOYyawcqIFAPH1ffAafgMKSax92dxsK4SjFsoIrIuie-2sGsx77VJqMi-iCg3Q15sPqKZeePgAkLP3gTqQN8pgS50zgzv9kzc2D1p2cSrL6Ktp25I9nB0ut2fJtfGhXQVWcrukIpOFZ--fcxP2Ec9Qo3P1z1ig-h5hIsohqK4JffbOkrI3Z0gD3tHX1Eq-7-GvApr19B9VqWbElnvijQJW_y1Pm-QwZmMPHdMlntn7EvfOiYYZdrijxS-SoyF6Us275AN3hPB6q32i-TinfhGiIHY2KQQb4-R7FgbNPRYbZkZIiQ8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
جالبه بدونید ایران با 3 تا مساوی در صورت صعود به سوئیس میخوره درحالیکه اونور ژاپن با یه برد 4-0 مقابل تونس و دوتا تساوی جلو هلند و سوئد خورد به برزیل :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96419" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7792e80fbd.mp4?token=fpAXRsoT1FeepkF3aP81gR8q54kf9k0wEsfuOPD6iKgIsUW6Ucl0iO5_VPXmEl54LG5q5cytJnQ4M9NzGoM71MMZYejPOEoLMM1moc0ofNg39F0rpsf-HjHx1UayWhXduT1ym4mGtuJSgnnTJH-bMPvwj0HeLFGTcM2d9mgTO8Ro4zEMlQn663e_y8Jx-HedNjoyiCwVdpmQdbGhNsEcbcVsaepVua8UFAJ5t5Xj44be984qnLMnHGu9iBeAfdpY6vVT0WA2mNLlp2zu9Tmk5Ip1xRhcwCR48lf3nPBM4WMzKy5HnknSuOw5uz4vPJe53Vy5KTcwfPAxvxdCjYa91rChC322TNTmsmHTPePBJ-7hyw2LUlMeTK3qjwNpcZkCCb-0Q6iN9pZXr38QMUbQInetYoU7DZSufZvnv_RDrrmZck7mQuieJf7Z_OVEFHIEanQ61NkOt3uqArGH9ztVW04js8sn0UuADR99fQc5TVp3R3Ln-Z_4IQQ0sJvGmtYxEPzLqzeqk8L4yjToJAGILiso4Kr6XuWTZp7yutS-VTTMK01tggA1i0EdR_rvzmnBPuq7iVPKDzJc92LQS-RwvruZWwni0SIGT94NJ8Q5FYIW7Gc0Sk6OrUm8CQ2uxheV6d9PjSH3iBfeyDtrzQTj_7jRS5qMHhKTLV_5QePR-Wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7792e80fbd.mp4?token=fpAXRsoT1FeepkF3aP81gR8q54kf9k0wEsfuOPD6iKgIsUW6Ucl0iO5_VPXmEl54LG5q5cytJnQ4M9NzGoM71MMZYejPOEoLMM1moc0ofNg39F0rpsf-HjHx1UayWhXduT1ym4mGtuJSgnnTJH-bMPvwj0HeLFGTcM2d9mgTO8Ro4zEMlQn663e_y8Jx-HedNjoyiCwVdpmQdbGhNsEcbcVsaepVua8UFAJ5t5Xj44be984qnLMnHGu9iBeAfdpY6vVT0WA2mNLlp2zu9Tmk5Ip1xRhcwCR48lf3nPBM4WMzKy5HnknSuOw5uz4vPJe53Vy5KTcwfPAxvxdCjYa91rChC322TNTmsmHTPePBJ-7hyw2LUlMeTK3qjwNpcZkCCb-0Q6iN9pZXr38QMUbQInetYoU7DZSufZvnv_RDrrmZck7mQuieJf7Z_OVEFHIEanQ61NkOt3uqArGH9ztVW04js8sn0UuADR99fQc5TVp3R3Ln-Z_4IQQ0sJvGmtYxEPzLqzeqk8L4yjToJAGILiso4Kr6XuWTZp7yutS-VTTMK01tggA1i0EdR_rvzmnBPuq7iVPKDzJc92LQS-RwvruZWwni0SIGT94NJ8Q5FYIW7Gc0Sk6OrUm8CQ2uxheV6d9PjSH3iBfeyDtrzQTj_7jRS5qMHhKTLV_5QePR-Wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
💥
روایت بامزه زوج ایرانی-روسی از بازی صبح امروز منتخب ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96418" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnaz5fC0BSo_bEZve7cFrDrTgqZqQf4eoyhhXWGUC8Wb9Z_KgU6mFlRZuPSiWRtlX2jcF0subMENAaiaFdH8rl9WzokRKbOsG--585LpQ2XIuOHOMwxyd-FopmVZ-tdUZ8r58kjjvCmrH-p3TqC4HpQayiLflGX70pfTr-56cJX4_-deMd9fqB17HECN132YnTJsfunGBObb1UdciBjKeylEQvlEx_is025Ag-kFebkpiRxLYXModPUWKWFs8mJkVxuYhquCyGyyJEtwXGO0_afrlPvmHwq9QASHnpN5q7D26WgwhGppFd6ZrcFCjPROXgcCEI6o3i1q6OdLFSD37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه لگانس قراره برای یک مناسبت تاریخی یه بازی دوستانه برگزار کنه
و اینم جایزه برای بهترین بازیکن زمینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96417" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
شادی اعضای تیم‌منتخب ایران بعد از گل مردود شجاع خلیل‌زاده از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96416" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyE4Gm4X_WC5nkfZv6P_4Gjd-cgQGDBkkupnIJVNhDwrOIVOSCJzGlNptUOS4hgOi7YjWabNteHnRwDuS3NY9577P3UK0XiqhYu1xEI4qVyGFaisDkxQKJrgtEXnyKeC3Q3SKmCxrkF82p-E_D4-fG5nkVmMIee_fj6j9wo8nAdcHDTa-UYrumnK5o5C15MwmKwBgaG8vm5JS5JBdDq75JEx2OxasAm8sEA7yiVWs13_-3gvCkUl9L-D5pZOO9KKov3uDgssG1zb8KZVCpHnNA6qSCppojS07McOwqAZBzJmxE8JisgrfxGv6EY71jfxcHcDJPpDtvMp_eFGdAQnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
این می‌تواند یک مسیر ممکن برای تیم ملی آرژانتین در جام جهانی ۲۰۲۶ باشد:
مرحله یک‌شانزدهم: کیپ ورد
🇨🇻
مرحله یک‌هشتم: استرالیا
🇦🇺
مرحله یک‌چهارم: کلمبیا
🇨🇴
نیمه نهایی: برزیل/انگلستان
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال: اسپانیا/فرانسه
🇫🇷
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96415" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh0H2Z6V_Uyj7DjFzYe6cXgPtVeYCK3x-uu13RqgXeD2PV4qxx05izi7XfH8SaulS6OnZMWKyNL_gNS9AZLIMjSFXiFYyKnWQr54E8CbIG_3QGvl8-puAwMF81bIW5nBUr2cglpc4L9L57UFeB7ZfSLj8UNq3jFXTOOV1c9FusGiCHwnvn8gmZnQtPB8aSuX17W8j8bXCxUtA4Ye9-eC6G76WY-ki5gEUmrTMSdZ3ij3Jb3oY34Zq9VEIa5uDC52xMpz1hB0S-gxK_Bf8lTAw4gocgfp4pZkKofhgYw3ffJx_VjgYJndpNKjBMjA5mNnjoKu2PMFDlp2chZY_sEQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇵🇦
🗓️
۷ تیر
⏰
۰۰:۳۰
انگلستان
🆚
پاناما
📌
صدرنشین در مسیر صعود یا تلاش تیم حذف‌شده برای پایان آبرومند؟
؛
جایی که یک مدعی جدی گروه برای تثبیت جایگاه خود وارد میدان می‌شود و تیمی دیگر آخرین بازی‌های خود را بدون فشار صعود برگزار می‌کند.
⚽
🔥
انگلستان، با ۴ امتیاز و قرار گرفتن در صدر جدول، حالا تنها یک پیروزی تا قطعی کردن صعود و تثبیت صدرنشینی فاصله دارد و به نظر می‌رسد با توجه به شرایط، کار دشواری در پیش نداشته باشد
در مقابل پاناما، که در قعر جدول قرار دارد و عملاً از رقابت برای صعود کنار رفته، برای حفظ اعتبار و ارائه یک نمایش متفاوت در آخرین دیدارهای خود به میدان می‌آید.
🚀
⚡️
آیا انگلستان به راحتی صدرنشین می‌شود؟
یا پاناما می‌تواند در آخرین فرصت خود غافلگیری ایجاد کند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96414" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2riMlaYoLDCEVpg1ufoNPZmeAnic_7UK34HNrOIDJ4_Pk4Qzuw0Zn19bajWD_ate6c8nNEOYc-rwLyZDq5XM34Qrqc4wVxUMIbw4iltsjFxZDdKYdHkZCq1PlYTpKWjzi9zXnqrfZ6ajo9jtTygRyIy3gONmkdmEn4W0lvSj6g6QzYwEwafbnbCm_oTMjcGgCbk6KS9Od_62ZJBzptN_a0xMUi_kF2GHJrDd1_aTP_SVjMQrvbbd65y95ZvBHmmZBO_ux23iT-tuoDH_uDpLrlR6NvAPVhLF5rjfBKzlVfjHtC8P50D_pOwJWZ0B0b2KKux7r1pcAYsqTQ_GORE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inJfT33graFvOTkqouuSJi6-Gtp8T-cAhxsapFmk05WpiAnuHEmzOV7U9cWm_1_KNHiTBAPqoTBfbOYUpMp9iI2LoQQ80Qdk1lmEedktpyTIardp0GfpHq_1elgTM4LkvMqDaE3-VkMDqzyeXFkOz98XOKcfIceHHramamD-UIlNpRPD9gI7AFkHcc8g03QxYwCaB6iKUrAuh07DbYy8TNRntWXfAcZNjpmjQkgixkDNUmiZvn9i6YIA-uuBBu97dDc787vdK7NTBTSX8cbBvB87lwXnh6d8V99qby1Pbw8855uyvRahNhVQBlOXxSi-TAwp5lV0EqA6CvtAioetXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YU-QpIZQBIBJtO3iXFZ4HhSpXWvX_2SIqTdvg-mnxQjyVslHXLUBnZaecZGDQ-EbW3WITdg_3-gLX7Ko5RHf9xGHfEszKCSomzoHehWRfb-cHThmspV0CKSvXin8NqHNTStjEP9l3HyHTC-Sr9Yt0ljiPaNRtHiWG8byrbVlx39P8v3t8B2Wt1F_nhu0mM4aoOZpTI9sgPdL5q7DmEjFORRLOSRbgBT_mz0r6qYPXx4gvzc6HqGeXJW4mBx9Mfh9S4mzCCVr0yN3tq4_zOImSXnMPkkPwlXYJDOzbKjXINIKsMA0L3KAGXNAUtwkQ_6vXUYSvYLg9024NhDL-R1r9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIg_ZGBCO7Qt5keaQp72HQ0z8m7nUrkB1wKXTu2IpM6Q9xeww43199WE4WSMffIAr2YS7WzznrDj7LwRbx2tVgh80wid1PMXPNjP-sttJo3erk-XHQGN58Pyp0BJhiVuFbUuSE39nQVrnYgfSZA-CQ70J3owpEewqCeFf-Xiu4J7UMKMGsPFDOUCvm72n0jUoax3QDHYE3vQfufdv-iwlWHRkahQrSqausnsu5LhPsaAAL1svcf7QDobPRdnXjUk5w0ciZ0_Zxu_T5sUMCDcPN8oBYZmX4ELOdYzn7tmpp6fcKzMRjcUOLmgdsD6zlvgSt8nmnqwy0pxMuav0GcQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJWnmLH3wymLjIlbBlpfNy9woN4GSDE3ZiWAg4t-kf4a1g6edDahjKMPdE0K75V0Epc7tQ2tpQ_pcJhPQZ7bBkjtubqwfNK-PWG26rAORF3El4UHU2Rh5ePzAvjDd5w2sFvXO5CThcFnSglWcSjdYZBmN5MFjlO8VQN3hNpV-JI7Gmhdc4g6AenPf5c4cY5dTQFbfC-1CMPYMJLugpv2X2z6_nZVnj6NAj3T_-F_uvLPzCpflLDjlHesltKBHJcA_YZN2Q5A6UXtceyOOnP3yI400omv-Tc2AI9pYMPzxwfs4wHT-BlNakMu4Nwx4osH7P_1fkbovWqSqTBPsh3Cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2CqwSiLbTG62rj9OCieahTpuQgpHSsj9tjMJcbvpeUxAh_sS5a_btcSLEycqAjdviQ4UAmFNzwUtAQ-8YfTybUXSoRbLlq7R2IQEwtIMPKpBYpyMXaIvfw1Vke1mVxGW4hANObAc9o5fpDoH3ZpM-QtsLbyJNRnl8H4WekN-DfwnuZB86dKMjECDu-TkRmkwkRmi2KeI_N4GPpxfrWoCsPDU6N6IEYMe7uPGgAAgM3rdivtup7Q0D2oR3GE7ev0OqxTi8TyNBSpdCUSSlt9T0ou1HzTgKZydz_1iasSs0AfFhNK7jGqxv2g9iCdFtjXJGayt_1gWg7v_SMqdi_sxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLmmUQaCL6o7IJdZ7r4IX3m7SanWS5s1mBgPJcds-fIxilrPqSbGkDkmjFolsPSDhguS-MpL9pki9gotGAHti4VOiVE3dHteNYn2yP9xY7a7xGxYb0CZj6atUZCh0VCTSc2api0YaNQ8UUzR-FXcMtixMnk7nMyogruE1Xp0P47ZURmLyzSohEQGBbPNy9YhedckAAO1dgQg-0UZgDEWD5lAVtY-Is1cR-txUnhyvaAzApcN-6cmJ8yTl9qviZMLoi8u_bqZmeWI6svUDvoObzKwxhIWxst9nQjz_zDR8oeTo_rBCHe3XyvPUyZo1pRY7Ton5AOlESbt8FDBTsQcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTaughOxWbYybskY2U5qJlviyX6lVgz-Gyf-H9N2w6GtX8fJ4V_48SPqrLf1mo5RJZr9XdV_-iuZWZ0uLFnRVeq6bYaYwxc1E04-iZpeEZuK0bCkVYYbrdCTgq2cVd1l00McZ6_D7DafAqbulMS4a8tmun6O5bap6rvm2RV5pAMQs8YwNMfk0iwA_ysvFJtsGKGqE-ZiQsgiH4UXV842MOQkPrfGvLBhZlbFYccrbYMbufjq7PvzZ8AO6Qou11qcARPAzb0qjkqcRqRVEbh7B8VLd2UWee7ZbvIc48nmpxwxdjc5inwUVPgKvW6awo4LXTk3eZu6WSqcsV9k6ssacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiMZuvMiZ2sTSz6GIq5wa_IinrfPfXOHBv1-4Y4sZyT2JRbCBhKuCvXVoDIqkROJ1BHH8n6PvgEn1w4PDhuTjg_ZA9_PvU8kJq7V13dDI_NSuBBpkb1E68wWx_uAiptIcc3ggdCQlppjAz7o0y7K-gni950N_JE9NtrQ_woJ4scFpcoeVX5368Xl_SNHl6-4TwAWUtYb8ZPrdXj5WrH41eOdknwDkdAXro2AvZ5mpIo6becv6HIX4cJvRhe0quaSwwBHTzr8mXY-XAs0_q6pibgzpaq3QvpXr-oCI9xF0mdL0cGdHzy5190DaphQQQ0q5L7GQHu_qwN3SdnIv1GpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
🏆
فیفا با انتشار تصاویری نوشت: زنان ایرانی واقعا زیبا و جذاب هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96405" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWdY0M2vM1cyv8tiNsd8kz3V72CDQVLoBwTftQqEPHg_QEpBpE0lvqY0PlfTsng_U83XGavfllqUpTgxL-DLulQRPqOKJcLzJrJpextocYrTWPt6INpqmbT-PyS0tYenn7Y4es8ckEjkK4HiwBT2kvDmpmBTHthUE_9mqsU7MI3CP7AjKy1fpwiLJQhoQJS49thOleYE9XtqbSXSmUeNRJVaBSDVjnXAUVYl7G1Z665fsGrlId6rSplKEbi99ybTbHpWdCDFfjcMioQ7KUtHgNgprR0AbvV2gGK_TzdmDoaotzufrYwz9CTKYWs-nmwCMem1wDXxpUQkhLydbhKTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
بازی اتریش و الجزایر هم جالبه...
الجزایر میاد نبازه چون حذفه از اون طرف الجزایر میاد که نبره چون میخوره به اسپانیا
اتریش میاد که نبازه چون حذف میشه
مساوی و برد اتریش هم مساویه با برخورد به اسپانیا...
خیلی شرایط دارکیه خلاصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96404" target="_blank">📅 21:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
مردم مظلوم و ستم‌دیده غزه با پرچم مصر به تماشای بازی با منتخب ایران نشستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96403" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU7Tb5wic2wnmc2SL3ZPq-NJafuBC16Y1rh0HAl15hip5M07hwqqeou7LfreOqClVCrRr81lS6dMh2bOtTyFIoNbGC4ewku2x_TSBvpYITGudvZEdSfoLG8quLPaca5fLdOqkufoPKvWbw5zmvNlDh3TPy4HHfxMdPLMDCqx5a14nARMwkFldc67kjbxt8VZjbSmT4o4aGpfKnxU-R8jOwRDKYbMbZ0deKqor4lOmD68LYYhG3QVqzubo-hxgoTVn2dEJ_jPqUFSChpk6v7qDXQw7bB1N-3uwOh3AT1l7Pes-ntIKE8lKnw8q4eQM6HyT1DYSn9s3j_Ll0UHc2jSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
🇯🇵
ماریانی‌ایتالیایی داور بازی برزیل و ژاپن در مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96402" target="_blank">📅 20:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCz22QS5NR-eoBGxCNxdf8qAhGzIsVDFjqvKYUHckDi5cy70kdfhFOdvItVsjXXggxe2jItBvmVplGR5ccZY52qA50ihJfqeQsGIDftaG7bAL7WBg3AMUDbTSHOmiLt_FpWxcWsdsHZLcFZ8em6UwmF65qreN0CHhTt50ru5Qan_7I9RiAxOf1YZuzxLWNrZuWPiGnsUbXBK-pl4GGk3hJKWqQ1A5RVE-i1ztPgjd7h6HjJy9RychkbaRQ1bS9cMiEbN4fNFE6jdRpuAJ8mRJGXwCdX-yFm9m7UMezZRCL64nA0y6W8te8LjqAuTGXsAXQFYsUc9mlWwKAalw7mROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پشمامممممم
یه زن و شوهر تو قرچک که شش ماه پیش ازدواج کردن سر طرفداری از تیم فوتبال ایران از هم جدا شدن
‼️
🔺
زن طرفدار تیم فوتبال ایران بوده و به دلیل اینکه شوهرش همیشه موقع پخش بازیا آرزوی باخت تیم ملی رو داشته با هم درگیر میشن و آخرشم از هم دیگه طلاق میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96401" target="_blank">📅 20:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0tlvPVA861jOYsB_swqXZIrmnT5k0Z210QYHi7b4zi85ANWjHMjG4SjBlZ1guSQRi9u9cewQDwxyMpCZ8d-h_UP34HjVyo3frqfroa5w_gMFkv4qUlG_wyyMPz7DABROUX1o1YQhwIQEKd3m3PKmcKc-q-yOoJ515IYoeIqMePJS-ayWQmeF_x2NS_xNYE8EF7xzIoLulkenjXJ7x5gCA-QP10M-Kbmb0EF3x7EVdkZ9D4Rq2se2jDr-0oka_01FrfV48JVkvJzH3-tAtT2W8u7wQKyvCd5fjMnilIJYNcJ9yVHlx6lfv43u-yaPegDDwlTh1at6JsCczZrbl3ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇯🇵
شیوکای‌بازیکن تیم‌ملی ژاپن
: درباره تقابل با برزیل باید بگویم که در دهه اخیر تیم مطرحی نبودند و دلیلی برای ترس از آنها وجود دارد. بنظرم فرانسه و آرژانتین بهترین هستند و ما از سایر تیم‌های دنیا چیزی کم نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96400" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-CzKdWvyKznyiIsOhx3a7zvQTbiOpGLEx2xzU4AZr1jvbiCAhAbi5Fc2C8oojPrVlzvBo3ifWXrH3-IQo4zlH2WPbOBE2dLQl0HhnHdiodOEw8XdNiDlFtBR8fK4fStTodjPZ691Dw_Z3nkoYWmcgUBGmUwkaTmYmfN0mUS9tBV5xhuhZQXMKqlmiuiC2u-50rpAaGnDiwSfv5aXvNQKI0IHOdlrDjX7sVgdWj7rJBu0rhZVwjH6-Blsx8Zbt61LSOFl5nSl746t0tsdQlHhdCysBMaS2JaLF6Rygfgjlt8YrN4ChZWvw1Djps0buU8YXtEFXzuZdjPWlsH4LIBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده مورینیو
حقیقت رو بگو سیمئونه
اعتراف کن آرتتا
آیا او بهترین حرامبال نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96399" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmupZgQ2GPc2ZlTRfwFlpFcTuO7By1J-Ntl7aXyzT9MJHe9jyWhjO0NE7Yi-qSsRES78TEk14vXv--z22QIEerFRj-4RaB8b62qJcsDRT_faEjDj5owjo8wI9VLWctGgYxFjFHpFOq4Y4Lxo14sHamnqNatx7JQ-YY2JFCWQmjUiU8COagl-CYYvtLEfFOyBYFNgh4-0Qj1i920RQEaR9uk7vrOBVPrmQIpixfWShKdWGYvnNYdJm8KQW-rrBU18LBeTaU-WeLIiuaFGW8mXvXryTJRapweMQJ-ZWJPSD4wwh5cZBOw6-fc4Z_TdKObyDKChbh9D9likksVfNokp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLCNtaq8MEbvTGTx0tvk0Q4_lPNJkK_UKYciXkyhpwtrN_W5_xhfZ9PuQu0kXHzTQKTgPJpyQl6s1VT4n4T8Xrt5I8kr9HMEJNqlv33HgZbAqEgFLQd7gdjwGfsoxwncueF0wcgYqcDCum5vmyYvyHVkG-yCpLmQVJ6IhDFfMW_zfB9hWXTaTSHWYQ1BRA1Nzz2rXWdlz9k9JHfEgf0nZu-ZIjopF8LhvywbLXghJFjfESXn0KKqdygfqFwA5eyjOmdoor9gj5cj2fe244hbNDgk0Fc145Npcl0y4MyjQl95ozF8zW9jp1osARoHMArnAH7i-deF3vqYhMA3F1S87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioqnJiLRvw8cwHUuDOz9_yn6Ppcjis0O-J1F8B2xeBSoo-elBis87k5EQNwYDBXzasAP3-zhjIBpBt3b7D_t7DXkmfkaMkMyhTVVb3miWzEWEpeEPlEF5GeJ9bJQUwIamVwujD3HJMePQi-2723302B5Cy0iTwNaWz80oko4ANK0WmrpKoBdR3zY6D2xw0zzA5dyCHrHkFNaShs0z6L6bkoI543lL1cuY5A2jkBJBmwjOchYOo1SQ4MxNkbBf1gB8BNb_AJC9jCrOqS2zVnX_CfjSDtnfURQoiZIw-YSWvme6WUkbPg99zA4jS9ObB6CaYS8UGcEiMwTuQq58BxNfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🇨🇴
کلمبیا سابقه بدی در بازی جوانمردانه مقابل برخی از بزرگ‌ترین ستاره‌های این نسل دارد:
🚑
🇧🇷
نیمار در مقابل کلمبیا در جام جهانی ۲۰۱۴ دچار مصدومیت شد.
🚑
🤩
لیونل مسی در مقابل کلمبیا در کوپا آمریکا ۲۰۲۴ مصدوم شد.
🇵🇹
- امشب... قرار ملاقات با کریستیانو رونالدو
⌛️
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96396" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaVTgcdeYihiFSRPhAu0f_QWOllNLxoTTpuaffvwDKMydPT-TcEcFCVFC5-bXC01sr6d1h7npPdsy7p8lqMO894UD9f4y44BSI9o7FMH5eCJJHUnotqylob9LzDYgfyI6mwUjA8bmIjE3ZfbeDFQIZDc7jOIX7L7meoqoUIpVrtSuZUC3CqH_1-41sJ41t5jOqY3p6Ni5dVUmgtK9Ws8RkLWQszG7e0GkI52iQvRXbAFrg3hqVXyEB-_cL4LON09SHwDbhiGr96YVtQcJERFGDhPM6Akb88kHVoHCOlZgUAmokrJPEGKzzusJYZT8Nx39fp84_VloLyW52r9w1a7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری
؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96395" target="_blank">📅 20:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فحاشی‌ هواداران داخل ورزشگاه به کنعانی‌زادگان موقع گرم‌کردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96394" target="_blank">📅 20:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwjgT4mszYiHSHhpP680dM3Td5gqb9oLS65CdHhfRfhnKXwibP9Ssv6wU772Sn_q6zX4zsJb-VZAflXIgpp_FLnQwmmtR0HJiItgKBmIyIjZB3lWaT0J0zpcFNKjY88Af7yABfGseYm_r5mCDRWVOA-ISpqW44LVUkJ-R6-cua_wzEqeWzmLkzE5-ssgQ4wFaKkCd3ZFCGGVjEqyaxcEHJDlk7wz62hMYtuFAEf9WFALkIWFgAr4cic3L-q6czX3hL_MaMM01FfIJQRkW5pfMfCzJuYhDUF87YEox9dLa6TJPhQF_T6oCBQGYuE1VM_9X8RlWcbmOYExsVSkPLIuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
نوزاد کودی گاکپو ستاره تیم‌ملی هلند و لیورپول امروز بدلیل بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96393" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
انتقاد تند شریفی‌مقدم مجری صداوسیما از امیر قلعه‌نویی سرمربی تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96392" target="_blank">📅 19:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Clvc2jety22C5s9FtA6oyKlnB8oNXTbzlMTeOYIZv_QtcH1mIiNtCUG2lEiRiWyKZTIUahbWKew4aQr2UWszf2tC9osCZgYn7z_ufqmc-rSVFnnqmJM8WYOenrDGwdC54-Cnx0N6bpP-mHoP4JIBluNH5mq0Nok2ooIkohFIJUnYxh5lSjWZDKizGC5DOd3l_X3zXazQW2dHhhr1gUSpoXrzizstocPGbCRhhZBbL6CA_OpopOlhBHSNbnaG8TQDrujkblQDwQ301nsGRS-MDF3xQCqcILesIYicDWJG8TiYMTBVodH3L-feq8FtxwMCquyX1RAeULzCV7NEy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عثمان دمبله در ۱۹ بازی اولش برای فرانسه در تورنمنت‌های بین‌المللی نتونست گلزنی کنه.
🔺
این درحالیه که دمبله در جام جهانی ۲۰۲۶ در تنها ۳ بازی، ۴ گل به ثمر رسونده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96391" target="_blank">📅 19:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی مصر از لحظه گل شجاع خلیل زاده تا آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96390" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96389" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYEUolvJdejmDUIMpx3FK0vt13rTAFdz2qElY3LtPVtfDpTfAyi7W7vzcZA55rYHlShGUOJXvhpHADI2r2OcH2Gmqt4QuKynooSNV_JHBwdMHarqz7AF5gzN9Z6hz5uHLwuBryN9NCSq1grKDSvlr8IKfW0mGQNVPsWguZNa3LTBuvd_oZnPMDXVok1DcqWsnip2lpVT6kURBAU7msc82XApnBzt-PtXR4Dhf9Kv-1aPVMcpPZNLFDucMBy1mRkCjUrcKZkW3eXQ-U7Jg4DpBJaaHJLxdgWxA5k8RlKPSSBfPaFaSL1FFOEg05K1qEYv4auLgjkZK5kG9G7iUGYCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96388" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی میگذره کلیپای بیشتری رو میشه؛ وسط خوشحالی بعد گل شجاع خلیل‌زاده اون وسط یه دماغم باخت دادن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96387" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
جلالی: سر حرفم هستم و قلعه‌نویی از مورینیو بهتره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/96386" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCuN_eil9WDgGbUqprblUqxDWVINIvYdu3SX0bbSojNztecAjtd7fRanzuatD89h0Aj55qo9JvMLPycOJ30442W_p8dgJaPVm70CtLBn4d2sFV520NbCMUrc8KxDxCNqjr9tT1gr7J6pYSXn9LD8ylWNp1DE3ofh5Pd1uSDrBfDwwSsev_sVnpodqiwzlRZUKcA9li-Wyu0rmIVSaBlDU5gCrfLgeaw1_uR3mS0BMQEyo8ska4osCuql8Dax-05X5KX4QbWNaQ9qEl6ADQzLBY5uSl6IuGamzKSyrWIkN3dQy-qe4HMwAEfsrhPLoVI81Gek4haTCLBVAk64u5KGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مربی های با بیشترین برد در تاریخ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96385" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quXhV6E4CzkH_rBUDTUmMK5NKv6xtoL8UyJRC07ysr2V0QCziVjpPx79TQAc9_XdKXdSBR0WyYFA3XkKGafLnLDjjMmP-gL6SD2tFdA2jLHOcJS2OtV1u0bKT-jCDGxhH_zuB69TrswN7VVC3GmgKSQR56G3_TMuHMy0-Eo42PDm7c6QRNxEOGCseou2QCIJLNngEKlLB95ZgAUTbvAtOpSAmQWVj8recses5OS7_bMDYzB9HlMOAfxreE4izkh0U7XTjf3umjK_dVjxasdi-meIulCZY99B_FmfvavgImxGHa5mJdPTPBYgz8GlBK8fG81geu_AhTsHqYO7HJnrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کفش‌طلایی کریس‌رونالدو در تمرینات پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96384" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IymxLAZjEPh5_UnSdV_DEK57mxgJiYfX_0xJL1f5I1_uT2Fz5dwWtVscSe3M89rK6VKnY5zTf6gkqUx3eKw00mmV5nzzFBvUHjvvYi99h2ZmDIJnaql3GTTqf5W4gnbVyegaGefBoQ7f6axBBmKaiPckenr__OhRzXJVCKrbxeNSM-1cXMDqUHzZf_dqWtJKUppSwNzWy-wofjvJwm7dr7R_d6rRSphCMPDPKSEVh3wcEdEv1yhqILsdrSIGfK5QwJSx_fshKWQrH4W45xv9vaUlFj2aAW7quSN_VXlAsyidvVzPem7hX0q4D74PKtewojK36UT-Y-xQgXgJeFVjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده مسی از سال 2022 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96383" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9jsd_zLWi9RSIV1aV7brXucob8g5lfh2XeXQaehkLZnhp21wuDpHcEKStgMPbBUhmzt1lvoLHa9uwnBtJkd_LttQfZCwfwTR833UGgyU7qvvSpb6Nuf0aKUXD53bHLJKvLD3CMY7-Gw9794gwOATzfuVDTBrTBkVdm4aVc95VGHEQdqjLN3V5_5Sm6TaNoeK8fuMhT2JvYCZzR_ML4wMPD6L9-y2bgvkLa7lnvaSBP1rw27sFwCRyYMIKkUyM1d0T8T1p6UVRFFcfhu4VSi2Enbsgk1YWR1UjIu5MHZmiPBHzDBTTSvQmZnaG_ZLBW2C8Yke4B7ABacAvDkmQGgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودری تاکنون 328 پاس دقیق در جام جهانی ثبت کرده است که 109 پاس بیشتر از هر هافبک دیگر در مسابقات است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96382" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzAm3I_WlnY0KqVIrKqI7zDMz6HmfOu1QzkPMqMgb4GaWFTgQOmAA4Nn9X-NCQXXFGkvKXrml1-g2u1h8gYx2LgYMTgCXA-inC109uJybQQYBKclLGOVbcyy-Vr6H2f_SFBxXAylX8rHplKiYOFaHdxAWJm73QAOVs5gIhfUBgaOFyJ9wbgwaWceLPJwh5dqE-h4cDL38Ga_yFsW1CCKowuTD2fEcTGI9hPfq7x7sRMV21G6t64-GVul62TKKC7Nvo1THqs6NG_ZckUM0vfJsDlPTPVEbQaQbPrUGIAWwomFON3Tz38vcjfxojgZt349Us0k5egQe4aaR3xlPnOBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسامی برندگان جشنواره ۹۳×۹۳ بانک کشاورزی تا این لحظه
⬇️
⬇️
⬇️
https://www.bki.ir/fifa2026lottery
‌
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
‌
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96381" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cke6ZmcYnr6GQVf8fULcro-ZxM4OVJTzWtYnZTi3Z6GrGIv__RpgDId4UquK9WL5PmnvLmSUSXbEkbBR31US5xEfo5FF2dX2HPuSbwdHADcXSFjNT2h0F2U9QZNXXV_NqzgYXsU7n7OA_w5iZy5cVXzslRA08J0j_tx-qox-OlJFFwbJSYTYPvqjON8zhlT2A_rh5deTQuiXc9dIaonJNRydBx9RwpjuiPw4RLVrKiUIGHiad5yuI4VGIfHYXo2LOL5RLKIPNMQRcjhyunha_kywWrncy7yia4bes89cPyPgj7Cjd8Fz-pssbWGWFb5yWfMkBXXmejBUv1lrZ4PqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پرز بگید حرکت نکنه که اوضاع خیطه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96380" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgwQNZNN_SwC4pu7Zq3jx5hO5xnIZwLuFoACFBSOwH6ACVR_qaGZ_eyAdR9P2SpZDjn3eYJGfYmf7l05QpAgCz-6NXVLtwOEaru_pXvXJ_SLro5RA0ppMTmQ0fnpyZwRLkhV8bibGOvzGacHOYAP1pwdbj32KW_UAKSX6Zx3KAhZ1wDMdVOErThyo14-ctuyT8dl8bBkytCDx7F5syfxjJ6yXl_Iyi6o2Rx_9hsuasEDr1FZkpsKei3wV8vfLNuyqohz-KSZBa9iVv6qrth4dzVd6_gWuddXcSnQE2CTLBo82wyQ09IadoF2F3Qa63DdE7IwRWhDNm17i_v6fkWnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبرومون رفت و شجاع خلیل‌زاده تبدیل به ترندترین میم حال حاضر جام جهانی شد.🫪
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/96379" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tINOzXAoAZV_IsI9qQoemWvl2ltwUsLg9W8SAZYbP1xA1wvWEC9lL0WE-H20zOoGqZ8VVzqm1pt90uw_Yf-5sAqHGeVoJ7qawYvQoyTLjJsMeiadAoHdpigM4gOC-J6miUoiZA1q29VNEMNXfqkZfB00Aw9QoX3Qn8BKcsBh7hiJYWBcGvNAD41i26dUi9dhHNuZR4Ex4m-lt-Jn6xA4ru5ZKOv0FBEiKW0pG0OV-K-3DVZrBNQ0WvO_01c4PGKdWFZaiBDJnm2IovbUBwycN99KfDVNVIXT00Wf8SWc6mZMhl8uV6R-1gIbPGEOQQfsO35MFpNmVQyPkKgLAycM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bd5QsJImBjdOrixrtgJbr3mwbxpd2HsyiE0mWAL5ozJYM3c7Kv2g2-enA8PAfAJRZFM3beIifl28gXvPKjIQKKdnL48P6UCC_uZfe6Mtx5utqvdom2i8hl44InvfxrEeuwYvipwPhf6lyM8U4B9JthRh98ennXdhGvPEnGu_oDetASo_8FxD-_BD7tcpLrjADCtnrS5q4l48Mlcqif4nulTyYlPorE_ddf0rtWzTH_DBaJ6048ehe-zoSbQ1AU2UgA_gWV6aQcftY9DOfSbqkhBxn6UVepkTQSKZA5_ArvEqwHQrWOL4tYseY1tvPRH4qRdxjxYwEj05GvvrvQak-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPrTeVnEfytaFchEBcbPLTdvBSh6pzUs-l4ohZ7jM6QP5lIEk9adLsrgbuSEUYrPKTR9RKlyUTHDRmvq2OhLjwf76zBdAmdoBOd5vWY2riIRvaYy8UiSgq1K9EUUbCIEInT1udJGQYH_28adjy_iTkdeROQ9YYcGdPKwuiy-Xeqdo-P8ZfUH2_R7eHkfQU41OzwRCXYP-Htk4QGefl26-a98HcMFKrYkvAERjRCe2FwvHgl9i7puPOHXxe-CkBXu5V-MlFzuVEGuuWZVWjvq4wAGRE0enz1lk9YhNRVok1ZdjekOZEF3PVEde6p3fkGRxCkyjH3fM_Jw0rDkETZxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG_H9vInuFVxx9dFs1N89Ej9IXLeJ_fatPsEAEOAD3WpoU8W1TFz808D1UDAgu8qfxfVAsfPsB12f5VwV0YBSk0VYigHRJ_7eKObTKHeM-UIQtHzskqxOBexCj6OgfOjXQXDB4cyZst_DGqOC3rP5JFNqOX1xc7iH-UP8JL8LnS--WKgOQThUAuWvVlYmxnsybyMB9DozwRGgOQL7RLoYgNIGHsBQBl8HPlWVjhphsD3XMqMfTOqO4iRgYvOOTPbpE1iR1OfqDDu0vJ42rsIKZNuU_ASyprT-3RSqx9FXYfSDZd4ewcKOgj79gvR1X15YHQHSHtl9aeNIKEGQZEpPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حیف شد عربستان دیشب حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96375" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96374" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96373" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96372">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
دستم را بگیر و مرا دوباره به آن روزهای خوب ببر سپس رهایم کن و برگرد؛ من نمی‌آیم...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96372" target="_blank">📅 16:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTW6_PtOCXCM6hiQeEe7dbsKb2gf7_p0IEGRZdoe7-8oqONC9OVXBc-LaQEwRmyOIb9U0EfH1VRDQV_NyEUKrHzDBaXN-JJbXJrMA4XK6wChaB1D4a_grx1gy_mz9PeuWojaBIFho_lXNiWzYnUy1huWrQ7ioxTmcaKOixQrbcSiS_R1qoIP9Kz_CCDwUv05QXx4UUIiNjtMMFl_IY7TnVICFmhpwH5REXWQCAFIWBWpKPF116klkxdUcSugD8CazA1zmNuOFmggRAZkwvCCQBZf15tdG7H5sN1k2F-th836MwG1XFNZn8qEQMUC-QvEe6d82z2SCSNSPq1lAFP0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هکتور بیو ، بازیکن تیم ملی ونزوئلا اعلام کرد که همسرش در زلزله 7.3 ریشتری این کشور هنگام مراقبت از دخترشان کشته شده است
همسر بیو زمانی که ساختمان در حال فرو ریختن بود با در آغوش گرفتن دخترش از ریخته شدن آوار روی او جلوگیری کرد اما خودش کشته شد، ساعتی بعد ماموران آتش‌نشانی فرزند یکساله این بازیکن را در آغوش جسد مادرش زنده پیدا کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96371" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVIFtQmwZ4NsTp2mdAv7OG5uX1hY9MSIZipQzYTRoMvF429da54d2ihO26iD9XIf3L3YAeTYCP54IS2eDYZVt8pgqcLJwgBZasg2ZNdRRvDYVfm7g3Kv76eO13ZwNYOgHGUxBKrprKKBLdjWYx0vk5dEnA7YGx-FWai0qBrHizrdXKAH_ILQUodV1xKd6wIcgKzSL0whU2qsVHcKu5EWGzJXnnLXPH_wPtylXqb-lLur7gpcWPlY49J9uOIJBsWkELmli87vTNE50hz4APsEkPd3fueJdEok71cc89eJaOeNYxhd7amJkJvB_o8zRVUrkVDa5uasMkrJPl8LuA9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
رکورد تاریخی به نام لوکاکو!
🇧🇪
روملو لوکاکو در سن ۳۳ سالگی جوان‌ترین بازیکن در تاریخ فوتبال است که ۹۱ گل برای تیم‌های ملی به ثمر رسانده است
🇧🇪
:
‏
✅
جوان‌تر از علی‌دایی
‏
✅
جوان‌تر از کریستیانو رونالدو
‏
✅
جوان‌تر از لیونل مسی
‏
✅
جوان‌تر از سونیل چتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96370" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96369">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96369" target="_blank">📅 16:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مارچلو بیلسا بعد از حذف اروگوئه از جام جهانی: «خود موسلرا این تصمیم رو گرفت که تعویض بشه. درباره‌ی تعویض والورده هم، راستش دنبال این بودم که با دو تا مهاجم نوک بازی کنیم تا بتونیم موقعیت‌های هجومی بیشتری روی دروازه خلق کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96368" target="_blank">📅 16:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
عشق و عشق‌بازی کف آمریکای شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96367" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇫🇷
شادی دیشب فرانسوی‌ها به سبک وایکینگ‌ها بعد برد پرگل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/96366" target="_blank">📅 15:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
شادی نروژی‌ها در میان سربازان ارتش‌کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/96365" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=Ctn-a6TERYNXoxGLjn5CMRcDYga_uW6TH4iwD01fAGjytsWuKHopppPaLLFa1pjkcWvev890dAFLqOcJgjJVlOnOset3EqW-jrlulYKeJfWzTOJTCaHz9EPFkTO00IJKteSTu7HDt2gcP5qEGHiKE1PfOgfiZ9TPtgxLsxueSGGY1k6-kq4CUVAcY6ZqIAEe-Bw6Rdc-A9grbtwaKsd1Avbv89VhV-ilNhMuOsv0bYEws_7TFNk0ed3bgjwWyS0qJ83DXD8njq6EWhJQ0trVAyCU7wdM8-eC6Fuao6omIscFMlpQoTVYvIajHMEkmuKK3UOLyj08orgJMM1BZesl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=Ctn-a6TERYNXoxGLjn5CMRcDYga_uW6TH4iwD01fAGjytsWuKHopppPaLLFa1pjkcWvev890dAFLqOcJgjJVlOnOset3EqW-jrlulYKeJfWzTOJTCaHz9EPFkTO00IJKteSTu7HDt2gcP5qEGHiKE1PfOgfiZ9TPtgxLsxueSGGY1k6-kq4CUVAcY6ZqIAEe-Bw6Rdc-A9grbtwaKsd1Avbv89VhV-ilNhMuOsv0bYEws_7TFNk0ed3bgjwWyS0qJ83DXD8njq6EWhJQ0trVAyCU7wdM8-eC6Fuao6omIscFMlpQoTVYvIajHMEkmuKK3UOLyj08orgJMM1BZesl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
مارچلو بیلسا سرمربی اروگوئه دیشب بعد بازی با اسپانیا کلش کیری بود سر خبرنگار خالی کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/96364" target="_blank">📅 14:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Sj45t5-IWau7vIEIo0NKL8och4Q5cvcwL8gUFdX_KXBBtnp5G56FGEmMUEWauRPU5Uw02IHTMpc3gBgemAZ86RP3AIyEUMr3gNR92UjsPEZhJkkaEdEViLk9QzuArLsOVkf2jCgMPExodY1rbhNaVi80Gaho7WhOKjuGhNrehV7mcuFdz3WaoKuIWXbVRlH7n53xPN1jp5hJx2ODvXbcTkp8tojxgVaIE7vJtTwbp3Hwqnz_9FV4PsOnqIVYnN8NPb2fOqp0yArDCFHM1XDvklk74_1KXwNLdveiG97RRA6TfQ-pWFl-st2-DGbEG_aZVjQHF99WklazmZaXceNKMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Sj45t5-IWau7vIEIo0NKL8och4Q5cvcwL8gUFdX_KXBBtnp5G56FGEmMUEWauRPU5Uw02IHTMpc3gBgemAZ86RP3AIyEUMr3gNR92UjsPEZhJkkaEdEViLk9QzuArLsOVkf2jCgMPExodY1rbhNaVi80Gaho7WhOKjuGhNrehV7mcuFdz3WaoKuIWXbVRlH7n53xPN1jp5hJx2ODvXbcTkp8tojxgVaIE7vJtTwbp3Hwqnz_9FV4PsOnqIVYnN8NPb2fOqp0yArDCFHM1XDvklk74_1KXwNLdveiG97RRA6TfQ-pWFl-st2-DGbEG_aZVjQHF99WklazmZaXceNKMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو رسانه مطرح مارکا اسپانیا از درگیری میان طرفداران و مخالفان حکومت در سیاتل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96363" target="_blank">📅 14:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=Yb35m2lIaHIWfY7qDHkUTE2uBaXQrmBqa8pAN1RJNh5uwU1eCitlp7ZmyIggKmc2loLFkB_A9PP0YZVn6jMKEC7ZA9bCt3IgZHP2CR7hub5O7Mgi8V7a5dDvLpQ42N5ipGoZB7IxPYIsXcpv71FKoWvr3aDEfIumL-6ZqBdciBV3MzgdiVI74yPWzYREBn6L1jqfboEuYSacGkYlHsRfHcKWXyZNib_vXxnezGIZSUARnWjkdjO3MPeMhtL6FZAq712zNDUuJfIZnamNG4c9sVWAq55OsxZBeHhwKDb0xbMmdolTT2DOU1MavH69J8rP_nJGDFrko80pzb1_q8rn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=Yb35m2lIaHIWfY7qDHkUTE2uBaXQrmBqa8pAN1RJNh5uwU1eCitlp7ZmyIggKmc2loLFkB_A9PP0YZVn6jMKEC7ZA9bCt3IgZHP2CR7hub5O7Mgi8V7a5dDvLpQ42N5ipGoZB7IxPYIsXcpv71FKoWvr3aDEfIumL-6ZqBdciBV3MzgdiVI74yPWzYREBn6L1jqfboEuYSacGkYlHsRfHcKWXyZNib_vXxnezGIZSUARnWjkdjO3MPeMhtL6FZAq712zNDUuJfIZnamNG4c9sVWAq55OsxZBeHhwKDb0xbMmdolTT2DOU1MavH69J8rP_nJGDFrko80pzb1_q8rn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/96362" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSKAcuB1vtF-OBAxoUqav5a5fJglrIig2JNQjwAOEnpUFFHS5e4ZGlgpxKoAvJ6hbDhj_plpz923ItyXjY7HkfziIwqEXIfHUNmD7gU5J4vDTsikFZefHBSLRzrUXZvb8DDEwm-dR-te3KI5L7C2NavEj7BK1oykBviABCazcDfJkAq3T0D_yO8Rr2CJUR6d5nMhBD5HVUN-MiNhRU3mWP11m3OnrZTxyg6v0xLEloFoDqWhTNmK5-BaawCn5_cOMOnqvZJqVyA4TenmtEvdreXdFCsyt-O-BMMA23SiF8SZe_t-3anfzl9XOe85Iv-_k5NLsTdi1sZryaPOv3DeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آژاکس در حال بررسی احتمال جذب تراشتگن به صورت قرضی است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/96361" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=eHyj5RVzGzoxJ_zRtuKWgAf70m7cwfj3sjnWx0QxjEWHWur1vdTqIEIupCqDrPWKqbwyLAEJex0FucVH-CsL8CuJxjqQP18ko8T0OyWrtYT-hm9CL66AFWv3KvEiVK-22BOufmcY0KaF1tX8qIDhe1iT3MndsXdHp363kiJSKvDNkiWabLRmyhNBcKlMqGuudjNgH-CGG7vNM7-_WfcdMdMLsO6yYyelrVixTTDmmaZfRXZwezmmmT5S-ZqpEt83skSUwt53j4litItzAnnuJozdE2dLpfWcOL-IgrRqRpLA3yqF7nkleZ0USM68mFCL2RGz1-cBDUAp94eJN8rK6JaQHWUUbfIL-WOKAdJ7vpGz0aAE-tMBVGxglicDNsz4rVFw-4mId5jlimL5oeOGszpjFnQKUbIw2KYrUmt8oz0gL16XLE2PbsY_evZFOm5BgluNPYniCRcfLQUEJtM_oefD1MGr6qsjBcP3wf9AujvtsfEwVVg0_UpICJfDjU_xYKvwOIwm9iXQjO20bpMO9avzDSxE_6Utpo5v7R6ZDrV8G-BoDVASwmzNloT8zgOtvti-uNip0Ux9COl1MmNCtGBrssDqi2xuncBTfX5tGHL_DwK5TQZmxC5LWfSo7IT0tdmnJuIQGymhloEhmZUNDMNwKNFCpfMb_Nz-JuMBqBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=eHyj5RVzGzoxJ_zRtuKWgAf70m7cwfj3sjnWx0QxjEWHWur1vdTqIEIupCqDrPWKqbwyLAEJex0FucVH-CsL8CuJxjqQP18ko8T0OyWrtYT-hm9CL66AFWv3KvEiVK-22BOufmcY0KaF1tX8qIDhe1iT3MndsXdHp363kiJSKvDNkiWabLRmyhNBcKlMqGuudjNgH-CGG7vNM7-_WfcdMdMLsO6yYyelrVixTTDmmaZfRXZwezmmmT5S-ZqpEt83skSUwt53j4litItzAnnuJozdE2dLpfWcOL-IgrRqRpLA3yqF7nkleZ0USM68mFCL2RGz1-cBDUAp94eJN8rK6JaQHWUUbfIL-WOKAdJ7vpGz0aAE-tMBVGxglicDNsz4rVFw-4mId5jlimL5oeOGszpjFnQKUbIw2KYrUmt8oz0gL16XLE2PbsY_evZFOm5BgluNPYniCRcfLQUEJtM_oefD1MGr6qsjBcP3wf9AujvtsfEwVVg0_UpICJfDjU_xYKvwOIwm9iXQjO20bpMO9avzDSxE_6Utpo5v7R6ZDrV8G-BoDVASwmzNloT8zgOtvti-uNip0Ux9COl1MmNCtGBrssDqi2xuncBTfX5tGHL_DwK5TQZmxC5LWfSo7IT0tdmnJuIQGymhloEhmZUNDMNwKNFCpfMb_Nz-JuMBqBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
🤩
کنایه بازیکنان چادرملو به پرسپولیس: به 2 روز تمرین بردیمشون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/96360" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_9tIUrLbZ26ScW4-i11TKR-MSq3NO8tRj1KzAW9VqGctb9hPB5HKJnVCu9mYfPf6Tj8mc_531PyHl-7irZ1WSG5aXrxeVF5BnE23ApxCzH2C9WGLxznoRpQ5qBF3vNKzjot10tQyWCo7NdeETldzLAfRavSK7X5bykV71k-RP61O79U4pgXdguGFSQFciiRERnGiwOSmuHayAj8y57ZAY2NmFuWtmz7vbn7CDhHrbkN-4mZABaDJSAgk3v_JoHG497lPsu-eV1hORxDJMVLAOl7zMzh0KeJhXv2D32yCRqzem6KVc0zTeuNKZRY05bxPz_Hf8KSYr8wkDslA-S-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه چلسی از لوگوی جدید خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/96359" target="_blank">📅 14:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=UxLEuWTlpJSMhExguOD76fjvZuvUmXeT4P-W5WCfNOFLJ2mKy5j5QfGi7qu53jm9EUsuNGOFv5zcN6GFnDGVBaTyXzCkWDuQe4MNckppcV3MfKk4ZMSvfOKvdIBRgjdBUVxd1tIyDE34eGHTMnX-1KRdWWU62fQVxk5tVSqku7kqp7j-QbkTSr6QnVl6OzxaUf7ZrBGkxDkLgYo-RT93ChiVgQjsG_vP0SR-TFO7y-6GdUokiZiMeLDElCC0hnzAwniA1luP6gg4bQIcMftjq7gAhUSzmhXXHyND2QAdEwqofUs0nKng32oVpfy_l3gNxj77YaWoRBJzScfheDt3TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=UxLEuWTlpJSMhExguOD76fjvZuvUmXeT4P-W5WCfNOFLJ2mKy5j5QfGi7qu53jm9EUsuNGOFv5zcN6GFnDGVBaTyXzCkWDuQe4MNckppcV3MfKk4ZMSvfOKvdIBRgjdBUVxd1tIyDE34eGHTMnX-1KRdWWU62fQVxk5tVSqku7kqp7j-QbkTSr6QnVl6OzxaUf7ZrBGkxDkLgYo-RT93ChiVgQjsG_vP0SR-TFO7y-6GdUokiZiMeLDElCC0hnzAwniA1luP6gg4bQIcMftjq7gAhUSzmhXXHyND2QAdEwqofUs0nKng32oVpfy_l3gNxj77YaWoRBJzScfheDt3TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌈
مهدی طارمی:
همجنسگراها نظر خودشونو دارن و قابل احترامن و ما به همه این عزیزان احترام میذاریم چون این موضوع به ما ربطی نداره.
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96358" target="_blank">📅 14:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTCJKsoShxqQK80Ic6HxXew9wuMwSi-N0SZ5gIPnZILNwIXTILfUUTl_82Pjdkq1HXX_e4IyOu6KMR-jHrG_yYrj7Yw5D94mWv6aX4VvTrn3Yj6LeYnLQ2rI9OYvU06lrFO6ArHhFOZLfURs3In2xmrjePrxkKvq5cfFGiJL-rRkLGN0MjKrQ2kGgZrPusVVtM9X_S_49ojy4jX0ldWum5cXQvytIP5xjvcRTLgdTEHUbBJXxuBSTHB-30GULhEjPtcfkY4ha73KOqcmVs76Ce7FvoM8-3zLRGEmDvqn-bNUtsXAd4R7HBzvrr95NTcF_duVM80dwWxYkQdBYSnnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇳🇴
در میانه بازی نروژ و فرانسه، یک زوج نروژی در جایگاه‌ها نامزدی خود را جشن گرفتند و شبی در جام جهانی را به خاطره‌ای مادام‌العمر تبدیل کردند.
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96357" target="_blank">📅 13:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=KFFAowRinnsxLHi3Ls-6KJuVLbM_xLDYgfzc706QOurKZUsrUZZjsfgFpwP1AnEwzRz6vxCJFPzcw22rfSqpfVM598RpqMPLwYF801QZoDixxEWDnxhfalcZPhkj2Ee6YHvbaM_QFh9oGMX1-7B9qFxVn6yxOzH0pDNbKqLHKrxM4Q4THyd9rLngs1-0_eq29pO_A50Cy1wCrO_rTir1bwGhL1W7DtY_9I25pT0bw04TI295h1Fy10iG2iqwNDJs8ngHskGOoEhlbJddlqqGIoTXCXUmT9f5lwPRvGz9bAzwM4EeZzxEeVeX6-aGFT7vvw3N9gMwwRKPMO5VBWkmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=KFFAowRinnsxLHi3Ls-6KJuVLbM_xLDYgfzc706QOurKZUsrUZZjsfgFpwP1AnEwzRz6vxCJFPzcw22rfSqpfVM598RpqMPLwYF801QZoDixxEWDnxhfalcZPhkj2Ee6YHvbaM_QFh9oGMX1-7B9qFxVn6yxOzH0pDNbKqLHKrxM4Q4THyd9rLngs1-0_eq29pO_A50Cy1wCrO_rTir1bwGhL1W7DtY_9I25pT0bw04TI295h1Fy10iG2iqwNDJs8ngHskGOoEhlbJddlqqGIoTXCXUmT9f5lwPRvGz9bAzwM4EeZzxEeVeX6-aGFT7vvw3N9gMwwRKPMO5VBWkmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شجاع هم حسابی سوژه مصری‌ها شده‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/96356" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=YmuaHHsxGf3LGDm97iRBCR2JTvyA-lvlA83GbjbNASCszIXjpi1qHC85ctLAvEPDIXbUFiNcKEdPRbc_HOaBByC4R4LNmgDXL0CAVnUSuRj4bG5dJ5cZRy3qE9yDj6kRFrti3JAO9ESu7ib-Mpc76FxTaeDtVAQ2vwv9_am-5d3s5btuKhzcZtSb4rE-0PsFLpTA0IVI7e6FezfAv-KNKzjb-JIo9gSRkJFnkKKQ3TphVx0S0AtcRwfnOdpnwNDnnHmf_Z_j5nzgfllnpM7C9sNVFDeW-4uNvWkm-MY1j43eRc8ZzIGKd9eFlr2BDk7onxnlrSPFU2ErJtgwK5At7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=YmuaHHsxGf3LGDm97iRBCR2JTvyA-lvlA83GbjbNASCszIXjpi1qHC85ctLAvEPDIXbUFiNcKEdPRbc_HOaBByC4R4LNmgDXL0CAVnUSuRj4bG5dJ5cZRy3qE9yDj6kRFrti3JAO9ESu7ib-Mpc76FxTaeDtVAQ2vwv9_am-5d3s5btuKhzcZtSb4rE-0PsFLpTA0IVI7e6FezfAv-KNKzjb-JIo9gSRkJFnkKKQ3TphVx0S0AtcRwfnOdpnwNDnnHmf_Z_j5nzgfllnpM7C9sNVFDeW-4uNvWkm-MY1j43eRc8ZzIGKd9eFlr2BDk7onxnlrSPFU2ErJtgwK5At7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
زلاتان هم از شادی وایکینگ‌ها بی‌نصیب نماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/96355" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSolZuYHqBbXpcGPor4zmAYTv_naZvihhH495DNlQnO81ysR3rao-NcXiK0WVow48Ciiaukssg-1Srm7CR6dv0peydFQptOZDrLv2s-bkUmKMb_5ZSsFC61gmBy6So_nad7VlFH6Vvuk0oFtxlbJABXR4sA31vwE3I9rlfvww30VLmA1rJF_ZpEzSCLxW5F84-IYwiuGXOavpLM_6LS1IcXgjEa-1KVt3ci0NxRdjsRmVOhMDEp98-AaHT6E0dtASn76WAnkpqpHYFCWPVQZaK6fv3s2zOGnUrs2xhte09TyQg9NOWrzuhIJFUz2xtm-SkRlHfh11Y7VlPJGeYOKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین تفاضل گل‌ها در بین تیم‌هایی که ۳ بازی در جام جهانی ۲۰۲۶ انجام داده‌اند:
🇫🇷
فرانسه — +۸
🇧🇷
برزیل — +۶
🇩🇪
آلمان — +۶
🇲🇽
مکزیک — +۶
🇳🇱
هلند — +۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96354" target="_blank">📅 13:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=obHtSdYROtgfG7Fd3RVleqExfK2mi7KRvgiTVeCZu2VVbJcLubPDo5fZpsU86pQbsAigh515JbQ7jwXFdkA-dKZudXe0UDo3b27pH8UUOdnEZ0fEfeUV77H4xGiKyoPk6wcTKUvqzBvKgfPcEfIDnyOTdm-A6LNqSz66j_s130mhJcBcAygk8R0wvhUoKHNalPkUg4wdjrjngpNfIomN1wMaBfS9skNU74mgvMF67Cmddvg_A78mMw_UQobqgqH4WOeGkR-qBN_4QmfrTDhetjPKF5-jiCWPsJomSiWhcr7FtsvTE_JhFOZl7vzxznme7A3i24Mv-u3_m_ihSgg7pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=obHtSdYROtgfG7Fd3RVleqExfK2mi7KRvgiTVeCZu2VVbJcLubPDo5fZpsU86pQbsAigh515JbQ7jwXFdkA-dKZudXe0UDo3b27pH8UUOdnEZ0fEfeUV77H4xGiKyoPk6wcTKUvqzBvKgfPcEfIDnyOTdm-A6LNqSz66j_s130mhJcBcAygk8R0wvhUoKHNalPkUg4wdjrjngpNfIomN1wMaBfS9skNU74mgvMF67Cmddvg_A78mMw_UQobqgqH4WOeGkR-qBN_4QmfrTDhetjPKF5-jiCWPsJomSiWhcr7FtsvTE_JhFOZl7vzxznme7A3i24Mv-u3_m_ihSgg7pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
دیکتاتور امباپه تو بازی دیشب هم نشون داد که چرا بهش این لقب رو دادن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96353" target="_blank">📅 12:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=WJXM3neG3osnmwj6_U_OhUXOvSxOZnePtPD2N7Evi91yeIR4GzjJSYpPmssDVzCffR2ok4uiUIqjGkLjCOL1tCe3Lr3uXk9lB_8iWkVRtPOXV-YAZDHuWgEK7-mHx6SSGgZd2V_r7Mr_9Rt40XSUtxWGKOpPE4C1wVqW4xBDU_K12lmql6z34KUm0xXIJYuqD3ZAihUM-B7eAXMqSf_adgQhyGb2TRg-_hiDkHsyC-gAtjysM6pYcSltmxZf2JAZoms1GTdkabxZrHw6szNTaQx5AOtM9jRuQV8hwPaCwwl5YsdpB6UteaXCRztoyuK2oBRA4KZmJ3xQPtNrjKgLn187V4FaA8dOxcnt6s5VEHOLh3aSqxt5063VXZ80bYOCl1Vqnfqa_iV9G3wD_oLR74R-VbYOqiqc633cjKLiw3teipaJBV3IFbMAb1HkMiMHKT89UxqgXeYZs7k1d58v9ns4X6PHkqSosusLXNIFMmfTfLZF04YVol62UlFPJM3Hg4_jXnZpAo46yVCuhDOBDqCtfbdGW3ZbUQgeefrcumXLfYXjwB0y9KS2DW00QbxmvwX3L_Tljm2Yy57Y8HmweLHSkQ0rHPWJ3vhM5N1OZmVNTnlxdwGvB65ij6lFA_yHuzmWuRrZI2NXEe5C7GN_7Jl9kKNYwEV02Zxf1npKlM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=WJXM3neG3osnmwj6_U_OhUXOvSxOZnePtPD2N7Evi91yeIR4GzjJSYpPmssDVzCffR2ok4uiUIqjGkLjCOL1tCe3Lr3uXk9lB_8iWkVRtPOXV-YAZDHuWgEK7-mHx6SSGgZd2V_r7Mr_9Rt40XSUtxWGKOpPE4C1wVqW4xBDU_K12lmql6z34KUm0xXIJYuqD3ZAihUM-B7eAXMqSf_adgQhyGb2TRg-_hiDkHsyC-gAtjysM6pYcSltmxZf2JAZoms1GTdkabxZrHw6szNTaQx5AOtM9jRuQV8hwPaCwwl5YsdpB6UteaXCRztoyuK2oBRA4KZmJ3xQPtNrjKgLn187V4FaA8dOxcnt6s5VEHOLh3aSqxt5063VXZ80bYOCl1Vqnfqa_iV9G3wD_oLR74R-VbYOqiqc633cjKLiw3teipaJBV3IFbMAb1HkMiMHKT89UxqgXeYZs7k1d58v9ns4X6PHkqSosusLXNIFMmfTfLZF04YVol62UlFPJM3Hg4_jXnZpAo46yVCuhDOBDqCtfbdGW3ZbUQgeefrcumXLfYXjwB0y9KS2DW00QbxmvwX3L_Tljm2Yy57Y8HmweLHSkQ0rHPWJ3vhM5N1OZmVNTnlxdwGvB65ij6lFA_yHuzmWuRrZI2NXEe5C7GN_7Jl9kKNYwEV02Zxf1npKlM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
تفریحات تماشاگران جام‌جهانی در محل بازیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/96352" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K602dxy0jC_FW9xJw72p_PZUngFt_CRRrE-iGWq53jzahRP9G822Ssc5AwCdEIYDas0ilOHfJOxK47LdEjtqqX8cI8PpuStoz0C8ghJRdQnA0-ck8JnKR46wwmE_MlNEaFTuSvXNjEYOvTnBM9KmNoEN6kJmBKKsEsFKI2JTREh0fMHMlILYI3i-J0nNC8q4xUe8_LRqMUE4eIG-xDFwQbuh7rFxpNDCw8OeIHmYgtl-Q_gnJHWz79d6XYJSxSdm7-aqn1-10KgQEAb7eRgqa5b7Zc3L12NyfeeQdwPfQ3lOHuAj-77Trnxa471MUlsCv4HkMWWYwbiuwFOgOBZptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در چنین روزی در سال ۲۰۰۹؛ رئال مادرید قرارداد خود را با کریستیانو رونالدو پرتغالی ۲۴ ساله به مبلغ ۹۴ میلیون یورو اعلام کرد.
🇵🇹
🇪🇸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96351" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=C0mhGys1ZDKbEfQ4EGhEFRr46gj1MCwJtHtaDTOUMLlU32-gDS-5qVPb0vydYyvPwWW6gxiVNOqRaFMeaQqVnCLUFp9DcAkTRqOrbx1LU6WSgNYU4o3WAlVRigTNFXIZybIW-c9dt5WM7gXEEHQsXdByfiO5rUFOQVl0yEE-d7klx7ZyvI9aMGSVMFeZLBHyaEUfgpzcX3dRPFtbRYIuNBIjRvOQkf0PPKRXUR8ndmP49o8FcYPh5mPMhc825PFApV_bDhgX5QlT0iMN0oiJCIbUmFE7_KmVppkqa7cFeJLiM1XXFBWIfRf_dY9yw9Z8NHPGePgYAygyfRjcRD95QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=C0mhGys1ZDKbEfQ4EGhEFRr46gj1MCwJtHtaDTOUMLlU32-gDS-5qVPb0vydYyvPwWW6gxiVNOqRaFMeaQqVnCLUFp9DcAkTRqOrbx1LU6WSgNYU4o3WAlVRigTNFXIZybIW-c9dt5WM7gXEEHQsXdByfiO5rUFOQVl0yEE-d7klx7ZyvI9aMGSVMFeZLBHyaEUfgpzcX3dRPFtbRYIuNBIjRvOQkf0PPKRXUR8ndmP49o8FcYPh5mPMhc825PFApV_bDhgX5QlT0iMN0oiJCIbUmFE7_KmVppkqa7cFeJLiM1XXFBWIfRf_dY9yw9Z8NHPGePgYAygyfRjcRD95QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های جالب و تکان‌دهنده تبریزی خطاب به بازیکنان جوان
: گوشی رو بگذارید کنار، عشق و حال زمانی کنید که جایگاه خودتان در فوتبال را محکم کرده باشید! بازیکن ۱۷-۱۸ ساله نباید مشروب بخورد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96350" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GagyW9xlIgLm3kw9rv56L-j10WKEelgynjKfQ4CReGV4iSnk44fuLQsqgNqR9MISEVaucm9C-WbSg4Sbo_q4ya1XNB8jzTdywrs8lz2FB-GzLI4zTF_iGWcxWncsKWVmif5wGvjCTm3l-9jyehoz1BEkZMpOZTiYo9UaObuKE8Yyx3fdj49wIEqYc4y6EAAiej2x3LxMZHeffv6HwLvR2a1KskZzXn1OdY2RsZ0cZ5WtJVQpE3R8GgI8P3wprtm5QlG4K9eJ-KmpK9SQbGgZTaBepdr9yBgGbhPKWBrY6o6uFyFuqIPUVt__VLsybYB5i36_1Hp5YQwRDRXzoSm9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96349" target="_blank">📅 12:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=RXjrLMa8LIsaqb_yGvsdwCRmfit_WsWV9TqcqGHD1-ZtQSTDws4lJIzNKvE942I5z6fyhDEUGGkz0cNMLJGFULnNcefUt0g2mhibiEr080MEu3jBnhX0BU7rBiSwb8hHklBA-iVOMvStxA4lyGs3mFudjFqN6dR1Dpb6NtjlqMHrMzbt-bDcsxHEpu4r0lrCija9YVTM8yiU5Y3rNUwkFwXVV2IG46QPUG-EF_mvE20UWZeknQNsTLYrYMnMEfEj0rqC6ShjNj6jeZjTiGNPpGgI98YIaCjQms4H6v8G_NxDQhXEDB1sAxKJGt7zFIN-F5w6dQ0Y0Tt-gPgLQbLrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=RXjrLMa8LIsaqb_yGvsdwCRmfit_WsWV9TqcqGHD1-ZtQSTDws4lJIzNKvE942I5z6fyhDEUGGkz0cNMLJGFULnNcefUt0g2mhibiEr080MEu3jBnhX0BU7rBiSwb8hHklBA-iVOMvStxA4lyGs3mFudjFqN6dR1Dpb6NtjlqMHrMzbt-bDcsxHEpu4r0lrCija9YVTM8yiU5Y3rNUwkFwXVV2IG46QPUG-EF_mvE20UWZeknQNsTLYrYMnMEfEj0rqC6ShjNj6jeZjTiGNPpGgI98YIaCjQms4H6v8G_NxDQhXEDB1sAxKJGt7zFIN-F5w6dQ0Y0Tt-gPgLQbLrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
اثر جدید حمید سحری از درخشش دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/96348" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFV2H7_4VG1ntMtWS9Ji-50ed_zD8GHC6HVHglxCCReasRSSK0NNZuvPz-fMaUPu0zAdtz6BFOmxhrb7EPt1KHsi9BFLlwqCJmoYUE_9e7hUgmKSWSPf4ImtM8_cYdVjJ45fw8BMtEwJ3rRUZuF9LVWinyQ7Z7pJmwee1Z75LGoBw0BsTp_2oIk2qhgyfuv2ye0fOr0Xutxv9BtMXPlabk2MUNaZjBLEHdTj8UablO6Jm69X-oaxmaR9CJ-STLI40gkEvgxWIG0qnF5nzhOm-shHfDx5ogGJrdh6QeODxMcwBVo_Ox755qxDJ4nc6FB4Xs1J2ggwSIkUCe0xLcBs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
آرزوی هوادار بانوی برزیلی
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96347" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=CdFt0M57BPobtOm4MaP0zsZxpGKZzbzpUuHLC68VmhUFLYMqbq4jfTmbOzIMMEjd37bRsPf3g5TWX7zZd7CWxd8qRp-p4iG-bdRhr3cRAKOaIsO9hxB-wCTE_TrdsSLZ6jbJrjuXHP591dOz41QIbuQjYKvX2bcOD2mseUHGhI2GWfPSw1DXRAG7UTXc5iyHOcKO9D2LDA5tafcs6YFKcyll7429Jy6T0h2lchilU1lirfAjNvI50WqtP1gXLV6gc1BuZ3xmsq4kQIoUJdfd-4QatfVFgLFK1raBQRXZtBrJud2kWW0rWqVv5luQ2_0-TXqJxeZlmhrPVppT7TI7Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=CdFt0M57BPobtOm4MaP0zsZxpGKZzbzpUuHLC68VmhUFLYMqbq4jfTmbOzIMMEjd37bRsPf3g5TWX7zZd7CWxd8qRp-p4iG-bdRhr3cRAKOaIsO9hxB-wCTE_TrdsSLZ6jbJrjuXHP591dOz41QIbuQjYKvX2bcOD2mseUHGhI2GWfPSw1DXRAG7UTXc5iyHOcKO9D2LDA5tafcs6YFKcyll7429Jy6T0h2lchilU1lirfAjNvI50WqtP1gXLV6gc1BuZ3xmsq4kQIoUJdfd-4QatfVFgLFK1raBQRXZtBrJud2kWW0rWqVv5luQ2_0-TXqJxeZlmhrPVppT7TI7Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
از هواداران جذاب و پرفکت رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/96346" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_2t1ie5NYoajgcZxUmESFiDurGG7KI2XTm1WZKyUdSHMmW0e3vw609n0U-0PKxLBF_KtTIchjHjs7CReIB2D6CthAvc-GuI03eyaEd1ONB-bO377k8XtqBH0NqKx6-yRwQkIC3llGMejASNw9cuFpw0H7qSTeCcfN8q5ucuwvXGvXXVOIVkCClKMZCCiYo-Pg7RrtmGMSWm7NwYwu9AC4Xb_gMBygmsXf2fD7m0Lj4A5UktNb_dsgzguCS06T6BGbK-k5oT0MiW7-YlKkaOJXT1OwoG1DXwQr1E-isfdvVySiwpYKglzfM91xI6c1wrYEfwmHgkkjUIzmTFzx5fwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ مارکا: نیکو ویلیامز ستاره تیم‌ملی اسپانیا بدلیل مصدومیت از ادامه جام‌جهانی بازماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/96345" target="_blank">📅 11:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm7aSiPE9SkTn3rIMw4jkpOxsI-AJzo97RmgpbK6sXvzChOOiR5xypC22Is_MwHr63Avt74OO6txSYbgpAAiZQXmZajATwHTSBh6rS7omZuh-3446eJmHOLeSoB7rSdau8W_yc5weD-OAmK13e6_nzzRM4qufMd-RK7sww8mRTU-zdKNzipZIaPNjeBlt714LeB4_IDfzbCt048Bfb__maN1zF3if9xW9TE9sESZ3X16dQch1bP-oxIVxh10_kOQGam9RqAzOY4HQr3WZGYTW5Gj4UzDJStp2VxYf2-EMHxZak4s2JembzAmYz6HNm4XcRdtKsojfAwuWJKGPXCGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
کیت‌دوم پاری‌سن‌ژرمن در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/96344" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=fP94OFpoSkSDM5r136aTiotrcryj9Le8JPx3QhOXNx6RRHIk4X1qdOBknLOO_fp26Ny0Ve-aCvFjcIWpOuPXYnSPLw-LhIK418jbtfJXFboxRwtg2f41NunSZ9bqSThfLExeAD77CG6lCoJzVNZjvtkkeKRZZ9pWklC8GiIh1zqmyOTtHKtTp-ku4Pi_9JLc84qAruH4fgiC2XKnFhF9194mPosk16gFdUxULLiVYOrNZCcMB52RXQ6H6ZJlHqG10gRDwLa_tDRGa0wLQ58fuAzxCCs6x2ZdoLzA6xh4nC9PAKOiskaTqTjapWPB_YMwYYAHtT5NICpR7esQw4y-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=fP94OFpoSkSDM5r136aTiotrcryj9Le8JPx3QhOXNx6RRHIk4X1qdOBknLOO_fp26Ny0Ve-aCvFjcIWpOuPXYnSPLw-LhIK418jbtfJXFboxRwtg2f41NunSZ9bqSThfLExeAD77CG6lCoJzVNZjvtkkeKRZZ9pWklC8GiIh1zqmyOTtHKtTp-ku4Pi_9JLc84qAruH4fgiC2XKnFhF9194mPosk16gFdUxULLiVYOrNZCcMB52RXQ6H6ZJlHqG10gRDwLa_tDRGa0wLQ58fuAzxCCs6x2ZdoLzA6xh4nC9PAKOiskaTqTjapWPB_YMwYYAHtT5NICpR7esQw4y-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤣
تو برنامه پخش زنده ورزش سه پژمان راهبر به خیابانی میگه انقدر از قلعه نویی انتقاد نکن، خیابانی هم کلا برنامه رو ترک میکنه و میگه از یه جای دیگه بهت زنگ زدن پرت کردن:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/Futball180TV/96343" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86220511a3.mp4?token=sG0dhPvWuyXSllNxz0uYXExkI71HFxtpU-5Lrp_upqCMFpFbsaJxP3Z4g67yhml0LNz8fgq9d25PY6MbnG5XXP-0PCF0izeATRETykhXedLrpwpNNXJC2fk51GSd8PRl6MBi24lv41MksEWuM9xXjz6Bk52JGEl3fnMVsrN4CwVIwvOeXICOZeyB_q0ZWluDhAwVLlYKIN5ff88bnPWXo5qtM54SDWG6q2u7QpwPrfGv3-jc2Uzwtl0miFKE8--xOhNworx1cwRaRvl1EjLjKWb967vN4Cvijs0-iakWtLv_PbjwIMXqjCCDiDOgrwdvB5naNGgwx9WDb16CAthgDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86220511a3.mp4?token=sG0dhPvWuyXSllNxz0uYXExkI71HFxtpU-5Lrp_upqCMFpFbsaJxP3Z4g67yhml0LNz8fgq9d25PY6MbnG5XXP-0PCF0izeATRETykhXedLrpwpNNXJC2fk51GSd8PRl6MBi24lv41MksEWuM9xXjz6Bk52JGEl3fnMVsrN4CwVIwvOeXICOZeyB_q0ZWluDhAwVLlYKIN5ff88bnPWXo5qtM54SDWG6q2u7QpwPrfGv3-jc2Uzwtl0miFKE8--xOhNworx1cwRaRvl1EjLjKWb967vN4Cvijs0-iakWtLv_PbjwIMXqjCCDiDOgrwdvB5naNGgwx9WDb16CAthgDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
آقای‌هری‌کین امشب لاشی بازیو بذار کنار تا این طرفدارت ناراحت نشه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/96342" target="_blank">📅 10:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=mJ-1aZtKyIyOtwbwxQ41w-iIIevKh0DmxC63_4iOqdHgIDgKc99IcwZ19ztb9xr-o8TSNtC98pn7IyqBTmj6on12zHEUnmArvOlHInPCsj4kWHc2NAu5s4ws8pzP3_vVCBKaLyEp_bweRIfY1CNye67vxEEaIzMJrXVn_HeRYchnWrsTKNv-hvboT3PPGd9jQHpD7qWHRDTuk2qS97RdRdrHa9zifBTC6JK75J-d87dTW9UHKfYYwXjKSPDeYOgF1HhsEQBa12G9YtIYo9LpAvPt592Ezfhpcb_UgH7Xza6j04H93IUvRLlA8jhGdSZnrNlP5Si8zpohKmmxaJubEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=mJ-1aZtKyIyOtwbwxQ41w-iIIevKh0DmxC63_4iOqdHgIDgKc99IcwZ19ztb9xr-o8TSNtC98pn7IyqBTmj6on12zHEUnmArvOlHInPCsj4kWHc2NAu5s4ws8pzP3_vVCBKaLyEp_bweRIfY1CNye67vxEEaIzMJrXVn_HeRYchnWrsTKNv-hvboT3PPGd9jQHpD7qWHRDTuk2qS97RdRdrHa9zifBTC6JK75J-d87dTW9UHKfYYwXjKSPDeYOgF1HhsEQBa12G9YtIYo9LpAvPt592Ezfhpcb_UgH7Xza6j04H93IUvRLlA8jhGdSZnrNlP5Si8zpohKmmxaJubEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
وضعیت قلعه‌نویی بعد تساوی با مصر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/Futball180TV/96341" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpIx_S6Lq9r0rplowfrMngHHXemdkigLDINZkefrjEOYHFwPc-_2EoyAJNcMq99XykKl9cZvTk7mrkSfvA0GT7aqgkrLFr9HLWFa7v8_mfnDG4pk1PsIkV4LMSktjj8kkAkVaZwidPxzKyYjz0hBJCS6GI_rnOipYO2KQXvYrK3h1IYqPG_YiWkYSfjNbwJKu1u8xqoMO2uoR__3bKnAweaDwIWBB5e3yysBFiSZIMgtBKf-4qcQn63TxIN9bx4Fg0q_i4FQRWQXSIXkoKZfUUUjums6dEpip3RAUV6y89GW1ygmLAukz2AGzgpst416ID_dN5V4iVd3FRFKcRyng7Vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpIx_S6Lq9r0rplowfrMngHHXemdkigLDINZkefrjEOYHFwPc-_2EoyAJNcMq99XykKl9cZvTk7mrkSfvA0GT7aqgkrLFr9HLWFa7v8_mfnDG4pk1PsIkV4LMSktjj8kkAkVaZwidPxzKyYjz0hBJCS6GI_rnOipYO2KQXvYrK3h1IYqPG_YiWkYSfjNbwJKu1u8xqoMO2uoR__3bKnAweaDwIWBB5e3yysBFiSZIMgtBKf-4qcQn63TxIN9bx4Fg0q_i4FQRWQXSIXkoKZfUUUjums6dEpip3RAUV6y89GW1ygmLAukz2AGzgpst416ID_dN5V4iVd3FRFKcRyng7Vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
این یارو هم از شدت خوشحالی سر گل دوم و مردود ایران نزدیک بود جررررر بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/96340" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🎙
میثاقی: اگر بازی در لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات پیشرفته var نداریم الان گلمون آفساید نبود و برده بودیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/Futball180TV/96339" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=dRxyZk05GK3ZQ7KmfUts6ksmyF-tFpEuBOtIMjXBQHmlz4k8tlShTSHvj5mbVdfXVX9V2sCWJtrxVsNpw55mG-RXfaKOWVCMh99NEAMGxM4gPkcCVcKysrLgggUoit1NYH63nCci8NgH1u5eKp__NWGAaEMpi5L28llPbwCAdPpdEjBh6ihCN-sIVCj6K9xp-5LrwwgkZXCmgmQTvUgrXdP0mQSJn_RwUHKjbdy7VYHz_afs3F1qF2_kdzBwC2teS0rWFTdDDjTh5_5cWV3BkxMgqR-aDEm5GAYfZHgEfuG_9FU0ftw_JMV4X6Hj3tICRWawi3yig7i3gA6Ft1AjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=dRxyZk05GK3ZQ7KmfUts6ksmyF-tFpEuBOtIMjXBQHmlz4k8tlShTSHvj5mbVdfXVX9V2sCWJtrxVsNpw55mG-RXfaKOWVCMh99NEAMGxM4gPkcCVcKysrLgggUoit1NYH63nCci8NgH1u5eKp__NWGAaEMpi5L28llPbwCAdPpdEjBh6ihCN-sIVCj6K9xp-5LrwwgkZXCmgmQTvUgrXdP0mQSJn_RwUHKjbdy7VYHz_afs3F1qF2_kdzBwC2teS0rWFTdDDjTh5_5cWV3BkxMgqR-aDEm5GAYfZHgEfuG_9FU0ftw_JMV4X6Hj3tICRWawi3yig7i3gA6Ft1AjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی وسط سیاتل تریاک ناب گیرت میاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/Futball180TV/96338" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRW8-6nScL2CwN2I7qLS5g95upXpVD6ufLD0mXo7fXj8tx9dKT96n-X1Mnc3Zcg20URQUdsmsULrGmfSepPF0a3w1Kz7QGTEF3W1fiPNRHDXKTtQy9excW2gw5YRkSZpsk1r8nUZuCclqkXUbqpAv0U9YJdeiQoWpAgJe5zkjDn9dfl-8qseLJw-gu1RRpyHmo9-ELXl-EMu8gtkNtMoR1MWv862H9Tx0kTqx4KPq6lh5xSHjbtfX5QgKdRGauvpMJ0siIS3iJ33J8h8a2xf8EeSpeUIfeqdwswLSHOc8RJ7SppG2LWR1drWQJnl_NUsV6eO5ilih5_5mizLx51eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق var بازی ایران و مصر
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/Futball180TV/96337" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNDUMFcfQg9jM-B_Adjsq1rO043NqCsgXKHutY4soSkASKaZSwxENyU7lg-MrYszOmRmNXr53ORkB0UoTnoNH6-80euQMYNpcNGt4juDrJT8nJD4d1PLcjvEjlRBEbA8uXWO2BSPwt2eZEzMkY9ArWMp0RkIcDQLNBJfOOjb0xZwEE1lQy2YYTbuAbPsiyBeBfeOh9CWFTS9iQujmfl_SmpaOVy72SctbinAD8lVtO2SGRR8OY4hwFscj-wHEqHn4zzKbRm9TWdFY1ApdNIsEgRzxHoesr0aPLPZfcCgsra7Rbt7BOqcjjaMDnaHMiyw0uBOkCFhs4NetSdSlBb98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
🤣
تفاوت‌سطح از این عکس مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/Futball180TV/96336" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=iqR0cop71WldLzsRL7LoYAGAmskWpWPodr2Qyscmze6gThLp6zfYuZP2nEm-i2FOJGUBA4Ip1Zgi-NS51KeV-iY7v_2Rg0hOS3ckVoJuMC_cAF_inR1LZSXMjeOGbkQcU20an2RlFusGtuoC3Tt7neHAVIclWWiU9ncctpyMMGUVHpEwrciMeWC3Te1Dc_oeYH1klugDou2L-e8LwN96W8yvaAmXzO2cxBaDt3mGMdiZX5915USfuNguiGsUYVon7qE9A14806z-4OLwXXejVF_g3rVVqswg-TMyJPDZMexZVhKGe2lvoy8-dlZGjmqVeOPrpn4wJ4d94aIobdnaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=iqR0cop71WldLzsRL7LoYAGAmskWpWPodr2Qyscmze6gThLp6zfYuZP2nEm-i2FOJGUBA4Ip1Zgi-NS51KeV-iY7v_2Rg0hOS3ckVoJuMC_cAF_inR1LZSXMjeOGbkQcU20an2RlFusGtuoC3Tt7neHAVIclWWiU9ncctpyMMGUVHpEwrciMeWC3Te1Dc_oeYH1klugDou2L-e8LwN96W8yvaAmXzO2cxBaDt3mGMdiZX5915USfuNguiGsUYVon7qE9A14806z-4OLwXXejVF_g3rVVqswg-TMyJPDZMexZVhKGe2lvoy8-dlZGjmqVeOPrpn4wJ4d94aIobdnaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی:
شاید خدا داره منو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/Futball180TV/96335" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQy78b-nnDarAjtMEEbRheJhuqq-jpyIyhlflvgtC4LcJSW2pf_QJjTh7wDNWRD2eCP0-89IhArilL1O40vTSJCdcKn8le2_63HdEntL8UrY6e2TKRJwDbvEPq16-EtRJyrfAmqC5pbOry1uIjr7sZJa3TX28Oxh_3L1SWYXc8KUzfn3K6ysSG9rlNeA0GAz4f2nt_MoqScZn1gooCku52-xqvqSpg20WoWunLaaFZB9-UJGPjJEXoqoMjFLhBAB9c-94dNATjkOesCBz8A5yqKQ6TqgXFAXvbK60OJzz0utOhL0SYPHZSMChRZB7-FGz7rdvj2C-zA1D00Y2_wThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/Futball180TV/96334" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlCn9o3cRsYT_Z_Ke3c2m_f8fDVmpTW83D0muwLGX4rS_LnTOcmUZ5gPJRlW-WLfLkr7eKwxCRIIYAL86IkNV5xhO67RuLuHyQMDrI7wNuOhKq6HFbDHKyZOgHlLDuOCbGqCyE-twqWB_ctme8KB42iiO0q1OfVroL7BF0vejmnVjwPNlXRJ2v3SMfLg_QuaGzOvJuIJVWK2pcuqcmqodNLeRSTuZ1YOfeI1DKyytQQ_2YORPeNJ_0zcH-XmH9WslmeuhvOJ5iqZP8GDmfKhgN4NljG7kzv0hgge_lyk76o5j39OKb_a75JJ1VGrNWkRMno_q82PakFJBHQG53m4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/Futball180TV/96333" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6j-w_B3LAFnXbQMsjIfTJ1b99MYHMcQcNiVZ3uw4LmsuezZtk6aftcxZEIPQw9BUVuxbyjjf9lScydInfg1Gm1kWTQ2BbEJgkdpvL7oA1rfyw4KTvz2n768U0cHlMAyHlmSicN99jqhNP4OzhvTZSsJuG5CRoItjsQvBdb3K4cFq9MpncQ5P1UxJgjmipvXol6Zc6x2CqrpCOe4GqqCcl7NDtscN4TfLnhCrYu2cebaEIK5P_4d5lG7AqwfLJZDZAfCl9tMhpkJNHV6__UTcif1MeSUNMyxeNGXuYy-pR2HHjsPJCtQ3utJJ3JeOKHuJO2l4JeYiixs9dlc3-r2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خلاصه ی بازی واسه کسایی که خوابیدن ندیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/Futball180TV/96332" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R95TO8t-DUm6yVZBaXqi9oFWWEzo6TXt6VDkL0-vQgmbFji75tZmtWP5xwFFGfIFV5QzMpoGN0X0ZICK0qF9HhsWv2iOXor4rCAN6ID269t5R-298-bMejIjQ-nLoEKB7SqoNLC5YKdkSW6e2uAREfKWZFCQl_fWUzzxnKfzZcMqjdv4Tm3RLfhxcLCIlnTg8WT5FH2CfoZf8FOJEhVMhFBizY8q-bG6WIH8pf2hgObPSJAS4Hj843LJThXYeND0gOYO9jNqd_wwF3rkrN5Hp7aOcnKPE4YzudtWxUBADR_-YuTn7sN79M6U3T466d9BE_t9JA7enXTv0MkTdQtLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سه‌بازی حساس برای منتخب ایران:
🇬🇭
غنا - کرواسی
🇭🇷
ساعت 00:30 بامداد
🇺🇿
ازبکستان-کنگو
🇨🇩
ساعت 03:30 بامداد
🇩🇿
الجزایر-اتریش
🇦🇹
ساعت 05:30 صبح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/Futball180TV/96331" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TupPZ2ASnH7anDpqAUYgo7TV6iuvIdn4fDC7ArGDdLMuwDOmojXTXtNi6k7L9tar0L-NEoE4OehEPoPrEFxOHD7JenwM1Ye8nKw4Kft63cFK6EZgoolBkl6mbSbO3IdFBV41wpDuTxUfH1xXXngpXwvSx7EoL-cIOcbv20UUucOBrGuBHEsONIvAAUc2AP79gxv_ajZzKl7AGV7O4GnynQ-4Ay2bOzlSDaVshQanJgG-XLNcKmRKjGMsB6K_DNZGtgVgyN-tfPU0bc2FiZ57q7KvobvQivWz7xBUhFY9S8OsMZX6TLOpiSVjpwb3IZA_g-2NRPy_9i_YaNMCxhflBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
جلو جلو ذوق کنی، کیررررررر میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/Futball180TV/96330" target="_blank">📅 08:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96329">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/Futball180TV/96329" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96328">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/Futball180TV/96328" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96327">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT8y5LgP5P1_YIpfeCqjODbypHqHcqIwfuD5Qch4dQPdcy-YgJnodLzxy5uqNGAG7aqWrb0G9UMpoNH2qRIn4zCsR4Mqqr34An70uNPKQnN9iPxk-6-wrBcIpPv6pGmh-kwd6BWBN3KSt4DwJdAykg45ge2Y9t3rsXpMnPoSw5FQYNW5iiFGoNy3ZoUaL2LM1TITFczHIB49WUosbqQU7bLE0nwBICsMRRbDqdsN-gevAs-MEm5AE3coXGX4vCTU4by2esidNcNr57S1KV9OzqxCrVfLdkpmJrrdT9kOyNjIYXMDwLsT1c8F4EtaW2HlLec6YjHBmPraRYcwgB4ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇪🇬
مصر
🆚
استرالیا
🇦🇺
🗓
جمعه 12 تیرماه ساعت 21:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/Futball180TV/96327" target="_blank">📅 08:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96326">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIojCDaw6LimJsUK1zFTJY7Bo2gciXFVitgge2dQkcHn3zK2sUlwXvMnEnUXY3jpWjwBB8EdkEgSkZ9zxYrJi2GCPFuLfg3FgfrstGFP0wpfhU5Ac5QKp_rrxYvYsUD-_L9UGNmf22p1Ii8LJ9eGDF7qPdFo7u-L36H_iz1xzeOoGV4R4iP38gsPrGz5ZPcMzMrZhBr5mUImr-JYno1ia0HC8IJsuzvWwNT8WHRXwU2tPukXL7LtSitWx7ac83AmWOZNfyosBQu0Tzgc3qPNeApUeumJSHe9yiiklkQEh7rc41V_LhZkKy8DfAuIbfQK2q79v8F7o27vWY458c5Ccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/Futball180TV/96326" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsQgV-GCMKeOjZAwM37L5A41MZjAUlij4ocHsGwemuE9EOxZJ6Zziy0G7Kmh1frRPMywwvt4EGAaDlD6jd5ucG0JIdTPMQtQEcVDC0rC8TuyKe0Z9mhdK7Z6YDeFgJWIXdrmopvGEnau7h6JS_UqfPJOM-oO4mivx1KgjkiC6HI_W9Ua7QYhpxxHHL3grUt_GeIcim5Buu3vrgo5Z95JAI0LPgZLJRfLX4qibI-0SahWdPdpcs1_qxsGx7KQwKdV_Cr-U_j6SjPt10NqUtyiYI8Ij4ztNO4HtqHE8iHCyfFRvaGJVswvqAefOLmsesqiKQ-Ma3NmaStqkSwmfLHf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/96325" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96324">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇧🇪
تیم‌ملی بلژیک به عنوان صدرنشین راهی مرحله حذفی مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/96324" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFdQpHrx35I6Fx1RpC5_CjE5vUIOwQCDM2UeiAFPOy9PbbvePRRHKfKrLyPNr1Ou2QBqsvNFRxFT6b4gT0otkIyG5JXZUW-gM1bP7LjmVNpica4JkztzK9w6Wb02OS_JlLL7fCeI5whqqYdjhDr4_epCog8G8z8uJ34TltL9pRAOpT4102vIlHstiJP4Pe7RTkl11-uken4ycbXZJHDOy1rmRI9uK-Ok_IjCm6Kz_k7Qvuxzgz_12qjmLC0EvEekupWqZJ9Wwj74sC_IHppuaOCznDjmVbjPznCDjN29jZY9sbAgFS7eBr8SY1MG-mBZ_E-N7Q-cdfk2VZ86tCyF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/Futball180TV/96323" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96321" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/Futball180TV/96320" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظر گل مردوده</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/96319" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/96318" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شجاع خلیل‌زادهههههه
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/Futball180TV/96317" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
