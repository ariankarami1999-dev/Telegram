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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 02:03:36</div>
<hr>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0EuEE9I_NYb5Wiwt4bw5eABv2-y_dSH4r62ajo1ByzhrfJcc7ZBTDhd6SgB3bLtQ_FfI492qW6Cl4wDKGThpUo9KcWV84cqzsdy40LPpejuRBtQ4kOWvHizBYKmPNowuvyfrE5ug7Cat60OXe-kgLJnMPnu8bmhudfMgFNppLgQcBxwyhaZdKzG5Ie1nag9Isirtbmf0_eRd99lmU1uQUpaW5lAYxb_RY3_YeKfEdOiigWMWrBxHGNUafdPHoAobkRITcMxifK5vKYSMyFfW5cgDZCyAWcd-G8B1tCApdXEt2yNCBBt544DM5oLtGrm1hWFADuBfBakLEuHYl3cUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZUmRoP3hFL3LlRznp25nMjuQZfUnvtHFE2EIhu7uXs5bd82f0GysseEmUhXd3N-eBtfl7unInvctIADNhd4yWo1dTImqD_zdxYmC35FmDQteEWxAeojNgQxt1DtFMXIX6YKLuSEhKU2Z0vq7NLRpKThbaki3mrIGm2Z4zmauoukH41TqEja7gyV5ZQy9dAVQTEoPAo-FRTWzrj6lo5i0aiKzvSuZShmyUULfwsN7LZOAh_cd8-KpajzKyWlBRIT0dE5M87vs9I27JxfDtuG5nE0vM7xkp4Ev2_KEUymjixjW8LEvjahzHSlEHShbVfUgCh-R-Sna55kxk132pynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKrKbCqdLLJyvGUSmzC3hfoiZLxRZ2B8Vp05WS1d4JfKg8ZYv7dPLHUBc82H22Rh53Ze0b_44oP6OpC2xpse4gjxs_60bWltLVP5fCp7XtDjPmCJdmAwPhKL2PtTGwrVqIxthcaK4V_Z8YDKw2RCaWq9mWnmKPbT32tOi3_y1Wld6pgpCrrhVnDD7gK0IxIEVn8jAgghu8gjg9Cxfem55yneVpkocKype0ezE7IoCMJACdv9bl-NSphDJ-a0kv9t7pwR4FfJzlzkjaNtAet4pDJ2U--bS-RXPFbhd6Y3yzsiSz5Te7lWDbucLlYfXOOqJHjAgx7gguFWSmTScnKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=VIE5-fyIEcaaYzQ9o162spVgoaa4Ml2-1owyg1x_FM55EWp919JniOfj6o6rvCPsebyahyveWtdw5vMwEjOOuBNaRkPCT4UKvzu176Fw0jaQcm5rn18mQRmheT3CRG9jI35jw5twruF-cctuKZsDiU9XxGTgCYW5KKFTEpVxCXY69TygG8DXwkL7PX16Ryg4fdgbq6uZswmjxlf3OTCZ9VIoK_0D3qNq4TqVNbtmnmYPyhcvzKC0nX14Y6Xlq6hgiRXK1KTn_pmHCDmL5aE-uVJQ8uWE8lDypnKIi9oTvN7JN-13xQZa34uk_EZBkM9Mlad6xs6B_fcup_nNMwUECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=VIE5-fyIEcaaYzQ9o162spVgoaa4Ml2-1owyg1x_FM55EWp919JniOfj6o6rvCPsebyahyveWtdw5vMwEjOOuBNaRkPCT4UKvzu176Fw0jaQcm5rn18mQRmheT3CRG9jI35jw5twruF-cctuKZsDiU9XxGTgCYW5KKFTEpVxCXY69TygG8DXwkL7PX16Ryg4fdgbq6uZswmjxlf3OTCZ9VIoK_0D3qNq4TqVNbtmnmYPyhcvzKC0nX14Y6Xlq6hgiRXK1KTn_pmHCDmL5aE-uVJQ8uWE8lDypnKIi9oTvN7JN-13xQZa34uk_EZBkM9Mlad6xs6B_fcup_nNMwUECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=S1nbH2AYOSprxguTtZAdlLKCNqBMmxdkdqO6kdMKF1B3rfFgoVzDGE2-cbVqIkIcvxSjP2nzl95uo1Xe4xUc1hp_-eDUyzadhdnbJC2_aO4jYSt46iAHsSMK6Or7qTX5qpVigIcLvwwDwFhoMBolhGdRY6McpAQHS-8NqLkNknmiPp7uD2g-gG7vhkfeFgXTYn1Rkon_2QZHv_A3TVygxxmP9ZHmEjmMs8FZM_bRdS8MQ6Db5S_fd6jcbbTUVBUnTi_HumD2BKpwnGkCLQW0fzmnhwsMO6JZ8pIcuMJAnzm1j6YuI_UGy7MHv6zPVprE8rSCRuDd6q3_XLCrexAOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=S1nbH2AYOSprxguTtZAdlLKCNqBMmxdkdqO6kdMKF1B3rfFgoVzDGE2-cbVqIkIcvxSjP2nzl95uo1Xe4xUc1hp_-eDUyzadhdnbJC2_aO4jYSt46iAHsSMK6Or7qTX5qpVigIcLvwwDwFhoMBolhGdRY6McpAQHS-8NqLkNknmiPp7uD2g-gG7vhkfeFgXTYn1Rkon_2QZHv_A3TVygxxmP9ZHmEjmMs8FZM_bRdS8MQ6Db5S_fd6jcbbTUVBUnTi_HumD2BKpwnGkCLQW0fzmnhwsMO6JZ8pIcuMJAnzm1j6YuI_UGy7MHv6zPVprE8rSCRuDd6q3_XLCrexAOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pobwNfTfIO3uQ1XLxwbfjVRu6-QWv_XALYEcc0lSdHPrVRRhznHIW0E5ZPHFXY_v_fKmRxdmHxiSclSZirKb-HeueyvILBzdGPjpBShW9mG09s8944I7rZpQQttRccl5OA-sZkYJF5gCWxzo8h_NWiN98CJyj-EbzpxfHy41MgGuXgfp3AtOqg8TOb_-Q5QVxWbf8JgtaOxyvepeiLnv02Ojnc7FU6vy2D5UDzFGx0V-iWtpINJcZ5ALqCg8oLFgGbPlD9BNWu0gFYiZGVnTfPLl-uL4MMwao43ep1UzxY2FlLSuGWV8zFEHDZ2ULOkRgy1Pxm2U0qqxKV7bGxIrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lmKU_FrqDBeEk_jNFviQOAAh67oDF75h9PoQjHdX4J6skywR4tGZYF6auJFawnCtcFr2emWlWWfnspAS3ctQxlC9LmHMH9pHkAqqBqUWL1Z7RaTjcFVkcmH6z4W33VLE71xyuIPgWWCcazvK0VO8uHM8JTAqdvDSjctOrifjRMwoZ1SwBZSY2Ox7PnDHbqz5t3EMstGZPzItZTbE1NH4dPXsuzW2bT1xLv6D6LiLWUjCH9dCJIu9JLR952P8ow_oP1QHjlUgLWbw3X2LoxzhrWBgfqQ5FGPhM1acYIFsJQTVEgGqtjH5z3u24MotlIjH3LVV7BpuR9eZLs5-phPqUYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lmKU_FrqDBeEk_jNFviQOAAh67oDF75h9PoQjHdX4J6skywR4tGZYF6auJFawnCtcFr2emWlWWfnspAS3ctQxlC9LmHMH9pHkAqqBqUWL1Z7RaTjcFVkcmH6z4W33VLE71xyuIPgWWCcazvK0VO8uHM8JTAqdvDSjctOrifjRMwoZ1SwBZSY2Ox7PnDHbqz5t3EMstGZPzItZTbE1NH4dPXsuzW2bT1xLv6D6LiLWUjCH9dCJIu9JLR952P8ow_oP1QHjlUgLWbw3X2LoxzhrWBgfqQ5FGPhM1acYIFsJQTVEgGqtjH5z3u24MotlIjH3LVV7BpuR9eZLs5-phPqUYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bv9Jl0ASHj-s2hEzvR-iXqM7U1CLDgj7_GrANJ0usSHtl_z7MNb_SJff2T0B0OPLZUDxxam8OvgetB6Bfc1ZD30yNubp8y8tUKFC-gkvcMbDRCCBMYLv9jJZ8JExhlu27J3lyes9AJhd_FMulbgR-B3SwZMERf00cb3WlLfyLOFRKQXSh8VJaKke_m-pmAIYyKU377Eg69BYFqQVGBF0PGVb14sM8NqGZ4KVYLfb5N7RTipiT6owqBzkmBakK1Cux8L7wC4DQhXLK8pLsvt1QYt_zzHC3RpJMvsXBst6tVUnzeyGtVuK_aXWmu4-vMJ2MiB-k6h1gBou6_qyq926og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bv9Jl0ASHj-s2hEzvR-iXqM7U1CLDgj7_GrANJ0usSHtl_z7MNb_SJff2T0B0OPLZUDxxam8OvgetB6Bfc1ZD30yNubp8y8tUKFC-gkvcMbDRCCBMYLv9jJZ8JExhlu27J3lyes9AJhd_FMulbgR-B3SwZMERf00cb3WlLfyLOFRKQXSh8VJaKke_m-pmAIYyKU377Eg69BYFqQVGBF0PGVb14sM8NqGZ4KVYLfb5N7RTipiT6owqBzkmBakK1Cux8L7wC4DQhXLK8pLsvt1QYt_zzHC3RpJMvsXBst6tVUnzeyGtVuK_aXWmu4-vMJ2MiB-k6h1gBou6_qyq926og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNDCluMKiGYw0sfnPMBp5Ffxk8QQX-bcNj0G6pioo8SbovDv19XGS62tyoHqasKVIWYsoqomAcT5h4ImW21W28Ny9orgVMvMGwufLQdW_mG9xSfSq0sEngmKYK-5nG4G6XQY_q7sxPG21o2fDPYrM2DW4ATyLEeKhyHRmQFVnI2WQu-AsV_0BIKbcQE3QzV4W-uVWSagTwT-aDdISFOqZfLnVQlF6nT38Dsv_Zhbs848JN0fcFuqDqRVuyn5k6b9gctjLimwdTKf7aF7-uTO5Hz9lIBY0qfDD9jq5mDLyOj2YdWRpvuxLU3JhkNHY9fFK_Bj_k7xG1rOHsmhOI38YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0P46-V4sbKfc20j20E3N36ToF2ggJ4R-p4JaAnUoz1T_7cSHlUPAB5Ih8Nf2AHx61vt-a4yH3UF2OIT6jI0dguD0P4rjW9OVmGGqp-krnXFg2cpAePj61spQYjrLKsNsA_rU2FPcZJ_IwLE8FywsFXP_wa55TWu0HeTm9oqC8C67oE45P8CN7vQWS2-vjRVNWkU-RqXFMrHcqc1IahX5_U-qKfQEjiHq6_qSbRjSyhe-jCAHvtjzuHB_nBwF8D6sejkigPvO9WpOYwPoKswj54Yl4IydVHI67VD01L2jrC9nwc7m6xMxNedBfozTEU4L1scrC72g0JBHAltkP0fpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJENiQrIvHTa8YeDBLV0VKgHqHXt_PniwN2Cb1s7J761h5CAkcCFyie-MqEqzp-bUcoU6EcXjV1t-cOOFDynxx2ArDanVKqQEjlMgumNYpuVO9-LQf7wCT1ozjUrkz3kdhhBqiSQ9OCkAIG0BEKxhex0IN5E5ZTf2w7yzcR1uDe7YBT-KUQ-CokSyR9sVXeB2ntKnjwTEuo84BXejai5_Et_-epl3xtkqPwLJKSM_hIc_pkoRQXv2pW6SSmvNY-fmaROXpO5drHrBfyQIqCkqO65h7sJ1gREN4Zp5oTiVuha6x1xxy0PbYwTY-2P2EfTtrGPOC7svkQpg1-XYtUbmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ByiXfewJl0dmhFWtyHkHQNN48pLRzeuYXHwNf4kKqKhC79q-gcYKxepAZnJV0FUi6y7BtRJO3bfB_SPvwNiESVY7R0MZm2-62vTj-3ojFaOU34ulHHH4mmxNZzkhq2re1h9dQtr0voKukVKZoOCadTORUsOAhxyH17Q29_ideMRaVTEBHF1jrdO0RXJUwSoLKzNRruZ1rcWX_XmBfkMCzaRp5rr1fD4NsqODqBCYNDVZxgnCDXyU8NO8wgpcSg9zay5z3Bcx3geCyhuRu55Ee_TH2P_Pr_9krn6ngVK9AkJUwiIAEmBhHHus0IRs9aSNBcN-_5_u3Vh6bYYIlNjBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ByiXfewJl0dmhFWtyHkHQNN48pLRzeuYXHwNf4kKqKhC79q-gcYKxepAZnJV0FUi6y7BtRJO3bfB_SPvwNiESVY7R0MZm2-62vTj-3ojFaOU34ulHHH4mmxNZzkhq2re1h9dQtr0voKukVKZoOCadTORUsOAhxyH17Q29_ideMRaVTEBHF1jrdO0RXJUwSoLKzNRruZ1rcWX_XmBfkMCzaRp5rr1fD4NsqODqBCYNDVZxgnCDXyU8NO8wgpcSg9zay5z3Bcx3geCyhuRu55Ee_TH2P_Pr_9krn6ngVK9AkJUwiIAEmBhHHus0IRs9aSNBcN-_5_u3Vh6bYYIlNjBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UAsSSFa_KXL7dd450XvXZfEm9KxaoptZiKdHlmQf7mv56tCwB4X2nC583ZbEE9bobCVIRBFoA6KBrvv5E1Co4CWD9M02ZpK-vODRV-I8C9re1oGo459HRAbVdE-c_FuWcWaSQF3fKgcs241lb_QLwIl_uvugkpBRZ0ad0OQVAwsKOpOm2nHM5hl6UCOxh7UW-MHAXinOZ_Ea-YMAodxrjExG_hH9phH1mejVSrmy96oD-orS2QyUxUjOAU03P20GZeC8d5B-lMug8zS81F-5R5U8l8YxtQ9xrHwm2nnH1E44tvAc7pdOokNsI1xvFDR5FJCMTnWsfWRpOFLPHwDT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UAsSSFa_KXL7dd450XvXZfEm9KxaoptZiKdHlmQf7mv56tCwB4X2nC583ZbEE9bobCVIRBFoA6KBrvv5E1Co4CWD9M02ZpK-vODRV-I8C9re1oGo459HRAbVdE-c_FuWcWaSQF3fKgcs241lb_QLwIl_uvugkpBRZ0ad0OQVAwsKOpOm2nHM5hl6UCOxh7UW-MHAXinOZ_Ea-YMAodxrjExG_hH9phH1mejVSrmy96oD-orS2QyUxUjOAU03P20GZeC8d5B-lMug8zS81F-5R5U8l8YxtQ9xrHwm2nnH1E44tvAc7pdOokNsI1xvFDR5FJCMTnWsfWRpOFLPHwDT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=qIl8Yydcc_b1LAKaNAuzhI3I7bjncBC7a_DRxStcOtIzt4o7adeIHTVRkm_JBZ2xYDDukchhOYfhdz-SCiWuc3q95LocGS9aYIR3DuluLKl5VZEJMyscr1AZZzJ-p63Q_lPsgduNg4_bDsLt6FO5fT7YalgyA9pIGra-Bc-Ro4Qtt8vrvl-3vO691SLHZ5EE20yo5qbx_d7_enENm_qGTeleSQKdeEvZDpSaWtsl06b_KvBWdSEgvYcILkBuBerJ7H5pT6MWievIRhQFsT0IRjFBMbKyrgM6nOGKmGnrKAzgMF0wpsBN-o-0831U1ZKJey9pa6RGpI0l1XJJ2znJ65V-1fJuED3UC9XxuNBKEI-2qHZntSRoMWxKeUY1xH3rknCv-Ho3anzFjJFeSNQb4kJF7ysocHssasD04JxwAgs03ppbeeGJO1VhlRZSYT75qE4D89RX-v2c1zzCE-RaWeKx42XBIrv3k1wEghuntiiTTNE0rNZeN4aIWE1-3O7_KUMcQJAOxdK7OQYYdAE071VlM4eG_BepME0q8iPQ-LK6_Ir5cJCI6g_HRUzB39jG2wEmmWy1QOxSQRM9P_2E27bbaHjqTeWZTCmBL0Wql1Qofu6_SgujG9AACJ-bPdJVdW-YhvTXALmenyvZee3KER0kBErKKBn9zvlQiYXtPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=qIl8Yydcc_b1LAKaNAuzhI3I7bjncBC7a_DRxStcOtIzt4o7adeIHTVRkm_JBZ2xYDDukchhOYfhdz-SCiWuc3q95LocGS9aYIR3DuluLKl5VZEJMyscr1AZZzJ-p63Q_lPsgduNg4_bDsLt6FO5fT7YalgyA9pIGra-Bc-Ro4Qtt8vrvl-3vO691SLHZ5EE20yo5qbx_d7_enENm_qGTeleSQKdeEvZDpSaWtsl06b_KvBWdSEgvYcILkBuBerJ7H5pT6MWievIRhQFsT0IRjFBMbKyrgM6nOGKmGnrKAzgMF0wpsBN-o-0831U1ZKJey9pa6RGpI0l1XJJ2znJ65V-1fJuED3UC9XxuNBKEI-2qHZntSRoMWxKeUY1xH3rknCv-Ho3anzFjJFeSNQb4kJF7ysocHssasD04JxwAgs03ppbeeGJO1VhlRZSYT75qE4D89RX-v2c1zzCE-RaWeKx42XBIrv3k1wEghuntiiTTNE0rNZeN4aIWE1-3O7_KUMcQJAOxdK7OQYYdAE071VlM4eG_BepME0q8iPQ-LK6_Ir5cJCI6g_HRUzB39jG2wEmmWy1QOxSQRM9P_2E27bbaHjqTeWZTCmBL0Wql1Qofu6_SgujG9AACJ-bPdJVdW-YhvTXALmenyvZee3KER0kBErKKBn9zvlQiYXtPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=lRvBvNZ2GBSrP-IoPyik0v9jD756CK6R1pb7ujar1v83Lmwc1Tnq5Et3EjZqKVgco012RR3NGKCXjzQww_51BdqhHrqKshSpxdPJhFjEhtPUhyMYJRVRnJ3ddbl6AzPaISR2b8Hey7O6AmSNHH2_lkYmWQ0TEoFARzpg1hbe2_BOEOudb_lfexy0V93r-FMwb-12m4ItCjfvxFbmtq7pyywVLv6uHovW8ZMXV8XbA1QV4CiW0RtL6Pme2OKXWKE39b9GosCZMy3ZXuHDo1itjeD95lD70M2KZ3Ry6kH7fP7fTofIaXOjS4BdGbFcpWI9XHC96vcp8YbPAyUR_GMCK5IfTk1_YpEEJsXPfRwT84bbQ8i86z-B9wNbh7TvPg5f1f1CWv3jyfOB2kzmodREtUpOUH6XKGffFIO6wT7RTpxyS0z3hpHBro2gv-q2Dor-WXGQEOo4aUk-_HT3Pd6iOELIoYZM3uzyaGktx6fR4agfqWEQU-juOrIKPp96wMOpCC6Q15wgD9zdqHK8mGvFqxRGA8DSEJxn2RO4bidOPapdtXfTDMsc3884ypHWXbvI3eBsqvw4uPY-ANg0UT-gSDcrhB8_hI1JQnn17_XNSkpRAjcoj-6r5JvQCDEEYLRK2xsvtjj_PqpP7HZTOfw48AX7fnYIp6SoOZe98bGYCQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=lRvBvNZ2GBSrP-IoPyik0v9jD756CK6R1pb7ujar1v83Lmwc1Tnq5Et3EjZqKVgco012RR3NGKCXjzQww_51BdqhHrqKshSpxdPJhFjEhtPUhyMYJRVRnJ3ddbl6AzPaISR2b8Hey7O6AmSNHH2_lkYmWQ0TEoFARzpg1hbe2_BOEOudb_lfexy0V93r-FMwb-12m4ItCjfvxFbmtq7pyywVLv6uHovW8ZMXV8XbA1QV4CiW0RtL6Pme2OKXWKE39b9GosCZMy3ZXuHDo1itjeD95lD70M2KZ3Ry6kH7fP7fTofIaXOjS4BdGbFcpWI9XHC96vcp8YbPAyUR_GMCK5IfTk1_YpEEJsXPfRwT84bbQ8i86z-B9wNbh7TvPg5f1f1CWv3jyfOB2kzmodREtUpOUH6XKGffFIO6wT7RTpxyS0z3hpHBro2gv-q2Dor-WXGQEOo4aUk-_HT3Pd6iOELIoYZM3uzyaGktx6fR4agfqWEQU-juOrIKPp96wMOpCC6Q15wgD9zdqHK8mGvFqxRGA8DSEJxn2RO4bidOPapdtXfTDMsc3884ypHWXbvI3eBsqvw4uPY-ANg0UT-gSDcrhB8_hI1JQnn17_XNSkpRAjcoj-6r5JvQCDEEYLRK2xsvtjj_PqpP7HZTOfw48AX7fnYIp6SoOZe98bGYCQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FkhWiPhX03Mc7Jd5VDuV-dTYXN5NFmb5Jrh2gEMRQczkCJhfhOsN5fBdFu-v6fTvBUDn06FFPRfFkQerHFjSjFSbKgaEOhpPI8-oo5XSd6RYoAoG3WZmiEGJbDUf-ZfOAdcEuqoV42POpcUukcjpTxesDa1Su-pgJp9Oqn8DH_59fuy1e7boQuSa6n6nhCQ7_1cRZGH0HDtbPNzPWLPOfh_zQzvdb6GVjiW6kKiaOPZZVytM0oNknXH2SioPUUhkewUEpDFULU7j4ll2ZddJdY0jMa9WhSA6482uaEvBvFlQyrenATF5y1JIHxrAJCJ12cEROltIUgXlpTX0j4dGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FkhWiPhX03Mc7Jd5VDuV-dTYXN5NFmb5Jrh2gEMRQczkCJhfhOsN5fBdFu-v6fTvBUDn06FFPRfFkQerHFjSjFSbKgaEOhpPI8-oo5XSd6RYoAoG3WZmiEGJbDUf-ZfOAdcEuqoV42POpcUukcjpTxesDa1Su-pgJp9Oqn8DH_59fuy1e7boQuSa6n6nhCQ7_1cRZGH0HDtbPNzPWLPOfh_zQzvdb6GVjiW6kKiaOPZZVytM0oNknXH2SioPUUhkewUEpDFULU7j4ll2ZddJdY0jMa9WhSA6482uaEvBvFlQyrenATF5y1JIHxrAJCJ12cEROltIUgXlpTX0j4dGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ_HtiT1T1Fa1BOLU5as1PEwlWAytLg8ens0A_B9O20BCk5PcsUtUVZrudRkWbZvpg3uNZT1hltD6bAe0wU6-vhdwl7xwD6LuZm7W6YmHBVXPSR1BMoMI-oFDlScBC-gMsHQAn28fpwL7-RMlKiIs9ScRtB9R-BuU19EEZFis9mleg1iJIs1WbpXCyVg2iifWbanI_MDNlJLE2U50px3q3SDhdASHjoUHqbrzaprb4XDWnL4P5vnLnTei5SeDh9OYz40VuVpUG7gRoKuowK8H5o-Ax-93UmvWvVvBouO0YU3somrdwscb78JDBQY7v3WLm5F1Z5ortLkpThP_QNhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=inQ2pS9S3qe6yZXXW4rqcLUH2tVATQwlYzTeqtXDqbBx0ktqb0mVOX-FWJSno4fXRXg5gu-Vo7imC1Yk2Z71256OL47n9MYrmwniXJfuNwG4oZLTs2hFwa35a14IUgwQr8PfURhMWAHDRO43vZ46zSlF-nIqYHtb1smAA4_LaErEgTZrSEburaSphPRsc6dUEJ2ForHpYiQ3VtBbNTGOX8Z2IfOv1syS8ai-didzkK4Vx4aaRM0-voJODqohlFrFZ-_ssWtGJPrTmRELdjihE683W15_EopFRZcqjxQ0MWhPHVoZl_r04-Du5TmZa1SkmxKRng6JYH3Qz8ntujyLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=inQ2pS9S3qe6yZXXW4rqcLUH2tVATQwlYzTeqtXDqbBx0ktqb0mVOX-FWJSno4fXRXg5gu-Vo7imC1Yk2Z71256OL47n9MYrmwniXJfuNwG4oZLTs2hFwa35a14IUgwQr8PfURhMWAHDRO43vZ46zSlF-nIqYHtb1smAA4_LaErEgTZrSEburaSphPRsc6dUEJ2ForHpYiQ3VtBbNTGOX8Z2IfOv1syS8ai-didzkK4Vx4aaRM0-voJODqohlFrFZ-_ssWtGJPrTmRELdjihE683W15_EopFRZcqjxQ0MWhPHVoZl_r04-Du5TmZa1SkmxKRng6JYH3Qz8ntujyLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=JYRufS9CcuIKm5wWC6Sru4tstKXg4Uc42HHTx0cOvSDh2agxSfylBHZ8KSY7OrJ74X7X0veNvVsqseDphnkeSEOvdd7oPX7Pz4vDOmGkTlPErNqAwuKpDzqbTTBlwaM0ARSJdJTcryd4H231Q_p0A1HFSVRAyNh6xE9cv51O9S4JynR9XrkSpYWavFKgeBEXoeUxJIZHyc4WxxC1r-1k5GUsCyLAw4by3X1Np_MF_GRwVrR189YlYnLTbghTz1Obr-nTtBHBNbkmIFILHnVJb24jyW6ufePRic5A0jnf7qHIIO5Vg19gz9qDspZRzVSu0hM542OoMwK2dv1GpYdbbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=JYRufS9CcuIKm5wWC6Sru4tstKXg4Uc42HHTx0cOvSDh2agxSfylBHZ8KSY7OrJ74X7X0veNvVsqseDphnkeSEOvdd7oPX7Pz4vDOmGkTlPErNqAwuKpDzqbTTBlwaM0ARSJdJTcryd4H231Q_p0A1HFSVRAyNh6xE9cv51O9S4JynR9XrkSpYWavFKgeBEXoeUxJIZHyc4WxxC1r-1k5GUsCyLAw4by3X1Np_MF_GRwVrR189YlYnLTbghTz1Obr-nTtBHBNbkmIFILHnVJb24jyW6ufePRic5A0jnf7qHIIO5Vg19gz9qDspZRzVSu0hM542OoMwK2dv1GpYdbbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4GanROXzgDt3ZvNENPOJQjCnjlwJGo6jXGnCM5ZbJeQkSttSXbxEzNXwzVKqCD-AfQ9j1WpTPOQVXWZl-36KOO20vWICzGNNqAy2Z9SdwqqtoRC41TJ3OUC7hlbs4NkYf2jAjYXuAxdtCxVXX80kqGIH9y9F2ZJvtAhzrXoZzg8ZtJBVAQ8nNFArkxSCkDR3EkCm0BzMGT1NYsgJJTMn6rJLOHcD52TVDKY359CClpP369XWjgU4uzitnFRHJrzLterwB6_h4cojNPXFGdd46lPzsu77MLANvV2stKFGqWt_gy01XooMg-H1OE2--LNYAN0VZbe09NsiGQ048nu9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHjuH9k4YhZVZxw1yRle87E3HORuZrJY4eKVBiwaeMziiKHYSMl_Lykf2FjdBSJo4bzgMgeL0mSBdP1QobvkdD-Mmg_tP3VtSV9-LeH0h6ZjRGU4ZgMfo7yJCyE47kOyKkj-dYonO1lXrzqWyUDrkFCHL8inmrATSWOCGDWcwUm2yFoAqBtb0E4sPEnhoIsbtQkE7s5BNo_9w92t-yABRVNOMsSJD-sdQM9YJmG8kN8ecSwVGiPwSnaTXJsx_11x-MCg2rOWAnwjfULgXMFHxetGykulvC-QypjVZTxfMNaIT9soscgi1c74g0UD7oNFyWIE6aE8D5ExsL25UUbh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUdq3MdGmeeYQkNuvZDQ4N6LrPJH5Phf-_YnD4ftP105A-5uePYRGimIMqiF98vtESDu325OWiQOp09VByU_SkN60mF-hS4VNqar1QuUyA6F0Fkr7bhID4XeykFG48HtXeYoOhVhz5EoX2OEiKKZelRGOne7liXmKid_2No0FD0ziJaPii8U1Kpft12rZqjyaTGO37gOCEwkt1vPN6WjWS5frOt_DyUqBqvz1er2P8R81akb6W53wmdiaGoE1_x1dvG5kl98dWs-j8OzkyOHR4DfyYn-cJo0H2b48jaXy0cN2CScHtPHbopYAOrY-sj6uAsa58YwAqwBHwH69FsT5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYMHgxb6EkGxlp9F8OZ4FuYyy5yvmzdIRsl6cku79k5Tpbkz-O56AGqZqTN_szueHIjQJa9jnYOES7bi3fx6B7lVJzpB0LCTHfa3DAZRGBF0tpsNm8S_NiIXxQIDLw2qDO7ZLaXlqH2S4mhKObPMA0o9KxkIVrDcqT2BbS_vJmyLbeqo74cFNu8kUZBVURhWDsLtMZ1q-39uQxSN_dWnqLVWN0sq2DYv6Pt9akrSNWda3TBx3rDE4hfd2f9nQwB7Rxr1onlMERGa35l8qK6GsvS8-7IeAkBmf5o48ydbsMwD9FB_fFcUIuzI8bX4dT_8kDk__0UWcwkHwlnepHqu5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzRU4R451MxddizhXmeXaBlwCCJH8yUTqhmlZ3kVMko7aqiLRoh4PO4HX2Lkl3L2mX8YbMKOwitiFU1Th3i24EHlxOgfJjcxRVhE6xIMaVMssLfv2vfUoEpHZCs0nQFyhiAj9rNq0WrfUo5bzh_JzBQV0Km-m-JgF7Sae7dYaJcqWxd80XclZGMlFnFCkNCCGR6q35QSYv9bdCXctNa6zY7JFQiQ-SQciQq35MaeNDza6SYLealCr8EqPIB_sBa7Q8LYF-jZ4y5XlXtUKuhI1BO--cPfvQ0jsklPegF2KqcrKsMDpCFMu2guQDjBw57m34eKoQicaJEPp5q57MWIzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiLTDzI52CvPFjIjuWNolIVdRac5AIJH68r1wjBVzz50uMlxLAhvr9iKv1wwUUxjatvNgMEiPAcMKJjD3Fur0QQU-0Ac46nfYB49NQimtVl-s9Ti8zBNTcVjfe4lZa6XhMQNsqF59E4KUn6ZJmR6jCE4ZKb9mE-xIqtiimxsIYbdSML6IptVqk_4H_VqmYJOqQV_pGrpahiDDP3WXqTgHm21Y4LsAXiYSMVNSsk5p_Wuj5goRkTRRr4gTkmMD7mkC4h-24PzpkKWqTJhD3ZbXp-F8UddAwv6W7CA_vflpPMIshOusjN8SwCh37kerH_oir-neAyO6zWHjrFeJjn6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLyivTpX_PaAaQQO3gNrQDKT9QHEIriSt-F2nXDC1q19YemuKX4JGL5TJm6ELVAKQaSvemE8k_MCvJUlMPyfrR_8UMtHKt_MUktaGodyPWigAX4YhO847Wf3XyoTpEioTMz03oGYvSi11uSm1Y1XDhbyEj4myghH8dt4le5lJB-PZh3EPI_6y5LI0KQrBcgZ-nCbqSiNv71VFJHRzMK3_McDyUdngg1S6TOQ0N5_Vxd1GR5ooQmD4d2oQcrBM-7SOqGEjOa7If3AiN0W2cknMYr-gybx0pvRylMgpzxQIxdt1ge-UAEtevM5kI0OHUdeZ3uPhzC6O9cBp-zwQrUtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXFGTmRX5O7b8VhhXHpdKNVtofVqLRCnU3Dnn0eKmYOQ06VokI2OuIjDxgDhOcw9DklVj3U6Pz2ONtFCiF0d2btKOWwHvC8HFxWp3CQQCIQirkWOuyiicxgOJ-CMR04pN9ZKJJ6z9TjshcELNfTKi9hpUMoftp-kS2fXuSXYeGwcxhzcNyZnod21k5h_MXcKCKGKM78BuCD84BrLGm2YSlHx2_Th0ww3RG_dpnZoi_X52tokM9Nq2HhUuUKkhkOGOesaNcUsjzTh2zGh8lrsAHLCSQI3GLBzpxcf3C171hp1X_5_WD09y6cZ-9N2D8xYKMWkApeGA-4qLCgboYmO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYcQzPuOdkfQ5r9mJzN4VOgXHzDxyZPUDj9Ra-AoBpwGbYM_0gJw6_tlFZ5Sd5YFnq8fBFLh4nm7HPTz01JmGl8KH5e3WJXXmxVENjrQcrjXXPVfmpPT47nyY2XMEf1eKq5fHugue_1eVezamgF7tSkP7XWZAKzWGkQIkjlmMzgdinTp4D6K8QGI3p3Zvx0W1ZPnKA3tQRSnUKug3xHwd72FQSW02z3ws5nIU7W6fJqYYaxEc41yMyWqbnJ1wJT1J4sNQSxR1_tB4bfqS5xsi9nj6BWkkIBqpPW-nYYXGB32rnNmo5pOfry5jHOqs-FhnWAS87nb1tAWgb3oGrJxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-X9bzRrcQ6aej71x0L8Z9A4SyldZda0nGTT5bAYnBTLuaUBSjW_6S7XbtAwcI99yyeJiyRrwar-jiwmbFbn7jqGgn9JPxhTsS7Fd1IN8Rc3JUj3eKM3SxkQtoRMXwPVsuSUwwr9SHYd3u3tht-Nqzwu7rIyhemBQm-pYvOXGQeJgYdc9Gfc_fKxc29AaFGY2ru4XUjUWPlxX6nrZGCXs_81OmuoSXfgHfeAcs7ExqMRqFKE37fyrmyoReKsDi3fDLpp5067OMmnW3lcH8kd7befJnHV3rpNqWhCYo8S3TGOS4clEIbm3oCjs0GT_vcXOFQt8Sw5azoi5Dp5XUfi-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=iTcXkUP_v-2oVZSQbJ9dzK4pCpeRqOWHYCxWlHPIdaRSIinjA67hm30EMTnBP4l-KcMVysj1Py-8dqSDEsj3QyH5UbvQYEr4dVYFEziXn6tcuxeGHytuRd3Y1oMdDDxhBEIzfExRJVnP7H-FSK0baH8yEG9ECR9iGP5aWcGGX4hvY1BJo7FEHPxSfe25Vei9W7PDtR4nAcRPqOJ3Ct_GpViUx_BO2ZqtBTjImPEOBn3bR1p3wmUvxvyJqzO3cCmTIA0PFJmU1uG3Jc-r_fxOpxOz8xfbR4re6zs0mC6UQ8iJDIIMIVJirKiBnljTfoYUTDN-ojUMt5FT6JEQPHGAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=iTcXkUP_v-2oVZSQbJ9dzK4pCpeRqOWHYCxWlHPIdaRSIinjA67hm30EMTnBP4l-KcMVysj1Py-8dqSDEsj3QyH5UbvQYEr4dVYFEziXn6tcuxeGHytuRd3Y1oMdDDxhBEIzfExRJVnP7H-FSK0baH8yEG9ECR9iGP5aWcGGX4hvY1BJo7FEHPxSfe25Vei9W7PDtR4nAcRPqOJ3Ct_GpViUx_BO2ZqtBTjImPEOBn3bR1p3wmUvxvyJqzO3cCmTIA0PFJmU1uG3Jc-r_fxOpxOz8xfbR4re6zs0mC6UQ8iJDIIMIVJirKiBnljTfoYUTDN-ojUMt5FT6JEQPHGAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJKvi4tFTzhYq3c6alGmSHGSVZcQ87H22p-_blDXQXWEvlf10YHQ_fK1GZwQbwuTVhORQf7txNmT14QTlyCgdPZadW-8_dDTzDNM__ZmA2npzcEtwrinREje4LOlg1XljibGFa3fCiJn92kWfnlcAlwo6eaxx_ooq1zQs3VKffi2bUyXwe94BedmJjHtk1tKXB9HPP4ehGaVYm77WrAbs-5jX4VPtNbEKmhTjaw1iBjXFZw61PTBX-q23ysJ7erAQ5Rd8rlPj43fFlJhyp7E3t1osiLbME_SGxr2Ladqviw9celovIg6QFKLbDBsW1tqrpEa284x1efhxLqVDcv8UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4LY9VvCETqnBSLkhqe5jlUqxcgYo2Qa7myLOlbHSZlcsIx1X9BnKK7nGiZEWYyNEgXJj2zmCfe1aJzk8G53QAaOV85IIQWMzXnxbityivHtapFJJhC7AxS9sYXulp3_DxO9FBIdiNB5JLC3aDCcU1m2PqrnXN7NV2cemVR4gjacWAcQQSOtLlIqKhGYt7UoWoGkLXLpkY7PaUgJUFCSBsnxGkIGTpCYIGGrX2KgBaFxhZnq6-wphc2Wjc28ZuCosriNfH8xP87dtwVMYC8CHVUBFhzaJUnvaR7lOfJOJDp1ZPyTmuufUT0VO4UE1jKhiWWLfD8qdvTWJYrf5JEB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Zg5kfvvLHtB8W4ZuujjTDdb7Cc0vGsx9qNc-ni9KBWeEOLnwfH0Rpp5iMwUgpbv_ryT6dKWDbvmdBq3yrdJDLOzWg06QVvUD0UjGswxWUCzynK1GtgA_cfSMstGj7Pu6ffE_HaUozSzBVGHJPofAkhRSjkpU9HhFDCVqXKacgdiVOdWOyDI1KOqd3iDQ6jotbwDccdnWheL2G0wy9dwLpxONY2IBH04NpgCnUv0gosnGPzLakw-xZiQfwa5olTeEDhJe9lRYm8Dh3W7p2Pb5WPFRNaipvmSHGTMWPVW7dAG5Cp7ZGeHhn2N5s905FGLozespzV9qYn-skx5H9RAPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Zg5kfvvLHtB8W4ZuujjTDdb7Cc0vGsx9qNc-ni9KBWeEOLnwfH0Rpp5iMwUgpbv_ryT6dKWDbvmdBq3yrdJDLOzWg06QVvUD0UjGswxWUCzynK1GtgA_cfSMstGj7Pu6ffE_HaUozSzBVGHJPofAkhRSjkpU9HhFDCVqXKacgdiVOdWOyDI1KOqd3iDQ6jotbwDccdnWheL2G0wy9dwLpxONY2IBH04NpgCnUv0gosnGPzLakw-xZiQfwa5olTeEDhJe9lRYm8Dh3W7p2Pb5WPFRNaipvmSHGTMWPVW7dAG5Cp7ZGeHhn2N5s905FGLozespzV9qYn-skx5H9RAPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YSjyaXYT3qjJYh7GfthcS7qqBgg6ihnosUmOJwOMgpJzjRvGl_9RCRT4thYhvP9FDQ6AnUhSlrWwsDk-vynLRvBV_kIXWmlmvtP2V9XFq8MSS6lJNDksVfMln6c7NI0M82ZKuNn-ggKhtFExcJGrDLxLiitmiCLKaPfbDlHDngTbkPOZfxG_Pu_jUZ51c9MJSWqDP6b-8cRUWtoV0oVyHJQyh2lLhIYl3GF2985s5n4SDydmvy2vESPwI7_VOdNp-mcX9zGG1l57Zfh2aEX9WmPu2SRldnFVKBBMUYN-rim47_cyjgmE2KZbad9xNOf4nQYDD2gFDvCERLyyw_Dw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YSjyaXYT3qjJYh7GfthcS7qqBgg6ihnosUmOJwOMgpJzjRvGl_9RCRT4thYhvP9FDQ6AnUhSlrWwsDk-vynLRvBV_kIXWmlmvtP2V9XFq8MSS6lJNDksVfMln6c7NI0M82ZKuNn-ggKhtFExcJGrDLxLiitmiCLKaPfbDlHDngTbkPOZfxG_Pu_jUZ51c9MJSWqDP6b-8cRUWtoV0oVyHJQyh2lLhIYl3GF2985s5n4SDydmvy2vESPwI7_VOdNp-mcX9zGG1l57Zfh2aEX9WmPu2SRldnFVKBBMUYN-rim47_cyjgmE2KZbad9xNOf4nQYDD2gFDvCERLyyw_Dw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUJCWUrUrVJTBEz8AZgSVd_Ze3OwmEVfGcsBl6lCyVJ5pxr7EFKdC4_I-8OxPDr2yWhvSiW7KKzqRvuFRdXkAHxbRs_Im-EuIFcYMwC1qRcj4GXCjrl-ug9GV3HOtd1nwr4Fh1xXz6hyueBXLY21FwpsWxxmKcFXrRbE0a9W88QkkzX9-9iipXmkJePlzw7l-TU0SN1GB8rOw1XBbxas3oePEyYS7nMYEu6ahlMWelc84hU2ie1TFkBSzEXUOnwPZHdU-fwFw_38O3N3PKJKoDKW_lfCnw8NKJtzqPa1LhE6ztB5TcIf04JLbddqDeVPSK4bBQH3ioq13DH3PA1gmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGrl_vzBO-j9lK4qO16iKPsJQpWZC4cf_xUKmJau6_aLRpZbcmY8edifRqMPRP2ykfcYBPaY9P3Ddd1Z8wu5W6vwklTxjxdY4xTenB_f3QrT_p2IPCy-iquS5cPIBSdeVHsanvfW_2EpKHjBS2X7-0QFSsADuksBu7epGnDF_V70qoXVoXkrvLkKWdPl7sBFPSRyMuH36nFULsnaYkPq37zk9bbdcigij-o3aeLRYmZ0LRbO_RA4yRjFoFN0wjqy_9QhQZxDQvJiTujJG-GwLjkJU9qUkCQFGTohh1TQe5rHOW3HEgyuTO-eMIW1Bnb1mAM9b-YX2TAoZB-w5ld-kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSOj39-WMSOyeEJVKXdbTki-bVywvrH90tLQPzVx2cfhbJ0ErdpRa68A5Q8zWeQpHaLTCw3fGJv2QxjAQRdjvOdTluMi6fkp4mIhUdGknxDv_jEDmgl-m5WosnLf3DDwLaO4dF5QBviOGxl_6IkxzpM4wGBbCRHav_UlegBx_yZGyECEEvz7iEs51iunkyYpeHAeoAGHDFS_Mv88oGnY3ZYpuD6YvDLkeUppaGiq93krI97v1DaoDOqdCaAvqu4r6RE-djxrVL-ztbzl0T8omAl8QuRZIRZ3zJEFl9W7ZQ2cOIw5xFZhXZEm545DwCLMCLI7h4Ftq5a4oo6KyXfQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avZWcDOeJhRKnf-nWImZCV4rZenCNYV7txrERMVpV53u9ZYygtUAHG6LQjnlV6s3cppeZhSRtu82_Q2XiQON5Ee3g28GdYRf4eeQFhWeFQuLC29563uedXtPD-5xWKEn__sJW8phkSSYbQDlDjAvf-XmnKO0NGiDIGcTHY5o1ZPpPfXjx8R-ytHpBliaWA2xrGH9N0iZivroZD2UHe8coQJ-TMUEV5Gs_F1XG_zIlqFtWDt8dBmvVSYpkguTL0YBTgzUeWvPe2_L3HTmk-bhJIArD_rnKkWGC7VE62i-l38f2lCu_qT3ifY_9FfOsghiwPFmqysMfFzh4jgs-hw8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAdspftwvfae0kWgoIeDkLXJDX-5yWlbplEBK95Luo1GaWQvukQCQXiacLM643mraItuWU46V2PtI51biBn-MDlWNtciWAHJUrzkg7mUNg4nPNf4Ohhz_nnN2rkB5sEh-Z18ekYNHzFx_3NunZyhS1PhyuxmuYgubyV3nyULOtAMFgTixIhszxszsXOzRri3oIgTjUPPGpMnO0MAEsinQYc4vIvefJ0qvKWbEA0il_4gLhAmmyzbKZQA07GhdPSnKTk8QKJEKm3kB8tYUIa1UWFgYN7HePVO6fi8ouIchiT7Avi1wyjMNYvxjiTZMWiThB1uN3NVnPB1wjc4pfRd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOMAbPoUlvhutlTlIRBPP0XYRkBJUlPSQbzIdMAsCgvpY5kV1wREuumJpE-RWbpBgJorhjYCMfww679ci6-xtiKF1aw48yda42r0rhAjRb6prAIv4Xgqy7b_NcF3ZVP4X_iIvgT62q_ICx4_J5eGMvM4Um8CsKdCYMMCbFa7DjZ7cajh2xYB_ZkrWsk97q3uWCcEv99RPqNxA1sOVRtXes2PINtpSBZ4lqY9WNGIkYF0UVB48AXw7YbrrRPH9myjQt2aelhfXm2W7dUCxOxPwwfh95XEtMM9gUvYd8Q9Eke-HMtX7n83el0pl7gKYZoFJTNeXcmHN-X5uQKllDq3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T56qVfWbePMJZ_NZTZ-JWFw79VIeQJprwjJjUA6zNXbfCUrer56SmXektGKGANlGJ199Yl789nTW8f-HrsjlLHgdOrVbEM7DSFtPS4jUhLR79xrrq0duNB9dCvAPf-gzE9FM_HTHlbiL21uVhR_M6EaRRkKG97PZhfRm6zh8am__ShW32BZ9artZ4bOHoLnN4j26B0Op35WfCpCWt2fDPmVCB8E6ZQ0TeXfJDklpGxtrXQluUoXYOZB584vKWCiyS7NLrcPB1dK5rlXDnUzpy_M5QlcFwq5a8pBOXcmRuhyNbpLXZs2nuOA0Nx4I4pnC2j1atU4bN_Gc0bBru0S0xw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sUaXNg_xSv_o7J_O53eHVqkgbxH2TASXkBGgEPkWIutwbUou8qmczx3WDUx1qtZ4xvEmqXCue0GH7ebhmq0QS4tgJNax9fDksj0q4p_uJzbci2bkOZD_iWzB7D5Z7nad3x9jUC0skueW3W_dABgo5zd7i946n43Zz9Se6IdkO3CamaDUDevlHI97NgnwWD0iVGw47SLp5FFufD6-1POcGtt5Mb_wFD_e6UvXsKyHtvfqP6q5d1-Oit-INVXi1GSadZqLDaThmrj6ckK59hDigL14EkzTDcaAnSjUoQdCFN_Ryh-hXEv5A72FNcRo5TUIxMghtLBO-B96xxZ2a1Cexw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sUaXNg_xSv_o7J_O53eHVqkgbxH2TASXkBGgEPkWIutwbUou8qmczx3WDUx1qtZ4xvEmqXCue0GH7ebhmq0QS4tgJNax9fDksj0q4p_uJzbci2bkOZD_iWzB7D5Z7nad3x9jUC0skueW3W_dABgo5zd7i946n43Zz9Se6IdkO3CamaDUDevlHI97NgnwWD0iVGw47SLp5FFufD6-1POcGtt5Mb_wFD_e6UvXsKyHtvfqP6q5d1-Oit-INVXi1GSadZqLDaThmrj6ckK59hDigL14EkzTDcaAnSjUoQdCFN_Ryh-hXEv5A72FNcRo5TUIxMghtLBO-B96xxZ2a1Cexw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-Uzic1h6tFVB_aDEomNxroYM07McrKYYgPY384uSUcMWk5b27AKTlPRVXn3huoI5jxwOtvMTTw9T39SgqI9aL9y6dUTp0bpZXb82mopEWlQkit2xkF1_RsI1E8SmylrzY66f0rWS49LEiXWyX7R91P835QD_bfiHEcaqE8yuxyxdRApM-AYc5LCs9aTkB_0Wswt8d2BqTyvmlQMZVJsIJx8elW_CoCmNlTWM-55z1sb-4Ab9nmB_5n6VReU1xUSffgPnhS-5V7nT1XkADJrpiUktWk_mau0gKaT-8B2AWGpidT2ZlfzkcJ4cMvJF4pOEHPVJrUoi9GDl3IjE8WNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=JBrXZzdP2q1NeFdnRbpgOYVJtLoMKH0O8z8Kd-xJ-x2Yp6-K6g4iFSMCa-uAlRukqsPoBvHSr4oM_gAzWIzx-ldCeOfGvqtHbUULsRcp542HddZMjAuDqzbFbZsZ-yADc1AOXsN4VE_u1GZyP8aTxGGuCPV2NUJrCt5NByWjB-qTDZgcd9T50i8FRgfxBiah3zDtuFht_wpi3ZbmrfVtyroV3p3Udg2PLmKaJyS3NeSQMP4S7Tm5hAOW0Yyfz2STUmGguydRv5w5grprpwN6OVlWTcommiKej45Jjzm9ksyXbVhYLYnff62AEr1MnokBE6RIEeF7XVfVIxL7IgevWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=JBrXZzdP2q1NeFdnRbpgOYVJtLoMKH0O8z8Kd-xJ-x2Yp6-K6g4iFSMCa-uAlRukqsPoBvHSr4oM_gAzWIzx-ldCeOfGvqtHbUULsRcp542HddZMjAuDqzbFbZsZ-yADc1AOXsN4VE_u1GZyP8aTxGGuCPV2NUJrCt5NByWjB-qTDZgcd9T50i8FRgfxBiah3zDtuFht_wpi3ZbmrfVtyroV3p3Udg2PLmKaJyS3NeSQMP4S7Tm5hAOW0Yyfz2STUmGguydRv5w5grprpwN6OVlWTcommiKej45Jjzm9ksyXbVhYLYnff62AEr1MnokBE6RIEeF7XVfVIxL7IgevWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=CjxkFDv_JQjFZSoA1y4uLpLXOVs9fe1Lk8hIzkT3cUVtPIaWEo2aIEp6GK6uXqnXROFEwVlmsetUeLzmXEZNtwmsd4oPHNl_gyABuOMFf-Eh9Pq5t4L_KtbS8zaODvqLOOtvJBi-byQMJs0wABnUnLYlskPB2876VbzSAORLU8bCFHlKJSFGwoVTHMEhA2YOuU7b3bV63DjkGY9Uaq6aVnbwIad6Opo5XUNSrjCFogX7AgEguQjEF5HXNYqYGb9XEAX5vTACZJyA8unCp1kp0_px-OucKY6MeCFckJ8v-WcV7vXdIhbh76TrUQQeAxEepowNcKPq7vZTa_AA0c7DeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=CjxkFDv_JQjFZSoA1y4uLpLXOVs9fe1Lk8hIzkT3cUVtPIaWEo2aIEp6GK6uXqnXROFEwVlmsetUeLzmXEZNtwmsd4oPHNl_gyABuOMFf-Eh9Pq5t4L_KtbS8zaODvqLOOtvJBi-byQMJs0wABnUnLYlskPB2876VbzSAORLU8bCFHlKJSFGwoVTHMEhA2YOuU7b3bV63DjkGY9Uaq6aVnbwIad6Opo5XUNSrjCFogX7AgEguQjEF5HXNYqYGb9XEAX5vTACZJyA8unCp1kp0_px-OucKY6MeCFckJ8v-WcV7vXdIhbh76TrUQQeAxEepowNcKPq7vZTa_AA0c7DeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbfSAL9a9m-JwniIHM7cq-qXgJgAGCV5mshIfVuUuYMvvZOWry5EbDedxSFw0pw-SvUekVw4fRGQRZtXeQl3HFJJw2_pLpRUerszlK4uCaYtSE93V2Ib4FxrYuPe8bo5NvrylCtbfAIF35yLcNImgaJ7479ys7lU0SlWVPCNTp-6YMgXW8Y_X5iRZkeLitc-oqrjd1orZ5otvqW6N3FZeiS5J6cPr2NBvv_CuJDRam-89-ITTXHd8xo0bg1j2ghFAhx94UA7wYCNl0ynYxItcDPKG0cfXU9hzQHFltHcfM_AX3GTxm-0ZLuK1ekKhlMoe4Jhv0IYmmH0DpcBWvf9rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4ldpnd4k4kpqdjMqcj97sZ8D52493302sIqijS7dSlG19nQG1J4NUzHkEfunxZY_kaYB3Ho2Nauc_lSktAfkfHv_BbkzYD18d6icEwsF6ESPHwge6JrCzf6MTRvUA-s3Z_mAEZUTcNY6mP5ev9Z3LsYQc85lJPNhQgAVUsIDsUjFcjbVQ8KKpTxPg-oMZa_9cdsYhMp9Am0gEimhliblI8pVeHCedDgiS5AHiVrM7hvTnwge0f5RZkigCaKONJON-MoeXLI0i4loNjNZcCB4-bP8WyEeYeKq83ke_qc7LVgMHkgRcByxk5WocB5MwgvxUT1w_eew8wyNeOYF-sTRw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=L-Z1f41JHC7eGPPCrLcnnBfe4J6haI0MttGzDPQAi2ogyvHToiKXqGGi-D835WPqabJ4YaY-k4fFAOLtxY3W43TmTrG8VrWeP5wbxTqsyxTFfzNzy2pFNGCmYilnE-4DOSZBwkI4u6c7iawG-fh5iLoRTvFXghGRKIw1yaDR_o-tlj4PPltgJJeErMk67SLK1A0_QWGK-h7r3YykuuQ2OtBT5ZG9XQkwXzT-zwrQAETjLHj8a7shn7-vc2HRVq--0BgPwY29783b2nwX5-zuAOOYBJsNlXY5iWXPtm1hA2lOTB0pttNPSeyhdPIv7Ka2L5722_zlJ0GQfY8AmPhqtg0V9Lygr8QEgOE3Wkpo7uaJf9jYCX-Ks851Fk2HIHh5xcd5lXYV4jqB6xwPiq6Dr8yHnLwsuSgA_MN7BlaOyK_tugZa7AgtnpJjM9ipOKhWQhvmlLGsCajgpoKSYx84jhIx8ThpsiLAsfGOEMoC9wvlrt6HqsGk0dSTDrg7l8amYt2lyWdTZbHgjV_kDhn35U0Cm77fUl9LCfHZId58t9-A5fGAy0ytA_amwCqhDwVg397ggYcQAuvt__WgGNBQ4gq0qyRsOS-iB70ULl74AvRnzjtGeXCOPHM9UsNlkjLu_x3uy9Bm22qg2jMJqyOSFIVUobk8cqimXuaLUuwEL7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=L-Z1f41JHC7eGPPCrLcnnBfe4J6haI0MttGzDPQAi2ogyvHToiKXqGGi-D835WPqabJ4YaY-k4fFAOLtxY3W43TmTrG8VrWeP5wbxTqsyxTFfzNzy2pFNGCmYilnE-4DOSZBwkI4u6c7iawG-fh5iLoRTvFXghGRKIw1yaDR_o-tlj4PPltgJJeErMk67SLK1A0_QWGK-h7r3YykuuQ2OtBT5ZG9XQkwXzT-zwrQAETjLHj8a7shn7-vc2HRVq--0BgPwY29783b2nwX5-zuAOOYBJsNlXY5iWXPtm1hA2lOTB0pttNPSeyhdPIv7Ka2L5722_zlJ0GQfY8AmPhqtg0V9Lygr8QEgOE3Wkpo7uaJf9jYCX-Ks851Fk2HIHh5xcd5lXYV4jqB6xwPiq6Dr8yHnLwsuSgA_MN7BlaOyK_tugZa7AgtnpJjM9ipOKhWQhvmlLGsCajgpoKSYx84jhIx8ThpsiLAsfGOEMoC9wvlrt6HqsGk0dSTDrg7l8amYt2lyWdTZbHgjV_kDhn35U0Cm77fUl9LCfHZId58t9-A5fGAy0ytA_amwCqhDwVg397ggYcQAuvt__WgGNBQ4gq0qyRsOS-iB70ULl74AvRnzjtGeXCOPHM9UsNlkjLu_x3uy9Bm22qg2jMJqyOSFIVUobk8cqimXuaLUuwEL7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0goARe_4t8eqBMS_W3rj4cxv0iSCNs_3h03Q7MiCSOv5oIS3Dyb1mz1Yulwna1i5jniLQ1Og8vWHoXqy03S2rnOJPJ7dMZgNnTpo7hZPm_xMSmPF50XAPonEzzERgoGkh7ZsCzME8iti-6JwdlSrSFuqquXZRhnzmN1Rso2tgylzg0dVpHsseYotbqqlbkYZ634b_bHm0j9GKuRZP3alMwg8d7eLWZ90as00icXpVa6uavc9k4--drX0YnemOX3aIoiBS83b--37VJ1wlaYkmKHRgM77Eu0u6bMTmgXwOba9WFycD5uIuTAMkjrhu5b2Ca4ot0UEHNKwp_-fYylVw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Ww7iZEgmMGMpohh3jRhUzDsL1FhVVYce9GFZz4hAEYNKckbuhuTA4gCcneaaGJ_mXSmxJBh38SVnNpBZrGtvsapOUMfrcJFMzL7rwDg7vr4Dg4rV1K1pLc9-A66tgD3kxyi_V4rBwwa5eOXjG7khxryiYe0Y4Ak9NKnj4PeMg5M2u0mvv64cnX99TRaJYEVHAbPUdFr2cFllZEBYTJo-f7N6LN6d6_AdAqwjC-bMPHZpyRmkzguK9pFZcc3NeU6QEQYR4kXp_Gqb9BVI_tfHV3vBiYM_XQDa_RJMRXjnTWjw2q0y9TSbcKyKguEARehXhHd9sNwDX3pBj0br0_9Sz4ytOwzkkJwfaFkNXJpiQrwsFG_3XaQfSYE2Bivg8wUmVhua-SHY-hJvNcR6E8YjQeaRb4g4H18auM8vxTd9RBz_y9_mm9HH-iU7xHiKDs4fIdkr-5Wy3nyMJURXzAe-b-KR2qX36yAcq9_yoA4VejtBIY1rDqKjNekiLROf1nWcqhgsnD9yCzTUNqbWF0iH5RL0oTjBKmC8VDnPtkJY8_mFMCzCBOOjE0brbbljSNUF-7tDwQFZ4Sjw0AQGyD7DodfLVG0FSubmn9ET7Wvhjp-yEaKWms-Ta3q5ZcThpWNtAFmFBlZlaGQjHlZrEVBwODADs6WFqWw1zNXrcS0QiEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Ww7iZEgmMGMpohh3jRhUzDsL1FhVVYce9GFZz4hAEYNKckbuhuTA4gCcneaaGJ_mXSmxJBh38SVnNpBZrGtvsapOUMfrcJFMzL7rwDg7vr4Dg4rV1K1pLc9-A66tgD3kxyi_V4rBwwa5eOXjG7khxryiYe0Y4Ak9NKnj4PeMg5M2u0mvv64cnX99TRaJYEVHAbPUdFr2cFllZEBYTJo-f7N6LN6d6_AdAqwjC-bMPHZpyRmkzguK9pFZcc3NeU6QEQYR4kXp_Gqb9BVI_tfHV3vBiYM_XQDa_RJMRXjnTWjw2q0y9TSbcKyKguEARehXhHd9sNwDX3pBj0br0_9Sz4ytOwzkkJwfaFkNXJpiQrwsFG_3XaQfSYE2Bivg8wUmVhua-SHY-hJvNcR6E8YjQeaRb4g4H18auM8vxTd9RBz_y9_mm9HH-iU7xHiKDs4fIdkr-5Wy3nyMJURXzAe-b-KR2qX36yAcq9_yoA4VejtBIY1rDqKjNekiLROf1nWcqhgsnD9yCzTUNqbWF0iH5RL0oTjBKmC8VDnPtkJY8_mFMCzCBOOjE0brbbljSNUF-7tDwQFZ4Sjw0AQGyD7DodfLVG0FSubmn9ET7Wvhjp-yEaKWms-Ta3q5ZcThpWNtAFmFBlZlaGQjHlZrEVBwODADs6WFqWw1zNXrcS0QiEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8tJIzyeePrwfYrL5W_8IWsJn8G5NHsuNEsqRYB_9tqC_sv0Py3ul78bEmKjwHw_UrHi1IDTPzr6QXieF8P7omrKxAUf717BoM6JAzbFNEjoBXLn1wUpnDs5toeTNcuEqhafTvzpVDUzjgfWrFiO0tCm6yfE2iD6YMeynrmv43oNmQHNYDL8iEBm7s-u9gc87SbIIRuenYNmrKCOZyUk2i7tKIVsxaCDJoBCJXwj_QGiH1waH9ZbGT8bhNWjmHGxcZbNHEYUEt62TwVcQzht1-kNSIKxPFMHZl-bNrRC6TwRLJo5IMnaKOs9TK2fqOsO0dufg4xK7AB5_46xyP_T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
