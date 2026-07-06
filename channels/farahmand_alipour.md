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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 01:22:22</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=vBEvhmW2MaeK7V5V7BecczLnyNYKSpbIoV0w3QZCSlUOFLv4wpU-KHaPOYDDkD546zjLN1nm2Tcm2T6gc3YN87_CMF-Cc88rPdyImdh_M6CR4mJVKHX0hNOzavtuTLecE55plxZjqty1b9NZQ3kRotL0LDoKu2dyumkg-mOKz1GvX5KSM6XiOgdbwC5GfKcRSLyh9-RApGdoLHHumJlTX_dK7hDSx-oH7kyUeO8GMc_VTHpgfNX2WmVdXOupS3zu2rT58f_LH-b5scccuhGROzweU2nHbQXzoDcyxaNpMnAy3m7-NMCaiH1zEpD7vgOqJch8NPJQ9p_vtO5fMfpK3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=vBEvhmW2MaeK7V5V7BecczLnyNYKSpbIoV0w3QZCSlUOFLv4wpU-KHaPOYDDkD546zjLN1nm2Tcm2T6gc3YN87_CMF-Cc88rPdyImdh_M6CR4mJVKHX0hNOzavtuTLecE55plxZjqty1b9NZQ3kRotL0LDoKu2dyumkg-mOKz1GvX5KSM6XiOgdbwC5GfKcRSLyh9-RApGdoLHHumJlTX_dK7hDSx-oH7kyUeO8GMc_VTHpgfNX2WmVdXOupS3zu2rT58f_LH-b5scccuhGROzweU2nHbQXzoDcyxaNpMnAy3m7-NMCaiH1zEpD7vgOqJch8NPJQ9p_vtO5fMfpK3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id6hEMXR7ZDflPlotw9Zd16G2JfeUQz091-8ZF70naN8VvtyYvvt03KnEXRn_N6TAAnpB9ijQ4MzvBB3WrH1eNZ-VfveUUSi30gI1ehN1M54F1KowFN1ESSUFRmuU418fblsrgUg7iynmAzCMH8JNDu9Y0ujIouQlrW80F9DNgpR8QtT5RajQHVJ8zmCwA1h6e_-JzhngdL0XlOBt7JZTkY-pZbA7YzOIyl13G-OsGzlzMTBO4ciN2SKOnyfMmIbeUIZJZWRr7idkespCFjWgSAK8xAqZaklNOhx7y2557a36xVIoUpA5B2c3ingbEu1VFPcXx4AebfD8MfqDoeDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMsYYJhGuggC1if8s3aNH1pYm_syrf3gWAgQjnGu7FuarOTFZfZJjy-xToogkitf9RAYyS_MYsg22EBUtMT7N2AK4TepZB6v1kmg59ZR9lLsRkPfp20Ya9pGfZFZjfjymzVbFvUBjrycBcn3o97zy3ZH7UhwP6oGu8QgZ1jwiMzDc-mG8DJcmCM4G0glRPoO7SCKQUY7ri-eKBcCsM8OfdX3BJ1aoNwTLVqhVMVta80zGcKLDH7fi2iSg10XBHXga--UerW_tff-9I1CjAnxHwk2ruqNjZeIA8SfqRK0jtlBaP1UpUwWnMipbNQ8sz_czegx0JT6a0XnRIMYX4BX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic5NifPte1jiI0KA-9GziNpJi-NmcSUo7_53qeisMvjSsDpd4KrtdG-WGv4hKQnS35UVfafgBjw4rsct9b_2JSJUyFCoH61fhy7UQ3U2ukutL40SEYeem0lMhEmb9vZXYhHIE2dtNEha2Thwxn56ueMwqvMDJTI1gYAppO44DT4tpSs-qx-Dz58TWPKdImSde1V8lB7ZDJ5oozAK5C0PU0nOBde46FZ8Hlxyh7J2HDfaurEf4PN-6vh77e-aE5IgOkjQOMdyapu3WadZBW965yN8buoJcT1QsjNmy919okXT0vsgLKGDhGWW-ZdFq_OIbqAjdR34garCCOFIIUYGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZsKK5LN198v4i1RiDOAGHnyIVT8FNxAgeqIMnDV486B6DPNzAyRdfm3ZQ9OVIsdUR0d-IeOMD5HCk6iBzsS1yVZ2CGW1Uy34NIlxVOVobr1toOpnvbPhVrnXVGRSRYae3KgtUyjaQ6AbmcPucv_JCWWYexzAvsjHDGrx5x4zlXKqmTfL0fyle12ddnueBA0Ba4UvBlAftGX6K7BpN800k_HIuH2exE2PX09f7fXUjEJxMSktQuQzKQPHtsRoUwQmdLFpkX3IS5k7X13OlVsNOL2as5YA0-jb-gipgHpYIO1xgJIlrTCzHN5qpDeyHupa9uNB4pdBa7EthtBHB0tyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV6DEW-Rsl0opqNqcrFJ8QxFXU86NUzz5BsBnLsuSYAhQJvQ37zSKurCl4yZeCHd0YCBpknq7VcGPnTBFs7QQOuCewJkl-XlN5BI889RCUMQ9BO9NOvGrg3Xagdi5wZ1uuyeHFuhGzKkhplGSUm4YVGWZziWJ6JqoGEzgEKiHH_KBzu2LnzUbUXX9nPC6ZwShRZRv39BS8VYgGyZySbDUHN6_1KUd7h3MvpMhjJcVxxPtrCD_umgIno0ZJeBw9k218H38qOc-37EcddOpQeAxC0nrbTNgZs4TzT444q8X1aWJY66e8UFNqgMPbLbJxdkrN2xs0FzXm6IJOudCwxB2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyUoImbLYotybMe8Kqp7wteHJrOopW-vJdAkKHktzBvOXemU5DmO0ugyt51gNGzqioqlE9pXzS-vELqa23gwkdr5K0iWGy12wyaNwoRf-3dpTNLe5SC3p1bA8xBtrvVOcxBifzzvZ2RTkl2surTr8rlPf4x5OvOSpkGelf2O-heHVJSfWLRnZW6XcCJbcKiaaQXaHlP41JePNWAoPINFVbVcna5umhSt_MfjBmcu3BhZ-8mZpIxBVoeumd0GZWQ25_gvkhhA4SK5FT9pUT1SO8bkpP3kY8oD_Ixgss_tRyrqOBpfQe3tKlLEePuwE5eJ-6haYMKuaYz6CXdqKeCwmA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=MXOFspqyjlLUSorcsVgwaIez1o7sFTJSkEZm3gCZXi_nb72pBh85VUNm9_gE0yQ2jPUQ2A2IYghN0jGfpvZ6P6OZ4dR_HXGGEogJd89uc-C1NxGsiO7C3qtr8wAuQsaTKGV0hl2Eb0LfrxCfvYAhIfg99jAlnNNrF6TemukqRVLcYDIcC24jrx3b5D62G8oWL1QFMwYoLQe7Ycn3G1LX6R4FErZ6-lF3bN2wBsC_fEuUJgvWp01Q1Zop-ys_J3rNVObJaQ3qwD2cWn6O3cY-wMQLb0q3qstqczMNbbGWj3OLnd1pshDMSttH6dKYu-h0t-bt9B5LNGx4cW98B5w_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=MXOFspqyjlLUSorcsVgwaIez1o7sFTJSkEZm3gCZXi_nb72pBh85VUNm9_gE0yQ2jPUQ2A2IYghN0jGfpvZ6P6OZ4dR_HXGGEogJd89uc-C1NxGsiO7C3qtr8wAuQsaTKGV0hl2Eb0LfrxCfvYAhIfg99jAlnNNrF6TemukqRVLcYDIcC24jrx3b5D62G8oWL1QFMwYoLQe7Ycn3G1LX6R4FErZ6-lF3bN2wBsC_fEuUJgvWp01Q1Zop-ys_J3rNVObJaQ3qwD2cWn6O3cY-wMQLb0q3qstqczMNbbGWj3OLnd1pshDMSttH6dKYu-h0t-bt9B5LNGx4cW98B5w_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=WXXgm4KcWqMOX2fD3wN5bh_iG6IGQZIR5tfp7o8YFgadyawTHoos4zdoHBuROK4YVosNaS6c0Y0-yigzmWMU2DwTNf5q4bfL-LcEGCZmjzma1klbg7_h6lqW0vS8crRseD9m3PUXvPXKZDB_06-0zjCsI0OJS4hvTKsE7NjqSAkZO8zMBnWFyk3S1vFqsNJR3iLrS7ucereVBcksbbDnAZWdEagb_NSbqecjdMXSPPlX3SZBe6GQuwjG21PJl_LEz3gOfymJh0v4w5pJnojDiqwvHONLvuSIw8-3V6FCQPWNX2rv6qk-3dwDEUd333Wp1WKSRALdZ6saPG6O3OKNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=WXXgm4KcWqMOX2fD3wN5bh_iG6IGQZIR5tfp7o8YFgadyawTHoos4zdoHBuROK4YVosNaS6c0Y0-yigzmWMU2DwTNf5q4bfL-LcEGCZmjzma1klbg7_h6lqW0vS8crRseD9m3PUXvPXKZDB_06-0zjCsI0OJS4hvTKsE7NjqSAkZO8zMBnWFyk3S1vFqsNJR3iLrS7ucereVBcksbbDnAZWdEagb_NSbqecjdMXSPPlX3SZBe6GQuwjG21PJl_LEz3gOfymJh0v4w5pJnojDiqwvHONLvuSIw8-3V6FCQPWNX2rv6qk-3dwDEUd333Wp1WKSRALdZ6saPG6O3OKNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=t3ahGuaoUv1imtYL8LFUAh3peA0Wn3sV_WeJE_tQibf6a2uluMukq-EyJo3jWcnoDhYZ4jHxqbwNkptK0009shaFhEQX0-NCtG8FJvik8dwgSyw__Qq8HYbWlGT_VZpxm8seAzsp8a6E0RXn7dWj50Ia_BIGGyZA0jPK0wCzj86leC_40f1LVmzBv3AJLxy0VFg5lRpzIT7jdANAEO_XBcYTyvonboNrFqk_LFcyr_1z9SGjRs-_w40J6zdKCxdbU1k6fvGSJzI8giFWTpkQKQ1zYGoLxfjok_aCa3t_JH6FblhFUSycCesSXNDJEHxdxvN_MYeqf2AtsK8a4k-oxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=t3ahGuaoUv1imtYL8LFUAh3peA0Wn3sV_WeJE_tQibf6a2uluMukq-EyJo3jWcnoDhYZ4jHxqbwNkptK0009shaFhEQX0-NCtG8FJvik8dwgSyw__Qq8HYbWlGT_VZpxm8seAzsp8a6E0RXn7dWj50Ia_BIGGyZA0jPK0wCzj86leC_40f1LVmzBv3AJLxy0VFg5lRpzIT7jdANAEO_XBcYTyvonboNrFqk_LFcyr_1z9SGjRs-_w40J6zdKCxdbU1k6fvGSJzI8giFWTpkQKQ1zYGoLxfjok_aCa3t_JH6FblhFUSycCesSXNDJEHxdxvN_MYeqf2AtsK8a4k-oxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=QYVgUZ5kQSAW7R3CtqppH2nagj5vhgMIWZxBreSZs6lN2fn25aEnPgUh9iWEusVGdsOIkbFddlUs4RRBa2xLx758-aowhB9cQIMmLmO6_I0DRTDeATqtbAId4rvow63f41zajt-mmolxUSZbjIQKJ-RSJHG__z7xJQsxXl2NrA5bvYV1WjeDx8ZxG9LqtY4Q48-XTpDmD3I5eY-qGQjGlK78PM_Y7Yrz4zabAkJRXbYH1kl0seXcS-cKsI692BENpPuWPlinWGCQwqqw7Lo4P7nKOaieLMn-w3_vNErWWc6qJIIXS7571gio82zGcpYH0xSmyt9YFNq7rabjb_urPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=QYVgUZ5kQSAW7R3CtqppH2nagj5vhgMIWZxBreSZs6lN2fn25aEnPgUh9iWEusVGdsOIkbFddlUs4RRBa2xLx758-aowhB9cQIMmLmO6_I0DRTDeATqtbAId4rvow63f41zajt-mmolxUSZbjIQKJ-RSJHG__z7xJQsxXl2NrA5bvYV1WjeDx8ZxG9LqtY4Q48-XTpDmD3I5eY-qGQjGlK78PM_Y7Yrz4zabAkJRXbYH1kl0seXcS-cKsI692BENpPuWPlinWGCQwqqw7Lo4P7nKOaieLMn-w3_vNErWWc6qJIIXS7571gio82zGcpYH0xSmyt9YFNq7rabjb_urPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=iXoKuXF6RVw-1s7kzQ1WzvLN1bkB4LyzjCaqpK58SwyMsv4pMMj_OQQ-hmpm2M9vz_dpwnrybhc5z1hWWXwyPJYduoK61OxVLEmxDjIsucNKBDPttXWVfUaZUPz4xGBku90dv-WYQFfcUQF-YdV7Yn3UOr9iACzX2fYO-yW0iQcTkp1bCCWAEqe3WHUgDWJAd0TFHaO7VjG1pXjKGVdepRyw9bkAXooz6SeLNCWyf7EOcl2OWtG63xZ_I9Chm1CGOd0D3g_SX10sJDAI5yRPFTKFF7IpmKskVCCfxU-hhGWf3RB0Aj8rmlq1WCKwkRBqxxAduzECCpiWt5nnof6cYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=iXoKuXF6RVw-1s7kzQ1WzvLN1bkB4LyzjCaqpK58SwyMsv4pMMj_OQQ-hmpm2M9vz_dpwnrybhc5z1hWWXwyPJYduoK61OxVLEmxDjIsucNKBDPttXWVfUaZUPz4xGBku90dv-WYQFfcUQF-YdV7Yn3UOr9iACzX2fYO-yW0iQcTkp1bCCWAEqe3WHUgDWJAd0TFHaO7VjG1pXjKGVdepRyw9bkAXooz6SeLNCWyf7EOcl2OWtG63xZ_I9Chm1CGOd0D3g_SX10sJDAI5yRPFTKFF7IpmKskVCCfxU-hhGWf3RB0Aj8rmlq1WCKwkRBqxxAduzECCpiWt5nnof6cYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvKjW9b_WxcgpLWKaIgmh7aBxg00ayLW8vZYIsPyrc7B-GHsmhpB0MMJmgbN0nIqkEeKy9K8COPIqgdrxcLt_-FDZlLas_tQEjPtITMRLok4zRxm3qZBDtZ-KDMAotXi3GbJhhZgGxF_gbw7g_iUtF1K7soTk8w-_DCPkfofzHmovGLEE6UL94hlf45V-Ymjo5s-DDWelqNSRclrbDI03YZ_f-PogDCiRljGBAvE14i-cjFrwweWyZT8wz8iMGTi9VnCaYWtPemGQPA0K4VGg3c9DFQSItvj5IVOK_iIS5WSrYy7vkHnIbVyD0as71wGjmOvT7iHSSwTntHy60cbTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2nHgUVuoXBLOP6mQPSXcyb5dVHMWZZHzyz_-VI9wjmacsrFOtfSxQlOv1alT4p5IANWFixJ9G5XxAVPyljjaDrP8SUPPa414j3RCzvLq7UGHw6cmQLexLWjTr8LdVkxHOtwLLni0KQDQmbVcnk95yMSbBtgizJ8D3PWbFwodtTzErOhKzywwUZbe8SqicluJ6aYSNOpk41ji7hdWQF7-BJJhcwP-dtXWAs6Rrd3Jv_b6HB7-3mxoHdHVYyo75cMtzxTczlW5dvdp9hXjA32meDNUY4Q6AiLKtcVYUIvS-n-JVMsqn4sdEQeVF4JZ6HMdm1yg_FMyYp2njV6v5xyDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diKkyO-8rvQjpcl5w1uHnFZZo0wqtsu1RIOK1n8ZIFkxIaohs-4q2Mu80Rm2OzRmUW0fP-C60B_h7P2myhtuznNAYRZwMj4yfEZpSxycdD99uaDwVXBeLBCyV3UIyiSltohINT-MT5Cb-CT-VXn_zrLpPbe_u28grpqL3-b_iVmiBOfTySqAq9CHcSGUt32Rq6TqmQ5vYnjIKKwkcUiQ_U2v-bnA0Ikeqac3UZBc2jLt8ZGIFDUqkapRywIzbPeH4LIA6DnFO-sVTVZi5-kmA2xEdb20Pcqg-aWc92hzX8bvAjcdSP4rbJBRJQ8sUFt6l0rO2b1RpyC82dJqXxNQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K32MdyOCprtSDXeTLwrmj_NfmTof2K-f03cGJjI08EfzVacGvJYs1bzKkfNL4f0xlL1VahEV9InsHx630PjafxRIqY-pumd7mZRR9zYbEU8-w_Svp4UktrzNYrZ-HuRPKItSfgDOe6DW-t3jK1nbXOaqY-Wjk9ziYvpjkdrIGJBOjitaFPUvdDXh41Q3QpQC2a3a09ogGU-4kRYpX2n_9t4yW7f8ZtGzCMkfNuWXOeTScwNS9uMLZG47QUVdbavahPkyzzAsWHhYq7cOQTpqZzPxRtYOVIt3t_u9qgxBg3hgD-tRKMqHSMbB6E-6Ds5Dx-lrR_RXS_fZGiNi7Nw3-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcarmCQh6Xuc6EWdJMrTJmM4LtN4eHDr7iYWYCEMO4HzCTRYc07LRDWo7yvGvufmfQLoP22RrQwAvtZkMkflZrCucENUgJBfvqBped9msequd6cnFKOwTu4nKlxt8skCAptEu20hwG-hz87h_YTswcoEAk_abEA2zlMKDeSyLnkQy_5oFCT22D0PWRsjGxNWF-xqTBmIGpKpfzKg-Zbv57JLh0nAbl1_956AhZSn8uzNTEDPVIIcs-RmrDx10BCGqAXXq3oSTRafPOWEWicIl6spRFTiOA-yXA38_GNtlOjuKEiDQ62eu4RiGy4U_y23HoCqSiylulL-5He28gDxMA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Ej7mAb5H-awY2rb5RVcG9aNPziXNCB1SbKt7JG8k1B7pMrhc5KXgAOoxvpLkCk8wkpEoTZJYrJNcfVt8LEYiAB-X2iyPmYcaM1cuTNgegnKKkTr-AXAoebxJyfJb5jLdhWwXTsjEUmp8JZiOK4-hsn48NZ_LUwGKhQa37KzNMLDxTKOHGSATAR4IONSTiY-HaoYRKs-0dwmHRAooh6c9kQ_Xi610erbda6ZOlsfj4dx4ygYItm5HD8_nTdMjmElXvMVCf3SV0FDnPtlQMQNbNT_vAY1dleCYAbs7KnUTTbZn-gfbxtpZJjVx6hRlraIedhP6KC1oWrbQt5nAL8jv5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Ej7mAb5H-awY2rb5RVcG9aNPziXNCB1SbKt7JG8k1B7pMrhc5KXgAOoxvpLkCk8wkpEoTZJYrJNcfVt8LEYiAB-X2iyPmYcaM1cuTNgegnKKkTr-AXAoebxJyfJb5jLdhWwXTsjEUmp8JZiOK4-hsn48NZ_LUwGKhQa37KzNMLDxTKOHGSATAR4IONSTiY-HaoYRKs-0dwmHRAooh6c9kQ_Xi610erbda6ZOlsfj4dx4ygYItm5HD8_nTdMjmElXvMVCf3SV0FDnPtlQMQNbNT_vAY1dleCYAbs7KnUTTbZn-gfbxtpZJjVx6hRlraIedhP6KC1oWrbQt5nAL8jv5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=k4NG-hAeKpRoi0geP4Mfdmw_ss_Zuk0fHIYSCMXKujuSzPzl1FQqMTNM7lFdVIVP55Y3P7D2dPyaNBcw3CX4Kq3EY2KfypYFwvKGrb6i4eHyM5PZGTHN5hsiGJMTdOLkNBJ-6x_z52EFUiI-9oR4brfDBUH8ZXUSnbn6RI7qIJ8HIKQ4gLYei4IrhgVV6zI0kXNtwaIIj9sdrMDpDlcL_NCIJ3GmRVYUpSAL4s9hn1y5KqhNjyyh4u6fff2bUu6t9oDKo0PnjmOiw7jm-vB136q8zwHy5eRNXyK0F1gbP88oyaYy1brhjQN19y3hrx8NMpYJsmjhHF6OJGgnun8rUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=k4NG-hAeKpRoi0geP4Mfdmw_ss_Zuk0fHIYSCMXKujuSzPzl1FQqMTNM7lFdVIVP55Y3P7D2dPyaNBcw3CX4Kq3EY2KfypYFwvKGrb6i4eHyM5PZGTHN5hsiGJMTdOLkNBJ-6x_z52EFUiI-9oR4brfDBUH8ZXUSnbn6RI7qIJ8HIKQ4gLYei4IrhgVV6zI0kXNtwaIIj9sdrMDpDlcL_NCIJ3GmRVYUpSAL4s9hn1y5KqhNjyyh4u6fff2bUu6t9oDKo0PnjmOiw7jm-vB136q8zwHy5eRNXyK0F1gbP88oyaYy1brhjQN19y3hrx8NMpYJsmjhHF6OJGgnun8rUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=GKAkq_6b9Z7sqrHv5ChSaDtz2xilxGU2DDwTo5TxTzy9pIKGW8--Qghvf181YmCM1uvw6NK8iQUZkZZE7hGLBLPsy7EEDR-14oj5QbdqPj7LX7P1OA3yp2MdBrQWjEk5NTbahgWrKiywoE23-7aXKWAhVtpva3s9bDA_Fp-JYFmTXgv3tU5OMksZ7XUB4AT_uuGzn94AtgSTxsKk6ncljIQtwr7gsGp9GX509r_7WCR0fjmnRtfgNjK-3UiJ2HK8QvMVNiZNr_9B7CA7gZletuCQ5YtO9OR0oTOrXaOXyFnbYl6oGWEaQF7ZkrzQk8wP2GvK-vHTnM3bKSTdRwyvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=GKAkq_6b9Z7sqrHv5ChSaDtz2xilxGU2DDwTo5TxTzy9pIKGW8--Qghvf181YmCM1uvw6NK8iQUZkZZE7hGLBLPsy7EEDR-14oj5QbdqPj7LX7P1OA3yp2MdBrQWjEk5NTbahgWrKiywoE23-7aXKWAhVtpva3s9bDA_Fp-JYFmTXgv3tU5OMksZ7XUB4AT_uuGzn94AtgSTxsKk6ncljIQtwr7gsGp9GX509r_7WCR0fjmnRtfgNjK-3UiJ2HK8QvMVNiZNr_9B7CA7gZletuCQ5YtO9OR0oTOrXaOXyFnbYl6oGWEaQF7ZkrzQk8wP2GvK-vHTnM3bKSTdRwyvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=v3RNtpvHOD6J6qky0XBw-yCQvmpxButOxLGn5xcnhYrqxIlyBzn6sCiE8utV4uU2USIVgVuD7EUs4yOfXDay_0Lz3t5No6yIIt-69aj7wWPKdqJukqfMjW7Yi8qLWti3szrqu6RWoFWFbPGVpmViIYeSn2rWcBTq_lihU2b-NfkA20qchOR1k3VGkH3zpOi0UlXCm01Rdg36uS8CBfCP4iO9RivBBssRDZLlJOWORiYs0mkj1UHSdv2I9ExuFph5MKPcBQni6GNg2fzLLDGFITcOhhsxjx5JgWxXgjO4ls5LJiy1ILdosY0Uzdz1XnPOc2anU9H-j7DjNHkQLOhqcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=v3RNtpvHOD6J6qky0XBw-yCQvmpxButOxLGn5xcnhYrqxIlyBzn6sCiE8utV4uU2USIVgVuD7EUs4yOfXDay_0Lz3t5No6yIIt-69aj7wWPKdqJukqfMjW7Yi8qLWti3szrqu6RWoFWFbPGVpmViIYeSn2rWcBTq_lihU2b-NfkA20qchOR1k3VGkH3zpOi0UlXCm01Rdg36uS8CBfCP4iO9RivBBssRDZLlJOWORiYs0mkj1UHSdv2I9ExuFph5MKPcBQni6GNg2fzLLDGFITcOhhsxjx5JgWxXgjO4ls5LJiy1ILdosY0Uzdz1XnPOc2anU9H-j7DjNHkQLOhqcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gTg_Ytd1Xrnrx32ui_M0GLTU3w3Gt8WNrUxQ_AjvFfutn78oYuTWTQUlNj7v3bTwM1NZWYZWIIhzCz9LSwnIP0WrdO4XQCqjMcy2nkaeGbhDuBo1l5r7cI3VRp8Q8KNxGONT9guwGuaJ44kMsaETkEVtWktEunQn1lC1mH3GN389Ia3zOE3-ZQHOP2DYNBgY8x6DRUanSloEllJmoX55uDvI-cU5bzC0Q1SQByPyROi_1bd-wSaqUHQxnyoGWgJjk64znptnOKUHB1ol1wmflVbnoPb1eNZDGBlzzJ6db3rDiVVC49vDRh9UcUwW92vlwq5TwCZAP8b3FrZttT9ipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gTg_Ytd1Xrnrx32ui_M0GLTU3w3Gt8WNrUxQ_AjvFfutn78oYuTWTQUlNj7v3bTwM1NZWYZWIIhzCz9LSwnIP0WrdO4XQCqjMcy2nkaeGbhDuBo1l5r7cI3VRp8Q8KNxGONT9guwGuaJ44kMsaETkEVtWktEunQn1lC1mH3GN389Ia3zOE3-ZQHOP2DYNBgY8x6DRUanSloEllJmoX55uDvI-cU5bzC0Q1SQByPyROi_1bd-wSaqUHQxnyoGWgJjk64znptnOKUHB1ol1wmflVbnoPb1eNZDGBlzzJ6db3rDiVVC49vDRh9UcUwW92vlwq5TwCZAP8b3FrZttT9ipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=p_yLFGWPzO1QTjqtiU4jVSkXjmyORcVxQ890C2bj-xbuCeJofa1IV4SD8bqltJEC-M3zpxnM8-g4KZaJXgtfl0tBxbiLljW1tlIid4nMyR2Xw0n3DNHw0ykKdx0lmKSB8dpz4fpfdVUN6DlxVifnec0PwoxrZuPdX8FL8iWHrIFCG0wJiLNv-GsWLC1MxCdYO51uvQ8AHDG52XvTJX60kwZDFmoCnESrLEQOIoBgqE8k8eHHRraJoECxV9Uc7-8Azt-KAukwUkIYn6STtEet5aGTVzU7FbON77FI5wOxpj7QVjsqvh3ZNOM4bGHFx5Yw4lb8zD0IsxPeBTqJCsWvtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=p_yLFGWPzO1QTjqtiU4jVSkXjmyORcVxQ890C2bj-xbuCeJofa1IV4SD8bqltJEC-M3zpxnM8-g4KZaJXgtfl0tBxbiLljW1tlIid4nMyR2Xw0n3DNHw0ykKdx0lmKSB8dpz4fpfdVUN6DlxVifnec0PwoxrZuPdX8FL8iWHrIFCG0wJiLNv-GsWLC1MxCdYO51uvQ8AHDG52XvTJX60kwZDFmoCnESrLEQOIoBgqE8k8eHHRraJoECxV9Uc7-8Azt-KAukwUkIYn6STtEet5aGTVzU7FbON77FI5wOxpj7QVjsqvh3ZNOM4bGHFx5Yw4lb8zD0IsxPeBTqJCsWvtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=UuKeG8it5btEnNhOGDP1LqdHX7ZZdrcaKk141TF3W4zkbhL_uGZF1uu49kJsSmwtYumZEILsuna74rsd9uQCOd67Z8_Kpwn8kSe0IVKuovUD5c2lmQxCOKA3FnJ2SldnUm9JEvmeLK_tzvHffCE5uwwInjuvOlVYuqkY_o0mw1LBvxmNkzBzFWx6_BhluVYUS8Cy0tDzl6OQ4tY8coGfJh0X52tRdgaQTQ179-wZkpcPx07Xaa96J0cvwi6kndWfA5i9PJtgvgpuLRjJtcZAkRGxEQxnuY-i8W2Y-XCF_tYrzC0n7KS2CC5QSNxFKNY1lxG04D45nl8pYKWMh1KJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=UuKeG8it5btEnNhOGDP1LqdHX7ZZdrcaKk141TF3W4zkbhL_uGZF1uu49kJsSmwtYumZEILsuna74rsd9uQCOd67Z8_Kpwn8kSe0IVKuovUD5c2lmQxCOKA3FnJ2SldnUm9JEvmeLK_tzvHffCE5uwwInjuvOlVYuqkY_o0mw1LBvxmNkzBzFWx6_BhluVYUS8Cy0tDzl6OQ4tY8coGfJh0X52tRdgaQTQ179-wZkpcPx07Xaa96J0cvwi6kndWfA5i9PJtgvgpuLRjJtcZAkRGxEQxnuY-i8W2Y-XCF_tYrzC0n7KS2CC5QSNxFKNY1lxG04D45nl8pYKWMh1KJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSpqRwHlfBaWsq3JacI0XchVzCinkvWMX7GyC9MHHpRQjofDbPuw6Me1FjMvlvcnVL9A5rRye0yXbWxeyU8tSdbDKXGoVNB8qTmLLuTlV9UHPq8t5UzAbx0wFEVp9eSTlOpYCvX5HlrQcl3aRnpCUdB5GG_E4jEwkRdZtcnfuhopXqeFnrDOJKe2L1s6gQpr6qt_Y7oV2_Te1ziCFFKFPvK-AARGw6SmwSP-9NV5WQJDsBQcnwVHlTt7ZPhhOuU-yWt1IqvsNRkziy5FbDurhL2oxvRFVJ8IkaxT520yKrdQ903W2tQKz3wI0Mr4lU-c82sjF4qu_36ILvPBTMHsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gc3kboBwxKU3DmHp_LrhR13lInl1mDNkSBXKT8Wr76gq_-4ImrsNcvwBzrt9R142hb2nyhrzrIviVwOAjYoN3mzQ3arYqdjAbSRzlPJI1foyoKJZDi_welq8w03B8NUEXEoTwMI7EUvQHDiJKbEEXS7kvMSuptCitkk3E-ViIVmyl0YdWoL06ydO8OMyF_xKNCJuFvZPbYWuCgw-Zt6rD7hsFM4LUfnBpq_L2VrY6uN1TIZ6h0hAOf0mPhz9uChDHVs8KhdKRaDSTgyP3mQQO-4_mkq3AlOUsTXUG3xP8z5ia_9o33yiOIg90zz4qcFL27jP1Nivq0uniMTAL91vhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=FCLv10dJmaBo5in-yHF6ScK1u-MYDZicKnyxABGA1DTr5jwMg0GJ-i4-BK0evXkHd1g912gFZN0yAQQ1HWOoHMi7tx49JYKE2ZCNpzhvq6HaZ-9r8qdSknPekrDsyqprdleDiTO-WEHyn8pcjp3UIYr1uyPuz6ogo9boz-t1FHj6zrRGR5KCyCFwQ97KOSdB7JXacpRnaDdnfVFVO8Pp22b4oEU4e9DJuuvhXxLYk2pEw3qfQXzDwnpaNf9cmnLGiOxNMotafRLONRxCUrK25OZNR9Mx9DmZJ6WOiSZxACQg8-MUWTz8lnOz0ry-MoiCMIAq42Esgk-C2h2uEazT5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=FCLv10dJmaBo5in-yHF6ScK1u-MYDZicKnyxABGA1DTr5jwMg0GJ-i4-BK0evXkHd1g912gFZN0yAQQ1HWOoHMi7tx49JYKE2ZCNpzhvq6HaZ-9r8qdSknPekrDsyqprdleDiTO-WEHyn8pcjp3UIYr1uyPuz6ogo9boz-t1FHj6zrRGR5KCyCFwQ97KOSdB7JXacpRnaDdnfVFVO8Pp22b4oEU4e9DJuuvhXxLYk2pEw3qfQXzDwnpaNf9cmnLGiOxNMotafRLONRxCUrK25OZNR9Mx9DmZJ6WOiSZxACQg8-MUWTz8lnOz0ry-MoiCMIAq42Esgk-C2h2uEazT5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7uNgdPYcVpf0qNQIvqu2Q_-VsHbwr_L4ExNotyXLNL-BVUgaOe83dek7Gyjb4pJhc9gJnfajJFtAtFK5lpQ0ezmriDmCgGvpUIVEPIiNNMrFitxpSpkByBFLhHmrgAxZ7_uoqRnTPGWY0yathKhAptdbWxDls67rAHO-7ErOgXLnTZ26Lg2kMhtEEkS6y3eIcZ1TgngE9w-o-ChC3Oi3wWApJC0MlLljmCr41ijR5q-kAtEZ3IQMXEYxH3VPg1sipdLvvoAe8LBu5SYB5cS31ixMxBVoq4Ru8qJeUDnVRdTOo7eO3bTwl-kn6DtVVpFVy5jC9PEeFsDubcGHHhQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bl5KfgRTqKCHKQVR1iz3uyrqL34caJ5OZSm06KwpnssbyQuMuuLs_oFmfFbkX-jh_bCi61DMxHATyGtYZeU3sllKxZrpzGoYc-LNguStXe4F9Fxvcx5XZmLr6F-iTujo50kQvBxYU1ekp768YaNRjksu1oiE5kK4Y9-bdJqE1lQEG2ge_7QC898i3iPJeijymggUIUTJAzSy7HCZt1iLRqawmP57kJvpC7-GiNL5_gMjlm_T3Z0ZFU5EAg2YmTtxS1JEO1vmpxKzGVz7C40TN9d_x2ZK94h5OtH9jyBYoi4tYe9FkonYJecj6OLsJ78M56FAtm-puvAbRqiKywlO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELZAG25CV0ckwV6o7AsdBemYpixmh9NA5qvTn9M-qeq3aS3PDefarDboPMKOVBG45urfZzhi_d25G_2x5NFQ9EPCy_VtRIe9QAv3EeziK41qPKPJN69M2ggPXDsJcovAj-IAIAaE0KqdogETX4xp9PHgCm1c3v38jli1NiMwokmZmR8F5YMIsyJVJT9aIYpNxuaF37EuhUELDP9JLEZKoV4oWhVIaSu1nn7L4bIBWlZlOev4qsD5ubyG2XX3dhODiat_KcUo6tVLNuljorc_d6q_YWjOyhcitzLd84vUCT3fqk9sfvGKAZB1G-BhhFsHP9kBae5oh5LrnYJTon0a5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uml5DEVq2R3mskj-eLO4xxJ6XDvrISMgnV0mcJ0xRSn_imFCJMVXvjMJC39YucRL4IkveRun6cQwqPH3QVhTAlYiFxmYV9buGzWL886Nwtx4tDdsqdRMxbPIIMFtZdeGw8cGn4kJy162Go9N8MTTpwOLPTsX36xiAlFBByedGO4JUH_dpjphYitlOUHHQYMlFjeIJ_kFhzA9yZylrSZOJzWpnYBLbnAfUk_ustpyI-QrlqrII6JyEEu70Pz6NbmAjvx0WdwUOvQBa0nSoyaRbaouF_KKGi3e_hWwJMBsH2Db3gWFXnKDbR7z7xBT72_0bh_hAhxxXQwR5UVw1Gg7PQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZAlpDq4-geUazyzt3ghCRUjhV8rnJ_D9gOK2lIayPiZ0U61v-mZNqISRkvNTIHrq_z1O89NCQe78P3KMXtFKrUM_iN7ohjdDSicq2JBBq3riE2Pvnk3VX84ewIE8k-L-orPmmjAqj17vYlIF7qAfJfoV13pDw786-uTp6eYuJTp686APriO6ONpemcwzw69vOXdlbg2OGwvwtThoCxHPqt_HxU6SLd9Q7jDVEC1S_iyccbxU_Z1SSNnINAikRDuGkEDegcJty2_nKcrQ1trd-GGbCfZ3MUPfsZ4dpotme_50U5FA9AbU7ItT0I0BWKOis7eCnHAzAh8aiZSHEPwmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=ZAlpDq4-geUazyzt3ghCRUjhV8rnJ_D9gOK2lIayPiZ0U61v-mZNqISRkvNTIHrq_z1O89NCQe78P3KMXtFKrUM_iN7ohjdDSicq2JBBq3riE2Pvnk3VX84ewIE8k-L-orPmmjAqj17vYlIF7qAfJfoV13pDw786-uTp6eYuJTp686APriO6ONpemcwzw69vOXdlbg2OGwvwtThoCxHPqt_HxU6SLd9Q7jDVEC1S_iyccbxU_Z1SSNnINAikRDuGkEDegcJty2_nKcrQ1trd-GGbCfZ3MUPfsZ4dpotme_50U5FA9AbU7ItT0I0BWKOis7eCnHAzAh8aiZSHEPwmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=lqxJCBLEpgsUdVyuVfy3YON4ER96IofUHVCmtB9YMwBz53vaMoc_NY8msS1ZgASMhyS3LcBtBOTfrCcVq1cSHS_a8eohMc9z0UVhD7QZVsQsTONCC-TTldk_0AGEkXu-9UgBugbt7Cyp81Kc5IH-EleTjIqSH2gna-fVoh7BZEepUi1frmCBcFe7hg8ZNNwMtop8PYUHg7fwNKzVHkQtV82DnOJMMK0Xq0rwPV0bWxMWtPNBCLhDr9krc-EJ8zxx1Cid7fln0FrH0ecHn8l1y-hKUf2pHBoim6f9q3vsnlDg79jBZdHGCtM0Kb55oitfkdaWOtsqKzg_BgzwoNOr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=lqxJCBLEpgsUdVyuVfy3YON4ER96IofUHVCmtB9YMwBz53vaMoc_NY8msS1ZgASMhyS3LcBtBOTfrCcVq1cSHS_a8eohMc9z0UVhD7QZVsQsTONCC-TTldk_0AGEkXu-9UgBugbt7Cyp81Kc5IH-EleTjIqSH2gna-fVoh7BZEepUi1frmCBcFe7hg8ZNNwMtop8PYUHg7fwNKzVHkQtV82DnOJMMK0Xq0rwPV0bWxMWtPNBCLhDr9krc-EJ8zxx1Cid7fln0FrH0ecHn8l1y-hKUf2pHBoim6f9q3vsnlDg79jBZdHGCtM0Kb55oitfkdaWOtsqKzg_BgzwoNOr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=TUJbUk68k0pMTmmC4uPN6cIEmMwqYt1OmuTSPt2APm0JDq7eondCWrPAIAIFNCns6qDpWSqFqPXmFafKlKQF1nwV6_kwSCtZheOuWEwo_tnb0ynWBmyOwGSKT4DULttK37No4RVnghyPIsc7w9DojFWwWY3HuoqPmDSPuR_TqU1iYz3YA_YBVxk08HxHfuauDzMM6Dk6V3WttGAo3XxrnHg9oqK4CE_HXdQToNdRPSfrT834NML_RYYmsVqXXXdD8nO5TUIoJ4zDG5YDm6c0nu14-sjs0ST8-y0FeG6qJKFjgB1uw8bB_8Zgw-Tf_D32PqcpAQkfE_-V5j6CQ74xOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=TUJbUk68k0pMTmmC4uPN6cIEmMwqYt1OmuTSPt2APm0JDq7eondCWrPAIAIFNCns6qDpWSqFqPXmFafKlKQF1nwV6_kwSCtZheOuWEwo_tnb0ynWBmyOwGSKT4DULttK37No4RVnghyPIsc7w9DojFWwWY3HuoqPmDSPuR_TqU1iYz3YA_YBVxk08HxHfuauDzMM6Dk6V3WttGAo3XxrnHg9oqK4CE_HXdQToNdRPSfrT834NML_RYYmsVqXXXdD8nO5TUIoJ4zDG5YDm6c0nu14-sjs0ST8-y0FeG6qJKFjgB1uw8bB_8Zgw-Tf_D32PqcpAQkfE_-V5j6CQ74xOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=NaKFK8P7UUlns8Zy2e4zSOYz-SdKmnBOBeGl2XX7rfthzB4TGcuLpnKDvQlAqwru3BSLuy21dqqgToYeujErc260fhXz7OVL2g7akprCkJC47OG-b5g_WRMMfpWtchhGNqiKcjRLmPmsadufPVkXWsr1Iv9LGf27u04XNBeo3qsxV6rachhIB5_T7Mz26UVouGwGp-UKeT4GNbHEE7lNpmuxt6cShLqUD7bVA7bL3P7HiqJJM7IXu41y9VeNWh1eGKnq-l9GFjaNFXOwJdyp-DE9tqDKwuugnMLndxisMSkRIv8FkrGZybvBcT0MdAb5Rbg2isWYNBtqFnep4FiJiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=NaKFK8P7UUlns8Zy2e4zSOYz-SdKmnBOBeGl2XX7rfthzB4TGcuLpnKDvQlAqwru3BSLuy21dqqgToYeujErc260fhXz7OVL2g7akprCkJC47OG-b5g_WRMMfpWtchhGNqiKcjRLmPmsadufPVkXWsr1Iv9LGf27u04XNBeo3qsxV6rachhIB5_T7Mz26UVouGwGp-UKeT4GNbHEE7lNpmuxt6cShLqUD7bVA7bL3P7HiqJJM7IXu41y9VeNWh1eGKnq-l9GFjaNFXOwJdyp-DE9tqDKwuugnMLndxisMSkRIv8FkrGZybvBcT0MdAb5Rbg2isWYNBtqFnep4FiJiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=XeI7GJkmTHH3XNbZdtSU-NlPTWFOQDbbDQn6AkRVKg89URYnmZcy7H2IDorprwgxDPljCI0DOjOhzaNuaN-L0gW6i4qKli3di-wpPW5pV6MWD3W6N9hs_H-9e647CxRwI0w61kK30MXCz5kyi7-uGG2dwa-dyJPAaggG8NASmcT-jU3jH6uD_I-M_cY3Z7_HizfmNIi1TMtfRsIZzmdvvrE2jv6hzwapUd9sArvyfCx3nPRvqgl-HApUc8ej7pfbPPl2Fl-9GsXDUmcYozyyUlyHOoroMGkBLFGcpmtabnMKNPddGyq2R3zhxgH2lA4M_-iqd_W-byC-vmiYaI3VvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=XeI7GJkmTHH3XNbZdtSU-NlPTWFOQDbbDQn6AkRVKg89URYnmZcy7H2IDorprwgxDPljCI0DOjOhzaNuaN-L0gW6i4qKli3di-wpPW5pV6MWD3W6N9hs_H-9e647CxRwI0w61kK30MXCz5kyi7-uGG2dwa-dyJPAaggG8NASmcT-jU3jH6uD_I-M_cY3Z7_HizfmNIi1TMtfRsIZzmdvvrE2jv6hzwapUd9sArvyfCx3nPRvqgl-HApUc8ej7pfbPPl2Fl-9GsXDUmcYozyyUlyHOoroMGkBLFGcpmtabnMKNPddGyq2R3zhxgH2lA4M_-iqd_W-byC-vmiYaI3VvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz9OODm5ECuLAx5uBCCn0Hy0gErMapL3-3o2e5jPVhuapfhvJF1EhJMP_VLlVZqLabRFsZMXh48CPSh6PrKQhNbcZBzopiJT3LZ6PvKI8DuLPiQ9HSQxP4AbN1chxYP6ihzWAQP_XV0rNyTEWxySnPakbS9NWVyrcifDH9SsbUNpZ3Cz-V9ZIFrHl3BB4QhMpwFfwKkweMI-94sbJ-q9SUdOF5tyBt07oMYZiw4-z_cLjCnkW8wC6u-jYTAlW6crzq6cJX4UGFdjtw9YMYJ6nyoEXWEbVjsAq39vF7VNG9_gqTyPwOZhe0n9uGj1ume_iiJc_-muc5fIqZnNWPxTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Y8b1_0dTF_FYe_YsF-WmzNhVHWwDCQEq_L9arkv2wMbhJYjbCmNX4YnzmzbQtlsky_ghoR3rljIDzMtifuzRNCAja8h9J4CHSY0imUJnBDklGI45AaqwKjQSsFZ6f_UtO6A9MIzBG74INHs3O8Dz-S2Ny10EHJnYR41lvCeNJTN1aGvcZHuGd2zdixT57hP8fzB6Dw_Ed_yIdoTOLYAMz8DDCu67s_TEdKLWokLkvE0YPm1zjRAZY1BnzADTbhWunT5yV9CxAQ2jy7Hosbpg7U2DZRS53mgVFM5QbTcVhRv9FCUO2j6SK9weagj2W6cyNddY1BROMcB6N9PJPEs19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Y8b1_0dTF_FYe_YsF-WmzNhVHWwDCQEq_L9arkv2wMbhJYjbCmNX4YnzmzbQtlsky_ghoR3rljIDzMtifuzRNCAja8h9J4CHSY0imUJnBDklGI45AaqwKjQSsFZ6f_UtO6A9MIzBG74INHs3O8Dz-S2Ny10EHJnYR41lvCeNJTN1aGvcZHuGd2zdixT57hP8fzB6Dw_Ed_yIdoTOLYAMz8DDCu67s_TEdKLWokLkvE0YPm1zjRAZY1BnzADTbhWunT5yV9CxAQ2jy7Hosbpg7U2DZRS53mgVFM5QbTcVhRv9FCUO2j6SK9weagj2W6cyNddY1BROMcB6N9PJPEs19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=UXK8YqbReEm-0B00e0q5NcnPdjP5Vks5-ytge3hDYHH6Wo754klJfwKIiSlcX6yEVFFdvykWUEnOXVtT1xDTfLpmhxKIHA1tVJXEmPEPEqqTO5iujz-k2gHBtv_hOrotoxJKWdSRPXD1DyY0a9n6DCUoO6wybNhWpGlyCOQpt4H3mTlsvGcbMG6aR6yw4qXyG1mCLnAfyMWAVEFepPDtLP5nuVJsjNXj8qNG2bYMCevW8yrH_QxazncQA3FveucB61stqSX43DL0eoZAlf1hBC78NamSrVtlKMO0PeD7rOS6_KwwMpsxBkV-OickM_pJA8VSP8YBjsw5ZZO0zLxY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=UXK8YqbReEm-0B00e0q5NcnPdjP5Vks5-ytge3hDYHH6Wo754klJfwKIiSlcX6yEVFFdvykWUEnOXVtT1xDTfLpmhxKIHA1tVJXEmPEPEqqTO5iujz-k2gHBtv_hOrotoxJKWdSRPXD1DyY0a9n6DCUoO6wybNhWpGlyCOQpt4H3mTlsvGcbMG6aR6yw4qXyG1mCLnAfyMWAVEFepPDtLP5nuVJsjNXj8qNG2bYMCevW8yrH_QxazncQA3FveucB61stqSX43DL0eoZAlf1hBC78NamSrVtlKMO0PeD7rOS6_KwwMpsxBkV-OickM_pJA8VSP8YBjsw5ZZO0zLxY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Q25LPsJ7HMvzkD5ciG0dV5D69lsAiOZfcvVx5Wzwe1_XZog2Q7MrV9wteZ8CCswE6djq_FlkeC6R26gOEXePceQIAeYUrHR9obEzTEV_7sadH3DelQYxHsYujK4fZq--Zfdsxrdb9wuxG0TfDeXIov5G7dyBcmoXtL29p-jlJCFupBJPoQv2BlTyMQA7pJal_VWO0tbbpCUamOqBD6A8xk0W0eIWMoWuGYu2ZKtbdb1Xke5Q_-pCrNBm97P7fXtZGZiU5_-bt_mdWb7Eci4b56IN68KkuAXrFjCae4LpIQZrGoVLaiSI84mzr2Ovl--f404Zmx7Yf6uZsPxwlPPvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Q25LPsJ7HMvzkD5ciG0dV5D69lsAiOZfcvVx5Wzwe1_XZog2Q7MrV9wteZ8CCswE6djq_FlkeC6R26gOEXePceQIAeYUrHR9obEzTEV_7sadH3DelQYxHsYujK4fZq--Zfdsxrdb9wuxG0TfDeXIov5G7dyBcmoXtL29p-jlJCFupBJPoQv2BlTyMQA7pJal_VWO0tbbpCUamOqBD6A8xk0W0eIWMoWuGYu2ZKtbdb1Xke5Q_-pCrNBm97P7fXtZGZiU5_-bt_mdWb7Eci4b56IN68KkuAXrFjCae4LpIQZrGoVLaiSI84mzr2Ovl--f404Zmx7Yf6uZsPxwlPPvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=OtTP_8djVtZzuitDzM6Gv5JQqIK1GLifgQq4536FwScBCmHNySCNfoX60aCJX_y8kNbZK09SeuEj7qFhYuo6FlMv1XqOri2AMAZ98N8ftbnb4vWtvnThNCoxyRdWWV-3wXau03FNeQQ3bpsRsx-GS5W5Crfd_479eE979mMOtLT3wBwymYEBu0Xx4M_sFChqReQ6-Ju7z-5RrJRE_Eim9f5RUl1PPp3dGYM6qo7LYtz7ofHzdIWZV08HXzMWHJhAUN3pvop7JIxSt-YYJrcChB-SgB23CrtK-A750yTwS0SxKKX6YSd9bvTnQZcgb9zwwcjCilRG7hhWfWXk-Twm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=OtTP_8djVtZzuitDzM6Gv5JQqIK1GLifgQq4536FwScBCmHNySCNfoX60aCJX_y8kNbZK09SeuEj7qFhYuo6FlMv1XqOri2AMAZ98N8ftbnb4vWtvnThNCoxyRdWWV-3wXau03FNeQQ3bpsRsx-GS5W5Crfd_479eE979mMOtLT3wBwymYEBu0Xx4M_sFChqReQ6-Ju7z-5RrJRE_Eim9f5RUl1PPp3dGYM6qo7LYtz7ofHzdIWZV08HXzMWHJhAUN3pvop7JIxSt-YYJrcChB-SgB23CrtK-A750yTwS0SxKKX6YSd9bvTnQZcgb9zwwcjCilRG7hhWfWXk-Twm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=gWfz57jDLlWoQQ5xPUWudC3Fs7M6Z-9BW7oHy-lKSIYAyVtYb3URp3UUthO2u1PcHuDTOiTybLlbzZekONo8pykVmKjBKKE-lWKHQCVxsohJF2nDOs6pH_jV9WlZInNlUw5nFVEVXbJnK_3tf61AG9dyaEX9Lg6kx9btB82VmC00CGsTq6rQXo9SPS74trlaOu4HUcISCkysmUsZMH65E4eviU7YKqIJ4H2-RdQYLfgmhs--yyMU0trSYQ1yO-OuUCfIQ4D4kkKUaxJQAtbJ9gOM8qPVWq1njCFzlUcU_JcpSpDi_N6h3fyG4a_g8qWFuGYbAybkQiZDpbY3AV5bxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=gWfz57jDLlWoQQ5xPUWudC3Fs7M6Z-9BW7oHy-lKSIYAyVtYb3URp3UUthO2u1PcHuDTOiTybLlbzZekONo8pykVmKjBKKE-lWKHQCVxsohJF2nDOs6pH_jV9WlZInNlUw5nFVEVXbJnK_3tf61AG9dyaEX9Lg6kx9btB82VmC00CGsTq6rQXo9SPS74trlaOu4HUcISCkysmUsZMH65E4eviU7YKqIJ4H2-RdQYLfgmhs--yyMU0trSYQ1yO-OuUCfIQ4D4kkKUaxJQAtbJ9gOM8qPVWq1njCFzlUcU_JcpSpDi_N6h3fyG4a_g8qWFuGYbAybkQiZDpbY3AV5bxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=RaE0-daTp9Vn12HlKPZtcV6sVGVRne_daCb9q4YY18wRAhARefQNINnhZ7pswxj1BMeYXKYw7n6SYdAGpw-lq2Ti4jODU27V_CDVt-ius9jyBxN3xT-ZJ824jzsqVeRkBm30eA0cfSu9ghhmvJJ8M__MTlhV-wSUWnuRu-3ZM_zalVfD_CvDygy5o8IWbf6IlY_P9I5Nfw7gfOsRog74no-iQ5PiknUIKSGNGa-Mu_Fosa8Z-7xXL5VbJJfRa_C0jIUjN4neGALIB_XLexk_Mbg2iUJZi_XAuPlhiyKvVm0Hvm5yERpoY6X8GTlFPk_223CdYWevrAsSf_8jChEm8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=RaE0-daTp9Vn12HlKPZtcV6sVGVRne_daCb9q4YY18wRAhARefQNINnhZ7pswxj1BMeYXKYw7n6SYdAGpw-lq2Ti4jODU27V_CDVt-ius9jyBxN3xT-ZJ824jzsqVeRkBm30eA0cfSu9ghhmvJJ8M__MTlhV-wSUWnuRu-3ZM_zalVfD_CvDygy5o8IWbf6IlY_P9I5Nfw7gfOsRog74no-iQ5PiknUIKSGNGa-Mu_Fosa8Z-7xXL5VbJJfRa_C0jIUjN4neGALIB_XLexk_Mbg2iUJZi_XAuPlhiyKvVm0Hvm5yERpoY6X8GTlFPk_223CdYWevrAsSf_8jChEm8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rb77ZDu56BtAgrvSHIR821yk0YBW445ijyfGVxsMZhCUI13nsbxaF8pBmvC3_biI09Y2YetewabUaFdalzS1L_LTlSau_ve05nC--SK73gEr-3PcsTxRDwC2keNCEdzpLfy-LHLi638g6S8DPTMKA8CUmGK6enOwKyLIC1_uofRHQ36EH_LQ8_5Kj-KfWTJ0F_NHsXn041IcGUy_75J39h4VwdXglg3Ls-_TV9Dldm_K42alB_h555v_HrbqGE4AoXY3N-E_cXDFzdfFmcDncTaiaFrv49YN8tzVbpf6z-N5Y-WZj6Oa39EJ67-QMmg8BZWg9bd-27NkVPzIGfSuRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VXKYFfDQiBJO_0pa9Jjh7g8phHjEof5VHUN933CRLqv4DAI8ufPXAZTIHwxYjPteWEphwDfa68NCJY1MUNDNXqm5YKEjzMGoNssE7SHI4RVXvszvm-nRtIxOIPj-z7koU8EykyHwdG18cJTVkdn17r0g1lTPHPr7yrpnX46r-lHNvzbWjYWFDsMAmuWU38RUqfUUN1g5-kvxaypDKfgHIqP7N6bNPxYlD8X5Yks-J0zoeCbHM7Ed2X-Wp6XVYUWkIX6HlsJRQll8-Djd4h0Oj6kImLH0doR2VlrtHQdlWS4kP92ttDhA8YU2cMfBYfUlHS2LnIR9XAEtMKAYI7dtGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VXKYFfDQiBJO_0pa9Jjh7g8phHjEof5VHUN933CRLqv4DAI8ufPXAZTIHwxYjPteWEphwDfa68NCJY1MUNDNXqm5YKEjzMGoNssE7SHI4RVXvszvm-nRtIxOIPj-z7koU8EykyHwdG18cJTVkdn17r0g1lTPHPr7yrpnX46r-lHNvzbWjYWFDsMAmuWU38RUqfUUN1g5-kvxaypDKfgHIqP7N6bNPxYlD8X5Yks-J0zoeCbHM7Ed2X-Wp6XVYUWkIX6HlsJRQll8-Djd4h0Oj6kImLH0doR2VlrtHQdlWS4kP92ttDhA8YU2cMfBYfUlHS2LnIR9XAEtMKAYI7dtGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
