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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=KI3Dm-znuB8xxKUXYPq4y8LdbrK-PaLd65Dudd9pYNnIuSR2IUIddL1vT6RdOgjZNqwuQg_A-aldk8Gl5v8MYQqaYyOzVpJmzB-r2Coc-E1Fc_OWxOxaDyY3J8DJ3HaGjSvoBxTOcQfBCkP5b7K6gtkzPUWenCu2SuyjQ035K3bpMY2yYPitnzHvDxE7fMgwMTHqacqougGAcEDXrqNd-X7WnZE4yNeDJXYR11Ftiq_W29VFJuAGGEB92PA2OcCUcTUAe4pxbAxKlmbC2OHUctR3R28R23M-ZvgAvZ-KVMf7c1Q6gjyP30kqJnm7XbRuJKsz_cCicNgeS6EOOj3heQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=KI3Dm-znuB8xxKUXYPq4y8LdbrK-PaLd65Dudd9pYNnIuSR2IUIddL1vT6RdOgjZNqwuQg_A-aldk8Gl5v8MYQqaYyOzVpJmzB-r2Coc-E1Fc_OWxOxaDyY3J8DJ3HaGjSvoBxTOcQfBCkP5b7K6gtkzPUWenCu2SuyjQ035K3bpMY2yYPitnzHvDxE7fMgwMTHqacqougGAcEDXrqNd-X7WnZE4yNeDJXYR11Ftiq_W29VFJuAGGEB92PA2OcCUcTUAe4pxbAxKlmbC2OHUctR3R28R23M-ZvgAvZ-KVMf7c1Q6gjyP30kqJnm7XbRuJKsz_cCicNgeS6EOOj3heQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=ByFdc47RdhkzRMnH5G0rnFF1NolD76u9e9RqvK0XTevPbT4Syy9XosmiJMTVvFk2oNOBuf52E8WGZ0hakdOa21U2jKtcf2pI9CPimMrcJSLWyCWgFkX5LLt5-pivx-9jY3l9K9jmZmgHH7lKZ0pjt1pLyGHWSm5xPKrK80izRwGMMhNi4xsapJ3C4Oknrkf86gMcc1LmPPWr-v41eITIR7DPBZr70Llv-N43dFxcLquHAAEXIk8LsDVP6cGQtxoIm-EW6WH4xPQXB-6LNV3FCpWyGqDDkeAScYmIUHeCdq-3NWOiQbKXLy-SekbHEdwH21xMW1qJySNs8fXmq8kSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=ByFdc47RdhkzRMnH5G0rnFF1NolD76u9e9RqvK0XTevPbT4Syy9XosmiJMTVvFk2oNOBuf52E8WGZ0hakdOa21U2jKtcf2pI9CPimMrcJSLWyCWgFkX5LLt5-pivx-9jY3l9K9jmZmgHH7lKZ0pjt1pLyGHWSm5xPKrK80izRwGMMhNi4xsapJ3C4Oknrkf86gMcc1LmPPWr-v41eITIR7DPBZr70Llv-N43dFxcLquHAAEXIk8LsDVP6cGQtxoIm-EW6WH4xPQXB-6LNV3FCpWyGqDDkeAScYmIUHeCdq-3NWOiQbKXLy-SekbHEdwH21xMW1qJySNs8fXmq8kSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYKpGDlamS5LMeoNyb0EpT2sDSiBOG2HHSfwi85EKbJvVJJR0AMdsiSrPu3GvAZ81JKjq7fCQaX77OEkP-tj9T_Oz8grJzFyADViR2SIa1PO2jV9OuFBeM692d0bMmz65Ymgr0Fg9z31Pw42MaeZvxAovtvdfdPbBoAVqsIvmMhr5l_CT3NM5dtexQi69zANWrfeEvlQymUMSsqNgX9WjWCZQXS2OUCF4KyONCmRsCXOPO7qjlNPmWy6Cof3y8ElXKxD_MncWT6kNEE4HYLQl_v6a-ws9LANiag_TvaPj4U31y3jI8V1CqmSgOxzX4K0wt9QaPfq7YOUW3MIbsCLcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRKE3E8NgKoheKiNLQy_Znx96xEhLGa7M9EzX335rmkzBVeTzdYlAkZ2c2U8Fz0lAo9i56d4A12WDV_LerQtx6aXPDGBUTABF8aObX122Ae0h_QrAHzl_Z-1VGIoFcnCwmaPp2q5DH3AmsvILAEudpBrxdMirUWoiO3SQ2R8ngZ80UPHraPKBqg9tBpzHiNf8egrQeOHFpT94vS78JobVhAEF_VZm98iJXeVbFcXw3TDXDuBDxlxpR3fMUfuzT8PbZOCPGbTo54Kc9IyWzgKHldH0ErZgW37eFW6JnajVK80EYNd1eTjvWNmNaEQnfneg77isPLcsRdiG11tActvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6kNvrbi-aZ3RYhb94nu6gcw_3xIaO6Rq689t2fjn-8qXxyJersI0kUpx6TqRVVHTjDJNqHTEBJ5AnEVt-57hXWTh3NeBEOC_i-SfqusAuubgo5z0oIyB3kj_OaY2feF2SbZvKvhQHSXBaKqbHNzb_z8yFzgHlDcwKD8PikMkEmhJ5_qIxss4TQKSzLmfctAEeAkdgvZx-WKNSEJJx5BsOrejRcdPKiEyXbXJdKWlr-FCB01Sfanur0QEA6ylrOfiEAnmTxRogTq5azInocybmve1d_fode0J2RA-6AXT56jcUim6qecC29eANXCQmUvqRS6-nQaPJ-6znnNvqIkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8NcoBTjvjILYPZR_pF7GjF--XlxsXxYSgzox8H9xLFkAZZUjaGlNVXyBTdSCtSbOdG-90yzkGH8Htr6nhk-B6pswopvKTZLY-Ngb_eeQA15cPNQdeJE4WEap3LlpsQdHdpnV55JmesjmlEsG9I6BvmASimPPEpa9IL8TVAAW3qXnFIpw97-6H9dsFlecksY8aluTgR1JjjIl8ST_T2qL_aJaeM_O8DIpaYAS_khn84434VV3ruIXIjezyoFRyo__UIJFkyukHy2D92VEbvT2a6xU1oYy8rfaZlZw5b-7MHkSey0d3ZMUB6skJ1AgzDAWc4PlbLsCp8vpEMsnjBkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFtRPqLwnc9Uk0h9Gr98w6mAfX1Ne8J39oRtSjavcMJqZ7ykL6byNbUmc4ovPSQz_lXCyskIybDX7CG6tgx9fCEhot675S-bd7JBdOps1kazHoEZ-YB75koHgASGWPvPDLLV40u5Cfo_6hZ7-wXZsbMWoFWOKyhCuyobyzV8JA8vDv16AtSGFAT1tQxgk4koA2dhh5WLXCOhYhEojj4HuoBb4THLBPNMKKC7f8gIw1efyC4I4MFtyk3x8vBtk0DnKf2tbyBk-zJfUxHzI0uZ4UX6V4-43tR-ZLZFEYozqqeiE5YAYOOIeiUIjpZBg2hbf5WKXK0Zpog8K_emNiP_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW5nqa13TWaTa6cTzu3S5cAOwPVGwUXq22bl_T3wWR0OhV9kWRyCR69jqoFjeIv_R3BN_wK-zbrD1-Dtz4skI_HJtEPxlDt-MF9qMHSe-a6GcLEZGCJGtzGcCkmp3CbZDA5fa_h3tUX2aY2CnhCZJijbZVhk6RSN8ZSVx0NvqtyNEHOQ89-aKdi0KIGCyIIOhhDkIX92XBeeH1u5A0Yv231I8XhlmbE0BJRqYyzlB4wsIz5xACIfuEEis2pSfbzNx3GZkbXGxr1UqjntT-DWlnTt2HmAUnBx9PBFGlNbjLQkaC1NyPWrr8ffakFG9GhxpQx3TXohmVmYP9jH9TXQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=YCvuP9T6m3b82CBg_p_FVaNo4G47J4r59VAclZohdDTSAVo5-ymtyffBwrkHukoTCpbI3BEecz9UGINK_uyrz1pRKQ8MTTyvOHQEjVU_4OP25vLTO_bnL8ozza73LxQJ18ad4U3K-svY4Pn538WnL2ZR16TPbgd8vQiw5WfErqTvejTfYq-taMjgq_s1-LuHjv-cKW1dofrSLFwQCwDnNDhaPntTFwLLw7dGWdVZ7Uzrbz-Xz0wq9qz7WkXI58FNv0P1hdfO2XH_sKBJLZyO4PoFqBqXZH99Hke01h1cAzN8g8_HQBF7-iS3zxszPAkxaSFOZJ66QzeFyXR9Aw6elA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=YCvuP9T6m3b82CBg_p_FVaNo4G47J4r59VAclZohdDTSAVo5-ymtyffBwrkHukoTCpbI3BEecz9UGINK_uyrz1pRKQ8MTTyvOHQEjVU_4OP25vLTO_bnL8ozza73LxQJ18ad4U3K-svY4Pn538WnL2ZR16TPbgd8vQiw5WfErqTvejTfYq-taMjgq_s1-LuHjv-cKW1dofrSLFwQCwDnNDhaPntTFwLLw7dGWdVZ7Uzrbz-Xz0wq9qz7WkXI58FNv0P1hdfO2XH_sKBJLZyO4PoFqBqXZH99Hke01h1cAzN8g8_HQBF7-iS3zxszPAkxaSFOZJ66QzeFyXR9Aw6elA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=nMb7UTg2Q-EsLV2rRV69dz8acXzsvbUiHUo4UAF3wG3gWpgxTMldPWs5htjN7sRoX2-IswNkLwuxQSC6r7lazGY9DyVcGl2vtemqqhIjOuyzT4TSQBOMhmzRQLEuZdlPYXgKnMQ_dQYO1lignbPKVoQymOI9V-UZXsQaMR__y2brYpvHWi2jaXAyLR_JnQXvPfgg2GDkzhlLsLfeI9taxDjxsm4xSNSRIFU1lzM_Egrnh8dXM9Czh1Bn3zf2Fjcz0Y2A_-f4PQKdo-gdnbT83lF32M5kAXTpDpwOUSyaBiRhLSr-9Tg6lcIsfPZvDbFYCmh-iPZbmTxw2nMNblLDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=nMb7UTg2Q-EsLV2rRV69dz8acXzsvbUiHUo4UAF3wG3gWpgxTMldPWs5htjN7sRoX2-IswNkLwuxQSC6r7lazGY9DyVcGl2vtemqqhIjOuyzT4TSQBOMhmzRQLEuZdlPYXgKnMQ_dQYO1lignbPKVoQymOI9V-UZXsQaMR__y2brYpvHWi2jaXAyLR_JnQXvPfgg2GDkzhlLsLfeI9taxDjxsm4xSNSRIFU1lzM_Egrnh8dXM9Czh1Bn3zf2Fjcz0Y2A_-f4PQKdo-gdnbT83lF32M5kAXTpDpwOUSyaBiRhLSr-9Tg6lcIsfPZvDbFYCmh-iPZbmTxw2nMNblLDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=WukFArRIRLt5-XIqGU4kc0jR9F37Y6nztxNe1TwTFHQ5bjzX8iHOw5Er4lUZiyP3r8dbugJcoNO7io20QphroTpQR6pBUF4RoO6-yq7ZmQvhSI7jzA6mfYZtfujlZrV999NgCfvmXCtzuWgM4_2YrO2YUymSaFgnBwzfFgKGTeHBnwgJsWKy7K0xQxWSDsc-duH8_kimRBwRcv88r7udQdHVA6lTzah93yvmy0JgIUDfoORpE7uvEDoUOGx-goSFFIxsixH4m9FFfurVDhq35Fwg2UlK0lzAZuEJrXdsPxEckpwyklkbGHd_WGpADEMX3JVl7D_qEp11uFWCkORgqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=WukFArRIRLt5-XIqGU4kc0jR9F37Y6nztxNe1TwTFHQ5bjzX8iHOw5Er4lUZiyP3r8dbugJcoNO7io20QphroTpQR6pBUF4RoO6-yq7ZmQvhSI7jzA6mfYZtfujlZrV999NgCfvmXCtzuWgM4_2YrO2YUymSaFgnBwzfFgKGTeHBnwgJsWKy7K0xQxWSDsc-duH8_kimRBwRcv88r7udQdHVA6lTzah93yvmy0JgIUDfoORpE7uvEDoUOGx-goSFFIxsixH4m9FFfurVDhq35Fwg2UlK0lzAZuEJrXdsPxEckpwyklkbGHd_WGpADEMX3JVl7D_qEp11uFWCkORgqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=P80K7Mny2062iAQO00lMDQicgWBPeGR8Lrf93z1lIR1dRQRr3trXQ7zPiXQ8fbRDepy3ufLrXQV_LMFXGvpacjAELXEIroQJzkF8bGJ8vGUivOhSs5o4FV0RRFgfJXEJUG5kDPCVD9gKtc0IUP2qaMnjOf4AM-876-_b7H_HmZw3dNygssDU05eywX5ztFVGJM9b2MDBoSq5tp8uogr_euNE0spAQeLeso9HXXeNWB94cME2e3eNoScj0EXa5iJ1Ezqxqu8q1PmvRclUy1ug4esstzQ_C4BI8CffX-lyNhFXxwa1dS4eBsNoGvXoJCtcmUN5Xi9cN1iRuROezYh8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=P80K7Mny2062iAQO00lMDQicgWBPeGR8Lrf93z1lIR1dRQRr3trXQ7zPiXQ8fbRDepy3ufLrXQV_LMFXGvpacjAELXEIroQJzkF8bGJ8vGUivOhSs5o4FV0RRFgfJXEJUG5kDPCVD9gKtc0IUP2qaMnjOf4AM-876-_b7H_HmZw3dNygssDU05eywX5ztFVGJM9b2MDBoSq5tp8uogr_euNE0spAQeLeso9HXXeNWB94cME2e3eNoScj0EXa5iJ1Ezqxqu8q1PmvRclUy1ug4esstzQ_C4BI8CffX-lyNhFXxwa1dS4eBsNoGvXoJCtcmUN5Xi9cN1iRuROezYh8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=L_ctncmYqykZcnazPStY2WZWPiG0vCzppc-woC3h96xtXlpHLgHuqpFeYlGU53hnb-mknN3sOhWJNprkmu3qZsnZOZxqkVY2I12E1zaqs6cIteVdh1gWgEojiWrDpWIXhAv7jQ8fWlLW_Nf0z4Xw_lw76zo81yONUu_Tac6W4T2mm_xcxRHQOFH3j6W90_B0ZrKQCLoWHrYzqayBZzWdbTUW7YqDojiPIAP-yVOfEGiUk9RyefKCAz6j4126PMv8j9YC9aK_jgPXu4ucNdQBNl5zgWE8czU07xZHEw2bewMm_sDGpqZkmvxMDJ3CnIqGYu9bEhKiEGmv7KuCLiyfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=L_ctncmYqykZcnazPStY2WZWPiG0vCzppc-woC3h96xtXlpHLgHuqpFeYlGU53hnb-mknN3sOhWJNprkmu3qZsnZOZxqkVY2I12E1zaqs6cIteVdh1gWgEojiWrDpWIXhAv7jQ8fWlLW_Nf0z4Xw_lw76zo81yONUu_Tac6W4T2mm_xcxRHQOFH3j6W90_B0ZrKQCLoWHrYzqayBZzWdbTUW7YqDojiPIAP-yVOfEGiUk9RyefKCAz6j4126PMv8j9YC9aK_jgPXu4ucNdQBNl5zgWE8czU07xZHEw2bewMm_sDGpqZkmvxMDJ3CnIqGYu9bEhKiEGmv7KuCLiyfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=IAL4GklR8ISJLi-rF43n2VRKO1095x2lnx8pn4j5ZX8xbbGJ5ZX678BYT0yx-m78D4u6CoV7m95mPBLs3duNd7t3r9hLey7L62WZqO7YxOn5kbtDcBPzbLQ0YzmxPxjjWJMpB9U_K2QoMEHQE0omwHvtu48NFcrLflFi_I2z41BuUe-E2uTNmZacoPiNaVgKwhUHYEh8RjofVz3EC5zEq4mImmHvUuXzuv7D8wQ_jvgMA2YKvdQOtNPmoxK5soDIKsBt2RLh09hi1qVLiYfAsg8RtRY6eo5tju2KG8KSNpaWVEQj_gUoom1BSdXlG9zwQuhn9elVWCQDjw2oW54pFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=IAL4GklR8ISJLi-rF43n2VRKO1095x2lnx8pn4j5ZX8xbbGJ5ZX678BYT0yx-m78D4u6CoV7m95mPBLs3duNd7t3r9hLey7L62WZqO7YxOn5kbtDcBPzbLQ0YzmxPxjjWJMpB9U_K2QoMEHQE0omwHvtu48NFcrLflFi_I2z41BuUe-E2uTNmZacoPiNaVgKwhUHYEh8RjofVz3EC5zEq4mImmHvUuXzuv7D8wQ_jvgMA2YKvdQOtNPmoxK5soDIKsBt2RLh09hi1qVLiYfAsg8RtRY6eo5tju2KG8KSNpaWVEQj_gUoom1BSdXlG9zwQuhn9elVWCQDjw2oW54pFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEjJAVy7Gh0hU6FIUq84UY04SZoqL_8SBol85f3JC2J5BLWKoVL75T_l5pRTDDaqmPolsSBUr8m2xO5S2PFSfX-nV-nM0zPrqoLpGru2rj4Qvd8PCp_njM4osFzFSxSRkUIhWADuI0zJkooHKjs6VhrO0KV1d1yKwqZywbps421L6sB6iOARVDL4UQGkiPKOYKR7oAwiF5oWOq2HjemjEkIcudAUVKZpQZitNHEjUNfz7XFr80EZCgbV6Q-6o7hZuYTeuhpN3tw1TG8GC6Oz2md7p0JXONMu9EqAEI63i_zUlzwEpHmmDAdk1BIe7FYB23VbtrZug2Y0pMl96opNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=IsLMHRNOGjHVZVhvLW7F7vPPVdBxGTXEoGXns-hdo8G8zVc1ZBskOJvpWfE12XmSX2XMdWnICDsRTvEl84tgCIfoQL-gdNhx3LcVejiOOKYKCjEHQ4D_CQ7wSqkCAHva-xZgryclXs3weiBzt0L_EHhe-5H-xk69gUmI5jGqMfcLcwXcK1Fv2jzhlf3o0r-ljepryZnKzoOfTFIxx3pDUV-TgjIkuBUGeeaFK0Zq6Zn6tKFlHVReQlEGMjypZ3Cc8PTf_rom0ueshhdoAXPiiUG1p-Dy6U0y2JE6TRZDg5OWnqzKFeQRk3ClSexWaJqg8NFqJ1alGAr8IJX3lp10UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=IsLMHRNOGjHVZVhvLW7F7vPPVdBxGTXEoGXns-hdo8G8zVc1ZBskOJvpWfE12XmSX2XMdWnICDsRTvEl84tgCIfoQL-gdNhx3LcVejiOOKYKCjEHQ4D_CQ7wSqkCAHva-xZgryclXs3weiBzt0L_EHhe-5H-xk69gUmI5jGqMfcLcwXcK1Fv2jzhlf3o0r-ljepryZnKzoOfTFIxx3pDUV-TgjIkuBUGeeaFK0Zq6Zn6tKFlHVReQlEGMjypZ3Cc8PTf_rom0ueshhdoAXPiiUG1p-Dy6U0y2JE6TRZDg5OWnqzKFeQRk3ClSexWaJqg8NFqJ1alGAr8IJX3lp10UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=APv4CtRrSXGm0apT9fzxAPu7EK59N46NekSTND-lcRWRCXIEaXZfeQnurQN27Ho7Lj7bHOL6DG0xIn7tTLA4Pe1I2G_pBOVGaxmeBkEgiEeWwcsUexqgUEDvS6_TB7I4W4SAQtCSlK_oiJDt3ja_5IHJyWF0r6c74yeFPpmDeN_pmjXuk1NjGC_vPQgl4nCE45XsWOCZ8i0q2yjo0HCQip34l4unImBF0TUarQsMoa42PmF5spqft2CmKQKd-lKSEXzI3CjYP_ZSB4hNn266aNhexKGHjb33N0_xkHCAONrN3rMFZkRRPb73INI75nvSOKKYjmQRnxJIS3P_5K8rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=APv4CtRrSXGm0apT9fzxAPu7EK59N46NekSTND-lcRWRCXIEaXZfeQnurQN27Ho7Lj7bHOL6DG0xIn7tTLA4Pe1I2G_pBOVGaxmeBkEgiEeWwcsUexqgUEDvS6_TB7I4W4SAQtCSlK_oiJDt3ja_5IHJyWF0r6c74yeFPpmDeN_pmjXuk1NjGC_vPQgl4nCE45XsWOCZ8i0q2yjo0HCQip34l4unImBF0TUarQsMoa42PmF5spqft2CmKQKd-lKSEXzI3CjYP_ZSB4hNn266aNhexKGHjb33N0_xkHCAONrN3rMFZkRRPb73INI75nvSOKKYjmQRnxJIS3P_5K8rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSRQEADT2eM5q5OunkFHl-Z65S-yEtmvVgugv1yTcJImtlGj2V5XO3F8No2BvvFoP0YnwpFNntV_ZvIul2A3rFa9V4UwQx-e8Ktvu5FGlUs8etEHyIpAVNHwOEYsxSH_5GOI9XN3pEM7TUBk3m8SjcrE0XjbWiDsss5Nip94oZeHQi_TguRMk6ocNChSmHCygHRFJmtto3RPPyCUqG7QQJxl0eFcRzKYfL9kJux4t3O7rfOTGwPX_YmYBClnC6J3UU740yVAboNkiLVe1v6CxkXAhQm_RHChWsgXVEU1ReSLKNkLgw-lWzAeSBnbgbdm48-UUoEFV1uM3FczNw0myw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU0uTsu3ZyVrqjOADOoVXvywhXEtVr8aQ3_uzGli3TyJI2thNHhSnEhaOzHRhbEPxyB4HAd0wjFmkXePPyExFeZPrlrnlKO7IYF7ksROpVGc9txv-IqbHRHQErbvfieXiV7e0kiM-6FG9r_PYYuBKjhrp6cHncVgauMJQggVxmqVFmVpt1rMG8WINfVNrXyev-CKYg4U1P3tTn6XsIJIyc2MkwFk2cefhUaGaVedGnYAGLtIaNnyJuz6aQNpZdAHVrX-GUzG2aqcJ9PqungyeWvBy3TclfyWgI8jTyK7pTO-5dhZgd8Rb2G1GaNufzkjQf_y-V6VqEpVFIMBar3ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7u07d3OlqrCe2TGVeChufrOg4ykEKiyLUhk_PAMagTkokIq4n2I0vDYPUguOLcnnpXAK3yeXUYFoahOpAAunf1bAsEIZquIXbBTA5IVRjrkHuX4QnjPXcu_Xrs6SazfFwa3C2WBvRUnoGDNRAWVfpGwnr03kFedGlq7a5-HjnFmr7amNtiI04TLlKic4npv7VJ7t-JqrdxxKcy55ALE_V3ZvH2h0CFtR8xQmok9JzyW0Pe7AQ2BeDmcGDDcYFXUeblT4zfsFdI_r5YgspoXXekKfDT6_hDirphYC4FWe5Cdysuc-msbQZgFrxvBhOKV6F-Kkpq6d5k11Ip9wr1zTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0aVvQLUr4_BhMgV84FVYN2DHGaDFS-2y5utexR0tkB4N-Unvw1NoMQTaD5-_los1fmPtZAgIiSLg8UpTKif2ZBTkxeezOufvCbh5LpLhs80cmJq1aftxHPYBAt42E2jRsnNqWDJnLQ46GegCTLp-zYfO7pCTIt-RKY1AHmoxg2L97bkOQiipWuqh2Y_KYXbMp3UBTnXp4kfzZllJWrInSyPJgJhwh5IfASWTWPLeG4i2e1YYqH94pBEGJcxGTv0IHjiQZz2ooQG-JqdqRBZzlrz73O2njNmGOgLyI5CySXUZfQaiIRQB4AcB1LR3mJWtiAI6OX3f36NpHNZy_ngxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuSqPO26mM3gIP_9W7Q7GsC4YCfEVhGQftCA97OJ5n-77nNP2vIWWd0RIaTEkHZNebqaceVKwzlkLVHic7KiTzCgwqyCJ88NdQAF5uGUbBW6X78Cbz_Xq5Qy1QZJgOPbSOk8daJMxZ6CiRxEKBklUTYKdm1iFhDtEngeFuEbqAopZzlXEZ8tZGGKZjY_vnguNUf8Vze97XxObfidxt3bg3SLhowLCHMeCFiqVj18aV9my6D6LjHHsQnr8BDYG9r7hMv1LNgcrCyWsvuXs4mNatQgDK52CsNRTFsf-94fCcJgAPZTGBzFjio_aFUIfdyr_7wZCgozzC8h0eyTNIct1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYMewnshgMtANfRkfgzrJV_BPu7us0yHpc_VK14fVJrVWsffeBHyKjEoqI1O3TQfys9x4qRlklw5tpHw0XEweF2JHwRNMipYkmvuSoa4tePHMsvuEvrlnUOq66DyOvn-_M64Z5Z9kGaeHvN6a934k_iAgKGGZJXPOrm8pPMZ1RU2od0tm36HR8evkd3A8NWraZ1B1N9g-alC2nld9BmfLobvUEOUAyS4xzxh1E6Vafys8qa2ay0q1xAX0kQ-xu7jt4IjLf3-uNNDlply0NFSoifl5YgJTodFRR8rhmGfQ-hZK2_DTKELxmUslCgGeYwkq4UoMPnnJ9hm-RwOzj9rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3UEcG2m8EJ6vZelWzjfjCMDswu17qhWXCCpHshniisowsFUbifXWH5W3Qq5S8St3ejKLTV9hazjoIMsi-ebeYSsvqKIyfUvKRHSJRICtFDFrxDzLDsrgKgtkJVtFsgAAiL0oIk99TVnXETo61HqShQAcLOJx3OE_99AJGIltU2GhG8BDYLF65Vsgp4sJb5jHr8F6TcoRLP37Qi_vkVQ-OjXvRbYdfvTOzO_yksg6b0tXp6ERAW7zM2YjExql2KK_lMmmngv_gxsTE31AGr4RDSssPSpPPGM-fntEyFQfPcJ4eOR7YuXm0ff32u5EvtRqUdZMe-tn2UNV9SL6efxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VI28okobZ3j9sgITo625do2bh_VP_eERqLZCuL5sxt0LjfZ2BeXgozJHB4iGqOSbgRHEW4_WcI0O621jojqvYckIO-ZVzs4lBCymej8kNE6yifNN27NdcbieIJUgszfInjbi6jFynDVh2NbCGtoNapFe2XDIWXz36lF8IZt-IPKCjf0aNtFWIfdkgXhURN6Q5DZz9bX1el_oCfojJ98YV5pAWIBwRROSUjvq5eET60AtU7gPk3Jaar59qHlur-TfOtLdPs-lGktrp-6M-dNS-vyxBbIyuONPfXd2OJ0CfOJHkNI7fjaRMA5J-sepm-rvP6m_Znyfc21333BwkuPgkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0qYEX-sJRLJRcMxzvJ1nsfq3-x8S9QePX9mmIiPQm2YEgj26MSq1zlquSk5QD5adEnM4i3h0WauxJK6X-g3J2FOl49fEbfCCCfiUndw7TlxQI2rhjtQPFhrg4YDxiO-fBDVeQMf7cr2UTdZeKpekX-UJ-SXkYqCP2-0UxALsmJepfsedKHHa_JLaGOf1Q7vfer-LiouZrxvdeLhEEJw_qPWdLY11g9xzwBl-5TjUMpuhTJ0ZobHNwLZsENb6EJswj64vH5psBWblty767zxe9G5s77KayN5eWebYGvkorLSrD0EHl92Xrptr_3ZR3S7AOwNTjXrRJFpSvvmdIzVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouRvAWEXuk2NdvobHwSJmXLwzirmDfd86zeR3IqY3zNPYVSXDmqbjMs4GSvfwFuIs3gBt5bDFQIcH0hRlOysstgNxx4NGVpXtwxTd0WyG-MvBKiVXl0SWJhXjEXM0JzaMy7oEVbBE9e5POXu2fryXj4k3QRlgnrEQT_4W48WxM0bLbEnmdmRzWZvehQLE2ONqf7WshYBx7iW5M92XPW_KCCGfiAlFmI_kqA9rh-KGEonaKf4pFQjvymlDP5Q3kX8ZSP-Ex8yu4i6ce_sO7WlTr4vTXJsrHOODxDinL-uyQYQjjM9iHQE6rM9fTp-CyfAiNUbth4K7s4l4x7JtXUHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC3g0XjO-sxlEheJdrr1dB_xu5VY_ncM4UfBDZB7iyf3lLBHPT1_0ixwjuHJqAxxrO8S4Zss4zQ27EKXNB9DFVxHsd_xxBeDRrWlGGZjo97vgMcfzeHZl6ExT7_XA4pXPguWFt7PLcM8W56thwPw8FUnPY2G0rDZYaxHtm5TpjRGOpT3TWwDYl9FlIN0WZRNKXR-qzTsRPWPP9lM0IqkCruHWddfHtdddxVnSu_7UQzbsUo-rinFEauaBfifmQV52axe87XOlUHnDZ8STV4-cptIRM7731qpgliVTMxeW3zsuJrAbqBKAIxUSt8obObFc8xVcimc7r-0w1uLnCA-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhJ_psEDaw0n4Qey0WnIlYJGz3e_cZyxr3OEAzR5wygAQ5B4-R6XvwKeTxqbyWAodwuPEfaxBseUQeGw_WFpVju88986agfQj7oAzFzANC9suzik_bKAWkekTwykGbnfsoPmCL_Oir1EwLnwYWpU-9j4CQ6CZLkCaR_MtpCHn9krFSH0KlUobCYe5VH5AETeEJGqDSgJCNFNEo4tlvRi_V9CnWx5f9HqAbMNL1XESfjLwn8kIxa-IBp_O1NicInRwaoKxqUBvqkcV0-Bg51jtTwEjgV3dLWHKx3H9qQ5L7kDORHDquDT2n41qMcdqMFzxfrt6NjWz3bUvSznTGUFQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=DED5z0d9A-TSL0zY9kgR3ANWMBmfFjQ7i9rdvZ5m6V2k4V0GUDX9L0wQ84gST-Vci-CYkHug8wbnZd0ItnDlY6Iw6WP9xPU0xVqG-71ubLr-qG3_RnPzJU2lWo8iaal4KvV8ptFjCsA65nZQWQkpzAbtRROHCw6E_Q_ksAi0ov2mJg4MraS-xF5NTuzufCWJtnWD7bnILCTVT7Xi6F3BlTSc3lBkKYWP_kzL2iDqXkxYkJMWcl-ktLQ8mqLmEZWQ-WhOpmjgc6zbtcAggoIgh0eDhPDB1TSOuCsv82BJ1XGkCL2nKNIaFRLLP6NXDzuKFPg8CeGSH0QGVW0gcttTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=DED5z0d9A-TSL0zY9kgR3ANWMBmfFjQ7i9rdvZ5m6V2k4V0GUDX9L0wQ84gST-Vci-CYkHug8wbnZd0ItnDlY6Iw6WP9xPU0xVqG-71ubLr-qG3_RnPzJU2lWo8iaal4KvV8ptFjCsA65nZQWQkpzAbtRROHCw6E_Q_ksAi0ov2mJg4MraS-xF5NTuzufCWJtnWD7bnILCTVT7Xi6F3BlTSc3lBkKYWP_kzL2iDqXkxYkJMWcl-ktLQ8mqLmEZWQ-WhOpmjgc6zbtcAggoIgh0eDhPDB1TSOuCsv82BJ1XGkCL2nKNIaFRLLP6NXDzuKFPg8CeGSH0QGVW0gcttTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=oVNqMI4kJlq0glFWHzsckA-hrpiTvaJXHfE8PTLXf3F1GHxdZa45QNGFrXeYtb1T027zzkUzVcMq2SNeTRPvVJouWSWqp0uQSNaADb2Dxhr9kEkNFFUyTMmGnseqS5Lqi7VPwzcz3Zh0x5PqGgrJDP2pa1NxFdGhQj9tgAa92nNOBoWU4RL_ho5Kr2tPWBT2g_5IURQZa2l9Zqu0ka3Pzb_yZ7bSKlksDQZ6Af-FYDzu-Z_oedi_MfQzEkgy4EvuKHcNEQMhlDOWucBeMZez_ZEVPn6V9e8xveCq3eiAmLxWzZaL0jpObi5_cQCC3U13OzPh7ftBFmsLunnyrRBrjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=oVNqMI4kJlq0glFWHzsckA-hrpiTvaJXHfE8PTLXf3F1GHxdZa45QNGFrXeYtb1T027zzkUzVcMq2SNeTRPvVJouWSWqp0uQSNaADb2Dxhr9kEkNFFUyTMmGnseqS5Lqi7VPwzcz3Zh0x5PqGgrJDP2pa1NxFdGhQj9tgAa92nNOBoWU4RL_ho5Kr2tPWBT2g_5IURQZa2l9Zqu0ka3Pzb_yZ7bSKlksDQZ6Af-FYDzu-Z_oedi_MfQzEkgy4EvuKHcNEQMhlDOWucBeMZez_ZEVPn6V9e8xveCq3eiAmLxWzZaL0jpObi5_cQCC3U13OzPh7ftBFmsLunnyrRBrjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=WZYvlzeQEyAf6EcKFUDZzNTHTyM2TQTsJfWbZF3xWe586FEwOsmzzVHkbq3yJp-XDKoAPPxP2ymKCvws0Hz0EPQ35PLAGi9CofDRUp2Pcyn3Md81kST7BhzWN-ho-j8EMBiDDBO4BH5Bk_Xbpp1-xmb5z97yFF-HCw02O2-bzuzA3O5Vjt0ybjdqe507R_Wo86tjWcmOfHq9bS7Uns9dhQajKQo6dJCofRElHzx6Cyw-VLuyjZX5KMJfnXusxC85i_Dqjvks5ypqW1UygpmtdrVX1h0QpyCmx_GRt2vqJjMisT84XmM5iEGUz5tw8TNcLTmALpR-sRleDsdlO-_kxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=WZYvlzeQEyAf6EcKFUDZzNTHTyM2TQTsJfWbZF3xWe586FEwOsmzzVHkbq3yJp-XDKoAPPxP2ymKCvws0Hz0EPQ35PLAGi9CofDRUp2Pcyn3Md81kST7BhzWN-ho-j8EMBiDDBO4BH5Bk_Xbpp1-xmb5z97yFF-HCw02O2-bzuzA3O5Vjt0ybjdqe507R_Wo86tjWcmOfHq9bS7Uns9dhQajKQo6dJCofRElHzx6Cyw-VLuyjZX5KMJfnXusxC85i_Dqjvks5ypqW1UygpmtdrVX1h0QpyCmx_GRt2vqJjMisT84XmM5iEGUz5tw8TNcLTmALpR-sRleDsdlO-_kxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XMnrq2kFXGk6ngP4yIUL4f9KmY0ihnMqQaOe9ETzMAjxMV8df3l3_YzY-ccqweUVrdTXHSdFwBls99tJREu0TpZO4GWs6CcuJ3us_USANzzH0Acn75OSNKaJoyPHNYUtyDIz87wHyxQZ41RuWOdlkTwYNiUzAtQzEvIzlXDPRrFnA8LBec2FCbv399LrJSWQk-VJkjyRvHdLhLpfMWJW5zlupGZEWZriJoEyokd8upnQJbncWn6UvkHK655bvygAgK0Q6WLoKk0ROxAS5pkre8DqwcIwesDWuNsagQSkObrf10_e1_HTQDMa0KaKVKFw8tqQT7LmFIO2ZooavGwVbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XMnrq2kFXGk6ngP4yIUL4f9KmY0ihnMqQaOe9ETzMAjxMV8df3l3_YzY-ccqweUVrdTXHSdFwBls99tJREu0TpZO4GWs6CcuJ3us_USANzzH0Acn75OSNKaJoyPHNYUtyDIz87wHyxQZ41RuWOdlkTwYNiUzAtQzEvIzlXDPRrFnA8LBec2FCbv399LrJSWQk-VJkjyRvHdLhLpfMWJW5zlupGZEWZriJoEyokd8upnQJbncWn6UvkHK655bvygAgK0Q6WLoKk0ROxAS5pkre8DqwcIwesDWuNsagQSkObrf10_e1_HTQDMa0KaKVKFw8tqQT7LmFIO2ZooavGwVbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=aqxLHkdSkbIYQnRq42KnuIOWzuZYZIFVDQE56268CcUFZpznIaYG8_1aYCwLBtIawvVMcum7sNIdf2cB0q7bCh0wSrRcDFCrTI3Cn59ePqnLBv3HGi1IZgsCwkg3BxKREmt7CFG3ujrDPoiqHJgyNYP3_u_nw6OZxKpTL4desxbA-kiJY20QHJJrfwIyFiWziTx0agNaYQrgTp4UGnPdpWc-adcbh6PWvRGxO1YT-A0iWnafGUNH5zW2hLx1EHoVScRAa-opI1ngenWlpCjYOloYGBi2mWGBFK21PUaU8RwtgX61qqQiTOmcpRmjsRoXl87EhmjyDDGCSsYcGnHBHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=aqxLHkdSkbIYQnRq42KnuIOWzuZYZIFVDQE56268CcUFZpznIaYG8_1aYCwLBtIawvVMcum7sNIdf2cB0q7bCh0wSrRcDFCrTI3Cn59ePqnLBv3HGi1IZgsCwkg3BxKREmt7CFG3ujrDPoiqHJgyNYP3_u_nw6OZxKpTL4desxbA-kiJY20QHJJrfwIyFiWziTx0agNaYQrgTp4UGnPdpWc-adcbh6PWvRGxO1YT-A0iWnafGUNH5zW2hLx1EHoVScRAa-opI1ngenWlpCjYOloYGBi2mWGBFK21PUaU8RwtgX61qqQiTOmcpRmjsRoXl87EhmjyDDGCSsYcGnHBHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=Vsvigzxg3akAuQcddcYNiXNekQT2_2KHhLbl08HiGNCRIfT3SF1W923fCV80AhPgdZsRefRvdBqntPtjjzFr8WAs9q377kKsS1GuoArRi3P1aOVRRu6n_FbBhaokZ1FzBzrRit2UP_cTmQwmBwWLFKqqOJv8yUjRiX3SReKcIc5Chzi_pQxXkSRHFWEoqhzLdntrlzIMPxAewYFvhCcnNWQSHZd9kHxo1hIUEAJLeCC7C7K0spl1iGPW40JW0J8R63HCSWvAZ1c8kyhBxynv77H591Tb_4oOAHSsKNm87PwhX-sizQ8OGpHQ-ClNB6sT3yvaKYeMbHuoUitIz5gXkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=Vsvigzxg3akAuQcddcYNiXNekQT2_2KHhLbl08HiGNCRIfT3SF1W923fCV80AhPgdZsRefRvdBqntPtjjzFr8WAs9q377kKsS1GuoArRi3P1aOVRRu6n_FbBhaokZ1FzBzrRit2UP_cTmQwmBwWLFKqqOJv8yUjRiX3SReKcIc5Chzi_pQxXkSRHFWEoqhzLdntrlzIMPxAewYFvhCcnNWQSHZd9kHxo1hIUEAJLeCC7C7K0spl1iGPW40JW0J8R63HCSWvAZ1c8kyhBxynv77H591Tb_4oOAHSsKNm87PwhX-sizQ8OGpHQ-ClNB6sT3yvaKYeMbHuoUitIz5gXkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=iUbfFwgXgugFhheFYAe750Bbyu3inV-n1BSTppkdvdrXLiGlN-TeGC21MnBnyYosR_cET0DuRgX4ue6q4TxRxr22KwCgNexM9CA3s__bhrPpwRPRcrsPwuQiZZEWppwX2W3vC_ZKqbmXbF4ZdeHX2ZW9UPFh-qHasPhVtvjWObasV3PKZu6PmnUdcPF4FiYx1e3MyQCTJJGSQ2gnFE8QzPhXGWtoO3lMC5HTDmUp3M7Z1jyAXYYAU_ZsdYMbRroL18eiv1-obbeKx_yU1Pkfl0IJI19MtAxrdIe_MRMKnDlfJuTkOeGa1_HN-YaE_WIuLbUNalllSn1xotfABaQxcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=iUbfFwgXgugFhheFYAe750Bbyu3inV-n1BSTppkdvdrXLiGlN-TeGC21MnBnyYosR_cET0DuRgX4ue6q4TxRxr22KwCgNexM9CA3s__bhrPpwRPRcrsPwuQiZZEWppwX2W3vC_ZKqbmXbF4ZdeHX2ZW9UPFh-qHasPhVtvjWObasV3PKZu6PmnUdcPF4FiYx1e3MyQCTJJGSQ2gnFE8QzPhXGWtoO3lMC5HTDmUp3M7Z1jyAXYYAU_ZsdYMbRroL18eiv1-obbeKx_yU1Pkfl0IJI19MtAxrdIe_MRMKnDlfJuTkOeGa1_HN-YaE_WIuLbUNalllSn1xotfABaQxcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrbzrJTg3UjVXeB9AG2gHZETEQZiFyru37h2PV4eCQ0uCkcG8QPjXU2mUz86x4RtOapq2UznDgA2PhbL3Q03vLyQ-2QsOsfYbBIZfCzH8wIsAJ3ey12FXkZFtQGuok0BmBvL5W9Uw_FLrXbVwdoAMR9dRr7HPIfF-bi1UIgg5020jwWWREWTWYiT6iV5ADYmp_r6jnf1nReFBuLl6wRFYu0WqVigLpNZarWVtjzAZUd6D3VrMh9MItAsZlu4gGKLVVJDrH6XaaisandcmvPI2hni2Rjkn1Qztob6T6cMeq-osBIQZ8unRi6X80Y7xy0OADIY7VCGwZf4VRvQenV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=JzgNVSJHXj6qgpltt4FekymNESJ6qfzayKxYBS4zYJsGbOLXvuYl97nKvjoK3ClMgPAsNp-nDfNIj-QEhO8CV0jOdC-OuwJHX3rInUvME0W9S-byTqPWOEaq9kdMcNiD-66SfP02iBMl2KFQBxpNKwWJGr_rotT8abgemoN8kKDen5Chhk_A94A9S41JbFS2-5K5sLdftceLU7_wzcZ5Sun_4TuWYAWuA9Fgon9HpFYhhwrddBfcz1hd3gCW7rItSnoLyg644GfqlBeBo4r1Qseh371euFAvyNFAlTKfBYRIo7ITtD3iY1pfIfyvLyqgy6CFkiWsKO0SKrlJGpSBTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=JzgNVSJHXj6qgpltt4FekymNESJ6qfzayKxYBS4zYJsGbOLXvuYl97nKvjoK3ClMgPAsNp-nDfNIj-QEhO8CV0jOdC-OuwJHX3rInUvME0W9S-byTqPWOEaq9kdMcNiD-66SfP02iBMl2KFQBxpNKwWJGr_rotT8abgemoN8kKDen5Chhk_A94A9S41JbFS2-5K5sLdftceLU7_wzcZ5Sun_4TuWYAWuA9Fgon9HpFYhhwrddBfcz1hd3gCW7rItSnoLyg644GfqlBeBo4r1Qseh371euFAvyNFAlTKfBYRIo7ITtD3iY1pfIfyvLyqgy6CFkiWsKO0SKrlJGpSBTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ROD2msOv1u5754oiCqheHZPy709lUe5klEEhroOHBMJGhDJveeelKKVBX4oHcs6G7eAx4YQJlJs931TbRXoaViL5SCWVTeb8KUYvyEKGj8Vep0UYXGpw5Ao4PTUnmO6cFgahNo_ypLILYlKvQoJKz2myyv18GXAIOSZs_eiZS8Azhrm11pdRQouaeh5hs3ko1rJBsqYzMX744IPYp-uHJnp-s-k-fEZ01DFgH0z7kuHP2Eqb-LitStf5cOTRwdSbwgCeDSZEWK54ucIQwGUwzZgZNYHPeptjDmD-H2gVgGHjcYeJNCkEZ0GbsjSIsIH7e6velzOb2eAWPn8lKIieaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ROD2msOv1u5754oiCqheHZPy709lUe5klEEhroOHBMJGhDJveeelKKVBX4oHcs6G7eAx4YQJlJs931TbRXoaViL5SCWVTeb8KUYvyEKGj8Vep0UYXGpw5Ao4PTUnmO6cFgahNo_ypLILYlKvQoJKz2myyv18GXAIOSZs_eiZS8Azhrm11pdRQouaeh5hs3ko1rJBsqYzMX744IPYp-uHJnp-s-k-fEZ01DFgH0z7kuHP2Eqb-LitStf5cOTRwdSbwgCeDSZEWK54ucIQwGUwzZgZNYHPeptjDmD-H2gVgGHjcYeJNCkEZ0GbsjSIsIH7e6velzOb2eAWPn8lKIieaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=N42oyogv3Fx2YL2HCHR1dcHlqIwY023tdciWVNdeEbK0QxRw-GuiYctpagj-ZsYROyriGKvfOdmkO682Jzw0tPKhlxCk2AdJkz99W0SSTkdrDde6ds7uPXs22OevbVwLxP_PDB4o9RHoQq1YH2oGjlM383VSjP6aEudnlO93bi4kMg8N5q2M_PvGEhSnmGXsERn5HdQJEifp_DNvWwvuGBAlAKArecibol9-i9D-CNt0ANnssOhULOUNtGLyVHlnzOtQJcQpOyuTbzbo3CvtUCuh3WnwzJVcxrPFetCABprWhhmUzE-jKmu4JSYJMbI98QOL52dOaBzZG5W76WXcfSwTUbo0GOTqNJzHsev5n6_yg_lQZ7y_MuQIBwFMb8OcdBolhjJf9kfK--q7qw7G8QBOctTcuGWnLV12R3sD8lha4TW7LVCZWjMookU9OV-xBDc7zEZBOo3vW6zQFGMxAepxYxdN3cGuQev7HCReJD7zm8yqLpTLBahW19nAbU87-xSl9EE0A-vcGx7UyzeeJULs9Wg_LXxGOS5D9S9eR6kxyb2WWGGrjKg3f7Qlsh8Ym1I1QrXhiOpETHK4qBCjnCsnTd1wPkNjT2WgBYbP7g82jL5CzJXZbYycP8F5xjJvjdCkk7KUe9Q-kul4cd9n7yqmBbl75jgJviOliTa6yFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=N42oyogv3Fx2YL2HCHR1dcHlqIwY023tdciWVNdeEbK0QxRw-GuiYctpagj-ZsYROyriGKvfOdmkO682Jzw0tPKhlxCk2AdJkz99W0SSTkdrDde6ds7uPXs22OevbVwLxP_PDB4o9RHoQq1YH2oGjlM383VSjP6aEudnlO93bi4kMg8N5q2M_PvGEhSnmGXsERn5HdQJEifp_DNvWwvuGBAlAKArecibol9-i9D-CNt0ANnssOhULOUNtGLyVHlnzOtQJcQpOyuTbzbo3CvtUCuh3WnwzJVcxrPFetCABprWhhmUzE-jKmu4JSYJMbI98QOL52dOaBzZG5W76WXcfSwTUbo0GOTqNJzHsev5n6_yg_lQZ7y_MuQIBwFMb8OcdBolhjJf9kfK--q7qw7G8QBOctTcuGWnLV12R3sD8lha4TW7LVCZWjMookU9OV-xBDc7zEZBOo3vW6zQFGMxAepxYxdN3cGuQev7HCReJD7zm8yqLpTLBahW19nAbU87-xSl9EE0A-vcGx7UyzeeJULs9Wg_LXxGOS5D9S9eR6kxyb2WWGGrjKg3f7Qlsh8Ym1I1QrXhiOpETHK4qBCjnCsnTd1wPkNjT2WgBYbP7g82jL5CzJXZbYycP8F5xjJvjdCkk7KUe9Q-kul4cd9n7yqmBbl75jgJviOliTa6yFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QUUrx0-RTccFtlDjyifY5JKbWKlcgfY2nqEPsN87CmkinZwNoe5L5o34Cxw_eD75CNQXiI1jjr8DdiuKoAcEas5Xsm50S5gHtvU6Pr7PvlpTsjp8-h5B6__o4Co8dBMJ-Io9adbB-g9ncIgoPYC97tR0qD9N1o8wzYQ8pzdFeyzcP8vNi1JTZfwALz1mWCa6YCCB_puB5plWVpt4TfmaYODpfJZx1L4Abd5INi29vPk9m1UfQFBpn0M0GN8Vu9S-hkJYuWriOrohQEHOMUJXOq1CtIBxT8SnhUQi8DS48gSU82IrGZQVGH-UUhbZQMTl4KHmKNS6mrh9ZN9fNSW7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QUUrx0-RTccFtlDjyifY5JKbWKlcgfY2nqEPsN87CmkinZwNoe5L5o34Cxw_eD75CNQXiI1jjr8DdiuKoAcEas5Xsm50S5gHtvU6Pr7PvlpTsjp8-h5B6__o4Co8dBMJ-Io9adbB-g9ncIgoPYC97tR0qD9N1o8wzYQ8pzdFeyzcP8vNi1JTZfwALz1mWCa6YCCB_puB5plWVpt4TfmaYODpfJZx1L4Abd5INi29vPk9m1UfQFBpn0M0GN8Vu9S-hkJYuWriOrohQEHOMUJXOq1CtIBxT8SnhUQi8DS48gSU82IrGZQVGH-UUhbZQMTl4KHmKNS6mrh9ZN9fNSW7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=fX0fajJuJQFfX9-aRGn-Wxm4-gx3UlNrFpM-vZ2r-nlCxM_dm2mV-amDDDI3uElcrNykYE6NnThEXn9jv1LZLRdeW7Ji-as_2c1Qm1WqHihhoB2rWp79bW415k4AKBOnGCXpJEVUWVQi0c66xmfRfLZ4tLm7S-yiwhnwfuHEA5D3wEZb0vszZ4iTGI_fcfpbnMS8_KQowceRDFys5MygHKO_p-cOJ-wpeMbyw1p172yM06aV--DUZWmMScir5GdzjDeIv5bOhmWASkoFlxKFKRKsov1Iev6j2InvJOY8kVhx6ToHx9DRMQQjSEINCLN8NMOpueDEk9XQqPLBvY6MqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=fX0fajJuJQFfX9-aRGn-Wxm4-gx3UlNrFpM-vZ2r-nlCxM_dm2mV-amDDDI3uElcrNykYE6NnThEXn9jv1LZLRdeW7Ji-as_2c1Qm1WqHihhoB2rWp79bW415k4AKBOnGCXpJEVUWVQi0c66xmfRfLZ4tLm7S-yiwhnwfuHEA5D3wEZb0vszZ4iTGI_fcfpbnMS8_KQowceRDFys5MygHKO_p-cOJ-wpeMbyw1p172yM06aV--DUZWmMScir5GdzjDeIv5bOhmWASkoFlxKFKRKsov1Iev6j2InvJOY8kVhx6ToHx9DRMQQjSEINCLN8NMOpueDEk9XQqPLBvY6MqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL6L5UMP849aPSxHzVOpUMJd1ZH0-S-4-i79uVqnZRcOHDIHDglFBSYmFWD5uKVEHQoHySX2O3Ull394n0sd7dDNGGBBNZ4mHo84vPIkqLT_Qel1_FdV5U2E_HMUojpSx5UcntoXT88wqDG1gNgteWh6nQcUa6spilqtlvrAVnfpNOYv0EhCwEFBKPoxEa36eydQel4xxTwPardu-hrTH12b_HmbWGUmGyzFZ24fXe4SYUGfcJ1sm4dBK_cWJVfJ9wmZTN9Y6ZOYIO-ecMPOgEFUjdE67quLt20VtBpyftg0W_Zlb8iQiNy31W-rclEQV6dsEdV7-f06_uYWnDR4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwr48JJPYF2PoLQ4KbV_DiuEmsTVAuuFtdwWRdYn39DjqQcs_4EMkDEYlDVlnQJmwWIyuie2e19knMH6XyEcm35RdUYbEo_ZUONd9-K1L04NbVlmbsUzbaZFvtDVr5mmb3LUbM7E6RS76awVQfwCqsfdaT_AWq0o4MRoK2PpgsfmNtEXhOvODN_Gk1il4LGUbVPSRpjDMybKLJ6mSJpqJXwLObpBXhSBLZhjE__FuvOJPFLMJsuGX9Z8pAiDlMcXV_l4UlcGg6RAk625lgfq15j303ixN9xIVKdMVtfes7pMToaJefmE-zN24lK3wMAVYxsGV2ACpNdYiKmfOFVjIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=rdFRu48e5IzeoOp7lUhz06H0CJm0NN25Xug1n6g7Li05ZGwcc5qbcxgggjBRuAKtBYqyH5ozUaUi4aNul31824uYrKcVk_qWZGSuOK-yoli998l_fYvlCiL0NscqxSYlpld0iUkkbvLG9mx96XAwxTVgfXA9223-GZS9-3qJRSNbN0hl1ub7xaQvQT-dAfcKDULC28Y4gz--5yM9ok6ldHLue-HnpuNzJ6xI2IBCw3X5kVqPCSW1IH1qvBZCu7l2oLhERHJAAI9e0scRi-IoEUa9kKt2tF5au32HB-0pwiL7kCKsz9faCPNttI2bbpW_UtQIUZWCLPakkfa-ub90iYhKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=rdFRu48e5IzeoOp7lUhz06H0CJm0NN25Xug1n6g7Li05ZGwcc5qbcxgggjBRuAKtBYqyH5ozUaUi4aNul31824uYrKcVk_qWZGSuOK-yoli998l_fYvlCiL0NscqxSYlpld0iUkkbvLG9mx96XAwxTVgfXA9223-GZS9-3qJRSNbN0hl1ub7xaQvQT-dAfcKDULC28Y4gz--5yM9ok6ldHLue-HnpuNzJ6xI2IBCw3X5kVqPCSW1IH1qvBZCu7l2oLhERHJAAI9e0scRi-IoEUa9kKt2tF5au32HB-0pwiL7kCKsz9faCPNttI2bbpW_UtQIUZWCLPakkfa-ub90iYhKG-cgXlPGCSycb3q8xltV1SYOxpdaYKihTgZl6p5Bw9DQh5NjI6W-n4d-0Klm2qsyQLYxyRTk6vRUuWrogDBIMSQhIekVZES-EZ-cA-zyj0EJqjGQvwMJYDzyVTN-VmEa9OC0I73f6niDenwtafe5KhQ0k_YU_DWo_EbGd-DOCey4DmfL2D7Drz8uJvIEMbSSvnyJ1q8rU8TMziE_efKh7bJrb_IEhb8NX7n9m8eEgsCrpKQO5WPTFEIG8CmORtz2K_0hXoKj4bCSEKb-toginoilCZNiXIEzKxG8cIiWcuqwMHqSldhil2ZPZt24srmpn0EsvI1yguhW8fjKoIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA3wHHG1lgz5HD5S6wFFoLjOFV6AgxiyfDZ3mnOm9GkRveJeYGviGSB5ud3oIhfBTZjKPrP5bw_MalMkbXMWtOWXGMZCRIcRG58vnzaQUBbBLVleXOcIbeJKgzZsUtPOo0F8RMndFcBzRozK2hIAuhG9BVaX8vG7haXy6qlemXSOBfVDcuPvNlxGAFqhwuYHf_4USYFf8WAZcxjw_YKjfkq44GaOIwN5FnzoIdbYJxhDMhWDTNlv7JArEWBM9r8OWxZl0U2kjW3roIOLk96yAutSlAmCdJHtuUm4cVuRzClFCWZi1y49c-MIK5NNbfzt5VmVCDbzeWft3EQ9vKiewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yb-rDTnmSuVjIlyb2WhR92FMygD-kKz5bgN3ama6T6JplFG7fj4s3nNAv9Knt9HlrHjzn1iWy0FwId9pwPMdWPCuueBR1Jtf7LqSM_yUUlMZSwzDysX7LOmMdLdRddNuO_rHVA5LIuQEQCToFkclYEsSP4CXm1hCw1Dw_YyG5UfA76U6HmqSx8jGF0_jgtmfc00r9sXWTFmuyhtHKLYZZnQBUtqYaxlc7lDP8v2Tvqk3swx-qRsOs62cDH1U8hq-T270vaOomNp93f4Tsz4nXrftbOgMwOlyBmDoi1mAlzWajgA2giYtFRaAN7YMpaCmKST-K7IcF8sI-7plJ3fF0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e58tMhKSTlRYpqipzK1e6aT28Wg-sEXROew80ihUHXnS4ypRHG--PG5eJQcr14OQQkz79YRWnZ142Rbmy7D0iW3PrmLzxHNQYMFcF3BGJfBK8JbmP6Y0lYJ8OTPvdK7wdzqYLjrRbpYEQcrEOktlJ_kZMBspsXaHPxJlcwZYF_hE-QNf-RuvXVtISanVz9dy6TBP65FsCmIw0_aoeaaUfZ4l0pVEbUl316-GgtqXOoSg805UfM5GwMtTJXHxnVpVoa_5z6t2GUQ-_vEelxB2Bt3JoXDf1weZHUDdsbxPVNdAlgSbiqpaVPWmwChhVf2zzcLD7U7gC7NqOMvhxl3pzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPDU5pxjYjfCc244g8fBcYnqUrtK9u-D0CPtvwtnSuowIN_Ceapy4q_H1wysLShTxz3iLPGL2mkT_-n-QzMBJLndrVIIxbFM7T7kDqE1MbscmP5ci4NKdGMP4CKv5V3sp3CL7qf_hsPICxBdQ_y0M_6pKAeW5ndaNcrQ3I5hsJvZSLxQqsYJnqbc07As-AB6u-tmK0dnM_XoQKomBmhJAiimYnnt4iqOZ1gEe5BbJbAvoIzT_AJKfoEM42ih2LPkVVbN3wUfgSlc0PgURmZOOrjlvHLDWKusCU5jvqPfceKRfuPBK1GjEmdCZiWfDVNFslaHSJIuxeB8KCT6QPYQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=VNkr13snLgQ7snzSwSoGzFHpf9MPmFIBsGqy43BnsjAbwLofSSo-a2kEN7WzTjtOo0CrE9XXIUBhyxV_MtMDLez-YgEOCay29469lQSBHgLKhYiaPjuLjpBy6n4eKmBcn480pgrofgKNUla1lp4ZGz7_PSZX-nZN8Ccdy03Z2qef4q-UK3tRH7ibs5GeJ1Yidb5kize_NKtBOStKP8HQ_zIq3gtLf7FoPZNk8N5PSPMKAIRQ9ZFaksAEM8F4LQMy8A1ky1PdQoub9pVIswoMUJUi3KOLCfqwwNGGgEmkWZcO5GVsYRVKi9FUEZNYjIKyUuIB_h8TnSOow2aV_u13yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=VNkr13snLgQ7snzSwSoGzFHpf9MPmFIBsGqy43BnsjAbwLofSSo-a2kEN7WzTjtOo0CrE9XXIUBhyxV_MtMDLez-YgEOCay29469lQSBHgLKhYiaPjuLjpBy6n4eKmBcn480pgrofgKNUla1lp4ZGz7_PSZX-nZN8Ccdy03Z2qef4q-UK3tRH7ibs5GeJ1Yidb5kize_NKtBOStKP8HQ_zIq3gtLf7FoPZNk8N5PSPMKAIRQ9ZFaksAEM8F4LQMy8A1ky1PdQoub9pVIswoMUJUi3KOLCfqwwNGGgEmkWZcO5GVsYRVKi9FUEZNYjIKyUuIB_h8TnSOow2aV_u13yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=blHRWDqKTm0AWhcntZWhhdZGFyqJhY6TRf6pTHYzOIwOTEkLMYoGDdCGX8Tg1SrU1EKPfvlPT3JhvV90ysOSHT1aWroh6uRBO86y628-D3FJeoV_rXT2yIW3b9ZyAibMhssAjrXF8Bb_30Y0oXO-ooF6Lwqg37Ij93bAUf1QaSL8Suy8qgQTNsGzUOBlnnEdCeJGlvcjB1CbjLigbCENIzFQSpbcuDhOercFqv5DGgKvhfWJmTJ2NUF942hyMp-NMYzlGCfZgBxG7KR4P93_f8qkuwnxmDXlG0ywNuYXbekLNsKA_kcJKPAwiqQRlNQ8xrL12kYE9yZcjh8YEPin-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=blHRWDqKTm0AWhcntZWhhdZGFyqJhY6TRf6pTHYzOIwOTEkLMYoGDdCGX8Tg1SrU1EKPfvlPT3JhvV90ysOSHT1aWroh6uRBO86y628-D3FJeoV_rXT2yIW3b9ZyAibMhssAjrXF8Bb_30Y0oXO-ooF6Lwqg37Ij93bAUf1QaSL8Suy8qgQTNsGzUOBlnnEdCeJGlvcjB1CbjLigbCENIzFQSpbcuDhOercFqv5DGgKvhfWJmTJ2NUF942hyMp-NMYzlGCfZgBxG7KR4P93_f8qkuwnxmDXlG0ywNuYXbekLNsKA_kcJKPAwiqQRlNQ8xrL12kYE9yZcjh8YEPin-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJx7iRtJo2IUK7uBysmY_Uon7OI96LV_SLZ4tMyEnpUcYfOQpkSVjPNwGl8-Tq_g55XtIvIWy6RSQiQ-WUFXJqi_XVpdK9WTzHw0CGvfAHr_ZPO8HZljO2tEXdprmt4mmd2iIjj3-bULvEvuUv7OrtRrhFRq7IiZpRZ2v_Yq729PS1fAqtYuplQMECLea40Zr_BTLxaR_b3evdJCe39Jpg0eGYAIWSl5jqDH5o9OcTg-QFgL_DnaJcIMDN0RqFTyb6F-jv3RQMGJghGw7_MHsSNcPlTCtyiS4byAW--1sLCTOkCWkaEQwqFukedjyETfgZj0OeOcvmGVr5kXAc8hSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=dfeANa0w3PhaRvAcSLAm4AMDlMl1pTyF9Ggax6WVT3pqbSJ_BAprw_BpNVLidG4z5S2w24qbP3fZzgG-p8MoZXjLJVRjUTnQ1ZwgjgOt2TCXhE5KyhHts1yUaJxch2FsHhV2EJ8vQkUB-ja-hzcLLxAM059Ak8pDf6-aZefU-kwG9JzbiqesnyI-1ZCJrj4uygbKy_1xZcEAiYe1xuhbSXEmQvkWqPXL_1IWHoZUwTeVLcqi4h9U6LZxgolxBPttCxHr1IyDNp1ie8a5Q630HwHzLom07mLGVZHg5wfwbvL6ebbJTas3ecaCuyWdu5IvOm7kOrv1aZvdc0CU2lS3VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=dfeANa0w3PhaRvAcSLAm4AMDlMl1pTyF9Ggax6WVT3pqbSJ_BAprw_BpNVLidG4z5S2w24qbP3fZzgG-p8MoZXjLJVRjUTnQ1ZwgjgOt2TCXhE5KyhHts1yUaJxch2FsHhV2EJ8vQkUB-ja-hzcLLxAM059Ak8pDf6-aZefU-kwG9JzbiqesnyI-1ZCJrj4uygbKy_1xZcEAiYe1xuhbSXEmQvkWqPXL_1IWHoZUwTeVLcqi4h9U6LZxgolxBPttCxHr1IyDNp1ie8a5Q630HwHzLom07mLGVZHg5wfwbvL6ebbJTas3ecaCuyWdu5IvOm7kOrv1aZvdc0CU2lS3VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=YSisJuLb10RNciDHAr5zg4kqMBN6lswjXpM2iuAxa1j9JdblEp0EjLET3Ld8Mletc7NhUVXwSlD6XiPlIO2QMTJjk7kUg0Qv1q0MyZrde54FyR-2ISJwPPbr5My2_cFRhOyk9PBmfZ2Dhd7F-r6vc5nwatLxbTfZRzFdCJDwqCW_mm87FQ8sNc4QjJ1eVOF5Fw9DmJF4UpNuFgW-HHsB6o3-YMuTp-tOZiAn-jTtw40oQhW0L93yis0S8ffIGDZhLt6eEP-1HBxizbeAmMM3nmaKA9Q9UhFKlPniS8DHPVWj7f8pKOA7oUTTwsRR_BhBrxNKDY-tvpx3qLcEeydwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=YSisJuLb10RNciDHAr5zg4kqMBN6lswjXpM2iuAxa1j9JdblEp0EjLET3Ld8Mletc7NhUVXwSlD6XiPlIO2QMTJjk7kUg0Qv1q0MyZrde54FyR-2ISJwPPbr5My2_cFRhOyk9PBmfZ2Dhd7F-r6vc5nwatLxbTfZRzFdCJDwqCW_mm87FQ8sNc4QjJ1eVOF5Fw9DmJF4UpNuFgW-HHsB6o3-YMuTp-tOZiAn-jTtw40oQhW0L93yis0S8ffIGDZhLt6eEP-1HBxizbeAmMM3nmaKA9Q9UhFKlPniS8DHPVWj7f8pKOA7oUTTwsRR_BhBrxNKDY-tvpx3qLcEeydwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SVtRdl3QjRjoMQruvfNRW5nlOJwN4dzJBKOEDWR20rW67cS4yjJ__B6ih2ztCzT3-fdAmTVg3ly7ouRisV0o7Do1TSn-BV2Zpog5vK_1EpX4BRnb4Cj00b73K99SWnQ-zBeLWdWhCAPW7uuB2EfsBj6rrlqq7DBi9FA3ycYTSgH8aTflAfRLuAI2iAGI2QwPqkUu9HNdtXC2cRaAuigLiSySJteenTsH35-KmjKNCDFsXTxOMQEBTdT_l6UA9YpsHrZomhDh05ADq_ZfGTDBOgmtUeEm4jK0fKV0PTra4ZF0xnKHpuMRVcX70OScJdxi2MElhjPYp4qbJoa1JZK34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SVtRdl3QjRjoMQruvfNRW5nlOJwN4dzJBKOEDWR20rW67cS4yjJ__B6ih2ztCzT3-fdAmTVg3ly7ouRisV0o7Do1TSn-BV2Zpog5vK_1EpX4BRnb4Cj00b73K99SWnQ-zBeLWdWhCAPW7uuB2EfsBj6rrlqq7DBi9FA3ycYTSgH8aTflAfRLuAI2iAGI2QwPqkUu9HNdtXC2cRaAuigLiSySJteenTsH35-KmjKNCDFsXTxOMQEBTdT_l6UA9YpsHrZomhDh05ADq_ZfGTDBOgmtUeEm4jK0fKV0PTra4ZF0xnKHpuMRVcX70OScJdxi2MElhjPYp4qbJoa1JZK34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIndHxGt-NVws7U1ciX2HU7xk1I2hU2LBVxlHOOHJI8O4xFE7jn7_YUsmmuqpK_BszdDtByAv65hciTem4r6mrUwfN1vFwc8-F2mEXQoqzbTdoNRe-cDLCNtUrqY0lmkMr3zFHhKRdC8YlbtIeGVdoL5s-IYcG26gErJV4pedL6b3o5CrJbeWld4IWkmEE4XGvQ_BXzO5icikb64sRlxSUjMi9fvdQ6XsUb3LmRR0cueWCUO9WY38SbTrB6IOzfpoSfqJ_zJP_niEe8cdBj3neyDyxVp2BnbUQgYxAtMwgR-WwVbc9dbYlaU8RtFNUFY-IEsbuHk9nPQSMjXAx3ePg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=CfWnUE7P1I7cQ8nu7hcpECb3eyWML8G5y22umGJ9gZjm78u8893UlEiEZNQc-wWltV_xWD3Jcng2sFGbQ-YufEdjdHQC0yLpdBoxibXfMfhgTUY8GQjIoaKn1NhAqoan6y-0G76JVeLGTQMGxGv0ULETvIEfiAKyQPOfirAqdOK8WDZwaJrUN6aLwhGZSObp-5vjGErIdN3iLyf3LN7SkH9TawBZ1Mqq5QLtZ5dPzOJPhAYKhUeqdQfWFUYusVMeQBCI8Xwzzs7NdGlulGo0ar-pXWC5dp7YOPdRGH-07q0hy3PJmDAHDkmO6cJm4U1dn5f38dlCs4LMj0zrLdeX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=CfWnUE7P1I7cQ8nu7hcpECb3eyWML8G5y22umGJ9gZjm78u8893UlEiEZNQc-wWltV_xWD3Jcng2sFGbQ-YufEdjdHQC0yLpdBoxibXfMfhgTUY8GQjIoaKn1NhAqoan6y-0G76JVeLGTQMGxGv0ULETvIEfiAKyQPOfirAqdOK8WDZwaJrUN6aLwhGZSObp-5vjGErIdN3iLyf3LN7SkH9TawBZ1Mqq5QLtZ5dPzOJPhAYKhUeqdQfWFUYusVMeQBCI8Xwzzs7NdGlulGo0ar-pXWC5dp7YOPdRGH-07q0hy3PJmDAHDkmO6cJm4U1dn5f38dlCs4LMj0zrLdeX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDKEDKkQHl1BMhnYdFkISihpwgkXdOxDAhk8yheqYxjC5Hx00ZXqXz4aTFxuaWUKcWiMc0NwDCioQcLldgI9vQlycXzp1dAPdmKswLRseNB_rnxndBMebsEXCwce12-Wabf0sxNfl5L05s-8uwUpMLtP4EPV3E3P6n8JOnY0oiqe5bG2YyGT841m8jC6bCCr-SMCym9wFroYTXj2LWrx-aD1hP3t6lbYsxSAf3I5xGkL84TQJhff0iHaaeKoL78a1qal1RNGsZfVPGMi9t6jKEAlPckRGeFYmasiesPHctzGXr7bLnogNPnQgFqZcgxnZVk9fAk99WzmuPderzHGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIrPGj7jC2E2uOUKRRdYleYTaAQevX8GKx8PcVBaCPf_rXQbwZuN-oSG-8yww0b_LNbAd9sOjfuHPLfo4YgKzrerC2_MiYmurmk5CAkBrX_gX6aFNN9h__xX7PueHxK4WA3kFN_UJGtfD1P9ajFHGZeLiXwZ5HD5MkER_Q4g8xOsASxV1VT4mgjpOHA4Yj0WWFspal6BMzn3uyIRBL40uEHoZ-KSSHjKYPtKCGmNz2dgSxI-MHwIHWEyj8ux05vYjHQ2-0v-Dg9s3GTjqbWEw0xYXfL9SiIpoqIVdcKYvjt5sldzWrmhzZC2QBsGYby8Yr6hXpEti9dzMl7mhB0Dlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=NQvHqRSrWDTwYDQgHf06iCn20XEO279ftkTXnEZGwC0KbS56dTi6YSrR-FPdCon_CT8AK45vEuhsC1hV-utE1clQZ27bPBuGaZ02E_CSMiUxnZujGsCWwPY91SqGrZ2WgxAjG74908KGCL82mfOtDM3pEU59-2VOb2z6TnrSqzUGbPWB3u_3NouvsdI4_0DDdTqRamchkD1At-EgPyboQTPeKYsUmXyfIexPEYgAz7iXNfTw1eh8a2TXLUBR2_ShSHM9C59Ord2aNTIj4OAXFtFZKQoo2PDgVfySp0c7e9Sgrco8X4l2XlrXdsEHZb2_j-HNS9SHtOgq5HoTMJ6Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=NQvHqRSrWDTwYDQgHf06iCn20XEO279ftkTXnEZGwC0KbS56dTi6YSrR-FPdCon_CT8AK45vEuhsC1hV-utE1clQZ27bPBuGaZ02E_CSMiUxnZujGsCWwPY91SqGrZ2WgxAjG74908KGCL82mfOtDM3pEU59-2VOb2z6TnrSqzUGbPWB3u_3NouvsdI4_0DDdTqRamchkD1At-EgPyboQTPeKYsUmXyfIexPEYgAz7iXNfTw1eh8a2TXLUBR2_ShSHM9C59Ord2aNTIj4OAXFtFZKQoo2PDgVfySp0c7e9Sgrco8X4l2XlrXdsEHZb2_j-HNS9SHtOgq5HoTMJ6Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Z9BYGAqZYkuJsEjtn30jdxbvlrVUIxE0NAyQtaAcmhKd71WsRlSHPvu5oWKIO1aKNNz8Z1P5xnQo5-Bf_glSIN_pSP55VneopbrbXeFzSz_g--hwx9UouHC_OXVkKcuDyWzX4uobYlTn4ZfmWHUjTIzc2uQZ1Vq_UlgmpiPnrfE27kQ2cCgGPcgci6wAuTBhWWm1KVe9vRluCsLBz2H3gAlyk0E2g-me23AOrZjwt9jfs7q3ClE4U18rclxxYA6msaQjRaBpv92_j5P3aDrb_Eo4sk0ZQLsFf5ZSUqvunZlDwdpmGymC8CEqCXJV5XSG7ufZ1RznMsktQCv44YKSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Z9BYGAqZYkuJsEjtn30jdxbvlrVUIxE0NAyQtaAcmhKd71WsRlSHPvu5oWKIO1aKNNz8Z1P5xnQo5-Bf_glSIN_pSP55VneopbrbXeFzSz_g--hwx9UouHC_OXVkKcuDyWzX4uobYlTn4ZfmWHUjTIzc2uQZ1Vq_UlgmpiPnrfE27kQ2cCgGPcgci6wAuTBhWWm1KVe9vRluCsLBz2H3gAlyk0E2g-me23AOrZjwt9jfs7q3ClE4U18rclxxYA6msaQjRaBpv92_j5P3aDrb_Eo4sk0ZQLsFf5ZSUqvunZlDwdpmGymC8CEqCXJV5XSG7ufZ1RznMsktQCv44YKSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=P7olS6czYOo4gnJsL1kkH1smtISYBtnphGkYamcV7HEWtsgMMpmGwoyNUAauIVg3CWnuB6AcvdVoz4LxPP8uHdpx_XGpD8_U0NGLfniDG66zlC5isrTTlcdyNtCsg2s1mm4XHwchFL6bdFEkpK7wayeZ53Rp5i08VlGavdL82-sJTjhWdQexeF_u2kPTWIMQ_2mz9vZQAioy7ZiA210zyuzDRK89PH2azXwt2dtctFAIVes_WUENCF-wEgDFCRYE5I8On4hik-aJ5dIIQc28uWok5XyqIWCHo-Ke-7vdstAGhciBGqPMrle7m0ysrEPvUSRpFAj4WVC1qDKrmcgKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=P7olS6czYOo4gnJsL1kkH1smtISYBtnphGkYamcV7HEWtsgMMpmGwoyNUAauIVg3CWnuB6AcvdVoz4LxPP8uHdpx_XGpD8_U0NGLfniDG66zlC5isrTTlcdyNtCsg2s1mm4XHwchFL6bdFEkpK7wayeZ53Rp5i08VlGavdL82-sJTjhWdQexeF_u2kPTWIMQ_2mz9vZQAioy7ZiA210zyuzDRK89PH2azXwt2dtctFAIVes_WUENCF-wEgDFCRYE5I8On4hik-aJ5dIIQc28uWok5XyqIWCHo-Ke-7vdstAGhciBGqPMrle7m0ysrEPvUSRpFAj4WVC1qDKrmcgKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJyWJdUh9Q7HNKsMCRItKidL_Kpv67j6DOqhDFYKkJs2zgOmuqn1CY_9U6Kwmdx9lUZseA3rQfeYvFdjD6usgvZ9-e8oQNNLdHqOaUmqIM8v1mCtnvEd688TOWWWXymcoLz9ezMprRoUQNvDOf-5ykObkUTZm-iW0TTp310j0le-BlkjKGYh_cUc6WxaCjHPxZ_8nZUlkA-dxWPHRPzpkv40rdK1neV2R6s5oZMa38BPCijDY8_BtFiHdFao9TGMWYazLVnqqNsCCs1HPs95m_PwCcsrkiRp2bLGd12iFJ7ejxCYdYUJQKVtpkVXSZq1rklRj6KCTFWImapVaTGA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=qEogDa_io2tEDfeDofbWjblMqZNLq9kVEUEStxkeQlhEIEyaXqew21V0x4IeLBBXHdo3E4IiCCa-6pTdv391l_F7hAUHAMRWvLP3yPkRbYIJnRUTakF4u29Hk7Pfxp8BCfJFqgJexr2jBHgiF0JSE8JxBu36Z0qFaj3cxi3PHY7zIY79NAR-vQrE9eg98sbqASIE4bCdwHyb2Ri6vBaJAAcF4QO8RDu5OzjhFotHTaUeXXYJKnAL5vPdq7BCkcTiTDjRA31Iwaz86Ep0aAL6DP6fBkBAIoikPYlg5bcsOJAltWuSXpcpOXXF3NStA9BteRmBkkP14frXozGme7pmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=qEogDa_io2tEDfeDofbWjblMqZNLq9kVEUEStxkeQlhEIEyaXqew21V0x4IeLBBXHdo3E4IiCCa-6pTdv391l_F7hAUHAMRWvLP3yPkRbYIJnRUTakF4u29Hk7Pfxp8BCfJFqgJexr2jBHgiF0JSE8JxBu36Z0qFaj3cxi3PHY7zIY79NAR-vQrE9eg98sbqASIE4bCdwHyb2Ri6vBaJAAcF4QO8RDu5OzjhFotHTaUeXXYJKnAL5vPdq7BCkcTiTDjRA31Iwaz86Ep0aAL6DP6fBkBAIoikPYlg5bcsOJAltWuSXpcpOXXF3NStA9BteRmBkkP14frXozGme7pmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nhMhM4ysRlRWjqlLDP2SQSNqPRSkxFNqjaExAn-xfNF38k_fB-ugclyw_S4GvT_L4ynQ1x-2YYHqf3jA-eQkg8aYQ883BTlfYoXSAZvcO_lj9gKWIM8rFSpfY4PnoqwmTsIkqGCamLEOe5VPrCHtMOXapEeieO9WZwueLTc__fPiIcfI0w2SKHcr8iAFtk0RUkWZGbTW2tmA4cd7xclaAF1CISlrkoUGvscwuAPgLuii8388ERSKugSITkG_0bxatt6jvWOD8TLenxkdFV74qgfvYEaGzB0PUJ0lnT9CEQJ_tHHJSG3EzkCjoAZZ7vwe9m51sgHMhaSJ8JzbF9A9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nhMhM4ysRlRWjqlLDP2SQSNqPRSkxFNqjaExAn-xfNF38k_fB-ugclyw_S4GvT_L4ynQ1x-2YYHqf3jA-eQkg8aYQ883BTlfYoXSAZvcO_lj9gKWIM8rFSpfY4PnoqwmTsIkqGCamLEOe5VPrCHtMOXapEeieO9WZwueLTc__fPiIcfI0w2SKHcr8iAFtk0RUkWZGbTW2tmA4cd7xclaAF1CISlrkoUGvscwuAPgLuii8388ERSKugSITkG_0bxatt6jvWOD8TLenxkdFV74qgfvYEaGzB0PUJ0lnT9CEQJ_tHHJSG3EzkCjoAZZ7vwe9m51sgHMhaSJ8JzbF9A9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=A6moQKGmz8-pBqZ1hMvO5gBXXbuuIf1mThGSHrYBRexPKeNeW12DY0rSft7p0oYhsQnaczILnO1ulhhGILpiT1b1towNm6jal0-nhZ4U3L3v8K_QMI13Cwct0CSxoC6ZYYF_u42XXJdlqAOg0y6seLRT62BdR9HUu9NsD_nLK9JwtQy0dqX4Mj4kIxrQyT0cxLrwYEOJwGadSN5rosgDZgZ7rp7t0Ir4eGeIQGs4FFqgjoOCJQSaOJZj7SdF1MZ-0e9AmGfFXFgqO8agjzf1jokQSjtBpSpttCa8uDyGa4PFedRlgl3IbZLg91cKy3EsaIUVxDe0bSN_JN5SFM33Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=A6moQKGmz8-pBqZ1hMvO5gBXXbuuIf1mThGSHrYBRexPKeNeW12DY0rSft7p0oYhsQnaczILnO1ulhhGILpiT1b1towNm6jal0-nhZ4U3L3v8K_QMI13Cwct0CSxoC6ZYYF_u42XXJdlqAOg0y6seLRT62BdR9HUu9NsD_nLK9JwtQy0dqX4Mj4kIxrQyT0cxLrwYEOJwGadSN5rosgDZgZ7rp7t0Ir4eGeIQGs4FFqgjoOCJQSaOJZj7SdF1MZ-0e9AmGfFXFgqO8agjzf1jokQSjtBpSpttCa8uDyGa4PFedRlgl3IbZLg91cKy3EsaIUVxDe0bSN_JN5SFM33Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=REwr_nyXP-PxN5w-mfgiMvMNlwdK5bwKrYGdGOG4OIggejTdWNQQ0A1eJYYT4k1bC9JSigMZQrKKti3aqzHhhehsiVbyTrJo91RvdK-4ji71iWbpHuZ8YYy_IqMszlfNZu0wqs_rLu5Jq6AdTSIbGeoiJA15Mm8Jg29YnRzMgaA5XG310x9oNYcfMXR7NBDT4U5CZMS1pB683sPz4rd8MwbF2zgEeNwFnZRkBtCaveQ-PVO_l_pdzAwy82fOufgH4aTbW_6J-xLB3ZEP9kBZE6b9JQAV3z-nj8fu63UzBOddLTfbfmPmc0DKC8p9qD45gY1dZaH1JD_TN_Y7YWzXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=REwr_nyXP-PxN5w-mfgiMvMNlwdK5bwKrYGdGOG4OIggejTdWNQQ0A1eJYYT4k1bC9JSigMZQrKKti3aqzHhhehsiVbyTrJo91RvdK-4ji71iWbpHuZ8YYy_IqMszlfNZu0wqs_rLu5Jq6AdTSIbGeoiJA15Mm8Jg29YnRzMgaA5XG310x9oNYcfMXR7NBDT4U5CZMS1pB683sPz4rd8MwbF2zgEeNwFnZRkBtCaveQ-PVO_l_pdzAwy82fOufgH4aTbW_6J-xLB3ZEP9kBZE6b9JQAV3z-nj8fu63UzBOddLTfbfmPmc0DKC8p9qD45gY1dZaH1JD_TN_Y7YWzXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caWkP2u9JmlRfPM_JWBsGKcMoO-0yECjFEgtLxKyKy3tdXRMNyA32SLJU3vVIT_KAbleui2WLMQCvKfSxkl2Y-Np6qvx4SyVM5OX0CCaXmEwZPAU4SJtNbg5_2UkI_DybeG4FMQKPAjsEIkwQiPRRc_6d1SFGDStwiwg8LNbbCtLlVuE3yQxCVyPdWDwaP7Ldm43nKEP8L2899nAKqTq_ubXonCq7yBfCrIZU3b10z-4ti2GO5PzkkKsuv0tRd8Cx2W4AUAewi8l33P-LXwpoGoik1dO63InpqTTCbNUvC6o6Uf-oWxfcdWCbeuR8f_jQ6CcSG6UkC28XQPphhPAqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=HQozx99rZNuDSvZVRQxwmI4n9qL4iwwzaHtcpBSeUgvBxhmzfJzy4jQYH523FR9cdQytf1mlE8Q_l1Zrg5JkKQGDKpJbjfMmggsjCeveyWrAk-vA3Erx7xWSbb8TUBcm4ymV1U17cIrl_9Dk06puZGBPZFKZCzX86Ulh-0pgxUOvLwpGV5HPg_JNisCvR3CWpm5M-8kmrzO4VqxxM5jPz5NokoSXTkHHuI-uGCGmCdrS_vWh_x_yUkmRY4z2l5FhJlQ9P2QFto78rjzmeNslvlVwJaBEGIRm69eMdAC6HZ6bfS9uS-rSRmU2LxFTt8C0bgbuTsDcvw_dr1aSX4-Byg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=HQozx99rZNuDSvZVRQxwmI4n9qL4iwwzaHtcpBSeUgvBxhmzfJzy4jQYH523FR9cdQytf1mlE8Q_l1Zrg5JkKQGDKpJbjfMmggsjCeveyWrAk-vA3Erx7xWSbb8TUBcm4ymV1U17cIrl_9Dk06puZGBPZFKZCzX86Ulh-0pgxUOvLwpGV5HPg_JNisCvR3CWpm5M-8kmrzO4VqxxM5jPz5NokoSXTkHHuI-uGCGmCdrS_vWh_x_yUkmRY4z2l5FhJlQ9P2QFto78rjzmeNslvlVwJaBEGIRm69eMdAC6HZ6bfS9uS-rSRmU2LxFTt8C0bgbuTsDcvw_dr1aSX4-Byg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=JpQeWFyLLd89c-RMbDVtBm-S8xa5Q6SO6_yfe-rcGFxIOvFSS-111bxX3JepANYdjnTYhAImvZuCHGeH1vgGq4xJiB1UbJ0XkmzGTUDiWbQK49Fkbl-bK0uJMDiI_V9nHyxdbAQFaS1a12dTZNX0T86AeyZ0DrJzTIqqQ3q35GfX-lWbDf6CIZnTMvW7vKerdXU7asO398YLU8bAXa757QdMTlQ0aMCpMvuCSNsUf54bC_PVupG0klLJEL3GPH0OFiayrzqP58DFzaAEZ_DbaOsv-64j_dHsWqWwD8n6TMkTKPJUCWgvonOxrz8kUM1HC-IOKPwM37YrD2KWsjSRQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=JpQeWFyLLd89c-RMbDVtBm-S8xa5Q6SO6_yfe-rcGFxIOvFSS-111bxX3JepANYdjnTYhAImvZuCHGeH1vgGq4xJiB1UbJ0XkmzGTUDiWbQK49Fkbl-bK0uJMDiI_V9nHyxdbAQFaS1a12dTZNX0T86AeyZ0DrJzTIqqQ3q35GfX-lWbDf6CIZnTMvW7vKerdXU7asO398YLU8bAXa757QdMTlQ0aMCpMvuCSNsUf54bC_PVupG0klLJEL3GPH0OFiayrzqP58DFzaAEZ_DbaOsv-64j_dHsWqWwD8n6TMkTKPJUCWgvonOxrz8kUM1HC-IOKPwM37YrD2KWsjSRQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpcYf-dr8sxZLS2lHX_sq6V6ofoH7rggvnYxI-dD0Im9ei6QOI89C9fZ9hhaT0tJaMQDriLghQrCUpTpDYLuiy_QnFSznBPTCJc7sFo54sa77T1-XsnJPSxm2vfxz9ZDTHYBvPruuxACjDLfwbRrhsaCGTFvxon_bGJNRBy_sAA_jO5qZZms-Wb0Lq6UDg5RG8y5rrWWRdwyffkqGGAcXJdB6H2J7rqIsBFVZsaG1eZ-yAFy_kkEGAzrELEQkj-StDM396v0L7U6TsUwlV2-AGVfds38TO5pXNJ85BaRccCoLEFJXHLaqyrO0dn6XNqdPk_Qs1K82zj9Cje1fHSYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=dC03uK03KjqT1MoGcp0ZKD2yefs3ndHnn0Lqh-G8fkAUahuUhr5v8umfqh-qbzd3XMAQFSGa_H5slV0sVn8f0KAhlGtayx0mRAPYtZefMXQf5oVGnqA6ZbeqPi52E_-HqSslbokhOGDn96qQVfGAU6VwtZ6_Sg_BfkfJi8n0WHW2DzAD4ERNiH5DavCy48Xum7q77wkkUPk5qxRp3j8z_R2Sf26_wOYoFTmOl7jGZFrGsc02NAeFvEMNJCSFRwIZa0M3ICt3fbuWlGu718U-5C1tpIystdsGwuqKWpUH9KntnqaQfUiMX24a4c-14DgvOjChlMylJDNJLMbEsNreWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=dC03uK03KjqT1MoGcp0ZKD2yefs3ndHnn0Lqh-G8fkAUahuUhr5v8umfqh-qbzd3XMAQFSGa_H5slV0sVn8f0KAhlGtayx0mRAPYtZefMXQf5oVGnqA6ZbeqPi52E_-HqSslbokhOGDn96qQVfGAU6VwtZ6_Sg_BfkfJi8n0WHW2DzAD4ERNiH5DavCy48Xum7q77wkkUPk5qxRp3j8z_R2Sf26_wOYoFTmOl7jGZFrGsc02NAeFvEMNJCSFRwIZa0M3ICt3fbuWlGu718U-5C1tpIystdsGwuqKWpUH9KntnqaQfUiMX24a4c-14DgvOjChlMylJDNJLMbEsNreWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Q7f5Jzx0k10Ld6RiEB-_IiLTcP5dX6XNtBMcoHHUV67lVtTMK60UMQvnIrSrl83pLvtebcWsCmxFyr6FySlnYAPYHAjccRwKpADw6GpIciBF7uHHNrvK5YfHz8fJ6I90Yhf8eoGw7SN786GKx8D1eT24ekb9_bHDD6a2qFreeQ__4F_B-g7E3nj3IePJM0Y9ZlGCxWolTl2O3OUe1p1yX0y8jSVCPKIv6my8EbxTcoFwt9bSbuGx2iv0qNghy4H33IzYz-WyxPVrR0JkfRxUH16dACOdasjg1vM3j-1_hrWJoWQPc4TNTVkUHYYuBMwK73tpKCQOfdWcGOWcI2Iiyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Q7f5Jzx0k10Ld6RiEB-_IiLTcP5dX6XNtBMcoHHUV67lVtTMK60UMQvnIrSrl83pLvtebcWsCmxFyr6FySlnYAPYHAjccRwKpADw6GpIciBF7uHHNrvK5YfHz8fJ6I90Yhf8eoGw7SN786GKx8D1eT24ekb9_bHDD6a2qFreeQ__4F_B-g7E3nj3IePJM0Y9ZlGCxWolTl2O3OUe1p1yX0y8jSVCPKIv6my8EbxTcoFwt9bSbuGx2iv0qNghy4H33IzYz-WyxPVrR0JkfRxUH16dACOdasjg1vM3j-1_hrWJoWQPc4TNTVkUHYYuBMwK73tpKCQOfdWcGOWcI2Iiyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nkvgEXuo9RQqaBt1gdYnV5wfrFJHuEVq4dUj3XwQt0-C884O5UZs5-YaszYsH7FiABB8So_dfOsCHkDwZtYF9IsTfVVTg1-OQHJ3o4BjWjZCpPz9x8c103OkXRYsQn6C99iqunT5SnrOZquZ3oi94srxeJBJdSNrJ4NqDYZyPBsX4ah92NSkaZ_bSgjeZjgb8Zx7YK4d0NYB34Q6n-GrAFvHkEQSZnVwGorAjRCerXcBH9JsJG2o4vxaBrIJlKPYm-7jlCZQAly7BpQ8GY7I-4DCt4tI4rOBTwqfomnT1ZdYjvIh2lQbcTzDuRr646tu4P3VE6EdPPyVUqSyVX6264i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nkvgEXuo9RQqaBt1gdYnV5wfrFJHuEVq4dUj3XwQt0-C884O5UZs5-YaszYsH7FiABB8So_dfOsCHkDwZtYF9IsTfVVTg1-OQHJ3o4BjWjZCpPz9x8c103OkXRYsQn6C99iqunT5SnrOZquZ3oi94srxeJBJdSNrJ4NqDYZyPBsX4ah92NSkaZ_bSgjeZjgb8Zx7YK4d0NYB34Q6n-GrAFvHkEQSZnVwGorAjRCerXcBH9JsJG2o4vxaBrIJlKPYm-7jlCZQAly7BpQ8GY7I-4DCt4tI4rOBTwqfomnT1ZdYjvIh2lQbcTzDuRr646tu4P3VE6EdPPyVUqSyVX6264i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJxa7aZuj-KHPIwORV-YKg6gPJsI3qecxl6X8zVv3AsRtYK1-q1TDOZCfla2jY-E7VCUqWReea0NCCJRswT_56mrNFYhsoJ80CrrWlpG0DBOpfBoUPleiGdN5nQ3W_p9rMj4WTfUiQJf233QwtfSn9Wq1rXaDjardN4n7H1VJEgLzufTLiVMCWTihCyBdl_7S9vjiF_YtC13P9JZbugyzx9iOCyv7f7lcEH8xKaK9c_EbOL5UlHOdUmBlvOb3bjQNti9m_8tN3KMtN6_H8Qz4_SDku5RKhAn_tsddtyJmyUyhwg7ZBQzdm3z60vpKXJCTud3nV3NpldqVYPMyH6RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPpbqwf6uzVe_CT-lcmoj07HRwvHlbGc15EIGtfwTygjDzonjQP4MjsFKgBCo_XCG-P40ZQvUz35Xaya6hNTD4D_OkHsz7Y9_oV5k7goQJ_9idolOLVo0w4mw5ueIHQOoGZCtTmCipYZAwoh7rWAKVZRKZmrhDroUXJZ03R3jRLqjSoAw2gMTEKkdY8Z9FooN_2z_LMyKye6Hs810tCNMOfI9r5vh18cFy4wwbF_jvXz2AULj_AMDi3CcbHChj06FbIt3QOMGkCLFNOZAdOPeaktcyb4L3_9F7sPpUFkxW8H7R_RAgFsnJDyDPyIgjwuGO7NCEluoEAP3YNbhNlgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4RzkX4t4uDeAYorsiAsC0NqLskuow827VVnEFli_HsaShIc7ISakYRrBwpk5VnD8tbO-CeHydoCrFMxOCvBUfxdFXg9cJkV5ILglb_fAG0gQkFX2AS3r6lbEvdBjtLEk4BrVu_CSjDuEZFAJ7jbDvmdXkM7ROexUPVu_r58pZYfMwXx7RbbZ2jb1dV1GXdA-w4izd90zd96QrHGej18ElXGoRNdZx3gPDZKwejGbFFF4KvgDWMURhP1ztE99AezAy9Ols9Y5yh_yAzgja7nhRfp1AsFhw27z9xDM_YlCn66-t65OCoexF0_4MlQobl4EY4JGVZlgSPT7kIsxwZqig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=qTst5-JqDrB7ksQkEYfyD3DO7CDLTUE7LTVTJfJ0biLAM-pLXDi9gl-5RcsrfmzHEuVd0rKEJAqpiLCFY6bhp7e8jcO2iISFh7ZLtjDYFd7rjS2lU9v7CQ__fwJv30xnCD5fCbsMT6L9wGc6KcoMJ_Ek0-EMQ8VbxccJMsGOlH9Vgk9ZAiI3kxTWLYbeQafv4c8nqxgi9fUGa93vDMwRwdR49Yomi_KrBPoeAe4HhVTtXzlBJsJkKCecVc7GOcT5l2qFnti0RaOZxb4zcOPzAYRmLjVHjN682QL690gm7P9-aAc3cW5Yt77lhw_IjgFJFMKLFj7447mdQmoA_utzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=qTst5-JqDrB7ksQkEYfyD3DO7CDLTUE7LTVTJfJ0biLAM-pLXDi9gl-5RcsrfmzHEuVd0rKEJAqpiLCFY6bhp7e8jcO2iISFh7ZLtjDYFd7rjS2lU9v7CQ__fwJv30xnCD5fCbsMT6L9wGc6KcoMJ_Ek0-EMQ8VbxccJMsGOlH9Vgk9ZAiI3kxTWLYbeQafv4c8nqxgi9fUGa93vDMwRwdR49Yomi_KrBPoeAe4HhVTtXzlBJsJkKCecVc7GOcT5l2qFnti0RaOZxb4zcOPzAYRmLjVHjN682QL690gm7P9-aAc3cW5Yt77lhw_IjgFJFMKLFj7447mdQmoA_utzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_ydteCe5VPs_JActBUkRJ3h39psEhqbn0iZaEbbhZCjWkNsla4QcTggS6pJgL7uz0HKBA8ryLqteIV1khP6OynmF11CUGxckr6Bf_d5sOJU2Q06A-31HKt8NJk8BZGK716PTHYfa7wUTMDRMZwltlelBaKBgQ3fbgT3mBbXApRTmkOFRPrOp22V2NEvUm5YcwkTNoNS0j9TVgaVlRgIqJ1ph17SYiM2ETDAzeYoqUZbAiyZL7MX9z5XHWADxfmVk1zEEgdgun86xFCobav4ExqdegbXugEPqXGvdMrpZrY1FjGUE5NHtX4oi4l-AoJeRt4bw8srE8l7TqlbrYtubsA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_ydteCe5VPs_JActBUkRJ3h39psEhqbn0iZaEbbhZCjWkNsla4QcTggS6pJgL7uz0HKBA8ryLqteIV1khP6OynmF11CUGxckr6Bf_d5sOJU2Q06A-31HKt8NJk8BZGK716PTHYfa7wUTMDRMZwltlelBaKBgQ3fbgT3mBbXApRTmkOFRPrOp22V2NEvUm5YcwkTNoNS0j9TVgaVlRgIqJ1ph17SYiM2ETDAzeYoqUZbAiyZL7MX9z5XHWADxfmVk1zEEgdgun86xFCobav4ExqdegbXugEPqXGvdMrpZrY1FjGUE5NHtX4oi4l-AoJeRt4bw8srE8l7TqlbrYtubsA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
