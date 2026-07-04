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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 642K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-98158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zyk8YQn4frQYhnv9unwjDjg6dvb1OLD5JbHFcCR36QF-AF8oBgI3HiVllXouYGom6FX2zDSA4PaHPfhPDxOCodPzJfND-Up1jtvaB02XmRPIU7e8Ut34m0DmrPG0ddHd-lhxtbvyTL4i59ngqTSz8SUSkCglRxoXMQmSStnUmiEi6yFG_XH1OkSAS9rpB5o2ftKbqZix2MznCYEZWmU658Bl2PEuwqkXeZdk-QpA5fbQTjV5wedbM8-qtR2d2ekstHhyiuor3dDmfeo2NzRbpqIEMI27cjoU6Or-p_RLluyjMIgyCSVJuQTC-PsHnqo4ckKAtTJZpeAO3cudEOdO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
هوادار جذاب تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/98158" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح‌الله‌زاده اومده برنامه ابوطالب جلوش یه لیوان آب گذاشتن و بقیه ماجرا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98157" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhVEa3_34w38CZbOCP3o41SYGKIi319cOImbazEy9Opb47J15VXukdA1kSugqJyY6SvgLw4_PdQ8J0S8zUm-xJ3DxVVTngKeLXC8qO1Bl68UorJNCeq57qXRhMv3eG8EXw4eHkvJgVnaXtAZrJzAFUQ9GGr4XpNycFLGBxmqC-wRL3bBLz6KYs3HcYKqWE_x5yldth6-riaxcS6q1QwZF-CtB7--PS8SQy4_sjXE8814olRVPH4xOApR0MO3-Qrn6YRT7nMp63VhTzJ2xdUpfQVA6fg8l9L6qeW41PIRA64DJEGhd5lJaTB4xVtkknyL4bAF5FmT8TPT_5DJO3n9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
حمزه عبدالکریم بازیکن مصر در پاسخ به سوالی درباره تحقق رویای دیدار با مسی :
🔹
ما با آرژانتین بازی میکنیم، نه مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/98156" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
دل‌هارو ببریم به سمت بازی Pes2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/98155" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💥
▶️
عملکرد لامین‌یامال مقابل اتریش که هرکاری دلش خواست انجام داد بجز گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98154" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYiYtaGz1HTIAe-My3SuJtrxPSTs5D9lIK8hYZ2kAlmoTk74WzoPVY106drqhxiCo-373IotslEVXiLfs7ujzSr40xaaTM0VObAbpgkWR6Qntp25JF3BZ1s1Nz148GJc3HiAfy6jUx-Aqw86UntwWViPgMLBth1oyukCA8JLtID4CyX3zUe5qhrujg-CeZMjGXb64tMVrTRgXYJ_4NzlNULJslU8CY5EJuMsX9b5xyD9V2UeGiS9nD2dO8rjn_AEE6RzP2Ittcybx9WYTkuFbj-F4UhBwLr2eJPJKn1JZmKBGGY9fssCAtsj-VLK0V3cnKjXu-6ZagbnjOaaZonGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که تا به امروز بیشترین موقعیت را در جام جهانی خلق کرده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/98153" target="_blank">📅 14:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYcYACRMn2AFEA1ByiU_UpaNF1bNz6vADeprpQQTq7dZQkKSKky5TW_N90Q_TfxADL7e-MN_3Mp_NYR0c447UCzwTSFU0uCUIIWVjgG8-S_OsgMrkFJOMA_rYx1b9gguWpp1DOqUek1IYUi7qn8tC7hBGdLku5hRg8DsL7uxV2yLV2wTwGQptQQ9wXMMxe6XM8jTqICHR0gTYFAqIqmthL7JqX9wsO2qzZq-WjTmaTbhDdKufQHKr1IU12OD0Olzd-hfjfivdasS9Nf6xZb3Fi-dZqR-uW9O5McNwX4tK3mPZf3c-PuZUk-rdCiIt3P-O3V5q8K41i_kl9ZZodizOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله یک شانزدهم نهایی جام‌جهانی از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98152" target="_blank">📅 14:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=YYWHEaF9o7U_iBHSXG4NoKNHE8T4-oAnBPWC3hDB4WVg-eu2gHBbGgestzzvf8VnTXxy_AiPaiJPscIdx7HXdj5T4SjxqoIAuRqJmFbIgjvOGhvTsiBs5HHvEY55BibuhBnMZlpD27cXbBtDedS64EcJsSv8GjdT8XOeaxgQb3uj-bNIbnPGgvC4NmlzHLqIrWhFbm-DfVYNhuVi_gca4hVRT7Kf1rvMzyQf16VdFsNDgAhEiC7mCuLdb9HOwpZ3dfa-mBGOq88ROJZ6umMmWdNZadgWVFEaD8KcMXnjAG6Rm1Od2kJIr_3D41ecQoQa7HJU5lObdw0yg_BDyqWkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=YYWHEaF9o7U_iBHSXG4NoKNHE8T4-oAnBPWC3hDB4WVg-eu2gHBbGgestzzvf8VnTXxy_AiPaiJPscIdx7HXdj5T4SjxqoIAuRqJmFbIgjvOGhvTsiBs5HHvEY55BibuhBnMZlpD27cXbBtDedS64EcJsSv8GjdT8XOeaxgQb3uj-bNIbnPGgvC4NmlzHLqIrWhFbm-DfVYNhuVi_gca4hVRT7Kf1rvMzyQf16VdFsNDgAhEiC7mCuLdb9HOwpZ3dfa-mBGOq88ROJZ6umMmWdNZadgWVFEaD8KcMXnjAG6Rm1Od2kJIr_3D41ecQoQa7HJU5lObdw0yg_BDyqWkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد صدیقیان از فوتبال دیدن فقط زن و دختر بازیکنارو دنبال میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98151" target="_blank">📅 14:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAnSjvvoUSrd8WrYW0YtnO5iQSSY1EtmPQI29FwpTNIHZYXz118gCw4Vv-qUpN4WZRHF1MYIPf7AjGW_QCrFB5Rlk2LlDrP6OP0gxTCVzRPWwr9aIJy-S1HdsGkGSKUdXKBDYBhDtJLWZn7a3uF91EuS6InnG5hpZrauqy6txzS4o10kU5MxQsrqQJeTYM4EZZcFmAWgzcMaM5Q6eQ5553uHdxaFZ-Xy3EmhsGHlOqpvokY2ZSPok8ejTdphg4tuket1QUIK0l-025IcTfIU3FWwnhS7BNb5bddEMJdkSTVdQ3fu2BUtTldUWxCsIywGRXTUihZ02NI_Q0dB9GV2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جیانی اینفانتینو:
‏"در این جام جهانی، مسی با یک سبک فوق‌العاده و شگفت‌انگیز بازی می‌کند. ما او را به خوبی می‌شناسیم، او یک بازیکن نابغه است و همیشه خوشحال می‌شویم که او و سایر ستارگان را در زمین مسابقه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98150" target="_blank">📅 13:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98149">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=Evjjyt3MGVaPCNIwAN3pNSOtJlNVIDk0-pqsgWqZnREOwwnIfO2XwnZtl6FmZTuehKymuQknSEVyW8iqfrPI5PIrrMfT70XL7E1LCq_uMSau6zuzwt9iVsZqbfkql_IRBkPy21HZofHO2VZZdeKILQFrwUzXMbbTZqa70fC-aFssruT9JScuAY4itzcrZ4dMiVFL7Ru9bii6tQnaPrxzUu7_Lnj2b_rV9yBsJhNj6bAJ4FxLcNwqyKQYvYJyLW7tTMWMo_Ry0-qRLWaX2K8Z9vnFvM670apLNAnQPGtd2LDsV5PP-5Qg71fPISspA4kT6ahdbmcyavX5c-VWWQVXbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=Evjjyt3MGVaPCNIwAN3pNSOtJlNVIDk0-pqsgWqZnREOwwnIfO2XwnZtl6FmZTuehKymuQknSEVyW8iqfrPI5PIrrMfT70XL7E1LCq_uMSau6zuzwt9iVsZqbfkql_IRBkPy21HZofHO2VZZdeKILQFrwUzXMbbTZqa70fC-aFssruT9JScuAY4itzcrZ4dMiVFL7Ru9bii6tQnaPrxzUu7_Lnj2b_rV9yBsJhNj6bAJ4FxLcNwqyKQYvYJyLW7tTMWMo_Ry0-qRLWaX2K8Z9vnFvM670apLNAnQPGtd2LDsV5PP-5Qg71fPISspA4kT6ahdbmcyavX5c-VWWQVXbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇨🇻
ووزینیا دروازبان کیپ ورد پس از درخشش مجدد برای کشورش مقابل آرژانتین:
"تقابل تک‌به‌تک با هر بازیکنی همیشه سخته، به‌خصوص با بازیکنی مثل مسی که فوق‌العاده خونسرده و قشنگ می‌دونه چطور فضاهای خالی رو پیدا کنه. برای همین مجبور بودم خودم رو آروم نگه دارم و تا آخرین ثانیه ممکن مقاومت کنم؛ خوشبختانه موفق شدم توپش رو مهار کنم.
بازی کردن مقابل مسی یا هر کدوم از بازیکنای آرژانتین همیشه خیلی سخته چون اونا بازیکنای تراز اول جهانی هستن. اما این رو هم دلم می‌خواد بگم که هم‌تیمی‌های من هم لیاقت این رو دارن که توی بزرگ‌ترین و بهترین لیگ‌های دنیا بازی کنن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/98149" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=tzNnHWB-GNSJvUWnRlSZJolA1K-1WxZYd3Grj4j9Ty1yjlpqNR_xChv9FPRsyMjH5dYWY2xYM3zQiijGwZKnlf7F8zS89hpN1XaiIRTBpbLRxxxrio-srPBkokP1P2OzB9c8UipjNOEZctbJr4gnflyhupaD0yH1xL-W_04TB7gygx841UyKZqypRmePK9QO3lfudWrA_zNqfPRytbsnezTx4J2qgFHYrhKdMfzzDRnblf-6ZXb1qLPU8sOL5DVlpPft15R1C90J5s9bJkaeobYMnu3jIRhjCm0JN7B9ZR7ADbFQujzpUZ1N-h3sDUbmv43vL42kOijo3sqkFxqqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=tzNnHWB-GNSJvUWnRlSZJolA1K-1WxZYd3Grj4j9Ty1yjlpqNR_xChv9FPRsyMjH5dYWY2xYM3zQiijGwZKnlf7F8zS89hpN1XaiIRTBpbLRxxxrio-srPBkokP1P2OzB9c8UipjNOEZctbJr4gnflyhupaD0yH1xL-W_04TB7gygx841UyKZqypRmePK9QO3lfudWrA_zNqfPRytbsnezTx4J2qgFHYrhKdMfzzDRnblf-6ZXb1qLPU8sOL5DVlpPft15R1C90J5s9bJkaeobYMnu3jIRhjCm0JN7B9ZR7ADbFQujzpUZ1N-h3sDUbmv43vL42kOijo3sqkFxqqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98148" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXDG5dADUC0yJWH2i82zrCBR8-mfSSViSLj-v7I0SnggSHfMXKItoBSgiJYKhjZgVQTC9GdtTN3Y7cdwq0gf6E1VqQ9HuagZYc_6FZTljWY2yfkw7y3st_1NU6YCO5zZcY1iPajdu6hEFgDlNwXkHD7rlJ6in8HvBLEXUv7jbaGcuYiqLGjHjRbODwilgi3z-qkRn89F4qYRzMNxVw5ubrlZIB_PAVYIGkpPgzPpT2yDGQkcROJAEq7wuQGhu0fW4qAWTojRPH7ErRDBjUhjHNA0-gNzkE-ZZbykqli3kPK5IMshLPUava-FQWiX8tXY-Zkjh2MZfpkfa_zFUwyvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98147" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=u3HIHEN9rn9-Os1zkBgwFCSp85YUSmv8yF9dcUClJWSC_WCQxh1yOOPp5SIC6MDiGpj_iQp5NkGoLfK7KisnTB0X-F2UazpFfEqGYU24atf11B-Kpb9cqa9vj5Ik-WvxVM-nxELp-crnol4vMjHqS5DH05NNXwR2XgnQF4Sr77afq_3dBXWrxfa6cHQ1F6mwx2jt3q2F_a2MtBKsaaV_JpipLvomgddp2ltBojZvWcXW5rHmOaRiubG5Ejh3hCQpQQN4LTypjgk_P0ZPrqutKtZ8efeywOlJA68uHlyGHLEglrYXrr1xy_5aEfncalETwpL8sNuSglUTwjU5BfA9YJlidxxilPEO1JhzPnX_Ng0AhMUCXNv4cnsOgBQYhG9x87QqC4gkHOIQ6OM5e6JHqMJFOSqEYzA_-yi3J4KsHITJywM5-LHEy8lp7zzUkon-GV4EG4qqkZijhvvEnqyrQjx_ooYZoLE2aphXbDd58pGjC5X9uwWZY_21l4G7e73fUTl10Bt18UF2b_UXLiqYbPu9V7266z3lGql-od4PJRpnPoSHWoQVhn30MMB65gWSAfXBu2PgK2Z0tPnKhHbadPQYPxhZ0PUuq1fbdCORQP3bD2rewa8I_Z8JA-y-k-9Tik0uxjQNBtEibR3ExgAjV0mFJccapBVgGn_TwXvucKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=u3HIHEN9rn9-Os1zkBgwFCSp85YUSmv8yF9dcUClJWSC_WCQxh1yOOPp5SIC6MDiGpj_iQp5NkGoLfK7KisnTB0X-F2UazpFfEqGYU24atf11B-Kpb9cqa9vj5Ik-WvxVM-nxELp-crnol4vMjHqS5DH05NNXwR2XgnQF4Sr77afq_3dBXWrxfa6cHQ1F6mwx2jt3q2F_a2MtBKsaaV_JpipLvomgddp2ltBojZvWcXW5rHmOaRiubG5Ejh3hCQpQQN4LTypjgk_P0ZPrqutKtZ8efeywOlJA68uHlyGHLEglrYXrr1xy_5aEfncalETwpL8sNuSglUTwjU5BfA9YJlidxxilPEO1JhzPnX_Ng0AhMUCXNv4cnsOgBQYhG9x87QqC4gkHOIQ6OM5e6JHqMJFOSqEYzA_-yi3J4KsHITJywM5-LHEy8lp7zzUkon-GV4EG4qqkZijhvvEnqyrQjx_ooYZoLE2aphXbDd58pGjC5X9uwWZY_21l4G7e73fUTl10Bt18UF2b_UXLiqYbPu9V7266z3lGql-od4PJRpnPoSHWoQVhn30MMB65gWSAfXBu2PgK2Z0tPnKhHbadPQYPxhZ0PUuq1fbdCORQP3bD2rewa8I_Z8JA-y-k-9Tik0uxjQNBtEibR3ExgAjV0mFJccapBVgGn_TwXvucKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
فرنوش جعفری گزارشگر دختر ایرانی: رونالدو قبل پنالتی گفت بسم‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98146" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnhAStwVs4OiGZV4maycnsrk31zDhWLhgrt3perzm9t3j-GbxWvCROjdLBhYLSjuliyEuxQETmTN1ObOTcyXiKkNYcnx-rkaI4jpd4wp4NTMQxEJYZdRYodc-aK_Ns7yzoPUdbebnOcnskVEW4r-jf6JSKoBSLmIOycBiL4UXWgC-SXeCUP-ek5GJ_xWnJR_hZdSf-uNHjYjBgHnqi1YtSisJp3pyIUH3IbTnVk_59oklAk4TqWx5gt9kZRJuBzZkrO1vpfFLTtU0xe1mtYpJ-S2QjMtvBUUWZpsmbqwfI71biqbrnzIuLIT2e00GM_4vV6a6RvGNGXbQ_5Cacb4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#
فوووووری
؛ شوامنی بدلیل مشکلات عضلانی در بازی امشب با پاراگوئه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98145" target="_blank">📅 12:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=cdIerL5jjpJks-1YaI-APNWxxn_EleOgr5c19mo_BEbD-RaN9hG-jjmAMtfuPFXF7AxDRdMjgVQL_J_SJpzIMixw7PALvtbB4rLtC7vXLGMQ1IV7dpIjqnVW_Uz4RfdNibxeTRrSBovbmsmjVl5zf-FAeiyRKwIXVizqduNC_5Wb2NAsBZbCpLD31ZDWEW0sC3-bYUAYAJZ1pRQuThX6PtblTzvRqkHxRxYfDv4tO07czw-K3CXthcIURKZTSSa7zDGt5MyYfVRdk6qZkLQVCbZpPYR7l8xJIdbnYAOp1-z3xo46kr6HVqwKRBP8JmagRfnCSDJx2A_k-eXJxkmsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=cdIerL5jjpJks-1YaI-APNWxxn_EleOgr5c19mo_BEbD-RaN9hG-jjmAMtfuPFXF7AxDRdMjgVQL_J_SJpzIMixw7PALvtbB4rLtC7vXLGMQ1IV7dpIjqnVW_Uz4RfdNibxeTRrSBovbmsmjVl5zf-FAeiyRKwIXVizqduNC_5Wb2NAsBZbCpLD31ZDWEW0sC3-bYUAYAJZ1pRQuThX6PtblTzvRqkHxRxYfDv4tO07czw-K3CXthcIURKZTSSa7zDGt5MyYfVRdk6qZkLQVCbZpPYR7l8xJIdbnYAOp1-z3xo46kr6HVqwKRBP8JmagRfnCSDJx2A_k-eXJxkmsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👀
دیس هادی حجازی‌فر به حسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98144" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98143">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pGF4L46dgiWMT7_fQ1DYS_L48yXpIzWnKnuck4QVTVkn7aL3NYyOxJrhcDbAx4TuIPg9uYTvjp-VJULo9wW_fQcfHz82AU5O8jX7rWOCPboB8do4ZT1VnFssFz1DzBprtcOuEGeCsDv4LhxNNgohu8c4TlqGp_AhU7ao2oFCkHXhWm_BwSS2QzCBpG9sfD-qyiAW3xPpewvku4GlIQuLnb1GDc97cGPs17Xa3h6aUqPOWCYPcIOulQczLpAfxUIEpR4mg3HW9dWWRLLiwCx7zL7Tmb0QXtH-LcnDtBGjjn6hdwpyumB1XBQpYk71Vmx2rEQ1FuKz4MQ7_7ypgqbEKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pGF4L46dgiWMT7_fQ1DYS_L48yXpIzWnKnuck4QVTVkn7aL3NYyOxJrhcDbAx4TuIPg9uYTvjp-VJULo9wW_fQcfHz82AU5O8jX7rWOCPboB8do4ZT1VnFssFz1DzBprtcOuEGeCsDv4LhxNNgohu8c4TlqGp_AhU7ao2oFCkHXhWm_BwSS2QzCBpG9sfD-qyiAW3xPpewvku4GlIQuLnb1GDc97cGPs17Xa3h6aUqPOWCYPcIOulQczLpAfxUIEpR4mg3HW9dWWRLLiwCx7zL7Tmb0QXtH-LcnDtBGjjn6hdwpyumB1XBQpYk71Vmx2rEQ1FuKz4MQ7_7ypgqbEKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
رییس جمهور مکزیک: از مردم میخوام اگه جلو انگلیس بردیم، زیاد مشروبات الکلی نخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98143" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=LSfJcCvDOsr_Thr31xg4rN-un-uDAwP6pfMuuT1AYELfdZitDc3Nxu_WKAqAYzFDuLh1a6HHRuI856HRi1z36ySPeGjCIrf0qurEWRbAfcU4okhjukAdH2jccVVEzrXfsHe1tg-wQbLzbOn-gFjZklqZsjJbZEKhDWfpgqjU-cCCfMu5k8lZ6bp6Ac2XlN-xPloZ-UVPvo4WagRCRKPnAUMgI7xBcI0GqMEl8ISa9Q_k7T5-hyiWwLY1vyMJe074ntKeEr-C8edcirwB5ten4sthxA5E6njapMOpxppIk6slF0DxjJUiqIAn5Ax-E8vmdhmci3PcQZXu7rxB048KSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=LSfJcCvDOsr_Thr31xg4rN-un-uDAwP6pfMuuT1AYELfdZitDc3Nxu_WKAqAYzFDuLh1a6HHRuI856HRi1z36ySPeGjCIrf0qurEWRbAfcU4okhjukAdH2jccVVEzrXfsHe1tg-wQbLzbOn-gFjZklqZsjJbZEKhDWfpgqjU-cCCfMu5k8lZ6bp6Ac2XlN-xPloZ-UVPvo4WagRCRKPnAUMgI7xBcI0GqMEl8ISa9Q_k7T5-hyiWwLY1vyMJe074ntKeEr-C8edcirwB5ten4sthxA5E6njapMOpxppIk6slF0DxjJUiqIAn5Ax-E8vmdhmci3PcQZXu7rxB048KSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇵🇹
رونالدو با ارسال ویدیویی به پسر بچه‌ی ونزوئلایی که از زلزله جان سالم بدر برد ولی تمام خانوادش بعلاوه یه پاشو از دست داد، از اون دعوت کرد که یکی از بازیاشو از نزدیک ببینه اون پسر هم توی بیمارستان این کلیپ رو دید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98141" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=GuisvYSNGx2CY0_UkhJnI0S95Iv6GKIqxDDlVR6DdwqNaSJwcj0SgQYoGEq5F2V8BQjnUr9M--qZyJWj57QenfCmZ6ExIpYJXPmvUXY901HlRPBdwkJkuDcCt8oRd6BaxtigJUg4GF3CmooLspEWgF5PETQjXFKmWzGzOm1gfi-CHO-tQM9bVMF_rIPbk75MFARHtQzr-o0nH1qVe-1Fd3awu0lXZskwYM1x9CpNq5abOKHEEUTOPFzgkTayYMlP8TvgPy2dSWjBKRFXSAXOlUEVwGUygCyOKaJ9MwLpZoIlxBYf8_bAJQmmQ0zmclRC6ZCM6uG1HBnnmQj6TfEBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=GuisvYSNGx2CY0_UkhJnI0S95Iv6GKIqxDDlVR6DdwqNaSJwcj0SgQYoGEq5F2V8BQjnUr9M--qZyJWj57QenfCmZ6ExIpYJXPmvUXY901HlRPBdwkJkuDcCt8oRd6BaxtigJUg4GF3CmooLspEWgF5PETQjXFKmWzGzOm1gfi-CHO-tQM9bVMF_rIPbk75MFARHtQzr-o0nH1qVe-1Fd3awu0lXZskwYM1x9CpNq5abOKHEEUTOPFzgkTayYMlP8TvgPy2dSWjBKRFXSAXOlUEVwGUygCyOKaJ9MwLpZoIlxBYf8_bAJQmmQ0zmclRC6ZCM6uG1HBnnmQj6TfEBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تکرار ادعاهای کسشر فتح الله زاده در گفتگو گو با ابوطالب حسینی: اگر مدیرعامل بودم مسی را می‌آوردم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98140" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keXiKCByxK5qrVKle8ykiVF3HdXxg6lBuSfdjzNAuvq1hlWJZxupXr5mDHQtcTedIWAWNjF8pUcV-q_qst5TWt07ujuyLS9Ylh8Oi0RmOdj1BHCVrnFQytDdA6sY0eFUOKL8W-xcRzXvviZrHTjSXiavn1bDJiigI4AJZ_p5tP4fFccJB7Rx1GYFptLoP74CuUAPHzuZbnHsR2LCkRiee5uS4GGwAQ7jzbT7sOmexZWTPjYsL_AIMkyw1pj_qVzXA5k-YtnMh1-_qoZSpbIrqHtcSB33UPVDmPyIb4Ng1PdX0HPIKKybDWQyCBIeOQmZIf14bJ5oBQzI7P-_rmG-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_K-FonYuVwyjbUd6jY13-KLz620tRBivw0GxWFxbIXV8eSCiip5Uenm3tlLL2mti9uRbhyWT3rEhu_78nm2R-j-m8-FmLFyaE3ZVV9etsTCfBersgXKRghzUN1A1WwNr18pYhhOr5nGKT_iq1KUmllUIZTVxYfju1PWONAG8nz6YaQkgLBEK3l3iqGv0y843AE8m3_fEb3qzBknDFUr1aQtypqEtBLlr1mx3h1cSnPmbTjv5W0rk2wrX6L4I9XNrX4NtA6wwrBO2VOmOvJ47xaSfrd6kh2BFiIi6-eYghsEnGo3X2eoMqBwhwFq_EJCQWWj4RI7D6_TVRvSRQUDwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هتل "انگلیس" در مکزیکو سیتی، به دلیل نگرانی از احتمال ایجاد مزاحمت و اخلال در کار تیم توسط هواداران مکزیکی قبل از بازی، با تدابیر امنیتی شدید و یک "حلقه فولادی" محافظت می‌شود. نیروهای پلیس، واحدهای ضد شورش، موانع ترافیکی و گشت‌های یگان‌های ویژه ارتش در اطراف هتل مستقر شده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98138" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=WfD0W4oklH5KAOsmJFnl29RDLA6GnZtbXjqQbekadGvUXLrvWNf_bQeURmqibjvHZ84RKPEY2jS1PeJ_c7xE56N_8ZvHH6RNrya4jRO4GM-p8JS5If3KXjP4fJ6EZr1nxgHrETfDW4AifOeZACk6UPnQEKlio1TRhb40MhKlx-0dfAG5RmuQL23Tz8xhA1S7FQlgcpb5YCOn7CO6UImbMn7ZxPfV1r1IMYisoKqFx7HRi2ErACa4MiM08sdYP5bEq_FpH6p85XOg3htZpyRic0C7_1X64N-wxWMrUbIgQmvEmkEbqutYdfl1g8w7CmzGjx0rvxHfxgm7U-g5tbt9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=WfD0W4oklH5KAOsmJFnl29RDLA6GnZtbXjqQbekadGvUXLrvWNf_bQeURmqibjvHZ84RKPEY2jS1PeJ_c7xE56N_8ZvHH6RNrya4jRO4GM-p8JS5If3KXjP4fJ6EZr1nxgHrETfDW4AifOeZACk6UPnQEKlio1TRhb40MhKlx-0dfAG5RmuQL23Tz8xhA1S7FQlgcpb5YCOn7CO6UImbMn7ZxPfV1r1IMYisoKqFx7HRi2ErACa4MiM08sdYP5bEq_FpH6p85XOg3htZpyRic0C7_1X64N-wxWMrUbIgQmvEmkEbqutYdfl1g8w7CmzGjx0rvxHfxgm7U-g5tbt9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😎
بهترین گل‌ فعلی جام‌جهانی از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98137" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=B9b5YRHHyBT0YrOC1Dhq0T4BYYRso-72LdDorNseVqxjEvuEhbL48DUxE7qill8EXYCE0X3FEO-h_1Hey9c2oLjNwVNfGpoAMEFtod51lw_W4AkHE-fmNwU2Xylq52Lx33FM9DiDNw5gb6oTtBTCXvcaX8Jf8ks36o5rlTq27LK6aH8ZPfL8sGfs-dee0hZ7Tp6pNJwt6EJyML-DAsoe2_9HOlYGKHlZwp-jWCsfsIcOu4HJXj46mLhzvcbSSxlca64F7ahe0pKsSZiZ6lfqCrH9O95ASlzm4zXw5oy0tx24_53LYsmrMlRMmkvChcW3AvSG_GncqqwQFILRs9W4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=B9b5YRHHyBT0YrOC1Dhq0T4BYYRso-72LdDorNseVqxjEvuEhbL48DUxE7qill8EXYCE0X3FEO-h_1Hey9c2oLjNwVNfGpoAMEFtod51lw_W4AkHE-fmNwU2Xylq52Lx33FM9DiDNw5gb6oTtBTCXvcaX8Jf8ks36o5rlTq27LK6aH8ZPfL8sGfs-dee0hZ7Tp6pNJwt6EJyML-DAsoe2_9HOlYGKHlZwp-jWCsfsIcOu4HJXj46mLhzvcbSSxlca64F7ahe0pKsSZiZ6lfqCrH9O95ASlzm4zXw5oy0tx24_53LYsmrMlRMmkvChcW3AvSG_GncqqwQFILRs9W4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپ ورد سرانجام تسلیم شد.
💔
آرژانتین به یک هشتم نهایی رسید.
🔥
🇦🇷
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98136" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=gbJIRXKLWSX6LWq5VngXiiGKe3dhZXSi6RAxMPEK7Fw5MjZJYJdoF5zFkFIL9wty8fg4njVp8jA7nMGjhnG_6D7Ql2ElqfwNh6DQsykyMANqAmi-OPfblq07q-eEEFKLqwQ9axVVrePF5XYclFAUB9K4ObDKA_e7EkQDfX3LmWEF5fKrTq1cqude-I0a_J3eBtihQlMSESWVxWJ9rko0_CyxOwGcKDE7zqysIyU4pjvP4WWKKLcwpnDwgZCSPaVLbiBLwuE0NVFgngLmtjHF3Of4JgpuJc2l-MD1iSFOlOvI990H7JzPyUWltfZfAZ0qMMvo-VsABKEmJ2LIOrL8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=gbJIRXKLWSX6LWq5VngXiiGKe3dhZXSi6RAxMPEK7Fw5MjZJYJdoF5zFkFIL9wty8fg4njVp8jA7nMGjhnG_6D7Ql2ElqfwNh6DQsykyMANqAmi-OPfblq07q-eEEFKLqwQ9axVVrePF5XYclFAUB9K4ObDKA_e7EkQDfX3LmWEF5fKrTq1cqude-I0a_J3eBtihQlMSESWVxWJ9rko0_CyxOwGcKDE7zqysIyU4pjvP4WWKKLcwpnDwgZCSPaVLbiBLwuE0NVFgngLmtjHF3Of4JgpuJc2l-MD1iSFOlOvI990H7JzPyUWltfZfAZ0qMMvo-VsABKEmJ2LIOrL8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇻
خلاصه‌بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98135" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=dsyKvDuzSO8rUCEAgx0dWxhmWYVgTHbjnLV4xVbsozg_7mZkUypSeo17dxCb7ak6SRTqNZIWWH3dxAVStY122LZ-igv7bTBZkx5TQ4ELqbQ7u1TDWFQZpxVKNf9NSB7n02gorPAyjtqfRVpLOr3HKnceadg7v5P8CmAMOzR1kz4osbptIDh5lrgWkEbTez4x-lB6GMS6aH6cZSVQEX1df67_IrUnDNOsmapTxJxrukVsfGm-OsX6pxIzmE0KsuRyGqZOe7vAslrY7r-1nZkXuL9fcpbMljvisA2jhnk0N0X_nWty5jmrXu8w8wFniz7rhD09vV8-JAcCaZLzsiYtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=dsyKvDuzSO8rUCEAgx0dWxhmWYVgTHbjnLV4xVbsozg_7mZkUypSeo17dxCb7ak6SRTqNZIWWH3dxAVStY122LZ-igv7bTBZkx5TQ4ELqbQ7u1TDWFQZpxVKNf9NSB7n02gorPAyjtqfRVpLOr3HKnceadg7v5P8CmAMOzR1kz4osbptIDh5lrgWkEbTez4x-lB6GMS6aH6cZSVQEX1df67_IrUnDNOsmapTxJxrukVsfGm-OsX6pxIzmE0KsuRyGqZOe7vAslrY7r-1nZkXuL9fcpbMljvisA2jhnk0N0X_nWty5jmrXu8w8wFniz7rhD09vV8-JAcCaZLzsiYtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
جدی‌جدی ۲۰ سال از این قاب خاطره‌انگیز گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98134" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=GmSJHFJWg9Owgbxul-hD7wyk3O2xibskaNT-Q27ReCRf4rnXcTESsTajtqI5PKw7zmfD90_2X1iCOgPMmiLz1lxjGqcJCsYFC7z0Avv4OHYiyJfmQ4nw04sqnnKiBPZxiOJCqOqkUY8BsKqPe_Ud2gCYfYeuvA9Td3asuUQOIO8_tkX5jgj13pq4eY_20bOXpDo99Bc4cxN8rHJ2mLiylNQtA5jkGO5-DkkbTP8Zkja_CJ99BnuVRDuvnxLd1-H09Wq4O_NH9erOKWrTBiTpzGBxhYtoUGrUOkqAhy2OA-6R-m2fGslEBUIWuKBvptS7M2umZ9kG8grBwFnLdsTnsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=GmSJHFJWg9Owgbxul-hD7wyk3O2xibskaNT-Q27ReCRf4rnXcTESsTajtqI5PKw7zmfD90_2X1iCOgPMmiLz1lxjGqcJCsYFC7z0Avv4OHYiyJfmQ4nw04sqnnKiBPZxiOJCqOqkUY8BsKqPe_Ud2gCYfYeuvA9Td3asuUQOIO8_tkX5jgj13pq4eY_20bOXpDo99Bc4cxN8rHJ2mLiylNQtA5jkGO5-DkkbTP8Zkja_CJ99BnuVRDuvnxLd1-H09Wq4O_NH9erOKWrTBiTpzGBxhYtoUGrUOkqAhy2OA-6R-m2fGslEBUIWuKBvptS7M2umZ9kG8grBwFnLdsTnsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مکزیک یه زن و شوهر دعواشون شده بعد بازی که اینجوری مرد بیچاره افتاده خایه‌مالی
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98133" target="_blank">📅 10:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=N5YmfxFmv_4O0NSyAaei3q7GFvqoa0tnma0KBPzfxnJ1L9mLBVfWZS6CJyOKFhVMwPaU2-r3KoSz9KFbusX95In1fJOY59wCDVrpDQ2f63azyYohMuEl6y_tW2PXCAXRHJvrhRWWCG2Qh3p5I4hHVIRVB88F9isP1PM1R1dRkLgy_BtGR74cYi6zKKdCw25JivJA8veWEkLJ4N-l8bAeRXJq0i5NuKm2mdZPlkXneg58OGz4HcXlFo91uBmnc1MqTR_edMP6RDW4lZkx5FOgSEpr-7mAIZ4LPHVYyhffPGsphhX0k_PcFunDt_HTBNmXGCFaOKXKIO5idhQ34eUmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=N5YmfxFmv_4O0NSyAaei3q7GFvqoa0tnma0KBPzfxnJ1L9mLBVfWZS6CJyOKFhVMwPaU2-r3KoSz9KFbusX95In1fJOY59wCDVrpDQ2f63azyYohMuEl6y_tW2PXCAXRHJvrhRWWCG2Qh3p5I4hHVIRVB88F9isP1PM1R1dRkLgy_BtGR74cYi6zKKdCw25JivJA8veWEkLJ4N-l8bAeRXJq0i5NuKm2mdZPlkXneg58OGz4HcXlFo91uBmnc1MqTR_edMP6RDW4lZkx5FOgSEpr-7mAIZ4LPHVYyhffPGsphhX0k_PcFunDt_HTBNmXGCFaOKXKIO5idhQ34eUmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
ورژن فارسی آهنگ جام‌جهانی
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98132" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=cKMt_PWiUQZOrqNAVE95-VNa4OHOtXnkNhyHLtItzJBPS4SV0nT5Zmmqf7TJ1c2T3ucaPp5Lt1_VtwakKz0JWx-963cxTbtrpJFO18dsprLClVVGH-QEy5KrrSmyyvwbJEUmDUdD4Uq4RUtvbg6jeLi1gJR2NSi8flbO4FRjpUSou92_allASydbrBjPX63u2rQEB3jB8EXYuBD-eOllggWlF-vYBXFFZ6v2lHKMZVul6qcl0p_HRuSr2Mo_oqG3PP4H3s5Q6H0ltB20-GVmggU8PS81Qot2ZF86lqLCXLwFUSrFLiozGs9Pv04ezIxCmPNvOduyGlQvZHKkFpZpHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=cKMt_PWiUQZOrqNAVE95-VNa4OHOtXnkNhyHLtItzJBPS4SV0nT5Zmmqf7TJ1c2T3ucaPp5Lt1_VtwakKz0JWx-963cxTbtrpJFO18dsprLClVVGH-QEy5KrrSmyyvwbJEUmDUdD4Uq4RUtvbg6jeLi1gJR2NSi8flbO4FRjpUSou92_allASydbrBjPX63u2rQEB3jB8EXYuBD-eOllggWlF-vYBXFFZ6v2lHKMZVul6qcl0p_HRuSr2Mo_oqG3PP4H3s5Q6H0ltB20-GVmggU8PS81Qot2ZF86lqLCXLwFUSrFLiozGs9Pv04ezIxCmPNvOduyGlQvZHKkFpZpHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه بازی بعدی فرانسه و پاراگوئه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98131" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3536115386.mp4?token=hoLa95NOJRJt57NUSdmRQgNFdj_Xl6GNvp9qW17eTbJlOcdQCp1lTl-AKmPq8Tgtk1vzA6XzjQ9wMJYyZJ6tPhyhXaEaJZ12QTZ-Vhu5kHHBh0X7cifhF-2fxzU78d4SkLUXpxA0g_OltFnQaD8THByfnBt4XfKqQU2GDwtqiI1CG2PEhTsoUxyHIboF-QbbWnkp2PiWUR8wPtEta-LUeQ8xL_hPkNH5sOI09vjsPjA1HvxOr0MEiIg8JBih2r6rt4mCchDzwHJoNE8tv6Rqds78a9fUDCZUBy8g3QUiQhKIoYdSdhGfBS2np7BQE7Z83rbKBUS8YpyQvfSnEtgZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3536115386.mp4?token=hoLa95NOJRJt57NUSdmRQgNFdj_Xl6GNvp9qW17eTbJlOcdQCp1lTl-AKmPq8Tgtk1vzA6XzjQ9wMJYyZJ6tPhyhXaEaJZ12QTZ-Vhu5kHHBh0X7cifhF-2fxzU78d4SkLUXpxA0g_OltFnQaD8THByfnBt4XfKqQU2GDwtqiI1CG2PEhTsoUxyHIboF-QbbWnkp2PiWUR8wPtEta-LUeQ8xL_hPkNH5sOI09vjsPjA1HvxOr0MEiIg8JBih2r6rt4mCchDzwHJoNE8tv6Rqds78a9fUDCZUBy8g3QUiQhKIoYdSdhGfBS2np7BQE7Z83rbKBUS8YpyQvfSnEtgZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اگه کیلیان امباپه در یک کشور دیگه به دنیا بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98130" target="_blank">📅 09:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXtwgLKf0bR3uxyj48I9G9ZCdhs02BUKKQLFw8wpinMflQ53xAVsI0viyxvShUaY3XHYHWG5L7oeaSPdaxghNI8ar2lHhV11oBklGZ0BvubsBFcTTiDJ65wfwGwR5BcjoEs_8S_3Ku_Fiav0xHLmUIVK5r9nDumv8SXXCTDMhNQhlcWYtRf4yAKHMFO4nWq2vpoBhd8GOl-1-S-BWGlkDqzs1zDFdA-aS0Spuoj0BnM8wJ2H4rP3ZzSc3niQsAP8lxrv9oqMHSQLZAG_9_-t0Ki5xekD_oC5lbn7iwtnh6DEYPKP7EpeSHYwuextEQTW_C7PpWOL24mJTAdvlBszyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
ولی چه کیری خورد این بشر؛ تو چند ساعت هم تیم ملی کشورش از جام‌جهانی حذف شد هم جادو جنبلاش اشتباه در اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98129" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeKjbdKiPdjEKW3BXL9ZNZJZ_acxvSRcfgSaACqog_uc_lAQLAspbf5CrTiLcFvlPePr76I-_yiHNsnzYp7peU04J2lzZUMSIgDyC9CJWU9wK9eeOM2pjh9eC1iE3z05C383iBajYHAAI7NgC2m8g_vUumipO-A16yyHs2jh_he1rX21kXHcDTDBMrQeyEpjiW-_2-MkO1wfY78GUwo2fByEadMF4WL5304M1FV3CcgL6PL7sXnuQ9AsBNaorUAzfixNgUR4vsocLRw7ahe0_H2-oFWrmP0DWR2sbNtUCYMPHQfl0GtZ6c-Mbxu76yykm77yNuhep8ZXz8i5MGQaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات ⅛نهایی جام‌جهانی
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
پاراگوئه
🇵🇾
🗓
يکشنبه
۱۴ تیر ساعت
00:30
🇳🇴
نروژ
🆚
برزیل
🇧🇷
🗓
يکشنبه
۱۴ تیر ساعت 23
:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22
:30
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19
:30
🇨🇴
کلمبیا
🆚
سوئیس
🇨🇭
🗓
سه‌شنبه 16 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98127" target="_blank">📅 07:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUpPqx-8FFpRHvfQPN3iZZcssZY81ei_-h7zhk54fj08B_F2fNH-cF7crN8b4sqck2KT9xUWsnzKqStGjMRQCSIN509YmGod8MpeViIAH671aeCEfEO9dvnn5vqfjfxAR2QvIwGFgykeXkmD64NzTqTs-mAkHks7tLYZsRz-bAcV9KveBdgGxjkmCt4idaZNBIlZId6eZp5oyw0zsvb_HiaMfA7FzOn7CGav5f7BI7f98zi9Z08br3Kp-0c1AkWs2hfSTI0-VV2TeMlVrDBI3TwCkZiflLCe9CW7JGiRbGV01VhTEq1TwReME1_AaakM-SmT3HJwrnwGReSXOoLZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98126" target="_blank">📅 06:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کیروش کون سفید پشت هم داره از کون میاره</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98125" target="_blank">📅 06:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98124" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کلمبیا دومییییییییی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98123" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98122" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDPA0PXkllNvSgdW0fyuYBNb9DCpVohcyNYGHzCV9i4dHxrGcGUVx_II3w_A9hTh8u940fQ6WKyMXbN3WGG74gKknC8ezv2RlU19-whAXpvQcGjSPHQi-arfQkQ6rY6OLI3nMI401YRxz20lFRAXlYXRvQW5PJ63IPdRPPBg2G1DKoHbtQooHXQoEFHxl9rUzhDkUSOJ4Ah37Q7-R9IEGhOtJFh_T49ga9GL2ouW1h7GA9rNyj0N3xwxLDhreAGmgiNuibIzvoTk1sycpRUJuLZX7_D8vdPJ1zvHUVbrCyBJD4MGjZ6c_X5Yd0a_uxY9Y_k0qPFlQr2BN6qJC7QFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دریبل‌های موفق این بزرگوار: 2 از 2
🔹
نیمار: 0 دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98121" target="_blank">📅 06:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djfXPEZNV7rC-cGnECHs4rzewtlAzaBbUScfbfqef0SDWRyhJmgtS016fz80jYW1bGu9o-aHHWniLiCD801ruXtVKSwhKtCrn3QAcplkBHx-HAEUjtQUQfY2rZQKoUEmYexJtZWqDUW8dRYFzQHXGXA1evhu86WgEbEhLWSwIFkaItJM3oZdb2IdyYDPJ6Px_jc2_e3EjpBCEJHQxZGhGYpX6fONCQ7XF8sFPcLKqjrG-KCS6i8Z093E-h4di9NMAOgD6i9lnbYVV3mn_57GzCHKYVUobu7y1KZ3EBhjBCcOErgWH33jJPtJtjznpUAxVFkLqII8G7JNenvrv9dVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خامس مصدوم شد و بین دو نیمه تعویض شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98120" target="_blank">📅 06:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98119" target="_blank">📅 06:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98118" target="_blank">📅 05:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Xp8_eIqU6Ez9TqHDo5lV9pVNYdGixDCaG8-ZnhTfwYYFxDipxUizpuKPD_DlXnBZpxWpC72qpjbb-JV8Tds39yTIcWdA8auvGOn5gfz9VGyoPrw7WpCliwKMESosJTIRf7PyzhOD95rk46A3ji3RTwdYuXQeriS6YREROg0lRN4g42wI0Rtdri5JirhV5j908nTxzl18NK_PwQ2BzbGzreUWV2Mm-aRCYAciIbWXutKLRcmFn5aEGUlywd5i-heS0ZJBEkqqWCBIncLOo5TXBobSbpL4K2mawk0EBFTWvdIISstuOxnSUaK5MmSN5hGNFPTJiCD15w1IF_8johPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین بازیکن آرژانتین در جام جهانی خولیان آلوارز هستش که در کنار مرحوم لائوتارو مارتینز رسما آرژانتین رو بدون نوکِ قدر کردن.
این درحالیه که مهاجم نوک اکثر تیم‌های مدعی مثل انگلیس، فرانسه و پرتغال نقطه قوتششون هستش
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98117" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3mkYJWJ0SOIbz8WF--QlsXNkY7C-SPdTawd094pIWV2d-PwjcxBLhV9UYKeV0TOuH-07YHyb6bXfa1jEzuUYJnZyetbTTlFwT8EvmyA7mCQ5FEAetp_wgUGhNGC3OlPNWOv4DSE3PswKpR7RL0i_4fNqOvpYYXLedLv9H3XnFlUSQupTBQEfa-58IaJdfCoOyFOw6NhhR0QActcVYWC_C7EkX_Gas02IfqJ_xzgMePANB5KVmf4XBkwrgcbsrIy0DOa6Ob2tEZrsek3jndJiiKuMpZAvexRLM4JHU5UNeTxojnsrtM3-BL_TG62vZqTFFSij9rvFiIjGJT5f7_aIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتونلا هم اومده بود ورزشگاه که شوهرشو تشویق کنه
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98116" target="_blank">📅 05:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98115" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کلمبیا اولیو فرو کردددددددد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98114" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شروع بازی کلمبیا - غنا
🔥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98113" target="_blank">📅 05:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsdwKZwid9UAKF4THbvKsgbmbmMjb1q3k1j2Lxt58qwWPaQEmtJwm91UrnpNqLKBOQ11G24gKkPjcNjIcHj23NXcNZouV0biFAzvwaHsheM9x25-tvekDaixYSd8NQcY2m-S681JCylp2cSK67ikCAOr0Qqnl3h7WQuGyD2j6uL7Oi4Gvs-FubKmayT41CTupKK3hnQxmmTBMVPaJFX3DUyoCwaCjW37dX08o-kuRRJ52fUCawGNCuFfTfE9oe4FXqY6qpfZ_oS5z416t4C9uHjAJUh2CrFd41TdkopB_fksr_IyqkNNWJI4gFxaypmMiANuD3aYwfrdAhDN6G2HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🔥
🏆
لیونل مسی، اسطوره فوتبال، اولین بازیکنی است که در تاریخ جام جهانی، مقابل 14 کشور مختلف گلزنی کرده است.
‏ـــــ کیپ ورد
🇨🇻
‏ـــــ اردن
🇯🇴
‏ـــــ اتریش
🇦🇹
‏ـــــ الجزایر
🇩🇿
‏ـــــ فرانسه
🇫🇷
‏ـــــ کرواسی
🇭🇷
‏ـــــ هلند
🇳🇱
‏ـــــ استرالیا
🇦🇺
‏ـــــ مکزیک
🇲🇽
‏ـــــ عربستان سعودی
🇸🇦
‏ـــــ نیجریه
🇳🇬
‏ـــــ ایران
🇮🇷
‏ـــــ بوسنی و هرزگوین
🇧🇦
‏ـــــ صربستان
🇷🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98112" target="_blank">📅 04:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOrl_CP3s9DOscrupUbELT1hSaR6f8HP_5su5M2_vxilrm_Evgm1TxjEh8YJIRB3HEWb2oplmdU_Pq3pNiTsuKTzQjsI-v5eOTAMbsMVYIGAfjCS5asNClBNDzQJkwnAUOiFaCxomtvqLbWCYwrbLLHcFpQiALPLqRH0RQxcynSzkn28zWma2YnpUZCwm1T1qdqe1x_p_1Z3i9wmBMQiT7LY9sHdiiO9hKmw48D0_Pdh5-qq_qa8Yn61p3ExM63DNA2pNxspeRV9dUjqUUI-pC107VjBRl3cMZgaD-oeysaBGiwOijU6ybdI8Nrnr3dUNP1LrQqloopcrDiCxTawDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📱
مسی همین الان گل زد. فکر نمی‌کنم تو بتونی کفش طلایی رو ببری، رفیق.
هالند پاسخ داد: "درسته"
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98111" target="_blank">📅 04:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBrWkqfz37EFI5FhWvghwb5ovQKWE_jg-M5NJvnGkDctqJ4hu8gFZwY3EQngIX-f4VRHHtQuuoOvHToHzpWN07xYFHDwtl2i1ROxXgt5vzXrt3djKeY_JRnMl-H2_bRGaLZrCedHyZfUn-BwuJNwwJMzLH2r66k6TkZrB1LfC2khWtB-B717t4RGfwRFn-S8_sf2-eMhIwqCfqxa8CgyJqc3tXZ0FXh84MloGRnTfzwpAlAL-3yt3awuOH1bxpSZpXZdif5h1BVAgCnx7GBvCHWVZ1H7Kq0X2kMoWG7acH_1m_AbXi4IY-huh2ee1FywDc8NPgjNGDN0WZYhgIWnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
🎙
لیونل مسی:  ‏ ما دیدیم که تیم کیپ ورد در برابر اسپانیا و اروگوئه چه عملکردی داشت.  ‏می‌دانستیم که این مسابقه سخت خواهد بود، هیچ حریفی در مراحل حذفی آسان نیست.  ‏گاهی اوقات مردم ارزش بعضی از تیم‌ها را دست‌کم می‌گیرند، اما ما مطمئن بودیم که این مسابقه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98110" target="_blank">📅 04:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgKQWoeA2lHs5F_5_Au0izl21_V1VELg4iV0mg5NDhCto_hGvrY2g7sp1387KZhBwHGjn4wi8cjWeP8qupG-f4DsP7SmfDgozoKmc7X_rxImBdF8p593NFaVTkXPdmfDjuv5pCRZaufe-ZP89yHjSllJQdoB9KfKEsRh23j5XatYiOy6rUFQVTX061Ej87hudv2Fa9p8emDlwFH5w56uH1v7lkH1bDSnaJgu5K10up8B1VWdLWhCrv2_JoCRAHYRWTCUBLAQNGRhJOaoJiz3dCP_HCWa4LWg3v1ruyUC_1J1BrgzF6bfRUKoJyAW4uzLZ0p9Vvfljkgph_-upicX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
لیونل‌مسی برای چهاردهمین بار جایزه بهترین بازیکن زمین جام‌جهانی را کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98109" target="_blank">📅 04:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekuw5xsRa-iqxj2HMWrPcDw_0soVq9QOaKmZ6A_bQN3qYrXfd-PBbHteiZjQcGCXe84gKaWi73N9WPvZfByvrzxcmCvyiiCH6T25JufssPFwBFIHL7bt9eKtjuIFarw9mA_tLpqecrpCOODb1yS1o7t5q3beFliF1jfD21mgruviw1S6mzR40oFuCr1tfrntl7HTzo0_dbRKjWZXszu6z4nKwh-wzFyTcH-ZLk2PCj3faEjFkGQcvjltEXkt4AYz8NnPKS9l2-GPoZPCxMyG1xj5HAP92pFLUln0Trw7qyd7Y_KlM3nBqD3E7ryij5bMR1fWRov8Z16yTt15FuKvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98108" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9ejCIGM9p9cSFCn6bfdiGXZ5Rstuhy-6S-lTWFbMwSwvMPEEeCqzw5tyAhWJdjRIK4aG4VfzpP7RqxZiO_pLj1f2K8ZKOZ7RgonwH3-VxJMhs1aYEIZMy-FjaeE0FYGygyHZa30rvsaQOvhVbvKYYfJFjAsxLSew_rBbe0DxpuuIOC5bzNQBx8hlVZde7Cj7-DgdYwEclnIMBBj7On-q1ROr4wEXj-gDYIibYBhMh10KIvnvVaXAByeHH5Gs3UZBvga4oTz4lkeGawQiDxn8fG2oaUzx2G--78qGUiOtLsUZxJG4bPOHpT-kyaoyKOCIP61c89ZPkYmPUk3X5NDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاتوووووووووووو
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98107" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP5WWwfE_89ijb28OngU-uPnMUFSE9dzTwq0pyZNx9xtgf_jQ7S324d6kPS0vLlCvHT2Nfcy2w3OHA45hr2DxGYMaZKONrrDeSU0btitK1ZmWtTvpNp1MChIzFmkh0niOSp0exnRcwt39UXXiRqEIfxycobNFUYkRTXhGI9lEOAkByyYR56aZD37Nrxwft_FgZPF1LjJJ58_CnmTGGvDdwoTDF93tpKFxAN0M6i2QSCFenNkEjmw158b0S7Dil2tBIxDCP3mHs7L9hyyoZ2ceYyXNoXL2Ntuw-BgWtiRrJnOyFo3qtD54oAahm7TvA0YlpGh_oIqqWypxrcNywCgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار خلقت در ۳۹ سالگی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98106" target="_blank">📅 04:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🎙
🇦🇷
🇨🇻
لیونل اسکالونی:
«می‌خواهم به حریف خود تبریک بگویم، آن‌ها امروز ثابت کردند که یک تیم بزرگ هستند. وقتی می‌گوییم که در جام جهانی بازی‌های آسانی وجود ندارد، این واقعیت دارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98105" target="_blank">📅 04:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_VbzhUDkuIeLM7ht-lj39uZz0ROvwXeVbLh0A1gHJm6S2apFv2JxOF2RpCUzXUPYbbvgRhugWwjwLKz9H79ULWxLBZI5XHE6RTyyJolk205hHImOrutxzGVVES5WeHiIV7qgloLZnzaqc_BNK6_eWQgPLRnJ_zVAyZ_XKGb8xMWEn4hyQhF_Me39X7x99kB7w3-iFWHCDAEnNtmjAeuJPRmweoDZtSh6u6qP2O4l6CE7qJjWafhy4Hfjz2j4th3oGhffP8_ox-bUT_tl5WoxicM3sqj9Zo8VvYZ3vdVtOL0MyhPwZejNToTyPskgSAvUvcSjc3ZwYm0zyyMjyJzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98104" target="_blank">📅 04:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTAnSbrxUj-NABfceo3i9xAZizEnVN8qLI8Fe6xBaTkMCp-pKfx4SO2mH5rIkZcd3IDCa-RilTZqqqKg8O5NIbsthdKAEbDdj-uOZvDjllkxdgKa5-lrF5q-8onXpiTSUyaZefm5ywwDGxfit_FXjPp8vMRKOXMFnnaMsunQwOi2PEVJejiwTfH1wTsysNBziLj0L68IJG7LMxsjTWrXDJrGe18cwl_qn6S4DhynYuCop5t18EO2j3GATF7uLODOKYFRqVQdBUxyzs_cKJ9qjRCiWW0nqJikebTz_H9VZIe6YaBprDjk024p8VtOcVMkz0vUy5UclNy-rI_sU20-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🇦🇷
#فکت
؛ آرژانتین (از جمله در ضربات پنالتی) در ۱۰ از ۱۲ مسابقه‌ای که در جام جهانی به وقت‌های اضافه کشیده شد، پیروز شد (۴ برد مستقیم و ۶ برد در ضربات پنالتی).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98103" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg2pS9RfWIYiv_AT1YjRZqQiAxGEhSKfmr9P0lQQ3rog4HvcozcoPWB0dK93cATnN7dQ-8zPJOUDxWM-9r3Oe2095GNgQZj4duXDERSNpPOu7Tqm-vAjoaO2v82QJKXVM9M17Jsd1_hY_kJ4HBA5b5BPveIrG-NW0yYn0ZUsakaSZ-s8pa12mYR_Drz-OHsEsy5amnhoq58CaW2NIQQO4MdrGkqbbfzdxZQSeYjUZ5UR9lmsdjd7OkIewaPKiztJMJDzucGyMJe3YN_QV1P7b-peav39hs2ygZZs_8GcXulvmyT_LZABSPWqeLVguSAlY-esEw1EbA_wR6FfHwKQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
گلر کیپ‌ورد مقابل آرژانتین
🇦🇷
|
✅
— 8 دفع توپ
✅
— 5 دفع توپ از داخل محوطه جریمه
✅
— 3 دفع توپ خارج از محوطه جریمه
✅
— 1 دریبل موفق
✅
— 8 پاس بلند موفق
✅
— امتیاز 8.4 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98102" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h50xCO0ZlxooV6-svYtMWBvQxBBujfs4gYjOLu1qrMly9xzRSIVQ81i56M0XUXYXb-s3F263__sizjLjbhx3748QXxn4TKV3urYrmdatq0UVjEp8k_-RL_B5NYfA0Q8jOAuOkRj93xtfyb4krLidLY2e8yBpTFtAhhyqCn44dakgCcYPWZIFrPTWykPP0bUX7PJKPg2cyC-k5Af3jADX5Wejwhz-C5evLVTclado5HSQBiddlrbF1ksEMhW_z4hPvmpTxZoANCGacBlKDQ308n7f_mZ_iKRuZKNFO4j5lygq9ir4T5yZseB8Ohpepi_hu_bQr9pf_bQJHiscdbaMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
📊
مسی در مقابل تیم کیپ ورد
✅
— 1 گل
✅
— 4 پاس منجر به موقعیت گلزنی
✅
— 1 پاس منجر به گل قطعی
✅
— 6 شوت به سمت دروازه
✅
— 2 دریبل موفق
✅
— 8 نبرد موفق
✅
— 5 بار دریافت خطا
✅
— 33 پاس موفق
✅
— امتیاز 9.5 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98099" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خوب اقای وزینای عزیز الان ما بخوابیم یا سر کار بریم
کیرم
دهنت تموم برنامه هامو بهم زدی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98098" target="_blank">📅 04:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6A8QmCnZDtjevG3Aj4x15AdgLNIJ8zBx7mNDy0uPiRcIe_64lV_3GJg3WxNu5rClO05z69IG9O6Rw8oSy2nWv_qdQ--0rwmKqwXWfjTEWgriO5bYnHYJ_ThOJoUwyRPKKP-N1CEvU4sexw8CQX1Cugn1sMHgjcjO4khNDSjLbU_JHk72AnjMh5t8HxQyijqsD9idBbtQLhwM7XWV_9rj3UAGtu_5vWNXWWMAqYI9A8OzzqJHiYuCEigRout09iEHQSqn5u7ES0ZD6JvoZYd7LZ8y9t7otQBnldqMdNsSv8Rw0Omn9HtOX9dNjIphUHEIIp1N7YdXiJMCBRMsggrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک‌های لیونل مسی بعد از برد مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98097" target="_blank">📅 04:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD7SWwWj2SsnjGK6l7PLNgStEmImxLsemQpvXJ2ijTKUY3Sc-Q8JR4fHYqNvD83KASoXfS2Sf8chvIOI8EvrzY2nH3O67O9ohOHCEMtvPBbeGwvUiS5wW0lEP1lbweg3wLG7-XEyK1n4EcZzWQYcVCaJEJIyuYuj-pJ2unE1dyXUkuiM_RFZB6yJ0udOa8s0F8LST4TCNl-M8f16WJhzsNc_USC8_XXakW96B0AwPQQJ8snYeOitzTkiA4PGbdD9sHZh_JChK0dqEN9eVILc6E_f-GnUw0h2JJvaslBDgRgGRxJyMteP9hCQ8uNhrJYpMHCDNcDWmyV6f522KZbPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ‌ورد سربلند ترین بازنده جام‌جهانی...
تا لحظه آخر جلوی مدعیای قهرمانی تو 90 دقیقه باخت ندادن و تو اولین دوره حضورشون در جام‌جهانی شگفتی ساز شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98096" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98095" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peqm50s1OG1XF_AHLzCrFg5wcMSqH0xUzfLgNqe20PoDE1Kk_Z-khDP-LUeivGZ9p6EiEDvxRwib_ru_a_fgc5njio-Qg-nCXj6FTuwNsUecRjEEpI0HDXHQReWlhofbxNhhG8QiZbPqD-0DrmUVAImDA4WvKzNoWfA8DZoGDia6_IRox7hcQVhL0gyCuAcuLRwa7AAB9uHfAjBoSKi6xMkaPJD7Q-UBWVd0mJyR-98siSMfbKTzNpknMo_1i0x-zM-rdyPQRynk_mtfDqokWTIEBnKzY4WzjY9hm4mqUD4kA6dwgVmfQogA_qi1oFhQA5J4ptrmt3er3GOPomd-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98094" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxAc-2BRrSYgVTppVe1AVAmK97zonCHhcxnwLgDgQwADyijydtjon1Bp-z9Oa9qy26oD7DIDmF-8GBlrS7BaERskF67vyD9niXkQlr-oCyMxbl-APEiMn19EUoFJ7g_yKvMcDQra5U6hzvXzVasSL0xVYAximJZpbpw1Ln9J1BbRPBkrq1YFszXKomMyQjBysEpjM1BbVX_TK90LwqMKu8cWcMmRZSs2BQzGO2YFxzf2_ot2Mp7LhnTg7P_B2iOE10SJC-0lJt1x94YPlHuajFzUNtg4sP0vr9tz0fdb7R28uDHURNe-XPr3uVYhb6BmjGeeOE_idtHDF8LjMVITJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98093" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انگار این بازی خدا میخواست مسی رو بکنه
😂</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98092" target="_blank">📅 04:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR3YssNqUdRPRdCKRUyw102hQleXx9281o7TiCnXb5tDWEoZL4T-WBU-TycyXtDzUOwrADCZuDirHJMRzq74HqpsjM9m7LTPQOV-ewj9n5DkPCidP5M4yoQXWchff3ItmNhe-Qclb7i6Gwr1atwR2V5fu45lIzoxe0I6NH19sxbDv0BTA2LcqPVVhXs_9A27CNZJqrSzs3zQn1wPx5poDTtnRf-hkWJ-aic9nIrcGO0_o2OQt4mebs7_xwZtncwEwp0JDkA9qBZUWb4jCMenACws9YEDfYr2dxRl6xKckdpadfRVf6ON6QfoHHqQnqZWGe85DxBHwsVA7ZeebYylIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98091" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با اختلاااااااااف بهترین بازی جام جهانی ۲۰۲۶ رو دیدیم و یک دقیقه سکوت برای اونایکه خوابیدن و گفتن ارژانتین به راحتی صعود میکنه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98090" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
عصام‌شوالی گزارشگر بین‌اسپورت: از مدیر شبکه میخوام هفت روز بهم استراحت بده تا این بازیو هضم کنم</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98089" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=q_AShaBIPflLU0NhNKOMEkgFNXzKBYQ2vINF9sBaqyN3oWPF22639UpAvbcQ_ErR0v3-4yoJCZAWW_77V9bAE4YRp39A0yAsWINahBTyT-hPeY4jRRaKDbFupbLRNsll-6Q83LJBe07r15Tl40gJJd9H7XDWv8z_qbvwGsNvELzIzd2IfyVeeFaBxiDhCwArE2LVWXBAdDdOTjXpKMi69cwuSAmg9xQ_zsxyPU3KN8ECCy-f4TXvfi2sGE7YFpmZBOYMQLXQTa5tMi_eTZNaQ-rHA1MA-GgrBQpj9CvYqofYzPoo_WD_UzRUmxmPb2d0Z1UOhf-A3YUj4fGKFbfegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=q_AShaBIPflLU0NhNKOMEkgFNXzKBYQ2vINF9sBaqyN3oWPF22639UpAvbcQ_ErR0v3-4yoJCZAWW_77V9bAE4YRp39A0yAsWINahBTyT-hPeY4jRRaKDbFupbLRNsll-6Q83LJBe07r15Tl40gJJd9H7XDWv8z_qbvwGsNvELzIzd2IfyVeeFaBxiDhCwArE2LVWXBAdDdOTjXpKMi69cwuSAmg9xQ_zsxyPU3KN8ECCy-f4TXvfi2sGE7YFpmZBOYMQLXQTa5tMi_eTZNaQ-rHA1MA-GgrBQpj9CvYqofYzPoo_WD_UzRUmxmPb2d0Z1UOhf-A3YUj4fGKFbfegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل رومرو به کیپ‌ورد با پاس گل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98084" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کیپ‌ورد خیمه زدهههههه
😐</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98082" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98080" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwzm4ZbcpqnJQgpFtEUsJnni_i7UGseGN17zmS89E-u-YqE4GVrOv1hegzlf0moo_aCkZgxsSr0Wx1lvh7TGLv786lrppuZ9iAzZniOZfLK1m6gGdu0w1KIFeJcn8RptjeVEsOLGZHci3Hj_DKNVdUBHxzBhTxWQe8E_-DeIWv2CwLdd6hvxoburmV-goA0BCdxz8EJHW7uKreKBBndJFgyNLCie9WwARqs4Z23VQZvMbhaDGFReDERC1qBgxTonjze10yZK3-DsMfOHXlZhts7Q203syUYTY8lwTdDV6keY5C7aj5chU-80Dti88MUCLNjfnA3_xujTa38MMDxTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.  • اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98079" target="_blank">📅 04:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مارتینزززززز چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98078" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0jFngoHC2OdZV3Yjauf655A4boOCmKjE5dYAQSFA81yuaW5PT33TJ0kkO7QX3ir-wQjgEepJuKHKQgfVJcsr9-ePYJBJzN3thqArGU0QgN1EiaIr7PzIKdwQ-5FbygBXN-3tiYA2CNaQCw-yAECFrvLcdNRRngQlhsDY61eqAMlwUqLxQLNuSAdOTEuVyZCPazRZk4-703Er9uz7b63Ivh87UXPrc92eb8Pp-mxciusv-XIKwCZ4BEI6OCin7Fu5vhFpc3PqhCgzT4jIKrtGIfNDWv3Led0KdmmqefDB7pk9Wl42vgO0iTKQOiIYwSpk43-pF8YHKoA08yONzQspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.
• اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98075" target="_blank">📅 04:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسکالونی داشت گریه میکرد
😐
😐
😐
😂</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98074" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاس‌گل از اسطوووووووره
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98073" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوووووووم آرژانتینننننننننننن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98071" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رومرو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98070" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگگلگلگلگلگلگلگلگلگلگلگللل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98069" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98067">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رومرروووووووو
🔥
🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98067" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98066">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جاننننننننننن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98066" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98064" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=fnbKVge5iC9zmMruN6YMR1DnmG9r_wP7Jwq2KaGsBQ2CAl4vYN7IS4z_djPbnUpyf-GeQfaTxSu577jjDCaHiR4kZD_XzzoMPTOW03neiyK4o-r_sH8QmY6u2M-b_ye6lPPn_y2sTIuqaQxC9HClufwsmzwfxt_45igJkKfc54AztQYZ0Xs5Di4Vhi5WvRV0-L5bH4YAVg5sbkKFUAc-1xnfLH-aBLPKj2WL4UJu-DeuxsE0FVYdkSkGPRX_V4rHKH_LuJuMAUOYl_VikGNudBE09zuw4yCHjbIbA3QaR5kXXlgDljptrH9zBg-XZH-nNHJ4G15BG9l3ydak3I3N-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=fnbKVge5iC9zmMruN6YMR1DnmG9r_wP7Jwq2KaGsBQ2CAl4vYN7IS4z_djPbnUpyf-GeQfaTxSu577jjDCaHiR4kZD_XzzoMPTOW03neiyK4o-r_sH8QmY6u2M-b_ye6lPPn_y2sTIuqaQxC9HClufwsmzwfxt_45igJkKfc54AztQYZ0Xs5Di4Vhi5WvRV0-L5bH4YAVg5sbkKFUAc-1xnfLH-aBLPKj2WL4UJu-DeuxsE0FVYdkSkGPRX_V4rHKH_LuJuMAUOYl_VikGNudBE09zuw4yCHjbIbA3QaR5kXXlgDljptrH9zBg-XZH-nNHJ4G15BG9l3ydak3I3N-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید لاشی به سوپر گل کیپ‌ورد خداست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98063" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyYuSXl9bxtSn8PkVSkM-CKdIEHT5wTYBWaSyqfs9LlYN8btrxI45pjZ2Wpak9I8rLtDXkEgkFf68ovYulKcuttL8OGq-RGKRG_fkt_3P8JxvLQQCDfGbOBfZ-4VKzy7qr417pvG0gpqw5vWpl2KmApZm7-LOXqc8WobiyEPELeGAReQFdg2B6RdeetCIAU5ldXLu3GK5phzDigTLaRYOWu3UrTaZjZERl0czUg02JlPvaqG8Ko5yq8b_Z8X5HQQSxRQlxb6jjEId36CVnCDJPHMoqDa7TiR_bHZRVtPgVNN0WcCUsWE6Mcd0gLfmj90X2RP6Fbwk5ThlScgfregKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرررررررررررررررح</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98062" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98056">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سرمربی کیپ‌ورد رو بیاریم جای قلعه‌نویی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98056" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98055">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینجوری که بازیکنای کیپ‌ورد جلو آرژانتین پاسکاری میکنن تو خود بازی فیفا هم نمیشه
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98055" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98054">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وقت اضافه اول تموم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98054" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/182721537d.mp4?token=cnHolsY4vnboQIi4UZN-VNY8cIFPx0JkDRfUPyDCYR-UnJZJ5Jl3EAIRcYMXgFMUCF-aPDTuhpgZdk21yth0WZePYXEaEuavGoSRwsXxIN55gpGmLpDRFbZSrdwNvV2faoad5VnXmm4k9C1eSChSLbpQdRD6YN1gYEt8vn7BGwyEGdPP8lf5K7Q2hvYgsPV0bdHVsXKhezYcXUnIT88VMPGY9-T5qfR4jLFovABLvWKNzzkVbWlHVjKxvoxjaYhWoO3kpc2ODYdNznwcYyGFWQqPhlx4lsPiW-OeCOVhLTOf38NAuDfDGqsqiRK9-dD9nG-Ch_izF34QtHX4fA1nZBaMYcrqlzuV7Cv1rvu90oHDI-yhSaqbLzQFTrgYLEpToojYD3432jcTYk9WA9KNkgNnydUdF5Lgk5fmfY3Q4WTyc8stlfxorbURXVuM-oVYrzHP27DFj5aRiwDcduva-4-Rk04H_18mMfwXv83ZvHVaEcQS4PY_99Io11RFkSnY2__CO9rA3HE8omFXNeBmPdXjBpoKV--3kT9-mWjWT9rXvJHnrFNsmNFEWrQ00PjRsGh_c56VbjzFn9Q294zpniZy5KRNR1SHxz1qcE-mRRfLFFoji4LtQzFp-Bl2-6iIyZPyrrcvyN67xJRUTwSNwFaiNk-BiIE_XzJapBFZDFI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/182721537d.mp4?token=cnHolsY4vnboQIi4UZN-VNY8cIFPx0JkDRfUPyDCYR-UnJZJ5Jl3EAIRcYMXgFMUCF-aPDTuhpgZdk21yth0WZePYXEaEuavGoSRwsXxIN55gpGmLpDRFbZSrdwNvV2faoad5VnXmm4k9C1eSChSLbpQdRD6YN1gYEt8vn7BGwyEGdPP8lf5K7Q2hvYgsPV0bdHVsXKhezYcXUnIT88VMPGY9-T5qfR4jLFovABLvWKNzzkVbWlHVjKxvoxjaYhWoO3kpc2ODYdNznwcYyGFWQqPhlx4lsPiW-OeCOVhLTOf38NAuDfDGqsqiRK9-dD9nG-Ch_izF34QtHX4fA1nZBaMYcrqlzuV7Cv1rvu90oHDI-yhSaqbLzQFTrgYLEpToojYD3432jcTYk9WA9KNkgNnydUdF5Lgk5fmfY3Q4WTyc8stlfxorbURXVuM-oVYrzHP27DFj5aRiwDcduva-4-Rk04H_18mMfwXv83ZvHVaEcQS4PY_99Io11RFkSnY2__CO9rA3HE8omFXNeBmPdXjBpoKV--3kT9-mWjWT9rXvJHnrFNsmNFEWrQ00PjRsGh_c56VbjzFn9Q294zpniZy5KRNR1SHxz1qcE-mRRfLFFoji4LtQzFp-Bl2-6iIyZPyrrcvyN67xJRUTwSNwFaiNk-BiIE_XzJapBFZDFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل استثنایی کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98048" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پشماش ریخته از گل خودش</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98042" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چه گلی زدن
😐</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98041" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98040" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وااای</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98039" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کیپ ورد زد پشمام
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98038" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98036">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98036" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfPy7nNsLWnGY_lrErAv6fEYI95vszOIYGzL2rIVywoDNE_MYpCnQrLeWKqzpCBrXNwbUzQvOofGiJ2OGtkKFaXw8qja20gxPOscAAEVTudQ3BdnLV6HpCS_Q09-hCQe7o50W43mqqnmEpF-LqCtB7iIrQdy24f-DQ-yXIikLvxkaz2aRQJEzOfmDWKPtBPSbD3mXalBE-tr9qD3O2ikZam_mT0S7FAIJ-HFsjADkQwnPEIMl4YQ29e1R9IHFA_NujZzm-1I8tN_KMonCLcx2lWeQ8kNPEMCYUGHQ9thkqE6BNOQ5STEKml-Arkn-UzJ6zMhZ7qI1F0wRKaN4HWbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWLEhZ5C3LD-G65-ahb18REidWz-ovao0xarKbKKzTpfW4310psBZFsdSHjDDfDyCWFTFJuohOcySUfJPcJwkQmUDTHBtCBZXWa6uI3dzuALL0bGXaaYdI_zBIXRfWfCLSaqsA3UjwXfCtaKFL2Stj5W_FPjkilmmZmc8Q38H_-N3VhqJ4qqDA202Kv8Qdx6438g6PuiQXOvheZC2O_NUKOtXLqq0s054Subnt8HtO1brILVVGuBx-uftOmn1Ea7wOsh4xqGCVbX5wDtTxBRerq5HE0bSFDbw38xAMclIzuVlTEs5K0SsE0xx7EZy5ndxmY44g1sncecJV1rRbCxwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇬🇭
ترکیب رسمی کلمبیا
⚽️
غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98034" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بازم خطری شدن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98033" target="_blank">📅 03:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78229061b8.mp4?token=HUjHieOu4ZtEyCU0akxGCx9AKD09hTQcmLwvNc0QSEDw-vo-AJSDlTQhT00RV5HxiaDMZ8iNeI3WE6B-p53Y9j_k4oa531IRsBrBcKxdy6UQlo1WzMiHauvxVSzJr2-0HuIvkwXmn-TzWhKwzaSHblioZzCwJQHBsTRC1-YdbOHcL0dxHF-zP1OCWFgMvYSIYo5RVpXCgHYfWXZu495L9fkQmq4mM3tXt506ymAZrhEj5LuVfJ2NSUfFecyvMeV4XstWF5Uo1Gxbyf-kXr3t90jtrZlvZDqlnmvyDS_4M_zEiNVTFUaHnjy7Ov8vzbbA9XfGW5uujsfwh23D9QwPhrNAxXKRAZ8kqapPp3M8JI-0g0R49h-bMITNqUOcMrBFCiEv3QU8THjfPGecBJj7KgJJHlVIkNNryfT9TdBDW1GcbJimNePY9_01SKFs6n-Z2m74x5v9Ty-hoE3ZU_M-3F6UaWEMPHgovFQ0MeYNCDEGJiu3a4OHjtsXLJh9PE6--0k6x_zNu3DAVfWhHrV5yt14_HE4NiRch4DqDFD1j-jTokA2Z7qsjm6lF8ryACs5KSgGkqKWGnwKYl9HqrflbXHc62bkuf0tRaeo8w7-foDH4oTqBcfK0o7ey47w9cOps5DySBWQfqBOj3svJjO1olfbT_FCr1Kb_hh6iCz2y2o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78229061b8.mp4?token=HUjHieOu4ZtEyCU0akxGCx9AKD09hTQcmLwvNc0QSEDw-vo-AJSDlTQhT00RV5HxiaDMZ8iNeI3WE6B-p53Y9j_k4oa531IRsBrBcKxdy6UQlo1WzMiHauvxVSzJr2-0HuIvkwXmn-TzWhKwzaSHblioZzCwJQHBsTRC1-YdbOHcL0dxHF-zP1OCWFgMvYSIYo5RVpXCgHYfWXZu495L9fkQmq4mM3tXt506ymAZrhEj5LuVfJ2NSUfFecyvMeV4XstWF5Uo1Gxbyf-kXr3t90jtrZlvZDqlnmvyDS_4M_zEiNVTFUaHnjy7Ov8vzbbA9XfGW5uujsfwh23D9QwPhrNAxXKRAZ8kqapPp3M8JI-0g0R49h-bMITNqUOcMrBFCiEv3QU8THjfPGecBJj7KgJJHlVIkNNryfT9TdBDW1GcbJimNePY9_01SKFs6n-Z2m74x5v9Ty-hoE3ZU_M-3F6UaWEMPHgovFQ0MeYNCDEGJiu3a4OHjtsXLJh9PE6--0k6x_zNu3DAVfWhHrV5yt14_HE4NiRch4DqDFD1j-jTokA2Z7qsjm6lF8ryACs5KSgGkqKWGnwKYl9HqrflbXHc62bkuf0tRaeo8w7-foDH4oTqBcfK0o7ey47w9cOps5DySBWQfqBOj3svJjO1olfbT_FCr1Kb_hh6iCz2y2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گل‌دوم آرژانتین توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98032" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گگگگگگگل صحیحههههههه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98031" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH_VwLqhudnN3m-dp6-R-m7WZCXB1hkbEWN5eVh1vAnejnrbWUkPzQkGGb1-HKpL_Xn7r0DrGYqRRX4Weac4Ax_kfVmovlYlHccyNI5PX2G6Zw3qMSazh9uZ15w7uG0s_6ymBrgor7hQUP9uNMu5iNHgNJuzww_4ZdtU-75wZK6Zv0YDC05sYEKRxgJ17gZFIM8H0KLs-MA-jvanMBKscTUe5DiMwDFrCpHpCmwbhOg_JLYlMi1p9s0ufPna1VBcx3a-RM8xqNAYkmsNU7wIkVLhPAFsgeakwtec1MgrYKjxJuhWZ75Xu6nyfTJbg2UytLXGoUG9q1VOpHz8rMOdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حروم زاده فالوورتو گرفتی حالا صیکتو بزن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98030" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کس مادر جادوگرررررررر غنایییبیبییییی
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98029" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لیساندرووووووووو ویزینا میزینا نگاییییییددددددددددد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98028" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لیساندرو مارتینزززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98027" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الللللهههههه اکبرررررر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98026" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
