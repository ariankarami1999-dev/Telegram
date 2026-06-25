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
<img src="https://cdn5.telesco.pe/file/cv7jVK8Vl6vgifbZX9sOzIMHsn3Vr7zsBF3F20X6V7-0eXZ6wJSrZ_f68NCWpXY5SIRg45Er9-IDf04K7DMBUrYf1e4YCEo24aiU6t4kPcFKZ4xR772S-Sh8AMaPvyX8Tq1-DxwUhDTI-yizf2JtIk4eX2BD7ZaCG3R7BXzZjL7aI2ZiSA-M7UIsQsKdkb5A6grdABeHERZiwA2INKYW60qRPShAiaulEMKfb4ms8DiTs9ZC-0oICj1e9rVc6UPUUs6NKy_ZsvInR2Yk5OrQTu7jWbdFl8MnWQMEU0QeFsycjtiOAlDdXfzljTgFNaaVsjOLmlWJk1mKlG1STYgXQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 705K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-95810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پایان نیمه اول بازیای جام‌جهانی</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/95810" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkMR5g1VExs1Wt99Yrf491dCqpJxBCrPssYX0Pvt5fZK5UZGEJLy_Lznp_kOoU0q7Z9xW9ndVs_rExbY2OaG5HJbrIjZimRm2RkHeby6f8Nm6XTAiIGhAkvxmyUli4jA1va-7uPMtDSHKjH9-Okbyj6fvDEIkT-_ok9LQ5kUk-eLY5ERCjCU9UnHZCHXHPPwQ_npgVLiWQQYq86V7ihlnugmsrvdvlX488lxYt3VK4TleWx-OqBuossR40qCuRFPt1KHwHdaLdYrfryhKzShK2l5hf2gray-RB2VjdKzleimjcUF_-YyXIBrEQK_EbTz3ZqkS0jfj4_wp9LRCWLgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTyYAVBP9twgI8uylpB7wQduEb567xqtCMyd7g-CDUl7bpVLzgdGcXC1Yn5Old8lF9Z5ln5w8leff2I89q0535y5awAyRTWxRHrYzycc-vYJ0YHN0MbRIfcRpBmIc8HPMqlYpcX61WSPIY-VZlzelF7YqkfHs1v-EYezKrQo5hDuaY6N2D9TXmmWNf4gWGFzUDXBQ3eGUDmPDn-x30nfRBHBz9WmwnDdV5z6gKrNshwcspdy3VeGORqKXex9LZOvFISXD58KGAf71WX1J-cJL6mfWvRFohcwyFc5ITBtBuetCvnzFFAEAMkhqmoKypZVvTI5wW4EmeUsCOueuhNUzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
👀
تعداد گل‌ها و پاس‌گل ها در جام جهانی:
🔹
وینیسیوس : 5 گل و 3 پاس گل
🔺
رافینیا : 0 تاثیر گذاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/95808" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMPahC_aBkBBinnJ3pQamblVVQmkVeiPolZwxyvGblVCX3qN-8ROz3DpOaBScLYIm6lCBSbe_yQb6A2ki2MZx0tc6HUp3cTMTm7RzNU_xbVmqRxSLcq3woy7dAkGomTb-CglbJpnUiI6365unqg0989f3TdjfD_tbrTHGyrFDj-JWGm6TA831HezLn-u7aW-SU0bClLN7XGg3s2PmiuT3g3VGitSm8hLHgrxRBCQc7DoK_P-qKcM80LgpO0CLQeT8Esn92uandfPH2SSYeElllnOL0ihbfMyxJMWLD29-if70J7vCF7OyHSl_njXYkKieNJzBlQNJsEM7xjCk4kLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای بوسنی راضی از برد؛ ما هم قطعا از برد بوسنی راضی هستیم
🇧🇦
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/95807" target="_blank">📅 04:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5mZReOFLsF-SDmnkr8MBNff86XGezcqnGVi5o7mHcVyBIOGmEk67kLRdUSv3PmrlLzIobMHmcUp8Hk7d-T_kz6OqQ5qM1XpUCr_gG6t7vVVu35cEvpc8OyPWyAe4kxwAjMVNrFTVOKwxzISfS9-VtnM0udAwa_gLgh4N1FDaYkBaZ6TFphlc2xqObnDmddnbfjWk79uMDXWlvd4IJ5B3_Zn5SXeaTX-gE8dvGXp6anrHRjSuVg045hX0z13qXV-Qot6K9a_PnYX8pcZ2rzJ0a1Dm1VBDD0-poYuaVPELKD7DBKA8OXBEWPUUi0Pdg1WgBcjNme_2DkRM3BqFbOvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBpJIfhDsUPUnoGqbzg5P2B3gtC99XIxnOKRpser8zbP45djWgPzkS5ACnbka5opvczzIhEKcNZfUWXL9O5xmEwm0KuRdr5LsEXay7fJ_I7PoH9z26FvhpJuW4V_hSPC39d6onxjzzz1ORGoOvx5Nn2KqVahmapYRp9bUUg1YHMRtFmaOhb_Vw4I-9ord2cR6E5YST9hOi_21yp5e6oaEMkKEoy-xLa9VCGssoDIufTpH6OgqtUaAFc_9d6mZ8bXeB8VtL3-Ft1d6VGZQLbQGAVdbevgnLYIQY4KIi8ol1LuINcX7PCNqsi15L2U6WJSLhCFHTMzE-z8nQw4nySu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooI9qavyNMa4UoJlGNbqXVXyOzNLbQFFtocwgFh6r8ecBZN_UrM3svUwShgeJRDu5deC84PvMMHCYpqQVR-sF3WQP0qSgj1yfmWBaviCfI2BSu787w6wBafXxBJIFz5KkLeMsOZAP2rmKv3haS8sxgLoWatXIhrd3FTnBhmHJVvTVwhzqLjI2s_8HDHE59R3k9jCj_Cy_l43aWZoRDz5EWbmw7CRzKSySx6u5nifLZYVOVgb9sVtVAmgraKP3hsyXdI5kCH1W5Ryt9ssnHevyecIDcBmUPEiUgNWAhJ8zO7LlkADfx6H5-t-k3TpLBXnYBlbucobmGIPRIsQsrQ3lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشک‌های نیمار بعد از پایان بازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/95804" target="_blank">📅 04:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شروع بازی های آفریقای جنوبی - کره جنوبی و جمهوری چک - مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/95803" target="_blank">📅 04:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugS_G4XpGiX_JYXpa0HIItBNu5KmDbPhBNSmx34ayWPe_Fw5G7hS6p5OCbh5MYSwf5YwpeAoD8ekiU_6PecTqY1S6z_D8YJbApjDCcvljEiaU2UXBbj08xe6DiGc11XAxvLKJUnsHF0lDkIZXTucDUOCR9PZfrzfLZnRKR6s4NR7wCN8tM5ME_m1PA-s35mQ4vuX6K3E_I6c4YF2tD3azMJ_EoPqs9agCqZlVIvaNJFOKvY6TPjhICZ1tDmIWY2IzkHd9cxTkIqzbHZB6gShYmawpj37HW8jpNmhIaoX384CYYPxoOdgABCTXhA3anMTZIljOpPvGtnFFktQsSD7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس:
من به آنچلوتی قول دادم که یک ضربه سر بزنم و او به من گفت این غیرممکن است و اگر این کار را انجام دهم به من هدیه خواهد داد و الان منتظر هدیه هستم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/95802" target="_blank">📅 04:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlSRH_HhjL6gr16LRJeg4JPtWuZYmaTVS7HaCa55ktdnzw1mz42sfMQxZnK78GQk-kcjGuBUKl0_A7hAxcabUS9vSXx7jgQ45wtkW_DljDXlz8CdsCDBLbdm6lcheojzdqBln_qAfmb-2lMcKmbTwn0dxGKX_a6lRTC2fwGaHPkJzby89JQEH1fr0oubsGD-xB0iZGMXSqDU9iZViowVVNnBXiiwGYZap20Ho9Q-MLlTLDq7wSLHziApBS1UatImZhdD58AMW14CGHGqUVPFOGAK7dIMuLGPx7Y4Tz1bRcwF1bnu7rVe6Z-tpv02687CzBZP3H1RimzOipUIZSp56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشنگترین عکسی که امروز میتونید ببینید، نیمار و دختر گوگولیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/95801" target="_blank">📅 03:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8jumoAdKryGQRIciE61OcHhpypNbCnCL4cNrnqjSYBp9J_OWz1-qf9nl-gdyhYdIH4ROWt5C9byjJgxFmQmML_ycWWvOWbNXhgl5ZlnWXlnMAzW6AmZy1AvlEsp0mzaTty5TPQJLUiQQLKWNlBuqdKa2nGFJSdcA0rF6AcVixYQo_rh7TWe3y9oWrpO6OmpmD1ZEdrP869rSZdxz-tXTCaJ92vaiacmijGtuem_BGorXKsE-twolyrTEA8SJBX7RBcjq1xuPX9SY7nwu8mvlwkpfTDbwfYo7cX4uppJ8_KiY3vzDogtZXTIf-qkiWwVRrrhd0OEU83DmwndsYFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بوسنی رسما به عنوان بهترین تیم سوم به مرحله یک شانزدهم نهایی جام جهانی راه یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/95800" target="_blank">📅 03:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbBn5QV8jDFORah5gnewgy8TUUNZg8PNVI1WtpZq3m9yIkgUoPVroGbm3lKB7buVCJjVbNsOPH_P9crNvu4BCIRQtimSaU2Q5yG6vLcNeW_ZiZmhbzpxX7ASqI7z-VdhPdIacXv7bCow56mlOyUN3pnfKpypF3a4qH4aA8fPncPGiaWBa5m7X_WPW9ooMoyWjFQllVWpoG9fpdnIrT0shRhO-17aY-fJyGhNSDuv84K9IZPcNTXOhi6f7xCFL9CJ7Erlw9RguffdHbIjeXZZs089MaBBymyVyVG5mO5MPg_L8HcZuhQUm7yANZ1CJ2c1W2cbsE5zzxqcKfojmRMxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوست عزیزی که روی نبردن مراکش با 2 گل یا بیشتر بت زده بود 3.6 میلیون یارو بگا داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/95799" target="_blank">📅 03:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZL6fKiAeJsJy8xZV0ujHSU83EB59KgAoMp_uabPZ-iwgTiZrd3gkemQJZYz3uVWNPIrN8o6TPgMsqtEm4ib-3PUCYWZS0rf9ly9fB00-9gEvbZgSs0BJ5GzLjM2zrYGUfNe8G9mbF4wcTelFLcHD-b3l72fLmtiSYlzkzHuFTFNcf3BUagPikCxL8P044RkIL0if6jM1UrlzNW3hValI1hWM3Ru4paKqxQZd55SxnkWrMSeYpzthCTEp66IrnwXdwjIWLUUVCoxlVXFmzBGzmqdRz1ELTcMMw36f0zrJomuHG4XbgORR1MEjPx0NzLPedpbp2glRqOpIRUn3rQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
نیمار مقابل اسکاتلند تو 15 دقیقه 9 بار توپ لو داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/95798" target="_blank">📅 03:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKM1aq2Pndc5N49igUujpjw4EimVFwKltXrB_hd9_ahSKzRVbl0uNE7aIYY5G3vNhW-mfzGSArx-Ao7e5S_uOqB2WKD1bsHrkkYYojc5h14uZJzmWfS6HiSLJRxfkc5k8gqqo45dQHacGEpmFAr9k1B2Tmfk-UY9nqhuPekP0uiZw4P51rvvgw7E0RIc1vvcDGbFVE6j_v-C6ALvxiODGCW93Ht5eDrFCO9vxKJowN-_kB71al0Kur975uld_vJNTaLXsBfbjhsBCJXpjEn87BEmYkqg8GcwJ9DU_aJZLtSLORx31pZ5bPMBVo_3zGy6ZrIW-SOm7APCL-KbBwsPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم ملی مراکش اولین تیم عربی است که دو بار متوالی به دور دوم جام جهانی راه یافته است.
- جام جهانی 2022
- جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/95797" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuxERI24h_UwEukaqrzITTkjBkWnm3IpKnIzEipECNJ5ZTe1ORpAnnvPV4PAkysNwGqYeutMXfJaFqfXctwCL8Xu-Vbj8cC-0HjllbjkVmceOjC8McbvkcGZwnwagcYRCDFgCnuGB4C4LJxvWIe-qhzIfdYcLMII23wstx6zMdCxAiW2TEzbfc7ARYESmMZBH9rcX11q0hxPpivPt1H7dPkkX4dmW2r5BH5c0McXrPt_KeewLwNryWeRW0PWnckm6YZRlsZNE-3WsN2Ur4o3q-o2_M2mWWMaEkuhc54_c2wp0LeFFg55_yE20NGdGbwSxYmdBj4OhJyc5XINl11W_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس برای سومین بازی متوالی بهترین بازیکن بازی شد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/95796" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLPoHxZBf6Nj34Ku7gLECMwukinAO-SX6BJDIz851mH9ybR9iHEn6LxOalV2fB6DaO5LFDqwqr-ZzAMZtqsxWlBtqjegDZT61VSCux-eWca22Pf2uFjWaPQ4r59BOKq5EZCox_fa2nUUtFfbqlfsccDIWSlD7ISgRuYcq1TsCBxgJH_bxyTH67J-ek8h1kwim75W7EvK7HZ7yEzTjw-GfPHm84WnwvGvVXbk7rWwNVjvRaecXgZfl8E9mZitB7-IXcPqxlY3U9Zs9QbydiPwM-9dCtWOcNBV0paCPQw_lI6xWcl18ipHzWRZ2ZnMNsDu5pcKy9ObrojsJXfh1SlSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه C جام‌جهانی با برزیل و صعود مراکش به عنوان تیم دوم گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/95795" target="_blank">📅 03:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8FXg5a4R5C92l8IPlXvdwPQkMl4rB01CtP5fYw0lRM2jQdHyouxPk1ru1rPLOYwg4ZqzT84tKeoN4cs3F6c-uD7aJ43bxmR95YlDIaYPEffuBhrgvKKW3I1cvAH2o-lV8lFb9BfaXsEDQ07YZ_qTA8qn5Ycvm8NhPIbvO0cXkQclJj8hrrRhbNoaw4KKaBuK38iCefGDbpLddY52MQLw-ekaDKmy0f_8oDuoEndFh36r_b2_BS5n5X0Hh9rGEfjAXCrYo2Js7xSQJ5_DegvQUrRd6o8bj_ChMuuRiRL0VN0M4PE9qtMOKB8vD3HBoZxuvcLvsTzaPOqbvEVJuvv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک مراکش مقابل هائیتیِ حذف شده
🇲🇦
مراکش 4-2
🇭🇹
هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/95794" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkBlUOOPWkHU_U8GOhrV3TIV48P-f66hDuJZsKf4eqZmIzT8wBr3vh-Vsvde-zXY9QG5VlkSBVl_DUlVRtWuIY1Qgx3s9-0EObWtgOsop7ei7x3ZCzuP6kUKCHkCMQ8Iaf5bYy-BkmsoRINdquMwt-hTq9apZi1ARBHMQEHNUWBuTyaN3VqnsYjt0D6v6S_GV3poKyScftWwexO4h1bEGpTO0XuaCQOnj1fkgbr5eZo1-fOdVSlEyTeUGvaS0MShBzBDqyyGG-ENeObg6wZxEqplmabXLmBswQ6sgZhw0qhOi9mDmwDN_oGQ1cJB0k_Jh7e0WcK06AUutETZUBxAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع سلسائو مقابل اسکاتلند و صعود به دور بعدی
🇧🇷
برزیل 3 - 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/95793" target="_blank">📅 03:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwTZQ9LmTM2jX7hV_NnmxBpTK-Aci2ShPMrpxx-W9BZ7qEeLx_FFuzJ7yK7BP1DzWG3_7gkiatYQk1J4dvAd9Be_c8U3TJ_FVewApbF97eSL499gxi5jqMa5DutltfV3Jil1U0SpQvyAoliXvos228Ef5KgaZ7Lp5zRxG3bPxiKeK-ZWvUeYeujdR-6mz-IFm72myYgblkkYJ-mVAKPcNp8_0JzjBiMbKkZazM14esXuxyJjQ07yfGqJjSQG2VmoSMXQ4bvmDbT9gAxrYwBJec6mZR1YAsHWs1aSVU1LA220FMo7HKHd9QDW2CQY2GZ2Cam9gbbDJljNdYccok3Mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برزیل رسما به مرحله یک شانزدهم نهایی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/95792" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95791">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/95791" target="_blank">📅 03:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaN7SuOW2MX_OTYhTuORAwhicqI8Qumx0McRsiSNpx_8sDtILgfD14ssPnNh4WwEkJeHPinhtxkrRHuuEv8iBxzZhqiFEVpmbhGk9DGhy6AHdewztNDopADKoje8BJsul4LE26meU2-F-HR0UUvedWEVM1u9m8Cgzq0ijaRzHmFmUmJl2JT6JOWy-bLiXb4GbV21Slp4IK6VxxqVsPykntBXVpBMejwCcw0xvy-eTjvv1MHqaz3af8-54m_Txo0W1QmUEs24i1gJt8EGktuAgQ2a0GV0QlG5D_B58_RqAwQXMSm0Ctru6b9mt-e9RC_aArTEK_UB9cBKtid8yVjO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WV7zkXi_KHKhVEolXP7dFNJoz3Kh3W_uEoTmyV7-KXIIFLQKr2rYuVYOVKfQKu9Im_3PP5Zb-ApLJKQLgh1hKjy0Oc72p-tjCzo3qQdMzKc1JRT3KxmqCqI1Uo8udWcZWdAy2-OfY8pNLRHdAZMQ3GmS0f6g9D4WNsahLLS2b5VrdTJtMvoHdZMR1Gfxcq2JTJMDdi6neaF8WfoAuz6Uhp7yuygJEavqd5XoSbL91KfzbbUNNy_NQ0lS4WiC05o8uMVRsduSZHOOXdR5qt-K2V53JK-trvmsaEWYPtV6N780ATbXcgZ9JWttawdNFbKveAEx99jPyynwHoEtoWCJqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🇨🇿
ترکیب رسمی جمهوری‌چک و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/95789" target="_blank">📅 03:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M55HhxrMqtiirArd89XjbypjlF1-Y2Z30Y1H6XMeg38Sgu015Eaqx4MG8Fh45kg8d2xr1Kf3MNAGPsKojn4TK1y8V547mI6cqXV1neSJ7rxYKdtYGTTOBgOiRJI0xDKDsSmncEyipGRuKnHU7BnzD-xZvaHl4olmQYG9wqNZF68KAHE_saIfbCbHw555QgLeS3R-sfP6V79argae1yZN3CBwkIonAnkCmNWN_FR5TH4LZCbuMfsklWxPR5XLfpO-hP2VYHW9fGgSjclF9n9I33l50L_iMo1yk4EEFjNNL36D0N_hvv88eoFlWwxvvwYl4_1j6AtLEECbfjy5zA4wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/95788" target="_blank">📅 03:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/95787" target="_blank">📅 03:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مراکش چهارمی هم زد</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/95786" target="_blank">📅 03:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95785">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اندریک افسانه ای هم وارد زمین شد</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/95785" target="_blank">📅 03:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95784">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم مراکش به هائیتی توسط رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/95784" target="_blank">📅 03:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95783">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مراکش سومی هم زد</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/95783" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95782">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/95782" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/95780" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیمار بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/95779" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhDEUbmuGMqwFSN0QAGbu6JBkjacnuVqAdV_aNJ_oH8fsXynb8xll3yUeUQGrLtZpPA6EmhlOXsmHE9w-fmi7jfPi8cHddt4ecFSRsatZEiDEAC0HohZSLFCk9tzsBWzwxWJp1FJOuqwY5nmAYszU8o2iZnCeekHpzdaVGV5kKnIPO0tME9JiZ-Mxo-kgYU7AcS1_2SAVAdwfqdLZCj8_t1U7GQGn040W_1GKPPaPPGd9K0W9aDbg5chk5y9fI-sW85YpnPw_iRDFkwe2So0veTxrHurLo1GAlGPhnsp5XRQux_H3Pj5Lwvr1OGRSuysJcyDT4t-F4uSCuqIyJybAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr869GgRIvZZsSgIsxoiMw3UYGyB7RDLY5ccSzp7AGRtz0ZDMJrWwgIxnl01M9X3gOXXLX4iAavAKrLpsIotJuHBq5WNW4NfbEtTziH2TnO7qVBzKvP7KmjMfwVMEATGI-Z610f5L8G32ucDzVRjvCOncdZJf4-AGACFrv7L59K6vCFem7LhAiLyiYsW08i6o3zFa8d_1yQSR8JTyH600tltBfsVv8nyOTqNgxR1rBVflB833-bQ444EmSc0KXCIMreKHLNtTu1-m-J4EDe1ktBl5oGbcPBv2Ym9J01iP1FRwbbtILFfoUim7UDBfXgukODVh1Xx9iB-k9ZWtD3TQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇰🇷
ترکیب رسمی آفریقای جنوبی و کره جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/95777" target="_blank">📅 03:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2gOjYMEpzhD1hvl5fR0eKzVn-08qFAdvFrmIeiRGmDUsw1MdXmfMH-osigFfUfdZ6wcBpa2DePSHUIdgLOP8jR-1vYfUSiEiWIcpyxGRhaGFUVAICHUp-ftxWzRN1aovO8Ax6ZPztVVhsepuNd5gxe2m83MvSGpUHfidYIPYjpwRPRDhOP09TIdxU-tJ-m4BqNhVPbOB66_NoWYy1tYOCOb0rvOt3vAS_ve0yj_gSKVpoIqlkJxWrWKO0hwIxUEM70XRavdV_dU0378rhlZwQf5f7WAQ-RLbS2QvqApCxcMWbdHdRvvSSJRz1E2GoViXm3QoYZR8UHVMcatnPGjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرفدارای برزیل تو ورزشگاه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/95776" target="_blank">📅 03:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم برزیل به اسکاتلند توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/95775" target="_blank">📅 02:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کونیااااااا زددددد</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/95774" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برزیلللللل</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/95773" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگگلگلگل سووووومممم</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/95772" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=DTW_yPvOqHSUOgdfVHj_fnHXq7FVaMx-oaGTHJlHjJNB5BR5At3MV4P1UPpTTD7jclKxTcv8MWYx1HihG827dxCLQ9kOriltpUbBL1cVqqYJKsO-PknNUb3OECO5KnpshPKVqa5yqP-VqHBbFsha6lVqAs-sFF_h0OVHQ0cY0eBCUmrVNZXJAsDmaXPOEeNAP6CzY8OkvcL1-YlmGY3469eMENGYZRgVzSH49VLCvUb7WX8hu2A6f8QIaqrCC5p40ovKJR8XtbbgsKqr7PV8n6WLtU1XmQhCcQkpC6UCpeQJ_i1zzG-5dJFCoBM-xae_FCKY7oEdZTKvA5ZaiDZLCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=DTW_yPvOqHSUOgdfVHj_fnHXq7FVaMx-oaGTHJlHjJNB5BR5At3MV4P1UPpTTD7jclKxTcv8MWYx1HihG827dxCLQ9kOriltpUbBL1cVqqYJKsO-PknNUb3OECO5KnpshPKVqa5yqP-VqHBbFsha6lVqAs-sFF_h0OVHQ0cY0eBCUmrVNZXJAsDmaXPOEeNAP6CzY8OkvcL1-YlmGY3469eMENGYZRgVzSH49VLCvUb7WX8hu2A6f8QIaqrCC5p40ovKJR8XtbbgsKqr7PV8n6WLtU1XmQhCcQkpC6UCpeQJ_i1zzG-5dJFCoBM-xae_FCKY7oEdZTKvA5ZaiDZLCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشمامممممم زلزله رو ببین ناموسا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/95771" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو کاراکاس ونزوئلا زلزله شدید رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95770" target="_blank">📅 02:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هوادارای برزیل از آنچلوتی میخوان نیمار رو بازی بده</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95769" target="_blank">📅 02:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شروع نیمه دوم بازی‌های امشب</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95768" target="_blank">📅 02:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این آدم فضاییای ما چی شدن؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95767" target="_blank">📅 02:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFD1k-6tIX2aHLClQcKNSiqZUGkXBJ_WfMarMDtUfY7mVJc5cSHR3XmXhJJW2TtWx55dv7xbbVZ_2L1V-vDUWvIXxp-VSKgoEYeM0VyZYNo_ZqyX3r0jZ1YYp9XO7KE6l7fWRZSxldBabUrcMHRY1S2K74VaE8fjbiWsTtLUVQErSYCkNv9QtJbLjZDM1NkO32mYb8BDQiXeHlQimez1q6mlbi_ynbBn1miYiNd5JxzHIL9ys29E7vngJyG-4b32xQVVHrqPYji9q5hwgHT_BAtQf8LCSRwP-i8-qt-HM6-5C5fSmHa37RtT0H6L7zdraMHmdeAG9eV6tAeAYAsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وینیسیوس جونیور تعداد گل های خود را زیر نظر کارلو آنچلوتی به 97 رساند. بازیکنانی با بیشترین گل‌زده تحت هدایت کارلتو:
‏
🥇
فیلیپو اینزاگی — ۱۶۱ گل
‏
🥈
کریم بنزما — ۱۲۱ گل
‏
🥉
کریستیانو رونالدو — ۱۱۲ گل
‏
😀
آندری شِوچنکو — ۱۰۳ گل
‏
😄
وینیسیوس جونیور — ۹۷ گل
🆕
‏
😃
کاکا — ۹۵ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95766" target="_blank">📅 02:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHB-Qr3VZ3ZaIb19xedvzchFucPRprcWDW7oEPx2ips7ML36caoJxeW-fxdGAHJQWNFL6Da30h8ehiQ25TA5CL2q_by_7goH9KbCJLFyA1A1xSQ0nmQ-a2SlLFumcZNvr3lm34sPRmX3ELpWM3WEOcrAnhnKszKwWAOVSF-FmQy9fzsW9BGHO32hj8VBQ6X9ffDs93JW29h_rE6W1d9dgGr_dYPnyQDsnR4nsUlemWeuL7bZ0X7PUDZ-mitz3wtYF9OQZsLJYeEXK1lwBfag9WySskegAT-Xu5gA4oWNABQIH8qW2XNkivZsQlE2Hzk5hDxsdf5uKUiJFFAp24padA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇦
عملکرد درخشان اسماعیل سایباری ستاره تیم مراکش و باشگاه بایرن‌مونیخ در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95765" target="_blank">📅 02:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osj4otaPrtMnDGdRXP9KLYmr7vLUv5UVeSEGJZQSk1FVequMrkm9PMfIigY3SwCyNIXhNvOSDxiDSWGRSV7yhZz7QCFPRPRFWpt9WRJRgjzzqtatvNzAIdSms1CbsP30DAIpiP-brsHKjNn45b8r4xk6TgVlZjr5sH09Y9KLWmhWi_2mvgELEAhAYMnDk8igqwUzHAMkmOM7Jxh6m12NtPS8miMbNCzhLSkU3YttaeYQbnLhkRv7afobjXcnUe8rUxrOcoO3HPF6guk6Hv3aIW357urzvnNMZ8YgDfxraSwGnQqvCh3_d0iUnRsj2vgJUgQL3Q9DBBDQ9k9wjQOazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس تو جام جهانی 2022:
• 4 بازی
• 1 گل
• 2 پاس گل
وینیسیوس تو جام جهانی 2026:
• 3 بازی
• 4 گل
• 1 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95764" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/95763" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3mvHIQaJO1O8kbtrhnKHznSWixS56ZyvV_3LYJBcQV_9j191ah39ZXwfc-voOYgQgKs4WGYt80efX5SyXdG9ylv2ib0gIwnzPD9UpV8KwkeuKG35uqALm3F7CvTqg0Tnp-p2sHcCr-exo9NHcn8JC2dkN1YpQU_ya_-89GfemRMWFdIcrcpPrQLARJZYYXFiLjTFavpTBqOcSGlumi1afS0ciRI6NneZ9u2bph67ng_aGyvWOcwviqcz_K2Wk3-vocktW0cUTJgzE78g6kjSNpP9iSCzFBxD0J5Jp-mJcZv_dFg3c2qKHXqL6bV1mQGe8zyTbHpKt3RoVP98vNV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95762" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پایان دو بازی در نیمه اول
🇧🇷
برزیل 2 -
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند 0
🇲🇦
مراکش 2 -
🇭🇹
هائیتی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/95761" target="_blank">📅 02:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم برزیل به اسکاتلند توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95760" target="_blank">📅 02:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95759" target="_blank">📅 02:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وینیسیوس دبل کرد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95758" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برزیل دومی زد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95757" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95756" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=WGDA10np2-TIa9DiubFPJFb9V8MaDB6xUNLZy6884HZ96n6Zke1xstwfGtwckvf3MAAIDWbtNjIUPBmgP9Kou16gqdVqUF277-bZdCUo83dsKGRZlbaBPNYX9poz99HRfVeeXICxYIYyfbA3kfGu7o5zY1LuKQ546SUm_rfrgIdnst6hM_efGM2j64VRMVPZS2cjcii4rJbNL4JN3fyuUOZCYsAiTIdNVARZXsj3rpYeY-srVpMLXVK8DgLyJA6vb0feRdw1gmw5hvB1q9WbadnYX6gYIeQYwho7GiKFO-k7UpIKtjVY0eazVBcUeP1vR7djbe9PNL7B8jQjuQhbTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=WGDA10np2-TIa9DiubFPJFb9V8MaDB6xUNLZy6884HZ96n6Zke1xstwfGtwckvf3MAAIDWbtNjIUPBmgP9Kou16gqdVqUF277-bZdCUo83dsKGRZlbaBPNYX9poz99HRfVeeXICxYIYyfbA3kfGu7o5zY1LuKQ546SUm_rfrgIdnst6hM_efGM2j64VRMVPZS2cjcii4rJbNL4JN3fyuUOZCYsAiTIdNVARZXsj3rpYeY-srVpMLXVK8DgLyJA6vb0feRdw1gmw5hvB1q9WbadnYX6gYIeQYwho7GiKFO-k7UpIKtjVY0eazVBcUeP1vR7djbe9PNL7B8jQjuQhbTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل هائیتی به مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/95755" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مراکش دومی رو زد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95750" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95749" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عجب گلی بود جزو بهترینهای جام‌جهانی تا این لحظه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95748" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هائیتی دومی هم زد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95747" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/95746" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=Vgd_LQ-UL0nf5W6haVkPzLFdjwOJEQqqJDFOxzm8AKEplCwa7yRBXj4jCjTAYnCZJ4FScmN2F9d1mbMglH39wP8vDMg4vPYxSldBwiNhzEvsXOyXXtP52eIUY1vltn7C0dc7BvcP8pJvkHu-u4lb-BDHxBDuzR1NWSGKzjny06fYgLejPUvtBbjuKJ6b3ACUfaJ_moVFCSd_rAIXJz7FRQzPHoIGecknOMk85DMbRJwpM0nTk4xujOpWmoTEo1uPqoLWTT1it4TdIWlEJlPSprj0j9-jbW0Y3Q6z_SQl2WGy-amX98R_0vknby4NWjzu9SqtGv3fUI0YsEXZWmrkIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=Vgd_LQ-UL0nf5W6haVkPzLFdjwOJEQqqJDFOxzm8AKEplCwa7yRBXj4jCjTAYnCZJ4FScmN2F9d1mbMglH39wP8vDMg4vPYxSldBwiNhzEvsXOyXXtP52eIUY1vltn7C0dc7BvcP8pJvkHu-u4lb-BDHxBDuzR1NWSGKzjny06fYgLejPUvtBbjuKJ6b3ACUfaJ_moVFCSd_rAIXJz7FRQzPHoIGecknOMk85DMbRJwpM0nTk4xujOpWmoTEo1uPqoLWTT1it4TdIWlEJlPSprj0j9-jbW0Y3Q6z_SQl2WGy-amX98R_0vknby4NWjzu9SqtGv3fUI0YsEXZWmrkIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به هائیتی توسط حکیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95745" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واقعا من واس همین کصشعرای این خانمه بیدار موندم بازیو ببینم اونم با ترس و اضطراب
😑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95744" target="_blank">📅 02:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مراکش گل مساوی رو زد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95743" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/95742" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/95741" target="_blank">📅 01:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وینیسیوس دبل کرد
🔥</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/95740" target="_blank">📅 01:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلللللللل دوم برزیل</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/95739" target="_blank">📅 01:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQOutR6g3N_rDjbE7t9gAk9ZgKUy8NbU-PYK1vCK_krUfDpppYqlX6ynDLpl01i2faxCZLhOg65bxn1eBSXgZ2hI1mJ5cIbEvY_prZMgu4nIpeWThTvSlWIgYotAhTl2gr9hX4vjUPDVbOCfVIuQRMnH1jQHZDWfYuW-lRR98lwMiSlVPAx6RUgvv1c3-eIEN0uuG-eEMY_vBktXUZT_bkysRhz6GhYMgF-AnHhtncqJPz3LfvxvEKHsBjF_erBI6lmz-HiDQO-TmzGsiwQFenKfEf8zfeaVYVG6NKjfB9zERg9VcpwxDRUHRSAJIMsCEvWWMoUwXtE40gJ0LRMZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95738" target="_blank">📅 01:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/836ef29bfd.mp4?token=KvUJNv6BCuq4gOv0b9xkrWg9nmBhIj_e5nV7pNRXn19e_QLPAHCNQnZLgQj4G43xOylISIdvAvyC-GkogUyfPTm2kmrPxXpN8-upekAt6-JXY1fwQZVnyzqFXhsA0kWJb08ntvA16S6pEm3VsGjkm7qS82A3RITcv4dBXeAQrmGtphqlE61cq8QbOD4mq-Y1uuzO8RQz5yDU34N1DSZc50ZunN-2lET26Gb5Zf_FotM-X575nCtYc0c-1Vng0O4RX7QZUGCWICoo2OpuTVxAkKZNB2TpCOFDIcamhYrwKOydlF6ackieAFb4pIPxljnwe1g5W10EfqwcgBuMorNTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/836ef29bfd.mp4?token=KvUJNv6BCuq4gOv0b9xkrWg9nmBhIj_e5nV7pNRXn19e_QLPAHCNQnZLgQj4G43xOylISIdvAvyC-GkogUyfPTm2kmrPxXpN8-upekAt6-JXY1fwQZVnyzqFXhsA0kWJb08ntvA16S6pEm3VsGjkm7qS82A3RITcv4dBXeAQrmGtphqlE61cq8QbOD4mq-Y1uuzO8RQz5yDU34N1DSZc50ZunN-2lET26Gb5Zf_FotM-X575nCtYc0c-1Vng0O4RX7QZUGCWICoo2OpuTVxAkKZNB2TpCOFDIcamhYrwKOydlF6ackieAFb4pIPxljnwe1g5W10EfqwcgBuMorNTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇭🇹
گل‌اول هائیتی به مراکش توسط جوزف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/95737" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f3b95bae3.mp4?token=EnyIpY0RA23eggG7tJXJGq4rQjUZzSveghpguHxU-g0TF_4aDm6KWeMLpKiuLOABg_f2urM_XX_tsNYl0lCmwOXP_v25lNa5NnESDevuKYGEq8Q51O6wyLjEdWMSq-1iIhohG0hWalBBuExclQAVtVaBXNu1ObnfPDDSSbwAHx1ubM16Mp1wZPkwHL0DlVBsKsIQFqxAs_Z1Fn2hLR8-G7bRKsEP_GqaCyTNSBY4ouFX_-4B_RfekpmqcWpYYRUAv8Dgaq-POYCSSrdwcaN7Bs2nq9R02i4MAhlepdywJPxc_y6K-8ndUaqEE2ndgt81hqTTXL-M8dpENEIHfMOKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f3b95bae3.mp4?token=EnyIpY0RA23eggG7tJXJGq4rQjUZzSveghpguHxU-g0TF_4aDm6KWeMLpKiuLOABg_f2urM_XX_tsNYl0lCmwOXP_v25lNa5NnESDevuKYGEq8Q51O6wyLjEdWMSq-1iIhohG0hWalBBuExclQAVtVaBXNu1ObnfPDDSSbwAHx1ubM16Mp1wZPkwHL0DlVBsKsIQFqxAs_Z1Fn2hLR8-G7bRKsEP_GqaCyTNSBY4ouFX_-4B_RfekpmqcWpYYRUAv8Dgaq-POYCSSrdwcaN7Bs2nq9R02i4MAhlepdywJPxc_y6K-8ndUaqEE2ndgt81hqTTXL-M8dpENEIHfMOKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گل‌اول برزیل توسط وینیسیوس جونیور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95736" target="_blank">📅 01:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95735">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مراکش خوررررررددددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95735" target="_blank">📅 01:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95734">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همه از هالند و امباپه و مسی میگن ولی ترمز وینی پاره شده قراره بگااااااددددددد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95734" target="_blank">📅 01:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وینیسیووووووووس
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95733" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برزیلللللل زددددددد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95732" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95731" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbzk3l65dVoQTufp_weSnxdRm7jOpX0lT0OsCS7PPHQUw5FNZxL0HqLwDwFiUAwbOSl6fHfH5w5P8mXLIDMY2UAQdQKZTUqos61HvNbo2Be-7qFM8-lyjYH1kZC6dYnIIfuhjaI47XQxAs0gwbq7jVdwVxyXaorpRW0jJazVTqUbk2nXKgMbkR_APqVD6ZLWo7nbvza5kCMo_UKLuWukieXOU36MyLaaBjVbLhEuUeGuQ6Rt5C1_o1ft6VrmcCX2Z_LomTYuR2vUPb_EuTq6dEVbI1y9I0MNfjTeIvOuwRo8Nh8HFLktYqg0mCk6tJysLIhCIFR_ucGlaw94oui1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95730" target="_blank">📅 01:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNWmGile1m4FZSm5tRGtTyOrhxLmnXIt3qNW-i3Avkc4CogKm_LZOVFgE9U_jivjfzA7_upBepqa4RlwReawizmtM0pZkwt3j29_Ks3QnQv_tOtZDxq9-F4d1HzLVFIvG17OLTfjpXSjnIbar-jkOXoc4KVr13jOaLZ3Mp387kQ-PYb-ACM6kPqpLAngzU2ZdxMFsPfE2EPG5b_d9cM5-s0u-j9DU0BGafCs97PP8ji-n15xd0BRe7tk5NWRMZk-v-2Ht5wXQA_Dl-vbcMKisnnpylJNQ1bNebPuG7apDp9trZuGTTuQA0_z_CaNQBepg_e4ymnHNVfM5e7kTFZFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
🇦🇷
برای تولد مسی هرکدوم از بازیکنای آرژانتین رفتن یه عکس از خودشون و مسی روی تیشرتشون چاپ کردن و اومدن با مسی عکس یادگاری گرفتن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95729" target="_blank">📅 01:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شروع بازی
هائیتی - مراکش
برزیل - اسکاتلند</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95727" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHHHGPigVpS5ETF7nd7D4UZ1reYriA2Za-uCiewp2__eLg1mNJ4aj5ac5K25xOFBUvBgbymRJjxVDfSK4pbg1asP8AKcPTJmumnhddsm6uev2mQN95vuENmNg0Dp6hZqKDUxhhQ71bMMsiQmKXgZVh6pv8VQoC0tJEbIDkCBDo3eTFF3oFMFeJxKr5_zGbD4YfE1iuMF2iI4jbCZLdHMazWPwvKxrvTKQGDM3w3oPp5aWEPhYUT-o8pEmrUxsT7pxFij41jDznp263mdbNTNWBhfv5cqpQWkdWMvnrRVgL34f27QEHht4vFO-9XhBYDIR1xiTb_KnYGP89Ja09FLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
اینترمیلان آماده انجام هر کاری برای جذب نیکو پاز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95726" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe1759a1.mp4?token=TS_Q-U7SOUPs7wctcsipz2rBONymm8B3rPw_LL1yblRcpQ2a03tBqW131mcO_GarfyYObATsmPZRdmMetNI8vhoVc7NDyd4NM2JPb12RpHfO9g92cyNm0PMeDxl52nDC9xw6TljXd4PWrwqPDyvsL5u8f0_dl6mPCaZbQX8tONW2z610SwBg_yO3ge7EoKgJ43b9fkHlPWXdbt4ddENAqvdS-MiJH-a-hbA1Te0XpsVCc2Ec-KaxEpYkDkwop_7dBAgrtOHYU7AUACHDf_ZsE_HGBw3f8zFc8Uga5VKqh3jV7i5ConuvdZQTKKsLveMAjyKfudrm7IUsLINkCdIejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe1759a1.mp4?token=TS_Q-U7SOUPs7wctcsipz2rBONymm8B3rPw_LL1yblRcpQ2a03tBqW131mcO_GarfyYObATsmPZRdmMetNI8vhoVc7NDyd4NM2JPb12RpHfO9g92cyNm0PMeDxl52nDC9xw6TljXd4PWrwqPDyvsL5u8f0_dl6mPCaZbQX8tONW2z610SwBg_yO3ge7EoKgJ43b9fkHlPWXdbt4ddENAqvdS-MiJH-a-hbA1Te0XpsVCc2Ec-KaxEpYkDkwop_7dBAgrtOHYU7AUACHDf_ZsE_HGBw3f8zFc8Uga5VKqh3jV7i5ConuvdZQTKKsLveMAjyKfudrm7IUsLINkCdIejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب درنگ، جایگزین فارسی کلمه hydration break:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95725" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSEQ4xz0yI_I9wHdD5hOKmB79UfK4c83AeY-UtJk43ynrV1gNpaQkHzWem-N4nh_dBWiw9-McSJ9NDaY_OQ3otStKu5v6YJsQD_0yyD-8l8JlUVK64O7yn0p4xD1TnZWE7fp1M8gIrhM6zdnar1LdKRmJEWdc8r3a2j-3gXO4BfrT7rQ7zeBft6Z0sROBTs-A084zJlIAAWzRKmKPQiesxAd-gD80zPuO-NOMlK8IDaEQ4xvhHk9cvohHjl31WlIij7saoj4bZGd-Q5YfKoWWq3w0B3MCWUVg6cgey9Zn8mXaHL5n9jrsiuyAEZfFUpLeXd-MFCDz2TeKG6EYdL3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تیمای عربی تو این جام جهانی
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95724" target="_blank">📅 01:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پایان ست چهارم  فرانسه 2
➖
2 ایران
🇫🇷
25|23|25|24
🇮🇷
21|25|21|26
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95722" target="_blank">📅 00:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS7eyR-5hhBtt4utsxmE3Jmg7fNGf98_gclQ37Xz1fYhINw9NfzoO7HYi4avrmh-5Zgh9z7sU08DKL3hpGml8DICKnuX7LFeTFsKHUeNR2UPaRbBJ56dw6AZwkJNkvCLBBeorD1x0JJ2tyTh_LCgRZ6PSoHunvUZkfJTVd-wib-Q6M_z4vzwJJayPV_nfveXxmdwm__gNfOaPg1F0MOz5Z3eC780_UIF0E_cczstigpd_UccWACCZGpOCfVdL8Vq5rwyCAaoprLBpFfjoTubJwTmiACzupRSxPKU1wiKAOLnSZZMukkNN-XNj93ZrhwaS3CnWr4mSit1ErTBD4sUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیشترین تعداد گل خورده در جام جهانی ۲۰۲۶:
۱۰ گل -
🇶🇦
قطر
۹ گل -
🇹🇳
تونس
۸ گل -
🇺🇿
ازبکستان
۷ گل -
🇨🇼
کوراسائو
۷ گل -
🇮🇶
عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95721" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgBNKeTIZDJdiwo20-0_SjNWfWIRxohgVbbAr_w3bw0LehVETTcWgfHiHuUZtcP_DhwpENeMFgk43jX4kll1pv0UXWmrr0IvSrNftPgI-k3REzxeUSlUjDdanhUPhJbkL54sznGzd05h3CVa8ZxVgopJxeRTIOKx8E4f2pESwoqnAJLrKRYvGRZmrrVs2rx0GCL29m-7u_MOYJJhY_9WztSNjXZh2aGN9AI7HVzuXpGtvEMZfwP0v0lFweJa50Je7gf4lL1Lz7LZR19H_lLT6klWDifefXVpQqQbglXEJc7hQFUPYoFTiXpbknw_ExIggENI-KkUXry8iczDWIsMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
❌
قطر قهرمان آسیا رسما از جام جهانی حذف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95720" target="_blank">📅 00:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95719" target="_blank">📅 00:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub_0uc8deMA7AkeYgmNcfYP_nJmfebwJj3pJUMj9PgBfeBvy5EgjmcKCyONwnllaMzacEnnMpsLZyYnrN1HVPinxiz2tA6D9L5rdS6B2MybebjbhwyxEsIOZfNlJjNlgwfpCdlXrCB3_3yPruI3t-pDUfQgfhurB-s8nRKio7swLRVq_LP-p8lEIELnsb-BwxxsmdXvn6dPo3Quj49fAkRCSs7ShjM1pXNowW0323fzl6St3akAZpPePlO2kRRaBoFlLBxXQe3y4BVlzIDbDCmF9pd3m6RSx3aPLH8nYm7ogrnoM9FxadHHOSHM3yKsdFYrM3eIxIt0WsqB0dS-S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
❌
قطر قهرمان آسیا رسما از جام جهانی حذف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95718" target="_blank">📅 00:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJCUG4EWc7aQvKtQBWLwjXiicswwuAoVTMoR6WZOy43-odLTbQr80zhaqxUEtTS5sPyz6yg_EX4EE2gNVFallMkNUYsDBm9kuL6cGFKxD05vv7KqRPCWdz2SmiwKWZjLPZK2mQEALthv9UOYkemnTw5rxW-4GzsgC_x5__fRYmWtCcBggV3840sGFcg7Be7keWytgGjwR-Iel91VPhSjKdopyV9t2jrrQwzygF63pz69wgq6g0KpgXdG70flTpczX052yquSydreurhKTPHk61aLHSidPZeTr5bFgyGbCWpmggtohEXMov7NdQYZs1ZfptsMjbNpg1BUv5h0j8PHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم هایی که تا الان صعودشون قطعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95717" target="_blank">📅 00:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پایان بازی
|
🇧🇦
بوسنی
😆
-
😃
قطر
🇶🇦
؛
پایان کار قطر با شکست مقابل بوسنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95716" target="_blank">📅 00:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پایان بازی
|
🇨🇭
سوئیس
😀
-
😃
کانادا
🇨🇦
؛
سه امتیاز و صعود قطعی سوئیسی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/95715" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان ست سوم  فرانسه 2
➖
1 ایران
🇫🇷
25|23|25
🇮🇷
21|25|21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95714" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=dqVH93cFNRZLTYNpmRIvZjBPjajr00yJhTkhe5oDfWjS335QTTbPhgPHkwVVFm-GWtOTma0gB7TjhSIPMzLTDji0j9wORDQ7UKYrmEKv8aJY5bWFtNwpJpYTu-FwUwE7VfATP8lRoe-8AVbhmctz1YC63q9jdQ4m-Xo0AuFDVnbPktPcwa50tBcy7ngjv_MuQJFQ9w6ir0dg1kKPFOcEFOl9mLe5bE46HKSESCm0bLws8IOaLTWN-KKT7LpiVfwaDo6ZCBoX3iNCvqNMhWhyY05bflmslhJb2c_xWiHYlm-T77TELtuXYVJkREWZR-Zvkb_fGclWZ1OKqu0N_6R4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=dqVH93cFNRZLTYNpmRIvZjBPjajr00yJhTkhe5oDfWjS335QTTbPhgPHkwVVFm-GWtOTma0gB7TjhSIPMzLTDji0j9wORDQ7UKYrmEKv8aJY5bWFtNwpJpYTu-FwUwE7VfATP8lRoe-8AVbhmctz1YC63q9jdQ4m-Xo0AuFDVnbPktPcwa50tBcy7ngjv_MuQJFQ9w6ir0dg1kKPFOcEFOl9mLe5bE46HKSESCm0bLws8IOaLTWN-KKT7LpiVfwaDo6ZCBoX3iNCvqNMhWhyY05bflmslhJb2c_xWiHYlm-T77TELtuXYVJkREWZR-Zvkb_fGclWZ1OKqu0N_6R4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
گل سوم بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95713" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8-OC1NTg_JEG3vHjDW3xv5amhdUGzMZmTboh_-y92WJPABlF6Sjy0oCaz2-IOEtj1rMXeTsgpUU75Vz_FlWDZqaVvNlbCl6iifky2DozwU0KZvq8TxpsMbSxv3DvK2O_jrNUL7vSzEluMwjgavfN0O7p44zpXaagYzzeLPEcdnPZe6ghUytobUCfuRpGzRfcwA-1FaIw0WS20p-Cbef7DOlSxolIIZ1RDvcyq6NsnB_oq1Ti6JB1p0fK4l2u25QO9v2BlPXDtaUT0NrtHMNxuqWt3CPdHBX1hq00iy9JBAcLdy-dWjWnL4xCwj47vHjDoAuVjl4knoyhEXT7Vqeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-j8C_HtieiQnYoEP6T28ORvMytNtapGHL1ag7h0y-VYX-mei8WVDmvzMoCPSS7IaBjetI4jy1pCMRmZFCu0pWFGuDrJiX_v7U4Zz3oOsbT7wO9PtWqPQQCxKNnaXIGWuhKsVYQuOFKT9e7D6HH20sXb3EZRpkpFYTsA9-bUD2xDvIvTbBU8wnhWIBrUP6qEqhmVHUE_Blh0DMN_Rw0xGpjYjlIan7N3B_Ay0ayvz8JhCryibGODRFbKXvMrsBnleXhoXyuD_CjmPzRBQm4vAVdpM_RE-NzhZYLuNkMmLj0EAaDtWyTZZa3SYnEDlXXVoaA0_aUEOUaUw8YZ2YcElw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
🇭🇹
ترکیب رسمی مراکش و هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95711" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بوسنی گل سوم رو زد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/95709" target="_blank">📅 00:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=DyTo6KAfU3TFIDOsFLacyrudFdo4cb1bEwohYPO8G94870j6_upTRKMH9g_QsETQVbs2KvjATcgYHirqggTGt89uphN6xSJ8YczGGZZEOsSI-Aa8TWxSRqxpPwHXmB0s-FtERHqzVeR8P3Rz0uVMRz7P73mRNcMnIkqyY-0D8wdM5sT1nHC1lgsENHv1kH5X2NhGoQOvI2SlHvGsS7ZqBDDdPli0veqhtRiFYwUywFY4Uc-JR2VkyjdHN5Q4gK7rZtMSCrhK6o_uQUluUaQaCUuNqMt6swGQSTld_Ee6vEuuOI0FAMaGpETuk7PaH8Lp5dLOjrS_P4mZZ_xoW3XwXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=DyTo6KAfU3TFIDOsFLacyrudFdo4cb1bEwohYPO8G94870j6_upTRKMH9g_QsETQVbs2KvjATcgYHirqggTGt89uphN6xSJ8YczGGZZEOsSI-Aa8TWxSRqxpPwHXmB0s-FtERHqzVeR8P3Rz0uVMRz7P73mRNcMnIkqyY-0D8wdM5sT1nHC1lgsENHv1kH5X2NhGoQOvI2SlHvGsS7ZqBDDdPli0veqhtRiFYwUywFY4Uc-JR2VkyjdHN5Q4gK7rZtMSCrhK6o_uQUluUaQaCUuNqMt6swGQSTld_Ee6vEuuOI0FAMaGpETuk7PaH8Lp5dLOjrS_P4mZZ_xoW3XwXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل اول کانادا به سوئیس توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95708" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلللللللللللل کانادااااا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95707" target="_blank">📅 00:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdd2JZ_dXzcAYjl62HmZKTEGkQUy_BWPt6HSfSeCrqqSQ511hWTQNPHLFayi09B4Xt7dVuHPqKSGRfTYDgoNVq6FNk9zb0PlOmzKPjJ06C__LWeLk5IBBiuDluFjV0DF5STqlqQXh-fXE1sw0SVLTZETjyvpIiVUy9BLHIsuCLf2SZhxV0B3Rrg1fy64bBaVlWM4xcLwujHT9IMcIg4tE0xoD2YcQ0T7AUrRq0xFFVL-IsB35AYQMIeP-goHOd9fheQY-T9FDxoUG9WT5_jwNnsHL0iAom9BPA0dmcwWBPwvZu1PNkMDz3AGKsw0jShyiBDXsV879HcD5TXfhW1DIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
حضور نیمار در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95706" target="_blank">📅 00:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇧🇷
ترکیب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95705" target="_blank">📅 00:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02624180b0.mp4?token=Nr2uw3UrzSK025wFg_EcxMw-wBpC_faaR2WYMtTKdIIJENqUiIf99cJaeRx9PSwYhwXi4woRe6zNJVYQxzUWOViSKUHnPN2ab7yl9ux2fUtO2QWiqcX-9Z1bx5j7uky3VxXhNcVpYTmYbfPMo238nlDh7n38s-Ewvn02WHij5AOVBSUNQVIn-4FBWRA2RhKmOqWCSm4YyLiRVbpf9yTgfEJi9ktXcuCwHaDpLrqRAy4prh74CxHJMjsMUcTudMyKVLLmsMoH60RkKP5u2FOqS0saH5Y3HASoAHNHtQMQSwH5H1SYk4ex9lBYm3Ego4vuo_td9zrT0jBfzRfWsoLSkmLWP3ktWgHGvJEOYStNeKxtzX6yA9ypMfgwDdW07E8Kk6x8-YuloLd3OL1gDmaPT54Z8nRgYea1ZWKS1vjbJb5Re2PqRZSx4ZiqAU-lcJ0uEnac_exJe2tIsxthzNhOSnLEXbojIU6BD53SwzXLq1kz1yM3y14-5CUbi-XhaGpqHz5nnxfY92OgtCHfo8so0PhhUa5e9_luIlxwSVw6D9hD4aWWgnG56wqxIN4cVpeUyfIRIOMMzpKIKl_68_PA7SkeDhWY-nfih_ombhMuf9pn3sAoqA4oVjYspLOzpQP_AYOf6NvdB0H4DMTkphO2O8OZTV5oz1wzki0OnZwLMPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02624180b0.mp4?token=Nr2uw3UrzSK025wFg_EcxMw-wBpC_faaR2WYMtTKdIIJENqUiIf99cJaeRx9PSwYhwXi4woRe6zNJVYQxzUWOViSKUHnPN2ab7yl9ux2fUtO2QWiqcX-9Z1bx5j7uky3VxXhNcVpYTmYbfPMo238nlDh7n38s-Ewvn02WHij5AOVBSUNQVIn-4FBWRA2RhKmOqWCSm4YyLiRVbpf9yTgfEJi9ktXcuCwHaDpLrqRAy4prh74CxHJMjsMUcTudMyKVLLmsMoH60RkKP5u2FOqS0saH5Y3HASoAHNHtQMQSwH5H1SYk4ex9lBYm3Ego4vuo_td9zrT0jBfzRfWsoLSkmLWP3ktWgHGvJEOYStNeKxtzX6yA9ypMfgwDdW07E8Kk6x8-YuloLd3OL1gDmaPT54Z8nRgYea1ZWKS1vjbJb5Re2PqRZSx4ZiqAU-lcJ0uEnac_exJe2tIsxthzNhOSnLEXbojIU6BD53SwzXLq1kz1yM3y14-5CUbi-XhaGpqHz5nnxfY92OgtCHfo8so0PhhUa5e9_luIlxwSVw6D9hD4aWWgnG56wqxIN4cVpeUyfIRIOMMzpKIKl_68_PA7SkeDhWY-nfih_ombhMuf9pn3sAoqA4oVjYspLOzpQP_AYOf6NvdB0H4DMTkphO2O8OZTV5oz1wzki0OnZwLMPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95702" target="_blank">📅 23:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مانزامبی واسه سوئیس گل زد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95701" target="_blank">📅 23:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پایان ست دوم  فرانسه 1
➖
1 ایران
🇫🇷
25|23
🇮🇷
21|25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95700" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=jm2rOlz_FewWg1u-15P2-7rvb0aRv6fyV5hoccmOL-aS0wVkt_WYuIZ8n_qRVthWZ60a7FuE_37F9v-BaMZa8Kl0PaEJxjIYAyFTSrJNuGKBfkouAaraH_47VzOGMiXRjfaTXBHIgybrZM-ymm2XOVLFgrqRsXZw61AxBNyxY5CmzcaGlwwHOLK62pIHinOYrocd88fWv_MnViqkyx07J8KINU59B83uIQ2XPQj9FZJo5T2Li7LC5YQ5NDYZkU1MgUCS65IiSrToBn4gAA-Xf-KJQMhjFl0TPOlgYVNZTsUZuFS8bAoJAfXxHSbjNMoI-uOFsrLb7R9dBK9eK9ZvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=jm2rOlz_FewWg1u-15P2-7rvb0aRv6fyV5hoccmOL-aS0wVkt_WYuIZ8n_qRVthWZ60a7FuE_37F9v-BaMZa8Kl0PaEJxjIYAyFTSrJNuGKBfkouAaraH_47VzOGMiXRjfaTXBHIgybrZM-ymm2XOVLFgrqRsXZw61AxBNyxY5CmzcaGlwwHOLK62pIHinOYrocd88fWv_MnViqkyx07J8KINU59B83uIQ2XPQj9FZJo5T2Li7LC5YQ5NDYZkU1MgUCS65IiSrToBn4gAA-Xf-KJQMhjFl0TPOlgYVNZTsUZuFS8bAoJAfXxHSbjNMoI-uOFsrLb7R9dBK9eK9ZvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95699" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سوئیس زد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95698" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95697" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیمه دوم بازیها شروع شد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95696" target="_blank">📅 23:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVd9DW4tdQ2Pj1kxwwWNM3kXhTR6NFtjxBEgYvIkcqIiLpXSIj9cR7R_8hZ9wnfM6JYC4z05HwGJM0xl7a0X90dHUvvrlQA4aav0tuIthWKbRA_FUua13eUGPzDz9l9V7-km3ud1WgPbIvCvm12fScW9SK7kTzXERf0p0wxWfCzoG1li8-1szsUAJ-e2qCltOAbAm5TKBjjS-Hq4rxnU6WEyVaAyMIQEknck7rwSYarjMdQSPJiGcI3HRhlxT08hW58beyPv8WUrv8duYDc8YNRnz5FgeBWShlo3h4ddLp8r0wCfkSG6_lfU-NFOwXPGuE9Lvu60-8aUSqYzBcY2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قطر پس از بلغارستان (دو گل در سال 1966) و روسیه (2 گل در سال 2018) به سومین تیم تاریخ جام جهانی تبدیل شد که در یک دوره از این مسابقات دو گل به خودی دریافت میکند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95695" target="_blank">📅 23:29 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
