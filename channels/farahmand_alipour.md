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
<img src="https://cdn4.telesco.pe/file/G1yguFHtk8vNXSAuAdBmBbfuaN7jTXYnxN1lwvANXL-S5CNCbPqvZOTisKlYgZ393raMwPFicou7xXIsj7CvFI6mDm2hhTAoUZ1A6uC_5IDl1cO-OfMkvKbkXo8Ztm8ei9WZEx39iAbfeVcNDXfKZGEVAk_SwfMSrz207YXNxbo7h91B3xAvxds7owsYdg2xU1cpFUIYyqVSmRrXyvAbKcmuA3d_CsgnoeS0LA5003FDDCevjRR3zu_t4wWWYTnkPpNV1oGaqjF1VI2qDv3XBDtHxJ3UeJLOX8ztiWaN06fK97qruLTjSty2Ku0Q3HISLEyNbh7Y_xD-9q6vJ11b5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOd_FPmjDaVIglxjgZJOkpfDlQ1-h-T35qIZ159v-JWrrN8OKnKKbFHcIfuVQnvAs9ksVI-VgYvdfLv43Dr3vM-PZosCBzyZ5pzfpLjpfUiNA6xl5tukbM11wbElyFlJ8B0oTEqspul1ggtq5loaQwl0o3ZYk9isg0GMQCwKSbl8ToEUAQYKgY6rGP7Wq3vG40-hV03NnWfBJ0oQ6H9JKuqi03Bl63RrOPiBhkxgmc2_O_CAIXOCvFAw6t9eOospGvXx679NV--D5enrhkDhXektvc5s3onaraEo3esvESH3Dc_dL6fWTzpvS1gA794A8m33YD9bwrTWtw2L4NJxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5Eq-ZaeZa0mxFd0lWgsoUdVSYsuEM0k1Lp32ZaymghYzd_K4hUybIvUImVYechFImJnnPe53b4Zd9gym1JHMP5cEfng9R8-5inXFtqV6DVxKnxSIJ2JRlzZdu78HZ0YhUe9k725Jq3sXu-FVUSI-qQh3yRk94yay5o0vUYz6pnpJJdkwwb0LvQT6m-TOvUUa-W8xHT5zwwxRK9wourPj83I7F0r55JIqcyNd_MCdCrcCrxeOYAquFIDSIt56jLPpfbKDdVMJcFqIPYA1vfMVg2Jo1L74tX-qT4bvesEGumulrJxbgldYm8yvv09AfkLUUC8foiMCULIuQyJ9Jukgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UP1YoqD2zKaB-QpK4bTi7QxsKhXXGeqp8dAgaXziNRA03PitlGENqrq8b1vtuhkzrw_MS1pow8h3yX0OTF6qmg5dJZ0s2PytWocru0eRdpS6rUSbOzbIDN26qasE3gb0BdOGwphOMgYv2JrP9usCAZYvsXOpxD_8CP0gvYkCARExkUKJ63BFo6G-2GxbNHvl1ifmu0F37a2-SLnZd2oNCVgnyX_ZaOETzg_bD9kngqIbNEC5_aGWg_XOdAOAZcgT36FK8c6Txkrxq2GhnjpAMyEqhYOqLXk5p0MiJ1jQyMWUdbPt8qPAr1chF9E5FRSkHDmS90L6x1owkcl00TJNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=flRtxG1s9HAXxDuj2K4LrnR1R7-rsdWgF89p3OQI3rUjJPuwt9U1R3tuxagjiAF5Mxf8IGIjDf6PUp1USkWmLxlIQ9MEAPqfv9fu3Bn-X_XrmFmr5okb-GL-EVmyOAta7yXbQFHdmKzY2qr8tsx3IN5z-yixvsjV9SWpc7kMrDvbeOkEVwCYtgD7wvihFvS-G6L8ePOJGrG3xjNXXr3W-F3AORWT4vIDhxR7swb6qqjNabRAmQHV8ycqDTyB5CKA1H_2y75nntIwClVkxBsDpJArAKp7urk3TZ4iw8_Q8Ybj7SxLQqDCGOs8ECySR8WFu-P-Cv6m8OUe5xHegBI6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=tlk04u6E0qUjzRXzsg6cSdOtQfXe0lPzO_Ulz9hRD04wU6wcvh39UG1IYANJMLo5qdXPjVhHJKia9ZsUR-wcBPxV6KxSb7zxjSoem6J_405LaenjHthxjKyTkf6jXIfTCUJEpNajaaqQfsYUrXt78y6OC_Yf2wgnNs9LW6631JJqPUC-HEqvpZgRcB7A2FiqsVCh9rI1QU9p_PPk9hHA_TVUCH5M-mLcvSo9gl_PzMF3V1WgeumsHUilio4wm8mmPjXbC0UV5f1TiusSCIDh9QBeQO3wkHf_fobzy9TKSP9-Oec_0sb9guW0YA_i7r2SXfoXlgV_qLjzdWJhqPEEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzRzwCHxKZ5jZrFJ6f18Knb21jB3rYbHe6nHZBG7whxAWWZW8u_Bh43UVBLBZqnfa61ocxEyG4X5yvDPkzutMGhgrHGDMIrOaaVsX0GDtiVmKxwKU9Irc9qq7P_HesGQ6OrHbF9rJ9kRlCgxBGhZmjdeH2ZXxE1RUGqXQqKZo7QAX4tWk0Ia3dANJQyWcaNacGm6oLUo8JH8r6sCSLkvIhxz-L22ghOVwgwXAY-cSHWOcMPb3SHd0Dz0SYRhxkNuGsLNAVHliyc6wvuzGgal1Qcon4eEf5S3tWCWJkmg3xV7MQW9kUsH0nvZr1T1l27eF3nljoYaT5pGqNkZJF9CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEYplLELLwQq-E9ukrEhqDtGDS9X24CEXFLsSGTMMfmGplnWjLRGAJ4sCS0zh8aNYtiew0XM75Bnq29otbpKr9kWcX8UUuT8OHCxkvC8dhD-J4yfB6DNpXPK6dZgEEoSsj7DmG_cjEzBoIfX7vPDNGys75ALXow9kY61a22TS1sKHTyIg7RvxF96yR_d-MnqbmuySQmi-8B00jx4AelmQOhQ5jjybBLAYRdAdqUaFXsY_twHEmdBKDqS-35X34pbkEl1yJJjVzfe9L_d82s7u5X-vcsNMfQq2WkmvlFNWAErK3KQ56jbtayo7XN513Z7aC2jkh4LMGHjAYS8FAZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=TqgwaY3PwE2CahovA3FMnEr6NUSI6RiR3VIpkGPqf4C4jyYTwrz17xKqtZHaoCireW_k96fWVxSJJ7tp3lMnRauH5zJskdV0UZQYxqFjN8F-dtxmS45KHFC17Vje9CCfZpLpSu0mmTa9avLnhsV7pItNe5lNpEc1tLOnGQlrFfbFUfe3VMB7NCIm35tPEBkaP1hy_PVZVJgVtbaZMD86vdLa04w9xLIRYSZrwMoOYmWGa5t5bGfSY2Ag5Msy_nnp1jhb7EyJ2hHs0GyNRDJYBKwU073e34-Cci3ab_MRXQL5Ed7DvudnUzKQ5EtGt--ylxw21sdJuwmXPBCoO7wLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=TqgwaY3PwE2CahovA3FMnEr6NUSI6RiR3VIpkGPqf4C4jyYTwrz17xKqtZHaoCireW_k96fWVxSJJ7tp3lMnRauH5zJskdV0UZQYxqFjN8F-dtxmS45KHFC17Vje9CCfZpLpSu0mmTa9avLnhsV7pItNe5lNpEc1tLOnGQlrFfbFUfe3VMB7NCIm35tPEBkaP1hy_PVZVJgVtbaZMD86vdLa04w9xLIRYSZrwMoOYmWGa5t5bGfSY2Ag5Msy_nnp1jhb7EyJ2hHs0GyNRDJYBKwU073e34-Cci3ab_MRXQL5Ed7DvudnUzKQ5EtGt--ylxw21sdJuwmXPBCoO7wLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=g-6jilEnzR6sJPLBVVevH5VaauEG6Twr7Ss-0lASQMkJM_BLeGcvwjCzEwJUGyvMyq7p0BE1KFOQaO4xJx37WsjndfOzrFlSngfLilM17cPy0GE9CXr1d7YfRlWPxhbNFY_qK6YBEghBwHzH8HM2baoTlFdHlz58LpYxzr8b7o-rbInWKIwlBtQS8jCHkhwVMK_12SPBV_0BRd_pqKEqJmR4g0J2hS8SyD7H0Swfrm8cN71s2OmDwfmVSNHPoZK8sFHK0MYCtbP4sAPYIhVynwRlGFGiRkhU8HPGI3o3h3r4kPMeTi2OcBYOAgYwGCBz-08vZKDPiAgE9DTU51-04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=g-6jilEnzR6sJPLBVVevH5VaauEG6Twr7Ss-0lASQMkJM_BLeGcvwjCzEwJUGyvMyq7p0BE1KFOQaO4xJx37WsjndfOzrFlSngfLilM17cPy0GE9CXr1d7YfRlWPxhbNFY_qK6YBEghBwHzH8HM2baoTlFdHlz58LpYxzr8b7o-rbInWKIwlBtQS8jCHkhwVMK_12SPBV_0BRd_pqKEqJmR4g0J2hS8SyD7H0Swfrm8cN71s2OmDwfmVSNHPoZK8sFHK0MYCtbP4sAPYIhVynwRlGFGiRkhU8HPGI3o3h3r4kPMeTi2OcBYOAgYwGCBz-08vZKDPiAgE9DTU51-04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=KOyTqdMmqjM1NTjTCVvQZBW_p9tahIvVSw1DYfFrlToD1dLwExx3P9poHGih0iu3N99FN00gxl1sCmYgtIidWluMEosNpyKulXmOrm2KUhP68DM8_5V6Ao26pgmbNzZu7zLaabPAPS-Ta2yfPQmrrN6YwrGct9a8HCahX_YeTY7J8F4tTgzeulTGRwPj7khEciHVtjc6JMuZbY5A2HtGcRVKOskQwPBX38HOdsykhwMFSRZwvJQdFHCxX3Kj0PljtN3iHEU1e_E83OwApo6Iujej7SxNKRxWDQ4Gp4YxwR8kcgLWexi4NEvY45cNJ7sOsSr2gtN6-w--LAKZ81HLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=KOyTqdMmqjM1NTjTCVvQZBW_p9tahIvVSw1DYfFrlToD1dLwExx3P9poHGih0iu3N99FN00gxl1sCmYgtIidWluMEosNpyKulXmOrm2KUhP68DM8_5V6Ao26pgmbNzZu7zLaabPAPS-Ta2yfPQmrrN6YwrGct9a8HCahX_YeTY7J8F4tTgzeulTGRwPj7khEciHVtjc6JMuZbY5A2HtGcRVKOskQwPBX38HOdsykhwMFSRZwvJQdFHCxX3Kj0PljtN3iHEU1e_E83OwApo6Iujej7SxNKRxWDQ4Gp4YxwR8kcgLWexi4NEvY45cNJ7sOsSr2gtN6-w--LAKZ81HLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7MDrS_8Xtyu_CrSp3yHT7CP-aCx_tcaJSkTs_OR56sf24mWp_AByJip4y9NLsuB7VPGZ4zY3rDJZlXtLen78suERurtaosnTgVnRVTHcCPxr48o2TWpDwsvtpp-O2HI8v1XvWZXLt5jP1WO9nEss7nOUhPbzOi519gGi004Ov45QTEKA-d4VL-DAJbpDMrRiqHrX-UBVl_265gIWKPB-rpO6yABVr8hsefZVwOX0VVVyB9o9NvjRv3hvOgcKfaoOZJVh2F0TgU8qcl4u36VntBJN15UWMoPd-fl9lCnGaKVQr3vRPP-R_punsO780uV-ZksdJeuZnSsAIJNFgb6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdDkWZkW6NDfD8pjtfXOQ4VL8wpmT6Ny812LOuFxRtZCFciMUlYucy7g7goZoPtVDRsk4DA6r6IX6lO-z4ccR5JAXuud_VGNbMSLnjj0qgaA9YL4sIyDTbQ4fXiJCCzTqrBVOLVoSEftqTn72kHPJcF1ELbHM4oRrwOUo4hxjUaz2y5tdplF8dSb-CV7dhe3_gYx0ORHSlG4j_P0yyYA4RA6DmKfFnPW9cbdNMkYHZAiBPEw1a2vgD71lgqGpg1n4g0buwD21bCHJ1njU6vQ1fPFujozeRyfM_NnPKuWMHQK3i7QwxVBBky_XOEmX6ozp1rCuTO51ejyvoSPgtKR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-NK5VPdn3af5tbKwCztrjoKIGszQzE3W45LljMhJTCITX139hyHjiZq7AvvyTWn52SzU2yqsIgcQAux3bFGKkz3LZtgWLdTn-AlgNLy7ceNvHJmSyH0aI7c264m9CSV4C8J3p33LSDAKJ8DsGSVKvmFxb5S5RH-0TqMmSQcNSO8bB4SPHYM5FHcY1GtTkc1XaT5TsUQ95ShidoA6JjAZFZ1KnCpJc0OCX0wlw-BnAgj92RdDzZpT9J1EzGcWyjxK7hiCyfnVCvc-7LTKuGDI3Zym3u6hVZL-JfWMroekBAxCPO_BYYysiIzCqNeQJpaQYjnlQt6NTgvjIrsHKzwgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDz-IKaJsqb5okbW1OUnqzRJyV3kp3YnG-QIEI0_nYwe_9ooAMwEcU0NCzh0ZKyvizd_jXb9FKwZgQvX7f5k_xbaZGQd3SR217FA3IeBWc1W-6r4sIo2-iPAQQX7sr1Rj4ebPIPJldIiGkSoofHx5wN5OzgLr-aeacyYRl73chDJTBmkZul4_HTG3Uoow6QuIk34OWZjZgGyE9qK5v2y2CRHt9ujNPITJcreQhkSg4Yj6e-sNp3YdCTCcq1PJXP6E1fEcppaEEBAfewCPVKGdRVE16w810umgdh5HyElmkJm5_0NnV6qLHpSZol4v4R3RKcOvwYhn-aSNwKY2DyDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQZDwMF-nPdVYpY-7QlrNXNydDIi69PwLZjsZDhF4VJT4T94yAqa3QsqGSYWuF2q1UGru4uuEPxaaSmCL14ln4hLoJaOrxHQLjkpvfRp9vqCElhHgrQQmxPpoFxAIFKnVNOvQPU7KnFtdsMXYzwQk8H891-hsw4jhoOVs8GEj-0VBVOTpg5DbNJtOQ4ngIualYNU8GvXm1AootrINpqHCMveZuG3rg2h-F2iEh3z29yS_h7aadVfSCyU2TnpoyX1ty8DacwP2XDVMLyXjKwSdAxZbjN6GnuaKUvkzomfuqW05wvcMGM_tTyH2Bg2tAS7rDFs5PIBhYfuS0_XLKqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV_zg3eSdGSu8UfgsN3xHK1VddBABB6PylYY58fUSG--79EWPpecS7rx9eSD-QX6IgD9EDHNE9IZqsaME9q7qSD4U_-Ry17_vjpnG0YMoQIFg5R7KQmx983RTNDPvESN3tMYmq1jQfbFCgJYPl_sHy6MgRJHXHOzWMldbOaxFMlTmMuyDc6Wq3T5A0NN5pQ0TUuw_C18-735RZkiMLEsHIGZz5Zk2BfBzWgaod3D1pnwFE72H6w-c8NZdplwTPfUUSQw2SZLYn68WIQlIqBrQPcK4Q4z1SQgTiF2Fb9uPEV79J4U3xPBxalBq5S63JUGb9P4M9oFZ0AaM96MZrQ4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON3bVQ8AtYI82PVQ4ZdnUTd6OylG_3jbF3EYMtrwt14sX4FCgyaPdYfdZOXmBFGta55Y8GPNCK4ky-n6EU9kJfm2_E5vQIRwaNszGBBI_T_DQGv2b5QBb320I8D7xoPCN5RKe5vfECY8fVACX9-tvkHalnsTz4WsQGyhHeWNbGqpzRmSbESLIbnUAMN9T5MX8NV7fklflduR3Wfw65Pxy5nWrjVr0mu1KHiqcb318km1EQXh_hdCH5GZIbBpU4blWv-5zvvivW9AxbldnXrZIZpkWGT9crmDh43EmFZ8_FyiD5AMJ9ZDf38-OYAWmLuBZbTp4KMcawazCXBwxzygDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=P24p16xspHg6KT0R4pbmvy2hPWxd69_E-pUS-gcVPgYIrydSAAI_Sc-k9Rkdm5Fwa9CAee_o_OHErJxHbLtrvhKKIrgfr8xfoKCNy7pnn1bF4jHPEN7lGuCu3NrG3GMVbxu27vAXxaAZwcaFvIIlrJbwpBc1UKId7MPl8XGKfn2nXh7e9QhZi9wbmTvyGcklCSge1l9675UDoush4MdRnkgB6w_ykR5uvBg20oqyyvhyOQm-EoDyuND96vrTJDvUtIwDCH_TvOK9FrH8fr5hr4eazHASQ9N9A031Z9XeOD9nVkreF185FtPgsFDUhJNBavJgnictH6pGO6pkJUY85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=P24p16xspHg6KT0R4pbmvy2hPWxd69_E-pUS-gcVPgYIrydSAAI_Sc-k9Rkdm5Fwa9CAee_o_OHErJxHbLtrvhKKIrgfr8xfoKCNy7pnn1bF4jHPEN7lGuCu3NrG3GMVbxu27vAXxaAZwcaFvIIlrJbwpBc1UKId7MPl8XGKfn2nXh7e9QhZi9wbmTvyGcklCSge1l9675UDoush4MdRnkgB6w_ykR5uvBg20oqyyvhyOQm-EoDyuND96vrTJDvUtIwDCH_TvOK9FrH8fr5hr4eazHASQ9N9A031Z9XeOD9nVkreF185FtPgsFDUhJNBavJgnictH6pGO6pkJUY85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJjhTOELClfLkCUAk_2ekVhtkVl2Y07Pdva2TSNVwfaKoAtRuaHQHJTge03eNWCdzlK9_ixP57L_JwrYSRbIiEpq83TO2aDbCmWCLrrHGwy9oFRjzUI0VMUAq7htx783wPM2bWndOtUJE-LdqpTrjA3L0v7ToMqy1T8StCfVcNqVoRTWCwodPYD5YscKlyT9PXv97XF3bvViKWIsyObI95DcsxNB4jJyUc_4y5YHtG1BjX1NdSCG2EryX5iuXCZIf9WS6Ea2NCGN2ef3FHeSGf5uhXlpBg5duI-L4WpAy_UC437nWZYFmpGPWQkttnQH-zfPppl8Vk_Zcdwi7c49CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQTnTy7RcbFWT_aruRc7D3gNx1NB5hoEIdtX7wpdvo4nNMXNvzpKxOL_7aaCSYUznWZLD3022WjUsLLQr15xF8erCVb9qyXL8GTzUbgrVnPsMu4nPzu_qYZPZFM068QyNSSKRJFEhH_1TupjmKVj9DQZ5IOKhQR77RcKBKXCG_rBFK7LbJXht-VkZxp-EAZTWk7qDIe5nCqiQT3AjP3b8p4WZikOWmivmvTLgdZtpPsCB09AXAfJjdwS8fONvqPT8iFetvmklygKslnss9Iu6oNzjCx0ddG0Il8XRPA8GzduqvqO_bCe4xpayJcFJoMdAqlttiHc4aSVG3_JnLXYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KP9JJRITWekF6pDUj0UhxBkEE_KtfbuMofwroCo_mVJGmRzekaqRI6O-kBKSQ8Vk1fYpMg1JJhMeZF6Uc1c1Rppcw-nSAw1vyXMDDhju2DwJrGFGi5I6hpbYq1-Sjtq9KQu9cWyZElxkEgukAb8gbIVKWWryi_ub7c8iEaY1j2rqsb3ZliPJoko8Di0kbF7hxpow8-frNe09o6gxJQ4REJ9Crw0pCKxQpByVvW4rLhueIHHPNDLB2CXP20tMChnExafGen8NIKWC1_ArwQI_nMv3FuWhRvYDzR-7DT6ROFKwuy6fDtWlArM7E16hlMt2PptTQECaR8mgeXeG2ekfvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCHuMTZJXcolbcqorbNFjkoeGw9Bsmq7IvYlV1L4gy2vRlk5Q78zstFmxoKG0W6qn0NPgNQYJ447vGcHb2iMXhRufbzJ9G_OBnmH3zXe9BMJYhaPMAyAsv7TkS9hMH0zlXCbBxbriR3LPl4hLOcOSBsgO-qVCLM0E6yf5EN981_QukojHMsksSIndnxVIE1QAs2das-s1QbmJ43-HutN7EDlUQazO7-u7Dh4vHQh2dqQ7_lmUrGfsoQ4H5jT8WRDSxR7P-caFko1z1GVjrhjeq-iuzPjDiH4DGTELFzoeaAOyZ6CAZXICD-0xTyhQ1J1bMCsn-HV_5RzdxTyhAOFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cg5RFwpXnOLw7N7RfS8MWiivNyQI07FHRhBsBGpvQ2Ai8EMQYs0OBEqMSOHtHHvHGsErfqWMHIO_8Q_PxypZYu4jt5RwecAo3TodIsE3oytoLZjdDTqrbV_1Bzw4LKrbAFUzS3u6qXy1c7_cIvg_uVouvUmOn8qtAfMPM8bAKq8sBPcEY8YcW3Asij1Uu3djwA1U8Z_vjKjhHU9Lj27W4o286gLKs6tuezA-TN1Zd6pkgKlVTq1SylmrtHHpkOw8xJK8RMV6i5uvNvKCJ9uRdFccoiCCMqg8VlgfNuq_-D-cEdgTSifIFjL71EEsUA93jhZPkQ9wHXlkcOGnqWmEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Afsm648SWva2M1na1CJsb8F0fEnBvzpQqlQFgHkb4kVO6i3Ntv0YHJnpMnDg8jRxEV53qx7Uu8UB9hc03PBU2xkdClrUPf9tQH6rJk7ouOsa-VMmpARAmick7KIx3zm1m3SphCNu95awmIXjgWfzg0HdFIIgDt6Mu21dKYjHkRXfXCOSijLyya-jENksHeDp68RAqZIPtxnZZXHVKPPo4MYnpADK-H5Gm5VBKXGRGYrjGInmSjgLXb0zj8_DKFQbbo22svQNEs4JRLWbwlOvCr5dgingdQXrK5QOaHcy9fn9_Jva3xw0if4e40vcthS7WmwOuOBQcr0hF7wIQbxw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKeMyPBP0veme5BZaFl6JhVST8K36mz8lAe1AHHD56pDVEdoLyMzCrQqoNApMt7jjZKAgdbG45RY8m-7414uGkFnf5Mz6AB957xDFo4x1tU8Xv_bM5F7RPdY_rlqMx8nBiu5LUw1brQ8Kt3u7x_1M9dRC4N74b4jQuYrnxoy_v26PLO89z7t-GA-AY5q2ahHGPYGYonW5ZNZlf46eBFIokXmVRf-HOCm6uz0Pahg9Vl2n5jUnJfn-kBnyV3tBbTmH2hhAcLJZSL-aohrKFOlXUuLKk_STnp72Y1Ucy5lwwPd_yrysI1KCRUsJctR_PPyvVvclevEa-aBI2YUttLZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8AM_48F1e8r3Z34wNKbeLmDDAZopT2He5VkAkBzVTk9GwRzBzj6mtomHQJB4qCFVTgX1XeBoSVQyV13pYDDJHmXRMAs6vw7z3Wk0HzhUp15lVcD7IBaHXBzcNOrEMEodKU4u9GVz1WieqqJ25o5AU00udCsXuxoGn8Zlayl3cp3wrwgXR57pGLuDXRTyc92AyFUJg8vD-fIYoleICts5_-7HzEKBPYUVMcqYXH2QA3aduYxv35vbRv_qWkTBtaVgRUsmqbWxkisJgWGjLDq4VufN3UiMxlqjayapsL_eOQtSnYHC_j9vESkUpcJUcu_6nuD2EOzySrZLvkO1VTWwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=FoRoJjDDFNk-Mxfp_tpfpfvjR7Lpyt5OyE18dWfFol6kuRVaQMyuFA9DwwbgsKGJypTHvuKgdnaJAaXAXryfAqk4-pifNYJ01n77rUN2MEgUoIgbnwcUz-CUub0OAoqS7h4HZ0GH7eGEbzNpBijdrCq3k7EdznZnT36nMAXhAaInwF5uGytEwBdUk-ZoW7wpIegsFRuOXuIcLxDkQtz1CpW69vgOcPhk5TMyoNLIc1b5BIMv29ojQh7LUpTkb1BD68QvewNV-GNFUWptKxzSfywj4KBfBijAsO9mx0yCyAt1rLsW0zLJatE7expR4txY92bq_KZVpMXTU2J0Tm2D6ZnfahwW-bnv25HaMI_zJqnupZqpw5DNRqg4vWkGXkjMw1inZPTkCF3hdarZRi_TDs1SsH2hiKvMNc9zIRbNbyhL_ZlrEBu54mH0roYW6we06hFKDUdfz-_5gkUxR4GTh_ACjjPkAFMP_OTkj-XfCJjb47-pxwOwySFq5azG1xU60tmbA1EwlZO_8X2IZ9De3dYman-ExzyAlme2W94l14r6jbtlmewJMhpjDlSmTwcxwGnpJYSyy02nU7MJtPW_9NQWfOebGZ9X_ySzyHDN-o9k-893sirNMXSC07aQhj7_5ziskP7RwBBGB4Cj1yAo2j3aTQxK31lkVZ-TQt0avFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=FoRoJjDDFNk-Mxfp_tpfpfvjR7Lpyt5OyE18dWfFol6kuRVaQMyuFA9DwwbgsKGJypTHvuKgdnaJAaXAXryfAqk4-pifNYJ01n77rUN2MEgUoIgbnwcUz-CUub0OAoqS7h4HZ0GH7eGEbzNpBijdrCq3k7EdznZnT36nMAXhAaInwF5uGytEwBdUk-ZoW7wpIegsFRuOXuIcLxDkQtz1CpW69vgOcPhk5TMyoNLIc1b5BIMv29ojQh7LUpTkb1BD68QvewNV-GNFUWptKxzSfywj4KBfBijAsO9mx0yCyAt1rLsW0zLJatE7expR4txY92bq_KZVpMXTU2J0Tm2D6ZnfahwW-bnv25HaMI_zJqnupZqpw5DNRqg4vWkGXkjMw1inZPTkCF3hdarZRi_TDs1SsH2hiKvMNc9zIRbNbyhL_ZlrEBu54mH0roYW6we06hFKDUdfz-_5gkUxR4GTh_ACjjPkAFMP_OTkj-XfCJjb47-pxwOwySFq5azG1xU60tmbA1EwlZO_8X2IZ9De3dYman-ExzyAlme2W94l14r6jbtlmewJMhpjDlSmTwcxwGnpJYSyy02nU7MJtPW_9NQWfOebGZ9X_ySzyHDN-o9k-893sirNMXSC07aQhj7_5ziskP7RwBBGB4Cj1yAo2j3aTQxK31lkVZ-TQt0avFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=omlq8HdB07F4wdpUwG41hT6cmog3MegIRrNFfHBmkKcp8sxWhOSfIKknmv8U7UALLfxhcxQRn-AF27OAKmXuvqPKTjPLdbo3RsaJiESMdUbgYN_dswuI5_SFv_PXhuRHExKGJaCejyearP4KeWbPxoDgS8eiWtRluzIMoFCWcgxcKnzS9FAg-qh_QQcesdKiyTANVpGywsPM0MSHmnlOqHm0-HbiJzJQfwv99rzooIrK_cCkbB1tZZndthT36oqVlUtOf1vhacP-O6TZbIhFJIhbpbq-Ia7n8v4KTMvjah_cC4ToqRIAudm8odt8tzRg6g7EvogE7ZnuJTcHNUADQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=omlq8HdB07F4wdpUwG41hT6cmog3MegIRrNFfHBmkKcp8sxWhOSfIKknmv8U7UALLfxhcxQRn-AF27OAKmXuvqPKTjPLdbo3RsaJiESMdUbgYN_dswuI5_SFv_PXhuRHExKGJaCejyearP4KeWbPxoDgS8eiWtRluzIMoFCWcgxcKnzS9FAg-qh_QQcesdKiyTANVpGywsPM0MSHmnlOqHm0-HbiJzJQfwv99rzooIrK_cCkbB1tZZndthT36oqVlUtOf1vhacP-O6TZbIhFJIhbpbq-Ia7n8v4KTMvjah_cC4ToqRIAudm8odt8tzRg6g7EvogE7ZnuJTcHNUADQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh18cfhBzZgnGSA0N1nsy9cTCCmupPS8Off0PnqxQoeEXnZrjZSHMA8YEq5AfPmBS18scKh9lkhRthAxiijCWUnWCxj6LwSBjtB2WWI2mmPKGSocoApUbZ8hhAd-RlYm8QoY6KwdqQIxegA5ePSaMmDX5S_esd1CK7yzFkBkrcNYYspWgsXpVpUwyyLrxr-fa6cV9-DiuhplGT4YUT_KhFN0m7RWsmDacS6MKEl1E8xqtskz9FB_8LlWSPoQh585HlM4K5KlkDrqYmiMlLycH-O09aP3JMkDWuj-o7fuwWPlyGtZJLNgDecv9oY3lK6ReL20EhiPMyv8u7-JiruGBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNw4jhubazH3jLqesjc7wbgYng48L0j23L2C9g_AaqlOly8WtGprzIPZTO0gVLXoh_Ff-5Zbs3zCl00yvUbmKPO67MkvORW8IwaE6vLnwuGNQZ3WwGKFSNuXiSbGMBbt37wxmfh1bo46FvKSx3yJdeE-YdfRMfSsrF_9oGdGSCJ10wGFGn8nywC3GMBmsHyXztwMzbMa9njrqM8G2kkUFF_mbvi8X065gLD8iidKTT8rsDaFUCBlJ8qN6M9U3jFGPUDr68E4-5EDDRxMfDzlTSvYvy978GrGNMKb77mxY_nuf9bjs9ze9mUR-Ho65pp6NzixgkE74X7qH35dmVHt_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7AG-W5GjPMy7IDpw7-PwcrIjHcRCigzlEDah3__Fl7sZHmnXT9yHwNYd0imjcOTo22oY5KwR2MIlMQdr6k_DM_OZ2vznFhCoqG7_P0-JH5kBhuAJrHsO3ywfKzThgp-HQvwZhQosxniG0IFDCfEsE4R4IhW3Ga6BRnT_t57kP-h5o3nzBxWWkcT5A8fDuydyUmZ_xdYhJ_2SSYoYGVzAOlbGI-2-EfeyzrYB9Qo96ve_BiTSrD5wG1AF5vrJCuD4zazCpw-PXFvem3sL7NrJFn3dlu7IV7f1jwECDcfa1cjXSLiAch5fDQVgA59DYKKLUJ9Q2A_6xLryn3j9vGKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtPy_Us1ZdKhfu-1oR2FtyyTS5moO9Ck0So8urBJ2P2mcvcHncujqw9pPo7f71OHE8cicbYMWLhBZIi19GeZLv0pHouWHrOguAccrDHyYiWQjIbAXCkUl8skMv88JroytQ7Hq7aGWWOKCyWOncJO8CklJg_--lr3dnXYRvTE4fr5NZAkXXA4BuTKW2B9zXxTelRTjqj2rQfPTjcw0fCJHHLP_2fRj9IOfkl_5q3kS0UQn7GvfIZlBgl3cTBGzbdEhYkQDjDytcHbycdCWKu8jq02yQEJcSUDKiy8hUp7HUHglmJEVWNukX7Qcslfv_Dg-2em3kEhFkZ6FXq2tZ9ojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5KKE4qAlo0MKOLWAGHE872gNBgh4qrdGVMR5PO4KxuOGsmEe1j_Bm2sQTCFELkuiaugrdDEnvVAoyh8gdmtgwK-0MbsRuSkmoyDzTpCAucy-O1zJ2Fyq_MZaZNi8BtWnS-BJ4pwZX4gFOtc8O28ubAEj9f3vybbC-XpD7OzMlnV5djlp8PuRJg7fyCRodrLOXci0IiRlzYIC5g-9lWOb6FcCW1LzkFqUwE3Z1hXv_L1L4Nxs6LGvsGr1k89i-bhFxQSzi__FhMQeQSHFWV5_6Us4G3Yvv40vVxfC8wODP4SDxwtHx2EtcIjzVmUFNwKho1ASzeMKDNKvkEHpyl2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2rv70Yx56D5t5vLr5YuIW5MkJ0dg1PkTBlntIy-0FZb8krPGaVykVd4LwASj158DD3ufarOsdHZ3nqGWAL9q0aM1-bnGTrFkW7CIa0hbojZ3IACUwP-s_PgDGcF2bOvo5vz8kkrrymvmVk_GT5eIn21LS0MHQD2IhzeacGUx4Q8fsp4kfBbCo6cmPmC380CWA7pg7c-WKVQDnV7ZObmPakikIxQ1zZ2vMPWuhubodBj7bd_JAwR_-FbOyRo6q3Sa5HKmWAG0WXtplFtOghe5l8OQUM4KsjyxRrnFGNepNm_WXmUgMugHyWQTFiZpQ6JuHJqMoQQqB47w-wgyjPiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7czjp9PELgJ_HWlXEv9ufQjKh6zaWAzwJWrJv89ZusBRPNrtUyMfvgCP6y-UjidEUPEad6X_QzrvmQ_yumcrGPNwwFMBMzbND43kWS6QAA6mdDj_KruMPaW_Quyy1yXmOy3v7NXyn5pq5dmOefaVmPmaQe_He7AFVn1YtRff0tHHstt7VZRkB1GClzgU30gWASxctAK0uDU5OEDPr6JYY6K8Ar-W_q3pyZ-ZbLm6O1uo7z-5osfRPUeeavUxHIkLbA_KwLGH0chh30t9zrepuuiAKkonyV1wDSreQ3zEroeQM52kOxpwdETm0MIA549JS26ZyHZe57Uam14LskEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4U1lVSqQIdd_LinIY2flZp3izk8ewSgCH8g7WMHdIUTgYr6W-63arFYRnWym8GogSFg7afhMptp0cDqojvCN48g2ueTX_aLJTC8AdmVw2PUlgV6ryoManARVjEt1CCEpOfOsspBsPR1uXWrSQaoFQuteXxUew0f_bAGKPu4TXcKHe8mNr3n2xuJbuLhFXury3ojD_xEh1tOSE5sUmH9BOT_CUjRD5Xgjhr8BSYBV-wubGlmLaFMb5dpPnMLwP5bvCfp2HMv2w5fTeAPJR34fS-eY4DgX2j87P2TAgQNA62fsjvEALT1Ond3ucuooCwr_l2TKhlh16i1nsqyP6dxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SstK4ibADdypDsXdyl6izFzl5nwEOo4zAwEOkmjOnW9OoNbLVGqgiEVCnpsyJRlaycVkTlygHtrwOzeSCOpLw6ArqBInAubiaO312AcQipD-xWPVGbvqpqILWFMPg389w1ztpGXBUDywRR4gKNeFTBvuOwXFSgvZM7NONGuJ2wACO1-DjFP1o0mjyXdXsZaR5fNxwUmVgOAG5XONDCtlG2y2jAfxh2nLYSnqTcFBrmqCyT7fdp6mjASS-EI_EVuieyDKyczV7YYQV6R1SYDdXwchbZAJg6QhfLsClMePdEkGZnwLkWSSCc-I-2Mrems7F2mq-cSzvluoERwnDbQnGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=Ifl_6ANX8J7C9-AkNKXUZgBqxpVssVv6sYdAIyzSSaxaD1D_VgkZctXS3M4YloWngf0glK8CLuGEs08wnRRvVX_Qr0Wy6FHeQNnIurU3tzBoc15SdBBarpgdNL0alMDi-v11feQABIPTolj8ds2Ago_SbufypuUK3lHkc-45p4qhcPnOIEqx98YXLdMnvRSdZevDONo9sRBukBKGnTHT3h-mD8iKxh1w_P_g6nOHjVyRJK7_l3BcrbSNfIq0kn44KGxz-SLqtOAFG-BQkIZjEyhe4kjiR38iDD0i7QWpEkZMamhjRTbexszB1TuRrgiCCKc-BaUjmyjaQLaI4iuWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=Ifl_6ANX8J7C9-AkNKXUZgBqxpVssVv6sYdAIyzSSaxaD1D_VgkZctXS3M4YloWngf0glK8CLuGEs08wnRRvVX_Qr0Wy6FHeQNnIurU3tzBoc15SdBBarpgdNL0alMDi-v11feQABIPTolj8ds2Ago_SbufypuUK3lHkc-45p4qhcPnOIEqx98YXLdMnvRSdZevDONo9sRBukBKGnTHT3h-mD8iKxh1w_P_g6nOHjVyRJK7_l3BcrbSNfIq0kn44KGxz-SLqtOAFG-BQkIZjEyhe4kjiR38iDD0i7QWpEkZMamhjRTbexszB1TuRrgiCCKc-BaUjmyjaQLaI4iuWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSBINYY5_lz7TecIdzki5_olIlv2fnve1AfeX-RzYBp3ujZAfDEyqqiaEb7JeJmFnpT8IurKHpBUmXJwSqzHmH8KLcms9R-cnLxTAJb___FqYVjUVoRSZD0XKouwr6luCSlJBPWFqK9tT3z8xqCl09HOmcpMF3uOvZ9xWyaR6FQJP8n20K8bumkJGYVNctmxLTcuN3knQRhW-LjrLVgDvKOisgA_koo5hVnIMiVPJPKwaDBIyX11kUZUVBq2I8Jgw5db_YnENA780YPyPRUrJpy3wRcvaoCkA-qyLaPkdj0lYBJu2iZ9YbnbmiubmqcdCXXWZpjTC3riL-Ofu7wonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=ISDKLj6LnSvXj69Tiv1k2i7hCwYhqR0HmhO8kiX-1ytDv5AfEsvxVOnf3pcqTOW-X47pxWl-WxfoKMazpLtwnmTsAkrCG1M1k_PiZ4Iosg3ACkvFUAJK3vPPLwKVNeNI537hUJLIH3IW4FWXxTZwf_gh4zz9L4Poa-r34N-JHivS7W0lYc5W4UtquLVg1Z991BQ-Qj0_XKRvGXZ2_zM-wbpv0sDiYy2-HlPOuMQJS3fWXDu7Z-kDXV8aPTDfNWwBkKV2cRmujzxdyvSCfk88Lv643E5KRbw-oUn7foNWoqAQmCtvxtVdTyJfwuMDZrZsqzgZEXmiK6f3E68m_1Ec3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=ISDKLj6LnSvXj69Tiv1k2i7hCwYhqR0HmhO8kiX-1ytDv5AfEsvxVOnf3pcqTOW-X47pxWl-WxfoKMazpLtwnmTsAkrCG1M1k_PiZ4Iosg3ACkvFUAJK3vPPLwKVNeNI537hUJLIH3IW4FWXxTZwf_gh4zz9L4Poa-r34N-JHivS7W0lYc5W4UtquLVg1Z991BQ-Qj0_XKRvGXZ2_zM-wbpv0sDiYy2-HlPOuMQJS3fWXDu7Z-kDXV8aPTDfNWwBkKV2cRmujzxdyvSCfk88Lv643E5KRbw-oUn7foNWoqAQmCtvxtVdTyJfwuMDZrZsqzgZEXmiK6f3E68m_1Ec3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=F6CTo1KDmZjKPn8MJv-sUOF4dxK3QwBGlL7gL5ww66sUdTjZh2Io-VicEyS1xz4cRLmTEUkdug5vvPJgqgJqaUoEsguy4Bvb2c1Vv5VQ-ASINmNbA4k3T7w1rQpke4KqVRQCMIV4KPEMqeMewJpH_Tvzviyg4rzzkbRany-tCJM52P6gHk4L_ujNn_jYwQOsob_gnyoaVnIUd_6TDoaelts-v2qMl1BYin8eb_yLqeohjamAnqfU_nJwBTwFdtygRDI2r4-JI8ogbvMJ9ac6KlxlaFpFzx8Wq4HZJvU8U6ZHkwq6wyQmbLQ8-Fyje1muV-j9JIXTaggaqYPBZYT6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=F6CTo1KDmZjKPn8MJv-sUOF4dxK3QwBGlL7gL5ww66sUdTjZh2Io-VicEyS1xz4cRLmTEUkdug5vvPJgqgJqaUoEsguy4Bvb2c1Vv5VQ-ASINmNbA4k3T7w1rQpke4KqVRQCMIV4KPEMqeMewJpH_Tvzviyg4rzzkbRany-tCJM52P6gHk4L_ujNn_jYwQOsob_gnyoaVnIUd_6TDoaelts-v2qMl1BYin8eb_yLqeohjamAnqfU_nJwBTwFdtygRDI2r4-JI8ogbvMJ9ac6KlxlaFpFzx8Wq4HZJvU8U6ZHkwq6wyQmbLQ8-Fyje1muV-j9JIXTaggaqYPBZYT6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc9BnrCh2r7kk3H7D27B5qXP480VJ5j_1vLd2sydWj32-lGhgkFi09At_qZBWb3fAhnzLCRXHGh-r5uCnySiYQq8OyDJKESdEYqDbStQamirCec4ujPFjaKVMa6-MlokCjDlysIalmh_od1SJ72Wi5j5mdH5S2Tmv0heRWDVgjB7VvGvm8IPJV2pAzKfw2RmnpiNA83yJ5DRemchCga3NMdXvj8tlSK-fHLhINlZGrMCcu3nxhjmo_7nM57yILZ5U4TEQOgCUCRcMm6ZbSomEgdEVJP--cr3wRICRWPoIA82vDrGJoYG6LmY_EFGRUVIEpWJ3mM3SywaChTZk69P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jBIxPUdsRDSw27hl8lpWG9GmGalYZ-FkZGF9kFiyRryzoMoNlIuNl_BNSO9e3YcHMR0k-dVrkKXw_YjBSB-SuKzSVjBVUadr5-kfISNS1iu2gNKVpCggz2jJhGNsfGajp6SrwhRC_wxWhvInwYVEt9CCa5k73PuZrbeclN38nB7XaSB_xnsf2JYTe1_QRkfbjfI7NxdI7GjWOZrQFv63Lg50IgtOyqFRg9kM4KTJu8UBIBv9cb-Nuy-O8z_K9VhCptiVQjI-dL1LPEhk6mAxKx4SEzaYBC32aLeLepkA6iact5Y6pQ8n582bwcP4jBFVogmVBs7xiTqADCU2ajc8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=jBIxPUdsRDSw27hl8lpWG9GmGalYZ-FkZGF9kFiyRryzoMoNlIuNl_BNSO9e3YcHMR0k-dVrkKXw_YjBSB-SuKzSVjBVUadr5-kfISNS1iu2gNKVpCggz2jJhGNsfGajp6SrwhRC_wxWhvInwYVEt9CCa5k73PuZrbeclN38nB7XaSB_xnsf2JYTe1_QRkfbjfI7NxdI7GjWOZrQFv63Lg50IgtOyqFRg9kM4KTJu8UBIBv9cb-Nuy-O8z_K9VhCptiVQjI-dL1LPEhk6mAxKx4SEzaYBC32aLeLepkA6iact5Y6pQ8n582bwcP4jBFVogmVBs7xiTqADCU2ajc8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBaCLPAlwsWE1iNIdvzQ8Su_HHtMWINKnahTzHm92G5qlJeljdg0le4PE_CH7ZduW4-3yDOJEeIKysQdcbX0XLHyNQYSOVo0sJoJyCyB80iDs2TqASj_w9KwCTIxfb23Ih7G5bGAEAqH74ALREqc3KrIA_x5pEmZB5Ih6PfIsSFYaJ_1UifNKwmXkSBmfC6bDvDl748h7U_gNCrt_WiY8XLHWyN5j26H79cfQ6-Q3DZrIwKPM_M_9KOX7WFoTjCPPyl94ZkuQuZwZmLZKvqvPk0zWfgchGXZ7tdnqJI1zHp0q8soLtrx1GtDRnMFLMHDfKtKoR8QvKEptN0wMuayEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNgbkMjfG1AJXJbZurhOTYrvBmMrLCq5Y4b0tgstA9lGTtdtcgF7xLlimHHc7KOMpsfQX08gjBNZ4kU8z-KW6_laGhU5dyK5N05pPZ9D5UNjTbjSxNdyEKs5axC8RGJcqkJnSlQzFR-OP7xaZFL-BhtTdkWSao4WJRNAGzGhMx9f32sdMIYVCjqd-J4R8FQP5OQQi-sPo9pUWRFkzveLF4-1A-bJCp34z_jkYr511glXDU-o4oA0E8UP3OPZpmtQZVIoBf1pzV7a8onhVKFkx9e_U7-B8FB8NHeva8rky-UFXU6vIt0jEYZlDSkmnqNDHroeDQEoqgBSG_QDT0b2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWCaCcLQip9LyZmTNd0sU8UFyYLfX18KMVTTct5j6MUo9B2epgZ8-XcohmZOn01oatQDtHeROgQJrmtUb_3K4OH6-ssFCp4DknBUQoHyBVLPLOTuN686G3Rb6yZEDDZuOUn-TpKlHIXXYQxg3N-rdoYooSyh8PkxRrvDbNJ0SBLBoQgqhk-7XMnbDzOiVNWExJh1alDDOl-SVgLInHibSqP3LDSxxLH6VMekdP6aVwXedCWQTs-iycuh6c0YekfLnfXeyAYngC6W7wZZDPSB1IxAde0AvFARYHFpG415qeWz4JSjE6_mUfbQKezozWtA690CBhkyExL9K97M_Kuivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoifUU56V2iac_NMAsJUVGvgnwA38Hi7FntXGO1a0JmODD0NC6N_5Yh9J04EBpXBs5iv861a8J-p9Bwu6BS4nRz3dyvveem6yBvwskcg87M_GLRUy8Yr9rkNRQb22vqIwaXiZknSjDllB50nPOftsSQeWqE_uxCrcmi6V7nYVkUUjxdBcHST-eCSJG0FbDDUw5mkZJCj6x4Gm6zWlu0_3pGhJtrwU1vvhhDWIhTzmglCoSkw0S-nAedOxSqsB4kyIOyyVwsI2Tmh1kiBJLpO4GK9iZQyKQtIQOPfWYeQh4LQK3kS2YpozarE4rdRUTFFrlMWBKMGsdVeU9I0yjtOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akotfa_UFfquvEmipZ928e2jkmlkKqMEqGtTEFAwCCgAINSTcV3EnTXdIYaOIhMD5kEnRSvEEF2yCWU1wqGVWV5CR2bKHI0I_3d_1_ZmOBtnxQJVpqTd2lP41XaPrNjodZ4_Wv6jsEuTGpFxbINNDEObL5T1MtTIA2IBUPMnSAUtsyrzvLptFRyw8piPGO6ClqSbxIzOPbdMO5F2geJw3Q_4mnXpFI1s-IAqYYvUJqhrIXJ0PtPhXG6fBxPJDgZZIPNAGSw0HotFyMVqx6bHgdJDhIVDvtnrwWkVK1XRMN-6GV7Zkru8YXKWhY1yWTvh1zYoyFUH4-MF8Tm6MwwUig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uhq6_uGymTi5mjX7ySwLUcSNeia25tkqVigUkSnvBsaM4RpZICTW8ftjr4eXAKxF2OPakcHRq30SfLlWdGZE5QXNzgRnrQiqB7ZNz869D28UOI-XWsp7u4bnMg13zEbZE7A06_yS1CDYUPvylXlhfffxxRiaXN0f1lC0TND10ydudNqfT60t2ZClbqPd3Hfp7u3QHBG2kg8rK-h9qulNhRMkG1HKbzduFsofkP6yJryIzffCVl0xMsjWxFL_NNCwUmm88RPCoL197azAFCiIfcfIUA7uxCnIpx_QNKLd7tg55VVeRZMhO5vDfVn7YXGd6wsqoLn_MCXoZYU1wnEw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPBFsYCqROjTEafgVCiSc0A-o3vzSf2XC2twhvjF_AK47uLd82Mmrf--cNq8CuV4LEEWZVXGrkVXpxW3SgNeDxRZ_hgvdaZ_uhj-RqMElRa_tnaHc4bY06HzxoBT8ZVsWi7LKk4MzvzQjmJ7SBY5Ddp1MHPcmHfNjl899ErAofoStCVopfJciv8STKlEkdiaGMPQvzMz_oq1DhuC9-XED2xrjmW7_JJnOBcFgixGrzrPKbksP0A4NlI8udr30p_0QWEeYAiLYWgs_Bs06u9R_TNL0PRcIkhmmOkRYcbERWPvY1ISPtMWKX19c6NPE06fGSixR9H4p6DvRkzwAQxZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU0agapbloBAXe6Gmo83QT4OyyBn4mo5fQFm8wE0uc-Hhdn-jCbCYpeuEBjnzvhwhzCGojjmJWb201UgakIJWT5OOLoVy4HkcQzRDS9E03vRxvHlnOvRG34hMpRUm0c1ng7iuemZEGYhYdJkxCY1usl2X8sC_arGyMbH-2lA5JdKy-oZ8PU1FJnXh41Fmv1xnj9cX_4X6sov2DtC_D_p1LvYhX99VGxm5wPUfonn97ZIXGl6w4B9hjBnYbnI9kXxtJNzlMqS6sOeX6CSOif46h6gjlhVXs9CmIXCqZMsNbzrunXm7NOoCrKMg67bAiQ08kvWiCoZ0n8QO7bdpWrfSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=Sob3ogK7lMH46AniPZLth4xBVWeeVyZ4_3aYlJPqRXsjLE9t_INtV6Cn_hGtf75enC1i2kEMTSCOiEGpXSTvt0t-dTqYdVxqaEy1RhaqJ2nhQIRtlZTeKBaQma9vrNEzZscAxze_SLFup_KJN_mWDxRiI-Wwj2MZgI5w_jt_zfBlq6_-5orwboWSDaOD6jhMVvdo7Jr6SGKPj1G64JQARSJuQ5bq6i4mJG_ZstF045ybBwUps9_n5-_ilP9lq0P9nrmWodyTUVQZALUJzjBiDjFLQBCEE5gAV04tJoTEzheFqtIiHwRQgka5Kl4F46LtSfGNm-WjeUJoTIHUWW6dag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=Sob3ogK7lMH46AniPZLth4xBVWeeVyZ4_3aYlJPqRXsjLE9t_INtV6Cn_hGtf75enC1i2kEMTSCOiEGpXSTvt0t-dTqYdVxqaEy1RhaqJ2nhQIRtlZTeKBaQma9vrNEzZscAxze_SLFup_KJN_mWDxRiI-Wwj2MZgI5w_jt_zfBlq6_-5orwboWSDaOD6jhMVvdo7Jr6SGKPj1G64JQARSJuQ5bq6i4mJG_ZstF045ybBwUps9_n5-_ilP9lq0P9nrmWodyTUVQZALUJzjBiDjFLQBCEE5gAV04tJoTEzheFqtIiHwRQgka5Kl4F46LtSfGNm-WjeUJoTIHUWW6dag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=CIGBBGgHosxC1D3eEyVx-QVujMuudYhO-S23ojm-6VBc-CTxtRY1WpkZ9x5fk3UUNnAlkgkC09ImZ2AicTwCTsxVu_VsskS4waNIl8OtVdPQ0BNdDUPIoUHcZkRjkIxGWBU-w5tj35GDKLaWztyFkF8F1oWL1hz5-OQy4q3CyWltviKjWhFf8JnCfr8lq9VZq-zpAsf_5__23qTMC2VAo0KzDEKrNbrnJ5Dp_13NF24tc4Jikt3cZeLaL22-hcNbgSS-o1rM5l4yXfnWeljqFR6ZD4ZbuiSHNQGXgDsRU06MbtZM1PAzBoeWrWzj3VyfcNfkoymt0dsv2c0ZoMCzbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=CIGBBGgHosxC1D3eEyVx-QVujMuudYhO-S23ojm-6VBc-CTxtRY1WpkZ9x5fk3UUNnAlkgkC09ImZ2AicTwCTsxVu_VsskS4waNIl8OtVdPQ0BNdDUPIoUHcZkRjkIxGWBU-w5tj35GDKLaWztyFkF8F1oWL1hz5-OQy4q3CyWltviKjWhFf8JnCfr8lq9VZq-zpAsf_5__23qTMC2VAo0KzDEKrNbrnJ5Dp_13NF24tc4Jikt3cZeLaL22-hcNbgSS-o1rM5l4yXfnWeljqFR6ZD4ZbuiSHNQGXgDsRU06MbtZM1PAzBoeWrWzj3VyfcNfkoymt0dsv2c0ZoMCzbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=TdBZBszcLklLsVOGx8a2tCYBqGfVIiTEdTAdXz9j4AY0SUDZtNphErUIkWwvogb-0UdpwQGXwuy_lxoLjHVcTQBvbVky3xQm9fO0JNeKIMRcP2xwkUmbm2kxZYNqQfZhjHKvzJJo7KgODkqryyIXwW_TQd-A6kcPBYnirVWZGd_WC6McHItn7LXvkhEGL3GMbGNyTudo_ZWppRWuqE20Xvimp8lCeGel3gE5kgA2n3hMSYFMxSRc8idLvsjT4Y2juYex_Yf74Ag-wogek4xYHhvxuhZ7ventVQRS-Hye6pcsxTmMtXkhMk5GTWHiiFi1ohOx7LOCCqZa12G2FfSI-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=TdBZBszcLklLsVOGx8a2tCYBqGfVIiTEdTAdXz9j4AY0SUDZtNphErUIkWwvogb-0UdpwQGXwuy_lxoLjHVcTQBvbVky3xQm9fO0JNeKIMRcP2xwkUmbm2kxZYNqQfZhjHKvzJJo7KgODkqryyIXwW_TQd-A6kcPBYnirVWZGd_WC6McHItn7LXvkhEGL3GMbGNyTudo_ZWppRWuqE20Xvimp8lCeGel3gE5kgA2n3hMSYFMxSRc8idLvsjT4Y2juYex_Yf74Ag-wogek4xYHhvxuhZ7ventVQRS-Hye6pcsxTmMtXkhMk5GTWHiiFi1ohOx7LOCCqZa12G2FfSI-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBJxYjfrsDVXNMh4q-4yEgqVzKc1am3MhkgId9p3rnJO3jgt5NBXv1cVBmn6pSO72Tj8TOYJJWQwuBVCHK85BkgpzgdGF7KhqsHpznpIICBaSKpR3Qe2EC9Yl6nuG-Me-H-p3ygfVMZP81HSXMJX8ZLlIofuKXwf7V_maL2nQ3nQze-3u2d_4Sr9eICvw6ND6A1fECZpmMwH6H70iUmm64L1U6uXzCdtxgFjjnkXhR0N5L-Kk2zJI9Oib_SFAgpAjXUTKJGl-AR0mt2YQdhuIYtnGajlcnXepGy-mgdHUO4hlaMb7ThHRfDlheuCvWpy8KmMD_CQOnxc8uzhV45_HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU4elOHH7bkfh4MyzsjKVqX-es60SImwoCQlMwHRRZvpOdz0FnsbtBD0CHOQCStuj_Lbx6fzoAboXZzc8F68ZG0QiN_hWT3MZtAHRy7wcWWJBVeePksiu9jzqwDteNSAL7tIbhmQH1JOreno4v5Q8vQv6r7oEX7hVAtHfvQrLJpbfUUgtbcupswcMfWOKHenWS5cyh-5DkdoPksDt59lfr-NpzU3eltUeAjqgQw2WRllesV5rdABgMNnzNpQ6wR8YH7yq0OFO8Z70NX-mbmHcqqHf4shZbS9mTLWPawG4H0F0QNyDjxh90JVMeAQnzMF9IhgVPp2TUkpSd_t0spG6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgtRnsuKL1Jrt3Jhmn7IsuD6JXeYsvHmXe9JZez3TL0mDMnhYZlEOgb2oAntK_uWAiwC7Tex7aj95AptahnFX014Trdq6HrdkJJY6g0vSs9h29jTzgAp0tEZ8c18MeioOiLa-ukZvdZHFxOx4deZzisH6xu_h7OvYhy7tAv9zocJUIAZtgHrGelgzygfeeJMiTmnD8PDKdcOTCg8BZmvnsgKg38NKKgRoAn9yDU_v6GlDm-dZSV1VFoik3T0TCNL58U2TlYLcLq8PogMqoh022GWkTOuIFft5Yxcmkw48z67b5Golyvbp5PbXQTKb7n6WifRzNMsl2Ba6ecazhcV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFs38pfVXp5Dx3L1L5IarTgoIm7bvO4pbCD_c8OXlMuOjgnT9ut9O9_DOsj_xnEIteV_TWo54B-fI4FCPqgQp1o4Gbpr2JNxneRYL1qQGMWlCI0Lsuv0FL1EPKgD-ObFHGxcwZWz0MUV5o72_CBzbHUx9CJMc0EgYJCtfQgk-S5nGIkT759JaSSq9a86I8qC_c57Jla2UWyLgpXkZ3W6cepCnRJcUQa1DqNRAGkgZrwnDn_CkhT987LKS4X2UsI9-QY1K3FCZBZXggg_nEQvu_JvOy2rqVW34ebNpSfswOLqCCFN2b0kXkkGDtGL2iLG4Tt4ScY9_5FVhPPSWZ0zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hxIhklCchefcDsC2oYTFciB9bqM5SRW9fsZyHlSgYLZ_kpcYsuTneRyzG5p_z3lP6A43d_Me1Y9kUEmlT9BXYmC5jgq1RwkxIZvqlKNg8bxK3pbECqiUnAdWee56vy26kn9rLvT5TtSQpDLjqeETO0lYdu4eOFtCuHuLIQt1vB0BewDL6Y_CuLA4kQaJdpu9WnoJol9pPnZtf6matFR5euD6fQQUejuiwpZWil1CurpohZIa3j13_thljLBeVcSi5MTVb4dPUtceHiA7TA48J5WEmFj-r9WrnbE9dkcX7dBk0l1zLikIAc4jrJmmqva40zM8m51mTkIXIBEGWJzMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hxIhklCchefcDsC2oYTFciB9bqM5SRW9fsZyHlSgYLZ_kpcYsuTneRyzG5p_z3lP6A43d_Me1Y9kUEmlT9BXYmC5jgq1RwkxIZvqlKNg8bxK3pbECqiUnAdWee56vy26kn9rLvT5TtSQpDLjqeETO0lYdu4eOFtCuHuLIQt1vB0BewDL6Y_CuLA4kQaJdpu9WnoJol9pPnZtf6matFR5euD6fQQUejuiwpZWil1CurpohZIa3j13_thljLBeVcSi5MTVb4dPUtceHiA7TA48J5WEmFj-r9WrnbE9dkcX7dBk0l1zLikIAc4jrJmmqva40zM8m51mTkIXIBEGWJzMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=rW5niHdmUM_fw-uvJwWxMCBIJEoqivb-J_ZfXNXZhMXlEKvHE-uZyvHYYPi837sOaUlKzNaNvJTPhSo4OADtmcORFtmwl8wATg0q5-Pt1B6qTXcnYuUTR2kwKYNptCJ8s2qRl8baVV5TjT1moQs1zl-xTCUCDpZRf_PbyAEKZTic6TZdlDoHg8l6GzH_yjBl4FS4whTUpuUEX_yWtw-efdAHZ3jqoGAMvjvXWTCVjm6IJT8TwLWUz45TWXqHxckOQVa34m0JR4LYJHKB7Rp-Dx-ZhhFtq3NZCx21eGiUo7NVZ0WSgBMVr6vaRhmaDbAbbw4ocDPmCjMfno-3xcOXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=rW5niHdmUM_fw-uvJwWxMCBIJEoqivb-J_ZfXNXZhMXlEKvHE-uZyvHYYPi837sOaUlKzNaNvJTPhSo4OADtmcORFtmwl8wATg0q5-Pt1B6qTXcnYuUTR2kwKYNptCJ8s2qRl8baVV5TjT1moQs1zl-xTCUCDpZRf_PbyAEKZTic6TZdlDoHg8l6GzH_yjBl4FS4whTUpuUEX_yWtw-efdAHZ3jqoGAMvjvXWTCVjm6IJT8TwLWUz45TWXqHxckOQVa34m0JR4LYJHKB7Rp-Dx-ZhhFtq3NZCx21eGiUo7NVZ0WSgBMVr6vaRhmaDbAbbw4ocDPmCjMfno-3xcOXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD595UJFlRa1E8hGhwvD1TsfBCT48nL5B1Jn_FYJw10CYLyFg_JwHjbVUBMxDDyH1kaz00I-Ccoo2yq0O11DQ2ERMxENHWsuLDrGs5Ol1xWTekC_dnxS0wiA4rGSgJJhxlj4ajHRHf9kT89Q2LpED3BPJHx8RyKdKYMyXwvN--53BSs2HIOGFGBITM2mDLAN7jf-cDIyN1-y54kHQ3nEND8sCOUDxZ9mGK4odiIz5Y6xkc35wYLepGD5EvhjRAv9cxYmcbL5AzgeiCUi2OXuz4lh2N4SQKqrxxqHL5XJDrt_Iv4GVXbyeoEDq99SjRjboPHl6q5RKZQCDZV_y9aoyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKE4OTCj3LV_G1C3n18qqPJHW92aTyvKVSwi0TWIHugHQLGXU23Ah7Sg3mft3vTruk5CyMyDdFzjBNuOQcZneH9LO5t9oIVNqHK_EZVNuDSvfY3oDYKqrlaaVzgvVpiOWV-o8_YU3o-KTpdK6Y4PJWBRudyiKBT2s_MyBluDZ73ywMmxGMIUGzDk7n69w7J8afUwx4tt8Ma5ZQnjaAFifhCwUxR49aSmnEeQLuYjyNGpuKup9O51oC5nwqIdseiLWB-j-wOf-otssg7w8u45RXy4xUIfK5lUlb4JVFzp0wIu4WMO6tsJQe44VIhys4_1jeBw5XmYML-SV74uxhZcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mduF-gQv7GVgNhmTveNq3nyaifpReSniEcrMs8Xza-rR45xq-zIbcPXKeXJEXEiKcEGRdI0ZVjCgUla_GSS1THjmFbBfx9GKOemlESAniFMsatLUaN3jZC4CZ0Kj3CXW2w7j2l_BXJm43v4FPFbKjTXuCNwGTjxRopG7SKG9aiIISNSdJNGfSpAIkHyvxdbtCrJxMBpK4G3JnsR4yuzRMQjm34IL_148sIo4t8RYOyBTZtlJu31y3RcUHwvgAtCOSGZfFv-Y7nfDlFq-8BuqXr36VNzlqUZCX9uBWDpGv8oYfeku9Da3PJzz42ouFnacy79UqNqydlpaMgVny4__vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfeKIOcrjofyj44QuuaXlsXBHDNBc5teLf-Ia1SuIH2GPB6vxPlFv_1kA6Ky47JgvHm_uJRkdWRmGns_P2CtVUsm1nJ-xygUhyf2ey9xkTkhr4V2S3EUMBhFzvigmsLZ5etNsGj3G0TdYa2LIjptyJEmmicNoIgZzaxOYBURXQfWFfaGfilU62_RrSfLMkdqtRoDUI9Do2by8rJDBrKhA3pEMZ4LknNKRhlVgJcPlYh2vhqkanFbrl-bsAShsRrmjevYIpQYeBD-xtgDax3hXfK2CVgGMjfT0S712jTIWsgJQINid6rt95-RuULq0z42JNPtBWp6aiLlPsASFAXHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWXfbV1KD225iBeBj8TwFaStlY2M8tJf23YKkZEM0mx4tgFg9zTKZLjfV0LJ6yTmJ0E5JGXsTTH23W0BTGX9Ezz_cBTU9Gb7KPkTkRBUWFNQz0HIOrBjEza7YAI4o88coRybbWovKYP3RjGp4zTArSrr1BEbjJdGBT18sPLn4TataEDSSSWP7YQqCl15cenKLWgVgE62vt-Zj4XouaDEcfOQemPhIJQZM-0xhXzoeBjhahcwg7RnlIlwPcp5CVd59iHiDSI883ivkIhs2eDBfwMU0WEjNoSSkTMFTk3YKCzYVZoGXuYlDhhfqNqTGG6-67udxEjGrYyDiPJ4ZcXV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J99BQR0j4sDpud09zbjtZvWL1IBNAQFQiBvUzbF63AWjgYf9SvNKEMEeRw92ibw8Dicma3vPH00f-ZkvMHC_TcCN2luENBDG3ep9-ndm-c0n4rzBz08-HqO7rvi-yHObGtJ2qu_vQENprrv0eub6_InjJSehq5zDZ6RYgAXQXQs66nDX_FfSVZpEK7sfKGzSFZfxSGuZ-4pt0-PaVh_RUCrMvZyCtFoDMZ1lyYnbNC37_My-dgud0IfUZiDnWiJIq-wEJj9otPnPLYyAYmQyFpUpO9CO4VLw8CpTpqyVvcWF1jB6yN3U7Cf5Q0NrFs0d6dGMobX7AZDTz77grSCcqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS5b6VGM9k5mJ2U1A_mJUmGvhZ45Qn5nwyRtigXFCtrbDoRLkF6nS4yfqIliXAFHLP3_Q2G6oiLFwrLgJj2QLUMJSXVWO1lbJsGqGm9EUQaNBL0m-nPdqETJhHw20wzkVyWY802EgQIalTKurBvnXmZ2FoheqAzdGqrj1FtERbs6u4EPypqSvVfdasNzP0bfr2NRG-4CS9q2JRmujaxEJ7bKK1mNoDaxvYXFjgyqwmINNjNa7JvHOnL00kW3AQo4AQVeek-atv4N8Ud2Ba1OaAH3Wnf5GZR-yC4tX9yDk8NWnYuzOsLVSlVtjuxUeP5lKz48KuQ4td50JV3iL0wIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agJjLCmzVTNLpdshs2iwNNtFkF_aZJCrcFrv1BRJQLeia-XeUTJy0dFXRo1y_ZKyjqIvf82AteWgYLaIQQrbvm3Di4vbIi4yIEc8yHabNOG35X-Q7zwjsCzouq7rt4J4VMjHjuISLRSv6fHIJB4-_lqMLSt_vQQF4_C1JuH75-PhI_AqIZmlqutMe2TLuLX3rCo36kZcUD8gByJKpEY2iZJkTsXCm1Uiyslgg_cXLrqxhys2rlb3jcnm1HY74coOwsURBJimty9H-0lsYMHNGR-gYH3nuAtVPufBKZfgCXSfGAExJOeK-elyMvtgmUa4HdTYLiyIocf2k_LH2zq45A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=o7eApBz3WPF0vkMg8TRmMs_mR187OXQQiSywmRuEDQ5y4bH-kKAiY-Z4SjG5s9dlzBrDaf4_Ck--W07Xl7Q1lDExCKBIretsnzysCIIAX1P0_GTrWK75V3xWOwBznsZAsDMNiOTeYEgLaVp4rhwOy_BOImE5TuUOfm4PJ80lH75f4Dz6t3ffkcg5St-IK8o6EQCDWLs1DI7V8oLe_9oDxeXaZvsBkDAssrw-aTuP-O1S6ejx4loykSSH6letYkgSKXIelZfIhthO_zq2U6Xcl8bwaElPheBciwlupLgNz43BRgad9VCASrWI-01oL-1VsyzKGb0Cnluy0FKLKOyAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=o7eApBz3WPF0vkMg8TRmMs_mR187OXQQiSywmRuEDQ5y4bH-kKAiY-Z4SjG5s9dlzBrDaf4_Ck--W07Xl7Q1lDExCKBIretsnzysCIIAX1P0_GTrWK75V3xWOwBznsZAsDMNiOTeYEgLaVp4rhwOy_BOImE5TuUOfm4PJ80lH75f4Dz6t3ffkcg5St-IK8o6EQCDWLs1DI7V8oLe_9oDxeXaZvsBkDAssrw-aTuP-O1S6ejx4loykSSH6letYkgSKXIelZfIhthO_zq2U6Xcl8bwaElPheBciwlupLgNz43BRgad9VCASrWI-01oL-1VsyzKGb0Cnluy0FKLKOyAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ZnrBryBOJx6d5xmG5PmANwUzDdgWfE_MPaaE6Vm8a1UIlcQozRhsI7Rz_YkmDAUEp64kNOulZPAlnMZLrFcCPz34zW0YCRLiFqRCgxdxMzKzSs6JglTQ94siCHZ-0PQGHttmoXV2zcd8AH1IbzBRWZyUKK2h13jIhUozxhpFZVxnqsys7CVzNdk2w5OZLczuasSaUiPdC_SnYSh3_xx_xseOF8ccNRis1nRAVBDjhtteutGjcCBaUbGPViSyshuJGXEmbeALbqcwdsx-p5q49Pnk_flaCpwgafn53PrtG1A-yRKUMc3wDniVMU3qehaakdsbIrjNI2-9yvzKQGKdbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ZnrBryBOJx6d5xmG5PmANwUzDdgWfE_MPaaE6Vm8a1UIlcQozRhsI7Rz_YkmDAUEp64kNOulZPAlnMZLrFcCPz34zW0YCRLiFqRCgxdxMzKzSs6JglTQ94siCHZ-0PQGHttmoXV2zcd8AH1IbzBRWZyUKK2h13jIhUozxhpFZVxnqsys7CVzNdk2w5OZLczuasSaUiPdC_SnYSh3_xx_xseOF8ccNRis1nRAVBDjhtteutGjcCBaUbGPViSyshuJGXEmbeALbqcwdsx-p5q49Pnk_flaCpwgafn53PrtG1A-yRKUMc3wDniVMU3qehaakdsbIrjNI2-9yvzKQGKdbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOwXLNQiHrYlG9zssClY6swShfu1Z9lMgmRY6uLOoixBGSdxbB21E713UeyuPMdDpUf38ugoa2meQ4OSG6YNuImqNU9FfZgIKU17AZZfNyV0f6chJlOqUqojJW3sf0GutoTSbzZZHZ449CrLQ87m_rLNyGzJon53oMtdt7q_Y1VJ6El7t1muPYhzLOIZiSfs939-IbPuAj_zLi7Wjygkkkna4Pa4LmoEZS07Z4anIeE-eljLJhhz8AtsLaT6vHJAqLCVd7EQLwkuFlbCl5-meVeE_FDjFZJgrlNIbfpE2pfGdyQm5PDOWxYjSGWqLsCFdfeMTsclRGS_HSOp4oPOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOEuh5CDCppMrPwVVdVl0bXWIGsAtArTclC95UxtSflXsmiyKwcIvDH6M8WMMbigYsCBE5Znz5AJi0rXrKUUZSdnDXgTuLPSmaauuwn4K8K7lkU_I61TRSpmEydKoa0iA2s6BfzJr-CT-hxTCrf-_zN02E_OlLfsz6ostFAw7YpeJZ2exqo53hf9HCvTI9Jg6iXrKnp2y5GUX7cgM1xIK_qTWW_oiDDOTwbut05TSirrhPd5cu9IaiVfb_go99SOM939DVmXWRKwhCvN4dW573UWRISdx8OntUwwv0RJ7o586X1h7K2gLcO1TsYHAkC59KnsNllylyz4Ai7PpcllCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=kfi2dm_4Z7CsRcR5JVeUsxk8XF8GnGZWilXrJZf5D50Zm8JSyMjC5Q7OeYTOFhfiA3ldp1ImmobNmSBBUtGPWeQrkmKo1nHgaMHF_n2XRQe3qvJWCp7R4PL32oGkqQ2QffidLN_EU8WYXzE_MYIf6k2XbbhCgA81Ny0swQq8CLkiAO6UVnpBMb71zdDm3iwuc6Y1WQenD5zaIhVhtJP--ClRlPbupPuFNBNa2M8jEyAbs7gN9reeWYnOhroJ4JYc8M2pEEOnKn9vUNXbP2SsmgrYCFIp27-PShK8ZCJFHkNGTdHYk4NmNkR4-Re-JzByMDTH-XeVSHrBf1YXETXfmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=kfi2dm_4Z7CsRcR5JVeUsxk8XF8GnGZWilXrJZf5D50Zm8JSyMjC5Q7OeYTOFhfiA3ldp1ImmobNmSBBUtGPWeQrkmKo1nHgaMHF_n2XRQe3qvJWCp7R4PL32oGkqQ2QffidLN_EU8WYXzE_MYIf6k2XbbhCgA81Ny0swQq8CLkiAO6UVnpBMb71zdDm3iwuc6Y1WQenD5zaIhVhtJP--ClRlPbupPuFNBNa2M8jEyAbs7gN9reeWYnOhroJ4JYc8M2pEEOnKn9vUNXbP2SsmgrYCFIp27-PShK8ZCJFHkNGTdHYk4NmNkR4-Re-JzByMDTH-XeVSHrBf1YXETXfmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRvPvvXhHMPcvXKXYCU3awsZ2OXyLCIVzKlBvYyxfCbQYoJuXkuHGYkwUT7V8Aa53kTFmgIF_1hj6E8OHhByvzbGGB-suwyQIjg0rOIesWuMQT7r7_D2_UTd7Omcx37siVDMAuF1iFLv8bU9nMlN-wH4FBW_3JPq9Qs5EpQFzeEoQx6OErIkihQ1-8iy6iXjcjJDcbfgJMkIcIEyQK-4C-ScRkbmnTHBltlH4LWuhXNuhecsPEafyHJl8nb80d8H3YjTj1ZPe9I77MjF7lOcYRi18ltCH0KvDGHhnFNGaFJL_WPun02AiGVhU99jpfUkxz8AgEl3bw5cP-fQPn1Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=M_OgbnPxOLuMQ2MxlMLFWabeTKlx7rUXwuvtZiQw6ehGc2o_TyNZzEeiQu3cbjIE-HDot2j-UkdtjSCbbiHvpm0sY6O2d9O6vYkxAt9-qRSL3SrC5FNwxUZJNPDOrpAM31h15fEhLqiqNAki1zHJZR-reIyGWmIplpovfT1_sngtWyHj9yNN2-j4srYjbQP4O3MZ2skX5e2aKLU9LbXQwR_E3ev07L7GuvZzlZBqpGs7bIU0iujg_k0Bj1ZAcPo7b5aPn3vFy2sIpPMlDuepxE4ovZhOwGlcbxKgvVdTCnip0bAPD8AKRfrclROdbtzn1ek2j9YqYoXOdk2BE8LVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=M_OgbnPxOLuMQ2MxlMLFWabeTKlx7rUXwuvtZiQw6ehGc2o_TyNZzEeiQu3cbjIE-HDot2j-UkdtjSCbbiHvpm0sY6O2d9O6vYkxAt9-qRSL3SrC5FNwxUZJNPDOrpAM31h15fEhLqiqNAki1zHJZR-reIyGWmIplpovfT1_sngtWyHj9yNN2-j4srYjbQP4O3MZ2skX5e2aKLU9LbXQwR_E3ev07L7GuvZzlZBqpGs7bIU0iujg_k0Bj1ZAcPo7b5aPn3vFy2sIpPMlDuepxE4ovZhOwGlcbxKgvVdTCnip0bAPD8AKRfrclROdbtzn1ek2j9YqYoXOdk2BE8LVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
