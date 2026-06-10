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
<img src="https://cdn4.telesco.pe/file/qnH6093dB_hs3kqc-xb5tae1zdvzf8ZwKfmLvvu3f1cuy2soWhVY4ETnxN8aUCZujewDMFkJsTdLhXRfJYzyANT0so94L6_czv7SBgI0EcioNjzUS79gFwyPBmXEF2qVGtd56_U53fsuOTlrE1rO9oBUL7n_QCiqxvKMIt1Q9ehHhPjnvBVm2RrakBpY7Fdt-8WjVw_Rx-q10o_Ns4aFH-bNugGMvms0FEo-KXQPNNjkZ1pjIKpIbrgkC0ImQ4cU_f8CHObHXL8k5Km3Q3Si-8RQsPGOjiqq2zsFR7-XiF8THE8CsSRtP_zImB6Uazf_FfeNiW2g1GjlrDWGednmiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-441261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a44HQw2q_vorlMk6m9iHFwhl0aPFOYzai_QSF6iCUwT0DtbmAHVtxd3fPn-eracnXnWu0g4tvAEHSUkc3UMDgFjZrRQTcYlSW39GSusjMJhgM37M2-EmWd3GHksfDHOkBoiPKqfKzPXbEzYgDwAzNZqTW1wVTv0QQf7-Db_8E5VGqEWvK6dHeMx1QYPhxtsTDdSIvO0oPOl18pSUAWoCOLJmZXgkpR5n_oWD4YhOptqRcwYoVzQjhiOzGY9m4QJQjhcsuPsC_5xTgycNM7d9qlejQCjzCb4EbpE7BjbkBRb3pRMjZU3iMiHl-l8Be8Zz_xMnQuqLsrJ0aKHvyomnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی آتش‌نشانی: آتش‌سوزی در انبار فرش میدان قیام مهار شد
🔹
نیروها مشغول لکه‌گیری هستند و تا این لحظه فوتی گزارش نشده. @Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/441261" target="_blank">📅 23:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB7ggdZhz9BlM7jDFv1_Qgqqea4PRKKlCx_MkPXMikHfOJCikoqc_eit8edPBrZc9fIUVmsWIFwLyOhsq1DTz-mGJ9Nym5CYa-P0-Oj7DTYZXz6oh7ZwrBmiAxnwTsRlyAol7zJT02SVlLHdtq4Io5afBiMalAj8_TldOKS9GBmnGQS3p_MowIqdlTNKKLZR_NxNA1g21J6RCThwNGHWrZhGTGzgFPFviAu11jaBLpyKRSy7och_gNXew1HN1p3tLpcuOzn009hU_DtvegWCMR_TVPzERMmWwGuVF4pthx3kX-Ms21Mnu22Xtdyi8FUetLCAD9e1byKPx0CNI0VzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ کارشکنی آمریکا برای حضور هواداران ایرانی در ورزشگاه
🔹
فدراسیون فوتبال: براساس مقررات فیفا، ۸ درصد از ظرفیت بلیت‌های هر مسابقه به فدراسیون‌های حاضر در جام جهانی اختصاص می‌یابد تا هواداران هر کشور بتوانند نسبت به تهیۀ بلیت اقدام کنند.
🔹
فدراسیون فوتبال ایران…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/441260" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e748be8bdd.mp4?token=UjdNb7BS6p--4Bsyzc-6cUawdm17x6nWLMdSb39PKXEfEnf1Cp-AAnYxhK8zoojqDVRc2GmLAVF_exTaM5XAu693XiWSH2nu7TV_gfp4NTi3TlrzkrLHU6gyCOIek74KIQ18inAw_yt7boSzMpDFrXnISiuXIG-rSDxiwZ21BSK2clhmvLMcjeUgiS83J5fuPtGCFB-lhJKmJeZWOlv1Ad4E8ZUDVPTSt8M9IDsh5VDWyT7vxMCot4b9Cz6s7QBSlT1VVSpHanPiLo4NNooVhyZREIf1hMLjrhySOPreO3Z2l-QBJd3ruA-rimCUTPttvqdRruldKMTTUrU2tU9x01sDB47adCoHarkVzsoV3zSjnhmWEEHwt2erq1Y6WzETX-5gCF-QBqrirIqQwZ1IG__Y981O6vW0g5_IreYfzD32BLGPfQ7rKj8BeYPDjNiKtH5HWSAtkXvfClKXyts9QUN6uVZ72lFmX31PXvznsUZnAzZWHYcPdW3M_dlfvDXqwlKpPe2yv3PtD1zuFjzjinuvDoj63lgkojTIYv2RZhhxdn2D9AngxwmJgcRrQhDaey0oQGfzjPrMDD8btDuOFAi8lF_pPCB5_CcZoaqvGk1ljcowz24PX-l9H9iymeLChNku5Sa_AhElhE800Njm4CXw70IXjooTUI1R2hd1kI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e748be8bdd.mp4?token=UjdNb7BS6p--4Bsyzc-6cUawdm17x6nWLMdSb39PKXEfEnf1Cp-AAnYxhK8zoojqDVRc2GmLAVF_exTaM5XAu693XiWSH2nu7TV_gfp4NTi3TlrzkrLHU6gyCOIek74KIQ18inAw_yt7boSzMpDFrXnISiuXIG-rSDxiwZ21BSK2clhmvLMcjeUgiS83J5fuPtGCFB-lhJKmJeZWOlv1Ad4E8ZUDVPTSt8M9IDsh5VDWyT7vxMCot4b9Cz6s7QBSlT1VVSpHanPiLo4NNooVhyZREIf1hMLjrhySOPreO3Z2l-QBJd3ruA-rimCUTPttvqdRruldKMTTUrU2tU9x01sDB47adCoHarkVzsoV3zSjnhmWEEHwt2erq1Y6WzETX-5gCF-QBqrirIqQwZ1IG__Y981O6vW0g5_IreYfzD32BLGPfQ7rKj8BeYPDjNiKtH5HWSAtkXvfClKXyts9QUN6uVZ72lFmX31PXvznsUZnAzZWHYcPdW3M_dlfvDXqwlKpPe2yv3PtD1zuFjzjinuvDoj63lgkojTIYv2RZhhxdn2D9AngxwmJgcRrQhDaey0oQGfzjPrMDD8btDuOFAi8lF_pPCB5_CcZoaqvGk1ljcowz24PX-l9H9iymeLChNku5Sa_AhElhE800Njm4CXw70IXjooTUI1R2hd1kI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ بی‌پایان مردم کاشمر در ۱۰۲ قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/441259" target="_blank">📅 23:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6803b8b548.mp4?token=cLPcki--mbdftr2oVJuCj8_qFrEUzmz1wIWjtMaG_8LfE9NzdrZObElBruiyH22AHsj3rl0EkbNRvIVtR5O-6wL4ltoo5a7Pig8s8cn_IUVB1iC5OpwDE1f5hFgmmwWs1GiLJfFRcjMzEsI25DzJNiHuMFdW3EN5knzMqX0oizAlfUhjh_wMKvQAKCmIWY4BHG0KpMRKMO-Ch7A0nCDB3u6LaPUGIA8SR58IfWnYYpnQGeL7kEYzWDLDEkqRuMtt6QJpMrvNRW8v_H7GoXjJr0dWviilXgBeXlcanoD-XhySYN5ac8Xs1RAf1so-snady3CogeksjoB2xJQQalmM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6803b8b548.mp4?token=cLPcki--mbdftr2oVJuCj8_qFrEUzmz1wIWjtMaG_8LfE9NzdrZObElBruiyH22AHsj3rl0EkbNRvIVtR5O-6wL4ltoo5a7Pig8s8cn_IUVB1iC5OpwDE1f5hFgmmwWs1GiLJfFRcjMzEsI25DzJNiHuMFdW3EN5knzMqX0oizAlfUhjh_wMKvQAKCmIWY4BHG0KpMRKMO-Ch7A0nCDB3u6LaPUGIA8SR58IfWnYYpnQGeL7kEYzWDLDEkqRuMtt6QJpMrvNRW8v_H7GoXjJr0dWviilXgBeXlcanoD-XhySYN5ac8Xs1RAf1so-snady3CogeksjoB2xJQQalmM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سینه‌زنی خرم‌‌آبادی‌ها در موج ۱۰۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/441258" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHR8ndACOL2IyCd9hggb3EnyRsAkrHfcRYr9iW3QVfKV3UDUzGI7gTbtH6HXezZ4_xGc_yCuywfNwlWUS4wVcrQxDK_tNLjhIkpVC9QL_KLKVX4zcX6TBexg0s19T-fDOM7Caem0WygCInFO5JxAsz1ZNltUWhQJS7yZNt8CV1k6FRnFvsHyFvprSrLkstebenJSRBvBjZz09wwuVHFRKdj-0_G7k8UlhglfAU6f_VO_f8ioP9Rp9gJtYdzuJqWNG4qUmTBglpYwfHPTvf5BaHerxsswE0HRWU7DaoH1NRLDED_GBHmLKPFBjuK1GWXZT1EdpcNlfHsaKpMgqnqeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای همزمان گروه‌های سرود
«
جان‌فدای ایران
»
در ۱۲۰ نقطه از کشور
🔸
به‌صورت همزمان روز جمعه ساعت ۱۷
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/441257" target="_blank">📅 23:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841fdb1a3a.mp4?token=ok3gLRxpsAHQSEqqVzDsIsPt2jDIcxmiDylhQJKSJlfbrI_vdfO46v6hnMF6EIrTGw71Yse0la0iWjO_kjTsny9s8NrKZOEZRsMU5odha5CRX2cH5wJZgwKSIv8BKEyXwfR_D8x1ZBGTO6MEfzVj28xAzFnwylsFAV2Zhg35QrBRN52rka9jhZDvAlZwkjonfwBampKuMVce6leBfp5iycmkbkOfon7Qn15Bq7EjIB3dwOnRqfrBpSo9SwqgtYGwhJm5_HwGxxmzEpHNJIfBz0J5ef3TScYh_Cao_zbXq35b_wVkUtjjYmHW-9sjK5NKAgFUFUG55WHJp2vgKfxenbFjXtTdw0aEZ9NJ59VZLFF-hKE0NwgnatgOUeJT4KNsC_4OJbEp01ucF9TAKiVMheDLcV01Y33wh1WN2PU3JsxEkeIwUrlaYybwYaS0IeGUFLkTbMvTDdtPhUYkiw-Ocsa7WOusKohEWq_H9KBxBfQyvD_GtQrUJfK1Yo-V3k78xhlP3Fb0yp-Dp1QQd0N0Z4sc6GwyxN9BKJfhZTBHDVFKFfzJCxcjAYSJ-Tpr6IC6AawI6RSkEKdP8yrhJEOIDuugJp_Uy471OUMMea5Mis1liIycRAvOm8DhIsFs-j0W4GGL6b8oUvMstW2R1imDMkEwfhvuKGgSDXvImMO6PTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841fdb1a3a.mp4?token=ok3gLRxpsAHQSEqqVzDsIsPt2jDIcxmiDylhQJKSJlfbrI_vdfO46v6hnMF6EIrTGw71Yse0la0iWjO_kjTsny9s8NrKZOEZRsMU5odha5CRX2cH5wJZgwKSIv8BKEyXwfR_D8x1ZBGTO6MEfzVj28xAzFnwylsFAV2Zhg35QrBRN52rka9jhZDvAlZwkjonfwBampKuMVce6leBfp5iycmkbkOfon7Qn15Bq7EjIB3dwOnRqfrBpSo9SwqgtYGwhJm5_HwGxxmzEpHNJIfBz0J5ef3TScYh_Cao_zbXq35b_wVkUtjjYmHW-9sjK5NKAgFUFUG55WHJp2vgKfxenbFjXtTdw0aEZ9NJ59VZLFF-hKE0NwgnatgOUeJT4KNsC_4OJbEp01ucF9TAKiVMheDLcV01Y33wh1WN2PU3JsxEkeIwUrlaYybwYaS0IeGUFLkTbMvTDdtPhUYkiw-Ocsa7WOusKohEWq_H9KBxBfQyvD_GtQrUJfK1Yo-V3k78xhlP3Fb0yp-Dp1QQd0N0Z4sc6GwyxN9BKJfhZTBHDVFKFfzJCxcjAYSJ-Tpr6IC6AawI6RSkEKdP8yrhJEOIDuugJp_Uy471OUMMea5Mis1liIycRAvOm8DhIsFs-j0W4GGL6b8oUvMstW2R1imDMkEwfhvuKGgSDXvImMO6PTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر پیش‌رو، روایتگر آخرین روزهای زمینی مردی است که نامش لرزه بر اندام دشمنان می‌اندازد
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/441256" target="_blank">📅 23:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hThZ__sGe-LWdBVHNy49SRcs50f-vwKWYfK2QTEA8NFVNU7XyyFJBPY7x5MuW3YK1WWhgfOGQtxjiPTyx7Xk5AZ-FciBgC6tLVL76E-8JBi7R5stEwwXC_JkiuQUCf1qn53ncPCBNtRmEr1Kr7jdREFw-yZ_5kcy8qsjGWIHaBmVnScldiwCxhRHwx5MxdqSSfsfPoKCN9_HQOYSJ8Q4icNvcUJBT3Uqi_CPyEZbk0dbnxYRAH8BAW5ZfE0S76fBtFiqHFKb8y7MYcVlRHVUIrCk57dpxdZmqQSu-X40exufRtRMH5Epgr2sWbi5WYp0bQT2N-LM0hF0QnDxhs_0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی مجلس: این‌بار جنگ محدود به منطقه نخواهد بود
🔹
خواهیم دید چه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/441255" target="_blank">📅 23:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b30113c6e.mp4?token=HgtqPBLW6PKT8K5RruLkcpf9ca_p3JBurPeBHzjNAsn2ahwA80X96kRHsIciRS2tPRGhatWc5hUKnTWsPT3UwYndYcCsEmw7wvbk0J-EJgC3M-3uBNXOM-HclmVAAjk61fYIaD9OTBZmbnsi56znwHldv1m45ABx3z61wfURBF1HXpSJXRzwO5CQCoKi3ZCzInfujmrRQhwppdQkvT8uEgu4t1qpTFFhMiTwAdXkMj_Gje3eVMQDhkH7kEp62zsz5Pbyvej0qfN6qEdSbO4DCz3NPlqvv3MP14AEGpeKbDokuRkkCrRaslVRzqbynJb_QuMCV40njWr8S7ep_OL1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b30113c6e.mp4?token=HgtqPBLW6PKT8K5RruLkcpf9ca_p3JBurPeBHzjNAsn2ahwA80X96kRHsIciRS2tPRGhatWc5hUKnTWsPT3UwYndYcCsEmw7wvbk0J-EJgC3M-3uBNXOM-HclmVAAjk61fYIaD9OTBZmbnsi56znwHldv1m45ABx3z61wfURBF1HXpSJXRzwO5CQCoKi3ZCzInfujmrRQhwppdQkvT8uEgu4t1qpTFFhMiTwAdXkMj_Gje3eVMQDhkH7kEp62zsz5Pbyvej0qfN6qEdSbO4DCz3NPlqvv3MP14AEGpeKbDokuRkkCrRaslVRzqbynJb_QuMCV40njWr8S7ep_OL1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش حماسی خرم‌‌آبادی‌ها در موج ۱۰۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/441254" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inWNkl_YoSQtNWq0hwekJfTi5icGWojuj2pPparsgPEjwu1Xw5Puoso1FcAlua6eAMA_Xs0l35SL2wQvH2exTmnS82AOg3M51r3PCS56ZIi_AFhmvihqUBohZmKVnpyHfmHmzWD3UZCPKJmnlkJLO2nY-ZvGKQVe4qGOSk9V6Y8G0Thi9zrrefYBkzRoc8g0KBZVALekHVTgkUH_GZWIaR0tzV-qH1bHZ-PDUkWUNgeYvqx_viptlLBDW_Fe9luj0cpZINd4_Uca7_xK9TE2iKQWxjh5TrrBpSzF4Em3tmHU2Z-6CgVub_ShqDj-FF0TcaZRqF0J0soChkvPc-V-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3lxGZPvebZ1YVGBQzdVxTpoPSxn2U3imIOPr66-WWaBBgM_g_aE_f6uR6txc5_-BjC9Iu1tFytluJI2ppUVi4gCqzh1pn5_TvfFgZGjPmbIa40EJYZAwXKfL4QVJ06-4e4IgzOOYn8nBMI2yfgtOQs7AcXKCM0SA2RsskpkKong8gTun9uxyNUnJgffGr76swYCDm_bQvpzMq3PJ6zwQyXo0GiVxMOeist7hIEdyoUjkNi16ihFJdkpPMx52HsmgDZciYjnq71aFAUArL7auwqexLZi8qtN64Xff6v4zfcH1B0wHzkjp120Lpzr71MIlxncitC1i4Nvh6DnAsOddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM_zYscHY17DGxI86PTOKx59XNhOfgfnQV1y-Aah8fOwZhBvgltLjJKxN-KFZahUby2Ustu7Ih_W6Kbb3CQqyNj_8SH1NyQveJRIe1PzUFvMrxR6UABGMk3epBYjpPAh4T1h-lR490K3Q8o5wTjJWmgoztAAYVh1qWI7EOyQ9pwAbq_tVp1eArj2rG2ti0VFWbPs8aS369FEG0knODyKKgJV_shEe-9ha2XdiJ5WOrXKBRtEKC1qA1sx_EYvwUXt70FGMOOkKKO4jpHJU7H8nV30H4pxgL3BWg4WeTPJf3PiZPuhKUJ9ChRTO1Gkb31oxbkub3oozcSs0kfZLQ76EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCqlPuiYUcyWV2-iCiO7iEUhsYi7l10NirYu1GmoJUrlKbucKkYCSRhzSq0IiSpYG7EO6ZDJBUaAEKE41hBv2IJo_eHRKIp7DG1MQls_L7XylqvNesqULLeUZMLGoaMvOIQp-yAXaMogkQQFkzO8_ZoF8pK8E4cAR8a_buWE5iRKZ0RmhsbX88E8jvm6SDwV8CzRrbohOy4gQpmQ2Do7iH8koDCF2csW_1EqWMpYi91IzPwvQrbMIp5EI-77lqtHImYQmBGWVF-5G0AaULMZ6gOoEKvELsNuK9dP-_ydmNmOLf8lt6KBMMzPCUM-81poRSvyj97EWaKeP8vN8qejgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6t1vcsP_Xq_----OxVX7Et7RIlQcqBqXl6a72WBXxuGy1HpBgrxqf8Q7AaAJbkD54Bmbkak2CSZuEzTPHSVNmXaK3EPd4sHkCzYOTbeOBv1Qpl-v7GGBKeSRSzCMvwVxZ9S8iOEkP-zjiuFv8eDn2F-slUt7olDXD49nTBgVxvrMWEMrbRDd93mjBu1Jrc6xaEZg7V1VESY1H4f-fy4GwIhvM_NW35W9djqSwVHyKHL7lfItaGWCSw4psqz1dNnKBiOfYkWwR6ZA_9SrWccg7G0HfXpaKZncmnV19xI4Yx0vEgnBp2gU7ObyxmtQG0i_cnlHDQ0pnXB76nHmDgYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9rOcxHsxE_GzPew6BsKaXI_Z1C1l5gpwYUaWQcXVqbabfpBxltMYKnsCMcFYaNQpd8T07Gg4GIbQ07r7yWVLpqC8nwRy9fRUoK-lDXFQIH5Yy9X1QCiKWmM69QmFihHl3QWFlP2OZ1RU6eY_pQokOf2EQgjy5rHjUMkxwr4JTPsAr7pPCjyTOMCx96wEUu7j8kSgZmQQk5vYjxfisIaZKZl4Q4Grl7vfFzjOeSJsmBxET8qXk_5cIRTat144i87b9fXQMcaMs0TvHqHyPvB9Z5lbRj2rqz2dV-UFy_vJg-xWoEonOUmxjbte3GlODjb20gSwYrZ_zJK7al9hpSRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQSNejUthocO5wD1sAAeJcT4SXdKlMOkmtXg9M5EhLXr-m6QDh2QM6xk20FvPF_mLM8Kleojgxr7ND1M741jFh2KIQRK_V6aJtxPKyxl-5ISDCFtRAH730EN3pbX7Yik7qq0XukJJcRwpWvD9A2pDnVnwE8XqQVM9SGQz5XBULyqwt4-lWAmTJGaODfnwOrHZR_4xNRCCNhCDWVQbXVLXm8vBWEOqsZrAWxCcf-FLvnba4IMfGPW8_u8SKWo5bKZ9JLv6KZNM2cqtHkKizJar0tbfdn6qx_5k_Zk0AsZLn6HJgzKKUXHytoYQ3FYwSZWzmygC4MwWmUt2uctenmKcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گشت‌وگذاری در موزهٔ زمان تهران
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/441247" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ce26d886.mp4?token=ngBxbdb2cOwUqrWfH1eccpiKPTY_GB0ui-bpX7mPR1Z5UGEgNc-2Jaoz9biv3Rj0dyiUwfvLa4uSVsJMy2lKkOlr9X2yE8JgqhAOWdzl_XHig9-eotqHmcryy4tk2esLfAtWiabUi7Y7Wvi2dnDZI6w35Zf7a8wi_FOOZyFPeBgO8mcbvXcYixmIsGCIqeH9Wd2l38axnir0e2kPmkmd7jf_eBfLpertAA81odUX4xXpeg536XiYYUnfjWsdGn-51CZEsM3vvMbPlczZjCFNaD0lvW9XgNNoNhpEI1_dmtjdFNVKnjMPDc00ISi8ix-UXFkuuIq6HpN7sizT-k72uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ce26d886.mp4?token=ngBxbdb2cOwUqrWfH1eccpiKPTY_GB0ui-bpX7mPR1Z5UGEgNc-2Jaoz9biv3Rj0dyiUwfvLa4uSVsJMy2lKkOlr9X2yE8JgqhAOWdzl_XHig9-eotqHmcryy4tk2esLfAtWiabUi7Y7Wvi2dnDZI6w35Zf7a8wi_FOOZyFPeBgO8mcbvXcYixmIsGCIqeH9Wd2l38axnir0e2kPmkmd7jf_eBfLpertAA81odUX4xXpeg536XiYYUnfjWsdGn-51CZEsM3vvMbPlczZjCFNaD0lvW9XgNNoNhpEI1_dmtjdFNVKnjMPDc00ISi8ix-UXFkuuIq6HpN7sizT-k72uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروغ‌بافی ضدانقلاب این‌بار با تصاویر جنایت اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/441246" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94dcf0afa0.mp4?token=PgNKitqCSzWooYac_wp6_mX4fqesSIbP46VPE46ZMC_0vWX6yLii8w8fXZ3d98osIF1k4gXJBPEepms1GEcKwSzkY_pM93pWaW4m6NUWxeRDTCC5lCNQwO1b6-2NynzKQ18cPfPnuL_RkxfGpJMXny6PRUPS8JI7x0LW3Aj4BgVqCPtQvC-K3R27tEVkySIjSfpPlJZzU87QKQj6QvFeKqDH-xC0BEIbSKVHaB4aVdercXin38e1rV4MYIa5_WZM72_HUa20D4tEhJ3jittv5lednHKouvog1v9jaoWf79AwbHidcNj88CJZPTEgn97t5TlS0ZtU2nAVLSZxTbI_d4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94dcf0afa0.mp4?token=PgNKitqCSzWooYac_wp6_mX4fqesSIbP46VPE46ZMC_0vWX6yLii8w8fXZ3d98osIF1k4gXJBPEepms1GEcKwSzkY_pM93pWaW4m6NUWxeRDTCC5lCNQwO1b6-2NynzKQ18cPfPnuL_RkxfGpJMXny6PRUPS8JI7x0LW3Aj4BgVqCPtQvC-K3R27tEVkySIjSfpPlJZzU87QKQj6QvFeKqDH-xC0BEIbSKVHaB4aVdercXin38e1rV4MYIa5_WZM72_HUa20D4tEhJ3jittv5lednHKouvog1v9jaoWf79AwbHidcNj88CJZPTEgn97t5TlS0ZtU2nAVLSZxTbI_d4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم بجنورد در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/441245" target="_blank">📅 22:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae39f9353.mp4?token=J8NLdPb3r46v5ebEbrLtwJp3QJedBFDQqoLLs-BOOXsq9QXL207fbYRHxgi-TuTyzJqqQQIWWlDiMnourUYkhudTgfCsG2BPLcOdxnhherYkUo06IRThGuzlHkNveG1LFlo7Paldbbc9eK9rUW1SO9SZA6n39v56GDmFywXrRZ-Ax19qd5aBDoAK_bU1EXX-K_7pXlS_0wXcExGpaLDHsjs-tgx7HIqMiwmrdDkJLctW0x3AAcSsf0E3C5VIe8Tpq12aNqdk7dOf8hRiMvcHzCE-UR7-KMQsnC0eH63eBc2nJg8YA0WekbnVHDAnRxqoN6vj-lUnrBR6ONvSgdRibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae39f9353.mp4?token=J8NLdPb3r46v5ebEbrLtwJp3QJedBFDQqoLLs-BOOXsq9QXL207fbYRHxgi-TuTyzJqqQQIWWlDiMnourUYkhudTgfCsG2BPLcOdxnhherYkUo06IRThGuzlHkNveG1LFlo7Paldbbc9eK9rUW1SO9SZA6n39v56GDmFywXrRZ-Ax19qd5aBDoAK_bU1EXX-K_7pXlS_0wXcExGpaLDHsjs-tgx7HIqMiwmrdDkJLctW0x3AAcSsf0E3C5VIe8Tpq12aNqdk7dOf8hRiMvcHzCE-UR7-KMQsnC0eH63eBc2nJg8YA0WekbnVHDAnRxqoN6vj-lUnrBR6ONvSgdRibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است.  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/441244" target="_blank">📅 22:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809d557261.mp4?token=UKerPT9Dw5oSNQmNfqPO5TPj0jNEPjndM94nqmeAx20isLuWN3Tw0Tj0PNSmAuvTfEgIVj6UZRogpKZFWlyVEw3-_Yw4_qnrGzdm0A4wHUsSWVxegaTh1T3p4zn3CYsxZTq7KpZnXLUpcSvqIbELc5_l92Xe6KWpd3wkbbkwjN24wGPBIgltCWYGWAVaO3xJhZ0GK9GXggqoOitKk0kcadJzH92A-QS4YRd1rjb1Hq_cLhiGfCGARuRL0ttWMt4IrnXZ_eaX_FlXr4QokIC3BKfDmsy18QssPUFrV52toAasOXy-_ehdZJuvVcebHLuI3D2E_4StCZr5gL2enjnxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809d557261.mp4?token=UKerPT9Dw5oSNQmNfqPO5TPj0jNEPjndM94nqmeAx20isLuWN3Tw0Tj0PNSmAuvTfEgIVj6UZRogpKZFWlyVEw3-_Yw4_qnrGzdm0A4wHUsSWVxegaTh1T3p4zn3CYsxZTq7KpZnXLUpcSvqIbELc5_l92Xe6KWpd3wkbbkwjN24wGPBIgltCWYGWAVaO3xJhZ0GK9GXggqoOitKk0kcadJzH92A-QS4YRd1rjb1Hq_cLhiGfCGARuRL0ttWMt4IrnXZ_eaX_FlXr4QokIC3BKfDmsy18QssPUFrV52toAasOXy-_ehdZJuvVcebHLuI3D2E_4StCZr5gL2enjnxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور حماسی مردم شهرکرد در شب ۱۰۲ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/441243" target="_blank">📅 22:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaS7FpKAbT7Qni3TQu6ixCHgFogbak95qsOuGvhhVyfKV_1qx5bR-IELr3bdAR30M2Lw1ykb2X0mGfY2_-380zGK5eMiYJuAvwmBDQsF3QGb0WYS0Cc5tvem31ipk3oZV0NUE5Tr_oae0O4TNqVUaTeLRItQjCeTvdBa3QXztN6QQoeA5_Ve2jtAfnxwEMcRR0_H8BM7cbG64BJalCWVrttQeQbDcOwAzTpAH3KKDap25lhLzsvKWGmmAsEHlw1AGz1sbkJLBheTB-SHJjBEkTmuBl2pzOa4kw2ItAXG9UdJYT2SGSoEx5UuQAcuiU85xOcJRqr6vUDoapaggLGHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوسمار به پرسپولیس برمی‌گردد
🔹
برخلاف برخی شایعات مبنی‌بر احتمال پایان همکاری اوسمار ویرا و سرخ‌پوشان، باشگاه پرسپولیس برای بازگشت او به ایران اقدامات لازم را انجام داده است.
🔹
احتمالا او حداکثر تا روز یکشنبه وارد تهران شود تا در روند آماده‌سازی سرخپوشان حضور داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/441242" target="_blank">📅 22:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
منابع خبری از حملهٔ هوایی رژیم صهیونیستی به منطقهٔ بقاع غربی در شرق لبنان گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/441241" target="_blank">📅 22:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441240">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a70dd69dc.mp4?token=O6jZkXsz0YcspyLsrPC3lhqhWUIolZn5tW84YvkCKwZdZZseFJR-pppFK_dasrWvfd1jI6flD7lB1PCGhMnLB5-iopDE5-dTbf7V6m08eEQxkA4FbYtd_eFxyABqcO5F75sgYZqjRjvHR2B5M2cjQPwk3ChituJ8rp-oOXwUtNosSB9xNFlyAL47LnrBCuRgVbbjXdfVaIIXf9YVSLhAbdueM1NeN9-epgXTJ7Vfjad8iNhd0Y_f__kycpKqbWGWS5Ijgt3xfLv6bQubOhyo4vL6PWQsujqVRiXIbxZyd9s5EWyVOm6ycmiSF4X7X2XxyyRYKekIUiydouA-svl6QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a70dd69dc.mp4?token=O6jZkXsz0YcspyLsrPC3lhqhWUIolZn5tW84YvkCKwZdZZseFJR-pppFK_dasrWvfd1jI6flD7lB1PCGhMnLB5-iopDE5-dTbf7V6m08eEQxkA4FbYtd_eFxyABqcO5F75sgYZqjRjvHR2B5M2cjQPwk3ChituJ8rp-oOXwUtNosSB9xNFlyAL47LnrBCuRgVbbjXdfVaIIXf9YVSLhAbdueM1NeN9-epgXTJ7Vfjad8iNhd0Y_f__kycpKqbWGWS5Ijgt3xfLv6bQubOhyo4vL6PWQsujqVRiXIbxZyd9s5EWyVOm6ycmiSF4X7X2XxyyRYKekIUiydouA-svl6QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم اولین سالگرد عروج خونین سردار شهید سپهبد
حسین سلامی
🔹
فردا پنجشنبه ۲۱ خردادماه
🔹
از ساعت ۹:۳۰ تا ۱۱:۳۰ صبح
🔸
حرم حضرت عبدالعظیم حسنی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/441240" target="_blank">📅 22:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02fb960e2.mp4?token=qmTatjcC3Dqi8HJohVa5hfGTf-i-cmQXhiNm0464XcBlfyxp3f-m3L2kjB-6eUfEQcpmDd4cTScPxPOVrkXFs5Z13cuXY1NdvXqjwG7hRQla7iWsQ1NTnmPgFFZnj_JsPVmosQ5dE1PHpETWJA8yQ72Phg_IAD8hkvnumriWY747UlkF9RuB3Ei6iSfX0KjPWnDcobf9j9RDihyOhJZk0b29Bc8rWeDTRrA1i9LTu8lvACAOLmAh_4Nt1jbP_CCyJCcebxJuuqo8FSgjCEH1MJJuCriT9HRT9n43AlhMCeVZa6nBJ13LY-n51yBsjchdWvSaIYoDrm5-2xQf2Ig7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02fb960e2.mp4?token=qmTatjcC3Dqi8HJohVa5hfGTf-i-cmQXhiNm0464XcBlfyxp3f-m3L2kjB-6eUfEQcpmDd4cTScPxPOVrkXFs5Z13cuXY1NdvXqjwG7hRQla7iWsQ1NTnmPgFFZnj_JsPVmosQ5dE1PHpETWJA8yQ72Phg_IAD8hkvnumriWY747UlkF9RuB3Ei6iSfX0KjPWnDcobf9j9RDihyOhJZk0b29Bc8rWeDTRrA1i9LTu8lvACAOLmAh_4Nt1jbP_CCyJCcebxJuuqo8FSgjCEH1MJJuCriT9HRT9n43AlhMCeVZa6nBJ13LY-n51yBsjchdWvSaIYoDrm5-2xQf2Ig7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۲ شب ایستادگی مردم گرگان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/441239" target="_blank">📅 22:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_piwebNWnlowRgWu6W-YZMoTA5sdHBxuZVxDEFVeFdPYBKNY8afCoTdhOM6t9jNpDmE00p__jfFJlELJH1dcPtguUoevBJjD4tIZ6o6WeR9bHP9SkLFlwu8MhZooN7lRjo05IMCBu0Azr9n6o0VHJR2Tb3JmtFzOkJpL8Q8tqiUDczzbFbXX0ULFuZVo8Xeg_W4POQqSW6lBVfD_IHkAFx7BGOQ1SK33FMBjcfWwZ1SRpguN-QcMWkPjeZqVD4-3yf8e1OoNDiahSVH8-rbt8y3VrDmkKVkUfBuXlMUnRvcVa1nycIoYsgb_ETRdbNBrMOPYLgWtFM4HkgnRrUVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب گزینهٔ اول استقلال
🗣
براساس پیگیری خبرنگار فارس، درحال حاضر سهراب بختیاری‌زاده گزینه اصلی سرمربیگری استقلال در لیگ ۲۶ است.
🗣
قرار است شنبه هفته آینده کمیته فنی جلسه‌ای را با حضور تاجرنیا برگزار کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/441238" target="_blank">📅 22:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INKOqIokcIU5i7mdMcfEzPw316yhPWZaGlKlGUGq84XHJffNbUfkHfsHF0aRXELSLr6-YJw97nwZ9oF_zP6aBEzaJP0dTLZS4efan1JGImleBegLP2WxCPwrU5h9mSGE3I3z3h2WkP-y6D-_ubLoApxd_7TbrjTTn6eyQjrBGIdm_9YU-4Si0cGJAONQlpugCAqsuhoIReGSDyVkLuUZZ1y0nSSGNC_KjZCixh5bk9U1X-7KlcGSIKB9HLBpo_qK1H6AL5aLyUo08bRIY4_f1C7EtTaePmlvypB09u1DtgSJKaDvESSuvjbpcDNCx2i87bEEj-GgNnmzjB4JeYWMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/441237" target="_blank">📅 22:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441236">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/669589d65d.mp4?token=AxivdZ9Hu9CgrOGqV2T5Iyhs6T-63cnn797Bpvq4l9cr1Uh6hlJfhTG-SybcXeGeBAFcTpEiza7bFG2xxP82KtT919706-qHFXdH7X6OGkM4pGdo5Wc1_XcyMODCcu4AbSP5hjO66sLcjQ4ykwlDv6HJKSobTewcvEb6qB9nCnPsbMuB03pOG4QXuYAq8TZv8w2ewsfGOGhqzxdyJgKVOig_fDCOoVVPLTFQLh67SkQTv603TFn5CStmpyT7DY0HkNjLMPAZLBel3D4SYXuC6NVSsgI2Tp9uM3nCObCvKxpz5_ngugM1wF2K8ET4u3Wx2IZC5aSB0VqYa58Ikn4_q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/669589d65d.mp4?token=AxivdZ9Hu9CgrOGqV2T5Iyhs6T-63cnn797Bpvq4l9cr1Uh6hlJfhTG-SybcXeGeBAFcTpEiza7bFG2xxP82KtT919706-qHFXdH7X6OGkM4pGdo5Wc1_XcyMODCcu4AbSP5hjO66sLcjQ4ykwlDv6HJKSobTewcvEb6qB9nCnPsbMuB03pOG4QXuYAq8TZv8w2ewsfGOGhqzxdyJgKVOig_fDCOoVVPLTFQLh67SkQTv603TFn5CStmpyT7DY0HkNjLMPAZLBel3D4SYXuC6NVSsgI2Tp9uM3nCObCvKxpz5_ngugM1wF2K8ET4u3Wx2IZC5aSB0VqYa58Ikn4_q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف قرار دادن یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/441236" target="_blank">📅 21:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441235">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_j_wILaVmt42yrCMEIUppkJJXGOBTTzG-LsLxDwohdRSvGklc9MeMz_t8tEk5xSyrsF3dmZvvDJFGhM_WU1MEQGAJTYKuCksXVRTiFIrgx6FxMHtDmfwj0uNdqNvl1YINu8pVNVcSSp-72sezWg4q59dufeLYplNAMFWniuSSCSVH74Pi1Lcicbwct7VrVHGCC7Bo76gG_nF_dAcAwI2PQfVhrXjI5xl8wdIDysG43rwL4exCuw-A9w16srcpjpUEl5QOc9WsIi2obmpGYUZDaNQfCkwhXko8RS1LuiN4rmM6ErqtHLZe2hE4svxfS4VVg5mUmb7NBCHHLRn9pnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش تورم آمریکا هم‌زمان با کاهش ذخایر نفت
🔹
جدیدترین آمار وزارت کار آمریکا نشان می‌دهد که تورم این کشور به ۴.۲ درصد رسیده است.
🔹
ترامپ ۴ هفته است که بیشترین برداشت‌های تاریخی از ذخایر راهبردی نفت آمریکا را انجام می‌دهد و تا ۵ روز پیش این ذخایر به سطحی رسیده که نزدیک به کمترین رقم ۴۰ سال پیش است.
🔹
دیروز هم آمارها نشان داد، آژانس بین‌المللی انرژی، تاکنون برای آرام کردن جهش قیمت نفت ۴۰۰ میلیون بشکه به بازار سرازیر کرده است اما اقتصاددان دانشگاه میشیگان می‌گوید، این ذخایر تا ۹ جولای (۱۸ تیر) تمام می‌شود.
🔹
حالا آکسیوس رسانهٔ نزدیک به دولت ترامپ می‌گوید که دلیل اصلی جهش تورم آمریکا، افزایش قیمت انرژی به خاطر جنگ علیه ایران است که در حال سرایت به اقتصاد این کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/441235" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441234">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
جشن ازدواج ۳ زوج جوان بروجردی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/441234" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441232">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQdA5Ry-NqratKSHeqAfIXxUpWIrUtPtNmzj6ASGxTehALzXdQTkgRfHTBrDxUyjGQHGDbPf96qkaV5K6PO4-xYWwPUfjacAPPYZ75lcawcocAF6EpsYYBuCN-O0OVvi7wVAaXKoZRKTqYDpnDnSHd55PiroPAP2cmbv7uPMpj_2oWhomMqoYxMol7D9wmLFRnmYdMitXnMALuUEP2LkoEFrlrytkHQkQ_g2W03p-OomJI8XcGwJVviqkEg0xHKX8hZmgUdTRZj8zyB_vhIZ2SUu9lUP1SCSufwR_LoxcJrXNPEOc-i0Qcs4GKkU9SVqwQgCtNZe8WY7U3BbwYJ-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در عالم رؤیا: تنگه هرمز را آمریکا کنترل می‌کند نه ایران!
🔹
​رئیس‌جمهور آمریکا مدعی شد که ماه گذشته دستور اجرای یک «عملیات مخفیانه» را برای حمایت از عبور نفتکش‌ها و کشتی‌های تجاری از تنگه هرمز صادر کرده است.
🔹
​او ادعا کرد: درپی این عملیات، بیش از ۲۰۰ کشتی تجاری به سلامت عبور کرده‌اند و بیش از ۱۰۰ میلیون بشکه نفت روانهٔ بازار شده است.
🔹
​ترامپ در پایان پیام خود با ادعایی مضحک نوشت: «این تلاشِ به‌شدت موفقیت‌آمیز به‌خاطر آن است که آمریکا تنگه هرمز را کنترل می‌کند، نه ایران!»
​
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441232" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441231">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4760ea160.mp4?token=MUynR45MfqO0bh35G2fJCELMDe6I-GN6_yCiLQxqXSxNe904MXbAkGBTeRGjJtezo6uVVxonkQ8tWXOqLD9RDE1OIzxxj1gerbKLlYw7NhPLQewWZKeVzZwdi28402EKiX5nD3tIehrpKniIIHUi8zyeaX0ZSd4q0VyHhmV95cBeMHzxjki9rna-DRqWyU4dedgFLWQBcJUCMNqA4UeXB3Vql8QnKFeFVkqVanO_Hqxgr0RvGsn4nAGDCqZMLf54WcW8Liv0Cc14rMVjr2oRQ27jQpgJCUMlfQ_tqavXrskEUO1hkciLLQQk5iQeDMNb_NJ_bTC-TO58yr_MJ_0nuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4760ea160.mp4?token=MUynR45MfqO0bh35G2fJCELMDe6I-GN6_yCiLQxqXSxNe904MXbAkGBTeRGjJtezo6uVVxonkQ8tWXOqLD9RDE1OIzxxj1gerbKLlYw7NhPLQewWZKeVzZwdi28402EKiX5nD3tIehrpKniIIHUi8zyeaX0ZSd4q0VyHhmV95cBeMHzxjki9rna-DRqWyU4dedgFLWQBcJUCMNqA4UeXB3Vql8QnKFeFVkqVanO_Hqxgr0RvGsn4nAGDCqZMLf54WcW8Liv0Cc14rMVjr2oRQ27jQpgJCUMlfQ_tqavXrskEUO1hkciLLQQk5iQeDMNb_NJ_bTC-TO58yr_MJ_0nuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فراجا: افرادی که اعتبار گواهینامه‌شان تمام شده باید به دفاتر پلیس +۱۰ مراجعه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/441231" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lw5HO6neuhC9ma6UY-GBBJxl5kNqUy8yNjmU1u01Rz5vTfaUQ1xrug9NPBbAZUpOtRQTyY4Wkh4KqE_J7Z5Z0sGg7VFA9N4MUFJXkOD20aAh7L9af_jls4qE5eKKg2Jnpt5NmTZ5P1UKTayWcTjlUpTSNSgHob_EX0xlrt5hRLq7PJPCPK7Z68o8kH3-saQXSpYRfKz5B9g7Dr2pyuoRhZUdGD0SUPgq4k9QAjmyiBbF4LWb2TdcGpP9V6OeNt7b5hL3n8UGSTqZjx371PIwphxBfbbp2yE_7H-Q5jMewAraFsEWJTAeNlEQFLIkLn4bFlDzhIzs9bNLuARSs2b_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFgXVeDfvT_uGGLsvap6Z0jPJiWjRBejIjzCpU7IdzkK9fSTqLwVzSpESP92-5zveT18xW7AZBr1DD5MFtBIFLDsF0BxauVsCuEASm7RviYW28-_3MafJopeteQArXyAV-EAJSh1R9LMQ2kl8wvIBVrSz1-m2KAORNW57iS73EVLh8yh1dz-Cwp8znDOCvMiInHRKHoVtiAWls4yShC0lJqrhFYcsjXisNaF_Sn4j5-76O7s8kz4ugfFza4_hPATwFtrGpScq844j9Q-5cWZ-WVylwYdGEGNYepH3LW7itBS0CEsZQ-0ks97-_r4ikQ7bkcijYvJwudLIbETXZWdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6fzeWI0ec0xt_SNbQjyWVyOhAeTgRYUUXrzsjswy51lZBR_Ks1TolenQUsgfbDhAuV8-VYWGtIL42eaSe75AllneipmUbaa0NTlBuMDkpi3CQDmnVONowg7phS3iGS9uvYqW7cPFCUJx49tLflvy3anNPQaXNkaUTZNE2kh4c9nZfjN3XmdkORpjdp0cxf65Co_VJLEXvEWa-IAyoirzTQo9d3Na8ER-Hbrdp9_MYctrQ3RE1wwPNMaGbhRFf00PX5QQtEmL-mZPhU2U5RjXC_YSJOKrEwg-hQvb9bbC8nX-qQUeCTtAfiTp3BVhztZ89fZnhmO3H8k5cBsGiGSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQrWFYuvKuLWxOdT3kvNgIkjqcIGlGR04K0gk8z4kTNuUknRCQCZmMawiEjbNhDYdpjyujAbp1a-8mXbwV1atC2dCdZcZmeEi98m3ZF2KyFYczqz8QTPPxkL-DLFcmNg5bnm6h7v3j-cGhG1Ws1IXYXSz-MQqRw2A6fsVIaPgPcNGxF9a8GAeuTqmg2pFZNRzmkfsMlBYossuSG9w7MvVd5SRGMXyXYJIbBdEzXSxhRkM4SbpawQyAdo6KE-8NeOnddzfmhXIcy--OuQUQ1jbPusi2IDFZ5M8OPEuSE5OVKCSdOixduD3tKefqhGFk5JGIcbFkJIo2pHpOucDTteeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWA_6cgocgJPI4A4Mc2dxMvER-IsxRSNZdQDnWgNtuGpg2uTJV4t38AxAeR_vielAL36sEFX4Bd9yi8dW3WFmoY8RdY3rmVwvrdB5gOL0YeEA2C6Rn2OQw-SVMgOUJ1y3uJi1xBvzw13LSLV5dRnRO7CalZQOlsSKF3EiPDH4kfBDb_ADhadks6muqdGu4CGQytnk6Gjcd7fsvH6axipBauEKCGRLNAT7Df5tNI8Yqzd7hMW_1buaYZeR_HSgL6eT9zCJGL5y3OQnJrcVFwuelEm1dqoDACmAt3L_rBO79_rz7KOzUSx4X_mCKTvFCt6dlyMerTzWvWfPqocyPdLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrVmYiVhB7TYtGd6osZ3f5aUjb7ACfDZK-M0RggNUO7IK9BgY9ShKOhYEGbVf5j_Kb3X8S8VyH9SxFXZLLZ83P0R0gOFkpag7tVa_z7oAFH01MTi6xnwod-ZbNQNHnZLDvLBQjL-RcWCJ0pQR2QgkWy6GzH9l524D5KWi_Lk_cNBTYJdT2JNyQcmBBCQys5FzpCMdl_JrSf4jAfYvWJHBfIInMK07qV5YE1Hbzvbsuo_B03E-1-HyH66oWWNQj3PMeoWx9-6HWkY1Eqa6h6L_JGhqS1hD7ftmDJSibklVV38JqLmZaGv1F0JUO2j53BE7biq6VZDhIg01KQC0jz0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDKoPmfqSj5WWRS6Z-eTIbtaorHKq2lljMl_t4q-xvolwy7XoVSbd3c0wEfiMj2UKNU3vt5b4GZp8rrevbP7yKaozj5CD53rYt2-UZWDeWCyzbbQbrIdN1apJQB3woQbMZ5WpA5oFbbifD2yDQscoxtn_c7CtkB_AyuI0rdb-8gfYg-SA37JPNrj5gw4fop89xvoSLuXbDfagee1m9laS_NYgvJ0vvpV8G4SVZZbL73ihc1f9kbIpFhvoCrNWz33ioWaw9vqldII414OzVKtU0JN99l7I6-idgxcBl58gMeSgngs99LpZEJtxPnFLxxvtp75rUCzO1NgHndm_hbruA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید مدیرعامل سازمان انتقال خون ایران از خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441224" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628a22c800.mp4?token=rqfPv7it8bhf6OQFbtj06ZuCbU7YdKBZ5Fcg0osjehDCJVLjFVQb5IH7Oej0dEVh41RQhRdjUpy8Xk4UoV2DFXsCZxOosR94iicRZggmjkbFe-e1N-5VUZbHa89BVziLUc05Djod2REKkKjri4G-N93VUCk1hbgmhvTm7x7L5fMJrWa7suM9x15Bzx6esfMqgFJflLgUm6i4EMLh-crqgblAUzofAtQ1NJhFLq6HLWOrEIjKbUvSUURg7p54dCZT7d2wpSiAejuXBuGuEdaPdWT4DcVZV617UwQzrLAvnOraReyJGHFXCkjtZTXKd5tXPieoYGv8LvSZ4NCXSrRNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628a22c800.mp4?token=rqfPv7it8bhf6OQFbtj06ZuCbU7YdKBZ5Fcg0osjehDCJVLjFVQb5IH7Oej0dEVh41RQhRdjUpy8Xk4UoV2DFXsCZxOosR94iicRZggmjkbFe-e1N-5VUZbHa89BVziLUc05Djod2REKkKjri4G-N93VUCk1hbgmhvTm7x7L5fMJrWa7suM9x15Bzx6esfMqgFJflLgUm6i4EMLh-crqgblAUzofAtQ1NJhFLq6HLWOrEIjKbUvSUURg7p54dCZT7d2wpSiAejuXBuGuEdaPdWT4DcVZV617UwQzrLAvnOraReyJGHFXCkjtZTXKd5tXPieoYGv8LvSZ4NCXSrRNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استمرار حماسهٔ مردم مشهد در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/441223" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHTzh6UAP-COFZpoyTHq5-ybxJjWjy5nrTAyDCOtWBcOhyvR5Skj63YbMaZOUIGitJMMGUVUpmkGuX7-t3hId-1RZgjXJZmPIvA-QrGpti4KtSz6MjZx0UH1ytVwtnvNDBwte8llhsR_YzllhKl1iOeejvHaZDz3n7CI9tI8gEiq3OJWNbsp2ShOEOGhETH5kyKd8eCkZ2TfJxcTpVqKMszWxD2DKuPkMa3Au6JJN636_kMBB_sdZWuu-e41F6MxmnHVmTY0emL6GtKXBIOHvPUSQ_XPyz8u9vzdcRWwttGppbSzjV52kny-kXtkNstuYdCj-QQiah09tPwYadP29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خبرنگار: آیا به حمله به نیروگاه‌ها و پل‌های ایران فکر می‌کنید؟
🔹
ترامپ: به تو نمی‌گویم، اما می‌توانم این کار را بکنم. @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/441222" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtvOIhTLNkQc7TshB8ruw2m6PlFL98Lw8PUAekiiqKio_0HOEq0fq8w1r-ZcWz0Rn-fIxpTO88xPUp1sylytVQsMxdMEAzZjZqtAPw4OHPeRumqqnpxVjghP7tI_NQE-OAZSww1VXm0RvNAsaHKPDikZsmSYu2wXXrWZXf--J747VaxjOSAZzO-zhAzesqKkoLLy06yMB-M0DPEvQUF5hkNq83X7xaJrFEyGt8QrfGJrGo6mBYvAWxh9stA3lUFleWUOBZFSV-qVKXdOYwubRCrKlCU8i2EcLUNssy3nQPck1yQAtw9d6N3rtgVJLIwWK8Mki0ed3e0EfQPRcJ9dJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیل وجود نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/441221" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONphVNEBZomegJzNeq0xhBo9q6dyKPsP097SskrTXk41G__x5o478DPP5gWREa9p-OfWq9bAgqNFtD4VxRrmqCeswgU71MOIExopVvWVCyXmSu5Y4igRwbR_6Ufxrl986FWvX-WUVIUWY5IRuqIMpREsZSgWkMjO5ixVhhz0XKn0Dj1KPrSCPdP26YMEwXAsPwm_lFOXfYKxzFiD_3xq1C2KjfjcVik4qg527a8udoWvsEBgTqCgeqYgIJ72GmbPrifJvCDTe3_2htFXNynjOmiahS8EjCvayBSf2W9U-5vdjviAfIfVRWOLoqPLz0P8Cwkh6R9HUYdEH13BOY6Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علیه ایران سود هواپیمایی‌ها را نصف کرد
🔹
انجمن بین‌المللی حمل‌ونقل هوایی: اختلال زنجیره تأمین، ۱۱ میلیارد دلار به شرکت‌های هواپیمایی خسارت زده و جنگ علیه ایران با افزایش ۷۰ درصدی نرخ سوخت، سود ۲۰۲۶ را از ۴۵ به ۲۳ میلیارد دلار کاهش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441220" target="_blank">📅 21:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7tZu2weZNHv480f32OFISQCFFwN-e2XN7U0zHdDZBFpfVcQqrL-ZBqACNCHm2xXMzotk4fwXG2QbASvj3e9hdZJJv6JKQQij9btDCCtMgG2W7TmkvrkvPpza8JZFRclWd-J3JkqyHnKrxA63U-gg9Z6loHvbQv_Aa1LV6WlH4FkNOi-F5Wko4Q43BXABYmLj4T57b1IeKCFoZPxht4of8MZ1TXImqR-Ft58c2tnOMK5RbfcFw2KT21jmqztcJqTt2WaDvnJuU_z08Bc4Fw4L5kUQoRzOVCrwGzLd2hZdesXkhjwpZQ8MuaVm63BsUkg6nqBwNoMhNC2T4pClRUGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5r5FBqGxeOhmwTMuAa5kxEFyFNEuN2yWw74fqhM7c4-xhNJ-pY2v95_A5bxtgLlkliaCePFPW1TXfk_7Yc-a4PxSGMeODJ3LjUD8hY85HXyzqvTsEp_LH9m0o4baI0SU30GdTYpdEutVshdgxEJlTqg_W4bI3TCwwVmN5GUdDVg3ip637H5piegxTy2bCL-mkzihSLicGFECHaI2yWpMoy4HVg3af0ZaBsNaQfroenMHYRWARQUXd43eiP-mnmQCm9Euh6gSYz0rzqRV3EvYmycY6I1TmMeoyd-r3bJZTwsNkQz__WsN2-O6SUz_JTH2hx6Asi6oGSrG83feOJtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srs4LyG1d_ZGpwEhMfBAabHYIYezucSbFjQD-lFrihDbYLqi-RZ1op84km55HZGNbSSRUJ4VTWv_LyY3bentAd3pJw48KGv5EnzVZWm3h41hahMYeSKsztz9CY_QuWJUKahXt9U9NAaOIG7euguTM_XS9A2ciXa4KXbrM5BpjTeDZMURet-0UspCfs9dAy-fD76K9tYVbJO6-MbPvKDbV4swGh7qTKIzdAgczIV9EVicyuOZuDUcWXAAnrHgVLCxoTe-b6mpZrTxZIY-XykJ66YYDkyrAHiHaJAildUS7W-ggfloqz62wlTztA_3bkHEKteQSPnn6YYHUvctgXNFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIGiOsnEfGKPTQO8h-5LA26xg09-ThCeNxIy-mh_6gQ1dTJCMTE2YHQ62uro7fA8OdfSq4LL7bgUSv1Ijpxix2CLLxu79XXI_37p1o_xmrIOkyeSJYq5bvKkh3OFfXzAC5yrFvYeTeY6_a8YM5rd9TztYRTQ9VT1Tc0HKXzIgyYwOqkbP3MH8cFIO47FpYwyOpBEnbV0fiHZ7YfLUd_jktXU0rE66tjOpIz5g2K1-Hff_wTWPNyyv9pxzCRUERRGSUwQShvInhuDr2kDQbdZbBDD4hF-ufT3gIQIn2gyfJ_CcQLpOUEUMKLma0ilOVnJL7J3tm872KtZZtKyVQ0j8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf1lVRvODw_5AY19oE8yaS1a2L36EKHh33BhB8yWXeAEuDldv2GJKrMHSaSYIHAjrBpwCzpEFMJf3467I02BE6Z8iRc1eM7G6ZtzxC8ymeWLvzuJwQSvcBcNfPioBCYDgXqmCS1JomFI6w6LrkLmVRK33VRrK_C4IUwSgB7TdPkNi1VQI6ODeGWaAev2sjTrVk4KidDvuXzWUY06TyJ-5nSnFqjFMWmGPvnEstdhbPyNlS6_pKS-BX4BapKlpQ_jwpnAt-h60Lp_5ShBiBg7wqpAXdOOXvuWhJlgJc0UIrxbLiusjsd-B7PGmnkBw8AVjubfi-55LOyU9d13OuxPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWHzfPHyqSzL4yr-TR7tf3RE15JIo4Z5xB7gCbHTweQXS2ifJ81PYofhtkkczKz5l9bTKrUS0XYhqDr3I2uPiUWjOMKzyCGFoBmR8rAFSgVM8cIIJwCf3JvxcFWZP04OWo5dCf_2rM2NsICAH94CzUKMGD1KdhAvC_iF80t1otHdlv3xI1Y9FAvBGL_3W8I12rgvMIcKmOC7lN7OL5xfvuLv77ZvaR2857LlFF-BM2CoRlW8mhooHUpuD1LGWVUrDPI0CQVJHK38Inl2Ur0jygsZH0QgU0ngBLDkmghkZ1cmSg0h450Nq810YAHefXZnLZgXRe2GQnCPWfS_lHzIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urLaJCPIAe440AFGVX70JD8DICoo_bWkho_QPyIvcrDRFo2S4rx-TFIlWZ7U9orrV1IQEeZ648OaJ9TxZ9b7KUtbpvtW-iPbK8tskIIJH_5o15vwzo6aSORGcCo9atX6i78JPsHjg3AJhri6Zkkojz7pj3h-696uBNKEN3RgZZvv4ZV2BtcWEbI7SbMO0h1mD_fPuCMpKRpMMn1qVFbxu8FMEAsJFxhnl-d_C1QTiZ5z2DzpM3cS2iUf4vpIqy7wZGpmvk8IPenXwFTt2hubgCAt9BXfTbb27U1yHF9z-_9RWbLM7Pu2tYQKCDho-3-hdsmc5eg_b3JrWr1eZrmlpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس شورای شهر تهران در خبرگزاری فارس
🔹
مهدی چمران صبح امروز ضمن بازدید از تحریریۀ خبرگزاری فارس، با مدیران این رسانه به گفت‌وگو پرداخت.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441213" target="_blank">📅 20:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سیاست تکراری آمریکا و تحریم مجدد ایران
🔹
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441212" target="_blank">📅 20:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9I0gNginCMQmq6qkwdbVUmYlFzV6MqmCUPLrxJSNpltxW9EXE4_GGHXE1BnVuSnhqfTSFj5DFGz1rD4iIiaGwoB331hBnei4cIkc-tC359MzPdKWdPB4ek_tQ-33q4eDkU0Oq46cm7Xo80urcddvMdp_X6tvEwSLi1yg8GQGjp3wtvxgdU_ObX6nocjkbppHoiEdzKaiEc1z4-bFxbAoOQwn7rLloHP3kJl5g487BnInCvcSv0jC6x4mQcYv5CFZ8syNfuGO7AlMUyZ7veKokrdRcqu4mSM7oEifON8sEfexr_-94cjhtGlP_i_bZ_TXPsn6hSOjfZMlILEEcjlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: تهدید به هدف‌قراردادن زیرساخت‌های حیاتی نه نمایش قدرت بلکه نشانهٔ استیصال در برابر ارادهٔ یک ملت است
🔹
ایران با تکیه بر دانش و توان متخصصان، وحدت ملی و همبستگی، در برابر هر فشار و تهدیدی استوار خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441211" target="_blank">📅 20:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
خبرنگار: آیا به حمله به نیروگاه‌ها و پل‌های ایران فکر می‌کنید؟
🔹
ترامپ: به تو نمی‌گویم، اما می‌توانم این کار را بکنم. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/441210" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441209" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر القنطره هدف پهپادهای انتحاری قرار گرفت و در آتش سوخت.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441208" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441207" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4bI8nr_QISTr9MJxGWBQoLtwGEuTEgf3kYQMJGMPF_5S1luFDOWoPeEqJm1HsOeT7nO2SLWE7SJh2NAimkZKiN9eFtSKu_aikMliHrSNs0o8ElGCuARl3ebhFUvTNtNtrHNRsNzHxnMg5Tgo-eCTJV28k2lxJHmW3ABKoV96esEJFblrXzVGQfhyqutyeWpKbnh3fjG61RW3n9q3ofXxn24JAqiFxdKH-8S9RnYulQY67h2W3btXkCvzB5kwzrlXasF-2zkeFbwPzPL8JoLRb2myAI-U4trSJYZB5sMpu82iSF-RUcKwo3ILhQtIXACSFdZCzui-plBuN5QTLIYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
دستورالعمل پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری ابلاغ شد
🔹
بانک مرکزی ج.ا.ا دستورالعمل اجرایی پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری در سال ۱۴۰۵ را به شبکه بانکی کشور ابلاغ کرد.
🔹
بر این اساس، به هر یک از زوجین واجد شرایط، مبلغ ۳۰۰ میلیون تومان تسهیلات قرض‌الحسنه ازدواج پرداخت می‌شود. همچنین در صورت احراز شرایط سنی (زوج زیر ۲۵ سال و زوجه زیر ۲۳ سال)، مبلغ تسهیلات برای هر یک از زوجین به ۳۵۰ میلیون تومان افزایش می‌یابد.
🔹
تسهیلات ازدواج مشمولان ایثارگر نیز تا سقف ۶۰۰ میلیون تومان برای هر نفر و در صورت برخورداری از شرایط سنی مقرر، تا سقف ۷۰۰ میلیون تومان قابل پرداخت است.
🔹
تسهیلات قرض‌الحسنه فرزندآوری نیز برای فرزندانی که بیش از دو سال از تاریخ تولد آن‌ها نگذشته باشد، به شرح زیر پرداخت می‌شود:
▫️
فرزند اول: ۴۴ میلیون تومان
▫️
فرزند دوم: ۸۸ میلیون تومان
▫️
فرزند سوم: ۱۳۲ میلیون تومان
▫️
فرزند چهارم: ۱۶۵ میلیون تومان
▫️
فرزند پنجم و بیشتر: ۲۲۰ میلیون تومان
🔹
این تسهیلات بدون نیاز به سپرده‌گذاری و با ۶ ماه دوره تنفس برای شروع بازپرداخت اقساط پرداخت می‌شود.
🔹
متقاضیانی که پیش‌تر در سامانه مربوطه ثبت‌نام کرده‌اند، در اولویت دریافت تسهیلات قرار دارند.
@refahkhabar
‌ | بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441206" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشهدگیفت | محصولات متبرک و زیارتی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhM2lxnC-ZNoS0UB9xtc6sBciuXqxy1GrjYiPHv0m655vsjHOFP6AckBp5--EYBWatpfbKwIhJtMqwHxsXlYqr09-Rskan4hzICxUpwmcIJNyfqxI-YQ1i1b_JJZswr5pEPbGoER7cp4fFpxDTHnpDXXpBFfQJ7f53zFSrWAGEpY70OYrPEhMEAnt4wH8Ei_ysnkAWhboyv5Lum7hKcuFqbOdI5mEDSaJAzthK4EfvpSu7y-xdafWYtlwj2MD_AOye1XC1zV5sfjUyiYJr6YbS2bHH8a5X_DjSK_Yak_icds6IFgDLCw04AF7h_7IBHRVORGlbZL1qawwtfj8uj3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهارشنبه است،
روز زیارتی آقایم امام رضا (ع)
روزی که دلِ عشاق، بی‌اختیار راهی مشهد می‌شود
سنگ روضه منوره؛
قطعه‌ای از حرم مطهر رضوی، برای وقت‌هایی که میان تو و زیارت، فاصله‌هاست
✨
✔️
دارای شناسنامه اصالت متبرک
🎁
به همراه هدیه
‌
📌
بهای سنگ متبرک روضه منوره؛ قالب دایره 480.000 تومان و قالب مربع 380.000 تومان
‌
💬
ثبت سفارش و ارتباط مستقیم
@Mashhadgift_sup
🔗
برای دیدن سایر متبرکات به مشهدگیفت بپیوندید
👇🏻
https://t.me/mashhadgift_com</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/441205" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/441204" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441203" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران مدام ما را احمق جلوه می‌دهد
🔹
ایران مدام ما را احمق جلوه می‌دهد، چون با چند رئیس‌جمهور خیلی احمق سر و کار داشته است. خجالت می‌کشم بگویم چند آدم خیلی احمق اینجا نشسته بودند.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441202" target="_blank">📅 19:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441201">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441201" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
پیراهن‌های ورزشی شهدای میناب که هیچ وقت پوشیده نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441200" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRxcUWaAWCvO9jhS7nlNkCD-kVPY8PEJwHGAilyZaEJCcGEbRo7ERRJlfcjNcT98MXcriAxT5H6dGYtR6sfefsIFt3kujS-up8ycnmaLuLbxIRg3hK3zE5_s21Gq1l2ILGwM6EVgbu_E8Agx4K_oKus0KSBNkpPILs32FjMGON567-Pakp0zTrfGvnJKXicvpQT7_X0Rd8oNR0qI2kPnAf8-cgdSUt45e-GO9gBJqfhyYp1Il_kJ43J70gXdKDtc6iRDg9Jiv2JSYMF5nMtkcl5u1UNtzhdt3hRID03VPKMHiYZNojqDzqnp0dbtGm7vhOfG_4rihRLW2bfR-cbvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام پایگاه‌ها صبح امروز هدف موشک‌های ایران قرار گرفت؟
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441199" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ1DiOeI0opDSByyBMr_V4WDNIghUXjLPT_7N_ZiLklVPBtfV-SB7YP1EJCSJNz6VT7nmBcrR2Fh697_XmIe_68azu-7D5SF4eMTUaicefI4QvqvkltHzUqyYP7quK2KyS7cr5OZ9r-7elGZrKYd0dJ8tZ6CIl2FslFHdYRlEz9wp5UxSOElKdbP0PNztoCnpcMPqVZAL_ORSr-q_Hldb-4tImHcJSrgiEwPdsO_nfwOMg_lDt-5UMfEuu0NZWE4Rl-bwxaPEOr5bUwsIspWcMHhb-rjdkxsYyC5ZZcoaG_CjQR7blsgmPcbFLIFR0AaqlaQlyO4-aWg2YMq45dKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک هستیم ولی ایران همچنان تعلل می‌کند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441198" target="_blank">📅 19:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7dDTWydp2TayUSt8UZkYXPQ0fZCGye2_98YPywV8atyqoaeJvg8AJryE1KR3dv40e16DJ0Xu3OzpHO8OiL7OSqGEWJSfcFuG_OAIPhbsobYsT0OkkM0bBltaATgP5KZousupwUIAyprgOtOuXoMbtEfssQhTNKAKNzAbqrPU3lNbDpHJ1WoO849ZXfwPqkm3AVG5-Lx1-Ku4TP-EyM-nl77Xqu6jzRYXFylXAK8uOQQKgC_Q4mdwJqzGKyfTQ9GuYVKiOFHge7q24m9_YAWcLzslCOJvnlPfl6KWspThlAANHi9WJVr-j4mIjV-fsIVJlCiQMsrEN3d50eL14rDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ نظامی، یکی از گزینه‌های روی میز ایران برای رفع محاصره
🔹
در کنار دیپلماسی و توافق سیاسی، گزینهٔ نظامی همچنان یکی از راه‌های مطرح برای پایان‌دادن به محاصرهٔ دریایی است؛ گزینه‌ای که به‌گفته تحلیلگران، نمونه‌های مشابه آن در باب‌المندب و خلیج‌فارس نشان داده حمله به ناوهای آمریکایی می‌تواند هزینه‌های سنگینی به واشنگتن تحمیل و آن را به عقب‌نشینی وادار کند.
🖼
اما در صورت انتخاب این مسیر، سناریوی حمله ایران برای شکستن محاصره چگونه خواهد بود؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441196" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucmTpWt9exGjLYoWsbKCLFhEo6wOrxSpNe6Wj7xRfMys-_PAs6BGIxmOBeTC3RTVjRcbutmFDInSRHPFyBB9D_NQBnJvmmSBaYJqOXhTbSfZVNAi8OBEWn2Q_XnqtrKLA2xff_xQXZlsPvC49EGCvVQtY9o5a_B_8OiD2WKfjhrjuh1pA-_6Nk3a_pDAb32mMUaiC8BOISZcHAKbtQtSq4MrbsuISMm62yMiP_IDkV9jhS3G4hvl9Jh9m9ExzGlLYEiKX40GOL_qOcVFvZdiBCEUMyMPoCxoCRJuSjdx8wpriFFxo-GnsV1-bnXE4R62P-FGTbMw5Bul95ci6fystA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت سفر در راه است
🔹
مدیرکل توسعه گردشگری داخلی وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441194" target="_blank">📅 19:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441193">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636c92e66e.mp4?token=AWVidr9zIvnAJP0y3hs7UzHwXUvGXYIjyV1ECjgufMEeQ8ME3UCZsrszF4YEk6XJh3QRVVudd71FvKRZYs9g6EEVxo5ZR-omm5vonRUTmMWerJSgCXq8aikqYnq4jizFw69bfuaILJk52S_xMMaN7w4LWSmjjrV8YCcRrqzAGSGm_UFgmAGr_bGGbwqedJqYqo1kS4XSmxsRQlCz0q4EImRiXtc7c-gS_0eXBtjhTC2QXelS1Uthd9PFE9htilLBs35p-DtaFNmipVG_SFewV-_TtDzpd7AINWUM8YvxdqaEMoBmhTIpSj8sNesbB2F0mEnTzyU4igKL3scnCL6IxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636c92e66e.mp4?token=AWVidr9zIvnAJP0y3hs7UzHwXUvGXYIjyV1ECjgufMEeQ8ME3UCZsrszF4YEk6XJh3QRVVudd71FvKRZYs9g6EEVxo5ZR-omm5vonRUTmMWerJSgCXq8aikqYnq4jizFw69bfuaILJk52S_xMMaN7w4LWSmjjrV8YCcRrqzAGSGm_UFgmAGr_bGGbwqedJqYqo1kS4XSmxsRQlCz0q4EImRiXtc7c-gS_0eXBtjhTC2QXelS1Uthd9PFE9htilLBs35p-DtaFNmipVG_SFewV-_TtDzpd7AINWUM8YvxdqaEMoBmhTIpSj8sNesbB2F0mEnTzyU4igKL3scnCL6IxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری جدید از جنایت آمریکا در مناطق مسکونی تهران
⚠️
حاوی تصاویر دلخراش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/441193" target="_blank">📅 19:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwfUzKi78_EOVyusdCbvbw4R7hA5G6wnl1_iPMUeNfChWP6xYcbMScH1h0JbzfBdaGZj7UOarGBWEQXmwY5p9uRllcNa9PmxWJCfs-3iBboaLCTUUceN7nz2WyQFD2OnahPsgtLbmFgms_xWaaowco_BOi7J9WB5X-CidxBPvt9vMWOc4YGLlKo8QMTw6w9tSNh_YycWHkTJYm5sCdhrKqw0m3zvwFqUzWZppXu34F6SAZWRzl2k-NdiOSAttk6sHHQEyZ0WNnIK_hJCJQzXpLXCE0x3u07-9l9aE6h_tQzeoLU0u0D604E7RhjaixW1smYKPHadM7kjrunxqaWOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suYMhaUwXHbRrKcH7K6sEEp3F1tIS48TxxHR-J8nTOKm1LIj1_yHXQ4kpLDGgj5R1nrS3Df6rU2kXFgajw_Bq0VVN2NhUxLSLfIF8sQsQ5zCp4rqJ89lg994NxIFsyAvPxHMZe4izMEy4J4leG3UyzDl7kWgCkkObFtSh5sheufzMuDW5dbkpYo1Oq3W8QymQus8_17mMRJUSCa56GIBoe3UZ94MEh202CTaS1fBrV7PIoAlbzWZAgZY7k4r7fjJducbL_bdKyZPStr4CWzUx7R7fJfxuPLIUlqNwyg2wOQInQtX0aC9xHbCVOm5p6rG4d_jW1l0E741ERU7YyyoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUcAXjMBulNHof-JNs3ZQpx6LO5YGLdIztth0QweNSoSQbxbnQyQbjpXvTXR2XbOvGM1epX9F9Fi9qkOZNJYjM3cRHTT4Q0mc9-Fr_BOBO2MLbTqJEnTy3LQxQBsPS4EZvuHYURL2d3O5HK7R9bVH2x-KmJdyik8YEaqC2Ow-86kca9JggInV5d1IlJteC_kyvmz_VoQkmeIFu45RKVIqZ6n5W-PmlG1iK_yhPMPIj8TTu6UVpnG7zn2LFrIT6DxZxVImaUWCFm49u9jL0IhD4XXKgUdD5yptOLNAo46vqMKo_BUHwuNa1TTmT-qFZyayMbrF0I4c5F84duIo7Z7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yiuz_LcEHfzDYuc5XR_ySGX2Tfh670mBVODjCWQOSQ82eTWEvA_bGEE4QW8egUFMWKa-d1XAn6zQ5hHUfSgfw-nvr8bP-E0sodMgU9sbedngOgrRd3g2-S1lbm1l-oryiGW7HEGlcjKauQS3VWxuEyhmAsx4cgymFDiiqbhBGG4b5jJtHXFDcAe8vOaZ612A934tdXpNRQwPGHuSrdpVsYmQ-KLpPFDspU2-6yLL3WM-aa4mwkF-jdjCTNLW9izNcA2VtuMwYCPajcCksApqhG79WT70CMy2XE6TuJmueWnIJck5r9tjb79PNsEUjxZbz1ZSQtRx7Jr1cNs0WXSsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkFNO2LVK84Sg0Iu0E63W_0zVcFKGyFJj60fUGgx_pfb5iePFokMdisD188hkZqVKCFo8FPWVqUb5Y1-7Jrf8YTEjpbauYDQXI2IRHyIEWpXtX8E1e-4iP59jx79GK7xtxUz1ivti45-0Gx-5GvOjUgXjKHS-QvjFi_cWPAT6Z2tKHTyWY6hqe9UWbIU4AO_dyN3zL1APSFwEajQLxKOWtoy8yhzNRuOCLrD0PGwAJm1WotaTq4pOq-t6PRAAwnIX0tH06WbQGCxEUogdoEknegX8ACUXO4D_w4ZGSD-k7X2N7Eq-irneopL6-iPfCxGf-8ebqm6BxJLLYnIQzSmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiuSi6ncjFPnMsqBDSGRk6gtwcnLtcFwF6NUTHMyS-a8eA65qzJE87bF7D4Xn2hbJdivX9ff9JYIHDM0BGSIsRBe7_HmR6dgQx4IoWjkLmGr0yfsjSahxrxhbAShva8IRnoVIedut3_bs3o0VM99HMU_ZmlkDp05zsXaHw0lMM_u3e2_47QtZItQmUbAuLbyySEzDxJVnhxZhOV4uV6epMh8-6-JwU4HMRWRyGP9LIjL40ihSiWyuiMshBSKJdOqxqAXbfRSOZPPqaK8kI3Qv0jQ5xNVZeFcp1QIuLabORQfgEQ9xPcJO8fcYfU5bi_95cxcLw_7f6VeG84Mqn5OzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید رئیس شورای شهر تهران از خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/441187" target="_blank">📅 19:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHIeM6ArFagk4UW350j87JTlme8N39MYQYJYSQGvbRkzYQdrtaxLUe4EbC8AJ493wp-NiaNynj__irRUbNN_fNv2IQpUsN7K4x-UgnWcPf14LUGxOBIK4s2YG8pcCSOaRZydCF08BAlI50-4FmS--mIJ5ioc0xMoq-ESNSjCg3u1EtOOUGYmffaQixTZz43Qq1yzpsAF34bA9Mw99acNEj_9T0vL_4_k9YT4m3GioZEepwgdNsiqtYZZR1UTd3zmtco3HycT3v0WLezdZmP4GT4AOsnCp3rttvzOivxHZp78fc-z1ivRR5EGmOvYFSaNV2imNhK-QXPJDaEWLN5_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی: طرح تنگهٔ هرمز آماده است
🔹
کوثری: همهٔ اقدامات و بررسی‌های لازم دربارهٔ تنگهٔ هرمز انجام شده و کمیسیون امنیت ملی مجلس نیز کارهای تخصصی مربوط به آن را به سرانجام رسانده است.
🔹
این طرح پس از آغاز به کار مجلس، در دستورکار قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/441186" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df9792bbe.mp4?token=oTTpgcyNOka6IO75imktQawtiiEp8nohUXlG5eMjYGh-9mp6Ynm3jLfHX4jNpKGYT5uYfgNZtzUu8i0fUjxh4Y7zFRnWhQmm3yD7umwGfhqXPBK_t5UxHeynv5NgW0N_3QbgV_jUTTuqiAUqhTz7TWq5iWbjAwCLavmpRTKH7y9ptyF_CefJwux-DJV89hKcN4xHA2HLnQcYz08nDrVkUME-k1q5ldXmQvblYhWRAsdYCXjWMp5rNr52imOp7Xb3TASnd28Xn2T9iCmIqWGqDf3lC0amvn-POMLLPNKZg2ezYn51aR4LIj2_3cTCQs-4r-kPDTtGPkS_AQ5SapTrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df9792bbe.mp4?token=oTTpgcyNOka6IO75imktQawtiiEp8nohUXlG5eMjYGh-9mp6Ynm3jLfHX4jNpKGYT5uYfgNZtzUu8i0fUjxh4Y7zFRnWhQmm3yD7umwGfhqXPBK_t5UxHeynv5NgW0N_3QbgV_jUTTuqiAUqhTz7TWq5iWbjAwCLavmpRTKH7y9ptyF_CefJwux-DJV89hKcN4xHA2HLnQcYz08nDrVkUME-k1q5ldXmQvblYhWRAsdYCXjWMp5rNr52imOp7Xb3TASnd28Xn2T9iCmIqWGqDf3lC0amvn-POMLLPNKZg2ezYn51aR4LIj2_3cTCQs-4r-kPDTtGPkS_AQ5SapTrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری حریدی‌ها با پلیس اسرائیل در قدس اشغالی
🔹
صهیونیست‌های حریدی در پی اخباری مبنی بر دستگیری یک جوان حریدی که از خدمت نظامی فرار کرده بود، جاده‌ای را در محله رامات شلومو در قدس اشغالی مسدود کرده و با پلیس درگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/441184" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر القنطره هدف پهپادهای انتحاری قرار گرفت و در آتش سوخت.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/441183" target="_blank">📅 18:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu5MY86x4pJTiYK4EgESgfxufEa16aqUwIXv-JzK1vK2DS7Hu2GyiHwlIqc8iv9gEKUzDfZklEUWX5WA5c6znMb-qm81Z5Ao_Hgq0nlCrTArgFwxLvgpgICNJ4oLV-tVaDG1Bhs_SKQqXatphOP8PZwkbF5jOF_dvOphiVfb1zv0-mirepuqRjd6Aa9Flv5iDOgAhc5MotYvsiCXZT7ZUtAbr1j2zT-hBNgZ5dg6SSN3zt-qVUQB2x-8XCzsl4ribtUbYHcWwZ6kpPCtzrMM5MiNHihNgRNYyBBTeYMnu1TK1st8kY4xc-90tD3coBljMbrrBJKNqytyBE3JlHlyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی: سیاست‌ ویزایی آمریکا باعث تنش در جام جهانی است
🔹
مهاجم تیم ملی ایران در مصاحبه با ESPN اظهار داشت: اقدامات دولت آمریکا در رد برخی درخواست‌های ویزا و جلوگیری از ورود یک داور سومالیایی، به وجههٔ این کشور آسیب‌زده و باعث ایجاد «تنش زیادی» در فضای جام جهانی ۲۰۲۶ شده است.
🔹
در ۳ جام جهانی قبلی که حضور داشتم، همیشه وقتی وارد کشور میزبان می‌شدیم، حس صمیمیت و جهانی بودن فوتبال را احساس می‌کردیم. اما متأسفانه اکنون چنین حسی ندارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/441182" target="_blank">📅 18:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_KBjP3r20Y7D5xNOc_M9ICIfxduv9AtFYDK1P2LqgZwiR3yvYzamd-tPmy2EWybUMhBamVUYx8C0_0sL_4gGmiWZBoopW7KX0lfNxZogj2b6w1fAP2HHZgO0m1oYFfItJFQ29xyp4z87tRQq4LDm4TPcUCUj0uT4vE0-NAYkSBetZx5rTDIc2bamGWG7wlJVQdn5DmZl-klxxcvAXyNE2NlGT5-q820bjsK_wHavwJkFOU4soZsc7RKo-is9pwuNMLpPyJ-Jlys2DaGVTeXE1hv4V4EL8GUrkrPjveQfPr7LgI9JFyGAU2WIIFu0SPzZJobb1JzUqkqgixFdrkjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ کشتی محاصرۀ آمریکا را شکستند
🔹
پایش هوش مصنوعی دریایی ویندوارد نشان می‌دهد که ۵ کشتی حامل گاز مایع که با ایران تجارت می‌کنند، محاصرۀ دریایی آمریکا را شکسته‌اند.
🔹
ترامپ ۳ ساعت پیش در تروث سوشال نوشت: «هیچ چیز از محاصره عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است. ایران هیچ تجارتی ندارد.»
🔹
ویندوارد اما با تحلیل داده‌های ماهواره‌ای کپلر می‌گوید که ۴ کشتی محموله‌های خود را در هند و یک کشتی در پاکستان تخلیه کرده‌اند و صادرات ال‌پی‌جی ایران ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441179" target="_blank">📅 18:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441178">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0S7NIiMysvcOClfQ7AJJWe17wnsh3hk0fSLMcqbAtJ_RKxqZGHTAkyd4d721_mz_aFf4Xm515yOkHC_Ucwy6cWeso8rw36s1fh61Xqw-Xl2zlI67P5Gm37IpVTbZVWQFqkBc68DB49YzDtzH16355xllsbMyiyPNcU4B6dXViSrm0JfsCpSQjhOOgMBwdop_qGry8QgX38Plxmh3FUo6r6rC9ppLBUjyUYoK8aecgf7uzc3rIhcbe5TZ-gfzr36Yrd2rjyJ_pTzyI_o7vhgCbS0lL8Y4TEt_HBlanFA8wEhG5DKdB31auzrbuQw1YqCsTI9kbzIv1qguS6WBYWhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح: هر تهدید ترامپ را با تودهنی پاسخ داده‌ایم
🔹
به‌هیچ‌عنوان در مقابل نظام سلطهٔ جهانی و شیاطین عالم، به‌ویژه ترامپ و نتانیاهوی خبیث، کوتاه نخواهیم آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441178" target="_blank">📅 18:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441177">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
ایران: آژانس به ابزار جنگ‌افروزان تبدیل‌ شده است
🔹
نمایندگی ایران در آژانس: چطور می‌توان به آژانس بین‌المللی انرژی اتمی اعتماد کرد، وقتی به ابزاری در دست جنگ‌افروزان تبدیل شده و چنان فلج و بی‌خاصیت شده که حتی نمی‌تواند یک نگرانی ساده را دربارهٔ گسترده‌ترین…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441177" target="_blank">📅 18:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441176">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تصویب قطعنامه ضدایرانی در آژانس اتمی
🔹
الجزیره: شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای را در مورد برنامه هسته‌ای ایران با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع تصویب کرد.
🔹
گزارش‌ها حاکی است روسیه، چین و نیجر به این قطعنامه رأی مخالف داده‌اند.…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441176" target="_blank">📅 18:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441175">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njZONvoZThRC9EBfE_NBFm8TBx2-21qT2BK7Qc72Sxkw870T_vW1SvGZ0krI-l3_AJrrM4orJtLoZ6GnS_t9Zp9ts-whciKUSjvMbZ4ACkjBbwkjZbckjEp4tnE-U7koTVdW2ymoK9doSPi_PnqjhV9GVsKt0lbibupD7TyqUPt_-SaUGpp2p3W-dt4EHWd3Yqx9sHU77ikf1AE2v-QvAPY6hZnp4pQ412zL3Dy4ApnmQSRwOz9BgpFaRSE04phNI7wSTLk0apVQl8viAJK12nft_XQmF6ev2XvnTB4ro98qOqVQZdM5a2BJ_-u2L1iQruBxqY95Q2tLE1CqjDIWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز استانبول-رشت برقرار شد
🔹
نخستین پرواز مستقیم مسیر استانبول-رشت امروز در فرودگاه بین‌المللی سردار جنگل رشت به زمین نشست.
🔹
این پرواز از این پس به‌صورت هفتگی در مسیر رشت-استانبول و بالعکس انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441175" target="_blank">📅 18:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441174">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تصویب قطعنامه ضدایرانی در آژانس اتمی
🔹
الجزیره: شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای را در مورد برنامه هسته‌ای ایران با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع تصویب کرد.
🔹
گزارش‌ها حاکی است روسیه، چین و نیجر به این قطعنامه رأی مخالف داده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/441174" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441173">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3UuUBxejHRoud3Bu1ucu6bqBuPvYFW6ujZNtw2PqKQ62lwZopmmt3m7Rr-6EI-H_deSnT4CJPkYLBF7b0ZLbS_oyq9mV3jf-GMT2ZLKKYYJ_qIzapsNkG8FTeSUYVOV0wfDb8Rjx7phgmXqwBQQOOKX_0_ScOb_99nRerxB2jrJDStOYFPXFDuCqiBRx9alF6oLiwhT0wlY7LlhLqM5QgD1g3bJ-1s3c6L9AuKOSWdc6oKRf4nKf9SjfJ6u_LJ8tBlZ2TwjfiCTmdXUsoW7-hWlp_IXdKiqJySpWGGWLHZGbDaCvaHgvt3huBqE0jUUev0b_FhNMO5G3AjxF_rFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب پلیس برای متقاضیان گواهینامه
🔹
پلیس راهور اعلام کرد مدت اعتبار «برگۀ ثبت‌نام و قبولی مراحل آموزش و آزمون رانندگی» از ۲ سال به ۴ سال افزایش می‌یابد.
🔸
با این تغییر افراد در صورت طولانی‌شدن روند آموزش، تا ۴ سال نیاز به ثبت‌نام مجدد و پرداخت هزینه برای دریافت برگۀ جدید نخواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441173" target="_blank">📅 18:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441172">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
پدر و مادری که فرزندشان را در حملهٔ لامرد از دست دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441172" target="_blank">📅 17:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441171">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yWbJgv2QPoh46Prns7U-tYd7uhKAszOwGX9UO9CJbf2-IoK5HetRbr4vG5c6-udixJQIf7jOq5XxI_5ClTBwL6a1DcxIOBDQRmJRUXkMZKgqE0NbX6QMKPM3vuI0b7C9oxw8cSOOloStuvVOpqO_hXtbpjSSZ2VBqgjOScAAJFwwIq1aw06ksxAg-hKtYtQ8acBvsKEDptLRcqUfRCTMCF4GFOQoisGHtm_wGXJ5eiI8BRPZK-WZcR1v1HyWmbm9WmjOLV26qVIlAJd458QvFrAWRR8fn2sNTFEW45Yj-Oc3XFZ3Wuh_H1zLzQFSUwcQMwJHbcKPjYze_ctfYSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبابافی نائین جهانی شد
🔹
عبای نائین به‌عنوان سیزدهمین پروندۀ ایران در حوزۀ نشان جغرافیایی، در سازمان جهانی مالکیت فکری ثبت شد.
🔹
عبابافی که بیشترین رواج آن در شهر محمدیۀ نائین است، قدمتی چندصدساله دارد و یکی از شاخص‌ترین دست‌بافته‌های سنتی ایران محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/441171" target="_blank">📅 17:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441170">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmhOrgS1fV8myHE35JG09uDd-graguw6rgbkWfoG7e54wk9Tg3p0-26_oein4j14Erg8oX6FXmCvkjtMr5hWUXmq8CozxJQtxBjdJ4xdVdJiyuU4BuqVMvp93wY4xIifhCgRbFIz0DAOIrcZo-Hp6iQZo6EeKiCFGfCS5aFGYozmSe7WUFWDpQSKHbQ8S3pkMnNl01-qc8fwyxCPOYqbpwtOSgjwnICqYxSedh55TZBo_lWQPscQYENU3oUyF6UCILIlAimOk0i6ffvrKX_IxHI5HmG5lsnK1zd_XBPd_-XwI8wM5abbExmR9Op7kQlthXF1yclnGDi2mFSZv7CkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام مقصران آلودگی هوا به کجا رسید
🔹
فلسفی، عضو کمیسیون کشاورزی، آب و منابع طبیعی مجلس می‌گوید سازمان حفاظت محیط‌زیست تاکنون هیچ گزارشی دربارۀ ترک‌فعل دستگاه‌های مسئول در اجرای قانون هوای پاک ارائه نکرده و بیشتر جنبۀ توصیفی و کلی دارند و عملکرد دستگاه‌های متخلف را مشخص نمی‌کنند.
🔹
به‌گفتۀ او، با گذشت ۹ سال از تصویب قانون هوای پاک، کمتر از ۱۵ درصد این قانون اجرایی شده است.
🔹
براساس قانون، سازمان حفاظت محیط‌زیست موظف است عملکرد ۱۷ دستگاه مسئول را رصد و موارد ترک‌فعل را به مراجع نظارتی اعلام کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441170" target="_blank">📅 17:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441169">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d26352c7b.mp4?token=FTkflXV5-L5vDgQYeMY80nHzLO25N5hSfhb-CU0Wmq_NYYJso6vD8A09PCijYKPtMXKNxX3r5FM1ksDsfGitkQakk1QYrU8lrzaYCA98TuHRQrALra6xqpwE6OKdmGNK6cr5mn1nhXUB4srVWSMnkDbatGxCLmMyTMWN3QNUE5sZyBgsDJFmej7HU9JdXtV61TLc2mZv5ZmTO4bQBA29BHIlW41NqIet3-gOj9zGc88k5Ricat3bZwEdGBdgyej0R8mJm5OmuFKwqTVPzf-RBMEpL3r3eq49G885wrh1Jntx_Y97WmgAIcX1uLkjmqtMDvmX2EX8Fr10_TubwaReAouYGi7-g7wbO44pcOVEFYryefbxNykKM0mOXxjIbJ4m3hQvjYC4XaDPVrAf0eTjxI9HZCtxEe6YdUHVs6xgm_iXYLsGgqSe5alyLPuG5T5htQfp0EyfugcLNH6QjQhVeZ-DU-Ht9POSHZpInxS7cK0nAZTPZjhLxZEK531kLnOC9LeuSMpWOCYLRClbILWfhyQiHfpvIdSgO5dJCJwgRW_8fWVPXsA5NMstvhwWhVpRY38oNBqcOhBWmTABpDUszNZ70x8brY-j8p5wnsl_HIRVUZG0UhO0sb6nHa6XU-ouM1-oHA7YJhhMmb8wrWkhY4dZi1Zbpu3pTjqkB06Pl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به مواضع نظامیان صهیونیست در ۲ شهرک الناقوره‌ ‌و القنطره در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441169" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHz71K81YuRoa9_ahmBfkhyivMp0REn6maj3Uvx4ADUZHj-GeRU8E8GekTUFLLhCzwzdtUJg6pI1ZvAqOUIxs2c0srKnTN-sqEsw2pThalq5hporyT1I9VMHRwJWlEpX8WJYXWjfgrkRRa8GuNilOCT7j9Wa_z_Q4UNXqQ1RPT1SbpfGGG8fHYOI5e98WIUsORIkkV5yram-jNukfElJcwmzQTlwfvl4XMEf-6cGlq2DgOiDGSdSPcVqFMlzgy9JuwNXRg0dBySb9R_hHe29WNUhY7t3pN8w5m6YvXnh-iTvckKc1og6GJhAwNFxKqEfvZ1EreWAn9qfWe58Y1xXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۲ هزار حاجی امروز وارد کشور می‌شوند
🔹
رئیس سازمان حج و زیارت اعلام کرد امروز بیش از ۲ هزار زائر ایرانی با ۹ پرواز از جده به فرودگاه‌های تهران، اصفهان، شیراز و گرگان منتقل می‌شوند.
🔹
هنوز بیش از ۱۰ هزار زائر ایرانی در عربستان حضور دارند و عملیات بازگشت آن‌ها همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441168" target="_blank">📅 17:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZfojin-8acRaFuds7TataHlXw-a9UKHomanK1GgzW-hrFabydMFORlzLy3THoYsy-JBYnFOvrrz136lsvz6JYZYReZJtAaJJDoi2KFXYha0qjWrChUJgVyBbBUQOqAhQNPYS1qaSD2FMpdS7cNkvzVJAkcd7xNGQDhP4c4DrcTYI2B27ei47oomq8J7IqjR2BeQJQYsFAoz5vqVuaXrXQiZHdlyFMwM_GjHtDO53H9vnmfq0QR1MENChcWJYVSNC7hfLdSAqevjmpb9voMpGzFYX1re42__FG-0LUfAP-DY7E6w-fnG_Z5Dk1TQgW6pBBsseQ9r27hhmOVy95C45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اصلاح مالیات کسب‌وکارها در بودجۀ ۱۴۰۵
🔹
رئیس ‌کل سازمان مالیاتی اعلام کرد با توجه به فشارهای اقتصادی ناشی از جنگ ۱۲ روزه و مشکلات ماه‌های اخیر، احتمال اعمال اصلاحات مالیاتی متناسب با شرایط جدید در بودجه ۱۴۰۵ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441167" target="_blank">📅 17:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b4ccd71c.mp4?token=Gsvqg9BRBAR2--p9RensZLDQn36e-O324SE_mF8z0g9cE9iVDo4Zt1Wr12PWFSPe3VCnNabk6ocBFjrZmSGT9otJ9vVhTyqzW7qqmJJ6lOr-2oC1_q69onoA-UUdpflwKpDmcUX01r81co0SkSI5BUXlq8oQlRK_rxJLC4IB3NHo5dKzXcI-QM0hztR_ltoLghC967fe2kuiVKrp4vHtQoPp3OKplxxRxOaO5AkJhHifhSURbs33Fy7Bb21mSVWwFVgq3U99fLNmkpTGpwZK63Jl1nBb-Ha-RDBGcxb0HS2kCpZnJPzj_xqrWNuB4gbl2FpgE-IOyciC9UJG4BWNUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجاج از نگاه مسلمانان جهان پس از جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441166" target="_blank">📅 16:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441165">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkwYy2AfQwa3zo4MDYJ1SGGrObe3zQbJYQRkzyjEApseEhFBLsbUaihPh4gDaj86N5xRtbHtS3bryUkJNshP3PD0nUA5rdVuFWp7Q5k-HYECEoe_d_qu1OrtV3o_85SHerntl6lyukfuSH4A56zzjy1rjI4VJ3A4kcOzjQZPR665mjh2WCzAqJGkbOFO3Tkf8xlIJeSciDs3-5O9FePHIa5r_Pg3ioSH3p9Cw5uqVl8mn_t5d2pfKwV0ZaFV-Gguk-xFvBIqlBBi6t63cvyBpOXkw6Rjj-MYx2r3OzUm7CSjoVVNLNHHKGWgjDPG2legvRHI0qJ9WWyp9gwCTnE-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441165" target="_blank">📅 16:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8867f73f.mp4?token=DiSRnuejqYBwdF3AaT6LYiXIeMTC2tWLabNr6g3VJu9dP8pQgJfdlUGtFdiCoDbE6YCeTbmGCuA-wqu8_YfArfgl1OkJHp3-fWXgAAgLXxAUjS2l2Dx2S7bw3c3Wjap5hdFKgOIOb57NCw-qEE3BOxdkcFHWqFP-uB3Ixh2wzkP3r2PC-pj3tFm0FgbaQ6u1cxbxadvB_utTRp8KnYakwKVAHEDhdEEmLzzYfR8qrkrWPSKooWnsRnPkF1n1TjyFplfThsQjH5MmXXtuNM9b53iCiNY13Ql2Y9v-nrfK7vxUlm3QEHoGL47Wp1FqXQdRjH97NzRj0GcxPJLfnTSbjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان کار گوشی‌قاپ‌ها و گردنبندقاپ‌های سریالی تهران
🔹
مأموران پایگاه دوم پلیس آگاهی تهران بزرگ در عملیاتی ضربتی، دو سارق حرفه‌ای به نام‌های «محسن» و «رامین» را در مخفیگاهشان در یکی از شهرستان‌های غرب تهران دستگیر کردند.
🔹
این متهمان در بازجویی‌های اولیه به ۲۰ فقره گوشی‌قاپی و گردن‌بندقاپی در نقاط مختلف پایتخت اعتراف کردند.
🔹
پلیس اعلام کرد برخورد با سارقان و مخلان امنیت با جدیت ادامه دارد و هیچ نقطه‌ای برای مجرمان امن نخواهد بود.
🔹
پیش‌تر نیز عامل سرقت مسلحانه از دو طلافروشی در میدان امام حسین(ع) و بلوار اندرزگو شناسایی و دستگیر شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441164" target="_blank">📅 16:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">دیدند راهبان صلیبی و اهل دیر
خیر کل آمده است به‌همراه کل خیر
🔹
شعرخوانی حبیبی کسبی برای عید مباهله
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441163" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4625748c1.mp4?token=CmacFMgLvmy22bzndpACxbtQN4n36oXP78bklUOi6Ywn3LUSeptTNQvrVemDcNKRvm9rNouD602wJDofhz74E_5GU0bKPhtLGTKyWLLJd0uOoVfsL3xk4qqehmMMMjF2tRW_dLbisxmygHY8WcmRXoXSc06orUbb2fnZsdlr0W65P7mxrXEoG6SEru1_45w4zD6JY5fV5yVOZURJtknMqArESTKAKJ43bah5G-6smmWWR9kMutXo4ubovWNXllAhhbcJWOLxpTWUNJfL0l4K371Q9E9sGfCywzgCewG0Wy5ff9BAb0yys6oM-tiEG89ZETPxLxmydvlEecHDq-eFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
تصاویر لحظهٔ شلیک نظامی رژیم صهیونیستی به نوزاد ۷ ماههٔ فلسطینی در کرانهٔ باختری
⚠️
حاوی تصاویر دلخراش
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441162" target="_blank">📅 16:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01957eb299.mp4?token=GFju5wIZTPW76b8kSadUlAdBxQEJIT3ymqDnf1kFkMIal4KrL0Um70UDSqdA1PZoHwDJ3T1YZWjmv2lsosTfgJWhtzzQ3UysPQ_gS7IVDCk7tMd5NNSFW9O0QREessgGvFJVUzPZUU0eBaskaP04zqv9H9v468y5fdoGRWhs_VFLRpZ9EYPgv6rFBtIjOXxF-LMowbnT4vxqoRYwa_D5P0y1FiAdvsaD4Z_ZQ4egMqGUMyZjIuJwny15-vjIy9CfetNpn2F6Y8X6nhv1eUbDRxJsXT-CjX8hhMOISMbYDH-wzVCFR0EBgKs9oqS3QpSI9OkXCanHUP5fQmyrrPadjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم دیده‌نشده از سلام نظامی شهدای دانش‌آموز میناب به رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441161" target="_blank">📅 16:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
پس از تجاوز دیشب دشمن آمریکایی، نیروهای مسلح کشورمان چه اهدافی را هدف قرار دادند؟  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441160" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a74VSdhZBcDyK0bkduJdTJKlNzR8SH6mw-MV9hDo2BureZt1q_0s67yjAGqlHlIFFAWFKnM45s1_kcZVMuJFkKXoMKXX0KrrOzM-D7huRkMSFvHa_rrLHF2R-IK3zkqlZZZbAk2A0Cl1xbM9E6ia9b9TN5_TNTz-OZ1yevREccwfkBgdkWtr5jv-1SAzp-QRIDbBdd41dHOuCsA39Hz45KdwBjWH4giqrzKHt_qro7KTokQBv3gpKjrOo4VwDPbH-8Gu7-CsJUKacQUtwWqFEui2D7D2vuGAQDEgtRlMWmCQ0pQuRREzd8tKEa0FRQSSY_sCP-ivRXVjFlt4oTkG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته ماندن
تنگۀ هرمز کویت را به قرض لوله کشاند
🔹
براساس گزارش بلومبرگ، کویت برای صادرات نفتی خود کاملا به تنگۀ هرمز وابسته است. این مسئله باعث شده این کشور میادین نفتی خود را در حداقل سطح ممکن فعال نگه دارد تا بتواند از آسیب به چاه‌های نفت جلوگیری کند و بتواند نیاز داخلی به سوخت را تأمین نماید.
🔹
مدیر مؤسسه نفت کویت می‌گوید مذاکراتی را با عربستان و امارات آغاز کرده تا سیستم‌های خطوط لوله این دو کشور را به گونه‌ای گسترش دهند که قادر به انتقال نفت صادراتی کویت نیز باشد.
🔹
این در حالی‌است که به اذعان او «ایستگاه‌های پمپاژ و تأسیسات صادراتی، آسیب‌پذیرترین حلقه در زیرساخت خطوط لوله هستند؛ شما دیدید که ایران چگونه هر دو تأسیسات سعودی و اماراتی را هدف قرار داد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441159" target="_blank">📅 15:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXeQUY92SezRHWYJ0q8qT3smUd6fY_VyMWGOw27Ks_LZ7Hu5SkWkovaYzteey2X5GDaK2VO3zEX_EoazezFg3TNUw_aD8hJnZ4VXgqUc144iOk5BJmvEd0zyB5qIKPv_PVbZG4zb3M0Ub_rt9jpXbJbZKXbkM4z0hayc5eocNDRCmEYEDkJ-f1MJv-lY0Oe6HWeI5R6sJMUris0D9kL7-5QMkFAqq6z8Kk7f-Q3c4-YaZSn8tZxaVzLA-vp_qWQQ2WRjU7asMY-MSz6Xisz6QG2fIyUnVBHettnPVFp41PN7ovopY6IHXQWmBcCVdHOotop8onE95JP35OmMRfFHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق زیباکلام بازداشت شد
🔹
صادق زیباکلام صبح امروز با دستور قضایی بازداشت شد. پیش‌تر دادستانی تهران از تشدید قرار نظارت قضایی او به‌دلیل نقض ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی خبر داده بود.
🔹
براساس اعلام مراجع قضایی، زیباکلام با وجود این محدودیت‌ها در یک مصاحبۀ رسانه‌ای اظهاراتی مطرح کرد که به اعلام جرم جدید علیه او و تشدید قرار نظارت قضایی منجر شد.
🔹
پروندۀ او هم‌اکنون در دادسرای فرهنگ و رسانه در حال رسیدگی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441157" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441156">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5c819659.mp4?token=Z86RWz9c2D_d03AVsgV4eY8HIMWggyCigluHBTwvv0lz0byo6janrRKD8ZrB4vWsVVDDA6RTvjjs1ayaY_G6cLcNnVweHWnE0YArX1_6tFDyq5mBu5J6LRICLaYYsRc8dmafG_l1Z-SPTuLAQ-IEoXdXQhNyGjMw5Bf6W9xNOqADUtwxDCwQYKpoEbhskjiLCJMtmcK2fzf5ZzwObA5914y70Qh4bhDIVvt9kKYm9EqzEUUE_MjqJ7Kj4UaPUuW9LgUzLEINN0yLIB7pGAUs4dEBQn2MTkuBglkFSeiXFyVzTWhOYWSTTJpAly1NjUFlfeNdlC4rrdqML0HxDH4vDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتگ ۱۶۸# تیم ملی ایران در جام جهانی خبرساز شد
@Farsna -
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441156" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHUfDAzprHVgeDYAksd91517bi4YN6rCLrmbQiSuQfEze7qcHz6kzyI5AzjchOVIy7dNlX4JAiglMtPt548ScM_XNgvOMO3z8A1RYszjukQnBEC1NoXABWhwhbxFBLTgw03_Ta9sSKHY0bOexyIwEldUxRydQBJxXsBu2JIRnWFFJNji3xD942J_nZHPAggfvyWSFbgQhjg-VTVbsBwxjKK2E69JkYsxiYFctUiqmLRpbbKM9jS19DrVg3EUucaQXdT-m7QBVfe-oteMQl472cpaqEtyeQWpgWE66ZGCJw6cIwhuazBS-BvjLfVwSXwkCjm4kLP4pRAut_4yoZE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441155" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue5u8V0MGjqacDmZ-ZqrLmb6J-HBNFgg5oUgOG951PZuqab1-1JodnOgcs5M71lw0sSZwfLEF5c_9b2KUyDHy0nJIl0CjIu7uU3KE8yRWvzDbNe4ZB_nJ0ovMS9l26-QNyHit46WEaz18pSZRky9tmfusb5DHE8N_QxF5ZrsGZvo2SeiwGg2Br-_UlumIu2vUCFjFe1ehawZANmCRZpSgEWtgzhfMyzqWRIb_n6mCTzMawSsAfhjzjhA90PABXph1BCcG8fswlNawwi-FvgSHXjS3eRbE3vhA8bCzRua--JYgtxRBjAFAr85JBpFEC7xRnQZkW4cCjV6_KFZAbtmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری این راهکارها نقش مؤثری ایفا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441147" target="_blank">📅 15:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckbJ5KLnrq_JUSsEmk8gfhXF31eESIFE-qNISyAg46qxStMc5V-87YAgUYZg740Jvt56SuhIbUQFTCOPQS053be_UUQxB11CU-m9dy8mSbKa3yftQ2bWSr3zLLGt2Y4CmggNNMAJva1OaqJyx6T9B2FjiWQhTs0Dlpt0C42KGHw1nMSiogENLqM1-Nb3jzYM0HUUedJj31pd_PPZteobE86_1jH-DD-Dv96dWnEeMMCnPSB0iDuHYxvg4ursRx-OHdex8pApBfMFOPnW7DMVSVrJ3A9D8FN4s5j9nEwCCPZhxFNAMlri_uMphDWkteVgRhV75PLertebqnXcKWWueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام محدودیت‌های ترافیکی جاده‌های شمال
پنجشنبه ۲۱ خرداد:
🔹
کامیون‌ها و کامیونت‌ها (به‌جز حاملان مواد سوختی و فاسدشدنی) از ساعت ۸ تا ۲۴ در محور هراز ممنوع‌التردد هستند.
🔹
در صورت سنگینی ترافیک، محدودیت یک‌طرفه مقطعی در محور کندوان با صلاحدید پلیس راه اعمال خواهد شد.
روز جمعه ۲۲ خرداد:
🔸
از ساعت ۱۴ ورود خودروها از آزادراه تهران–شمال به سمت چالوس ممنوع می‌شود.
🔸
از ساعت ۱۵ مسیر پل زنگوله به سمت چالوس مسدود خواهد شد.
🔸
از ساعت ۱۶ مسیر مرزن‌آباد به سمت تهران یک‌طرفه می‌شود.
🔸
این محدودیت‌ها تا ساعت ۲۴ ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441146" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rI-ZU4lFXh-XpZ1O-AEN_kX4N03tqRoLnJAMH163-8YasXhw3dBAhsV8boeIWIjBodtq59WAnn7Yij1oWydc8NMbjpZp0QPkvNlbYuYA3cycGFp2k5i3O4KFteikrGLe4BNbOkeMBDJhrMTePHOhsNrl4hhkvxVxHgsOx-WhtweShHjfaTszE9dCfGONYb8ATaN3f4hkCvgsX1GkQf70Bw_MxiGL4U664cjdqFBmTcdMu5rXX8yFNydgo4b5JWXzz3wZI6SgFDwH9zPzZX9fD2MQtkzCPs_uAOXGjld4eYnkLR3cdINFks9zRWVOuJ_S30sNQXg1ZH9TyXQy3mmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام رفع فیلتر می‌شود؟
🔹
درحالی‌که برخی رسانه‌ها از احتمال رفع فیلتر تلگرام خبر دادند، براساس اطلاعاتی که به فارس رسیده دیروز کمیتهٔ بازگشایی پلتفرم‌های فیلترشده جلسه‌ای برگزار نکرده‌اند و هیچ مصوبهٔ جدیدی در خصوص رفع فیلتر تلگرام تصویب نشده است.
🔸
هرگونه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441145" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf0RaT4UJYkD_pojqWJ4l0qA1g5zitymFMUbDwTTRXWya2XIW9RYxS3mmQD14zBgf_uMIvcXQ4jIGiDJNpeAO2f6d7t8RroSWGx5UEtT8MvCX7xm1NluTgSeXcSV7xTcBDfVE5cNUJxG6XMeatftL4aXXEUJku4ww2OaYVqgtfcqPncH8_5U2xKKeio0EnZHl0oDqD-eDHuYWuff1Q5KceKTRlfDB_Kejp4TIKYNG2Y-0c0s0CL233P3m4eiWKtVv33qTbGyfIPSFN4R2Tlb4ktiI6N99Zgh_d8FmDnnvv4DmzTuAgq91t-tMWWsN8kla9COzEZn9GivrS5mA-b26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل میناب
🔹
فرماندۀ پایگاه دریابانی میناب: ۳ مشک ماری حاوی ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل این شهرستان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441144" target="_blank">📅 15:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm2Mtq9MuswkWx3rrNTE7SYR69YxYBdNq0PTg8zlCaOVlZ1tTyHQqpzdkFRX4jGfIWJWzEwb9qlK26jzjflpCrAOtyhxGI3Ky-N3wgfmjKTu-YplXPmEVw3gVxawrCLHsLo_Mx8kAA3Nr6mVnXGMiDAN7SpTwn_QszrydsAFgw38hnPPr-IrkXVSYIbW8MR3cB8gBgIFoAfjc0yU6vnX98YzXEfjo669jfc9_T3wynD482YV3qlXDc4sgMv4jpPinTJohCf8B3EzzTS3tAAz_RQs0roNwUvmyv6qaxN3RLFaqHq0mfmP37yF3ZaWJHp7SQcjEujZigUIrKscQpN4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیکود نامزدی نتانیاهو برای انتخابات آینده را اعلام کرد
🔹
حزب لیکود رژیم صهیونیستی اعلام کرد که نتانیاهو ریاست این حزب را برعهده خواهد داشت و در انتخابات پارلمانی آیندۀ رژیم نامزد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441143" target="_blank">📅 15:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff7d0417a.mp4?token=SmEjXH6r2Mh-PJBp9TY7RWNCA7neYZJfPq0Oi-FbeZ1wCAZQcswxsakNEv-n5mI1J8m-XN23PqHzWptk-tdtTtvhMmBBTRBSj6MYmAdQIpzBkU7-HaGdUVfFcXsW-16t8AsNX3v5aQA8R0MpZnQEfzMlF03uIv1iBsG1hR5L5FxuCViiaiTL69nOOfnhBjc9eu3HAEB7OjaELQ2EI_Rty-iArHkt9S43s-Q9UqyzWbFj-9ygYaRwcIaprpF1zXmcEtbLIjuLJRB8lHxtREyGVwj89mGuqyed5bd1Xds5xVjv5-GXIq5ME0yJ-ClawmeMhYpPweL10DkkUX4ZK3Jmwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بازی ضدچینی تایوان با موشک‌های آمریکایی
🔹
تایوان برای اولین‌بار با سامانه‌های موشکی توپخانه‌ای هایمارس ساخت آمریکا شلیک واقعی انجام داد و حملات دقیق فرامنطقه‌ای را شبیه‌سازی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441142" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رویترز: هیئتی قطری امروز راهی تهران شد
🔹
خبرگزاری رویترز به‌نقل از منابع آگاه مدعی شده که هیئت مذاکره‌کنندهٔ قطری صبح امروز پس‌از رایزنی با آمریکا، راهی تهران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441141" target="_blank">📅 14:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c73674cb.mp4?token=TbZGMiKUS936SpRpydlVzjv4_FUhqS_7P-qIJGCMfUTP2yzx_ONZY-RrIJ9AL6nmUwwPiOseWv5sAIXu0SIbUvU9t3B1q8amtUzvd5Z7L6KRH_xMcCqpWSJreD71M2M2OeMEFLj4lwt7POrvTmy0Zo3Ms2Pm1rG645cMi2iaDun8TQfqbTejjg2VjFIHHALCJezK3QWFtxWM_HV1ZHTnu0Qd5ejqfHHQM8l_M7kkK5BU5eu2idMyCx_Jqf9xE9qIP9ECkYNbcc6OpmYF0mtrEa3CyGUx2foTYwtEQ3HKC6FsdRQbMqlEySP68iPrlFzbkvuWTwgMGkzBKRbl7SM1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پالایشگاه بزرگ روسیه هدف قرار گرفت
🔹
پالایشگاه نفت در استان سامارا پس از حملۀ پهپادی اوکراین دچار آتش‌سوزی شد. این پالایشگاه یکی از بزرگترین تأسیسات صنعت نفت در منطقه و بخشی از شرکت دولتی روس‌نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441140" target="_blank">📅 14:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9232e26f.mp4?token=EtrMEmtESnQN2b8u1WcBLMYU4DUZIdxdrYvP2QA2EM0YWBKplyhGe4HhqoU5Kvq53owOodnI7Cvp3_3iE-XociV1BiTe2elbUZAuGZOGlbXv9ORmc4KtM-jJbuarvGIOXaQTgDC0fU3YF6JjGyUAlnWLYKbRGORF7wMMTijEP5mkZVSvlhwLmLKAPJ-OWsXLysnBBqCWf39LI4Y-fKzgeS5UyC7JGIdUO6C8lBulR6q4ddXCdTik8PAd1n_Er0TaHo3mc9YMCuf5_P3a-14O9jp1tq3ccvWf_iY7E26RMFM0anmvBF20f8-ocu4XHfQ2z3y1lUVzMa8l_wWrjglnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441139" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-NPbq5Uib4k3OOOj_IF-1R7ePjNkfiNai57oO6UebgJ4Js2f0FXJsgjk8UcxLjqOmM9XvJhA1qlRBdcYNhWPebCcQjk-4ZSDs0gNlkmTmhTLH7MH5KQyJTh2JAkKDclBh5_vR7gpEWnjdqEkwc2_RvAnT2CHk1ALWpMsbs5bbY-CTsRTQU7TVeGQsk90HhrgHJkTbVuYqFjWDU-0l7l-eqC5u8QxSZTi25cfwHd9AHA2g0K1eF-Rextri7T53r-bYshyHDzFSn8yXs4mEdGSPiuYTiMVQgURto8RoNser6l1OVmau7SrhvI-h53ue9eznD_vx32i5oxiEhMG4owbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: حملات اسرائیل به سوریه و لبنان تهدیدی برای ترکیه است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441138" target="_blank">📅 14:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwfeMFgBGtJf5l_x1C5ZdOgHUG2FfmDcq-Y3Fq35gQvaqaltqwhroQKcbQMWNQ8YS_zYDirL-BcSfDJpokOZqxMh5JKMv_wVwrU42VAXU9YC_v558f3c2anuEN6d9ILAMDrFzggFrkyEJGh-ThdLc4lA2zMXLfFjrEM76FTCgpV6T8beuGZpjaoMqbIVneuWBBiV_e_Z0jabXfLy-AqZwIL-R8hp6GPvDdzso5isjc1-_oz8No61pxbBpzqNy24a0NB98fXIA08Qd-4jc48-9LWuV9eQ5ftYaUDEnavUsRRFbvxEUhPqjD0AU4ecrg7ea12-39eDlCLgZa15LOD8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحولی مهم در منطقه آزاد ارس
جایگاه گمرک نوردوز به اداره‌کل ارتقا پیدا کرد
در پی پیگیری‌های مستمر استاندار آذربایجان شرقی، نماینده مردم مرند و جلفا در مجلس شورای اسلامی و مدیرعامل سازمان منطقه آزاد ارس، جایگاه گمرک نوردوز به عنوان تنها مرز زمینی ایران با ارمنستان، به سطح «اداره‌کل» ارتقا یافت.
مرز نوردوز که در محدوده منطقه آزاد ارس قرار دارد، یکی از مهم‌ترین گذرگاه‌های تجاری کشور در مسیر ارتباطی ایران با حوزه قفقاز و اوراسیا محسوب می‌شود و ارتقای جایگاه گمرک آن می‌تواند نقش مهمی در تسهیل تجارت، افزایش ظرفیت ترانزیت و توسعه مبادلات اقتصادی با کشورهای همسایه ایفا کند.
با ارتقای جایگاه گمرک نوردوز به اداره‌کل، اختیارات مدیریتی و عملیاتی این گمرک افزایش یافته و بسیاری از فرآیندهای اداری و تصمیم‌گیری که پیش از این نیازمند ارجاع به سطوح بالاتر بود، در همین مرز قابل انجام خواهد بود. این موضوع موجب تسریع در تشریفات گمرکی، کاهش زمان توقف کامیون‌ها و تسهیل صادرات و واردات از این مسیر خواهد شد.
ارتقای ساختاری گمرک نوردوز زمینه تقویت زیرساخت‌های گمرکی و توسعه تجهیزات و لجستیک در این مرز مهم را فراهم می‌کند.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/441137" target="_blank">📅 14:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJGYk09RY-ZDKnGvVMP77BbR_9l2TV80otdCmjkoqPIxulC51WTBEcnNsJ5ZDs09kNd7dJPfsntJ3-QKNIo2UuhlFjGWUbRUrcBO7J-Ybtuwu3G8h0K1F7S72pJywE19Q-2W-FxBwGIVJpCtb5mkc7SGR_S1iKDQgAshGcJa5T44-bQdBCd5FQj1o-3inXpDP30sLO4J7li2caUorG_aW_yK8KPtILhgBF-l2Oe62e6RLNFEsMD4FthD4RpH3W_2wSHJZaLl59ogHLKvtdaqCVcPhKvApjvCZYAgLfX9ZuHGYnz6nrptDNjOO62ri1u-oxiE02Z2FMR2sQuE5NJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/441136" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/441135" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40024382dd.mp4?token=S_COGhWFGuC8fPT1CV2zVo8O7dpPH87cSjfsABbaxG8y5cZxsh6Td8ZXlbFvgQxI-Z9cSNs7BcNJXgvHF0kYmw35uYgyoUWqx5KFrHwSlJrmSTVPSy-vsCuAcOacMLfpOTEd1cVFTNpAPGA6PceNym40QcPY1D2d0ZL0FHqEiJW_a_hCBxSmYeDT1jtfDC--lBGg2HV4VmR_XFm8phpnmaRxCYOfBAHqe9c9TCSQfVcD6FDiOk7fFaVHndKLrBHzkBs2i1ieZyED5VhlfQQnEEP7f9KXBiChpAKIfK0Ie0C7xc4iNS9f4GrUASYbMJ3T8G2Mcbh34Yszj0nO7BAoojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر شلیک موشک‌های سوخت جامد و مایع دوربرد قدر و عماد و خیبرشکن به‌سمت اهداف آمریکایی در منطقه  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441134" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441133">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
قالیباف: جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441133" target="_blank">📅 14:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔸
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441131" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441130" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441129" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad86abac7.mp4?token=vOg5B_luQMRmu3A3-auXhHOdWoNW950DXDqpq9C5zypEMCuXVOtQBdgXGV6WdZ-_x3FYRdRKx_OyyiJakyWOB1_h61DhAz0EF-ws5td5sIDRxINz5qBclfeCGEr6eYRwYfsN7bThKtgaOL41MkDGqZEoCK6BdljKDa9W76lr-ZE1t1MD8jPPqTrNyQMnDOj4vLHu1bONVpLKhbnoXtD5HxbKPyAFSzxAFxrLsrlf6midWpyRRQKP0Z6S4Awyf_inAX1duiQOLtI_KokLdHT_JgSLwmUG1rhxhGHXtl_RCLwSxKgoPw0TtN45O-enxM65y8mmNOB4fVZzQAryaKhi7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: بررسی‌های ایران مبنی بر همکاری اردن با متجاوزان به کشور ما، تنبیه اردن را درپی داشت
🔹
این رویه شامل کشورهای هم‌دست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441128" target="_blank">📅 14:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441127" target="_blank">📅 14:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoP2gfh_TRBsuLckTbJrRsN3F2Wv9afzIYGAfrnScWvDvmE7ns_WL9QgfR8YUyLdn5ctUy1qjhHkw2AXNxxomCcGJmAcAOjdmocFF6bchX8gc1D6kbsEjOMezLSpHKKtbhNA_4-YVIMWqmpnSeLhmp95Oz9vVVOaHgBt2ED-G_AjlU6yd1OylixeYSoqYhrPxvsCcYf70H5DFoSw-BrvEagOxnZFfthNDaiWgncvvWyTLxrbYWiWP6VXVZuyJKY9KVsW1oDA-sLNXWd-h__DFUPX6rSc_cuRFgHNptztmbWX59sXkFo19QNYXN6rAWL70TmkM1VUw-BuD8MIQFArJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام آشیانه و انبار پایگاه‌ هوایی رامات دیوید بر اثر حملات موشکی شب گذشته ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441126" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1117278651.mp4?token=In4IOJTWBhQGH0vF3M0D0TD9oFyVgCr9EPhPfFgibykPhWZHsyaDecPq8vLPRVaasSV1kiQIaJD_lR0YRZxM70OofdChfu1mPeI3Om1HdHFFxGYZpOQrrNKlYrzltoCwy6tU6kY9QEXBz6b8Pz4CViPn_OtjR99KlLsCtwqL5DM9ftP5w8mZR_TsZRermPObT6j9DCDXcVXi2gohSOERXUpKRIQVI-gKQeC8IzZMyCuscklk13FizztfZznZ1i04uTUi-a9g5P-Nl1-BQMSMv0gEWI37iKCNXjrRSW0sotwL0DTCK9ry8fTY7DQrnomFUD9R57lDtwlXf6PnKbmAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441125" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">️انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441124" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
