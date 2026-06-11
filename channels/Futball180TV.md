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
<img src="https://cdn5.telesco.pe/file/m7C5MkWIvgY_2OSkIc2S5LWwZzmxepfG_r5vhUHNV-ZLeWKAKULt7jwxK40y5OuFioqr1mKyhDXv2-Edh2SZaJRGXBprZElMeguQ_38XBNBVr9UxKE5JbnaOkNtqN55RaF1yv7UsJGihDH9zwpaC1BgHXo0nk0VDQKccryTX8pdNSgpv0Zp0EPsaiKm82K7dPmKyccU7OQ4_M3_1SCXloFJ78LSExnm0H8S6hfDk3QYYo16jS7it4HsoX-HSzhrI_CNTIr6LPObh0xCMfwi1I1qp3hnJ8vIo0uJq-7TwYpA4X35nREfBO1BcORgxfnbgBVgeKwVZLQF0ERTtT1USTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 333K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-91995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینی رونالدو اما با کیت اشتباهی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/Futball180TV/91995" target="_blank">📅 10:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=oEj6HK_afSbUr2eMymxzjynKwxl6pQSFfwIX8W56Kn7lD3qKimX_Hy6lBYOdrsUGIGrWNuKTxVP9cLXoLXYX5C17syK2t_oIP1XaTl7Duvorr3wvAlabAM8bdocte5YqAP9Nnupv_hUevNop7qchY0c2cfgvQNATuwy75DvsefIx8Xgep2Ywu8uduYdqX_1iXywh6sNJkomvvPDIZ3rs487dXAYcIrG3oMjl3uzCcos-OwEeTJS47PonP6hUSaGR2ITYHc7j4nE9AfLSGEpW3_Ifw-u7X9rKvxJf34Zzifn1SVujNkQ5T2UpJfxlZCNAm47mgrH5iiBSjs7Vn74J_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=oEj6HK_afSbUr2eMymxzjynKwxl6pQSFfwIX8W56Kn7lD3qKimX_Hy6lBYOdrsUGIGrWNuKTxVP9cLXoLXYX5C17syK2t_oIP1XaTl7Duvorr3wvAlabAM8bdocte5YqAP9Nnupv_hUevNop7qchY0c2cfgvQNATuwy75DvsefIx8Xgep2Ywu8uduYdqX_1iXywh6sNJkomvvPDIZ3rs487dXAYcIrG3oMjl3uzCcos-OwEeTJS47PonP6hUSaGR2ITYHc7j4nE9AfLSGEpW3_Ifw-u7X9rKvxJf34Zzifn1SVujNkQ5T2UpJfxlZCNAm47mgrH5iiBSjs7Vn74J_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رفیقم یه دست شانسی منو تو (Fifa/Pes) میبره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/Futball180TV/91994" target="_blank">📅 10:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=oWChsRkg4Fo5yny8JKE6T2hnhxpCVmn_rIjD7bsTft5oxQdiCwv3zTOh5iPoV1VHqRO8TcCP_8os4FuuIy8aVy0Yd3QgNXSryp0sNG_JNzoLb7JJEugfq8Cz_zcUB_dE_JxNBBqmvGAdIF6Od8Uq7y_zT8dhPD2fM6id8L9rtJ0A4zTySgu3vlUFQT_vEmN79sEDBj2azOh1PqcLvfXhT_QQMbQey7TvC3q27tz8XBSCFRi9Q2xpg1tc1ZD5Fd9jZitiBRkyYbRn-ILAs2rywmJmhYVIWv2U9z0bNNUzw65UVo7GuiSiGmpG-M-C9Y49O474MLsFyk90IQfxDnanWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=oWChsRkg4Fo5yny8JKE6T2hnhxpCVmn_rIjD7bsTft5oxQdiCwv3zTOh5iPoV1VHqRO8TcCP_8os4FuuIy8aVy0Yd3QgNXSryp0sNG_JNzoLb7JJEugfq8Cz_zcUB_dE_JxNBBqmvGAdIF6Od8Uq7y_zT8dhPD2fM6id8L9rtJ0A4zTySgu3vlUFQT_vEmN79sEDBj2azOh1PqcLvfXhT_QQMbQey7TvC3q27tz8XBSCFRi9Q2xpg1tc1ZD5Fd9jZitiBRkyYbRn-ILAs2rywmJmhYVIWv2U9z0bNNUzw65UVo7GuiSiGmpG-M-C9Y49O474MLsFyk90IQfxDnanWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از مقایسه نحوه استقبال دو کشور آمریکا و مکزیک از تیم‌های حاضر در جام جهانی حسابی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/91993" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_7QeTJatvN6EnShyZwBWasiN-a6vTV7A61Z0LNz8maoPWs268aa9zgW7f8fgT4F4YJEvI8j7kY8qKfFdSVKvsUTeDf6dn8rNvYkvKSCXtbFOx24nuBQI7XCBKI05fey8YrKaH3kiEh-l0V6WJZJ-Q3E83jetoF31gd21FyHop9J67DhHLzFiQUZZkQuwzeiudxNyDbwPyqAXtFBYv0pi2CZGXt3qGgO90DI2X0qxOn7AfmCtezmUBk6C3JKKFfZMQH-6_2aG5A5bn5o07c8piVHo2aUxkq81rtxW3H6RTl3chigCcJg6wtjMRfgKILt_ebs5txi3V4P0kdpKHjujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
امیلیانو مارتینز درباره افسانه مسی:
"اگر الان بازنشسته شوم، وظیفه‌ام را انجام داده‌ام چون به بهترین بازیکن تاریخ، لیونل مسی، کمک کردم تا فوتبال را به پایان برساند".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/91992" target="_blank">📅 10:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=cLyVGvJ3n-hwLZ1Kb16CVsS4VI4kOtf5MUBVGPhH5We_wlHbkiwbulbAB0uB-YiEvWQwUD3M9mfg95QI7CbxkC6Gs8rvQk8JTiMSF9QOf-AGDDLdH_v_22oq9oE3640yWZUMnS79v-i5fi_zshFa_npLPbGh4gbQNQSxfNtnp5FkvMpaiJspEFp-ypZTObxa0gS4rRzoOjDX3QqE9EKssbNrZMj54EpXM1mgPxisIk4WGTUg5RYvv23HYp30N7zKa4879qPnDpUxuKx_r4CYqsJ4clb8Kz7s4CEZ3IGKUZRKbl1r0CEwh4ru_gRh1XSwLfSwvvgybCCQFhNWfgoddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=cLyVGvJ3n-hwLZ1Kb16CVsS4VI4kOtf5MUBVGPhH5We_wlHbkiwbulbAB0uB-YiEvWQwUD3M9mfg95QI7CbxkC6Gs8rvQk8JTiMSF9QOf-AGDDLdH_v_22oq9oE3640yWZUMnS79v-i5fi_zshFa_npLPbGh4gbQNQSxfNtnp5FkvMpaiJspEFp-ypZTObxa0gS4rRzoOjDX3QqE9EKssbNrZMj54EpXM1mgPxisIk4WGTUg5RYvv23HYp30N7zKa4879qPnDpUxuKx_r4CYqsJ4clb8Kz7s4CEZ3IGKUZRKbl1r0CEwh4ru_gRh1XSwLfSwvvgybCCQFhNWfgoddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهار فرصت‌سوزی باورنکردنی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/91991" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Cherki Core
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/91990" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=h-pXp_m9DbJ7g8Etlp5WIOjOQwk9SA-cO-swdb1RqcV_YRWVnRgLQtc-ED8ApP63cukSB4RzZ2NUmhv3VN2Q7LVyOc5vCB7MEUrPmnhHlcDtEqt33EUhpErFnYC5mIQCk_LNkKeC4utBMNszjivXxP1NYhC41JzJrr3JKDu7tXCz8nEXb9W58J3sI8Uh0uJWOZaHC0YAvGIuE8ihZBpqik7U_8ckAIvWsb0g7T6AeA9W_mdBaWpq9b2nEYK3XsIvwTg48rNZcogpAj7BlsuMSwMXyDNhp20UuT1LhN_Mehd6RqnkfXsJlz0klL-x6ToQti4xnRDaOddkVLRvQy1yIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=h-pXp_m9DbJ7g8Etlp5WIOjOQwk9SA-cO-swdb1RqcV_YRWVnRgLQtc-ED8ApP63cukSB4RzZ2NUmhv3VN2Q7LVyOc5vCB7MEUrPmnhHlcDtEqt33EUhpErFnYC5mIQCk_LNkKeC4utBMNszjivXxP1NYhC41JzJrr3JKDu7tXCz8nEXb9W58J3sI8Uh0uJWOZaHC0YAvGIuE8ihZBpqik7U_8ckAIvWsb0g7T6AeA9W_mdBaWpq9b2nEYK3XsIvwTg48rNZcogpAj7BlsuMSwMXyDNhp20UuT1LhN_Mehd6RqnkfXsJlz0klL-x6ToQti4xnRDaOddkVLRvQy1yIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
خبرنگار: چه پیغامی برای مردم آرژانتین داری؟
لیونل مسی: «هیچی، راستش فکر می‌کنم مثل همیشه، هر وقت که یه تورنمنت رسمی شروع میشه، مخصوصاً وقتی پای جام جهانی وسط باشه، آدم خیلی هیجان‌زده و امیدوار میشه. قبلاً هم گفتم، این تیم هیچ‌وقت کم نمیذاره و پا پس نمیکشه. طول این سال هم نشون دادیم که فرقی نمیکنه جلو چه تیمی بازی کنیم یا تو چه رقابتی باشیم، تا آخرش میجنگیم.
این تیم هنوزم با همون انگیزه و امید قبلی داره جلو میره و همه دلشون می‌خواد تو زمین رقابت کنن و برنده باشن. ما یه تیم برنده داریم که همیشه بیشتر از اینا رو می‌خواد. خلاصه که مثل همیشه بازی به بازی جلو میریم، ولی با کلی انگیزه، امید و این باور که می‌تونیم موفق بشیم.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/91989" target="_blank">📅 09:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91988">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9iA8cAWEgJdwWOdN_RHddN-Vn_c9k2wK9CbKc_THI1DxM3SuKhAKxWVN-j3QMBZhgXiYpZSge3LQKiggd-SXQ8_mjInAzd6GaQeXpDviQ01GioX3qvGZrTZ9SAGkA_cZkp9DX7px5ZM4IsnJXZy6ElqRS46ouWlJQrG4oa-0hd0v76-JFBJncXZF4wo2zbfvpIt8Ut4fynOOoKsrq1hKZFFXMlGSaRcYtZ1gjaL0jnmiWwElOXOITIalmSmBkpNC_jUMieET_N-EIfmVRkBJ-ZqbE0dknoteIXP2P2CF9hxe8hSDfWi_DACs5jibV7xhhr7JJN3wR8-5i_3tCEGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل جام‌جهانی در مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91988" target="_blank">📅 09:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvMW_ivgZffQZ9g61QU26JDhVH8UeNVESc4mtej1GF9y5EazakY2eHHffuRreRClFzTqj_hnkjc3gvuaf9o18er829dpj9kikggwvcMT-m9I4hfLMlv4fEC7gJk0fdq1yA1AH8_DJ6hsSZ_NzvrOobdhvjVb6LhqQlsmu_wku9VPA3eQYQKQQ_91kttYAts0IyIqEClltDPYsfv6het9GxIUyxAJqx9xvzcfJPJF_6WRSnhf1ooCG6j9saWik12QwPchTg4pQVFUePlisDEzA6omNTm2jWvyXAsrzSuQ7fNQxWywdgNMJVpEb6oQ_RF2de9EhW3gztr4vUJUVjWOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4g7FYHQE9zexSMxlBVhLjYkPbJ4LYOLz8j2-9DtGgDIUTBd9TSKx7FTk7W6KbH4emzkbcQVbDkcgcNVmKmzsNxQqQGEqRN1s308Pb-bxe7CNJPyMHDnL26r7ezjCe5d920SvhHsVllXEudndJFPunkDXESS-5fRw60VtYsHTO_IgcjiZxpr7SLtgm-pqkGI7PIVxuMSIMo_ewAylNrvVfsamYa-SrnWAEwa0PmEmHgm97SoWr_PFFmwlWwjm1qFsi9FvSdAkHEC3Jwe623VEDzhxkkht8mTdXDlZ6sENybFlMdoHbxqG6NHHtkH4lwBQ3tjFsxybZHrpHHnFA6rRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛ آغاز حملات موشکی سپاه پاسداران از شهر های مختلف ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91985" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=KCSCYvEmV6359lZ_NbCzKdgQVX_ICVYeG0kZu2zyPrvTJkWvjlIftgnau1CG-CszWPimtdWVN81pn_jt8gU7VMNouZY2Hu_i_ZER4QfHkh_XoRx3LWfIZhvjbCB748jbFCdZPUq0DCNKJf07gujpGRPvBsE0QmMO4rMvDkWm09J2qSAbBd6OMLR3zmo9TC5sOG5IdErZrswbAywQ0kDtNYiZ4Qyr-OgrME7UQaFqRMbDmrAQtRdtWHldSIxV7pSRE5yepofe3pxhayoxurmT5oTJvndMN7kl_dZYeaNN52NZaSwUshiNzsniErBONkKpbODQmdJNefKiCfu-u-X5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=KCSCYvEmV6359lZ_NbCzKdgQVX_ICVYeG0kZu2zyPrvTJkWvjlIftgnau1CG-CszWPimtdWVN81pn_jt8gU7VMNouZY2Hu_i_ZER4QfHkh_XoRx3LWfIZhvjbCB748jbFCdZPUq0DCNKJf07gujpGRPvBsE0QmMO4rMvDkWm09J2qSAbBd6OMLR3zmo9TC5sOG5IdErZrswbAywQ0kDtNYiZ4Qyr-OgrME7UQaFqRMbDmrAQtRdtWHldSIxV7pSRE5yepofe3pxhayoxurmT5oTJvndMN7kl_dZYeaNN52NZaSwUshiNzsniErBONkKpbODQmdJNefKiCfu-u-X5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سنتکام: به دستور رئیس‌جمهور ترامپ، دور جدید حملاتمون به چند هدف تو ایران انجام شد و درحال حاضر عملیاتمون به اتمام رسید ولی همچنان در حالت آماده باش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91984" target="_blank">📅 04:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏐
🔻
پایان ست سوم دیدار ایران و برزیل:
🇮🇷
ایران : 15
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91983" target="_blank">📅 04:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
🇺🇸
فوووری از سنتکام :
عملیات های امشب تمومه و کارمون رو انجام دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91982" target="_blank">📅 04:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:   تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91981" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMhGE7eGorI-nblzOPZt5PbldAPGI4euxOBUY0I0jNCdX6HfAYz0PWD6mFqFPSK8a7xjKalwqQqlez4b354Kujn-Xd8y4VZdIMItdaOiabsRZLxLZA0GCXYBex9yjmHvOCdVpmsylwZp6tk7BWetJ80n6jn3csClPZlbOXR32A2Bar6mxqQtXTIiefXkuUEh3PneIm864gKpES-ctjbjuqvDT8FPwp6HzrOYe4VHbEKE7Z3TUhHZRf5wbJu0EcvlXg9mTi-8qOOEJxcUYR62Pmj8WLDX43ZJc5xmTrtOdvI9rdEJCoGy-WJCI5pZ1krEjZelIQi7NufAkK1jrM4RlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:
تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91979" target="_blank">📅 04:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993f547a79.mp4?token=lRKu7XXFlAHyOa25fWNGs35y-xoXElxgT8dXQ8lYQKJ9BVu89pVU5aRvSgDttF_9k3jEfdZl8NGDOda6D4CKi4a2EalYtiw54MbA3hb3M8Il1zdqTOBVQIUrPcL6J6qvJ3v2OJgfzsH4r5iV32uZP4B829Gi93awpKf8WSMn1Wx7LaPS-Q-n3Khem50e0ShOVo1QKn8C-kn-FOR4X-VW-kvJjdtg2HUAedhK5LhNKXDEWFk3diBDbyshxkKEzgFZKkFYmISaTg7D3MjbR2NqnRY2MBugmZiD_ZpLO4-YFGWgINMcv0-qfp2mg5AKdd6r72h1Yo2O59m18huX6ILHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993f547a79.mp4?token=lRKu7XXFlAHyOa25fWNGs35y-xoXElxgT8dXQ8lYQKJ9BVu89pVU5aRvSgDttF_9k3jEfdZl8NGDOda6D4CKi4a2EalYtiw54MbA3hb3M8Il1zdqTOBVQIUrPcL6J6qvJ3v2OJgfzsH4r5iV32uZP4B829Gi93awpKf8WSMn1Wx7LaPS-Q-n3Khem50e0ShOVo1QKn8C-kn-FOR4X-VW-kvJjdtg2HUAedhK5LhNKXDEWFk3diBDbyshxkKEzgFZKkFYmISaTg7D3MjbR2NqnRY2MBugmZiD_ZpLO4-YFGWgINMcv0-qfp2mg5AKdd6r72h1Yo2O59m18huX6ILHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در کرج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91978" target="_blank">📅 04:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-U4b99g72W2MZGcoumtxMJwlslHA-_wDgR9ySbwRXJVJgJLHI8YWJE1vTVjRZHyMNBk__ELQOLTbDAHog8dnJN8FHlHHfNEJKf_SYR3cm8hBgI2qpRU3Bj0TGLjc8Vx8Z-xOulIOGwIwADhlYIu2tNgWJvSpSlrksk8lsiGR0aRb32_KdLPHsXsOq0yep7zEC8Lx_rqpqgtZWiJ-mvFwtsry64cPTlAF-lfg5hxo92v_6ois6ZVNtqU4py2pnDutIXaYSMtbR99BNNJ7QgUyHKvjABWKV0CD-LjvjR9rUVumeAM5dWq2XYpQw7QCFbftAJ_Xrqeg2IdUH5zfCshjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czAe_Dd6jfOu_NYdvZ4rgmW1Qq6AC9NDCRXZE0GcCgFZtRFnBMsQSmwrjFXk220Q3BcR1pHXMKmesWWiymS_tqbQuwJnt5hDx1PaYbAw_ikqTHAXATJxvsmUC7WKO6QYyo_RmkSFWqFhB_7SGH8NtS3ywZ4JXTULGJSkAvuYJEuN5Tn6hOTdG-nHOS7ifgKcaWEkTN6eD0JR1zGDVsbtOhJ6gfJ6QoQAQAnQ-wsb2Mv5ysj6lS93zpTmU9Dflv6D7U3lVSHRqlkRpMZCdfwf_iMcg84CjXlluiDeSwXxpsorha7Ph3mMeslKlDTo3zqJpVoUEQSCEPH2eu1AkSkfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqacLj-e5oEdwlIiRb7UEZ7-kPmXmkKmmZTLrcVvoJsaPzvOhwgcLI3TxB36BSmseIc92FkHU1zScNbmn3I35qwvnI8cF8oksplxbJFnTJTa9RKP7YW0jjNvCS4lvMs94wRXcz3ER1qh4nm_Pjo3s-QMbfFCH0A-7JYaq2SB9Fo-oV2hEqJdDx8FPhnCZXjp4_r7O1JNwxFDSs6aaVfg2tVpZ2E529EytPDzVqEshBDP2QEj2hg173Jthme6GrKofycfUqEONuFwg-Rwa8-9qZzhj0Xghl-MFGue5G6n9n9K_Hwwk4PpioslguO0-_2m2uyqaBZJMnkXCTm-DLT2tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش مناطقی از کرج هدف حمله قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91975" target="_blank">📅 04:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏐
🔻
پایان ست دوم دیدار ایران و برزیل:
🇮🇷
ایران : 25
🇧🇷
برزیل : 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91974" target="_blank">📅 04:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران : 21
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91973" target="_blank">📅 03:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=ZnOlncIcwVrd4eXJ1j0qwd4GzeG6Svz5wmpfWnIUpLdurK-Df5FPY_YmdEIMb-D5KvfObgOPixkzcO7erbkIQlZ5_y9_iP-XPKEqrw15-H-NZDCri84Fy9PLHO306RNcs4xa7SZFC7kh_jHXbX5O1jM8UECEvTr2V0ALqX18fN_VSaAM0UOe4Q60jaHtjV5Rzyi1fel4cV3PEMURtukG15_u5ZGVgp5yexjtc90g_QFXYrEBZf_ZG13EdJJSygWmtgGRydRGmXNGw19LfZ5EbXbFOIDmT1g_DXGjHo4aofV9QrL9RVU5mk5YxHJWa46AP3WVaTt-7MuhtuEHlnXoBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=ZnOlncIcwVrd4eXJ1j0qwd4GzeG6Svz5wmpfWnIUpLdurK-Df5FPY_YmdEIMb-D5KvfObgOPixkzcO7erbkIQlZ5_y9_iP-XPKEqrw15-H-NZDCri84Fy9PLHO306RNcs4xa7SZFC7kh_jHXbX5O1jM8UECEvTr2V0ALqX18fN_VSaAM0UOe4Q60jaHtjV5Rzyi1fel4cV3PEMURtukG15_u5ZGVgp5yexjtc90g_QFXYrEBZf_ZG13EdJJSygWmtgGRydRGmXNGw19LfZ5EbXbFOIDmT1g_DXGjHo4aofV9QrL9RVU5mk5YxHJWa46AP3WVaTt-7MuhtuEHlnXoBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
کارشناس فاکس نیوز:
اگر ایرانی‌ها توافقی را که مذاکره‌کنندگان آمریکایی ارائه کرده‌اند امضا نکنند، چه اتفاقی خواهد افتاد؟
🇺🇸
ترامپ:
فردا شب حسابی بمبارانشان خواهیم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91972" target="_blank">📅 03:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران
:
21
🇧🇷
برزیل
:
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91971" target="_blank">📅 03:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91970">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
بمباران بزودی متوقف خواهد شد و مستقیما با مسئولین ایرانی صحبت کردم.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91970" target="_blank">📅 02:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91969">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⭕️
🇵🇰
پاکستان:
میانجی‌گری ما میان جمهوری اسلامی و آمریکا به‌پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91969" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری؛ قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91968" target="_blank">📅 02:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91967">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZLcNlDtCBqJBcDU_vNI4ZfkScvkUcA2bd0ITz6mXVO2hjozdCOLIpE32-eR-YnYd0XRxogYPxs6E1T705hEwTt-ku-Xi6KNIRqAgAA5vzc-QpjKrhGW7rlzhgK2Sp0_XPqnpT5cAF4vj2VFwtoWGdX7FyvLAklNAO2o62DYbS3Nd2QVTEZJwerdcEws9NXMb-EENV7NgWgKwHtGonn_R0bgwolfGQaI--9Abj8iULJ6SsvpbRPfRM1XEodDtycdNg4fwXysYKhEP8KbF8EXyl9QDcXayOajtbP_R3BAZfaSOCRgL3ShknBOf1cspl_vEJwQxY67yoUgEnaFi8jkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
صداوسیما: تنگه هرمز مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91967" target="_blank">📅 02:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری
؛
قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔸
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91966" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laLd8zwCAbUZCv9FVU9FNqUhBznCGs1Oj4i15NE95HT68j1EvVBr17LwagubcUA2pkZMBn_MMbJEQD5i-naj5W-t99jKVvlQ9SwIO0YtbJsKehstC07YY-diCf6sdd62RrON5oKZ34ka9sGKF0QMVOxsLRTEECNRvuYdu0_zsklI6EhCPtjYj10TU2nIgjVj8tVVxb1cRCbI92iLEPd4YUj_mZtBRKNRY4otYzdcDktP-do6M5l5TapzdDB99s8eY6WMYewaNOeIZ6gLjLHUoUvBh5OkQsUqziLFPLWZ4sByF3a2wQDioITeEP0nXZxlOsGyFutUSzVCH8gs5DunBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورررررررری
؛
پرواز دو سوخترسان آمریکایی در نزدیکی مرز های آبی و خاکی کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91965" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انگلیس یکی زد به کاستاریکا   عشقم گوردون پاسگل داد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91964" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
روابط عمومی سپاه به خبرگزاری صداوسیما:درپی تجاوز جنگنده F۱۶ به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91963" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری؛ فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91962" target="_blank">📅 02:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری
؛
فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91961" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezUdENBxe4va3zrFu6kRf2CzecpUY3G8zbLJ6dn9QpIe0bV-PWrjN1b7D_NnmlIg5SajzPgBYZaVGmbEM66PZUr2pR_XUo0FDupaJof8zSWtws8PqjTu0bdeqAOArg0-uLLdF1OQ9RsGXTVHZxuaSoTfagGyjFDdjhWLl_7sFrFHEcUho8UVQbvh8zLC9nSw4NlPs2Xp75j6wjV4ziZbBSV1hp2LSEbsrbq4umnZBHuigymjTBX-JAe4ku72IYMN6WL4NmgZ3NMiqxYAvhXJL8g_IQ8VxVSS6TzjYijrUf-ctoM9dQFwqKRlOCs-P1701huIXTyFjqUbJA1xgPUoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
شیراز وضعیت یه پمپ بنزین بعد از خبر اینکه به عسلویه رو زدن شلوغ شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91960" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
لحظاتی دیگر تا سخنرانی دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91959" target="_blank">📅 01:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇮🇱
⭕️
مقام‌ارشد اسرائیل: در حملات امشب‌ به ایران تا این لحظه حضور نداشته‌ایم و در صورت نیاز اقدام‌فوری انجام خواهيم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91958" target="_blank">📅 01:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#فوووووووری؛ صابرین‌نیوز رسانه سپاه: الله اکبر. یه ناو آمریکایی رو با موشک زدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91957" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ برخی منابع خبری از حمله به پتروشیمی کنگان و‌ عسلویه خبر دادند. امیدواریم تکذیب بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91956" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
صابرین‌نیوز رسانه سپاه: اختلالی در اینترنت بین‌الملل دیده نمیشه و وضعیت پایداره. نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91955" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZWyzLkH34W3XVgrHP1pJX54L9S0z8NZXK1J_SbkYm2WVVANTAnSMdZQ-gx4Ap0iyl1Nw_Q_eQ39qpCI2T5PmJBJ6x4ikWkeFoakOogth0jRZJ7ccU360uEQcSES3DVsuN9u5n2y9BoeqiAUyRKyuWt4QLXvAoAUF0XaJEIjO68Ug28kUDQUEOlk6c2abqZWTg1T3-6Z4Z8LXEQkks9QuJad23CPRNVwve2i_dEaIQuHDqJX2HqiSG7VdDEtYifewz_UPc1IbqoBtdV9a_U0Vkumn1YP5efjPzu0PU_tvHAzC8QoQJpjBkvZSkOwfeerEtm6yfQPb0owsDSBZHVV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توئیت جدید صفحه منتسب به سید مجید موسوی فرمانده نیروی هوافضای سپاه
:
بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ
- فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ (بقره، 194)
- پس هر كس بر شما تعدّى كرد، همان گونه كه بر شما تعدّى كرده، بر او تعدّى كنيد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91954" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#فوووووووری
؛ صابرین‌نیوز رسانه سپاه: الله اکبر. یه ناو آمریکایی رو با موشک زدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91953" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فوری
؛
صداوسیما: ترامپ بدلیل پافشاری تیم مذاکره کننده بر حقوق ایران در مذاکرات و عدم امتیازدهی به دشمن، جنگ را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91952" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
💥
باراک راوید سخنگوی ارشد آکسیوس: حملات امشب به نقاط جنوبی ایران خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91951" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ صابرین‌نیوز: هدف قرار گرفتن نیروهای آمریکایی در نزدیکی جزیره هنگام توسط نیروهای دریایی سپاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/91950" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
#فوووووری
؛ انفجارهای شدید در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91949" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی‌دیگر پیام ویدیویی سخنگوی قرارگاه مرکزی خاتم‌الانبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91948" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-poll">
<h4>📊 پوشش اخبار جنگ اینجوری خوبه یا کمتر بزنیم؟</h4>
<ul>
<li>✓ خوبه راضییم</li>
<li>✓ راضی نیستیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91947" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
وال استریت ژورنال به نقل از پنتاگون: این حملات اقدامی از دیپلماسی قهری است که با هدف وادار کردن ایران به دادن امتیاز در میز مذاکره انجام می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91946" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ گزارشات از موج جدید حملات به بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91945" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91944" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=aKpguC9GegYuH3web1TJ7ie7YXEk0tj2a44bssQdYXmujVrpQONLkSnnDO2fdMId86b3Hx_roB3wbisv1LssjEDsUIMItCwByMM-OV1ENXu3qwSX4o848FDbL05deVze5uHgqH7nu8KOjEbOK-RGXao7EWUkFTWVQTPOgbQzV0CkzF2ORA98yN66srMvaQdCjqVpIha3XmBHX85w94PjZqZV3TWckK_sA2X1uetvCoGl-aDv2jeS6T_UuG3qqpor-fr3FFD56AbVWbuxEF95bVymjxw4lDclEl6Ds8RggnW7kyO_gJbZ-LLJLwo1Gvshnsg0kXNQ1eII7SYDuhtQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=aKpguC9GegYuH3web1TJ7ie7YXEk0tj2a44bssQdYXmujVrpQONLkSnnDO2fdMId86b3Hx_roB3wbisv1LssjEDsUIMItCwByMM-OV1ENXu3qwSX4o848FDbL05deVze5uHgqH7nu8KOjEbOK-RGXao7EWUkFTWVQTPOgbQzV0CkzF2ORA98yN66srMvaQdCjqVpIha3XmBHX85w94PjZqZV3TWckK_sA2X1uetvCoGl-aDv2jeS6T_UuG3qqpor-fr3FFD56AbVWbuxEF95bVymjxw4lDclEl6Ds8RggnW7kyO_gJbZ-LLJLwo1Gvshnsg0kXNQ1eII7SYDuhtQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنگنده‌های ارتش بر فراز آسمان تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91943" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUZMCnjGDfI1dffiKDs-I2Bq0TKyrzcKqrcgZLbTQAU8W-ylkx2Tc9j9g_VNW9YUUkuW_RuI4Jp8Fxmz9j071fm1vPOp-6t5TG5b_TLDVRxY_t8s2D6trIDOqTugB2oOMLagJIxeuOzvinkDgaTfY5pYN9b0VWTFp5oT3nwnInHPx0f5nnuJkuGQA6qg0iZWMs2H85r8b9dBPqBcTGc5OUd8AUl_835giiOIzo7u1MiEqqtmssMn0EbiaLjBUygfj29isioPWszoFLCuGmk9LqCs2QeEjae6G5ARujJsd8zmJ4a71iffz2qeFRqx089F4iAzKso5xN8OQdTIsrd0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
Betegram.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91942" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ برخی منابع خبری از حمله به پتروشیمی کنگان و‌ عسلویه خبر دادند. امیدواریم تکذیب بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91941" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووووری
؛
منابع خبری آمریکا: عملیات امشب سنتکام در تمامی نقاط حیاتی ایران خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91940" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از سنتکام: نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، چندین حمله دفاعی علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمی ایران انجام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91939" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kokUW2YJqyMvr6F9Luws4AlzHWDzhT3K6bUhfzEikQJh_8otgtnQElTlROcFOMo1Q16q6iVnpweUnO8c8UUHomfD-_6-rYzluCYWrdvw3cPG4ioPQmSZdXQiO0vXvwTVFsu8EYA7kFc60O_71vFWRkz4zejlLjkei87_J-tt78F5jSrZq_J7vqmyhxRQjMNvXOeQufK0pu4TzKXduvsMuSiJFt1W32IgDOYPiEQ-VPbDefCNh_Ne0SLr0DOKvbEpEXWWVMp_18K8EN0inQNEq_6NGwPIi18fGJaQejHLlELHck1nOFCkJ0QXOU3MZu_uvf51v8Y1Qo1dw4LjnWpJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از سنتکام: نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، چندین حمله دفاعی علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمی ایران انجام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91938" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فووووووری
آکسیوس تایید کرد؛ عملیات خشم حماسی در فاز دوم با قدرت ویرانگر ارتش ایالات متحده آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91937" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک سمت جهان جام جهانی یک سمت جهان جنگ جهانی
خدایاااااا بگم شکرت خندت نمیگیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91936" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فووووووری
آکسیوس تایید کرد؛ عملیات خشم حماسی در فاز دوم با قدرت ویرانگر ارتش ایالات متحده آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91935" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در شهر بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91934" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ مقام نظامی آمریکا: مقر نیروی دریایی سپاه به عنوان اولین اهداف امشب در سیریک‌بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91933" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ اخبار تایید نشده از شلیک اولین موشک‌های سپاه از نواحی غربی کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91932" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2a236d0d2a.mp4?token=IsguMnJ9Fg5Pcq6OSLB8uc91PaIZG8UVqbVQwGclD1snj3c3JHujYB0geEdMnZ-8Quy1AXPWdNSWVhtk3lz8iKH_T3hDeU3JI6p3IiFt47okpMJK_ubXOG-1jDuN6VvL2XBUc7k8LwyMXJp1aeL6dbkD7KQ72-f22j7_ekdcFs1gBskNWkJqCOuJkYm8_LKbAKkmmHv0QaKwEpmWzyKlI0sSdSS2hfPJa1z085yqaAIPKt2cH-xlooyVnJ98JCAjWqzuIOyshteAjTGaDDtdd_qdVGfQN-rBKbU-V3NjSHCAqwGLVxsfNobuV_0vQDezf54AM0R-Ghg-aI2ULvon6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2a236d0d2a.mp4?token=IsguMnJ9Fg5Pcq6OSLB8uc91PaIZG8UVqbVQwGclD1snj3c3JHujYB0geEdMnZ-8Quy1AXPWdNSWVhtk3lz8iKH_T3hDeU3JI6p3IiFt47okpMJK_ubXOG-1jDuN6VvL2XBUc7k8LwyMXJp1aeL6dbkD7KQ72-f22j7_ekdcFs1gBskNWkJqCOuJkYm8_LKbAKkmmHv0QaKwEpmWzyKlI0sSdSS2hfPJa1z085yqaAIPKt2cH-xlooyVnJ98JCAjWqzuIOyshteAjTGaDDtdd_qdVGfQN-rBKbU-V3NjSHCAqwGLVxsfNobuV_0vQDezf54AM0R-Ghg-aI2ULvon6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس یکی زد به کاستاریکا
عشقم گوردون پاسگل داد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91931" target="_blank">📅 01:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ اخبار تایید نشده از انفجارها در برخی نقاط تهران و کرج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/91930" target="_blank">📅 01:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ پرواز جنگنده‌های آمریکا از پایگاه اردن به مقصد ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91929" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ منابع خبری اسرائیل: در حملات امشب، احتمالا جنگنده های امارات متحده عربی حضور مستقیم خواهند داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/91928" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارشات اولیه از انفجارهای شدید در اکثر مناطق مهم جنوب کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/91927" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ حمله به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91926" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛ انفجارهای شدید در قشم و سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91925" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
#فوووووری
ارتش اسرائیل: در بالاترین سطح آمادگی نظامی برای حمله به ایران قرار داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/91924" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
#فوووری؛ فعالیت شدید پدافند تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91923" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
#فوووری
؛ فعالیت شدید پدافند تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/91922" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛ پدافند اطراف زیر ساخت پتروشیمی‌های شهر عسلویه درحال فعالیت شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91921" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/21a0fba9b9.mp4?token=MNt2dGT0ooyyL9biR5AdvTZK_gsDO5daDyZiZz0Mp5VMe4GRSXmcDas4Ihgkz_7OiQ_MVJpR971sPLKVlbzTFlsRGN3U8GTVnWWxpJAxrme7E1xQymzv0LT4788UKWmPK7nP3AyWrlPQyg5zHFO6gwEgaCukTY6ELDpHhp7ajEW8BTL-kNJJUnhow1f8cNf8Ow8tjR8Fl5iQ6BtovBssZw95WoaU8GfkEgcIVMgDSN-pAuJZLdb5bwd7Rxe8Cz0-zATfY9XDKKjFcV3LzcHuHRLkbX6Zbe63sv_l8YRp-UNimzqsLW_lz2TmrSzGkYuHUSAylTmb2Mnh6zuaCPbf3g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/21a0fba9b9.mp4?token=MNt2dGT0ooyyL9biR5AdvTZK_gsDO5daDyZiZz0Mp5VMe4GRSXmcDas4Ihgkz_7OiQ_MVJpR971sPLKVlbzTFlsRGN3U8GTVnWWxpJAxrme7E1xQymzv0LT4788UKWmPK7nP3AyWrlPQyg5zHFO6gwEgaCukTY6ELDpHhp7ajEW8BTL-kNJJUnhow1f8cNf8Ow8tjR8Fl5iQ6BtovBssZw95WoaU8GfkEgcIVMgDSN-pAuJZLdb5bwd7Rxe8Cz0-zATfY9XDKKjFcV3LzcHuHRLkbX6Zbe63sv_l8YRp-UNimzqsLW_lz2TmrSzGkYuHUSAylTmb2Mnh6zuaCPbf3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو
😂
😂
😂
😂
😂
چیکار کرد دقیقا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/91920" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست. اهداف فرا منطقه‌ای رو هدف قرار میدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/91919" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ رسانه‌های عراقی: جنگنده‌های قدرتمند ارتش آمریکا درحال حرکت از آسمان عراق به سوی بمباران ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/91918" target="_blank">📅 00:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری ایران اینترنشنال :
جنگ شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/91917" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91916">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G0IMQ_vs4G4m0uGgYhmKApnOhOH_9HBpgWx-rC1JlQdGURxeMg8APWfRpb-NX-rB3Z1iJRYXdQC25tsN5eUl_JmuATX8wmcZgILLdOESXhSZdiCnT-2vnW7Ocj0-Bp831VVOSQxcJp57OL-yz6ruaoU5iLKwqK3Gn7039e-pqPECyjifOtSsWojTfAawTX2msa4YGIWc9LDHHUZEBJ75s15NvA62r8-EkcstPdC5bQ8O-AHo1LKmssqFz41WpG5p3itOn_gyDJR5j5ulwyg8CtGViojNeV-402vLDutT1C82z1MEX--dSOtNq93xKRCbGhf1085RTfU7nDnrsMmCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#
فوووری
از ترور آلارم : شب بخیر تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/91916" target="_blank">📅 00:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای جنگنده در استان لرستان
البته برا ارتش ایرانه
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91915" target="_blank">📅 00:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
فوری پیت هگست وزیر جنگ  امریکا:
امشب تاسیسات اصلی ایران بمباران خواهند شد، این حملات شدید و قوی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/91914" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن فعالیت پدافند در شیراز و کیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91913" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رونالدو
😂
😂
😂
😂
😂
چیکار کرد دقیقا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/91912" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKIetpEKtCc8H5h1ZNRntQMchHNiZF8cJ1cCsfZdfxOTOr8oHZ924tjXGindqLie2BiOkbiKEUJy4FNjaETOQlgqbhEYcY2dHTE_csPGrcdzmuXx4HzpWppg7oun1IzdJxCOVZYCTYIqgw2alSXbFyhfmG9TUS6cMwI-lNP0YEZMYm0Ytofp-LA8iNZ8AzP0vXpeRwoAI7SKO7BhUFN6L82QZF50ei89oP6SDmZwdWYAj1L49hsnvx6RzZ4tY85OmMZP6vBu1SV83sQhfwLQwGJk-zD02HSVWXeVy0uWIfWNdN7ZyfLBWs6ae-b0w_Vn3TLEmSWybPSmF27MhI1dCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکای اسپورت:
🔴
اتلتیکو مادرید نمی‌خواهد در فروش الکساندر سورلوث عجله کند و می‌خواهد تا بعد از پایان جام جهانی صبر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91911" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
‼️
#فوووووری: هگست: شب بسیار سختی برای رژیم جمهوری اسلامی است زیرا تمامی تأسیسات آنها بمباران و‌ نابود خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91910" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWOAh7OrWJ3W34tGLDbM_dMnyXml9UuXfjqO75Gq9qU5pBt4DxRgHAVDgqOzBigvPwD3JEox0oqomnWPtcNd4ZposKjc2Q3uwfug4oAmQGmczmWsohdJaoS7kUTdYP_bFIMWV9wcAvy91oBTmoTxH1oJuKZCeueV1YzR5VgDQ1UoPrD4lUsLmdOXtSqISGWgtLKnK9axzptN9iHsjIlA0JJBd_li1cfQcJlCOPMg7obp6-mIG9gXiLIymB2VLb1oieNnd2J8b5G54YU3hE4kSjryiwKV4AOSHa_0xTW6GXtiKPnQNvedhe5JhGIrNIAo49ZtwBs9jYu3AgdzWK3pAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
🇫🇷
سانتی اونا :
باشگاه بارسلونا در واقع پیشنهادی برای جذب گوارديول آماده کرده!!
آنها آماده پرداخت 80 میلیون یورو + متغیرات هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/91909" target="_blank">📅 00:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
#فوووری از پیت هگست: سنتکام امشب درگیر است چون پرزیدنت ترامپ گفت ما امشب ایران را به سختی خواهیم زد و این کار را می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91908" target="_blank">📅 00:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=klCxe8yf4mJiQZWi3iGpd7IlVAYuc2k_U4hJ0bFVntw-j39GwAw_pziTWldt2Qe_K6qv3NDBC5sY6NgVOEQzFgOnIszcCUaOdVdrHIpMTIiRusZZlUJkG52cGjE54I34Qvtpt9IHIs76VkuJLQN4T7zQ00073qQtZm49-t7DwKq3IX_HJXv0WVUhyKhmZzmUwfafvrYcnhayaDQuFeLXcpBC3koJvXNx6iytLRFD_nzlY5Pk4D2ChVo8d4h2sYnGsgBSyr6DyiK0LPK0DrLjfQMb0dv92LsPN4r5ak1VrOdqJFYdcWqXDUoJWWcwa1xc9BXjJ07Div9Wem12KofEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=klCxe8yf4mJiQZWi3iGpd7IlVAYuc2k_U4hJ0bFVntw-j39GwAw_pziTWldt2Qe_K6qv3NDBC5sY6NgVOEQzFgOnIszcCUaOdVdrHIpMTIiRusZZlUJkG52cGjE54I34Qvtpt9IHIs76VkuJLQN4T7zQ00073qQtZm49-t7DwKq3IX_HJXv0WVUhyKhmZzmUwfafvrYcnhayaDQuFeLXcpBC3koJvXNx6iytLRFD_nzlY5Pk4D2ChVo8d4h2sYnGsgBSyr6DyiK0LPK0DrLjfQMb0dv92LsPN4r5ak1VrOdqJFYdcWqXDUoJWWcwa1xc9BXjJ07Div9Wem12KofEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوووری
از پیت هگست: سنتکام امشب درگیر است چون پرزیدنت ترامپ گفت ما امشب ایران را به سختی خواهیم زد و این کار را می‌کنیم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91907" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91905">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f735cae0f6.mp4?token=HQXMlzQn000ic7Vx-EsibmmC1EKsXufDOocA4TS_8vKDaokb_-AqigKCA5j-CQ1-UMC_mUk9fjWgHzOImeee_XU6izWqBTdOWP8xcO587ebPvERLLjGQZ6WsTMuSzrZ32OGmWQWjDuKB5hvp6dNA1J_Hvk7_6ot3eqNSU43Xu4daSy0FQ9CG1ArZUixm0Y6PFWRJgTVtczh3qPr1XKH6Wq9o73XWnjhZV0uklpJQagtOVZTqeyjx7O9VZO1RJ2cUGATisD5oxzhtehnXeM3e_a74vIcomDHZj5hJVMPrgSjpakQ7wHKPs1QQVY4jGOqd_H1xtzvpcWp7bfKj9Pj1ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f735cae0f6.mp4?token=HQXMlzQn000ic7Vx-EsibmmC1EKsXufDOocA4TS_8vKDaokb_-AqigKCA5j-CQ1-UMC_mUk9fjWgHzOImeee_XU6izWqBTdOWP8xcO587ebPvERLLjGQZ6WsTMuSzrZ32OGmWQWjDuKB5hvp6dNA1J_Hvk7_6ot3eqNSU43Xu4daSy0FQ9CG1ArZUixm0Y6PFWRJgTVtczh3qPr1XKH6Wq9o73XWnjhZV0uklpJQagtOVZTqeyjx7O9VZO1RJ2cUGATisD5oxzhtehnXeM3e_a74vIcomDHZj5hJVMPrgSjpakQ7wHKPs1QQVY4jGOqd_H1xtzvpcWp7bfKj9Pj1ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری ترامپ :   به همه پیشنهاد میکنم امشب حوالی ۱ تلویزیون رو روشن کنن
👀
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91905" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91904">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
فوری ترامپ :
به همه پیشنهاد میکنم امشب حوالی ۱ تلویزیون رو روشن کنن
👀
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91904" target="_blank">📅 00:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91903">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGx9c4p6ZrRuWRSfKGMMJqFD2nyq4crT9Ib7_4dkEu3SUKPfS9d1D_AZbTvM4YlJcudzzBq5bHH8aeIIiXTvebop8pcDgDxm_MQSKyrFTds4LrmkqrRdyQZt5IFxCPy0y8xkaicgkrbpK7TaK3RUWJyQt5EbQ8g_KTakQwvCvYcrVxWLXs5ZZkv7OY0wiUcE99gATe7IgJNSmBeKn_wwa79v9vT3CfGE6E74N9-00OZZUjLq3Cl0zfGv4U8y4FPcMmYtOXgaLBGMdVF6i_RcitGliD8aLF6nfh1R8IFe5miwHibfa4OtRwLz4K9TOqHyJwMidV-zNEZv-XvP4AEpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالک حرمت داره نه لذت
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/91903" target="_blank">📅 00:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krDg7dzdJ2GlBAk8z7F1K_6wPDX1VvbhEB-MJJIB8gdz-jAJa4R_vzT-sko3k2PCNDk4wpC0KYfVnbZqz8oe5teAV5ggafCkyU3vi6IpbpVtFikZCHpZvEpBfAtz7SoBBVyzBQ9mHA-k11bAvkOFB7fRWpLuOuXC02gr2dUetxy74Nw19IxRO4TRCiunZRP8iosfudwBgDKDGnhKyI70jwEdjS-jLjEr3is8HGmC7gCxwvooaKREYg0ZLZX_RUMu01Q7_yF4vfVrw0j-DlFLEZaA-IjU91WGKS_tSMoHdZDDvSpCCkl54cj-ZJiou_xq4gwLv636r_MH_BvqEWPKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ به نقل از روزنامه لکیپ فرانسه، پاری‌سن‌ژرمن با ارائه پیشنهادی نجومی بدنبال جذب اولیسه ستاره بایرن‌مونیخ رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91900" target="_blank">📅 00:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا رسما درخواست میزبانی از فینال لیگ‌قهرمانان اروپا سال ۲۰۲۹ رو به یوفا ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91899" target="_blank">📅 23:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ffd2bfee.mp4?token=qagiKvUfsM8hUd6TT6PRZ-UW4PaKWrxMLjkG93MD9TiII5lR4IzL_sZwzoTUGRk-9ePz1xrYw9SQwhcx-Dd9qsBYmI6JFv50WE9A-iG2_qiBiQ8GmPvTnpGBBuA7VVgPABZQRJeBRZj6GxgvjDgZCpS0k_G5bUrq8FQPib208BstGL5NQo8ftd9EFyKuPLQsmKRA_URYb2dB675Ov0RGAwpgcGwqbF0F4_w-z7lHHIRuYQAXXZOL_0vQodwDfFn3XDBYa4os_1g0pSKdWwWZnZqWkzP-BEkuH5CTKoUDUJkcmW0vzC9AKJfIY3x4r_TQ-VgU13eDgGUoRMWvzdnM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ffd2bfee.mp4?token=qagiKvUfsM8hUd6TT6PRZ-UW4PaKWrxMLjkG93MD9TiII5lR4IzL_sZwzoTUGRk-9ePz1xrYw9SQwhcx-Dd9qsBYmI6JFv50WE9A-iG2_qiBiQ8GmPvTnpGBBuA7VVgPABZQRJeBRZj6GxgvjDgZCpS0k_G5bUrq8FQPib208BstGL5NQo8ftd9EFyKuPLQsmKRA_URYb2dB675Ov0RGAwpgcGwqbF0F4_w-z7lHHIRuYQAXXZOL_0vQodwDfFn3XDBYa4os_1g0pSKdWwWZnZqWkzP-BEkuH5CTKoUDUJkcmW0vzC9AKJfIY3x4r_TQ-VgU13eDgGUoRMWvzdnM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
عجب موقعیتییی رونالدو امشب رید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/91898" target="_blank">📅 23:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoVdb-n51-LDdqCvFNwxwtuxfH6H-eJMOTZ_X8h8h1vSovg4xhmYU6yIYlFV8jSEdPOUqM6Rh5Qgq5NTs4LetBF7LHnrFLRUWxIe7nNppVYNkev77qYt879mpPKpP8rx6JNW3t_Z-UurwiR9FmtZO43d5HVBHzp-n83y8P8xmSNKeyUiS6ql944aPVhdJWBZ9_Ad1R9gKbwfMPxdWwKTgB8S3JPCmkvLVCgjb8rvvXwX2B1nSQ-hMAuhA7AQM_8NhEBaWPbGxKwACn3FXaxOdKX4wfkBlLeMgVaHUXrdoWkndSjDxEn2-u1oTnz2kFdQ5D5Jqdp6rV8g--LKoadphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی:
🔵
در حال حاضر پس از رسیدن به هرچیزی که آرزو داشتم، سعی میکنم با آرامش بیشتر بازی کنم و از آن لذت ببرم.
🔵
درسته که وقتی زمان مسابقه فرا میرسه برای من دشواره که آن را به شیوه ای متفاوت زندگی کنم، زیرا در طول دوران حرفه ای ام همیشه می خواستم بازی کنم، برنده بشم و رقابت کنم.
🔵
اما این تیم مدام ثابت می‌کنه که با همین  ذهنیت برنده وارد هر مسابقه ای میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/91897" target="_blank">📅 23:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0ll6bjz1_O4d6lJ9fNaLNhINOyeF8c06TDWqpXfjaHsHgDknGPBoLngZ_cb5lGL-Kd5XgoFMJf4u4A6COddQMt7LG1eexRpgreLn4z5u5GeLIMy4EIuPixM-Nj98xEH_IKNAvbNuslkLPTbWYshE0v6D8jWV3pm7usc4jlHu83mIT5fgUR_cFAQCBE_Ms3UZms5ICx-1QhwrEDAtd5orEp2C5-Lzse4nzTAwegEG-onFvaFBEd0muJ1ldrg7tbyiS_HzuhRsRDl4-pUGP8Ak9uGzIQErG_80HQDRhdz6xZrwMD1jfQs_wb5_cf3Bq_qO6-WDuV80d5K6JrdAcMq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیانی اینفانتینو:
آیا از انتخاب ایالات متحده به عنوان یکی از کشورهای میزبان پشیمانم؟ نه. از هیچ چیز پشیمان نیستیم. اون‌ها قطعا میزبان بسیار خوبی برای جام جهانی خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91896" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
نیویورک تایمز: ایالات متحده رسماً از مذاکرات کنار کشید و راه های دیپلماسی رو به خاطر اتلاف وقت طرف ایرانی بست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/91895" target="_blank">📅 23:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrvNZe8BUKaMMEIOFf__nxXQUvTiTkCImdmog2fI7iQkirK6hYFhjx8lsvtSFfkqpaWBiTVrrH6-l-7Dor-pQ7czBoz5oNt4paDsl9FOFeViWvh1GRt4zRSLxR6Js8qddYT-8hk9uhTkBY2KjKo_3H8oRinK71ybzL-gwxS320NVjAsJAHdqHfW8vOFbs7N8rqXSuc5AIuBWgJMuJTp-NRzj4UeQQP08e-xTjxr2xbpQVFrhsZFyUrr0w8JroR2wba9IPp51oS_u1gAMylM1AcRlfpv754ki6xLTtNJyPSHhrR9Gvwg7h-cBAO1BWMvEYiZ-0bKj4ieHncKu2WmsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
اعلام ترکیب پرتغال مقابل نیجریه؛ عجب خط هافبکی داره پرتغال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/91894" target="_blank">📅 22:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1eCnnwa1ZeXRnJJ2Zr2dz3FRozgd95jxOONK1Yk3hKfndunbwBek_ouvsVzQwHQ7wbdWqXzy9NTxr-Nh9zDj3QnnqJEMwSTa92DYT8jQwOUyC1VCFuieaDYrzV7bfZsfyvoagNg9EShEL9kzDvCHwgFRdCuLNVkQ1svz-Cjt5Pi8KdbMaPJ8jxgQ1OOcA5i9Y_J86jNdFRx6vOKqfPwkq0hdeHXbZJXyxAAJ18SufE4dQkFAC2_Lb6hiJ-iCoGlrKc_XIIv_gORRmInYzj1jY_ZszYRViqhis3PWLm0T4BC2jWLfv26pNAxbxLtwstaRMZ2Wy_Om7jyBvH80eMLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فورییی
:
🔵
منچستر سیتی پیشنهادی به ارزش 106 میلیون پوند + 15 میلیون پوند برای قطعی کردن قرارداد الیوت اندرسون ارائه داده!!
🔺
با این حال ناتینگهام فارست 140 میلیون پوند بدون پاداش برای اندرسون درخواست کرده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91893" target="_blank">📅 22:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0zvdsTHdGn1DpcdoklMOQVUgzCFdyw24BBH0cMRjOSFSSWhGoVCoRewAivuUNLs4XN_pDX6jnaXhOOfVY4sdUiHXs3qW51y4lS39EoLPFHH3xAaRaz9Hc3CPh1aS5lwNerTzwq5c2Ecz-UdIwlu8ycbeX9-aJcWucexFeXX7rRpCQKrrUscdhBGibl4jJRjdYjB8UFhz-RTb2DBpXAnU9A0ww0hvJZFqPGGCrs4akaZaZL5VKHXhw5EX8YIXzUqo53VH5w-LkaU4tuq8i9v97ljfQWlqpBNO4ToBD1DckBWbWg_W49kd1BW5xO49yiIoCQNvfzosN60Ijvo4EKyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبات و استمرار اگه عکس بود یه همچین چیزی میشد:
❤️‍🔥
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91892" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922b907be6.mp4?token=U4kUxPMUHTrehl0fAI27YmpHiV3sfoPG6ddgnlJpKuVBK4UkBAI-jO0o5iJMPklYg89pE5xM_hBnbAVJ5FNwFafnqUlh1ET8867AYKUZ0Xzmt0FFrKiE6RmLywVnTWzFvPUhsLPhmqGDdk_31FsRNVnokK5aqwARSgFFghDwVOg96r9_wssZWlR77pJNYI1mwUo45aEVhtzFyZRBYdkecI0i3gq_rUdWuPtEoWDeQQaJQyFHpPNe91aAbLvk7T1JuOxdW7qdFEuQnh7z8qMIN_FjaVaUqrO6IgCq6hDJnynY2_7KWrK3fCztPDshREx0dQGSUGmAa67QbUiT7CM3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922b907be6.mp4?token=U4kUxPMUHTrehl0fAI27YmpHiV3sfoPG6ddgnlJpKuVBK4UkBAI-jO0o5iJMPklYg89pE5xM_hBnbAVJ5FNwFafnqUlh1ET8867AYKUZ0Xzmt0FFrKiE6RmLywVnTWzFvPUhsLPhmqGDdk_31FsRNVnokK5aqwARSgFFghDwVOg96r9_wssZWlR77pJNYI1mwUo45aEVhtzFyZRBYdkecI0i3gq_rUdWuPtEoWDeQQaJQyFHpPNe91aAbLvk7T1JuOxdW7qdFEuQnh7z8qMIN_FjaVaUqrO6IgCq6hDJnynY2_7KWrK3fCztPDshREx0dQGSUGmAa67QbUiT7CM3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین رضاییان مدافع راست تیم قلعه‌نویی: ژرمی دوکو؟ نمی شناسم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91891" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
جواد خیابانی پس از 36 سال از صداوسیما خداحافظی کرد و اعلام کرد با بازنشستگی از این سازمان جدا شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91890" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91888">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmxVztm-hIgM-nbxwMnA2BzetzaxNz7kF0T5F8HD-60rJ3LFx_Px0Q71lFBn4aJAQn5HZqhTAJMcoKTq3YsdIhynO43kflO3zFo2OOPvSLEbkrkto4ZdFHZMexCUakxJvxpFDr9UV6gqM23M_oFEcRniK2PmCSCPdsg0amMd7aXZft2DWcfEPmxs8T_C5iTc8b5zQOIQwpgL1OEFR8znHonnYzVMovVQ2vLcDR-wvuEuA6ne_h-WoKMgcZTREcbRQY8XN0SvOqZc95xYm1JAF9WnSwkg5jT6-u7vFhzz78FTi_ApMrie8Knl4ogIVf54v1wwKYFSMyRC28w6rqBMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHps6SJsk3R58DmfNEyO6Ayjl2SOjKYE9nBNAgX6fmCpinWXbWZLGXP1w10N9l5wXzN6NeHNSBxC6EChlGQFnPKRcSNyQQTYsTUYFxlnmCP1YQBCIZAi9TnMkiPApGhsHxNeXEuj5cuqzA8nXt8Cxr92U0NvBFxMRGit8tGGeK7aFF8crgl2RXwZ2ekuGED-i1-sdtaZktAe0cuemhu0j1B89Hp5xqyozVuKeJPS0NW9eXtrUKb_QZlRAk7GTX3fhQRTMPeKFsb2XAxpf0cK5Q12FDg_bYjC9lbMXY73QRTmJ5F6NN5--N5bErRX-xp9eu9u5848ly0qpoC_m4GWkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
فووریییی
بمب افکن B2 در حال حرکت به سمت ایران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91888" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6GsOcQko0QZN2ABR5ay6Yk31gcH1qYZIThg-SGrOy1A5FBC1cWV-tRJFDi6jEyzuq3qRPKQtQrH6LpuGnDVKiB_VTayYoG_kgV7qHTw8PABHhdSsl7g3PCO9XmWhZc6VaFTkpdtNa7AVMCg_nw9rMVnUf6H5VO4EGvEET9QhC65dtsuvZRw_gtvyEmNywRCFT9BtWttK4hx_l_k5hE322zxduRiKaUA9WI6K1apup5IjgTHrHgmrVLDsEPOKaNUwgJn44I3SneKzLZ4cYc6eQE6kgzjlse69b02cvs6xXgLPthU1L_AQCpOd5hXc-gOG7Gp5--YaXGZy4XvzMzYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
سپ‌بلاتر (رئیس سابق فیفا): "هیچ‌کس رسمی‌تر از داور نیست، و اگر کشوری از ورود داور جلوگیری کند، نباید جام جهانی در آن کشور برگزار شود.
"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91887" target="_blank">📅 21:19 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
