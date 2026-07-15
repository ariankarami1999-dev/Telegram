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
<img src="https://cdn5.telesco.pe/file/Ti1O9aqglQnYjMQoZM_BoWTSryUcqq8TSN88pvfwLLu2wLv3XBC4qBZEsHSbVMbR_t6X-oJx9wg2t7hsPg87y4iHgmcqoNi0gKeJQRLDAdGzHL_1WrVTlrMTWsrnnXmz6XtNjm6eSNYjO0UQ8U2CW1wvzMy0cJtHYpidDiLuvq3oL197Zb-Uc2FBW53nU2Tc3zb3NFslsdKz65ThtoJpwxS0Uk7oKKGktdBXard5v8DOdsxk6Dn8kZOR3bM_ewciWjcwTWimJWjgnUgeFyCsUP7WMproGMjfWX_LffX7MLdOR6vnBxyJ7XCKWLoPbp6FPLS2bxWoCMYDsDdYoyYOVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 575K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-100251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇫🇷
ویدیو لو رفته از رختکن تیم‌ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/100251" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlYFBxLoyZQh4He_pSvO_vx3vQeoCgF50FNzJzGr7pTnJEp09zHB1biAoD3XEuTLUz-Xv5bTfHlKAdvWd9dlQds42YBmoKFnvGtWoYKPBoaYHunyyEh-Fl8WJsc5MX8pxka2j4W_eIwZQJttNLCH2HsyWl4rYGfrUoA47LognM9i1VJ801VzzUmhPxYbVLpWxvVktWUFmfMG_fbpE0bpm1svrmEa9eUXTuznWewgyvcqEaFZcWtrVWyu0KjLQ7GTeAJnHZZHJw45o-NXyoNGXuLxf4icvp6oyvoDb0PNIaDmgJanM_pZdGrtKgFnEIw9-pKUIkQ9f63KGDdZwKZDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدین شکل
☠
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/100250" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیکی‌تاکا ناب اسپانیا مقابل ستارگان فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/100249" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdavPxt7205WQGyZyaQu1v8aoJKlr8yoRlQy4lM_CkxYoTK9eZaS3EEiEztMxSKN_dkywpoT6mDo-Q9yktc_7OX-ewgkbhF9d4aoswLKcOLkfOBsFcuiax1EMGiTQvmyxS0xDiH0na8Ei6peM11HIpau-o9NF5CGg5Dyo77TLpL9QmXSezoHez-Veuo9W0nHwS5k-940gI_lrzciVEwYZvDQG-BIKGfyfB5Ag32lwRmCi2bIaPoyVOfpLOKajqcGio3cTs--6BvmbApESdaTzrVPxdMzaYwMhz6EP_dV0L_I8hXBN1irLcfVknzZ31TJGe-IltrFGExNV2CEiNr3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
با صعود به فینال جام‌جهانی، اسپانیا با عبور از فرانسه صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/100248" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LON6AAr71d9ZD7QZMMbmhhfEzjjYReQwDVcXi7LgEwXRzZDdPz_Mhmy8qzcNeiLDuLQpVwORTCqrfmDTN6PsyiPNGTW_O5LKc0kkvCKKQ0JGzzfBjgU9Uu9SS-K94SowxgcE8PHvZBWReZ6wRQ_Qjav7R3Lj_fatkoa32bTh72_VsnRjcMsXV21i3PXDFjHpDSvByurF69206OTDi7kIc8SB7rGypex7MMDaPxNgi6dkwyQNfHGN49b5evIxby6CXqQoo_vi4BBm_N8Buy87MNqErHEyQXh64AEUDgEp1VPwhk9uS9PXMRb9eySOQobFsPfGcsIDrArZR48umRc2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میانگین تعداد گل‌های مورد انتظار برای تیم‌هایی که در جام جهانی 2026 با اسپانیا دیدار کردند:
🇨🇻
•
کیپ ورد (0.20)
🇸🇦
• عربستان سعودی (0.14)
🇺🇾
• اروگوئه (0.20)
🇦🇹
• اتریش (0.32)
🇵🇹
• پرتغال (0.63)
🇧🇪
• بلژیک (0.34)
🇫🇷
• فرانسه (0.31)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/100247" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
کسخل‌بازیای اسپید تو بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/100246" target="_blank">📅 13:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
کیلیان امباپه که دیشب جهت پنالتی اویارزابال رو‌ به درستی نشون گلرشون داد هرچند اینقدر شوت خوبی زد که در نهایت توپ گل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100245" target="_blank">📅 13:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZPO2SE4N3Pv3EWqh0RfoEkGh3Zj_QRFUSoXcZyObydcat95WV5P5ppWTwg3mpGL4IgyPix9eNsyI3Rgr4793UPj91hpDlIzDGglyuiBX0gih6EyRo566jSOVkkOMbZ46EfNgKCZsJMpQt-FfWKQG5rdOVIvGdJzOJ9BOkrLX7fXs3rs9REtApLM4yIEOymzsNacJc2gUt22T2fgxE6o-radTRbhUqPCFvK-06--ZoRy4HVWbKuqOWyxKloSE09912NmkFr59uqhtGLHaj-ZFX6EC0SSX7c6WHjqV2YFOfbvlfLR4aPOaNyvY1hvgU4gsYhtXR8pZEmnlVkb_Xr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌟
امروز، اولین بازی لیونل مسی در مقابل تیم ملی انگلیس خواهد بود.
📊
در لیگ قهرمانان اروپا، مسی 36 بار با تیم‌های انگلیسی بازی کرده است و در 33 گل نقش داشته (27 گل و 6 پاس گل)، که این رکورد، بالاترین تعداد گل‌های زده شده توسط یک بازیکن در برابر تیم‌های یک کشور خاص است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100244" target="_blank">📅 13:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJIyBKTRJCyR8pvMNLpU09yH26qOtRW69r2yNDjTo9TY_BWfdJzsbpalM5B36mmA6zFrtMES2-ffZGrq1rEmBQMAQDRjhh9zWBU1JliCBkwEQDwQ1Dor1o1F4mNRA9SZMmoCre-S0nfKzw7JyG6rf3JvWLb_A3oNUqXDyp4yZsswzYCaZvjdsbOJ3cs5yv-mmxX9MtI8AOTTHRVx-JZTBlhR7_tH0EhepDcBdLnw_28bUVi4IMQEwQgKSs7Eqaf9PrInlD0oqdmQQvFphrw2yC07yzaAf2pgHcs5lsoiZaMmjaSnaQqlqueyn_Js5TVrYN_vCxGvVN-wnEuFa_Fpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
وضعیت جسمانی شزنی تریاکی در شروع تمرینات پیش‌فصل بارسلونا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/100243" target="_blank">📅 13:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
تصاویری از لیونل‌مسی در آخرین تمرین آرژانتین که حسابی خلوت کرده و فکر میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/100242" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⭕️
🔴
#شایعات
؛ باشگاه تراکتور با یاسر‌آسانی به توافق اولیه دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100241" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqHKHjxEhSo_PdgdXauL8zDH7kE7IzNf3zdbhqGLIa8Mpvn2aJ3FPd_xAiSSIkqhWf1t6d_S1pHLzRJKAjdV-0JAHRn94tpbrnqQ6H-QPxiGoG5VPUNrTZSjRnRGeSTz8mB1xmL-I5y37TjZ2MHO5WDroCiiWJdENrnqeW0x5gtd8VOORBeGf9G7EiczgmLX38pfFNZnEbx5ITAadHb9i4g7sNPMLYH7HYwXCeRQwxNPKU1BITs_XPZezp-ygZn0DwY_qFfDJfXaJk1IaP7VMyhAukWuseMVGoGWg_EiTdirZLRNe4v7CoWyi5rVSe4NKAssNsLXKuJfWOAq8Y3FsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flqFFFytp8RgYGp8PcK11xNL68nULIbh_VUQ4ZoIBhZPAPj012m9Y8TkyVUGq7QcA7GrlOc3CZF2De5YnN8o4jilLnoN-0bDxEb7vFqb7s2eqowYizYADsKhqSelRB00PoOmVJLhQ5RsfWx0QVw7h_zOldo4r-DVjxJhGNyOBen-V_Iz5FPdJV1llMpz1-4oECSHtqXpJVlcGBKTFitszDb_8wibqS24vnKOchNx7gzYFUgscKGN1oZKQ8lkuAAs-7Fag1Jn5BCc5L8LAGb7CmAULX4BE7o11QAz1ZxSb2tIN6sBnD1I0bYNQWMBBzhgNsktqvlAgFxTnpEQIxR88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imp5Y6_NlUHcUsoM73Fj45qeMVtZTsDcGdUzgEjsBf7CuUiuonRtHd1VHoxEYRCPh0RS9HECMJ8jn389hTZzFPHuqzgh1EpLCCj7jolVawlNW8_FKVSMjIc2y6gbj53n82yVt8dtaIe8tX6VPgnYZQE41Pz6nl9tXwIMpxtgqMJ2k5AuAyrnPZfAVFF8fgO4fUX7zelXfMKv0bJKBFb23UEEWkgs7kKT6LioiBt408KmR1Nx9R-Ws__Q4PtGWfXS_19TZr6eDb0iE-e1gSYvmts69-seb7xmVi_ba_yHyEFNdVV1WTic9SOP4YLEmMjhB47XUX_1hutesZnQsmwqtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
لامین‌یامال و زیدش بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100238" target="_blank">📅 12:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhrhake-fzdGrrdPykxfUh2Eotclq0IOV_q9XaiCmejQKtqOX5jIYucu5P_PN88zlH90-gzyQJ6wgJg_XRLoQXiz9P0j9ooojiZjtto7AD75UYgK9v5GZgQLCHgTA0wrUgDU88woQ2YqLkkH6M6XSoucGGIkrfEOnUoX09sn7fjfhBliXQSaDiIWPXlRsyQ8rAuv4NTwgOPYG91Gx7aznDnPQGtKo34DAqW2Jq-MPcc80ESXsaw0lyRxbvEsIjrNus9u1_LKzpT8hrcOHU76FQoUZrfAxKR9ormc45FcUUf4cH6TfE2acxXN0aWpq78tgUF7RDvKOKq_V6EQN_-FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هواداران بارسلونا حاضرن چند سال کمتر عمر کنن ولی این قاب رو فینال جام‌جهانی ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100237" target="_blank">📅 12:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
در تاریخ بنویسید؛ جنوب فقط یک جغرافیا نیست، جنوب، نام صبوری این سرزمین است که بی هیاهو، سالهاست ایستاده است …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100236" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100235">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن تیم‌ملی اسپانیا بعد برد دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100235" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100234">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG7MEHThpbuCsSayw_BGiR4gsf90o5WtKPG3REJHI2QR3kjAghM8QvjwVulF30QvO-DZz9GjNozXujcFL99HdUkXYxMiwM7IofY6DyapwnePJ7s8WFa1xqLJV78Lim2_2YF89VW0WrVZDorX78k7tRtIpj9EwppM2ojKWujeDzwjjLtp8QipAsv8puMJyuzjfQczdnZVwKDr7sskPz51ygyamjKjs12mgXuc6Pzn9gdgEtfECwk0mph6NjNSecPOLUnT0DweJnmKq9AITjBINK_-k-A93OMwD42wG8v9l9cjPlyARZ3aipzsdkWKBdwtHsKO4xkZi37mKi28Qbuqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فوووووری
: دیشب حین بازی منزل لامین‌یامال مورد سرقت گرفته که با تلاش نیروهای امنیتی اسپانیا فرد سارق دستگیر شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100234" target="_blank">📅 12:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
شغل جدیدی که یامال در جام‌جهانی پیدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100233" target="_blank">📅 12:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اووووعههه رو برا عمو ها بخونین
💔
😃
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100232" target="_blank">📅 11:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100231">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9efva1-oXbSxBAYJuO_aNZSXEN5D1F7osJd-FWOMcLfiHiLvVturWve140VmCVWZxYXEFtSKIb66s2ESdeu0N992bPwnD6rgNbL6mlpKwqPeJUOOxY28Sa9Y0hOXKdqDrjpWFTFyiHIQB0PTv85u2T5j_UY4nhIe72nrx7-ZurefDJYaQIr5vk7AmAHx6CH93f61PulS6Yhg6htLVQkDIhycXggozgmVBw4A9jCN5sg_t8qAoIJcps0vYHTYYrpqJcmQ9lUK3xy7IsKa12qMfv7ssLERkuJJlKYbU9q1z_HaGaQRuA7ZpcBkHXHIfOFvhSCRlAgnSx15Cbp9KIrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تنها سه‌مدافع در جام‌جهانی بیشتر از دو گل به ثمر رسانده‌اند:
🇮🇷
•
رامين رضاییان
🇨🇴
•
دنيل مونيوز
🇪🇸
•
پدرو بورو
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100231" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100230">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند‌ساعت تا نبرد خونین آرژانتین و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100230" target="_blank">📅 11:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nitR7Lef4EmGLJfrOcpAA3EJSQAQ96MNjusYZz0QJuszqBHKy0NhIE51wT0y6B9-wsKr53ZQGff6flMqresbGKVuwxqPI6bk_dA7TxHkbQmI9dvyg99fdUpD3PCbiikZ9dWO0wR0bwt2MD7ygCTQ007FJ1XBRWdJrfaLgnvos0prde70o-S366rS5H2Pu_YPtTzp79DS4LEwtdpUkop0SvOjTSwOqqZouolaZpnJIisln3v0ubaoTzOPgucLO5yyxaCQWFznMXMBXxepUXzsDNApbA8Rl70PZ5BZPRi5R-6J3M23fc_b05BLUppJYVGZolLFOjL-XcGRiLV0y6kIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات مارک کوکوریا با کارلوس پویول در پایان بازی با فرانسه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100229" target="_blank">📅 11:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری سمی امی‌مارتینز از آشپز‌های آرژانتین که درحال پخت‌غذا در اردوی این کشور هستن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100228" target="_blank">📅 11:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmvUMjv12uQJdMs_G0I6eJSEBNV3StcbRyWnvltpjuVmHdnvveqwh0O-p1KiKfmARV_V1azppzmr8RNHT9-Nv7QszmxHtM4ukBz3HFkDdRQyjloSXvpnWtr5aDl7GhrM4ozG4DcN4OoMjK-ORe6V9bA7d_KO_a-xB-4TR4gz80exGpirUVQIINJjjLcT7kZFmiztH_ZIs-LbFhbSjdiFyABd7WwSje2HDecu8M1Lznk-ekHf-Qz1MF_H2-llN4NLoapXPsxBeN6ceE2dj66eqvrUJyA9u-0jNeCZy7e7hHu7Hbgby3d2VTPtUok0okELmEiF3O7vFDPmGFgOtNMunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متوقف کردن مسی ؟
توماس توخل : حالا یه راهی براش پیدا میکنیم، امیدوارم سرما بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100227" target="_blank">📅 10:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHaIPyuXqmwwXRSEscNaUZeu6vMoZAwdRIVgYzIGELfoudWnGRJnNxDthKFBjzLPD2a8klLXwZM20-kGnbWOozzqtTdZN9BYXohaf9Xy2bwKdVzhacB_REL37lqxVfJie-nQVO_jVHwowXh3q69TC0d-tEhOlejTyzrndTNmAh349A2Ydo-aUjFs76z8ur22KP_B-mQ7vDAt2Exh1Q43864lBYXjL38WJFXHsR0tHM-vBeUTrAMMLA4VKSoauStfeRbN4cerydb7A1CwzOHASjla59sYVvAiiLahgPzZG9RiTerm70Clo1DR36QoO14rDdr875u0bObShiaxINcuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
انتقال مارک آندره تراشتگن از بارسلونا به آژاکس نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100226" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100225">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ملینا بلیک نشون داد هیچ استعدادی تو گزارشگری فوتبال نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100225" target="_blank">📅 10:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100224">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
گرشا رضایی: بهترین صدا برای گزارشگری، جواد خیابانی بوده ، هست و خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100224" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100223">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏆
گوشه‌ای از بهترین سیوهای جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100223" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100222">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f24ohMNDBKLJGXQjWvBTDCW9cwCJoeftSxnraprO6tsOKYJVvTa2AWQXaq3asRDpIYpd5Xe-q1bo78OFC9BFFLNB1FWt5O6MFzBuHC_FcwNiKFcopCiCHxMQmermwPHCXf95FMvF0qa43xfoZbwatxfBQPW86LbctbSph6OrqlmV5QPNjwxvuEJXLO6uSUiGa7THyj4YXaigA_HrmKtwP3Ok3WlRzzgLZdbYtduN8shFYSU03igKmG25wzGV6XLN1H17BdByOR4JOLPvTQEhMS5dXr0etD1yKAdMrgK3HcX374MWyD0w5lTmyt9SSd5K2WJhX9ZEnLunk7Rg5cvsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین رشد فالوور بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100222" target="_blank">📅 09:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100221">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👀
🇦🇷
آرژانتینی‌ها از سنین کودکی به فرزندانشون میفهمونن که لیونل‌مسی کی بوده و چیکار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100221" target="_blank">📅 09:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100220">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در حمله شب گذشته آمریکا بیش از ۱۰ موشک به تیپ ۳۸۸ ارتش در ایرانشهر - سیستان بلوچستان برخورد کرد که گزارش‌های اولیه به ده‌ها کشته در محل انفجار که عمدتاً سربازان وظیفه بودن و دست‌کم دو کشته‌ی دیگر پس از انتقال به بیمارستان حکایت دارند؛ تعداد بسیار زیادی هم مجروح شدن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100220" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100219">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pELxHSWEWLAruGWjGG0YEKaHtoSRNkngNp4WF6OEDKBIKv8X3YxdQLEqsJw0w1hWCEHKQsXbDts7p5s3HonbapP7ocARTdBWaekl5i93o-2P-YUehvOiOi6zn_IT9f-ccg-4nP1TRg6Tn8Y5AtrUhVcdjHYdmOnyIc2xue6c1zNziSByu5ux_INYO6xoZ1KlvvAV5Ag58l2h3lRB6tL00HgntJLXWfVypARs7JIqMJAdR0ZxxEU2cJtGI_XFivB74XKoOaF7x0WB3Lf7pSscaPwkPwzRctJ0NAMRbcEoWC-Qq0Do-I5KgIbDGt_OnBsIesF6MfI1tsN2kWug78RTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی خروس‌ها شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100219" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100218">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRZ4u1fLbmcNFY7YxUc0f8ZpeTj_5lQQbndzJWUNE4IDTAN9Do5cwYOsQNNNbTkXAysamdKZUqdB282n--HD3eo66huqad0V9jC79bFvXs1N--2opHkVmI5kHlv5EhkqEt7kfIggJc6HlhYcvLI9hDqkiC81oPoH1_pkLcBfZQHFzFKuoGya64YPTHq0xCMem3wp2DWDHWF791Qxu3tNYZHiTnZQgzBGz1BJybMA8koRKFR0a3ClofanWg2kxLOeO0Sm9Z8rRA-udlBSisTOB2fFuJWJzQWbTrFB7raUp6-9VlwW64Tuh0T9bcHbEirxnOQrnVB4sOJecBpxH__2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🧠
رودری با 11 بار پیروزی در دوئل‌های خودش در بازی با فرانسه به تنهایی از کل خط هافبک فرانسه (9) بیشتر دوئل موفق داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100218" target="_blank">📅 06:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100217">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
شعار هواداران اسپانیا: امباپه کجاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100217" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100216">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود اسپانیا به فینال جام جهانی 2026!
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100216" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100215">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100215" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100214">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق تماشاگران فرانسوی توسط امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/100214" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100213">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyolGa4CdnKaUy09jEkG-Df6Ot6ektFBHQaQ0_J-fp051XeGLRAJ1ZH2lW9hBPURMZG8MgUDAdYrg2dIhD5Q22HCu_vzRXkEv_GYm1SnSew5bBry6OKJDtUBzWtXpqvLWGmrhH8G55a5uN_2z4GsjUM8zrA_0qmfA4GWesZAcBLgJjBcgX0VMKfHMS_CXlaHpAg3OIQRHswZSWNRvphXlU5eyCPfrTaPg9twXbundcvhj-48aQW5WNBAR_TwTIZplXwvSa0Alef2aTmbXkAUlGz0X7BqcQbr32z3_hmzXlThl1vVLK6zGuqCOYW2vmK_IeF1lzMkqZrBOg57oQkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🏆
‼️
از میزان هوش داور بگیم که بنده‌خدا یادش رفته بود اسپری محو‌شونده خودشو بیاره و وسط بازی داور چهارم رسوند دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100213" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100212">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری ترامپ: اگر ایرانی‌ها به مذاکرات وین نروند، هفته‌آینده تمامی پل‌ها و نیروگاه‌های برق ایران نابود می‌شود
❌
روز دوشنبه‌آتی دقیقا اولین روز هفته پس از پایان جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100212" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/100211" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=OISB8AUlejg_AKlIeG0CflWlF5cKLLQnQWZCJcn2trsb_Iwz9n_qjeBkLfzHhES9dASEqOD7l1yJnFCeeYqM8AiOnQcAoAailbXdedy9OoiqaYxScxG5YYa6lxzHpP1NCxWzAcoXD5ocisHwdZu11N0vJGDFLa3NYf1yzTgqMA9lRR6s8-Lhu_wWdyJUIr4mw_ej90oLPqxzkfOCHVMihXrN_3j5MOXmz6bihuZ7AJPGmraegX4RSbC6zzQVqI7mnruVlUlzaFb8Y3Mg2I01J121T_ePtpoBPEAPjha_krVzVRDiDHyA9xVtOP2o8QhIbfwDH-qtawkhOV2Gc_h4NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=OISB8AUlejg_AKlIeG0CflWlF5cKLLQnQWZCJcn2trsb_Iwz9n_qjeBkLfzHhES9dASEqOD7l1yJnFCeeYqM8AiOnQcAoAailbXdedy9OoiqaYxScxG5YYa6lxzHpP1NCxWzAcoXD5ocisHwdZu11N0vJGDFLa3NYf1yzTgqMA9lRR6s8-Lhu_wWdyJUIr4mw_ej90oLPqxzkfOCHVMihXrN_3j5MOXmz6bihuZ7AJPGmraegX4RSbC6zzQVqI7mnruVlUlzaFb8Y3Mg2I01J121T_ePtpoBPEAPjha_krVzVRDiDHyA9xVtOP2o8QhIbfwDH-qtawkhOV2Gc_h4NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/100210" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100209">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100209" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100208">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=VZEN6RDovN4bJ-02vwZf9XufzIVXmjpvqSkA-HZ6C9FrQ-AzXTpeV1EpTj7KRZXKjmJ1-dGpydTZitlAOQCkKOHBHPlnS_T1HUBjtQgyN2ryXilAzlVtnvkjcDIVjcvxPzIJdrIcV2K433-oO3EWYUMRktxX9T6BgTl-t-qdWvep7Nl-zsBnVI5ACriyizbcXe4xv1icKvZdMSN77OXdEyN68P5dBGEbxnlIJkJhxYxpDm3m9GjVkSpzXJcdxAXM7zv0VqK_ADAytWa3qp_IB9uddqyGYAy_RSQ7G5rg7r2XYWDwqvJfuc_axHReHJALuU1DG4PK2qC6B8YoX-YOtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=VZEN6RDovN4bJ-02vwZf9XufzIVXmjpvqSkA-HZ6C9FrQ-AzXTpeV1EpTj7KRZXKjmJ1-dGpydTZitlAOQCkKOHBHPlnS_T1HUBjtQgyN2ryXilAzlVtnvkjcDIVjcvxPzIJdrIcV2K433-oO3EWYUMRktxX9T6BgTl-t-qdWvep7Nl-zsBnVI5ACriyizbcXe4xv1icKvZdMSN77OXdEyN68P5dBGEbxnlIJkJhxYxpDm3m9GjVkSpzXJcdxAXM7zv0VqK_ADAytWa3qp_IB9uddqyGYAy_RSQ7G5rg7r2XYWDwqvJfuc_axHReHJALuU1DG4PK2qC6B8YoX-YOtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
داداش‌یامال بعد گلی که لامین زد و مردود شد حسابی زد زیر گریه و اشکاش بند نمیومد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100208" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100207">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QbR-lLw860UR3Y6Ddf8T3qXpIf9PcvPqIRgcrEi14L4GpTuQMv1vBNkhFIagpOArDWoCPP9M-dg3jnxLRiEajb0Qb20tfo9x2MZgwC1vGBCtCNH7XnuK4YaBYiWu6yxiDK1FruOmrPvQgNk6zD2uZbzU9QdxBwX5RPhvQVTcUtMMm3wLxgU8awmDRZIYsXwfwHAbaFQ2H7RCud3mJoeFGPA1zItuqUG9k1dzNmsUfXGgAcebIymhauzkuyS2PLhrKozk1OEHK5KddiStWMPx-sxuaN-idyyeOLe055kRDaYhS7zpZON28GIUDO9C0nJbzelu8KjGhHZc7mTK7zOxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پدری، یک سال پیش، پستی با عنوان "19/7/2026" منتشر کرد، که به تاریخ فینال اشاره داشت.
و امروز، پدری به فینال صعود کرد.
🫡
🫡
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100207" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100206">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=PV5k1D7saXfjHsSNCQ2edanaYSFJCQahXO6J9JfUKW0T6W0bnqZAEMVd1okFDAj9Ftb7tTTX8lyJt2CPfFfLUre02KIBqltcw06KTyv_ltEao8tlyBxzu2Of1hTBoHB6hh0EuvqsgYcNrCWSRRIu0tEXoGePHrj-chClwzoIvvc7pUGtVq_staZAlqcrVuzmNtc_wPDtASOAhiLo2CEraypGGn8DbcOOn22v1YQWje-HN0--smFQ9oC8lNGcOsynb4fawcDXmsEjuGkcxpwc18Jl_rZMGQvNg4FEr3cHpCMacsRviVuvT8-8gBMk4pY0deoaWPzxr5-qoPFVcW-OKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=PV5k1D7saXfjHsSNCQ2edanaYSFJCQahXO6J9JfUKW0T6W0bnqZAEMVd1okFDAj9Ftb7tTTX8lyJt2CPfFfLUre02KIBqltcw06KTyv_ltEao8tlyBxzu2Of1hTBoHB6hh0EuvqsgYcNrCWSRRIu0tEXoGePHrj-chClwzoIvvc7pUGtVq_staZAlqcrVuzmNtc_wPDtASOAhiLo2CEraypGGn8DbcOOn22v1YQWje-HN0--smFQ9oC8lNGcOsynb4fawcDXmsEjuGkcxpwc18Jl_rZMGQvNg4FEr3cHpCMacsRviVuvT8-8gBMk4pY0deoaWPzxr5-qoPFVcW-OKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا خوشحال از صعود کشورشون به فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/100206" target="_blank">📅 01:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100205">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یکی جواد خیابانی رو بگیره. بعد بازی رد داده سرود خداحافظی میخونه برا امباپه
😂
😂
😂
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100205" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100204">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVRP8sAzOrbmYx8vKe2bZogzxPXNKQzH4Ex-gP2P0-52VQkj_aaxE_HHDQZNx6HTwMssedLbyupopxERPt9voqf3-wOPymspJUFEKtWR0BwYaSC0M3YqMc1uhdY32U4cqwc4NsPdrEijiYTA5Klc8cw8GTklgH30vezqZzFWmDewXzC46ubCjZE9MHIUxVTnDR6AW3lfqH3e_QagdZcb2eH7YivbqQsEnQxVR7KK8Uxzc7rb78OEHdfvirgoWw6Pa_SCcr-Up-DPTlaCIq0pw-WfJjHI2jH7TmIYJ0nNCazntIcrXuEswTzvREQrSOQ6FUn5KS9bCrGT_LK95Q_9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">25 درصد از شکست‌های دشان به عنوان سرمربی فرانسه در بازی‌های رسمی مقابل اسپانیا بوده است
16 شکست
4 شکست مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100204" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100203">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPypnt7T3CCfgDBRrcZ7rcwwEFt_K2In-80DRyY0Khi80cZ9HEC1nos7eHBu4wki5JtDSuqLKsGiX97WpvSzB-WabT3j73GQKLiYytUkx5zOVz4ZM744PU_dIjCbfk6NRWAA8WJkSy1Np8twi5rqYANqgBPfhmAmMfZj1DDQ0QoVe1cUjjRD61Se9e1iD8PDkaCor-t6YvuAVALZKp_I_30ptiMOdRh0SUa6yC4_SaBn1crcJeKdH4mxPDAmdO5jCQBHgphcV6pLEeca92gBSOrOuQZAFN24sN5SkG3VYZWeI5tE9011jpB1H4n1HTIN9PNtfAthh3OEgnHAJasnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رایان‌چرکی علیه دشان: مشکل داوری؟ قبول ندارم چون اون باعث این نبود که ما گل نزنیم. ما به تاکتیک‌های خودمون و قدرت حریف باختیم نه داور مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100203" target="_blank">📅 01:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100202">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP-fDKxntqfnSbHaqVJmNI_GzHWNvrt-xVDYlniGaf5oUp6q8N_8uvLhfPko5Xyr88fc2Cu3_7uJGR-Uy7U1U8J73AHLqH3HgxqDsC2GwUu6Mcp7w-kW4R0YhZT9UUI21NfOyZeHnT1VG9BByi5bNt1wEy0Fg6YTRw-JitJ8c4U118FxahO-F3kQ_IEGKql4ydt4lze2aEdXadJvNZvpjP9RV4BR1l8u0vcrig5iymMqxrHY55AuszlMIZ-GT7FoSn-r1zHJUkOHD-k0wmxhtt4yvr9MMNcGvvA97m2-jadtdt7D05Vp79mftzD_eGPglFkkha2m9TQMFbV2ANwZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👤
لامین یامال در 12 بازی، به عنوان بازیکن اصلی در مسابقات یورو و جام جهانی شرکت کرد و 12 پیروزی با نرخ 100% کسب کرد.
😮‍💨
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100202" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrEU_6hb3SpYJWja2-UQ5I8CeY9DEBY8ZRroarQ-JQWaG4TT5qt28LnZfx_mQbuVRcRQZbTtKBwKq3xyg5QNYgl3q2ZlASTgj-cQbihkjlUCk4BHvMUjwxv9pYG3wSvVXfRFFA4TunrMJxetdfYSxXHRK4413i5CGAwQlUSWG3OdvXYfvXjysD7AeKDirROu9wEqcT94Mp7rtEsD58XPZFYj7vLuLogduskx7TSvh9x--5UGahKl4fz_u3lwLo3ZE9I912bLPaGx6q23W7dx3fFGZc7AJ4RfCHKQWlOgjTQd8y3UYzSLjg_jRM4OVl-FRAi8VWWBWPisU0kMllKbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
امباپه در تماس با اکسپوزیتو: امشب انتقام سختی در راه است. خواهیم دید چه خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100201" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100200">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ5_t5pUgO-EbzRntJE3-Hm3Am_mang-sL3tpT-rqb9qGAcaHm1-dZ70nl7MMgDgTo4VH5IWhB6VYVxIzN9hfLk9AvUFbw3jL05WMoLRmSW-t2NCIRSXdzbGvJz609qpzOs7m8gYQmQUyOBodl0BVE5BQjubPKmBON3zl1vT-ZTmJor2MrKz_gtTZL8AGZ62umjgt7_07XFWm_nKyGa24RkoyFrPsWnvUBSYR-uct-WJFzskqU586DHe0BV08yeDyLm9y2S-iWM2J3oO9IyCIi1OKU1SQKLtBW3YTvTEtyMzttn4BRt6QIcXXEmkKOpNNhh-1c9EhMt8TeLBCkmP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100200" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100199">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
ولی این صحنه خیلی حیف شد که اسپانیا گل نزد. یکی از بهترین کارای ترکیبی جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100199" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100198">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHO3u6afEhdTluGstwaXDR00Qwoa8dITvv27v_quWEV3yNxojid6OHYOIHpPnUEaW7EsVTgjQ13tODl0rsjr4vkH4HP22z7A4IQkBPnsANZB76tI0lcY5tUrx5T4Vfaj8fX7pFHxYvioPvrALAgwcAZqmbvlc_rE40dEVWoPs5u4A6Iky39BwswT_EUGY_JQ0o34txU5OC9lrKlVCvWtlMfzPwR1GnV2DT7-vgAEGw5T3QVV898JmrKlt09m9podKZrVtC16u-3_A6Dx0pDJ5yD7zJHdX0PZ76j65hTz_UT6viwd3KHujiGwE3-kPueOUGLf0iNGJ_lk3cTysfqvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
رختکن اسپانیا بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100198" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100197">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
❌
🇫🇷
دیدیه‌دشان: یک سوال جدی از اینفانتینو دارم. آیا داور امشب عقل سالم و صلاحیت کامل برای قضاوت در این دیدار مهم داشت؟؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100197" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100196">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکراری ترین صحنه دو سال اخیر تقابل یامال و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100196" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇪🇸
کری‌خوانی دلافوئنته سرمربی اسپانیا: امروز مقابل یکی از بهترین تیم‌های جهان بازی کردیم هرچند حریف مقابل بهترین تیم جهان شکست خورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100195" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100194">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr5VUiAmevuZSgzk1ivcTG3mosbdDTyad9LIwpt7NwCeegYBNyXd3zykWNquUQHhWxGgHnUXbrgshKW3WbqguY9kF8zlzGrxxRexwET9o15yEgIh2MlkiM6dwNVr5kWCCOuTTgerGYUSLyLVAnnbl13nrCu8CxC2wjbVgkjktJSD-gcFGMplK6ihF0E-BHdQ03s6Qwchk0Cdb9KHHCCCUrmuJczt8iRzbFhzWjIFi7veEES83KCX0rWiUFdt7CijEaewVmMINKzyv8sIcsW7oFPzURYUTK-3lNcu9jh8sJ4_Oh8d6I2gdKTwzjt0x1t0VxHgfmP2DotJE-IDahQ_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
فرانسه در یک بازی برابر اسپانیا، کمترین میزان گل‌های مورد انتظار (0.30 xG) را از سال 1966 به بعد ثبت کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100194" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyPnKWAPNM3vIxHpvLpvks0CNqfCxI3AjdoxES7Bn59i4fBv91NO56FOz6hfnDXsRJPMIMQcIXgFfgBpnMR7KVnL2WY4an8llDhopdkW-Q88r_CfvKP81wORTd3uUwWutBuAm3WlGJC8JLMsftDq_lb-Xd5bMO6B9S_uhvgg81oYPJUVK8IjbE1GML8XvaRwDjhtnsf9ielD68BJc7i2wqtOPPhmM--NgHnxqPuOC2VgreHUDeTO8fPWLOrNSW6W8VUeVoAYmO-R26gaJCIEu97rxpD5HrrKXgM0kNtq3K-EfcWNXQN4USY7bymd5X0MWMSwMkqpuU2wdmwl0PdnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
پائو کوبارسی: کیلیان امباپه ترسناک نبود. قبل از بازی هم گفتم که ترسی ندارم. من در لالیگا بارها وی را مهار کردم و برای از آب خوردن آسان تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100192" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BpliGVFJAc0OLOsfsAyXZAEEGA0PNMQdY3Bc-CqwteGKgL163NNHzIHZgPH8_XD-SXnV71rOGKGXpaj2P7C3290GVGZE6nhHT6kDZrNngNGlsomxCqf2PLtBZEnaBNd_Lc92l2MLMcXlA6B1Pnk_h4FJk5HUd8z_iSkg6p-alzXbYbNrW2wfFAaqvk1s9tRQgn5KOnvweEJfOaXZ2znbjZdQxLts0Jmn4ooZ1ywXn2YVq4Yfp5CHlikDflSjBQk0XiRNWxW9KrK6RuU2yzLBPdvaIkH3695PhzckyM57e0fCKHbpQTuW4REDMOsOd4NJjuUyZRSgl2mB-n-iBVcnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oZdqeIMjc6E3bgqxf-P9WN9deYLGKvzhOf2-QnyxTryNxDflwgq25UC9cUcasFWPZSmQKqRjEIEDVSf8sKeGAgr8w2eHbkZm3NQFGZ1iYZi4V_NY5M8SafRwcYwEVYOcRUUk-m6Mu7MCJ_OGRLDcCRG9HIBj9jjCOgMFxPmCFb50SKSytXyJXUWCaINi_WgODasc3bHaNOPhPTgXM_t7_N20iZKIeY6wDRMBh2t7VshJTNJFVTSqYxMC-ScmJyUwFBZdphAseY3BAlJEhBGSOKcvkkUa_bjawTD3GP0oizNo6R2fiE7pYpaffQsL-3Fa9bRfA3aEOhKrMPxdEQP1_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه و این حرفا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCJwSRWLKebqwAZiP2D04GncGRs1RfoWrYQJEZN5_lFaHnXVqT8XuY1B5KhQA3T-wEOb4foWzevCEdXB71TeILbP7kFKo59eOqDJdv-HIeSXWTOdwZnanTWuXjH2OPDUX88U7aLY3YaJ5Dt-1KOemqgXcKKTRMNY93acY7Ix_kkD2uhSVdsy7NNuY_U4ZVmHs_3CWJg39qUlfPu24cE4UL4PbAUBW_r1ojCZqw4wU0QYCWZQFbDP5lctpn1RCRnYtoOC7vkrZKJGR1ycgdCGSUb-EYXKygGQ8xqdPcH-5Mnu6ud21PQYNJZSQluJcLrnfmg296r3Ff1oqiYbW7M6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🫡
🫡
🫡
🫡
🔥
Respect For Olmo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100189" target="_blank">📅 00:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HuPZ2MLU5yv1GckVhp4rtjFcApsiEbgQA6OstD8p6nRstLQi5mrfUcNiThky0xmBsii34igCb9E16EAmRB9QC7umArbBAFd7nbBKBynxDM2PIhp_MpFS8zgH9S3pH7VQe4WPxMA7EQaJFx_lGLyN0pJWFJzvuKsx8YH-bwJpDPtQ0YdUSu7NIdTzyjny4JJ9pFvfT4aY0H-Ik2MYPGjvMLQ00gu_roJcNUpdY9L-M_7cTwklvOXJqsfnsoa6WfolEZXYur0f7n8M5Ism7lE3Abt6RT8zxjQUPwEgOcH4eRP68AC6c5T4OVDH3THHtEoels7yA_Sacl0VpPjm1xBV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو کورتوا امباپه بعدی بلینگهامه برا
شون
زانو بزنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100188" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100187" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lST0Sdio9_LZqkvqmL5hf1WiV1TsMxIKWKcoIytrWv0BNRb4UEXDGJObkamJoiXIGY7IwAtVhIEcejDHxhnciBlDXOHxOmKfUnwmxw2URyMwqYDidYfM-8V4PrYi4cwQ_uUtuVDZ4JxmgYoXsuf-lm2XGglbo141u0tF-nXudbzFpAtJ5ZPQJ6QCCSXD8D0lhZMu2XfG12x3l2eWJ7yJiZsH2hRwwCWVBI6tWMFqt0QqXxdMuL_ty3WKevsVUiX93O3C9hhIZKs3aGXqhqYIGRq0E2YstzqyPpomoyED1Nc4Tt2WULxOndh6eooTxf0IbFmctJ0_jeI6__tjtA7Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100186" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohSfqnqTG-_7t0jyUUTHUE3uXaJULldH6Qq7w1eRRb1kgwPfC5Vb3hzdTGcI6v-CzzBLxnn0GvvIYeFJHsOmsiAKvk4p-X58Gz0LTJuKlB0gXzbg9avZxPSHWJh_DJjg6AQst90UhkHBd1NaRU7G0u2Arh7KeGPbOjDHUxLdRca67YDk7Y6jdon-reAaBlngztPVNCCSb8xSGpSHIccS9pzDItkrDdPsJ4bSZOlGCdXaTityuwm_8v73XaiytYwyik5qSbE8RZ8c8BRFRaK9llRuSqXYGSK3dX4u-tQrP1lkxsghe65bfsXjZEHTztqBLrFykabrVPe__8JswxTP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100185" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy6ZvBsRRyTmjG-mD46yWRbAIvdipz-imBVpx0lPtgQ80Vl2qJnuGLwFj0o7gWL8hdU5KuvKOIn5e8Ma_0XqVFUni-lLxQtJffUoZ_AMRNxfcrry_zBVwCrNzhyxniJUcIxDtYCHHfVM0KcjWGQ0FXgFFmcz0897f_0DYiMEvpx_kXv-FQzckuFefK_232CAWlpTjQUpNIubJZ9_L2c5zsMrm9xap1n_5UhDXUcHea7Fmx9aI-jZa1ZsJttw0aWVbDbiRbeZRgIPcSiQbexD2tJCrjTP8LkXuJLJWf-PyvkKNi7KjQnAA7rqA_ktTBM_bMmwM0PxClZFW5qu2_lVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
نقل‌وانتقالات تابستونی رو رئال‌مادرید با خرید کوکوریاااااا بردددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100184" target="_blank">📅 00:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فک کنم تنها بلنگهام موند و نصف دنیا مهاجر شدن انگلیس 🫩</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100183" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری
؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100182" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100181">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8fU9K5-7HF7TVlMo8u8G48tmcvinwAugiauswKIc8HVibklgPTMYFtIgvGsI4AKqt7PYkpFPIM8dJ-oftfmrhOF2JjE6CYmwyWKetNy4TEYcrcdlIRcbD0fjci_YCyKiV1F2jRcsClhvPBZVMte0tFGUQE4NGSOALIVOiRfZqFGfQHz-3WsWMm1kUELij6uBfL48EJL0686m-kpUuhDtWn5H7rqfZP7atxBwffL2Hd4LtbRvECu-EkE9JK_Urpr0Mk08vz1FNPgDu-t05vyiJXw9jiTYzaJflQI4dpXiFD4Jm8S1Vze383fO4T12mwFeBO8qrl-wuilZ-PwK5Mc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
کیلیان امباپه تا این سن هرگز از جام‌جهانی حذف نشده بود و اینجاست که یامال 19 ساله وارد می‌شود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100181" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mnT1s_yCz4bfF7WKxMJOMzpBwB9pKczSLgHhqc_0vPvxFKUcMp-Oj9bIQTILy2Q6K1Yp5vGb-TBaicRKD6CY3gf4lyqW40JQawQbvBDXtvDOPrj0Yd1E7v_tw4kQ-e6ufxKoSXPeJLUgbG_4faP1KfLn8lsKO8px_5YNwFBaceLrlUFE3og3kmPCjqJDRaX6sab452fUDILE8-WFGOVexDaSb-OB4gj3FlXBJQdZNPY0erwlkpGf1Jy246w2IDtpEfGTmkyISp4qbsemPq7Pl9d4DQHsJEu-IEVDrCTWxNK90WWlMcvJg3EwBo9ceJ9WMWklSWXFgAC12FSh9rPYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل یه مرد کری خوند و مثل یه مرد یه تنه گایید تموم تیم فرانسه رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100180" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNHeCMhFNsqzSkho4M2N6eWMuf2yWuEqMAGU3jFpdtpJutEZIDuNjZH3Wcvo2VtMJdQusMdM6EIeYcPdjVVaQhTB5xrNCcYcJNW_7AwFx_aUKNmNC14qnh9rrnuQ1oFDvMTZq7xSbfc5tmYK3msTLLbM_O7ygfycpaZES-jZEUwQVEDx77oDEvh8hC4vTCNKByHCwtGMaEZ4aFU0U2BIDNta0Xl0Iso0KFvXrGn8cFggiGOjBujz5Dyt771KEvWInuVeTPmiBArG7ExwR9x7lQ6oD1eND2Rl3M17sxfN3GRP3IVcwNh34nNZ_8yay3W2BzogDYOMDhOdoKwKckjz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🔥
🔥
📊
اسپانیا با رکورد ایتالیا برای طولانی‌ترین نوار شکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد.
✔️
۳۷ بازی بدون شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100179" target="_blank">📅 00:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fkgdg4HiGLqyUKvRIZ49cHTnniER3NyKiEZ7ZXvBcQuQ5Uko_2peI2imrfBO6G5hw4AtsbUoJrhJGwsG5hWW-VUVDRLogfgFR66pKk3q1qBq-OzZkysJGJV5-wq0ET2HncjB3q7E_VcaQLqxeEewLLXxHBNbiBZb1yctCkd_XuPrUyHiO_hvqb_Ol2OUZ5BxzbN0LyhWeCXW00KPmqaxImu4SzsabymVh4_tC-JneTpX3Jjk8u8LjOD9i-UB2RihKc3L5NljW7VJ0e3BOpeSOGtgjMo1C4XbKiyuMPNtCg2Lus5MqDAotSnX03IEG-a7LWzU3vnjq2TTEkHLD2NCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
😆
۱۹ سالگی کری میخونه و حریفشو میگااااد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100178" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HslOwP6CI6uWB7hQXDgi8l59BuyQ6yBv2O3Pak-GUm9nCbY06ZDb29PoRZHxpDsHdx8W0QSvwKST8m8sF8DI8n56NCd-finJbSUF8Zgav7bKF3RuwUJYgQqEu3Jt7COEu8pnEo_GhfC6bkMKQN8Mtqlhk-o7f4njZse6b4IRyoR3kFsiMutl-X2fyzF0tPkzWg0XabqGQhhMpHFylAuNSe77NHNErsjNEnZX6Vy-udOjFw6mw27NNt_ng6QTnQHrDB5sr4s6_ExamfWqLkwSKJaEI8qT8GdtZIQ7brgibBupX_gt8Jo24VcKDUmAFXXOiuls30IHEuThj7DeAGftgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پدرو پورو بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100177" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK9dodObcx9Ief4l88LWn6Iwz8pM2ZmjGEO9_zKaSlc5s7GIK9lRUW2U6FKPEo4ixNYrPEcgJvr4-FhQPOBRyB2W5PIIN9PiwZ2XVx4qOp_ecMRjLxbHge6CJd94jAEh3jYKwy9-99hBvDcQ020DiXXnvo3y_lL5MryyngM52EzP85SutfAbGLbC4Z7kR3wYn2gFGduMw5JnhTepyhqrrAa1_Pj1UE3Bka2jJPmSxMBJaV7gZGG34XOHXm1xJvPbWC3DbutH1B2hqsvSbHN_CPMduGa2zr5TgOLPtUS8qxiAU1hLMq3cjfVINGUMM_CLlz7eL6x2zsj4l7lN7OQKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه باااااای بااااااای
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100176" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100175" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfhKWs3k8YiyHCO8SokasSxCa8zRSfOqqUyJeyHb4mefFQU8Psxmp97jK40-MQSXjaSI4gGSbIHIvLrfjepya6L4FRU6-puN1swTt72J9mrNAJMIMBRVmUovADbYNKGu41upfiYwzqNRcFBPT9kpDa0QgTQy9-ESAfDI5H_4ap005Bnz0kWJvBykZhge-mTMbBtUK8Ch08QwgCJcp6wYIjz60n4HJxP-3CRYKQ4G3mK7F3rQJXs3mKpUn2KikLn9Fu1MUTveBXAWhakEXQbFhQu24HcsdBbDwGlm7UOV6uF1_p-atKhXir4I25FXMaoPBG4AtI92p7nJmQi5ii-RnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100174" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب یامال نشون داد ریس کییییه
😎
😎
😎
😎</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100173" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100172" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
عصام الشوالی:
‏به نظر من، توپ طلایی سال 2026 به سه نفر محدود خواهد شد:
‏لامین یامال، هری کین و لیونل مسی.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100171" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امباپه رید تو کاشته</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100170" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زرد واسه امباپه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100169" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKucb_TH5P_B-JnEuNM62mG_ilddBhhsFnoda7pmOFVMZbAcROusA1kgUupgabYVdGutq7QVj0Sz0erLp2HHbDBwUuxSxbcUVx4CCYZxWjieBI0koT7w6W8IgMDRz93UiS3gfeYoQV9PKvH55-AV9e6-DWDsU6CCT1j7HwjNTpSas3na9TNPKfxMrpoGyrcYPyh9ryzfWl9orq6vVX6cu7A9i43pc4IEpRyySc6bXcXwuGquBueAJlrrrXbbzjyFwUP98FfmTd2tIFmn4_oPW-tyMp7L24t25OLKThm7BpIDZxz45d1anomsnI9rIy-mGdYoMJQjw3EtL1XnCEC6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار لحظاتی پیش دوئه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100168" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یورنته هم بجای بائنا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100167" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیکو ویلیامز به جای پورو وارد زمین شد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100166" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سیمون گاییده شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100165" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امباپه به لطف یامال امشب از ژنرال به سرباز وظیفه آشخور تنزل درجه داده</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100164" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چقدر بد استفاده کردن از این فررررصت بازیکنای فرانسه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100163" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100162" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6hyaUr40rS9M_473REJpIZfaYFoAZU43UmKA2O5lzbD9vNPFQFzk4VnTdG74ryz2PGiWfWD62UWy614xW-2cpSc85zY_CCiEJHA1nVTHUJ5V_Z1P_6i623i-qpZYSxV_BCMjc-6nvJntQdayBoGci2xsiIOAfNFiFiQIdtHqhPzXzVZhkeTVsmld2LHODc9fVD3TvV2nWOKSZtBwp4hzTab4IxTZHI3xl0RECIfp_fTMI1uP31GnEKnSaVdNvY8NYVKQDvR7RjulTAvB0WKEDJyqVRHk6erARkXfQdLXaLLYDPBhKpYwp4-28dhtXT8ZJNR7XvgXF4Ke6mpmhbd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق رونالدو وارد زمین شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100161" target="_blank">📅 00:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اولیسه امشب جوری بازی کرد که بایرن‌مونیخ اسمشو بزنه دیوار مهربانی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100160" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اولیسه و دینیه رفتن تئو و چرکی اومدن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100159" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زیدان هم بیاری این بازیو نمیبری اقای دشاااااان
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100158" target="_blank">📅 00:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100157">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لوکاس دینیه نمره ۵.۶ رو تا الان گرفته</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100157" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0pO1JhnklIiMv5TPA2c3DHCdz5EiCCR0WG625918MajoInHaCT58qCuvBNuLXQjXxqF_JWvb15i5qVSzLCqbif2uOhzmbjGBhQBMkyQ_p2PjNwfyV9BdKqsNv4pvQdRlUv0MApfEN9OyFUOzlGXQmOsth6iVbAbQTL1Tf6h9eN3Wgi6XW_t2yKD13DkSzs8DITKjOdzXLPakcMnhM4tMqKyECRlU6T7TZ0v9iQB1qvelgeCYxRZKkKc93ltaxcivgXabGessmNFa7sQ6dnhevGL_XFEtwd5EVIjQOAxX-6c5wb22rrbTohowHiy4WxTTLc4XBW_0Gm1RTrvjF6ibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🥶
🥶
🥶
تو ۱۹ سالگی ترکووووووووووند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100156" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امباپهههه داشت میزدددد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100155" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100154" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرانسه این بازی خروس نبوده مرغ بوده</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100153" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلللل سوم ولی افساید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100152" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=J2Z1NDU7SDAjEVlHi0SgG_QlVBA8O5a4qwkBtHYsKxJGsL6NK9iwjoU5a0LbGy54HZLrzHUHtwqzsSoxcqNv8xT7s1ldHAzyYAaps5wvjq0hOfG1PHyalYSpRL1dq2wufVK4D9sNvS8hvBsg0YSCQSGa3c1-6foGcEMri1edDYq3gMXZ0O8sS6qZNax53HUKhUDmi_kWYjQhsSsetO_8gHtvtpu_abgPj-QczXCNgpyPkmhiNM_eS4imvNkzkADp2cZU4lY4YKuEwk2UMHycB8sdmpbqPbiafy5LCd2BVcSoI-dU036dfutleND7sZQirllMflVI0mJt-sHI1dCmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=J2Z1NDU7SDAjEVlHi0SgG_QlVBA8O5a4qwkBtHYsKxJGsL6NK9iwjoU5a0LbGy54HZLrzHUHtwqzsSoxcqNv8xT7s1ldHAzyYAaps5wvjq0hOfG1PHyalYSpRL1dq2wufVK4D9sNvS8hvBsg0YSCQSGa3c1-6foGcEMri1edDYq3gMXZ0O8sS6qZNax53HUKhUDmi_kWYjQhsSsetO_8gHtvtpu_abgPj-QczXCNgpyPkmhiNM_eS4imvNkzkADp2cZU4lY4YKuEwk2UMHycB8sdmpbqPbiafy5LCd2BVcSoI-dU036dfutleND7sZQirllMflVI0mJt-sHI1dCmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100151" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
خوب این‌ پاراگوئه نیستتتت عزیزاننممممم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100150" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پدرو پوووووورووووو</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100149" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرانسنسنسنسنسنسسهههه نگایدیدیدیدیدیدیدمممممم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100148" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
