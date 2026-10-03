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
<img src="https://cdn4.telesco.pe/file/scqhaPl9jwu5mwjC1WZNODqMg6kfuKMjMBWDo-jCSTBYtDrMgnqS76WiwH18VUDsqtElcx8j0vApmnxKXS-k5Yp72pb0LWu_jbsClQdHAQtYEq6zGLEGr1Co61TDP87CrJ33vWXSgIxHDrRwwXHwrWJXAtynSH6adsejdNUgyACAB6NVFBH6nUY-LyqqXRVJbTR0f_G26HkOZG7GeAVWHwPw-Xo4s82a5FVBj9n32lnTySRw9DtT3To3esZI4paZ9IrgsVzgixA2h6OG2-CyDKIQwc2b6_v4nomhT8BT-3GWqO-yrP2p2ffOGtO3SPXH9FXsj7cx3wJNh-OC2dv0mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدخل منطقة المساحين في مديرية الشمايتين بمحافظة تعز</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/naya_foriraq/92434" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">إصابة شخصين نتيجة عدوان سعودي استهدف قسم الشرطة في مدينة صعدة اليمنية</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/naya_foriraq/92433" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzv02zAAXhIOhGjHMgVSUgb4hIv2P-mu8nN2T46VCplLmZmmd6s6-Z4ZJPkuyMbMiPpklAaIe4_lLJ_ptdRfGABlbHYTNJmMOR2ptvlQHCz7gmuQRnWaAds3izAE4NeaRya5uFYthBhW8z1Fp82KZJnK9NXdfh4TBxpEOrmAvCEO7DYBrpHnifJWDCIIn-CFWC0I9VKrfiK2puKsBt8boSHNj1p1TqtbTvShDQqHw5wEMg2OI4uNxM2kivbJYI4vX5GpB_xOpQrtjOdrAH-UqJqvWYKR9PSk0hX746uySuupa5qyx71C4htx44nlwtI9c6cTFmxHkvUBz1hCCV_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العاصمة السعودية الرياض تحترق</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/92432" target="_blank">📅 16:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو تحترق</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/92431" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/naya_foriraq/92430" target="_blank">📅 16:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/naya_foriraq/92429" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92428">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/naya_foriraq/92428" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3lttzcG0hPtqa0_H_t9wy0lBvNO58xof9UFCK9L-LjDOv8yrdK7U1Q0r7ZCLzECtRVhMpA1VEI9QLAlWex8mWgJcAuFdLE6i4b-CwlTpwJLx9ATjQ2Wb-34uqAkObQlHUEgPJgwHMIUmUEMVqroUDVw6TQJcj5dNQqC27GFz-Jc6PH5ynu9J5CcPNtbeyL5qyYkqrAshq2bCpnlH5wGJ2-gAYqF3QFksJgQ1XJnZ6B-SNy6PEheuXHLPrO6hcV9iJkhor84cbvakcWaoDPBF55f11ukgCd8Woj9Yy0QOefcF-lsN1iLaNAXrKu7oUkEyKODwcB9e5IAG1So7SZong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtPjaKZHrixrae5V54WT9LleLITGn4vSmMQvEwSjBkPvixNyBGCbOaFoQBLRhWUI8xdFRpYhJ6LbQfmE98jjqsTUiZ_E_c9TKUSAxeItwr29k2bI8wngVf8AW3O10cx3-MW1MHVWLkWcpjwp6Sk-63HwPBTv2hMyBizULrJwysbmd0mIhxm2Hk-j42NKDUhP_b1muu9z8w-BuJrVNhdS0JrJ7IMs7560bi_iLkaIiMeSYqdl_LMMgauJLZKBujm1KG2aTu-ntJjWUKicE4LVke1iuuUR3oJ8ZF2FGlp5qzYViog-nAGERXPqtKzZ9ex5i_fQYFbc1z3GHcVHTDZ9kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور أقمار صناعية جديدة تُظهر اشتعال صهاريج الوقود وخزانات الضغط في مصفاة أرامكو في الرياض عقب ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/naya_foriraq/92426" target="_blank">📅 16:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات جديدة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/naya_foriraq/92425" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جيش الاحتلال يعلن اصابة 8 جنود امس من لواء المدرعات السابع، بجروح نتيجة حادث سير عملياتي في جنوب لبنان حيث اصطدمت مركبتان ببعضهما بالقرب من بلدة رب ثلاثين ما ادى إلى نقل 6 من الجنود لتلقي العلاج الطبي في أحد المستشفيات وتم إبلاغ عائلاتهم.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/92424" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عضو المكتب السياسي لأنصار الله حزام الأسد: العاصمة بالعاصمة ومن كانت عاصمته من بترول لا يُشعل النار في عواصم الآخرين</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/92423" target="_blank">📅 16:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارة الصحة اليمنية: اضرار بمستشفى السبعين للأمومة جراء العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/92422" target="_blank">📅 15:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgclSmCYcte82r9uUpLTr_kYwxkuWlTXkctO-m7HGJvfkvdosnULblgqQtZhGorBAkMOZ_864iBdlTxITDWdqXd1nnxqeWUSAhhHpuftHboya8sKq8_vG0Y5s6ATC0Y037cdXGApOT9ALI2QUiuJ3bjY-Lo00fQ10UyYhryVOFURm6azgBtytg4cqh0JBcybb43LNyTF-WPbXJcTLZuzP3t9z3ZvqBSqDtAULJvnMxFFidIkBQZYW29MFt-3DKkLRetRJOKRtWEaGxBgwVKiv3aTdGVNcfsMqFQy_f1tr1rUZCJ5CnB-LYDwoL8zHaFUiTm26xZWr3S40xnSieUx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفر السواحل الأمريكي: اختفاء طائرة إسعاف جوية كانت تقل 6 أشخاص قبالة سواحل مدينة "نانتاكيت" بولاية ماساتشوستس. وعمليات البحث جارية.</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/92421" target="_blank">📅 15:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/92420" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اطلاقات صاروخية من العاصمة صنعاء باتجاه الاصول العسكرية والاقتصادية للعدو السعودي</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/92419" target="_blank">📅 15:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي يطيح بعدد من كبار تجار المخدرات الدوليين في منفذ ربيعة الحدودي مع سوريا و
التفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/92418" target="_blank">📅 15:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4VhrjmwQbv53p4Isdpl_In0g9fNuMPlUWcc5SHNOm8KSn4I0myMuXK8U2tSNUqn8OY4UPYgfB57ehF1tBThli26GZzuatl6ppQLwPUoA_gCuuRQV4f4IgvvDHhSewn8ViUFHO1dD_HsQIqpBWkhq4i9X8gjhm2OvQ4yWJoOzdjXIM-wDF1KgM45sM7BBGfgVXIc5wwDWcWx5Gn8aP-4FvMHGJe_nOsPq4sZuWLOwcNBjoADRJxcWeiszVJK8sYrwTYscSvjUFzNRgg4-Ntk1c0BQ6gjAC-gQlRbA3mXAb2mw53zN7VTgAhkZC8oiWik4g0YUc0XgMA9YDwqqS4kxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/92417" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/92416" target="_blank">📅 15:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ممثل المرجعية الدينية العليا الشيخ عبد المهدي الكربلائي يعلن استعداد العتبة الحسينية المقدسة لتقديم العلاج المجاني للمرضى القادمين من فلسطين وتحمل تكاليف علاجهم ونقلهم</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/92415" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/92414" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=lX1ghUJtIw4NSaa-VzgyydMdozueMKTkxAi_mjCBIrpGWmOPUt6RY3ARxXdHFm_zf2KdMedB0FIK8itGoO0esha9aijlS9GnXY4F_vWNehqR5wl6sEu8MyT4-EZqmCB8RMikibFN_Wvl7NCIjbqzUMn6M1YrYk7CEOrr8H9UeZ2YgNHwDcyWPgribTyCIbm7inVbVz1u1mrbpRdkqaBRNBCdIVhSMgjPTBU9t7W56cD5WExaNJUodLrklBuA-LF3KDMi34AHhzdm2BaihIucmYX6u3Kx7S4rV22HDhwSYg9uOKhXSQgub1T-idmDKajaFbX3ZXp1dRqIH7v3MYun0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=lX1ghUJtIw4NSaa-VzgyydMdozueMKTkxAi_mjCBIrpGWmOPUt6RY3ARxXdHFm_zf2KdMedB0FIK8itGoO0esha9aijlS9GnXY4F_vWNehqR5wl6sEu8MyT4-EZqmCB8RMikibFN_Wvl7NCIjbqzUMn6M1YrYk7CEOrr8H9UeZ2YgNHwDcyWPgribTyCIbm7inVbVz1u1mrbpRdkqaBRNBCdIVhSMgjPTBU9t7W56cD5WExaNJUodLrklBuA-LF3KDMi34AHhzdm2BaihIucmYX6u3Kx7S4rV22HDhwSYg9uOKhXSQgub1T-idmDKajaFbX3ZXp1dRqIH7v3MYun0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق يظهر إشتعال النيران في موقع نفطي أخر بالعاصمة السعودية الرياض بعد قصف صاروخي عنيف من قبل القوات المسلحة اليمنية صباح اليوم.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/92413" target="_blank">📅 14:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/92412" target="_blank">📅 14:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=YPa_XXJ0QiDOxF-vVsYElX9uPOuXfiPAVa1Bo7Sl07ncwaOi14ubv6KK8c6lValOQGhh0LhzFjCUN7kxqh73e23kDb8UeS9xk_AnRc73MrcAEQCBsZjM5DrJjwv9iaVCZyve9a-n5HH82B4nP3QAjjIJPW9slR-YvZyjbtMfRu0eQT61twOMWahaLR-v9L9SbW6uqXrGbEdEdkINqsdHEDBksIgtNA1VrOipFdZK1LkI0rWwzY3t5OaiUomRt-aPpvTwhNw6q6GbiTDJu9NcGthArdnnYFk4fzgNscBsnCFQ0ToaEcfb8h2ENJ0qQIrzwOqzszJ4Pcc000xmnOOl3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=YPa_XXJ0QiDOxF-vVsYElX9uPOuXfiPAVa1Bo7Sl07ncwaOi14ubv6KK8c6lValOQGhh0LhzFjCUN7kxqh73e23kDb8UeS9xk_AnRc73MrcAEQCBsZjM5DrJjwv9iaVCZyve9a-n5HH82B4nP3QAjjIJPW9slR-YvZyjbtMfRu0eQT61twOMWahaLR-v9L9SbW6uqXrGbEdEdkINqsdHEDBksIgtNA1VrOipFdZK1LkI0rWwzY3t5OaiUomRt-aPpvTwhNw6q6GbiTDJu9NcGthArdnnYFk4fzgNscBsnCFQ0ToaEcfb8h2ENJ0qQIrzwOqzszJ4Pcc000xmnOOl3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/92411" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba88927483.mp4?token=gykmCR3uS-Pb1VYg2E9-5P97uecQvWP0t194YVm3hV5aIAcsVml8U6tU3QX2W5nXsgbAOOey5eIEmMQ347xlZJ5b4a8-nQ4qrXQZM1vTKXhUCESBDnghshsyje2TPC-kIa77IVc5B5KIIm80gUfse4GITamRuvWxs6wN4Yios9X3gIZNpnh9VHlzFzaLyG0wiN-sN-s-Fyv4GM2i2gU-sSGlI2zpTbaFBPXt3Z-l_YCMsyhax1zJprskETv4CuJ9PVLSUyqOBwzVDA1gvN76rns2BJBnI2g5wwObeAcP25GM1cIgwb2onNAbTrCijnLoNW1XAwz3kY8oldp0WS1ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba88927483.mp4?token=gykmCR3uS-Pb1VYg2E9-5P97uecQvWP0t194YVm3hV5aIAcsVml8U6tU3QX2W5nXsgbAOOey5eIEmMQ347xlZJ5b4a8-nQ4qrXQZM1vTKXhUCESBDnghshsyje2TPC-kIa77IVc5B5KIIm80gUfse4GITamRuvWxs6wN4Yios9X3gIZNpnh9VHlzFzaLyG0wiN-sN-s-Fyv4GM2i2gU-sSGlI2zpTbaFBPXt3Z-l_YCMsyhax1zJprskETv4CuJ9PVLSUyqOBwzVDA1gvN76rns2BJBnI2g5wwObeAcP25GM1cIgwb2onNAbTrCijnLoNW1XAwz3kY8oldp0WS1ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/92410" target="_blank">📅 14:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92408">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHukE2iA4TRe6qalDXbvekXnTni2iwKmuXuTh9RrnmxgbgzZbFVeL_tvn_bIk27JzcqlU9Ra19dvsclrjG0PvCxwN4rVIrHxiTzF1kMbOhBOjI8Ski-g_pwVzrhkdxiOCQ98MHSwE1scXAX449w2Lw6UXCHIqUpOdilG1SLhpKeiKpeLX48JIXgQxAXjaMzCo3xDqj78aqHGPZwJsbvMaECZiWzpZxAoeT8454omW0pKXzQr4riJNBsje1t6D9-XqZCoVKhfI0vOGAsb77enwPGnNHgZjdnkNJva_VBQcl5JXZSLXbpDG2aHEfvev64yKXEWwOb2WDivWhMdYHxjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Urv22ksZzz2acQYaWutZqCA15Cn_cc02kPs2I4VmZQwomQ_HESf8gaL444ESXSWFhUf_Eqqdbt7o1wc5batYwk4YYUhBACBSJ22QXYflAgSc_vzWNlNfQJx4vaI9JcNogwdDtmZMlC4pyYgGn_dkdNCvnUzAtyIz664OceUypARwAlr1g4ZET_0_ZR8X9TxliOC8M28Fei1F1RMOfmyw7dWDpnzJJOvfkh6SrFHX7xm3BMlNI_QQ26Iwh6fbU3thH_jxlSFDyMIEsVVD0MEljHtlwMxVKXuAFBeI9_ox27StDBEt1jvL4vgWYMPEElT-utckJMM8TSVy88iNPPGJcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">غارات جديدة على صنعاء</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/92408" target="_blank">📅 13:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من العدوان على صنعاء</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/92407" target="_blank">📅 13:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=KlNCSDVa65SDDpHbmABk54jTe0dZ6JexebTltXDaDhMcnVzLVq6RGHngnOzLooOGzXCWoIKji_I95Gi3mq8PXJmzDMRTf18lXO3ReSSYL2b_ERJmjVxIsaoh7saW-dn9YdeU3sc0x9h2cmHnNsJ74wAVmJO4UhDx1jOJJ2oepv6iJzL0N8qWAvHjti2mf4yz6ikCFcJlhR3ySJWMl-R8P4yMPr-XtRhatPNVUq9IvVmN72rCXNARsGZDaCKk0urHbKdHhWnqjF-Bd_1umeKfAHlCMNJusMl1bUPlC8QBYiPkPG56QY9kPhr9Aj5Ou1tQofxbqnSaTJrZbhixbTn-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=KlNCSDVa65SDDpHbmABk54jTe0dZ6JexebTltXDaDhMcnVzLVq6RGHngnOzLooOGzXCWoIKji_I95Gi3mq8PXJmzDMRTf18lXO3ReSSYL2b_ERJmjVxIsaoh7saW-dn9YdeU3sc0x9h2cmHnNsJ74wAVmJO4UhDx1jOJJ2oepv6iJzL0N8qWAvHjti2mf4yz6ikCFcJlhR3ySJWMl-R8P4yMPr-XtRhatPNVUq9IvVmN72rCXNARsGZDaCKk0urHbKdHhWnqjF-Bd_1umeKfAHlCMNJusMl1bUPlC8QBYiPkPG56QY9kPhr9Aj5Ou1tQofxbqnSaTJrZbhixbTn-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من غارة على صنعاء وسط دعوات للهنود في الرياض لشحن هواتفهم والاستعداد</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/92406" target="_blank">📅 13:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9T57z1FasjXGi-Zo0BMMU0RtHB2Zv6EQSCGAZ323SxesiXImBi1skd2knbCD6QX9vmaaWtEOPHoRwvdWhRZBEz-35VhDJ86uEqloz73d2xLDK63c4E5x16svTpPBqlrNTq2iT0q7MAOiL_upDF-LsJieXz2ELE9if9f5tVoFAkXAHzQIxxhiEZc7Jiqsem5wQUrGtCJp6iFXm9AYSv8lGYYiO1jYV_K_aUyW2dACcDBneTdEXaQ4G49fKbDwiZgQY2VZkgZsbv82gAEg2Gx7ufd8ViDensNdxrsHarweANmQlcoW9zyZMUZsTM56UHBQ3WDFsh9WvkEi-Q6V6j3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من صنعاء بعد العدوان السعودي</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/92405" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jexMetbIdKDom5jjYIy4tJeHz15hA57nUyHb1DoxYeyR2aZ9EMH2QHNeqCRqWdOqX-QsXrf1e1Dl-_WtncU-Vtd2wEF95aMngZT8xU_iWqq13oFQ7ylDji9M4jvlNkWJL3wwj1BvBqpFWjFDzP6lUze_Tm2yj3qEBqNbIcg87-IbApDPePyXme0utfBmanFqctlhki8O9LqMgJ-co-hG2Kw9MBmalU7yTDJWJKIaQxAtSIyLyq6HBNbD_KCo4C_tBPuW7W_6Ao0xABCSXNc5BN8d6RjVGFuW_KQrCAVbwxsowsI8bXErdntbu8PX3NAfO_t8d9r0qlJEtDdbWRrx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoQbw4OosoArNHyNcToeilJ6BOqqjJwY-zHGIwauFUU6L_idxGjojdCF7Y_8nI4Mu172NNjzIFbTTLqdreX7RoOO6tYPfFbkq9e6cFc58EHuhEhafiJTtwKQONI2-4OLxWgNW14qh5ASCZgYlMB8eIgzWf8MdoyFD3_f0_UA1N1yz_xkJ0sETNc5T_ErRxxVAOeZ3zkO95YRG0WRkjvh84R-hEdtUJqtSE8bySAyq97lsqvC05C9njRzQPuqm-y_651cCO6DsxrHWgM_YVk-ZIDVWF4KoOS8qMFVfDP7menc9AONZ60gOdINRM4WIAl5KTpwIyNr4uAX1wOEPgdrbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/92403" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRSzs8z5WOjK8ds5At-h2OKLB0mI1c7E8krhbH42W7W6xZgcRZ8iXQiSI4YGUYd1btFCrDSosceY1mc7kStL4FmmyIj4mB8SLJrRrWDggO7nWOF9b28kjP2mJeTD9BAIhV2aWYDOObueXvrYxYDSnXwQzvUWno3XVvcpHZ6A5_V6rQ6oMdnZMkWDkStEqk0VU95bd1dHMbUX9DixQPKTEz_OgOR_aPwLSSQcJKxZyGpfd0oR3blPHjolARPS4-39cAacXMaPVD2voGYqYu-XbQdOUezhbs-KIElJILd46FOhz6jhvQmrDfRdqv_JQ9lOX4ocV_6h8RAE7pSojHtGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/92402" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/naya_foriraq/92401" target="_blank">📅 13:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تتمكن من أسر عدد من مرتزقة السعودية في جبهات محافظة تعز.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/92400" target="_blank">📅 13:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
وزارة الإستخبارات الإيرانية:
تم تحديد واعتقال أعضاء 4 شبكات منظمة، تتكون من 31 عنصراً من عملاء العدو الأمريكي والصهيوني في مدينة سيرجان بمحافظة كرمان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92399" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇸🇦
🇾🇪
انظروا إليها تحترق.. من الحرائق الواسعة وتصاعد أعمدة الدخان في مصفى آرامكو النفطي بالعاصمة السعودية الرياض بعد أن طاله الإستهداف الصاروخي على يد رجال أبوجبريل.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92398" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92397" target="_blank">📅 12:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92396" target="_blank">📅 12:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصفاة النفط التابعة لشركة آرامكو بالعاصمة السعودية الرياض تحترق بنيران صواريخ أبناء اليمن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92394" target="_blank">📅 12:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
إعلام العدو:
فشل محاولة اغتيال علي العامودي خليفة السنوار المحتمل في غزة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92393" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصافي النفط في العاصمة السعودية الرياض تشهد تصاعد كثيف للدخان جراء الهجمات الصاروخية والطيران الإنقضاضي اليمني.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92392" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92391">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد تظهر دك مصافي النفط التابعة لشركة آرامكو في العاصمة السعودية الرياض من قبل رجال أبوجبريل، واعمدة الدخان تتصاعد من عدة نقاط.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92391" target="_blank">📅 11:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njVoMxA3c2qiiP9JqYQB37-eIaryrSHCjfB2IBW3BrSvuusG_VxfBoMDaO14smegASFqRsX8I5rFbmVO9nHHFwq5mQwgYEkEHNpG_B87S9VcRGgzx8iSv_YRUu_sGsOaCoCJlD-uEjdXvkiAfYn-SGQ7YTkoiIiPTuLYpO2M3JXcvSP8YhEANCYKiArsqF2BaTvjx_z5Fir1cC7adXEZih5iKtOQi2Yn07hBgHa5BmaOBvt9Gr0aKUZxHzxHA2wqYSH0STkKCWH-NER2eEpBm5ZVUBa3V7b3IBdNoo6mO6yoW_9lOXEbfLyGnhYLxLrzhn-tw0maZl38oHnPg1BvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li8PzaHDlpkviKA_fv2pvggN3NzDW8n6bLgAVvHX1E2K_jYXQ7i8GfVZkQF8vTGIbdiyNQzHtA7eeAU_x7Fs1csp6hRmO_DJ51ZfJTlgpyonxnN6CxAg9G7HJCckpuakMzfFzzEkK-fl5HlJUa4XnpSZIw4Zz5qgD2sawVi12ELanzOZ1eNoxb8a1vEPA-HquwFhyG4GRcPXGAjGltnLzkiwBqTOT7ZIzws5IirWPm2f5-txpyz3rB8eztsIKBh37PqyiiBJMOdKuQY-NAqH-bQuW4duB9p5AN9gwkHDXvWy9CNs3k9h5lvmuxc9AyE9CEB-cnxeFObn2NTHyZP1TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة استطلاع مسيرة من طراز "MQ-4C Triton" تابعة للبحرية الأمريكية على ضفة النهر في قاعدة "مايبورت" البحرية بولاية فلوريدا.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/92389" target="_blank">📅 11:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
السلطات الليتوانية: إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92388" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92387" target="_blank">📅 11:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgicUBZaGLu1s8PNlegP8uFQN1FFuWOy4WU41dP7XqRmpT9kN1yY6RaTRMFJImpSx3DtXFspX9gMZ9HjW2Rdk-gn0vJv5rHG2uCtXTT7P3k_2N24TNHlHsm5oC99khw0CoS4scjgrXvKZGVLB6BK8vSBmZQUmdsP_VK8d0BPYb_JcH87YpKmLLjoATN6331eUHpwpDsxPqpTNJqw5_bhkmRphqqMEj0wx5KSLUkd_WPHuIz5b-m1Pfjy-ycwAka2Oqls5M2s5heP5EP9vA1k0bYPVw92NQGCwUWYc09uWZ7Q-viLav1cGUuZ5Vygg0okEjAZzzTmhj50uFkzE6pinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من صنعاء نحو المواقع السعودية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92386" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGx_J7Vo9GqMa5O2CG0gzNbT8QNqzLjV7RbjQAG-gmmkmJgQ8exaeRDbRFsbmaSs2Ch2rCaBO_FhP73l6f3jO8nJxL48J8JCF_8GpMhKzGJ_Vehh8S3Kns6jm2RzI4Avs0hmOJOxZ8JZDQDFcusZ0gdVxKxBb0JaOMXoHZTlUAq6FLWcLNe06cHth2LIHgSaUQ_E8s_2tZLXHXZ1zjvOR1K7F97K0ml-5bO8c_MV5IuUzD2o5yHzxXazSLIhzkktzrPx2n_RY8WE6D3aIOJ9ShIvywKMW-RoJpm-NpRQczsbS__-YbD-C9jVLiBIhq9gWCrlDNJTGN_y_BBlc4Wa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية بمطار الملك فهد في الدمام.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92385" target="_blank">📅 10:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
السلطات الليتوانية:
إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92384" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92383" target="_blank">📅 08:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW1e_Hy2qu2EcViMIOND0PVGzr6plERpvclD6mlZYDX-B4-P86UVJv8Y96rFovz4-srvtkOctM3mIAwvkwvUsPAjfAyRHZrwoI0c6pK6AB619rwRy7-8QQRnz-F0DKNK_BbwrpbGdskj1Hy7aN-5PkBPW37rMcfrId2edlHpqTTswUeiHbWpzsG8biIs0xDCsMGY04CJAomwaL675XdGAHzE9oG_3-Ox-KH6CFY6-4nZjBXD1dmhxW9d9F9rRCz_BBrSHIVpaWFENXSneJdfocEyGsSqx4ip0_QKszEajYtq4paMo1YEPMnD6D0o5RlT8ndznpOl4-RexYENLMGhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92382" target="_blank">📅 08:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترمب: لم يعد لدى إيران سلاح جوي أو بحري، مسألة إيران ستنتهي مباشرة بعد الانتخابات</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92381" target="_blank">📅 03:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORr5MdbGOu-ePKxJLkmN4nf2x19Zf9gkIcnHtLue2n3ZApFR-IiRZem8YP5baD7eBN1ze9qOLetDjq_HL19Gkp2iHVDEtThkSXg1kgdgCquXqTuwzpGOYm9PzHw4whLJ_1vOh1TQLf9MTCyA-0xWSeHET24IKYbQtGEgeELlQ5xcIvBsF27b7EtAERp1fLlNnJvUH3m4u9XBaxHu5hYZReUdRjmoakgm_6u_Xs12MvxZPXqNvG8Fn_mMtIIHm5cVF20YOj2s5wT59dSXjwKWVLyx3bbgMLZ6KZJq5vJxgaT1lk_OgSTQodCBDL-61TYVGkHygN4G1Stq9h5JioyYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري يستهدف  سفينة مخالفة على بعد 4 أميال بحرية شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/92380" target="_blank">📅 02:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات في  منطقة عسير في السعودية نتيجة استهدافها بصواريخ بالستية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92379" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الشعبية العظمى تختبر صاروخ بالستي قبالة بحر اليابان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92378" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsAD1mqk3d1eM5bW6J9R2ieQ3gBOX49Fy2u3dywqEEvwgA5c2m_WBZ3m9R8bySaMRD5lQw4y99OR_6ZQTCn2BPQZIqGb4twnM6SLukR3dYU0NtxJrYN3A1NA9-JekxQL9fv41wve6-vGJqwDrs9OVlYnjCYiZ4ZwsRYbv1FFY3C0BO96dQrdv15bn9dguKlZoFIWYcnGj8DaZrSN7xa-iY8b0XXNZWJbbom5XS9dRx5-RaEjX4xXR6a_6TzkL83OCsHQK5Gi7O2ymmuTD0_HC-eQBkjUKvtOC8L9pv3GZr-i4n40HvO0g5rH8CaPxoMRENQGQdJDWzp0tLBzGdcP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الأمين العام لكتائب سيد الشهداء، الحاج أبو الاء الولائي:
اعتراف ادارة الشر الامريكية،
على لسان رئيسها الأبستيني، بحجم خسائرهم البشرية في العراق وتشبيه وجودهم هنا بـ (المستنقع والجحيم)، يؤكد بما لا يقبل الشك فاعلية عمليات المقاومة العراقية وقوتها ودقتها وبأسها، بعكس ما كانت تحاول أن تصوره بعض الاصوات، عبر الاستخفاف بها والتقليل من شأنها.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92377" target="_blank">📅 00:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPISSvMyAlh-LOdOP6VpMhUko1KaOhijn4mCzF3Nwfm0kmkBohlHhYYp7_SUwTRC45QtqteA-PdfbSGY3Hl1AfwZEfq0aWdjoN9RQIXUgx0aktiUHK1ULkeYK6n2WMTLeUMCoViXbFN519VznXiZFdqP6YasloI4mg_rnnKA9y87CLjFdNRjdteWOhfqnre-ZhiZR1ks5pB3SgJu-57_3TW0AGK7WKB-CUU8IMxSp1fJ29TfaHBAcymcZCQkLi16g3fkwMTlNVmImqYFmO00ntf1L81Kz7itLdJNx8pH7yMIyWJpG4pbF255lpnjEvNNr_UthexZ910Pl8mapB1ZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.   الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92376" target="_blank">📅 00:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
🇸🇾
الجيش الإسرائيلي يفرج عن أحد عناصر الأمن الداخلي السوري بعد احتجازه لأكثر من عشرين ساعة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92375" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23207838d.mp4?token=CUecc6KBCVCQTHxQpJmGd8sAEIKMrzoBmeYUtwng8b2iaP8yGJlL16GUAoZc5VP_FBb9vugmmJUuWa9rTX1tSL2oEk-C5JWKsonSy6o4hGLYHbbx3ZOsPi0kT6tuLXMQ2G7jW9NZwsh9ptWm6HSxh32gZCg3gttd_8JTUxy_I7Q9kDOLgU2J4VhSM1Za1EemdL3RR9PwYHGZ3ezY4iuMmPMe5uQhg4VFgW29z-zA5qOLsgGMd5E2chUR31-b4tn9FHlzXl8VKmzGxRCgJkDp30XZm7XKf3VcuUhquueNpganHBf3uwSzxVALQ7kX5wZmuIQUhav5_l2iquAcoIIc7VW82Wm7AUpvICB8oSmAyL_xUqvTQ3MY5VrehwHbPSg28crM_xnWQWY4yDI4BTrtJojNZRqzhtZWz6YkYqUcGsDIdFOY_oo2QzclHc5xl-Rt86LCEUiuu8mBI9jWs3zfHOxm5L63mzomKRx6t07JVbRSZXQtoK23d8_6TDXj6ZYxTwjTpgZ4xHGO1Gc_hvF9S_4WJomIubtzkEKNIKUSf10oBst4FXt4lb_1hc_Ak72x1PpdJ1rSG703GVGPag2vo2o3m8u7gHGkpxWSq9TVvuk1AQwftuI6yNVCfTjx0MkMYg3LJc2mXgNg6iZJgDNiAaMlV40ZD4vDTouOi1uRYfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23207838d.mp4?token=CUecc6KBCVCQTHxQpJmGd8sAEIKMrzoBmeYUtwng8b2iaP8yGJlL16GUAoZc5VP_FBb9vugmmJUuWa9rTX1tSL2oEk-C5JWKsonSy6o4hGLYHbbx3ZOsPi0kT6tuLXMQ2G7jW9NZwsh9ptWm6HSxh32gZCg3gttd_8JTUxy_I7Q9kDOLgU2J4VhSM1Za1EemdL3RR9PwYHGZ3ezY4iuMmPMe5uQhg4VFgW29z-zA5qOLsgGMd5E2chUR31-b4tn9FHlzXl8VKmzGxRCgJkDp30XZm7XKf3VcuUhquueNpganHBf3uwSzxVALQ7kX5wZmuIQUhav5_l2iquAcoIIc7VW82Wm7AUpvICB8oSmAyL_xUqvTQ3MY5VrehwHbPSg28crM_xnWQWY4yDI4BTrtJojNZRqzhtZWz6YkYqUcGsDIdFOY_oo2QzclHc5xl-Rt86LCEUiuu8mBI9jWs3zfHOxm5L63mzomKRx6t07JVbRSZXQtoK23d8_6TDXj6ZYxTwjTpgZ4xHGO1Gc_hvF9S_4WJomIubtzkEKNIKUSf10oBst4FXt4lb_1hc_Ak72x1PpdJ1rSG703GVGPag2vo2o3m8u7gHGkpxWSq9TVvuk1AQwftuI6yNVCfTjx0MkMYg3LJc2mXgNg6iZJgDNiAaMlV40ZD4vDTouOi1uRYfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92374" target="_blank">📅 23:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇬🇧
🇮🇷
‏
الشرطة البريطانية:
توجيه الاتهام إلى إيرانيَّين بالتخطيط لعمل إرهابي ضد الجالية اليهودية في مانشستر.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92373" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
ترامب
: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92372" target="_blank">📅 23:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZmAT8J_BQrS8aQzA-NZPCjTlm9QFKE_kPT4NwcZTtVYub0eS-Sc7NkVAc8CKEQ4O3enAqhPRFn1EiBKRdVH7F70LlnwXoUJrT9CDV-z6lUNf8Nc04XkzqWDC5Vl-pKQ8rWtEbAqzstfNeRlSm0w_97NQFdu6m87ikq8ALTgVXRpPrYoVtvem5gqDeE6C-YdHmq3i_L2liUqZqFqKOVcu6XgHdXUM6mxnPJOE5JzAPmt2WNOK-NgtquU_iiPsIheD3mfyDL58EYUCX7oV2MJfg_79abPyY4hMmsKiSBnVv5w5pGLARHLV1RaK8gUKBIfNh7ce-dqA2ShfAmzkEDNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب العراقي محمد الخفاجي: كتاب مرسل إلى وزارة النقل العراقية يبلغهم بإجراءات الجانب الامريكي بشأن العقوبات.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92371" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
الاعلام الاميركي بخصوص قضية فلاي دبي:
عُمان منعت منفذ هجوم فلاي دبي من السفر بسبب آرائه المتطرفة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92370" target="_blank">📅 23:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhFDzOJoH__iFEDt8Xr6OKm67CLiP_dn-_36fz3DfM0Gaf_yQRj9wt14CDM6-GXVgxgv5dnQ2n8MZsqcjaLXICNp_dHn83zBJ3CYT1zj4w1dRjmAfQx5vVfkeCZBb8GlqPGyuusb-1R6RofI0uPY5XrBo5LARa39M4kabIurlOVjoe-E08gHlP7mNgt5m9KNRA36RGdKJz8eZ_aVSk29AQ49uF5scVGpS-uqmLL_m9TRdcG1aiPhUeXCTqjnQ3vN5hGYQEVhK-S5V0Be5WQ8NA7KnOo9QBspB4xiq5qBN1lxcHOA8J9Hzf0rGsu62H6F6kE_5D6ySE9Zj9tSejqx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92369" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92368">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92368" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
الميادين عن المقاومة الإسلامية في العراق:
رصدنا أمس 4 طلعات جوية للطيران الأميركي في أجواء العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92367" target="_blank">📅 23:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi6GtA-iGspRrLsQo94HDRu6JX-1b7PxBx8vsXQDnooBWZY-3X9tOOHsm9OBo1Y56dK4AMpNmzK-FcBwpQKuH0_VXDL7YDkzQnFVZVD5QT941hdG3PfvTZY7cT8a5MRutOhBONf_kav9P7g975Dyr0wNkKrWNhekMbl7awNVDhb4MwkBAr4oN0WjqBA9j6_EIWmS0KLLgJAiTECpgj20P_jb6diECrcF9HOAwRwsPoyMTtWNgkyEPdGlCPTXDzCQiw3LqNNwRBqTgt3TEMUrXMeREinA0pCNNDzSWBVX9dkBlkZcgTl9zwnm9puqu8U9k33HTRj5vo5jweDnawwSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92366" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92365" target="_blank">📅 22:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇷🇺
زلزال بقوة 6.2 درجة قبالة سواحل منطقة كامتشاتكا بجمهورية روسيا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92364" target="_blank">📅 22:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
🇷🇺
الخارجية الروسية:
نرحب بانسحاب القوات الأمريكية وقوات التحالف الدولي من العراق، نثق بقدرة العراق على مواجهة التحديات وتعزيز أمنه واستقراره عقب انتهاء الوجود العسكري الأجنبي، الجيش العراقي وقوات الأمن قادران على تعزيز القدرات الدفاعية وضمان الأمن القومي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92363" target="_blank">📅 21:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwuRLin0y819xFUSCJqXxdVoO7avGi_FCz1AhPviSMA_-Diiaq8u0Lvc3a60cLgfR793XnvTXpBe_rC9MxMv9d1xqH660tb0CPD4UC7kYJWaQpt87k18xdqekchFCLDdSzAxVYgmhAfuY7e6cyHxmnn8TeDr__yhLh3Azj3elC2z2yvSxISOpRqxx1pzKmQgEFTsaOy1FxBYSZr_id-tQfZfazr2K49FS--KW0HKZ1gtzdglT4uNd3QAMZzqrlu2gkW9ycW1AY006uKtasrSzPGClFxFbRThsH-G-xDoc6WcNXTI7YgvadGRXIQBr5vJ8jz7piFJ31FIYaWNe3TY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
اسعار النفط تصل الى 102 دولارات للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92362" target="_blank">📅 21:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
إطلاق نار يستهدف ضباط إنفاذ القانون في طريق جونزتاون بمنطقة بينك هيل في كارولاينا الشمالية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92361" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
شخص يقدم على قتل اطفاله الثلاث وزوجته في قضاء المجر بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92360" target="_blank">📅 21:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇸🇦
🇵🇰
رويترز:
أن باكستان نشرت ما بين 30 ألف و 40 ألف جندي في السعودية للمساعدة في الدفاع عن المملكة، وذلك من خلال اعتراض الطائرات المسيرة والصواريخ. وقد وصل الجنود على دفعات، بدءًا من العام الماضي، وكذلك بعد التصعيد الأخير، ولكن لم تتخذ باكستان قرارًا بإرسال قوات إلى اليمن للمشاركة في العمليات القتالية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92359" target="_blank">📅 21:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92358" target="_blank">📅 21:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇦
🇾🇪
استهداف خميس مشيط من قبل القوات المسلحة اليمنية بثلاثة صواريخ باليستية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92357" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
يقول المحققون إن مساعد الطيار في شركة فلاي دبي، المشتبه به في الهجوم، قد التقى بشخصيات دينية. والتقدير الحالي هو أنه تصرف بمفرده، بينما تحقق السلطات في احتمال انتمائه إلى أيديولوجية تنظيم القاعدة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92356" target="_blank">📅 20:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 94 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في محافظات صنعاء وصعدة وتعز وحجة وعمران وإب وخلفت شهداء وجرحى من المدنيين، وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان .
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1350 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92355" target="_blank">📅 20:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgxqbQrcWi6FZ1V62FTviIbQExvT9AvYSqm6pUbZukzAgYA_YUhB_hBm21ZBpEL8uXRw94y8vMUu3SnogmVykb2lovyX9_qfPKWn_ayvVIor8bPXhO9bHZYwyxShrcGcymiMM9etDvaAMTfWmIHG96OL62t0fZn__Naqjm2GPTL5gaB9aoc73LQjcoouRKMgyydcOy1VFUyyH9VAzzncv9-SgiekFtRCAKdgaG22h9MoHn1rJfQjMoPtnwIE7wvmgPHNDDBDpTvEyZW5jSUx4AStHyL3L6i56006LvTbeDdc2b05ZMbgYif33cSgeoH4dap28Rlaf94c1hsluIBVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92354" target="_blank">📅 20:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX7MTaTqiLP8mGtS204hqlTTpiIo4LgoVFyjqgNnhgyEnN1ewo6gFEgXiJJ86XvYdxkbPu4T1WCX2wW0P9Vxvaoo-8qaEVav6kWpvKHLeeCjAIO64qnbFPM2TrrEYsRgVmezX648qU-22ykJImrl1DT6wdZfiWKMV9J9ItPztRhVwq7YAMJDUKgbomTiME2PzRFcRqwvUj546R2mRsNMMROpaunyYXG31GFgW_rA64zovUp0Zn0PZP2i1uhcdPn9Ezo37M-bsyGZWOYCg7wvdr7SZWTiG62ntt8jwXfMbzSaiWbGN88IqnQlbz6Y8qpZUGv-Op-emECuIpNjrraS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🔻
بدخول بريطانيا رسميًا في العدوان ضد اليمن بمشاركتها للسعودية، هل سنشهد تصعيدًا أكبر من الجانب اليمني خصوصًا فيما يتعلق بمنع الناقلات البريطانية من العبور عبر مضيق باب المندب؟!  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92351" target="_blank">📅 19:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94d41695f.mp4?token=BsbtJZMJyjqZk0RzriAfXD6MuShTpVVQLtRq6q_Mkr8tB9oeipIY2RO700FAb-8rgBFdI_5s73IvhJkZCtFD4fAjvUtntaAdrjxVijrhcvnmI0GZ1gga7FfzZy7AMQbjwPEqkdKd84TEq29ZidW5k5WjV_O4vn4Ase_qLmL0x_3LAbIXandAiOMU53mqcsyLUS6datkcx5dql2XM166mJ8o_IjqjCoadrVmrzdxzAKlQbW7lU10351_kXxwV0nO9j7YM1RnTt7Dv52dktDB-0BlkWCETRvNrVbV0XU0TcKAFi4uLjqxYco7w7kDRvyylI5IXsdthe-Rq4c-7bM6SSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94d41695f.mp4?token=BsbtJZMJyjqZk0RzriAfXD6MuShTpVVQLtRq6q_Mkr8tB9oeipIY2RO700FAb-8rgBFdI_5s73IvhJkZCtFD4fAjvUtntaAdrjxVijrhcvnmI0GZ1gga7FfzZy7AMQbjwPEqkdKd84TEq29ZidW5k5WjV_O4vn4Ase_qLmL0x_3LAbIXandAiOMU53mqcsyLUS6datkcx5dql2XM166mJ8o_IjqjCoadrVmrzdxzAKlQbW7lU10351_kXxwV0nO9j7YM1RnTt7Dv52dktDB-0BlkWCETRvNrVbV0XU0TcKAFi4uLjqxYco7w7kDRvyylI5IXsdthe-Rq4c-7bM6SSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تندلع في العاصمة السعودية الرياض فيما تكافح فرق الدفاع المدني لإخمادها عقب الاستهداف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92350" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe53e872a4.mp4?token=utSJvWd_QlVHssi8g6YXdjZkN_UbSK05mA8iYSnfDlLh0_Zi1sfcOIq4I8glXYPVBkNO4bx5k7-1gq58zzhkgb1u0zuWUqi06lS_iq8prumR415EvK-PouDQQEaL7AtUU9ThArMKwMwJhmVb8MVbq1wky0nxM75wTpvE8QE4Y0Iklq6rIOnosgUlAuM9H1eJ7GiqftFBV0XqS4XMkyO63icDF6Lbz2hCHLSLlq9HDdAri7FyfJ0cBzrcusS2ykeLVDYF3emcg80JcgP-5hhscFQL5rA7gk6LI0wVMIYX95UejIYWkxHjSyWbPNtu_KuQiFk4FHyv9rxu7M5Agsmm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe53e872a4.mp4?token=utSJvWd_QlVHssi8g6YXdjZkN_UbSK05mA8iYSnfDlLh0_Zi1sfcOIq4I8glXYPVBkNO4bx5k7-1gq58zzhkgb1u0zuWUqi06lS_iq8prumR415EvK-PouDQQEaL7AtUU9ThArMKwMwJhmVb8MVbq1wky0nxM75wTpvE8QE4Y0Iklq6rIOnosgUlAuM9H1eJ7GiqftFBV0XqS4XMkyO63icDF6Lbz2hCHLSLlq9HDdAri7FyfJ0cBzrcusS2ykeLVDYF3emcg80JcgP-5hhscFQL5rA7gk6LI0wVMIYX95UejIYWkxHjSyWbPNtu_KuQiFk4FHyv9rxu7M5Agsmm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تندلع في العاصمة السعودية الرياض فيما تكافح فرق الدفاع المدني لإخمادها عقب الاستهداف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92349" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRHIA3A-IBiuaK7w43BFapurr7fM0twEYHD8gZIB8IDY8RrC3As5R89W1XN6wV6ES3fiVuSgpGci7hpv8udzykezX0xr0vQ4h-qevJikTa6eWWu808FtLCKxhliWUB5Cew2P2NjH9tLEpN-6YhkFOemErvR9deOT1-gaJxYbm-oLCATFUuOvA7tbcjpFmd4D3JNeD33UXvhW6clmeYEayT9lRLyaJ0ZbOrc1FXa_EyvNbkzNDULrguSOB3kR3ul0g4317RubZ-uMrTjbjp6k1x9mhxglinHeK2zZpmBpPntrUUItZ5Gt5DqgJsPKP3BlJvO9ZNY6YEwfvTj72w9-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
منظمة النقل البحري البريطانية:
ناقلة نفط تستهدف بصاروخ أثناء قيامها برحلة مغادرة داخل مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92348" target="_blank">📅 19:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52317416f.mp4?token=k0J0wsBrUANuUzEDf02AhVHqFnWg6ovsFMXZTqMKqkQz-cbwHzWNPh20x5EcmbDdlYcWjpLzzOGilF6Fpw8Lb5nhSLFNTSYalW9dg4LbTZOykQPyUeWaF6ujI-yMrh3P1ECiKgyF-vR5pb62XO1GuwCaogM9deSX78iRaPqmkn99CywV_18HT7krB0iDR8-4hTd97kxYQhOtk9lVxjP5QpGhkpWyKcn45g5NSCEx3H9c9ONW8o1EtsFeyhW0cBw0bR9Dyh6xkQB9Ix4HkZF5K3hYC_3RRV7PkMv2ACvqOXpOUphj5yee_2yW3UcXtDvufvpx_oC8xO1GXLGgyQEeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52317416f.mp4?token=k0J0wsBrUANuUzEDf02AhVHqFnWg6ovsFMXZTqMKqkQz-cbwHzWNPh20x5EcmbDdlYcWjpLzzOGilF6Fpw8Lb5nhSLFNTSYalW9dg4LbTZOykQPyUeWaF6ujI-yMrh3P1ECiKgyF-vR5pb62XO1GuwCaogM9deSX78iRaPqmkn99CywV_18HT7krB0iDR8-4hTd97kxYQhOtk9lVxjP5QpGhkpWyKcn45g5NSCEx3H9c9ONW8o1EtsFeyhW0cBw0bR9Dyh6xkQB9Ix4HkZF5K3hYC_3RRV7PkMv2ACvqOXpOUphj5yee_2yW3UcXtDvufvpx_oC8xO1GXLGgyQEeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للحرائق في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92346" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92345">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية:
الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92345" target="_blank">📅 18:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92344">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مشاهد من الرياض بعد الهجوم اليمني</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92344" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsrqoN1QKXNEwypLfXj7TTYYXpOq4vvUb085ZkNTD37PKw0o_pA_GONMS1Ri872izARG78YW6QwJ9j6PXon3g534iUFksLZW5SBgnwn9DNgNUxvwtwYjnvsZqd9mjXWPfmTcz0ZePA4MXFmOsSJN3kaqbx_L7_ltoc8hvFujnb-kNh6Xs5YYwdZ9gO8WxX2Vo6GGYXWABLAVlJcZjv8f8gOhrDurdEZXIKPVwZsKHrzinQz1qWQp-h_e6whyQSdJLoV8ppVWwfGiC39bZT8f19bq6TmZhby5_2pAZMlfHqYHV4W2KEun3sSB-QIgaYr2rbJgZ8k0ReByhCFpe15Uvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇷🇺
روسيا تعود للعراق بعد الخروج العسكري الأمريكي
اول عرض لفلم سينمائي عراقي المنعطف داخل موسكو منذ عام ١٩٨٣</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92343" target="_blank">📅 18:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرياض تشتعل بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92342" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مشاهد للحرائق في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92341" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92340" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=Nf_jBzywVqRHH0QtS8NPa0s52mEvEIGYzp2Uvoeeg1SMKtLXEciSWob9OYsF5jMktoLSQMU96cusjvUF-OzSJa9OATyr9dE_aYynj_TL5oeJCwWCBYK7rNzblzqcUXxTfT1beYTajoFoWjSC4ogIagu3oUEtOo1moRuIev-ySJfO7vQegQKRd1tlJt4KHCL6DLSZYseW_IhVxEzZ7Nve77GbxKdO2mood8sH-xjbbjpWs_cIyVahqXjms9J776jpHNOX1K9tRXpqDCrpCkBRQkb3Xm0pBpDS45cBfR6mqoUwdGytKD4lcmgrMaxBjM_8w_I7weE0yDNhiojTpxkzpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=Nf_jBzywVqRHH0QtS8NPa0s52mEvEIGYzp2Uvoeeg1SMKtLXEciSWob9OYsF5jMktoLSQMU96cusjvUF-OzSJa9OATyr9dE_aYynj_TL5oeJCwWCBYK7rNzblzqcUXxTfT1beYTajoFoWjSC4ogIagu3oUEtOo1moRuIev-ySJfO7vQegQKRd1tlJt4KHCL6DLSZYseW_IhVxEzZ7Nve77GbxKdO2mood8sH-xjbbjpWs_cIyVahqXjms9J776jpHNOX1K9tRXpqDCrpCkBRQkb3Xm0pBpDS45cBfR6mqoUwdGytKD4lcmgrMaxBjM_8w_I7weE0yDNhiojTpxkzpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92339" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1SXxipO0ds8Sr5zMG8TlVwGqWI2-Njg91NVEsMeb-jgP5IEFizc4yF_ReU4z9SgNKNbD7DLKaGaYeBi_DsFLMbaQUw8l3eLOTBHGqlxgOY2mwMp6Bj9GUdO6o21_ZdNC3ExGjM_SPNHAL-RkxMCbNwaC2AfdaCMouqCUNtQyXnRnsUDHAhesqgn2ke0it-GWw2kWDw7_ECshdpDJxS1-0jJc_uZkNygChMgblPOVVhE-xvMLZWzvNPOvbuocxEhTRqJsKLlgrTwN1ildHHGhtesOwKr85L9aOX2PbJ4UbAVQb6eN3wAOQvgJjbPyH9T_-T5noXPbV2wh5Net11VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐖
🇺🇸
ترامب:
أوروبا وافقت للتو على إطلاق كمية هائلة من مخزونها الكبير من زيت الديزل. وستبدأ هذه العملية على الفور.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92337" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إصابة ناقلة نفط ترفع علم بنما بمقذوف وتصاعد أعمدة الدخان منها أثناء مرورها عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92336" target="_blank">📅 17:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
مصدر يمني لنايا:
طيران العدو السعودي يبدأ بنقل جثامين وجرحى الجيش السعودي عقب استهداف مقر التحالف في عدن من قبل القوات المسلحة اليمنية بالصواريخ والمسيرات مما خلف 17 قتيلًا وجريحًا سعوديًا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92335" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=Pa9EBsUWuOL8wHUoQ9rDS3SssY9rIENV-NCOvRkAX1NO3sY2Sw2qcOBNKm_1yBDM4DvYnDMZAsSxDibwlsXxUxhULRV_W3sOcVZI5Px9mwuz6Vmxj00bsCdd4HZmwIB2_AFtPBMy-iEEgtMl5JCS7uCq_oQIVpHx1Ogat1MCNOZnMO9u9MFzaDXqEntrqRVvuAuU5FbJB9CkuuenIiQyX8AXdri1VTZgldoc0K6JMR9XEMoUHZoasanbazaaY7gdsUU_0GYLCQ0xmOatFTKTfuPNsM5ccnAeaklFwgYzSARrQM6A_CJBDVWegctl2A8CxuQVhUjg9pJEdA0dxI0kmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=Pa9EBsUWuOL8wHUoQ9rDS3SssY9rIENV-NCOvRkAX1NO3sY2Sw2qcOBNKm_1yBDM4DvYnDMZAsSxDibwlsXxUxhULRV_W3sOcVZI5Px9mwuz6Vmxj00bsCdd4HZmwIB2_AFtPBMy-iEEgtMl5JCS7uCq_oQIVpHx1Ogat1MCNOZnMO9u9MFzaDXqEntrqRVvuAuU5FbJB9CkuuenIiQyX8AXdri1VTZgldoc0K6JMR9XEMoUHZoasanbazaaY7gdsUU_0GYLCQ0xmOatFTKTfuPNsM5ccnAeaklFwgYzSARrQM6A_CJBDVWegctl2A8CxuQVhUjg9pJEdA0dxI0kmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعراض جوي كبير لمروحيات الجيش العراقي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92334" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتنياهو: كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92333" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتنياهو:
كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92332" target="_blank">📅 16:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10465af39b.mp4?token=r9_BQrxpIsSVnEAaO0Z0G9qTZiyeYn5Y6w2-xWXZAaI5jN-2opNiF7VNLgxlCABXADJYiWsney3IkT24mdX-0eMyvaO39EPtdzra3_gmHU0s-y5pGpc0Yg2vuZfQ_5kELa9e1B8JFQWcbHSjlCirmjISHJKhDOXsfikpn6JG8Jxmdlh39vq4KkseMgz7VWJ2-iwtH_6ffvtKX-LR7A1p8A0vNAWL3SxJcpZzx3mXYr_iZM9CBZu4vIfh2xJqv5PBqke2B64VV22BQ5NHuiyvnQfVWqQBM8jzWoSAToW-ykEQE2PeFRpJ9vThNrBxME3KsoNP3dKM7YW7_skrzEVcDTIhduH2lHZX4ytnwc8Y0KlGmjeB5OCc6ZnPKdgN0TgEahR-13Tn5T9nT_jDO_mv26DVBE1qq0DcdRVU_aUmr6UFSl-2yIAsvwmvJXw1oMIFhAN2rH2xh4aLSbbQLQcXNNqDynh8rMrH5XDqJpjv97vGnFKu4ATcoLmfXJ7OFO3e_K8rsqSJ7JCg5Hdn_9j0TEA1eEJbOixRZ9ApHwWiVuzqX__6Z8tEXIzVCOIi-NgrefIVzLjG1wo76lBh8zNBouhTTHlWt_-8nBiH60FOw5HNm4E4yjjJFvzSSm6TG2zN87hiXslVivVRODYilg-DrV2NJTx2j5-0nDTbUdKDjcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10465af39b.mp4?token=r9_BQrxpIsSVnEAaO0Z0G9qTZiyeYn5Y6w2-xWXZAaI5jN-2opNiF7VNLgxlCABXADJYiWsney3IkT24mdX-0eMyvaO39EPtdzra3_gmHU0s-y5pGpc0Yg2vuZfQ_5kELa9e1B8JFQWcbHSjlCirmjISHJKhDOXsfikpn6JG8Jxmdlh39vq4KkseMgz7VWJ2-iwtH_6ffvtKX-LR7A1p8A0vNAWL3SxJcpZzx3mXYr_iZM9CBZu4vIfh2xJqv5PBqke2B64VV22BQ5NHuiyvnQfVWqQBM8jzWoSAToW-ykEQE2PeFRpJ9vThNrBxME3KsoNP3dKM7YW7_skrzEVcDTIhduH2lHZX4ytnwc8Y0KlGmjeB5OCc6ZnPKdgN0TgEahR-13Tn5T9nT_jDO_mv26DVBE1qq0DcdRVU_aUmr6UFSl-2yIAsvwmvJXw1oMIFhAN2rH2xh4aLSbbQLQcXNNqDynh8rMrH5XDqJpjv97vGnFKu4ATcoLmfXJ7OFO3e_K8rsqSJ7JCg5Hdn_9j0TEA1eEJbOixRZ9ApHwWiVuzqX__6Z8tEXIzVCOIi-NgrefIVzLjG1wo76lBh8zNBouhTTHlWt_-8nBiH60FOw5HNm4E4yjjJFvzSSm6TG2zN87hiXslVivVRODYilg-DrV2NJTx2j5-0nDTbUdKDjcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92331" target="_blank">📅 16:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=uFypJpJbTExjmbM24dE-S2KArE7pShU1kyJ1-RL3ifoW2zj1HZutbZQ-WQ_23xVuFVSU0iM08jSMw1m3DYRRdt_RSO5cDZ7ERARvulgd7XVU7_3aEN3b7b8hUbHntj85gCZgFFWvWc81bAcyuTNEIOKIyUhZQw2ahDIFW02ed91qGLvwo2XCnrIm6aEY14XQUbxpO5h5hBPlDKi3RkQN99SHv6IwQvc00P-zvaQ7BdDhpABJprBR-TpyN3P3XqBPLDBkcvGJ3mBZ5PTbutIDVHmsChXb0UlOUiskwIqEb2tHDMeQzp4WVwi0OrZ0FETljIUCfKVFo70Io9TKHaGTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=uFypJpJbTExjmbM24dE-S2KArE7pShU1kyJ1-RL3ifoW2zj1HZutbZQ-WQ_23xVuFVSU0iM08jSMw1m3DYRRdt_RSO5cDZ7ERARvulgd7XVU7_3aEN3b7b8hUbHntj85gCZgFFWvWc81bAcyuTNEIOKIyUhZQw2ahDIFW02ed91qGLvwo2XCnrIm6aEY14XQUbxpO5h5hBPlDKi3RkQN99SHv6IwQvc00P-zvaQ7BdDhpABJprBR-TpyN3P3XqBPLDBkcvGJ3mBZ5PTbutIDVHmsChXb0UlOUiskwIqEb2tHDMeQzp4WVwi0OrZ0FETljIUCfKVFo70Io9TKHaGTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92330" target="_blank">📅 16:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">المرجع الديني جواد الخالصي يطالب باستعادة أموال العراق واستقلال قراره: لا خضوع للإملاءات الأجنبية ولا حياد بين الحق والباطل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92329" target="_blank">📅 16:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=kG0ScHIPeld6BWDEpfGN2zu6QrDJxAjcFRchXTjb9xZMs9ThoUnox6fRX4NDU4j8nJhhUJYAcn_sPJUVqtHKkHzg4R89DlOaU70ItocQVvtp_pijkolm5QXRSOb9itMlt3zPcQhHjHNxSwTzpLMPHaw2ruRTq0B2GmWaJdA-1Xgi5lKRAHrVLDaL2zmSW4YAycpJyab1NQOxBe9T-UtfJJxjVTZ25U4OCDnY5Oj-2ardoHchBQ_V1VRXsSFjoEyT7iXQ_bSW29tnRVNCEfhrLO5TjxnsCNuRjm_3N286XRkVKEphD5pDmqczM5cZRiBI8CT0FL1Y7W6bXpQwEk5xJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=kG0ScHIPeld6BWDEpfGN2zu6QrDJxAjcFRchXTjb9xZMs9ThoUnox6fRX4NDU4j8nJhhUJYAcn_sPJUVqtHKkHzg4R89DlOaU70ItocQVvtp_pijkolm5QXRSOb9itMlt3zPcQhHjHNxSwTzpLMPHaw2ruRTq0B2GmWaJdA-1Xgi5lKRAHrVLDaL2zmSW4YAycpJyab1NQOxBe9T-UtfJJxjVTZ25U4OCDnY5Oj-2ardoHchBQ_V1VRXsSFjoEyT7iXQ_bSW29tnRVNCEfhrLO5TjxnsCNuRjm_3N286XRkVKEphD5pDmqczM5cZRiBI8CT0FL1Y7W6bXpQwEk5xJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات في مدينة الحسكة السورية: الاكراد يرفعون رايات كردية والعرب يرفعون رايات تنظيم داعش وسط مخاوف من التصادم فيما بينهم خلال الدقائق المقبلة وخروج المدينة عن السيطرة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92327" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elSFjzCj6HKpKWaMedZiPaa2PvVZVKI5wwHdX190uvifgb6dMV2aq_ybB_y0L9Hig-4KZ-dkgO6MorUCPAGzoTyx9Shck-dbfw_mm21bDWcwUPLCtr-n8rOpmk0c0z9bKD5sI5_1cduv1aCS9uUYWMQjQzKFcOj2YRZ6uZHUEKE4oTnPX815NzPmWRf2IbaIv5FZZEx9-Es0XWTtsTKxd5cTaHbpjWvcfmaL-6Rt6xAofvhYOKdUDog9NmeHU4hKkA5P8ZTgovrwaIE1koIq2-FKn4JN-qpLIRivYh3X6O3rH6k0B05zl7QmzHxvessero41YDyS9Jgc3GXUfRtgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب يوضح بخصوص عملية التون كوبري: يوضح الجهاز أن العملية جاءت في إطار واجبه الوطني في ملاحقة العناصر الإرهابية وإحباط مخططاتها الرامية إلى استهداف المواطنين وتهديد أمنهم وسلامتهم تمكنت قوة من الجهاز من ملاحقة عنصرين إرهابيين في إحدى المناطق…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92326" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
القضاء العراقي: السجن 7 سنوات بحق النائبة عالية نصيف بعد ادانتها بتهم فساد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92325" target="_blank">📅 13:38 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
