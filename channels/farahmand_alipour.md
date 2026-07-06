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
<img src="https://cdn4.telesco.pe/file/d0pAHRt8jWPFAIqfaTSn-1eeyt2OkXBO75ajzl_eiBfmplvvbI3b8ScQMPjtx8Mln1kIx5rb_06gKSNHaECFaZtV-sYyv8BHG1_HJSdBZ0rM8lVnFzlje9SZl1MjdeaM_QIw_GAjAcBfrG3vcQJicybBt7Eq_NclD7WNP2T7U0qj2AH537FW1XIt2D4XtRo7I4EkxWssXKnAuHASWrDz6cv6QZ7vYBZEP_tlXT6wIGFnk54DCgafVgE63M44OKZXFRiWcQL_WbjZZnKGtJm05iA1-QHFywoqvBsYHJzl2kQaWmj1ZKaHuPB-59xDRXdg9zhbXolAlx3TL8pti0_tNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 02:28:55</div>
<hr>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=n7VSooJAdq5r85H5fTWn7pPB-JGK9yceyQZqMFm9COxMISkZE5IG3CL3Izc41MLNo4K1AkkQW8vvj4Ktbvwp0HMFXROq-AzQOb7MEGOgwvYgTVaP4hyP5WIbKZysPnI8O8gZXhJLzV6GnHoXVmhNPStqxwKJyDPQWFn6rgU044mBVt3WjRuekCrrNrZ2xEudBE3FEhKsDDaBaBkJ_ea1N-Oyj_7wSJUpUnKwINJeiW4Eoj8mUff1gMEWvmGK_-LfKvgOcWDKtuXKGLMDdoBz-cjWz1yyj1KhtdIUH87G1ZbOs928Xu4gTXWXtIsz90_nptfx7h6EKkUKdSiBXk-7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=n7VSooJAdq5r85H5fTWn7pPB-JGK9yceyQZqMFm9COxMISkZE5IG3CL3Izc41MLNo4K1AkkQW8vvj4Ktbvwp0HMFXROq-AzQOb7MEGOgwvYgTVaP4hyP5WIbKZysPnI8O8gZXhJLzV6GnHoXVmhNPStqxwKJyDPQWFn6rgU044mBVt3WjRuekCrrNrZ2xEudBE3FEhKsDDaBaBkJ_ea1N-Oyj_7wSJUpUnKwINJeiW4Eoj8mUff1gMEWvmGK_-LfKvgOcWDKtuXKGLMDdoBz-cjWz1yyj1KhtdIUH87G1ZbOs928Xu4gTXWXtIsz90_nptfx7h6EKkUKdSiBXk-7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=j9Es14Giub-MvbFIHY44D5GOKPX3LmKkxyuOmTHB6FgXDeZs0ItISgSJT9dEET5HF2Ri-3TZL3MuJqFuRk71EEYe7HL3ivVYnpgtrxI880M0ApwOuuvj0UOam1bTLYAf994KTT7XCK6PRsR4-EXPnZ81ltEtujZ2JfhxEKytT9J5greXGTqSWVslV-Ky3S-TLdEzUAdUMzUPcf7xWnVxPyXvjIzChv5oaRKnLpGkGjRD8YpIrdO4zIxefzLOAUUTmxheunGH8ZtMPHsaUNjHHxgh_DprDp7wsthSvUVnbYhfmgCJFeJkkZNn4bbFZvWN7einQebFp7pz4bmuZx-5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=j9Es14Giub-MvbFIHY44D5GOKPX3LmKkxyuOmTHB6FgXDeZs0ItISgSJT9dEET5HF2Ri-3TZL3MuJqFuRk71EEYe7HL3ivVYnpgtrxI880M0ApwOuuvj0UOam1bTLYAf994KTT7XCK6PRsR4-EXPnZ81ltEtujZ2JfhxEKytT9J5greXGTqSWVslV-Ky3S-TLdEzUAdUMzUPcf7xWnVxPyXvjIzChv5oaRKnLpGkGjRD8YpIrdO4zIxefzLOAUUTmxheunGH8ZtMPHsaUNjHHxgh_DprDp7wsthSvUVnbYhfmgCJFeJkkZNn4bbFZvWN7einQebFp7pz4bmuZx-5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=FJf8RM0ZtWqYt8xvSFARTk-TxCl8ICfBkiqMSRRyX5C0lrIVceVKTcJ6zAJuCZ1mR9TptuNlCkP_4BxcUjx6BO5x2JlflCXjQ5esIE6SEjJSnt_qkw8BbgTdrnOUrfroFLVX1s2ZowrvH8OSZYJjZzn9tLmuI3CGDdK-9vDiSOZ-EAVZMpBAAiJqxZ4Tqpi2N16NYZ6JPXv0eYTX1OJfpoSExQvBVewOo3C1dRycNQTOUOIC0bhVryFXv79NsMZTcSHu7UbzeMKNyTMcNTPfTRuSJnZTQUMypB9yJ_dCi0xJQ4gAD30656o9DV769uVSvqDDw4cvc51hu8UnRlf8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=FJf8RM0ZtWqYt8xvSFARTk-TxCl8ICfBkiqMSRRyX5C0lrIVceVKTcJ6zAJuCZ1mR9TptuNlCkP_4BxcUjx6BO5x2JlflCXjQ5esIE6SEjJSnt_qkw8BbgTdrnOUrfroFLVX1s2ZowrvH8OSZYJjZzn9tLmuI3CGDdK-9vDiSOZ-EAVZMpBAAiJqxZ4Tqpi2N16NYZ6JPXv0eYTX1OJfpoSExQvBVewOo3C1dRycNQTOUOIC0bhVryFXv79NsMZTcSHu7UbzeMKNyTMcNTPfTRuSJnZTQUMypB9yJ_dCi0xJQ4gAD30656o9DV769uVSvqDDw4cvc51hu8UnRlf8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=on3LibvBC5XQ74LOr-E7JsTa78I4IuXi_CVTJGTFYBiZ8jr4ZDxFddP6rlq80WPFigVtOdm1LBdy4O-cHmWmZieui5DfuYHRsZkA5a2FzDbGrInN5_x9CCLOyJRq7ZsjeQw4YaY5kv6yF7QXx2dW1itXWZJhkISV4SvMLRLcXvJ3i7sjlDkP8_-5cvme2JEZ3kNbZ6whbN9Lijzu2crsxwAd9fNmoiKLwOQPlWJBk6G78ClNZZeDQ-y0VRc1pWfbVcCXBlQi6TmomJM3nWOt1G6J2gPnIhfiZnRxbGhJqMfrGdO_29ItfGwzKX1tsAaU3GJbXBH1-S4NfVHNd9u8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=on3LibvBC5XQ74LOr-E7JsTa78I4IuXi_CVTJGTFYBiZ8jr4ZDxFddP6rlq80WPFigVtOdm1LBdy4O-cHmWmZieui5DfuYHRsZkA5a2FzDbGrInN5_x9CCLOyJRq7ZsjeQw4YaY5kv6yF7QXx2dW1itXWZJhkISV4SvMLRLcXvJ3i7sjlDkP8_-5cvme2JEZ3kNbZ6whbN9Lijzu2crsxwAd9fNmoiKLwOQPlWJBk6G78ClNZZeDQ-y0VRc1pWfbVcCXBlQi6TmomJM3nWOt1G6J2gPnIhfiZnRxbGhJqMfrGdO_29ItfGwzKX1tsAaU3GJbXBH1-S4NfVHNd9u8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YIfwKlGFZdCJSUCyFx4rUzhHnQ0eoEgWOZN4uIBvPWnHruEKVemQYR3msZDhIq17HMOBjXeQT1GDeq4qpT5FZOcYOetL4uXbOb-WQf6Qj6JSktJT5suQqOOLnK036IA3yu4eYEzZMqI9YrQ88nSXzZOZkwp02i7-MpfT_DTI5xpoqlvVZfVfSjQqeuaUR2Niv-oeTohfjSVBmXIwILvnsVUqtWARjQmDQoWhHJV8EyaH-AVnkVB6ac1vgiia6q1wMuA8MmDK9hn8IAZzc1WYnLSFV44cOtWsZtI6Doava_tJH8OP6llOv8doCIs-3t0ikuwZOEChn3D0CFwVJXOCfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YIfwKlGFZdCJSUCyFx4rUzhHnQ0eoEgWOZN4uIBvPWnHruEKVemQYR3msZDhIq17HMOBjXeQT1GDeq4qpT5FZOcYOetL4uXbOb-WQf6Qj6JSktJT5suQqOOLnK036IA3yu4eYEzZMqI9YrQ88nSXzZOZkwp02i7-MpfT_DTI5xpoqlvVZfVfSjQqeuaUR2Niv-oeTohfjSVBmXIwILvnsVUqtWARjQmDQoWhHJV8EyaH-AVnkVB6ac1vgiia6q1wMuA8MmDK9hn8IAZzc1WYnLSFV44cOtWsZtI6Doava_tJH8OP6llOv8doCIs-3t0ikuwZOEChn3D0CFwVJXOCfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClYufeb9wKFbF4T8LtD6rBgPNWzPVcYxpA4MlAL5jEMDA-FLsTyYzBVyKyd_5zyO5DBsPh_PhQsNJkIuacEIDT06nufAQG7vNto8CfzNPo5OEq6a6M7Ti9n49ksPIq4Tvf5_r5ipc31bk48cYwlvO0yUwugqKoFmEwpXRsO8END4AQTLsq2ro8Fp3NJxIKJMThUwGUWAnwKYBW5aTgcg9gSZSwwEmWn4p9LyVZ93dAy3Ml6kuH5VHJ-yxzQlc9jjDkLLDAcjpuq_775w0-q8x4EZLugElZ2kDZJE0rXX32QSMoZzBu9ouvqa5useApbqM76A2AYULgzCLgGgtmofYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=VweTnpf-7Dpkw63e2WkTzP4DNsDkR81Gc57SoLKz6051ffglmDfGpkTQ1PD1sA6DnahwclhRm3htDE2fv2AXGFuh0wB3Jo6d_2lba5ZAH-ek25uebjnCHIcCBhhkfXdgbhXpY4mWhZd8cVjRLdFSSrbg8YqTdpwzEjFI-wAFe2irCsSrgyTowJ_AeuGJe1aabJq_cwFVJdRN6SURPjJJknvV-ICV8neJRm44EA7w7wjPDVTvorJHvcn-ARFeQg_F20sTkS53HsRh8Jwndads9aJnSVz07fwbA27yWjjHk3yCcabkJLThnopd_36kJeEqqHHmQs73DrBxJBsgeiLQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=VweTnpf-7Dpkw63e2WkTzP4DNsDkR81Gc57SoLKz6051ffglmDfGpkTQ1PD1sA6DnahwclhRm3htDE2fv2AXGFuh0wB3Jo6d_2lba5ZAH-ek25uebjnCHIcCBhhkfXdgbhXpY4mWhZd8cVjRLdFSSrbg8YqTdpwzEjFI-wAFe2irCsSrgyTowJ_AeuGJe1aabJq_cwFVJdRN6SURPjJJknvV-ICV8neJRm44EA7w7wjPDVTvorJHvcn-ARFeQg_F20sTkS53HsRh8Jwndads9aJnSVz07fwbA27yWjjHk3yCcabkJLThnopd_36kJeEqqHHmQs73DrBxJBsgeiLQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GgwycXy8dSHYxFg0_J_0dYRHx8SHOM0R-vTd2E9VWgyqTkacEPVihsSgEqmstgL48CTqqaWEZzmGVdQavHIKEScwG9uOhUV5L4fYgs8BJnG3kFQODN0du66qwH8lvUFpnqmox6bhjnlnwsTpuaz99Y540fNwwcm6SDuzqb_Vt0rvzbureujWxeWfx6yflIuqm2U1Fpzgny9Xd7znUymub5rB5Smj0k7RE4tk7BWcyGbZ6iTSRmmRfsUdEJeeVz5KBhySCOa9vUYzbc33hDfIX66JfRVzBhXHe0so0AYH_3h9sW6c1kHtrmLAtmzCNU6zepd8RHdBU2_foVmUw_ARbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GgwycXy8dSHYxFg0_J_0dYRHx8SHOM0R-vTd2E9VWgyqTkacEPVihsSgEqmstgL48CTqqaWEZzmGVdQavHIKEScwG9uOhUV5L4fYgs8BJnG3kFQODN0du66qwH8lvUFpnqmox6bhjnlnwsTpuaz99Y540fNwwcm6SDuzqb_Vt0rvzbureujWxeWfx6yflIuqm2U1Fpzgny9Xd7znUymub5rB5Smj0k7RE4tk7BWcyGbZ6iTSRmmRfsUdEJeeVz5KBhySCOa9vUYzbc33hDfIX66JfRVzBhXHe0so0AYH_3h9sW6c1kHtrmLAtmzCNU6zepd8RHdBU2_foVmUw_ARbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=nv-CD3lRyXRWZATtvMA0pC6I6OmDycjg5xU9CT8eAW1DzNQwWvqwZ9G6UsMy_vO0-J4qmZci9iHxklzFNC9D4Q1x-lPub1w8icKjR5rg27Ru3Uz9wuaa8Unf-jBe3lqrsagkUAdCFyrPYsMO5dabDwXSxdXKKaIWMKDwIpGsOJoaDijGDoTew2zQTThTKqOSZc-XaGcKzq7cE8cwIKcpbUV04Ama2LHuo-z4V9mfB7qn2VcIZrDW3CrAVx62HyT77cUQIWrrgKokrJEYuMkF9l4fGNjcR6BEp2eVuCnIrJXhb_dyrdMW6jbq5V3-ygccD3hZ6KQQ2zHJhj5I6lJ7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=nv-CD3lRyXRWZATtvMA0pC6I6OmDycjg5xU9CT8eAW1DzNQwWvqwZ9G6UsMy_vO0-J4qmZci9iHxklzFNC9D4Q1x-lPub1w8icKjR5rg27Ru3Uz9wuaa8Unf-jBe3lqrsagkUAdCFyrPYsMO5dabDwXSxdXKKaIWMKDwIpGsOJoaDijGDoTew2zQTThTKqOSZc-XaGcKzq7cE8cwIKcpbUV04Ama2LHuo-z4V9mfB7qn2VcIZrDW3CrAVx62HyT77cUQIWrrgKokrJEYuMkF9l4fGNjcR6BEp2eVuCnIrJXhb_dyrdMW6jbq5V3-ygccD3hZ6KQQ2zHJhj5I6lJ7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKiZe7WRTRMyCLBlk6PtVIBvOPL3sr8sa2Vy1JkOBODmgcai9w6rGHux4ztheshAuhyTvts3Z9abzNGgAKTWQWu3zoFa8LC5y_720balSc0EHdA5JtRxl3B_vFj9mPhcbtS9hGHyWsysNdM-Lipjqax8mZBTLnqxp7RdkNnxYRGxz2cj3KEjg5Q-pHjePguIboPZgJ3W62pchpqb7VMp3xxxqs0PU44WgBUv6DN8NBbKxEdGkadXf8iUVcYJ837NJdAN_o-BZLmoiLMJtKQ__Y07tbx-FcaL4ijLrw4mUjB5-Sm8j7WzXw1SthY0Z4yBK-Unu7I7BCx2f7jf1N1lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=neAUwOFAFD24syHPuxSjzIGLf8wrrfr-GeGnORf9r-gFIno2q8wvvQtcIMqtpNwPn7JBGgmAdxeaoXoECpeMwi-Hh728LzYJf8F8GsHkzmLDzgY70RKPOuLSpXrVSb_RPdWGy2Zq4gffqQqHl57ki8kUevB7PsZ5chd4bjHWoQMNea1QAlpxqZXhrsLSa4YemRkuXQRF2MgWBHmcatbPv-fMW4CfkOr3JpFyZH4t1ldJFdCXah9qVGLr4r5xn-somatb26OiBZwAmIqArfdZdD1Lvf62UqjFKnH4b1NFB2BLB9X2yQJYz384dYCcbGMZXoqvLBul0usrEFLSvbGRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=neAUwOFAFD24syHPuxSjzIGLf8wrrfr-GeGnORf9r-gFIno2q8wvvQtcIMqtpNwPn7JBGgmAdxeaoXoECpeMwi-Hh728LzYJf8F8GsHkzmLDzgY70RKPOuLSpXrVSb_RPdWGy2Zq4gffqQqHl57ki8kUevB7PsZ5chd4bjHWoQMNea1QAlpxqZXhrsLSa4YemRkuXQRF2MgWBHmcatbPv-fMW4CfkOr3JpFyZH4t1ldJFdCXah9qVGLr4r5xn-somatb26OiBZwAmIqArfdZdD1Lvf62UqjFKnH4b1NFB2BLB9X2yQJYz384dYCcbGMZXoqvLBul0usrEFLSvbGRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=XQXqCdPoOnVGrOSJ96M5y_20JRnd5RgSLcCmR2s_WV76wt0AHPMpOHFKAfJhHRtYSY5hmKpfN9hFUfHxNrGuVs5NqPsMsqjopTkrYP5IEKDzxsE6WD13pPEzzSa0-nu3v60if22tro9k9_2QEwRf5JFE0TODlcORa9treHABgBY5inDNX1ZVFxBVoAVGuvRHLsPErTxzL0aAsEoTIyyY-FafutCPgqFfRsyTxJUFIg1zUwCFJhP0Fjq5fzz2NJwrR7bfbd2-YdBA9lev1EboxNZtzA0yHrGOMZwuIW-OAxxGfK7LQVEF5J0nfaTRSRJpNwEsPZpaOS3HU8_tMUzufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=XQXqCdPoOnVGrOSJ96M5y_20JRnd5RgSLcCmR2s_WV76wt0AHPMpOHFKAfJhHRtYSY5hmKpfN9hFUfHxNrGuVs5NqPsMsqjopTkrYP5IEKDzxsE6WD13pPEzzSa0-nu3v60if22tro9k9_2QEwRf5JFE0TODlcORa9treHABgBY5inDNX1ZVFxBVoAVGuvRHLsPErTxzL0aAsEoTIyyY-FafutCPgqFfRsyTxJUFIg1zUwCFJhP0Fjq5fzz2NJwrR7bfbd2-YdBA9lev1EboxNZtzA0yHrGOMZwuIW-OAxxGfK7LQVEF5J0nfaTRSRJpNwEsPZpaOS3HU8_tMUzufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aidBX6O6AhfuCV-qpf6MLH00K7Q6JA3UiQ1FZAlaR4N1ZXTUNSyCayKbsS6k5h-WW8doBSdShT-Ib0PsnAAdH-8rZ2C-mMYrSd_6D7724D77NLOP51X3CpEE65P4lYJUQkbSnJlbP0mpnlh3MIqtnSyIHum_gglj2SozpNnezrwrQn6zCgWsdcK9li0PMKTtFt8KXhGhNkfWBw6c9u5zFvMPXQniZHbnW0PDvCiAM6buvCTg1S9nw9dtdMuhsV8xM44-sMRh0aBtpzEyuLuTNBXRWIE7pkFOa1BMQhud99cEsI7Vr60ase8CXr8O4Ql9G4OgV5IFV_leFP5W7KDVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVYqmxNRtLH6pVw56B-NsWi7NpHUlmKba-ZoFauuMBp4cFvtcpF7CmCp-b7zkFvAa8J2AXluPs4SJmhH-EI5xXhQQjxcLCnswOIuneVhTW-D1aq7fj2n_TVLPZNvBDTetGJxmfXgR-uiWUDe5galwv6E6Qxycbb2XSLx3sbeYIg42Aj2bHQqpHVqQAheTNX7Z7QeW_1vWo0mJRBIJYGnTaX5ZRAzHqH9tb7nmFHsQfv68s_H6Q20B5bKkhlHcvU7iOtrKs-jL2cYNFPIaT7bfw02IvYY7eSR2RRCwRGJMI9qZ1aFYiqBW-c04TAHT3F--l_7cVGppZjGEzpBx4uVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPzlVIsPnjdFbenbXwRPbcpZnS97emGSsINF84W4g5NJXI7BOw0zEvr_D7e7nQvVEOYYyoTUbS46lsjQjVa50sm5LAc6JyFU8WrTt586SxfoKkKdakVIzzjmGx1--tsMKs6HdXept21xIZxpsYxZ84J9pvpTbeIHMXxplwDQ9aZkMV0KselY35l3dkggwF3O3sxY-kWiuOvQTWcEvw8nQoXKPdy09LFR-2EZLIYFGAeCmIDRflAO9VavZK9WiYGbk-uP8Rl9HRlQRuG2RIkO0iUc0nvZ0UZdqCbPVADJRUbn2VQTJwQNAbfubWjypImusy5vpU6RfnkkWIkY0p_UDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXSLkQngeitUl4sBHeFJB4jXeTfhe0yvyVmkZkj-xiQKH2u5C4EofDDZNURb74YQ4WV36b1OdO5Qv55iuZ2t5DsSBLJjyWGS9V8Od9-14XwzAbYC3g2a3BIdgxVJSA2_JjY1ROx5YCU6WN6opPtXs6Mj7H3n3hx3ic14DMovFKkCk5XU-R-HqG5z5_q_pU9NHZNmwV65yK44fpog3wdR04Y4nQJP_HF-iJPZJ9IEdx4RFHszy56j2rgEVnbW8VItZY9M24Vx6W_o_Z0WwVilY5xPLitEqksM-DNkAIT2LYxSl9BwQQxjuPpzOtPoZIns3sTzcLNSvpTDUF7t5zMWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_sAmDKfOAne5k3bhSt9C3WTyL9-Wd0n3bcfngSB5szthYEoBfRd-q-JIdYPkbUvMgnGg9FqH-mgHozo7RXpdyLPqj_s0zVerxxLVQzrujQW-eTN1f8HAcvNwlr-CCqmfJ7VNCB9r0v3DIScEU2SIhS3zQpvFSFrWtX7XRYP5soyyESYLSxouzoU6npulitnoclFqQ7GWCU0LOAjCVx9RDEFwETUhB6r8Ld4sGhqQl8OeGV-6X75kAghdRGv8JS0-LtyoiMl9_8tnzeF7bXp4qm-dj4ZOIHqHJixz02d2SQhPKUIKUpheky20udpj0cY3PRZ5WaBZZhhW9sZ_5O4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fig5F3vUTcOL_I7afhQbYouvixpOSOEeOgC6yIjtkhkGxEJ4TQUjGUrc6S_jmF3JQVBmQQrBBtlUnwsmnQjXND7kjiDNXoli_izFfmQjMbOu5hb5COIfsenoKrOlwScg3DRL5N0xL12ZYF5lVR09902mnRqrQHfF-EhXGt9PHuJs0eKCvqyahLcLMDNS7hS3-Dzltn7dGPxkub7p9By8PQZAedOn2xoDyvfTI6ibxL_i61dTbbXSEHnlBrnUCgqnzhRpMHy1VGKdC9Nfuu42wHjECRwo5IhxBEYQQeO5MprjOdi4cQmnp1glNAUt2cwSKHu3kDif7fWZo6RignBsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=n2QH3p9FuMUwbVfYCptm_qBzSZLSbkrMcbn8dCVBVZIQIijFjC_o9pwU2pl0J4j6AQAlcR2eo3qemM0SQDrJBhi3o-p0BABWV2HMOSyA6O-VlNdROf2FGx7V04egelO8h1vGnUkcSIpWO1eikhPFC-oHhRfV0zJmuhbV_guM2_tYG5B-ArESRHrl3CxyJPf7b-5oRWQ3np-G6WZevntTwK3NqgnJ061dR70R984t7CPZHc74ZkeXi0bQfNTx-Su5sLvqy20wFJgFEjtLn3i3RWdl71BIz_cPx4mS4ex9pBl7tCMNE9ndfIQvatHNp1sLxVaF3nwkAQRTHjIwdJwwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=n2QH3p9FuMUwbVfYCptm_qBzSZLSbkrMcbn8dCVBVZIQIijFjC_o9pwU2pl0J4j6AQAlcR2eo3qemM0SQDrJBhi3o-p0BABWV2HMOSyA6O-VlNdROf2FGx7V04egelO8h1vGnUkcSIpWO1eikhPFC-oHhRfV0zJmuhbV_guM2_tYG5B-ArESRHrl3CxyJPf7b-5oRWQ3np-G6WZevntTwK3NqgnJ061dR70R984t7CPZHc74ZkeXi0bQfNTx-Su5sLvqy20wFJgFEjtLn3i3RWdl71BIz_cPx4mS4ex9pBl7tCMNE9ndfIQvatHNp1sLxVaF3nwkAQRTHjIwdJwwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=vagnm5LWDLj7zKZB10SLQXuIDVNSSeFflsSPZ_nq5hXKPvgeBgYLk3SeuTv-COK9pZtNP8wAZDy5ulya7KTthJH1mWIr0iHnNA1FGG-EFW9LDpvoS6HUPskrq7fXOHDcNNMlt2Ayr2zsUm-CBXAzJI-VbGhxicGqfX3oaQXvgZHtW9krRiCQ7EMSrdSkh4lAeKTfryVtMdk48_I5HuskJEBv2YCkRWFS0OwCNZH8zZRLA_LcmWeD7InfdFMMrpu7voq8yNqAAiNfRM1OvwdZEItqc7BdYGdnhPR-m6zCWmXFsgeqjg1deMsNvYIr-ukaHPzEYYwTIcxQzd-JfcRl5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=vagnm5LWDLj7zKZB10SLQXuIDVNSSeFflsSPZ_nq5hXKPvgeBgYLk3SeuTv-COK9pZtNP8wAZDy5ulya7KTthJH1mWIr0iHnNA1FGG-EFW9LDpvoS6HUPskrq7fXOHDcNNMlt2Ayr2zsUm-CBXAzJI-VbGhxicGqfX3oaQXvgZHtW9krRiCQ7EMSrdSkh4lAeKTfryVtMdk48_I5HuskJEBv2YCkRWFS0OwCNZH8zZRLA_LcmWeD7InfdFMMrpu7voq8yNqAAiNfRM1OvwdZEItqc7BdYGdnhPR-m6zCWmXFsgeqjg1deMsNvYIr-ukaHPzEYYwTIcxQzd-JfcRl5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=QYLATOyo6rN_QALrKXbWkGXxmD104ro-ueaqBSPcHKrgNxAHOSnx0Gs_ZaqkBKAuuWX06vhAzRq1yO0BXM4qNIw5CNe1zh0MNQt2tCsn9jxlQc1khy296u1j7M2NL0XGijBlNP1ffZ8p4mnR2OJKZC-DTMlz2e-nJ2bekDHdXMexR5AuefioF-YStoEv8R5_uX620LB1jEpnzm5VdMgAApOYNMYXnjY7Y38bJ2vr-EIsQm8OKFUgieYdsMD2GLVL3UFwP9ibw_K2LtVz-foS30rjn9Ah5LCrh6F-oIn6Bcuh5tZ6OB09bYV3fJSxj7dSil0il1VJS9jsZf0qZdJNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=QYLATOyo6rN_QALrKXbWkGXxmD104ro-ueaqBSPcHKrgNxAHOSnx0Gs_ZaqkBKAuuWX06vhAzRq1yO0BXM4qNIw5CNe1zh0MNQt2tCsn9jxlQc1khy296u1j7M2NL0XGijBlNP1ffZ8p4mnR2OJKZC-DTMlz2e-nJ2bekDHdXMexR5AuefioF-YStoEv8R5_uX620LB1jEpnzm5VdMgAApOYNMYXnjY7Y38bJ2vr-EIsQm8OKFUgieYdsMD2GLVL3UFwP9ibw_K2LtVz-foS30rjn9Ah5LCrh6F-oIn6Bcuh5tZ6OB09bYV3fJSxj7dSil0il1VJS9jsZf0qZdJNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=pODe_QThEgdRZJQEhD3ftplJIhE0Qf0HGaE64EpHRGaawd0JlqPmcpy8sQO5ES46jbZd0zNE-qoYuEdI6wwFr5jFg_bBUldu8lHPoEdv7JZY4qw-SQ8-Trxzcm8XCvTEH40J6KtQ54wh1gemCoxqioPaabBVwAmH9PToemPTNhVl-1QSQuXCZxeprUV4HIkvK942sr2w8U8QNFUaWrcToiQ3xrNdHDHxeQepO8DxEmJQoeRTFw7ydoLhO448RBwCJffR2VrZUv8__rAFunNoezxxFUHivuEDN98mZCi0pW7Lf35XzQ7UQh3rkGoNOXAWETbdeukEax7H7giZBoiDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=pODe_QThEgdRZJQEhD3ftplJIhE0Qf0HGaE64EpHRGaawd0JlqPmcpy8sQO5ES46jbZd0zNE-qoYuEdI6wwFr5jFg_bBUldu8lHPoEdv7JZY4qw-SQ8-Trxzcm8XCvTEH40J6KtQ54wh1gemCoxqioPaabBVwAmH9PToemPTNhVl-1QSQuXCZxeprUV4HIkvK942sr2w8U8QNFUaWrcToiQ3xrNdHDHxeQepO8DxEmJQoeRTFw7ydoLhO448RBwCJffR2VrZUv8__rAFunNoezxxFUHivuEDN98mZCi0pW7Lf35XzQ7UQh3rkGoNOXAWETbdeukEax7H7giZBoiDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=AT4iIWuPtsp4hmhMYarvhhn3sT6m007wZ-4bTXZCT6w-bLuyZy8eevmK7zu3tH3g3N0rS7j9EVKMPb9MVgeDxFhffRtCcqPE6KbKYUOwHJGlW32_IU9xdQ2LRzTo4aMGpiYbCRuJ7dSMtwqWReL979eBlmjtCs8g49Pd2QRQwfmh5rgmBDARv05Yk4RFcXWdBSPD9mDbha6MGwT46j-Cqcn4zMod2BTNNjsjDpbj-7eRAkNv6S1q0I8JOR0VlIgHfEIYWHa4pOSgXPTeI5pCeMphBI1vHKX6_70GSOt83iy7e7d9qJe623qSe8F8weFXQbWEGnn3UXEaREF0pqNn4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=AT4iIWuPtsp4hmhMYarvhhn3sT6m007wZ-4bTXZCT6w-bLuyZy8eevmK7zu3tH3g3N0rS7j9EVKMPb9MVgeDxFhffRtCcqPE6KbKYUOwHJGlW32_IU9xdQ2LRzTo4aMGpiYbCRuJ7dSMtwqWReL979eBlmjtCs8g49Pd2QRQwfmh5rgmBDARv05Yk4RFcXWdBSPD9mDbha6MGwT46j-Cqcn4zMod2BTNNjsjDpbj-7eRAkNv6S1q0I8JOR0VlIgHfEIYWHa4pOSgXPTeI5pCeMphBI1vHKX6_70GSOt83iy7e7d9qJe623qSe8F8weFXQbWEGnn3UXEaREF0pqNn4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qBm9Nh7UYQ_p31kmnr6eXyzKO2fTAefY10yCrIQp01-loKqmVTbHHotYcyJoyTP1KtuEFjAprET3Lxa3ytpNtqh-PAXPP95EG4UFCeyek1qqSpXKiMfpg4f6SUo2NbdOJl7bs6yDCOZkjT9TGhdj6eh_3tA-wcwaL5PWUEDL59VLlrWOpaP6oRvhFNzVjatcprvC-VmGhxM4nZ7v2YTGkjeV2Nq0QAkNIzJxHegg7-zLdRnn-6xCA8NJgXrOsqNFUHRx_K00uM5K1eMSFyheDvHWOdOPRloGpE1N2MXf2hSATqTX1jjJXsGLfBwQ5VNvrq8xZo5kaZkzNOC6Z3eJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qBm9Nh7UYQ_p31kmnr6eXyzKO2fTAefY10yCrIQp01-loKqmVTbHHotYcyJoyTP1KtuEFjAprET3Lxa3ytpNtqh-PAXPP95EG4UFCeyek1qqSpXKiMfpg4f6SUo2NbdOJl7bs6yDCOZkjT9TGhdj6eh_3tA-wcwaL5PWUEDL59VLlrWOpaP6oRvhFNzVjatcprvC-VmGhxM4nZ7v2YTGkjeV2Nq0QAkNIzJxHegg7-zLdRnn-6xCA8NJgXrOsqNFUHRx_K00uM5K1eMSFyheDvHWOdOPRloGpE1N2MXf2hSATqTX1jjJXsGLfBwQ5VNvrq8xZo5kaZkzNOC6Z3eJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkKp-xX3cg5sm44Q7YdEBEnPKtcpJ9M5NNQCNX6nlg-XpsAIlDpTfbE4lvaxtlkDboq39YDrfHcHTYXpUgSi4_lV9JvJruBi6CHXat1LDBU8X2FRJXxdtoq2jCgVbsx79TrPrspwcQJBWMSrqYAalOkiyxjOWcB95HC1Tmx51vscQXBKpBNjsvoqWFpbLQEFEtehfpUH0UlJJY5l12bXEfvF3OcYEGan04Ax-Xa72HUkkUKUGWDX0DptklErgwzMVCKdn_vD0xqM3fEvQeLL7eKD__W53niKSR7KSRIav-Fx_robVBrp81GHi53hsr2y3ma2JQB_mgdOXSaEjUwIjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=dE3XAzHS_iYnn5Yz-XitPhvOAaezKaVnWD-cjWRWO8fkVNcopzRZuLhaq5OK2AoMzFZB6nFQYM2IbdcCPC15c-TgYMqvU0xo1-ce9mdvWwE2227mS4tvvfXfRoGq45l3Ud1XOsJiWGM9R_Us1l72F9358lQnQ3DwvgbUCmooRHAFnG7iDOfQxuv63SSHUG_4s1mu6uh8gRcHuwEOak_SGEbzqMCc_sSojcrLESMDi2-ua1E9hXha72Mpi9gYnxdmfjeSpyOy8YP_HW0lFmKKO2dTKnUSun1sOZFrEXk7oEumIAUFEbLFUscXRzvrPod12X4FWy-amhMxBT9YE6wPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=dE3XAzHS_iYnn5Yz-XitPhvOAaezKaVnWD-cjWRWO8fkVNcopzRZuLhaq5OK2AoMzFZB6nFQYM2IbdcCPC15c-TgYMqvU0xo1-ce9mdvWwE2227mS4tvvfXfRoGq45l3Ud1XOsJiWGM9R_Us1l72F9358lQnQ3DwvgbUCmooRHAFnG7iDOfQxuv63SSHUG_4s1mu6uh8gRcHuwEOak_SGEbzqMCc_sSojcrLESMDi2-ua1E9hXha72Mpi9gYnxdmfjeSpyOy8YP_HW0lFmKKO2dTKnUSun1sOZFrEXk7oEumIAUFEbLFUscXRzvrPod12X4FWy-amhMxBT9YE6wPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=JW_MHnU5tYpkOtoUtrltxbJToANmPspstPWsQoTCpfpXGTsp931HGXT85_9blW5de7hRZJ9Bs7fxsUhUBkfW1aryGUny3LPn9_jUG3FuFF0EAtmuc4XxG7lh_oeOAgNI5vZMsq7yRIJyfw6TV6F6Zj0geSOYB-K0U_lmLbWoDuhs3lyKzmmsbu49jhGayFWrzVLYo65U3XB4DD24Utmn-rPqFePR9mN1CxUR9MCxpGNre9C28lPAcBvEn1AGC0XUWkeze7rzO5I4e1AEsrT-0q3Xujte6ZZfD4SV4z0hBkXT7T47vV_edy9TSxPFi7lxdoAbRaIBjwcQcrWFTFep1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=JW_MHnU5tYpkOtoUtrltxbJToANmPspstPWsQoTCpfpXGTsp931HGXT85_9blW5de7hRZJ9Bs7fxsUhUBkfW1aryGUny3LPn9_jUG3FuFF0EAtmuc4XxG7lh_oeOAgNI5vZMsq7yRIJyfw6TV6F6Zj0geSOYB-K0U_lmLbWoDuhs3lyKzmmsbu49jhGayFWrzVLYo65U3XB4DD24Utmn-rPqFePR9mN1CxUR9MCxpGNre9C28lPAcBvEn1AGC0XUWkeze7rzO5I4e1AEsrT-0q3Xujte6ZZfD4SV4z0hBkXT7T47vV_edy9TSxPFi7lxdoAbRaIBjwcQcrWFTFep1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvik2BsEAak3h1t_pemomhwbuOdb7YWMdmlEWjUrW_IdMwngdSyZJ6bkfQXGL0FiJJzAjeiT0R_4cxK1SfTWPFEYdi1MI_deYzq-1ErOfXXK5Kv_EbDw9NhVgB7zOkq7L-q8cpNQsZ4FyNCTjyJG2H52QDIvlMS-Am90fHlla5XQvvwGzfDDv7Q9OKgJXOuFjORoeAMQUi_e9lSPW4yFuLvOY31wK-rznQkkzMAWVg-5VLpu0p_wAHoHY6xw7Id0VV_wtQ17KM7yGOksqq_IDseTr6ZpzC7DSxj5iETxrnhz9BYNAR2lenvGXH1QqxalK9DDa7WaRk7YsZ1J-P20Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0QD9_yaQY9WFSm4JHwTCICXoaxY0PpT8hsyJi2J0y10d2UqnfG9ZW-nZQ_mHm70YIUGLD3DZ508shBzBXXebWoznuPvf_aMMcS4TaxX665MpjdKbee6bonP_Teu61FOjuoI9-zswLjoanak696saBWETkGs7DXVnhxM2WBo4Wz14pT9LGHBAvYVqV9ZAz_RBwf5W9c-4lWNDHVmizukLqICFI0rRB0_UanoKTHz6AGa5FGaqZlYUgmoLq33wJJaKUpYk9Ct1PsrxiHsMk9sofUWJ2ZyfQLE1UCW01SWlfpxjjcwmu6noxe7J_7CVbN8BbV_cE9JqNZmJ3RrWseeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_X2EeIdQFkS4Ydugk03PvY2KEBE2VvUOH82JjuXbcq8eI827xqmj_mFOO_gAfQIFEqsSOgUCa1w9xCWoBBNkl5H_rnjqu325Avej-37sZ9y1-uDyeDclXg1XkgzL0p-Ndp1-NiOP67Tdjrnb4NfrAroPgtd0RkLiz69vNBewLIFRCDQC7MQXsaf7QXQ2AbyDgz7xUYMjuW40u7IxZqvlGJqJh599gunA5sTaDqKIT_BYagmKRsw3gyfhHrWZ1mWbDvgXV5Io9BTU1pYFYYcAEt-sMKC0uo6yZPSTcRCSzs6y-Tu2C5Dmq2mnk_Xun4TuiSwhkjK8YfZUYzpgBEpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg_EipDk1jsQzetzsN9KA55Kl8umeOpSepQLdmzZ7g5OZGmUG__Sj2_oGHAMmPWwZ5Y8ANSxBN5UziLPk-K_owXI_x0ydCOScqJkMVOtWXiIXBbD0q_6j4DaC9Cyv9ITR8ehOaZ-YNFTYVbaWK53i3UkZD2oz41GjiR5saXkno9ZSYvtJh7cEDp7iP2y53uKalZPmq9JgrZDJnXSC0vUNN6HBgKsJxyoxeMkd30NiLMXI06SAC9W5ryILfMoloTyjQvd9b3lgU27ghAs3tIRm0jqJR64O2LpGQeS4CQuFD3bn5sQ2XLlF6Zg0RdHKdN2TesOd_TNmsuy-5RS4YxBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDF2fn31BkgqIe5dWx0O1DuGtuAUndOwTYmw_qdMOuXM2rtkls7tTyRuSjIPTFxNbLkiPM77OSSlIsTJyOsaAwxgGaPkJvNM6GbFA_p20gPJ6bQGd9a0oVQonnedGGLLAcHL2r_dG0_yeX50Ld8xm5x5DHlRj37MACAl30DRI4YCcMjNsTgm3f2Z7fNtFyCszgQI0NCSJYWfmvrxRS8aWukW2c0xVnEQAwwV84MGA_-7jAItTBcdNT5op15iL3g0eK1f84t07FPhXWi1EaTtK1vqeSn82fbTNiDwAfRbb4Rhe13EMpBqjSzWu2AmbK21Zj1q4h_j7lgmD0h6PKf7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKvhoug7Na8ctOLMULcWy6MbguaqPkOaB5Scc4nHUaIXGLkUuhQKiEw_6SPDvqxxgd1aeb4pkt8lJqkHk7XsL3-rR5ixFPF68AAG6BJJUoYSqFyqySgPoxYo2BjEEZrMgCTVpZ40P-I_Egw6Fx1KV_zx7e2Ht1Gq6HFTYbYLdM0KfpYZykT10sqnQ6YKtuUtr8-nSlej24iJtfxrPukY2irvANkKsUwiYKS0kSXSiRbFnlQqv9dw5lzlM4CuDLD3D6vay4akHSXc4yaHaPbN0T1eC1CjxaKvf9ZrPh4qQSUC7uKaHsmJql4n_btRDlfv3DKYWAvec0zfnBaSwnWkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TF_DI2c2tt70CGmZL92p93cNDrcteVGl-yjoIzSuZJlFefZie_QO6jtfEESlSearGhHGMS4BOTJTClX-DH2JQKhNaImGQtDYLz2UGX2oDbAMhW5th7lTJp_BernAyYFkWu_AXf1wJFqdQyI9PE6fBWBoI8B52IPj7s_zM1sGdFDPMJ01M2KLXUBQU29O9l3qFhhbePPDoDwrVIuxExSfb_iNmznyLwefUzB1sUGba38OknwXUPr7e_oPI5nlXWL6uBNzUeQ6D2c1meBftPI0Zkjfu3JfzfAKOH_3BOl9HxHcRZXZemahRcYtAlgIdp8CzN7L3YCM4LsUfbRRZMwfgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqIWRWydDrADMwMqvoKV9fdzZRtniq_NA91EKzPEy9Un4WIbO6I-iLJ_kHlyZeeCDyR50RCWc0_aKhKjqLvq0QYdAyTGDw3pxqRLpv7iWvGfBGhHDKfkvWnIKlf9h6qu1sXqOeGEAh2WrZYNjflLyDR06PhrqbqH5KqGMf8mwBkgj9DixZDb-QPXSKPPC6a-0WEc-pRB4RpruWY0w2mwsaHZhFeEQIg6QDqI4UWoIu46s684T7dvpon9phTKlkdk0X2PIavwg3wCSjjFQvVzmhBUQRleANg01V358bs0AMw579yeF7SfFVkqO3I2e3NyET2ydODdaV11PDvzWATRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHiiFAcxr7zd7vFnnU5Zq20LJ0CSMc4Airr9UuPfG5_sym6b4vPYrhGCuZB7ImDlohcnEEDxuygnKis_kLNAGkuCUL7eU_1MUp48J_PQvuIER4olY7i81RqmlTYiluaH9R7bJVcnxAuJ1kqXsPgpsj7-zBmMASzOfd8gvtrNEsusM4Fdv9g2uDhBmB55kON8u2BhQPwSWVBtSqgmVrc2o0sCWDgopDz3Gm7kIB5ljegsqF0bPQJr-XamhnNlPjn5SnuZl5n9N_PLEqwTAa1Uujd1HVn1RkexGVOxU-fQ8K9ybKzWh2ttkiCRBrz1WlfYtQBmBWM39Ik5XgzilO7ieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrR-Lyj9Rt0O-m-ExLoNgwQRDgi65FI_IiGBdiZwlCI_89lVfNiRdOCdHri95QBfVIjeFwb7Lpb6HtcuID46d7_YFpNUWv3mFy-Rpre8URHHetAyF598UYy1qfNneAw52YAvPkR9oqutXZdW-Sy0RfLQW2rfrOImjliZPQGlcZkHBdS0qUXIMd9xr7uz0D1iQMO7k78iAogE9wD4szVFZaHHqO9PI4BSpcRf5lqD2acvf8LZhuaSm_Ajvmozp_LDPGPNWEzTAAh7iAOcVrjElYQnybIXkfwsVsZXx_9bDxRsgBwCMkAIPYeffUitsspjBnODPtUnIq8u7bHFuNTAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz_IgotiJ0yiVnrA3xMjVEAz1NTPMH8HyjUQY52mWDWQyiYa4Rs8eiJE5moXIaUbDEVEvRojj5F4MUnFo4ZF4wm6jLscnJumLdHCRSWXx5IsCGUbRLUOPircQEsMSzKyYRc33UGu38PSaHG7VDeldXE7e69pTt7vHus1llObktK5qcJVJRwpzZKMyrK47xn5YrVF9TAL_m8E5wi6jLRNSsnioIe3IhbT0WAATsEuaqfIIdabU_HJ-utxyoFXTq8l5BdUU1S4Pxb_mYR3taajz4z-_uCKh1ey17Ky_KzLoIeubCs3jmqFNDWHB96S-IowTQouTBQNLoo3fcaBubr9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Tvt8pDyBiEMB9rvFljdlUBaqGprkTbj5zboRSSK1FvRMqQwPuhHoDvioLcwwCHx63etAgugod_RzumrwPVWUx4Dm5tgdaj6EWCV9DfCSs8HE0qSdl9uDOY8wtbYZ6A7Wxpl53LQIRe9s2wR_Wrwhu7SadfKg5qK6dgzAZeXLZG6L4SDViwCHv45Ur9GPE5PRQbE0IAzBckgX4UHqmXDZOc2wEVXAZyYT-rmR75EJm-xRPl9QuQuOC_FOSp4JeQLSfmDxAqN0xkCkogJRoP3icryGnNUrquGR6k21t7kIWATNhWh8VxOh21UeFGgiXfgwUvYx-QaBbrI6yv2AGMCVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Tvt8pDyBiEMB9rvFljdlUBaqGprkTbj5zboRSSK1FvRMqQwPuhHoDvioLcwwCHx63etAgugod_RzumrwPVWUx4Dm5tgdaj6EWCV9DfCSs8HE0qSdl9uDOY8wtbYZ6A7Wxpl53LQIRe9s2wR_Wrwhu7SadfKg5qK6dgzAZeXLZG6L4SDViwCHv45Ur9GPE5PRQbE0IAzBckgX4UHqmXDZOc2wEVXAZyYT-rmR75EJm-xRPl9QuQuOC_FOSp4JeQLSfmDxAqN0xkCkogJRoP3icryGnNUrquGR6k21t7kIWATNhWh8VxOh21UeFGgiXfgwUvYx-QaBbrI6yv2AGMCVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WK7flCwcl-E1NhgntgXocPF3uMwEKK8dLYk55uvd8VUH02y3r0ssOWzSdZodJZreu04xiNIm6nWI5BSPh9OwUaUVmZWuw3byUjVAWEPc7bYEOgB0JCP1t2pbqNcBteq5I2ihMnAjGG8_y_J3OZ8NVUEOwXoBH11-kzYq2To3O4R6RQ1v_S_3loNCdP2ensmqNbJ5DfjftfEmTTobM4x72_V-303v7CJgGfawqzCEkCp77BPEpx0WBE9bCDMg_qxlP7A0-NmQKYSmTvPcvdSe4g1a6jwtklkdaSjoHiQPVQvXvLQGfdRJf46y6EOlFbQgEg_rNwgjaXun5U9Cv1HhBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WK7flCwcl-E1NhgntgXocPF3uMwEKK8dLYk55uvd8VUH02y3r0ssOWzSdZodJZreu04xiNIm6nWI5BSPh9OwUaUVmZWuw3byUjVAWEPc7bYEOgB0JCP1t2pbqNcBteq5I2ihMnAjGG8_y_J3OZ8NVUEOwXoBH11-kzYq2To3O4R6RQ1v_S_3loNCdP2ensmqNbJ5DfjftfEmTTobM4x72_V-303v7CJgGfawqzCEkCp77BPEpx0WBE9bCDMg_qxlP7A0-NmQKYSmTvPcvdSe4g1a6jwtklkdaSjoHiQPVQvXvLQGfdRJf46y6EOlFbQgEg_rNwgjaXun5U9Cv1HhBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RevJZmDaShLmzUOAv_k0qtJIA06wl1AnkUPu7Ee7SkcknB1zP_DhnHZZOddsr7fSe6XvTya3aBnbvxoX5RmV5Xe2-xApXfOiAGqRtNEPVmjuInJgiwh1M1xo0Sxw03cqB65axV9twctIpLaYSD-LD7_iz3VrMfSdQW3riJlQ2ZDspx28b2JfHj_qfyODeL60xKzfkFQvpH_hvL0_xcucwNJ9GbwgEP-suMhp8LHYGTm5ZJd0TqbiZUSo6kiZQm9IwuIAdPwYBuw3ZkIZUhgsyjUjlCypWDVG_VCl2v3x7hIJE6VCnL-bNq6cDE9GwDX01-taP1TKU5bctsif7X-4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RevJZmDaShLmzUOAv_k0qtJIA06wl1AnkUPu7Ee7SkcknB1zP_DhnHZZOddsr7fSe6XvTya3aBnbvxoX5RmV5Xe2-xApXfOiAGqRtNEPVmjuInJgiwh1M1xo0Sxw03cqB65axV9twctIpLaYSD-LD7_iz3VrMfSdQW3riJlQ2ZDspx28b2JfHj_qfyODeL60xKzfkFQvpH_hvL0_xcucwNJ9GbwgEP-suMhp8LHYGTm5ZJd0TqbiZUSo6kiZQm9IwuIAdPwYBuw3ZkIZUhgsyjUjlCypWDVG_VCl2v3x7hIJE6VCnL-bNq6cDE9GwDX01-taP1TKU5bctsif7X-4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=E5wM86ZBuT8OXyq4t1MKLxh3gLpL-xTKfkDmeBERE80dA6YjIYplUXa-C73FjZ99_7QtymESxSy026vt2XCLJ5YLITRxom0LANNt4jRUkfukiQ0PVSXddQr9v8dFmq06xWmmmbJmmf43D-c9FYPQghuzMqMZ6--xO2BLdoaUWCULAUVXTyeiGpkUHZLofVK4v9GWntIU4DCkcA5f1Fmh6e7CixtiXmpYBXgwCbDOcxzfmQBwAK8mntP1GP8cmmMRdhfXHEStzYbGrB0qhvne-5q_91tZXGVnOt7-QCFwUrgpkG_izuaJSElFycqaToZAF0pfwJTkTAfXu7CtI-IwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=E5wM86ZBuT8OXyq4t1MKLxh3gLpL-xTKfkDmeBERE80dA6YjIYplUXa-C73FjZ99_7QtymESxSy026vt2XCLJ5YLITRxom0LANNt4jRUkfukiQ0PVSXddQr9v8dFmq06xWmmmbJmmf43D-c9FYPQghuzMqMZ6--xO2BLdoaUWCULAUVXTyeiGpkUHZLofVK4v9GWntIU4DCkcA5f1Fmh6e7CixtiXmpYBXgwCbDOcxzfmQBwAK8mntP1GP8cmmMRdhfXHEStzYbGrB0qhvne-5q_91tZXGVnOt7-QCFwUrgpkG_izuaJSElFycqaToZAF0pfwJTkTAfXu7CtI-IwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DCCyoRC2FysSQgDMSekSSd3ZY8iv6rpgykmD8esuqpdoMbHYoStflPLtroXAI8CfTSMhUsaK-oacEQ4S68qBM7pDqT6yN-zm_iwE1yLrFVe7a9gN1u5K6QqJ1SVcCWksAuZMjziKXSWqrx6YZJbCPshr438IJ1a0neBTkrEm7_xsuU-aDEF1njYUOoBvfpqazjXY2dGzHbzVZfywdghvJlbmPZwiD_7JJDPjN9XZPzQsuvFj4GXOB3NrZzRBjEn-enOYfUzf7YFTwmvfcPPWyCrr1fFQrzBVx2mkkVS65ynXZV-BHLUJGOznbYLYaks2Mb7RnKuu3SxnQdDeTxs78g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DCCyoRC2FysSQgDMSekSSd3ZY8iv6rpgykmD8esuqpdoMbHYoStflPLtroXAI8CfTSMhUsaK-oacEQ4S68qBM7pDqT6yN-zm_iwE1yLrFVe7a9gN1u5K6QqJ1SVcCWksAuZMjziKXSWqrx6YZJbCPshr438IJ1a0neBTkrEm7_xsuU-aDEF1njYUOoBvfpqazjXY2dGzHbzVZfywdghvJlbmPZwiD_7JJDPjN9XZPzQsuvFj4GXOB3NrZzRBjEn-enOYfUzf7YFTwmvfcPPWyCrr1fFQrzBVx2mkkVS65ynXZV-BHLUJGOznbYLYaks2Mb7RnKuu3SxnQdDeTxs78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mp-damDjWq4sj05phLwCY3i9SV_3X47OYj4maGHTmJsdQqV_Kx-042TQn-4dioPmrbW4HWdIHWr5jtuCWCLYnN5uikqqLMEzXBDQ723qDTbmWR-4d8OuoUQGJY3d30AD13fIizH8fSvXrxCVrbbS7BSz9pLqaHYlQRsvuypFImiEh04JWbiQIPbn7PvNuPhdAftZEATTadifUaxk9-A7mqSQAKYH0nZX2ZQmMx48fAKMshO8QNf9z-aJ4-q42Mhae_8ollxVSWU6_iV4UU-dH5QD_o0xKpAqFRwF8pmfPvRn-7G62DxOQfNVk2MUdv40F2fHEEETCZ9VwCzcPh8u4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mp-damDjWq4sj05phLwCY3i9SV_3X47OYj4maGHTmJsdQqV_Kx-042TQn-4dioPmrbW4HWdIHWr5jtuCWCLYnN5uikqqLMEzXBDQ723qDTbmWR-4d8OuoUQGJY3d30AD13fIizH8fSvXrxCVrbbS7BSz9pLqaHYlQRsvuypFImiEh04JWbiQIPbn7PvNuPhdAftZEATTadifUaxk9-A7mqSQAKYH0nZX2ZQmMx48fAKMshO8QNf9z-aJ4-q42Mhae_8ollxVSWU6_iV4UU-dH5QD_o0xKpAqFRwF8pmfPvRn-7G62DxOQfNVk2MUdv40F2fHEEETCZ9VwCzcPh8u4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=FVItSPhUR-cch8d9e3fLyWSR8OjvDiBJQwK0H4JuYwxVEdTx-EP5jQmoNG_LPSAyXDIyL57EJ4D3wfWX8AQan4NbFwpWbuPQ9swfcSfpWudJ9oiQlbsSsen0arhtC6zn8fMD9lyhHI37SfLnu8W4qJkMq3hZeKGOBMVvmCIJbDBGwbwkMm7LuZupCOpemnncdYJPzj_5esMcW6Hgke3SQI6Q4aexJ2bDqi3ITmG1wsfj3aQZuj8Z4cv2Ldx7Tz-hMRdhwBfvFBLOMSRss2KjaEQdQvQwZuf5ulguZOChl8pYUBSS-hAxPNky-wGniwvMLfleqrlHGgKPOTn-fkaI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=FVItSPhUR-cch8d9e3fLyWSR8OjvDiBJQwK0H4JuYwxVEdTx-EP5jQmoNG_LPSAyXDIyL57EJ4D3wfWX8AQan4NbFwpWbuPQ9swfcSfpWudJ9oiQlbsSsen0arhtC6zn8fMD9lyhHI37SfLnu8W4qJkMq3hZeKGOBMVvmCIJbDBGwbwkMm7LuZupCOpemnncdYJPzj_5esMcW6Hgke3SQI6Q4aexJ2bDqi3ITmG1wsfj3aQZuj8Z4cv2Ldx7Tz-hMRdhwBfvFBLOMSRss2KjaEQdQvQwZuf5ulguZOChl8pYUBSS-hAxPNky-wGniwvMLfleqrlHGgKPOTn-fkaI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFK034rPK8W7zj-T5Uarl_-TEdzIUyO0LKWkgQZDAAsLfQ3QmBUFuypzIFK0WaxARbFHN8uRE-48ft2wC-olYLuxpuFa73Q0PM36GRZ_3Dz5Vvt8Zgyj1Z1dJaw5MlNoCdjOMnZVaVz-fEcTWjJVMybskaEfsV552VbgV2KL5kV0IteOJTj_UYuBC-CgIRR98Bx8K2m5ZMwHV8Om31YeBA_a3i5mggG4G3z42UGrwMDv5mY7q8V1ZEh2xwgFGL_Agqfjb-QzGzdP73X8UOtchPW9zrXctO00gItS42M_dnrcaEnz5DPPTh14bhQTWWlWj_B__IDebfH-52cN3KzHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=eihqovzPyu7A4eP8IiLEU-Xtt4oWKvoAevHijaJwlfgVxLEdoFso1K_K3-S7bd2DW2Qv7hQRl-N-Cn0TAFz7uyWhWy4wqXcVk-xMuybJzDia2pJSN1Sx6IyGqosqSL29eCZigKF5f8Xryldjeo-ripkiUlebYekJzWl3QZAA1DQa7ttZiNR5ZTZLokZpk0SLVRK_FKMAEbSnM-ngPa7zslnbgdacD9x8v8gr_vSwZq3XE9Y43i1UaE2ThakM8a37y6ROhMkKCy6rhB1POkUjAQ7eG452REW3z2WNZwC9OAc6bJ-By_JjDuXdNWiDcWhcMbPz3a_rNmPelqmDt4z2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=eihqovzPyu7A4eP8IiLEU-Xtt4oWKvoAevHijaJwlfgVxLEdoFso1K_K3-S7bd2DW2Qv7hQRl-N-Cn0TAFz7uyWhWy4wqXcVk-xMuybJzDia2pJSN1Sx6IyGqosqSL29eCZigKF5f8Xryldjeo-ripkiUlebYekJzWl3QZAA1DQa7ttZiNR5ZTZLokZpk0SLVRK_FKMAEbSnM-ngPa7zslnbgdacD9x8v8gr_vSwZq3XE9Y43i1UaE2ThakM8a37y6ROhMkKCy6rhB1POkUjAQ7eG452REW3z2WNZwC9OAc6bJ-By_JjDuXdNWiDcWhcMbPz3a_rNmPelqmDt4z2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=jF1ZxHo_drrLD2untdKY7jZlGy2LgxdBf2OsCucDhnLr8-R-lo_1rKUF56GZUwJvOpZwBJ90a23r7K6mt4yBIhzAcSCys7tw_MYKH_9MNApHGG84WQdeCIAv6al07975PxDEBK7qThTxhWr-oCdt9qMY7zZo3IDGLvCS0yIvBpRw3ktQAzILqsR7ddzsjjf4J6QgFHZ3WEZ-n7qr4UZ_qKRld33dQxAWnIJg7ftd6j-9ifbv1r43jmB-y5iqVno5fpx5qU5Yk8omExEwHVk_wMkuzg0tfpoVMPm2jc5HshYdrDz7zHK6XtFAQDyr3PsEIiXxPg2cTAp-4llrEni_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=jF1ZxHo_drrLD2untdKY7jZlGy2LgxdBf2OsCucDhnLr8-R-lo_1rKUF56GZUwJvOpZwBJ90a23r7K6mt4yBIhzAcSCys7tw_MYKH_9MNApHGG84WQdeCIAv6al07975PxDEBK7qThTxhWr-oCdt9qMY7zZo3IDGLvCS0yIvBpRw3ktQAzILqsR7ddzsjjf4J6QgFHZ3WEZ-n7qr4UZ_qKRld33dQxAWnIJg7ftd6j-9ifbv1r43jmB-y5iqVno5fpx5qU5Yk8omExEwHVk_wMkuzg0tfpoVMPm2jc5HshYdrDz7zHK6XtFAQDyr3PsEIiXxPg2cTAp-4llrEni_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=h4F-eGOoxxzIu9CANI4ukuvp11FigKppMD5KT25By2Cc6Hn2C3HO7ecCHBPfeBTEz78c9_iRaCCk4K6BowQsYu1vxDqJstQdFVDU9UqddLFc3ymM9oaI8m7V8y7UvYBBYbqVpQ5Ad2HPlHUO3jNvu8grqOTNrsAyKUuecE3VMgWNO3PMUasW1Az25UZCUkHi1n_6YwypiAqHLgR9DUJCNBDj8VzqNKwKX7jc5yrAuYiqOP7Lqc2uKZfDQ9n2akaMTnOWHVjbwjuQHWQC5TTIapNlG6HZxTye8iyg60bXbXtQSvcCc9wZ_AtFa_WuAkEW2e1A352Ovmy7rST2GRJyjGNaJ0myu76om0WKPCIZ6DxM1mQmfksqR9hxr3CXreHSXLRZu26nNok1QWnncQ5r8i7fUAGnvEzpfGoZ5Ahy3XgP6eMIi-_F1qlL3sn5XJQVgK809TlsyGAhrDDLgh-a7jRW07jeLnFOiaUKy0RfcujjankN0zqNqUIOS9BD3s_ln8wc0NYiteQRu8QfWbYMIgNvjD5djWtTCAOcQ0QQ4y6wdhVQGEut479216UhKrEi5Y0bcrm9BcBABOTod86o1vIEqV2LbL_6PpqdoTTNA9fuKK4ePEtoqg6mUVvr4pczuaz_BnLuUpDjTP3emfQkdTZZOBS_HoHDmfUP7KGOGUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=h4F-eGOoxxzIu9CANI4ukuvp11FigKppMD5KT25By2Cc6Hn2C3HO7ecCHBPfeBTEz78c9_iRaCCk4K6BowQsYu1vxDqJstQdFVDU9UqddLFc3ymM9oaI8m7V8y7UvYBBYbqVpQ5Ad2HPlHUO3jNvu8grqOTNrsAyKUuecE3VMgWNO3PMUasW1Az25UZCUkHi1n_6YwypiAqHLgR9DUJCNBDj8VzqNKwKX7jc5yrAuYiqOP7Lqc2uKZfDQ9n2akaMTnOWHVjbwjuQHWQC5TTIapNlG6HZxTye8iyg60bXbXtQSvcCc9wZ_AtFa_WuAkEW2e1A352Ovmy7rST2GRJyjGNaJ0myu76om0WKPCIZ6DxM1mQmfksqR9hxr3CXreHSXLRZu26nNok1QWnncQ5r8i7fUAGnvEzpfGoZ5Ahy3XgP6eMIi-_F1qlL3sn5XJQVgK809TlsyGAhrDDLgh-a7jRW07jeLnFOiaUKy0RfcujjankN0zqNqUIOS9BD3s_ln8wc0NYiteQRu8QfWbYMIgNvjD5djWtTCAOcQ0QQ4y6wdhVQGEut479216UhKrEi5Y0bcrm9BcBABOTod86o1vIEqV2LbL_6PpqdoTTNA9fuKK4ePEtoqg6mUVvr4pczuaz_BnLuUpDjTP3emfQkdTZZOBS_HoHDmfUP7KGOGUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=iChn5NxxZiOICkASWm-JPlLg_cgoQKh9TGS4eAa0M_1wtLiYoxIWHGI9ya2f9zJgOp6xZOj2yxz7K_I2OprXI1gkfA_0G7m5CxyK83J57vijcJmrvo8Luqcmz84piBZhC5zXXz1nhzXSyaKEuVQapXuslwqTa2sLeJc9t2QRl_kilcPqILLeckbEd5FYc3YyernyaTWnOsYNFC409E3nC5lWT0giUzi_MJV4dc0vGETuaY3Enql2C_d7lRtO9gu4Pqi1TvXiALMVbruhgq8WC1Nqrq9fdHw92I3-7rwTQ2_iOE3ZvXVx41k1YfV-hgw3euD6p26BA8pepiEH_Xjo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=iChn5NxxZiOICkASWm-JPlLg_cgoQKh9TGS4eAa0M_1wtLiYoxIWHGI9ya2f9zJgOp6xZOj2yxz7K_I2OprXI1gkfA_0G7m5CxyK83J57vijcJmrvo8Luqcmz84piBZhC5zXXz1nhzXSyaKEuVQapXuslwqTa2sLeJc9t2QRl_kilcPqILLeckbEd5FYc3YyernyaTWnOsYNFC409E3nC5lWT0giUzi_MJV4dc0vGETuaY3Enql2C_d7lRtO9gu4Pqi1TvXiALMVbruhgq8WC1Nqrq9fdHw92I3-7rwTQ2_iOE3ZvXVx41k1YfV-hgw3euD6p26BA8pepiEH_Xjo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ItF72SYj8J-gPVu2Fus3lqol6FiU_JgGZztkoR_0C9qeCtV0ISjSOkUIlUnDYA0r0O7QBsor5L4wIYrrwZb27kVX1kKtac-WLWT_BWGkN5pOnuCyXl9cvK3lpkR5H4AJtlR-j7dnY2LFf_TEDC6zY5KDYXjb5US2yeihD55gDvpRIFFyNtJTwbXaEl7hGT3Cpb8OteLML21_Ftqv04cS5XiA3kHQMJhT3oIOWbxj6uo89hwPB0rqnGvcgzY81UTDuDwOkCLpioR29tlVeND1L1KLX9UsEfzi_6pGzPScM79x4e4DHtqau0sUh4pCiwMh_kjxGvw_s3XSoOUpERJ7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ItF72SYj8J-gPVu2Fus3lqol6FiU_JgGZztkoR_0C9qeCtV0ISjSOkUIlUnDYA0r0O7QBsor5L4wIYrrwZb27kVX1kKtac-WLWT_BWGkN5pOnuCyXl9cvK3lpkR5H4AJtlR-j7dnY2LFf_TEDC6zY5KDYXjb5US2yeihD55gDvpRIFFyNtJTwbXaEl7hGT3Cpb8OteLML21_Ftqv04cS5XiA3kHQMJhT3oIOWbxj6uo89hwPB0rqnGvcgzY81UTDuDwOkCLpioR29tlVeND1L1KLX9UsEfzi_6pGzPScM79x4e4DHtqau0sUh4pCiwMh_kjxGvw_s3XSoOUpERJ7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQnEP8UGAEmEqvh5cgPFlGXeKXMSDdxi0wkeXjQ3AHjDCaoqXVKlfKb8D4VyGiiCz87tkADyD63Z2U2ZmRRhz8s2qT3pMC_vrkk0FPiNxPgUc2_jwJJK0vgirAe-R4MrhThFES8baNDFhzm3PuJP1xl-jCE7e0vdUg3zMCZMwE0uh8k4h6pZSVyIpom_v7of14KifdCXr61QGNKNJG2SVwp37HQQqS-h4df0gxEuv99o131znvC_O9gI4X6Pb6Voj53lAkVsU1hLt4F8ovxtWBUNJZ-dI_nFchVHlC96t9Oe6PpCA4YIcDTU3QMo17TNi_z460AbAlDp17abs1oQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lg9j-od1TXFvgQv40_mfSz_POs26YNLTHzF_cNXstq_WK_VrnLUiy3zP4YyccjioS7SMBI40cbbC8udyu13UpYQpLctOq2Kbv28qrSYcjVVv7zuEWfaR_bJsJoZes6geivNuYsBkaaLrY388AB5rvUlw30nvrlkUxgdGpip31plki8NzwqqmhVARiCz4LSMurMh8nSFw--DwtU6NviNhHRiemJ_Xk96Xvbhe1qkX9A-s9L3VqVAZhaagImCam_4oGM_9_AZBf_TMHSvWVtNS-adMuAAgN5uB2FJNPnArCLgZ8d42JigWAHLoFzgT88vi3igMfnNH4b07HQrayhDRiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=aBPS4sEwcAvujneo4RajCRBFRa4oGB9qRJXj3qAP50PGiPFVKMzALKWAgNOlMu7xs7YIpbrRl_uCIsVamgcofteV39R9XWlxT4jcDnKjsvHwtmIE8OBrfkX8EjRdlpHgjHQPBAURwHT_RlwXN4Ytc3R8OGjIWwOgeupF7ZTqQFmnqu08ETN4pnPKAH-K7nUFTYwRa7g285qDtjEOh-cmRRO9XS_VmbpVa9MolG0hgYltR6xov2oIJ0dL_E7EE_OLbWl2MuQBaiy45Pvhfkf7Z3zzZZXq6jlZcrSMms8BTz66OH32AmsEmw-r4RAN9qcfksb4pKgTC4mW9H2rcMZevreKQpKH5XrVrOh5kldLnhATn0DlckW5J6fT9GZNazrYy8sip863e6ed-EbYGumTB9fqiJ4CUAyHT2JLHCPTOICvImfW4jebMg6Oxx_UXcJuomCJ930XLF5RfAqOiHXdO5CAaKc6BUG8LcvNXa4ZKgYeS94IAGjljIhH2sqv2KA4FChTdoLFZFpV1aKxrbG_hA5RVQxrg3G9Ns6kB3erEn-NX1Qz7PNMP8d1GQIpRxWeFraz9RJuGyagrdjUsy_Aq-56jDB3E7uUH0icamuZUsReWwcGOGQRWXK-s7GpCR_7sTsP7rO8-0g0UKW5nolFVgk0ZdPZseYqqM1Wp4AVYWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=aBPS4sEwcAvujneo4RajCRBFRa4oGB9qRJXj3qAP50PGiPFVKMzALKWAgNOlMu7xs7YIpbrRl_uCIsVamgcofteV39R9XWlxT4jcDnKjsvHwtmIE8OBrfkX8EjRdlpHgjHQPBAURwHT_RlwXN4Ytc3R8OGjIWwOgeupF7ZTqQFmnqu08ETN4pnPKAH-K7nUFTYwRa7g285qDtjEOh-cmRRO9XS_VmbpVa9MolG0hgYltR6xov2oIJ0dL_E7EE_OLbWl2MuQBaiy45Pvhfkf7Z3zzZZXq6jlZcrSMms8BTz66OH32AmsEmw-r4RAN9qcfksb4pKgTC4mW9H2rcMZevreKQpKH5XrVrOh5kldLnhATn0DlckW5J6fT9GZNazrYy8sip863e6ed-EbYGumTB9fqiJ4CUAyHT2JLHCPTOICvImfW4jebMg6Oxx_UXcJuomCJ930XLF5RfAqOiHXdO5CAaKc6BUG8LcvNXa4ZKgYeS94IAGjljIhH2sqv2KA4FChTdoLFZFpV1aKxrbG_hA5RVQxrg3G9Ns6kB3erEn-NX1Qz7PNMP8d1GQIpRxWeFraz9RJuGyagrdjUsy_Aq-56jDB3E7uUH0icamuZUsReWwcGOGQRWXK-s7GpCR_7sTsP7rO8-0g0UKW5nolFVgk0ZdPZseYqqM1Wp4AVYWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSl9YDgY9Ds4vwxAYntmelx8KxlIPv3fetwcf_mRORt2qrfV8sjjSXfK6id5LE1B4-IAFBNpMqIgqQ701_yyvTKb9KffEId5FUC_ccSNeLE1rANDBU1mibdtfsJDGdoi8jCELeDEa_8yLIWQbmfyihde_V68Ccz5YV2hBxJmtd9Wk_O6uSzr2sg7nQK3q9F426FTfORjPOIkyoVMDM4iISYJ9S4fIRWmN6aWLF6nW80hb6jiT9IXV3zU8hl4y0XRc-k6RRa9MIWamjG1L6dV2A1SEzL_0JX2iy0WM0by6HBXYjP4Oen2ntBSiOMfIi7X2z3QDEnT7RiQsu-qO8-7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7Vx0gYz6RAHDJDQKhniTI723gybQmyNx2xglnJoY3QhUReTfugEfpprsrDYhK4-1qjwALnN-LkkqcaVmFjNSwyQcyZdXlOGkZqt-aVsNY3x6lBD_16kSoB-oG1R7PsVdoXZToKLkrrmPqvjqQgUUZOU9sbX7kvyD60hmPwHS691cP8qAiy70t_BSBHthF95vvq3AoVDJydXhSCOi_phSj9pq5PUYGCVEF92QH4R4uEjNzvY2QeK9CKHFEpcLhX3wgtJB1kYvsHc3v0wd3FtqtJ7q-coL6sDR2bPER4OdvV5AAGDMYjsSXTqAbD42lN4_nKWyOdwbw6ApjOi7FMxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np5fZu9T0rskq3q9KVdBEzwFoDhMJ5whk_5Kt89EL65hAR0gkSWMbKB6DgaHobJ3As2P5hzJQSN7ALMG2zhkgFAG3B_hPKdAbIvrWIcjrfXRGDoauDN9oi6PY5sx1lVABmW84N_7wpM5dUTn_LRNXq9VjqIKEGHQqGYyKcDIxas5cJ-WlqMg84_-ei3ppPdkCtXh6y2mxwdonkpoZS0lpeoRoY9LkpB_3DMLLo0yl77tUsMWvIXytUrCDwZNllAMo2wNh9dKTTbQn4K_iqO70Id5jrM7sppxesvlAKPBrhibWubDBpSjPMfyruH1iJZKGG6YwhbzDR2yfKYHZxgqnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pveOkJ1Z7mTgNqmvPzEvPhKbZdJCHbvXta073WGC4JE9OHxbvn1VOiUObjTe73OIQBHBqMLhodseVN9DvHdi_IswxKuXn8CBGrCq2OXGZvDe4DK2flKqyq8XG1-t-gNtCl2JpHNwUFtf08GeJJ80mfJdtZ0-hvSOmbKwVdjEDOOanpWlp3WoHXH9U7vCfDVihDL2h4TZaOzHeMHw2fIjYlplUpKZuD6QrBLCmJtnRVPD4krV9sx0-ueZ4j5o72fUrZ1nPeERU9iVujint-jRr60jDelSv5obbGdZu6o-P9L4hAmSCEwcfiy1Nb0QnI2FktolUvkCg6WmF_ITlnrUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CwpbdECrd_eE9YcQyl7c-lOM84FF871hYf2uP7t8ZZoqLlz1ofKucoEGHzUYB7QdyLqxHp0lfJorwOUw8Kau5VKysFTCycQ6Y86ZufDFNKf9hX3mWR-UUqfUdyBnYgKV-yQSENpzWRNA1cdTyt6iJS_E3tmTao9vPgbnN0wSE8sWdfFsxD5r5j0030nDgpZ2AIr9ZlVhEFVVX6VNTLNlhwGhTibDjYlf09sEcF8EIYUT8pIYCQyn27gGEPellgB_47PhzuVWRHeMVk0YkekfHSi9TIvEiz4IOCaMt32nIh8k4giw7IgNJh0Ckp-SMkq5HAvUnpiavjrsYsSKfe7lzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CwpbdECrd_eE9YcQyl7c-lOM84FF871hYf2uP7t8ZZoqLlz1ofKucoEGHzUYB7QdyLqxHp0lfJorwOUw8Kau5VKysFTCycQ6Y86ZufDFNKf9hX3mWR-UUqfUdyBnYgKV-yQSENpzWRNA1cdTyt6iJS_E3tmTao9vPgbnN0wSE8sWdfFsxD5r5j0030nDgpZ2AIr9ZlVhEFVVX6VNTLNlhwGhTibDjYlf09sEcF8EIYUT8pIYCQyn27gGEPellgB_47PhzuVWRHeMVk0YkekfHSi9TIvEiz4IOCaMt32nIh8k4giw7IgNJh0Ckp-SMkq5HAvUnpiavjrsYsSKfe7lzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=O2z4qX6fKEVagV3JnVDv_ybcZqllKlYzs3TrZYuuBebLCEQauZRlIIoOU6ebXMa6Cs2qnRqPQN4vKyeHCKe3gROhn5NvDUsoHLb6g-mku_IgEebICy44oZyex9wHXg0l6kHoPjEytFC_uzq0ARa2ozf1Diubx7DXTnrHWaQ9F1Gz51f5R5RaaCV2mZWmZfv89AO2fA0J5ZqG9sghJOwipCvjmjjlBGmcYEPbM0Ih22Yp7HudgkpEsPB3NLj8yHpDJYy3s4304ObQQkG_JIpnOrP90yNLK6YuGptADT4_C3fMrFr3qqWUK_V4m3fXpzhENKAwfA6oksLGLxdL5bY-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=O2z4qX6fKEVagV3JnVDv_ybcZqllKlYzs3TrZYuuBebLCEQauZRlIIoOU6ebXMa6Cs2qnRqPQN4vKyeHCKe3gROhn5NvDUsoHLb6g-mku_IgEebICy44oZyex9wHXg0l6kHoPjEytFC_uzq0ARa2ozf1Diubx7DXTnrHWaQ9F1Gz51f5R5RaaCV2mZWmZfv89AO2fA0J5ZqG9sghJOwipCvjmjjlBGmcYEPbM0Ih22Yp7HudgkpEsPB3NLj8yHpDJYy3s4304ObQQkG_JIpnOrP90yNLK6YuGptADT4_C3fMrFr3qqWUK_V4m3fXpzhENKAwfA6oksLGLxdL5bY-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuZkqNZf5V21KZbI-Q1m6Kin695UmB04XLRbt9QuLl0kRLjkeMSsI_X86eeFP46n79hwnAL6nR_2b8aSnxMq77zzKlYE8I3uP7ccUm5htnC1DAGFZN6P3BsMmtcFfWP4AJcOe9mOE-Ceocwh4iFcQKFAUyejgSiFkAy4tt97w11P2rXdO5wor-0tE8MhovilXTf1O9FfAzUpj9f9Q6Wr15QWHJOdXyZMHxjGol9MYphYsnT3GRL-oohVtbDg002ecH7vK2Y5G9p_JnCPcz3wZPc4MHfOV7clofaDqQC2z9YQ3sDvsfws2zUZ4bxeMLxyldepFxjefTHAYTG71QQpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=X-i09YWI4JS6T9igAVRWbBQjgWGBv4rOZLxBhomTvgKoO6DwW4-Q25aeKzx1CH3Hf_82RCKbHKVBp8oGeVVq301fq0QDNbtVdXeDQCOcWlh1ba1injO7rbdJvRpwXdRYqx7USUdHNYPCG-fWRhm-cjwDiZpIEmpxQzYsiLIZardQxZfB38Gx9tokNVdcx8nSLylRxYY4ppCQ_vuH-mi1LtES1dZHOd1he5garfkDcYsk8PFQfzvY4Tuut2cAM34cJFluK8832vvrzChzlC36xGD_iLfvxZz_AwWXWS2_LzYCOAmWU3VOuIkd6-IgIJgz0tJMmowH4oSjsfQUIcn0rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=X-i09YWI4JS6T9igAVRWbBQjgWGBv4rOZLxBhomTvgKoO6DwW4-Q25aeKzx1CH3Hf_82RCKbHKVBp8oGeVVq301fq0QDNbtVdXeDQCOcWlh1ba1injO7rbdJvRpwXdRYqx7USUdHNYPCG-fWRhm-cjwDiZpIEmpxQzYsiLIZardQxZfB38Gx9tokNVdcx8nSLylRxYY4ppCQ_vuH-mi1LtES1dZHOd1he5garfkDcYsk8PFQfzvY4Tuut2cAM34cJFluK8832vvrzChzlC36xGD_iLfvxZz_AwWXWS2_LzYCOAmWU3VOuIkd6-IgIJgz0tJMmowH4oSjsfQUIcn0rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fl_ugZK75NQ5AzZS3WGgeYkCu-FJIfPk7683jZwd-UQzsUf63_NQbXjQ5OzRG4qxieV-GaHDPn5ERcgNU4SWUcw3k0BaAHBjBCc-O0hmEFqJSdpphK1SWcGR86mM6z-K_pymacSaohf858eLjTgJ06e5xNyy1SGkmCp1S83gDyP1vt5Up-g089BlZHLqFao7JAls304GNs8v3D52igpNY-3p59oTG8i7j6kLwpwRzlrzgzndXaQgud4SzgMdFCtEjVbmAwEtpSK8WzswcdkE89YUMQLjRUoETGXL392lLKRO-o6e1w2h2UivATp-2u3pzR3AVjY0SGjb643201zSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fl_ugZK75NQ5AzZS3WGgeYkCu-FJIfPk7683jZwd-UQzsUf63_NQbXjQ5OzRG4qxieV-GaHDPn5ERcgNU4SWUcw3k0BaAHBjBCc-O0hmEFqJSdpphK1SWcGR86mM6z-K_pymacSaohf858eLjTgJ06e5xNyy1SGkmCp1S83gDyP1vt5Up-g089BlZHLqFao7JAls304GNs8v3D52igpNY-3p59oTG8i7j6kLwpwRzlrzgzndXaQgud4SzgMdFCtEjVbmAwEtpSK8WzswcdkE89YUMQLjRUoETGXL392lLKRO-o6e1w2h2UivATp-2u3pzR3AVjY0SGjb643201zSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=BIxpwOcJqvBBMASCkH2OEpwSZMzYDpjz9-WF5p4oYtqtzWN0PXdJZRNmXfPaQUP-CTacsOCtvCWP4wuYVjJBqkVF_QiXQdPSv60IUF3khSbTs_xcDmqrDdVQeS7vrFu-sWzw9pJIzwCp1I9I6m710gjx4_yY8KUjb1D-_eKF6pgfuxkNl6Ccwt1aKIxjbSeHHTNZrEr1RESeIM50wkKUkOP0_KQGJVd9FdvvEQNZkrNS4QqnQ1_hSIrLfaYrsi_CdBvUl4nWhNmQTz18EG4yGO4n6390Cfq8vXsAlYxbRCLLmLWYedbZazM9rQoT9HnJLmlFDnxdLASp72A5lY1-aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=BIxpwOcJqvBBMASCkH2OEpwSZMzYDpjz9-WF5p4oYtqtzWN0PXdJZRNmXfPaQUP-CTacsOCtvCWP4wuYVjJBqkVF_QiXQdPSv60IUF3khSbTs_xcDmqrDdVQeS7vrFu-sWzw9pJIzwCp1I9I6m710gjx4_yY8KUjb1D-_eKF6pgfuxkNl6Ccwt1aKIxjbSeHHTNZrEr1RESeIM50wkKUkOP0_KQGJVd9FdvvEQNZkrNS4QqnQ1_hSIrLfaYrsi_CdBvUl4nWhNmQTz18EG4yGO4n6390Cfq8vXsAlYxbRCLLmLWYedbZazM9rQoT9HnJLmlFDnxdLASp72A5lY1-aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWFl6eiJBXEeVKrAX8FGXpr528MXIzcQVvabc-JPtTC-tASksrFtqqNUv77jneOAbWtoF913sz81-gVu4vUHmNwYrH-CCVcw9y5MZqvmNvIn1oicoJKvBkX6YrQhZU1KpjCHYu8umFzwoU9CbxQ8rkeMlP4swcdFZOYwXtlopC9MF9sI9Uw2zYjlK3hyE4Sd0p0-BiRKnqpc0UIAH_3BBrBjDQZbg1T5uythfhOzDALPFjY4oaEOFM06Dy3ywpKG6rasv2w1KhIQ3JenHMY_bSjhFEsYI8QRIlYHC5F8xngBra-D77-dsfV36zAkhZs9oLKBbBZ-twifY903WdHQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=HfiP2X9PYgzAXA3a5mJ4iNxLGsNCYROZ0Db2O4W6AjsJUrELOZBaX7uZX8zZMMMAoEWZR2b4NYtDQmjfmxlQgvuxig_-uOem-8DG9m1wBTTPGoHnszYRgBah1IL-mRSK7rvFHX6hPxU16CSFUgTacwlLYB8a3Xjs_YIy8PpBejwatBMaOWx0a6qgkEvYpEdVIbJUElzf5IzRiVzVAvsxpkvKVKPIYEXzlWn6o3g9LVwMWc77N9UzHxhSY9gHgfL0aSLOcjNwYcb_-NUtih3yCQLd5AqFzDPPB3g72DmppLwmweMuxUqJMjkmf-byDWcKJERtstv7LrR7qm1BM3kyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=HfiP2X9PYgzAXA3a5mJ4iNxLGsNCYROZ0Db2O4W6AjsJUrELOZBaX7uZX8zZMMMAoEWZR2b4NYtDQmjfmxlQgvuxig_-uOem-8DG9m1wBTTPGoHnszYRgBah1IL-mRSK7rvFHX6hPxU16CSFUgTacwlLYB8a3Xjs_YIy8PpBejwatBMaOWx0a6qgkEvYpEdVIbJUElzf5IzRiVzVAvsxpkvKVKPIYEXzlWn6o3g9LVwMWc77N9UzHxhSY9gHgfL0aSLOcjNwYcb_-NUtih3yCQLd5AqFzDPPB3g72DmppLwmweMuxUqJMjkmf-byDWcKJERtstv7LrR7qm1BM3kyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1hhCZzdUyAgVsGv8hkRFO877SloiEhw7ZnaKUaYxFgt37l66BVvVYaDGHJbsL_P84fPd7HjSVKSH9E90U1tUTW6LG6Dica6Imr0Sk6T388Sie9gJ_R7MXnF8syaOcgsj1MnXrG8dhbzj7hK6EKo09IK1lTXKqCG61IKmGDrD7mNo_G-jdWlbIqljcTJrCYjE4FJjUvkYCwl1A9397FDJrlpvEhTfc6bjs7lN0QI0hv2lr9wTuKctvqQTh4uucdBk8b6v5eA-2rSzpgiujHgUfSzRp3zDjlgnEtK-FWKM66Pxgg6IJJoypJ941RRvRfOQqp_XtRtW5BH770n_f8EDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px0v1XvBkBQHTw8_t6DDS-Pf54Dtx8owb1jPREUCE5PxPcKzZiilIpZewQMPiMOemoi3cBP4_LOP_TmhGRNKfJCgnT5WTRPh3-VsB87OaOLfKcLB499UdPKWFhGp22VLV8ao7PPYjeky8gqRq_mensMa0XFSvb46Y3hMpcr6JWxXo6yQkA21k_QvdHO6OVfqu07AC88z6NhW4bCoop1GpmwYtOHorGrDosk6IwXPIUppxh0WSrMJBAcPYj4tvNLB0Y8pyAkltU1B2dyj7BHkxrZrRZtjQ5pABqVOoi4IcI8CQT2xnC33MCwW9KTftl-xMmhsm28b20l2tDdUG6Y59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vTceukMnv6xuEEd38X1b6-q5ZXsAmCSoqpeuCsD02YJRkJuR05-FNFY73pIa2qLy63_F9GA7uTOY4HPvQFdvQ-ltWRfcgp3Ns4rn14IQ3JBfxYIgjL7arWNACQILJG6IoYJ12l18tdTpDLRnzl1XbfMxEgqMO12ObZBNAIe_8v7AjEi-spKNxB1w1iTkIIVrHFYArj6p565QAj7h8YQOZBwBe1ETZj9zpqRIvUa0s9ZdF_2s7rRq6tdE8WkQ6ITnTd2VLKWN98ys6t0NLPpkwWUBD4pVJLkPcDHByngCbEuaUSlwXnkazKUuYvT8Lcj6tQetckCGNKsuxje6TALV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vTceukMnv6xuEEd38X1b6-q5ZXsAmCSoqpeuCsD02YJRkJuR05-FNFY73pIa2qLy63_F9GA7uTOY4HPvQFdvQ-ltWRfcgp3Ns4rn14IQ3JBfxYIgjL7arWNACQILJG6IoYJ12l18tdTpDLRnzl1XbfMxEgqMO12ObZBNAIe_8v7AjEi-spKNxB1w1iTkIIVrHFYArj6p565QAj7h8YQOZBwBe1ETZj9zpqRIvUa0s9ZdF_2s7rRq6tdE8WkQ6ITnTd2VLKWN98ys6t0NLPpkwWUBD4pVJLkPcDHByngCbEuaUSlwXnkazKUuYvT8Lcj6tQetckCGNKsuxje6TALV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0o6IHzZQ-bi8iZk-yzu9U7NS6XHJDTg_vdg4NM84hTq7KDMnBpoGrh6QNYa4RGTrU73bNpSFzdCqtb2BFvYtKoVJXAmcOP2DQyrxezUQwcuGzOTLLfo86ilbaK0hRazklQE0ilam5pmE4MJrCU3-_h3XveFsTGsR5NmUfwEnN1ejcXJQgBFqXfNRkOBqUt3w4veQS6Twmx-DPxxFgcZDMjNGoT-oeFdVxoahxRd4U0Fg86ZAee0FaP3NsseQlnenN3nm6ti3CwZ9ZG9T7Y4DFDpvDX2d30cw4CReZGKvWqQqCdWFz1OFvDpcfmRc9NzzJt5J-V_rVoKmmsnnbRJ98RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0o6IHzZQ-bi8iZk-yzu9U7NS6XHJDTg_vdg4NM84hTq7KDMnBpoGrh6QNYa4RGTrU73bNpSFzdCqtb2BFvYtKoVJXAmcOP2DQyrxezUQwcuGzOTLLfo86ilbaK0hRazklQE0ilam5pmE4MJrCU3-_h3XveFsTGsR5NmUfwEnN1ejcXJQgBFqXfNRkOBqUt3w4veQS6Twmx-DPxxFgcZDMjNGoT-oeFdVxoahxRd4U0Fg86ZAee0FaP3NsseQlnenN3nm6ti3CwZ9ZG9T7Y4DFDpvDX2d30cw4CReZGKvWqQqCdWFz1OFvDpcfmRc9NzzJt5J-V_rVoKmmsnnbRJ98RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=OUs1cLxJGmx85KxDMaSUiy3G7FOEfqKMdcRGLkPUHxuQmJ_WlvaRjNBnxldoqCL3zuIFtvAD88dOlLGNdATHr1kVfEaA47x7tS78AWCuMYNCyT_81ld1szZx7XPVhvvKmv3glKH1FcWNUnfQwZhlsHSFsXA8IJ9iWAY0-JCLwryK4icUmTJYDDZ2np_6gTlDiUvqFjzEkreCd9pOQ31wNHnsrL5uOI7UDAL3shddC3EnfLp76nphilbF5w-bboJA785l3R-bJif-b5N5ZCmKe1TLC27sEbNBBJe_1rSj10OBLDjqXWC1adg35Pel4_8s7ifOibn0XFu9Q9UllejtrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=OUs1cLxJGmx85KxDMaSUiy3G7FOEfqKMdcRGLkPUHxuQmJ_WlvaRjNBnxldoqCL3zuIFtvAD88dOlLGNdATHr1kVfEaA47x7tS78AWCuMYNCyT_81ld1szZx7XPVhvvKmv3glKH1FcWNUnfQwZhlsHSFsXA8IJ9iWAY0-JCLwryK4icUmTJYDDZ2np_6gTlDiUvqFjzEkreCd9pOQ31wNHnsrL5uOI7UDAL3shddC3EnfLp76nphilbF5w-bboJA785l3R-bJif-b5N5ZCmKe1TLC27sEbNBBJe_1rSj10OBLDjqXWC1adg35Pel4_8s7ifOibn0XFu9Q9UllejtrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHXSLHAiDD71u7FzepD921jjhysibC_I6NLztei8C7CwYolFyUKPtRgHgXmzPfiGAqTaFc0AYvDXaVDZDmBLBxc3Nxorxki4YLuncpbF1stkAwc-Q1yoe10zwHB7gd3FvHzXir76zCppWC7hbWH3j_kQj43yHykTq1dL_svAsps7sK4pomxLRA4sYFqqpCEdEfQGbsMqVEQRjpOfvZPfVS5HuLbRKfgLgajnEqTLKrC7xxEHjWQiPtltK_gPzi09RA2Wnw1FSpmaf3NDpKMsBpvbX_zFTBSetmtbte6rkqylwqJdEqcsjxVl5JRDaLcJ6UQPVzRA29ySEAy8LUlEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=A-S0DAzpuF0oFYZ9rWr0I36Vi6BkWAFkqvBD1Uwc5X3yzGHn54sobezMOopqdq5Co3ZromS72LPHRCP4YVTd94zUX5XAWoh-xCAs5Xibw0QF4-Ka8U24Skljcm0yP9099yrUjss3BUOvCNey8qxzlWox-xrGCDM5cBSwV9p8nRczZvPmZUgzaxrJh4oth0ajJ8cXEFNNpkPzDn-rOWzLOxPpnFhlcHIeVhTcerFdnhfimNIGIRrrJ01f0BNX84YAqemXow1o_EBZq4IFSVQn_OcFtll6mRzByPWM12fmBX58YlYcQz7HrIhwabEgGKiLAfvcirdMmCEDKxY4eeoDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=A-S0DAzpuF0oFYZ9rWr0I36Vi6BkWAFkqvBD1Uwc5X3yzGHn54sobezMOopqdq5Co3ZromS72LPHRCP4YVTd94zUX5XAWoh-xCAs5Xibw0QF4-Ka8U24Skljcm0yP9099yrUjss3BUOvCNey8qxzlWox-xrGCDM5cBSwV9p8nRczZvPmZUgzaxrJh4oth0ajJ8cXEFNNpkPzDn-rOWzLOxPpnFhlcHIeVhTcerFdnhfimNIGIRrrJ01f0BNX84YAqemXow1o_EBZq4IFSVQn_OcFtll6mRzByPWM12fmBX58YlYcQz7HrIhwabEgGKiLAfvcirdMmCEDKxY4eeoDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=AGoLylHx08afzkGNXToVqP_j74ymb8rOZ_TJDrIFjZhXo_roaHkWxTquEswXy7JNoubEcmskei2G9sb-EzWbFOuDVZiYwJrcr7OLYLD_aXPU99JQjHh2lSTEacISL-bNktr5p2h3LtzjXlhzFPrA-j49_p33VdGwzJ457Lai_OxzEz_kj4990R5jjsSKNYfvW4HnERYzdqWgEwVG4goKCjMV72Ne7CmOEyHhAC3N3fiXXDL66CmwjE-Zl8lnHlgYIhvi35Vr4k1UoG4in5a6bF30snpxwMOf3ye2ecqsga4P_db44d0mBPzQpzVdnzq-6Rmrg-RRfeVIJEb3B5SeAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=AGoLylHx08afzkGNXToVqP_j74ymb8rOZ_TJDrIFjZhXo_roaHkWxTquEswXy7JNoubEcmskei2G9sb-EzWbFOuDVZiYwJrcr7OLYLD_aXPU99JQjHh2lSTEacISL-bNktr5p2h3LtzjXlhzFPrA-j49_p33VdGwzJ457Lai_OxzEz_kj4990R5jjsSKNYfvW4HnERYzdqWgEwVG4goKCjMV72Ne7CmOEyHhAC3N3fiXXDL66CmwjE-Zl8lnHlgYIhvi35Vr4k1UoG4in5a6bF30snpxwMOf3ye2ecqsga4P_db44d0mBPzQpzVdnzq-6Rmrg-RRfeVIJEb3B5SeAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=jMCMU9_23761dReq6D76UXUvEJGHCQX9lCAzIKF-2BU_ppQznLJE6fuakFOl_oOOdTYgppl8v4_HCT1hzN8XWG_H2A6Cv49OTIuoWdH9N2TCPEJqGPkRO9tUlwG3mrOeD1k05yQOSADijH3Zu95bh6ITLTEidYYPYqQQ5gsqI1DP2zkufN1I6WjpZBYzNsiiFNzdtzHkQsP1V2yXklKC9DQC1hsphAEKdxRK-Q9dRIdUTy5Klfox4FLg7XR4JRZSAekmr_HaMbtUzPeloGaBYiJAamoxX9G7FMl8KBGU8D7qastBqAAxQWsbTpVu2cKHQFd5934aLSCOM_DnzTfI0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=jMCMU9_23761dReq6D76UXUvEJGHCQX9lCAzIKF-2BU_ppQznLJE6fuakFOl_oOOdTYgppl8v4_HCT1hzN8XWG_H2A6Cv49OTIuoWdH9N2TCPEJqGPkRO9tUlwG3mrOeD1k05yQOSADijH3Zu95bh6ITLTEidYYPYqQQ5gsqI1DP2zkufN1I6WjpZBYzNsiiFNzdtzHkQsP1V2yXklKC9DQC1hsphAEKdxRK-Q9dRIdUTy5Klfox4FLg7XR4JRZSAekmr_HaMbtUzPeloGaBYiJAamoxX9G7FMl8KBGU8D7qastBqAAxQWsbTpVu2cKHQFd5934aLSCOM_DnzTfI0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=PUtGxjNwcVbuc8Hkg0sa5UJbesvHg4_cvdRA_6ZzFPffn-p_f5mVHL5FKsHpW09h_UcPeARs-85qXN-8CocufxLvBo067KDbDrxsHia55VlqR0DU91gaZ0PU49S0wz2_bb-CUyjJXHmWRdms7IwBT1H40ZlwLWos67IAlhmScOVWnBp4t2LwzGyCUEWg5QKJ49_w0_KnWq8ozhkyDGJ3deSzDVThe1SBSh3GKCNBFkO6FRDMVmjqpxOrvX3ysXtNtjuSMZftWEmnAogyCgGQaMduvoNziXwg34vmXCGREuqsaLoHWMSrixHk_wrNTN9Ux4mK3s2Tx_NIXkwOrGVWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=PUtGxjNwcVbuc8Hkg0sa5UJbesvHg4_cvdRA_6ZzFPffn-p_f5mVHL5FKsHpW09h_UcPeARs-85qXN-8CocufxLvBo067KDbDrxsHia55VlqR0DU91gaZ0PU49S0wz2_bb-CUyjJXHmWRdms7IwBT1H40ZlwLWos67IAlhmScOVWnBp4t2LwzGyCUEWg5QKJ49_w0_KnWq8ozhkyDGJ3deSzDVThe1SBSh3GKCNBFkO6FRDMVmjqpxOrvX3ysXtNtjuSMZftWEmnAogyCgGQaMduvoNziXwg34vmXCGREuqsaLoHWMSrixHk_wrNTN9Ux4mK3s2Tx_NIXkwOrGVWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkEEhs_4ayu0aVZOnrCv4QrNzAfEqNwZFbsUrGPWVJxSLjouC0mhxJyPQM_EuB-8ZdcoWjFOxgOzZU1sJ9WPQUZXrfjboTAIWJL6bGdAXGNHdg1hxaR0r12OqGrp77KkFCil3978nxBaLAgp2NZLyFd6dUVgMaFMeLNsLCi0TRGw-Jjq0bnEszAN40TbTsq5S0I-Oh57UOfknDOFbpd4yU9nwC1_ayD269O1QSlxNHIWwqKiT07McFijf7hIg9L-Sw1R_q9AZVhesv6Gnp0js38xvLS3R-GuWxLrtM085Eel0j0G3u1uJrtaQ7ZwAz34J10_FHMsHbN-HTWBD4UaEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=u8aW39Fq9OOHom9svIyKBflxDBC3yJ-Z3hHCnbPpQ6KWzWhSPt5pTucOKcXKxzaSSHjgzm2kKx4N4Y77IISDnUN3xR6cdRR5REK8YbF_PWaus7PWpUWqeiiSB-BWdtV2h_9CkyEe645i-GqQzfqvKDC_C3rhbgTWLC0YkwdWY3tzCWP0WdPl1xe6WVPP83Rr3qYP2mPo5LX2B9lhsNKZ3Je0P8nNI5haL4RGHuuhaCPwEaFAZc2Id0YtyePjtY-Mrgf6rHeT6oY4HLFKkKfeq9Rw_s8hnyscURB91FKo-MjFemvcTm6c1LAmlqedw2PJnCLJXID9FupC5q3ghUabAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=u8aW39Fq9OOHom9svIyKBflxDBC3yJ-Z3hHCnbPpQ6KWzWhSPt5pTucOKcXKxzaSSHjgzm2kKx4N4Y77IISDnUN3xR6cdRR5REK8YbF_PWaus7PWpUWqeiiSB-BWdtV2h_9CkyEe645i-GqQzfqvKDC_C3rhbgTWLC0YkwdWY3tzCWP0WdPl1xe6WVPP83Rr3qYP2mPo5LX2B9lhsNKZ3Je0P8nNI5haL4RGHuuhaCPwEaFAZc2Id0YtyePjtY-Mrgf6rHeT6oY4HLFKkKfeq9Rw_s8hnyscURB91FKo-MjFemvcTm6c1LAmlqedw2PJnCLJXID9FupC5q3ghUabAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=lFoOJQeSEA7SLC4W_LlBtS3A5_9tLURrcrbznA8DDUVoDDGPinNzMjgVBD61uoSRQjmRJ0KdQuxxESKh8mfy-vZBIWejk5cMP3x9Dl4PAjuh2DsZANVW_E8HCU3kyNUeaW1NpGdDXO4QTXcNJmJ2x0hDdI3VlsyGK1On9vkF3BW_gNgKJmlz8xGn49p03tlIzlIWDNWlJuLTu91WFvrORz0dtAn-o__St_BETCdwq2oc53tmsggqy41WP2pyMDElwebTc7-SEK1UI8wf9sRyWPSxxMjev3foOMFD8g10x0Ijwoiro8j-3Tix1j8J5IAG1fAQ3hJB6e4sEuIEuHSn4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=lFoOJQeSEA7SLC4W_LlBtS3A5_9tLURrcrbznA8DDUVoDDGPinNzMjgVBD61uoSRQjmRJ0KdQuxxESKh8mfy-vZBIWejk5cMP3x9Dl4PAjuh2DsZANVW_E8HCU3kyNUeaW1NpGdDXO4QTXcNJmJ2x0hDdI3VlsyGK1On9vkF3BW_gNgKJmlz8xGn49p03tlIzlIWDNWlJuLTu91WFvrORz0dtAn-o__St_BETCdwq2oc53tmsggqy41WP2pyMDElwebTc7-SEK1UI8wf9sRyWPSxxMjev3foOMFD8g10x0Ijwoiro8j-3Tix1j8J5IAG1fAQ3hJB6e4sEuIEuHSn4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ6aT47rBzbovckwYOzzfHfxIp8DUx02D_0PySpldmkEZJRSFrfxqKToWUeU9JK7WvPJ1G9FdBqfaB_F5zakThz6_TT6f_hTj2fCIXnSTmoQSAyK8-VoU0ZUVREJUprnB4rmGgrRuMkfjAo1kAKVX3Db1luyITqyqlOUZUIMWTZo9pkJcylhfZDz1fMZcqkc95eVCYC_N1sjajSZhoe9h455TP7ikDM4AK_0OYzmybyatipgZi8nvSkos6uDFIiHiYKP62qPtrQTA5uCKsM5jmXYxSbR02nvgmbNBSliTVCH4nBJIgQr5bqZY00xGOi50AGLOR6njGWINZtbH4hu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=gxJSbXDgvWFoTN4uLHMjatVEhQgk20HlY9sv88q-3i4AjN_AY0YVtfpQhPbu7_FfIAmun9brNC49T-KH3q8S_0ps90HMANB9wwU3Cd9yXL92A8mZ0Kgu2YIAzXAgRVC1y_BCA-ooSn8JMgQ6O8OtljbWtNp2_kTtHp9U9g00ici1CAWM_cROIuvch_Ud6D2DxMEATnJ7tXXKE1RLz1-8-jOZLq8Li_EM4jTyLZg1_kLdGm9hcFSPmZ-Pp995PvUYMhwwVVZVE5L-bjKWUZAG5pMu738GhQ9TWSb0YOxskf6Y6Oxe-Jz63fUPwZNXRz2y1_m7ze9XyIE_rhtGINAI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=gxJSbXDgvWFoTN4uLHMjatVEhQgk20HlY9sv88q-3i4AjN_AY0YVtfpQhPbu7_FfIAmun9brNC49T-KH3q8S_0ps90HMANB9wwU3Cd9yXL92A8mZ0Kgu2YIAzXAgRVC1y_BCA-ooSn8JMgQ6O8OtljbWtNp2_kTtHp9U9g00ici1CAWM_cROIuvch_Ud6D2DxMEATnJ7tXXKE1RLz1-8-jOZLq8Li_EM4jTyLZg1_kLdGm9hcFSPmZ-Pp995PvUYMhwwVVZVE5L-bjKWUZAG5pMu738GhQ9TWSb0YOxskf6Y6Oxe-Jz63fUPwZNXRz2y1_m7ze9XyIE_rhtGINAI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VcOQqLAailIeTxMOBe-GhyMNw-halTE5W3BLYdd7qr7cVKpSP_EStSrClYtH9TiSuvXuFAXNo0u9-PA65Yspk1dw3Va1mgXReCRqVDXPSZG6Y5d-aoGfvxrRh_lg4PGyvV34GU7NK5WBR9HxfCk920ffazS_m13sVga-1wwbkw8VOHRyRnmYCPzW1XqNiYcCR6Ywu9Ay8ZkEwCp4EXMUwzuh2UDDGICe9lxYL1pd8TUzfkuof-hEXuNU6maqFpdT6Ev9mAqKWplG0JPUpbVBlinxbrFoCW4hWhdweJwxvpJf9oEGKa1cwngcGoWNiG4yHfW7hxr2PSf5sD8awGDtdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VcOQqLAailIeTxMOBe-GhyMNw-halTE5W3BLYdd7qr7cVKpSP_EStSrClYtH9TiSuvXuFAXNo0u9-PA65Yspk1dw3Va1mgXReCRqVDXPSZG6Y5d-aoGfvxrRh_lg4PGyvV34GU7NK5WBR9HxfCk920ffazS_m13sVga-1wwbkw8VOHRyRnmYCPzW1XqNiYcCR6Ywu9Ay8ZkEwCp4EXMUwzuh2UDDGICe9lxYL1pd8TUzfkuof-hEXuNU6maqFpdT6Ev9mAqKWplG0JPUpbVBlinxbrFoCW4hWhdweJwxvpJf9oEGKa1cwngcGoWNiG4yHfW7hxr2PSf5sD8awGDtdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nYOUPYjR7Y_hOP8SwM2H3kFMUArWd8lIgWKYVubOUwQzwC60_Tb77sQnasgkUgQdLg3fOfxSjgMH5E-v1bcVRCP1uDF_1HJ_VeeNkh1_Rkv6dPCPiOiKxUzp04-ZTane7sqzPiCdCwvSdfp0kFG67ArkHj2nB5oIvynnN9MaG2CeF3jFeD7paIASFcgP23yeNJfyqSM0oOdiH7lPNHMUsazr_3djN6r_MZpnpM9tD9nPXXQ2ghiduFYu3SPM5dMEvCZFPPcdQ0-z2I2dWgtoID2fzZQJNo2E8V1k_aUntYgluS5YWGI3C5qbCIW3BODBYfuwCEFxAbzXyUrdQOrsSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nYOUPYjR7Y_hOP8SwM2H3kFMUArWd8lIgWKYVubOUwQzwC60_Tb77sQnasgkUgQdLg3fOfxSjgMH5E-v1bcVRCP1uDF_1HJ_VeeNkh1_Rkv6dPCPiOiKxUzp04-ZTane7sqzPiCdCwvSdfp0kFG67ArkHj2nB5oIvynnN9MaG2CeF3jFeD7paIASFcgP23yeNJfyqSM0oOdiH7lPNHMUsazr_3djN6r_MZpnpM9tD9nPXXQ2ghiduFYu3SPM5dMEvCZFPPcdQ0-z2I2dWgtoID2fzZQJNo2E8V1k_aUntYgluS5YWGI3C5qbCIW3BODBYfuwCEFxAbzXyUrdQOrsSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juNMQazN8Gb558lM5KQfuYT66ckDMLGZc0UjjaWq-qg4dFPTH_4Kxqan3gmZaCTqaFggZBAUrQjtMpvh1726_B_YFWBNa7gS4rFp8m_KD2w5VKu9OxYY1349BYlRLZ-UIrIFrcnjkOHUTydyYBUN8e4VDghMWLkRQON1UHB9BdkIEfFqGLGZSds5TFHS1IKLxJ-DRnl6nKFdf039OcLxfGYsUqhEUINYkuM6IfE6VK8EVPm_6n6MlBNtHlIRJX5lL6LOlXohce5sSvDxChQ63-OPX_G1p35KJIzwZqxbOUdcp0I9YaZqiM4Tsy391KlLeawY5fPt52YP31uZyOnTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zy0BA-lFEj1yDd6u1bYcYeVwhxjg90SqUoyMPdgqVwHOdKb2oXsSmXnXTyuwtbdoeujzKOFSYaIQRin05U9J_akckffD8OW4V4i-oy5YPrzc3Zj2qlrpjo7iU9krrNwMdDvPaiJq9Zrpbq-5rqdk0GPTLlOOLkBhg9h_TN4aRA6191IBMK-vanh3_aEyJK0X69FPEkBd361aVK9fI3ZcFJXMC2GiGZIyOAoY3LrjP7FIZDw3w-hwoJlBwhK3pJrk4iZZZRDJTdC5lPu1beS8TeV4veMpqt43BUnaRIKtXvvDQUEtFv560VpBTp0na3LI4bfNwRb4zhMqS50lUsUsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hs0yUlLfycJG65r08hyJ52JaIvlmvJOchjNfLgDgGAxgHeIYH4jsBNy8lzNOSTo-5hXVYec9qypkpbY24Mq8kqx52z81lwM2EXonIWKglZB2tSprptH-4lJEQNzhKH3T_Fbbu_WBW6Gaqq9J2Tda_CfR_qkA6oJzmYo2h4PQOQUxi2Ag1Ij_tk_8KTyF0Q75aRkKgBERSIXwGR-mCTiPXLk431m5qzDgM_io0lPSCw5ziUmMx9stO59nZ3800eFegDIOOV_GoZDBPGFGZ3YVXEStmYOJy-8_T4gkzJ_qZOQrEh9y9TyiUb1uAVxw1FE6eDjpQNVDdGZGzjYpf5n14Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=R4OpcM4eQ2CUh_vuWmJ0XotO67pwoGR1j-v8wnkL08rynS9_eUEjilbwEjnkrJTzJ58MZ6viem-00rbQUL6Cg4YJIwlPXE2mZVFvEhOT6TavJ0SuJx5ZFsXEpC0916QgW-GbNISdYAhdGso04-YdTDNk7ZiUi-cH3c11QBBWrl0dmlm2VJxPQp43YLb35198OpY-BuUELtBDbjPB6n0MINMGzbSa0Sg57k9DUcvsLkcE6ZYvaKGwdJa3xksUONHhgwr9PXwNcb9vTyGv_ErgysmfaF7pUSVhdIzYivUpXErX6ES1tcjnRZ1q6qQ0BD2xSBwPb0VCkLYjadBal23hYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=R4OpcM4eQ2CUh_vuWmJ0XotO67pwoGR1j-v8wnkL08rynS9_eUEjilbwEjnkrJTzJ58MZ6viem-00rbQUL6Cg4YJIwlPXE2mZVFvEhOT6TavJ0SuJx5ZFsXEpC0916QgW-GbNISdYAhdGso04-YdTDNk7ZiUi-cH3c11QBBWrl0dmlm2VJxPQp43YLb35198OpY-BuUELtBDbjPB6n0MINMGzbSa0Sg57k9DUcvsLkcE6ZYvaKGwdJa3xksUONHhgwr9PXwNcb9vTyGv_ErgysmfaF7pUSVhdIzYivUpXErX6ES1tcjnRZ1q6qQ0BD2xSBwPb0VCkLYjadBal23hYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
