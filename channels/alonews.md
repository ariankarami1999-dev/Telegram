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
<img src="https://cdn4.telesco.pe/file/sZZAGKBaJzlxPKr0fnU3J23KFB1IrS8R13vYCz_108Mczwl_x2KuLxErtJU_eMza9l6VsTBbHnEhq_6u2L2N54xtGdJmmKk3NJOCX5DxWLzrawDpH7IkmUAIH-fVe9GaWTSO0xy-J17JhBwgmY5RDMufr9gmc0jhzXyZIrJpxBd9siTBn2AMZzqXaS9f7RTPC6XXJ9d-yKbbuXWj16Ea1Msa6cjNb75u3fwZGwknN6fJOBHQ1CrQ4FTp7FofLAaR9ImVRM3w6Ucm1U1q9urIbPz17AOaOPFrNAyn-zKL16LCuBZXwkSWv6IhUBi6DVSciG9ymF7TbJIG_z4GS8xu2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 979K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 15:35:27</div>
<hr>

<div class="tg-post" id="msg-140394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbEgKr5SKzhrzIs1BRzUOCORbPLSD9U3ip6Gbbt9TJj95QNSxe45acSOVWTN0ckHbHCsej9a6v2J-8--hhUXCpMLA-gvLSyNYwIDNGFYWOIeZJkSzEIUMzqyCfY8FxGpyD1K7qAI4FJouEevxGowvvyhHMsAMnbwfn9a9HkS3FmQI4skOShKoVA-CuCrY-pSGZEoxq5cg69H3p2IPyVmuQX4Y4Y8qaMYleQL6EmeU90RCmIpUfgtWaqwgY7Ke0sGdOf7gXNcDnQLy52jKnV2vJ5z2-Pt6Jfg-3NUYWs4fZ-17X_h8GoqXbhPtXDsVw5UlcMW2TfZdeA0hRpbeyR-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال گزارش می‌دهد که رئیس جمهور ترامپ دستور تحقیقات جدید در مورد نشت اطلاعات مربوط به ذخایر مهمات فرسوده ایالات متحده را داده است، زیرا در خفا معتقد است که این گزارش‌ها «رژیم ایران را جسورتر می‌کند» و اهرم واشنگتن را در مذاکرات بر سر برنامه هسته‌ای تهران تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/alonews/140394" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DruvME6VpRpd2nkALgJCFvvZMqYwsIXK-uPj5UQK8I6XlsDDj2-l2QSOIlXnG5j0ry1Ua4GKjb-Zg8eqbq7vFz5vVtsZ16L4bzGgblD3ipQHMN2-tR-Z4WjRevbunv5hCMfgrgypFLo9pW2_S86-EcB9Km0RrYyfSare14Bo9VtdSBkIQEIZooxXt3wOGxRfrKqNhJ4IuNSA0tjCE_RBkgjp8Iw5gvUdnnJoVXCj1eWtDAEMCcO-DX9Z8ByNA-Qm3t52Suxc8RFBM9dXtQ3jDqcPmD0T3LmdTAefg5G4tqEJzng2BhskgwaQPoXHciO0dmAorGlTNfRklFvo93ZsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: باید انقدر بجنگیم تا پیروز بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/140393" target="_blank">📅 15:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im5l6ZLVpMZRKZ3Hu_tjrBsT1aXtLcZm1kVRbhnLuKrZA1aEBrzxZ74vmv548VJ1oJ81oPFtvqLPIVrl4TascbGf9k1xYfnbmxFQxsl8xiyHXHyMKSR2TJQv4fHb-RGrj2tInhpZAL8gBKAtQJR9_lcEBVAAlR1VBw7Y_sk4F6NAQRT0Eolmit3cXgY2xX5iHtCik1B8C7QC6QnS5sLwfYz3bY6GGD5YIjuhWGFcr6lnsMHRRYdpwaFTIJSwL21gEnJp6sQg645a1WbvztAwgWX8y73LspNtwTwp_mC1n5o4JsZ3GZjGqofbRVDNpCrYH0ZljVmGb53ntwhW41Zrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لائینی امام ساری:
مذاکره درباره تنگه هرمز اصلا تو این شرایط مصلحت نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/140392" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbRnH7aeqpPVTJq9gjpTQd_l3RjN5RCZTHa_ll6rQa89vpKttJpzONTkGX_1-0IUBThmQSxTuNXiNFSAShYoetkgIdaiapW2dcwOgXR49P8g_n3Dc7Y0ENZcQyB7raCPQYMo-hSSFh2vQh7K6JTXm62SfgRUrAvVuU2TJ6zcR1OGOnLuAD4fW5rS8HkfyuYgrV6iGN4RwbJ2TirH-HXc6aGt5gYd6sIhoQI8ZaG4inzFrNO7bqhptYm5ZaoO09zENbliI-_rbSjgp0jjzyoTZNi2SKEPUEc_BPWPmElfolvb0bRDQ0eTe7AB_yH7nMvge706o53C3veoe78iRyoosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140391" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی:
به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/140390" target="_blank">📅 15:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6iRhbTxzpyhpMWQyPiop9VqmNZR5hdNfMw6jnezanXi4k3U4QRBhWjabDa2yiEAncqBukItsh8oI7ddpiHzRChtK6KT4jGFnOxd8Vgn8snYEVMyJriUQ1sVlUM4QsEW2KPHqiKtQeB14wUpMtn-0H7yyo11DfIksqX4Qy7kHJ5lmTHIWJVFh4vopg87VqwY1Zed7R5MczP9lj9XGxKVbjDdwX5zy-yye2hJBm2lALYG3nVtkQlnxur-lTGGWEUH8gV1eUKKOlJIUGg_g2ZnAcD8RbHB1uQKHBRYgcrucyscG5Am8txJnYJ5-L21247YNLO1aHWw1tzJNu_U_sIddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt0sXRaEBXNUpacW4v31R4gC_1O1ApZYEk9GvSmy7yS44r0K4BRjOsP2CCys10Yb-n6-Jnypg8xplTGE1aoEbQ-VgnHYzoTJP4snq5gxWNIprdJ3O-q6SheqleUEl2_X1Fi7l5lytOc8SL0tMq3fJgs6AeOFqCL8XBoytRTKZ6O6divZkO5BO-u-1BeiFln-SBPIawVvHDMNa6NZje3G9WFOBZUl6gDEylDoy5Z6lXx2CRUVecryXk7PKjdUoZZduZlimrlnkJY6-KCWYeks_VRyJklF019pgnl9lvV2tgTTZ0KVsgo4uOYAah3x3dl7bK0Fz5nR51qBN-rFujBAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSHxCJvmCaHNlCmHqrvW9O9h6LNhucpJp_3E4JX38fveu4dA7gvhRv7CiaiFjSIZKsflaRrcRMvnxSwafgnXgAYJgZCMNOmm521UVcISVBfLmoRlzUqZPJEMxSSHgrIuP8btMqYLXcq3N1EhPvGzuzo4Upbz_jIEDx4Sao6Ktb9-GX_C9RUmfhNpLZ7xSs3XwYMsSYMziwiJiJRcXirSf_pdIF8i9DJCO9HQmiX5FUnT8oWTsVwQ_BcDuPt1hs4odbb2bD7KNuV1HmJ6w5Xbp4GZ-n5rxD801IBeMIJLFTLuwbH8Pv5iT9KYe82QT2K7ph2cwLTO1q7JR5LmUwU95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYFTSMY9l-l2Qxq-VfOS_Ue3cynfbNe7fcpF1FkscHyf921-8OiPkzut2c6cgStA3KUZeWR9zyM_8ORB4FONMUuO9F3MOv-S7tHbG2b2Af5vWpC2xyGZzcRq4HL7K_RK0GomJDn0rrv7ppZO8cK4WOMuQqlxHcY0TeOZoZuWRdj1XY94gvjKVYM9ThSqOfHG6ujQROUa8RKSKslfq5s4xEHCtzCfkjhGmtWAIUC8QWnDizYpWc4tcrETUoUI3B8tobgYklD7SFxjUpseJ6B6-dsusqE_jkMsI33wMa0tEmWuEdXiOku_ccb7qjDIleMMlNn4eXBnwAf986QBzFU5yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از انعقاد تفاهم نامه مکه در مرکز جهان اسلام
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140386" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBiFYavPnGYC71iv2GgaGJwPfwzNJ_9BO7If1Cd3a4wEiFU5OhcplwVWrUoL6Eq8X-Dq0LIbcZd5sIt1uUDSSpstuQdDQ8bjAZ5wIx6yZQ32qfPvJpjuRXwH_wl5EWkEim6EqBp2N3wnMB18_cHXRDo_3OZ1vOWqAAM-98kVGXRbhJq_c-dNYOi_rUTQaFEbXDQqAlMgrKytxSN6Eyu9PETGUjEKBjj174doZMPDdazwhni2RbN7EAPJUlQ4VRJJPJDwiKehk8s14VwTpdfEgO5zFOqTJHfhA11IPlRXb0vxMhGVT6bjZcwOBjjKBj8ZVc47OEAvVU-ZBgl5S29Aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری i24 اسرائیل به نقل از دو مقام آگاه در دولت پزشکیان ادعا کرد حال مجتبی خامنه‌ای وخیم است و احتمال درگذشتش وجود دارد. گفته می‌شود به دلیل وخامت حال، کسی از کابینه با او دیدار نکرده و این خبر در سطوح بالا پخش شده؛ برخی مقامات ارشد معتقدند به زودی خبر درگذشت او منتشر می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/140385" target="_blank">📅 14:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOJalX1b7ehNLMOOaZCt6MitUxw19YNO8yDUNiPg6GO2jWJ6OITwFoAi0ZGGI5LPeHt4J8i80iRjS_f41sjqX2p6ZCC_z6Jkbc4qBiEOmstk2I6CcpEurR8f3DKKkPVmpILYGqKLlHwy6afB4oR67a6CzUoxou-dax5sCLdpoCmFAK1OPd_CloX_QGk-TKbF-gb1kM7F7jdVtWQQmbZ-o6A8ZTb9nRBVLeKV2Jo23ItGJ8DCkPeHMkKOls4B5jU5e2ZHLDPadXFsAEl8u9KAUS7iCw8hhPl5EIssg1OIIR5HscLO5Xr941J-wGtpenqQYrVaVasoERTiQJaKsIo9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdNQYUPQSR6EA86M1IBtEWxVhk2oeuw5bYHE57ffkRvWaKQaJ6KLmqDXE9qqpjITN7lqb0KP5WlXg742OW2OUF017E1t0rSPBVhK1itCZ094nKFDGBMNnZoydccQm5od9z7xeGa_v5mkl7_V9qRuN7oCaT0K_Q8U8Ih2z3yRIt49zT2AC18kNaOOPKcWXrc0beLlTSSeDOGs5NgU07g8O3XyEBLoNbhHoAlOuy5KWcgBSPw-ZyaxZK6Dmt2_qmRLkmdo1Cb1S0Av2QiU2o6DRgi1FfUBM-qjAgmHhpJ2PkBL6aM3F-mcvyOsXyMvhnDhEUb-vxNCDLvmnjWflmdiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnPUBr3BH94_F-3kIQQCRqm9XTjfT351vFO9hgYYEXM0gyXAdgrp4a4vwKI4PMbFVKtkkxUFtvSZFnqHayFVPI50bLT0JQmAtPyND_znW41oy2hIKT3UERWpCre6IXUlXQGzNtHfylsOkI6-eF5sOktHILwhtIGrg4TmJc3FvL_-O4sjmp42UUDKSpX4Dmgm3dj9iIi0JSZ--QwZTkeXg5EQKIVPS8QmA5f449KIPSoYCyBD-goc_Z1fQzlXbTb1rv5iNwrZpIHqRuO_PufdQ-xUUZCX3kjBirRbCY4JkPDqTJv8f9wcuyxWy5xO2F64zYzXuG9E9bTJ_hLhQTzsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از قطعات پهپادها و جنگنده آمریکایی و اسرائیلی که توسط سپاه به نمایش گذاشته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/140382" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ سوییس رو تهدید کرد:
ترامپ در تازه ترین مصاحبه خود گفت آمریکا حدود ۳۹ میلیارد دلار کسری تجاری با سوئیس دارد و تأکید کرد: «می‌توانم با یک امضا این کسری را از بین ببرم و آن‌ها دیگر یک کشور ممتاز نخواهند بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140381" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
«توافقنامه دفاعی مکه» رسما امضا شد
🔴
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.
🔴
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔴
هدف این توافقنامه، تقویت بازدارندگی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140380" target="_blank">📅 14:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140379">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
«توافقنامه دفاعی مکه» رسما امضا شد
🔴
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.
🔴
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔴
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140379" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6SZP0b4DtJCK4wJeF3UpOJ4KhCL9BXe8Xgw36VwJT-_obJDQ2bgyynFfL6dS1JGFrCdGaivSWlyZsNcMJCYXVUW0c4aZjmYbKNbjY-x6CKgMUDZTKI1OhFYPHr-QvtzjpaTjSkyMPhNSSHgPTAJsIL__wWzKfrXNg2Y9KFxyHnbNjo0JjZ0I4s1OXIUhgmOqzJZSld3nn7SsSFH3r9Qjeky5I-PKRLOGuQ0HuIhASuDn5tut2J6cYup_wE_mKcP4jFpNvt0blaj2PIV0qNNY2uDFLTF1fk2xQe1zuCnWbL2-LDUWBxd9DExJ19hQJ3Su0X-_Pkv5Z_eBuw4xtqukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عبری:
محسن رضایی جزو اهداف ترور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140378" target="_blank">📅 14:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت دفاع روسیه از کنترل بر شهرک آنیشچینی در استان خارکیف خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140377" target="_blank">📅 14:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
الجزیره: آمریکا ذخایر موشک‌های رهگیر خود را تا حد زیادی مصرف کرده؛ در صورت ادامه جنگ این روند ادامه خواهد یافت
🔴
به دلیل این کمبود فعالیت نیرو‌های نظامی آمریکا در منطقه خطرناک‌تر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140376" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3iEDdBRrzFAwkwbIkESuxDi7VODePboawwoXKqCVfIU_2y6mGG6VodJeOyZPjvb4l5EkgdBm9Hc8BUmixpQZvvoKFcKD6zeIxdh-mX199laPMZwZqbCCsYZyZY3DsySl4QPAdQ7PRorWyN4aHw1zjKNI0zvMNRzsVa1Nyo2gf0N3j0iSIcKowhxbmNbfGZkdLbynjAuRcmFoXIwglmoiYmVPTsifB21Rq-zEveJHms3P-w-iOZufc4lsW_rWOWVW1bxkd63M6mrR1ZtgrRn37bn5Mj_qPSpD_4ZK-w28g_E5yQJ5hGyr0Jt_m_zvpl_bf3Kd_MATuGQoUmI7rqyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWIhBOXjtleg0nGWgyWVf6JsjrnP4M89bjRj3XxGXmNaPCNTAwqL7zlLBsAH5Y-MPAe4mt5dl6ksvhM8dVn4OOoyEY1fpbPt0lakkacr6ZoSS-rtVZrlD_ISANuKEizHMr4XXZWatSBWxVxWBQgkWRnutLIurFd-kM-ih5IGAuMNOLbOObSiC5fHtCNskPWVCR8KKtieeDUx6w7kplS_TBB6f-_Oed887OqvqHmcDo9ve7P-LWojUp_aetNr2fA4iWcFpXY2olSwsQzyhQY-sHOIcgAnHEu7Tdh4c1pfdYiRqnt0Hyw7U6dLWX7zVIAOr-iyWUFu44GB4-7gfmhrPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سپاه تصاویری از مهندم کردن پهپاد MQ
-9
آمریکایی در طول جنگ منتشر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140374" target="_blank">📅 13:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رئیس سیاست خارجی اتحادیه اروپا:
اتحادیه اروپا امروز (جمعه) فهرست تحریم‌های جدیدی را علیه پنج فرد مرتبط با مجتمع نظامی-صنعتی روسیه تصویب کرد
🔴
هر حمله جدید علیه اوکراین دلیلی دیگر برای اروپاست تا تحریم‌های خود را علیه روسیه شدیدتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140373" target="_blank">📅 13:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها می‌خواهند به توافقی برسند. ببینید، واضح است که آنها نمی‌خواهند مورد حمله قرار گیرند.
🔴
آنها می‌خواهند به توافقی برسند. پس، باید ببینیم چه می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/140372" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfadad379f.mp4?token=SxicbsgUYxHlZce5-eigZN5Q1q9jXs-Cfdeu_De_7p0HBIyZz2MGZkVKPAQ7k9x9SFpdkwT6X-tiXLcZqbNH5920guRCysfCXfRRgj-TLaRdkvwB548gdCNKMHD1ZAUAOk1Ob8Lkue6-wzNeqJucWJvWs-jACx8ylAUric4VSMu3mFe8S3S2ssC1b00pJjnkSk3X8-1bWaBX23CYIhgHeZe8p3emHY4UiOvtx0Wre3gqyqvLYQbBpe6P9q2-HWlHoW9Al_-HgidsizboABkZNT4UB4TmTNMpSHik4ynpYGLz7PN0M8NOUY-htb2T-dU0TODvrbUjk8DznW8Yptv6OZaJrjgH2yPrqmc_9isQhD1LHmB6LqkP4FlwUAXfYlVynJccSAv94Dr_HxlT0zdKHG5E8YIW3iRaxzYMVyg5aXNzaCQz-Gi6pUDf4UE3hcHZBurjBhg8GDBq-opX-wwSJaUfGYYJu5dglag_GpBP6PucUVUS50akdFOphueAN4vYceCFm_1FkCn0pjp2TxysLavYE-oCTw7oPGEVyMMZ5i7JmcGsOTKZaRmIc7RJnidTeTWo_6t5QNPviv9qznYCDZz4aDpEuCPAFki64zPJQQZ6SszEl65UBNFIb2MsBZLpKNDLWgJ2bN9eRdu5JtHkS5OUMh3Q6P4zpun8ActamIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfadad379f.mp4?token=SxicbsgUYxHlZce5-eigZN5Q1q9jXs-Cfdeu_De_7p0HBIyZz2MGZkVKPAQ7k9x9SFpdkwT6X-tiXLcZqbNH5920guRCysfCXfRRgj-TLaRdkvwB548gdCNKMHD1ZAUAOk1Ob8Lkue6-wzNeqJucWJvWs-jACx8ylAUric4VSMu3mFe8S3S2ssC1b00pJjnkSk3X8-1bWaBX23CYIhgHeZe8p3emHY4UiOvtx0Wre3gqyqvLYQbBpe6P9q2-HWlHoW9Al_-HgidsizboABkZNT4UB4TmTNMpSHik4ynpYGLz7PN0M8NOUY-htb2T-dU0TODvrbUjk8DznW8Yptv6OZaJrjgH2yPrqmc_9isQhD1LHmB6LqkP4FlwUAXfYlVynJccSAv94Dr_HxlT0zdKHG5E8YIW3iRaxzYMVyg5aXNzaCQz-Gi6pUDf4UE3hcHZBurjBhg8GDBq-opX-wwSJaUfGYYJu5dglag_GpBP6PucUVUS50akdFOphueAN4vYceCFm_1FkCn0pjp2TxysLavYE-oCTw7oPGEVyMMZ5i7JmcGsOTKZaRmIc7RJnidTeTWo_6t5QNPviv9qznYCDZz4aDpEuCPAFki64zPJQQZ6SszEl65UBNFIb2MsBZLpKNDLWgJ2bN9eRdu5JtHkS5OUMh3Q6P4zpun8ActamIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر دموکرات‌ها به قدرت برسند، ممکن است من آخرین رئیس‌جمهور جمهوری‌خواه باشم.
🔴
اگر سنا عاقلانه عمل نکند، ممکن است من آخرین رئیس‌جمهور جمهوری‌خواه باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/140371" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK-X8kh_9tFXONZXwCKQ3ROHOLD6BeZLITul6kRbJe06zXM7qrjxU9zAozES2QHZ0-yfUB55heJ6DbOACnqnB9hBi8kEiu_kiM50O7AJzI-W5wJgqIeI3gBCHvpyBZral6ch6Z_whFpc_JfHroOZ-pnyZLEbMeDOBF0KustiAc3GfZpQUJHCvMOofXxj6RHGBE-vriYUsDySd_lpRHnhpofbj1UNAUxZIVSYoIg_cv6gzEokPFQ4VteOK2aCJM1I0vskMSGHvrX8ZUueyab_NmQ5v6sZ9PzTB8SPSFOvlAsgYtOifKlXw2cvAPYJoPlh61OzOM1WSP9dVOdkvEL5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
رئیس‌جمهور چین، «شی جین‌پینگ»، احتمالاً طی چند هفته آینده به آمریکا سفر می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140370" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b39fb9f9d.mp4?token=aBRpYJ3a61YFZ74k1m31VxSa9_2Xik9HFvAteskiRRe_U-M4jDRUGro4ti-fVJBbWudmh4_lqEsp3tDrp_USKJhmZbLvcf1wW5bgwiKyt9-asKexMvFeiEap26iT9XVQF6oOHPv9xx61OipxZTvupcew3aSgm5cBe8O5WFU4vK1P8WihQ13d_Grsa6BRgJdjhNU1ikTfwT30v96hE6w86h_zuAKByV96m13q2FF7Zw72Pw2V5UdOxKAM-EVcRXafOA_eLP2UkNocsgg1hY5Fhpa-n3PLHhMaQI-YSrXun7HbfcKhR-R1lqtgZkPO-U5K2cbkMSM3raQr4JMF2ekWmwGyYKsIgvezY0cEPmWeWjzrT2zEEN2M6nALdcsyvyosyH7l4F3K68hUvxmY_2r57xnaS-p3RvCeZcq3y6AVqWAD2Clg6HDcAxKOYxYoHUW85ZxfdqMnQ4QJV9ZW8CNBktT7OedDqD99994PnSKFIR4jFufoBt1t5ARmqXtZiUTyvptAsDs_kgP-9YW_hzkI__TzE3BEnnLDTiIl8Gy-B57xpjJA8t__UUEmfH69e-QSrpvCg4kGL_72FTty5r9CgrsY7IKtuIlfl5O1LbFriHhE8Zqpam98XE42qITIX5uRvcC-9HpDcaDsAs61kVMRCUxSERSUjjgl58v6dv5LGsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b39fb9f9d.mp4?token=aBRpYJ3a61YFZ74k1m31VxSa9_2Xik9HFvAteskiRRe_U-M4jDRUGro4ti-fVJBbWudmh4_lqEsp3tDrp_USKJhmZbLvcf1wW5bgwiKyt9-asKexMvFeiEap26iT9XVQF6oOHPv9xx61OipxZTvupcew3aSgm5cBe8O5WFU4vK1P8WihQ13d_Grsa6BRgJdjhNU1ikTfwT30v96hE6w86h_zuAKByV96m13q2FF7Zw72Pw2V5UdOxKAM-EVcRXafOA_eLP2UkNocsgg1hY5Fhpa-n3PLHhMaQI-YSrXun7HbfcKhR-R1lqtgZkPO-U5K2cbkMSM3raQr4JMF2ekWmwGyYKsIgvezY0cEPmWeWjzrT2zEEN2M6nALdcsyvyosyH7l4F3K68hUvxmY_2r57xnaS-p3RvCeZcq3y6AVqWAD2Clg6HDcAxKOYxYoHUW85ZxfdqMnQ4QJV9ZW8CNBktT7OedDqD99994PnSKFIR4jFufoBt1t5ARmqXtZiUTyvptAsDs_kgP-9YW_hzkI__TzE3BEnnLDTiIl8Gy-B57xpjJA8t__UUEmfH69e-QSrpvCg4kGL_72FTty5r9CgrsY7IKtuIlfl5O1LbFriHhE8Zqpam98XE42qITIX5uRvcC-9HpDcaDsAs61kVMRCUxSERSUjjgl58v6dv5LGsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نمی‌خواهیم چین در هوش مصنوعی و رمزارزها پیشتاز شود
🔴
دونالد ترامپ گفت: آمریکا نباید اجازه دهد چین در حوزه‌های رمزارز و هوش مصنوعی برتری پیدا کند، زیرا این دو حوزه را برای آینده اقتصادی و فناوری بسیار مهم می‌داند.
🔴
او با اشاره به رشد استفاده از بیت‌کوین گفت: پرداخت‌های رمزارزی در حال گسترش است و به اعتقاد او می‌تواند فشار بر دلار آمریکا را کاهش دهد.
🔴
ترامپ افزود: اگر چین کنترل بازار رمزارزها یا توسعه هوش مصنوعی را در دست بگیرد، این موضوع برای آمریکا یک چالش بزرگ خواهد بود.
🔴
او تأکید کرد: آمریکا در رقابت هوش مصنوعی با چین پیشتاز است و گفت: هیچ‌کس فکر نمی‌کرد این اتفاق ممکن باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140369" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754dc045e.mp4?token=cbjKIsYN9rTxRHeTSUhBFMBkBIw0vSthla7HshuogTOnYgjSMuxYWakDgMAOCA3fpFSZccHvksL2We-F029yt-ww6pL9yIJSwrPsJZ5F3SDeTyM838lkmSm36syM33_UkZB40Ef1bJ53wHFb7XoiIMIuJlxty1aE8C9inoUhsdTwhgneKZQrydu1RjJxPoNw9Mg-etxTs62sjpGGPtqck-8WX8-hTDYxQpH1ddUIvYo5847kzGdBLj4UpKuog_Ydw7sqK2xxdbtMhsWYdPTJO60E9NAYXbyZfm2EUW7Nllx1vGqD2ouWstUooXr1xjsCEgljxCfFKihlK4MHEHIenzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754dc045e.mp4?token=cbjKIsYN9rTxRHeTSUhBFMBkBIw0vSthla7HshuogTOnYgjSMuxYWakDgMAOCA3fpFSZccHvksL2We-F029yt-ww6pL9yIJSwrPsJZ5F3SDeTyM838lkmSm36syM33_UkZB40Ef1bJ53wHFb7XoiIMIuJlxty1aE8C9inoUhsdTwhgneKZQrydu1RjJxPoNw9Mg-etxTs62sjpGGPtqck-8WX8-hTDYxQpH1ddUIvYo5847kzGdBLj4UpKuog_Ydw7sqK2xxdbtMhsWYdPTJO60E9NAYXbyZfm2EUW7Nllx1vGqD2ouWstUooXr1xjsCEgljxCfFKihlK4MHEHIenzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر نامزد نشوم، نمی‌دانم طرفدارانم باز هم رأی می‌دهند یا نه
🔴
دونالد ترامپ گفت: مطمئن نیست اگر او در انتخابات حضور نداشته باشد، هوادارانش همچنان برای رأی دادن پای صندوق‌ها حاضر شوند.
🔴
او افزود: بسیاری از این افراد از حزب جمهوری‌خواه ناراضی و عصبانی هستند، اما این نارضایتی را متوجه شخص او نمی‌دانند.
🔴
ترامپ گفت: آن‌ها از جمهوری‌ خواهان ناراحت هستند، اما از من ناراحت نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140368" target="_blank">📅 13:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یدیعوت أحرونوت به نقل از یک منبع امنیتی ارشد:ایران، حزب الله را مجبور به پیوستن به جنگ در ماه مارس گذشته نکرد، زیرا شرایط پیچیده حزب الله را درک می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/140367" target="_blank">📅 13:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8-Srl-BEAocxUWIaY54SlpVOEXDphO1G-QqAtEmFvaAOoc2fyrSEg3avJ-9DuP7MBw2BonHzLB99uccsu6DynIIGdwvOKRXjlmnokuJREOljL2eW9W7NCgqXdwar13icV-9YBqa74lS35uiQnsTJ-IoLXEwegRUxf3EySisSa8evLKLj1sA4fgyxKmi04pgHQmC0c-Y2XgOsHoYjYTwThenJ6uIueiGfROGjrw_tkOIdAmbdNN4RI0JeaTDnggHPlHYpe9EayocnIKngpZBOjzAzPguRD4L6Jk3d1mDseBzg7ZXyCvwXqjCFToR7WLeeBWNe9TsClPg1OLM_euTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی مدتها پیش بر ضعف فنی قلعه‌نویی پی برده بود و اطرافیان او را با صراحت نقد کرده بود و خواهان جایگزینی گواردیولا با قلعه‌نویی شده بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/140366" target="_blank">📅 13:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dc16a409.mp4?token=Ypy-NKyH-5f_tNyBMp4-910ErVewHAGiRYDlPNhWaRiDFsyomCzjiPzrJmEaCCNAmZascn7--vUUFfmrnGvnwBfVQUb-yl_viddp3NS3d5sTs9X-Bu5xgrK88XbZUH2LVsRcvz3LKYZBnSllUHWofakT-TCbS6tWk6vsZYD8_xhyjOej-4qe9N-dThvTdh79YbKbWWc6F_SL7a4i1eaf01iivZ9zAYmTcgZLZEAdmtQsCSZw2ASORJG8DD90WMGvMBAPsNWyijwQVMhEYE5alNNw4FhM5--FhcExuW9qI7Dnn4DMS7LWnNgjz7zeKpkqaX9SAkR5JYqFhPptg0OvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dc16a409.mp4?token=Ypy-NKyH-5f_tNyBMp4-910ErVewHAGiRYDlPNhWaRiDFsyomCzjiPzrJmEaCCNAmZascn7--vUUFfmrnGvnwBfVQUb-yl_viddp3NS3d5sTs9X-Bu5xgrK88XbZUH2LVsRcvz3LKYZBnSllUHWofakT-TCbS6tWk6vsZYD8_xhyjOej-4qe9N-dThvTdh79YbKbWWc6F_SL7a4i1eaf01iivZ9zAYmTcgZLZEAdmtQsCSZw2ASORJG8DD90WMGvMBAPsNWyijwQVMhEYE5alNNw4FhM5--FhcExuW9qI7Dnn4DMS7LWnNgjz7zeKpkqaX9SAkR5JYqFhPptg0OvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان یک خودروی بمب‌گذاری انتحاری (VBIED) را که توسط ارتش آزادی بلوچستان استفاده می‌شد، در شهر نوشکی، در منطقه بلوچستان پاکستان، منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140365" target="_blank">📅 13:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo-ZQpGoNQJgP4MJBHPLlzdtMrCIhUijecwZawrghNcEb8FYhiYNCmHlvAvrdVOvJrsBex4SF70mBo7GVBNu5YmxV7110YEA2s-mogqgw5kSu9JQp5gbLPUekaxful_f6mXoVhix_wbb2XBT4FqOt15jPCD1BYt3Rpb7hDRceJuTyCME-jaxwm3K_5FLL3EP7jE8JoSFrfZmDaN1Xiqb91Nb8d1l_oHj7UIDPBgeVOnOSDsNarE_JNOMY38AnQKrFe7MRRNCCHm7zsezRF_QnTpCs4BQ6C8KlFHm17snnu3z6VxwfmdLCnDbKmS7l4-En1AlgrAIOXyfbbg_4c-dkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطابق گزارش (CBO)، هزینه کل برنامه تجهیز مجدد ناوگان نیروی دریایی ایالات متحده با زیردریایی‌های هسته‌ای، حدود 275 میلیارد دلار برآورد می‌شود. هزینه ساخت اولین زیردریایی از سری کلاس "ترامپ" (Trump Class BBG(X))، حدود 23.4 میلیارد دلار پیش‌بینی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140364" target="_blank">📅 13:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وال‌استریت ژورنال: کاخ سفید هرگونه کمبود ذخایر موشکی رو رد کرده و به شدت دنبال نفوذی توی کاخ سفیده تا ببینه دلیل نشت خبر کمبود ذخایر موشکی کار کی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140363" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35faa8191.mp4?token=HSeNlej1I1v4zReUkYrkBUWLhpODN5yi90VIcVvfg0HRFcCPR1jpDubNqWEwxNUNiPzVyZTijjbf63jBS7gZxq7zIaJmrK0BhgDi-MOhie9xgaTRbDdMbXPDVPiuaOI2iOT3W56DFLK0Fn07pOfg1IDu5DpD6QRYZLSqXXpPps8gXtE_eQ0cl9LaadXlW1B4k2wt7DugQoeVAhjz35mCITaHKuyY5wXTC7P6IwqPaICoahXfmeTIa8sWxqIcGN8PhEk-DXPkSRsIF8aasCyatxkHPPWeA307a1aY006RmJxYk1n4kqQPIsasJ5MWkk1F9m77zRM0oV1HHiHKTpS2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35faa8191.mp4?token=HSeNlej1I1v4zReUkYrkBUWLhpODN5yi90VIcVvfg0HRFcCPR1jpDubNqWEwxNUNiPzVyZTijjbf63jBS7gZxq7zIaJmrK0BhgDi-MOhie9xgaTRbDdMbXPDVPiuaOI2iOT3W56DFLK0Fn07pOfg1IDu5DpD6QRYZLSqXXpPps8gXtE_eQ0cl9LaadXlW1B4k2wt7DugQoeVAhjz35mCITaHKuyY5wXTC7P6IwqPaICoahXfmeTIa8sWxqIcGN8PhEk-DXPkSRsIF8aasCyatxkHPPWeA307a1aY006RmJxYk1n4kqQPIsasJ5MWkk1F9m77zRM0oV1HHiHKTpS2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترکیه، اردوغان وارد عربستان شد
⠀
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/140362" target="_blank">📅 13:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olQqC8iy5Wj4jeGoM_cMO4iLre1o06VpTjnA9qCwHTPGReu0K0PkiEXa2F2DxBLOrRWDr7NqBRj6YUwMqBg8yu_JGnJriFPd7Ut6PNIqSnJE7O6rLdh94McqtocGMAYWH7RUZXkvZNIjFuh5FHaxxsjHozNYCe3XTGZsK7AMSqvtUNiPQq5gz6ECY22n_2LnQFSPYTtgLRKpIe5zngpXOjb_OvCwQCu6tyQhcH9azsL8DGM2YhARukJbgurwVDOvRalj_WHbcIt5k5K-4DEm38TqFLaLrB36yLXCKFosgweRo47AFeZAIuatsFwNBCMMe-wM5rxbUqii4uYdaIWyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی : اتحاد سه کشور منطقه در مقابل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140361" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Zlimw9aXfZb5JuIv_D0HbUkOQciED7fwzYmt4qqtSz2S-aXikkbPjqpza54ATNowtutLO8p1JfBD1ucGOnZ1ROgs0Nnch6bV_BFhTbkQ-vyip2Sf26YGYCTjl5A1qlxDZU-3m7OwKa50ZDm0x89j1WpoxCLzwbYdcEqoHAKPU39TE1NwmVOc8fEtzM8RKdpAY8A61Co_-A2-1Q5w9vxc9jZ9VB8VqaDVk4PLDLQsCly0Jbvxpf51MqX1SlqLf2TouOxtuVvqPUupprpymxDA2FNQmtxgBAKIJ9vUOq2CDvjXkjs8H81iJUfGzLpe5-iKtSD_Cc4ymZ07d4O7_QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای شناسایی و نظارتی دریایی مدل P8-A در حال پرواز در نزدیکی سواحل عمان مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140360" target="_blank">📅 12:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرنگار المیادین: انفجاری بزرگ پایتخت مسکو و حومه‌ی آن را لرزاند.
🔴
صدای انفجار احتمالاً ناشی از عبور هواپیمای نظامی از دیوار صوتی بر فراز مسکو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/140359" target="_blank">📅 12:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرماندار منطقه «یاروسلاول» روسیه اعلام کرد که پالایشگاه‌‌های این منطقه هدف «بزرگ‌ترین» حمله پهپادی اوکراین از زمان آغاز جنگ قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140358" target="_blank">📅 12:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره به نقل از مدیر مرکز عربی مطالعات ایران درباره توافق تنگه هرمز: عمان شرط انطباق توافق با حقوق بین‌الملل را مطرح کرد و ایران پذیرفت
🔴
در مقابل، ایران بر ممانعت از عبور شناور‌های نظامی آمریکا از آب‌های سرزمینی خود اصرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140357" target="_blank">📅 12:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شبکه خبری سی‌ان‌ان: توافق میان دو کشور ساحلی به‌تنهایی به معنای بازگشایی این آبراه راهبردی نخواهد بود و تهران تأکید دارد که آمریکا پیش از عبور آزادانه کشتی‌ها باید اقداماتی را که از نگاه ایران ناقض تعهدات پیشین بوده، اصلاح کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140356" target="_blank">📅 12:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: صدای انفجار مهیبی در مسکو و حومه آن شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140355" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی ان ان: دونالد ترامپ، رئیس‌ جمهور آمریکا، با امضای دو فرمان اجرایی جدید بار دیگر تلاش کرد دامنه «حق تابعیت بر اساس تولد» و پدیده موسوم به «گردشگری زایمان» را محدود کند؛ اقدامی که پس از آن صورت گرفت که دیوان عالی آمریکا چندی پیش تلاش قبلی او برای لغو گسترده این حق را مغایر با قانون اساسی دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/140354" target="_blank">📅 12:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45b8324347.mp4?token=NdyopsenMUGPrxwGZuGuf9JXReu8wP-6fDn6iBo-iis_8yL4AunGhNdJF-rk9DcFtHsSjcvZ3MzD44_dRRSk0BjDsVTMiaMbbETZJ78s0iDxkyaO2sLMzqzPd0CnUPH73liBeZP2V-n_2Lf3dHNWI1TXLVM1psb10arkPB59RxwXcRpXTXvpsAM3vUjltZ5jSHjXMps-fQ1hU8afR73k8zTV4kdDWeq6De-KtYKc93x9B0T1EzPjjQzGFzTQWNNm-hQWTO1Qu6aCAuFMXaiRtSf3YaEBU7hp0Nm1r0eMoiIZWHnCYxONkEmni1pfsMgcj9AbwX-vRgn3MXwpM_xYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45b8324347.mp4?token=NdyopsenMUGPrxwGZuGuf9JXReu8wP-6fDn6iBo-iis_8yL4AunGhNdJF-rk9DcFtHsSjcvZ3MzD44_dRRSk0BjDsVTMiaMbbETZJ78s0iDxkyaO2sLMzqzPd0CnUPH73liBeZP2V-n_2Lf3dHNWI1TXLVM1psb10arkPB59RxwXcRpXTXvpsAM3vUjltZ5jSHjXMps-fQ1hU8afR73k8zTV4kdDWeq6De-KtYKc93x9B0T1EzPjjQzGFzTQWNNm-hQWTO1Qu6aCAuFMXaiRtSf3YaEBU7hp0Nm1r0eMoiIZWHnCYxONkEmni1pfsMgcj9AbwX-vRgn3MXwpM_xYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دادن علف به ترامپ در تجمعات شبانه !
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140353" target="_blank">📅 12:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEspV7xWPgrTxkgei3LQJ1htNamDflm0bBglcXfHiSG7BW7AnqsrIIDwxbMK6HMFbzTfQTzKpy7V3GVeEErJKxcNd0Cx87-OAedEYrICgBDaziiUy2_Ud7xilSFOsmiPgcJ-7qredroDJjHuxAf-vFKOohl_XAJG7ovtu-Bf9h2Eo57m7PdVlYtmxCIxbD0DWlqn8Bty2og8O9URln_1Pw-f4tp6XD4EIdbae-MpET_kb1doYU2YqsMObiB1hNCTitn0xy8OjBX4xlIjg3rT9zJxpywQinFEZ69zVEb-7-W8yYMWt9LvplCxUDQ3Cq8-K2NFqvET3x7oIRgs1aGGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DY0K2t9o4kLcLnUaO3wJwciEN8jgYZI4ECQbt8k970IMJDxCkqTLEtStLwkfbhJgc3sM_8vOck2xwv_f-GGz5mJ6TNOtrX29ijMgDuY4ckr4eJkwL8zlbvTOeR7rUtVTLTvbS7a-ZdsoyxDN0TEaAuuDyj1_r08_JTS8HXpLcFx8OTnOP2L2CcAmIQHxiMnO1wsrm5ihcLaFZnSkCOM1VI6tW0BM1F3gRHHpQ5J2q0V0fpewFlKaXQrmASYoWzO039Qcqh4Q-_0EonU-ng0HLVFg8f2bln8Na6nwb3Tw6ff-YaCa42XRH0yh2tYLquvJIBieOZmOWiFC_AHGFf9zjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14930a815d.mp4?token=tZaGThPSKT_RPdx343zzdWs7g9p65WvCfWKgbZHVe-Wl4VLSDFjkUqhx8gaIVJIhWS9E-euLDS8Vi5IRcAzwJMj9Rb-QAA0ZKXDyU3lxyOzE7GmLZnGpIcfPq6_09w6DCCVgtkZsmhaj2hYXij5xdPNAElE1_ns_cjSbKCPTFUF3BreeTLFrQNA1lN4D2gruVS6AX05LbdGuUtuLU4GfKEhoiaUGZZq1FBeY1kMYK_MvDi-onD4YYIr-zLJQYY4bFJ0GSHwdcwqFsoJedUNgpcYHIa-RTDmL6Qa_z52Htncg5ARMEceSMFXQ5eSHQUzoROhhD3e0_UTbPy777zRBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14930a815d.mp4?token=tZaGThPSKT_RPdx343zzdWs7g9p65WvCfWKgbZHVe-Wl4VLSDFjkUqhx8gaIVJIhWS9E-euLDS8Vi5IRcAzwJMj9Rb-QAA0ZKXDyU3lxyOzE7GmLZnGpIcfPq6_09w6DCCVgtkZsmhaj2hYXij5xdPNAElE1_ns_cjSbKCPTFUF3BreeTLFrQNA1lN4D2gruVS6AX05LbdGuUtuLU4GfKEhoiaUGZZq1FBeY1kMYK_MvDi-onD4YYIr-zLJQYY4bFJ0GSHwdcwqFsoJedUNgpcYHIa-RTDmL6Qa_z52Htncg5ARMEceSMFXQ5eSHQUzoROhhD3e0_UTbPy777zRBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو منتشر شده از محل اصابت بمب های گلاید GBU-39 آمریکایی به یکی از سایت‌های پدافندی جزیره خارک و محل استقرار توپ ضد هوایی عهد بوقی ZU-23 این جزیره طی دوران جنگ را نشان میدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140350" target="_blank">📅 12:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/140349" target="_blank">📅 12:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تخلیه فوری از بیشتر اردوگاه‌ها در استان‌های مأرب و حضرموت به دلیل حملات مداومی که تا این لحظه توسط نیروهای یمنی انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140348" target="_blank">📅 12:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f683736cc.mp4?token=gw-zrNRa07nfm8wx4Eh1JGZmvSA7zejLLdlm0ojyXYKulmqMy-ud_hzKyZLEDris9MIHzDfW1-Yz9XM845_7qhGvHhosCQU7l_ordgavREru4LZzUGMDxjb7nB873bdDYmKeePoRj-SLEBKtqf1EfRk88uMvlP3G0EgcFswqkgeiaLWdv2li_CZQxqD3WQwaz6tSI_tgriO9bGrYoFjxb-OCC9hup4jEU4K6DLHdhZUHNbKoEYbp567JXIZq6Mx7WhSnHaBj1F_39jBKareaqQUwk40BuTbmM4dAy0u4qyTLQw5ql6aPCQpjA8_R-Bw929Qs7xfc6VGHcPKA7_Y7Bp170PnQIobpH7mgVeuhCD2xIpDImvWLP_COXPfGOEZRbMCzH50N0vujAvSxvnkGtIaLVUlBp649bQsw7Eq17aSJ4tYkPGWkOMSCiRfhnF9ialvBds_oovUX9gpI-Fi8yyatLaK5o2_OYV4T0sg-rhVzU2UO589YJrikJRHllvhwZ5bJNrNV1BQsNjeRCoz9smc2z_jgQsTBla5liFhuZU6Ft_ZhlT3VjTgKfXmSVPcbMiP8xdRHHMUjuc5Uoej22NI9xWVKnu1I5iWMaIjdUlVFYATRyTwytYi0W7FSdp2PX6F2lR4_vkWEHy5V7uMmIFlSJS64D2ovoyPhx6Wp018" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f683736cc.mp4?token=gw-zrNRa07nfm8wx4Eh1JGZmvSA7zejLLdlm0ojyXYKulmqMy-ud_hzKyZLEDris9MIHzDfW1-Yz9XM845_7qhGvHhosCQU7l_ordgavREru4LZzUGMDxjb7nB873bdDYmKeePoRj-SLEBKtqf1EfRk88uMvlP3G0EgcFswqkgeiaLWdv2li_CZQxqD3WQwaz6tSI_tgriO9bGrYoFjxb-OCC9hup4jEU4K6DLHdhZUHNbKoEYbp567JXIZq6Mx7WhSnHaBj1F_39jBKareaqQUwk40BuTbmM4dAy0u4qyTLQw5ql6aPCQpjA8_R-Bw929Qs7xfc6VGHcPKA7_Y7Bp170PnQIobpH7mgVeuhCD2xIpDImvWLP_COXPfGOEZRbMCzH50N0vujAvSxvnkGtIaLVUlBp649bQsw7Eq17aSJ4tYkPGWkOMSCiRfhnF9ialvBds_oovUX9gpI-Fi8yyatLaK5o2_OYV4T0sg-rhVzU2UO589YJrikJRHllvhwZ5bJNrNV1BQsNjeRCoz9smc2z_jgQsTBla5liFhuZU6Ft_ZhlT3VjTgKfXmSVPcbMiP8xdRHHMUjuc5Uoej22NI9xWVKnu1I5iWMaIjdUlVFYATRyTwytYi0W7FSdp2PX6F2lR4_vkWEHy5V7uMmIFlSJS64D2ovoyPhx6Wp018" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری جدید که نشان می‌دهد یک پهپاد ساخت ترکیه، متعلق به سودان، یک کاروان نیروهای RSF را که از امارات متحده عربی پشتیبانی می‌شود، در نزدیکی مرز با لیبی هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140347" target="_blank">📅 12:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSkUt3tKDhcDp3DZo_U8nQc1GN_yvhFzuv2T50awMEljayvoLMHaXQL329BAaFyPfyul3o7GG8mCqkS8OexovS8a9Z7zvOFGOPuu7ICjFe5ThzWMvPYPGrkZaU45z7hjanSCr1EJq5dAWbfd3XwkNkdy2ugIkFagkDVX8BHlhHeT7imBRZIPI7ZuIT8SYTEaPq2ITsVGPeOL7qcXdaGfaJWdC_tXueIcLCwKPMjetP9p63jW_qJmxMwmGMx-Cx4vfU0XguMjRz-fUDNzuzG9VLlB9FZyi8ZrqBun99yBiApPXsNLgUUbez61fCytgFb3yH6ZF11Uhwl09AEk_dKo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پولیتیکو: نگرانی جمهوری‌خواهان از تأثیر جنگ علیه ایران بر انتخابات میان‌دوره‌ای کنگره
🔴
جمهوری‌خواهان آمریکا به‌طور فزاینده‌ای نگران هستند که ادامه جنگ پنج‌ماهه با ایران و افزایش قیمت بنزین، به یک چالش جدی برای آنها در انتخابات میان‌دوره‌ای نوامبر تبدیل شود.
🔴
به گزارش پولیتیکو، قیمت بنزین در آمریکا همچنان بالای ۴ دلار در هر گالن باقی مانده است؛ رقمی که حدود ۱ دلار بیشتر از پیش از آغاز جنگ است. جمهوری‌خواهان نگران‌اند که افزایش هزینه سوخت در شرایطی که هزینه‌های زندگی همچنان مهم‌ترین دغدغه رأی‌دهندگان آمریکایی است، به زیان آنها تمام شود.
🔴
برخی اعضای کنگره و فعالان انتخاباتی جمهوری‌خواه می‌گویند در آغاز جنگ، هماهنگی میان دولت و نمایندگان جمهوری‌خواه بیشتر بود، اما این روند کاهش یافته و برخی جلسات توجیهی اخیر را فاقد اطلاعات کافی و دور از واقعیت‌های میدانی توصیف کرده‌اند.
🔴
بسیاری از جمهوری‌خواهان اکنون خواستار پایان سریع جنگ و بازگشایی تنگه هرمز هستند تا فشار بر بازار انرژی کاهش یابد و قیمت بنزین پیش از انتخابات پایین بیاید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140346" target="_blank">📅 11:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWx8Q4poVHcoS5ByiX15yyYmfbbRDLRS8cIjb2gBtdUVCgzjxIU82iu3XK9lkX-scfWGz2klXkGV9VfO767RKGLX6eNEcMiMOmHD83Mh4NGS2VLc72vaFE8FbMrlb8sU-J8gmKq4B_u2P0_bBsMRE8jrwshPj63KSfNUd8RsmSTxKr7rng0R-Tudr--PeXw1NJhLzpyWogmvcB0Koju3GEeZ4OKIXloZU8EDFAkZZYr7K3jK3Bwe9AoYwvcPGAn15XgbYA9wuuhqt-Kh7Dcu02BC9P-S09T8Wjp08O2JOsGBtNrMhx5EofSQC45ksYbN4YNZ8I2ikxsahlJoBGFGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافقنامه دفاعی سه جانبه جدید بین ترکیه، عربستان سعودی و پاکستان که امروز امضا خواهد شد، رسماً با نام "توافقنامه مکه" نامگذاری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140345" target="_blank">📅 11:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc42b1a82.mp4?token=LoFTGbaB3O9yt16p5dOiUstumfJtbekv5FFMOqK39615zkRm89ypFJgCfiBcSdx9k6d5CCdCObOb4OYbKPH9AHfJntKS9JQeyjePcAXVXA0_2PwsgdR_J3z2VLff0ezYUAnUyF-2POZxl7XVfpvvvQ8Hp7dP-f7kigQn-718pnzgRj1qDvyENeZic-gxBOWIpny2ME1_hoBniXRsm4ogqmT0N7W7WNYRbGV0KsfYwuoWQJO3DhtQmwEM5K7s8cRFuuckPoD_QdktuLxvz8uyasGwL_kV_emit7HlMBZUXaZwMEVE_k49N1_iRr9ez2a0PFalJOoA7o5quJkmA-9L9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc42b1a82.mp4?token=LoFTGbaB3O9yt16p5dOiUstumfJtbekv5FFMOqK39615zkRm89ypFJgCfiBcSdx9k6d5CCdCObOb4OYbKPH9AHfJntKS9JQeyjePcAXVXA0_2PwsgdR_J3z2VLff0ezYUAnUyF-2POZxl7XVfpvvvQ8Hp7dP-f7kigQn-718pnzgRj1qDvyENeZic-gxBOWIpny2ME1_hoBniXRsm4ogqmT0N7W7WNYRbGV0KsfYwuoWQJO3DhtQmwEM5K7s8cRFuuckPoD_QdktuLxvz8uyasGwL_kV_emit7HlMBZUXaZwMEVE_k49N1_iRr9ez2a0PFalJOoA7o5quJkmA-9L9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدعت در دین و خراب کردن فضای کربلا با شعارهای انحرافی توسط حامیان جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140344" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
از صبح تا کنون، حامیان انصار الله حدوداً 10 موشک بالستیک و تعدادی پهپاد را به سمت پایگاه‌های نیروهای وفادار به عربستان سعودی در مأرب و حضرموت شلیک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140343" target="_blank">📅 11:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آتلانتیک: پایان جنگ علیه ایران حتی اگر به سرعت محقق شود، منجر به کاهش فوری قیمت سوخت در امریکا نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/140342" target="_blank">📅 11:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش ها از انفجار در مارب یمن
🔴
دقایقی پیش  منابع از انفجارها در مارب یمن خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140341" target="_blank">📅 11:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140339">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYQVPjDXzpI3L8dhfMm-1mHpbPJmxpmcGhZpeBGCtV8qeTx1wrWbABrIYpBOTGjLeQ2nZ4Wd0OfQgS696Rvgv84dByrQe2REyTzHjxkyUndNL0AEaJ5IuLeQNXCeMA_VgorWYoqGe_HrETW7A0cvheke92N6UaU3R-OILQfaTBbQd0epOphsG8vcgcovgTc1bGWt4GqViw_p-j9MtFP_igcik__ANuac8MeETcYM7DX5wA_25x3-1R9omYp7pG3oSmH-JR2X9AqefIRs7I3Ksa5QoAI7b5SHf6hDc18JMWIcv9GTzYb2ZJJysCXo1jTShZ_1e3fcEi0kEMCM20fI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJZhdrQtxoLomcUUNA16B9L7y5OiLn8eZ1_wt3qO8z-EGNdGGejSURxNCJ2F-VY42f8GQunq_MBBN_Dyt5F-28n_E7P3gBpPJs6gLJ27uOrCDr3nX8aqazL2MjdqNXkCB0skaEvXepb8mhIhuqqPC4AoTVjLTr2Cra1pdsh6miy1UWgaLphnfEP1dBswk3wxPlmD1G_IRU3I3IyV9IcBGsBso0bCocJZPOLq8BT3g21PAGeZ8ZNbj7J0mAqnE9TkiyKH0ydqdde1ikp3AGGmAKuyvCaMyHjIe7QTtxfi96uOzkRsc5YYUYDinhK7Y3rWHS5kjHmc7Sc-Ljgeimr5Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
3 فروند هواپیمای آمریکایی تانکر (تامین‌کننده سوخت) از فرودگاه بن گوریون و فرودگاه‌های عربستان سعودی به سمت تنگه هرمز پرواز کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140339" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140338">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
طبق گزارش وال‌استریت‌ژورنال، ارزیابی‌های جدید اطلاعاتی آمریکا نشان می‌دهد که روسیه ممکن است به یک کشور عضو ناتو، حملۀ محدود کند.
🔴
این ارزیابی که توسط مقامات آمریکایی در اختیار وال‌استریت‌ژورنال قرار گرفته و سنارویهایی ازجمله حملۀ زمینی، سایبری یا استفاده از گروه‌های مسلح ناشناس را بررسی کرده.
🔴
طبق این ارزیابی‌های اطلاعاتی آمریکا، حمله روسیه به ناتو در فاصلۀ پاییز امسال تا سال ۲۰۲۹ انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140338" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140337">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3NVWP9iY7491AOtAkZ1YTNOlrDahrGltYgS3U394vW83nIeRh_yyUVsjj2n4sCVGWfQ4NYzZOl4mbWFS390iX2yG8OfeZU2uVSqIXsEyR9w_3JPoo2N2UWwPgQOskwtaLyayAaiD7IPIZgurGUBB2mFWPTXTg3mUaldNvKlWh3jsf454cWu0DFNOlCkRZJA9v7Zu39rNQI9m87FN5UfgwEpqQ5gZ8Ox-sTlaYjxX2ftgnpw440e-4GHBXeMCmzF2PT-sAeH4R54utPLqVG3zDmrKMAiCJ4itVWBpqBZYnDT6QtYIScElHGSkltsvAsicIfE4LEerXRuRYkFbfqDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان: ما پرونده داعش در افغانستان را بستیم و آن ها را از بین بردیم.
🔴
ما هرگز اجازه نخواهیم داد کسی در خاک ما و از خاک ما علیه بقیه عملیات تروریستی انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140337" target="_blank">📅 10:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نیروهای امنیتی عراقی در بغداد مستقر شدند تا جلوی اقدامات احتمالی گروهک مقاومت علیه عربستان رو بگیرند
🔴
نخست وزیر نیز دستور اماده باش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140336" target="_blank">📅 10:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR1383xp0QmgF0XGmaj4-x7v_K5VUXHXE5CBokuBBkuz-uILJSWO4w6W1gWURYxBDtDWRgxmxq2wByIOal5Jg_JXeoaXd8D7qk_RlB_qeXrUVHvMAVx0iVOMACu3tiJ4MltBCKrZsnCrFmniyWqOpT2gkC1FW2rylrj-syQPiIL96g0hrvhE1EUnF53dDy0LAAMtAboBPrhZwtB2t3bTy16V0zCbRXN3QiPNUhN7thruygEYAG2WThQS_1dlo6fqzB01mMbW4IjGtjJ8Kgoe4ylNu-HB-xT_85WAopwsiqEOigLkQmL5Rh2gGlPTZ9XYG5o1bR3uxeL6LdodZxIOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادهای بدون سرنشین گران-4 روسیه به یک کشتی در سواحل اودسا، اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140335" target="_blank">📅 10:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffbc4c05c.mp4?token=n-amZ6YbEJ44XD8jVg1cWU5f5_LPyGi9MwbkA9G-HN8ZJRgXAYrxtd9quwv4QJ6hugXv4VP9gUBrrmBEK8HPZRW1xqNunu4fcmOBqxdOTczzStBG0Hq87zBWimk9PVqeKckZfr1oPAgVNESvVv-gxW6MIaMcWeOHwR6KPBCtl94IGBMAO3hkxet0d9qC9idgw1awPAw1iEtA5OLDZ21P9O1Ggf15UabIHIth8ro-9QP2GBlT_ZC-152XnMJDJyFEjcL3ljRGF3jWsbU2vwpMhhWvZUGH0lKWSde18vbF8dFmhRStUeQimFfm8BdhLqEAfq4Gf1ZFWjAwYDq6vcLQcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffbc4c05c.mp4?token=n-amZ6YbEJ44XD8jVg1cWU5f5_LPyGi9MwbkA9G-HN8ZJRgXAYrxtd9quwv4QJ6hugXv4VP9gUBrrmBEK8HPZRW1xqNunu4fcmOBqxdOTczzStBG0Hq87zBWimk9PVqeKckZfr1oPAgVNESvVv-gxW6MIaMcWeOHwR6KPBCtl94IGBMAO3hkxet0d9qC9idgw1awPAw1iEtA5OLDZ21P9O1Ggf15UabIHIth8ro-9QP2GBlT_ZC-152XnMJDJyFEjcL3ljRGF3jWsbU2vwpMhhWvZUGH0lKWSde18vbF8dFmhRStUeQimFfm8BdhLqEAfq4Gf1ZFWjAwYDq6vcLQcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از اولین لحظه بمباران بیت رهبری که به تازگی منتشر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140334" target="_blank">📅 10:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0Dm1jAA3Jz7s546m7rgG4ktPVJe7xmqwuoCEkTxxNJV2HMFVMGS1yyuhau7JqEAZCdf9gQehLevXvXCeLlC62q7rbfoHM3zd--AagKRwZPC-b-KL1Fy4auJwjBu11-9vy2ZOUC-oPv3r2QBqL2QMILovSQEZJ0Hcy86zUPU_nzIf109BxkkZqnlPuPwlaBTKbRNh3-Yt7pPF0OQlT3OHwoJnkmITTky-vf05WceVQCObxVfM2MBSrvXUR4ykNc2mvC3L660OyJ5GV3078xWKDGZ10_Xikz9OCFOf2RuHCQFg64eOamXf1PX3jr9mGILfmB7l-Pc76itcJYKkzqmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه، به عربستان سعودی سفر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140333" target="_blank">📅 10:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8034b4ceb.mp4?token=aUj25gPfuaYqil6uT6e4ViGQvc0cs8rI_XrhNyHOrAXw7FUt2lbCYLaWW0cu_h2_YTC3XzEg4XggaQyHEvPFS8DkCMZVtXSXXr0Ieqq_0qg8kTmm8enGifbaqExbU0GQeaF3XLZvJ71aYQr_IJ4xM7bmp8b0cB3lVjdeVEv-GS_WzFjwh2o6tVcP1vDNB0FrobrzKX2i_mhHbUDaQ9NLGRwLzyuPoxpUjqCX7zFq3x6cfLLh-Z9VyS4ky1Pc9k0-XSqH2Js9NGlJs0cr9MMxX8a4POf8u1nAAB0mwmoeBtl-mMhI9PEx0Ogo_YmhHJWe_zw6sOSqi62x3FhUuMWClw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8034b4ceb.mp4?token=aUj25gPfuaYqil6uT6e4ViGQvc0cs8rI_XrhNyHOrAXw7FUt2lbCYLaWW0cu_h2_YTC3XzEg4XggaQyHEvPFS8DkCMZVtXSXXr0Ieqq_0qg8kTmm8enGifbaqExbU0GQeaF3XLZvJ71aYQr_IJ4xM7bmp8b0cB3lVjdeVEv-GS_WzFjwh2o6tVcP1vDNB0FrobrzKX2i_mhHbUDaQ9NLGRwLzyuPoxpUjqCX7zFq3x6cfLLh-Z9VyS4ky1Pc9k0-XSqH2Js9NGlJs0cr9MMxX8a4POf8u1nAAB0mwmoeBtl-mMhI9PEx0Ogo_YmhHJWe_zw6sOSqi62x3FhUuMWClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود غلیظی از اردوگاه‌ها و پایگاه‌های نیروهای وفادار به عربستان سعودی در مأرب به هوا برخاسته است، این اتفاق در پی حملات نیروهای یمنی دقایقی پیش رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140332" target="_blank">📅 10:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a48272dc.mp4?token=vf1k7gO5BlJ6pDVLAWfGt-69ih1jLNG4VpBM7UvGzD9TIeT9sqhvwfgWxs33OWeOeJBJTo76Isjh2J95p3Jl0Tjlpo7Gf1JLbLK6zOh8off05m4yxZ4Q5ttNwCs7JYfWEghynNReaYSNrfs4uMnHuO5uR9qK2T8ZHMy22Yj3nZAEKKa2dPXHPcJjLO0H8Lw0SrjRbzWokAz8x7RBE40bYmxHfbArLXAcFvrhD5IFHDEdTFX7OnLp7YT124-P7HTkdolPYqOrBtxMGWsQ7vaO16ZArSpw6L4u_yOsm4tBWKdEHXG_bvY8v1mnDy5kkzvppB6ALhkJXTVlLqaei2ZsSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a48272dc.mp4?token=vf1k7gO5BlJ6pDVLAWfGt-69ih1jLNG4VpBM7UvGzD9TIeT9sqhvwfgWxs33OWeOeJBJTo76Isjh2J95p3Jl0Tjlpo7Gf1JLbLK6zOh8off05m4yxZ4Q5ttNwCs7JYfWEghynNReaYSNrfs4uMnHuO5uR9qK2T8ZHMy22Yj3nZAEKKa2dPXHPcJjLO0H8Lw0SrjRbzWokAz8x7RBE40bYmxHfbArLXAcFvrhD5IFHDEdTFX7OnLp7YT124-P7HTkdolPYqOrBtxMGWsQ7vaO16ZArSpw6L4u_yOsm4tBWKdEHXG_bvY8v1mnDy5kkzvppB6ALhkJXTVlLqaei2ZsSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس خزانه‌داری آمریکا از احتمال توافق با ایران در آینده نزدیک خبر داد
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد: امیدوارم در چند روز آینده، ما به توافقی برسیم و پیشرفت کنیم. قیمت‌ها به تدریج کاهش خواهند یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140331" target="_blank">📅 10:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خودتان را خلع لباس کنید، بعدش هرچه می‌خواهید فحش بدهید و دروغ بگویید
🔴
محمد مهاجری نوشت: آقای باقر خرازی که پرهیز دارم پیشوند حجت‌الاسلام یا هر عنوان دیگری برایش بنویسم از جمله افرادی است که نمره اخلاقش صفر است.بر فرض که همه تحلیل‌ها و خبرها و اظهارنظرهایش درست باشد (که نیست) چون بی‌ادب و بدزبان و هتاک و زبانم لال، دروغگوست ،  پشیزی نمی‌ارزد.
🔴
متاسفانه باقر خرازی تنها نیست و نظیر او را در مجلس هم داریم که معمم‌اند و در عین حال بی‌تربیت و بدزبان‌اند. حتی اوردن اسم‌شان هم کریه است. همینطور بعضی وعاظ
🔴
این آدم‌ها چون لباس اسلام پوشیده‌اند رفتارشان پای دین نوشته می‌شود و به اعتقادات جامعه آسیب می‌زند. کاش آنها لباس روحانیت را از تن بیرون کنند و هر کار زشتی می خواهند بکنند. در آن صورت لااقل دین خدا را آلوده نمی‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140330" target="_blank">📅 10:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با ادامه روند صعودی خود به ۸۳ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140329" target="_blank">📅 10:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارش ها از انفجار در مارب یمن
🔴
دقایقی پیش  منابع از انفجارها در مارب یمن خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/140328" target="_blank">📅 10:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a2df6454.mp4?token=QXJ9d6F-XZm_ZsNdkQyGQS2pvr7rLjcyCSmjmlz4doXxaeRGbG7fy1mlQfdyvcgXR52h3s1k-me2J6y06dCKKV5JqDNG_T8vHlbF8b5nz92FKio5TIuNvvFeAPNipFizUIgEFsDXmQR_7OUD1Ln5pr9znaVbOP05jsCGATcSBHDAAVviuUNAA27f_Yrqe7ETyjuPAjVIA4CvrTxH0tcrNXYjJ48VzYzCrKuvXIPxQK668SdcEQjZFf1pbXbc3GcN82kYDdTaMpMac57czyg7AtiwJUWChQq_BVL8k3nHRfBk7pCFcvdZNNwmZQqx9lK-ZthDkfpSZ-zXoY5jlD2oaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a2df6454.mp4?token=QXJ9d6F-XZm_ZsNdkQyGQS2pvr7rLjcyCSmjmlz4doXxaeRGbG7fy1mlQfdyvcgXR52h3s1k-me2J6y06dCKKV5JqDNG_T8vHlbF8b5nz92FKio5TIuNvvFeAPNipFizUIgEFsDXmQR_7OUD1Ln5pr9znaVbOP05jsCGATcSBHDAAVviuUNAA27f_Yrqe7ETyjuPAjVIA4CvrTxH0tcrNXYjJ48VzYzCrKuvXIPxQK668SdcEQjZFf1pbXbc3GcN82kYDdTaMpMac57czyg7AtiwJUWChQq_BVL8k3nHRfBk7pCFcvdZNNwmZQqx9lK-ZthDkfpSZ-zXoY5jlD2oaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سندرز: جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140327" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ترامپ به سمت توافق با ایران می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140326" target="_blank">📅 10:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار الجزیره: سفر نخست‌وزیر پاکستان به عربستان در مقطعی حساس برای کل منطقه انجام می‌شود
🔴
امنیت منطقه‌ای نه‌تنها برای عربستان، بلکه برای ترکیه و پاکستان نیز اهمیت حیاتی دارد؛ دو کشوری که هر دو با ایران مرز مشترک دارند
🔴
قدرت‌های اصلی منطقه که توان نظامی، فناوری، انرژی و سرمایه مالی عربستان را با یکدیگر ترکیب می‌کنند، اکنون در حال همگرایی هستند؛ اقدامی مهم، به‌ویژه پس از تحولات ناشی از جنگ ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140325" target="_blank">📅 09:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHEQVfADmVCr-HNC4pNdr8OSa3gutaEh7goySjiaW0lsFdmQiRFZADcvZxszn2c6d832-hlcQPziXa255_B2ZNQXr_LBpO_pyrXQjUjAA6epWbGG1CtvFzzDV9JrvXYLms_pWS97m2usYx3ayQHRb5AixMZcpA7ClmbeiqysLnSSfIDcWHkSqjbym_Y8AFwSRlpMCW3kHPlMH0cep8Rw41MrfejmhsCN4yo3JfyQ6SdhkLBbiqzo6n81UM7FsGCRlwhN9CRgnprpOeF0GhuBcdeoqESxjUQNnmgjywBAL1_IbNtSLBS5TLKC4isTmZGIikYPek3Ve1BvAPH3TLVGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکس خودش کنار جان‌اف کندی را در کمپ دیوید منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/140324" target="_blank">📅 09:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZucdB_OXdW0MQcG4Ypw7LXxmNt9jR4l-_ps4c_QojovysbeYNfxCmklM5gE2RYpsInmgXknloUlnSnF7CyR4YjK1jF5EGr3QdmwiQwz-DMp6pwQg1271hmkhmEigBzArXq8Yca-FmKTcdYv8ND3teC80-N0oAC5zQjDUYVJQl2RhEemTkWnWUHzAvlYc1j5CSWOxL_qS1MAZYyEu0zlN5k2HHg4klbPGmXFeeR1_1LhbkDWtXKqIbecHCpFJ1JiYc4LSVrcwocJzGV6lZ7a__EM8jtNSI3aGOhxrrEqxKg-XG9BUUE-3WxTQHlV6Z1EJu-3cQ30c0eBfqAPnvxDj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم: وزارت دفاع آمریکا(پنتاگون) حدود ۴۰ میلیارد دلار برای جنگ با ایران هزینه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/140323" target="_blank">📅 09:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=oLjBv2yqzLy9W98GctQ8rao5UqFYH2BBfAy_uvnkwmfilTtVblPL5lODOFJ2h9P4NcOYUxHePq3sMTjcEIW6sQ5LyXYu7vKCWiKSIdmQn0iUZVH57iCtIwvXkGAfr4KJ6gY-Y3DnSxmKj6lPf6UOqFMBzvgG3avOBO-p4r8kZ0VwkHL1aNi2HC2pEdCTwA-dyOuV-mK7Ja4l8QH2SzJLs2fOYOFGPc0RZe0LuBb93rMUdOMh2YW3k16W7Gn-SRdcXgzqkGvRlF8sL4y84YKZItMKHrF0wnjhxb68ggiy8eJ3LhkiNWP6R5XqhJfWtWA4B4MwZnN6iUMVvikv81lCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=oLjBv2yqzLy9W98GctQ8rao5UqFYH2BBfAy_uvnkwmfilTtVblPL5lODOFJ2h9P4NcOYUxHePq3sMTjcEIW6sQ5LyXYu7vKCWiKSIdmQn0iUZVH57iCtIwvXkGAfr4KJ6gY-Y3DnSxmKj6lPf6UOqFMBzvgG3avOBO-p4r8kZ0VwkHL1aNi2HC2pEdCTwA-dyOuV-mK7Ja4l8QH2SzJLs2fOYOFGPc0RZe0LuBb93rMUdOMh2YW3k16W7Gn-SRdcXgzqkGvRlF8sL4y84YKZItMKHrF0wnjhxb68ggiy8eJ3LhkiNWP6R5XqhJfWtWA4B4MwZnN6iUMVvikv81lCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز بالگردها بر فراز آسمان بغداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/140321" target="_blank">📅 09:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در استان بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140320" target="_blank">📅 09:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGJPomGX0hXieQgVMjxbsnc_Fd6yiYI1AtP-JoC3fCaH__38hLu656iDbIzxmses_X9TylabpqwrjZbY86Xx2ybJ9ao3zkVTbEotcRZE-SPaesHTcniubgT-YfXngTkpnKLj-6AZlAycabUbKVXXWPYzAX_SEcUYap-9ZXowFX6KRFm-2YwZ11hkaZjyvh6qj0lJoFCftvOWGGgmcdPQFlsoLEPIQNgeU_cLA6R4ar3ca3zssZ3rzBo1C5BQ0LKSlDY3CcwDV5frkKChvJ9OUEuc7zC72A2F-h_pt8Zy-Vit3QPDyVjvoL5uy2pC9RumPnyzRYv6cUlZ2zNYCjvF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین دفاتر ۶ شرکت با مجموع ارزش ۲۲ تریلیون دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140319" target="_blank">📅 09:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دنبال تیراندازی در مدرسه‌ای در منطقه بانگ کروای استان نونتابوری، در شمال بانکوک، چندین نفر کشته و دست‌کم ۲۰ نفر زخمی شدند.
🔴
پلیس تایلند اعلام کرد که عامل این تیراندازی یک دانش‌آموز بوده، اما تاکنون جزئیات بیشتری درباره هویت مهاجم، انگیزه او یا شمار دقیق قربانیان منتشر نکرده است.
🔴
مقام‌های پلیس ضمن تأیید وقوع تلفات در این حادثه، اعلام کردند تحقیقات درباره ابعاد این تیراندازی ادامه دارد و اطلاعات تکمیلی متعاقباً منتشر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/140318" target="_blank">📅 09:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق پیشنهادی بین ایران و عمان می‌تواند به تهران کنترل بیشتری بر ورود افراد به تنگه هرمز بدهد و دسترسی به این آبراه حیاتی را پیچیده‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/140317" target="_blank">📅 08:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSKjIT6q5_IJYrM320FVrwBfS40IevlOLe3dLaXDxlUOmpA4zG0pQhz-y9pQT3gWbxskrMAFKtSl8ePkCPYHIM8McNzTQ1CDoyPIwM1OI67XMPYnUJZFgM_vD0nXXdDmQ0Jl_VvHpd66GOZ0v5byi6PRkeZ1ohEFTamq6YUnTtG60GeB6fXuyco93o4kUChpaPIik2pnIfSHisvwAjB5mzZ9wOUGnd10D--rS06G5zNp84Ibqpfh9iz5L1OfeIB8cSBd33Ry5M39q-cILru5gVnyd8DMUBeJM_fbjO4tKQ5olM3qRDsbE-hoMVe1N3pdSv08R1fyYuENC5yTSkGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ منتشر کرد:"دونالد ترامپ در جنگ با ایران پیروز شد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/140316" target="_blank">📅 08:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:  آمریکا انتقال بخشی از سوخت‌رسان‌های خود را که در فرودگاه بن‌گوریون مستقر بودند، آغاز کرد
🔴
کانال ۱۲ اسرائیل مدعی شد: نیروی هوایی آمریکا انتقال بخشی از هواپیماهای سوخت‌رسان هوایی خود را که طی هفته‌های اخیر در فرودگاه بن‌گوریون مستقر بودند، آغاز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/140315" target="_blank">📅 08:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615b2fdbae.mp4?token=AKGJaIuf_QulS8nk_c5wgOfOJcVpN5KH8kgdzN4krt8RgLf5Ry-C-u5xGD0FBQxzllQD4oO8hRWSmZ5DbJbHYEaIcX3Lx9eY53qC-QCNmOQIu6hcosu5inerhQOxIV8nh4gaXawBG20vApeU-qluEFKqzIjwooviW75COU_rdAl1BHsrzt3Pes94653F1w42RueWOIHzdIDbjwHhjtnkHkgIMYHVdGrsod3XIi-6fv3Mz-HLzolBdvUYe-OWtUCGMrRidUGIZfrUtF-gXfEVDP_Q4ZoX12D6sQ6vNIcF4R41fgFSfzg-jlTv8hPxwqDmFxLtskolrHvytyXUSme_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615b2fdbae.mp4?token=AKGJaIuf_QulS8nk_c5wgOfOJcVpN5KH8kgdzN4krt8RgLf5Ry-C-u5xGD0FBQxzllQD4oO8hRWSmZ5DbJbHYEaIcX3Lx9eY53qC-QCNmOQIu6hcosu5inerhQOxIV8nh4gaXawBG20vApeU-qluEFKqzIjwooviW75COU_rdAl1BHsrzt3Pes94653F1w42RueWOIHzdIDbjwHhjtnkHkgIMYHVdGrsod3XIi-6fv3Mz-HLzolBdvUYe-OWtUCGMrRidUGIZfrUtF-gXfEVDP_Q4ZoX12D6sQ6vNIcF4R41fgFSfzg-jlTv8hPxwqDmFxLtskolrHvytyXUSme_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا خبر جدیدی در مورد تنگه هرمز وجود دارد؟
🔴
ترامپ
: اوضاع به خوبی پیش می‌رود.
⠀
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/140313" target="_blank">📅 03:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc90d74a3.mp4?token=Fp2mSvl2Po3Kg2yWFWEntNjkw9kfnI8YheAGBRbysaV86LeH-VAAPdsMdN2QJo7hBYUyhcD0e2kXuk1DbTxZb-CuvvARluaO6I1M7HO9fItt9xEb8zNB70-xXIIKN0EkiQmXfthlR0t2q0KY53VXk4bMkCFl9FUMHqrrG_TrI0vRyIpktCxoeRrLoTrGuyMKJi-qdSzn8ZOenOvPRp6v_JIZqhsOGwwMNhyjTf9BTbOvBtB2syfa4fb7zJ2_6dsfyhl_i7CgALrtUW2Jx359uvsd4oj2HHuQZsKm8gFcTO83WLZ1SKdrVq_LbuyCQcMSOk8AAcUYeoQFLOQIiDxMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc90d74a3.mp4?token=Fp2mSvl2Po3Kg2yWFWEntNjkw9kfnI8YheAGBRbysaV86LeH-VAAPdsMdN2QJo7hBYUyhcD0e2kXuk1DbTxZb-CuvvARluaO6I1M7HO9fItt9xEb8zNB70-xXIIKN0EkiQmXfthlR0t2q0KY53VXk4bMkCFl9FUMHqrrG_TrI0vRyIpktCxoeRrLoTrGuyMKJi-qdSzn8ZOenOvPRp6v_JIZqhsOGwwMNhyjTf9BTbOvBtB2syfa4fb7zJ2_6dsfyhl_i7CgALrtUW2Jx359uvsd4oj2HHuQZsKm8gFcTO83WLZ1SKdrVq_LbuyCQcMSOk8AAcUYeoQFLOQIiDxMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای امنیتی عراقی در بغداد مستقر شدند تا جلوی اقدامات احتمالی گروهک مقاومت علیه عربستان رو بگیرند
🔴
نخست وزیر نیز دستور اماده باش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/140312" target="_blank">📅 02:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=J-3mqBIQkJim6cudi04aP4taTtzqagOJbVcY9SZpqPdXfrONiYJucz9TM25t17V0wldMfSCPgUKG5SUy0twTh32bVrqwQls3Kd76hrcm-hm7yIunUdnMaIHZ77g2x7JN7UNpvxT2VDh5JMLGFM1n5U_QgWUWgBHquL1uwAcPQUhNjhRGPUUHvAlZeYlIZJpVf6fUicLxYJwjLMerNZBb5fKLE5gPIhoKIOhBluMfd_EPbTyRwpG1CdM9VaMBtcfyk7qH_4z2iWfK1fE1g_npzZgEbK7FxdCYg4_SQsi01gqJc_Lx8JXoYDN0JMM6ShC9h-OoewA5t1KUXpePD4dOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=J-3mqBIQkJim6cudi04aP4taTtzqagOJbVcY9SZpqPdXfrONiYJucz9TM25t17V0wldMfSCPgUKG5SUy0twTh32bVrqwQls3Kd76hrcm-hm7yIunUdnMaIHZ77g2x7JN7UNpvxT2VDh5JMLGFM1n5U_QgWUWgBHquL1uwAcPQUhNjhRGPUUHvAlZeYlIZJpVf6fUicLxYJwjLMerNZBb5fKLE5gPIhoKIOhBluMfd_EPbTyRwpG1CdM9VaMBtcfyk7qH_4z2iWfK1fE1g_npzZgEbK7FxdCYg4_SQsi01gqJc_Lx8JXoYDN0JMM6ShC9h-OoewA5t1KUXpePD4dOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خرازی: فتوا میدم بی حجابارو بکشید، لشکر کشی کنید و برهنه هارو به قتل برسونید اگه دولت اومد اونارم بزنید، این دولت شیطانیه و زیر دست آمریکاست، اسلام همینه، باید ضربه بزنیم و ضربه بخوریم
به گفته خود خرازی، وی با مجتبی خامنه‌ای ارتباط فامیلی و ۴۰ سال رفاقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/140311" target="_blank">📅 02:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رويترز به نقل از منابع: ترکیه، عربستان سعودی و پاکستان امروز جمعه در عربستان سعودی توافق‌نامه دفاعی مشترکی را امضا خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/140310" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljqWXRpmR9isENZtNFuOB9Yq6XRyvHuS-oMq6_N6223sgiprN1RrvvkE35tbvGzlY3wBw4oG1X6otNF-BYz9Jlt4ywCa9zY88MVh_trl52-svxDpm6bud-Pjfo8vGd0rz3l2qf7tQolV7g9n_e7G_U9vyhJJufgVAM-HMHYwsCH9CC-4Metwt_S3wrqRkjSv0PTZLHn-sMl_-Xb_QCK96Hm1Jynd9HMh_1K2vRAsS5zOM9NfmlBkT9knfpso5HJqS_CBoq-jTjJyDuGurFM1jMP0HQhtKmkq14bWn6YE2FtgRxU6nnAzbLRxKTopceDkQ8QfOADWblQ1xc34jRNwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲ اسرائیل، نیروی هوایی ایالات متحده در هفته‌های اخیر، با توجه به تحولات امنیتی جاری، شروع به انتقال تعدادی از هواپیماهای تانکردار خود کرده است که پیش از این در فرودگاه بن گوریون مستقر بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/140309" target="_blank">📅 01:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVARVplJboUsWs1v-_vV5edypM_wy3S0jI40fbPvBjnmZzYSQgkllL6GBronUdi2otZl7FTTf2NgNdcODMRFAnkVbm2dAOiCwFK6RuiE7RpCBUTOZH3HMSvjw-pgGBk0Kr-XaNawuB3wdhXqTRTmH1ZLCzdYoW9aBnDbEz1YKyAfH0-cCfxs0LOv_AZqEiJkoAEjk9nsQzDT5pIA1HMG2VbiOR9olklSxd1TuJmLcsGmtQCRU3MH7lLM1pL1vabOXQ0_7mOnB95Tp2-zuOsRR3cMDulc46h-LiTw8Ckpif32TBh0VS2z2cmauyFti0MdIHxcdXL6BgR7l74xQJanBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باقر خرازی:
حزب اللهی‌ها تو مملک
حمّال
قدرت دیگران شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/140308" target="_blank">📅 01:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df7fc98fb.mp4?token=KMpqnDfmveofiiFsASXxDybjyN7T3-hf1buV_TXNJibRmZTgiA7CP95DtAIfsrpJM9CphMf8nR1o_Q3uMKmIu7HBV9c3nQQgFXeBDlQ8slkx77E-5b0GRIn8bFUvw9v8ALcetl8rUC3sLORX5xDDXT8g3jjtM1shIrGp0VTTOvCnBTKs5mVGec-4x5e0ZT6VugkL2Bz5V5ufgSCXh8tpjyDiWFf1uLhrhxom602I5uIdv9CcUJ0lKVaLq74gm3OjAhQOf9ytss2ZZYThMfFXZXlJLNFc2gfDuug7vpJPGZ4pG6uYMjB_ujk1mbfUcPFqXGhR99dO_pPatEsKlkp74A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df7fc98fb.mp4?token=KMpqnDfmveofiiFsASXxDybjyN7T3-hf1buV_TXNJibRmZTgiA7CP95DtAIfsrpJM9CphMf8nR1o_Q3uMKmIu7HBV9c3nQQgFXeBDlQ8slkx77E-5b0GRIn8bFUvw9v8ALcetl8rUC3sLORX5xDDXT8g3jjtM1shIrGp0VTTOvCnBTKs5mVGec-4x5e0ZT6VugkL2Bz5V5ufgSCXh8tpjyDiWFf1uLhrhxom602I5uIdv9CcUJ0lKVaLq74gm3OjAhQOf9ytss2ZZYThMfFXZXlJLNFc2gfDuug7vpJPGZ4pG6uYMjB_ujk1mbfUcPFqXGhR99dO_pPatEsKlkp74A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
🔴
سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود
🔴
وزیر دفاع با معاونینش در جلسه حاضر شد؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/140307" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIZaMrxC5w0TYSRQzCdoSgWDvNAJUQQoglmKK-kuQe7Hte--HeFfaUpxHCTEn5HD-3H-AvDlKR1btoUiqwDICt_ngAMwrXaRV6DpqEIQHY8k7dHLmfI-p2CRMEdnPM6tKncMH_jzDm3a6lE9W7xqJO4shNk_04oZQUJareYWKsUsK7UZDbzDBav-dRtngHju1Crq4oqOBpoSyvw5YffvV4eW3A-VJ2X_G3e9uRGILLfLwG5OchkKEmV-rD-uJnX_y5AObt1IngvdSuNQVLnhBQF-SiyFcqERwXEDz0qjYA9yG_-5G9XbFxLQVKH5rZNCsIZ18-DYzhIR7ZovoYbKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا شروع به عقب‌نشینی هواپیماهای تانکر از فرودگاه بن گوریون کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/140306" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD09vQMyOHIK4cEshYzJ99e2lThhE5y6kK2mFiAfttOfFifoRRdNgFnGgPCha1GNpF4AAIL6LRZXIfVBwW1viNwwd7LWmjhPzyQXH8O2hNkjLetrS2_SpfBLUcYR4wL7molg-lJ9ttbHYwpZqekSEjSgkSXJ2neQ_oaVIhMSGdPrDvC8PeePn2bncVDqqV4XvoJezttEYeZtWSirOKhUmgDr4ALFro0-O1O-KBt-sZotAVB5FlzVwrtQ9FhxrVglF4nmwpvaTgpVSvq-SWogE1izWNvWLlMpAwRshY2y2h-NbQ5hMvs8w585bYyr71HfiB0B8AU0Z7TdMReijCX6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام‌جمعه رشت : دستور دادم عکس هیچ زنی رو نزنن سنگ قبر، نا سلامتی مسلمونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/140305" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: ما اجازه نمی‌دهیم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/140304" target="_blank">📅 00:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است.
🔴
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/140303" target="_blank">📅 00:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها علی‌رغم محاصرۀ دریایی آمریکا قادر به کاشت مین در تنگۀ هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/140302" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ: تنگه کمی بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/140301" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ درباره مهمات: «از نظر ذخایر و تأمین مهمات، در وضعیت بسیار خوبی قرار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/140300" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4VDT5OOkk6UNlKd-DXusqfr_A2cPh0Ou0Sj4t9-jKqDef8Bd1Mz5k6rLKz5JL9olvPbxDRJ8EilIuXeLGBIcGoxfxEAn40nA9FFb_yO3EyAdt2Hl5GPXSoOsuE47qQevGmPwvKj2F8mxnIfI-gffweYp3QienQ0M91juOKe_fPeAWQszp17q4kiegYJl8D9YccDykDRK5_XW6dNerHQFkimLmJyAzKDCttxs8JWzazHupyD1kOckpb4EOyTodllH9J76Ua4v7dWz18uvvZa_GQrrpuVAd2582gysoJfEILj9nCNH6KHswF1DdTPy5SiFhSTmb8r4ikfPs2qC6br3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۸۳ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/140299" target="_blank">📅 00:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ : - فکر می‌کنم جنگ به‌زودی تموم می‌شه؛ بعیده بتونن این وضعیت رو مدت زیادی ادامه بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/140298" target="_blank">📅 00:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c703151.mp4?token=Vnv54sAAWq8kl-wmguUS-x6qZ06urKFzzNvEyB9uSByZ02Z46S61VfNejaHlZP2-NzdGXW87KyKBiCuFfltNHJrjA5I1k1R6KDHLsFqYcvuzlTFDWI_plFo_P_mkDJmlJOSeBbE7P83VmCAmc0VEphqL2ocU27_FItwa2qi-UkUNrNPwyXyCa3B3PkIBNZywcUD9UaloEbdrA_oMK8tq-03MLIMWDRuarkNNKxzITTo8KKkTckXV96UG6bw-m9N4kKB0m6_HPt7XwES3c0yK3-sEutl7qnu7Bn4hMvUUL1qyPR1vZl1gdpNkF9ib0oimKvUoR9Wgiur4UOEKw-MwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c703151.mp4?token=Vnv54sAAWq8kl-wmguUS-x6qZ06urKFzzNvEyB9uSByZ02Z46S61VfNejaHlZP2-NzdGXW87KyKBiCuFfltNHJrjA5I1k1R6KDHLsFqYcvuzlTFDWI_plFo_P_mkDJmlJOSeBbE7P83VmCAmc0VEphqL2ocU27_FItwa2qi-UkUNrNPwyXyCa3B3PkIBNZywcUD9UaloEbdrA_oMK8tq-03MLIMWDRuarkNNKxzITTo8KKkTckXV96UG6bw-m9N4kKB0m6_HPt7XwES3c0yK3-sEutl7qnu7Bn4hMvUUL1qyPR1vZl1gdpNkF9ib0oimKvUoR9Wgiur4UOEKw-MwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
- فکر می‌کنم جنگ به‌زودی تموم می‌شه؛ بعیده بتونن این وضعیت رو مدت زیادی ادامه بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/140297" target="_blank">📅 00:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkzlkjgKrv-GUTfpayZvgy0D5xv8uE-cXEodcLg1bvW-Nh11Xv5RYFohXStBliE1plsYy82qizabvus9rDSVkGyAbxK0Bc8mzZpj6herjWjuBfl2NfEIylfHsg4cMxHl7sfnpwMgrGmeiOPgiElYue6bniEgyISEq5SvQIBSmNQQfnKCvQOVur38WiCrV4QUhXj0vcSSoAuh2n4EyTJTIO54t9U2LYdC1ygbTCwcq8dPcKIaZR25btgxZOwt9KIKmB4J4Pn6oW3U9ndzafLlL4WGIEBfehObw70oO6BofMaP9msWX1z7bzSmwBe1LMF9iKR-JEFu6oZNOF-nV91BOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔴
‏اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/140296" target="_blank">📅 23:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از منابع: ترامپ ماه‌ها است از مشکلات احتمالی مربوط به کمبود مهمات آگاهی داشته و گزارش‌ها برای او غافلگیر کننده نبوده
🔴
ترامپ از این که این اطلاعات در نقطه عطفی از درگیری با ایران افشا شده که او می‌خواهد موضع قدرت را به نمایش بگذارد، خشمگین است
🔴
افشای اطلاعات مربوط به ذخایر، از سوی مقامات ضد جنگ درون دولت صورت می‌گیرد که مصمم هستند ترامپ را به خارج کردن از درگیری با تهران سوق دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/140295" target="_blank">📅 23:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8ZJWGquu2CE8tWJGepJRj-X7KqE3Oyq_Bw2n2BuN9KgUPvTNEpwqZaY9wC6j_dn_ZDXAaX7FlLdEiz2y3f6QBOBPIblCKhKnJIDg3hNbzsddaGoNHHPbCuiWttWgE4Sf-nzrrvi1yWq-H8vMRw8hikQIDUAjgfpHNNzTISQrp7duxGWvbdhha3iYaCSvXVjAxXtvSwZ9VbG0p8WSY82LndF9N_-2TUYiNmE8Gt3eUkJo2LlrphqS0PKS2tEvigZo-ePcsYTAVZG6K2LrlDd_yQ58wnJ5xW0ge4CIjEDN-AEl9N4a8Tp3JtyLMFmVlL0sNbAEN2Fb_3km3xyZCk37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: برای سناتورهای بزرگ جمهوری‌خواه، دوستان من «همه»، لطفاً توجه داشته باشید که نامزد کمونیست دموکرات مجلس سنای ایالت میشیگان، عبدالرحمن محمد السید، به عنوان شاید مهم‌ترین نقطه خود، بر لغو قانون فیل‌بستر تأکید دارد.
🔴
دیروز تماشا کردم و او در مورد لغو آن دیوانه شده است.
🔴
اگر موفق شود، دموکرات‌ها ۴ سناتور، ۸ نماینده کنگره، بسیاری از رای‌های انتخاباتی و مردمی، و یک دیوان عالی با ۲۳ قاضی را به دست خواهند آورد و من، متأسفانه، با وجود کار بزرگ که انجام می‌دهیم، آخرین رئیس‌جمهور جمهوری‌خواه خواهم بود! پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/140294" target="_blank">📅 23:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
👈
کانال کان اسرائیل:  رئیس موساد، رومان گوفمان، رئیس اداره اطلاعات و مسئول پرونده ایران در این سازمان را برکنار کرده و آن‌ها را مسئول ناکامی طرح میدانی برای سرنگونی حکومت ایران دانسته است؛ طرحی که پیش‌تر به دونالد ترامپ ارائه شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/140293" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=ZVKcDE7bSj-DyL9KyT0564V8fB7rk30-r2DTJ0MkU3UAoGnIMj_u1p3YKXnL5sx6u-G8exUPHb5Z6fK_I_UzPde_ax3WXbqaKClDKBr4vICLaB4Hr9B4p6ZPZIhWEjiVHqqA_MpVFS_BDAYCTIBv7rZSFM9bsWl8eA6cY-7a3PbX8vuTCJLukRP8vE2PmQ0RfgXI2Jylbgm2Z-nRAdKuWMjrISi9GuYqPSvQneQ6KvahTdbidHlyWUk7jws8O5u4nQIiBNVW_glWiKXV7nSxRqFHufSv2Owo7KwzzUimb_2CiCFnUfJ4KgKmVrrTEU0_t1GQazV09XFD1UElZc5fSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=ZVKcDE7bSj-DyL9KyT0564V8fB7rk30-r2DTJ0MkU3UAoGnIMj_u1p3YKXnL5sx6u-G8exUPHb5Z6fK_I_UzPde_ax3WXbqaKClDKBr4vICLaB4Hr9B4p6ZPZIhWEjiVHqqA_MpVFS_BDAYCTIBv7rZSFM9bsWl8eA6cY-7a3PbX8vuTCJLukRP8vE2PmQ0RfgXI2Jylbgm2Z-nRAdKuWMjrISi9GuYqPSvQneQ6KvahTdbidHlyWUk7jws8O5u4nQIiBNVW_glWiKXV7nSxRqFHufSv2Owo7KwzzUimb_2CiCFnUfJ4KgKmVrrTEU0_t1GQazV09XFD1UElZc5fSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ارژنگ امیرفضلی: «بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید...
🤔
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/140292" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مقام آمریکایی به روزنامه الجروزالم پست:
هر مسیر موقتی بدون هیچ مانعی خواهد بود — به این معنی که هیچ تاییدیه یا مجوزی و هیچ عوارض یا هزینه‌ای وجود نخواهد داشت. تنگه هرمز یک آبراه بین‌المللی است و هیچ طرفی کنترل مسیرها یا توانایی عبور از آن‌ها را در دست ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/140291" target="_blank">📅 23:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار حوادث:
توی شاهرود، یه پسر 25 ساله بخاطر اینکه یه مدت از باباش موتور می‌خواسته؛ باباش با سنگ میزنه تو سرش و به قتل میرسونتش و بعدش جنازه‌شو میندازه تو یه چاه 40 متری!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/140290" target="_blank">📅 23:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMJDEPY3hEmtNmxTTFxcUaoGvTJVGk2Nu_c0ulm60Ez_ecufzrEFtejH_5uGEHgOqYhJwSvPGC4qd_SvOqfDshOiC2sDLvCokm40KGa9rptONhSSnsxCkoMIF51DTdERUbIJCTciz9mHfiSmD-nCh68ZiXVedvvY3fOQ9uyHqNWTVXbua4ROaMDsuXVoJUjk0VAIsXUbIx1eXW_xH5ynx3DzNk17iCgajzzlSHD03o1a8hZAS0dUWBFVq3hkY3bwpUj9Y1O1YLFSFsQ0C9LREClHgsg9wF6FD8XDNVqmFHXCuKxWJX4M8ab0ftoPLlM6aiNhBLPIQ5QYNdSUDQ1ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دبیر شورای عالی امنیت ملی که از ۳۰سال قبل لباس و شلوار و حتی مدل کمربندش یکی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/140289" target="_blank">📅 23:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرنگار حوادث:
یه مرد ۳۸ ساله میره کمپ ترک اعتیاد تا مواد مخدر رو ترک کنه. بعد از دو ماه ترک میکنه و برمیگرده خونه. وقتی میرسه خونه میفهمه وقتی نبوده زنش ماشین و تمام طلاهاشو فروخته. همونجا بنزین میریزه رو زن ۳۲ سالش و آتشش میزنه. بعد پشیمون میشه و سعی میکنه با پتو خاموشش کنه ولی نمیتونه و زنش فوت میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/140288" target="_blank">📅 23:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUj8aR5WvCC4u60QHo3Ef_15T2ggg4k8kJIsmiz9IDFnSOCcULgLF5XJDAng1cxOjATFQSU1c9_f6KJOCnJij8mkl8rf3325aOye8ahwfqqSkAvIQVlTTUYRsS0I3lgFMtdm7jIzw8oYkFd5HgdfeFwVapkKLkjBqIMgs1YKejh_3b8rxIE_LXG3EbD5WODL0X8l2vl1vcu5xaO3SCcFoSYYE39MQS-9ZuvxM1XxaRruac8wpO0V5g6On1j_DUaZfKqD7pk0QS8iilFmzeaMcenwNo4hGjlP9G9aaR3dTEmKyVzRa02bF2MEjNvGUDWyRJOOe11l44IcH2tcQ6MYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جادوگر معروف غنایی:
ایران در نهایت آمریکا را شکست خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/140287" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ امروز با بن سلمان در مورد موضوع ایران گفت و گو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/140286" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9vudsCZrGc5ib_T8Y6mSxztCWhYVLg5H0fjWc8EvBzJ5lE-ZWhiVwFCVL0i0ug-Bsbc5fokKBEB1SDHFKq922EOWpwaJRCPaLBVhrFfR1DW-n3EhDfaWSjdVa9a1WVzkGsp6mRdTvWtm2phP54ULGyEbVLPhun1j4kIm2mzoiAvgnTiXAQ6ezWHSWNtSIO1_n45oQfs8kXcAP7Ividv2LoE3285cpTyaX8CxtA2F2G-JnRY-MceuOfP7CscJlgmPh2MFJL81DWq8M1AB2Np7RyXGLBcvgl4E_5JNsWrKCGC8vTOi4DTYsj4p2gkCW9tiO2DizJNUxHaD2VgWJ1t8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروژه ۱۵۰ میلیاردی به واشقانی بدون یک روز سابقه کارگردانی!
🔴
مجید واشقانی ملقب به خایه مال بدون تجربه ساخت تله فیلم، سریال و حتی فیلم کوتاه، قرار است برای اولین بار با این پروژه پشت دوربین قرار بگیرد. تهیه کنندگی «بریجتون» را جمال گلی برعهده دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/140285" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
👈
المیادین: عربستان دستور پنهان‌کاری درباره تلفات نیروهای خود را صادر کرد
‏
🔴
یک منبع نظامی به المیادین اعلام کرد «عربستان سعودی» دستورهای سختگیرانه‌ای برای مخفی نگه‌داشتن اسامی و شمار کشته‌ها در حملات نیروهای مسلح یمن را صادر کرده تا روحیه نیروهایش را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/140284" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
