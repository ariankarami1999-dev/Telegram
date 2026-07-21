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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 547K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 18:01:04</div>
<hr>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ba1VhD2iGzdlO0CD2YXypc_nsdiiCJkbqjPBecIb8SqS7tOpEuJPTnp3wgX65BSqQ27s6tfe5i6GOlNniG0pCuVgegRWvWV3pfzXTqiEgU66ULRTSSCh9j6uowFPlbmGJj0c3f0KyVDcvhqzQP2VQjmmfLoEK-ZOjbBPHQYK-790a745viBQXxwiqjol6PiL6pGtGfPVRx4pODBUd8O-fQjJPdBae-Q07nfe60mxdJLF5Cbn4yHs5dAIxZVHngWSL9c14UTsYw6GFOcJEanoekqeD06oy4iQXs1IfQ2ButBirZhuJX8T3zFPB9Orheo9_ch0wf2Me4bd1OsPDhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KWVnA2YIXGLDdul_ADCdunqTzLBt9jB3D0TxtkkTMD_UPRLSPSWkhwCRY_yhOhMLlnnntw_qG-IZJQBzUFFucZzVSzaFDqVk65P3v4RX9rwZxzBm0PK3RnPgO74nZRRY7l8cGCG0N4r2p-Nm7fOq0d3jLn-Tl9bijbJsqx7vHsu0B-0v_wRQSkTvxH3b2Jw3eFJvtQy03jR7rH35W4F0JLERajZsyni65AWSFR9X8-54ju3xzX-utwGHZUIAgEL9a1yJnWKxoTWDxqvENlAwEjf5tPYonsgZjDwp8k7wpDHrNgrRtcQCjM9UBanlX9k3PoYgWJfV83TiBsWXCq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJXjEuvfUFYWQIHhVj8Ev5JHBDfNBboq88zrHouifXYhGtT-qvZMVUtzmLPIgBMcVx0Off45NJGfsUQ3bKgK0KT40E5UmT_UfqKquOoWSBp2zTw-gplGoeCb1KlF8-W6lNd-wdCeK9UxbOgrUVG3wkCZTvXiQeIk0BUV1HJCyt284yd8DY4NErdz3R7k3dkIjmQIwwcf7xsMOeu88XrPEIpasN6GRmBumblO7R3GZRCV-Iv8R5EUWcChgl9R7kiAdxclbHYf68yOxSW-0Zcvqe4OaPHYkm0ZlP9bmpWE2Lv8LMlkhkpWcDdN7uIU4hp5H9HZj0RqhyMzOFXJ2nrgeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=Dhy_QojMM-bbyXnz4qVLA3ZNPFKBPmX3k4YigPBLXG6lhlq6FB9rYSWyB6uOP-sbnS4HDtxj24LUgyTnx3LIEXhz9TNBGFikDXQeEeCdANyL9oi_NfxGWM-y_6XoFLeZfkXYG2Sm5S2CF3c1RXcmiDt2kT4KS2JHag0lg27jeSQWijLYJXb9XBhEZLnuxWTJBXOodf4dgq7XCPF8rLOwwfYzlYYXYq3ltxaTdNADEH_NWchyrBBvbbAaPAZTT0hlCZHGqovK9k98UrZA0nEd0zczvuKus7jt9zSV47h-EhUgj9bk1yNU2oMeR6e39_jGB0IwnEpJHAC91mfhIk28BwaTGbv4DhUK-Hf6PkNIeYUON3fYdU-flYl4Ebfdz1zJvSG3K5kSon4fRwY4JaOCA1bGcKBSMXWqXhXecA1uA2CFjwGerh-xOkKpW8KdCsh2m96-XMBF1Gs7N8uSy8MomRarynvFdj7Te2ZTecDW32Epb0mTAiU6kRgWeyQawjsDeQB7ycov_tbbCeIPFUkIZXZ9L3CMSpRX2wjKZReaFHsVmUPyCiONYJIb3X1odGRQ_S51Tr6VJD7qYMXz3ch65sg6Jv06R4hSLUN-rfWM7CXh3a_D12isgc1-DIDLXE9rGJt_3xpkAgMPtsYNqewibF35NBmQXvYnILLyusw_3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHa0-ytl43CERasALwFNTAu6l6omzO4n187rfEC1vd5UDkheI31FC8VFWqk_rPfcfjuZrOBZyx9CCpo0i8QohN9Gs-pvNyQjLiDiUp_urBNJnOKZNkUwmzUtZjYL8bGSkuemrY0UU5V2bTomZptcRJebEkMNy-VBOu5lTZIq32UiUY-BwwBnooP2hyLWyxNdHhP3gbJ-uou1H3k4fSrRvQU_QAcBSfKhGdRgcKJtUP58YUYOzw_vIUz6WoSUsOGxvTtNNm0SwI5lQezIEV_l6ezkf2UVJIYTuwFz1Bx9wWLhRohiToYxzl2L_S0vopUB1ZT9ZzrDoVz_43t5kH3djIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=U7BYIXwL8-mrF0ClEwTNC_0TAxhf74-GR7XovpHtl1bHBHOoiacdS3zc8PKntpmoIYaBIEfQCka5P49RNi3flv9-t02_ZuwVluea70g0MhfeXlUmmbd6bg_7aKft23Yf9c6Hs0LWT9Wanq9ay3ZQKfQVg4NX15wnZPQuTqyzQF9Xgn0HpqNonzpY2C1_4P0GIcioRAYw_7b3wwVrSj43jS2IhJo42Gp9D3WLT2_nSJkBl7MKZIkJJJsDua5y_CpliU-OiE-34eoYMWAnFIb0LW5-ubvJUY27fHz58vrEkxZ4-GaBlCY7MGz8x1D4tlbA_E2AqCKzSk058bMDUhf-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=i5OebZxyyO0q7df_tkXi6mKn5YqSODP7kiry4jUR3aR_yw7Ax0hcrhzmnRjv2heQMY4XoNk59Guf6mC9EGPbfwdzMyCLDOcQk8MtdsdV5HV5dlQ4PyD0ZxnMFq8mf9oC1iwVk3FiKtbQ-16jd_zdcWM0_32eyNpZBiPFvmhtwBNNA0WeDSMVhyFAGP5edg3Q1iaRhAmpE49pHbZ4Xp1iQLbz-Mulv4zgILQS8iMR7i3wZxglYdko8MhzC0RGdYRpjTsH_AWmxm0d64TRyNDUq8f_aPUIN1-aEEzIbG5XpzMnzVQL4UPdiS-fb7NpQfXrER3qaU5Ng9L5TDbWnealKiNQ2vppX1JDhquMAAT4SQzuzVuqHyS00R39aTqBGlZyhPwck18F2Xm0X1imHZ5k4EtgxHTHCLOO9u1eHrAZtE6GoLZOAggSNyStrWWYNim6ZkIoWEpyCLk9TcC8ZyD7sa08uTxhg26STXMFeivxUhPLn5R2fzG5ao80RRVGq2XswUknrOfgJNsr0fHR_U53xrD5WTddUIpvPu7V3pck8l1s1NA-VQXEmTF0CQcE9GZUEftdCoWM6vQrwAfU-Z5KYK1-r-GOPx9fyib2c7APOu07CNs0hs9gCs9lc45fj5SgeoVsYQSuXeU_ao3HVx96rWHivDBBMiUw6I_s--dOZqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=pABTumjlXpsFqnvM1gJ9kr2JFxo6mrQkEgQJGflvqZ1Z09xsIN0ZU6O7r497VEwMETkg5dUVIbDW823pNxqbB1fnRSY4csSG8JvbIh731JL4czxID-1CsA_sw-Nrzlx7GUFugRrGs1rkDLq9VwREpEksO2TvjnUQw7ibntfxFGs167_w6JjoE7ZFKf72n3byehjUnvs2DiOgM_XslnRu3uRGML-3mxtvN65abI3em8gz6T3VVYgr5G5RTidtDFw46izm2_xS3UpUCr_ogT2j6qsKPnz65RSdUTA2KbQZbjetqZosvwJQ241nSVhRNkfrZAKr8nsaJSE931_536U8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=cg4x7QiQsbU5ZNP1o6UzNyC-3OeIrTYZR4D0z_w9pLsQqcvXsMt3wJENNSR_2Onjy4VjipUGM2zT9xQTprp93bQHZ4rKxdMjLBFR2dIM2dzfX4yJlbd90BLkxfcTNbQHHc4khBPwghn5minTzotPM4X9WlaKJkjyaunjeMU-RMKuUo1EsGsqltcPf70hVp7TdOkgsmbdGaJB5lEVLOhZfYzCmROrpQysAB-qqprKpWOsAaN7NKcMrojAMVpenbG46X9jj5cgIjwIipigX5usCQ3kMX4GAJuULKE7cqWfZWSIbxquE36hnr5vIWVDyfewQZPKCLt3RqTuhxtSQmUHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFCG6Rq6nSAuPypwT7GBC8ye_4xeWvPSlyhQGOhtrqf0SzzxlIphZeT0xaos3vjcH-sIw5Q3-b2M7d9rJyT2PSsg7zkLszv_WviL43HiBUVmb7RDiDNWeD-xKJAzHW5IvlIX3oFYokb12TkHxuZRvufcOt9UMPPJvLTTDcXi9y_yfMIIVY_a7iCImKVTSVdoL9Px925UNj4NsfpzmgSZ4Iv0DdyD0-FsJk8q9B69bUPxEmEVwzhGjmtEJIYli0aA6gNgqft5WedysFCLer7sBvn-QAYKXpRSQD3j2bphbT5whBURxXbi0O06SgI-u1AbbGahXwRa8M6w2ac8eivGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uDI1Uudgsc9Ocf5KY5XyGywTV4hIMcqecjyzXtSVnSHpO0IOMMPGutRRJvHjxH53fn6P-KOROSu4kE9r819gjNG7_NEUFDJQVLka2IGQ6mzXj2h9iO_2H-bCp6v10UhzXfr8SREzwsFMSuhENLJMiCn0N2keSvupQHZ6S_BS-vpajcwE_V35sgTdJHwe21MWTAIf2jksGL8-YVoZZ9SrsWSxcYWJ_XS183a89Gn2OEoWBWww-BclRQ2XI7VgcTbyXizVe3owzfO9ljQzA8RTkrlDbjImvIEyy41dkUDL16zLELwBpUwfIt66EySJoh34wjEtxYjYvgfjkZ_I3iWVWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIL7gNGbDwzmImp7suZtqYlRlko1REKrZ2qexoMTVQZf_jtgegF3H9_WeawGXeOA4zd5QZ7BtosYxbygHVjWQIWjwYcsJTNr6a8M_3-Bdr2_wWEdVZTWkIjqNgXkMaAluCEJtNQIJN91S9c4N2-qCHtCR6v8NEPPfgo7y7Pv_1SaPsib7_8_iGS7T3pf4BMUl73NOMoEiTQUzF5PvVciI_jKxNS-omFtmk9N_o1k8cS7iVXwbA1gicipYaIX6UEXj-x0scf01cC1TFsskzlSz8bjhpPmv91YZ-f3XZcg2mIWKs4yx7UNPBoBlIdi6cMfr3dYS7nXGj852n57h894rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=BwrFby8CsjapsrwkAuY2nrVFRjutI1tgw5yzjMGjn5EsrhAm3T9FqKEo8kbUAZdF2gRSkKjZJRxHSWmEEUNMHhR7EhfBHTDEyvj_ujjdFKQA0S3yL-6di4BaHutC1Sui-yckc6-6AAnGW9Ujm8Bc_Se6-0OWVdqFZ04iRl3pPUH3UQ5QaPLT5cgBFCirOUeOBYCiiZkXmyOubrsfetnd-cQeo43aEVZKJFquWLOaVUvC8f-TXDSycgCsXQRXayLP0Luhl1SN3KnBkOlOYwMoM5xMHtbtkOxlbyoWTE7_MAM2YL-YrjCc7VXg3ekFRzxpoGpP2p3PzfZZ9mRbh-Tzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101445">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YeiiLTyWmaH4X-4Pp40TK58SvpC1FwYmasRiL5vky26KBl1VHSRAZgoWJc4Iqn76iFh0Malplc4jxOSJE7V7kWgpZNAhCbRKn0-HnGPa2g_Au64Jo4f4AuyXtUDVggmOyCDLuJgYTu5athBfloyKWLwPxhpVHAsx_GhsdULAqgsQyfZzftQS_gnULgNJ4c8_ZBzW6LmHR1NJCRhJdlVhtN1Wk1kxnatV5QDpG4QTIVffGwkdege6sQluIvcR7gDFoMc_oNZn6MhEUqZEy5os-4lOHqzIWx0fsR2WssppZDWiEpSuTupAxtCioYLrKSN6qP0P_Kak3Y1R6ZcB8xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
تعطیلات تابستانی رافینیا و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101445" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hag7ki8B7t2PcGfpUqBZEPw0VwcwqlTlF-5lZUEqtoJGyqVAYAe9JgnLhDUZ5n4OkL0REOS0aa4_qgptFdEyI30e4sZTdSIKLwGs98vRnAv9_ykjKjqp1e9pMqRQUrhziZV_XxdkZbCUuD3a48pEIBm6_Hq4x5htGQvjbXuMqwZBqTUW0dTtOcVFfSDZMvpYaNRpXA48EY5H7UADXYBrlcrVNSFS3Cu-5a4h8oWN_ua_O8CW_gV6aTw8jM7AW5IjFde_7v-EoE6KXqD7Z4fjczRNt-NOTLzI_huNpRG20HGNeMGba5KjzJhL5hfunxfr0Y2qXbBfQ9q50jte8rH8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD6oYlT3Nm_lBiTb6btSHhjodKvsPH81tp089KsqiccI9hDIPn5GlgGqYcHWmlZnSB4fxhqrNIV-CVmH90GdWq4zJMOL0r5YmG4P22J9n3R0VZgcpHOfM4entr2hHY98sNplSxitIjE7ukpErU9dsY3gGx9USPlE7kM2zhR0TmPse4S4vSPm7kXCpMcueaRdOxsHXd6XDqvZRopp1Rb_Dyg-H50EchSvIGuY9EvMO4yq3VHe3b9B768yRlWXvPqePzlBC_E7rD1Su8qnGmfdb9kjnviokLDHe2F45A6cN8An9t43BmM-FIiSNtwxW0NCkgbLr9c-VKrypIwaqLquUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eouL5Z5Ji27Gig83aBAXLqQlDbOp6aX9g_GBsmtoHx7x5cWxj46B35nC043M9pSANAHb5CAsRYoqzPdY32MfyfafYAgJyk1BycTw1IW1V5Pdm3-77MLHf3oQzhEVEfz_Zl9h_AmjPUp4RoEhyhkvh0vTfd3OW4zJV0Ku1ieoImgpc-VNIOMQWRFY3lnAw3gpWYg2BHj_AfaVLfRCvpwhHTJJDPLl8cUCcs4dRv9Fkk1N7Crih4dDzdTRbHxfbu4Ql9s27vplSH9-G5CZVe00fvLa13UAUdP5nkP54NLtmNyvX3e_KdoHpP7cLYyXXZ2wFbKOaQf6QW2PS2GBszq0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7wpS2OZL6i2F0a0rfSOnjmHDXz6ZRHxYIkxEkVKOxMhGtngEm9eumt6RN91AAD4ikPB_Q_KNczWE1am24UjrfN4a1iW4DPV8dMUaBTP9zbEGeWp0ey8m0MqokPVBgpI-jkkxngRR3bPOi1GwNjtRbT0yHxrOrDvNN-V9Kwasfjwxy6OKrOFkRBasTbZqH3sm6EO0j9DGUl3RpFfapWpqSMuc770YpO6tUqt3oejTOwlyPF5xX9Fxw-PdU3jl2D_h_KCaNhWWhEYyGGc-OZux9yttV12jpFDqe1hCg2EwDcJHVIBfB3oza6wldwpOf9NNPjcy0mus-kyrimlqI8TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b01qnqpWiSJtGe76zuSFxho60ebc_nIlXhWIjxd_nJbgBMCSQRZAIgUik5NBuN98xkbMr8IEd-28p6ZiLYzd43Oys7zItVN4wfNgLxuLEvdIT4cT-C75fImpDeRv_6gDRIsKV5H-dl7_JZbpMWXz2la_kkH_aZy93vHUOJ1cj09KVneQbThACrmOSiNpqwVcbUCFW3xhwnvZnM4KZvV5SZawC-MZHgw6EQnESuzbXD40Bn7tKTmEgUYSQgy8n0r5tXwK-QEuvD5Xl9VuoZ5shbYaqnQPcm9cxKUpQ_FDYf__yZMsmxQnhvgeaQLRs7pVQIJ4_i6sdPU8oFmYkwyMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rJE5AzDhndZeZsdo3Zcps67huw-S_idOX0pknW8fO5qgHFkWKpA7JDaPbUq3bIQn7cLlG9V-2QA21zoJMJYR7D62ZodnRvvJOQRn0VWRR3nDzqRwFrLwE--8yKnfIXyJgXtB7QLr6g8IA1WFVnRL1hFnXZ6v8ukdt5N4l2afmcRTJbLLr__jsC2bu48lgnqlvbSQhnSjhNUTEScaCTaFB8KchhMdgPm8g32VGVce1YNTQuRrhn_YATGDEgeAWJLs_1C5rTUT69RqZ-slTV6W_AWBWuG_SxoZ8f7t53V4I1sk7YB_PZ5um_0O1bSe7LPrjXZimX4gAdaLqR4b5NQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co-DkvzbSi9KWK-ZQknG6a5UHIQI0HNYlFbZlEFBYuzBNJ0HxNED3AUfO6-QjEmrpXuRL0yJDHyksx26D2AkSRLN_PhWoGzrMoUjYP5ZTR0ADuPSNrKS3mh2urJGUAlsQxuObpZlRQjObZeZtUgsAs0tHw-vKfsGb5qBci30CDsBC0VhoBX6QnZlAelWL0IxK3blcTtdg9t6BEQFIAMu52MWYWa7LbYSJmR_u7LjPyqEkFgJWA7Amq-f4ggESJkYB1xa538FHezwC-0aLLzvl7HGDP2Nl0x3__Y4_D0zOlHo9I2soc60xzT-2Mnzo5c9asR1EQZh9gncJbWmUPvI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfTeh8xssZa_5JIwUYX8sfGCVkn95cn-wQKEI1TH0sIfLUPBK0Qh-YFIybDFbOYNxmZv2ZfMy21JxONU7LyQscziPilL3h1wfp2vpDYYg32ftq1jXDFfOgUqw74hHtjH9lQKYndOnjFe1hGsdpeLWU_RzwvsyMb3XIbbL2-VO9-mEVi_cpy8avdrlh2Tp-GHWznvIQZtcoBpv3PPrYYMR1eNv-nVH1TTYn_xspSK0Hk6GQmPgasx7YcCLH0oGgfOfRG6eWRzLtNZq0fLZVT0suWSZxP3D_HOdp-3P0Np-HuJrHMOwVObcpDM4S6UkOsFB1ZBXvhQ9fgYx-y-KyEjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9zJaAB_OUQZX-Jd1SuPvXJMB0uZu55UPsfroDntnbcn6uWgZH-zE_gTQOcQpA96Rbcu6ACl-SRoDIkUI9qRWkxs0QvSM2e3Q12kmsotslt5l9Xd2ELuLXmskT84koqaBRCRmarBS5hN44lXe39zRq0WC3UUOPIuzaSLAHBuTk2jcfvxZWEgP-cbUl5TOFcZgDZxjTiuDfi6rcnlCEom1JK77kfIHOLeHE9H7zrhLtQUr-4ERP4grhF9xgGZqQl2NJvJKWx0Ub4fgt2aCG1JsEgGz8aBnsd2f4nrac-Te6Xqp3s61dtOBPkE7CL_FXtnknfb94gI5IEkee14TXLtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfPbzucTC6EWk_j21DEQMrrG2FmQ4irsRRTqDFBJ9HJCxVCx-m-ij442a1_s5q87juU3XJqi6oK8MA8gdO48TTQ5fSwbeJ4n2Gqgs_rDPWtCnDs5pT0Ja25L5yXiomUR661wi6z-1awR7oydY-nXVqAD6eO2AQTA2kaLlwzLM4nnordTDfaFeCdq_SocdL5fZo3L4QK0yg7zHkOIpekeSmz3UCtJ8jKcgNVPzL8FohELk6c9FwUJaSvqbUaVeOfDGsLaMGpEYQpxTPNHOl3svudyKFviAMNLqJXtm1yrvyszty2PzPw9XlH_aH8Nii1xWvgNf7s_yEReqpOAiyWBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmrASAEMMOE57-9eYd8SduNq7yfzy5oyHnCcutbhvCjdfGYLfmBFF5oKR6-UlV1AMEe1s3_qmuwDTpPJjBigT4an4W1Co3RxiWT1boxNaFniBwcXyqvJcwOVSrrRcP5UDW4g1MzjE9DxWowK1Q-udhbm29jvw_WeYHQr69heehnrup-zZLUiqf_Zt42CSbdt90ttQ_XDV1MJrs1kXLBN1FfNd35CNfe60uOGKLLQZoVkfEoRwZMshMSvmWUfGVbLrd-OYfSX8GSKoASgnNzW3LapFCn4d5zKOR3Hy4C1dnNNuZTs7_v6WkA1anONqKi36BsbOVUuZ8_Sqz_g9gBZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/On3EXAHguG5Dg_Sm9SvYA7fkBSYc3BR5oKrTlwV7CiVOYxxNCbRDgmHpK2zu_iMnFu6fmlSmyPj2NGTa47g_H5EYEjcVPPR-sXy7ZQ0I_x96WDOsxdQQMryOKusefEFhM7cjZSfiM_yF2SGhG6OsRarG-jbuPdBZgcZI4mdMBi4izupzDkG-mzbPZPmnp5IO8_1zT4-92jr6il9eVePB-V_m_Wvhj9C1UOAIfKRP82Cr6H3EeNX6PQGFwQjOoF5_Io5o7eMr-lwY39FeYAMcaRid8_WIDhZmVgxxh4pmVNnR51ty63RiXZ4sLZpMx1EfcXOX4o7b1WWRyX2nubCDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMnvsXzBBEb9KpUvDCCj0vkNia1CiRc8a5efMVGZzvC0jh6vDYC-SemspudFPbYp7X_jtmqxHjv5rlmcdkswoQfi7W1X6BY8O5F9LGnva7ADQxznhqZuvIlcr4_cnkyUAxXT1F8gTchW0-q1cG--FFTrRIoA4Mvl8xvfWOXS-NvHCOL4a7iEX9_cEowQNGhRmlCEpA5k1kmnkDBxo02XiwqYU0_N04nj7eRTxbrxo4rdrcp1PJjnQDD9Lppz9QhzY4yroUEYrVMavKhCzMBltD5FoQIz_fL7lQoEWGKsDZwSF7_obISzpRLvDU1nDI-cenX6IvInjWlvkvLFVNRn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8fYHrtYVviBeGjJopBai7LbxG0f7FU9jZZxiSqmqRj3-0yBogThxVuY9oVHUS0gaFOXTqK9RRNxOh_1xti0jGbs22bQqAfGjwyauIwbKOu9HQElUpV4j6zdo9RiLqvPNmYZretvBfJgptli1a75NwyJ9oChNKwQii6haquDhKt6qLvYEm_JMlT_F1VbTBdO4tY_bJCJeCH-RlIACOGtqCL9QeeiFo1PuPWv9Uo1YdgUFNsiXuGoKuSfmqXoV8HQBmiGp8EfpjA5PD-hENvHpH_Gyi-k7x9_mOkmqlJIozyldUuWejITtSaNnNjXdULtvBwgvb3efflCUapjKB156A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2kiGjt8ezf7JwDyozsp6_WCSvSnEc0EnOby7mXIrObXYAQTwqa_aBXHyynI5jmVQRkHcUL-r9GCtERtv0-rMxrq34Ue7bmO9E_zRbufbUeXNK5hQxYAIfDhoASXBcATOu9OD56fHPlFirjUFZx6u_wmnagtqIAPRFLvKhT-8J8JIojzxl5MNYRW4OKMDVf4NWznVA-Tbc4uj3pR_cGftoxA_Q6NtxwBzIqXkDu797JiSvU6TvMrNgJWHSabgotRt4gjN_tfCADxYjZ4vsOfc_qjhHzA4sNp_ngwFmHW1hpAUkyX1avVM87zjR_PmhyhuUsdjq1ahNb0KG6tviV4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101419" target="_blank">📅 11:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پایان‌یک‌عصر طلایی از سه‌اسطوره تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101418" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تک‌تیرانداز‌های مت‌لایف برای تامین امنیت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101417" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhE8OSHk4Nb6XbG5v5u-gwLAxIYPCFQ7TbCZ-k_3d--VGa88efE-bf0PAm665Xd8LTxnEsmZ-JjEkIw20oH9yIPIIhU1zMWoPQDbDJhizvtcQnLs5RRs_rSMAqk4v7ucN_FKZI6z-fpoDXUzgB86iqQOnRAhQyNr1C5YbPhEVvlrm4s4Hv2BkfEOQgTUfs_ZCoENnuSdLRHl8MNT78lZSDiX5wevGCSNB8kMZcB3TtNknahQNoGV7SAaIZozhB8rXNM4y2ekqE7FjLsx2YM4BFsBB-uH4XzEgfKUr6m0Kocr21nxeRx5nCG_qDYLVI3xQDKPSUs6kb1YfHvVG-EXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBklY2l9aDpAREKz1pamfdEdc6X_BfVt-iPiKiY6z0cxIZ4ndreKyWepBZMG2_IbiCULFBorWIdeA80uYYeh-MLsWoxQ2Q5vcOmU1-zjI_gBLR70QJyX5W8moTi_jutX1ruhspVwJX5JcRZCnE5A_E254pi_537usW4SDv4sxVC2c8wkGgs8p9G7NQd0YWkogATGIQxeHEOWSlIKFIxZvxq_XgZDUOlyiKDxpN2MTlASB_AVHcnXQd2e83s1NnSU-dtLYsOD7ppi1Qgq3IImbAZmgZEUmdEO4FJafAdD2SBqmohQgx82I_Q40SZ8dA5litF3FnoGblnFn36eFGzYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_C1YjHMJrHKhAGOrGJsKfkVa98VjBF1YqgGTMIp9jFNV-CGfLARK6PrTXEtR6X3HWPqlqZpvrxSSICWshj0pa6aT-VvGIScI2MIBem4pt3aM0fy0OVSviU_Aaw9a7pHbAHtvvuIyCFq-DSFjk_DjnC8Ng2ryLOq1MDeR8xv2EwPWq4gPTHhSFjDw7SPofj3Xprxm4J2-a50FTRXf5Dd9FKEFxeJomB1rzWBjH20ZR07WPdk6LFM-SdnO3DjFQFggVslq-f4St_SVx79vs27rH_4MdMXZbBpeaNvvkR3oMS-kP5mPB67s7N34IE9Da6oHhZoq_CVS1msflUEe5B0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال وسط این همه آدم تو جشن قهرمانی اسپانیا شرتشو کشیده پایین و میرقصه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101406" target="_blank">📅 07:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
ناراحتی امیر قلعه‌نویی؛ برای اسکالونی کلیپ ساختید اما برای من نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101405" target="_blank">📅 07:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0EXmPwpD3G_Ue1tPHM5nKKlGPj2ZrRkZsU_kZYuHh60Eun0k6UgnNykpeOYQrhVFlPyFbk8FWdny2xWyao9_YxsE9nfV4-_u6Ha6xAdStMXwKKAsTQshvNubJZlneyTH3GMGzOyPRvVaOpjWG-10J9Xr5R20uzayvoJVrzYVp2qshNapvvYw57fJ9iJWR6F8OEXDhpuFcOVZxsjlF_JftxifQF5BgrYp54KaeRlNUqe7imDxoNt1PCuvylT2AAmIFFhaVu8yWrR4-vNRSaR3qyqDdglhkxYIgdpDXFnhBXmlc8axWKXu6U8aIhi5pEWqqaqw8BQk8nvBrWZ79eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvyewI5ixQmqRX7NKfZv90GAp7pIVabUdetDf99rP9HmA5jZohN3lBuUI0lGlGxd_QZCXl0P1v2nNJl2h1J0COt38etQrpJqb591HkPpwrtnl55soPyBv87SSFRtfYxgQH5GsD-WjjQG9dfg8pVqQK_YATEMjFwfLgDAKILOekB8lV8c78QV6iLo59B5lSq78kTlRJgswEslUc_yLqeVujz5OTufK9q7FO-4RZnF2hqDyTpog9iYDArryrVIeDgw8929IeSZYaXDB0SP_-pr3IMasEMHMnoN35_lpcaWfM_bxP2Tf_kicyNlYBdr4OAGcHNOp6mLmOZbvnqxgiwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeXIoV6UxCPplFkxZ1hde8Zsh-2ka7TfHTBYjb8LZVYtX0ShV86n5c7bL55yAdNHCKSlbgEJAlGATrLeoQdkMaU1qNwXLrekbXMaqD6Cd1Rb8r0u8Zh70z_4_KdvIkeJflNBfT_UM3tMMdo4fmFxmVsiKEQhglCq3gOASNHC4qYe7jAucnK3yF_INvBOxSPDPJWQztmI-vxJYRM004kbvJp65IsAtni-S811Kvd881pPFrwBbsnHI5jrErMAiGqeMso_W95l1bjJwA6EKr4er5tn4j1uYWtvPEcsaNq1Mv3Dy4OfirFpHnh6KWsd8zIp7Eh0Dlr1a2sbXZV9CvlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoJINYBMS4dm5CKx9MnrnR8BPL7sfVjIkjm63_gWapR4nIFBKLNFgd4pbhIY0lHEboRHmTEszj5DG1vn92IO3ilozJ87lzWrcP7QsJlE0gnneWszEqX0q1Ozm6ECLiAR6eOzlFyKY_UwGVWcIwn9KALnPxb8H7n7u2colGvFqfjEhMm_j6COlqFowCecd5KzG3k2ZGHz3O4rNYH0rMsyaZ_afB-aTSRmzGmXIvn9S_FEprsiPhvWFzwn-wFR6wjf7u6OwwEwM3ZfHjiYRxTGVvsN3hA3E3ULm9lKbkpVnxtNhhb6As0_Y7ThHjCrdtDByHySjV8VLy6tkY_E3pVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB63G7uwgaIwLENKyzAs0RxNEbww2GgeFci45S7OYN3mwM4_P1CJoIJ1nIsgM2EmisXi4iS7r2v1k0ecG61i9lIkmD6em09kwaObLDO5z-UcDsKmK-6CH0_-HEVQlAYnCDSHc-TnWrNlKBCykHRFRLvFqnC71KHLEQ4ewLT3UzrnQqGlZGUfjNVtCVBfxX3NqnV7y7qb4mY_ozzx2gh7c7nD--qccXYPdrS1FsJSNqIDfec2eNfWZUVA1dXkoRxa6HnFT5Qlczd9ZOzlafjVOQkrNqzcP5AHuqwUGzM-7pk8L9yj2N7fkOOJ2SjjBV2yA_L1bOqtpKb6OdVxffg4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piLJNNk7Zbu9fZg8OQj5X9_c8DuXIjBMx8SMWhZ_Xs7IuzjJ9U-F3XpS2ax-AVFPklcrsukDp4W9uC1OZVi0rFx810TA5nM-88U2jjA25_mjruCfXfg1keXrY_7OvSsBJREnRyciRh6idZNjHbDLeseKyP5BzZPLbzdeMzwuDw4kLBDarF8GC941hKoq1TOQ9AvvH86xcZGCy4DjiU_R-59RJyN00ztopddEeuE9KfdAF6euXT1O4TSIOXdAuB0QPylDxMfCPjmstMFlw26IOHMH8WqsXtnddwglqqa-Afo4jqPZlRLWEUVJiNMVVGa6W0frOdXL6NczjcFov71RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvkDlXAEXk3jchIk_fD5KxrP8T5Z5WE4a8BBQVCpSpNnRi4oNkPjBOID8Cu2A3Jl5chrt6ty_zJn4XfvZZSHGEwi6_WuPmFR_GgbzfJcN87orSgsARGNgUCdPCseLtYx192BhC_gNyHarFfE-HRWFwD6zRgOpVydBR-B_5vbR2_63X9YZ0qRyBiiXG0k5egc6ccg0RzOnZs1c0zr_Lj3L_0G0yZIJ92aW4Us8nd7FFFZ0RhoLxJIek27o9iSOpbRY7WWLFLBJjFGZpG--JESB_rFv8UuUtUzJmEVkYBc7La1cvcowzDwO1OSUCtyCC0nTNi1-pHi-IUT2yQ_aPMIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKT2ohFoMKFjd8j4Yaa5M5ObZ12dA8U3Sg5J_qurR66XPvWpVzjGOG6Z8sZtae3wPEqhkOeqJQn3Vx9iiVpsrUoKweDbyXnHI6dpp1qyY3ArpMB1H2_79ggHLDG3vN5eY_JornTrF0sqvBlIcojo3wgNjvNoAR0PsutjLD2OBerFnSHqa1fPSX9HTwO339TQW5k4rrP6DN2Hyvh2ok1u_UPvYVSgLqsiPyLFit4AFAzi9ROZcY7NNYrA7GOrXYGKX5ni8n9QhgdP3M8JBoJQyZ1RYd4EOzm00YhP5WX9SCmL_JHp1gjcGgrr3eyQvLMJMDmXNl-NJmXWxNFSB8XjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVpEgDgKwex6bQNFzYE2PY4wAc-nDtpZlr7JY6YtylxSfb41tTwLy5RhHTgDEBpO6bv4_x8OV_nZE6sRM8stnKVTGCUbbRvK-Fy6yK_kSGgB-zNt_DT-xrU4FXmMecDAwZCS3Ngks0sDZytt70VhV1EzEaoiN5POfvDigbS2Pitg0qv9vPGCx8fQzpAE4HPmEtGgj7Wz_5ozufVaq7hTeGY4KLxlyx4hFo7QU0r22KTl2t2tsQTGjjU1_k9Nyj0RK3-4UKgTAQ4i1X_A8_yKBnfpDtz_rYReoUCzawrXTmCWao7trJm9vLB1tNRVpxM-SMXAcNupYKjp-PZrLbSWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=gfjjf33q2bGl-KtUZ8Tdk_NVaBf_eYxQszgtdjcSEu3IOs9JqoGpEivXnWJK2SaA4MvKB5-X86j918cxD_sxZoV41Lnjs0iJ-5zqsQAz62TBTqU4D2dUieKHQh6LR84rSXAPD4LDfCmLLFDGsWvlJovYuRLKbqWzed2QLagw1Sl7PTyiv4zUo74C32aefKf9Sgf6u-JSrUCWbEz5z3i7pZsym8yODhQ5Rk_aIU4v37XkkKtnTxq-aFuktQE2hYufKyqUc3h6ZgHbbNCStsAScqeOT1IgEwbv1vV1l_Lj8XnRVTOev2fzrC2f5vXaYHC7paTz4muQG-3yV8CA-Utmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=gfjjf33q2bGl-KtUZ8Tdk_NVaBf_eYxQszgtdjcSEu3IOs9JqoGpEivXnWJK2SaA4MvKB5-X86j918cxD_sxZoV41Lnjs0iJ-5zqsQAz62TBTqU4D2dUieKHQh6LR84rSXAPD4LDfCmLLFDGsWvlJovYuRLKbqWzed2QLagw1Sl7PTyiv4zUo74C32aefKf9Sgf6u-JSrUCWbEz5z3i7pZsym8yODhQ5Rk_aIU4v37XkkKtnTxq-aFuktQE2hYufKyqUc3h6ZgHbbNCStsAScqeOT1IgEwbv1vV1l_Lj8XnRVTOev2fzrC2f5vXaYHC7paTz4muQG-3yV8CA-Utmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnPKhIXO-LxWdfSDuuMVwIcqCoDU-cC7adcBFuDkl-RAVvukQP84Tm0mAZTaooEPhYnnQraXyoTWVTEc-vM2yP-ZvLVlkxfFcF5jsXaobiqEbNvSpyffpQCUX7yb7N44iHgICk54fOwPRWIhm27gDLD1lZEV839QCKxlUpRGARRjMcI7bqFdSE3CMNNqq_-zgXHAEe8ofjWAXzEow15S8sp_-2ugqs_nPIDjGhi3y9g_00ov4dbLzu1SL2sMVCGfhMaMeltwx9SgO8jts1osirOoxFck8ySYRqR30ForxsroLipGgFNsQVIeW9SklamWXR5NS4c72rc0Y8qJv9adFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcSq3Rcz3xjuEPWz9vdIsZAxHq19UgKywO5DtuEWh8zuaSpbwqvpN7fTR4iV7sM0sEQx7GiwjGf7Cxo0Bswh05TO8sHR3u6n8o0BWkDBqmt4Agq8XvrzAY1iFOIh5Dn5B-QY1dFAlpI6Cp2h0GoKQtS5STvFk9zFT4P4suvHZwogwm8jiKDqpAUdYvI9_CLX5tlV-hvicMohaa8eWrucUbgRygXCU8Ztbbz4ZsxmYTuUsreHuf7zQV_BzbWaoqRoQDbvYAZChOjM-adeQbFWAzO2_dHiM9Hwg_iZZLmRfihVDJ1HRIwu7GlFkvI6uSYBmNp7tMHz9vL8BwsjrfJjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o86buwAt7g2RVKbHD6XqDo7vp-MIvrTNlHv1BehaKfpNd9b0lzumCu1aQi4wWMDB3Ujxk6GHrgqgTeCPEa8ILmzQ5cORMvnivQopAsqopLjfLMH-1PLxAJBMfVcDrLtt45mGNr5va68Wa1tyaYQlTojx2CR-NIogucsH98pTqBHQUyRudiHnfF8fwQOBcSrB7SdTx6L47JKZxN1r8FWD8oOgdtUf-29aEsMARI6_78wccdaqhSkHGwvKTLUJEG45yFxSMoWLDr_xFDURIdof9AUAEpN-Zv6FWNszMy43UQKIZle4JMeVvNSIcZ0SChvTH61Vlz_4e-ocmMuJin-HdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ElW3Y3Rr_OHb-Oz83VOM7KHQBNWGuPfvrtBJlccf5nqmMaOAFwdKnr4Dv7TmaZ7-JHIR1OzPv5R_vTDK_mgtwa4JbmEuEPm7Bx__xoHide7GD5SQsdRvvMHVktNG-7f-GTqkc_1OvAyuu1grQaJeEQemPtlwNCB93tr076FHLNSKTspsJ54Ng55CSDDS0aT91hB7M3Cst2f3YMRdqi6GKHNPEG_FT8JECKuF4oOREWe9h8knjoPmR6-1IZ1oSo34OSSJL1YQ95xtmlkaFg36IYcCkSzM5oipAE8olhoPMRrRmqYdDOGkQkDSMZmo4v4T2dh80s6AWekQlByFEK5uRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=Iu8Te3SHFry5WTaJHUt4stXLgfyqDCCOKsAyOCGsB-UD9vV_AFgVdvr7SxWSNFc7TcZomPSvMqRvpRTT1UO1dxuzAzEDwhrEDGre3EiWSb3QpqZeLK6ecU8-jzatGtoDSH0vrAjI-7cumg3tzs0NVNxsUVkPew1fFsbKWxSB6pOgn6uYzU2ykW81VgOyHTd3s5HU0m15Pxg5utljjtN4YDdIGHktzFm0zvlO9AX-yBNe8Mmdca8PC0mzaA8_WsJc5zV9T7UtPT-aU1SfPZPu_5AKe_HwtdrR_FOF6R08MM9xQSlLh-pnLZ4ODotAhOw33dUtQubfy3NinV_oxBb2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=Iu8Te3SHFry5WTaJHUt4stXLgfyqDCCOKsAyOCGsB-UD9vV_AFgVdvr7SxWSNFc7TcZomPSvMqRvpRTT1UO1dxuzAzEDwhrEDGre3EiWSb3QpqZeLK6ecU8-jzatGtoDSH0vrAjI-7cumg3tzs0NVNxsUVkPew1fFsbKWxSB6pOgn6uYzU2ykW81VgOyHTd3s5HU0m15Pxg5utljjtN4YDdIGHktzFm0zvlO9AX-yBNe8Mmdca8PC0mzaA8_WsJc5zV9T7UtPT-aU1SfPZPu_5AKe_HwtdrR_FOF6R08MM9xQSlLh-pnLZ4ODotAhOw33dUtQubfy3NinV_oxBb2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=v3807VlMF4pCXlwmIsprNnW2BAavQKR6-Pp6Qi2q5OVDNNxgS658bYnUio3La7FTq7hcus6wittZRYUnDdSuBzrfUHDdkdWq4HESY-XRrFZgBQfwTPsdGdLthMjoCEAAp2uhLX2iaXSOp0fv_KkeyZPZuBXfdsUDGP9RQuELLY32alrz9W_U0gr-olRQzz86aMW4xLWoVr2gvvDibS1VfrBXKL9fP22qALENF5f0Irf50X79aXq5SYkvMAVNRqFxpI9A7MmcQ6iiMQ7yghaQLdcYaOg0v-hHQIpGscMNAai0iLFn9rGPAjPfCFQFpnb8R4_rGortLQ4BLU9tjTJkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=v3807VlMF4pCXlwmIsprNnW2BAavQKR6-Pp6Qi2q5OVDNNxgS658bYnUio3La7FTq7hcus6wittZRYUnDdSuBzrfUHDdkdWq4HESY-XRrFZgBQfwTPsdGdLthMjoCEAAp2uhLX2iaXSOp0fv_KkeyZPZuBXfdsUDGP9RQuELLY32alrz9W_U0gr-olRQzz86aMW4xLWoVr2gvvDibS1VfrBXKL9fP22qALENF5f0Irf50X79aXq5SYkvMAVNRqFxpI9A7MmcQ6iiMQ7yghaQLdcYaOg0v-hHQIpGscMNAai0iLFn9rGPAjPfCFQFpnb8R4_rGortLQ4BLU9tjTJkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=ARI-955BcFM5AN-IfmuDBFAWZZQVLpiMA-p1003VCZsqeRd5Tevo3uVqmA6NwY1O-p9p_5fb9HFvgMr7vzA8G4yhgc70ANnYoJq9wTyO7cpXwTdkY8d7XyZiUXG_mabFlXCQn88HOHjWyfRxP5mmapU4xVXzEtDuqh9TTKrjFGccrcoyNW8Yr_vXen6TlN67UCGVfXt7MZYOBHujiy_tUBcYBYyOsR2W699jfKS8iKI8xWlbfYLPMiMtMtl2XQtuld-eFHP78CzoVsyYQHzeE9FDlLpnQ2uYwIt3UueChm47BEoEVc1gQmgHwuNEAjRzsAOJ5cdIHPUYvh2f_1NJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=ARI-955BcFM5AN-IfmuDBFAWZZQVLpiMA-p1003VCZsqeRd5Tevo3uVqmA6NwY1O-p9p_5fb9HFvgMr7vzA8G4yhgc70ANnYoJq9wTyO7cpXwTdkY8d7XyZiUXG_mabFlXCQn88HOHjWyfRxP5mmapU4xVXzEtDuqh9TTKrjFGccrcoyNW8Yr_vXen6TlN67UCGVfXt7MZYOBHujiy_tUBcYBYyOsR2W699jfKS8iKI8xWlbfYLPMiMtMtl2XQtuld-eFHP78CzoVsyYQHzeE9FDlLpnQ2uYwIt3UueChm47BEoEVc1gQmgHwuNEAjRzsAOJ5cdIHPUYvh2f_1NJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KscvSVnqWNLTAPF-bGMjucfqjaXY_j0F75Tq9xZlUc2FZasUcfcUSbyyMyH1nzJxg3jAW1XYxWSkjTNEKAwy0g0w4qQcwWl1zE1rPbmHQYjzUiE_BCkVqU1qgkpULNzNt2RvlFR69Gel9O3aFrUWGQ8swLIrPVxx9liEDGsyDZVOpwgveib6EuO5yCelx6NlXVXwx-N8PuKq_mz1xPZAL9h4vOuFMl4LDHjiNkMpX-P-JabecASR9AMF_hbhDhG8fGyPDmVsE5AJGeypkb-_3Jz44SN4cpenATZsJAOVNq1dcdvD14gIr7ziH39NHBsdvF5YvUA0tMEMsRHho0JMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=PazVza30wbgCWjXtgXA4-rFy3zjTzkGuGMy8Bjjs79sCU-AQF66ron-ZujRe9We65nGLkKzBTCEAbC_kAP6vTdhhJCOZzwHdczNaJoWqlMRSwaGkCW0j5ODD9O0_wRA9FNVhBHIzZo6M6YMv41jYONWQLx98IMdpUiKGfujMQDnpJr4U4ds-c0ABFpO4HVtZngPvN8qnaFi3bmi0sEUPoWVXkcV4eCIghgBIkc5G-Sn-fR3pUG2dvDGXHMVlp9vNHJ7UqX4k6D2N8hgtBllwTWGB_T77KLEUGgHYuV0Nf7FF1CBT4oArGCNu4ci-rOHI6NpvNEkmU8GmwswolJPMRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=PazVza30wbgCWjXtgXA4-rFy3zjTzkGuGMy8Bjjs79sCU-AQF66ron-ZujRe9We65nGLkKzBTCEAbC_kAP6vTdhhJCOZzwHdczNaJoWqlMRSwaGkCW0j5ODD9O0_wRA9FNVhBHIzZo6M6YMv41jYONWQLx98IMdpUiKGfujMQDnpJr4U4ds-c0ABFpO4HVtZngPvN8qnaFi3bmi0sEUPoWVXkcV4eCIghgBIkc5G-Sn-fR3pUG2dvDGXHMVlp9vNHJ7UqX4k6D2N8hgtBllwTWGB_T77KLEUGgHYuV0Nf7FF1CBT4oArGCNu4ci-rOHI6NpvNEkmU8GmwswolJPMRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpYmKmSrB94fvUmavdN1nmXyO3hPTscIb-uJ81cseTKiAbdjMYYj0L5wfpEafnsG417SCQgP5txflkj1mXN4zDNP4qBr1-tYGJgrWLty00sOu6s0KhRxwk0C_qZN-KsJJVd-fSjpMCWwM9TE954txBh1t8LcKBQW9T3VTq4Z_quEEAF6TOB6pQ12N_a2vXfxeFSSsV4RGBnA4CTEmHR5cRw09Nsg3w8-F5yJM_M0mZWIVt5Nx4ymkkLDSTxLvySgNg9OQ54KZaj9v7KFTF2_O2ia-0tQg5k1alKc3zEhKBu6tX1Ro0-WSte63wLWq4ql3Qv1cOMdnob2J3OvHV8hBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3wNZ1W9rwOygbvxxDHc1Y2GZzBZQZdyRiAi0GJE51853_7eai5akeq5pjAffGntrOgZTQDHzjfnFJJPEstJBO27jaoyZX37j33WqzPXqGd3rJBrEGPYy4RWIRUtlWGrfAw8ohTGjt0W3Pskfyg954npWw8b6fiX0QIDSuT5Lh5-iLnkhCpyZilkKzUO5hoElnOOUKiJzFnJOkhgEDdC1mx0xbr0HWljiR4OdIZkLreuVpu4ssJ895fKy6Zu9mIaEnXKUwZ5V471uDNLfhGa60MO5NkO7kxKCFyhxNrmWRm-Ikk9kUlvcnOBZIslSEuHjEDy-3_ksjt7MmDTRbbIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hj1UwHuIbWXRrnWH19i4NbgumXfF8GjB9GFAoCF04kF-jbK9WGOyXYCFymlVCjVcWQOBh1Iw71OPhCzVBFZXq5XpG2IAsqLJpCg4p-h1Q7K88h0HSF_b5VTBuoTjz1ilYS7OMLP56jMw5IJgRT8WIlm9_5-QJTHNuRl-ofFIZe_S8ZAxqugBC6Ot5Sz1dvsq89r7x-uj5TFVSPQ6NhzGwRldTh_L84-L6d-2jE2BrSvg_ZM1o2rRNa1gGdJvTIzbiY57uezt1a30VblrsA0npIIFGV3nmJlhDuUsX_AVnT5qZvDvgM74C7zqwDUOCGu0fYA1TKsAbl_hbyWVTMRDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTxNBtDLuAgMXo4hvDDIO6whJjC2sVoRn6NwvjziPrSiA5u545A62GLeD_DzB_2MCnxr9lo7VcCShHUhPRygedgDw5YPETPZbswQ2lT51t0iit66yOFGUET_dYv_l593Ap6-3uCYr8X1OgYPOeUoKYXt95e-Ry-1930O50L9h2tydIFDwObHi_tTetb7W31B4BKYW8t_Jlk8uJIDkAL0npd_F_FDA8TSJXokhWHq6nxhkPVsj9RKkZ1UqNB4KqQcyCM8PavRVARuNtadZJ2PAE0x3TGgDkW_T60qCtrTu7PhQJrRNKd17mAnLjDgU30lSBWoY1qiiVPdikyMv_gaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVKHVjLxex4m0rKN1UEvFKwMI3gMB3McL5sQjii8AtYDmmjaoZN2iRnWdEDMzffpc2hKGGzf2Qv3QDIhMWpBl07WbPHGR0imRhRc_mxiJ6eHWW0sv6uQAidUl_6fDW1shsx8DkA3tORMyw4CwfkW_fgVaR7YHF5tKZC-9RMSqn4N3Ur9yUHESaEnbf1XHR9F2h12wlfBZKhZ7GrQuyPlbqG_zIjvAmDc6fZjYyLCruWuO0ogTz9Jij4Kbpj4W9Cb-s8XTvlEdxrIdppLy66slrK8dnKfAyhM-6Y1jJy-vtYnQKnDY0GKe1rZQPyhC20K9CYCCszjbmdjLv4eSYfN8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCCyGNtc0p3tCR830W7QgQ7DUCSVqMieEgIIjcIdHa8BY50fGbYJV1vB3ZD0EsdABXv_gZcEHAX8Gs2-RC8irxIy1ReWtyasdeTYWtGJtLjwkYXknWC9zKxo9K6VghgaQQNpWdF9R1FECzL1Ea7Gx5ZlAeQev43T9m-wOkCJbhz3qMbd7CNHxR7_NobIMSXbfOncU9CcL2jCfU-b7eUbwUCALRpm8WDYG4xQxEH-BGx6b3bzgSop-lzQJrvolQuql3meNwHO_LOHMC1jBjSj8Rn076heyg_wqqPAZjc4lmNUR9Mo8nLRqfWvsAV46Ezn2EQzvt3E4x8Y_6m5UB-yTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=DXZbnodxPgCsOBvK850LOglPUm8Iz6286rAEGHoogXQI7RuboslpTI-Zm4ZnwqS_FjLHWvwQm1wu0y7T6JS6gqvBpqhOr4fXvKEGjNgjfqiYCbS6jbGjOguANKMGCoApKZNtNMTxDka_RBB8vKb6LmopZY20wOxmY4cLSoWjgJidwQhYX3Up1Tz4pXRqTMZlcRsHq9ugRddnEqjGjdYSuPO4rfN5DMqhvhpJlo7oPDviIHRFODaOt80YDIX6lY6M3LoHsrjR-UcSr-omoja_gd-iLsKCjHVwRDpyNEd6li5Bf6p2F9MMGHhtY5AawwsvKDirajtMhGTZq1sodeXKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=DXZbnodxPgCsOBvK850LOglPUm8Iz6286rAEGHoogXQI7RuboslpTI-Zm4ZnwqS_FjLHWvwQm1wu0y7T6JS6gqvBpqhOr4fXvKEGjNgjfqiYCbS6jbGjOguANKMGCoApKZNtNMTxDka_RBB8vKb6LmopZY20wOxmY4cLSoWjgJidwQhYX3Up1Tz4pXRqTMZlcRsHq9ugRddnEqjGjdYSuPO4rfN5DMqhvhpJlo7oPDviIHRFODaOt80YDIX6lY6M3LoHsrjR-UcSr-omoja_gd-iLsKCjHVwRDpyNEd6li5Bf6p2F9MMGHhtY5AawwsvKDirajtMhGTZq1sodeXKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slEFBwsdQQ44lt8JhbhMvm6t1jJjmz9ul7YXhfj4yS_eW4LtCs7b19vxk0XtncVt7yAhFq4GQTnnwQsxTQXTnxRoOrUAwQCMKsSLGQRebwiPorsOcDgr_nPCTcG8WjUYiOxiR9ItIfL6Uk5agLhErNSzxYHxfOxorunwcyThuNy539PKXprUm0Y1mm72V9tLhLcMJqTXny1wlMm4qxYLgirq_C3dLXiwviICwkN_fCpXm_Wq9Q-hPh042VYt8uGinzzf4Ra5xOzmw4MhB9DGL3OT2pkTDHyXhmW8oP5S80RTEV4h8lh6LDSPhaBegwEs6MOTknh9WUNGHqCg2nNiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV4Ef4uzoHAOkd5CWOcRgR0gbGhQF7EivLdB61ECRG7Mifp-voc7e1CEjbqiQ-bfnNHHq9jZIL6cJzE_c3GOXQWaj3XVCW_5S05tt9P_4_LStMzjSprnVFdI1LtgTh7qCY3R99ctaOJQ_bkPlX5f-wqZzcIf2JIVFTlmpayxXrvu-DcHI6-eASwlXAJ9dB8t9sw-7rp5Z8ZPm4_zo5AB6LgGXgsXZaUwbHmNQE_sSYi3gjGGkmy-Jk1Uo2o9kdI5bj5qawGwMBgMZNcVgXgb5Cdm2DZzb6VsQ2vMWxX5j-9TywObbhIecqz-jK_VML_BHz1NWGdrvI973WgkVVbQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ9mbRC50UZaPl7LNEIxOBgvgtW5sstxD7ygg-zaIRk5Roh_lmlwjGMZf1uA9lGTV6ejoZm1uEtbhiyeV1EMVPnCt7zzAwTHpBI2Ob9DXF5q4ztZreYKNl9mvFF4k_SADzUDPE2IpMBzXUWvNp0DBg_8zoikUo6BDELCbXCuTyuuog5ZZyhkIQuNnDRjGgNuQ3uDuOcHvDvXRAAoG6hz2wtIv7ouEAOADarD2kuSBK_amVGMcD4aWnaXkryANM4Iv6SXq-800bUtINMz-XoyvePapU-sQIkENMPVM2gIKsX-5bGXWv2qNZwvclMVOdujtnCvCfp1JDz7RutycR9RHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=OCwRiLl2wtKwQG6kkc9yqfQ90Vi9nxDMPSlBAj99hPM-kQE3c8s9v_qzuvM92Ju68PZFpsPu0Pr-JI8FAVIY1kf4mBXJVPJ2e9aWMmNnQkbAPEwHhGRl2kNqdlukuWHgltttV4OfK038QLvpigqJ480ztphZlelowX7AYsrw3p7vjTHHT7axdaQj81xJKJJQUdiBxD7r3baX0GSEpL3VyFyJIEhCydw-51zYxtsAusRbmSX20XMCvp_5vMutexjKPwCW-yuXZr9M0dQnGiirJjhy_OsHA44ToZOenunhgFJKMtG_oaRI5lySD7ZH3BE6Z3sOaxjxyXQTW7sfGU_s-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=OCwRiLl2wtKwQG6kkc9yqfQ90Vi9nxDMPSlBAj99hPM-kQE3c8s9v_qzuvM92Ju68PZFpsPu0Pr-JI8FAVIY1kf4mBXJVPJ2e9aWMmNnQkbAPEwHhGRl2kNqdlukuWHgltttV4OfK038QLvpigqJ480ztphZlelowX7AYsrw3p7vjTHHT7axdaQj81xJKJJQUdiBxD7r3baX0GSEpL3VyFyJIEhCydw-51zYxtsAusRbmSX20XMCvp_5vMutexjKPwCW-yuXZr9M0dQnGiirJjhy_OsHA44ToZOenunhgFJKMtG_oaRI5lySD7ZH3BE6Z3sOaxjxyXQTW7sfGU_s-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=OAzc2Z9eldy0PSwHGBpIdYLY00v-X8qmR0OoLmVVn1N8pnbFU0_HX5rttMOjh1hLujaZlkAoFKWLe_-AHmtHpgXB-ixLSVgUEll41zUhDS1VIX2ISlpUG61-uejV4obNSfI4qY9w7JqUOnmnbIiNGWWEVQD7QUbam8Cno7TkQ3jylciLAseZO4jjikwWL6KfsGQykN4dwsm6pmYqv5EPtKvtha1T3SZg-ha7uIvjWPaE1wethcFVnfp4YO5oglHve_KWMBmNNezusSNlJ2HtCGRsJxwyfBK-A1NQyHPSgast9iK_0NScZB285RkdHioHYYphZ_vKTYHMZjHEjzI3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=OAzc2Z9eldy0PSwHGBpIdYLY00v-X8qmR0OoLmVVn1N8pnbFU0_HX5rttMOjh1hLujaZlkAoFKWLe_-AHmtHpgXB-ixLSVgUEll41zUhDS1VIX2ISlpUG61-uejV4obNSfI4qY9w7JqUOnmnbIiNGWWEVQD7QUbam8Cno7TkQ3jylciLAseZO4jjikwWL6KfsGQykN4dwsm6pmYqv5EPtKvtha1T3SZg-ha7uIvjWPaE1wethcFVnfp4YO5oglHve_KWMBmNNezusSNlJ2HtCGRsJxwyfBK-A1NQyHPSgast9iK_0NScZB285RkdHioHYYphZ_vKTYHMZjHEjzI3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY75K5vzz4MO4Bwl3rSbri6NKTOd-JRdbeRZuaJv0OQt6mOkA1PtRuhm9BqGsnBYi_6_JczP3yxOU8e9ooStW1tpI_7Aqk6sy5lECjrJBv43zlouGnQfL07ZrTl3nzCsvH8pThPOC9lsyXU1l1AyMWiDgxbb-59yp6L_dSvfv9zYo-rflfS5rYgSLWHoSCBYQ1EgKYd3G1BWsuG5KWNdrGHeEHxAnsO5_T9RE3W0ZTQ3yyY-OqKVsUgx4TK8ZI8L_GVm4mp7RsYNnxNJK-_wOzfCYqKgpW36xCdVA6N0el-t8Yk1kbO_3Syurj_nrQQgqpuKglx2J5uX9fDfpcJX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-AT_ePWTjDHqnvYkoAtA07F7NMKe9SpwQrew-jbzMVd0HvjKvpesDKnGM1uh5bGco5TjkoPDZezrVfUFt3Um7DP5wYS4pduwhHZs4ruplS1dbI17pESYMYA1tPK8tVTBuBzt992MDBVmlI51gg629LZBdkve2ZbXVaHL88aEzBhMKrWGfOq5VfX-UdeGNpuaJHQi3dYNN7jHTefjoknv0D7G2bHBuyQHX7vo-UyRu0p2XIkuEZnf8qeUyave5yQ4xLLkK5B9u-Evd_6bRI2uj29xkY62UUM_UyMJ3OdnBvWM55Rz-KtAwrGoENCjBoJLqh1rMiwJm7wj-emQRwZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyoc97urJdJ-2wTQOQdBYnyt1SVCmoEWDoHjB-me41oJTGYf4oawrA4-22OodBeq-jEqIk4xrtrXZui_gZkJWI3XvPflmEET4yW8VF-dezHlAnpdSFvJpTfMZILon24uVJxhw6CLuviO2h4URAqXXLlnR_omVLYjOG9y-qUB9rY_ajKz7MWMHgTgh31smJ2y1g0H8sHeN8CXT0XXvK5sUBdF9ruvItSXisr6sQrSF6y9yrCP5qzey8CaUu-Sg2eMjz6SRmiSj686We-bwQSWx7vAtc_u1HT2MpkhFZJARjb0GDE97VDyRour2D1VRZh4aCC8M8ydpuJelw3QgtbdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDVk6MeZ1F4b73jzQdS6HLShpMVypJOBZL2gLobTrtw2Su0dZ5WA9qlL3nrpklJFJ40EUykNCKqkAK2JZfmvpqYOyfuK-q7rF5z66LI1d11lJcQMqrWYwgDIguLaqe5iW0yqgKDAr8GrnRRnxGURALXmjunH5TtTGvI_KmA5ydaZQUm4sn6xJv08HtfOxQ3lkKGFC1PjbnFNOfKaKOqJz7boTvCnjVf4743weK_mFAkw1Oi_Oysmeih2NynKex-qjnHGft8QbkIf_8igqRChEMJ4stjGOnnLiVy1adJ4X__Rf13qASp288wXAyHKBk1aTvPhdaTWAaohK32TTCx2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCi9P5F-vSQWgw0AjS90qP8QwkFuOW_znF8oWv6mfyKixKUIv0AgsApEr8LW9GurMv5Meu7MpzqrCsnKobt8NRj-RqPrd_57k-PQGFM1-jB2HwC2PxQOj5rlTlsfU3lcQUdPBbk90-JL6QotAkuqjX2etgjFkYS_UfHLFzXNCsXt5wDxhBBnRIND54i7KNXUW7AR0Y4ANrZatRdj2-o_H4hoLBHPoG32ltkqDiqoE8ZTPdgv4bbfAn34RUrg9Zem763nnWOcfvNet3hkiNWBK7ANOWcTZW0OANaMy81m0x3gBXodpxdbg6z6lvURVjhMrQ-kPK7JfQ2lKUvYzmo_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=RfsuFNNaDfRgh4880JJ4djfvcJJRHYYNuNh40cx0pnZk4-tHazjimhkVzs7j-GGHi8KPstlgiOK4s7wUCQHNUJQZW6TKf2ZSxW6SE-t6ZvffpdOITlnM-erE8TRR3JPxRqZh_GNsHotpQKk3rKnAXCFtTzPM7uoyrI78wU24UPhPPJIqxYxQYQ06SrnDt3FVz8Aci_2GNCCXGS2zr1xNuEKrTxZh_S4FsU0z7WPDezGUS35bLCSx0RqV88O8-IjkHUCOBt2Q2zlshgjiRS-gQIcut8qUwsf4dN05w70Ag5MPROgEZEODqXTsxKZkJytYVHotD164sFg16YhvRtSt6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=RfsuFNNaDfRgh4880JJ4djfvcJJRHYYNuNh40cx0pnZk4-tHazjimhkVzs7j-GGHi8KPstlgiOK4s7wUCQHNUJQZW6TKf2ZSxW6SE-t6ZvffpdOITlnM-erE8TRR3JPxRqZh_GNsHotpQKk3rKnAXCFtTzPM7uoyrI78wU24UPhPPJIqxYxQYQ06SrnDt3FVz8Aci_2GNCCXGS2zr1xNuEKrTxZh_S4FsU0z7WPDezGUS35bLCSx0RqV88O8-IjkHUCOBt2Q2zlshgjiRS-gQIcut8qUwsf4dN05w70Ag5MPROgEZEODqXTsxKZkJytYVHotD164sFg16YhvRtSt6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8dY5SLrB_5jyfOQVQUPE1XoGfpDFnzc1Glg7sm5H_V0WJF0XvVO-q-cycfL8xOTa4AGGhb-1-Rrpj3CWcd6RuchE6Wa6ro3AibhQhtxCInVUEZZNiBCE__PZ-M7IpOBNGKRzPpwD0sKv30Dx9fShKz7Gm-sHtaS2ouHLjsvTIOK5JfRNEwF51N7HAPZEkxZoNX8EuM6aqfb9QHJe1TP6eM6xwfc9_IS6Pacj3OTFoyIY8mROsSHs30IiVF6qC5aMpyCjK1JHLWqX31_y7GEMSFgBTsd0teQxmMF9MI1rCsg6iFKH5rtHMkhAjoiyGPCSRkF4ltsOxQ64aWVetJgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=BAWWXktWuCgyydG_17dYEQGreFn7C1-QsCZx8xucRdJRUDG3wNfWazADK4TOHVmKBryfRuZcmVt_sSA6U78ieEZeXD0d8SxI1ZUALUI-pPWou3K-gf6x6aIeugBXLyGoDsbo9MDIx3c1d8s5NTQU71pbM3g6Se3qwmwuLcvMiE1IaZ68z2rDNnLl61vBKlKSU4KGm7-c_JgWQS2vpNfs827koBkjC1yC4hxgL5JMJRGo__Sv2pbvfWZF9xWJe2AGupv7WClyXBiJm8agOi9mkJtxub99VkhUgeUh_NQHhrL3k2_85sw-uqiyZXPH2Q2SrLkGcTcHSQgYcv4JzsDG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=BAWWXktWuCgyydG_17dYEQGreFn7C1-QsCZx8xucRdJRUDG3wNfWazADK4TOHVmKBryfRuZcmVt_sSA6U78ieEZeXD0d8SxI1ZUALUI-pPWou3K-gf6x6aIeugBXLyGoDsbo9MDIx3c1d8s5NTQU71pbM3g6Se3qwmwuLcvMiE1IaZ68z2rDNnLl61vBKlKSU4KGm7-c_JgWQS2vpNfs827koBkjC1yC4hxgL5JMJRGo__Sv2pbvfWZF9xWJe2AGupv7WClyXBiJm8agOi9mkJtxub99VkhUgeUh_NQHhrL3k2_85sw-uqiyZXPH2Q2SrLkGcTcHSQgYcv4JzsDG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=l0pAf07MWoZUW7CfQpLHxiznWcxbJdS5j75cbJs_0slFtMP6aSmaCq4ZmMgwAEKEtVNM-GbC4NPB_3s5UafHNisB-7Zc5fFWPj6mslJDW5huJqo1lkjWb7pPm3x0XqvpkFcO8_KqLZM5naJFqupEtmZSnT0yw8AFoPAQ7jBGw8y7uH1kdj3AmBFG6SLOMWUHTC11-RlgGNyJtCMkMOtZe2GMzk3DLD67c74ZxNrKKLc9Nz3-v5qSRRraP0HTIW5h3cRAhTMH5DDQyl7IBQxORgNDmE1nVq_Y1Z78XZzLT5TuzZalPfNXsYaE9ZoGtrGPgKDd1YXV94uS0CxJAp7B9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=l0pAf07MWoZUW7CfQpLHxiznWcxbJdS5j75cbJs_0slFtMP6aSmaCq4ZmMgwAEKEtVNM-GbC4NPB_3s5UafHNisB-7Zc5fFWPj6mslJDW5huJqo1lkjWb7pPm3x0XqvpkFcO8_KqLZM5naJFqupEtmZSnT0yw8AFoPAQ7jBGw8y7uH1kdj3AmBFG6SLOMWUHTC11-RlgGNyJtCMkMOtZe2GMzk3DLD67c74ZxNrKKLc9Nz3-v5qSRRraP0HTIW5h3cRAhTMH5DDQyl7IBQxORgNDmE1nVq_Y1Z78XZzLT5TuzZalPfNXsYaE9ZoGtrGPgKDd1YXV94uS0CxJAp7B9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
