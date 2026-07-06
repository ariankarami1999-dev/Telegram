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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
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
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=aRfQCNtzXLOm5HtXBMMd6iAZewy1TQR_olhJOMPfhfDEf602MXqtp_qzjz8WNXLCrH4ObHtZTKOkuQ_0IC45uzXcenj0WvVsYHuwTTBvFnYs81K6qGPOVNu6mnzJVjHkAs5sLEwORtOf2TxEEx1_P88Iw3VAQjwZ5o-cBlQ276emCkpvxq2kPWTK2pNJ_MABoHj6psamibA0sQrJKO05ovtSgHfwGbqS3ydzipCSLLnZ5NohmT4kUNkeRp0cFhm1dkVtbPn3JAsk16Rdch98OkhSObpitCPVcc9RscRIs-b_WoqJJmCX8XD81Aow5QdEB3yPIjzAIv1CXyWm-VkY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=aRfQCNtzXLOm5HtXBMMd6iAZewy1TQR_olhJOMPfhfDEf602MXqtp_qzjz8WNXLCrH4ObHtZTKOkuQ_0IC45uzXcenj0WvVsYHuwTTBvFnYs81K6qGPOVNu6mnzJVjHkAs5sLEwORtOf2TxEEx1_P88Iw3VAQjwZ5o-cBlQ276emCkpvxq2kPWTK2pNJ_MABoHj6psamibA0sQrJKO05ovtSgHfwGbqS3ydzipCSLLnZ5NohmT4kUNkeRp0cFhm1dkVtbPn3JAsk16Rdch98OkhSObpitCPVcc9RscRIs-b_WoqJJmCX8XD81Aow5QdEB3yPIjzAIv1CXyWm-VkY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=S2U-7H_ovzXFgNUpGDM9hZWir7UwD_-zMLUKIp8RhZj6o2BooR4J7LW0d-JXfiAtCKcoVwjVDm-mUM9fi1bvb1GfnG5Fcos40b7bp8v22_Ij8VbgB4iwYRvcODenz-8_J1ASY6f56Fl88ji0Bs4M7Tck4RsOR_Y_dOByWrL8NhgRGhhXSjMYhkmJ93J1IHchjmP5ESkFuvQ4SIsfEvH_EOuAz_4z_k-Edbwk_p0IgcNMRjxN0Uoc9AH7n2JdHwLhDfiRj9IDAPCOtuskXpTlO_0EQ77D1MeolbA-aHL2Fro2EIsCF96p2nAAp5ffsN2Mg99_IrguSdTspEMba3yReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=S2U-7H_ovzXFgNUpGDM9hZWir7UwD_-zMLUKIp8RhZj6o2BooR4J7LW0d-JXfiAtCKcoVwjVDm-mUM9fi1bvb1GfnG5Fcos40b7bp8v22_Ij8VbgB4iwYRvcODenz-8_J1ASY6f56Fl88ji0Bs4M7Tck4RsOR_Y_dOByWrL8NhgRGhhXSjMYhkmJ93J1IHchjmP5ESkFuvQ4SIsfEvH_EOuAz_4z_k-Edbwk_p0IgcNMRjxN0Uoc9AH7n2JdHwLhDfiRj9IDAPCOtuskXpTlO_0EQ77D1MeolbA-aHL2Fro2EIsCF96p2nAAp5ffsN2Mg99_IrguSdTspEMba3yReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPRtrGGrQHw922D5NOvpr1VMkfuR7Dd3cBn8aJICq2EhBDO-uDMqNw0c04U-4PEXH11-dkEhHyE9lCqGrTBvZ6U0xEmtXVBnXg7kHOXrWVWtUJUwhAqaOnRC8DiUtAXRMsL6X2kC2T0mJhtTsQJakAa9DF1i1jZEcU7sKz_KcUQW0qEFWG4wbMqvbqn8OD-dwFdu3lGpQyT9-hO57sjvYeHjm9zU80oLeJfo8N-6KPHXoraV9XuEoYwk4JZogm3fdL5XpvdBJ6PM0clDbDydHjx_MhO33nS0vim7sVtS-cGY13xT_CdhoHtLx-CSU1PB3-sDMoqOu8PW_yFkaEGojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9XmYWhuWL5lWa9cvTMUQL68R0sEol3P5pN8z4lett-_XW8R5wg51-vy0mZ2dHTTQNE89gSrbUbxgTWFKDS1wLsHdTPKlO7O_NSh1z-ssTTzi24don40dg18VCkVWq_fdSEoSr_s2W3zClyh4_BX9mAMptS2b3kGMAXoyfc-pYj4njZVGMMGoCy7hcHzI4OPhX37QtfxOj7XaqryhDZEhYVaNod9FR2j_jAuYuhSAc-UQdlNRihYQ3o2jkiZQHlHPRoGnZU2wHt2R2rMzhON0X3-uUQq9uqshIL6wWKClhVI8Tcs86ZFbDJPed1AdiLZ9_NTjgYQBR9mq21sZYwWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs_8ItVikQwmLxUMmSiM26zwRwt6DyIcmPwqetKcha6cjGeM87UYjAwdCVcEOHLhA62LfDKlukNClL_k20il6-M69ovqZiTPpoFrixCHygg9wmV09YULlDogOgkGHna4j1I--DVUNYpzcmm2I9NJ_2RXhseHxrVCETw0cTJp8HoXG4wdmmIZJpomg2NgZvHcTyqH2n9s5r9YX3JoS0hMN_rxIe9JE1-ibxI3RBKGoPDN5OpPUE0k82KSKfanAMwzhMn7xy18aLfGU4YzeyWsjEI_zSui-wVQJhNJ349mg-FRabFu5mkROgZbUMXgUKHK0wMZs7F7kwJBVJmtVjSMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v11lNDXsn028ZtUyjEI_gEg72PM6_BGil28rWFzTmndSZjXHnlgF2U72Pony_aeBLFHTPtEKAzGkEweeGrZWLrP6-aSrgoPubHOWrGGqOHV6FjV-ZKnh6cCxg072fSjKOhV7Vkc2Z2UCPvVu3oVwcpzDNA0nkFbWTRq9AoCH0yXdDvv-0cl6xkwpA527fGUF44UHPdgKxi1SH20MSQgAL1fdrZH_y5YH58FhsfCdd9Ho30oUnixeVEexqwCyA_MtE_SPykBHk5SW3LGMS2JNzIILYgYEzu5PNPjdDKwQbUDVOOQu62t8kJC2ybVAro2i-Y06GfV9H3kTnYqA7ztLbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsB6l9fIhasNZcYPOUDr74EWVsWVf4a2Mq75OCRL4R0-CjW69HNVIT6E4p09lwJhGeFbGG0LznbS7bxo-c9xzRgdLP406O86x7Y_saW4X1XALVx6BnTJF7Ul2UkBpGKJbrW91_oSBqgdV3BXu2ZqbefBsyCOkJD8xbrUjJhm-IeUFp72x21_TlKPooz07HdKBiQ64m_nogmB9xjVBBBbm3XeYKW_JL_iC8vi-N5h2kwOZUj3AvXWQOi0hB6Bnt1jf7HLBy2pqgNNzBz1I-D8FCCvmNBKZUFQKEOOmHQsJ_H0Up_E0wCLiNx_F4vHLh0OoM0qClFIP864aNc1r-xivQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8KYf7jrzrPM4B6Gu3UqkpYf2Deb7b2jSDihkUuQP52yjGJIjT3_EsuS_bDOvzwx2nMbIHdLqEDdoJCNnO_8nRIDGGT4DvBRJe3Ot1MXMG--SonJaf4Dg0UIHtk0-GEM1JkY3OCLIJXTM7RWgY5i56Ey9oJSSyDsmAvgy8PAa51gc-s_GzwWqZ2HPtzU_As20dQw-Hb5A9UqXgWlJwQWO_rThtCEesv2bkw_rxgGnY_Pf8xDlthnsdgHSXgLeQ8S-QITwBM4Ijw96bw78QInuO1kMdMQtDCOB7hMd0xXT41KPW3TCJys1F-spQCYKz8P4DHeYA1bm02tFdIh_hgFOg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=PMUGj9_1uTJ8RHriYra5Gi5tPYnzR2c3obfmUxk6jQ07ZSZgmRL0HshbmWuDaWo_pcRQ5pgldJ1xbCFlLCikxsYl_VwjNIDLBJPpqp5K1PVZP4oKmulDuaxWi_AlW4wi0PhPwFePrrvDorcT2tqlzHwAi4Z3eSPUwIGobLKFz5DBB9JY7FYDbMlVFJuESlWKEBuRs1rV4dBYC-v_DJePDNyZSpE0iN9Jf2P8XqaGEXwXkxxoHD7flpjuGWV9aZIFUwbFSeyDIlM2J1SGDS3NnSE0mjIpSn2_qt39CnECJPeN3_Y-sQaTb_jy-Q0j0lc6zA3vPAfJyKVtnL6MzDg_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=PMUGj9_1uTJ8RHriYra5Gi5tPYnzR2c3obfmUxk6jQ07ZSZgmRL0HshbmWuDaWo_pcRQ5pgldJ1xbCFlLCikxsYl_VwjNIDLBJPpqp5K1PVZP4oKmulDuaxWi_AlW4wi0PhPwFePrrvDorcT2tqlzHwAi4Z3eSPUwIGobLKFz5DBB9JY7FYDbMlVFJuESlWKEBuRs1rV4dBYC-v_DJePDNyZSpE0iN9Jf2P8XqaGEXwXkxxoHD7flpjuGWV9aZIFUwbFSeyDIlM2J1SGDS3NnSE0mjIpSn2_qt39CnECJPeN3_Y-sQaTb_jy-Q0j0lc6zA3vPAfJyKVtnL6MzDg_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=UjGQiFcQ-SryQ7nkmifQZDykEViibxwOKkCeb7PO1IXBvwH6WVeArngENwK1hh5d9Yn4hXNuFgJfKjbJsUm-iEYbiP32kEcRvcEJ2kB3STAU8gBS8S0ZwEscXiue-DnmTjqQsYzQGA6h4JW0uHKFzp7gC7wl3v-SA5O-pPQHVYoEdluO3y_yU7EYPR9PuBrNeAJr3RyySx3fQA7_e2mVw0HbvlShHTfD38gyshV9gTcz2ehazR1tC3KT8jFN0fXqti5IJyqancKtqmg2sSGK8srotIWcXK0-f-vymTKjDM9z-blmHEzVKW5kfI2JvX0ZwjIkjbIo_COxbFvGiX0YgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=UjGQiFcQ-SryQ7nkmifQZDykEViibxwOKkCeb7PO1IXBvwH6WVeArngENwK1hh5d9Yn4hXNuFgJfKjbJsUm-iEYbiP32kEcRvcEJ2kB3STAU8gBS8S0ZwEscXiue-DnmTjqQsYzQGA6h4JW0uHKFzp7gC7wl3v-SA5O-pPQHVYoEdluO3y_yU7EYPR9PuBrNeAJr3RyySx3fQA7_e2mVw0HbvlShHTfD38gyshV9gTcz2ehazR1tC3KT8jFN0fXqti5IJyqancKtqmg2sSGK8srotIWcXK0-f-vymTKjDM9z-blmHEzVKW5kfI2JvX0ZwjIkjbIo_COxbFvGiX0YgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=opOn99K2BOifikd-rzPALFeqmeNvpu-CsjapT0jKGZerZDDyTo-m27wGbl0JRqs2U4egyT7UQ7cSKTkBrhVo70aJhitW95kmhaoGjm5LowvNQQCtMxdLzdndFsvv6Z8uuF281z1k0k2X0FNvbcTa_o7IXpMMO17ifkLdlW2KsNcvzQwxcHbAXUY_fWLhbhZgxHiEk7aj7-QLy8uYvLuSDzZ1okCAujEiq88pnt9fvYix_BYp3gmazvRq9o5gHh9SJ9GGiTh4snV89XAsGP-RrHD9avPWQv4OrOhYA8N52fiN8qh6Yix5fqA_37zbO3CeRgVDQQRdrGJDSf1pUgLCQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=opOn99K2BOifikd-rzPALFeqmeNvpu-CsjapT0jKGZerZDDyTo-m27wGbl0JRqs2U4egyT7UQ7cSKTkBrhVo70aJhitW95kmhaoGjm5LowvNQQCtMxdLzdndFsvv6Z8uuF281z1k0k2X0FNvbcTa_o7IXpMMO17ifkLdlW2KsNcvzQwxcHbAXUY_fWLhbhZgxHiEk7aj7-QLy8uYvLuSDzZ1okCAujEiq88pnt9fvYix_BYp3gmazvRq9o5gHh9SJ9GGiTh4snV89XAsGP-RrHD9avPWQv4OrOhYA8N52fiN8qh6Yix5fqA_37zbO3CeRgVDQQRdrGJDSf1pUgLCQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBcpC3YI9HPdZgxV0XX_fiDDKu0QgRbk471oBXZys9cjnD4PC7jg3B6tqbjsSptbKLXkz5TlEoQI2yRzw6I5LzgPuYFeiguruVFTTcy96QQ934oIAGqQa5wJeh78BVLur_QjJ1YXzdKc_1o8121fj2v3oqfIG0kZrSZDxBblggkT0MPLI9I596Z3dS7KZ4VpX8W1b_fLsLzox-6U_5_3SaqlQMNw0Ep40BftQxmUVMKnnPw6G0v2rGLUgt393NtspfdiI0GyHLbbXKOdKDZ8WSCvQkxnWbYGuuW1xqEnXKcx3UhMbGwrEfC83IFdErrdgG7_7pNCiWhdavcsXx4l0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_Ii7sutQck1q1J1HPgkf67UVc6YpIhWMHNauBCGQW37MlFMQhlQ0w9TnPcUCy1tf4C4EZ_BmLuLCIQey6H7xGKSpS6qlYS0vlhbcommuDTDvtb7_sYMoSaxHsAAaXFONcUuNuUbateQCPjVYrAVUIWq9ItyGe8Sv-FoDat502VwzOMZQfYPqVC7ip-bYvY7F8JciYepdxXaiXVkmtJHKTQNgdWx69oBhQLhPORPnyYChtm06l0hFDvKZUnRhN0eq1KDZebQ2BVjso9LRQoDkdEeQpeQ0JhpxqZqv7Z6LcWPqqkQrNI5Y0B95_XxUvKcV1JNP83-oO9MAKH3G5zOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVPE1FU1Llk5oqzD6iuEVAdIw4Y_uLIToTWT_0ySw77zbjynRw8GzwLItKxjhND-lRnNzL2hjlheWh8LJH8dxZIpDoxpqeYC255AUb0xJ4AXnahA_K6MuFGllv8KWiKtyKBRcKVOMHDoZyOEU5u3JHKuyrGsHp5UrnXKskC9vjlLqmyanTsLMdA64ddhKL5Rw80VDTvIFdrK75RLqgF3W4LobKReNbxEEBpDH-Q79rktqG8MiJ_bd5l-x4XA6YqJQ0d6vaKyck_MJQ2DCx5aE3dlWjnWNubb7MKYT6dxT2eJdYwwhclDsRQObvpj-MT_nPETW2KP0g_K_SuxAEpCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTzd_k-V5l0Ok9SXiGulwktzNc48yB6di83icp8nWxXI9lYZZai-l2WBqDuM9RMtO0DoaS4UzOIrWgg7ZyQzzh_p6RGZ0s5tCKpC0f3RR7gUwJtQQ9-8d8o_batPn2-3xRfCTpUQLMKieGyIOto6LQEhFUFzurUPH5a2Hz2yMAxVSrQEQnkpWb4_u-X0JpP1r-8dt53W2PpXLe-E5d2pkPIX7uMBQziNDi8mn5eowt5fWwJuZZT5VsrxsyEwhCMydVyEim_ANEGHUsFUqR0K-uz4zi9cYCTQv0NMSTn4mMkRfRmY1NEQIvXzmsIcRXhK2chACAqNogiNxdgShhJEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkVgrtNnvNEAc66JsNrbQslunoMdWzXN2jnn-LC00Vxc-DOu8DVBJMk3VFQqZYDvVzmGNgd6mVyNlGfXQTVsX946bKiOZs0TvRqWNQL4LbvxvV-1FHqWivucroWImJCQ4wkyVfxkXqa2w5D1ATnzAUsg-G4MY-2cN6CItPBkT_a844PUxnUs_5cxdBCPxmiPt6iujY-oG3M8ACwNLYx2KRv4feUftQEenlB7X_1kzNr4KCGrMumZFMtev58a_i05FU0Cx4w5npMJhES71by9B7QiCWohTKtVY7QRJM8XUC-mswGD3aVpAuraS4THe94ZIh3KmtqhRAr4vyh_qDj4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyuB1COS_Gv2a8u9Z9dd_kH_NyzHzF0h9bJ6PmjpyX4EX3-euKrlvu_v5gdWHIvsRbg37HDCCe-InR1Bm5as_NufleijA7m8CVYSdGHl_Keae0YWmD8TaRHoGuxg9TrfV8uqpq57AUoMTnbegYp9kZlvK0Ph1aKJBsn5Hvy1iq68nkI75IJEoYVP1kW1T-iE_ywab5BHdIy62vOdtG5WT5Ws5HtL4MwjeCZwze0Q2UZ1oo2ULn3pXpc1ICMaTHvBK8FTjGKBJAlgoo3UC0vUnkHklZm1UrvJDFiNnvx5UFyv3eEOUr3EKIvJ_bFEw5FqES_iKK_SXdy4mPMMpsFslA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn2-k432StLNiuo8aZPby4dCCTr2N4QWo6is5xxl0eWbc2a8dAzohKtfkhfjzNVywbSu3fgxlp1uLTj8QBGV8B-vIi5WaoArL5thLwdtFFXgM29RQTY0JjWqdVQOUcWewqsdmbGu9D1ay4DfRK6QojBd1ipa7jARTgO5G9_DgmE8cMJsEaHIAmF9HVkr87SNEUqRYCWAitxZ1PTHSkkxrJB1YlyNXNtxuDe1WQ7eigNHQAQUa_1oVyGkMVYDN_DSy7O5Z3q2Dxy4RPU8Aoea9gXCB8-kP6rUuDwm7z3Q4-kbO90ZyFolAKlb0m5xeY0ekr9twrwOdwvDBE2jSm49yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UokGPATdhsVHaczI7uwRMahueDatOKrXo0crPys9KhkP6ycTVr6SYCVn3293q4DFAb5o-c3TQ-9gbPPI_kOdwNDFkRIBiHYbWG8g4Hv-XbntTkl-UFaDTTliZ_MCRdM67sHLEyQHLEPYJg72JR_oumfXw3y-htvvZpqL81nkHAqjZ51zRn_uora8Z4Ic__TcOzRZxtS-TVEcH4VEGKAOCa-osLSEI3G3_6czLtmj6_d37L1Y_AfRqbR7Fc1E9jZ4FtMMWGyYW2hUdhXHWMcPDFSInZLtPyqVomdezqEGRviBV_utQcBMR4Q-DJ0YZOVQnDbR0AJT-ifMkTTy9steQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObKQlCr8ibpxVpwSg_wfz6wyMGGJ_DiIQQwwpUCuM7_9AmaHWEN1-nqUEmPSgSw00Ce7w7wrQJQelsSvzoMrQc2994AddePeEatWOX54DAZ4WO6BPN6J0v1sqF5J-SR7Nu--kvAo4fT_NP7VLdlhNuwIxqTINiiTicMrnpHdkHUSAGisNiMtVpB71YuG6b6nmo4v2i4o7BFpq6NMUVHT2l9U1VDLK7VnQxs9K0mbVXrSl8Ovx1fpxWVLCmKHU51qxfzzXqxn8KILRreioA-a9dQo69_mwXLygusCt9m4nY810W5iyHSu4UjGscs3G4cd55uJnb7H3xjTcICst24GZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxlY230H1mTZ34Fdz-vrdsb_WwJr7cBcYZ7_ZqEDZzpHEsDvNST12T3jHZcSay2BUs8a8qqOWosmJLomT3EQsdmdGBrx76ToGIj7Z6bpdPiwfhRs0qnjBPVxc3tfael_O74t6jHYEQf_CVRFSLoqINQPaYiG9_ztMiQi5v-Nu5whOuR8aVDy0QSo7ITkcZTI99PB0WbDvf50ctOwLedAIekK6i2HKQgmAtnIBVWg797539RsRbEnIiX61xhsaBiZHA-kbAHddmHcAs7EBo0z0GAV_ZZK3YYPQ29BMAJQCYscyQ60sRmPPDVL3FKuT90-aN7_1DUfZOR8JMM6brxCAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=hoyeTLFI1r7ZKsk7qGPBize84cpKx88tGASeKV-F9cuaSS9bpOrI920m4qbOYv8UgcxvyvfL3kDdBYzs1b86M3uWyKEwBNSk4JaVpheZ6lfI1r0Zr_XHwFS71tML0hoIUPqMNCf49tt_YGsqbRs7Z5I4hdJG5VMm1ABDsg9xg7iSF0x5xHv8Ahk4uK-olzpq73sA56OCQ1rrnGjQtY3qS45zSOCJuyqWa-Q0RLcFRdn_386YrjMDR8AgbXXUjWSYVokU_BlklNwf6odJCvrSP6zyzZqe5TFkrTkqHvI3qBC_UjGQnUdqdIRSoSdqUHbrr2Oy9YT_rtkYM21oNn8h5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=hoyeTLFI1r7ZKsk7qGPBize84cpKx88tGASeKV-F9cuaSS9bpOrI920m4qbOYv8UgcxvyvfL3kDdBYzs1b86M3uWyKEwBNSk4JaVpheZ6lfI1r0Zr_XHwFS71tML0hoIUPqMNCf49tt_YGsqbRs7Z5I4hdJG5VMm1ABDsg9xg7iSF0x5xHv8Ahk4uK-olzpq73sA56OCQ1rrnGjQtY3qS45zSOCJuyqWa-Q0RLcFRdn_386YrjMDR8AgbXXUjWSYVokU_BlklNwf6odJCvrSP6zyzZqe5TFkrTkqHvI3qBC_UjGQnUdqdIRSoSdqUHbrr2Oy9YT_rtkYM21oNn8h5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WwMfAgy1b7hZRhfTpgw1Xs0JZAMOp6qcESHaqMTJ0NNjRYQZi3UJOyvg0wNNBV-Or6zKFDlbvcVvoIEjvLTosG9pJRaVlyKJ5csgLBVTYENc5TXjBY4Z-C9dVeXIw8fRLWgrzn9VLUwrt__FJG57pletD0v-E6AFtqveo-JXxJZ8hvI7kAoUYnZtdn_StRHbDXPkIgsjsOc3YJ0tvPx5ydFXEXU3oZQ_K7DhZXHPDZeD_jahZCErrYbHj7_YVebFs-vZKWeeH4NFqh2KwmdVTZe2qf7L3xDEXnBvcO84MH3IPVKgyG_Wf57Bdq4ZVExQcRkNrV8sLQSkdK6zsHDkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WwMfAgy1b7hZRhfTpgw1Xs0JZAMOp6qcESHaqMTJ0NNjRYQZi3UJOyvg0wNNBV-Or6zKFDlbvcVvoIEjvLTosG9pJRaVlyKJ5csgLBVTYENc5TXjBY4Z-C9dVeXIw8fRLWgrzn9VLUwrt__FJG57pletD0v-E6AFtqveo-JXxJZ8hvI7kAoUYnZtdn_StRHbDXPkIgsjsOc3YJ0tvPx5ydFXEXU3oZQ_K7DhZXHPDZeD_jahZCErrYbHj7_YVebFs-vZKWeeH4NFqh2KwmdVTZe2qf7L3xDEXnBvcO84MH3IPVKgyG_Wf57Bdq4ZVExQcRkNrV8sLQSkdK6zsHDkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=oyD2XkVNSw5OGDsyhGwNVdt4E11OiyLr-xw3Q-na12rgSIH0Y8o8lgufyxH_iR5wCH_tVai1I1pz0Bx0xGNPqZtReTtcr-oEs-MNdRPVoXN88xb_vX3zAglg5HG8ngb_HLAPc3FhUczGHzrI4_jE-DY3YBfF-ZSwz92dUzKQkLzETouRhc3trGA7lHHkOqrKfm21qoi_O816tSi5sc47PQsKpWTw9RPuajdmzATrlAfQ6yG4cVUKZmUtUdXpwmdeD3UJLUhuhOSFEHBmxkSlL0s6EX7thkxUZ3NzXWWt-04zekRjwoZgEOQbsbu9FufdR1HlAqD2GrWzW_3CArVEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=oyD2XkVNSw5OGDsyhGwNVdt4E11OiyLr-xw3Q-na12rgSIH0Y8o8lgufyxH_iR5wCH_tVai1I1pz0Bx0xGNPqZtReTtcr-oEs-MNdRPVoXN88xb_vX3zAglg5HG8ngb_HLAPc3FhUczGHzrI4_jE-DY3YBfF-ZSwz92dUzKQkLzETouRhc3trGA7lHHkOqrKfm21qoi_O816tSi5sc47PQsKpWTw9RPuajdmzATrlAfQ6yG4cVUKZmUtUdXpwmdeD3UJLUhuhOSFEHBmxkSlL0s6EX7thkxUZ3NzXWWt-04zekRjwoZgEOQbsbu9FufdR1HlAqD2GrWzW_3CArVEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=rq2GvSXipXe0p3Jy4fuMbJH7wSaDP1EGAGQjaBvBdbN003qN_zbzHV3DXRU-ycjH1kjoT-55KKnTu0WzRWWZMUrZ-rIkX06YuBk0GjTpejKF8_fRkxZUdKfer1HEUVqyYoZbEzEu04y0OoggATc-o-JBCaGjFHXr1Xalx5wxFPqdxBU3pZuikMfOJYJJjcGtknGWZ8fLZHiB9sqO0EzkwSrtA5nLPwSVrvjgT1Ag2OjNDTvu9O9pFdDWb2VQWOmHpNxhIY1kUg1x6BXMJixqYrdnB9A9_GFz__-BQwoIQR2SpZIsoezsHGDgIKE_l8mvIDVnWpT1TmZGA1olIW3w3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=rq2GvSXipXe0p3Jy4fuMbJH7wSaDP1EGAGQjaBvBdbN003qN_zbzHV3DXRU-ycjH1kjoT-55KKnTu0WzRWWZMUrZ-rIkX06YuBk0GjTpejKF8_fRkxZUdKfer1HEUVqyYoZbEzEu04y0OoggATc-o-JBCaGjFHXr1Xalx5wxFPqdxBU3pZuikMfOJYJJjcGtknGWZ8fLZHiB9sqO0EzkwSrtA5nLPwSVrvjgT1Ag2OjNDTvu9O9pFdDWb2VQWOmHpNxhIY1kUg1x6BXMJixqYrdnB9A9_GFz__-BQwoIQR2SpZIsoezsHGDgIKE_l8mvIDVnWpT1TmZGA1olIW3w3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=i7jLX-nX0HMs8x9kagW3FZ_Y--hdE0OJzLiNSresZe96RWQd53tKPb6kL5UWQdQV883kHGgMlRP12GVzZcgjnSqYRQQ3jhU9bq1OTZbjwEWcewP_Am35OgEORMdelX3vqe5_FMuYkFNVTIw-9OIMXdyQzKvWaXRk9kR5PCa-t1AlfPMbwwkwWYv1e9XAPbtf1MNoou80yYJeQIehuUiWY2PgjS9Z0tqsKB_qQIOa28PyF32-TEp3gH0ok_wxVGTA_-thn8UtS7sJx9uJeHDOS8X1wKI3hGLPxQR0VUoCU_SldqwZwWatuKNrkenP2Vutvv3dLRlX85QA5XmXFiXL_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=i7jLX-nX0HMs8x9kagW3FZ_Y--hdE0OJzLiNSresZe96RWQd53tKPb6kL5UWQdQV883kHGgMlRP12GVzZcgjnSqYRQQ3jhU9bq1OTZbjwEWcewP_Am35OgEORMdelX3vqe5_FMuYkFNVTIw-9OIMXdyQzKvWaXRk9kR5PCa-t1AlfPMbwwkwWYv1e9XAPbtf1MNoou80yYJeQIehuUiWY2PgjS9Z0tqsKB_qQIOa28PyF32-TEp3gH0ok_wxVGTA_-thn8UtS7sJx9uJeHDOS8X1wKI3hGLPxQR0VUoCU_SldqwZwWatuKNrkenP2Vutvv3dLRlX85QA5XmXFiXL_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=OREGtio1nFQsL5pqh3irRsA9WRHBcaAI4EzgzL0F9j18dz2Zlc5_fTuKqWlFtThUU1M81FOFPfojxZaz-t8GH51RGFqV-IXfn-mNeqHEznaDiWE2fb5HOK_5BSEQxRzxbIAlV539yF41zisCjfHReWm2XtBPIorsUy5RHc1BTa5g27ud2o1qO8dplsRb-zfs32rsTHyTN-8wTGCsOJrKIZBW58azfSDANZTrFN3hiJ5WC0mI8oJb2mPE8fzrAbLnY_4bDyuZZIunLViokRRjrT0vORlyDoRJc5OH0vzBsEMj60MkRwptezaDCj5XSRMJ10oj4f_uPdP-RUx4NMknDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=OREGtio1nFQsL5pqh3irRsA9WRHBcaAI4EzgzL0F9j18dz2Zlc5_fTuKqWlFtThUU1M81FOFPfojxZaz-t8GH51RGFqV-IXfn-mNeqHEznaDiWE2fb5HOK_5BSEQxRzxbIAlV539yF41zisCjfHReWm2XtBPIorsUy5RHc1BTa5g27ud2o1qO8dplsRb-zfs32rsTHyTN-8wTGCsOJrKIZBW58azfSDANZTrFN3hiJ5WC0mI8oJb2mPE8fzrAbLnY_4bDyuZZIunLViokRRjrT0vORlyDoRJc5OH0vzBsEMj60MkRwptezaDCj5XSRMJ10oj4f_uPdP-RUx4NMknDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=IKJJfTMHI2_5fkQcMifpxW0wkai2P_GxQcPCjcHXPlvW4I0zsEZjekU9FMq7LY2_WAr7bQ-0BtWXxMApu4wV8TGXEXkf00m1vk8V417FMB9FEYI8a49QuszcED_RLlhAj86ETpaQ7wPfM_j54rEzd8b7gY8R4yT6iA6jSTrpP2OVTtbzS4Bh53KoNvCbrePEmyjiX5xLlBu2pnnQW66Y5pe4WF53cOjuopsuy-tFCdE01P3TFvxWlRYMxgsjpWcdiHW0ARvyBI1T1zC1juBemBv9acrlvT8pzdW_Bwq_SlwKM4UIpZNxVhoX2nOQGL9FaKN8XSy52jpV364wcpFXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=IKJJfTMHI2_5fkQcMifpxW0wkai2P_GxQcPCjcHXPlvW4I0zsEZjekU9FMq7LY2_WAr7bQ-0BtWXxMApu4wV8TGXEXkf00m1vk8V417FMB9FEYI8a49QuszcED_RLlhAj86ETpaQ7wPfM_j54rEzd8b7gY8R4yT6iA6jSTrpP2OVTtbzS4Bh53KoNvCbrePEmyjiX5xLlBu2pnnQW66Y5pe4WF53cOjuopsuy-tFCdE01P3TFvxWlRYMxgsjpWcdiHW0ARvyBI1T1zC1juBemBv9acrlvT8pzdW_Bwq_SlwKM4UIpZNxVhoX2nOQGL9FaKN8XSy52jpV364wcpFXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6RUHiaROOTBJYNNsT_sCv8sLBvyPvyFlx_9zhMoh-58-DBjdsVU7olNRmQKguYdh0VnqlogeLAd5hg72pwa-SXtaio_tyHaMQls06xOH30GCQHriuHi45hV-Bm3c1wA_1AtQetNMfAPcEiIqv4lfEOVoZAZVavNwq2-0SDuf5cBHdbFRTF2nzyg3KEURTx1d4EQiMcil6-d4Xvi_aovl8CEp1CSnxRXnAsyI6EPVmnyMOa5o8RiWoDGUJYSdBzHQJXoIhB6ecjZ81j11t2wX0QIdHDZ3inHI4CWtpLWpeIEmy205wf-7zgYnFhgtDymc1d2JvFpOa5V2bGAq-bHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=g8TOiivdOsrQFVazyciFpSitT8K12jd9sdbGSBrtHogfZRO1TzQvQ-1d4Oi29ixKC6cD3fc3az6OCy5X2NyCLThjWlbxPWgJFUXKhxzBWWVVuZZ1nyNq7pH3WJ7XqfkjuAmp7yz0alWlC1JU-_UxwbiLfXw8LhPP9jlIaZBApo-eajFSsVAGInMyXQif_9iv8xikeUDlslKl2l_sr99mGYffXS7GN2S6JxHcFl5uO59LjrLW9pyUIgLtOD6GP_Wf5Lfd7NQe7MC7TZU66uQS8sLPBJQuPzQwEgx-L46B8ntN6SpGak0VCf-AujNHrPqUay2pqff4eQnnH5BIj2XGQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=g8TOiivdOsrQFVazyciFpSitT8K12jd9sdbGSBrtHogfZRO1TzQvQ-1d4Oi29ixKC6cD3fc3az6OCy5X2NyCLThjWlbxPWgJFUXKhxzBWWVVuZZ1nyNq7pH3WJ7XqfkjuAmp7yz0alWlC1JU-_UxwbiLfXw8LhPP9jlIaZBApo-eajFSsVAGInMyXQif_9iv8xikeUDlslKl2l_sr99mGYffXS7GN2S6JxHcFl5uO59LjrLW9pyUIgLtOD6GP_Wf5Lfd7NQe7MC7TZU66uQS8sLPBJQuPzQwEgx-L46B8ntN6SpGak0VCf-AujNHrPqUay2pqff4eQnnH5BIj2XGQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=c6qqAil2EyDPAyw69lq4s9XhpUNnBigXboYyRibGBGAwRFtfaaiY0mVwYKy5-JSSBhYKgEytDJfPBrseNndPWg7nzxX5PYamc_I2adUi5ZGsD5m2mWc4h10vluiRnvdgeyji8ULDE0Qm395kR3T7SCtNNnW5EqyyTYBXX6kBuAb_sqBM20Tk43dT_6OlAKlw-ruYs5KU0AjIVcOkd3t2zCJtwYNoVBlC7_MxA60sx0mLvLwaJJ7Mni7iz-giVwBCOpfM6qysP1qbe_n3ZyhsRlhb0FEUSZC-GFKe4HMkyX0kJTXKe-dppUawJlCOE3z8-gOsExutkHN_ZrIlNqwQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=c6qqAil2EyDPAyw69lq4s9XhpUNnBigXboYyRibGBGAwRFtfaaiY0mVwYKy5-JSSBhYKgEytDJfPBrseNndPWg7nzxX5PYamc_I2adUi5ZGsD5m2mWc4h10vluiRnvdgeyji8ULDE0Qm395kR3T7SCtNNnW5EqyyTYBXX6kBuAb_sqBM20Tk43dT_6OlAKlw-ruYs5KU0AjIVcOkd3t2zCJtwYNoVBlC7_MxA60sx0mLvLwaJJ7Mni7iz-giVwBCOpfM6qysP1qbe_n3ZyhsRlhb0FEUSZC-GFKe4HMkyX0kJTXKe-dppUawJlCOE3z8-gOsExutkHN_ZrIlNqwQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=VQkUqJEi16VFW9npDP1-KsA6a7DZu-KZG8xlYfyShvz90Mu7nhwKkLWtMy443F2GjElgtFAaDMgtVAG1m49wnFTpLB6zxvcj3kDHtwr9f-eSlai9ycGcLjAlX-ba_X2qyxZ7_jJWZ86OT0wkB-O9RYPTKbLeQKOJabWGbQHzlqSAVkq939-ce9vSFGUGRtQcJVJv4LBAgwfQhDpRBe6FX4lRP7A8M9_YXaFODta0rgrpiG1z8aUrTHyUTeNQ1Y0Y4JbIFh5cwT0aO9W4fLP1jSZrB57GsmBHj12VMykisAW1HJ-mgspEhVbnYA9_PqD6dk5aKn-ZgWO91GEB8Bt-0w0xQTS9QseuwNeLymnVgD5aaQ-JoDoaA7qa9KHzJhlvIQKgdip9hHbP69tv98t49T_BMobhENF6czLerNBuviEhP5JafTHDtkGz91M6e1i8kZ5np5oaYPThDgRHPhCCTgx70NxP9qP2Wng57gK3POnewLr5TmJMno3KrRVaAWq0bNgu9xGFDoTMM8x5soOw4wrH9OprFeip6LBaU2rXURCCgwsQ3Oiead0mn_B-cj3m-uzwcV3YFbd_ckZkVa2yQVJHQ4KGe0wEX35TfOO5vZqy_17Y2L50v7DwH0A3rzpPDmvu-czFXPOHu4LmX55nwIxbaOGP-UM7sZljGjzVrl8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=VQkUqJEi16VFW9npDP1-KsA6a7DZu-KZG8xlYfyShvz90Mu7nhwKkLWtMy443F2GjElgtFAaDMgtVAG1m49wnFTpLB6zxvcj3kDHtwr9f-eSlai9ycGcLjAlX-ba_X2qyxZ7_jJWZ86OT0wkB-O9RYPTKbLeQKOJabWGbQHzlqSAVkq939-ce9vSFGUGRtQcJVJv4LBAgwfQhDpRBe6FX4lRP7A8M9_YXaFODta0rgrpiG1z8aUrTHyUTeNQ1Y0Y4JbIFh5cwT0aO9W4fLP1jSZrB57GsmBHj12VMykisAW1HJ-mgspEhVbnYA9_PqD6dk5aKn-ZgWO91GEB8Bt-0w0xQTS9QseuwNeLymnVgD5aaQ-JoDoaA7qa9KHzJhlvIQKgdip9hHbP69tv98t49T_BMobhENF6czLerNBuviEhP5JafTHDtkGz91M6e1i8kZ5np5oaYPThDgRHPhCCTgx70NxP9qP2Wng57gK3POnewLr5TmJMno3KrRVaAWq0bNgu9xGFDoTMM8x5soOw4wrH9OprFeip6LBaU2rXURCCgwsQ3Oiead0mn_B-cj3m-uzwcV3YFbd_ckZkVa2yQVJHQ4KGe0wEX35TfOO5vZqy_17Y2L50v7DwH0A3rzpPDmvu-czFXPOHu4LmX55nwIxbaOGP-UM7sZljGjzVrl8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=N24ofbgm7LFWjhInM0sVwpiq-PyVWlPHbOjNknN_66tSiKFJYi2ParknF_DYDgRlVFNm0VZDlApLjEMHGK9Y7-8o5ielOjntdGobowX_Cdf1D1E-jiJATzP2I8V_HEKJaYYGa8DtYPRvbOwqecPG404Idj3godDYbrwkNCaPgQJDHju3pcHiJJFrZG1Q7Gz7IWoBdYkBX_GLxiGTFwJGoRl0qi7qsaOZ2OZNfGCSbFLmqAK-rKXI6tCC0tj65flpNL78edsn7JcJJycDp3YX19ew774xmaj6y04WZXhufP5JEdFG3acwWTnEB_MkimyXcZ-SMET0q3hYjwDuyZSfUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=N24ofbgm7LFWjhInM0sVwpiq-PyVWlPHbOjNknN_66tSiKFJYi2ParknF_DYDgRlVFNm0VZDlApLjEMHGK9Y7-8o5ielOjntdGobowX_Cdf1D1E-jiJATzP2I8V_HEKJaYYGa8DtYPRvbOwqecPG404Idj3godDYbrwkNCaPgQJDHju3pcHiJJFrZG1Q7Gz7IWoBdYkBX_GLxiGTFwJGoRl0qi7qsaOZ2OZNfGCSbFLmqAK-rKXI6tCC0tj65flpNL78edsn7JcJJycDp3YX19ew774xmaj6y04WZXhufP5JEdFG3acwWTnEB_MkimyXcZ-SMET0q3hYjwDuyZSfUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=NEu8aMfdug45Mq3TP-2dLU5R0xLZ7OYadxfoJ630R_w_h9GgGiOlOx02ZmZoIr6ZuChbk7Yp-fowWtItNY6RhvCFwzJ8lDIoqDSxN0DcAR3FVhLlXWX1eD9r8-tk81xlqg3N6WPVKjZRSrfwWdaUE9y6L-hiA-g_Mx4DiewXOFvhZ1KRHV8-k0dy7XVZUvwZKPb4g656rC5L-ynXHdvzN3NJzfcg2W-WV2pj717PlWwgz9G15AN4NoPGchDq5_7_XPvtC6H4uJtmTMmaIww7bu2FJNkDYPRn79F3ul8cDsmqHDMy4Xry3V5mC_q10MlMVkKyavU_H517Y0W1GBBuQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=NEu8aMfdug45Mq3TP-2dLU5R0xLZ7OYadxfoJ630R_w_h9GgGiOlOx02ZmZoIr6ZuChbk7Yp-fowWtItNY6RhvCFwzJ8lDIoqDSxN0DcAR3FVhLlXWX1eD9r8-tk81xlqg3N6WPVKjZRSrfwWdaUE9y6L-hiA-g_Mx4DiewXOFvhZ1KRHV8-k0dy7XVZUvwZKPb4g656rC5L-ynXHdvzN3NJzfcg2W-WV2pj717PlWwgz9G15AN4NoPGchDq5_7_XPvtC6H4uJtmTMmaIww7bu2FJNkDYPRn79F3ul8cDsmqHDMy4Xry3V5mC_q10MlMVkKyavU_H517Y0W1GBBuQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzH8A0NJ8fcmEquOrwkToyyWXgXDYauX_NC4TF7X60vgUanDlDxZAH9dhaHmdYzjwM9rZEW9IZKn0Cxw7w7aDCFrbSmLBK6Op5iPMn4mHVcKbFDKl4cvvX_mGu2NAcgnUkx1a4rlKkmkA4CbL8BwlnFe1CL6FRontIMabJFh6_maRg76qHXNDnBuM7cqW3P20kfcSVlBiAb_zisByuAkd2ejR3cROZhBTOEx2bepWrRuBw_z7bmRUxW1et6mwLFUNPkxhnkqh3u4uugvsbx3EylfO4miMIaB0MBZRkI-JrLDV1S0GrkwYQzqik_zTNzV3MjYhHw9yFzjc4JEWABBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtUFPUXD0McVh0Ce5Mr8xp1e51KLnmr0_PAJnqLgRhIWxci4u18t-wGRfuoKuLsQhnLGq49a9wuHVOtIrBgf4rezCiVUvGO4QGgdxoIjc6AZbZON6Kn0R9Pxu2ns67rquy8gTTJlOGI_Rw9RUkOWUS7vLfLZ_Lfcwqsu9sVyhiXuVQwaFK_Anj96eloLeaquigCwCOWAwCc9LpywEwyYEkOD_fEaM6xiMSQXCgf82ad9CX-FMNpMAacepKJIQbms_0F41P1dKSBGI_2RYxUYSFQbvrT9hWPPUJI9xYvso40EuvIrQeKW3BWh9QbBVg-P-9WV0yQ96f00sVF7o7BX4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EOjEjvmoEDWgkljjJR2ORzFqHm6mMa0VGRVm2dOUmNO9Dg4YaQW7kCb-dWrahJJl0qUNhZfkYlrjveDE95lAPq1KzaoN5CW2wjFeGzBXcHqUGxKuH9dndwuwWffxgQqsGjEuX-zcn1YdSsGIoX3bkbN4v3ZAV5eNFi3VGOdChYcCm_1j-4DoCDSX2--8avv3gXxTcTsdtnqdonRWpZhrw0sPJkoi86fAQ3dh-R8uWpTFPgtMWFXdEeDq9Q4HwS6QsH0BrTfaLt2d1MhNr7jEy6hnrDs41doIdbrSzlhPeT9KdoQ8IbqQvScFSe_iUcjLUMnkJed_EqWUT0x18gms4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EOjEjvmoEDWgkljjJR2ORzFqHm6mMa0VGRVm2dOUmNO9Dg4YaQW7kCb-dWrahJJl0qUNhZfkYlrjveDE95lAPq1KzaoN5CW2wjFeGzBXcHqUGxKuH9dndwuwWffxgQqsGjEuX-zcn1YdSsGIoX3bkbN4v3ZAV5eNFi3VGOdChYcCm_1j-4DoCDSX2--8avv3gXxTcTsdtnqdonRWpZhrw0sPJkoi86fAQ3dh-R8uWpTFPgtMWFXdEeDq9Q4HwS6QsH0BrTfaLt2d1MhNr7jEy6hnrDs41doIdbrSzlhPeT9KdoQ8IbqQvScFSe_iUcjLUMnkJed_EqWUT0x18gms4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l44XlH3VRRmbn0wFqLc6_kXO6APYNN67uLPOHufoZGXfHW1HDMlVWmd_Bqj-NWASl54glAYQZafdavycCUNueog30MI2prAilNz07DoQkjjjm0u9bteMwyPVdx0uwEr6uArnSLmTho90u-s9hIY0y41CZOf_VvjUyH3MDzHmv7epeaPqxX51x6Pdb7XOu74JR15QP2sezi1TCYUn5yrpQxXHiZrFfe4lQmNJ0L8pP9mPhCnqqx3HclXTmOMBNz5MT2YHIqZlayp_0Jn7SfBzj3QGGUDjm60mpwqLIHxRkGhRbAr0wz__LhBVSoamLirAm_xllqMlwXlZMFvIjLeuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWwUK0s0dQ3q_soSbkNsXMYCM8GxKjMFump5Tv1dyxLeYTUC-MLybS5vaDWabcBYYNlp35RONn0aC06ePQg_PO5wd70hwF_5brHbuIuZn8_qtnzk9g7CIMemLJmH4cZ7At85dsxZ1FTK_eJGARXww7NKu2G3OZ_g_CxvajCyNvnqDHnmrvm8MjgA5NaF7au8A808f-mYWYlh0xWp6zVUti5ie_hvjXu51Bj7cuDql-POduFJljXaFZ9HM4IP-h9wxYdQhUnySGUT9Fh_7_iCP7SgtS041jM-oBXFtxnMW_ciDjvESlpYF1z-6PRs2JVbNgdPJlGMCHY77r2xMtU0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UaawpFF50OLgLpbjndGyHpsnvZA01osUTR_nV5RrCOl-U6FupMYd5UMNgVq7y1nR2bOPGRy1NhBf6uQWp-G-zReKp-gYldp0aKLMzK7GsqpJa4nKnzxKTkeWX0zhvz3yHrw-Mh-jizK2QG5G2mTnFE8ov6zDfLxZsXpjU0BQ0USQW9_sQZQNaHB-Xsl-XIMMxkMHg3db7hofjOHEPHCdh_JAdN6izdaNKC-MIZJYNNIFEAxAFtBTEtuBLOUzbjQj73FQB0XXwkNyVHdZBf2j5GclcxxRlYhrw57MzBjIgRAPErx4j4n98mnZRmWSbhnodkU-b6HtGHlG80GoAOo-FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWkZok5npnqNWjUsaf_MJx_Vzj8iZDkyP2I1GsxZ_wrSxZmFdBlQxNkzfDOnfpS3i8_QtGs0SotAGp-MjWwUk1YZMNJCP8wXgJ5Plps1dNP6CSV1w-1JhuFoHsnEiee0g3UNgzfF-GHFWcvSeqksnG3WMqJ9d0Uwf3jXRFDFmuxt-PJjEvSljBT1j_xoxA7VYr4wb63_jNoecDIsuhRKDoOJCjAVq2sjoBb2ezSzZr4YpxZU5o1GtLV8p13fiFLLWWkE1uoe6kuPfRvHwZ5gWnzjjK08cVxAuAxokCqTeK6t8uG0sFJJi-vuRFUIrWqlawk04QIYdPY_PJtxnwTZQQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=nGNJAgYpd8DibqjXG7E-Stpvpdvt-d9Xh2rj6henN8oDc5DenawErLyB5FSfnD2pH4F__I3NvFDXUB9g8H8Rcy2eYi-08AdGJFzzbdgYgWCm1_1z0aFXPwd_w7ThEDTXmAUK9RU37MAMos3mkewF6wCV8liIWvQ956ZOSzLQl8DinLr3eDU6hmvLqAiaS0EQqvDnPzxvN2eI7iHwIf_xy0Dy_gp2u5SB-KrgspHkv7j_kSvFI_iOapmd1L8oW8I8qqu0uafdu-uUvUqFqh5xpHcvhrHOcTbf9gMFMSTV8cn_pE2brHW_vvCsqOL0MXiWi3PKjP4o-l0P-96NIJcVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=nGNJAgYpd8DibqjXG7E-Stpvpdvt-d9Xh2rj6henN8oDc5DenawErLyB5FSfnD2pH4F__I3NvFDXUB9g8H8Rcy2eYi-08AdGJFzzbdgYgWCm1_1z0aFXPwd_w7ThEDTXmAUK9RU37MAMos3mkewF6wCV8liIWvQ956ZOSzLQl8DinLr3eDU6hmvLqAiaS0EQqvDnPzxvN2eI7iHwIf_xy0Dy_gp2u5SB-KrgspHkv7j_kSvFI_iOapmd1L8oW8I8qqu0uafdu-uUvUqFqh5xpHcvhrHOcTbf9gMFMSTV8cn_pE2brHW_vvCsqOL0MXiWi3PKjP4o-l0P-96NIJcVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=vx5FwKpcgAhDohsCHqrGslE9UuI6QFmCtKj1F9o7o8Zq7ZwxsydBBe0OpIBgKNKOBvPOdidl2eO6cd78fHdQA9ApLl5G_65ahEK6RENn5a686Jf3GwoKkh1rMEGhiKpYoFm_x0z4kPjA66BIhD01kPYBdckkaDrvCnAdBCmUsakjPJ19k7RJhgLfiS7CKpBoT8wPX5Drau6N9ZkmDxQdaDypQZsmXCmuCIY7Wv-W6d4A_Pt9H9eZUQVgxxXIhvLWhwbAOER4qHdZ-BlxfXe2_X3E9N24YhgViTm-Pm1uxXhEmJDFYVVjDOIDxX1eCsBTpGD_MUhJR-SRgsbxCP12mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=vx5FwKpcgAhDohsCHqrGslE9UuI6QFmCtKj1F9o7o8Zq7ZwxsydBBe0OpIBgKNKOBvPOdidl2eO6cd78fHdQA9ApLl5G_65ahEK6RENn5a686Jf3GwoKkh1rMEGhiKpYoFm_x0z4kPjA66BIhD01kPYBdckkaDrvCnAdBCmUsakjPJ19k7RJhgLfiS7CKpBoT8wPX5Drau6N9ZkmDxQdaDypQZsmXCmuCIY7Wv-W6d4A_Pt9H9eZUQVgxxXIhvLWhwbAOER4qHdZ-BlxfXe2_X3E9N24YhgViTm-Pm1uxXhEmJDFYVVjDOIDxX1eCsBTpGD_MUhJR-SRgsbxCP12mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvz_n_ls3JdyYmZjYtitP3Qw32DHRUX7dimxC5QvkpBfLaNBdqseKcq6qCtkV2TI_pshD6vVrQlIZeMAI8Mt4n163VjUXOU2-bUqG7fNDmhbx1W_DgzdVPwVPSW7hlh64Es8nGZce2JcTZR2YIaAcBGsBi8tSHKnrny7lL9EkBMUWUaBVmF42-E2VKcKKoLW48j3mzJ1Vf0d1QYQ2iEZkVTHqw9nD75xDw7kdV59J09J5sLiCXAcToLvJzorbPOWOhErdg06fBJ6m4vlqpI6yJcnmoC5GIVg6u9NSFcuLrW9uya8568Kxj4szKIaoMqAwK3Ls7ugChocdfOV7vRlvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=CFiwG3Jo2jwhnAw_yLfSY7oPAhSIC4de4tSwkZI5Kz4hDPCwfHj0kpFurLz1Kf9KblqORrjm7HuwnkuDoS2kF_2PIrfI-xT0esBAEZZA19w9KlOHIvFILJ2u4wpX-FalHlW4jt3M-8ukhxoSECCNEP3nrsPusXVz63lXedT9EpFlnXV-lB1BOyqtRo-hQVVB087Q38JlJ7g3DIwo52FfBBgmSE-uL-3X-k1io3UVXDE8B67VZqWXzPr4MWsX6eT7CNcrMswA7Yj3TDzVdjRsqCkQczUhGlZqsUWaoxLTSPkM39xQZyhUNBNxTcGAdUoxV7Dm-G7gW9j9E_Hnm-8dZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=CFiwG3Jo2jwhnAw_yLfSY7oPAhSIC4de4tSwkZI5Kz4hDPCwfHj0kpFurLz1Kf9KblqORrjm7HuwnkuDoS2kF_2PIrfI-xT0esBAEZZA19w9KlOHIvFILJ2u4wpX-FalHlW4jt3M-8ukhxoSECCNEP3nrsPusXVz63lXedT9EpFlnXV-lB1BOyqtRo-hQVVB087Q38JlJ7g3DIwo52FfBBgmSE-uL-3X-k1io3UVXDE8B67VZqWXzPr4MWsX6eT7CNcrMswA7Yj3TDzVdjRsqCkQczUhGlZqsUWaoxLTSPkM39xQZyhUNBNxTcGAdUoxV7Dm-G7gW9j9E_Hnm-8dZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BgQSR6iLRhkWALSThI5_R-dvK_UMosoX3wAbJsmKsrwrweIUP4tbsVM4VIlV1ecyj0XE460nhEnc82_jLXkWmqxTeaNXnnFyyPA73ngKDDyWJRsk3Iil2RUlWn2Bik_EgOG8TQxwukshBxEaOEmto4Wv1zimXV3k9M_2J4K-t9mEcgmKeHe3dox3ALmIUHoZhdWEZfLyHyDtPWuIYiXwJIVaNXayovYIABnRNKfX0IRIP06tQK39B6mkHwoPT5WGENcBXD4HTwSYrSehyAboklBrH4Wcmwn1ypixHtCkBNBTtvCC7HMKUPlz4nvy5fvnh6jpTUXLdv8cDWqVN9wE_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BgQSR6iLRhkWALSThI5_R-dvK_UMosoX3wAbJsmKsrwrweIUP4tbsVM4VIlV1ecyj0XE460nhEnc82_jLXkWmqxTeaNXnnFyyPA73ngKDDyWJRsk3Iil2RUlWn2Bik_EgOG8TQxwukshBxEaOEmto4Wv1zimXV3k9M_2J4K-t9mEcgmKeHe3dox3ALmIUHoZhdWEZfLyHyDtPWuIYiXwJIVaNXayovYIABnRNKfX0IRIP06tQK39B6mkHwoPT5WGENcBXD4HTwSYrSehyAboklBrH4Wcmwn1ypixHtCkBNBTtvCC7HMKUPlz4nvy5fvnh6jpTUXLdv8cDWqVN9wE_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=WcrOHQLZI89NqAtqf9IsyjWmeXTRTixmEEJ0UmQH3GOA6RfKehoCsDmaz5yPrf1GzmTbWUAmif5lFYUnUFN9939d6lEhvk5ZAAdVqV23xRYLPXUl-c2qRBQ9VQNxTZa7VEMfFawrLQpVbeRddyvOD0QQZLG5tVek67MTkI5zTgXZ7urRP6L7PNAMYpj0HYB0pt5qi2eoe7kJ8c0wTdGBNn8MHyg5herCztFa7u-V3p8fdrX3LNSnk3ovciCIz1TssR_WZ1oizKTFe-tJgPbuoZQX2p0b2qafVjEC9PEvOv4goOspzwPEQ5s01v3E-sC6icCC3WMzNuYiavyx1svjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=WcrOHQLZI89NqAtqf9IsyjWmeXTRTixmEEJ0UmQH3GOA6RfKehoCsDmaz5yPrf1GzmTbWUAmif5lFYUnUFN9939d6lEhvk5ZAAdVqV23xRYLPXUl-c2qRBQ9VQNxTZa7VEMfFawrLQpVbeRddyvOD0QQZLG5tVek67MTkI5zTgXZ7urRP6L7PNAMYpj0HYB0pt5qi2eoe7kJ8c0wTdGBNn8MHyg5herCztFa7u-V3p8fdrX3LNSnk3ovciCIz1TssR_WZ1oizKTFe-tJgPbuoZQX2p0b2qafVjEC9PEvOv4goOspzwPEQ5s01v3E-sC6icCC3WMzNuYiavyx1svjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC-6FlthC0MCVTpMHouk7Y41EwNgFFecVOhfYOTkLaExa9JhmbG9WtVSvDsHurKE6iUCENpcRc5Stk5hm6WMORfE_2JXF7BYJ-rzX8mxHACHmjmFurNixUG-XrTaihQSseXnkIkU1T4sGgppm0Ebb8nOvhoJgef7jMw6OQXz6VZ6W_UmXQhhNjWb09_g2J0IRZ6kB6zYzQFCPllqnCAgx7rxTi8XSA3LIBGDevxD1LcivJe3a_CJpxWFoDyG74Gr063qk9wUXN_erUUz3ELSjaG9ljCARSGGiOoyowhp_N48GAO0krqU2m5gKYT7c2k-YebvRwuVljZt0X6mdygKpg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=fxBfqDaDEh8HlwcOeCW_e5xfVzVXiC584msFcCOJLC-Tddy_eEUlYdu27Y0lwBYYDan3Gjgxk1qe27NBBICaMHewUXo7W70_3AY5ojosKnCnETULwyFpFh1gg31aQMul98E_fENfdkgpQg3Z53Y5uTa7dTu_kFxo4vGuZ25xqgVRpj8EgIXK8c_3CR1Tfe_qo0Xaq2hAaJ0e-CwowD7uaIj9IPXJQvr6pxdZ-VWgBqTZWh33kJcfcnjhivbQAO88zvXp9JhPVs2lL3hNevudWgPjLJftGaD-4AvJDYdjFJQg8WN2Rz9ZwJSsGYMoW5cfP9UVMCRFJBzt-seErmXFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=fxBfqDaDEh8HlwcOeCW_e5xfVzVXiC584msFcCOJLC-Tddy_eEUlYdu27Y0lwBYYDan3Gjgxk1qe27NBBICaMHewUXo7W70_3AY5ojosKnCnETULwyFpFh1gg31aQMul98E_fENfdkgpQg3Z53Y5uTa7dTu_kFxo4vGuZ25xqgVRpj8EgIXK8c_3CR1Tfe_qo0Xaq2hAaJ0e-CwowD7uaIj9IPXJQvr6pxdZ-VWgBqTZWh33kJcfcnjhivbQAO88zvXp9JhPVs2lL3hNevudWgPjLJftGaD-4AvJDYdjFJQg8WN2Rz9ZwJSsGYMoW5cfP9UVMCRFJBzt-seErmXFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWi7B4Uucwck1aPvwMlLLR3QGIJZz5Q1uNxNT9HdCKIdrFq8GHZRCkXlNEgY2npyl2Tndaux7hWpZ_j5hf3ybOi_q3b5zG4wYkxvgAXJ5ph6sc4G9Y197PxbRgPgz9B9_rv3YTJQwZVEd94uxl7X8b08NrCt51gPWku07EQVKGv6rG726D94dxOe-_FdvArguceWaPzMq2zcseq_Tn_ulDqmYOHkxkx9HyWNDO-I6dLM1CHA8DiKr1TpSkihV6pLXFDsJAlt65WeGxS9uSrrlZG3yQqiiDj7BBIF-qC8RktFWEldXkzLU1mfGl7_Z1zRQ8LzErzh_pB4KV9ko2TWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5yPu8P037aMd4M1B_FUjZyIqYy4FnYuUYE0ySMrQFRsGBtfUM6eCd_hmi7uA3nI1gFoaQ_BycE0jODV3T5U0B3rAJrFv0Pt3i0kqweBK9qTArYQztYotrVKlyX94IcDyCINi0w-PqQueNiU86xtomrkvBysx2vTRXhNcvMeAbppjTOCNwL5T50sW_U3RRpNawvw_T586dWINTleVMNsMD2dZIIyxGtcro0UG5PHKttyUBoJdqIXx6yCcXOpswJN5-cnodbCjXWB0V4-v9LQr0dIHUeMJxd3JoPuv0Xag4L9yti_zh1qDIG-IKVW_PszQvSABDQ2wS2bF87uVWgE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=KvL3EuQJGflvHp2S_HsWlNVjOEXgVw6w2RFPPAd4yIyQn7k5wNAdbpdLEku5WR1KHUM86blv7MqXicU0KSqhTxXyrtpGDPYdt_sFZkqqzfUOc9h0VthTDXTQMceF8y1Uzt3QTZE-rC17p9Fn0QWGJOQtQYAPjGSomm976i3ZpeCWTXXoQe1k7Mctt6N_j24MlUPEuxhc9Debdjb0oehCo4iZPxMQ0h6Yg66IJ-bMOa6lISVETpJhbMHH8nOTKcFiJeAm8o7394wFOcPgmJDJmQF2j8smhM49XfPC_RZBINXFIMCf5z-NPnNKn_q_RD2b3NEtW_YlFqRX2MC72BaDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=KvL3EuQJGflvHp2S_HsWlNVjOEXgVw6w2RFPPAd4yIyQn7k5wNAdbpdLEku5WR1KHUM86blv7MqXicU0KSqhTxXyrtpGDPYdt_sFZkqqzfUOc9h0VthTDXTQMceF8y1Uzt3QTZE-rC17p9Fn0QWGJOQtQYAPjGSomm976i3ZpeCWTXXoQe1k7Mctt6N_j24MlUPEuxhc9Debdjb0oehCo4iZPxMQ0h6Yg66IJ-bMOa6lISVETpJhbMHH8nOTKcFiJeAm8o7394wFOcPgmJDJmQF2j8smhM49XfPC_RZBINXFIMCf5z-NPnNKn_q_RD2b3NEtW_YlFqRX2MC72BaDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pjUB58pJ-pUz7w12MqG62qiM6FezrRRZ2_JjlL2ErdGZsksq5n7zphJUr_HQ0uis0SNg7uRYVwsVIus4L5iA1MY9NJUqhB2pCU-xVNRNGU1I3YG47XtKoXFsQQscxBYYU_uG3dXvLBGmoZhS0yE2iELrhd348LW5ut1s6SnnxnGhnnm8RrXT09gE_LzCDi4t12ZTASECw4B9P56jRmddMVRnKY4P7qr-wJ8eKg_oBA0iV2WAXhDe_H-N34nla7PAHf4qMRiELsTg_uRjHage8o0rrj0MqStO-KbHrYQo6iKEwcAumTZrCpqJN1Tph6q9ni1GLWP9czT_VNwG5m8i3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pjUB58pJ-pUz7w12MqG62qiM6FezrRRZ2_JjlL2ErdGZsksq5n7zphJUr_HQ0uis0SNg7uRYVwsVIus4L5iA1MY9NJUqhB2pCU-xVNRNGU1I3YG47XtKoXFsQQscxBYYU_uG3dXvLBGmoZhS0yE2iELrhd348LW5ut1s6SnnxnGhnnm8RrXT09gE_LzCDi4t12ZTASECw4B9P56jRmddMVRnKY4P7qr-wJ8eKg_oBA0iV2WAXhDe_H-N34nla7PAHf4qMRiELsTg_uRjHage8o0rrj0MqStO-KbHrYQo6iKEwcAumTZrCpqJN1Tph6q9ni1GLWP9czT_VNwG5m8i3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=XnUFkivi2-nCS6MvroC8sUqsK1-7W-Erk47PuOSWQODn4JmaQjoV4f0RvOny20KZaV35nu4_s7SHzzBbsrnjUlGaeTcAFfJ0ZUxhxysEdw62ye_KpaO6-Fq64qMBnVHfFC2M6s5US8MjSb-85OWIPcX5mB38i9DgPri9vA_lTWdBDXfA6s2kxekRiW8H4R8AnCu4HJy-a-Cn6CUEOwMKwZ6S07f2R1qPJ1otHM7E_tdDNDI5BidnoCKIqXrQ5uDCGUpuDe23ZGINdGIp-49kjkZZUfaFBaybqzpiZYpgIas_pUGqKCAoJ7f9y6YcYZI_ACxrdgtrMadeAAaLNL1MEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=XnUFkivi2-nCS6MvroC8sUqsK1-7W-Erk47PuOSWQODn4JmaQjoV4f0RvOny20KZaV35nu4_s7SHzzBbsrnjUlGaeTcAFfJ0ZUxhxysEdw62ye_KpaO6-Fq64qMBnVHfFC2M6s5US8MjSb-85OWIPcX5mB38i9DgPri9vA_lTWdBDXfA6s2kxekRiW8H4R8AnCu4HJy-a-Cn6CUEOwMKwZ6S07f2R1qPJ1otHM7E_tdDNDI5BidnoCKIqXrQ5uDCGUpuDe23ZGINdGIp-49kjkZZUfaFBaybqzpiZYpgIas_pUGqKCAoJ7f9y6YcYZI_ACxrdgtrMadeAAaLNL1MEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja8RCVKzqZN4qd_Uk3cwYBUkwWDAyVEfQusIS9fXwnBKa6NhDhyEi2b3ijNgh9OP1Zt6AbQQrsGkmNiFgcNkDnL7v6WBSUvcoA3Vfkt_c58HjEQSm-Po47yQI-yHMaBnwuUX0yzCjDH69J2l-ZBH4GdwZ6oPGjUZuQ4XwVU2k_7mByXql909mZz8V6vPxSnVMx1vuTtz5nEC0n3ic6CibE8jX_MXTNZRyTmDkQHdNSDa4xnF-Fm6BRf8ypaD0WVI-2V_Rk_YbrqUlTM8OkXZEWuMxfU8x2nhMck5LstJ4C-Wo-KJVhZzLc9zHcGdjkU3MwhNSmjo0lWuhjErXZthDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=nnKDWD0qHUQ-0XAEL1Y7fgW3IUEDsMu5Uzl3HH63mJ697fE1UFfUVQAFBs1yxrFQqTiUdDmnUwhtse1BKzHq2h0P9gdMCEkhHEkS9vfupv4LZdvwcQbKNtlCvz95E0lzqwy_EGZGtzEzTreDqOAKNuBKm0SECkX6I7RTTjHJaOkkG2-32eg74jQpykS2VD9ZaYebeFr70q4AQ0wvgwo8XUrnoPVAxq6WOl-K2mLT8m1hZHfE1KOtmJwGmMAutqA_9H3rs0LcqbaRdvo8zyWud4Ev8W7a5MccJ7w0BEtLSinDljI8bWdDqAaUVg6y_-RgRhz6Dg2t-PexJXvHiJiwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=nnKDWD0qHUQ-0XAEL1Y7fgW3IUEDsMu5Uzl3HH63mJ697fE1UFfUVQAFBs1yxrFQqTiUdDmnUwhtse1BKzHq2h0P9gdMCEkhHEkS9vfupv4LZdvwcQbKNtlCvz95E0lzqwy_EGZGtzEzTreDqOAKNuBKm0SECkX6I7RTTjHJaOkkG2-32eg74jQpykS2VD9ZaYebeFr70q4AQ0wvgwo8XUrnoPVAxq6WOl-K2mLT8m1hZHfE1KOtmJwGmMAutqA_9H3rs0LcqbaRdvo8zyWud4Ev8W7a5MccJ7w0BEtLSinDljI8bWdDqAaUVg6y_-RgRhz6Dg2t-PexJXvHiJiwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=h0Ec177pwQzTUffJfYhz81aF4ESHv56Rxw4l0jNRarSTIlVBaK6Q_ZzPto0_Fve3Pd8d0PZKfFKoZC5BWQHzAC4JL0_CM0TjFazfNuPehPujCjoPdvGDmDRAsAmAU-20STuyqupdIwtZ_EzdCcHjLlIGnhxao7Ahpem3P6HIJt_f_920YyMFpGK1t_k9_qT75Cj6nFOlI9LWIsMjk_sBFcekOzHrzwdarfA-HdYQLoFfUXjm0zZkRx0O95wdSLzOFTuLV7ml7PiCPOx4kfAe77mhAX5t1s0aT_JsxP4zTOdoIa6tVwG3q5nL7Zhka_dT20lIqEtCc86Yzb4KBzkEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=h0Ec177pwQzTUffJfYhz81aF4ESHv56Rxw4l0jNRarSTIlVBaK6Q_ZzPto0_Fve3Pd8d0PZKfFKoZC5BWQHzAC4JL0_CM0TjFazfNuPehPujCjoPdvGDmDRAsAmAU-20STuyqupdIwtZ_EzdCcHjLlIGnhxao7Ahpem3P6HIJt_f_920YyMFpGK1t_k9_qT75Cj6nFOlI9LWIsMjk_sBFcekOzHrzwdarfA-HdYQLoFfUXjm0zZkRx0O95wdSLzOFTuLV7ml7PiCPOx4kfAe77mhAX5t1s0aT_JsxP4zTOdoIa6tVwG3q5nL7Zhka_dT20lIqEtCc86Yzb4KBzkEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=OCK3Yc2CnpPi0U8EeQqksFLPuit_tUOagUd3-x1-cEmLJoXFd5vM2BkU3U-WgQU2zCj4NI0AUL-TjCOGJm-2s98wx10q5NLnmySvD9Lz6B2Xd2Vz_t9TCIBIRnwnhlXIYBTlC0PNUEqvtWE0ORLsTgXjamLny9Nwfj5P5uk9_x_3mAqfU1GFhwtn8PZ1ZRZJqKVM0NYNDKsyRfXrViFaOo45_OGCcv_AYEt60NEqfe3xgJ1mCF7FtHFLlt86_3EYUyCR9mQ_PZPVrutgvk2q5RRrNTQgnCZU56xFxa2-C7OFHX97fpTT5JKsKePFc_pTcvoKhNQu4l1Bvtoa-gfJCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=OCK3Yc2CnpPi0U8EeQqksFLPuit_tUOagUd3-x1-cEmLJoXFd5vM2BkU3U-WgQU2zCj4NI0AUL-TjCOGJm-2s98wx10q5NLnmySvD9Lz6B2Xd2Vz_t9TCIBIRnwnhlXIYBTlC0PNUEqvtWE0ORLsTgXjamLny9Nwfj5P5uk9_x_3mAqfU1GFhwtn8PZ1ZRZJqKVM0NYNDKsyRfXrViFaOo45_OGCcv_AYEt60NEqfe3xgJ1mCF7FtHFLlt86_3EYUyCR9mQ_PZPVrutgvk2q5RRrNTQgnCZU56xFxa2-C7OFHX97fpTT5JKsKePFc_pTcvoKhNQu4l1Bvtoa-gfJCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=JK52z0-TcTqUhMRq-sKF9k3TuXXcQ1-iYcI7HBPoaiYKmX7L3qEHihHX2R9v7COrImhuYat1GLgh5uCQtK5q-2tTwAsGXHtY0fNw9w7uNgQ4VHA25QsXIJGjBz2IHTtoxlc39pFopgPUx_TsRyVMYX5IUwqi9PNmMw3riYYBotJqUefuFiuIR5HklmZn_Q9nMRUvOIiQ2paXL3LtCP2ya9qUbC5WaqX6j1D6OGEKOl0ZJbI5e93Tu23TJIcGCGrVkActMKVZMrJtxV3CUmeANes4Q9F8qQVnENOzj7x_4d_pywDiUyGuq4cneHVvGrvhQxo-_dybxk1bsj45FHb-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=JK52z0-TcTqUhMRq-sKF9k3TuXXcQ1-iYcI7HBPoaiYKmX7L3qEHihHX2R9v7COrImhuYat1GLgh5uCQtK5q-2tTwAsGXHtY0fNw9w7uNgQ4VHA25QsXIJGjBz2IHTtoxlc39pFopgPUx_TsRyVMYX5IUwqi9PNmMw3riYYBotJqUefuFiuIR5HklmZn_Q9nMRUvOIiQ2paXL3LtCP2ya9qUbC5WaqX6j1D6OGEKOl0ZJbI5e93Tu23TJIcGCGrVkActMKVZMrJtxV3CUmeANes4Q9F8qQVnENOzj7x_4d_pywDiUyGuq4cneHVvGrvhQxo-_dybxk1bsj45FHb-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paLH5dUuCw-LXJBdBmGEdFiRNW1XbSiE6C8Zy9VWd54JkyHixw_Yqph03FQlu4ne3FYQRlPdENYhtGK43tQTQyd8cWgeCzeM92h5MoEurDz6Aa9NeAZJXnt7OQVCdHtQzc8xWKAdjz0q9WNGnaPhBcAiOkagayVap0q44gG-wrFZA1PB_laLqFx_VH6hXOqa_UYkq93lpZTk5mSAIJd5RZmWfFDDAICOJG5jVvJ-kksueDbZFH0JB15GRhE6mEDJmXjZRJXNpqveHLC9oXANcUH8scIqaOsZcNy4Sg07AqwPwyX701T-DFfaBOIgU3OWAB6SnsAjsW0EWyYF_deRIg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=I0-cMA9u0Q8DhnkjSxQifwouu2-AhVQZoyA_g6_4i8JgE0Sz96SHywWymwvFKMyq3KFBsw1eeoFEdde42r3r39dElne-XOYNOP5T_0tcv6S5KFbDFiGzYRFfwCWS6K38z5r7SJ16l-VHVX5nEOROYECPKj8Wy01izRH_VL30Z6O5mCPDb8MLaPRwYmCbAgLRck4yBqKlHJIC07GJaaetlEBEemJ9ODgroMXk6usFlfd9c4Y4f5eNFQ5fn7P3gabJ8BAV0IbljCuibMqZVO1YfpfJxLuTEtrDY7HXxcikbdGQcknkbbolHqDzYQJul9DZppHjYEuu-orEVk-PZqeRqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=I0-cMA9u0Q8DhnkjSxQifwouu2-AhVQZoyA_g6_4i8JgE0Sz96SHywWymwvFKMyq3KFBsw1eeoFEdde42r3r39dElne-XOYNOP5T_0tcv6S5KFbDFiGzYRFfwCWS6K38z5r7SJ16l-VHVX5nEOROYECPKj8Wy01izRH_VL30Z6O5mCPDb8MLaPRwYmCbAgLRck4yBqKlHJIC07GJaaetlEBEemJ9ODgroMXk6usFlfd9c4Y4f5eNFQ5fn7P3gabJ8BAV0IbljCuibMqZVO1YfpfJxLuTEtrDY7HXxcikbdGQcknkbbolHqDzYQJul9DZppHjYEuu-orEVk-PZqeRqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Mtp1x9WlkVuocwq-DVLtclt80tquLh4fJc3EgHxqaKVsu5RKAyzLQQC9LNfLZ_z7Ge_ZDjT8KPGhLT8pDhnri5E6KcrprlNpEVZG2T2v21vpCTkKwP8K4x4rRbwbB6mkKCZA4TgS4dvBEj1qXX6gBPeWHkqxAt-XPGAxee-Yfuz-DIVPHOHtWP1bZfDiVGAbNqFdYsgyoStDmLgdb5TVDMRiVLXfZ08AemeYrTzyWXAvcozxKO8gEFowqHP47GsN4B3tH5jTt2x0xsFeWyE31UX_n1dIOthTaHYMX5VFwUQ6KJyAQigl2WNHuFWWGECzdXwRSU6YYVmcJKqSwxPu8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Mtp1x9WlkVuocwq-DVLtclt80tquLh4fJc3EgHxqaKVsu5RKAyzLQQC9LNfLZ_z7Ge_ZDjT8KPGhLT8pDhnri5E6KcrprlNpEVZG2T2v21vpCTkKwP8K4x4rRbwbB6mkKCZA4TgS4dvBEj1qXX6gBPeWHkqxAt-XPGAxee-Yfuz-DIVPHOHtWP1bZfDiVGAbNqFdYsgyoStDmLgdb5TVDMRiVLXfZ08AemeYrTzyWXAvcozxKO8gEFowqHP47GsN4B3tH5jTt2x0xsFeWyE31UX_n1dIOthTaHYMX5VFwUQ6KJyAQigl2WNHuFWWGECzdXwRSU6YYVmcJKqSwxPu8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMGNcugs13T7UXuvwCbefH47RnUsISRI7d2blsfT9B_TtFMH12nOtpOhppqnODTt8SHufcY2KNTaRDIaWPSfYKOFweAXRc-Vj4_L-b8tNN4IZg7xXtCtoh3ETtjk9iYubNqzveo-95vW2IrxBYIwlKsCKY_SyU5iccq6yY2gR2geQ40u656u4ewnLymsmbQBF0FzxrvKNiLIcxuc0f_MHnKKRCFem1vnBn2EpPiYx-udRKRufyPsCrO82L6acrphUM-6_w8fvtJoiM7rvYjhR3zi6WggrFebe51SxCNUUebDJASIZ04qZpAC89tYAr_dIasokn5K0HuwPK-olh8SeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=NW4H1GysK5SE4uKd4yjpG1b5EyvSPml-C9f6bhh6RJb6RpF6uidp0yP_q60RGY-Af9A_bgtQV0Em4qCgC5ibiej1l97KlfVcHoYl2HFBUtWeU3lW07r-fCwdrqZdztj6IzJAhoSe-h4lmJdLr5k_4azK3Ws3Xzk_YMM18Ks5dIfeiMITDTxIcCB39PzTgeLBs4QbpzKMpS9bNnee1B-LsBvFc-bPjgT4vsSOB3rHKdHjWJrcZ5mQHi2pjdkE9cE_E4uykRlVWNvtqZwZPJ4ypw-nWClCvkb95A7gj7AVcvY1qM4HllsDLTkhPhmpciuGyBQlk8ESdp_txA11ormjzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=NW4H1GysK5SE4uKd4yjpG1b5EyvSPml-C9f6bhh6RJb6RpF6uidp0yP_q60RGY-Af9A_bgtQV0Em4qCgC5ibiej1l97KlfVcHoYl2HFBUtWeU3lW07r-fCwdrqZdztj6IzJAhoSe-h4lmJdLr5k_4azK3Ws3Xzk_YMM18Ks5dIfeiMITDTxIcCB39PzTgeLBs4QbpzKMpS9bNnee1B-LsBvFc-bPjgT4vsSOB3rHKdHjWJrcZ5mQHi2pjdkE9cE_E4uykRlVWNvtqZwZPJ4ypw-nWClCvkb95A7gj7AVcvY1qM4HllsDLTkhPhmpciuGyBQlk8ESdp_txA11ormjzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=jJ99PQFvESG7bKY_FRHeeyp4HXji2w1Umi2UI0F7WaLWhEWC5zXSonZAIyUYodJrKqr9jRm-K5rf2dGgHjkMvYWsTexWliMvXkqoFMyNI0E2oNIyUp5Qwl8gtFueoFrqYdK2thZDpJLgwJZ2orIvG-hbIBQDtkOMDKd4vOEGhsts_ovMM5gXoKd76DiHU9gniyWLn_5loKTUDi8HElGWGaz-f3HzaQgwtr5KKUhSLd2_7lftShbTuWzTh0uRfT48jtIAlQRUsZruzlKUExxdKq9RgZ_fUJ9ADuIphexFfxO2pImXusxoLUZn6wIl6ckK3m_PvVyjlhyr7BMDhp6qVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=jJ99PQFvESG7bKY_FRHeeyp4HXji2w1Umi2UI0F7WaLWhEWC5zXSonZAIyUYodJrKqr9jRm-K5rf2dGgHjkMvYWsTexWliMvXkqoFMyNI0E2oNIyUp5Qwl8gtFueoFrqYdK2thZDpJLgwJZ2orIvG-hbIBQDtkOMDKd4vOEGhsts_ovMM5gXoKd76DiHU9gniyWLn_5loKTUDi8HElGWGaz-f3HzaQgwtr5KKUhSLd2_7lftShbTuWzTh0uRfT48jtIAlQRUsZruzlKUExxdKq9RgZ_fUJ9ADuIphexFfxO2pImXusxoLUZn6wIl6ckK3m_PvVyjlhyr7BMDhp6qVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E1CdF8Fro6gmLxdLR4KKGuT4JwlZQHlHCatFCq1CeO40soZjIml8MbU4v6I6caDcw_VZYIoQBAB70_DBbWf0ChwJMg-d0k-s-VXIQYExK4H0e8Y9bPuqddZF9JodDvF_8GcXShn0sdytcYpU0dKXNH9NZl2HNxp21HQG889QPP7L-Vgf0oHJ9Ol33OvT24jLjWimhbgR9kni5kq2aGmmqt5ChHfubFIbSJfVERxPmYGDAClgI-PO5bTQmmj2Lhg11RzmoPMQLg7DPFvmsmO2C_UPHLwGCpgCq8ld5mUqmi6X4YVqZTdKCXfVz7UmrNPWu2mHXtc1eEnHvR9SOUt_8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E1CdF8Fro6gmLxdLR4KKGuT4JwlZQHlHCatFCq1CeO40soZjIml8MbU4v6I6caDcw_VZYIoQBAB70_DBbWf0ChwJMg-d0k-s-VXIQYExK4H0e8Y9bPuqddZF9JodDvF_8GcXShn0sdytcYpU0dKXNH9NZl2HNxp21HQG889QPP7L-Vgf0oHJ9Ol33OvT24jLjWimhbgR9kni5kq2aGmmqt5ChHfubFIbSJfVERxPmYGDAClgI-PO5bTQmmj2Lhg11RzmoPMQLg7DPFvmsmO2C_UPHLwGCpgCq8ld5mUqmi6X4YVqZTdKCXfVz7UmrNPWu2mHXtc1eEnHvR9SOUt_8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob_OCKbJd-nYCTTX96wgqw0hA-QOY4AVtDr4aSFbGye77Lj4P4uTZ35ceMGp6b1A2Q6onXOwNDiTi6U8h6yP9_0UsRGjfg_Sa3E76d3dz1G7IricCFDBREqNdHKy6isvcjUlhFQ0chfHhwGgI0c8jKIm37cmFTV4yzSn5E2vtgVsz3DOEsyf-Z5ctLsKV2a0q6vHSG_cJ55lGBMasN3-XGzUPDxIYU_22TxROmN2Miui8rQMF_s7U0s0FBhZWX8dv5TbYnYQUz30ggjMqdsnbsG2RSCWUQof7YMZDtRbmMneBcqfXrd0ZsvaLfnaEGqXIS0tSw2WzfEwixsKKJbwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URCrqb-6wIb4iJVk0kL3uI4S-sdrAo8zDaeGqOzSono0R_56mtxO2bsc7dngmQGmFKCbOv3JodDeF6q_wavp_944kUnbGu6LtNsN3Y6M5mBaqHcB5E1q8AGejPdLEVJktYqUITKFzHAaU3X1_KF8K8ynKKHuh2Kv8Y9bIjV85gXyEvpwFfNYLQ4tTDO8DQNUI3arOpn6qTIqC7SBxpcAwv3bG72GjZ7KZE5Fztt5XF7Vez8WbvFu2e1uO17pANg5vD4T3DJPKswj59hMtp8dD1a784FCbc40yJpvbRNvEOZtk5gy-BlFiiB_aU9VJrsRj3QRaTAZgEUHttvfRg4JKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7--5-_9cIYFr1kOQ6PYnzx2zai9LdalXHQiDzah7azLSwVXjz320cSU63O6wDwfn2eSqkFqzX8EUDU5OLLQNB7B94TWxL135GOgxn2igFiFXFuYiL14nEOXkSCeQ1fzqiip9GrP8J0qPMRoGOwgQHwxjLPW3UKbcGcEyi5PtPOaNJBGE9SheyXrk3DjFqC9Hnry8WAw5Wxbmpt4Rf_6Wh2Ci24Ou5HSnNiZSlUHDeknc60dMm0CZqhu2ghYOzTfpH4ulaW7eJAUiZ5J0NA2z5qeiBF4wtY37i0a25P2kUZifCssk9Lk3RvUUAzVL374m7vzEaM5bCGo4K-Mx6MSFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=v7Yi4LHUSqxfllw-nO7LBuyxzACpVLIqbWb7cMFmy_YDUYdNW1015EA7xmAzkK8VA1N7tfG-KZqw0-FUGNw5w9K_foiRzfB7_q0ggGcOG2Zz-buNNsQz2MjIH7A4Ql061co43IEPW1IWp9-6-E-OghZdQyIZAPBNvIWQkYYeQQWceZb5TqJPezu6sxsCIoMdpyA4oLt-d2HzUSlyKLanupqGcuYac5YXLjMIdWZ7URJe2rWv155fb6Re6XBBsLLC7Nn-YRyPxxN-Vhh3pAmA0VjmFIFONldSaL0SGEW7B_x4ePEquF_VCGuHs5zlmjYVpNASeDVOOmWbvu6k-OdAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=v7Yi4LHUSqxfllw-nO7LBuyxzACpVLIqbWb7cMFmy_YDUYdNW1015EA7xmAzkK8VA1N7tfG-KZqw0-FUGNw5w9K_foiRzfB7_q0ggGcOG2Zz-buNNsQz2MjIH7A4Ql061co43IEPW1IWp9-6-E-OghZdQyIZAPBNvIWQkYYeQQWceZb5TqJPezu6sxsCIoMdpyA4oLt-d2HzUSlyKLanupqGcuYac5YXLjMIdWZ7URJe2rWv155fb6Re6XBBsLLC7Nn-YRyPxxN-Vhh3pAmA0VjmFIFONldSaL0SGEW7B_x4ePEquF_VCGuHs5zlmjYVpNASeDVOOmWbvu6k-OdAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
