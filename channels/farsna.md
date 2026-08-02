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
<img src="https://cdn4.telesco.pe/file/C7vkidNe9JAoRBpT8-7iaV8s8TPKvSpEVCT6mfTU-f-8OiR83gb1fh5t3wtgXqNKnwxxGGwBQQ9EbgdZFcg_t3uYD81Dk-jyFuMY2dMoMiIE_pMSz_vCEwhZ0NUqtYN17TAHG2asXb_rRfapLOoDnAn4LghyuIFfETlDThFLBE7ruNLQ81lAXBrytlbUc4QL1eo3qDu4rC6CrHYREWpl9Tu1H1jfeS9LR04qjcMY7mYSNr9PEqKxl8rtbe0h1SWC0XWaa6x_-P-ZBcZGaru3ojXg3FLrBdPmWyRnWzkzxloG3-YBkKnwL3HjlhzVAy1_DGCMFeHtQiFnfhDAL5f4sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 22:26:43</div>
<hr>

<div class="tg-post" id="msg-454101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ورود ۱۱ تن کمک‌های بشردوستانه روسیه به کشور
🔹
فرماندار بندر آستارا:  محمولۀ ۱۱ تنی کمک‌های بشردوستانۀ روسیه  از مرز آستارا وارد کشور شد و به جمعیت هلال‌احمر تحویل داده شد.
🔹
اقلام تحویلی شامل داروهای ضروری، تجهیزات درمانی، بسته‌های امدادی و سایر ملزومات موردنیاز برای مدیریت بحران و ارائه خدمات امدادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/farsna/454101" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی اربعینی مهدی رسولی در وداع با پیکر ۳ شهید حملۀ آمریکایی در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/454100" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454099">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poqeLA9daLVozk_VWNn5jIzfaH1uEcTqNoSEGOAN5DBceo15xGgUVKMLnnQRiaoVDeGO2XWwoTp0gMQXbgGmuJKx72ZC_WGVl2FeRCuro7b62-9qwjopgfsc32k_4UQ8sf2RT37Q4vpkNT-UkAhApX_j6dni-nPTJJt08OQAc-ENsWGXjdQF3zfO_rhrXP0PxKlwEmGn6E_M8nLZfRloFicJQdq0nhiSPur605jSSQZmU_2xWd1YqwinVzFoDfY0HHrxm_9KOd_pKa2yuhHo7w2PsHO_8Mhp9CFe3U6xuUSrS7fR9E_VWA67voZT5kGVs9Nzj1-sdnhjvn7okltiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: باید دشمن را وادار کنیم به تفاهم‎نامه پایبند بماند
🔹
تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود.
🔹
باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/454099" target="_blank">📅 22:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454098">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت دسته‌های عزاداری در بین‌الحرمین، ۲ شب مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/454098" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454097">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد مرکزی اربعین: به علت ازدحام از زائرین می‌خواهیم همراهی و حوصلۀ بیشتری با مسئولین و خادمین داشته باشند
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/454097" target="_blank">📅 21:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454096">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر ۳ شهید حملۀ آمریکا به قشم در بندرعباس
🔸
در حملۀ بامداد ۸ مرداد دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/454096" target="_blank">📅 21:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtUkQda3-xryFpEK9eQPulfT59zwVasX70XSXzPxVhHEyfSRSqJiIv9T-MOpM7Op2J1hQoE566mrw1oh7MJZYwQg4H8EhDu3rTrEoATPg1sfqtXvwgkRFqbCsV9iiQZUNYEdk1gs34EI1R14wVWZq8PmTPIXO5cp96YMRfUaEJ4LpMu5fVJ-0YHetSRw3LIrrtS0XQVRY5hSlUcSbUe1KDgfZJQKtpUh_rMjxSz6dxEfTlzWHBRXQmeOdR3oZncz3TNzDH9SLCr0ns57pPO-ADGNa7WnLYNjw9cRaYZXipCBdYXoPXL6H23D29bl_QXdC6haZt63xt7v14vIxlUXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSeMoLtmqlOGjWITP3IeRo3M5ofcb8ZBZbXZuKdr30vazvqC0lri-5ikEMKJIc-SQQGAuvmLy4xrVDbfODOqufUx7z9KfL0QOgcNo785mgY2_gFAfryME3H4I2V8Dq0g3pfn417mVNcvhfVhr5Jpv8sj1Ft0kZv47jl_RSTXpYisSi-SLxNw1jNqyh50SowWu2sTpgF-D2QLfbZhjd1t3rWVpwebqAqsZo8yGVuzh8JTkX-xkVMBaWApWfCdbU3GnNsFUhHkX0D7TMKM_gfLkr0fIHuceDPMC-PJcQGwDWQsDMX_oWlpXPAxlZ19gBLM7y0_mdE0LaLuTrrpJZBsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg4qyWjHhNrUPcnDrbACxOFTQgZH281VJVk2Mj7fagsmYhye59LFZsXBZnR8Jp5ImBrWQea7C_ZQXUTHqFE_rj9C-g9ETNSGUaPtgBbX2lXphel4i8Nz9j9LDdWJWI8FxthoWjY4aPZG3ZCg-vFzSMIMo8lQo2Xswv9lS9P6SKiDE1PUMnji990pA93OwX6pz3Jd8S0N_1LXsRShsDMWSVG8K3GtFUg4efpMWOBbYL6AQMq1zoql8fYRjgsofNqkXo2ikcZ8V8QOK-cySWC9XPwA-b9avGvvW0HB0hD_i1ZEG_kCRP7_spTBprhNxuAnr3Kx0fnEjMhwEMDSf6bZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMozjlBUfoBU9G9ViYeYAvh57dZThndydd94qxK6waaoLxyNKc3joLezN0keaNWin8EWNwyDtKeyLPMAtJZyVW7rAGrQNvvdb9GUmjbNADno31IqDXDZiKf8kUM-0IoSGxVrTrsB6o4xSlsoxmxGiTjlYM6mv0xPmQ1XgEpIEdG6vLccc7Ny58YliZI6fkeQlB81I_1SoYlV6AGMHTudCX54uZJDXLSaxaNLTGUNOuO1oLJ7YYzaN2PwzBsVmLxSH4xjKkEZgCHQf1G8iFr-bTWwu_ak6UQdjPg86ER3N7M8JYMNNhIws-xxcDDYZshd6uQvYNxTPh1YmGjvHTX0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN9bzTxa3RUHoX56AyHAPmsetUIcVPtVZhinI-TYRIF62lsFUR5gLRBpDc2su8QiO73BAkcVdIflmCMgoZE2DhZZnJWvBkNzE-S5RpIgy_BOR47MaYw4o57qmZ3ajJTBXb_SPaeNb_zNlSw75K4xF5bj2-l49pYueeskEjZaJ0Qfz_OES6NZjgMKf-jntTdTT1xIWYQjht7fwpokXAVimz04PKDBEamKbOknXidhjYVLRuGlazu1Igw9EVJf6iEav_ZhyCu1yNQCHsbvERLeBNnoqcwqk7yRj__EeATP76jE4IRGyiSuZtj_fsGUkmaARph-e7EQpIRcSdoeBjvFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-VB99b4cirvJ8barY8nJ0G6IxYiylNjzlZhg5bCv9zkHdVAu__Zl5B2GKgbQAUUmsiKNG2Bs4NnsCSxzieLtwm-A8JgrStuQ4smnDa8bilW7_AwqQS2DgfuKyy4ZzVyC9kMF27BVX8imevB19ZguWXGQiO_zHDkWHnsNBmsSao-weVWZOupOaKhnh5J8574WotUAR4zGhcw7XQ36opR3KhDzGlBWk6ECUAM5lSIFpP6XZNiozhc51bnly1kfgrZ9OD_vaf1TJ7eoCbnV9MxPAia6klO3DlnQh0DYBzgVUu9QemEZspLrujmS0IKaasrsqEafJnZIz20BNPmRyLYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQIMOCHy2q7UdCkV8tMPggPWCyw2BpXtAHA88CFfDPCXz69vCjIStHSKaBqAet4UpIybboZh1-LUg80WEZPmYHuUY5jNmO6AFZPqHqgIIXVTJAZtgNn5xIoTfnB7bQg7v3q_3TSvcHMZACEL7MknTg6FAo6t0I7rizdJz9kqpbv4DrBTvLlEO9XFh3f9bYXMPumI5T98B4yNXQI4uIZ0HsCJlzOUOnODHeGbKKDVP7sG7Qpp8D41Nyua9jfg1RKC0jPzNQEnS1nbUWnxwPiFdI7jir6APpHEFGeJFMkfcQEd1tdJDt6WGIgZAo_opkcifjax6quqbQd5FHo8JU2uEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت به زائران در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/454089" target="_blank">📅 21:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuR9Fn2W8c7pJ8d6wQu4mz_r9mr7MYn8fFG7kzBJ6ZzgY-jLt8IklM4Jayb2-uuPTeyA5DqblKixEiv01BxcI-FC4JjNTTDuMFQukHtSBxyYiIKUiYzz-U_2X6awwgZBb-TQ5oEQtGRbdo1WXCsqcnfqtqR4Rlc2BVbjbQSR-vLiOhVFZTXwPFX8L3OdSa8tuYXbCObMbLu90EjfLytDEt3DmYrMpYRHWlByhYd6sgZqa1pPLZcxkUu4uPFYI2ZQ1I0gq0Ca2s_25rPu6zn57xxPAKvFRPAuB8cQNNpnUFDUpvp7hsPRYdBxgmlNVPN-cdKojSA7zNsd_0w-veX5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
پشتیبانی مداوم و گره‌گشا از پروژه‌های شهری با «مسیر جدید تأمین کالا»/ شهرداری تهران چقدر مصالح از بورس کالا، خریده است؟/ افتتاح پیاپی پروژه‌ها، با وجود شرایط جنگی
محمدعلی‌نژاد معاون شهردار تهران:
🔺
برای نخستین بار، در دوره ششم مدیریت شهری، مصالح پروژه‌های شهری از بورس کالا خریداری شد و این شیوه تأمین مصالح، ادامه دارد.
🔺
شهرداری تهران تاکنون، ۳۱۵۰۰ میلیارد تومان انواع مصالح پرکاربرد پروژه‌های شهری را از بورس کالا خریداری و تأمین کرده است.
🔺
با وجود شرایط جنگی، در ۴ ماهه ابتدایی سال جاری، ۱۰ هزار میلیارد تومان انواع میلگرد، ورق، سیمان و قیر از بورس خریداری و برای پروژه‌های اولویت‌دار تأمین شد.
🔺
خرید از بورس، ضمن افزایش شفافیت و سرعت تأمین کالا، کشف قیمت منصفانه و کاهش ریسک معاملات را در پی دارد.
🔺
افتتاح پروژه‌های شهری، طی ماه‌های گذشته و در شرایط جنگی، افتخار مدیریت شهری است و به زودی، پروژه‌های متعدد و بزرگ مقیاس دیگری نیز به بهره‌برداری خواهد رسید.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/454088" target="_blank">📅 21:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD_6N8cL5LAmhI-4RoKEoqJToBRJiRP3yFvxNlfv8tMIyw-WtGhRKCngYke4VqThyc0JpewE0FbSJQTyCW4dpmStB_SmD41n7xChjxsMG9jWyjHA4_ovgq4FD5VDb7Ru3c8dnMQC9zFIHUst3rM64v1Fv3OhYeZQ5wkXt59Hcuxsb1H70Co1TJkeLO3g36mFu50PY6SQHku9F8y9NiQO2289qxmCKgZFYR1Cl6q30RLfWmgu9n25iur0kJolTzvOZELc_LwJTZuDpmaykFWa3AGdvpDa9iGncYck8xSStNk42UK5dpc8FKPh1txFxWaBPc2UJntRmO7d1SxwCc7zmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
در چهار ماه نخست سال جاری
بانک کشاورزی ۱۰ هزار میلیارد ریال تسهیلات برای توسعه تولید بذر گواهی‌شده پرداخت کرد
🔻
بانک کشاورزی از ابتدای سال ۱۴۰۵ تا پایان تیرماه با هدف تقویت زنجیره تأمین نهاده‌های اساسی کشاورزی و ارتقای کیفیت تولید محصولات زراعی در مجموع ۱۰۴۱۲ میلیارد ریال تسهیلات در اختیار فعالان حوزه تولید بذر گواهی‌شده قرار داد؛ رقمی که نسبت به مدت مشابه سال گذشته ۲۴ درصد افزایش یافته است.
🔻
استفاده از این بذور به‌عنوان یک سرمایه ژنتیکی، تأثیری تعیین‌کننده در بهبود عملکرد مزارع دارد. مقاومت بالا در برابر تنش‌های محیطی (مانند کم‌آبی و سرما)، مقابله با آفات و بیماری‌ها، ارتقای کیفیت و ارزش غذایی محصول، سهولت در برداشت مکانیزه و افزایش بازارپسندی، از مهم‌ترین دستاوردهای استفاده از نهاده‌های استاندارد است که در نهایت منجر به بهبود معیشت کشاورزان و ارتقای بهره‌وری ملی می‌شود.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/454087" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/454086" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک شهید در حملۀ تروریستی به یکی از مقرهای ارتش در مریوان
🔹
تیپ ۳۲۸ مریوان: در ساعت ۳ بامداد امروز، عوامل گروهک تروریستی پژاک با استفاده از ۲ فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای این تیپ در مرز حمله کردند.
🔹
در جریان این اقدام تروریستی، یک سرباز به نام ابوالفضل گودرزی به درجه رفیع شهادت نائل آمد و یک نیروی دیگر نیز مجروح شد که بلافاصله جهت مداوا به مراکز درمانی منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/454085" target="_blank">📅 21:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4KqdFWVHqB5eIMq0DFQiKJDh5JV6flVOdIkFdwIQD8iBBx-kwUzfPgMSLlxdadFI3GcZG1NnL262d3-hvl6_vC3gCq9p7gVBYzFY8fsZUHz7KDxrroPhG10TCCbV0ZRATPoI-HOLZEBpBz9TMciXz8KumigMJyrJy5EUeJ0Cs150SXZap1q3EJ9tRHXaJxwADYH3Bf_6m-0_AWeMB5PPFfANssoea2N-2V2igvPlT52Fwp9X7VbZtsNZR1BfodUbkfD6SG2W2CNgbc6jttuCSM1zkTnCCUnR4ZAi1av56YkW-5780Qtl0WZMVjL7kSxXe2X_R8lnzVP2lEUyiuUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: کشورهای عربی از راهکار نداشتن ترامپ مقابل ایران ناامید شده‌اند
🔹
نشریۀ آمریکایی وال‌استریت‌ژورنال: «کشورهای حاشیه خلیج فارس در گفت‌وگوهای پشت صحنه از فقدان یک استراتژی شفاف ازسوی دولت ترامپ مقابل ایران ابراز ناامیدی کرده‌اند.
🔹
کشورهای عربی خواستار تضمین‌های مداوم ترامپ مبنی بر حمایت نظامی آمریکا در صورت طولانی‌شدن این درگیری‌های متقابل شده‌اند».
🔹
روزنامه وال‌استریت‌ژورنال چند روز پیش از این گزارش داده بود که جنگ با ایران موجب شده ایالات‌متحده کاهش حضور در کویت را مورد بررسی قرار دهد؛ این درحالی‌ست که مقام‌های کویتی اعلام کرده‌اند که همچنان نیازمند حمایت آمریکا هستند.
🔹
این نشریه همچینین نوشته مقام‌های کویت مانند دیگر کشورهای خلیج فارس از این‌ که ترامپ جنگی را بدون مشورت آن‌ها آغاز کرد که آن‌ها را در تیررس قرار داد، ناراحت و آشفته هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/454084" target="_blank">📅 20:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HboBCXRErDSjKht6ofL93fr5VPcckY137hwzKAExzWHimrImvrXIa3FWD3SWLepIj8uarPxokeGNLH1bKxIywDzIj4T8Rzi04UuSijatk3u4J3gfoE8ADzoc2NVk1IG6gs1o0N2aXo7yHlVEFBqeSA7ph6eqeSbZRFzqBEZ0AWoQzS0NLbcIirnr0no0w-h8f8DX9gATNH8KtxGNSl2IBECcvUo633RP8ZtLqNB2ejFc8paXBLE0Wxc15T0Cay-lMMGZ3-vt0EhV-kSNq-q8LZYoOTf8FeA4-jPziJ9CwNmhx9HVkDhuJuw9XNPcRg9ZwT4qRe6NmE-WsnnYm1floQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برافراشته‌شدن پرچم ایران در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/454083" target="_blank">📅 20:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هر کشوری با آمریکا در حمله به ایران همکاری یا همدستی کند با دفاع مشروع ایران مواجه خواهد شد
🔹
در اختیار قراردادن پایگاه یا امکانات نظامی و لجستیک در اختیار طرف متجاوز، آن کشور را در ردیف متجاوزان قرار خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/454082" target="_blank">📅 20:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: همۀ دوستان و همسایگان باید بدانند که تبعات هرگونه حملۀ آمریکا به زیرساخت‌های ایران، دامن همه را خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/454081" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKgaRQbHR3tY2AEEtb9bZ5ij4WJu8AnjUD3nvgBMA7BAjpOKExJQn583_3AtUy6Vx4HX39Gua5Ay9kn7dfw2nWJWkNGvgPLR7dN1grrcRuaYaC0F8FBuAScfU4Qe2ISnJbD8FRVjZBBgEhkmRXnK0m7yd1QRu2X5NRN_hdNJhhLqS7waBI5q2HQtKsZkUkcWTWI1p5a2QAd8lJqQq5FPAEnfNlFUNEeCcAdnK_YA9tAc7lZOdY-3yJ2GLT4Hccfo1E0z0tPywrzJWLq-13yr0jysh1x7nkfmoTvejikNlVEzY3dPvpyE-vvTCaqSrJ5uVSG5i02oCA3f_eUqc9NSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: مذاکرات میان ایران و عمان در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/454080" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: مکالمات آقای عراقچی با مسئولان پاکستان و ترکیه هشدار و تهدید آمریکایی‌ها به پاسخ متقابل درصورت اقدام علیه ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/454079" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عراقچی: برای پاسخ به هر ماجراجویی آمریکا آماده‌ایم
🔹
وزیر خارجه در تماس تلفنی با فرمانده ارتش پاکستان و وزیر خارجۀ ترکیه: نسبت به هرگونه اقدام ماجراجویانه از سوی ارتش آمریکا هشدار می‌دهیم.
🔹
جمهوری اسلامی ایران برای صیانت از حاکمیت ملی، تمامیت ارضی و امنیت…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/454078" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایران به‌خاطر تهدیدها و فشارهای رسانه‌ای از مواضعش کوتاه نخواهد آمد. @Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/454076" target="_blank">📅 20:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: وضعیت تنگۀ هرمز به‌هیچ‌عنوان به وضعیت پیش‌از جنگ باز نخواهد گشت. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/454075" target="_blank">📅 20:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌‌
🔴
سخنگوی وزارت خارجه: گفت‌گوهای ایران و عمان دوجانبه است و به طرف دیگری مربوط نمی‌شود
🔹
موضوع گفت‌و‌گوی ایران و عمان برای رسیدن به سازوکاری که منافع ما را تامین کند چیز جدیدی نیست و از مدت‌هاست آغاز شده. @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/454074" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454073">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/454073" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/454072" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9tCGzlCdxeBDFHDWtV7UCEAxCzKN8aA-cah3r7sPGl21Y0b53QgV4welOeUGA6w2gVtaXGJ0CVlS8QxPi9u2HinoSOfJWWHFKCn8hviFnFxxco2D1KD3eOkSg-FZjQS6s7xYvNVm4WtFKiJaRK3AED9vV13cOs9Rtl9StLWoptrQ_JN7FjHAl9fbagA1p9IMgR6gEbVa142U-txv6vlb5C9iWrSLAXr-BG9uQa0trnIJNxOl5lYcwVolRNk9g6gFicrG0eXNtbGfalk8qvtDONG5KDn4bLcXdwD6fv_frpopF_doZRe6ZG33xPZdV5ENFvcHSyLHhmQGIT5w4qZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
موج بازگشت زائران حسینی از کربلای معلی در مرز مهران   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/454071" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAxjmDXxXTp_okIKIl5jJkq7wLgEMy6TcmDVzQQ1X8lTo9FZNzgljjmxEgKFDj6opfyeEf5yIxK4K6HCqXarGItD2K1_p8k1otUtMoVl9hXhveP-d4Cwq2vhLdYmArCHphsT5jQvYycXMtNzLOE7LQf5s5dbKI1Kv0EtQppMfpqM6jSREbZWOh1-tGzCERYnFo5DmnH5Nw76cnEpC-nrWbk-3AE2jHubF8MmxxiF2AkOfJpHg7zu5B9vHWIOeBramSQ-VrAtvTcLy6dCnL3Vthy47e6RaY0PfHTCURGa9Z9vPlkr9s6Qhy6EaNQ8icaInK3I89aQs3zFUVUyHYzkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قدردانی رهبر معظم انقلاب به خادمان اربعین در مرز شلمچه عراق ابلاغ شد
🔹
نماینده ولی‌فقیه در خوزستان با حضور در مرز شلمچه عراق و دیدار با موکب‌داران و مسئولان عراقی پیام قدردانی و تشکر رهبر معظم انقلاب اسلامی از مردم، خادمان و موکب‌داران عراق به‌پاس میزبانی کریمانه و خدمت خالصانه به زائران اربعین حسینی را ابلاغ و لوح تقدیر به آنان اهدا کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/454070" target="_blank">📅 19:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454069">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مرگبار در پاکستان
🔹
رسانه‌ها از وقوع انفجاری در شهر کَبَل در شمال‌غرب پاکستان خبر می‌دهند. در این حادثه دست‌کم ۷ نفر کشته و ۱۵ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454069" target="_blank">📅 19:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJb1mwi8RR8UQ296fnqinQgbS9Wm-4_DbGEQ3kKyg9qBho8J2SpHCRIZ7RxqNeSAranjXZhPSrcPFX8ras3RB_xwr8arPSVOV5o4yY80Jhss1_AsixxRC0uR57ugesXr9El1_OOsHSbh71UxYvWXtrgXY0oxl-FWTf_lXi6D7xnfS57eU5ukBuducf506zOpgmb7aKDea3Jj6cJZyjQkMwLcSR4P-J0B54sKO4rlJVd2d3Do0w_-ZLDcEoKHIDV-Tg3FVETNkWyPciJczJYSt-NSmvWkS6fYb7AGw3w5PjByzF8Fmpup96nQ2Nl7rBD76UY8Ln6QtlMeQ2Rh_0ylAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیموچی در اصفهان ماندنی شد
🔹
✔️
مهدی لیموچی، وینگر سپاهان قرارداد خود را با این باشگاه یک فصل دیگر تمدید کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454068" target="_blank">📅 19:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ هجوم مهاجران به اسپانیا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/454067" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با وجود افزایش حجم سفر زائران اربعین، فوتی‌های تصادفات نسبت به مدت مشابه سال گذشته ۴۰ درصد کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454066" target="_blank">📅 18:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQI-K3JJ_L7kMP-aFsfiTK940RVP0FPDFpXgYc8DAvZFhnje2_dEmIcvJKHSh0Pf6pGTs2JB_FnIoRl2dfZ6-C2POtQGyvII23kXh9gyKEDt2d79SMOmyVlMA5NIGfaLVuU-EgeKVbPFqCw84VNmxP8asMMU8suws4eGFb7T4VxqTpzkCoHs_WPgmOUqZzeEv-FYdF3FuitGHkS_tRCVEjohDpA4jfQfNhDY8IXzPuWvUzm0qFONBkj6Lren7oTZ9f7qzGciDF0Yuqh0_Plw5m3App8se9Pxt1Sy_VVS47FYxim_VyuAybKYTscWIyM3ofNicwhQ3QfQKcLZjCvI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdtwimWZbLXSdwPLfYSmp0GQMjaXnDVBAzAOrEw0_qKjcEer2alMzxcykb832bXXGzym48Qo2ilJLse4Rox9X3Kb03kon8gbIJ6i6Z2MfP6CwjLAG8HCxJGsghA_MZ_o2TeCSxAM6l-_kILUk2JU4Z6THogLsc7d3SUOap74tAa0OyhfpM3OpScqEP9lFeKNUCaR0mfZV2n5Wd9SqUlcCjmKjf-SAmfdHKI-vRFTev66MejcYVwgzAT4nB43Der1SxhxpVdEj60fphzIyWy54utUSZtrrltu7O9YlZ2TfThlwCoGikh4u-Wjd_ltZ-vc2e32d7EdlsV7Q98yzneBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th2_GW-rnasOq9Vk3ypG5-gwdf1MAYrXU3t4ktKYRdYhxw6W5PbwxVKn-Qq1ES6P44pg-bEt0XoARCZi_JES5Fo_2SHE5K_fdYrHoXzCfbw-p7POjQ9yOHygj_0VJ1AEGmq_7yZIkEmv6nSPp5p0F_DQHNYSefahMNybIlDQdieQfNBm_so7ttublObGs73M02iLwVAUJ2eDLOunpfXM23t5Gy4XEmC5Fj9KMwgQwBFpxaVLHFPzOyUjL_4cugXnxm0_hiGbyRDzx0zAFCaKiVue7cVXM_zxK3gA4bzC-CcxO2eUIh8Y7bT3a-3vOzbsbdnVOn_ZU0xMOGqrarQbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-mnZGY_Z1f-Dgc0jlGDqDGT8dkzYCE_jcegKkcDFzQkhS1kZzjKsQd3CuXZ554cy9IisRdILcEHA-omMjyDYFJbC-Z-KsSPNH57pF6KQa8_U_pTk7oropy6SdNvDY86KdFjh9ekV71jjygCVkdd66LZ93f3D9xC2CldW_xfLO7dOijsrK-CLlMFbaLOrXtM1iPKX1FEfimUJ7Q3Ub5Yp4qPuslu-F3lgNCOOpvV_eKc3Pad7qrY83-94trRZi7dmCzgbTkso1Y1lAMOVDpBHs1Mi_bdCj51kcPxRBbkx3RyqaN6wAYqQQw-qZ9wCT1hF_TVGcVazZIgTTau1deb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWJfo1eC4zaPRqczhR5zD4t_QDspmyP6YTqU1m1FAomC86qgoF65GLrXfknZTQPZQ2OBB2W35MSEUoIvCvYHrXR5QHDRrDEzWD6BDVNcQ6G_irGz73taKsuzrA043J_owvgrOBMEkv2sSHrNkhu42ebL0Tpd93DXy_yai-eiGAvIc6t5x4xod5tKFR9xwajhLYXtVqNb7k-v89DGMIeXabd0er0dQoMhDpAL7nVTg8zSUzu5RmtA8Lh8EqgZnU2JO5XsSvZj5nUs3chv8zc19Bb0FsbxWHHW8PGtLtyijq3DeXuc5wx8cI-ukEvaWlJtmMQQ2yLe5AlMY1SWGMHPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uz64cEFW_k7sSD4M34f9pQUgM64uu1-UEqKO2wAbXxNDtQ5Ela5ZwAhTQVvxbflhIKbFVZuALqKXeNegFQ3rX-2aGhb4MyADc3-3sMRDphVw1OlvQ9Njg1P-3rKMd0dwVlK5-CuIM1ddfDVWozkXJJV7PaNqfHacZvcistfz7tCI8al7zKRef8C-QEVwSwxVKp_FdilO4V0elkJnpu064QnQVebfDceNm44W0bYjHQAQQiYrkehc-iGbZrU7alRKX6Hkp6-i0hfsxX26CPCOZOyGMzfu_d5wltyiK8MXK2QQYl9l3Q71xfDsvm3E8xo_G79S8mBsyBfThCRyYv6TRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTjYtzZB_xsda4Umv066wbnYM1Q03RHnsuz1AvaBMCwJb9RgdpMhyL_U5YkkjNDuMAmSUxZho1vE8AYc7XfTegoDFB3Vfesnff6NWQ5MEDbW2V2Y8w4GddM4MPdMEuSCuy5K2SooKq41Avacn5JOUiM6eSgaLBXrGmFcJT-WWP_X9RW7sLdXXaZtOTM2hUpU6dwCm88yfI_Ew-9rlr-DWT_X_jU__-Tb25OpdQRD4K1fWNJjebGXl52a_WslPODVYO3KmxA4MyrqGt1NTZ9l3Vfs5z_lpTdkGql9X54Yhisn-xRh8xARKidGDOponGsaeeWXO6kWUDVnGdiv-EAR-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق سدة الهندیة
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454059" target="_blank">📅 18:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWLY9W3DT_RMi73VN83w17NEM_jV9dv4QTJcMVuDpx9NVZQhH16q57Q_xfta9nZtAVndvCGqSmhhemZAcb9SUlkCkIC2t95LDLEr_W3caZmGljkjFBqCRjsv2evEX6wcPf6hzDhETQth-b9R36EibXdoWeLAibsojMd8HrlZA1l6KlIImxlu1BqTzAYUv_IOXCPFhVL_IZB9DUaLRvuLec8O3jy8-9hKsf6KdpQen1M2PCPUPXSu7z4LyOO0nkWpAS4eOCMwMH0hIhO5jqGVYluGcSo2HvfRvGnchDUcjqYZ7hvDriwaTcXvGcZFUpjrmqPEq0tLd2nI3Mf6UfqYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج قرعه‌کشی ایران‌خودرو اعلام شد
🔹
نتایج چهاردهمین دورۀ قرعه‌کشی فروش محصولات ایران‌خودرو روی سامانۀ
esale.ikco.ir
منتشر شد.
چند نفر متقاضی خرید خودرو بودند؟
🔹
ثبت‌نام‌کنندگان: ۸۶۱ هزار و ۲۸۵ نفر
🔹
ظرفیت فروش خودرو: ۵۳ هزار و ۹۰۰ دستگاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454058" target="_blank">📅 18:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e92d2385.mp4?token=bZSLh-Pq9ir_Gc1_u_5SIXqs_cAkLBLaENuZ2LrLfay6mTvYCd-K4y_mJXyXaXLM3Pi1iMQPESHoqcIiWczOxyS5lSEV0oDfqwen0dlBd020yaW-86giUUa2kmCjZPYQufgdlXEmBAeBdgPLKhBiwqqsLbuUpaB8_Q1G_7ozJuBfmTQHTsVQDXvHdOUFHu6IYsNda10EGqEBfnjE7gAilK7jLhNjBiF-S4PLahdHGBTLI_-YFjrC-aVikWbVGOY49bt8ocKGZmR9H2Qr505zVvVN6lRmeSY2eOhQAv0QrA6NrUAKGsMBLxsdKwuFQKeSMJIvyIDj-bvhXlgiRCGPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e92d2385.mp4?token=bZSLh-Pq9ir_Gc1_u_5SIXqs_cAkLBLaENuZ2LrLfay6mTvYCd-K4y_mJXyXaXLM3Pi1iMQPESHoqcIiWczOxyS5lSEV0oDfqwen0dlBd020yaW-86giUUa2kmCjZPYQufgdlXEmBAeBdgPLKhBiwqqsLbuUpaB8_Q1G_7ozJuBfmTQHTsVQDXvHdOUFHu6IYsNda10EGqEBfnjE7gAilK7jLhNjBiF-S4PLahdHGBTLI_-YFjrC-aVikWbVGOY49bt8ocKGZmR9H2Qr505zVvVN6lRmeSY2eOhQAv0QrA6NrUAKGsMBLxsdKwuFQKeSMJIvyIDj-bvhXlgiRCGPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جبیر گرفتار به آغوش حیات‌وحش بوروئیه بازگشت
🔹
یک جبیر نابالغ که در یک استخر کشاورزی گرفتار شده بود، با همکاری مردم و حضور تیم‌ محیط‌زیست به آغوش طبیعت بازگشت.
🔸
جبیر از آهوهای بومی ایران و شبه‌قاره هند است و عمده‌ترین تفاوتش با آهو شاخ‌های نازک و بلند آن است؛ جبیرها به‌شدت انسان‌گریز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454057" target="_blank">📅 17:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf9616077.mp4?token=surljXo2APg9yMRXtnECLxRYugaYwLaO_PUza5kSBHUMy9BFRK35HwQH46QdTotX14YthgWRAoG-Au1ah_f72aHjrj-0b8PbxCKpWrgUyz9HBmmpn2HuOB47dUGEfim5dboOT5IL5E8vLbOB0VR5d56xoKUcol9uT7Ksn8gTG_MYIAv7PhdX44e6XgAioeskCiM-mXvCOaFfWamPqgZyp4QcdG27fuMgpykrBF-gG-_Eb9j-OgNJoMX4PJnay8ScmenzHoJiYPOosVmcEPKrvXumjW0WsunguCifuQI7c01ZCO50HrK0COZDB5Ltk4Viwx2MWBoxbP-b1_UxGRcK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf9616077.mp4?token=surljXo2APg9yMRXtnECLxRYugaYwLaO_PUza5kSBHUMy9BFRK35HwQH46QdTotX14YthgWRAoG-Au1ah_f72aHjrj-0b8PbxCKpWrgUyz9HBmmpn2HuOB47dUGEfim5dboOT5IL5E8vLbOB0VR5d56xoKUcol9uT7Ksn8gTG_MYIAv7PhdX44e6XgAioeskCiM-mXvCOaFfWamPqgZyp4QcdG27fuMgpykrBF-gG-_Eb9j-OgNJoMX4PJnay8ScmenzHoJiYPOosVmcEPKrvXumjW0WsunguCifuQI7c01ZCO50HrK0COZDB5Ltk4Viwx2MWBoxbP-b1_UxGRcK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳.۲ میلیون زائر از مرزهای کشور خارج شدند
🔹
براساس اعلام رئیس ستاد مرکزی اربعین، تردد زائران از مرزهای کشور همچنان ادامه دارد و تاکنون بیش از نیمی از زائران، سفر خود را به پایان رسانده‌اند.  آخرین آمار تردد زائران اربعین:
🔸
خروج از کشور: ۳ میلیون و ۲۰۰ هزار…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454056" target="_blank">📅 17:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yun261Z1HIe8cAM74EhurmmlSFmWShhtE20IoSCm-nJHRWyoi2VaQg-MFbNeDEv67mKhfSsxrH5xXX5GSHnk7TN9DmKtOJHH5SERkP9NGobm7nzX65NttKFknNp3tOwa85jxaotuQunr2_-_a-N48Z6CSwrKX4vRZ6cGVK5gLrqkXjhFVololFVuZ3ZZ0WX_KtzaaqzyARHkHCPuNHs5K8kqDktm7kYPoVBiEk-gFsmz5hdBldwUGrzHIzEJ-1I1jO9Z2iB3vQXqd_g_301uC0hj9eailqM33UBcnrDryubXUsIcaa_ROcmin4EMLeW4zQLIrKd8ZwxJTsWPHyDWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدایی مرتضی از پرسپولیس
🔹
با اعلام باشگاه پرسپولیس، مرتضی پورعلی‌گنجی از جمع سرخپوشان جدا شد. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454055" target="_blank">📅 17:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NngOr-Meb0Lw7UHN94N2Y1XUH2Q_X1YvkArz8HEZ3YsYnEpNvgnsz5_wTQhBgG1Vo8g7i8K0isWITyEziqZGxIIzFARVMl3DihN9tb8MPH39hVoL7iOGukM6P1mKbYM2mQLmlWPFuKaqv9KF4ya0tEVUNJzBfeedA8jH1VZkzIcf5Eoufh7-JLoJioejEK4EKiNGZPnA0q2LFfeMEpPxzj8rMmxpkqQKhvFWPLqzn1Z50csPhyezTDvYFEJM7WO7lQCPN_T9Mp9TqlGQk4LPBazrgebMM7Efy8Eip18s2dxQvyiEfWz7h-HfVoO7V5pXfKMBRSECJA7NU0NTKMoA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نمایشنامۀ زنده‌یاد اکبر عبدی به پردۀ آخر رسید  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454054" target="_blank">📅 17:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597894cdae.mp4?token=WMUCxpJYVQfFARnCJsL4P4jKKvTVkFdVwLE-qXyAKsOyE_ndm1aMO6JUDjX4_X4K3mRSWxRxxrS8bbcRcbVG3MxVhOVuWmN3SKEBuq56rvrj2y2rK9bnf8LM4j0cOeFlIo01Fq23WSd3y9OQ6OIMlWhrt6pGPs3tlaup6vd2_1j18xQdzaYV659MiLcpsirz4IGGKU9IzNfw7zKK7BdxM3Thw-5mAsX_qpCPKyJgUuah1j9GSQ_zDUz_0ey88XJcNr6X5-SYG3WbMNKui5GRdbFmMykEq7QJTuuf7rwNZzfXAQ4pvEw17kB0y7rElOtvvIiY9K6kvBu-D3ayP_L2RTa9nWHpUqm7JI-Su1qtfRCQ3OiVtekyD0wSCxUbWqm08BrBMp_i1yPP-10ueblSkA0kBzXEY3AyB-G196pbjFyWUgEM9hCcD-K5_lnNHJPZHCg1DNCr-m_KUf9xOtPO3HU4sFmOd6anffuTBii0Y9D22C8P1xxXDVfnBSxHbXsXdAcykuYmELLrrKQeVMqrZ-tGublMElcq40BFqflfz8TjrlsIQIfTm2w6LcI9JJVDQruhQujxvpRy3GXp1EFbuD5_autBHvxrl5b3fp61AJ6I9efXNU2EbJVV19NWOPHgyG1t_WTr-5HQvnqUly-feK_pJsMOJL6-lWUS-_xt0HU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597894cdae.mp4?token=WMUCxpJYVQfFARnCJsL4P4jKKvTVkFdVwLE-qXyAKsOyE_ndm1aMO6JUDjX4_X4K3mRSWxRxxrS8bbcRcbVG3MxVhOVuWmN3SKEBuq56rvrj2y2rK9bnf8LM4j0cOeFlIo01Fq23WSd3y9OQ6OIMlWhrt6pGPs3tlaup6vd2_1j18xQdzaYV659MiLcpsirz4IGGKU9IzNfw7zKK7BdxM3Thw-5mAsX_qpCPKyJgUuah1j9GSQ_zDUz_0ey88XJcNr6X5-SYG3WbMNKui5GRdbFmMykEq7QJTuuf7rwNZzfXAQ4pvEw17kB0y7rElOtvvIiY9K6kvBu-D3ayP_L2RTa9nWHpUqm7JI-Su1qtfRCQ3OiVtekyD0wSCxUbWqm08BrBMp_i1yPP-10ueblSkA0kBzXEY3AyB-G196pbjFyWUgEM9hCcD-K5_lnNHJPZHCg1DNCr-m_KUf9xOtPO3HU4sFmOd6anffuTBii0Y9D22C8P1xxXDVfnBSxHbXsXdAcykuYmELLrrKQeVMqrZ-tGublMElcq40BFqflfz8TjrlsIQIfTm2w6LcI9JJVDQruhQujxvpRy3GXp1EFbuD5_autBHvxrl5b3fp61AJ6I9efXNU2EbJVV19NWOPHgyG1t_WTr-5HQvnqUly-feK_pJsMOJL6-lWUS-_xt0HU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454053" target="_blank">📅 17:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادارات استان بوشهر چهارشنبه تعطیل شد
🔹
استانداری بوشهر: با هدف مدیریت بهینۀ مصرف انرژی و برای تسهیل در تردد زائرین اربعین، ادارات استان در روز چهارشنبه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454052" target="_blank">📅 17:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtFFDmw6kwTjkooxm7HXhC62qR0KVB7n8FbnkAMp8qav1fKpCou0uCP3-hn8FiV_QSfE52eBSm4WeOyyloFTG4wjgMZMGtPdhXwbEXcLQAawFb3S-xwGIrWUl_FtxffKFUEgqw1KJcbvtDdumJ4MIKFj4UFUTmfDraU_fcmPVgTCIuwiRwLM3GKrRQNfpZl57ahkFo_LKcfCJeuYNv34iXRhnRA9BRbB81yIa5AdQWBJX4tC7r2TqA7Z9yy6Dg4NERomPJr6URu4q3FJn6NqUU7yKt_eY42uT75fkxuldL1PdYlmRbjNmAX8nKX8fj09qJh6vmRUrw25jpXGW3aMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هیوا» پنهانی از طبیعت زنده‌گیری و به مرکز تکثیر در اسارت منتقل شد
🔹
منابع خبری به فارس اعلام کرده‌اند که به‌تازگی معلوم شده یوزپلنگ نر جوانی به نام «هیوا» اواخر سال گذشته از طبیعت زنده‌گیری و در اوج فصل تولیدمثل یوزها، به سایت تکثیر در اسارت منتقل شده و به…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454051" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOu-5NnIMpzDDthzTVPjPF8Ni4mK4HbxVicYieVYejgg-eQz5qvO_QB1jf-x6FprUbEHHGUt30bb58IKQXf6bDPyIPz-lNc4pj52opKKgkB2n1-tNFnB_tIvniialNofNCY69_90yEP1nr4fKMpJeuMlTKsOkPnoJxFC9ClIR-moB5xHQnMy5JHPI5citmZtKdSCPo5lXHPkVMcEmn_HU7B2rVTgy83QyN6dCY8HBZF6cVnFQYZkX2gLYu-clVPpeMqpzy7Uvk0Dj2YA0AcBzpFLt-PeI5UZjL5-zqNdvlSeoYjFuSp8dwlgJkX9hnghR-JDVqg3JLgD_RZpapR8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454050" target="_blank">📅 17:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfYi5N8oo0GopqJQ8ZDrydOq-_vQho_fB97PMQb5uUqk93arAR5PeelMB0QARR6YPfqb6905p_uib3McdhZmwh86wCpdGdlPeSLkKzOgavyNgpwpECw2IV3mxOTz1K_U-dioUJ-ZqbflTb7fCWi2A8EqC5kk02--Ma1n8lk9TzcaVs3B72m3403wosneg47lnrYouVMldgtKPW90MGm15444OKLLY2ouo2t5ftJE-39-DfknrLMrr5ALrY7Ca34LDwEgV6ti_O07TRcEhXLPLvijPBYIAN9J42qanC0JqPNVTorvrcmAeuWTN_jvrCApWQxOSLcQJ7-FtIx2T9BYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: توطئه خلع سلاح حماس با شکست راهبردی مواجه می شود
🔹
سپاه پاسداران انقلاب اسلامی در بیانیه گرامیداشت دومین سالگرد شهادت اسماعیل هنیه: توطئه خلع سلاح حماس راه به جایی نخواهد برد و از هم اکنون شکست خورده است. ما به جهانیان نوید می‌دهیم که سرافرازی مقاومت ضدصهیونیستی خلل ناپذیر و به فضل الهی پیروزی نهایی فلسطین در برابر اشغالگران، نزدیک‌تر از آن چیزی است که دشمنان تصور می‌کنند.
🔹
ترور شهید اسماعیل هنیه در تهران- در حالی که  مهمان رسمی مراسم تحلیف رئیس جمهور اسلامی ایران بود- جنایتی عظیم و نقض فاحش اصول و هنجارهای حقوق بین‌الملل، حاکمیت ملی و تمامیت سرزمینی جمهوری ایران اسلامی بود.
🔹
با گذشت دو سال از جنایت رژیم صهیونیستی در ترور شیخ اسماعیل هنیه، و تداوم نسل کشی و افزایش جنایت های قرون وسطایی صهیونیست‌ها در غزه و گسترش جنگ و جنایت به جنوب لبنان و سپس آغاز جنگ های تحمیلی دوم و سوم با همراهی رئیس جمهور پلید و اهریمن صفت آمریکا و ارتش تروریستی این کشور علیه جمهوری اسلامی ایران  امروز بیش از هر زمانی ماهیت تروریستی و جنایتکارانه این رژیم بر همگان آشکار شده است.
🔹
استمرار حمایت‌ همه‌جانبه تسلیحاتی و سیاسی آمریکا و برخی دیگر از کشورهای غربی و نیز همنوایی و همدستی دولت‌های مرتجع منطقه‌ای از این رژیم، آنها را تبدیل به  شرکای جنایات ارتکابی نموده و مسئولیت بین‌المللی آنها به‌خاطر نسل‌کشی و جنایات جنگی رژیم صهیونیستی را یادآوری و مورد تاکید قرار می دهد.
🔹
راه شهید هنیه، راه عزت، کرامت و آزادگی است و این راه تا تحقق کامل آرمان‌های فلسطین و نابودی غاصبان قدس شریف، تداوم خواهد یافت. ما به جهانیان نوید می‌دهیم که سرافرازی مقاومت ضدصهیونیستی خلل ناپذیر و به فضل الهی پیروزی نهایی فلسطین در برابر اشغالگران، نزدیک‌تر از آن چیزی است که دشمنان تصور می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454049" target="_blank">📅 17:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmxoWhrHaY9ryg4Awwbb1tk-2h-jmsIKx7XMRM1c00znsJf_tTQPB4lZxUYTakqOhX7yboOzmqHwBkuHyjlAefMNahAw6ShNYtf_lF52svjdTtIXnEi5AThinvI0jivBhQd3JUk335bSNLkMkrEDetB8-tU1ao9UnhwJNIVnqU21J-H474MuwBnY8WqqS8TFFi_ksrlBfr0INNYUaeWH6Q_7mPVK0JNDY6Gi20qh8W-BSeH3j6RbO4vc4vw3xPi4qh6vBb_Iox8BVFd0A9h7qfnXEfpOkAlNFGl8CEKy4vBZMp1bYGAx69O3l5obliT_FOXnnrlmOZaUGHOu6owbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی علی کریمی از عموی جدید سلطنت‌طلبان
🔹
علی کریمی فوتبالیستی که روزگاری شهرتی میان مردم ایران داشت اما با قرار گرفتن در جرگۀ ضدانقلاب و سپس اعلام حمایت از سلطنت طلبان نشان داد که در حوزه سیاسی به چه میزان دچار انحراف فکری و سقوط شخصیتی شده است.
🔹
او که به انتشار پست‌های هیستریک، عصبی و نفرت‌پراکن شهرت دارد، این‌بار در یکی از پست‌های خود از «یزید» به‌عنوان «عموی» خود یاد کرده است.
🔹
سلطنت‌طلبان پیش‌تر از افرادی مانند لیندسی گراهام، ترامپ و نتانیاهو به‌عنوان «عمو» یاد می‌کردند؛ اما حالا کارشان به جایی رسیده که با یزید هم احساس خویشاوندی نزدیک می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454048" target="_blank">📅 16:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سردار آزمون و محسن یگانه در فهرست توقیف اموال
🔹
دادستان گلستان: اموال ثبتی ۱۶ نفر از مزدوران همکار دشمن تروریست آمریکایی-صهیونی با کمک دستگاه‌های اطلاعاتی، امنیتی، اداره کل ثبت اسناد و املاک استان، راهور، بورس و شورای هماهنگی بانک‌ها، همچنین سامانهٔ سهام قوه‌قضاییه…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454047" target="_blank">📅 16:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU4JBIV6PubY0mPbgZTS1K6RKTTEg0i9A6T9qdUDEM-gtS_tVL2PEwCAcsnXAQNpcxNxIOrsAZ1RTUx11slKyKyzeDE0F9FxcbMhw7MyjWh_ZpjRyxB9-7jg4elApBLqBZcZC399HOerWAJyg9AaXGWuKkXa2WH43mafopFoncLG-NH1aj_B-fl__1NOVc52FG8hQF2UezKf6Eu37B8b7mnB12TY1hi-QZCPo2031UCz2U1JFvg5g1dJoZcEjCUDrDB8TQKdyvHycPX8-Z4Cy10Lnp8TklRPMNipts01V90XHYykFcdUTXrzDlWk03fLQSaYrBXWlDbrEnR6tm1QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: زائران برای کاهش ازدحام بازگشت، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454046" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7eOwlEtyClPD7T7Akir0bjblwebx59WMJBfkji9f5-V1cJqtoxpzzazQLJD7eA6TPZZSxFW9tSXjqV1JeFBZGqXTrdVCukaYWdPYAdtpNbzRR2qwkAoT378OajyRa9FMycRlh_m9tw_dFrHboCBW_i_LcTxHdNB0WitG86SDVzFzs0Ln9PD14-mMTskf_eyUT8zRvhpPv9DOMhHDYCgTdstR8l5zzcvFrNMhWdzKdOSUKUnYjcc8KGj_zKz0h8gw7NBTLaaiGwU5XT8y-bsYlGjnp8zvj5zoRvFCo8OsPVV4Coym_0cfdQ1Eq_MKbNgik70UTA4F1AXa_AKa_Kb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_FPRs6CJoIQDL2fh3PuDG2s-2MDP3A8CV43GTD5QRl_14c1kHVmb7gMjoVHhMf6sTkYLFkulm0kww5yMbPAeWM_D58h2T-YMOot2ZV_6v9njdXr9tX8yZyOR7a8s7FW6P883YhUU5DtLVQWq3h2M_nbSJZaFUUplI0ECviq3BVIMMKPIAC9gHYjENN_0nNyOGvIJ7TmAw12kNpyXemPkGCMTGoKJ1lhPeKPDJEIt1Ut5KjxBzfo_Icm82A5L1CkIczsumf9HQbBron2bS5hvBLC-kiguQJQ8Re4GW_gm1wbf3E-JqR5AqXDhNg1Cz-_N_MT6eN8iIItkVmvpaXATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fz87EGJkWiXLPs4m9YwltMKuxUE6IolL6XlqaTQM8vl5od8juJZ1o4oIexeykemX_cBtXtFHRxy0oST9dR9h09n22oIgwKocSBPWrflL3ASPefXL05P10u3ratL0MrxCajEPXUExGTq54EPF2gL7aOnh6hYKrl64wGA0o54vOu5xciHmrJQ0-cS5ay_nCictdXF3E0iTpd6c-M8B9VTeqzyhZGW-H6N9OqZK0empDkNne67hLRT-rYbFvZetVwssiGzPTytmSYtd3_7qCNqJxYM1_Tc9agc42oCleGtjn_wJUN0iXmis4K5CLOy4nZWxC0sR8Gmg2u83YVvq80lnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELhjga4Gn1jSZ9ZNc1tQ97USK4vpGRC3pIsuYH_Oww9o8w0GwOQQSHJFfbSXpbbP_HkyIYTUkrfBxfiNOzP5OPexRWPgN-ehaaAXQXACkE8wUGP1ob5h23E7vG_WTj4YiIi1W03qhDEWAIbwdf3v3wrt2jEyoL0mCDTS5qXjjpL9O8jOQSJLqMCmPxNSD-_Q307cXQ-vkzDMiCK_p6ca96_C9xqZ_Yp0Pl-uJADvxeYH-F3KpFve9B3ybqfmzW4w9M-eYj_-CxvYV6tp7i2zBVvbpGOrLumkws7_6JhszJBm5RXoP8W07R69M3TM3JswtLTKXr5AqhbpcTkm3nfXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiZgbvMNMR8OEUbR-CEBPPLXTpOJsxvY-kTT_vn6gQfoyKg0JpQ4BvFOicE8sFBv1Cxa5yiHKiP0WduRS3Io1fMSzeAuFyxEHc-8N0SXiB3OwzYagYh8M83KkANSgL7xEAEWepmFqg_kYmFcV-DLxaiDx3kY7ACdk-_tlSADCMz54UZX5xLJ4hDGxlun_SPJ_Al4OHZh8abNE0k-N7sxvh0-ZtvfLvaT3nvQcCtbhvMtrNo4Bsb_hChYtwnPUO9O-RgZix9DZy6AXKHXqzs5-IEGd4YzCCa_6hqhIbnrkF955oBcxJYjnuSUv51YfDSsvreFoP71ABpfnCFArrY82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOBba_Yf_kz9vVVgwpeTXAHr0ClCZ08Uq30wVi-hqrlqYRRGZqtAuU4MDn2baazTo6xTKUIPLIuUUsKEWbQLxRNR_I_mo31ErEhITUeZ88_xhPPGj1CvrhSLm04SfYD3FHf7td5HNpeG5E6a9xHWJ7cxplY1IemKBYLWdksqUuzjBFfGnzU6v4FMqsZfiiOrEH0D4J13eoeU4_HPIu02ccIgGpMcD80MytDq2pgVRqjFhaNbkDG_pIgnFMQIbfJ739uhyrKOHxrsTlYWLAEbjO6orcU8GHgF7v0hPIKB1EfFNPDZ9EkyeJqxB1aBrOu-kOFqU4rvpE1TFbfg0vP1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-2UC73fUAAhvHcfXsGgUdDgCBBR1aDx5EPQhrHq_mUqm3Jy6OC4NlDJ8nMgeqGXjJJeNT-fXYgmmrFtosy4gqV6T3dZvNMUwyuonEFEAU0XPZOzo3h-HCIddpkMJxw6aGBmajxGjL0EsysrVO4K33vtkJGlX9aABN1VfY2bp6l6gcEdbCxf3IqzuFqMLI4RyXPgolL2BTrITxT-F7jBVGY6w-wy3nwJ9UE5sVgbwpDL9mbnBbhtDwpR7sF7dMHrza5T1h34i259Ej8TBDP-YwAtNK4Ipx6QFdPe4D4BIJGhuR2kPCfP5QnJk1ZiCpp3kk7YsgFXTnRj-aMdqgNSuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری زائران اربعین در بین‌الحرمین
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454039" target="_blank">📅 16:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEVQrU-tr9vUVM-3Ksx-__3GS9co8pe0fdUvdLsYgqRc-lgf6gZLPN2lzsWGDNpzMqZPlPI3yQmJth5gIA5RR-XxaAkX2m_5Z8Ff6QSJGVoawvblMMNMNe9p0v6HYV_BxV505NoQnPRSbjkCjgjFFEjxSqyHahneh6W41BbMlS6ZgpuPr5DaG30XGU5oJ8ymlwr78brOdrQuk0Mk_9GQOr7GCrcIR_hh5VaPGcl5n-EGnqvWXy-vJ22iB9c6W1pqFqtMjBcjnkxRYjbOqZEwxqixK67qiZeBmssQYV1WkPEzqhbYSIHpF1y8WMiWDaeD3hdsiHdKYRk6sa56IGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح اینفانتینو و ترامپ به گِل نشست
🔹
بعد از مخالفت شدید یوفا، کونکاکاف و AFC با طرح فروش جام جهانی به بخش خصوصی، رئیس فیفا از توقف این طرح پیشنهادی خبر داد.
🔹
طرح جدید رئیس فیفا می‌خواست حقوق تجاری مسابقات مهم فیفا مثل جام جهانی را به ارزش ٢٠ میلیارد دلار…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454038" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح کاپوتاژ اتوبوس‌ها در مرز خسروی این‌گونه اجرا می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454037" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گرما اداره‌های خوزستان را دورکار کرد
🔹
در پی تداوم گرمای شدید استانداری خوزستان ساعت کاری ادارات استان را در روز دوشنبه کاهش داد و فعالیت ادارات در روز چهارشنبه را به‌صورت دورکاری اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454036" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv68tC0uNh4ZplBOZf5lWzR7gVOzMSFN8WdlBOSmQY3KvrVYbUOZWeBCgZmLNFgw73k030sYknRfmV1zP398jcnMiqTsln_l8MCBPLAWWm_XF31N16xcILITXeNFcgf4FukoWu5HMWVMlv5uy7WhKo2LuVfa4kQBLSEfwjJS0J995VexOZVaxfLHn5Fd_-gE7xDnVeQrS7JdGI0FNTWIM1HMSW6HFapVex0SEbLceEatsx1iRr-Cl5SAwBp4trHvFxuD2BG8yfWbCepJrEoXdEn6xyn8SyMqAKOwY7Nyl-0WF6xxrMWG8sPWsZ6rxRmkAO9_u8eyqaGUvuBJCi1Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
مروری بر عقب‌نشینی‌های ترامپ از ابتدای امسال
@Fars_plus</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454035" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNuJqXF0o4yAZJHvmHNlClEeOqMaDC3-UWf0QgOq43D89imJovEuU-GpGl7Dm5n7wh2J0haP_ghNgWmaxJXIHEDSXgsnnoR8yBJ2O5t0yXuFuaL7pVeddHicH4mONNepyOGxmBVQvsmnyOXYxqt0GxBN-xigEoNOs--6KRrMFWizQVjPncz91esyJqSKOgxz9SOpWTToTX-tXMr790a_yEX-q_h62wgeyOkcDNdVyq5bSlPNVPCIecc7FLlyYzevzq0CqPD9aRPXZtEJ9Lmk4DedbmzRHgCYfUC5u-Fb0mLWQoQUMdJrm8xM6kLrnO2TZCaRxoB2gki7lBDy5TP8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی اسکورت‌شدۀ آمریکا زمین‌گیر شد
🔹
منچ‌اوسینت، اکانت رهیابی‌های ماهواره‌ای، می‌گوید یک کشتی حامل گاز قطر در مسیر جنوبی تنگۀ هرمز لنگر انداخته و متوقف شده است.
🔹
بامداد دیروز شنبه دو نفتکش در مسیر جنوبی تنگه هرمز در آب‌های عمان، یکی در ۱۱ مایلی دریایی شمال‌شرق لیما و دیگری در ۲۱ مایلی شمال‌شرق خساب هدف قرار گرفتند.
🔹
یک منبع آگاه امروز به فارس گفت، «تنگه هرمز همچنان بسته است» و شناورهایی که از مسیرهای ناامن عبور کنند، «حتما دچار حادثه خواهند شد.»
🔹
منچ‌اوسینت می‌گوید که این کشتی در جمعه شب ۳۱ جولای تحت اسکورت آمریکا بوده و هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454034" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454033" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454032" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roIOSzudX2nQrxQdPHSOlaw9dHUkKdNpodvsYLcGO2KKCvONqrLBJXfZJNXTt9JLTtZnZUw5yEKoWbVUIH8-PUFahw3uaaM4rOgt0DdV0yXBnc4z6y_khBrx6oJGH0Fnpy_9Dr8lWtmTVlNWB4qjOi7lus5y5HM_61GJCEMtIsgXRrN-waV_EY_VZ-wpMzxC8wuuu7uvTgbHmb2LbZ9n2JS_5on-CzSSXhBsfoKbcWJ2YkNWO3EwzCbIvmPK-Zp9LpUSBKmeF6v0FFJ75KbZBcpDOJqwPkfQELuXPExT_FlNywujIx3A7_jZNWe6WNI_SBvD6xmMJme0PmgX0NCgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه خرید سنگین،با اقساط سبک!
✨
فرش دلخواهت رو با
اقساط تا 2 سال
بخر!
❌
بدون ضامن
⚠️
بدون بهره
با ارسال رایگان به سراسر کشور
🚚
🛑
فرصت محدود
🛑
4شعبه فعال:
📍
شيراز،خیابان عفيف آباد
📍
شيراز، پل كشن
📍
شيراز، ابتدای دوكوهك
📍
بوشهر،باغ زهرا
براى ديدن مدلها و اطلاع از جزئيات بيشتر همچنین مشاوره رایگان، يه سربه سایتمون بزن
👇🏼
https://jryn.me/bWa2AE</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454031" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/454030" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن آژیرهای خطر در اردن خبر دادند
📝
منابع اردنی مدعی شدند که صداها مربوط یک «هشدار آزمایشی» بوده که به موبایل اردنی‌ها ارسال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454025" target="_blank">📅 15:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454023">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر اتفاقی بیفتد خودم را به اینجا می‌رسانم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454023" target="_blank">📅 15:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454022">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
۵ نظامی ارتش لبنان در حملهٔ رژیم صهیونیستی مجروح شدند
🔹
فرماندهی ارتش لبنان از مجروحیت ۵ نظامی در شهرک کفرا در بنت‌جبیل بر اثر حملهٔ خصمانهٔ ارتش اسرائیل خبر داد. این حمله زمانی رخ داد که یک خودروی ارتش لبنان در حال همراهی اهالی شهرک بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454022" target="_blank">📅 15:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454021">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: قانون سقف بودجه موفق نبود، فیرپلی مالی جایگزین می‌شود
🎙
رئیس فدراسیون فوتبال:
رسانه‌ها باید بدانند که بحث فیرپلی مالی امسال که توسط سازمان لیگ فوتبال ابلاغ شده، به لیگ برتر منتقل خواهد شد و انشالله امروز یا فردا به لیگ یک نیز ابلاغ خواهد شد. واقعیت این است که فیرپلی مالی در واقع جایگزین ثبت بودجه‌ای است که قبلاً ابلاغ شده بود و نتایج موفقیت‌آمیزی را به همراه نداشت.
@Sportfars</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454021" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454020">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت عاشقان امام حسین(ع) از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454020" target="_blank">📅 14:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454019">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی کشتی در اندونزی با ۵ کشته و ۴۱ مفقود
🔹
در پی آتش‌سوزی یک کشتی مسافربری در آب‌های اندونزی، دست‌کم ۵ نفر جان باختند و ۴۱ نفر مفقود شدند.
🔹
طبق اعلام سازمان ملی جست‌وجو و نجات اندونزی، علت آتش‌سوزی هنوز مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454019" target="_blank">📅 14:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454018">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZMNx6lPKDaFhcd2_5yCA9PbKPQ2jA69yc1GBU1ycVg2h0Gn5QN1L-PWXU2fj3vKpAbEEMjzm1BEeVT0zfQXY30kzd9y0ZBEf9O1GXiq_4YQ2-tjkDZPeMoDsRX5rgwo5-8QHP4rgVSCI04rxNoNyWeq3lamLE-qnO7Yy96lcHnAkYWOYc5zFayXympvvL6XHd_Gt23lA3kXImgxkj2EQ8hHoW9fW_RHAjGr07mo6pKqqD3AhjGdM5ficj87juC423C2Mh1oFcx3UkNV759AVFVp4zoEoZv96pikNMGGLhoq_9M6_0RQ_llBopa9fPBUxYsVnB7tZ1JKBmd4hAwRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: زائران برای کاهش ازدحام بازگشت، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454018" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcIJ8E_LXqIM8G7sgy-bjhEYFM6h7zVFVejLM6wy-x-Zv8zMlNKVJ6ueuPQRfPhGj0PuiXDB2laouVmSKSNaComPdoARcovU27HJlc4hLkkqLUPmjk62WiC7Aic06EU_8Lwdlq4yQb3kHqz052Ki7vWTBPALvvcAGLIWp6nWUPCFAZiK0NU_o5eH5T7a1UZp5N4wS81TVV1hy64WNnnon6RyUWWvsTZmOwXyjbL4S_1wUzaoH2eiFVavt9LdAIq082hbcfWl254PbwnNwwZ-MWq7NTb5PWbc1riHYlKLw4IK_9Xz3h-y1IJeZUxM6t1v7vDIklKBgP9c1o1hxUeD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دلیل نوسانات و تغییرات در اخلاق و اظهارات رئیس‌جمهور آمریکا، رسانه‌های شهرک‌نشینان صهیونیست او را به سخره گرفتند و تصویری را منتشر کردند که «پیش‌بینی وضعیت روحی ترامپ در روزهای آینده» را نشان می‌دهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454014" target="_blank">📅 14:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا،…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454013" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoNWYDGDolwm7cTCsi36IKevyLwL3sqnXvpjiOh10g06VGnheSSC5DxOqzbf8M-JH281_LL3e1nzl9W1cabZOUCKZ-NaO-5iJNcJ0V3TXimdHVELyonc4UwG34oRhyW10DpZGPi8vvdTUol2qviPYQzne0uW3ztO1R09kH-lNjqlgarHcGLbblbE37oY0svAg976jKLKy9e0f9FXZZjVn-TLihNLZ-Y6T5HL3yVIs2USjmcLPtefPT4YQvMYvLSoFX9xhckaQFUDmXY5IDjB24ZIDWS38wy0IcmVeLq24OolG7k9wYeDsiw9aE6ddFZdjzxMzlI2jWyaMSFf9xmheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ هم حریف لابی واردات از امارات نشد
🔹
شایان نادری، معاون وزیر سابق جهاد کشاورزی می‌گوید که «لابی واردکننده کالاهای اساسی از امارات» آن‌چنان قوی است که حتی بعد از جنگ هم مسئولان را می‌ترسانند که فقط از ۲ بندر امارات می‌توان کالا وارد کرد.
🔹
واردات کالا از بنادر امارات در جنگ متوقف شد با این حال ۴۰ روز پیش، قنادزاده، معاون سازمان توسعه تجارت، گفت که تجارت با امارات با شیب ملایمی درحال انجام است اما «امیدواریم به شرایط عادی قبل از جنگ بازگردد.»
🔹
واردات کالاهای اساسی در ایران انحصارا در اختیار چند شرکت بزرگ است که در بسیاری از مواقع کالا را نه از شرکت‌های بزرگ تولیدکننده بلکه از امارات می‌خرند. تسویهٔ پول نیز از طریق تراستی‌ها و از مسیر غیررسمی انجام می‌شود.
🔹
فعالان حوزهٔ تجارت می‌گویند «کارمزد انتقال پول از مسیر تراستی‌ها در برخی معاملات ۱۰ تا ۱۵ درصد ارزش معامله است.» یعنی تسویه یک محموله ۱۰۰ میلیون دلاری حدود ۲ تا ۳ هزار میلیارد تومان برای تراستی سود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454012" target="_blank">📅 13:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
به نظر شما، شهرداری تهران امسال به شهروندان مسئولیت‌پذیری که عوارضشون رو به موقع پرداخت کنند، چه جایزه‌ نفیسی تقدیم می‌کنه؟
✅
روش مستقیم پرداخت عوارض خودرو و ملک (شامل نوسازی، مشاغل و پسماند): سوپر اپلیکیشن شهرزاد
✅
دور جدید قرعه‌کشی بزرگ شهرداری به زودی برگزار می‌شود ...</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454011" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNuonlJLOPvkRD5Kr5gG7PpeoUip6qUpfF_Cj5Qo3c6WS11ihbtML80hOWAj4hOLUtSBtixWV_mdePpNeSg6Ww2ZLdOi_QnnfG4w87TJ2_a8I4NdFyxmdl8CIvXpyq5n9uFMzJza6XkxBESiE19Eud8DCiZ9u4Auyp1YIrPeCCvpgGOW34iZKKvDy7aELSOIof94lbMLkjDHh_jcQSCwxFZdnT-TG2RFbsbc8GBl5MtfEKimMe9_z-_vcoDVWMcBjRkBfAXm3bV7BAFVe_FjVwk1113aSSeUdzITbWfNpkAyeKjQIdTB8fTTDFf8gozQsGmB_D1Db1bnW0tHJ7YAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ساخت داخل ۹ همتی تجهیزات و قطعات کارخانه‌های مس در سال ۱۴۰۴
🔰
صرفه‌جویی ۱۲۵ میلیون یورویی مس ایران با بومی‌سازی در پروژه‌های توسعه‌ای
🔻
شرکت ملی صنایع مس ایران با اجرای برنامه‌های بومی‌سازی تجهیزات و قطعات موردنیاز پروژه‌های توسعه‌ای و بخش بهره‌برداری، در سال ۱۴۰۴ از خروج حدود ۴۹ میلیون یورو ارز جلوگیری کرده و مجموع صرفه‌جویی ارزی حاصل از قراردادهای بومی‌سازی این شرکت به ۱۲۵ میلیون یورو رسیده است. همچنین جلوگیری از خروج حدود ۷۶ میلیون یورو ارز در پروژه‌های توسعه‌ای سال ۱۴۰۵ در دستور کار قرار دارد.
🔹
در سال ۱۴۰۴ تعداد ۷هزار و ۵۵۷ آیتم از قطعات یدکی موردنیاز کارخانه‌های شرکت ملی صنایع مس ایران در داخل کشور تولید شده که ارزش آن حدود ۹۰هزار میلیارد ریال بوده است. این بخش در مقایسه با سال گذشته، از نظر تعداد قطعات ۱۷درصد و از نظر ارزش قراردادهای ساخت داخل ۵۶درصد رشد داشته است.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sg
@mespress_ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454010" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454009" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با
بانک‌های متخلف در حوزهٔ وام ازدواج برخورد می‌شود
🔹
معاون امور جوانان وزارت ورزش و جوانان: با وجود اینکه سالانه بین ۴۵۰ تا ۵۰۰ هزار وام ازدواج پرداخت می‌شود، اما همچنان ۵۵۶ هزار نفر در صف انتظار هستند. متأسفانه بانک «سرمایه» با فقط ۲۵۰ متقاضی ثبت‌نام‌شده، هیچ پرداختی در این زمینه نداشته است.
🔹
تعاملات نزدیکی با سازمان بازرسی کل کشور برقرار شده و پیگیری‌های حقوقی برای احقاق حقوق متقاضیان در جریان است. بانک‌های متخلف جهت برخورد قانونی به بانک مرکزی و مراجع قضایی معرفی شده‌اند و این روند تا رسیدن به نقطه مطلوب ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454008" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاموشیِ تنها نیروگاه اتمی مجارستان به‌دلیل کمبود آب!
🔹
نخست‌وزیر مجارستان با اعلام تعطیلی نیروگاه هسته‌ای این کشور «به‌دلیل کاهش شدید سطح آب رودخانهٔ دانوب»، از محدودیت برق و احتمال جریمهٔ مصرف‌کنندگان خبر داد.
🔹
نیروگاه پاکس در ۱۲۰ کیلومتری جنوب پایتخت مجارستان، از آب رودخانهٔ دانوب برای خنک‌کردن رآکتورهای خود استفاده می‌کند. این نیروگاه بیش از ۴۰ درصد برق مجارستان را تأمین می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454007" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا، تنگۀ هرمز همچنان مسدود است و عبور شناورها فقط از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه امکان‌پذیر خواهد بود.
🔸
ساعاتی قبل برخی رسانه‌های وابسته به دشمن با انتشار اخباری مدعی شده بودند ایران با طرحی برای بازگشایی تنگۀ هرمز موافقت کرده؛ طرحی که براساس آن، ورود کشتی‌ها به خلیج فارس از طریق آب‌های سرزمینی ایران و خروج آن‌ها از طریق آب‌های سرزمینی عمان انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454006" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWt9aXes-YjFFkrNfEe3TtLJ7uAGt57H79G1ki6UxU0slSvCEW38XdZWz1q-CzUB3no-4RZBmrcFKOCV1GpOJ3_GXKcGsqFBLZ-M4-0Kx37rkUPUWgRZ_NtY0ufQ8AKgpqz52tUWHx_FSFDpMyWSOwZeqEiQoPjO9htkRqICxXzRgzPzsK4LdtclACCqpwdFq544qYcYuMhqlrp5CF4tExpJ8ZQAHUFzuGuKosxudSMBHCHKdf21wzvT9gcO2rqxxw3ePwV6MCyVqWDGU6j__3mrNs1FMk3iImDN9OKn2eUK_lAHS0bcwWbI2cj-5-mxR85XOgJoj7MzBtDJORRhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۹۹ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۹ هزار واحدی به ۵ میلیون و ۱۵۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454005" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLknFKPto43MxFj6FZI2FYNEgDyK0ZX8wGb9yhtF6n8hhlmuYUYT7GQDx4Wim3iPRtdp2z3ht4VDVK-uBz6UxA5p5YSSPM9oFQB5OiCYhwBzMuvEqrtOCYCXlvRD5lsycNMBMi2japzc4upw7mEVkjS34Fv31vqBvnJOFLmKUt-NaA0Ud2XybMbPecfhf8PwTAqa-vm5rPNpE65D7QD_wF9cEwWXYcFBHdZku26bK8ML3TztwcpP9PaFgtL2FQsZrz5jCcaabwMGCtSuBJpDS-w60rd1OtpQvTcBtbGyGrkRm0UYjuHZ09NwRrMYXS3sG168lad3qpafcLrGM3MbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار رئیس قوه‌قضائیه با آیت‌الله جوادی‌آملی
🔹
اژه‌ای دیروز در سفر به دماوند، با آیت‌الله جوادی‌آملی دیدار و گفت‌وگو کرد و در این دیدار گزارشی از اقدامات، برنامه‌ها و فعالیت‌های قوه‌قضائیه و آخرین وضعیت برخی موضوعات مرتبط با این دستگاه ارائه کرد.
🔹
آیت‌الله جوادی‌آملی در این دیدار با اشاره به جایگاه سوگند و دلایل در فقه اسلامی گفت: علم غیب، مبنای صدور احکام قضایی نیست و معصومان(ع) هم در مقام قضاوت، براساس دلایل، شواهد و سوگند حکم صادر می‌کردند. اگر فردی با شهادت نادرست یا اطلاعات خلاف واقع حقی را تصاحب کند، مسئولیت این اقدام بر عهدهٔ خود او خواهد بود.
🔹
آیت‌الله جوادی‌آملی همچنین حضور گستردهٔ مردم در عرصه‌های مختلف را جلوه‌ای از نصرت الهی دانست و با استناد به آیات قرآن کریم بر نقش ایمان و حضور مردم در حفظ و تداوم نظام اسلامی تأکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454004" target="_blank">📅 12:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق، خستگی را از رکاب‌هایش گرفت
🔹
پیرمردی که مسیر ۲ هزار کیلومتری از خراسان تا کربلا را با دوچرخه طی می‌کند، می‌گوید: «ترس در زیارت معنایی ندارد و خستگی در مسیر عشق به حسین (ع) رنگ می‌بازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454003" target="_blank">📅 12:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_krRhbniHSDMTrAuYvLNklWAbq2SvluFTe46SxJo4U8BicogyewVnPvfygTgRGToJN39lR31VpiMBNoX2zWKV-tfiHpnoEReR6JlkyKIOLC7ifQVzR_pctk8fa5HR7kb0342yYYQhlk7qZTEW9EJpd648E_GU99qyun4oQ0izuoV6zkfnBKOusEZCKOyEdDSBMTW0sk5P5HrJGaD5VFceQJzXp0DtU0Xi74YXU3UCNVniZ--6J09C03XulTHll2jfNVdcjYCvwc-9uyC0KBmHNgWpWRCq4DlWSrfFpv_DiIeaO_iokp__hXQJNBqzdgqnXcr-b9GGzZVEGotpfSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سی‌ان‌ان از عوامل عقب‌نشینی ترامپ
🔹
بعد از عقب‌نشینی ترامپ از تهدید دوباره‌اش به تشدید حملات نظامی علیه ایران، سی‌ان‌ان در تحلیلی به قلم برد لندون، خبرنگار ارشد امور نظامی این شبکه، گزارش داد تحلیلگران فشارهای اقتصادی ناشی از جنگ بر متحدان واشنگتن در منطقه را یکی از دلایل تمایل این کشورها به توقف جنگ آمریکا علیه ایران عنوان کرده‌اند.
🔹
طبق این گزارش، در همین حال، ارتش آمریکا با پرسش‌های جدی درباره توانایی خود برای دفاع از نیروهایش روبه‌روست؛ زیرا ذخایر موشک‌های رهگیر سامانه‌های پاتریوت و تاد به‌طور فزاینده‌ای رو به کاهش است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454002" target="_blank">📅 11:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYSC4nSUZh3AiP_da1nVAe3aHCEFuEeAukI3mpAtXC5K_jo1zG8ltr-2MGuKzrMc8C0NyTqHchVEhLjBJVjmXaOd9ADqBizRNP9tnTNmDcUkBWUAweamRTORxliYpvD-FbS7HXwUlk37aNAT9njF-ux11yrAtPOKS7oZmKwh0zRHityhQpWh7WmdO6cJ3nEoURi5pctdiGIXeVA7kjJfaQWSIWxfHUbH6yIBwFKNvEEpivCvGizncsr9g3UNEHwKkftReiB_XNBClGWtgZUY-SONoSHjh72bDJx5xgKecHixS94lMVm5_LoZ3iBeQDS9SFpr3VitVzFWjBQO9zi1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سرپرست وزارت دفاع: نه غافل‌گیر می‌شویم نه منفعل
🔹
تهدید را مبنای افزایش آمادگی، تقویت بازدارندگی و ارتقای قدرت خود قرار می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454001" target="_blank">📅 11:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان یزد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضرب‌الاجل دادستان یزد به ۲۰۸ فعال اقتصادی برای ایفای تعهدات ارزی
@YazdFars
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454000" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e5f69ffc.mp4?token=d-uApch8RwnqtXkRqMaQ4ArXHAjam6tnbSAlGaOlUY3Rb_6QVUgJZC2ogMQMJINWRuReW0FhGcUOyVc5pjHZyqrWQZKZzVpQah4JhKn24nraikqVOMmmZI-_f5_oAjQ_-6r8hDSJBGfPuqWiXvaI4neiNWSNgJHZ1CVcVKmSS5qzTo2qikwanNL6Og2lON1AN5ULgcAwYx3WXdr1tSk9mzs4T0SoJr13itta9NABhGjuSfmF0dYN5zL74SQl9JzAHEYZ3oyuhZvnBb1ZBo6F9hqi7nChbJvT0pJKJ1i_g9ILIquS-XpKbxWoJlg6ErFW5RsqUP102j-3YY-R3Mt8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e5f69ffc.mp4?token=d-uApch8RwnqtXkRqMaQ4ArXHAjam6tnbSAlGaOlUY3Rb_6QVUgJZC2ogMQMJINWRuReW0FhGcUOyVc5pjHZyqrWQZKZzVpQah4JhKn24nraikqVOMmmZI-_f5_oAjQ_-6r8hDSJBGfPuqWiXvaI4neiNWSNgJHZ1CVcVKmSS5qzTo2qikwanNL6Og2lON1AN5ULgcAwYx3WXdr1tSk9mzs4T0SoJr13itta9NABhGjuSfmF0dYN5zL74SQl9JzAHEYZ3oyuhZvnBb1ZBo6F9hqi7nChbJvT0pJKJ1i_g9ILIquS-XpKbxWoJlg6ErFW5RsqUP102j-3YY-R3Mt8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش میدانی فارس از وضعیت زائران در پایانۀ برکت مهران
🔹
به گفتۀ زائران زمان انتظار زائران برای انتقال از پایانه شهید رئیسی (برکت) مرز مهران که روز گذشته به حدود چهار ساعت رسیده بود، صبح امروز با افزایش ناوگان حمل‌ونقل عمومی به ۱۵ دقیقه کاهش یافته است.
🔹
اقدامی که با هدف مدیریت موج بازگشت زائران و تسریع در جابه‌جایی مسافران انجام شد.
🔹
مرز مهران در روز گذشته به‌دلیل حجم بالای بازگشت زائران شاهد افزایش تقاضا برای ناوگان حمل‌ونقل بود، اما با استقرار اتوبوس‌های جدید، روند انتقال مسافران به استان‌های مختلف از جمله تهران، مازندران، همدان و زنجان سرعت گرفت.
🔹
استاندار ایلام: ‌هزار و ۲۰۰ دستگاه اتوبوس در پایانه شهید رئیسی برای مدیریت موج بازگشت زائران مستقر شده. شمار رفت‌وآمدها در گذرگاه مرزی مهران از ۲ میلیون و ۱۰۰ هزار نفر عبور کرده است.
🔹
۱۵۰ دستگاه اتوبوس دیگر تا دو ساعت آینده وارد پایانه خواهند شد و ۶۰۰ دستگاه ناوگان نیز در مسیر مرز مهران قرار دارند تا روند انتقال زائران با سرعت بیشتری ادامه پیدا کند.
🔹
براساس آمار اعلام‌شده، در شبانه‌روز گذشته، همزمان با تداوم موج بازگشت زائران اربعین، ۲۰۴ هزار و ۸۴۲ نفر از مرز بین‌المللی مهران تردد کردند؛ در این مدت ۴۶ هزار و ۷۵۸ زائر ایرانی از کشور خارج و ۱۵۵ هزار و ۶۵۶ زائر ایرانی از طریق مرز مهران وارد کشور شدند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453999" target="_blank">📅 10:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca61f9402.mp4?token=ubUN-Bs8_b17FRpK2tK9ZU7z15HWy5JeKulbxFunZL2h8zE3NBausFoTJbpSqkMyWPT511eUVrc0D_sjRV9YI374pn4HSy_lSxR5GBShaeN7TVc2pl0NSgEWU0kOEPc_d-CuK1_EyboAUFIq9cxaCwdc40zLZpKdFKV80rDe5L2quwZ2lDLkOlbGY2k9VJVxUMzcqCvZ6Lj3VObZMQj8ikdyy8ACSidXRkkV3D_rKNjrB7RHRwDOBlAnKR1oYcurOfp7xTfcmG2qn6Yq1aoWlLsyq0nOONXFK2JGOGeROZr803cmgDjnW2Y30GhbUin5fsL2iizM4odVrKIy_TUhfKagOzeEtl_E1ixk52TGl2YU3gb17fFugBTWaZNEPs-35_M7Ulrtqno2hxgsG4n862ow2xPr-Td41s_n06Qj1-RETuCIpwhZ27L4gpKBLTpS_4-gViq1R3269uYgCaxfiMtudaFcTMoB1zS7onbXUFy7Cmxy1LYV-d7JZs0chMjsJKJ_GumuBY1YsH6bvOS20QSsfcpHBn3qOAJvt8xBcthV_9VhmefkivKvWaCVlGdA8QcQGKb9lEfYq4B-xGwR6qvgSr-MGLd0wcq6o5UqNWT9XmEGokiH27NidLMhTowtqL5ibnJvc4B8Tn0Q6beef7Q419KqTVNi2GoEnh4aElM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca61f9402.mp4?token=ubUN-Bs8_b17FRpK2tK9ZU7z15HWy5JeKulbxFunZL2h8zE3NBausFoTJbpSqkMyWPT511eUVrc0D_sjRV9YI374pn4HSy_lSxR5GBShaeN7TVc2pl0NSgEWU0kOEPc_d-CuK1_EyboAUFIq9cxaCwdc40zLZpKdFKV80rDe5L2quwZ2lDLkOlbGY2k9VJVxUMzcqCvZ6Lj3VObZMQj8ikdyy8ACSidXRkkV3D_rKNjrB7RHRwDOBlAnKR1oYcurOfp7xTfcmG2qn6Yq1aoWlLsyq0nOONXFK2JGOGeROZr803cmgDjnW2Y30GhbUin5fsL2iizM4odVrKIy_TUhfKagOzeEtl_E1ixk52TGl2YU3gb17fFugBTWaZNEPs-35_M7Ulrtqno2hxgsG4n862ow2xPr-Td41s_n06Qj1-RETuCIpwhZ27L4gpKBLTpS_4-gViq1R3269uYgCaxfiMtudaFcTMoB1zS7onbXUFy7Cmxy1LYV-d7JZs0chMjsJKJ_GumuBY1YsH6bvOS20QSsfcpHBn3qOAJvt8xBcthV_9VhmefkivKvWaCVlGdA8QcQGKb9lEfYq4B-xGwR6qvgSr-MGLd0wcq6o5UqNWT9XmEGokiH27NidLMhTowtqL5ibnJvc4B8Tn0Q6beef7Q419KqTVNi2GoEnh4aElM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات وقیحانۀ سلطنت‌طلبان: ما لشکریان یزید هستیم!
⚠️
هشدار؛ محتوای این کلیپ به‌علت توهین‌های بی‌شرمانه به مقدسات، مناسب کودکان و افراد حساس نیست.
@Fars_plus</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453997" target="_blank">📅 10:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa10b8ba2.mp4?token=OLg06lE4AB8qgL1FmdCir4qUqX0EUX9R4Uk5H7SiQuzcI2CnQGzz-oHvt-ViwibRlC7l7C5ZTtO7bEKFGj1TB3508tg2_1WgkGduifswSJYllrN_Y9X5HmuW0_KJCFw59RgyrqXwPapmPC8hq-ZM3ZAInJKIW6L_Bg-B8EP039fppUgSkf8Fkf0i2LYBgPcQg6sAXbfuSBAB1c9rEM99kb0aRULNxWox3c8ZSjyJdAS320QxfIISyMqUko-l5dKk-bsNxm9Te0X6d_4O9tXkZFwjEZ9w1wydIxZPqtKVnG1lyMUy6dUW-wspKYZ5Sz2i8hclqf44NuTafY9Yw05FqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa10b8ba2.mp4?token=OLg06lE4AB8qgL1FmdCir4qUqX0EUX9R4Uk5H7SiQuzcI2CnQGzz-oHvt-ViwibRlC7l7C5ZTtO7bEKFGj1TB3508tg2_1WgkGduifswSJYllrN_Y9X5HmuW0_KJCFw59RgyrqXwPapmPC8hq-ZM3ZAInJKIW6L_Bg-B8EP039fppUgSkf8Fkf0i2LYBgPcQg6sAXbfuSBAB1c9rEM99kb0aRULNxWox3c8ZSjyJdAS320QxfIISyMqUko-l5dKk-bsNxm9Te0X6d_4O9tXkZFwjEZ9w1wydIxZPqtKVnG1lyMUy6dUW-wspKYZ5Sz2i8hclqf44NuTafY9Yw05FqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط هواپیما در پرو ۱۱ گردشگر اروپایی را به‌کام مرگ کشاند
🔹
در پی سقوط یک هواپیمای گردشگری در جنوب پرو بر فراز محوطه باستان‌شناسی ثبت‌شده در فهرست میراث جهانی یونسکو، ۱۳ نفر از جمله ۱۱ مسافر و ۲ خلبان جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453996" target="_blank">📅 10:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf35f6e62.mp4?token=oL9tIl9x7fU0PJkrR1RcPfthVgfYgSN82O7tQzKhg31b3U-FB0G2ILsiXpSiNbBcdaFQK3ddXIT0NQ6HzVqImHhOL6myoAYDa4EAzI0Z-MXmtCfBB5Ja7p9Ho-HEzZcR69IK6US4-OPDv9caSUTRw8F_5cwXQuD81OE8Pe3Oq_zBLYFZQLOzc9SM2XLSa5PnEEhLypPCoiOswp3S5vxW1J3vJwSBYgPazLVl557J6mvL4AfXRz1FHufqB-7Phu_e5iXygBS3fCFw_wIU8AGjW62ptYkUhbKoT5vX9Hwe5EIxfGXSP-2oWRLdYY-t1zfIO90VWz54uaYSSSHiGUZxhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf35f6e62.mp4?token=oL9tIl9x7fU0PJkrR1RcPfthVgfYgSN82O7tQzKhg31b3U-FB0G2ILsiXpSiNbBcdaFQK3ddXIT0NQ6HzVqImHhOL6myoAYDa4EAzI0Z-MXmtCfBB5Ja7p9Ho-HEzZcR69IK6US4-OPDv9caSUTRw8F_5cwXQuD81OE8Pe3Oq_zBLYFZQLOzc9SM2XLSa5PnEEhLypPCoiOswp3S5vxW1J3vJwSBYgPazLVl557J6mvL4AfXRz1FHufqB-7Phu_e5iXygBS3fCFw_wIU8AGjW62ptYkUhbKoT5vX9Hwe5EIxfGXSP-2oWRLdYY-t1zfIO90VWz54uaYSSSHiGUZxhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پسرم را از دفترچه‌اش شناسایی کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453994" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89916d3d3f.mp4?token=aPQN8qkSEVrjuXN769aQbwJTr4cJR34dXPwnWL2IWXc_SeejEQmHHl6HH5nAZdq4EajLVtxjuRIUyQEf9SiqyP20aYTVziQI47S9C8msOq3miWZFHhJHDInbD0K7YXYZxozfhEvqTT8etwk9v7WXKQhoXxnF0G2LLfU12JDUjFBQNb2LnihxXKz-UIqIUXzcGtBpIoJYPKkCGb3Q8ogppOnJFm-_1Mr5g6ItUx4fFClD3J51yOOYJef9YKz8bjQlbvDFm-PC9ExSSLQVdfhBoUmLLpewAvKR5WffZILOBV580sgFhK_IFJ6ccLNp5JyQboP4f97IjREOhuf5ys6NTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89916d3d3f.mp4?token=aPQN8qkSEVrjuXN769aQbwJTr4cJR34dXPwnWL2IWXc_SeejEQmHHl6HH5nAZdq4EajLVtxjuRIUyQEf9SiqyP20aYTVziQI47S9C8msOq3miWZFHhJHDInbD0K7YXYZxozfhEvqTT8etwk9v7WXKQhoXxnF0G2LLfU12JDUjFBQNb2LnihxXKz-UIqIUXzcGtBpIoJYPKkCGb3Q8ogppOnJFm-_1Mr5g6ItUx4fFClD3J51yOOYJef9YKz8bjQlbvDFm-PC9ExSSLQVdfhBoUmLLpewAvKR5WffZILOBV580sgFhK_IFJ6ccLNp5JyQboP4f97IjREOhuf5ys6NTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در رستوران آمریکایی با حداقل ۳ کشته
🔹
خشونت مسلحانه در آمریکا این بار یک رستوران فست‌فود در شهر «توئین فالز» را هدف قرار داد و ۳ کشته و ۷ زخمی به‌جا گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453993" target="_blank">📅 09:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlguzSchoEp3c4IQTPtpiKTADwW31kvltn85KadGAtWWAE6mC5OGTj2-HggBAWLHTPdz1vaa49xAAabKV_d44vlXsH21q7L9BLR6OQDC6AFXLl-rEVjWVv4jyhwdZWGjJZFI9lnWHDut-Vlvr7Mk-BYpYDv-wdd6rm75Pwe5mImR_34esZhw8HJrVo7ZnQMLtFHV1vC6R3s-6iIPvBbUpCWqD0UKBR7cYovj-MuU3KxQOEoYci2dQKzQgQ5tGHgeMS_aMw1ckOWXAwGCKPR3_OVJzAOfNlr4f3s-Y28aoxDAE-2aqpzeNDSMcwrFbtbhNfV14CgxuLXA-eRDH70S4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxk8triuNwIlzuRhCBhaWi9QJoDbDH_lvS7-8yjF5g9U33BxTnqH5naWSbk-4-pMHPyhCnGDbyLPsdkUTTLmLEYZPeIRBf6rOZr5TAGFUK_S13Xo_bqI6xrP7aq5xEW0M_7ZUTxAquem0RWagN7mtVWb2ThCW-Ws4soSLbce0Qwh74ZlaDVwvuJlVaNdIFblNAfrnjH3jmvdwaWaM8tixuxE_4Y70OseOR05sQoy7bi7z_NO01MPhYFB1TVi4EhyzzpvcEZJASLek6eZJBqJLX_94pkYWb17kfCNDZAv4koAamuppu6N6g3jMZEjuGtwdEvBa6EkmSs6seH8p_n3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHd5CCqtAzeMHuQZVO6uyUPxFbPo8VOco5UtSBdD20RRDacv7ysOjRdhAlZQSaUOM8e8EYBMkPXpDVr6fan8naNN2ioQ9HR5jlebJwOK5g-1SNgGyihDROg_8Kf5meLWuqH9ugiW7xaqMjN6lq_lhPTzsks39K5vVHLvZdLm-aUAwSpiTmB9xWx1BRY0gf6dr0YeE-NlNJfq-VxOBmUoRWfAUwdo1BrEmjUwc9Ttw8cz5fcNIsp5xwAVQrcC_TCjDyK6dhgAvHdBrjQ7Z05OUtmHK1ZZAA5AhemVrHkqX-M-anXy-3HMPllWvotDcsXZHHXijUHiUKh1tz7zqmMn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdxqpDiTvojLiz61kqZkoophE27dLEK28h29fR4m9Bw26HleIF1BeJdMAfeNTMlJtX5t1MRS1VSpudtlg7SO0CUQxF7IeLdROF0qt_z1pYhd99iM_GKKH75bPMSYXpjo-UHZiWFl5iJu10NDFt46qrsCewjPF4oaw84a_9LIoB6X3A4acE9vlGTnueJyGL1nAGqdM6bVfODXH5uR7MWnt1wAR31TNc1JfrjgErNV543a8qPa9NeOHiIgIizEw1gwYAbLXRjiYoKKzVPBPEqZZKAtZpao4XBUnMKeesZgIbuOuPwZrC4EoqPXwXFYZV1mH9NpblQhBz_2IYzidj6AZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUEu3NRb98eJniG5Jc08tMpiefjD9o-k4NEyx4C-wlFJbAVI6kGUK6B-0-21LCAyDDgs22v1IUMa2r0Pqg2o5Do0wNR-cPIAIPbTGPF0m7t0SS8H1C1Z7qOds7kwn1aZ3a3zbLEy7TujfTcJ-EnLuM82zxQOP9j__DcX0apPxy4fe2gxP5mduh8u1vATloJHBZ1mNsQKRPVAVHjn7zwbI4QikjNizQ8rKeTEhD_YBDjKpdCBZNmeZmKBIR6U4pTFrkKAgm6-_RKhwUF8ghChmfAcDgEDrvrBCIyQQf-n-2QmJchyr9azvhPw69UFg4tk0_4RQdqLPaSXzGDmq7vmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcB4tbwtx_fa66QyXF5LNA1zwiQH1WrJWA-bnfyqZmNk8TgXj4ccWLIbredA7xpD-ysx-J5tppo7bgasuWeocFvM-30KHzQ944Jxhn8XjalINyEnbsz8a51g6DMZdiZBH9zuIIxSondwebz4aevgI9wU7SBPeiLqRDY3AeoSDkV5J1EcTj5q_dIeoaVmlyJX5_b5Ylsqh0T-8PBfdo6zHufCqJqKkR7MxhaTlDIBcFHGJegHFKt-9RKynbkaeXQIY-vCpFupcQUtK4yNqPzJjtKB9bpXDLDqKHKvszg7z9765QePoX132NrvlXOkiQmNN6Su210WFisbankogWm-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gk9xv3tawHot_2etiTF8D50kxAZycfGGG9Jl2wuWgnSq6-38Su0XxOrfwl3z9nWYx9TfMmA5FbG4tRVTurRT2y26SJySUmVEg0aMx-qA4pJo4hqQFcu7NkQI0jo1qG3bHbGQov4jLCLZQG4ySZJwYJ9FRhRGUfUJdppqFEPd47JLvN2eHyTB2kgR-wjxd9i1V58uBoB9OaJT-qm7A_sruhdYAm_Y9-sMfgnm4DvVTJnaytDhVfOliHTMOuRSFx0hJbWeQYA4CGHQaig11AClcaKgx6tusqVlC5sdDsz8h9zIwFt7TBoWhu2JShm4pOzLH4OuiaQ9eOflGBGenlT29g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پایانۀ برون‌استانی در مرز شلمچه
🔹
با راه‌اندازی پایانۀ برون‌استانی در مرز شلمچه با ظرفیت ۱۶۰۰ اتوبوس، زائران بدون نیاز به شهرهای آبادان و خرمشهر از نقطه صفر مرزی به استان‌های مبدأ منتقل خواهند شد.
عکس:
فریدحمود
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453986" target="_blank">📅 09:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDZ-I1V_VTi_BcJ8LjEUAZvvua7JpVReJFG2Ee_hk1VGTjTQKcNUQMDNhM1Jr6gyAxk1vSGI25-fiilmK6tAY9yrLaobdeUhmDrUd-eAh_hgMz_Vj3pwHlsds4ZGXdPYfUv113waEl8Yd1TgvsaJt0-fA4ILCSl-Z9cfLs5li2gvLgs5B8Y5j8EGe9tFlkqiODJhjgRf6lVZ6IobKCluKI2MpQEp8SIzmMVzjNPV7IWv2DD3Sx_5OkD0XCuI0F8qmjmN0R4AFoA0IAwxTlwdnEfRz3NzjbFkGdWjMrzs4Iu4hXCnT5EjsWazdfXFDZyDNkncyIxENRQ7g_5frhU3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع روسیه: از دیشب تا حالا ۶۳۵ پهپاد اوکراینی را بر فراز شهرهای مختلف روسیه سرنگون کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453985" target="_blank">📅 08:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fluwK1M5PnQwjlPq3vw3oJq2_-NIqr7BYpMycRNSrMwbaW-FAvR33THGnm4tqBA4wRv0mR7s0YtIuwm_3xNBUUewn4Z2jcDAGb5Km647tQnGOPEn6x2jTjFevRr-jWovisvqXUlJWb0ZzM7v9PWhFPC_Ja7_GF9zaYwU6ygNv3Kc2lXH9c6r20BTYFe00rPjBUM2u_60ZFznjhhdlvoO8r_qMSVokWoV3QIPHm6VZXp8kNGHAPdc5JSJXlSSQurKKTmZ2pkDghXpzAltJjhEyPq6FNxACp3hVoyZ0Z76G9YqR1XcjFcfjOfdMpvYGt5_1B_t9V5UHQTRsO4OzfrDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت‌نفت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453984" target="_blank">📅 08:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0233813a9.mp4?token=CTwDzf8QAOKKkU07SpJLJnWtDZrytW63T-uQDDXPRWREJFwXR9Vu75OoBMB7Yng1d38fPOsxsc2ZdizoqgZ7FtyToXJ4kE_NPx7jxLnuHQuMohvzvBQ_YIeaJR7_Lbl43U76wFDTkDo_E9nulXLDoGKTPPuEJ4VHBOiQZjtzWibmWZLPp2ukzYJMQ8Le05VQ4vOwYYvk2RQQZgEeni9z2EprJjo05451rT3PZ-CDNAJIqYFZ7V757RkmzjaTSGDn0nHhi_mawgqx0pUgi6QbSJXL-wtaDhYwa6UF2PxWvh2V79cG_3NRTM6CB-dxoixq71YqsInsS6pfHJbrqeicZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0233813a9.mp4?token=CTwDzf8QAOKKkU07SpJLJnWtDZrytW63T-uQDDXPRWREJFwXR9Vu75OoBMB7Yng1d38fPOsxsc2ZdizoqgZ7FtyToXJ4kE_NPx7jxLnuHQuMohvzvBQ_YIeaJR7_Lbl43U76wFDTkDo_E9nulXLDoGKTPPuEJ4VHBOiQZjtzWibmWZLPp2ukzYJMQ8Le05VQ4vOwYYvk2RQQZgEeni9z2EprJjo05451rT3PZ-CDNAJIqYFZ7V757RkmzjaTSGDn0nHhi_mawgqx0pUgi6QbSJXL-wtaDhYwa6UF2PxWvh2V79cG_3NRTM6CB-dxoixq71YqsInsS6pfHJbrqeicZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453983" target="_blank">📅 08:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300b440c0c.mp4?token=SEcmUCfUw5XdGvSPd9ZyqhB1jpdgzYBhjHLAvO4euamufY9ATPqi5mn2gPTbxMNRwCBIoWVv9YxDJYOTqspzvjIL_-m-KTTe-F_JRbI_sS7jc7cXgDWNhDv-zLBlrwVf4t-6T3yOXzxjuLAfBVzBiqOss1-i0CNv7MBZ1QPM4sCQhBle1fkV2QMcUOZ5YCy93Q-VSmv_DxIu6gI2rB_K2ANFfkIDENK6iUodQpTrpKD4narxvHbuxlCCt1g8KaCGaKbz3eTEnyudPIa1vmkq-BWYKxgE55hd-M2ZmBClh13kZmvO-g51dE_ybD1_mgKR41Tc45jWr3aXjyo05w9zZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300b440c0c.mp4?token=SEcmUCfUw5XdGvSPd9ZyqhB1jpdgzYBhjHLAvO4euamufY9ATPqi5mn2gPTbxMNRwCBIoWVv9YxDJYOTqspzvjIL_-m-KTTe-F_JRbI_sS7jc7cXgDWNhDv-zLBlrwVf4t-6T3yOXzxjuLAfBVzBiqOss1-i0CNv7MBZ1QPM4sCQhBle1fkV2QMcUOZ5YCy93Q-VSmv_DxIu6gI2rB_K2ANFfkIDENK6iUodQpTrpKD4narxvHbuxlCCt1g8KaCGaKbz3eTEnyudPIa1vmkq-BWYKxgE55hd-M2ZmBClh13kZmvO-g51dE_ybD1_mgKR41Tc45jWr3aXjyo05w9zZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453982" target="_blank">📅 08:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d82d0e7b.mp4?token=LUn4PHI6Ni4kjnm3fp_JZ2uuHimdXHKo0mNvpqdYUjejOf7kw3nQA_UbjKM8Ot4bKL3oXBxqKGPjfLnkegjtHH2_1tz_pPYridKXIyPzOhNYhgjBdWF048O7iTebK0mdQyWFqVNfvMUy6Cn_GrZVK7kGKl-R8uEUwFZcnLyttNLFuenjAKEaHrBKnei0DD7GHYuHwr5rxwghOOxSeBmnNrklbDlmshHhhqb6PzSqbytp6tmDAEwpMUYTxWqZNYyTePmymFn6funbI6b9DZFiLJvsuaCiofGxO-q0r2x96TJygg2tK51ROvlUOUy5CoRULkha-DdpjLlz6th4i-Y-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d82d0e7b.mp4?token=LUn4PHI6Ni4kjnm3fp_JZ2uuHimdXHKo0mNvpqdYUjejOf7kw3nQA_UbjKM8Ot4bKL3oXBxqKGPjfLnkegjtHH2_1tz_pPYridKXIyPzOhNYhgjBdWF048O7iTebK0mdQyWFqVNfvMUy6Cn_GrZVK7kGKl-R8uEUwFZcnLyttNLFuenjAKEaHrBKnei0DD7GHYuHwr5rxwghOOxSeBmnNrklbDlmshHhhqb6PzSqbytp6tmDAEwpMUYTxWqZNYyTePmymFn6funbI6b9DZFiLJvsuaCiofGxO-q0r2x96TJygg2tK51ROvlUOUy5CoRULkha-DdpjLlz6th4i-Y-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران حسینی از کربلای معلی در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/453981" target="_blank">📅 07:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453977">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=IEuWtExKmd90jGaJtHvGL-kaTt-wsyzky_ON87emtSmF2jYFzHair6pTSLmpoOvEKYgvdG2HJBJj6txci5Rnu6ZPtJU8v4BKQT3FCBXlKH3HKjpacUBUiSrPN79CQPz0sVkRRyNfI2MTMbWOKxRnvuDXRP2QowDVVQ8594WPSfAScUD0zb9mofpEzHAr0oHCtWblfP1eCSIHqH3h5QVLyIt9T_BXvXWQrbyUfztOvieRG7IYUfnTMjpvAkqZK46Htctcc7flYhOOikT_0UYs0a-K8qkyqRBgBNKsyM_rmDBbV8XkzSt0goGFP6KqwEL88YSLkKl4rbYjzwok9Ldl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b32c7f4d.mp4?token=IEuWtExKmd90jGaJtHvGL-kaTt-wsyzky_ON87emtSmF2jYFzHair6pTSLmpoOvEKYgvdG2HJBJj6txci5Rnu6ZPtJU8v4BKQT3FCBXlKH3HKjpacUBUiSrPN79CQPz0sVkRRyNfI2MTMbWOKxRnvuDXRP2QowDVVQ8594WPSfAScUD0zb9mofpEzHAr0oHCtWblfP1eCSIHqH3h5QVLyIt9T_BXvXWQrbyUfztOvieRG7IYUfnTMjpvAkqZK46Htctcc7flYhOOikT_0UYs0a-K8qkyqRBgBNKsyM_rmDBbV8XkzSt0goGFP6KqwEL88YSLkKl4rbYjzwok9Ldl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
🔹
خبرگزاری آسوشیتدپرس گزارش کرد این آتش‌سوزی حوالی ظهر شنبه به وقت محلی آغاز شد و علف‌ها و بوته‌های یک محوطه باز را سوزاند اما به‌سرعت به‌سمت شمال و شرق و به‌ سوی مناطق مسکونی گسترش یافت.
🔹
مقامات محلی، با اعلام بالاترین سطح هشدار تخلیۀ فوری، خطوط اتوبوسرانی شهری را برای خارج کردن مردم فعال کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453977" target="_blank">📅 07:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtgEdEt44DjOiTbl7JyhImDXOKBJ5mPoyYIw5Hxs4Wjbd_Q7e0IbHoBlIBbgK9akq-3i3dvVtD0juwp5ff4hzc_13FnGz7wP_DQSIHfywyKelOfZBdYiVQay5ffaUB5_whtWXIoYXGnKudllJbqoTSuJOB4wCPizszEoDvZ8rx_DOzlYTNv82UFIUYS2ssZHNazvUOutwm9pnbKyeyKIHdYc8sx4dEq1BHFkCUp2XhaONftPiM8AKBOfcjQ8MzhJPhOkZZf5GArD6jTo4g_3zNZYVwl2SYmw_I31VubCZXokz_Us9SAA7eJ-nrnOE98Pkk3ow3F8w1mcZ5SN2KxCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا با طناب ترامپ به چاه افتاد
🔹
نشریۀ تلگراف از تصمیم قاطع یوفا دربارۀ رئیس فیفا بعد از طرح فروش جام‌جهانی خبر داد و نوشت: زمان اخراج اینفانتینو رسیده است!
🔹
طرح فروش حقوق تجاری جام‌جهانی به شرکت برادر داماد ترامپ، هفتۀ گذشته از سوی رئیس فیفا مطرح شد اما بلافاصله با مخالفت یوفا، کونکاکاف و AFC همراه شد.
🔹
یوفا حتی تهدید به کناره‌گیری از جام‌جهانی کرد تا رئیس فیفا بعد از تنها ۴ روز از ارائۀ آن، توقف و شکست این پروژه را اعلام کند.
🔹
اما جایگاه اینفانتینو وقتی به خطر افتاد که رابطه‌های مشکوک و سیاسی‌اش با ترامپ آغاز شد. او چندین مرتبه از سوی اعضای فیفا به‌خاطر اهدای جایزه من‌درآوردی صلح به ترامپ و بخشیدن کارت قرمز مهاجم آمریکا در ایام جام‌جهانی بازخواست شده بود.
🔹
نشریۀ تلگراف می‌نویسد که عقب‌نشینی رئیس فیفا از این طرح کافی نبود چون اعضای یوفا احساس خیانت از سوی اینفانتینو می‌کنند و می‌خواهند او استعفایش را بدهد یا مجبور به اخراجش می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453976" target="_blank">📅 06:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">داستان تکراری ترامپ: برای منافع جهان و بقای ایران، حمله را لغو کردم
🔹
دونالد ترامپ در ابتدا برای حفظ آبروی ارتش تروریستی آمریکا به‌دلیل عقب‌نشینی‌های مکرر، به تعریف و تمجید از آن‌چه توانمندی بی‌نظیر آمریکا توصیف کرد، پرداخت.
🔹
ترامپ اما بلافاصله با تکرار ادعاهای پیشین خود مدعی شد: ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم.
🔹
او سپس با کنار هم قرار دادن لیست آرزوهای خود، ادعا کرد که طبق تفاهم‌نامه، باید تنگۀ هرمز فورا و کامل بازگشایی شده و تهدید هسته‌ای ایران پایان یابد.
🔹
رئیس‌جمهور آمریکا در ادامۀ پریشان‌گویی خود، افزود: بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453975" target="_blank">📅 06:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvstMSeGgFEsN9jQj7Y3tyk__xc24cNCiAMFj0DPyJvP4VkOjzjFGNyACnYXmhmvum9pcBjuR7Hqw0A7KVvFxkeYpoJeWzWzNg57VKD6puEAlkYunNVWbUSqBzM6K81WDmWhF0D5Yg4iT0WspKsmbS2S41gHegI1kzYKPQW4z2AwbajNq2j4eYhhtNGhEYgTrwOjx0_qmd14EiUyeJ2fRdpn1_X_IohF6E_XDf8QoFk8fE9y9s9Y5vaJuPGH5kdnA5uJzGapwsTGIqyLZ-ZPdlMkCFPVQXeFmXUQnJPkjLHmRuiE-lhdKoxWBd4tpI6lRZsJNRI8CuXrgRsTRfhfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۸ ریشتری در تخت هرمزگان
🔹
ساعت ۵:۰۷ دقیقۀ بامداد امروز، زمین‌لرزه‌ای به بزرگی ۳.۸ ریشتر و در عمق ۱۰ کیلومتری زمین، حوالی تخت در استان هرمزگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453974" target="_blank">📅 05:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/432d846a83.mp4?token=KXabJfTi5bwV7UV3fg3z2uiUJ8wzIia6U1_pGdev2B9bjkWGshmjmOSFUVlkByTQjWBdwcdFIWbgDtX5c3MWratUkp7_RalyB3-9q-nnrR-jRsA6VN8wPIBn5QncTwBosVR6OOHFAA4Q5cAvN_zO7elZ_HRNJ-gb2eIxwndeFONECH8xbjC_fAhzKOrLK5HlItRPetCYh3hoaXbMV4Vzu9COaFU3nqVPJ9WMXxE7yutFwOz03AjoEQG419qDyFncxA4L6g41-ToON9UUnUJEdD_AiNIZ0lgFd0fJPMt9EMgEPb9e83-av1E60UyYtiI-LkU60QOFsu-Fk2NQwdgFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/432d846a83.mp4?token=KXabJfTi5bwV7UV3fg3z2uiUJ8wzIia6U1_pGdev2B9bjkWGshmjmOSFUVlkByTQjWBdwcdFIWbgDtX5c3MWratUkp7_RalyB3-9q-nnrR-jRsA6VN8wPIBn5QncTwBosVR6OOHFAA4Q5cAvN_zO7elZ_HRNJ-gb2eIxwndeFONECH8xbjC_fAhzKOrLK5HlItRPetCYh3hoaXbMV4Vzu9COaFU3nqVPJ9WMXxE7yutFwOz03AjoEQG419qDyFncxA4L6g41-ToON9UUnUJEdD_AiNIZ0lgFd0fJPMt9EMgEPb9e83-av1E60UyYtiI-LkU60QOFsu-Fk2NQwdgFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری شدید نیروهای ارتش و انصارالله یمن با عناصر وابسته به ریاض
🔹
منابع یمنی از درگیری شدید میان نیروهای ارتش و انصارالله با شبه‌نظامیان وابسته به ریاض در مناطق جبل هان، مدرات، البرح و جبل حبشی در غرب شهر تعز (جنوب غرب یمن) خبر می‌دهند.
🔹
این دومین درگیری شدید زمینی طی دو هفته اخیر میان دو طرف محسوب می‌شود.
🔹
پیش از این گزارش‌هایی از آمادگی هر دو جبهه برای ورود دوباره به درگیری زمینی منتشر شده بود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453972" target="_blank">📅 05:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
حال‌وهوای مسیر نجف به کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/453971" target="_blank">📅 03:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHs1Yu8x4z5Zs8DaaWL8PXj3mtZk1gdfqZKkCsT5Hc0YspTOg8dnqjJqm7x1o3oG2cbfPHBReBCuMRjhqEgKhnEdCdiQG7O5pvImQ-rLlQ97O2ifnstdVPXqLRVTfq0ACRwviGQeVLpyoqd5N1b5w-zvrKhjFxXZ21XUzwg-Fg7vbNgNO-Hb4-qpaT6GUKh78Er-_SEP3fDTOlHcl-dLI_Bv-giSWtYIXOW7Radzp91WSsU2oUf6irtCiQ7h35jZCRlQXkWMjJw7_c5ei4qbIbFUbdW-V6pJSimJKrHTl7OSnDWqRp4_O-PveiPxc94r4_jbvNa0o_WSUPytVMbMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان و هنر ائتلاف‌سازی‌های بی‌سرانجام
🔹
عربستان سعودی دوباره از تشکیل یک ائتلاف بین‌المللی خبر داده که هدف اعلام‌شده‌اش حفاظت از امنیت دریانوردی در دریای سرخ، تنگۀ باب‌المندب و خلیج عدن است.
🔹
این اقدام پس از آن انجام شد که نیروهای دولت یمن عربستان را محاصرۀ دریایی کردند و چند حمله به کشتی‌های مرتبط با ریاض صورت گرفت.
🔹
اما این کار، بار دیگر همان الگوی قدیمی و آشنای عربستان در ساختن ائتلاف‌ها را نشان می‌دهد. بررسی رفتار گذشته ریاض و روش‌های قبلی‌اش در ائتلاف‌سازی، این پرسش اساسی را پیش می‌کشد: آیا این ساختارهای پیشنهادی عربستان واقعاً می‌توانند یک کارایی عملیاتی و ماندگار داشته باشند، یا این اقدام صرفاً یک مانور سیاسی است تا ضعف‌های بنیادی ریاض پوشانده شود و هزینه‌های امنیتی‌اش بر دوش دیگران بیفتد؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/453970" target="_blank">📅 02:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع عراقی از حملۀ پهپادی دوباره به پایگاه‌های تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453969" target="_blank">📅 02:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منابع عراقی: صدای انفجارهای جدید در سلیمانیۀ عراق به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/453968" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0af910028.mp4?token=J2-yjb3zoineTbbWh9b3_PHfaoSsxz7Gbsu4RJvi0-TEJ060-34eWauKpXRFLG5F6RYpfYjCcYVYL_tPVufK3yvqwvr_KSDEqo9JMoDvf0XU7XWrPr1JxTXGVVNiX_2iklSi6NgMtTzBaqdz0UcQSvlZFcBoZO6HCHk1uHnVEecBdGqewWFlxiQv9xZyDVRF0NHUMflhqsO7Es9xHgQ4J-ZFQ82PnCCU3jTYBjlRNHyPNcXRB-GbmU_naPH6WkmD2ZPQH9TZNr0pJ7y18CC7K6w-RZAVcUuUNbrkq6JuVZHEC9OmgwFnmTbwVz51CZOtIZYQfkUunlm7aIpk5bwRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0af910028.mp4?token=J2-yjb3zoineTbbWh9b3_PHfaoSsxz7Gbsu4RJvi0-TEJ060-34eWauKpXRFLG5F6RYpfYjCcYVYL_tPVufK3yvqwvr_KSDEqo9JMoDvf0XU7XWrPr1JxTXGVVNiX_2iklSi6NgMtTzBaqdz0UcQSvlZFcBoZO6HCHk1uHnVEecBdGqewWFlxiQv9xZyDVRF0NHUMflhqsO7Es9xHgQ4J-ZFQ82PnCCU3jTYBjlRNHyPNcXRB-GbmU_naPH6WkmD2ZPQH9TZNr0pJ7y18CC7K6w-RZAVcUuUNbrkq6JuVZHEC9OmgwFnmTbwVz51CZOtIZYQfkUunlm7aIpk5bwRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق  @Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/453967" target="_blank">📅 02:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUlE5C2Ni298xJ2C3Wrevps6qSUygNLFc5C9ra3EFNtGvnTCQOTqMbwyCOyXZioLnFKsSKdvL1qJ2etNAOtewKbHNYmzQSNow_Dmm_w9etjoeABbxsinz5zdyh4mNYQnDTT3lmIPelBGLQM7SfX7jiPM5lqIfx5vp3fUreLZM5DzhhaP4bc3WVhr2VYRZRjGOsOgeMkTkCVS7bX_IcyBnO8UP9hFTV8FLKRnEi1qla--nxnJj23WpvkpSP2JyerrM2pc0EgkLE2EHHrzgbpMnsKs3FynlAX_YDLPstXasd1QUfFctyrVT008xkiR3N8XK8HbkPaeE0ykPphORVO8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: اجازۀ استفاده از خاک و آسمان خود علیه همسایگان را نمی‌دهیم
🔹
نخست‌وزیر و فرماندۀ کل نیروهای مسلح عراق از آمادگی این کشور برای مقابله با هرگونه تهدید علیه کشورهای همسایه خبر داد و دستور تشکیل یک کمیتۀ امنیتی مشترک برای مدیریت چالش‌های پیش‌رو را صادر کرد.
🔹
وی همچنین خواستار تدوین سازوکارهای بازدارنده‌ای شد که از تکرار چنین مواردی یا هرگونه نقض احتمالی در آینده جلوگیری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/453966" target="_blank">📅 02:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=ozKTp1sqPTOZJHyQ2DcK82B_A8lGutE6EBY7wZFy00ZjPhUbiUq7SwiCBhVbvcggBViaNTG75ZBSJrYeZvN4dXs7uVELwbZMj-blXJmwvenZoc3oooauXMTYhg4c08WR0wgIuh6LTwtpBYM56HYCpl2tSr3kJPMdHBbxfg6m5kaAXrb81cCFYKyruq6Bp4-oHJKXgrYn8gSSChR3CCrddleNf9IMmMTyIzYeGVi9Q6i73OlMnFQ7Wkg6ZOHxZtZd4X8XqtLrXlVYXBvSWq6K6ROVJTgDyCRzXtQNLSjFXFxyeL9hyLh9JR2wS1yokTJkzB2b5FNR6xieYhfNJKS5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=ozKTp1sqPTOZJHyQ2DcK82B_A8lGutE6EBY7wZFy00ZjPhUbiUq7SwiCBhVbvcggBViaNTG75ZBSJrYeZvN4dXs7uVELwbZMj-blXJmwvenZoc3oooauXMTYhg4c08WR0wgIuh6LTwtpBYM56HYCpl2tSr3kJPMdHBbxfg6m5kaAXrb81cCFYKyruq6Bp4-oHJKXgrYn8gSSChR3CCrddleNf9IMmMTyIzYeGVi9Q6i73OlMnFQ7Wkg6ZOHxZtZd4X8XqtLrXlVYXBvSWq6K6ROVJTgDyCRzXtQNLSjFXFxyeL9hyLh9JR2wS1yokTJkzB2b5FNR6xieYhfNJKS5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زبانه‌کشیدن شعله‌های آتش از پایگاه‌های تروریست‌های ضدایرانی در سلیمانیۀ عراق  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453965" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/453964" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d49a247c3.mp4?token=F1YXUFZHaFhU-FSI9ecrsMxzgSzXpdsL9NYiERYaCaxMLBZktC4gTt9OmCj4HjjE5Dx-S04XG_kRXSrtIxR2rrXWNjIYOCxSYMfhsvarYIVVzw3Uwcpv0O5zP_50aXQ7fturkca4_adFqgDtOo7jP9hDt-O6ZMU0g0rpGUYQhpxaoIWSvJH0HLaxhXhbMrbiADGUtcuVA2cTlHljW4dnw4rhX3PCWkwFwfoW-ZSCk8s-xHH_tbN8zyUoIJI5Xny-P2sYZk80fx9UYZLSNbHhs-D3W9HAJCa29RbMMULwpF2xSbS27gBqt-GY5uZ3_-qyeUJkDkxUMFPnCYwaY6vSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d49a247c3.mp4?token=F1YXUFZHaFhU-FSI9ecrsMxzgSzXpdsL9NYiERYaCaxMLBZktC4gTt9OmCj4HjjE5Dx-S04XG_kRXSrtIxR2rrXWNjIYOCxSYMfhsvarYIVVzw3Uwcpv0O5zP_50aXQ7fturkca4_adFqgDtOo7jP9hDt-O6ZMU0g0rpGUYQhpxaoIWSvJH0HLaxhXhbMrbiADGUtcuVA2cTlHljW4dnw4rhX3PCWkwFwfoW-ZSCk8s-xHH_tbN8zyUoIJI5Xny-P2sYZk80fx9UYZLSNbHhs-D3W9HAJCa29RbMMULwpF2xSbS27gBqt-GY5uZ3_-qyeUJkDkxUMFPnCYwaY6vSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453963" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
