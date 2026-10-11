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
<img src="https://cdn5.telesco.pe/file/pDL0E12lylfR7sm5ETUI21Ip7F8QQKI51pFHdy_ibHNW578jEdUeyJM-eKHGqnJZUo3yn__hSIR1lXA9BMTVBnZAOGR_Y2Sx-3waRg3SMzm9bysaC0QiBq3u8uO5RqpUmW-NJVc1nOTmFm35fnojqYuueAHE7laFLbuhguPkZxpYKjeDfWAb8XebhC3XyFc2wNOtt8IKqtIIfumhZXnOquL8bxW1Ys687WkKEKbA-G4jaQQrC9rXQPyYddnKIqQEfIhrTpBkik3vRS-cCDplYxPkwmvKscbkzkQrNlwY4rFEvI41h8TN4_EnwxyeFG7kDKI_TdEHLFAtIcA3l4jtfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 385K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-108361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJZZkm0wy2aiEKTj44heyXqmh0t9_zy30OZal7wiBHBnHAu-9GKkPcbnD7J3D2wElNdrQ27LgGP8dIXf2Jx-XQkC44s5Q0tD7BjFEFq3VTbg0xzoPHNBn_O1qc8mGtTFQDuEmFlwJlnTnUy9vNIJwSniliHRmed9tgzqeO1Im1bVrRlA6VzW6ok8sEf8-ztz8TkD9d9JJxnkuqIhxBeRUykv2dOKtbrf_1CkUASOZC6M0s-PO6JW6BU-k9mvYzET-p_piIY49WWPnN3Y4qcJ4o47B_eUHQqfaFGTOg-sKNMrhKq2PzgZS4_AmQNJ5B_Ssd7kEdv1JkydkTpYw-8Z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/108361" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/108360" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دوم منچسترسیتی به لیورپول توسط دوکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/108359" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به لیورپول توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/108358" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
دیشب بیچاره شزنی سرش محکم به سقف نیمکت بارسا خورد که همه از خنده پاره شدن. فقط واکنش لاپورتا رو ببینید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/108357" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد ربیعی: سرمربی تیم ملی امید نمیشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/108356" target="_blank">📅 19:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رختکن شیاطین‌سرخ بعد بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/108355" target="_blank">📅 19:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بارسا با 9 برد از 9 بازی به دیدار مقابل گالاتاسرای رسید.
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/108354" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
ترویج گل‌زدن در صداوسیما و مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108353" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3e_Msi5Bm40-HPxfabZu-mL3_20qvLvMwxEugcMwm1h7lnt3jSQC_cKeQBVOfDAXCNITvKWbrchw__4Ho2pj6gS3YNtrNLmAVO-Yvy9pYCoy2KX02yRDQCvBMa4gcSxd9YB47Lxf2yVb-2niF4NoUNOyxlBg9qDleUTYu9HUd3YdYW-Lloz7YTyzBylNurQEcjz1SpIGrRKa9tJNIevprAxSeLKOoBZDByCyxnk7qubik2y7RNWQPmtovyXmu_oMrSdIRFJrvPi1UY1q3yhrujnLTW58bjuzPcnmdBetgQLFDJ2pQDcAzorBTok1f-QM0vOMyYAtLP7lGIVSkpPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلارنس‌سیدورف از شاهکارهای مدیریتی تاجرنیا که به مدت چند ماه بدون هیچ کاری چند میلیون یورو از استقلال دریافت کرد و از ایران رفت، سرمربی کورنتیانس برزیل شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108352" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlwnbDRXonE5ZX09_Nqx0f6ON9I4aa6hkpqitkfU6XRJQw9_uW3LkRC3YwUf1G2-UcZ2USeNixFG2tS2lPFoUwDblKEhOBN7CMZuwYs7G1znJ5myhsXD4FIXg7h9S4BkwKWhxQrYEkW8rng9RmYJnQfDkfzs8SsRpZ5MQS_f6pKDSv1Sr4x78BEFAov64M3T7g9p5CYF2A0bhW7bcxnrwMp7Q6ZcN5A9xPDiKVblVSgfxrR2KL__7euhpLVuzyX5R_8X7Oh_2MYDmwcz_P2rt0J_R1heKnsaV4cTkOSu2tXpfl8nXvWgi_Zd18PqaefMksZl2-e5QUw0YTVzqyiczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXXqeraMtM9uUrNWdk2cyKgGLnsYnpYCzez4aQr1u8W3SFfcU9R-ZLawbrlxD8zFM2slMQXRbBtRzJRpsHvyYW-Ve7GWuQTl6ME_U0udwiHIlH8-tSwZOMDOXZ1cWZKv2vZIO0EzTZ8xXVeNLC1mfYcm6FmJbrtN5bpJXYInGkeGuuSsmtEqAaZ5KlIsM2xloDctKBX2Dj8NqmZVZXR-5N3b_kpkjbuVaHVve-6tSCUejwSXstnSSPqpTAVNxofGHeFbxeXaALalP-dRMP624Y4Lqjbmixse4qHY8TvuLuyxsZC1-zAvgF4lkYBoHQmlAQfAGQ9Qn0jnngHiT63j2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچسترسیتی و لیورپول
⌛
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108350" target="_blank">📅 18:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR05krKe9fnZg14jAeY9ZVr3AjNI1Ni3hoB7uD8Gtld4C-mCAkH6EzXkDb8Uc2etYp3QyDRqRA-GJ_aAAbVfevULmetKwIBMDUiOdY1f1eRT1xtiM1Ne8EB2TanwgPWBRBAd9Qo6krVILcr2l1wOGpGDHxiEhzg-s2gXOiRqbmEwoylqpMRJc6XRYmQb_N0hkqDTQnxTRtzlNHAJfE8zxOMBcIWoD20TPu5UUz1-L6OXq6oPWDJzivgX_1zC8fdftoaLi2j8vCvnT8bdE75RM2bM1jZ4xAtmP9_lSZDnOpmmDlPtPs-nf_sk73ab9JFCrXVL17iLnBIPxLDZ1fR2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیر سفر گل‌گهر از سیرجان تا بحرین را مشاهده می‌کنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108349" target="_blank">📅 17:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب خیلی جدی ادای آخوندارو درآورد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108348" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108347" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/108347" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbruxj_aqXRY21nP26LabQJpDIzPemaKsEd-srEga6s8m2t4Tqe-TXGKSo78lP6hoeroENn2XgTKgk2TeN4ch8VIKNDmB8lg7TNzG-3T0nkBV1y1gTkM1TNR5jYntJNpJT37JEKNMLxFzCM2tF4S6-SHLdXYxBsgRV8yUH6Z8neU_VwC6YTPcUxnv4MkwxrQVQ15HmJu6JMnMliwWbncdInZWT5UAOGRhWwO9ujlxEKrMTNY0gRjj0r3RKOYetQ8OlRdxKSDeTxV_bRwug2cjlCbO-8RxTA3ug-bWdWclQNOngmPvLxfPYnJOGpUOTgEv_AOyP5DSN8MBMp1rwKxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/108346" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس سمی عروسی گرفتن مسعود شصتچی در قسمت جدید مرد سه‌هزارچهره
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108345" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842c49b387.mp4?token=Ad9lZT_45ssxelX7aijksUrBqIo5GSz3wZnvsji52j-OL9yr-Z_P7uyXJpDjWqCXArcYFT6VrrzfgjlyD1xyjgZO6zj9DrebbgEwOkTQvqmoF0cXVP9ze5Dxu5X60WOkpvnY2vm9VhcVjGSyVqvskUNfxIZErOKhYcg20MO4HmMHqalMbBUMNBtWg6H1Vl-4KT38BgesQw1DQmzZ4aK741RBERd9O4ygBjlcDdhfzAqw0phY76JaN_-rcM9Ey3O0jn18z1O2JUVz0DNvq4g31-K860yUbnfXWid7tPkmvMZPdUbvOqyVQ722oTpScrA_D53Oh3mHknfyX27svkHlHJBvKJ4CCETBFJotZcc5RfF0fepTOAC8OBiL3ixSNFeEnB7Zd4xrBXl2hWGM1xKJ2cc8qdW_XL3npprRFg6P-Q1nASub-IvdX66WRlyMybnhXvVQONUsXyCJ0aHZ91ILw2NVN3jOZNaCyJQn-iW7OHsVeVKoF3UQiqmeeCjbOZfyjFq9SepgkhZ8Hed0SG33-FOT9nNlZxyPuP5YgGDAgNkI3C3OY0HGDlQFcO4xw5cLFv6yK8y8cxxUHn5tLGbTQ5zn6SqoIrl_TDOMnG1X3pXOo1Kja5ad0wJCgWMZQNHNXxRFgFzbZOoFZPgZKpn-xse0MZy57Em3I3-7gYHJcIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842c49b387.mp4?token=Ad9lZT_45ssxelX7aijksUrBqIo5GSz3wZnvsji52j-OL9yr-Z_P7uyXJpDjWqCXArcYFT6VrrzfgjlyD1xyjgZO6zj9DrebbgEwOkTQvqmoF0cXVP9ze5Dxu5X60WOkpvnY2vm9VhcVjGSyVqvskUNfxIZErOKhYcg20MO4HmMHqalMbBUMNBtWg6H1Vl-4KT38BgesQw1DQmzZ4aK741RBERd9O4ygBjlcDdhfzAqw0phY76JaN_-rcM9Ey3O0jn18z1O2JUVz0DNvq4g31-K860yUbnfXWid7tPkmvMZPdUbvOqyVQ722oTpScrA_D53Oh3mHknfyX27svkHlHJBvKJ4CCETBFJotZcc5RfF0fepTOAC8OBiL3ixSNFeEnB7Zd4xrBXl2hWGM1xKJ2cc8qdW_XL3npprRFg6P-Q1nASub-IvdX66WRlyMybnhXvVQONUsXyCJ0aHZ91ILw2NVN3jOZNaCyJQn-iW7OHsVeVKoF3UQiqmeeCjbOZfyjFq9SepgkhZ8Hed0SG33-FOT9nNlZxyPuP5YgGDAgNkI3C3OY0HGDlQFcO4xw5cLFv6yK8y8cxxUHn5tLGbTQ5zn6SqoIrl_TDOMnG1X3pXOo1Kja5ad0wJCgWMZQNHNXxRFgFzbZOoFZPgZKpn-xse0MZy57Em3I3-7gYHJcIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
رونالدو این‌روزها کلا اعصاب و حوصله نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108344" target="_blank">📅 16:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG0qJvueh3wjg6sRxuxxhY-I5ewDX8qm72hlV8K5FvybPZeyfyA3rTwMpXqX14TaeAkJohI3x_1zp5hc-c3NshVNIEEUzIJ4VQsZIL83uMQIx7sgG9PrjDLCtaYtqMTOb-ZWgd1DfJKk7Z8Y-OatkwxUPjlyL5O4yH-3BImk9arm5Y1CsjEGpN6bO4kPRMNSYU64S9itX2C7DyeQYRroIJRaDW-cdaGI29C0svIxmnSk3M0UtWbamQlBTsPsfIEljjsrqNo8sexA4owenGzpJFSWMjxu6-Ec3w5dIveRxwaVSTKT0V-ySXWr1iHojr-YmdKK7DktCqoVjRO194lBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
با اصرار یاسر‌آسانی، پزشکان استقلال تا ساعاتی‌دیگر تست پزشکی از این بازیکن خواهد گرفت و در صورت بهبود نسبی امکان حضور کوتاه مدت مقابل الغرافه وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108343" target="_blank">📅 15:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkhgCnF8dnpnyOc6lDgrvEtNy4Kpcj0q6acG0SdHPQgSmdpV-J0rtafZaMWNXBy2slX7cRzyR50cQcMnH2EWPRs4Vo2gfvEvaSika2DGxBDdGetq2mmr9Q_a5phPOfFiz9QXJi-hmhgKLURonxejKcRCzxqAY6HFEcYYZBMRKUiThQ0TDK5-fkc1rzZ2iNLR70N2VSzU7M_7k3BoaGyz0CHrpua41QFXU-kymENRNTRjY4uKY4oKUpra6zXH9RY4SfZjpYJYVVWseZJi4UO6eWljMZYtqVehOLty78bYsHb6dBnJLxXePNVkMWP6yCnQxbBQKh7EI6zs4VtfAHYyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108342" target="_blank">📅 15:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT2VNlNg-pK1c34UjdRZ44dtifmKKy2hKnccHE2a7EtBwPLkdXJs6OizjEo5UBOcwFAzRfQ1n3zZML9rnnLSZCUQjnMYUpQR7ophxj_yNFCrj_LaTA_UBQ8P02-JAR1-DN_xBYI6jrhtwz-Cb2Ba2s3Bfzu5jYEtQWEnF6ye8PZZwjmVcvTHQivLisMVpTD1TGmF3p6Ift2PsUjZKq7MzkgKHW6duuQHL-v4GR06CerSYF4gOec-c5CObystHmqqF970M57KfgiPahm4fmNLv0Upv8l4xJlGmAvDxbF6RED6bktDqHCbqYQ1V9Udtvm_W6aZjlkaoHyiEFnG9_kbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آمار تقابل‌های رو در رو لیورپول و منچستر سیتی در طول تاریخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
110 برد لیورپول
🤝
58 مساوی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108341" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش مهدی توتونچی به مصاحبه علیرضا بیرانوند پس از بازی با استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108340" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه‌سنگین ابوطالب‌حسینی به ژوله
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108339" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
واکنش گلزار به ساخت کلیپ‌های هوش مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108338" target="_blank">📅 13:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbt-7Qyswj2KuE_Ht8w7X9pXVecBL4RX4UPM2MzK4H-usJODevYJaUTOuZI03GiAPFp8TNepQI26LBeybe3IYB4HJ2MQNlc1s-UqWYPbkOlHg7Aeys_klwnhcrEOjkQQzmfnR65bd1EzmVZfR_g0C_sWo-zLYSWtgjUXGunZ8NF_8m_TOFGBSTKLC3oItjzRYHqE2LX0TjiELdspGWn4msqFwPnz7FWd8V5JwSRbFo7rZr66FppH6rODyz70HwQ-GxVsjY_ko_icWKzMS92_cJFhJcBkG3jMv-8CYboSsc8eV5aj-t3GDvWSupnB3vX93ye58nRQOm1hso6HmSdrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر باشگاه استقلال ایران برای بازی الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108337" target="_blank">📅 13:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تذکر تند رضا گلزار به قیاسی درباره ایرج طهماسب؛ گلزار با تاکید بر جایگاه طهماسب به‌عنوان یکی از چهره‌های باسابقه و پیشکسوت سینما، از نحوه صحبت قیاسی درباره او انتقاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108336" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینی داشت به فوتبال برمیگشت که ناگهان ...
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108335" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOrOvD1JIWfdr9zNglo-3XWNYmYglQ3qG1kpj8QbtqcirdfN2PwYknguNIWY2HnYv_CmP8_ArKgPqnq3dMFjk1SSozhrfYUnPX9vHvCn4D6vQbvARTTyzPxRXfsk335y6FX4Uz5O3QUmnayWS9CIFTmb6Y0CqTDL2U0c-sReEoVLmKtpl7ZoMfYpYfgkXuOMJMirMV-RmzZhhCSgIARtBnJB8_Kxfg03ZvZtebYhCZ8E4S-NqePvyjljMxkHzvC83Qq8P08kQPW63MkBkb2f_5t2Di_GJsfqmEo5_PnN5P3AZh72p1YIHSi8zA6VI5aDHeTJSk-LXB4ZizM7E6ZRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108334" target="_blank">📅 12:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پشت پرده دستگیری مهدی طارمی و سروش رفیعی در جاده شمال؛ رویانیان ۱۲ شب به داد فوتبالیست های معروف رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108333" target="_blank">📅 12:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108332" target="_blank">📅 12:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای کروس کجایی؟ رئال مادرید بعد از رفتنت دیگه پادشاهی نکرد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108331" target="_blank">📅 11:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ختم چالش رو اعلام میکنم
🦦
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108330" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جادوی دیشب اسطوره لیونل‌مسی در اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108329" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل یک فوتبال
❤️
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108328" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108327" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZQoOL3CNIgUHF-U0fp44rDoVZoZney9NatzdKfM5zP7xcO7ZpgV2fJH84TvywVlznyvWXbFCGXaBEI8SIHv1a5-hwBTUecWsI23VT1FTY7BSOeWOKXGaRdhpxlo_WWSYx41WMKAQYtZtQgCFBzvElksUAvvjWQm7V_5g4VCANyZ3yua9GO3J2mKEPk8Gg35Alaxr3EMdWjzKh1ghlngPMKAe2mQVYWMYaVCaSStq5hTfN-90SP00E1sJOn3vj5-HcEwnICLx-Sb9LHwDJWvLfTWwVXUNiSPEjKUC3imua3rEa-ONV81EC-TgDge8H3pk6u4vtzjbo5AR_9Jts0uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108326" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxII3TBqq_yfTM_wK6QgMC6R4rwCYkcbohnQSPqTu7bDQTvnCgMYnq_wcqlY6NuSAzD-4uXmbI-jhAIDTWwUAkGBKVQBLduYIz0b2g-Bdp_IB0c2pdllIl63I_zjZnDkC8RlvlPZEsfJICeKdnsyz8CMbHLM4WGkOWm0CqhnGc4Uy9YY3pNFW2p9ogYdKPtfxRWObaM-TA9zBZhkBxvuCFtAW0-bi8cbO5GC1ga7l5t4jN9XisGym_1ImCtLSrdQHl2AtsUpF6bt4x9iPKBqatpiL3xak8494KAn6F1a-55yfUKmid-asHssOSbi5DLSBVf4MUga0Bf7iSP9mbNHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108325" target="_blank">📅 10:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نادر قاضی پور، نماینده پیشین مجلس: تراکتور پرطرفدارترین تیم جهان هست. از رئال و بارسا هم پرطرفدار هستیم. کل مردم ترکیه و ترکمنستان و آلمان طرفدار تراکتور هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108324" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
بیژن بزغاله 2008 روزی 4تا رونالدو و مسی به عنوان صبحانه می‌خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108323" target="_blank">📅 10:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108322" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
🎙
رسول باختر، کارشناس حقوقی فوتبال ایران در گفت و گو با فارس درباره یاسر‌آسانی:
🗣️
درباره بحث مندیت از آنجایی که این موضوع به منزله فسخ نیست اصلا نمی‌توان به آن پرداخت. شاید باشگاه پرسپولیس بخواهد از این سند به عنوان قرینه‌ای برای اثبات فسخ قرارداد استفاده کند که در این صورت باز هم فارغ از اینکه فسخ صورت گرفته یا نگرفته باشد، باز هم تفاوتی در ماهیت ماجرا ندارد. چرا که آسانی بازیکن جدید استقلال محسوب نمی‌شود و به همین دلیل از نظر من بازی کردن او غیرقانونی نیست.
🗣️
اگر بخواهیم طبق نظر فدراسیون فوتبال پیش برویم که مشکلی وجود ندارد. در زاویه مقابل ماجرا هم حتی اگر قرارداد را فسخ شده در نظر بگیریم که بدترین حالت ممکن است، باز یاسر آسانی بازیکن جدید استقلال نیست و قاعدتا نباید مشکلی برای بازی کردن او وجود داشته باشد‌.
🗣️
کارت بازی بازیکنان توسط سازمان لیگ و فدراسیون صادر شده و نبود پروانه کار این نفرات در نهایت نمی‌تواند باعث تغییر نتیجه یک مسابقه یا اعلام غیرقانونی بودن حضور آنها در زمین شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108321" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
پاسخ زیبای سیمئونه به سوال درباره مقایسه مسی و مارادونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108320" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
گلشیفته فراهانی توی جدیدترین فیلمش از جان سینا اسطوره کشتی کج و قهرمان دوران بچگی خیلی‌هامون لب‌ گرفته و حسابی خبرساز شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108319" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=blGyQIqHHeK6pSXTOBsg4MWove6E9iSbKKWQdrWXZX67vzbrn0wIFJg7ce7HZpAENEt7ioJwdAXFOKEY-AvaY8if9-8AvJek_4PuOfAE6DjC7TnhZXZKwy5p4XfQz9hFB33DCUrzwePlq_UPUEOpWb2dpupT6phASoDaQYMbr85k4d-Kknxl-tkg6eM_jOKyuJJPnsYHeyzasdt1fIYcdIwBJCJz3VG4b-QAAd_Px7UU9t9JDm2NH3Mck_z3Si9wA__GX3UPRC_19wDom9_0AkeTh6hH1POooN-nVmE5IoiDCwN4VhyEN1D_RW9Pp0hPb_q6TDX0SAfy_6jDJ2Uzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=blGyQIqHHeK6pSXTOBsg4MWove6E9iSbKKWQdrWXZX67vzbrn0wIFJg7ce7HZpAENEt7ioJwdAXFOKEY-AvaY8if9-8AvJek_4PuOfAE6DjC7TnhZXZKwy5p4XfQz9hFB33DCUrzwePlq_UPUEOpWb2dpupT6phASoDaQYMbr85k4d-Kknxl-tkg6eM_jOKyuJJPnsYHeyzasdt1fIYcdIwBJCJz3VG4b-QAAd_Px7UU9t9JDm2NH3Mck_z3Si9wA__GX3UPRC_19wDom9_0AkeTh6hH1POooN-nVmE5IoiDCwN4VhyEN1D_RW9Pp0hPb_q6TDX0SAfy_6jDJ2Uzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت هوادارای بارسا در این روزها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108318" target="_blank">📅 08:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108317" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108316" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1G2jFigGbK3YKS6vkh6wbAcz8tm2Ot_dFwSkhoo9vgO5cQkeYnO2RyJwH2NMD9SHy9i9GDARTTbjaxaTDCmWNwWE5DOq0lDI--8V3oclHE6PjC8zxHgGHm3akrsxF4ZGbIyvpbfkD8wGg6ItW4yFSFaE3iDl4zu5o10BD_MFcQHYq7KgUBMI7lyseWNC3ztENe0sC21dTAr53tOU40B8TXE-DTP0IwTTkGifW-d0s-91ZoqFovvCE4dIMfuryucd9CVo8NCbWAtSjGJwEZyqe0IQx03Vth5HStqia8upz8U5WL67V8SoamD5RMcva-VV8L7r-TK7AIaDvOr9ld-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6LJ0Z8-a-8Y35HxTC0pg16AgOvRqsEYu0ncI989sz3CwUrkUZ7Ca_kP9hdfzft71mBxMAmvPZAof-6xgsAZg4EoH6Qfq_cxx10zT1uKQXbhW6ItiU_v17fQfnEDxTg0u_nf73fMPKvJ7TjAuxvEq40w8_PCzIh0EsgHbNm1pBSx3TvDzTiiHVmrY7ur-d0zrm5pX4di_sH7at_ultdos6-hSPbCVZ5T10Ia1Gjfcc9XBVIoOhYD3QUnEAs0NMqIqixtBxbu6u97Mtvs5rArRoi4RqMwqop0R5RqOn8nnHMMHypttE62MCPcKoQ86LzoXzO28h4kaz6VzWMjp6vuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFqlfo1Zm9g26UMRGpUyPIUtgYbd0vrDxw8Rc9W8bAlimrxbKApJhZBFSdkDPd0jnTN4olwxIapW9AR_ChqA8Y_0f7LTpPgrG6xEuOzUQKLaJ0SBwKZn2YTxZYB7PKWHGWYMoVB7qpS0LuUvDXYB6rmzBzXoFu9fKXPQGvWFON4F6BV3zIYOMNmHsExEmGbgBCnwBaZwHNQCeHh4srV2HFU0bOTAkRarfIMh8bMpcwFQD5IDtCnHbWm_GD5dq0IXF-JzMmGwfTaDDhLJCaOKcNMmAGpuPEYBSuGU3W0rz4KK5MNpnOQcL31z-NTDXay0TNMCVf16YAtur8If0BrPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
وینیسیوس بدلیل حرکت غیر ورزشی حداقل ۲ جلسه از میادین محرومه و الکلاسیکو رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2fF7qzg3wr90iXD0VSNUIXqj2T8Ej-a4vLbB5hICcp9GLzuqcnFSbRFWVl3SuGaXXbN8PLAcWEZSHVRx0sjjohUvapy-DVGTUj8ggSJfO-fHcPL6Km0DSTc8Wd64MgN-c03xzGjP2-c_k-xdfRAg_G3NMIjY6UMCMNItmuAnpCNNtXI97AfI1SbJzj9SjMxMsfd54l04anaZl3nLhPsM36-eZEfz-W1gU1PwdgPqFuYEBA7COZw_wSP9lLs3e0_FZJKK6kt8K0Zk7Z_iH1gEgtKhpfnxiK9QIgs_x7D0YtNoAO69kFfiV3llVMSGcmUgGK00MCR1O1EhBjd53itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxA0d0Lb-XJYjCgFpHc1ZeHTIdWz4e-rrJicr8A7Bsa-nPJAqbEPYuNTDTlYOAJILeLcB2iEUpG_B-n-JFSIuMdShpi8pQZSdOIK7XNKKQH69diPhJUj1DroivfQi0IOZ6J1UcxuF_-Hdp3he7yGxyeYkOe41m8uq-tVhsPCWRD7ixxYdyliHjPQaGS1m4N0uHYSKlNuoajh0aa5MBlZZvHaBL6b9YWLUtLDsiZ16AWvTXV5uKy2SN6d7OO-JQy-p9VCv9qOiIL1OVlJoGNUHfUAb6sHIgjnT3ZGbACEbNFLPxb0yKL6BMmJixrCzqxU09Nt_G1I3kib6vZPgreeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYyLrKrh8jIeNqjdpNAWQx3DWPYA5MsDbA-534QOanDS4W9wsxe41WLTBqYEL1Xiq6BsjGFa72X4Jnsn0nIQ8ioHzCwIgsNDiSu_ttOLquZWArptyPRbaw5yzi0r_PKxOo-Ddi5YKmH1M6WvxMhavo6xuTmdAFbyD1zor_2lN5T8LEOKsd3NqNQyyb0WYfFQtDonxt2HN6gH-xEjeUTizZyRLGqn8oBh7YzO8xkev2iPLex7xRuHDIm9O5fUmgQhWHwejJ5S4TuuDnWYrh59y7SiymoAxDmnqUjiPGHHSarcIzhr1Yct5bH--9SEToLbRTZKLMwN-zTBGsbUZqIoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUmGqr--atrpfbWp2o0WYfFOZI4d4jDya18wMmetii-9JcM17ixs2F1hObT3xPZeRntkMdL4Tum3tBXKRuR6Mh1xnDRIY6geyLPo0QgfAF1E2ZkE7tmpNcI1cXO1tDAaSy-hpaHtMTOCZ1QQWfMNij64lyvlD9KvbA6CNUqqFGu8u-BnVlQc8hAe49n71Zb-A9JVzeXr6SKc9Zq_B7xjzHBgLMWHq8cpB96-0FDpa1jmX_kCbEgl4P0Vml2t4QU1rmGZwY_ocl0juTeTN1Ydfw6zWaTpww9yvKu3496WBHQY-nBS3u2BXzgaT5ofnpETcQZW_0zpwPPNpP1EduJ3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=ZX0NZzGEcDC7wHDT-YHu54QXN_gKCV9UnppYhS7BYNbECGyUQtm8XF6getHH8MDlOAAl1uqm1FGoRIymIMOkmlAafdl9cE1UQFXwHjI95v5kBgI3N0lKqQGb7UFMEeeADN9gKW6vkmwtoMXx0G_O3Y1-iRo55xAa4_ExRfjhzpUxeoyPBKt8-GTcyhizKbFBPctq69F0B0VVLq3v6zmGqqRQWcLiNzmLsC2StFgLkBc2oCE5L1gCkYXNxS7TdqzmScbO0MrxoAny62tOMHb8PcfyPHjy0issrNF7me9yNzt7p3EErGQzICg6bmGkgRhmIyC3vBFzeHfKi8RPjVm5jpUUsiFKwEXiWOjIkCTL-4qHLvIJeyXp1H-u8O-qrGF7Jvg-3K66qN6ojimcCHB9zT-tv5_7xpb1uUaVXqn6UB-sSDip5eygJTbzYXHDgCh3Li3Za7Dq8aAAPBhvn-FFIDlV_R7V66ciQBBlqge7TWsfuKQo7KFskAWaj87OemCQkODMJgB5ZeSxgDezdyEjZaJRlYftaH3SfQLVhfapqBKUM3riqOPFcsQPXORWL8z7T8w1C4kn2XKHQ7BfxxANtIjm2NV72a-z-fffhjtkRbD-cnkMwpoEFcASHsfEdaqCdLqo-B2PrnHieNK0aKXgQhfxtQT5ArlX9dsFitgZC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=ZX0NZzGEcDC7wHDT-YHu54QXN_gKCV9UnppYhS7BYNbECGyUQtm8XF6getHH8MDlOAAl1uqm1FGoRIymIMOkmlAafdl9cE1UQFXwHjI95v5kBgI3N0lKqQGb7UFMEeeADN9gKW6vkmwtoMXx0G_O3Y1-iRo55xAa4_ExRfjhzpUxeoyPBKt8-GTcyhizKbFBPctq69F0B0VVLq3v6zmGqqRQWcLiNzmLsC2StFgLkBc2oCE5L1gCkYXNxS7TdqzmScbO0MrxoAny62tOMHb8PcfyPHjy0issrNF7me9yNzt7p3EErGQzICg6bmGkgRhmIyC3vBFzeHfKi8RPjVm5jpUUsiFKwEXiWOjIkCTL-4qHLvIJeyXp1H-u8O-qrGF7Jvg-3K66qN6ojimcCHB9zT-tv5_7xpb1uUaVXqn6UB-sSDip5eygJTbzYXHDgCh3Li3Za7Dq8aAAPBhvn-FFIDlV_R7V66ciQBBlqge7TWsfuKQo7KFskAWaj87OemCQkODMJgB5ZeSxgDezdyEjZaJRlYftaH3SfQLVhfapqBKUM3riqOPFcsQPXORWL8z7T8w1C4kn2XKHQ7BfxxANtIjm2NV72a-z-fffhjtkRbD-cnkMwpoEFcASHsfEdaqCdLqo-B2PrnHieNK0aKXgQhfxtQT5ArlX9dsFitgZC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbH93B247I97-6tgp5O54Y3v9WdpdSJykeB3-7AhGss_4WYMoZkbWSrDoNPjafjX2UW1PHKXmBXh0dobchNyFRaaT_wlNfaUOvLg-8ShelgJFfGniiHOdpFyvza2V5mD1nJ3t8JGivweKOADDR_7um3iHGub0t6boAAdEOvzkKNfQIqAfVrUQs7ExwQHuy1M8nltD9D4sNUXxnpPrfdwpr07SU1R_p5AUc1Kl_mymEDoWZBeW6eOa1GGusxJmVmCDqXGA7lAqBhC3W9bRpZBbJtL-jX1bOm3aricjutm6yI0aeUVRjhzz17IoiI7-rLwlVq5_AU2uSA70I6GfNJ8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxrziPOsPQWr366XlHvLZ1pzVcLTRMYLx6IKSN7N0FcytCo3qeLuTEgwL285vgH2Jz5OuWU3WVUbW5n6AUoqKWcpbg3Y8imHMLaJNS7XQYRY4Pwf2y1DIWeS_SNSK98BMzaRlT3Z-JMDBmOvVhXxgXcd2WfWwsjnEZD6kPkSzKXczuQw5aBW6Neb0KwQ6TufYBTQDe8Ao3cY76T8WReU2X3IYf1JBTOGSO1529yLBRT-Q7kSFslkDogXFDIx3PYKaiUzMdY0IxnIAmuV24Pr1KuSmOhalrzVg-W_UGYYLrPcbnQURXLD8_Y93L9lsj2QEnQixG728-iiOpY9EtNNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس اخراج شد
😐
😐
😐
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=A59zq3u41YxlgDbmg5lujYGWZzd6hlcurFSeMCUgWAZhyWEvk0lo3BCvsn4MyZkckrzoPJ5KyRYfJtghOzT1lzCQF4zOieYNX4BcwOFgsI7I5-86sSMDLd1QTW3DSd_wpfBdMu0Oqqg-x_ACQyteEm53EE_9X84JDVvFA77c3-TOXzraN7RjhBMVBcqtupFIWtuG3FoAsKVOlU3HvuK7df23JGz-WJhrAHSZfZaaI5fLRa0EHNNjufEmVUjpPuQi_hVvzgmXVmk7tyh25FkNepHt7r_pXbIGUAd_8VKO3cVy_eI73owZFg0m_XtmApMrcfBXKGjNB-Ev_locPs9kMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=A59zq3u41YxlgDbmg5lujYGWZzd6hlcurFSeMCUgWAZhyWEvk0lo3BCvsn4MyZkckrzoPJ5KyRYfJtghOzT1lzCQF4zOieYNX4BcwOFgsI7I5-86sSMDLd1QTW3DSd_wpfBdMu0Oqqg-x_ACQyteEm53EE_9X84JDVvFA77c3-TOXzraN7RjhBMVBcqtupFIWtuG3FoAsKVOlU3HvuK7df23JGz-WJhrAHSZfZaaI5fLRa0EHNNjufEmVUjpPuQi_hVvzgmXVmk7tyh25FkNepHt7r_pXbIGUAd_8VKO3cVy_eI73owZFg0m_XtmApMrcfBXKGjNB-Ev_locPs9kMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
گل‌اول رئال‌مادرید به ویارئال توسط دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naMpOpRoreag3hi0O_WmGUHBXI3qtMgJHloJohMNyVK6kJZAvB9O_dOo6hToDquNEEkfkM-8ytcX1jRFAVV69liJLmdZi-envKPFXU23P3mhKM-edbLTPkGTerzi_lkbUV8A0ET_m_-55yuPluMVbA5RwXBXxYGrISPVm5wX04qdmlJ6q6h0n9o7ZNLvOFYzb5itGfgbg2m1ymGTCwRzrVPfDilzD3xmQPNY3CCSfFz3HQ7-P1dBNsg8j1fD154l3zUkI1EMPOS_vCD3IFz-MY3JfDEclLJxrXSvVmlKv2_o0G0f3YI40vm6dNbJXEPH8IU_Fmwx6VL4BdCY8Q5reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هشتم لالیگا؛ برتری قاطع و آسان در خانه؛ بدون حضور رافینیا هم برنده شدند
🇪🇸
بارسلونا
3️⃣
-
0️⃣
ختافه
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saqezsfJeujGglBHQweeecF1kjhShfKxY2J84xYtwDSbjM71F5TgmZBYqOCs_XG2usdvPMtj069t21ySXHrcfd37Oh8KOp3TdZteXOR30jNKrBFrFFhPsdEvjsEXwN0-yGIvJluCRXd-fFLmc8_MSByMKbj8N7SrRE6Lr0sBeskXMnWXTK5KuuNdMpccV1zT12jlUelINrwR4O32ddiQPkf5-_JIclY7A0wed-06P9WpmNCeixkJVkHYAjb3t1bM8ZVQIYqYjikSZUZWU02aqlpXMdbh0KRg0I1uUkyKYRdv8Ss3DUpU58-w0kVW_ehGrWiTA2NwcGmLTxBNyVJGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=Z40rANGP6Jt0aG6SOOHmzy9XBPLoIjHYKNa2rVdMyYAP58AZImZQYcbYtVDHKgjpMxr0o1sNK9B3NhBIebQ8w64Da9wKxoA-THH_13gfRs8JGLsHrVgZFfQmfIDByqPGvZ9wwTrNmK3pg0zUCj0oJy9jx3SFSEt5FtVEbt2G0bXZN8EL_yEWYj22O7WVwKTtus7HLFSlaaJmhwansmI3eQA2DvodmcIHxtRmqi3_M-m9A14KaemN2g9SoM-8NIH7EF64sE3su0JIEI2F4NZvw1YnggFO9YMs2Ad2lxoesTTky9mU-d_9CnZiHf9sxNRiT01hHQIvlAPduTHuwFQvlwLKzSrAQbjWLMiKvmeE3V66IdSIOqIH-4BIHp7obwYP8vdSxp9KA3Z0nQhHJk9_5vdrkp9FBtTfyo8mUdYpWXoylfyw1pUgTV4eqqbaQCROHuqEjiYK8fWTDEAceHiyuHLCsOLsVFLABSjiiDjoKbyz1jaNSJ5NLZsRnJHEPhDp7bz4w_5qKe3vo-k0lP2Dv82CCHCv7ZHtiYDbn77DcbFbUmDDqJFk9gEEuWuElJoF4iDQHqI0iFYsTh8PAPMv4LIn_OjOBtltvIo36DLandjweIpAWJnmoD3vGm593RKggCfqOIxPMAbE5d4nd8krWuPEl3qs7r1WGjpT_3_0nVM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=Z40rANGP6Jt0aG6SOOHmzy9XBPLoIjHYKNa2rVdMyYAP58AZImZQYcbYtVDHKgjpMxr0o1sNK9B3NhBIebQ8w64Da9wKxoA-THH_13gfRs8JGLsHrVgZFfQmfIDByqPGvZ9wwTrNmK3pg0zUCj0oJy9jx3SFSEt5FtVEbt2G0bXZN8EL_yEWYj22O7WVwKTtus7HLFSlaaJmhwansmI3eQA2DvodmcIHxtRmqi3_M-m9A14KaemN2g9SoM-8NIH7EF64sE3su0JIEI2F4NZvw1YnggFO9YMs2Ad2lxoesTTky9mU-d_9CnZiHf9sxNRiT01hHQIvlAPduTHuwFQvlwLKzSrAQbjWLMiKvmeE3V66IdSIOqIH-4BIHp7obwYP8vdSxp9KA3Z0nQhHJk9_5vdrkp9FBtTfyo8mUdYpWXoylfyw1pUgTV4eqqbaQCROHuqEjiYK8fWTDEAceHiyuHLCsOLsVFLABSjiiDjoKbyz1jaNSJ5NLZsRnJHEPhDp7bz4w_5qKe3vo-k0lP2Dv82CCHCv7ZHtiYDbn77DcbFbUmDDqJFk9gEEuWuElJoF4iDQHqI0iFYsTh8PAPMv4LIn_OjOBtltvIo36DLandjweIpAWJnmoD3vGm593RKggCfqOIxPMAbE5d4nd8krWuPEl3qs7r1WGjpT_3_0nVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به ختافه توسط کونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os1gE8e8EceZygJd_0K2FzmAlAP0HsdnnbAtHpTwuxIdngUPxyFbmmsW6cwlaPOiBcLrBSV0cTGzwWxn7ogEUBVelB8HGK290wlhaam6Sbl_Gs0_pC9dSFyOritTz6dBTrJQHOmbyuH804zTGZ_YZybrYhPffBx94Z59waqGsd3PK9_9iHd-AYwb2epE0MBMFtEBLIReI0v7reTt8bHQ56dJeII8oRcVgrjMDcNd56lGg0oyYi43BoCfbzq0_T69jWzxbu7YrHpCjgnp5GD4lK32u29QK-tl3WIGzz4A5Ep9-lVHhppXQjJ1yMniSv81fWCQFlgrZGYJnX1UK52TyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I17XG6pXHqltENdxFHWE4tZa1hSQm31_TSLfqtSggA2lgvvhyuIcI-F94HLwXr5KRDQIeWhBo_wQ5mDH2uiKJoCwcA4tvl1upZ-C10MqfgTD3NjEiCUhr-M5zFb1zJ4rlTfkTnzeXSi9OHsGPXw_VDnfu6682oo02owTTUm3F24vKNVYK0pUzzIPmny3Y7087m70kH35Mo35z6mQpWNEg1W3c5-yJCAjamOcKGk1o2et8-2toXexClyyapexmEGi92EKOsgDsmump9wo3PaDY69vLfIUUPBnbkIO6y4v9Fek8Bz3F02D_WC3-Wx1XtxTPei7Tht2UR-LhoqqGl91aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHn-N_BzWPxsqjc7YFnhNCLAPt5Jz577lr_tFmW2iJamKgr0v8lAbgKZccOPoJ0et2hG5dNlEpOmjfCYsaEj1U74wlXEe730aMVEfcJv9WWC9amkDETYQYbCLN5mpfCf_1gEhujBVbD0fppDT--a1d4GuWjS6tlJ_4QqJUniDmqWfkhuy04nV5RFw3zZr7lqy7uZAHfUJE90uXQRXcMmtqyDN5MRIWy4lBBmz6TjhBFK6is7OctTmoqbmX4WW3Am56waava0Ujz0XQWMor18lrbGbi4cRzmEtcgfYfmTxE9oMYGV74GpKn4SzXPRQ4MCbodbNpjBNGzYGWzmPR81AOx0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHn-N_BzWPxsqjc7YFnhNCLAPt5Jz577lr_tFmW2iJamKgr0v8lAbgKZccOPoJ0et2hG5dNlEpOmjfCYsaEj1U74wlXEe730aMVEfcJv9WWC9amkDETYQYbCLN5mpfCf_1gEhujBVbD0fppDT--a1d4GuWjS6tlJ_4QqJUniDmqWfkhuy04nV5RFw3zZr7lqy7uZAHfUJE90uXQRXcMmtqyDN5MRIWy4lBBmz6TjhBFK6is7OctTmoqbmX4WW3Am56waava0Ujz0XQWMor18lrbGbi4cRzmEtcgfYfmTxE9oMYGV74GpKn4SzXPRQ4MCbodbNpjBNGzYGWzmPR81AOx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=W0Rsso1hpLfDuFTRNEx4iL45s0BxYcBlEvipq6uiZBTa0fqo8U1CVRXP_-6fHbzxff_sbgauLMygAoRyVXgrVTmo6MsQz6sq0RF7-NSqcdvigxoAqmMviCesontfGqX3ZKeBFJ9J9whCXR_TZ5GQr6eR4Yj8p3qam6PcfU8mpy3wYprHK1RoZ5a2ZhDeTN5BfYbsGmDBxY05xAXZ1DMl51no7nrNav1_-fOvjVNK3MwX9MfyWkc74q0LhsVvbRJ2_s5MXoM4FsGBkRjGe2tFxzqlayWmgJDC_jM4ofFPyGJ7rdyHqXBe6UTUbQj4WPth8UMRHFhWGETZne-s3v7aLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=W0Rsso1hpLfDuFTRNEx4iL45s0BxYcBlEvipq6uiZBTa0fqo8U1CVRXP_-6fHbzxff_sbgauLMygAoRyVXgrVTmo6MsQz6sq0RF7-NSqcdvigxoAqmMviCesontfGqX3ZKeBFJ9J9whCXR_TZ5GQr6eR4Yj8p3qam6PcfU8mpy3wYprHK1RoZ5a2ZhDeTN5BfYbsGmDBxY05xAXZ1DMl51no7nrNav1_-fOvjVNK3MwX9MfyWkc74q0LhsVvbRJ2_s5MXoM4FsGBkRjGe2tFxzqlayWmgJDC_jM4ofFPyGJ7rdyHqXBe6UTUbQj4WPth8UMRHFhWGETZne-s3v7aLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=NtMPVok0Fp5oexfsbw8AEL8oh9tJUC-VDaaT_Y2xpIuQB6O2hGMQGpjqojQBDudujDlSx9rBD1oO9iglpUKnF9TmqLqR6w0ugWZfttlF36ENfIVR-v6tSR_Mc3ZLcR54vIaWNXBRr_xc5ZDifrWyF8sS5gSymCMrZDEiTpFwl4V1i9HLk68SXrkRtsfEQwFPKh8Xuqmalrq1lL9f7E8qhm5N0QbpezldOK9W-u76aNuyhPw-7QDgEzZ9vHA-zO308d54TL8R1qyG13ARveEclZKagUH1X68HLtQ40ekHxlSYOQaMGAcGp421YFlRgEFIMr0iEzNkT3SvWaCWzjsyoLE7QD4WhDAUpa09UXgI8K3GX5IoOSiLWS2FaJZz7o64E2LM3wlcb3LQwhhTI_nSpnLGtm334AG9YdLmNM8IODn-n-I3yxaRMeIBuHRhMqrV5fcly6bsFX01Yk5uRQ5HmPo64fbjJYEtySDde3hxXQAVhpJ3s5wje3q2xw3UYBS7vY-ZpsWhFaLyJVki8voio1yvl6ZQLW71dKygr4GtlUcANT9YyNEXLwq-BF_JgaD6GAhrFVkxkAexCOIcCV_n37QkY9WpldgbN4X4m1pxJhDGDNWXithWUqphJjszOUJndTdGYZUZk45gf08JS9XIa5Uc0yeTeNtW2NB9JtuUYHs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=NtMPVok0Fp5oexfsbw8AEL8oh9tJUC-VDaaT_Y2xpIuQB6O2hGMQGpjqojQBDudujDlSx9rBD1oO9iglpUKnF9TmqLqR6w0ugWZfttlF36ENfIVR-v6tSR_Mc3ZLcR54vIaWNXBRr_xc5ZDifrWyF8sS5gSymCMrZDEiTpFwl4V1i9HLk68SXrkRtsfEQwFPKh8Xuqmalrq1lL9f7E8qhm5N0QbpezldOK9W-u76aNuyhPw-7QDgEzZ9vHA-zO308d54TL8R1qyG13ARveEclZKagUH1X68HLtQ40ekHxlSYOQaMGAcGp421YFlRgEFIMr0iEzNkT3SvWaCWzjsyoLE7QD4WhDAUpa09UXgI8K3GX5IoOSiLWS2FaJZz7o64E2LM3wlcb3LQwhhTI_nSpnLGtm334AG9YdLmNM8IODn-n-I3yxaRMeIBuHRhMqrV5fcly6bsFX01Yk5uRQ5HmPo64fbjJYEtySDde3hxXQAVhpJ3s5wje3q2xw3UYBS7vY-ZpsWhFaLyJVki8voio1yvl6ZQLW71dKygr4GtlUcANT9YyNEXLwq-BF_JgaD6GAhrFVkxkAexCOIcCV_n37QkY9WpldgbN4X4m1pxJhDGDNWXithWUqphJjszOUJndTdGYZUZk45gf08JS9XIa5Uc0yeTeNtW2NB9JtuUYHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/326220841f.mp4?token=dVpB_hELW7ULODoKVmOk-UAeUaC6TVv1XDzcyVUSZqZ2upeBcg00Sf6oabGTjJlP7J2qcvHBS_Q2JsACF69bwOkFmm5mB1ioK2RCTityOBYa71qTHOB5xVnX7Ig0tol3NDVzrK2c2jelFtUuXwt0pl8NJhkqE8j31WH6IIhcwgdg0jbaf0USLAITxtw-hTYcRIILUMUWFdQu8b7AjW33-6lp5bSTj4HYJM1nQralI6a4br_pHZIdAJW6oRNLmoeb8xM96HXJykB5uWtt8uqWBZjiAI_dOe145UCzA9NzaTHve_Jc4898yqsiRZi2PfbwviBSSD4xLWhLPELsQYXFTJumHC_ZY5hWQLJnC9DdIILwButpXDIyA8bDXte8tm_oNdyUMzkHXv6OFSlnJox-PBZ36avi7KXMH9lJdTTJBcWj1oKeQdN0PJjucjrB0DBWGAg97a_e9ux0VMrLVCs7lvtrge9GdE3WVPnGjntmb5PedvOXm0QS-dgTqNrVQAsWn6UIDNxK-0jE2o9xikwD2JPnmgoPY5i-dOOKR7gN4JNJdwBA1J8vXwVbyaulGNqRVZqGh1issvqSyG94l2EkyIUyWTiQmxedMbBG7Xdu2pR0CDLbnKpP9D7NohyXS48IopMzXczkPOMj_TGEu_Y2Y8_SDr2snduiElmo12-AwA0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/326220841f.mp4?token=dVpB_hELW7ULODoKVmOk-UAeUaC6TVv1XDzcyVUSZqZ2upeBcg00Sf6oabGTjJlP7J2qcvHBS_Q2JsACF69bwOkFmm5mB1ioK2RCTityOBYa71qTHOB5xVnX7Ig0tol3NDVzrK2c2jelFtUuXwt0pl8NJhkqE8j31WH6IIhcwgdg0jbaf0USLAITxtw-hTYcRIILUMUWFdQu8b7AjW33-6lp5bSTj4HYJM1nQralI6a4br_pHZIdAJW6oRNLmoeb8xM96HXJykB5uWtt8uqWBZjiAI_dOe145UCzA9NzaTHve_Jc4898yqsiRZi2PfbwviBSSD4xLWhLPELsQYXFTJumHC_ZY5hWQLJnC9DdIILwButpXDIyA8bDXte8tm_oNdyUMzkHXv6OFSlnJox-PBZ36avi7KXMH9lJdTTJBcWj1oKeQdN0PJjucjrB0DBWGAg97a_e9ux0VMrLVCs7lvtrge9GdE3WVPnGjntmb5PedvOXm0QS-dgTqNrVQAsWn6UIDNxK-0jE2o9xikwD2JPnmgoPY5i-dOOKR7gN4JNJdwBA1J8vXwVbyaulGNqRVZqGh1issvqSyG94l2EkyIUyWTiQmxedMbBG7Xdu2pR0CDLbnKpP9D7NohyXS48IopMzXczkPOMj_TGEu_Y2Y8_SDr2snduiElmo12-AwA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
اتلتیکومادرید با این گل دقایق پایانی کوتی رومرو مقابل آلاوس دو بر یک برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=Jmqp4v9pyG-49YOwdY9Z470MKJ7tPNf2JdHrhraIgdn3maTrlEF6Yzsc0fnXiEwYa3_NfbwDR0deyZtpojw-Mbqv5cHIONVBZThGTjQtjdR-MP3x9Via7-XDXIPxp94InHi7AqpkVpPlOW16lL51Hz9NgKro8ZoIP_jiCF2AwmvWRX7ekfPLBDNloSxY0yeakU6UqS9R6qVVmtgDlHN-HmR78FAnh1zrCXV8hfLk_Airl5bw7uKoHXoYQA2YfaNOCcxSqfTRPSoVoq3Gf6_uvEaeQ6rn8LJAuI5cYMDNTpCAOYXXLlVq-u8tkbwW9W3NWkhLmNmzotHLLYqDFbWpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=Jmqp4v9pyG-49YOwdY9Z470MKJ7tPNf2JdHrhraIgdn3maTrlEF6Yzsc0fnXiEwYa3_NfbwDR0deyZtpojw-Mbqv5cHIONVBZThGTjQtjdR-MP3x9Via7-XDXIPxp94InHi7AqpkVpPlOW16lL51Hz9NgKro8ZoIP_jiCF2AwmvWRX7ekfPLBDNloSxY0yeakU6UqS9R6qVVmtgDlHN-HmR78FAnh1zrCXV8hfLk_Airl5bw7uKoHXoYQA2YfaNOCcxSqfTRPSoVoq3Gf6_uvEaeQ6rn8LJAuI5cYMDNTpCAOYXXLlVq-u8tkbwW9W3NWkhLmNmzotHLLYqDFbWpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل دیدنی و کاشته هندرسون بازیکن چلسی مقابل بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=PggX9NPGb14CZ5hiXbBRFomJpuKdTBS2ZbMBEMbq-lnzWLsKGMHPwjZ19rb1obrCDuF-4m2ZtfdOwjLniTVUxuOWPWB4fVZNgFVAI85t5wOr71hhsuwx8jqGw24dmxQuTDS-t9e210EULwv4vxvlNKT5irhEveLznJQeFrbSJik5mAOJPBuWrfZIH3x7gtQ2mAkiE1KhpxHgoV8DmDUILyVcQ3GD5fS7xJ89u9iFhTJYFy6kb86z3RHk1geVQtM6S6RkBXYwYWVtxqrSiPEoDRqrPvU8t7LVKLfhGKkTt87MLU3lHRzzPWMpuYvQysoNhfxnBs0NbDPWPHCWhCgT0wGGzAXRwpQ3nUyWR2eC7HeTtiRG3jBtU77HFQCA8LFCwIZ-b2PHGrGlCXl8OtgTnl163Nm7jPbF94hPdXvRzoSCMko1dZXQ8HlhhhEnbDjoMiNqVJGpLTB0AkNNRdtAkC_AhoVVOyhfAZJkABuKTHdvOqQncWE7bcuZQBXHGMntvBcO89oTkTd6lY30yFwAnIJaFFOwMWqWIXsGtYgez6Il0YEEPjkspBf8QmJGzCLy16Qjowgh9eURq8holZtsORK_2gy5OzL-eYnsyQummnK8ObwZBwrDFDZmZW6S-pznCWH0ihcghDe3cUeBIrJtT05086opmAoBsZGpecC92BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=PggX9NPGb14CZ5hiXbBRFomJpuKdTBS2ZbMBEMbq-lnzWLsKGMHPwjZ19rb1obrCDuF-4m2ZtfdOwjLniTVUxuOWPWB4fVZNgFVAI85t5wOr71hhsuwx8jqGw24dmxQuTDS-t9e210EULwv4vxvlNKT5irhEveLznJQeFrbSJik5mAOJPBuWrfZIH3x7gtQ2mAkiE1KhpxHgoV8DmDUILyVcQ3GD5fS7xJ89u9iFhTJYFy6kb86z3RHk1geVQtM6S6RkBXYwYWVtxqrSiPEoDRqrPvU8t7LVKLfhGKkTt87MLU3lHRzzPWMpuYvQysoNhfxnBs0NbDPWPHCWhCgT0wGGzAXRwpQ3nUyWR2eC7HeTtiRG3jBtU77HFQCA8LFCwIZ-b2PHGrGlCXl8OtgTnl163Nm7jPbF94hPdXvRzoSCMko1dZXQ8HlhhhEnbDjoMiNqVJGpLTB0AkNNRdtAkC_AhoVVOyhfAZJkABuKTHdvOqQncWE7bcuZQBXHGMntvBcO89oTkTd6lY30yFwAnIJaFFOwMWqWIXsGtYgez6Il0YEEPjkspBf8QmJGzCLy16Qjowgh9eURq8holZtsORK_2gy5OzL-eYnsyQummnK8ObwZBwrDFDZmZW6S-pznCWH0ihcghDe3cUeBIrJtT05086opmAoBsZGpecC92BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل های دیدار آگزبورگ دو - دو بایرن مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPYF9KlXo9wuwCOBuoAYKPfstz0hLvVnn1YiGlJh1udcRPXbfxsMQe_VNlbBoEh8pdo1C3E5_4vEmOHcOPxmHcdJh1_vxWYHPdVYnHdIaYkrjC7imuNzC-e8zadjb79aEydiPtILEqWP_D5by0Zr7F0KkMHdgpNqmrf1wJ4Q7mZnqdSDST4RwYcDWkAEfaKzRJisVIwulD-PTBrZr0w_h-uUZn_0dlCkFuXGMjYnvmRow-pNuShPkU_D6sDcL99LITyTnnF5jcdYZZA2XX9tUKpAS4vg8XdpvnIP88z-jH2KSNFeBe77ebh1zadmMNiyGX5XhNkei2-8Oo0Ch6FKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R06mekHDDQWB2zKfwPSCanulQJ6Pc18UPlm0ldLbtZOq60BtvE3mQvNmQRCx48WLT7VaUU7bjmY_6dOiUQYFeJvGa--dw2lyLDiUfQGYd-0_2xep7zo021oaP560P7DSJExIFss-VGPw1-cmq_g96SbYdWrx7F0Y9Q6O-W4A4RjTVj5KHjtllX5my4HilOCAzPAFPGWnbS5QZKUC5kgFw6LXzIzIxyLYZ5PvD243QNH1vCDALxiH-TAkMzeFz6ULZ680rUqmL9E2QO8itm5h-sZNVrknXfQgwXsaUkiGoOEf9GD6p_maLfUJxoMaKyBnTAIRvr2Qoa9HOgbR93RGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jT0R8rwzQM0TE_AwhWjXQ4nxur27Etyx4zJ-5iMpi6VtVJ65ValbxqCJ63z0_ycXhSxnnoHkG5UvOv_vOW-0MJ-qSLmxRQGYX7HqvmEb8H18TURflqpU6kVYj3uNvWzbJXdrE_0Iof1JtDA5qbdbnWFKCq3Xg3laMod6hPQdtUDQBJi-SNltDa1zYxh5FpXYqLlWNNAsv8y9IbQtAdwodnTOagoe4MV4CgmckKdrt8U0p-Ff6FTOvAgxuX_32ZBAm7sTerqdwYiUgJ01vW2UkH0hqvWH3JQZI4jaZ9GbzdGolwtsgtPA6Ks9Ui4wA2tMo4rr-8HfkA359yKtuFndFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4-h9jDvCdkWir0W1fqESHawGZ9pXpY3EuyBY5wqQiGLzLlrY-NEA8sXHc3POchGevpUlYWrFt3ljLdjhuWCkOKH81i86u7byepNq2GOSR6K0XwlWfcbFR8bLuuucDQ4C1tHuC8xzZYdf59_f0dO8072itHew3jgBASSd3eYSS3mgopcErOlMdMMIChRTcJxgBgG2iL68ldsZ_vmq4ZARy0zKKydlmabJzA7GgKl2A_HAa7sr11U-4rAho04YvFHYlG5XkgMUaO8K3DTTJKBIyhwehGnc66Fn3Fy_vv1qRJzlHMIJx09dC8ZOAkppb07Sqpi-NpXtydZG-jn8Z5WdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و منچستریونایتد؛
⏰
ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofnQkZ9fYqlpQ1UXZa-gBtuPyOllG1QX8y5dLZFC4umB2aSQIbH9P8TlYsd3gTB4RKk48IMOSAvzTH4_3k-pui8jqsZGC8dCpy0_TPK1My2eAgJxHhYrY9b3HSj7mTUN8YsNg_-Z8PzLK95tuswIm3toGLIvGEB8RHrLr-wMZlP1iJNBOCpTZw5BWlK2_ZmCXrNeitUF6frUy67yQtHZTB83sTm3H733FACKOgOnGAV-FtBAsCsnE0YpBWbZQRGAp7YfK4F1ILyNdPZCQ7xWapJY5h1iXdncuVKT4dtYPkdaGu2r4Se8OS-K08SgQGNKZ_toFMv8oHH08o4GaNosOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108267" target="_blank">📅 18:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5Fl4j_skui3pqhocmh3Nkf8drfV9kbu9yK7MdwBBWyLOP-AaCG_8MaQOERcnkobDWgXvMZh6AIYyGVnJtqB2lcM-as_Fj6tukrNsWRPR0HtU-p0WXs4U8OUOXsAu_7tQPEqZdTZ8XwhYC7JxdOoFF1GOh2oc-C1OxMD0SsMS9kc9_jhXHWcXeadeo0ANb_atAi1tSotA0q6DAIXA0g4hYFD4F8NZcswGKZ6VFoiegjo0s7Cwt5WtwYYjcjBPtZvK7TQQuQJ-ZE69148XOSoWPCyfam7IhN4kBb3ZxY0cR048lTLLDqUVHyZoRVjuQZX1EEawlZ01wpzInGSLUgVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
با تصمیم محمدرضا زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108266" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33630db290.mp4?token=Q4nuOPGsmo-PIQgyeLEmdvZSKWdn-lh8M8j-H2FjzLvS88I0qLVp4nSz-7zgJmMapS_jIWADcG_cW9SduzatF_Ffh7-WPM5xh-8Ae93HIJmRgmsHMPGB-fQe5-hRIF281d3tYRRP9YGBs8GnIlnGt-pyjJfmNzu-8UevbMkAr0EpzTEsxlJLxJihsiMbFIGjjXFqefvTL3QltnlBrMh4QRPzhjHmureQm-IbqtZCbADol7iGt1iRW_rKy1l_MQbAUkjQlrMtkdaL-fPVHHvcHPzfrwtnjqHHGBfNg-s0hjooMTbgCJXX-6KXD3DHuWuJredime-SCjqIuAWMpLqq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33630db290.mp4?token=Q4nuOPGsmo-PIQgyeLEmdvZSKWdn-lh8M8j-H2FjzLvS88I0qLVp4nSz-7zgJmMapS_jIWADcG_cW9SduzatF_Ffh7-WPM5xh-8Ae93HIJmRgmsHMPGB-fQe5-hRIF281d3tYRRP9YGBs8GnIlnGt-pyjJfmNzu-8UevbMkAr0EpzTEsxlJLxJihsiMbFIGjjXFqefvTL3QltnlBrMh4QRPzhjHmureQm-IbqtZCbADol7iGt1iRW_rKy1l_MQbAUkjQlrMtkdaL-fPVHHvcHPzfrwtnjqHHGBfNg-s0hjooMTbgCJXX-6KXD3DHuWuJredime-SCjqIuAWMpLqq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
سیلی ساکت‌الهامی سرمربی پیکان به بازیکن تیمش پس از سوت پایان نیمه‌اول با شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108265" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtVvxIQx-MA4IC3OnFry4zvoIZ7LFaJvgzjD7HmG5cNMWkNkJMVLwq0tsbPWFzbXNPESwTqxGA4C6brZ00BJwHDu9eHR7v2YDnpcZH5FBz8z1ANTwD0LHv2ZSuCTkgtrS5s8VBh4J7mBjWOFuPXncoSisscqeuly3rbJ5cLmpz4B_Lqde91C0L2DDAndelt1qwz5-PT7L_N6QzlzFnNg-LPeo62Fo1eTb_06_4KoZuywEHbjsNp7Fu3ZcuZXgTlq95GS4dEtMPxPatSjD1Y6bzkqAYJXmTrdZi9Cde87DYpjfWLZ11r2tSFjd4GrYEiYcLAzG47k99Ly8P6b7WTUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های بارسا و رئال تا قبل الکلاسیکو
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108264" target="_blank">📅 18:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=WNWz3MKhs0VFF_D-l6V0sd37LTAzFN-AE8_ujpHMcaLUSaKzSwcMW2Kv8r5hEvhDGJyvi7J-xufwIDuEZkl6m7KXD26FE3WzzPyWD3fZ5g6_yIB3mYNeI_mGZVlC-xBH8Wpt9SO4wkFc6bCJwh_9jm_YK6jD9sfkLOACQDfhfiUkezW32PHAJUd6o_g4sGR2-ntf46MJcLPKNLM5E9gVzfk3B8KE0qwnTaqEs-XA3i-MIgFeOHPtkl7RpmLuYr2ewLS5_jm0gAP9LLsDxNmJgU_zkhOF9I9BhftdLTrqWFMyurSYPdMm6sOt_GnELUcuFBcBdDNWwK8KXU2rIt3EZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=WNWz3MKhs0VFF_D-l6V0sd37LTAzFN-AE8_ujpHMcaLUSaKzSwcMW2Kv8r5hEvhDGJyvi7J-xufwIDuEZkl6m7KXD26FE3WzzPyWD3fZ5g6_yIB3mYNeI_mGZVlC-xBH8Wpt9SO4wkFc6bCJwh_9jm_YK6jD9sfkLOACQDfhfiUkezW32PHAJUd6o_g4sGR2-ntf46MJcLPKNLM5E9gVzfk3B8KE0qwnTaqEs-XA3i-MIgFeOHPtkl7RpmLuYr2ewLS5_jm0gAP9LLsDxNmJgU_zkhOF9I9BhftdLTrqWFMyurSYPdMm6sOt_GnELUcuFBcBdDNWwK8KXU2rIt3EZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
یامال نسخه ایرانی هم خوب داف میزنه زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108263" target="_blank">📅 17:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108260">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=PzmKRmOlddK6U-gf_0adP9HIlw7VJ4qz-4ZFKqRZbam4VCQYf0JTqINU9rchcnXBCeoqjI04-OezCHTU9N8D2mT0BIYvaIknaoFPy2DUiL8kKEPi9sai4IjlaBT-VFa7QPGPGB6C0c-VUrrAyu9catoAnxi-6X86GBYMl30K7nOxz5RMofMjvJuMP4JIELt1bVk4r5l8Dj-rwJHVzdApiDnXQ_J8p-Xi5jikc-1_AsK3ItyA90mtJds5HYmGhwiPZKPOJjPMDlqSp0jx2AanljubH4gXLzX70fEMCZPPsJpGOHfQXU3tUNJEtUi9oG0Kh5C155sKQ7zt9lTlmISNYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=PzmKRmOlddK6U-gf_0adP9HIlw7VJ4qz-4ZFKqRZbam4VCQYf0JTqINU9rchcnXBCeoqjI04-OezCHTU9N8D2mT0BIYvaIknaoFPy2DUiL8kKEPi9sai4IjlaBT-VFa7QPGPGB6C0c-VUrrAyu9catoAnxi-6X86GBYMl30K7nOxz5RMofMjvJuMP4JIELt1bVk4r5l8Dj-rwJHVzdApiDnXQ_J8p-Xi5jikc-1_AsK3ItyA90mtJds5HYmGhwiPZKPOJjPMDlqSp0jx2AanljubH4gXLzX70fEMCZPPsJpGOHfQXU3tUNJEtUi9oG0Kh5C155sKQ7zt9lTlmISNYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بخشی از دادگاه انقلابی امیرعباس هویدا که وایرال شده است :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108260" target="_blank">📅 17:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108259">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=vaPRJEJqMIDIcho-tmNEdPb7H5mbLpiGZ7MZze7vEKTYUNqF12xDbHFZGkTHNhdFyvPQ6rIG01sISCUPrJUBnH6ZiNZ3W6IxmN2xr30o5uxGzQV0UUDm1AYskXJ2h3JF5x9y48XAOv27Lp1D31PIQjtXAo-Sjl3djoqqdW1IzxL5Ybc_LBPSUGGLeUEEyciUpM6EzjjYqhfQsxXExIrF6ROov5CPQ9k53Yfxw06F31IJ86xyNdwYljFR0BOVs5ev9RzfN5fKhI3RKuEsS1_O6CtDxxa_bel501CFgxXSZtHrymu-8jo_nJAVj-nfHF2uhj_-2z1gz1h4QNb9GE3G4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=vaPRJEJqMIDIcho-tmNEdPb7H5mbLpiGZ7MZze7vEKTYUNqF12xDbHFZGkTHNhdFyvPQ6rIG01sISCUPrJUBnH6ZiNZ3W6IxmN2xr30o5uxGzQV0UUDm1AYskXJ2h3JF5x9y48XAOv27Lp1D31PIQjtXAo-Sjl3djoqqdW1IzxL5Ybc_LBPSUGGLeUEEyciUpM6EzjjYqhfQsxXExIrF6ROov5CPQ9k53Yfxw06F31IJ86xyNdwYljFR0BOVs5ev9RzfN5fKhI3RKuEsS1_O6CtDxxa_bel501CFgxXSZtHrymu-8jo_nJAVj-nfHF2uhj_-2z1gz1h4QNb9GE3G4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباه عجیب مانوئل نویر؛
گل آگزبورگ به بایرن مونیخ در ثانیه 5 بازی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108259" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108258">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
⚠️
‼️
‼️
⚠️
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108258" target="_blank">📅 17:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108257">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead49b429.mp4?token=XUQTVtFe-Rzuiq20DTfwDtQcKV69vT9qYAydzEEQOD9kAxrEpihe5BswboaampRm856AM6lilmHQ0DeABhK6HcQK8_qhz_8SwREV_YAq40ZfOoXuT8BNPpvEWZvMDtUgoNiID4cpuxru0qGgEMAl10TkuSQ1l256VxiiJjctp3qhAutLkGPNhihWNLIDXGJs_OaN4DxHTJ3hpqajGVPccNkYZq_8mh_6FeD9IGDZp6dSwQnBVpCoBV6NuPebnRKNEKvfqzmcOSDTUe8DEXI_UYEffEwZC8N98hkb56KRVqNNnp511Lq89FpMETD4qM35bd8mMUHPE8NfHXkHMPTT4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead49b429.mp4?token=XUQTVtFe-Rzuiq20DTfwDtQcKV69vT9qYAydzEEQOD9kAxrEpihe5BswboaampRm856AM6lilmHQ0DeABhK6HcQK8_qhz_8SwREV_YAq40ZfOoXuT8BNPpvEWZvMDtUgoNiID4cpuxru0qGgEMAl10TkuSQ1l256VxiiJjctp3qhAutLkGPNhihWNLIDXGJs_OaN4DxHTJ3hpqajGVPccNkYZq_8mh_6FeD9IGDZp6dSwQnBVpCoBV6NuPebnRKNEKvfqzmcOSDTUe8DEXI_UYEffEwZC8N98hkb56KRVqNNnp511Lq89FpMETD4qM35bd8mMUHPE8NfHXkHMPTT4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
امیرحسین صادقی پیشکسوت استقلال: علیرضا بیرانوند به استقلال برود، من دیگر هوادار این باشگاه نخواهم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108257" target="_blank">📅 16:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108256">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIAJeGBsl5FuFrbmIHuMiFww2wtnWUFr7JLTgMXZE1Y935z75W5vmJ-iUdQE8ZIeV_AwMAH-hRF7qvp9LcuNBsjwgXExa1pHMBohAb77NcAK2NqKAsGzQ2tAXB1Ar374ELan_KQgnQpSfBGGQWQUenyZ6d_iWP1ChweHQYjc9zg9XTSaVaU8RWptgJg-hoIVOhE_Y21bEP5dM-AfHIHjrWfOSoS8hp1racZALABU0O57gnHrvgBxVsl8-EUmUnPsReoXifkc0ms7IAPSnSz38yOaU7U5j5pu3lJn1ae5anttB4oSCgEZUL4w9FyGOq8E9Llrb_R8DDM5XToABepM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108256" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108255">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uE5tT9qWq3qj1RaqVl1cKbylynxLhHGP2h0kMdoICsEkyNJPhDa78k_6MTTwXUqz-NpeOKmNs077VH3Md6T4bN5jEGSAyYsmyXxh7FrRuJVSSBUVS5AzL8vrwgdsoe1KHowakyprqyjyMGa1ag9EApcPcL9q1GBXYjMrt_McdDZBGwWXi7As5h8bgS9bqp3XHWANF7reJt95FEmxKArtmZWAzYXbvvhBLKf0Sd4-pCwxiOI_XwnUlQIygq-8v7oTBpLVwrNQj_t5F4BpgZZecCVnE2jRDoN8TrftwAONfCsFa6J25bUjwRMyVE-lSmnOolR5C8YXnw7Kgti2EzkeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
کاروان استقلال لحظاتی‌پیش با پروازی مستقیم از تهران راهی دوحه شد. مدیران آبی‌ها در ساعات گذشته توانستند محاصره هوایی ایران را موقتا دور زده و مجوز مستقیم حضور در دوحه رو کسب کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108255" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
