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
<img src="https://cdn4.telesco.pe/file/UI0X5Yxl5g0V2r4tyAeZv0dMGyOQImQoX8cYT7UR194V0O2ZiUVKg7ixroeFif8M-Fp_01rGSADsqra9IP2Tnt9B06hnozvhDvSxWJx43dUbOp2ZEjbaJ-NQNbpIEVxv_FKGvHJcOWP01P5SPRSLfhiil8BxnadcGruic_JI-gnPXu9XaGG5jhfBLnO8PSc0Zw4A1_LqrHXemIV7AthWqDZn13XWn83yMLW0eoUhRoqrsVU1E0rrL9MYu5HRK4ZIY6ITb9QwekOyi5AVQNkyXdheehflvXBhWn6y0F4B4sCDGV7HjpgKMnGACP2f20FQzZVaD-j-5EIqZe2E5SIm1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 434K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhvTiJloofmffmyFgzsRLrhSFia2QoOaSW3NLWeL2UvTaK57e56ic_VsKAxowcAOPsLrHNLxYbfw6QzoeLJie6xUjNu7weR6xnrJlBhYJPgP-TMTNBkX4cdqb9FYLXCNuAIHAmte5_GcT-P_ljglLkDOQqvB7cjOGBib3TWkV56yp0jvEYeFn0aVf0z9Xv08eFSBC6LIwrHw4qbFI0den7Brv_ooZbR2T6bLuGfeHlcLZzb4yLWGmn7lWqyQSOImJT_NoZLm_3s2OtGsl9F58LkGEIrdyezDRqsZu2yo9hFn2nPOieoxPRB50_l0miBvZcVZFWTrrAv8dBpMdxaTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od1EpY_KrzUNeIa7fGvSWiPh3De0CkkR-WxW_Z-VFOP_FV89fCPZXZQQIAO0Q1QHLQ46pys-G1f_uZ__46MJNeoW4nfC_DPhITkaqbcxnCSsqnfDrmUyPYFTb5hTyuzR3TrlZOvN-CGudaAJ4F_rNBZp0R2ZnThcsQzSKug-R_IRxTBLMh5u2njkDXHMG9vmeAhJRHN_z22ZQ7XqZgI8ix7TI0BNB8HIbzY4u4UXnSWDRWYXZAxSFQB5IXu0OdYx0Y0EEK-PFldmZdhljGd6-D-RlL-VChlz_PlcqBcegz8XB2kxyU11AEvCc2NTU1mMN-2s53f4gRifzYUdqgikWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd2YYELGlxakoqYjLrqZ5RJzjCuFVNXvTLtlCldhm4sEGXSP7dthg9NLIDn2CrnJIZua3bdzP8fzzRwtLkdHv818aYWH9DaVXYrE1sjYrYZ-zJwRM1U_kagRk1J3G4clHCj4cCu1KAT2tuVcAyq6OlvhKfKVjhaHnl3t6ginOoB4jnhCy9smrNsDZxCPEQe41xBBroGd6G5dhckhwbNIpdcmtODl7NCXS-dcb3PVdP44i5ipTvV9Oqdr6avCF0CJVsBc5rHNh41UWFaYiPjgFW-AdmuIDWuFvQ8C_Nw2ItL2dLBC03kzsLBha1ywSQNUD0UyZ2YMNFouwWcKYHyF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGvFDI2VYSXr5Q2CNNk6RnpDZBGpKO_Wwxk6JYCLsMefwk3C9kWkmWp1YN-zy1L6wT71-Jtole6SOx0P9j2TaWu65b3KfiQb019MfrFFh6WtpCI5iFu-FKChUyqpjx_JHKls6afwlAyOlFTTxYazvAW_2jHrJ2sy5cSd7w8_6778pzSR5O5oWZmZsiHTI3prCnpDr3dGMP6orHRSXQVb1LIXdvrxq8ybXzc5LD4a3HRDTjCpY-13opigqT5C9q7dpTXDykkM_m-DmZh7xxZwA-xX2S0Acd4phKXjiKKL7peIbWIwJRzVGc7eIAzK921Yr_jTb5yVK1_YE-3GcrUQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=b0Zu3oD-TmomycWgINOWqdTNfIEL_200OM-CUJniWNztyirR191i8BdlqiMuT974fYtP412bC4NSfrTHjuW4xPHuG1acddg-h76db-mzLCKZbXQQqR4IAwxkZ2jlHBJ4wjZXgtR2aQTPM-nVLiN1QGEDl45GR2Dp62tdw38epMdPSNmFTiEbrewXv8BKpjJrOmIThSOBYgn89N1mBvPRz30D1SIFmWNBBqBgFvv6ijo29_IVWmkbXZOZZpuQ3ZCnkR7-JYrhSx1CFJ3EC4UG11YKdcvQHR08mO1jfBqYn-3e_2pgBSgCwj1tA8AbSBUc5s-2EdII6smdSVRyhBs8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=b0Zu3oD-TmomycWgINOWqdTNfIEL_200OM-CUJniWNztyirR191i8BdlqiMuT974fYtP412bC4NSfrTHjuW4xPHuG1acddg-h76db-mzLCKZbXQQqR4IAwxkZ2jlHBJ4wjZXgtR2aQTPM-nVLiN1QGEDl45GR2Dp62tdw38epMdPSNmFTiEbrewXv8BKpjJrOmIThSOBYgn89N1mBvPRz30D1SIFmWNBBqBgFvv6ijo29_IVWmkbXZOZZpuQ3ZCnkR7-JYrhSx1CFJ3EC4UG11YKdcvQHR08mO1jfBqYn-3e_2pgBSgCwj1tA8AbSBUc5s-2EdII6smdSVRyhBs8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk2XE4QsVR1YhU5_2MJO2QtFcEHZSzJWvZIWvvdnwzzCIbg8rTyKRE6pHTZ0dv8mhlbaLWJIUNljzHs19Ml6ITmpluODY3g3s5-TmUzYVI5EX9nqkfDsXxdVpL9ViZ9ac_SzQjjnfDhedaTtuo1rPZqzrT8awbYthBXwQ5SHc9D-QbEvO1rqCFhsdEtOX6cAsgKjn8GjjlLVU5bbD9CzTQMMD8IQ-XmTjDmRRJuRd3iTI65OXosBJ5e0CScc74ufCyfZdxwZPJ_4x1vaTaixaVReJrYILNS4ZRtxM5h2-qG-POluE4gC72ljEbsdKGvQYLNj91KBqBp45pqOLfb4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H71YdjnxQ4Ng2CJEZE5vt6brg0BG8sCqamqhITYGs6sut1Bi8XTvCk_CAtUX8fEi_g7ZjOUPjddP1gTagsseMjG9JYThh0xqqJJfvQVJz4n0_CY6okKc20t4_qHiD6Tvjll8lh6pOdQKU6Ye1QHskBcrZe5w2odlTzTr0zUngCl1K-tp4PiqKPPJv2qg1SDDByOW1iial2p8F0M7WyuofkprbMJDAwKw8yHxXL0-fsaMeKhaDfMtn2VrgEB1wLJDDpN5sMobc2MzXb4d2Ghu4B_bCk38MO-aGmhuQji9zhiE4qIt6h9gkRqEMw4f_gNyKTMWH8CK4TXAZQjzLDhQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqBMiG-y1H07Io1NOETYFo-bMRaX1bq7S9HwrTcBr95zqJb7sadi6X11S12vk6cAZxhtFlO6RhAjHj87_cnUcBySG7mBtGaijYQdTOcQvMPvyI202oVcKyLe_XeGPIGz9QN7h_yZL_qh-exl9ZKbLAJPRb6mx7X28TWQWOWdhPlegkDEB5T25c__upAvFK3V-TtQsWjvnLprKHYtQqIKjSTNtW4C5YXRVK0arOAM8NIL1Xu99Cw9aQlpyjGl7TINghdZoaWnSSizbyNMaxQahS6mhj5gapw-y20hjlXBS_Js9xiK6UAkFZmZsSuZgB_45Syafudi7Ty3bxQiYFPTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=GeZqXVl6pE665L-WYV9iK6av4eTF5nVmxcN0t_WQkysB-bp154Amo8kiUcb4D74ZEqQyEw4gXlzZQF8GatLbPW4CegrjxcGY4JcYupxuabMtGmQuuif5Pg24zZ0hJsrrwijoBSaiZbSu0023eVVdvmGIFQxqmTiQi7m7-tXOpcCD8xySJgI4u-ADvcM6rDw9N2L6M23GlYzF6Z2utmqmH204ZufHY5CICPBf-3t4S92z-4sd-DmYQwDMcDis5h4mHvzly_Uzv6T_Wmd8Q6PctzM2jQQGJWT5JqSYyo1A0uI4c6vEdbnC4SwS1TvDoxFxJ6PGDvdXGGFiE_jGFsCv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=GeZqXVl6pE665L-WYV9iK6av4eTF5nVmxcN0t_WQkysB-bp154Amo8kiUcb4D74ZEqQyEw4gXlzZQF8GatLbPW4CegrjxcGY4JcYupxuabMtGmQuuif5Pg24zZ0hJsrrwijoBSaiZbSu0023eVVdvmGIFQxqmTiQi7m7-tXOpcCD8xySJgI4u-ADvcM6rDw9N2L6M23GlYzF6Z2utmqmH204ZufHY5CICPBf-3t4S92z-4sd-DmYQwDMcDis5h4mHvzly_Uzv6T_Wmd8Q6PctzM2jQQGJWT5JqSYyo1A0uI4c6vEdbnC4SwS1TvDoxFxJ6PGDvdXGGFiE_jGFsCv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzuy1udhuRpTfmQ3vxs3Wh8MqMOOc8hHDRjzDc6goQjp2xuJBQr4QbRuwhrXqW24687GEicGgsJDA1bIotK_UFdK5LMCE8V8ysUX0Uu4V8QbyGzbizmH7oSwdVstzCCr8UkMZZRNo3oCrm5aZH4bgUIjby_cqXu4oAyHthD6HdyIi0VroOgQt36XXm9aybgdl1c2Q749fvluMnEh26OCoKUUEiHn_10SzeroPp2Vkz94TXuCVeqW9y8yWpi77wi-VqebUW0GCPkjC5qkRnkqT5g2AHVOQgaNH58FQWY1KVhYY_VFRYe70GJflusWcKxSLakxGw5Fp8j6BOSi6wKcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwDPDCzdBhJWqJHKSgUBAb4gAW1TSSShdd33H5CHt4o1Ap1gLYNLzU4DfXqYp7xm0OmCbBL7lviepaWswoSRUq_P3D882cphasCJLLRgcpvB_4ptbKnVK90II-O7zNfVKYUgnsWmDmLmpZfhp6tCRyBJ460tqWBZKhJkbDWczOaGszBbffWUjNC5dhx1GDuhSUaVPMyPVjh-N5L_5yIKLjLbviycmxXo6mVWpiVO5sF91Lx42bzet0uELgvQhfO2Wj-5O4wlojGuTw-k6I_jvtBgaHJ82Gxc7oqsDqZsU2ND_aOZdkvf_yvyvzRNlvfO2Iqm781ZY9d8rdp_BgViCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjYj_d3dLRTI-lJdTfWHjhnrOqtLc1dFxrVijJvWLa75_a9H-KIQq66y-uljq15mb3Uvtnr3JOGPwnUJ1ozp38zbuzPcbpFauL0jBU_7TsviKEof5FEDKJk3RPsby4Bt66Y8IaVYyuxlNkfM_Rn_oSOZLUgc1OHf7Y08TwJo9cTkgyp6XXeDvUXiHxO9pIm0ZlWIhKO2h62-vezNFU9Pwo373n0EghuFUVdW5mWPPoNOkFrrAY9rNjZhKw2Nk9uJ45k0RfEeZJhnMMutMSgxI69gkvO58BJm4795uANULlEUjkwnKR141oL6ggsfvd75bURprYV2FvfP13ZzkpaARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اگه دیشب داخل کانال بت ما بودی می‌فهمیدی چرا همه  دارن درباره‌ش حرف میزنن
😂
🔥
😃
تحلیل‌های جدید  امشب
سیف تر و آنالیز شده تر از دیشبه
😃
♨️
آرون تیپ=
وین
⚽️
✅
💵
😍
فقط یه کلیک فاصله با وین داری؛ بیا خودت ببین
👇
😃
JOIN
JOIN JOIN JOIN
😃
JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30953" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=qE7xokWTSNYaHveSz-jqy0dau6a2y3FQGnxZhetaWE40uQqOqThHyMBU-VxPbsrMoFh7HG_MOlgMAlz2BsSISw2SKpXZYEivHaAyO4KaPc8F8DZN1wDZ7X_TwpRbtu8xX5WipzNdyAP6GeacltGVB-0xGVSGnqFmg9t4bzOD19KRoFHAul3-8nXWXTmy8tLKwX-AU-wsRL9i6qGdbnSkaj7sjaVABXzzgt_wOKzHpNvhFCnKNQhatFFDXBw06RYjwxSZuE3r12v57qWh8tQjrC9gmwnAlfKfMOF3QNtGrYVp8GCxdAv0ltmYjYkBUEUdgK8RSM56LTFrOM0gFWiehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=qE7xokWTSNYaHveSz-jqy0dau6a2y3FQGnxZhetaWE40uQqOqThHyMBU-VxPbsrMoFh7HG_MOlgMAlz2BsSISw2SKpXZYEivHaAyO4KaPc8F8DZN1wDZ7X_TwpRbtu8xX5WipzNdyAP6GeacltGVB-0xGVSGnqFmg9t4bzOD19KRoFHAul3-8nXWXTmy8tLKwX-AU-wsRL9i6qGdbnSkaj7sjaVABXzzgt_wOKzHpNvhFCnKNQhatFFDXBw06RYjwxSZuE3r12v57qWh8tQjrC9gmwnAlfKfMOF3QNtGrYVp8GCxdAv0ltmYjYkBUEUdgK8RSM56LTFrOM0gFWiehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx5APqBjiv-JUaz85K_tsprDrXwjZR4hxk3RD8TKVfDrPLN4rvo-mg0weTLa5DDRWAt3zVg_AfTzeUC--03-4eUUSKEnEeHrY78F7Igp0NgHZsc7zMXTCrl5Fi39Upr7PbHdd4zJ86iYMnwvBY_FUdSbey8NDhVUWZPPKjLTaqzl_kryRlmzX7UU616oYlMyprISI_xZbUcedh8Q9-6m6-hK_nWK5uaWFRS7rUTdYlUFSC5GsOxBmOjdNcazNBEldZlC7GT6nOxN8Ksvjbnrw9b8Hj7zPUNqia8iiagfqEPZD5oLSXhUyftL3oJRdrBbEzYcw2qPk68LCxInLVHoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQlkr-gnZEvfn0bkO5vxum1ZmqJaiizrEc0MV5IVc91V5ZnnLrPnNCn5_8XLblUOQ3xwG9OMQa1FKhMIsjQxRoderw_Vo5yQTMVhhjNFLbIOnETptaQ49WNHkOLbtkq9LYQd_SEhz8beAmcod0fPaZIW0HwX0i1oFwc7k4GbbwCFiEzCibD98M0RUeq9sWHiW8mzFlFfiCVnSbgWIS_bNHT-nY3HCDsg0nEW46Vf2nqx5G_RJfZvB1ef_z1qUfFwlU9bUDAJb1niGWlcammghKBiICE2pQxBBLCMynCwIQCqYlXLa8Sa9DB0yaQykuV3mU5UjSbNP64xWOP0SOp6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htf2yc7rl3f__1bHhjM4jp7KUyqXak5fRC4KvqYUzU-ePYDlYcXsFar_7JS_aojD7pkFfAhAs6NMweXefF9XlMjJcX8cHlD8gIlVQI4Q0CdTKgeIZnpQaJ9d45E6d8vX0u9-BmNGqpPb5vOlIWBGMIoUuX6HU346GkxaNTY-MrFgUlOlnx1bzFH-tkF76RkiBDjLD3VlB0IzAj6R_tN3nrrElW2LMK-xxZDW6C1pkh5oeiY315MOe2SshfNbepMPHXEwTGhv9IwdOtOmCNtF_ESPfiutlT1YAOTCXx8__OcLhgUJXSQ99SfO1GDG6XQZ5G375Yyjzkgl-wmar9BeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdbSH_Livv1YaKqLu8kHetb9Ohx67Dapm3lsLYUN8i7KSyN2u6N7sNe6GLLnyD0251sqfwsyz277sGyXuLm8E6RHt8l3uI1yvERLMooSlSnztrAak-vbFqM3FD60vzIxHHD8DutvBQCOiRTDQN-qoPkMOEpgwUtZJaEJWZqBMixUJ_nYPs9693rFRE5_OJqnnuZgdFqWeOPMrCb7fIZTxdqI4SAQHSEfr7XyOdw14-0TZe29wcYB26Gp8VfPQc4TaqJsvswdk5wWy9NWGX5BGRRDOo41gtXUU09_36L3HzQwHcjZtTHVxlf8aM_bifVcIdzmENck9uCzsGKqoR0Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAU4lPr7OxFEyBz208PpOn0niAYW9ijxzkiyaUb9TD7tSJdUKKSCw54CoKyoiPHg6qTz1YVciQXWU3bFD7nuX0T4Ylh_oIBz6VUVgkVG9z6VSaNKEh3bQ5rRgAHA_pdCWQBqqTxBxJYpALx8MpVaBuKehRn-RT0zFNeh0oGFfnyBCNMSS6O-Vj9QRcAhHbe0h8adz1un3_jhIroxMdCDcpUulKYM233u4ZFdT4GwhXJQlHeZXp4nL5y7zPkNVhSz2R__Vdj8_y3Yp170be8fTPxxOk9gOt9gkVRo5lY2bipiub_YkepNfOPNbD-IZFR8tKXYrRR0ZohkbU94fVrGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG3r4EPMM_AwUoZ4mnkkKoxBB-p3c_en7jWZp9gYR2YgzcGQDsHPdX2ph9YbKa_Ss_93YQ7Dihpd-O0bRGGYLRsiBibEs2EfLuiW3ruVRjTdD0Zjp5oWgUYQH2vji-b506-sj7UanrIjTKT9wUJHFWYXJucyAYufrn-e15lb2XfqsPxAicKec3E4oDT22ylH3TVI-AsgXOtKyT5l_en0APavpSYg060J_UL4-o1mXGahn34L-3njxS2lTQcz-wa_YesQ-i2-ddJS-srq7qL6r1y-E3JpPM_WeI-2KEBX0db7qkzW_PGY4FkzTYK7F86_PmDXtDfTQTNUolVT64-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov5rhXuDa0L-HkqK5f6-j8YB1koBcEBd4SayhPQkywZnV6Np338Tx5n4Ob81fQQp5gmZzz0Wo5PQt93_8WSg-d21Ogjxd6qBW1jO4ILUF7rKsRotxBN1qfwMpHrpjw5G_zdSk7L_SItMhAZD9_9IjiQrdniYfaK6p9ohHx9ARgZCW0XI1IyB-SW2m5eWJet5ONEz-1sKoU9umVcHUEPXIrKTt4G-fMB2Waynh4YX2JdPxua7DuvO3z8ShvT_W2kaiV3BuBy7uZ9yVhMIFwjpomssh0IIGZPp3MQnvJFmEK6lFQ58MBkv_5FCrHPeWnvWIGGIOJ-vYrb9oqZ8uPApjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5SiukSwaM6EN8dAD9kWg_Oe7JFaUMqMGZLVc5qoS94sp-e4X8Qexsv9-RWZrT_Dhz4l7b8qYToUjxn8SK-eaQQ8QdMATVsWVYmiHUt6UevkwrudAEG3DxVSYuF9o0DG_dzOwrHMGFovnF-4jj7pBnaS11KnTU8mgVUXZ2kQMGKluGB41DHbSxRw1REzAU1MxwXbwayG7KtdNXUOV_Dq6gSbnCP_WciPPhAsdrZtipKS1j4xQCS17u-ynCFy2JBnnY1KAzdvHWRUAYaoShO7FVbsuKUoXEY5EvnEaibVeuJHJrg65-B73KCQtzp952g9csRt7Qf3QpL_bDAVVhR4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwzJIByrqqMInfxq6AbsbowRAI25uu4X5EmLE6ZYtMBXZ751bGuDpjOa1-fwi_LCBVlmpGgkRe-t7lPlpJdKAqo7L_4-YvFDkAGUBmWv0irb2sEs065hNCyE9ev9dHL-B96IBfwQzRBRLDOw7eMPOsQNwJRpmrj7TLygXiXTkrCV7I_Q3HnYQY-_M5n5hNxkNpFok4hiapHoY2OvxZLkCB6STLfxqufcC2dMHjeuTojMtKdaUil0thhm5lHeDn2cSCJJEQOhE3T3ylKD2fCYkap_0akwO2eNsvLknFKCiE2GRUnLgwUHJX84NPx4ujYuBIHVoJTIiF1Qr-XrXMrjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnVZaJFj1y4LQM3cCtjONEeMWNNalsNmMpCsOGYwnChnfjTJWozoAfMljo_KcvglnonxQQGlgEUSGg6ck-4njXiMtItVVEZuY7-Rse1W_3nU_mCbFukt_WtNTSD9nEaK7Fn5pQZTuduriKEj0HM7cVKHdnr4uz8-pnatKOdhBD_tQ2vsmEo_IciJUad9ExyflJdnxMYiO_4JKiEPyWvLLFzjsOr-vftOG0SAq2A8Lt48TwdNEfcAPs2Efn2h9yh1tjRqBOzdE4bf4fqfxyCoi2X0EZXslCc8SWCoBFObj4pCJPeGa9e1S1iWW9yl-vmMQADnJ3Xtrr8-mHwFoK1RiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=q4nL59CLViscnkWOOjRKrBbEH83B5mPM8xt_R9u7WpZkkCcewCs157qMp4izytRVaDOwO5rXTq1MzJvfvmf_X_kKd4wSORKK18Z766KGWGy4BYC0c5b6rYkBeWLI55-LNpqhYL30uWKakI2vmlCCx_liJyTv5OuwIWngXLMHk23j_14RzJfkemw3SaryIdyxyefdI71x8ranLHmQuYfe9B7Eb9Z8yL7z0oOJwsyVz5lXUoTtBmNfEzjuaTVgCeoJfiUo9US21kIsGW8Ou9MwpMmG5bafu-HcysW0Me4btxyrak63YzHuxc51naIsACH9TUfap9pSKmsY6tFEhUzlEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=q4nL59CLViscnkWOOjRKrBbEH83B5mPM8xt_R9u7WpZkkCcewCs157qMp4izytRVaDOwO5rXTq1MzJvfvmf_X_kKd4wSORKK18Z766KGWGy4BYC0c5b6rYkBeWLI55-LNpqhYL30uWKakI2vmlCCx_liJyTv5OuwIWngXLMHk23j_14RzJfkemw3SaryIdyxyefdI71x8ranLHmQuYfe9B7Eb9Z8yL7z0oOJwsyVz5lXUoTtBmNfEzjuaTVgCeoJfiUo9US21kIsGW8Ou9MwpMmG5bafu-HcysW0Me4btxyrak63YzHuxc51naIsACH9TUfap9pSKmsY6tFEhUzlEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=qr-Pvk1F7fk6mxRm2_ofhMGPa8TX9gXlL5Rg6d9R6yVstJLdMiXcB-vRZZInqrxx7wC2SLFlkYqnKaJ1IeQvvvth2hRB0iOp1bvZsIynglnW8S9TqHm1vHDvDvLYWc2M5NVuVsWjzmyWiDvN2iuGpBSQhxBWaDA8-hoNE3Ty9PIXHQWtVroy8pDgy6PdWmD5ab3d5Fe1ZtkxRldjyWd5al-c5w62aBRqysuFxyDVGDG4QQ6TacO-KWYYv6yJmhtk1TrXBf6lo1HwV0Fg73WuuZaKpxUcYtyJrotgr6LYW5nruYq-unN6FrtNWEaSGMQ76WKQhskkaqweaSTjm-p63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=qr-Pvk1F7fk6mxRm2_ofhMGPa8TX9gXlL5Rg6d9R6yVstJLdMiXcB-vRZZInqrxx7wC2SLFlkYqnKaJ1IeQvvvth2hRB0iOp1bvZsIynglnW8S9TqHm1vHDvDvLYWc2M5NVuVsWjzmyWiDvN2iuGpBSQhxBWaDA8-hoNE3Ty9PIXHQWtVroy8pDgy6PdWmD5ab3d5Fe1ZtkxRldjyWd5al-c5w62aBRqysuFxyDVGDG4QQ6TacO-KWYYv6yJmhtk1TrXBf6lo1HwV0Fg73WuuZaKpxUcYtyJrotgr6LYW5nruYq-unN6FrtNWEaSGMQ76WKQhskkaqweaSTjm-p63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJpEZerE0_9C5KVeJEmT_MQiDwjd-awyF7hBnqRs0HaDkJa7Hraw8DkRyBuEzwWukhwFSNelcqtCSsnfwvODRV6f3INLB2JdI8AFQ3NPnxMdtk-_NyKaRJSfz4fKh3fi9kpYGe7L2RsbLHm9sMqnHwBzbchx8FTc0SgVgQyyTSvFUeFtyWs6ryjG89wtfNAycxK9FSRVM_FLhkFcWOlwox9z4dHC9RpLxnz1vWeKFMVBIGvuV8c_j-k93VcpDb-YtuQlDRdNppHDcHt5x72GVBqUfT20vDvaWU1o_l0bomkQhbtajbmN1B2gu8P3D9jNUlT_-7XG1JBJypsJv-SeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_YswnZI0KMJcBjb5DEdmjeI-YBcQXKp56-80MRjh4IfaOksYPs_82RmgHWmIO3fVr0TtKZcejAg24GMwylMikCcpsTlGUaDoq-seVNNurwJCsZXDxFaVbFITbM7x7fDXm0VYq_csoMBnebufDuLw5EC1ypZ1YTgZFZoGBz-xxwk_MiaqoHp9yXkpQv9KKaEHjb7J8_if9VPdBARE_AX3hYpX8F8dMcUa1HYM5TWHPYnZ98jYEKdEZKqIhgbLUgE3s0llyUz2Z9hR1iDQ_7u-E4NC4GAUUBrmq7KW3-HbR6sqEw-CpqJKc1oIEjZCx8YtLtqzg2Xzr6k3TqRwWOYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-DbkFjdkiRx7nLt3AIiJfZNO0PMeMX32b6S32DYZ24-vC2QpkZHDXvSwr06pzBfHa6Cu9vZowThGVcS45fa2KsgweDaIfk25k-pqBmRpcEJ_0WhnjbUDFvzHDxMoZg90hmcfQ1UfgE7XfEcHTYfNuwWQWlMP4ZqnfvuHXF625i3O-uaxaBWUkOoUpNyhHE8zHi3Frg5c_nyUiz9as6Sk2-zReEU04fWNiiZoGqJfwm3xDWEcWCAgig5BWgtCIXONqVM-dt32sWPo8iaI8EYFpd4Xd_-ARM-b0BC4WXlnUcqgFH-ygmUbMdk1W8yiBoGwrJvYHF5RS0sZA0c1OHcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hm3By6WLryadRvkbHChUbzsumh2oAgvf1CL6SbHJ1-1bXp71kaHROWxovq8wRQ9UT9AQWL_yzecWhxhoWUxdmkcXpMMRocHJPpI9J-zNXAv-bJ_K8cR_fBgXaooQpOlo9HfrA88WCQFUOBQgB4qYBEKMYvidBIlU12ZfrOm8O_-SefUckEChbDVbY8EjKfcKxUEEHqUhi1mIhuGFltFWUIx6OeQWBHj5cjKAO4jRWemMjwgk8p9JWYZzvExeIdcc3nMnWqHQoVb9TZsu3Nb2Y2lo93lwSFItkWVkAN-0ZYgYTAQRJxLE8Nx2hsbUhW7tjbqcP6zerdNXton1sQdupQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=mTICH5m80Omyq0BaiHyKiHCET59T79P3dlwPKL2xs7lrKoIY2JECKMUw92MHi1Cuc5F29iWQEGP0vv4d4KNkFWcixBG-gM8Pbyl3IEyVRBmSywk3Eb_vNEcTOMlTCHPcgQBl3y-R39HAn3EA5a8MAj1PEbB6LC5suRX9HJAu4Jff11zeTGzwo-jOZN7Ij2Dt2VSulpB1c8XFSj_QVCri_-hqqtmGXcMPUf107x3lTU5AnGiKEh2OGITtF0fLaevg9ZEqb08xhfH35NyRlkCb6MPrMPweqs9HC39prtEp3i7LPeF5CTUCeEj6BmhWRstJVIYMRobmQ3jwTzDtyD81P4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=mTICH5m80Omyq0BaiHyKiHCET59T79P3dlwPKL2xs7lrKoIY2JECKMUw92MHi1Cuc5F29iWQEGP0vv4d4KNkFWcixBG-gM8Pbyl3IEyVRBmSywk3Eb_vNEcTOMlTCHPcgQBl3y-R39HAn3EA5a8MAj1PEbB6LC5suRX9HJAu4Jff11zeTGzwo-jOZN7Ij2Dt2VSulpB1c8XFSj_QVCri_-hqqtmGXcMPUf107x3lTU5AnGiKEh2OGITtF0fLaevg9ZEqb08xhfH35NyRlkCb6MPrMPweqs9HC39prtEp3i7LPeF5CTUCeEj6BmhWRstJVIYMRobmQ3jwTzDtyD81P4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=ZORd5w1w0IL0UD7Eoh5R5HFfBA5A9FCNLzVjBtJiulgE9CIY-aQERQZJMMaSQCFcEriIEBR6MRiqiCStegcFn1AGGi6k4SkvEWvnZcmdAOzqAT7Nq7bwhxlXmFJmLF-kdmezAtp-_rL3V2_pqBB5406Rfoff7tAB_jg15i8BaKA8FP9jNDCnVUR4cRl8sjZfYnzI-M7IMd9LkWST9fCj4RHbsvinp9I5U4-C6icgJXbKVahrSkimSQRt5AigPhVFJ5muZKtnjMDbWppPex0yvkPzClJRRVxpEYa_q5CR3lG3AzPPFNnkmzM_k3OCjoVvROlOfmZRnLyeXz7tjEI5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=ZORd5w1w0IL0UD7Eoh5R5HFfBA5A9FCNLzVjBtJiulgE9CIY-aQERQZJMMaSQCFcEriIEBR6MRiqiCStegcFn1AGGi6k4SkvEWvnZcmdAOzqAT7Nq7bwhxlXmFJmLF-kdmezAtp-_rL3V2_pqBB5406Rfoff7tAB_jg15i8BaKA8FP9jNDCnVUR4cRl8sjZfYnzI-M7IMd9LkWST9fCj4RHbsvinp9I5U4-C6icgJXbKVahrSkimSQRt5AigPhVFJ5muZKtnjMDbWppPex0yvkPzClJRRVxpEYa_q5CR3lG3AzPPFNnkmzM_k3OCjoVvROlOfmZRnLyeXz7tjEI5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knd_YNbJhbz753WSWZBU2oDIXi7tvP_hyvwV6yH-VBTYTPfJ_VmkWNGYJnwQ2DgS4RhNNYTS7_7Eplz6HkhHwq15rWqHHGVM-Xdyc7SOxx_9zA3dAubMNpMMPUg2oq4KCenNpPEZ9Pt_eXIfGnRtl-s5EiHz-Krhx6EsJgaAvHUI4Zg0WgGZOh-NbyLkDfd--lw7Wq-1oMzim2T4NyvF98bglk-ZWNmWf1x5ipIJycj9DoO3cDwIKabaHa1sX658sYGeQD7e6FSPkwQVqC_P-B7IZG5E-W6O6t0lPxfAnOrUQ9W85eaOpGwljoNmbEkicI5XzMY74OSk6pqhZi7pEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_0Tvv2EEBfferDoubDjDJiZ5lqwiSQCp3xOyRK1h5dlKzUr_Roz2AEJ_fNr-iEymn-8yS7h0R8DG4X-ZkJhUbFl2-omGY7iZzT1ZxpfFBmcj5drJ_6SkdZTJYchI1FUfTpyoYGeqz3ZWD_DNclOa_dEMLqf5VoFMniB5-rfqKM-3CCmllhrlW9MA2K9yydxCh9UWCPik2YtYENSn8IHFinAhHx4Wl_iQwKDkosLJsDM0tll1YOXlBqNlaFwFvHpuZLkUxFpODFFqcJonkzTOVJsWwQJaj0BFFo_5F2_l_O38S5d6N8wjOCwlX73ZbiSmWyVrBf52_ThR0WRyoqsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYkPQhulV4vtjSfHnh2iDHWMFnz40Ay6umwU_XUxhWMP-ErBEHpW0FeyUz1Z223f1F4sFWt9xC4LmP9H6mhU0jd5HbQ8YbliDNpBzy0nBzZB09vFCFIiNJoLDVqdm3Yfl48-qirw9Ps1vB0Cy_4J4K156rUAZOOcucsQbShHQUXStMH7durSOns2uk32kslAMygb3hQm1d06rMEM5R7PNxof9W4ZciqBpelnHDEq5ZG_9KTSiaOjWfILZKPG0selCEW5PGvi-3ubj37iHkrhl6NaW1LBhNMAItpD_MuBcQx3OT5YrsBiV93i3N5qmv6-1aEA635e-L5Ml_G8LY4Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu6k8pvzg0pmQyLKqdugTRf3XO7dKLEyiMTuusLluwfRjEhzPKGFwHGWtxqEUIB9a0KxEOTEGYR3yyYGmhvfH4PI43Gazl113MY85VDGptWZckwKy1UimVnvMvk9rzZMrdU0RAd-VX0WRy_5sYiv7VPYRlXpOEfdoT55MkcprBUoLg-Htv_3R97AC-MFIwOCfwhsBwUwGQY_nVcki7yFmeNRxVCifp2QmiYaBV37-ei7ig221c6FX5-AjVnl3Ciyz8o1x_e8I8xn9yuOFEyGKmwz032sqxkZAsy-Hns0NfUOr-ufF1B73a0xYeMBUC5ZZrli90u4RjwZRSXyg1NLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2P1M8ZBzcWpkECZ_7Zt8aqwY3RXBFyQH-b2OHaV0m945bAb4CiYWm8sCkWLojJLutVYquThbuvn7_6mMH0VUY0KS15cKhn9LRJ6B8DJcqjM_Qt1gA2x8YXy46wSWY0hbbu8m7K4WUErlHCiA7HXGXabFUMqT0nNq8ez7xv86xm_V5Eb7zlTT8lUrKL-18zgSebl_jXEpt176Mbyt1Al8OPN0W20uVzlPzUq2eeFUEFFnm9pvEHAphJ6GWO6YQkBoBTN00y_vWCBTE3BS8hlmWYd9EWwsSF0VM9MdOkloMiDPrggS8r3ZWOqN8ONvLe33oDru9i6srfFd2M9U1EpHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyJSu_BtfsCY_xAFPeXMOmFYKi0LCJMy-iaREvpl67IicMXH-KNlhLpwsDrR_YcTSWcauVeG6thb5U671Z2gtZHwtuLbeyCTI87cKFb5pNLiokOgeC5_as1LFEXV9CDpXr7_AKYdFV6OpwAyKP4vgkb_Z-X9O9-1flUGWgEZej-IXcnnBSdBEwDkD9c8EIc4SojiYMr3DT8_zNi8YV_VYtzbsDNCe5Rsp87QHomWi-0HVhnwrNZod9Qop8tn6zfxY0bZ_qdsrBWF49PFLiZQhhPLTOBHdfCPSxwiv-rFsx3y-KoO8wmHngBEH3T_Y0x6o35rt4RrjtnM1e8keWBlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTeyCIrOWD-CQcPctzJ40tfOjnpsVQUtEcLjAaawUPNufdXBJIWAOoSQUbJOwPKNkuCI_meZfjvSjGxu8wsRTUH091I8Cos7892AR0Hg1Y78f5zofMXU9OBrSdHJ9M39g7Eu_LaknjUyEgkt-LAUhO8wy39LTmcvpBlTm3GjGP4c4DtvZkCQq0QbdiK487kx_7FNfFnZ6WCS42zJqY_DyOm9TY3E-RoaQnH_22nLUF7fOX5m3im0DX9xvSklHy29MTQf8j4srFql7YAP-BHo9CckfnwtjylmAdWYIbQwf32j0mzSCKELhdqJn5h0dLVQCKkVbjjM0IJ_R4KTTMnmwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdyJ8YRL2-YJuECNx0DM3R8RcMdJYU6vN5fnPrCrzx_JK9fzNPeCWSyRwceS3s4iK_SJr13H4q0kcuPRGY1BOET-0XXpliKu_14d-M6PnCKSgBmdJj0LJs10h63lnQiBWCFsUDVkXZsjk__mZLjb7Sy99xly4qkxWp-WWD1Un4ABcG7svvh8uzA8hQQqKVDXp9F8up-25pDBFszb8WF53gRjqD4SoQCFfUQoOfFAdbk_a_vzwQmvypTTitnBzPukUnMoZlG_BSWtlD6cSln4aOW7EA-4Tmt_P5MD_J2R_aUDNrSsyCqEqkxlMvkQAJAnGo01lPYmvxS8ThYMdHpVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2uvW2Q8XbWJOU_6IlHv11QS6yDiaLyFbuNH3WfHhLweXrd6zhl6IZq7PCGJgjFmjOqqsgA7FuedcuO5GPhMsh9Cg8iYVdgSojQNOIG7_AEcfl_ZS6bWlKxoXqPrBt5BkrK8IOmEiq_Zf4cHhNNgKShqczxSJjglyAt6mwtJDfuec6E4fcZ_SRCFlHkwF5S1kH6BxPLPBbjqemIro-_d9N2xNoId7Wus4XEAHnuNIFxwE0lmPOKLynxzxRKpxuv12Od1WwDZpglypzlW-X6A4jvpb0p3rAxaiKo3oa0hs4lMTFqAMYMNSeE-NYa2pw30dCLgU7szFzLkz6TCFvduEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s17sodWGntbRzXePX-YEbyceAjxYGtIsk6udyI2WkwVaMNVffkRoOEsirFRRwgzo2OAuCpOY7-YOSOCdk6ttvInolh0G9PrNfPM_tXAIc8lmyf2OkXvu4n26f9YyaY1-p3OmpzDnz89pYXvKiCt2ZpvWpObty8hotUnZQMfaqRBvjdTawpyDvDxRGbd6IMZO9iIXQLun0-bPtNhvLf1mre89DbIuZOTK2wCGFltWt6jvjyZ9JmmDBbsJHhKon1rfJ7fywDYUTVR-RCV6o02NJEunVlem89JHgTsk2SP2Guod40Nicm00dEPK184S3ypV-oZObBI0kJUiD-02WOCVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-d9iEMQfAgp1DVpcI2qnqnJ_hLEDWg0NH6yZoI_OX6Pi7mwZ8AyGiUHVWwSbnpDNbJh4oymY6qrNZXZViJ6cEXOR-PMyLqTrG70lNju_RGwMaTyd_a3SUjT_xtpq_CmM40YZfmcFTBDp7NwKetSnQNPqfTEmENb-sEIjLh1J1IJ6FG40nRAVThkUZMTf24eVOGlfn-1siHXCypzyx0bYfmIeBaZw5tcI_NhDr6XEgAtUfEJXAiRXFaSmWdkSepN2B-6TjpTtfgsCNsOfqxoP92CenUZClxd72MVvL8__aoXDjBObesg8gttXhrZwPY8g-3N75PcUrw2O2Y5XQC67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG6xlXF28olBItYfuqJ5zQkwxe6BAg0tDQvjdG3ShAC9rAf6JGVjkEXGQ0aiBY0vhOCO0mEBitTFsGkzpOlWVEqxT441CbnsinkpkeLD8UhEODuuI5TzhoMHl58e14w1qLkdba0f9vmZ8Z43g0yAxERQg6Cofj4NBR7WqNfIkwtRtcCQnm_E5u8-bNwzXzjPAJNIsW7C4ocx-eBr9IGxxIKHU0fL5VOzJZS6puvoH6bVUpAsCtMLe-zZBjWtkGZqtv4Fdtijcxls5xvHxJ8J-HHe5l5GO1lTfQTECKzb0sXTWpIDlYRHnmc8hrWnw3euA6k4M246DWECEi2g_R1XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSrjTQIijgm_HlthZc63t3j8GwbZC-DWqHcpFtpsqKfOjFehJhKFxmBFfbkvFUsIwAqicssJ44bHe563qsVi8Yw6GW6eBF4dm5sAbTGbbzyBdTGu0TcQ6-SNDnGu6Y9X9aK2QKPkwqENSTK17gANbvbV57vZ_gzu_MvtNuQE64qpbF0ykSAbFW73O2U25UmulMc5-q438vl5Q_paJpBp-GWpefmqNXIj0SkrNuC90v9u-ICi-BXSnR-TWP7hEbMm43hljaB70Ax0xJxtM3grcYId8DpM7-n6L8P1_jce_63qyJnk1P44WnekRUU6OSMrJisq_XFdT7eIl-epSEPX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=NJNiFfmT472e2oBrFPzX-zlV9D9n0KhCUVPqQYGhBBocjIFm4mvW09Fv2qOY5x0fvPmXJ7ga74E4sjFHYV8mlHYbULMTzz0moSEPtRenCwnBvqWX68krd-nwfCVOJGHp122JJGnL3xzWjAP0oD8QS7hOZ9IN-_OCfsWv-pG9qqNBbI6XVWnmcQ23kF2480zcPUD3DL6M98dnZ2A2x3CIltIyAEsemWbTBw3d45dWhe8OnJllRAkq1uhtOd8aKPwdBzieJRprVAH86yQD3t4_4I6zYz4piLb3wDSAtrrn4bY7I854pZwTIjqry-aH5Tna8gPqIWaN2GftTnItqIZ1b7_PXq3n-zqlwu23eexnHMQvBgmyxtB42RhqHg7iEVvslGOW6YQPfwpSgmzNm8CFJAar1rJEYEU29B87dSYDFZvNuffEtZ2THJislFPH7hIXlSp5bmZel8idin45gDEmPcmIlypicVQ-WlLxj4tr_J4nHtRE6e_gspAJeiMZuMbeUlZ77dsJ5Nk0w0iTiIr3SwbKMmvqc_7BvefPXJjhqkmcQ9q-Ixa-G18CtldKIR79ybznLOmthaJ286vlRIKjMx-fWqAQN5IRxjcymnvlMsRsr7DrhH2nWm9Bhameo3gqrN2Ny_fFy59jS8UpXT17sZ7e1wfYnO8Ceo_mihm60aE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=NJNiFfmT472e2oBrFPzX-zlV9D9n0KhCUVPqQYGhBBocjIFm4mvW09Fv2qOY5x0fvPmXJ7ga74E4sjFHYV8mlHYbULMTzz0moSEPtRenCwnBvqWX68krd-nwfCVOJGHp122JJGnL3xzWjAP0oD8QS7hOZ9IN-_OCfsWv-pG9qqNBbI6XVWnmcQ23kF2480zcPUD3DL6M98dnZ2A2x3CIltIyAEsemWbTBw3d45dWhe8OnJllRAkq1uhtOd8aKPwdBzieJRprVAH86yQD3t4_4I6zYz4piLb3wDSAtrrn4bY7I854pZwTIjqry-aH5Tna8gPqIWaN2GftTnItqIZ1b7_PXq3n-zqlwu23eexnHMQvBgmyxtB42RhqHg7iEVvslGOW6YQPfwpSgmzNm8CFJAar1rJEYEU29B87dSYDFZvNuffEtZ2THJislFPH7hIXlSp5bmZel8idin45gDEmPcmIlypicVQ-WlLxj4tr_J4nHtRE6e_gspAJeiMZuMbeUlZ77dsJ5Nk0w0iTiIr3SwbKMmvqc_7BvefPXJjhqkmcQ9q-Ixa-G18CtldKIR79ybznLOmthaJ286vlRIKjMx-fWqAQN5IRxjcymnvlMsRsr7DrhH2nWm9Bhameo3gqrN2Ny_fFy59jS8UpXT17sZ7e1wfYnO8Ceo_mihm60aE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=GJyowbLaiB0yzH_neo1WAAStt7i2ZNZ96COBIF3NsZFgdg2F5H_WlHKRyj8mXlmGDMZdPhl4SyVcyUMgdAENaXpSBjWXfs8oPKjGcn7iXGnNp6OiVQTdGaeUlX7pUjaaMPWkyovkxTdBKtVqJDzbF_388NR-t-Wk2OGmURGt6aLZ777WRew5QcM3PjL5mqXhfm4m7GnDkidODfLg-FGmYV82XYOZDK0vQjBbTkAcsi4dgITSIIGdCemv1kYQcSDJiSl2liox86onFgK7Lco8C_jKEiun5er3JmvELpLWlQyBDfJ1VWy9jP-PWlFlH8c-bRJfDXiaPqb1DouHTkTYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=GJyowbLaiB0yzH_neo1WAAStt7i2ZNZ96COBIF3NsZFgdg2F5H_WlHKRyj8mXlmGDMZdPhl4SyVcyUMgdAENaXpSBjWXfs8oPKjGcn7iXGnNp6OiVQTdGaeUlX7pUjaaMPWkyovkxTdBKtVqJDzbF_388NR-t-Wk2OGmURGt6aLZ777WRew5QcM3PjL5mqXhfm4m7GnDkidODfLg-FGmYV82XYOZDK0vQjBbTkAcsi4dgITSIIGdCemv1kYQcSDJiSl2liox86onFgK7Lco8C_jKEiun5er3JmvELpLWlQyBDfJ1VWy9jP-PWlFlH8c-bRJfDXiaPqb1DouHTkTYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcqfvuNsG8FzitdvogCW_-jYWPud0anb1Ri8Lzdu5h92NM1e-tQEqR4-JiSklgS07NhkVGTNK7LnXGQqnaaeAxSYOhf_EaVmYB6EyvLmY2LhrILd4Cf4xYhy2nFBdjpBaRst7A-nsGLah7cueLWkbJ1detHBAE_wSHNKtAqdRl9Bn6Fsm2Gp-cffIFCWiS0rvHKp3vDU9YqD6w4lavMdwiHJtnkl5a8Vt1CLgHo_Yt4elEPdMC2aui_fl1gRNvQS9ZNIPbRW_7USZcntmFYQtmWJGrKu-0pEDMuag0Su6PMGJ1E05qckLJ67wmANVmpUc5cMLinfHJ4q_HHo-CjW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk4PyueUanXT8ZijEMfgC7jMKdXEhYwyXm0YyH92lU_8PfwOMDUXyT5QNdRQJWKTTSRbsiAyYHzv568RuB-9pnjgobj7tAqGZFsRG9QAjnJzw04eS5xVpDKv9sTvjeEh6ONv-0PeDmKGRuh6Rsoei99aDiLzql51rNHf3uUTRvZRi6CwSdK4AwQ-7v7Nw0pPdOHxS1OJiMezq2FWcWwDUS276MhOAgAUm9F-ndUTK7CZgU6GPN_r7j9M89hbPpYAx1x5RFO0Q99G54OgXBjakxPtWrhPLo4yy4Ic5NFHmTuxRwURQxb4nywAq1Z-2X4vU3VwqN0RVxkIKG2gxqCP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxQewi2tY6hvfAkBVFXdK8pS5DX5L5BgQ2pldWcFlLbsyCUZ07xSficl0fGFqBARwMgKQK1FFnAWoGPpQC7rjN7meDzFXLkkQvDGuRO_u7mqRGtqDrR8ox8AW5KX0KwAZKpobFPWI3DmvmA6lKgvkSJPPGQ1FNVrVy6ahAyhFCE3VJUmOOOnh73YoPC1EqKEiRVl5jluvbYUlIFq3q9i3Hh5T4G_gJ2ucinSgxkcPaAOcUDccr2O7W4SlrP3HnS-TYGUbfVksMoODrWbbSWLQVLfLmAuyMDZBeOcItLsATdvZhoFOryVb2lCpBheUg3kywDz3ADllV5zTMtlgVWzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=HY9krC7WHB69q3tFbNl-XWSuULZBwjXn9jZxu6xvgxCsd_f3GEPOmYjQgWSX8pm8KFfFNBuhFbEZMPTsfBLwBOl-Ox1IGSexkLxEjqh7clrQhfP8pa4aqurWB_9Uc2-Fjcl7j86hDdmzMqBlL63WcQhhmKp0R5JMEyO_GGOLdzPV1FFK7PwsFd5PyC-A3DNm7h9HPDaPlgRDrnJSHl43nBAzdgAQqaBV9ZP-iqLOZgbCu9NydKiziF89qmklr5KUtmtdsFPIb1d2JD4U2oBn5TPkUhO59eyxi2-nvilZpLCrkaiZXJKKPBPbOBrL6DtKYP5W1gkzn7HBoYPTMnk7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=HY9krC7WHB69q3tFbNl-XWSuULZBwjXn9jZxu6xvgxCsd_f3GEPOmYjQgWSX8pm8KFfFNBuhFbEZMPTsfBLwBOl-Ox1IGSexkLxEjqh7clrQhfP8pa4aqurWB_9Uc2-Fjcl7j86hDdmzMqBlL63WcQhhmKp0R5JMEyO_GGOLdzPV1FFK7PwsFd5PyC-A3DNm7h9HPDaPlgRDrnJSHl43nBAzdgAQqaBV9ZP-iqLOZgbCu9NydKiziF89qmklr5KUtmtdsFPIb1d2JD4U2oBn5TPkUhO59eyxi2-nvilZpLCrkaiZXJKKPBPbOBrL6DtKYP5W1gkzn7HBoYPTMnk7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAi5NdiasriXHnOUn0MG5tBDPimtGQCWL8lmNgjX4l3lhA9SuF0Rn2nxO28dQxYaufh8P75ZmlprtvhXuumbYorAKeOf_UF9Btok_jdefFYQTUhyNBmdQHFHJM9urJn8Yhhuuf8akyL5_LrkUkndgvMtpzUO_KoDEZFufTXOlk3uPQ5po2VR6z2xHxNaGRaUPeR1n-ft-OzJ5Fl-pCsj0lkHgmjCJr--jVJf2zQzSGG238tDBklaCbFU8qUsEo1kTS-kjk8M4sZwKwCYJRLyE4B-BM4BoM5yUUCQlTL0W7SMZm79wuhENtIUTAWjTkTpBYmvfrmxLbftd5VarD-h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkJ2L3nlGhaKAFAyPUSsG7KGHe5PMHefg_jg_ibAXt9i2VUOOm3IvB8aORcub-mpK74RgwoSmEEGXZH3YAF2Ps8Eefqf1CxeonsIXwX6R7EQgAG5PlnV7e_4e4WF7lUwW-2bxypmF9izCMU_LRTY_KSv8fKGG8WtYk4seJZ-yD4lm8N9E-BSfu3zboKbKSCRBcJWR654j1DcvH5dqVJ6r-8DXIt-BdJ0GX7KNIIJklFxLG1D_2J1dQvgKgwZwX-xMjZGds8MQpKDBMn90j02H7pICKr0oCCS0C7R0qEp5CsLcl9AsDnGZjKXoCA1lrAWc2FhBbzi_0Cyx68eGyzIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAiwQY4lCOAN1kGY7Vw6ziaJMCzHwHpoe8kL55-3V1b_FigBukFVYNG6vAYFzdBzqEcOeGYfukcwuQK4lVRRmFQfX-XGG1Rc7-EXb5wwtFLaeeMJC093fjmwRTTyrmkjv4R7F0gq-tfQrRP-NHZexmUQ92W2fmAKsgbJMfnG2nAdGwGAjhU2NKOSUwAVwM7fbjg7ciPP27ciwnJa2-ca0WnDaa_CJd-nO5pqWOZauXxkOfP36UA9kpfZkbpo5fp26YMukQS4Py93Wq_UTP50oazMusFJYoU4cDmWT8TSBJpI9vaU6Ik9-JWmD15N3GKM8esB3fCQ1i1D7RUSyps1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_Q_q2eVcixJ2-PHAwLGoiRiuFpcgEJDmfLOpMAn_J6lK_-RPgK6T8rGBhTOIKZ0Fk-LF6zeiqLWaHYvv6q5_58qar6UbJGsorEpuYUUA9lqyVyOX4W943jSHQMoLQatg7rEfNDhjld4XdSEeqHFID8AIo3pWTCOs1MfvCIKw3GD7W9wTrH5GfPXci0btSlbBaY79Ens4HfEJIBMZsp9gO4ABWU--ANaFWYYyi1wcF8pGdSdSteVTdnphFWBf8-kCLYAGHxLK4a0_N4JxS9ZiuyLJzBrqft2ufHZoTbjy17udm_5uAkeVeafGOtzvfntgNKkP771bYPTGZ5UIXqcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvBcWpI2_iafxxeAm9zWQT13QeLnhiPinX3S9myiF-HlyAcE9IxhOIcBo4v91mQJBF1yfmtC4JP8D8S1HyUSmBcq1T0YJUKBUWl8OYOkew62Yv6SZBfVLfOzPqbyHM36bWi9qGiLDoE74efUa-QfTLvhuhGo2U1Ec8T6XlunVAs0PQSAMvpao5TqpGfwjXV04frL_Le4O0exJXCLQ5D2gaUyYRtKU1CiHtMEQdh46aMnEYalh_oDEjhaZ5yvgMfXJH3dSf0YuYNJ666PZZpwi3IOUiIajvkndVvcAGiz2LF7pgi4CwUz5HhCxQuFsQh4E3pCRvEiJ8KipfThmrOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGOwN2kBe1GuxDaqoCncPAYl4awpok7pbpXjthcJtIaT8SaboJFpSNY66CetK7qjP48xtIRX_P7ay8ffvHtPNCg-tg7CN4vCR3kE4WAXUtfJ4i4MvkD-CKf1KedTyVNjXorOT-OpuBWUEUekRldUyPsw0HL4aWeSGxExIVtfO4pYonahKreY0B6n6u2kvY6wI9YESFPpVSxNaFdY_5msghBqv7A7wtKF9mX3E20HwaCHreiy5RyCKlAmZM-6-CoG3_Ppe3coCU0AhZQd4crfVxYKSyuFTkFsa06x0aSkyqK2b9Z2Zokim4oxt1tioPQ99-8kKbapM4l4xzV-Wg3qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=ZWx1A3ku88NuP532AlJ_sjQhD8mduSmxHNK5ZjDhhnNS7gf7itPZNK6VatNjmpMmvktttV87nFzXQCziasj33BClsLO41kcPgQI3INc1cGN5cypVhBwG752tu9cEXvnQo8QBPKNEA-3yATHzxMEurieEt6Eytk972hbs_BM62W1bWtwd6OsdeTadm038RwQ1GPYKduvtnFXU_NvyYpecuxkUrL7Sxcdw26Sl3SoskE9NxxNQL5BZJ2tFBu2n_tqriOFrYyHRLtC1VxGIn3T-_bW0H5Qbb9uKrVlDLVGQR4HAJx4H90d8X_8yrywjtKcoz4OBPT7_9EKvdqr1UL_ezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=ZWx1A3ku88NuP532AlJ_sjQhD8mduSmxHNK5ZjDhhnNS7gf7itPZNK6VatNjmpMmvktttV87nFzXQCziasj33BClsLO41kcPgQI3INc1cGN5cypVhBwG752tu9cEXvnQo8QBPKNEA-3yATHzxMEurieEt6Eytk972hbs_BM62W1bWtwd6OsdeTadm038RwQ1GPYKduvtnFXU_NvyYpecuxkUrL7Sxcdw26Sl3SoskE9NxxNQL5BZJ2tFBu2n_tqriOFrYyHRLtC1VxGIn3T-_bW0H5Qbb9uKrVlDLVGQR4HAJx4H90d8X_8yrywjtKcoz4OBPT7_9EKvdqr1UL_ezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzQPdY7cXF1_NImnqo-ebUYVlPITmGhv5kbcerKEymV_WQOyYIVKDDmuUtzAC3Fpk8i4xNZX5YBzDsmO1fP0vblbTjHX92exOpIwggMpVHki6czgMftl3qXQupFAmuXTagypvtz7wdvgY6ARonQPzWH95k5vCqcBh1ZkN8uRpstQ-VrdR_KPQNnG868ObYwpDjOlPFvuWWQ7UZjrQiU3Q0WRwWI68WxAR2K1S0j4Ua3vg_flfuEZTd1-uSeyAqoKBNJa-rchKT3JIteOkWHVE-R-hmrxG4gPm_UBMi94iHECpPzGErCSEoifv9g2_yH7e9t-3D-AZ4ODRa8OJMplvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6HCDzp8ktXMne6xEB2sXg7aHENEZrPqom6VwwrZkay2kByztS5nEQvAIuqgc-ZTzoC9rhBJ2vBnXpupH5fdvKwhmtHqi_Bw2zsggN8Tu0DOndtNHXZwwUcymduXl0uxdZXJdnYqW5woTGisofD2-oYAhfoAL_GnNg7ekY18FEFERe7aqAS_-5J4Xq9pyeibybyqj6loyF3Zs7FmyhY4XXrUdjyWYVeBhl_Bhmwb9gdhep1saHOWLWmMB165sOpYaDDSTFDfrfaVQtTfzp4Rb4zvPsUdr9foMsZoDiQ50ljRqCpaHl3bqjY5Uc5vJs0sGTPte9Yo-fd7OXSYygdM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxXY3npW4V9wEpnbxRVFWnA1Bc0LFXc7xUKkY1bWCOmPXZXEc8LGE2oKqficKMdd0-P0dF8rdexaT7xja8MXbRyJbuY3RR5IlqmRW--n_QnZGn32CUch7W7AmXJp2SOVR3EH_yoZuz1bqNG4Y409SyndGJgWrFiLZdM8Ch2SQe79wuIar5W0HY8-5wP7oX1K6WyVBloPZ4atPaOAper2YymFvFNCM98WEYNlj17vAqaoo2BJYU8S3BbNv7oMbxRPHuFTQkW1fszyoFZfmP8Gm6cGJW5cne1dhD1jIdFXeas0fpZ2JHaYNK4WT-sXJUYod69kXKaWeVmn64oeqnyxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeRpBDIyBsyWKRChzUF3l_3UD-ynVroTTKTIxZArNtbQtekFimgCSAJytXmuQffRDf8HPjgGpZa_TRumiMRyOCj7vXcir1pdP3vwJqBMwaYynQFoS0v2LakO2q9BHJDPkBMj_mQ445rd_2f90sPzmKsJ16wAWB48lk0bMpFxZZc4l1HI5iiR61y63NM27jJMxX7akLa7MGEds-7LKL9KJ87artWVvbGdnS_Xug5U4sAiE8rTrOqYpc_ukSM7C_eRtmZj3-jtOge37dzwfrMScR6i_jxAnHUTgY86U20LUspFZdRbLaveQN8iolI8sohBMEYAYrWpw0SCSFMDHuIWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaNAz_-YWVD5hY-kA1f7G0RFuqyamS_PAbteCDinQtxibpuEl-bFrnL6sg4Uj7j5WRt36eou6eV8DM9PiTDCgf9SqJ_AFTFjVnRcjAEs11FV5KcR0Xi02VF8rAqPGA6DdrsBlHdx9bnX2LEFaptVd6xnrKr5zKezjzPioIiDSiQoz9xJNE_JGo64-HdLI0RBV9LZku51DNSzu3_uC1K8SLOZzRz0lcTaiv68UC7q5VJN6NsRf8cq3Sh7DhPR6NIsee290TU1ufmJvX1WQK2Kj1bi8XSs3I6H1BteqA7WHKhyBJRgbBgIByEjFMEkcmZQ9f4nF6I3VWqnuZlhyQKlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=Yly6SI8rMEswlOXYE0WmJc55ZjFvt4VC2fk_zl-6F8y7SNl5DZB9EDtT8P1Ayp5tIpWeGmul4RawJmLgL-VMB_ue5YRqdFv76VJpsbhnOl6_MGSAgaRe64_oRafspTzB-X9GxiqGyUS7gEoYvqFR7tlIqj4Wiy3TsRbYtu9zvVAkUwRZbuv1RzeqKi9TDXKQzEpDKWds1tLVHLr4CRzT2DXkFuw_5f0bk0820GQdirNRGpT34Iqjy9iOnkugsOvusLPfyyC4cxKB4AAnl6oyZ0mk2vOd3PJqe0r7DJlZFFlG-HZ0zuxm5cwpQIq-8FjU-rw2Ot0Svxl_ecFtVTLSEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=Yly6SI8rMEswlOXYE0WmJc55ZjFvt4VC2fk_zl-6F8y7SNl5DZB9EDtT8P1Ayp5tIpWeGmul4RawJmLgL-VMB_ue5YRqdFv76VJpsbhnOl6_MGSAgaRe64_oRafspTzB-X9GxiqGyUS7gEoYvqFR7tlIqj4Wiy3TsRbYtu9zvVAkUwRZbuv1RzeqKi9TDXKQzEpDKWds1tLVHLr4CRzT2DXkFuw_5f0bk0820GQdirNRGpT34Iqjy9iOnkugsOvusLPfyyC4cxKB4AAnl6oyZ0mk2vOd3PJqe0r7DJlZFFlG-HZ0zuxm5cwpQIq-8FjU-rw2Ot0Svxl_ecFtVTLSEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtGE-WGjmwXBuKyrtg9pbllp8pbjSHp7GAqSEeUTdpxfFGWYOh819chwMhCjg5ZWLmNFUXbM77dogC-vVoHdSGy8cpIHjAZxvFH7LlL3jyVwA7iBw4Soh8nR5CkvY90MXq1gzlwMQJXYbrykWJ_mXVtP-uuiZi1Rf03ezMBjvr7V_-uFIhH4QRcoSJAj_Waz-y3iGZiIbbii-a603P9MpyW4ZQO4T5RvmlOib86SRO1S_WRWv7Fsaf9MY5TXY0KpSJ6gRChrHstnWq_ZMxLP6pdZQAOMMpL6aQxBQ2HbawBIQOXiEPHeJyPiqpceazJtQgrCgY_W_Z2XFIiwN5z0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcXdhwiA3d0FhJtBhfCrjmU1tSVND-3d3F5t0VcCUj_yWlt-9U5It2PJIJoTCk352Z_lcjnrINMqk0OX9_2IvRDAqSfaLo6pKancExn48ZAT9iZN0i7PR5Yg8ohuonUPrQPa5lDHUX20Zp2U41kdqBqu66eDkXZ0NRZkdr3wbpu2rK5UW4sx8Y2W34cwlj7HScuUK7xeazw9udQTPbQuZbjBkDdcxXE5CnYjZPR62V2w3MFMDO0AcLnEaL6tByCfutNY6lBiMSpOHs1PbP_CnlHFRriHUmsQ_NizMoFI6N5dK5a3XD2-46YU-MQm-6aCfznhovBdMgn54HNPudmkpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt5ezNI3hut7oWjufzyHEU_tyIlnQdQer5mR_Y8SrF4S_wVjxFKAUSoiBBVHnDgSNXm-YVkTCjOYvhK-vl2To6_iRAlPzSMTuTs6_aqMOLnu-HQUB7oJyh9valCFh2oEyUFm44AWUhiwAos0az_J0vhczGoHkRgFmK8i_Ir-aDuPijgxGunZvinxOd6pIGr8W6fC7wiUdQizkBU5OVK-4NkMqNj884YRoVq_gH0ATn3Ia74G_9jyAlmBVL8-ertrafEOP1LRJIQ6BxFBrRx-m8HM0E5Mgr9mm9FEBTY2keW-sOH2F3_m6Lt77b-h7H30qHTYIidXJg_YojncgOwZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUsslM7APiUck5xeWhku2G_s9nzhw0vpSC9FcOiBOrmM_zpOR8ctv1A4nM2-i6aVfaDUyJPXCfiRY4V0JhOeoOJ1qcXLOe__jtG_gaNCpT8whlcxjU1Gf7jeud0LFwNTH0MBPyjLOM5euovZ32i2XGIvQB3hNqWOLoYWBvdVPsGNcpa87k3y1FUbLTxv5_InI3LC4plPRCcZG7FN6sfPPFMHVMWgQnc0heQNpMx6sGgMotb2cyW1UsdguFxSazOgpoLT84dJaT3SmZF1LuziwxokMNEo-0jUz5naJvxFUpn4F1nvexsbB9d9WEZMbHapDwXQWQCg2Wrm8qze3uyXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMWj6JSyK1SRcVkNMtO-_0qCPm4vem4pRmFc6CblBAOB637FIh5kcPFoo-0f_qjDt-wH27f2y87DMLvjtogw_9xymr3fhVdAYPA8TBMEEU0ubwA612qN9mzZhkaZml5sL1dbKdSnshihzW3jxkucX10wGyTYcEd207zEVJoelqW-aEnhVlMVZOFaWJqz4fEnU5ATggxOQ-q2kxsPBQ4Zy6QJxx9amweURaIthLnkK-RuOD2QO7gb1WZyB8pL445NhzhhNVc1c38PiG6C_8XK3-CmcP7RWPEf36bLNRsFX-Cyki3f3ovmUZgg40j8CmM3snywBmZ3_3vnJ5VRJCzVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyYKAmFFRxmbp1EqWtu4EXaYbA7XcKmTUq3gki9rh6HpaTFWTi3OQbCFdq8nzHSgOidlrnBOYiFCrXCel-EQNlyfCFQuGH5ObhyjfTP6o8DZgWt0kjnSBX822NYstP1rkIG0wVpDHxiS6PX7SPL9XeSvmGvFXJHk3uCHZnpv72BSPAVEjqnHrfIuFvtW_tYjnloDjzK2oNHmalkcxT248cDnPMqlHPWXwvJ8Yo859i3DLh33yoNIdtGvtYgKLIUjmwnaj087T9cy_3qLHU4gMC0SvIqJUjQlyQUKzn7zToqkVZgPVEBEQnkiNMqy37MrXtXNLFRHnQw3R321-dBdhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4vSnM4EawaP9_vCSTYlz62j5qfeVEu-FpWLMlIxP0APjF_b3vO6cYbIdMu-DXG-uL6K7zwHsjfq-9sB0RJqGFhZYWE9Zb8iptJ2VT0yd59cQkXr6xzF4jAhYg0XihYlJAp4A5N-oWQZt4CbAR1B5oGRCB_CGrJiCG-ZlhyXXeOfdhyxEOiGZjz9YVtWkZX9hgRj-UV8IWo-HPWqVdToBN9h8MmZG0WTuaypshnbAhvy-ERPqGwvOyxJKO-18UBv9Ymqo5D48byhkOfovqECU-2SgHyCVRVHNcZKXoneFUl9GCFFwEoOCJoVne_cuz80EWITBOqvABSsnvGvzZtDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsZpBNlRC7-1ZU5QxYkcssgxbeYlgWmXZ_yZhhnTjs7NxVdKpKxwiNFL9rVnCNKVrHOB8QxM7iSJdJ8z3mRpFrLOD-pTAb5GRBWXDtzXqWyLEwfpK75ic8pBD0XKC3HY7W_8S8ULSJj-lRrfXRjjW2XIYwgvog3sKELb5OL2GvdXL2kTYtSt-Qt1Od4lFSh_3aLbdE_BMsjdZGi93li9-rqhrUIjFzhIoWx5pxP1qbghokRPfP2TEZdjzMf021zmT2I2JygL3oyrh6UIaHGF5cSoGvX_HNUanRMGuVhhFue4y0t-ajLyTn5uPNHnWTpH7yAeAtz2YDVutXyEE3CNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqlDMWtBaqcQ4h7zKukBds2Tf-FeKhhjfo63rWZrDQAZU4pIQvsiaAEnM3GLBfsHb9B5r60OElmxydyoxBc2RJ49kFGLRtGr0soPcEIUTvhRWrkftwvi-wrRVkGH8FZrbc8fWakBQC4c6Rakn3yJ9t5yf-QricRfH1d4jmn6w0aiKfM4MwRs7-CWUqYfRTM4kzzUxADBaFe1_KRCEbBBtRTUM69HNnsylhO-6kk7rJzj4t1-pxezUb5e5l30xdnh1_Qg0kEZ-0BteisJrneWMGQU3E75qcdx3xBxxgbr2JreElPBVad_1yX1jC_AhlVmoUgLPMOMGcDYEiAmkjqbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egCzGAqazb_OBYdVSe2zmq-m_J6c_nksFOpp0qWh-daRiGtPr41zDGa6f-Vn7urROAI0qxG662y2SrN67viSgb3KvkNTXXWJ1pDn6bwY8QbqlcCMEXfhN3ZsnXNKtBQ1uT_gK2s2JHhj_YWFydlDwSIbof3nlTYbE5sMiGFgU_Ip14RFko9JAvsuAqGM6ZSSzHnWTDOlPVXrCbXiSz6LmOOv08lEsZX5AO786Iq-dW6oR1A6csKs21JmRgPZh0NI0Supy00HYWgb5JTZ3GWlweS6EF6Biq3HJR-tBjSmRQ1xwdwC3kZ2FGmwssaHPQGIV8cm8FaKNd_zOtmDkk9Hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8mUM1kebI7TGu3chXFlJzl5c1rLf87bVvuzertpjGvJi2REkPLPQDY8vGZs3s3Gpp8NOMs-An50pFhM7diEKP0C_PaZywLoV45jb5MYkksd1qGhoNJ1h81wpPXxw9pFJwb5e3D_2OUJITxNYm4y--C7G3u4zJHKa4eje_HFxQRzUoTvZygNnMk4SinEl5CAau0vRpDwuGwG7ysZC12_7nKOqvNJa_GK6Mho24dTZ6cp0083nniJJPuN6tgSTSZAAj0EInCgDtnuilXZcuirekejdOhP3v6lJouapakbAmjfzwTzTzYONSwdC2uqNb0tUm2-mwEiKaN0OQpMx0vgHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xp7go0mE7xvE5Y27P5aAk1ET1sylJVC9G1oUM3vk03t24q6IqagwrM7C4hoPzabNTPK6QIuDEHZuH2sSc9q-V9clUrpuxhpL2wCjzDBESCyNZ5c-zNM0pZ46ZHO-rzbq-1UUe03FCdIBy-GEHXFSn8-ZuC1qvDBgVondIb2p0djLHefAo3fzHu6W5xBGjXv6H1Djo7_IvHJYh8ahs0ARqEoB2oQQH_eqWy1GUD-bPls-hwuopHXvJ-b4OdrySTY6nUo6s5N4KSs70Mbyd8gkamO91fJ1AU8nB-uZmavxBItyW3X4ERH5xH44Giqx4Jc4w0SFQ_ymOcES5uym65mQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzGcwfXDal0GP9C9RJeVljWrvBGiN19zzxdRap0sCVTSFCse5QOXs62ptlj91EDps_PFto-BWfjUJ_j58qQ54F8YrQDUUPMFE1UF281QCMRCr1DgJi7yIepnFLLglZ2WSdXKYjVkSHHbfx6C8qZEE0tN60UpiH-GQs2tf22UTQ-BbwM7NbzbwPnW6mCzsADtDv0BbdBizCCL2zwkTdbakNVGUxhqUhewNerqx4WWDQ3EorNcvNeLJ4CBY7p44-xvcuNn08_6ITG6b4ZAoGFS8MUmVHcgi5ETQMoAnYujbXmh-0JqMzqfNFD-orQX2dBFg11T7G8nqGa9rdMrt_pc4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=mWHEoaM_ndlyB8CmliFXWsIh1TMzNhNw5wZiVt1ihhFVDez9VBZnVDn9U1AIMvGSlxATJF047hVBt8qzFvFtzJXzBnx-gNe4GekOhlnC-mDU3OXeC5ycC3h1n0KnjU6RyOiwqk0frRXn_vkyyHUiIMuYKRPT2ota8e7D04JcVv54Rtv9Q7791ptsNwfJ_b0CtbAc1AZO2lpZudDQPOQmsEtX2gJWgbwVHuXGCvw9CW46d2h-P2ueDPDfATf4urS7MZILS6xxdXfsoybT7JSAHaGbR0vz2Y_j2yJVKtzl-qrLYIQ5149jUly8g-2X4lgxLSz-Bw_pmShRgVcDCjIUhoGLON_cJVvKbX4ADq80Mz7CJEeA_SCC7ThsXsnjg8aSy8I4yf0Sr6I1fysS6nx7CdqTBqURHcNZjTjd6pNrTm1wTFDnsu6cv0ckfhhCfqS7oSYAS75sNaOxK61q_lbiQKXGhkGYDVeedkhCuxO5m4T9SCHIQo6srEH20a-EA2Sy1ZDCzXwsFP8DBONpKN344SodBgOVyyguD0NJSiV1YWo4xx-l2UJ1Yk8ST0SzvldahBGggCeLls3nXi5SzQhI2p1Cf7Kb6OE1h8U9JJI7_DlbdDWJ9p_1C654H1vP-RWNQcFYuMi_y5MYVpxvVAY5MPKVQwKBKn142p3ZRcsUTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=mWHEoaM_ndlyB8CmliFXWsIh1TMzNhNw5wZiVt1ihhFVDez9VBZnVDn9U1AIMvGSlxATJF047hVBt8qzFvFtzJXzBnx-gNe4GekOhlnC-mDU3OXeC5ycC3h1n0KnjU6RyOiwqk0frRXn_vkyyHUiIMuYKRPT2ota8e7D04JcVv54Rtv9Q7791ptsNwfJ_b0CtbAc1AZO2lpZudDQPOQmsEtX2gJWgbwVHuXGCvw9CW46d2h-P2ueDPDfATf4urS7MZILS6xxdXfsoybT7JSAHaGbR0vz2Y_j2yJVKtzl-qrLYIQ5149jUly8g-2X4lgxLSz-Bw_pmShRgVcDCjIUhoGLON_cJVvKbX4ADq80Mz7CJEeA_SCC7ThsXsnjg8aSy8I4yf0Sr6I1fysS6nx7CdqTBqURHcNZjTjd6pNrTm1wTFDnsu6cv0ckfhhCfqS7oSYAS75sNaOxK61q_lbiQKXGhkGYDVeedkhCuxO5m4T9SCHIQo6srEH20a-EA2Sy1ZDCzXwsFP8DBONpKN344SodBgOVyyguD0NJSiV1YWo4xx-l2UJ1Yk8ST0SzvldahBGggCeLls3nXi5SzQhI2p1Cf7Kb6OE1h8U9JJI7_DlbdDWJ9p_1C654H1vP-RWNQcFYuMi_y5MYVpxvVAY5MPKVQwKBKn142p3ZRcsUTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMYxAAxu6zsW7pqgt4eFOr_bF-5E1EnchFWhABZijPWfTnh1LKtGy0drO-ZwyNHpvlgYELAdOTIyaqFEYfEZ0bkbnU-p53jTaPwIqBKYsmQdeQXwnNOZFVAMPEwCascDLbomR3KbDm-0ZNO0IIUXPtH9-_tJXZaHDwSaDPj84KZjmiMRkDHr4zQLhP5sIS1T0uhn5CYpZHDFe8N7MOOTyfhuJfXc8mTV2ow6nGyi-gwp1Tmcdzp3iqH1q8vTU5-DDjN2wSa_egEIddaFXBb8EWfSRvlc8pjpAEV_2V_pkglErytc-s89_2ZVHxItaqbF4mgDFeUcmubQ4qvvi--ZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAPBO6T0ImXU0Fa-FQREph_SelcWNDK8YR_FVxAhUkvl4McWowR326QLwEUZd3m997sNCY3F-_KxUlamKnFWmRUFyghoZlEyS58AzstA0r8o9RFRvz7EtNfue6qGAP6_1Cd1xwu4Y97pxPtHFu9VER_a65YSQP7-MFOel30NcswOWaZtDJv630IGEw5eufiq58hTLzrlymsCSLNvEi7Y3T-3zBCnvxhN25CwGdFmzJ0SQUJd1_m-EDNwkH14Exa35U0tIVrp3YmK4vAbEAlg5nLNvZ4oScu89Qjlsagu9uQVCIDnucf7MkkZuNEi9TtGO1snkmG0twLxC2WBye_Kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBoidriXprnrv_3fUqFTQApBKSlZX7F15FYNpF_hXxhwK2X7Z0xUL2OtmazNXQS9Rrvn1H24LbBLMt-BfMIzcJ99SP_WCVlpjAILOiG9dlPNnTr8wG_qxpavJjxi7cc33GFA77AqA9-bvlXMxrEuqHPAH-efLlfa0SFRTHHrtZn-bkPcCPk3NnjZjwNsbD70soigorHpdAfeuC2UO6-Pl5REnIYxphvdI1Dw610YhRcyyJHs3zlNQ98XYzw24H-e3w8D-hPjtrwXcO_uCTqgworqdFeUZF_m3jOrivFmux6F9pR3Prd6QLLMcv6VVX2JxYskwAqwAJ1AfhsQ-Eqiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptKA0GRUHbejKRrvyQtbTZBbn8fqjFVUaaoX3i-okPgpP-GE_bLk6SIBq7xoBokrz5mR0yLH38sbyeMgpBidRZr0kUqY4IcPnhH_YwCRv961qMRO-z4NPGJoxZG3nMLbjC8BSD5biN6bdlZZVVaDmv5lntnAHRUTdl5sveLnaRy3occ47llOh_og18JitW8PBOzvDuHNxhlAS1bB3GCWXs8v6HVqf5P24L9IaB8klej6I9IuQCH4F_nckZBROyRW-i3UGrnO-NoAVcT9qg25oG_nbcXHc5R_naahH7il0IPIlqaM5FxX5qOChXCnoq3vl12mehj8DYJQtSNRArZMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTGu7tBiHrvAiOHEofJyPX_l7Nif2XxJY8-Zy0JRjwK7sb-FgKRm6nxJE9WwWP3mBPU1IPABSVXWrzmSTA5_PDeBJsUAU1Jk1a4B9uq4wjmTac8VV9H3FD1FirYXhS-1IVgNSKNd3exJKVEQHxv6h9YSlZCcrjxUSE0MXWBo5CnlbexPK24Q3vHGyv2kZPp1O0NzNa1ZHZkNAHbfEU9PMEy-HvqpfN3ND2P0-Lz91JLv9zShBN2lwx1m6_rxm14PWf-rdBfT10IKyvzmp5vziK9uQ5j8DLNKkrfjavtGy8_OCT3tnOPs6XhpcZiblRWhZHxXKI70Eq-aMrca9kqeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skOn4qKCR_K_hZQR3ipvL-HcqwG_cTmfIqHiKtyO93W7FFHxHMrQ7QReF0HS985pOL67_t4roNgNS0t425eM4yMFYF5eLs0xUxwcG3ZRxBnouUfEo0ktIhoag5cQhi_BVAeFM8zemIM2Am0yXtPJub2GvMqSMKaCNIz_6Tjhbpfflrw_GyAn3ifcpYCyG_3Lj1TtiqhblP6Ukidr2doXsoWE-pRN9PEw7cVy-IPQfkaET_L7084RJYn_kcnMAD1xA6ZADRN0jzwEQeAsoU1WG7Zl5Vm9B5rM5KEnoaIJBp75iTikCLWjCAjsK7axgl9TjVwlnzxdqnTAWXtZfXDuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8WguQrtu8mF0FH_NaaSjYWYHm6tWYDtEl_tOErB1ZXU8ZQXerTHpLinCfRA1s7Bz26BMjrlw60oXByYOuJ6j-A9ZUACu30wSoTYbccCFyHTJ038Z4Y5x25uZFx7r7tmf1vXy5m9iVKSsJY_kP5R3BwFD5jU75gxpxYKXi4-bKyrMNPLBviYd4v4T1VWwwODI7dr4MuVlJVZAtQ6iCA3zvB6x1i55GVdeBGhxr3F2Hb0KemKMh21AL2GAKQhJO5tRaJVchVXOaoZFtbDK2M_9DEuG864yf0UYs4PUQBfAhINZDE6kqdNC3b2XtGasQeABjFhOtgSLmYSyXHoQrPk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV2n0XJ3G24EFFMTz2ti6eexbKhrh2LN0SqTIqFRQis1GStu4sLkUCofb0Qp4c-Eu4NykS75nO_pJMP66MgHkhw883Fqp8gXK5h-Uqh_vJOoZk-doKZ3TXyhuR-vANK3wwvzBo8htXLhqcrxBYu-u5zij_L5Gtvn1_bzoVb4zKtFxtC7lbHB-DNyGVJRbKDHP1Ioyf8h8W9TADo0i5y41cckNbx7lz-C7v0rI0QgRrosxLylsIuAxS3dUjvzEbfbbLisYvyksUiBH1JPOqSiw9A8XAf2R6t9wkVXGF5yZst-DRJO9LZBe6SuRFZke3wk6LKMMX-T3V1QXfCIBhvlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=dW_Xvr1kTGgh4rLrIdXhDRw1NvazgHmdCuhQTyDAOLHvqeQKNkxbb5_Y0g-ND4JS3PsaDxlz2rV8BgEr1Geab5Ae9ThB05dHKLlOe0Szo7PEd1rP7-vyiQvvimJ8tn_zwqNAts4bPDGsDGyyLf6QwvbSgZz5wqZ0jjlNtiGclhHtARUG2_P0DIisfoWKlxQeK17NBDuZs3XbFYfzQyhhNXZxTl5ZwjOE8j3Kl7tLvaB9JU9MwGS8bXLZkXAL276tMYQRpDhQQ62RdW2N5puWPlo-Vw1lfyPLwnO6PR0WFGMIYv-4CNCacOU3XBy3_qlj6OF7CTbU6ry7-uSZK0vtBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=dW_Xvr1kTGgh4rLrIdXhDRw1NvazgHmdCuhQTyDAOLHvqeQKNkxbb5_Y0g-ND4JS3PsaDxlz2rV8BgEr1Geab5Ae9ThB05dHKLlOe0Szo7PEd1rP7-vyiQvvimJ8tn_zwqNAts4bPDGsDGyyLf6QwvbSgZz5wqZ0jjlNtiGclhHtARUG2_P0DIisfoWKlxQeK17NBDuZs3XbFYfzQyhhNXZxTl5ZwjOE8j3Kl7tLvaB9JU9MwGS8bXLZkXAL276tMYQRpDhQQ62RdW2N5puWPlo-Vw1lfyPLwnO6PR0WFGMIYv-4CNCacOU3XBy3_qlj6OF7CTbU6ry7-uSZK0vtBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH_n6HW4S-gAMbq_gyHnxZ4VsecwLHchxtFt_NkvEn-ApHmJelzkeFEhkdDl19Bb1Myh0cXFF0Q16un3DCwDOTpjJtECKEYJW8Z2neroHxMUiy7cPL2TgGqpkA0HUKWeIFYbH7-RaZz64DnEb0214irfFnHk0C5h7T-g6__WPmXJihmDrKd1ZH_GPjd1S-z_R3xz4wSHfWLloACSfCjPoD2vr5XnyjBy3A0XIcwZS_tB-tMpY4uDrDJbNWra5qWiklsA-K6KsxQ8m6E_supTp96dHqhnmYjWIG0NeDRtAp1AH0hYjZxC8gPEscl2W5ENDM-qxLMdQBtKE_sucFYFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSCdy0UXAyK0pTvrKtIZrwwjG8aW98zxzw6Oe6aOBXwslRJxuFlKMsvE3GUhahR7EYOWpWqI1z1LbRFY8LxyPm6FRhrEuDmHYMyJZO2E5jHHTHmiPa3zeKdNVPVot_s-8Ki_HjRzGW_VjnfDlyOHrv42eycj1LdVCyf_CReGymMYfzl7l9fF6xOMNJIzni4WurqaZ7rRxBgDmx1UGmKOZTOLOZ4xloW8Pm1OwWVsd7wY8g5Vw1QApu1BpHi3FgvFGmcRoI45cJ3i0Vfy3ac54Qza0prlWSqh5ELBoL6fGBNEUwOZuQPVyaHKl-SV0Pq3oGPeH6Mbtb4QbMf-QjS2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETAtpJ-9cR7gGZabkfGJIiIqnbW_KkaxYBoLLMZ-nFOZrHm9jJUNbL1AsqOXtZ8-RZnn1JJeDZkhOJbguGFLEpdXsAl--IVnOSfZvLglNx2yct46EwOb6s-aTOhVwcWDBDXMaEvcd866J54DsD9VrWbndg2GM9254qlCIwDfiSYuhd3_URpWuScL7w6Pn-T7Ht3vI7I9EiyXrEiZbP5_gxIjpxNh-Hcfu1-Odrv0YBVKnohkqauiCbn2hALzBQFkWvmOeQAarYEX_gb0j1Crw8bdcgdDQMirLsKH2n8Gq5GBlGkJ7cb6mGfQUsnE3B3Dcl--P7Jt0J3oyy1EI0RBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZJwNQxHcpsZd6QkNOQ31drlJVQ-k1xhTwTQMjHu7OdrV3jmQ_ERwZ-P84Gu9V906OpMt8-IiT8BSYgYTA0u_U1vTffNLSUclJWbRB5fL0gYMciehpPZlGSO9q38Ig6lsHm3C9MWdw0wuUK36Ehc_yIqZWnKtEc-ZQF1B7ZKF1tkNfuu2VRkWwRbkj5etgzCVYUc2bYJH-EAng6VnYW6BS4st72onTlx_ODsTGMG314dE8K9Opm_zBiurmCuHszSUGZ8yIeZ_JK_AXv5lRNYC-w61oYm30lgHJ1rWEIc7XljOtseePp-BOkP44H_NMpWVB_TEm3yfploJuwaiKshLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkji6iRt2RPIAt0S0KATbNmCONto1ZOpDuwwD_GjH0HvFgRdGW-samQRsQgqFUuBBDxjr9LtTOltriec8ve7W6iMoFvDvFwbii9P5Jf9DkEqaWQOxNQtq_j__yF2fCmyf1rBjJPFhMcEaGxNATBUhqMOjSrMXhBLiqakOroYm8gxIu6ubh_u6KPCEH1djxjXiaLMNxmcn5ShWvm8qj01sXrJVmNdfzVLc2BjX1N2bLGxUp6waoVo1xTSjlwJt1lTwShTMFm6gKF9wgFUNG9kKmaHlnc0ZlE9-_3M201VRBpFtBjVLZOCWIFs5RDDJgDLm3vEd4yF-eTSt89km1J_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzLlgmSFVTH8msS40pCFE28YtxQWyc0nCoubCnbUUMphztFqFNZPpVqQEm4ipQ2sf09MVh5zm7sOBkdZ1L82iemMdP20CykRELlfVPTrhgqls-wTPvi_IfX1ZyEVHJs44syKIOMTetFFqZNuNcNt9JY3Dl7t7wDrqoTKXm8dTdOnHgsw0YaKFlio684t7oIKfkzYZ-xdH4tFi28g9TJAJj6cozRYTDdcxQRaaJUcFsUJ8z1L3HS_iuCKnzhAPkgQIwLz4W-K9XFmP0RppbG-Q_Fg1izgKh0yTa4YIBtA1smd6vb2Q9Aeq_gAJfwdJ3QEZXAiK5U8N_ovmKYb3geirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOWCYJXjHoez2a021JE0c5WuVyt3PnfzTg4ZerYrOhHKPN_Ix-1RFqLhiHYzYAvzttuGSTJ8Lr3e_U3qmYy5XQCkCteIAcQtgQ64rk-tXMcB5n-zknbN3f-xd6muT2VSMfvypw6GraS5i9S3GKNEnWKUb9wDrjcO1uru4yD9mXWpPaCsgUkLIr6O9IyBzxQU-C9Tk246ZhAeznP__JMo7wM2JZcgaH3RzBgznpyvC-hXUBwAX7IZ2UDKBgyKelKfF5eCA6t8LvXUzJUcK1YTDl1J-UN9tMEkKrjjSNJGejCQai3OMTexQZGF_9GvnLjvJyQe7Bn8FPca7xNwoWbl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
