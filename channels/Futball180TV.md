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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 593K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 01:10:23</div>
<hr>

<div class="tg-post" id="msg-99634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeaaaab8c.mp4?token=LQAItvdNLowLRZZZqPwUHTz9jhWH19O66108prm6J0m8tErn_Xp9TJvMwreR9MabtWTXcyoDgo-ZT-JdzNbXEt1RBnncgUYxzvHQB_z81pMUZTCNBEke-KBuwel5L99niAT-dxQb-Sa-1jb3WgHx3fhIdycVgx9avity2p_5fOjFiixIFyZ2NmsdxeZMN5HamvUbYBgHBy8wiMlp6PtX3Z76IqcFvx7KEc-UUxiyvBy5VsgjePSG4dA6Q9V2vvZ0P3JBj6bXmNxbv_m9vt4WgUYdI3xNLQKHk5cpzu1PTLr8e5zZ48zJ-I04ObyiUKwBBp7QOS1qHE_H_iB1iR1C4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeaaaab8c.mp4?token=LQAItvdNLowLRZZZqPwUHTz9jhWH19O66108prm6J0m8tErn_Xp9TJvMwreR9MabtWTXcyoDgo-ZT-JdzNbXEt1RBnncgUYxzvHQB_z81pMUZTCNBEke-KBuwel5L99niAT-dxQb-Sa-1jb3WgHx3fhIdycVgx9avity2p_5fOjFiixIFyZ2NmsdxeZMN5HamvUbYBgHBy8wiMlp6PtX3Z76IqcFvx7KEc-UUxiyvBy5VsgjePSG4dA6Q9V2vvZ0P3JBj6bXmNxbv_m9vt4WgUYdI3xNLQKHk5cpzu1PTLr8e5zZ48zJ-I04ObyiUKwBBp7QOS1qHE_H_iB1iR1C4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌اول نروژ به انگلیس توسط شلدروپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/Futball180TV/99634" target="_blank">📅 01:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdaIj_cs-Bd1x1HnL9yZRKZkY-F5LEdiKhprW8WZXxXZwncF8EkP0T9MviF6SD_8AQYDvjkdMxcAHwR0ntT7P7VqglLRQINVvHm6RFiUnaff8efrNDT8Iue85Gs_pO3R5v9xopzHLGK18WfSMSu4RDZiIdbu4dopkvGwiMj51pgjCQbM13y5JwQMpqoakh4K4k4YBq6PWtglyUTdGDTvvVxkkp4cI3Fe_LDVhcp6fA6_QfkykndH62a2YKgCE_HKbCz95tNGDaya7PCUrMBsSVX7ykxa0C4BhLeXh7_QlplA3kNs5EY-kYnUVtGChLVmf3KZ0kPrmzd3yGyHpu29qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالی گل شیلدروپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/Futball180TV/99633" target="_blank">📅 01:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گل تاییده</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/99632" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تاااااایید شد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/99631" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/99630" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چه سوووووپرگلییییی</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/99629" target="_blank">📅 01:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نروووووووژ</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/99628" target="_blank">📅 01:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/99627" target="_blank">📅 01:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاشته خوش جا برای انگلیس</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/99626" target="_blank">📅 01:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاشته خوش جا برای انگلیس</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/99625" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyf_qlRMqx2PahJBmmSol89VloKdT-Yd5UAJF__EkeKHd06nPdoo_MN9Hd0b9yD5n9p96mj7qzaPiFfz0ZAJ4WkpwySj83SBw2QpvE8Ousn-O5Ignpq7mI_rv01WAlxRdQQdRZyglHcfXCJczt80B36xyxfz0mw7NXAYg1OLc35Qy4y0doaNH1DY7-A0jPOLtcLaLfiWjvhWzr7ros3lVbCCbJcZZYGSuYgxrTw0lMQBw12jQrOrbMHecr0Ecyw5j4YR0LGo2uWRyw8TNo_y9gu_P-TuTlao2YepqDVDutcJDO_fxVuIX-VvDiMiuLEZPKsi1kk3pepTUeRl8aODOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/99624" target="_blank">📅 00:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lymkMvBETWPQstQ-0JCyLQ9xVzYSepnSFCakvfIrf4oaiXE0SdWQ8gf8DJdOps-lZfwfXNNTjlr41NEUqfX1KKwirFkOK1aacKlehbJwjNQv0pq3qumGUw-BqVh0tmfP4HN2cFAlY3aiphhu5Uycfw0sOuwgISos_9EMTH5A4uAqUNI1spsa--si96NQsnYr8l79lXdvTfR5-wKYxKZWwqGel3zbpmQr64OqoWWkzIRwrRT6qhLdOt6WAgR4D3cqFA1AiHZmqkwVsHB_LWc6eKlzvuBBRJjuBHlij-dsVHwzbxrzEYxzwnVqmBkxfpnnDNOhaNCNxLIjr1Fo5r09zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی تا اینجا حرف نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/99623" target="_blank">📅 00:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6CCTz0_eFHDNt-dTfcA1SE9cVSitreYVPkMe1aeb56xpEPeaXMCybHBJr15EJ1lPE_36TjOxbgfDMzR2m7xS6Uc5PFA-hMI2VBWLnjuT0j5piX7gUfceUpeqUvNDbAiKoyZoiHxKuQPigcRDOxfOj2r8H9md9cA91r-vtBs-c6qM7wVk83X40217nsLRnoF8nRbFeBomtvC8SvW3OuLjcv5OX8b51pP0PgE1YJ3egmlyZk3PVgDufhX5eyc3CQMlKthfYl8oN3drYptqCVN5TbIb4eZj71lTnzx2sxNGZSkNWgQxrWOqc3_pxFpE0s8c3g-s1Q5lW0WoWIoRIAW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم که هستی بادوم زمینی
🗿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/99622" target="_blank">📅 00:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بازی از الان بوی ۱۲۰ دقیقه رو میده</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/99621" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عجب بازی مزخرفی بوده تا اینجا</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/99620" target="_blank">📅 00:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شرررروع بازی جذاب نروژ و انگلیس
🔥</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/99619" target="_blank">📅 00:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPvQ26MeCUJfYlLxAWqQuGQFEKltwy0QpNWX3Srrjzz0qTAxjHFHQ1aPJjZ8Eoii01bMxe7ANrH-9xQ8ExkuO2I-TJCP2VZNJVd483oM_tL1KxCCWRFOXOs6GN8LApHKxzBLChgd6vElU-Vze77Gn9cS7agjCN_GnRUeJc87WydOUvrn9xjPejPQcsHprU5Slpy7NTmdt-eN9ArzFpLTRilRBIrb-lKGYfURM709x-VnZmW6nxcxYdrng0aXye9RI5pTgfoRV6iyr-JI8V95N9N46ZVQqwo3G296t_cYH0QE8nI2xdG02Wq7D59fqKivLsBrx1T89ncU7Gf0vxIxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYaiaw_7KRH6kvpVIE7LJQbtFZPd2NyGAO8xZ_M7xEiGBvc8MZ1a3gU-mSfTmujHT1ARyf880SmC6V4qcv2BBesCdDhYWHJoZuv8lmBUld-hYCQwCBIHV1SjU3-q8ggVAOnUMl3dd3qa3WCOw4zHlq9WwDr0Q0dTeuEdcRB4jsuMxnJOB1gZ0VSgwjUCBi1Q1RG6hYZ33UfYCFdkCo8BxCA8wieRmmfKxMRNluU4j0SLW4LkB4XPFHxgFWV2fgHKC-YQoHvsXxqFwGvwo3D8cgsbgHbdH0x4gVqQS7_nHm8wyATt09Lht0mqWMrxVikyhUQfRBKHDavGVWriFOj_rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای نروژ و انگلیس تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/99617" target="_blank">📅 00:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48060b8592.mp4?token=XmnqvaVfoTG_8SPk1kFNGgblc7XQtF6jSmIoB_2rZyjO2y-Ddc53JEKyEZR-rZBO_Ku5Xl2wQaDpU7EWet1eb-pEI6Kk1J7g-aIB6r6DGiSQ14BeXT8cPN1oD2ehDuv-DtBoZ__RHuSPFRL0qT8NYGHJS9hsecZCwadVhGKWyV4jKcjQrFcj9lx3u8mDfISu1TPwkc3gi0Wqp2KlNXB3AlWNXQ7-dkwDZN5uGuLXOJ1XE-MVnT95m1ifwjui9nNY_bmxJyJ4PvHsvdBG7M0tZTQ9RxdsTVoUjfvVxP12zXGkEPOAdHV1j8fL83uVDNdFmpm5nyP3dS4SJhD4Wp59TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48060b8592.mp4?token=XmnqvaVfoTG_8SPk1kFNGgblc7XQtF6jSmIoB_2rZyjO2y-Ddc53JEKyEZR-rZBO_Ku5Xl2wQaDpU7EWet1eb-pEI6Kk1J7g-aIB6r6DGiSQ14BeXT8cPN1oD2ehDuv-DtBoZ__RHuSPFRL0qT8NYGHJS9hsecZCwadVhGKWyV4jKcjQrFcj9lx3u8mDfISu1TPwkc3gi0Wqp2KlNXB3AlWNXQ7-dkwDZN5uGuLXOJ1XE-MVnT95m1ifwjui9nNY_bmxJyJ4PvHsvdBG7M0tZTQ9RxdsTVoUjfvVxP12zXGkEPOAdHV1j8fL83uVDNdFmpm5nyP3dS4SJhD4Wp59TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرخان چه به‌به و چه‌چهی میکنی برادر
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/99616" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtldyV4En7496hhFUgJUBwavSJBDolfo43qGUjyJGt2zoqlZFdqwSI3ud8JkgySyHvacU36sKD_0Ja-hpCza25t1YA4v7WXCj9nbQ1363syLfn74T0RPkHshSCVzQ9rGV7TjizMovwL72ldg4uUfmNnOJgxq8DY_DFbEgEGzPOlwVqAw3sNXD0DbiN9vANCCSDiesCgNs29jaCtrHrsE1kp88bhNi7qp1RuZjUcqfmU_8nXfq5TzuY1wfRCixseBxZYtuH2dlCJoFnvO83cdn-1dRDBucKCthvPaKh-N6QIJcps0u43BHVhZSvcsK2Yx_n_V62k6dux3I943AGfSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🥶
رونالدو مهمان ویژه بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99615" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb23tLGursXFv6y2SIVWgymPiPyrFFsq4dLCUIZuOxfEvDr3hT-y6Dhv3-py09ufjhay3gy5l-p7plipgGwrqJFb35zuPMDJwus1fvQ79ea4t6_JAivuaoA829bQ13t2xqI2rZQN4ybF30r8wMlWb6N9IVZbXKRzlXbjFt8P41u5Cdwn9pCkna9wS-MghK790z5NnFEb5dgKJPsMkE0DmYBPsERGS_EsBzBnLAqpytaZwgcG8S1EZzjgmTDvREdcjrV0LV4n1K8sJQ5YWEsk7N8CeQT2TzgKkvekLIXmQsQhnUZpDZoKZoDkL55VaUfFn466chyoJkV7VAbEg7pRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه میاد با لشکرش
🥶
🥶
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99614" target="_blank">📅 23:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzGSqZhHR0CXYdmMhhDN_LvAmy0Nfsi5xVBLoiZvOX55spbIdnTOiE6joyLAYYlbPoXQz0LwWtYigMdyfyZrBEZ2fCDTxBMA1XsqLBN05eE7dVvbNAYblX8iJjUwt4AFHRXjwuqtzel4gu6X0B9IUoSFyrASI94dL8NSzuo1qj8qLJ0VhNnyjqVIM2wIWzljuJ0uaQBlrljj0dw-Vv4aydIBvICZVkPLrP89FWNkg4tdxkQigWhlx8wKia4zHSKlI3RrTAMcJOPRkw6gIm-luGbKmcax-1SJ-A6Nfd3ATmHDvxODfyLwnPwl-izf_a98m2Jo-5UkHPCxO4dML9xMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهت داشته‌باشید
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99613" target="_blank">📅 23:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde4757921.mp4?token=G3GV2IwKSQF30jTFicJhnCKZge9AlzUXv-NqJGQJxlB5vjtubW3f5kqQSE7GpjInYra3MvlzXtulcgdsYqoz1rJyqgDkVQDn3Ffp9FAmpjg82TIOMObdQVXGVwzmz4_AfEsYTRe9t6rPlQhtGiSKzqq_HMW1SJD2j65TxFXtoG4xUd3H-Do6Z15E9-23QkPE33cz4KyAwtfHzOL8fxFo-TPLS4SONRjgz3l5-JzPuJ4hLkRPNsBGUbPsIfc1z_BWBRt2dawOjFh22eJk33qi8OCzOoLF0G2JSJrxEpotV1vnKT9BCKECxHoeTAOje0zrx_fRjJV7By2cI6nL_Ugk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde4757921.mp4?token=G3GV2IwKSQF30jTFicJhnCKZge9AlzUXv-NqJGQJxlB5vjtubW3f5kqQSE7GpjInYra3MvlzXtulcgdsYqoz1rJyqgDkVQDn3Ffp9FAmpjg82TIOMObdQVXGVwzmz4_AfEsYTRe9t6rPlQhtGiSKzqq_HMW1SJD2j65TxFXtoG4xUd3H-Do6Z15E9-23QkPE33cz4KyAwtfHzOL8fxFo-TPLS4SONRjgz3l5-JzPuJ4hLkRPNsBGUbPsIfc1z_BWBRt2dawOjFh22eJk33qi8OCzOoLF0G2JSJrxEpotV1vnKT9BCKECxHoeTAOje0zrx_fRjJV7By2cI6nL_Ugk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🔥
نروژی‌ها فارسی‌زبان در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/99612" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99611">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/99611" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYdZkY8rR_JkYALN0SKFh2utNI1lddD0CKhDVj30BtEW08BPVmS3h0ABcVgYOrpckNSw_V03hEmAYhigwBUbRuUwPWq1n8Ye8af-y-icrHyh5zYFGI0PbV11dsZbYml1sFoMP3DmDKJqmWrm_CwFThpbE8MvYKcnhYt2nxrH10Z_t8rThlJ2iTZsnHu6QQcPey_0XVcjnV3HM1LecfVLe8Og8c_F7FbsMSy6KeHFSXqnn6DTP7yXxYod3FgtgiT0y6yfWmb0r6ggKUEJYoMuCBLSP2M6QYzYz8F0hji_8PHzyjRCatiZFfrG4JA1ZXjYiQA7kaXTbGIVkE3fxFSI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/99610" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99609">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ffabc857.mp4?token=fN8Alv6b8eodCRPzjcfZlyDjEZ0sADgwGQlcJzXmvIFVI9BQUBM3Q6FnQ7Pqtk9pUcY5B9gpxRhXCaG1tKg3ozj5H7GF9AfrUB_U8Z2L4ik4FKQoJRXP1r-DNzB_sHNzrH44W17h7BlcXhh7B2iC7Z7MPOm9axYEM_ZfPweGB5UZKgP2ehtl-h5D2JWL79yn8JEOeIDF6XrphO8vrPI1KeEsNNPMi32cnyyy-W8Aq_9aekIYWTp_H9D5NLQJuZk7VfX0t9QNCqmbHdHLhM36JgsMJgJjTCOuVzQqAeEmi7ekYpbN7SddFyFlBJZqBB5RK8KTW1Zfm3XjyC51BeLtEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ffabc857.mp4?token=fN8Alv6b8eodCRPzjcfZlyDjEZ0sADgwGQlcJzXmvIFVI9BQUBM3Q6FnQ7Pqtk9pUcY5B9gpxRhXCaG1tKg3ozj5H7GF9AfrUB_U8Z2L4ik4FKQoJRXP1r-DNzB_sHNzrH44W17h7BlcXhh7B2iC7Z7MPOm9axYEM_ZfPweGB5UZKgP2ehtl-h5D2JWL79yn8JEOeIDF6XrphO8vrPI1KeEsNNPMi32cnyyy-W8Aq_9aekIYWTp_H9D5NLQJuZk7VfX0t9QNCqmbHdHLhM36JgsMJgJjTCOuVzQqAeEmi7ekYpbN7SddFyFlBJZqBB5RK8KTW1Zfm3XjyC51BeLtEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این ویدیوهای ساخته شده با هوش مصنوعی از بازی امشب نروژ و انگلیس چقدر خفنن، استفاده درست از هوش مصنوعی یعنی این
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99609" target="_blank">📅 23:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRx07MZaX97_GLKArnos4G0CfDR_ztSWV0eWQa6aHxUwu2MiDYlRnWY8giOgtHFBiy_VzYfs87xrAgmaUzNK7QNYQK32SzZ8CFlfy0d_xNvSn7YEfGpIUaZlEIzsF6j77bDwIEuf2CzkwB2w7xTeqZgNWRkHwiQrRF8NFwWBsvmvSeV4XeOnH-2Lz5iXbWFGkGO0RkD3o2yc5Hl-QrAWzZMjmVEnp0knHamGu6t16x4_0UGaPe8YGPE-YyYpZp5Ql3rUJZw2OE_d--kIkAxQEjMVF6o7R6BiJjAd3kWheT9ud8ktBitnYtdsGKPO-_e6qL20ODu3esbWKfPP-dHDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تیم‌ملی اسپانیا در فینال یورو زیر ۱۹ سال با برتری مقابل آلمان قهرمان مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/99608" target="_blank">📅 23:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjMVQOonpcLL3XfWdDYfN77gGV5GOXt8zHsoOPACgJDgHDVl3TflIJoHUGDDdX0aHRFZZfe-a8pbLbte81gXpGA7yRMO34aBxThjzKMYV706m7nlfxOb3r0D9mAiU0ZQ2a0hOIQigHw0P0HnK0zt0UBdjbEpvY6o_kPqKhuEjGUI-Fr8IdeL37Ol7iKy4fesqTfTzlA8nkiRA_y1k34O5H9ayImVjPLIGHeKLic2vFb7Fc-Dl0grpsB2cdoiba42p4yFpAlHklhKIT86kiaNcGk5gmJyplZUjP5vMc8P1XQJ39oTb8Zi8Rcrw4Yml8NXfdBJ0NGxYwonEDTMeGFYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جوردن پیکفورد
با حضورش به عنوان بازیکن اصلی در بازی مقابل نروژ، به بازیکن با بیشترین تعداد بازی در جام جهانی با تیم ملی انگلیس تبدیل خواهد شد و رکورد پیتر شیلتون (18 بازی) را خواهد شکست.
حضور او در جام جهانی:
2018: 7 بازی
2022: 5 بازی
2026: 6 بازی
⏳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99607" target="_blank">📅 23:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1x_o_VXIwtvefMm3as6felqOEPgLW-wFPmkx5WpasWC6ZG5LEmFZqkQUepl82n5CsUEGaRSMaN87BHBQVS2CT2czu9euYA8Gcsua6aKLsdurwLk1tECI9da5fcI5P15BZ_2xTINqAds19CajcYpZeV_T-GF6vgkBnsYmAGJ1v6UijPPCHiareYfUiNM5AVNzYcDqq60NSOqp9S251ENNcFDV6_DVYIjOecw-KapTEDH7Scb_45DfUfoaBjPEMr3SsUGtxboDg7TY036Os2Qg_wldPxGTvvfiyQRvBQZ-HTYMvAW-k_1jfk5g8SIv9elskvlOfbrlexYj7p-e87JrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ترکیب تیم‌ملی نروژ مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99606" target="_blank">📅 22:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiIjq0jYhb9vEHWravVYI3CROqCHpBuDs6Q_upCnr9-Oaz3MTdxytYK695Cxl7DHd8TIomFV7QXJDc44jW6MFAKknzpUaRKmHN-d2WCVTsgsiNQyWKxBOIRs0oh0pTZnnM6A0u2cN0p7f5FwL8iLPY0a0uZkn6E93S4YjFgmHELfl3hBKpaYnzp423HNCEMm34_3Unv2n-7ux_CEDm8jFEHGgQA3sQiZ2jP7sqeMr7F6t9SvJKql_tiF19XEr-eNEF9_tXV_-f5324Ucb3j-kC7Jd8AvFbdlITdW8lCfHxkbBjSH6JdVPoVuzbqHDnCvtfCTxDC6Rfwp-F8bgyys6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه یکی هست که عکسو خراب کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99605" target="_blank">📅 22:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzMr59aHm1NCPhtZ2QxrPeMP4y0JIdQNtoQ60XxHopEtSzzzZkB5_7eau87MEWXypgonbpErLKYZFuVg_6QzAbLjNO-JaWSSSSxKlVxP8gKauO-FSqelvqGBrcR1j22ak9QSBeskce4OqEMOcAQx4GblGWnFl2MciOn9hlUaHG3zSqcSDPDNiZFT-9hz7iFDikz0WqKNdieQi2NAc5KUPakKxcJYtfr7M-Bxx5-YHLn_wpg0aAAe0GehqmVSidluZmer_cJ08S2-LqLmPXEWbYQTCO_0DUQwuRDaeGYh2GjYAVF3LvcQPVe8MGju1V8r4PFPQ88jB25eHqFGupLbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبببببببب انگلیس مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99604" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Km3FKwAamkQlF06825qdvVyW1oxbUPRcYeyjazXcRR4KBkuIRM7wKPVdwLJ1A1ry9YeG3CG7-nfghkgkQe1yTLHKV1-UJyKf_GLzw5CajIE9G_ctDzkcSE_Sh-ck7Fm0JMSK5IYYdRH7hQqx39c2JNlbT3NU6pnuGMXXTswziaRSAWBbUy5ZGQQVcL73n6Mozjnp3AmpUfYGy_gw_hMLn0JP-kcnhZRftEUAxg5Q1zNxXEtLeBhhQSoO0HhI4H0bYmvMWKQg4PQtIS4OO4XVwT8cDURPAF8KNo4LS6AlB25_pJ935oTU67guzm7PuMtR_T2MJtt5AX8VSGPBxA-32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفش کوکه
😂
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99603" target="_blank">📅 22:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c14b876fe.mp4?token=Ny0y5gZHj5LSVeFFo3_VJRcdZBX-hONPkfvRLx4zqPMJa1OF1dFv41WV2uIw_PGaW1gHBeOtkn_rqf3vggz8PNA6A1xJ-kFHJWWmH7XZbSkcXYcHd-mNbEzNnYlAmVRDDDiTi2VusL8MnGdE7w4LGu7D0XJfiim3niHQ0BgeOmqdbHUjukFQTp8733f0-NLz_zk5UmvnvdmM5S5IFo6mJ2IRRojqmylV8BfpbCAWnILuIStabJrqhppt_nqAyPj8A0W8ZmK30oKraUiHdkdBHhx4BCKBv5QYcXtIH23GZvki3eUZIL9PJmw-epc5oy6Q2t6t8VmQhKwr9-uO1rb0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c14b876fe.mp4?token=Ny0y5gZHj5LSVeFFo3_VJRcdZBX-hONPkfvRLx4zqPMJa1OF1dFv41WV2uIw_PGaW1gHBeOtkn_rqf3vggz8PNA6A1xJ-kFHJWWmH7XZbSkcXYcHd-mNbEzNnYlAmVRDDDiTi2VusL8MnGdE7w4LGu7D0XJfiim3niHQ0BgeOmqdbHUjukFQTp8733f0-NLz_zk5UmvnvdmM5S5IFo6mJ2IRRojqmylV8BfpbCAWnILuIStabJrqhppt_nqAyPj8A0W8ZmK30oKraUiHdkdBHhx4BCKBv5QYcXtIH23GZvki3eUZIL9PJmw-epc5oy6Q2t6t8VmQhKwr9-uO1rb0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند حتی تو تمرین به موانع رحم نمیکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99602" target="_blank">📅 22:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxDSUON6Qpr1Krp3Sp8zX0IRsGikx-23SQhYHWDQoivl0yFq5FiRdFt5eiSpeWdi5I9F6XWyA-Ifb2r9cjXVTiG2PlsUJw0AMnBlGc5Q3DpNqE-XntMnsGjVQZzb9-ENhdDdZ1d5caChiRgvT9pbeRewnPgA-LsV31su6xo5JChyUwUXx4pjyz5dsJWxfrqMYNTqQyRfQXRogTHYC0Bjt8uV3zg0-1jFa2_8KDaAaFXN1mqVNHLJMSC-VG3pNbWLmnUpp4IlhhIcqsUp3iwjpMav95nU3CC7ersu7oTUQKGssnyG52aVRFrF5k6Dcyz4hpdoMnWSv1v0L4-UkIpezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فوری:
جیانی اینفانتینو، رئیس فیفا، اعلام کرد که برگزاری جام جهانی با حضور ۶۴ تیم در آینده امکان‌پذیر است و این موضوع پس از پایان این دوره از رقابت‌ها بررسی خواهد شد؛ او تأکید کرد که جام جهانی باید متعلق به تمام جهان باشد، نه فقط اروپا و آمریکای جنوبی، و هر کشوری باید این رؤیا را داشته باشد که روزی در بزرگ‌ترین تورنمنت فوتبال جهان حضور پیدا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99601" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyxPCuhSuQudQgFEkgOxX5pVnUNrrOu9oFn-W9HegA4gB3VdbKLiicCF4qh3qQP0pKrzgcTX6p_XLqrpRS8VZ5jEW-8GxxvzX800s9qujTa0drB4p1ylhppfXFwzQngu0tx7WhjvPhoJMqM7ksH59fnUv-rXKUH2np_LvVguAzt-v9sIgqpriUFq_NtZyOsSPWKRJfAjgIcNHns2t-favEaIQ8P_EsWzHZ-mjsVOqH10fSuqV1KOmKCIx2IdxdbLwCJ5eCWJMqWbmVZX1OAfMV_sIFiR0wn7LEF_wQEHqD9sZkBU9waTwOMrPnOr8JnpNdODLrUcrQVDHAZORVMsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.
HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99600" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vreQ1k918WQcP2G4169jQDGQ06dPEpweh9BzNqV2XmfZ4oxQYMZUZTVIs93l6Aycu1M9Fu0hUNMc7hUuW5-8h2vlK4shErHcWT0OgmQr5wlyRizE_cN6M31EQSYq0_tX62sgQ7HVSfvOQ1SVobhp2da-kkcfVeNBjt8H5jkVALz3A6XfZIwgX_8deAHgCky_4-ci89Ev02glSVCtCX9M8lcoFfIRUJqeSXxp8ZZ7y__L_ihlG_JXkkgIqFezVEY7NTTIM8NXiKZWTvz-857ag5xBPQWoSavMboOMafXCLnbR_L_iZIoY8i9gJCv_1EJ_28YXoaHGk9WrotEzLCAK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس تنها سه بار در مرحله یک چهارم نهایی جام جهانی پیروز شده و 7 بار حذف شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99599" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StG4NVdDDhX3Lw-LiFlWCIQ6dhEjXUuUUaPxgVfTz0o_auMnCLI_YrNAtPpj5VaPPq0eWA3d9OC22N6DJdfgKlnkv3ci69B4MEfvMDwHQTNimnNpRhY6syloUFsMcPUrJL0N8Aos6wAENMwPQBUgQd_hqyJI9ZDPKXb2RTlyYNmp8-OwwE4Gr9RkZN1UKtmkohSRgKqJ_5KV9q4K-_xHs_RblKb-W_8b7HLqmr0JXOoiHgII4sMsHCUq0THEjDrDI08PpGkx49jZ-vSBMMJGS9IWU36jwIUw0EWsSWU1gif9V7VCYIfbgtr0o4VHVzePrBUwY1t-uTAs-3_EKYUAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
اورنشتین
: توخل که آرنولد رو به تیم ملی انگلیس دعوت نکرد الان قراره ازری کونسا رو امشب مقابل نروژ تو پست دفاع راست فیکس کنه
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99598" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b14b56d3.mp4?token=huql2b5kc3RRt1U08sS6iJnwOq5YhlGVaDtnxEn7tM8vTjTBG_6247sDEDm6z7fgJUN5lEjDpUryotmeybrx63KS_sH8-GxCofdu9zE2TK90Vb_iRQZ7Jdd5VzV8hPA6_IYFPbBOvwCWPQDX9k_eX2sx7XIxVfCL70sILMgutnLcIV9McG5AQ-7q_ANRIb_PmGh0kiGoOe68e6jnOfAYl9nGOMaS7kmfxRpg_xKwzXCbWFntbuQ0oRlDyK2ETh8slkE63GlnZhy5_lMuy77W9Rx3cCEaZtcIYgq_boUYvb2XoJPCcqZpgwqYbRg_7N1VXOrW5Zs0fKoxMiCDbOXXnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b14b56d3.mp4?token=huql2b5kc3RRt1U08sS6iJnwOq5YhlGVaDtnxEn7tM8vTjTBG_6247sDEDm6z7fgJUN5lEjDpUryotmeybrx63KS_sH8-GxCofdu9zE2TK90Vb_iRQZ7Jdd5VzV8hPA6_IYFPbBOvwCWPQDX9k_eX2sx7XIxVfCL70sILMgutnLcIV9McG5AQ-7q_ANRIb_PmGh0kiGoOe68e6jnOfAYl9nGOMaS7kmfxRpg_xKwzXCbWFntbuQ0oRlDyK2ETh8slkE63GlnZhy5_lMuy77W9Rx3cCEaZtcIYgq_boUYvb2XoJPCcqZpgwqYbRg_7N1VXOrW5Zs0fKoxMiCDbOXXnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇦🇷
هواداران آرژانتین در بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99597" target="_blank">📅 22:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dswmoyvEJM3pHj790UjvKx0SeagxLk0CAlqABK37j4w7Huc2wA2nZ7WGiXm4Kzou49Lwc-d8iQFx3zd6rkxXZLCLxCsSShyfg1Q95htq2TbUpCGmDZJxlgLd2sPYdZjP47JTS4pKVjK_0Jd_fe10YRSp-BAXFwos_D-sX1-IjVHd36INukxOk-P4cvnLtrorlj_-JqfSlAPpMOzz3XpXMX6FYzN6id83fqUDCZeyJ8IyvO0TGR-YydTySXD7y4y6ppBMHgWSXBW-_yM5CxY140EJYZ3iA60bJe8KlyXAN1627H1_lo10OchjHiNj0pbko6nqS9MHEd9giDgBqnPZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🇦🇷
عکس همیشگی قبل از هر بازی: رئیس‌جمهور آرژانتین با مسی و بادیگارد قبل از بازی با سوئیس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99596" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgOW3jeDYDWjv37TkeMdkqpIAfvU5bP4REZ5hWv1z2ciChPlO7lVoAAdi9nYskaxBLGFy6yiK0Y4t_yD8_fJl22nnUGvDIT7tYneARKBmWeNruU7tfvRd24_vY9ydQp5u5CxU8bcQoCuv-9p_pOYrviJfZ3o0nNplrFE9q6NBMUBFMBUr9jk_9Ugllpr2mKNWNRMXV-Dy9Qvz8fl_2Hr9UqqPLKzM-6C2Q9fZIIdgD7jgNU7pAEbQgUnkwlrmXVrA1LaSG2kZwyVo_G38z756RwrD_RoNCGfuCK1fCwzwdXfA9v761pv6RX_DMwxRq25olEGfeL2MrQf-kaloqwt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99595" target="_blank">📅 21:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😢
پیمان حدادی: نه‌تنها حقوقم را پس نمی‌دهم بلکه پاداش هم می‌خواهم!
وعده پس دادن حقوق در صورت عدم قهرمانی؟ حقوق سه سال من حدود ۳/۵ میلیارد می‌شود/ حقوق ماهیانه من فقط ۲۰۰ میلیون تومان است/ لیگ ادامه پیدا نکرد و هشت بازی دیگر باقی مانده بود/ برای اینکه دوماه تلاش کردم که تیم ششم جدول شانس سهمیه آسیایی داشته باشد، باید پاداش هم بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99594" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇬
استقبال رئیس‌جمهور مصر از اعضای تیم فوتبال این کشور در بدو ورود به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99593" target="_blank">📅 21:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FLSEzwLIZvPYiXHRCp_WOZRujrb43fIJFQBUsbqfZx5mZ57NQXBFcV9owpIISeOEe1lPeyBo2ctXLIcLlQe6hqX_KR_Hhn6QrWScQjceyPWP2ZxG6qrGzwtOIJP-pZP1rTKRVbyj_gC41Fv8Wsbw5U25u-kPbSxHvF0mixuXzO9LpJJUOCNilHEbIRXBtvnf4l4IB2lJYhotCo5zL7w1beKJ5VVCUUYzSqy4nvc4GefcNHcn5--eatZSJVKedaJxWJKmT-e9JPBkGx_hiKiwbW_l_y3qjGJdwujFfaecPMPLkuPWszNbLT2LR33zYnWZO3DOdT7qRnkC5k9k0bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
اسکای اسپورت:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه منچستر یونایتد گزارش‌هایی را که حاکی از لغو قرارداد با ادرسون است را تکذیب کرد و اعلام نمود که همه چیز طبق برنامه پیش می‌رود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99592" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
وقتی عادل فردوسی‌پور هم از ناز و عشوه شکیرا ذوق‌زده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99591" target="_blank">📅 21:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBi4xUzdf-yO9y57d5ASqxZOEsLlZ5Mj5PlU0gdVwYwH2yOKMfnzjm8d-raWpbFqnNwx6dhA7MZ9ZrGw4wWGYD61tR0PNumwE6CwZrKuWl4wndSAjVBh2XC3Fquvrxcd5DRd9de_ssJhY1TB57wu_zYgy4w8H0Wd3RMQRnZf1w1ASu-oI6XOI2wF2mLhgear74SbpAu6TDmJrBAPtINop8sJkM2NwU9XIidNHSErWP8NLmFjq2dWv_7whT7Sc4NNXu1kStoAUzr8NIuu-7dx98RpNgunuWtb7J1aCO1dqtVmji108aDAZTUld2fdTQ3vLgoKFA3JtqrCchNz82LKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژابی آلونسو افکت؛ او فقط مربیگری نمیکنه، رفاقت میکنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99590" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyK7wm743sMHZE1TTKe63nlfh7j0K1ziUL58CRpxY_pP7wUJ37jdAi-q6Bg74qJ0y3PQ1PnTmVf4jFjxJSg9SRdtUQdsljku54V-z7YkFsGVtavhjbGB6uyNT3PEEOFGHQcpK-VEug8KrV88x3Q5ce1H4pj-7bSBvY6Dk964e63j4ip_HWCsgdApCIUxt83RHlNYixncYNTd1l-9qD2wmhun0H1ZkGzTVBFwtOxrf_fePnsC-OlekAf49r-D81nrt07bkdWLdTuXG_sy3_eYHheiEvBl1x77HiC4zIpxiGuOKZzZakJDD3BiMgpE3uUJeBHdnGBBm1d58eNgEbqjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
#فوووووری
؛ کارتل‌های مواد مخدر و اشرار کلمبیا در پیام‌های خصوصی به کامباز بازیکن این کشور بدلیل از دست دادن موقعیت تک به تک در دیدار با سوئیس این بازیکن رو تهدید به قتل کردن و گفتن که در این کشور حاضر نشه وگرنه به قتل میرسه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99589" target="_blank">📅 20:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Kek5HXsHW2DJe0gck9kzy7Cw6aaggVitzxiUjWos3Hr9nihaicdMncj98y9dl3UUMCCluurRweuHVXg1mzLP2w87iPKwVIij3r15MLWagXvseYyoY9Xrh-HNM0GXlPCHQeQ43Oda0FP7B5b1VxhoZruv34th6QOOhd6F3e7EHas8R7fbNO262HAVsVauHNpJMEMPBZTiRc1JebutDN4z3lngKuqHwGCvFIGfUFsHxn9Q342YU1Lp-FOkSytlsc6sqtiQkaLURa9e3be-j8ftxczRAGlJkE8-OywefGgJraQD3v7YO5YyhFRZUBX05wxSqZb8QZ6J5sH482niguiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی همچنان ادامه میده یا به این قاب میپیونده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99588" target="_blank">📅 20:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله مردم به مجریان صداوسیما در مشهد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99587" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLW9vKaPDfKYhilnbu5P8HI4H8okQ4_m-Ikk_uohmt8tfnXtUEIkt1XiJxLg9RjmEvLa-XU3ZDdZRuSLtDQtvjHPD-HVRGErtkUbClIQOmuQ70_iqtSZK5xZtk_dfH0Uj5yY3AgeFt2NJjKzKdFAH70dqM6dSASTaAtnblcEGRNmpTNfXwSrsGCKjwHGGRbmDJNXmLQL_ooqBG29SyJwY7ePwc8r_0w23h4Wz-vC-HBLvv2PvCO1I8bOCdm6Tl37anvEeXw5w4mODIN9iNybpwhaDXIf_doCRjwfzpUPUKU0_2u2Gu7pp90QBAYgXug1L8fqT8-ofBD3B_61z3x9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🗞
رومانو: الکس خیمنز مهاجم بورنموث با عقد قراردادی به فیورنتینا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99586" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با رومابت
✅
بازی های
#جام_جهانی
رو با کمترین ریسک پیشبینی کن
😍
⚽️
انگلیس
-
نروژ
آدرس ثبت نام
👇
✅
https://halvirox9371.bar
ادرس کانال تلگرام
👇
💠
@RomaBet_official</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99585" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb8mL9bcp6k0_pe7Z3I7ywGyIcgzyfUKaaj1a1aOyFFh97aHAlIJ6hksB4Agm_4mD3XO_Ypkd1hjjWGcvir6sVlR0KsTgRLd41hkwAAl9AoluP1igg_gCkdEgCQNgGFL2tdRPa9gRu6hFzrBi5AhIhlHGurE_my9HocCUALtKUF2UlfGCSpyUCr60YrRQTvAOuU4T1AUlTDrcz84cXH92NqKA70cRYKczFLXBx8VnGpHOznfnb-NGBe8YedyDDHsjfxYp3t4Z02ec3e3fDOCz_PySitbdODWBudBH1XMcDZSVhHEKw0KOqUd_wZhRyenPBOThJMRUMSMBvs8KPJxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت 2.500.000.000 تومانی رومابت شوید
✅
#میلیاردی
🚨
همین حالا وارد حساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
👇
G20
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99584" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
نصرت سر آشپز معروف تو حاشیه جام‌جهانی برا یامال نمایش راه انداخته
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99583" target="_blank">📅 20:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO9n0pLA-5er3QsEwMA7CIAOW8JTKCB-_VihKob4GE6LE8BwV6Uiq4c2wwS0cp0sNl447By2p6n69lquAsVQTImoVh4_cn77whw5Xh9wHnU3WPzwzkZ2fFdt2X-ic6K0glzG2YGZAh5EDwHB2gRPoEwY4MZsuLRv9Vu2DGVr_U18LFHpsZLAdwyGIK9XtVbe4xRZNDKq-r6AiKqWoRc_nOBBsFRqIACIVTUIISEsJaIIEGumcscqPnP-0DTgDnAeTcGUqPeTAH2Ne7tk2AHoM3iIVP4H6kjKzmnQnMlbFEQiha-HLQfxZmlo6TtF1HZgw09x3xQbhuCiS0QTK34vdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هادی حبیبی‌نژاد ستاره چادرملو اردکان با رد پیشنهاد سپاهان به تراکتور تبریز پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99582" target="_blank">📅 20:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrq-v8HS8Bw9-kIH7Xyb96BEm6Le0WtCGHGUBQnAaL7axkCUqwOaDcBg9N6_eb_xWFyPn2p_xkl6hQbMpgGgH5dpxJDWnw7qOar4-eJaJLZZ3zPFUXhseWpTxK0BDfsyv02DO88zn9pPLNCRTW-82V2wLy8kkg2MA4zexJVZlg9VUKAmXA0NNWSyhj8VWvSiAlDpdr572JZOMGqsR6AYxTHB-Tk2zCcLCh3y4FgJbnTa26F5kigF7Ytc4pYuLPBI4b3n5rDO7jLQAtNyZclnRxs3VFzrvZjcqr5p42fOlFouzkmfWs46WRoxcuf6V7UzMyCGN73uH5-e-2T8dtxmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری
؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99581" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99580">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5GM2g_ymB-GfMPqH9UotXJ0DuKf4dLOynCXuJBX_GZ9xaOHjt7sLQpbRLeMQKKLBkup7kwiMMbWEmAlqQXMIyL8ObdJrqirGSSJpYawCAdMKEziSRInbN06p1uRVkx6_OokalmbbbgWNi6bnZK8Tkeet5ecRfz0H5ML047ZExIUaTIeir7b7UMdlRNU5sJeh1uWlLe6lQVMv5mzkHWl51wE5OD9f5sz9jRE3GHpk7kLdketGl9XLE6WbMn-4GoELMXMmUzIKcaqrEjKrAn6giMAEo7Zi0_D3duPV_4qZg1q1HFkUK3kN_EHYw6n6QbIRje6usWbgmtNPnUl08afvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99580" target="_blank">📅 20:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99579">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC-0BeRDxQsqVjlyvHSuKqdiemkCK8B87RHvcq5Y1oieEQ4ARDuECrannarVx1DUSbleIkdLRcCl3VcG725Naef1VUWSVNSOyBABksP15J8DPc8wJ4hEIp6LT_BThAheWvuLOPIloKz1E7VHHUU4NEb-77p6qKrZCJQEy93-S0UfzoOOAUU9CPaqjtRdMlMuBGTOrQMhSgQ7rvBjZRULgoGwUHlhKZvftYXorjIRhpUNLqOrDde459qKbcDLifxwWUoFjjFVkXhVi4E6rYB_H_3fYkyO_eYZxo9LNcC65ni-DyoWbnB1B7ZRLPQmDNUSYHi7_ENZ-srnjWRAZwdYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد امید عالیشاه با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99579" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXk4t7JhzNYXbt6ptxZDynOyOUrV2U1IVSkTN5YiONed1dVbRFMWPAfDMsPfP8QvuotIrktCZXIVLz7yZPphmw9nCgDl6G3ZkkZfFv-thJetUKWPMHkTU4RkKT52qR8gQWC67O68Z-qjPiXobeS9AFaUqTEcv9S_0V12XXf0MziVmSbwz6JeCR4cewzg9s7NSsl0hlLsCZ5yMagA-I_dADKKbhdFyv71s4oANhpe30OQ6XZIsWLK1R1K3wYGqOQLrvJbxSunNYma1wugmgA609EdFGfdSPDwTR8D4Fgvpvix7iWxalSo46DMtqzvTdUXdE7_31Nphg3ADSIbVVpXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد میلاد سرلک با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99578" target="_blank">📅 19:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl95RdFuZXLFZ4IT2sFY7whFroz3mxoSTRL_zdfvRn5iQk7nBqjUqQLbKjKy3XRJmCYlm9BZh0qk0ilJ1XAvwN2MRAMBaM4QIG7yr418gjmpimJjp-HCFsE_hyfqDeFb4kRmkPB5_sAqYM3CoDvE8GzdNDhzWZlvA6eNHwC1fXPRvTKjcxFIEAj_EjooUipktJANmXW1Ai5E1gy7Wi98-z6V2ZUZYPcZQUfjwAi7ktOwz-n7mXcq13nYFAzzAOxl0kCIWLnIFZ0ZnRWY0wHcSuwKf0R5nluY0RWqaR2n7W019HdSHKU2kBqLh6jIoZX0IAmcbpe8Og7UCh3SQV-_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99577" target="_blank">📅 19:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf_4qNKKyI9wcdAz30JBTGb6GhD0UaM0EiSAxxbxNjCdlEF0kIZEe1fmdU5-71GO7tEOWa1N6H_AR-e8eZnmUWVQFNje6JptEriqloflhppTYJORmAY_42TwneLu9wuoSnZfWcepbgTzC_xZER_e67KutkVSytqd6a92Dc8jUasn9egqT8VVi18675My49mCgrS-lE4WACPxNDUphWwjmhZ4IhMNgsHVkZ7Rc-cTxCr13LTg_igS4Vdq6Zx_HWgOS1igPTBeL6Q34IU14jP5np9uktXxD3GPK-RUmMPp4WnzKRWw8fi_4mpmwAR4ZhZF9W7Ul0OJ8dPfWvp2zDyjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
تیم‌های ایرانی بدلیل احتمال از سرگیری جنگ از میزبانی در آسیا محروم شدند. عراق، تاجیکستان و قرقیزستان گزینه‌های میزبانی تراکتور و استقلال در آسیا هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99576" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99575" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV9VQfrpxhTswVcMReKsWmeXgbfy_u3xJyXjsrltL9z_sogNAfHt5WUZVcwxWRO1AdEzBOamc6IsbRf2yUH1lk7mi5NDBpjkqRNWO8S8Jge9J_XWI9fBaoKB2uc2zJ4wgmWQXZ4R6OSjLldAghoIwKUpfI73KtriTza-i5_MePtJ94V7Box1kEnrCJG40FFq26hUbgHjvrZtp21TzUuHADgx4dLwD5MrNJ6wZMlYQeWFHpBcx2gy3NeTPADu_vCXQAuKrCZKAbwliBd8uFeiAkhoeCHGCMezOz_aKprY5Cea2qSDsbzX7vUSR05aLSmLrhZGI5EK4UxNkyUZgzZklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور در برنامه ماهواره‌ای دردسرساز شد/ براساس شنیده‌ها برخورد با فیروز کریمی در دستور کار قرار گرفت
🔹
بر اساس اطلاعات رسیده به خبرنگار مهر یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
🔹
قبل از شروع جام جهانی نهادهای مربوط به برخی چهره‌ها تذکرات لازم مبنی بر ممنوعیت قطعی حضور در شبکه‌های ماهواره‌ای را داده بودند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99574" target="_blank">📅 19:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYwEa5OBSvh-nQGnzh9GyeVeDmkCpAbRD5H085VOz2XKSDG6fxLeOpWJ-FttRSYBA8aqF2OgdRruqPT5oWd5fCgc_WMHbjIR3iJ2s-HTrdev_JHNOPbxp7dFeyzH_SxSW9z-ntkotnAC-60TMei2ecq-0Uceuf1N-AtQeL4EAl7gZ2T6l7p6SZ8IpEGVjqKPxSE--7hOs-K0Yo3k5eTvlYg82fh3_hxG8lBD1q29wlX_PDrvsjHiZ-dgWx23OLlGxpwSUlkBkt79XAxMO46gYC2tkyJrUgqjaCB63U68wqdyFAyH29ecIgCyZ-4Eu27XwFitoQg4pKpZyBo_ft5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس هرگز آرژانتین را شکست نداده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99573" target="_blank">📅 19:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E57KrMvk_j29yrWrTQXXrN8HamLMnmL2_ZSIBps3Vd2A_e9MoZCQqx9oIZqh-lYUv8-adyMm_pbQivVM4brwL15mH-_MjzGMJcVAlm63uZS4_x26PDPH4gpotoO4kHCbCxJlgzkv6tAC19_d5d9pKCCkrtN5aO8WkM9zjHG6-7KV3ZOemeyBJuvcJR3yeR9EnX1z4mGiHNaSfNsQ9jdYPTkDysPiuPyaYrc7OcWxPd319yATroz0oRi57JqcBVjy_tWmoFXmKsqppnsdjv0eHIbneyq_QZCUC-hpHO5TujudrFpj8CwlE0E3lQqTmhVgtlrOMx00vdUfe8BKLRg4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کیف 45 هزار دلاری هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99572" target="_blank">📅 18:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk8Ol5nn_ie-iTC1Qp5RteOYLsDa_aWNc2gkF5xa2TjgcF179zAWnxFzo1IP5CQdrWmTnBW_y-MvQCctntfGjGsOoJoy0ti_o4DE-AjfN_igA3E1-QYKSFXByLIUaqt0a4jdOY3lmo2ePBhvFJs-_PR4DmBVkLrCvyW2UyYBtAHU-i1G4S_ixosa8HT0tEp1AtpKjMsWRDR8UNl_GAS5zrR_bojSUvjjtTFmFIFs4MZjNQXFbXMoKFgnFv4cz-a5dYr4o8uVAnMoyzOnoZ4YZGwVHGahvxg6DD3VhCKcjWfIC1yF7crmaD_IXvQX90keM-VuhiIEway_Mi26NDhn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
میزان شرط ها روی تیم ملی فرانسه بشدت افزایش پیدا کرده و با اختلاف شانس اول قهرمانی محسوب میشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99571" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVJKcWqEtekPYtpnp0HYgGMK5KzRVXqLvgNUC51N2XSX9K5OLq3d_yawF8Vlc4Z9jVcokYYbIQWDxEtJmiLPLu28Dlz4zuj6eCiKyjU82xtJIyo1a0B4pRjmkEBFwfmPYg155cKuc-k8qTp6GGCZaWlIjslvBtuDieqDYdvGsbZYzuzxDG4H2za7jDwPTlhwsCnGGxuqe94a7IqCCAnZ0g9n847MDU3ORYac5lAuJELaE3d8XK7t13lIp6JcJ7vl9G1b7eVlFsW5WMDDNsRXqBEil26jTETA-R4A2HhmrPVA2d5mDeW9Btp8clvZbKmKaz8ThAzu1Kv1VsanPsvXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار نشان‌دهنده میزان مشارکت هری کین کاپیتان تیم ملی انگلیس در ایجاد موقعیت‌های گلزنی و حرکاتش در زمین در طول مسابقات این تیم در این رقابت‌ها است.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99570" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6j7Z3412I99Vd2p1YVILP1hdjJCxmjiYEdtIrSSRuIQrOQEWsMLgLKOh39I_UxtDSAMF8RDWIeYfhB-BEzVXsGSmYyVxpCV6DeE5VSwUDltuiQwIxop8YtZpHhzHSeCB2Ox0oTyEQkVVCmJOo-WWkycByBgvkxOjinJcPkFrFTmvQuAYx1dIlji3pFj5zUu19IXrBJNf1uG7RB4ZXj42wZB6KcttVFR5xpKUC5I9tN9jt5GUddJVsJdwtMe5QD5Zaoc2gpl-UBV5NEsgQqgaMhBrqv99-mnRejnkLfS3fe3TOKuaSVP37vvfI3w6VSfg7P9YXLhVqdLQaBx6Svuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🗣
دومینیک سوبوسلای:
- من مطمئنم که ما توانایی رقابت را داریم و امیدوارم که با مربی جدید، آندونی ایراولا، در مسیر درستی قرار بگیریم.
🔥
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99569" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI6c92UocXeGa6xNIhj0IRX9AbgUvL776IVXz-iqtolg19gCOzMfJy5aplJT0A9n8vAmJxs52XTw3klhGwfCjO3Y9f8qTnNCUPbchC1HWDuK3M2CkikBY36n3M3eKY3-y2PHprYJ5rQ2i_dcHG6Vx55nljHCDiy_97cZPDOuc8wYqySuGQtl24BuDoXJ1mGpGLHVVPJI3o2DqLtNwnK1S_2rIV5vz3_XTvYONdPF7WFpyN9ZAyEgs7GQVYbruIH0vSxq5XsxljZljlZWBbOS9IGzbojNqTcZPPzwLX6UnOR6fQtDIu9LtnyE3JR9RaKKe37MG1jswM7XqI_U3lU-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار لیونل مسی در مقابل تیم‌های اروپایی در مسابقات جام جهانی، در طول تمامی حضورهایش:
• [18] بازی.
• [9] گل.
• [6] پاس گل.
• [15] مشارکت (گل یا پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99568" target="_blank">📅 17:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
محتوای خوابایی که میبینیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99567" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO8foidMWrGdYoEK2dGDFGOCqD5n5EB0Qnp2XDC6HjVhuh3bvg_urIIILiCLNEsTWRhVcCYuI0TIsHv4GVS3zGV0Pjup_kqbxwVaEPqDnly6IWeyDNBZei3DqECcBsy8WYiTAAvDtYFYpui3p5cU4snoVzTmNuLaB-c9Lp_l9PWUiVpVXDKzZyK32rJbmQQLwG3TFGVJDOBz4wgosBEDalhgiuriIMz2qaKE8pmn_npjP6DxribxlksrV_2pcsknqc5ujKrg6WN-hITOyRt9zpq-VWePl8DxzU2eRzizO80Y7-Jfh4tJFrIq5w7b5EIYKlPlZvxb7xSJBV7_-KcnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⌛
| مقایسه باورنکردنی کریر رونالدو نازاریو و امباپه:
🔺
امباپه:
🔵
590 بازی
🔵
440 گل
🔵
183 پاس گل
🔻
رونالدو نازاریو:
🔴
598 بازی
🔴
392 گل
🔴
115 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99566" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAWn61dZTkOT1QxIaiOdbj82GR5Ld-EXxaTxU437Mco6-kPWi4m5mDE7JQOAaUJZCJKsooxbPtepcIypklv8DPMuWOeu5UOFemTQXNIFruMmPkV2dxnSJV-KuzXEWb7z0rtFW7WZ8K5ubOXRg-J9LbJXDL7uAeIVOvVp27fgZFhoRnGeU0hf7GM3R6Sa4Z_hdqjOBzMhqdOo6tjIMBIDfaattjPWyqUMKyBIALV92QEkBMnOchgLcBCZzIdV7fYSA8Ueh_kAXKT7pj2ZLSzUXWLrr-kuBurZzQGKkJ4D9O9DQ2DrmAY8mFHhV1iD4ak9JVoM1WZ5W8U2nAHfxwK6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو وقتی میبینه تو تیم حریف یه اسطوره محبوب حضور داره که در صورت باخت باید از فوتبال خداحافظی کنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99565" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRLneVlh8hNiwoX6vCWyaJVi0u91RHvd08orl5zAcYKWl6VkZFzoZaf0Y4XZ8K1_w-JBFWzRxXvz6AdInngSOwFrkexmo4Z9qUfDgyJOrjDgD2v9DkRo3Dc2DKzZaNb6SIPc13v2yutnw3UE6kONKbEkJueLVJUSfofbi7pCSuQPQ68wnpPl_FATVLTi_eu592tWth82iWxoocRYWRyaex40btauJ_7TTEnlFU79ua8H03d-6Ovn9qZDEVoPEo1-knhiX7FM5ggNkDmnCen4gCt6lgtSWt7RIZwRvqrOD-cYb-Vh0DxHgEP9O9mtdpS3go2PolTudubg_W2X1su-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
🇿🇦
جیدن آدامز در ۲۵ سالگی درگذشت
جیدن آدامز، هافبک ۲۵ ساله تیم ملی آفریقای جنوبی و باشگاه ماملودی سان‌داونز، تنها چند هفته پس از حضور در جام جهانی ۲۰۲۶، درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99564" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کمپینی که مصریا برای سوزوندن پیراهن مسی راه انداختن؛ اینا بهتره یه شاخه گل بگیرن با خودشون آشتی کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99563" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
انتقاد تند رضا جاودانی از صحبت‌های محمد حسین میثاقی: حرفه‌هایش به فاجعه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99562" target="_blank">📅 16:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛂
سیستم VAR در مسابقات محلات شمال کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99561" target="_blank">📅 16:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTZsxPXlrFNaUkbRo-MOmFhaNQ7bW9KzlZNTfDYR6t8O0r3Kh1jahLKWa7WOJBcFCUPYd3qOormvr985loRTrD6KtClwkazWhxQlbBM9-EOkEYXlbL0CGnGxxSaK41LVFBful1pnhV8sePLg9gyFx1htNtqxTTT2u2x62UdtrzFXmtU3535X24O-j-1CFiqhEIM5pcSKgq29GfzQajV9d_hPzi7I2QCqCrK6qTcQyOCl0s8tEOKrRla7kDF-UMsWs4yLVe_UQVys8Yv0qDm5zqLsb4xp-MHxOpuplXqrHzqqzUF46P7M4OOZTd2T2i-Mwkg2RETzkyF6sXXvk7zfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ ترجیح مردم کشور های مختلف در بازی امشب :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99560" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرینو کلا آخرین رقص و آخرین شانس و این چیزا حالیش نیستا.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99559" target="_blank">📅 16:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Aaw9qOI5VgaPqZOlPyLfS5FW3HCu2wS27EKdm9SdcPy8ePwogAtWbJKunrZRxvKtMJEjCu6yo3AqbQfT2FsuHMpEZQ16q0KPFwFtu_Uph0k5NoAgE-j8Vw7t1KureJAbchdScLOJNKYNxyPpjzOcp9TwyjxbCse2aV1cFZlIdBDy5EhA20Cp4sDFQ23wgBrKAA2MhWpAUcI5seEARBDBCMC8pJBS_OjY8-YZ4nSxIXPqADwWrH7i8yeQGhd574qJ1QvuwzgRgC1xLspJN3-iP_ki-8QJ704QUBelzCs6edyHaRDRGrbFbIEpBT80XlFzHaSYPhKu_hFOQWr40x3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
سن خط‌حمله فرانسه در دو جام‌جهانی آینده جوری هست که به راحتی میتونن کنار هم بازی کنند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99558" target="_blank">📅 15:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=Hwxgi9ZHJnoi_cgOfsgAPzE8N4S5u6BKPPFYUVpd3n8gT4DqHqYduZFOhc_PbdMiADOPjnT37ocaTJSu1vRujPalIn4s_jlYHKLgHulx2bMpasbIsu9GCX0GLEO701hhAcTlDMvvdsCl8ybMZ3Ka_g-91RpfoioE0yfOeoegpWXwwjhrttwbEeADsoz4rHQDFh2_o4O1jFLVn_3hFHcFyBMDeeoJ55cWsQKoBydNwWoD4JN_tVDIMNDCafiEV-qPzIEYyF715w-fchRRvQ_b9kkzYzHVMFiHXVIDDf2mIxFBLDOiFDVosTm0fBtGS7VTuEEqdBrmcUsb2LnN8Sd1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=Hwxgi9ZHJnoi_cgOfsgAPzE8N4S5u6BKPPFYUVpd3n8gT4DqHqYduZFOhc_PbdMiADOPjnT37ocaTJSu1vRujPalIn4s_jlYHKLgHulx2bMpasbIsu9GCX0GLEO701hhAcTlDMvvdsCl8ybMZ3Ka_g-91RpfoioE0yfOeoegpWXwwjhrttwbEeADsoz4rHQDFh2_o4O1jFLVn_3hFHcFyBMDeeoJ55cWsQKoBydNwWoD4JN_tVDIMNDCafiEV-qPzIEYyF715w-fchRRvQ_b9kkzYzHVMFiHXVIDDf2mIxFBLDOiFDVosTm0fBtGS7VTuEEqdBrmcUsb2LnN8Sd1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرگزاری مهر خبر داده که برای فیروز کریمی به دلیل حضور در شبکه ماهواره ای جم توسط نهادهای امنیتی پرونده قضایی تشکیل شده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99557" target="_blank">📅 15:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=WZHgvab3QQkgq-uIv206N56vbpW8n7pc-7ZQqJFXDdWERZYURuS7id16zEee568t0plVL742JNMkQy2Koc9XjvGcqK3lIYJDStW-2LhEzsOpLchbp22FSt20wW2TwN44bnUzgSo_DPg4UaWI1p6-8ATR5TELEnuIBxYZnjmJN_sZM5ZBTEzaBZIXPwi8v9Vj8xRh5ewfVn7o9MMfIxsiUE6zasvkV709tW52j94cE-UJqXJaknnx-OAwttM9HMTiKCvWYEdYGFvFmWOEOYujXdnaHgLA9ONswxLqNM9euurvxdDgIQWdMqZdNSkNGZPGFytHm7yYi5hG-hG4QdVXpxxsVgoidozcvcUmOztnA7bLRCknF_fIC-2uagXF9yJsDES2VfBlSD5GB-2GW4KZhdG6ZtI0j5Nuh6pNNUJ4uw1dlFMBIunPFJgp_atVk-kjh5QjZXboxYLQ6sPnXsNzRvyW8nd7LVtzG6V4NwMV2OZMr69gIJhhxFRd0siNM0iCUcpmEC4Deqnx9l0RI8nZy1pRpbDs6ByGPFeOKBEJktRglJ31H8BCziCErsmss01_ULPCbFWOub1cOqZIxwpwSVyBXJD7y7URhlu9JaKV-AG5m4sIPTEMRRoDXcPd-zv10NgCUd9hd1nbWz6mziieAfSZY4bBGw8z84P6IGvyXLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=WZHgvab3QQkgq-uIv206N56vbpW8n7pc-7ZQqJFXDdWERZYURuS7id16zEee568t0plVL742JNMkQy2Koc9XjvGcqK3lIYJDStW-2LhEzsOpLchbp22FSt20wW2TwN44bnUzgSo_DPg4UaWI1p6-8ATR5TELEnuIBxYZnjmJN_sZM5ZBTEzaBZIXPwi8v9Vj8xRh5ewfVn7o9MMfIxsiUE6zasvkV709tW52j94cE-UJqXJaknnx-OAwttM9HMTiKCvWYEdYGFvFmWOEOYujXdnaHgLA9ONswxLqNM9euurvxdDgIQWdMqZdNSkNGZPGFytHm7yYi5hG-hG4QdVXpxxsVgoidozcvcUmOztnA7bLRCknF_fIC-2uagXF9yJsDES2VfBlSD5GB-2GW4KZhdG6ZtI0j5Nuh6pNNUJ4uw1dlFMBIunPFJgp_atVk-kjh5QjZXboxYLQ6sPnXsNzRvyW8nd7LVtzG6V4NwMV2OZMr69gIJhhxFRd0siNM0iCUcpmEC4Deqnx9l0RI8nZy1pRpbDs6ByGPFeOKBEJktRglJ31H8BCziCErsmss01_ULPCbFWOub1cOqZIxwpwSVyBXJD7y7URhlu9JaKV-AG5m4sIPTEMRRoDXcPd-zv10NgCUd9hd1nbWz6mziieAfSZY4bBGw8z84P6IGvyXLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
لحظاتی با داداش بامزه لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99556" target="_blank">📅 15:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a53021254.mp4?token=lysVnmceQeCtzj8iPOyIv8_VZrdcWi1Bl7yBuiqhp1tiKOiLl8-MmBV6HfxlU8zQDHv9yhsDyQ7hX0fYUm6r6MDDxzDZ5_EBCrMGuUTGXIF8-hjA2xuT7qlYiJpli0RHbX_pMrV4CvaSjurAwrTP4AxZqIa_LbY859fJPZ1NY-kFqzfMRC1zYogLt5B9BiSrpCYUPu3fkyXV3f8lhTuuk8GuhYzYkBzsCzRBwsKhFh-GMZsEeptF4y5a04W6j-YR8ef6Op7CkQ8RiaIObzomrFM6522nBbtF1IY-k6hCBKa6VSl2PXLFOqXKC971BO7BBbzB2RseyRSUDBTa2Ivwb4U2-cfSa96LFkgsw_rqEn4158AugmsxCtfharpTfwGgcZzcMYVGUvf0NhGKlBBpq4OYFbo4DT7T5Ajoi4KqsxCm0JWWEzE9Z2p1KwP1sgL6EAu3vS0aneYQLTHluMwEHbrMu5h97-UMYhtBkUePRK1Veweu_RaAkUbi2ePTIbsqj8HDOhLrr-5KrmMC4OlkDU3gPNHHaAOJ4DZ6_BxIcWl9SA6gM2GZe_suhNt0KuTDTeY7ae70UV1AkmKO4WbJGkSYlxMZVHKJiPp6nhFjO4sIR7-UC4lbL-gJ-y0JcrYbl4LUSQndo_toxey8CSp3ldbBpfWuJcEszjmE8WQxPr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a53021254.mp4?token=lysVnmceQeCtzj8iPOyIv8_VZrdcWi1Bl7yBuiqhp1tiKOiLl8-MmBV6HfxlU8zQDHv9yhsDyQ7hX0fYUm6r6MDDxzDZ5_EBCrMGuUTGXIF8-hjA2xuT7qlYiJpli0RHbX_pMrV4CvaSjurAwrTP4AxZqIa_LbY859fJPZ1NY-kFqzfMRC1zYogLt5B9BiSrpCYUPu3fkyXV3f8lhTuuk8GuhYzYkBzsCzRBwsKhFh-GMZsEeptF4y5a04W6j-YR8ef6Op7CkQ8RiaIObzomrFM6522nBbtF1IY-k6hCBKa6VSl2PXLFOqXKC971BO7BBbzB2RseyRSUDBTa2Ivwb4U2-cfSa96LFkgsw_rqEn4158AugmsxCtfharpTfwGgcZzcMYVGUvf0NhGKlBBpq4OYFbo4DT7T5Ajoi4KqsxCm0JWWEzE9Z2p1KwP1sgL6EAu3vS0aneYQLTHluMwEHbrMu5h97-UMYhtBkUePRK1Veweu_RaAkUbi2ePTIbsqj8HDOhLrr-5KrmMC4OlkDU3gPNHHaAOJ4DZ6_BxIcWl9SA6gM2GZe_suhNt0KuTDTeY7ae70UV1AkmKO4WbJGkSYlxMZVHKJiPp6nhFjO4sIR7-UC4lbL-gJ-y0JcrYbl4LUSQndo_toxey8CSp3ldbBpfWuJcEszjmE8WQxPr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: هوادار فوتبال و شور و حال آن را کاملاً درک می‌کنم / حرف من درباره فردوسی پور این بود که ماه نحوه شادی کردن را بلد نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99555" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T77VbeTUWPgo_vrkTQOCV3VGKB0uY19EQgo4Tfnj106jrdvgGrYyVS6WxVcEePfq6FGyVs8Yo5yqAkQsyPZoiPDpJaNvOf59m_sfkynEQ9lwJih5ocTeSH0MNBp2La8bKzZmBN5eY_wr2_5fUlhdRai16bbH-Q_WIoqPQK07nX6qOhq8tYS9k77xv1MXOKxHXLw0bePlGKMtnFLz6spho5_9eH6ixBlfAO-eBFMSPSanjGUvR4KodSl4Gw2Gg0yI1XyXitTyDbRBf-PbRKj1p3ZYo8UMWPWxprh7jdKEPkWMevZgfR9zzxVutZNnmqd6NwVB99nnzEhjU7ZGxeb9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیبو کورتوا:
برنده بازی اسپانیا-فرانسه بدون هیچ شکی قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99554" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhII600uy8IGPfKEJXAuP1-4FUVKjiQ1poQy7k0b9Xo41yC4XPVAO8ajVjrQlOTCxkLudNxkZ0HGyDezUwtXs2GUKF6yjxbiKJNXscR20wDcjMXCnSKl80xwiNzFfhoLkZxYftmoCJT7U6U0XiUbIVwMGfU0aA3nTngvTIsUdj6CWEfyYPLMdGR79R6BHMCVoGnhJwL0F6CV6gPyqE0U9UxTraaDnFAvOJxoEt-OaadwYWktdkY4Tvm3-Pssfi-jkWOCLJa3zGKMVSuBuyPaSULY-Ju4vgX1h3GXEB4AhA0DDBoJDVsOny_NNpxL5JQhlM-iYsSb7fFmvsZAQxU5PPs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhII600uy8IGPfKEJXAuP1-4FUVKjiQ1poQy7k0b9Xo41yC4XPVAO8ajVjrQlOTCxkLudNxkZ0HGyDezUwtXs2GUKF6yjxbiKJNXscR20wDcjMXCnSKl80xwiNzFfhoLkZxYftmoCJT7U6U0XiUbIVwMGfU0aA3nTngvTIsUdj6CWEfyYPLMdGR79R6BHMCVoGnhJwL0F6CV6gPyqE0U9UxTraaDnFAvOJxoEt-OaadwYWktdkY4Tvm3-Pssfi-jkWOCLJa3zGKMVSuBuyPaSULY-Ju4vgX1h3GXEB4AhA0DDBoJDVsOny_NNpxL5JQhlM-iYsSb7fFmvsZAQxU5PPs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
افشاگری رضا جاودانی مجری سابق مردان آهنین از پشت‌پرده این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99553" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_DBwRGg9bnrsnyW8TISx08stAHUi9EH9c55Xa9uTSlVd0EeeoE-tQ9lrR49w7Ifr0QaqP77MuHfg2I-7iN-Ps5Ulu_xBOb7GpyIHily5OH2oG4aOL7_0aCeoU6CznvWHdSnjeTyHQkQ-5NG2tsO-I55e8oaQ4QCCO2JB08zALtcYKF_IC4e1Sg6TfGeDtr1nIptOOJNlGYseU3ANrE9toemFKGZ0OSvFhUwtkXQ5T1lq-YyiVtYWpDy8DGSglKdwMgYnnBwwptnrWPASVnIt54jg4nueMALvNRJBQ8LXPSXb5layOcba8Gh8BMQxQtYkoFhZfIJRueeuBqe-GUx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇳
اسپید:
هند به کمک نیاز داره! اگه این هندی‌ها واقعا دوست دارن تو جام جهانی 2030 حاضر باشن فقط یک راه حل داره اونم اینکه من رو جذب کنن تا واسشون بازی کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99552" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axjXy5JBD-arLaoQygte1mFkmG7GmIEJYqlhzctC2jyx6byZaLMmakqTJklrqNyxx8QKObbS4jCyTyFGiUbus57BFvQB7PI8E2EvVNRr9b0c84OWJqFtloRr30sFuzGhhc3SmVsZeJr5xwCjwmd4kYAk6iO46u4dIbozQtx8r55Vvl6VdjPWR0OPxh1EdLxlSjdlqXVn5uPnzR_fsNm-uz_lw4pny3bOYhCv-LjY3tf-A8TbR1mauMEnW2Fog8KGHqm0bLvviC0Yat8IXvhW6Q9Nvm4g3YQQcOV8FWZYyvA1OidhhXO2PwbDdwfQgybK4dqxY7LFNtB249b4W25BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99551" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=lR0PyTwKGY0ynI-W7MrUNzZvdd40e65ERcYVQFaoHwlCUH6R7JQYvMBRXLOO1MnyRsqx40Dd6NeZqu7T4TbLiW1W6A1yKC5rEN08QcBwe6WU2FhkK26xBmZokUeWJOnGCvFfurbmGRKvRa76nMZvwKEQcz1t08BgkTTYAb3BL7MtANwuSHwg0izs0EIARW6dCdXfo7V0uMeXU57moa5dHvmlkdJQvyb-qfL1WYUXE4cvNtUcrLbVmjxlMpHUM7j5NNQl85GbV42ItK2hhXGD0SAKAP9Pr9FHgMQKBSjyvDbmfRNjndWK6gOrkhV4mWEQMJCpKZXTV1rOheJUaTnc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=lR0PyTwKGY0ynI-W7MrUNzZvdd40e65ERcYVQFaoHwlCUH6R7JQYvMBRXLOO1MnyRsqx40Dd6NeZqu7T4TbLiW1W6A1yKC5rEN08QcBwe6WU2FhkK26xBmZokUeWJOnGCvFfurbmGRKvRa76nMZvwKEQcz1t08BgkTTYAb3BL7MtANwuSHwg0izs0EIARW6dCdXfo7V0uMeXU57moa5dHvmlkdJQvyb-qfL1WYUXE4cvNtUcrLbVmjxlMpHUM7j5NNQl85GbV42ItK2hhXGD0SAKAP9Pr9FHgMQKBSjyvDbmfRNjndWK6gOrkhV4mWEQMJCpKZXTV1rOheJUaTnc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
چه اطلاعات مفیدی مهدی‌رحمتی بهمون داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99549" target="_blank">📅 14:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be29LQqnR7coznpZbrXlasszSFVdr60KFI30-gkDShBZxz-0F5Ql0UtW3NwFwyekQYwKTWYhiGvD-VpTfT3S_ZeQ87LUH1A7hB4LxywCjR__PvagGjSIhx1VPghKmxnZRaNGKzIpnWjvHvDn5NhXZLFI0OgKbz0ZxGAOCEWo7jbiAsDLYi3CTEjyryaTDAlqG3Nb8q-Bn9SamBEmaIeBAMq_WPElXNb6sHYdXEyHO-XJvvAuAvCr2OQ1kKZFx_CzdNOqWHpaWdYtKqA_ag_X2e1Ql1VpigeROQYXfqa708yYlguO9mywrjxY35WWRyHDf4Znfu01Y4DZgKsv6FC79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99548" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuNBheQAq3u4ooNYuxOkIqxQ9z_lSQ6paBkczkLFGX4IiSD8qMy4WUMXvRwZJ8mig9RiS1hrlJMEtU9KO9ZYG3zNQCbFUfjnJXZwToSkEBjThLqt0ZsYXCfcn9rT9gsuYELcSCJDxUSkMiw2rRU8tQivmoPZNCPH2LrVMG4L8vBVD0U2UrYGnM-8_Cf2qwMXObUT3OYi9rpHCkZbJkyGonMXI_uweUD-GIwUn6i1Gq_ofL8fr9KyZgOhhWa1zWHOwqDAAfN_oWgPERP2SX78xqzn27yghPPZTSBc94DGbxCweZ9mGrTu4QGdtif2s8MOAZPHLMOVQ3hqUs9WLI7gjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‏فابریزیو رومانو:
🔵
بارسلونا آماده ارائه یک پیشنهاد جدید به کلوب‌بروژ برای جذب جسی بیسیو، وینگر 18 ساله با استعداد بلژیکی است.
✅
بیسیو با انتقال به بارسلونا موافقت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99547" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2YgY43w0JQo4qN2X8hcS4yvys4rcz6CMPygfZAIWfMCzfqyGYs8NZY-Yvo3d1GLiRKIZZlaNAdQ5UMC3hRvtLxEuw9VNuxRvWMaQOOHs95RljCslwba7CN_7GCj69pRVqICy9jkmVvwAL6fq_eArBX0oRqrIDYi-X7NXlxBhJgwZWEWt0d9AkSha2iTq6G8o5CV_6mQMyCcKeOVvbP3AmVRbMszUjvMAVw84np-mlxVAuPXTFzWW11no_A0QbGmkQlNN4jvO4K2zqh5unJuK7h3vmWucbk4rYlvo8E2OAMR4VrI5dGrnxBdTXJnihicG8QzNmq2-dCjIngA9MmTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل مرینو اولین بازیکن تاریخ جام جهانی است که در دو بازی حذفی مختلف به عنوان بازیکن تعویضی گل پیروزی را به ثمر میرساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99546" target="_blank">📅 13:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99545">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFGPiNsn-76KluIKKb3pancFmtGYYLi-ljWR52cOVDZdT82ctHhibYxf35MV1fO-kwKDVwkADxqbqTduf9LT58r3iI2h3bcmCnq3cpblvJEHe139Aa7O89Xz76gRHXIG8hJo6m0ducP6klolBCsvjqj-XQs2swV0jONHykl8AmpXJXtpIeeTqnbdwVSYErkMc-gHYjPSJ6e6h5tRtnp8SjB-Qba9RcnlBugpAqo6lBRcRVu_p_t2ZMwfk1DE_fWhJBaNsi5t2Eor94HL0kHR2oJs74TlpP1h09C4I59P03euuAPrpl0h1JPhLw0TLfOntjmayNHY8AjHuGpZr4q8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شانس صعود انگلیس و نروژ از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99545" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99544">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoEneuXr0lw2EhdJ-957sW0Imb_Iqha9jnes5iCwS4I_WnbZECFgQMWoGoHnhyAslfDAEDAcxGcbAyf37m46kZRYkjAVOD8cXTBR4jNw3ia02pEO0FQHeEnzTGsRdRzlXdh6U4xit7OBzW8ih-geb4aj2FuqGDAzvIabc-dvv1gztznduEVxhEZujHxji_G6mEXN4S7THamezml3peLvI10vbUckegf36_ZpKGDN0OvFN2G6ep40DScGJj3kXjLAA9MNjDPCv4w30gLrebObeEsbr6MgBa6m6po0Riv9KXjc1FZ-T7SUqGwD7rq3IxMkBqvpKiamRpZ-ge-Yf3J13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کشور آفریقایی که از جام‌جهانی حذف نشده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99544" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99543">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgT9M7ZWW89Ct_dpUTKYl_W3oSLaMt_LJqE0E67TMkBx9sLMXbMpXYFc1W8gQnZhGYIeSmbL7sDbt87nVtXgXt0LVjyOvmpM7haAM2-iHbZO7RBOLABMGMhvtzG1OlWIrTo9No1of3XxmcBQ4e_E6Z_ANmm3DtcquAlEWcJeKLavTebOVVaWwTuubPPhAkpPTw2Wg6t9rWGnn9aeVg1fy4Xv7O4jxiyJqhqb1PmbYQBF5txRiSiDcdlFoG9kSOFkMokcMoDWqa8QNLk3duw4-lIEYg-pXW-Ci49b0RYMgSnQ0j9gPbktS3FKl7J0bzxVfnCIo2jJKmWKM-VcZpJ8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| رودری، بیشترین تعداد پاس موفق رو در یک‌سوم دفاعی حریفان در طول جام جهانی 2026 داشته است.
⌛
از 180 پاس، 170 پاس او موفق بوده است. همچنین، او بهترین درصد دقت پاس را در بین تمام هافبک‌هایی که 100 پاس یا بیشتر انجام داده‌اند، با نرخ 93.41٪ داراست.
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99543" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99542">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPK5QtfTjtE1l7ITKn9Ya1Ek46-lr6doKJdUDkYGtHdH7kPr_DOF7IiS-Zir87YyNVuKzYJpZOkRfq5H1FjJsLCgje4XJtRrlhkB0fXmN-3Ym5yjOTwUnCq5KxLEz9aU0t96rsw0NzKXZOcL_deKxeidCKu_TrdDrfk8vwAo9-bw3BHpqb1-fc5TGjPYrG-vea52CxnHtETtYbCWCzUqNZujyhWZE1piP9Ow0Kb_XDKkKY2noO3nZx09RTkXIhccdufcPfYMaLd5objv3jtDVKZOHWD5wPzsspey1qmhZo2JeKWsfbV3wgy1HHYze9VJ5pimYX3H0j7hToHhh6Iq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99542" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99541">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyhztUmxilrqE6K5h0vcNZnKNokQcz67z-CKAph6ZxXV2PiuQDqbOFNj2Xq3WhYb8csMRBVsGcmdiJmWJVLX7w2TK_4ZCs-hWimCARR-S49Ad3xUenqJkXUBchlR-bLX5nzD8eN1jCtZ-C6N6O0U8aALH4rofR1_uZze5PC1FZC9sY7nsdlueRkA-vVE7SiNxwTDrcDyLidqmY07IW9ykp-DvbuI_NPhHvXvulRAUC7No_PDp_-cqjhsXOnFzCYq2V97bWj62nQxugxgYEHDPhjWvh5e9yMo4Odo0HFfcMHr01_Lm8bH0oWkqZHQ63mUJnxYzYiW-u4DAE1c3KxXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99541" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnuFmQF9IQW1-DZfRtALz0C-lnLnO702iZwjcbBCQql-jZSwcxMrHGnEvFC_BoW1BV9_KJLIY6tOVU8LjKed7v4Raekx6YrxgrN-m7en838vNhjjAbH6ix3Vg4A9yw5PYDq5LpBjsgrq5r8YhdZPv3KFCnFTG3hxXAmI_K3rctWntqq9z_uiZyeqo52tCb7bf2agoBIp7bhke6-InGduxgWDzzn8QarKHmZ60YKR5E-UjZ5khg9w9SIaTlpYrJ5LRRUCIrWFEGl9sbzwZTemfjNmf8yBhK3clThMGtv9OcI2aC0izhDX0ZffHTTjnW6dMxamO3FXQC9Y_ZDnP3XzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همسر جذاب و دوست‌داشتنی آقای نیمار هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99540" target="_blank">📅 13:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=liPIvjBFLr2D9bU1u5ErbjMsfKAkdbnzfH730UdiWFV_OBLBVSzp2SR3DME5nS1jbE4GSOi97vl4aWkT447kvobXruCinOJsZ90KQLauqBsRRYJ3-GPc3h2cX3JJLoS4RvLid1PCltD_30qJE1_JXIjpEhl_-GZ4QHyrpDIYPNW-wB58PH9aV0M-HnR8Nj2YeJzqe-eId-UcLfxo4nmM6IwUEJdn5BW5LW_2tzftwfkW5FxjxM9w_R_vVzBy-Iu6rU_hHfZKqAL2pl83l73Fuy4Zx_5ee3d6PQ3kb2uTtvXFljUcrCMVPM-oQvhFmgM24Ow9HLGeWkfLkDWv6xo3Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=liPIvjBFLr2D9bU1u5ErbjMsfKAkdbnzfH730UdiWFV_OBLBVSzp2SR3DME5nS1jbE4GSOi97vl4aWkT447kvobXruCinOJsZ90KQLauqBsRRYJ3-GPc3h2cX3JJLoS4RvLid1PCltD_30qJE1_JXIjpEhl_-GZ4QHyrpDIYPNW-wB58PH9aV0M-HnR8Nj2YeJzqe-eId-UcLfxo4nmM6IwUEJdn5BW5LW_2tzftwfkW5FxjxM9w_R_vVzBy-Iu6rU_hHfZKqAL2pl83l73Fuy4Zx_5ee3d6PQ3kb2uTtvXFljUcrCMVPM-oQvhFmgM24Ow9HLGeWkfLkDWv6xo3Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99539" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‼️
🔵
🔴
جزئیات لحظه زندان رفتن ستاره‌های پرسپولیس و استقلال از زبان ناصر ابراهیمی: من که لُخت نشدم. به هاشمی‌نسب گفتم پاشو خودت رو به غش کردن نزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99538" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=ECFWQDPQNFDFwSbPrvjIp7hKIyJT7G5UG-cUXRCD8zvHMU1WcpwcRNfXXZ9wxTV3LhfR2D25sjSDWRgHQO_QBL2GzXgvhLPBHJc0cq7NeDJXKw4ClfB5X5KQpSI533CYHIt6eYjv4EzaRh7NI00RniaaL-zMFkBvwXH_VuFMboyKzlaWQ79NWb5xXWVReTnYhNwxgoYRv6IdV9Q2EQj5cVSUCkNvzjSX-hrl-E4NCroKT_Nk0JKOftQgKBM0r3wLAlgnY0Rrz776XIT2zVGWMaJDKtOyOLhC2QP-BAqlYm4psv_bOZSPKCEq7kyMVKLLACuVv8ktPiMkxCS4svIqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=ECFWQDPQNFDFwSbPrvjIp7hKIyJT7G5UG-cUXRCD8zvHMU1WcpwcRNfXXZ9wxTV3LhfR2D25sjSDWRgHQO_QBL2GzXgvhLPBHJc0cq7NeDJXKw4ClfB5X5KQpSI533CYHIt6eYjv4EzaRh7NI00RniaaL-zMFkBvwXH_VuFMboyKzlaWQ79NWb5xXWVReTnYhNwxgoYRv6IdV9Q2EQj5cVSUCkNvzjSX-hrl-E4NCroKT_Nk0JKOftQgKBM0r3wLAlgnY0Rrz776XIT2zVGWMaJDKtOyOLhC2QP-BAqlYm4psv_bOZSPKCEq7kyMVKLLACuVv8ktPiMkxCS4svIqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
لحظاتی‌کوتاه با آدیمی‌ستاره جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99537" target="_blank">📅 13:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed2u_D8ppTkroNGCJtAfA9ywxR1O0uJBXPPgEff-rHTVVgRJ8P7W0E-lUrAfYKNwUaga7HnuPhtfzwiuxVr2-PWGBUvVAjcIZ0KPjzisKu7UCA5Rm6SzCMtJ_vEGgjkBxp5tNN441YVwanDS67pYBB5QxACq3yFySv0R4KLpx8XexUt-5cPDOuY_EuXMjVAFityJ05cezbGOBiYJ6T9c3ZCOq67AtpZn9RIj5CKys3uh7p2aJXhTu89bfjlXBXqtpZR5XzRFwPsDs4BzXjQnELwyXIsLtM-jRIZbyc8ftR1DKZBONtz0Sov8e367m_pybJyl_cbktyhZODiRNmzLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">12 سال پیش تو چنین روزی لوییز سوارز به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99536" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99535" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkteXhJrWMgYVzCuMbHFjRY3HpZDlqtkLhnWMvVxyX8u1Q78ivW8Pkhu_mKuPyhKyl2NFJz62PPWvuO3OyhPjEnYxYT0wg4u-eM8Kz7d6QEuMrqwblCYp1fFI3QRE-iVSJvYYd-eyGRw1uRZwzPJXcOfR7FkPrmVc1CUGD0LAA24d_c9_y79Adyd5MDCHWpqWcvO7tbjayjvb0YjhXkqO0_sah7_5XFSnsQsZZ6CZUARkYIJH7toZ4OUfAE1loLKvWXnkQERbsk5ehkUeGb3sVzFZLr0zqjfRbVN2oa6PilONZ2zymmK0xN-3NupRDeeS7CAk82_8LIzdm0cjeG7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✊
برای یک بار هم که شده بدون استرس شرط ببند!
❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
0️⃣
2️⃣
🔣
بابت هر شارژ موجوی اضافی بگیر
0️⃣
2️⃣
🔣
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r20
@betinjabet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99534" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=AnVFj5lRZWPxv6gnv4LjcMcAod-Hz-QMjkcJT7JYNPBDDDeXlYyIg5YnIamE_WYdNFz5jgI0GXt-VhwbtGVDSxDKHesc6Z2-CgMU1LNX9Sp8W2t9rThEZFq26U0pVjCSLficQl2QtXY7OXCcPEXi46TrbqmXpkJjpglPQPm7h5d_H8GCdnuduuGMJ4I2lD0zZg5tmfuKVicYZQRk-fA5-oi3vLPFRNhcCXUy1-gkK8K3exKBkkYqZ1F9toItfXl3kilQavs2cX15521kNfnZTG25-mNOkdDLHF83pnw_irTylxqKktH6TuaqORcuMkou4gOjVTEs-zyW-m-eumMHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=AnVFj5lRZWPxv6gnv4LjcMcAod-Hz-QMjkcJT7JYNPBDDDeXlYyIg5YnIamE_WYdNFz5jgI0GXt-VhwbtGVDSxDKHesc6Z2-CgMU1LNX9Sp8W2t9rThEZFq26U0pVjCSLficQl2QtXY7OXCcPEXi46TrbqmXpkJjpglPQPm7h5d_H8GCdnuduuGMJ4I2lD0zZg5tmfuKVicYZQRk-fA5-oi3vLPFRNhcCXUy1-gkK8K3exKBkkYqZ1F9toItfXl3kilQavs2cX15521kNfnZTG25-mNOkdDLHF83pnw_irTylxqKktH6TuaqORcuMkou4gOjVTEs-zyW-m-eumMHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇵🇹
ژرژ ژسوس در مراسم معارفه به عنوان سرمربی تیم ملی پرتغال: برای من اسامی مهم نیستند و هر کاری که برای تیم ملی بهتر باشد، انجام خواهم داد.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99533" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
