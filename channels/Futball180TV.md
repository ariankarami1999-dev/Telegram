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
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 699K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-95915">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی رفت آب درنگ</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/95915" target="_blank">📅 23:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95914">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/95914" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95913">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5rDWRF6N1czeL1YNoteBcJDJteds1JVHb0s2NUuAhqxeIFrETkJh9PjLo3CBC5kqv_LnqLRV6L45vL949BSrJlUU7dPXI6PlaiSRjJ4Vd_jnKbRAxc-uWfPVv7qHBYIKNtQIr8wHs7OV3PSd3qlQQWhpa3WGQjR5v01TNQHbg5q-sEKDtXE0MjCJkUV3mx5_EQTr-S3e_olKJ05Uf-zEo4o36D81V7RHmLv178WLLnwhM4Fa0Lo5oTFeAA7uj7nfJ2e-if9vO5-BGSxrphScbq9gNMaZfc-etckuFHJBUs2x3spN66_S6JWpkEzUyTCe_Lav3ZleigYVVqmCJX2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو، ببین من خسته شدم نشستم. مردک یه بازیو از دست نمیده.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/95913" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95912">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsGwA5ukvsKqKK7lzsBhkXQsHoN_Is8EuH0UfazRpycWO3b0p5f-l04M0BIJpKA_7t92Qpcq9MLCvIUm2dsEaHn3t5hDKrggd3Na3ma4AyGwhu-tUg61F4pCl99bZkSToyqV4wFXWsIKsxTzjF8ICw9aVnevpOKbOK5zGAXTy1E-urZekw4etGLpQtedXb5O034epHPuDHxRCy7kCdLFjqzWEvVaTcceNgC__zIkOHG9Be4MM3jXVnc1CmT3UEB-7c7ol4WYK8OH-N8MWG7jSoaMWuq9XV3Zbvr67PvZ_gtRkuj1k3jCDNCVuQkmwacs0bQpEtf7mjk34xFw2_1nB8shU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsGwA5ukvsKqKK7lzsBhkXQsHoN_Is8EuH0UfazRpycWO3b0p5f-l04M0BIJpKA_7t92Qpcq9MLCvIUm2dsEaHn3t5hDKrggd3Na3ma4AyGwhu-tUg61F4pCl99bZkSToyqV4wFXWsIKsxTzjF8ICw9aVnevpOKbOK5zGAXTy1E-urZekw4etGLpQtedXb5O034epHPuDHxRCy7kCdLFjqzWEvVaTcceNgC__zIkOHG9Be4MM3jXVnc1CmT3UEB-7c7ol4WYK8OH-N8MWG7jSoaMWuq9XV3Zbvr67PvZ_gtRkuj1k3jCDNCVuQkmwacs0bQpEtf7mjk34xFw2_1nB8shU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇨
گل مساوی اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/95912" target="_blank">📅 23:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95911">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل اول ساحل عاج به کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/95911" target="_blank">📅 23:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95910">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گللللل مساوی اکوادور</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/95910" target="_blank">📅 23:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95909">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گللل ساحل عاج زد</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/95909" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95908">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=Ul2uvOkYQarPrfcnqOHuhmmp31trp8fuNbfGwbNT9KdzPuYVtdqruZuel3rLXiyqMCoDE4hjJp_qthC3eDTBmVRVmr2EJHtu8UG1TLnabFrNgdYP0aX7kM1XrXz1tO0sJLv_Td6GtFPrPyVUIeTcxGfWTUKbp8qmenuIisFRMr8AMnKOf9VEig00K4IOi9-G2nvcrH2DK1LAzoK4T5L-1jnJgZsM30teM4M3GcLHqtLDOjtQkNUweqHaEbZR1ZOH5PH0nWaVLKbKeWkp_3vzgTJz0Ht9c9NSRaUvUS21MRQc8UgJKAgMJ7d4QJRWWSF2qckWN_03fQn2f8EQPjhTTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=Ul2uvOkYQarPrfcnqOHuhmmp31trp8fuNbfGwbNT9KdzPuYVtdqruZuel3rLXiyqMCoDE4hjJp_qthC3eDTBmVRVmr2EJHtu8UG1TLnabFrNgdYP0aX7kM1XrXz1tO0sJLv_Td6GtFPrPyVUIeTcxGfWTUKbp8qmenuIisFRMr8AMnKOf9VEig00K4IOi9-G2nvcrH2DK1LAzoK4T5L-1jnJgZsM30teM4M3GcLHqtLDOjtQkNUweqHaEbZR1ZOH5PH0nWaVLKbKeWkp_3vzgTJz0Ht9c9NSRaUvUS21MRQc8UgJKAgMJ7d4QJRWWSF2qckWN_03fQn2f8EQPjhTTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/95908" target="_blank">📅 23:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سانههههههه</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/95907" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گللللل اول آلمان</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/95906" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بازیای گروه E شروع شددد
کوراسائو
🆚
ساحل عاج
آلمان
🆚
اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/95905" target="_blank">📅 23:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95903">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne--BQ4Srv30nferF-27kJJyAQ3i-qOFyuqFcZTaxZvhQWoKZRcMh_6-7K8Wx2425iAdu72ssbPoeFGN1B3VWS-T_KZ1_egFopDNvkMbyfcUtXAjit06j3ZIoDQNSqvZiol00uYSqwKw6LFHYuHwBroxNOl0xNCEk87uimWTNRnL4iBFgc17LwO2mn-NKmRDNCLryUMS7DUrkJyIs8Py3nC611u4G7e7RBwv-4DpQTxXcoQ7Tb-HjOkqFHGtQzcMbmn9lYrSWCq02YYcJA57hqKpqsFaU7aIzDUnLZ-CpGBXm0YqJB3ss9v3gypKOJX8TpNyXUIcjSXfkmJG9ZwHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_XqWE2W_6k-r5_n5E-Q4gMZjCclQZ2nNpSbEiT23wos_MgMQlaD-uES6T5f9T-GW1fLgQYO_-NGXO-iWwDi4RgTcluC8m_QLezerHJm_kmC3VCs1wxcuCGZQnsX_lOg-CLowl8jwRuSaiBhF_kbQFa7Cx7FBEtrxtHef3pSE_4RsU7lP7vTOnYz7Tvj1svnisg3j6GgJUCi0LSWW8bKr7jibmgwpGwE4MRji34Wk9H8A2okZKDow3mO1A8oyglFFWuW9TsqxfyU1_MRAPhGNCYhpfH8MGNB9pa64guj3xSXggv_dDm2JnLnbl7IzJaF9UlUgGlDeLHZTdN99JOfaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسی سر شوخیو با ژنرال باز کرد.🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/95903" target="_blank">📅 23:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95902">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=OZYwaLHdk6ZY7l5_n-6E9Vv7GyjKRHDdqgVOfSokP2T0XKwNu6HGgroLZn01oecobsZjJeVMQqyMMwXJIeUiukMFCvtGDLWAMx0mAGtSO6jjBYZMvTEE-2PzjtqQllo13OTCDjRc5Ipp7NDfeO2afYg2kRQlLzkViYJSXR3uhC87PBt3G0_m3TsaDzZLJmfW7VrsguBYmIDHnKbpCcVJDoQfjasMYyv8WDTMzOLMMeooxtccS1DRDUkowQDhIzGYKC2Ne5sC1DlE5RqAmMOyI9chtOQCaX3lak3PV0RQJBcSwQpRD2w6O2Mn2gAyPvOGBv3wT0sqrVe3NewrMSRVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=OZYwaLHdk6ZY7l5_n-6E9Vv7GyjKRHDdqgVOfSokP2T0XKwNu6HGgroLZn01oecobsZjJeVMQqyMMwXJIeUiukMFCvtGDLWAMx0mAGtSO6jjBYZMvTEE-2PzjtqQllo13OTCDjRc5Ipp7NDfeO2afYg2kRQlLzkViYJSXR3uhC87PBt3G0_m3TsaDzZLJmfW7VrsguBYmIDHnKbpCcVJDoQfjasMYyv8WDTMzOLMMeooxtccS1DRDUkowQDhIzGYKC2Ne5sC1DlE5RqAmMOyI9chtOQCaX3lak3PV0RQJBcSwQpRD2w6O2Mn2gAyPvOGBv3wT0sqrVe3NewrMSRVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلفظ اسم بازیکنای بارسا توسط داداش یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/95902" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95901">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bmpddHubQGbmWvSiBfOuTuiskeoLxigewiEbDJmesOuIWCbv0fcX4w7YYf36a9m08IgUh8DBekVTIFOQ0FMeukZdszabnvInBirzu6aw2rUDsTnPDHoYIdCBRWyfSbGfAk_w3FfZzfj-NczXyK3jwbsU7rSw0iADWO20YN-ftLxw1IIXL8g_Hc4xabVwJov1e9OX0Dr7e6oAq0-MdnT8Njet3zepvey-4reqo1yKgazU8DHCMaf1HvFpjuAtz2oqagsSjHtSChfhENNQATQpO-c7V94luSWSW-4ujdTx7J3PqacsM9PKf8Wa5qH5VSqv_xv6SiD18GMLgMf8Ctnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
رنکینگ آنلاین توپ طلای جام جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/95901" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95900">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSsWOBVijesOvZjUx3-NcQiyS2QsjatKISXztYvnTEliSQe1Fcci2wxc9A0_dCtb0I-EJ9_asI65tFYi5U46VtplHUr-Oci1vtTWGXgtPcKpRLLI40KvRUcMllqU4MMOrMelKXVPEWYRSsKy7fl5KsCoZvPMEiGEe4cUjUZSsvr375M-150qiRBTMM_selxb7Oh8fiw3NKZ8q9hR4P6qdwvSpGR3iD20mtP_xWCbkNwoLHq0U54f6VdvVEAaR0WgSgiKSng_tmOLVHmTkKbEGNiTNHvQwhpvSFVNZ7Uj37sjwOApKQOl5nzeq7JvzvOD7AS-eOEypvB7Kl8ELg5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو مسیر متفاوت پیش روی کریس و رفقا در صورت صدرنشینی گروه یا دوم شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/95900" target="_blank">📅 23:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYG_sW0NgG9BgsjoxlzZPKVtqNA3pw6UJVyC0LUCILhG0juKQTMrB-O0DVqP76tVnpBnlaP7jlMxAF8-cP-q6MyqSay5RosAAnwWUqoO-p-9_ftimV3CJz7KA-BkRysZJYBxMm3A5x8Ge9lJ-lfwN595so32U63zmMgDh_LwSguVLpCy1yGVrsKudNEnMDpnDD9lPerKVmDQg7XRVfSAlSUa6XyDbXNJzp3n1yq-LYiyINLK9nbxJD4V0qUnQQOav-VTIcFKL_TzEpnUiaVAyTdWX7zhvDgErxJoOF1RXix5YXT2ZVE-VqnbB9PjpolYCz76GOoZwCnbWACo1df3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEfz8CaqesyR2jpb7MOVbhwDgOMpBtxMJCMmXeUa5rnCrD3g5V9dBk2TOSo-JHmJuWYtpvt8EyfPgpifBuKxfACFtdfrBY6mo5Ksn3Lf0J2tNCqbbpAqhfHjiZOHHsfTbLD1MXIFAMdFLSHRi9K94fQFM9mHjA3ZnpdbUdAqIWYBHxyTj6yTb23HfsfQDvDz9qMehu12cYPAB4M_T1ToHTibDPIqyVYeXWdmzeKRT_v3r1QxUsiTJiDS68bCC5qt3R-eryCi_DJGiA966dcLgc5kCBS_Tv1rJk0awalyuwNZnpywRxiCfrg8NnlxAiakddrbNgJT8jXcadxBjRLN-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فرانک کسیه صد و پنجمین بازی خود را برای تیم ملی ساحل عاج انجام میدهد و با رکورد دیدیه دروگبا برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95898" target="_blank">📅 22:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZlQIBqvilv7AcZhFK62lnCJ1fKeHI3JUqMIvfNgRzWFbE4kInBQo1Z7lvHl5Pfv5h0Abt8EuKC2dtQoA5ztjOpdxYtOm1kndoyi4LUI4fNYL7Zygy6F_jaZVnAht9utd7CIKToCHIiY6I_ewzv7gELly_r_D_arSfXlyChBx8NTgT7rORxsSvdIrwr4U_Dnl7kehHPS3OPCWYa0n0j1RISIr04TR-TIf7oVT3VEOhaBy20Om71Y6iaONVHzTl8NizGHNesIbL6GDOKaw-mt7IVwdQQvVrGB3vUf1MUnTLZHM2ARO_pi8zM0CVIWqM20JQWA5nCjZLOE_FzJJv725A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کریم بنزما در حمایت از وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95897" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG6iHHmy7vAhQm6lOdWW8WQ4d0Vn7R-jHPyKV5CQe3c2QL4R0suaF8j-tIdNpwXEhTHSAzZ8MWKyNGNFeb35K6vktW4jeTg2m3ynJW2FHZ4xKWQW104d0Bsrvfgq_mr8-wJrbxbalf0MfcZ0Y01WMf-6ofFgMKpSozzp0M7Sbvj1QDV0UlwMnlrcOlfBJFAz2SiHmG3206rYTomXcElVBWpf0Z5jmjNh_OQ5zb3mUJj93McBAS3eSaCGkNn2-M5z_EnxjwlobzN2t9FhLQo_dZ6uBbpeQuLEXLl2xa6tVvG7YvXxWZN0LGrlz1L030x9_ymLqZkEYKFkLXoaJctLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMuiq_lMUzAE9XB-lI2tSf5sFVUqYZ6CvbVIDUH7Tx80Wi9Hd26MfuvlFCzCbD30D6QTB72XZ7JKOxNig1oEJ3ZSCs5IIh3ubnNkxLl08jXnVKNmt2A6vyznnS7-VWYKZWzXclo7uDb3XbyP5eQC4gjr2gTcNhPog3OQtYNjF8JtCStWmRcrE20iXfqQeRsUfeiwvz50WoJEoZSXzD15sfkinWFOtBo7k_3e3P7GGGOzXG1K_yR2j7KV4LH9_27kgi1Zr48X0FhIRkM3EVzZgRQejXNIPkiCYYqMoQriKOU8pSWmpJ8odeledncY2e5CtFXpxK8pOikdGP9p7VIi0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
😀
ترکیب رسمی آلمان و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95895" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAGrxH33gN6kZmNdALIfMiDbdBgrxNbV8ImBd9HczrW6RVXvN-chaSQ3tAbfVHapvPkGdc9iyEHwjDBfot0jNG_Ti8_Y-DLCIbTO32uj6pj2d5NlFTsdDeNy-oIjNP0g104dcAeG--JcVhuGuBcS3jaVEsurIqYNtftTP723CCezmr_MnOSNJpZfuJ79Hfsf4y3Ex8qWUsta4OymSrFMagsIJ0Lonkw3VgrzRCXNrw6PzUWirH1SAkTf__t9lv71ozgrwhYpU0ThCPcyR8OpJaZEINu4MPvrCxjwj2UaNCNrRs0uho2hO5NNyyErNloAstH6ESs_jJVuhQgxReAvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHRIO__0Sa1vmqeEcNklQQcFOg3JenOb-_3IHnPkywgZ1tCemHkAp3ZpBM1g_dlxbwCDBbMiFAyIw8OB7RzWbcD-X7y3cT89SHoQ20_lAqr-uAdVsD8rlcvK-njMhDLN0ybq8aWEU2Hf1qWmdGe6iOkeQxFa0Zp1AEXyAo1JyOkKjk0lC5TM5j0O9NOuxOXBe37T-Sq2hpUopm1obUjICDy3QHZ5CS7EKi83nfBA9sLTAjfdhfvp94C4FjyAt34XgSNaDr5cje5vNMTBcHTaSLzkqKOexhkfa6Foynddkl8wfzXdmGp766McGnsmXYmRUDZOR1uu6SS4aZ08KKI2Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب ساحل‌عاج و کوراسائو؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95893" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b5db1264.mp4?token=uFmEimg1xq9bIcT-Ei4crhAxiUu7J4P9xfBU3qmdyz_8lu7rpMJMJ89cXhe8REq0z1VvQOisrGdz4d7zy-KKKhV7nZ6pI7iFnnIoHLVcai1__8pC6aY2o7Nv1Emy4ZYJL7l2SR2HemT2iiByCo6KHUOkkSJZjn21ng1dEJ-JEKfiU7UerSzam96lnMgMg1bzB3Jg3HF4IHPIe0i8O_Pe9QXz_GbmIwHq9Kj9e81d_x3aNLCifUiZnIl49AL-t3ZYhbNfDMJsHwRs7GhAbf-i2D4NoXOIe2w5gUIAF0Yyk0KoaeeUnBr4aXFEyowsmCIWBO6VwoFnK6Sa-gOlThB5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b5db1264.mp4?token=uFmEimg1xq9bIcT-Ei4crhAxiUu7J4P9xfBU3qmdyz_8lu7rpMJMJ89cXhe8REq0z1VvQOisrGdz4d7zy-KKKhV7nZ6pI7iFnnIoHLVcai1__8pC6aY2o7Nv1Emy4ZYJL7l2SR2HemT2iiByCo6KHUOkkSJZjn21ng1dEJ-JEKfiU7UerSzam96lnMgMg1bzB3Jg3HF4IHPIe0i8O_Pe9QXz_GbmIwHq9Kj9e81d_x3aNLCifUiZnIl49AL-t3ZYhbNfDMJsHwRs7GhAbf-i2D4NoXOIe2w5gUIAF0Yyk0KoaeeUnBr4aXFEyowsmCIWBO6VwoFnK6Sa-gOlThB5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا لیونل مسی پنالتی‌زن خوبی نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95892" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98f8a62d4.mp4?token=WiTpkmytQ0lSvkzxayxmeWBb3yd3_2djuroYb0Oyca4RaVVAyKcYwmi1ODP4ID8wtiFkrCyTBu4S5MUf80VR61u-AwwGlDonTWxeHn1UjaPCu1KJ2-Hq3b7ss9LJdSE1R-boOC-psVh1GBPs64EA0g0B1jVm7OIRp0hYgNZyHSUNdoA7gUKZRjI3WWt9ZmypiyBMx9o3gwpmK-wZ6DahXJN2wQ49W55SvNJeZOlKjyYJ1AL_W8ZhP5lJc7VaG3FoDrRLoFEr2FjVhaagGYtctAW3A-K06ouYVHLnMZn3X38d8t7ZklYDlwG-47dnDPvlMeUGboDrJmc_OXjbThcSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98f8a62d4.mp4?token=WiTpkmytQ0lSvkzxayxmeWBb3yd3_2djuroYb0Oyca4RaVVAyKcYwmi1ODP4ID8wtiFkrCyTBu4S5MUf80VR61u-AwwGlDonTWxeHn1UjaPCu1KJ2-Hq3b7ss9LJdSE1R-boOC-psVh1GBPs64EA0g0B1jVm7OIRp0hYgNZyHSUNdoA7gUKZRjI3WWt9ZmypiyBMx9o3gwpmK-wZ6DahXJN2wQ49W55SvNJeZOlKjyYJ1AL_W8ZhP5lJc7VaG3FoDrRLoFEr2FjVhaagGYtctAW3A-K06ouYVHLnMZn3X38d8t7ZklYDlwG-47dnDPvlMeUGboDrJmc_OXjbThcSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دو تا فن مکزیک تو همین جام جهانی مطرح شدن و اخیرا کلی طرفدار پیدا کردن، البته دلیل طرفدار پیدا کردنشون هم خیلی واضح و بزرگ مشخصه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95891" target="_blank">📅 22:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای هلند قبل بازی با تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95890" target="_blank">📅 21:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqjoU5mNaSLH2MMAjIYEKyRvx-hn9Tcxb41ILGFdH5fJroFDtMy2VUHVaWcSwHpdxNcboetY4PN0rPpUOrRAKt9BPJXeYL6qA7rd91O1k6vF28bAJDbkg5pRJ1xWlsmnNMXJL1vNUeeHJQo3h5QUV9hXlhKa5C5_RG-V4mPWGaJZfU4625nQ58UmjSeu4A4Lo7Ix9cwC-a-pyVshYjrMeDAG3_EvTMPyXz0MjNQE-T3_0sCdMEpCCGPoA7VR_Xafzl9BBTmKQ_uLXnvayLqhbzDyqn9NUCv3bVAJU9aQEnWCoN3DuSCZPVXxfmfO0WOLklosQu2WtCMliIyjxCrgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇿
❌
پاتریک‌شیک مهاجم تیم‌ملی جمهوری‌چک بعد حذف از جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95889" target="_blank">📅 21:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCEfEZ305v2Aq_pT1mQK5UcWL13jDT9IooRG8BVXweqg0ClC-WYbhWnFqkh59TU3XOUTdTxLn8wqiSmRgzPI0YHZ3gqni-TO62mCTmYNt1iVUaDWrtlnQtOfNU-0RsqrDm7_7EDpuf4brycu9jOMEc0adGHHyqbFTi6i4VdU-CW6cd6do0AqCnTuP9NbdvPWtri7URWkDDP95ByIehbG5dy13NAp8BZYVwEY-Bi0pot-WDCzgdRoi43A0m-d6cvUBeIhRUitQq6gNyg_BhewzEiz_55fpur2YQPZ6eOAwr8hPjyCsJ8-cbRiTrbKqvPrqcpNh2fAwLjtyMFnj8b8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه هوادار به یامال کمربند قهرمانی WWE هدیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95888" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWgKeWviS23LM65DdQRr8BQjy674GM-2RjLAvLnHHre-aau3RCsa02HH2FfaVFZzMcqibTb110qfbVoAfi2YS0ZD4mwHUUaxFRy6D6EAEM4JbA6qF906m0kPB-QX-_vci6or5WCRDo-UytGxG-JXoxONCWycsY1-Jg3rQ5iHbMiJooVDdVxnFcDOmnP0-aNZFjkKzuaO0kCDWEZF4sKzx7ldGqOSIMaOQEeu2hIk3QohueGV0H8ISMQN8oPCt33VsWniqqq87cytQmTvcVYY10DpR0K3lAsspz-xsuaUNDJfD-oO7kUaRvdEWI4ZboerjoF8sCc1FUx6jYpIePMYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇨
🆚
🇩🇪
🗓️
۴ تیر
⏰
۲۳:۳۰
اکوادور
🆚
آلمان
📌
آلمانِ صعود کرده در نبرد مرگ و زندگی اکوادور؟
جایی که یک مدعی قدرتمند برای حفظ روند کامل پیروزی‌ها وارد میدان می‌شود و تیمی دیگر برای آخرین شانس صعود می‌جنگد.
⚽
🔥
آلمان، که با دو برد متوالی صعودش به مرحله بعد را قطعی کرده، حالا با خیالی آسوده اما با هدف قدرت‌نمایی وارد این مسابقه می‌شود تا جایگاه خود را به عنوان یکی از مدعیان اصلی تثبیت کند در مقابل
اکوادور، که با تنها یک امتیاز در وضعیت سختی قرار دارد، می‌داند این بازی حکم مرگ و زندگی دارد و برای زنده نگه داشتن امیدهای صعود، فقط یک گزینه دارد: پیروزی.
🚀
⚡️
آیا آلمان به روند بردهایش ادامه می‌دهد؟
یا اکوادور یکی از غافلگیری‌های بزرگ این گروه را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95887" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgwxl4j2nZwBbbNdqcZWmEguXMWP5sAwmOkB413oC5qNkl3YqAVsyfyF0Z5O6kFuQ-y2kvPFYM2Aq6yi6-JJsjmR1FS0xXtBubNe8oUjQe5k6k6StPyOMUsK3EvC_I1Yt_ydlnaiPK4xAXLxNulgKH6k1CJS6j0fJF0hM11jvS7rZBu12Nzjg0EVruBNRNxQ69BgrAHPzew4XXpVe-gbOjAxHH1TUI1yZG83oBjAG979c0N6IdPh4YYUALzJGZ45j3JOaPVkoOuXM6K4xWZ625T70iNWflWO6Gq8K21WuXLYe7uSq3daUIVYIQS6nY2j3BZJzuew40z49EAdlJ1Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
؛ با اعلام رومانو، ناتان براون مدافع چپ ۲۳ ساله فرانکفورت با عقد قراردادی به ارزش ۵۵ میلیون یورو به بایرن‌مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95886" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو: رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95885" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGOjF8lNzhAq07G1VqRlk1lox2SS_J4SN4UWko9IQMscK7wFIjSjEPoWcoRYLyQQOZmfPeKrWz_rEWQtiPl9yPWdwA2dyPW7Ni5uKxUHuIxppAb5lWPv8wXLxojI_4Ks9Kn8-SvE_5ds9lIQDiHWp4CdgA8R-vEHqHBlXdtzDZSAXcKThmdY0pmepgTEZiaAmqbyYcb_C8ctg6aecZ5APoxe7l73JpdmgSfc9qh1QlG49sMgo52T9wPlNLkjV5eKD721LBMfPGxNdG0FzzZ07TWm5SHIUZ7piLtFKSFyobCCUJR-fAk5pJkfxR5XHMajzIG_F_rilkbNFlgs5RlULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
ریو‌فردیناند: پس از درخشش وینیسیوس باید بگویم که بزرگترین خیانت دهه اخیر فرانس فوتبال، ندادن توپ‌طلا به وینی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95884" target="_blank">📅 21:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZiXiUHiYLgW3AR9bZQMvWwpVdOJqKdU6mcxjbDuqkY0zE4FTdZfc8SeZRqhZFsBvNvpfebV5SqvyLpJP0cOIJxyQ0GfoJ-tWq6k5NfGB9mY0nV1prW-EF73QJkJDWFXlhJoQGdN3bZd_7_q9EHIhwPzqXMW8oEUJhGqfSrWDrlX7z3QmaglQoXChF0G7XU-yOoNhllGu5Y6mZ1rGsv1eaTx_3grSXtzoQ-gXYepJI69sPFRKyefNF9gvoPbvj45yZNci6r5DOj-S0LQlXSPAjKIU_tmGjPLDzrDtjJdcGphDHRAQRpi11g_H2EmS70mTrxuaCfWm7dzK4Y7hAAH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
#فوووووری
؛ جام باشگاه‌های جهان از فصل ۲۰۲۹ با حضور ۴۸ تیم برگزار خواهد شد. بزودی فیفا درباره نحوه برگزاری مسابقات توضیح خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95883" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9cGoJZcmfMM-ilTt5bsfbHYPeLyuNmkx882XCeTck4QWKmm7GhsqbO3czWey_EFpbIsPVOozBdsD-VxKpB7e0UrkPVGKauqIdizT2a4QhXndcMYm6JJU4pq8MOFnHNaC-mi1L7e41om9MBsBZbQUAvE683eekFn3Tcb-tcX2lZP0r_Kt2gHP42iDG1THxuzJMkq-pzIoKZA__t6F40Hugi3zon5cgRS4A_FItPZgjLIgkosnBHauh3A-ltlg-iOPu776AAeY73KbuW_MOqFJ3bBXPCtsDOP6BHYee_XhsKCW-HUU89Zwxj_SA_gJHg2iLUz-XcmBi5W17RKphBDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو تو استادیومای آمریکا میدن 13 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95882" target="_blank">📅 20:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh0kfApbsBX54tMacqXNKkzDN-qub1rkX6d2JZM16E4Ahuxbt9unhAFYUDWvEBbZ6MeR7GoiQQCY96kZGEDiv8dliMD2sdfxy30nbjx9AdI_5lyMzfBiUsJ-0uGjDqGNvIrLCxYkt4ITRHq1L_D3EByDGLmywdQSuecXiuFBcrN-lXG5UgQtditoTmZPsXd37ncvkwoItjjaZvPHmdu4KMFQIlcGk2fiOS9spmTIagGXguBWOq4DvP7irQGyfA9Q4W2whuFU4JktvNjFDLbCc1ga3H5TS7OCc_M54tk8IcR6z6doh-T5DJOhyO8F2DbE0omgHgcCCYfOtPmH7u_N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
مارک‌کوکوریا:
دلیل عصبانیت هواداران بارسا برای من مهم نیست. واقعیت اینه بارسا به من پیشنهادی نداد اما دو تیم مادریدی خواهان من بودن و ترجیح دادم به پرافتخارترین تیم تاریخ فوتبال یعنی رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95881" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh6UjU5wS3Den-6J5RcuszJpkpFjZ3RSPyzqlldHWfXCOGPZRVN6wYl-Ez4E1eoAGjAoY6SoE-oEN4ut-FVlygxqQ7OJN0ScOBU_mYdq6IVr6Ax1hrOs5FPE_ujJpbyTFmibGkKUG7EMfyI1pEHaNbipXSpv0dxTyGvzaKiOpUl28pgFtjMhmOYECN7SNwtp1xixU21giQG5MkiAWtv2EoGoHzKCvh3LTQ6UuCkeZ65WyenuWGdCeWtJlLZZzbdHWgRfJ0OZTNKt0ZTupnsuZH-uH4a9XJLwNxu3Aurgyjx_q1jkLEezVcZt8q0Lxb_zj3xmZl0TAxzl11Cf6bBASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
🏆
بازیکنان برزیلی تاریخ که در مرحله گروهی هر سه بازی جام‌جهانی را گلزنی کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95880" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPWMgLUYO1czdDF7H-DhYyVIbnDFztDPBUO2fZ4dpUo8pTW2BZN7fS2uWt0t04mxUdg_SqaEHFRCRNmo0z9GMiV-hO9lrOMDb8-3ETcpqfCOSq40ijoyU06Rx5Us-bE4eP9JFUJ_HAh9XvD7NpiTN08EyC3xy7irVfEGyyABZ5DPw39KC6MV-gRGGXRimm0gdtuTViT0ZWouZM2ZCTo0-jmw7V5SUOWGKJqowR90bOzq1QxetM3n6YCYtjprmWKD4XdfrJiXVEGRsRRayeUFBuyai_sgMqv1pkZAYHP79mjoRdG8A1KJd4k1wYheoOh8V9K1xcFiTRa2nMNrC46_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
پیام رئیس فیفا اینفانتینو:
دیدن تو که فوتبال بازی می‌کنی همیشه یکی از بزرگ‌ترین امتیازات این ورزش بوده است، لیونل مسی عزیز.
در زمین بازی، تو غیرممکن را ممکن می‌کنی و باعث می‌شوی کل جهان برای تحسین استعدادت متحد شود.
برای تو یک آغوش گرم می‌فرستم. ممنونم برای همه چیزهایی که انجام دادی تا فوتبال محبوب‌ترین ورزش روی کره زمین شود.
😊
برای تو تولدی شاد و موفقیت‌های بیشتر در یکی از آخرین بازی‌های مرحله گروهی این جام جهانی آرزو می‌کنم، جایی که با تیم ملی‌ات از عنوان قهرمانی که چهار سال پیش در قطر کسب کردی دفاع خواهی کرد.
تو هنوز هم شور فوتبال را به میلیون‌ها نفر در سراسر جهان منتقل می‌کنی، همان‌طور که هیچ‌کس جز تو نمی‌داند چگونه این کار را انجام دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95879" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/95878" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npymefwXRHhEpXtky6It67PhmS_3iMFPlqfCWh-eMf5oa2V_D1MArlz16rHdwfzjrVSPNTBcIrotSy1F9ljteIOOswRnr78HBk9vwES2G7eqUDQqHX4XnaqbdvVBIfbNmLKmmS1psfyFrcVxBZTz-DKN2yQX2T1KFOuC5suKjtJD3du_p4j71pyrGvnKuIc6PeWoFlUc43p7NY5pIfKKdyUbvm0t2LTIzNKbLNzhmIg148sqTi-6cVOYJaZU-wMjYp80ACWF5sUG8LM8uyj9NL0gifLGj8M2b6BRAS3_QomERs8Q0gDhh31AgWsuvlV-ia1lVvOFy5Ey46MP6wrgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95877" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB_Xw2KOaFruWOXrTwVA8h5Rgh_oe8xNkq3aXLI5eD4wWFHPJJ0yv1pMxiRpBdQPDorEwlg3OiydxB-hNAxLuIHOA8zUgXSjt4q-PikibIXcImK6TdSF-PvMu3pi0rw9fEelDfuNgdrPPMYv-e1Z6y635phInSF_dYQ4lMA9yBG-DF7cHyTNaSsVs75kSz2D_k884HdXAJk8mAjsx1YBHqa8bAQJxvoy_6MI-Ez3M7OCC2GgqUKjjrmDQqNW70IR-lvjL_iegaTVdlOHDa7HeRVzRuOQ6s49Y2RHe2mfs8_TmtWvOk-VE2j3SsntYmDq97Tmu2f7SGK98P6seGY8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95876" target="_blank">📅 20:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2N3iTBmif0u3McmfeSgayKaWlLSGwUqro5Mwp6jpLcmoHWIFaBMyXoy7ZWVGX1MNT220qkTyhPA-sXaz8j99AOicKEPmT4yYum-lsZ18hkfCsWgnQCUtxXI3hH1cgiV2rf2SiG2c2h2InF6zslLWnKog_QOevz9X5ibzBdi3IR2bvW3_-ODusMb2KnJCBJspKwZxuZWDD0-iq6pdHwPc3LzmQfODwZdNer_PbU1PXNAu1iLgZ55rVYYZanZRKVOOPKxlg018E8ttcXn6ORZ4yTbbowJaJyeimATWzTeL9czqUD8Qj23VJq3NKNJHo2h-mcaZ6GrkRgYEaHvM4LYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95875" target="_blank">📅 20:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇻🇪
ویدیویی هولناک از لحظات اولیه زمین لرزه شدید روز گذشته در ونزوئلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95874" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d7deda96.mp4?token=jJ2shahcTYwNOnRkKacQrA5_7AwvKvTTBkarYNVdaC3C-avNSGfGAr8LYvzaGVu9ec1QM2PbCmYfjOiARh2vE863ttKsE48pWczNULvjNlStfXXRjb1j-lC9BIM1n7rhP_ip8Wqip4VSNcxaho4y0HlJ47rWSjlueLhNB0CEtFQk1a867AAiEPv0ftGaw7_aCuYYK76Hka1CZZnkGCZ3gsAf0PdwCFNGKZfN12UYVK5obt5Vd6SR6xLenabLwpBEBH0018-zmHCwEdxQ3cnu_xaX3HvjO4peDLKSXr7YBWevO251AB2NO4jVqzZKQwjbJFnuX4DkX2qAs82lSHjzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d7deda96.mp4?token=jJ2shahcTYwNOnRkKacQrA5_7AwvKvTTBkarYNVdaC3C-avNSGfGAr8LYvzaGVu9ec1QM2PbCmYfjOiARh2vE863ttKsE48pWczNULvjNlStfXXRjb1j-lC9BIM1n7rhP_ip8Wqip4VSNcxaho4y0HlJ47rWSjlueLhNB0CEtFQk1a867AAiEPv0ftGaw7_aCuYYK76Hka1CZZnkGCZ3gsAf0PdwCFNGKZfN12UYVK5obt5Vd6SR6xLenabLwpBEBH0018-zmHCwEdxQ3cnu_xaX3HvjO4peDLKSXr7YBWevO251AB2NO4jVqzZKQwjbJFnuX4DkX2qAs82lSHjzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در نهایت چیزی که پسرا از زندگی میخوان..
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95873" target="_blank">📅 20:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWjF9Dr40tUCiUw5-6wvGkQqI2_reAje8P5tcu1-ZMq-eW3X5qWCkCmURtsgZbyUzDFl_El27rCYBQTjMsXcCvurp6Z_elaRHFd0Xf-w5LwhfHkOnXe0M3Q-9u1NbxX7WSNZ-uq6h9txWCU-43mFHWbxCkaZkNAtmHddf3f4pr1E9dsPEk6KFgyRoDbx-P65Yq5RYf1mIo-WcsfiZWUoao6tM8gcgJtXooANMra31pTJ-5ZuLGr1RZNaluQmv1tQZU2OQ5P3dZI46hZ5BOBoChiGQVP8_JLpYX178Tzt73pWV2EkweICE3uxJf0U45Xwbc7lMveXRAUfLEMQnQDBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
همجنس‌گرایان دوباره جنجالی شد
‏
📢
🇪🇬
🇮🇷
گزارش‌های «نیویورک تایمز» و «RMC Sport» از تجدید بحران پیش از دیدار حساس مصر و منتخب ایران در جام جهانی ۲۰۲۶ خبر دادند، پس از اینکه این دیدار قبلاً به عنوان «بازی افتخار» برای حمایت از همجنس‌گرایان در سراسر جهان معرفی شده بود.
ایران درخواست رسمی به فیفا داده است تا «هرگونه جشن یا فعالیت تبلیغاتی» مربوط به این گروه در طول بازی ممنوع شود و تأکید کرده که فدراسیون فوتبال ایران این موضوع را بسیار جدی می‌گیرد و از موضع خود کوتاه نخواهد آمد.
‏یک مسئول در فدراسیون فوتبال مصر نیز به شدت با این نمایش‌ها مخالفت کرده و گفته است: «ما کاملاً با ایده برگزاری هرگونه جشن یا نمایش مرتبط با این موضوع در دیدار مصر و ایران مخالفت کردیم و از فیفا خواستیم که هیچ چیزی مرتبط با این موضوع در زمین بازی وجود نداشته باشد.»
‏او افزود: «ما موضع خود را به طور قاطعانه تجدید کردیم و تأکید کردیم که بازی باید فقط در چارچوب ورزشی باقی بماند و هیچ پیام یا نمایش خارج از این چارچوب وارد نشود.»
‏در مقابل، فیفا بر موضع خود پافشاری می‌کند و تأکید دارد که برافراشتن پرچم رنگین‌کمان و شعارهای تبلیغاتی در تمام ورزشگاه‌های جام جهانی بدون استثنا مجاز است.
‏لازم به ذکر است که پیش از قرعه‌کشی جام جهانی، زمان این بازی به طور خاص انتخاب شده بود تا این رویداد باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95872" target="_blank">📅 20:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChFB4dfGfjKmYFI9WgVg15m59XZ0bWJhG2-JZcpHrVwXwxwlZABJOeu9C3KDLpb5pJuS23ZAqcsuvPwCHwG0bpCWuYGjhuYzU2QC-EH2yo8E47kFRDyvkvUtBgl6IZIf-INTdinUg0gFr8z2tJrlUPQmPQoQpMUGn199V2AODmPJWS6CN2Y44h1XUMfXkDcLyND7VMQL58qYqd-Coge57-D5lotDobSbvNzevV-j4ZKIXp48jbbhJ2c0KlPQbUlw1tXoNLxURbsvrebML9Mf_3GK4KmquMs7y8pF7qmXb1_IvO0wg79kFbNnhf9t8NmTIsXU6mVzaXyeJFsNJX4lfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
در جام جهانی منتظر چه چیزی هستید؟
🎙
ژوزه مورینیو:
دوست دارم بازیکنان رئال مادرید حذف شوند، چون می‌خواهم هرچه زودتر برگردند و در تمرینات پیش‌فصل تیم برای فصل جدید شرکت کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/95871" target="_blank">📅 20:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBvuBE5xlZA0oFNe2ncLyBKV1cdPPVntISL62nvs39gjz2dO8FXq4RYvE7dkOb_vMts-er0cpCc37E6YYLyys17qWtsHizqgV5sozynm076rFg1LBh0nv7LGbyFp3ZWgfubhh6BPe0y9NdC0uVFeMqSPBPhPMS8SRodYm27E-dNu8ogLqo7RlUgOZgwUf-CuyW2GB06O_AI0pNrXfKvga_ImHPPzKy5t_dnDKkI0A0PbWNj7MO5-LfHKCP-EM8phMezaZn3RvdFa42Y275jQ8gGhM0n_9wg64TN8BL9dSKHfFuJtvDeDQdGK6pCEhC2dSBXNOwnlsyvOIf1ArumuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
با اعلام باشگاه فوکوشیما یونایتد، کازویوشی میورای 59 ساله یک سال دیگه باهاشون تمدید کرده و بعد 42 فصل فوتبال بازی کردن هنوز قرار نیست بیخیال فوتبال بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95870" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">والیبال دو ست فعلا از آمریکا عقبیم!
🇮🇷
ایران
🔢
-
🔢
آمریکا
🇺🇸
🇮🇷
23 | 20
🇺🇸
25 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95869" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95868" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbpdyd1ZStvEbradlzBjjtkO0nBBUENfF-3uINlbLccVnSfRXbINhKYC5pYY6BGsJ_MJ43BRubzJrAqfBxLh3IHOG1Fk778Ylc61X_CBW0lr9xVvEbUDQKywAkT7jfJ2WzuSme3ljhxqapLQaYxbe6QiIbOtnY_a-D7gBperOu1evun59djq3iOLTRA4bwUk_uiQcHTwq6GeBbkkk7lvWJ5K5XCkZNebL7gphbOzkLMsVd0zVsgP7sW3bE3rcd9wnefiV3z6CPHKgpuyPFssFLyXn0j_waqc4pxLh2raO5TXvutfLZKDm_TWZP6xwMIgLkUqJN5WbmbWgTCuFIkM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95867" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWQTf9X1nhQ5hqVaPweaYdtNqvs6R_DCc7twag-CQIUL_h17jo6PjhQNqQe3Kve7dpLh1yWnkaTSmu918QYNa4J_dNxK5zrlN321s56QzYQ0xzh-QW2kSS6IHpYhHWZ8-sI64NDZhIFw97_Oi6T5lSCE8XzCDg7y1A-zb4pxQbRBF9w0LfFj4Fp-tXGGMk8c0sPuPgdnEcnTuiG5ULL9eESchT3qTEg3ZdpFs_daQEx_zoljRiDU3duqHlye5eFH9PSRPX7pP8VuuLb3a7M73JZWCRUintWu8IFu3CLLNx2jYRu9JAU-uwgu8WabdRQHTifv_lMzHxPGv9DDd5InEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آندره اونانا با یک قرارداد قرضی 1 ساله مجددا به ترابزون اسپور ترکیه پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95866" target="_blank">📅 19:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHEm2fdyKifcuAZt1vNqD0pBh79oUaPCADGjD3F6R3rLwdvscpXlqmW2iYbCPdN1Dz6Q7iWyjFf4sb9lCdBkelQsV1FokdeP7FHJIWIBlT8TuvLaZPsEWbvXnaFRCquuex6f0m4OuuUDFZtbYqWyKbF7eg8QQAubXpBB7XGA8x7BjFWvnEBapc4INzIqSPkq7zJol-f7njjj5HniAbffFedVQ5_QGZGNUuJSv4XTJgPFk2m_QqvN-QnWDjmHiapLMCdQVbTRMFGcMFNAGS6nP_5oaQZHXPTGal9wXbSUugZvTgIKTOV87aqLhl2Ml0QWhtSd8DSpUcaPF9enB9aVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: «میم‌های توییتری خودت با اندریک رو دیدی؟»
🇧🇷
آنچلوتی: «بله، خیلی خنده‌دار است»
🎙
خبرنگار: «خب پس اندریک در ترکیب اصلی خواهد بود؟»
🇧🇷
آنچلوتی: «کی؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95865" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95864" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTGFNfrMyj8Ft821oLW4NJ_3C3EQBsXRiJeXwn8mCMVLgmiIsZK5uS8bR9rw7pCpvaZbsO2yr1_0bx28s8z7Qhr3Abksuf1n1q3JRhGYaYM3GUd0hvlfT1vqIIgqNMX6osBQ6X1dSu3c9vicMl7uUhUnENGmKJPzfaJoriJrsXhWMICKTFrDrIPvsZyOkOFOdRNikY3pTkw4b-70WzlquQngWJFlLgNTlZ4OEiAPTs2M_Xq3mlQza65eoXf5_Taiog09lGiEQ7zow7xlEAFNSFi0MuTYfaHAVjbgiRP2pCsc1Lkw2GQp-hKp1NPhcnYLzHpjNUb6iPGoMcqNg6iD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو:
رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95863" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbBMvDABdciw9EWnZ7Ol7aVgNbmL0kTnXK3-KzRoGl4RSunu_6Cnq6P-iLgkCoVVt0_fnnqrWe1QpRAgDD_queIrQ78N1eMwJgIH94Z-tL-8yQ1Tndp_39ElZLgZeKh2AACvV3D4wCuOS0M7cntgBmv24mjYUQincSsRlNfFb-8y0KbyeC7nH1CB9iTOmWsxJIyqTNkpTmIM7QQec9FfW_jD-yI5Y6HSH1BaqOo7gAz0wJ0waUcskdU-8QqBNnufP_DxfYLOjH-i2n4ATh6WpxC_8hb10VsjlINLoHyIQg4pv-kQA4Q40IvZbibHSmurKsT1XAl7c6kRfSmY_2bVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmroZanE3ZfDElKtOxJbR5cCKH910EwLy9rWHjd3trdZ2Zcucr0dmabxcOOwHZkgIxLHDEa7we9xOsAX6lhf5iN07pfQiT-j8Rk5B4lvkY11nWF0Un9FAr8h0fTiR06ZBqCtmDNMm5krVdhBHsTmA829hiJ2XA3WxTjBzZX9dUZmrAU0cl4wthxWYNwdBcaOe4yaTfpiGdNikiIuuV3UHuZ5u4YjiKvGyzXYkU-lmNbb60C3bLjcCIRz_SJK4UuDJ0cMcylFJt4NEL-65vO1pD-XN8upyfo4kxPG2gQKHwbaIKurMkzBKhguBvhZOR8Niw3ZNLlSVO4M36r6vmfIPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی) : من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95861" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل‌کل دیشب هوادار هائیتی و مراکش
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95860" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عادی‌ترین هوادار تیم‌ملی غنا در جام‌جهانی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95859" target="_blank">📅 18:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUUwSc0bFVb9Ix2pB1hEQztC4doHMhKRzgFZQHIYcbrskR0iZPIoqS3hkjvStOk_XtjUzGniJt6oYsQOLLQ6IcnKWp330rIq-mjLv0s5z8fe0dXPJ8P6mO-XaiQQsYhbraMriwaocX7ucGyXnjsLI7d0Zpnarp3ryH7ZCIqpdDbLe1k8pKdI0EQ-XY3zFC4uEoDykZBd6OOW3WzcqpK6Fuv-OsondDNat_29tQTJuVucOdW5auycWDahrRJ1GPsk1pSDZevwDZ6hAX1pnIr4KRUMvg-tA9uqfpyKZ8d3GKGpOamlEF7-GaTQ5eaz2zKvFu_GmXdrZ92zNhM6tFtOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو به همراه بانو جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95858" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp1E4zN8Isr1eZMSYoaNv_cXzseT_kjsansw1P6K86QqPe8SgbR-ViN8m4M5rfA5JPYqz0oqLjXPA_Pn-lcMrYxDtktjqjXf66LRymZAIpeNDtf6ValAcmb38wE0JyXce3J8SDmjyxwaXH0MR850y64HFlw8jqPvXhcCpVHdHOqD0fdpbemfdZtDw3xn2zGIK6gPjcu7IYKGXGvp13vlPmFRqH6MUDia93BOpa9qdy5VnybpTdPTg0JOK7MZ76yy4MRBdUIeP4uqaAfJTrS0wrFpzFrT2NXMtv2SWxgv1NgkekCd7nRKSnCTxVjzy5legqg1tcXwC2v2QQtwcziRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تبریک تولد مسی توسط اینفانتینو:
تولدت مبارک لیونل، تو با استعدادت مردم دنیا رو عاشق فوتبال کردی، ممنونیم برای همه چیز؛ امیدوارم در جام جهانی هم موفق باشی و همچنان الهام‌بخش میلیون‌ها نفر بمونی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95857" target="_blank">📅 17:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQrT7PmfWkWDzdXBXbFl_Ze6wNpb7MkBmveKu-S8OVXKzvLWstGLw4Y3hznp31u2YLhvIsHE72hTIjsCDNHbIt6IhRM2uyL-ghKJVl3awEeDA_pumV92W48eYK8RcKBZ6Fg4wjT-twTgOMsPfW00g1s9UPKh1wbXb4-7hlw6rpN86KP5f6LFpMc_1hSx_kWvyse1XAMK9dgBgMwylg5R-oBpu9_-wDMcfFHMdp8w26QxcMEZ-_drqPJpLJyd7HHgDkmLZTkRRBLWDF3F_OOeyJ7YWStwOI5SJc-OfEi0SgCy6i4BtpaU4YhMQ7jP7IBNoMp3iysbG9SKTtCROTF-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد آلمان:
لایپزیگ پیشنهاد 116 میلیون یورویی لیورپول برای جذب یان دیوماند را رد کرد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95856" target="_blank">📅 17:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
نیمار و دختر خوشگلش‌ تو بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95855" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDb2luhPpunZRaNPn8-KLmp2xAMhnmoSGFKhYOXJcaq-Lv1CnWddZQcl0UUROhZbrmJJs7gzGuxNRHI_UC7Tqo8HEzNxrkms1GLlHTJ3X-vTtWox-ij-VjgsI-erJemZq3lmd5II9FNqPnOpBPaUG9go3EVdhJVPzCMW3V7d9Az6GNmoKoZGkEXEH47rEF5COyhRuNvxaSqfYLseG1EXCpF8CPkv19af8EqLQUvww6c8FQOLIYQmiu2D7Lnw0IxQ1dYOTxXRyVWOg65QcXTvfa_BwoOSFRgz5nG9ikoC-ojlizfLZmnz6Ax56ywj8YGZd5Yerelo4HlNl6YkV3CTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇨🇼
کوراسائو روش متفاوتی رو در پیش گرفت. برخلاف بیشتر تیم‌ها که بازیکنا رو تو طول تورنمنت تنها نگه میدارن، کوراسائو خانواده رو در اولویت گذاشته و اجازه داده بازیکنا کنار همسر و خانواده‌شون تو یه اتاق باشن. حتی فدراسیون هزینه جابه‌جایی خانواده‌ها رو هم داده تا کنار تیم بمونن؛ این تصمیم کاملا نشونه فرهنگ گرم و خانوادگی این کشوره که حس تنهایی تو تیم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95854" target="_blank">📅 17:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCU4j6WW1tfNuJACMwFPVCX8h7UYi6cY4LXPdbOjJMFLSgsDBfwk1cDKTRGwSAldxeeXocWydDI5E6L2IdAw8_ixXKGfT2YUNSE8rRUXCvglVi_oLJuTzr8_DafhKjB4cbK8qjXL4fCGYEeDu3r0rsDpdpaxTFp8qVejWCI6aVqDaDFTuDBErxni0eX4V3mAbdW6hivw269RukdxH6d_TxYPk15YevgsSmEReRcmRjNNxpKSN1hXOkp_nllk-rnyMx-dcCVVRnlGaqpS0VrUrswwzVZa_tji6IqQkUNhGAMjtw30lUBTtqKosZgaZJsLvFQUMuLCP9zyVNIK7XknAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی تو هر 3 بازی مرحله گروهی کاریه که فقط اسطوره‌ها میتونن انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95853" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
روایت ایستگاه آتش‌نشانی تهران سط بازی ایران بلژیک که بهشون ماموریت محول شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95852" target="_blank">📅 17:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
به‌مناسبت تولد لیونل‌مسی این صحبت‌های زیبای دکتر صدر راجب اسطوره رو بشنویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95851" target="_blank">📅 16:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
وقتی قند تو دل هوادارای فوتبال آب شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95850" target="_blank">📅 16:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇲🇽
هوادار مکزیکی قول داده بود که اگه کلمبیا از گروهش صعود کنه یه حالی به پسراشون بده که به قولش عالی عمل کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95849" target="_blank">📅 15:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=fT82ib_PeQkcG5CrlHXYbP6GgZ4H4LdxPZF9Cp4-zSVgkaGEzMwksfW5D1AHTXRDdVMu5ivzyHTTO1qfySedk9uZsF9aGqVSlZilcWkvowqXu2mYdBbibwSkALZ8dtr8RqxEMZPKMD2ygEqOhCb33uyZdTvj1AzmAbd0jyV2w8-6IjoUzYyVvvWAI6oizWAAR9kiFU6_Ult_lngpKlsaffiLB6Uml3lNon9ENbK4TPyFCrLG_YrdwjjsTPdI1iwLf9Nin76Xo7UecePh67ZeYQMmYaNCQUUrKAeUYLaJ9PpSRLLmFrPbjl4djyRAcssAisck48gomWSOxSm3PoacHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=fT82ib_PeQkcG5CrlHXYbP6GgZ4H4LdxPZF9Cp4-zSVgkaGEzMwksfW5D1AHTXRDdVMu5ivzyHTTO1qfySedk9uZsF9aGqVSlZilcWkvowqXu2mYdBbibwSkALZ8dtr8RqxEMZPKMD2ygEqOhCb33uyZdTvj1AzmAbd0jyV2w8-6IjoUzYyVvvWAI6oizWAAR9kiFU6_Ult_lngpKlsaffiLB6Uml3lNon9ENbK4TPyFCrLG_YrdwjjsTPdI1iwLf9Nin76Xo7UecePh67ZeYQMmYaNCQUUrKAeUYLaJ9PpSRLLmFrPbjl4djyRAcssAisck48gomWSOxSm3PoacHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
جواد حسین‌نژاد از سوال خیابانی هنگ کرد؛ چجوری میتونه اینقدر کسشر بگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95848" target="_blank">📅 15:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=FJTeWNf3sb73zcRfpcEUsl6j7sF9RJjnxEPygtU0j8UxJ9d1FuukPW2VwibnQuE3HF2a4-SHAMaWGdyzj8QOfT5VnKH0ePB6RyY8Nh2hgdK_LzEUjL0RgfQZ9WNF219sF0_kDUZewFbc3r748BP2RaBoiOMldYzPpWUi9wqSyH3u1ZI0zGX-KcijULqr_yUD8UP6eTjsqUqu113TeUKMJSAsvD-5QoeiArFXsuRpJQe21jyrvUuXn3hNaKprLCf86EEhzpyLKWgIVhp25W0pCTfMn7_UBztsNOmuKmhETOrn32-Qp3-jf-Fdks0k6XTyxq8iGMz39wEgwwJHLKe3sWxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=FJTeWNf3sb73zcRfpcEUsl6j7sF9RJjnxEPygtU0j8UxJ9d1FuukPW2VwibnQuE3HF2a4-SHAMaWGdyzj8QOfT5VnKH0ePB6RyY8Nh2hgdK_LzEUjL0RgfQZ9WNF219sF0_kDUZewFbc3r748BP2RaBoiOMldYzPpWUi9wqSyH3u1ZI0zGX-KcijULqr_yUD8UP6eTjsqUqu113TeUKMJSAsvD-5QoeiArFXsuRpJQe21jyrvUuXn3hNaKprLCf86EEhzpyLKWgIVhp25W0pCTfMn7_UBztsNOmuKmhETOrn32-Qp3-jf-Fdks0k6XTyxq8iGMz39wEgwwJHLKe3sWxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌صحبت‌های زنده‌یاد صدر باید با طلا نوشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95847" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5255345.mp4?token=luRzPyG4EZIUn9AN6sDJ8s7SguUkwcpMPkTxOhgYzNmGtW1ztQHp15cDOdsug32LNPHPBxGBHwwa8lZkQbY6Hbd7Z9paQ17LjDNuwdtP5lcSKyuyN7z5gwqNoiglqYvWvNd4fJRLYpg8yQlC2qtdklYISsRInaMwEsjDG55_hSdmMNuOMjm9DXrskOrKpefMumBHwYrAzwDRnk1uHy5McbUm9gjehfKW_kZcBVaF4YyXukKYDXW63aZYlGwUMXi7Xc-rBHZzXMotgWZJ7VDeZw7XcHaqMwgL6JrnzBrkMr4CdUugpB16JqRM5wZNJQM92XTBDWCD75yxQhQ-qKaO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5255345.mp4?token=luRzPyG4EZIUn9AN6sDJ8s7SguUkwcpMPkTxOhgYzNmGtW1ztQHp15cDOdsug32LNPHPBxGBHwwa8lZkQbY6Hbd7Z9paQ17LjDNuwdtP5lcSKyuyN7z5gwqNoiglqYvWvNd4fJRLYpg8yQlC2qtdklYISsRInaMwEsjDG55_hSdmMNuOMjm9DXrskOrKpefMumBHwYrAzwDRnk1uHy5McbUm9gjehfKW_kZcBVaF4YyXukKYDXW63aZYlGwUMXi7Xc-rBHZzXMotgWZJ7VDeZw7XcHaqMwgL6JrnzBrkMr4CdUugpB16JqRM5wZNJQM92XTBDWCD75yxQhQ-qKaO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
داستان ریشه عمیق ارتباط صمیمی بین کره‌ای ها و مکزیکی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95846" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbf385023.mp4?token=F5jci7BFmlMl8PMUfpNnib7WO8F1vVyhRzSjd-oyKcSe2T5kt6cVfAxUCU0pipLkQqhj9YdwY11QIvWS8Z3VktGKryPDIV8NJ8UKcjWT80CT_0q-b7mNfybIlg9_x3XXG6r_rO54k_UdDJkP0FqixMr2-gLqONhmEwb1LUVLU1hMD_kJUrFypA2p3O7TdF5gLw3Islm210iHv71F1YAZmHiv94KyNp_yb2OuUb-bEHLJr-oh8jRi0IJiiHTZzjlY8-IU3Fwr6_LwBS9hGnfgHcSEdSHRyrWvWl48_LUe4KOhJxu5n6Jni3w4VcsCfflVYVxA1cbIKLDs2UICf1ccrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbf385023.mp4?token=F5jci7BFmlMl8PMUfpNnib7WO8F1vVyhRzSjd-oyKcSe2T5kt6cVfAxUCU0pipLkQqhj9YdwY11QIvWS8Z3VktGKryPDIV8NJ8UKcjWT80CT_0q-b7mNfybIlg9_x3XXG6r_rO54k_UdDJkP0FqixMr2-gLqONhmEwb1LUVLU1hMD_kJUrFypA2p3O7TdF5gLw3Islm210iHv71F1YAZmHiv94KyNp_yb2OuUb-bEHLJr-oh8jRi0IJiiHTZzjlY8-IU3Fwr6_LwBS9hGnfgHcSEdSHRyrWvWl48_LUe4KOhJxu5n6Jni3w4VcsCfflVYVxA1cbIKLDs2UICf1ccrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دخترای مکزیکی چرا اینطورین، ولشون کنی همشون از توریستای جام جهانی حامله میشن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95845" target="_blank">📅 14:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇷
🇪🇬
تلگراف
:
فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم رو رد کرد. طبق اعلام فیفا، هواداران می‌تونن با پرچم‌های رنگین‌کمان وارد ورزشگاه شوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌شه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95844" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=sgTbkGZkYAmN8zfcMe7MsalbLuXRFqQiN7f_yE0btpIOZDf5D2xG4_VoaYgzvQmqoYK6iRBtz58vzxFVzAvKwozt4WddD2PaW7J9kZEn6pQ-SiUm7c2yE8ZX__y9kvfwWsa1dFp8HgV2pvI8vsn-mHlbBD1_LYuP3OkpqyZyqFZb7usSWDX8nXMjozSVT5XU2yvyjKbuib9C3Al6-qAkDFe5v9uscn1oceU8360fcUMGWjFLMtcsd6fRB4bvUZNVcQkYl1p5SW7_uHzpLPr_jh8LC7EIOGv1VLnkwynKRUyDaNY1Epj-up2fyLWFS7A5JercpZgJE01wHGaKDmLo0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=sgTbkGZkYAmN8zfcMe7MsalbLuXRFqQiN7f_yE0btpIOZDf5D2xG4_VoaYgzvQmqoYK6iRBtz58vzxFVzAvKwozt4WddD2PaW7J9kZEn6pQ-SiUm7c2yE8ZX__y9kvfwWsa1dFp8HgV2pvI8vsn-mHlbBD1_LYuP3OkpqyZyqFZb7usSWDX8nXMjozSVT5XU2yvyjKbuib9C3Al6-qAkDFe5v9uscn1oceU8360fcUMGWjFLMtcsd6fRB4bvUZNVcQkYl1p5SW7_uHzpLPr_jh8LC7EIOGv1VLnkwynKRUyDaNY1Epj-up2fyLWFS7A5JercpZgJE01wHGaKDmLo0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
کار‌جدید حمید سحری به مناسبت تولد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95843" target="_blank">📅 14:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrfYZNjOAIE_StAp-Mrsv9aZg9_go0_aZAVXdFLT3XbPpOfY__CzuZaLUJst3K3Z-fdjBKEKW2BZaDe7tsSz-j-1Q4kUuumuKrb-wxD_JVZXqp-T3PvUJuFNWn8vkDAsIr4Q-mnjnd9RlJ5yAepp-ZKCAExc-D2LVUgpU2aJk3quPn0xnKNniZhgCYtY9HsIwZ8f3LjR6qRJSshjv4Uve8Rq9SUVMhDX72SO_-3T6d5MPdqmaL4dGESLcYeg6ASi3JfMsXshZZv7l9PL-RMGB0ut9-Y_ep5So8K41T2LKfP-X6GUlGa5KQ4r4Ehek2KbE5M9kILZQ5JlqTC_bYYzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dp3uZFUxI1EzhYkrOkdmzqrjk7GEXWoZumGe_bHQiU-VSrKol8wJJ6ARTQN1-ij6LMOD0_3L9m24v7YRwhG5gYhw5izNPm2nTgGznzyn45gk5YzVkJT_7AcM6kHTsYolrggvWWe43peD-NRT9vMZYsHphb229_JXUV8fmCa0Xp_PFRbndZ90JqaOaoxSgijtjXH4iQCigyYpOK4CW2PlSiVDtZI584-YstxFPMVA1bgfQP7Vhn2mW2ahSdbxkFEEaS0E9I9Qfbm1-Qjcn8NcLjeJ9MD0TFEXisa655D7VfzA4MQUaz97Hp_hnEBxjoVs9vTpZ43WWNDRD_4u5xhSTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95841" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=BFqO7pGeeozg_qlW9UImkhXvbj4Z6Nbklk5JmcitC4KlXqqlOSDSu8kSFC8QZElGWUWuGy3zM6PTSLosHK4f-qBuJto6BTpH8f6540iy-SeVVoM9tS6fpldzpZRu-udmaXrk5KLwgE1f5lZyp2g3DC6_uPw4xP-ziE7jTz_KRAYLzxtCdOEEshJc6DgNcyTV018bFODqDH-EYh5StV3TV4u4sKKrTdzzQx2k2ybko4l1Q37dHnUWH2p93-UzZuileKHY4VPt6phYq1nR67ZVSuPMjcYA8mhzqEjTm_4asz9W4eGmXPSKK7LREX3yyZMq63xCKtYiqfCRJLCQbFG5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=BFqO7pGeeozg_qlW9UImkhXvbj4Z6Nbklk5JmcitC4KlXqqlOSDSu8kSFC8QZElGWUWuGy3zM6PTSLosHK4f-qBuJto6BTpH8f6540iy-SeVVoM9tS6fpldzpZRu-udmaXrk5KLwgE1f5lZyp2g3DC6_uPw4xP-ziE7jTz_KRAYLzxtCdOEEshJc6DgNcyTV018bFODqDH-EYh5StV3TV4u4sKKrTdzzQx2k2ybko4l1Q37dHnUWH2p93-UzZuileKHY4VPt6phYq1nR67ZVSuPMjcYA8mhzqEjTm_4asz9W4eGmXPSKK7LREX3yyZMq63xCKtYiqfCRJLCQbFG5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
😛
سطح اعتماد به نفس بلاگر نچرال وطنی: فوتبالیستا و بازیگرا میان دایرکتم؛ طرف باید ماهی 300 میلیون خرجم کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95840" target="_blank">📅 13:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9758eff507.mp4?token=GWsg-UpGrF8RA0h9wZHKzPJbqiDi-DT8Uprut75OuJTJOi-gSfEE8Cs17inP7TI-7moC-ONfE1lL3D-zIvvugOAsTdxSbha2i7dXbjMbSe6T_IaY3fgvDa391OhgN-9ixn4cq11x-R4YeoynWEqbXl3ynvssjOHXK1oj1KVBHeHe2GpwtxfpLmxhE8S7y0jaJ4lGb1JGOTFyENwbmXumggXzUwCNerUN0sopEl-PQg-BeK45wxmcAuUkXlkCenggN63_PqSiFd-od4gEUyY2e6Lk8B0Cts4tOqX0STmfWlZCCTi0LmIMVJdTRhk8orYu0Q9efsjqT8KYYDesFFoi7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9758eff507.mp4?token=GWsg-UpGrF8RA0h9wZHKzPJbqiDi-DT8Uprut75OuJTJOi-gSfEE8Cs17inP7TI-7moC-ONfE1lL3D-zIvvugOAsTdxSbha2i7dXbjMbSe6T_IaY3fgvDa391OhgN-9ixn4cq11x-R4YeoynWEqbXl3ynvssjOHXK1oj1KVBHeHe2GpwtxfpLmxhE8S7y0jaJ4lGb1JGOTFyENwbmXumggXzUwCNerUN0sopEl-PQg-BeK45wxmcAuUkXlkCenggN63_PqSiFd-od4gEUyY2e6Lk8B0Cts4tOqX0STmfWlZCCTi0LmIMVJdTRhk8orYu0Q9efsjqT8KYYDesFFoi7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کریستیانو از این‌شوخیا نکنین
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95839" target="_blank">📅 13:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNweeFlWJmX1zsnvrniUDmjh5_82sRKWpZ7IUAP3e_lvIJzzAWuv-NhutLZjoFyDqtVO3DTc5t3mM_wPY6J2mi__2jA5Q_TKZ2cVstuLRbvbQJArMbwPnLXHmd3AiEIm9q1ib35C-aCnNJJtiVY1FfxJxigf2biVYCPFAxBZW901YMZnwvmLrpDZd3eDD-Whyr8Jw-wf-LOSKGP18CDFQDKAeQgYwl89EjubRyBSfGf-x5DRI8zs5lqlgR5QBnS1rRWouuzSk8x8SN3TOZBrLCMeqFgA-D5j90tmrGRvzGvjCStR6uPOqNjiMpnAdr-6UonUL8qo0BqmjC7lkEDnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
🇧🇷
🔸
وینیسیوس جونیور
:
🔺
کارلو بهترین مربی جهان است، و می‌تواند بازیکنانی که در اختیار دارد را بسیار خوب درک کند، او کاملاً با بازیکنان سازگار می‌شود و بهترین ترکیب را برای هر تیمی که مربیگری می‌کند، انتخاب می‌کند.
🔺
او به اینجا رسیده و فهمیده که چگونه باید بازی کنیم، و من فکر می‌کنم این موضوع موفق بوده است. او در طول مسابقات بسیار پیشرفت خواهد کرد. من معتقدم کسی که مسابقات را بهتر درک کند و در جریان مسابقات پیشرفت کند، برنده خواهد شد.
🔺
در مورد نیمار، بدون شک این لحظه بسیار مهمی برای همه ماست، زیرا الگوی ما بازمی‌گردد، کسی که همیشه مبارزه کرده و همه کارها را انجام داده تا اینجا باشد.
🔺
او پس از مصدومیت بازگشته است و امیدوارم که به پیشرفت و بهبود خود ادامه دهد و در طول مسابقات به ما کمک کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95838" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcOUR6QdjUB8iaSQBsYZyijxKqynA_PstG8riolAeIkflyzppU_KsL8KBh14tBaJvRl1VU3OgYBRSZGmAWMVXpGLitCl-u_g-G4ayvLewKHHTXKNj4_S-LCqO7gw-o6PJZdPEhnpK5RIN3pFWItMdZ4hNt2NBY0P026FOSVojMwI2RvlO3u1PmVoakEhfyF4Q0iRiAPhQQ9-B-_t5S1M6yAkDdRus4jPsi_gLtJ3J3OETy0wn3c43_hvVWyRDbAt6ih1Pb5ACdN7YEZY1suvYGiO3aFdY5qQDYvfRG5XqTcSwS1evv8hIgEJGDWyQcT-K7Xh-0VUjMUboceOYM1oSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب گروه A مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95837" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=AyZfuVkFCfwdlNoBxzJ9rDrzaZyQ0eEohyR7yAvahFk18xcZm__SHz0o_AQeS8J7GxLuYqoSbT7QdAkXpq54TN_musUrfyAKN2Sr-rxbWLI4N1MZIcL3gG_8J8TktdxGsQvkjq3qD3kv4HbyV_9k1eEcWhEVFysqqugO-s1EicpJt203YBA4fTPOgVCn0BdnCRUZsiKZvPXsRf8173CksMoPnbnes7xIIVAHQXzJLI4Wko4MRACmLJDfzuit9RG7F3zwpc4Efuh-G8zwpQmFGPFBYQeD8JZ4Bp0JyC122nbu2IiXwH8xoF8kDryICGPz-72Z3cOSdmN4sM0ndVg8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=AyZfuVkFCfwdlNoBxzJ9rDrzaZyQ0eEohyR7yAvahFk18xcZm__SHz0o_AQeS8J7GxLuYqoSbT7QdAkXpq54TN_musUrfyAKN2Sr-rxbWLI4N1MZIcL3gG_8J8TktdxGsQvkjq3qD3kv4HbyV_9k1eEcWhEVFysqqugO-s1EicpJt203YBA4fTPOgVCn0BdnCRUZsiKZvPXsRf8173CksMoPnbnes7xIIVAHQXzJLI4Wko4MRACmLJDfzuit9RG7F3zwpc4Efuh-G8zwpQmFGPFBYQeD8JZ4Bp0JyC122nbu2IiXwH8xoF8kDryICGPz-72Z3cOSdmN4sM0ndVg8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🇲🇽
هواداران مکزیکی این‌شکلی بعد گل دوم دیشب کشورشون عشق‌حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95836" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/95835" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95835" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-BcEaZB1SliDPz2vT__oR8QAdUVPXoGk4KoWO4o4eOgBEitOtotoRh6ZU1ty5jJJPrMT546LnUNVQm8zLAxjZpm5nDFfS0U3GZSIUM0ytUJRv8wqBf8HN_EHBaDCnwrAb2JSnabQIAATFNcGCeqj5iSXNL52HNiT_AcbD_xH11j1aBY_-F8zwuEzPsZua_ALGtSNfTxjEr56e5rKrQ5nQTbEzGWBrkRSxt6MmfjVa08dHyfgdnb2-k7HaXTrC4IEd92id6_K_LYP2ks3zKUupLoD18Vmf2Q-d2lrZzs00F8lAepVCaMGU7yKdHRFo2wcPUIgNizdZqqq6RmwfMufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95834" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQRvcXTkoRuuUnDXHMGAXPY8fgkMjpDxH6dOe6HbacAUwyuRtM3H0o97cp6WATn1Exb9lVFec-6k-jYJBg6EEggLK7J7n7wY-6JHb72Jo7KbnIOIt852o8LcCyf-eJqSSUJeidn00WH1RSxO8599ddHOa4VQ_-99iGXF3PL9YXjKyfLtYFwUh5aP-sZwCdgqIYTPqvtbreqQFgVyhxL6nusKA5ip_V1g1Km6x9aBKLsmpeF8HoXc30-Hm64Q9qrXtUV1D5mXdJKrBmnYF3_ZsFF1BaMz4r93QtAWedN6LTT7TeMPcqH5t18bx_vJWJi4AkouxMaBtoFOtWZ166Hnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95833" target="_blank">📅 13:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=UMkvBSGMNYcUEXZdlx6G8o_jTQ-xhAesoWLUReJhAEGFi4OJ8OsbYjmDXsJfPyB-2D_DKGS76of-o52wSVDMWImQCW8ox56hRDwjYQYetTtrQlxyTiULSSzE0xNfqI-hHCt26J1EyCpYKeVxUSFA8dseSj26kZr0PopGm0_0BuVMyhryIfBLHl-F-xAvBdXwnqrV9gVDeAutQ8I_98C4gQMRN6BN0XvkUVPl_J3SIwXZ0snjIi4r8y8pjuUWbcBKQh5kg2UDL8RyZUK0PRyeE1zxEkfR6YI6hu_fayQXfv61Dopx7IerND4_nkO9uVbIO7EsPPVgr6go9DtFL--eEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=UMkvBSGMNYcUEXZdlx6G8o_jTQ-xhAesoWLUReJhAEGFi4OJ8OsbYjmDXsJfPyB-2D_DKGS76of-o52wSVDMWImQCW8ox56hRDwjYQYetTtrQlxyTiULSSzE0xNfqI-hHCt26J1EyCpYKeVxUSFA8dseSj26kZr0PopGm0_0BuVMyhryIfBLHl-F-xAvBdXwnqrV9gVDeAutQ8I_98C4gQMRN6BN0XvkUVPl_J3SIwXZ0snjIi4r8y8pjuUWbcBKQh5kg2UDL8RyZUK0PRyeE1zxEkfR6YI6hu_fayQXfv61Dopx7IerND4_nkO9uVbIO7EsPPVgr6go9DtFL--eEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🏆
روایتی‌جالب از حضور روانشناس خِبره در اردوی تیم‌ملی برزیل و کادرفنی آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95832" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1FzgDr7R8c_9fMvIgjrQ0Q2mjE9YUcaKr4jJwxpcvpsdtOLxQncJSXkDyfGIDorde2_qt9SyRGdgkH36jf9k9CTp822Ab9GiSCVhTzhYxNAmNYMS8vlCtexLYbzG22fN8xWlZHf2sY70XHz9Xi25VqQ9m49gXpSj7mUDrNwjnB8StBAzXSzvgnE8iMUGqb3r7v-8PBzZ8LYTX50Ln9bh3V8d1FdSZq4vzaem659OCDLmD2OmSzX8Ea6L2o0nzkJXgrxwb9Auf2NUETo99i6QrBaBCiD-q0mRiLs4EyfQDIX_CgM4sDF8PxF6SgHA46ZqdVgzotKQwKvdTg1v9ULAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد گل زده رونالدو با مجموع گل‌های ابراهیموویچ و آنری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95831" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB9S6aOcalIVkk6jiVY_QBw0YzBBFrPxJArzgkunWq_zpoBGLr4owH4pjoK0r84GlHPhA9rMIJoX5OdpeT6gZg5vskeZr-yX-msSegE5sK3Jjo0xdWVcPs--6yFI_YLVUU_351nRbsSWmn8o1GdqRlE51elKxgGJbdaeS0kb5mFjJGSjJ_Guc1Qaj7UkZ1-IeVgif73eCX91YrjcJUCaM6CWdYz2PahaLnC7SeRvYE5xGQFWFuKSlym1j89HsoNvzdG_PwL6gUqD9dKcQMC5c8uxyFq51N4p47BJF6TqlT9lF36OPcl_avTAlPpQppH703vcDTNAj68vYgh4d_npxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
وضعیت سون بعد باخت کره مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95830" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2alajCIFKFnEILzTIN5xXS5JEX07FHGIGCuR5KcSbM7lqnXzM36PRFzhWWJS1jUlLy6BcIeG3zpGm21981X74ub2-jUL7vfaCeLRWi5az_COUa2o_BQxXqhbvKGgCLaeko_cBao7uShkGq4QFqgT6ZnEuTOTYmEcvn27Xo_yaqOm2gjHyG2vhE9MmbSM9YM_aiBHzRa8FrCGGbGwEL5uTWhk-m98uX37vgiM-UYQ0IzVAWow100rlzsdpD4PFvt7XoO2z695HrRXyUG-lyiKDMIWZL_cXD4kcOJCwHev7p7zAVKj_pOmhj_5SZ1hVfUCL1TMCH0pMitLqL1FqZiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از صحبت‌های اخیر تیری آنری و زلاتان درباره کریستیانو رونالدو، هوادارا تو شبکه‌های اجتماعی میگن این دوتا هنوز از یه سری اتفاقات قدیمی دلخورن و از کریس کینه دارن. بعضیا هم میگن دلیل این حرفا میتونه باخت‌های قدیمشون جلوی رونالدو باشه؛ مثل وقتی رونالدو ۱۹ ساله آرسنالِ آنری رو تو خونه شکست داد و رکورد ۳۲ بازی بدون باختشون رو زد، یا وقتی رونالدو با هت‌تریکش سوئدِ زلاتان رو از جام جهانی ۲۰۱۴ حذف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95829" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=Q2UrEe-cLXcTGgJEszNbTvi5Ko3fv7JLdYjXC30plQLHK9KE8LCOFpyCFpEaEFp-2EuNxwkfr3I1O1uUUXs1i82cbs2ecpCFnJMO5UWWqoa8GdQ1bb7PyemScAfdD9UEcaJ93XhqYGKY24xF-SrxhaJuLqAaJpvABZ5XAFpXTXwWuW2cJk-apMB-CpVbMzQPCgMcvhaeYSAfhuYq81myg5sb4MBBI3E5d7THZWLDx-si4cWLl02r_3fyB5cPapZHK2RQ3ORW1o5v7R7tYwFG36NFGxRFdv-f4lKudYWA8xT3GkIjc7jV1o9cnKLAdp0BXsaJQdPfpqZnt8rtmiGP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=Q2UrEe-cLXcTGgJEszNbTvi5Ko3fv7JLdYjXC30plQLHK9KE8LCOFpyCFpEaEFp-2EuNxwkfr3I1O1uUUXs1i82cbs2ecpCFnJMO5UWWqoa8GdQ1bb7PyemScAfdD9UEcaJ93XhqYGKY24xF-SrxhaJuLqAaJpvABZ5XAFpXTXwWuW2cJk-apMB-CpVbMzQPCgMcvhaeYSAfhuYq81myg5sb4MBBI3E5d7THZWLDx-si4cWLl02r_3fyB5cPapZHK2RQ3ORW1o5v7R7tYwFG36NFGxRFdv-f4lKudYWA8xT3GkIjc7jV1o9cnKLAdp0BXsaJQdPfpqZnt8rtmiGP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
یکی از جذاب‌ترین ویدیو‌های چالش آهنگ شکیرا که میلیون‌ها بازدید خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95828" target="_blank">📅 12:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=Ttvxe8RRCj6LW3pSSucbNWg86dkIeCDg3V-WVB2LyiZzhHUbWGizmLUZGPeCjy3larNVnK07VsDaE_gUaPBC06JnpFf7IBfLsPwMpWnwIsyWV7Wn18qxh7lZbUtdMtEOXSte4NPlUwrChYu4U6zpedB7reFdZHLf8shEqKvpizbbAktkkVf8hKSzHHEhiIEaQggk_ZTSRdocsve3IAPjrsfzAErWporIXGIQeZIO7Bq3xFlurkMms17D1ALqIe0P8xWsRVAxbhMhNDSZZD5wu35K5ov19J8h8sBq29T48Ey-9yCfcfUKbxD0UPNvdW3ReQjKcH_ZLMwfpucUtOfjAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=Ttvxe8RRCj6LW3pSSucbNWg86dkIeCDg3V-WVB2LyiZzhHUbWGizmLUZGPeCjy3larNVnK07VsDaE_gUaPBC06JnpFf7IBfLsPwMpWnwIsyWV7Wn18qxh7lZbUtdMtEOXSte4NPlUwrChYu4U6zpedB7reFdZHLf8shEqKvpizbbAktkkVf8hKSzHHEhiIEaQggk_ZTSRdocsve3IAPjrsfzAErWporIXGIQeZIO7Bq3xFlurkMms17D1ALqIe0P8xWsRVAxbhMhNDSZZD5wu35K5ov19J8h8sBq29T48Ey-9yCfcfUKbxD0UPNvdW3ReQjKcH_ZLMwfpucUtOfjAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژروم‌بواتنگ مدافع سابق بایرن‌مونیخ: «مسی باعث شد فکر کنید احمقم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95827" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521d31d087.mp4?token=oOqnsxADN5asoKHhd9MYWkm1qHnNUrofvtkzPOn9pw8c0aJLc_IUTqew5sOB0EHVSiL3YMhj4kNhiy1Yno1IXD1BworilGsfysAFLG4XQL5IbXaDqQwlyxSeFQVakQNHZFOpRzmQGbn2Ats7Hrb4zgA9m2LWQ2rXC6eHfENqn13fyV1HKbcN5rgTk9NQ3ct2xlBJp40Uy_1y5C7K3ig4fW-SkZMkqTkYp2__sOGV_rXU5mcUI0lSqlMrdRrIDIZPMNRsH4hWYtB3FHJnDq8_aBPKKqOlucYtTIUXDc2jZ2WarqTocdq46-ctcWMcb-1xkVDqQd9niyKP9brBoZGVvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521d31d087.mp4?token=oOqnsxADN5asoKHhd9MYWkm1qHnNUrofvtkzPOn9pw8c0aJLc_IUTqew5sOB0EHVSiL3YMhj4kNhiy1Yno1IXD1BworilGsfysAFLG4XQL5IbXaDqQwlyxSeFQVakQNHZFOpRzmQGbn2Ats7Hrb4zgA9m2LWQ2rXC6eHfENqn13fyV1HKbcN5rgTk9NQ3ct2xlBJp40Uy_1y5C7K3ig4fW-SkZMkqTkYp2__sOGV_rXU5mcUI0lSqlMrdRrIDIZPMNRsH4hWYtB3FHJnDq8_aBPKKqOlucYtTIUXDc2jZ2WarqTocdq46-ctcWMcb-1xkVDqQd9niyKP9brBoZGVvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
امباپه: «کین، هالند، من؟ بهترین لیونل مسی است، همراه با کریستیانو.»
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95826" target="_blank">📅 12:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00614f2668.mp4?token=LLjI6SFiGvsJgg8-uCze8Rd4Bxa8HOnh2x_ygT67RXwAuuMXs9bQ9XarpHiRtBIhhEdR82SFrL0dFBdPzpyt6uP6vSCqVuKngHfsviiiWzKfpExG30Zdl-uXm_Ydo3V_scxZ2Q9WSnZbZsM5Yymm3SfOaE2uLQziHXkZ2Y3syejPMNzWFSZUHnnZ5OayRNsYyxHnkWAMAm4lQhsSb6DNQhIu2VLMq6-5e6uful8A3s-Kui26fkyFlcx3GN-hKPeiOyVcM9AENm8aBLWo7om52NdH8SqUBXLN0Yq_pY_AL99Un6FMp5R3okvKRFi1T5ciLJJeSSAffUQUOkDj6qvayg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00614f2668.mp4?token=LLjI6SFiGvsJgg8-uCze8Rd4Bxa8HOnh2x_ygT67RXwAuuMXs9bQ9XarpHiRtBIhhEdR82SFrL0dFBdPzpyt6uP6vSCqVuKngHfsviiiWzKfpExG30Zdl-uXm_Ydo3V_scxZ2Q9WSnZbZsM5Yymm3SfOaE2uLQziHXkZ2Y3syejPMNzWFSZUHnnZ5OayRNsYyxHnkWAMAm4lQhsSb6DNQhIu2VLMq6-5e6uful8A3s-Kui26fkyFlcx3GN-hKPeiOyVcM9AENm8aBLWo7om52NdH8SqUBXLN0Yq_pY_AL99Un6FMp5R3okvKRFi1T5ciLJJeSSAffUQUOkDj6qvayg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پیشنهاد جالب و شنیدنی محرم نویدکیا به فیفا
⚽️
@Futball180TV
‼️</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95825" target="_blank">📅 11:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=euCZLJZZtURl-CfC6s5NcKST-xD_du-hQqdeHMJ0XDjczfLWLUitnAR-spBoaVfT_XsmGcsCV5rYGd4t4gPCuvgrEUjZBjIo16HOBRUaixHYsuPUp833SJDRLjtTD_YYNlMe9xSLY8Q1iN_ySShK7zVGpc4_FqEhynFs17L2vOxXFNKQN_R0vw1kJ56fTiy0xRynhkF_vVg7n2sR5kYn8KvQD2GgV4_LpFlzcsvdm1Ip4zdeSfwSVhPHfZSvth6kvatXvNsKMHVgmbwYsWbS4cuD8L7HSj3OvgJ9x2xeb4It1JUSaH7bmV5MNVUQTSKsOt2OpEwi48pUXC5F71bTg6rWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=euCZLJZZtURl-CfC6s5NcKST-xD_du-hQqdeHMJ0XDjczfLWLUitnAR-spBoaVfT_XsmGcsCV5rYGd4t4gPCuvgrEUjZBjIo16HOBRUaixHYsuPUp833SJDRLjtTD_YYNlMe9xSLY8Q1iN_ySShK7zVGpc4_FqEhynFs17L2vOxXFNKQN_R0vw1kJ56fTiy0xRynhkF_vVg7n2sR5kYn8KvQD2GgV4_LpFlzcsvdm1Ip4zdeSfwSVhPHfZSvth6kvatXvNsKMHVgmbwYsWbS4cuD8L7HSj3OvgJ9x2xeb4It1JUSaH7bmV5MNVUQTSKsOt2OpEwi48pUXC5F71bTg6rWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
دوتا تشویق تماشایی که در سراسر جهان ترکونده؛ تشویق ایسلندی یورو ۲۰۱۶ و‌ تشویق نروژی(وایکینگ‌ها) جام‌جهانی۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95824" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcp41f1-Eua3V5jWA949fzeGsxp5euQuuaFsabjVl3XLWxKBEXAEzjre0jEuRBMvMmBDn_yY7oaT9e2DRaKk5wd08whiC5VzbKto6_Rm1OqDIKkRgGgRCVJUaLjmIwEv2mHM-a3_lP2An5I6h2O6OF_qVHn_nn5XqHPUj3JrYIKyIrWjMyrdrpbSKWXwemRm83LICWIYpKLYgmpdco7fDmfkoOe-vrBnoKHhUGua6y8yGkUMT4eYs2m_pzBJm3jPteZulmcs4w60DKKsJ8lPHyZ4ULIF49IT9tjacqmcVmbmxmas6LLXY_7c3FlmpFvHXvH-ELSk1XrOfQMbVYvNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
پوستر جنجالی فدراسیون والیبال برای بازی امشب مقابل تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/95823" target="_blank">📅 10:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD2uZ0CGlpE8f875kdpRgwx3cJ8vIMWO6uK3vi-r08L2QVPXbmmKwKS38ifrIjweVYi9wVAS4duL2xruzLmLtxsK81JLlp_riZ1vF5VXoX7rnba4JldTEHcVHIBiDRDecjJ69AIoirPpcuPTDynNN33DYscfmn-nGLsgI-6FGpJEGKFrR1GFiz7UNV1PRLFq9FIKY1JJk57X2wh-RE3ckOWrmKb1IaapnHcCBHFVp8WPgL7H42t_ul7HR87d-etaFk6jywaJJcNEmZ6XPBmpkNHSb5itwf51lfR23Vpu1J43MB2sE1nYWW8ucK5bbO00L9S00TxKNQcrFTvgRjHR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
🇮🇹
رومانو: رئال‌مادرید به کومو پیشنهاد خرید نیکوپاز به ارزش ۶۰ میلیون یورو را داده که اگر باشگاه ایتالیایی مخالفت کند، رئال مجبور به قبول پیشنهاد سایر باشگاه‌ها برای ستاره جوان آرژانتینی خودش خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95822" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beRA_HUmI645cHurVW4oClO2fq1DeR48q5daEUyqf5_3YCeRZmSu_Y9geoVse2fqTxaqw2Xs_nDv3fVVmFF5bDb1llgj4R1_WK_I6rc-8h8DI1wr4t-b_pkNhC7FlhKQTxBZKpKfoB-Yye34_sMTkA8i05yuFVIF4ramjSPzBn9wL1AcFq2QiSYTXKMtT-Z9-jIuiZe7tgeuPuBtdMIpOYOxtQpW-UFZN7_i1Z7i4LQPhhPtKBdCBplt3Bd8mynsAxrL0I2WmvpBH3AvoWC9mBKK7vqgoffdbboFD2Moi45mscTYYtHywkSjdYWoCwFwvDkqQ5pSPBkxBK0vxlREDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه F:
🇳🇱
— هلند برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇯🇵
— ژاپن برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇸🇪
— سوئد برای تضمین صعود مستقیم نیاز به برد دارد
✅
— سوئد، هلند و ژاپن برای صدرنشینی رقابت می‌کنند و هلند به دلیل تفاضل گل برتری دارد
🇳🇱
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95821" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlTNdz9jMa0OFbiiAPkrdj-8y458OMj-Pi66mP2L7bT10-YzHnWj9sExW4WyOPlts1M5as9tg98frRb6weuGjybQ8cBQW9f7iCuYEtEVtoWEXotiCiUo1DVJY0a87DSZ00xlfj75CCXbaBUBrMsfMVlU09d71shbD9A3tL2X6GhbS0iGmOQjRBGx9lArJEIhtZ_LjOXVv5OTd_MTP8fQWaRQV87iYfFbwDwq6JDmJTJfnVJBW8bp9R5nPNc9OCclsibNeAO3tAMQec0LACml27k-5yD0QvvvaXCeDQLap8X8f40Vyw5Mj0S-aWKuZxPm4y5rqxfkNcUtVMkmllnErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه E:
🇩🇪
— آلمان به طور مستقیم با تضمین جایگاه اول بدون نیاز به بازی سوم صعود کرده است
✅
🇨🇮
— ساحل عاج برای صعود نیاز به برد یا تساوی مقابل کوراسائو دارد
✅
🇪🇨
— اکوادور برای صعود باید آلمان را شکست دهد
✅
و منتظر لغزش ساحل عاج باشد
🇨🇼
— کوراسائو برای صعود باید ساحل عاج را شکست دهد
✅
و منتظر نتیجه اکوادور باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95820" target="_blank">📅 10:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA79X9iNYfnedqS0UQ4uWMHiSy7zST2qWvjA4OrjsUvcS3FsIENeUCTWgrTqsIwZ_-cGWMltfU-ENkCJIctuH8LNbXV8t-KaJtjVMQdobSnEO92TsOWwJHBkUsZq6c_wVH-rp7svCEmxnOWdWTZoMPOnhtzRXMZhTYw3quRTiH3YCI8mjXGsdICqbe_NRRAdvfbt55R7PISjsgWCTxJ7jktSzj8ELCjFipihfxy05W2MGbBPZGsDkRxuPWavQmg3Czhe_WDSBdQkSdnM-x8CQMmi_7b1YkfEvtDhvqodJULoJ6qIWWTQiv4k5g568dPX61UVzkC9ji_SLFJ3sIvLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های لیونل‌مسی و رونالدو در جام‌جهانی به تیم‌های مختلف که ایران هم جزوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95819" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=NpgAFWwVnVXhQgks9t7r5Y3G8hEZ6RQVDflV62zzhe_FhuAlWOeKGNLjJqYRLqJwqY2bxqCzRUiN4ORmpUpFeYedzkb4Qy25stpHeIc5AalYB6iHmfOrx6bDVSfL9Mde7W7TYLzP9WIJ51IIau6oFEcDwLJtVfkjge7hsZ7XtUi8UOxxU2JZfiJkYVFpHwut6D5Y9r_XtDETCVqDdRTFwcU1LJCz5LITQ8tcYsPg1Koa64FWeyamXtQ_0inYfybqovjW-r_oQYCmIeh9RNBfMq-Wt-yI90HzUfmTUOLdL-9gG0kUrWNvfu_ls9W5DdZ0yWRaptMKccY0zTEgdMEHX20HCU5d4v4eWii-DFduszlgtQECtdZDdpQ4yEsHWu1LKZiaHB4dtPnF6yumTM-lwmW4OZz93vCwEQHNRsr1Ep2sCpAILZEDd1pZsVtXnIEcYHrP6jYoOhj-lwYtOT7ZwQoAJdEP4pXya3nNlq_Av6fcv1zsEwpPfWzQC0hB2FNlkSVyK_zm4IUhR7ePcbosoaaYIA82HZYEGHtjTjoqHPqxgKGQ9UbZAYdguUAvSSTs97Gkx-s90eUyAVHzpa-ZfE4FqH-rXgJD4cD45j8wWTuKFiVwxCcT4Q4sT3USiCTeOG2zn2_DSlKuLljujRF0n5j154B-UIBUpTAMyMVSJ-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=NpgAFWwVnVXhQgks9t7r5Y3G8hEZ6RQVDflV62zzhe_FhuAlWOeKGNLjJqYRLqJwqY2bxqCzRUiN4ORmpUpFeYedzkb4Qy25stpHeIc5AalYB6iHmfOrx6bDVSfL9Mde7W7TYLzP9WIJ51IIau6oFEcDwLJtVfkjge7hsZ7XtUi8UOxxU2JZfiJkYVFpHwut6D5Y9r_XtDETCVqDdRTFwcU1LJCz5LITQ8tcYsPg1Koa64FWeyamXtQ_0inYfybqovjW-r_oQYCmIeh9RNBfMq-Wt-yI90HzUfmTUOLdL-9gG0kUrWNvfu_ls9W5DdZ0yWRaptMKccY0zTEgdMEHX20HCU5d4v4eWii-DFduszlgtQECtdZDdpQ4yEsHWu1LKZiaHB4dtPnF6yumTM-lwmW4OZz93vCwEQHNRsr1Ep2sCpAILZEDd1pZsVtXnIEcYHrP6jYoOhj-lwYtOT7ZwQoAJdEP4pXya3nNlq_Av6fcv1zsEwpPfWzQC0hB2FNlkSVyK_zm4IUhR7ePcbosoaaYIA82HZYEGHtjTjoqHPqxgKGQ9UbZAYdguUAvSSTs97Gkx-s90eUyAVHzpa-ZfE4FqH-rXgJD4cD45j8wWTuKFiVwxCcT4Q4sT3USiCTeOG2zn2_DSlKuLljujRF0n5j154B-UIBUpTAMyMVSJ-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
🔥
تشویق وایکینگ‌ها به قائم‌شهر رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95818" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=RytXIhFfPlgPlyOnNZMZwKtY2u-iGerDc1ZlZwU2ccdcFufwn7biZ4uJeLRYsXxjRkJzz3BU7mIvf2irEMcnOPQTqJjX4uPyqjTX_47kw4Z1RRdbRCGu028sm4W1AV3gsZKDlwFaz3wFYdcittLkbbzmzk4clqznCh2cNTlbWsJnU5jgENJoQRF71kbR15L_phOOUvwjsjAPLI5a3Ru6IzZM9ewbEfdYAdphnGJrWcQqZki70g3v946rKSP65zcc9nGnYTeLwfsZMkoauzMdHVJOBS0MKEaYuOZiViySCu_NIxMTtcp2KNIltL8SEQ1Y8MB_iEcDc7f5fDG_NK1NBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=RytXIhFfPlgPlyOnNZMZwKtY2u-iGerDc1ZlZwU2ccdcFufwn7biZ4uJeLRYsXxjRkJzz3BU7mIvf2irEMcnOPQTqJjX4uPyqjTX_47kw4Z1RRdbRCGu028sm4W1AV3gsZKDlwFaz3wFYdcittLkbbzmzk4clqznCh2cNTlbWsJnU5jgENJoQRF71kbR15L_phOOUvwjsjAPLI5a3Ru6IzZM9ewbEfdYAdphnGJrWcQqZki70g3v946rKSP65zcc9nGnYTeLwfsZMkoauzMdHVJOBS0MKEaYuOZiViySCu_NIxMTtcp2KNIltL8SEQ1Y8MB_iEcDc7f5fDG_NK1NBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لذت دیدن لیونل‌مسی در جوار دوس‌دختر که ما ایرانیا ازش بهره‌مند نیستیم
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95817" target="_blank">📅 10:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=b2qIdfE_eRhhjV_ZRnmxKsD9Xl3y8BBtEe0r_wS29czYN7GnDIXIp-RWD-e3ezxAYHPhWCbIetl19BM9GxKxmCEFGZrvnjskQz66X_cAzxM4pBESDXigzzG12DhCUFdfLnx8DkJWnJYwOtu9TjOGI1AIax9Ignd8Zll5k9T_0MLoXOw94x7PTHawuxpfePfx8XZNkOxYMLIhT7J1OLJQDL1Kv8i8zab29P5vUrocRH1UpxDGabFQVu2wWostQ4_CBtX5FGf1xYdUErsSfp7PcE66udP7FWTocnAQA-D7Vf-GEVGyxu1qjrp8BCvQ3bX77YJTAfNwKJ-EBDMGNuFqpBmY-QIGqNQxBpkGryyzlYUGXRWdBh6I028Oc93TPecD-FS_vXGvVn1sWI3Wn1mzyx1eYjL4rYEBkHkBHzWmQn7mUPjWTs-ju2NIgOR9lc9pYtBJItMs3k9f7eby_m0uI6bqb6hjAaJ_P3X7hkPlxNc_HHLsgdq07djjPoCbdfU_NK9dffHlxPWnB8e-tWsaAc8C9LUJzCgmubXMZQS87MA3dte8bryUrPMwqjAPmQ287gDIPB3dpeZ5ihOl4kuq66PfPu2-xEFdBAX8V_SP_s15RVQ4pCCu9GGQkl2kbZTvtMO_bFnQxNudDDVfB8EmPAtwnqvA9Lm1nIdTmdP-hyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=b2qIdfE_eRhhjV_ZRnmxKsD9Xl3y8BBtEe0r_wS29czYN7GnDIXIp-RWD-e3ezxAYHPhWCbIetl19BM9GxKxmCEFGZrvnjskQz66X_cAzxM4pBESDXigzzG12DhCUFdfLnx8DkJWnJYwOtu9TjOGI1AIax9Ignd8Zll5k9T_0MLoXOw94x7PTHawuxpfePfx8XZNkOxYMLIhT7J1OLJQDL1Kv8i8zab29P5vUrocRH1UpxDGabFQVu2wWostQ4_CBtX5FGf1xYdUErsSfp7PcE66udP7FWTocnAQA-D7Vf-GEVGyxu1qjrp8BCvQ3bX77YJTAfNwKJ-EBDMGNuFqpBmY-QIGqNQxBpkGryyzlYUGXRWdBh6I028Oc93TPecD-FS_vXGvVn1sWI3Wn1mzyx1eYjL4rYEBkHkBHzWmQn7mUPjWTs-ju2NIgOR9lc9pYtBJItMs3k9f7eby_m0uI6bqb6hjAaJ_P3X7hkPlxNc_HHLsgdq07djjPoCbdfU_NK9dffHlxPWnB8e-tWsaAc8C9LUJzCgmubXMZQS87MA3dte8bryUrPMwqjAPmQ287gDIPB3dpeZ5ihOl4kuq66PfPu2-xEFdBAX8V_SP_s15RVQ4pCCu9GGQkl2kbZTvtMO_bFnQxNudDDVfB8EmPAtwnqvA9Lm1nIdTmdP-hyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
خوش‌وبش گرم اندریک و بوسیدن شکم همسرش که بارداره بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95816" target="_blank">📅 09:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=ZNmfW73EzrzANSJXrHpeAGB4qRhOU6j1AdQxQ-OOLqgialTXQnVek0x5ufETj6x45URqxic9btPt1JcteHBaZgH1XUxgJ3RSXAzWl43qbHrjftCvhyrOcLYxgdw_uMKbXeKm_QWugviLdFDTkg5BVOB3t3-hwT1lSmhtOWd8wdVyexJMQeizvZRDxKEKN26eHcfTBhmVot5SjEgYgqO0oW6fJSWCatanEqy0efG6Z44eOxIIk8GONIP06peaCbw2dWS0dDPx35ddvT02Y80geG2LmCPoWpNSgDiurfhphSRP6Y6uLz31LGKiD9_8p025vTdE8D1hWEG9xyRQBEcPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=ZNmfW73EzrzANSJXrHpeAGB4qRhOU6j1AdQxQ-OOLqgialTXQnVek0x5ufETj6x45URqxic9btPt1JcteHBaZgH1XUxgJ3RSXAzWl43qbHrjftCvhyrOcLYxgdw_uMKbXeKm_QWugviLdFDTkg5BVOB3t3-hwT1lSmhtOWd8wdVyexJMQeizvZRDxKEKN26eHcfTBhmVot5SjEgYgqO0oW6fJSWCatanEqy0efG6Z44eOxIIk8GONIP06peaCbw2dWS0dDPx35ddvT02Y80geG2LmCPoWpNSgDiurfhphSRP6Y6uLz31LGKiD9_8p025vTdE8D1hWEG9xyRQBEcPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سلیقه موسیقی میثاقی آپدیت شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95815" target="_blank">📅 09:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=ievIOJ7gDG3UvVQNH9JCz74xVGuIsUAMXE074Eilg-sm6Znk7yYt9B74WCpol7_buK3mvhmak2NKqfjou_RrRZ5xQtHA2nWQqYyr5r0YlEAa1DC6Fz-U1XW8lvV0rrGaUa6kWR4v8UQ_67vCPz-1qz750r98FguHlELlLG9ym0szum8uqWEE4H1M-BK3XxMj0SW7dFodyYVJlwLsBaDC0vXeAy5R45F1h_DltJiUXWZFJbNI6KEdyYOIXxtuB7UgpIQpdzHvs56p2v9JxV3Wif4itDB4ApUGsBe-oYA2fPGz08rKccSIsKZ__gh2KQdHkskFWxPepTmJnHeeaorhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=ievIOJ7gDG3UvVQNH9JCz74xVGuIsUAMXE074Eilg-sm6Znk7yYt9B74WCpol7_buK3mvhmak2NKqfjou_RrRZ5xQtHA2nWQqYyr5r0YlEAa1DC6Fz-U1XW8lvV0rrGaUa6kWR4v8UQ_67vCPz-1qz750r98FguHlELlLG9ym0szum8uqWEE4H1M-BK3XxMj0SW7dFodyYVJlwLsBaDC0vXeAy5R45F1h_DltJiUXWZFJbNI6KEdyYOIXxtuB7UgpIQpdzHvs56p2v9JxV3Wif4itDB4ApUGsBe-oYA2fPGz08rKccSIsKZ__gh2KQdHkskFWxPepTmJnHeeaorhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🇵🇹
فداکاری ویژه کریس رونالدو در دادن کاشته به نونو مندش و تعریف این ذهنیت از زبان هوگو آلمیدا؛ تیم > فرد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95814" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK-c20qoBUstLKFzhCFZmyx_-PiBcT2nIHBe5dJMQz89ojU0sM9Kp0YkDvQSIMorOd3d4eQTlODkkzJvCwZoAzmnQ5ba0fdbanx3icURxCXOHVEsaVTws3v7GnUwd5DYD1bzkoWgG4a1cYei16cytKlxp-ZhFizrCRIYAOOFJO55LjWC9JW0oWJlaFPh31RHb_27uDhau3Ak8M40ReU6jSFnjeaoMQa-q0LdXlBk04NkNb9XKFwdK_sOizWvIFVj3EQcFAPgJQWCjmUDw8I0JunsuTyekH_Jw1G4QCuT9ctgcChHHvQQ_3oIdigL6H6VXEO6OjOQTqXHaJzD6WGjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار درختی مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95813" target="_blank">📅 08:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7KwjJrNe6pldJjMtTJRdSx51gOj04lqj6ECWRJJE0ax8dJqBgnd6-OHA32MyIfzDdPvz4WfADqpvy_QtkLrQBs9aw4wa4qPoXn6zDHwzkhXUo-GfohVGiv3RQhF-sVVgN7M1e_pVbboISeLlaImjVz2UwmmZmJ-imxMjM-woWMcoPQznm5oco_ViBP7RnrKQEmKawQiAmKCkik18uTKhpn_3745OkECPRzEuh-BqlrxUxP-Wcq4hftcr7WiqmqpY9PEKr2NjmIPuo05DAMs5_URy7w-JPA_KrbYW2T83pohSsftCsY-YRvXLD0kmxGNTd4ke3XMU6pgz59D8LrfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95812" target="_blank">📅 08:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV2QZUEuvfHvYOXYUyvNJQyLQZvj8VJ6kpDaxEfuHFRWs_eAdKG8jodwYLj8e4RJ4p53OJxaDqUNuRm4NcvoiT2bjRoOqqisETxmB1TlKhaNFAuv-sOyBuxvtxPK_UBhxzfdBQLkZditbwpaOZ7WgRs9U-3uYrA61iUsi0Vi2kKGN2CvfiQsjPxppbIUsubY8XaOKEEetRQWeAxr2pXoKNqp6lSuF3N4fN_j-PlhukLIOsFxGD1VDSFO9LNl49-RCKuacm59yKMiEue9RZR29nXFuhFwpr2jkUMpk1riiXIreFyXuY3KJqelCAp8STSRe8fMyC42-9TP1o2hlI_KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95811" target="_blank">📅 08:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پایان نیمه اول بازیای جام‌جهانی</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95810" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
