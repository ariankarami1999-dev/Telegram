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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miBEryZsuOE2r8Crslb_UgMIj5UBOh8E--8tk7DnH14PKKZjrz4AaTsfOy7g1vQimhg5YAVJqOXNV2DlPYXBnHpCCrq9KlHssYkH7XPNUXjIaZEKSgUdFU4jlTfFng0O-7RpcYLHawrTJrPdXPwnPXc5q1Lav-ejsDKLMcJrickGF9LBYGTh9GH4_1L33XrpF0eF61m-zGQeb-HPzx5DGElxiNcL7KopY0uUBPSiwE1_0sbUAeF-LkxxKrqkqmDSwd4rIJTePHUoRsH6UoIL6vYfTYVlxeUHyJzMUz4KiJ6_VjNjD54p1MARACAfOj872t9jh0oAfbVtw568ZvTfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=AkYVc5JNE6IkbDhO_aJ5Pr8GjWlONuiOhRE61tCwD-Bs9omUP-hattjk9OhMKUtc73N0d0B3dyYosqMYELNGpqTrZH9pwO43W5On7_wF0DGCAFNizOoqf__RtTM3TRz1p1SWlNSMiwqoNHL-pGeVS7bAtBN29HJsN40eg22ifEy21xvfYzNOpEFAzt0arZPiS-wIKMwg3iyEf7nMqMAKY4nC-ZnchasipD7cvq5ZHBuCxXT7eGStDAfOAUbS1vNgKx8MLlrobtaF4swwLkj1sqD46UbLixll51WhcdSMWR9i7PT1qqjToz7qbThBTJCgdxFMKgXjZPTHq0HTc-Aovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=AkYVc5JNE6IkbDhO_aJ5Pr8GjWlONuiOhRE61tCwD-Bs9omUP-hattjk9OhMKUtc73N0d0B3dyYosqMYELNGpqTrZH9pwO43W5On7_wF0DGCAFNizOoqf__RtTM3TRz1p1SWlNSMiwqoNHL-pGeVS7bAtBN29HJsN40eg22ifEy21xvfYzNOpEFAzt0arZPiS-wIKMwg3iyEf7nMqMAKY4nC-ZnchasipD7cvq5ZHBuCxXT7eGStDAfOAUbS1vNgKx8MLlrobtaF4swwLkj1sqD46UbLixll51WhcdSMWR9i7PT1qqjToz7qbThBTJCgdxFMKgXjZPTHq0HTc-Aovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZUmRoP3hFL3LlRznp25nMjuQZfUnvtHFE2EIhu7uXs5bd82f0GysseEmUhXd3N-eBtfl7unInvctIADNhd4yWo1dTImqD_zdxYmC35FmDQteEWxAeojNgQxt1DtFMXIX6YKLuSEhKU2Z0vq7NLRpKThbaki3mrIGm2Z4zmauoukH41TqEja7gyV5ZQy9dAVQTEoPAo-FRTWzrj6lo5i0aiKzvSuZShmyUULfwsN7LZOAh_cd8-KpajzKyWlBRIT0dE5M87vs9I27JxfDtuG5nE0vM7xkp4Ev2_KEUymjixjW8LEvjahzHSlEHShbVfUgCh-R-Sna55kxk132pynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKrKbCqdLLJyvGUSmzC3hfoiZLxRZ2B8Vp05WS1d4JfKg8ZYv7dPLHUBc82H22Rh53Ze0b_44oP6OpC2xpse4gjxs_60bWltLVP5fCp7XtDjPmCJdmAwPhKL2PtTGwrVqIxthcaK4V_Z8YDKw2RCaWq9mWnmKPbT32tOi3_y1Wld6pgpCrrhVnDD7gK0IxIEVn8jAgghu8gjg9Cxfem55yneVpkocKype0ezE7IoCMJACdv9bl-NSphDJ-a0kv9t7pwR4FfJzlzkjaNtAet4pDJ2U--bS-RXPFbhd6Y3yzsiSz5Te7lWDbucLlYfXOOqJHjAgx7gguFWSmTScnKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw--Vi9BNQuVrtjPJk2TqERD2FWIwvOT_Yf3XQb6E3ELccMkmNDd6bC38Hdx0s3f-_5GPQo3oTRnxdeEW-W8D5fk2RXAGHj4hemW8IdYJC6Hb-5_to699DZZDP74Mj-IUUObmYMN9GLsCt3M8Qa118dkia0W2KFXRgRkD5Aen3KPU7pNGGEjHOYsU612iZ8ePlVp2D6vowNJpcLJ6bvVshMHdRCb33M0bggtiyO4dnkj9-4TXs3MSFPSA01t9f_Humv-MpyGdulnB_YeC-cYxtCaNKNiP2MGhZoi96bJqttFPcD2tAzx_eEOtM3Sg9a78LqJrKnOnOH5ibagJuYSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dNUVEn6JcyaBpHXIvBiJo8Wv9jlfu9pCLJ9huSMRoxZ5KjghsvCIpZ_5-PwioKJ_9Lzg03O1hh0wwbwmLNhFcJJrRpvaNRJynBsKVirwU7Q6z0WCv4aCDrCHyeA6Cs09Wv26pIO_3_v_1svXIf7v2Zk7f0dTGuWsW2-QjfUY4YRqFYti422ajsc-5wdq53la8ODgYh22vSemH7KmMzpLthKlRKljBImKrZ4eA90Nt8viVM34KNgHVGnG3dFi4IkZe8U-Tg19NH6XBUb0ztNpXtrcW-vMWHdky3GKI-unAYO2akApp5hV0rjmHGF-ZA8jQFAWdry-rC7R8wUPUH0DsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dNUVEn6JcyaBpHXIvBiJo8Wv9jlfu9pCLJ9huSMRoxZ5KjghsvCIpZ_5-PwioKJ_9Lzg03O1hh0wwbwmLNhFcJJrRpvaNRJynBsKVirwU7Q6z0WCv4aCDrCHyeA6Cs09Wv26pIO_3_v_1svXIf7v2Zk7f0dTGuWsW2-QjfUY4YRqFYti422ajsc-5wdq53la8ODgYh22vSemH7KmMzpLthKlRKljBImKrZ4eA90Nt8viVM34KNgHVGnG3dFi4IkZe8U-Tg19NH6XBUb0ztNpXtrcW-vMWHdky3GKI-unAYO2akApp5hV0rjmHGF-ZA8jQFAWdry-rC7R8wUPUH0DsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=LCwuPrQVuTIB7bl6zdUlG0HYfKRbjdsPi6oQiJxvR5p3LDfUhIB3Rt-kbwP9kv0YKBY0c7g7OKoTME6iopGUgI15QdW0nL8Y4zMGxed06LEqSCDbj6LpAWqXYgNRdA5_2F9zj0eI8wryEn34yMl1g3KtGUoyZX6mcQpvAQrE7xhB8cs1pg7Ix3v-RRFmimZVSnMu8G9y8zVWnY_Kgi1ZYQV-v30CN_N_JqPqooQZZ_9wtkBLk_CFcc68oeBVFjflg597Qn1xHHcC_D9703363jgcit37EDuegFNNGCu2wMvzsyPr7k5f1Yz-xsGf52_Z7SEHpjUQfvpIHBBWytDjYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=LCwuPrQVuTIB7bl6zdUlG0HYfKRbjdsPi6oQiJxvR5p3LDfUhIB3Rt-kbwP9kv0YKBY0c7g7OKoTME6iopGUgI15QdW0nL8Y4zMGxed06LEqSCDbj6LpAWqXYgNRdA5_2F9zj0eI8wryEn34yMl1g3KtGUoyZX6mcQpvAQrE7xhB8cs1pg7Ix3v-RRFmimZVSnMu8G9y8zVWnY_Kgi1ZYQV-v30CN_N_JqPqooQZZ_9wtkBLk_CFcc68oeBVFjflg597Qn1xHHcC_D9703363jgcit37EDuegFNNGCu2wMvzsyPr7k5f1Yz-xsGf52_Z7SEHpjUQfvpIHBBWytDjYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=HddLJuCh_2ERmrqMFFA50uoobb9X6yXTCIRPqQhPcqrpHfWIxAu724_uCgWqhhz6je5R7AVbUOHihpEim4tSbNp8s11Ded5a73EUNe-eZwrB7rSmAY3e8lXPivyTaM0P-uBJsklksvVLBTpOWvZCe2lEG4pWAM-Ti1lFnwq1QvsDvVzvjEFLl68ymFD1mLE6I_rIWa3Z1PK_Posdv8SK8URzzFQo5LTlniQKGy6AIakAdUF7qCtlYG4ubvx-CEdERhjGGksmRsjws1Eic2pyeIqcCtBOKRx2Uye3oni_4LF1y7OAu-DhqGPocW22zU3jrI08zkQSgOUtZtUYSlk2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=HddLJuCh_2ERmrqMFFA50uoobb9X6yXTCIRPqQhPcqrpHfWIxAu724_uCgWqhhz6je5R7AVbUOHihpEim4tSbNp8s11Ded5a73EUNe-eZwrB7rSmAY3e8lXPivyTaM0P-uBJsklksvVLBTpOWvZCe2lEG4pWAM-Ti1lFnwq1QvsDvVzvjEFLl68ymFD1mLE6I_rIWa3Z1PK_Posdv8SK8URzzFQo5LTlniQKGy6AIakAdUF7qCtlYG4ubvx-CEdERhjGGksmRsjws1Eic2pyeIqcCtBOKRx2Uye3oni_4LF1y7OAu-DhqGPocW22zU3jrI08zkQSgOUtZtUYSlk2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oE7OSd7gTx7oSyQ_zKnpJ3ziK0iG68eePTporant8J9MBCoFIwMsYtgwLTGbjqPC3q5OLg3cXdb5PugMmyzekKzi5kAssL3u2vo55v2PwSAQoxOXe3g_phiF-KmTa1k7U-sZ7w94PLZNsKj2NSgVB-fXqBPaxxjBtfjCU8_CU8ZrSUuXVpBjUOJCojQ7NqtDdBvm8KTgA_rH1Q_eOzMOjM0hjEPDDbdfzJrYA8-ThvegWOISWQrZsQcjDdXAhlmZgGZLmhq4odrJUdFbQdP1zZKdnASIB8nT8MhwdTKK08c7-Z4jLiAuJKpGVtPI7zwzfnnt6idwS8IV0BmyZO2gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oE7OSd7gTx7oSyQ_zKnpJ3ziK0iG68eePTporant8J9MBCoFIwMsYtgwLTGbjqPC3q5OLg3cXdb5PugMmyzekKzi5kAssL3u2vo55v2PwSAQoxOXe3g_phiF-KmTa1k7U-sZ7w94PLZNsKj2NSgVB-fXqBPaxxjBtfjCU8_CU8ZrSUuXVpBjUOJCojQ7NqtDdBvm8KTgA_rH1Q_eOzMOjM0hjEPDDbdfzJrYA8-ThvegWOISWQrZsQcjDdXAhlmZgGZLmhq4odrJUdFbQdP1zZKdnASIB8nT8MhwdTKK08c7-Z4jLiAuJKpGVtPI7zwzfnnt6idwS8IV0BmyZO2gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urX83ahd_BSIa3_WsijqdTvOHobWQychuMjug3Yi10saMt5GPlCO2bF3zWXB9gkYb5ChCtQAanyzxI2uG-ckLYJ4akYMCczCeFRTlP0MEFxZNx2fbp2zFWM9A50m__HdBlc8MQwbreDJ8b5Uj_dKTwM-jOA0rfKOa6ctIU24Mx2EqRu1S6xmz81MZOLkPgMUkVzVl77CVHpXm3LXzL4O_QYRAhEbQ7wkYl3mlt4qlRqk6ulAOkyTOF_QHxW5W95hj2fPmfFtCUZqvZ5nXGwqv_PX54glVkvXNRTvftGShZAUK6Bv_2DbzJ41gxDef4DASSdrn1nM_hywnktyU2F6Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YSwJI5lETrF07WTyF_Rgxxr4nSCIOdT2nhO2Ke3UVPx5OXM3Hy3VGStxRmIX_t4BS0pm9unfPDDbv0WYlNOhHeXk7QoqyGykjXR7pqdBt5wMxN4S3i4V3mPL3qDzVT3mAhuqBIlndWLQpy6vV8Wc8QFhHmg53G6dIzYJjbA69VaBeL0GjRY2VMWM8Tkob8u-qzkhGQLGSWf8WtvuJ9ysiOQy0O39qCRNw0E6VtQ1jpXpwSPWO2FDmC9gKuoqlmwD8D5yAl9JtJnwCIZIbxqmxxvA0Ou28XIFAu0cMMlhoC7T-XpjUqTfcecJ0ISOyUBxZhrZqXmmKgJNeUf43YOzCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YSwJI5lETrF07WTyF_Rgxxr4nSCIOdT2nhO2Ke3UVPx5OXM3Hy3VGStxRmIX_t4BS0pm9unfPDDbv0WYlNOhHeXk7QoqyGykjXR7pqdBt5wMxN4S3i4V3mPL3qDzVT3mAhuqBIlndWLQpy6vV8Wc8QFhHmg53G6dIzYJjbA69VaBeL0GjRY2VMWM8Tkob8u-qzkhGQLGSWf8WtvuJ9ysiOQy0O39qCRNw0E6VtQ1jpXpwSPWO2FDmC9gKuoqlmwD8D5yAl9JtJnwCIZIbxqmxxvA0Ou28XIFAu0cMMlhoC7T-XpjUqTfcecJ0ISOyUBxZhrZqXmmKgJNeUf43YOzCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=WbK0WIe9L6Twd6VKS8v3xlLcRFPnmg7TJurrhniKSu5mpxrSyJaXih2ZQHXSuVxbwUIN-Sg6DzAnW1TD1HpEnJe46jrxkJWeRV9IvDAhOP0MuBKNXwXmKol18-Z60Qux8g1Hwo5nX-AzpTsAR0oVEh4qQPXHGopJisVtt9gu9VaF9Nxi-E5vO90v4-cwq2YLpZv53__m0oATJyYuObR1hkVKfAJ75CunKLElFa5Rpi-4WPJrKIAz8bLNocYxu7ysGHw97GN-XM2PKYwDMMmOCv01ZW4JD7Hay9yl-OEfI7vvgfGDikGo-cfV0mwxFLzkr1iCsHXUC3rqhmmv4PhCRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=WbK0WIe9L6Twd6VKS8v3xlLcRFPnmg7TJurrhniKSu5mpxrSyJaXih2ZQHXSuVxbwUIN-Sg6DzAnW1TD1HpEnJe46jrxkJWeRV9IvDAhOP0MuBKNXwXmKol18-Z60Qux8g1Hwo5nX-AzpTsAR0oVEh4qQPXHGopJisVtt9gu9VaF9Nxi-E5vO90v4-cwq2YLpZv53__m0oATJyYuObR1hkVKfAJ75CunKLElFa5Rpi-4WPJrKIAz8bLNocYxu7ysGHw97GN-XM2PKYwDMMmOCv01ZW4JD7Hay9yl-OEfI7vvgfGDikGo-cfV0mwxFLzkr1iCsHXUC3rqhmmv4PhCRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve90TCeiCUB2nhWNhaVC-uNaYmZSzW6cFXmozBCmXSAFRGfaFiDZAyHeVu4ls_pWGqoxU0t5SRPFeBXrcqCf3zM8eoX40VLs2dG860E1CPzUnyh5OrhQPOn_9RvVx7JRhxCGrJT3KwRd-txZuTdEElGEIDvuJe6iku12Ht3wH-KDpO9HD3WS1RzBBkXDRZc_lezOttuCpHcSdRj10gg3JCWaGrqJmcZPpOppVyAh9QV2AgolYFoDNDAwObEINZfd0UQPk-u2qVt06o0VGZlBL8keZlxAhvqqWySu1kDm7KkHwsw-Nya4ZFxcWG0CC17xQWkPCN4CpJCxmSuEZGPqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYp0_iiYBP3nId67532LzB9UCpOnP353Inuq-JLGnm62dD2QhlAARsAdcyZenUJm6XGr8T8ltstDW498kitnsi-FLWUzbMGJMxv53k0-iA8akyYJ08yxaDxhEmef3p56Y-9r7AvrcuVKLYDpnUxRXhzo8etPZ8TRhbVMLp8Zah76NSmXar8QH5WmX2ScYKZ0iIoCb3yWVssyY_Elo7Vm6DJ_P2w1zhyaCOThboPZtLlerSOH12MbTIsvKreteRTsTE4i8-YGpSiFZgyAVD3N8DpqoxTKjVJqMsCRYFVjJqeTguH8QbCD2F3VxuvG_kmKu-JL5TZ0aQmlH7bZOMCmRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ls2untFr3Fk67_yUkTtxMDdEJ7frDCiBKY5nrWBtVbQooB9zdl78C-KyOe07CVa6ZAHMIvrqeEevs1GXPdfX7C1w_A-55zbBV0Jw-gEEwImhuhtkLJIXs0h0dQGPBVNd6YodKXt7xIBwLauFs63hczWQKdN_AYJ8oY5f6yrhwSkcn_URlXE_j90cU_T4OnUNpOSwF4rbRWTc8noMmYRuJAJnP1kmPRVZt2VldlEBU3qP50v7VafoUYeC9jkxlJDBB6M2O4sa7UN203boldzcAdIsneIH5xZPcrfikgKQaI4YQcgzIiQQqZtClHVdDsvxAGMi75wKXrz17qQD6dsx4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ls2untFr3Fk67_yUkTtxMDdEJ7frDCiBKY5nrWBtVbQooB9zdl78C-KyOe07CVa6ZAHMIvrqeEevs1GXPdfX7C1w_A-55zbBV0Jw-gEEwImhuhtkLJIXs0h0dQGPBVNd6YodKXt7xIBwLauFs63hczWQKdN_AYJ8oY5f6yrhwSkcn_URlXE_j90cU_T4OnUNpOSwF4rbRWTc8noMmYRuJAJnP1kmPRVZt2VldlEBU3qP50v7VafoUYeC9jkxlJDBB6M2O4sa7UN203boldzcAdIsneIH5xZPcrfikgKQaI4YQcgzIiQQqZtClHVdDsvxAGMi75wKXrz17qQD6dsx4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGmmQxApkxND3RC9APRVo_ncxe9Bf4QdCAPh5T5K9ht5737qCuKffc7GPnyYE2_zbepFtD3coSsnYD_xn99oXjxB7BdfPbGxTrzTPOxH-XQi_lQZF2fGAfZsVyzhVBT20eVs8jz-l4aJ2_XH407_vI0WGEGLTD8Ap3PFO75ISfDCqD5XxOVmWdk0Ys3Lw8eotNTanmuQWXcXkdcaslV7jblgs65OADHKC1uv1c2rd2gVCJCkyTSWSOKbM2RTczKCVFXTh6-9sY6n3hSUqXnwm3r8BeyW6c28ER1pHV34sVMWZt675kMysiEoLlKl-u8ouWw0qWk62dKsOxezX7vANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL4NHVVf2sgmB2IpqRPaov4ZD9oCmaMxmx4ub9x9gR9cxpum34uTk_JUL9lcnhM6wATk8JvVvdVDDeGzL7SJ2w8JDmx2Da02l2TUi4St9JPL5FfY_riSMqixsa0J157NHHl9ZJ_CeX0GJLaGPRUmCtz3m3SRz78lU2ADqkRpuktqyqL2lKAh4GMqRPTnsy3JFI8dKoIRJwzGHXQbdp-kI7s9qwwqjcxLX-GkhhyGnmw-K5f_fRiRb5iyrc9DncOcQ1DwwytoAReOT3hnIRFDBJCuF5PDeEHtDb-RNW4azha1q8gbqacgdxEB-2wjgT5-KgXlq-wHD9M1vvt87bFlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZ8rf1T1h8pgUT03P3UtO1msHd2WuCSEHOIFlru6H4CICjX7MeL4WlgMiDdgK-qzEz9JkTsL1b-w4obm1c-kU25Pi5l6MeuGhKwHyCyvNQLGkiuqazJga5igFBk7WXShAN-w0mBsVb85-20USRzeQNC6RLX1lhhzdjjE7eANT5x801mhbkbOhEemmEgSulKQzsaUdTLnOAfl1hkpQt9mykEyIbubC7MHhdxTEcE96ebG4hPhFLBN_iQDjK1wiXfXlTNPx0wf5Rj-2_aVX-y-NVWkRThxVs5zZK8eKBJkAM571eLESzQoxBzaDwpAXFXIYOK0jDhbk5U2y1Hej39dOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=RBuyDIH6F5_dVLnGnm0exIWSJ9cTenM4Eo_Pqunk_Qh1UTrGUO9wPCttEhjL-IxIrUZZQue8mqMDuhzAJ4U16T4KdO17LFZqiaFZHfNjwFj9X6Z0x2jHe9ntkq4zKmBhrN-JEo46RMDNNSCUSiVhq1B2bu92jjbpk9lXtM2Sz-9zZTOmN0vTvIax-ggy4RQfsB6XNV-qZxiTqrnt2vOdaoYLbxFTYbp6p1TN483cFqIHBONNSUIj5CYt4FpAeVkez27anXr5tUy19KsM1KRDM2RngjAnVentAdf-UYVYVES6xFDw4o-ciX4SpbCCLhtgFATRPdXzBi1Jux6nctSzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=RBuyDIH6F5_dVLnGnm0exIWSJ9cTenM4Eo_Pqunk_Qh1UTrGUO9wPCttEhjL-IxIrUZZQue8mqMDuhzAJ4U16T4KdO17LFZqiaFZHfNjwFj9X6Z0x2jHe9ntkq4zKmBhrN-JEo46RMDNNSCUSiVhq1B2bu92jjbpk9lXtM2Sz-9zZTOmN0vTvIax-ggy4RQfsB6XNV-qZxiTqrnt2vOdaoYLbxFTYbp6p1TN483cFqIHBONNSUIj5CYt4FpAeVkez27anXr5tUy19KsM1KRDM2RngjAnVentAdf-UYVYVES6xFDw4o-ciX4SpbCCLhtgFATRPdXzBi1Jux6nctSzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=HmDJwHC_jqTMqh4hVsBr2hDTwNLzWkQ0ShKT5LO9d75IMOaOm8CU2v9T5JAMiQJXmha8AndhWAIMl1EXhf81N_LzMoUey3t--R_BubpKHroWXmpNXVfj3UhoB61eBNKnDvVOybEDMW3Hk0u986lDfCaQUc-cviAoPdukoYKgEAYbGefhBGBrzTMazorYLJaHf5VtGUcnMNyBd2eXWTUK1TinSB0iwKEzJxzChNBBlA_g__0-TqzNzmIfrbutTu4bL3AE6CSHRTiZebxI85K-ozbLMNa51TJp8ic9MjcpxLvNLkKK2iC_VXf69OkNKlgvL_4P2ft2da6d47s76C9_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=HmDJwHC_jqTMqh4hVsBr2hDTwNLzWkQ0ShKT5LO9d75IMOaOm8CU2v9T5JAMiQJXmha8AndhWAIMl1EXhf81N_LzMoUey3t--R_BubpKHroWXmpNXVfj3UhoB61eBNKnDvVOybEDMW3Hk0u986lDfCaQUc-cviAoPdukoYKgEAYbGefhBGBrzTMazorYLJaHf5VtGUcnMNyBd2eXWTUK1TinSB0iwKEzJxzChNBBlA_g__0-TqzNzmIfrbutTu4bL3AE6CSHRTiZebxI85K-ozbLMNa51TJp8ic9MjcpxLvNLkKK2iC_VXf69OkNKlgvL_4P2ft2da6d47s76C9_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=G-P3MNEKuu6GYByX6h_WdEAzfvAhc-HYKgvuCH6nCRLwz8tM7GpxXVMmtJhnqT3pjrUtH5CG8DTED15SHEE5FNq50yM6RZ7iWQT8vldGenay1y1YhYQTo0ljii7RGPsuh5c37iULjtNMWIWj5KYDicRGad2_5lyqp0QT3ePfoXWwebQlNj6uPcZnYCciwSSFa1IV4hk8PBImJeKXYjnKxHPOjXAjv3BheZb87eUz06_VZxvPugjnAujFMrnXfjZfrepTGRmjNjGrtyfP51IHLXb9cNgByhPYe39uO68UMg_jfhcMKSdZInMDQK2L7xG7kApYEPWQ_b3VxaDDD0Zt0gAx7UzhVXgWEmryWRejeJ8ODpqCyfUw5bzWdd2QAt_n2VLgaa9vEgoxBB40jGcAMM-urSCpCLSj7tv4GnRGnqwzo-mmY7eLQAf4mAqk4WkrWkLmHieKhgFCS83yOoUtDXwIIpcrvBRHOaoIykFz8JodDiDNynW5CCEDgjbpAjJrdNyJROoeQmbYm7jkc9VfSYKz7lBJAmc__F06gBeOmHsResRn504Kgm0DlEhqNoPzQJJsVLpuuQAMRASaoEpTq0VaigqN4xaMx2okGED2DDBaXkY77hA38JgH_JU0Z0jJ-HUUdLz6VZ4YkeESYSgi78_1AkWoq7FuCmUCD8BFVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=G-P3MNEKuu6GYByX6h_WdEAzfvAhc-HYKgvuCH6nCRLwz8tM7GpxXVMmtJhnqT3pjrUtH5CG8DTED15SHEE5FNq50yM6RZ7iWQT8vldGenay1y1YhYQTo0ljii7RGPsuh5c37iULjtNMWIWj5KYDicRGad2_5lyqp0QT3ePfoXWwebQlNj6uPcZnYCciwSSFa1IV4hk8PBImJeKXYjnKxHPOjXAjv3BheZb87eUz06_VZxvPugjnAujFMrnXfjZfrepTGRmjNjGrtyfP51IHLXb9cNgByhPYe39uO68UMg_jfhcMKSdZInMDQK2L7xG7kApYEPWQ_b3VxaDDD0Zt0gAx7UzhVXgWEmryWRejeJ8ODpqCyfUw5bzWdd2QAt_n2VLgaa9vEgoxBB40jGcAMM-urSCpCLSj7tv4GnRGnqwzo-mmY7eLQAf4mAqk4WkrWkLmHieKhgFCS83yOoUtDXwIIpcrvBRHOaoIykFz8JodDiDNynW5CCEDgjbpAjJrdNyJROoeQmbYm7jkc9VfSYKz7lBJAmc__F06gBeOmHsResRn504Kgm0DlEhqNoPzQJJsVLpuuQAMRASaoEpTq0VaigqN4xaMx2okGED2DDBaXkY77hA38JgH_JU0Z0jJ-HUUdLz6VZ4YkeESYSgi78_1AkWoq7FuCmUCD8BFVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LrqI2z_-NQhIiTxm3wB7t2FkZiRnVSvPjF2YnFKEi74Z7UbyxQtWHxqkaCYRDrorajy3bIb2-cGAmoIF0Nd7Q_SzVUi8eEN17eYCskLKnijf8C7K3yOOdegOfrMcubanLI9MkOIpvZ-aNXreCuKeb6LtX7LDF-ANlE8HQbRAPr270Kd2Sv88OlZ6aGT6NKnEVfVAiVDuAJjLqU3YGEk2FDOAr6Qyj6uqcNGlCBeqqe_9tuQUNpcE6xe5MQbUfaXnIDKH9pYBHvOhy9C_Az8Jys8-3PS5M6Xord6X3Fjjf3Eu4zmqe3PeBTdEnBFGU_MbKawJBiEYbSFW88XKYNDsDRxbOxYd2nBPcEmQ7Xmu9mgDIXDO2hXZLqORSWCsTSKTjgdtHMLVVUn2A-XR5HrIf6I-YwcW5wzhQJk6BC0HVeoN-wgLbkFdjnoN7L4qpFXmgEhKznbwaUc1SpRhHLKcogkHlZ35iL4Z5aMXvokV2tuuN8UUCWl_ZNmmQCctSkWnnXvzK7IfxBxkdrPWMFv2_PmDsntyh8gIZb2y8JJsSA0CqvxGp_KIQ7BgHEPogjfeqPGY1wXnObNtky4gNm8OJ26l0gygrbxR_xyG18lDa9THrMVNSs44YaBf5rN95k747HBGzYjbK8WgyzU33egnWG0f5XFyPkpAv32XqtVxIAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LrqI2z_-NQhIiTxm3wB7t2FkZiRnVSvPjF2YnFKEi74Z7UbyxQtWHxqkaCYRDrorajy3bIb2-cGAmoIF0Nd7Q_SzVUi8eEN17eYCskLKnijf8C7K3yOOdegOfrMcubanLI9MkOIpvZ-aNXreCuKeb6LtX7LDF-ANlE8HQbRAPr270Kd2Sv88OlZ6aGT6NKnEVfVAiVDuAJjLqU3YGEk2FDOAr6Qyj6uqcNGlCBeqqe_9tuQUNpcE6xe5MQbUfaXnIDKH9pYBHvOhy9C_Az8Jys8-3PS5M6Xord6X3Fjjf3Eu4zmqe3PeBTdEnBFGU_MbKawJBiEYbSFW88XKYNDsDRxbOxYd2nBPcEmQ7Xmu9mgDIXDO2hXZLqORSWCsTSKTjgdtHMLVVUn2A-XR5HrIf6I-YwcW5wzhQJk6BC0HVeoN-wgLbkFdjnoN7L4qpFXmgEhKznbwaUc1SpRhHLKcogkHlZ35iL4Z5aMXvokV2tuuN8UUCWl_ZNmmQCctSkWnnXvzK7IfxBxkdrPWMFv2_PmDsntyh8gIZb2y8JJsSA0CqvxGp_KIQ7BgHEPogjfeqPGY1wXnObNtky4gNm8OJ26l0gygrbxR_xyG18lDa9THrMVNSs44YaBf5rN95k747HBGzYjbK8WgyzU33egnWG0f5XFyPkpAv32XqtVxIAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=KRqaxfl6cQ-EG0LmKeokL3-Buin-MnnXtlXTAtekyr_8UBZY76TV6Izg-XTACRT8PiJIe75e72mgcal1uE6gqIJ0Nov-BJi_PZGUqHQhUR_FaDj0cIDCJmBRtBrMBKv1vuAEAcnY8mx64-J38fcESnx4b26qQLtDkXteByJRk4fkrL_uNB0AD0Ta3uxQfxbyGlqFwCLWK6B9QummyZnS_IO8xF6uSkWwxNoy_83Gg4Z1U0EAVpGta7rr7QsX7os5260Yl24zeb98hHsV1AXUafiVosnl3xM9btviwMFUv8_6wYcyNa7_Y2qLzIDqoUeeaijAAT4cPBwmC9tAmP-7PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=KRqaxfl6cQ-EG0LmKeokL3-Buin-MnnXtlXTAtekyr_8UBZY76TV6Izg-XTACRT8PiJIe75e72mgcal1uE6gqIJ0Nov-BJi_PZGUqHQhUR_FaDj0cIDCJmBRtBrMBKv1vuAEAcnY8mx64-J38fcESnx4b26qQLtDkXteByJRk4fkrL_uNB0AD0Ta3uxQfxbyGlqFwCLWK6B9QummyZnS_IO8xF6uSkWwxNoy_83Gg4Z1U0EAVpGta7rr7QsX7os5260Yl24zeb98hHsV1AXUafiVosnl3xM9btviwMFUv8_6wYcyNa7_Y2qLzIDqoUeeaijAAT4cPBwmC9tAmP-7PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPHEowj_sWynt-luQpSuiMCQpzkyAxArcuKE_lBBgoaD0VujGUVKozMcbIMHEYJnTaAvLz5Wdg9hJjXJoXxaZ5ldZ7HjYt0uUwBas05936rAmLC9lLe-ZNxLyDGZuMIeV6VLZxvPsuQlGw0Jf2yUgqzrkhFgB_4yf2yk-HGVXpf196cVL4PGkPjqp2NapqJE283QaddCJJN7XR-Ts-1mvnKWpXi22QrttzZN5tOp6aLqi9ucg6HSGfPsbjc4VZIltto2Er6c81Kp-vXtLNj8Cwn63Bi-pB6AU2ah8xTyVeND6FY2-fIAfKUISfoiPN65VQ0POaHmPfA_6ZWym_i66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=WP-FYkF5YzKlq2a07Kdnc6wtp32GNjdRMUlCu7Y_tUXv-cPXBWUY0dK2DRF2veJ0cOmuTYuHpS92nyIXa85VR4NWZSfEr-68140vlV55H53z2HoW1b3NOElFoOvHIoPehXKKiHIsguQ7F0sV3zEn0QNsGMOz6_F2TYrv5_4n1B7rr71GbObfRVH-WdVPj4n4g6JoCXDrtGCejSSDa8SL8GYBDHBpz9JExGk0YA3PKTSnegs76siNA9NyBQ8NTVxFkFqBV70IHb6qGQ0ALbzfLffowYOTBtOrh4T-_Er5hCXw595hqqlxWCwk8A3ESiI_GYVrUJIuv2Ya3Dt1O-LEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=WP-FYkF5YzKlq2a07Kdnc6wtp32GNjdRMUlCu7Y_tUXv-cPXBWUY0dK2DRF2veJ0cOmuTYuHpS92nyIXa85VR4NWZSfEr-68140vlV55H53z2HoW1b3NOElFoOvHIoPehXKKiHIsguQ7F0sV3zEn0QNsGMOz6_F2TYrv5_4n1B7rr71GbObfRVH-WdVPj4n4g6JoCXDrtGCejSSDa8SL8GYBDHBpz9JExGk0YA3PKTSnegs76siNA9NyBQ8NTVxFkFqBV70IHb6qGQ0ALbzfLffowYOTBtOrh4T-_Er5hCXw595hqqlxWCwk8A3ESiI_GYVrUJIuv2Ya3Dt1O-LEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LVH0quBg1bs6oYDn8dEAXPGEYSvc27WluEO5TSVG_g48qRGkqlRu_caCOaUV1sAwTehO-t7zOTUx4ZlOgIAKo4Y7L6jlKi2pJJW_YIV9u1jwdHm8scpIa3y9xyGFw3T1zamnyUpCEwCPWcXVMr5FCYwMd3TC8kzG2R_rNeIlvuXvZhWiuwBIyZJG4txesyvLaDm88-LqLwqzpVKoBV_jDGVqii1BRsAF3MyFkQckGjcmmDXwaRHuahGTDYWS5sG-mP4uTVPYAJfrS85F9aFa1pJUBEFH-4HlNdEhF6d22tRPmHRcRXpK6Gm13uxt3-3ie167rq5EUEQefdmQvugxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LVH0quBg1bs6oYDn8dEAXPGEYSvc27WluEO5TSVG_g48qRGkqlRu_caCOaUV1sAwTehO-t7zOTUx4ZlOgIAKo4Y7L6jlKi2pJJW_YIV9u1jwdHm8scpIa3y9xyGFw3T1zamnyUpCEwCPWcXVMr5FCYwMd3TC8kzG2R_rNeIlvuXvZhWiuwBIyZJG4txesyvLaDm88-LqLwqzpVKoBV_jDGVqii1BRsAF3MyFkQckGjcmmDXwaRHuahGTDYWS5sG-mP4uTVPYAJfrS85F9aFa1pJUBEFH-4HlNdEhF6d22tRPmHRcRXpK6Gm13uxt3-3ie167rq5EUEQefdmQvugxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbBIfmV7QQpJJjSzi6COzcDX0DIy1KiRuhCnsMEfvTGi_35N59gJxejQ0Hk-JTi8wdw7mF1G6u4QUU1HmbKaQpNPVWyeN8cYdzQ5Y1WGK8OQaUh52tMp6Po78XNYOyFvBddRpOFiVWr_NoNUrdI-Lw7r9GDe9WC8PuSUffAWNSA9Tb8q-CPHoHL44pmwmZwzgUJ9rHGxts_WmMMNhvqF3MlAS6aMxpzUxdDFXk2ZMRDHjjk7R3t_VmCZudBsOipESqFGJY8Dp40ZJGmV4-9GNfFXFWOAL4X01rfl0E2Ztc-UKyFXS-dIhu3uZXT1LQSTtf6sRq48NSecjVCssa_3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHy_j52gWN31lEQysNN4boGWhy70hWAbbqkTWlQP4sBfH5NCmEl01j1yKavkISYsxQS-MxcmY6zR7ELSot0k-KRrn0CM14Rqd4zMud-lw3mciu2FRiX7nfTw2lxV851kY4bDXtJsLdFOZZ6H7vvS9I_sz2w8RO-zUcVBqy6HEgcP6v7F9ssaBUNgrEb0Yh5QKn-PZouvwonaRYH2qq9DwzYttOJ3dUOiamByfd7QGjTf8uzjSYKUWRa3ovFSLhXJn4oW-xtLaolvQ3dtbACOIVAHCGiWjUnppiY7QTMsKs4Mx03mkiH72GvOwZr8SKh01ILbuNtWr14glOrk0vj8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2kjWJl097jYALZK32e-sBG6UofCwzOM9I6S4h_VrcirJQuJpEXgslnUnrSfQLu5si5TZ27N_byI2SDFc75U7w1ssKCss1YdZ2ZLFFXmAYG3Y1_BTyLAqEu8Zeb5jDPjowUQnA5UTWuH_qMSzclt7qHJZuQvABuPw4g18dgvCFpdToy3WLa1xn0qJqRH6J7zXmCfvLsGGd8wELSv04N90G3aYwXwRmmUIVIE9gGv9Vqi6xVJyvF9sbSVENR6O6u37TrJ1VO5crUyUBNFoNr43Xl89ilXZ6fFrfXLpeaaDLoTp6nvXeQvEXrBlHYNDcPrIW2UBr6oSDsvyyEBXOTQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl62BmpCiD0NmBP7NvTmQQpJJKUqWxNq_jm1oBrPNKchWATuQsFLkbuESDcvL1zE149expzzzDImiPfi3QuORKhO1BrslqOsd-j9V3T0Lge1nf78_xn-wZZqoAyi1roBgU3XZjBPfWmTENPKkR07bTSgkzyYfB_AEeCnaOypDDg6eJMn3Tt6wBwXqL0ZKeSlhOwhAsp9erKxB3ifE92rQoeAS-IWpWAfp9onbfK3ebUWwhX0OJAYMkL5TrOYF2KjPECE9DPwrOMWfNDL1yfxbpol0AoYhgn8zVjOcvG4zMj5_sDKA3gipYUJo-HzWsi3LP8qs4YjBI66Mc_1H8jK6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vktclwXx3HpEf2ZE5aBAraMdn096kD2l62mTEeGDMvU4c4Oguw5OxLfBFamoyf9SlmnZBt2HaiC4wJ3Kz2sPwfT4sxZqAGIzaOyCQz33Lx5e00Zku1Qow1YgW9QqlGLScNietTW_81QVlLDwL05ZiOCHmu1E7QilONxRRymtBVoih1c4vmCgWB2RprXsOHyXInSVwH3nM8RALZFbZT9YBchBdfJ4PGPsdmHRpBhN46hzuTfLQ1puYL50uWTs8Suzrqi_fKwMyJFKr9NjG0xM-aiFhpsZqluA8YEapnqmLfzJQaD8ELGuZjSD1gUFuKx-JhOZLLrvcn9qSKDWMMuXMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqQMvlLBzcVS_ee5sUuVJDywPLZXu75mXO0uPWsAY85VIibjaBiD51Du0I-pAmxbL0m1CesK_WUGQpdxmtwuoAsChoTzRz3UOqW4ZxQzxWjSDI1KqbdqUVl99fuPFg9qXJO0I2SeA9fThLCsdilYCwl21DYc2WCmfdLBpntvb3UzceAAaWkLunOYreCB-bDXcxU6ikPNsv-NHwKKZArZmInOsfhs3LZHfxwlYnoIPJGpN8AWvB6TgN8rTi3NQrXAYSWjOB-FANSdvRKwkH3F4Jq2te1SHfSAyT5FXOqpX4I2Y74J5Gmqzf_b503y2j03REJViwH-UQGZItCZE9DEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czPAKBAQVc_sgFAeg_fZSOart08LlJSGzu6Gc189Kfq_qbCTlMkCQoVBqnrEQY0ryqiGNn3l1mkhsi4oO7GbjzgHpbflWf6SJEU_5NKFdUBowjyD8-dO9QcyPmE_fTj3nfa5Ekwx8miQSlkurwV4kXpF4O69Xpw1Tw_JoL39wNdEZR3Os-pkA-LtrdAlR4bOPmWq-HZ8eWBUhLZjONNBcxCIrhtEz5LasjI_ZCHoCOw6aSOVBupIL1vEvz4VcU8fR8RDYmmywNGPiiFBByhm8vA3Hmm6KyyTUdQXqSzl1gmTy161m1q8uhzPYhFxg8DpjNEWtHUewGyvx8URiKTyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceqrsDyldSPc-6R9qlXyjAKzdviXgVVdcmEZiLwvs1JIkVgfSLIWP_mq4S4aq4so3MhXY7hBceLTsF8c0xcJbckJx5wtiSlCcg3fwU2fsEhSuZ61zAoJV_OFUdJZ5FJ7zZasUgffxkhneldqD5gKdgnjqnc7hUIjlAy_AD6FruEiA6olTIT-nAMdT1_rD02_ERw2D8hwgYbC59RMGLcUrU1T-djhVwF1Y4hpjAr1g1tzB78xphwnveVWHvs_SHQcjFGol8Z9IFbgMJmt6C_-sQpx2IQnl2xu_lFtiwNxnUYIgYE5nOrFItMKa1b-JpNfpvXrcn7WtUXrDDwxhaXJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxnafeTtFUgGfYguHYSQFHxItYcSsI1s6PgbjXCJNScNwgh1DnA92lIlaPMRa-KyqGIWwAJBbFxyT56Q_aX5W9af2kmntvjFS4Ndd9Ni1dlSKQKtMa0MgXqUkZUFS2eAThth747cYQUQ9uCrQeZE6Sa-anp5qUpjP-_35gUuuAlbz9VfvzYtBUid2ZTsO1fQG1onPmUm3I64P7jWm957xf33bF5KbSdMp4TMZqI-3KxCwKHjYAPfzbiBkjCigxcvcymKBXevfQjXk8PAs_UccUwQaO6R9Cd-Y0j_KNETNbwDuDcwpZP0qZ61ZcptwhC8HYEi9ksfBEpFTUyt041Opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCpqUi-Mt9HKRbQ1u0h1RcaF4D9PAET_o9UFkFa9Xyvd7MtKQCJo68nJEKLIGUIS7A094FfNHg3tIIYmfXFz5ROzntgE-QCUXBEa0CIExFzLoV-1dmAuTuHKFbUFzgBaQdkAfe7LUY_yySQLvT6vzu9xRpqfl0eHiwy_9E-DO3A9IE1RnHvGo1Mix_sR5JufGmwbTP6iVWvc1JeaJ9DWfGnaK2Y0wGEQgwzDPHb2voQ3Lc7pbiNK0BdEsNeT3X5pSdiAMaXSziyktHSCOkpkYcSlIM41eELpv1_GJzdSJYHe47e4ygawd574-837g7UDsHUXyYfr9PDQt0uBxFQ3hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XdW39yKKOFdyUMYyLs2qzq6dakCBPt_8PeXIXsDabI3lrQ0A3_C3e-ozr0vY60dN3v0OaIfez7__EljW7YS2xAc0fHkrO1G0mcSNrQblzZ4_zD3Wm7EtuGJJJ9aTiTUvcTGWfCOkD_Lg5DOGJQFrcx3lLm828u-ltlZ07RydfcPFtaXOE9BD9AXwkY3qIKVWOA1zDQllgGtNYzReQcOZIlUpsIIps82RMALJl8O_wQikp4M5F3tPP_BwK1zaO0RIkyKCog1l7ybHmc38WmQMgkFvjFkhguQMBR89TL5_7V2xnFDlf8rHXuyNXJRA6BC1KRiFvW9cGCQ5O1RMT1sHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XdW39yKKOFdyUMYyLs2qzq6dakCBPt_8PeXIXsDabI3lrQ0A3_C3e-ozr0vY60dN3v0OaIfez7__EljW7YS2xAc0fHkrO1G0mcSNrQblzZ4_zD3Wm7EtuGJJJ9aTiTUvcTGWfCOkD_Lg5DOGJQFrcx3lLm828u-ltlZ07RydfcPFtaXOE9BD9AXwkY3qIKVWOA1zDQllgGtNYzReQcOZIlUpsIIps82RMALJl8O_wQikp4M5F3tPP_BwK1zaO0RIkyKCog1l7ybHmc38WmQMgkFvjFkhguQMBR89TL5_7V2xnFDlf8rHXuyNXJRA6BC1KRiFvW9cGCQ5O1RMT1sHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUGIKBLdfVpfePvwQUVNCLmQZHnF2JEQAH_oGrUQl6yJgW69VhYFiJJALNBU3FE6pbhsnYTbi5SC-hLldSjzK-BstJCbatnoZyuECI1CTCiVZht49dsQm5E4IkT3ABqC-tfzXyZyilIe59U6ZkFPu9stmDtPziu9cKe77LRaUeZvYO6HTdJknjNPOxgEh_BQzBEoWmacYjZsD2jmJum6iMr3S4mTxjhCjOUGx-xIxxpwgxkLpNFS91ko90X0dTYLF2NbBpH4MJMVWcOYByCNZu-sN_afh4RCfKRDmGRzQzSxYXxTQrMHLrgU7Jc8VhqIQUmHPpWZH_YJmpnCF6Ev_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5gaIxbbUS--jOLqfe67fAXFaxdfWbZ6cgb8dJZLppSvhmdz6x0upuYJHrKEmmh3yXoc5owBK2xnKxLi6PAN373jdZtDe7bzeYfL1Ybb2-r8Kh8BZ-VxkyZ-k0_hggm7xA_ciT0dWUpN5-Pm8mKP2nPgvVVLagiHSr9VLnFIPDlxUgkVVRHSpKyaxB71hEjlmrh5xp66ieZJoTUD3a5TsrkJEQH_-94XIbjGeg8a4wAhD1EdYw4M8_HY_wiTigC2BO-Su1sW3QpH_CWbP4W53uUmAtx44NlhUX9CKHux5qetkNWhrS91AfH6JjH7LH69vjZ29HRE84NlpAQLLMSRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ipp-iaubZq-SCsbFP0T7B3Gfq1fyUal0ntDp1NreFSFhvSHUZwJiWkNCnFmfylcGP-iqvov4j_486A6MAX-POdP8hEavR02XJjpWjrJTk_NXkQ5VNLgk0P-XCmhiWG9Hle-6ivP0JuUwV_bLAbGPUMFSnz2bWOJnT3nd_6XUoQlkVRWPZaNZ7151PUybXR4-JU2q7kZvlpvlS-fig9LEKk3XPcdUHPNUt8AFBFzykHE66if7PbZbFmJcUpvgLsRVJ7EQDkY7vsFNDtJr-oQC8RgMUrqfS-3fqKaOVr7Thrww_xf0i7KkR0UDb-w4AgHC8GyjXoi1RlsFOHCTYDO4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ipp-iaubZq-SCsbFP0T7B3Gfq1fyUal0ntDp1NreFSFhvSHUZwJiWkNCnFmfylcGP-iqvov4j_486A6MAX-POdP8hEavR02XJjpWjrJTk_NXkQ5VNLgk0P-XCmhiWG9Hle-6ivP0JuUwV_bLAbGPUMFSnz2bWOJnT3nd_6XUoQlkVRWPZaNZ7151PUybXR4-JU2q7kZvlpvlS-fig9LEKk3XPcdUHPNUt8AFBFzykHE66if7PbZbFmJcUpvgLsRVJ7EQDkY7vsFNDtJr-oQC8RgMUrqfS-3fqKaOVr7Thrww_xf0i7KkR0UDb-w4AgHC8GyjXoi1RlsFOHCTYDO4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OXTL2FSRsiBq-8vIyAOf7c-rLiirajgGLbOhFWEFM4nN6TQB-69suXceBP4mvQy2QOzMEnjbly8wj4cvyv2xeVh1UzafHlc5PHOyi99BEf_5IqI4ObJ_cxzkkaQVQeJHtQYMVRa4hvgosNVTrfdROYiHPCcx_U7i93o0FBEwKppxlrZwRTYsnmDYMY_1eXD2GyttkeQD56kto5nd-CQxf9zT5npUXvqS3nKXGnSsT3SRfdsHXcIbT7oY5t2W5cKcPdqhb8Gq0MzcdM5khmMOPe6R_eCzecFLNHx3ruHJTnEtExYGhXLsbyorLCP9sXYdVRfpgOZgrAtOhwuF4CYcJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OXTL2FSRsiBq-8vIyAOf7c-rLiirajgGLbOhFWEFM4nN6TQB-69suXceBP4mvQy2QOzMEnjbly8wj4cvyv2xeVh1UzafHlc5PHOyi99BEf_5IqI4ObJ_cxzkkaQVQeJHtQYMVRa4hvgosNVTrfdROYiHPCcx_U7i93o0FBEwKppxlrZwRTYsnmDYMY_1eXD2GyttkeQD56kto5nd-CQxf9zT5npUXvqS3nKXGnSsT3SRfdsHXcIbT7oY5t2W5cKcPdqhb8Gq0MzcdM5khmMOPe6R_eCzecFLNHx3ruHJTnEtExYGhXLsbyorLCP9sXYdVRfpgOZgrAtOhwuF4CYcJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAF3Eh0DyYWhltzqDQnBlS4yihQ8I0yWVlT-y3viQuVEIGy22p5BIQO7Bwl9QmrcLXqRRlGii2N4VYk70-3nzY8s2PS7EMV-1g_tpcIPACr4K5wpTCViZfoKZ4pMLVrEYxe-9qgWvhlJgO9qGvd1esaPPJuCIX2msVeDqgy5OqSZXsG88yDxkx57ZyUTkK1amo9_M-LxpTcMDLGzbCtOpsF3kdeT_jzpOPDr_WZC5TXEkdDZfcfB0FX56Sc3UBTGyDn9awfF3fmKQIaZCsBTliIpqVPkn91n5pINoG3CxX-DJEV3vZ0PtidjRbaStQcH0OkA8VpnNO9YF30bAqIfuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlGRvFJAhaX6YecLoCBF_sd2KZIGOmrooUMjxtZDHTalhHykp-evuGRAEnX45pqlGddDquGxbyqiGyn0tvZUOo0HLt8jHJsreCXEgxkUP228hq8O04KZEdLIvb_xz_9bCOpatMnxP5gwangKHYg4JJgBKdNxMUVQhLj7sKxiGokUlIka-z9KIbKOZZwBwbIrRA0ObE30Pcp2sBlzzFmBqvG0_MBgnTVr0kQNrNbLSQXu7qP1tC4cHSXn57F_RAtfg4WkEDLwRYLMcsv9wgaAzB_IQi8YFgEE8yTNk7Ecx7rmPE7oG0vDAG3eyJRbA4a32q7bupqMD3jzDvUydHPAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIK9fo1zTR2_xhOgh7wAsxYUMsjY8cyoaMZMWs1CjIOvE4VPgnDVzL0B1NkcT0te3Qqox8wBayAwKfUC7n8KnhuxgmFSah4z0B9GQgHVdqvH290qXe2S5WJZaWREOi1IopW4QIevCrmSaat13_vXHVcMgsKy1RTdSQ8Y-4VbNCBWjsTRDRbvGrx__g1i0zWhDRgHcPEaQxMunCfWehgVsIYZDn8OVj2s2bTvOjTrKEIhFMNIxziVIvVJRCSDWv6q4BKZ1Ab5-xnHQqyLSobAod52vV5QGRn8UXFpc4yicF2JytC5-vnqACAcnGtXng-w0nMy5ngjMm44mGOQeWQDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otd8JBP8shKKm9f5mbbBYDwbAKIakv26vGEgnL5xBLdAWi5vpdS8wWzNxNFXfPEUgi1oWqzXmEjxqOKps5mfaV4q522WfOsJLPJ26uVoyqAkgv_cDOs1Fq8Qj97YNfAQPBa27z0DyiBWZlHU6luKQbpfmkSVkPt8bP93YPXiaD1AZ1F87AK0pOEn5tUoLqO4z3o0bVt7UCkZ8qddSdwA0o7f_hkWqIcYlBy4nP7ECvuET3lVDPIh_416q17rObYvS8WcoZOSJWOxZLCRpxEoxAeI5WNDJcCU41IvV5k1ZCwKDnYhYMQ8inNfl5F-4sql6qUexokGyZhT2EsipW-H4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpvZntRnU3oUWXvtN-c0sStUaqrhrDBCQJblV_QchoSaVP6CMQcE0czhJLFjytl7Pzs6vqKPktlkrQ3H-H-a2eO3llCSzt-Oxctmvy6lR37L2DRqTIsFJYQIuZUxYqSTRJnM81LNyPphA9zma9FdQVpAIRWUxENwfvmxYMyD7rCyb346M4nRossW6WqRankprQl1bYvG-1CxFF63PAosWMn1PEu7BPlWk2VBpDMEQEuuZUrUzUyBAabDYgwYGnbo5StAyInEHY2VoULUt-OtOZr8-2Q0Wd3CkUJrczwWqZ9zQ5c1cmy3KbpKm2LW5pqnpHhUMxTMOtM4JT1oPn72Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGfrsvH0bq0PfK3Jmz8gRlHoB4LxRhxbu64sKrrIK2ktl8mtrAy0x2IMk-9wCClx4ilm6rMwxUuJI9PJbF-aBbwre5zNiekK_L7rUP2tQ93EC7N6fosg-PWIhgYoRGeAv2zmA-Ilb_LqkHy_PoLWGUAy7wfYrtrLmNTLXftadJfeh--_gssuHzs4ccakfLvjaNyuYWV-V7hdNhxLGKYzo1TVBQU0T_VbX2NsEpGI_i02pY5CJjQBj4XJr9qETY0B6p0b8Mh18tOP5zorCEbywkrBSkRzEk6RB6ZaibZZzJwKKCtEF5boGm_9348TaGBFfUDrYSxAeS2SyA7FKH0BFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGEt0CDlGuDh6v2IKRUCXDJpereqHl6km_cTYSjA6nzoryx0JBVttljMDXO4HbAvbLMzSr1hcLilYmO-HpotdEqaMaLc2YzfcAHUEa_7qh7SxdvuJOWfzvWW6ts4qhlY6bTDnAuh1y5HdEN67A47FC84Dl67L93sNOTGi_SrJl50nq6_8Bipr45UNzoC6kGLnUHpPdH0CYPV60Tb-H05Z7dRDxQ6RdI2gw3Y9ViTBfLpWWxyc7yBAP-O8qQDJ873mMCJ7HsF9khd2VV-vB9PlIg2Rb3yiKKkI7AadDVmFZmke_wmNa-LJ52IviBWf5cBJqHg1dDRYK4ljZj7qUJgxQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=XJP9Mbk15w6LcWzr6XjEHY30HQBcgVON0UrTyB-Zq5QxNmYfF-M1mhiAd9tuJ2OHKdFzTCXdjIGXYs5CYb_o_8JRTfR9y1v0VVeVyQvVArCK2RyTFFLQnkW1jCC3SSvOU5Rk2dbyFdrY-IO2Qatu4bOj9XzHSIftO2ifMtxLi0rLUhTcA0K84AMYN9raDilm5CdRY6O0HV4dMbB7Grv3d4DLGI9QVA8Ic88Jq9ZmGNyq7yZWFzwwFiKGTIyvY_3Z13zzicP6NiefCIMSFlM22c3pB54VJBJseg34KI2kYJ3MZV0uclQXMMDHRksMdnIq2gtnda3hJ81xHNelDuCMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=XJP9Mbk15w6LcWzr6XjEHY30HQBcgVON0UrTyB-Zq5QxNmYfF-M1mhiAd9tuJ2OHKdFzTCXdjIGXYs5CYb_o_8JRTfR9y1v0VVeVyQvVArCK2RyTFFLQnkW1jCC3SSvOU5Rk2dbyFdrY-IO2Qatu4bOj9XzHSIftO2ifMtxLi0rLUhTcA0K84AMYN9raDilm5CdRY6O0HV4dMbB7Grv3d4DLGI9QVA8Ic88Jq9ZmGNyq7yZWFzwwFiKGTIyvY_3Z13zzicP6NiefCIMSFlM22c3pB54VJBJseg34KI2kYJ3MZV0uclQXMMDHRksMdnIq2gtnda3hJ81xHNelDuCMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ossOASc7osk2nr1RTBZyBlck1iS4SEXusj0nFKv84rsMxuM6IvYPdrjdwoZ0_gVtojOCKoF4t1B7MMyPsRmFIHoaqGuYyJl7AAtFcHl__6Zbk0H5tcVJJ4h7cYKIsxHNzLLYNpYKQogmF-KoGdodD4GTzNPRjqPdffDvj4FE9q1rhMWp1tK9Z6JcEh8Qk88-rdEWlrwO_QcCbZHyoT832SM08aaydwwzUjTudcqvtWy557VOg3Hji-QCBRDjYGYPU4UcVjWq17N0Wl_04v0Cb92SY2osp_yM6_1q3wmOBukvtUAKX-nuGJ112yci9Xf0JfDZiFbCuy5PFe2Vdv0RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=plREIRJjOEQXK1ih-s5wOtyYJf-gUuILcAsDNOKgjq2x6oPEOI7M38MA5PJUUY98XAE4JD67jxxWbLfkOfWgH2RKwfx9BPvekw_A5XAb32Pf1W5nI4eqx3JoPFAiKKWsaxHK0tRG1eWsdwEhOrI00mpSL6ie5W9hTcPOLzr2PeMG-M5U9nRWAWwWGw4iuZUZJgRBYd0ihVn4rbAQ7i6zC1uJVYs2PBcEUMHHdYNv2BLVbM3aJXVW0yLGp3HfhamSRE3QzzXYNOikdVDdj3GLvyB9t8lajouz0fbO8pEahqGfSjfmmAGUYDr_HiR43nucF5j7cPTEqcXpvzcjD0sYug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=plREIRJjOEQXK1ih-s5wOtyYJf-gUuILcAsDNOKgjq2x6oPEOI7M38MA5PJUUY98XAE4JD67jxxWbLfkOfWgH2RKwfx9BPvekw_A5XAb32Pf1W5nI4eqx3JoPFAiKKWsaxHK0tRG1eWsdwEhOrI00mpSL6ie5W9hTcPOLzr2PeMG-M5U9nRWAWwWGw4iuZUZJgRBYd0ihVn4rbAQ7i6zC1uJVYs2PBcEUMHHdYNv2BLVbM3aJXVW0yLGp3HfhamSRE3QzzXYNOikdVDdj3GLvyB9t8lajouz0fbO8pEahqGfSjfmmAGUYDr_HiR43nucF5j7cPTEqcXpvzcjD0sYug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=KqtrA3kvMa-X28SMDN2kj1OyhdpQrCJceeUvVin7OqE358H5Hw_rofgMIeVh4ddNEeV0KkU9FX_vcL0SeSwpZDRBOp7YlcfNk3NgLcMfL6D0yjjcdpMC8gJRFZe3676plzpU24p2pnyxlI_1UAPuaTgSaQnULTv_1j1TCho1_WVkVYDC59g7PRsFOTYFSs5i8u1miQUR67wYy_q8-fbXdfgxloUsOeW43EdEcRzda6twc-Dgvc5Laoo2j4W3w9Nvffo4gC5U5RToCAL9JtHwCv4gki8XfhhV_GW56CvDD0Gq84agJHZW-bXiURTAQTcgmSv_3zUjW_welqlE89Q3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=KqtrA3kvMa-X28SMDN2kj1OyhdpQrCJceeUvVin7OqE358H5Hw_rofgMIeVh4ddNEeV0KkU9FX_vcL0SeSwpZDRBOp7YlcfNk3NgLcMfL6D0yjjcdpMC8gJRFZe3676plzpU24p2pnyxlI_1UAPuaTgSaQnULTv_1j1TCho1_WVkVYDC59g7PRsFOTYFSs5i8u1miQUR67wYy_q8-fbXdfgxloUsOeW43EdEcRzda6twc-Dgvc5Laoo2j4W3w9Nvffo4gC5U5RToCAL9JtHwCv4gki8XfhhV_GW56CvDD0Gq84agJHZW-bXiURTAQTcgmSv_3zUjW_welqlE89Q3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhRznWiA7r747BG0nIU11hrr78tGUs1rbvfhpfT0YEf9dDBTwcZj0nLrWd-G7uJcppCA8R3VuCKjREXMFxIf4rkEvjfxyaLdjsF4mld-CxqRNIHygK8Sl7xUV1K5YoAOfFQw0Judf8tiPHrFSqZ-Atqtuhxk3jPJSQpr-SHnB7JYFVCCqf8qOSXigPXxspXQTNk19R-zgGxdeZjAJyAyycACgcL3qA7NwJ6VU2MaT-DkybaRN9os251J_UChxb-0u_hmcfYaUlDH572QNnzv8RRKySIEUxoTOFPQQvLX9gkl79XxXkSXUdRdE_Diffl4u07hz4k63JLMYSP5uK7ZfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkj75umYVROOGN4B2Ty_S_zKd5HNxB71cCGG2aXHQoto0hazaSWpRjUC1-N_fwRoJqTW7zPDEbPoiyUxelU-345PYTP1WH1Pt43JEwBcRHq1YQqI3Bj0PS-U6SLbbwAX03cL9gWYfJykpXXuXghHCLGqWw77gDVrfGGePUc-iYUvsAv2IJk6s9GR6HYIHdkOuO1BvhFdY_FioAji8FADsgZ06qAHFQ3s4QN7S4RJKdD6jWxYdHd0J7JJ1rvLY2rFsw0hHDgQwr1GPakWqfnGDshNj8rbGL7g7k4EqQmUDlCsQiv1fwK-FjQk_NTXLmT_C16rO8oQIa6tPiFhyh9Sbg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=AFkLz9UExdZVU_7qduipq8BWncRnhH47AjV42Dt34AGKh0iWlNst-Fx_Vq1VJ17SBJaeg67uC9mrCMQHg2uk5thqEDyyrrVPLDCzn33oUSfSzvSNwT024SDopMdNDDlyDgDoDbMawKSd0rhwnJzXJ-KVYNDQKojwSdnvVBnlHSGWeHRzqKvUHC0Icmayt8CqrYFBw0Ve7BAh4nkQRN4raPmh9x9cPDVSgDoXxeTDG5NL75e3L5ipoIJpa7sXzRtbJqEAeW6Wgq3va3LhRthbIalT64JA3DCJuI7tPIQezAjK9wAzffAo6bt8Pi3THKA2wh1eHTLNevG89bQHyMUfIyteAKV8OHcnHnWg4KuiXUqslK5v9DKtP8rWmq44YqWAvEjoYbXhne8oSgI7Wlr2POs78122k_J6_QvU6dizssaxq2rpedgZL26n6WaBZ4gvZD7695nHK6SwdSBmDEL00Twl-uAiZjb345nqYiZRYiNmpXSn_okItA8OyJ5AxM1qIyRPYX2U718lCHhqWZTAYUCNmgurvosnbAn2xfeb3mUXH_JSRlSSVhiIQ_8H9ryQ4RCz97jkYioQKAdzyGab6egwdwTgbuofjQAx8EsrFx7sXWTkPaaEJsa8ifpMtUSUjemxb3YfIfZPVD8ylBGJWTkVT3xaKFCOqlLN2JaY2tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=AFkLz9UExdZVU_7qduipq8BWncRnhH47AjV42Dt34AGKh0iWlNst-Fx_Vq1VJ17SBJaeg67uC9mrCMQHg2uk5thqEDyyrrVPLDCzn33oUSfSzvSNwT024SDopMdNDDlyDgDoDbMawKSd0rhwnJzXJ-KVYNDQKojwSdnvVBnlHSGWeHRzqKvUHC0Icmayt8CqrYFBw0Ve7BAh4nkQRN4raPmh9x9cPDVSgDoXxeTDG5NL75e3L5ipoIJpa7sXzRtbJqEAeW6Wgq3va3LhRthbIalT64JA3DCJuI7tPIQezAjK9wAzffAo6bt8Pi3THKA2wh1eHTLNevG89bQHyMUfIyteAKV8OHcnHnWg4KuiXUqslK5v9DKtP8rWmq44YqWAvEjoYbXhne8oSgI7Wlr2POs78122k_J6_QvU6dizssaxq2rpedgZL26n6WaBZ4gvZD7695nHK6SwdSBmDEL00Twl-uAiZjb345nqYiZRYiNmpXSn_okItA8OyJ5AxM1qIyRPYX2U718lCHhqWZTAYUCNmgurvosnbAn2xfeb3mUXH_JSRlSSVhiIQ_8H9ryQ4RCz97jkYioQKAdzyGab6egwdwTgbuofjQAx8EsrFx7sXWTkPaaEJsa8ifpMtUSUjemxb3YfIfZPVD8ylBGJWTkVT3xaKFCOqlLN2JaY2tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcnlsYyLnztVpLmHhaxWmzYk_xWQ_2tQdRgzJAKr7PCNdlWWeKcdnWaJJBm1RfJ88rt7WrJIY7PKShRkGXHtsJuck1BLsmk_seTz3XvRU1f_r1Qnz1rLoc3ra7T_tyX-xCcJ9D3VaMVbBksGhaB_r0U02WpDtRzWOJqSg10Wwh7FU6XOIEkeh6FoSgqvXVI1NH0rGqjy9S90DNcDLqveDjDdsbfqYjaPkHMLN4ZWy2EU7f1BUIapnqAygp04C4n6VH7LARuv7wuJtMLBhs19qhH3PB4ZN4bEHSrS-yoB3qBGm0KVotX18k3By6V_hMwqHagvTEnTrEc6qAMGM5t5PQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=gsfv8Mlff6hNbEJq9Bg7oFN7SfvrTyEACyr3TxK__mH53hrEXH8kAGCHv7c7GuZX8K__650o2wWWw1KknYp6OLgEjV13m7HhxxCDuuvdKQWPE4u7eBY-5GkxpnzVFSDvlpNHV4VlVApS19kMshklCvr3r3BCLmtAueiYzoWv8zWqa5rgfOYdsTGdl7gudQdCVNelfU8BW8LPbCOkASwKQDwqVRA49ludVqhV1qQK42QNC6CIeXIbEL1x0XSH9vpDoQ1MvaVCqdtQbEB7vXTvFYA9YifwQnJzccDf4zBvndAb63OC3AOmGu8tSafZk7xKtKaFJxbakFbFTEqd-YWR8awzkBXhD325VlU2y23HUtnwAMzx89nmPwoQyotW5qgiqIKNMZs58uTwGY08LQO5lTjdh2PUrqjxmdhGULNnCW9gvaeFi4-axxpD6Id6W30vmckg2G9AI25C_ynbgZ1Gnx2LJzJzXgCtiEPyj3DMlHA-jartM6HD1KtP8yRrvtVXo5YT0-Wu1j52gULbteCshk9-qslwPif5XnRPoEbBZCYNCN5B_GtdpOKLV-FNPRuEDvOVgI9hVzbxL5lXMwVlZUiZOLzKw79JnAnpGqWR6F045n5--w_LXXwEW_NR0vbLEWxxKId53ubn8KHN9TNinE50htZ6EOB0pon5DHfcH6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=gsfv8Mlff6hNbEJq9Bg7oFN7SfvrTyEACyr3TxK__mH53hrEXH8kAGCHv7c7GuZX8K__650o2wWWw1KknYp6OLgEjV13m7HhxxCDuuvdKQWPE4u7eBY-5GkxpnzVFSDvlpNHV4VlVApS19kMshklCvr3r3BCLmtAueiYzoWv8zWqa5rgfOYdsTGdl7gudQdCVNelfU8BW8LPbCOkASwKQDwqVRA49ludVqhV1qQK42QNC6CIeXIbEL1x0XSH9vpDoQ1MvaVCqdtQbEB7vXTvFYA9YifwQnJzccDf4zBvndAb63OC3AOmGu8tSafZk7xKtKaFJxbakFbFTEqd-YWR8awzkBXhD325VlU2y23HUtnwAMzx89nmPwoQyotW5qgiqIKNMZs58uTwGY08LQO5lTjdh2PUrqjxmdhGULNnCW9gvaeFi4-axxpD6Id6W30vmckg2G9AI25C_ynbgZ1Gnx2LJzJzXgCtiEPyj3DMlHA-jartM6HD1KtP8yRrvtVXo5YT0-Wu1j52gULbteCshk9-qslwPif5XnRPoEbBZCYNCN5B_GtdpOKLV-FNPRuEDvOVgI9hVzbxL5lXMwVlZUiZOLzKw79JnAnpGqWR6F045n5--w_LXXwEW_NR0vbLEWxxKId53ubn8KHN9TNinE50htZ6EOB0pon5DHfcH6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYhFj_u3wMJncdh3qyB8wmG_YKx8oNjp8IuHVqVVe4htVjCn9DW7maQZKrNbbCibZIG5eThBxC4kqd_qpl3z8JjFwUSWO5a9zV8n6LBUcN9VxgQU8dcOnuTP9GTyxgbVWilde_q00BfAaz0uTU-ZrkgOv8u2TDUm7onVkr4fP2SI7DgWnnorXLDxHFLOhOFinAiY1Y4y0oMpl9K5BO9QYPy-ApSSz19Lp-kr5-APqfqwFGKKOXs2AeNaUdDLAyqfEZHzttR0Qy8HSFQ9gK84_qlaKNg80bIRvJVKMurRykdEJHhFHHP4CTrzgaz4Np8qujUG8GnT_xucLx8HiRhCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
