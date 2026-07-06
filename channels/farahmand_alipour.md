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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
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
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Tnn0xsgkKjbwfqj34MmkiRDI2vEgeCblEMfjZL3zRKKMTHprPuc4npIKab04bF3g6TIFzQsyPKZyUVM1_g9TgKo_mN34zotqu1DRzLmKkb1ME1J119fGYl4y2-lkyHBSjGCMvXtsjT48H71V_vDQRXwjiIj-qq6D9i0WCo9hpDgQxM5MsEc4RU7Bv4xFxtN8LXIJVC0ZAipHJU2CJwFn5XRXdYiezFg4F-kIQo5lfi9kZ0EMTc4958GUDKjqrCEPCMuGIE146EdXjVly7rBYyPqEFBXoCZOrBBcmMMCFRF9zt0bc0ATDQyn753yWvnbhoWb-yLK_hDzXpwIb2soaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Tnn0xsgkKjbwfqj34MmkiRDI2vEgeCblEMfjZL3zRKKMTHprPuc4npIKab04bF3g6TIFzQsyPKZyUVM1_g9TgKo_mN34zotqu1DRzLmKkb1ME1J119fGYl4y2-lkyHBSjGCMvXtsjT48H71V_vDQRXwjiIj-qq6D9i0WCo9hpDgQxM5MsEc4RU7Bv4xFxtN8LXIJVC0ZAipHJU2CJwFn5XRXdYiezFg4F-kIQo5lfi9kZ0EMTc4958GUDKjqrCEPCMuGIE146EdXjVly7rBYyPqEFBXoCZOrBBcmMMCFRF9zt0bc0ATDQyn753yWvnbhoWb-yLK_hDzXpwIb2soaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLU3ZqkixYOl4MtuZt7Vv-YQ1gq-9xpYT_NXxaYUydy8vMnhrU1gO5XBS8q_skoBscMlT5swg7ci85jwe7mrhlyL_s9vVjDgv2x2XA_u08JwVnO7J34ovqELTTDVECunq4bzOOrK8vheYemFy3j_MlJNnY7OxMmIfWaJyiuLwnSTewvXgjen-BhpwZQ90x73K4yGFiMprkyV41_J7sUIAvkrNk2KFhOczZvn2oKfu5AOIqfDOywqeLYumc43pOkYpaJHhpNZAeU5IL7sH2Vpgz-LZaNqNx2zkTNy26im47AEMIpm4qAULj5Q6gsg7jO010JUZbWrXTX6TZHOry7low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=loGMjPF6Oc_hE3iaYHXvjgF-dn1vuEqoseHlWra_geqt2gnbct8JHqxg1XhlbfESZgCLUkXw20ZbFfICSBA4kuwZSFvmLUCS0QYfaDY3M59yLeiP44KCEC5eihAEiWjspXPfdlECpt39RAO3mOiSkpFsO3SbILzDcErkjHsdi2qZKwAL7J46X78rcn_1aGQQwcSvI_GPfrDYF-1fV9P_WcSNmK7e2HkYxXDj47WtE_m8AHND0ViYWX-7cCzfbYBW6mX-b0HOixowIkx_U-5cZEKq_bVJf-6UX4Ue1FwYgiYQHA9QwAdjASXMIfYbs3mluuigVvj06uBVq2tsB-YKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=loGMjPF6Oc_hE3iaYHXvjgF-dn1vuEqoseHlWra_geqt2gnbct8JHqxg1XhlbfESZgCLUkXw20ZbFfICSBA4kuwZSFvmLUCS0QYfaDY3M59yLeiP44KCEC5eihAEiWjspXPfdlECpt39RAO3mOiSkpFsO3SbILzDcErkjHsdi2qZKwAL7J46X78rcn_1aGQQwcSvI_GPfrDYF-1fV9P_WcSNmK7e2HkYxXDj47WtE_m8AHND0ViYWX-7cCzfbYBW6mX-b0HOixowIkx_U-5cZEKq_bVJf-6UX4Ue1FwYgiYQHA9QwAdjASXMIfYbs3mluuigVvj06uBVq2tsB-YKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=ENDAW9QRlEXND5caYgefZHJBXzhnqadNsc3DzR_vj_8GbamIDbPm23gwDp-y3cHnbPzsV2bD6KSfOOFJKFXmeQdCxIWv88p1mOrSfodSOcX6iBvHANjLUBBYwAt3LYUZvv_sg_52HBgIVWlXqM4f8uv6GyTxNgUcpdHRYMzs-ocoksHCfpD7cS4FfSx73_I96X_slGP8kZp37XvPXaPRT1poJxZGv74WG0mlNgD8w5lhPz-Nc0K-5njOLSUanWy_joVxtpL8REeuFYVRNO0Zvv2MWatjPrsu4vzsfFKRApaVKi6H8Gg4Bynq6Mn8UepSUETc-QRAGSXb35h5O4pq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=ENDAW9QRlEXND5caYgefZHJBXzhnqadNsc3DzR_vj_8GbamIDbPm23gwDp-y3cHnbPzsV2bD6KSfOOFJKFXmeQdCxIWv88p1mOrSfodSOcX6iBvHANjLUBBYwAt3LYUZvv_sg_52HBgIVWlXqM4f8uv6GyTxNgUcpdHRYMzs-ocoksHCfpD7cS4FfSx73_I96X_slGP8kZp37XvPXaPRT1poJxZGv74WG0mlNgD8w5lhPz-Nc0K-5njOLSUanWy_joVxtpL8REeuFYVRNO0Zvv2MWatjPrsu4vzsfFKRApaVKi6H8Gg4Bynq6Mn8UepSUETc-QRAGSXb35h5O4pq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko51Ki_KdYhCB18EjZy7BFD4knVP9VwRCL8PcWYX6IupDtizb1Da9UQE37Zq4EPDsdD1A11ELfAkA_w-3j2-txtIIqZB359f96balsOYrUmOIB51NXkXj7MPm2FLlnrB9zSUrKr_mkuj-PWWtZ711AWd2IkKckAQnyLY6nQU7iViX9acDFVZn4jnjLnwNOXRTkNSkhSu9q3QU67_c1KLNzI3ItzDVe9bRzQqxv0tNfHZsOAtGMdw0g8U78vecPyL8nJpW_X4WzHwiXVQCzp7y7HNmLCpSUejuWwuLt16drso3mjsqLxB4PLA0QSqWAdqprJk8KXUHgiHtF7r5XEijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7nfb2hKHCOFgtAmYqMSrLk1-gylKbHonANiZTb8Hw9gPtx1jsX9q1thv1dzgfJtx7Wuat080B4VdnBY6Mp4xhfk0RHUFGiQS0BzAPwhf_ShjaT5UHua3FbJ7IodlgV36ABUGQ65QHd4u8LG0JPDuK5HWStPz66_j55bJ5Em6RziX3xpsJqyfZpibTcMR-veubrN-GNGXrfXoVRCA7uDQonjtiJi0ghpQDkDyZlAQER-aqpW8OT4ygwpsRadTcXWwzhbY2bRxGhpA2cthZgQ3bICJW2gHnb2hvWR3hSqUbWozHKxunTYPJOWtZBp37XE9vZCiEmRZV7G4EzjtaM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpjmiADBb2tiHH3cKmEP9yCdI3CI8WKdDEC-aWFptqdZajoLajHkc5RrfO4t452Wh4xjB6Xio9CPIdEv72d6bViCJKR9M127wpyUCONrhxgQZU-hcRRLX8NSRhL9iNdh03W3Cwb4Jwj4KRdTBvBYP7Z0CD4KGQRYo7l4EQZpwfx2uudpbpixwupSIAMe8sV9WxV6Ho9Ux0eZRmfjgZUO011xiPXdbgyjiDKL1eqBpkJgbJd2skVVSBvRvNTDk6TnT61mzTJHP0vTpCbqL1BOvQ25I2Sa1d8jXTG5UUfkXLkXQ-_fpfQDz9C0-NUeGEWB7xgnieT3VvHXA9LkmXbhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO4c1hdK_VBqzYXVjF06KroEyGWf8bnT6WPNHzfK7n2rQB-9XWjtrhDJlRkG1vPs9jrDKlWWVlyXar0O7tizMWIEtxr27exYvDLAdx2BbmzRIch-x4uyYCMM1Nq0bimACuJu-M5Co-nqWPvn0fSTzv2yq4AtBl7r33s4tHiJ2gerwga_qlijhor59snyMyw5cYMWTV0TmWofo8_GwKAFgeCR2MtZ2XA0qf-HW3pPZsPEZoEZupqdXrSpG1jWFJKCoUT4xLCjca8bpOAUK3I7Z-FmyB0Wock86dG50t07j_WIzNtcbdVtdytH89eHZ0HdUGgIA_bJNY8QQZ9hEJ3Oqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl7yEz41oqxC5IHooza8Qq5tICDZXCJ0V1JqPhGACVn-pSB11hw7-_VdOE74GMP0NILTB9CrLbVnttMot6ZUXyQNIPrznX5XqBfl9UdIUvnmfqeFmN0c0DJxq-wgV4j5RuZFN_Y2vP4Nn71ZxumYn8yBUt3PRFS_RVjMfZIsTpjfAQARmiyKMCDxcWqAtefpBg5s5HZb1ZeX-Et7JSiVcQyTdtVZcwYlE7PVLYB0JS-H6n8O3gdKDSSreR8Nh7SIWHdAnRwsO8DIH3Woq1sbJIndTGpP3xfWYGKw_8NM8YykSBufNVrvtqrz27OZMx-yXOOsOccWYB9FbIs3emYg3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvbnl8zNF9rhQJWpex-XutN_kAxE93KnezH0HLqpLJHCpP6n05WGVlkpOwwN6v9N6_-eoehWtLtYGWrxHIUT5lYlJ_lBKGT1VWzmKfYxCvvArNemHIZZwJoMW4y-ugohaat5yJwwOTRoHqcM5vC4vKuQpTEwlb95r_QDpTDgp1oa5jkhmfN_sh5JzkT65UAs44detbPiY9L05CaiB9c3XwLvW-mVn5jKWzrX8iO549Y4M5OvX6oaduF7vXV-UAnmUz0Sg9xhgQ3wT0S0nj9yllaJ5WbFzHYARu7CnOwcNILiZLoVGlLJTQQ-wp1Kmk84vSVMFmOTPwLwIT_dJ4hicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ZmuDnbjifW92LftmgQp6aPKN2oARUJ0o5QpVZnzVSX37eUSnhqsmVjkONVnqIw4fUJU9bKVmrO86TWIsn-5oCokJqTU4HOAbkuSCRRYJxgtzu9j4IpEvEguSyp1jV2L7EGP064BR6Oy6cCVmiDnDL8GOP4MlRy604eLCezvh9TR8P92IolbfrB34uuJgO3_xwfGQxhQ2za4qaVLyd3POgJPj2WgdiazZQ2MtzlcVpSEIP1MKDMbGSF_sg0mH_BfjR0uTUemT8iXdDq-Y3cWHEYEVQIGQBqy8wIWOgtWzdHhNBFpAuARlrRTG5srQCbSu38uv5eASox8rpzw3OOCsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ZmuDnbjifW92LftmgQp6aPKN2oARUJ0o5QpVZnzVSX37eUSnhqsmVjkONVnqIw4fUJU9bKVmrO86TWIsn-5oCokJqTU4HOAbkuSCRRYJxgtzu9j4IpEvEguSyp1jV2L7EGP064BR6Oy6cCVmiDnDL8GOP4MlRy604eLCezvh9TR8P92IolbfrB34uuJgO3_xwfGQxhQ2za4qaVLyd3POgJPj2WgdiazZQ2MtzlcVpSEIP1MKDMbGSF_sg0mH_BfjR0uTUemT8iXdDq-Y3cWHEYEVQIGQBqy8wIWOgtWzdHhNBFpAuARlrRTG5srQCbSu38uv5eASox8rpzw3OOCsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=t944KEme3bXMYrnoHlJ5cE1u7XWtKPMJ6r3oCyhCQRb4NWoNxzlrjaXGmU_qtCUTnUS41MedoXsfAjk55-3UcZjYl0ZTamWSH3Bh916rM2AovKUNJMsKjVTnidTERVEM-0354fGVwDXT3zVyfVR2X_ApzF0nOX8q8eJLE1MHU7ndmV1PPHrHawTOihV19MYDnmhmTM73mwEeHZ4YGKyOQq8yQn2d7d0kmWiG8AUirwZhaHEB-P3k-kqhYjACXsBo0Of7iCwQhunxCHljcDCYQBf3XfkjmMCKFiSVpZAMA2NgSNpPu8kAY0jCtP9dWtsj06WOmoUYpCn6NVF_Q2sxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=t944KEme3bXMYrnoHlJ5cE1u7XWtKPMJ6r3oCyhCQRb4NWoNxzlrjaXGmU_qtCUTnUS41MedoXsfAjk55-3UcZjYl0ZTamWSH3Bh916rM2AovKUNJMsKjVTnidTERVEM-0354fGVwDXT3zVyfVR2X_ApzF0nOX8q8eJLE1MHU7ndmV1PPHrHawTOihV19MYDnmhmTM73mwEeHZ4YGKyOQq8yQn2d7d0kmWiG8AUirwZhaHEB-P3k-kqhYjACXsBo0Of7iCwQhunxCHljcDCYQBf3XfkjmMCKFiSVpZAMA2NgSNpPu8kAY0jCtP9dWtsj06WOmoUYpCn6NVF_Q2sxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=eCy4ip7uvkGkNkdn_yn-prAJrtbjjJoFjtgrmol_pSqVhK7Y1cGxchMVUKiHMwQE_2PEL10HmO6aZBkiSzOdZiFh_Th_BYVfheVSZjxfKeE8RUyPqyAjHjKds59JYfsGh7WcWCrOSZRMNzZ8k1KqinrNB0IpyBZrwim-nuVOabimu9txUg5f0ly8w-ojGP6cZUKV4c8L6POoO6bAXusPuPkLbU76elx-nzw2BYLhZduasICgxLHVZUpODeyQX9lTfRlEmo03TTwekRaaDsp65vZ409-EdZJKpE2doTjGUg7qZTBARjBrF6gSfpMSE45oKgeW8j0febYawGAZ9ofmSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=eCy4ip7uvkGkNkdn_yn-prAJrtbjjJoFjtgrmol_pSqVhK7Y1cGxchMVUKiHMwQE_2PEL10HmO6aZBkiSzOdZiFh_Th_BYVfheVSZjxfKeE8RUyPqyAjHjKds59JYfsGh7WcWCrOSZRMNzZ8k1KqinrNB0IpyBZrwim-nuVOabimu9txUg5f0ly8w-ojGP6cZUKV4c8L6POoO6bAXusPuPkLbU76elx-nzw2BYLhZduasICgxLHVZUpODeyQX9lTfRlEmo03TTwekRaaDsp65vZ409-EdZJKpE2doTjGUg7qZTBARjBrF6gSfpMSE45oKgeW8j0febYawGAZ9ofmSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=rgyl5h0c7N5chNuXrR2UxgTwovgDH57SQlfYrAC7rW1a4Eu0t5wHmVoMf15MPG4VlgobQ6kzSfZilpeJZMJMCr7HaTtieAaQ-x6MHezqrJzWM-Bmm1c-jtOKToM2qbKSpe6Q80wMlENMFaNrMOMm93PDtLPJuTPQyzcELBus7blBvASBdQmOTD8BergJiJ7G2DnTgsiw5Hlv3XSk89pZ05-1CYZ_uNNLqmjhkfHS6O9DSivgXuBeXh2HSZZ6GZIbbEHBSGM3tKwsPQeBC75aIatOIQc9l23jtelbcec274sxBXepSoZ7IfKITbb33MYQfnBjGtzwDpuzl973B3iRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=rgyl5h0c7N5chNuXrR2UxgTwovgDH57SQlfYrAC7rW1a4Eu0t5wHmVoMf15MPG4VlgobQ6kzSfZilpeJZMJMCr7HaTtieAaQ-x6MHezqrJzWM-Bmm1c-jtOKToM2qbKSpe6Q80wMlENMFaNrMOMm93PDtLPJuTPQyzcELBus7blBvASBdQmOTD8BergJiJ7G2DnTgsiw5Hlv3XSk89pZ05-1CYZ_uNNLqmjhkfHS6O9DSivgXuBeXh2HSZZ6GZIbbEHBSGM3tKwsPQeBC75aIatOIQc9l23jtelbcec274sxBXepSoZ7IfKITbb33MYQfnBjGtzwDpuzl973B3iRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=dh5IVhTdJwUu5UDMNESJEdEZUj_Tex5ML8W-fPvAAJscdRK-5SW462mmOD7oxZIp4uDp5m7f6PsEoaJ-lnb9hvo18ZdpZKbDOrh1K2d44gRQnv9REcshbQ3NHZVC6E9OwHVjY0SNyiv3m6Fr4ce9gsLdhSjicgt6tozWkq8mLCgymbUTm2YjqpRR0NXNEWZC8WWSKh0Pfw89qhGrFCH94c7cgtJS8VkJR7jz2JAFILkLtDbpjrw4AMMO39gSB6jJU6gm1kbZ862A3ZVVeSHsZbweVgx8PKa1T2cFyLRKAjt3juoRANEnvIiiG9aOY941nmhTJN2JewGPMsExbtGcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=dh5IVhTdJwUu5UDMNESJEdEZUj_Tex5ML8W-fPvAAJscdRK-5SW462mmOD7oxZIp4uDp5m7f6PsEoaJ-lnb9hvo18ZdpZKbDOrh1K2d44gRQnv9REcshbQ3NHZVC6E9OwHVjY0SNyiv3m6Fr4ce9gsLdhSjicgt6tozWkq8mLCgymbUTm2YjqpRR0NXNEWZC8WWSKh0Pfw89qhGrFCH94c7cgtJS8VkJR7jz2JAFILkLtDbpjrw4AMMO39gSB6jJU6gm1kbZ862A3ZVVeSHsZbweVgx8PKa1T2cFyLRKAjt3juoRANEnvIiiG9aOY941nmhTJN2JewGPMsExbtGcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=T31vOB8Q09fhsv_wPXZOP0-dtNlVl2A9WkJVYv4dZ3cq1iDJwpFZ_P4FLYE1cdvZ8ax3HkAfTQGMDEDDASN8ygXjaFV1cuzts47151S-nQisQ0iSsU4YyaN0C5R1YjnnvkEC5EJVVpiB2Fr-heV3uo2NnaALN9gefvP6UGA-gl78wAYHoMBI1GSJRK9ECkYTuIfQWVbEr3VaE2_kodOg-jr904zUxK4-E1yVOTiat72ZQK7PRpUOtE3kfIHTEIQX1n9jMJcqq8-G_WLo6h6EhIrckraZ4QF6CSu1S6BTWjDUpMfw3OjG6k9_JbW10cYCxaQEGYOTtGORoAICtxcJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=T31vOB8Q09fhsv_wPXZOP0-dtNlVl2A9WkJVYv4dZ3cq1iDJwpFZ_P4FLYE1cdvZ8ax3HkAfTQGMDEDDASN8ygXjaFV1cuzts47151S-nQisQ0iSsU4YyaN0C5R1YjnnvkEC5EJVVpiB2Fr-heV3uo2NnaALN9gefvP6UGA-gl78wAYHoMBI1GSJRK9ECkYTuIfQWVbEr3VaE2_kodOg-jr904zUxK4-E1yVOTiat72ZQK7PRpUOtE3kfIHTEIQX1n9jMJcqq8-G_WLo6h6EhIrckraZ4QF6CSu1S6BTWjDUpMfw3OjG6k9_JbW10cYCxaQEGYOTtGORoAICtxcJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFxaLqBueh-tTQGXm0hd9nuVzP7qsrsE7uoTqjRHeqOulo2e3pggy_I30Y-zXUpiwJhZ991AIGIy2yZbzMYxaF9JTnvYPHO7L41i-Eqy3Cp3eCYdRsa8WSVUUURcxNw27lVcPp4zilb2xHFmxssYvvDW3y6hK8VLaktT5Fl1k4H0Sb8ZpRaBtQtEeoaOtaR58qUzXcJtw4SjeMZUljaRBXFJecZYjv3nCaYIU5YetAm10GAnx3KSkuI-ReCdRerAUYb367d0c0a-Az8wMWtLI1fIF4F2Hp378UyPTAJEst1TSWjvUm3mYFJWKrjpNRr88KAYLcwv0P7FYYgLUN71KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=TAu9_RvUGIVjzfnCGaV5wr5st95l2ZCwBumC7bLFfo2am6NNNzwRUb02j7ySGuD6KVZ980E7jXbOIq-0M2YIxj4QyVZ4f9zKFtZNX_kGPXcPjWo2mjlphQcHWaqC4rZzZSk0G09ooKKVKu64OmTaSp2_zbxTxwdzVHZZPYRYk7Uk6-bYEl8Nz-ta8Uts8l9EaHYRfBd2LJQjBp--PSpEkqfvUKqBCeDNhEhfyAzG4yjuy5XIUXM2JcPIAz8dtNDqWzv-EtIvbZZkvzW-udwT0fTERPaG_KDl4CblH2Al9LbdqoOQqps-uVC-7OXHXu7CRvQOFQbnpZFcxF6A3kOiXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=TAu9_RvUGIVjzfnCGaV5wr5st95l2ZCwBumC7bLFfo2am6NNNzwRUb02j7ySGuD6KVZ980E7jXbOIq-0M2YIxj4QyVZ4f9zKFtZNX_kGPXcPjWo2mjlphQcHWaqC4rZzZSk0G09ooKKVKu64OmTaSp2_zbxTxwdzVHZZPYRYk7Uk6-bYEl8Nz-ta8Uts8l9EaHYRfBd2LJQjBp--PSpEkqfvUKqBCeDNhEhfyAzG4yjuy5XIUXM2JcPIAz8dtNDqWzv-EtIvbZZkvzW-udwT0fTERPaG_KDl4CblH2Al9LbdqoOQqps-uVC-7OXHXu7CRvQOFQbnpZFcxF6A3kOiXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Sv4bKvTdG24rfU7WTvDzL9Sa6OCcPmFy1q37bjuTgqFDBrcJ47Pb1CKCJaHVRmGABypMCFOlGPBh4pFH4TXCpsErux4qBT5b3ELDWw-4_uaqEmf9UIFhSmqZsh01fKafLW8zpruGW0LyJJY3oPA7QKslV6U-QlC02xIzyD4A1SnpCeSvqkGGnsOmpB2DNjXLnYg1wCzXSWQauJpOCxAKm5tRJEuD7EuL5qGBR9eqyKggDYe5qfdWGy4GOBLYUievOzNM9z7cBMOeZFzzlYnqmw6xHVq4ANIvmI1Px_QlW53fnvsqpyhtaHI3-esvS-mHw1EBAhhExi1RjOuGjABnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Sv4bKvTdG24rfU7WTvDzL9Sa6OCcPmFy1q37bjuTgqFDBrcJ47Pb1CKCJaHVRmGABypMCFOlGPBh4pFH4TXCpsErux4qBT5b3ELDWw-4_uaqEmf9UIFhSmqZsh01fKafLW8zpruGW0LyJJY3oPA7QKslV6U-QlC02xIzyD4A1SnpCeSvqkGGnsOmpB2DNjXLnYg1wCzXSWQauJpOCxAKm5tRJEuD7EuL5qGBR9eqyKggDYe5qfdWGy4GOBLYUievOzNM9z7cBMOeZFzzlYnqmw6xHVq4ANIvmI1Px_QlW53fnvsqpyhtaHI3-esvS-mHw1EBAhhExi1RjOuGjABnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2lXjhTjzxsK606ao9-qRHHXxQXOLopPhqS_oIxucY2l2KqPFH6klhThDI-_iqh7JHfl5ie4IQXb7hSMA4drsdeGYK2aJw7jq15-hh2KN6H39vU1zyx-T-GMQMck33COf0qi3nf1MDPXuWyr2xcC27DI37VXh88kdYDv6lPsLlhtqKfl4eaQA5hGBXJZxYGn9_tcfnhsAbLcOFUY9EDvU8yCLW_yTcAmuajPD4dv9gCHAZZ02JCw3R64R7R3wXRzwcL4kNSXe76wubLBMqp302rZPsPZ-VbfsrPGIM0i4Bl2JkIpsMDJBXrc8NbaXBb6yMYO4lTpqU7Df9wOcdocLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxBxIC67sCXc0cOa_AmQ-dm1KLhf3SZDOhOFhaqg9o79fHI2OGVTc5ctMO0mKNn16X48G4NuQ6owKlsHguh0niJWrG5reTDcfT-_4ii3ld0CW8uyOY7nGUROsw4X5mJZr9pQQf0DaUla1kmvEa3Gx1N1S1qaq4BUn9yxnnhbth3uDl7nmPc6MHPBoMK-c3svJy3RcD0fCqcbmsyn_ID1btNAc54uKjxX3AdUuQ6CtxfnO74AyF4wxaRc2Q4YNHhnu-slhCDCaor-DtNxWy0PdHpbCagjAibzxVKgNqIiQek2RvuRwJtfb-ZdRZGUa4ZwhVxVq5quEv9Jnl9JhKXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyyXtWM-5mxeAuM8yBSKFrHCe6EISEekAo_M6ScvbaogJqqN1ewsGigiL-m3KbuXnMZNf8fwvtYbyFFtElPE9xThmmbYebKY4hidy5_WvHvjKN5KtnTVI0gCXjcm22kz7Ov1I7BVgtgQh1XRzKNHDOY7wiMvNdXBvhLePDMJUk4UtT90UNIaU7w-7jrD1zuD-cSHRGHhyzXNzQtQGuU9JQ2vNaqilLYJqK2NAqZJq94vzmCeu7XjF_Ftu7ZjRITi2hpgGd3y_R6WKPFbohA54mQmcgl0rZDcBXnr3Xxd4-HRlluKv0SysVxOBJI5VkBZlHnUZCfRkndCgEWbj_JraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLgPRrs-tX8BtaqQoLeYJJcmASlNCJBh-hJVNKbIyntpAzaoZPCz2-K_8wnOwfFejLh9rL5uC2XcYXcHLnMUIVqvN_ij6u9aXQtB8nRLfnLODUW6kbSPljssBZ3RQPRYsZSkqnm2z_Wa-IpBTNBcEr2dgHYij1NyMZAHVqpXahRdEzaX0uQIbLqzPaWqH9kjgnPfdOmXdCcg_caPvLvxROJO4nGNCIYeY_iePKLk4z8Sn_TplDcbcuw-LlVrRWcoRgChxFhKfOGeVRM0bn6ENyBbBZcnr0mDYHPxqD1JNOx-RUrSLAgrNPIdMIDSjS8NlL6lKVH22b4TBnKgMFi8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9p4Xx-LexdXMxIJmKFbRk8eJSQWk0XaUP7xF8ijeLSt5j8g8acCeBb0zSqxv4IEtStgiMIU_WcMPzuuJAfjbq0EUfepux8snKff4TFmid-dHhYO_NaFzZa5qmppaSXCKCwUcfDdL42p79ltQepj4YVOJHvG1J-R2ydvTr1Mh8OZiBxrDTcxP97KmixyNkz5jM19LGWMnJZFjzU8OOAupDkAF3K6PEB2Cgj7ZWGrtehlQqi3OG6-qbhKNBjXigwE8j_97OR7VOeNpkBxgeP4HXd5AkXV1orOzCFyX9206CsZk3ora-NtSFASPdpkhZZC7pNLbUPKeuZNnNrjb8hwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2wh4gTOCdOCoaqFPNMnwf3zun-exCxyPlOddG-ZrKg9FsP1BQq7FcyxcXt9B4VSRQ93Eu8E6eYPxq5ElZ5gtfLSu4TR_SmCXJH0M3VqMyj4mlkGEcZtEJpiIdLOWaqUzlXeHTZ0qf_WjwfKpKuNG5LMnzVz14kw5cMfgAGPZ4eSDNFlgsuu0FgLp0pqmbvbdZBcOqXcXXOVBLiCAX-X2QPVoYhtbU7pLoub_tsOA8CsJehJUrBUF0GfsPl4CkAdMAS9iGqdigUp5274nHFCgJq72aToHstur-4UB6gm5K2bDLYpC58HenwyLKJGit_dqtogFsv4JzC469D_3B_qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdZu7nclEkBcbO7x7r-41yLd7JKYTz3UQ9cfgiXXfm-4b5MU9GEiEDZeHPJTpxaKfrX-08nMzlwN_TycbtNc61Yqs1O1LYvFWbW0DRoNbaI3fNK_qD-uYn0VZoHwpgG1rl8ITl8rN3fDih1BkuwINUCwzS9Fp2xOVMF9lq0e_eEsl_RAtvb2HEL7I-jns9x6esoYmL1euQwsn9wtHAnwsmsRI-EqMO8TFPTP_Um3qW04RoJPw4nUNe-LZ7XD1SKJrM4CmRSGpCU8E2M5b9HphUVwoHv4L-daXFwQvUU6WJaxFtILNkb0cUbd0iSDpxE_6PRuF0BhPLvr2zOG6pB3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcYCjkBJ7sihIHPws_3I9nIPJCx2x5qIvbRUtieqJ8n4IOe03rr3WhVK2tr0XtefhOo7heOOO8G4eM8_pW_Gwdp9vPevxd25dzgBHtMGPwayri9XTt89sobm_WYtvwmvnwxCvFTcPQeAWtTn-Ps_KLveo9DHS0H63BwwQItBFfzVe4Pkcs1848VXqjIXDfWBj71v-isBJMtTNKN3ukVhFSF2YPqa0_cIXBooHK186POws55pjUy_EwfoLZhp2Sko6WxAcSU0OocmZwV7feo_Dz_nZDYx77tl_HvIA8o43nW-XUmX71MAvkry395ldP9oyYVreE9mqXRYA0FKgRDoeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nB6SNDsOWWjzwLNxXFjLsoBueyW3QLUg9RxZQjE--JWttwhgnDVBJeshscO8PO0WOWsx3GYlFAGGjdGImXe06UdITlOUwOdJtt5jNppA-gbfDgqpv5Qy9H6Jd-yKBC6VTnCTKqCSnENfZaYNZ2tq79sNn852O6rlQ09-TGQz3yhUElJk_L4cAmCWGGQD0t_IFO2yVjOlo6V2b-hSz9z-9Q4viSIEQfrw66khJRH_73oNZekkxAsveIWed8dg0DE6-o3S2PRpc90rhqv5YB39GvynEBSbt6pZ642JA2pWw7QKm4veGGKfyhJ9Na_iEpG3Tey2d-1xPUi0qFvDnMcsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7dCfaIK6uXrqxivRpoh2zGng9GizSvUYw2lvMtwNOHj7jMr7gcrSzU3mGr7zXPUw49xOdpzEp8_1NwYRGzCbmUKhMkiSrW9mDFQxTcVYWYKrWvUQPhBkGQ85ws0l2V6vW_93Iz5ySnAhNrODOCYhFFTyLs85M3FlxAOcdttvYm-kMFQL3YxqXuKoa4mRNOAmH2HaUMFiCAnKQazbWcENdQDAFeeTRarPFOAZdXPzfiQ2xLLlegKyFAIdqJnVwDk9tPMpLq5pWi4DboPABeVkTHikHpGd0M2HzwFIeuSASvKzn-4SMmCSiT-JFVVyUvbnL7jQi4VK9Ivxh5LI18RKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cemZde9SZ4Mh7TITyZL3iqYN_0I-6m2fJq7Ds8cajwlKpuY0wnK1Y2Y6mmYsx4w8TGROqfTFZrDE4Id1pgGQV1i2Abwa3OLDweTobikbQTIzb49WPMA-2-fn9xXrvL6qRmXDKApNUERNHfqd-sQ6znPkyZRCrt1Mzrvttl83nGYE3UTZCquJH0II983uXSDCIGJooL8RIJ0xYamEuqlx4oyAECQbDvM5DMZUrCiGxnYdS8hJodpLOSASUOyK8htbaKEAPTeu_Fv-EvnEjTOpdzFyfO9DNbpp68X9D-IkAU_-HX-K3qzK2pKZr1ITStQV9kRT0tage4dmYGQwBwma8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwVAP7dnQqNi8w1Aqd3qzgWnIx4xYD86iu-hlTdDrZHNHE4VX9gZ-9sqC-56Un7OQKkg3-txJQ3W9GLrna3nAelYia0aSMs4Uf6YEpF3B35pMktbPGco01iLen5w9Inw9qWbVUUxlnONCfb2_wu0-M3skqYge2nNBnQ3l6m0C1--imBLFSkQLxqOSFsS1tRDwdTNTgZnrvtuluM7Y2gCndRXYjpmxtYmqDw3RWt-x-OJoKpQ4a76czqWK-I4DlIDgsFCNXI-TCTlx5yYgVLT9uz6BkI1_c4sRsxwY3Pt7rDPEVgE2L_mcpbTgJoToJT3RcRPvLDbhUntbBTyoSP9tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=N7wkKqY80kOURY9ZvjsJ5cZFmpz2wpycmdycxnfj3LheNrIbSeQJZlyDQddE2iEnTBQwTWjlVwmSfstIXZJqVkve-QoKpN48wcjTiXExV3SIhzXXSxKjAcul_WE2pW53TWJgBJYXqU9bN1HaCchFJ69P16Xe8-JmCDbWbiPP0HFOCO-bRWqV8xs4nUnCBB4cOeCft95feROaloxV72nzMttHZf2kMMsL1jh_MzZKfi-ZnPZcSOAOQJND3Djg_-xjuIxT9UVvSHENjW8ws6gvKiiCndkanR5JMNgFksmSP1dfudyhX2zdJqx8GZBxeaSzCHpbOYHhFwDAuCHaurbheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=N7wkKqY80kOURY9ZvjsJ5cZFmpz2wpycmdycxnfj3LheNrIbSeQJZlyDQddE2iEnTBQwTWjlVwmSfstIXZJqVkve-QoKpN48wcjTiXExV3SIhzXXSxKjAcul_WE2pW53TWJgBJYXqU9bN1HaCchFJ69P16Xe8-JmCDbWbiPP0HFOCO-bRWqV8xs4nUnCBB4cOeCft95feROaloxV72nzMttHZf2kMMsL1jh_MzZKfi-ZnPZcSOAOQJND3Djg_-xjuIxT9UVvSHENjW8ws6gvKiiCndkanR5JMNgFksmSP1dfudyhX2zdJqx8GZBxeaSzCHpbOYHhFwDAuCHaurbheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=dkE_Q8Ex7TY7MRgTyoYusmG970qkjaep2ydsZsNsZYl7r_3LIF6QES7TnkqQbTsHQ5pMELycugv-R1G_euAp8toONT3mePxIvuuNWb0pibCshAyCh2wk7x3gxVSxezaXHQw2k1s-x1iLPboAoKmy1EHU7DJIE4SsSmoIuf89YiYtVTlhMwAYLh4yxEi-kaHNJ0wwUsGryvNY5emSbED7wwKTuoEyzD_YvHOHBdl21JNzhGtJCg5XODT58RT9pc21I15LWBmKs43I99YbFIEv5KKB44A-H_Awlb2Z-S5ansQcMrwi0w6-rj1RCxV8xiGS_Ytrmp_LgIxaiXlcz1m_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=dkE_Q8Ex7TY7MRgTyoYusmG970qkjaep2ydsZsNsZYl7r_3LIF6QES7TnkqQbTsHQ5pMELycugv-R1G_euAp8toONT3mePxIvuuNWb0pibCshAyCh2wk7x3gxVSxezaXHQw2k1s-x1iLPboAoKmy1EHU7DJIE4SsSmoIuf89YiYtVTlhMwAYLh4yxEi-kaHNJ0wwUsGryvNY5emSbED7wwKTuoEyzD_YvHOHBdl21JNzhGtJCg5XODT58RT9pc21I15LWBmKs43I99YbFIEv5KKB44A-H_Awlb2Z-S5ansQcMrwi0w6-rj1RCxV8xiGS_Ytrmp_LgIxaiXlcz1m_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=vpCGOQJaA9nTY6_i1aDflZTwX9vMoI2MECDYtW0By-YxY46yMjr40fkvYh3tHAaR1OfCjG3t2TwXZvx3hYEj4kAiHmi2jY18g-b-7deDREc8ShnCgWgIzxbVUHeI_Htkv8HkBB4euVXbYkUM5NEKmp-RyEhINE2smoWeYfwSIoyDEJIcQJFGDG2aMD3vlwa_KdTd-Mg5V2Tmy_qACTGyl8BLPkibKt3gRFJa_UwEyK5sHz6xohRc9PbDViWPFHIxnQi8QmOUZh5FwdpbC7BVNyrlOYMieBrQW8e6f5oCusk0SOELNMFSWSy4VQHGMLpZJJoJq8ArGnKV6K_zdl8ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=vpCGOQJaA9nTY6_i1aDflZTwX9vMoI2MECDYtW0By-YxY46yMjr40fkvYh3tHAaR1OfCjG3t2TwXZvx3hYEj4kAiHmi2jY18g-b-7deDREc8ShnCgWgIzxbVUHeI_Htkv8HkBB4euVXbYkUM5NEKmp-RyEhINE2smoWeYfwSIoyDEJIcQJFGDG2aMD3vlwa_KdTd-Mg5V2Tmy_qACTGyl8BLPkibKt3gRFJa_UwEyK5sHz6xohRc9PbDViWPFHIxnQi8QmOUZh5FwdpbC7BVNyrlOYMieBrQW8e6f5oCusk0SOELNMFSWSy4VQHGMLpZJJoJq8ArGnKV6K_zdl8ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=t3dSh7jWRitGv_PuPuUrsiPU13-0tgr7GiGZUD5PSSNBCb5Oqn71VwJ5jFDs7RjnT9HguAPHWmMvC4UHO5hnjYODVNp2Jwjq7C25TAetSEPm2snCY-gqSJXBmz_5zpfhoEqOUK88Q9FWqwiPBB4x6tkU8E9W6D90P1_NlyDMp4Get9_SaN9vbh0Z4elY2djF_6dTf7uPFBmmlw2pYKVel5_7gw-YOy4_8aaed0pSCimAeuFKC_mV1_whqF1uz5BjnyqfGuYE8knv1dWnuwlSmLTUBhlqRLzwHWafFI0eJF4RZUhZLWcIVaXGRJQB1k8jbVTSayfh8MVSyVLxK9dM0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=t3dSh7jWRitGv_PuPuUrsiPU13-0tgr7GiGZUD5PSSNBCb5Oqn71VwJ5jFDs7RjnT9HguAPHWmMvC4UHO5hnjYODVNp2Jwjq7C25TAetSEPm2snCY-gqSJXBmz_5zpfhoEqOUK88Q9FWqwiPBB4x6tkU8E9W6D90P1_NlyDMp4Get9_SaN9vbh0Z4elY2djF_6dTf7uPFBmmlw2pYKVel5_7gw-YOy4_8aaed0pSCimAeuFKC_mV1_whqF1uz5BjnyqfGuYE8knv1dWnuwlSmLTUBhlqRLzwHWafFI0eJF4RZUhZLWcIVaXGRJQB1k8jbVTSayfh8MVSyVLxK9dM0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=dVMkBcDHdGiRPwv0xf_8iBId_FCUdMIk-A0F318InPAguaGMFdNCfhJUDyXpC19uheR3l4gXwfonpgs6KwyMUxfs10JHcq0fEauQmbb1d4MHmTBDwNThD5ARr8JdOzGBaOVVadNUxF-J6YfHd7LMPUc8GqZyDSOmb-OkZm9RARF0_GDiWDMnqKXViAt_6opgBXp1jdKhFxPNWHH25qUJngZAVmUnJ1wFPS9UZb_BzDP__l5ltZmq6uw7_xayMhqSev9iyoOD3t2D7ZfboKREQvRWDFHZpX8B3nTME_JpwCmvD87XoAg7A5KSueIV4MgiZbRR6KSpwlWoxKsfyGJdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=dVMkBcDHdGiRPwv0xf_8iBId_FCUdMIk-A0F318InPAguaGMFdNCfhJUDyXpC19uheR3l4gXwfonpgs6KwyMUxfs10JHcq0fEauQmbb1d4MHmTBDwNThD5ARr8JdOzGBaOVVadNUxF-J6YfHd7LMPUc8GqZyDSOmb-OkZm9RARF0_GDiWDMnqKXViAt_6opgBXp1jdKhFxPNWHH25qUJngZAVmUnJ1wFPS9UZb_BzDP__l5ltZmq6uw7_xayMhqSev9iyoOD3t2D7ZfboKREQvRWDFHZpX8B3nTME_JpwCmvD87XoAg7A5KSueIV4MgiZbRR6KSpwlWoxKsfyGJdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=SZLOXq0_BkLdqGhCTi1H6y77JXXJgOK89Uf4t-lEqM3QPn9UoQTkK1aQ4Bd4w1sdT2XjhwcmbjRUHUxA-pwWJvpgYGomhFCWCdNfGX1klca_XNzuxGjUXMKl60kIv9o7sZ7hGSFq9JouprQ-4wZ0ooqF98e9pKxAfMEH547-zpma3IQcyb3N6g3lHy1RbDGkAZhj6joMfOs4rzxcSjiJSZvuY2H7sYyMtQ4X1snELoCnwJkE-BwltEQQm3_71JWH72WiLWGnPXR2I5xoel9vTG0qX7kggsaJSyf8MPt8dHCzmWXtEYGtEwLyZATpjvn5Waj8MsVYDPCic3Y2TK7uqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=SZLOXq0_BkLdqGhCTi1H6y77JXXJgOK89Uf4t-lEqM3QPn9UoQTkK1aQ4Bd4w1sdT2XjhwcmbjRUHUxA-pwWJvpgYGomhFCWCdNfGX1klca_XNzuxGjUXMKl60kIv9o7sZ7hGSFq9JouprQ-4wZ0ooqF98e9pKxAfMEH547-zpma3IQcyb3N6g3lHy1RbDGkAZhj6joMfOs4rzxcSjiJSZvuY2H7sYyMtQ4X1snELoCnwJkE-BwltEQQm3_71JWH72WiLWGnPXR2I5xoel9vTG0qX7kggsaJSyf8MPt8dHCzmWXtEYGtEwLyZATpjvn5Waj8MsVYDPCic3Y2TK7uqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Y1i_nNL3nWtlLsiBrtHWcUnRri2ZdGbvqx_vimh_gmUbj048B3C2AEu5dr2ThKT_ynPGdETYohqxZRFTiK1LmW8f8tdl9E_e8QW0vPFuT2pbZXyAIWKtq_puvcsp09BjLmwRuSvxmKYO6p3ZChXEOtn1yrMCqWlebD8CaL_3MnaN_w_lsGkh-rwKnI0Z4YKH5OX5B1DssGKFw7VO8PU6IftDkBMER_8kQ-OcEBNuEXqz33aHPIV5Rn0aEevtpRvrPGkKsZITIvdhALe4hD7msMSzTwa6AxNte-ZEnJH4GxuMmWq_jc2en0ulS2o3x991FFnLvBtWbSml5VJUWH42zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Y1i_nNL3nWtlLsiBrtHWcUnRri2ZdGbvqx_vimh_gmUbj048B3C2AEu5dr2ThKT_ynPGdETYohqxZRFTiK1LmW8f8tdl9E_e8QW0vPFuT2pbZXyAIWKtq_puvcsp09BjLmwRuSvxmKYO6p3ZChXEOtn1yrMCqWlebD8CaL_3MnaN_w_lsGkh-rwKnI0Z4YKH5OX5B1DssGKFw7VO8PU6IftDkBMER_8kQ-OcEBNuEXqz33aHPIV5Rn0aEevtpRvrPGkKsZITIvdhALe4hD7msMSzTwa6AxNte-ZEnJH4GxuMmWq_jc2en0ulS2o3x991FFnLvBtWbSml5VJUWH42zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYl-oCeQafDDHZ4syYfiD_rkKG_5kylYORM3ybg79FXV3Z0QxkQdHBU2A2njMa1tqp6fRz_2Gskr_tMi3Y75aRBs6jLXAa3_PtlQ4UNMTsN0UVXlnsl0Bt6mN3CICX4dmDp-jQL1DX8DXBiDhqPNzeD3T3AHlbRQacFctjED8EUYoT022LG5cTY_a6tJxeqDWWsHSHByIVkVRaznGT3NbsC8FkAy1vx1Kbv1JjyK1platg-UhE-anMzp78_1NMRunIbmBSFMgnK76-eTtm4G34lItDBTrKSjbIBuGm2ZQXSLzj1Trzcw1JUHpuVFRDgrUNZaTln4Q4x--U7P9JHRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=jTMTGkTq4-wGsA75OXJKQPDfda2NX6KAbHJBSVOIU2yvf_WYDKYIvax3OoRZ7iBQKje-3z9WU6rwYh7BgaMg3P7Ea-v8WcA4a2QckbrboitE2gjsu6G6VImn-rQNcGhkgAlxW3hXgX3RndzwlJh411n1gVX1TbslH0CCRDeLyu86_EAsl7dOFqYrUNjXoin5RZKMoQMt6gMbtSy3IYfEsg1LgdD_4RpXWVRLTR9I_WExVXEiS9Keldjz9MmXNrPE81DtvtTNFD-_5gh14Cob64PLc6N92j9uW6UzBo2MwQuIjsWVHMHua6IJI2xvGv23ghKp_1yWxcc1-N-xED5sVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=jTMTGkTq4-wGsA75OXJKQPDfda2NX6KAbHJBSVOIU2yvf_WYDKYIvax3OoRZ7iBQKje-3z9WU6rwYh7BgaMg3P7Ea-v8WcA4a2QckbrboitE2gjsu6G6VImn-rQNcGhkgAlxW3hXgX3RndzwlJh411n1gVX1TbslH0CCRDeLyu86_EAsl7dOFqYrUNjXoin5RZKMoQMt6gMbtSy3IYfEsg1LgdD_4RpXWVRLTR9I_WExVXEiS9Keldjz9MmXNrPE81DtvtTNFD-_5gh14Cob64PLc6N92j9uW6UzBo2MwQuIjsWVHMHua6IJI2xvGv23ghKp_1yWxcc1-N-xED5sVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=Nh9NPsuYAWaHdgfBLUcneP2ocnhPrG_lZhUV89BlmLeigvk1VFCrVcnVryPaoGkSyTQsq53WaFvgw2OLCvKsm5d_DyOga7rNY7RoakJLmVDs6kbCh_6A6zbcaj-aVfo_-fMmzKJdQQW_0YXkerFJ0YFVwyIGaAXI-nZosaNBQPSk6tNtXfr87vxiiirJJ2p-YSznp3BNYKe-ixU78lDlmpl2O-2w9gKNu8cr57Es5fur5nz2xNITzq54pWWXbAj8VB-lwOnDNVdUYLG9mXlKiq3TeNlqcNmm0QeQxAqXbK40d1CoqCgVUSwOjCsqxKKXYBcQQnpnMLikx0u6RUQbPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=Nh9NPsuYAWaHdgfBLUcneP2ocnhPrG_lZhUV89BlmLeigvk1VFCrVcnVryPaoGkSyTQsq53WaFvgw2OLCvKsm5d_DyOga7rNY7RoakJLmVDs6kbCh_6A6zbcaj-aVfo_-fMmzKJdQQW_0YXkerFJ0YFVwyIGaAXI-nZosaNBQPSk6tNtXfr87vxiiirJJ2p-YSznp3BNYKe-ixU78lDlmpl2O-2w9gKNu8cr57Es5fur5nz2xNITzq54pWWXbAj8VB-lwOnDNVdUYLG9mXlKiq3TeNlqcNmm0QeQxAqXbK40d1CoqCgVUSwOjCsqxKKXYBcQQnpnMLikx0u6RUQbPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=EH1c-LpCr-5C3KXrZXq7M4Y2uJEGXUv0KEA_1xilj4fPrWhNYeh7a0tvLXp5QC5PqknZ-LOjcngaFx3LxX2N8PCnxo1cRTTsrt4sq_v0tdTVqzsrvM0PEphCuPkqKlLI3-TYHP5KVabYd6pgqEpxVb5DYyuiadBYTfbfrRt4nil7wdvoTd-sqikD42pE5sZbNfOuJvW5wu4vRnOoUUIS7WoZbQlMod-5-9gK4vTaIibNSY4mH-IH_SmAQZp-jhp9z-iVkJwLrr8ZMMWGHqShh2vMN-UjmN1nX7Nz-vecisR8Ez-T-ND_1NtmfABFycDS1vGKT3vodA2wjQTytAx0kKysSAV4VnEkIKv2tqjOGfQBdRs9BSxIYBV1gU6_WGf-tMd6h5jnzo704mgK0wnJmXq8h6cTPgSeSpSNztTATKr22ZOnSNBN9Qb5vYNjN_71E03vVfmmuFXXtkWhp5fPROQj-SVLLvGMxqYFYOlsUyATiLuGIfyMBEVpCflld09GSl7op8NC40BhiFHClkEkOELHfMpkiiM-TZ5RXlDf68POeRCmuvryBsIUAgI2m07zJ8IwfVboO1yywIfhNfo3pCiY44v5V6xdcILm_uXclM8wqHQFuUrHRxIjQL9ECfQ0vaZbgIeczDSQt0UEqsb-gX-QNoEFwiQayMAKBSzQWl8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=EH1c-LpCr-5C3KXrZXq7M4Y2uJEGXUv0KEA_1xilj4fPrWhNYeh7a0tvLXp5QC5PqknZ-LOjcngaFx3LxX2N8PCnxo1cRTTsrt4sq_v0tdTVqzsrvM0PEphCuPkqKlLI3-TYHP5KVabYd6pgqEpxVb5DYyuiadBYTfbfrRt4nil7wdvoTd-sqikD42pE5sZbNfOuJvW5wu4vRnOoUUIS7WoZbQlMod-5-9gK4vTaIibNSY4mH-IH_SmAQZp-jhp9z-iVkJwLrr8ZMMWGHqShh2vMN-UjmN1nX7Nz-vecisR8Ez-T-ND_1NtmfABFycDS1vGKT3vodA2wjQTytAx0kKysSAV4VnEkIKv2tqjOGfQBdRs9BSxIYBV1gU6_WGf-tMd6h5jnzo704mgK0wnJmXq8h6cTPgSeSpSNztTATKr22ZOnSNBN9Qb5vYNjN_71E03vVfmmuFXXtkWhp5fPROQj-SVLLvGMxqYFYOlsUyATiLuGIfyMBEVpCflld09GSl7op8NC40BhiFHClkEkOELHfMpkiiM-TZ5RXlDf68POeRCmuvryBsIUAgI2m07zJ8IwfVboO1yywIfhNfo3pCiY44v5V6xdcILm_uXclM8wqHQFuUrHRxIjQL9ECfQ0vaZbgIeczDSQt0UEqsb-gX-QNoEFwiQayMAKBSzQWl8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=EuE866Y_UhgeEyUapR8FfVykMJJQWeVu2x0kk9abkZ1jLO5weFVaH8V-4AYYxg_1pR-sA1_zG0o0U7qOux9JiyxOP-rlw3g6GmMqmvGXfA740rTBV2dUWgRm3t9BOvkI2ZVL6OZwtMS6b4vFJR_x5qYb4w0ZDAOfRhEaUPnrv9ndcX-boeCfW2MQGhxoKI9ObcwX3p6nxaH3T79h5kYRECwxHN1AprLcyno3pX2uw6ztyqvzYTfEOKyTRjRaSQp8HHXnlurje0RTyJHK827wMIVNPz0WSN0Kd1iQ7lDGB2nqz1mKXPTBqS4Da9pzStb9X23lJb6fr6tb1RMvbn_vjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=EuE866Y_UhgeEyUapR8FfVykMJJQWeVu2x0kk9abkZ1jLO5weFVaH8V-4AYYxg_1pR-sA1_zG0o0U7qOux9JiyxOP-rlw3g6GmMqmvGXfA740rTBV2dUWgRm3t9BOvkI2ZVL6OZwtMS6b4vFJR_x5qYb4w0ZDAOfRhEaUPnrv9ndcX-boeCfW2MQGhxoKI9ObcwX3p6nxaH3T79h5kYRECwxHN1AprLcyno3pX2uw6ztyqvzYTfEOKyTRjRaSQp8HHXnlurje0RTyJHK827wMIVNPz0WSN0Kd1iQ7lDGB2nqz1mKXPTBqS4Da9pzStb9X23lJb6fr6tb1RMvbn_vjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=UDEqlSjz39Ix-4GEkFGLOBbowxzPL_xMkxVpGONOkLyJiwqIJhU3YyNMsfsderPDu0pcUjQmqKT0tpn5R1v9V8J951NEBlpR6eZFHKQp4X-9a0qZ85OnOZxIRMQzDaDIAVO1GnDg0cCvHybUwlEZQwymUBcVA6ANr8odHNWyw2f4P4mz-bzHo1hRBZm_xD63hhoOzoSj0AARCVLr5hZ_ACLU_AUHsCAq28bEztkH_nudbuLM8fw6vR7XKVDGr9XE24k-LJewh5ZUBGF3jijiCMzlmMJE3a_I5v87IGw6YFIWVnR_7F1W2bS-wFqye43iIhWA5GpNV-Z1cHzKCiTDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=UDEqlSjz39Ix-4GEkFGLOBbowxzPL_xMkxVpGONOkLyJiwqIJhU3YyNMsfsderPDu0pcUjQmqKT0tpn5R1v9V8J951NEBlpR6eZFHKQp4X-9a0qZ85OnOZxIRMQzDaDIAVO1GnDg0cCvHybUwlEZQwymUBcVA6ANr8odHNWyw2f4P4mz-bzHo1hRBZm_xD63hhoOzoSj0AARCVLr5hZ_ACLU_AUHsCAq28bEztkH_nudbuLM8fw6vR7XKVDGr9XE24k-LJewh5ZUBGF3jijiCMzlmMJE3a_I5v87IGw6YFIWVnR_7F1W2bS-wFqye43iIhWA5GpNV-Z1cHzKCiTDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX6ncos1Y4uyF_sdBgiRRZ38SGYu5n6YtrSdEcYQi1bnfpjDXe6ODEFWThDJvSAPLNo5Hupe11-t75NWI7wySwbuJ0XD_XjT0ZiWnZupE8U4s6lC3uc3hfs_iXVftQJBi9A78vATVAlDPgKGUUMU6cT5_9vdbeHxW5Hst-JXrktQRhSw2eQoPEHMcXI3lIPrg5jLmIRgZzqoOM6_Z1jMFLPpXcPXibXenGe-DaerTHkAQCe0c-tmQPLos0HpBs4mZBLH2i2Xq-JK1llRSEIL-AxZQVf7WHtIvADNDB_M6rcRidmGAJiznCYcZaKL_O09QalN8D2il3y-ktLchY41ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVo7siEL3pXyOPYM4dl8qnfUdP6WkgYmf3DDgHPa_7u0AyERgTV1wq56yMTrm8-cQ5XXXMWF9br6eIBOiFCKURu3C_YCHOx8dTRRceXdf5jg-UzYxVpUrND43hWQinKXtkrHVLY1RN11uIjx1mO-R4YnBV3x1Heh0fBB_0eEQ4rbUNxmGCazMGMyOXxjm5EkYDjxws_DVLnivCRJv4bXB9t4Mokipc4uJ72tMzz2Ar5kpjaX2RTAhK-tGGBZ5t7ypRtnyYBXUMyGWg_i9t2A_85nqiMVesaSHFP0KUPu7Wysq5_OkmfcwhOk9PMVxeKb5Rcin8jDwLsw7nTsnBo8_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=dsaShLkq6TsqlOxW0m-UTw29J5eP8M69Utqrz7oPVMsEOB2tp31t5kLvvXkOw6S_kZMrDsPh0Ud-pnI8U9Z4Dksn6312cjuJaS6_ShiHR_-r9y6LCypFjBzB06kI861j5urpGFoiRy33a24ljcyl32aWFHVsjeuSXa-3ktB9XfBFQKR5brNLGcwdk67uYjOFR2R424FevDt6nsz2FL5U4L-p4stI1KwWbnpoUa4Xhsd3ksJgrMzBKRVjR3jB7NMvGflmXfaejM3noA9WM6-2N8DxIv0dGQfQHcHHk2CF1jEiGTIO5nlnpc2AziEyQ-pHthN7GUv_BvL687zaN3BCMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=dsaShLkq6TsqlOxW0m-UTw29J5eP8M69Utqrz7oPVMsEOB2tp31t5kLvvXkOw6S_kZMrDsPh0Ud-pnI8U9Z4Dksn6312cjuJaS6_ShiHR_-r9y6LCypFjBzB06kI861j5urpGFoiRy33a24ljcyl32aWFHVsjeuSXa-3ktB9XfBFQKR5brNLGcwdk67uYjOFR2R424FevDt6nsz2FL5U4L-p4stI1KwWbnpoUa4Xhsd3ksJgrMzBKRVjR3jB7NMvGflmXfaejM3noA9WM6-2N8DxIv0dGQfQHcHHk2CF1jEiGTIO5nlnpc2AziEyQ-pHthN7GUv_BvL687zaN3BCMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf1OX_Tmx6TnWKap6A8qO5tu5qTKkYY-JE6Ts_0QDlr9PP4qJ5zHBoqOPyDEPiphx2j17EvB-w6Vagw6Bg6xVQGYYNR82_FngjubUiJfKVovoQZ8k8f9G8SWlxhC2EV4FS5TavvbR1zJoejvRTpD5D4cblUV_gRgocEm9516xA6tHVRHRqJNeZzTHLnVbRX6GJav98GJmcN332-0imytSDEd9Uy2r16i03qWxZvoD3A__uRfTWDuKCHKd9OJKAUikr9ZgXaIcwk-CANgpYUVFG5PRyxhcHwMmN26VyFOuqJmobvOFzuVCigu48yV7yecpkKxbvdT__vl45GGz1REww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ut646OfMaaFZjMwNrW7tDu2-QQTGgh49FiNsHzipImxaMGcglsEAzySqpY3w93XEpu2sAWzGHvP05AncZBySm-SQg2bMriGpQBru0HXrOwyOP-EWfhDtuLx9S9Lr2y6Haw_wPbassWsJWIbnFUPADTRN4R7wOZRvLVcfu8RIog0dRjWh3yXymcb0UoH5IqLo7jYhZjQz7N6o3uNJJpaV2ZYW6JZmrYmaBHBTG3iAACCq9FCJjJ2-TMWeuaNYokJIyF-ypHcXLaph3vH6CR9hYOIwtR3Gz6oErkiqxkEmqWqAoEhXAOm5R7j29t0-FsF82Pb6occJuJz9iOBlf-l6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEMcXamSs1mtjubIxDQPdittvDbGU1N_wdRyCWwznuOYmpO50NgEXYfSDwt51b0hyPsMViob_HuWFgmiYizwxhVOtAVq4YN7VjQGgtnPlBBfBU1zbi9uGZCoJavKonhdx_VjLA1DfvSjgGOEhZDo3WqIxuXLb3GXD_V-3NXn0qfsqkxk8vQek4nPzeZUV3e4iOyS3fhz2HoZJo2PTDEWcGR6vdVO76LZ3t_8xr1sz-TtybUfS_X6GAw9TcmeYUUAYfQ5z9-oPU1VgTnGJAaWCfNIpP829IMFSQX-jq-z8WS5bWsiK48kkYUss1BYJPYM-3Xz5gFxZhQJ065unBKaKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1hSGSwHFkkp9aGBnCgc6fI8TIpO3N19M_Gj2dCAbWzC9znqIioau5Jq3aIcF9oBw2zD-E7ixPhEKAm545vtPkyeS8Gibvb9RtpoEifY576Z7xJEkpIhDQwabgm8KdWbr6qe4SzEYv6u2mL41QvV5OtEy3oxWnuY-LTF7pvXUDUqCbrKN8CQQvumePFyqPCXC6_EYmOreLVvReDhFRfbRUnG4ecS5siOl2R7BZOTPvwZ25vkmqzbHS-JZUSYiB5ZxuOzEfnh4FZo0aHUaMgIVVvVbkFh1Qwu2atD7Mij00I-YWjsMAU2JpUW9lVVd9J7R0OvGsg4cAmQfUhmBqS5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=IGiqX6TYNNkUrS49dQEt1NQIq5nUs9_5fdaKS0fcvGHDdWzPdHM47_3dKRIrWqsEHi3o06SHCSuxiuZ6MOweGO9z8NKYbdoIZpv4WHsmcz1eptOqnIneCnDtOtgE0jAYFGPc9fpxl3veeUwT1xn2ewsNCdOcc_5gTCy1XsLqLRgly6XM7CXy14YAuu_QzscVM3iZfIDyz5Ibfk1Am6G2XhHNVt4v9EfQ-NusVNS7ZjMVJkHI5m8e9BIekrnzQ-xKXVkNhY59cFrHRuM5-Esi1ucHW9K0Wkfy3deJZ3_h3Kad6sXlrtTU8lU3yf4G9Ynj7dKbamKFcGT5lyV_kQGJ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=IGiqX6TYNNkUrS49dQEt1NQIq5nUs9_5fdaKS0fcvGHDdWzPdHM47_3dKRIrWqsEHi3o06SHCSuxiuZ6MOweGO9z8NKYbdoIZpv4WHsmcz1eptOqnIneCnDtOtgE0jAYFGPc9fpxl3veeUwT1xn2ewsNCdOcc_5gTCy1XsLqLRgly6XM7CXy14YAuu_QzscVM3iZfIDyz5Ibfk1Am6G2XhHNVt4v9EfQ-NusVNS7ZjMVJkHI5m8e9BIekrnzQ-xKXVkNhY59cFrHRuM5-Esi1ucHW9K0Wkfy3deJZ3_h3Kad6sXlrtTU8lU3yf4G9Ynj7dKbamKFcGT5lyV_kQGJ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=isz3_KKoOK4ZZuYbdqKfbuZLsbWUttMnelUXLmkadjlhJDC4WxmkWTe0nmEHPnUOw_RY-sWhnFq60kCwlhlvNyvhZdX42gm1473TMH4HlNP3oCaslPmGCbFEcomJP4kpSXYKy1QVFcSO0BUZDaHv2k28-DAPfWZDGn5MREjJxun7USf7482NqVMiOHErqOfJViq0Y9farz-nUy_9fhBB7D_kgH8WoXqCWJ3IE8KzFdqeuENrN-J0dP1VUp5ih2XRGGDoJd3Vlu6Z9kNWaTzdEX5jwcOEGlphxj7ycyxQ-HhPBsNKHU1WrJDOckBK2Xx-RqKN90c1XwjpOd_dACBuWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=isz3_KKoOK4ZZuYbdqKfbuZLsbWUttMnelUXLmkadjlhJDC4WxmkWTe0nmEHPnUOw_RY-sWhnFq60kCwlhlvNyvhZdX42gm1473TMH4HlNP3oCaslPmGCbFEcomJP4kpSXYKy1QVFcSO0BUZDaHv2k28-DAPfWZDGn5MREjJxun7USf7482NqVMiOHErqOfJViq0Y9farz-nUy_9fhBB7D_kgH8WoXqCWJ3IE8KzFdqeuENrN-J0dP1VUp5ih2XRGGDoJd3Vlu6Z9kNWaTzdEX5jwcOEGlphxj7ycyxQ-HhPBsNKHU1WrJDOckBK2Xx-RqKN90c1XwjpOd_dACBuWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJjapICJSwN4AM1R4w-AyWUoOpv-qpQCZqZMV7sm19XQFvb4NednmDCZqRsxE8NrF3dqBgZhfdhXAeUB8el726nDT1NFYSAN_Ctan8GQTIINjMH-ZYv1Faxi-pDLyj0QTHXbzslSmJg6we6YevJ5nGS_ypsM66t_oII15VlwYythxNR3E29NAv4ROWNvRbz85oZgUxLvQdgUv2dCUXUBGS7Pip27xrwdpVD_gBSUEIB-WmiICKNbBQ2MsGgYXu13a4t2z2I1DiAezAvyXG_XxuSCWsRAAo-ZN1-onzE3ptC1rUz5yqy_LSsPhwauOBGhK9rc0x56xrXOZkREzD-aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=OH38dDCRoa5Bv0cJgBRJ9vzJ3rT4sWOvSgsueWdELAJbEJKR7bGg5PbCtBcdn34XTga6sniW-AbXFM8FessjHqtibaMJHMi0AcZ753TQqyVMUFVdJLFSA5MVBR3-CVMBCTU8pb0zBEWIrMlm92Vpnr_cH3rrJnDtxoRpS2Um7dKJEXZOSgpaU2zyM_NABrDkrpnlspac6NtmK30wDvZY_AzTppAeuxqKUsEwxb7AfKiG7_CKfXSaba5Rn7rvlk7FhEV9v9bzTsGq58IXnFSQ9AAryk6TMEzV9M1YZXXzb8ZCwoI-52vCKOxuLW5EbrgkaTyywmU53SedfN8AIiOF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=OH38dDCRoa5Bv0cJgBRJ9vzJ3rT4sWOvSgsueWdELAJbEJKR7bGg5PbCtBcdn34XTga6sniW-AbXFM8FessjHqtibaMJHMi0AcZ753TQqyVMUFVdJLFSA5MVBR3-CVMBCTU8pb0zBEWIrMlm92Vpnr_cH3rrJnDtxoRpS2Um7dKJEXZOSgpaU2zyM_NABrDkrpnlspac6NtmK30wDvZY_AzTppAeuxqKUsEwxb7AfKiG7_CKfXSaba5Rn7rvlk7FhEV9v9bzTsGq58IXnFSQ9AAryk6TMEzV9M1YZXXzb8ZCwoI-52vCKOxuLW5EbrgkaTyywmU53SedfN8AIiOF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bWbUrOyBZM3izhAhP2DIJ3EJPGvYbOkQZTzstnDvMO8dRn3HGt3kn84vxZKURqbM2HkhZPm7rysiGEIvaxVFsHwQ-Y6o5tROTqNtFeiuirXmjuu_ugfppvwb05Hws8FcT0-NpeSB_qArCrlGV0RGrb6c1npAuc7hgaHq_bz4aihNuRV2VS8O13hs4-63tyu2Of_gWDF6jv3_s4OsFwTg1RRlKuz2Szh3fPp9HJwtndeIBXX_eVWr9OdTaYujFCwhNpeMocP6DCLU8JU52hYvkTAAUwPvKpJn1bY13zyLqVCIQQj8cHr7PUo03BxQUP6_SxjxXcSSUY8kMWCKiQ41FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bWbUrOyBZM3izhAhP2DIJ3EJPGvYbOkQZTzstnDvMO8dRn3HGt3kn84vxZKURqbM2HkhZPm7rysiGEIvaxVFsHwQ-Y6o5tROTqNtFeiuirXmjuu_ugfppvwb05Hws8FcT0-NpeSB_qArCrlGV0RGrb6c1npAuc7hgaHq_bz4aihNuRV2VS8O13hs4-63tyu2Of_gWDF6jv3_s4OsFwTg1RRlKuz2Szh3fPp9HJwtndeIBXX_eVWr9OdTaYujFCwhNpeMocP6DCLU8JU52hYvkTAAUwPvKpJn1bY13zyLqVCIQQj8cHr7PUo03BxQUP6_SxjxXcSSUY8kMWCKiQ41FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=f-p8b5_NHjvVBbHSdaxpv6PI4sPy7qkcLMeHA7zxEmAAFdCUTR_8hnNjyvby_7rROM-If1hB_KgOCQY6qqUh0nX9jku3yWjLIejG0HebdFr_qI3P_kKY2z8uYkgtvyjybdtWNcmVUK4k6_IDZqHE2r859zLe2lCTYmoOCxhUq280WWgd9_1lJdQxQ4LPrIOqgLewSqSsW-_8l09Pc_ihRdwiXCewusEMAnvbI9vjYsA8xo0cPz-QrUnpioMeVCZVECqNVbx-FX4MZKMD2oZG4YPFHSFI3xcPt4nKWN9zkuQbddakYAOXq_2PkzX_j4nePxstkW2-T5hjwTiYXm1PPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=f-p8b5_NHjvVBbHSdaxpv6PI4sPy7qkcLMeHA7zxEmAAFdCUTR_8hnNjyvby_7rROM-If1hB_KgOCQY6qqUh0nX9jku3yWjLIejG0HebdFr_qI3P_kKY2z8uYkgtvyjybdtWNcmVUK4k6_IDZqHE2r859zLe2lCTYmoOCxhUq280WWgd9_1lJdQxQ4LPrIOqgLewSqSsW-_8l09Pc_ihRdwiXCewusEMAnvbI9vjYsA8xo0cPz-QrUnpioMeVCZVECqNVbx-FX4MZKMD2oZG4YPFHSFI3xcPt4nKWN9zkuQbddakYAOXq_2PkzX_j4nePxstkW2-T5hjwTiYXm1PPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_LcFCOfYGXGp4MrYKLlUwxihlrB4Y1Kf-jg0WvOkAjAkiboAijGGRhzkCq0g7xV7q2HuXZncMneP5LBv9pYArRvYqnNYYYF3eyJlmInQaIk9YmiVjWCMcs90smDEXtf-lnpUdxLNhMCIodzud610JDkDfdnuYUqc0FAduvOEyhll9p9bSoU6s3qVglbXWCNIbSj6gXPFYcQs1t2BLV9Q2AFvqVj0dy6TbuwcTFi_Dm4aP92MejjBH5ym42BFUY8w_jPbTvK1WGVB5p7mo6TRPq-UQsTqAibKFyZrvLPzIQgVd2JZUEbSN4AWuj5pTMKFui8iXYG55FVojJ1twjoAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=J0F1vwsF0DuH_S6imUvwjjIXj_OnETVgFOHLKVh3f-_VHWvIKJu11Bs06H30PDUdhceWmNlT0LhQHJoygcA4spMx5NfDon07KYHd6mcTg1SMYrOx3BjQ01N00kkAii7mRlaGKi_CXrdFeMzyK1UPW5j1lUt-qd9Is4pz9O9Kk-o3Oo5lxW0ZmH9wIEIz-dDMs1VOkQMMkJusrHDj2loWE2HeC1LaGCDrQlysQbBIUXOp-mTdupQp5obzrhkZ-z8oqo7CDMbPaJyGq-8Th9KG4sODR5yuB2nLZMC3TmqRygu-6NKhM7Cdz4yfftd9fi5rVLGN9odxrQHANoxCUC-6vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=J0F1vwsF0DuH_S6imUvwjjIXj_OnETVgFOHLKVh3f-_VHWvIKJu11Bs06H30PDUdhceWmNlT0LhQHJoygcA4spMx5NfDon07KYHd6mcTg1SMYrOx3BjQ01N00kkAii7mRlaGKi_CXrdFeMzyK1UPW5j1lUt-qd9Is4pz9O9Kk-o3Oo5lxW0ZmH9wIEIz-dDMs1VOkQMMkJusrHDj2loWE2HeC1LaGCDrQlysQbBIUXOp-mTdupQp5obzrhkZ-z8oqo7CDMbPaJyGq-8Th9KG4sODR5yuB2nLZMC3TmqRygu-6NKhM7Cdz4yfftd9fi5rVLGN9odxrQHANoxCUC-6vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqnxi85eGX5sMWvSVmD-7Ov6_IOjZ1nIFrUY49DuouqdgXh3eWZWY8whIkh2mwVeWbkBb3_X1WtiSHkpl6uI4NXsKwYsAyie0_4PpMrs8CKhxw9HbTKlvSNBJLQgVOjsjYZifooXXvbdt_H4bTtIY3Ot5GU0oQN5st-VHQtCTXHpruBHbiYTg7FnS3fo8zYdS9LFkA5tBHoZa9drDJivbQeI7-OrxqLqSoUCvEse5ibdoFVCBH8sNQvqu9cUd5hZm4sF7ciYpagKEwbfexn-WnNel66wwoErQkAutXR5lBy5bUH7hmgUuTSHh4dngF2YQSJReteZi9Y_oWttfRAG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj0rgyh16P-_wNGNrBGyfKO2bXZE2qIUQ8vjrgrNP05tZ4LmqCuXFRQqlzLsQZcaWnDqgs9H4KprujVyADrvBES4GJAm2e6XPNJgRZlqV7GF6oDQUyfyZtJ783NoTiGBmERmvp5DMlZPe4rG0XOMQFqBI0EQBSxnhd7q9tPwDOqUfKK-sqRUgHQFYwkfvCTi0DS22Ee6xlR8ldU6sQgsSWLGkb9VKDRXZ3XuBAoBX6u1_YMrRoRsRyx3nbI8Nc6_3KQG-mMQvJHm0v12MsA0v23BwmJshNsNfBUUDRunqdnqW90gxysferm6zK-EhP9pzgXLqRUgV8n7Gr62DtdhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=GItewYavsdtdR0CCV8w6Gi8M6jmxAihfrzKu7wF2JgS77AtkCkkP2YcQfMyg3dF7wS0nB5eJERvS2YVizYfyf78KuPNNPg8K3f1n-Se5sHYICDVtaDjlJmWXCFi-mkzf8oNbWGp_dCxSfWBHoLmDi7km5Fm1wJR4gWUJOShCPBWNyDnsr4yzMOMnFc0CDepHn1opXggt20xsbN9NWqs0b6QfD8qTkdd53-EYpH2QLzRCV_U83bvkkjQIKW92SpCAYa-y98nIoCbGd1hQLZZn6Vywz5tydmgCSKJtB-mnjgVE-wScyvPKZ8oV6EwEJbI-InDozC-RzLK28p4IVhTN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=GItewYavsdtdR0CCV8w6Gi8M6jmxAihfrzKu7wF2JgS77AtkCkkP2YcQfMyg3dF7wS0nB5eJERvS2YVizYfyf78KuPNNPg8K3f1n-Se5sHYICDVtaDjlJmWXCFi-mkzf8oNbWGp_dCxSfWBHoLmDi7km5Fm1wJR4gWUJOShCPBWNyDnsr4yzMOMnFc0CDepHn1opXggt20xsbN9NWqs0b6QfD8qTkdd53-EYpH2QLzRCV_U83bvkkjQIKW92SpCAYa-y98nIoCbGd1hQLZZn6Vywz5tydmgCSKJtB-mnjgVE-wScyvPKZ8oV6EwEJbI-InDozC-RzLK28p4IVhTN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9RwTgYjbm9ZSMQbW858Yoe7aUrjLufdMAcEApATVzZdMRSRbSKHNsETvSIOPTJdIz7A7IzEfUoqDGHxOzxfRaaAxtqTY9E3Wpoz3rjX9t--wADbpUYaZnw06iwjiAwLoq6SWDAQcAX8MShXI_Vzm3a9SEB0SzYYJrszCoMEOOG0-jrddxcAhjAFMyn2eVtr51O5TEIrQuKMFhAjLSBIb5pQtWSTn0tgFfa50VkntYd9wQvHRPTdgDSD8KzT07BRTBjBL-cnL8BJFMOjUc9XOVjkS-dvb00X8zsDULzfN-mB6p4tpWLloCnfma_rW41ax9i8bSkolpVagp3eaB2MGG9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9RwTgYjbm9ZSMQbW858Yoe7aUrjLufdMAcEApATVzZdMRSRbSKHNsETvSIOPTJdIz7A7IzEfUoqDGHxOzxfRaaAxtqTY9E3Wpoz3rjX9t--wADbpUYaZnw06iwjiAwLoq6SWDAQcAX8MShXI_Vzm3a9SEB0SzYYJrszCoMEOOG0-jrddxcAhjAFMyn2eVtr51O5TEIrQuKMFhAjLSBIb5pQtWSTn0tgFfa50VkntYd9wQvHRPTdgDSD8KzT07BRTBjBL-cnL8BJFMOjUc9XOVjkS-dvb00X8zsDULzfN-mB6p4tpWLloCnfma_rW41ax9i8bSkolpVagp3eaB2MGG9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=UXkUUOHKAichWJfwLHEta7QtAYaM0FUtjZOjrcr9AuxDtTKU72s6Qlia4ZEzPNwqfC4yu95DhWiz33Got5GDUiSoVzxxpQ1OFAJOED4bfylOXGC0MaqDsBK7X3CLknv8VCWSj5VqIo2HH1nZA5puFULEPMOovjv2wFaTPn9iXzRtacBYSmysCUTTTXK2gAPrwOsCVMVDF50rW3L-xxF0WlY9dYw5ezRJ9OHNGvTMjPnpmbIlRQd_VIXAG16XJJ8NtP-tn5p0yhCHcBEWjiKViKlAVPf9OQlNnGV1OQ_qGABDKVUR3dwElE6R9ciEazT5jZT_hBvjeR6jnvEfi-QaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=UXkUUOHKAichWJfwLHEta7QtAYaM0FUtjZOjrcr9AuxDtTKU72s6Qlia4ZEzPNwqfC4yu95DhWiz33Got5GDUiSoVzxxpQ1OFAJOED4bfylOXGC0MaqDsBK7X3CLknv8VCWSj5VqIo2HH1nZA5puFULEPMOovjv2wFaTPn9iXzRtacBYSmysCUTTTXK2gAPrwOsCVMVDF50rW3L-xxF0WlY9dYw5ezRJ9OHNGvTMjPnpmbIlRQd_VIXAG16XJJ8NtP-tn5p0yhCHcBEWjiKViKlAVPf9OQlNnGV1OQ_qGABDKVUR3dwElE6R9ciEazT5jZT_hBvjeR6jnvEfi-QaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVlnQaR7LKzBqgCftz0PSNSwU25QVSu1tRYf8lf-is27ppdhd9eYhdkoe8XVLI3XAljEUm18aPEqlai-HJzZ524qZ2j9CkYSuFq1Xw2JSGktuF4dyXY6ObiUm9NAeeN2IBoDqgyxWNE4EAiFKcMIacfXTGRNYN2o8dazwIscV4XQ71UIiu-usFTBrRLEkw7t9WUq0WrVjrIFb5L4GuPLD2JSufISu43GMpaDNxBckQyU1cdRcKy-HG-TrV3rGLshVJflJNSdjX8gMd6iTjx2DFU_LPr2YNt9uDCtbU5hxXnmfF6h2706O4HHS749MsC3qphXHOf9qf5uPIXDiefCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=rKxScePlY868NMofpDYSVOVUehsvTvU6_G58X1FysYfPduWe7WldtAt83545m99PlBChPmCAc3DfApOBNRd1hLLylesLxHJzkvAxr3uLyo6XLKq26TqiYAJYocnO-Gyxv_DL4V6pTsoHqinKe5MfeYdz-a3MxrgZ03CyioNrKG2XGOKeV0bP-3UToc1M4LeK0fuj84NX2JnQWDatwddZjTqXRgrW-TVImFtW0eNpWrYVrja3QStixNjrBHg8ELvjCUVjYxlnu8mLYlPrrIIJ76Nu5lnGaLSX5RXSq11bgK-CkKktUW3xX1UemR2188bJymKAU4qLvdK5YynC2SmLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=rKxScePlY868NMofpDYSVOVUehsvTvU6_G58X1FysYfPduWe7WldtAt83545m99PlBChPmCAc3DfApOBNRd1hLLylesLxHJzkvAxr3uLyo6XLKq26TqiYAJYocnO-Gyxv_DL4V6pTsoHqinKe5MfeYdz-a3MxrgZ03CyioNrKG2XGOKeV0bP-3UToc1M4LeK0fuj84NX2JnQWDatwddZjTqXRgrW-TVImFtW0eNpWrYVrja3QStixNjrBHg8ELvjCUVjYxlnu8mLYlPrrIIJ76Nu5lnGaLSX5RXSq11bgK-CkKktUW3xX1UemR2188bJymKAU4qLvdK5YynC2SmLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=dNzprvD2gSpNROy-LUCoONltb9ooJuu6m-3iM8r_sUM_Ymk-h4QDwOGA6HRJGx5MssWPjFr4MZnyvsZY0lcck-fVKOw5WBqo2mZMjvgwtfhLACcYbfnGKBxiloZOKdHIAp2ZYaAT9Uisk9LNaDzWG4Rij8hXJMYiFYas_ZaqRPMH66p7vM3qtXicFM9def79js-Nnc8GlaOTfj0CBdLMAOT-a1DJSRLSd9k4SW7kSRwx9Zij0v1FbUzW7pkv7UlxXJD110ZE0aHmErTBZdeXVtYaH6u8PAlC30CfdaVulFlMSCDPn3D_WB6Qfor0Ld3pt1SG5cUBNceyxLijTRtBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=dNzprvD2gSpNROy-LUCoONltb9ooJuu6m-3iM8r_sUM_Ymk-h4QDwOGA6HRJGx5MssWPjFr4MZnyvsZY0lcck-fVKOw5WBqo2mZMjvgwtfhLACcYbfnGKBxiloZOKdHIAp2ZYaAT9Uisk9LNaDzWG4Rij8hXJMYiFYas_ZaqRPMH66p7vM3qtXicFM9def79js-Nnc8GlaOTfj0CBdLMAOT-a1DJSRLSd9k4SW7kSRwx9Zij0v1FbUzW7pkv7UlxXJD110ZE0aHmErTBZdeXVtYaH6u8PAlC30CfdaVulFlMSCDPn3D_WB6Qfor0Ld3pt1SG5cUBNceyxLijTRtBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=FVMv1q7qx7Fy5ToimXB_PaYAZqV4pAg5KYDOXGkyG7k7p_tOJZT_MQnX6i_vEMdWsv-gQ6ThAglNo3qDgaV5PfpTGtvSQmIpLA8oY3sFEWxonFI8blblCwjXbSQz-Ugtu9800m9U8zaUt-sNBIsKTjqxaV8e60Eb7mkKSjlSU1hrcb2qio2X3oF5XFnutkSUeq4M_k2KunPw4oaS9gG1MqAc_j_sS5gJFYjfFQjdJ1iQgONaV7R8HnQjRSiOs9o2Aqqw8QTtvBCgYnKrUPTqtoZrQ9QMzx9sDE0f3xIHAurGKMye7iHRi8Q2nbdN9Z7X-PeXK4hvX7FqnHDEPSuGfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=FVMv1q7qx7Fy5ToimXB_PaYAZqV4pAg5KYDOXGkyG7k7p_tOJZT_MQnX6i_vEMdWsv-gQ6ThAglNo3qDgaV5PfpTGtvSQmIpLA8oY3sFEWxonFI8blblCwjXbSQz-Ugtu9800m9U8zaUt-sNBIsKTjqxaV8e60Eb7mkKSjlSU1hrcb2qio2X3oF5XFnutkSUeq4M_k2KunPw4oaS9gG1MqAc_j_sS5gJFYjfFQjdJ1iQgONaV7R8HnQjRSiOs9o2Aqqw8QTtvBCgYnKrUPTqtoZrQ9QMzx9sDE0f3xIHAurGKMye7iHRi8Q2nbdN9Z7X-PeXK4hvX7FqnHDEPSuGfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YJpYupg9i2RtgIuCXpQ_A-G90NBiOShsJCw1stcm-isRYrHC3L65DVD-Frg_rmT9jQn_xK2F2Q3fmAl8zfFP-hQrTVcojgUN54C5W8hxe_XyUNnAT9Dv9y2MQaLgekPesJei76XZJenANtqDfLqMOikOeT31YvurIcckhGrglzjIFrUj5r2tgfAKm3sb-UKaV926GJVtRvYpHEe_4ugorYgaFT4UcFAshf5XWiq29rMRArp_9TQN74-umISl5-nU6fZdrpzbQTOHfYSeeI7UIaxxntkQIrRyXHnqfqLv8iadlsQumdnSj3DXuG4hi3uw89mssWJOai3Rlj3mwWQcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YJpYupg9i2RtgIuCXpQ_A-G90NBiOShsJCw1stcm-isRYrHC3L65DVD-Frg_rmT9jQn_xK2F2Q3fmAl8zfFP-hQrTVcojgUN54C5W8hxe_XyUNnAT9Dv9y2MQaLgekPesJei76XZJenANtqDfLqMOikOeT31YvurIcckhGrglzjIFrUj5r2tgfAKm3sb-UKaV926GJVtRvYpHEe_4ugorYgaFT4UcFAshf5XWiq29rMRArp_9TQN74-umISl5-nU6fZdrpzbQTOHfYSeeI7UIaxxntkQIrRyXHnqfqLv8iadlsQumdnSj3DXuG4hi3uw89mssWJOai3Rlj3mwWQcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acURp88YRuK2HrIbzO5qWU8R8NRtyoDaKX6kpc7IrzYMZmFej_9VC2qmIJWLIih-waAW3KVBfWkjCAI-X245HO3BbLA46B2lin-aBcK64muVfzmtmwe6hM1zz4eCMqkTD1slWdL8s_RedDoh51_qI5d0MKV8p7fJ_eMSYtvX_grrttWM4ThssmKjap2h3311aGPUCOuLg3cTk-Pmi01RWer_JzzwJpk58inYJwQnEpUuZoH1YGW7lOqSGcMVN4IdVXEK2Lsc3GhL7nBIYwkBRLu-2s6JtTqBQL8-vOEz9SKq_rgjW56JcXezXLnd1O1bFQ7y1wiGDzC_LDKWWr6ccQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=RsxzDYXhB7sJ4_fDZVCdYmCdT9Ecu0FeAJJfjDWVhGLvE4w6wJSAnx2g83ApZId48Zv4L5gZ_ZtZrVrcbEzOko6MdQu37Wm-lag2Mg6U3F7NrJ3Z74fdM_8Q78HXRbFLe4K66VPUTuwcHchqx6RbOpG0bHuWBxwYTdIQTJpuz_lfps3Ti3_Jr-fMmNogE62XR-6-SGLLqwb3vAmIIN3mxdl31KwmdsasTvlVfUbRsnbRlV9FWtqLpgtfP5_9PI3h78y81FZTD3TZJb68wGicPalMjz1NHg6mWPkh2anYAQ8DI6q0x3F-3RFPdiyDIBhfCYmccKJT9TfMfYnZE9-Uyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=RsxzDYXhB7sJ4_fDZVCdYmCdT9Ecu0FeAJJfjDWVhGLvE4w6wJSAnx2g83ApZId48Zv4L5gZ_ZtZrVrcbEzOko6MdQu37Wm-lag2Mg6U3F7NrJ3Z74fdM_8Q78HXRbFLe4K66VPUTuwcHchqx6RbOpG0bHuWBxwYTdIQTJpuz_lfps3Ti3_Jr-fMmNogE62XR-6-SGLLqwb3vAmIIN3mxdl31KwmdsasTvlVfUbRsnbRlV9FWtqLpgtfP5_9PI3h78y81FZTD3TZJb68wGicPalMjz1NHg6mWPkh2anYAQ8DI6q0x3F-3RFPdiyDIBhfCYmccKJT9TfMfYnZE9-Uyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=q_Xdyq39cK19CZDzByp9l8jgxG1Dd46areeTWLd72h-7475-KonQtKW1AQN8I4IIe25TWiKZNXtJDPYVhwIH_U9oGYT5Hg0HBSmH_NwscHeetp-rErsn3pxfyWGBueDOuiDrtrFpA25IvV9NqLY3YFXSqj6VwpTz_aUBPEdJTdmm6zZlUaaH7GoGg3mNjQcThFg0shPYj-SF_ss5aCc0jwu55Z5Wh7DeJyzeNJcRZNt2EVMH7UX-4LEqPscYnKS8yzqhv6EuonJlGV6xJ5PUK9rOG0Ds9pcaw7kmrMDKhfO9iLAgwMcWfIDwjnEXVHJTImMbzIDwAs_F3C7vJDoDKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=q_Xdyq39cK19CZDzByp9l8jgxG1Dd46areeTWLd72h-7475-KonQtKW1AQN8I4IIe25TWiKZNXtJDPYVhwIH_U9oGYT5Hg0HBSmH_NwscHeetp-rErsn3pxfyWGBueDOuiDrtrFpA25IvV9NqLY3YFXSqj6VwpTz_aUBPEdJTdmm6zZlUaaH7GoGg3mNjQcThFg0shPYj-SF_ss5aCc0jwu55Z5Wh7DeJyzeNJcRZNt2EVMH7UX-4LEqPscYnKS8yzqhv6EuonJlGV6xJ5PUK9rOG0Ds9pcaw7kmrMDKhfO9iLAgwMcWfIDwjnEXVHJTImMbzIDwAs_F3C7vJDoDKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAR_LBGpojFZA4rg0Qcd7U5-VVhZu4D-FjgdaR7q0g84LZrcCeLx_OCSgEDJ4YXdA-GcePDUrn43DbBMuOrUbQvd8mA1uQwwwRo65lmzRyS_VD4RzaeUsfbsK0-V-xuzEMP99BFnHSb9NWcbgugMgHvZZ4-1y7IYV3R_gpCn3qN1u131hvm7GY1DKC_yiqaXSKTDONQ43xK_kkn80OrmWYt_r01eqZy5M6BZJLWHsiS2t2CR3EKVSaa-Gke4ZwcbyUgku40YyTFJo8TlHlOEOW-m0c--te7UiX-Xz5AA3lW4W27YJNfHrCxcN0bwmzsNQrZFMQpiCdeYBxodMpgcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=mWxZ2ssMCwLJgUcEMZF2VbpcH0xNremiIEEcVl3J-66q8Lp-s4fsMXQes1SUzAclDT2nUjcTs5B5oI9Y0Hi5QP6a-5U42zMY1C7ScF87BfH5WgW5nx99i00wlZWh9IjyUidzMqmC_L0vxIO4bmSkdTBgtPzihSbA6-IISAdiOszgBLnBGYRnoFQhpwEWAmK4KcEVPwHXYsthr5BkkwQMljuIwhEBWnBvCkU9S3054aqywGfg9DXspunBqQOyEblPydvs0eFHONIqByqvmIzlg6MzsCATvcPpGYE7VaCRvcxI_JizyaH7LteQ3GIpK7HWGIf0NAeGpFDkRiAKfQLHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=mWxZ2ssMCwLJgUcEMZF2VbpcH0xNremiIEEcVl3J-66q8Lp-s4fsMXQes1SUzAclDT2nUjcTs5B5oI9Y0Hi5QP6a-5U42zMY1C7ScF87BfH5WgW5nx99i00wlZWh9IjyUidzMqmC_L0vxIO4bmSkdTBgtPzihSbA6-IISAdiOszgBLnBGYRnoFQhpwEWAmK4KcEVPwHXYsthr5BkkwQMljuIwhEBWnBvCkU9S3054aqywGfg9DXspunBqQOyEblPydvs0eFHONIqByqvmIzlg6MzsCATvcPpGYE7VaCRvcxI_JizyaH7LteQ3GIpK7HWGIf0NAeGpFDkRiAKfQLHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=TYzxTNWUFYzjIeGUuLBC4O0sGwf2TFBx412mglrw-vfyDkid7NRQ73mcB2-zvLgAAJP7Fq_Zu91rQi7quslRxPjq4UHHcNew00QAJQDOMBOMfc3Y3T7APRkNSFJLHtZS1x-pkXYfCWlck3Oc3EqeKoOusG7avP31y6FUUeGKhbLwKNlK9iuJ-Cco23efHMCSI9Dkd7IyChSVLgPRodF932A88HJ7GPdqp7lxs5Gy_tT--nIdc1OTVSQu8Gv_Wtmu-CsnlqYh4zRcA98qVN8RQu6U-3qevwNf9mvCidRCUINpD81HxbFRn_YbEISMHJ1gfkPkQ0RMnEg-EuluBYj_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=TYzxTNWUFYzjIeGUuLBC4O0sGwf2TFBx412mglrw-vfyDkid7NRQ73mcB2-zvLgAAJP7Fq_Zu91rQi7quslRxPjq4UHHcNew00QAJQDOMBOMfc3Y3T7APRkNSFJLHtZS1x-pkXYfCWlck3Oc3EqeKoOusG7avP31y6FUUeGKhbLwKNlK9iuJ-Cco23efHMCSI9Dkd7IyChSVLgPRodF932A88HJ7GPdqp7lxs5Gy_tT--nIdc1OTVSQu8Gv_Wtmu-CsnlqYh4zRcA98qVN8RQu6U-3qevwNf9mvCidRCUINpD81HxbFRn_YbEISMHJ1gfkPkQ0RMnEg-EuluBYj_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=PFeYpixyGwnrtdC-bmDhHs0cq8Mc7DQC24H1n01_gIkjq23iiXia1Q9rcrf_GmgVTy0PfhNoTsiVQLdrTXmY5IEO6lZUH9doDFRsZoRgcyA1vvdAlgBYf3olIJfqKStepDKWNwGMjJcE28aLZkfLtKvIlB84Z2nt_D5dZ4hStYFUdxHYuzFf0Gnk8xTMfvLzwv_uwFPqXtS7Dkv8pHa-yIkE_n44Xe86IWhgD0nRf5ZNvxw4R7NBj3Sl2IJeI8VosMiHxai-im0Xr5aj4j92k03N3Aaqi9i7OV_JmwGAClsWARTRTrwsX_MbpFbSKV76hH88DGRir3CjmSuYbvLh5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=PFeYpixyGwnrtdC-bmDhHs0cq8Mc7DQC24H1n01_gIkjq23iiXia1Q9rcrf_GmgVTy0PfhNoTsiVQLdrTXmY5IEO6lZUH9doDFRsZoRgcyA1vvdAlgBYf3olIJfqKStepDKWNwGMjJcE28aLZkfLtKvIlB84Z2nt_D5dZ4hStYFUdxHYuzFf0Gnk8xTMfvLzwv_uwFPqXtS7Dkv8pHa-yIkE_n44Xe86IWhgD0nRf5ZNvxw4R7NBj3Sl2IJeI8VosMiHxai-im0Xr5aj4j92k03N3Aaqi9i7OV_JmwGAClsWARTRTrwsX_MbpFbSKV76hH88DGRir3CjmSuYbvLh5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXaPPWLi8AiQGivqpZTDlD73ktbmyaFBh5INfRu2VgvzDCvfQpWnp2ebdD2WFu1Zt8bvHpOd3Om88eDhQhEvY3d4VeT74mJ5MqOpAhaI3VRStSwPZdvE7iiUEKvVkuocztJlOGFin5Bsdl2SAqWoFKmP_BWUQo5v4_DS8R2ldr6xSIli2Tg4o8TzMEi5BxseF_3oniiRTtxqau7WE0PRqvp04MKhn_V-hb3WiftVgcFtkQazGeexYir7XcwHtsgU15Ls7mx_WyzeOheuZ9F-z6EUUFVEVmnMeDwhoTYskAYCsbP3AkjdwsZuyQttVoVxg1XLtLnJdrsLYMzv29rCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYvubX4AmkPOPhMmF0WIlNI7TeW1JA-Vh_rRp9R1Lf8JfBJWXnr9gxdvizbFRvlO5kWK5_2fi87bPy8BOhAsrt0z2ilk_MXGEQV3kWjECo0fOvAiJqKW7-irwm6yF9GZ_RkwxvPFSYrk5u8tMrV93D9nQv24R9ZIX3UpFwsgiMmBvrLl7FKQRCJhXbYmMNgIvIDuBeLnuBF3HaiibqgQvL7hq2E9LbbNEoFjE1eg1n_fZ5RRtcsBSF2N_N8-A5riJJPsj5j0hGMAZHVRNKZWoz_K18xh2dKQyyNSF92bsIKYKlDsczb3uWfMl4q5j6UoZWjD9VJsEp2O1ii6Tm6oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz2lYJdYZf2uB-8tsReVZbjA3IBXClHBMSNFAoY0M2V42UajCeOFnXk8ONYY-bFxTqLZV_hXAJJQe2sKhde3r01se7efrdgtwGm0hdVCb_9Oa7JQ5Yw8WTb89vHePDQ3qZiw9buwoT2k5GtfsApCBfxdvBk_Klks0W3dDI75sckq_UlCFQS4TYuJvxx37SZb0SLEcZaITKUEH1KSXHzlVxzo3RAwNYAahs-ITuhnOO8_LTCzkYUDa2dBXJPuxw9suyeEjndIv29N-Tq-mDro2-VTpZpnKpLXDCSfSMzB3lC2xQwxTYJUT8N-ma355MPxuy1K8I4P7r8r8UioFacYFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=UKLR3_Vn4PAiVw6g-oLhGnAM9I7pG1iz0Q7IuB6t3NkDHi1d51rwW7WEovj9aa6_LBkc1gRXAD8nygTQqX6Le-0tgNX1QPIkrpJsLohgL_NTpORWZVk7Y9b0BkY1A8hDoDh4s3g6o4UZosfBpEPy7qL0_3jHh1F7a1jnVgtCQLA5LukOPCZ2lU8PZdZFVUPTnB8Khz-RKf4HturdhSyoYZDTrH2F_VlO3OlhcMqmWTSr17tY5ymt_jQx_Kbqw6clnwlarKl8gLHBHMEmT9J4wq9cFPaac-aeJm_S90q4sXwh3kBZLPG-ap4h01KV_AyydLtM5gFSzf09mKMxthBnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=UKLR3_Vn4PAiVw6g-oLhGnAM9I7pG1iz0Q7IuB6t3NkDHi1d51rwW7WEovj9aa6_LBkc1gRXAD8nygTQqX6Le-0tgNX1QPIkrpJsLohgL_NTpORWZVk7Y9b0BkY1A8hDoDh4s3g6o4UZosfBpEPy7qL0_3jHh1F7a1jnVgtCQLA5LukOPCZ2lU8PZdZFVUPTnB8Khz-RKf4HturdhSyoYZDTrH2F_VlO3OlhcMqmWTSr17tY5ymt_jQx_Kbqw6clnwlarKl8gLHBHMEmT9J4wq9cFPaac-aeJm_S90q4sXwh3kBZLPG-ap4h01KV_AyydLtM5gFSzf09mKMxthBnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_0GC9dm7f5h4mpEkGW1MVBdCtXwtYPoFQkatOFTXrtG_dx7Uaobv4a317YY5tfdoTYd8G9bEQ7jNDmhL1oEJRxOSgvtmzn-FpJM82NUAiQaIqvtFsrZYFBNzwX5Mlnvz0uAURM4AlmjG5-jzWwh8cRvInzLHrbHODoZ4VGo-WTV1dpoOxeQK6fk5CgHzH7Ff1RyospdcM5Gu-XpsT5w4pgyvjrrr2pu1BW1wnDDaeawsmFteA8tZVILAMhyXQXnJXVlxiuRyzpfZsujnGK6wVjnX6EEvTO_PyVmGyxSLXhjQgiUyKFpT1reEAqaZKnuBlrLUt9rgQPqDTVDZbu-xVNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_0GC9dm7f5h4mpEkGW1MVBdCtXwtYPoFQkatOFTXrtG_dx7Uaobv4a317YY5tfdoTYd8G9bEQ7jNDmhL1oEJRxOSgvtmzn-FpJM82NUAiQaIqvtFsrZYFBNzwX5Mlnvz0uAURM4AlmjG5-jzWwh8cRvInzLHrbHODoZ4VGo-WTV1dpoOxeQK6fk5CgHzH7Ff1RyospdcM5Gu-XpsT5w4pgyvjrrr2pu1BW1wnDDaeawsmFteA8tZVILAMhyXQXnJXVlxiuRyzpfZsujnGK6wVjnX6EEvTO_PyVmGyxSLXhjQgiUyKFpT1reEAqaZKnuBlrLUt9rgQPqDTVDZbu-xVNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
