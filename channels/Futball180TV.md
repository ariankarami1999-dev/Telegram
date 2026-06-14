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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 517K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 05:10:33</div>
<hr>

<div class="tg-post" id="msg-92813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/Futball180TV/92813" target="_blank">📅 05:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلللللللل اول اسکاتلندددد</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/Futball180TV/92812" target="_blank">📅 05:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n22HBSgvYmlAmbHVSZH5H4RuQ7LPZEY28wIZD2-wgchQy22Pdzo9fs6PDuciUE7xOsQ3FSbj00-ulT_ph6t6PB9Iwse5Lb5ALTgKail9WqEcjwrwmksyZOFA-0FlLxF7JZJe9KQWpSdOFoIErdf40Wwf5tLCTdnDZJZ-pq5po2j9VU3pHYMXRfRoL8VlOBs_G8Qu7ZHvRh0sKIkp8vc5UnEN6c8mOauKy3oixVxF4HlThxfJZ8B2_mhkN7MOXuKqXAjPSpoQH5jj06U6qfQhS0yZIr4yDIa9VDmI8bb3wqAJnlHzdtC92_hH1uVBuQfuJmonOEKs51tVJfFXfYbTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRkgOtT5XTHDjI4oJhYTfDkpyTG9W-2iz2FUXf0b0CdZ7EH2wjILuDUDs-_EqLLSVZ1A1n0K2Yuz8daU9mT6rFd4aBJLyS2pGw9mtu-152t5SMktULSQuSUoOm-W363rsWlTm9I1UVIQyOn1lCtlBgZgTz2j8_p8hdn3DlTO85XsLVJSdijSJzot4ZFMYdvwDRJh8Tw0o-t-ygwI9_YorfEn6kzUGKUmR4HR-lLUUCDZxKpPBH7TAM4OOynGRr-N-vBCQNqLU8QCl2wvLTolJ63JGiZ7cRJDiLbkKV-BL_Wn2ZWq5xabw5G4kSDgTYBjnYZsCXuJJ7x_sMZ2PDheHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
صندوق سرمایه‌گذاری قطر اعلام کرده که بوعلام خوخی پس از گلزنی مقابل سوئیس در جام جهانی، 3 میلیون دلار و جدیدترین رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/Futball180TV/92810" target="_blank">📅 05:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrGGGnkYYd3psCY0YqXEpkVcKL3O5e3i-7nl8MFnDsKxgCmh_gqTSGhbMQh0JKfwzLzNgLbe3_vhEqYdJftp34-x59QlYGgfJGABbpeYe1Za1SaoHBz5WWQ-I4wKzqLZ6FdUrLUwiz5OjBTXE5DrgBhbqLcgBt2eg7l-j9C8zeV4_35xOfwXYIczruHwmKBh9zo0qJuBeKE7oszF05LsZj89Qsv_MJM14-WUeoTDMp4IzDFT1ujb6lMHuXurTVKdDYKh6I3FMSSSwdtsbYMixlmVjouOcAuUtWKnea3XyLRtnAqH7OTNq3-cb_enP1SrQ7bDIWifpmB88CWBGWA6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2o81fftn4IS-H4hMtBS9OVWULixNIUAYMGIJlQnr2mZNhqP-Ih6DR_lyCdJ69kN8nzDb4P8ytSNCdVBrwzvhaB1U-1kWUmLU5F5oU10P5TSWHEp28jpuG-CWFFPMkKbldQz_EYyqtr1AFxmJEUN3iLwT2MCSk-ck_Tc19qPZ8cWgGkr91c8COolmaKohAYiudUb7aIc8hpOrEtw9qNcdeA8zo2ne3dLPaVkunNTK0viupnpyYijw7_Q06gZkel7eOz3bD22ZqybZ9M5IOfJAArjyK8Vm4J4oKkploXJKoqb46fkD8LFHQbW39SFOIlW2M-B5kVUH25yD5ArW_WA4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جو ورزشگاه قبل شروع بازی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/Futball180TV/92808" target="_blank">📅 04:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بریم سراغ بازی اسکاتلند - هائیتی</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/Futball180TV/92807" target="_blank">📅 04:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqHLT1Tw_hN7IUgkWo7FPPa_ArCnvxy-Sudg429ySBtgRPU9VXyVMyHOPwwweUYSMAyWePpK-IpZMtZOWaJcGbepawK424jQq0vLPsqa5lcQocNDq08ur1_e1uMVnqRuPQGDXDoM4HtTgU2OBzg_aPEca2z3oTGzL1OYArKwbEwa8G7GQV6bmhqsEC_vUSKUoNFxVUeVUPrX4C_KMINwOUiiJ3Qc1nrVOGiVblENPrWiwLcopjYAuCDff0_hLV_kzIFQNgPiKdRXtlLpTon6D0jnyosp02ejB6V7LMH395hfmxG51FfMd17iia72RVb8B6vmdIaKYQu6R-ZGupHrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین باری که برزیل در بازی ابتدایی خودش در مرحله گروهی جام جهانی شکست خورد به سال ۱۹۳۰ برمیگرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/92806" target="_blank">📅 04:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyUjeYv3i54sLuJrUJ2ts5wAqAcclrwxR8HaE0i2uLi8xPqppqK2Skq5IRRhYxYkSzByI1ejhBcPuXl8z1R7_xStvGUGwABXs4yPtQ9mUuZ1gycKeoQb2KWlZV-Dsa8NcZekrXJb82lQD32Lm0IbFfc1Ohy0PTAE09FqQYm2y-aiuoP1zigBo4Ina1dMyAF8yDBq-PZWUL0ioqPPv3LK_x_YCZzV3KyQFuz5MCaL-8nsVswMaQlCdWFY5nadpO0xZdfep2PAgnlu4YANVrBtqWrgb8QuoWVifRly1NaiWpfGBmSIpo4wE9T7gQXyPgVLczEA7NbzgA8X1mcQmerMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aI3mLAr0NGh11ZZuw8uItQ6gPKdAqMbHQ-RAsTgIdstglZwYfAHs4ILvoVWLH1x5xTwQlQdYtl2FydNZqf-kHxMKq6kP-XjIFu5gOKt34I47s95NfqG1Lb1FgdNn5Z5cGDBYOdbfu3gbuUBL8PFV_de8ycZBa7Qlel3LrC_IAFmDJ-1B3vjMwMDxJunq70zqCvQ136L8RjWcaG0jXnOJ_QPzpyY-JtiPO1heczCXY3Q8hw_cK2Fl6efNbSr1CfuSNxkBHKWsFaANSu-FgigZoP6m8BRr0n0PA_im9n3pNQrfQbOLTrDkOdOiJYiO5MAH9GDCTTAFCwW5rhdvvl4eWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
خلاصه کریر اندریک زیر نظر کارلتو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/92804" target="_blank">📅 04:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPt-f6wRACkKOLVA3w3i8og35fG8LMDlhDHDfS48sabiBSY1zg1trcCsJJbejf59yJMjQKxk4PgnmQzXLvy5kV6kjsEgDaUaj9KGrAb6ZcSNV3oR0u1zqOlx_ucFs-XAuij2MWy9ysmbZNJvPsiwtcckxpUTUjETqpNg0ozGHvyLRqz4hjBAylS9aZFIistOP-irqmT1nRPRNtLm9uS6vCJh5ROIAUFwZ-xZL7G9oCr1wBIAdlDaZyvvDJFzMz_YbzgoHXJ2Mx_s_hKMlabTK_wDfr5TouP6-NaMMD9jrxX0_Gpl7R2jH64nLx4FxQz2utC_T56jnxRFPwVfCy1Osw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
🇧🇷
🇲🇦
آمار تقابل برزیل و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/92803" target="_blank">📅 03:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojp1D8paeEifEzGxNljAVIpqLhBHK0DUidjc1CgI4hTaCpQP1DOZPD2oEt8Bv5xTrtCf1PAHmCfxcq6NbCF7v4lJNYA09OvS_mFadRMEFZby7WLRu57NKDDI_lZUkzQ0JvWPw1QOIipi9pxnr79KLP3cEwygdhOw2tw64hXNNW3G8ihAjdAdP-l42FiGyM8rJFMeet7PJcVUetZPe5XzcDsVSP88hBYsAq20KAHGXAdOqOKEEgWFtvX1HK04TeXGV4bDAjqPvSfO5IuX8hXBbwuXiZOmgZYNKS7Mj01JLdAHgtPAlO-DCLtMZkWgSKAdFsXMB-4vlH7cCThbBDWsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وینیسیوس بهترین بازیکن دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/92802" target="_blank">📅 03:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD5f2jWebVv9G5A1pVF-EIkpm-NHnPrcBAiuxG3O4I6K5tjo6T6oaIejrtPtm08NgnWNH4UMrmcCDexKenz1aKL-Z-Sq1BGxyVKm2Fj8rS_Qoq6F-0Q3ZgfP8YNs7Y8EHKgIAGkIQW8__SUFaQxHBHG2zGJINVysD3ZyO_3K3LN-CuefMvG4_sAhS7K2-yH_hKS7MpgjXO1iS6IsuWRpcIx3SU73l-rg0453gxpjPK8DW_cMcdDBdnfD_Jn6Sb-i2I1t5brRVbDZgepwqlZm_AUst_NslRTK3dP3MBD8h20Oteat2takSGAXwOOE0obsYQI3RwQKiTLJSYJBZpWr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمرات بازیکنان برزیل و مراکش در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/92801" target="_blank">📅 03:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شب خوش کونم از ته ته داره میسوزه
ولی بر میگردم
😭</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/92800" target="_blank">📅 03:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwjBNWCsPWhnhcOsXdJDS_VUnmX15eY5JqVt7uyEgT6QFeksKJyhO_jTTvG5NHfIhr8RjoZdDroXSqsk-4PQ0AE07yLw5p8ZwNG9XQRKtp3ew-AKllll7hEaB_xydhdtKikh6TpR8Sakw0GwmHI4gQQ8nk7zUdFdbpyay0tFwOiCfZa22e2b8Ros8Bz_IyKH6ogGGE2kLZ7GhXZ5m3URnLsDOwz_jQUS1JZnWx9ZKMQGdPrDUYVCQ0Qf_NUgapTrTC4likIkHkF2yQ0v04cNZfh-hfQ9goW_9ZwyJyM8wU8lLbBVoA-qYfQUflefw-Wkr4tkq3jrfyFnbOlYDdWwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
وینیسیوس با تعداد گل‌های رونالدینیو برای برزیل در جام‌جهانی برابر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/92799" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcNf3b1b8B22qyEu19D_t2TLkDSxK_X8Q8IKN8DA-sXWXrWeQRF67Tsv4xKUiHiLB3K6GkP0wrDj0gr6224GRdRS3E7r-sPln_8ozhsRDKj0CBJ66mF61WX1O3P4SFYq2J7sMIO1uhcEbIJ_B0JMvgua_xDe_cEqWon2rYaGVeDdWIP--fdiWEtTWSULXUGnhMskrY3TCZnNFVWGWVFewMdbHvXjzHjiNVyGu1rKsn9SeNGMj-JGP_hnA9DpQeuJFVcXIV8ijFe4CeK8R-GAJfUGZirlB-20MQzQ8bnDu_yvBR4srQyWdl7rTfOtOF6V_5TDcv10u1Ue2q7TJm2f-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|نبرد هیجان‌انگیز نایب قهرمان آفریقا با مدعی جام در روز سوم بدون برنده شد؛ برزیل برای قهرمانی در جهان نیاز به تحول اساسی دارد!
🇧🇷
برزیل
❗
-
❗
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/92798" target="_blank">📅 03:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqExGHnfvF5P0UrJ36Ot_Wd7RJFNbc56c-PF9eBaoyPVhDlGMZK66C5tniuEXubjLswmk0b_Q-9FoxhGwycVK24YG4I1-vLE-gFsPhj22GPjV0ogGd6YMMfiyOyzoJb9XYaFi7znbUESgLAx0U72p4hmVH5gtuXkLaMw9RQ10lHsfnY8KsTne8zd0PbUhNGe6IOuMtAD4_AoEAkqKgtDE9iPGzO4B1RTqZAzqDgvVVU6YhgTgU3sTwKhj3ZAqhyTJabl3aPlHQzY7xjK4PLOizPiLU3KVqoRGDQ1FYrZyGAR9iDIGy3qp8dPcz-3RFXCryCj60M7w1YCHziwPobU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGxK0gFmgLAiGfeIy_ZEMBaFWIyECnzqrx8ZEMjuvAUroZ8Kgxua7JDybgQTSV2oEAoV1Lniu20zywtU3jyLLF3Lbj36I9A1oqPFmZPHq2O8QGo2WOPsd4ZcF9z6wh_-u-38qCoyk3AlF_6cxnZJ77LZ9HxkQTRKMXZoQuPC1qB-BjocTuWDB-KIq4vGBFH4xlHXe_9T_E5pOaLguMmo0zL1hW5qK3pcfi9VfR9JFyC8LdZ3PSnEMI1gc3hUFYS5iFiK2rlPxD7oSvzxujV_Ja4y97mTyvaPJoh9dBfo0ITl6JHRHTHAJA-a4PadP-nzOglp45lh1MR6qLzVFKh3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم هائیتی و اسکاتلند
/ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/92796" target="_blank">📅 03:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بابا بزنید دیگه
🥺
🥺
🥺
🥺</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/92795" target="_blank">📅 03:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=tzIWDlavAuuaVuJbs14nyryn-fkZXMbfSFPyeBBctViJ3feAQt6BSs3-mEcsgfdTKF1oRcATGov_os64YXQJEMpgQTX7HLEd93W3ct25Gfhp9OTlKXIU0C9CtCf1CeQg5wUm3hEPvG9qbOuxRYPd0Ola1QqxS8MvhgQ5_wCN6i2XHV2BYUslTkXVibsS0v441EJVMHbXKIXr_b0_lArNSnxz_UDlKTfGpGbZpevkwkuAtIxD1h8mk1E84jCN4F9RMqsps-pVDBlEGOtSRJIf2u6C7ReqvEOfh41RY0tWhWjrl3vmMznh7oDO4Sunu-yjjJCtB8tQe3OftHsgGKxw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=tzIWDlavAuuaVuJbs14nyryn-fkZXMbfSFPyeBBctViJ3feAQt6BSs3-mEcsgfdTKF1oRcATGov_os64YXQJEMpgQTX7HLEd93W3ct25Gfhp9OTlKXIU0C9CtCf1CeQg5wUm3hEPvG9qbOuxRYPd0Ola1QqxS8MvhgQ5_wCN6i2XHV2BYUslTkXVibsS0v441EJVMHbXKIXr_b0_lArNSnxz_UDlKTfGpGbZpevkwkuAtIxD1h8mk1E84jCN4F9RMqsps-pVDBlEGOtSRJIf2u6C7ReqvEOfh41RY0tWhWjrl3vmMznh7oDO4Sunu-yjjJCtB8tQe3OftHsgGKxw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی برزیلی‌ها از گل وینیسیوس کف سائوپائولو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/92794" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Du_L2ww82aHz7K4vl9GK5SIisVRkV4hAbJ_bkWntYhniSkadi97r6Fvn4qQN1uowx506O2z2o2_P0w4kXmZEy759ZW8faFKNmHHJM48_87zC8lDKTdy2JMGT6b2eLuLbSHVwioUkkyHByIovr95KG3UcKkiBOx4pz3b0fvzlNdMJ2EznGefBvVGigl4DiEa_S-t6OOFDmWrMHb3Wttu_FXwyln9NIj6EBGjdsvD5b2pII3jpvRFG9oa8pCl6a5BJYFs7vEJ3T5LGiLMcM_DaAi_K0IFeGqoIa8R-wSNkRtgeZqoD8XuAeC3-arVIaz2UwifkEAy_14K9UviTTSO5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/92793" target="_blank">📅 02:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=vp7Dmg0hRi6WjYKTSXcYKB74fbrjni3jiWvIIE3Bu1R1v7bDkm7smNToVn90f2ksHvqh1An_1i49prYgDcNRKQfixUIRluHrDNiLpBg4gdzTQgiwsshbWwI0srOvzjh7QsBMnkGuoJVHsVYqndDSwLy2gbg56Qc39IgXr0RaUi9oT-QTf_r4pj4_eg-UY0GquiZPcuhoJczXYjK7sfEcHerTTB0om5x7qftDfrk0coRenRkz8pyiTDFK1oM4ypkVWSBTMON9GvKzDriz__L3VIwn8kHE-TmvRgXJ1PC_lSRgl9owsPj7kilxhAJuqn5XCGrU--JPE6PDw_N2fSI51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=vp7Dmg0hRi6WjYKTSXcYKB74fbrjni3jiWvIIE3Bu1R1v7bDkm7smNToVn90f2ksHvqh1An_1i49prYgDcNRKQfixUIRluHrDNiLpBg4gdzTQgiwsshbWwI0srOvzjh7QsBMnkGuoJVHsVYqndDSwLy2gbg56Qc39IgXr0RaUi9oT-QTf_r4pj4_eg-UY0GquiZPcuhoJczXYjK7sfEcHerTTB0om5x7qftDfrk0coRenRkz8pyiTDFK1oM4ypkVWSBTMON9GvKzDriz__L3VIwn8kHE-TmvRgXJ1PC_lSRgl9owsPj7kilxhAJuqn5XCGrU--JPE6PDw_N2fSI51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه مشکوک نیمه‌اول بازی که اشرف اخراج نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/92792" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/92791" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lG3OK_8iBe4x39wWpEu3KQ0NhPdjOhW7aHgomWDgntsEWSrKSUT2ul-msZ_rbYERE2ekQdguYK4XzK2wJqA2RY1NLfSqcfqSLH40yGipHA2dQRFhhQgqPmxPfEyz6THPAemdGV2ImQPdbBDQg7b3KOSdGldpFzcxvEdID1jyUjG0ZuzH7w_YhRXpbvhCP_R3xcanbfIhejE61lMS2cEXv30iL5E3SM2HlKHujXYpme6rNHF20zuDqw4Qb284K8A3tZK19qj9v6cvDYfhH3NIbxdpvjK5L_2DtYxKUD9d2K5uTUqW_XhmDzuhyi9vVTS82J2h6wn_jgleadxGPvxP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/92790" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KABpb6EQFAr-XwHzmSXW8nKXdzJIy8ONANpBd9USwIIKWrOvabNnX-5A9kGyqarHjKlgmA73bwG6JG5EgQX3ZZWypJRampugOApbUlpUXmKGskAfEnySJ4rBtx2gpbxxnTzes6ge7QUh_qZwGM3NZ5ivXprMY5VPaVPRaGQD4nVpamGQ1s1P3NVDU6R_FJ8Bii3K-dCqrr9KCos_G1VH9Gw_EZi8to12tshdwHjIBHpQl_nfeL4ZeZ0m5pcOOQuvnxwqNx7hjSrRb5lnuit6O6phpgOZXGWnTYJ79V7IR0bDZnBvZ355VBgnwdlb1c63xV6ac2t-arod28thgMSfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
آرشیو‌وار: اشرف‌حکیمی بخاطر این تکل باید از زمین مسابقه اخراج می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/92789" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آغاز نیمه‌دوم</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/92788" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5kApusIini9AFxlr3L5RTznIvOh4eEonb_jpGMLAh2toHzRuO35Usuk1N8QWkcuT2CAT89y9rxPoK_XnwXqrP1zuX53jS9DWMnVytMQnQvFaxC9HXvhdWrf5b6QljjxBiZOn_rf3IgTi7q7kntyUhglExObYYuhSSwtE3kfh2FbaTv_s6LnVwFpmRv9YmjxmxfVj1uM1T87950l68jbCTpuGXE3ClO1bjUE-_wRV9QfyAHauyPXqcuccqDZJ_8V1SvD9D0rAs0w9rZ7UW95D7dsfnm8rRSRThxLiYzFSHIfFQQU6iWg7tWiK0KJWSaN2-EflzevYmw9BsRrowl7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
آرشیو‌وار: اشرف‌حکیمی بخاطر این تکل باید از زمین مسابقه اخراج می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/92787" target="_blank">📅 02:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3tTDv5HAAmZtYr8SLUnorpXO1ZIlxLi2ZRnz6eGzpyrotwz1BmXTMqFYos-WWXnt7OVEySzirrTaFgMkHxqLPfcKWHWXM9cOeh0AcDWrF0VoyVD6dOMEtkTTU4mpgyJXNP2U2CzjbW0-qsMWmtTOBjRdiNc8PgJVEi-QgkvyhmtV2xMqfB1-ntOFCG0-gxw4fGSc99idq2q7htFNN-qo8L1Q3ctmM2z3uFMAmY5vRWZjpFfUM15V_kMBpFTx9Vi0LRmTzGicJK6kU3cgMg9v7_O8z27dgMAPkyPhRZ7XnEL_S7DFW6arspY7mdNwP2X4qbfnrpW3kWg_pBdJcuD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92786" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh1kez6hGCrUV49gWjUmX8yv5z3jWU9qKEVnZABKI--N11wOllQfWiiuitV0Qy-MWBsVyQeAg4FY0EN0D3E041Zug4dancliY9e2PqYRzwekGWC_4i9CQfCxNcUrdI7nDogiCle6JWb684UENApCcjM5_xvzMeRx-THWdjADkGSqq_ZYfTHAnWNzJUOS8Gvbo2ACrvjsX5vE-G5Yrruzze6_UnpN0CuAri6FY1PtDegKkZ4dNZOfdmmWyP6qAMq9U9CwxratfTD6Uq2zYqWFeoGvrMSVjWU5lI7FBzE-np2aVtezWw-j99Zu3xNiCmMktsRUR8qtE_q3L8tSwr8qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار وینیسیوس در جام های جهانی :
5 بازی
2 گل
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92785" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول؛ برزیل
😃
-
😃
مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92784" target="_blank">📅 02:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سوپر سیو بونو نزاشت برزیل دومی رو بزنه</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92783" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برزیل داشتتتت میزدددددد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92782" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92781" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ایبانیز هم کارت گرفت از اون بازیهاس که احتمالا اخراجی بده</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92780" target="_blank">📅 02:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwGEtrgBI178E9xFjo5Csls_q3Du1vFo_oWANyQTllkp5ZtDdLLHKCLyoCzpKW126kybU_RHj2A58W6zIrsg_yhBJCbt_ZAUM-FFQf2agV4U_rgLyuV-5M-6FenKmhss8IwOUjwNm3unQnhNi_t5pPoLBEDSA4UJdYY3ai-DiaMhcBZU3DHGb0AI9E2R9T5pmulXwJpuDS_sYrebXYq7I2jrNeoaS5VuPSbS684FYUty9PzlBZBPZCoeQcejSs0xk9TammlX3044LYSVLDh6bsRdDNyVY_93-Ea3lL3BYtJH6Z9YPjWRGpUO-XQrYKwOyTMXqh7DErKSljmaYBY3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/92778" target="_blank">📅 02:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کاسمیرو کارت گرفت</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92777" target="_blank">📅 02:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92776" target="_blank">📅 02:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92775">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لبم به لبااااات وینینینننننییییییییی</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92775" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92774">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چه گلییییییی زددددددد
😐
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/92774" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92773">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رحمت تو کونش عروسیه
🤣
🤣</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92773" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92770">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وینیسیوس
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92770" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92769">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلللللل برزیل بازی رو مساوی کرد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/92769" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92768">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برزیللللللللل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92768" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYekJ7lZW1nGAFn9mkR1sCjWPKvWc3c2kXTDgjWjQ991t_OoEDcSjnxjUCMWGnQRjinKpVoEDSO5vAYY8WPW0UVQ5DGCw6rufhf0zkrnIFLo_mF3c_dCwkatV2kuE5QT-Moell0rRaFUMPHu8bqs-y4KNCTb8AgLMBuOfXLnADoUlqulpq6XNE-q2hzLToKvv0qua6YsBuY9CzMCTZViKCQ5QBIbYSFu3WlMXo3lbnkFJ0JEtY9vY5yLeC-PnUe6dTZdlRQ7sxf8zk1bVl1gY4oqzcdzWImP5BLIU612jImctObHacF7E0sS-Z_ijWACwMtDvJrH1fT-TKz_y4JBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92766" target="_blank">📅 02:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/92765" target="_blank">📅 02:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/92764" target="_blank">📅 01:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92763" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92762" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92760" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">😡
😡
😡
😡</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92759" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اقاااااا کیرم تو ابروهاااااتتتتتتتتتتت</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/92754" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسماعیللللللللل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92753" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92752" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ضربه پاکتاااا گلللل نشددددد</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92751" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92750" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برزیل بازیو‌ دستش گرفته</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/92749" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این تیاگو مهاجم برزیل شاید فک کنید نزدیک ۴۰ سالگی باشه ولی ۲۴ سالشه فقط
😐</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92748" target="_blank">📅 01:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92747" target="_blank">📅 01:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کیرم تو کله کچلششششش
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92746" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مهاجم جقی برزیل چرا نزددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92745" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/92744" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تا الان مراکش ۶ شوت
برزیل ۱ شوت
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/92743" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/92742" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92741" target="_blank">📅 01:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این چه بازییه اقای انجلوتی اخه
😑</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/92740" target="_blank">📅 01:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بازی خیلی پر سرعتهههههه</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92739" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رافینیا داشت میزددددد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/92738" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92737" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92736" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کم‌کم بریم سراغ بازی حساس امشببببب</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92730" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آقا دایرکت رو هم تا بعد بازی باز کردیم
هر بازی مهم تا بعد بازی دایرکت باز میشه
حال کنییییییید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92729" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
خانواده وینیسیوس در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/92727" target="_blank">📅 01:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيمار همراه با تراویس اسکات از روی سکو ها قراره بازیو ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/92726" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92725">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92725" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2DYcKKtfgj1z-UbOUUS5WuREk2h_ulIK5is3DCsHUHHwstEzhbZyuakkrrgutfJPNTEgPpEdRJjocRRN0JWssR0pp63FFNL0ZsigVJHXncz4LPbByuJ6tjdJbAPtnFVZMItnPGdQXzMMzv5T9jc0YeGw1ooAxRBe21etkkrVz8iIUimP5tMMPO6R3fzO5YHwOG8PqJgXOv7OtXbxeE41Zrs2xWLeYFSo5jzsLkdrF_qgsUxzMJ0vKWJ2pCrY2rgGInCrkwYn7VdGnOrtBvqG9fFSI6BkZUW1BQGSkXErrGkjGYnQXdkbLeNwE0npQTpQCkETY9JOBKAQ1OnT_oKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkEK4PkXAYoK_XWBcS8r7QWAN-iYMjuUXckTz9ArE66SbGi2fUpyW8zeiDY8ulFdsH6F7DJPEvJhhH_c6es0EbaykFqLiA4HTNmnWO43KeuZxEmTEK7tu0FOd2GBQYwE5HHcElZ70SG7A6eDctTuggA5oLGT8blhbeKozFEib5KGxsfMvfn93NvtptCJsseQphIIkg3rj0nWcxRUkUVzxeqU3cHyLhm1CLESekgNAoioRGa0Ydb0KEQc4IA2w-Mup80vX2Gzwo_-mibE333xAsRc3w8K6FO2oQB-pd_mXE-_Aa5z9RGkBh9VzPc7TiZ7oROGPQo30ZQSCdJihpJ4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfRsR6ACbZAU9okI7WBsrgqxqkz0YUAENPVx0q7CSOrpnN1Q8OpsSOQ6SkagEjOfURE8pmQ97811pqVwN7YW_JkDVwllQCCjLYi3_L-XC_W6uK7O8XojFCeitLY5YGTF07IXcQq0CpldRJMoYsXuVm0L7dtu06Lm-0nbllrYlriFXKVOihhLa5QN3sU_sPXdkJc9Pyft3ulul-HZjdHOawIuYElgiSWmzn-t-jtvZAte_wpDNEc_d3DlaAQbfZVQQZSRBpsUbg-V2tHZKlP_cJnk5QNN9uSuRzpTeZz0zUJ2qMTnAU-scHcF7xNUe0PTf3ZjW-b2fQcHy-F0qMSrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/em3guflenZzH5Evh6Of0OqsPED9W0AwO-4gUa8PblRjP0RMt8CeuyY0WKHbxAz7PBk-tppLAqBTMJZkUxcCgrhONSOU860AVRZsTAn758HGe2r80luT9ILqlqZJPLzHBB_PxSwk8IQ0DVkBmXBEYDrd33hPaoUx1saiS58UO8BD2CyPSjiTwuKLqYMVpR8bPRAZBoYiQS9ZGARzkqJM23WP1syYJ63GVaocXi2VGV-tkZr1UWPmHHkZ0b17Vb778p2TNCz1I5rPfLLYI-6H7wZOvaRHkDTjtXnXErfZpZeFkqtQ4Hza_VWsrPyaMjYzGhIun7uiekWIPqfQPiBCS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9u-2MZXL6hxNjav8l1qhHVxfI-Qd5RT6kZyPB4sWraLaFixBPJQzadVlJLV3ikQyUWSx-mVMsM4cbSjCzlWOJDAdREi6XKGPPG4JPE3WHKmpakTwRbW7nufVNiD5GAJZmPcG6HjPlsQ2AIyj4aIUd1HVOw0Scn4m4r4rCFqnsT8Ca8eeqvUmR4h6vW8YMZwFqxXht6IXcMY_Gl151Mu61KkOJ3GrP31j8cnbeTDGhl4x5GGRf1HCr53bYHfNWonuzwHvUMQEu8FRs-wpXLhbFW7I9ZmGrFXHdcpskZLnNhx21I8ekoHPssNiA8dD6LnEQb7gXdxvB-2MTfuI81Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHbyASEptNl974eFL2PeBO30vtYtRFNrcU8qv9tCmN7YtZKXLqxUvF3o_TLJIHOo5MmAR4toNXaGDGF-EytsXtVN-XXemwuO4ax4tGfeKtfwyVshMD_Jo9wjwdsrZ5Xd7lYcpbbevx0VarnPkEjgwCiEZg7juYvVv3MT5W6hb5oBIFb5-GLOu2S954ZJzweTDvfctJRExu7_0USlMW1iSOpadYwXxBiHzO-abC2SJIvl5Wcr45im0MjgvG9NS80BVw5fONQitvtJKNemJYukEDipYn-UB4AdMla9QoKv3Vv7hSFu5M-o1xfLxXodzkmod_JOdfqs1zk4ZDrWdnsydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plFa8MsxlqPLz_1VcSDFUAtENL9UNBqN3zFjwilJbXIYnlyimUiw7WbPUN1Akxnx1Hmt5Gt7vQ_Uv3eFM4F-TlEvPT__1cTbYU8MJ3klfg8BP6Stw2IER-9ZeqNouRjrk8OQx7H6Wg309AfO6dQR7GLxUZX0UV6pNNDulCEaGrEyrIvLDeMHbHIH8tomqj9VS5MbF0WL9JQyX9zdohlxNAnT6z5fpTuhxle3VdZGdkyZuAyDRN3c7pYlsEZ9E13JTtitZF5N1cEM_S849nXP62HacSPxLfyJIES1MLmgWG2EXaUsRPqCQbu1beRSPN7L6porwKhjtvzQCP9hikNyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjOcXozHOW-c-z88z94pmxD_94FNyKmDouNzSrBOd-1bvBin6ad_5v3cpU9Fw2j7SZgZXAq6_Tfi0IM3D0VTxTdNmCt0P0w6NRSyY-Q0tO9Q7Vcq57hmqV8v3Px0xMlbcERVY6rXg4rMMMwXu8OEYnnM72DtMmGMnmAB14m5urcDwoEuUBPbS4UQpmMVIwYzk5yolZePGajV1Pc-YcPJJ-lth1rsECXgnW0jtJ7IE4R63O_1Jy0aAYqoKGqr9x41fpXUnncW-zKJV4zjQu217bemp9C-SROi7OLGGW_emaDMTHCSkuBPiEDTZ4EvoWbDh-3coTZuIv7hlMTW_C1gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FprqC5mEfXUKsQmpa4Sx4IFtPhszlZxoI_gZrvGWXZFpsA4s-XCDRC0eAszql5710omSgZ-Qn7WN3gonRXAHP6ewRY1Zz9_LiadNWyqtrOIr1qVDpt4QqRtoZdmoss_scX67vcxRZK5vWPkWzwPj6nrOJn8n08DKIT5ZuG--y8xcLqnBAlu3DUeZPWjBC-fc_LjQarMFQxCE5ESwCJJn6TK_nH6isekIA3fm2G0a8aRj2vqwslLxAAEdyr1coCEnyC-xxDaIRTgO79M5Li-MEsfGXSqw2msiNQoeLpAcdwSm9rshqEMDFXqzN7IRNV2D81GasAzawCdMWTPIfMC_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب برای نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/92716" target="_blank">📅 01:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
حاجی ینی ریدمممممم
😂
😂
😂
ابوطالب‌حسینی امشب شیث‌رضایی رو‌ دعوت کرده بود بعد داشت فضا رو احساسی می‌کرد که مثلا شیث فکر کنه مادرش تو استودیو حضور داره یهو از ممد نصرتی رونمایی کرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92715" target="_blank">📅 01:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhWET-xLm_BQVK0ia0joi7Evx9VNW53ij3RYVXQyH0sP5s-tistnnT_Bko4ruDCSyQ_wAvdyLkrlSvwb1guieIx66cf_x5ym0VK4D8E_Kzw9Z3iqjhV2pxh6tp1A40NyQ-ezYHQTVHb9oycj0-kfFaV8XY5eFlqhOK_Bl5WX72CejWDiYrva6QlJPmgZUZeRYv1fqTpKgQv7hdaUY7bQU5_dKZrrQDueuT6A4dfgiQw1XBzeA5SkzOt-isPT_e90KBmfJ6nPqpDkU1BqJxnYA7eJ3AfeNlLpIeem8vhU00Kd7zZ98Gsz8ZSiWDeVBKj530kgs8_bApudrFA51j2rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇰🇷
🙂
تو حاشیه تمرینات امروز، بازیکن کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه نفر از کادرفنی این تیم اومد گوشیشو ازش گرفت
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92714" target="_blank">📅 01:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
آقااااا جیمی‌جامپ بازی قبلی رو دریابیددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/92713" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
هواداران اسکاتلندی در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92712" target="_blank">📅 01:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnMKQ3WxWTIFgSvWVGiLgFimE0tgWjnUXQbijfRTpLKUr_GgKKM4ZxzMVrkY5rxAlrBwyJvdVGQlAXy6reki-M1Ja__ZPW2D0XFK_TmZPRbrPdlB-Ydhz0zP5FOhRSt_kXfCyffElwsBNXS9_FafNbdOrU2BEUgVVIRh98FnBAADmnALCOJhFZpAkt2M9B3IUnAGn8N2h1ZwikOrIlSLLydkk-80OrMFYtfQB6WhHNQTDwrZtq6fVMAZazL3vcPcQ_t6OyVPrQ4_21m95YRlhMq9Yf9pzaZc6q5Hmq5YTysTK2veTRcll1Q4MZOQqfmLxW4errMO3gT6no_8s9kK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92711" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwD3b4yajv_dy-FzQ_HQVrgXqn-U17dqzHfIaScRXNCfaWbfgW0nGm09rdGQ8gpYQKvwZtRYQtu07DcQfyiL82X0kgqoqMIBXSzYZe0UIEoJZ0WJCd40VQ6SDjE2te-wiidovzTrpkgjauVg4v0uuWmzz2_Ls7a0NWhc_VfjBDca_e4w0Btz42gjV9hJJMb0Z7kqCulh1VYFPWAUBi4PqKdFohjD60v8WG6lbvyM79_NNZ4eiV_LD57-L28EbZCdi7VNljQ4nAtWUrmrn_A4v3N4lVxAtpabvGq8aEkF1I9d3zac7NpI-G7HTeT0e4UuOGZ2IlmJPyNibIJCVmIq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92710" target="_blank">📅 01:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMYUGoNPEY8fHDIX9aXJAVrvhH4em2MV_QONG19bCJlamgUtyo6cnwAygtIJzG5gVW_pJYBh0NpZHI2sPJDlnSw4-kbfFXorKAn_kaN0ZoUwuXNr1lpHaKFGWoHdXeiN35-9OPaU6XTUN-KAnAiD6_n6a0IrwzcrRgpfCv0c4WcU-Xv-zF5DNqPlJQgog3eW--7Vb5k0wrfQ82PpgKabG3z3F4U4DuNunPtnDVhQpRqDe9gut0ZOo0d4_ynP77EPnqEvhuI9ut_ZJqGMWUhXJllHJ7f7ksrnZlbxZe-5F9Gs-PL9mqX-IhMrpI8pjGAA0ndJoQSjv7MNw3hXdsoN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92709" target="_blank">📅 01:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAFMT92UD7ZNYTjdhG3ieXbN3gWNhyTzufWXewcAGkULZJMgE563SukIRWjm3L9vwluQt8euBky-3srrxYyz83Ilj1-QpKT1EPHYr9jLL_m4WmzPcoARpBhMJMHj8-vttrIHrGcMp_Tm3e28ZLB8htP_u7VtIyIgTRZXejPnmF8lED4WoWXLMkthe5GRJwh3mTK-OBkpD1Gc4mbQIbW8z0wmDxL44fU1MvVDehCI5TT59gUY3CZ8sAibL3iw-VFqsW-xW5PBsfdZj65i3dYe0y_73ZHjZbvEmH4eGoGp_4CPGjCaqqPeDX-uxmBEgRxXFz1n21gu9IZMSLU7-J6_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از نیمار دوست داشتنی قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92708" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlHyCtz9o4bUoD6uCMAOyb5dFxp3y_myHsDl5rRVHeiGJYgq1v0KyV9JMXGokQZQm7kgBdyZVnbrsn2TKug-22rh1Bme2zn7L6POO1l7ccKeQmlEZWjrUEDm0r1K79ogM4y8ywMhg__O118VhjXjCfiMDJHPx09Qgb_TpH7TpoK3RL4fT7-tyyhSr5xlLDegAut_fxPY0As9b7YFAf1red4h2h5vaJRMu721C44Z12_kwmhE_z6szlzzkGDA-WjDrsqtgg1LkJ51kg93BnspWvxSH5GLgFfLPo4hcg7C06CKhfnYnbXZIZ-mq33xL2ODp5EP8180VQiTant7X7itMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92707" target="_blank">📅 00:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqwCHkKNRYRLQKzqOdOugicvbovkdGBsocde1J50yABTlF6ErePgpkYV0_5C4REDZMIvh5Fi1AFIEOO_9S3hVlIIa4B44wAF2ZFOVa74NDpf58nLu93vZ4batPNV0voEC6I0k_wOqn3JyXyPZCNkD-_zVjOcn2XZOJm2DH873ihINkvjEiHO0W1yUUvP5NGhmIiCzsvP1JLc0c1gawTIghiDnnh6CGzN-rcHHzIEYvgzd-n2q8m10QCd1qgco9HN_Cu769QPGHV99ETyCX_kLx-ewO0Kd5bf5d18YqRMxRP7UG0Wbq2CySuE_Vw6D9wMVEW9nwWtUv_2-fvLcOggfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات گنگ از اشرف حکیمی قبل از بازی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92706" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0Js7klBcJGDbi9xC_pbZuOJwzjt2_qpsjyUIsCoq7KQEhw6LyT9gG8nP5tLEZ1PlIFAIALPP_sxWQtDZnntPY83W3bp-dVSO-hQ9SPY5exUC4DP01oWMrT_gGAYIngSSFAvAkhpwJo5DsQM5AcUUwg_Sw8bq0to-ku8fjrbZEeXHIxdrsMm1NOw4QsR8879YjgzFySS3rjPeTPDzv3UZ70J34jnZj722F6xZ6PI4OYvFUDl9GvAj9b7OCPUjZIuIBOBoAtIOt6ca5QnUu81ctoqGypDXp41I0OkQXPbWgUMq3YndogBcHyAwKBObPv-5pb63JvYpsrBcFhMTG2u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🏆
جدول دیدنی گروه B جام‌جهانی در پایان هفته‌اول مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92704" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewk-vRmtKAw37h08qKGMXGQxyF9GW9SmF9_dKAeLJPm1pBtqm3Cp1IAnGBpkxa6yaqg_k8gCajvycWq-16nfZolXmju-yOljZ_NIfMSZI2iEjtwE3wsZ6JVsymcemRVKTPtHNDLd_4_-5_ggqZGoUIH1Phkm_sRfdYbnSJsuJ1OKeuAFj-E0Cfl4w2bTsjPXfC0UIBov15jOqW55j-CSuqi73IDxxXBttluhdiYtw-2UNyvRY341ZelTG_vo4DZFMDJGV7uSn930ys17fxiitzXE96DGY4vh7WqfCt3KGE-6jdVDfvxSdQzY6JeTEbHYlBafIVf_41qEw-dUEqx2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92703" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpct1ZMp-FXduVr10ux0MyySYHOH92zzio65s2QuMLbcsj_bZz2G3lnD9E3vmb9XMseiau9hZLdrOiOKDmICKBBYy2qQ9QrPH__JtGdzcqyD_OKkb87aJ-OHZmWYsNPuqVrVDUEpOqg1zUsGMD1UisxWr8AVEIgEqp1PW3aN_7D98abyRxOnffw64RuDbo6sItq2gG9rpKVLX8I67bSkwfRBhKrvBWXRuol02BvwQlIognYiDlpSvCxkE8k5CMm0kLGjMOzbpE_QRdXSMhcNMPUDNW-ByuHSPH6By7Xz9wH-lo38U8nFvw0EwhgPEcg7Hb62qDi1k9spITj9oobhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇶🇦
#فکت
؛ بوعالم خوخی دومین بازیکن قطری تاریخه که موفق به گلزنی در جام‌جهانی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92702" target="_blank">📅 00:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92701" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5Q8TxG-lgBDyU74IQmxBrTXwGlG5W0ebv0EK8YEZ6uCnvePL7angvBxB-zDjSVL4o_WRBuVhuwJeVN0UDsaz3PJxu4ObFqx2uVrFq0yzq5dF_dzWWQwm1UGIRMUkY5ouJo8CEj6zxpz1CaExOxVPoggLwLCrq712UJSGTvS7xyQSCNE3msVwI3JpX0-gA8ljW9ok2wjRYBjeqOuEEohbXd6TvmlDKFiLAeqzchtCMpYF2rtZkYyBsgSKcAu6m30HnbLO17CpNCtYG1Bd_ZK7KsTT_rbdUuNbDhuHp_o4-WmgkcULWTxcM6ayIyOg5wgdb78Q_qEZJqNPp6Jv5DHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92700" target="_blank">📅 00:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIZ_gAHY-j62khg7axr-BhRhoNXpQnqhpGlLFZ6GMymDHB2i8rnfPOjNNog6OYDJbsMczhHZRlt53Mk5HJmpKvuPDJyUEx1Kg8spKUtwcgZml5OGKm5vDnRSPqVSfBhJdCc9Z82gILuhWNQWwnQh0qpMgXxeVN7n360UQkIQZTD9mVVwREiYhch1N18T36PCMFgpLvwdnGnx8y8YdW6jGU6YY15wyoDFilkxy9jP0NVS1BTsQA-GCYiTiDIbJGzWSD4vhPmQdoCBcFoB6uMhMAoIoMuhPDPjkYQpR0p4Ip_MSJjbIe_zqEk6rSyG1oWUr0MK60FPRosWpc9EFXn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92699" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بازیکنای قطر بعد از بازی ریختن وسط زمین
😂
😂</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92698" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92697" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92696">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سوئیس کیری کیری نبردددددد
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92696" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92695">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اللههههههه اکبرررررررر
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92695" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92694">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یا خدااااااا
🔥
🔥
🔥
🔥
😐
😐
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92694" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چه دقیقه اییییییییییبی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92692" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پشمام قطر گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92691" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قطررررررررر زدددددددد
🔥
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/92690" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گللللللل قطر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92689" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92688" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYmpeguBhEcXqvB4ZO6MjdOSWSYEZwnAfeQSaLB6wIEWuVvD2VzhqLFSzoDztDj3tiMgF0aYtiYPuGPIqdbvgiDLS2yx1KcUrgK3I0V4Ebp3Tv7fEDAKLe-DGMDDDhmwqXhYimTobUCTcawTOkmywoEGVYFDUw_TjoSI8fjFaJlVPPqQ8xB6j3_GlHXlKf3_T8nnObzFCex5bPd63l91qEzyJeOyV4LdiP1jom2u9XwowMLxOdvv7pQMBVGRTkotRriB5bbwVmYGV0HHa6ZSZildrt9xidUnJlZo-OtWVLC_OuW_EWMtQiQZVrR6cUc6egHz4PQF_TR3PoGkZqsMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر انگار نه انگار 41 سالشه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92687" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بازیکنای سوئیس تو بازی امشب عجیب کص پا بودن وگرنه نتیجه جور دیگه رقم میخورد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92685" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92684">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmWXXxOsfnUmnSapoW1PIiL4YQz2lRy3vRm16DUnxUl-79DG6HVZvrri0g2tfQMCwIPbx8UuvF7weNKOpPiYB8G0_PNsawCma1h7sWqSVwFABnUdFdYJxj7bJG_i6V-AfpqnZYyaCLfU3mHl6ZFzduAHmgAPEOQBq6KRe0MFPbVUc4n4MNIVReeEyvhEkyVqBiAW2HJPhj49oaIGg3XRMTdI2AuQ5n8KM1k3-Jx9SF5RbAS_cq4WKTaEIk-mG5hxm8b1BDy2B5-0pQgrjiVo9mXO8yrAR8kpbCgz1vNMu9rWRzVl11ZvVlptYlQsBGbTs4JzPnhVSfPJH02nT5UaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🏆
کلوپ در مورد کولینگ بریک:
فوتبال گروگان مدیران اجرایی شده که تو دفتر‌های  خنک و مجهز خودشون نشستن. این وقفه‌ها رو به عنوان «سپر حفاظت از سلامت بازیکنان» و مبارزه با گرما معرفی کردن، اما در واقعیت قفس طلایی برای اسپانسرها هستن.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92684" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
