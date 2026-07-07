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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=hK0kK2grIdkzG9Ak7DIPKO-8hQPjIQSGeelcOEMddu1uJyJ6_K-HEiSzenuWjjX9-PmN74r1EUgM-q-cg0hzZjRn2zafTg1jrqArcjs9alIUjTNtkPgFi-JWpVgn1GK_BhopQ3LQ-St2kyWjA_au0PWCAtu7G1XVTExzbQZhtEcMM8pW0Urei1IjZZ_eBgOptCAeWzt6a62a-fscFKjS4RYaikKn29cnMagvc7N1sqyrV2v42AG5yQX3pNVgJZ3ba1SZDRH1-sRf57tZ6ja2u_maXFpYH7mzvxu7HORom3G8wmmAywY9LHiyvZnqx-9nLgybZHXj0FGuAaw1bDn5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=hK0kK2grIdkzG9Ak7DIPKO-8hQPjIQSGeelcOEMddu1uJyJ6_K-HEiSzenuWjjX9-PmN74r1EUgM-q-cg0hzZjRn2zafTg1jrqArcjs9alIUjTNtkPgFi-JWpVgn1GK_BhopQ3LQ-St2kyWjA_au0PWCAtu7G1XVTExzbQZhtEcMM8pW0Urei1IjZZ_eBgOptCAeWzt6a62a-fscFKjS4RYaikKn29cnMagvc7N1sqyrV2v42AG5yQX3pNVgJZ3ba1SZDRH1-sRf57tZ6ja2u_maXFpYH7mzvxu7HORom3G8wmmAywY9LHiyvZnqx-9nLgybZHXj0FGuAaw1bDn5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=Mr88wh9FrssYDEFDM-sxHnZRYh2y0SkDNWBtqn1cJELDasWaDPyQICjo5O6MJLRQoNiLVoO3mEIuZe541oGDvcoJkT2oHQoLcYpJggUrw9JXulRVKO88lfFBzL9H_hWIBqYVy9nnVtpY-QAfNajRBXr_Q_GBvIXgp_d1KXt3VZ3w2_hseZAOy8EGxGutOKLZsD6ssB2Ihpnm7zuGhnVcBuVYdVYWFgrsHa-XSgmlEUJzq3-sNaLCain47mWiT4YO9Iwf2vweWpLoU4kX79LgoyqHGQADBd5Kizu5gspg7jmsX-Gk7htSB7aMUDVKqxZOQwAfEkfiJWObIJpko2v2VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=Mr88wh9FrssYDEFDM-sxHnZRYh2y0SkDNWBtqn1cJELDasWaDPyQICjo5O6MJLRQoNiLVoO3mEIuZe541oGDvcoJkT2oHQoLcYpJggUrw9JXulRVKO88lfFBzL9H_hWIBqYVy9nnVtpY-QAfNajRBXr_Q_GBvIXgp_d1KXt3VZ3w2_hseZAOy8EGxGutOKLZsD6ssB2Ihpnm7zuGhnVcBuVYdVYWFgrsHa-XSgmlEUJzq3-sNaLCain47mWiT4YO9Iwf2vweWpLoU4kX79LgoyqHGQADBd5Kizu5gspg7jmsX-Gk7htSB7aMUDVKqxZOQwAfEkfiJWObIJpko2v2VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg8J8EGREXL-1CdhbhNUgrfR2ZcPSEevmuChZS4AlfL88QEd_AnJwDA6uLdWhmMqvuMn3DqISwp1jIqOfVOlN2F_RkRMRIgZP6w4vynDC1q5lporBDpopdcAfcgGghTQC54KpefydjwvJpfSh785_a5_HvbRNul1VT4dpfubJGKU-mT8Wc2Z18MtnJb_wyDR4WmY1mp0YrBY0vbvcICjQ04PBGUeLezs7HYDwBgnPi5Niw-AKk-Z3NTlhEyPIUKbQ6hiBgaNSrM46bGIlmwc2eB7R19IYxaB3YfLIy7lOSEDSv_AzLbUY0W25f4-KNfAVsR4qAhtCE6CZTGMbxLUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig8KjNRbr4yd9Rd8q-C0oT31gK4_36Le7dRgVWEirueub1mudP-VO2WB7sooV77FV1AczsYK-LBOZAlRyC645DROlV3iE3whm2Qgh2d1PlAXmoZcgTEC08b3Vl2XkdT-IhNzRVgTHile1V3MraG2qfJkXJVvnw1nN2-sSQ8A-0VqNucnFjcqjtKk1zKd5z-Vg1vFM-Mw_Vj1oeQD0yBFZfW7e7O4H2-NvIBEYbYGcVS6Ame2TU-q6kHldNJ5crlYwbHuZtf-oJY0Wa5_Huer3fPDA7o4aSKoZJrcpM4lD2Vw3P5q1LzyCYts2dFbbD5RAtF5M0KNbFHEicr-rfn1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQD6mknQHG3bqvDXwfb5zO3XBcHmxi68EjlPpXD8TPrZKHeyxlaJOvYy1GLEgrHFE-6q3G4I9m_8cEkaITwkSO-LTibP10MborNdRA5J_-6PYnMzNpQJdnM-z9aYMHyJWzPd6TCI9L2Tx25t0KydiNDmWwyZIkJUCSc9lxraA9hGpF8zMBPTE2idU0XZiIG30RRyBjuCRqtUsh-UehFza_0T4pKi7IJLAP8Qx1QImzm-KKLSm_D0UZdbj7O6-PE9YmffVWK5jvjcVh6YKkI5M2zw7E4v8GW_Q_zqNBMj3AQa-E6arihaik_cMeBOo1DK6mYBKcBauvF8VFz40lHOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCbRuPfClB3JSNHsakYtkoL0D33jGVOrnGvcwML_axjnTqk2pFwfePFguCzTj9qcFHl7qLOD58Cx3KJrpwCoT8fD-dVbpORMQTSvP8kIvDk39lAw84BEtCZMn8PRNu5BHkDHYqNij-d6-N_YgQVnL64S9wIdWM31auWSuP6sZs1gsSU1Nr71J5ghrizHHhjm5W8jDKxlzSYMcEpupcC4sWxhBtq_C9PzAhMv0xA1CPeqgP2GmhhNUM-pzVO96OZuiJXupkWCb8UNvEUf1ky8Cqvi49xeB0Tgjvif4zPvnXnGRvjhXHfHje3W5GnQ25jkKHWeH7SbPUwzNj7fWoEPPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIq7i3vbIzGDYRavdu0I5NEwjqKenKmetWqKAqkEhIw-xYGGYNgnSaDjelo8j0TsXHreAVVum-MmKesdAOYewHg4aE33czI1ZOcr06-AkcB_CzEjixsLSQWzVEycLlB4ijsUmV6u1ZbSgn4GYM63ibMn6lPtFNXpKi2PFQIDYhlEwCpniXSxeOC6K47rMAPv4SBDuidNkw-6WzLf3vW6xNUYKMNFpo84ZlAuFcndYCU5ACg7yhVdmP6846oa4i3J3sQfv6ESSNU5r0J2Gp1B8BS1Kcqh66tQlx9l7BzWL65oPWFjh67K3MXi7PUEsVFxEEGbuogbHsImA3xdk6foCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLqpf3dtnow8OTQ_64kF9LPs4LMzV4UdmjfJ5LsEkASLF7e0hXY7QTP2ToP7px_2t5ZCfSjWvhItHDohGvMFG5cV2q29bn0LeCAVzKlwLDUubuMAf_Qbh2m15r9KaezwJ0gpHSjhsYA1_5XLPT3K-74-qr5SQ3TWDf26VGpushx7BwR_RIEVYrg8pGyqkflVjPmTPXlLzLXVWU19QAxR-xjv-35aXqTDwoHM41WCmoVMG79cYppQgy8KxiBZog7qnud9kigkQlGL25ZBgWoyz0rYJcps6P-Dt3bWZUoJKcJBSUkMVHCFDavrWlQRcIq0HDA_7qOZsLwUwR1wAJz8_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=fdG6l0jXTVkptTmuOoxdeUPX1yfTeySTxpi1XAk6Kex4DZy4zL9ToW-vwJn6S4z2WSX8eA-7IXMfDhhFKtpuUuG49rV1sJ4sIxEMXQYYzu_iGmimn0ii3w0fZyGpvjmDGWqBAh497HgL4Mj1wfkgN1NznqR-RpU4BXtmOYycIFsqEZmjh6twA8Hqe7iNNYyFvQ76ZvaObYbBpYugj0sC_tSGsUDtQb3rvCWMQvemzVtGLVuMD3c5t7mrYhJYHc980H9blATv5lBK8aaVA0wNvSbVeW59Q74sbT3BOc0kX5SRDUfkWgNtqkmsLfEksO8VO_EajJ7BhXf_fky2PZKr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=fdG6l0jXTVkptTmuOoxdeUPX1yfTeySTxpi1XAk6Kex4DZy4zL9ToW-vwJn6S4z2WSX8eA-7IXMfDhhFKtpuUuG49rV1sJ4sIxEMXQYYzu_iGmimn0ii3w0fZyGpvjmDGWqBAh497HgL4Mj1wfkgN1NznqR-RpU4BXtmOYycIFsqEZmjh6twA8Hqe7iNNYyFvQ76ZvaObYbBpYugj0sC_tSGsUDtQb3rvCWMQvemzVtGLVuMD3c5t7mrYhJYHc980H9blATv5lBK8aaVA0wNvSbVeW59Q74sbT3BOc0kX5SRDUfkWgNtqkmsLfEksO8VO_EajJ7BhXf_fky2PZKr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=HveA54LBT_MWrIElRM32-NLhDXeTXeehAXKzqOvYPpHI10mSkfjqomSS-dNzHfqglwB8Oh7aPl5GfGwIHrXZT8NBKdt7dFn4c9grBRCvYFhO25LljME2TruvbUGT3H_fLo-uW4T-I9NiHpKcWeEp7XEUvutqwhA1f6Js2JZFdEM359-isSAA4YnkkduP968x1uK94mh8Gb4kfG4k_h3JXAKDsB4deoItXZd6BsRi3VejT7tj3J-pKaYoKdg--wOCUtqe553MNCG4ldbCH8kctzwhwVVZqq682scWIU6Oxv6jInOwJc9ym1fcsKu2BqbqkL8XA5KrE0HSMJYX7ZJ1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=HveA54LBT_MWrIElRM32-NLhDXeTXeehAXKzqOvYPpHI10mSkfjqomSS-dNzHfqglwB8Oh7aPl5GfGwIHrXZT8NBKdt7dFn4c9grBRCvYFhO25LljME2TruvbUGT3H_fLo-uW4T-I9NiHpKcWeEp7XEUvutqwhA1f6Js2JZFdEM359-isSAA4YnkkduP968x1uK94mh8Gb4kfG4k_h3JXAKDsB4deoItXZd6BsRi3VejT7tj3J-pKaYoKdg--wOCUtqe553MNCG4ldbCH8kctzwhwVVZqq682scWIU6Oxv6jInOwJc9ym1fcsKu2BqbqkL8XA5KrE0HSMJYX7ZJ1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=UdKjpQko0Yiugdm6upkGJAFkIJ9JDZoomQmaV2jUEm_Q-KUi0NjONjjTgw6sWxzF07yFzO_36LqsArGVt6PB2rDNZQmHBfjsS62NBb3MJNJym23ruzwDrSNIAyhvn0bIK5KoUS_zO4dx5UQPo3mQOa4p9B-BeTh4_zQTsmpA2HsgjsyeS6yOyLdEE9ti8NHz0adpD9Qc2HIgXzyM6juGJc6183WOrwvJmzrFhUcUM9U_GJQQkB1JqPqmFtu7SELz2OjBGpYomTYj7yidjtfS_h0VtxL0UDJO6J7p2mSS5uyNE--43a2NLv4YzuvX7jln-sSw3wBeir1yIPjk-QIu1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=UdKjpQko0Yiugdm6upkGJAFkIJ9JDZoomQmaV2jUEm_Q-KUi0NjONjjTgw6sWxzF07yFzO_36LqsArGVt6PB2rDNZQmHBfjsS62NBb3MJNJym23ruzwDrSNIAyhvn0bIK5KoUS_zO4dx5UQPo3mQOa4p9B-BeTh4_zQTsmpA2HsgjsyeS6yOyLdEE9ti8NHz0adpD9Qc2HIgXzyM6juGJc6183WOrwvJmzrFhUcUM9U_GJQQkB1JqPqmFtu7SELz2OjBGpYomTYj7yidjtfS_h0VtxL0UDJO6J7p2mSS5uyNE--43a2NLv4YzuvX7jln-sSw3wBeir1yIPjk-QIu1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=aiJ_ow9-PGAyh8VRzripKSNOibSeAcBIw7Y7qrPYhpdhyq6IvDiL45snnochCuYD6p2XIf3s9xZr5Ji5QOsSPEj2y2wYdJZotq7x5SHnWVGurfHhNASqvmwTgqlxfeEZ5m-RwucsjRAuz7CXcp3thGR_Wo9IMTuH1WuM-GVh8lIXP0Oew7c_V_I6LCy-dnKPAMNE1F-oCe835B2vTSshFwNFBFht56Yzi5ByZfQ4ULs4VpC1qpKYoZCVyYKvd3QvF5oKLmV00q50riKdfI81RftZf9eI22LHF7EpUt8_GPfvd3eV4Wow4NjlLKfGU4qtHMMK7D6mHuC0Bawk20IKYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=aiJ_ow9-PGAyh8VRzripKSNOibSeAcBIw7Y7qrPYhpdhyq6IvDiL45snnochCuYD6p2XIf3s9xZr5Ji5QOsSPEj2y2wYdJZotq7x5SHnWVGurfHhNASqvmwTgqlxfeEZ5m-RwucsjRAuz7CXcp3thGR_Wo9IMTuH1WuM-GVh8lIXP0Oew7c_V_I6LCy-dnKPAMNE1F-oCe835B2vTSshFwNFBFht56Yzi5ByZfQ4ULs4VpC1qpKYoZCVyYKvd3QvF5oKLmV00q50riKdfI81RftZf9eI22LHF7EpUt8_GPfvd3eV4Wow4NjlLKfGU4qtHMMK7D6mHuC0Bawk20IKYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=UWsWrDVCzgeiSw5th4wZMELDhGW-PvE3leIBTeznhMXKjmuiTpBHODYcEOVu6kV7i2hi7VOPrh61vfpUkLaN_zZfrlUO8AbCZndc9lxk-TRfd5swb3RjSrY7IbZ2BxtC_0o6B0xUl9nF7lTcQYZ3UmfGMGFM6LuJPpVukiO3xZDihVP4QnQe2UxmccARsZ-MlazpqRRbjS8l99d1o4f2YhHzB27hnk2YE_DiEozkbqGFX5vdQifgyePZ0JMwHlpJg4EkWnWZg7_bC2o4G3NELAvhx_M6zgBowHCNGZS37HpBCWjfuaaDBcmEWFhrdBsDOT1pZVHpEiViA7T-3oO6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=UWsWrDVCzgeiSw5th4wZMELDhGW-PvE3leIBTeznhMXKjmuiTpBHODYcEOVu6kV7i2hi7VOPrh61vfpUkLaN_zZfrlUO8AbCZndc9lxk-TRfd5swb3RjSrY7IbZ2BxtC_0o6B0xUl9nF7lTcQYZ3UmfGMGFM6LuJPpVukiO3xZDihVP4QnQe2UxmccARsZ-MlazpqRRbjS8l99d1o4f2YhHzB27hnk2YE_DiEozkbqGFX5vdQifgyePZ0JMwHlpJg4EkWnWZg7_bC2o4G3NELAvhx_M6zgBowHCNGZS37HpBCWjfuaaDBcmEWFhrdBsDOT1pZVHpEiViA7T-3oO6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=SXlzP-mReWm_MRDi98wdD6ajQKn2YdiZQnySRJ1XpYboR5A7PGj5jMB2LBtHkRVta_TU6wlS6kZlmSytLKy7h8E0LhqL7wKq-mZRxNs5Y9t-CDwW6vUsihAU0Ko3wnvwKSJUB83QdCLgEVE3nVDJS7pcDcl6qvsxfDZSpTy2V9cvXWOsor37Q0ETT-8eSCYKKh8Uvb6KyM6VzV2ecCC0VNEYvg_D-ML9a1OJudj6ExgDmQus9h1lhARFeAj4IjLigv2TAKihSGlwWwEg8EWM68md1GA5gmVTrBZtFsoBPI-NzUVdle8ZxEUJg13SUaiQfRYWbvUcQ-wd_V6otHpClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=SXlzP-mReWm_MRDi98wdD6ajQKn2YdiZQnySRJ1XpYboR5A7PGj5jMB2LBtHkRVta_TU6wlS6kZlmSytLKy7h8E0LhqL7wKq-mZRxNs5Y9t-CDwW6vUsihAU0Ko3wnvwKSJUB83QdCLgEVE3nVDJS7pcDcl6qvsxfDZSpTy2V9cvXWOsor37Q0ETT-8eSCYKKh8Uvb6KyM6VzV2ecCC0VNEYvg_D-ML9a1OJudj6ExgDmQus9h1lhARFeAj4IjLigv2TAKihSGlwWwEg8EWM68md1GA5gmVTrBZtFsoBPI-NzUVdle8ZxEUJg13SUaiQfRYWbvUcQ-wd_V6otHpClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFT9nVCbSOO-Utwf8v7vMKW9q73YYQ8x1oG0ymdZJJRyL1H-mSLV6_6LD4r5FS8rXkGqRDqWPTWAGDMU292DIyL51ZDyJWYE1bZ_bvVfrCOyf-8AlzdFvpPhLnyE-7Fa9vvGXInwWEKjJhuATxHG6F0j_oxMaoVuRc9WJB48LEgu35BWgcaNpj5-dkl3LZ2YG1FOCXfb_-qLEwxYJi7pOeLE6g0Fsfy-FIzV8EwX0uOZPV9oUt3EoYjDp8EEuzTWbVXIzBTnpNUYyFVuyiuKpbdZP8G1wR20GxZiIy02XnqqbfKu-qCKlZWffywKCpAFjA_-2yybFX39NcVVMET_Pw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=CqnG_QXBg6w-4kj4ELNDRroODX4zINrQ2JiQ4734mXE3gqQLrYx7lfl6i_0nVBReyG6lZWnqhnlkFg87NuY8LDcr2bCRgED_furHBYhERsUp9wW-Q_ETzAIPcs7Pj9XRvd6eBmCA5tAGcykI6DCP1L_czTaJIQ8jiwag7Rtf1_upp_2EdN2S-ZhCdaXu0JMI9QUB3lbq3Jrcca7bKJYb8V5U_Zd7TwR3B46YRMR0vJwvUdxTIG3Ctg5NmaFGuk4toeiSW6ODk4rDC_MPb4JP33RqU_PezPSltWPXyqhbwrANZPTn5Q1YQeV6rjwvAh5_--1PB36XG5FyDyVw_SgRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=CqnG_QXBg6w-4kj4ELNDRroODX4zINrQ2JiQ4734mXE3gqQLrYx7lfl6i_0nVBReyG6lZWnqhnlkFg87NuY8LDcr2bCRgED_furHBYhERsUp9wW-Q_ETzAIPcs7Pj9XRvd6eBmCA5tAGcykI6DCP1L_czTaJIQ8jiwag7Rtf1_upp_2EdN2S-ZhCdaXu0JMI9QUB3lbq3Jrcca7bKJYb8V5U_Zd7TwR3B46YRMR0vJwvUdxTIG3Ctg5NmaFGuk4toeiSW6ODk4rDC_MPb4JP33RqU_PezPSltWPXyqhbwrANZPTn5Q1YQeV6rjwvAh5_--1PB36XG5FyDyVw_SgRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBIc077r_6Ao4j1_QCjyyKrViqbyPrK9mShzt_Qaowfo91jWQRS24kFRj-GhVctA8iWcPtFyAdZDxzP4BmMDzwT2u6YfU8DnU3b0dKYYW04qbkChxGASfV1b8ti2Pu1dkFdF-pIOKPyOOJZ5E7AMqxHpDabWoYOXgcZQaL3JZStB-kAUtzTrdewAYZfP40dov2DgF9DGtuY0ZNHA2YX1cxD55SgxfiRpARC8OamzEDZ-HKcr3CZ-bCLmJiqfaXn1LXDcvCXuKZ4VTxfHnUYG7Fw-XSVxnXOgHhkv6A1gaATx-7qI53jBMQlcgb8XAQdIVoErbguVQncpFLGsRKkWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE3NbZ8shtxJfQ7mg05jghgie_XpbgiDv9vSX-NSeUZ7XSoVF4StScfsDlTAwVM-d6a6Wgu2DnRV0LXdy-xr2wkLV3HYgmlUwK-89fm1P2MlkpqIAxeKVuHnuTLO0TApgoI_NzecV8xnul4kIAFIoNbyc2Sb-KJVrtfj-i1Q5xDWYnbDw0cBQfqgRyMsOLUtzoQQk3UnqAraxMRf2jTe9ARop6fgUuX6krnDfe6hHBoeZiiFD5cB7oUWb3Ov3QJn-llR83GzxFju_suUuK_JGhy330WKePQVu4eOW7HypUg-iQT6QYqsAxLhfVP--3vJlKbyoiJ3h2M0lbZC2LUPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBKWgLiTHyidmeXA-QPcrFC4yqzwwak7Rt36NZCJfQxohK-E_WM0yCLxkRUCAbLW0UVVCAkuxVkBYxgiP3h4Ayznz-46ABRtURzz5la9FCzeuQy2npQqJtjA8Li7si7H2jnPqmFRTfVBQrGcFaZ3WLIxyuftmPeouzkKYo2jGC_t8asl0M5vhpqBaBW0BvWuEDBJVq550sRcx5YGLniwX6reYfPtenGFLCm3CKVRDPlTPvVsSt7A_r-PA_9UNsK3DZ59pi7hT_mTTERXr_Q2Il9wo-vsFQX495PrFKokloy56t79qOx4WicgEX3kJxV4nVYlkFkkZzfdWmPeBh-rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jywS1nWTfxh35b6idTUVK8wPeUEHsMI3ZIQgUZ3Ae1l6M68ayiQh6FB60EvO83xyayZoSQA400pMjvpCmo_gKZbTqodhxJEuRui_i6ruH-btu1Iu6DLURgTy3rbGrqrpCz8FPsHJx8gEBmu2qo1uiVLAX_8acs0oMAX1fVHUIKjjgguaRD49zMXB09wVOgYlZbRgNAaymo6gdNcL4kWcj4zzkNXiUiA4cfb7ugJz5Tx4Uimnk6s8U1Or3OdzYcbziGagYKke6zONCjpWrVUSXxzBrRqckqH3ENJU9BJfytMSXgOBArabycKQs-H6ckk2gZeyPxBaPhYIfqmY46nEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoHfRx1yg9f8dv-L5zQ40bj8nvGVPfoIdMK-P3wDfl92GsEPx7p7zmHw6WslaNKobnUYywxq3AhnbZlLqivtd_CxbLhn8XctEwiqIvWmdX_B2IE9iqTSvHeVJ3I1bcJJoTfS738-xhvW4fB0XTddpMztHGO8cVlcvr8sdOma9xGtybDTW0IS2oJDc5j6ps4kE4FY4eybKriVLlkDU_atp-hUl4RwoRxnVeWB_hUOASa5k2NkEmOm7Qt0-IpkjdmbSQxIvw-1W03MFdSCWgiPORFevcQg_zbjvvraUkAiVxrNIuj-YB5Jk2eqn3Qo2QHIFe-R4xW9w1VC2ewRQAv0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqi08tQyQ8MpAjjGH5hxC4-CX0-yGr7BikXmz7NvHx10RV-JiY4Scp7a1zJTjAo_oezYsQ7Q-8pDd-01QLVEupcLVfVHZkoGIxVNyGxIKTAUAqB7GaRTUQQnSlgzkqeNGssURFUOZcoEyQQjOEFjbCMpX8Frez7z6n90bYyftAtTYDh9nMjHx-puHwBfke7ZpCkYAqpOJAZDmtbNUX25kRzLNeVDmoLC6jLucSABZr9AbFNLh6Tk1b8o13VwWngsrCdRMRMAVS0TPD6ja2V7ZM997cebjOKgd3uL82FWfLXhS28NNJKZyJvRxQw87nUe3QxvFCkZ0tjePTaxn29O7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8uDShsELevg3K09febEzpj22gpCOJYeN84WfDkJPKgKjNsr_W8Hl8ie7LByC989amldEnWMsqEivTz2Y0z7P6_jCDotyVn8hiSSXBh2pqDIPjVcqiwesbezhDUmp5HzKYSt7mLpj962GVvDxrPurMtLpUaAxBWOdTs8tGhTV2RF-DhFyswHUn_zY8W2F5SAmoigOaWvN0Bt8RiEH266jv8LB0MW5zoaA4VXBQWSf-r4uCI-E8r9rEbKMq_bOLBy_UB6XHXCpTcmHAcgwKb9NaauP2avM4RXGXrelYnJlsgDlFtK1a4dw_mB33lTWIGHC26c8xy2tpAVfGEUvL84xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoLB_ZZO9F0lTBbFIoMlpFDBpLwpCl15VYBR27cZIF6rubPmv2I5sq_3TOGjv4Gog78Fvu-SnKPVy2dISbiC7te8qjngGUOcOgAmH0YKTWvFImeHs1Y1E28fzHTzdfNRSntXbl1bmmZzjW8lPRe5ukfJu3BqGk2-NZqSY8YNwtwetiTRkrRQaaLzCYdh3Fuu0bj5QmO69ARd3qiRTiTgkGb_KzoAX286IS1GW72qE5b0PXdaepWpi889E0vaZ4D82j6G0ogu9i_2mcdTruZ7V4jTUmjKoOBUf45M6yE0LuZy0IjDpTm19ZWHOdLI3Wm864MhbO8410nB_BB18Jm2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF3H3FummN3flH0uaOK5XiSGLKpdkJ2R2zptOzYpbeTUz4YjFuWoWzP2GVsr0AYwDGzT6VF8SgCAj7WEBSLkctcqh2s3t8GM5-zgpsmAyJ3-tVHQm1FKTvUSbseqgDzCRAerqROKLJHEXL14MaGOJGRK-aqWCWfJ3Bu-oRW7D7VJwE-hfPAdW0b5D6xba0-5Adkmf6lvHwIo32M6Y2nGgJO6bytdANE8lNH9qCtON1jR2SGyBCDIrRoDrWz1ruvmG9bjKGpl3TmRSku8ZnLr-61Uu_GQuU-G1HXJxRchR8hdKZ3oXAK30jeqOpw_3zRw3dn227WqMQxovqja7QmPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT-aPWNYqwDNDK7V6YTaT8pivITBcJUH3ZUwnk4WdhwtzOtJQeOQvOi32Qxko9iOsxzA2vP_mPNMT7gIOnb9UVw7jRbUkZqoL7TfMhHUMhntXw3Fc5sFzOCo21QxqKIlKEtuRoD7IG1LKluiqYeRBA_vcids-4XHKEhnmD6UclKn9U60uOWB8ZdDF4rmM1p-M8HUg6jAJdWNujQDaneAQ__xQf2FQzsag10uny8Nc10l0Bz3pLM2RpUGiSowgI7pdIqmFKxfZ-7sou6_yYjXnA4zEC9I596xav1uphoP_2XTMgG45_AzLZ6WDKg6rPGy1DsTyM6MwQS-Uy6XlwIPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeENMIGvR81AG7m6Ovxx60baC2JoHQZ3v1qhmBFRsgRiKGDLd69-wbyjYlyhcoMz7J5rk2aIsQNhMfa0s2xLxJCHHDpZSGOWEtpSNKFx_kRlx-IMtpSjfxOtQ1t-hcMNZT5FhafWnRfBeSFGb7k29Bg_6SbZ5_itxi1ca7dwD2TjH5oS46Nl1l2P0B-WNGgyCacHQNbanYvhZt8uZoGo31xAlpRpB3nSyWuwvMDKHdjbQ0P63yYi55b1sz7fqgGe9WFW6GKvBqdYLDyvQVJ0Of7-eLhag7ko-HIitUzJCPVKsQw3r5aDjwtqHlaflyIKT7uh-QeVQYacUKZYC3xk5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=i0xM_vWi6KbqmQSsSCt-NXEqO3ewjAkbOK3WZRo_qgICztqUxEWGn-ox5ddqRU3HuiadlWHxZUMQ1Q2bpJGINaz486-Vtfw63xGVnoFuzthsUsenx0apTcERklIGm4r65rHRWYEz0icaUynSaS1yCCH-aQ_D-tTiAYMYzVoEPZDk9KveibpD3Sv6hQsqYaDyI1aVNmSFFukyO13yP29LbyQmCv9NAO6j0VwtPq8FerXOPhdB5v6j1HVUanSimHM0hbcLNXEOycQ81bV2mgBc5K6TpCMpwLp78Cib6jU5vPps09Wzf3EIZXHM0gu126FJ9svgo31SpLU_N1onlW_tGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=i0xM_vWi6KbqmQSsSCt-NXEqO3ewjAkbOK3WZRo_qgICztqUxEWGn-ox5ddqRU3HuiadlWHxZUMQ1Q2bpJGINaz486-Vtfw63xGVnoFuzthsUsenx0apTcERklIGm4r65rHRWYEz0icaUynSaS1yCCH-aQ_D-tTiAYMYzVoEPZDk9KveibpD3Sv6hQsqYaDyI1aVNmSFFukyO13yP29LbyQmCv9NAO6j0VwtPq8FerXOPhdB5v6j1HVUanSimHM0hbcLNXEOycQ81bV2mgBc5K6TpCMpwLp78Cib6jU5vPps09Wzf3EIZXHM0gu126FJ9svgo31SpLU_N1onlW_tGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Wihz4Z8s0MSQ8yRqKIfsijw0XObWW3G0-cvBdyIEhl7lA2FTOvzmhqKkh9CkRzbiXnmFymLz83Lqo1X_BYlhueF-jd69ZDbxrYngVdBi4563IerFZBrvIbUGwyBdTo8sivZQnZkKWfSVj14ai4sd9LlNr7vd8RZrOCsyCbgt_y6MyM_xA_xZcAR7hx2Ajdn-xUDxDecIjB67-urc6fcsYk_TU3jMXmL6vyFLt0CQI59RTfRxC5i6s0IE9WzMPW-HAKmq5Xg0R-uagps9cj_wlonBePLPME7DzwYewdgwHjSyXFOz2h-RoHXecbnSFni0mYsdiA9w16AWWWeIGM2gfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Wihz4Z8s0MSQ8yRqKIfsijw0XObWW3G0-cvBdyIEhl7lA2FTOvzmhqKkh9CkRzbiXnmFymLz83Lqo1X_BYlhueF-jd69ZDbxrYngVdBi4563IerFZBrvIbUGwyBdTo8sivZQnZkKWfSVj14ai4sd9LlNr7vd8RZrOCsyCbgt_y6MyM_xA_xZcAR7hx2Ajdn-xUDxDecIjB67-urc6fcsYk_TU3jMXmL6vyFLt0CQI59RTfRxC5i6s0IE9WzMPW-HAKmq5Xg0R-uagps9cj_wlonBePLPME7DzwYewdgwHjSyXFOz2h-RoHXecbnSFni0mYsdiA9w16AWWWeIGM2gfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RfkCOooyg5s-uC5Z9guH2tfsruqnlxAlYHZm_ZmyLeXqdoid-xMLjjf-UWYY-fw4AHJstYZdj29MEeISP_n6bgQaABZzZXo8uHDCVyDyR469X91OsjZ3xdYfWFnvdpVIxwD-s43lLEHxyuEnnqy2M-Mp74mp7sEC223hd3t_0dWuDZVG3nPooj0BehDzDUlpw786m8l5T22SzOMQg_Yy1MarX1AELJUlOhWu5NNku66YeBL7Ji-vF0HFDEEUM7r82POV6zxx37WcWRS0p8ehuPzOOtAOgTZ_ZASd4W179S1xu21oFpIkjIkvOocW1tDL3B-FM9C6_wdH-spqNwMaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RfkCOooyg5s-uC5Z9guH2tfsruqnlxAlYHZm_ZmyLeXqdoid-xMLjjf-UWYY-fw4AHJstYZdj29MEeISP_n6bgQaABZzZXo8uHDCVyDyR469X91OsjZ3xdYfWFnvdpVIxwD-s43lLEHxyuEnnqy2M-Mp74mp7sEC223hd3t_0dWuDZVG3nPooj0BehDzDUlpw786m8l5T22SzOMQg_Yy1MarX1AELJUlOhWu5NNku66YeBL7Ji-vF0HFDEEUM7r82POV6zxx37WcWRS0p8ehuPzOOtAOgTZ_ZASd4W179S1xu21oFpIkjIkvOocW1tDL3B-FM9C6_wdH-spqNwMaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=axIr1LodzzVrMagRRBECkP8nYjTkxEsGLwGv6Bl_1h9vV_uKE76QEH-zuLolf_-905CuSAVf1pS6BzJTQ2MfIWQi1rw28-6byh4s-9oh9r4iMqBt9hGB__4FOiKzLw4pKvKCqDEnX2Sse71vcWvbRYoTzLTTI6OwDim1MVf3BP5bw7OJCjROcoTLLzdTErztZYzAPNpo0dNR5iKyRi0LDnNJbHWLyed19gKc3UsKZ6K3JRN_wsEzg-I5LkUlUzpUGiEIdtUxwUYvlS76ka8r8QerSRWqYcBOcnlI-yV7T07O_KtNAoQc6jGOTES7O9L054JTEIYWYf9jey2OXC-Y5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=axIr1LodzzVrMagRRBECkP8nYjTkxEsGLwGv6Bl_1h9vV_uKE76QEH-zuLolf_-905CuSAVf1pS6BzJTQ2MfIWQi1rw28-6byh4s-9oh9r4iMqBt9hGB__4FOiKzLw4pKvKCqDEnX2Sse71vcWvbRYoTzLTTI6OwDim1MVf3BP5bw7OJCjROcoTLLzdTErztZYzAPNpo0dNR5iKyRi0LDnNJbHWLyed19gKc3UsKZ6K3JRN_wsEzg-I5LkUlUzpUGiEIdtUxwUYvlS76ka8r8QerSRWqYcBOcnlI-yV7T07O_KtNAoQc6jGOTES7O9L054JTEIYWYf9jey2OXC-Y5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=E4hlroJQ-ouXdBlEYl8KarxytVFhWQakiOHhAQP8tzTZDEnaAgDlQFNc8-C9rAWVIOmZyWidGLMRl_AZ7bHqzyO7pdyMiHvBWxpGUNoBQoLPXlZRRP9VH4lbikh_90gXnf9LVEEbqDHWt_NnOE1I4IFvP_CpYxBxgAcDiyTrDRHTvqmBIvDPZ6UDFlquiskEIHeqoC-8GMGZgyFSKqAPrQ094QYkYyEtBhK8cJGMbxF0QyrPp3St364IKkri0nX9bN0uZre-LkSIAik4m3A4ckaH7VX5ApNYN2HRR1m1cB9rKLa6IQmHdghdLqGFwL-IpYpu8qf52ubKUPrpaG13Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=E4hlroJQ-ouXdBlEYl8KarxytVFhWQakiOHhAQP8tzTZDEnaAgDlQFNc8-C9rAWVIOmZyWidGLMRl_AZ7bHqzyO7pdyMiHvBWxpGUNoBQoLPXlZRRP9VH4lbikh_90gXnf9LVEEbqDHWt_NnOE1I4IFvP_CpYxBxgAcDiyTrDRHTvqmBIvDPZ6UDFlquiskEIHeqoC-8GMGZgyFSKqAPrQ094QYkYyEtBhK8cJGMbxF0QyrPp3St364IKkri0nX9bN0uZre-LkSIAik4m3A4ckaH7VX5ApNYN2HRR1m1cB9rKLa6IQmHdghdLqGFwL-IpYpu8qf52ubKUPrpaG13Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=LmNrEPHaGHvaOItsEPSMWxxsXaVK2hs4Qa9PHtqoX5iCvkFjZ3UzCwog-56c_Awt-88lBzaCsiUbhLfLr033H7m0Ye76lH24o3K1FrQsw40lBMrTol7MJbf0tNeC5wt6MCm_qUEtYsG3lvLBvVPmryPIjofN80DMExz0MGlUKxpNMQpHNuF5VpfYsqwO-B-JN4nI25SgVzGkmDmYGJuBBWqEPWE3pgBXoS6t2w5G8JsC_aVdvm_CSak5ipyJOK0zV50wnq9_IWscwCAAgTgJGzDXkPJV_zRiqcsjFbj4pKK398g8lXsvbBA6jKZ4NdmxL3Qu_RqhZv_C1JB5ttYGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=LmNrEPHaGHvaOItsEPSMWxxsXaVK2hs4Qa9PHtqoX5iCvkFjZ3UzCwog-56c_Awt-88lBzaCsiUbhLfLr033H7m0Ye76lH24o3K1FrQsw40lBMrTol7MJbf0tNeC5wt6MCm_qUEtYsG3lvLBvVPmryPIjofN80DMExz0MGlUKxpNMQpHNuF5VpfYsqwO-B-JN4nI25SgVzGkmDmYGJuBBWqEPWE3pgBXoS6t2w5G8JsC_aVdvm_CSak5ipyJOK0zV50wnq9_IWscwCAAgTgJGzDXkPJV_zRiqcsjFbj4pKK398g8lXsvbBA6jKZ4NdmxL3Qu_RqhZv_C1JB5ttYGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=TTK9mGgfvg8Y58XHS7qejl19jBk4k_edSlX3Ls10NV6J8pxOE56imNvPFqKRcD9GO1Nfgoqnm1AHnluSmQSF8s9XRhYr65Vq8ukM0wmz7t-S_jT0Nsm_b3cV6QmNwahAI20LOYNAb2mkHJAY3a2T0kQGVOmx68JkBuYLBvq7U6I6L-VAa5xgyHX26GSXIR_3_yVOUTp3JikbglOykxBRKBDsirI1vWOimg1RQURwTgPhZCyMH8ZT6_Kgjn0HX0jjdRqVfJaeCB67JvnP60cAuci9lyIyDvIRNuvIpTO79xLqDjItJ7bmTVC_WgIGO4ixqoU28mOh4OoDIhxa7CqQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=TTK9mGgfvg8Y58XHS7qejl19jBk4k_edSlX3Ls10NV6J8pxOE56imNvPFqKRcD9GO1Nfgoqnm1AHnluSmQSF8s9XRhYr65Vq8ukM0wmz7t-S_jT0Nsm_b3cV6QmNwahAI20LOYNAb2mkHJAY3a2T0kQGVOmx68JkBuYLBvq7U6I6L-VAa5xgyHX26GSXIR_3_yVOUTp3JikbglOykxBRKBDsirI1vWOimg1RQURwTgPhZCyMH8ZT6_Kgjn0HX0jjdRqVfJaeCB67JvnP60cAuci9lyIyDvIRNuvIpTO79xLqDjItJ7bmTVC_WgIGO4ixqoU28mOh4OoDIhxa7CqQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9TJP8OgMG_ZJC07pzR_1fUbf8FmVKB51TnjiMl1C739metorsgOi4Fysi-pwLt714nf_G7JsmLlxgf6PVeFRMSOipiVW6sKTGtdalgzVE3GhVDfENEirzHthsLJ_b1OlX05sWeGoxwcQ-u5iDYQol-NKkGJttVmQ9YtwNOfbRKTkdslyLNhfNuX0SNhASOpP7y7hpRpLutFZlKxZWUKVkLNwcn2F-_HKgkn-8yCG576SAuaVV4hhjTFQg2ts-Egegvh8dHT6VJR9uOOpOUovQxmfD690I-eO-cNN99EMVR5zY5z4VJ2IWppY5LpDUwR_wQP5bHkeW3eiMxnc4hI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SSNZc-VjndcLB7laKJfMbTzqdA4nc5hKd_6xbzdGuAoyXJnxtgq5-2cZxkeYteWqX70J4pueRV5f9peM2YUzv6uxEaXmqv4xuik5t46JD7-8bcougQaJkFIwtcJ-rf4Fp-2UBvn5qEl-PWTEZGNI_gBUeg1qGccjGJBJk4NgsXQhYbD2OtRLvpKYx1jmwcj2-rsJQOjNN712YcsEkRHCUJ1VJoFbPQTubMu5PFYJcscZKY42fzegIV4MYQTzDc9ovzfMfEb-6_aXEXnE1-VTw06zkVG43thZrZsTsI1cD2LevG0BCCDUjGaYSmrJMXSLryzufhTCSfUl5hzM25moDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SSNZc-VjndcLB7laKJfMbTzqdA4nc5hKd_6xbzdGuAoyXJnxtgq5-2cZxkeYteWqX70J4pueRV5f9peM2YUzv6uxEaXmqv4xuik5t46JD7-8bcougQaJkFIwtcJ-rf4Fp-2UBvn5qEl-PWTEZGNI_gBUeg1qGccjGJBJk4NgsXQhYbD2OtRLvpKYx1jmwcj2-rsJQOjNN712YcsEkRHCUJ1VJoFbPQTubMu5PFYJcscZKY42fzegIV4MYQTzDc9ovzfMfEb-6_aXEXnE1-VTw06zkVG43thZrZsTsI1cD2LevG0BCCDUjGaYSmrJMXSLryzufhTCSfUl5hzM25moDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=eJGxyM25xFUzoVBrkFzS57sq-dmmcTK_r6P_VKKAw0fMzLbt7xbbzDUhC5EWefcFja2Q6JHez_qjfrWM5j56VXl80WSPBMIStCjpr9SNZwnG-v9YpzImuNzomA0t2K7rO7xhexJqiYnYKRq-G4NxENUCnME3kuqIRYNQ5dJdIqXd97AJcOi-KnlXRimL0Wl79KYupEO_uXdZg7pslnL0VCOeTcoYPJry1kCn-beYwL1UAxtjJ9w-GSOrDdQkHyxjcbE9KMpZVXTcQoQ1G833eKIaYQHo0bjs6G_IRnWgIhRFA-ZgrU9_URCW3cTpazZHrFbJb28z-BUMs0DCDF4xxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=eJGxyM25xFUzoVBrkFzS57sq-dmmcTK_r6P_VKKAw0fMzLbt7xbbzDUhC5EWefcFja2Q6JHez_qjfrWM5j56VXl80WSPBMIStCjpr9SNZwnG-v9YpzImuNzomA0t2K7rO7xhexJqiYnYKRq-G4NxENUCnME3kuqIRYNQ5dJdIqXd97AJcOi-KnlXRimL0Wl79KYupEO_uXdZg7pslnL0VCOeTcoYPJry1kCn-beYwL1UAxtjJ9w-GSOrDdQkHyxjcbE9KMpZVXTcQoQ1G833eKIaYQHo0bjs6G_IRnWgIhRFA-ZgrU9_URCW3cTpazZHrFbJb28z-BUMs0DCDF4xxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=jaEV525wwJGkeWA2gIm-7bElznh4j6BzZz_wJo9lDAflhdmMQyptQuvIm5BQ9OzYodWwuZT8O5uOs6JiK93l7vyYjjIblusqRhOr7XCC91TPGrY3FLu6RmJhhj46zT_z_hd1LoA4l8CTVGSvuKKtF_rWhHYstTOATp7xQ5VqOulbqQqZFS-Z-HnNmbhiNumNmd680nTekOvnlbG9VclAv93Rw6cCn44O__NqWv34yYnvIT9YGBY6Gsr6gJ-VGhDeOHZRkPh13nm11vKSwuvlGhfce2kno3NfnSKGWypB5rTIBWeCI1behj54wPUO1kBk39RyAi2vUnYr2L4i7RxovSDs0G2WwcNdPmEaGQcxtJFpRoZVBfEh-RBZzA71u9A_y0VG6zO4ISrlOVdMtio883RJylrxcPfGpguKQJIwOr7tIvEbvC8BK9xtQsQN1Q3vrM-rJfD3UukC4zy6Q7xSbv_S-uEADwh7lSp5dch2_SamMpc4zKKN16VZeeFZJi2oTCk0Q4iaIjEfU2dYHsljPvnQ8dzTwnskydbGnxWWBQdQ7zWHIGU3NPgxHit7yl5dLV5Z03N17LfMhnYKFHgJasSprSBClK6eOfCXbhw7e7G6RWfuP3rcB8mEMQLVz0I3b72cbI03kn68QgKN5FZHj-TCsINcLA-JZfnnw3Zu8mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=jaEV525wwJGkeWA2gIm-7bElznh4j6BzZz_wJo9lDAflhdmMQyptQuvIm5BQ9OzYodWwuZT8O5uOs6JiK93l7vyYjjIblusqRhOr7XCC91TPGrY3FLu6RmJhhj46zT_z_hd1LoA4l8CTVGSvuKKtF_rWhHYstTOATp7xQ5VqOulbqQqZFS-Z-HnNmbhiNumNmd680nTekOvnlbG9VclAv93Rw6cCn44O__NqWv34yYnvIT9YGBY6Gsr6gJ-VGhDeOHZRkPh13nm11vKSwuvlGhfce2kno3NfnSKGWypB5rTIBWeCI1behj54wPUO1kBk39RyAi2vUnYr2L4i7RxovSDs0G2WwcNdPmEaGQcxtJFpRoZVBfEh-RBZzA71u9A_y0VG6zO4ISrlOVdMtio883RJylrxcPfGpguKQJIwOr7tIvEbvC8BK9xtQsQN1Q3vrM-rJfD3UukC4zy6Q7xSbv_S-uEADwh7lSp5dch2_SamMpc4zKKN16VZeeFZJi2oTCk0Q4iaIjEfU2dYHsljPvnQ8dzTwnskydbGnxWWBQdQ7zWHIGU3NPgxHit7yl5dLV5Z03N17LfMhnYKFHgJasSprSBClK6eOfCXbhw7e7G6RWfuP3rcB8mEMQLVz0I3b72cbI03kn68QgKN5FZHj-TCsINcLA-JZfnnw3Zu8mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=VDSd2k4zd-blKdJx7fgoAqM0STGwLTSyf3LlXbr2XpdHeF8dMVo_fgDn-6UArreMLsTHHaElVGc327SkDLoySj2XoGyU70YVBaPWP034WWqXXFrY5kjx-KdfLBSg3jIXFtMEq7BcHzP373tR8IMOU1yuzcQb_zoWfx0Sx7QM0czUv4uqJoAu2wkDL3Cvhm5GfUOz0sNbloXeRgw4Z2tL8mU-ryhYw_LMj48v4IrGKjsLGLH1OiYsz5wTMvO8JPwrFJwC-ySHnP9sCBoKblw5llQ6ViPWezgOZqQAqBnC-mvJz3b03qw2GUZ-Wp1wEE434hWdRJEYKKDuSRR6irkQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=VDSd2k4zd-blKdJx7fgoAqM0STGwLTSyf3LlXbr2XpdHeF8dMVo_fgDn-6UArreMLsTHHaElVGc327SkDLoySj2XoGyU70YVBaPWP034WWqXXFrY5kjx-KdfLBSg3jIXFtMEq7BcHzP373tR8IMOU1yuzcQb_zoWfx0Sx7QM0czUv4uqJoAu2wkDL3Cvhm5GfUOz0sNbloXeRgw4Z2tL8mU-ryhYw_LMj48v4IrGKjsLGLH1OiYsz5wTMvO8JPwrFJwC-ySHnP9sCBoKblw5llQ6ViPWezgOZqQAqBnC-mvJz3b03qw2GUZ-Wp1wEE434hWdRJEYKKDuSRR6irkQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ETe8Q8e9Rw5KEj6n7KNd6TtHuIfopRfaBnlTnbjwCilKBggfvbEZlxKFbfAaf4P3TU0FElbkcSioN3DhTlr8gpL5oopU7GnbeD5ed0sDwQsZk76WVMGG03pqY_QjgfDgNvWJ9LPtjcoeQSOqPE0_bgcV0yFKQktRQhu1IuW_bQOPWUZ4EvN0LlvqoEw0flWtjILSLJvuWEmZVZt3WHAa73N9i9EQssBqZSNAHcfyNhxgf4k7l-xEsOkwcbcjpd-p1FKy6rzxbND6gBQmUN0YSeHmf2gT8D_xmGUct7JrcmSWOLctjW3m03D_D7qEvq5pmr5b750EAE__jyRJVzm6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ETe8Q8e9Rw5KEj6n7KNd6TtHuIfopRfaBnlTnbjwCilKBggfvbEZlxKFbfAaf4P3TU0FElbkcSioN3DhTlr8gpL5oopU7GnbeD5ed0sDwQsZk76WVMGG03pqY_QjgfDgNvWJ9LPtjcoeQSOqPE0_bgcV0yFKQktRQhu1IuW_bQOPWUZ4EvN0LlvqoEw0flWtjILSLJvuWEmZVZt3WHAa73N9i9EQssBqZSNAHcfyNhxgf4k7l-xEsOkwcbcjpd-p1FKy6rzxbND6gBQmUN0YSeHmf2gT8D_xmGUct7JrcmSWOLctjW3m03D_D7qEvq5pmr5b750EAE__jyRJVzm6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvonRssNqGHgIiYOY-LA5qP8tGmBDp88TTuB2eFeDf062uhGFg2DDeDKGzJtkb_fF0aQ-fGHtOOIT6EpILeMs2L7pHRr3aAZull7cX72FlI0lTNoalfF4iCi4tTLtPFSkLfD0VZH1DdoPBXHFRIE7L3fkvdaXkM9KZLQdPAHAQW5txn1RIuXljvu3CjPpIelsp1NW8Bb6oTd4sZyFbgbNTGyKCCdEtbkkeXdX1kmvnuT3UQWdtEz54GkAC05FBjKpL8L7Zo_ApZWHxsBiRx1cjprQ4XyEBDNqd6KJeTKSD-KnngEa3HzRes3onHXPdQVcoDHfe4Kd_rgIRNzE96iKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksrMrBgZOGMd2DTaEQYoPUybPa98E-aV57Z215MXGG9vxQt8urkUtc-95YXitG2JrSQk95tY9v-sJ5pac_tY0aKz3omuMtkH0xrYQo6AxdQZREbrtm5PaBh-VbWKywVouhoUoonL801Z_XihVZM7r3FNeeA3r4ELXmHIDmDliCFm0b_hVdu4pp9Fkz5SmMNfOPN_17HG_y2lVznlvmrUP-m5xUhDolNigp8zTcD-uecuaSz_YVHY6r7vDNa5s2CTIm_ZnUrkn6_a0gsNwMgXlldbpp4smXuYq1aKQbAvhjNAgbL2ktdODNfd_rAoOsBgYWD3b3gBOQ33CdbwOs5_Uw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=PtWs8KAVUecJRbxsPuL-KqNWLPPqIxf5maanuKv0F02_FPGZN067w5O05ZDT6ROpeLYdtSifhKhXE5cC61M3AdgR5E1PUoLH613syGiVXsTBNB43QDImP1xf1PKrxCsCQPwWmXr2nwzn4WzRj0NOpbD3qe4fPeAVzsD5V8jHq54bZ__vJfql0CMg5yJZBAyjQpLK3bLCSAyd5Wono-1tyql8Er5y3qTaAApKj17Y3zKHSoNtapT2Cc4otjQ_H7pKGWmHE3TspWna0fcxP0SezwTC81lEg2AlDgH2FKK_korBvqLmgw36aFepxiga6l-MIF4Y1cpveiwi301szcy6O4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=PtWs8KAVUecJRbxsPuL-KqNWLPPqIxf5maanuKv0F02_FPGZN067w5O05ZDT6ROpeLYdtSifhKhXE5cC61M3AdgR5E1PUoLH613syGiVXsTBNB43QDImP1xf1PKrxCsCQPwWmXr2nwzn4WzRj0NOpbD3qe4fPeAVzsD5V8jHq54bZ__vJfql0CMg5yJZBAyjQpLK3bLCSAyd5Wono-1tyql8Er5y3qTaAApKj17Y3zKHSoNtapT2Cc4otjQ_H7pKGWmHE3TspWna0fcxP0SezwTC81lEg2AlDgH2FKK_korBvqLmgw36aFepxiga6l-MIF4Y1cpveiwi301szcy6O4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCxqLm2-gfuIYAzNlP8C7YPiGMzi5cD2aK0_J2ibJaDid-T8FvJBJ4s1syWyM8TkLIagE9SY4wsXTupf6nWHh6_2ZCLdWKtN7p2Mmva3oB1YqToxHs6SUiTECgW_jGxvcX2zWFU_symA5KqfC3synyRmx7cnzG1oOx9Kee7gPdrdrlOweqo4_l3N7nzgUdvjU9y1UKnQxw1ijG51JLcyiSVw917hvUIpXlWAypl_HllrXuxvlcsPpbUie0UHV0YTzKKyqRvEKvQKYDn9c2xZqMDyLQTU2TuAyLfXD-z84LaHy5G8m-NH21di-1jh5cfItH1rUnAXSJdLlsjptLre5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ou43LyyYdyoYBHV0vZxWQSCpJtFKv6ii8myxnckCM0Aj-98GcNREvkUFl2VZv8CPkmommuwh0vhZVkD33zZqcJwVMoU4awnBVbrAsec8xthABS6yoXsvk5g0wQe-g4qOp4q_ip19i8b8q72w9aDIp32E7d2nRVCIsGvnVi_m1WHJ4bxgTilSHr0zsi4A1tO42vAUMpX4smgy2yJ7SIMnqnYJWcHQpXpgKqA1V-gCFWZ_QWBDsLI23pHtqyMQu7Y2h219k_Wui_-_YYALs5jyfA-2hJetDBq0BdRa_gqoK8AluKvayOs9Rs7KKFktJVXOYgs1hJm4PvUCVzCRlEXhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJI8osJ9ziADpBPFj1W1KOzDIHN0AgRUMWA1PYeZ0Pd57hrpdgQbbUliMHmDYVe7QamdzmdHIuwCd_SB74LgsRf2-SmKKCiysA2ih5HIzNKzmJ-iyHyFWGbdn9Fxs_kHOus9bNYm6W9Kk9mvkvTFTS13KQwMmmEs66Xldq4-p4Krbthl0zg0GQDpO2xLI62nSSXFPxlH050qe2L1P1orzZ6B4MJLY1z1VyadxnfA8PCvlQjWAGxVeqcSo4EK3bOjjJqP-rImA2MEIdhwM6Y_pXQ6FHIhW5m8Ke8aGRkhc-BvLjPpWfv29pjhhxg1meWzq8m6DC1dAT-Fn28AG1oy8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLk43E_Hf58Y1MhWf4fd1YEqaBJgiwNH8B9hmC6NfsPl94GFocy0t94LKhBIA1ulcvhs9lLyz4wHD2kTSD-dKSfnoA9g6fTyZReesGHuHd7E1TEe51_T_C70qkZ1B6narX7Z6vkXrwnSoUEZRM4Bu1S-UpMNFVy-QdO4W0f0SnrWemSPd1AxngWqgBFnVRaQH0ttC6Yqzhyje6LctXFtXM01jHL9Yid5O5tKWd05acjwSeXhmsyNUQBps1pshqKCLtKA4aGve8URSwivzLiz8xz4h4CuGL2zqBgpk5WhHn7pnutMsBN7-shWaLxszFQw5oejGHoV0AXAGEDnkxiyVw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=PN0IG3kd11a0y6z8bXCwv9Ses-GlW8WG1q_r2jE9qF0hEbrDtO-o-v6kSbUTSGIokOZsPdl2FIEdzdX0-Fno7KMCeVZ21lXH1bvBiGWJx2nTPOaE7ZlJg6WgcvRbmsJh9Oa2Eff_JLd6sse9XR--RXXTq0MWFsbiN0rF0gOqcAOsHBYR0f6YLILvdejtDTEcnoJxk0kFCO7GQGw3bG2-dFtMcFb4CIiFp2iH4lHZ0hFfN9VoG6jGCcJsq3MsH6lx9-f7MDl5Zu3qdpiicLy4WPYZsm_bHf3eY9jLlRyFy4ht6r6QqziFiXSt1kSIdoYk81bdHnFOqpx2tHZ2rLtxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=PN0IG3kd11a0y6z8bXCwv9Ses-GlW8WG1q_r2jE9qF0hEbrDtO-o-v6kSbUTSGIokOZsPdl2FIEdzdX0-Fno7KMCeVZ21lXH1bvBiGWJx2nTPOaE7ZlJg6WgcvRbmsJh9Oa2Eff_JLd6sse9XR--RXXTq0MWFsbiN0rF0gOqcAOsHBYR0f6YLILvdejtDTEcnoJxk0kFCO7GQGw3bG2-dFtMcFb4CIiFp2iH4lHZ0hFfN9VoG6jGCcJsq3MsH6lx9-f7MDl5Zu3qdpiicLy4WPYZsm_bHf3eY9jLlRyFy4ht6r6QqziFiXSt1kSIdoYk81bdHnFOqpx2tHZ2rLtxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=adGfJA1LtwdrjSvHMwtYW3uvUBgc6wVKBqGvDs6QGv8NyFPCldS9qtAJT4cD6w4eIt4qmapfU9kMncPCWDSLNuqXtgWDJbqTz_yliKG23tRO2AXZXPFwQWPiNivmXE_BNv4cYU3mAhFmnB-Ico_GcSzX1s5QBONqXXwym0BrbLqJKq_NFZYufM9LrqpamE4Rf3lkTW7dwrnJZevuug6mn7xeDbv_WMxKxyuSj-i8XODn-7GSAPd4J7IDJwuCO28fXwaajpIS71tTo_PU1FRqXbB3SB0ndBBgnVL10mUsqLN1BBY5Be7MFvEYBHqf8NifwijHuj4W15xmxIwewTBzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=adGfJA1LtwdrjSvHMwtYW3uvUBgc6wVKBqGvDs6QGv8NyFPCldS9qtAJT4cD6w4eIt4qmapfU9kMncPCWDSLNuqXtgWDJbqTz_yliKG23tRO2AXZXPFwQWPiNivmXE_BNv4cYU3mAhFmnB-Ico_GcSzX1s5QBONqXXwym0BrbLqJKq_NFZYufM9LrqpamE4Rf3lkTW7dwrnJZevuug6mn7xeDbv_WMxKxyuSj-i8XODn-7GSAPd4J7IDJwuCO28fXwaajpIS71tTo_PU1FRqXbB3SB0ndBBgnVL10mUsqLN1BBY5Be7MFvEYBHqf8NifwijHuj4W15xmxIwewTBzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCp0hcGgh8u2uyjln2IpBe4A5MUyyQu1xa1kXql4NLhODh-bykN6tZwK3t8YLpJtJUGkDnCHKoKsX6I47IQrwSEzIckA6cJKn5Fgg-550HAci4Mj6zXFBHzyksC57GhdiSQz88EN-xKX-Wa4EDF-AhJceuWyVq3JHO8oXg4AJYHytLLJPjrSSZ8IF9w41o2o5QzfNnc-gvdvbklIW0oXTAnRBRCYmbNh0rBiXB2UstwUIfwQAyAcrhr0FqmWZqh0BDR1uUK67C3rGmyCIrsj7O6tl9g179pfXManpOettoGKQ4UWqiSZruj-FMTX2_jzn837Kogu9CUB0Bge7Yfcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=I5ciHxYVHkL80WPH0WjUiz_VaSbGBixYsmSkzs8zVZUFZsU1pLA7z9p_3fuU50_tX_WxA9LE5BIL4zJa-6rGgxnHOPi2Gm6EJBuMnhmpLDPFF6-dTVZRHEVw2IgvijSKYbvMHqryU1RuDXe7fNIXWT-9t8C7JMmtp2ZquKNpaPRCGODWxAxRYOQpdiHTM0RIGU-C40Np8a7knbYUuz65LYOCPVu5BCCI2-V4eaBNgjs9JeJc4MienfPv5B_S07TrM3eD5wKS0J6XkKWj8uWQzAVSaeNtwOjxqdj8PlG5AbRAjD_wt9anrODKc532IuwqUOK19XhZCKGw8hFFpsvdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=I5ciHxYVHkL80WPH0WjUiz_VaSbGBixYsmSkzs8zVZUFZsU1pLA7z9p_3fuU50_tX_WxA9LE5BIL4zJa-6rGgxnHOPi2Gm6EJBuMnhmpLDPFF6-dTVZRHEVw2IgvijSKYbvMHqryU1RuDXe7fNIXWT-9t8C7JMmtp2ZquKNpaPRCGODWxAxRYOQpdiHTM0RIGU-C40Np8a7knbYUuz65LYOCPVu5BCCI2-V4eaBNgjs9JeJc4MienfPv5B_S07TrM3eD5wKS0J6XkKWj8uWQzAVSaeNtwOjxqdj8PlG5AbRAjD_wt9anrODKc532IuwqUOK19XhZCKGw8hFFpsvdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=b0GjsctUsJhtJv9WsjnCk8Q72D_kOO7tMYuVkz_I533oxYM47h5d6tNMVDjo8ndr1hVoJEFJaEjCn7wyOc9EeFb4BT0FoJLWvJw-rmihpAM9go-8aPMGto3r48HOsNmjXsvW-jfkCIjLV4d1F8f2_mQQTCDp87CPZmg-3UCtxO6kv1XhMbGGsCg6hZjBathh1CB-O2Lmw7Saw-X6DzBmptA5zaDc0rgi1cQ65ZJWVaKrsJlMdHvy43_Igi6xQfEnq_Z-tcbWBg1ivZIyItbTINe4rpWMX1ghNAeyVCQ3IZ_1Qaao-TQcD8SOStTGaWsyNR9uuxNovOS1K3Fatrjvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=b0GjsctUsJhtJv9WsjnCk8Q72D_kOO7tMYuVkz_I533oxYM47h5d6tNMVDjo8ndr1hVoJEFJaEjCn7wyOc9EeFb4BT0FoJLWvJw-rmihpAM9go-8aPMGto3r48HOsNmjXsvW-jfkCIjLV4d1F8f2_mQQTCDp87CPZmg-3UCtxO6kv1XhMbGGsCg6hZjBathh1CB-O2Lmw7Saw-X6DzBmptA5zaDc0rgi1cQ65ZJWVaKrsJlMdHvy43_Igi6xQfEnq_Z-tcbWBg1ivZIyItbTINe4rpWMX1ghNAeyVCQ3IZ_1Qaao-TQcD8SOStTGaWsyNR9uuxNovOS1K3Fatrjvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=agEQVkvkgi1b-5pNnE4f4SYXJRp0z5yoTx_fxh6aLYAqKLMj4xkg3CjZ3b7AAsg1rpVpfttXC2zhLkfqP_--psIE2vKpkK_z9otdx6qER0nJ9tQovG-h_yMJkokWzN0ZMGtzKZW_TinORiD5Oy00y-0zzmTZFpNXRgAO4-PiXDhB8usDmVrSqQGsgmu04PA_bMYyDwxD5VB6FZC015vZnSqgemYHvb9_WPl-XBjUJKICd5Ue_HKdTdCm_WNWwRuJKEBq8XIGGKGzgYyq-uTgQnTLA5XfNvnYTsj_y3YVg482B6LxTH7qFvMW8AugTHPghsjTlc8MgOUbwXZKg6zXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=agEQVkvkgi1b-5pNnE4f4SYXJRp0z5yoTx_fxh6aLYAqKLMj4xkg3CjZ3b7AAsg1rpVpfttXC2zhLkfqP_--psIE2vKpkK_z9otdx6qER0nJ9tQovG-h_yMJkokWzN0ZMGtzKZW_TinORiD5Oy00y-0zzmTZFpNXRgAO4-PiXDhB8usDmVrSqQGsgmu04PA_bMYyDwxD5VB6FZC015vZnSqgemYHvb9_WPl-XBjUJKICd5Ue_HKdTdCm_WNWwRuJKEBq8XIGGKGzgYyq-uTgQnTLA5XfNvnYTsj_y3YVg482B6LxTH7qFvMW8AugTHPghsjTlc8MgOUbwXZKg6zXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=FIO3AwJAa49X5bBVk1Zy8pHX9wTzmDN5j_yK8_aN2YfTWKfG41aw5mx7qcGLsGkHxWSNN9oIR6Jpk9KMsAKAb3X9VdLTpZLwMvIsj0odjt2AdCCj328gCjsljH4AJvdlqlmNRfud9g9HqhoMEX6KcTcU44d6A5QhVq4rmOT1VYIcj-Do0_IXKo5ihhl63sE5bUH4CINMX8Evc40Pu1CkAGcEF3ThOYR7OVdwS8oMETAa6qwMvYBiNbhDOUU6-3LKBoMkCSJcBLwitdQ75RdWeaw75nl3aglYdaBsgMGPx4nBh3IERPLtyjqGVpjDb0nV31bZ3umRQpAkOeccg99usQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=FIO3AwJAa49X5bBVk1Zy8pHX9wTzmDN5j_yK8_aN2YfTWKfG41aw5mx7qcGLsGkHxWSNN9oIR6Jpk9KMsAKAb3X9VdLTpZLwMvIsj0odjt2AdCCj328gCjsljH4AJvdlqlmNRfud9g9HqhoMEX6KcTcU44d6A5QhVq4rmOT1VYIcj-Do0_IXKo5ihhl63sE5bUH4CINMX8Evc40Pu1CkAGcEF3ThOYR7OVdwS8oMETAa6qwMvYBiNbhDOUU6-3LKBoMkCSJcBLwitdQ75RdWeaw75nl3aglYdaBsgMGPx4nBh3IERPLtyjqGVpjDb0nV31bZ3umRQpAkOeccg99usQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq-OJiN5GTRR8JhBHVTaZb4OOmplmnMX01mZ5G1WCeuPpCin0ETmxhCcfBfa4o1AxKuZG9NAQpa_Ea0kLcYtSBdlCyClpP3ttEeXKaS77jEV95aIGJvwRKOFIxyi-Hoh1f_rHSpmZSdaBN3ZGq7QNNsbMYrBIcB0nZMvCn2GVbI0t5KX3xJVpzfMwBj_5MLFZ5Bo3noZ2_zUS5cwv6VZVyinchJJ2OvO_OeqM1g4o6MqFEullW9z-znZBXvtIHG5v7IPnMbRyhz0pR6pCWsurPz0edmqRXpw5YWpheiEDElrUiJhzmd_n9t5I35HOeKFRRMtnQr9YQOkpVUixnyVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_hqJZDw1mt2KN_aZq3Bbb0HoghIEVIHRCkU6xHKqLet-faF8Z4Qia-_COZkZPcWlEW0UfKOKTLuh1fCRrKzP5ZtlQY5ZAybo4YAIZpq6fmYpabMFzAoOJeyqIuJyrPKgWmPBOJ083YTNRI2QgaNst8GvaEwb8dZg4GT79w696bVLY96X8trnOdpgcCnItXFV4H_YgPHt2__Jau8Ck7PjprNyq8IbSNDHa-Bgf8160WiXdzvR5yY1LtGW_3u2BLBu9xddda-SmmGpyRWgTbAlk9VU3ID0s3xLU2vFgZvbJ1ovQIMpwFaG4Rb7i0uD-KRQZw_OA7MzIA7CjL5YeY9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=kTsGNra1XEnuJi2g7MSPPrKNTtg_pF_qv7L8es_08OEv4SdpC0PtQQZxzNiZSL-_APyBUuiRrImgcWfBcoij6KrAnC1hCR6S1Yq7fqPyZWVjV_JgauKALi_JA-9ySBRqrNt_dFWR48mRc3nRgJQpxO1xJS5GhZa6uPJSSNjb5X_YHhjuQUp4YzUlzp28ueb0dhJ80kx-cVsthZbi2dvo3c-VOtP96ctl5NzfY7DN9vZMco8Y_xXABOutCFbQqCOBqDeJnVcTaGqDq-gqGhU9JxqqTHK1I0jAucvPxMKv88laq82JssBtrVFyl7yKSKbGA76WH-6ysx0OzklBrGWDTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=kTsGNra1XEnuJi2g7MSPPrKNTtg_pF_qv7L8es_08OEv4SdpC0PtQQZxzNiZSL-_APyBUuiRrImgcWfBcoij6KrAnC1hCR6S1Yq7fqPyZWVjV_JgauKALi_JA-9ySBRqrNt_dFWR48mRc3nRgJQpxO1xJS5GhZa6uPJSSNjb5X_YHhjuQUp4YzUlzp28ueb0dhJ80kx-cVsthZbi2dvo3c-VOtP96ctl5NzfY7DN9vZMco8Y_xXABOutCFbQqCOBqDeJnVcTaGqDq-gqGhU9JxqqTHK1I0jAucvPxMKv88laq82JssBtrVFyl7yKSKbGA76WH-6ysx0OzklBrGWDTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YCh9gu_PnUKHzlJirpTlnEf74YLQaO5e_BiFu1ov7A8_x-rdQcJpXV28AIAvfe1h4nj14dQweU_m1G2i7BV7AeQR85BgXiOb_mcrCCDG8qRIc2c12H35_O96ihPRMqxVOg3tmdC3AUi4EUde_4UKHI_GXco9MUR-asUM-Y8SZlS9nec5UJ_a1XKTWo-b7j5cfsQPtIFENJjpfYl5KCSdLuwswE-hwiLnl--ThGhkx35r7n-DzxPFnv7JtAEQXdalG3xdoO7eT6X6K3kni2AX0zihpUC96sa55RTQoH--Ik8y3FGL96Ip8gHGRYE2tvkQYPj2R36vCotBgFirzwIzc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YCh9gu_PnUKHzlJirpTlnEf74YLQaO5e_BiFu1ov7A8_x-rdQcJpXV28AIAvfe1h4nj14dQweU_m1G2i7BV7AeQR85BgXiOb_mcrCCDG8qRIc2c12H35_O96ihPRMqxVOg3tmdC3AUi4EUde_4UKHI_GXco9MUR-asUM-Y8SZlS9nec5UJ_a1XKTWo-b7j5cfsQPtIFENJjpfYl5KCSdLuwswE-hwiLnl--ThGhkx35r7n-DzxPFnv7JtAEQXdalG3xdoO7eT6X6K3kni2AX0zihpUC96sa55RTQoH--Ik8y3FGL96Ip8gHGRYE2tvkQYPj2R36vCotBgFirzwIzc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=kigyXQPh_Cxf1G1ZqJyTuyOj3nN7kgJJs4TCBaqtwxEPAfO3HqQDr3aQX3PAQ3Ac03xwCTrri68LmXIX72hyAk7ble8IkWNz1DWytZQ-b0bBFt23vAyig3uZTWYlzOhqF07d-DdRttG22l2Kr48v8Qzvbb19grZVymHgH_WzlFZmMKi73p2dJ2V4vK90tOcZMRjMH4tVt7i473y3B8gPMV1FmYach4ZLvVLBX_ruFi5PMqEFLxvpfdoC1GigHShuc1gh8_LgAF_NEtplQHNm0G1RQ3dNAwvarl0ntDcrMpFNF7CW5eqnTi9nBcMhEftwgXqB6RJyH411GAB1NjLSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=kigyXQPh_Cxf1G1ZqJyTuyOj3nN7kgJJs4TCBaqtwxEPAfO3HqQDr3aQX3PAQ3Ac03xwCTrri68LmXIX72hyAk7ble8IkWNz1DWytZQ-b0bBFt23vAyig3uZTWYlzOhqF07d-DdRttG22l2Kr48v8Qzvbb19grZVymHgH_WzlFZmMKi73p2dJ2V4vK90tOcZMRjMH4tVt7i473y3B8gPMV1FmYach4ZLvVLBX_ruFi5PMqEFLxvpfdoC1GigHShuc1gh8_LgAF_NEtplQHNm0G1RQ3dNAwvarl0ntDcrMpFNF7CW5eqnTi9nBcMhEftwgXqB6RJyH411GAB1NjLSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAUYrniVaE6hfievgzyAStlLm-a0GrpluAB4mG1dCH8rxaJk9nXL_ew6JRVXscOq-1Rppxmsys4tere9f142LchT_OAKzbJaWffdcg-E7CXt4EkPuLpZsDHgxXHBmkWNpWuOcia8WkDMc_FWKkvaPeTz-5fEambru9ffAHyCstWJPqFoaDMErW7uqY8eY56YtwJMkL23vrZLeM13LzKuV1LA_fzKVNbgJASVxNVv6TLyN3_25MNFshuV8z_VyWY8dM42-MiQdXBTTnWDmZdldVrhn9o4hjYZCvw6Hdq9XNcDEgwNjDdirF_TjWR3u82ECuLi9rmS9vijnpKZOGAAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=tjDSd--ejAMWk0oBv8rUYSJ_-xylLMmd3pycq6qpf_LCCT2-8e4j8E8QULsiyTEBPU0_97wUuoj6B0V-e4Vu9Cbsh8HUb1ak7lUSjR3ikcU2xrNH0TdZ4n0Or-seNWsBUr6pIwWBeSL8ORbPJbcpcNOgaw_FhcBw76H-8GCCbBWBj25y0fT49OTvG2b9KigC-8z62KqREd91ABPlw7zKb3EUpnIRpOVDBwko2rxuJJQZSOm2CiLkzz-oESimmPnT_DWtZ30ThncjhYnxBWEgYPYrhnRhgdWjVnnU6TdBYLgqINiMWcDmNVoqWOpxf2YHszYwOu16E4tjmzPc-QEzAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=tjDSd--ejAMWk0oBv8rUYSJ_-xylLMmd3pycq6qpf_LCCT2-8e4j8E8QULsiyTEBPU0_97wUuoj6B0V-e4Vu9Cbsh8HUb1ak7lUSjR3ikcU2xrNH0TdZ4n0Or-seNWsBUr6pIwWBeSL8ORbPJbcpcNOgaw_FhcBw76H-8GCCbBWBj25y0fT49OTvG2b9KigC-8z62KqREd91ABPlw7zKb3EUpnIRpOVDBwko2rxuJJQZSOm2CiLkzz-oESimmPnT_DWtZ30ThncjhYnxBWEgYPYrhnRhgdWjVnnU6TdBYLgqINiMWcDmNVoqWOpxf2YHszYwOu16E4tjmzPc-QEzAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Q8OQaEg8pezLOQxK-UGRH6voai0s8Dta3hTfX_PEb5EaFxKaRTOkNd-MkKS-GuQsr3HhHicHhtuRskMXCnttQfwRAZJZ59kmEbxxGwpZubF4VmKXF5Br1s5dRTbG-CWK823fKu3kh5PPUVmvm48CRR4s14Wawe3hAikCdfgiboNJtfF3KB_3ndMC7PmRBQjUhFSyfIbu7cXYfjncwf8qN6UOycrwZ__rox2IMB99Ub9fLIHeDxIr6SmxR4_RiL4SIcaGsCVyrNAJp5qnbaInV_VpN6Fo39sl2z0BS4okyH6MGW2cwJQvE1rI0em4qMjX_iaNjrrWE1IrIcBtg2ccjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Q8OQaEg8pezLOQxK-UGRH6voai0s8Dta3hTfX_PEb5EaFxKaRTOkNd-MkKS-GuQsr3HhHicHhtuRskMXCnttQfwRAZJZ59kmEbxxGwpZubF4VmKXF5Br1s5dRTbG-CWK823fKu3kh5PPUVmvm48CRR4s14Wawe3hAikCdfgiboNJtfF3KB_3ndMC7PmRBQjUhFSyfIbu7cXYfjncwf8qN6UOycrwZ__rox2IMB99Ub9fLIHeDxIr6SmxR4_RiL4SIcaGsCVyrNAJp5qnbaInV_VpN6Fo39sl2z0BS4okyH6MGW2cwJQvE1rI0em4qMjX_iaNjrrWE1IrIcBtg2ccjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=PYkHUjzekEXbbS5ORn50COHAosnTq1Rry0W1QPpEz7eBSZsdPrXhJObal4EnC4r9Q89ss3hEN3rvMsw1a4ZB0evbJ9OsF26FAKT82fCEEtecUiyNEE2keagem9k7CRUkeSeQTkP31KNzhWUDbHD1Z4pKoUY2aSS2GEIygkneud-LfZCL0Gawsxo8XCJ0A65CxtVFx7TYhJ5U6C7SsWrgy6llmTc3-3J6cBhlP7dKOSyQ3RvZtdA0uXKZRVmJ1X4XgZNeiFJOrUXGu7rQ2chhPqo7B7ixvADFnmGEcfyjAYunLomcaOR1hJzVnNOyb9ogdBf4thJx-RKzLVNUxCv5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=PYkHUjzekEXbbS5ORn50COHAosnTq1Rry0W1QPpEz7eBSZsdPrXhJObal4EnC4r9Q89ss3hEN3rvMsw1a4ZB0evbJ9OsF26FAKT82fCEEtecUiyNEE2keagem9k7CRUkeSeQTkP31KNzhWUDbHD1Z4pKoUY2aSS2GEIygkneud-LfZCL0Gawsxo8XCJ0A65CxtVFx7TYhJ5U6C7SsWrgy6llmTc3-3J6cBhlP7dKOSyQ3RvZtdA0uXKZRVmJ1X4XgZNeiFJOrUXGu7rQ2chhPqo7B7ixvADFnmGEcfyjAYunLomcaOR1hJzVnNOyb9ogdBf4thJx-RKzLVNUxCv5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=aYALQy292fMh3ELrcHqKIIk8fYE8opkPJ1cFQbTSHY_t9AU3whdYh7AI8M0eeocO5n7mztCRlJheFua8bnpCGEHgiTMo1bW0-nSDXenOz8WEhuCQCjHnPX0CyXl3qLOs3ZUFZ0Mb7hxHhoFlLpK4basLw_XRJLjyUczb3Ht3L0sB7CWz0DcKvhHu_elIf3omqr9Nd0Hy1vEGztUPxRlIhwiJI9xqVB3q8XRKGBM98T4YizTXFchLAvbBlrAd9lZ4pJAoDIJmNRNl7Lk4yy4-okVVfInxb3F6grNZbuWK7IBPLa4tGYCIgMTwzoxAMeYnEMsqkVs0ROc_h9noKXxxLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=aYALQy292fMh3ELrcHqKIIk8fYE8opkPJ1cFQbTSHY_t9AU3whdYh7AI8M0eeocO5n7mztCRlJheFua8bnpCGEHgiTMo1bW0-nSDXenOz8WEhuCQCjHnPX0CyXl3qLOs3ZUFZ0Mb7hxHhoFlLpK4basLw_XRJLjyUczb3Ht3L0sB7CWz0DcKvhHu_elIf3omqr9Nd0Hy1vEGztUPxRlIhwiJI9xqVB3q8XRKGBM98T4YizTXFchLAvbBlrAd9lZ4pJAoDIJmNRNl7Lk4yy4-okVVfInxb3F6grNZbuWK7IBPLa4tGYCIgMTwzoxAMeYnEMsqkVs0ROc_h9noKXxxLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6rAVMDG-LI5QJekVfWpJ-Amc7FAKh1h6lRiAAoUYlAUGFQAtHSEA2zMRaRZIJKHxXc-rGDwt5pufStyepXAM_Q_MeN0ZY22flysvUNLqSrVOGjbgVFdKSZaV4HZ185R-UVPj_moyHbi7YOdn5oSxTPaR8RWntAR3xG5LVConZ2iPCeO2RNHivsS_Y8S1Yj-60aoKPDgwBK0d2E6K-SWCf2Hma776mSwG75dtiM8MWBeZkFF4nZM_uOWIUeCdOIj2vGeVXN_7m0T9YWJZKDb_XY_iJ4U-X-u6V9xMYQKBVNgaEDNMs3iFGckp-1ciErXvzykdn1ayeTcvpX-pceLDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tDMKarbkFFfEmBnO6EvjCFKgYnKJOz5bzhJoD0QGbyJle5qt58OBXQoPxNXZmvLFNYuQxjN7x7ZXM0obPv0rqc5whEqPM61PImkkZyHEdS693zOI2aVx7bo7Mj14wXKSH4phxstFh0ix3zwUEmktb114zxse4ZMbvZcyoSsE0UARnuJgX0swHRomAG5IlodJ9jRHxwnOO40Kni7osAm2P5tmIq6LTguk6qI7RZDjPJZ2kBmWHre8_nkVIfVSs2YkBAoKCgbPAbyuC4Dt-VITdXtz4qVf_0m7efluqYIX_if-hiIkUl-Bvr2FcLu7y9BCudDRbEECf9N8H3T_S88nAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tDMKarbkFFfEmBnO6EvjCFKgYnKJOz5bzhJoD0QGbyJle5qt58OBXQoPxNXZmvLFNYuQxjN7x7ZXM0obPv0rqc5whEqPM61PImkkZyHEdS693zOI2aVx7bo7Mj14wXKSH4phxstFh0ix3zwUEmktb114zxse4ZMbvZcyoSsE0UARnuJgX0swHRomAG5IlodJ9jRHxwnOO40Kni7osAm2P5tmIq6LTguk6qI7RZDjPJZ2kBmWHre8_nkVIfVSs2YkBAoKCgbPAbyuC4Dt-VITdXtz4qVf_0m7efluqYIX_if-hiIkUl-Bvr2FcLu7y9BCudDRbEECf9N8H3T_S88nAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=hCsx5FiHDRHdoxIAYti2pTRhpkmtbWvkr05DfBN1I_c0KWi5OCVxy54zX3tcPA8eWHsHNwEz4VkJqqCwZnt3Lq1haqTAr8TPYhX5F6FtAJQDK_koHU8jTsn4_pYqtN6evSLBON-knD2rANdmUw1Byx5tqh5fe3UYoXsta4tPGtdZc2dQ27igRuJYJB7SgFJdTFvwRtVe4UJ-w_FclbGLYTlpXJKftQVddwF9ig0n6aptDBVMTm-CYh6A-oHmUw1OyBAJpLfyIRajaKcA_NhkNCgVrR68Xsy-5U3SKAcyrybBPl0saZYqzMfG1hUxmGcz_Tnf7OCe1fnUrS7FN134Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=hCsx5FiHDRHdoxIAYti2pTRhpkmtbWvkr05DfBN1I_c0KWi5OCVxy54zX3tcPA8eWHsHNwEz4VkJqqCwZnt3Lq1haqTAr8TPYhX5F6FtAJQDK_koHU8jTsn4_pYqtN6evSLBON-knD2rANdmUw1Byx5tqh5fe3UYoXsta4tPGtdZc2dQ27igRuJYJB7SgFJdTFvwRtVe4UJ-w_FclbGLYTlpXJKftQVddwF9ig0n6aptDBVMTm-CYh6A-oHmUw1OyBAJpLfyIRajaKcA_NhkNCgVrR68Xsy-5U3SKAcyrybBPl0saZYqzMfG1hUxmGcz_Tnf7OCe1fnUrS7FN134Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpPILedyezRtuq4o2QUeQYl5stKnxFKzDdxLU3e1gaxt5o8mB4VZv1XQ8Y6XAUito6eNpEdbIrEMgidDZ3R1IGaJMLvUPq3haWltZwS7lmwTLf5e9K3ny2UOM5o4fMK_kc3uYvhpvWEyl5v9uVdKj8P8dDwRWFFNNmWFyQ2aEmqSFhkeHMrphGwPPyOYUB51urQAIgtkBR44b9LzLO1yOKZxKjz1h-HjzXBcQD_UDP88LB_QhYMd0Vyl_4QSHSih9jd-Mdv8FPyTiftYrun5z2DjI5Beyor5iCxuNu6UyKwg8z76Em6AfVgDBDh8Z7t1K67a0d0MUb9hvCOg9xasfA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=a5uBWQQ-e-RRRFlGAoMotCXCYkatOWnQX-CAprRPB9pYkt2ohIwvGbXPGFP2_JoTKb4fd30jlKeaEA2BZx0UmS83um0LigOEVcx8Mq_DBAioCWMywGqf-sNrEWVjM4g3nIck9XpD0usyglQ4qi4snuSM3vzVOLfyHHh7nATR5q7sfejkoK85DYHy818HYp9DAv1LyXwqvxeFw_lBKiXO_i9NA3aIyTaedcToJ1Cm6f9w-VVva-YgyEP6o_tvjNSEwP6jbXI3DVQhabPWWHL7EqXUdvjhaRKLpKRDgNz3DzYrrGtezDXKTbh3mDaudacGo4TekCce4Wxsf-S2kt3Rsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=a5uBWQQ-e-RRRFlGAoMotCXCYkatOWnQX-CAprRPB9pYkt2ohIwvGbXPGFP2_JoTKb4fd30jlKeaEA2BZx0UmS83um0LigOEVcx8Mq_DBAioCWMywGqf-sNrEWVjM4g3nIck9XpD0usyglQ4qi4snuSM3vzVOLfyHHh7nATR5q7sfejkoK85DYHy818HYp9DAv1LyXwqvxeFw_lBKiXO_i9NA3aIyTaedcToJ1Cm6f9w-VVva-YgyEP6o_tvjNSEwP6jbXI3DVQhabPWWHL7EqXUdvjhaRKLpKRDgNz3DzYrrGtezDXKTbh3mDaudacGo4TekCce4Wxsf-S2kt3Rsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=YrV3NqDbqkzOhCYeGPOi_OIXu8tyiw4_Ah_3PCIHHf0lULZ3G_S2XPEvSbKg8VJQkvBQdf1XIVI1r-9eWTgqSwgXwJwGHOaEyoC812arddIWo6yzmZMpGlm44HxMVgmP4ImaJ5izUzC0tFbwNBnIBGpRR6IILbFXcA3rxDNS4LybNWW84zwvPTeENynmMFlILZt6_XQ7I8KGOVSWPAF5gS9a9_fRQX6f9xsIwI9eWvzWujC-_nKnrJ8Lk0bb-QTpuaTOA9G-mnhiVpD8GrUxAU4YL_JORXf4_VGwC9LlASm068uhCLO85RN4LiDEiKswQ6UR24cJOzsx0KU6x4EnjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=YrV3NqDbqkzOhCYeGPOi_OIXu8tyiw4_Ah_3PCIHHf0lULZ3G_S2XPEvSbKg8VJQkvBQdf1XIVI1r-9eWTgqSwgXwJwGHOaEyoC812arddIWo6yzmZMpGlm44HxMVgmP4ImaJ5izUzC0tFbwNBnIBGpRR6IILbFXcA3rxDNS4LybNWW84zwvPTeENynmMFlILZt6_XQ7I8KGOVSWPAF5gS9a9_fRQX6f9xsIwI9eWvzWujC-_nKnrJ8Lk0bb-QTpuaTOA9G-mnhiVpD8GrUxAU4YL_JORXf4_VGwC9LlASm068uhCLO85RN4LiDEiKswQ6UR24cJOzsx0KU6x4EnjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hx-mFT13dFC5V1v1CUcEevJgQ_jW0CJtBYRTTrNoXytie-05wJRboJddQpvixwQuK8eYVvlffwEIjQ2-b6l8y3rNfR5ADyn000ErlnJMMkaWlLTY-2RZONrAgrDxS7AAOqSVamPBtbbXIonELnATRfyhG0m-tXjdkXZuXKrmLH1NscCd9kaN2tKqb4fLMb4O72IZk0tRGwMNF8Cfr72ksLQP_MjNhqtTKuNZb-_ziYeaQ6P_991JOf18zJBgnKRZuoJ5I4XxkWaHIhSem3o5ckj_o4HuUvPXcurn2Kg-KPjiIacSA0NZewCnkEQ13dasyVzoIFXsu4QLEbBnwjyIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NS0RwqWZ4528JdAjvIB6YO_RPY8KLNeuzNDfGp9TaGnU-ncy_suOKnwLlMAWop4sow4oBhntvUSPQephnsqIbSR6kSyiuaiYXrjerLnRWcnSqkG31uydfWOZIRFt2zlEiYpzAcqWbepbx29v1DnX1iJ_1TPOp5uzlIbvrzod5cTUPIyX5wKvdnzSAmV5QcwUsgTFHGtI_OVWemjjN7Pq1lHGzjWUw17TE5w2-nV2ArXGvwsSRxjJbf9WT3Gasq2s8rNOhLepWseza3mL7dgN_cS_0jAW1KfUGTUzoA3cbytAJi2azoFjDGqsoyKPTsmIewlUeEW-TCSh75noB3UkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vho7UzA0bEz-asA9TdyDZZVN5Vl9nkqSTcRm7qAm8Ag56vQ4YA11JG1tRW3uveaJTNlXeIbtgCICqEDg-sBUxMCQn8AqeVS1TLcb1mwr3qJgKLpfBnvrM3FldAaF9hNCWvs5Gw3qs-6EbWr9IfGVbwLoAkj4eFVBsA6iETCJsESESa1OIc1AQXTa3ttSMC8JSL9dQDtk-M0uLfu7Dc1aHJ5wa_F8OrSgNUJtRXRka6VeX86tnYs9hSBF1W0_H6aQVFqSAs4v_2wBex7xxOA6ULS1DKPXdXWTrnuve-J40sddchb67o0gesUy020wxlYXDjqn8PcydFmJg9pdLMEpUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=oFpUvbdo1PjSJHercm4oPosxNEG-ZGWPMlYElfcQhW_eOWG15_NUDDqPybpPYCVKPU0nLG1iBy0PDqtk5uN-wgsVRGL-vVeCbdkONd3G81aDgTZ9ygUn05zb4EDC0mLmn5rGOLKuWm74kb53DXyL2pD1cT2bZcU8BTcs1h2DAsIN1EP5J47C4Eno45lw-LonApmOPyR-qtgqE4ta9iFj6ftvpeHW6TNL0DsSknaC6aXwCJglzpRDtljdC1As7XRdJm5oGrI-KpnrM5vufBWCEVSXz_UgSrJe0-oLWC2PE2Sfj5omXCT-SYbcjagY99_FbDuXw12M0vJB4LgZF9mbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=oFpUvbdo1PjSJHercm4oPosxNEG-ZGWPMlYElfcQhW_eOWG15_NUDDqPybpPYCVKPU0nLG1iBy0PDqtk5uN-wgsVRGL-vVeCbdkONd3G81aDgTZ9ygUn05zb4EDC0mLmn5rGOLKuWm74kb53DXyL2pD1cT2bZcU8BTcs1h2DAsIN1EP5J47C4Eno45lw-LonApmOPyR-qtgqE4ta9iFj6ftvpeHW6TNL0DsSknaC6aXwCJglzpRDtljdC1As7XRdJm5oGrI-KpnrM5vufBWCEVSXz_UgSrJe0-oLWC2PE2Sfj5omXCT-SYbcjagY99_FbDuXw12M0vJB4LgZF9mbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
