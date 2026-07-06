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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=MrIDCtJ_hUl8n29-dNFgdpD_DOI0_d-mvOVgiAadkfgbd72Mi8QkFfaHtaT6M2okQW0y9j8ajgrO0ZXBARJVjAcdD37lmon09gIzfDLfvGp_8BpB-wfusr00meALOD4ELfrQkcqVY080khSDOsJ5Lieol7LRKytWXxbsOaEqE8xgoMDsJWiQzIP6Q1udJ4Lc9yoCvR9jFaKcdo6Nd7162SiTABb744tHKZ9o-4Tf8GgTGLoC6dzwvnTr5YBvGzEqNDEKvq4qu8JA9PT7OxdCnM81Ri-hmtviuyrA-KMnj1f7njUlqqZ5oncz6ji4OUWZvbfyJ5NeMUE6TLkbHAtO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=MrIDCtJ_hUl8n29-dNFgdpD_DOI0_d-mvOVgiAadkfgbd72Mi8QkFfaHtaT6M2okQW0y9j8ajgrO0ZXBARJVjAcdD37lmon09gIzfDLfvGp_8BpB-wfusr00meALOD4ELfrQkcqVY080khSDOsJ5Lieol7LRKytWXxbsOaEqE8xgoMDsJWiQzIP6Q1udJ4Lc9yoCvR9jFaKcdo6Nd7162SiTABb744tHKZ9o-4Tf8GgTGLoC6dzwvnTr5YBvGzEqNDEKvq4qu8JA9PT7OxdCnM81Ri-hmtviuyrA-KMnj1f7njUlqqZ5oncz6ji4OUWZvbfyJ5NeMUE6TLkbHAtO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=lBnipX5BoSedK89uCoTn9Ts2_6H_f2b-v65jrJoy2FRY9VlDOAh7CO3YGivrgku_FE31fmkia2zFdBEPvL7FKVsyRcVJsTV_2aV1VvRkhNv09Qn8DbLGPiAuXbyrxq9Ln3Bz6NFeTRyN2awECEX2UzO5TmTBh0x4zVNTpfD6hGvzYXhysILT7w4YF-PMaEwT6S9ZLbGk0k3duS_6RVsS8JxziN3pnMkddd7Y_xMgtEkTyq8pme_zMMr02-Ry8H1HzvS_jXAvhyDnB0xQaeMa7zeFpDPPygJQ65c6nCMrYxMVFiSbypLRoU-yd5dh_cmSqrK_1h0teuvbRxtYoV0Evg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=lBnipX5BoSedK89uCoTn9Ts2_6H_f2b-v65jrJoy2FRY9VlDOAh7CO3YGivrgku_FE31fmkia2zFdBEPvL7FKVsyRcVJsTV_2aV1VvRkhNv09Qn8DbLGPiAuXbyrxq9Ln3Bz6NFeTRyN2awECEX2UzO5TmTBh0x4zVNTpfD6hGvzYXhysILT7w4YF-PMaEwT6S9ZLbGk0k3duS_6RVsS8JxziN3pnMkddd7Y_xMgtEkTyq8pme_zMMr02-Ry8H1HzvS_jXAvhyDnB0xQaeMa7zeFpDPPygJQ65c6nCMrYxMVFiSbypLRoU-yd5dh_cmSqrK_1h0teuvbRxtYoV0Evg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dod13zofHJLZCetnXjnD7dm_p56uCf7dQo8FMhHYVQ5ehRHrOmV0L5scd7c-5jDwx6pXmGY8hK491XkSKyVXdS06oeKPLlouL12MwWy3JtTRlsu8YNVuldlxHs0hZPbTXlsPS1LVfDIxCNXZr6-3bru50FFYndR-YukwxSWkFUrJeZnsuzSVJvzXqGqhllOLZkumYU67Hio79ipoaf0SmlbsMG9moAeAZx2AetQeBm07zk2roth87TuQS5RfsMz6t2xbJBQ6XO2ZWqb0grVNiuWQt0I3I_qAxO2nGCe83UvtpRRKEgcsrTCa_-z4O1pfq0XXcw3cNwzFf8wR27tdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1BzCRGSET3WSliuaNiGxUhjvGvzUb_x8pCEzvo4ItyYhBVaDrlsy0sNyDxP0NTNFvekh0Hnd3qU9CpmNz5RntgZXK55fAkw4alqHZuta9AHgd5Wuv9W_Ya_USVJ4gXuns-wfEndyWj_tYhMEM2RputwjCxsE_UROncKLmAPz4IvoQBKq5urElTQ6TFX6YvgQbhIJGxBliNiN12uLob3TQ8lipgsHLWIbTwaf60Dvf2OGAEcLVXHNiOUyRFNMDIHi76AxvTs_li4nEQM1tld23CGL4YXvXCs9rpRAr-WYOaeFyTfCK3HXFJMvWZIxUukJtF7u2CDS7Iyv0EVm5K36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCvhddkieiyaq3Oj8jtixm6hJESbm-mS8vrLSPrlTplHlO5m0UJ0yCE3qjudGnV_2-vF-oKJszf-InuJ51F8ykLRU26eCeMkpzLDH3XYiCK65Uu54pffu3YMOnpvveHPxMl9UjzO5rlhnmJSaVAQFPHlTKWA-g3X7S9ayZkPvL3nkeXRUed633lrDTHyP38WWhnR-1Zg6QPmn6KCAXo2K-J348-7IlinJL4laoVNM6kx27XSvCq-keHu63GTvyklPWlqKiC9TrAYP-yAXt5ZFe9nBZbfzN-o4crxpGNnd4VUZ2Ii9dh2aU0YBURnKBQqKbkegBfOgbySb4eNwvRdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up8FWFFtoB93Owub_w03o31UsVumlEyz88Jay0Hlz9ofR6w7BZVOuOqjT0F70MGv7WIXJr4ryXtNIHb--uZL0NwLgsBP9QFz7iw8JEN9q1aHahr3vF0eqBQAqwLREh0hjWkxRnabJEx6eAx9Y8NZW_uN6T8CzaZi51QMbjmusmnLSvpWtGfxiNAC04fJCWbZY7uzpc2rb5V25SX3yjD0-5SHrjmSzxLq2v1yofkRlHKxwLFQGbZr-StkSSOEmx6qAcs5ypHIhufkOzObWrUTPc8HTpdJUsAUWGMlYNFs-cReurknReupZMUsT_5Ivb6P6IaSyQEa0zMaU_V0g78fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWpSNW9pqOFfcHYYy1aeoZEwtXtQKozZwsSV2zofgtvUYSOysuI8Aoz5n3aLPkE9jOFQh5WSAJVcRSrZARQK1zW046GSEEAjEQHH0nuEl_7qcI3KNrDkaBj8g_6f9OroftxDPakhnBhZHkd53SOUoMjJ6hT08E2PsqR0sdectX_x5FEC5JmTRK-s3BpxSjOOSCxbJO8xpyNopY0Y_A0gLrf86zm-ttvNmykx2l-9xEVx_wkBQXBtGrvokdaRU5jhkmJ5LPdkIdiMomeRAOvmBL_K2Nn69_Je8iFdqajUqmfmhCx-023ndXRhSld4UJrRDZ553f64_YHc1IhtgMqnrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4Lsqv92hogr1T4ikdRRmjpYTAUmsSUW7ClJhF3YM2nL6SaN4EIWw03hZCXaUrmdDAJgwuxICIDTmoXIxB6ODTHqol842x24wFd-HS6bSzSrx1j1Zb_YEGda_jGlB3m2VBWhQZs76awpAPSxbMlfvLc401NDmDk0qZNkTk7WOt9w_HkTRCbKprZJ6OLHoUv2JgplJPYHbClnd6bN-jRT8iBBfL5sMPcpAE3-AR4AASwmsnhublbAJcQ6RTL4UILCMPBWjpoC39OQvmbJcpPTPfEMG0pTjLPpgftydyZQUIzugljghH3sF5p5_OVyfzxpfe-MXetNj5or6KIQxX1RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=bDN7Q_bQtbrPDndZ5mr3bTksGGphra7fiUObAF6eFCGCc17hlalNLNnGDX2vWXDGQ10cHOLZw5zNE56dYJl_zk_IceTcf3LT_a_DOOKSG0Kc4jPdvCKnoqqeyxgCi4k2BrhpQzmeonipBxBukx8h8zK_uQHrim7na77L3ikC_n9Mc2AyEB7eTTma9uD41m6H8przNXHNRSLm4BOSEwRJl3NrMVMYxY0modTo0tgUD_Snnsfy8zcKO4IX5TDPRwnU_1lN2QwvhkabXiIBpojtt-QTVAk1_gqG2Zw5cAnHbVFTPl7m17ZLlw_AOn_tJIROGXhusTCQAlIdUyY7kOgY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=bDN7Q_bQtbrPDndZ5mr3bTksGGphra7fiUObAF6eFCGCc17hlalNLNnGDX2vWXDGQ10cHOLZw5zNE56dYJl_zk_IceTcf3LT_a_DOOKSG0Kc4jPdvCKnoqqeyxgCi4k2BrhpQzmeonipBxBukx8h8zK_uQHrim7na77L3ikC_n9Mc2AyEB7eTTma9uD41m6H8przNXHNRSLm4BOSEwRJl3NrMVMYxY0modTo0tgUD_Snnsfy8zcKO4IX5TDPRwnU_1lN2QwvhkabXiIBpojtt-QTVAk1_gqG2Zw5cAnHbVFTPl7m17ZLlw_AOn_tJIROGXhusTCQAlIdUyY7kOgY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=VIZA8vwYW62C5qk3wGoUaoKMyO7eaqin3GcWXgtKt54lBVYBQkq73UCaCbyM81T8_zeYdDhtTyV6i3x_JvahfxuW1PbrfkMzRxlNyV5NSqT3kB82cQlojVI6HjXdBLMhtaZb18zshY5KBr4tscso_PQRwPGl_Uq-TKs252QtwVMwTjf8ufy4B-9UWXmgqbN_zCqYah2eRLoIlJlkoNu6gd43KGTo8eoDOrOrHlvy6MTiwV7pNWk8I-Wklh3mLnmzzXIpCtp_O0IlxmCe3Wxywn-b5stC2l9EVeuwRlG7AtCUpqaxOzoL33wl4HXZmy4rQVjn52pWVI_5OXn5aBtdUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=VIZA8vwYW62C5qk3wGoUaoKMyO7eaqin3GcWXgtKt54lBVYBQkq73UCaCbyM81T8_zeYdDhtTyV6i3x_JvahfxuW1PbrfkMzRxlNyV5NSqT3kB82cQlojVI6HjXdBLMhtaZb18zshY5KBr4tscso_PQRwPGl_Uq-TKs252QtwVMwTjf8ufy4B-9UWXmgqbN_zCqYah2eRLoIlJlkoNu6gd43KGTo8eoDOrOrHlvy6MTiwV7pNWk8I-Wklh3mLnmzzXIpCtp_O0IlxmCe3Wxywn-b5stC2l9EVeuwRlG7AtCUpqaxOzoL33wl4HXZmy4rQVjn52pWVI_5OXn5aBtdUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=rNGWmvEd57quOQqTUF7i96f7eESSewdj0N2ZkHCGUmbwh9PKPQIA4IuaGs-DdxD_h90Vb5S3_VOtjaW0Re2suimNFDNMNa_plzBNn7aBIBPvRu4F5cnBPjoZhbNC4v4JmTcfsNlWLdrR0Ubt_5tcILc6ktXJaKk1oiqGLbXzI-Y6H_cyADpSDhtWo4MNHKFAUsDCc-TeB97VGtWkfgDCKQGzZAUfGiVZ2evkgfV56mbff0xWD7O1PUSalRjRO1Iqz7WFZEz4H7lIC-Ssv_uCydfWUHyX-Umk6wKBCFzb-eUrSWhyGg1pjIb1Mdr--k5Eh2-p6I6V1li5lC7yTstU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=rNGWmvEd57quOQqTUF7i96f7eESSewdj0N2ZkHCGUmbwh9PKPQIA4IuaGs-DdxD_h90Vb5S3_VOtjaW0Re2suimNFDNMNa_plzBNn7aBIBPvRu4F5cnBPjoZhbNC4v4JmTcfsNlWLdrR0Ubt_5tcILc6ktXJaKk1oiqGLbXzI-Y6H_cyADpSDhtWo4MNHKFAUsDCc-TeB97VGtWkfgDCKQGzZAUfGiVZ2evkgfV56mbff0xWD7O1PUSalRjRO1Iqz7WFZEz4H7lIC-Ssv_uCydfWUHyX-Umk6wKBCFzb-eUrSWhyGg1pjIb1Mdr--k5Eh2-p6I6V1li5lC7yTstU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=QMYbdYugj2YXnPOCZfIn4DhxAs-902c2S2fNC6Ke4A5O7y4yVOl9SdShjKzX94Xf0xehYQZ0MlNwSd1cJowJAztpZghaU-tio_elEoADsBXbz3KpLlBowyORm9fPPhmQo5vVq-xhreA2GsBdOrcNgEkY6jY4vCd_kS5dxDO9Kw3npqVws27Y7lJAml0YYQXVAN6FG7xF0bz5rM8k45CGq7yjtZrquCMYPIDnWxYmCoWC4KubKlUPGLYjTmkhEJRICUl4K5Ued6lSAEObw9eUi6MZRN8w4gddtF8IiUMcJuKGrZOHFHUdqH3QyVUpf4WZpHyU0R3mCc0XhoTQ1OLXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=QMYbdYugj2YXnPOCZfIn4DhxAs-902c2S2fNC6Ke4A5O7y4yVOl9SdShjKzX94Xf0xehYQZ0MlNwSd1cJowJAztpZghaU-tio_elEoADsBXbz3KpLlBowyORm9fPPhmQo5vVq-xhreA2GsBdOrcNgEkY6jY4vCd_kS5dxDO9Kw3npqVws27Y7lJAml0YYQXVAN6FG7xF0bz5rM8k45CGq7yjtZrquCMYPIDnWxYmCoWC4KubKlUPGLYjTmkhEJRICUl4K5Ued6lSAEObw9eUi6MZRN8w4gddtF8IiUMcJuKGrZOHFHUdqH3QyVUpf4WZpHyU0R3mCc0XhoTQ1OLXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=rGrAehX2jOJIhe_rcr1LcNCnLy3saZaCqUtFYyTNNeg-AWTloboggX4qcd6iSmXjWOnLxGyVYbuxY_XxMDJG7oq9dta3CsXxBRjFYFdf0ZueWgrzwlc4VAQCAoXB9Uzqvn-6Bcw1VHUZeBxMCNJxwNeDuhXJS2KOfdL98p3jen6gWs6zNLtp7ih9d_6WYJMZfOuCZ7rvaaGg4J3wyEXH7okfXv0u_tvz9dA2l7HHqPf6Vhj31qXn1cjtIJNqMSVHT9UECGxzFM0hcgpo688GXRxU2GHJVKuclUGWcHxlwkHscQmY-ly3m-U6Z834Gf-DNZdX1R5mxiQ7RqiQ5_-xMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=rGrAehX2jOJIhe_rcr1LcNCnLy3saZaCqUtFYyTNNeg-AWTloboggX4qcd6iSmXjWOnLxGyVYbuxY_XxMDJG7oq9dta3CsXxBRjFYFdf0ZueWgrzwlc4VAQCAoXB9Uzqvn-6Bcw1VHUZeBxMCNJxwNeDuhXJS2KOfdL98p3jen6gWs6zNLtp7ih9d_6WYJMZfOuCZ7rvaaGg4J3wyEXH7okfXv0u_tvz9dA2l7HHqPf6Vhj31qXn1cjtIJNqMSVHT9UECGxzFM0hcgpo688GXRxU2GHJVKuclUGWcHxlwkHscQmY-ly3m-U6Z834Gf-DNZdX1R5mxiQ7RqiQ5_-xMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=RYK5dmLQEWBPepAKu5qPMro9WH71rUjSnySEnFfX0P5IOIxBcsHhMzl9D6BYdkKL7osMKf9XwIQ3CT-FOPjWpaZkD8L8zpPWZUypm0vmEov8ek0sMyr3OUCtmcStMucDEEQfjpANTwxoY_SxySTnmqyqrRD50x2QwaGWIL5Rtgctxp2TmGFjg9YNgpU6S88_RrBUXXNjy1wsUgTY78P7evcmE7RzCG_OKlfXA3rd6DQQuN6d25RQLoZrajr6iksXVPvkn0ekeNw56RPIfCt3cfQVGZrLrNhSC3z4lClbrXNtIlUmKWis_ByfE9OC0Q_8yyVNIou5xyTuQiBBFkYAcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=RYK5dmLQEWBPepAKu5qPMro9WH71rUjSnySEnFfX0P5IOIxBcsHhMzl9D6BYdkKL7osMKf9XwIQ3CT-FOPjWpaZkD8L8zpPWZUypm0vmEov8ek0sMyr3OUCtmcStMucDEEQfjpANTwxoY_SxySTnmqyqrRD50x2QwaGWIL5Rtgctxp2TmGFjg9YNgpU6S88_RrBUXXNjy1wsUgTY78P7evcmE7RzCG_OKlfXA3rd6DQQuN6d25RQLoZrajr6iksXVPvkn0ekeNw56RPIfCt3cfQVGZrLrNhSC3z4lClbrXNtIlUmKWis_ByfE9OC0Q_8yyVNIou5xyTuQiBBFkYAcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syfq0OP9QDjJkpk4Q_PkMesH0ZbppbIt8qVLg5poy1RBJ_LD3vTTYpYgHUX1K6zh9EGIX-5xHts-5qLdmkeZBROWBJMO3WwewBrM5vhvY4dDUWLRuFx_9nlE5dhmKQ4P2U4rFNfKQ_aG5HQc2nY9qp80ld_NmpeHfPHKpMMBL4uZIBQQAMscBFbzQ51LuSRP7JXknmA667WxQ92sbzTjw-nH4NlFbI__WLU9lyh5kNsw-7dYedBfVJsuFm3eYg4JNIsa0gTL9-dUbX4Es7220nTZzGpKoRPlzeVf0GDBTTsfxs9XWNA_i4XhoLvO3hCTNxXxdumNhNK7npzk16StCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Jonfj0adkXPb3n91oNJDqw5c6sxI2mGgswZt0w1ZoD-6EPErXdMjk_nUkbqGWblvTr6Oy4OyOpHCfyWFaeNhp793-4FqdKjHfE-fFtaYw0g9A8uGZXG_4S-4lkCkUjcnlnibHkAeEBl-uJetdMmcNWoNYkRW-w0w2FV_iP5qbbi2-a34m1KXprNqWCsUx4JnPhctJUcKbRr26Jm9P77EYJMllSaAOlNF__A93RbW45YiI29k9ucSsNKRw-x56HluArQnU8fo627G1i_VDWckmiwk_p7M3moqE5ZDTgm4_LKDtt-iLLvmOAYKqmx4e9xTPPUU4rf2R-FdhXnfF_jpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Jonfj0adkXPb3n91oNJDqw5c6sxI2mGgswZt0w1ZoD-6EPErXdMjk_nUkbqGWblvTr6Oy4OyOpHCfyWFaeNhp793-4FqdKjHfE-fFtaYw0g9A8uGZXG_4S-4lkCkUjcnlnibHkAeEBl-uJetdMmcNWoNYkRW-w0w2FV_iP5qbbi2-a34m1KXprNqWCsUx4JnPhctJUcKbRr26Jm9P77EYJMllSaAOlNF__A93RbW45YiI29k9ucSsNKRw-x56HluArQnU8fo627G1i_VDWckmiwk_p7M3moqE5ZDTgm4_LKDtt-iLLvmOAYKqmx4e9xTPPUU4rf2R-FdhXnfF_jpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=duywUlXlHeXU-oH8HtJKuhpHpQkFdfeD58uEpGIIjOGGyc_1aX5LWamOTt8pNBMSU-sbjz0CljkHPZ2B2B8MTFdlQ2SZx2mwCLn6WGEbTmasQSDziMDvcRiQftwdup4YoiOxR_EqMJU7aeHMPNtoBUl_K6izIKP7nwKRluLr5JiCKL33pc6v7EODUdSVHBaN29kce7ibz_ATl4yUJe_WbvQG-VQ4Fbwc6HvHzbbjzL7hbcJsPV-d_psinL3bfgSGhMURtbylC0y9EwCAXUuDK9Q7hwcP68L0MEAC-t1zP_XQb0p3rH36Neglrf4W1OZlIhgoX3a-7Jo9TEtB1Gi8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=duywUlXlHeXU-oH8HtJKuhpHpQkFdfeD58uEpGIIjOGGyc_1aX5LWamOTt8pNBMSU-sbjz0CljkHPZ2B2B8MTFdlQ2SZx2mwCLn6WGEbTmasQSDziMDvcRiQftwdup4YoiOxR_EqMJU7aeHMPNtoBUl_K6izIKP7nwKRluLr5JiCKL33pc6v7EODUdSVHBaN29kce7ibz_ATl4yUJe_WbvQG-VQ4Fbwc6HvHzbbjzL7hbcJsPV-d_psinL3bfgSGhMURtbylC0y9EwCAXUuDK9Q7hwcP68L0MEAC-t1zP_XQb0p3rH36Neglrf4W1OZlIhgoX3a-7Jo9TEtB1Gi8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR01kPAWq6r0Giz9tZInfKbKOmC6NJehbGfZdnHt1XdeIGaCU9SaV-gxmNnBE9LLMpSaKTmrz_RF6aa-HjQm3pJHUzWdcK73GZOyP4XH5HlyWDjopaYtkh-aZexmDI3O8-WOP8LbNwG3CbHjTj6lk5fPWKj6j0DaA3cOZPlGQiiImaKNOiaA9kNje5fiOztspViur8kBzQXeb7qhflyZHhcDvXlpjYcuxO5vlZWolLYd_IME1kZBsNdfD620ciRQln9u-AJ68b8uI_vURBvacHWSPtyDYxFQyYDhtqn32jplq5dqpaZCh9mHFhCaYOlQ85hwXOy0p5fWzhVLDtO9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBcpC3YI9HPdZgxV0XX_fiDDKu0QgRbk471oBXZys9cjnD4PC7jg3B6tqbjsSptbKLXkz5TlEoQI2yRzw6I5LzgPuYFeiguruVFTTcy96QQ934oIAGqQa5wJeh78BVLur_QjJ1YXzdKc_1o8121fj2v3oqfIG0kZrSZDxBblggkT0MPLI9I596Z3dS7KZ4VpX8W1b_fLsLzox-6U_5_3SaqlQMNw0Ep40BftQxmUVMKnnPw6G0v2rGLUgt393NtspfdiI0GyHLbbXKOdKDZ8WSCvQkxnWbYGuuW1xqEnXKcx3UhMbGwrEfC83IFdErrdgG7_7pNCiWhdavcsXx4l0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPz8CPiuboTYET09B64bnoE1FVs39KcV2-iIuSzAW3btPOwFsEgb7SI2tJ1L9MJUfUXBZfY-zKAxq78GB4TDlJhZHuVV4Yy82mV8hvIrCDEIcMbI4bJ2Rv7P0mwJd19QH_OyDp4hWX4krc65r2_haUo2sixNBPqWdakBeUDERjY7kwf5Enph-t-B1jI_kr2ukJP2y46kHskvu3QmunPfhLkDxSBDkONyH1FBL4tgi46VzfREVYx4ghDr7KidUs3iYvbiaQVsLzrHcIz9Wm8fvdiZlPeL-7jIHOfnGvwtXptg03y21Ga7Fd910dRkJB-UyjdvP_CHA_YS8SYZCBFU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuaC96eLHE2rt_c1oR5Nm5KEgYZ7rnYGk6mp71Per3jU5DmA6vmP0gY-qSxyXW1_qr8yX-CFmJJEdgrOG7rpmnpchWYcpdbN6j_lvo1AXri5Qn8aPczWZxFQgDwgnskxX9WVyZwSFB8ulXzBlyroo9XNGWu8flGGP9jZl-f2kP-GoUrjRkTTtRRCOIH-TA6ZMTO0bvtLjKxI4dT9AROXqhRGKyGhkzWKeLykKNWA3bY0A6wgI_cDI4C7mx7Jiyihu6zbFl-a6Jme0XQaBZ9dgfv02MXgzc7QO41mExzoMuwKwPcC3DbNqJzSqj6ObEJfgbJMOWshxGO-goaHckQwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxk8sFJonkKaUaw-sl5efWPunu5FX4SXzUgX-RhYZesGJC8wmlHnNF678k04qBeHo9EBTQ6DaRQlZUTWxCKgCLDoKY5xKUef-05P-bJMg2zk45MDfIZ-PQLWW3UCLMbsRR4N1rDGPNmvfTmA5Jz85BVrs1PGZ2bQKwTRPSQMq-OOM-yH301CxgL9gYb5QCdTy5WL9Q3sKBURH-KPsgNijcN334Sq5kX1APYULJQAgCthaZbQ_u1FS6p55oeayApTetSsOmF0RE3P1XLczsJ1zYRjM4Km6rwACDTBycToCE1tbudD0nQkrRASHqjyioawECqFCq8MvkOw5fifiqoK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVhD5TBCfhZHYhJ7PyM5vNsjhUA_6ddteUQkjCSjhOnsvSlD9H3abr_e6SWY7O24kCghQgRBIS9SObG1cK7TwcECCX3esRVDtSLIoZyK_gV_kCSDSGGzBuS4Bu4GbRCeixH7C1XzvUVu6K9jDVDI4GULhkjklpydmdWQJeNZRo3s3IXYcTNMkyK_ryRbu7z9p8xNZOXhMNT7D0ckq0bMr790VhYcJ2IyOhL9l-CDi6NAiIoeIh11rMjwUHUH3gUSUtNwtxixU09bvr1Tqy2S9LQJ8H--DCOvmGTEfWGF1EMbNAZ1yhkZ34BtuzeLZnoeiYFSw35SjZxgcuYJ9Nju_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M45_y-GxWDdfU-QhoPbVk3qoPgaTreaae8nX0WDDlHaO5PUUlJKDXOzMI6q_8vqOLbdsf33S1QkjwGYXL5Q52iwfm8xIdq567p7Yss6bF-mTLfs4j1_JaVe9rcBpw_CNK3x1UF-Mffi7xO8hAWq-oJ-c2xTinJgzkJfudflxMi3ULyIvQAwXH5UZMLZp-3QQJtzn5VqCVbhU3pyvf9u67wEel-sUPW5CU4vhY61O_w3VeGiAm5Oz2v22C5grCQ_NAPS48VHFGH2n2fB9gXx2V7BqwTTPnHGjDMivDR0k8r_L0SHLvMAk3SO-7Rf5ym9uVUJ6-i94sAfh80rAxGHb6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2sd6Wmk_wYrnIGXNzeLNxqUpCjaDToPx8wr_DLWwet1KaGyWaBRtlD6VqdOdTxy9QpU6m6qRv75XRHzV4lL7jJ30Xqf5NlitIg-7CpwE8268uKL6sWpiQBIhhb4KDJbQVCly6_Hpz-tnJlGAIB5WVPIKosYbbFe7QQrnrbDbMhyGINGkvnICTufuyBz5Wpqs91uIoOFjVVq2zV-x_KDxoW_DM1ghIqrGJUA5wzRDGvuLIpXASXad1mWOu0ojZMHQSdc3b2iWXxdbI7aIDgd-2PcKDAv9urekq0NswuJ2eVoimIehL728tQtfcGtgVi7kFksb7ML8XDhpBML7BoECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqlYNzRVNs2Si3J3WbKMke3yPFS3m4nWsWptWNOm2ZctGUkt7gPltyvrOztCcLF-vFMtJZfObd7vVYll9hdbxZYziVmTzjiWFTPJVYn9d-R21FxHRw1-HzyR_wgHOttH62sJlvwOl-21g3tNYeqpBM5zUC7u27GnJQIyksdQ3Eim9_yvH2AHhBbWZwaFaZTCOUUqCBLVUjq2ZGINrPGkdShqnDEdKOqftQrxVyqHYao-kAbAFGe00WVFEfX_jxhCnGR1o4qggmOsW8PaClOn5X0Vn19TrYAZNI6AMtU4KgkbJIW8ZCN_iJb32Ie_8UJt2pXDzTQge-zK2iQtBmafzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf3o8vDeHcywGXTfFHrZgbi1yNLtJ_w1Qt965vxFtQeOIDO_ZkRYQPJZX5By9lotzB3y7QvUVMgu7vDpEDqnEbnpliACTRsoS5C3D_f84BXvtMPNqDwBgCQ7IyuVAwdYfQIFlJS63fIqdgOBsT-J4w1TJE6eqspnofUmfSN-Ckp8XS1RAGvFkM947icCShIIb1tg4bYS9SHiautHckPSF1OhN5TOyJyVmR5apGg9sXi5T4AJugfOl9BSseBD7MNJ18tuH8CWj7Sl_StXmfaE8z-GUnc_n6CvU_f_f-46-7ia0xfbZk8DBK1M4eFRaBRCwaFn8hu_D7ws7e-pTB-O5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYHqyw7VAkEV1rqcIOw5L997nC8cZRhUbFE3yIXJ-ckNQYtPuQ1dApmHJn2YC3j_tmpI4xxnbwJtLhMAnAO9s05GlIIAPRNUf4dYElmoTRfHRLIFq-JzGjhpi98yo08P-2N58g68o9lVSQh_CjAKkWI45dB3Dwx6x8tMR-Ar4k13uENxE1T2_6OkC8WEwoiDdu37Frhtn7iz2pejCmyM5NbWhwPhPiWEofmi4yIFa-n3lRKMIND5onhEzu0r6sUw-xiB5D7WWYXIjALqG-h_rpWgi6GliUmdTKfi__Ed4bID46RNd6-I9PnFy0qd-Kkwgch7Bnlc2jLuXg5Oa5tRwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=D5Lu2POj8cjCqaHFxhn3geOCkOQno9msrf0kXPE2DE32Pxvib0cChYsf9iETUM2mQk5XyCeHj_wzoDwkNPrRCaFBPt1br9GMx34GL8acB8ZWEijo1HhuqPCywBbXd_TxXf5G_GN2K6uGCAYkV2unzWTLyjeXHL0UAyflAOT3CKOs09AQxvqP3_0FPUSgPcU7VnAImmnbzmGjZDRpcLMhXLXfvJQ5JWBIJ2Hpqg5KBb5odmJxzrP8Yx9fx2eKgN1-vtQdO0q0o7fSQETCp-uy8x5nme6Tt9Nl121zqe_T8u7Rzf5slgBSBwTtn34ndy7BZBCebIGiMO9EHa3E9CtH7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=D5Lu2POj8cjCqaHFxhn3geOCkOQno9msrf0kXPE2DE32Pxvib0cChYsf9iETUM2mQk5XyCeHj_wzoDwkNPrRCaFBPt1br9GMx34GL8acB8ZWEijo1HhuqPCywBbXd_TxXf5G_GN2K6uGCAYkV2unzWTLyjeXHL0UAyflAOT3CKOs09AQxvqP3_0FPUSgPcU7VnAImmnbzmGjZDRpcLMhXLXfvJQ5JWBIJ2Hpqg5KBb5odmJxzrP8Yx9fx2eKgN1-vtQdO0q0o7fSQETCp-uy8x5nme6Tt9Nl121zqe_T8u7Rzf5slgBSBwTtn34ndy7BZBCebIGiMO9EHa3E9CtH7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=BXpDu1o2hSusyzHhKVyWpH4SUENMvQ5OWEEzUeBs5qFdUFw_Sd85XSlC69fp1fGXIK3hsCzKDrdvp0HpHPClZ2OuYXoeXSJ-ek6zKMg_y-sO7GGlXPbbhI6nFpfQEFj_41tTs5yRwluxdNpA7pPsal8PvZToKsTuKvA2f1wYD2yS4Nwf5rF7cCuBMrAApqCNrNspbJvTnmGivyCeod662cpHcFNRAvQpYwotR5LvDkxTEbRCw5WD4Kett6_aO33QGclMj4fBGIjGHSA1YGx1uwB4jOULYuI7vflYbvaUzGVZYSexmntxhBxcXkwjrzwE4qjjQypx3NksRr-dTTVaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=BXpDu1o2hSusyzHhKVyWpH4SUENMvQ5OWEEzUeBs5qFdUFw_Sd85XSlC69fp1fGXIK3hsCzKDrdvp0HpHPClZ2OuYXoeXSJ-ek6zKMg_y-sO7GGlXPbbhI6nFpfQEFj_41tTs5yRwluxdNpA7pPsal8PvZToKsTuKvA2f1wYD2yS4Nwf5rF7cCuBMrAApqCNrNspbJvTnmGivyCeod662cpHcFNRAvQpYwotR5LvDkxTEbRCw5WD4Kett6_aO33QGclMj4fBGIjGHSA1YGx1uwB4jOULYuI7vflYbvaUzGVZYSexmntxhBxcXkwjrzwE4qjjQypx3NksRr-dTTVaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=W5gHmWlXrEu9IUvNiJ7QnZLI6yVuYkFGhd_enczgdzozssWyj7j_tII6pp6kEh7Icl9VIFqp1BlhT2r7bmcMlXAElmzpuM9Uk-KL3sFBvc7U7sLWyPTGtRdogZaaN90f6z-IGGzl9dPW_IO7guTNOYwUuXKB9igWlKmJncw8zheQy9RVnbhCwhTa7n_t2TiIr2sopx2CMv8wSkzcsxTB5p6IJMx2NCCemhZ1ujm2cq7VH0R52HC3pjQy05JEWkUYNDLUaTUp-vdXEF9PabzfneU5dIfAA8nEZQFTScKX6W_vJYQoozVVqAVJ3Hf8lpzudOcKvuTu779roCRwyNVCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=W5gHmWlXrEu9IUvNiJ7QnZLI6yVuYkFGhd_enczgdzozssWyj7j_tII6pp6kEh7Icl9VIFqp1BlhT2r7bmcMlXAElmzpuM9Uk-KL3sFBvc7U7sLWyPTGtRdogZaaN90f6z-IGGzl9dPW_IO7guTNOYwUuXKB9igWlKmJncw8zheQy9RVnbhCwhTa7n_t2TiIr2sopx2CMv8wSkzcsxTB5p6IJMx2NCCemhZ1ujm2cq7VH0R52HC3pjQy05JEWkUYNDLUaTUp-vdXEF9PabzfneU5dIfAA8nEZQFTScKX6W_vJYQoozVVqAVJ3Hf8lpzudOcKvuTu779roCRwyNVCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=m70LUFXeOelTYbhhYuzDccxRzN0k8471pk8np_3VsxG-v6XWnHuSesUWhbQjQYDYYROQEqJVPDsg_Ob50PhdhJsOnNQfmwXQVMFZLJGHzZ5ilsEsT2HKsxtJ1BvnBUP7fu2IboEwC4CABkqOLy-ftZJhWa-qfzoMMGxLnkh52bgG1XEJafmc8urcPxqs47MyZ5S6QQ4R_7hfkBvKEBgzRLFcZqovhNcb4ph3KUrcY57SCxhsbOl9DlU4T7sOypg_BlVvTyQ6x00CT9dLnfM-66aqRavR5Et2rA6oRrt4GOei1kJxfGVhWsnb7N7XjTWk0myMRUV7nbnVRaRWu8-sVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=m70LUFXeOelTYbhhYuzDccxRzN0k8471pk8np_3VsxG-v6XWnHuSesUWhbQjQYDYYROQEqJVPDsg_Ob50PhdhJsOnNQfmwXQVMFZLJGHzZ5ilsEsT2HKsxtJ1BvnBUP7fu2IboEwC4CABkqOLy-ftZJhWa-qfzoMMGxLnkh52bgG1XEJafmc8urcPxqs47MyZ5S6QQ4R_7hfkBvKEBgzRLFcZqovhNcb4ph3KUrcY57SCxhsbOl9DlU4T7sOypg_BlVvTyQ6x00CT9dLnfM-66aqRavR5Et2rA6oRrt4GOei1kJxfGVhWsnb7N7XjTWk0myMRUV7nbnVRaRWu8-sVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=ClC35E8L5OUNpMTJ8Kpu4s8u-CebO09HOopvMCnZB0_gTXaDqavuUckvCBIB9qdUI4O4qor5__ErW-SDjmN3QGWBPd6goIzE0kpacnoWft0Ot9GwbrH4l5u8pqaxZUPnik1qxBIdJ8QLsQMYsMWJQUx6yHR-GWAxAf1mQ7mepwTM5cPIyXQfaxvNziiKn-iMeX_-XK-_FpcupC_OQHm1IJY5EM0wEk57oiW8oNlCwuFbTVAkKlsCBQBDif-6HdER4t-wtuzUOUXOCWWwxCAk82G7OMai3No1KCbr_LndwK1HBja0ujXeUxea4fknxc7Xu5N0sZpr5z5oGltxzhPAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=ClC35E8L5OUNpMTJ8Kpu4s8u-CebO09HOopvMCnZB0_gTXaDqavuUckvCBIB9qdUI4O4qor5__ErW-SDjmN3QGWBPd6goIzE0kpacnoWft0Ot9GwbrH4l5u8pqaxZUPnik1qxBIdJ8QLsQMYsMWJQUx6yHR-GWAxAf1mQ7mepwTM5cPIyXQfaxvNziiKn-iMeX_-XK-_FpcupC_OQHm1IJY5EM0wEk57oiW8oNlCwuFbTVAkKlsCBQBDif-6HdER4t-wtuzUOUXOCWWwxCAk82G7OMai3No1KCbr_LndwK1HBja0ujXeUxea4fknxc7Xu5N0sZpr5z5oGltxzhPAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=gp64BSGEkEivim9ovTP5EKBO8mdWhNkJi8Qe1sO5KFthKlBPRDkIHhpxl5t50WsBUALIUKeKOXyXoJB9ckiA1FwJfYycAEcZHWaXOxp8FI-iSBKVDomFL9N1JmZWjkyfxowCKUKeQCeFqMtp3A2TBbwsWf2Xy9qScPUF0SkvKcRTNrCKnt56BFJBlNvzLq_SgAf9kuCe6fdQwSGr8EH4IYvwtMEkjNqSy0jrRQD9nzMChzH9OZazB-wT30Qc2RCGBuOvJkpTIjJCrdJUR6KO3ac2LEZynclspw9osmTuZ3PUgJXy0aT4gwLBlftg5H_xSdV_1F6u8uM7XvVjHaqqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=gp64BSGEkEivim9ovTP5EKBO8mdWhNkJi8Qe1sO5KFthKlBPRDkIHhpxl5t50WsBUALIUKeKOXyXoJB9ckiA1FwJfYycAEcZHWaXOxp8FI-iSBKVDomFL9N1JmZWjkyfxowCKUKeQCeFqMtp3A2TBbwsWf2Xy9qScPUF0SkvKcRTNrCKnt56BFJBlNvzLq_SgAf9kuCe6fdQwSGr8EH4IYvwtMEkjNqSy0jrRQD9nzMChzH9OZazB-wT30Qc2RCGBuOvJkpTIjJCrdJUR6KO3ac2LEZynclspw9osmTuZ3PUgJXy0aT4gwLBlftg5H_xSdV_1F6u8uM7XvVjHaqqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=JPqY-3-fd4ApbG0WDFRDiWCdt6-atZkClawc35xrLxqC-ZpTHbrak-KPB81W8euIWfP_U9l4sGoB78OIyL-xWZgmaCe1GgLmyY4b4FyJaYI9Q08foMkBcYKXURTYPlOqp4HHRuM0WhUxyjQAig5FyHBIkaTo7VggicM5HQVFOFXTezqrFyyrNAIEmnfmdlqc3WDzIHLLzryC27aMQvMqh9n5hR37hpdVa1GEw2uT6Cth6VWK_XF32VvfjAKyK2oGPm1T_NsjwhkbchiBA-gQSyzki0oqfGvz9g-tP8083dc4qbaqCVZwN1CEl8ke3BaDkDgBoYVcH_iTRcmrfkwhew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=JPqY-3-fd4ApbG0WDFRDiWCdt6-atZkClawc35xrLxqC-ZpTHbrak-KPB81W8euIWfP_U9l4sGoB78OIyL-xWZgmaCe1GgLmyY4b4FyJaYI9Q08foMkBcYKXURTYPlOqp4HHRuM0WhUxyjQAig5FyHBIkaTo7VggicM5HQVFOFXTezqrFyyrNAIEmnfmdlqc3WDzIHLLzryC27aMQvMqh9n5hR37hpdVa1GEw2uT6Cth6VWK_XF32VvfjAKyK2oGPm1T_NsjwhkbchiBA-gQSyzki0oqfGvz9g-tP8083dc4qbaqCVZwN1CEl8ke3BaDkDgBoYVcH_iTRcmrfkwhew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itpGuAf8RlpMw-bl5FFLmWNe_YkDny3co26cwkboKzRK4eGI0LDn2ccwgmr-GNUBnLXVTuB3RCGUZv6wod54ELrpOz8th1re3c4vNsvkZiTviT-dB7z-1nju__-8W_3ADzCGBjZwgBEjSVvKE3Q2X8Yfgakt9Am2yTf_r4aqfL8p-u43B1QIvL_EkccT9YpSBMUfWOlCtA19j65n9Ol8Yr6pdMrbqbP83gF22bua-_JpTmwI4_zNHKUha6Z1_tu9hfIpfersgiE4Ei5sf3ayLitcGF5PtHYqfVjX8Zbe_Ux3mCyL0CfTVREEOMQTw8BGf3q0qzp4JHK513YXPD4fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=sNLUVDUpIDI0DnLvg_9pRTkdCjf6GEKeEu76hZQ_gpkoYX4i_P7HUv5aTL7uVUQlMT8ONSmDV_-yiGOAEEeICgi9xTm3DHc_vAE1PX2PwQuE_1zg56AJTkN653mgxwmIwXXVmPN9wv4PCzc72t__S2M4_gpQJ_pYdQ0xjBagYjMcX4VTdO9nmJgfE0nyu3GdIbaTgWm5EY6K5odYZjpgIn5O-hl8NZ24rvAMvhkfgSFBNwBFVnbjuBWhrOA1UUAgU26RU42SYmxFyp0MI39b8E3yCzvW27uQM9FvD2AoVSVbUtSZl6ZThyk3kn5nfKYylX2TgpjizWMySW4KrF1ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=sNLUVDUpIDI0DnLvg_9pRTkdCjf6GEKeEu76hZQ_gpkoYX4i_P7HUv5aTL7uVUQlMT8ONSmDV_-yiGOAEEeICgi9xTm3DHc_vAE1PX2PwQuE_1zg56AJTkN653mgxwmIwXXVmPN9wv4PCzc72t__S2M4_gpQJ_pYdQ0xjBagYjMcX4VTdO9nmJgfE0nyu3GdIbaTgWm5EY6K5odYZjpgIn5O-hl8NZ24rvAMvhkfgSFBNwBFVnbjuBWhrOA1UUAgU26RU42SYmxFyp0MI39b8E3yCzvW27uQM9FvD2AoVSVbUtSZl6ZThyk3kn5nfKYylX2TgpjizWMySW4KrF1ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ePORoh0gDbu6U2zghViMS8PUbxClBPJyloKaHNduXlE0rUIPy685CkLi8Hd66zUxznLJG867xYhChdURaIs8hRMah9yzsbCnzio7qcj-_WuFMOydXL9QNI-0DXvQIoENbkkdT8uzN4wMCKpugL5MliypZWCdQJgaVOqriIh3FhhpqdyDiH6RS3nbuUidUbKRsGdrNdV-080LkMivLB2amUzclRH2014u2HG4C1mQ-yqvf241HMgBb2ERUBXQ0jzdepwRp3XFLM3CwXccf7ATGUuJmwFGZgVxNWOkYnwi6kMKSw6FRrZucXZ14V1fJed4mi-UNTtUr8Fj2gtFLWn0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ePORoh0gDbu6U2zghViMS8PUbxClBPJyloKaHNduXlE0rUIPy685CkLi8Hd66zUxznLJG867xYhChdURaIs8hRMah9yzsbCnzio7qcj-_WuFMOydXL9QNI-0DXvQIoENbkkdT8uzN4wMCKpugL5MliypZWCdQJgaVOqriIh3FhhpqdyDiH6RS3nbuUidUbKRsGdrNdV-080LkMivLB2amUzclRH2014u2HG4C1mQ-yqvf241HMgBb2ERUBXQ0jzdepwRp3XFLM3CwXccf7ATGUuJmwFGZgVxNWOkYnwi6kMKSw6FRrZucXZ14V1fJed4mi-UNTtUr8Fj2gtFLWn0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=QWWk92-V4wGTkfC6n2w2Z9m46s0Kf2-JVbeMpDnMDqNJu8t8DfEqnkSKateZRDafiRt2bd9Athcfo5qpgGpFmuiYCcRPEW-bjF2mndC8TTa8VORv0RIMHG2H61mUyl9mBItJgAVHx-akTtsaGzZDgTM-Y2xN5utaCaG0inW-RSJwMUgoBHjr2bkgC6DJWnrLatm5zVk_RNvmqxIqqaKJTm66uJw5FsutOiVXV7TDXiqaajVQRo65mMKOIb6AE4WmmEKJKna8nrRf7pvT6ZLKrQJKGFK899JEsXIIzqK9nE8cuSK3Wi11kf6mfmHKDLRX0iB_YWhNveXa7eGd9HASzlEszRuBNf5Gi1yzoOekZgw1ZfQX6bmcrgmbst7X2GXczGNlt9GRCR4bWr0-2jNLrit_tUCaTRLmPsDgHZ3a3qwkm-iiX-Gf8Ii75kuOSR7B_WtDrfA_Nb2fM2UusiVY2Ns4OtPnU2Vk7owoDvbFeLBag5yw8gnxgs2BKcizP8oB4mtcth7T_DPs29KGPlTl39kew_Jd3p0q1sR1gkl8ajXSTPKpbD9Mq0mIWHT84GSwIWOz9CuarEUE_nizS2Z-Rp2MDoDS9bCf6tVOfeV74zpHNZVyE9BoODJ3RBtZKIbK3DpTuT6btYbGEFQQ-AVch4tVUN7OL7kTgH3wuyGA3-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=QWWk92-V4wGTkfC6n2w2Z9m46s0Kf2-JVbeMpDnMDqNJu8t8DfEqnkSKateZRDafiRt2bd9Athcfo5qpgGpFmuiYCcRPEW-bjF2mndC8TTa8VORv0RIMHG2H61mUyl9mBItJgAVHx-akTtsaGzZDgTM-Y2xN5utaCaG0inW-RSJwMUgoBHjr2bkgC6DJWnrLatm5zVk_RNvmqxIqqaKJTm66uJw5FsutOiVXV7TDXiqaajVQRo65mMKOIb6AE4WmmEKJKna8nrRf7pvT6ZLKrQJKGFK899JEsXIIzqK9nE8cuSK3Wi11kf6mfmHKDLRX0iB_YWhNveXa7eGd9HASzlEszRuBNf5Gi1yzoOekZgw1ZfQX6bmcrgmbst7X2GXczGNlt9GRCR4bWr0-2jNLrit_tUCaTRLmPsDgHZ3a3qwkm-iiX-Gf8Ii75kuOSR7B_WtDrfA_Nb2fM2UusiVY2Ns4OtPnU2Vk7owoDvbFeLBag5yw8gnxgs2BKcizP8oB4mtcth7T_DPs29KGPlTl39kew_Jd3p0q1sR1gkl8ajXSTPKpbD9Mq0mIWHT84GSwIWOz9CuarEUE_nizS2Z-Rp2MDoDS9bCf6tVOfeV74zpHNZVyE9BoODJ3RBtZKIbK3DpTuT6btYbGEFQQ-AVch4tVUN7OL7kTgH3wuyGA3-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=HwqxK9gboyDhgMbUFkLUf-X8KiwskF5Vv1GpiIZ_ksTtR4lStX_6RQ5c2_8UPfrGEHSoFgYFFeI2UJmaN3oXiGH_h8ZYfBO_c_lLfFw-zf6-ugWpMmCuFrrQVmfYALfqIH-YX2gwHJx_es1y047Fec3-v9xXB3QpnZs-spgWTWQ4MJwlGfuT4A_LGEX_xupCuI72_y5zhsfH37UgqswYqWbKEw-tcponvH9y25lOC6K5oHPQn6AvO2dHHeU9Hc4w4uxTdtJThjE8-sKfVSlyPX4wui4RNVgT4VAW589fJZtpiORotIVcZr6BABqXu0Er6mCe63a17Je48CMO3-ahbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=HwqxK9gboyDhgMbUFkLUf-X8KiwskF5Vv1GpiIZ_ksTtR4lStX_6RQ5c2_8UPfrGEHSoFgYFFeI2UJmaN3oXiGH_h8ZYfBO_c_lLfFw-zf6-ugWpMmCuFrrQVmfYALfqIH-YX2gwHJx_es1y047Fec3-v9xXB3QpnZs-spgWTWQ4MJwlGfuT4A_LGEX_xupCuI72_y5zhsfH37UgqswYqWbKEw-tcponvH9y25lOC6K5oHPQn6AvO2dHHeU9Hc4w4uxTdtJThjE8-sKfVSlyPX4wui4RNVgT4VAW589fJZtpiORotIVcZr6BABqXu0Er6mCe63a17Je48CMO3-ahbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=MRuCS1gkBSHOBF3hOBc00dcQJg_MHYfD44SlXENHwDwUfg-J1RZTaJPqvlYUwK6QbxRCl2SSZxsYVV6Wf6Bzc9lzirFHo0gvpHC21FPeUW-AFqjK43q5SW-WIgF1_Hn5cNuJvInohHYEKt8rYDXfvxLYJ2SQiDTETDlc9_P9-OgKyBuqkWRJAYh_69Ena1Cfi6oy3swyzb102nbzbW03K7G6CiDc8T7Q98PuFLmreMwbNHkKbG2lPSnWcBg_wJnLdrckNtG-SoNsOGNfKLdwSbG_QEZQ4qcXNBNnDMKBVziBy3uu1-J43ThymEXzkLJowvUZKqkHsFu_uYrcbmi2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=MRuCS1gkBSHOBF3hOBc00dcQJg_MHYfD44SlXENHwDwUfg-J1RZTaJPqvlYUwK6QbxRCl2SSZxsYVV6Wf6Bzc9lzirFHo0gvpHC21FPeUW-AFqjK43q5SW-WIgF1_Hn5cNuJvInohHYEKt8rYDXfvxLYJ2SQiDTETDlc9_P9-OgKyBuqkWRJAYh_69Ena1Cfi6oy3swyzb102nbzbW03K7G6CiDc8T7Q98PuFLmreMwbNHkKbG2lPSnWcBg_wJnLdrckNtG-SoNsOGNfKLdwSbG_QEZQ4qcXNBNnDMKBVziBy3uu1-J43ThymEXzkLJowvUZKqkHsFu_uYrcbmi2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VInpTTdMvF2ul6RiOjJhnwQi6z2RZtHdWn2dZqCa5oS_CEMn9o-fKmXgI4KTTI5HhCuzN79vcrfjAsaFry5rXQBtncNiPJqAdAhUlIRMPtMFejawU4h1uS30U88I37NIUNHjvjOOMVAtLcrinCKOjCHcIxq8U2C_Zay-20Jfm98BYJvFm13BEHA4NZTyYcOgS_HQ0MII1YqTFEiXSCE_VmxlGWDMthY2a3FC1_0OHr5qMUJBbNQw8qmeeLkpx6XgA8B0a7fCP-5592zdUr8LbvR_piSjNIStveXgLKu5i3yGKJQGfPv5xhYU6-REnF90i_xIc6ihnQ_rfuojS4S6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5OH6vCeKp4H-VrQhozhwpw0vykMD6mg7KG6Oykqtt1CbAMt13Kjgn8-49P_lxmpuLVYV9B5oLegGq0Fh1M7a24b4aGzbLgauLCjucJYqnMS-j8aHsvuTyHuDxVt-K-ToFfF0vd2fKbk5MeXUDhTQL1-Cw686ZeFJQE8xcpM1uZlmhtsFwtcy4f8lxy9BMsXioA8wqBw6onIl_Eakwt1EO9N8cl5NpVLuTS8Yt0xEy4o5gLS2fOcq2m2UwB6L0CYgjBlny55QNbSl0DwrCCxmR1kgTOO6_AgOaok-8VZPXchQaTfZPiKplv362VhbKy8u2VBfc71A6Lla8hdOIkBaQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=alPnXuzJn3cTPKLBhc2tHzyGgf3qnN4zxE8VZuJ366E-_yHKm83lkYaEp29ZSflnrYHGh5rXjsCKg5QbvW0sS0ZYq-vAGuGNFmZTwml_7qBd72l3OfwQYsAd-A-Ywoz1pg_c16KmdoboSuxqQtgmJ7_ayN3avaAL649Q7pMZrHv1pKLWkHSsU8a18ifMDAfNex9cwCkkXEcDc8RnututIwieOV6HV-p-rpXocfsi4ONSB8ejWu1hxE1Ms-0PfN732-70DrPSPAZJNFQnBULkZK9LBkUm4WJJfgAjty7kppgZu-fX2jHPsvC_TPCMqxmmuzAGRVYq-JXjTSqXIvktbU4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=alPnXuzJn3cTPKLBhc2tHzyGgf3qnN4zxE8VZuJ366E-_yHKm83lkYaEp29ZSflnrYHGh5rXjsCKg5QbvW0sS0ZYq-vAGuGNFmZTwml_7qBd72l3OfwQYsAd-A-Ywoz1pg_c16KmdoboSuxqQtgmJ7_ayN3avaAL649Q7pMZrHv1pKLWkHSsU8a18ifMDAfNex9cwCkkXEcDc8RnututIwieOV6HV-p-rpXocfsi4ONSB8ejWu1hxE1Ms-0PfN732-70DrPSPAZJNFQnBULkZK9LBkUm4WJJfgAjty7kppgZu-fX2jHPsvC_TPCMqxmmuzAGRVYq-JXjTSqXIvktbU4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Ydv48YnHQCZ60hTcfiao6GxBbRWiny4Rzr9RWWPkYyxrDX7cpjzCjMVbvEC1Sd5F4qmczDPsWs6eggZfH8NvP-_TXyqBTrMB7UJS3-c3uN4qoDTiJIV6KPJJXUFcbTtBWSlwAFrxTTpUyOYAMivd4vAMA8pdgc940oInUgErwGoPMdCBxU1Y1_txSVQaUAaSx4zUMwtn6RiVUveO0_cRovy-jvBByjmQb3yMo38RNI9v5yxNHjPI_WpRfyj_HFkbK6o4UJfNVPo5tzfZxEUCZy-BkHI0cDHwhInXXi9a2wkIlfgpRqRrsQMTQoLcCiPvE0qRATTUwuAurC1qENDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISaOJ8NoJqPxA2EPdYioDpnhvfKcElLp2EESJLc82Wn88kLzfJopOriiqUHfvPtP7AFAgRPZXrSE35PjO-MJbiTkLWObMuV81sMAUjILWnYXCJ2fdQC-lCbWeaQHUeuH8e-W151V_zxN_wXcDTHJEfjTE1q4Kx_aKUrq9WVEXjM6K4vGpG9QuCQQHArhn1_U7lq92nj5Cyz4OTxImc3fLqoT4gS49EJVtGbH6pO6XWr3xkIEwPjSm-EyXyTZegYk3K-M539mg4Qy3PLTwLD984ghckiyySmqmA37gMdJq84X3SfJteT3Agfmae4hkg2jfkuMr2JOP7LGQXztOG5i4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPUJ1uqMsr5P0hM1g6QvTZD3-nMLMri32zUAIHrJdIxmYaUv4SS2XvSNyFnRv9PBMSTdPqtNOF3CdBnBNhTQlX-oAiQomZcboG5jZ3vQIfpaKlE4FarR8Q7XjCxez-vfDMBnFrLluJJYN5IpGYeCPrzPLP7R63-jcViMgLiW0PimEh-bIJNI5h2yxNYAKJnPg-7VZT2FUi_DIBceixINcB0VruBwIrD6oE27Rcnz-413zCOh_CCmZwlRhWp1ECk4-rsJ7X1d5jfAF7BM_IW5Wk_Rls0XeS_MsxzY-EQuN42Y_6zkBcyytA91DjASZy1OrBQlNDY4p4LIakxJ2ed9Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmLHMX9yEe9Eko-lt1shVa5AM9e3a0tTHrKTLcOe01AyFz3PbAur0TxTRDwvhZlPQe38A8CF51daqDK2k1YAa-wLjBTGsX7UM49qznYIIYNwBP2lMrIESXhklmo86MYa99yfRwGnt19qi9AXurxSURATmvgR4LrJeILguXLshJ797qrg1wIl8pYczA5-UiifLJo40fRdsMD7GKTygpHZTZy9dWuVEBG3GsY6T4cEh00roqPQ2W7E1DXs42-wsSUe4E9Ftzb98scqvOHy2iiyOwRgikMT_yD2oVQxkpUIDkmjkqVW3UVevBSTpYHwxjKGBmVYFOMcCS7Y5-URHXA40w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=lbiLhxPMLHMz0WrZy4VmqX7uV9roH5WwqKpwS3ONiYS2vH9Z1ZCg8GbzIr84dhwTfljRlfRTUi0DKcniFLoPnLqu082FI9XeLHeif-9pHeWq9GQVciAAGDYURgG5uW3DZaQ5P8gqtZOP50g9FOWS8i_QW2xeVn-hdhe7FgjxkuylCPM9dp98cMSHusAcTlkn1p7StMF466sf1MmOoTDl5-pzpjMA-1dg9M9R14j0abjxVsoWuQiXdjgGnhY7zjHZnSsSG7GPvRvLGeTnOVQpQE_wDq2ENZ3FxP2rBGzTbHU_D_dwVLx83bcA5al2AVBKPKODH8luxIUEhhNe-qzbWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=lbiLhxPMLHMz0WrZy4VmqX7uV9roH5WwqKpwS3ONiYS2vH9Z1ZCg8GbzIr84dhwTfljRlfRTUi0DKcniFLoPnLqu082FI9XeLHeif-9pHeWq9GQVciAAGDYURgG5uW3DZaQ5P8gqtZOP50g9FOWS8i_QW2xeVn-hdhe7FgjxkuylCPM9dp98cMSHusAcTlkn1p7StMF466sf1MmOoTDl5-pzpjMA-1dg9M9R14j0abjxVsoWuQiXdjgGnhY7zjHZnSsSG7GPvRvLGeTnOVQpQE_wDq2ENZ3FxP2rBGzTbHU_D_dwVLx83bcA5al2AVBKPKODH8luxIUEhhNe-qzbWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QghfIo7VfnoyApxU0YUDqmXfcsQn5-rotn_9bni6zM-l5EhftUvqm6nFpOPUcKOQHmGs-CW1EoDbW8jDG9U_SOQ26-W-7d25yp0ukTvszQf7LgLJebjY0L85kbsm2Ke_IXN6feb9c0zFgOVji2IEPcU2I_qg5kFUwKJ1na7Yt_RWtMdYW13jZvDWH0Nco891lB75rueWHNHd5ayPMXH5u_ZndS3xYWRUbDsk2MFJ91y17AHRfqXC7Zx0sdH-PLRvnCLO7asEaR9hQelYDbr-rRZS126gDZyKLEu1cih_5hAAEbYXROYhgDRyHqlC82YoeKdiqoXOWxfrKyqu6558-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QghfIo7VfnoyApxU0YUDqmXfcsQn5-rotn_9bni6zM-l5EhftUvqm6nFpOPUcKOQHmGs-CW1EoDbW8jDG9U_SOQ26-W-7d25yp0ukTvszQf7LgLJebjY0L85kbsm2Ke_IXN6feb9c0zFgOVji2IEPcU2I_qg5kFUwKJ1na7Yt_RWtMdYW13jZvDWH0Nco891lB75rueWHNHd5ayPMXH5u_ZndS3xYWRUbDsk2MFJ91y17AHRfqXC7Zx0sdH-PLRvnCLO7asEaR9hQelYDbr-rRZS126gDZyKLEu1cih_5hAAEbYXROYhgDRyHqlC82YoeKdiqoXOWxfrKyqu6558-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3c8tugGEODvYxijukqxyR5Yky4W6x2wnLoVvw7demmnTFTk454VbQt2hbHBU6LMzlDi307KMTkHCrbyU-7FNi4Qy9ELviwO0XWP3mCO4TOiFWr4iv2Tb5JzQNX9DX404jlI9gF01ounINsVlCROVz2q9XmfFNxD2wh5rHimXHoq8SrCnCnmE6GhlM2fFjPYpAp_tOwNWx98Z51HEZ6m9aOmWiipyElWzkyhkvbEVZhsBpL0QgeLjYnw3A52JrgBMPpZ9Qbt3piUWBPVWn0qy06mfZLuaJyE4PaCexkCwua5YbD-5E1c73v76m9llcInak93SBu5pyjdepAHGePosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ho6MLOsBZszkdqkT8dR6GVHRCBZtg-VHbNQPnOjS_hGmj86OZQ-S9ezdulp86jzjKezG6bRC2BEmiUZmtlvrfoUScz0IX84pyerqTWmxv5bFtKk0N3gGAYETy8fy8c-e_tQdPxD8b29U62nLA5Qhuhjk__xQ8nQWZMlRPKDPMHqjeIfaoPNJ4fGD9AGqXXGrMhg6fk9OFUYW91Dx5GPZA9Er48obIPphCoN7ZlwAJ_hZgvxIb5C_RYYby4Ajk-pVNTXl1uH7l4swA6CofOOrtr-UFv8r2lK807xJ0axBo0G2fGQfnecSnjpAxDVJy2v4jYeE-P08bcWE3GfDOtqJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ho6MLOsBZszkdqkT8dR6GVHRCBZtg-VHbNQPnOjS_hGmj86OZQ-S9ezdulp86jzjKezG6bRC2BEmiUZmtlvrfoUScz0IX84pyerqTWmxv5bFtKk0N3gGAYETy8fy8c-e_tQdPxD8b29U62nLA5Qhuhjk__xQ8nQWZMlRPKDPMHqjeIfaoPNJ4fGD9AGqXXGrMhg6fk9OFUYW91Dx5GPZA9Er48obIPphCoN7ZlwAJ_hZgvxIb5C_RYYby4Ajk-pVNTXl1uH7l4swA6CofOOrtr-UFv8r2lK807xJ0axBo0G2fGQfnecSnjpAxDVJy2v4jYeE-P08bcWE3GfDOtqJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=n1w95PVqUw-CbgT6CZ-auVM83SdKaYtD0mfR_PMC4TqbhRnf2bT8gvJaD5DMKxuMtY-TMskJmPPzJ3HJeIeiKGt3GoL7GBZXU-i6Zca2-Dmywp32IXrlqZVhRYFK5KS8-PZc_NvoPYLHZdmE4qGA82Zg17C9LWCYPxM_g00RF-LO33MC95tLkLu_cIrGiOgkfQ1WVmvmlIQMotmboevu3yM249hbSJkJXIbpA1z_0Q3ehz5-NoijMA6StoXEywlvaonmQ3Wv6j4e3k5LLC4RizQIUXlDy8YZ1fUQ0sX4m2KPN-LkjMt-O8O-FAkIaW_UZreyx_C-f919nm8g4uxjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=n1w95PVqUw-CbgT6CZ-auVM83SdKaYtD0mfR_PMC4TqbhRnf2bT8gvJaD5DMKxuMtY-TMskJmPPzJ3HJeIeiKGt3GoL7GBZXU-i6Zca2-Dmywp32IXrlqZVhRYFK5KS8-PZc_NvoPYLHZdmE4qGA82Zg17C9LWCYPxM_g00RF-LO33MC95tLkLu_cIrGiOgkfQ1WVmvmlIQMotmboevu3yM249hbSJkJXIbpA1z_0Q3ehz5-NoijMA6StoXEywlvaonmQ3Wv6j4e3k5LLC4RizQIUXlDy8YZ1fUQ0sX4m2KPN-LkjMt-O8O-FAkIaW_UZreyx_C-f919nm8g4uxjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=m_RpAXdXrnl-iQUPbGxImvv9NvzYliYMGKrBvKnjrjXuRatm5OLhw3t1LpH0dpHmwfSCgxY3G4zMzztsiUbbqP1cS4s_Or5reoAsUv4lKwFYRMmr0ru-O3TF9KNNBCZnNAl1FoTzERL3Rvox5XUEL5kZoAA1r7V7UxylvPT259vfZ_kM0GbD67qY0FHo2nsoOBdxxRV_bY4YjhtnD74dVYVeofIlwmdw_yNtx9JYUXEd8v34YMrnfyYbz-7TF6Ac6Y4c-TX_jomyZxxl9WL5v08vDIh7BzWAkNjwVbDb9yQ57IwDMDNutRSVpLhC92x33T0zd2AALkLVxzjqj5cGmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=m_RpAXdXrnl-iQUPbGxImvv9NvzYliYMGKrBvKnjrjXuRatm5OLhw3t1LpH0dpHmwfSCgxY3G4zMzztsiUbbqP1cS4s_Or5reoAsUv4lKwFYRMmr0ru-O3TF9KNNBCZnNAl1FoTzERL3Rvox5XUEL5kZoAA1r7V7UxylvPT259vfZ_kM0GbD67qY0FHo2nsoOBdxxRV_bY4YjhtnD74dVYVeofIlwmdw_yNtx9JYUXEd8v34YMrnfyYbz-7TF6Ac6Y4c-TX_jomyZxxl9WL5v08vDIh7BzWAkNjwVbDb9yQ57IwDMDNutRSVpLhC92x33T0zd2AALkLVxzjqj5cGmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibJnkQXgAWxC-ylmyvKIC-ShO0vLTot8MIJkX_5bs7emDKNRSWnOer-4Y8g-DMb1xNLAsVyl2BFyD_QWJ31PoRtY9X1BPV23ZSqjCCTWUUBYpQLLrUeuumCiwVwoOTbD9NTUoU62eAHc0u3jZVii4qF99TMZT5U-gl-D_ukIevtiAq-zPshSaWMiRC2DLJRAx0TV3VmeJPaQ9h9WEb9Q9p7sd-4iKww_pXEGqba5HyZeJnjLW-lA6WL4jBhwKiMEl46AP99Txv3DCjSVgN0ehgWgo1BGduQQesMUygucjmemUx0LwroU9qiEv7_qLAoKwi_jVYXsIcbDFtcKg6tLRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=u6De-1ISqEeRrZVI_P5Jm3zYX2g422egBelD0AHyxQe5iRSZctuQ8N6D4D7z2FNbMyLBkd35n6I8wCyjD6_3D92arWvfJVqg5d5uDqd2Cx71-VilBJVA0ZHLCT2sDqB4UCaT_HxfukV24b6pZCHkZNk9cLDQX_dTnvBRTRomcsI09ck9qS0MrQd4cgxLbpURLmC4QpsyxgFWwas_31c0JvjkZlwgPL1h4hzDBi0par9sljUbVEgo7kz_5xVjFAL6fNG_VaHODD0NhozPiyjKPNHJtIqcVnBstA3jmcqnhAvVtr8JaZpGcuGB5YzvFekPn3QmWQDLDsgz7fI1R4I8Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=u6De-1ISqEeRrZVI_P5Jm3zYX2g422egBelD0AHyxQe5iRSZctuQ8N6D4D7z2FNbMyLBkd35n6I8wCyjD6_3D92arWvfJVqg5d5uDqd2Cx71-VilBJVA0ZHLCT2sDqB4UCaT_HxfukV24b6pZCHkZNk9cLDQX_dTnvBRTRomcsI09ck9qS0MrQd4cgxLbpURLmC4QpsyxgFWwas_31c0JvjkZlwgPL1h4hzDBi0par9sljUbVEgo7kz_5xVjFAL6fNG_VaHODD0NhozPiyjKPNHJtIqcVnBstA3jmcqnhAvVtr8JaZpGcuGB5YzvFekPn3QmWQDLDsgz7fI1R4I8Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo9G9OZVujGxIWSgSzNfX6zirau3SwZbGxID5vqCHuJtZNowdX9kaIlCRPrPwxIE4bW-xRRUfMdxdRJWOu6imyvFlD1jp3fZSV7ZWSTljjsoiol8QecUVh1Uh_4Mlg1HwjgqVJRd1mzSE_Nyy9B5e80joFxoP7jilkAwgtEdN4iVepnMVmNDX54465sYMR1GIqHFUaHD4IZ1ybWpEJoJbbycfLo3-lyLI5SdyoqgFpigo5ysqB-Pk2w3O0MtaPiPM66R2i3WMYHqkNLUP10fx7TlA57wyUkNtCIviZZi7245wGeblUT87GmwSV5kfzCeDsPQ_uW4bJsXbgY1UBmHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZQZA_Yz6kzEeMykT1SQz60TXCg4D0a8ZzWQQZgsJse4dMHSOU-Wgofi922McIRa2NhnBMpKcNaCBq4ONjngNGKisXSZcGXH10RBwUpjzI9oor2uWWQwWBCfPm8lGgIzJ5d2swUt7aSct1AE_wU5w3p2xfZugO1EvO7pBwiDazUvcd7IzS9PCDNomd-HxWnkZfQxtWmubpLGbY4e6cne68H8AlkIMK-Nl43kUzvCrInA-FgBOGTmfAMv6fFoexdAi3A6aP5web7uwIGuk4sSRq0gqzRaG-a6kM-jZ9L_lEwKR7KJBswHsO03U2VBZj7YWpyUFhHR--9rmM92zTdTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=blQV0kxOeGUmDTZJK1AqpwuIHy3IURtsdHhTBXV0WbDCwVv3TLHYNNfYfQl2qN7-IqWcLzOIfwjIXTC-MjE5uGA3qHEUUT75L7kvhkpE7a6_NwSaPRuKG3ugN_ZKbjcrrDJjyEHqguPLEpJ7DpxTsyuygEVYwFJjVWnWY9GIAIvQ9VwyoM2yA6E_m8aBK-oBRUb2sZq-21J5i1jeUZP8rFYTtB0c4gXu1zy616hmfW0Izc6SD12lvWR67EIo2K1xyJOPyWek1l_eqBLI50S7aav9sFpN_MjhV3uxBpnMzR7ShxRBlkckI39OCjR60VUA6sgu0_dhlvLcf_ieVOmIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=blQV0kxOeGUmDTZJK1AqpwuIHy3IURtsdHhTBXV0WbDCwVv3TLHYNNfYfQl2qN7-IqWcLzOIfwjIXTC-MjE5uGA3qHEUUT75L7kvhkpE7a6_NwSaPRuKG3ugN_ZKbjcrrDJjyEHqguPLEpJ7DpxTsyuygEVYwFJjVWnWY9GIAIvQ9VwyoM2yA6E_m8aBK-oBRUb2sZq-21J5i1jeUZP8rFYTtB0c4gXu1zy616hmfW0Izc6SD12lvWR67EIo2K1xyJOPyWek1l_eqBLI50S7aav9sFpN_MjhV3uxBpnMzR7ShxRBlkckI39OCjR60VUA6sgu0_dhlvLcf_ieVOmIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0qtIL2vroVqO7ugs1HwiZ3l-fot0DUYhuC7UCc2Qsix3I_jrW2fisOnt4BrBcWELbhs5-C0iujrk60qg-9N04ATJw9USryh8jgpzWmLXV0WWvPAtLswJEy8bl7WoWtgiOmcYXUu7PvZyx9znT7pYltIJsc5iFIJhYi-vxnAoCc6XAJ5Opp2dndd-X5EzojBZ4ovC8z0rt3EA6TXSiv7UDWVDsrFoRe69Dz3zmVNdxH4_BaRk98UWOHh3trmcrPwwWXsu-D4sadxUflmGJau7QYc1OmQ-waS3m0Ogov9d37DxYtxHmbNbkYV0GG7ztDCyCNI2nAQc7qWg9ftp0THqdvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0qtIL2vroVqO7ugs1HwiZ3l-fot0DUYhuC7UCc2Qsix3I_jrW2fisOnt4BrBcWELbhs5-C0iujrk60qg-9N04ATJw9USryh8jgpzWmLXV0WWvPAtLswJEy8bl7WoWtgiOmcYXUu7PvZyx9znT7pYltIJsc5iFIJhYi-vxnAoCc6XAJ5Opp2dndd-X5EzojBZ4ovC8z0rt3EA6TXSiv7UDWVDsrFoRe69Dz3zmVNdxH4_BaRk98UWOHh3trmcrPwwWXsu-D4sadxUflmGJau7QYc1OmQ-waS3m0Ogov9d37DxYtxHmbNbkYV0GG7ztDCyCNI2nAQc7qWg9ftp0THqdvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=VZTs_wPn_HOJ3LOK2LWjU5faNE4N26r4kt-xDyqE6JmACXeer05bc7TQ8XJLzB1laddyzP1u_w7cy1WK9Udl0a0EwKruk_lGfUjXzkeYwyqwc0qFg6CI03TFmB0ETB-MCD4U79nh0P9wfCVApvK1GJHAKDJ5R5N8oHPGcJG27ayDjodThchjcGs42rVtKj-4bxr3bUAuzq0rDh43-twQPKnqxYIW2ZKFjrb9XZqdeHyLktBZkVtQ8Uc1JLbxgQ_Kr-HvgQoR4P82-HKHCH6VpFvYgdK8eqdlUWRgTOD7ubadCHUFtZVNb2VcJySEulak1F_ora2T8oYgyjlk5gIyXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=VZTs_wPn_HOJ3LOK2LWjU5faNE4N26r4kt-xDyqE6JmACXeer05bc7TQ8XJLzB1laddyzP1u_w7cy1WK9Udl0a0EwKruk_lGfUjXzkeYwyqwc0qFg6CI03TFmB0ETB-MCD4U79nh0P9wfCVApvK1GJHAKDJ5R5N8oHPGcJG27ayDjodThchjcGs42rVtKj-4bxr3bUAuzq0rDh43-twQPKnqxYIW2ZKFjrb9XZqdeHyLktBZkVtQ8Uc1JLbxgQ_Kr-HvgQoR4P82-HKHCH6VpFvYgdK8eqdlUWRgTOD7ubadCHUFtZVNb2VcJySEulak1F_ora2T8oYgyjlk5gIyXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIJ5H17zTDQMC8bTSjTuXKCtpzjk4arvcocd7SSP-cluq1arKQw0q7Q3GaPfJsIa6oe5VbJfjFnzz23RydhTubkb1uzyeD__qv0WAdreaNd350hTJTuoyY8JjtLwolFb4hbGx22OtXwvlGIoS2iqo6APYCuNzo7GG3L5eJXHaGH8qMwexOxFg0QQd8KfqHvFpsFQVt7YuRZ04wSkgFz8BoM4C0ED3e-Z6_U2ZZROSX7rci_JiWuIlcx8LJ55CJQYxohuBJL9XRTbXdZdaxJSg_mqorEnSMliNM9hwrHiMVmBSTO8lOvTkmqD392ybcPgtdciIKWdfsnOsJ_4uMGj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Mp8XEu5-F1EH4Ijyf0t8r9XQ1GnWUGc9bYhUU8r97IvFEwbzCK36Ufv5TmZE5biF4qAGS5otc_fugVMn_H1hzgzDjBrekCpBkj03Is6M1zWuxRd1NyBbOWbVnZNrv64034RQdj6i8OYK7zDpE_JRaxqnthS3mRlJEoNku2Wy7qSv2xsAFy-31odJZfLJ9kZERPV-YaqV_ncvIrD-Iev00xALBo9GIwF2NCIfGUBBM2wO6M38oTlC9zVbwQ7qArXCJqa0AHHQP_Ixwy7bPl7J9ckaRo8GbLCezfjRM9Yv8WJ9d32JBuMvsJUaeYjwWIWMKVRCPdt_SJL-olThXUzcGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Mp8XEu5-F1EH4Ijyf0t8r9XQ1GnWUGc9bYhUU8r97IvFEwbzCK36Ufv5TmZE5biF4qAGS5otc_fugVMn_H1hzgzDjBrekCpBkj03Is6M1zWuxRd1NyBbOWbVnZNrv64034RQdj6i8OYK7zDpE_JRaxqnthS3mRlJEoNku2Wy7qSv2xsAFy-31odJZfLJ9kZERPV-YaqV_ncvIrD-Iev00xALBo9GIwF2NCIfGUBBM2wO6M38oTlC9zVbwQ7qArXCJqa0AHHQP_Ixwy7bPl7J9ckaRo8GbLCezfjRM9Yv8WJ9d32JBuMvsJUaeYjwWIWMKVRCPdt_SJL-olThXUzcGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=aW4dP0UR3J4MAmYL93N5wknisWMH6jZT8qx1EjKh8SBCnwM2RgZnDN-eBh7SCUGX_B8_WeRy9wwT84L0-VYEen_Qpx9GgUIwI3IDaC6HquSplM9aSDIhEKRZt-HvfHW3a_0ynadnMRQSWIOWbSxJwlXeF8Nf-iZfIyVMC5p_u2ioMmuFn9gDWRCZOs2CfC2Q2NdOT2svM5eJsp6VAKffHli6AL6wbixUsg9sZwY4WF3ep1tal8D7B6YwwzyCcbQ7P_G3dZPU6EHy52Lz6yaw06PDWW_VgtZxwUSGeaKhvDRoMtk7yFwFWoPRTIFCa6VacRmCFv3pitCj2XbTLJka2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=aW4dP0UR3J4MAmYL93N5wknisWMH6jZT8qx1EjKh8SBCnwM2RgZnDN-eBh7SCUGX_B8_WeRy9wwT84L0-VYEen_Qpx9GgUIwI3IDaC6HquSplM9aSDIhEKRZt-HvfHW3a_0ynadnMRQSWIOWbSxJwlXeF8Nf-iZfIyVMC5p_u2ioMmuFn9gDWRCZOs2CfC2Q2NdOT2svM5eJsp6VAKffHli6AL6wbixUsg9sZwY4WF3ep1tal8D7B6YwwzyCcbQ7P_G3dZPU6EHy52Lz6yaw06PDWW_VgtZxwUSGeaKhvDRoMtk7yFwFWoPRTIFCa6VacRmCFv3pitCj2XbTLJka2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=mlqb1s7sRA2TdXfiI5k-4OEEmk4y9Des3CZvds2SZvX0FrTX0j2_flJ2ntZd1POo_BmyLj_lTnwRg_IEckdyURA2rDEY5TJ_z6Rocz2n5RzzovLGHjdsrzRCCknE5812Xo6frjzN_HCRQsSghsLhM6xUy3cPWmIanXC2c-HjrB0Roap6DsLSYqfTiGH5k5dCfdntVA8nt62_Yz56nqTq6wjpdnlznSU81wbrrhCzS7Etrg_sxH_XxSn7VINZovqqU5GSSMlpGFE9tJhWz_I4BsW7KcuIucm46s1pS0TTJUh15_IURtrv-Ayl9jHKp1CCwm3zwDpY_qJaEj8r_lKPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=mlqb1s7sRA2TdXfiI5k-4OEEmk4y9Des3CZvds2SZvX0FrTX0j2_flJ2ntZd1POo_BmyLj_lTnwRg_IEckdyURA2rDEY5TJ_z6Rocz2n5RzzovLGHjdsrzRCCknE5812Xo6frjzN_HCRQsSghsLhM6xUy3cPWmIanXC2c-HjrB0Roap6DsLSYqfTiGH5k5dCfdntVA8nt62_Yz56nqTq6wjpdnlznSU81wbrrhCzS7Etrg_sxH_XxSn7VINZovqqU5GSSMlpGFE9tJhWz_I4BsW7KcuIucm46s1pS0TTJUh15_IURtrv-Ayl9jHKp1CCwm3zwDpY_qJaEj8r_lKPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Q-QkgMawHCiwdrvOiCM0h16O2lWD7sy6O7WK41ULhNgfOWOC2vIXg9UjCb7auc99duSSpE9FDssGTUnBAWRMt-OYg7mNT4xWLQwkzCL1ZVqzW_l8sxa9-Ulr9Bt4C4sUE6HO933l3gdks4efqxoI5D_iSxz-tjBqlYMTIEWiS6xwUs4CTCaJT2_zr_FUchSiQ9iz4XSggwWBSQWm3zuiv_uZd4qXm0ejsbbGd02s-0vOuWdjlv3aTON_VSpXy7vSKEbx83HEofOMN2e7uuhITOKdZGUiUvxOEx_FD7AOEhVTAlp3gETTo-1FX9nBJ3MN3T00dithTxkhVLc6Ca3atQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Q-QkgMawHCiwdrvOiCM0h16O2lWD7sy6O7WK41ULhNgfOWOC2vIXg9UjCb7auc99duSSpE9FDssGTUnBAWRMt-OYg7mNT4xWLQwkzCL1ZVqzW_l8sxa9-Ulr9Bt4C4sUE6HO933l3gdks4efqxoI5D_iSxz-tjBqlYMTIEWiS6xwUs4CTCaJT2_zr_FUchSiQ9iz4XSggwWBSQWm3zuiv_uZd4qXm0ejsbbGd02s-0vOuWdjlv3aTON_VSpXy7vSKEbx83HEofOMN2e7uuhITOKdZGUiUvxOEx_FD7AOEhVTAlp3gETTo-1FX9nBJ3MN3T00dithTxkhVLc6Ca3atQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrnlGYd4Jct2GkCrJOOZDxb9-s5Vcezhgq_DtU2IeDMQgbm0PB2h9zl2oAf94qH6xN0GXswmCuwlI-xNle6_SzRF7d70_HWtLjNrJ8TTcrjFiidnbDkdyLmd7Jv9K7ReJSLUXRELokn2PmrOsnFN4DYw9TcacpW4E7EYCSYM3uMPdQ7lfBnSuvGWYjY2Smh9MIbyrnNeIhUdsdMyHtzYI3XoSthv5G5wGjcmhYe4YkW82CoUDwf5Uodk9iBvqULfExSd7cyJ0Mex-YM6oxZR7RKQG6JHR1o4p58HG4UMibEhcKH3sb3YgFYaCL36ovD3xv-TANr3VD-8HsW736bBUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=S1rbHiqDSuCCb3HQCeUIJAlTID-40pKk-s3pCEMOrXDF0cL_YVljmpuCLXqf3cX3-w-IgxxjKQuqXRd43d81Ve1z-mI6nsly9uQv2L5dtvEUWw9Lrlxor2MtYo4umpnsi5AJ_ohn0Lf581LdBB_kLtJDIDYfaE3VS3Ke030NP_VhcjYVgw220JCWiCUVW7WKyc5CaVdI90cHcoHQq89qBGeLJbawG7RMvZhviZovnkP63RSx1xr_BEZupgEqE-47IlkTzoJ-rkswdlduyVFApiENybInNbduKon0S7WIL61nnKxfudk03FyBcCzNFBWJjAgUdyzyjKH9X6uAS1Gmmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=S1rbHiqDSuCCb3HQCeUIJAlTID-40pKk-s3pCEMOrXDF0cL_YVljmpuCLXqf3cX3-w-IgxxjKQuqXRd43d81Ve1z-mI6nsly9uQv2L5dtvEUWw9Lrlxor2MtYo4umpnsi5AJ_ohn0Lf581LdBB_kLtJDIDYfaE3VS3Ke030NP_VhcjYVgw220JCWiCUVW7WKyc5CaVdI90cHcoHQq89qBGeLJbawG7RMvZhviZovnkP63RSx1xr_BEZupgEqE-47IlkTzoJ-rkswdlduyVFApiENybInNbduKon0S7WIL61nnKxfudk03FyBcCzNFBWJjAgUdyzyjKH9X6uAS1Gmmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=PfbvmAG5AQjcr5KxHS-2e6jBDOSrSixM_JdF6hxR_PMUEYvDJFsG1NfYhqXbmNbsVsyec_IJLn_CJvwlYwUCptuQWVzIbejKn6TWYBhXi8TGvqtIjpKGobIgyxGs4hY_ZEPsRnBBoaaHK7Ijh2I93ZEvBCGgX1ExRqAM63IB_sv7LaZCSwKktMaofZJl2RxeS0weU5XCGU_nFWckYW7r-IfwO3BAbii86TGMs-EpX70hpESEkVivNGSGKeVW6sKUha7qJ9fTkMNxO3E8DRSsybaRqmrCHCz2PRzG1qOUcdlflHVKwUxdq6BywqPwd5ZT90dFaXVA-KIQtUbjkB8pyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=PfbvmAG5AQjcr5KxHS-2e6jBDOSrSixM_JdF6hxR_PMUEYvDJFsG1NfYhqXbmNbsVsyec_IJLn_CJvwlYwUCptuQWVzIbejKn6TWYBhXi8TGvqtIjpKGobIgyxGs4hY_ZEPsRnBBoaaHK7Ijh2I93ZEvBCGgX1ExRqAM63IB_sv7LaZCSwKktMaofZJl2RxeS0weU5XCGU_nFWckYW7r-IfwO3BAbii86TGMs-EpX70hpESEkVivNGSGKeVW6sKUha7qJ9fTkMNxO3E8DRSsybaRqmrCHCz2PRzG1qOUcdlflHVKwUxdq6BywqPwd5ZT90dFaXVA-KIQtUbjkB8pyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-spi6Cp1WglAvKBfbEKFCQ0m3eMdV_K_hQ10j6nUV9hpwcW7h3wimkrGOzERs5nWvEJ_xznfDXyC2fRSKdcEm6SFZPtTVe2nedI9RZXtJjQmeJPOI1EopnOTOY2uZcb1LuF5CKE2xuT_sv2OMfVYgo6rN0bmdDJIOeibz0gciPwpVjJnOwuh3q_YD3VgD3IoMQPnk3T66pbtlLrLm_549TJTuyqUzaPzaE-TLP6o8T5piOXWpAOUgRTherpgZ4roAYMAW2jPa7Xa5kjPYmoO-3ie6LGZBslml9lBtPphUgRHfIXLwvueEc-Ztabq3TCKkOxg26etJlUOP0g7BfTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=iaERmvALXagNBk2Md19D9w44zQYT-HIEjacDXGtICEBJO57xEUbBxtdSzmh-opnlR3MoAonrWM1i1oue4xe8aUdt7Z-h63aFPF34F_5StgmmzbSGh9f8NSbvSBmXXTjhJwhmgq3BKTjW2btYkwEJYYB68owh9XeHY8G_Z6x6u22Z50ZBnL_BT-DXzZ9bAmX7o28k50-C6hX-Ht0wYXO9zB04diXFOG1rLIjqA3Evy_N6t8R0_nmXjDB_5wP4jebsvygy6S0tz0nAzT02_mWYfhumX8fhga2SWTBRp_Mp1lynmmziUfbQXQ-MpyHSsVk6RXU-Ot5U8gQ7ZcC2RDBHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=iaERmvALXagNBk2Md19D9w44zQYT-HIEjacDXGtICEBJO57xEUbBxtdSzmh-opnlR3MoAonrWM1i1oue4xe8aUdt7Z-h63aFPF34F_5StgmmzbSGh9f8NSbvSBmXXTjhJwhmgq3BKTjW2btYkwEJYYB68owh9XeHY8G_Z6x6u22Z50ZBnL_BT-DXzZ9bAmX7o28k50-C6hX-Ht0wYXO9zB04diXFOG1rLIjqA3Evy_N6t8R0_nmXjDB_5wP4jebsvygy6S0tz0nAzT02_mWYfhumX8fhga2SWTBRp_Mp1lynmmziUfbQXQ-MpyHSsVk6RXU-Ot5U8gQ7ZcC2RDBHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=eyBvkV7s7qjHxyOFKF3AqpOGBJSUtQl2KM7EU9jl3_0tn5fZqHuvAl3-je_baIciVSB6jV1DG7GDNgG7lgZQHZEqYMZnr8sdPFc5-Geo_wm8ECWcjl4fYPU0nYKQ0Klqpy0kXVVqiAFrup7W6Bhr9M1cw8kX2Qy75KBPmN2tERkes82W0S_xkGepW5k1YE7t5KTEiTBJIGNciSe283hot5kgfrjUrm-1fm0szxMHIga8B4X9jYhc-3ICV53CNELB6qYzjGPvraYhdTDbNwRfFlih9GJF-hwhRUH4-FswzwmE3jU2TC4h5as87Fn-mTs5G_5uEmLwsU4DlGtuGT6C5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=eyBvkV7s7qjHxyOFKF3AqpOGBJSUtQl2KM7EU9jl3_0tn5fZqHuvAl3-je_baIciVSB6jV1DG7GDNgG7lgZQHZEqYMZnr8sdPFc5-Geo_wm8ECWcjl4fYPU0nYKQ0Klqpy0kXVVqiAFrup7W6Bhr9M1cw8kX2Qy75KBPmN2tERkes82W0S_xkGepW5k1YE7t5KTEiTBJIGNciSe283hot5kgfrjUrm-1fm0szxMHIga8B4X9jYhc-3ICV53CNELB6qYzjGPvraYhdTDbNwRfFlih9GJF-hwhRUH4-FswzwmE3jU2TC4h5as87Fn-mTs5G_5uEmLwsU4DlGtuGT6C5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VotKE3Mg2UusRXWMw8c9JRojXRIipFjlxFIksJahg4ikpoe6h1US_5fMfcsHyYZQ8wYfp_vJRhQ_Ul2YCfaz-wO3NhxQ8wWnyhiwjwgTf01LRnQsB8RY3jHBPfHY8jxEsXfqHcFWlAEtd0FsdM2PzZOE-Fk6mZqWGd8-0vUbIyxVwjX1ydf4pma0PHexgLFCoEVDzTNUv1nCK1ISQDMqh1I-gcWadT4I9xNGmL2AD85O9W1LsSj-X7NLpqSun096ULH53l657WMOIvf3iIwpzlq0FGa2djCFa64XIBB9OPiKWgxbSCWVKP4ZmDC1_x4cIpIVR8Ro97QAk3fhUNhQg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VotKE3Mg2UusRXWMw8c9JRojXRIipFjlxFIksJahg4ikpoe6h1US_5fMfcsHyYZQ8wYfp_vJRhQ_Ul2YCfaz-wO3NhxQ8wWnyhiwjwgTf01LRnQsB8RY3jHBPfHY8jxEsXfqHcFWlAEtd0FsdM2PzZOE-Fk6mZqWGd8-0vUbIyxVwjX1ydf4pma0PHexgLFCoEVDzTNUv1nCK1ISQDMqh1I-gcWadT4I9xNGmL2AD85O9W1LsSj-X7NLpqSun096ULH53l657WMOIvf3iIwpzlq0FGa2djCFa64XIBB9OPiKWgxbSCWVKP4ZmDC1_x4cIpIVR8Ro97QAk3fhUNhQg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHxtpRaoUEg_jCXRnjhYW9Reu4XC4vZ3gJUTeQeimmfVXRhKQenWMWFtnzRB9oZe4GsWkxHiJESvYTD3OXTZSZ3VkEvIVG1PX1S2yoDwZpjg6J822-xq38x2cCXlM7wufXShRHykCYGLjulr42vyiAi15BbZMEq5L31ZYyhp2V8IrDXc7qX3z--rdBnDUSqh6pZUA_2pHuxQSnJBdANcCP6cRb2fVsUUdrFC7GRd16C8uHVqnr0OHMMhH61usMQg4xa69cqSlpztU_wvqTAJfg42nCiqJsmCZrq6U1JWvbA_GnP92PBwy-dzUqjiZadUzgskstmlR5kfUoQyrGXt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H50D1VDZX07ccfGvoWBMc0pVWhgKuBMvFXIdPYEx-ozKgIj37u62eWz8UmX7ukb56pFZBAEo8JFQ3gloTQgJqgWvgp1K8UG4NcHChmBv5mnC1gxtnnl0BLjAz7JdKqxUoY59RoF4KPdb_7xDpPnObFwNhLGkWJpr1jnk5JVPKlPIFpjS0SvCsGZ6jusW3pFIpFHtbglP6Jd8dO3kMEq1Z9kVfmw35hCsFWWe9psvn-QWybDTp1wEQiTpisi8nIxvsxpgYGEjEvwFaFGeZrkEy0SQgP-BQyOqG-cY85Ww28_GMVRWTvxXXnket9tkZ67VIRrpZy3y99Joi5K-v3SKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4ff60yrsaGdhw7Cs7Ix6wBnh_mu_lNu-0Pw0lX3uy3kmdWMgMwYpRaE-HZmWY_QM4IzemqaRN-zJM5XJEk7Jl-7QtbdDeD6eMmSw0_Xo-kbubKwyUKwAM2YmEoxJ52K3uHxD-t7WGj6dl5_o__Aqpux13nG9nQrLvXqrxg4RmvhMMseNneaf2fr7k3jhmvnht4CMoEIx2roVFg3IoEsmhn0wKVq9A1Fv-LS6DzJ7_g4rkVzgLBnOFKDFkzeEwZDTqxZs1ViANh_pj5yNOgT-RBKSUBVdaWwyzWEIF1_C6Kwx37v1gWJwNjKfemQown5LbIQjky0tzks_j43Pw6rjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=aRIYxZ8k5UPdrUkgHXnE-4oDzVKNA0qR7ba3Ft37UU_Vohtw1XZFFGmZE4LmmPznUmB40FgRPzTUe3u_p1uxjZ2-9AIMP87SAety4imfCEMqLrc8BpIO3Zdgnfk4cMDSiMk7WCXaKQLV-bVxDVSKJv5REbRrQhd9w1NUv5v_M_jfJ1DiAypMV_1bnlfIoJvn6M0bOfPOE7yLlGp03VvJG4bDACytqbOaD0f4HsFeWAgwDgwtQ-DLvkAYmxwof3HfIxL65f6HyuhSJmk_KkIDrC9z5kdDpVEBtEL-Fm3LOSZGThCLAJBQhlBKwhyURzroxzgdWc6bcIVJ5G8GOYFEWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=aRIYxZ8k5UPdrUkgHXnE-4oDzVKNA0qR7ba3Ft37UU_Vohtw1XZFFGmZE4LmmPznUmB40FgRPzTUe3u_p1uxjZ2-9AIMP87SAety4imfCEMqLrc8BpIO3Zdgnfk4cMDSiMk7WCXaKQLV-bVxDVSKJv5REbRrQhd9w1NUv5v_M_jfJ1DiAypMV_1bnlfIoJvn6M0bOfPOE7yLlGp03VvJG4bDACytqbOaD0f4HsFeWAgwDgwtQ-DLvkAYmxwof3HfIxL65f6HyuhSJmk_KkIDrC9z5kdDpVEBtEL-Fm3LOSZGThCLAJBQhlBKwhyURzroxzgdWc6bcIVJ5G8GOYFEWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
