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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miBEryZsuOE2r8Crslb_UgMIj5UBOh8E--8tk7DnH14PKKZjrz4AaTsfOy7g1vQimhg5YAVJqOXNV2DlPYXBnHpCCrq9KlHssYkH7XPNUXjIaZEKSgUdFU4jlTfFng0O-7RpcYLHawrTJrPdXPwnPXc5q1Lav-ejsDKLMcJrickGF9LBYGTh9GH4_1L33XrpF0eF61m-zGQeb-HPzx5DGElxiNcL7KopY0uUBPSiwE1_0sbUAeF-LkxxKrqkqmDSwd4rIJTePHUoRsH6UoIL6vYfTYVlxeUHyJzMUz4KiJ6_VjNjD54p1MARACAfOj872t9jh0oAfbVtw568ZvTfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZUmRoP3hFL3LlRznp25nMjuQZfUnvtHFE2EIhu7uXs5bd82f0GysseEmUhXd3N-eBtfl7unInvctIADNhd4yWo1dTImqD_zdxYmC35FmDQteEWxAeojNgQxt1DtFMXIX6YKLuSEhKU2Z0vq7NLRpKThbaki3mrIGm2Z4zmauoukH41TqEja7gyV5ZQy9dAVQTEoPAo-FRTWzrj6lo5i0aiKzvSuZShmyUULfwsN7LZOAh_cd8-KpajzKyWlBRIT0dE5M87vs9I27JxfDtuG5nE0vM7xkp4Ev2_KEUymjixjW8LEvjahzHSlEHShbVfUgCh-R-Sna55kxk132pynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKrKbCqdLLJyvGUSmzC3hfoiZLxRZ2B8Vp05WS1d4JfKg8ZYv7dPLHUBc82H22Rh53Ze0b_44oP6OpC2xpse4gjxs_60bWltLVP5fCp7XtDjPmCJdmAwPhKL2PtTGwrVqIxthcaK4V_Z8YDKw2RCaWq9mWnmKPbT32tOi3_y1Wld6pgpCrrhVnDD7gK0IxIEVn8jAgghu8gjg9Cxfem55yneVpkocKype0ezE7IoCMJACdv9bl-NSphDJ-a0kv9t7pwR4FfJzlzkjaNtAet4pDJ2U--bS-RXPFbhd6Y3yzsiSz5Te7lWDbucLlYfXOOqJHjAgx7gguFWSmTScnKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9qUR65QcyDg4DRJrvNNK-tiS6zK2izzc4lZ-boV8s4oIo7NrTBz6hAr0xjShd-4iv76H-oteNqTNm0eX4wY8MWDGs5TGy1BNdWwmEd55q041WEFotZiYZ-GAo5kogTRDgy81bLpbqwe67OTPYYpAH7sCAKTkMVxUBekS7PnvCEvaFd2lZq_Cwq5TjUxBidqTALzBzXttoaLXf-exxWpZC8w9RONsBYJ6uTTJoMa4hSMFVJbVTh4HKvIg4Y91kkx1QvkhYkM_4QYf4qkrmxlf54BDiFgzczEf_pxldBJPRXpPpHn1qAf9Oc4L7BQmfjbx69e1bohOc476qHst9Fluw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZO0vllu4Hdey6DbIgBA5Oh9s-IVpzgH3hnQBCRBSUJRi7fYcCMkriJakfoLYF6CeO1h60K8SiunGXkcI0XCnGruWm2QOR60g9aIFZzlrL6voa60SsQitK_2iurNltQkCZQEoks-RY8gVu-eRGyA9-SktvF7UIRTSUq_Q9JtXIxRK7jxAUorCgIhAkzr31KbouDEhIqAizmRtbjl4ruwntD-EcKGhR5ah8bZQyfogCrKCtaSe-tN0GM_mvC8rpMf-s_PdvVTzKhbVKVWeUGiKTeRs0fyCw8HFSWQMq79jG9E1xRsLJwYWuTrQcbl0dE2CsF4Ujb3zNxP3NXmRnYImcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZO0vllu4Hdey6DbIgBA5Oh9s-IVpzgH3hnQBCRBSUJRi7fYcCMkriJakfoLYF6CeO1h60K8SiunGXkcI0XCnGruWm2QOR60g9aIFZzlrL6voa60SsQitK_2iurNltQkCZQEoks-RY8gVu-eRGyA9-SktvF7UIRTSUq_Q9JtXIxRK7jxAUorCgIhAkzr31KbouDEhIqAizmRtbjl4ruwntD-EcKGhR5ah8bZQyfogCrKCtaSe-tN0GM_mvC8rpMf-s_PdvVTzKhbVKVWeUGiKTeRs0fyCw8HFSWQMq79jG9E1xRsLJwYWuTrQcbl0dE2CsF4Ujb3zNxP3NXmRnYImcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=kRs7TeOixCfFhpk0_aucI276xcigez8dCahZMxlzR2gyOx9T5rylTX_iX8_IDOA4vAN_B6MZOgmogK9WDHY0iOUm9DGzXLHxK_d4ozlhC1i4NvQqb8FBFDiUc7b-4Jc1OrNnUkAg1ATwoBKI8nSsUCDQHv8j-06s4pPR3baf538_ab2Iw8L8KuLMssLZERpl_hnxZNLwJjsaVMFRGKzVfn3vzqv_EZCFRvxgXCirCqo7r_eyOoYxJUDwi482IJDw3jlVtAv56eFkhuVMPG_ybl58_x9EtiDFFCVh3T9ZyHu4fh4g-yKLu-1Gcwo12-Opbjm2lWukA8ZiTMnODuspwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=kRs7TeOixCfFhpk0_aucI276xcigez8dCahZMxlzR2gyOx9T5rylTX_iX8_IDOA4vAN_B6MZOgmogK9WDHY0iOUm9DGzXLHxK_d4ozlhC1i4NvQqb8FBFDiUc7b-4Jc1OrNnUkAg1ATwoBKI8nSsUCDQHv8j-06s4pPR3baf538_ab2Iw8L8KuLMssLZERpl_hnxZNLwJjsaVMFRGKzVfn3vzqv_EZCFRvxgXCirCqo7r_eyOoYxJUDwi482IJDw3jlVtAv56eFkhuVMPG_ybl58_x9EtiDFFCVh3T9ZyHu4fh4g-yKLu-1Gcwo12-Opbjm2lWukA8ZiTMnODuspwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=XDMDG5B4Q4U8tFpgO-Pu4w0DJLpRCw1frGRRNYD1iFCNxk_L_glLyIXv9KivoWhgF71pZKqFYGc4ztHd7d7y-qCcJQepty7H__ClhzY5WTGIyqWDd-XyREhFtc9z-ENmlorGROecOXvGRDpxvueoFWYTZVEAo01RqyhDeO_ZIRoVCqwu8wM0IEaVdn_1bb7I6rTn562w69kgDdvXykLcBU-yp3bAMlfOXAj_lyoIAIy07jDrSfPwPww9dIgAjIbz9TqTXANHpeWlFkkp5y9AJHRsQ3XGA4rkLrPhZIEesBbXqNn2u8Gh2KyohsJCaT56fvgbO3bReHtDUcN1UsXAHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=XDMDG5B4Q4U8tFpgO-Pu4w0DJLpRCw1frGRRNYD1iFCNxk_L_glLyIXv9KivoWhgF71pZKqFYGc4ztHd7d7y-qCcJQepty7H__ClhzY5WTGIyqWDd-XyREhFtc9z-ENmlorGROecOXvGRDpxvueoFWYTZVEAo01RqyhDeO_ZIRoVCqwu8wM0IEaVdn_1bb7I6rTn562w69kgDdvXykLcBU-yp3bAMlfOXAj_lyoIAIy07jDrSfPwPww9dIgAjIbz9TqTXANHpeWlFkkp5y9AJHRsQ3XGA4rkLrPhZIEesBbXqNn2u8Gh2KyohsJCaT56fvgbO3bReHtDUcN1UsXAHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Gx_VW2Kb-vxnJ6cVGIwVKcbi6cDSmqRfYMAhrwh0L6Q4My5H-e6hBX6XPfEmKIX8jUvtDBVSVFsJ51pkKq5kFSCfrM45k05_ienGAx_zhFDDb1SoUesqG0Mnr8-416hTlcu348QQzXNs3x9g-jr4kFwu_x5XZ4rdLMwpKSXC9Cw07DO2m3sHSEU9aVYMq2Nqyqkt7eqA7m9KHXteWteFvuVpEe7cxsfjSKDNJugAdmdbW2rY2q5uhg21A4DhbswZjn5BA6_vxfFdrvC9PObIbKQh1XOFJVNYjWA4Mj8sr7kH6CIOEXRfRCFeoL2YDWqoH4nRcdDP5f5AtdW9AFRiog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Gx_VW2Kb-vxnJ6cVGIwVKcbi6cDSmqRfYMAhrwh0L6Q4My5H-e6hBX6XPfEmKIX8jUvtDBVSVFsJ51pkKq5kFSCfrM45k05_ienGAx_zhFDDb1SoUesqG0Mnr8-416hTlcu348QQzXNs3x9g-jr4kFwu_x5XZ4rdLMwpKSXC9Cw07DO2m3sHSEU9aVYMq2Nqyqkt7eqA7m9KHXteWteFvuVpEe7cxsfjSKDNJugAdmdbW2rY2q5uhg21A4DhbswZjn5BA6_vxfFdrvC9PObIbKQh1XOFJVNYjWA4Mj8sr7kH6CIOEXRfRCFeoL2YDWqoH4nRcdDP5f5AtdW9AFRiog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY69BtzJlQnwpOXXKp3R57C-1rvjH_vFn0zprPJO1C8-qQkboaEBVig7n3L_TfwSi4t2FXQzGEPYk-dbDDBbN4n76PfDPvmdKP7J8hYvuqGi2FY02PbGuHnpdQrJtkrlaeUHhtY2twXQrM739BXt7y5phIxlTJgVQ_DYSHZiRty-4Tqx9552OnVjvBJ2ndR9p4GFeZw_KXxqFebbyQcHsif3TRW52yLaE5ww9o1dDqOz9pUq_Ksm8BNmH9zl1MLTyQXvULJiO57z4H55itexihOzItLYb8gYa5R3G01sdklxREDUmjMlto1Kw_lbtZc72hdRrdwDfHBsskOQMCNk6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OybxjbQkascJumXX57ORnogjiNnLkx6rpODgggKFdkcM6ha1Bjx0Wasisydy9-gIybS-DWBTKVH5gKqkUL6lpf6gfmxlcqNaD1gX4Qso9hMdQADAAeuvooRLvNNcMIeECRHq0ziTqwFUUTPYQrF1S8KMhcsSC-Z2riG81OmchCCtN7LYzzqhsCt3gOPTJzovHqlG5m3m4PXhJbdPnPJvxLdDgzj0iUu9W5ahYuSTClo4c22mDZ1XEns1BhaxbdkyUuYVEkcM8ZZMDHpDnlwhymkOebjtdS8vGhQXDwtGM3DrqK_CTKxE1xo3hkJj05N79rKDbsxwmw_uxAtVPAs2PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OybxjbQkascJumXX57ORnogjiNnLkx6rpODgggKFdkcM6ha1Bjx0Wasisydy9-gIybS-DWBTKVH5gKqkUL6lpf6gfmxlcqNaD1gX4Qso9hMdQADAAeuvooRLvNNcMIeECRHq0ziTqwFUUTPYQrF1S8KMhcsSC-Z2riG81OmchCCtN7LYzzqhsCt3gOPTJzovHqlG5m3m4PXhJbdPnPJvxLdDgzj0iUu9W5ahYuSTClo4c22mDZ1XEns1BhaxbdkyUuYVEkcM8ZZMDHpDnlwhymkOebjtdS8vGhQXDwtGM3DrqK_CTKxE1xo3hkJj05N79rKDbsxwmw_uxAtVPAs2PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=LnEzlqxBLjJ2bOnjaRm_rkTxnRxPS5dJkyWnK9QcYL4viKieGGeRGVGunkkr6nTMkU5P6C-CrkxObHcKdvvjATTHtjNYDM8jBgYuGmZ6xmC_GyA94j8bkzPWW2MnLRd4-kHz35dgjT1il2JpyF-NU_NAFyoF72wKAubuJOoRlmFzBlfKxD1Yk1qabrnsyvop7jKUbGTv1rS87b8JSTiZmya8zcJcoeOc46-qwRP-c1AQGbETR59ETqk2I6JpW4AgOKuczHxRY_JRxaJXoA-qL99Ad808EiuAXEPGJnGbJT-XXBlr7bssDeyMqjyKW0vKUMFVJVGJi3TO-_4jAZbNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=LnEzlqxBLjJ2bOnjaRm_rkTxnRxPS5dJkyWnK9QcYL4viKieGGeRGVGunkkr6nTMkU5P6C-CrkxObHcKdvvjATTHtjNYDM8jBgYuGmZ6xmC_GyA94j8bkzPWW2MnLRd4-kHz35dgjT1il2JpyF-NU_NAFyoF72wKAubuJOoRlmFzBlfKxD1Yk1qabrnsyvop7jKUbGTv1rS87b8JSTiZmya8zcJcoeOc46-qwRP-c1AQGbETR59ETqk2I6JpW4AgOKuczHxRY_JRxaJXoA-qL99Ad808EiuAXEPGJnGbJT-XXBlr7bssDeyMqjyKW0vKUMFVJVGJi3TO-_4jAZbNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHGIQZ1uOmrNYUYKr7CCjrbO-yTVbkiXxPojpYodWCLQt_MZlGxPy3WlLjwlydxTbJDvKZJMVOnw5av8UtJXh1hLu8K-P9kZBy2YCiu9ftQc4kbY6Pa-svBOS790l5Pg-iGOX8-cUhNHw0kDo6o4IeaEyGUSqeFEu5hESM7CHXT6UFqOyMLNyyt-PgYiE71HiJcVeMgV6ts0DDNZdqoFg0qbuDnq7-TfAoMNx1DVFHapewrBzPaOiBIaa2IPwpZSrWAPyugQzcKBjkrkxKHjA33H10d7FK8JPHBYnF6-90YK_YJhfzYhx3oG7xasxL8HMqX_WdyXgxqIQFZA2TQOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVUP0On1AjdWZ_44IC_pjnHRqfBPzilOIiezZuPT_EVhs0ZrGLjpUUY3B0x7uotVs27X_QgYXTuNU6RDPcfMoWhHd5oL5z_DoTwz7mQnA2d6DAMLrTl0uJnFeQSDc3Xm33RSF_ibn2DujPXw3CntufXQG8eICc3EQBTbZehqm4hARWp7GQNgEY9ms1P9BiQtBW5sdIKEsrgPZz1fOJdad6NjkhNQZ5eh0YV2Rj8bUqXTEoUd4rYVukTQUdqKGzRge_WIvg_wkA68XvOXdKqN3nksGgFbIG6JSNt4ChbmrKHsmZQFSCNG5bFDFa_B5JJGEZUPLRUIaGyLr6yRwHMH6A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U6PVShuB-j24txXJCqrQ163ci-AXjRGeOG47I4kqCTDQcuuag_14e7aJySiWirQ6FZlWi4QjDkV1broT0JDTTxOjnwIMOpqmsIIbJeOmDiPjZOioV_VHZ5haktoYPsqwte1YNVEaqjIPMHW1CuDfWx-xhNVVWhO1ZV-BTewBuyZQBZ-qSuvItobdkgKNZsla_Xb_4B8gYGzAPlhYL-LRe2VHh68rY3dsFKLdpAjRqtcg8aJCTEbxFX-YfFlE55zIPFhJVIVAI8Ney9MgdeVRxqXJs08KVgD_o37ktAuK_5swTgG3Wf56RVvXJKlZUHe8lwkwvqgaWy4ECOJp0gzkTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U6PVShuB-j24txXJCqrQ163ci-AXjRGeOG47I4kqCTDQcuuag_14e7aJySiWirQ6FZlWi4QjDkV1broT0JDTTxOjnwIMOpqmsIIbJeOmDiPjZOioV_VHZ5haktoYPsqwte1YNVEaqjIPMHW1CuDfWx-xhNVVWhO1ZV-BTewBuyZQBZ-qSuvItobdkgKNZsla_Xb_4B8gYGzAPlhYL-LRe2VHh68rY3dsFKLdpAjRqtcg8aJCTEbxFX-YfFlE55zIPFhJVIVAI8Ney9MgdeVRxqXJs08KVgD_o37ktAuK_5swTgG3Wf56RVvXJKlZUHe8lwkwvqgaWy4ECOJp0gzkTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeWsH7Qewq2EZpqtah1dR-2VHbQvPbEEvyIGnbMi4cfkxxs_3No45NOCqYmR7Yl-TR3lWt_EAq_RmrS0pjgKbh-B4fj6hSG8PQ__qkxLDPg3q-bY3tptyiZSga-_KB-TEYQnACGmiGAsSoVD6ISfEqFyEHPJWgU-aZCm0c93xXr9Tnmp4-Bp2Or1nsjQe5G_plG6-OLDN6xTgFLW5orJdj23xyw8o_RbY0R96ET-g3Pt-8AGalb-YIrWWWRHm404CcBWTF1GFbWgukKKQvV1m_gsVkgjxELkq2W99YiwC577XSLLeSn2Zw4QbBzw0MegdzwGOLkh5RnDhlzTGJO2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZe1lenmKog6FS9lsyHWwLmiBb3adG86U43zrhFT9d0UtDboBRFwjAMa3SBmS-_LcoVdlC0bngcvhfPTuLhDL3b001ju4YdIhBxolRemhXZOSUB5_JgbdjQf_HoP6uNYpLv_Ol8mTYOAhIQxPMWbFH4Lz8CGH3mWUg_D0xVSKexgmHWGOeTCQbIaSp-sEvJMmV00ndtNmB2AOjT4WBEoRVIML9WGhWFz2chffNkZmwdSQdFNXOJaIAVdKUkUuuLH2poQUz2sa5DmfeUNwmOa8X9CQNP93WJ7vWqh2LLa8vABwJ_T38yOd0efjTLEGmVrWJhQLUSm1yCR9doox1KV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goEBxIjSl1fIA3NODSVNgniYYfFsrZVej1dc2QzuxP-2riZohlFew3fOw2OH_iq0fALA_aOUS8Eqor3rafdr2CL88t4P5XRu27u4k8xMSkzeqxKN3cQXjogFLNO06AA1ZnEdoxY4VM-ym_8MwmXAqXC0HsF3kqgQ76XP5JPHD17xwhZ3ZnPaIUFTdR70c7aphCtT6L6so_1PxPABUPmTlUswa3K186y7rbU_qpCTbh8RvcPUJK0j3TwkdKnr0x8SdCzZzPC_Vs3KloWxLM7l6nwZF6tKqH0fWYfueaYCzCva4RCwmK8B3tnrJ7jZ9bTrQtTpKxwYQP6x_mpSs5EC0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YWQCseaKu3JujMC45kz63ygHGjs4FZK5c7BjCgTqRSes4oBpo274dyU-304PqPCr6-M5E9qnrbJkgC6fAknFAiXCZU-tfTYitdntyiW2q2khbJeFyFVHtRs3uLq2LZIafnxakM0NX0z0ac8GM68Pdwd3rXKFKvl6DuhSMIrCDqtx5NMI3wQZomjt-pP9KluYLBp84rgzzsv1i2Vq4aeWdbf36W9Jc10ZHHMDaYQH-rK-mKG2gHGnSWEdBdmsJbtAEiT8sHrJdpCqAHqCPtFbcXxz9Em0ZFHB4cr0kHTtYDweyNBXj9-UzrUebw5EP9Ez-mzOzgh0HmbMBxnI8BIU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YWQCseaKu3JujMC45kz63ygHGjs4FZK5c7BjCgTqRSes4oBpo274dyU-304PqPCr6-M5E9qnrbJkgC6fAknFAiXCZU-tfTYitdntyiW2q2khbJeFyFVHtRs3uLq2LZIafnxakM0NX0z0ac8GM68Pdwd3rXKFKvl6DuhSMIrCDqtx5NMI3wQZomjt-pP9KluYLBp84rgzzsv1i2Vq4aeWdbf36W9Jc10ZHHMDaYQH-rK-mKG2gHGnSWEdBdmsJbtAEiT8sHrJdpCqAHqCPtFbcXxz9Em0ZFHB4cr0kHTtYDweyNBXj9-UzrUebw5EP9Ez-mzOzgh0HmbMBxnI8BIU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=W_LvJqawe4gD2JGgwkfHKCob51jxsjrbdEz4Ul0yDy4J2uXmKud-d9HzAmYdMwaLfAwfftEiXD9e2s8e5MTFd73ez6AEt6jSppNLnua_ti4OCOQiPxpqvkotaF9IGUzo68sAmXv662ETMlMgcjb9sA4Ay42EKRtnjgYphpUslxq5Sq0fRvcNqyUgrj4CXaAL8X59Vm4_xFvo0nFnamfL5lFO7H2b6NdCuNXyJOz9PS-svNByPtMmuyhpyLryn2k9Ul_5r_Bbas8fhJJfLOaWlh5OFAnYsITQsePSnR0IABIHMN65Vpnhygi-ffo45TkfG-FYbOfvjT8_utdoTJvvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=W_LvJqawe4gD2JGgwkfHKCob51jxsjrbdEz4Ul0yDy4J2uXmKud-d9HzAmYdMwaLfAwfftEiXD9e2s8e5MTFd73ez6AEt6jSppNLnua_ti4OCOQiPxpqvkotaF9IGUzo68sAmXv662ETMlMgcjb9sA4Ay42EKRtnjgYphpUslxq5Sq0fRvcNqyUgrj4CXaAL8X59Vm4_xFvo0nFnamfL5lFO7H2b6NdCuNXyJOz9PS-svNByPtMmuyhpyLryn2k9Ul_5r_Bbas8fhJJfLOaWlh5OFAnYsITQsePSnR0IABIHMN65Vpnhygi-ffo45TkfG-FYbOfvjT8_utdoTJvvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=pg50kcAz28V_SFZK9Gl1zQzop8Az6TNhLiV5aX7XqWxDDzrSR-FimUxof1LsAvn8gbHmvGga29PYWwL-raP4KSAcAuWOdh26W4tearJlqdMpwKt2yTa3bH6dHxdOI69-bluL1o2W82v2uWyGjDZgDZaQE5L2KoKdjziaNoFCKtn0ASX9_A6twwJOSk3uirCgd7X0t1TP_bKTt2gEjcjqP-7EfSt2cBOlx7UxCkDQYF-hb-kBVb6aY-JpJyRFf7sgkXH5hIOithBhXDLAPP87rzsLB6plug7hyeKVOQ64ENxw5XdQeV1-e1P90mMsdEJF8Hrcf9AeEnKm_1JNp7SiRapPQ2Vd5An7NDgPwrgAEdhDBtfFOYQdrW_lcHMVtPCF9Rd2Bw0jiwYeAzxkBNqjyIxmrszz78KMzwrZ6AWE8FsGYTeRPIhNLCJ7nV3uYqKJWzc9Z6bIDVOK0trMx3q6QEUoXai_ZTw_c2JXMFaGbHamh-v0CdpF3xNzg78Ka9UqUmK04nS30XQVja4OtOAkju9MGXnU1TOnLNado1EIBR2tVfJWmflyFmFJ9gup_Xzk7JBlt8Fm0fBtBWgWQfnotmAiRpQB6M_EQk7Skw9eHs5Z3w62G2E15YFRxerkB9fXgo-2gHmMFnLM2F5z5L0mOxKo9A8ivGmQJcWanaJ4KMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=pg50kcAz28V_SFZK9Gl1zQzop8Az6TNhLiV5aX7XqWxDDzrSR-FimUxof1LsAvn8gbHmvGga29PYWwL-raP4KSAcAuWOdh26W4tearJlqdMpwKt2yTa3bH6dHxdOI69-bluL1o2W82v2uWyGjDZgDZaQE5L2KoKdjziaNoFCKtn0ASX9_A6twwJOSk3uirCgd7X0t1TP_bKTt2gEjcjqP-7EfSt2cBOlx7UxCkDQYF-hb-kBVb6aY-JpJyRFf7sgkXH5hIOithBhXDLAPP87rzsLB6plug7hyeKVOQ64ENxw5XdQeV1-e1P90mMsdEJF8Hrcf9AeEnKm_1JNp7SiRapPQ2Vd5An7NDgPwrgAEdhDBtfFOYQdrW_lcHMVtPCF9Rd2Bw0jiwYeAzxkBNqjyIxmrszz78KMzwrZ6AWE8FsGYTeRPIhNLCJ7nV3uYqKJWzc9Z6bIDVOK0trMx3q6QEUoXai_ZTw_c2JXMFaGbHamh-v0CdpF3xNzg78Ka9UqUmK04nS30XQVja4OtOAkju9MGXnU1TOnLNado1EIBR2tVfJWmflyFmFJ9gup_Xzk7JBlt8Fm0fBtBWgWQfnotmAiRpQB6M_EQk7Skw9eHs5Z3w62G2E15YFRxerkB9fXgo-2gHmMFnLM2F5z5L0mOxKo9A8ivGmQJcWanaJ4KMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=a89QUafadsi5XwHYpmOxi6lmC-Kl-jRDxYN8RUADD_pjVixngFqBEtpeVNpvAaUhnyna_YlD1n6GE5gF_BZawkD19cOoPxEyKthIil4R7JQB1XtU3VQBqPI3ECbT4RVA2nEaogoKMXcBCLbQ02xqZH0wVCbLHgtm32RjZ9PLUwBgwRg1GfRdAzg5VhL-OGfYibHI4W3JwTfGPIXIkSA-WPwbT_T5ZwIoDw2iXybuuGpwxzVeJ9DjJoYoK6QPWGckmH4H4C-k9d0VwKPuax7Is5O8uGq-EE-Y3c2174aK-3liIyJn6iGyezeTKrvAppiF7t4W0Nfv5ckGi1oTZXtcqKkz7Bh-czWEbX6oOkcxBjYt73BMZ3llUrXbSH7AicSECNDb8-2-H_XcvtuWv8GGElDbTXenEvt_hFxVhXiR9hP6yFG5C83ZJko6QTFC6JUzcr-HzBJNTEpx-drV3kd7TwJyPxFTYxnjIEJrGRuqkjYOVbwEyosrR8lNz5gaNlVusxpNxgsYLer8quTG1MFGrQPW6XG2Crd_TLnA6E8PqhUpaTRErtqDtPy1HsvfqlT2-WHh8iuVO_3PfixdEh6qo1ECCRmhp_-zM_Bp91baceaq0sc1-vWQ2t4YHga2ZYer8bV8sWL7RoXG6QrgzvMc5mWb5faK-Iw3qkLfpZ7_kiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=a89QUafadsi5XwHYpmOxi6lmC-Kl-jRDxYN8RUADD_pjVixngFqBEtpeVNpvAaUhnyna_YlD1n6GE5gF_BZawkD19cOoPxEyKthIil4R7JQB1XtU3VQBqPI3ECbT4RVA2nEaogoKMXcBCLbQ02xqZH0wVCbLHgtm32RjZ9PLUwBgwRg1GfRdAzg5VhL-OGfYibHI4W3JwTfGPIXIkSA-WPwbT_T5ZwIoDw2iXybuuGpwxzVeJ9DjJoYoK6QPWGckmH4H4C-k9d0VwKPuax7Is5O8uGq-EE-Y3c2174aK-3liIyJn6iGyezeTKrvAppiF7t4W0Nfv5ckGi1oTZXtcqKkz7Bh-czWEbX6oOkcxBjYt73BMZ3llUrXbSH7AicSECNDb8-2-H_XcvtuWv8GGElDbTXenEvt_hFxVhXiR9hP6yFG5C83ZJko6QTFC6JUzcr-HzBJNTEpx-drV3kd7TwJyPxFTYxnjIEJrGRuqkjYOVbwEyosrR8lNz5gaNlVusxpNxgsYLer8quTG1MFGrQPW6XG2Crd_TLnA6E8PqhUpaTRErtqDtPy1HsvfqlT2-WHh8iuVO_3PfixdEh6qo1ECCRmhp_-zM_Bp91baceaq0sc1-vWQ2t4YHga2ZYer8bV8sWL7RoXG6QrgzvMc5mWb5faK-Iw3qkLfpZ7_kiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=nm5j3YXj7f___iw1lI6up4LCQWjAGFR6-pvt_MqYFRaJYplFQzkLRWhHaB6nU6_Slz1qw6gjNNaS0hGgavpD9t5cdikKNd8dGijUd6RWYfh-wucUvkLtENakqn55dhoAiWYjbw1ho5jbKMa5my9WT3mK158jjaMsR44tKbUvYFe8fChYHlyIeF7CPRfshW5Dfu90W7x4bHWJuNUiEOv3wIA6_zDY_Nj8dwzfLPM9SHk8EHLZ0dclmKhecWDx2nKi0PLXhyOVEqeyGc8r1exl4bScrFnkCxYMf_UJNJUhz-QiMwUo9b-peon3RgviAf9QsKpIfmdIzMgykzV-VT4Rfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=nm5j3YXj7f___iw1lI6up4LCQWjAGFR6-pvt_MqYFRaJYplFQzkLRWhHaB6nU6_Slz1qw6gjNNaS0hGgavpD9t5cdikKNd8dGijUd6RWYfh-wucUvkLtENakqn55dhoAiWYjbw1ho5jbKMa5my9WT3mK158jjaMsR44tKbUvYFe8fChYHlyIeF7CPRfshW5Dfu90W7x4bHWJuNUiEOv3wIA6_zDY_Nj8dwzfLPM9SHk8EHLZ0dclmKhecWDx2nKi0PLXhyOVEqeyGc8r1exl4bScrFnkCxYMf_UJNJUhz-QiMwUo9b-peon3RgviAf9QsKpIfmdIzMgykzV-VT4Rfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYxJVdhl-gMZHnmPMSiygxdFigNh-JqPK2oBiocTuvH0JJmztG9c9r1v_Fr4AGhNCrtO5pJxjNTtW9PwMRtpUwUEp9C-le1-SMFaUCtpzCaXwDddGlAPHYokf0YTlzZBuQJN8wBJPKWCD9yXnxo7u9-TJocatSltlq_BPceiRzATuTgMsIa1Sb9ZG8pOK8qSH8gqcnowttEZtso8Em3P6EcoJQcWBzIT_CpFfblgdbVXIj6uHWO-bshiD0QrBZRUYkUc759U0SE9EaWGowRNZzRVJjLD_ouZvoMGkAeuwyMZDi_Gk4C_jez0UuBNhjxgivQiqb_DELCjlKj_iNAt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OZ4viPEc_Gw3eoYZXOsAA135tLhO1O3LSPCRXPmAno-dXO_-4-yVvrvfu-kb6r4DBeDyOPfHIw36QGqaEM8Yq2DoOYY27wNefpnPKE2DNRaDWm41qgOY5ZbPldpyGZYJ8YA9GXecYoQ0OfrMrllIQgH2uSKbHgZBR2_lSnsHGXV9cda064GpaDJIr8Um_tCu5HLOhaFekLgeNNDnP7ardkcR7Um71tyuATTzNQKkCOZUDC4MsUYBXQpCQDPjsF0b_4biZBsvKRr327NG3B0GOpg4HI3RWwlZKE84MxGOhsO50LHkaG8ZQLT-DjdwzpyJLPzXhdQsLOE-hn5AwHpJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OZ4viPEc_Gw3eoYZXOsAA135tLhO1O3LSPCRXPmAno-dXO_-4-yVvrvfu-kb6r4DBeDyOPfHIw36QGqaEM8Yq2DoOYY27wNefpnPKE2DNRaDWm41qgOY5ZbPldpyGZYJ8YA9GXecYoQ0OfrMrllIQgH2uSKbHgZBR2_lSnsHGXV9cda064GpaDJIr8Um_tCu5HLOhaFekLgeNNDnP7ardkcR7Um71tyuATTzNQKkCOZUDC4MsUYBXQpCQDPjsF0b_4biZBsvKRr327NG3B0GOpg4HI3RWwlZKE84MxGOhsO50LHkaG8ZQLT-DjdwzpyJLPzXhdQsLOE-hn5AwHpJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Jn5iRGSNPpP-f6TirVtLw7OOL9IDNf-02IVzC7GGAuDi8Jmk1aHgGyW_rI0obX3vakvWQgB2ZzqGSa48e821VyBN5qxHsYePT_cmWT0Ijewu169zr3quD8fAn_0xReZJCPVBo4Tl3TuGXpNnQ-dANHMxtWbgaEZqMsG16f_2EEKiBwNhlbWrkoNpLCnN0FTfrl8gIW5R2eVSEpCeU6-lvqrHjBTJ1CPVctN5EjGb9qcDGz4yjg5godZYCAZUiFqLCK6cJZEHssRz6Y1P_oORnGd0kLP6HZzzorq6Rd9A0BZMJQmkIm5EK2a_txVtIBbXxy7P0nGgxcxZR07t8Tn0rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Jn5iRGSNPpP-f6TirVtLw7OOL9IDNf-02IVzC7GGAuDi8Jmk1aHgGyW_rI0obX3vakvWQgB2ZzqGSa48e821VyBN5qxHsYePT_cmWT0Ijewu169zr3quD8fAn_0xReZJCPVBo4Tl3TuGXpNnQ-dANHMxtWbgaEZqMsG16f_2EEKiBwNhlbWrkoNpLCnN0FTfrl8gIW5R2eVSEpCeU6-lvqrHjBTJ1CPVctN5EjGb9qcDGz4yjg5godZYCAZUiFqLCK6cJZEHssRz6Y1P_oORnGd0kLP6HZzzorq6Rd9A0BZMJQmkIm5EK2a_txVtIBbXxy7P0nGgxcxZR07t8Tn0rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTQyyMw4xX8Ui8R8aWLh7D_QT9j9XEZ2iz0OXD-VjbSb29sTE5PoE7_tCXi8MwYWZ8vdOVENKvTAUvL8BTxuv6DUBmScBe_RUIFAXWgEQHy28y44ueKOXdPkVVWYlqTyF7svEywvdc9TRhxbhKfKpnZXaHt6h-AoCmquBuluKoR4s8_a5-DBRXC2vwnp2T5ByeOd8cHrSXyNnt1svwWHnjxsxv3SWvT7kf-XO5fYjOxEbqqClkdurvE35EqAW3fF2ymuYKA7YelZv7WhzUr1Tiqpflnu5Mua0VpfepcwhdK4o67wIDUVIZWn8B5d4PQhBWPv0kmnrlEyfwPZJCBCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGzf9niS-0PBP5zCwQNpDXCG60lvkkIxYUMeMCDI5B9wISjEDeD9z9kcubc9hVRxS37Evyv9-E7y43KUqWb92dzBVrZ6qbUWObbC5eX_2vb_wErOqduBcxRsWixLq_WDmmUFnjkKiAvpZkcngix3PF4hXB3jCi0juKvF4fuiTjM1mgLC3b4FvCa00lC5n8J2gGZDuuk9BC6U8FjTzSxEWVVk5KLn95q-IkdvX8L-2gncMIrk63hj_W5m2MuvEl8B6YuQBT3EFVbAkd0BCKUW_d2M-SruMYh8rJXwH50DKwqrgybpoACKW8amtjdmkPpVKI4X6tBjVwjCEGaTlFTjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsDbZQ0LfBJOu5YiRYyZbyBzX1-ck8bcUuJ56NUub3c4DOfweNtng2TFtJWL3VfhUxWqjBUYZ1f00RT2dSEnvoCaDO54oU9ofd3kPy0kgTzDzzsYVYqNYb8erqHO0a9th-_Mw4MrKuZTYr81ek2VZIcdg4-J-HBshiAYjj8rWnoq2TgbqRmLSxvkBAE561PC-apQVuqR8rpNTfWvOX8ZE8hpImkmlrzYoay8KLeyJQ0fZ4eVtoPXmBSvu7MQwx8LbzUccRaAf8yLLoA83_F-EpB3vVr2XQQO7YOjwwQT-izTSdH9aafra13y_OXwm9g02wyLc-Hv2YAyXFBM6bijQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1kdwWY89FYmSfWYfrD0oZ2L6AN1fhLFbmzf39lxp-jqd_rmsDmyXtAUDdPW2BPmg_KphrjCcWshPlHmTvsRxQU-OOruXHc7OkcOOlAH8PNwSnGRlO1spUy7U8JHnz6JbB3WNCR36PvwN-sfuB9RzetcXvHfW_nIGWEUct5--1UJ5FVbwfZRdgUa0wzE3zeW2sC7NHSpoa6gnnC81O7cWRsMywzY5JSo-ES4mR9_50J_ys2TbaMTwhEJWxxyTDCKTJe4emZ2wFuLl4gF9x82zPpoKMvCZcVuXd1ZG3k2yQUb2Wh815RFRTB-WL3E0AXfOZBAwLWXHMuwhT7217gi7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJSV1ZL0rxG7RwmEf1ou-h2BxLhe7QzHcsSRsRs3b4Ff1vcrS36ZibEKzweRF-3ovhAMyUTh5wemLYJXuAdNR_0jlqGR9KpzBfykWdFZFfF2n-Ftql1i65Q1BG2tqE_-2zZKf6WaHr-3Unfy7FWFigJakBjCDbahFPh9TrGYfXeseFLxSVyDblY9Dgpr1JzCAFDSVTyI9Fi1LCTpb18mCQg2Ezy22p2v7-1U2yKvLHyP80rPjHLVSlQCE98ny43zhYIXCG0gRkfRYFgmZgW_UaQOdFOgNiz3QYP-13w2tVStkZTHZetGnyYmYCg5XWp8xJ_m4a76CFz_yUbYwcqOTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyNJ2Iihp619__stvY5Dsz_m9FSbSQIPhMOPDmDDt6duLHFfZlQBOaOJqTbSppAkrBeBgoiRAnFTdNzFrCdu7eUkzL8wqXfmb4gihTQ2sx7Qv2mdAB9jTQg2Rb-dtj-1f9ij0Yf-Hze_6YcVi1kN6AeVskgjLO_H2y-c9wm3-TLAOPsyEXpbD0QYf7ZUreEMRGj2RfpZdjZe61uNSFC-TDR9lDWc9cU-TqFj1O7dFfDjkxXXs3hjgCUPcHfWPEYk7tiAnlb6QpEYfZr3ZfwZCPoKTg-FYfUXMy04yJtnLvBi-O4frZVqjQdgpct0OMi7oE4p5JZfHC2W0IgFDz_ZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKx27aVJJldPSYvo9cpzXkv9kTyTRdzfn0adXnUYAbeNq0iPd2Qul_tKNUCFFPc_Nz14dF0dtZxoZqSjTtxIXpMOYSdNq3g9FJAWozmCDwkaXYnhV-fuivu0PfndqMc0G1PuWtsKyF3jgzS2a2srDfNe55B_CmePUXYpV67SXoju-TkJ-3sxMurbJor9MdnmvP1oMZRibti-z5bsNUgYDj40dlbkFlT8Y8UgjHj4QnvzB3xgi3TNBVcPccvi8B40OnW-_rbh_adSDLAkQhkZ8pPbmzo1_Afjk2HMd4g7NWU84Zfi4j7IfpwTieRAzSItiWzHiCDf5rU2GW3fC5gb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k10QSMVnH4RAdfGm6SHyjG18-r1hYlWHYIf0ru51ukNnvWjcVsUyAWOpBu-bXzzi5xg6gdUk1mgu4olI-EBIp2i1K29sCdluqICcjYrKKHWOxnPxjhHBFAAO3LnYGVbs_oJ6OnL3jj9GGjCeuYEsbOkUVa4Ya5ml3D_KpIM3Z-OHEbxHHS2diVWwu7Zph15WN3OQr4vFJ-22wIfjocKnonyRKE04YTU1U6lxa8LcSidQThanpD8ek8IoRq2_FRWRcKp24wQgqSjUwXB2nhSezI4GmvKJc-LANMS2ufomSHefmoPnlCWEq9n6UUxbJgl-uR-QE6GkyfRga9INKjXmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFI7vZKmaWoNkSTd88SiuUaH5kpXvCo4r596ZzM1iSBQqgesNV_JnTnLfHMxcWlYoR-qpI3jfFrN5P_5k7t-yhwtDRSV38n35t6FManJXNvT4CgiXuAn0ojVYzpMKHJhp78dge3M_GIUHXALNFMr9TMu7ps5DpEIpzUkYCcaMDL-TInls98hfmQFvODM9dVnrbTTwGYZriGlBuL-Yr4Jh6IKPod7R6d8Tp3AvH3FGbhzI8F6bIm-cnZKd7nmuwwwa9dmiKxud90uHbQSgH0iOTdYtfgNs_YOdeXuBE4ogPVeqdiyCEQtWPOmke_75kDbzy1C6WK2-3a9dInjuI9TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVLxVpjI-dsOfxF-8ycIli0_7P3YG-lKRSAO5KpgZDxEtFrje038Dl7kxAcqbzwd0hP_3zKaSC1_-AymC_ubNjacS2405Vhtu8b8j4syUCKyzexnDOMzPP-Hp-C1RxmcxOl23qcQWX2-xTLiOG9txJrB_q_U6Ibp8FnngVMZiy52KTdN0xZsv_QfQV1r2Miio6w9znps8n7qBLCaO3zJ-A2_OwXHscrfx5t67ha_jWQQayIofwlkI15IOW4KNrV99QUX_fJ5shyRQXnM8FMVXGqotuIDHtw3AOM1VkAI9ljKMpZNyUvwtOw0sVRWP6qOR2UgF-kWyvc10DDOIYHSag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=MqDtP2CAPeLIH6_ovPE72jYrTE9mmxfapVORZ-sY43F37imQ0Ka8_6y1l4rKtRXVe4nQeo0epBq35sUZNuxLGJvTibvTrRsWlQ9ZA-SaabStLwd_QEKL-Aev8OqIuyVqYi4jNXYD8_Hr7091BqLkZSg07F1qQ67pYTacHUlvUzN7D4kJ_vmGIWDVjWjg7RYgbZh7sS1nGPbEFuf-sYITAHV6E_RdgzZ-DwI_3YORE1VLJEjwtIavhiTOO6R-f9aj-ov_NKlg_76BAH6uYlIusTRwGkQW77GhOF4eUSMCyzRg5-Np_yteWAs2Qh7mSgSVmLs1RfmOUn3T3y-lnz5RRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=MqDtP2CAPeLIH6_ovPE72jYrTE9mmxfapVORZ-sY43F37imQ0Ka8_6y1l4rKtRXVe4nQeo0epBq35sUZNuxLGJvTibvTrRsWlQ9ZA-SaabStLwd_QEKL-Aev8OqIuyVqYi4jNXYD8_Hr7091BqLkZSg07F1qQ67pYTacHUlvUzN7D4kJ_vmGIWDVjWjg7RYgbZh7sS1nGPbEFuf-sYITAHV6E_RdgzZ-DwI_3YORE1VLJEjwtIavhiTOO6R-f9aj-ov_NKlg_76BAH6uYlIusTRwGkQW77GhOF4eUSMCyzRg5-Np_yteWAs2Qh7mSgSVmLs1RfmOUn3T3y-lnz5RRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD4R6uivKqbIQxWV0ydKhQWReqj5G7lCpmMosby8r3yVtxWwI_epYv3NumySv2nMOS3tVKPZTBUEBTNmGTHcbxUjmfDLFZSxVmvj2lweM8A9U22eW1BZnTX18ruMUJj2tugSpRh_KizuYc5VA3iSggAGyzVFRrpSNnXjeMGfPB0ZSC03cKMNb5L9NLFiZ7m6sDa-dP4K0XlZWCUGTc8gI7bYD0arIhxuYNfEqDEBgcEc7sgAoBlJs2bHQMjRIGEDckhVoDrxKqBy_AZS-jhGObQ43aDtFbLLs6x0WK4Yic7S1RUNniC3M6tiwdF9GYM7yPgf-BrRvEIXrYAAjB0GvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4TINgm5WR7KqdmUibGRHkmjAtw_1penow2za25MHczSPuu02ty16LohwrKlmS_oX2Prqyo0HAJg5ieVMEz8rXclHPAZ7hBHKIdqyk3h8j-30w2yGa-dEGBO_zkVWK9qdisxQyRL_YRW4PU2tIoTJmTmAWw5vrIJHEG5YyQ5dL7xtETPRWjP3yvmA0noPEWRJoSELkHnwQekqAAExE9u1LNSv3GFwhMy_gv5W52Q4olfN0mvbc_Ekf0uF1dMqhEVHfnOSAuqBrK2Sce0vpeNsg2kXaMORSgBlFDo1A9qcvdCVaztKslI0pMzFY-BQiSUxGNOkkUdbk2222HO8Z42oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=AsNu0JYdIj1J0wVsUGWF1l-30vYBMgxOCYRPCYI6H2JXd9CmR08Xwzfn0SHXUUJqGfKIrb_rvsSLlfkMFi4k7ca0I4BKw0djmcBfKoLuZFCv4e1F-rZMMjZMt-z-k9NPdXp3RY29E1aHllbccaRYKnCuJuLzqja0KDE14YUGTqsM_FOvX6SXOPfJaf-vRFAg1jvrmukF6yeqtJuK6aLm_kQYIxwlAUIPHZmswDrsJtLEZXEqw9400jAv-aqsQYq4uppTuQHOBMT3ktxxvZHcc8Rj_gvg36lWfzahD3mRfOb6jeU5TCJ0T896S7zN5Kv928ipBZng4sT3Msxc160pPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=AsNu0JYdIj1J0wVsUGWF1l-30vYBMgxOCYRPCYI6H2JXd9CmR08Xwzfn0SHXUUJqGfKIrb_rvsSLlfkMFi4k7ca0I4BKw0djmcBfKoLuZFCv4e1F-rZMMjZMt-z-k9NPdXp3RY29E1aHllbccaRYKnCuJuLzqja0KDE14YUGTqsM_FOvX6SXOPfJaf-vRFAg1jvrmukF6yeqtJuK6aLm_kQYIxwlAUIPHZmswDrsJtLEZXEqw9400jAv-aqsQYq4uppTuQHOBMT3ktxxvZHcc8Rj_gvg36lWfzahD3mRfOb6jeU5TCJ0T896S7zN5Kv928ipBZng4sT3Msxc160pPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Lv6A5Tdz2P9OHYbccB1YuvOMEvQA0t1co_gaMr1ju53TOQZ5KVhibY6A1XUR3wjaD70fIFtaM0IWyLKcuNGkv_Pv8vlIQo__ftarBAD8MWuguASdqPHAPzc8rY2_Z9y2V7-3XQOuZsmScb6KMFIHQsYmfYoKq9vuVRhLxVBsIW_D5r6MweJ4hXV7UvHslaH4sJ0mpkbvKoRAxltFKZRYcf-SayZoJkfCFizgYKZdONmCybV1YV0GluE1DN4jYDdTblXuRRsvjvqGcHEVCUV9_aPxJ0cWjuYZ2Ss7rEIuQ8i_vXRuxReX7hJUSGyxh6VsKc9J_rcWZWODmgcIOVrGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Lv6A5Tdz2P9OHYbccB1YuvOMEvQA0t1co_gaMr1ju53TOQZ5KVhibY6A1XUR3wjaD70fIFtaM0IWyLKcuNGkv_Pv8vlIQo__ftarBAD8MWuguASdqPHAPzc8rY2_Z9y2V7-3XQOuZsmScb6KMFIHQsYmfYoKq9vuVRhLxVBsIW_D5r6MweJ4hXV7UvHslaH4sJ0mpkbvKoRAxltFKZRYcf-SayZoJkfCFizgYKZdONmCybV1YV0GluE1DN4jYDdTblXuRRsvjvqGcHEVCUV9_aPxJ0cWjuYZ2Ss7rEIuQ8i_vXRuxReX7hJUSGyxh6VsKc9J_rcWZWODmgcIOVrGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaRXGFSkZUB1XcVXpQF1jpiZFvzXZhV_jjXxqRjbQpc6Xnf_4rJRabG2EGLXEbnbg9Y5nQjr7ZBW6-OiNIf1uVNFlPE8rWCRTKc-xzNQmAG_kk_jDiRICI_nwzgSPSsRVUQ2Mq1FU6CboyyI3lKPQOzLZYajmMc4QNJk5S6--wLOTsCmwrgJfuvYrFUDz2VZFszaawQM73lw0yi2CE9iRhQd3HpsTAu3ID6LfYh_DoPJRZB4JrXqrciFvXBSMmfD-bJHtjqj60DFpawk7XSnoTAv4bu9sNCuCnNSi7hjZnlQC4DcLS1XAJU5-En5A-JXS7qxfcGPk--dmUB9skuv_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0fN89-br9J6BTdMkHNs3S9ELN0riLXHZt-UnzVzc0fz1AmaxHqn7zHDozABMsrILKkqHqo3cCA1NdDNA56BqxUIODYV_ci1NPizOcfiRzBk_sQrRVwhp555Rz8-BySGr2k7PqAfuRlfLoRsf0da7Gm4t56ne7qdzPZMNytM1X0YKCOnbm7Lc6orJuGYnj56v0qzJkEG0vMtMf7ESed6SzeI7oOlBgXJGutvdN1z7IOR2Pp0W7bpphzdOUAHtv4Qz5qKPdrt33VMcPvYNU8TkfwmagNkbZPKbQ3xToAsMdVhp2iuo4sUxDkTsdUkhjsHIHcFI_GZBkPvHtrzWLVuYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxiUWffWRYlGlcol91tVWxnkUvOnuiSay5mQqbwwK0rGMgykdExl7J0HRXpoOP0Uuj_uFOqDp1dSk0UgdmxW_-DwbU2TPU5tF13vrfc39FoI93ZjkKAXiwYN0hFE0xnoBLVTYAKoU0PikH7XFNK_QLFRssWSZZLI1OJW3w9HYMLRc-iU3zgb2TORwm94FGI7wL2cVGBTXWZvI4s7p7e37Ks1FngAK0_h6GtUokfqEiaPqGoKf3koM5SZBkKawwJmxA3fiv8Ut7h8sv-5_zZRBBLxdghxSjDrvSdj54m3vjj__kkqLEq5BGxqwx8uxOHCROMUxtpQKQwpS975a7L71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B51cRNHNNbNAYsqmZnUuM2896jOtcYvRO2ZiKLrCz0bmuaZeQ2-yFnOLvUoNzsbyfkEavTRIuNM4n-Z3Pb-Gkk8oWIbr7_dixoWg7onwCBTEJ2O4NMq96eUgfqKm1_636TDGHs7GgbpUz_VtiE2bhPDQERdd0zV68B7II8kYL0zZnU4N30xpLbU6BGyS_TbI8Zhih_OKUVnUVUTmWfqlF7L3GG7b-70V4vIkpNOZRvk5O_c_TVkzPIGtJy5dRuoSRpmSaqiu-ZCukHZC4NVF-tIR9I3a-G6iiqp5ukEsR6bMXlzkgvP-Nxqah1kJjSyVJdM378aA31Qk2WQ2Cg7lAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXP8Vvhnz_RJD6H3yZedPN7EQ84o67Y7T86QkcJ84UkqVS5vpH5eSmoLxEL11oZpksbc97psRo_wTtTOn8wz6eWEPuKYgpFn4goHsyqbOzfhv5ikqiOQTt6jSJjMTC3mKYgd81_-uzM-5H6rQNG2exmXfMdi5E3cntSm6YTQBwqTjqDyRBZgBOvmxFu-0W9KtjXRmPJbLvRkk0Whpd9HynzeTjDZxrDYFLV_nr958UXPgGO59eB3phCFCHzq7PLb89knPieeHuRtnrZUZ54Bf_0rSn_Kjxvii_D0NZLP1etmyO1c0EH25S_li1SGw_uAMEyGSxkvyF40xdpq5rpmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uza6TZqUZgR89AjODA8d5XgK2j1_kftRFZ6H3LixIEylnFYbCHiFxT7hE9-IQYp5k8IahkNNh2wsiNf9-vPwIKvh_Psxane1Lt78F9YxUYShuORzEig2DHP0R5klBzWPt9VytCG_LIqCqyggDWMXpbEMQ2arPs3hKNUMUfF8zzTGVDx9mdSfZRYAnGh0gdpLG53DUFBLC6564NNLpPjA-uPVd4ImoUvv_E6BESFmFWWI5DhHAe6Wg1RprS_jbN_mxy_TE38xNa0_zpBAf5YtvZ9G2paM0j74d7tw2E5bZn3JlGfuC-Dd6yrdaFu44MrXT5TChBfV1UYi51ua0Goojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqvVhSi62IZYFEweaNF5lrpmAn_Rz8TzlKYEbEFCgEwBoxuLPFuz7B1UcU3Z5h8jR8DC0HniCrBtTTkWezlmCfNq__2BGYEbk4yTnHnUS1UVoqBW_Ta2jWHrbDLZiOk-ZFgauZd8aZUkb9V4nzSAbrznpGQEX8k2f4n2mGDNd0pLXRjS3xSvj9SOxHvHVTygOOxjqJ1JIiG1PPs_A_jY2pHXS8ltTfzdgZDubVQaq1TzxQKXKXVliiaEEO7fM2OvfNom2lawz6XsvVGf-a6ZS5zZDY3uCI6K4sTdW6wtZGE5S-F_65QXANLsWF0tZTMzMn6ifcQRXDkE3hXuPsg_SA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=T3wxmrNL64M3U9Batt-9D-MtrlX6ZxBWq-2ZMvsD9IjGbwnnHq1PNWMAIETi9RFOH4A6_E5I-EDkGKOzHRPl7fToSpzed_bM7xTajJSrW2WbWWHGo1HcrbykAoHHKidSHaqhGwEwCx2tsst9JsgtOzjlUSBCO9exXC5nKQJNM4291NCpWHlPeQDesxP43ddV_3QxgPNqun_gv8Ewzzax-KJ7G_6x2uYpC0T8dSEIXa1BkchsS-wNm3EvhwtVgx5NWMu3VCGoyTYK5lnvGpD0Ekogy-1EAxVk89ZVddKWrf_v3fi1IMqziOn74N-QtMkKhxQnOS1AUSVAVaDTitRFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=T3wxmrNL64M3U9Batt-9D-MtrlX6ZxBWq-2ZMvsD9IjGbwnnHq1PNWMAIETi9RFOH4A6_E5I-EDkGKOzHRPl7fToSpzed_bM7xTajJSrW2WbWWHGo1HcrbykAoHHKidSHaqhGwEwCx2tsst9JsgtOzjlUSBCO9exXC5nKQJNM4291NCpWHlPeQDesxP43ddV_3QxgPNqun_gv8Ewzzax-KJ7G_6x2uYpC0T8dSEIXa1BkchsS-wNm3EvhwtVgx5NWMu3VCGoyTYK5lnvGpD0Ekogy-1EAxVk89ZVddKWrf_v3fi1IMqziOn74N-QtMkKhxQnOS1AUSVAVaDTitRFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X801nycwaUx4IIRqAWVTTF3XWnVTGspTLKbvyzECF3ynX_l58xk1KcH5wR-qRAwBAqlW_G75HfdM__iZ2zCTBJ2fKq3qVbN50LWl6TRQW_8ia1IFrZheZTjXZ00ehgynawVjF10ZAjb09DzU4YCoD9LTWWJFuk_iSi1--Y670DoUmIbcrY31iHoDJb6czEHo18Wub4XIB5PhMkHC-RVXenMbrwjLIU2PXkFTuT3FPOV133R162gkm0cgz9vIrzldWOhtipr5LUGaUbPOzPMDIlmsi_fNQCYEw4X8olzXiZroswcYWjmWtEtJYhkHhmj5d4RaaCB-bbVC6rLzeBtk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XARYYrnKlXhwx9xX9R951iWrQye2eUrE7HlSuE9Ucc1ZuHYiAxyFk_vLA-dq4cyfsGnIvK4KD4u00wGCADGPSdaVLX4Iv31FV3OPP0CvqHTpKhZXjsv9Lz9m4gm0M7L7xTwk8r23BvDPvp8cOEvyHULghCANGWtHy15EAdG_s0bXhXdbSe-diUDWYOyrJso-jDVwMRqQiCuBujgujRMfRrJAmRH8WjVGBJKCCwhkDmAPEH6HbgBDXojwUOQBhV_bflqwHyQdfDE6hI70x5YfuKVlmHB0UuHzsSheHtTr_jFj6A5FbIti7bypNm7eX7FvUIuUang2LSOg2m0loQqoBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XARYYrnKlXhwx9xX9R951iWrQye2eUrE7HlSuE9Ucc1ZuHYiAxyFk_vLA-dq4cyfsGnIvK4KD4u00wGCADGPSdaVLX4Iv31FV3OPP0CvqHTpKhZXjsv9Lz9m4gm0M7L7xTwk8r23BvDPvp8cOEvyHULghCANGWtHy15EAdG_s0bXhXdbSe-diUDWYOyrJso-jDVwMRqQiCuBujgujRMfRrJAmRH8WjVGBJKCCwhkDmAPEH6HbgBDXojwUOQBhV_bflqwHyQdfDE6hI70x5YfuKVlmHB0UuHzsSheHtTr_jFj6A5FbIti7bypNm7eX7FvUIuUang2LSOg2m0loQqoBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=FSIJ0S99aSd3ijRQ9YC92Xz9liRwRqKJznwJAJduJIWcEA2S5CFp4fURSDDiTxqjvBz-CQbi0UXxcLKA2raG7Jhjj2RPA0FqRyYXMdJ7B9_8HlO3s6sNKFdA9niHx_KYeWbKkMaSSkJttUaZapN1N_KtLJ24KBvm-9F1txvK8eSBZK0Y8X-PbpqAfBLwBEltCuetvJOyzjyu8M8qriB23la8s7j6_p9r8_BTIjxed93MlXykGcyr1Fh9_SP5lIcXj0-jUsysm1Dxvj37mZ85z4C85z3UfwvGu-Mz_hD9kAoTto0-nUH6QXGaKcsZQkPl91J_pekcQ1pLkcbZ6Fy2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=FSIJ0S99aSd3ijRQ9YC92Xz9liRwRqKJznwJAJduJIWcEA2S5CFp4fURSDDiTxqjvBz-CQbi0UXxcLKA2raG7Jhjj2RPA0FqRyYXMdJ7B9_8HlO3s6sNKFdA9niHx_KYeWbKkMaSSkJttUaZapN1N_KtLJ24KBvm-9F1txvK8eSBZK0Y8X-PbpqAfBLwBEltCuetvJOyzjyu8M8qriB23la8s7j6_p9r8_BTIjxed93MlXykGcyr1Fh9_SP5lIcXj0-jUsysm1Dxvj37mZ85z4C85z3UfwvGu-Mz_hD9kAoTto0-nUH6QXGaKcsZQkPl91J_pekcQ1pLkcbZ6Fy2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN4Qgi8trJbZ25FBIdvssA68zahUwQGJmxyWI4MT-992ZBHYzaKzfEUd3EFhcEHfb484_Zp7A4QbvWCUoNocj35feI11XZJiBBQqkM5Z3fCR03CuPr_WYfua4a8bgXY5KhzpgToZTqeQnSP37_BOw2Bt_NNnz8MYy8VddbAQXn9PBAk4H4YU4GckqJji0Rh6WYgAcv7eC78ZPlKfEOPc3HI00AxohUB18U7D-Fo_L7BxWtdzi6ajwe9MGc-3lt8aSAkSJwMNby3UuGl0QWHdSzHmvfMWz4XJUxZQKBuY6Xaz5PwDRxBlW7-BkdCClG-dVMOpSIvreH_KMqYM_Q1sqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqi9V_lLwkxqeWM_W6N3UBnmtYvWpIsjcGWFHd5Ir4cmeQpBGvhWqvlTvpPMjsBNKiN9m2ysaQDOhu2cvmA1UIWOikez1p1N9ZgPq3MSdBuxb9EioqSEDDKJ2w_LtxPWn7UyLDShSJBn7fGLvn09uS3yQ5ywl7xE4VNBKsWhi8nw1AGyFmWQNS4Ng_OerHiJjqCIKP4Qom9gxgGNmmynbY8bEbJX2qbYsCE3sWbiSuW-Ryj_kKlHWt44k8h4rZkM-vwD5ANBliN05UHSauIBofdrPfQl76p5Q_xt7WQCSsAGmRsibnBVvnztryRsCo9Gh5F3IgEzbO8gsVrZSZuj1w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=B4je03RL5hrruL9OHWGCpz8NVYG8dXfpppP6hjT3MYqM2_BaLcmGUmb3Vl_aRjuHifq5gzh0p_qt_7sY1B9B8RY_2fDC4zz5yiDBLOVr7XN_GkglObpUIj01PX0hIAnQtR-6lJQ9HYUwFg0-bVxAAN7C93guf2TeXTNMyPlwNdeTEk8BIrjW3mbGI6hkdjjkvJ66bb7GC143p5aVBlK9dMGO00PhIpYZWktT9FLm_xWEeqwkWiSw_Rp-uB6ZpYA41EXUA9P-yWzMBmdTmEQPSGohNESSrLTxkgWCCgYkeBkdg6hzpgzdFHhZtJSJChJlrc4aba2oLDavVuaxj4pijSCiGDFkubEHwkT_kgNe4iJZvJtO79WQJUE6qAblMck6k6Z358ideIV0WUkUli_ToYxglZmblJ0Q6XDbLyx3SA4Sp_4KCLT9vmxMVBoEKE_aBxy8j33UC2gMnqI-ngoPawa6PVT_WrtU1YGtooGLUfayIcIvCCyGdzQRT57GbZUpZJLV6w_77fyf6V0wk7nKWGbmIxP-xHxtY4XG3qiF-FYLQbcP51pm3KHvvPtq5-M55rM_9V2EYPjlQIM9RVVsIYHdnC-5tFSkmxRdseqRWqRuvjpddyiIT9je8Ssb7VfFpk42d9EewughHpN5s6w2jtbciID4cojVG171LlKE_Uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=B4je03RL5hrruL9OHWGCpz8NVYG8dXfpppP6hjT3MYqM2_BaLcmGUmb3Vl_aRjuHifq5gzh0p_qt_7sY1B9B8RY_2fDC4zz5yiDBLOVr7XN_GkglObpUIj01PX0hIAnQtR-6lJQ9HYUwFg0-bVxAAN7C93guf2TeXTNMyPlwNdeTEk8BIrjW3mbGI6hkdjjkvJ66bb7GC143p5aVBlK9dMGO00PhIpYZWktT9FLm_xWEeqwkWiSw_Rp-uB6ZpYA41EXUA9P-yWzMBmdTmEQPSGohNESSrLTxkgWCCgYkeBkdg6hzpgzdFHhZtJSJChJlrc4aba2oLDavVuaxj4pijSCiGDFkubEHwkT_kgNe4iJZvJtO79WQJUE6qAblMck6k6Z358ideIV0WUkUli_ToYxglZmblJ0Q6XDbLyx3SA4Sp_4KCLT9vmxMVBoEKE_aBxy8j33UC2gMnqI-ngoPawa6PVT_WrtU1YGtooGLUfayIcIvCCyGdzQRT57GbZUpZJLV6w_77fyf6V0wk7nKWGbmIxP-xHxtY4XG3qiF-FYLQbcP51pm3KHvvPtq5-M55rM_9V2EYPjlQIM9RVVsIYHdnC-5tFSkmxRdseqRWqRuvjpddyiIT9je8Ssb7VfFpk42d9EewughHpN5s6w2jtbciID4cojVG171LlKE_Uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb51kdGD9qCvUo6qAzEnaZZe7rK2igiVXikLUjE7yAhPq9ugGKZ_KOSUX5ZdaKFUs-BnfC-wFaRxH1K71MNZORx5aYjj7GzHkW9x8mn_MmINa4h4jdS8P7YRLoNl4BSgF5r9q2ZI_Sg9GVzsZGmm1_h8ww1KxGOh5vx-qx6QvVbNnTfjWTtS7S8BG6TCxQ8X79LCeCXyB6BUuxR1mtbFlVlvmBA4EWw4e-GyphnIF6E-vhMldoVodP7YZFFoFdplgGTbOwCAluJmAwUhaM8W0uVjO9Kg5z68nO0WFV2l8_Wyj5VmwOCeN7aPdkfYrAJWiHOZ9M3lJCdfsv3acMnM2A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=jeeeCtnDCy9dYwjJS3QfZ-Bd4vNW9sCCTUXqsaaF7NYEiD50KsFmuLFGdhiRF-Zj1p-d5Dbldum2SzYO1WzQ8Q5FuLzgswbzDS1mc9MpSqu8R9f5iFojN7MuVvn8iWPeseMc9J0aMywiPIf76QZ1yB9TF82nr5508CqhVPg2pUuHsB7w2uEGZcqCbssCLW9eAahzLxp2PTNJTnvwWXnjNeIWF1VVVuhV4h6LSZoTY75LiI3Cr0f9yE7E-UDeuo1OKuPRd6lr9uVmNOePwGcgx3_TqYFBgU1dyL7Jx8B9HAboWKx0seqIzVMrfYBDhpLGsK0jCQun1DVwh2x_3mabIyYA0Mi52p_b-JSuEhpsPa9myB2ke_u8YzQ1RHzTYfBzx76msikRn_QL24c6ticxmJQaBo6NQBflhKSbi5TDrxI9NsSfwiReHlv132DgmEc46CPnm4R62ZAkXuwK3Xg-MU_aAGG6otYaG78d-NsFk-LbfOeeoLq4rr3fcKz1Wg5bca7NtcZR-LpSbbuD8E-F0UpYGBeM0Ta_FnPzZThAXkHnQXgAPNEK0kLPwpjzmm9byHveu6zh9VWfTj_IKcRcuuVH3hPcVl2gp884zZNcdD1VmGFT0ta3KmuiGccGaT4SIx3-Iz3RtTb4PEroAouC3SUUaoO4TrBQi3g-GwAELEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=jeeeCtnDCy9dYwjJS3QfZ-Bd4vNW9sCCTUXqsaaF7NYEiD50KsFmuLFGdhiRF-Zj1p-d5Dbldum2SzYO1WzQ8Q5FuLzgswbzDS1mc9MpSqu8R9f5iFojN7MuVvn8iWPeseMc9J0aMywiPIf76QZ1yB9TF82nr5508CqhVPg2pUuHsB7w2uEGZcqCbssCLW9eAahzLxp2PTNJTnvwWXnjNeIWF1VVVuhV4h6LSZoTY75LiI3Cr0f9yE7E-UDeuo1OKuPRd6lr9uVmNOePwGcgx3_TqYFBgU1dyL7Jx8B9HAboWKx0seqIzVMrfYBDhpLGsK0jCQun1DVwh2x_3mabIyYA0Mi52p_b-JSuEhpsPa9myB2ke_u8YzQ1RHzTYfBzx76msikRn_QL24c6ticxmJQaBo6NQBflhKSbi5TDrxI9NsSfwiReHlv132DgmEc46CPnm4R62ZAkXuwK3Xg-MU_aAGG6otYaG78d-NsFk-LbfOeeoLq4rr3fcKz1Wg5bca7NtcZR-LpSbbuD8E-F0UpYGBeM0Ta_FnPzZThAXkHnQXgAPNEK0kLPwpjzmm9byHveu6zh9VWfTj_IKcRcuuVH3hPcVl2gp884zZNcdD1VmGFT0ta3KmuiGccGaT4SIx3-Iz3RtTb4PEroAouC3SUUaoO4TrBQi3g-GwAELEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw5lQA7ruBMGtYJs3bjbHbcFunA46ii8h1Z0xD-p_EscRV4ohdxnwMTJ4P3sD0gOz3JmW50zXaBVzhqtOrLXQmTzNbq8xLVDBg5gKtDBCYYdDBiy5Kstm4K5m-HywU2iIaNxpGzDh4_wMVMAeZrkiIGGD7W3G1a7FdyL_UCXKVFhYbVr5EXcblDOAhUwmuu-l6lQ9sJDTN-4FOcLjRkV0ZuIKbHsVu_-GIiQ74GIrJY7yX68XqQphEVsX3GainWldwrch8XghwPmHs6c6pqvskGbEFu3zKX1236j9FuHrzZgVzC6I-hUFP2RvGmBlE8oayLd0PekmSIP23hj7ua7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
