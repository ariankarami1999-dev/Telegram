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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 09:48:57</div>
<hr>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miBEryZsuOE2r8Crslb_UgMIj5UBOh8E--8tk7DnH14PKKZjrz4AaTsfOy7g1vQimhg5YAVJqOXNV2DlPYXBnHpCCrq9KlHssYkH7XPNUXjIaZEKSgUdFU4jlTfFng0O-7RpcYLHawrTJrPdXPwnPXc5q1Lav-ejsDKLMcJrickGF9LBYGTh9GH4_1L33XrpF0eF61m-zGQeb-HPzx5DGElxiNcL7KopY0uUBPSiwE1_0sbUAeF-LkxxKrqkqmDSwd4rIJTePHUoRsH6UoIL6vYfTYVlxeUHyJzMUz4KiJ6_VjNjD54p1MARACAfOj872t9jh0oAfbVtw568ZvTfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZbPSwhfBGMKxVmmllj5ywROGon3ZEERk8sYrDxF4_U8blpSwsNlcSDy-oza1SMNyZNzR44yopzrdJC54gc77TY2WvSbBOoxgJCoKdDlkP8v3yHQxd6IdGiSfDwnUKq7OBe0XlSKsxAhn2fJRtpfroMhyZgtV9hGHkOhM0ujRxF96AGYt76VJnu4Nihn2ICVkXUNYjs2wVmsay6AWuxAYC9jdSeOjiAZW-WyO8EH-vm_A0iAy5danmSPGsfZFBgdtnN1uoyxlc7LYSDJSJmcCkAti_Oa-_bsHpyRcd4nFJJ2K-P47nX5cDbSz3yEGtZOw6KxZ5jKgUnZgd6y8Ubhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jDn4zd-nSGvjb5rLcen7s1KazvaVk_QrQco3M7Hj9u_TqG0fujVdivpEBvImzZfGHjAIHC3PyAKJdD-FurhJaRzK5X_V6u2I2aua_nv7Kcti0eQF240xZaizhmpChNcxhIaGqihACWUM3jT4yVYQTx5JcoGam5r8mt3Pu-jfw49tOYuOHO6Dj8JxQoe9ND2eshutHgKMF33Kv3ZNrjWrdqJk86UGw2L7jhUOgkD0HQ0SFOxmrNCgaOkxsVztWFWF3oTjBUkLZ269dNqBrLI-9BX-nqu6Aanum_sq6yQdG4Owp-OezhNNIQwB64dkbZAMY5KTuyac6XZtK7TUP98hyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jDn4zd-nSGvjb5rLcen7s1KazvaVk_QrQco3M7Hj9u_TqG0fujVdivpEBvImzZfGHjAIHC3PyAKJdD-FurhJaRzK5X_V6u2I2aua_nv7Kcti0eQF240xZaizhmpChNcxhIaGqihACWUM3jT4yVYQTx5JcoGam5r8mt3Pu-jfw49tOYuOHO6Dj8JxQoe9ND2eshutHgKMF33Kv3ZNrjWrdqJk86UGw2L7jhUOgkD0HQ0SFOxmrNCgaOkxsVztWFWF3oTjBUkLZ269dNqBrLI-9BX-nqu6Aanum_sq6yQdG4Owp-OezhNNIQwB64dkbZAMY5KTuyac6XZtK7TUP98hyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL0sBMXVei0b2yfK9ciEkmF8V23met0IVVrY4GP_UyPeWzbjYXzTomXEPt0hhqF5frE7TB-NjtLzt1hIoJgyBGJpEW1fzJxGoNfbyogeEdg_ezRDxVexM1G8bjhobMM-Dy7GqVXuGpajP7nclZb_emb5a55k6f3iauLpfUjxkPIpDiwJPDvOeAD4wDf83GyZS0A1qxuawSIHuT7Dc__iY_CXdkbx8Oi9zwYnJkJmVMt_FRA1WIQiWjZwgA23lRstjrKoq70izsL_F9nyfgDByULrSchDfUUdRWeaFP3Tly2ZOlr-tdePHmNlg44Z-xWAXdt1OKfcnBkuKE8ZTvRVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kb9OehnaLTpbEyXzxOJZEQ-BLH12RjoKOyXdTLfHg8zpX8mI3gBkhUWajjtIw6zjbEZfoDEJnbeLMIElZuejJ5EhaMPpZF2A5Azyc4CooaozVm4wQbJ_DpIYEPSnpppJHd-6WMu6ZgiOIFs4tyQGi9elIxGqxJdJ07IFwn2mcQPoRSG_jq_e3FxPicSjBzemWTHYBJC30fQYfYUFBXUXkIUgIjcgpHPN89Yzu9nMUpv8KVDqtuR1nRee4dihNMeCLdbIbDcXOzLaX_0iuR4hNOntFiItcQJKeyBZx5wjZkikmQnlqcTW7N3A8KsNWwLk704f0Fr9ShWfsnX2jeF0FDd5gj23RKP-dCnhd_4MDzUWyyiYDxsxijTStAlRXCmmeadM93EUJXxBclL_PRXhauEL_cMmnMNMZVqcQL3GwkP40D8DGrxH1rDSpUDTNZF6LTfA-fk6tozOicdoYGUYyd_qAL_wzEZgXr_R3ob0igAG7Bp9MU0w-rsDHiqrRGHScmpsxdJiys7MmpAvTylehGcHtIfNuMcFmNLwNphA1IS1VdFCvvj_PdtOtzhNaFO2ZrM3QJIN6O3ZirAfWAV_6GVx2hxrPK5jNTY-NfxwH9hm5rPL44A2oiEVcnBLPjC5c7j9XaP_c_Zuh9CJ4cTjgZ015WbcuvepOjx664FaJYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kb9OehnaLTpbEyXzxOJZEQ-BLH12RjoKOyXdTLfHg8zpX8mI3gBkhUWajjtIw6zjbEZfoDEJnbeLMIElZuejJ5EhaMPpZF2A5Azyc4CooaozVm4wQbJ_DpIYEPSnpppJHd-6WMu6ZgiOIFs4tyQGi9elIxGqxJdJ07IFwn2mcQPoRSG_jq_e3FxPicSjBzemWTHYBJC30fQYfYUFBXUXkIUgIjcgpHPN89Yzu9nMUpv8KVDqtuR1nRee4dihNMeCLdbIbDcXOzLaX_0iuR4hNOntFiItcQJKeyBZx5wjZkikmQnlqcTW7N3A8KsNWwLk704f0Fr9ShWfsnX2jeF0FDd5gj23RKP-dCnhd_4MDzUWyyiYDxsxijTStAlRXCmmeadM93EUJXxBclL_PRXhauEL_cMmnMNMZVqcQL3GwkP40D8DGrxH1rDSpUDTNZF6LTfA-fk6tozOicdoYGUYyd_qAL_wzEZgXr_R3ob0igAG7Bp9MU0w-rsDHiqrRGHScmpsxdJiys7MmpAvTylehGcHtIfNuMcFmNLwNphA1IS1VdFCvvj_PdtOtzhNaFO2ZrM3QJIN6O3ZirAfWAV_6GVx2hxrPK5jNTY-NfxwH9hm5rPL44A2oiEVcnBLPjC5c7j9XaP_c_Zuh9CJ4cTjgZ015WbcuvepOjx664FaJYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lbXdhSjAf5Mb68r8uaEekxNlXLmQuOZ7HP3fzfr5cVpvTDb5lVB2IcvRtYlIoTBk12LIgvm7KIyTpExt-MVOXu0h5DLOEtrb0ugTQEJ8Q9S2zdM1bjqH7qEl8r1Jk_6srhRTQt5FCXAscLE40qaQRrvtxuclIxWTGUeXXxWCX9xR6QQQdCsm3Ms2LgM-t5i-2wR2NXBlRtiRf4JANPMGgf9sTuomNiyeA2u9BYSnLY2p-C8lx1wTFAQxQpObPAduV9xNSJfAW49PrlXMJFyC853941XT8r_Ef0X-S4bhUQcNpP0nRVF3mLn1wp1pNpP7sL_54R6qXyWUoCayA_Ci2XZHYO0jJJNCXtwRjf-wfcwmTpFmmL8oHtHSO2NDT4_7ziRdME3VGRnZy5MVmxlQX5WP3VAqBEaWMIzEOq1vzNpgX09g9Z1cxhJXYDeaF2oIjNccp94hJWSA-4WvNknoC3V1KQpMQMJjdje_9j34nJe0dYq-KRcQ4FLshIP_177bVMto83fqE6kN-LMRzISvn4qntDEE7Wd1rgu-n3-lclzxOepS0eQMsYPDgyv8Ltdy08_4JYRCDgsR5fThBfn5uj3sirzt2pxNdmlwyL7z0zqV4LPyFFywVzpciWh-AcFCt49qLp8GFYqQm_kPwZyhKxE91JJQj-qehiCN9TdrXUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lbXdhSjAf5Mb68r8uaEekxNlXLmQuOZ7HP3fzfr5cVpvTDb5lVB2IcvRtYlIoTBk12LIgvm7KIyTpExt-MVOXu0h5DLOEtrb0ugTQEJ8Q9S2zdM1bjqH7qEl8r1Jk_6srhRTQt5FCXAscLE40qaQRrvtxuclIxWTGUeXXxWCX9xR6QQQdCsm3Ms2LgM-t5i-2wR2NXBlRtiRf4JANPMGgf9sTuomNiyeA2u9BYSnLY2p-C8lx1wTFAQxQpObPAduV9xNSJfAW49PrlXMJFyC853941XT8r_Ef0X-S4bhUQcNpP0nRVF3mLn1wp1pNpP7sL_54R6qXyWUoCayA_Ci2XZHYO0jJJNCXtwRjf-wfcwmTpFmmL8oHtHSO2NDT4_7ziRdME3VGRnZy5MVmxlQX5WP3VAqBEaWMIzEOq1vzNpgX09g9Z1cxhJXYDeaF2oIjNccp94hJWSA-4WvNknoC3V1KQpMQMJjdje_9j34nJe0dYq-KRcQ4FLshIP_177bVMto83fqE6kN-LMRzISvn4qntDEE7Wd1rgu-n3-lclzxOepS0eQMsYPDgyv8Ltdy08_4JYRCDgsR5fThBfn5uj3sirzt2pxNdmlwyL7z0zqV4LPyFFywVzpciWh-AcFCt49qLp8GFYqQm_kPwZyhKxE91JJQj-qehiCN9TdrXUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KP2waT-tNlRjZGh4jAG7AJUClsNVJxorRhM5dyU0xAtHGB6fDTy4uiSo6fk7nuaY0TUIKN0aC1WyE-b74xymn3AgqBaGkygJ7bH3q3X881rj1VTdNybaH8XG-0MHnFiac3ujJ28H_hRVcmWbjWj5dmfuGC0KWA6EGum_eerkyRQkCcsPRWglSdcJUTM9EZnswu9Vcn4SYI_XmQRmiswQIchgGUtZgrM4MIY3pHfPtC2rOdiTO-ViYlSmvcWKgwCv3WJtIGgLaG4bMtbhgKcTYROS7Y4gll_h_iIK5hRshxwI7Qe5Y2ZDUKo1Pyn6bY0Ejn0ksMGLHG-pKI6fqWbrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KP2waT-tNlRjZGh4jAG7AJUClsNVJxorRhM5dyU0xAtHGB6fDTy4uiSo6fk7nuaY0TUIKN0aC1WyE-b74xymn3AgqBaGkygJ7bH3q3X881rj1VTdNybaH8XG-0MHnFiac3ujJ28H_hRVcmWbjWj5dmfuGC0KWA6EGum_eerkyRQkCcsPRWglSdcJUTM9EZnswu9Vcn4SYI_XmQRmiswQIchgGUtZgrM4MIY3pHfPtC2rOdiTO-ViYlSmvcWKgwCv3WJtIGgLaG4bMtbhgKcTYROS7Y4gll_h_iIK5hRshxwI7Qe5Y2ZDUKo1Pyn6bY0Ejn0ksMGLHG-pKI6fqWbrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fuDmV2C0ch4RWX_iqzk-cgBUUD5UYaII9h4gvZwBt_5fkxhnUA0biKS7YA_N7y9FB6O3qJjJNEUogE4m0biSC2XE7qDnetWovVEuu6Z7R8DQls0xsz7HRuW-6fr9rhUT1v6Lr9BXQzbOiGjZg7-iNEQcGp00DMZTOpsDaWMYPQe-Y_Lc_v6HkbQmkr-BIPfi7U3uwYQn4izF6HDsETk5t2OVC_qkc6VhFFBF_EN7yru7YW6j5ZHjIx_8cnjfFf9JZ5Yr8gUoqeLyGBr_xvNJApd2B6AYkaIpiAAoqEHe-p1f373RrRd_IZ67XdTtKztGoPwsCSLvd7-wQfiuS3omtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=fuDmV2C0ch4RWX_iqzk-cgBUUD5UYaII9h4gvZwBt_5fkxhnUA0biKS7YA_N7y9FB6O3qJjJNEUogE4m0biSC2XE7qDnetWovVEuu6Z7R8DQls0xsz7HRuW-6fr9rhUT1v6Lr9BXQzbOiGjZg7-iNEQcGp00DMZTOpsDaWMYPQe-Y_Lc_v6HkbQmkr-BIPfi7U3uwYQn4izF6HDsETk5t2OVC_qkc6VhFFBF_EN7yru7YW6j5ZHjIx_8cnjfFf9JZ5Yr8gUoqeLyGBr_xvNJApd2B6AYkaIpiAAoqEHe-p1f373RrRd_IZ67XdTtKztGoPwsCSLvd7-wQfiuS3omtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlc2wp2ZMJGtzRCXHo6Z6RPfvBw0B3kJcmmPnu_pu1xC3gTrgvdPhlCwHJav4E7UqLNNxqOCQZHwKZ-APKyRrr6KuQjyn7VyPFsPvfAXg22hNU7uWOq4H1h0fcnOjvfo7U-qfRoHY-UBK7t1lLuDXi3LHU52khlegCObD4-ZekaWzGlvnI0q8birTt9de5Uv_YFftImNCF8l5iiohuIdyxERsKMh2KwBCHK0p5YNu_83lMRSXO2M2HD_b86d4Q41_jVVLUYM9mTPnr3grp_-1C2GcIoskcCG5eeP4-5zBEMdgGRrdtZMWJWVfu4pt7NUGOjvNC_rFF7Dim4wuLN5QQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MrQvRSytlKudmwTcN6zmmNFsDCSkoCKZ44GrqWeUP580sgC-ia4-sLclMAQyvEYSouncq_iYEnHTlK7TBcYouCV4uXP8BewwUBPvhOAUnjO_9lR30Wd72-12jhoEIeA9wFGsq0xERI4m3WpvGrlW3ZsglTkour_FRsfAYZBP5kfto4ZIHmLHuc2Ptlk6YKbaL1xHyoqYAnhRlOLM8olf-HIO_mWsn8ZOvqAL79j9cU27p4Kze4nFrwzgHaqdnbPDfz0Sq7L7skwGSuiUNxKj6rKOEqcZFfWJJW4oWTHjNBQynYOU0A6RqgcDlyeKaGsfLJhSrR9Z6CX2fz2ra1P2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MrQvRSytlKudmwTcN6zmmNFsDCSkoCKZ44GrqWeUP580sgC-ia4-sLclMAQyvEYSouncq_iYEnHTlK7TBcYouCV4uXP8BewwUBPvhOAUnjO_9lR30Wd72-12jhoEIeA9wFGsq0xERI4m3WpvGrlW3ZsglTkour_FRsfAYZBP5kfto4ZIHmLHuc2Ptlk6YKbaL1xHyoqYAnhRlOLM8olf-HIO_mWsn8ZOvqAL79j9cU27p4Kze4nFrwzgHaqdnbPDfz0Sq7L7skwGSuiUNxKj6rKOEqcZFfWJJW4oWTHjNBQynYOU0A6RqgcDlyeKaGsfLJhSrR9Z6CX2fz2ra1P2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Hrmmg1I8Pd0poOhpLunmdFAk46iBS1frJrxVlvFySHZ7hXfB15sgDmToizz1b7ZUVOc81l7i7n7QOYPLM91v7I2-5I56QA00AkD_6n1sNyiKprNz4L0H6KECBc32vckbn72XgFbJJ-I8GxBloula3CxWjTrUniBf8GpstsJr13bY5vDkUxmRLHrbBIw2-yN9B2c-9z7i6pvLqRK6r9A7IQpNYxWX5wHlSqzcz6Hhjcg7LFVKJeesnvLR_D2mjVESRNVSpexDZ-WOxfwnRkzglIMxG2oRzOfLxh62dyPg_HsXNHunwx6sFTVzDLppyaYI4vxsF1QhmEckT9urmkGpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Hrmmg1I8Pd0poOhpLunmdFAk46iBS1frJrxVlvFySHZ7hXfB15sgDmToizz1b7ZUVOc81l7i7n7QOYPLM91v7I2-5I56QA00AkD_6n1sNyiKprNz4L0H6KECBc32vckbn72XgFbJJ-I8GxBloula3CxWjTrUniBf8GpstsJr13bY5vDkUxmRLHrbBIw2-yN9B2c-9z7i6pvLqRK6r9A7IQpNYxWX5wHlSqzcz6Hhjcg7LFVKJeesnvLR_D2mjVESRNVSpexDZ-WOxfwnRkzglIMxG2oRzOfLxh62dyPg_HsXNHunwx6sFTVzDLppyaYI4vxsF1QhmEckT9urmkGpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=FeT8RW0YR9kP0b3Iz9dJr2WU0T56RhOCSA2HNYW4t-KmhytQQ95GrN5uly382iAyQ90qCcZSXSXaDv3zICN2U4N1abVaD6sHnNF1WARE5FjZ1aXiPM3k-77eWQt_L7bRw-nvpx93KwquuS9dPGpXlJu3CBzupk9d1sADekZhSlndGz8OSv7t7aEJR2UfICPfB-RolfbxBZQIy1mQw_6KBZUkD2Qu078S1vhKOod9iMOgAhZ4FMJtBijQUHucmjYFc1V9WWue0fN8tn35AQwv98FnVdzNXHoKy3zAFoyhfCguWPsGpVgyvW7_4WYO5EjVHhu3G7UdOO4Tnzfxglmxdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=FeT8RW0YR9kP0b3Iz9dJr2WU0T56RhOCSA2HNYW4t-KmhytQQ95GrN5uly382iAyQ90qCcZSXSXaDv3zICN2U4N1abVaD6sHnNF1WARE5FjZ1aXiPM3k-77eWQt_L7bRw-nvpx93KwquuS9dPGpXlJu3CBzupk9d1sADekZhSlndGz8OSv7t7aEJR2UfICPfB-RolfbxBZQIy1mQw_6KBZUkD2Qu078S1vhKOod9iMOgAhZ4FMJtBijQUHucmjYFc1V9WWue0fN8tn35AQwv98FnVdzNXHoKy3zAFoyhfCguWPsGpVgyvW7_4WYO5EjVHhu3G7UdOO4Tnzfxglmxdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HACKhYcTPrVdUzR5EIxRKwC72cqm-lFUwIs2yEHHhXfwMQ9eMI9EWnnKCa8lCoepC7ltd8bmrNLOpGliTYZpTMyw4DEnMZI8FxbaKRRrWh1s85L7k_0TlRsgFRaGkfP3j6BM15M1u_x5QxFlyz6pdZRJSCbk8GJngMghoobZ_-tF4sYC4jc0zbs9ZuJ2G7k0D9qjTp_idRvX3tD93reDZJTnGTBbIwaLqbN9-KNwZbBXmRvPyPcbA3Ek_yMWF54JjCg2UoXJCRZNTWbUrw0PMe_kvL1W5YBQax1LKUgd5i2xyE7FQ8S5Fi7PaAGj5ZzGWVQaBcVMMd7UfVfPTr06AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HACKhYcTPrVdUzR5EIxRKwC72cqm-lFUwIs2yEHHhXfwMQ9eMI9EWnnKCa8lCoepC7ltd8bmrNLOpGliTYZpTMyw4DEnMZI8FxbaKRRrWh1s85L7k_0TlRsgFRaGkfP3j6BM15M1u_x5QxFlyz6pdZRJSCbk8GJngMghoobZ_-tF4sYC4jc0zbs9ZuJ2G7k0D9qjTp_idRvX3tD93reDZJTnGTBbIwaLqbN9-KNwZbBXmRvPyPcbA3Ek_yMWF54JjCg2UoXJCRZNTWbUrw0PMe_kvL1W5YBQax1LKUgd5i2xyE7FQ8S5Fi7PaAGj5ZzGWVQaBcVMMd7UfVfPTr06AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8blRKebrrpJPoOjsVrz8izSmWdYdjv0Z_hXPV3_UTqeawfpWE8n1pjXe_WQV7ds-4hhibkV5GSFrKPG4_xQLaEg_m9LtwFT2pCEHBw0ncDu4ak2bz7Goezvz-wnZuAlSJzJlwCbMH8DqrxJUrY5nCad6DuFqGfcp0ChGyKEMWNCsEKaqWuYS4NvhVqJ6iyLI_RPORSagpjFOSmOilu9F1bpqa75irg-_Yz-8kiuCULhkHUIi7B0vgUrMCGIp05boJz82BNybzINtQVL98jHdnY2qVic2nmDg8cVmS8raf7y6cpUI_nEwD5wWmZPVlT-KCCdjPg6z6V9xjfnPkWVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=KjXtl0tRvbISUKTdxh8j3dmbdrVdPftjhCJ9zQ-a5c_QJpDM6eFQS13eXchuWmdiZO1diAPTqhRnSHLXvOtFK6cnHGC2Y4V2KLm8-nRM3hcExHaukCD8l9FYiixPq4ysSvee34-vNeHOiWCXKdgw4tstZ6aBdQc9iKU-MDgocPrbzIisUqN2ZjuO0cWm2Uunvx5RNzHRbMF1n3g4wTYjfyPDfZcqe0epiEyLKAWGtngt8h-u9h4kfxcR5A6Y9hHsHSOtZQ_u-7CcS91XKWT6Ps3as1F-UNqy492CVLqw9u1CrhQnPDsqfih7Ut7yqBHGUPMpGtAyd32H_qB3BwjD8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=KjXtl0tRvbISUKTdxh8j3dmbdrVdPftjhCJ9zQ-a5c_QJpDM6eFQS13eXchuWmdiZO1diAPTqhRnSHLXvOtFK6cnHGC2Y4V2KLm8-nRM3hcExHaukCD8l9FYiixPq4ysSvee34-vNeHOiWCXKdgw4tstZ6aBdQc9iKU-MDgocPrbzIisUqN2ZjuO0cWm2Uunvx5RNzHRbMF1n3g4wTYjfyPDfZcqe0epiEyLKAWGtngt8h-u9h4kfxcR5A6Y9hHsHSOtZQ_u-7CcS91XKWT6Ps3as1F-UNqy492CVLqw9u1CrhQnPDsqfih7Ut7yqBHGUPMpGtAyd32H_qB3BwjD8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TRAMgCl5Bma9q652N2d4pX5POiO9SbKYVUmRPdkI_UB8MN49eeSn_L4u-CBVrOczSKQgSxymIxvDjp9ylGcs8dFRSqNXSXSwjeXP5e7u96D4KVaVm99K3u8F_55T_daM35u_26Yz-eZbxiVOmXEwx7SuOU8yjZr6ph5h9eJiRHJ6Yn6YfGj7hKNUqczAOvph4Uj9OVCR4_2MfeNwjH4DeZeVgbHFMNcSMrCfGsnhXzrQVUXCwunN3UNSCWQLzm8HRN9whCNvyfDnNZ7sZuVKLzCIaMGAKemfkp1LxurqFABGt4oXDDp1p2G_1Po9yPK_P0OB94N35qdxftYRBujbsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TRAMgCl5Bma9q652N2d4pX5POiO9SbKYVUmRPdkI_UB8MN49eeSn_L4u-CBVrOczSKQgSxymIxvDjp9ylGcs8dFRSqNXSXSwjeXP5e7u96D4KVaVm99K3u8F_55T_daM35u_26Yz-eZbxiVOmXEwx7SuOU8yjZr6ph5h9eJiRHJ6Yn6YfGj7hKNUqczAOvph4Uj9OVCR4_2MfeNwjH4DeZeVgbHFMNcSMrCfGsnhXzrQVUXCwunN3UNSCWQLzm8HRN9whCNvyfDnNZ7sZuVKLzCIaMGAKemfkp1LxurqFABGt4oXDDp1p2G_1Po9yPK_P0OB94N35qdxftYRBujbsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx6Tk8OCUJci-mG-5Jnixek7spXoD3irCQOwkvRCi1nlZZ-UDJ0ReudIA9vkkLaiwEskFc5VGVHjVPaPN4XcZGbjoURAKgXh0QiCncSimrqap5fo7IWD9E3Ak8j4vEgmpQE0dFTqZDMmnv-XvLGXo2jHNk3UYDDt5T2z9p-C4mEayAutXSRwbKT1xWAWACiUQUbvNjrPlmD-RWx7p841njEoKuU8D-McObzRK4t9yt4wAlTJm8UfEOOwvBAVfT0MfSR5bZQ5PkPRJCLYKwysHow1EaKg-PiCnuuCk9RMNj9VoiktF50-eJdQE-PkWlAOMPOuuK2ZhHgsqnjtOzUXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOP7kGTLKMzFWNiNe8xZkFxvVlaTpSdHble0IO0zHkjwxX93qSvu8w_wyT1SQptjEZkUdiv8PnfiEcA5AJCD7tdz1kE49LxCxRW6yOzrOyjnWoOmctEtKWYDclGXPdxRM2KFV8AOV3y8GBfqHkiTM17wIYOGhBIJ_WUAxbSmyM5i-5UuQP2CHDNSSpFkZ9ASbZsWcVOoylmwYWkQGFB5BXAaSnGuykT3u_4YzW47Tu0Xr_Y9rfvTo5yogCIpjKUG-YtlRFzxoKkeQhssSuMh-WlfU99_EwfiG6sExp4IxB5j-spX_Yga2c418Ja1ZV0GhrpNwjWnKPvm-sHq5RyXnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U52eVhzuF8aktU021JbpwCSsJLXQtUhfh1HVnUGUMb3Hl8dQsPp_iCh5WD2aTV0AlPj_A-HYMQcWfjcAqzNrnjX-ebv1hoKvnYIuD0R7GPt_k65jyw-m3KmUcwwAdLk_qRt8kqfU0NGImsl-c2EOIg4ezpxlnnnCA1S_s3iDd3BYKpsxWLBbZ0G0faLmQyEFPRRYQpYPnmSbiQOJwqpbtLLYDpEc3UMBOHU0U7Ff3jp-WiMOlKN8JpmPzvQutzkGnr56V9R2eCRA5B_Ms97h7uIFBgiEQwRAu5gM9oQPazNwmQgYStTTo7S10vT5QbFVzoS4G5JEPOoX_llPds4e_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U52eVhzuF8aktU021JbpwCSsJLXQtUhfh1HVnUGUMb3Hl8dQsPp_iCh5WD2aTV0AlPj_A-HYMQcWfjcAqzNrnjX-ebv1hoKvnYIuD0R7GPt_k65jyw-m3KmUcwwAdLk_qRt8kqfU0NGImsl-c2EOIg4ezpxlnnnCA1S_s3iDd3BYKpsxWLBbZ0G0faLmQyEFPRRYQpYPnmSbiQOJwqpbtLLYDpEc3UMBOHU0U7Ff3jp-WiMOlKN8JpmPzvQutzkGnr56V9R2eCRA5B_Ms97h7uIFBgiEQwRAu5gM9oQPazNwmQgYStTTo7S10vT5QbFVzoS4G5JEPOoX_llPds4e_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O88L_qcOpGkuXRfXtD0fKEyKZfitWVUaL1U7Lss51SOVJ4otRAFdFonPizx0p_48GSPRZH5HXu0LkKVTVaeTsBNdLYKRU38tuMwwgU3X6_52t6lAq3gY_DYVTLJ4qPNiTrMnHQQ3o0snZI0_YGkoUfx1HAS0SM3zCYbS5CzDEUxSE3Z6FapO5xSWINRsxfM-CjdJlaFOm3qR7rcq6SQOqj39HBgrSG_sUgOBb4HjlWGXdrz85sfze2TfcIkc4-q5C1h6sR6QrGv65M1yQ4LhX-7IWD7ymoDnEU5fXVTzSCfBib25Qa1pgQt13gaKZHwRjI1MwYwRZqHwLZsXYWbGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtAZUGG7fPEZOjYHjasQi97m9O2ZTxVYG3fUPVUbkixZzY6QKN4JB9nRbQZvUO0bhWkJrEfEVaXXQ4xe6049sFfq4UWO_FaoArVmpVwPggYlBLexL0vh9CXOcR3lvLs46hoJn2NcSHsu_YaoQZtXj9c1ZzCRbzXNye5FA7h5YigLBJh1kAnsX3Q-op9cep24K3_ZOkXt_A62y2-LkS0H7P_NKRTbhebT47xGaEQnx5QU849wXDWOUDAQ676evHazBx41_wAQyihdL4j783Gpyhe2w0SpJ1Az3QzWSwMQpGfBR9TtRMRKi-AHDEA2gfVuvMZczW0rJYBJrX4ovHk5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pakA4wmmgmUr32IFnoekyFTjv1pNeBsqAeu18dppDr9bieczj60rcEExRhYksu3JbM19WOOQxE-TJUylqjKKQmKI283P5irkSX94UuLS4M23eLMr7gqkA6TDS2hCVrE4VmQ0sGzzQxGS8240Qu-kx2UMnKJe_zS5fkSv3JEl0WSOiE21Z723gRRIsIq8h_dcIJZCRBMB1iWv43JIvVOo0Pm12goHD7ITovwJDwAsdRjYZTEqlZNP425ZXVui7xdDcOEAAUysLCID-ef4GZfFZ-YyJcqJ-kvqb10zLmLEwld2o3YMbr-bMsO489nCUxmjXzFMmnF2jcWWqXv1d3kh3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=f2aSR5iDh0vopOIJ363XYAyZ8siv4OjXPszHo2ESC3TSdmc6WBckgx6IWn7grhnzCTEHzIwKlqpnP-EHGphKIR2T5fjwx5hD4dFnOPMjVbEZcdBCaNBtNZLVgji8JUdZjA55X6057H0JQOjAb4npYwjEkbfoz70BkMewcxg-C8URIFoqgDFiwiyVBVYoMMhA43HdLDPp6UJamcjDjeJPDI_BlKKpKoVqRg-Ag-r0mpPhUJ3caeLh_I3i3iYJDndNwtroSA04ZxsAF-AG92zT0Don-NyGhxQ0mXmhcTaygRYrT0yWnt0rD3tAvrISZ8kHichyQQwt212jqRDYxTJepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=f2aSR5iDh0vopOIJ363XYAyZ8siv4OjXPszHo2ESC3TSdmc6WBckgx6IWn7grhnzCTEHzIwKlqpnP-EHGphKIR2T5fjwx5hD4dFnOPMjVbEZcdBCaNBtNZLVgji8JUdZjA55X6057H0JQOjAb4npYwjEkbfoz70BkMewcxg-C8URIFoqgDFiwiyVBVYoMMhA43HdLDPp6UJamcjDjeJPDI_BlKKpKoVqRg-Ag-r0mpPhUJ3caeLh_I3i3iYJDndNwtroSA04ZxsAF-AG92zT0Don-NyGhxQ0mXmhcTaygRYrT0yWnt0rD3tAvrISZ8kHichyQQwt212jqRDYxTJepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=aVDDO6zZ5JdDMZ3W48FYYY6w6zw_Td62nQ0sq-AbylButy4_xCSTFhitYfvgnHOpMRxT3C0IrhpDupqDWLg1vdfnTR15JMZgep-ADfqX5-A-c23RC_htXz_9DVUo3KQUJN6Nz01y_W63EfxNjLj6Xy2025L-CbsjHYUkEPTH-DbggYkDmfvfWeVFQ3Sh3ZMU2w3SRHTlvmRhxImW60dm9IjZysulgMaZLs1cs12CwCLD0h9y9Hf2dFj6ZmJDuiQxSfs4SZtZf2JbZ-vGwK6sTW7Eqw2-mrW_BIvk9eB4IYhiRd3sRkHFlGHrYJB42ngL1LQF6FkXEqciLyeJAXtx9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=aVDDO6zZ5JdDMZ3W48FYYY6w6zw_Td62nQ0sq-AbylButy4_xCSTFhitYfvgnHOpMRxT3C0IrhpDupqDWLg1vdfnTR15JMZgep-ADfqX5-A-c23RC_htXz_9DVUo3KQUJN6Nz01y_W63EfxNjLj6Xy2025L-CbsjHYUkEPTH-DbggYkDmfvfWeVFQ3Sh3ZMU2w3SRHTlvmRhxImW60dm9IjZysulgMaZLs1cs12CwCLD0h9y9Hf2dFj6ZmJDuiQxSfs4SZtZf2JbZ-vGwK6sTW7Eqw2-mrW_BIvk9eB4IYhiRd3sRkHFlGHrYJB42ngL1LQF6FkXEqciLyeJAXtx9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=MxpwZevkeFVbZcfeAT_54jiFBP-LWxyXz5DTlkzT-QyFzTD2ykWAYJCCixDqhCodPAJXg_-aTheeHxKRZnC2yalhRJXULhb1QMn6ZhxfKu8YrzstGELeatp6dwlKTegnn-22YdZZ434SbBy9KQ_ROiEXbFV5wlJJg50KYqjfsgeR7KTjdS0hhoX2fuqllb7qqFbThBzif5Y1-p5mJLr5Uf0NzNj2lPeXA6S05WDGsVDRjTtfWpTiGVaicly9jmlgFWZpD4akpWF_C7SQKfHYCR90FlsLTtutmGSiUpXG9CLhN6wtbTTSqCeAZR8kvIv7Y6LLSK7kifCIi59AgtB_3wxb4_M7unqbyanjtC4dFB_Fx6I1g4MZB8aLXB79nXMjzYe7n4bOsIFcBRB6xgMwaDEEO3RoaTp8glokaPQ-8mCUqQQsfxH8As2dJuwCNsE4noLT0kVn8Zq84c4g6pvnLrH-iazXFRbVXSA6QtX5bbxXjJAtfthrKGI826RD8oPsSu1pDijLOyXTP9fmuRhuHAvpPdDdzlKpItZ7zOy5WtU_Ik8Zd9jiscobUjh-v2cw9IaPS4rwh_zSJtnEZgvGlE639F3k5V9tU4YiprXwujTyaR0lEXgv9-0Lbw62LmqzWHr42N4J1vdAkaLoTOP07ihetD2aiHvSke5XcK6Qy8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=MxpwZevkeFVbZcfeAT_54jiFBP-LWxyXz5DTlkzT-QyFzTD2ykWAYJCCixDqhCodPAJXg_-aTheeHxKRZnC2yalhRJXULhb1QMn6ZhxfKu8YrzstGELeatp6dwlKTegnn-22YdZZ434SbBy9KQ_ROiEXbFV5wlJJg50KYqjfsgeR7KTjdS0hhoX2fuqllb7qqFbThBzif5Y1-p5mJLr5Uf0NzNj2lPeXA6S05WDGsVDRjTtfWpTiGVaicly9jmlgFWZpD4akpWF_C7SQKfHYCR90FlsLTtutmGSiUpXG9CLhN6wtbTTSqCeAZR8kvIv7Y6LLSK7kifCIi59AgtB_3wxb4_M7unqbyanjtC4dFB_Fx6I1g4MZB8aLXB79nXMjzYe7n4bOsIFcBRB6xgMwaDEEO3RoaTp8glokaPQ-8mCUqQQsfxH8As2dJuwCNsE4noLT0kVn8Zq84c4g6pvnLrH-iazXFRbVXSA6QtX5bbxXjJAtfthrKGI826RD8oPsSu1pDijLOyXTP9fmuRhuHAvpPdDdzlKpItZ7zOy5WtU_Ik8Zd9jiscobUjh-v2cw9IaPS4rwh_zSJtnEZgvGlE639F3k5V9tU4YiprXwujTyaR0lEXgv9-0Lbw62LmqzWHr42N4J1vdAkaLoTOP07ihetD2aiHvSke5XcK6Qy8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LUtKQlkJ0S9WVE0CwLWj-0xhKo8IIADwPrZC47iaXTRN8u0CEV0-GXtaiRApRm1TMQRRHXC5pSfVOUv2QyGSmsmDVKpP7Oog30PHibsXyMIZuXe_UDzXK8uruqv4r7LfzzyV1xDa-FNwXlgbFpU0neQ_HwCcT0kKVtsjggf7y2VG_c7w3TorAveoKYltsgUbtHzXXa184qGPXcBDcudGbV9VuCcxOKm-O1X0izO5keBH0XSNEG3vId51f2AER43NtOjJDCvoGn03_w1NirFRo16UN-_F348U20ge99esvIWdi5z4FZa5_Nz82V1hk_Xwu0TtwY2vFxS42lpfnld3ZSGM8lUKlngHtKjMMU0dWP01n6RYcAYZ2KuxUGQp7HbiM8cXZzQ-JYEApxjHkFyE2Bqf-ZO4q3_E2atKAFmw1YfyrmUltziwRNd7RK5fdkF6JzuRpJA4IsnGyNA6O8dFPZ5taaAOEYE1wk5DhY2NTs6c28SY4y832qBObnksergLpCzb5Ry9hOKY2wA47aL7gvsj2M8A5rZNsg0Fp2gtXvWaYq0-WLLRACJDotxxlCivtsXEVg2RnFT_y0DQiSoU_5fJ_YQJC00WCkqaYHeJV6VNvhqDSfyHI4PGmWUuCOhZi-vijomdEoofJrb9gGgTLqJX_WVZoXniG0mu3reaXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LUtKQlkJ0S9WVE0CwLWj-0xhKo8IIADwPrZC47iaXTRN8u0CEV0-GXtaiRApRm1TMQRRHXC5pSfVOUv2QyGSmsmDVKpP7Oog30PHibsXyMIZuXe_UDzXK8uruqv4r7LfzzyV1xDa-FNwXlgbFpU0neQ_HwCcT0kKVtsjggf7y2VG_c7w3TorAveoKYltsgUbtHzXXa184qGPXcBDcudGbV9VuCcxOKm-O1X0izO5keBH0XSNEG3vId51f2AER43NtOjJDCvoGn03_w1NirFRo16UN-_F348U20ge99esvIWdi5z4FZa5_Nz82V1hk_Xwu0TtwY2vFxS42lpfnld3ZSGM8lUKlngHtKjMMU0dWP01n6RYcAYZ2KuxUGQp7HbiM8cXZzQ-JYEApxjHkFyE2Bqf-ZO4q3_E2atKAFmw1YfyrmUltziwRNd7RK5fdkF6JzuRpJA4IsnGyNA6O8dFPZ5taaAOEYE1wk5DhY2NTs6c28SY4y832qBObnksergLpCzb5Ry9hOKY2wA47aL7gvsj2M8A5rZNsg0Fp2gtXvWaYq0-WLLRACJDotxxlCivtsXEVg2RnFT_y0DQiSoU_5fJ_YQJC00WCkqaYHeJV6VNvhqDSfyHI4PGmWUuCOhZi-vijomdEoofJrb9gGgTLqJX_WVZoXniG0mu3reaXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=bRYX58Rr23guCK5RGiE3JSf8gV7CKYAWoYfstBqlE2PGR9F9IypSMhN55nuKwXZFFBLjOtL1BE-BUvkn_RBhqj8F2-snH5p-uHnzoiHwTcCyPGUk2FhDJmr1QbjUBH55D28qf1uliRcMWzVkkX5rVJVOiOp0uap6u6F_LXKRjEg6S2Tw_A0nFLXj6YV1Dc9MQ-OBzbXhO941rct5uhGiyNcc7A_kHY_nDRuuQDPmnJBBHpfWqknC7nyrOjnmeMbTMiM5yUDbzIEh1vD1Eae_fwt_DSDw3pD1tgAzSNAubN0vaISFBNUefc_Zk1JvuhhA-ZjgZiLlNsGLhPaf333qJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=bRYX58Rr23guCK5RGiE3JSf8gV7CKYAWoYfstBqlE2PGR9F9IypSMhN55nuKwXZFFBLjOtL1BE-BUvkn_RBhqj8F2-snH5p-uHnzoiHwTcCyPGUk2FhDJmr1QbjUBH55D28qf1uliRcMWzVkkX5rVJVOiOp0uap6u6F_LXKRjEg6S2Tw_A0nFLXj6YV1Dc9MQ-OBzbXhO941rct5uhGiyNcc7A_kHY_nDRuuQDPmnJBBHpfWqknC7nyrOjnmeMbTMiM5yUDbzIEh1vD1Eae_fwt_DSDw3pD1tgAzSNAubN0vaISFBNUefc_Zk1JvuhhA-ZjgZiLlNsGLhPaf333qJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUV86_Fcz9PASWMC2H5JLMA7OCf7IP6vgdZik5hXQT6X-nn-x6roVR2OeHOnwiblrYnw9nfk-Na3DlfmR5rXg8SDiTAvVEH7kQgiF202XlMkuMcyJp-pztxh-fMtIlWKyLBF6MqNQq8oCsxpTVcSJSBdTy09Afrb-FHxVj1bkxewzZcjVRuKSF0GlEOFs96yWdXvsdYxo4ytOVU2bhOzGSvkHoSjPE-fCST8XSUPcvf0St62Hv9jAmVW_x-kwh6JKnPfN3vJ4vpcHuDNCBu-oIrojb6TeRCATnnAGOK94eHxxDlOuzYcSu80MKbutaUsU11lO2YYOFo6N22xIAqPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nIHPc3xLLpEEQ-iWF_1vzbCOXLOZKnMP1hSVUs3gJF-drLpO4UX6pLnpk4GDqbWH3eavf77oML_CRPe5b0qF8inx5Jvju5QzT64lAcmL1JwjYGUZdvAq2ohCWHzJKz6v7cri1gp6Y2Nvt7t2wYeP5y7KpGZMgjAQgYM5hS-BsBVzz0dw8fVQgynK8Atc32NAfxdVuDMqE1OrcA0GV4ifnGKnne_YwvtsBvpVS-J0wSsoPHug3Q0BxiAAmIKo_GQoVl_wct6wQzbIAOry8ee4VXdlZ3ggKheNHUh9V4pADaPDnuM4z3MPtEtMXkH1KpiEcqmIGULI4ScvSqBXsQfP-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nIHPc3xLLpEEQ-iWF_1vzbCOXLOZKnMP1hSVUs3gJF-drLpO4UX6pLnpk4GDqbWH3eavf77oML_CRPe5b0qF8inx5Jvju5QzT64lAcmL1JwjYGUZdvAq2ohCWHzJKz6v7cri1gp6Y2Nvt7t2wYeP5y7KpGZMgjAQgYM5hS-BsBVzz0dw8fVQgynK8Atc32NAfxdVuDMqE1OrcA0GV4ifnGKnne_YwvtsBvpVS-J0wSsoPHug3Q0BxiAAmIKo_GQoVl_wct6wQzbIAOry8ee4VXdlZ3ggKheNHUh9V4pADaPDnuM4z3MPtEtMXkH1KpiEcqmIGULI4ScvSqBXsQfP-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=HRhQqlvkuylTfFWoxZu4DT-mCvFJkInzPw4MTFUMAoMz5Ot8NVf0IdQCwWB6U8SrWiooHwYnCZW9d_B64ef7hknZuSkFpJVN8L8Y-D2M9v6NxzlNJIkYYkdA-Pl3uVKf59bgQOCYbte3QWgs4_2drNlChzZyiAr9laqwnEw3i6wNMa9ooxzw3FvsK1Ac2oGJpGwy0-VVHwSoiIvMLHjoAwzR7hybNXGxD7nPycJLnICtufheMf4P8ILN7DlNwUL8pZQwIV7Hv_shNvlM2q38l4BSqpztmQbzB1u64P_n6k4p_Q9Mv5mvsB8F9L-fNApkA4a795WPKWOknNzBBlNfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=HRhQqlvkuylTfFWoxZu4DT-mCvFJkInzPw4MTFUMAoMz5Ot8NVf0IdQCwWB6U8SrWiooHwYnCZW9d_B64ef7hknZuSkFpJVN8L8Y-D2M9v6NxzlNJIkYYkdA-Pl3uVKf59bgQOCYbte3QWgs4_2drNlChzZyiAr9laqwnEw3i6wNMa9ooxzw3FvsK1Ac2oGJpGwy0-VVHwSoiIvMLHjoAwzR7hybNXGxD7nPycJLnICtufheMf4P8ILN7DlNwUL8pZQwIV7Hv_shNvlM2q38l4BSqpztmQbzB1u64P_n6k4p_Q9Mv5mvsB8F9L-fNApkA4a795WPKWOknNzBBlNfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvatcLL_y-G2qYlqEqm4HZ_WLinS8v5yn2AAQYApr8eHFHzRZAqvXm_6yq-MPNv9oT6KwN0wSQAzWXo1ESdEb3C_mh4t1nPcNAfMZzw-LEGsharKnXPo0OjqLXE8akDQcowEny92i268YZcp-bCXpx1s4KQvwdiZryDpOSyCL_b6V4-JIVP67UJeibMIscXTtKII0YkcUGb8B2CC5UEzFAHONRCuuk3g0ypARxkuu0xP1tXUKGngVLT4VVVjZzTFgeDGKGC2h64uznc2h3-uIaQX9nz0WS7SgZBrixKE-tucvi6z9tPAUa7h27B9Sf7T63o61bW-lUZItd_Ve4rZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH_Ld86GHqDIA5EFd12k42gKK7OP3ue2mFz3UxIZAkWyNUEgGR0rUbjNBID1PO3K9jpjMvLZ92U_mZgriOiyFmo3biKJ96NZDtby4dlqYQO-l4k6S1EK9NHMaWmDw83aH_S9hoEEKQjMKDP7Jt2wz6z2GVcUUPvAUygTWHxUl6b9FPX-x4D-PWgxFLlIvpnlVWn_s0ZawPnELIOwYXyIoZWmfrK0DuSxwg7z41j0Lerg6kylCVxTqsCsBBNhszSpJyoppNcbje1YuZzLpCtJXhEXlIuyheJH-2CDb-yMIME9Tj2zaG2b-g-Gf5O5HqC_jR2NILBOjX6jTUs4daGrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0N50jXL7c3FYJywR2Aw-rb3Y7tusFx1Ya3IRb2WgzKjgUbakHLnjLLbMZZV30bRcEbmXuOv2lP4LzjAFjh18EzkPDF5zozFrxaXyiqAK6-nqJQwf3WlxHUS2xriXTN7i38Fgg8AvUuuu9RM1CSM21L-aSYiXxqFgQFU3IS0T9Pxbua1-uoJjsHitqw3Axb14v0vConcgwV-AtAWkZKpu259xpGeSN9JJKHw5zoVvBzYNBQifDRSuDla8mAnlWTknu6Rdd1TVohAfGCaSLp-6uq9b8Ald4_vbbBbBENLYFR2D_o1q3nivKwZ9hRd5ItE-YO2ONxqP40Fn24LaFHghg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AePZgmrninWkxDYmFg0LsOOiGHCaw-OrFaD_QOC-BIWMb1lQEJWMMUW9VqQEeKVUnaqD_8gt7V46wWJI53tAS6XTDDoL4xX936ooPZRft4RLnASFM1H9i3HcrBBns_XefkM1NT8GzhwNTgMKRthixsXj25cjmwQXuCiC9iZqvH6IFLXBlRCRBelj9aO-eqNiJR2qu9HwvDa9irZYIau4LyfsvKXH7QRP5LFsq-HEIeh6Fbm8umFu5oWUh2JDRRmd5hukZzgHWplbUs2SI9xHpgOOGDZ4323EGhjISTZHmIf8s6RKznMbk3v6Rmkiapn4zD2p6AdGCRVr3aW4ga5Ocg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzGRMzski-dYP-wU91WqTyqyjvl3v7ghsSvVQRXELmcphjNGQLpeQvjuHFAFpN3i4i-LTelGKIN7YFnZtsgF-XFHKcdxOm2vIFyuD9GE2kev4YTNgR4yALc56wD6gcddFRUtZPWcgnBL-LK8a428cCjq8qpT71D6qVram4YpSwLyFmrQj7F4Xe1Jk1gzJ9jj1r1aLLrBVI5WG4sO8uo4AJw_fcb6kUG3SwtZtU-i8oPCyvhtiItA5mWrcDCGsABh3mlYsvndA5zoSOe3UIyAkpVveHyLDYV4Zi0z7B02HHGyB6FlD-E5crm4ClMlcV7fePTlJCH3vJpxQbDFRFul-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJiGM2P0vJywpkQHCoq_Xd737temamOCbSOq2-0RjmzTKPZ842hOKOt-Jf7ccHZHF7CkjaSFkzjGxLO2GoieF02W729DJMk4zMLqkhndFF5AS6BwiDga3vs8uNHTYWlWHfRbjLoVY_gBrYivZKZekDm22dIMzyID54qsEOoovrMIhUzhg_2WYoMPTgY27SBSL9r-81Dqqw0_Lr2P2zdLxmtovOjae9vQBRCSQf0Rs409rBdr6ixmsDsNRTbK6Yoaduu4R48b_O9-zJzzLSn6YjL5j8jOCa6GzrDQe1ZmN1F8zK2c5D4Nv_RA-AEJOCnKudFooXWNJtcoaEQ34wiEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W92FcCYkb8tGlXgy1vCsBZ_hMWnMiFPLR6pkgZzy5lr7A_ez858f1d-mWwAL0lVRj8PpgSK8rxnhlf9R4lB7OdBjF1Q_znqvKSTfyEqYEzGcyZF_StxaY_Ij04rosYSpJ0YciFm5SW3NICO_KkxJYgVlCEx79SUNf_KLjCTrjcyfVDwkmAOiQ1e_YZRF1nqa5ZdWbiJmJSJx-vvSAKQAemQSfVMzvkPPj9Ux6tbp9kyNgDND4DrBd7Hrx37qdNs28RBqXI8shbpps2pChcnzTgpfJJZoBnDxVcXbsT98ysCRZxwAniKKqHz63tK2OZLyn2UPWsMnZIhFg1RbIdfy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq-lgQVKxpTqXLZm693MpFtdV7yNDJgfm9hMoiBhDiaLEs7sRHWtwhcCr0cnLNR5Bc2Bs1GWIsMPdkWdAPs1cqiZuu_X28CqTTqAVkz9F-zYv8v4xe02w-HSWpH16E6LwkENFu2pQvKLEDfIvuhg8k-UH7LRnc-MVcVaUCJkueWKIrBkP0q1xnu7H0XeJW_U0aK6zml0wVjk2o6YmKrNpWOH21aPQ8cTASA-HPWO6QjAPJGXjceDnK7Zdntqch0R3zBE5PXUA4e62uExMsLONgCWVrePBpNNlaL3GXCC0i0upgxvhm7iWm4tTxu_0EgrCiBKcSQti1qpnSjN9mRFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPWxkIaIcjsooxM-aDBEPYfkabSLj_BrfGng-XBEtxh4HHX7jcRlFviZ2IJS8Ey7yXKqDe5ikdA1X2_ZygXqcAdE9nsfBN4bbFqlw8iPOrJ6vYQyk0YE0c5OCKS4m4HRK7JJmiiOYhMRzi-Hl6E-LEO_sODH1cAy4sMeok73q71OyhEZ3tvwfp2Ibrx1CpGF0bjIVmMev-h0yVEljJENPIwx0x9gIReKqFKm2gy-t-yt4FhMLeq4mDuDvcsFO-od3v4e5ooUOOWzfBCIPWvB3Ol9ySnxRM8sUCf_qtwCL_SKAYJZIfllOU47a2cv7HqwDiw5toR7aZ-nDlZ74Jz_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3bl0hHxTKEOtQZHRRz-4I0k59gpEf1--4W8g3POqi6tMuw8LKlru-obV1apdie6Xjirg2cwZeG5ZKoEObY2ObcgirQGQk4dbk6Nwt19H01eNiGp1LUYdHGRe9t0NsEYC1SzHWQb6grJkaBz9rUPUb05La0HUGWrSm8-GKAqXpoH3rsqbGgdlhHblVNaqWqgdH7-P0qF8k2Rjm9RnauVlADzioM2V6UAaa-e0rWLSZRXLQeTsNJU7IYocSAUj84jBPkifmU5kTaIy5Axg5jcHcIfGeBsDl1TdtNeFK-fRnTZ3EY4I0WrGyeJLDlSbQzvESf_1AVVs2gT_sFLSL5D0Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Hd_wJVqNOZY13tBhkRAg_lFEua5hzWu7LIDFuvlzbZLmOH2cqu3T1UQ8LA9b3TogeoNWw0FXHr9wyzaHSyIa0B6DF_Z2IOP8xZF4LYej-N2X_TdQRsR9Ofj7n-zZ0dNr2Mj6sCz4B-0l5bCwR0VTq_3a2Vx26_bhEPBclvL57VKqGd0F3wzX2r_F_gGG_ng5wZlRwWrHTySyW9JZ6ho2Q2S7n3GC3wNemDOiEOxfLChLC6_Adbt-v-Yjj7flUWD-nCuYP-uYThuT5VF3SmTXdh7_5BTUlfDqeRG_SukxudcixEZlCgsxosxruKrlYy8_BC1uA838DGIcnYebtpw9Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Hd_wJVqNOZY13tBhkRAg_lFEua5hzWu7LIDFuvlzbZLmOH2cqu3T1UQ8LA9b3TogeoNWw0FXHr9wyzaHSyIa0B6DF_Z2IOP8xZF4LYej-N2X_TdQRsR9Ofj7n-zZ0dNr2Mj6sCz4B-0l5bCwR0VTq_3a2Vx26_bhEPBclvL57VKqGd0F3wzX2r_F_gGG_ng5wZlRwWrHTySyW9JZ6ho2Q2S7n3GC3wNemDOiEOxfLChLC6_Adbt-v-Yjj7flUWD-nCuYP-uYThuT5VF3SmTXdh7_5BTUlfDqeRG_SukxudcixEZlCgsxosxruKrlYy8_BC1uA838DGIcnYebtpw9Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW80wXoZU5XBxymMej6ZFVN5w0vPibzeaA3knD9GhlZ9RjY5rGrXhweijknxsQVtMjkk4tQawql66hV2cK6ChsZ4Ho7vw_BktAViW_Cvf1O5gPuA92FCeegkDpX4yTQf9L7nU0kv4DuW0lrPH1p65TwHyp5EPlbJvv4ytAKE3UzoYB02RRMWn6vpmO6lkkjedeHsGepJyyf0lBzS3kNxC3k8-DPey9hVt6JVXo2G7cwpbKdHPwxVkE6Yvsduz1DzkanGtSZUkkTVM98RB2jJzyYDmsxQj4zLEiNP5EbDaRBWCGx3Cbz8Nydo0HDEpx_bZZvpYTrtCbeuku-p9nwy-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZITYWu1mPfBys_vxG7NMmUCxYMiR8vYGdPJTb9JBkS-eHHmflgEAxU7zWJ5UV7ZIv7nDrjU3XrriL14ZBB6Ga_UzCD9BrTxzURubaSxvBbiUZT5Gfjkv8piJzyKjOH74hCPhRdRyhneRJMA2VgVtqhjgvQm8wA4Mu0bIwr_9O5HXuhhiNcJBDwvXyi161_Twd8ZiSzyCV1v2WchZN-TiVrmhSvKu5_G-_vHe6Nti7v5RIid6jVSyRj1w7QKF6twNgdRR3bjqfh_jy_sae_kvutTxeODe4ZMswPLhIUH6CaYXU1ReLAFaDwhor6Z-f3SUBTgdST3M-f3PSbzwd0Y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=IyVYE2hXvKU3dhuLEbwifEAh3ZkqfyWvehG_PHSwb_Fw3Rytkff6zwMwfldptvHnP2vR_o7YHhm3f-dtqD1Fu_0BBDO62SNdIoFOf3wIJ3pvWXT-n6Eqsf9yOS00ugdZFUJ4oZ8Jh8hJZLGztC6G41IUS4W782aUdpAkW3HdZRZLNAWQgeN-E2PyU2yDWOrJA2uEWhuhBTCkekJqDtErsX41StV7oISMhiU_GsY-HXVV_x3u9eVN0YzAw3FAimJNc7dtePknOSbeOqLj7jCsszM0zJYfkJ9AVh4wMOgq6rkh-8sd0t_6Vjs0IPhXEqagqxxHJRylEl5QR0mcFH7ZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=IyVYE2hXvKU3dhuLEbwifEAh3ZkqfyWvehG_PHSwb_Fw3Rytkff6zwMwfldptvHnP2vR_o7YHhm3f-dtqD1Fu_0BBDO62SNdIoFOf3wIJ3pvWXT-n6Eqsf9yOS00ugdZFUJ4oZ8Jh8hJZLGztC6G41IUS4W782aUdpAkW3HdZRZLNAWQgeN-E2PyU2yDWOrJA2uEWhuhBTCkekJqDtErsX41StV7oISMhiU_GsY-HXVV_x3u9eVN0YzAw3FAimJNc7dtePknOSbeOqLj7jCsszM0zJYfkJ9AVh4wMOgq6rkh-8sd0t_6Vjs0IPhXEqagqxxHJRylEl5QR0mcFH7ZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ZmfFDg0rWHVNhuAfwfj66nrBTiOYaEyQN-DAyapr0KAv4BCzfFAF-lEmxY_6hKr_ZNRRexW2ov4AvCJqohWKLAW2nhvWy9mkphE2lWtz4XthRqvpGRIKzw34fa-JB21fVjFTmgKJDXlY7Kf33kO-VIJBNSpuMEPxIarp_92LnRV5cyKT779DUtMfCZEENx0GjJvxTjKrAzbGheGjNll2YXjlVR6TPmuR5ZD3G3AZ1W1FndR2E4i-E_9ub5Vt9ZuMQ_j-ZefKmJmgLGBbAX3KPAbb-FU16iSMgii35Vb_eLjnhD6Ia-ylXWcdpTyRMlMEuYQkk1DYUPrKeFPbwOkRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ZmfFDg0rWHVNhuAfwfj66nrBTiOYaEyQN-DAyapr0KAv4BCzfFAF-lEmxY_6hKr_ZNRRexW2ov4AvCJqohWKLAW2nhvWy9mkphE2lWtz4XthRqvpGRIKzw34fa-JB21fVjFTmgKJDXlY7Kf33kO-VIJBNSpuMEPxIarp_92LnRV5cyKT779DUtMfCZEENx0GjJvxTjKrAzbGheGjNll2YXjlVR6TPmuR5ZD3G3AZ1W1FndR2E4i-E_9ub5Vt9ZuMQ_j-ZefKmJmgLGBbAX3KPAbb-FU16iSMgii35Vb_eLjnhD6Ia-ylXWcdpTyRMlMEuYQkk1DYUPrKeFPbwOkRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyYv6E8SzbJUoe2CLso-qW9A_XhlAXwZ8WFvVu4w49Z4do--Q3Td8fRqzhVboN30MNWv3NyU2LmdyqV7aNswrf2CIZot6htvQn1NwodOFVXU0QcSmqTvlJ6oNgY10o35yo790R7e2oSAFBYicaE2HFGyLnO_Jhdl9xOe4HyqIFtuBfGmxu0xdCWh3vy_j5qFATXmvCwGBkziVjc8yKqvtauBZzcx5JBcxjmv-3MQG3AW_9H-dpAM3l0KA_XXNU1-DDqz0oE9u9UMwcekjDgp2rfSbOvuFQwUX-kGdL8e3_Mejq2M5e2fqtkfvktXSxdwgFHPyQAEpk4sJtDX0fGH3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFx6N0s13POoshrebu6TdcN2TMpSr7AvMcMuP2rFudEdDvofmzd80AxuAdxupqbpRHrlw6N6VB1HiXU4C__5N9KpJiwBAMc42mVFvqOts8ZOgro_mZLIyohEOsdERxGc19g3ISRP2-vv9NGUJ0eAejiV9eSYvvPjwTt-N2B6J5bJIPOMZr4EUg_0eLcl0lslKzYrecx1QqiSyCYbCN_MbQOfGHzfUEIvwCMbrIG46MDETVIVNfm0UDA7TupPrC6Ze-3e1o7JjNlnWOlWR5XjoQtFnhwzxZDphqZusXXEVaEem53WdUdtFO--yX2UBtokZNjOuHT5XVvuo_CRpK-O4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFGYwZ_ne6mu2a5sxmyriTuRftQ0kS1T6PCSrdHQp7oc1J86GjIVKaBX4Xeq2aMDsyE14QO3mtvFPP7ugOuiIxMPxkLLz9y4xKUifUa8BlyUtQSzEti8IXZ4WcOSyyBaOaKRemWSVHBUz5AIAJcXo1qISP_9Q-R7HSnxBfsj3m4R8KoHIern5IIhfCaXIA7La_u3wc1I-XdNma4NV07oS974K0-2esu6NvFQl1xiBjy4Ss79LypHLpyitOShbqSalpYa5gPy6f3XwEiZ4ybvXuF8JpRmFCg0JmSzZ1ZmRa0R5bcQzQueyatc8Dluh8Ay1kZ13oMj-LAJLmKqgNchkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm7Kl4fKuMEzEWoHLeGhLNHqfVjWG4zeH6om6AOQwBFvt_Y7k28NB7P5Ev9BhtQdiEdqXzuBymdZUDzk4324peA-de4cpQCZ83TOzZf_DyoOXsCHWtS_VuUBXxaeRF5wqz7UdPRPK8Ru3pnmOHFmJnpfoxfHeQr2W4QRs3CqWExEKPzDntMY6R48oBfwP01BWidkdKDhz3xroSmpJP3u2gHsGFzd_vhizyK7G1zT4FPC1W_U9SO1AzHktlLs1MK6jOtDswJpfhSdZeHdVa___fbL16lCoeqhnQOiGfpX9M8fAHVFMsPQSQsvmR3uNycA0m9trt0AkmEV2RfdcyZHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juqhnqCrAgAbrdM41SX6XXtRjQC6HlkaZI18HzDj_16Nicv33hmYx7QbLxhpWEYqg50AKG_e0wg8ZQiqfXQRPpmWSz4GR9a1oUVlljAahMlnK_hsGE9oZ-hjh6UROTNis3QJNLw-jJNkMRKH0ax94dVCJ5zgzd_phJ35r2bmoTxs47ccFEexxzcFlNnGsZlFn05ppTvPCBYKxHhxk2eYlfIxmJwwnYbphFbxzP9ZrlaQ9cQ542a80qhkDr--TlxPSLt4-Oa3VaSYF5EjspU4CaBo_dsu4uRonHvQt97RJcLiPXFtfZkbz4m9iLKWcja87oQRirrYJBJVCSKyYgPHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcBPzz20AEDHLhKh5Hau7QF31G85g8dYtEXy3K7Jwy2h6BjwQDPiNPZLLCKOt7h_cTUsmKuNmyM63c_ce6T9XJ-xW-AByOP7WpvyRObuLCEd3-I-Cv8sRYVpjI-SVrKoDiBu3W5N5O70_Ltl0rDVcaRs28Nk_t2uhfuUNNI-wJoK-L-O1E6MWHxQfdXfFuW9oq9ygSKEJfm-JjFHHTE9PGHb8GJlDT2dr9x_Q1QHPgmtyAwTc_YvASFevEuUhluGO0Y5BBrJkgvFTJ6LhmdcrQZWpdhXAJNaqLi4GKye4DZVNghLFcOflBWtqH2ajKX0UGR1TrbxFL7gPJCKcXmdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R28tQPCsYe2Z9IvJjw5BT_V-iVTHeVWJoGGSmwVbMqtc1eHCCQz8Pf74FJPe_KOm-DCTj-7IeU9ih-qS2keVZHWCTwoH2hIF4ztwaDU7Fch-Ixp9PS2aQTY9CIeIkuspvobJRIQv8h-7HdEg9HQYv9DAwd-QngmmgZZBySquIn--XURRJnq-W3xPdW2iGOp0i2Afn590cZ7_u-6-RmVcFuVJhYaskE8Fgvr18EdDo6PVdNlUMg9P6SJqm0TqXupkZFMGmvq7svyT1V_bInAGF0dmmmc-UT3nJV5_WhXAAK_7-pLPXK-8PAigGzzY-07ymL6UmJNUhmqXiRc-T1U7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNDhT7jfQQh1Mq2GoJx-XgBmc-PfuENLvTMxU5kQ_XZ23mt4JzUP63i39FjyeDM1whV7Iq63ijEr6Fd3Axr81XVDjOvZNQOcBozhcHuTmiUZZyKGQ-eWVNnpXCKbvJKfWA8NltNVaFwD6tWznJE15QH3YQDg0axAdhxCFBzZeUDGcAc0zwivfyotNGidrrf7xQUgeY4lLCqEadKfHUAwRkrznPAUWQ7zqJUgp2Or9cuMq7QQVKykHDQrMXB_dJBJxMcAUFqxLzzFCZob969yJJPCs1HHroAaLVk9YQ587brdx8L23tTvXHqWGqgsZg59wC9SAznV_ataQy0QllyCKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=QQxS4sKcK1G5NJ-9Ool858K2juJw-U-FGCwWWY2H9E5qcfCNaLId7OqlPqRURpm62D-l0lcGQmABgZIgvcMquheNhL3rXSWq2wcVtTgCBBFeKwWTi69y_lPgNfuHqc097UeIux8pQwt5xN6tepcROH88oFoLtP_RZDsBMGrdYkESSvuaWIhdaaO52gIXNGfrSyEXP4KozDKOhPmlScTt2dUjSgUcLfEF2WIsJRXaZGdU7qiDNIxDHE2kABKH7GOzlpWRUzzS_dznBznulQxAoTXQXpkY8WSZB1G7jTeTf-btf7RQM-bO1DdcvukXaClaxivQuRJv5682Mu2ieIQ_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=QQxS4sKcK1G5NJ-9Ool858K2juJw-U-FGCwWWY2H9E5qcfCNaLId7OqlPqRURpm62D-l0lcGQmABgZIgvcMquheNhL3rXSWq2wcVtTgCBBFeKwWTi69y_lPgNfuHqc097UeIux8pQwt5xN6tepcROH88oFoLtP_RZDsBMGrdYkESSvuaWIhdaaO52gIXNGfrSyEXP4KozDKOhPmlScTt2dUjSgUcLfEF2WIsJRXaZGdU7qiDNIxDHE2kABKH7GOzlpWRUzzS_dznBznulQxAoTXQXpkY8WSZB1G7jTeTf-btf7RQM-bO1DdcvukXaClaxivQuRJv5682Mu2ieIQ_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow0dZ0cyZBn3i1HTj5RZ9y1atBgzc1e0lC7FmSO8HIgQE-NJJK7QIc9JpiCKjdwn-B9Xnb_Gl1yaB648wkJqzyUCw-9Sp2B9-IzuA3J4R56_pS-8QgYJyl8IaP2PWyDVy_awriloKXImKjHoUcEiYChJZ32ChtkAbFfvc2WFuU6qsPcfKKxekW-2l6OtbMtLfq8n6CiHWRTtRZ5J_0LGM9oIv_e4N3HMlgAHl1UlHwevABRtZSApb_WKFRCyRKqBi9f9u9iDTs42yJji16fD_w1B9WthiRB7rMafkL3G2DQMDCIAmM36fzJDB78XT6nVnucTqrJizgjZ5ODB2d8B_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=M6t4KOvi_1N37t6l8UT2MF7T8-jljWNXy7SAxYc1VqmIrDeTFStmQ78Knj7Soo3pi1xuCCFKEogKCR1BewcrJxCHK14Vv8doYysv-lGIm8rUDETtR53jRKfBTq8DQ-8CzcupVPyCtL_FTXDjlW8ZtfDnpqdErbTs3dzeC15G1Dl8jnBgiC6VqJaiXArW1AFHHJPlYaUdFzROfapQxCDqrKEb2SP7FfmxjDjQ62df6wwnlxgTfPBDXlmXhOf2K7Tb6maHDJxLeIeavIz1EtjlgW9YNXYrLIN55Dm72zrS0lQdcjVOD5dMM57AUQayKSebxy3NntT16N5e5Jn7dMiFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=M6t4KOvi_1N37t6l8UT2MF7T8-jljWNXy7SAxYc1VqmIrDeTFStmQ78Knj7Soo3pi1xuCCFKEogKCR1BewcrJxCHK14Vv8doYysv-lGIm8rUDETtR53jRKfBTq8DQ-8CzcupVPyCtL_FTXDjlW8ZtfDnpqdErbTs3dzeC15G1Dl8jnBgiC6VqJaiXArW1AFHHJPlYaUdFzROfapQxCDqrKEb2SP7FfmxjDjQ62df6wwnlxgTfPBDXlmXhOf2K7Tb6maHDJxLeIeavIz1EtjlgW9YNXYrLIN55Dm72zrS0lQdcjVOD5dMM57AUQayKSebxy3NntT16N5e5Jn7dMiFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=bFcJrx5ZLQ98zsInS0KF4iPJ7Z4_eK6ndg1BFKUNJ2824wEs8gT4pg7khGay-pX2-mGjkYAr6A--KXBnxhBdoAa2enSRe0P-uAfCjCoCmnUyDBDc0t7gtow829vUzFjfJ8Zg770YqlV2EgmN_5zyds0bqaecZgl7o-vOvdO1OjKta6ugZAE6VUu9O4GwEpR_hSvdJ0Or8VOd_SQjrnnv00sdG465ehTaaV-SuDP_GvWpJcluowoACAoTJ-zPP0_nFlzw4uPD6kjHiooZI3Qi9uRluKrX2l56-beeULfnDjT2w_WjFRl4ekUmlSdtcX0uQ_7khkX5PcScCXgsju-9ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=bFcJrx5ZLQ98zsInS0KF4iPJ7Z4_eK6ndg1BFKUNJ2824wEs8gT4pg7khGay-pX2-mGjkYAr6A--KXBnxhBdoAa2enSRe0P-uAfCjCoCmnUyDBDc0t7gtow829vUzFjfJ8Zg770YqlV2EgmN_5zyds0bqaecZgl7o-vOvdO1OjKta6ugZAE6VUu9O4GwEpR_hSvdJ0Or8VOd_SQjrnnv00sdG465ehTaaV-SuDP_GvWpJcluowoACAoTJ-zPP0_nFlzw4uPD6kjHiooZI3Qi9uRluKrX2l56-beeULfnDjT2w_WjFRl4ekUmlSdtcX0uQ_7khkX5PcScCXgsju-9ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnLz5a3Xse6em4XNWU-NjStICrRBOKl_QM-GjuDL6eVpdi5GIz98QPYzNJWKs25TfSynsiSyWSojNssL5MtGnknw-uJL5KRjDAMYIkwqZrzUwpwcDyLkJHHYIBMKrWL6lGOKREWsj0fuX0LvL35r5zegX93FOiSOf7iK3dDLYsOFzYs2FIsJbHgkbGEs7M3JlOpRuBonSQhiLD9kjkCHoxziRh1xUGlEYhr3t7BdSetTQroJowLWX4x1zDqDIG-TEiGQLp_H1zAppIOYk6FhZQ_Jx6oEgKokBEZoPoXhPe-_PIUOW9-h1-XfrQOo18064_ZHuuERSHaHmS4MnmBCIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egoHo-nX1TCCtbyrBxNDP-GSo8gthCJeih2vI8XgDTIwv0v6QQdaQ9PKtn-HtQB37DhbrFENvPVWH9edxeHK3K3P-c6Os73NT90wljJeYv0UXCe4POlRe89U-SqlS1zv9ot2JQglr7NL-hJyPZDH6WBs6tZpu0t1e44iP_MBEstLoWAq9FZr_Q0qPxMUKwj4ub7D-kgsomw9NGzcG484DsVpIDU2FlH3YEaFlB8osJQ8G93xV-qw3lQNeLX3oRpr2U0tSUTONg4mXjSPX8bO58NjpPUXqtnqZCN-_ceub6wsz8OjdM3hytXqVZH4NHKEGqD9cOYyMwayC99FqFCKsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EvOo5IarTZmxppy7q9cSUfzhnIWf9WLkck-FdCiYpSWFAuSUdo5berMqyRoUv8xbl_ZhQDZFdu0QFegmXTgPLwt6wCgubW7hMol7_7fBzlOpGE4m6KBvT5Tn9k8RVVuacVvQCctjkbPVIBqISTc0dQzmrjm9DQnuTMoI6zNpmAJTMDu8HJFSoqchfdzszb8fzVP9iCiHDm_LYAK-u0pUdLuMMhaqdyQqSCItMM7l4jsmPyJMll5x3i3qxE9CLgBR7i84BCyg5NdJkrYtDLQ4kt-HRebIOS42xTNOGIDI1Pn8dXkzJbAu0o_lnlz6HHTwzmk0wuRzSqIdEhEH9Hb_sl2VdSCaMCdOQWYtvsOWN2rvDZFYxbt3NjqeERyaBwPtK4y8V3qfM4FCVkmikVcLhRd2UA8SFzTxkK4aRBVbVkkjExENtnEDDgKbbaL8ik7opMxtH7MutfgBNnBj2ROBwxqsRhcfGcaEiWDXJprvPVOnqeitEiTrlXWwsT2meiowQfZlJbUercpo9dE3lyvs-4bRy5NlKTd5iC6BAmtENa0crK2Z1FuTuGi_wiP3dHsqCYX7lwn0BpnEUQ0DItkLmvMI1-hu1213SwWkw3REp0Xb-HUOgPfE4IVcCi0ffdBOre8ReOSlACBOPJ_mBITLbQk7wh3VIR7l6-HHHbM5VU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EvOo5IarTZmxppy7q9cSUfzhnIWf9WLkck-FdCiYpSWFAuSUdo5berMqyRoUv8xbl_ZhQDZFdu0QFegmXTgPLwt6wCgubW7hMol7_7fBzlOpGE4m6KBvT5Tn9k8RVVuacVvQCctjkbPVIBqISTc0dQzmrjm9DQnuTMoI6zNpmAJTMDu8HJFSoqchfdzszb8fzVP9iCiHDm_LYAK-u0pUdLuMMhaqdyQqSCItMM7l4jsmPyJMll5x3i3qxE9CLgBR7i84BCyg5NdJkrYtDLQ4kt-HRebIOS42xTNOGIDI1Pn8dXkzJbAu0o_lnlz6HHTwzmk0wuRzSqIdEhEH9Hb_sl2VdSCaMCdOQWYtvsOWN2rvDZFYxbt3NjqeERyaBwPtK4y8V3qfM4FCVkmikVcLhRd2UA8SFzTxkK4aRBVbVkkjExENtnEDDgKbbaL8ik7opMxtH7MutfgBNnBj2ROBwxqsRhcfGcaEiWDXJprvPVOnqeitEiTrlXWwsT2meiowQfZlJbUercpo9dE3lyvs-4bRy5NlKTd5iC6BAmtENa0crK2Z1FuTuGi_wiP3dHsqCYX7lwn0BpnEUQ0DItkLmvMI1-hu1213SwWkw3REp0Xb-HUOgPfE4IVcCi0ffdBOre8ReOSlACBOPJ_mBITLbQk7wh3VIR7l6-HHHbM5VU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyjR6AekqJdmYe6uo8O5A5bPqp67A8MxiUi1uYHrDBrQWPMgodHYh95UukE6pXipU8vdrZLuql-paR3nm7wlZsfJ6RCg85xFsDVNsns4X2izllnqocWC10x1iF3X1QS7U5QFhQF7bU59Bm9l1b1-Si4sd-9c42MXMyTZc9siDd2i1SfMvEnTezlF78Q62XP6nJ3adfNnAdpq-B1lFhfcV64K4ttg2dGWhUXJUdfpNjVXWa7pZrWkn9sTefHhPJYjDMRiovQCisiBiQ1w4O0IjVE_m4l6Ri-DNnKJh11kx6iyJsMi3BBv1RnAphL23c-bACWk-zqAcaNw8dBs4HgwLQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M4xfSy_WuGlC2WEqkYGsseNyODAGX5NNMtbeDPIrq7BMaLi1dhuoLfuLfoHS35mkH2xBQ9FL5PzkcBPItZ4ARTHJDM-mrHVGz29vlxEZ_dei16uV7Q54LZgGrK0JLXV9BxjCcuFiU3P_SdMLAiy-koV4J3DKOtJliKAsfIryIJbVhFuOgYkX7B7BNBWHvS8EdN4sDO4dTf8bd4qamrC51sqdXHLKRVcc1NcOzhd49zDjypG9Ci7pVl7mludtBXYMwBhuuwv15uQfArxMRga5o9nqc8dg0jzO-XCxDYcsrSKTB8Ad3sxsb1ojn9VB5I3bzVPSGRAuLMCynaSU9qlD-KqXZI4iXRP7DBj1Irau7_RypRXknMfj6Siyx8HTo2j6A_zYPil-xiEED8U3JQMBZwiUTU0SPrvTaRZDHjyZFWUGFk_xLb-dVqOGELmQDKwaGrRQ1IUpwfTHPzqmMSzduVpGbOWWQ78PHrxLJFkN2y66yH5kAs2GYpYpH8Pm3bH5eKHqjo5eKxZVo5k1O7Cd5oY7oSsh42lfTRQsBf-82aelHtFdgGpNKw0IpJIwe-gS4yi8eBNMhyzHa6jP_RHzhxhh9EnmIhxLVyDDIL6aheVyHDTVpJiD6VfwU4PPp38tnelTR5cMCorQ3wvxIZU7pkbvjF1Osx4ESa_c_dyXxb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M4xfSy_WuGlC2WEqkYGsseNyODAGX5NNMtbeDPIrq7BMaLi1dhuoLfuLfoHS35mkH2xBQ9FL5PzkcBPItZ4ARTHJDM-mrHVGz29vlxEZ_dei16uV7Q54LZgGrK0JLXV9BxjCcuFiU3P_SdMLAiy-koV4J3DKOtJliKAsfIryIJbVhFuOgYkX7B7BNBWHvS8EdN4sDO4dTf8bd4qamrC51sqdXHLKRVcc1NcOzhd49zDjypG9Ci7pVl7mludtBXYMwBhuuwv15uQfArxMRga5o9nqc8dg0jzO-XCxDYcsrSKTB8Ad3sxsb1ojn9VB5I3bzVPSGRAuLMCynaSU9qlD-KqXZI4iXRP7DBj1Irau7_RypRXknMfj6Siyx8HTo2j6A_zYPil-xiEED8U3JQMBZwiUTU0SPrvTaRZDHjyZFWUGFk_xLb-dVqOGELmQDKwaGrRQ1IUpwfTHPzqmMSzduVpGbOWWQ78PHrxLJFkN2y66yH5kAs2GYpYpH8Pm3bH5eKHqjo5eKxZVo5k1O7Cd5oY7oSsh42lfTRQsBf-82aelHtFdgGpNKw0IpJIwe-gS4yi8eBNMhyzHa6jP_RHzhxhh9EnmIhxLVyDDIL6aheVyHDTVpJiD6VfwU4PPp38tnelTR5cMCorQ3wvxIZU7pkbvjF1Osx4ESa_c_dyXxb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaLFvtKrzhIC0giupfhWR6X6jWxr1RW3nLGA_qZFrgj5MYmwAvpQWU8JhDzlBIqHajsTmcLwoLnrK4UpHzq4N5hznJxdq9DFVIwx4eE9ErN80-VP088N3xsiZzEr32Gv0fcet2WP0fq0nTWLrkZsD5HmDeotTaJGEb_-NyUhGPhMMEOwwegbfGpj2-4Xee8SDJkryurXugWs3QT1XzDlx0_Xm5CkzA1QNisZr2K6A_9IWy3DybBaNU8_mE1o_2HnGZDoC2UOwoNET72-VZaQIv37PmnVjGXpDri8ZqbrBaTgrH8cRvtnqaqwbJNBhneQwHeU5v0zw3SdqA4yp3Owrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
