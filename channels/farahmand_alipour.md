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
<img src="https://cdn4.telesco.pe/file/YoBY86lE0GcKykK2px309nV3NoLxYEzdfrxxdm56EWSc334DmPO1w4baaHGE-VyRHkBlFueUw1j7Eo5hn4JxbW1ngDTETP7leph6pefTajSef-eZUqtsME7poie_p02tLwwSGuHpVvpMbTsG8A80J5gZm9BFjdXXYZbpc56zz-K9iOS83jlpMiFyllpg2Jj6rzHONnO5Tq3geoeAkW__J2nDDqNs1dQsJ7rzBc7r-SF2tAk_54-MJPQI9cMtZwbSs3klhTveQ8YeSrrwkhvKRN1TCr92ogoJvhlIMTgf6CyCsYPT9FnsbHZMoabUNnSSv41C3u0Mh01JGNlwywX1lw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0EuEE9I_NYb5Wiwt4bw5eABv2-y_dSH4r62ajo1ByzhrfJcc7ZBTDhd6SgB3bLtQ_FfI492qW6Cl4wDKGThpUo9KcWV84cqzsdy40LPpejuRBtQ4kOWvHizBYKmPNowuvyfrE5ug7Cat60OXe-kgLJnMPnu8bmhudfMgFNppLgQcBxwyhaZdKzG5Ie1nag9Isirtbmf0_eRd99lmU1uQUpaW5lAYxb_RY3_YeKfEdOiigWMWrBxHGNUafdPHoAobkRITcMxifK5vKYSMyFfW5cgDZCyAWcd-G8B1tCApdXEt2yNCBBt544DM5oLtGrm1hWFADuBfBakLEuHYl3cUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5xNjM2kQW5WL6uR8Z5s6us6NXZCT7bnjSAIRsBahdsGJI7xEya2l7RG_NpbPLCUS4-IlA66-tLQZsZl2t7uFpIw4tHc8FT1C9c8X030d3WR39wk1_8z9dG_g4LZX8j-tPNdkmkiMYtr1kOh-g9eY6h01s3V_e0CRTfQJXEGKXaqfh0Ke9-L8m-IANN7xJnvv_oGJ_uxMfE65MzSz_0UK5jINjKK4_hRpi82DhrFUjy8VZWB1WHcqxPgOpo-cxOzEE_adNvU0Sq6wQsmPk0o753ovGoeFqH5s-MdOm9y3tkKoMf-SgIN-XM4wxxQKyktAuY4wFsHMpLJxc4o9Yy8gMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5xNjM2kQW5WL6uR8Z5s6us6NXZCT7bnjSAIRsBahdsGJI7xEya2l7RG_NpbPLCUS4-IlA66-tLQZsZl2t7uFpIw4tHc8FT1C9c8X030d3WR39wk1_8z9dG_g4LZX8j-tPNdkmkiMYtr1kOh-g9eY6h01s3V_e0CRTfQJXEGKXaqfh0Ke9-L8m-IANN7xJnvv_oGJ_uxMfE65MzSz_0UK5jINjKK4_hRpi82DhrFUjy8VZWB1WHcqxPgOpo-cxOzEE_adNvU0Sq6wQsmPk0o753ovGoeFqH5s-MdOm9y3tkKoMf-SgIN-XM4wxxQKyktAuY4wFsHMpLJxc4o9Yy8gMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DKk84gUOBCp4ziTymW0vuHXHkKpyUy77T9d-irQrCSS9BXhWhKLXNXtIBP92YHUHPf5s_0hNomTH-wQRROTvU_RCbyM6o2_s7L_boQwSPtvj5G-vCcl7mWWF8cU21Pc5gibQTQgs2_Tt4-WmXEaZ1NsqGyF7nonkQOgTO30rFsQGycv19OR9_s4CA9O-Q2GfTEPzLlNFO5lbncsHqaxRRW0XoVvYWlkEcx68VErgbOFSj20GSUT8DtDr5oJQTdDPHoVX6yqngkihBUDgnYSNPVDDHcKJdYY-ZkrxTqXGgXODeW1FhC9Exfqv6shS2M8_C_vaTfxAPzV3_1IahF1UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DKk84gUOBCp4ziTymW0vuHXHkKpyUy77T9d-irQrCSS9BXhWhKLXNXtIBP92YHUHPf5s_0hNomTH-wQRROTvU_RCbyM6o2_s7L_boQwSPtvj5G-vCcl7mWWF8cU21Pc5gibQTQgs2_Tt4-WmXEaZ1NsqGyF7nonkQOgTO30rFsQGycv19OR9_s4CA9O-Q2GfTEPzLlNFO5lbncsHqaxRRW0XoVvYWlkEcx68VErgbOFSj20GSUT8DtDr5oJQTdDPHoVX6yqngkihBUDgnYSNPVDDHcKJdYY-ZkrxTqXGgXODeW1FhC9Exfqv6shS2M8_C_vaTfxAPzV3_1IahF1UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VO9h4aIEBP5SLtBCZIf2wnx75vUeiuet0r5oIriX1HV4uxZ9r3CLg1qbYWSAD6rhxwsyyAj-94Yul6kE1EoG7ch8rxr37mAXfIbI1dr_5W-WVUmYgmvplC6VMGdLaCp7rnv8iY-7qu2COvS4wrNV7m1uCE3H7RQ4KnA3TTqz2T2Yz_sijSbhXnpke0PN3TxmwGdZujrfUge3J7RJG7MdEGl0i0KrfdMU7mulYclYGq9B9MwmA0fovczcJsCVJ3U40a5_JtOBvcFtkAkiMVkqAzGz9pEsE9mhj8OmwwRZtTD6pPz_Ms4jAJ60BbA9RlzDw9LTzGH1BI1yBRt2Am6IvDhbPcPE5_FjBKNEO0y9S2wuThdRNQUdLxSNam5cOMe5Se0iv6PMZ-a2Rfam65_HOR1xkizzrK83rE4wT9q_hM2x6KcjpZHNIZzJEKnn1v7NAZK6CXAs_T31z9vWAwoEKeY7lszzRKytmD8TV9pDbXFf71ns0XrKIetR6nEBswcBhHNaCWh9ttNtnRCHJ2HSHZNO_Y4wUD_mDFP5nMGDQWEq8w78EPtDi8vsNkVgN0v-3st47i7eGf10VmYKvaDdV8oeirax4XbIeIJ3JwY2pbQGcP-_wz6ogpuyneYc4lrv5ix07AchsLdOGPamgDW0Md7ik8nLV6dGtzDNhP2r8ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VO9h4aIEBP5SLtBCZIf2wnx75vUeiuet0r5oIriX1HV4uxZ9r3CLg1qbYWSAD6rhxwsyyAj-94Yul6kE1EoG7ch8rxr37mAXfIbI1dr_5W-WVUmYgmvplC6VMGdLaCp7rnv8iY-7qu2COvS4wrNV7m1uCE3H7RQ4KnA3TTqz2T2Yz_sijSbhXnpke0PN3TxmwGdZujrfUge3J7RJG7MdEGl0i0KrfdMU7mulYclYGq9B9MwmA0fovczcJsCVJ3U40a5_JtOBvcFtkAkiMVkqAzGz9pEsE9mhj8OmwwRZtTD6pPz_Ms4jAJ60BbA9RlzDw9LTzGH1BI1yBRt2Am6IvDhbPcPE5_FjBKNEO0y9S2wuThdRNQUdLxSNam5cOMe5Se0iv6PMZ-a2Rfam65_HOR1xkizzrK83rE4wT9q_hM2x6KcjpZHNIZzJEKnn1v7NAZK6CXAs_T31z9vWAwoEKeY7lszzRKytmD8TV9pDbXFf71ns0XrKIetR6nEBswcBhHNaCWh9ttNtnRCHJ2HSHZNO_Y4wUD_mDFP5nMGDQWEq8w78EPtDi8vsNkVgN0v-3st47i7eGf10VmYKvaDdV8oeirax4XbIeIJ3JwY2pbQGcP-_wz6ogpuyneYc4lrv5ix07AchsLdOGPamgDW0Md7ik8nLV6dGtzDNhP2r8ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=W5JmuwjX4noNtWmsRYpDXG8a87q_5864iUPPwrBZLX5nYbEtnK0qQTV8zvFKXzH2L7bLPvjMbGXDaOPv_Ydu9s7ZdSd4fOPswsj7ZNCbiDNQaZkpDkFUxmb5_xWysTT__0Gq_gQLZf4Mgy2ixuyvQvqbJucy9fkY9XS-IQ1Gb_JClXLqLB98bFnM9aSZFG-CDbQZGpXDUwpfOIj6-Xu2CLb3l5jMHCPJPMQftMBaS4VTyXiGwkfCDmBTV0Lxl8rUkez9MP8pJTp3nHTSiJsWVBrMsh2Bzl-v5YEIYQbi9zxDCHI_MuSjf_VIkUBxINBQb-WkSyZYGf712uO99fV7EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=W5JmuwjX4noNtWmsRYpDXG8a87q_5864iUPPwrBZLX5nYbEtnK0qQTV8zvFKXzH2L7bLPvjMbGXDaOPv_Ydu9s7ZdSd4fOPswsj7ZNCbiDNQaZkpDkFUxmb5_xWysTT__0Gq_gQLZf4Mgy2ixuyvQvqbJucy9fkY9XS-IQ1Gb_JClXLqLB98bFnM9aSZFG-CDbQZGpXDUwpfOIj6-Xu2CLb3l5jMHCPJPMQftMBaS4VTyXiGwkfCDmBTV0Lxl8rUkez9MP8pJTp3nHTSiJsWVBrMsh2Bzl-v5YEIYQbi9zxDCHI_MuSjf_VIkUBxINBQb-WkSyZYGf712uO99fV7EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZUmRoP3hFL3LlRznp25nMjuQZfUnvtHFE2EIhu7uXs5bd82f0GysseEmUhXd3N-eBtfl7unInvctIADNhd4yWo1dTImqD_zdxYmC35FmDQteEWxAeojNgQxt1DtFMXIX6YKLuSEhKU2Z0vq7NLRpKThbaki3mrIGm2Z4zmauoukH41TqEja7gyV5ZQy9dAVQTEoPAo-FRTWzrj6lo5i0aiKzvSuZShmyUULfwsN7LZOAh_cd8-KpajzKyWlBRIT0dE5M87vs9I27JxfDtuG5nE0vM7xkp4Ev2_KEUymjixjW8LEvjahzHSlEHShbVfUgCh-R-Sna55kxk132pynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=YDQ2U3SeMQTDsiXXI0xCvl5agGkFDo6w9J3Zvrp_riyBd0xQbNkc3WlAv1KPR6VT40v7-0zv3kaC4rQy8SA_kScl90o68t_3C-SYLk97s7OD31wYtw7kWydzSB0vCM1FM3qBjzB3xFyJEabu9kIQABLq_RpjEqDoHiJ5AL4Bp_JebiP8FxdPk_WvKrfy-Vsq7FbUYFIXEw-jIENOGzel9e3Cgs6UDC_lXsly3U-x_4iM6IYIJAZ7YeWo3HT_PTNWpJbvqxBCrCIdYZgUc67ZlUO6SXGcx_ulSMSAf8ZFpR3WYgKzc6i-EjNjicBhh18pVYYwRF4akkmdYCJrCM25ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=YDQ2U3SeMQTDsiXXI0xCvl5agGkFDo6w9J3Zvrp_riyBd0xQbNkc3WlAv1KPR6VT40v7-0zv3kaC4rQy8SA_kScl90o68t_3C-SYLk97s7OD31wYtw7kWydzSB0vCM1FM3qBjzB3xFyJEabu9kIQABLq_RpjEqDoHiJ5AL4Bp_JebiP8FxdPk_WvKrfy-Vsq7FbUYFIXEw-jIENOGzel9e3Cgs6UDC_lXsly3U-x_4iM6IYIJAZ7YeWo3HT_PTNWpJbvqxBCrCIdYZgUc67ZlUO6SXGcx_ulSMSAf8ZFpR3WYgKzc6i-EjNjicBhh18pVYYwRF4akkmdYCJrCM25ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=M6oTg1m4Ba-_FLb6vilE2Io4EhnpA3wILRgEBOjRC_qF9vWTUl5FF46kJvWmeOQ9YoQHAlRTwWKj9pAfeGnNxYPVEahf4Ba3WaBO7me_uax1ZlhiCaEd5R5DllpzVQiy4yNcZX69L2yUMBT6CCE4A3VASv9bHqmF8Ofpg8MiJ0LwXdqEtWtiDf60v-pWs7bAWZgsSFijPQn9X3W9o-4z0x10QpX55214zFW78VmQ_xlMWNQxu-SyprhaeKCjEH4JjU0I84-YVn5GBqQ47lH4hkMTYC1szwXUKSziQj1sEGJnP89rVkxUL4FVwRWB73fXu92Ph7iwVR601QC0X8TktCbo4gZWOgJtuyyeH6HP4rl2bJdz8TdWkGm4dcm6Yf5S7CrHnSKFyL_cxr4mgqG2khBxlRoUdr_g346fMxquGVf0PVYNO3KZkOokrtPY2K3a7-josNBGBI7puGQRgF-kql0mJaZ9RhvlEG8M4_3IQpYn7n960BorTiiQO9_vaJc4tG7Nbl5KFcB7cVNp1EIN2ceP0uBWAGBd6eNr7x6SGT48RORUBBo8QsgMEsHzS-gNelbw9C99Gb08sqFgU1qRLZldYhgl44f1pe9_12P2LOlIW8e3HWoQG8SWtOOGJUPRrGQlICUjtVKFv3KAf-zMxOt3ZuM_nYiVvBEGivSlGmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=M6oTg1m4Ba-_FLb6vilE2Io4EhnpA3wILRgEBOjRC_qF9vWTUl5FF46kJvWmeOQ9YoQHAlRTwWKj9pAfeGnNxYPVEahf4Ba3WaBO7me_uax1ZlhiCaEd5R5DllpzVQiy4yNcZX69L2yUMBT6CCE4A3VASv9bHqmF8Ofpg8MiJ0LwXdqEtWtiDf60v-pWs7bAWZgsSFijPQn9X3W9o-4z0x10QpX55214zFW78VmQ_xlMWNQxu-SyprhaeKCjEH4JjU0I84-YVn5GBqQ47lH4hkMTYC1szwXUKSziQj1sEGJnP89rVkxUL4FVwRWB73fXu92Ph7iwVR601QC0X8TktCbo4gZWOgJtuyyeH6HP4rl2bJdz8TdWkGm4dcm6Yf5S7CrHnSKFyL_cxr4mgqG2khBxlRoUdr_g346fMxquGVf0PVYNO3KZkOokrtPY2K3a7-josNBGBI7puGQRgF-kql0mJaZ9RhvlEG8M4_3IQpYn7n960BorTiiQO9_vaJc4tG7Nbl5KFcB7cVNp1EIN2ceP0uBWAGBd6eNr7x6SGT48RORUBBo8QsgMEsHzS-gNelbw9C99Gb08sqFgU1qRLZldYhgl44f1pe9_12P2LOlIW8e3HWoQG8SWtOOGJUPRrGQlICUjtVKFv3KAf-zMxOt3ZuM_nYiVvBEGivSlGmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKrKbCqdLLJyvGUSmzC3hfoiZLxRZ2B8Vp05WS1d4JfKg8ZYv7dPLHUBc82H22Rh53Ze0b_44oP6OpC2xpse4gjxs_60bWltLVP5fCp7XtDjPmCJdmAwPhKL2PtTGwrVqIxthcaK4V_Z8YDKw2RCaWq9mWnmKPbT32tOi3_y1Wld6pgpCrrhVnDD7gK0IxIEVn8jAgghu8gjg9Cxfem55yneVpkocKype0ezE7IoCMJACdv9bl-NSphDJ-a0kv9t7pwR4FfJzlzkjaNtAet4pDJ2U--bS-RXPFbhd6Y3yzsiSz5Te7lWDbucLlYfXOOqJHjAgx7gguFWSmTScnKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=FRzXQhT8-EY7hW1X2KPoZT0ohL5UkRLvf5s5KFo6e6Dv2hoyRAFLWK6fYntGgd8MQmmqHTblWMU3ONs92msiobChIxkND7obMj-dXRoY_3LEUMwGFOrNxApptKmmWHM9_A1zm1hWtbJRgB1XkUdkydJnYe8lFPU9n_gA508Mo8hf8h4OiBpl9DbpKfcP4ylLo-PP0D4xAsJrwuCv-j5PbFumnKAq6VDz5DiCLoyLxdxw3djr4sxFdOrAijTqCKmgXNNqc3aq5glQJhbc2yXW7_wsCZJ_6pC7upCjpUuHg-vKN0a5EnrqJhfzZRVh5ul2jAjhcfwQ0YUo3nzYvUOedQlkQhAQ3EA22gzYDHkihYGFmaOv9l3P952fBM341415lG23PdA2ClFxLbDk14il6L5aM__QmVtG4EusCMxtQxf_vGNyC2IKrnFHqegQ2irUBqgbxnrsxIJSXw3pnCgJGLrG4zdc8_pz2Tp44bVviFIEeCaFFV4CPAiQ10a9XK_bebNKkWrUH3uXKZEqsusUcbV5GdM8xF7W-qUKdDbkOP34kcXbwPDzJkRoRYmvtzK0yCo8IfvZsPmJGM6VTvDvE1Kpm0prafY-gxWJxHRtPKLiikmVWAAH6I2M6d9JQfTW8feIYvkzI_BkNrh804kSvg5sDxHSIL9ANKW5IFJOBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=FRzXQhT8-EY7hW1X2KPoZT0ohL5UkRLvf5s5KFo6e6Dv2hoyRAFLWK6fYntGgd8MQmmqHTblWMU3ONs92msiobChIxkND7obMj-dXRoY_3LEUMwGFOrNxApptKmmWHM9_A1zm1hWtbJRgB1XkUdkydJnYe8lFPU9n_gA508Mo8hf8h4OiBpl9DbpKfcP4ylLo-PP0D4xAsJrwuCv-j5PbFumnKAq6VDz5DiCLoyLxdxw3djr4sxFdOrAijTqCKmgXNNqc3aq5glQJhbc2yXW7_wsCZJ_6pC7upCjpUuHg-vKN0a5EnrqJhfzZRVh5ul2jAjhcfwQ0YUo3nzYvUOedQlkQhAQ3EA22gzYDHkihYGFmaOv9l3P952fBM341415lG23PdA2ClFxLbDk14il6L5aM__QmVtG4EusCMxtQxf_vGNyC2IKrnFHqegQ2irUBqgbxnrsxIJSXw3pnCgJGLrG4zdc8_pz2Tp44bVviFIEeCaFFV4CPAiQ10a9XK_bebNKkWrUH3uXKZEqsusUcbV5GdM8xF7W-qUKdDbkOP34kcXbwPDzJkRoRYmvtzK0yCo8IfvZsPmJGM6VTvDvE1Kpm0prafY-gxWJxHRtPKLiikmVWAAH6I2M6d9JQfTW8feIYvkzI_BkNrh804kSvg5sDxHSIL9ANKW5IFJOBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=mZT6LFdn4Id8_FIlhi-pt4M3AuxU7BvWA2d2mOUIWGUVOt6yzrFtoNZJhRqL1sr2_6758h5hvw6t266j9Q301XEzfTOgvg-K5UCMbiuGMVlW1YDVxONLbERdSNU64AkQBVHALc2mfsvMpKeEusb2IoDCnWuWx_DA_iry9nW_e-wkjjpw103e7tvDV9pp-9Ahr3C1qpn0nFrFeF_NxrarLK_ry9HpKP60Yb9sKrKetbWC5PUejKCnAmNXbvgeg5l4xcwQHMi1B4hr2P3rNXJiqNJxXMCiLiIBA6SUiRnll0_UYwirney4fG6204wNcgAf1iGJh4qRwn7_v0lVsnOgvKcglAaGHhrP4hahrUaJbIBe5RRi22gFw68-N5cMwb0N-YT7td_7qT6qzC771bXWO0kVmmxHeOPqwESMuokj-Fv_bIQCAJCIsmA4YX_HTlRhIOC9_KktO0JEUsNoJ3e0m1f2Hk3n2V0z9OW1twJulIYm4mlB3FO1wH7qsTcQbgQ54CnVM7JsGypcnGdwnr-LtVJgcJ3JVSgNjGa-MqSOnrjciC_LayIESLVT5sMiNLg67kN0hTm_3RSyBpI-0AdMYVyx5s0_QTOu-ZqrTF60U0-wzYlN-1D8wXAL3ZO6C4ESIoJafc0aPBXDe1QdbaPEsIiEBgHkaAJj5_bOA4EyH-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=mZT6LFdn4Id8_FIlhi-pt4M3AuxU7BvWA2d2mOUIWGUVOt6yzrFtoNZJhRqL1sr2_6758h5hvw6t266j9Q301XEzfTOgvg-K5UCMbiuGMVlW1YDVxONLbERdSNU64AkQBVHALc2mfsvMpKeEusb2IoDCnWuWx_DA_iry9nW_e-wkjjpw103e7tvDV9pp-9Ahr3C1qpn0nFrFeF_NxrarLK_ry9HpKP60Yb9sKrKetbWC5PUejKCnAmNXbvgeg5l4xcwQHMi1B4hr2P3rNXJiqNJxXMCiLiIBA6SUiRnll0_UYwirney4fG6204wNcgAf1iGJh4qRwn7_v0lVsnOgvKcglAaGHhrP4hahrUaJbIBe5RRi22gFw68-N5cMwb0N-YT7td_7qT6qzC771bXWO0kVmmxHeOPqwESMuokj-Fv_bIQCAJCIsmA4YX_HTlRhIOC9_KktO0JEUsNoJ3e0m1f2Hk3n2V0z9OW1twJulIYm4mlB3FO1wH7qsTcQbgQ54CnVM7JsGypcnGdwnr-LtVJgcJ3JVSgNjGa-MqSOnrjciC_LayIESLVT5sMiNLg67kN0hTm_3RSyBpI-0AdMYVyx5s0_QTOu-ZqrTF60U0-wzYlN-1D8wXAL3ZO6C4ESIoJafc0aPBXDe1QdbaPEsIiEBgHkaAJj5_bOA4EyH-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=DmDiKhNdQ5J-h7690cR2lpulN9zLbQt4vFMgAj4W8eqZrzJcFVYvg3lJfJUloGllzjGMGL4DXdEk7CWdAK8oY71wFa4Otm5OG2A57UHKFGONmuj-dAbUl5OC_9v9lhWvj8uMtgv5zYBRwHvqCdhK9Ts4A9kF-GUN9yWQnaaIZntw8WvhLLjOF-0E63JYB5p_j0mAAaB1660LMRuQK99CJt6W7KBvMmNkLtoR7f1TS8C99kJNH9vr_IWbEiVcX71zeT-dms8TXW77i5wx86g53TSBIyjADaI5UKxK3eLBBs7orVTNIy2lL5aoRmp0EnkQmPj9yrbjGMCTD4mMcLjHLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=DmDiKhNdQ5J-h7690cR2lpulN9zLbQt4vFMgAj4W8eqZrzJcFVYvg3lJfJUloGllzjGMGL4DXdEk7CWdAK8oY71wFa4Otm5OG2A57UHKFGONmuj-dAbUl5OC_9v9lhWvj8uMtgv5zYBRwHvqCdhK9Ts4A9kF-GUN9yWQnaaIZntw8WvhLLjOF-0E63JYB5p_j0mAAaB1660LMRuQK99CJt6W7KBvMmNkLtoR7f1TS8C99kJNH9vr_IWbEiVcX71zeT-dms8TXW77i5wx86g53TSBIyjADaI5UKxK3eLBBs7orVTNIy2lL5aoRmp0EnkQmPj9yrbjGMCTD4mMcLjHLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AsnuTdXreW6WDLD-IO_HQSnnc40QDvjvT5G33AdZ3TEqtIxsdoR4Tgk0EVDSAYePdsKFpEQu6KkiN8FgidpML41jnf2rScYgNYDJ1zPcC8xQlPcuV_-T01nsylsMfY9vpZqs_Oj_yxpe7qNYja3BtE2fS__gcrTNJTk2Iobn3qDVrXmMXt0L8m9jW1B3EUeJcAClWI1EVSQz_pCyTHiy8uOrbS8Vd_FQd12BNKK7kH6D7y9OHYjvv4Vwl2gflsTX-UUqkLJtDpGCNW-fiGTxNYLF4-wMbclibWDT5psucrXfoy79fDIEG8-mspGElshFJ9yrnnHxN4CXeNfFlbahnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AsnuTdXreW6WDLD-IO_HQSnnc40QDvjvT5G33AdZ3TEqtIxsdoR4Tgk0EVDSAYePdsKFpEQu6KkiN8FgidpML41jnf2rScYgNYDJ1zPcC8xQlPcuV_-T01nsylsMfY9vpZqs_Oj_yxpe7qNYja3BtE2fS__gcrTNJTk2Iobn3qDVrXmMXt0L8m9jW1B3EUeJcAClWI1EVSQz_pCyTHiy8uOrbS8Vd_FQd12BNKK7kH6D7y9OHYjvv4Vwl2gflsTX-UUqkLJtDpGCNW-fiGTxNYLF4-wMbclibWDT5psucrXfoy79fDIEG8-mspGElshFJ9yrnnHxN4CXeNfFlbahnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=YHkHTShkakPLuWbYM60yDiNlwg-eTLZj7wkPqKapnseX-iLQeJMQ6SbB1sbi5jcO8IqKITF-SfZRyKhp7A6t0V_zsfFe2MTG5ZZ0opjyLVxjePpho_-g49M9S5NUo5TZPzMFrS_CF5VBdsbF-naHXpHwUGcA9Tscyz4Z42juf7cPbPu3v04Caralo2BLQJtV1nhZVM-0QU09cy1mLIkMVgDlTNMOmAeIyYssY0j48sHjmSi5iweIFYVUXp2Ylb2he7WnGNnyA8uImDHZlCKW_2TN1HfxBL-gyZK_7q--ZihoB0tReJdvHdM9diTeDUcsrhF8dI5WmNQ--M8HzEMm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=YHkHTShkakPLuWbYM60yDiNlwg-eTLZj7wkPqKapnseX-iLQeJMQ6SbB1sbi5jcO8IqKITF-SfZRyKhp7A6t0V_zsfFe2MTG5ZZ0opjyLVxjePpho_-g49M9S5NUo5TZPzMFrS_CF5VBdsbF-naHXpHwUGcA9Tscyz4Z42juf7cPbPu3v04Caralo2BLQJtV1nhZVM-0QU09cy1mLIkMVgDlTNMOmAeIyYssY0j48sHjmSi5iweIFYVUXp2Ylb2he7WnGNnyA8uImDHZlCKW_2TN1HfxBL-gyZK_7q--ZihoB0tReJdvHdM9diTeDUcsrhF8dI5WmNQ--M8HzEMm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hK5IcXipBhTUvysbRawxXIcCsAUeLD10VMwxH7IJpD1_EfIWYxEAf97k-uB3hgSELR-z_qxTiTEO01_h0Hl08LlB4yiU0FqYyT7eJsZVC5-8gCOGZxHXjt3nyzWWb2cASINK7UGjfjQOLF72y4ohxG7Lln4X4EgS3-aC7oe82iDBdR5PAsQKpOvWnllPpuvKilDF9qG76-VQZ65nir3AEmX0DNBzEhel44-mb3WC9bdrmdsJ4M5FWas-vZam0Du4lb-rlDaU2oUmHyCP2qRRN929RLzvH4AOvCUAIgh8H0Y4AqUSOuwzL61KvNZ72k2ujKTZ8ASWRbQhhAnRtJsueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=hK5IcXipBhTUvysbRawxXIcCsAUeLD10VMwxH7IJpD1_EfIWYxEAf97k-uB3hgSELR-z_qxTiTEO01_h0Hl08LlB4yiU0FqYyT7eJsZVC5-8gCOGZxHXjt3nyzWWb2cASINK7UGjfjQOLF72y4ohxG7Lln4X4EgS3-aC7oe82iDBdR5PAsQKpOvWnllPpuvKilDF9qG76-VQZ65nir3AEmX0DNBzEhel44-mb3WC9bdrmdsJ4M5FWas-vZam0Du4lb-rlDaU2oUmHyCP2qRRN929RLzvH4AOvCUAIgh8H0Y4AqUSOuwzL61KvNZ72k2ujKTZ8ASWRbQhhAnRtJsueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=e9y_wYmquuuwrTFFnMdpMPid3mZxNKawI1KqtYNEqPbJ26VnB8eDo7e5MvskuwknpYF4wGmXO5ouyx22JvG1MdnPh_CnzZcFdSzYwNJtp3zFHblUcLVl2t5E-T2wdsx74X7ggf7gpwX6JIEq5rdv6UB8QA5NQN8t6Iac3OJkPhvS5ZsZaDD7NXYXkscZ_80vaHkJXu3kXAwC2bDremSMz0nmzbPla9r1rJshz4JQ0u6IuefW8BTUUoduq91AxvsK5YyFcSfgIbgEsGc_FczmJtgLfucEnzAimvabALda7-2emVFGhILkqVfE2fjbaWkpcaR_1KPAbEOzx0FCtisV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=e9y_wYmquuuwrTFFnMdpMPid3mZxNKawI1KqtYNEqPbJ26VnB8eDo7e5MvskuwknpYF4wGmXO5ouyx22JvG1MdnPh_CnzZcFdSzYwNJtp3zFHblUcLVl2t5E-T2wdsx74X7ggf7gpwX6JIEq5rdv6UB8QA5NQN8t6Iac3OJkPhvS5ZsZaDD7NXYXkscZ_80vaHkJXu3kXAwC2bDremSMz0nmzbPla9r1rJshz4JQ0u6IuefW8BTUUoduq91AxvsK5YyFcSfgIbgEsGc_FczmJtgLfucEnzAimvabALda7-2emVFGhILkqVfE2fjbaWkpcaR_1KPAbEOzx0FCtisV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Jz7sOiSsYmSLY0A694fOBNrW4BAxPirZZGzWs2GTLtSlTjc2UQ2Qjsvmfqw2JUPJLu2Uh_wdsgVyfsxSgMa8UYsCwuef5HmCOVF5uUen8-9jlacmv7jwxBBVxr75xg_kJd18FcKMEf0UUhsIlOsKTUjl_zvb-TZ-ripbM_kkgjOvjAdVNTZe8B2vjbSvpbl-Tegplzp3giuc33tkUsX0Y2mav2Nikxpo_u24pDtQJkF4FvLmQMl7QCvOioxDP7MHqvcejVQY0gutNnbnghbJW77VRkboTI1AKPoNdwvyjUq5AWmxhEFcah7kMQuCpi3svkosgyXKiqVtb0g63mrvCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Jz7sOiSsYmSLY0A694fOBNrW4BAxPirZZGzWs2GTLtSlTjc2UQ2Qjsvmfqw2JUPJLu2Uh_wdsgVyfsxSgMa8UYsCwuef5HmCOVF5uUen8-9jlacmv7jwxBBVxr75xg_kJd18FcKMEf0UUhsIlOsKTUjl_zvb-TZ-ripbM_kkgjOvjAdVNTZe8B2vjbSvpbl-Tegplzp3giuc33tkUsX0Y2mav2Nikxpo_u24pDtQJkF4FvLmQMl7QCvOioxDP7MHqvcejVQY0gutNnbnghbJW77VRkboTI1AKPoNdwvyjUq5AWmxhEFcah7kMQuCpi3svkosgyXKiqVtb0g63mrvCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=b_u5HhdgRM7uvmevaD0z0pZb5pvA4nEFu10MQe-AvPAY10l7JBkQ3EnlxQi-kZBbs0mY6mJyMfylIfpSDO2wayO1sPFq0o10CyLX099NvP-fnqPAlB088Ls8zj2E0MAM-64ASFY6ium99-GgL5yGuRYKnVUZHJr5IA1Z7B-bP0yYlurZ-MmYZZx4hLqVBG269jIBva46qtyID9CyrIbZP7qMKU1UVr2-PEeqPnbgAJLwbtUXK1tQDEoaSRUkgHGv-K92udwkf2S_2tUBL8_NYOfWqrg5GfWFWFlvvJaLHKlyLNI6vQgwYY1zGX8JQ-xzl5Gc2v2uaidTHQ3lnKtmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=b_u5HhdgRM7uvmevaD0z0pZb5pvA4nEFu10MQe-AvPAY10l7JBkQ3EnlxQi-kZBbs0mY6mJyMfylIfpSDO2wayO1sPFq0o10CyLX099NvP-fnqPAlB088Ls8zj2E0MAM-64ASFY6ium99-GgL5yGuRYKnVUZHJr5IA1Z7B-bP0yYlurZ-MmYZZx4hLqVBG269jIBva46qtyID9CyrIbZP7qMKU1UVr2-PEeqPnbgAJLwbtUXK1tQDEoaSRUkgHGv-K92udwkf2S_2tUBL8_NYOfWqrg5GfWFWFlvvJaLHKlyLNI6vQgwYY1zGX8JQ-xzl5Gc2v2uaidTHQ3lnKtmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q58gzDIWbgKyYWlzeBDYMoW9OTs1CS6li7Cuc_8tDg8QxF4f6YEnymohQuy2olGBtGvu4sqdSjwVI5i99wcJ3AHv48M0bm3UGvf2IOBWKyrKIoioUhhacb_GmYkPTdmZ3Cbi4N4rMjVOezQ7Efj9ZFpNRaj-Emknp9nPHjTslghMDhn3DxFsiG14kLKa2u3V9f3Y9RaJSyvKKanl3EVCGGm31FGK-wvd2jehmUhjLJw1GfaqXvvy75iulVbNiDA1S4DhYi6NOK0rA_GvbokE_3hDSeSjDthsUzuH8Z1_Gah5UZePGHuLNIAG5JMU8FMqTx0r6e8lHoLuW-OAf39eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=A91txGhidm_a-2lXSeu1S-ILBXHc_MqHcuhGtJo0quhb2gjuaMzs2Y_CLXzsrK0CimDpvL04NcEvoVcDWFid9yNkpZw-bacDhw3BfnYCamaG3rExbUaA_2ka-bKRz8Ixm5Rivf4Ogc-Gw4NvOkEy9G3_xRH5RsXANwGWexYlXjHi74Es95zn5IsKczqa5zijXwy9nWQXdoeKC3YbqDIm0sPxt-9uQofCs2ZLiJZUF5YhrKw3MMXrR_mzKQn-S-ijGpFD0keLT734CPum2JF_RVvmjfy6JnOBH30lVgG_Aebo_5LaJSysn08zsL352xthSqJBCHmGnxkrPcWKui3hVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=A91txGhidm_a-2lXSeu1S-ILBXHc_MqHcuhGtJo0quhb2gjuaMzs2Y_CLXzsrK0CimDpvL04NcEvoVcDWFid9yNkpZw-bacDhw3BfnYCamaG3rExbUaA_2ka-bKRz8Ixm5Rivf4Ogc-Gw4NvOkEy9G3_xRH5RsXANwGWexYlXjHi74Es95zn5IsKczqa5zijXwy9nWQXdoeKC3YbqDIm0sPxt-9uQofCs2ZLiJZUF5YhrKw3MMXrR_mzKQn-S-ijGpFD0keLT734CPum2JF_RVvmjfy6JnOBH30lVgG_Aebo_5LaJSysn08zsL352xthSqJBCHmGnxkrPcWKui3hVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GlocROfGEIBNjgc57T2b2bsvxSOPqr8k2zMUubLj2Q0d8_0caTSZQqXrgCGIP6UvgRjdA3WyGkV0nZF6SJ-nNNqdBC4xRCN2m8N0tTeoberjPdcRyWB3y4qBMobPVjotcE2FYLrUTLxhF_udMqzmsOzE2gTjzZ8SytLSEAAkjbTKT9TLWY_QnXyHc_lWxjLm4nx2Y9uIEuw-_pimoJ6RB5CadxI6f7eY51jMK-n-uGaxriMm381crSdFONnTWS-l6DUIBDSVVgV9Vnkuno3DlMgfQTOIdP2FMOYEBfGgME8QGb6_kWGokrgDXnZMDz7KEXAM7mRsycQ7unNQLdTANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GlocROfGEIBNjgc57T2b2bsvxSOPqr8k2zMUubLj2Q0d8_0caTSZQqXrgCGIP6UvgRjdA3WyGkV0nZF6SJ-nNNqdBC4xRCN2m8N0tTeoberjPdcRyWB3y4qBMobPVjotcE2FYLrUTLxhF_udMqzmsOzE2gTjzZ8SytLSEAAkjbTKT9TLWY_QnXyHc_lWxjLm4nx2Y9uIEuw-_pimoJ6RB5CadxI6f7eY51jMK-n-uGaxriMm381crSdFONnTWS-l6DUIBDSVVgV9Vnkuno3DlMgfQTOIdP2FMOYEBfGgME8QGb6_kWGokrgDXnZMDz7KEXAM7mRsycQ7unNQLdTANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vu9A0bW7PiQpLweSQUkTgt6zpI7w-t1SLAhTQQjtVyVrJQ7dQR5mctlkB5s0SjPikibiZxMK197AmFGOJhHvlZji0pi2YvjM-6KI_1WLYXyfwrT3pRqUUVBOokxqBeL1i5RhOL7M__Bt5XgGxqTpocZsxzvPrdk2K6YQocRyl-rRr4KYUhHPB0UVwhQOh6xeyFtOcnJ-9oxxBNpElnGgiYnWWJXAQrpGVvg0pyahjlap79-C57mTD4OLl4m45S85E2uY48WUmkJAjDcajtTajyyPhENwkS3gGEnLRQ_mWVuDLRtZWFEiWxqAHvoVnLjyx2lqtPJQT5vK8kjowJPH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vu9A0bW7PiQpLweSQUkTgt6zpI7w-t1SLAhTQQjtVyVrJQ7dQR5mctlkB5s0SjPikibiZxMK197AmFGOJhHvlZji0pi2YvjM-6KI_1WLYXyfwrT3pRqUUVBOokxqBeL1i5RhOL7M__Bt5XgGxqTpocZsxzvPrdk2K6YQocRyl-rRr4KYUhHPB0UVwhQOh6xeyFtOcnJ-9oxxBNpElnGgiYnWWJXAQrpGVvg0pyahjlap79-C57mTD4OLl4m45S85E2uY48WUmkJAjDcajtTajyyPhENwkS3gGEnLRQ_mWVuDLRtZWFEiWxqAHvoVnLjyx2lqtPJQT5vK8kjowJPH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=NDRmSNrShKtjzsHTPJqXSqoBxNBlEl8gLcLnSsQLyHBdLP4MuAwmUgNzyzkb_ajSyArkMkEc3gFQTx3cIq8DqI8Qyf17iEPjujVm_0lYOm7jHmEGUMrmFf9skmGs2V-64cIF6One_jOI1sCqVw4PlPndOPo0XzoXz9FFVp0IJMeEBM0oYqeDGDoUnvGCmEHsRzNaKJ0SEkdOJGFtZv5YC0zZbmvoNzkH4p1R5gsP1T1P9cGGx_ps-JYzKS-6OS_-XTLM_zzMNyhJdiPemZAWEKY_-gVjKuX_kOGOXBuchGFuyl_ze8cmYDwP4sKSQzrzwmFbZSErxxP4EhI_C7D4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=NDRmSNrShKtjzsHTPJqXSqoBxNBlEl8gLcLnSsQLyHBdLP4MuAwmUgNzyzkb_ajSyArkMkEc3gFQTx3cIq8DqI8Qyf17iEPjujVm_0lYOm7jHmEGUMrmFf9skmGs2V-64cIF6One_jOI1sCqVw4PlPndOPo0XzoXz9FFVp0IJMeEBM0oYqeDGDoUnvGCmEHsRzNaKJ0SEkdOJGFtZv5YC0zZbmvoNzkH4p1R5gsP1T1P9cGGx_ps-JYzKS-6OS_-XTLM_zzMNyhJdiPemZAWEKY_-gVjKuX_kOGOXBuchGFuyl_ze8cmYDwP4sKSQzrzwmFbZSErxxP4EhI_C7D4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwulTyMKt7tm1d1XDy6oowfBerbwFHqozAWEmG8e13qH4X7K7CrgAQg9vk44lJEwdZ6x8keCrvL_9RGgShP4UgloZlJmd1jKIdjzfvXQMa6Ujd_13Utbi479MtP5u3uhmLyQPmYbD68nXonp_1853MJBfXTYj5umbbOFfamYBPKbVZEKVQNem58Nd-gsn4Y3IXiQ4wrx_OWBxYGEs_7jyF0Q8xwC3IiyrpV3V8EI3deeNnZ7ieUi149D6oBmTeYwVwCFODJ_Wv9JwExOmrGJiZfiLs4qiKDWMlYvi2W7BtAbHo4uz5dtciQ7HG01GZdJGjCTWT_e6tOzrDaFaXT0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=kpD6wHcV3iAhOofAm2SHBupapH5cROM7apEy7wgTsJRauuWgIKn4txpzzINTmbbaNtz4MdKwhVGd3AAzHQPjjKnLj5ljMezwBAqInnllZeEnsyWdP8H8n9Q6YFIhhom8iqHimZTTFM6qiw65PS8bSkr8qRMiIT8URixAZqX92vCnWR1tRkvzQosbVWztF_9cQGEMYJbfTwnE17DwB5mNFd5-GfnfB52juKzcTmYDyUp8Dh1TPfNMxuB0CmZNnODCNaa6jygVrxALjGx2mvmdNhHw_k6Y7eoSGi13KOnT2UdmKz0gHWXc4cKnsb6lwcDpDydgi-FxJBwTtDn5uEyJjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=kpD6wHcV3iAhOofAm2SHBupapH5cROM7apEy7wgTsJRauuWgIKn4txpzzINTmbbaNtz4MdKwhVGd3AAzHQPjjKnLj5ljMezwBAqInnllZeEnsyWdP8H8n9Q6YFIhhom8iqHimZTTFM6qiw65PS8bSkr8qRMiIT8URixAZqX92vCnWR1tRkvzQosbVWztF_9cQGEMYJbfTwnE17DwB5mNFd5-GfnfB52juKzcTmYDyUp8Dh1TPfNMxuB0CmZNnODCNaa6jygVrxALjGx2mvmdNhHw_k6Y7eoSGi13KOnT2UdmKz0gHWXc4cKnsb6lwcDpDydgi-FxJBwTtDn5uEyJjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=snQqjyk88bUv6QjlI4HK_fyvbFLGhwUhLe5jvEB7mx4X1TMgrVo5WHHgwqdRS2JfkdPf788XvlFjr5CVsmQdZPyxcK6d2amd5r0o5VHYaaxAmGD8xW26okU4CUB6v3CfJXGmNOZG4ux346HIflWlr7OqNdgPQiiKT1LAuqj_QY-Y7bGzIlRYPyWJI4vrOHCSnYqVjvRtkk_zpNs2pkgd9xY_VRo-FKt1nmKiyoSxu_3fMq76Df6ntqpnjL92zLwhjOtjVExKxaGlgt-oVFOiUnV877jU3cXewt2_anCiBSZ-tewacJgdxJfJrJcMKXw0QadBgAf_yR7uy4KnxkjOLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=snQqjyk88bUv6QjlI4HK_fyvbFLGhwUhLe5jvEB7mx4X1TMgrVo5WHHgwqdRS2JfkdPf788XvlFjr5CVsmQdZPyxcK6d2amd5r0o5VHYaaxAmGD8xW26okU4CUB6v3CfJXGmNOZG4ux346HIflWlr7OqNdgPQiiKT1LAuqj_QY-Y7bGzIlRYPyWJI4vrOHCSnYqVjvRtkk_zpNs2pkgd9xY_VRo-FKt1nmKiyoSxu_3fMq76Df6ntqpnjL92zLwhjOtjVExKxaGlgt-oVFOiUnV877jU3cXewt2_anCiBSZ-tewacJgdxJfJrJcMKXw0QadBgAf_yR7uy4KnxkjOLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltf37hsx0OWGYOKz2hHs8HG_iNNF75hqI8Kj0oQIGFIBQOv2G7eJLR-oYLb0TX8ZFESxC_gMArOY0DbWuHq77bv9-HLY12-xCoXZ9WvZyR43UStqRaXKQsLTkS0qktBY2uGGKj-qY8gJcLzn-gxSUt2x6ob3l0KNs7DFRkcuOzAr8c_5m046lHRrY041Tl8fnj37JAs61b09AhFol61eHq5G5yXbkDIF4zQAliKWmdrSs_zLMQfimZdBEVTWiC-S89WAKNYFZ2rzU8QnNyAPWUL-Xk3-wLTtwTEpvyKoewXyJKGF1bkE7a_XEyaWqwQSTKHMnC3Mn2j-3qsnjPIZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dq--F_Z-JyFrzB6RF2ipjfmYvS7bDBHwI0KoiTyvYGVzWocdWuLpS5NqA7GGb34wWVMoWaAfLKHXI51VOPcxRwc2HyF1PoX0POdwUbpgcXZwj2ICjuzxaGzTYNJ8V3dcIj5hu-NQ5J-i2z4RGl9FjXo5HHE3Ci-jMyx7wV_efWExOcsORwboMeKBg_7zKdH4fdR5848Cx73NQ6R2vsPlrEKOwihxtVcQAgr4zUJe3K0lArk-94B3htXbmYKHTLXLfxGT54VF3ib5wvf493NcqqIRSiZh6VhUw2GWVwkrRoLj8lmNUh6aXvenvdYo089GC4Ll6cC2mKrgCW8KJ2eGbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=smS95qDi09Ib2QeRoKL3obg5FQslG_EKMcFMfG2kSIrnhlzo1JYoOO4ND0wfSSGQEH2iQht98xV4-sEx6SWFRmPKgp9WI8vpLN_-dfq9zRe9MVRQenpnhM8diDeZYEUVUx9ujFkEMfJ6goNvEw6XNeGyXlXbwcV7pJpUHvFZUI9yIqCxZGV86ujcM-fj9_Sjyp3XJZzErmG5M8wNL2nTLkpQuLANeTYJFsJaNWcZMYuBWfWR7Vl4llOXwr6q__NCxRi4JG9vpmb9lbJFRSmyljqH3C8yMzL3C-6BrDRv_pS4BRULW8Sx3FFxMUBcuQKR8Pj7fbTQhwKxuBoIw4MOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=smS95qDi09Ib2QeRoKL3obg5FQslG_EKMcFMfG2kSIrnhlzo1JYoOO4ND0wfSSGQEH2iQht98xV4-sEx6SWFRmPKgp9WI8vpLN_-dfq9zRe9MVRQenpnhM8diDeZYEUVUx9ujFkEMfJ6goNvEw6XNeGyXlXbwcV7pJpUHvFZUI9yIqCxZGV86ujcM-fj9_Sjyp3XJZzErmG5M8wNL2nTLkpQuLANeTYJFsJaNWcZMYuBWfWR7Vl4llOXwr6q__NCxRi4JG9vpmb9lbJFRSmyljqH3C8yMzL3C-6BrDRv_pS4BRULW8Sx3FFxMUBcuQKR8Pj7fbTQhwKxuBoIw4MOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNosoBMG1Lthx6AEwdpoovxvfVpKk0clLvH6fiEwAws2cBf_bMnP5-CmtRwOTkBWKzqbkGbOfl3wJkvpfDVXgWmwV9dAOy7EpJkfv2JpNWcT0fUaviYIl0yJEB9CwS_Y8qG2mjGeKYvUSaRjyCkfiEPC-ZhO-b3SXp3brkeCUpq_UqlCj4dJGwbwTbEaNY5HiiOCPwW-ClDiPhlqWxadAesir1-GMukN8yhyiwdortcz9hwDwobp6DOW835gEPrC_XCUpro0fCUaEgnptmHjDD9_co8vPrYNzXFvv3elqAS5CXciw_wEe5WkF9C_rKwcPXZ7lD0YGK5nnLwzgw3zJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrWToYPr6y2rG0WZQ9q4agNspZc87nBR8n3q_ePFZmIFwmVuoz9gTNIsSgM_hoUsIBdgan9Epb_32XuKjV_AhJ1R6yFcGR91DhNofKS90GCYFM1-aPRSKBN3V1JzSQuioLR_wqYC_X55orl3PzjzbOB3jAiuEld3qQKwBrnefbLigYV8pHqXULNEI0SYjI54dWK_id7NRkuRTegkZw8oZy1OuDV6Bke8lBDXlMWsTgnapDS_oNyAtzyjcxU5Zlw90nDTbryplXAFwgngGPON9QhJbTCI1vPYOHN5ffcKs7Z3ysSNzKj3Y22h4QUznMGbJ4C9iZ5NCcDt_4xuhVKJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCe2u4m94AzyuebOoiSBPol-Vp-lEQuXdqdpC05O-u9sA3pVbID21dgSlmhvCtBNIX5etCU8qkCyE7Vas6pVkLxI4tKX5PnXg4Xj8AFeeYfA3TbZ71gA-ty_xJq-jhwFhVPi8Kk8zH-ONT85uKLAo_ykftjeHNjv8cSEHwDRaMxWT2Q8ZkbGXVHvZBzlmO_HqW0ULj8gkTPZcnsWphE739flMEOTrL4R4w540J0WN28TZi-PzVWBSJDRC1Eh2j1nErPoPqFcRdfir4nDqRLim2_x7EzqQAIlkIgJytXR_4wlRojrONzVwaNzFK0upiuCYt_xv96RAK74eO6YQ0Xl6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=mX6vSWGsAr9hCSX_G1oiNMLvU_suqo1X1uXhfsgATePz6xpkFy4xHlMrDV9MV0VJaM_fAy06Ue6SBCBL9zrXhTbhVhP-INoikbKHBd4XVHlXIxbXYj-p3CC5O4_KbeFONSwjd6auiUxhnK8Bpotnk_XG2YYlgZwkorhmQjr1noe0qZKEsaA7xkkilR66K37RkYMrdi_DnWrYUFyUqh_n6RX6CB6Nfz_Rfoy6VyerVfQ6pKq9gV_E8slQmMP0uc7kgNPpfQVTzC-TcmQLppyUMjviDOOkM7NrSpGZX85J8ShSXB9pW50CBXeh1g6kdYZxcvIgOYrlC4bGn6-DPOHh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=mX6vSWGsAr9hCSX_G1oiNMLvU_suqo1X1uXhfsgATePz6xpkFy4xHlMrDV9MV0VJaM_fAy06Ue6SBCBL9zrXhTbhVhP-INoikbKHBd4XVHlXIxbXYj-p3CC5O4_KbeFONSwjd6auiUxhnK8Bpotnk_XG2YYlgZwkorhmQjr1noe0qZKEsaA7xkkilR66K37RkYMrdi_DnWrYUFyUqh_n6RX6CB6Nfz_Rfoy6VyerVfQ6pKq9gV_E8slQmMP0uc7kgNPpfQVTzC-TcmQLppyUMjviDOOkM7NrSpGZX85J8ShSXB9pW50CBXeh1g6kdYZxcvIgOYrlC4bGn6-DPOHh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=R6pT9v4ozU33WTvcj1CGFuRFODFQWT5ORs6dT-N-6ND7sPHafrWyRmKZnEdTVpeVeDoLvGZ17ZxARiHWBsK-eptZfj-15nCafMxq9jjQHMlKmIsKCuh7v_WO_ZUsC9pYNMJazdVbwPzCQ2ZC0PF3ThCRsYFcdho7Pr-ZsX19E7NMcf6LZ2Pm7_AGvnA-13Lksehu1ct2b6b9soVfeof8r-x52Gy0VTqQEAPeacAAR8EnLoRTDrqz30E0yJByegGboZr5XhOnu_M3a2gBhKbM4FdzzaPXO6Cqa19Gu9W62iPA2-SXgtu-8x6VgT6B99_kQBYtwM_usaoF18bK2Wf3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=R6pT9v4ozU33WTvcj1CGFuRFODFQWT5ORs6dT-N-6ND7sPHafrWyRmKZnEdTVpeVeDoLvGZ17ZxARiHWBsK-eptZfj-15nCafMxq9jjQHMlKmIsKCuh7v_WO_ZUsC9pYNMJazdVbwPzCQ2ZC0PF3ThCRsYFcdho7Pr-ZsX19E7NMcf6LZ2Pm7_AGvnA-13Lksehu1ct2b6b9soVfeof8r-x52Gy0VTqQEAPeacAAR8EnLoRTDrqz30E0yJByegGboZr5XhOnu_M3a2gBhKbM4FdzzaPXO6Cqa19Gu9W62iPA2-SXgtu-8x6VgT6B99_kQBYtwM_usaoF18bK2Wf3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RE9t7JMhUpJs-F7qF2zpZJkNQa_sKt7H1z-oTZ06G_z9vWS7WuzE2b9oPOuxzh_uJwFOj-wEB-JovOt2EPCWnpPCCtWWNYrvDV8rlKy3JKAYTR0n3dcWDKsEZxB5YEFj1rpP8wLZRkSCTG0DJchy3M0w8kLFnBa8Ixtr9_67OtQ5FcCGF8VTXa3Ca2nTbqKJms9jXhlEL-D1x4xfr5KWLm7Z6-xfbniBVjwiFXo2v9kS9I3TLUzej23oyvYS5Oms3HyPOsXuqqYJJWbASWXs-1ylBUklxw2Ap7bGFIy1cHd0C0lBApUXxWe3tJOZbX_2Q9T2vzkUnKA1F511bYWskKaxXcC-L7obBV-3T52e0XGjBszG6pwP7hbh0Vd_HS5F5oHpvdj09XyT2TCBTIpg0bA2BAHCCfLkH_FNdteHddf8oNoaGOMtZ4dQsZz8UPVAXSBG95H-AraWQBz8ApmIxrqjTOiUgmiKV9vHhblm56vvcxIuIKyNRDd30BL11Kx5hp3bo0W9dVZzeYprqXRdDdD4gLuM_f-Q5dwNwj_cS7PRRmN5eZSx75h4wZm7DIj7ktWC6jtIY90X2LCn-ATElTXaGir-PpxpkjcILXN7puBEba9Bm7bnD8x_WRdg_IlMw_q55IA95EPXsdspSNV4qRCuD6LxmxuytMyLFWFR3Ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RE9t7JMhUpJs-F7qF2zpZJkNQa_sKt7H1z-oTZ06G_z9vWS7WuzE2b9oPOuxzh_uJwFOj-wEB-JovOt2EPCWnpPCCtWWNYrvDV8rlKy3JKAYTR0n3dcWDKsEZxB5YEFj1rpP8wLZRkSCTG0DJchy3M0w8kLFnBa8Ixtr9_67OtQ5FcCGF8VTXa3Ca2nTbqKJms9jXhlEL-D1x4xfr5KWLm7Z6-xfbniBVjwiFXo2v9kS9I3TLUzej23oyvYS5Oms3HyPOsXuqqYJJWbASWXs-1ylBUklxw2Ap7bGFIy1cHd0C0lBApUXxWe3tJOZbX_2Q9T2vzkUnKA1F511bYWskKaxXcC-L7obBV-3T52e0XGjBszG6pwP7hbh0Vd_HS5F5oHpvdj09XyT2TCBTIpg0bA2BAHCCfLkH_FNdteHddf8oNoaGOMtZ4dQsZz8UPVAXSBG95H-AraWQBz8ApmIxrqjTOiUgmiKV9vHhblm56vvcxIuIKyNRDd30BL11Kx5hp3bo0W9dVZzeYprqXRdDdD4gLuM_f-Q5dwNwj_cS7PRRmN5eZSx75h4wZm7DIj7ktWC6jtIY90X2LCn-ATElTXaGir-PpxpkjcILXN7puBEba9Bm7bnD8x_WRdg_IlMw_q55IA95EPXsdspSNV4qRCuD6LxmxuytMyLFWFR3Ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=pHcoyRgI67iHgFklnQTqCpKR_mUyORbZPwOD21TWjcXMgu-6ebTc98UbGJJU4kK8NPgrD-K6mkzsIdcABmSJgS0lQOsij5V5HY0tx93PTVnwDDR3WR42HrP0yrfVI7kpJM9n1L47kxGU8NSdVq-qhwtXm1rQN4vKjsD1TyTsip10m6e-chzwKyjxn3gFvHonrq0I-KUen9hc2sclEjSmfvJzUW2-WOq3tEeLjSfnl9waL3O5sGr03h3mfFmUrfFouaKIj_hBiNHKgpKrqX4HGqsXy4r5BSn_hc9Xe2Nq1lN8-RTzqxzK3UkvTEApca9p84tHcnmyUOnKdlI9-YMLBCS3to0ObK7Zc0izg8fTTw3iFLNa2qNlXpfTxp-BbR63LexnDmVsXuk2efZ_36p7LuzqHQsrl4WPgCZOh5SU-pgzC_8y6-nlK9pVN1IjCC7J1VlJiQhWe36nno-DZVZyBRGFSMztLC-rOXGjN_F2jlFVBheWmywQjStR-34xAam5UxuqyFdlEWcm3VZ6J65IuhKnfFFQhxLH7ZUTcVc5BAfk-0GEFNjEzT903sT4yOmfLibw3y2zl4JaoE45-2I66xB0VUKm8L6pw2djshjD_9hE3hEKRt-yOzZ-wP-xARHlTYBZ3tltxmaT-eb3gFBEvJ8GiTETmHiPzVDmUnIqBNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=pHcoyRgI67iHgFklnQTqCpKR_mUyORbZPwOD21TWjcXMgu-6ebTc98UbGJJU4kK8NPgrD-K6mkzsIdcABmSJgS0lQOsij5V5HY0tx93PTVnwDDR3WR42HrP0yrfVI7kpJM9n1L47kxGU8NSdVq-qhwtXm1rQN4vKjsD1TyTsip10m6e-chzwKyjxn3gFvHonrq0I-KUen9hc2sclEjSmfvJzUW2-WOq3tEeLjSfnl9waL3O5sGr03h3mfFmUrfFouaKIj_hBiNHKgpKrqX4HGqsXy4r5BSn_hc9Xe2Nq1lN8-RTzqxzK3UkvTEApca9p84tHcnmyUOnKdlI9-YMLBCS3to0ObK7Zc0izg8fTTw3iFLNa2qNlXpfTxp-BbR63LexnDmVsXuk2efZ_36p7LuzqHQsrl4WPgCZOh5SU-pgzC_8y6-nlK9pVN1IjCC7J1VlJiQhWe36nno-DZVZyBRGFSMztLC-rOXGjN_F2jlFVBheWmywQjStR-34xAam5UxuqyFdlEWcm3VZ6J65IuhKnfFFQhxLH7ZUTcVc5BAfk-0GEFNjEzT903sT4yOmfLibw3y2zl4JaoE45-2I66xB0VUKm8L6pw2djshjD_9hE3hEKRt-yOzZ-wP-xARHlTYBZ3tltxmaT-eb3gFBEvJ8GiTETmHiPzVDmUnIqBNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=R6vi9qkwML67RJuhN9iUSxQDNlCl5FPYLXL3s9dWtNmmQnRBIK52HN1xqvze8lfzPBe_yUdSw2sWz_MP95PjOWK7vtlzONat97PYvfdkgp7uC3YMYpaEhD7AW_51HY0z5xHECNX7dbEwumwf485RSvl9Jz7AIXukPFJOpnNYJjNMjpuc7hJpal6Y71aHJfj5sx_n3OiLO54g09M_BgwLnQQlrv4ydE_9zqBDn2zvf-CmEkqInljkE5UGD1mMcE_aN1JOVy7Iao-Eesao1T3yAeAkradRVyQ3DfDN5xVQz5qSGjOmzutxlw2M0nPovBBfiT4DE7jbCLipJda8inl26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=R6vi9qkwML67RJuhN9iUSxQDNlCl5FPYLXL3s9dWtNmmQnRBIK52HN1xqvze8lfzPBe_yUdSw2sWz_MP95PjOWK7vtlzONat97PYvfdkgp7uC3YMYpaEhD7AW_51HY0z5xHECNX7dbEwumwf485RSvl9Jz7AIXukPFJOpnNYJjNMjpuc7hJpal6Y71aHJfj5sx_n3OiLO54g09M_BgwLnQQlrv4ydE_9zqBDn2zvf-CmEkqInljkE5UGD1mMcE_aN1JOVy7Iao-Eesao1T3yAeAkradRVyQ3DfDN5xVQz5qSGjOmzutxlw2M0nPovBBfiT4DE7jbCLipJda8inl26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIwdBcSRC5QaFgsWuD3kKnvo4NhOwoX3A3vD_-XYtIqzqafwQtGrJWvISXB0S0YqWEAR2AmgD-1I4wfiLiZXaNqcOgzC80kaALvzgX9EqMuxetzFpF1S6el9ZRWrXogbHjCBmUWUXep6JMImKKQnQRuzPaP_nMn81u9EdJFICPOBbC7GSAMWgL7BNXvjufdrknKJAlTH8mi9IqD7K7A1bvPcJn9Bn34juCDtH3bHm5Fv1BGCxop5kug2a3_29Rl1DRuu6TAhIoVbxuEi6uvkiYLCGMrfcp2HLRToFC_cRbE4Em1YmnZbEdCOzbe1rFFM3U6P1-sk61KNg5F_kkoyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Zc9PTgpjg5lXPCmUlxrm-Ed8xN_iuVFiUP7-uMw2mJJpdXJlo1qlasd636DiNt5HLmAOovV8HIQxe9EjqOKJItDaMXhFYfEi_K2mVD-v89JsieH6voMX38DnoYBamNNR6ko5yFUZwNDSfdYv3s0FD4bW1bvQOpN9cfHi4dckub9sNIfRrWC_C2oSd3klUhw-mOnV62TBl1v83XY7ZnusPrskOqQlnW6kW0pY7xcq99HX7kUs-a6xTzKzbpvR93tIPkriU3bSLvCVYCADjQLPU3xJYySClU_qb1Fe4tSk9KAAIiBJ9YWDgcn5VlrayNCZtkwCJe5vfG8wiXdCnLcxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Zc9PTgpjg5lXPCmUlxrm-Ed8xN_iuVFiUP7-uMw2mJJpdXJlo1qlasd636DiNt5HLmAOovV8HIQxe9EjqOKJItDaMXhFYfEi_K2mVD-v89JsieH6voMX38DnoYBamNNR6ko5yFUZwNDSfdYv3s0FD4bW1bvQOpN9cfHi4dckub9sNIfRrWC_C2oSd3klUhw-mOnV62TBl1v83XY7ZnusPrskOqQlnW6kW0pY7xcq99HX7kUs-a6xTzKzbpvR93tIPkriU3bSLvCVYCADjQLPU3xJYySClU_qb1Fe4tSk9KAAIiBJ9YWDgcn5VlrayNCZtkwCJe5vfG8wiXdCnLcxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=qAe7QdfQHDMjUbPopPoDfYiXVwLy-37B9XSWRXusbGNf2rS3jZsc8NPX__Ann1zOIT6rFLx6NbIBainonhNowMeSTaiug_7YqxcM8iAAIRWNNmrmF39hU4uA9qybvlmCMw01y6U-wKQwJbj-v9j5HmfISaH9vIEKLBj59WB-xyilR2nop_V5Nn5KCcdtMSULR083ndW40uJISq1GkUlWVutW5wt2httNvGo-QDjT8akmKehyxIwqIdg--KbyKXuGHfjCXLD7dlGqvhJwEDlmscrmArH_ZEs-02hlhrc-qfQFvX8OjoAf4K9mpwDZhM-XhLIUaAXCDBiD2prTQtNOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=qAe7QdfQHDMjUbPopPoDfYiXVwLy-37B9XSWRXusbGNf2rS3jZsc8NPX__Ann1zOIT6rFLx6NbIBainonhNowMeSTaiug_7YqxcM8iAAIRWNNmrmF39hU4uA9qybvlmCMw01y6U-wKQwJbj-v9j5HmfISaH9vIEKLBj59WB-xyilR2nop_V5Nn5KCcdtMSULR083ndW40uJISq1GkUlWVutW5wt2httNvGo-QDjT8akmKehyxIwqIdg--KbyKXuGHfjCXLD7dlGqvhJwEDlmscrmArH_ZEs-02hlhrc-qfQFvX8OjoAf4K9mpwDZhM-XhLIUaAXCDBiD2prTQtNOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBk6E5PX5sA0FmOd2ZTGeDSoSK9odLiuDpYmd6vEIYtfvOeQSpNIyZuBvMYh7iEDdbfu35QwSKVCS2GR44213gQkHIIL8sdBzh8eA2nuFTEWz75__vbi3JLFPx8oMNo7X6KUjFmkzj3kIzKq16bCPq9-2Le__IEE-1MqQRKprFw7ak0IAMPBq-E2sOrwLUHssRd5dYDkZVBHQ7tN3qceGHpVUYiUDRmSSyD7B6_M0RPjdnHNxdHCGRqNpTFC0gT2-A9IyVJBMYNi9t0bzRNva7vUqNmf8Lad5lenR_S5qviB4WyfuU55col3ikzaVqknaqfkyu5KilWiKcd3clBvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3EUJ0EvuDkCftNDD-DSzx6LOoIHvaZ_GHlTubI70QC4Sw5Pnpvo1dPtQnAuQ3QSUbiLNNcEh58jpK0J7yyvmJsAf5MkQuPFb1o4I6vpusTeVgV49wqi97XnKJvkLo4S1o72fIoxzRgGMLunxa7wFQ7httgCHJMdWUYrRqMxQn2gxSxGNg4TsIBy28B9hW0PYBEDGmo9lrUPXTqmcIlVJgEgYs2PxUv3HjdfvC2oEdw7zNXWb1zczrI1j_pPooqnPEtkpqE1EEfag1s7AwgBUlL36XXLDGSizm_hQZtDCBdsvX81XYiJmngccKHP3NkM3ZNIAmR5GQoPX4dDrpKGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_sPNtO9IaBz-ktjbiz1AFGUMpILejeZomS20thdyLH8LLP-sX1DmNSenzHc65uaKZvLnuynGfI-FHlzoSQ3MSN0WU_9G_B-K_wxHPYWEu7Y8ijSKYpLhJTaebeiqmqn9tBl0TuhUnSA8-Q_Wfye-D-Pu5zFfAd5dV8quRZNbnC5vFQw9g--_F9wc8IqCdc4H2rAH8tL1RayybPbx4PKz_qcbWq0AlFMjOf0EWSog5rXnDpx2zN51e8TCm02HEHbqLsVCe2sCOD-vBihFl4KAF1amlKJPLQV5buVK13zRGOUewvWYl5QIoSMd6-7bvd72R2GkEYcv6zP4SygywdpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UApYM_uJjJDCECiR2Ah2T1_hXvWrbwJYnHBk0uW-SzWduAHAjOo9eMFJs6RbqI5EC56C2-8QI9t-lmTiDx75eMH_-64sZ4v48PFwRPcCZhqGygCNLImXIEKMpPgdY8OBweBCigP7mkHyM0Cc0sMlmeiym_1L7797yKU0_lG4ExkFq-QcBjB5K9_UtouglD_gxkNncZtRwsm1NTTvc5x5VdB8Paa58ePr7bBR-bmhBUFOwmB776m6gu9KJ5XACxFOBdFnm_x5rcKVgyHSrm9WNk6TcboVGCDdp3Rx7mbBJ6n0dV9ymGeBgfDAvsEZoWCC9Mbrv_aRJI8Nwf9By2WVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yun5egavoO5rkqXD3ooNjKRhMaJdX23Ph1psjt0XBKCzHJ2fczApsziLTJbxP047CotWIZgLXxM_G1tLm-vTTKjET0j_Fv07LQTGj6GGLdbIlsSXTXtWjwZFycGN4cGoO6V6ug5ifnwXPlLADECXcagqfSh9f05dcQs_ZsjMuzGGov7kI_zU0EnmLqiIhmi0eizeieDaOnD2Lik3TruYgL_zCCvFn5XUuOK255G9QMIl1_mc48unE5-UiGOa4FePOMyoZI5WthexFqaEa42Ly0k1vbCq0AdnBDUznTw5xP2FLaaFiN3wAfEsbJiLKlZI1txAvNd6xjAO1qz7XbzMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhQ2JSIAKR7U8cbdW639BfZSTAv4-mLB-fmpVdbtTpT_QZDfserSCUFqSs6JlQ-iVp-7grN6tlHvsIB9cFtdOLGebwOkqRb-8FowDUuYmBfjqoeU8ja423SE9L5_rFZ2DV03EPGWGgz01zrPjGCvelI_K2f2UIn2RltwUn2pLt6OvJcV_gTLreyGvHoYlkRjUtW3TTVJbxafcLiSBylsz9VdI8xTLnkJaXLuSfa4P8QxCwxlSLhhyEN19QN-2vqTYp-HNkQ2mM2LwBA3l8LMSlwFSMWzXGVczbGipZoZORNIk1Q6vqIckbCgolRDSCwlK7v8MZeQoh1qkPb327Rd6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUuUkPx4kVlmT-JviFAA3rgi-N-g7mPnnVCmmoifEWoS0OHtzELNsCR6AugvFl-3HBfcE3FRGsYCJs1rvKi9VxuZvSEAQDcTcmfwK1TEmuzP6XZmv-56RPSSbLt_3TimdDgnX05I_Rj6rukq3PjIHOnQ3b_If6LbVZzKOIpo6wJWgdEdLacc9KzyiFVoxCeVystJy_mYvlFxRF4YWRiKX7jbMbxlvgcMCetKpGXsgwPx32JOv_hGQ2hnJ2asatxnGtgqGkFl23Ezk7i49eRzBc4fuseC3bTXDvVGdFxbTUs-ROIzx8cGaewbrmyEeRUj6fTUW1DAxg8UW4NRhcs6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/teGguQW-YWbnq9W_1oOW5K7awhVp0gmE1YWLSFV3jrz_gvOX-PT7VDHUYzlZCwjUyWbl-2QJvamuYwkpKm_rXT6jDAT_37wSVj1658q_TJXcSgRjZ00ZTOwfwcRdnU6a7cedBsO63mvhg1_dXNuGrB4AnCldM49JxIx2Cl9Auq1aWmrrky1OUnb7A5O0W0i_bIBpJ78CYn7jAED2SkbYudFvUG_3KKI9kiP-XBRm9HDLP0wuil1_wjuiwHTkiEHsXp9yDQg5fb-yOxV-5i51PVNOY8vn4xBwpup1ISsa9k3P6rMXOQkIv55y_SBa-MXU7LeZqRVjR-IVxp3oBlSDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuhBgmmxMn8HeMYl4wkBj9p5SJjT4h05FGuoKRNy9TE6lTMtb8AtTCmCgrolxUYg52Rc9sJ9N2e5hmZ0JPzue3-fce0EGPZaAFmMIJMaCi5Jrg1mQyO9dEf4adS07BMma1CDdYbZAkFW-6R3KjRA2jy4a4_T3uN45UAMN3NuXiZeYEkhzpoSueOhygcMrg-U83pfXz4i3SkZxmSD03Gf0tIkA01EhulKKc6-yHOZdMc5GXwS_aMrTvPDTRfRBfl83G9RRV5jxtwCq5OXDgO4BI_xAMftNNjyc0MYKa9I5AHUsY3QWvRrHDLGhDp9VfG-hhnqUH6MdTs2Wc9InCvoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-dsthsl6Cf6pIOgLkg9C4_JXAfUxipfomVQ8Dpwju2MHsECgwONRBkDFoq_--6yuu-YkqslyiNy5feIZTASp9uJoTfRYtNZe-HAvqouzO_itdIQaLboiX_7oSHa2jGNmxokjLPiTAm-P_t5ii6bhwetjkCKxhTGRhDB8NXu_0wSvcVbh143P6mmEf3YkHADgFmK5_Ct9suawI0JGjhy1fCgS0MrqKHUJsKS7E6MFIqB2oqJuIM3PzRtXx4LuZortJnDuD8jU7w3-tRy3XrWYiMptSsW-E8F99oGOW5whd-lghQ9Lafe7vm3WBhwvO71DzywFmvPxCrP-5RaELjzCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=uMBF_Vsr21rsH-4t1APqbmBU3fIOWTIIeeQSWiS6wt7RarHcOuwytgxJcyOfFF3QW3CWEaXdw7kcQgZ5CnJK8P58u3igIlaM4oN-z49zvWRUBnkHxzpVp13QMsP2ZJOaMAxqUhQpRN2kbGceHhBzBzLXzJUDVe1lKpQD3lqzEKD4nADQHgiqNJDLea56-hcV6ZalHn5_tK_OD5arGSTkfksRjXjTbEvwR9L6Z5Qa-Wq5I2-n0JB4nvuu64zB_-CnUqckHkDs3iFP5UoKhFyAMsjr_AWfvkhhzOVSmDvO2NeQsqvGN0ROW1x7MAO-qmBNGeEDDNpIdHgvQaLuyPbm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=uMBF_Vsr21rsH-4t1APqbmBU3fIOWTIIeeQSWiS6wt7RarHcOuwytgxJcyOfFF3QW3CWEaXdw7kcQgZ5CnJK8P58u3igIlaM4oN-z49zvWRUBnkHxzpVp13QMsP2ZJOaMAxqUhQpRN2kbGceHhBzBzLXzJUDVe1lKpQD3lqzEKD4nADQHgiqNJDLea56-hcV6ZalHn5_tK_OD5arGSTkfksRjXjTbEvwR9L6Z5Qa-Wq5I2-n0JB4nvuu64zB_-CnUqckHkDs3iFP5UoKhFyAMsjr_AWfvkhhzOVSmDvO2NeQsqvGN0ROW1x7MAO-qmBNGeEDDNpIdHgvQaLuyPbm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGQR-eodmxgBqmBDbQKz_tVSLmOYANSyOtNc0tV7phYaCMcCFBAZnI-JabCDzY1CMUj_pNMvQXexfeDJx-4ZgTe2NrmAC6UjdtmeSeEIo0L2CZ1yARCTpvU0hd9v4bzsnkIsQMjAvSFJEcOci5Sisu6m14PlEq5RTZFzcb9SsuWZ0cRoEbPwyaVUx9vRLbSTdY7e2wvoE3B7EK_qnhujt_7egXq-th58dk1ZkqWtyhdth_1pQigDU55ApAj0eRafFQ8_MYRj_OloR0eSxWOTKBuK0jEaLiKLXbqlI5JnDgkpyuPVwgRIXpgz8PN6JuCiQubBn9_X41VMk68X2TvPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrWrsJdC-t0lE2UwNcaoLypwUIUUk-2exBkUpHIuxLh-Ug0WaufqNfwSiTPq23i3snpaeUdNXAMg8me97g2r2JLBx45Z8RcPAdMgrZrCDNPbiG9pIMcEuoi4PQPAvaq-ZMzkQ923X0p4ysKxtcFhTCEfnJAZq_6n-nNNJXB_vvxTbBxywRlj9ZWzwcgrNuS1dfnC7xCw-_7H6Q2rIP0tUYVGY9emHHTLoMrbIukfpluKhkhmeXZAXOe6k15b0ywi7GHZb-tPtRNSk5to9d2n_UAJXXz3lXD_nd5yrQ56y1Q4VwQ3ZfJx9-lzFNM2U5bwUdjgNnVDILD45p4JTfHlgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=XKm2uDGSZIixy7r0wP_3UOaxmNXGvCIxELTUBGbiGzRKJku0Ynw7T0qH3JG9mksNZzetGvkFNv8b4f3CffiG_Ag4ISJA8dNA2BH8Sa_ydW_eiP-nLfuQZslu1bOLgs3fU19Us_hjU0v-udAD-6tQUrh4oAep9cFff4sOdCvk4H-u1qxCFuFoXnm40UGSxuF5M2G_C340h7aKfWKvlMhCkD4_sLb01i41Zv1bMLo063rK59Ze6BvU4CZo_vKXsQvwOuJJGOhiWJoxJDaAHo6H3M04pIfQryivzjeCxnovwNqSEvc9n08APFt4e5KtgHXZAyfV1L-p91Aol5DOW9xphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=XKm2uDGSZIixy7r0wP_3UOaxmNXGvCIxELTUBGbiGzRKJku0Ynw7T0qH3JG9mksNZzetGvkFNv8b4f3CffiG_Ag4ISJA8dNA2BH8Sa_ydW_eiP-nLfuQZslu1bOLgs3fU19Us_hjU0v-udAD-6tQUrh4oAep9cFff4sOdCvk4H-u1qxCFuFoXnm40UGSxuF5M2G_C340h7aKfWKvlMhCkD4_sLb01i41Zv1bMLo063rK59Ze6BvU4CZo_vKXsQvwOuJJGOhiWJoxJDaAHo6H3M04pIfQryivzjeCxnovwNqSEvc9n08APFt4e5KtgHXZAyfV1L-p91Aol5DOW9xphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=luYzkIczEfCS3vPY1vfCGViFgDuoeA2KIG8BlgIe-tqXooMw7iwAeImbtPid5wrcnfff9sc2tV7Nh8-aPIijRrxlzdQA2vo7T49FoKQ3pjH0tucaEcOd9QMF64Yz-aez84crisZgxfDg-JXOIac3cISgBPfumdRqlxnLAwqVPF01KJOPRUqzkZbIKKovkOx-H6gpfZ9SmRghLLTVzW2CWNUIIT6LCdGPGQssoin_we3ps1gGTlYKhbMC15IKikfrUle4Kw7Suwubw413bqBv3FxEoiKZAQP3m_VVWXkz8Ngs7s1hzYccxadyTrPO2jWiCMr-k4QrwNp7IGFrWz-bVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=luYzkIczEfCS3vPY1vfCGViFgDuoeA2KIG8BlgIe-tqXooMw7iwAeImbtPid5wrcnfff9sc2tV7Nh8-aPIijRrxlzdQA2vo7T49FoKQ3pjH0tucaEcOd9QMF64Yz-aez84crisZgxfDg-JXOIac3cISgBPfumdRqlxnLAwqVPF01KJOPRUqzkZbIKKovkOx-H6gpfZ9SmRghLLTVzW2CWNUIIT6LCdGPGQssoin_we3ps1gGTlYKhbMC15IKikfrUle4Kw7Suwubw413bqBv3FxEoiKZAQP3m_VVWXkz8Ngs7s1hzYccxadyTrPO2jWiCMr-k4QrwNp7IGFrWz-bVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwNXgGIP1P4ViXueIYyx5swgyd1YGsXpYdNhoYf5wFPIdBBL93HkNIKQXqMhI3lEIfNjGtK0qIfcqmw8S4FfGDqC_7VqtQbkvP6SZYcY-QS6RA8hl13Uuviuz1SnUcxYFgPlmVctSb41U_Hb83LzfR2Nz3bh8Knfr-RbC_MsQVnYMkCFFFYYT6YzQ9LesawYfseAdZ3CgugGwyLAX4Vq8okO6-uybKjJolnWncbc2jSNtgTKarcsLZ4MoOmzup-iAxfnIpLIpSAqCMoWDhAT-sMaK-Q86fWruxaFfZihQh7g9hY3JcyC_mOL2awZunb3f-V0C8Nu6886Spcb6H9HOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5zEhDPnSjrJUs01KbOK19CrehKhUQZU24KX-UKSFgKnHQdDjPw2J4RNLAsNYznOX9ghlUnQu3HBMs9zA0lIy2oJtX1IozX0vQUOU_nwbCfFXxZ2j-tb6Tdm9lWwULdkheiPb4LTdT2a17xMS8SXFV7NzJmrShmjDaV-NigrMrocEUdNky57nt3pfUZz4fIP6tvqizNSnwTs4A-3jf7pyKfCLNGIhxt6Ka9ZbZiDq-rcmIW8HlwdDPrJVBihLTP9OsMnL2DLI96y3rbu5dBdQWuZ-3WIzkHkoWrbRAqrqHZmXAGcdUihUAPeF8GKrz-CAE7BXYu8x7Do8xSbel0Scg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj3Ssc3Q_hS91_DbYeQ-WE0qxj76gzDoZBRLwAHB50TxalWFMkinpE2eyWZsB4QHDxEUMop6xgmeXVv_OY50NAbykUkJGHp_Vq6gcxdclYvh4JTWPAX3QrI8ay6jeSQAdZSWsJrVlxkTsFu85jRNB3PZ0SLhiAlOK5zGBN3bDyPug9To6vPFaw5oKZzpTxypJ0Pgf5w16S1MO9f7EttXGAwHUSs_tBSvvkaBiwSqqBgPNpOTQx74uX3ClbjkOqNLBzuigjBN9KAkXTWchXLo_z9IieZ7zys0WFs4xZTQgUB8D01jI5UWF8V9TY6CRdRFKXjQqZPfJlapnDA9HL_ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9SMkI1bLtlgI3nayCcn7b_Is-RW19w7wVyc6iifCLrTcngDDLC2hLYWXIpGdTFLWbjL5fNI6Ns6NcWKH1WBE8tqeZCE9-IMx9gu7X4iVs_E5yfIXW3bJp9rAd3wwn9VrGjtUXRE6ZIIoj0tqd4CBNcZdpUfMZ3LC6LZR7RILhGUBJT0se-ZMO2cAWcdfy17dD76sLhgTj330heoyPBzX0j4g2boNPnvBpuwZFSSr3YsiuXXOKqOgONQBakVWtYixvIaVGnahuuQ3trqq58f3yp4ZdyGsqjcQfA35KJjTbTohNEFHTO_hrT3q3e2T30m4ci8POm7NH45d3NjGTGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx8XdANpxDkunCTi5dIjkNWJbzoU1uTnINmLudCwzzBIJTskQqIXzfXgaLr1foMObIB1wBiexfBMdgUPJG9vq7Aw5kq1RU8zESENpdsIFb9HUv74y7Upopm5GMHJzlmaeNNLHbS-dYFTrsDIKoPrwa8jirR8ywat06jOVhTFRHSIHCcKxx2c5yezdoZbohpF_o3c5UL7cpSwjQsSG_9w7MatN5Jjra-NVerSJLxrHreNbP0FQySRnwsSgHQPSqLIkM9kz2YuOQODzddk2JarL0Sbvh6niylK0DyHwFJ-oZjAxhabrvUJlNIm4ImCLt4nmCadSm99_sNLSQ3lFLYMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5TRclkDAxfUuAkwuA4Op4fNPkdr-97LrgDDx8CCubS8HVe2ORelYTDVxF26zwFA7YZtM8C5DRQWVHQ7t05ydg_pcArn6xUhrpXT_i-DQZjbUl346HVN886XWvxcB2Az3Sj7nVP_e58WnrmYHUbRWqohxzIWJOFRPoP18IQrTu9Cfshm6fEzvF57iGOHVYZkyfFTYf2KP4W089y557qnfdqZaKLyS70kRwMRsVh3cZ8sSEYWYZXzTyYqeIcZ5eg7uk67fYsCHj-pruk5DgE0uumyNqZkAfNSeInzZ1WcsAHNpNvDwTaFHx3MGnCp8jjtZ3QCWvHITfzEnlBT15GyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSNx8fBLkEoxgnclqua0OCGmSbyNiPbjV-yxKLdBIF9-V-oFudTuKCEx8DPq6tYf_Ki3-fLf5FVe1iNQ9ATE2QqW6HDRTXlDJB_jdu_quhr86ljKZKR7N4oRl2PJwvtfEoZ_s5XawU9tS5hqEIDdiM7uw4GmDksS3XfM69txQSgdphd5gJARBfmwCwXCl7eGZv2lWko2yKetr23uAd2w59aLBZJSgQKb334s64uskkBzpvQux9sqsC_q6Qpm8OHkDo7xo4twA5uZzctVOovB1uTksBbe9Rf23SqQXb-is-2lb-w_9sPx9hMZ5kXJSu2DxMVJeWky_Efs3UPUqqswXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNiuHUrkf8_Z0XgMr_T0yvrqqpP0rk51sD_KimNxh31A2H4YWytcvRKTg0e9obrR4aEnquxn5C7EmlUmg8Svh6QQy9aHvvpJfGL7rejvOgNhOiUBo7J__Yu74GTYxFdCfBGx8MFWuMmO4z9YAN-FMsY5UbKTNksX_18WC-kdXiDIytsvQzKBMlTU_hfVGkG-Kxp-DhQ6PLYThZdURHnKG1oC0Kn0XBTbsG5nUFXBC6HnLKKnrWO3ftQdQOONF9Aa5YXxVJkZyuXKNVv1cSt1V_neMbuFUvcOOOr1i51awc5yaqXnH8KSIRkj9baPGzZwXWhTtlKiIiPObAc79OszoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=We5zt2YfsCFWmQl6NuPb6tUKqqdgtKWg9dr3xhyGB_Hm44OPProkwWXG3UhTEnu2lo3SA2yzbgmEPEcOOkB6ZoG6-WLHKzyvMJz8inJHNemf-dUCIHa8HSYJfjcwTveOfHyD3GMxOZhWDgyoC2qXgLj2dRKc_7j3QfwO0QC2Z9g9CRHK164arh8d7EvXD_wi7GEl9tNDq_yHlPaMGwrJhVq76s1w76oVb9ODqBddZ0NeKvdJwGJVqD3eS63zZPi0uyTT8QZ3DRYLN4cYVsu4KmaZUeuDd79fzoHrqWXbopmrNDs_jq72IlFYqJ6ruqj_cpjTQ4Z5oBiEOHtre9geCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=We5zt2YfsCFWmQl6NuPb6tUKqqdgtKWg9dr3xhyGB_Hm44OPProkwWXG3UhTEnu2lo3SA2yzbgmEPEcOOkB6ZoG6-WLHKzyvMJz8inJHNemf-dUCIHa8HSYJfjcwTveOfHyD3GMxOZhWDgyoC2qXgLj2dRKc_7j3QfwO0QC2Z9g9CRHK164arh8d7EvXD_wi7GEl9tNDq_yHlPaMGwrJhVq76s1w76oVb9ODqBddZ0NeKvdJwGJVqD3eS63zZPi0uyTT8QZ3DRYLN4cYVsu4KmaZUeuDd79fzoHrqWXbopmrNDs_jq72IlFYqJ6ruqj_cpjTQ4Z5oBiEOHtre9geCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqC2i5bkj0986Fyf62lv2d0tYKS_VJ1y5XB6_kdlDbgRUe1PiUVQDzRepJ9k8qJiYRl-uHfqGRVSP_qQ4dLzqWgoU7M9Qhrm78UYGhf5w5FWe8hW1tM1sBKfZHy_iDQqnoizkxImgxa7cUuUpMX2QxP8lgJlBUygRmNpEKxwMn0q8cgc6Rz-cPzXM2KqX7mn9NWfZltvMIuyP-jJ1q5tQ8p9JBkz0ri_hvjwb3356BDDHbFOTYCbKF-IotibhDaszNzptjLSrrUY8_0WQEU8r13kYAbNfqqBpgrmXJOLQtrLqpAodMr_awyXcTp04WUUtcoo-ydPRPOtKzIu-NjUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=WI8zhz7uiR7frUbOOyZMFCvqTPwZZRR1pI2PatZTxP_bv-GL49kCOk2sB7sQ86_5zfyP5dVu-ZPD0ceHyntQasjykIVTzmI5-ambYd2Tbr94TiMJ-eXxMgObW0egauN3knwS3FE21no9sG6mLfSKuaUHTTejB5HKinKSNBqUHfK9h9Lei24F-pPT9uu3HerHE1jXt4CZ4sBLTbJyzf_MsITdlohRleVhVblpfowjp36gBFkiXwHQJLPX4dtQ0whPQXrBTycYJpPxtXpZz2OrXlcCXntzB5UqDZNBYFOblDuDRWlog8p0JFtEwnGnY76zD6c0hRPBUI4zQMACZwK7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=WI8zhz7uiR7frUbOOyZMFCvqTPwZZRR1pI2PatZTxP_bv-GL49kCOk2sB7sQ86_5zfyP5dVu-ZPD0ceHyntQasjykIVTzmI5-ambYd2Tbr94TiMJ-eXxMgObW0egauN3knwS3FE21no9sG6mLfSKuaUHTTejB5HKinKSNBqUHfK9h9Lei24F-pPT9uu3HerHE1jXt4CZ4sBLTbJyzf_MsITdlohRleVhVblpfowjp36gBFkiXwHQJLPX4dtQ0whPQXrBTycYJpPxtXpZz2OrXlcCXntzB5UqDZNBYFOblDuDRWlog8p0JFtEwnGnY76zD6c0hRPBUI4zQMACZwK7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=b9KnaOAnqe3BvODcenNBRrEQjOMWxkz3gNCQCK4ajzWpC5l905xathW-Pj9gupuKPRd27ZEKnXlOX8janx6k_569PT-B9PPb50EHVQM7X9kHD711EkvXHV6F1J4-P2r0EaQSFlk9SlIG4aRP61H6N7J8Rt1etHAun7UrvhiD1_fMwdZk2zlJGDzt51HNjMZ8WGuAO0kQrrjzx_zC-30gktkFEoS3DYOhGHIxrGkFPc2c_c1V-8Wgxm6wOJXk4Zd2pJnN5ye39g1ate0yAiNNMyKuIKybvYyb3PQuHFL-HKB0gsHixH6wj2KHEkvEDKuksaWweHzw7DVCEXOiQH4_Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=b9KnaOAnqe3BvODcenNBRrEQjOMWxkz3gNCQCK4ajzWpC5l905xathW-Pj9gupuKPRd27ZEKnXlOX8janx6k_569PT-B9PPb50EHVQM7X9kHD711EkvXHV6F1J4-P2r0EaQSFlk9SlIG4aRP61H6N7J8Rt1etHAun7UrvhiD1_fMwdZk2zlJGDzt51HNjMZ8WGuAO0kQrrjzx_zC-30gktkFEoS3DYOhGHIxrGkFPc2c_c1V-8Wgxm6wOJXk4Zd2pJnN5ye39g1ate0yAiNNMyKuIKybvYyb3PQuHFL-HKB0gsHixH6wj2KHEkvEDKuksaWweHzw7DVCEXOiQH4_Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogrHU1XzMvYSSB2rJzFYSKzByWFiaIlzSpu6UJ21776mQfxUTf3bSv8SdeshR6V8iTLXR_BSMe5OG6CwYbdipeSqEhcSlnSLm0S-cGtFS5Ri3oQPrrRvXPrb-lujUmaOdg4PfrMJRkoZ-OCfgiDA7PWeFGIhVELthy09vnYFhZVg-2yxK_-AXXMgbRf-Pl1-ht__zb3R8I4vxzgy0LGiOnXljqigvvx5-MP-gX2zIYcq0dLlba6lRHmiaDluQS8L7OrOQ1fYVvY8674Cra1Dj_xRTx1PYdmVtQaPQzooPR4iAyusPJ9OEuCnz7yKfuEnw9Km9SGiILGfyTji5EkIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAaoqUbGgUs_jRfzfQhi7ijMw8-7HKPQAdlABhA97JHM1ebwv4P1wnZlFOFzz7m_0xAcCxu5H8OfjysjUtvCyQzqcIyHZZwer-90AzF7q34KFSleySuvqFZi_qIQ3Snm0kBsDpjc6wfab1w5tRTUrX4z5eLwk-e4xPuJaMBNuYLnB6wHy7NQEF5d9Mwpuo8HcF-hnLwi0-fyH5GAr3zXm_sY_lPhTei-moCIp_yfNSHwM-PRUbfJhpYNg9RYty3fbwuW9X_LN1C3dJIzQ_cUXBrFF80b1FlpQH5m9gX7sRDR9xXRI2dJQGKJSf8riODCIT-LH4VxYsjZRunx9sSCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=aDMVBPmBU_GhStL_1jiI5eRj9tRL45b6ommSnW7SgAKDZuJQ8pM36uKes715hfxqBwa___iZiBmfkMKESlUQiOvU5TWtnVLIEiGbq1HTkKPinMChqH2-OdKAQHK7l82sldslogzNXIXhyZue_uej287LOM_5o31J6hfelG9iN73LWm8swi4Axc2FKEGsnqq3HwYLPlxIEeQlv-eEmBhhDu1Acrz3vmF-y3_g18tVZbBSctMwMb9AItjmpYlLumEwBhbxCZJy_4AkXt-qG6Zvkam7r8eSEMpUfWBN0RCaVqg-JPsGGCKEHpD-inUijKfz9nG-7vghEN9AiCopt5ceGXGIFf601lg-RrbCRq2lUhQbK8U99_1SrV5_qcYOllr5olfHPt4nHaqUrAnQzUKwiAjt4DX1Hz8xl31wuypGCkQsKnTUl5-l29T5Cro0xvgql1SaxgR5gBC7YiT9ybn2TYaR5UtsFiCLofYTlvZaoed-7uMuKm9NsINY70YylPCWyoyEDAOLvolS4yaBSim3nPbgbBqyaV5yBT4Im8s9WhNk8L0ojzdElMy0JW3uVOHXPvhSRtBIOMt7vfNk7ngJO9xRmc7smkKISJzDiQrQqAnJfODZUZX5N--MItup2Dlqi0EHYZ7BfaZLJ6mGlZ6l25Fs-h8eplbj3RWNQ8JGiRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=aDMVBPmBU_GhStL_1jiI5eRj9tRL45b6ommSnW7SgAKDZuJQ8pM36uKes715hfxqBwa___iZiBmfkMKESlUQiOvU5TWtnVLIEiGbq1HTkKPinMChqH2-OdKAQHK7l82sldslogzNXIXhyZue_uej287LOM_5o31J6hfelG9iN73LWm8swi4Axc2FKEGsnqq3HwYLPlxIEeQlv-eEmBhhDu1Acrz3vmF-y3_g18tVZbBSctMwMb9AItjmpYlLumEwBhbxCZJy_4AkXt-qG6Zvkam7r8eSEMpUfWBN0RCaVqg-JPsGGCKEHpD-inUijKfz9nG-7vghEN9AiCopt5ceGXGIFf601lg-RrbCRq2lUhQbK8U99_1SrV5_qcYOllr5olfHPt4nHaqUrAnQzUKwiAjt4DX1Hz8xl31wuypGCkQsKnTUl5-l29T5Cro0xvgql1SaxgR5gBC7YiT9ybn2TYaR5UtsFiCLofYTlvZaoed-7uMuKm9NsINY70YylPCWyoyEDAOLvolS4yaBSim3nPbgbBqyaV5yBT4Im8s9WhNk8L0ojzdElMy0JW3uVOHXPvhSRtBIOMt7vfNk7ngJO9xRmc7smkKISJzDiQrQqAnJfODZUZX5N--MItup2Dlqi0EHYZ7BfaZLJ6mGlZ6l25Fs-h8eplbj3RWNQ8JGiRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfVPeB5-W1jO21T5t3PoHQLQEeqSKQvbuyj7eEehyZr8Bbdef9DqUlptNgOCHKBdBkiKb8NtEGJ-8hF0k2PVYFu7OnuTxvh0XpVE5M3e9HxSFNWBU85NxWZ61ZqymVpBBqTa0d-pcEhZscrtQwHrohObC8OUPb0cGZbPlRwjC1dHRmj8mKxJpNTheSQ6yqbOQ7w4_as6T5GjnPbgz6icJ2v3t8Ja4aZUL3KG5kaM88hckTVb3VGdN-sYo6Hk9J-JFXRNjPC4GaAmM4chrcSpufoJE1_uigfCgWzokdfOmNpjvt9C-dE66zidGC4yhhxOqnA9GjALn7EuIc25oOUQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=CfRuz5OCozsU_kAan66uGG5OusR4-a7cpXxf_vaRxBp7IfXi1YcsJ0oCiz0Wgj61TMvRJ0HqG8ZwJZTrgf7Bfo796z2s0BiyFJ_CQez--XLKf_Zsh76ry_XyLlQJib-6zIZjHXquqweBxVELNybeTuk21U34GS5a-N9mOZYM3Y_ji6HPgyrBoRFCKpLKKWLmZTGO_B7nqgYlyyrM4Rj0trP06HHfowaVw5nMoXG0nfWSKTAbjxi9y4nBmyXSlZZ-vo6JliZIvJzhGOnyz1KvNxoSBS2uRg2rJCjU_0IQB2tNJ0VDNAHmlPnOgl5X4ol_pgmFcgpo0_JJiIZE83qv4QQd987Q960qlVX5ww-os17VUXs8h307RsSL_uukl1bHpvjB--9zPKzq-HKq_YktlH0iE5xjWm7brQdlYOWZz2t-3s86WGGEPzMYDtDI4izBmpbuHi1cOhr24r3toEm-h19BD1VOBfWcLrGqK9k3T8mT6bYrWFPXUf5qknzOWSvvazccQxvgjeRqIJ5to4puOIC7sroOylPxAaw8ACpBGAOvv8FqlZ3LexB7RarvqaLPxDpfWfYp6ZvBqA5DDEUdTtxMdFqrSJ7YRC8dOQwIBAUv80dCpq-aRC5w-KgStZwxtE4na1tPBWJZwi3WsIYXaqsmT7-pI00dZyZ64EGEc9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=CfRuz5OCozsU_kAan66uGG5OusR4-a7cpXxf_vaRxBp7IfXi1YcsJ0oCiz0Wgj61TMvRJ0HqG8ZwJZTrgf7Bfo796z2s0BiyFJ_CQez--XLKf_Zsh76ry_XyLlQJib-6zIZjHXquqweBxVELNybeTuk21U34GS5a-N9mOZYM3Y_ji6HPgyrBoRFCKpLKKWLmZTGO_B7nqgYlyyrM4Rj0trP06HHfowaVw5nMoXG0nfWSKTAbjxi9y4nBmyXSlZZ-vo6JliZIvJzhGOnyz1KvNxoSBS2uRg2rJCjU_0IQB2tNJ0VDNAHmlPnOgl5X4ol_pgmFcgpo0_JJiIZE83qv4QQd987Q960qlVX5ww-os17VUXs8h307RsSL_uukl1bHpvjB--9zPKzq-HKq_YktlH0iE5xjWm7brQdlYOWZz2t-3s86WGGEPzMYDtDI4izBmpbuHi1cOhr24r3toEm-h19BD1VOBfWcLrGqK9k3T8mT6bYrWFPXUf5qknzOWSvvazccQxvgjeRqIJ5to4puOIC7sroOylPxAaw8ACpBGAOvv8FqlZ3LexB7RarvqaLPxDpfWfYp6ZvBqA5DDEUdTtxMdFqrSJ7YRC8dOQwIBAUv80dCpq-aRC5w-KgStZwxtE4na1tPBWJZwi3WsIYXaqsmT7-pI00dZyZ64EGEc9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-c8_Yf7vqQulOvnO3l5yEvFD8yoBlbZ7ByEfj7qWMAP3LU7Tl5gsizM3IKuFjgh9MIYDlJ1yd-Py1_gfPpSO5-pifXeY77-3yL0uhudZBVDDwpbMLctSn7gG84Faa-IITT14sH68UnDO0Kt5OPSZgW4FElqoRAHmzWmGwjNfaW_BC-0s2sBolSENSXwOGIMavO8oT_zepGRN0vi4m18NTAeiQyL9FpFxqLcbmJQPmpcP-iiINPWtLjYMLsq0_QtVRt7fas6vWU0Pjxc3GHkrRmCELagCPKL0I0zbueW-ABfnC5DyIJ-djvxsc2CKfpg0TBZTOurTpXQBhO1rSbwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
