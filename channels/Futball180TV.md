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
<img src="https://cdn5.telesco.pe/file/f-ZuP7v9L5eFSA1PNWBNWqWJ87aHBVEYlWO3b7UceFXyNu6wJkHD-VX9kRVK3bsg43xufk3ueMXdex-4oiAlWzspCFqX9AUXS7kNXI5VgY5PKp2EJo9sJo7YLfpAhdS3xpZ7gyUdql7ZKWowrQLLKhO-FvVAlE9JrUkMn6Kzj7rs_y3W5i9kk-PtER-EBj1xjo0xBfrac0ZxWlDxaoCQmnOzkh79pUAMZ6S6jqFw3zRTUn03DYWU3Q_y9ZNO30yknkBb53t7JYKgTJpDCqugZn1yG4iN_6rlhQpFckxGPzH6CpJLzaPBrbFJMbUbvOvwmUoZj8JVtAbSAdVvd_1w2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 481K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 23:51:06</div>
<hr>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImaqvA_tjidQvD14m0vPHgIGCM37ihyLRFYgpASQuN2CC2cDGFTDY35TC8CcAOPwuztoZHkAd2_AK5uHevOo8sAv7lBXjgw-ox14EHxHgNRd6_iqXKv3ffVn0UJ5m4CxTbuiuZVpMYGyjvYrixgKpl6Str1rN181wtQmNWmf8qoF9vaud97Lb1c5d3jhPsje36ByYKnmO-siYWoR9Aa3PkoIVd2N8TTo-0YHhl2DY6WT52jtBoDYXEOUG5IxNBPWWIq76AlqRrnJB3y5SdJ0_v-CLlM1iOVSWoa5xUYj5YyrmBk44HcOVUnfFwJbkEaXbeuSZq_C8Vz6_gtjYcCcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 489 · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABBr1vIea-hg318ogCBL0_BC-tWMjblBYjYKT_bfdBN4_DwaWwNCHERfz7vWtCKHCNU9AcdnAi3S6-kE5P0G6XT7nqVH1qdPuHot0vRDt38SEp6PNCq1tHNXMeXvPK77XtC-AEqW2GIZxU-FyrRSGGcDdaAjG56kB_muGBigIK24k6mjO2JpAGA3eCfDhpEwcb_mHcJ05QHvc2s057zhu4G24cIXk7BlR8sfr8KRRTVbZjErwl4HWyb0jYFdlpu6poV56Sa-HUlgvfGiLTmjTnd7-0aiXuqskLLgG-csHMkPjiZcbOo-U12CntuJqsDWvp06d-yMLXgOskdFu7NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zI79B5nl5xozx4cnbeDh2xzBsF0mX0ARyJBoaeg5o1J0OXoTvFztdeCVcPTEFqYFAcCd3dPDDojBrMTzaXYR_hetCuL3C2wSWw-Pv91ycOS4WKU-XlFabtUAXYxQ_ST_xX_4-rMQ5KWQ_flyaGtdjv73WPfBoJJdHzx6ssXUlypUgs02GzP9l8Hrlp1YNa6IQH-BvI1Jgmv4Hc7Wp3eCHn0bUOhkf0jhTS_dbxOKng5ikSKePZjeJQMS9LQg071jDM_cLrcU4HhgwF9AlLfM1-QwqplV08pBs-C154taqs0b6ma04k-2qwQ7GRULMrb4ErKA6UsjhnSxsN2L0ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7-TPWmyDPZfqbJS5JYKqGlryeJJAEYC12C1NybTrBv6wv9btN2u0HYxvdv5hhTs4vWBR71yX31yeWi50cB4870YHAaRiGnBhgzhR6Lvx-HIkX8S8LJXRoUmNFivwUH0LccH1hMsaghuKKLXfiTkSgBethqnfOqPyTfZQofiNwhAqy098wJUGKKVtb6naq0JQHBnPCbziNWsUSXZ7HLJxtjJgDXFfW36vKlba8bjRe22doPP6yIOCM6BvL8IhK_oog72llwmAEFg8STSGzpUJcrdGe0nlmJcdoqgI0nmPvMdqlzMXekODjx8h88gVE6-WZWfW8RU2glyq3GHMLZl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_y6FbsRXxjyLpz-rHLoOD1PdWglJJnS1Ktbjw0ygdgSdNR1en6lvyT3q3Lwv08uzD_DiRbwzk3GnQ1sVmyKJuEIqs5JAkrLBSZdzxslqwjqVWR97eOAeuSIDpnwj9jMigMo0R3fzE-xw3PN95p2sl-tLJh99u2LTJ5f1rmc5FjZFH6E3QuwncxcmBp25HnS2H2ppKV5l_CxszqrfwFpexdrmPZd-AjUpmrb0DFhUoUozcU31Si7TLMzpFeJA6K_Io6UD4aLlXqSk2t3vgqqeYqxrYoJ8CdJyUJ_l3kBaDJ59RGQFHanG0F6xNxk1CFruFxwywaccMM7QxYaIcTfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD4SZq1X7nNg7uK-Xe5MssTrZxZp2nk_-mjnFku5MuYnvR8ZXWissRvgoHKZ6POPUh5Lq0rnEGjM-ouA9eC-JNswUoA56iB8vdXsyNzN_YR5iWCqVaLCFJ6rgy_wCD-rnSsDBIgruNXnBPYwOTErDMl-C_MMsayrsHne9gWdaOdtWy7vKPh2b3wfLhIjzUCoJ9KI0X96NgKo532ppOmzdj9IeFCldNEb6_xQ58ZcW7y9SaMH8j7Mnm_T5FDzq8Ylmn_s7Dd-AShEQZUywEp9mgSN_5YcL15VHAbDjR1oehfLqJQ8fFvlGTk7jXQ_Hde75RRXOY8Ogxo_30kDzD85cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddhPEBKNoIgJKfgEmkmRq8UtZU5CM27aSYkaBETdq18N54h9vWcIUoTC24X11iVHVZ8JbZbdYiwEN5wiQkczdDo7R1-iSbAoYTZE41OMqLFnBO8Xa6k7SbncEiNIzm71E3VranoFCbMAUZg4FPW_3Bgqedfel-QMTmZBRU_91GTyjSd0JrgbvTKH_ocQOCNV5ISwFnkkQGbf7LUd4V0IlKBxIoqdruS16lx-YY7iFgDGVz3PIdOOGeREpdGKW5GYw847dDVlyzpH2zow9H4xgT0qGlms8ZuIslVqJzlny63KIILEdB4qC_DNpmuq6VvGAEMqCf_jqs92XoxrKe9fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2O3JCe64MnBitMBtTXcNhwG0ff5wt8bwG-DR2sBZtcWmaLfr8dMlp57vOqa1XmfspOGgdd-GkaNrFFurGnpVRwhcbMx777wLLDxl5FD2T9XocPkQZVBjKQSkQrtAhjQGJKKToe0SKNE2k_JRqkxMbuyGo59idsH0mfN_v8UfvKwUzQqvVQ6uy2ev-LAn9vVFoRW-Fy-3Qj0sOIevirbkd8_DdmWnWKgoeN6CKSSd6RO5ZSQP2judBx6S6lNE8LxY_mqBaiGTAm1OOmUjyL5emdUf75691nATbJVAnBIQQ8Btpn7MWEfOBWJHiG2ixZXVl4cj2qgbfs3sLZ5vN7_5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqr8okGDATIV3dIjyAo8imPsa_BPsiWprqshijNJnanmYUvPsUDl-YOKKXxfmHwB9eS0EBuVPLKQsdZLwmPWE2qb4QQnpdwJwmp9fV8iczPubZZRFaNsb2iD2ynphpqpY4X6aqcyAx7NHG6-cdbLnyyFHSIAh8Ge5QL7aEM3UeCsv-mDUuC1MjfEjVVMh_2-rnP4_8i2loUVUnL9VvlGngbqnJLu20aeUGPnzuJmT9x62AzqpHuZM1LIfOG40j6e0RkAp2OtHxcY3P8Jimqw1H9r4ubsT69pKAe5NQ9GZItrri1ezo46wtOf606Rk8jmT7lF-wVDm0ub_CfUEAMDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQQ7rDUZ3QC3znHgPPFK9vpXwxjSmnSl-g8qhjvC-q6aUS6dKfVnLDMaTDNMykNkIcu8Rfdpn45Z5G8Z4NnU6HGTJBVqS_vYfHYpQ4-mZ075vuh3l9PcRB-D9xlbDM-jnBIX9ec1hXi1FpzqI4cdXadA39xcVrMjc8p4JhuN2V2kiVjbFZXH_gtXt3vRDBk4kM2PKP6NTYKNYCxP-0ghh5KgQx2vdkLTF4gw38WFKhBYRzejdOwfBdUA6KZyofwS1yd-qrKj5DgCpq1HHrB8MUffbQ1P75Io9zWUtHfANzzD9fJmtuvdrX0-0YesXxt9A8V027qGqJrrOI3UeGaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfDctse4xeQkE-hovGGheMkWmjnyCrutgzmSvSf4-ewXWmfdshuwKZsciSs2uvpu_WjreBATMg7GwMIkUrZuzmtcdGWIQnNHpEh5tAxJnV7rEndjht3DLiORQrgYNvvzMZd-eKMsotI7-Q7-CqHFR3pxIxw3mdiaoPMUIdf3yK5rNFvQ7qxgzJfrJlJK2CbLUBfkacMUbpjGv4gU5uFUrjWf3eEEZAjhUJlcBuv1CnO0se30x6lnx75kDY9aeaB8DarzqYeSrWLH3SCEGIkqT_tADiLvlGlQYB_-3lB7bxAYkM5C9Tx9ZxDDMKvZg25DvxBN83ZuaQn-k_qF7Dvgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ6AUWioAofUF_sWFx2HY6cWXSz4tkAdrwANW-72c2dYRHiqsj7ck69v509PHpMYTSQhKQs5-km4WhCEQQeYiL-CU6zBtHgsmpcY7FQAfxOm4yHZW0HWQY2GNFb1XhQEkjjVMAZHbs5MgE0OHt8yUBe--APuZ0EzflIGnjNizQOTaTlMRky6W9fBGIUD-e2KXkjYmtau6CGXDKiryc24BXuOPD_NitosetSshJMbsg8XGmu6JuZ01A31Ml5BX3LsY8oc5YeTVNzEaIzXUFXUoy7jbv-eCAD7YGgNMNnBu64DhG8FAtYzbVu8bxG27BmmzO_E6kOn6f2zJ74-Rq8-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl3HsosAcFYH5gS5lXyIhfDNGnmaIi6S2tFfCX-yTFd1hKtEaiyQbQl5scuSiVhPUSfedTfx6v8c6Zvr_iSG0wa-gg40clkQSv1DV58YYkhwZ6Tk8tX5xgYhh2umPRHYsdB_nABxsL_O6hoKtpEPJbBZnpFK-lOMTGAVxO31n5HdSEecYgjjZ9-QXATy3PSVfeJsv0pFXJ0_ot_3iinQ_J7tA14qzwt3vXBwgy1RwtKHEk67s6kuLNj2dK9o5MLHfBeaxoK_0mYfit_lw49zsKvcjPudcFvDtnP4QvE0du6ohohuZUQrERWkFvOZeUWKS-0nUXk6HWsKAiSp39b86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJnbHt_gp9Mblj8ZFZd07S8ZR-5OQbQP0X90ZRoHc0Nw-A1J93Fswf4oW_xhOvIxZJefq_Mpuca84c4BEHIKGbszPG1w6YVeVC9WYpKH3DHo52fGh9gYDkns3yv74a6x_sJBN_z02IYCPOhuQ2ODTIu_x2cp3D3DNhjeN_itN-OVlj38F2V09CN2L5wfkk1GTe8x6bzcnh7MqP1Oa33tS-nhPGhdWOmWdvRAVVrUC5-7xApytzotz4Ws0cpZ58faBAqCxvp_fTqX_t45qWRUIjXruLnM6tTP9g4d5fQzy7P1akk7RdmFG7CwC0LXElcOPsNNvITkUOLjNUywLQgH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFcQZhplobxvvPBEmMA8NtNaZdg1gBG-cRTrRMq1JC72HPoZV-quiZ2v0d_wJMgeBg2Tk9dEtIJWMprRu4rm-5ubrUaG040qE-KfYwjdQdMYI8sE0fQgRpW6ajIiT1HOFg0JN4u4drTXRnxyjwuV8pK23JNs5zQ4x0BMKPXyePE51Tf5FWruvxpahzEHraQ71aqUCEI7zPGHNVKQBsO0yNiV3Fhp5hX8qjIrZWq5seZpaVXmOE8XBrt9M-nCOMbTPKL8fAxkbGSOLZz2G2TrDz9xul6ynVltPIxytTc4Ryexbo9TdIQ7z83PYLuwb8Tr2HoDGRcqV_kLIs-ZwMNVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPXDTCBrGfVnQEjIOXs8OpbWwpoOpth2TijGKXvVCJh9dkOzP21O6SXQI_Q7pUcJuy7pMF9io5JTAKmxbLP0kP0c5dR_jzGP1lgCxTIIQSMvZKMSVVpFMuJRhMgeAchBA0RGzzSjDSuZaRFZ6_Kxk3a495ip1IwrwrwkgPqL37Gw6aGXppqmQp1CedbvpnxLCPxL23AXoBJ7U61NQwCcRizFw5QkyCx1sRgWiAJtDy0F3FTe4Gv48bLDUre3ekGwjaYJ75TIKorfs6Lo96PitNHAUNkMlSabCW7-1aK0NP7ISEOkNI22IEFsgnDr5jDTgfNld-7Vav9wA8qdokMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103186" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ovMbFwDuLwqZSARa-fIvumr1PnU9_DXvPhxSd7RSzutp0Q2NU-6_wMtQd_LsUfFZZz1u3G71OfSj7urY50R5QqgJ1ltXliy5EREjqnBPcOQuvzdLTMLOUxIRFCQW1kGJ98-vkkCgSBRLKkLFXbTkt7PHqurZPl-LmoLwTkeh8teNJ9NMfH5_L9XSDMvuNXk_uCPbudF9UnnoX-5Onflvib85PhvAmw6bDyqVYirvdP-aBa17VsgQriAtunvAmWJ9J3531o91QNHBD5pCaX54Mtc7WkgtzV76vxEgaViE4ZL925_0H7QgYAPDTVoi8NR0gq9HzeMGA8s7Vb__zF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103185" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAx74HTPwcJl-3yH6CcZCuWydHlQDM7JK5bJjJ-nsdMxTD-h8bsYomsk4RxS9_JSZBaz8JE84ZGyYlqeifmoR9U-lWMBkzuoKAP4nhJdtZOK4RIFC08iYXbC8Ys3UimVPT1aUDyjM8f5CHoHmi1a1hY1ONRmeSekKr2w2k5pa9ePwhNCM7Qs770gA6E_C39SdYnBl9Edq92zg3WSIJ-aF6-ud92eVFVsp_LzNl4hjZd8FQ2csoyP96WR9rqSQjBSQGj3JAb7_QBR6iCozFGfucPpaVa9RMzt8qrc5ZOHdOxJ9PfApt6jiQ0I8UuTHstouqDMs3DLiNKh4iujXSLR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuiEMbwUFY34eHdqbE-IQgAy3kIqgqu74ZZB2wsZRXxP0-WPBZANu6x9hLzGlajbYd60uwUDXRtdI2wszDf2bb8KhCFK0Ztfj-xArtRQ8fWJL3os_V9qn_xVMeb0Feto7PH6x1P1yu4ydJhYwOJXYBJRpqO_AEMmlyojdIrAB5QkoIpaLkCP9BHMSHCF-GXnTpt0odb7wOXVWIim-QoSWErZhTXkaPbn_hXkatD0SgZw9swI6ULoDwOs0RoSvkS1V78mIB8a3QQMClkqy3LzEC2MGKDKT-iJlhHBxlmnqg5H1IwhYdDBPJioRm2RBxCS9GR6DIe9jDIpEP0UV1q9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC0x5rT54DEN-D4gevkT-BuBM7UxRhuArJQqmJKzmXtcKy8QXRtcoQ-X_ILAGxDATAPEX5P-Z7WozCOVz5bCrOrOpe_aPV67KYJaVyKk8A881YI1TeMqeSnFdq_vcgJeBwqktqerwXwDorqkSadBCCiGYrRgN_c5GR5SkBfxrIvJoCGP1iuf2KGfQfV9JrrNNPVS0ZNqHVTismMwSW_ImKQ2DRbgaAmRo6Pk-jDZP5AYyL6NQ7kttY8JbwmCe0VIuY_o8FVTlrz4nCQQ7BdJAg-F73CdTDX4WCfkJIFT4Dul8VbGGd1RgNHcxhH43iVS9WhGxFxEMBgOGlBXpGosdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyvU6GuStavzjZlqNlT8LCxAPpKuk5eTWmWP7Nt6P6fmewbPYqxNUklURhc_f-vJVsDvXdYGek-G-pvmMgXLfX8yEnFLnO7liHiKIgiJQ9UJolzP6eKRuOhU2dZVJrdvWJv69AzzoawlqWOI0RLASLjVjleP75DhhANNMld7WcEeAwKXy5RCp5bT09E29PViYnnOjrBQyAUevO6fLu0CStcE7cOOU20lbcTVgJ_Viwidy8nCz4jhyAMSqxQ2KVZzWoSAgTFEwMVOdLkrTBkYClUDMI6ZNHKQZlouIqhYHGZ6uBMzevFvVwMnpb-sIN7qrQfadye1h9A8-BjLC-U4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چلسی مقابل دارالتعظیم با پنالتی مساوی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103176" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وسط مراسم معارفه نکونام برق تبریز رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103175" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKRbatB-o2F-01y1DBmc9iyBhhovw8hh13qW3GFjPdNEiGlnjEeSPzkUrn1zXLnkWSvfUNo0I2-Hmr4M6dqq2o_mGiQHathDC0M5TdEUIIKa9BJBHAdrf9rTg90naM7_T9R4sN9WN3TkExrS9AmJwgDPDqi_1CeRQwVSoSrJbvtejyppME2JyoLeN3PwNxN6ZXaRqg3ToJKEpmEqzXlQtz3X76x-kaDvg8OeixnBHhAA5xFXQ46nVGcb7ef9T5B1-z4yNH4Gc5MrIlpNYAsD2sI3-shMmPJOK5pRAcYDk9Mo6WF17EmAUPNszegQ5rXdhYWriPgWGacxsezf2SgtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه دومینگوئز بازیکن 16 ساله اتلتیکو تو بازی دوستانه به سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103173" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjHqXBDlf-9KkykGigTTVCGot1ZMEkLelYeFvd2gRQ6nhGP-L6cVOB5K8KPlwyBdZ3BolqJGFEDrudAJuRdv6Uk0L4uorC5eHFpk6tfrKZZQ8HoimSyKyXb-3y9St1i6XrOHz5tMhGtFgNS3iOHt1LH8jq4nVsMFMOjdzy90QBPLdWQk4Nh5GOzGy0KJPcEPTiqkqbdEY0w3FHfEzfIiv_xJH-ZTvaqLSMTz-wB_M2frz7CiImqFqzfg1VLg5qetwrz61RWkXIloVBXJUbLxHVYtF9R2L_RAAtT-TlljECJ3s1OF23LqTs1tjpwwz_rQwQiXkzjky-FGRkD352T2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8pDCAV-DOS9zpr1NcUxzGyu9dnl69EPeFbTiciQdkpm3eFd2k1xtALEyDrPOMYNfZw_XWDv-q3y00RTFtPvUfCnlyd3UEnOdBHHrd31AYOkwl1eEQBA4oqz3GtUOQxjkjcM-QK771UeSCLFEBawuv02HCe_S28R5KFOXFTdyA6Yt04DcZYqLGe6cvJ0Ue_GZP5AJ6dxf7AkaITpbNkLZiPmLCBjeOWGLrWgpoHNynLYvS5YBuJ_BHrwqiJYvzyZnzFjDAxI_J8_tclrQxBRPuzqpPi744O05jdkrZg4T2t9KUaqBFpWki_HCSkBBd6TGPMINSESRhyyrL5zMJ8Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN3QANWX6Y4IZspuGMIg1Cqw2s6-swU0iiWnerdC1cX_gVfBFMaRb6-nNLmAEUo4ZICtdeIO-lSs0C1VIUO-xw0PyosihrsM8gwgZPyMy7k9v1EzaaT4Hn468D80Tp5YtXr78jLzTSZyf9Fp7pNlB1KpldqXqP9Zi3yTmrf8E7qbu9GG-0XHW1n4hcYWskVrCNTldWcjG55u4SlGEuA3j_T7WO2dO4zM0Z1p8ttQMNXQJw7VSkT193bRL37e9TCmU5OqqNCC1_VQiA9xZRezpqLobcvOu6_N-h--e9SogBWvS399c2jhlENIb5eNT1iIPjC2cs5QR0DzlFmHk3ApdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogYPOkeMGoaGLl0JWiChBFCmgM2AnxMVL9Ax2tLLa1hFxtKyFtsIe3uD2tlnIHCWPlzXIbyGXYBrc_HmK5cbsrEWJAYnyvqXf6CP0x43jLdOKeYdYmKsAA4Mrtgy2Bg6LFtCg2uROcZJsUa_guICBSaiX8fcIqepBM2XjDhqwCf4sZ9hGWMKoij6InSF6PwNIMdWib2dANMUbFSkwBaZefFNsa0NuxN50H2Yt8y2g-BbrV10pd_sIRyl6b9MXdOsOu7nvyZTmmcD83ERJ3ltXjws7mz77MyzVpTu6J-cJ9-GYf1FEkOaOCopeGWAo02j5O_vqDu97ew0uFB9GZDS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5F4M3NX816YsdtHJz-G4mSRVJa4n1Vt1IA1l_hKS_T3eXle7rJsdMu9x1nFA8FHv5bcILfDRUbvhFEqgnONyNdoRhnyf8_f83FwHvA0NIuRizDNmo-o1O_YEBfs8YavvdE5jLnGAQcWBVtUYrE4wErCH8t_vFof03ZB828PShdarNIwLzShFyMqPrLoNlIMqOtNh_zaJNeTMKIsJBtl5Yi0Hy4y5ZY-JfKbepRLLfR2oo0-zO6Oarvlrkbu5CcEuzRjXhcOWkLre1-6OT6hrqYLaunFvbBI7c98orAc1WB4YfTx1KvLQLDDvcnuzOC35XCmk4uPMsqbop914JhonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRDtYPowlbrdvoGimkTm99fK88Cf5JTM--XbVhg7TdleMm_l0j0lN1Ej3WXMWHVRgD_60QxsellOENCvH8Iv4X1wfmNrrwfLWuZW5Z1sJ0JRrZB8SAxzo0m-6irumEYjMAZOLWLVlhVPu_VJAHl89dzLBTogOxYOBaDSvFwJrklekCK0nbz4XVGV1aENckTs3TBdyIHoOmGN-dcEXu2_XiY2FH_u7X4FsIi0-hg_Q05a0VFKD2wN6XJj6756_ycWTgyYm8f0cAI2a2lbcGOQ10Y_pYmK_qMjtCVSIPRD9Ox8OQ-LaRlpBqNhVcUbs_ABDfLk5hKTEqfqPAPVRaTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آرائوخو وارد انگلیس شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103163" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVYxjH-gejZ3pd4WaEb3VRtQG3Fg0UN9riU4mbCNuwPL_gEVfH4Cwq23DwnkQt_6YaSrRClqjjFjlSzzo8wJR8Sfr-zf86IOcLBzXoFNTRTEPFVY9EmQyNID8gJUqgDCtOE3pBPtIl739uLRCA4JbhEDNm8BEedUy8KPlw1GjOVmGrbj3goOfEHvCSShUsGuc5AsS2z0ZYlq2nYCQg7TeU0kX4MCXZxN5-E8HcYilK0vIlgrfidGUTW8B0_b-QcmmVQ9kYrmFLwmZnjrNMLgRkTCfcXcL1cy2OrlzL-SajmlZf5QUSKpC719OPEtFmRyrcwZi_XbP9AcQjIjnXu6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
هایجک‌های تاریخی بارسلونا از رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103162" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
یه ویدیو کاربردی برای دوستانی که حین رانندگی قصد دارن ویدیو بگیرن و همزمان موزیک گوش بدن؛ بفرستید برای دوستان ماشین‌سوارتون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103161" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmF_DGhb6m5u9AiHvms49l2E7ogfjR62Iu0BSU-KntJagcw2TLSfK9ep2-eV74sVh-4ceF2F3AN2D8W_mHMwzl2iVOEp-SWrNEVKoaNDTKt8FF4rTg4ab1qxk-fI2KFypCyA0QD7kDsn_tBAv76zScKcvwxNj8i0T67y6Q8PSmBBBs23hW9jy_553RgotrFeQ0mizXMs4O359hj4OUDbfwIjadq7eOKmWxACAyHLWIPWMl2Z3qjZ933iqwc-VGzfp4oFlAyKcboVtnWBrmS2I8zysCfPiNnjMgpnrfF_jJjIJpMiNF5UMQO3gBHRv6ub0TRhup4-JBoHZMInaEV5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuYxYB757tUjG0Xmy6G3cbGaNeWL76En0z_dcJtL_Zxlq96gSQtDsqYy9ArZ4PKn4Ygk0-gPqKBb-hwtFCizB794C_KrdzINzGaIXHs7E2fSOXDTYbpx5jD0sZ2HM6eaYVr5UEWwZkb7hZntLE54d844_C7b44mN7lFRsBeqHA07rxvaosWD8cgYKzwsePv50L9aKD_O5RHZUN1ujFqq05VHGM_KcnfWVb0lhUEgaxmBrHU8FczAvM77kTo_9iA2dxbFNXeGYvZVNAUbwvzPzSYydSQKfprTh-P-gIIAZw59_GR_IaYF_zl4VgTDyR7yJvp415jvp6yJ-j3etH6jmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
ترکیب منچستر سیتی
🆚
اتلتیکو مادرید در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103159" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
⁉️
بهترین گل‌تاریخ فوتبال از نگاه امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103158" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjuEUCI40KUm3YKL9x27_nTCZDtmQvpXQCinB-ojXwNZpb_nzj3Xlnf6p_vf_2fiCDVgKpn5jiM39FHDVKv0fOvmT_iXAaD2WLYQ2B4FfHKFWs3CoiSeDK9fBNR0804hGFpB1B70Lz8LcLtLLfEaJW8H67ijm7jAflDIUQKX6EGRflTSTsIijnwR-fpWLXs43UWVseHDhdkoYHmsQkZK_HKKKz_vVc-JWfM16tF3INOGZX7S418sIbRr51reywDZrGgnY9-SvT9WIsLwC6WpFLcL-yadLDIAtA-IotCyLQkSNVQ7w_q2Mg7fbRmYaPxMbpL5uidVZIRoGEa0JV4YIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گستون ایدول (خبرنگار آرژانتینی) :
✅
علاقه بارسلونا به جولیان آلوارز همچنان ادامه داره.
❌
آلوارز تمایلی به ادامه حضور در اتلتیکو نداره و احتمالاً دوشنبه با سیمیونه صحبت خواهد کرد.
💸
بارسلونا آماده‌ست تا پیشنهاد خودش رو تا ۱۲۰ میلیون یورو بالا ببره.
⚠️
هنوز معتقدم شانس خوبی وجود داره که او در بارسلونا بازی کنه
📌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103157" target="_blank">📅 13:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تخریب یکی از ورزشگاه‌های اوکراین پس از حملات اخیر کشور روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103156" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3i2XhziiZ59SnrW8wanlJLalk2cmVpc627fg8o3uDSfZ0YMbjM98Oc-Cs0JJqAovQoKSUDZp_IhXYe2SGg3JfAOmPa0lD5M2ZI8Mu43otZK02WrlnjQDRaT4J9FGiV7nWw95NmzpZJzGaPhNLqBozNM4gohgqKfm3Zkcbf04fm5QEnAoq5N3FiS9QqDLh0dYdnbRBA1wqLAsKeSfUfl0nHij_op3mr9Gh_zEeZaDiNsBLu6pC7Y_IZhTh7jb_tSilSZ92T5OBmRS7wupbAQIVKjuS5a3g0MaiT-8r6Bj-FsIuInK7YufgO93NoX2CUGT4_sanUTDU8uds_gI7lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیل‌مالدینی با عقد قراردادی به کالیاری پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103155" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMXhNSok93UIaQaEOM_N9mRMoNx52BG0AlpuaDUvvzE_7q_MxE2TaDQVZ2yDzh0DYQdZ5LjuZBMJgbMZ0zSTyqGnWxKHk-GQN7GfqSOVaUpAxWvGqscyTtgEmh895MfzO7R9hP-GRohleGC_IkMmVaSNPByhLApAOE3_TiBKMGxPFhMKoh1hFcT_8ZYH_ssVJuD530UKvohCpIj4EcE-U3WB6QhVXY5Bfd45mh0iWGGhpCLKDFdh5BYUioabKpaeLq2ikP0ZRZQPK_CO2PwF5lp8p--K76XFHY9iTQ-MnreqnmHKZTLj9B26cL9m6NGu1C1yQukKLX5EzQBu--xuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
😳
😳
ایران مهد عجایب! یه مرد در طول روز، زیادی به خانمش دستور میداده که براش چای بیاره!
بعد از یه مدت، زنش توی دوران پریودی میزنه به سیم آخر و وقتی مرده میخوابه، قوری رو میکنه توی
کونش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103154" target="_blank">📅 12:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoJtC48a3himsg4LHQZHLKnHsUu7oIXXs9OhXfF0S6dIKptBCctlSyO-i8ldM3AX_3KOA5szoTBlZ63vEb4OaBzm7b_GS2P-afQrbJoMjkPlh3Wy-DaqvL1irfCNSfNjy7m4omwZoJSG4IZzS3gyVEg-GlTg6RAWE5RgfGlWsqpcb47UvOrCu1mFcCFcZjfmjFPWroJb8_aeFI4MA0Mi7noyGo1tl1bRWDVo0MlkeS_zVgVNx7TNtJB4RG_GnO7p9exHg5h3qGrzBBwDUWwf2ZJ6url1w69LcIYDse8cbK6b_TKJNXFF6p7Snjns6wUdJFtl25R_3G1X8e-SUDgJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
روزنامه موندو دپورتیوو:
❌
🔻
اظهارات سیمئونه استراتژی بارسلونا را تغییر نمیده. هفته آینده برای مشخص شدن سرنوشت انتقال خولیان آلوارز تعیین‌کننده خواهد بود. اگر خولیان نتواند وضعیتش را حل کند، بارسلونا سراغ پلن B خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103153" target="_blank">📅 12:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVDp3B_5R5mCIPyxvv1SiOLzIszgtkNgxgY8LDBZSO58AUk_WBWPWuZ0PbP0JAiB-g4NbEljYOvuEf6vLZHaPx4W71RLzxQgRd7W7xvKF5yp9Btu4dbkeARAT8aRf5U4UD43eoH-Dg_1k4P9Nr6Zn2pHqVIjLKthqERpv-abcG9CV4PGFsgESVxLYwSkYSfrGuaHFhg8dIL_PgaLumDv2XOZbq2Erp6m6qxFkWkCAErU3H2B6yg8HkIWMOI77mYh1nKfo_QNuGxXm7Q1vMN5qWOstoEamuNMYMO0M9FcueH7k_SlHthX7AZ5jdRTv1COWVZ6TcFxWVdpXvFrivnRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
خنده‌های حجت‌کریمی و جواد‌نکونام بعد کودتا علیه محمد ربیعی در تبریز
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103152" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9cB75soBZR3a7wEF1Wd4-V0VFbglnjGiUaHvZknOhB1Md8G8o_bof0SDqNrS0CY8fWWL3LpCXwIKBxDEn2uirCufXg238kDrQPcKYSEySJsAwyCNKCXzx35uW021lnKvduyTB-pZDVmACS8sLNMR3mbhqccfCYGe0kz7bKJDj9FppkKPfyfUVWen-H5n6N3BFvxio5JjmFdpbI-L7qpQt5OwB6zT-eZ2KGUNblHp4N8fuJdpjqYds1MZfK07MvXGEYFpQTiAwabLywf6ROwBKDGe8qtFEXjyt0FRgAd6PBhp_oIzL9DYLLHFf0Xa9M5dADxlnA-MBOpesnxuqt-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۲ سال از بازی منچستریونایتد و رئال‌مادرید در آمریکا و حضور ۱۰۹.۳۱۸ نفری گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103151" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103150" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWWx7iWig-cR_mhfrVAXbbx7M9o2Uvcx7Cjhv2PZrO7MZQRgsR3QkzH2SFv0RxcyRZbfJp_V-0c28JX6alQYqe5uEejBWd0DzNiIiE97j5wSsptJZ-ByQdoWAKdAoaz3yYzQRBMUKGnxnexLnShx_E65w0FdrErN9KjL-ZqmOmZh5OpthgAGc8IQY6qAkwvjb739UDN7H82zfv948dWacyAJpvI7EY2VUE5k9XYjIoOxEfDfy8ZF7vBfDJaHoHXy5AgIgDW8-HEmXyhseHP9n_nQBT8O_f73dEWiYzTsE60W2XWFKLEJrXZ1NcfCwSJOiyIliCepa01BrxHaQQ6txA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103149" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یکی از جذاب‌ترین دربی‌های سالیان اخیر منچستر و تقابل پپ‌گواردیولا و‌ مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103148" target="_blank">📅 11:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7M0x--iXl1GVOv0hohUwNktEEww73Tez8gZ7vt4bqVr2ZAemfBZ7UYX2fahK3rq_UafUCb-4L7_FFJ3Oz3BN-9-MM5a2-W2l7_fQS-bNyy3Hgl2_o8NomVBhbldVnBF2fN-olag5OU1yvA3Zke7lgWQTddR3xoa7WLwHwa8Mk-LadbzHgcmoMFdJUAe4gs5mTNCCy-lcOH_rA6ow3TQnglXpUv9kCwvA0mx2-zLEFr5v7gDaQDXqVBJ0GgoFntQMF0olzq3YtxotT9jWTOZTCubN7xq0gb4d49H2yEi9lMN3uMOvumtDTqZCaN18cTp-MtqQ-712S2QNE_wsMHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
فده والورده:
من انتظار نداشتم مورینیو این‌طور باشه. او خیلی به ما نزدیکه. گاهی اوقات سخت‌‌گیره، اما فکر میکنم همین میتونه باعث پیشرفت ما بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103147" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اَبَر قهرمانی وفادار به عشقش فوتبال
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103146" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
والیبالیست های بانو رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103145" target="_blank">📅 11:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqSgYhnAaSVIN-4RQobCHqw5sbzDefvignjHd9PfchZL5LK-x-MTpTCbC1T4ZNmQ7Vh0nEqA2iV872WfStTqhz7gNUJnYjaNN2D0jEVyvKcMoHFSXcNR0IT8x6Tgt3s05CXssQPjM8fdI24e8iI9i0_PXFUdVeAFuFAg1KXyXgK-2Y02SlWwTcZgIDfBiqI62ICISXPIbhw6hKllvWv0Fe2L_I1fuKloAK8018qQ6v1MtuWcTfHmJe9saZ38VmhQS-F04mnCw9PbpuTOhjS5Al9TecdFKSUHCMRN6BVGcsJsP3xmGACX1UhrhxzrjiI3yE_zzaK0cUSxcamTEh9yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینزاگی عشق میلانی‌ها امروز 53 ساله شد.
🔻
فلیپو اینزاگی انقدر تو دوران بازیش روی خط آفساید زندگی میکرد که عملاً آمار افسانه‌ای داره؛ تو کل دوران سری آ 300+ بازی انجام داده که اینزاگی دقیقاً 368 بار آفساید گرفت! از 125 گل رسمی اینزاگی در سری آ، خیلی‌ها معتقدند اگه VAR اون موقع بود، حداقل 30-40 تاش مردود می‌شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103144" target="_blank">📅 10:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شغل لذت بخشیه واقعا این فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103143" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=nvEmcuQ1X6rKmCA0SK_lyn1vstZC9xCo3StVhpp54GKUTFhQzBghSfF2ojWzpAJ5Kt3uY7tQnaWIKx7GjS93gHREIBj806Lsaj1yxT6CKO6_oAhUUlCFiR6WT26bVyv-0RoHDyDlFr9srzDSYLQXlPe8T01_RzWyb_93-3shzFC4S8gARigNVlbki85VRWpVPZt3COYpFCA-kvgjafuVYYhuTXhsnhe9I_WaGwdQjxB9Mi1Mgf6p30HYWAsyQdSaHjYT6jTiTPB37r5OT8_JkYwv2o-WZ6hiWuGTOrqS5aFFORM11gPHJfsSr8Dhft-NfWLOgoyYiyjJmbfXjyy1ioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=nvEmcuQ1X6rKmCA0SK_lyn1vstZC9xCo3StVhpp54GKUTFhQzBghSfF2ojWzpAJ5Kt3uY7tQnaWIKx7GjS93gHREIBj806Lsaj1yxT6CKO6_oAhUUlCFiR6WT26bVyv-0RoHDyDlFr9srzDSYLQXlPe8T01_RzWyb_93-3shzFC4S8gARigNVlbki85VRWpVPZt3COYpFCA-kvgjafuVYYhuTXhsnhe9I_WaGwdQjxB9Mi1Mgf6p30HYWAsyQdSaHjYT6jTiTPB37r5OT8_JkYwv2o-WZ6hiWuGTOrqS5aFFORM11gPHJfsSr8Dhft-NfWLOgoyYiyjJmbfXjyy1ioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
هنر جذاب و تماشایی زین‌الدین زیدان در کنترل توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103142" target="_blank">📅 10:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP28gQaDdZiev5HO50MyBfHI9GghEJu3Cwf4-XBzS65c5sKSBu8-V4wvxAi3E5uixg1hPj3TUQvm4vzT8Ldtj-tmhgnfM_A4RCo7Of24Yze56jHBwFD3IZDivuJvOLeeag93D-BymXVN5tVZ1cwS3eJvMNZKBTudYuxof72mBlXcdO1L0QQ9mdNjmspsDOxfKvQdYgqSBIJtwie-0HOzhiLfim1YoBf35GQAksR4VmjmF4lRYnL-xb-_V3MKsA2_n2OV8IW_3S11FAenW6tTOt9mywG9OGEP6zUzG5mmqk5Z0t6QCqguSLhj5TOcRu_QgLBU6-8ls4VoNQxeP3CnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو: رونالد آرائوخو امروز راهی مرسی‌ساید میشه تا تست‌های پزشکی خودشو با لیورپول انجام بده.
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103141" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox7Rps37cCzTTzmB2HGxj4z0jDRr38sg6gT9MiTYkoorA-TeyUrDzcuP0Gs4jeAbh60s-lhkgPXKWRFkQibO5EJEzcsRfeJzts8EDyoeLW1HEzS0vIlS7VsHV8zoulMXbee2pntmpfPmfAJIWXmzd09wrEbGwoDflF2eW9DH3ULLhY4THy_nnwdK0Odfe70Ddg3ztNsaOeSGD5sHkVEmqm449H7XjkGEyDhiBB2r7iOZ7oMpN5kCLc97ZBo3Tx0rldSJSTMtgDA7B2FXDbAYzo-LUow_Cy9oBOVBGSrr7NN9SPCjNEQ-MPGDc-z4lML6nThvnAabec4T95kcRmPhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
آموریم با میلان هنوز تو بازی‌های پیش‌فصل هیچ بردی نداشته! حریف بعدی میلان منچستره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103140" target="_blank">📅 09:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رقص معروف لامین‌یامال سوژه عروسی‌ها شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103139" target="_blank">📅 09:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVGkKNoHEtUcY7434a3uQsnWmv2FR4XjFxO7cp1e143CJchwQk-FUINNo153fszsQjEAKDdQsStAZiXdRFbZw__nPRaCl4ouCrP_Z2AxLpv-16rZiaDEiz5e5ATiWv-xckM4uOjeN64xchU-tdEe4d5CePtOeXDkgOTMXnXpv5cN5fHdw3TfK2Z5vjTJnM1trb1s269kjv8pANHiOU430hPJUiZwaY5J_-m4A-9eimz7bAkgbV16jO8hfdK-dsB_wBiWSUv_tE5A2xiBA3Qj3Z9AAZz0gJtjxa4eAwWe547chM3RPurG0GJSMTQylmEwBTWMV1lFaHdGja_jCGsCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوووووری
؛ جواد نکونام به عنوان سرمربی جدید تراکتور انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103138" target="_blank">📅 09:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5Oen7LUFCimZFCchF2ZGr4845jbDI04ZIyDxsftFMUDe8s0FbzEfWFUU6m1IYe0yCGMHm3lBZ2MXYX-U1OAST2z_10QLMnHt6ns333BI0VRR0Tudq968On0IX5AQPJ6BPU4vQaY9XsYxyFpScsOEGVJV-hObJsiDKnJIfjGdjozMBf3G2Al48rTPtUF-XPl0nvnXG6BWfuqSstVpDDy7BhH7J6aV5cH9kut7qtGrq_lVbO7WI-UB0lMEqVFsMolM2WlQplOoiQ2obRlsYuHd2QYhto_Net5CNsGxMW5TxqvSVlp6O6prfsaDsmeilXoTr9lrJykc76dfA-Jk5HBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💥
هرگز فراموش نکنید که لوئیس سوارز چگونه فصل ۲۰۱۵/۱۶ را با شگفت‌انگیزترین شکل به پایان رساند
🤯
🔥
⚽
⚽
⚽
⚽
🅰️
🅰️
🅰️
vs Deportivo de La Coruña
⚽
⚽
⚽
⚽
vs Sporting Gijon
⚽️
⚽
vs Real Betis
⚽
⚽
🅰️
vs Espanyol
⚽
⚽
⚽
vs Granada
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103137" target="_blank">📅 09:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان یه سبک زندگیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103136" target="_blank">📅 09:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZAc_7gm6-hMBPYaMaUPkXAE1buAeiOqBpCWiOjiqwiunCRcOgaWvIllZ5Dq95qosA0vOv2Q_UnwZNSzmL5jos-jd7vf-eDiLp6R7EnxzZgNwpqp7nfi9xsAfmx7gL9udPGX4zpU_Q4W_Ht_STOPhWJY9iSSprws66v8Umv6auKrCYh1UzfuQu1UB3uTtHj-R9jBqZFaeoMSE7IObkLCE3GlGhSnk-hDK6tj-YV3NXcjV2lEQHQFMMrqPuBKyWjg1Lo9YAbrKBdgtvJEZLBUVD-yuqYpdZos_qctcE5OqwDpLLmdS_CEvCEPNBTXY_mLBT9UUbL_qXC0QCcBXd3BoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره مسی هنگام ورود به روزاریو
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/103135" target="_blank">📅 07:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رودریگو دی پائول، گل خودشو با پوشیدن پیراهن مسی جشن گرفت. لئو مسی به دلیل فوت پدرش، خورخه مسی، در این مسابقه حضور نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103134" target="_blank">📅 07:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103133">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0UUOS1E1MYciPBifaJ32Idk0haLWi0_joOl5uvQ2SHGltr3G0JOxkEfO2O2EAqHb4HJm7h1o0Y3RcGLlnubqNcGIMhcPu3IgBVtin9lOS8Cpc8wFWNlMRBDg9_1_QM3KUqlOdXuR-q7EabYgbHqb7zvkASvITHyx2O1Oq5gmEDq0xqVRLQ1vgmwPqD7TwB2kbq1NePdKsdYaAWLfEaelVioE1UkUwMsQw8px9Z0MwuRjQsl0qmq2NXsJXHbT_a_6r8tUiZineXE_6MHpIOX6HhPL2Us4l5ztESSiei2AsXW_lN23_TEVhPoXJpbVzZU2z0IZOAcX5eKDfxTlSfyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اینستاگرامی لامین‌یامال
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/103133" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103132">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه اصفهانی که قرار بوده برقشون ۵ عصر قطع بشه و نشده،‌ زنگ میزنه اداره برق یادآوری کنه که در ادامه این اتفاق فوق پاره‌کننده میفته
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/103132" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103131">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKfxT6vV-GmHWLjZferjKrjyFYbFcBYMHW-PFeNDovxyrvbJ4bNfQJv-vCCw71cVuV3mg76LQqf0kCBMj4jjoJxh1p3PCCyAcrtuBbzuWPS1u3E-x9f0AjB8ubaje-fg_5v0aZnmI6VyM4VVMpWTKreJEFGoLichUgZIk_OfMLCE8BeHnOna8ASgF5mamj9ANOVZWZVED5K4G5KUWAUl-QBrLaZe3-GGqs_xs5GmVHRtnE--0Xpy6Fi4o2A2D05pi1HKnY6zGEE2jgwcQGQ5U5T1ASseqOOk__GhSBuzVk3oUj3vsepTzF4p25S4oCvcSfMVRbXKRmE12HCuGrrCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیو فیس و این حرفا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/103131" target="_blank">📅 00:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103130">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWZnRL3gox-ROlMyeLHPwXtTKPopugNRAejdQ3Dy9Lr12lLoXbHFCyNBZvWdtSmsqxO2H_FbJBL0hisSpmUD5bkYO5Dl6RBXGdruLisDfJHMwDSy3DMvz44ZaA0w2SXYrDinSnBUXkYfSeyLHe2JLHnsvA5voWK46CPlQTeW8KvEgOhAmcFNnVPJHwoo1cMNWHFAx6Y_2gfgAwv7TJqRj5pYrkTnhhF6oL0G2nCpNRfnO8XxRbOPovpIYv0cVk2GfEcRNZSodzI2BT24RWcvVzTFUbTCe1n3-x5T07lde8-IIrao6NbgnCrcPhY4Yn0C0OxtAd8QlmJ1Q8yVj4FJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
👀
فلیک‌حسابی کلش کیریه که اولین جام فصلشو از دست داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/103130" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103129">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
تک‌گل تیم اودینزه به بارسلونا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103129" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103128">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103128" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویری از مراسم ختم خورخه‌مسی
🥸
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/103127" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuujFo94t6cgMEjgR5xHUw_DBUcS6sa14d9M4hYEwRWvu_ViW9pMqMo89U8j_hA1sQ2xzSXvkoqVlAJlbvCgIcJFizd6LDWbsq4XqiSq0MbK6e1M8fLoJaeZRAn_I6v9KfLa09yDv8KCFQvJlGjKdrmVRoB6snWOuGYRvg-21AiTNwvaLtH4H_JsCQdSXkXQi8tS3SCZwmS20Tfq0ulnWFyaQhxB-cX-X_aFXZgOBRCdMDQQ208tzMLYlCS0dCw4ipyuAHkYf-oCGgCidlEhvQnL5_rn9qOh7v80af9UozkQBTP0V2Nd3xth96NfTapuH01dbaPE6rbXPLYEHk0KIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103123" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbVQMhxTYDQYtggQ720qW3o35CgETYaVEf71QtAKNumNQWxF15RMonv3fW1pNTWpHhm6c6a3wQp8UHHkFNSvOuMSWce3uQ-8jdNt53eHTiE7UmtyociwpoMyOjM4-naCl8LACYrgRj7D7qAW6O4GAEbOcKy3ftC6ZmD4AUYniWFXVsgvnXqElHBbdj0k2ifKwdeRt14kI7_VCxjl1Nfg3cbrCUtcxADrigZnbtTnaooKmvHY9JWCGVRVwUJ0CWym3nR3mthYcpI0ohIifQIf_iWdunCO_XABk8wzC-y_BMrlI2BmIhL0I3UskqbOyMeOI4yzvEPuqG68wJHVoCfhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات رشفورد که حسابی داره بهش خوش میگذره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103122" target="_blank">📅 00:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103120">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7Bw7qb2blVodt53yG6PXRupgFoSdDfgShyL-our3-_pGdiXD7ey3rZuCL1e186-mtZgE06ZLrlqj9zt1sUZpYV3_cKz2PZ3EsbBFl5dbXQP1PKGX27OeyXYe78BXUvjGGUzBq__NNixdGDBnnZKhnMkNCAGSvRfBJBCR9_A2VNfGkCvfb7AlaUFwtcNRk6FN-7cWUZ0ITWph1Ifi7QKK51w3xkqE168A8Qh1UOb9qiidHakdDqcKvaAluKXm4a6fPVXc4CW_zpW2Z-xdlafpXBS0RBkB23Vtz56LY_cJngCRpemU8J0OjvnEr35YpMfngTB1MFH5IS2WOHabXWTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_CyJljtiEgOA_wtUTtcq2KihZ1ITMTV-VqgZbQVdDtH9FFOd2C1O3LerFJHd6tbFAWwhr7xkOypKZNjO36fDnvvJOjmHnMJy_6DsTtMP0dMpNXPmD32XZQ5BLla0K8FZDvoMdEwCo1l6SirKfOb0wgaHw5YeVHcmaq4A7xrIZIi2Cz-EW0K6eiaJXMwtPmnYoiyQWxfVyhWYPCEooYwd_L1aBwYAHuiKCKlub6EzAQsBPZ9Qk6FH1M2OG5xzJalrsyKzEUmVo5S6aePG7alDsVbp31TTqkfyJZvMOtgHGNUSfiCq_V0I9sRF7jHmlwEz4SERB0AxDOkavfXY0RJHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
گفته می‌شود فران تورس تحت فشار دوست‌دخترش برای پیوستن به پاری‌سن‌ژرمن متقاعد شده است. پاری‌سن‌ژرمن پیشنهاد رسمی خود را ارائه کرده و حالا همه‌چیز به پاسخ بارسلونا بستگی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103120" target="_blank">📅 23:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103119">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml6C7NlRyoWfKc27Ry5WUgcEqq0iBulw8DFkW1Y59gbK1u_xNYohBjzGWVW30qZj9S_WYspGnv0geOichVmkmWCijwwvTUgPQjP_XHqXQGSwldV4bq0OhhElRfWaUa24vuxUDNvQihN-bUmUfHUz_i5p6zhqANxcoP2vKP6A60FiD-3LcfestjonIhtUeeFyBssiJGmoMldCaMZ4NYIIFJcT8zJmLrBP76axLVjAbaR8vdhV3l3wUMFh31GtFWQ-gC7RjiDoRGTxBWlvGZpMMM-TnWY8sWX8PVGbB_TLETforf-4meDz8v_T4XRO42P1u4tUnjn82_TfllBFVeR__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103119" target="_blank">📅 23:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103118">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngFhMKRB-EoiggOXntUZE3CXkyqxFsspSYnA35b39SkIrnPYA3laENl9h2Ti-WAWjr0kS2lX9HvWSQcwME4UOco1AklNsydalPSjcI4l1swV86aw8y19mhoHbo27BLj5RwpZmMgiNDdJwVimgMJcx4OwbtCIUPTZpE9osjEpPqASkO00D7_sjahBNkecZlNWcHcWmFhqdaL1rkx7lZR48oNDWKbYqlrOpFdzgmVEzKPgGN83UL-NODSmAZ4_hJsB6McimK0ZlZOFsBAfYqDOXBBbR972LzbvrKFNcjyfaZC2EPguBVvpElxkHgO7yw2yGEWccBkj4yJaqIcHPoH0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تسلیت مارادونا برای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103118" target="_blank">📅 23:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103117">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0hj8ISbGPCJTjWugwKQNNDN7dvvwD2qdavCbhOCI1_Zsf_UMvQ_L4UfB-6EUdLdvHcY09aylchTQjZX10cOKXtmnzRYMw3GmGrp1zkJeQeLOgcyBEzf7aTRbnDMqHYFCz9XF61SkrA3TSdD-4dvkwaL3Gj6S4h5D2nDfWcZoDvk3wNTR47VqwMs7x2-y9J6CQ7yQl2zxVWD6HwwprdE91PiZQQFMs4kOym1FnqrHU7ANH1Y5cJYfSJKBgjcLcYylB25ESsXMJ1NgOdMhIOIBHH3a4VSHUOBEI6uI1HrOKI2pYUF0f7qp5HgTtcq4cHx5zxm29dwEzLLscVXZC0qjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
پدری هم بالاخره بلوند کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103117" target="_blank">📅 23:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDDh2naDjJIYxPa41sUSZIupDS2-KC8lgV0Vi8YWOf5eIdAcfE3WCK6bhYULzAvZeJxoNzM3hMrUwacIqWNW8ioRJYBdIpd2lI2r3iuQCLWMpSVRQeH0ZzlX1H1cKo0CgWUILdLMaIBlAIf3r6HUXJTOAmsoHLC2n-gSlUZYyQtT7bRoUPvMAGt521b2f7n3lIk546xhpXWDaAmEyvZLsTRQ_yhpulZd0BxmMMX4EYMpwFCsbtxGNQ5GtHt6yIleRJeilcwEYDQmbwOI1aceyrldfjOAS8jVpovJVP2MQnVjQo2E1eUUnBcbHE8BWJS_bho0SFhSETCHT4ZgrMe9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTmhSa2gUe3SUK4G6uNR0vkuKEvL-VqP4UnatyIRerz6hv0yqVwxWGMOFxY2frjvbL-7hmVVzbEK91bXfQ1w5-H65WVQhzFOUx2awLnWqckTolP1py8_VS9uxXuAeX0tnUSGmS5k_JtcN3ctsrpSS9ITAelSSWeGOOAz2loOEXwy3aFZMQnSrsT5ZhbNlgDmr5eOBhtbUTNG4iICQyD6LA9HMqBcwHvQgriR97F86ZvWBz4MP2GjPixwl98KqaEbOXv0NJiA_4RfXVGwoVDohlTC8q57ZZaI4YezDB4ujaEjqQ1ZpwCHNj-sEBw63vRcwPdmniAWg3Rc4XWYkiGIaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری جدید بانو جورجینا از کمالاتش
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103115" target="_blank">📅 23:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbb_ySsteE-coW_rFL1s0ICUpEPxJIqhbu7rjTHcn8zqVs1XDtuBuLj6OpSjEh4sCQLJhUtO5LLqCMeGTZjlEFhe-DHxVvN_ywBDZeB47Dq4Km0w4MNgquIY_Tlg-vYp-iBUFFA7QS5tPNpl0_cJg-l9RMADKHivhPgfjJMqtQAmkfXw3R0vR1oOBHTWoAlbcfkvlwFSdHiXNFCZiDIA2pD79smJtF5r8cUgnIyz3WQtUUqMficfE9nl0ykl-zHB_bijwUyxs0FoRtRFfWo1NUh8POvHc90x1YwywFn-Xg4HTqC5Hkex6YeBh2lYRBb7ZrLeT_NNa5ysPcaAt4aALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
این کشورها به‌صورت رسمی حمایت خودشونو از جیانی اینفانتینو برای ادامه ریاست بر فیفا اعلام کردن:
🇦🇷
آرژانتین -
🇲🇦
مراکش -
🇶🇦
قطر
🇨🇩
جمهوری دموکراتیک کنگو -
🇲🇽
مکزیک
🇩🇯
جیبوتی -
🇦🇪
امارات متحده عربی
🇲🇷
موریتانی -
🇰🇼
کویت -
🇳🇪
نیجر
🇱🇰
سری‌لانکا -
🇮🇩
اندونزی -
🇱🇧
لبنان
🇧🇹
بوتان -
🇲🇳
مغولستان -
🇵🇭
فیلیپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103114" target="_blank">📅 22:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgA1wsSW4aLa0lcV7d3nh3Dr1zrfMkzBFtHI8QRMFh3jmv04p1mayMlzarKoPDdK_kqUGAQzvjv-eIHy3XwDF20n9t5ZkjZbdYq0qG_k_h4d_8mkaN0-7vpqVOLPDkGoMdYHv2XazP_1YhFzkoYM_BoJP1Z4zGuB8MHIVlz4OAzP5o2nlm5X3I4GsU2_7ERhAQLFzQ0BzWKYaHzz62TYmKgGKAyN_x2R-7-dfF271a6_vflHzVrhluhXyh_2vc-Gus4tdWgkK8mSuQEIOuyvfT1B2jCd1oD9JcuCn7wg18mVilE8193IDZl9okzngdyBNB6V_BMANWFi3_uNV3bfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWonKWcISr8YNmddplFgGfCm4YGMKjl4cqxQLNMGsFOdJ-MDdplNacFTB7c0wleNs3UguLnpRVdGRmkDvd3RZMEgTOh4diwj-Vn6bGA_mvQEtJpETcIry47vb74_7JNeV6rDEbLQkJZjmc6MRdYei6fz3s5piSj18SAd9_dNU84BipFp6uMnIulnGnTY77eNSZX77l_89GwKWUNiP3YT3jqC3ya6XNbDMeB5orFRQ-h5lTMhuN_Kt21xuiNv0mTCj2LuS5nRqpJjOgoIPsMBzkq_iYIShkTGXyxD7YgIsKOkT6QR3aH5AbmUmZBpPkczpKZdHdyXhBkWcVfu-sw7JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مدافع وردربرمن، عبدو کریم کولیبالی، در آلمان با صحنه عجیبی روبه‌رو شد؛ سارقان هر چهار چرخ خودرواش را دزدیدند.
🎙
او با انتشار استوری در اسنپ‌چت نوشت: من فقط می‌خواستم برم تمرین.!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103112" target="_blank">📅 22:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTfMdO9r4V5v5LFprFM43XVKnzQF3XX258K_rz1xPEnp7a3cfsCFXbVNuMFo2VqyD1CwRZmguHm-FgHTMarIHxAfFm41hG8FGIfHYTevbIw_7qKZbdIn_Dx1Fj5aoMb5M6Aqgs1EJjy4qBjEON6pORtsZFS6u7JEq_t016bNWEfy04qmGCDKSLCNMAK2OZYqYObneiQO7GewjPmjAuNmsiNSc5rCKne6WLWUZs_cyNGIbFk8vrOP8HmfaaN_U6O3VoXUOHFLMgnxICySf-oi_zBRTnXkhS1qDWXDdjRSW8HR-jTWeCvK5p31WP2tNrmHCJWyM46G0qDdrVhdZspoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رودری در یک تورنمنت حذفی، تعدادی از بزرگ‌ترین ستاره‌های فوتبال را مقابل هم قرار داد و انتخاب‌هایش این بود:
رونی یا اوسیمن؟ رونی
بنزما یا کین؟ بنزما
کریستیانو یا لواندوفسکی؟ کریستیانو
زلاتان یا آنری؟ آنری
وینیسیوس یا هالند؟ هالند
امباپه یا اتوئو؟ امباپه
رشفورد یا لائوتارو؟ رشفورد
مسی یا صلاح؟ مسی
رونی یا بنزما؟ بنزما
کریستیانو یا آنری؟ کریستیانو
امباپه یا هالند؟ هالند
مسی یا رشفورد؟ مسی
کریستیانو یا بنزما؟ کریستیانو
مسی یا هالند؟ مسی
کریستیانو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103111" target="_blank">📅 21:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlXVVlSZP1oebjvRVM2QFQRS6mTQYj7AAr-DfprIYUv2R4J5Wz8N1ypDl9rgI_Zgxywrv_PDJ5Ltky3ZMWYeoky4oY3cMHX5tBOHPOVswLbnWvbkki-g66xr9Ib-OfHoOgLOiYdrR3dBEmNS84FpIByXVe5wAIFgpoE5YFHZgXRB4FFw3xp7pWHqfs-xPV9aiUDXj2HvMg8FkTtOCkHeko6ACcaROVZ9uBOmaVbErqXtdi0vY5BA61LGS53P_5jB2sHcnb0sXS_HS4duR0NTQ7eUqzvRHIxHaJ__YUmeIo3AqEMbpW6gL8gZ_j3q8VRN1ZZBuqB0ClfcaQZ87rzm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔴
گری نویل :
🔻
من عاشق بازی در آنفیلد بودم، ۹۰ دقیقه شنیدن توهین بخاطر ظاهرم، عمدتاً از طرف پسرایی که شبیه سیاهی لشکر فیلم سیاره میمون‌ها بودند. یادم می‌آید یکبار یک پسربچه تپل فریاد زد "گری بابام میگه تو یه جقی هستی"
🔻
منم بهش گفتم "من ۸ تا مدال قهرمانی لیگ برتر دارم، تو غیر از دیابت چی داری بشکه مادرجنده؟". او غرق در اشک شد و سرش را پایین انداخت. رقابت یعنی همین کری‌های دوستانه و صمیمی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103110" target="_blank">📅 21:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i28dtZgyatU-uZW9omMGTA-qIlVoKRwGhov0cJIRyZDap8ONe0yausBfBOlccH2TuJa7GCYNVaDo_tQVlVgINwg4amIXjhssS18_I7wg2p71yfiTVwiBF_GEKqD8acaOe_eer_BjpVeS4V49XkTl_M5U_a0VR9q8lm7cXD55bK9febb1NjmLR6aBlOmuBHSIwJFKfa0go1i8H5x5PdNlhzqWU7L4dNcBhhDXNbAJj64ogFa_WMFYRWnGpLfdy4SMsXAJhrtPKwFAyrVwtbhLmWe2RJuCr3s9Wlv4MZANgw5qMMk1yOor0iMSdJ7f9S2muSCv_zNLSHegnQHA5tmJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب رسمی بارسلونا برای دیدار مقابل ناتینگهام فارست
این مسابقه فقط یک نیمه طول میکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103109" target="_blank">📅 21:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poSg90HA4-KoADi5FIaDYAKtm91RWjNbicSoyKDtjPo5uuRvq4TNgKonSKpLvDqBdr0yScCQqh79dSCw5mShqZrZP_1rft6q5H0B66O3a5hEm7Oc2AXsJ0bcnoa633WspcGZz5sut9JAd5Hh8Ddg-W4xpBX6sdJ4diryjsIBTUlmuFzdNuca7p2iSrSIS8s493w4EM8zAUBtDH3fRsmEyGFuHVdTho43BMCPmRzE-MLo6dCT87q9ut_E3pmPa1EeuO6AFyHG0gbRbyTSgaYODdcZfBC4QF_Pe99pNdcJ0YEl5cjdkXKJH1JJwwBrKJ6ntYdOkeFlADnEuUnwjKfchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از فصل اول حضور نیمار تو لوشامپیونه فرانسه؛ شاهزاده تو اون فصل تونست با نمره 8.90 با اختلاف زیاد بهترین بازیکن لیگ فرانسه بشه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103108" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s202bwhuCddnWWwDMBEN8plOjGTLv0XSWPBcvJd2y_y2ibghc_Zr61E_tkiClKoLa-Is-XOZ3bTTN7IXbfZKcn56tcNpZuVEqd7Xu2xiO4wbNPUVLwT5fqEFOFhVHSEXKxAS1GSE_zbHzYFxfSCkZq2NyUsIHF_WhRK55p43lAEmdYDBt8pyGQzqjHMmhSr1J407rv45aUV0ylTsmaPa1gawPFX70owr-u1oK2bQa8BKm1SEq50GBo-cB5PW5X7XH3zDl8NSP30RNEllZyormaeLACyqGm6P5ir2helfOSBNDLhpnBDxywk9zOmX9BAial6ANfX5Zi7YRSbQTybQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
بیانیه باشگاه رئال مادرید برای درگذشت پدر مسی
🔺
رئال مادرید ، رئیس آن و هیئت مدیره آن با تأسف عمیق درگذشت خورخه مسی، پدر لئو مسی را اعلام میکند، باشگاه ما میخواهد همدردی خود را با لئو، خانواده او و تمام عزیزانش ابراز کند، امیدواریم آرام در آرامش استراحت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103107" target="_blank">📅 21:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M04EQyRNxMo387nFYWt6srL44YqRFhS5RnaVIQz7cKBBW4-n7ZuE9mUAke7DTLSL2dAhfrHDd5QIqNIndTb_dqooMrhI_7zJ2pLdRt40JnlRuYaRzcL-E7p5uhDTe50hwVAhIMqt6cDwddRqTjS6oBz18AfQs40pwvXoFLE8cPKBYD-p1UFjifGMOgFzIpyDY1m9O7oinbqPwXtHYYA6noyGhbGKJ4iR1hh4D-p98AgR-eeYmppXULKxI7BNzYBqvTwpu_aj-dvXQ9d8FaeqG88mEjer6HX0rs6U-8tDB9J5xFHgrNhk8N8WqJsoSFLh3ENLnoAq5GpaTA5PFL7hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KELxEbOp74IVRTLgxaqG8idc2qb4RG5Y75mA81ab-A3uIliN3XPvEg4E3egivgh2boia4s9fCoNq2ysT75jZXER6t1arn95WO5ud8VefNYOdO1JnPQgv5gYtw4ZooGNJIZl0sU1ccxiaRZCEHSnlv-uUxxjW4xQMJSPZazxtFbt1z28GxrY2vAxmprTDmd94vPOgpyAxirMZnBdoTSUWsPW8FvsNxnqOSDN3VUtcglADa5iNgwsc4OgBaC2PtX4-wbhyxIVKkDY3zSUvN324TxSWbetomcy6WFSHzsMneB0CpYWRB3frKl5MhVzN0Nm063JN6FhX-jf_AboMSYT6hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آلپر ییلماز برای گل روی ایشون کل پیشنهادای خوب اروپاییشو رد کرده و میخواد تو گالاتاسرای بمونه
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103105" target="_blank">📅 21:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=nlQSsLrX0ha7ZltfWJA2QnRMa8oaFurCHLwHXlFig9DGMJ0FgQmEoIPW-pFN1_KGHIBxZpP-w8m3QED5qgRyNH5tX0Y51DDkqMRSazJ-XcR2qT-U0i10tA1G2nsNC-2l9qjIDgftCuaZcDT0bExlHU60CHYn7VblvshVR1UlcEz5ASOe0GauRd77wYrhph6X1TzBgsH3d3v4plJOrZfaksA6o7R8SlY1-_Gj-dMZglqCdfeILTOkVoKMYX2rx_kPXNlcbrnvXhPW9PCa0l1O0jYGJo0V5ceeCtw1ZURsGUtHVQnbzc_xkyNOz1J5Yk14qWhkGjbaSfxsqDGy46yo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=nlQSsLrX0ha7ZltfWJA2QnRMa8oaFurCHLwHXlFig9DGMJ0FgQmEoIPW-pFN1_KGHIBxZpP-w8m3QED5qgRyNH5tX0Y51DDkqMRSazJ-XcR2qT-U0i10tA1G2nsNC-2l9qjIDgftCuaZcDT0bExlHU60CHYn7VblvshVR1UlcEz5ASOe0GauRd77wYrhph6X1TzBgsH3d3v4plJOrZfaksA6o7R8SlY1-_Gj-dMZglqCdfeILTOkVoKMYX2rx_kPXNlcbrnvXhPW9PCa0l1O0jYGJo0V5ceeCtw1ZURsGUtHVQnbzc_xkyNOz1J5Yk14qWhkGjbaSfxsqDGy46yo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرایز نقل‌وانتقالات تابستانی
🔥
🔥
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103104" target="_blank">📅 20:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCnxD5su65MHKFUiSCYr2GcMFgR1yUdcbR22DK_SJS-D7rRHM1w4qZhk8scEQNBMPtsUypZRky5BRlX1DXtanRqIXboz-cKh_VKha2Eecnop-HRDOlpg97HEDUaxQS-KIzfBAnU5FMl-5LNqJyB72yxnohds0UpPsml9D9f3iMMVQ1n41LsnuRzZizGEde0Vset6FYtweJ-aFKmjaNdBEwqLL8GtlIAZmxQV7DiSgazcBVNZ0dzgRw6pZ2zlhrlzrDXjSxMS9ee30CCiwIJ7BPfxnFBf8OQRZ9JA1jc-dwKOtfWsChRaaeRZXWUWTwaGiPqXJIwFrElNac-3IsEbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=ZJgmU1_WvHsBl3Ms47SOE7LAAO2lVFTW4n6OZssrcOyRY7eVcARdkkDvZFj-i_9FMSpJDoPz5qb3pNoBZP0EuAfFI7BL5jyJRV0D96aU4OSSPwA0-XMXWgbZ0kzwI8cjnV1jvoCxE-Ga5Lgp8TAu3jDo7wyTUA_4DIudONM8S1trtu1u451BDraikBl4EfD_RHl8XsYBz0jFjGXl9iXgFwaRUpv2QoEZecec8jM90SiuOqoR8Uakqt-gVhWRLvo8pGrZPGNSXjuVS5umRlwWONkbs_ApXKuhmmbMGKd87mlfYiSwOVs5zczp4F_b3nZmR5uEZZ7RNTyV8e2dpd6n1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=ZJgmU1_WvHsBl3Ms47SOE7LAAO2lVFTW4n6OZssrcOyRY7eVcARdkkDvZFj-i_9FMSpJDoPz5qb3pNoBZP0EuAfFI7BL5jyJRV0D96aU4OSSPwA0-XMXWgbZ0kzwI8cjnV1jvoCxE-Ga5Lgp8TAu3jDo7wyTUA_4DIudONM8S1trtu1u451BDraikBl4EfD_RHl8XsYBz0jFjGXl9iXgFwaRUpv2QoEZecec8jM90SiuOqoR8Uakqt-gVhWRLvo8pGrZPGNSXjuVS5umRlwWONkbs_ApXKuhmmbMGKd87mlfYiSwOVs5zczp4F_b3nZmR5uEZZ7RNTyV8e2dpd6n1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز رسانه ها یه خبری دادن که کریس و جورجی قراره توی کلیسایی تو مجمع‌الجزایر مادیرای پرتغال مراسم عروسیشون رو برگزار کردن و سریع کلی آدم رفتن اونجا و جمع شدن؛ و کامنتی که رونالدو زیر اون پست گذاشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103102" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slAm-0u8oD1Pg15JLX5U2QFJlYhrtphhowpMnINFvsf8_K5DWLdSQepHvquVimIh79nUXS2rgQXiSZgWuGIStc2gQUGQD2E0LjBsvAhYsSbm5F_qJXeK20RNyRbNsGKAg1y99zrEQ9D_dSdZGD18RFsRyyJhq4YcX9Jiokh6mf2r7zehRIbxiQgCdJSmRti02B0RoP_d1aOTg_KCMS8YQ_3zt-VXhliajxV6PWf4KqFMUT2lpIGvC1luMJE-X-SRio-6V3_jIhK59WxgVCSkR21pWllTdiFVfULB0hHy4oTpxuiPGpg1Pl39OBDJIXPeMHOCAOr7NuUivmi9NHeLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
کوروش اژدهاکش هافبک ۱۹ ساله آلومینیوم با قراردادی ۵ ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103101" target="_blank">📅 20:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103100">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMpkOe53rgBkXDVBgOU-vYmo4LmzcNkDVmfWkw143hULXHo-6xYMbAGiZsPigGf3FP3tnrp2peOvAOdP4dpY5EJdQuiNdHoTebxEMHJJhgkp-np9NW8LAcQ2qY6PFumaEVjVj2H_ao7PJgcLIS7hqdlbRzSCcxs4tIYZUqIpSLOT2qxIbNMo3O_g1oPopOGTshmCHFeCP6j31ZsPy9_k_ckoYihFXpQkTTt6cbQ7SXL-xjOt8hDTWb5cHMHTXOF_QPPcJkwC38tvaVO3Sahb72Ycw20hyCN4-d40_Ky4IKrttUP5CsGxwi6JT8o2LrPZrehPZz7JSqce-oLcEy83nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از رومانو: همه‌چیز طبق برنامه داره پیش‌میره و رودری بزودی بازیکن بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103100" target="_blank">📅 20:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103099">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=gjJ3Voj_pzLRVUczmBLI4rWtuui6mE88PRrXG-Iobm9IxWY6pmvKxMqdD-UZB1lJIXWVad1EmMhHd39ex5YB7P_NqtR7T1XzROHdHxuZ4DxV5rsGlFuyo_uwMt3mYCwbggcnGbALX8ovNctbgKddE7X0V6FdO64VjF56NselU_uXSxQpVrnPB3i127JJXOh6fs_zc6cImyZpxLQ7r0x-M6bDdY96Ef1T105w3R1SyNphZM3Hf0jLpbc6uV4VRtLfOEyBYqd9hOpY7VozVo6zuuoan-kbUBUEJXnN_Hyu_LKTrYdGbSwwIAT9UkikvBrtDNrRlNPZ8JpbfoResjD-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=gjJ3Voj_pzLRVUczmBLI4rWtuui6mE88PRrXG-Iobm9IxWY6pmvKxMqdD-UZB1lJIXWVad1EmMhHd39ex5YB7P_NqtR7T1XzROHdHxuZ4DxV5rsGlFuyo_uwMt3mYCwbggcnGbALX8ovNctbgKddE7X0V6FdO64VjF56NselU_uXSxQpVrnPB3i127JJXOh6fs_zc6cImyZpxLQ7r0x-M6bDdY96Ef1T105w3R1SyNphZM3Hf0jLpbc6uV4VRtLfOEyBYqd9hOpY7VozVo6zuuoan-kbUBUEJXnN_Hyu_LKTrYdGbSwwIAT9UkikvBrtDNrRlNPZ8JpbfoResjD-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیرم برا مظلومیت لیورپولیا که قراره این یار مستقیم هالند باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103099" target="_blank">📅 20:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=o8f3PVWf_KAXA6-PaGQPohJefP1KmmI6yNL4tJKvHNkQDTZStBqTHdXSTa7a6jf24hPLuWbgb4Wadxxu1QiyqpxFaEfu6lDBhTvTrMr2wpq_7C__kX7hi9ElTC_2GBTuNUUMiN1KkvnrI3Q1iN2lCDcwnPrGbU86Nv16sjoOj6K-1bEmS_5Pr76ZFbFx4aw3Rl2p9jkhp2xFzOxdnOtg8pUMpTOpP9ga-egwBnm-hbCdLu8FX661fZhPAfjG7TyBhP_qKNi0G-MLBs_Z97euu3G3IwuC8_x3GLjrBPAs15Yky-9o8f-oRqIdkKQYNY5lAy2scXl0FYNvB3DxrY6hwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=o8f3PVWf_KAXA6-PaGQPohJefP1KmmI6yNL4tJKvHNkQDTZStBqTHdXSTa7a6jf24hPLuWbgb4Wadxxu1QiyqpxFaEfu6lDBhTvTrMr2wpq_7C__kX7hi9ElTC_2GBTuNUUMiN1KkvnrI3Q1iN2lCDcwnPrGbU86Nv16sjoOj6K-1bEmS_5Pr76ZFbFx4aw3Rl2p9jkhp2xFzOxdnOtg8pUMpTOpP9ga-egwBnm-hbCdLu8FX661fZhPAfjG7TyBhP_qKNi0G-MLBs_Z97euu3G3IwuC8_x3GLjrBPAs15Yky-9o8f-oRqIdkKQYNY5lAy2scXl0FYNvB3DxrY6hwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روحت در آرامش خورخه مسی.
🖤
🕊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103098" target="_blank">📅 20:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=hUoDxzXh-u6PrLb_iD5HRywwBO0tJZ3BPzf1uDlR4F3PBjXenzKWTDjo1mZCc8OWo50Bes1Lk0DoAKfPPpyb81sK7dUIu3-vd79PPKWO9piTSNd2N26XJ6OkQK9BpmERPgzPGYvsATzRnaiu7wLPS9FXeesz6z96Qh8VxVbhooy4zi_FTRmh4bQgSwsXd-rfuLQkSmSgQDHIcT1PhSrbCIbEfqCI7sWVse3xxBUa_gd--xDwJPcAwYYpDPYVcODU5YGIeYlGov1kyTGHZXFPc8KNpLg9x8b_9oBRUXMBHU5GNifWuBGIv2QPjM0xUUZ9dLxjcP96RtjJ0Q1r4ZmVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=hUoDxzXh-u6PrLb_iD5HRywwBO0tJZ3BPzf1uDlR4F3PBjXenzKWTDjo1mZCc8OWo50Bes1Lk0DoAKfPPpyb81sK7dUIu3-vd79PPKWO9piTSNd2N26XJ6OkQK9BpmERPgzPGYvsATzRnaiu7wLPS9FXeesz6z96Qh8VxVbhooy4zi_FTRmh4bQgSwsXd-rfuLQkSmSgQDHIcT1PhSrbCIbEfqCI7sWVse3xxBUa_gd--xDwJPcAwYYpDPYVcODU5YGIeYlGov1kyTGHZXFPc8KNpLg9x8b_9oBRUXMBHU5GNifWuBGIv2QPjM0xUUZ9dLxjcP96RtjJ0Q1r4ZmVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول دوست دختر سابق یامال:
یامال ازم سو استفاده کرد با اینکه من دوسش داشتم بهم تکست داد و گفت هیچ وقت واقعا دوسم نداشته و فقط دنبال سرگرمی بوده، من کل شب رو بخاطر این پیام گریه کردم. اون خیلی دل منو شکوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103097" target="_blank">📅 19:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh-AKxSal-vS2Z5o77p6jdwSe_BFfdE50XAWWc5wASVQ_PmiLV7SltTC16SOyhiFfpWr_Q8vmwU7FSByor1tCb2Qzf0IEstgACwOOoGSM97PZch_9kuv__eItQiJZyZXf2IPh1CIqAzKli21iBp5WvQK4TqQ8ilZbBHI3i43qxFsCmnPbfihnWcYVFKB_gBKASlBaLSjHJY5YMcnumWwBtT-xNNnIYKACiTq-c-l6p9S_-VzkIQoUPEK0eoyU6MbL2F5bNiPu6cbJCNZfOAXPf71Gjkv-wDyNNoWZQuuJvsB_LQQIadESzgV69Zocd0IlOnnRY0axFJMfciNlgin-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی جدی از اون نسل طلایی آژاکس که نیمه‌نهایی به تاتنهام باخت هیچ کدومشون بازیکن درست حسابی نشدن تقریباً
دلیخت، ون‌د‌بیک، زیاش، نرس، تادیچ و اونانا
دی یونگ یکم توشون خوب بود که همیشه مصدومه؛ جالبه همشون هم سود مالی خوبی دادن به آژاکس...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103096" target="_blank">📅 19:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=Ti_yZv32VJNTJf3lQw2CNSlaGBvziQwr_6PIivX64RolG0zF5S6MmcWaI9rlNPGhb4EUimSIrSLzJfxvHxxLPEE3HLr4lXzX6xbPnIOocIHikNqAwUmBWJuiQo1lGGWVV3HAzmPTt-UxwXIEucHLybEXb8-vqkIR2XiVIS8SIqE9Fd0C7K3jiaY2uGdc7pbH0B_1kSQXeTgttk8i6yq5JQTfzh6ZQL5MKJbRNElW3VnrbSqsJkMvJW8jxEFvlqezgs0EHbAkS4Vc2I2H4AW13Ri-Qx_aN8dSXqzPj-KqBXO8Ds1FLWlDEBT7FM4uCqzO8vPT2ObpPneafucU5VfR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=Ti_yZv32VJNTJf3lQw2CNSlaGBvziQwr_6PIivX64RolG0zF5S6MmcWaI9rlNPGhb4EUimSIrSLzJfxvHxxLPEE3HLr4lXzX6xbPnIOocIHikNqAwUmBWJuiQo1lGGWVV3HAzmPTt-UxwXIEucHLybEXb8-vqkIR2XiVIS8SIqE9Fd0C7K3jiaY2uGdc7pbH0B_1kSQXeTgttk8i6yq5JQTfzh6ZQL5MKJbRNElW3VnrbSqsJkMvJW8jxEFvlqezgs0EHbAkS4Vc2I2H4AW13Ri-Qx_aN8dSXqzPj-KqBXO8Ds1FLWlDEBT7FM4uCqzO8vPT2ObpPneafucU5VfR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از عروسی رونالدو و خانمی
😃
😃
😃
😃
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103095" target="_blank">📅 19:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7iMt-qYaNba7YPaYVaReUR3shI1WBb8OMk9HAgnblfabcC-Uwkw-pf5DrADNmsYdoS05WTj6D3DUaAvHEa4s7ofA-DJTcyxA-EL5amNqf9cN1a5PnN4dCpOIp-tUvFQOduk0enNRrk2T1XzuoN42G0V_PyW7TXdExDHyyS-a0P31HZ1EymRIRP5usEhYdLxxenYzM6-Z52SbtdfKIuAqooO1DOWXSwkoeuO2_OhsMqd3hdIK6IY8BU2-cJT8bt-48Znk3yI_XA33a-ibYX3wRFgEEEVi64pqetQ25LCQK3F4XFcmHL1kFuc91TSUqL81wBVq6IgVO5TmmYnMmiNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iwr--WKnj3cCnI1fRnXrhcOD0s0cYkMmQ6voXQjNc8Eoa93gJmSbI9tz9ni6YLGAdegpOPxf_7h-Zz_VT-u1T7ZGQruV6rjluEJ5Z9a1jVjBg9FG-OLNc4qDNlI7xvw4KsqgbGaxEL-TtKFgs_rt5lb9qFMJwNlSlB-SwEg1aY1GcYP0IA17MlJztl9bwTrsZPFxbgWUcKqB-EY5YN8J5SMYYXBVVvK9b_FCmJ059j1aMXQRUw6bDPtFxLNVT_K65WhBHeMJ6t-2eo-ilwv4D7tCioyz7Nnxq-L6H4F8zDMDHlBEznVtU6QE_f0Jadj73CquFY4mlS4q6UGuIERupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8FGZfzTqvjqBdYBBWftdTpazHx1OnbvzK5OJv6cWFbn6pdTmPIWRgSYASXdest842sV6J99KfwCOq1rnDpwOZ4eCR_VZ3-rBWVptJt1W8rYx39oxcSpPb_jfn3s1DXaxSJUQB7ja8KOnhXFHR0SbTCOluxlDgU43YCE89gTwVU_gOtOOy7935O2Abh8WQ7lJMpSRal_JBpWJeLxLXeZSU8FQRRcqK7B3XgyhSqI6sNd_mDi6wYJo3amu01EN4cIn-G_DuNEL3a2vsRoam4JUmaetRsrB7LQzj3CvxsNxEkuJztgJz-Wi_fGl4-mWSfTANTr9B6LoFqITBZtO8TgfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
✅
👕
کیت سوم فصل جدید بارسلونا که قراره ۱۲ اگوست رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103092" target="_blank">📅 19:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpd4zO_9O-dt8MZ_034q4G47u0ny1tFp8hZIPKAOTcEpJaxPmmmlyWvFUDEd8aCDW_n4cN02GGTAsz0s2aykPD1RxlBKCmLZx49Im8MQthXMxzLlniYDFhjO5pGC3Ggq1Ai3kUsvNAzY_iqocyCyi-AOJ3del9RLKWEq1gU-CpaixearHHzm2zjaORLMs95lM2yYBM5bkLtGrS9lIXdl9qH-h5hhLgcW5zazITsNGitF8-cZH28OQLf8FfhYgBWiVca-ZGIc4GkmdSeUvIX-8gAupi60Th1GZz0HySwLPWzwkfIFbqASKCx2HgBsIRFNwvNEmW3VOFPlA9WKlioZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🟩
پرسپولیس در دیداری تدارکاتی برابر آلومینیوم اراک به تساوی یک بر یک رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103091" target="_blank">📅 19:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3KSIgKuYdTeYf4QF2nncMPlauPSRZhzezDNo4wm1dc73PHhtvp-SOaR-UfIXy4LE4ro7qY8ybwEdxtZbrxIGoz_vmMrek4oQqgt1gsdz4FXP0QLh5oWjDAsDGHL6KR3lWYPfFBOpnIDDhDFvJmfmTvUQUvZcrODVnOUmn14V856ItpVVwuGh6j8hmVCrUcA5oGQl9xM4doEpV1X6Agbs78og69OZuPLXq5Rgom2ILGGb1j9DjVGagTqoVdozWiJ6z_jjDaguHGRynavpEF2VaXEatplx2jvGHABjktrWQqibEUvoSeY6MqVEjhJna6y6i48qiK0AkNZkb9wFIcJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل واروش‌مجارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103090" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
