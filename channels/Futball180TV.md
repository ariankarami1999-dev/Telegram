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
<p>@Futball180TV • 👥 702K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-95851">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/95851" target="_blank">📅 16:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95850">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/95850" target="_blank">📅 16:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95849">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/95849" target="_blank">📅 15:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
جواد حسین‌نژاد از سوال خیابانی هنگ کرد؛ چجوری میتونه اینقدر کسشر بگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/95848" target="_blank">📅 15:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌صحبت‌های زنده‌یاد صدر باید با طلا نوشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95847" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
داستان ریشه عمیق ارتباط صمیمی بین کره‌ای ها و مکزیکی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95846" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دخترای مکزیکی چرا اینطورین، ولشون کنی همشون از توریستای جام جهانی حامله میشن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95845" target="_blank">📅 14:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95844">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95844" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
کار‌جدید حمید سحری به مناسبت تولد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95843" target="_blank">📅 14:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcnPGg3WRnWBWQT9bTrrQ6S0nHnHxjNGzjdjDCGiC_zPHzRu3UFIwq4lgvpuIcLsg3Y98AEKBWCW_Ksz9YCaM_p_WB1gXPOzmmXsVRL7mCFYVm2hQDIbSAFD2nwDl7SwFbJ9nQ_s2VHy_jUItVbAq_Jkj65e043BBXDwBCkjhqvO3nqEihaqAIMGCRFVFRMwB15xt09sSzyN90Xo1u6GOKb02MHztpnzpO2Ogle3VOMymx9jrYI-bQZhz_xBqVGrmx-jVKkNLaZCGCVkXd86eZDHUQxPiii8BZbF_hmpMDSLpfo7wJvI19eD4XCG7bwTDEfAnEUh3-8_D_Fy54jL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le6G32TIdy49JFOV4DqiIOuAAORLXYhju8oJlYCdgv-vmVj_MqAvox-0z1Cu_kD1yU8upuKSODr-LPaS1c-_ubroUtnXNaU1AFvuLo2BhszWNBFHLAhcSi9HlA5kuMICFTWEYtiFCwmX-e4alS9EJApktV74Pj5Y26oOM_XtdJaY9H5cq6jsq1shosQlYKfAu9If8sztktNORI5_13xrNbQIhWSHf0rxiXcYefjSjoBRPEkHk2Nx2sH9dgCB7r43sHGwpzz4c8PHt3b5VqBJNFIOObHmRJ-UcUC4BQ3-i15Eq0W1bOU55yvvyb57btOyEvSOy5hpmjuW1TWWkrUAdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95841" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
😛
سطح اعتماد به نفس بلاگر نچرال وطنی: فوتبالیستا و بازیگرا میان دایرکتم؛ طرف باید ماهی 300 میلیون خرجم کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95840" target="_blank">📅 13:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کریستیانو از این‌شوخیا نکنین
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95839" target="_blank">📅 13:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSSEay9aLRJBlcNXLxghD4JYyAEVf_-Yph5yhHiFbJpWOBCdv4Z-QQbgnZL_kFmb2kXMdMw4E7IXQBEtmqaElU-abzOytKWYYtnqE-QQ3hxG4XXwbQ7Nkm7r8TWxxy4QG6pBVlPAgJIRBJTY8_h2offruFHEtzAz3TnF-UcvAYROv0VbuR7H038cLhxrzkq-KUbH182S9VZw1Gayc2SKsaJPmejrXSVhe9mYpevsF1cevjZYp3t4ZBycw3z-y2vK4aQzic3072Us_37Lzp7eQds_Ve5XDwTeCJyIQBRoMDwWvt-W4OHfDxuAGc6hBOHg7YSDHK1vyWvDaaYmOpCxDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95838" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9Pktg3QtTL8L-RucVMHwe-xhFnTFV76gmfOwqejUCf3tA-3RxBwtod-dX1ZuiwdoHtxSps-nOS0w-3RsdPEkft3Q2ZH5zOK9nuO_X5K7yGAP-JXe_14iVY0ebNEkAdVKWmFYS-MLeiREh-JAtaL91_ANfCswqs_J2kIs01sNAsTlnIX6zyTgs6fc1nirQbxqpSlkDzi6Fh2WI4fd9FAsR31YDQBbPJJGknz8hvjnn_aCpcmwkmGKQQTQeKcjbvUeEZ3CYU-O0FsIO79ErOZJbf8ahMCGB1STrRj77jnFoYFo9cbgrLIEI9gQpz1a-lyiqzSrY1E5_GP7jPO2qOKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب گروه A مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95837" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🇲🇽
هواداران مکزیکی این‌شکلی بعد گل دوم دیشب کشورشون عشق‌حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95836" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95835">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95835" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpTzQAtew7eda9ItDlLtIEd0ZC-VlWJGJaPM5b7tLtCF1_DH2wZzdeLKfCoC52IokkY5G6Cw03T-pI9OgfV3DBhyBrqhhydysM-3yLnFajrs-fTs0s52nOK_uNrAy10zVEhzFyRgQFCsIi7SQdXSlpmfhq56dGqs7sZOjnABzxRT-JD9iLSXdmm6LH_-0ZODHl_yvyBxdpGCx07Qyu3BQQlyN-LqAD2fZJJ_UaGQj1_C-G58xB_U2SktzNzwTHsnHk3qlflLZzNZnS7JdsA9g1QafTkWmEZa1BEGHhO8lmtZB6mzFkEalB1ga8hNgjn_ptnhK7O1xUHsWaMLWmmsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95834" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3soYolMU7XbeBXBrh-yngcOErIPuZdihpDU1gNaHRzEEkrmru5yDV9fE1OA2YD8KDw0dnRk1f08GDVtVhbUSJYnkhgJwSbPIwDv_T2BMEvQ2xF8JxjVInvYS0DBF70fzynY9uHVAL6iZBzAX8lMc8OhBHGwu4ggtTynfwAvAkNoWo3uabGcJey9LGLQ9ZWQVk6KKBTfVItRzxDdA7yijQEqdjTXlRd3NuBpXbOekJIexVtcK4Uc_xc1gQWl1VB7XcYmmAW0oTiBQpvzgK2asrh-ih7d3d_FUZx9itlm-4eLarA7YjN_-mouRCMrYvD-YkFtNvxHNc4KY2gm06nimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95833" target="_blank">📅 13:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🏆
روایتی‌جالب از حضور روانشناس خِبره در اردوی تیم‌ملی برزیل و کادرفنی آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95832" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnUzCoOiZ_Wm0WlS_ubQbMNV2zx9_NlTo7MsA1YBOSTP7X9fqDhJ7lgCglNNPOZJrKcufABGRnJtmHettmkmWmcx6kphsNheVHYJt0HGj0WmT3Oiztw_zo8jDg1W6F9sfoedAOGIrEHljZOI8L3GgU78NI0vp1zkwoq3Uj-RGDtWqgOY7e8NAjlsf5hA7nBGvCT6-Z3z7APdf5_olDyLp3WnTLnWS1QkuR57yCkrlyIjs6O-H1gOgCYiLckeyTonD7WRbQ5NyGueMGZdjNDOIlv26dZRAGIzLE7eAJHpl4j1xMWQIHAzE1-d-7BpJlV5c172c-7yQHOjRPnk_37OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد گل زده رونالدو با مجموع گل‌های ابراهیموویچ و آنری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95831" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcgPq9e26ZKQjMsrt3Mgi3aSmFuf7VkerNQowb1dQnv3CacOZRju0KmUtsIqBE07N1A16B6SiaOwmWi2V78YfnLBv4l3lYwXBKKmTB3jRditNTudAEqUQ9LbAKVCFvExivEPBO9jUP1usaKg2Teijd3DwXLI0ucYFne11ZNr6vGOPYU2NCzbhgDT6tdnP5TniB_Ft4MlEewkzIt-WPuPFI0YFgvrcOHqavx8mdy75ya-R9MvcLCoU-eBlE-hOXBM-tqthl8BWeWU7M2MhAB4379R6vpUDqvYN1Db3LUyq6Bqup7hRd5LV5Rf_mAmZYLc3zGt_-eivh2SmjkaFFi0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
وضعیت سون بعد باخت کره مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95830" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSKnlGGn8UEY3cnEHv2muecKwjrKAGaH6qoCV1_NhgGOjFr-REsJLdiI47lc7085-3nQW85RmdjfBFDmka_LeM4WSRbiMIwTdFQTHb74uNzQaJgJhEd56As7MLWb-CTR4dNJ-dBnKO3MpjXJLaX8j-rSyrD-JsgFu7W06R1TBscMUlBgAPOXkx4nBjrSL0M6nYtTSYTIH-zZ947cSNq5olvWUcrHNh37DsqieUtsNN7xL9ZLyWKvrb2EIWgNt4OwZLkFmnj48IPlasnoBsFagHXjVfbLlQYG59h5uQSX_4EIkjBLAeWYtJ3KcxMudu10rCGakYpdcEJnbRVk16wNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از صحبت‌های اخیر تیری آنری و زلاتان درباره کریستیانو رونالدو، هوادارا تو شبکه‌های اجتماعی میگن این دوتا هنوز از یه سری اتفاقات قدیمی دلخورن و از کریس کینه دارن. بعضیا هم میگن دلیل این حرفا میتونه باخت‌های قدیمشون جلوی رونالدو باشه؛ مثل وقتی رونالدو ۱۹ ساله آرسنالِ آنری رو تو خونه شکست داد و رکورد ۳۲ بازی بدون باختشون رو زد، یا وقتی رونالدو با هت‌تریکش سوئدِ زلاتان رو از جام جهانی ۲۰۱۴ حذف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95829" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
یکی از جذاب‌ترین ویدیو‌های چالش آهنگ شکیرا که میلیون‌ها بازدید خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95828" target="_blank">📅 12:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژروم‌بواتنگ مدافع سابق بایرن‌مونیخ: «مسی باعث شد فکر کنید احمقم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95827" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
امباپه: «کین، هالند، من؟ بهترین لیونل مسی است، همراه با کریستیانو.»
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95826" target="_blank">📅 12:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پیشنهاد جالب و شنیدنی محرم نویدکیا به فیفا
⚽️
@Futball180TV
‼️</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95825" target="_blank">📅 11:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
دوتا تشویق تماشایی که در سراسر جهان ترکونده؛ تشویق ایسلندی یورو ۲۰۱۶ و‌ تشویق نروژی(وایکینگ‌ها) جام‌جهانی۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95824" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1-CzcSQqev5FYaBcaWH7ibHjqiOvrtbGBn1Gt1TkJGtmL4viX2z6olMVUao21lMw2Pl7v_rPAD4TbseARYwD7CNvwNX4KzezcXhGdq1gaeRdFXPzis2LqMBmNkNYjzaIWP3gCS1Hn2Z2fjvMoZppIalOirvHGYQh92_NLUvr5lTilKWnRddtlYDH_thTULLrd9kvrJ9Jeg3UvTSG9B8L5eI5W4Xd777YpTKWUYLNdHWOdZ0kxQomSRwKO5aZMY_AUVnhXrrNqaSZT5nVdseKo9D6BLVrSHxh-Zh5Zgdmelro3mdpS8qODn2UVAJTAtgPlIpFV6dmZYBm3hyhwEczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
پوستر جنجالی فدراسیون والیبال برای بازی امشب مقابل تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95823" target="_blank">📅 10:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qscJ7ue4QUhbuOCp2zF5R761dhyfQI08XYYzO3Oq0hzaxzQGr1i6wVIBfeXwUnZYA4FKXowy7EwmeVzyH1HQQ9laVHvIRlvL-AIoTcM0fU2QsUFtSEzh6O2av79CGLLOGfXrWw4lPkcFmUWufyYXfO92tHHxK1OU9p89FtFqyFDQmyrSg_UmZIM4ZGlHdOZ2rzy2ESdMcGd7p7kVUb2fITKpjE6HKGN8WkWF6rxv1mlKesGQ1hHLEkAT__hut8IQVY2dnSYMAD_v9afBc1QGWwcsiqiMZ30qqtI7t7Gd3boxh49_0JlaGo49PL-3QH63MreRl83A2egdpzv4Sy3jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
🇮🇹
رومانو: رئال‌مادرید به کومو پیشنهاد خرید نیکوپاز به ارزش ۶۰ میلیون یورو را داده که اگر باشگاه ایتالیایی مخالفت کند، رئال مجبور به قبول پیشنهاد سایر باشگاه‌ها برای ستاره جوان آرژانتینی خودش خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95822" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e47Uyqy6kHtY7IHUIHrAHsrBIJEv7jlEBT6I4Kp7cTFyRZF10LpbPFylVXBWS9227bfqqYLHwcVndofEvAYvEfKLLa344TFZ4zin2L78P9YH4Mj7BoedCSvdeTxGReYvU9rP2pTiyE8zl7wXDWY01zB1Pi5SKjD5rQ0t-ycomzr3RrRaoH8rtCSAOLTfRkGLqnQ5OFgKKah6MKBp-oy0-Um_cofO5wpAm8mwa3XJJfJFfIuTj4yVf6fcazQO0dh4qCnlpiBfpOHYPHaeCGpdNSgN3gK-EaUU9AtHQeKxA9CCrYY06EpimrlrSwwRTNlSGyVhGQYFQRlenHDFU7SAVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95821" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-KxdI6NZSBPKRua9yATkB0ZFIbNLgcFE0DxhwOf_vcBQ2xy4mRKmjrtHUo-yX3FKl-7RXcnCpkM9gQx-0TqvE2vZxwayhYvO1HXHwQw8wnHub_VnkkHvg4byxc50bgGvyi8eSOc66CIF_qoVFYeaO1CXqY6aWUvPX8XQj6QF5imwFc-zSKYqjcZCyZIF9oXrCO52LwNrNsG08TeTWpsiCfk4MTPF6pDu1CLwm_4AY833FnHgebGKkacMaU1XLN6we-RHA39xtrtMG6yhQZbfvZn3M6uPxNp6VlqjwI5yq1v6eWQBa87dy-NW3gfZWJwG66fqCBuCz8NHYzTum0NTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95820" target="_blank">📅 10:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grS8NltFdKASdbtUeB-LEooqO6FD_aF6r-BVVJw2QF8QYQv3GNia6LI5PwT1uH8IGaMsu1Zg8ekyhUTtozl2e2kgsV84hzkwFG1Kr2liVMcpYjDtUgYc7iz0RQTsKQ4gv_lCrKuNJYZBSrY0uZN6cY_Hs3Ri1JcYj9sM1icGM9Wx4suuPwLdT_QpTH-xrHzeL0CkTNsVXzcu6yKhBYwQd_wNme5hrVp6VK8hKB0fKwQz_3apgxjihwWLnBZAeW0034vmPF9dIQN_jFoyIOpK9Ne_-mEHOlxYFgGc6Ky-L4Ot6HnW8R4jJVFu2ZXi4ZPzc3q3CTy0BYDtICozzwq4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های لیونل‌مسی و رونالدو در جام‌جهانی به تیم‌های مختلف که ایران هم جزوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95819" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=WVbfjXjbACs-Ogq_b6vj03jvRkla7nvDahsWN_iCVNEJDChkEBefzQJDr5OI7fy8IioWgF_p1jmfu3Gl0xAXIXjqczuNAZfuS_FXohFHfPzAfAbg8Xqzr3Oelo_zE8L2U1J6nmBfEfYfUMCdgWs6FyODe0UJeMzQkn6mjQle__J4VeYu6W2Z8v7c62b6t7zJVsH60aqGUVtZSF8SRRbU99xaUEwshaJLOCtdJm_PJCuoFyjDkf3B4Vkb7vupu6_fVMHRBoVjjlSzN0Nni7IlLb_pxee9CNKa266w7K4mJ1_vaX9GsP0W0OK53TSQsSV21QWj_vTu8zHmhkcfbDI2n515qRhPQ5uEdGu-FKQWqAra1CN4YzMomnc_BAhe8Eo5E5_oVDmbrN9U-qKX0U7uu3Ek7384045LKJqPCM4avs5umg35D6MN5z6tiLv8kWwERIbdttRNE73Biu7DnxiPs5wMaNy63NNSmaOaDS2usx2Ww7Epl8FY0ZkUtt8GSaod67tdt4WOBhyQ4Gj_SiQ_Ksl6maEA1LEF7R02uLGKcj8I3UammAWDMS3EMZ9VZkb1XdmtqzNHYlDTcyQFtTNPaNLnJEStCIfTF19Xh0D7K7UKvgJYUXZnL_lcYnS2yVK6m7bvYiqbrpQp1LBHJyuyPb4_qewGDjd1XC3Xhx0XYXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=WVbfjXjbACs-Ogq_b6vj03jvRkla7nvDahsWN_iCVNEJDChkEBefzQJDr5OI7fy8IioWgF_p1jmfu3Gl0xAXIXjqczuNAZfuS_FXohFHfPzAfAbg8Xqzr3Oelo_zE8L2U1J6nmBfEfYfUMCdgWs6FyODe0UJeMzQkn6mjQle__J4VeYu6W2Z8v7c62b6t7zJVsH60aqGUVtZSF8SRRbU99xaUEwshaJLOCtdJm_PJCuoFyjDkf3B4Vkb7vupu6_fVMHRBoVjjlSzN0Nni7IlLb_pxee9CNKa266w7K4mJ1_vaX9GsP0W0OK53TSQsSV21QWj_vTu8zHmhkcfbDI2n515qRhPQ5uEdGu-FKQWqAra1CN4YzMomnc_BAhe8Eo5E5_oVDmbrN9U-qKX0U7uu3Ek7384045LKJqPCM4avs5umg35D6MN5z6tiLv8kWwERIbdttRNE73Biu7DnxiPs5wMaNy63NNSmaOaDS2usx2Ww7Epl8FY0ZkUtt8GSaod67tdt4WOBhyQ4Gj_SiQ_Ksl6maEA1LEF7R02uLGKcj8I3UammAWDMS3EMZ9VZkb1XdmtqzNHYlDTcyQFtTNPaNLnJEStCIfTF19Xh0D7K7UKvgJYUXZnL_lcYnS2yVK6m7bvYiqbrpQp1LBHJyuyPb4_qewGDjd1XC3Xhx0XYXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
🔥
تشویق وایکینگ‌ها به قائم‌شهر رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95818" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=qxcLWlPBPYUCp9CzaMOTRElt8ain5uUlmvBO0BuuKf7XyPgtVAu8-44o0yJmGzJ58DFfpQbBSGHtGccEH9eLdSUv5MqnAD6DTIn6ifzujdvz0WYWbxWcUQ9TKhO8ye-EnPQoppWLVyPgrql2e9aNKtCYJuMTiM9HS0ED_wOFONZ3MPilcuU4SZicTVcoWgtjgQtvq_6A4gFfjcvNdVqz4eSGOMeGSiFA897sRfu4sPySIEBDz28AcYcDYJiPs17b82r51wUwwt01tQcKuQhuoGmh2TebPqL1zn0GDTvkCQloChM1n8wOmA-uKnTbEYhWqfH-p9qql1FNBx8QTgB7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=qxcLWlPBPYUCp9CzaMOTRElt8ain5uUlmvBO0BuuKf7XyPgtVAu8-44o0yJmGzJ58DFfpQbBSGHtGccEH9eLdSUv5MqnAD6DTIn6ifzujdvz0WYWbxWcUQ9TKhO8ye-EnPQoppWLVyPgrql2e9aNKtCYJuMTiM9HS0ED_wOFONZ3MPilcuU4SZicTVcoWgtjgQtvq_6A4gFfjcvNdVqz4eSGOMeGSiFA897sRfu4sPySIEBDz28AcYcDYJiPs17b82r51wUwwt01tQcKuQhuoGmh2TebPqL1zn0GDTvkCQloChM1n8wOmA-uKnTbEYhWqfH-p9qql1FNBx8QTgB7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لذت دیدن لیونل‌مسی در جوار دوس‌دختر که ما ایرانیا ازش بهره‌مند نیستیم
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95817" target="_blank">📅 10:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=haE_97SEcp6sLlWiuxOdlZBvRwsjdoj64eCATvwLgnPONylAmaHfE5TPB2Or_YbzCkZaYEBbxNCg57G215jpel1McSsnUZgDL7L03mL7y4Xw5B7vTNg1RHOoJN72mdIUgL26hBcE0CkyI-nUgMVs85XfJ17fp3yOc4BgAkk6GCm4O5pU8Jatc4K72XR0fCm_5nFba0JOlrDHdV2E-ZzMPutUTaF4b7aQivTkQ6Hbs1oD3LQNyQKqVI651VtNGuW9yWknm1221qk9VJqBUukoFK-D3OgYo7KB43RSEDtsnjLaXbnS1dJ613FPueGV3gfaRiad3YUUEvkv_MG3PYtSQx63DPK0OI5oiv7WPPReJSQecjwmTpaG_iM8jAzChKiwK3Y46gkX6GY-UbtRxIoeDhMCqSFh8ulkCbhtRcz7FknUJqV8mi3yiexYsFBnHvY63yx3ewR_8qXvN7OCIh_mSZ08go3_D6Lqjjy-1mnpu4Bmg0EZczireO-npv94nY-TIfz3J6kZpf1d5-Fe6nB52AcU_-z9dK4oQ9Ba4UM9TtWF_x34JpHJTQ4xPWc7qBQ-tVT2-vhtgAIRCfT_GAHhaUG6KYtuN_StWqjiXdSL8vf_KGMl9OTZKZMBndmi6fNjrPBHN2bi9-__c5loph_NbvzdDfHSiAcgpEvGVCJpS10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=haE_97SEcp6sLlWiuxOdlZBvRwsjdoj64eCATvwLgnPONylAmaHfE5TPB2Or_YbzCkZaYEBbxNCg57G215jpel1McSsnUZgDL7L03mL7y4Xw5B7vTNg1RHOoJN72mdIUgL26hBcE0CkyI-nUgMVs85XfJ17fp3yOc4BgAkk6GCm4O5pU8Jatc4K72XR0fCm_5nFba0JOlrDHdV2E-ZzMPutUTaF4b7aQivTkQ6Hbs1oD3LQNyQKqVI651VtNGuW9yWknm1221qk9VJqBUukoFK-D3OgYo7KB43RSEDtsnjLaXbnS1dJ613FPueGV3gfaRiad3YUUEvkv_MG3PYtSQx63DPK0OI5oiv7WPPReJSQecjwmTpaG_iM8jAzChKiwK3Y46gkX6GY-UbtRxIoeDhMCqSFh8ulkCbhtRcz7FknUJqV8mi3yiexYsFBnHvY63yx3ewR_8qXvN7OCIh_mSZ08go3_D6Lqjjy-1mnpu4Bmg0EZczireO-npv94nY-TIfz3J6kZpf1d5-Fe6nB52AcU_-z9dK4oQ9Ba4UM9TtWF_x34JpHJTQ4xPWc7qBQ-tVT2-vhtgAIRCfT_GAHhaUG6KYtuN_StWqjiXdSL8vf_KGMl9OTZKZMBndmi6fNjrPBHN2bi9-__c5loph_NbvzdDfHSiAcgpEvGVCJpS10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
خوش‌وبش گرم اندریک و بوسیدن شکم همسرش که بارداره بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95816" target="_blank">📅 09:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=EVRZXGd3H5Qnaco3ANcMrhtTLxLzZFp3nprsR81PvrEMzvO4wPOz-OFH3I9rh1xmboTXyuVBMwJrAjGMVrRjAgBlul2zvMOB2nIEZN413GuJkzy9l68Jd3hwb7SD6cUIn1JvXJR9pyWUgbNJOmDiQZJgtTk0pa-SzihnjZ_UoQ94NNyBuBHp5BiChI2r9RTSCocXrJe7gblLraNcsT9RWItzCYS6JztWjtLUegD7xjpGUcjDLQKkn_Jn_kvTskRauVbKLRkqkjifDjUdBr3AYr406ZM5gM3T9-YtEiuQN2mA_PqyjOytn-kuMrQZAFz0p6REi90sXGl-is9iilH37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=EVRZXGd3H5Qnaco3ANcMrhtTLxLzZFp3nprsR81PvrEMzvO4wPOz-OFH3I9rh1xmboTXyuVBMwJrAjGMVrRjAgBlul2zvMOB2nIEZN413GuJkzy9l68Jd3hwb7SD6cUIn1JvXJR9pyWUgbNJOmDiQZJgtTk0pa-SzihnjZ_UoQ94NNyBuBHp5BiChI2r9RTSCocXrJe7gblLraNcsT9RWItzCYS6JztWjtLUegD7xjpGUcjDLQKkn_Jn_kvTskRauVbKLRkqkjifDjUdBr3AYr406ZM5gM3T9-YtEiuQN2mA_PqyjOytn-kuMrQZAFz0p6REi90sXGl-is9iilH37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سلیقه موسیقی میثاقی آپدیت شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95815" target="_blank">📅 09:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=na9PGCq-qTELb6JEaDlx4zXlAZk_GbYyKmSH9EyGAtR6a2bqnqgioxrczdXTXFEWBetCCVA2oojUVdRgLDAvUtbrwm3w6UZJm-Tt1dj2ftbCgEOyvR9CD3eEKqejHwRbBxdnjQB7S4fE_eRYwfWwyFe8LsVUsSQlKmQqarQs-3Tgv_T4843tZVeEcrlQElXua66XtsiGSKSctk2SWeUfiOmTO8IQNNrEOaySaiycneePm3Up8mAkwEsxfwxdcQ3eVKzZ4ehb4ncgUQ7RK-RhznhfUO43rLPMtmpfpNfKX_F3NgvkonVKCHt_Iopq_hKUQ-fpbt5nNajurWkwHZUuvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=na9PGCq-qTELb6JEaDlx4zXlAZk_GbYyKmSH9EyGAtR6a2bqnqgioxrczdXTXFEWBetCCVA2oojUVdRgLDAvUtbrwm3w6UZJm-Tt1dj2ftbCgEOyvR9CD3eEKqejHwRbBxdnjQB7S4fE_eRYwfWwyFe8LsVUsSQlKmQqarQs-3Tgv_T4843tZVeEcrlQElXua66XtsiGSKSctk2SWeUfiOmTO8IQNNrEOaySaiycneePm3Up8mAkwEsxfwxdcQ3eVKzZ4ehb4ncgUQ7RK-RhznhfUO43rLPMtmpfpNfKX_F3NgvkonVKCHt_Iopq_hKUQ-fpbt5nNajurWkwHZUuvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🇵🇹
فداکاری ویژه کریس رونالدو در دادن کاشته به نونو مندش و تعریف این ذهنیت از زبان هوگو آلمیدا؛ تیم > فرد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95814" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClE41-DjOb6BQTekGmrPBwbsR398Q2Iejw5dYMRGepOlaLrCUWyHjL7VoemwvaZFF7skXi3SSgQbYSdb8Cjs1SlkZNdSgBwqtCnjNlPbNvoVAdnoBALgFVFL2q-YF9h5ZH7qsh6CcxUCQGgU33A-HIDozfG9fOKxN_Qnmr1q4g0yO4rXqOmPFE8mqI-YdXJWEHJaOIwGVF9ZLAt6hYoJYcniGr8NBU65Hi5H0VXcUTfFvsxQsCnZc8Xe08qFCVWxKD0mArEcWiUb72OkFv-uaAR7Gw5Fz8G-5o58uSJIcR_VAJP6OUllQUvEQAZZ-heLx5-tEyuHE-zJBNlqPUNIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار درختی مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95813" target="_blank">📅 08:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZsOvQjeLwxyIw_1jjumWrQ7SbKnGZ6Dnxpyz2J0P2Su2evGXaeXkHBjB2rjzQ_qQ4R7L0mLr6QZzY8_6pnmJKvLxBfIHagJdbObEORnPaIvFD7KXtBaA9JfVUWyLVqFlZtVFxKq0rwo4SAfKeGG2YO4QSbjpDTFSKUH_OENFxZHCZJzrmyCZ_6VxGjKl8Is_3-YkkNhbtPwSjshyHUjJctDWpd0iyzta7SL38cH4iR8XEu10wbIJqy98DEz6n3vsqkXDvB4e1JbF5D3Xt_Ra6s6FlkZgGKVhqC3nmb57wxspGBOu6IN3f5YTSwNRqF6NZiUAIQ0fvH1h3_VZFcooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95812" target="_blank">📅 08:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUB7HqnKAbhLOM4Gy6nUJ8FwP9oXda7A4NXglLzsw8ZTrLpX_t2Q20m6_HUkp2FDOGktici-EYYgzOFHMNKmpi_BVH97nv9AeUgs-n3TftJTyl20RYf6bHNVk8_UY8qU6FnkepB6wuRO1dgT9449AHc4pCF2a6Ll19Wr3WY1E53Qvs3iPnopYoEspDofi9MEm4udDno-oRqzwJUR2uTiBp-dfu3JP_n_l0DZI5PfJa7jDMmd3pA0KRrdS0NXZpd2KQWYV5waZ_QEwj67bEhwiSLmVVdeF7KB6d1AlXY62mz2c6Ui_czPO8XOqH9ebehoZqnRdRf5yYVFIkIwlYu9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95811" target="_blank">📅 08:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پایان نیمه اول بازیای جام‌جهانی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95810" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkMR5g1VExs1Wt99Yrf491dCqpJxBCrPssYX0Pvt5fZK5UZGEJLy_Lznp_kOoU0q7Z9xW9ndVs_rExbY2OaG5HJbrIjZimRm2RkHeby6f8Nm6XTAiIGhAkvxmyUli4jA1va-7uPMtDSHKjH9-Okbyj6fvDEIkT-_ok9LQ5kUk-eLY5ERCjCU9UnHZCHXHPPwQ_npgVLiWQQYq86V7ihlnugmsrvdvlX488lxYt3VK4TleWx-OqBuossR40qCuRFPt1KHwHdaLdYrfryhKzShK2l5hf2gray-RB2VjdKzleimjcUF_-YyXIBrEQK_EbTz3ZqkS0jfj4_wp9LRCWLgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTyYAVBP9twgI8uylpB7wQduEb567xqtCMyd7g-CDUl7bpVLzgdGcXC1Yn5Old8lF9Z5ln5w8leff2I89q0535y5awAyRTWxRHrYzycc-vYJ0YHN0MbRIfcRpBmIc8HPMqlYpcX61WSPIY-VZlzelF7YqkfHs1v-EYezKrQo5hDuaY6N2D9TXmmWNf4gWGFzUDXBQ3eGUDmPDn-x30nfRBHBz9WmwnDdV5z6gKrNshwcspdy3VeGORqKXex9LZOvFISXD58KGAf71WX1J-cJL6mfWvRFohcwyFc5ITBtBuetCvnzFFAEAMkhqmoKypZVvTI5wW4EmeUsCOueuhNUzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
👀
تعداد گل‌ها و پاس‌گل ها در جام جهانی:
🔹
وینیسیوس : 5 گل و 3 پاس گل
🔺
رافینیا : 0 تاثیر گذاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95808" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdKVBSbAElphcIO_X9anNtD28bjAGKYOUK5HdZyXTco_Nd0R6L6BYIZaemFvd3cLUhcbLx2t6v8u51lYW8kQUTEHU_X6idjbj7iQhuI-afQcSGzJkPW2TMKnBjxrQcTXwrZO7T_AkdHLVys4tgUzUgjjuT4jO5eeEpx4kV2-NVWb_uDo-9YZ766jLqQLIYQwtpINLrDqf1Gnkbvntt1zzP-3ol_IrOzR_4tOrQkJvlWs7lRBi9hoGuyRvtoNyl2B6H_Cc8ZdRGyu2AyhZozlXPQxHR3SDjP5-XwNt2JrE1Y0FA4uO2nDK-wqLV5867jEbRx1TpgC3mWMbm8o-yLR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای بوسنی راضی از برد؛ ما هم قطعا از برد بوسنی راضی هستیم
🇧🇦
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95807" target="_blank">📅 04:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95804">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5mZReOFLsF-SDmnkr8MBNff86XGezcqnGVi5o7mHcVyBIOGmEk67kLRdUSv3PmrlLzIobMHmcUp8Hk7d-T_kz6OqQ5qM1XpUCr_gG6t7vVVu35cEvpc8OyPWyAe4kxwAjMVNrFTVOKwxzISfS9-VtnM0udAwa_gLgh4N1FDaYkBaZ6TFphlc2xqObnDmddnbfjWk79uMDXWlvd4IJ5B3_Zn5SXeaTX-gE8dvGXp6anrHRjSuVg045hX0z13qXV-Qot6K9a_PnYX8pcZ2rzJ0a1Dm1VBDD0-poYuaVPELKD7DBKA8OXBEWPUUi0Pdg1WgBcjNme_2DkRM3BqFbOvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBpJIfhDsUPUnoGqbzg5P2B3gtC99XIxnOKRpser8zbP45djWgPzkS5ACnbka5opvczzIhEKcNZfUWXL9O5xmEwm0KuRdr5LsEXay7fJ_I7PoH9z26FvhpJuW4V_hSPC39d6onxjzzz1ORGoOvx5Nn2KqVahmapYRp9bUUg1YHMRtFmaOhb_Vw4I-9ord2cR6E5YST9hOi_21yp5e6oaEMkKEoy-xLa9VCGssoDIufTpH6OgqtUaAFc_9d6mZ8bXeB8VtL3-Ft1d6VGZQLbQGAVdbevgnLYIQY4KIi8ol1LuINcX7PCNqsi15L2U6WJSLhCFHTMzE-z8nQw4nySu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1SmGtdraCDhPpwK9aWrgMtidsCqwkvh_KXi4URMIndNDctu9BvHNd7hkgnEA_VkfdSQWbrXM0asqeAMpIjxsiv0HBSH7g4IvJ0t3AVjiFDUC-pjmIwawD5wvhzzKDViNx7EyUqwnr_XFmmgaw-SFDMSK_6D30ciKtF4i2JC_bO4PYjI1ppmJC7KHWAG-HwPGM_oQ5rMUiBDJz9m8U6HM4scaK8Jy-TsGVBXjGCI9sgN2ZILxqNrDeXawsSwDqeVaC5Q0XuMXB46jEJzANHXQ-pbpqj1sr6vlivQ0eF9v-6W-0ib4ROjsA2ZiGTrxbd3oqx7N9h4meGZNOAygWe9Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشک‌های نیمار بعد از پایان بازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95804" target="_blank">📅 04:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95803">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شروع بازی های آفریقای جنوبی - کره جنوبی و جمهوری چک - مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95803" target="_blank">📅 04:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95802">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BerGDO12uN_sAFvPV1iXkP0w2xhjXmaVZhNu4o1MUEYXtVgE7rRcmvcbLFa5hTC-5fxLnyIiTWhEKFYVEeS3ebzZJJjog9naVWMu_jF-4t-nRjDRkmqe_pfAvxA-cuFLQblWgrZNmP7zcuKgVM0QUrGSeyemYWI1SNvaffDlGDF--BnywmrTH2LrTI3jl0z-55GzMr3Ikn_lB4cv04h3dyIXngLx60IjGYyQsX6RnlFqtel3TFdQkWe4VdTuGtpMsnVpPOjfCioncQzIy_V7BxNcrIA0owbLjV5xLOVxAohDRx1G1DEJBSsht8r05y_kOV1qvuOCAAef_h6oyYUqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس:
من به آنچلوتی قول دادم که یک ضربه سر بزنم و او به من گفت این غیرممکن است و اگر این کار را انجام دهم به من هدیه خواهد داد و الان منتظر هدیه هستم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95802" target="_blank">📅 04:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlSRH_HhjL6gr16LRJeg4JPtWuZYmaTVS7HaCa55ktdnzw1mz42sfMQxZnK78GQk-kcjGuBUKl0_A7hAxcabUS9vSXx7jgQ45wtkW_DljDXlz8CdsCDBLbdm6lcheojzdqBln_qAfmb-2lMcKmbTwn0dxGKX_a6lRTC2fwGaHPkJzby89JQEH1fr0oubsGD-xB0iZGMXSqDU9iZViowVVNnBXiiwGYZap20Ho9Q-MLlTLDq7wSLHziApBS1UatImZhdD58AMW14CGHGqUVPFOGAK7dIMuLGPx7Y4Tz1bRcwF1bnu7rVe6Z-tpv02687CzBZP3H1RimzOipUIZSp56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشنگترین عکسی که امروز میتونید ببینید، نیمار و دختر گوگولیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95801" target="_blank">📅 03:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8jumoAdKryGQRIciE61OcHhpypNbCnCL4cNrnqjSYBp9J_OWz1-qf9nl-gdyhYdIH4ROWt5C9byjJgxFmQmML_ycWWvOWbNXhgl5ZlnWXlnMAzW6AmZy1AvlEsp0mzaTty5TPQJLUiQQLKWNlBuqdKa2nGFJSdcA0rF6AcVixYQo_rh7TWe3y9oWrpO6OmpmD1ZEdrP869rSZdxz-tXTCaJ92vaiacmijGtuem_BGorXKsE-twolyrTEA8SJBX7RBcjq1xuPX9SY7nwu8mvlwkpfTDbwfYo7cX4uppJ8_KiY3vzDogtZXTIf-qkiWwVRrrhd0OEU83DmwndsYFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بوسنی رسما به عنوان بهترین تیم سوم به مرحله یک شانزدهم نهایی جام جهانی راه یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95800" target="_blank">📅 03:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95799">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKMEU5jmMUuymN4zualKtMD9u7Moy27xRzCzlu0Mhvdv_wgDKNpQq63Bgd9HqnY4GXdm23Bz9XbP91AroSj8Vv2HLywruTh3B_FGKxKCV7QJVqUyYqWXLhkHwNnPFh94_ad72Ke8Z6AUY7xUGdsy3dNj216Kp9PO3EGF3KLOuFZyyRKQUEyzEybd16Ogju_YV9b-O0GMAqGPSiDIzxrsudOv9hnDzt-31x49qaYY8qrF6dsOU8bUeCGljjrZPhHhJ59e3KSAdca2eyfXrP1fVQxxShk1zciHJlDezj6COS3WSpTqqRbgvTIDfXrRPLaLZ2sYOdG_2idgBYVKy_zDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوست عزیزی که روی نبردن مراکش با 2 گل یا بیشتر بت زده بود 3.6 میلیون یارو بگا داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95799" target="_blank">📅 03:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95798">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZL6fKiAeJsJy8xZV0ujHSU83EB59KgAoMp_uabPZ-iwgTiZrd3gkemQJZYz3uVWNPIrN8o6TPgMsqtEm4ib-3PUCYWZS0rf9ly9fB00-9gEvbZgSs0BJ5GzLjM2zrYGUfNe8G9mbF4wcTelFLcHD-b3l72fLmtiSYlzkzHuFTFNcf3BUagPikCxL8P044RkIL0if6jM1UrlzNW3hValI1hWM3Ru4paKqxQZd55SxnkWrMSeYpzthCTEp66IrnwXdwjIWLUUVCoxlVXFmzBGzmqdRz1ELTcMMw36f0zrJomuHG4XbgORR1MEjPx0NzLPedpbp2glRqOpIRUn3rQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
نیمار مقابل اسکاتلند تو 15 دقیقه 9 بار توپ لو داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95798" target="_blank">📅 03:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95797">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkflHDD-gLgMtaV1gBhrfuqaKuZRPuvctVTp6ZPXmWgaSol7pwow7h-8aZX8vrUobY-3QCpx49wkNVa9J8F4WvZizAA6jFaDfA7En_F7SbRzkAVhgCxgEITrIG9uvwlcKxbupoZIX2WEAwlVdMCngOHORRKzfLJ-wT93jdAGnUMq_7vkwKIF4s2M94tWXzot-nmoLpVhaMR3yQCY5ZBbzc-6zx2t44f9d9Y02RBD24ogCvqmPSiThIVxgdQuAAnVqLFkb0e1Z5fv_VO9LFudrslx4k3xJA3ljdyESj9DGM7Uf9BZIMIWiiZ878sKsNO6zcf6tVWK-EYGDsL76lRTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم ملی مراکش اولین تیم عربی است که دو بار متوالی به دور دوم جام جهانی راه یافته است.
- جام جهانی 2022
- جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95797" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95796">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuxERI24h_UwEukaqrzITTkjBkWnm3IpKnIzEipECNJ5ZTe1ORpAnnvPV4PAkysNwGqYeutMXfJaFqfXctwCL8Xu-Vbj8cC-0HjllbjkVmceOjC8McbvkcGZwnwagcYRCDFgCnuGB4C4LJxvWIe-qhzIfdYcLMII23wstx6zMdCxAiW2TEzbfc7ARYESmMZBH9rcX11q0hxPpivPt1H7dPkkX4dmW2r5BH5c0McXrPt_KeewLwNryWeRW0PWnckm6YZRlsZNE-3WsN2Ur4o3q-o2_M2mWWMaEkuhc54_c2wp0LeFFg55_yE20NGdGbwSxYmdBj4OhJyc5XINl11W_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس برای سومین بازی متوالی بهترین بازیکن بازی شد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95796" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95795">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLPoHxZBf6Nj34Ku7gLECMwukinAO-SX6BJDIz851mH9ybR9iHEn6LxOalV2fB6DaO5LFDqwqr-ZzAMZtqsxWlBtqjegDZT61VSCux-eWca22Pf2uFjWaPQ4r59BOKq5EZCox_fa2nUUtFfbqlfsccDIWSlD7ISgRuYcq1TsCBxgJH_bxyTH67J-ek8h1kwim75W7EvK7HZ7yEzTjw-GfPHm84WnwvGvVXbk7rWwNVjvRaecXgZfl8E9mZitB7-IXcPqxlY3U9Zs9QbydiPwM-9dCtWOcNBV0paCPQw_lI6xWcl18ipHzWRZ2ZnMNsDu5pcKy9ObrojsJXfh1SlSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه C جام‌جهانی با برزیل و صعود مراکش به عنوان تیم دوم گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95795" target="_blank">📅 03:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95794">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8FXg5a4R5C92l8IPlXvdwPQkMl4rB01CtP5fYw0lRM2jQdHyouxPk1ru1rPLOYwg4ZqzT84tKeoN4cs3F6c-uD7aJ43bxmR95YlDIaYPEffuBhrgvKKW3I1cvAH2o-lV8lFb9BfaXsEDQ07YZ_qTA8qn5Ycvm8NhPIbvO0cXkQclJj8hrrRhbNoaw4KKaBuK38iCefGDbpLddY52MQLw-ekaDKmy0f_8oDuoEndFh36r_b2_BS5n5X0Hh9rGEfjAXCrYo2Js7xSQJ5_DegvQUrRd6o8bj_ChMuuRiRL0VN0M4PE9qtMOKB8vD3HBoZxuvcLvsTzaPOqbvEVJuvv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک مراکش مقابل هائیتیِ حذف شده
🇲🇦
مراکش 4-2
🇭🇹
هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95794" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95793">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtrS4YvI78pT6RTvtKwlQfN7ZkfEkODeCTtjIQeqxbusZVTQNSemxm_F23QlRe_9TAb6s-vk_VC_zyIniXGwoAET7vY8iASroHnXgSar2YUPYS2oI12BRv26pGpJsSSJKWtkVNa63hI7lJPKOsbPefFIBiHYU09sf3yJORPEMPo2YP3EP71RbBxiXl40ZAvzXE3tb41qbh4rKby4QSVtiauGzgQbLK4YAGfRlSAaOcW4UVMAFIKFSd0SldTpbmi8YcfB4qI-9hZKjAbeBJHRRynVGG-ztrj4LPVPkqCnyPrux0kcj8cXszjJwEl0XggRKCHv0oa4E9LtrQwIiIPXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع سلسائو مقابل اسکاتلند و صعود به دور بعدی
🇧🇷
برزیل 3 - 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95793" target="_blank">📅 03:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95792">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwTZQ9LmTM2jX7hV_NnmxBpTK-Aci2ShPMrpxx-W9BZ7qEeLx_FFuzJ7yK7BP1DzWG3_7gkiatYQk1J4dvAd9Be_c8U3TJ_FVewApbF97eSL499gxi5jqMa5DutltfV3Jil1U0SpQvyAoliXvos228Ef5KgaZ7Lp5zRxG3bPxiKeK-ZWvUeYeujdR-6mz-IFm72myYgblkkYJ-mVAKPcNp8_0JzjBiMbKkZazM14esXuxyJjQ07yfGqJjSQG2VmoSMXQ4bvmDbT9gAxrYwBJec6mZR1YAsHWs1aSVU1LA220FMo7HKHd9QDW2CQY2GZ2Cam9gbbDJljNdYccok3Mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برزیل رسما به مرحله یک شانزدهم نهایی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95792" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95791">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95791" target="_blank">📅 03:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95789">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaN7SuOW2MX_OTYhTuORAwhicqI8Qumx0McRsiSNpx_8sDtILgfD14ssPnNh4WwEkJeHPinhtxkrRHuuEv8iBxzZhqiFEVpmbhGk9DGhy6AHdewztNDopADKoje8BJsul4LE26meU2-F-HR0UUvedWEVM1u9m8Cgzq0ijaRzHmFmUmJl2JT6JOWy-bLiXb4GbV21Slp4IK6VxxqVsPykntBXVpBMejwCcw0xvy-eTjvv1MHqaz3af8-54m_Txo0W1QmUEs24i1gJt8EGktuAgQ2a0GV0QlG5D_B58_RqAwQXMSm0Ctru6b9mt-e9RC_aArTEK_UB9cBKtid8yVjO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7m0TkoSAGuQWL_Pxsg3egUs5TybfLf_a_AoRfWF0yd6SC0dO_WtLPz8SRICboiA91ZcicFThw74zqRDY6gjx9gnsC9mEUBPTR2C-r1uVE7N08y1BzzahiFOjAMufC4neh9Y2FbEFXsKfyhEV2afb5mJtZv4G7k5CZaPErtO5uzmCAkiiDYxd400hVf6_wWdvVVEjOA-ySCwbRp7xnnAWfbf9su-zZ54jgv34y_w0MjiTjNdc99FzDBHELFs0KcqQl9GOMJ52bu9qHbtaaHjPsBUSlHX1m7wVlus1w56YSqGkdLp7BESOsh_VI4PsV6nlPrWHsYhMoEeBfh0Zxxy_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🇨🇿
ترکیب رسمی جمهوری‌چک و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95789" target="_blank">📅 03:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M55HhxrMqtiirArd89XjbypjlF1-Y2Z30Y1H6XMeg38Sgu015Eaqx4MG8Fh45kg8d2xr1Kf3MNAGPsKojn4TK1y8V547mI6cqXV1neSJ7rxYKdtYGTTOBgOiRJI0xDKDsSmncEyipGRuKnHU7BnzD-xZvaHl4olmQYG9wqNZF68KAHE_saIfbCbHw555QgLeS3R-sfP6V79argae1yZN3CBwkIonAnkCmNWN_FR5TH4LZCbuMfsklWxPR5XLfpO-hP2VYHW9fGgSjclF9n9I33l50L_iMo1yk4EEFjNNL36D0N_hvv88eoFlWwxvvwYl4_1j6AtLEECbfjy5zA4wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95788" target="_blank">📅 03:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95787" target="_blank">📅 03:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95786">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مراکش چهارمی هم زد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95786" target="_blank">📅 03:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95785">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اندریک افسانه ای هم وارد زمین شد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95785" target="_blank">📅 03:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95784">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم مراکش به هائیتی توسط رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95784" target="_blank">📅 03:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95783">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مراکش سومی هم زد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95783" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95782">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95782" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95780" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیمار بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95779" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95777">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhDEUbmuGMqwFSN0QAGbu6JBkjacnuVqAdV_aNJ_oH8fsXynb8xll3yUeUQGrLtZpPA6EmhlOXsmHE9w-fmi7jfPi8cHddt4ecFSRsatZEiDEAC0HohZSLFCk9tzsBWzwxWJp1FJOuqwY5nmAYszU8o2iZnCeekHpzdaVGV5kKnIPO0tME9JiZ-Mxo-kgYU7AcS1_2SAVAdwfqdLZCj8_t1U7GQGn040W_1GKPPaPPGd9K0W9aDbg5chk5y9fI-sW85YpnPw_iRDFkwe2So0veTxrHurLo1GAlGPhnsp5XRQux_H3Pj5Lwvr1OGRSuysJcyDT4t-F4uSCuqIyJybAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr869GgRIvZZsSgIsxoiMw3UYGyB7RDLY5ccSzp7AGRtz0ZDMJrWwgIxnl01M9X3gOXXLX4iAavAKrLpsIotJuHBq5WNW4NfbEtTziH2TnO7qVBzKvP7KmjMfwVMEATGI-Z610f5L8G32ucDzVRjvCOncdZJf4-AGACFrv7L59K6vCFem7LhAiLyiYsW08i6o3zFa8d_1yQSR8JTyH600tltBfsVv8nyOTqNgxR1rBVflB833-bQ444EmSc0KXCIMreKHLNtTu1-m-J4EDe1ktBl5oGbcPBv2Ym9J01iP1FRwbbtILFfoUim7UDBfXgukODVh1Xx9iB-k9ZWtD3TQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇰🇷
ترکیب رسمی آفریقای جنوبی و کره جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95777" target="_blank">📅 03:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2gOjYMEpzhD1hvl5fR0eKzVn-08qFAdvFrmIeiRGmDUsw1MdXmfMH-osigFfUfdZ6wcBpa2DePSHUIdgLOP8jR-1vYfUSiEiWIcpyxGRhaGFUVAICHUp-ftxWzRN1aovO8Ax6ZPztVVhsepuNd5gxe2m83MvSGpUHfidYIPYjpwRPRDhOP09TIdxU-tJ-m4BqNhVPbOB66_NoWYy1tYOCOb0rvOt3vAS_ve0yj_gSKVpoIqlkJxWrWKO0hwIxUEM70XRavdV_dU0378rhlZwQf5f7WAQ-RLbS2QvqApCxcMWbdHdRvvSSJRz1E2GoViXm3QoYZR8UHVMcatnPGjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرفدارای برزیل تو ورزشگاه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95776" target="_blank">📅 03:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95775">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم برزیل به اسکاتلند توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95775" target="_blank">📅 02:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95774">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کونیااااااا زددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95774" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95773">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برزیلللللل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95773" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگگلگلگل سووووومممم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95772" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=II6IRjY1q15TAQ9znmEQR11rtAATdJEP9SM7libOLT_IfwJuIgm_rJdb69slNbXvkwnyvVfNoS59P7yG1uDS3w67eWa1PfvsMyNgWoL9Nmn5dnep65ZsPeN6e8MoTLUVbv4FXwObkK7Gbye6rn7YEXNNN9zQPuROVKmz433SQ2eQBgXF1RCLQ-NSFTh7M2DbjqZS6HWpVF2IfMIeeJfZFar-sihUowSEIje33txIuET62zYCetq-JUBPMsRHpLi1bLwe2lY8I8yNXpXS8kr0i-PKH2gEoZMhvBIggBTDFh6nxBwCOfF71qFDazEH3gn4DCLZdZTAWdvLqq5vgvxnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=II6IRjY1q15TAQ9znmEQR11rtAATdJEP9SM7libOLT_IfwJuIgm_rJdb69slNbXvkwnyvVfNoS59P7yG1uDS3w67eWa1PfvsMyNgWoL9Nmn5dnep65ZsPeN6e8MoTLUVbv4FXwObkK7Gbye6rn7YEXNNN9zQPuROVKmz433SQ2eQBgXF1RCLQ-NSFTh7M2DbjqZS6HWpVF2IfMIeeJfZFar-sihUowSEIje33txIuET62zYCetq-JUBPMsRHpLi1bLwe2lY8I8yNXpXS8kr0i-PKH2gEoZMhvBIggBTDFh6nxBwCOfF71qFDazEH3gn4DCLZdZTAWdvLqq5vgvxnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشمامممممم زلزله رو ببین ناموسا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95771" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95770">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو کاراکاس ونزوئلا زلزله شدید رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95770" target="_blank">📅 02:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95769">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هوادارای برزیل از آنچلوتی میخوان نیمار رو بازی بده</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95769" target="_blank">📅 02:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95768">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شروع نیمه دوم بازی‌های امشب</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95768" target="_blank">📅 02:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95767">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این آدم فضاییای ما چی شدن؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95767" target="_blank">📅 02:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95766">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl5bypD1w6_3a3oypPGrp1ag-lK5vjFKbR-BmjgXGk1_JMqMXKGs1AbVnG0_7_P0RBtZCNNEakAZWdwQOGcq_XXn2KzR6A1XXYssGqtIscDZhZGcXEHlSEPX1-UDFNEHquQtTLjCUUbQaY4o9AqcRkVkI_XIzJRWIYuc97Xl8Z3bcLdTu31YU7houLxV099wn_6OfKNpsUM3BbNuKYJF-nC7wtXUd_97cQvAYolFCsgrshmaPWi1Wg1rpET9F_qKtTOC7nKHrXyIVOpaIonGAXDRsWmIKw5wZCNVgTYml5SB-ArT6gmC12N7H24a0fznsM-NLXGWdJyQtS59avzrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وینیسیوس جونیور تعداد گل های خود را زیر نظر کارلو آنچلوتی به 97 رساند. بازیکنانی با بیشترین گل‌زده تحت هدایت کارلتو:
‏
🥇
فیلیپو اینزاگی — ۱۶۱ گل
‏
🥈
کریم بنزما — ۱۲۱ گل
‏
🥉
کریستیانو رونالدو — ۱۱۲ گل
‏
😀
آندری شِوچنکو — ۱۰۳ گل
‏
😄
وینیسیوس جونیور — ۹۷ گل
🆕
‏
😃
کاکا — ۹۵ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95766" target="_blank">📅 02:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95765">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1GsT5KdlSz5pGXEpGOY-2zikn34mv3gI-OyLBqDBNjpJ44TmJJw3qf2FxIEdjYF6qSeX-HDkOYvZ4IbzJ3eVwV3vUC7EMMFm0kM-kgwG5-cjjougS3f9pIhvYzzKnjcQ1EbGaKo9YCLvL9Nge5SdmXRxG2g8gppaQmsxj0x1LMM0GaHGNlXmsXH3507A1mhdA9TLQHTlLfWBndmnKHs5xSH6Lw-eMi2WcUbG9em1LV0IV5H5pMcYtIDnDHMcDsqrZb6T2kSFTEc8_TSEaF5fxlXYS_BVRh_zm5JkhfLuFOppU3DFMHdKxIXYLZqsju0gXq6WDjVN7lPDAT1Oe6ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇦
عملکرد درخشان اسماعیل سایباری ستاره تیم مراکش و باشگاه بایرن‌مونیخ در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95765" target="_blank">📅 02:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95764">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osj4otaPrtMnDGdRXP9KLYmr7vLUv5UVeSEGJZQSk1FVequMrkm9PMfIigY3SwCyNIXhNvOSDxiDSWGRSV7yhZz7QCFPRPRFWpt9WRJRgjzzqtatvNzAIdSms1CbsP30DAIpiP-brsHKjNn45b8r4xk6TgVlZjr5sH09Y9KLWmhWi_2mvgELEAhAYMnDk8igqwUzHAMkmOM7Jxh6m12NtPS8miMbNCzhLSkU3YttaeYQbnLhkRv7afobjXcnUe8rUxrOcoO3HPF6guk6Hv3aIW357urzvnNMZ8YgDfxraSwGnQqvCh3_d0iUnRsj2vgJUgQL3Q9DBBDQ9k9wjQOazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس تو جام جهانی 2022:
• 4 بازی
• 1 گل
• 2 پاس گل
وینیسیوس تو جام جهانی 2026:
• 3 بازی
• 4 گل
• 1 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95764" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95763">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95763" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95762">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5cpG0B934jq9RenEyaZNOq5ui-vSCZDdng-TNNnU0wFBkBACdy7tkic_u-eHlo7BZ75iw3dRy_sxSVO7ro2PyJLUXNAXJrlHQo3dKDjbcRbHLUm-M1Tf0hkiGA1m2OvJO-gAKdO3R9llL81zgqtGZS91AaYAhK7NEyKUGvetgYAGjJmEgER5DAUJwYZ7GMH4rm6q8dtNcoIAU_hA301PmKrlzH8LdT6UdX3ftH1rmq9l56PeTXV4DNTHuFKwMPhsH2_7XNDb5SHKYjk-DiQtX28qGZylGxOnbWpK9cj_BOO-BtGW54Tfy44f59q1gxHpO4Rhs-M0I5DzIHuWqj-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95762" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95761">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پایان دو بازی در نیمه اول
🇧🇷
برزیل 2 -
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند 0
🇲🇦
مراکش 2 -
🇭🇹
هائیتی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95761" target="_blank">📅 02:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95760">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم برزیل به اسکاتلند توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95760" target="_blank">📅 02:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95759">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95759" target="_blank">📅 02:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95758">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وینیسیوس دبل کرد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95758" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95757">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برزیل دومی زد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95757" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95756">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95756" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95755">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=eq3TcCPDphsmn6-bD2s5JGOmRNlV3jZ8FInl03jPWYojE-8iFk52L_-vulYn3mugB6IQlcu2SCgYO0XAfoNIPTS_RjHfnppKYz0dSHFaFaxHhO41gRwtd0zAOOtiMwwsG6a2frIlagk0P6wNUxeBAAha-AI8vf3F-e8hz_Z8T7c_TOihs32rME6C7KugJ73lAkTnh6bBeho09d79NkBia_QYAngvaQ9IIDzJjaSp93zTUP4Eh4AIY55VDQooNGMWLqOi-iRPwbPGha1LlbDLPm4JBKV5MSGXV_fAcLng9YMecHlI61qakfNwoC9IUaC4HR3Gu4Yi6-t26UbhlBAa4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=eq3TcCPDphsmn6-bD2s5JGOmRNlV3jZ8FInl03jPWYojE-8iFk52L_-vulYn3mugB6IQlcu2SCgYO0XAfoNIPTS_RjHfnppKYz0dSHFaFaxHhO41gRwtd0zAOOtiMwwsG6a2frIlagk0P6wNUxeBAAha-AI8vf3F-e8hz_Z8T7c_TOihs32rME6C7KugJ73lAkTnh6bBeho09d79NkBia_QYAngvaQ9IIDzJjaSp93zTUP4Eh4AIY55VDQooNGMWLqOi-iRPwbPGha1LlbDLPm4JBKV5MSGXV_fAcLng9YMecHlI61qakfNwoC9IUaC4HR3Gu4Yi6-t26UbhlBAa4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل هائیتی به مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95755" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95750">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مراکش دومی رو زد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95750" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95749" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95748">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عجب گلی بود جزو بهترینهای جام‌جهانی تا این لحظه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95748" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95747">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هائیتی دومی هم زد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95747" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95746">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95746" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95745">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=u89KZ7oVeEP6-4uT-fC5uQ-vBd0O3Za7rQ1rQgmVg_Zbemc6zk8MDnMSD8EcTRCwK48pvnXYJr4_O8run5bAb2yZkgCXkyaueHf8E_MbuWDe9vTf571odsQwc3f64-Mw-aQx4ervB1ecYCIyyEuUu0c_TwVVZ3df47QC1fymgyG7bWa7Ua5sB3gB_5DbL2eDWcyhsx3QnQ2ReU72b-sHC6yrQLBsrFu6aDjhGSr5Glbba8P154ESERngjJ5V_Pnwq269lxGdpqzhYcksFp6UzFXgio4yyJkx95zg8jhyHmtdH2OxOPLHxhdOu15hlhDor3zUtYWrfH7E93oTNVeP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=u89KZ7oVeEP6-4uT-fC5uQ-vBd0O3Za7rQ1rQgmVg_Zbemc6zk8MDnMSD8EcTRCwK48pvnXYJr4_O8run5bAb2yZkgCXkyaueHf8E_MbuWDe9vTf571odsQwc3f64-Mw-aQx4ervB1ecYCIyyEuUu0c_TwVVZ3df47QC1fymgyG7bWa7Ua5sB3gB_5DbL2eDWcyhsx3QnQ2ReU72b-sHC6yrQLBsrFu6aDjhGSr5Glbba8P154ESERngjJ5V_Pnwq269lxGdpqzhYcksFp6UzFXgio4yyJkx95zg8jhyHmtdH2OxOPLHxhdOu15hlhDor3zUtYWrfH7E93oTNVeP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به هائیتی توسط حکیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95745" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95744">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واقعا من واس همین کصشعرای این خانمه بیدار موندم بازیو ببینم اونم با ترس و اضطراب
😑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95744" target="_blank">📅 02:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95743">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مراکش گل مساوی رو زد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95743" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95742">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95742" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95741">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95741" target="_blank">📅 01:56 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
