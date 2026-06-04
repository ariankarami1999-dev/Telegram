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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSzSJHYVHVhFewxWEpvvBqFV1gnDezgXfxULomicmmGdKIwaXklgjsp3MQYMR5f5I2HJ4PcQ9jldRJ9eZpoyWTp4-XZ5i26Aau4CqrqJht7DWk_RhpRdtNH0hdCAWctFwhZvAjxvSaBRwLAi-8zivbwFVWvdpsrZzFaUcdAsuUP4XxDM0co_wQhkFe5zmDt2Gt_ffBhKvaBBRX0v5ukeHrSsSYvDLnXp-vvl4WC_-3fiS3Ly9UsRWWyL65qjNGYU8aafGDDscO3Wxons_Wb6M6fDGT5d4AZcby1daud_Tjzzuu3Gx1AMISQH899uv-XkQypQJl8CVCBxs54ytOEQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR7MSmD4ceg44KxOVt_gVCsntJEWKwc2FX31xcKBwYnKqeYikgwIdPMWEs-InCiCL_kPIN9qORACCUY7Cab7C6lec2w_dcDAUuaY2cXJwyuALsygLtEhOzGWwrj-XBxHPIVQ93QiqGBeygduhDOxKswXRP395TaUCj3t2Eumfv2-J8-oHtpFoM-Xk2aBtCX_EpyZMOGdqSkmlyKCVbhdR1o99Em93pBqWyo2icaCTFOlFrQMY8_KNIPpBLkmyz_26qvVmBaTLXHDLPPcxHkqiHwqCFgkjs38XfGPri4HFaoWS7FXWQyJSQj5X8sQDXwIkb88FuKIaGG9ZJqBcDtWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDAj_UAwChIlpkjR3sIGpJm7VVt0bKWgHnFM8CXWi9mma0BL8UsyTPpC1I136Q0-eq6AkMLGyBmO1gD_H0ntLL8hYWbcikAXt1QxuVKRnd7YZ1NYK4jjPu-2OVBDCLLMOyuASmS5WWbgVI5hrjaYXNfxtWB2rlTDNemJWw4zZsCDpuKix0PdagOgCQxanUdvJ3lOr1Ed-hWjRtuOYrl_W4_mtu5vKFCKBK1EDj278ivPXLQZ4QkOJ8rHsDcxznmCAwHf-afwz6wVpw4VQeXv0X_uV8XjnYwzEQtcK6_dxJamQprNcy56gWDdoUFkK_tEuO5y22bi-zkREKNO_QwGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=AixPhBaZDAON5WO8IYZnTKW2DE4rlT4ofi3wQUEi3F_MEk_i-3zoegWIjF9i-C8mmGSH0Aw8Ys9oCYITuSZ-BRoMo7RjWJJdhSo9KnwUduGQ4LN2vZMOV3gabSQkbNKBs-JI2u9DvQa17ZR2oMzXjs6qV_R8F29KZ8t3Osg966FaVK-eWuHe1KQIN2XiEJqMlEmt5TmFf5AF-C1LsX6WtT7SxxfRmiQ5IOJ_PukuxDv2T-h4i26QKi19xLyTVDJBXQgPwak4VLTPb0knw-l8hF-QMZuvIvuxPDvRwhKTqi066oHMsTpgXs-L5xoqjeh-pcjS_EHWevHdIH8E7zh6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=AixPhBaZDAON5WO8IYZnTKW2DE4rlT4ofi3wQUEi3F_MEk_i-3zoegWIjF9i-C8mmGSH0Aw8Ys9oCYITuSZ-BRoMo7RjWJJdhSo9KnwUduGQ4LN2vZMOV3gabSQkbNKBs-JI2u9DvQa17ZR2oMzXjs6qV_R8F29KZ8t3Osg966FaVK-eWuHe1KQIN2XiEJqMlEmt5TmFf5AF-C1LsX6WtT7SxxfRmiQ5IOJ_PukuxDv2T-h4i26QKi19xLyTVDJBXQgPwak4VLTPb0knw-l8hF-QMZuvIvuxPDvRwhKTqi066oHMsTpgXs-L5xoqjeh-pcjS_EHWevHdIH8E7zh6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ctoj4xfWTKPkhAehbB1SkA0WWi0IEv1riL1s45eoct98pOwTSR1w9CEte-5WTzcQhrZHXkFRKmviAIfjUJUFpIKhIs4utSFviQnWvMEAPsi7yfWsSofxsh4j95UIq9MLXVcMVMSeeas01YFp_T6nSouFnd-WOfmtcVlvVRxEXpJkIUTelfa-qzcMEQ1y_6891Hxo1Mdro6Y04kcJbGYd4tPlviPVDwpqWRqL6-BG5ozcXqysETQleI7n4TjNWXnWEcqlYut1dRi8FNPuE6H-aoDJYuQgyII9YNkWvoNg1OYTp2eeozylgBph7tRyGGzNnvKCKPgMtlknMkCnmF4pVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ctoj4xfWTKPkhAehbB1SkA0WWi0IEv1riL1s45eoct98pOwTSR1w9CEte-5WTzcQhrZHXkFRKmviAIfjUJUFpIKhIs4utSFviQnWvMEAPsi7yfWsSofxsh4j95UIq9MLXVcMVMSeeas01YFp_T6nSouFnd-WOfmtcVlvVRxEXpJkIUTelfa-qzcMEQ1y_6891Hxo1Mdro6Y04kcJbGYd4tPlviPVDwpqWRqL6-BG5ozcXqysETQleI7n4TjNWXnWEcqlYut1dRi8FNPuE6H-aoDJYuQgyII9YNkWvoNg1OYTp2eeozylgBph7tRyGGzNnvKCKPgMtlknMkCnmF4pVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=EIsfoidtDMsRUE1Z6FhVMO1OjOi6zpKF5Y8_FSsfWT-Wy_YLKEkf0qobMfM5tyy1AIROn8_M_DioIPdH45sdwuQq43TmItKvF-hlvAFCwgMEt4s0HCGL5ciSedqf_RLl-svjmcU_H3_ZXDO8k59iOFR96_33QBBiZyaTpiCHYj8z6I2VANqjZw5owyg5ubfiA59H_T-2Er02c8qiyUm9of0wb0WYENjVamXwoJeWSBU1fEoG4dzGLCj6qOeFkGcdBXLoLzIjMTSI6tsuc6_gUusyzS45gqjzWmO-WHSoFANBZGVngIElmBI0nIPRt33O1ogBTl-Wr-p3sbuw-5e-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=EIsfoidtDMsRUE1Z6FhVMO1OjOi6zpKF5Y8_FSsfWT-Wy_YLKEkf0qobMfM5tyy1AIROn8_M_DioIPdH45sdwuQq43TmItKvF-hlvAFCwgMEt4s0HCGL5ciSedqf_RLl-svjmcU_H3_ZXDO8k59iOFR96_33QBBiZyaTpiCHYj8z6I2VANqjZw5owyg5ubfiA59H_T-2Er02c8qiyUm9of0wb0WYENjVamXwoJeWSBU1fEoG4dzGLCj6qOeFkGcdBXLoLzIjMTSI6tsuc6_gUusyzS45gqjzWmO-WHSoFANBZGVngIElmBI0nIPRt33O1ogBTl-Wr-p3sbuw-5e-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=KyCzhwZFm_tDl9unJlu229eHmheAoq0fEWBHlC-noN-sehzCW0cgeryyefGGTaZmHkAoDwwcgj7CdZTdnm0SDc6kka0Q_KdRI1guHsVnUB0PMe26T07w3DXBm0Z8R8JB9itoCTsCVjaAiuSmI4wlnolKVKqLgnQ1trJSc6zCVXFeYX_x1t2vudq1UMZeU4nLEdG07t9d3QY4GR9ZjzVQSaJjMkWgfJ9AEtR8MfF9xc-h30Vu4f01-tkdsJ6-QB5QUYZnR_ds9o59lUxLwf2N0u6rZW5Bl29a0R--mavL1mK1BeIJ07aypnu5OlpLRGdV4xrbueOY41JEJBouRshrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=KyCzhwZFm_tDl9unJlu229eHmheAoq0fEWBHlC-noN-sehzCW0cgeryyefGGTaZmHkAoDwwcgj7CdZTdnm0SDc6kka0Q_KdRI1guHsVnUB0PMe26T07w3DXBm0Z8R8JB9itoCTsCVjaAiuSmI4wlnolKVKqLgnQ1trJSc6zCVXFeYX_x1t2vudq1UMZeU4nLEdG07t9d3QY4GR9ZjzVQSaJjMkWgfJ9AEtR8MfF9xc-h30Vu4f01-tkdsJ6-QB5QUYZnR_ds9o59lUxLwf2N0u6rZW5Bl29a0R--mavL1mK1BeIJ07aypnu5OlpLRGdV4xrbueOY41JEJBouRshrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZYKhksK-ScuXSjgZjTbgy6rqDWCjURSOaRdUw-dSYGt6cpglp-iPETwCYjnM9FTkd12hYCXiONZCA32KC46ghPxvBO6jyebk6vXFe6cqR8W9yL970JfQ0LDi5ts_1C16w79NgAAawjyj5s54Y_9-3h-i51uhvLUTCEXdX-86LPqdzDCW4udhl62Ttx0gADpydz8-aDekE3DMPWaio60YFRrXel4KijgtrTt6e70m8RuwIEVEoDKOoHzsRK9k-zOpE9__2E9504IMBx5v39DvhCpFJYg1Hs-SPSG0NNShANAtOds6oPi6x6yXJyVl6MQYzNZ7hnoj6nKqJs0wVZ21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oze0h-XhhMjj64zCPpjgYWXcKygM5hxu0a_rw8pG2N1PAYra8wgS8G5g7f66IQOccux8ZTb-LlrdQ6LE848B-dZAApP_-1p2H2o7XXPz2DIloY9wbaS4_qgGQEeVS0YMnARLPWSLy8o_NJP6CMLzwZitCGH6-V3LQeRgvKLrIinR-REJMFRfHBp2xDXwzONomZ750-21-QY7SZlnyFvL8X-GDurCoAv1gl_XoaNGtdx1tk-rsxYHU4erD6MmKPjvhdtUmv4NSZ_JJzKSX4uRqpfB5SMNhabj0d6qU_tzPcs_8efQOEZcvM3Qz7BMJKvNGDKTNfFibTqT7S-DIYKmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTln_qnFS2aj52J785ipVoT3Fb09leDl_7-nAGSevXxBvtrrZUOcrbEQWNVBl14U0-Ba00igfwr-MZXWRW9hPFGYnc9rkWSJ-X-IeqI2ODPtg9JGzJ3fLpuMDEu_EZp3ZytDVkz9WRk1Zw5hlNhpOT-agFrbvc4gmKf9u2bZ4zYvYyHVVmwYle2JVc4YdhMGPfkFIaDmcy98KJR-3WGIb6Ok4X9eX-Nk9Gi6SM9-eGA3ozqXbYlXAGtKcc2XVE4j_HAl7K-TINXwgs23SgwxD32piJ6Tj29oxNcK-zrwNIVCpaYOpb1Hi5Us-ol1OuprCBqr9aSpI2g_8xBY2S473g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coayqIC8buk8BhjdfGUeobwWdh0aj3aqfqw-Oj-4cy5iTXFpRYl0W8HkkW52Ai1raEk3bihkhumBpGv-SyFeKHcuJxPNOKryBAj8XQ99dCaVpeqSemlxw3Sb0jIiq5mVGjw2fdghQoNc5gA8vOlLsVFlPJx9G5Lr_UG6FEzYSnKSQHmUVU7QIJkvtXZVk09gxHxHuZuMWs4H5CudWwAKOhcE2UbZYopuJMuj-yGHdaWqLuPtgc2IJ-7xTTX-WAo4pXCvI7PdT2rpaPF7oCHkhteaE3lJCqFdaCcFFqjIlChXHvueDCNo_sHXW4vxKIl2pabrzC2_-lIRCAI6az8NYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g35S6t21dCcHFDe7Zt67upLBAZpgo7d93F1hmaO5fsbm_WxP-2N5KeQtBnU8fhZFvzGdctiEjQPNN0O9RMK2IfyAu1VTpyMAzVLQr6AZOqMu9ow6IBXt8XJ6jNKLW4RBdykBqK0gU5UHSJp-GQNJ3ZtrRMValQm2iij7Nn9lamB3OF7g-10U8GomeoEYJ8ORpbsnTD5EGUj650ByjNCdjIuCWOFYU7uDPWMJzqEPu-sMtg4YI1tthhKcI0aW876-GDReFWLDrHDelQPKvlwKK10xvn8_D95hBphGHg8E9UVoIE_6RjKMIsGGcTg190O6D6xmvHfIQaBNebp8c2g1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAmZCfGXH0ZTA9vCVXRRCu_2efFGGLAJuTqrXufgEiMHVGr4DQtWGKl95UB0nczepcXXpNhOL3eYw0awh_T7N_tAm_HZFlqMkshu2ouVq3qgw5qiG8DEb-qO_Sflvw-wyx6c5sK77A4j3xFkLB6BSpbSsfydZt18BZAIOKf0lXqlAe_TDENK0aU_lEwSyEhyU4oxA5zrKsZFk8edIuHbEwdrvUsBpsl27h-bOXdzaSPFmh5wuXF5ot_LEupxEbfM-EeAelE8erLqKR6fBiwEAtuyz-xi3FVOCo1YK9hbhG9w1UCGtp_nxmOj4JfdclbB5yppRts5HpCoTZd9S7ubqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jajZ8deRpOiubEnByIg3nzl5xsGrf5tEiH7KK7QRULNWIU-YhrsD-b-ChqmQTzcRbPZBJGDlQcvtiP32KstB9fRVNZaKhYXYWD9sN9L3uSxCacBgiBOCGzQogBtexORUyS83IDkiGnyB6Gg2mMxCPMDBgJBOvgMfWjuU9slSGehBdiADvcfL2gjxBDTflJsX-J25JnvODe3fsX06t016ZKDy81BQIo9gBiN_ujTyvgHtQsT9xGFPppsCWuLi7ucfdOGS3FbI8ns_laneG5sEO1ywOpzwj2ePbBkkjFietdAoBrjP1jZ0nlRuMWggbQjbTRSQ6n9HzET51fGtM1dABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ENsnH0Cc3NTZmHtXUk4IuNa0jCEfbOYp12LfcHsBphB4uyxxVcOWyC-lMUut9FioGXWN3CvcrgfHM8Dl4P9S_taqbBin7sZYIQUw_7gMpqKjH4Ty_OwTOg_DKlBSTVO4mz07Mzvsc-5g_YPhQ2TD4cFAaV5uu19G97AtqQ1KEQ6evnEPmunAQVlw5jU1Z8TM-UzW2canYDFjRMFTqENQ5TXCOBwdNz-nnYtLzZ1jN-vTaDXheGZPTt7nJPoLE9vPweqRoHDdbBgNggpfZ5szdPEcKYakM0gL2qu5tWho-icdQ-7ZWmmBS-WYgS7XJjQFZLCpoOoC26ZpHc4-AISeYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ENsnH0Cc3NTZmHtXUk4IuNa0jCEfbOYp12LfcHsBphB4uyxxVcOWyC-lMUut9FioGXWN3CvcrgfHM8Dl4P9S_taqbBin7sZYIQUw_7gMpqKjH4Ty_OwTOg_DKlBSTVO4mz07Mzvsc-5g_YPhQ2TD4cFAaV5uu19G97AtqQ1KEQ6evnEPmunAQVlw5jU1Z8TM-UzW2canYDFjRMFTqENQ5TXCOBwdNz-nnYtLzZ1jN-vTaDXheGZPTt7nJPoLE9vPweqRoHDdbBgNggpfZ5szdPEcKYakM0gL2qu5tWho-icdQ-7ZWmmBS-WYgS7XJjQFZLCpoOoC26ZpHc4-AISeYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf-5CpZFnTlIH3grCiweHee4nFpTycgBvjD7nhBl8Q6EBofAhzC7kuoDB6evfCHZTKw1airpZyTV_bAK-NFE_j3h2BfswZOzE7PPNqOlbt2jw1cDYOOG6Df5JAitiP5FGXyS1dCK1cSBLNaSH_joYO0seQ7dFWRI4hHRdWkb9sMDGyZwmd8vmq8Ia8mvkoUf7S4FN7QO1GWCdu6_LOLCLfx_uP2AvaylBRYX-lw4COvb1AGv0w2ucoPz1vVDTL4DNwGAA5A0AIq3Xnr7NWz0CDrZK212TzpO9K78R4t-5vSiXWW6JwJ97KJqPVuqh14kEeogelPq2rFLoDwfyXSacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4jX-_xC7Vmfhf0b1NyyVBX6QooRiR3UVgKRGn9A7ug1MkIraLCPhJkRbsnOzaHBRjyBgaYvkGiQqWakxqhHrljWGuPlp3bgjbciJZUnsXEuv1PDOefe5xxj7nXmMV-JDKqljI2DJo8PCeLp00HpdJnzwrHjZgmHcc-GEFhKn7fyq-PywI9Yvad2IDcP4tMjInHSydHC4PkdiwCZUkje9EdBPks-aR9kP1mR13CDFizjYHmorgYdYHG_VxzmntFn-8xCzWkQ1X9If8oQjxyDvIXfIG6pApRhtanDEGoN7JzZ82DMIDO53S7X3yCRClg6QWHDDEfW07MKVmhX1tBkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixWsEJZ3JcHmIQRVkRrXbYWbcYIDTOUUj7R7dK23lRONMbH5yJ2qS_ZsmtScKZ2m6dkz5X9Dn9w1ZRvOvBkMrZt_Ys7-AQM7A-vLISXzMrkN9SXV1zSxx4bCpz7JqQaqKf-9sPxKKc9ZNdAPZcS8A2OPSfDA8upcVRpqOZcBiU36oYzxv7qS2o2ZJ9riDxl5ooEJrD6NlJuOpBOo5slArZcI6L6e7wEvSt3B2PFDb3lcbY7od6ou9tb6EBeTmj5DikeouvFyAr0OlmuQMRNZgRaNTsAOuScg4bsNz-JPfNlX85DtMNL30W1Az4KvRuN8lIipAShqv_hFrqiVeVDeCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wflr3c26Qrv1dpyM3g-KHpMMKrtvkbeyj64uMYStKs1qGo6KYXXI_SAATO19sKlw6jSiqRYerRuK_25x6tjpuDyZMXMqgdNCjfiluqe_r1kk1GEtMNb1m82tboS1kbK9PYj--qefVi6GLX8s4Fpq-bJxll4yU8oBSTu7ytwZSpB5MUCMDBkDiqJVRZskZIY5vC0vDYGF6U91uMdTH0j8oXNpZ1LB3sfg5qxnKVZb6J8PaK35SCNh1_wts9S6KBKZzxTcNAbDkCWQ8Rft1w-W3iPl3DwtlNoR85toavwiE_uINoNj8KoK3JcMMpPaIdhLYDpNE3TODczR43eE4G02sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mr2_gCXF52PGZMqjxzbbpACj2cjri01s2fJnr1tZ0YwV0XIMheAujbzJwyzxc2P15toAz9K2X7SCTHb4PTfOqB3E3rnuAIqIz9DNeZvE-a_xVUsCxSB5xFk6wenZl6OECtv6HleaIB9oboAJaShyU3NE7X7QDxmlpDKW3njZ31Jxfj8mbWa54US7Yv3_ue-uieB_PtUHkUC0SXBGJrgOonhZL0JXeMY2WIn9UrItDrl3Fv4MGX7g-N-udncJ6L__MW1nAOY1C5UdU9z_WHH1M8KAqOU2cesRp9ShCG3f-EAAqMgkrfXIfqFXsfCFgxfdqFpNBZfOJoq9eaHBSnyPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLVEuVNOO1cQZuMVO0VKdiqw6d2_w6DHjrlLQefTk2Bmdz__1B4EBk2OKxZBX6celq6AzbmORjqIhjU3qd0TjiJxSSIwDBgn2VnbCki13OQEJOlXIisJRdrRUYnINlzyw1_gaOR-08fsmbmnB8jlfZQqW_a1CR4AuNyHvdcnsERgW331TUPW8b9o60Sr5N3f76UGdffkKc23OYekUedr69q4mG_4A-HRra6aGvuGlZwSfab3nxErcmq_KH7HWY6X4ry3UiS5WuwAHuRg9bkHJupSurgVDuF5ixewxHuwecjjh0He1AM68d_7pIoBCmPWWp7FI45sdAeywVYKRS-i8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D32AYYnCYd-3BmQ2aVk7vi4IbYWz_-SBdRL4fCBaPpngLTys3DOpzPRhXsjUQU6Rhm5On2vhDOJ-X0fcZhvWPIqRDsCDk5Y1qkM9uvVLQabyyWgOHG7fJ3G6uV-vAiCr_Y8IkilyvAPpt4GEeCGXV5RHaO1qWIbZ0JX3YJ4Djrw5h-5DD0Zh0vODYHZZWItV5Jqo365nHLQJ6VL7KQ9EU0wpkBUwXGdWNWhfoLZ1N273jEJT3IUVwAdGJ1RW44JeCTbhsosGOMibKne82Ie45kdkx9tV8chVyYxKc2-npyPXyjgbIGRL5Y1k0XqsAfsN6R7b4LB3tU1XQEcK9VX3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-s2OQ-u3POXvNJ1q2VIzR50cp0QDdj6SCKQWRpiODBO_APLvyGVXMgLs0kS9tuXv8_So_wGkOWmQyB6-CljLXdnTStjgsqc3mpVsfv7juiGMf7E78xz6pa07mx_0Ji_f1KieY0mAMvWI1YZeu3P8__gOJzpgspIUUL93VvJf2Qz-wft_NBW9vrl7mu5I2UxTPSNt1oFau5jPRheCbGv-lqjdWjU7_9qSbJ6ptFEoZ1OnB1_XsfKH3VLU18YbsxFjO6Q63_r5WdYJnCSMYGTrtUMr2G8TBW09HhG22UDjvgDv_0ESjBN3nOdmyxeL7FMOG-6otN2cA2FZ4aUqUxl-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=nGcVeuVsnGdEdhHwwXtEMhIseHpZ32dVoZquZAJcOiRSQCGrWApKVJqr_uyKIrvssIyX4TR4ChhxdVE4oIv4WIRb7nzAr9BnloDS3SJsUHgPwA_cF6mSPLllvYvnbZEM2zdyugBn3nrrUj2V1G_3JnnKznh-bTWrPZq0fteRSTJfQ5qR1xy4lYGl5onmyadBtiZ276WXxFR3cGw5GnBL1_faJJMHotZNENjdkLu2NgjPMsRbwIuUq6ZNKycFv8sYEDE4kE4vUXkVW7OJhHlBakTrxV_JQi5Sqy5s7oEktWFkgL86kuKL3zgfV1oOarWgufK2ctdtEXwZSb5cpgZ9FIqufdqmRBhV5_zJvX0Vyoraslc2KzQInHInxb2MrwMvePZS3LEDF098XOrecbo4OTulSDita-8bjiQMtQH4dm5iV2TISu3Sh5xzB_Qy3_7jZ9a_3ThsB2oymlTmmmXlfop0y41D0B1YhFkfWaeFa6WU9MK8ngK4yT2uDTI5PZgxBII8uvQd73wyakke5XIhF5IFaHwMy75PWQxo_cyqaQjI17N7RlB7ZKhheX238PlPH63t5gdk037dcRVhuguhZO1j-QbLfg7tzp_ImrpWJvy6zouOk1qmad4E79z4u98qdA92gCvPXPnWkq4IUOS_wPqdgwzEuLul0mH42a7HnSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=nGcVeuVsnGdEdhHwwXtEMhIseHpZ32dVoZquZAJcOiRSQCGrWApKVJqr_uyKIrvssIyX4TR4ChhxdVE4oIv4WIRb7nzAr9BnloDS3SJsUHgPwA_cF6mSPLllvYvnbZEM2zdyugBn3nrrUj2V1G_3JnnKznh-bTWrPZq0fteRSTJfQ5qR1xy4lYGl5onmyadBtiZ276WXxFR3cGw5GnBL1_faJJMHotZNENjdkLu2NgjPMsRbwIuUq6ZNKycFv8sYEDE4kE4vUXkVW7OJhHlBakTrxV_JQi5Sqy5s7oEktWFkgL86kuKL3zgfV1oOarWgufK2ctdtEXwZSb5cpgZ9FIqufdqmRBhV5_zJvX0Vyoraslc2KzQInHInxb2MrwMvePZS3LEDF098XOrecbo4OTulSDita-8bjiQMtQH4dm5iV2TISu3Sh5xzB_Qy3_7jZ9a_3ThsB2oymlTmmmXlfop0y41D0B1YhFkfWaeFa6WU9MK8ngK4yT2uDTI5PZgxBII8uvQd73wyakke5XIhF5IFaHwMy75PWQxo_cyqaQjI17N7RlB7ZKhheX238PlPH63t5gdk037dcRVhuguhZO1j-QbLfg7tzp_ImrpWJvy6zouOk1qmad4E79z4u98qdA92gCvPXPnWkq4IUOS_wPqdgwzEuLul0mH42a7HnSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=qZvs1D638TXN1hq5D4VVr7466lkR9X5JlPGw_895rlbFS3eI-Z7HWiICMZowXcQq-kVe4ETZFT_tjp92SUfCGjOkuhQbtgkZnWD9-jJ9FQByis18fgnjsmlstuNmYBBsOXO9XpG4kcwmlQgl57oqrpS36VygWO2SKL-o6KTxHyVt2TbESrYu-jqcQR--gPtN5uNv8yvzVJfgCNaRFLovX4HZhe4-qoDpSRXNAbajm-A1f6gXOWvED-gLFS2chl8E3hFcd3vTv6cfq5aQMgtSECl_JjIjgnic8dz7CG2u6C8M8LAYqmM-DDr-hfertnyTjTl0OHWxc8llehTdKX_pyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=qZvs1D638TXN1hq5D4VVr7466lkR9X5JlPGw_895rlbFS3eI-Z7HWiICMZowXcQq-kVe4ETZFT_tjp92SUfCGjOkuhQbtgkZnWD9-jJ9FQByis18fgnjsmlstuNmYBBsOXO9XpG4kcwmlQgl57oqrpS36VygWO2SKL-o6KTxHyVt2TbESrYu-jqcQR--gPtN5uNv8yvzVJfgCNaRFLovX4HZhe4-qoDpSRXNAbajm-A1f6gXOWvED-gLFS2chl8E3hFcd3vTv6cfq5aQMgtSECl_JjIjgnic8dz7CG2u6C8M8LAYqmM-DDr-hfertnyTjTl0OHWxc8llehTdKX_pyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7p0brtfLgC88LljmYbL4CooI_DRJvHLwEze5NRIhXjnsVQNDo420p-drJUMOBuu-ZKowk7jLuwLYF36QEEam8xfJ91bdUjyaXp2ueWj0Pt0oapqsl3cPqG2H3kbOme_4L_OryWBiIGsLqrtOY4fY2w8Bww3G4GP0oJRWeJLdSTRHDjRw_FBYZaWkmri1fz66oaMQu6eD4-BSNepv-A54U0dXiQoFjhaPQEyr8JovwoCbOB81cC6MGORMrZv78UYz7tYChfqMVnRjUlDmN8hh00TNllpWnNiaq6J2g0_tapGNElPeK7hzBF1zYWuCt_RsIs6c4GT_FaXeFvkuF9aBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMAr7eWUz7Yk5BMZJc9KZ2vPajfgIsBt-WtJ7aAqp7bxxQA1MWGmroblUh81eyuTiwj-WYxLf3AMg_GYq4UlfvcRHjz1oyPS74a9d6q1j0V87uqV1mXp0HvqrlCr5d_VR1KDsRjqeQSl7oQwUxEAmEUVjF7iwtXtXuW33NFBsPgovI6G-DJ9GOcJ3vI-UxtfqbImVFGbG-UYgM3wvfEZtd5KFyFd1udhxFTAXZF7IVYyM4FuF-wX_pb5JVCQicuw2HykiZupEFnYepJf-Vts2GWIPq-YLajfQUdFzt__yRjMoEsxYcFGjpXXnD-_SZQ3muJ0rT8tE8XNN-qtU-S9JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flf81M8byjwC2GkS0pzGPlTmiZQL57oRNEZ028fRyswgWlHYflaj7LobcRGoYgYEkDNTePO4iHZyYYV9mMgX3G_84Y9BDaz-OtiIQ1RxRthZ_GkOoEa1JIz5uia7A-Nvdh8myfP-J-WzYdPjd6pYQBCHe-PoUDLKhflrlTxA1Hqs45KH_ubOTE3qZys0JE6i7QwRiE_7bde4kaBj_Y6mOhnZaAZ7VxpuXr_Jd1juXjFpfEecjHDeni3H3uy4X-u7RXdweSCS8PH0kKCH-zdfYroAbPFXQBf1oXOq92txW2sgQFNP4E1SKsW9mCjUC70yzbcGGIUWKiRVMzV7H2c9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df-Yt2AMQzSN8KA-9jHYVl1rkxXXZF9uG8Xrvf5_ojXFLjXBnFAtzhSToDSZ7UOlJWAcg0acXyJ6GM272r9FmZTOJtoVewDqbM37oGKCU4QBDlD6ktIDuXPMbGRhipa5Ti48mC1O03Wc_UnpeKZPjdut1LT9ruUFN6OF7V6zHdYVi8zybs57-tasquXIULuo3loL2_xUVVEgYX3GlJBZt03qofkkaZ713jEZYE6wNt__x8lObW-p49HSFkv9db-DO5tzePfam13uDodDhTSi1MyHLwk5sRP6VKX2o5LYJkkaPc6lksne6pFRjvYmsqseiXGK183EWQPKXOHL2Q8aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDwDlSQPmyMvfxmG6-1xqdTCDqMl3uDC_N6vKlofJVfdo8JAi21UcX8qou_WyHRqgi9y3k7YEdii3rVinkiJaIo-0Q1NhXPrJdlmB8Q34jlcj2zfuYZsYikOkFYMxkmeGpQ5PfhU3Eb0sNN3Pgr6oMWPJEGJLpz9IVDbRxTct65rVT9fn2q9ZqEvVeyXKceS74laiNZM2ceJqdqDQ1sQkQD9xlBQcLFcRTk2HuWg9TURsQNKBVRERWFLv4pMddBbJYVRH67aG2n0h-vDxNAw0vNVDLbM6cQ1hin5lRx1eBQso5pOu3fh_R1jSBoLk2asyhRHTahUfOGdZ2SEcyZTmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erh0iuubio9Ev6eOtdTD5cYPeemBmgQmexDpy8GEGBeFuUSOuVleOf4DQiOj6SKIzEq7sJENzjQAc0bhxfdT3fvgl19T_-dKkNjVVWxvCoEdA3qvSh-TR4OtVHU9BBt9_MSKtm4pge5abejVG5rpiCizLp5rtNc4JFnFbXD8Xtk4dZS3ODSqvqzlIkv5acwIO-0N6sFZ77y-gZcdEYEEz6huhXnS3gK-TRgPpMcFGDHvakG-syOY3EBr3PhDhtnJOjCll6eVqPft1za2lCx-VXOyJU6Au8X388OvLdXzKiDKKUUNp0WH1P0mBPTBoeoFU1ipTT1wbaGdtOtmZdbotA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLtz_wqCNWTKUsEA268Z7O0pusVYEOXwgEtQ-pv8RGQErBr8w47Bp1njTKeeh0YpzDIE_Tkc3JpC1GSsxQkC8_U8rIsBINo70BCC4pJpOJaldWjNY5-3Rx3NiluuXtzOXwwKJLYE5DNIBtbTn7q4T0KhFtRWhC-LmsosVMJ38JMXXXJ-nmFm5lCgffP2ZwQfnGR-5_BbACyI0iGIijOV1BPn2asqz3xu3b79SxI2PRGaUf8KQCmcuEAZzrKZHuqJXtdf8x1dXzahrF7gkxbG5wczReZc6Gb8bEyTBrHcbHpI1kboiBDtGuKtm-TAmK6Z9nHD5Np2I2rqC_So5wIHZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWLygIf27McpG3BM2WNfe6gRsHB_9YZq89cKytqs4garVQS75umhW5mO-XwEao_rRO8T7m_C62Jz3WxJFKZIn16gUCNIHewAaskFTIC_0mFwuInhmCN-Z5fa4GlnckWUpIo9onfgqlSGmWBE75JUOAc6dIuWyahjw2V4VIXPwf-6XkV5Pf9c8v2Wl_QDoPd1qtl42I-qYwl4yZr1prL2U8C218Aag7N2-Rp-OeW5ncwAbwoQ_PYia3PsbHiqGnxt-bVT5mUsTZ-F5eRNsP_SHqRxkQryz-68L8iRZg8RVspbPxEG_GVIHFm9-ta7O4sxfjVYcCESEVvlbX-T4IxbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVoHx2MzUXkCmLkvkBAngMpGp1MDQvGNBYP0EPsTb_3_DXZ_ecGVdwHuqZI2t0IBD8mWwd04iBTZsVZcQGKxm93-omEAluzw_7TYLtmcTEEbc-SdQdrD7_gdAsH5GdndYuJX8wXmy79Xntmzi8DoGcNQ0LAt0PFlv17D_EP252zYS_z5RCug8kUYCNu6m8fg_BmGdVpViBg-e8x6IAw3LeRduMASGg9Eb9DCNTEQrfdheP8A1HC01zO93KRdTcOdI58F-IDKwNx9bymJDFdywMY1KKNkGy52rSc76mZC6UgcJ6lXMIE9EkevDgsQxpxqboAYaH4eBQTN9hs97dchpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=uzSG3rGQDOKuWrC4hjpyyXdtWe9ManoXfEsv4BZN4DHywREeud7TAP9bxKxEdx7O0__hdYWvpfrZZhyhJayAfTKLF-5bY-LFfL_80j22TlUYAiiI28SxlnEjgP1WdR2J6Z3to9UPBvU5fe7igPAskyqBBTu_SJW21zNZKjzdZOAGpG9xYRg1TiAUUdulARwVAUXi42-bNnEypyG0qN5d-6HcS3f_4B0l6WSZYb917RKsTn50yMxRdeHsy9p0W1svQbeUyafCZ9wdQSsWcKkBvHZXU_oKdlMbgobXluhcZAQ_N8eKd8X5dK4rHnR7Uj38xOFOTNe2wUroiN5TYRnrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=uzSG3rGQDOKuWrC4hjpyyXdtWe9ManoXfEsv4BZN4DHywREeud7TAP9bxKxEdx7O0__hdYWvpfrZZhyhJayAfTKLF-5bY-LFfL_80j22TlUYAiiI28SxlnEjgP1WdR2J6Z3to9UPBvU5fe7igPAskyqBBTu_SJW21zNZKjzdZOAGpG9xYRg1TiAUUdulARwVAUXi42-bNnEypyG0qN5d-6HcS3f_4B0l6WSZYb917RKsTn50yMxRdeHsy9p0W1svQbeUyafCZ9wdQSsWcKkBvHZXU_oKdlMbgobXluhcZAQ_N8eKd8X5dK4rHnR7Uj38xOFOTNe2wUroiN5TYRnrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6kAKcYHbWO4JjuhGUMLljlCP3rUCTLUt4sGGKwG1WTeWS1_OFKjOMdcsBJCwreyPN3JbOxFU36K0FIp702VQag-hbPORVMBtqahS6KQfFV86peyGdorY-NCCFvprR93kYmYWbdIxFj67xUeZABG1Ma8sp9B4fBUp8Q2funtTavMBU7uovl0unEBX3a9FdcsRp8j0q1nT-bPBlkLe2swLDP1I41ASD7XNyzmJCyF4RhBQPYiSNK-pZig3ZwycXVY_pZSYXiMdOAww6YLJqDtkFpWK1rSD7ZwEgXiOUvyDHIk0TucDT5TtSaCWmIJNu1fM6Gu8cGNpy52VJ6OByiwcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Z05510Kjf8906XTC0TrsC6WlBx_XjO6BEH6dDuD7WLZeRPbx3sluHGiOcBD8x-A49XIKiGxDCSHvvQB8InEbUM-1VgLyvz2YBzcF3zYfhOYTFk0-y_oeCo6D6IML-bScHD57XS5GeqhVrNBBkdGt4nEgxjuJ_lhC7p5NY-WDJ7A4aQqKoK4eXXGBbNwvr1F8amgUCsoS71Q1hJlAvm2_dDq1isge_gKGIc22TQ1gLQ_SrsV7qw7_kPbI16HTUyEF695McuxFajx46O4xmVWg3ncGQ1VNZ17EGYZkkXXkk8LodkVtcPgT6Tfb2UqwZK09AWqZkuzLyJ_l8-y-IeB2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Z05510Kjf8906XTC0TrsC6WlBx_XjO6BEH6dDuD7WLZeRPbx3sluHGiOcBD8x-A49XIKiGxDCSHvvQB8InEbUM-1VgLyvz2YBzcF3zYfhOYTFk0-y_oeCo6D6IML-bScHD57XS5GeqhVrNBBkdGt4nEgxjuJ_lhC7p5NY-WDJ7A4aQqKoK4eXXGBbNwvr1F8amgUCsoS71Q1hJlAvm2_dDq1isge_gKGIc22TQ1gLQ_SrsV7qw7_kPbI16HTUyEF695McuxFajx46O4xmVWg3ncGQ1VNZ17EGYZkkXXkk8LodkVtcPgT6Tfb2UqwZK09AWqZkuzLyJ_l8-y-IeB2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=XUjayiAFcvF6b2dlgKazx7d1vd3zLkYFlnpZefDDBA-3FFO--6nphvLiffo48DuWC64qp2j161uTmShkCcQ1FFJRL_AFzS-1NY-GR4MU03fc4rbR0b50QQ3lPtQAAS6ZFmCcO0R4OVc1Y_jyGhwJxkUXNXRUg2RexJJYrEaFtrfPpZUXquQZOGFvnlfna6UIxLru1EsgiMwGmRyd8UJ6Q8g7zgzdQ9SsmS1dDE6_a5bP2aTn5O4GqRKSnshHHlCaoz_coVOuNXVMSqIMLTaB_XCr1BZq85fo7-Z8WTXIwUxYJ2H_VcZJcPVTd2Y_jLS4kMNcdAdcmVCArUe3SMMKtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=XUjayiAFcvF6b2dlgKazx7d1vd3zLkYFlnpZefDDBA-3FFO--6nphvLiffo48DuWC64qp2j161uTmShkCcQ1FFJRL_AFzS-1NY-GR4MU03fc4rbR0b50QQ3lPtQAAS6ZFmCcO0R4OVc1Y_jyGhwJxkUXNXRUg2RexJJYrEaFtrfPpZUXquQZOGFvnlfna6UIxLru1EsgiMwGmRyd8UJ6Q8g7zgzdQ9SsmS1dDE6_a5bP2aTn5O4GqRKSnshHHlCaoz_coVOuNXVMSqIMLTaB_XCr1BZq85fo7-Z8WTXIwUxYJ2H_VcZJcPVTd2Y_jLS4kMNcdAdcmVCArUe3SMMKtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar904nzWgj4Muk3xBE6RfRnvlNdw4C_1f0kkqKNfhMNERhqgqQSzNxBz58BfNuPYioZHeUyel_5sycY2wD_adOXbSiXp62ffx74oYh0Omiqy2mEwEUidMBuJt3hoVpg1pNPeF90YXgHPU-RIBI0AtfiSWRSYjG7cuIq1pi0fwYHGs7nLSTMc8I-8tQJEC3FbOqVJRhQdU_dNI4W-yv_SgIvmy-BocNXcTjRbTJm67mt5Ku8UgR_yJS_DvBRx4OH6nR1Bzdw1Ri3qjXSAflIEaLcVx4zLBIZLVxCuiY77msCXfTZylbEfj0-6_sa-Nuq8Fq3BL9BLNxdPIEBce1ft4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=rX5QdUTw6EDkhySZ6USlgNuEV1ApGHQAKPuXC4j4ovHLnb70g-6HN5vd3BWHIP7fW1EUBrjYPoSBF3YaDUF9lg7ksq3fM_twm5L_XV-zLhcSC8Jv_MAI2DazjK_f2eUT5hPEwE6jNdwXi_YJ6tG-e7lsm77VYgLXHd6ALyCb29xzix6xZs38obw3lVvcuADCUKi2GYkLcRVrGq9NiFcDKHPpBxAf6q8arUYuY-jbR_FXQF75UARhZSZzCGxh70HW6gx4DjTIC4_XFK_i-9RFvumK0vJhTH3XR2izku01KsMyj9RSyXE46GwsCJvRjhd_PMJmLSQkE8cJm3CDV27Rwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=rX5QdUTw6EDkhySZ6USlgNuEV1ApGHQAKPuXC4j4ovHLnb70g-6HN5vd3BWHIP7fW1EUBrjYPoSBF3YaDUF9lg7ksq3fM_twm5L_XV-zLhcSC8Jv_MAI2DazjK_f2eUT5hPEwE6jNdwXi_YJ6tG-e7lsm77VYgLXHd6ALyCb29xzix6xZs38obw3lVvcuADCUKi2GYkLcRVrGq9NiFcDKHPpBxAf6q8arUYuY-jbR_FXQF75UARhZSZzCGxh70HW6gx4DjTIC4_XFK_i-9RFvumK0vJhTH3XR2izku01KsMyj9RSyXE46GwsCJvRjhd_PMJmLSQkE8cJm3CDV27Rwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvUd1uQIG0EF2BeRUowHoSDMBNyOSETayVfkVD6Gu3XtSDTzENKdNxhXAYZyPpuuaOV1-8fr-jiA3lfVnVYgEHnWUf9-6LZyWaKEQIquZ2JRh29Szw8DBa5LeKZQ1lGs_i9_eVmDUBPCXRRJ5UNkOKsVALd27zJ5WQRWYlkYeKjnlh_SvoAQgqnSQyMZuZoWCG6mhdW-M0KoYqnpEwX49q9kqPuzkjf4ZO48BqYV5wNQTI6vi-dt88uzxwUomOC7_GdwQZSy6AYZGD2HCM5n6mklp7W-xUrunB-Ss46nZCmUtNS1iqZsyfq7H5tMwzxDqaONLbRPQzT0kExlT6EG8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_TRfdQv7j8QcpF8BJzzaH53MpTIW9oOQv3aW30U8Mi1uz9zvB5LLGwG0vK3_lrXxfmfSbz5bDYVlaUExBOapfVznuidsXksiOyYVsU1imiL2GsisS0_0IIWGss-GCyFyuSerQ1JLeC8edUjyaYh8IucPD6v73TJBTVQWDzKT6nXADkNeK7rNmThaojJYaEp1hzyf3-_32bMfGc93ZMDc3IWUG2EvuLO42mk0Jwjx-XD6tx-kytMnIV4NQ1kCkgvwIyLW-O55pmiIAOoIoo5ovAuw4JiIdXWpTNEb_72ly48t4qFHxPv_oD6vepl_RUV-pKzUAGt-NoUBDDtwWBjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dt8RNGwPS40xo1jKMKEau4mUkwuQ3vP4Zp416FpbGr61fPX60urbFbp71cQAPQy8qPRzAit4KQ1VdUcU6AEfqcEIiVF-t8wYejn0XMmg8s_36gt9P04Kw6g5kR4ahO4abrC6dbmR79Iq3iGk21YlvLjVzybYeIjkORvD4MwL6wLJJ65iAfty1jaTSwwOtpooJwil7aF-73oMgFGatsv26nSk1SOzBC5SbY4l3O5KRsG79434UClIfVj9LkoiXOedzEjG5jUAzJ6mcqp2NkJZmmqraYQJnpf4Xjew7uDTvNdgGLNxFs8VWy0a4LJ2DnD_H_MfvoZHhQkE1Qo816SJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9rSWj6W-JvpwT0U9L30iX-aCGIxoJdGYa2OJHDffruMS0jANV3MXJ4YByCRDFszDmxj5X1cjKVMF6-96gbV9mhwJaB1WcXAAdEMMwhoKKBuMj8eZyTY9L4ctvCj7UQMDBrR1_P9RiWwtuB3QP-gnRPtAYZ4wj0LSbSUsS9b1m4KhVrxav5H97R7CfmzpJEBMg-R5fBn3A7b58xwPBwUflncWCb5Ck0jp0uswiu0ifu-3z4Z5eKX6-pbotUbbwMOymrPh_Xtlc1fbFgBcl-GXMDxJoFECQmUXjgAZFophDDrv-AKeFpZSK8lcwmmdtIfb0GOs0OAvuoLyCB9vbFNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQlIt36_5OQd8VbwmKxlRfUo92LAyZi22Qtt6oCD28JUYGHDm6xa3zJHfDiJkSCXQbiienv09xMgKs0m6Sjv_Mj4K5cvfoOahXIBCbWalXgZKdHUZJnJIjgbe-U3WvLcVM3GSDXdgeu-E0irJV93FTkKNqBKR1cW2Wk5se7Yj2KyhxUnHePq0E3QfbctwownMqP8rOJdKECIbCqgGlhXJ4EORcpfBO3oT1pdYtndClhz98FxPTLMEI1zylj9MIgX5om2V_u6ZpXRoQ414G6PsvitZtbS4YLM-UrakxqI1UMufngKZ0VV7NByRXifBbEWh-NqaWHkn_63LWOWZtHcJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vW9FRPB5fS7P8wCR5ZFi1aPhjkGuEKBeDZ8FVMpQjrKDSPFJdFTuG2f7kYS1TNRGbJc_sjj2qc0IjU9zm3umQ0JeAE6rnzbK1W_fU0XYkAYM_s__nsuJgzKa0mXOZc_Mo6oOnZLZtmFkoZtySBN_nFcMGLidgmLko7AEREZGJybNOBfqnwfRbgO5o2SkIbKj1k8NHcvaXNEIIEB3QTxZ3S8dV-mzcQ2tmlefJHYqrHCUhL_gd7gdxcN2Njh9qdfXO2ndCsxbAUlLZpeXaDpVSRVSIqEtlH-fJQgbqKz1JCpBFreDoF4H_w-_QSJWgNY2P1VuG-5P39-qcqP0YlzW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKZtt38oEWnx7H0jz2r8qZ2zgH6eHYVVETp8r7nJQxQopZc3SNEe3ZyETbI9COlgpnXb6yaN3y7qkuRpPggISw5HbNefId4IJMgYbTNRqZqoWcgPe0ukw2Hf5HFHXaeEy7XUB3D3rscToIUVB0qSkP9D80_huo1dKkIR35cCCzTwg0hPg7gTdMcYbRRawmtv0h0LTUcyBKDHGEwwg-f1TD9U6OjjkSLtQrpmOa7N3ZFDWOovH8eE0ij0thZ4T8hfeFeW4Awl-ZbTqIIm6ObmfTFcKf0pXpCLFTI5iOBjsDurNpqa-1t4_x7BhKKWv7G_oH8kD_5aysSfA5P4ro9xuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VimpmACwl6uU-WiI_Ol9Jw5xXeipYzRSADtBg6i4cARGzAhLCHV9raozsR57tqIDhIq6OoQ_MO6tirPie9SZZCDxMgyvTrv9f_O3VEwBRFTVRgDkLHZbMXkEgIhY11-dbFJy1ddCC3EImxr5sactAPQjHy2imr-5-YivwU6-WPEb1kOL-VmfCFwtJIAfsz7ETJpeq0_XmlNnwNkYgLAkVKTacVTDbncOQXAQHMcPwaF1Vftq2vyQ89ChLfDXIznt2gaVvOpcJBzHadGbEVBx0OfDYerUmJwQ-o3H55nrk3zTmp5kc3GPSgjLdoRXRWPLUBUGAbV7_weaaz3_ieNSPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=HoNc2029q1cBg9fCMJrZ9OcFUuvTZPidEf3EiM0mYe5Zk12Ujs3DDQ-DGw4VVZ4Gpc3aqpS_j60o7fE49A3fn1x6FV7JPnrhI51I4vPXhXs5DZ0oOfWMMFqEAoiiH8o3QmNsvrkzP03pd0ur2gyVg5D5nEydvFRL_stbM75njFBb0tVQZuMZEM5TXq8sZZd7qH8AgoSXLE1q-GzvXyZDY9_sV-FVg1p0pjVoa7LSOo-R5Jz-JfWhSoBqaAHAYVc8skWkn37yVY_fIok51fQO3Nihfd37IRnTBlpCvT3vpaNMsYhZcsHE-LOu7oJjD3kIAriGvKWcYf2HuR11jSNqLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=HoNc2029q1cBg9fCMJrZ9OcFUuvTZPidEf3EiM0mYe5Zk12Ujs3DDQ-DGw4VVZ4Gpc3aqpS_j60o7fE49A3fn1x6FV7JPnrhI51I4vPXhXs5DZ0oOfWMMFqEAoiiH8o3QmNsvrkzP03pd0ur2gyVg5D5nEydvFRL_stbM75njFBb0tVQZuMZEM5TXq8sZZd7qH8AgoSXLE1q-GzvXyZDY9_sV-FVg1p0pjVoa7LSOo-R5Jz-JfWhSoBqaAHAYVc8skWkn37yVY_fIok51fQO3Nihfd37IRnTBlpCvT3vpaNMsYhZcsHE-LOu7oJjD3kIAriGvKWcYf2HuR11jSNqLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=ILl4FoDY_TrBM0a66cQoy6OhFwik8hW4zahaHMwn7FIRY7HiLqIDgvx0-b8g7957SxmNz8sk2pUrnH_V8qAJniCA05mWHd0aqTKHxwOa0cqMwWj8LSphKAi4sM4Byj1CswknZkXj9zWp0HCJ1CXvrQE5-OR3V2xkp0N6xlTItXUesVnoe2G7m0B2-DWPiYXtSOt7OKwLcqhtflDi9kdiS3dyGzW4im-_NmtYpYTuMYZ4Xd6mKXscrNSFSWFhVxHBBhMxPVx40GsHm5TUMkXnusuTrli7oetqKnXI0WZW7XL-GzAoA0hbCVkTYwcPIz8hRHF8aGs5dlBH-KKyrRxC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=ILl4FoDY_TrBM0a66cQoy6OhFwik8hW4zahaHMwn7FIRY7HiLqIDgvx0-b8g7957SxmNz8sk2pUrnH_V8qAJniCA05mWHd0aqTKHxwOa0cqMwWj8LSphKAi4sM4Byj1CswknZkXj9zWp0HCJ1CXvrQE5-OR3V2xkp0N6xlTItXUesVnoe2G7m0B2-DWPiYXtSOt7OKwLcqhtflDi9kdiS3dyGzW4im-_NmtYpYTuMYZ4Xd6mKXscrNSFSWFhVxHBBhMxPVx40GsHm5TUMkXnusuTrli7oetqKnXI0WZW7XL-GzAoA0hbCVkTYwcPIz8hRHF8aGs5dlBH-KKyrRxC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=o8dOpPpIVwa2_3OKXex1oONo4s7-pNWcOWY2KzjNHPj3-QhX883nQePfQZO1aB7rlZja5LGnlRIiyfJ0zRogUbT9CpzCQ_nh7ug6iIvm42LEUAPG34Fu9k6lzP7Ns7YwBc0JCzmIqtPdTtPhD20V6_EgqBOiTn9iBNBlyfGud009jMLuTCItwtHCk6-AcZvRQVpcJpEjjDe8RedoUFmY02pfitImqPkQpAM0jkNQHO078FwJG8Ys4vPK0dvupTGbawDQOYz7pxgZ0857xNf3aqe4ANYJkYg2lIWjtEb6gQ1xSnhR4zTpKGA7HoWNyBTYZttDPw2eYT34tRJmeQUEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=o8dOpPpIVwa2_3OKXex1oONo4s7-pNWcOWY2KzjNHPj3-QhX883nQePfQZO1aB7rlZja5LGnlRIiyfJ0zRogUbT9CpzCQ_nh7ug6iIvm42LEUAPG34Fu9k6lzP7Ns7YwBc0JCzmIqtPdTtPhD20V6_EgqBOiTn9iBNBlyfGud009jMLuTCItwtHCk6-AcZvRQVpcJpEjjDe8RedoUFmY02pfitImqPkQpAM0jkNQHO078FwJG8Ys4vPK0dvupTGbawDQOYz7pxgZ0857xNf3aqe4ANYJkYg2lIWjtEb6gQ1xSnhR4zTpKGA7HoWNyBTYZttDPw2eYT34tRJmeQUEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz538DvB6aVirg2F3B30OnI84JZER2PsaPxWjte0PocaeTuvHr9uCyae14lEj3oODhh2XN0QMSKG0JM-aIv16ffqQq3EtICqABJDOyFGBEjEBQqKD20QXouDhOOhBhNgjkWLmpm3dWDNidDkBqqhsXLbr59x24aF_NLI_Q4buXFQ19pHdoqz5twMyGdG9207EXb-01yBrtCkXlAx_a40t1-icC83VdwIVBm349Tg1fX4Q36vtAAD8DwgumuLdsPv3g6MxgbOkK1d3PB_KbS38PBum-ygWV_mEBKtyEX2OyCk398opiqDnmTy94S2ta9jI8jodcZPWkRvxiHxtA7OIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPTPbfI4LuqF0Sq62ybKK39lr8hWdc6eyU1QCUTgRTk3EcaLSV8r9ervOhRoKDiJHhwTAMZE8Jve6ny05yMxVl5R5xbkxlW3YTdxZjGdwWWRtmena8HxLyRfpdSM_ISalB9iXbk8LgnYEV6krDjwfCCOl9CpjpK7BgeLwqQXU_oxUX5rsQPMGhpVZmnz1fOs12amKxAcZQYlRN8u2JQCrOfUmhqBVSPUgdH_72m_DmI8UQ5lMiLNWgzyHtHTnwctSR3jQwqx2o0PyTr_oXKFZfX6XbbSNGqq9x4kM77J5MSkyhZDoa8vTtPQGzIj1Uo3q47qNvmfu54p94eKnjZeOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5geXukaD0z13K3w5gf0NTTXER7ctacJuj4exhSFxHjs-36RZ2SE3dCJ_ab2TV9qRHNxjXDEnwf7yW5m8vgm3ctw9Hm81ExaHV4joVwf3xr-F8BeKYJstssrHaSqd0X3kCT-ck3S9sBb-mA8gbFAi6fRhoNU_6BB1tyhhkGcCpz5aHWSyCSgcl6Vr0uDFqRQxSNHpv6UQOWdAp0J_wGfoK7URYRFnYqWyW9u-cBGcFUv160w9qOmqmT-5z2a1TFDJwleg5s0oTQywhm05uSlALHEBIe2K6TxsSkYq2_M84VoPIFfxyzvnfxJ8z8Vlm_cdQzOTm3GatyB9SZxnTMAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZsb2sdR06JCsrNdbyE-2RoIKeQniFb2qxN4OxI2eKhOBLpBeYYUJo-Z9UC_CVlUEnb-reEvmsKxqgxNe2pRMzjQULbTgMVML01WrozOIN7LG3TPRim06o3xzZuysllD0_f0ghoghYY_QZfcVq6HjLYoLm0ZQm3xWTVxqTxJp_MUjycU-NqHUkBLMGjIwrqDfI73mXvvX3NHOQYf-fo4gv73EllCtyjnJG-W_W1zNjxAK8zp8XXrRzK4EVlZWnH_QeMVxCxr9vny0IYBqxvdiVrA8Rg7gh6dTp4_rYL-oyW6E63rG1gqBuX0zkJ3s9Sx1O0C49_afN-oA-wWTcq1rw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=mQZg0PtIIlOl8MXPLBMqyVB4ZOnJcFMMNtZVleqs9ppdzNvV8dtI3o-a2LJl9L4vCNHZ8Qa4UdgqMnQCoMqTDksIXaJOtdE7rODw2zVrxGzDbCsfjArCXqolP-QOiDlme6T0z2rBlnU2khh4idlHqa8SlCW69wuTyjvcaGtRwtnG15KeKHs6UbLOfVa9gxksUbGtPv0f1if5c-A5Y9owue_4aSpNlaPOAUNvu1jfRgnyNHTl0DEPSLHKUz8Tg4o7yuAonMtnADH8wj-l1gWDWermIxJVziRdnJBYuyRHXqPaBmn8GZR5S6o6a1Aio5Y-qEdZ2UfDxorUiZH5sRAnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=mQZg0PtIIlOl8MXPLBMqyVB4ZOnJcFMMNtZVleqs9ppdzNvV8dtI3o-a2LJl9L4vCNHZ8Qa4UdgqMnQCoMqTDksIXaJOtdE7rODw2zVrxGzDbCsfjArCXqolP-QOiDlme6T0z2rBlnU2khh4idlHqa8SlCW69wuTyjvcaGtRwtnG15KeKHs6UbLOfVa9gxksUbGtPv0f1if5c-A5Y9owue_4aSpNlaPOAUNvu1jfRgnyNHTl0DEPSLHKUz8Tg4o7yuAonMtnADH8wj-l1gWDWermIxJVziRdnJBYuyRHXqPaBmn8GZR5S6o6a1Aio5Y-qEdZ2UfDxorUiZH5sRAnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=v8UgUvS3LSQVSs-0sKVAJTfl6PYvTjQRBrfnxqZfSuGZ7rO4aoB5QW1GqF3QUB5DdkVP_5DiG5QQ5vt1QQi6z9omHco8aQnP3H-Eo5GgHnio4Ky0oOruZij7z3JDLjnmGxXIl4GsCVuBY44d2o7Kc5etbGnqRDp4ToIJdogo1U08XuXwZlWMahq3rObFzchgI7ZSWZOSOevfc9Rjv9559-R04010S709drsL5Y9z2wtDLJrHXIDeUKZM16rHOLFr_-cY8qnx3rl_boqNn3XB-EUOaM4rdEWxsGiELwB81plQLDaYWYkXyhsLcS-rD1O0Y8-JpNjtKTRPRWg0jHFkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=v8UgUvS3LSQVSs-0sKVAJTfl6PYvTjQRBrfnxqZfSuGZ7rO4aoB5QW1GqF3QUB5DdkVP_5DiG5QQ5vt1QQi6z9omHco8aQnP3H-Eo5GgHnio4Ky0oOruZij7z3JDLjnmGxXIl4GsCVuBY44d2o7Kc5etbGnqRDp4ToIJdogo1U08XuXwZlWMahq3rObFzchgI7ZSWZOSOevfc9Rjv9559-R04010S709drsL5Y9z2wtDLJrHXIDeUKZM16rHOLFr_-cY8qnx3rl_boqNn3XB-EUOaM4rdEWxsGiELwB81plQLDaYWYkXyhsLcS-rD1O0Y8-JpNjtKTRPRWg0jHFkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGIEnI-_leVqAsfDB7rwCgGOvLih_jcOVqC_X-Vlys9F0P8OABAyu1tKc8r31XujkGikKVZHDX0cy3AKvFPh5LPl_6mdr1Xc3ju6YenhfbMybh4Uw47RpFXaWXxgE23V_p4Ez4e-1PW-xg4cdY1befd2P1X1iZR27DRxll5TbyHZFEEyZ04E_YH6uSSWRDnjm2-ChRM_O3cmkLL6W5s2H3l_et1PXiDwGypxt9cnHXWEHV7e_NCglfyd0wLAKqgWfraPQIaF3bwOFXgNwB_sUynfIa0KCbn5pU4B8gNsYZDgxorGUGQpX56tCifVisFbPKX6kRj5ZN5_LsE-VMnOHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2DBFTNTRiJ0DkfUQqAV1X8c17ZmoYyORTtP0kXQ5oNWIO836dQVrSZA0EQS5ODvnRcXZ2TrL6cnKkZ-nMFB8p-1ZnOTO-mywLxwTObsGisLiw272FqLFhSuYs-_nAzIA_SUXTgYmeUfyYcXXCoeQpgunROS_WUqQX_9qMyVbbCBQg_sYKR-onIEjpWihcpdy5LekajqTVmnNzAVVfZU_gxap-jrulVqKroVH0dCG3kqN-H3x7lUkIx46b_czBEDaz-Rr-hZ_4WuKORxBEGA9PhMNXYMMZsUBux4-3GVKAnVclkRPgvL3lJsCEtwtyoHpC_hL451OzBH_Vt8u3t3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMDrgB86G2JHyUUTa7Sub0Jqc0eVOdo0w5OnvxX4RRSth6htJMnyvlTGTEpiXF4ABDAdKafNvjA-hH5T_NPH-o05978ruZZrsICXi97JpjBifk7919gJ4k_TxDZZjf14mUHoq__9wFz-qrHt6-BUbQmLfte1H51hpF2PpG9YZpb5IzGw4-C_ePnQg-lQJ0jyAEJxguj3zXCZfeQwSbO9EQpAzGXk9xWhJ1PqMc2izOwL2iE4VJ1b0rYWGRHPg5cQ0cawk9d8hnqlDwzHmKp6WujibSQBzch9JOuXp5oYneOEWnARvNBTutzJv7m1_i7SS7r3nh0sC2acEHvieACvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV0s33AHE9EhBc9umPvVaP8wCuVaeDlWXpKWS0Z6YJ4_gzWhK2I_6OMtVsUCTvZ3FOisSUWRLWNiaXrJIUAzPWE8iaMwyvHIGKOaIe-gQGAdjCArd9p9GyOElAGq9Pi1ulf18v3ThfVqDK5X9vmttJApcWi1RHzFeK3g4cUh0qmmtzZhR4mDmj_fYIDJvz-EW8wlkhMutrinLbHtFOFxfa9VPgMEuotVSKcjc79GWuf77vopsA6OhwaT63ddWsIZZ2hZPiHAEhBFEY7Ix_fWzSe1YeSLQzkKDVldRTaOgnxoEDPs4sdx7qthotPvyXFVGaCZU9CPTfHX46Vq6DSXyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWWO4GMSj2JTKBr-nx4WGXpjo9SxXPmR0uNOsp4ZLYtQ7SC23JmJMQlxbJSGYPLhSln2CMAh4GpRB0SsB_rrDxtaeERRWuf1XNI1PdFUPMSZXaya3Tbcg_OrzsIJSaOz5ByxwNZpYG-1Ff562MBC7pSpCBgF_FlhOqePW8BNC7OlOCfwv1LA9OURze_6iTGVSrgoWKKYosgDUkW59KN_QRXNvC5HKiInwVJQNow3tfBTOjjCre_VFpH5Ve1JSrbDgXFD4jonYDnMndSDM8SB7rkZXISDpzPKZtjb67WZd6KwXI5KYt3UEa8nT-DWHXTXdGNESyD6c9PiK_LIqL0DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Litcufl_rATJkFAXrK9pJN6crb3Ep2JGk9aFY3tQja-9PS7xFBvdRpBauVk20N9Y2d3ML0BhLq2HiOvb2sTc0KxX7CF46dp88feZhxvmdW5NOykZ0rfVEMMqmYOrV81c7meHJC96xSOkN4Ob5yZIjRuo7xY3cUXrGLADCeq0UMTZ7GbNf6JYappU27J-VQcHAzcdvXmIkfnfYOI5m2bM6JHX99E0rr92xetPqa3MIkqdEuxCADwDWjO7uV8dM9DM8wdpdFquDnxpCj_-0AG-ZiRKzOKKwdBJtieQpgqOygMSlYg8kh441juXR4JuTF7mzTX2CmwxFhMLF3MvREOunQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnOcWrgDMuM5jYDqe8IJ1tSPgCS-rRp1xEGDVP-LhPEqCuMeZQY0yqxrjFABm4Rqr31jvRi-WhH9C9QY4-eU-6p_Ud26Ei7WCK0moRRPHa6LOq4eYBoJDJF-EgdJBZemJuopd-is8A2RTOuU2tBfL1XdxTB1dCCxFQH5iwwh6mCQB2_TOSickq1EHSJUzeoiPbuLSIY61G2_1OGMfHHTkvPcVzNEtbwxUIxHcp_z3pvV1uwLsAt4_Sdo55ZMcClHrDI4rRsLIS127yhlx6IRuprr0SBh7_zeV9kGvfHwG6KNoQ0iA09D9ww0jPKaSw8SOJkzq8ICxMIUpAYZ_gmtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrWeYHIjjr2MIRck9g-95R1Z52S_toqMqCw4k9ZkeK2nX_gqbekSLzi3bzXXBnDWKf-AWux0sSuKnIiFdzAUKwK_UJFKpkoNYAxPwrpOtEMM5hBwq6MYXp4ahXuKAP-j85Ro48WzWzw8pW5HS9dVZo3DvYTac6SvG5bZcpwwhYRDeJODT9C-LL0PNt0HlWx1jSLTjG1jXK6PS8znR_vKZaIiIQlprTAeFKRJl_JKqpXF3cCTmwRSO50MDU8pRPGhijKSKkFPsGAT5mza0dCCTK3iQeYNyIzU50AdEVp0SzGACYUM68ePuknxQZqz6m8XMzFNj89Frhe4nHe1gtfdPw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hhmgJhGcYo9iDP5w8OS6By4xb8ukh9Ti3YMKzaCQY07VK7U9b59tpwyKLmAwOyG_mGcdPO5elzBuiTnLyNQFAlN9H_GsvlNKTBNsiwpRZzGbq5PsvOZEyx8lA_pN3qqKVjn7wv0du9XWbYp6htLibVnjmnznOBAY6iZJTbvras9joEDmEdaOCxerzJl83xi8W7Z2CduQ2RiSxg8fEhmNCDlNGX94VXDNLhNw4PPhnkA259_162hI8vs5VEP0mp-jC3gpTco57X7XasdAWfORJUfIY0FF7mMeVXZ5dU3m6UbnJyA-lV4NapGKgmf_k2Jkjj0y9qwzqU_Jkw3a_tPHIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=hhmgJhGcYo9iDP5w8OS6By4xb8ukh9Ti3YMKzaCQY07VK7U9b59tpwyKLmAwOyG_mGcdPO5elzBuiTnLyNQFAlN9H_GsvlNKTBNsiwpRZzGbq5PsvOZEyx8lA_pN3qqKVjn7wv0du9XWbYp6htLibVnjmnznOBAY6iZJTbvras9joEDmEdaOCxerzJl83xi8W7Z2CduQ2RiSxg8fEhmNCDlNGX94VXDNLhNw4PPhnkA259_162hI8vs5VEP0mp-jC3gpTco57X7XasdAWfORJUfIY0FF7mMeVXZ5dU3m6UbnJyA-lV4NapGKgmf_k2Jkjj0y9qwzqU_Jkw3a_tPHIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=I74d-zlXQm-ZRWkKLYu9LzZa7_sqt8_SuFHXBMIGIWM7Wfneov-pPcuHHoo8MdKJ4kO5-wgIy7DJasuWrhAM4e-7nVfjKtJBQfBKbPyVhmBGOklCG5sazX03bCYvy7MHi3CjC9dphDF_KyG5f9U0Av1n4ZWfs3zElOZqtwKIEWOAF-M_VLqTUrVt_LrbWf-P5HjSF7VL7YrVnOdUqLwLCm-2mTxqe3V2bdEgzTGFn-GujYmQXWWH5qGYqAg2WBvm45As3pbH5ev9lbuezDpCOG0uZKqaeCyHaxCgjJMXpyrO6gKy4gF0yxgYHBgGjTeYEAEOruvSuYZOT8aD-vVXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=I74d-zlXQm-ZRWkKLYu9LzZa7_sqt8_SuFHXBMIGIWM7Wfneov-pPcuHHoo8MdKJ4kO5-wgIy7DJasuWrhAM4e-7nVfjKtJBQfBKbPyVhmBGOklCG5sazX03bCYvy7MHi3CjC9dphDF_KyG5f9U0Av1n4ZWfs3zElOZqtwKIEWOAF-M_VLqTUrVt_LrbWf-P5HjSF7VL7YrVnOdUqLwLCm-2mTxqe3V2bdEgzTGFn-GujYmQXWWH5qGYqAg2WBvm45As3pbH5ev9lbuezDpCOG0uZKqaeCyHaxCgjJMXpyrO6gKy4gF0yxgYHBgGjTeYEAEOruvSuYZOT8aD-vVXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrvyCD31OVDkizwdVLUOMZ6G4FXpBj6uprLq5HCSdfQlpdH7qKRoUBC74d-i8N15ryPPiIg9TKKpk1ODmCUJBE5FmIi68ANvUIxzNhW6oFxAZsN-QFmOkE7zErIT0wyHKJwp8--uf1MYGxxZiowGRZCOL1AKjk1lAPFLkVITd5pdOKLEW7kY81l0CcZIfhd7f8xXHE1Zp-curT-ONvMHsjwAkdfLaUXEyZr3IeAuzbh1HPx3wMdPBVl6BFJKyAcmGDvZUmOeWpvnAUjaaJoKTk5sHe2xHzcxGJ9vVZ_NGD54AaN-2VY6bGzpQFClfD9EQ2i-X9dk1aqI8-jLRNefAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0KUWQ-QqbqL6VA2yogV9yhFtqRMxn5FKTWsF7wJc5fcdyHXLyVdG-miqLJEU-FSG4p1_0nxQ69nQysI4xaVDFLxdBxUGQ_NdOvUJZ8SHlHjZ-68g7T6uV_cLT5N17LOxghd28cuqvszUPoDHfC34qcTs7FFnDdc4Pgda6kRq322Cvmk21ze2Bl9cNKCmM9au6zAr4ZvbHIWyoxWksdE-aa8m4PHnJaRWVyup46RcshDZtNRootC2OFZeZDNSlUghT-BHhCVHOt_92MVLe-UI7XDuWFB9rEkGNs3elb4iH20KYciC0sywgek3aGpcP22shGb7CzxB1LbCiF4fhI8tA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=aGq2Om3ShopH8ehOA6nPenvJdCuhBYH2qxxf9dxqCoZkvmwK7lHRbhwhK2aVmMTySXgRiGOUgp2UjJ2xvUli-9_9k4NESdDfI9Nt9Nm8MZH6vJsn0kLGii0RWmRrFDA3tVq_VALmBPsvM2LA8Yaie2_cMjDZU4bsfMhDArJ0y0po4ApiLpYd8cCQ8e-3E9lBMpY2_lJRSdat6DKpJmBw_KYSYZbeF5TiqwFujPwhvyf7iJKDZekpPlJ5RqG-8Fd4PCwJMVpx6Yc8Db1wizHMtjr5OueKbNRuWnqr9W3ZTX4hcoeNu2Sin8CXPBtpQi8dOUvwbWRpig8SuAO_e9bvMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=aGq2Om3ShopH8ehOA6nPenvJdCuhBYH2qxxf9dxqCoZkvmwK7lHRbhwhK2aVmMTySXgRiGOUgp2UjJ2xvUli-9_9k4NESdDfI9Nt9Nm8MZH6vJsn0kLGii0RWmRrFDA3tVq_VALmBPsvM2LA8Yaie2_cMjDZU4bsfMhDArJ0y0po4ApiLpYd8cCQ8e-3E9lBMpY2_lJRSdat6DKpJmBw_KYSYZbeF5TiqwFujPwhvyf7iJKDZekpPlJ5RqG-8Fd4PCwJMVpx6Yc8Db1wizHMtjr5OueKbNRuWnqr9W3ZTX4hcoeNu2Sin8CXPBtpQi8dOUvwbWRpig8SuAO_e9bvMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9gG6WdtMl-UTAYt7n7pMk927mlFZe1d3jjQ17gMN4nVtzh4h2fG-ZmqFvenW_-pk-ruzoiEPiWKwbIWFtBX-KYEnFWAc1jl6Ys7ifPME08Ayi-Qd-xUomLBwQix6iqllefz0G3vDjpMyOxoeNNpnCtn8N8MtS48cVBK8LaRGkxTx3yW4oSUAMV4exLp5sLHLjbwVYCdZtXL89svtTWatkCR_sPfj6oei5CpA1OGB3bFYKRurFC9OJJPUmkVAAhpFOVs1uWVTbcyS2Wwz0GMPPqoMwX5dkw8CKd3htVJF_zjqWGzb5sdOJ6QKW19gDE8a1mHBSCcaZf9xKwzhuH9zQ.jpg" alt="photo" loading="lazy"/></div>
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
