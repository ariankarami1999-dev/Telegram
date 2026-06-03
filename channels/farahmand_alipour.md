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
<img src="https://cdn4.telesco.pe/file/XmOr1_SGKVCUaNaqu2FltioBJuIZEJDMvTaj8WaZ_VlYZEQox_gSTJIlPyRFauox_wdU2ZzdhmSLoYVk9DqdVR1Pw7hMHYS8EF-k29xm3ed3BFmhRt8qDgHkok3EWVjKRDfbc4_-QrLgU5a6ukr_RqeNre62eU9OXWQHN9ieJ0g3kTh1aPdebfT7dtpATBApRiWGY_ik-pbbSIeqtSy41b_wRcUMoKY8ac1d1XYBDY_FCf6yseD3OxX_azLiPDLydKntydCLB9jr0of7xC1paQF5IwAozQsjp9998DgAwlm59HNvPTUBKxSYpq-MuIuVNZPF3lIDurH2GxeZrsn3Mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7MSmD4ceg44KxOVt_gVCsntJEWKwc2FX31xcKBwYnKqeYikgwIdPMWEs-InCiCL_kPIN9qORACCUY7Cab7C6lec2w_dcDAUuaY2cXJwyuALsygLtEhOzGWwrj-XBxHPIVQ93QiqGBeygduhDOxKswXRP395TaUCj3t2Eumfv2-J8-oHtpFoM-Xk2aBtCX_EpyZMOGdqSkmlyKCVbhdR1o99Em93pBqWyo2icaCTFOlFrQMY8_KNIPpBLkmyz_26qvVmBaTLXHDLPPcxHkqiHwqCFgkjs38XfGPri4HFaoWS7FXWQyJSQj5X8sQDXwIkb88FuKIaGG9ZJqBcDtWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=btNb9eqeRBLLia0qoB07j12joadq3NuYsf_q51jIvDCiTQDRssOmto6P17t5I8v_ms9WH_uIqTkQrYqpbGjEcmFXsmNA4-sEnMAVumdnTbk4T98RAL5fBNCgxhVK73UkJJX-S_8WVxSCBlZHtPjsCTDqo1zpDit6t4yKGTK-mfdxCbqYdDdfNtb3LDnQf5l7MUjFPUk5hQFRbSEgj_OdwSyiwo6i7iIQ40h7tdEggO7l3zpf_P2m3B4SolHRRx-mkSD-AV6t6uAi2dxT8MoTjXz3M_JEoVa7inZnWR0i6k1UA-Rbrqig_X3h3uLMVZY1TVDoMu2JlJFgwj9-8AdE4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=btNb9eqeRBLLia0qoB07j12joadq3NuYsf_q51jIvDCiTQDRssOmto6P17t5I8v_ms9WH_uIqTkQrYqpbGjEcmFXsmNA4-sEnMAVumdnTbk4T98RAL5fBNCgxhVK73UkJJX-S_8WVxSCBlZHtPjsCTDqo1zpDit6t4yKGTK-mfdxCbqYdDdfNtb3LDnQf5l7MUjFPUk5hQFRbSEgj_OdwSyiwo6i7iIQ40h7tdEggO7l3zpf_P2m3B4SolHRRx-mkSD-AV6t6uAi2dxT8MoTjXz3M_JEoVa7inZnWR0i6k1UA-Rbrqig_X3h3uLMVZY1TVDoMu2JlJFgwj9-8AdE4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOd_FPmjDaVIglxjgZJOkpfDlQ1-h-T35qIZ159v-JWrrN8OKnKKbFHcIfuVQnvAs9ksVI-VgYvdfLv43Dr3vM-PZosCBzyZ5pzfpLjpfUiNA6xl5tukbM11wbElyFlJ8B0oTEqspul1ggtq5loaQwl0o3ZYk9isg0GMQCwKSbl8ToEUAQYKgY6rGP7Wq3vG40-hV03NnWfBJ0oQ6H9JKuqi03Bl63RrOPiBhkxgmc2_O_CAIXOCvFAw6t9eOospGvXx679NV--D5enrhkDhXektvc5s3onaraEo3esvESH3Dc_dL6fWTzpvS1gA794A8m33YD9bwrTWtw2L4NJxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5Eq-ZaeZa0mxFd0lWgsoUdVSYsuEM0k1Lp32ZaymghYzd_K4hUybIvUImVYechFImJnnPe53b4Zd9gym1JHMP5cEfng9R8-5inXFtqV6DVxKnxSIJ2JRlzZdu78HZ0YhUe9k725Jq3sXu-FVUSI-qQh3yRk94yay5o0vUYz6pnpJJdkwwb0LvQT6m-TOvUUa-W8xHT5zwwxRK9wourPj83I7F0r55JIqcyNd_MCdCrcCrxeOYAquFIDSIt56jLPpfbKDdVMJcFqIPYA1vfMVg2Jo1L74tX-qT4bvesEGumulrJxbgldYm8yvv09AfkLUUC8foiMCULIuQyJ9Jukgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UP1YoqD2zKaB-QpK4bTi7QxsKhXXGeqp8dAgaXziNRA03PitlGENqrq8b1vtuhkzrw_MS1pow8h3yX0OTF6qmg5dJZ0s2PytWocru0eRdpS6rUSbOzbIDN26qasE3gb0BdOGwphOMgYv2JrP9usCAZYvsXOpxD_8CP0gvYkCARExkUKJ63BFo6G-2GxbNHvl1ifmu0F37a2-SLnZd2oNCVgnyX_ZaOETzg_bD9kngqIbNEC5_aGWg_XOdAOAZcgT36FK8c6Txkrxq2GhnjpAMyEqhYOqLXk5p0MiJ1jQyMWUdbPt8qPAr1chF9E5FRSkHDmS90L6x1owkcl00TJNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFXbJz5i42oX84D5-wtIixPpo8ObqTS3rFoyKHAYzB0Zx4OVGv3QKY9IGDPYtq2KsmMCcTw7nIt3GdxyoMASJn4vjxdlSFfHw-VuqU2qJOvh0zY1bNStoiDGwcD1vWQLTB0yOFR4MYXohBHZsHfaIWAH6dWK8FQbZ09kqTAfkkDYWLyBsrqBTPUUZjBKuMIxBZwl_jpr9EF28C1nPQt3pPwrfTpPca43f6wph9BfR2vX4VuD7ALi6xLCoK3t0ygguLVhjAIdBfaGtKoRarZGy1jtPTAMOo4ohR8uZ8vNCcwaSbf-uRCJBNCe2UpDF3aulq87dDrlbOCgsAnl0p3TY-28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFXbJz5i42oX84D5-wtIixPpo8ObqTS3rFoyKHAYzB0Zx4OVGv3QKY9IGDPYtq2KsmMCcTw7nIt3GdxyoMASJn4vjxdlSFfHw-VuqU2qJOvh0zY1bNStoiDGwcD1vWQLTB0yOFR4MYXohBHZsHfaIWAH6dWK8FQbZ09kqTAfkkDYWLyBsrqBTPUUZjBKuMIxBZwl_jpr9EF28C1nPQt3pPwrfTpPca43f6wph9BfR2vX4VuD7ALi6xLCoK3t0ygguLVhjAIdBfaGtKoRarZGy1jtPTAMOo4ohR8uZ8vNCcwaSbf-uRCJBNCe2UpDF3aulq87dDrlbOCgsAnl0p3TY-28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzRzwCHxKZ5jZrFJ6f18Knb21jB3rYbHe6nHZBG7whxAWWZW8u_Bh43UVBLBZqnfa61ocxEyG4X5yvDPkzutMGhgrHGDMIrOaaVsX0GDtiVmKxwKU9Irc9qq7P_HesGQ6OrHbF9rJ9kRlCgxBGhZmjdeH2ZXxE1RUGqXQqKZo7QAX4tWk0Ia3dANJQyWcaNacGm6oLUo8JH8r6sCSLkvIhxz-L22ghOVwgwXAY-cSHWOcMPb3SHd0Dz0SYRhxkNuGsLNAVHliyc6wvuzGgal1Qcon4eEf5S3tWCWJkmg3xV7MQW9kUsH0nvZr1T1l27eF3nljoYaT5pGqNkZJF9CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCC5-up540c4JnRgByyskAeDgXc7EyG7YYI1VULiSTw2bbe0TaR5kIb9jO2v2HtlB3n7fXrMEDqp3SmQ2hDl-yGWzkYO1BoC6PbXQtN2buKpyGL_pxklTHJX2qE83ROrzfe2dvIdZJMW_wFyKfxUVRzb6JH1jz3e9OOVxZbTI_-DEhwa6mJs0I7BhYLM8s5RZ61HzhM2DGOQ1ogWeHPfhODtWvujFP9kTpHInzuAZnk7X__DzMf6zoFT5066T_QLwHYRE2h56sdppRJzRnO9NmFygc9TimHUGb28MNGc0xwdLKrUjWeFUnpC12jtCFoNcEn03YMkPhMjE6i9m2mPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=kh9AtZY4VoQ4yBR5laLVnAwx-H5jumS8sVItGHOq8o4XHNVvMDBW0MK02SvUuqRUWfm_wKuJ5VJQiONlRUeadsRrD2h2WguY72QqOfki1CrlLWoiOLavxwgufJHQGtkwSCmSMeubfqHLHJqMb98B2MuhGAqqCKFUp17hdtgDlFvBx43oYRVRMivVLj04BgCEK14bZGSUlX31UCvIVBHRNGy5hHvuJwBCr5cPooRYvgvapQqwRQJU7rOIx_uCPZVr-wsk5MflX72mHJN9zj_8Q5fljlxRuU6Q2GxHNMj26GXzzZs-ssNib7Kav93poLTtJGqKbPh5fBCkALzGyHHypQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=kh9AtZY4VoQ4yBR5laLVnAwx-H5jumS8sVItGHOq8o4XHNVvMDBW0MK02SvUuqRUWfm_wKuJ5VJQiONlRUeadsRrD2h2WguY72QqOfki1CrlLWoiOLavxwgufJHQGtkwSCmSMeubfqHLHJqMb98B2MuhGAqqCKFUp17hdtgDlFvBx43oYRVRMivVLj04BgCEK14bZGSUlX31UCvIVBHRNGy5hHvuJwBCr5cPooRYvgvapQqwRQJU7rOIx_uCPZVr-wsk5MflX72mHJN9zj_8Q5fljlxRuU6Q2GxHNMj26GXzzZs-ssNib7Kav93poLTtJGqKbPh5fBCkALzGyHHypQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEYplLELLwQq-E9ukrEhqDtGDS9X24CEXFLsSGTMMfmGplnWjLRGAJ4sCS0zh8aNYtiew0XM75Bnq29otbpKr9kWcX8UUuT8OHCxkvC8dhD-J4yfB6DNpXPK6dZgEEoSsj7DmG_cjEzBoIfX7vPDNGys75ALXow9kY61a22TS1sKHTyIg7RvxF96yR_d-MnqbmuySQmi-8B00jx4AelmQOhQ5jjybBLAYRdAdqUaFXsY_twHEmdBKDqS-35X34pbkEl1yJJjVzfe9L_d82s7u5X-vcsNMfQq2WkmvlFNWAErK3KQ56jbtayo7XN513Z7aC2jkh4LMGHjAYS8FAZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=aSPcbZDUxsphAva5-ln1VviBdUxDTJBitO2S0IvXryfLPSmmjz5R17O97baYytoPG3T1Qs38guH5hjnrWd8kqodALK03nqNRNY63NVn05wQEXPj6JJW0gHqjxsoxG-KOb40wbZJqx-m18MO6eY8yKLshKvAOhyjVZreGQSTkRAPw6nSZIR8IXQA08FQyrg683Dn3KNTi3L5XyAg07vkyXiPQ3D6wNbBfEZOktfGpzDZo_nYG8v-5AbLS7gqjSjZ778JPpwPnYUF40SneoMMpBKj5fsci6ZD1Hyc22tCYA0Ak9IS_0QMlq6u4tK2tkLnk2DS3n4RssKg7V4SDWX_sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=aSPcbZDUxsphAva5-ln1VviBdUxDTJBitO2S0IvXryfLPSmmjz5R17O97baYytoPG3T1Qs38guH5hjnrWd8kqodALK03nqNRNY63NVn05wQEXPj6JJW0gHqjxsoxG-KOb40wbZJqx-m18MO6eY8yKLshKvAOhyjVZreGQSTkRAPw6nSZIR8IXQA08FQyrg683Dn3KNTi3L5XyAg07vkyXiPQ3D6wNbBfEZOktfGpzDZo_nYG8v-5AbLS7gqjSjZ778JPpwPnYUF40SneoMMpBKj5fsci6ZD1Hyc22tCYA0Ak9IS_0QMlq6u4tK2tkLnk2DS3n4RssKg7V4SDWX_sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=HwCtR3kqfVPspMlMxko_hjKFyBBNPBK4ZU5Dk-uNMccwrl56r0Ur473QgKpw8cnnVBVINatJqFIs7SZj6hsJhLfDfGKXM55JMs6WOOURstxJ3mPJozEVHr-aRDPpKFljTpZ9gTeasXHIPeyV5Ta0B7lQZjpSt3MoOfY8HI4jyCmtmjdCYOkO2u_UXGMC2hw3npKeEvJjvMlH73KoDPYCyrUMb-SLIXDURbCn_bODLmKdLwkTKtEpoLVBHqdfbnVzXBn6A0dI_AyCXSR5z9iIQKawcUQuqGR9xL3rjOVIVYYVCJ9KQfslmkCmOZUhN6KRTvDUzGsmWJy8Cp_v14IAEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=HwCtR3kqfVPspMlMxko_hjKFyBBNPBK4ZU5Dk-uNMccwrl56r0Ur473QgKpw8cnnVBVINatJqFIs7SZj6hsJhLfDfGKXM55JMs6WOOURstxJ3mPJozEVHr-aRDPpKFljTpZ9gTeasXHIPeyV5Ta0B7lQZjpSt3MoOfY8HI4jyCmtmjdCYOkO2u_UXGMC2hw3npKeEvJjvMlH73KoDPYCyrUMb-SLIXDURbCn_bODLmKdLwkTKtEpoLVBHqdfbnVzXBn6A0dI_AyCXSR5z9iIQKawcUQuqGR9xL3rjOVIVYYVCJ9KQfslmkCmOZUhN6KRTvDUzGsmWJy8Cp_v14IAEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=M0MWWmIbTJplcAbtA08AueOpsfAiD3HLzihF-JaWANgoTMs2lgMkzqo7GJwJgj_DPxyEbOzTX3FfLBtFHgQcZnac4z9rzQtPDWDqDygUe7ihUBgD8rVpqHlJGGKjaG9jXS5X2cxignMo3trC-uHaETfmliznWBbPVl6MaijGg1xIBy0IqVx7dbSqu1lxZz5Blukz7u_EXLMT7Jli6n-9Lk6Zg60CM5Ntb0VeJtQu-NHqfANhx85_Mo40mExyDcKvt9WttKjRK0I6rI7137lR66sqNJekmfWJlm4QIYn-4FlQIRbEXeP-B21882C_AUmYKupcZDUYuisGjkWot_szVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=M0MWWmIbTJplcAbtA08AueOpsfAiD3HLzihF-JaWANgoTMs2lgMkzqo7GJwJgj_DPxyEbOzTX3FfLBtFHgQcZnac4z9rzQtPDWDqDygUe7ihUBgD8rVpqHlJGGKjaG9jXS5X2cxignMo3trC-uHaETfmliznWBbPVl6MaijGg1xIBy0IqVx7dbSqu1lxZz5Blukz7u_EXLMT7Jli6n-9Lk6Zg60CM5Ntb0VeJtQu-NHqfANhx85_Mo40mExyDcKvt9WttKjRK0I6rI7137lR66sqNJekmfWJlm4QIYn-4FlQIRbEXeP-B21882C_AUmYKupcZDUYuisGjkWot_szVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=f0zXXTWt82uvRkNoM_5ydrFgCkBBzxO4vulD8rtS57rkrxjIULvYfwdSebwTj8rw2jECKxvmLrAbwbRmkjcvwJcDwUplwxHiDGSeuU6UyCpiyohsxK3JIun2FtUwEhCzhmmxux-Sktgwmc2ZfwvuoNGj0sNUMwAwkVP41-OhxR-q8Km7XiA8DWuyCT6MRMb_3fdJCZbQX-wLMWH0WFipAputGFmHLc7wbidZboA5E3CCXnAGuY8s4qUvHUqyZwOTxY12TmucpXaZsnksVd8bgSJLiCw_rWxCOgMdncfClmC1PiA0MoxUkQMtFjrS3_TQm7GJrFrY5O0krFkAqcyjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=f0zXXTWt82uvRkNoM_5ydrFgCkBBzxO4vulD8rtS57rkrxjIULvYfwdSebwTj8rw2jECKxvmLrAbwbRmkjcvwJcDwUplwxHiDGSeuU6UyCpiyohsxK3JIun2FtUwEhCzhmmxux-Sktgwmc2ZfwvuoNGj0sNUMwAwkVP41-OhxR-q8Km7XiA8DWuyCT6MRMb_3fdJCZbQX-wLMWH0WFipAputGFmHLc7wbidZboA5E3CCXnAGuY8s4qUvHUqyZwOTxY12TmucpXaZsnksVd8bgSJLiCw_rWxCOgMdncfClmC1PiA0MoxUkQMtFjrS3_TQm7GJrFrY5O0krFkAqcyjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_LFbs34S7ROjqvdFxSiFc9R9-BEDinMttg7BB702wSjv-rEjIDj2Z5ozZ0fZAmJ3Ay4SJtYsrFPMwwlTqYmRsdgPjmRtmUwp7BH11z7U0vdbs8m8edleMwLGmGkvfwcN6j3faUWg7daTKWteIlUDzIOC4BTkdRQ8gwsKips0bIjK-cLoOgUy4TDDYMOsEDDL3l3k0swHOGfVoRmJXDMwrfe02zBP_81wvFuasA4VdFOC6jifXYRpsnU55VZA2wpXrEz_MmRIj69sV_Jk4RNAuWGtEs9uviZ00rTR-E6I1iyn1UBwgzRUjk8jCvGqOg0Guo2DocaOsmBMju0zhtT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8HMxSxY0lWQVZQ4lrJahPJlKdONJCxXl_ZpqnUgamSecf9pVWEwx01owoC2m4ZRjsrcX1abz7AqHQ7gCoRCDb8gb4TlqEcP-6Tx3zNBJzE2-l8tVaBrhOZywScmgssvlfv80XWLyj9niEGrxW_tazOmQnUvJp_pJ3Kv-yb8geCZicCnbpWXeYy5nxmsiQ1Czs8EgUTRGGStOmaLpEr1U1mjhjZbNFIIi8VrFFlWEkmy8lrbzYdm5cjpSGRGrCJCt_aW0yTaL5HH-7d-VI10Yrs5JrOohfrK_ILEvjxV6pZVfrZ7lhk6YuG2suG8KZ3EFihbsLX_4KYIo_IuHVktLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCmzAmsshT_4iiYEDArU7Ry_6XY0RCq7y5CJsFZ3ywxaZd713RBkx7bmf8tjaDW4AOZULBpJSvz5tBhMp64lVgu4BF2AQREQeSe0YozNF9Y9mVHIgtXkn0LHkoPhCSGeUkBwCINDTuwy52hIIWv9z3UvHPZxS3DwtV1v6OwNtZ9cg6C2luKtLDycIEz8XVTt79GyF4igXJBow8nCy2HIO5hnrCtsst0OwhOE6iNa38Ff5Uo_j9jDfUYHGKkAi3DDBz1506oFqhC7zV6df50hGx-p1j-wsdfvQ-WIWusorGTbQovHdxEGAhrUCz9gSGKewbscMhW-MuoAOGW44T40jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0JQOLZN9vtX5HZWYEOxHmyAJ1mdqwpe3CmhfDzr_ziQvXo09fcvCPiDJwQAt6m3VfeeXVL7Y1x0fFxfvTrK6ntN6xk4bjCqWGlnXCqaJ9Xf4k1M9QUU5yXo4pKaKvyFjglWLwgLUYtY-iukhPl--RTNPonXDralwqbmdma__Tl7N4mxupIQoDRI8h71Up-Qiy85SFI3Zrl9UQjPJDYK4AkQPDEUEEWumDJRZKsnCG_ZMoDZOIjy8mh_dxd0l0lya4f17yPc-6Cb1nXLmq_vCAJ15BGXWZ3xKe6bYx1JwwEUbl16yrDyIR3h_WML0cghhiRCOiwb0L7yYoflbmMpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRu4-mu10dXnLVeShw8PTKDTY0OfIED_toZ3t2gC1A3l-ZY1qDLI80xFjFuXYjPAfAZe-rUYclR0viIQMzuXWGNRwuPlp78noY7c8eqt-QvUSUuJJGdkU675ej6y9cKiME4OntU7RktmDuqq3W9C0VZzHYRbDiesY3AWDVVnAkLQ4klmoDVDPqXyWwz5myjJjg2kK9G4uQ2v8DhUT2EEvKKYsXSv-U3solodihmwqkHuAHfTq8Zwto49QG2KOEDkweBRBGFce6waSJrkSJDfLVkMRiBAtCRyy9XBxBx81EOsBVdLWIMX3fKObhnhaz-QqHl8o9efhfZw246d_IyNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUeoa0nPRjcZWWTbdBwSWZwRxsXOYeyhns8_Cfo1X2zzp-0onwT6IosEVp2Nvw_yTVNErRe1kfUnCb_KkhSDnHuyKY9nkz9fXcSx5m1Zyp3Gujbo98igJGXYHd6L-2N45Q-HBzGnKyvscX_cUHUX9U38bZUyXDo141II49v4grAlMGf6--BDYqDvB2fY6TljBxqfLr_6POlHSjMcytQlmEwtBZJ23dZRLQ4RBgY5JyTdDq9-S9qlDP3a56KbXUZUC6Uo-DEv45CA5u2mK07B2gpt4PtfrQxnAmx945TT3hBGZRuKD20MuWemRESlxHlfp_4t6uoR82Aa066vBmMmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANsjEQOEZJka_JM6TkaGETdu1PRSgSKaRbCFzTHOEhBcUnyCCaLnziAzY1cNFtK4PSPUCMnMmhEdhheGUjc-4pVdvBb4RrsqHNBSOpLmKKzDLG0kUg-bmipDIwoP--E3cCme-BmJTbV0biyNRjP6kNcZ3LYXq4HaFoWkLLAtkatftgqZnlt8584oDzlZyZsCWScsH73Hoa1xNhZLbfBTGMCsRhWLqNVIYHGeAdXiyqnZLMVt1XTfkc4KFscsfZxASKeNvCQ-Wh2icaxolsxnLxtP9tegcUfCMD18gfwUb1LDZUZGG79P_bpWOkJK3oNo2JzQ4xFn6LxV8N7r_doyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ci0ftyzrVkFhnTPwvFbXK3JDV4JeXIv-kgsSMKY3pDE36WNo7-wNcD_nOJdYQ9oaxvkS8s8jD95P1S6Y3qQEV9pg7fE5_Zvt6kT50B0xBHxcvcO9zlcIYt45kcUKlG1GBkIWoHKT764ddRbNfQlGb3Wt7JATiBFaLe4K3sRqHlQ4e7ncv03D6gn94A_tBBahSHW5nr8QOVbmSKp61SDo2MiSSmLu38wUtGGZNxPLcl65mBZ3jgh0GbRPPrUJgefJPJwns7kMi4ksitzQtuzBGvpRa5bWUo7zy6rLQyYtu6b6RPYIPdL_q7UtBRCQjGjlSyPq6i1n3T7vzV-E-HH3WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ci0ftyzrVkFhnTPwvFbXK3JDV4JeXIv-kgsSMKY3pDE36WNo7-wNcD_nOJdYQ9oaxvkS8s8jD95P1S6Y3qQEV9pg7fE5_Zvt6kT50B0xBHxcvcO9zlcIYt45kcUKlG1GBkIWoHKT764ddRbNfQlGb3Wt7JATiBFaLe4K3sRqHlQ4e7ncv03D6gn94A_tBBahSHW5nr8QOVbmSKp61SDo2MiSSmLu38wUtGGZNxPLcl65mBZ3jgh0GbRPPrUJgefJPJwns7kMi4ksitzQtuzBGvpRa5bWUo7zy6rLQyYtu6b6RPYIPdL_q7UtBRCQjGjlSyPq6i1n3T7vzV-E-HH3WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_RTkilYxI4u5zZvj_3zv2eB4M_nmV0ZD9FDoqrPewRKHUiBzBA4TC-eFbqboJzbQUrLmAZGi5w5RXbiC0xFhvW-SX6chCAWELHyYrAYiCUpQWNz3oDj1rX2HTio5fgsk_jDUat-P8wPF3wNXAJBdAZRibGZ2hkJEzEn87LuzZyxo6PFXTGFaB8jgLt5Rha-sBf1fh5Bxcz4kFP9tp0z7ort-8doxmf53fDMAQmNXa8Dc6KWPqn95dVqcqAlOZzQ5iMAwj2bmrRjzbHx6ELTb1VkbqwlsVr77BlCOVSYdmdlOOUTsG1OFtc5lwwN7F3INO07W0XAMk5mFLn85TaXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNxwSJdDigX55H3n9W1akhM1uKjrjxqML6m0hec3v-RXRA4yNMB-0IYHfAAsiRMDbc73vS8oBGtXwJy-MIBKwxVdDShqoiC97eCJoMmfDhEantglteNYgH_HvHUtKp0g6SRAbejzdsSUoq7ILVOrLJqqsbSTtMEwakhyqtVpF7X9ApD_NWUSuc0l8vZk5o7vYmaSL4yJdLCqftsXBJRwTsuYuUJjggD9uVm7bG6zCb8SKUKNIMSpfFrusVCbLJYmld4d-FruOgS7_wK-_gR1xLZLO-lE1Jv67dMFdYp3p9pawv1QZNIu4EXN8LRNPRTjP5MvbaMQepFxegZKYD1aIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jj5kQFdMee-6uvxF9OvUL2rzILYnt29OeJ3kisEE7f6S2MEur9ZHU_adwgMH2jsRy6YgZG6HC4OAk5mekqi7xQOONgRigYdzTE_M_Xy-Bjrp6Bqu-pF8NRZgwVZO6dS5JNyeRDlgu7EQq-seYVOHnBMh2ClErymD5YfxPlIAx2kDgStVhs_It9-19f3ta-gFtpjUNej2ftoINWb1XCeLOMKmsVsAJUWuCPKOX-xjBCehuDQN3FHJKr7wjJk0BCcLcQckZwcB7z90AwavpbeO-ssbLDseo9ONNSf-yibF-IVjI5klh2QkeZRGO_XBIwd4uOUnMlymHp3c0jZu_zvQVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6Fd_moVp72r10W2SshpZRYwKiIbKOFTiZvs866uVM9LC94feWRRfGgTqf_cYWBGBz7aVVKHJRXqouTlch9Vz7ef1OybRc6WELyCv12tkfhnGCJOl5c-8EGmHzw7anRCsNdaBZvh7_4l1qRuIs_mF_XCQMPiXKWMtpXgyi4zOh3Ny9zrVlGH2ZbtyP3xyG8ioTIWYPhjZOp-Z4DOckz6csPRKMiURBp32C_GKEuC6RRTRfScZnfhHGm4dtoesXv4V6KKD-ueGZ5PoqwHHKtIjDJjcLxRAzBhFvUSwH0w_q6atV5V_cSNxhHfBNVHpS-ZXcaJ2R0NqY88VAy3Y3kebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFJVa8iKagnpkxxH_i6Rg80UVOb5hCUP220w7HufTnaNH8dXgkG1VGTshuxCo3c0qhUGVvqo8poqRtgT1RudVBZ5RfOPXbCwTj5CkZjVIy7k5PmqPeOsm3m1_GgLIV8XaJdSqUr981Pv4MMkH1JCsPEfg0Oi2YHW16sFE1zRyK6yPHO1-NoeI_a_JS1maJYUEj-N1-jJHy8_WOxYrbtKvw0jMPdn8U9wCr66-Ff4sumSOslRqqIlFFpPG_ldIqVoWOcYUMl0LlB2MajRxD5G9cxL1TBOaGV43vKkUrC9G8olJ4VSNx1m3Sd5nN9WGNoyl4ohjPRHAuja48AQrNGVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1PuH4Rm95WJe3LPEsg10OzXFRz8D6SfKIXd39Lb2JyqRlomYpY7Hx-jwGQIN4UnCOzVmFkxsN_cxuw0lAFoqmMqBrJTFz6JXKwVa6fJp6OctiE-yF1AHWwDa63u3nSiulqNk9BwiLCmsm_C9eNeVlFycWdZ8nGFxdm7djuLII3OnIC-_pZtvVDtRmCdy0rXHQurD99IcjNUxGG6uG_1DPoIxSAsjDtaXIdteKoo-w0g0CUfcPXKTsIpxEs3LqW38uaSSI7h_XNl1WxqT8PuNUXGC4vSyRjv946IX7TSHLtnutk5xVBybr8bzvQz5jpO0bGBYd-Nc_iTdD504ufIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Hu2qjPxlQI-S3lKiXeyJYWGt8Dwh-M00XzjaOSpkIjlDPFi6BUquYACkk4tC_Deyby-8bGxRvzgg1o5cUP0A8BjYPk_cldv32kWhGtaDVpwpjVPaiEdq-gZ5Mtqjo2giiaUcQaK2bzKnCvZ3-_o3LTNDAJy__HeuJkh4PTgv1rZN_gnqFIygFSa6ebZarR1AU1j7cerKarZR79p63jiYEXbAz185tnxDRHujKGhykaWXNY6DLc4Gr3HKYQ-mzrVkCFZLc9N5914peRGJ0XhLN1lHoGvF31Kq12Epi0R3-kT0oeCTLVNPYRBAyfUlgd9oPvLqp_kjgWp4S18urMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uqd82cb1f3qOgZ5xOoNGho6OJ7zVXbNBvCHnvxSljaj6JTGhAFle4nCAGmZbxgNWu0PyRRDusc7rrDWnKxz9VgGtPBEx-3c7FamAIGzJBeL9_EylHonxhrdvlS_fTL_NXUUne0yJJ53fyVsujWpKZykU908-8zNefNolgBqSymAywuPFxZkDv5kFpu5HF15FwK4AmSc3lzmspSUSYnMHcKtRBsAUsxh_HNvTWMzDUjxwRIh8nu9R6ilHHMnLYTNlI6GpYXs2pykRpp8R23hy_rNzxkrbGhVBH7RpYvHYtQgwRhSylxqF7Obb3pC5XLMRrj8xJrHruJQSwnh4bfVa1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=kjpd-ix3ROpaM1izo2XoM5Xw7i6hElix-bnuLUouxKLQhzRcN34RUixcYkOfIkC02Bn-zhDgcdlXHHtRhKKY7uxVXXdzVXKpfz4cwbcFBUkiTHnFZvDRfKPJahMipxGFgsqUWTk8uoMtO0EERmqEFbpVPVzYmGtsAVrfNC6GtG3oLh4F2aVJY9wwqFmn-XGle14SBt-OsD5TgnBY1Z5tQHm9keMsuAAHwL8wXcPeR6FJHElXIXMy5Oid3C2amZnJHJ9en25ATVL0nAF4jePOvAGU2NbMZdUVBfTLz6Vrp3xrRN7uxiypcDVp005e0yoXlpQHn1uaeYcssbN61cu7GDnpsxP-invHZvFpjHFUn1f3YXPzSdF55L75ZEnuD5EhukUuIph63tl0nOo_3bmDRsYZbA4duOjTssnZl3VDY5gk51YOzww0Lh47FEwCeTDoFLeIoJ1ACn9W5WtBDNlV2M70rOuJPlSATsKfsoj5ijv2IczRm1jvn1iix8yVpa5gY5SeTSw713A8JgTCoWQbGDO7C_nTzjHqWnWvrViN4YylEylLmziHlo5NFeOQFRaUwF87NIzNLOQFQ3XoEtLtlMlemJRDZzLf7xYVkcFX7xhmBw_1_lzUbbNVzTsfyZoswocJ3l1bzbi49TDSIturwZmEzz24I7g-cYZhj7uf1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=kjpd-ix3ROpaM1izo2XoM5Xw7i6hElix-bnuLUouxKLQhzRcN34RUixcYkOfIkC02Bn-zhDgcdlXHHtRhKKY7uxVXXdzVXKpfz4cwbcFBUkiTHnFZvDRfKPJahMipxGFgsqUWTk8uoMtO0EERmqEFbpVPVzYmGtsAVrfNC6GtG3oLh4F2aVJY9wwqFmn-XGle14SBt-OsD5TgnBY1Z5tQHm9keMsuAAHwL8wXcPeR6FJHElXIXMy5Oid3C2amZnJHJ9en25ATVL0nAF4jePOvAGU2NbMZdUVBfTLz6Vrp3xrRN7uxiypcDVp005e0yoXlpQHn1uaeYcssbN61cu7GDnpsxP-invHZvFpjHFUn1f3YXPzSdF55L75ZEnuD5EhukUuIph63tl0nOo_3bmDRsYZbA4duOjTssnZl3VDY5gk51YOzww0Lh47FEwCeTDoFLeIoJ1ACn9W5WtBDNlV2M70rOuJPlSATsKfsoj5ijv2IczRm1jvn1iix8yVpa5gY5SeTSw713A8JgTCoWQbGDO7C_nTzjHqWnWvrViN4YylEylLmziHlo5NFeOQFRaUwF87NIzNLOQFQ3XoEtLtlMlemJRDZzLf7xYVkcFX7xhmBw_1_lzUbbNVzTsfyZoswocJ3l1bzbi49TDSIturwZmEzz24I7g-cYZhj7uf1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=DiiHxD2ztnBFrJEWXqT1xeY4UMS3bJGQ5F3-QL8GbhB91VrEKmubFoBwrMaSdLk5o9852CUVMT1u1Yq7HU7GD23-co_LCOW4MH3DFQSXJid7Lws2BzBG_F50bZmUkpKHmWUnq7YOOUirzzjUTqMvs3G1YnCBZR8nsWrtzZErMxgrQnbctSbT-8bp6FsjW2sDyIkS7l9HQSo9HotFba5SCOqbeSfRbesx89Ba8jLzl6cY8wGbCEuhM57pBd2sID4cvkz6heLB_aJS1lnv1BkCL24IrptGupQb8WkgcfkGHNTA2MorYjUfx29Fjdi6oODs4gOPiVAoZ6RlTPVr5AwI8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=DiiHxD2ztnBFrJEWXqT1xeY4UMS3bJGQ5F3-QL8GbhB91VrEKmubFoBwrMaSdLk5o9852CUVMT1u1Yq7HU7GD23-co_LCOW4MH3DFQSXJid7Lws2BzBG_F50bZmUkpKHmWUnq7YOOUirzzjUTqMvs3G1YnCBZR8nsWrtzZErMxgrQnbctSbT-8bp6FsjW2sDyIkS7l9HQSo9HotFba5SCOqbeSfRbesx89Ba8jLzl6cY8wGbCEuhM57pBd2sID4cvkz6heLB_aJS1lnv1BkCL24IrptGupQb8WkgcfkGHNTA2MorYjUfx29Fjdi6oODs4gOPiVAoZ6RlTPVr5AwI8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd93nhJn98eBFen8wt5X3PWRMElHIzgYcL423hhi7gFTzqzECJWhuebO1IhI0TA3L_XOkVCZ6VD4Q8_DUYN-VlxbgJ8aLoMPXUis5PdjYxuBxfPIy30oi4xRWffNCFpfFuVinAGoNgu2ksEkapCXXqmVy6JfLucazDhWeQLMsR0w64kIbd5EISg9rb4Ls_Kcg5QxtZgCLrLiKYZyl32P8LrJknsVGV1bQwKADnx9SyuSCfHTp53JrAPB5t1WA0Ft83POmb1vDShNIbQvQHhH4HBowm8P7_bEaySm1_eQ26Ygwr0dDzA-sI63UXVj__YrRGlaFtQXgFvdY-UJ58mhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1G2aJ2p_mZ2f7lTO_bAhkGJjTlCGDRgRr698PnICP_bl0FUknjUBVG2dpMh1nIneEUwNCjtupqqWEiso2irm7LwqzFN_kJT-rP6sLY8Sc4u_04pWUo3hXmfENdbhfyOaoEPhdYXSYf_ovoBP7grWYZ3tQBy4OOFVpCdPDq9AMOP1dF4IJV49nipdLFDYZBThco1B8iyjHV3PqoFTIFiwthGWs3aLaBQa3INauQZa10ZfjpG9L_1IZUST5hHS6JqArGdE0AtDDOZ6Ravzs3wVQVcSyWzvsiVUZXQ7aQF-KmQ5T90FI7C_rAZ--NxPh5milXB4OTrfn4DuZFqwQ9hpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBqV_a7gfPm2bRvuXXelE92luYsOmked5YVDXlm27yMVrTkvbnResJi8IqkSifumaDS_ymaZrVWzE_vaGn9l0jvVDDvQEgb2HucJvESjLwFTEZEahNvVj162HqTPKL1AHCICvmxbrMAnw7Gib0i-vZd-WmzmeNfuJTnrdGaTwAeD-f-s_hR6lwhg_jSy9EEL3bWIP7wW8zoannObcGQ2FiaCSSjyg2eiCdNmF0gI2gkwxhi_yeQ_e0k4tiUVyEyqTBq6RciP33IKEfdbTDiDvG0DWnVQRIXZ-ysa2_V5iw3jN1TjbElQDZltgTvC292Asuy-vUVAa9yhDGBGZYh9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuSYSpzLk5h0ksE5VINsjo6ZsgEK_roa7BmNSevizw6KUzBZS1Oz6lWVbOe4IfQEmy1F3wSXdxrL5l1bNiEcfikAu95NCZ-gf1taY3I6fqwBFFTgb4aKVh5COyhcODt7xFlKoVTYWQSfwFMDUWFRfchtSe0vuF7hMjBQZhoH7UFeF-3wotAeFFLo05ESjsUrHMr556DgMp9PN5WMP10_dUX23OUF75xPb1fp-RgFPsaxDEbGabmlzKszlfG6nihpbmbjyAue5_qm8WqFEI4jeEHXPzX-v7elTX-Z-zIMHeUQx7vyvjjR9_AqqDtgP7ZHSbBGbO93wZZ9BZICROlsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV8Pz98ERF0sveeY067oztcac3nnwZsr5wevC6gTCY3pCryPA-pPDk4_4M-oFREV21KBzth-NFxpmAkCy6MjVmXpveCfxvT_3yduqFsM2CBjSXWWDZJkHiM8Kca0jSbHeLFiEOganoAVSK3Ikp2DR-HbkBipOGW6J8hjk6MHts9SsTdOb9lLVmnhtgwlJUQE6sx7uCMHRj5Fc9Z9rC2ImCXTi-ACgUlJDcNXsmNXdHcM9gn5bdKg_-9ek22fTa-oXIZopSylIf1e-5LVS2A8scG2jJXTipXZDy-XOv_mHO9EkGrMMG6QQK6uUAPMKDjMCmjgeNu1zDhPHcX5Eajbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgDQobck87hW9Hh0XX9rbdwLcMGXXYgoF60KYIPSNAvDIYc77jCug9GH42YFiy0ghcaH4kz-rJMsGpFhHCt7SjNsGlF_cwW3Lgv2CtUABbaPAwwALUm30jTb0eZz6k3zOp9tunQT9IbSPSPXjBgUI9A4bZStkpWvc1-VCsS8GUv7vbpVPT7ZIdwFIUuTrbP8KOJsJn31dV4EAjitj7krK3a-NF5otHdKwpDAZFzwXxIVFSF628kGKoLQ022hurYj7ENLBD5US1OYtapw9u1ZiUgVZgEKImEU8cIwmYo_ETVO3HIkqqbkxdMqwVuh-dS9Ytfwl8j8rIEfJYXg77EHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNDvXI7F7rt-1GsyWJ-fvHWPedbvokkjVhm1mknzSVLAaIL5AjehHgfS5Yfd6PslLUMbeGCxsrQfo7ceKdXwUwk_eAH3aYcMWXYN7dglZ94UubEdgyNQ3_ThvdQ06ZUTqSdl5bEBOt4lzISR8eP7voNeTSbFfltxaRxtMYhqqkBHMvgZD68EU57W9616w2npzE_DVC9UCgDZDG4CC0vTOycd-hTvlb0JoSSz_JCPFuK7Yqj-zwqtLQBWjS-nMZBkSvnhZT5UL1yHAwgLSBzsh8XyvxbgqmAX0UWW4TyrXzq1fjsUI3ZC7ftJkmd6flG2WS4z_g7XlywzKcj7RLdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iy4vbkNOs9ncbult5WhEqAi5rRa_oU1SPLA57OiC0K6wgFPTsUysozOtZcAIsJ9Bm8DluZuEVEanNdQMp_yHM5mrEGQGz6sM7KZmxLR7myE3U-QbAI4zV02ZTrd-rmSBi2RxFoysq0qxd3JTfUD99LVlRfRdecgE-MN6338vmTmvxLJUvgoV0zDXU8CVGw9YG-ZtUYgymfrtPFX4agFfyrKL2hRGoleTpYZOZvKhsMZII8GtdthbOx1GNxLgvxlm2QdETvCvgO_y6SyEYio0EcRPebGW79DbJMdQ4KyMorJun1tZs_SBVypr1pijiXxfRClNkCUdICnHLdhcVh9ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhZzKGyjX9sA8oMG1uiZ-YSW_5LS5Jud9r_Zxcf85McV4uFijczu7C-bFjW8YhPWrYloxYdcb34JPInehZQ8JFVkEIqyUsonYbkA-vTPYpLbCRSHykDs8kEE80yXLreICqlR8LSwteHYTiJJoBwgQlgnVHtUgDR1C2EECGcTLkjAg5bpJhG8B8UxnUiz9D1HjNni0jbeLhevaOH9sG8Mt55VqG2TmFmUrt6BKx67mrAe6vGpCki2vZNPyfKGH2SU7CW38OPgjHwfXgJHAaokcjy5tA3UR4NLrmlX473ykWVGQlZRFhV597T3MDWSnkR61YPbG5Lif7tCDLSwRBPpEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ZBSIMoPLJCUQ5iucWc18ibO7ZgT8im30CZamysoeSG3gHBOi8JSDoVS0_ZB4yOaKT20QUs8PvxRN1TGqwNfjJHjnAnU21MBWRQXSGziB78r6jsBFOPj-AC0-xcJckZeEfAQClaJdAKLyNvH6pH4jMVR0hGbEElt7OcJfS2zf1UfYMi6sO5bZQ6DuCLRnKIj2GNRPQgoxRXa5YZ4A95nSvKPMmgqPBc7rmYct8j-4JFpZsdODyh7_Fr_mDrfwOo16gY9hKbiq4t65_QZmB375qIZmcStVdUID58t3P_WolMYFaAUxHOPwtj8G6nuDhhpkK2IO34aONzqEnMO3jhxOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ZBSIMoPLJCUQ5iucWc18ibO7ZgT8im30CZamysoeSG3gHBOi8JSDoVS0_ZB4yOaKT20QUs8PvxRN1TGqwNfjJHjnAnU21MBWRQXSGziB78r6jsBFOPj-AC0-xcJckZeEfAQClaJdAKLyNvH6pH4jMVR0hGbEElt7OcJfS2zf1UfYMi6sO5bZQ6DuCLRnKIj2GNRPQgoxRXa5YZ4A95nSvKPMmgqPBc7rmYct8j-4JFpZsdODyh7_Fr_mDrfwOo16gY9hKbiq4t65_QZmB375qIZmcStVdUID58t3P_WolMYFaAUxHOPwtj8G6nuDhhpkK2IO34aONzqEnMO3jhxOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epayisg3c1SmBaaLqO6RCBcUXclLLzcWezeYBJ28HENsi3dt3lSReUGaZFv2QtjsHEkfwioZaiTXMevK8-DSKG8Vw6vnZWMX1vLbnEGj1CHpjQDfI3kAv2elSY9hHHcO_EbcY7k0KlxsbTK5kEi5qI_CrCPE1YoAXMMbXwNpP4tB_bQb33oi-N84MtVhkwf3S1SqGunIR44pR6ubqzwYttFMV530pYsuQ-bAsjgsZpkitENFoSUaXjeTb7LCuM1V3HCOUGmVYChghQuHVD3GNh1Kw8SYXbIvte0APERmje_zSMoikDdDvUVw_Qf-kS2wfllU1JuyvD_JiByXWh69sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Vf4VSo1HwP0Rf5V_NAJFtRFaoLa9BYd6grIO0FUakkXuX8LH4frwKJESU5yxPGqxAofxQTrOs9dJ62QNKOXls4goWBCi5fUUIQKMBNue3kBmVMhPjtrPIKRl1Y3861oAb4Pd0tfu9wri2NvAIPSmcwGw-TTPrYvZ1kRRuiGoqlevpSD-dG_vjDaft5VWfKYouit796WH_ImANWgdeskISG5MWoNFGmLAgZ31DLjS_AC9Uy8kedEn90b9fydZOaZ5cAfZDMNhik8OzMCBKGAQf_o_RyLNBfpLExpVT8LfFmHclw7KWsosrNAzrts0IzHsqDvT_LR5b8gcWRUnjrMQNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Vf4VSo1HwP0Rf5V_NAJFtRFaoLa9BYd6grIO0FUakkXuX8LH4frwKJESU5yxPGqxAofxQTrOs9dJ62QNKOXls4goWBCi5fUUIQKMBNue3kBmVMhPjtrPIKRl1Y3861oAb4Pd0tfu9wri2NvAIPSmcwGw-TTPrYvZ1kRRuiGoqlevpSD-dG_vjDaft5VWfKYouit796WH_ImANWgdeskISG5MWoNFGmLAgZ31DLjS_AC9Uy8kedEn90b9fydZOaZ5cAfZDMNhik8OzMCBKGAQf_o_RyLNBfpLExpVT8LfFmHclw7KWsosrNAzrts0IzHsqDvT_LR5b8gcWRUnjrMQNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=uUyJhpy4VrCNVyMzUBHktpr8PjtsEJEW86ec2WH96kglRGA9SGwCV3MbCuCR8pYc9fmd7edYochWuwYQt73ec9yCZr1UMwft-Dr3RTP9vQHYTq-PKGWNKkJDUuUlL3bvaPS0tQydeKP0xg3imAUcSUpSO6ck4_G2p8p2siq5KUsAWqjKJLsa59Fc1hCHFSN04OMX72hZvEZJNjiCYf1dWqoJB8GLHJexi5s47UK8x78QN-rn9ylC5Nkvgh8RuYubr5aN0jZoVyrl_L66KTwH1AVotwaAxFuxLs2wbnge7LrfTPnyFbHX2zGMbSkm4N3Kf7N5McbEL7L64DWGxb_OXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=uUyJhpy4VrCNVyMzUBHktpr8PjtsEJEW86ec2WH96kglRGA9SGwCV3MbCuCR8pYc9fmd7edYochWuwYQt73ec9yCZr1UMwft-Dr3RTP9vQHYTq-PKGWNKkJDUuUlL3bvaPS0tQydeKP0xg3imAUcSUpSO6ck4_G2p8p2siq5KUsAWqjKJLsa59Fc1hCHFSN04OMX72hZvEZJNjiCYf1dWqoJB8GLHJexi5s47UK8x78QN-rn9ylC5Nkvgh8RuYubr5aN0jZoVyrl_L66KTwH1AVotwaAxFuxLs2wbnge7LrfTPnyFbHX2zGMbSkm4N3Kf7N5McbEL7L64DWGxb_OXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu2jIOtKSsYv6H11fukyD03hBN7c84y9ZVlWkn2n-fzuwiRrpdX_eyAN5V-YKIVrHymZCpmWxC9Ya7VwfpC4tpQdt0HRDC87AyCZ1SzT-RS_PqUvTx9TCsL1fwoLFhqlCTzb7KPNT95y35ab5R7AocXhR5-aQzjQzRmBS8Ov5UJun8ddvU7ND9LQq1fsh5o05Ubbpz6bb-ef6SXcW5KHQMQGW-O7tbXI9KvrJK7LZy8jp4ZZMQD4BQ-hdBnIKIR3wwA8JbolO52Kh-NhhJqK3ZI9m9_5hiffPj_d5bxMbNMj6zlw0yb6nz7H_sgMlIVMo1yFSEAeZueDhPxOeTzFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=uszbyK44AF4JgRUhX8I7WOdbJt8tjzdJYFFOSwRD9k9STADAjWS6GKLfLuJ1KMs2Vqf34EIkQJu1d66tXFDYZVEUdu4Gp68I6LubRqzhta0QYm3-SLJIXXLn6UnVVfBz0xu0OB61JxM_llbP6I4gS6up9OSdU2PeQcAJx1sPzkV7GoGWe_umxefpjCNWfW71F78xQ-58mFaRh7I-caFwi7s4aXaeeZyniyn5rMGtyfXZZrnX9D5V92dfvMB_mCWcYYxB_vRR8OCZhUoOjFvmH1StAltIeyQ497myA7E_DnEiQJGN7Rj4c_nKcnfdAGtZ2uuy3mwosQP-kdZFTWr0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=uszbyK44AF4JgRUhX8I7WOdbJt8tjzdJYFFOSwRD9k9STADAjWS6GKLfLuJ1KMs2Vqf34EIkQJu1d66tXFDYZVEUdu4Gp68I6LubRqzhta0QYm3-SLJIXXLn6UnVVfBz0xu0OB61JxM_llbP6I4gS6up9OSdU2PeQcAJx1sPzkV7GoGWe_umxefpjCNWfW71F78xQ-58mFaRh7I-caFwi7s4aXaeeZyniyn5rMGtyfXZZrnX9D5V92dfvMB_mCWcYYxB_vRR8OCZhUoOjFvmH1StAltIeyQ497myA7E_DnEiQJGN7Rj4c_nKcnfdAGtZ2uuy3mwosQP-kdZFTWr0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYKxAckfz1GOleHPAyIa8B90h-Fj_PdadwBrtttNisgRsHIKFCFSm0ejfsqzx-6cmzT9NMe7P6tWR2X3m3zHRla1-E7Ymq8AD3zbLHVR6Vvs3yaKDLqm_LpPDr7HA_ddT1KucSFWgIQd49oxuc2aE9MthiW35Z5QDeQV8yhv0y541CQ33EB8w9hRKNuo10SAXR7SZfG065_Xz0_umt8w2zLBj9hBAHZt4d1J0ZPkhVSWUQVlD_0PKnmLFZDgUxN0qL8p3knU5fm_nD5oOLJwGeyjlOZGU77lYbzJx-DxVb55_-Og37-3BFMYGCe3eu0h3rXNq_E62CMi1fMZT3It0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvyZKLK6eOGlmPQEKAWh5SU6arnpefotUQ28YGgLdW_J5GtHQs_6YiJL1qj2pgmUfuw6Y0dyC7B9iX9Z9UunVuyRQS-3v1ulfVrzF1A7W8lNzjtwsq9SPJmDaLZOwtk049v_I0jHg2a6ux860nJKFG7B1S_XKfS_F8gZjwX7RGjIXUHBxNZox4A4GkvR_Sd0dmRjoLun_3zyK2wQ4RGrn2uZEI5eIm8-5YvPCSlKW5a71YQwt59TB7KPtc20tTE5FSRLI5EVlQ0ylj5sOAiszpOf95UCi8RqtE5BSzUPP1gtObSsXOIggqYuqfmIa1MgamrkgPzAhb6m8y-9jZ8GIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frdabgAlqISZVZiU2FG4GY_heFcDkOpB3OZwJb8jaGgvsKkl0gcXaDBh_VrC3ZBwFGdZ6X17-BgsoW3g5BMXlh928MC1XvOn3SAZBrcA6fUBYQjDAI4KsvcKm2Q-zKazoL0lGOX7PMUCSQJyqH9FZOtw2kO7aJ2d8-AQRPfgC2H3xDFGp-7d9n2I-_EDYwNHUr6T7cwv8igJNPaEwBsYLnMpiMhh6GTzGJBewgJ2gHvliwzxIYtvh_EdWHyeO2ZfxjaV6UTK7Hs3mmqd17WQd0vMlQeB-uVox4o2biZ-SCiVsgZKk-7dhQC4edxAW3zlkIc9naOGAfUYVro8ccpttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m22VR_qK3OvOKN0xQo0odlD_9im36b0bku8Vu8pRDaW_yvxJIkeswl8gXMcHSsEoRilZh-26VGPB-mMtZ7y-g7GVyp3kageNbjUXxoDCbn6IOWdkiLXf-tzUs7FHbB5MZNrFtviu92JEz7ASz6uQCD60OnJSmNL-kFp5wvZqDgiPzIG7Y78enjnIzPqU3QY1TaDxALBJLQE5fxkSCIKJK5tYKoMh8v0IUZjsomX8MEhjLMETbl-HdlzGmkgowfp5njgkVaz1yXFge8XKW8sBZedOQlhiN3WSwmtOl0WSrziMNcR0eH-I0jqJv1xeIJQYAvtx0grc2G8RYHVoce5rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0qj4l52BQGkHAJY81-pOeOemBrx1sKSe1gDI_nAuoqoQAdIQXuuRYFSRnLFXXuXbNJrUslk3dpQdVql_T0uOZrNYy_GO0MRen0XEkAVpbCHU3CKgRNVL4I6Vlv43ri9o0NesZ36IiopqQyFAPZK8r7YDOZb9mtWU-z_zy3ypKWLra_sP7n9zgTc-84HfL_AmXLwxV8Vn-dGvK1r4wMZh0hw0zsnXWrYlGsFsUh9eds-pl_IqEwcy43C3BmXTs1nTLRVaFQjybp9IzDT-owkBi06zkuuKqaW8UdRXCJAl7BeXqBsuxlLEAkS0P9zFRlVV4pZy7SIQX3MkkhM8x3hFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zw0syexH8cZTsz31-eYV7k9xpld9LsX65bLg7l3CF7wUrGPmJtum5piWm5pVyINgopB32TjJCm0BB9shmh1MxUB3ql1KdNpBwI-70hfwqJtrfH3tAXdT4wbdpfP8F5fyEbp7kUTpilt9bSef-E4v4VILbHIF80oIyPJO3YdgC_5QoPtfM7Wp3HaiIZ3VOTUmvoNOlPjxZMX8Gp0k6tJXBUbX1tQIwfbSOLtPogmWU2z7XPVteJrKVCCc3KHqHPdiBDldd7wswk1nL1dVmu38iBahrYaUtFlRGMXPjRfDy_d28f5poQ-S77wmSmKRNyAHNX_tZBIrR1Odd68UZNXV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq3EL7OlCKbJ74dcmtg1hBDPcqbTRoGyXyrYx1LM8S2BfBVf5VqrGiu5_l6PSnwsQjc6VWVuihSQQtaRxviUPqy0PNwRaAWIBAxMLMede2iekIbw9Q2oMz8OsY7RdT-6ZzKo8A-B5Dc0ZYj0gA52LAGzJiLvkf2OI-dggweDDvximh56WfT9urT1leV-i-z6r6Za7ow2misuoLcubTgusPGII3HOxKLiwl3DGlXYmi7uKRVHcNkMR2pGJFt3QevRnX9hdbDfC1j4N8ezcUvPCgz8e7Zrtg6k-Lm4bMMixkOTpLPQ_oPF6v4oxuCZdY197-0LY34lUx53KE8JdMonhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1bRgcy8UW6dnbQkbDSvHNixH2DO3sgIq3FaEPsQ9e7RXh8zKfZfMiSBr3OvoImhNq8-aSZHCUNeMXzm0glFkracI08iLjiGgPTlbMM0ZmrSDWF5gIHXiLXQU8YQXF4Fi2N23zv-epdb7NMJYsyjKwAeiJf13wW-OAzlW4iE8AGfqzzXDdevErRr3wQt50AxxaHoa8IAvXNBY-N6nvxq8SFc4pCAUSMtEtcXVMrJH3K1K-8JBYCZX8ND97Vi8_vtEMuNw87M3jLRFdQuaxYBOKKS6DogXHDYBGFkMslmzM8l9928NF75VWdoRSSSFPqOTsoMFyFfpG5OKJBJjVJobg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=ubKcp-jawIWRtoKJs7xcDeRXXwAl9qBSHTmaEmHabkbMemZbRb569J3sTg1Pt-19LCU-CVbtUhFFSZmf5JUA9EGO7GF3e8I3qo-foK_tOT-oQDAmt4xZUabV7QFZl9oPPrQZEHOVT3VvBNl6xJGOTyiHlXLYWKvSI2yzPc7tsZBCT7-whQ6gPJBcy-P3Bv1YNSV3dRFEE455ztC-d-VpQrFKJB-aJ_HKbxmdIL7kU0AzKR2L6icYJsb2pLR8lO6X3AeLFqjvpkjmnMVL7lkQEx_G9FyuhCuiH9w-fDRTWshzqaDDFMRb1Y3c30a2m5rLdg0ScUrS9L92rQ0TKZENqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=ubKcp-jawIWRtoKJs7xcDeRXXwAl9qBSHTmaEmHabkbMemZbRb569J3sTg1Pt-19LCU-CVbtUhFFSZmf5JUA9EGO7GF3e8I3qo-foK_tOT-oQDAmt4xZUabV7QFZl9oPPrQZEHOVT3VvBNl6xJGOTyiHlXLYWKvSI2yzPc7tsZBCT7-whQ6gPJBcy-P3Bv1YNSV3dRFEE455ztC-d-VpQrFKJB-aJ_HKbxmdIL7kU0AzKR2L6icYJsb2pLR8lO6X3AeLFqjvpkjmnMVL7lkQEx_G9FyuhCuiH9w-fDRTWshzqaDDFMRb1Y3c30a2m5rLdg0ScUrS9L92rQ0TKZENqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sWSQGhB3DPI3-Loo8oO_EVVX95UhzyGOCR6SapxPJ5ZQFGurvty56NrFB8S3z0dYLkEXUfbBWKQ4E88kAuDWRWX-5yNdOiTFycs6TuIbZBKa7qv7CPWf5HFS2a4yEF6IOILdWA6y7FFGwW9USFKbqYJB8BP6wp2-DMiIZ4QfAbWkulRoWv70GVGxF1FIiLCuIQctnbM19XhR0Q5eQtsOh1HxKsdjEwZxnF2NB0VnEccytT0cY6nFXPdApOnarmiUXXFfE-iCueEU8XQbIvDQfy6bc46srYB_opabMFPR0aa5h4nCJbm12DDnZ3jvcB87A5SAAHrtEwgG0HQCNiCLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sWSQGhB3DPI3-Loo8oO_EVVX95UhzyGOCR6SapxPJ5ZQFGurvty56NrFB8S3z0dYLkEXUfbBWKQ4E88kAuDWRWX-5yNdOiTFycs6TuIbZBKa7qv7CPWf5HFS2a4yEF6IOILdWA6y7FFGwW9USFKbqYJB8BP6wp2-DMiIZ4QfAbWkulRoWv70GVGxF1FIiLCuIQctnbM19XhR0Q5eQtsOh1HxKsdjEwZxnF2NB0VnEccytT0cY6nFXPdApOnarmiUXXFfE-iCueEU8XQbIvDQfy6bc46srYB_opabMFPR0aa5h4nCJbm12DDnZ3jvcB87A5SAAHrtEwgG0HQCNiCLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=oPfhm6WdrWfTPBLgHsDmjRh3-DSOc_NA2qPNjpBH9xQyDZaFSEpLX1yCDttxGDFqba8LhpnBtDKvYFhoHHloyELoTm_jVtfT8xvIvS27zNQBuYnKXzpVLqh5guLZN4opzqbw-Ardkz_YaMMPpn6xZ51jJYI_4-OUI8WPpXEkv7npUccw5y0ZUdVhkszPsBWhVtWyE0oAqSgWbuYUl-qEvXhQxmVN7nB7eR3wf-TZKq3kKoJ7epXQB8e612Si1yLRv5Dlk7ple_LOIFfDm-KfDa6NiLxtvj6DfO5R2Y2cr9wpl2T5vdlwJqnDlUCA1MFlMgG1GDezyenUo7W6wwi4XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=oPfhm6WdrWfTPBLgHsDmjRh3-DSOc_NA2qPNjpBH9xQyDZaFSEpLX1yCDttxGDFqba8LhpnBtDKvYFhoHHloyELoTm_jVtfT8xvIvS27zNQBuYnKXzpVLqh5guLZN4opzqbw-Ardkz_YaMMPpn6xZ51jJYI_4-OUI8WPpXEkv7npUccw5y0ZUdVhkszPsBWhVtWyE0oAqSgWbuYUl-qEvXhQxmVN7nB7eR3wf-TZKq3kKoJ7epXQB8e612Si1yLRv5Dlk7ple_LOIFfDm-KfDa6NiLxtvj6DfO5R2Y2cr9wpl2T5vdlwJqnDlUCA1MFlMgG1GDezyenUo7W6wwi4XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9fSlvlG8MpeEHhl4Py3bytseI0ZHrouJLxMfbux4O8fHTlxcou2yKoBRE6fz3tOq5uey-mfHlOJOd0_Bjh4KfRlDBPXN8CSCMai-eObWeq3jtTIL0mLZQYeCL5H8QVMk-b8mwqGi8OqZhmTccOUeIwzyVOVTFkF5gD74lXAAEpkVdRDs-fVyAb6MwWc4u-Db3Fd8JYsE1bgh9imueUhKSY4iKMoGjoKGAOSCqayG-DWCnTtafHE0aksMVAG2UlNgNZKiCuwndYhTE41uwHvS2H4B7SSk0sVqj6oBFcDk5fYILjyvw389XwGy46pkZNrHhOMFz1rnW-g0AZacCx1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc-m84DAmkcsSEJuqUwUBdZw1VndIMwo3r-tB5nQNollZvgyK-FdiGUkaWGrrpJCgZdVrxvSFEKSR-OuhwtvVU2vIF_yW-osQ47TEyCAExjvAoTdnFrompFS9nV0evgKs1topql1EVoJOHooVktnh8OzBF06CMMOmNIH8TA8nJRsIx8vHnqNBtSHk4fEpJxw4GnAZUm9sQS-f8HDcWuRTiI4i5eKfXJ-rWSzH96UCQrB-4nnpvBt5Sywn_0ew0WlqWc9Gpzyu3Q67yM4upV-zZ3zlwnfdvmYWu-aH2JmCxux3c5F1JMFKDmUhCRJJlMfaTCCO5KkCnm3LBaMMqalCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2jXXUHYZaMTfDVg5mXK0goELu1pYqGxZl1ERdyLH0JWwTvqD7O6VJQjTq62my2LjWhsYPb5h5ar9m4fvGKKm1XHuJnN9_qLqZh7ibqea9-0dI0-T6Fc-2oKgqHlPrz7ttuvNGqoP_LT3p1tqnJw_HYvDT87Ev9yYB8kKkI80ZUTP65Lvm9CPkN1IOgo2RvPnkl5ziQtPIXWdI2NX-kfiYgV3iyiEKA0u93mR1PLOXsSsDjDJjm5xGMX-PWak-tTtwbUfnDuAfG9v6Khdp-Xi-VFKdNfRnQmQiKaJINdObJdAYbw31J422fsvmROD1mdGBfZEcc8GGb1k-4LwW-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWHAwAMkS9F7IXHznGP1yEu9i8J01toFbImfqij_YZHyrEo32VxQ_Gc62JEYv6LuXiI1oej1Y5hbQowmC4xv_h0q8NVVt2hpvNpc-1demreqRbwQhglg1XaJQKNoJKOdlsQho6OYLDNHNuFmSlVkfJYpClMcsSo3177e9LHXi6fI7-nDqEN_moC0dQj3-_kRg5EIB4UrW9xGzMVnQcb_J8olWlYx-Ku-0g4jH7RzEk2ii4YqCYJtVi6zTnEiiv_-Ma1_TKeo8AsldpYn0tex0IWpFbTezIoQQ_8qCMKznUE_zES0ae-WI2MI8Q9j2JH4B29CDSeqHCVpznr9DOtvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=LvzpIHMKKPcEc1phQ18Dnb-X4p5Hi2k9jkbGCb9Rsm10ufpmIQrxgAQHkbH_STzU-lW-xrcCz-RPTpy9-MTsPnTfGKYU8H1PcqyBZw8as6Hvx3_ObygiEhqhEERW41SrLj9mr7gl4xodSHyIL9B05lcrPihwfv8r5i5CFu9i-aol8FP115-LOpD81evvd67Wfgo3GghMa0dC4OXbXSKNvPQ_iImD_Sf1JketLt_wQw8WubFOopm4SCS_PpfYd06ZX0A2nnVQXvJGQ1HWNtNJ1EY3rk1951bS1ZP418w-GcldxKraiOsFa17y4p34olzQwqWwOc2Q38aSTDGp_zwhbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=LvzpIHMKKPcEc1phQ18Dnb-X4p5Hi2k9jkbGCb9Rsm10ufpmIQrxgAQHkbH_STzU-lW-xrcCz-RPTpy9-MTsPnTfGKYU8H1PcqyBZw8as6Hvx3_ObygiEhqhEERW41SrLj9mr7gl4xodSHyIL9B05lcrPihwfv8r5i5CFu9i-aol8FP115-LOpD81evvd67Wfgo3GghMa0dC4OXbXSKNvPQ_iImD_Sf1JketLt_wQw8WubFOopm4SCS_PpfYd06ZX0A2nnVQXvJGQ1HWNtNJ1EY3rk1951bS1ZP418w-GcldxKraiOsFa17y4p34olzQwqWwOc2Q38aSTDGp_zwhbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=mNLSoRWb0Odf1LMbfXeX8SuMgNuKNzaD8EJtO56ngi3ixXmG7hbPFQ8y5LcobtKY78jFbPIHrfDa3SSTRZu0Qw6sfnLrn3pO6xdb8XIBW9Ulc4OylLe0AxLq1kiPHjkkiVaY_Pn665QXI9-ZEerSCf9XVspg4cO82AIb2Utkz6navy6i8E7L2LCNhVHcAXPG00darHBXxb1XJhwXDre_bR5-UMwd_rVeMtcwtMvG74688qDy34WY7NBFaYg-3m0jz3_c15p7udMdlDVq7OHz1SKLGQsOengszmjUa-7MhkJFdia0y3No_am8DgnXOnoyd-PgrUpKt5iShGpX9JZrXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=mNLSoRWb0Odf1LMbfXeX8SuMgNuKNzaD8EJtO56ngi3ixXmG7hbPFQ8y5LcobtKY78jFbPIHrfDa3SSTRZu0Qw6sfnLrn3pO6xdb8XIBW9Ulc4OylLe0AxLq1kiPHjkkiVaY_Pn665QXI9-ZEerSCf9XVspg4cO82AIb2Utkz6navy6i8E7L2LCNhVHcAXPG00darHBXxb1XJhwXDre_bR5-UMwd_rVeMtcwtMvG74688qDy34WY7NBFaYg-3m0jz3_c15p7udMdlDVq7OHz1SKLGQsOengszmjUa-7MhkJFdia0y3No_am8DgnXOnoyd-PgrUpKt5iShGpX9JZrXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCIixb81rEArQsmsRvYb7Nk5qdmpOp81ISN0s9hTNFfNavPwafrdbYoMaBEzngElSIGYbGaVrEfxEvqDPMZ01T_r1BSCGEASx9Gesftg7NS4oVf9XV4VuB7Iq6aIk1c_1PBm5GNCSdKBGSSqUWY8lhFfUm2GFsPpcqbCczYuwIPydLiC7Gvkr_KVcFMs5hp5KtOdLf2XyHIQar2oySqg_Gq0zT9f30dPzHWF6wGim8Rw_O6QxOYbRCr9dHtm4ygkmptwi5X5Gl2rZnsDSGBPooIdgnMmfI-F39xpWB3FTF1AIhLSkTrdEZj8Zqi08-71xpA_oK_VAceFIZCCtsAGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2_9dkIcxRw_n_7k2IxJxLpi-3NQ_OMAn3weMRzkIOqTIglfYI1PbXor2egOtwmcnZ5WH5VKppJusyNxHCaTmfuFwXwR24-vptqbrkeiPd1vUbMxd1e8sQdMluJ1yLlr2fXyiS2k0H7I5P5f4kAyxmuxmhoIOfQM6xnvnGojfhuE3aNTdInjGqcG80jR_WzXB_NazidMc_Q7h3SQShJHYjaHxawvTqVaVmVswsoRI7xAbCGjh6vMSolxVZ9SUG2OwkBgXlomvgT5_sqRzmSCS0jHyLVcgPp6nvaM9dft-vv9xGCGwGmEvheKcdIIgpzX6sCHMohjdh4GyZD6ZpcsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdmrI9lSCPJB18oWVt5WZrC41gW9QVFnj0HScoGMFb1dpqszioW2hECCnRp7iDlXT0Syr8ZvScXbsgzbVt5dX9FbfLBZxsf3WIub8XjROBzmtGNdU_JZZ61UC3L-RwEvSvD_j1513E4dcGtcXnzC8G2c-5S15qK30VgIIxOkYIYsKxSCkA5gZb-y8o0aCGs1b1g4mEWaGYFbVXpo1LzyYvLnRL9LwBKbE3ay7oU0Tl2Z4Fg0vRd1RFz-knz7MlAd8JfuWfggBYVJPbB3o7TgQpjTA8OIDCa-2UAeczr5_Z5uU0P_L1doPsg23ccsRXXBIwZkQgbmgV3s6fiKzYCcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McDcRBta0QOjQNA3l5R300f2ECqyPcYdCsCup5uOaNXj4XAOuaEGVsdHe7ATq_Fxew_95HUcHgycqhOzri8CcJl39ujhd7WEpbdQCptZN9_Bj0AI_QpWA4dO8NY5htlkTwpUA3ZyLqmmAgDNL1NPJaTBxCi-UvzBi96dYPOALQ_ugyrGm12OhB2W-WojaOFRymPQH_ppKGGCWL_LRdIuFfCOMfnrRSYs8CpQ0pFYFdyiwmrNf1TiOFY7hCotEFqbosRZLdTZy5gU4sQBW4VnCziNWIVKRfB5mijz_PkiEJJpNrz_o882P8sY2m06ovydQ3gQ0m1Q-v_XMfmKHeGTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWO86RNwEeP6keBrXx8biruS9QM8IvlEPct4t5ZL8ZUaflnS0V066jpoPlsaPOM0Rv8FXZaBMFyT-WCbz03mzd4qFPyRBQ8-_HpfweTkWR4eHIvYOZ9lVG3UveDdVdAZ0-w2Bc6peMXK8KJeQ5djPRdtvMtCvzuexxJUIhLnEbL1vZFUV-LCWPXeo4kJz-RipidYXuAVyyIilaQtY_yo8daXRUFJIUfnBQ247L6hvPZoOQWFwG4m7Qy9pEwP70KV7HgmYJEwnx_AkSTmo8VNZ5Og85g1Z69LmBS16ys1bh9HozeUmghQTgdUsuwXLGMF_Gegx5Hrd0OYFjj4KabNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6wez3hIlng2to_cELUwNRM5ZfJAzFu8vxpZpgZZLWGZHYuAQeXHxYbcNXpWNvPrCStCCytmcZRBNAGHLKXpwasX7dKe6ZrEJQDyDOZbkb3arKr3cqhylnWp22ntxvJKMXpRVX7P6wRRRDpQ1grlRZ5MxQndMvni5rPSO8bpZRF4DxW6bt93GpA-as96W6MWUTC09Z6B7QLY79LGd0mMYozlAnOG-yFdA-2iYMFGrzJEmZgoqhmQVwUUap47wBSoRvRIpV5YqdD_T3TYU6ydVyUGnhl4sdIL41UiuI3Rm0SfUfWrZ60EDZJD9YY0-UIQzVzlENYcLWHEvB2CTbDuiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ix0Tw-8YjOYkbIqBCgGRt1zZldHRW0789_0DyRhUNaFQVKRcMalNteKrO0piiSpVDD2X1MfCGONoVyze5Hl4Tg6l6YBLQXYTII4XozxZ64DSKKZC4Y8yZtrSHds7nY5YYoRbQkIU4zCRjfcaIolcY2Xw5NbPxgJQ91u8gANJMBN2HBGuGbM6B87Vb_Zfljl9hmemVvpaZPVVO348xo58D2f_OuC_eOehwphOW93XajdXUGBR8EZRjMAU2w2piUTzh-U5a8UBcg3QD_Fb36KyhZRGHJzdQRRbqopVVnkVimmgoEr9zdEruKSmAQXYqp528KT330EXeB6Irt-HhG-SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/df1NIHfo_JnYTu2CCcq3KH2mluliv-PENMZjhSwmAWNOm27YAGvWOFCTs5rWMFXDhtb79WWStmatAuj0Zc2HC1Ud7HuBNdCqJPnU1wFym0ZkFPs5jPWHNFBokTjhhLFRFiH3bKXQRvc6mvgzacnY3OfrKSRhJPoQZHgy3DNVeqkHIW728jRst694Y8rrefU2zO7bCh-EXuK5zl5nsoQWHN0_CJuoezXnf-GEQGMw3mRCqPJn7Ny-KcovDb4wP0ey_OQ0ZnuLCVt3vZTiYEQzbvNucoaZuqNJHC-KZpiNptv4jYLjlXJOlNSKUwIo3J_hU0QxXoc0l7twmsht5neEkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=fOQiu3rmV_dh8A37rFEtvNl-AgeTArmXvj7LpZ9ujfPEaZGBZjfE1qeaZthjfbeA7jCJsOpR1gqdm0SV67OVg9NqHYqzpInFTjFcfLohfMzyD-IxubNQexgLa_wPWewiTb0dQP5aUVCsy3kraAMMXYUDMKc6OzeECoPiu8AGiVCq5A8pK1KtsfZd52OrWQtUAAjNC3za_yWrovMQpXUBq2mhQ0RcNzpQ2UZDiamoTPa_wJcp7XGE5RHaqaw6E5C1j5K_t82C_Y9wWCkKyHQbRGal8VAKfwd0Mb1p0CSFQ8OE_yUh-L0qA83UHBzlfO7Lk1WGMFlaj0OIMcfMgX0x5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=fOQiu3rmV_dh8A37rFEtvNl-AgeTArmXvj7LpZ9ujfPEaZGBZjfE1qeaZthjfbeA7jCJsOpR1gqdm0SV67OVg9NqHYqzpInFTjFcfLohfMzyD-IxubNQexgLa_wPWewiTb0dQP5aUVCsy3kraAMMXYUDMKc6OzeECoPiu8AGiVCq5A8pK1KtsfZd52OrWQtUAAjNC3za_yWrovMQpXUBq2mhQ0RcNzpQ2UZDiamoTPa_wJcp7XGE5RHaqaw6E5C1j5K_t82C_Y9wWCkKyHQbRGal8VAKfwd0Mb1p0CSFQ8OE_yUh-L0qA83UHBzlfO7Lk1WGMFlaj0OIMcfMgX0x5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=k8cSAK9KXKApGg4yZse9d__gqcEXBpuuAH8c4xE-vV7m8X-OjS8LQ2-QaNykNFByX44VAed2Y4abDdnWHpd9CIUhKbCTSEOW3JHNTAIPkTTgyzHpGRfhnp6vhhum2YUCN55Wt3WN9NtQUlA2Gqf4HGBXZxpybsRMKAe2xTpmupPVmXI4ia1MwyidrYiqFDO4toOrvAE9HLpBCbZy-gZXiC90P7wjtKQPyj0dxCydEsXGPQFPnjNCjgOPamdmHqZrGb2LEiT24eaopBs_QqvinsnjcZngoQdNfUQM50aQP30vsPI2XvhXZiozwsjQHtjGzmt0yLDMEz8-P_oRtu6GBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=k8cSAK9KXKApGg4yZse9d__gqcEXBpuuAH8c4xE-vV7m8X-OjS8LQ2-QaNykNFByX44VAed2Y4abDdnWHpd9CIUhKbCTSEOW3JHNTAIPkTTgyzHpGRfhnp6vhhum2YUCN55Wt3WN9NtQUlA2Gqf4HGBXZxpybsRMKAe2xTpmupPVmXI4ia1MwyidrYiqFDO4toOrvAE9HLpBCbZy-gZXiC90P7wjtKQPyj0dxCydEsXGPQFPnjNCjgOPamdmHqZrGb2LEiT24eaopBs_QqvinsnjcZngoQdNfUQM50aQP30vsPI2XvhXZiozwsjQHtjGzmt0yLDMEz8-P_oRtu6GBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2zqycoLvjgOCbGqoChAg8wbSIpA9AsttL-Zw8sKkCSAqP2_2qcrspxiac3lx2CK8YUEWJalLcfYsTqEh9fbiRKeNPIz2Ukml46MMWRoNA1xWlkvvdKL8PTA9vF1M07UCreZGkH-TEklTid54QXeQL2qsCaRx5IJKPBgYykpP-dG6voiFy879jbH_hbbjtyNoUjA2QjsXQVWpHRpSvNycdy8_L3ohMWU6cPW5YjeOyt8PChMG5jUiaI9RGUzCNd1Mt5EI-eKCA666zye9ESBEj_3MuJvgT2527FerQpAucppm78EHWKmMVf1pJdRdeGDXeAS_3sTeZ-l_AI2AJebAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9wHnl7rGXvbbcElUzngAcD1FJoHb5aLLdNyf7IHTHRuaHXv4M_xlWGndYtWzztP7RwnqVnc9Egsv9oeV1saYG7E9eSYXU3X7m0Yo6VPYWIPpCTQwhQ1xwmvfzuIonju8-m-jxSFfMBofQ_XfW9G61BVgXY8pJdcKqLXpj7uETL_jSFdtG0w_h34U7vmaH_vMy4YZAizhAJOTPoTFqCDboP9NleR-0UdPYuA2iwVqfn2nrFDqh8tEq0r1dRrIuTBYwMfFUldKDvmjE9T1lsJyKRGurFpasPGOC4CuUvX3sotAFs3LFQHIgTybzFy3gRA7gp6PWQGmD3KRmN2O6Qg3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=nq4qwZoDbaFK-9cGqezEc0cv93CWHxwyHRfNGCNBpONwfiWITB7FShQeScRJH84j8bbV7tqrl1MONAeFqQj7UEBkhloxTP71JvFULJzThYFJSHWgwl44gemUjY8RFSiB0-l_3Ohm_JPh2DHTOUmvXcPawUyhb_iVGhXqabEqXrPb6EnsV_I7wDGD2jrX2e0T-CO4eCKB8xrOH874ko9TxPj9sJ-fkTTCyNPwGsEApkTj5Uw_XmtImhwgrENZ4guGNiVRuDTlK3M78jP75jIW_otu5iKKVIna3svE8xuO6RcC1jqejcW_iNpjZb3G8-F57OZE7LLZdVTYd1tm74eH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=nq4qwZoDbaFK-9cGqezEc0cv93CWHxwyHRfNGCNBpONwfiWITB7FShQeScRJH84j8bbV7tqrl1MONAeFqQj7UEBkhloxTP71JvFULJzThYFJSHWgwl44gemUjY8RFSiB0-l_3Ohm_JPh2DHTOUmvXcPawUyhb_iVGhXqabEqXrPb6EnsV_I7wDGD2jrX2e0T-CO4eCKB8xrOH874ko9TxPj9sJ-fkTTCyNPwGsEApkTj5Uw_XmtImhwgrENZ4guGNiVRuDTlK3M78jP75jIW_otu5iKKVIna3svE8xuO6RcC1jqejcW_iNpjZb3G8-F57OZE7LLZdVTYd1tm74eH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orVAxoLwRQNnzxy5088Fu-pIcKGX0ARQTGpmIZT1LUXdbXP70v-b_4Oe0bJN-y-0SMAZRRRnbbMrfWF8FwqprZKMIfQswn-awrF4SiDCCX4l9ychiayNUjtIyJenpfCWZHTyqn4ycl5oU18wRnMMkWOzVGQAZmAOs3NxGTBtuOo0vhfKrN7sCwlFrutGNKjn8izpU5HnOixKAtAswK8nmA4vmNN0wLKczJ-X_8o4EAq9de5281ixZUjw9tEGI5CRkSa87LqjN1xDXknwK1qtHfJ0Ey8yFwWXNDIYHbHYtYY3_qLcOhjdEHjCYMITsTX_DWWetbXD1zE5CZb5BoGSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
