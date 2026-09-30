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
<img src="https://cdn4.telesco.pe/file/IFGohYSVqMW-9wqVmU-P_GkRKqeLmVWqn0wQS7Q8P9GTrN2zPGfJlpcNI0KY9ZJ-1WG3napKAPuqzzwD9PyD3vHUwzdPbVe4O2lhSJE2bPxaHY3jwHb16-WnaJkH6meWnJsGFqdtFS4k9b0Xf1HW2qSn0HMGw0Y-Uu16eU8n-V0-SnbAocpkPngNzZmmUJfIDdkSIg5rQNAh0qzHvE2pRbFEKekK_35dyh6t8E6IDZJW8DdX2PM9_l_lBoXQQNs7pmAdIbczQdLN9Q5BYHo0lpILm7frXrD-xNJ6RCSBJbDgiTQkkGEb2r1Bsacci1LNqAzphnAlIze2kH9eTO3DSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 434K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=jf7fxEU0SRI0Rk3BeJsidT45SNVa97yG0bkIA5fPlvb0uMom8CENmF34UwdauMwjJLf8nwLbiVDxwH0xpE7ldL615Oh9RJ_Opow3Rco375gry-Ggbzb9ISYyRchlycO0MgZYsyWbpnAOGAULmx9lYqyt4Ii6Du6c0boszy81XdB0Gi6K1g-VNu7SQonjhFnS_VBsQLQthY3pNspxo09TjYWSd_5GFnv6GMEpf9bba9IYtEGjksgw1ZuBzytfK9Rb7w5txW_pDxHqznaYY4OszYOvdk_LeHtZauQmTKqlav0Q1MuV_SjAY8VctlEfE3VsNkyQpt6_J1mupUC7o4yHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9UzV8aX34N1ILOj7y8PZTPq1gBmd-S81XYyRZii0BSi3zlmk0hGPjP4MiAcLfQ6ynVmuCcM914_fu0BPK-TUXwzVkdaKev2hP5fw26lytdUtJbNtkyKj2-lDbRy3mTlijCjwQ6N5jBpZH04plsw3SI1G4cuYP5WdBNpbIjsxsk-JVP_xf75zbrtfsZgVORZYPrHbsueSbDV_C8VnZsyNN6hWs8JhIclZ4pEOXJZVx8w8ZXyYDSYfl4Zzc16KBvRobjOGsdRote0oOpU6wDxdZh1hcztFAw9JIWGRTwOGrL5HmsxGENbIzzlhcKqZ60vqkKB1HPTUFNh8_DNe8sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=UoZsuJn9rSNwa_1V96QrVaeNoyFvI4Eu7V60v-04guKE0cgRHoyCO4hfRAsCbf20TDDeH862yQz7vs5y33LNcU-jxUqsJ5yefBosiVAB-hgFccClMgn2H2HY0mvpKRs6XRBWVvpQzv4GL_kwAaxtJ9HKW7C0zvbfyEZKxgGFH0su-NU5r2joAVDnMOPrdBC1SGROYKElIlDE7AQ5-SZ7xxWZbtDaoqLxSnttU2sgUDTmreLe8qKPGxFPUZOPVmshJjwpvKHQ47gY1JaGvUsxWW4G5lwUG1wm0Z7ajRB4Hm35at5gQsyf4HmPMpDqcTd5xGUEunmS81wWmPYXdPIV2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=UoZsuJn9rSNwa_1V96QrVaeNoyFvI4Eu7V60v-04guKE0cgRHoyCO4hfRAsCbf20TDDeH862yQz7vs5y33LNcU-jxUqsJ5yefBosiVAB-hgFccClMgn2H2HY0mvpKRs6XRBWVvpQzv4GL_kwAaxtJ9HKW7C0zvbfyEZKxgGFH0su-NU5r2joAVDnMOPrdBC1SGROYKElIlDE7AQ5-SZ7xxWZbtDaoqLxSnttU2sgUDTmreLe8qKPGxFPUZOPVmshJjwpvKHQ47gY1JaGvUsxWW4G5lwUG1wm0Z7ajRB4Hm35at5gQsyf4HmPMpDqcTd5xGUEunmS81wWmPYXdPIV2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwjTi6Oys0Jq_LYg21aU1lMpxSyWr765utLYM66masNeJk8YU_gStxApK3WvuNk1Gv-vY7LY2ldwX5SeyoBg1SyGGVqzTYbPDkDzxqRbSGNxS_qcAr33uRU3PPqKUb7mot-SPyIYwduZHDCjiJxCldSByBuhe1E-qdZF8ozfxkXE2Yz83L33J3GCiM3MN8RF3G2USYvt0jOKKwYb9WSm30CyXcyjh0YsUOFV7MZOVX2VqUXAyBo4cfjxxvJEodLBkmG43LQUYq-h8jnkkBeKBi5N-Nnn9oOQKbHQXnyNVTs3hQAUIUjBT4PRRYHwB5O29qbACIgTxrkluPbVkIIjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/persiana_Soccer/30748" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz3xoEsEipoPRkDcjIqPl094cyB0Hs4xS_8u0krimTCsgXZqo2mtGr34TQx0PjDj0gTTRA70SdvYU60HxIi944UMy4PBX6_L-e_yae1OHyWzNRn2NKFm6kPS6bIt7p-3KjFk8PNh9IwIUoA4R-gh3WJkR-UPyL49hBP5JlHCwaT7IrGHQf6DasIhoG-PTyWCyX_rumZpn70o0eWe0cTKdYmsgFLxRap67gIqOgaMUoMTvjgJiwAdslYPedoJLlKXFKk7naH9yXfw_P_ArB4liOm4bG8GjTlPCSNdsSbRNrB27-2I0u6HVyj_7FMqe1fXaDU_2eQ2XJ4sJ2ExvjwbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQbdrtn1g1RGLC4P_9Jm0uJgTGj0AadMTEOc8kFgWvHD03Mg0QR1tKm46vMuMpZhjt1lFrAcWINRusQ35hTgglUM-mxBv-izOUHYpkXDILij_K6YX5Dt_bcOxJuNp7g2PtTQ2W12U-Naub4xhmZrC8ZIYgJC8ZFdpUiUXBCzf965LmlVTULd8v3h1sXA8EHJ-6e-EzbVlhJiHDXQBTVYCV0p08pYfalKEJbclQiz4bP1OdG0eizSonvEa_Ivg8ZZnIbyJzthVTZy1z_hf2w3_ztixoXxDk62_xal3psLOFaO-A8nM15wNj5JSyvdk3I8ipQFYVO4vTKorKH5-XMg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU2qM_vBjHwItLFBiQjGvV-qHEIuUuQPkoSGv2dcrApacL22FJ-1qn5q98ak4VhFQXx01IXvx2m7JN5_3l78S4gAl0cKjBgOK5kFhC4ywqR38gkISw1Y0D_BKPeVs7E5Yq7JsPAO66QFN0VLWEkpNG8mh57LGXefDZNlTtLmi6W727OXCjO32zU-YNaieSnP_Or1o3BVIiPHyQPOsEtUMQXPygpT0uvwlHslWRoYK03PxCIEFBKSqjX7Gw4MiCRjIsZ55ohivtwvECZgEaxRq2mn5zegoWX_w7VoSllhv7liOcFk5vO-w1okoxyosB9AbYpvcQW0cwAlzB_1-CBufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQYI3LH1oOvkNU2BYD7GyBYbSBbdSFoBALNRQ7djaFc-XBP63925eRMd6wk7UKxgCoem70nRl3-49znXAmKXfAf9o2mb0T3YO7BvEjg8jHOCG3wvuGtc3xZVvphpd5040RH5byK_WRBO9zmG5j6rIjLTs80xbXxFZV6hd7EYXaQbeFQiuxDqpswzYTrYmTzzJoreANZ684n64k5KE-xPXGrdex0ZL6V8urFON_NRlc4AqaQnH_-CmGWlsJNiQbTw7DTYn5eVGMpofhI7sB_j-VsT-DA0dcH2EbSHazwVntQv27SEkkBVmqtfIHi1mMeeLV5WYhYiaQY0wBlzalXCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4OJ69h5U5YD6VjC2sK2XvP8ohB0LE7RxkASFlrVsskXQPIgHLzG4UZxzHoYD65L4ePtiC5S424_NRMD81UBVkaq-WIiBuScUSxCFkEK3N2fdEsIeaiXATSnFF9dT0WHDxc9Vh3t1vQG4mOoztTgPYCgU8J-hVJ0fWB2M8bvKAMqpy5fBypgErFTglkrdN_C6b560I0HHe_XEhUNv0_I9ClHEwjNb-TWRV9sIEpUAGGurQGdKQs-TAEaGGzLH1fVteAAEcjCtAcf2e8V4pu7YOQPJlwTeg1mgxzAshIvVPVyahA6Q7Dw_EbXJM4qPC16yChw5FwmaHxeAaEFgF3LSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZr7jp2KM4dQuzT9c7NRN2SYmQvKKevGf3tENlKJvRwphT71xZ8oG97XGNmojW-S_7cS92NKMVmkTCF6IOXqJAL1K03r7kuzdRjfLDCK_yp0l9KUSL-fZxSdC-Njfgk7uhwPe-4U6_L_9krZrfaiP8jo7swIepst9CRGlgE-X4yb0pER1FRJWprV1wcstjEbG2Gz49beF5maxxUQkQKkrBB1MlFM94B0yxX2pjlxsoaNRT97Z2TjYWjtZniIWuemhREuTZydlVXbY1INbqaXaHGGtwD-ifhsN2uI_Q3LqjOX1LOvG4-mC5c9Qndvc98AknyUK0xSpHv14E3jLkpIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGpjxCwhxoaDCx056qs3B5Rs5ZwHxw0pPONunYvm3KA1IXPyd0LHK4kXnt9Rn---bVi6i4uC12bU3TiKUEDFhuJiHXRmrINxiFv4t6bhG7g3le-D-hLCUtLqE9k5LthDxD4976lGRRCtR3FIzdUpuX6THJOkqo9ERJNK0_irvQVHxwuFEBcKcwyC0PE4yJOzQp3ghv5LwN3SqeUBYnpigw_mU2h5KJgjUde65wL-Q6AUh03Q1jaWkdtE1yVfIAxbueIYxbnl_ZooXtOeKJbIcmJP12Ffgbh6cqzOUuNYoU_JsRFSmtJVSAJVTuN_mIGcLu9-hFiZ_qhEUVhR5bMz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtSNDy-mGXv6zntXERsAQuRYk-tU5PZYDVfTITs0p1DJchVPiUBq_lisx73PI6AVqCOVdC0CzbLM96rWk8LussR0OC719pUYtxRJTJl15HyA_FB3GoJr_pc2V9hkAWwI93qK6-HE9z_K_TinLgu7OMQyxUGzxCqpsii6Of16GNUwRxoxP6Ov_bN7EEMA9HLEtpXUfnpSVCa9vHeQF-uQx_ugcGOlMmYGYIkf2B6pRfhX1MvNSt3TQFdSUfm6mc5AmrhXmjclM4KceSNORANNRfG43fcta5jfi7nB97cLi2ql-gmhrF4XFX2oK7QZ6BLvOnqfn7Xu08mSyvIICAmZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu8ZUFP3wpDcm10F1Lsq-qKbMZ8tJFUSe-4AT51mGdmer0xSQT1lRPCNRPJVGh_4GVqepdpiE-mhcrfoecOuJIuCv2TLQK-v2XHUsgRyiFi2ATroSmb9_7LmrxsVN1XIpVkVRypEmRQrb6nQdtZGA_Zj9f4Owk48cUlws2ukVhi7IqqOmQm8r5yySnK807nemQDi_jJKvmMqcxsw9UZJTW2mzmeqC_N3T2uYG0mUIXO1VPDXGHoGhUWfTn4SQudoqWy70ew71CCG1svaMRz6odr8ku9aB4OXtVjGO9qRKbvZgWlZEpfW4gLBPpnp4XQ06g2tC9I6N0jqb2sbc_mzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ik4zh30KDdFZ6QJFgstWoGjD-6MOozJgg6UhdSCEDq6eInMba_mligs8ZpQ8gYJFw-nrmdL4sDuP7-rwQurA9-CNknhB6-hJ4EmTAKn8c-dK20gJknWqEIW_w1x5ti_b-kyLvdD_wgOfdjTNP0_ccKyscjDEAQRHYi-c9aZ2FPaiR4uO_QOx3MRVjALMxsk3TbLIXRko0FNzIGl1fhDucCZVjIoZd_OB_7lt6mGG7dFqAF4JF4hzaW2frrUM8RQLLtVyqjq27HEZVBV4kQJzT6fDURwUA-Lbu21wadC7YXeiNriG3rxAk9lRenTv11SDAD-axhWl8OXXOmudYQe4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxpPKrm7XMbx03LIoApLg2C4Zw8FQBE3fEwNABbWBlS-rR6y6vxgG83CrmAtwhSr3-ukvCfMfND8xg7mh7nodgyZx9r9HXXSfouB6OZmQwMBWAn5Feh87E-tO1qUnt8SAZDSSc-Lg0KiQTvZNfrawAvlyQsko5fI4az0GAdIUzszpWZLgARbrK_0B1NUx9g3ZvVgQFjAHt4ZcYUboa9kzpJD05GLMGvn227LaQnxrb9B_1Dt19rFk5KPNeMp9tszZvSNFFi7bV8oHMqVatZDcS1WvaVg-FPjbStCLR-Ew6BkwztUv2Fzdiq5Qud4664AsZsAab1ACuOso4FKJP1ggw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVyn62i5eAaa-VeopKnDdq8fZsVO-VeFvuyqTauhylPY36Fug6-DKO1gy-16ejVF9DD30G_5FzM3BTyNqgLdE8Pi0sSXG10WdZFYnslV5oY1fvI4ZoUDZyGkYpwMMSZsM6aw9nNDEN8U8tY8XC0-0C2Q4ctkwDuU0k5vf-jdHNh1rHxA5Fsn4z2oaw6Bcvg8uR6_9ajObTvuva8s17-18gpapKOopuEYg9yn1gFe61HWIE01cvcQKi4ki3iDqX7qfa7fFlCso3FjGhVisIHYkAr7FM_bXS9j0L1yaCD3kY69SxzFz-qRNlcS1_D-9uQ2jcH1Ez9p3jgYIVR4MavmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTn6RtCGGyNtsvWK6Xn0tRrV9qfQUH3vLmCzGMoHvZ9xSigdsRk_jvb8zBUbvAw4pybKeVZ01gTk7VEaXZR-EQ_Hin75JdAKGOo2BHMqmSNYb-10rqHuAD33DECCzO_sXnIEdxYeR1K9MvUL2Mec4E3misCx0HTMCPVVOmK6mD1aNZNzAXuSfxiSdEMm_n1eomceMIa1HBKnsCwQfqhEMH0nynmEW5zYi85aOZ2kbHJb2B7T-xfADMOSkgKieIqw2fxcYqwQrZFZjFgl_RC8y8Qn1g40yOb6VjVXZfuilkgmiS_4HIviHFpdPObiHwlK0aFHawdA5x0KLJEYBFSBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV44Iz-YVSQ_DXW_i3_WV7vU_jW9LRR2JPIId5FKSHV06smFNFT_l166GBvBRISgGoVupvfu-wG1HrLFHrBrbrmf8CKKeQmLjVBu1urBv3HvDSlbG_q-xoKQzSK3cx5dTsC1eMWZf59Ck7bWO3qzQVZeF2OnY6v4FggoK_uMscqH6hWWooxtoK2pAfFIsk9IDSEaAV9c5yBm5Y9CaEGAVKIGfx8wE1-Vb0vClM11dObjMkc8XCl5V-CTitqurZiy7DgAo2lxQL3L2tk830IBuzuy6lJ97DoAsfvl_4ZafdKTGn9rN-bMCEtiAolsQkQAn_i-NvVBD9DkN68lb127Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdtr_NiNt4jPn2ScMEIE4248sOGnFgFO-s5m7WS-zkAk8bctZ4-TfXtLQ_u7BOnboQWo4evoIWApmIvXzJ_vf0D3nkhCD09HHql8ZS4AErN3M-MdSitaDhUys4nFUZlKPuB6Fnt5gvDHVgJZXu4eU74inq8nWyPnrwD5VXdbwzBwj-OLdMuDJYuW0H7zkeE28Vagcq3tFnFFEWfcY-MYkYNjz8d1twSw7d9WAznJuG9Qyh4AQfpvR9sbVVBwN4RbjgLqDeZuAp_KM5vbF33QSWoTm7b2FZ8kvQMiGDndrYSBh8o9JZ3oVP6LmysO_QxGrrdVnuhJQeMV4hRfrdUh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEBDKtyKsmecBPCYFalatWF6Y75oZxaQoGTP3TuSjp8-mySlvdWZM9ALMUv33-dHta9DVCBCKG0yE9tdvTjQtOc_xoFqJnMghPpDyPy_VDJopaL1tu63x8K5tbAIrYzuOeVaiMl8MyOINuq3HD-f7rrSJRiDPDDjxiVo5EosuWAiZKsrzCV93ffUMvpMpf6dw78CXZGYd7mL-nl4hIgwZjRepxVwagRRyVRafmwDkyp3FprkQrgMAuj7FMeP18c9XxoD6ykKr58zzFc6yDns1dYUblg8BS0c0dSvAeI79jCuqn62SEEwUTAmCpetc6nPurkKfLq9AJBn-wUs8oOLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Abepv0N5T_tmkgjBz51EAxqqwaedaJ5pxlLWLZbFHN-IezWsPX3D1SvVO-4C0ur8zv6n7iqE8bn98586yKFtb4Q8yIed3R1ZKmQlHxio7LQNC6ph9Tvn7MPzQWri8YlcPFHd2vls13XpH9YOFhOWGGS58WXtJ8CFwZNgzVFpAI9C5VbR2bTTrXSfSvH6H6vjvgMINNxlMN39vRKlbcoOWm9MJgsg6ZI2eZqPSntBiZiogxj0X3PYqOv3467eQSJGCa0dFyLdSTY_r1d2x2p20qbXBeqbH6ytSbRUEBs7pXkUaBHaXG9a7l4OpejZHSRU3o2Yj0WH0g4AM0xeGnN7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz3Ssv-2QrEn-Px3Cup2Ah_ZtB_VIdA9pPnCfbd-duhUjPYWZ-D4X9iUWtTVK77mtJAzuy5MSQ1upkKXM5e9wRqNQurt4806QVCXhGQHA21ZWEas_3htESwjIcwZz49oU-Dwe6dIdfSlI9HLv_b7gNmM_UN4B3lC2j97BlNOs7X_QCprnOxSQT_r630_A-reaLGU7gL_kntroOX-0eAFpTBjphqdR_oYXtcWm2dhEk3epfxWJ-jwI2sFdK0wlhEkCgoGNbc8eOvQ2LjKzninuluL0wlAc1-hl5CaIH2xyjoybL82Vb2mjAjvYpI3dXScsZ22ueBZc3-GDn2VOUcn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCzneA69Xz6480lRq5cd4pKB_TyvpUu3e0aeFuGJIV2znw7xL7W7ZgXJG-70Upn7Svf1DLMGLAaJvvI4vjDqsIBDZGW9fGcZJxISEdrYuc9xsA5wXmbKA_ZrvmTWj5_ALHmOztHHeJDxB9YQE1RyHhCWp8ahE3rbAse-hHMH7ijX_JfksU6jVwXdqiAJ7kYaW9IImjY9A6dnilRm6qYU5RXSVW179nTiXRBN5fzAKAlAbgE_WA74mUn3sJRMMXJaprcFdUkR10wfokyRx8LwcYQSNjYVzpmwefhBTXIFryGT5YXMlk1yoM4mViQPzdQ2zL0Zo2Yhn8A8hPJUOXvs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=rsK3UyqiqkAVRyLwO0SWiOisOWlegiClIGvzR-1vHSCvB4sHQhJs4qQMSKXpkk_nEfkKcVWYHr8QwnEnmlWqnyi19i616KRcCH7_-5tzNZ4xbzPVoPL5egxBhNmLH0RZx3WLAERrDvGAwWIIXb0GvvkF_-_HoXgOuvMX_kanzObZGeq3tbJdPxeVB1GtyhUl_S41s288M3hzsbOvrArVQpwGRHdI747EPVDU17CqJ2JjYUbMzHyA2L0_o_5StTtz-iCnr_SwvC2dSmIJmr-a8GUhhJsSqXDKcq6OG8ldfBpHKdIVf0DA73K8-bVf9vxA-ezYzxdqnhvh0N_jggNN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=rsK3UyqiqkAVRyLwO0SWiOisOWlegiClIGvzR-1vHSCvB4sHQhJs4qQMSKXpkk_nEfkKcVWYHr8QwnEnmlWqnyi19i616KRcCH7_-5tzNZ4xbzPVoPL5egxBhNmLH0RZx3WLAERrDvGAwWIIXb0GvvkF_-_HoXgOuvMX_kanzObZGeq3tbJdPxeVB1GtyhUl_S41s288M3hzsbOvrArVQpwGRHdI747EPVDU17CqJ2JjYUbMzHyA2L0_o_5StTtz-iCnr_SwvC2dSmIJmr-a8GUhhJsSqXDKcq6OG8ldfBpHKdIVf0DA73K8-bVf9vxA-ezYzxdqnhvh0N_jggNN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQd_igHBeYN2fx5sMWAhWaIGWVGnS72tLKFLG5bzvqoPplhRSZdil1_px47eSxlsyTM-FtrKgNbxxOOBfmYDWaoWiPTMUJZpasS7Lpk4EQdXU6CzB4TxDZ5fEpNiOzerGhw0JZ_rSMYI1uGYxVU_KHh5cTiQeNn2iV6ca-yYdtY0ph02coAHC6I4zIAq5IbWk8zxzf3RtmK7x-IA8HBw8AjCICdCyo5IJ7v50mBC5zbZCp80Wxn_PgeIJbp__-PimnAXNtBZSPIZLA9ieuGzTutxKQgpducDkT9yIN9EAA9TQTMhXCqU_FSJWpd5K8KyarxsR_GK19WYZSD9SZ7r9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzsTSZUh6DcltHlr4v9qDr2H823i_X1fUqqHCCE1BoMpdgq0kG7SNdYNd1oUatI4s8-SPPlBkGrORrwKI-rkRvq1li2c8mS7tnSoDVqX5mArISIkLgLCtx8UEjhgB-gA3-V0FcmAXjjH0PwfNbj-BaFateT-kt1Vi9dCPgug8YiJ4Bei7jOdRBCK4YdP42qSm2nRTVl4q-nKJoO1qq6APtBNfpGnnmITiHdy5UJIlbwFCpWJo5DE_e2ArJXc_IzR2lWFbjEqQ7cVVboadM7Gqrb5mq-tC2c1UE9lDT_YU4kZ22q_2t3bzB1ILzc4ca3BCJGrK7_DOcNFPysaQpkwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOZI4sYRUOkquk236OQsCEINvZ9VOW5arKu0J3D7kBmwQF4JZ4evzupD-uy_4pq1BEO0BTBlrVM4JvPqtc_7Hjgn_bLkXGt4H7moIhslNHFzxvFzkJo63D2oSWohEKarezxJGtx3aUs96LcgrORRKRy12udH5pugb0kzDFUkZ5uCPUouKfDCTaw_hYGbvsWt_CP5WU9a_onlZLHP6q8FvkDp1Sk1WlyUGWBsK3yhY4YCuVxyppOpuFxeVvyrBqIo4MTuWvPAzRAp0MmJ29CeYgqlf6OSjd2lo2XczfhkoemfIVKhDFVhn1zYAvaCb_PUVElniLk-H4Hl8i6OHWMKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG0LbcGhY90KVbdkABWQq-e7qjYAesBUqP-rTnAbV9g4U6eD5BvGqs716wHzEbKx_q6bLy5SJWDAwwDkz-aWeA4g19FO6nC75agApc8cAcDU4w5sZ_Bt_jFhdk3mGr4uLxYZWYNLslK0LI7I3M1xCt7hNHahQJ0YCTAOhAxPCdEB9RA-M8rNMT_WJgHqE1IFlYyA_ImyP1uuW_-Sa2dzgoFWpGx0KpJAgmyE_JP14AponTyTi9KK-MdMXqxKVYP28hCKJdNsasTc_JKV48O9z1xAvsvY9mOfjej_SIZXVNwrnpv8fto7objIc-KsvOpXR7yGFm3q3NV6PiY86Zm8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHBYqKmrGQwLBysgDz0ZbvcZaLqHnq6_5xghcIxBQXPsr5_YmepmmMRS97XE5gMgjdNnXb0E0B8s2WDomkz-RtxpFpoamhR3MihMvPOCWSJAJYTuR-A_PnEblRDDVMB7ecrckysRymnxeROjsshyETxtBI782wp4kEwOPGT9pHCHQMNIowXc3tku5iCmDE0FeSKJPWfTpQxaOtc5R1fd5WzcE18NOycklgtO90W5tGGYJUFDAWt9HykgZDcM2Q3kuaO5b6RN-Fwq8PQyGyygGhflDAMC9_01SelhJY0StVHIUoERKV_ltzwTcEgThi5TXgrMbjt6afT-2tg3P4qcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#آپدیت
اپلیکیشن بدون فیلتر(WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
✅
سالها فعالیت در رده بین‌المللی
✨
ویپاری
🎁
نسل مدرن شرطبندی
😮‍💨
پاداش‌
100درصدی
اولین واریز</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30717" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsjwYVTC-RI5bPF6R16knSyh2Z_Ow2bNvi2MgMvL9ex_J8B9XAZLVHxfUDNzFNV5rN-lk_-JEf6vetHTizoRShhquugQq_s_f1CdaFmV2YdcP2FGFrETekRJ9_P7Gld7eTMXT-EvrQMGRviGp3OKv0ttP5s0Zd8UDklhY2T9mlXXrvEUzNVCD64AXAunPdAngT2fR95J7deaR9Q3fsJgubygHO6bV__-GwHJFWMwcGo_W-swGvJzRHbn8Gj0-2hnVyPkmaHiW8vIv1kblLEn8MvnRt_RzkFQ38S4_lWyeUJuKs6ARC5fmrbWUOU7MD3a9UidmYmPGlx3OUWB5ROQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
میدونی چرا حرفه‌ای ها سایت ویپاری رو برای پیش بینی انتخاب میکنن؟!
🎁
┅━━━━━━━━━━━
✅
4بونس روی چهار واریز اولت(به ترتیب ۱۰۰٪ ۱۰۰٪ ۷۵٪ و ۵۰٪) هیچ سایتی همچین بونسی بهتون نمیده
🍷
برداشت زیر 2 دقیقه بدون احراز هویت
😃
درگاه شارژ ریالی پیک پی
⚡
تا 25% کش بک هفتگی
⚡
هر شنبه 100% پاداش واریز
⚡
هر دوشنبه 50% بونس واریز
⚡
باز پرداخت 100% شرط های اکسپرس
✔️
بونس 1500یورو + 150 اسپین رایگان کازینو
🔵
لینک ورود به سایت(با وی-پی-ان)
🔽
🌐
www.wepari.com
🌐
www.wepari.com</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30716" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snHKHLsLQZ-sMnNoO7IgCrXd7A-RG6H8nn8EcqGgCxzdh9QGQZsKK-UV0FVgv6O7HzaD0v2ezXB0MAA9NVlpxht8o4FLpM-vNMLwvtrPNNzrQfvPGx0XqS7IhtzxMLni50p_lfe5GiRgrKdkThgO1iOIMEeeihQ1UnPAZmCAgrH_ohzd1fjBwbrdi9iKXABKwSS523-iE_pNa6T-ZVOBQxRbd5Prin-2biL_foURQipqtZk8K0IClwSUDU8cV0_LerrBlCrwprE2PLFfoe5xePAeZrKdWZ78w69UXq8ihLf46lKZPBt2TfHukYxZ4YUeNB1Sg3JH7Mir2ysabOjx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkdZ6Nrx7EhzkBROiTMIw3hzoYJmFuZ_dVg4G8EmldB6scm2tegKq3uauwMcyrsNiz8T8e_3E8evxDiJ8noYktoejKK7_oKxPWOxibVvnNZkF6_3gYwj_WTpZ_ZEHA-_eeCoCzznzP63H0dXzUt1FkiNKkU4WFxPdk3jS2oEjEeSXIj_dNtoPnYn-QQxUVOwbeIgtDi-M9KdsCGxh0oxMlOd6w0yWXkXIc3Z3PR5KEtUKDpVv7gZNZXTiw1yTq7w6CpY3Fm5qn_wy9-qOza_QczJyTlIwUXRditbYcXsFUfL2sE1F2nJDNHzu-299ToP0ADaUe5gGfvUwAze4_esJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=vQTlp2BlI83Otd2Rmvhrvwrtonj-6toNnqZt_MQ0YhHdNBWj-BOsY0ZtkSDD_wC5XlwV3mxft_XmZ21dCwOSikViQMFpZzp2wGoLZ6-PUIzopA0bmMCjfpBD5OyESjCyOjhSAMM5XxzgrBm-cASwGMiezCOmPfr1sbEe1FoANTUtv7Ia7ibtcpvGylE9OSttanFcXFesNXN4GwxoosBGrxRFQLECsIb_nS0hmSlzyAzLySwR0Q8UDupYCfJ00vhvFiHGmr15SBUatbG8EWCFt-qu-9C9VpmzAf80CVmk3Hk4KtxBgluld0neSvAolAr-qGzyXKK7Cr2wOAuOmL-xWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=sCdpFTeANq5jGLEO3SehaPVXnRNzyxq7GfVtd2UKLR0WjzRroq-S57oI4CF5-yG53lqx1ME_XI3XfvLB6hUtIQLlQad9m0tZhrAL1sTvWV0SO4AZw_CSrqZv_szJLYNTYV4QYyWYWKOWXVsvZze79jdJEEyajYRjR6WITNrq_0hJbCdGxJW4_y58pzhNruN8bKu8LnICOlVFFMMN6BDdSIP1WDx3LolzTWbFx8BFfqQIAXHGgKv7PAVuduRvqNm7A4Ml5uSxCATeplvNOS_G5WGbtB5F9Y5rLUssW-5kvQ4YlhFmrin5Pxj6UcSO6tLmwiAPMVabtX994AWfkg2ORw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=sCdpFTeANq5jGLEO3SehaPVXnRNzyxq7GfVtd2UKLR0WjzRroq-S57oI4CF5-yG53lqx1ME_XI3XfvLB6hUtIQLlQad9m0tZhrAL1sTvWV0SO4AZw_CSrqZv_szJLYNTYV4QYyWYWKOWXVsvZze79jdJEEyajYRjR6WITNrq_0hJbCdGxJW4_y58pzhNruN8bKu8LnICOlVFFMMN6BDdSIP1WDx3LolzTWbFx8BFfqQIAXHGgKv7PAVuduRvqNm7A4Ml5uSxCATeplvNOS_G5WGbtB5F9Y5rLUssW-5kvQ4YlhFmrin5Pxj6UcSO6tLmwiAPMVabtX994AWfkg2ORw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-2pgzk00Fnc23YmNcUq7dQ7lanjlCqA_WxwO5UnRoufZwQKS7xJey_sK9ftK3v9eRdynU6FZ7IGjUwU6bUjTO4xrLPwtjKa99cZa4FasdKcHUVW2W182hD-xfxV7A7wrfQ3dhK3xvACiv2ylcpiX7D786WMoOEd8gOqWEHa3G0ACLvX1nbBPnnxgFVWZInABfQaGAJi2gaO3giFw0xvdcR7b3vQNiiKvTguwb8lHD9ErdRzkz5QtNuMkcIkjXweQUslacXFR0z6nF55L7tPihcqxUwS04X1-j_lcWvDe6TtZ7dagSsdckg9dIbydvXT6juEij-h6k0G2VgYnO4Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnnd4xf46GwseFKg0hFy7z0BH0daQuqZfO-dDrzbhQtAkPy1AFoE2KtB2jWu3DB8LSypdEL9ANZptkj1m_FhFFwLgZQe_QYcypvbp8sK4qlHzYuZZJ-LCq7kmgQcav2HzPGN4sck8lVWyLNlv6ZJt9DXWsEb-AvEjyweTfG_Beop80AlqFbJwgPeFMl9UaFgZW5I2oVrPKj-zmKO3N0DjWNFnjMmUJpNGueQPc4qgiyrskXoemprqD5EIFZbPiJmY8IcZZXlPG9vwOkoYqnmWo_R-ETjX5bWrm2XKovMwF3okZqYP2a5pOwag2p8EOS8Hfp3gqFnmT0dp97zdot1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY-QaP7r1HdgnvYcqqtjKizXCN0814AXqDhg7JvzLchb7cZc3-hAGpOI0PZRC_iNDf7J_Efnt6RCSaXY7tlBjwtikJpgCkLuvUKIkd5vWQBTFYrS72BbV-rO4_7cQs1Cz6M6wFaNsIJBhERlF52wu_NrQNknGXSIQUwjFyKXN4dJfPT5c_3yw_TJSJgqmLczyo21COzXWvLZmcrOOJriqF8IPDnUt3P9c_E7KCyJzA--WF95iLIFa9vQovsYFZqdSnniEnTOfunqc2il6hb2RvveYDe-vfWnbEvsY6W2RzryoxSyRDtn4oKL_EwMZyuza11Bf82_u0-FZ2SLS62VYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikgNnfcKqeHGxWacRfIsZYeE8YivvOc10X8wXJTfGjhz7Ek7jX5w9oAUBtXUYKdYbpKTIFBYEQ2b81v7ouApJyzFpuyH5y7gkO7H6N71i02tKR1cVNfaO6pnWsvnCrVwbBXd03iX9HeSjWLZks4cNaFzUDGxZhyjizu0RH7Y216CDpzxU39XKnyDZyOmwqrsxz43hQCZDcqmUzGjNm_gVKSeY1DPR6E283KKvc2YurXvPCDTJIEtvoTpHK-M3I8iHLIbLx_fCWxhDW5T9sUorMhwGwYHjpxmzysoiYo8Ws7QhcRpRo-T5L4PuNYW3hxDjM-zyFqohwro87pynd51bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObRM_jvs2Jp_btDI0RvCRcNB9VF-P0A4JynQ_B-AoLbEcuvnUYSXBubX9PxwwoNmoE2FODNL3ozBPELkbtr8Titfpugo4uecMXKMkSRaXlH0Aa3OmOgxsfCKiy8DYOqw8otgHqjHHvqQaowbiT0nB8o2yXP7hkxp61o49QXP7gOtBVQGMjm1xnlsetAoBcDMXponwPub8MwPiZTqLfNHPnZRbYMnajavetLKVrlNGTmyqhe5EPRkFpgJke6JBqem91bXcGaj_1wqWTbuMZIv8filWreM7VnOQBAHOBu2Q0oFyf1SYcMn9VUy44xDEVBRhzPZhfnAeMNOpBUOlfr9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKiyHCIogn1Y5VkFxc10nG7Lx1I1dq28lzrzxMruyMYsB44Uwqr7LsN7EqOLilW8aoOMX0vBOzy4jk3NiyY_-99AG9OxzRfUUXQQuL1PRqnBZqBqlCC_94wkqSMs6Rxy2QSjsWYJqaXWagNietmhgnXlq6vej_G6wr8i_0DNlwGKRru80zQzznFSZPNRsQK5yOBDUBvdU5AUAX3LRwyBOFTuMzVBRG3tjrFfGLzNy20GrTFa6NtvEJMh7jj4eNCA65YRwol9sQKlWJ1rTMpL0529QThygpANEct0rfzCZBLxRIuvRaSy_PKtVJMPuzhNpX4B94chaQCX7ie26hkz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R61zMpXp8_HvC6m3iiF_LvgM7tz7e9tFCPDQTgXPq1XYR4gHD-UddfqGpMToxQrG8FHluuUbg5KigEDZlHUQ_6G--pnChVn7lSqR5FrEkOi553vLJQNgcvUEsvWCK0A22bD8RgNdrIZbX5hCmgt2UrgwLVUdosesyDDVx2FVdj_HA-sPLGrm2ICST5FIE4HOwgpCvm-w5WaYTWq9AKgm82s90JErIVRTNNGNQIPLPyVKK84FiOaRpXTd_lfg_g5zKjTPY47GGdyj64KAzk-vgVyjRIJCP-V7DhSRauWOP40vTI5u-_5Fkwk4eJqxxSZ4MrujZhJ6o9Hc377LtJsYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WL-a_J1oR9oUOE-7SEtny6jxDCfyTSMr-YMxtLPwsymRMWVI9Vz8uexDFiwub0iyWuJxyqPgDVF7w93Uj7U_YLVwSQfIazbKm5UlCsUKpr1ovwTxMm_vMi6Gxe7IwLssyRg1dcGNytimLMQnN_B6HRSiwKnTknq01-ObMrSGl8eVv2nlawcTRsoj_k-8psoyBWpdXbkuCZqdjknOmlktCyWGZ1QtvTyQaoiDFn8F2yo9yheKIQ2OdRSJ5_5l5VUqYXjxtvy6pNrOS4I03FDt5INlCCHzzFwJkIMIVkfgSfeqUx2HLhW2-d-sCGas3Y9lcaHy8RM09u-x2sCSjmYJq3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WL-a_J1oR9oUOE-7SEtny6jxDCfyTSMr-YMxtLPwsymRMWVI9Vz8uexDFiwub0iyWuJxyqPgDVF7w93Uj7U_YLVwSQfIazbKm5UlCsUKpr1ovwTxMm_vMi6Gxe7IwLssyRg1dcGNytimLMQnN_B6HRSiwKnTknq01-ObMrSGl8eVv2nlawcTRsoj_k-8psoyBWpdXbkuCZqdjknOmlktCyWGZ1QtvTyQaoiDFn8F2yo9yheKIQ2OdRSJ5_5l5VUqYXjxtvy6pNrOS4I03FDt5INlCCHzzFwJkIMIVkfgSfeqUx2HLhW2-d-sCGas3Y9lcaHy8RM09u-x2sCSjmYJq3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7FmrjU9Aq2GbRssybKh7mGIp8cnBjEQqZvDF4iS7gCLngu1c6dH-VU1oGoRfglq0O9Sk1K7c_xu0S84nSmNQeIC8TRPDfQQh4g7mPFmbfomcobR6mE7JoBTYJu68MOOwMwXKaCz2MhTdgfySk4cYcHlczq98UqwIGGzWvQOgITnUITgk6fej0haVDAhV0Bsh5t8UzZDUm09qkC40IbK4yCg4s5dTv69f6bJcOB9zpasFSUcKo0mO4meQ8illMkUOBXOiBR4nyErrtpvzEOu9QF4tVojOo6eYD9bH1P1PvvHvavtIGFE_SvkT511xzFZU57FD8VimT8FCvInGmKE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIbZYC5amT50C7kzcVH7sDtCQlWjKIDNzNacYvG2XAXEjX6I1g06WVM_RoGMD_acfdBIU_B6EBlOCtgJnAtXsRNLOpGj5eCQrApAsNmkNASM9Q06PF0cy_G4khhoQEhvCnba2UYiQcUX_3K5hLOBKZvvWwRSLI53vDWJTeOErQ1ushXVxrXF2JpiHbjRQL0Kkqo8Dj0OUjYmwzoRfWoAr6NtYK-5YMvyqnja51YzDk2N66yailD2ifGIgy-rMTYmX4KJZe1QBFz5sTN-PO1ESjmAuMci9MMN9JKiENgww_EiSFUbENwPOx489FBJ43NhH9Rmtgb0kEkyiHKoVOFsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=awkOU5TbV4Y6avtqTjMXQlxFmLBi7R85k0LkFf8pcJmlkLf9G5firTcI5n9kCm_WSqmQXo8Ztyh-P8Oct4aXfwzhj5ikRqEDvBuRZld4itIL-0oEikI57DwZC5x-UQAK0clsBqirwaGEe9qmevuDS-Xae6ij6Gj6cBK7u797RURM98w6AaecA3FxPPV6-COpJMM7hoLQpnqeodeDfAWhut4zywlnTIIu_Rj-yMrh2nJ1Nv-fqRAXW_zSbU1GdYlCw2srhqoQDzbawKnRLeOc5G9LWuk-Kq2mGYUktXjLuc5p6t8NTzC1-H37LuYKjCKOn3d6078lePUiiJgY6J-OwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=awkOU5TbV4Y6avtqTjMXQlxFmLBi7R85k0LkFf8pcJmlkLf9G5firTcI5n9kCm_WSqmQXo8Ztyh-P8Oct4aXfwzhj5ikRqEDvBuRZld4itIL-0oEikI57DwZC5x-UQAK0clsBqirwaGEe9qmevuDS-Xae6ij6Gj6cBK7u797RURM98w6AaecA3FxPPV6-COpJMM7hoLQpnqeodeDfAWhut4zywlnTIIu_Rj-yMrh2nJ1Nv-fqRAXW_zSbU1GdYlCw2srhqoQDzbawKnRLeOc5G9LWuk-Kq2mGYUktXjLuc5p6t8NTzC1-H37LuYKjCKOn3d6078lePUiiJgY6J-OwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6MrffuwJFUfsKGNFfMHkUfhyTqAPGDFll_F2HiWjOkjB_uDThpAq1lQ6WAeiljIoEFboC3CzHf4g94VApnoufYBTdap1hODtpj5kKyApbf4JDhDLnuCWSN8GBhJ6-86KifrzHPYeYaZPhhjO89i98meMVcsSz_r1OFwtgpPSnO2VIeZAyZoCaR6jwSSAU0BjvW_now3Jshv49HoPsw139g1FnXxFXuppdImogak_d4d-sKy1qfOMUioTMOUYtJED8BnPp3AjZVg95MWbNv7erH36CdIicoqxUL3vNpNMtmn51D9tKbKRrHo2Pet5rjEl8OmCkeOUJWmYBbS-d5F6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVgPu5yMFpDWwmIP3qMVBZbZWrg58LIgsi6Tj9M03Lzzw9XL5MUq3gw8onxhTkD9V3QACbMTHyF2IWwqRtX7g9emRLnPd5r4HQR6NPqykjz7DYgBP2V64lT4vmITe6du9DUI5FMzXqYUDR0YeRayU2NzDr8EidzH0lhSR5jjBnyXbIpp0MCS-Mm8LXCMfLTdVlVERAEXfykSYnZzqQ8TW9e4ZYvLZf31lXRhC5xLxA-QqaF4uY7-5ZEV1wF3yODY8QLBMXCH804K7CdvhBCB_np82GvZ8zqGZgeOVkCilltFq_aFbu7suEggJpis7EYQUL9FGpmW5Ypt6WeyMNFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkjvGLJXsMX_C4zFcm74edl5GmfKcEdtTImJNMTqC9DcMs8PH9S5ADqDBu0kXy42QHayUyHnherP8yR_-Hxk45WSeDV2Vk5Iy5ZHNlX_CkveCAHVWG9Z0PigL7ucWjnNJtrYZ9E0LKepW3zytMX0rW17LW3Ou_eDYZ1NQqg96Z8ZpBdb1F865m_qCukIXfxQSQyJpm_hOEWCLYmLrMrOpFwV-n_3QL_o0u_6VDxIbj5G6hePTcx-ZgyDU565puRfJEjQZcPXsrzqoJEt_J0HPBIvEFVPSJCo0hXumsL1GExNVfNRUSpO4t9eHUWdbG6tJijE8U7w65n-rJwL_uYAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=rGujsOb1FET83g8wTqx4vN-f5RXgeRlwdntLY0Z6BmuN5pQN1eKMo-NgOPSR54XP2qU3hYW58rQqOGchNZTWbwwmZCefhk_ENgvWbP0dmo8_SDilR2Mm0rCfeVNNRf4_FmPgUhPgIZ6tof6r5X3q5ULIPX8VXD8gYcseDXEKPJIyYioR0S6_-fPsq_LCNhs5G2xruL9-lVt2C74_aRk7zmDFYsCawS20t-Wx59cH3WovCTjlPit5Btnxigs6Kii8RyPVsqYw6IGqN4Oxn_U9l4cE9kdQFJRBJqvIC82dW_Sprt0Obg9QCeq7vZ9rHw1p9H5XAgFcbdO8C6MHDXogjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=rGujsOb1FET83g8wTqx4vN-f5RXgeRlwdntLY0Z6BmuN5pQN1eKMo-NgOPSR54XP2qU3hYW58rQqOGchNZTWbwwmZCefhk_ENgvWbP0dmo8_SDilR2Mm0rCfeVNNRf4_FmPgUhPgIZ6tof6r5X3q5ULIPX8VXD8gYcseDXEKPJIyYioR0S6_-fPsq_LCNhs5G2xruL9-lVt2C74_aRk7zmDFYsCawS20t-Wx59cH3WovCTjlPit5Btnxigs6Kii8RyPVsqYw6IGqN4Oxn_U9l4cE9kdQFJRBJqvIC82dW_Sprt0Obg9QCeq7vZ9rHw1p9H5XAgFcbdO8C6MHDXogjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNP-Adkvv8JM-nTSmmSLqOhMtgQEMINqMKt0W6Xb8ZawTk41Z1Z956D8RKT9yozcYDwAYLFNJeTxx1vSKVGeyMtCK87cpIEIYpNW7wyIsRBDlsOZzo_LP2CBn7WHWWe6T0D-CebWm8o5zUK-F1evqWEosufT9l25SZBpUPYi3gyd_TNEaNt8qFPkhnlbL_v-3QIdZScY6-xgipQoj7ECD3TMwyj-44uZ1Z_saiXj6P-IjmdPj3CnUL-KEPTZwN7PUxBTLIdshu-MRzgRZywP4Bse4kLqriDsFLbaLDPN-PCloj2ml-SnqodryqvVtpta5urh-tDjXNCaK4IWX1sbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXYIw9rgvHoeYlksfHB7V1S6wa5KLKrvpfJeU6l7Dbnu6xKVkqG_ykB_huOClsZAoMgcUo2rMdVf691kSIjEhEQUWJhyQmjh9pZjmVl6BL6AD9N9GnBYa_qp9649TWO1Cg6kn74Ta6cjVnSzmd8ElI-3cH1Rw3dLvtODTZDSWc6XHKrbWkTaYiXzh505w6WokhQunwzkkes90TBbJtJ6EP4is2B39bzCbQT_um_XDw1mdq80Pj5kfwG-QdlBEw4IhG3_7H3eX3JCQh1DMm7XObfnu7fMrBli-mgSJc7aNv2cBK2Xp79CP5sj8sso06s3BlDZYarrCzIdnIYKxspDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=sBJblV4UGT93zsbPuEQg6Y33gzVNKIAcQX7QLD08DQE-g-ixGpuSfFVlrcgXCKA0XnTc9y2cXsgWo_pnzvpRwdpCc64TZ4j9d9Kz5XbcqiXvSQnEfPJQr9H_Dgi0u1u-hYz9W9bgod0TPNI45HrpQpVRckvAhbYPFKzTmqZIK60cB68kl85xy0vz4s32Yk6uciPLmm533ZO0SjjweQB0VA3JBEV2qPdfNPzV3r-OB966EjxF8j1rulSjRCIjt8mEsqH5Dbi7XRMdS-XR9mNkFBJbjQwWN4cEkq2SxL-TVokRBtBo1XGG4S0PZcdZRljp07eC64pLkuDxCEpY4WWKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=sBJblV4UGT93zsbPuEQg6Y33gzVNKIAcQX7QLD08DQE-g-ixGpuSfFVlrcgXCKA0XnTc9y2cXsgWo_pnzvpRwdpCc64TZ4j9d9Kz5XbcqiXvSQnEfPJQr9H_Dgi0u1u-hYz9W9bgod0TPNI45HrpQpVRckvAhbYPFKzTmqZIK60cB68kl85xy0vz4s32Yk6uciPLmm533ZO0SjjweQB0VA3JBEV2qPdfNPzV3r-OB966EjxF8j1rulSjRCIjt8mEsqH5Dbi7XRMdS-XR9mNkFBJbjQwWN4cEkq2SxL-TVokRBtBo1XGG4S0PZcdZRljp07eC64pLkuDxCEpY4WWKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4-fVyRamXFC4sP1AQOTeDf24q8EGcjG2Vj9EY0fjMvjAZy7ykZhh93ahWEiXWPKVu-_2l3PbWGwNKMKoB7ZU3VzTklFBNNEwrOyehWtpdXfcqYkg7TKvOKiyDWwhkZpHmWqHb0p16LVJ5_TZzWgMnHqEQCcwZVLtgvE8O3KTcKHOCDhuxYH030NCWSIfeAF8T59Qeo3z04tfD3VWnpqVf-zZiQ1fvspypucKs44_6MEqeRoHV4u8eVTUOryPc0cIbsWZWlFnP3SWoJOXc4Qq6z-OJv5L614DQ7gLwSI7ncOgK27RG1T9pFnCkPj2D4eY4gCAd_zNt6uU-q86U_KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5gwTn0ye7TTgm4myODgFICsgPiBfu5lCp431k_uXwq2lVH6TaixzVNOuUq0hUp_fVPKiLL9AfH9WDuEFb-ckcTQQKUDn3WPNjyxE3Vwh79_mvkQ1tyAkc2mSARCZFmWD1tphFkD-qWRjJ77j1su6rXywFT_pkbuIYeSGS0JykGe4X3-VArVK2ROOrMFwJonjhmTZ878EN23auUogLVuEaMgv-6eoG6kcpgNdqvMfOrzrl6y2jdOxW0asXHtzQ42dTs0da3KtnMWU1aT40JEErekhfQp1vbhPzRC3-btxrHTejIJaQpc4yWNnsj9RtxYYpWv7_jcm-uSk8y8PtTsgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=tROlv2it9ZYgqV9VtF2xZfnwuaavPipjIYiHs3DlVMc2PnsOFU1gDPQvkeEUK2vzlGSu_xJZUO64aURdwaSd0R-K5qeQRyeKO91xuDUsL9Y_WPH0wbPjyfSX2rc3pLFrj-UqZv8m3pN2awNEP0ERAr7aEdbTTa_wKtU0NXSitV6B_kMna2yjpUIHd2EtAc4P8nU1khmko3dZuD4sLSsD0X8gBhVBQbi16gYNbpnNTOuMWNh2qIYD1ctZSoo-OCWQ1pSELOm3rczLToShJ_N-lHwviT77OaS5WV0-tRm_nD2yDBmXpVe2Pmo3fXH5oqfgkLjiWofU1PeFOlkth1pZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=tROlv2it9ZYgqV9VtF2xZfnwuaavPipjIYiHs3DlVMc2PnsOFU1gDPQvkeEUK2vzlGSu_xJZUO64aURdwaSd0R-K5qeQRyeKO91xuDUsL9Y_WPH0wbPjyfSX2rc3pLFrj-UqZv8m3pN2awNEP0ERAr7aEdbTTa_wKtU0NXSitV6B_kMna2yjpUIHd2EtAc4P8nU1khmko3dZuD4sLSsD0X8gBhVBQbi16gYNbpnNTOuMWNh2qIYD1ctZSoo-OCWQ1pSELOm3rczLToShJ_N-lHwviT77OaS5WV0-tRm_nD2yDBmXpVe2Pmo3fXH5oqfgkLjiWofU1PeFOlkth1pZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=KTC_Pq-P8_hXO6i6jmelff8tj-NVs5_X7ccmf7Wrhv4AZVlKcT5FTHQk6pA35ndn0j4LveYkhBSV4Mk-xozJbCSlp4TfnRvEdq_w_dlJZXBSYEqIU31MLdBsjAC8ZWXDh8zesC13CwWMH4NIi7SKiZ8fMWnMxaBbuRulIt3MEk-AlN694IbmTNaPg4i3vKn1fK66_1gIYdBoloQNmCZJd914XzE4lzNOW0ENjMip7nmKRgD72nkf5JlPp152Tegkrw47iwD3prKXGUrfR6mXtsSNn3B62DNDU05clwESEvyLAkILAs0VTJ1zZfuzX_6KqbI4cLxOZ2AVh8WtT1sifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=KTC_Pq-P8_hXO6i6jmelff8tj-NVs5_X7ccmf7Wrhv4AZVlKcT5FTHQk6pA35ndn0j4LveYkhBSV4Mk-xozJbCSlp4TfnRvEdq_w_dlJZXBSYEqIU31MLdBsjAC8ZWXDh8zesC13CwWMH4NIi7SKiZ8fMWnMxaBbuRulIt3MEk-AlN694IbmTNaPg4i3vKn1fK66_1gIYdBoloQNmCZJd914XzE4lzNOW0ENjMip7nmKRgD72nkf5JlPp152Tegkrw47iwD3prKXGUrfR6mXtsSNn3B62DNDU05clwESEvyLAkILAs0VTJ1zZfuzX_6KqbI4cLxOZ2AVh8WtT1sifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prh8Oi2lpnz8l39KrGDkWTOT5FCVlS861mpR00pXjosw-Btttf9QKTqIM4NeYBJIYWy8D5eqdd9saFdedEiR6hMiWmtBqSH1-nQf71kdw-LGyqaDTzjuD9Xk-MhIodup6dcs1CA7z8pKAYlRE8Ww3UVrf-cKXhQtrcUPovbA9XLb72tTZqrXTLnmjEH16ZymKEYm1syedQuXdPzN7-izs5JuPRj4Nu4i8MSvuoSyFce2wA_QUEao27diP7ShexyDhIXLKnPVmhmVjwNKfstMVkE3Fwci3JBw3dm2bP3IIEl-ic7w13LuKBodyvE2H6ndbFAPx1fB-77dmaOxi4C2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdMWc48CevrOgyGFQqgN-Al9MEekW0ww7Qq09U1m__t3Cah0ePimSfu4EgPVn4t0SiAGz-p-ypanj11Z-6MyhVOmCXWxRDtr8OpvWIsBtRns8jFKtISQJZKlMGLzFCs8ai057pOxE6MQuSfm9Q1YygTEoDkz4cHb0I3CzSoLgSKVwYw6U0OvVfwHAlBTyLeM0FLYaBl_ABU-KcMTwjVfeXdRpKan8v0IDuejzGF2noCX9b3PBNbDz7ACVHyKuyoEQmhqGcf8yY0m7iplkfgd5ztOc8cZvFQHY9n8iPN4i9AzxVtpF1w5zxWOTZApg6srG9iV5Ls6KvP_v1v-PZW08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJfJn3WDh13snfodHf7pEqOZtxlj0K3bw7qT1QpZVKB_Gqek7HvtL3GLrL7MAHbj6PqF05f-SjMZwW0ERvzZETx_IPnTaZ-VbNP6LUwaandNJD6pzEPdhsyjefRiQLyRPQ-GX5h_fqd3CBjp-OzA0hyPCbOJiiNdBLMXrqRu8jbP8NFdscNwxVKC8yCLP9irSjb91OQAayhcVfPN8ijGOfRl42rrjMp_0xyFcqTU8QzEqRgWMFIDrQ5GmAPCEdgpabm0NVvSQO9AY0S7InQm6Y883CikttmTdFdS3BgeDbRNk1xaPseK4FqDiw4JqnOXVmgHEIOH6QrHDSQHMEp1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV31IZJLh7PA-z91coBu286bIuP6b_GurS8vKwB5S5MXpoXQBhJTlGzOJEA964qb5OF-Llf57k5iOmXZKDARNSKER2WYEGcJTtCmGqsJoP4ojQAsI6kIj2g_082Cq-6iQmLgGluHmoswKX5RNUgkidyDwtVQC4PE2jG5cL_EGT_6rEHDxByI1TeEZPR3pM7ceUGM0faWw3huAk6n9QxeuGV54b1zuXpGs3ToNv7qkWQCM7lFx0vS_MyX1eJ8p7HcDX3_g7bDRzeyNl6GltQr1l6QdyhwNASf0NVdL5Yqb__A3fQmbpwwFOzvEf9W1keIX6S-KuwFdyARH6zuw1aZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciF8e1i__wfrDw2ufy7Mh5KTf4rUS7jUEHkCtLkTFE9vS_tI6xf5gXucaDVnFiydZsUCz0xK_77TiaTkjB15Nm2XrUX3mdy0Vgly5YADNq8Yu0k50dkjz3isd5UnS3uVxnhw7_HD_2q7uImqSCfr8UpN6zv_smxjIjKYuooc3QvyAMPiZNrmb1OzseouH86CFuifz0OEn_fzR4XsqzodC3Wao3v_3Tzfczx-ysqBek1n8L0H6KCsMdPx8gKp8nWMZoJQixQZo87zG09D9pQrJxFduJZQjQk55oslQVWrqbmd9xenDOHNGffMp3mK05NSUgZkhpamvzOQX-7INrVaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doJdjvED1PNP1CiZGcL5YRDYm_E_-EQ-Dj6WslyYIKQt7CrDgQfiLSDdtEeAABDVuEOVqv12ZE1FUOvAjAMmRHdCGQ8V4kdsC2UDB7voVXwJvzCEcNdNlPxwcuUdJkCkxG7Ic1S-P6FbWot9ueDW0J3LH6XXWk5kAwmzhYFuh5-P5j4o8FlWzdi6yBfk0Ip6sFUGd59dbK9R2ZArU5n6WcsKyJ3KzjY437D-ZSVfXLnpKvU0M02NbAsCRjUiqWdD0XmBkX9ZCIQF5uDo7ZgJEtm83mLDzZSoGrfEk45SzPSKi7BJUtt_sRJSJl6WpUPGu8auUd-EoH6QrqqSOloR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p32yHs9yawST6loVqaUz1ezZ5CBpQ5CNsQQR7G1vHAAhh-lKBwx1_8B8-H02LxsfzZcI43wEDXss4OZgizcVBeRiQRflEPyEgfhmZGxg-ctPVP8CLK8NC9ksKqiYkT_dao31QikcxQ0FnNSnc9B-ijw66NRizXUGXFkVE3R-Xp8dWBg7lCzfHzxmLFPcDsOb9SEngefeKDFYwrxVaYoj-ikWbpaEx6lPjvNSbELAz8v30IRMtjza5gZlY1V95F9oUuzVoewjG3uWIOZPXSZqrJkBWWzP2xmudDfwttEFzT1QRbCheCWV1LT54gXIjKAIaXEYGxuXs7GvN2gmOLdZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntCcP-6AnkDrn0xioHahkfImx95Olm5woYT_OGRZFiZOaDF3cdpkQ_2ba0ALxwJZJSfQkb_AjtDSSiDfTPM6jfXkWgp7gd5ibaQwE3fhGg62GSu7hVjsi6ciqqGhV4RWRVBHLt4_TXj7E1RHuOzxhLYJgHsy3YLc5Ot3q7jNIVLVlKsGcmzSN-QbB6IuQSvsBJom4wkWvGwJ9SswdBgp3hkMx6EK3ktlozvY7EdPKSfcdStLVZGN0brL1G13rTkjMBTIHJgzwvBLgo8IWORcr6-u_J3pxG8Bw28ZfNA_7LwThZvRYIc_-a6tcQGQ_BUbFhuNbQ3wt6PKsFRB1jFSTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=JLJ99VOD44HX9_nqzooKTNu9eHyKobjtHbWTc7ZLnQ0OA_rj5nZGhwP_dG8wS5QQdllEEUU7T5cx7whErLK0Xs72ZTqON4RjsWqivLG407gEWHoNnUXOeleSGMXUxunMVVpC9LBdO6nsJ-qkND1CrDeNr3tIS18csPXE1fLRXo7UwCR3VM1xsp7MXBSwnaQl8TQqk-cetW-p4jBAUxIm70hTdqQbZdGMXCZ8DDMbgL2LtNK_J0mvkqPxm0hRcoHIhonCNFvoydRW_Rvl6Jf9NatZTdaq28LNEQJLj8JvKnloD0YF6NTx-yft-NVK090OSpinPHWmzDKMZ_6i6tGLew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=JLJ99VOD44HX9_nqzooKTNu9eHyKobjtHbWTc7ZLnQ0OA_rj5nZGhwP_dG8wS5QQdllEEUU7T5cx7whErLK0Xs72ZTqON4RjsWqivLG407gEWHoNnUXOeleSGMXUxunMVVpC9LBdO6nsJ-qkND1CrDeNr3tIS18csPXE1fLRXo7UwCR3VM1xsp7MXBSwnaQl8TQqk-cetW-p4jBAUxIm70hTdqQbZdGMXCZ8DDMbgL2LtNK_J0mvkqPxm0hRcoHIhonCNFvoydRW_Rvl6Jf9NatZTdaq28LNEQJLj8JvKnloD0YF6NTx-yft-NVK090OSpinPHWmzDKMZ_6i6tGLew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCXoXvSllcwwJuiC8LqNOjwWsC2IfpJvYuP3Yug3MdXln3eC3QcpDeEBIcR2I2U6QeuxgEonlmIc8lPULhcgJD2DHx73M8G3TaKpE78ujWNo3rLhtxz4bO1Ks6M3ieY01DpB8UgFro_A9rLUfjSdHnpVSOsGgcpGKvPyv9drmwmM34e-NEIS6cNFKOUKxD0CZBeLO_SrxAa5dvD6fWXkRNeJGPGBZsa1gCAkmOIAjQ30rCusVaZbchy7UwYDU7pHVJXmg3MG-ztwj5_vr8lmb8zFqqrA17SSEG7ZXTYDJsYKQ-GxZmzpoxuja7GG0VuCF6WcYY8wCAvcitrgCCCteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDcjikMDMTWGhbRSDfjmgEzxir8HcFJFKshLYnv5-7bwuhxxhVVaxe8YaFCk6INh5Mux1MwBZCT2p-EgY-6gBdKibcWMzlBBZ2c9WrQAKUbeJlEDtKOqHdnxUX99fBfR0lwfBhmRYtDD-mV-ir0gNRNp6Pppl3x39SJ-5khpaOltoQdLMALLnGLLpuPNirB9fb7ObwKWn47gNraWOrMBn5iSLKCJbiPRnGFT6bGm1KOWVRu2Q2cVbVC6Nu1dmIKmKm81Fk7VlyBWJQEb2EjWlpTmcpO1cIJ8Y72R7hV0itYOZScsOL-pPJNj-4udnOwDvCuIKQb8l1aj4cHmXJdPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig77mrRJMuVyPIBJrzsJQfSKHvUjHUyeO6_7xtoAhuKcUh6dhwusFC_Ek6Gpp1ILX4HMjIpLIkd45wlJdl-dbwLFp2QBb4pHH4DzKzYklEYbyynWJEiDLqQB4o6Oy3nxHWHtE0ceQOIqh6_iFoMzVzNNh-Yb14rIwRvV67E_j4GyIiac7gUjALSrJrZdjsd3VTfbd-UvqjS9_PsT3i8oOT8eYfOHq5jLVqW4esqNmZeaPGRGcBxHscPyBl7qwzwFRBBF-Y329HZ80umerEp4nhedV7qbznfqlvK0v-UOWpS_u7Tm3khcWrd7hc_tTDWqk-5WcuuYmLZP0IuSYcmNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJY88uBwdPqITUfVjGmkFOr-1lmC2nsQzVMkcNONFv7FS6I1bnnufu4T0nHUoBhbIv3rsdLHSMHaZ9BT3KOTegcNFHbDFmMcZt4_9m77z_5ET8DzujjfXdCc7jhTSkishmMycY5lkRD8ku-3DajXcymgu2nmWiz8E2shmGrVy-tCqeZ7s1gJzX3EggKXDoqmmipbh1PRnbhhw8Pgx2ZWYJRNic1m0iBpp2-NXleDexNbPG5rU7hLXrAg2icMYiGZHaB6xD8lTlSfem_13Kv4h3k7A447ZO8C8eC3KvudGnnyYWlboTNgc9LRgxp4u00rO27ETcBOAKH0g3Mr2KKJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k11RhGbevJqqKr91r27t2QOeFRJ2XQCKrlwt7NhYUlS53eGNT8FFFpiHPgoiH9w9bsCIevGk3TrSPl4y7Y9DR0hVGED-bJRHVdKAYlX1ehW-VdzO4VzmRWBH2bu_rwLS8adC92o_nXf_9-L2alihMetVzMsZR2XtT-7kOW7BwgUiggiTJ9ETHV7800BPcW-BOECya9DDu6BWwUIZ1kteacGxs7aT3AaXm7hD73loKmwWE1jQ9d_zNHtl0fjJIb0uq9NmJlc9JASiSdQ3Fy4vMkU7apjjnXTJaFlcjkj6DNdU0sOFccI47mdOMK5DUAgj2xgr9Y5OR28fKhclmQDOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0vtt0xeYbxhHELCkJcM6AZq_fMG022BXvt6jC_Xxes-LCl5YHqKqR8aorRMSHQIgLYu24hGz2dwkIIpVTe5C2e1cnFYLDFniWi6ry8tICoDyTRL8XbXNhldxBEtCW9j5Chj6de2N1TIr-eRYtIkFO0Q65IHcVwzY0KWuH993Tr1CbwNHj2xH4AVr3jqP9Rq_9tRfpIDnadKcttnulpw6s71IOp618yczWVxZFWa8acj6_eApvknhtbGok1D1-4Hp2SVRnIwN0zpdov-w3cpG-01v39xKSxkW44OkZ27RhnCHslpKeVLVxy27RhszZkigheVTAgyAOtV3-5yOkVT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOqmbtK1SfzUbEB90lCWJqZf5Obo26t_JceBhiJSsWhNYMZ1_7RSMZlARohTHtCr8qMqpJSPBFjlrtTICerHpxedrsvyG-ahV7UrdiJD9WHhZh4H2YUqeOsHOUa-AeJuyDyzwyCucnnlluDSOO0E0GDW2p8ZhCeneYfXjx80XCHVAt-kyTQbC8KGUhT6I4U3VyJqTxJNtcHnPfx6KN8V9sUOCM19NBz04asRu9mhU6NIBZlsHl7BZWl1Z8tLq5D1KzplKphtRbPI-S4Er0vzgKMTJQtdys3lrLYESW3hWAIFKhaLDWGOjHeU5p47yOXNpkvL6bhdI0NuWqVSOqRcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo2wNwSHNuQftrMaZj5G8FMhFVc3ao1F4B7f0gM2sAF61Bd3XNZ0RMC9RMcLX_he-1n89JJH_A7ftdq7O6qYEKFQdPMT_5b7j54-jFlc679Cds9gVL6TMK1Ywx1cbYncEZRgS_He1tRJCp_9SUqiGI4z0oW7eGQuExdXMPE38Hslyt63kQR3SoLd4KAWBhG22x7CQ1z8Nc2-pyjXnfl3yolOmOnpV6dhoNrpV4TjZYGZ5cbTZ_54fAhrv03M9N921natohft3gQ7v9KkFMhWXXODneNcPe67avjCWLHNsMlSVXV-TFuHmjahXGXda8vW7k4TfQ06yemk_tLuOF8G3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV982z6YcQw1Hh70zuaJ-tb5S0HNm3pbc2bAAqlCy8HLdr_2qhQJ_sgiS4dIy-fQUWlvlRbgVDSIRRMmVv4y02RvszUXtZO0zUVdig7sxEhW0HiMoTF2GCOmvVhdQuqSAPTLo_L-iN3Et_Oy7q9Y7xrcEujLBI2jMQKB-9DIG0XDMMVmmMn9QkxuP2ZN7Y2IdeOinE1Ee53l6kag0GjzTAtoaFrIJ28UfNRF6aDc8JenVL7A-v5b8cFdh9zFGxPHjRa4mraqrleRGv8bwwzWL0WU8IxcMOkYbpk23lz24bigBm46xnkEmV9ly5Ts4GFKPe3T2LAUWGSVx4ReET-m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=HL0dnEuZ2TXVQ5udN3axzY_fTnxcKSy_l9ccCrs9BQax9YL_DyjMMLUW2SwYwOfmtv90_253Ndwdmrofz22CeROoMYI_D4uVTHxXUgEPv3xUuBY_nmvsAINevexjvpikZyMtUZlXi0C066QKxGmwQITJ7N8xN4IX4thVSobxvtFfkKFouY84f4eXu8lQRfJl85W5Gz5DU4Ic2EDZz1hgftOug0a8gZ4briy2vYE_LRbMqTOXzj3hcQiFWbQGFOV3hV2x4vjkvkSgqHf00s9w_ULroR-gqZCJxkEMVuvfKoetUoJepdfeJ2LK7WQTWPQfv-xoLTUNWv7U7wYDVnFYjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=HL0dnEuZ2TXVQ5udN3axzY_fTnxcKSy_l9ccCrs9BQax9YL_DyjMMLUW2SwYwOfmtv90_253Ndwdmrofz22CeROoMYI_D4uVTHxXUgEPv3xUuBY_nmvsAINevexjvpikZyMtUZlXi0C066QKxGmwQITJ7N8xN4IX4thVSobxvtFfkKFouY84f4eXu8lQRfJl85W5Gz5DU4Ic2EDZz1hgftOug0a8gZ4briy2vYE_LRbMqTOXzj3hcQiFWbQGFOV3hV2x4vjkvkSgqHf00s9w_ULroR-gqZCJxkEMVuvfKoetUoJepdfeJ2LK7WQTWPQfv-xoLTUNWv7U7wYDVnFYjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxF9wuR6CbikIT9_VtwLUVkcNC8awUeJC6Bt0XEv6D0s96iN71y4Wio3zeMQbhOYwRaqH_sJulCpsaQXnniqe5wtAh7XEAKGtBg-zpPy7AE8Mwr6933ecZ0l7-Xz2R03PLDmVB0942sJVAMEywWScqncTBDwqmJZsdmRNoSavhtL1xltWYT2DI7CenwJadgF2f-FORw3jevsap5mIO99hN5rY2N_39JZqDrqCFWZvEN5B3QrP0IXA-oz15R-6SY9bMS72VscrbDKRNzmjyIE9VSz34CzMuSm0IcOnfn7PcG3B3eXUyZg6RksVnuiBJ10zNCgk_t5qX5xtnCgtmw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=m9Xzi9STZa0OC1KVUENy_R-WtWS6FhNUHbfybv7ijHI0_zNN4Rh0NuKtzumw05-vhKdann5oScbpnmdlO_XDhIB-pm0rlxnNqvlMQjftf8fU6wGpF1NDNKM3qbYLdveaVkuYHaRmMe3TFrdKfk2itih6dcm11BoMK6pAZu8yVamrqF__B11T2KcidtstLuWx8gW_i6n8vOCs2B-nw5VjWzx0qUSV9RYpnFfZS1z0YC09rxa9p3tj95jA5GVjEWNtnCRqGvBLwzlcPi5uuwNLR9th0LLVAl6d6kh6nFKrzu4I6xESIuSQ8WHsiBoQ-qV05sRzJvSs0NbA3sutpY1TWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=m9Xzi9STZa0OC1KVUENy_R-WtWS6FhNUHbfybv7ijHI0_zNN4Rh0NuKtzumw05-vhKdann5oScbpnmdlO_XDhIB-pm0rlxnNqvlMQjftf8fU6wGpF1NDNKM3qbYLdveaVkuYHaRmMe3TFrdKfk2itih6dcm11BoMK6pAZu8yVamrqF__B11T2KcidtstLuWx8gW_i6n8vOCs2B-nw5VjWzx0qUSV9RYpnFfZS1z0YC09rxa9p3tj95jA5GVjEWNtnCRqGvBLwzlcPi5uuwNLR9th0LLVAl6d6kh6nFKrzu4I6xESIuSQ8WHsiBoQ-qV05sRzJvSs0NbA3sutpY1TWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارتاکاشته‌از لئو مسی فوق ستاره آرژانتینی اینترمیامی از یک نقطه در کل دوران حرفه ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkfzLwopjppqb7kkKfn0PnR6OKCPZFpqyuQ8fLVSF8Y5iFyFi-0kUPlKZE1fupPthTnPwuvqZwiNSVNKYh0bzAkRz7MRVNZa7apkf2d1e2zYuJCogtBJsFWlro82bzI-bNAGAdSAcJ9qY-vf-ntjULYlRLuJsVdGVW8p4gL_TvF2w-iLC0bdZcQOfG88eAa_adwswNahxuwCnH2Bn1xpFstZpmjT63S-JNfvL5vlK84uZTnmtAnKR2Zq9ndQ53QLHoYOUwZvNMWDZWXQDrudtHACYh9zcGHLt6akm8ETTrKgYydZAbCXUIB417B8HvcXLh-Ujp30Va8j69vxO2fZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umPDvEtaHpjctYOOskOZdsb0bANZJ5KwGLPAgER2DEeRFcWnwGqhVcHNKYVDkFJQZMxrSd1BWZ1dOb-oYrfjCT8XvJPYsjSXA2Mdx68eJlKoC7X9_1L0ZgWpjGHf7ZW1VGV7-uKFoxaWiaR_IJtIiasfeFhd8-1hGplPQ-gknPMWwjuywqAms_mj-9o9EewgMykT9XgHatQnTINngt-bNHh2FvhNliF3um80Q8f_OLsGS3xmC-qbSHMKDgHt2LP_SD3TF3urveedOoReHh0CY2nxfLaY5JrcWnATCUC7eZhKjp365ljBVJSFnBEi2_FO_FUFC9OVcU2W-GHW58vntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=isbzHpbUVsbWYqTp6bj_uj4NP3wFWopng9ebptf_3aUoegdRmXQxj4fyACZBDUP-_w6K9V-9jXgcp2cPTuF17woeEi7aX8-dkBc1nam_n1nO8PQy6oL74GHUlqfPiA3jJKb9eZ1TLgqFHo5iJBisB27E3mz-ts1doKAFcrG6uCo7T7OOq9VBlRDM00E0jT4H4X5RJveV0PEDS0Sp7vLwYD2ecLX3efoPme0AqcHR8Em_XhsJfzeBA9q9tNBl99agODP4z8BDEv97QRSOhPfvJtGKebl1HKX4UnsRdsuXouCM0qptBoLuqE6gkZhGb6ZG8Baai9ua40bSCjyZxVDMKWnzdWqazigt7lV3IxI_3_OUuD7o1DDfq6eeiuRh_9qf6RNnADKzTA2JzkOJ7-KiSJpGTEI2N_riyadc9HCHqBWlAe8nkeXL8W0gXQnSy7gfnNWKYdZbIdgWeoKRBmR8iBBtRn92WOSEmK4OOV3WyYa_UdceE-WXzdNvvokML56ctN7OTlcF2LUcEq8oBSbwd9ykQ9bakmXoyUolqeV8Q1NOlG4QKMyabL12p2On6nf-rmcsuN-bEHWCznJF0w_VNESZUxAzSpbhRrI5Geiza-repETx5gX0STQdPhtjXidbccbicpwbQ_Phy25UDB-FvvdE4-ZJjVEtZ-1rYylAE1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=isbzHpbUVsbWYqTp6bj_uj4NP3wFWopng9ebptf_3aUoegdRmXQxj4fyACZBDUP-_w6K9V-9jXgcp2cPTuF17woeEi7aX8-dkBc1nam_n1nO8PQy6oL74GHUlqfPiA3jJKb9eZ1TLgqFHo5iJBisB27E3mz-ts1doKAFcrG6uCo7T7OOq9VBlRDM00E0jT4H4X5RJveV0PEDS0Sp7vLwYD2ecLX3efoPme0AqcHR8Em_XhsJfzeBA9q9tNBl99agODP4z8BDEv97QRSOhPfvJtGKebl1HKX4UnsRdsuXouCM0qptBoLuqE6gkZhGb6ZG8Baai9ua40bSCjyZxVDMKWnzdWqazigt7lV3IxI_3_OUuD7o1DDfq6eeiuRh_9qf6RNnADKzTA2JzkOJ7-KiSJpGTEI2N_riyadc9HCHqBWlAe8nkeXL8W0gXQnSy7gfnNWKYdZbIdgWeoKRBmR8iBBtRn92WOSEmK4OOV3WyYa_UdceE-WXzdNvvokML56ctN7OTlcF2LUcEq8oBSbwd9ykQ9bakmXoyUolqeV8Q1NOlG4QKMyabL12p2On6nf-rmcsuN-bEHWCznJF0w_VNESZUxAzSpbhRrI5Geiza-repETx5gX0STQdPhtjXidbccbicpwbQ_Phy25UDB-FvvdE4-ZJjVEtZ-1rYylAE1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGx5QLNZFG-ugVTyrc-wFJ4dqvXLjpAmJPtHz8FsIasyLAmY2ZSIVjDaGxmFPAzCUUjI-MJVMu4XKQM3_geMDSl0JmFztAUwn4sEA6xuTyX1brECJ_MsXAGBmhIFPEL6rT0vap4_sV3ZSCRrvBT1VAQHZ49qqJKvdv1CVMWQqT-yW1BePG8P_-z6ynjaPzwMfDj7WShJQjr5Xj-O7KHAicm_9KA7aPkVjOjoaHhMpnRzQ6AORwZ6OekWxpxP1oWpsNvM4N_jH3Sl7Q52szp5NS6ETu9nG84PxKl1Sp80zH00AmKifcp9Jc2D30PtpLbiABnMw0sQkBkvh9xUO2d6ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osMG5VG3S-1gl-IyVgTFvY0xg8ppOd2zWeYaUPM6OzG69SjqZxzzFUFH6xKemqDlIQazEazWEqJh2dqqkfhc4MnaG4BGE8LvggdsDSs5NwKhAMaUpEjSUJqtbgHnEgd9f5eHEShscCkaIUF70_q436KGRUohM7MinlX7_0v1OuV3jkuE92X7w0y8gcDeoI5fM8CaQmEPSLWfwA8ZThHY7iwi5XC81U5NDAFHJXZBbJJk0EVr2NZWVzVm4Z5ASRJHyH4v571He55qXoGDEtWNWqeY3a4aEjhKN6wZbjXcMnfTh5qRyvl4bjeh4fzOAVGxhAAoPQnPK24OiSnc4dCeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY3kKhgkEF4_ZVokpaAIs6tZn7Mv3GwfPwkVupq50c0omDGJNbe3uuKKFTFlGDoNvSs9fQH757dGL1Ez25rzXn5TReay_6V906kP5zq7dL-MjbuAlQlAfy10C_jisz-DgVNPYbvFDZ-24GMt2K0qyVY05n3tUzsLpuoUcmkuWcgukRzshNXp1TMqRFZRaTVRk3Xo94_1nhZhd9tj0o8G2N0bPutgKCj10JEQ31R6XIslDwGzqMNyWjR8hmRSdR5gCqv9i5gnRvEEt6AFmT-EUqTZ7TU3DLnvrxdCBbAKjtNunRFe4lan4snIiPi276B1885-fF-B3FJrBRcoPBmHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=jvNap2VEsREkA65xG0QOi3V1YCYWn0QFKwdMrZgFFY94-QZCGJ4si6JM_6VOiIXbsq7wa66nr44yW3nSxsspjruLg5iE52AeFvx5hoeSnHK13GDM43oW1GrzePPp_hSAkxvtsCtQ8T-2wXjgu6zkjf1nIVwGcnnHc-RR7_EMarjGSdpe_Yz1m3x8YyPVc9ZmTipnLQIR6OSliE84XO_sVRRLrYM1Z7oIVpFEC_mT13vuyXZbfTQyH9m6vhJ3nRGnlB4Noi0DRgFwP3269YuMX_de68gyPWRmgZ5cpMWYdnUpzF3cRUrLJ_6jFU7gYWZMOE76g20b8GPc2U73S6AK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=jvNap2VEsREkA65xG0QOi3V1YCYWn0QFKwdMrZgFFY94-QZCGJ4si6JM_6VOiIXbsq7wa66nr44yW3nSxsspjruLg5iE52AeFvx5hoeSnHK13GDM43oW1GrzePPp_hSAkxvtsCtQ8T-2wXjgu6zkjf1nIVwGcnnHc-RR7_EMarjGSdpe_Yz1m3x8YyPVc9ZmTipnLQIR6OSliE84XO_sVRRLrYM1Z7oIVpFEC_mT13vuyXZbfTQyH9m6vhJ3nRGnlB4Noi0DRgFwP3269YuMX_de68gyPWRmgZ5cpMWYdnUpzF3cRUrLJ_6jFU7gYWZMOE76g20b8GPc2U73S6AK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMLhwtjL4mKpOGIdazCsBmTRUpwLSRPIKyGDz4K7w06AELJW9SELqRczZieC7fDOBRuw-RUa4v7aeKB3eHX6nSO9laOcjfZHdKpbOWyb13bAM5QSUi0t9HW-8nkeeDwyiGIWo7Y7vV56wOmtF17zqFVetzfmvfJQhrasZpsWjrSJ6p4mp0ISnr1EPnMPTeenBJfzuS_SeqWmAsm1Ql_R0PI9cWztKnIzMws78Cmldng857pnQnv0j8N56ukinn_g1Z2Vrsl7SCiYuVWIfG7-T6U4pvsz1OXMEZZcxpClMBiaKHZhH6VcXBgrLGGf1L-js0erL1-E1IMkNV2c_pD_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFa5HutyAbdDiSCJr-K3lWwGazoVEiII1RjRMaWELpYpFB91tL3vUFPFE25Hz2o6_tp2Rpy6R2iif2CXWUbIQHl5tqq8C_iF6oLSTH2oWTQjFmAdEdn5zvCK93K0b6ixY1I4pT2aJxIzWzdl20N_qoSUjyjrfA41048OEXkITAxFUcdTwPCINVe0Njf2vVA5DGJThEkadi178N0sRWWC9xcENA6rhc4qjHnOMPH95DAm6xdKDm2_UIKkIKayp2zF7Ck3vLAkZGtSSrgh-dnWAPA4KvHg2LQf_-kCuaLKL4v9maAA4cBzYMYIu7EFvo8Q_wNhykzPnU2Zsf8HAL-0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEuELWPhkPQhN5_hXF5R8XngNvbRPJclN7wli8qi0XSITVDdoezYAD-4sGZt7jjLEU-rIS9hgkoUqT5DxkvsYtkS3hGkhT3BbYIT3sqN5gF-8d4KUE3FoNhIuoejTvIMk_0P61t-4jY8gzTHAeXO66etl-3Ht2eN1WkFaoUS2KdJU24mXrZoyQj3eqPA7zCLJhiKsuELaI_k_m66Nf6I0yTorM_LH0DzjwFz2Ub_RzBIcE01t8DDoUgz1KqMGYbSSUb734PZaCst4OGWWxEWA6A7GabpGUigHT1rTOLZ2aKrLCgPgtpVD949llwN-1ME1zA5jZ9AqZODyZdWIQYBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=t69GD74kPVwjdXy9KV5YgcrEqqfdfN892gPryanVmpk1TZ5TD6L-2Yzp8ymZTcMuDvZvgzlvKDRA9q8t61fN1Z8sLzbjOzFiBfwwLADLBODX5JHshr4ztORxBthjDWbQolvHEWR9oG7x5QKwlQ4iqsIFOpr9S7cHuQrpmFYCJ9SP-4wMzef-f__uNi7jQHQbw35LkdCMAUiKg4foo834jfczc9ndrGYHj28_QsvcJ4d0H_cuYXRGGTmWxEOcBgjZ1ABV81dplZa1EsFnhNKce9OudU3BsB7xT0MT5nZJar8A0Zwq1zPj0a4xDtDcI_HLC4KJG7ZpXXR4W8vcWP3sSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=t69GD74kPVwjdXy9KV5YgcrEqqfdfN892gPryanVmpk1TZ5TD6L-2Yzp8ymZTcMuDvZvgzlvKDRA9q8t61fN1Z8sLzbjOzFiBfwwLADLBODX5JHshr4ztORxBthjDWbQolvHEWR9oG7x5QKwlQ4iqsIFOpr9S7cHuQrpmFYCJ9SP-4wMzef-f__uNi7jQHQbw35LkdCMAUiKg4foo834jfczc9ndrGYHj28_QsvcJ4d0H_cuYXRGGTmWxEOcBgjZ1ABV81dplZa1EsFnhNKce9OudU3BsB7xT0MT5nZJar8A0Zwq1zPj0a4xDtDcI_HLC4KJG7ZpXXR4W8vcWP3sSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=Np3ZKqnm4gjtMlQg2mDy015Cdvelzap25XsNjlzdgj7olhZKC8-lCUc6zxzAHbHNJIHZqYfQne7neU2Qmvt6WMKPFfd0RUehbxgw_yUUBgTIPi5gvBJEd29PH-4VU1jPSYdkdAV6Jve2vkEZOSszyKgM63Wv-LM8CzKmnvHX0vnxWCpIArU27Wubeku1Y23z7C_d6srTPl5FaLA7OofrHsiBpVZ2E57TPg6FmuMvAvMrJIUbv0TCe3le4h3jocjfVdgCd0mJvvdQA6E_wp6rBu9n77nR2_w1eZxo5qiuSuZ3hhFNeUo9ATNUoOfVHHXP0mIG8velcYpasF724_qi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=Np3ZKqnm4gjtMlQg2mDy015Cdvelzap25XsNjlzdgj7olhZKC8-lCUc6zxzAHbHNJIHZqYfQne7neU2Qmvt6WMKPFfd0RUehbxgw_yUUBgTIPi5gvBJEd29PH-4VU1jPSYdkdAV6Jve2vkEZOSszyKgM63Wv-LM8CzKmnvHX0vnxWCpIArU27Wubeku1Y23z7C_d6srTPl5FaLA7OofrHsiBpVZ2E57TPg6FmuMvAvMrJIUbv0TCe3le4h3jocjfVdgCd0mJvvdQA6E_wp6rBu9n77nR2_w1eZxo5qiuSuZ3hhFNeUo9ATNUoOfVHHXP0mIG8velcYpasF724_qi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JojO39-EpgSMKrDW5somEa0m8KfshgniMCG76yxPTWia8gGgYVuOOC9oxs4YCu_DDtXefrh8EvZJXRdJMcuxSA5lP5n8tn5U6j_MjhaN5XGyQIs5YiHbQy_cWzFJZlpcAuONfa5Ue9sSjw-Zv41rCLiCgpOQvYMrU2qAuM_wXAz-HSoIPo-jheOzmyBgWgYTvkfRjMMifEmBc7mTUB4JLLCFpCR11F_KUnqFp5OKNlH3F6WkGmfYOABSdgf_gzn8a1rM3OJfuGoe1Ywi4-9VxCl2DPKxVeHRmohpAzD02usIdt6q0Le_oQh21gHGX-odsQhq6GsRl1nnVuJ55oOang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc51IwE91Jid-PHU2qTRFrOCajNRREkhSWcIwcqWhFwBsEOVXNKt0cnMOQeY97hogy7-n8HtT_qhBtvGDQsCvCGfDQ9CDhygQkUvqm4vyuUByFjNFwxubEBIcPMzkkEVTmWgMCF9rtUoDpPTPAP64_tH95lYhMg4Uk6kGp6hP3t9AAUGR7OEtghqsMqXkdKD6b2a4R5o40SNCgfOUu7vBka1ZWwlnKpc6pgEpcaTqfh7IF66k4WO6n81kjnByaM0OJSqSeq2ibN_-D8SVdolX4dlJzsy_07jhZoe9bzKS5BDd3BU0OwBvHsk7WfjWcyiYoIvu-l2OC3TsI1I7hdMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ3upBek7mL6rlet5gDnDUB6fS-dI3G9ngXjhfGO--bkCnrxNOI5CDzMtFEwzWfDojRrkJ__II4PGoyzX4dqUwhrQp2Qz3DmrSdGkyl5cNghHkZKdnokeUyOq1DVbkzWovd7zFtPhPDpQyjc3bRwllUUv6auKb9CNcmcj17UgZvXPhGZqJCj8aAfAGJdhu6ya_bZpJCX5yP8gynLY4h8FWOp6Nqa8jhPrFf4jK7O39w40yeeVf8jEPIl1LE-wgf0SbuyNZnYdOR_oZJ2pqRrEX7K71iuXaPTrNMQd6akNwD6dVskPOxOb7pe0r_5yFU3xjqcUPkmBejksQl5cuGSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=oPSSJcMscgWlnf9iHzbziGPcGuOzG84fgiYSZeIk9Y0Goq_4FB4XHoJIEhURQqP-ZXCleiQ1qfuSc_StP07NttBGxRPXTV5GbNHfRJpfUGaOk3yZXxRJMxTheedRZvmIio1IA6I5bsRpnsJdWRb-R0n_3kwDzfrHBQZste5OxHIW80-FR00iVaGczfdmi4SvSTXE9uHoQmxllQo5KXELjZtetqAnGotayRKoVAk1KgGBu2ljWyzVkoMAtDb4zbwEKw0cH1MmLyWolH5HaIqmEzB6-LOYV0jz-FxzN7NEt55MzWsl5KyeIinsIUT7y40UPfHmHv44lmCjKl0mtlQ3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=oPSSJcMscgWlnf9iHzbziGPcGuOzG84fgiYSZeIk9Y0Goq_4FB4XHoJIEhURQqP-ZXCleiQ1qfuSc_StP07NttBGxRPXTV5GbNHfRJpfUGaOk3yZXxRJMxTheedRZvmIio1IA6I5bsRpnsJdWRb-R0n_3kwDzfrHBQZste5OxHIW80-FR00iVaGczfdmi4SvSTXE9uHoQmxllQo5KXELjZtetqAnGotayRKoVAk1KgGBu2ljWyzVkoMAtDb4zbwEKw0cH1MmLyWolH5HaIqmEzB6-LOYV0jz-FxzN7NEt55MzWsl5KyeIinsIUT7y40UPfHmHv44lmCjKl0mtlQ3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
