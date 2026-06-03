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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7MSmD4ceg44KxOVt_gVCsntJEWKwc2FX31xcKBwYnKqeYikgwIdPMWEs-InCiCL_kPIN9qORACCUY7Cab7C6lec2w_dcDAUuaY2cXJwyuALsygLtEhOzGWwrj-XBxHPIVQ93QiqGBeygduhDOxKswXRP395TaUCj3t2Eumfv2-J8-oHtpFoM-Xk2aBtCX_EpyZMOGdqSkmlyKCVbhdR1o99Em93pBqWyo2icaCTFOlFrQMY8_KNIPpBLkmyz_26qvVmBaTLXHDLPPcxHkqiHwqCFgkjs38XfGPri4HFaoWS7FXWQyJSQj5X8sQDXwIkb88FuKIaGG9ZJqBcDtWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOd_FPmjDaVIglxjgZJOkpfDlQ1-h-T35qIZ159v-JWrrN8OKnKKbFHcIfuVQnvAs9ksVI-VgYvdfLv43Dr3vM-PZosCBzyZ5pzfpLjpfUiNA6xl5tukbM11wbElyFlJ8B0oTEqspul1ggtq5loaQwl0o3ZYk9isg0GMQCwKSbl8ToEUAQYKgY6rGP7Wq3vG40-hV03NnWfBJ0oQ6H9JKuqi03Bl63RrOPiBhkxgmc2_O_CAIXOCvFAw6t9eOospGvXx679NV--D5enrhkDhXektvc5s3onaraEo3esvESH3Dc_dL6fWTzpvS1gA794A8m33YD9bwrTWtw2L4NJxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5Eq-ZaeZa0mxFd0lWgsoUdVSYsuEM0k1Lp32ZaymghYzd_K4hUybIvUImVYechFImJnnPe53b4Zd9gym1JHMP5cEfng9R8-5inXFtqV6DVxKnxSIJ2JRlzZdu78HZ0YhUe9k725Jq3sXu-FVUSI-qQh3yRk94yay5o0vUYz6pnpJJdkwwb0LvQT6m-TOvUUa-W8xHT5zwwxRK9wourPj83I7F0r55JIqcyNd_MCdCrcCrxeOYAquFIDSIt56jLPpfbKDdVMJcFqIPYA1vfMVg2Jo1L74tX-qT4bvesEGumulrJxbgldYm8yvv09AfkLUUC8foiMCULIuQyJ9Jukgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UP1YoqD2zKaB-QpK4bTi7QxsKhXXGeqp8dAgaXziNRA03PitlGENqrq8b1vtuhkzrw_MS1pow8h3yX0OTF6qmg5dJZ0s2PytWocru0eRdpS6rUSbOzbIDN26qasE3gb0BdOGwphOMgYv2JrP9usCAZYvsXOpxD_8CP0gvYkCARExkUKJ63BFo6G-2GxbNHvl1ifmu0F37a2-SLnZd2oNCVgnyX_ZaOETzg_bD9kngqIbNEC5_aGWg_XOdAOAZcgT36FK8c6Txkrxq2GhnjpAMyEqhYOqLXk5p0MiJ1jQyMWUdbPt8qPAr1chF9E5FRSkHDmS90L6x1owkcl00TJNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzRzwCHxKZ5jZrFJ6f18Knb21jB3rYbHe6nHZBG7whxAWWZW8u_Bh43UVBLBZqnfa61ocxEyG4X5yvDPkzutMGhgrHGDMIrOaaVsX0GDtiVmKxwKU9Irc9qq7P_HesGQ6OrHbF9rJ9kRlCgxBGhZmjdeH2ZXxE1RUGqXQqKZo7QAX4tWk0Ia3dANJQyWcaNacGm6oLUo8JH8r6sCSLkvIhxz-L22ghOVwgwXAY-cSHWOcMPb3SHd0Dz0SYRhxkNuGsLNAVHliyc6wvuzGgal1Qcon4eEf5S3tWCWJkmg3xV7MQW9kUsH0nvZr1T1l27eF3nljoYaT5pGqNkZJF9CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEYplLELLwQq-E9ukrEhqDtGDS9X24CEXFLsSGTMMfmGplnWjLRGAJ4sCS0zh8aNYtiew0XM75Bnq29otbpKr9kWcX8UUuT8OHCxkvC8dhD-J4yfB6DNpXPK6dZgEEoSsj7DmG_cjEzBoIfX7vPDNGys75ALXow9kY61a22TS1sKHTyIg7RvxF96yR_d-MnqbmuySQmi-8B00jx4AelmQOhQ5jjybBLAYRdAdqUaFXsY_twHEmdBKDqS-35X34pbkEl1yJJjVzfe9L_d82s7u5X-vcsNMfQq2WkmvlFNWAErK3KQ56jbtayo7XN513Z7aC2jkh4LMGHjAYS8FAZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Z9fOpG4bkPz6wo2WatOYP_mc6X7cC4gC4BAMQYwbUHS8XKN6STpH4SNsSBML_O51eLI4e0E9RKXrGKUqUNuP_mcvSGnBImZjUnw86qmpIbAUqDlQoVauhsJH2oVoNQ2AGR4aa-DILO9u7GOM8-bG9vBPwbnuG9nEO9FcsemFrbSYZ3WFqNIfD-powQrGT33zQzDrs61Xvq_EVoXq4VStIgSnkR9rTAZ4jRr3HBIgjc3he6GNztrRZ95tIaOJNrO5gD2y0cthNIWifjGz7J_afIvCDP7tTelrlpNSODP6jdYA4W__8fN-_ySWXpBXKvLVPiM4HF74hFEhkMSfnbgUfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Z9fOpG4bkPz6wo2WatOYP_mc6X7cC4gC4BAMQYwbUHS8XKN6STpH4SNsSBML_O51eLI4e0E9RKXrGKUqUNuP_mcvSGnBImZjUnw86qmpIbAUqDlQoVauhsJH2oVoNQ2AGR4aa-DILO9u7GOM8-bG9vBPwbnuG9nEO9FcsemFrbSYZ3WFqNIfD-powQrGT33zQzDrs61Xvq_EVoXq4VStIgSnkR9rTAZ4jRr3HBIgjc3he6GNztrRZ95tIaOJNrO5gD2y0cthNIWifjGz7J_afIvCDP7tTelrlpNSODP6jdYA4W__8fN-_ySWXpBXKvLVPiM4HF74hFEhkMSfnbgUfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=fDEsPlk8ZL1xSONeyCpbZ6UU_37jAiVsMLLR4fXbk460opSfELV_viw7sLV6oK0uGF7-Sl0B5Zb4VQUbFwVry29iOfqBoPHZ3uvApZwh5scA_WsfvALJWSd9FPy4ec8XTKCPfL7Bd1S_BDAmkF4MyDCL9tykECYF2PdRYR2LvNj4-m-H9xKU_SG88pD0xuwxRp_9DX84PFNOiENUszDV3HuVI0aBHUOr3v4bfHHLDxNMGfoF_t1UL7wSg_wYI5GW2vFvU_PZHJxwVp5hKe2B25WlCZ1FcBpEmfDxdA3JG76WEam3aCBm6IdBzM_ydaPFWmMT4DPmbZS7vKx6XEljwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=fDEsPlk8ZL1xSONeyCpbZ6UU_37jAiVsMLLR4fXbk460opSfELV_viw7sLV6oK0uGF7-Sl0B5Zb4VQUbFwVry29iOfqBoPHZ3uvApZwh5scA_WsfvALJWSd9FPy4ec8XTKCPfL7Bd1S_BDAmkF4MyDCL9tykECYF2PdRYR2LvNj4-m-H9xKU_SG88pD0xuwxRp_9DX84PFNOiENUszDV3HuVI0aBHUOr3v4bfHHLDxNMGfoF_t1UL7wSg_wYI5GW2vFvU_PZHJxwVp5hKe2B25WlCZ1FcBpEmfDxdA3JG76WEam3aCBm6IdBzM_ydaPFWmMT4DPmbZS7vKx6XEljwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bZy5L0-5UJVZUeKN6zEquNKbHp3s5d4Ggw5hB4DakW8a9K9aEHSlSnRaj8-m1SSaQuQ28_KUaLjZtAGvODPrpHI1i1N0sE3cu38UiEHGd76iJEt0MTU9Ylmz7lGzHb0m6sJPh98z1MenMuoPZfSjMbUgtvesInrJZj5cd9hfVZV2H20GatN9EuQ6K9pJQ-Et4V03axfV2TdC15BkGTMsVQhcedkoK_3B_RHEhjMNxa7vdwWpp5lFbxz4jPfis-iQA3tyBEGFjeqP7FhWSIvfkQ7iyb5HT6KFvjSJpegDEq_vfWZZHimNQ49r3Uy-VhfnCxNOR-s7RB3zfBrgZaQr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bZy5L0-5UJVZUeKN6zEquNKbHp3s5d4Ggw5hB4DakW8a9K9aEHSlSnRaj8-m1SSaQuQ28_KUaLjZtAGvODPrpHI1i1N0sE3cu38UiEHGd76iJEt0MTU9Ylmz7lGzHb0m6sJPh98z1MenMuoPZfSjMbUgtvesInrJZj5cd9hfVZV2H20GatN9EuQ6K9pJQ-Et4V03axfV2TdC15BkGTMsVQhcedkoK_3B_RHEhjMNxa7vdwWpp5lFbxz4jPfis-iQA3tyBEGFjeqP7FhWSIvfkQ7iyb5HT6KFvjSJpegDEq_vfWZZHimNQ49r3Uy-VhfnCxNOR-s7RB3zfBrgZaQr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=XLnqgbUalwojKjYjqrHwTyNIiWJgaTgJ9yoFglzQwVTXMg5SeVAPy95XBvvgCCP5Ubk7R7uXs1ceilu5g0D3DM_n_ppxEtLzbDseRhSqwXMLKoRindbds8l7InSfvyNAfhWRKD-gz8klL5T_xpCCS2fMzU6TvNOO4GlwfNOUtnf5QsfS9otsPG5Ns__aV-GzsBud3Nk4UW0RCOajvJ2hPEc7h84WiIw121vE4jyVil_twyhcgOGDfSuNG7_WKrHBIjU2rfbG1mxFDbF7xRu6MD7PvStVMeTejBlBlNEWiU2WbViHU6yMhmKJ4fxa4M-VeEFKlYLWUiFEMue5SznEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=XLnqgbUalwojKjYjqrHwTyNIiWJgaTgJ9yoFglzQwVTXMg5SeVAPy95XBvvgCCP5Ubk7R7uXs1ceilu5g0D3DM_n_ppxEtLzbDseRhSqwXMLKoRindbds8l7InSfvyNAfhWRKD-gz8klL5T_xpCCS2fMzU6TvNOO4GlwfNOUtnf5QsfS9otsPG5Ns__aV-GzsBud3Nk4UW0RCOajvJ2hPEc7h84WiIw121vE4jyVil_twyhcgOGDfSuNG7_WKrHBIjU2rfbG1mxFDbF7xRu6MD7PvStVMeTejBlBlNEWiU2WbViHU6yMhmKJ4fxa4M-VeEFKlYLWUiFEMue5SznEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXRLGUopWwWqbGBut7dV0Slwdm4uNRn5O2fEmtEDznMWuQDGIK2i_V9xefpXntbM1TK8AzP5rmEUaCgz_MGOII_31fzzrm01ULbVdRv43x9kKXihpTuECe4gGhg2jxHSNgghUzSJtHJurOg9DEWXwZR3QY5TqIfkt_FVybmFMJRodPnDwr3G03LEQcTZG4Sjclq8H3rWM7L9Nmu1t9XIWt8Vc9GHtpNBL7H_dSD0G3o5_M8m5FDPihObefswgN-3ACUvueQIZkstbbk-99W07lGZAsb9AjsT17ygBV2oJ5ahjRvTAQCe6GKsobGm2_p5JqANMUeFTktDVvF_GwzbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sloixpHAHwbki48MUXiRtGO6R846Oe8AQ0eCBJ4bkyYoF8Le9495HshzOQ9onrxGbutRCbV-YkoOHGcN72YcBoMVTOD-fxJY0g3eq0eXrUF7V4inefSexI9FFvSseA-0VjP6z-4cssL3_C-PwCnYQQrhAlTj318EYZHFuwJqm_oycrgi2e1GRSF2NffYA3JfZaL8TXTcQDrn2lCxvI3RBIf3cmrUJc9ZNdLyDovejtUM1syK0l9Hd1hxLi7J5uBeYgw5JyYV7mhFHw5lmkYXnh3Z3la7-NPq5bBx8PpxJgl4ZHEH3eWoi6lXlJkhqfCwRFYZJaVzHgWKzgMM549vSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0qrLPRKv_QZ1UGHeCZlhgem4XaqGbiiScYJq__2GQvc7v0ysnXwcinhB-caTHQJhvQnCcRD6qohYJaMO5QsQ6ykbZliERa7ZT25qqZZqRcz9Kj3Yj1ANbmDcRDyhpSi_hDZqFjiAaMQB3UayerLBW5dwSF9TxNbQ09jqTEJxpGG1g14oc-NdZ_SU99W3SqyHuVnAcVQ7QgQNPN5BcI86awVRvXxlyadesqouiYvdlTSWaAuP8Mum8QmRLN3jS7TQuvsfK4TVrUx0YX-uelEgTfZT79-xFBhaNG9ZpaNRZzjlhOi2_oVjrtph3Me2YmATLBepRUI98qPeAWyyPYEvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du6pSIMaNkzER4Sl1V0abU8zE2Q4kK_T93O4_2_T203Y-D3a9ztylXEjMjX43z7Eabs47kFCLLhrltGjzX5GxkiLb1enOHi4wSEAqAfVzvklwsfhhP_xOgEIzWel3QlAw89Y0ROrohngMWaUiv_SR_CvX9TJYJFaLMoCbRjk5l1CzAcGMYT7KzI2sx81eXohITmlpg5VcCrJ4MxFzlPO4YS9TYl1jAwltbIDOl7ikDlbptNtXMvqK4tF9hce8_apzwknQQ9t23jlZjeklut0U6F_l2fbweUdCwbWSdelTn6dPFtP62WLKLkKKN70U6LJJiehnOpKp3xaesjlysOv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejru6mMsPFPa2_VkJpIA1jZHAVd9GSIZ4q_Y6t1lq0qyp1-wXEITiQ2G4frHmHWz4V7Wconz4dpetNlDZ6E0EtNBc9d8w2RQVN6IwzrDDWUxEYqPfMmA6Q32s2ipbqn99YWI3L_Rwy-QSueN1jkbipWNMQCeIxTKFkmkc6hyC6C0IIorj88h3SE8OoTaASwc6YxPwjwp87n1lxXtKjyc1k101DFiGjb9coAAbF1ib6EoUIiESa1tPasPHkX3pd6MRfkzH75tbm5q4nJCUNqNL8lVM50rV8romyZUfE2R_Aqjw3k6iinGlGFsk5zi_X_QTzBF12YmyX6pZtx7igGFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrRDOscSEKrrNcKUbK-iSwQ3c2VAd50xetHa1txZRw3_YX0fkvhfvvUxxGFFahd5LDtuUKKEQS_jREo1jYT-RbJ79rSOEohwA9h9Gbznn2Iow8qKi1ZVw7VJYzpYKY0V6rWoRCrxZmRo8weSRHJT2jVT5m1S2HTPuKN1PmZBmoggoCqkfeEUJW4GpgJdyHLbRxG_kAVUP9Pvnfs9o2XF6G283ffkLnI589EUFZlxnJkp3zVPOB94Y4fpqfOrPZUcFlDTgsjgHWwA7ocWw3cdPuNxTgd-DWWv4SCf1LX-6qriZ2cKWYRk4MwGcaCGI5qm3BDIh5z9YKXVpCkLD7f3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7TTOUmIlE_J-F44T-rSXgGnNomahk7vhI8NhZQAJqNQs1wklx-OcXpugKUehTa0mrstYCrCieRmiyjD0k4dZxBpuBr9ZryUAvHEbQlYXBLrRFbSvd6hHCBTm5QSVQpSKiQ2hfR8WGPT-7Rq1OLdAGOa4p6D7MUVYNm8axxtggDTylyJX9E5W-rIkZ06HadzTH-ZV4UUABgrRREjGuKBMAgawBxrWv6fFRIexM4kVTtI-NaaL2VPvzuVrh0u6EhUjTTo8wnvGFjbPVE--J-PX66xLgng25WrXuD_nBsT-Bt6FRnMp3kp8rKOiQwSxrgkgIbn-6GBvaMHf5iADSDijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=JU0OVG9zWVnSeitiWRwjzwtFub3ew35rTloxdBKTxojKZeVaTJvQ3ob9FeBWgfTQ-ht6GkhVHqClDq2oJJxGRuw8g-7vHOkoIHRUIFmz9MwPQCmHLTgXgyNC9tujRWc2YDCH43Oh9yx2UqVrHp6JkLoK4Px_D-BOUnaADvueT2t8UOisXG5dzSig_gMuDl2xSm4v-utxEW4ueuW9Tho3JNvB3XjpNEBPIpEBjlRfp0YCTd_qzz8oTgJz1gGfQJrxY9ElDKmoI-okrPckgVDvttmq_4RSA281ZP3lWPtjEyZF0IdSkhf8pFi5ExmkcU1C7kG1OUSI5f72QxZvDgeEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=JU0OVG9zWVnSeitiWRwjzwtFub3ew35rTloxdBKTxojKZeVaTJvQ3ob9FeBWgfTQ-ht6GkhVHqClDq2oJJxGRuw8g-7vHOkoIHRUIFmz9MwPQCmHLTgXgyNC9tujRWc2YDCH43Oh9yx2UqVrHp6JkLoK4Px_D-BOUnaADvueT2t8UOisXG5dzSig_gMuDl2xSm4v-utxEW4ueuW9Tho3JNvB3XjpNEBPIpEBjlRfp0YCTd_qzz8oTgJz1gGfQJrxY9ElDKmoI-okrPckgVDvttmq_4RSA281ZP3lWPtjEyZF0IdSkhf8pFi5ExmkcU1C7kG1OUSI5f72QxZvDgeEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKtdHQWArq0FIavan3gXhEc3jvbS8H6y03vj8Y7MX7jReHOD6kBjTE0sVC1aIzzxcwjHRxIBCP3AcrVlEfel6x1RpvyEkakx7Mvm8Q2CLumpAJIxYVj0Ni1nWJuUNANuHSnIPXX38zr3yLSAGs4jh0_IWupvLnw51ZM4rZ65Z2PkKwBnPWY9tORGjZFa-_WpdvSJkG256rsfW1lS_YqkE5cGiUqDBvO5ER05Fbguvnczj8gshHoUN6OJvebdxLXENNL_1GfJXHQYsl0Rcj4pe3XNLeco8VKx3eC5Eze7wdYGMNdi1ZN9fAevn4JhO9RSvhHq7hVGHUzvTgl_3ZS9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7xMnUMm3c7z-l5sDPUvI3Qlg66uYu8ZGqRrqtUpKXoRiCJVWquzO-3Zv1atppVBQdypxRpCExHonzxKXVkfn_fwUmZfubEOVK3_ynTvaOPXNu_6i17rUKe6BTxtG5dPbf9xmPKbXmNWvjAtI-5cowzCPmnvbcSMudONuOb1k40VHSLkn_KLwECOJ4dW3FTPkMM1tisV079Z5MhWlTTKuRy-lGkZ58ErEoxeyUfoUz9brZQYSLEO6FQu3WLtVV_4UXLj2CIloxCwRMPbNBZRgxTR_Ne0UwbZxVeYG8hlEvkEw1MJA0F-ywH7N1J8M9IXo6g6n5SIpcK7lxYSus31lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4UEPvDMYqLI_JQvBMckOAET3ZW_u198Io1ozGyLJVln4lVPGpjAabY7Pcl6MybMhRJmn0VpGURJAL4M-pEcFROxfV6mjqQ-4xSBNqRhpqwYOaR2l1SZQltQ18d7MpfygkMBXsMNDVDFlMoa1w1mEKsa3aSxMUXFVdS-XiB_LduqmqV9DOGGFjUKBT2nuHbci0B3_tgKGJVbYRtNIYHO8GG9HOKdXzWiflufLkkbg6wcyTu23AQER-7QQC_hyUfxQD99qCGascvh4JBxZv3Uh9aT2bWAt7Eh66IAoghk9maoVtyGuxZOxvtZEJIuKQavPlRGvnm2yy_HdUPToYjvhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwhoRrL-rjsYbiW0Rl7WYusHJ4NbSpAWWOypGtx1Zf9466mF7r6RGsh9FrcDxjC0LTe1RWQ0xg08OadXR8lAcR39t9Wup9o3O1RqEhZzpK9cSB6GdsOC0I0_qpENSvE5XPA7iiayUk0M9-Kc8DLVQmiZGX2ESkYOU4cZbw2rVtqQduiCVpNqHJWlzzPxB-LLwtM8fq20hFU4P_qwhOs4_NwAZo7HV0RwOMHjspPbPuJksHD1lnWEXUlNpU8s22bEIH_8sxkMGJS-wfAEwqis1LTpJw0P2Aykfs9yKOUi_pP7CmNzHuHQAbrOXiyiVbRM0zGhwgy9oS_bwrMiFNXuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLCE0bfnMP66qEwD8c8JmoTY7vu_vbaRJ86Pm7NHHHN2v6PDyz8LJ6blVNpu8_cUsLspjfGSUFCkQz3nUBvuhG246dLUxkCFpySH1O4Cw9HbHolDY0Q_fFRYKdu17gb9VtZsEVh9ogTmwLZ2CA8iu7kbKni-4uVVLV_TGCnoIW3O3jxhyTT4c6k-RzRVG-H7dZipwPtnaMDcoUiPNNrl5YWoeA1SV8tiCAOj5KoOx1YyXhqDTqQRNq9FZBtQyQ-zSx43bCYdPQyEizoux24TObVLbHkD7um1bXcjquY5iq8MmdMmkwyOKadY3r0sMn9p3cLgbilBHEBGspLQ1JlL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ELBRYSZrL3m5lVUjFeImUsLulUyGRDcDogrcWGNerEylUMK5rgiaS9VDXhig_F1cJk8b-T7BxLa_M4Mxbi6Bkd3yLnwcxZV2TJ7UMPspFjNc2MJoaDGMuOjgtGxfnvxRzf287FqqVfGAw7S83_9eQq7cEOEtj3zmwWFfpCnq5p25ado4nzlErV-02j5OxbYyzh4mY9NzHLrWxnkR69u8QJ_qz1XTRaVnFFCM3rOvDmQUc8w07goQsI7D35AOwrXAvcNacjfIWM8hSXzsIpFKpmehxxtYV3mNI9O3-uXjdSvm-9LKFjBMfrdYGvN9BtdwciJPajyuMjI7sOBeBg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoFx7bO-uihj-t5-v-H-aOy6FQdn26duz-GA3xS8YChNtXmo555lc1P77OoKUoTVqWh44zR44t5XbrFZkyRtvuo6jx1fXIDzK8h9jtExrHwSvL61afz86AX7gr67E7QrDzxzTwtyRSph9b6TUmcT0vS1FhS_7JOKn2FBm4gQU785qD1Vk6xUbLwAkZsZ91LgEYXg0im07eqbi_2T1cv6mna3RC7OHC2J7kF1UIKkI_DJNcIPL-kx4oMbKyF8W_dTEDuQW9v1Gdd7EKumraaDv6_zra10kRSx2S1smaNyELtA9t_TXDNZU3nYmtmVDFzksdU669mqY1m5m3QUaQbv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsD01lmwGsIHr9OIxbtmAhh0_ZSc90kLKrDXptG8GDOaO8xQxXcXTtK08RMqrIGTjD7vcioOIWvN_esPN8NFAUn6rGyfQKUmVTPKS4L14ryWxY7uPTeEI958e9oUFzkjPVetQntLcI5h0HdpVb-mA_8jpmUEKzARWe-aNApnhrvaupY6P8vmkWsno5Aawev65152gyLBuZwOFjj0fH13TvqDHh_9LzFVYOV7tFCK0gNGrA4KPN_aoMOqrYzU1JUjKx6h0LKaeTsgyHMnKtuv346uqSOi2C0Ei8QjiyQZaW5Br4Pfij2wbGm7stKZebrA_HvatI6TK8o47ptJngQDGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=dvMsPquOvNe4LiTKYwltyuXJloyxYFrbAaYjXFYQMYf2Qy8EaiJKr-1nwbAABiOlyMfbSI050AgyLWadTpuA-LR2Ikt9IJIHEhquxdIS2sJvcalgXDXFdSgTSKAyR1xw6okuy22P_P5Vaj_hJ0RWzNXCUi8zhKj6ilTHxNDR3kZb-2LdEEhFnmH9hgStub63r8B6Ar2CuXKJ0kFh6EqbhmeeC-wD2y0QgY0hV1EOfanJGDexg2FUfMyCX7NNo-NyaNsarHiGiNd3Q-HYjhjb80i8RbVRwTPLhdB68FjGRPPFUa_ZgYwwPMGxXMEkM6PJkXcxlLdgoYuv7HJFrpQSXhZ2HpP-ffUoOVU924L46x7Qvo9DedFDJLQRidPSTOx31v7q3TP7K98D0uo4XWjvN_MPX_pp8BWWEQ64y343bmTlImOfs5RtxcoVIYniDnZmd3em0FmDKfj622-W_GUBBEAQcB9xQWlC7YWhb3Uav6iQRnP3fK1C0yUj8khwHGfQ0umfSYvX6DhXQzLdZPuHeIpwfCa_bUTmOJAzZOvx3MhErFnjaGGhfSryALk5dyMmIB_hYCmDZ7Rg1BgidhIX5bte86kRe1mW7J6q7ORUw8E7elALFcOUD_gQAkC71dbxyDy6CeFtNkMmymI9rIZqDUMfxu7s93z6crq6XIvRjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=dvMsPquOvNe4LiTKYwltyuXJloyxYFrbAaYjXFYQMYf2Qy8EaiJKr-1nwbAABiOlyMfbSI050AgyLWadTpuA-LR2Ikt9IJIHEhquxdIS2sJvcalgXDXFdSgTSKAyR1xw6okuy22P_P5Vaj_hJ0RWzNXCUi8zhKj6ilTHxNDR3kZb-2LdEEhFnmH9hgStub63r8B6Ar2CuXKJ0kFh6EqbhmeeC-wD2y0QgY0hV1EOfanJGDexg2FUfMyCX7NNo-NyaNsarHiGiNd3Q-HYjhjb80i8RbVRwTPLhdB68FjGRPPFUa_ZgYwwPMGxXMEkM6PJkXcxlLdgoYuv7HJFrpQSXhZ2HpP-ffUoOVU924L46x7Qvo9DedFDJLQRidPSTOx31v7q3TP7K98D0uo4XWjvN_MPX_pp8BWWEQ64y343bmTlImOfs5RtxcoVIYniDnZmd3em0FmDKfj622-W_GUBBEAQcB9xQWlC7YWhb3Uav6iQRnP3fK1C0yUj8khwHGfQ0umfSYvX6DhXQzLdZPuHeIpwfCa_bUTmOJAzZOvx3MhErFnjaGGhfSryALk5dyMmIB_hYCmDZ7Rg1BgidhIX5bte86kRe1mW7J6q7ORUw8E7elALFcOUD_gQAkC71dbxyDy6CeFtNkMmymI9rIZqDUMfxu7s93z6crq6XIvRjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=dNYaZ312mlnm8yn2N3nz4zmbW4znoiuQuT4I7JcJfHzf4OWqezNBXh16FUI1pcYXE-Kqg8nrWILw0YVVUruOP5RtMMAsORnwe2zSqLg25hOzhP5oheq0Le2MCcska8GtYCT__CD1JdU4ogj-QuixReYNt4_f4EOVAjnx_rg0mhkuH7ADJBSI93FV8lN_NvYEhXZ-HOywJDgZ6YgZpfBubmc_nb6KepcwTui63UDiSoPuolMMMZbfoctjR7-OteLtr8a7SwvHwJeWVySKYaf3Fcho_R5FqW2D8HgBhibxDFDnvNFux37ESrSipUXJZWaX-qY3_RJz4xyhBo2rHPta4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=dNYaZ312mlnm8yn2N3nz4zmbW4znoiuQuT4I7JcJfHzf4OWqezNBXh16FUI1pcYXE-Kqg8nrWILw0YVVUruOP5RtMMAsORnwe2zSqLg25hOzhP5oheq0Le2MCcska8GtYCT__CD1JdU4ogj-QuixReYNt4_f4EOVAjnx_rg0mhkuH7ADJBSI93FV8lN_NvYEhXZ-HOywJDgZ6YgZpfBubmc_nb6KepcwTui63UDiSoPuolMMMZbfoctjR7-OteLtr8a7SwvHwJeWVySKYaf3Fcho_R5FqW2D8HgBhibxDFDnvNFux37ESrSipUXJZWaX-qY3_RJz4xyhBo2rHPta4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA1bYi7aBzY8FgrIZT-Q97z9Dow40TEbIl7JOp7FAt3yfIFlrb6eYhJD8lyeu9lnZvgR3KZAPJsVrJUAcgSgn_TBSsfHyFiafdEPiOc518lDwGZiAyoblE8wSkMPrqnsdP797EPLc4Ffh3KoEG_Qw_rk950m5G0OxkxL03t12aO_veZ_nj0zvSWt5y8NA3ufsz4RpReSMO59QltiH71ttEZZxYsevdkriDiyJy6NrqSIXkEUQkZ-uGGbXstwvb93o9zPa5pFGnMQCT1wUCyvLsfQWeG3i95am3g8wTtHZWOrO6JXoRQJlTC9RBc5HEMFwEDoeybAxaXKTuj_RQKbxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZCdFpOWv7J5W8qP6hC30Czccid29AhfMNPACS4kgN1AFkP1DLKb4Xik7cdFL1Wb8jFY-Z2MCGkdfQBxr2FFVg_PpPi0Od6WeQHZNxHJTHLnBkaeaGHDukoxVjptJV5PVo4UpcpDu7VZSZh6BEQRLp974xDfrE5hrY_Y9nf1hX7-m5pZEV9q3tARs0M07N3anWxIQScdDc7X9YcJT4QErRZ2I5DquK1eDI0MNA9LS5-f2fJS-0XYwo2hrZyb-xAELlO0qLSJnGBTMxuwrZGKAaCW53pzbiw834vJw_T7-1t0ac2MaoaOCRG3VaCS4GDbA8CkSuHEeETz27BH99Pg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNrGy4B07N5uY10Z00YTLDqj9aerpBfdeqU2vn6FbMtEzobvYQ3UPoC7MbRMqgbZL43uP3LIDtL8EFv2OmZCgfBpisdSq8yHlmrEHTVmSS4gPMvFF4lHXwVJvtR1ERHPL-LAmCr972esPyziyxa5CMhBAm95-ksoz4fR7ty8ctPHdb_R_g5BTl3jcfRQxulh0B-dloyK_R-IpbzWMJqTuJt6XlRKMiCy_YATwxT_bzLHXGBiro4ZF_k4KxHsW8d8lPknAslIck3GkSgx93i79HvwyPN-X_zBra_xiCA-4tDBPENJa3LO8k4ggPfR7RaPevjIYaW9BRtEavB-YAu4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOPFuomwwzWUkwXFvpv2hcIq5DPAWVZnKnKSWN7pwXirPrSjzUgqeAo4cH0j8JVYqXnvjMgdIIyKwtdEgx8GPJxflINm4EOO9j1YPescbrCBijNbQzS6slQ7FhCFtB5V_5ExrkXhq6H7HDbjbO_GQibTF08Ma-CaTOihoF_zmz2p0vaKgnp7IWMJjIeR625-QEeLDpVkh2CqYEZ2HcXi-nVxu6L4CHs3G22yGEE91cSfoPGV_2_tR_OcguD43OiJkTgMY42jD2cYk5PyygPSauCCxnjBYx3njGlKg1KEHqs7GfRovcPLXnbGKlPyrKwsb3f4ybhhIu5x_CpdvMYghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAl64YKd2P41XSBVHNQ-ltSgBKek_EDBj5hxuqh9qF5PMLHbSajj4AZ2Mq6YvgFl7PpyatcaJr0by5xMRU2ks-ndBZNd8QFziDD2C49oIxsscaz73bO3rcGDMTez9MEFUpCVjFtNYxVQrI3ZcKRypFvGwSjGPszDBLJM25jJh_uZqJ-4D65ssglFUwthms_RDr5uIqlnfkcLkTcDqBlxGrpd4G8CQ3eGQXGncL-TMxPA1Z-10NanZYqYtFTG06D2xIfutrTm9ompecOERHvg5tJJA3qdvnlaCAPIZpWJSzsi4sZ7CcEpSyqp06hQol41x2MHRKJvB0KPlj5a3WT2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqluHoJiw3mMiiQ8GqPrepw4ZCjbmXWpy9u6rMFZOI0CHo9liV6hwWgX6NF1fgT3hK6PGKCsYohGGsPIkW-ssv5l0Z68YYqZZorGeqHdtVNkivus1UI0hAnEWS3xZcES-23LzchY4HuKpDeRf87veUsABORoSQw97pKlR-GmgPEqeXKZ33It0noEWsWWJkodwJxD6ar6mQPIZVKx6L50K2pi5_fPMEUPibDT_lVLSVldVDyZd8B6-G2SDqgD22H5nxTL6o_AYn1RiGJj17fEgkYs1dxdhu_FF44JzWxEaGRKoAGT95UxOWfkPaq3DQ86gtwJb2U6n2eWIvVZOvjRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEqOWOBQC_PzARRH9bnsdtuA73kwO_bImIAEbkKRzXGgpXKgrjBT4FVCAYPaD8I3hBYjDEYG0pg9Bux5LNyvg5tDpogTfi6QzDDN19Ytesjo2lsnQ018naQ3Y2fN4SE0g8eaPgjQsY4TR8D_WzQqpwz81Rf5cr6R1DPhHhqVeHy9_5sEAjjlhuclJ2TtIRzN2mALoABSGsU0_PfgzqXXWne7I7VAQGah0Uh28PInazmIlKpX_qF5XfoNCHPgkIBIlyKzhRg15H65UyDclXcI0NGs02TITVdqdJ99_G2dz4ORIagJIgDWtn8ftcBpE72qwN0KPZ_co8zQEqANhAuZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPnIK7HVZWDr8MgNibwCxD0Go8Ov7qe3khvLM1YjyPn26QQGLCKKAbgvrU4Aet2TYNEDJEIGEYB2Ry_9ZL7cRt9LDRDBKW10AeJh1JAj2YszLU94EBaSp_vBFzl-87Qa3gnDGdnZ2gyhCPdx2r9dblpF6AdL_dt1m0rfc5ABY1HNmc4DXd76dE-q7aI_3gvO-MouoYmg8Nhku6IB0qrrMttTo62vIj3jaXrV5t62tgBb6mHHpTqiqr9ovJM0S1iJDJrd9wz3nGsrYfIsoqxvPGFJoIaPOER5R_7dwTHkHZF-nY8MYcmSz8u-z0VHuwpN_1FNHjH-cEBIcUhSouhMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jkf1xwbMOZRu6fw_QRchAUUzXQ361FnGQmRhusWPVB7tbbP5rIqttPBrH3Pv9ZYAfB6Hw08g7jg_Uij8YjZSjSgL9fkmHl-pY-D36Yv9kN47mOFiqxpepZXapZUa2Ffe90woVZDrBYMJSQ_T16LNk6x4eNwhRp00ZnGk5NtGoLALnnl62uimTlmaDVnYExQK4wuVn0JKnTLIdNpe-DxcmZasTe_cxacuVtAgVdr5zUk4DOSxDuuC5ckbud56b7wYap7gUJ4NPH9G8YMBygVWt7rgeMI5RuXqeLEi5fruSMwqBIn1wa7ZypuIM-TF-roO3nP4z5pM2FSBCJZjNPwMSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=H9okm5LkT8OSy0L5dkUw83JPuTrDasQqFy7gfAfGN-m1pjcU9biOeQC_ZmRvO5lv0jYG77I23pe_BZ5GQvr0mGhZyyQznBr0ymGapGFDNLI0kmPf-fvxME3Dh4x7yVNOxJ-c9WHmOiIvh74RgABTQ_xgNP32Q54S-LWrd54q1aEq6JerJ4N1IzM_7ucOuGaS7VbtjtURPY0lKBhX7kohxwIWRRQNRVLN43Y5yok2UJ4MtT37BgIyeojV7UpSnb6oaZb8xRF0SL98Nri8IE01x099Nkt_cdIFfRUHs55_9tnsT5dJ-UabPk4YLP4fyCMuTugbBMi6TGzW9hy8vXFVtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=H9okm5LkT8OSy0L5dkUw83JPuTrDasQqFy7gfAfGN-m1pjcU9biOeQC_ZmRvO5lv0jYG77I23pe_BZ5GQvr0mGhZyyQznBr0ymGapGFDNLI0kmPf-fvxME3Dh4x7yVNOxJ-c9WHmOiIvh74RgABTQ_xgNP32Q54S-LWrd54q1aEq6JerJ4N1IzM_7ucOuGaS7VbtjtURPY0lKBhX7kohxwIWRRQNRVLN43Y5yok2UJ4MtT37BgIyeojV7UpSnb6oaZb8xRF0SL98Nri8IE01x099Nkt_cdIFfRUHs55_9tnsT5dJ-UabPk4YLP4fyCMuTugbBMi6TGzW9hy8vXFVtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4LFf1Lguc86lbrHFNMWFuynJtGEbI8xY8lC5OvCjijEdb2M-1zeUwqq6QtbSwURMGecE8WgsMBb4lzdnNXBttMGf57_5nbymG1Q6EmJjlFyVnB8A-KebfTj9EtZ4rWYUIzW8eSHTRSbB7uY8Bd15ALc5eHCA0Xiz48q4w9JsQufWisaTyl6nuQlBNitDSxIvEeeB5nTQI5BnPohnUPEoKvTYfKREEh9iSNSPjfInLctMO_CMPW0j8wkHROJ2BEm3Aipd-hccAfJhQpbxSFQBHeyovWsJU0BgwyGbEgZG2ZszNSo-2qmfahzG4ksVmnDSr3j8q1RPZm882AEXRIQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=X7Z5esnvtN4Xw-EdnOgP6vOIetXVJdLbV77nUM4fhhh1G56tNSxQvciV6X7-ELe0neaPAUwG90GLj5QXNMfqjl8Tew_S-7KMliaj0eImNkdak_6gUCeUjluSgWRO8vle_BDysF8eAPbgiHYU3ynE_Wb0oKVBq--8KOkGeq9YJI156mzib4-bvA5Ew_N2A__ld0495Wqy5qGxisgER39_ATPyKq91EGrsI_Ht4En6jdsDoKj6CXRTIIVSnQfekw5-fVd5ESrCf46RxKaj4xhTrqfegiCrC4VqAgz0-gQmH5GNEHk_3bZ_ceO26hHEARwebZpseENkZ_f5Wd4wgZfveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=X7Z5esnvtN4Xw-EdnOgP6vOIetXVJdLbV77nUM4fhhh1G56tNSxQvciV6X7-ELe0neaPAUwG90GLj5QXNMfqjl8Tew_S-7KMliaj0eImNkdak_6gUCeUjluSgWRO8vle_BDysF8eAPbgiHYU3ynE_Wb0oKVBq--8KOkGeq9YJI156mzib4-bvA5Ew_N2A__ld0495Wqy5qGxisgER39_ATPyKq91EGrsI_Ht4En6jdsDoKj6CXRTIIVSnQfekw5-fVd5ESrCf46RxKaj4xhTrqfegiCrC4VqAgz0-gQmH5GNEHk_3bZ_ceO26hHEARwebZpseENkZ_f5Wd4wgZfveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=fs8De6B54rgWqUMUTDC0rgFFrMNysXQM2vFOzDYjFpkMCimUpb4bjbh3gj-TaCpFHK-bqhL0R0iMrfjdEHNy6eHCrr20jaX81-W3CgaxDGE4lwEiAjae2de5D1cwNI3F2D291-AmtwKE4Y9OpJbMsKSF5L2QI9iuhw4OyLODXhrRxxJt2SRnz5DIiOThUHWzlnLZUde5oHbk9BhN7ELOfBsokomKvUFY0Lw7M_z7nYBtfUSNBJZSdnc-kLFyrHKWbHAlyT-CLJ0VKFdjuMvc4z3az9mTKRCyrYPqvU4AfBVjT43Oi8brrktWzaji3X3x3TOrlcyV0s4n4yuYIZ-chQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=fs8De6B54rgWqUMUTDC0rgFFrMNysXQM2vFOzDYjFpkMCimUpb4bjbh3gj-TaCpFHK-bqhL0R0iMrfjdEHNy6eHCrr20jaX81-W3CgaxDGE4lwEiAjae2de5D1cwNI3F2D291-AmtwKE4Y9OpJbMsKSF5L2QI9iuhw4OyLODXhrRxxJt2SRnz5DIiOThUHWzlnLZUde5oHbk9BhN7ELOfBsokomKvUFY0Lw7M_z7nYBtfUSNBJZSdnc-kLFyrHKWbHAlyT-CLJ0VKFdjuMvc4z3az9mTKRCyrYPqvU4AfBVjT43Oi8brrktWzaji3X3x3TOrlcyV0s4n4yuYIZ-chQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK8mKwR6fgpz9d9bmMg8vvyA4XgGVOkFncCZfMVNJ6XDGLdS2rpEmi0Yy3km_z4syXbGRWT5oPf6xSexs24AtD3Wf1wAkpF7mXolkVIPJUEMUT6IqKDu1QTxsWoe8XdNWNwhpQBzE0XmhSTlyqqCeOyaGTSti47WKphzq3n39l3g-_zgVRn-_MdpJd9MiqzEGXl5WHUDLoCzA7NGC8jMpSRHWAu5ACdPd2BydwAeAWxbnvugTb1elgvtx6_iRVDymZXmXpwQuwA7RfZ8TQsEDuGm_nT33HtmDf7Jqwppzo-kJCcJBH2V4zckIVfXzzxE5ON3rA-8ZDgEceDtenXKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=myHFEkZaPmzfWFRY8sPFY9-cqchDryEMpw000HBSlkKz-WM5at13PUjxwZ5AsR8t1EYEBQ4_eVllXdD2uv4PfghguTT0FiH9esPw0rg9oDsXxhloqDQPt-sogou7eunSICNwognqVcWkaU4LG9Z3jDExN0P6CGzjsYmD39TBCdkVaMFQsLM-GhPuynb2qywHdh95sdyYiUkgVxPPgsGYATmlIzUDhUZ9Z2of5SGmId8BRlivtEmeIMQsZD-FgGy7Aqwg2EHzbH7_OKM9PWFbNiKF9zRdvIQe-mP0wySFv85ZBo_TS63SCBEIGIZg4-p5R2XwC4yhnN0r923FozoWuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=myHFEkZaPmzfWFRY8sPFY9-cqchDryEMpw000HBSlkKz-WM5at13PUjxwZ5AsR8t1EYEBQ4_eVllXdD2uv4PfghguTT0FiH9esPw0rg9oDsXxhloqDQPt-sogou7eunSICNwognqVcWkaU4LG9Z3jDExN0P6CGzjsYmD39TBCdkVaMFQsLM-GhPuynb2qywHdh95sdyYiUkgVxPPgsGYATmlIzUDhUZ9Z2of5SGmId8BRlivtEmeIMQsZD-FgGy7Aqwg2EHzbH7_OKM9PWFbNiKF9zRdvIQe-mP0wySFv85ZBo_TS63SCBEIGIZg4-p5R2XwC4yhnN0r923FozoWuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUGkPbiN7keAG_sNmJ4nP67bMj7I04-VsavOv1_ajVViTAtAkHhHxCI3FMAm1ABWbj96_qct03HzsHmNXyP53JeQYjqaUM7-bTtOP3QECkBZpj5iZrPBd9GvjoMgMbLdwVw8mRcWUOQdhGmkL8rtj6RmiGLMYqxuhNChwvHv5ofpbLMjXLEhSny2qaVlL3Nu8bxbFC3t49GHqByXOiiCgyauNZt-xc6v-scZWINbiK7LOrjt8vAoi7spXh1Q78uUs812aY5PntO9hyaasWqcpvMk6Do85xjo5PM_fRCqrrhCAKYY7eeHs-Inj6LgLKP8lqtliJXl0MY-Qyhud2UV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLG6X6IchydcnRpFyS1yXngPEP8FVSXuKdajSly-XZczMua6IB91cLGqN0hp99O_Ncq5AKH024qGxAHJ8Uy3eDSXoaG9i_0z1dDZUrCUOPrOWOVjDrNo25Hqw3nwHXXytcTiEh8EQsz1nWJrGgJRwIYrAGNCF6SuEsO2-FF3jQIVJ7Cahfs36DW8JkQw_NRUFbQM-GMdDafplVSXJ8-PWF5pFj0TWmfzzTKhhsnCeqPMjv0L_LHrvWAPzdn0KXcJeP_wWIdp3XfY3Bg-3WlmLfWcYRMl0uAwlF12YNwRYvNyY3-mD0W9ZaFJO5YUrkXpZWsJRBbsMJobjhVQqB-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJ2Mh93cc9ibulgRQXp64I7bPar2Y6bwrzi0EFbkAlfKfLP68G0NeEhnH82wG35RJsrKIYWkLtNZ56_KUIHkMtfgP0jp3zVi_4ibd0WMtFwz2MLuPj5N_U9FNwmFU5DDCglE0vKw4GIXz3ZI3iPc0Tx-hzH-O-0odMS7UHZTP1Bi8zuTQnkg-6BSUlf2DcqqDZVnm0WrtRoYh3yGKunmchFzcUAyFdWQJb1TXEliFES2bgBd1BDJ_-lMgBzqF6TUP7pxSK_NGoSJu6onuzaV_yG4AdcL3koEqSiRoaoC3b0nm_rGAZGsBSsLsKxNSLbDh1XQ2HgY_0bSBdk78meFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VreAYg0a1LE1S2I2YBKN2iNISApKCbhqEXxSh37pf6X9m4knY2dRpSM7iMYbmzl-Ra_fpHZ3fELuJPT023ZU_0UebhCGuuUg9zUmdasmURbylYqCznw1eam6NJLlGNhfYkOwcaBtl8TjltPMgSpo8UcsTyqrrsq3GO-YvLmAasjkAOnqGS7eA1eFd772C24NWH0bcwzEPCgVrB1Ktdd5REq-dWIXCMtdhsohoeRtatiICFHIu1KhibxlS0rGTuLt07H5Nl15-Hdlo24iwb1b80LQbsgxDuE9Kqbt4K27Z8uaRZImyAKOpUO9--6_yKuhYPcEoM65I1Bh0ZEOEqIxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eI3xKHjc6DfXv6uWtUKO4Up8n6h6oVv_DW_qXg70zPXVijI5lvIH050Wi35hg8wNk1CYfGxktap1c5pmpFINFjHzcXIVrfVsrfEY-kLWXwNcUBVIDn8YKQSfxOhWphUHAuWk59Asha6arVov9YyjguKGQMjhw60MoYAUbh_rWpxJ_VriM09Q_tm2r830W2KtppOkYoX7w0l7ZY7l5ZUGcvjpSHCi2n6I4WNiW-LMwM7b6ILYKfX4n2v-Ty0hIRgxcZlNIIWslbjpnnLwAj3bMevKcTvi4OHut_xhvvibFylkfbovAJLbWyWlmTVUK-XssWahoZziNVXfv40-dAkQ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xza9Xi6lgA1lQg5tL-QJx6gmoKut00zCXpp-RsZcg6nMMpi6Jte2Ia1_5n37YGD2DGCTA4X4Cc44pnZJZSK-MwF-YzXRMq1a7IaO7EOr_gFKaYjtz8VAUPGI9VYFvwiMXHklrhgaVmGnlDEpkdeqp_abZyy7Hy49pAqsHWnJ9ya5fne0ru9HlWQsH8GwoQbY8TfshQ6jU3VRXDc7RRV8ETYwN2ys7t4Z-EIS5ur3By3KqGo5j54TNtKOCd-cBoQRc3mwarF6XtgV2afYHKYns-oadrCgx1DcRJ8XPh8PCAPdWmdjd6A8xXyuZnKGwmiprfG-ZEIyImMrVUlsqqTjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2DTGkCAnNn5PAbI1D9OgsZxjFhe9IRQ7tH3GN_FHlExsYGa7N3lxZZHLdIOKKsFzUaEKhfhA49QcDI5VHNdfok9LQuBQ9u9S4mCyWFUwiQSLyulSXtGG3r7YDwOgaIWKFpFOldKXszf3L94SiDl6r6b31SPE4Qk7B2y0lMSfs0tW75y3YCNDDq88Fzwagoebkd29m2QQBLifddRdZjzNNnzb5ii-Y1RCPspYR0_Xjg8Gy5oTLHr5cF22fnBAc6_duJZ8-Lf4rEI5B-qMz2TOarPGj9SvgsFxCTns8VXxLayPZULkqSCmy2lsBSyNUe2QhQ99E8qAHJtrX_jHaQmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eF5fLG-IcLmcd961zyg11KN-Mru36ZLNrD8Jko-YhMYipZnTTPBiEdB-8-GYIRgW5XudePjpr72Zw8MkFoRcM0-HVtZQIA76vOmgDCiwTgM2fNDXOaKDqVfJl-6HtBWGbwX7Qt0N7tzu4Y-Y4bsa_if4BNgdbQqXSrsG1U4iglDGyOsdm7ckSvuN1tlPsNLz52Y-bkd7ZFs2huxOCvhVd3mx7ljxe0U5zbuQ_eqQSa0uTu4k77gHmq0R5_S7nsBAGHzozdnWzO18JicRJOi0g6pvhib_bqE7wVTDhg0cafwoC4v3rpMlpkvdjgZ9z24KMe-ZoyN_QxxDa17B37qMzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=dEpJDkiABIIS9SwmmIKMY7Qq9arWQAXzTBSTk15M6xImQ0HstGphkX2szaO4GSvSekybdZiscaH12Uxg3ntu9n312F5ELrQL7JUuCbxvLYHjnzv6Z3MKm0RM7Uk5qCJ8sUEWGTvuAIAyHEq88HX4GkrjnpYbWPDRlZrmCaPfrvORngmvtoWAhDhlN95CguIznYFXsdOC87UZ6znEH5QjqisuymHQhGODzQ86gTJ1ySemhj9v269J5i8dVJUn8NSUlutnL7xsCyznEk7QjCmNFDt1M5WUhfSbfrHo1lqnGAy29UEXnztHifabxA3mp_yh-MxOT7zgmxYFlHCclwy7IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=dEpJDkiABIIS9SwmmIKMY7Qq9arWQAXzTBSTk15M6xImQ0HstGphkX2szaO4GSvSekybdZiscaH12Uxg3ntu9n312F5ELrQL7JUuCbxvLYHjnzv6Z3MKm0RM7Uk5qCJ8sUEWGTvuAIAyHEq88HX4GkrjnpYbWPDRlZrmCaPfrvORngmvtoWAhDhlN95CguIznYFXsdOC87UZ6znEH5QjqisuymHQhGODzQ86gTJ1ySemhj9v269J5i8dVJUn8NSUlutnL7xsCyznEk7QjCmNFDt1M5WUhfSbfrHo1lqnGAy29UEXnztHifabxA3mp_yh-MxOT7zgmxYFlHCclwy7IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=gHHe3Xltlj-h3tZ0teu3-wDprCKuKujySmyKQ9ayaZE43DSi9QRl9pXYPi0FtGnM2cNDU3Ma44WIbQNgGBEJKa8UDEzIHv0iFAAAQjU15GMCN3zoh0WgGkc2p4lH1a9JcyO_izme8OFIhMvaiX4Lncmx73LK5Yq1JpK6Z6RmkjbETbgjIsQDrnFstvY7ayntjLhsn9WWpKryJcPSIMLvLReYTYChcPotoCFKG2kbHoS2aETtI292EkUDCS5tLHyw877sqqODxeJvgiLpumHKlEHBgF1Cu9K912ishPtPZWU3rrJw0bQDlKW55uxVdgo0six0IBlC2zVJDhQJsBsApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=gHHe3Xltlj-h3tZ0teu3-wDprCKuKujySmyKQ9ayaZE43DSi9QRl9pXYPi0FtGnM2cNDU3Ma44WIbQNgGBEJKa8UDEzIHv0iFAAAQjU15GMCN3zoh0WgGkc2p4lH1a9JcyO_izme8OFIhMvaiX4Lncmx73LK5Yq1JpK6Z6RmkjbETbgjIsQDrnFstvY7ayntjLhsn9WWpKryJcPSIMLvLReYTYChcPotoCFKG2kbHoS2aETtI292EkUDCS5tLHyw877sqqODxeJvgiLpumHKlEHBgF1Cu9K912ishPtPZWU3rrJw0bQDlKW55uxVdgo0six0IBlC2zVJDhQJsBsApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=K-bOdETFqSCLtQ9caH8rircpG7HTFrjB0w4orGg436j7VKKV_iMRpOPTyjsRHk7Kz76PgSjp81ApYPAPF-DvRWjGBDj6u1_DMVSIwDNs5mWY5MNVSbnvwcTF14QX5lx-QCC6XJ0RJf5rGm6Y_ouxB5hzjiI8lXMcKE_PRsL8GRM3rb2HYYBZBVSW8wfGtpXXV18eCK6M4TFU7P-l8B5oJc2CMaCQMsEw7tIxmH99y7CUP6M4A6xYcuBKO1EcueYQJgy9Xycxmmtk7Zr6x8G4mHk8vA8fqBbMrTjWYo68Ux4PBlz813f0jWCUfVfDLcVwec1u38hzmg-Wti3hLHt3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=K-bOdETFqSCLtQ9caH8rircpG7HTFrjB0w4orGg436j7VKKV_iMRpOPTyjsRHk7Kz76PgSjp81ApYPAPF-DvRWjGBDj6u1_DMVSIwDNs5mWY5MNVSbnvwcTF14QX5lx-QCC6XJ0RJf5rGm6Y_ouxB5hzjiI8lXMcKE_PRsL8GRM3rb2HYYBZBVSW8wfGtpXXV18eCK6M4TFU7P-l8B5oJc2CMaCQMsEw7tIxmH99y7CUP6M4A6xYcuBKO1EcueYQJgy9Xycxmmtk7Zr6x8G4mHk8vA8fqBbMrTjWYo68Ux4PBlz813f0jWCUfVfDLcVwec1u38hzmg-Wti3hLHt3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke004D9mB23iVaQn-hG1opvSZJ-GNRLTNYu8ZQiNlc8deMBaMJ9F_DVx8zaT6_wpJGQt_VVtQo0joYYL-mpvJ1u-LRtfi0Ecbk0ues0Ws2aGQFVIO43JdqntVxwJGmNB-uhuRw0OSqoMWZexQFbRHN_qF2PCVMncTa_sVU9NAGOf1V_9t36oH606xC_KtGNek5cR6q7HlbaUAbmLX3DT6j7BlO6HWIum3623md6Lkn5pFmnsBZOjI5rlg5akmSiXLCb-DgHPz3d1yRH70sZcbKNM0u9N6I5a7IzfwJHMSmLz3Zs5MIzWZeIZ6VPgkCMAY-4JENrQVJkEYSHzktRgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnv5k6IbkYw2P-t42YGfb-SAbL5UsIN2i5BREAHevxpJaVXRVHHyzYRNoI3V_gsRoqH5Q_kNjMD_SriWmN60bsGDHhisdj66Rub2EI4gZmh8yG-eLYqWMzJ4l93K0M0ZJWJ7tLc6jm9cuFsYYeC8qsbWIoNcIlV_PrvCwV2EkUMG43PDvvh1SfvChdRwf3qu64BQEgC172Jn8wrFXN1Jids5KQOyZptfprJhX-Mt7pcQstIN04zBAQIDlWNo6apLBKCRBxYO8AGTiZ6cYYGHtgqHCcAaURv6PgcBN7M2sRzKgSk3d3YBTDNr0uBdvKDh369z58zwM7RpATm73J6cKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzl-VuTgnH9OdSdY2BdVwVNXhEfcVfToWrC0TiTiJVypsTzQFsmaJ8eKRx8LMip8lhadtnSpbmoYLc9S1kJh24G1XcChRESt5jU2NodQfvb-7oyk1ZtO2MrK3cMuPI2p6k-F6Mb9sj5g4Xk5Xg4CtFnfUFX21EAqO16h2lG6XJX76eHwX3Xah7uhjz8Jy7vpqIbK87fYP280OhvlXGCXsfBwdssAjFmJQygEka65sBeSpzNqRsdjn8_kFHa12xiCtcjL3HHAL2qEzx8dcKq3U6WiOvjvpXEg_SqV5vDgSXgAZYV-Vk-DtHMi18TCZ--3pgnS8FenhxUhwVocCVNdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-uyw86BYt1nIxFmKHs-aY58E8i1sWj69fJqx19jusn8WMFhzUZ0VQo8RUPHXXrpgfEKPyvP2kyYryzEmwETaYWgxyoaA82OIiVMYNdxuZwEzBmP5ZMSoPeLKRhdDRvXkKpOO9WF7wvb2OyHS6nwhl9vPvwa5pm64tUBzagkDTTLIIlCkRPSi4gBftp1PgW3KIvBOKxcACD2yJ9tDwThFHzeXypkF01xAdZ7O9nlFZHJDbRsV6ervvWWb2Ug_PUWw-PJY6QXQjt4l7916YkB9xepjIvPDM_V9vjWGBUKR8YcWUAnsvnys8orTM98PTF17U-Z_sxPCnYjEzrSTQ6CWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pBoVD_NFuNPQcglhF7yW5NfNUQXcVs-wzPPZrJiLxjBPiw6jaIR-bvmJ93Q_zufnDZBxf8tnbArn3oqJdu-mHiM_5e3XdWSsqC3tzzanxNG05EQcXfrNJ13rsUUq0_iowLaX2xikWgY_FGk7EbvcdsD9t55irDQaLeyvx7J5_nK6HiJZe6VVUxOVCYGXJjwQfRq2FfMc6FLrdbGZ88IIRaMfFsuD-jIGc48zsJEm0rMRBekdBQQ-b23VrW-YbEWjjGXOTUfJqU6vTSkCYVsEnOFA-1DNlNl5HNY9Bbxbs0HlRGxEv5ixi4JBxqQy_JEKtW2I-OD8M7s1YabpWsV0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pBoVD_NFuNPQcglhF7yW5NfNUQXcVs-wzPPZrJiLxjBPiw6jaIR-bvmJ93Q_zufnDZBxf8tnbArn3oqJdu-mHiM_5e3XdWSsqC3tzzanxNG05EQcXfrNJ13rsUUq0_iowLaX2xikWgY_FGk7EbvcdsD9t55irDQaLeyvx7J5_nK6HiJZe6VVUxOVCYGXJjwQfRq2FfMc6FLrdbGZ88IIRaMfFsuD-jIGc48zsJEm0rMRBekdBQQ-b23VrW-YbEWjjGXOTUfJqU6vTSkCYVsEnOFA-1DNlNl5HNY9Bbxbs0HlRGxEv5ixi4JBxqQy_JEKtW2I-OD8M7s1YabpWsV0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Vj0Ae5deu-BzvPPKf_ThjEGcyKBKdeWSgwpQwl4eTGIRo-NoUEXDyLJheGAWBsCgG9WZJUKU7SdQXpGbuQkdnUp-1hp6S14kYcbDKMySLUhI-NrolWfazcwU2pOLqDoBFWzHEktqIF3ENgr0JxxJQdnBV2WLbizvkJ4e603o5urYCg_v0UWEx6h692cSIIV5Wvyab9anwE66vs5SIvPHNU1bZiINrPqLWHp-DC6SrtERiueh_5la_CESNj5Onx3QEzzjiMoyEQ8722ALN35lfIaYBsafckN5P9ri3dA6wffGEgMW9O2MS73QrESeTcvazOYbvy9S6XFz1rlZYBitLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Vj0Ae5deu-BzvPPKf_ThjEGcyKBKdeWSgwpQwl4eTGIRo-NoUEXDyLJheGAWBsCgG9WZJUKU7SdQXpGbuQkdnUp-1hp6S14kYcbDKMySLUhI-NrolWfazcwU2pOLqDoBFWzHEktqIF3ENgr0JxxJQdnBV2WLbizvkJ4e603o5urYCg_v0UWEx6h692cSIIV5Wvyab9anwE66vs5SIvPHNU1bZiINrPqLWHp-DC6SrtERiueh_5la_CESNj5Onx3QEzzjiMoyEQ8722ALN35lfIaYBsafckN5P9ri3dA6wffGEgMW9O2MS73QrESeTcvazOYbvy9S6XFz1rlZYBitLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ummYqTHhihuv7cehplSCEZd9eQ4BFyLBL03K23_DMFtP9wKuywFnbIq7NrRWTS88ONXMtS_eYAxL-ARjLJV6gXmQ-bqGtpvIt4gGFGOthEniNHK1KeXdAW_MnY_gTpI-x5l1NReNL5f2LPX93kt9KIvAgU22Sy74ik2tXlcvQg37rF-GboVW5prr29OzMs9oPY-Np9ihYdRvoBSDn7e5JnjYb5G-XcCqy4RMTWOzC16-ph8RPlQ_W0Mxn4ZmHFh83a90kj7lX0NiczWm55-kTm5ghCCFYokZRla_X-FUtD3g7pU8eAiYv_2py9dW0Ctupf8MiKzvGQRaGSV_r8hhsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW1V4tsHqr3pUeiVGutDk-fgCxWB7mP5HA3POvezgU3nFwFqXzM_p7tY_XooOq0IwBdZ4iIGaMMUJHw-Ytf1sWuDYZq3uRmXAjdX5yVEMaoWj0cAkoDqhNx9s-VKRdjFc55iAe7DMGWVv7blqKELPmOmoaDFquhcy-p2CtkT6zQHcBGp7x980ynKmybEKuC1PIxXVIbaun34QW4MHw88ekyCZCDwlzwFdhBE3U4nwbF2KsL8qFV887eYI7vpogVh3GyOAdHz6QMRO2SzAqH6bsUKLwnePCbf-siiitsIzN2Hz1yhblSAFwj7kmF4KngS4sjJF9ebiU5x0RuQWjB33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klH-iUSurzDNckOSLv6VzFo028eSOhy7sN--mBjIECqCHQO6wz8gTt-ObKo4mf5IeYkPlgqp4GGfFg1aKIgfwDW1zUZoerpAE1h1GXhjeB0CgFteHry1tMXfrC3KjdRGF-Eh-YuabzYP6Phg0kHNFPpcRXfUvw0v9MTk0igJTgJ-sYr5mpEcsnQCzFTCl9r0uhmxnVazpdnt-HiXn7-UyZBndXQq-dxrUh3Ycdmm1tGseTfnNk404KXqz7yYGmT9839YbnZUjGH9eysrohZwhMEynk9kuepfNMoBP_q5zDljaG7IxnPvNZ7gBuyaqDJEJxzsS1r_wc-qY7iaNAFsfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUYOFdzLlLQG8ZepY9dU00QsMnZpegb4NpBZkMieFkbpqCWpboW3Jkol2ju2GPpkrLAXx96b_ukJkREj7_mP4UkrPWGj1Vujg-sGnwr81c0AnV-T16faJsTZogoiswNwfbjg5am_UPnowti_FZrf_ybiLiPp2E832pdrHpgRGuU1_o5u5jhnQnjTkHHY_dfC78H5BxOuO7PV79SzUyFqX3FiA67StnW2Ln-NyVy_dhiSdu8TlKgKnAgTzbSFXbLrdyuXxqSj-b1-l7Sz-SFPWXrP7V_QjAsCmr7vKpkO4DiiWHhZMy-_Syx3ZijdWm2Dd56HDP2Cs2QvR1Lu_Hg91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiudV9U0iPIQREgX3z_VZ5_SqUxrPTA0QzIjKuCR1LMlEovqd1TSnIlFIGKnZW0J9Id_cRVDx4IL1thMe0ccNptI4RNljVpT-FaTdRmMdAk8N5v0DIBHgu7VP63vdK45ZpUtWUP9Wfeo2PoQTMn5lvKghXvG-JLMqBbKnrpXPod7E4IHSHSY0kYhJcSVGnf3IKfoY8KX1e_PEc5Qf8PGrFLqjPzz52nbCHeOhFzFyk28npfdIUhss2q9uwxNwVZyDMxwTWYt7a950KF3ndJO_GrWy7Hz6fBKFCnldWw5-deHDcDgmJwOIi7zQF-SkFoqr01V9ZrCKH1Bu9u13ky47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5JwwEH-OkDLAQc0fSsPY6F2HJP9QbKHZpan3iDlZhL8SvaDX--c5qlfTmFS7VNO5OAhmYwvz0stU3p-M0G5DLuxgGtH3P8uEu6fWW9Lrnq3YusHmXf3VRSGW888daD0Bs3GjS7ai0-RltaS7x2q8Vpii_BlG9reKAoMb03kkFcgqxqWS2h8Ex5ifXbVJV6YDyYPeuaatCRGVzY3c7zXsG0Dgatw0BVjEtj_Lqbw3RekBvFL71agvI1_3tOR8B-CGGL9S_JpGY1J53fJByAATVrsn8XbcDTCTtwhCJcoVhUD44PBdumx0Cc2UhwT--z98UdrdbpzodzY1NuXSkiZ9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDBXr_1SStjpDrpqv_hqGiA5ynBgmci9m_WAa4YqQUesDLk8R4IOxOoIkjBItxNAM4j1f7v4kTuFPeXibksKfeWwjtnMka5tMnBa-DGqRVVEYuDihBu-3kuiRCkTEISvYmt5asJDA92tOW7FFWwqmPduDbtyKyHSf3-mGcRreq9iH2AOs4jlzpFqFSdMSbW5cNLpWZzKUUUCGlh5KbBhR0uyYcfobCzOkONWIx13uLq1yELcEtk_enec9UCD-I5kWdg7lL0X9q1UKO5HdfK_QN65WPhUmX7ewAFnYeYu5TRjjGyaPczFDWDQX-t3iKzlkMsAOy3WxQGM6anytbPh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cikxz7OyuZ2In8rY2tOy1GSOmQhfNSmbraEwlz8ppKyFfJ07FG4yced34F0Du9NQbZguJ7MS_q-FlwNCaGA09asRRBrsB6ch6UJY2kEp2-PRj_YPnTv9kkyUyRTbHnkHmTvm2GbXuiiHdFvQKTGsRMXPWvkDOr9iaEo27mhuOGlvnsUb_6q8HjlM9XVkxUv0MjblZB7KHDiJmRxNGD5hZTBwnzTBK-HLHZYj-abmcsBEUAIVNkHUB_81qDkA6rCfjfu39umfa4p4eu_9_l5s0qOX637zscfiSG0CHS6xqum_MX7jUTnN4OMuXe5WTLpI7CFpCwJLeLK4whh0WYMHmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=WiF27LnR5crcQnInzjkPvLyC4xBPViTqS-uBn-zbfYtYG6u2ih5IsaJFQr7U_ctWM7qSlHyNrOsqSW-gUovWNE9dVRjCGnc5PGiC-P9kaSRJS7c1WH0VTZf68uXIO7g0GD0R88qk4u-svbPh1Tlw41n_RxqtOxo9ezYHiHnJppFPdWI-IlAajt21fUxu_1P1WtqIeUtmBqv8a02D6_Ynv4tJIp5j9f2Eq2c4Ra2Pxz0kUZDFKeeTWHS1J_FAg1WBYkmQBkIm1tMbJmZYXkp6eKiXRgkeVC6y4bCYWpnkdHCrHTcbPQt-8Zq8UePP4mOJ-FasA5mvqNMjOVUz8K8pSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=WiF27LnR5crcQnInzjkPvLyC4xBPViTqS-uBn-zbfYtYG6u2ih5IsaJFQr7U_ctWM7qSlHyNrOsqSW-gUovWNE9dVRjCGnc5PGiC-P9kaSRJS7c1WH0VTZf68uXIO7g0GD0R88qk4u-svbPh1Tlw41n_RxqtOxo9ezYHiHnJppFPdWI-IlAajt21fUxu_1P1WtqIeUtmBqv8a02D6_Ynv4tJIp5j9f2Eq2c4Ra2Pxz0kUZDFKeeTWHS1J_FAg1WBYkmQBkIm1tMbJmZYXkp6eKiXRgkeVC6y4bCYWpnkdHCrHTcbPQt-8Zq8UePP4mOJ-FasA5mvqNMjOVUz8K8pSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Fc19axyQ01wfhvBgUVl-GowH4qdkq08ERqiXA9g-en9rJZF8rvodfaEmdcQd92t8X8ufOcTLhZE0fE8TlVOFj55QTmgkU5E6QewSwhNdxj6uybYiHI23IyS2kxUvWu7nT3zy545ayqED8PJNO_A1XKCpc34X8Na7pMyZEr-3l7kxIRNwGnSJY4nydOZ5i6P6PsVuH-MldC0ALikyQVW5EEZQhpZaNtGdMp3FW296kmeOzqSj7PfszwQEj6mNy972IQbdPo6w3PM_mB0Hfs_3zA9QZCLbPFunZ3uvFHGdLduWyyhjfaab-x0YLGpznHpPVcjM3923GWGZ4D-nVBeWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Fc19axyQ01wfhvBgUVl-GowH4qdkq08ERqiXA9g-en9rJZF8rvodfaEmdcQd92t8X8ufOcTLhZE0fE8TlVOFj55QTmgkU5E6QewSwhNdxj6uybYiHI23IyS2kxUvWu7nT3zy545ayqED8PJNO_A1XKCpc34X8Na7pMyZEr-3l7kxIRNwGnSJY4nydOZ5i6P6PsVuH-MldC0ALikyQVW5EEZQhpZaNtGdMp3FW296kmeOzqSj7PfszwQEj6mNy972IQbdPo6w3PM_mB0Hfs_3zA9QZCLbPFunZ3uvFHGdLduWyyhjfaab-x0YLGpznHpPVcjM3923GWGZ4D-nVBeWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKD63aWrn2cpTaHWWx3NadZ8pN-wqJowrGsvTwTjQb0z4UxWvgelAWZ7FvMftJq32j7jvQcep_9PKP7FtO7Ef4Z9KvFYw_thSKUTCG4-vYVPTwUv7BC3iU8WLdOnVHI25Z0ScTtdmec-pRtpRSw2-noAoLtXoJC0vRmmkTdtDQr860mc5ql48OZNqxLvfeVZ2TXUtQE0X7GnPssos81o9rwowXvxWtgcbJXFxj6PU4f_Zsr_L8MfbTFl9iJn3SYT-7mNhYwbYVlH3xQFggSb6cb1gHeXI7UpCUfnpH7NCkac4akIJgLeLjZHXWopa3ESl5AEYU_aCCK2rnFHhp_Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BelHoRHmI9JJ-4R-0ca_WaeWqXB3K902BxjVMDVKxgvlu3LJg33VfuVlV2BFIkRENdJRV0nNHHf2VOIWEYNLib6dLLj7OHMRqe6FYXpTA6CJHPBzndlh4LBE_j_xWqhIgvwPCxY2qOrqm6ZWTAWFwiRprI-ejGhSkAYrelK74Jl47F_7cHOPIk7fEVXWgWC_WVjzmlVIn3ShAvYYmFzS3qB1rz0A_cqnDvRgDxN62fZby_YXT0mIWU1DvVuOWLBIqPIwICJ_Ca3kRGpJ04UDr6Tm67DZhlnimZBad0cTYXJnkPBFYAgLWl8DtOgpgfaPX4PNUN62DMF-y98XffKfVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=HMsy2AgZXH2HM56M1XyzPbwrVA1APhuz5Rqs7VtNztPtMvtWqkfeUzX8ifNteKscACZTG73_3zvgYvxomWcdD-le1RZJk23XgS-mYdzKrw_nXOUFdrxBhkyyFb5HJ5UsJHvOH-3BEmp5VVeIgquXNTj8_TzVKGTpW_rCG8xT0fv66QEoU_3cyZZgGS3YyIHpkOCH55IJsCgPKy68uLnNXJNNPn80IwBuPYePAd5NvVJaVg-rLkb5NIhLsWuq3tCtAEzbAncev6KZoMDK3UkiRZtiE0vMqDavqEzXB9H7b7pAwZmYGxmd-tAEtgKbhmTu4cN1uS7sD4saRwuxpJHizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=HMsy2AgZXH2HM56M1XyzPbwrVA1APhuz5Rqs7VtNztPtMvtWqkfeUzX8ifNteKscACZTG73_3zvgYvxomWcdD-le1RZJk23XgS-mYdzKrw_nXOUFdrxBhkyyFb5HJ5UsJHvOH-3BEmp5VVeIgquXNTj8_TzVKGTpW_rCG8xT0fv66QEoU_3cyZZgGS3YyIHpkOCH55IJsCgPKy68uLnNXJNNPn80IwBuPYePAd5NvVJaVg-rLkb5NIhLsWuq3tCtAEzbAncev6KZoMDK3UkiRZtiE0vMqDavqEzXB9H7b7pAwZmYGxmd-tAEtgKbhmTu4cN1uS7sD4saRwuxpJHizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo5cXvnIRffa74V9Lcn12IajTlvzMfYhBnEsjYDLfZ8yIQhjq6Ru8mwbQt6MHT4sg1E79ED_B0WN7xcPFErpK2EvsCu1ZRq-_bHoVAS-Vx7Fjyyf792ktA5QQCMO6Jl70e0Wax_FRBW1hLoEyAUNwAIrqZTBNXG8YIPPZFKsTuRMWSvZXZWugQ0EAHkodePddhBcciLbZaM2i3hUwzP6oYKn-NsB8EIw8BKvEoLFKkIBkSVC5pof6ybyZ8cn220A9UlkJGnvigLjE_wpw-Vz9Y1I_3VMe2AU8FmqvF35jr-YhhjNUJLNhj-Mwdoh-qB4tEc3IQVpS_oeKpaJfCoxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
