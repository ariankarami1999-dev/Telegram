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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7MSmD4ceg44KxOVt_gVCsntJEWKwc2FX31xcKBwYnKqeYikgwIdPMWEs-InCiCL_kPIN9qORACCUY7Cab7C6lec2w_dcDAUuaY2cXJwyuALsygLtEhOzGWwrj-XBxHPIVQ93QiqGBeygduhDOxKswXRP395TaUCj3t2Eumfv2-J8-oHtpFoM-Xk2aBtCX_EpyZMOGdqSkmlyKCVbhdR1o99Em93pBqWyo2icaCTFOlFrQMY8_KNIPpBLkmyz_26qvVmBaTLXHDLPPcxHkqiHwqCFgkjs38XfGPri4HFaoWS7FXWQyJSQj5X8sQDXwIkb88FuKIaGG9ZJqBcDtWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEYplLELLwQq-E9ukrEhqDtGDS9X24CEXFLsSGTMMfmGplnWjLRGAJ4sCS0zh8aNYtiew0XM75Bnq29otbpKr9kWcX8UUuT8OHCxkvC8dhD-J4yfB6DNpXPK6dZgEEoSsj7DmG_cjEzBoIfX7vPDNGys75ALXow9kY61a22TS1sKHTyIg7RvxF96yR_d-MnqbmuySQmi-8B00jx4AelmQOhQ5jjybBLAYRdAdqUaFXsY_twHEmdBKDqS-35X34pbkEl1yJJjVzfe9L_d82s7u5X-vcsNMfQq2WkmvlFNWAErK3KQ56jbtayo7XN513Z7aC2jkh4LMGHjAYS8FAZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=XOQbieZEgXeKegzwOkVgPcYwoKMrC2jrsRdHyLqhNcuSF_boj2VB0Vucv99tQPv-_mfIJCeR5WSPunWR7DsMib1v_JyC9hQFc8S9OA3-OARoWru0yrFogtV7_3mLgenStPDeEDhtTQEbp8q9gUUaNWQ5qxjhyQxDctRxJ_O_bqys4RvGrOSbWloH8IibeBPVLEkQNZDBmAMvjYUdvhqnejQ1xnQQPVo1HgxdSOnl6yFu9zOaQpvQD8PMJubZxJ4ROpYTRHgZeLZDr4oZGpM2myxg5GyIKXTMkIgbbY2m26mZS-1Oe70GNK5WlSJvdFjrikOKxtkonTHKA3Qhf5puEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=XOQbieZEgXeKegzwOkVgPcYwoKMrC2jrsRdHyLqhNcuSF_boj2VB0Vucv99tQPv-_mfIJCeR5WSPunWR7DsMib1v_JyC9hQFc8S9OA3-OARoWru0yrFogtV7_3mLgenStPDeEDhtTQEbp8q9gUUaNWQ5qxjhyQxDctRxJ_O_bqys4RvGrOSbWloH8IibeBPVLEkQNZDBmAMvjYUdvhqnejQ1xnQQPVo1HgxdSOnl6yFu9zOaQpvQD8PMJubZxJ4ROpYTRHgZeLZDr4oZGpM2myxg5GyIKXTMkIgbbY2m26mZS-1Oe70GNK5WlSJvdFjrikOKxtkonTHKA3Qhf5puEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Gfat7AFEObUgIN9nrP57RgItwH7YCfQz8LEmhDAWGEhraEIRQ14TQlZn9_XGydtJfEnL08IYXIzrGo26EcELT1ExL0OToBo9qmE9CbDXl6jXR5cnGnD4Zb_qzq74bHjeTpmbUKeUPl2RA1I4gJYx0pzwrH_IBh-oi7FhyWdboPg5k6r353hawH9Zq39x36hwGghjwEsYOBF4ZRxQAvjePcZOoVhXjKoznbq07MpW2BXlRN7zgMecM51xFfVP9tutg_MEylo58_p1EYhVoiijf8TOiRXMt1xenXc7VRVh__5s6r_uLTa1vHTzV4wC_Q6FvCh8h7on9TZV0sTgXgfm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Gfat7AFEObUgIN9nrP57RgItwH7YCfQz8LEmhDAWGEhraEIRQ14TQlZn9_XGydtJfEnL08IYXIzrGo26EcELT1ExL0OToBo9qmE9CbDXl6jXR5cnGnD4Zb_qzq74bHjeTpmbUKeUPl2RA1I4gJYx0pzwrH_IBh-oi7FhyWdboPg5k6r353hawH9Zq39x36hwGghjwEsYOBF4ZRxQAvjePcZOoVhXjKoznbq07MpW2BXlRN7zgMecM51xFfVP9tutg_MEylo58_p1EYhVoiijf8TOiRXMt1xenXc7VRVh__5s6r_uLTa1vHTzV4wC_Q6FvCh8h7on9TZV0sTgXgfm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=hvBhfnMpHoe0vU5327V9T9Xa88L9E_g9327DVwNQl9aeDCoOQQeL8QHWpGQJ1n0NwO0VYCXUDuWocdh81cncwPVyBElgPn0VR94kFEhPLdBjIQUduxljbw8ocTk0XY6uy7mPyzLOktjjAmgL9QqbVk7azO-QlJ7WLJiBaZqVJhE1TSP93Ef0CuVVdPblQRzPh8-5vBsWfhnt7iK-kFibDdAaCExnwVnM90ythJEj40xPszZag5kJ7J-gL039tPI5CLOgdPMuueZFQrKOWymI2tWDzsLNs_pv1Gf5oUFuPicBUttFb0uXzDTsITDQXVf1-FX3ZMI20Kh8LCE_1qI66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=hvBhfnMpHoe0vU5327V9T9Xa88L9E_g9327DVwNQl9aeDCoOQQeL8QHWpGQJ1n0NwO0VYCXUDuWocdh81cncwPVyBElgPn0VR94kFEhPLdBjIQUduxljbw8ocTk0XY6uy7mPyzLOktjjAmgL9QqbVk7azO-QlJ7WLJiBaZqVJhE1TSP93Ef0CuVVdPblQRzPh8-5vBsWfhnt7iK-kFibDdAaCExnwVnM90ythJEj40xPszZag5kJ7J-gL039tPI5CLOgdPMuueZFQrKOWymI2tWDzsLNs_pv1Gf5oUFuPicBUttFb0uXzDTsITDQXVf1-FX3ZMI20Kh8LCE_1qI66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=ScRCbDVjnyMa6CAPt7r1j-vpneoxxFjUblr7RyZOUEUUk9UlxpUj3C7lV3K9uds7Agl7LP5ANoh-aJN1ze-OT4NWuQW7JaJqBB2Sv6Cj9w6acVb4KSf9jlRqbgAjAgYcIy0rXVePqfkxzox-aDB0ck8j1EOxCVOSbgwaz0b_rZfttV7fylYs-NMe50PpEKczwUyGaUrvFEuJL2eo6QonsanJCWFlAnMsuZFb_AFED8xyV7eK0uaufWyjf19TjimZS5fu2d83O0o0N0eHntvK3m8-iHXTVLh-yGu3nxmAN8cPlyj6BIlUTypbXuGrW2ZVOcnrRF4Ot1fSwcAWtzzVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=ScRCbDVjnyMa6CAPt7r1j-vpneoxxFjUblr7RyZOUEUUk9UlxpUj3C7lV3K9uds7Agl7LP5ANoh-aJN1ze-OT4NWuQW7JaJqBB2Sv6Cj9w6acVb4KSf9jlRqbgAjAgYcIy0rXVePqfkxzox-aDB0ck8j1EOxCVOSbgwaz0b_rZfttV7fylYs-NMe50PpEKczwUyGaUrvFEuJL2eo6QonsanJCWFlAnMsuZFb_AFED8xyV7eK0uaufWyjf19TjimZS5fu2d83O0o0N0eHntvK3m8-iHXTVLh-yGu3nxmAN8cPlyj6BIlUTypbXuGrW2ZVOcnrRF4Ot1fSwcAWtzzVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_LFbs34S7ROjqvdFxSiFc9R9-BEDinMttg7BB702wSjv-rEjIDj2Z5ozZ0fZAmJ3Ay4SJtYsrFPMwwlTqYmRsdgPjmRtmUwp7BH11z7U0vdbs8m8edleMwLGmGkvfwcN6j3faUWg7daTKWteIlUDzIOC4BTkdRQ8gwsKips0bIjK-cLoOgUy4TDDYMOsEDDL3l3k0swHOGfVoRmJXDMwrfe02zBP_81wvFuasA4VdFOC6jifXYRpsnU55VZA2wpXrEz_MmRIj69sV_Jk4RNAuWGtEs9uviZ00rTR-E6I1iyn1UBwgzRUjk8jCvGqOg0Guo2DocaOsmBMju0zhtT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZ4x6_Vr3uaddmEEcPQ1_zy8semaChRV7FY2iTpRXNGbR1HJpW0ew1-SMYHTlzw3b-FdFuvnSgwL-Ogn2wJ6eIPymXkV998ugcFcdP3wsDIbKKIzy5Hgyr9pP_YL1jE6Wt6OmeNH4ewuZ8k7jPPU8omQL8Dxfttp9_YK68wMprXfCZpNbYVF9_V8gu4-hxOfypIuhPehus2WTMXc4ZVpUkz9ia-f0sEsWZVp_JZRKlR6P6Pyd3zlDBslJvl2eBVToNZyOEQlR-FkhuWfVfcwTh5uH3OC0_Jr9jXevwcf_uxCn9qFncP33cJ28WXGS5OG7mdhe_h9H1WlsaQrhH8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYZXKmw6Ta6Ju_ZxOjY18E8sfCK2bNn07BQsqk-IO8TT897tFzyk3fcTrLVPPPK37zXvH9yRtoaQ6BcQd3YNdiic477SDsh5RP_LevCVwtYZ0n75XwxA5qUWJy-obHiY_1VcZCet-Zu-rgA9mM0mZks0kRCN7-lbsuN1w4gHFTVs6mPOoQyfLhEFpfbp73h_cWnAvoos18uCKWprMSMoSLybyhLITJh7GWVrO0qVC5pndSu6gyyqaGjOF9wlGSi752dUWhXtobghHDb4rIngr8HxzDIk_PMqB7Yo2MG1vup-M4hAcJlFbFcug_lEiuWd8ONIn7rnsOIQSOv1aA64AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAltQxTKkLqhy09-Oe0UpTWJiVuF7ajHMn6PMacpd8F1BJ5MLHPOVgikcsl_jgT8NsbVVghnpeIse1dinJvnW47R0-UxMjGPxBWxWDFXIiVaROTpyxgxo7zIelQROwuDX61-RbOdI5wvaH-oHNkyL9bae6sxYtZfKU6pE1-L9wXx2BBgzR7melaZXD0CNUIN3jsG53xm_H8iNp4z29tQHchUzgK3oAzmyl2dy8XeYYOd3wNgjVXpQMi6SyspuVVgeTeDutVT0YZEtfUo_0pOXsHHMALzg7vBLeu6V5zQQ69u0W-xcKDYlajSw55v_fsjCZs7MeMrEO8wEvkIx_jJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3J_o4-FHp57PUOFRUL23AkwqylpH1CV03WH6ysc-9Xic3phNbx4bGxjI86952kjVieWqZIAxaQq2JDuW6Xmk4sqVeY2ILPwavlOOHlmgf4og5Q2-E6fy9C0Gp9nGchtk03bz-k9cYQC6BPumbz2jgol-b0ExZP6H72Vvth7E4AqJwO1QPhZMkrqjINJJeaZL_UhNzltZk4fD0GcK0Xso21YLT7-0dtAQfv16crVj7MiV6Q9PTcs0jWXuqFlMhvQOXlhFDtZ47L2OF8ibnjwqVM1DFhCb7XHdl-tb-uT1EVSo7YVrJcERj8hmyTYEpA-E5x63S7rF2Sv1KQEi0JPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc6pMGQwQBf5LQya2ccYrfuZF0TjFkt_v_uPAsFiyq6THS9Mycg3qjPbSbITdx09IY-KGnNO_g5c_6exFiQuxUsawIT6H48DyK3HT6bb9zAl6LmVKDuyQKDGeQqs3DPI1c1qpSBTxc-IT7tjry7UR2rScuyaDHkAzEB-Vx_93RBgEoo9yGEElKTYlPZktDdLXnB52eEho9Iv0IWilkssSuHhtNA9XowXe5gY_mkh9tG9w5F8XrjejjsVgt6RhpBJ_aRafb2uWLbUhHflnONU86o_fokIRNutz-bG8HLS_9pJ-5oZLnJfiYVo3JTVOems8gVx4w1ONbRff_9ZJ17geA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANsjEQOEZJka_JM6TkaGETdu1PRSgSKaRbCFzTHOEhBcUnyCCaLnziAzY1cNFtK4PSPUCMnMmhEdhheGUjc-4pVdvBb4RrsqHNBSOpLmKKzDLG0kUg-bmipDIwoP--E3cCme-BmJTbV0biyNRjP6kNcZ3LYXq4HaFoWkLLAtkatftgqZnlt8584oDzlZyZsCWScsH73Hoa1xNhZLbfBTGMCsRhWLqNVIYHGeAdXiyqnZLMVt1XTfkc4KFscsfZxASKeNvCQ-Wh2icaxolsxnLxtP9tegcUfCMD18gfwUb1LDZUZGG79P_bpWOkJK3oNo2JzQ4xFn6LxV8N7r_doyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=jKwWI5aFz_7D46F0ph5iSdmea3h16weZ0hG3ulfZeCZDFNb04UdITm1LSFd4Aksu17aGGKmE1rA01SYtM7OpQ_UO41ACs6YZNSIjBabVa3Lw74gFWhSC2SILbZc-XkR_1IT0_iGFNnX6R7ZaMEZkXfx3VkAZ4QZA1aHTfXMnSekmDSlvMJ0cDRfHK6acsO4sjEwLS0iqLrohAnT1axWQ0CtWBZok_NhJEkv8egwsvg7m8Z7oIbNWFQp2L-34re2T8-6jZpllThHjiDGUod4oemGO0_tlVAmjGFq-lROsbnthElHx2VdRnSbFNZjgw48F_sYJ--a22U8Q56OQdwnZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=jKwWI5aFz_7D46F0ph5iSdmea3h16weZ0hG3ulfZeCZDFNb04UdITm1LSFd4Aksu17aGGKmE1rA01SYtM7OpQ_UO41ACs6YZNSIjBabVa3Lw74gFWhSC2SILbZc-XkR_1IT0_iGFNnX6R7ZaMEZkXfx3VkAZ4QZA1aHTfXMnSekmDSlvMJ0cDRfHK6acsO4sjEwLS0iqLrohAnT1axWQ0CtWBZok_NhJEkv8egwsvg7m8Z7oIbNWFQp2L-34re2T8-6jZpllThHjiDGUod4oemGO0_tlVAmjGFq-lROsbnthElHx2VdRnSbFNZjgw48F_sYJ--a22U8Q56OQdwnZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVqL4ltGVg0MGpP0DNhUnSG8luf4TMTxNfHfiEKXZ_OQvyZ8-hiDU3ahUwYfnaeEJ5f97ztoOzprCWTsvbm768tTv3pFN6uuUOotz2EsZUmG8dzlP_lAV-jeXvus_cIovEJzwBFO1yLnySwVR8vTp3kgvq38f0HM8NWw6AsCooard6Pn5wkQZDvfdzxWxh1D3sndUNqAPrUS96XPhAfU06xqFhsinRdo3267GEmiCW13KXBayVctyOJUkusrIoTwltidTSs0FftVHUFMEl7PmbPJUoy38L6RLHSzHcSxyUb1RB5USAyLRx0rzSr_oX5MzmDStRwmxCOf0ax1CkZD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZukbX3bDbJCMWay5sWPyKTqNWfwF9fk0aVXjqNZ9iwRawWzdNOSd1ZN-uiNubBAoF-ybceWuGEjhhejuDXsMCvE2pNUHGf3Kcmjb6TKDhhw-gVtmwEVEQ5aTe3oprOV1h5jJDb3ik1PZa9EH0C2elhLJHJ-NmGsoDxIw2HVOzD73XQeUU9ajh3mbHALk7fOSPTh8HnvZyqamLgsqE_ji5wNrg-UGyT3OHncsQUm1B2KoSJy-zkQlKee0-cxLB-KqZfAgGes2OGZM_JfC_HUEf7MyvZmz6gt_GS9oEIgZ68B31YwJtuAGPueELoBho1KDhGZ21EPlZ3rlkWVodcE_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzGEPQhvQzbwH86KOfmGUlohWhiTxduQ3WEAiv8SUb2bClUIqGAhEjh10OpCQcxPtnWIO5jWp-rrWGv8IYB-pSZmSKrNU8w-UxE-xYyvBceCE5OqYoAxG7UNgZ6dQD2SCWLNf4XqKRtyW7A1sqWJpUYKRflr7oMmDcqrrVrtJxhQomD7LBofg38ZZusd3YETplk8dWtOAblYbb7_uV7g5JNyfn6oE3P5lhszk6CdUiVivZUfxRyoyMsuTeZxH83Lepvzm4Ddivivde39tqJE-Yl8P5AmSbWntpjGJaYXPCb0sIVKyDqvEYISrB1-nBgqV51Ef3reJ8o7NYEXG1U2Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX6QpqdM7_MQxrkL5D4kLZFnuGKZuwRjJKKMT32c5eaNc0iaHCvxi5KMTzmd7Pk_o9ljfegqapMU1yI2UzGacIE4gqdDJy4_K3LuXsZM2XixTB7qiPxRIcnK0IVLHlr6xIzyLIl4ZS4Z_Ts3XXg-M7iF3bWybeudfUfSmB3nPCNKemqJ2-SWYPl29il8lL55SeCpx2OIrlfd5Lvw5EE92pg76gMm9oKbjOldi4fnQQgmIVo1j-q8-rwBjgqOMmuPvUG1ZiWj2nwKbz0CDRLiKRHEXGmsR5AMdIh0SHwdriQJi-NkIB52ULvSoydaESjs1ZN539HZ9gba7T3p0v_jZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIbkTnQ3IhEp-5fkmh4I7O2KyHSK8tzBAdkTRm8HMuNieEU8Sx1ipvEpgsP0IMm8mq-o7qwjg27L98Xusy1Th1xqk5lg2tcK7_Y1buUG7N8-laLLMSHmLdMa_k0fbRHlSN4kjL5CJMl-uV4bV3PlTgo1QzzdmvnV2nZ3IccdU4-UgM8ce6wKLB31zxkyL_-p5Jh2M5XPuTY6YFiCFGzGdWWYpiqVCwzcFhL8NWshJRvYAJoCi4bBdZhR_kI89-vG56wfMfClGCwmSo7vF8K-0vFKh9eGnRPNuD2K9dH7Tv6LhZ81BBClnn60bbC6E7-Nsj3cSH3sc3yuSBz8k1RH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5lRmfgf9W9bv9gJbuE7WaU4GT67ZNBc5sQ4elk12ewnsybtP1t2fRSrQmYaMLDuh8VU7hKGlz7BOFdD3hEqwHOjQ1Gm6ECKimQ7gWfjKb43ySpylIhd0rEihwgITNt8efod1tSv0IsWxxopdrl2hWfR7idDvR23A-jPjokV36mGzTrQ7tWW1O9IpjHG24OSbDKQdYZrWi3dov3T0_fmk52t1mWJdFWvDG0IawcyJjtWl2HV9DYtWxbfgIHEt1GYf4qgdh_Lynx8N2baVwDBNvyO8dI6j2RMyt6H8sOZzpuhDdVKqkfZEFHKB-GF-rU6u_Swmxldx4epBnN4AJuKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFbWuAkMEO_WzaLOCmkNFOLwb97FDUEcKOj-yWga5AMgJQAO6wSF6mYTvu09RRHdQT4hBOTgv5Xm6iYU-fvEm4GI94bf_02FYop-RI6TOyVrVkPzatmOUQ_Vh-8E1qjBwr6sMJas3aitINIPlJ5YOBjDvOrGv1b_A_0-XwNuqUWACdSr3oDJdYP4uauxJgr5S2blmPIjDQF9EgKfMsHuViPcMAbksbHVjD_xvIK1HCV7Xu27MLzwu81dq4pUc4p2vfyqivNcFiSAJ-tpR-6ZLb94ulRB1G2PaOacBrFv76jQQdB-xN2RqCtTx5qH6vaVKBR8T7xb_oajSCUOjL746A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx6fH9YjTBprPFMPtf8_2NUBhjY7R_M9x7VlxsQp_aS8-mdUc-b6pl2dg1Voc-mlBeA7GehiKaybGJPEOLsYOvT7-PU_KSnkDMiNRhk6BYbO9Jepo6l6xyL9S8JcmTsJrxyZKIGkXUSpINDs-k9mS8I7G_5LOrfA7biAjEzTuLNRvuM7pqueL1zCTFUmOawJ3VkUiyxnFry8cUvLaQAnD3BiNEiqsllb-g0SVA4gHQFPezrG1fx6LgLNZxtIDMk6l9y6iUItxkM2QRArV2N0YuF2svAQQyT39zwp9ES5soeA4pmGfgFg20e5PCdxkN4VZFKlwQd1wpGb67Eh9PFX2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=om_jZzOtgAy_I7j8g9Qmjw7xEV0XLqt45uV6LbNgkch_7sKY99MUncDujpg4XcUQy1ymS-_00KzpTyhmV8Ae8p1p7xkzd6s1CL9CtpAJk7HOT9oBBFKrfLK8TAGVUo0reybiEr4plafk59sxRVZxb52XXPCZ9Z_oSeqOuCkHJIavmiOZTQqx0RQA5P0XRntVDJWA-C0xAHUg9OCvIJeDj-AxJIWheEHtmzAqxVh6VsYCnrKIxIvxnO8UZKz9KWdpEsGHGmprSUBuR7JMQd7d7_yl9sEd9a1u2zO6Duj1WJ0b5crFl5FhrApdulUWe_dn7nLHANzCivWxJfI5-veS4U2otKa_gfGPTgPmWb9bOR1w939DDKwI8TiL6ceIRfcfuJ9DhkYzZbcZz9KQruAI4vRbPPWz-N-gbWPLavJ1zCIw17cAhl8VUqpZraw_m5WbFlHrMq66w-aolB1omFILgBXtwjizIQRb9IykT5nv60G43LB6ZkejH7EjqtHaYU0zk2XdPtZ4uOC3L_lPp0NNdculu6MkWibY3ER8H-TM3YIUqAXlTFkTqMQA14Hj43aXoeQwMA3qnjxeJYU7g1RS8UZ3KdSx7LXL9hmchXw03xpXeEg42vvJ2urFkKkLDl0uXwF2r-uUWRrUiMc58OhTpg4JaIaWahP4d30Fz1GwjO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=om_jZzOtgAy_I7j8g9Qmjw7xEV0XLqt45uV6LbNgkch_7sKY99MUncDujpg4XcUQy1ymS-_00KzpTyhmV8Ae8p1p7xkzd6s1CL9CtpAJk7HOT9oBBFKrfLK8TAGVUo0reybiEr4plafk59sxRVZxb52XXPCZ9Z_oSeqOuCkHJIavmiOZTQqx0RQA5P0XRntVDJWA-C0xAHUg9OCvIJeDj-AxJIWheEHtmzAqxVh6VsYCnrKIxIvxnO8UZKz9KWdpEsGHGmprSUBuR7JMQd7d7_yl9sEd9a1u2zO6Duj1WJ0b5crFl5FhrApdulUWe_dn7nLHANzCivWxJfI5-veS4U2otKa_gfGPTgPmWb9bOR1w939DDKwI8TiL6ceIRfcfuJ9DhkYzZbcZz9KQruAI4vRbPPWz-N-gbWPLavJ1zCIw17cAhl8VUqpZraw_m5WbFlHrMq66w-aolB1omFILgBXtwjizIQRb9IykT5nv60G43LB6ZkejH7EjqtHaYU0zk2XdPtZ4uOC3L_lPp0NNdculu6MkWibY3ER8H-TM3YIUqAXlTFkTqMQA14Hj43aXoeQwMA3qnjxeJYU7g1RS8UZ3KdSx7LXL9hmchXw03xpXeEg42vvJ2urFkKkLDl0uXwF2r-uUWRrUiMc58OhTpg4JaIaWahP4d30Fz1GwjO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=hhxQGUlYNx0Zqjfk75U2LY4grdgsNgje7i6FiaOZWlsey_VuQqSK0Qc_GkrUtnm8v5n9IXl-mq2j4fX9gPtPN4bKhkWv0kGKgIajWdiSPbLn1c09Zis3-YQmv56YpLadwHMhCIz0BoLOKvRH4UG2jMJFbMUZdyC97B4J3t7iVU2tQNlUGDa84BAPrZb2zy_0GJmqkMxuJsLVKOronBYVvNLSWdhpBkZksGxQp65PKID65b9RPHykEMCNK5X54CpyuAJDoEVICW656ei7nJfYiAgna3ZKfJIBx0btC5YL_JmByDaAlzbRjDK2LiXJjs9dpTv-lFQsMBJeloRUoocicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=hhxQGUlYNx0Zqjfk75U2LY4grdgsNgje7i6FiaOZWlsey_VuQqSK0Qc_GkrUtnm8v5n9IXl-mq2j4fX9gPtPN4bKhkWv0kGKgIajWdiSPbLn1c09Zis3-YQmv56YpLadwHMhCIz0BoLOKvRH4UG2jMJFbMUZdyC97B4J3t7iVU2tQNlUGDa84BAPrZb2zy_0GJmqkMxuJsLVKOronBYVvNLSWdhpBkZksGxQp65PKID65b9RPHykEMCNK5X54CpyuAJDoEVICW656ei7nJfYiAgna3ZKfJIBx0btC5YL_JmByDaAlzbRjDK2LiXJjs9dpTv-lFQsMBJeloRUoocicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLsbenH_oFAhxUhxhpOZFcCardm4umQyvSmdKc-VGTPNcYWcdJYnhecrrzm9YQQ9-RrS7agz1WS7SqqbmZ-rr-erwfpZ8lx4Wp8Au7KPxzzNwNSGikKIG5D88Gh3Vw4I5x0g8pZdvo10oJY90ZjScbEl_nNDoUOu8erar3ElAFqJVvLEYcBehpbIkXvweqOl8_ToexNvCk4hBwsnpyA-8bmRHPhnQ9vqHD6I0V31yVo3Sgs7Bkbdujl6aHMFNKP8jmsUm7olbPIUJ31ER0ymvj80I_gI6lKuNCr4FkXpyhvpnbHMCQF76GBsXSRuaf5YJZVXcgE8r_iZ1J3DK917xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnB2-JTdotrtcc1wIVpVgoY3ry68e5YNqa0H8HFyHxxgOezFUasmsNG8-i1TZRMjSbsdzJm-ydvuqzZJYLgvaqVcke-kxn036FAw3ypnJ-uutB2cFMtW8ssjFxF08774cInq7_EFgQWegNa7CtR3TjMa4f4M_9ck_SuOZFhNfOi_RsB-rwEE5M62pDZ6K3QnlWnwz3dW_7zv-TaFMZi6279f6_L4oW0EJnE-VtQVQ0i_75zI6WSO_-SnuJvvLecjWY0awG8B50Rm7uZ5o6Fy-Y7vgqYBlZaKaRsh717_RxPF5zwULBeDNIEehao19C1pv27jZ3TchlTMUsRYl1cs0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuNfZEsAl_Oz_XJFwYtOXTYTXM1TTqErFbDCunG_uzrAovQXHx5aY5SyeKuE9CI465hCQGRgvKwloJXUQykc5bJGqf5VzvCSgzjJr1T77rTX2qMKk2HUaPcYtKRJdeqIq6-cxi5-s7SoxW-heH3bZQywOuooP4YPhh5XLjol3mP-YV24jjnBt0PiNYHOAYfM6L4N05KmGe2ITBIrQ_37ecGmDFdTa0ROc2MLlGfJBTal93G2WLLjIzJpOVAywiYaFvN66hcJLkz2G3VwRF-0BpJCM8N4B5f-03dR9DWpplbXdBkUBIl__-fXW6ZmDNKC7xvkTpDQm8DA5I2MtVdt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrhmIjiebdrFgrXFpnsl4bZiHPvagslqcBuaY0dmia770UfFzRDLq794Z_bd-XrDbDOE_kj29DZ-ytLdwjYRB7EMf_tskejMrM7KOVZAIaylOZJRqeuc1ko2M17RbBlQvpmDb4P110O4v_S81TSySBICzyEe_yjvYCaV0QPIGx5ClaeEeVpvMnA1sulymDiZ568Ny8c7Gsu-wsvdEziXgn-FxwA4sqHcgFRybE-bx_Ukqm0CTef5vjGgte4HhQevbOfrPfle2CZ4otDDQpKBnA8-IVfyUOH-GDSmdrp7VK1xlTrTQo8TqCvvjfPZdHR3pu4t3imbgX4PvOc6RypxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKWf251Yvm9uOT8KLHC4u7mpTttw_1JuPD_7_xTleNLNqx-eb4llrAodDijfGDY2WnvAfMjkYFExdtsAWYQDsM0oMwCsw_5ME7VQMoURQM72bQCVvp06cjOJN50HnxjD4nWWCvKBmgYfZ8uiziHdUy6rLyDsf28wohpfXIUJM2TMCVd6ytoCBEtpK0gbMvJD1RF2L3YTmx-nGh5Mybe2_fOXFBYz3jM580Cq4wuHWhN4F44jXxMCp7BhPUOLgXLLPKkTcyamn2zAvJ7q4z8HyIkRyybuyJ1jiifWoMuYQQQ-T43UaMZueuQ5zsZv0KHdmVONTpexOh1omLq0O1aJ_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCrYAFyrOlKD6j_eQl8hdmFlB63_QlG789kSzmTloaUuV8XnBmB1jXw8ekoGbMoMXCsyav2gR-8RclGMv8k8NI6A9LQTmyrf5Uit9uo3_7oPC9KDMWMnpE-rcy_3c0q_naFixwwCOzSmVrIlhC59Vo75ku-OFUbY9_ny2njwGR9slQ5rrgdEXuRNb3amVHAC0QtOpDzKLW8fnHzb7A_pnEwiGQ3f_ceZQvGwX5NiHyZ1KVv_S3aGqMryuVenir7z3PYxAOlpHaSK4azb2bQy1bsoxqa76X_EewOoe7mvxp1n0Nw_KNLrMQlKp2ZeTktlMPNPoGZa3s9lbN3R3XsS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU1UFCid13evygqpywdchqd1tBDsD667zpsooFcajAsnm5mmU4ZsvWw742l3L7vLK7h_B5XAcEpur6BlvXP4Z1MMYxtd9w0z955xxxo2aYPed11YHvGQ2W6dTKz2hj-msYg0Z0m6m-3DTSZE_IMVnSA-eE4vs0o9N0n2TR2wAck8OWYoRBD-xMCGcf3eAadTC9EvES-S-ZNACUhElMjNV4NKOvhhBz4hoJZLyiPkkH1Zk5_KXmQHZH42PcwN5-UCOGLKnmywt7ogZjzKC2kmRr0t11Iw1y8TGOy91U1_aj9YpZEL_rjWjf-s5c66TpmqAxIb-P3zQbiY7PQnOGFU-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Whjxtc48cJBK51nzZbBFJjrpaoyRiBoiUl5axHfeygpFHoakc92CM-2Z48iqSrqotrJXklUWjBIfUTllm0bvG8DpZTk38OztClMd2B_lgj6dr3fVWeT1CI00THiZb1xQ-4ez37r0uWLEio9rHZmlacBFqSwI8ItFY8MbwDGRaiWt8fqvFbJ9f1ZQFUqAylTVuOqN6vM3icJUiluLLjIh4ZlrNI_vE4weoDSqJICMkFptHVDofGxG-QvPc9rO3EJJxT1gXw015BRKYc0GUpiotLuN-4r1rnGwJD3KvOwG-A5UJpgowJGJHcSIIBEGtdIDIHf6RmEz7dCbotFaPtvQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqFgcESAaV2ivqZsf8MziI58q-mjU3FI2kMqejISIArzexJUj9F3DWlpPnt8Vpaaq8_4tg4qbD1VENgx8tm58vn-LJMLXqhs_VSvIQWH76SImWFm9-pdqYOgXy0QlxNlnW3SCMEsLalN13gGfoT-x8GXigmZapN9O7oW6rBPAZ6dMG-8XVlFGE_b0NyZrXkstHPCgs8m4T_l8EjVk7oR_cqgD7kd5EKU0GMDWxRARPR771Do4f30_aGRl9qaSUoLGUxTtnDkJtIunMKpM8Cf_UTs0-Q6vzhzMI1z4BUsItwTZePpQYEVj48OHCJVMW28cWoDjr6r8AMK-I9cxmwM0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=LkLmM_Rx3dUM5lE9muj0orDHFX_Uk-sYdfJYe91tXrCiKD04l2aIFoTMD1Yrmnr3IZOL5fHg0CHF5pPv7ru2Y6M-aks6qqZP34w1157Wt04PY3FkizcW1GnVoTUGp25KrsPZ-Kg80-sMzD3W-icu6J4ZWj3MudAST2BYtuouB81GDCrFcsi062hgbS_LrbpcKlcniqW-6L_m2-zOo67COcQTrkR8d5bbA1InRaWYK14NP4VML8b1RxXmDHdnnfMyaNcS7Y8yKFDGUbpmJiHlHMOFPxqEB23VNPiPvEwKNq02D91qP0NzG31NSFYgZa7MhUVrUoGuHuLFnf4e0cy8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=LkLmM_Rx3dUM5lE9muj0orDHFX_Uk-sYdfJYe91tXrCiKD04l2aIFoTMD1Yrmnr3IZOL5fHg0CHF5pPv7ru2Y6M-aks6qqZP34w1157Wt04PY3FkizcW1GnVoTUGp25KrsPZ-Kg80-sMzD3W-icu6J4ZWj3MudAST2BYtuouB81GDCrFcsi062hgbS_LrbpcKlcniqW-6L_m2-zOo67COcQTrkR8d5bbA1InRaWYK14NP4VML8b1RxXmDHdnnfMyaNcS7Y8yKFDGUbpmJiHlHMOFPxqEB23VNPiPvEwKNq02D91qP0NzG31NSFYgZa7MhUVrUoGuHuLFnf4e0cy8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQX2h7mWYf60EN-05c9yCMVtA1qQttOx4RWLAgwRux8tuUNsaWvRI0ZWI7l0KtV_20AwHkAgRWPNZW42ltQ1KrH-dPH2oGpuvgJlGhvW-c6Nk4r5PHl_fR1oj47jcTkUuFbcozeFejNYGe-EEBqiuEUaTBbNGDZlwJOBOjIn8hIjhQsI1RFyI2cHkPKHWtaBhg1ESvhGYSZ5_uJMm_-IKL3A59T44Knf0715ZD0MVuCcJx9zi7yM4hR4RMhgxF710xTdkIoRqjfxVejmkZVpntEnzSpbApW3UrGIrZqQOPDx3nMkGlWjUeIUoGj6J-LaMY73s6SM6QZzHWG0QOA3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=WSay74efBjbktG3xtdhKOsogvOTM_e6VSEtul_mEeUw-SlwvmHV_UgSWMwXghLq0H5DqEhllSUBfbOY-hOhrFSdK-6VlbX0jGUhS5Y3PfgMpZ05vy5pXDUgcXdFnmVHcnXtpProBevD-KVEZLwwSlEwfeIgPEmve8JDhtE0HXDkzYzIh3QQb4qv7kWQwCK5xHURqHP2rMDkt4X9b-RjYwUsUVJUlRCVWr4qj9IyKe7Tzl02HIXhvr2Mo-Xp0h1Ne1QTEzCXZ7arvHoubh58a4PGFCQNrxu9dOW4m3hkM1HKV0ctbMBZVIilievWRejEDG_j06QAA5DMsRegE1rKsUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=WSay74efBjbktG3xtdhKOsogvOTM_e6VSEtul_mEeUw-SlwvmHV_UgSWMwXghLq0H5DqEhllSUBfbOY-hOhrFSdK-6VlbX0jGUhS5Y3PfgMpZ05vy5pXDUgcXdFnmVHcnXtpProBevD-KVEZLwwSlEwfeIgPEmve8JDhtE0HXDkzYzIh3QQb4qv7kWQwCK5xHURqHP2rMDkt4X9b-RjYwUsUVJUlRCVWr4qj9IyKe7Tzl02HIXhvr2Mo-Xp0h1Ne1QTEzCXZ7arvHoubh58a4PGFCQNrxu9dOW4m3hkM1HKV0ctbMBZVIilievWRejEDG_j06QAA5DMsRegE1rKsUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=W53uovB0ZMKKsT3IaY9VTXcMcNwsyj3Rt1lc-mAghYfhh_c8tSWAIgfvU74IrnZvLT_DM2h4dUD3-_t_psVfNSK7SDMMPVO_9NdTISL5vywDBqgEPwAsYHB93WSEgMr-I7v-UZiux0N_8ol4eI-QdEgfGEEv0-hIHuHvirNceIPYMtHfMXVPOBdIhH9PaxRrcEQiOzTp5sANqdj-Q10GOlaH7sG3RTcJVTxbCzaHVU0CEmHTzed0ZYi37GJ7P7JIaM3PRM629qepW2kKDVzjkgSPkmGHisci296aVVo2VbmenLT_4GLyXW2U3Jag3VbPgi9t0ntmBflvsRSnE3PK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=W53uovB0ZMKKsT3IaY9VTXcMcNwsyj3Rt1lc-mAghYfhh_c8tSWAIgfvU74IrnZvLT_DM2h4dUD3-_t_psVfNSK7SDMMPVO_9NdTISL5vywDBqgEPwAsYHB93WSEgMr-I7v-UZiux0N_8ol4eI-QdEgfGEEv0-hIHuHvirNceIPYMtHfMXVPOBdIhH9PaxRrcEQiOzTp5sANqdj-Q10GOlaH7sG3RTcJVTxbCzaHVU0CEmHTzed0ZYi37GJ7P7JIaM3PRM629qepW2kKDVzjkgSPkmGHisci296aVVo2VbmenLT_4GLyXW2U3Jag3VbPgi9t0ntmBflvsRSnE3PK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR-vacEtgA63PAXO0VnUzclkRIbLv3Drq7H7_4fCVjz52mhvFlamkLO_vrITvsFjweE-LL9j7zsmj7vRJfqmF0T-G1C_EIN2V8BNiUwiMWx0Tngt0DzA6A3ghJQ0OmW-ThFZXvRylOmrsX4mzKUuZ6IDlBMrskfaiJOXKErdle3UUsKh6VrJBxLKKPxbUD4K8wqUAODFX1UScjf3t4wFOWTX3-IWrR4bBLqPhnUljB1WL4o_mlE4qhQpvpBNEE2y4PF8WPufp8DAkftHNgfqqZqwUxbdUm9kteRCJpHEGGZKDrmho3usDucagZHpBhIQ2lNu163KZgNYqr1fAiDf4g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=e6XEuEZwpON2QvNC0cLzbZKZ8O2TdEyNo5Q9H5o0PTnwBlIsLqCtoB8v77bLLYOiOls9PR8MyjUX1F8ICk-ltaNonHHFkKAXGhsA4-NwTiswk-AzJn1L2phqH5OqMjtordaH1uDWtWGQIv2YmaRgL3QvkSo325DvthGPnMLxiT8J2Sxb2NXDGkF3zXKgocqaC1LiTDAR7xntAkO4FRey9_1w-GklhtwEa2qU9CVPP4WPShi_8A9vARvrNnNxBo5GoYnN7OLrMSB1pVAXy4-6mWEgVhj305IcbrDXRDAfA6j2gSsugnT_I_SmrQonl_YD2ObTrgzKMrEuW3d6wb9d5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=e6XEuEZwpON2QvNC0cLzbZKZ8O2TdEyNo5Q9H5o0PTnwBlIsLqCtoB8v77bLLYOiOls9PR8MyjUX1F8ICk-ltaNonHHFkKAXGhsA4-NwTiswk-AzJn1L2phqH5OqMjtordaH1uDWtWGQIv2YmaRgL3QvkSo325DvthGPnMLxiT8J2Sxb2NXDGkF3zXKgocqaC1LiTDAR7xntAkO4FRey9_1w-GklhtwEa2qU9CVPP4WPShi_8A9vARvrNnNxBo5GoYnN7OLrMSB1pVAXy4-6mWEgVhj305IcbrDXRDAfA6j2gSsugnT_I_SmrQonl_YD2ObTrgzKMrEuW3d6wb9d5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoqBE4D0VxiQ8etZda2i8ktzwXgyDMl7_0VuT39U_h3sYx6TCNgWfjPQk_UiqOs7awMZ57NodpeC1Js0TUIPyxS8X8M2fxO50yF5rG--ChT2jrEMCIpjlimFQsNtP_2xY5Cyc5yRkJpjqNmgK6twC8lhtbnWGOtVAj89qVfePnXFUxHgKHa_303YBCth8wm5neNSXQ1VgBKGtXEdMjzT923-60jCdY1O6_NQUUcX47RwxaTfeovimhVPygqXAPkyJ8m5h_0LOzyhqfWXDOeCXjl_h0Ywj-pgJZdBswLav_XzH2mLdJaDdtPR6j2XmKkv3HeFftJRf4nwZAU4Cf2FIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6GWN-cXgR90qbuclhTvqsNNSQCHgV2yLvqMUNc__x6fEAW5hTNe978PGVfQx05Pc7V1EhF0qiWaFFwgJkvyCR1faGNzR7knv6ltEgH6hixcMvEKBHQFEX6gDGoRI8vr0q1AOnlY8iTWkMBSePvHq8FU3drRpbJNlKTSaIQegFpov4k-1sV4PaGd8Iu7wGSG8kxvAoyqmpGreGCqKBlGTkFLQDPmrT3n-j6lv_c9LQau8RP3sMkJES9aD8j2alIG1EL6nMCtHFlcgLDgDL6IHwc3W0gt3JWjxDdN7czbBPDiDmytHDL_kCty1ExdnKhfWqNJXA26wVfDtDa2GBekkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAHmbgMPai6Z6YGJFG_ocridbjI98p276SOm77VIixBUBwVd0XYuUAghlk-nxAMMcHoljlW291kAAeCGWNEVNCioNSoZc2ReNWi1lzlPOc4nJ13KIdnbOA-j4-jr-k2yzpAB4eLgFlB0IKErvneCWe0pJKZXHCACJtVMtNOLjHNDVOy3y14Ok5CJ7Z7cbs1LBnWWDizsLPhYxyo0z4DG1cuNsg_pREWvj54mZh-74rgm5LD8Qfs0vwwBwAnR2WlRszIdY6igQbcFyNT0wp9H6f8pImxiZqqsBVoZbtvyx_Z2ILHbbC5oysXPQ4_penuvrY9vrrQiIAvywkZG928qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXJee3Dw-sb2ZKiclc6RV2JHkXt0CZbIzkHhUwNkoAJXjAzkCdCCIkBHHC5vg8KgOp7euoG7M4GZhIy0B6vdwrIF6N7quqGJV5PiERds4KFz-KtV7SOlknkSmpPbzg6SBUoRvS3tkm8hRNA4n-FnqJJg4SrNDk64mUQISDrm57N7VJxyz3CQOM4xNmsNx3DZSL9sP5UqUfyOlkEcRqw__hifPiewIenwjPkZ3x0KpHi6mSpWaT0gkp_4oekf01_n4MZjSVk49PJ2bDoS-_wBoWsw7syLgEFr-K20rgEbPSZtWOV_wdexJpKlQ0N4TcNxEkmxFTWXdq0FCzpttB5X9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdwWhsc3pvt2tCi2bzHd395Tvb6IllCBzrnUQSXu5LxURmEgkmKSnq5IaL_G5z7Yy_6InAxRZZ-_YcESIckDHdt0idCz5UvbbXMWbM6LznWOid8c7Ts0puNj--ZssLqdjuYBBWTC8pJ3D4eA87vVGA5YO_F5XEop3Nylzbw_Ec-Qyp6uD8ewzbrCVAzpFazCIelL4bm1HzwhaQix9PD4xHlIaD76xA5IBpN7dQ4YsRRW5fI4pHJkGrHaoVT2VewF7hv9QMNWD4hLX5yYHEPwUSGf0ZKPOG74LdyMFHI5962uPnDv4aLcRMclVXg_YQJJ-NkE16PEioZ1mnjTGZsdvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDIIxWZ-PBfVJ6BjGY9suGa3LlV2ZItPLgFPvRbSHZ00t4ogsdqEjhSTgLWN-iz6enCM0UOtlP3l0N01DGbAibY4BG8Jzk9fSBmDC3KZPZG3cdgj_6O-Hdmy-cq1XDSaHOaEdi4SRndKkM3KCS8PhIjJ4EXIT_IoeKqHEOlBNXGTESGJ9FgL_GLa2zUOfoLl3pHA2jePlzzuvX-MDZkjOH1fX0MblHLRiIbgMp0Q-O1xw70JPTCjofO8eXXJXYIlHmmhgHP0p-MQrYC3FT7w_ypqpTr5ayuf_5Aufw1m2K8Uk8ru0gnqjpbo0hdFtsfTMxNRDB48PnWvS7gAqEGRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmWymzxeEFKiP1NMmo-xMaoBzLBBPcIUsat7HliFEB2xD7vqSyHeJ2X6v54GECpnEgFX6W6rVAAQVECqdV-6_3kogmFTecnfycAgO4kKSoP3qMmiy0869IWGvwmpBS4BV2CvqeBeVnFFHtTJBouLDJfIHiq8NDHvtHRipvcqIwF770neCByXApJA_qbk5FXNkV_p_ZLqHv9Q8iwTkNJ0gczkM7o_1Hu0-8hGO4O16fwu9xwAT80-HcTcz4eGjcT_qA3xtNXb1QitRSbO0z5oiUcYtlOJeST-DVcnF4fvkN6QV9EYF16Qgk42cAwsljUOpp5GFKXgjMN3eV6Tw6pgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT5vOKRkgQHNM13J13hYmiWyFCMvoV581RMItmfVaORo1C9tRRt9WsYITLYfk9il_uAcSZRnnbl-PZmj5Dt4FMFjjfqVOhOd9eH6e3DH8UklLSgwBmB_3YSuYB2XX2nn1UxgRLl6zFpAH8vKxTCzN2lonKRaHImGOo1KpS-8pyCQzR77Mn63eAeHDtuaiE472EZN0Q3TqDR2Mlbvkhzik4U9lub6mmOrbANf7STo03pH7Jf4aTRI4Ho-8yVIp5bpjWNFSTi9HgzFtOrK9jvNH7B9UXcTx4Xse9PUBqmuneOWC-e31J5bYKA2oC_jQmW5IxPKUF2QQ2Mds2HSRuKs-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=g3HhDxVyrAHCjTBgp-89L4HcF0nmoEhhl07687vU6lCxpXHo2WSkina9XwcNUvtlCffYI3mTMj6fi0_jA3F_vNva0ATA9KjSjxdFWKFCqofyjaexM-TGdivsFFypqsWY4o5lV1o1eVwlxRO6TcdzzSg4_oRfrgRp5KcyAR6t1HYpQLf3lngFMz-ulOjlGgphbe8m8oOPZiKq4f5EdUf8yCwJUiDKj1_Eq3qwN1oA8_juHSPw_Gl1m3M5hifbvBfC00u0R2EJbGd4DW0hHA9s_AfD9l5pie8Rsp1JNvtjhmZtZ1SZ9ko1hCdTIA0N0Sej94HelXzX9JWhY33pKBBaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=g3HhDxVyrAHCjTBgp-89L4HcF0nmoEhhl07687vU6lCxpXHo2WSkina9XwcNUvtlCffYI3mTMj6fi0_jA3F_vNva0ATA9KjSjxdFWKFCqofyjaexM-TGdivsFFypqsWY4o5lV1o1eVwlxRO6TcdzzSg4_oRfrgRp5KcyAR6t1HYpQLf3lngFMz-ulOjlGgphbe8m8oOPZiKq4f5EdUf8yCwJUiDKj1_Eq3qwN1oA8_juHSPw_Gl1m3M5hifbvBfC00u0R2EJbGd4DW0hHA9s_AfD9l5pie8Rsp1JNvtjhmZtZ1SZ9ko1hCdTIA0N0Sej94HelXzX9JWhY33pKBBaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=LJkzZmkWx-PjmaDdbWTUqm8rJSgq8ACL4pZYX3nBGgKkZvf3ZNjJRhcQQOrBcOIE6TomLMaqWkjxAHaOjq4kYza4P_9gH8YES4Az-gK8EKFDPKhXGnHQcf4xWHy4gTnIAU54DzDybLxQ5mx52X4HfpprdEgkP6dY4gm-HkGvmzejyJA0KRnNrusHmTxz_Fo1CWq5Zd_q0TH91TLn1SuoFxVliSRDsGp3qOltUC2P51bdU60GzdDDYuxnQEwN_JmrL_Mec54kIr9ReJNbWQJC7elrPNvE6TQXOGr1pVgtBjFtN7iWXg1dMvdvqk8jJqSFyCxfkiWu6q1ZDCMBCS808g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=LJkzZmkWx-PjmaDdbWTUqm8rJSgq8ACL4pZYX3nBGgKkZvf3ZNjJRhcQQOrBcOIE6TomLMaqWkjxAHaOjq4kYza4P_9gH8YES4Az-gK8EKFDPKhXGnHQcf4xWHy4gTnIAU54DzDybLxQ5mx52X4HfpprdEgkP6dY4gm-HkGvmzejyJA0KRnNrusHmTxz_Fo1CWq5Zd_q0TH91TLn1SuoFxVliSRDsGp3qOltUC2P51bdU60GzdDDYuxnQEwN_JmrL_Mec54kIr9ReJNbWQJC7elrPNvE6TQXOGr1pVgtBjFtN7iWXg1dMvdvqk8jJqSFyCxfkiWu6q1ZDCMBCS808g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=IfBJkwqv7p4HevIM19WbXDHzoTotfMbELpotHp1iOCjJIzlnXn79KxNx2UJoXIKeZzmlos1s4nA7VWdjdbp8IxR44ph362vcgAIbElFoUNQ9Mj6-9lqHnbHqamy2m6B8Dca-3M-vn7vKt_7n0EAwj8RO50QcBwijZzGVj-OM2H2-bxp1qnQlpvc6t3h3xdR8FM367CeKGHGRcJ2UXJ2eZhOHIYf4OWhqt-JP_ZmseusueGfdVDpZCb76G44mrmvWXpT5eL1YAl0zEGSwaIGmz0q2DWdJrDKK20nJR4_Wy5l7FG94HqCtFhREWdZK4eawoAhfYyXYsR76ud3uhi4nNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=IfBJkwqv7p4HevIM19WbXDHzoTotfMbELpotHp1iOCjJIzlnXn79KxNx2UJoXIKeZzmlos1s4nA7VWdjdbp8IxR44ph362vcgAIbElFoUNQ9Mj6-9lqHnbHqamy2m6B8Dca-3M-vn7vKt_7n0EAwj8RO50QcBwijZzGVj-OM2H2-bxp1qnQlpvc6t3h3xdR8FM367CeKGHGRcJ2UXJ2eZhOHIYf4OWhqt-JP_ZmseusueGfdVDpZCb76G44mrmvWXpT5eL1YAl0zEGSwaIGmz0q2DWdJrDKK20nJR4_Wy5l7FG94HqCtFhREWdZK4eawoAhfYyXYsR76ud3uhi4nNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbuN5IN94P29HRE1tWZauwsvO2mMD_R8qED6ZR2OpjRGW9JyJaUVtDtm9q9EUumcuHpafZ7SFJja1xE03ZIRqt1rWf2ynaw8w1bu4zlRZG4oIbpxN9IqceMauy43fGXZ8mTgGBJDU6iD3ZTULWccfljIm_czyI1ecmK3qSEiTfQD6jAzLxVhSe_uCzb_kpklWBHMZZcMG1I7fGM3G3FEb6viNkNDCFmv15UrXS3otFIgUU7HLJV6Kr7eBYWRbgkIsEMYW3FjgGcYwAQsRkPrazx4p5_3qR34hFfPRb3N2K3XcVurzvDNn7hJUYRrOnlGWr10JKHT9qA2645xFoFbXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQjzfPUi0jo71y0uc4mjlqm9xzbwimdpwWIEXlf1xsN70u4zzUTdAraSk8aeXwPRiA4fSlGuvkGr7SMX3RZxbszJF2jASGD3t7o7pdiuNVuKoPrP3oFE7_J2FTp0O1_1EEhM2MaWvAAbbHOCVdAVtv5hBUvnOVefI2oHkyFXGUEPhaQYroNjwUdiyIb6rtBJ8_8-PoTL2gXrvA0H3rwksiN5iSpyQpMf7RClYrShmnx067fVNdcXWTRCB2chSu_dCsGWfwujwgPxSSRKgAZVpTiUbC3Xm7PzFLsyDR52SVOGSoKOSpYQQqtvSF4dhWzBsrakHLAhbJheiEOT17TlfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU5K8zB41kYNQTSB1s0LL3pa4Q_PpN5Viwduc6ldxqGzlrZh41zmJh_F2biX-Iio4c8XO0nX4Ipx8RyjSetHmLwB3svk3NG0O2xDDm4DrwthZfIlNHrOjhYCw93d8yzC1RyRxqjpLwFdnJ9LqDq7Mr7xs_kRAcV-RXlJSzHKQlG7KeTAvsn5UDDlUpQvpGIk_Y4W3LxM19hYciUj425s2W39Kt1rN2erOH2-zRF4A50svAQc-zTI8mLgljg8PItcTEPw6exYJfZvX13RNkt0_nRiV_0-ti63OoKSsw4uWLvyoIg5OBCLPkOOljeUB-uLnoK_xnH2fZyXpjYFj99ZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBFvSoqOipkqvc1Z2IAoYBxV2kCy7kBcXHy31wAWFYPyRRLIzUYJBKHjvKDVCpc-tClw8Gj4u79RX3p9rhz8tY42cEQfQeEG89dMfHN5CUNcBSZC2uyFIb3NBoghcr-EgwkEjjrKU_3eo7lkh-NNeYftNr-W9DbsnSzP4ENqsR8ETJmChHCvbdiQLKGMqyzi-H8ZawZpwoqQ19OUue9FR7SThYTNxEcoxFxomKQaiOBkLRyj6ckGTfrFSGADEjO7R7XkYL5UOlgFJVVnlm-HvV1pexXHbTw2dTIMYZ1yRKi_M2LVJHC9iZVcwHLGd872Crza4GbswEgbSJkq5Y2HjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=sMoAL0ahMu69_O0tkYFF0gGSeheJDmHOP1ENRt0gJuTywTvCezaLlGDJ2nPa33tZviV9cvIuS9z-_iULRSdwYppIuxB1ARp71cjjT3pcGk0fe66-Xjyq73vS4WckdH76Ncv357l4FmCSDirjsMyFedMK3lyZtOwGNDABswXNLqrGgmJO5jVcGJR4FOIYdpbQQX9WYA0bbimAEFCamigEscLmiqWvZB0V6SILH3qUf2v-vTLRyBjmoCRuwQZOd9qMd6H57Bd8VT9zMZa-f-6IXgzHvHky6rbpUiX_jNQ_XMXsvoZnYjjA0cRNvqA8029gdrcVfbcUqxCb0z6cz_7aZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=sMoAL0ahMu69_O0tkYFF0gGSeheJDmHOP1ENRt0gJuTywTvCezaLlGDJ2nPa33tZviV9cvIuS9z-_iULRSdwYppIuxB1ARp71cjjT3pcGk0fe66-Xjyq73vS4WckdH76Ncv357l4FmCSDirjsMyFedMK3lyZtOwGNDABswXNLqrGgmJO5jVcGJR4FOIYdpbQQX9WYA0bbimAEFCamigEscLmiqWvZB0V6SILH3qUf2v-vTLRyBjmoCRuwQZOd9qMd6H57Bd8VT9zMZa-f-6IXgzHvHky6rbpUiX_jNQ_XMXsvoZnYjjA0cRNvqA8029gdrcVfbcUqxCb0z6cz_7aZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=HdAJhBDeJ6ZHpo6lr8PX1k5TN8xWr-J0D82aL55YzaSTEfAyjsYLato_zSY63Iiq2MxoxTXBnbtQzWn475Y0FnrZ0N5gNbh39DZFUkhvZnBT4xwsG6Mekuf1aCCm1klDxYCn_99yVJu9rMwZ8U1L2LjmzE256MQNyWNAt_3eojyX1CAi5T9gi1X6be-fajbJSNlfAW4iU-9amuDBxn-4t2EZFOGmb1eMrqWTuoTE6XtahNfDhjcmyfg06NtDGZBce-kb7-1FoNxxbKu2Ip6zNCFrc_kzUo8VvNCKKkNQor9CmQDYsOLgbbwE6kVNE00onvxjuW8rts7wxNVGCIfD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=HdAJhBDeJ6ZHpo6lr8PX1k5TN8xWr-J0D82aL55YzaSTEfAyjsYLato_zSY63Iiq2MxoxTXBnbtQzWn475Y0FnrZ0N5gNbh39DZFUkhvZnBT4xwsG6Mekuf1aCCm1klDxYCn_99yVJu9rMwZ8U1L2LjmzE256MQNyWNAt_3eojyX1CAi5T9gi1X6be-fajbJSNlfAW4iU-9amuDBxn-4t2EZFOGmb1eMrqWTuoTE6XtahNfDhjcmyfg06NtDGZBce-kb7-1FoNxxbKu2Ip6zNCFrc_kzUo8VvNCKKkNQor9CmQDYsOLgbbwE6kVNE00onvxjuW8rts7wxNVGCIfD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYpgnr5TUMi8uIpQ2Fsx76rov_9TcLVjie1_LXlgS8Yov95GEmqL-_2ZhoaQdO1UDGOdZCIuLXsnpB2gu3MY30MXppl3aPUA2q38RMmCxKTTC2xS6FN-FZHjs6K2ZVU-IOftZJhKP7p6WkuuQMugjPgx8bTTRTmo4wD1OMdzJ5JsXf5VuIKeFMHaUaxL2AY_KlFLVvV5IdVns3ESmPLCkDeSRT_We4npEMk46uhNWBo-u9XQDDGT53wK2IqQn_XzGYSw58TxDmBaq0EkBEOxkKma9RY2U5eFTcyoysXKYs_edDPGYf5EB29wCTFeODHEGBIuyCTHfRxKF1mlqLb5sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc5uMx8r5OTeEKYRCztdODCD_pCu8i3AJeEnru3ZBnrFcNViET2sU75RD5UgcyTrarJnYnvEobKdd9accP1uBtyqApekhyiVadx6yJoTG2XP5ByFx6ts1zOi_tCzTH5iTsZnOQdUkBbBz5MijpAqeMCceobOl3t3Hs2BWZUSru4EZgbJiZE-0F5YNvCpA3RdkthkbjD8_C5l0F7v9ww1T6LeWo82oX0ZwtThYB9kyA0UM1AX5aSWaHPCkAo5idrYTXBG0mTo_IG72ZoqZ0053M8fzhVZx88CkCEg5HELqpzzlU7EG4LEFZwrCt5N9XBZ2oh4T4E6OBOf3aoMUTkdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc8-VLtpJQbgmYUU7dGcprO0lFtjc0HqGI7Ryg7MZmpK9veh6iMSJFX2Xb3N1AFluHyMM070pbD4jvMVBJeB7_Y_GPIXcdcFIcUacCWurd-pbwLuKrm3aAyUcHOcJ3x76kqTiSPCBidrxkPaxtJPTt7_OD31j4gOmQm8ryBhmYwCJpVP9_P_0EehkPyCmVep7eRkrjB7R0mCN9SyGBat3JIHGm3J-Zn84sqy_f10cKL7v1lkqybM0SRQSJ295Sm1diMbpKJAOEa-1HitNCZXlh9OV9ZLHLS5GfdZrA_qOCoRgTWQ9MTWnmuf_d8eYTxG3l-b6DlpLs9ZfLifHQW4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF7J94oh4NdkWq2vT4SmIQMd63KxZra1JjAyR22VrBff7EwTm_hznxvIUYvSWr1E8dfg2MGes5KPnxw3hDl_HxYFgrafBySIy8tKdDjWtH4aQRcpy33F0_t_S3ts73wxrOI15HMeLdqqiZLKGu2-ZmVAOk0SPpc5dNgrDCCMAs8ysg3a8DHyrPQoJnu41UZGzTc-RjsESFeZBtzRRTzz1VvFZk-Vfld0Z1wEz3skLrUQPXb43CYFF6qBR1ChFepvTbezcWTAiPZ8TstDumXluL1f7X75MjEAV4Fjfko-l2JKVu29hqd2jg9Jk9793noneASoPrk3tIjSjtdcmUYs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6ioQDj9Qha7DopKSjVMxUNrfIhKwmmFEAoe3KBW_aZSc_86FEo80aJT6hLit0GhgxVZVeYQxU8asRpa6LXlwBIb4Z92IAVjM9QWgLQzus-1LCM1pReU5A0HPXmsyq-FEVhY6WH3l_4iQVPmH9xk1z4Cq38LIcStlucf2ksZOJ0x87qZUCW7P1xmNfaLKFXQDzM0_gulsRM4l7590pZkc-YosTv4iMaL8xfR2GMdy4XWC5g-bMv_WJbxDLVQFyoP1C8gJoMJJUZ83CTZGh5U_PaOn__T6XYKFxRRPwPShY1yEHdlfKQVKt0SX79g1lwcfGvFi-kNejnwDpD0ii8tRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1t6LGBCxY3nBIx-4R7GGZnwXEhcXAi4OdtiVXSHMi1kqSZ3YNEFdQHWjw_GxaN0kVgF4zqVSvW3fKCv_yq1ib6CGBpziPAjvX7gZU-HAnXoFCTN3Vvfkdxoc0OkqjcKIMS4_SnZW19HcoPy5NNBb9NdexSs_Six2IDAzMJXSyrLW3OS1DOJ5gaJ2tNMPeS-L9-Hb0dMVROSTGNF_WyC2egnN5C1Miu7PsshulWD1tYkzJNMnufRb4rw6iQ0Q1h05CO-hTRi0A043h2hkLJdju6-owZ-PCyQp-a6Q7b34NuM-aER0fx-3cEZOaMSs_pf9ToXr2sfQgXJm9SrzfLgCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DonqQZpn6qOy7uupXBkrgyLwk0hl8qyJtn4z4zfDqTCbFsObZFsAoPyjNY2QJ1TkJyv1cGS_y3BvCsjUpQgfn9o5RxaEA8Qe8uQlDC1lzVzRoHlGvizeKQlGuHCwnePEqTn9ORr-i-1GoZHQE8yuaKZaKp-sd9QSrvBxtYbLYjD4kKRBEGNZoZPtVQVEpdyAfrGYnE-1li7QqBYY9Dat2C_qZogGRx94QLc0r6y9U8IEZW9SNgz6B_oNv067jFv7C_dyZ3qMSW_WnRJH8KQpRnqAdOJZbVfgBhKF-wG-tK6y6zycjUIBrkjtYqHR_A9eyslbOhAkjjiUme_DCnCeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP6WlQtkPQSmSiMsKgcy8-BCQoAxNcGi3md1G_08_iL8_D-qAh6o3dxqYgh-fmp0pm8B3DG0xLJ5w9olBr0g2uwVjVmESkrmeKDDYXZnD_vun9jm229FkbA6Fp7r3sEbfsoK4Voqn2lAMZbfE6bFGGQWtPWVsBoSb6NKXzbDjNZpbjOaRlxZo3xn5q0ysv955OsO0TKxlx9lXF6knDFShnT6Y5BKO8EARAjonXvWDzPWSGrka_zlc-56X_aHQ_GaCzfEOQG3V1y1BinafuISjFcgjPCkpanNyT7_vC_hEbpX3lALwLaJ4imgYh6cv1KegF7u8Sq6pVN6vuWJBuwa3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=Um3dE-3mzpSiKemqbXuiYG-mXziOG0P0RV-saD8N5fp5xJVO3lvHr_MxJ1H0oxfQtdjek8gwjExw8gqJcrJ_pgT-J5xDqCPxcSrFs3qE5JXcv8jMyKDMqu3BOBg73gN7R_qUkIcyuMmnMCJxCOV7WO6OYeoxCXj1TZhWQv3sDX3ie15PspsudwHxB1v8KJXT-doq6k4ho_gs3sNs1v3M8_x9F6mBuhjE_7kQ5wphUBX-Qs9EA-KioEGiFbACwWSDy9DS7xQnk5u1tWLpNB6FRrbDbzDEn7TRXsKpRgjQjeEKXK3vRh9r7zEnKEPuh_YUJL2lkveT3MRVHR0tov1BNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=Um3dE-3mzpSiKemqbXuiYG-mXziOG0P0RV-saD8N5fp5xJVO3lvHr_MxJ1H0oxfQtdjek8gwjExw8gqJcrJ_pgT-J5xDqCPxcSrFs3qE5JXcv8jMyKDMqu3BOBg73gN7R_qUkIcyuMmnMCJxCOV7WO6OYeoxCXj1TZhWQv3sDX3ie15PspsudwHxB1v8KJXT-doq6k4ho_gs3sNs1v3M8_x9F6mBuhjE_7kQ5wphUBX-Qs9EA-KioEGiFbACwWSDy9DS7xQnk5u1tWLpNB6FRrbDbzDEn7TRXsKpRgjQjeEKXK3vRh9r7zEnKEPuh_YUJL2lkveT3MRVHR0tov1BNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=TNZcWfrMoVed5aA7IIKR1mLn5hzFjF5SSRhsL1VftDQIztcTUzbfggjhjek5Fgim12WKCiiSTQ5JDboiCJnM6zJ_r6PmBEMplYDct3OlluucMNZnSPst-tIOKjA5mijcg2MmHD6hHl02QeNSS28PvDb6QEp4zv1t5Von96vmKy6AHeH1zdHf57MB5_rkW7MQOa5KopGBm2BPECJnNTh0ZgrBMD05Umx6Uj_AGyCulScDqT11RTm5k2HO0UJKePCi37qDCzjfNC0QZHkbt0gi4c-Otu724lDNJ8_eqEL9sc91GmzJ30vhs9CpDtFDrZgD_zJs2NyYxGh_sITP1f78qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=TNZcWfrMoVed5aA7IIKR1mLn5hzFjF5SSRhsL1VftDQIztcTUzbfggjhjek5Fgim12WKCiiSTQ5JDboiCJnM6zJ_r6PmBEMplYDct3OlluucMNZnSPst-tIOKjA5mijcg2MmHD6hHl02QeNSS28PvDb6QEp4zv1t5Von96vmKy6AHeH1zdHf57MB5_rkW7MQOa5KopGBm2BPECJnNTh0ZgrBMD05Umx6Uj_AGyCulScDqT11RTm5k2HO0UJKePCi37qDCzjfNC0QZHkbt0gi4c-Otu724lDNJ8_eqEL9sc91GmzJ30vhs9CpDtFDrZgD_zJs2NyYxGh_sITP1f78qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1tNkj2yOe0Ugm4JV5aPZnzofNo79G9I7ubfcUVtDbLmLVBqj2wi7HL0oUpaemuWaE_3USk1CkjRIFqRgJug_t7Q52ShaK_eSEWTww6iAWfkypJd7dhgv7_IpTQdM5btPuYvw73-MAyVo-CbzwAueTSgninV9buRe771hXeGt2KuZa8y_RhvrDudnqZN1o4zh-Od0yTFJwPrPahfZ8kylr5Casw6E0LRvXcRl4v_gE8rf9azBtha1kK_tsF3r8vEgka1pAmiEqKD6z5fMW_1hD58Oz_s1kHdyjpAUC7giq1tBdR2KE0OPISEu52kl3Lf5bPe5gEo_-IO7o6giVBJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhElplhn7BfRoK9vdQpll1-OaHNCLj6qeJpeUacuP6JEO4rAeGdPbvK224eUMEpTInti3snplpPD13NLGXUcJ4nBPvuchT3dBB3jF5s1iHENf9VHF6OQ9A7G10zz9czTbenJY-F0pzDgVqGoppAoKekez8MwZd_z1ZbX3oANTdw7VGqEg_H4vBcQfPeH-F41ZPCIqfJNwhb3M4iNdNxn2gfTqWnBH5XnLJthLkWv5El5fUiBVKnFOQXvhsiuVr4h35_35FxBgJn5mVEwU0sT3XpmKKslvlMHAkS3Zpuu5_J8nCaL6VryEQgp5TqvCn3Y14T5TX6rToLYEoGDKphEiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=KAM_wMoRugRfcE9uOTn93sQyh0bd3wDuTlz359IqNt4m50S-uY4MSmMKMPX4a6sbwnN8MiinkuUI75daGKxHIfWsaeZW-Ry1AIVxKvP4gg3Pgf-nZp-Tg53b21Vji0rvwsVljyRAdANK4oeqADPFPyKEIaiD-XHC9XcIOBoOXjdBIfB0mrZ2hy8DPX77UnNjTBIPfzBxfxx6zUtDqHTSr_nqdA0L9pgKJQ-xPURj0ZqCkJm2fzzfWvoUZ0wtDFTI7xt_6xxDPrehAxbg5zhznKLjT9ACs4rIapCSmp0K73eK8Gmk7VqjlPLoh9JL6IPWEMVU8P6n5tnezunLLLwOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=KAM_wMoRugRfcE9uOTn93sQyh0bd3wDuTlz359IqNt4m50S-uY4MSmMKMPX4a6sbwnN8MiinkuUI75daGKxHIfWsaeZW-Ry1AIVxKvP4gg3Pgf-nZp-Tg53b21Vji0rvwsVljyRAdANK4oeqADPFPyKEIaiD-XHC9XcIOBoOXjdBIfB0mrZ2hy8DPX77UnNjTBIPfzBxfxx6zUtDqHTSr_nqdA0L9pgKJQ-xPURj0ZqCkJm2fzzfWvoUZ0wtDFTI7xt_6xxDPrehAxbg5zhznKLjT9ACs4rIapCSmp0K73eK8Gmk7VqjlPLoh9JL6IPWEMVU8P6n5tnezunLLLwOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud1L-igEejltR-D7xVP8-ZA6JDJ_d0xuvYdarQ7S7ViGrHOiatUVAXbfTTuK2pQ2KZT36ViUiRdssMRvUFiBnuag0r-z1TEb8doy8sPigxiXT4JoMqSgVPLFAd4TJGbtrIH3d85Da5h3lPwZkbyKN1N8F6DK59W6C91loWsOrLa9pilaH5SCfCAJv6ofyIet2QfZIuR5lxbD9n9m-2zauZ6TqyVym6kYRGlGA2S6Ushgu7NGjw6o9ip9UvRzTO3uNN4T0BsXXcT5OQ80MUbHuXrTxzew8zUGRCjPVLVv0AAkyz6a_jj0adlhSPoG8NWLZiQWq2CLBfPwE4y0EQ3SlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
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
