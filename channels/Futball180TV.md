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
<img src="https://cdn5.telesco.pe/file/YY4PXxtnkFfUcBm438lPy88QxJ3ZB-XJtLVlCG_lRKQSEBd2FqDRQcc-sUXUprEtIgE3MPjP0iwB9cN8eDkvkwCzqFeArgeuUOnYLwvzOi6YEDTSjuj4SPH50psm_53PwGglGnnpbSH8ohTwHkmMrMP02yMWvr_BLHtnjeoaqL9fptQo6W4XhdQBz_xVMYlEPODUDd4qYDYOyEZUm2_CSVAd8NkmRKga-_tnE7fcZ8BSOoDbd6nekoCjqABj7ziGRuUxQvizQvjK0BXixec0B73jzrED1j8WbdybKgOYetKlH04szBqXt_Z-x9EEeNQpBaHjKN5TKwAMw0tjzp2xZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 515K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui0yjMm3Zu_G7dypiiDJsg8_6GQ75FHzuwTHQMMhomacq8FgKZY3FvZpqAdLZRVzYGxMJzVktfYWcYXGp3imXZjNMUF-Sx7ICIVWk06MuNAIHeM4SPzySDmuMmcwWlxiurlkZbpZMUG2HpHCy__Pyo972dvVv0PUp6OEk6dsSjD3lCkay-d5Whjeq-R8LtgFl80IaAEl8PH0msZ7wiQg2hbVmEZIrln2WzHqpGdFmMFYcW1Gd4_63HG7LBHeVfZtLJo7_LtxIkwmBUIAF2wtZaDHH09FJsxg1aprS6pL6ehg2fuaUr7xdILIuGNmF0TwMjD1JEA6_OyQIEh_-S4abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faE1UTWfzVRT-YUIB8NhxDVHpFO7zzfMMRg2D2hhioWxfsSg9if5MFl0jeXrGV3D-WGQTaFYZ5qFMO1EEHqFCp4zcemOUaAwexSe_srmLfwiE5xH_U-NjlGMEsnjbjgLp22x1SVKw4kaphVIkiKhl56V3nA2i6wP6UVuuQa_IizjieDjuZcAvVWqFzC4yYTN-s4GJEfdOYWsje46DlmQEPknzwTbVKPfTzmxesHgqVTPfx1y7Hs7hxFILoaOxAmE3S4vSScAkednbp0TmAyLbK1IXzcbTWde2DKi1IbJObs9qfMyWZE2u20xeKIDEVhSEG-TN_EgtD1cbqO7i63anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbqTszGhruKTcBZz6spydkSXn1EGrT2HrBnYAp4ZXlIzK7RWZYh63qZGypaJUCXcQS2dF_csmkj9grrTWUOYepiaJCjEW4jJfOBGo2QjkQJvn63pQAkJngFjscd_1u-bBAdqEGmwsw41omzgXHf7optN-F3KLZlfVNiPKlxIAbyYd00eHAk5dF__X4ZvLjudSyKz5wnwx6ZHWvxpitj7X6bLcJUAF2eyEY0IgH1CeIB_mLHLxfAZtmRDcM0aWUK085gvVRxwBkKQu7UeEGV4oO1q1ICGwX_H0omMbuSl1zG6T2iZOSmtbYRwzNeGUhCYgQTOc-XP0urG_vZ8uumJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=cISLELarF2jhFhJ8pQSa8_IH37Pq4T_gOjDvwkAqS8jIPYQhiNx740MFylhncNjwZ8FDgfS8O1OEcUaFdRm15scAGDT1K5RwXqi2GXAPMnCeKdhVV37hudCFiZycBgeResBNo-Qe3Hi-DpbIjfhGTnl_ql7iw1wwiTPUFY356LbwGOpok5RCZWFsOe6qUCytgJPnYXud6Xdu-oAXmhGlmzRCIOXg0PdMGPkYOyd8wY3q0hJ1nbwtULO038mWjHNCMBMRJUrXtb8_QQvGqwIKwWKtmmvVowcdvT0Upqd0O5cYDYwoykBcidMqYqE-X3tr86HtQnKEgBfgh812IefxJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=cISLELarF2jhFhJ8pQSa8_IH37Pq4T_gOjDvwkAqS8jIPYQhiNx740MFylhncNjwZ8FDgfS8O1OEcUaFdRm15scAGDT1K5RwXqi2GXAPMnCeKdhVV37hudCFiZycBgeResBNo-Qe3Hi-DpbIjfhGTnl_ql7iw1wwiTPUFY356LbwGOpok5RCZWFsOe6qUCytgJPnYXud6Xdu-oAXmhGlmzRCIOXg0PdMGPkYOyd8wY3q0hJ1nbwtULO038mWjHNCMBMRJUrXtb8_QQvGqwIKwWKtmmvVowcdvT0Upqd0O5cYDYwoykBcidMqYqE-X3tr86HtQnKEgBfgh812IefxJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALFpusfkqhS16RHYdF-9BX5WjbXwe2FopnxYuKyfbnE-aSh8RIxa1e_IYpPmFgmiSAimEXWW0xq46Lf-CZRLNnenyLisPH_YPqEDiZv4ZGWxsNwjo0quTtz7xmRBHd9yFp1x-ngyyVpCVHkWHA1UtnlAnfn6dBCpAxglA1p5GjTJazvluNbuEGuODsLpwugDRDDSbIjKcOp4FnkuIssvGj0bgRP1mqpYO4JTehiIW_8PYbI6tLAv98E5_MnLSLTR8apWYHOuFgdGZ8zTJDEBlZ9ixO4cquLKPlZO5qjyNJhR68bfA4EBHoYuQBWTRLrRvqZddUxwzYiEJtFsaV6ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=ZpoMOUhuzHxVYqwPA3zlD9VQF2rXJtauLXZUG6KQ6wjq4vXQm2iiVnUk2VOKV0_7BA84R_4SnZBkgEzZQpSnMc6ZHeYXQvc5bwYvuSHnx9h08hbsDGZV4D0--M9oechFmH-WLVKuFVU7CUEvzHVsce5wbpQY64n6YahH7ATB_hxgONy0nO_sGaAx34KUBikOhY9C1K6KLyWyRtABHZHuLDddA30A7vGI7Pfk82IaMTB-WjgwqgbH81r3nr5ef2azXRmPAlDyU0IiJSZA-m3YkdsI5sjubO4x3k7-orXThiQmnwt0UMENnIOwc-Cm75KihU828sorM4i_s9kD0UsBwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=ZpoMOUhuzHxVYqwPA3zlD9VQF2rXJtauLXZUG6KQ6wjq4vXQm2iiVnUk2VOKV0_7BA84R_4SnZBkgEzZQpSnMc6ZHeYXQvc5bwYvuSHnx9h08hbsDGZV4D0--M9oechFmH-WLVKuFVU7CUEvzHVsce5wbpQY64n6YahH7ATB_hxgONy0nO_sGaAx34KUBikOhY9C1K6KLyWyRtABHZHuLDddA30A7vGI7Pfk82IaMTB-WjgwqgbH81r3nr5ef2azXRmPAlDyU0IiJSZA-m3YkdsI5sjubO4x3k7-orXThiQmnwt0UMENnIOwc-Cm75KihU828sorM4i_s9kD0UsBwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMj5LnjhZDgTnm3otnzXSTdAwbR7COjnT_xz4O1qYbmU6b3G1SPnOpKnoyGlVtzCt-9ykjY3qJ8f1WGBJ9fKhEjiscfM5XycAN0gF_UG2Ja2ABpsoealEB3jE_HastBhyasJIaEysUhroauGCt4IQTiQJx6GjmcSWp7DIT7fcyM_OfBBpmhKTY6xhepgiRmmj2sAIY-zT2CIainp7QGxUzlaXgdo4slHt32fJBC0JQgbFmrIS598ydCGDunCMg6Jdubx1spcDdZOyMz93FPiT3jEeXR-BXbbbXTX6zk_26Jcr79W0qMDsGXPP2KcmLLLGVVqCw1ydWRnYjSrB5qsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=Je1CiC0t29W2ABU0pVsfts5_lKsRQa8TEsE5f0Iyj7AzFtH6K1BwBtGoY6QnW7EtsTP-Lnwt3wovjYN5SuDQv0gJ5ppiCc9-IMu3VhF52-8g870NnyorHaB1G-PjHzipGrietd1khd2cjDaLyJC2h_IhCOETChtY2mkiBUGDvlHb32-yPcm7kXL27Wk08UvKY9RVtpVkorEtE9Jeng7xO_tVsKpe09HLAJoSJcRybpU2l8_7WCKFcy66djoDdqWaNP-qKLDERrrQdFxB9JdA4fLqaSoRtgFTZGHVznXlnrH0QNqaUHwwNRcaV37dwFZZldrzN6pVlHXTBxxfLB7bsrj3v1Z_f1YXVUJeqS2bEIHgO8OMl6eo1NRS8WJs4hNQx4KObGSSWsrQk2MUg9urzzvwX5Zi9IrCBjGyQL610BUvtS-mk6rRHRrjUVtjqz8M6R57RZLqZSUwMFS8fIjj9QAlET7uiLCHi5pm2gUJWaEElGmnQCR9_8pL3lDSi-phCDBfFm2BBih7FetbMn5nW4wCeN6fMqvvQdBxb68kxwAq9VPK_07GPP3KMuKVYmp2u2q3q5iDE2i15ac5dnm5oaU-y769vbxjc3CxwMA3EGSbvzUlmPtfrbpuOz1N1jGmtBA_QP2ztRkWBQCuI35sTlaV2tmQsLiKcLyqqgIEdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=Je1CiC0t29W2ABU0pVsfts5_lKsRQa8TEsE5f0Iyj7AzFtH6K1BwBtGoY6QnW7EtsTP-Lnwt3wovjYN5SuDQv0gJ5ppiCc9-IMu3VhF52-8g870NnyorHaB1G-PjHzipGrietd1khd2cjDaLyJC2h_IhCOETChtY2mkiBUGDvlHb32-yPcm7kXL27Wk08UvKY9RVtpVkorEtE9Jeng7xO_tVsKpe09HLAJoSJcRybpU2l8_7WCKFcy66djoDdqWaNP-qKLDERrrQdFxB9JdA4fLqaSoRtgFTZGHVznXlnrH0QNqaUHwwNRcaV37dwFZZldrzN6pVlHXTBxxfLB7bsrj3v1Z_f1YXVUJeqS2bEIHgO8OMl6eo1NRS8WJs4hNQx4KObGSSWsrQk2MUg9urzzvwX5Zi9IrCBjGyQL610BUvtS-mk6rRHRrjUVtjqz8M6R57RZLqZSUwMFS8fIjj9QAlET7uiLCHi5pm2gUJWaEElGmnQCR9_8pL3lDSi-phCDBfFm2BBih7FetbMn5nW4wCeN6fMqvvQdBxb68kxwAq9VPK_07GPP3KMuKVYmp2u2q3q5iDE2i15ac5dnm5oaU-y769vbxjc3CxwMA3EGSbvzUlmPtfrbpuOz1N1jGmtBA_QP2ztRkWBQCuI35sTlaV2tmQsLiKcLyqqgIEdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEJMNlow4DcwW_9119Wz1nFaHdTkgP-wjRKoD1boZ8n4Ch5BJrEZYQMkjhul1mh3YvgTejVG2oQ-sL62JF6myyxiVy5nk_lv3cpB1QRQDDyWB3v9gzrIFdU0oTeEKMkb415yOdug7BLF536S-iywHTUTCpNK0NknO8HwTSPBrspEx1ioxtKw2x9bYfHHlBqdaE58ST-4LXu_vqgNv0R3lYZHF7YZX1JDcfTvbcKNFsUVQLaUxeKLJz55SpOz_nWZXhWaydStiONsS6EG6GzFLtnSP45BID4j8Y3yYDafc8ei7RYUAtDmhB6ks0zJxrNTFEu9nIkjrY4TvgKJVkxfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzzwbTTBo1JCNNmBAGlbnYMcJrbu56nG9IHBFr241r8xobnuGxV3ZTQMhRzKiSpM-PIPdyCSivgcehGt2d-WvRKBOMnYsS63bzg0Nx583wX0rk6g2EcfHB5p4bbwVLdd88DIQY6x12PZihTJdLr986siX2TaEMnSbjIcey1bNUjAUGaqnlAER1l53gnQNC5Tk85D6Dnqpm1DIVI4Vi8cwpb5T_SubCb_bgU5zcYFuopWdSxugzgFGBFZ7Z2fl8zZVclLnl4QMCzI91tQmgFGazUnYhDMwd8fyoSgV6Yyg1w2ODtvd_iEIbKv_HM-jUE7oHXW2SdHTPAr2KRT3kkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qErXcoTLANmqxBBWHQpuV3P028prtp6qLYy8zvrSKB7xVgNJwBtFl9el15ny2Agv0HO-e4U2WahZWAQRBxiU810naDWOw6bvLm4TdlcwB-R5uiuewox_J2jVvnP8oyat2FcFq_zWSWeYKMcyyFM72Kg1_SgHQcbskndtz4MSJf7SAigy-CA0IM9VfEqnJMz6cADJE5opsWHZhfldpWI_XVYVC44u_QdSJdBr5Ze_ic3uEupKcXfSRz6fMVU8BtLW56SDK7kTImYDEQpt-V_2JnRtXDCk4_pSTGTBhXfEErx-DFMaVn2CLysdzUWvKdtnVdF9TBGwz7hU9gdf1ZyZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkwZHE4IK-tosQtkmuXrA60s1FoxjccGyT25oTN6VLiGVbvIrs9J3jiHepZ1AyT8rgM3ow3kWKO92XYTqq9D31O9bExB9m_mRYzPjiP1FOi_gdOtTym6r_DQG5Ygg0bYzUalPDpWH5p7gG2xMFUorAXVPQFeEg6GZN-Mbi_jNiR9JdKghwSmzHbgC_f1K0pZtQWLtqpE4pLVAUyiNzTZ-TQQxZ6umv8IBSHvifaP_L1WhlWbOS2GwAF1UEKTHP8dmC_jS9YEqTy4mJjK0U7Lhf33IOhu9JjGbVxwJloWoju1qsPEr6YKFqmojvmQ4K494mdjtpQrcG_s731Ww4HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syXeCFbI8YaiJhKiuKBO_I_xbyIBoEDStEyPwOtfyr8hBkBoqX4yCJzJUwpbdLY3RT9QZSyO42jvAwfp1CIOS-RgO0SAkgeFAZNFR3itc-87HyOm7nR4DOk_tIzyy09DezEdmtU7JGjKLit9v5Mus0QESu6je50pxmlE2_zvmBBdF4u99q6KLXN4Ad_Sxu9UZqRDNAm5X2f3Omw4MCCv40GwXAkOp0-N0faHPLh6i1XVGOIPkmpM2Hw1zpUa6pnGJA7oYW1Iwa3nxWhulEcvnJx9hc8O8zmN4AXpROHTEFSe_3wlOiBTb_8SlUdfeOEZ4bi863GwbDy4SXI9tcjd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTPdY2MZZtpZL9mt6iY7NYc2GA5RIkhGG5DRwgRrXBCdnwvqgFFPtI_2dINaAh7S3MFwygjex9Wz4vKdkvBM1qizkKEY1roKata5Yt7vR9CtZTtLyiQI6B5Qw9SH4ewBpDXlzIdc-f2Ltcy3zHpXPbVS0kLpY0N0hvBMGbBB715pENz4PrfOhGlomBMs4XnuCo5IZDUjAY4Eieo1VmflPMeKovfmKeq4nWV9Neaa3nRiNiwZrppTxo7EJDzl-fEoOUPCyyHCIISKRLPsJd4xRE4RvJPy1oQTyeMcUE-IQWXmp2GUli09tWVUsuhckO3PIEj7v82w1tXPz2xAxTOa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=aOoaKdp0oLdPrhrSQ2l2KmApGePVIkL1YZrk1ckW9UyNHosZNZeotCjQzVc4H5A4kjAexsop83J0KNUT2t-1MRJwhUYU-O8dZsTWPaIR8MWGkb46VU4TVtPlfS0sZXLXUsrgdTyWrnRY9iQ-ERLMqiEqOzKvBRbW_j4V29xp3Xb74D-FhfIDS-N2YjwrAjWgAxcaMiZaPh8fN4xAtsstqRvJEuOmxgk2b-HMK6SZtGjwPrfbKYhS_AO870-QWqlBMqFn9neY2aslndnrTlmQER4_6slIvyDnfN0mK2glcw61eJ5ZvQruf-AzHeJYLfL0cT7p4e15J2RumLhEbyGuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=aOoaKdp0oLdPrhrSQ2l2KmApGePVIkL1YZrk1ckW9UyNHosZNZeotCjQzVc4H5A4kjAexsop83J0KNUT2t-1MRJwhUYU-O8dZsTWPaIR8MWGkb46VU4TVtPlfS0sZXLXUsrgdTyWrnRY9iQ-ERLMqiEqOzKvBRbW_j4V29xp3Xb74D-FhfIDS-N2YjwrAjWgAxcaMiZaPh8fN4xAtsstqRvJEuOmxgk2b-HMK6SZtGjwPrfbKYhS_AO870-QWqlBMqFn9neY2aslndnrTlmQER4_6slIvyDnfN0mK2glcw61eJ5ZvQruf-AzHeJYLfL0cT7p4e15J2RumLhEbyGuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGgEm16p8HTipBefpW6HiJH38wJnHVezuS2KLmo9B3tCzCgs0SaLThFoq8puCYgQrqn-kF-ttwucGD_GDJAhJYFifo-nxF1FtfPT_adVyNaQYVw8dwM7vcLa5uKMOcLjR_1YWRfVJWSul4gbtciwVZ7lqyvUHVIOaRsTYIIzSloXFhz5hnk25HXxBiyrJSsZLFheG5MRrhsaCkpvYCyt-iRWu9KVUj1yXdD7XO7iyXB3bCc1AX-h2gB7meHALgPhtBIiKTMpYqX5ZWUO1BIiLtJjbREz8OYkZah6037iBT_pN3WrPqXLOOeubgQvUJukRHBu1_hXWjOa743PEyS4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-ROEaU9hJfHo6Mi39lkj0RsxtmxlsyX9TZhFXpqBsvIQj7jWiOilzJCL6rzkBmosTwwTsp9dxy9dV-IMpoOXYwjhZfIjtduLvEgVhHJrEnHR1AM4kYQOUyDcVkMucaKY-M0KgSfXeYwo7hFQVbfdceirUFyvRdfR3r4EvVrviTMfxAg4mqGRt60tWZErI1zoqnRxSAzbqQrzUmp2_aLXZfOmGIrqzm8lxJCUxC8Ah1FkpQbW2tgQ5jsjgGFukqIgfvvPW-6dR_Icvf5HQOpZOZcsYr0DUE7psCZ9o9RHg9q1zGX4n_LVvuKQKPRnCU1kKCjF_mHWImFpylFV1D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxuOi-iRHNK2hYvec_yOxonjXvsFg9cQWCmGyMWgz7ZwNqZ_LvTndQfisDsCR_SZy4itFIL54z1hUxicRgUvEQqpdcHOBYjfcf6qun7O7MW8ArlN7A4EiVbqWvCQRhpV_O_2xa8QfzCay5qdY7XIaHzFI0tJ-GDV72jZKp9i0tNPQcDFEpj93KxfeGYwBfm3cfN1oz4UCgoKJYNzRjec4DcH7a4b78uV9FAOWylwG8uF-ilV6AZNTB4ULMj7Fsw-5HFCkEJwAr5jhz-I_INy_r3xf4y9dFpkd-2Y0kCjnPSkY1Rsgj5zjnpYFOP3VA_PyPKtYZIlzOvdah8QGlQCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWTP5x2PZ5MPm1QZ7W2xZoyrqAAaaczL1pqrkkxii4zqcDut56F2Qj1jZ4LsumQcaVLjXAEw92NwcukbrxkBE6PblLOnTfkn3xl8dYFIPu3yILyg3UCItBOPYTH068gQ7jJZd5CxKBv99CVNsvBGe9zuahRoB6vERHVra-ShwVaL4rA0f02TNQ24CBJOvM9JltBFgTDShOblCEdsnHNX8kr_6ODHizU6sU_zrD7Ez-1t01qpjlrGIi73Yr3tmLfbRJ6YnYbpMWq4fM3dMcJbEcYqVwYv80toc2WIOd5fE_9kdtWVU5oos7unMtcR-orQKCvDxBJBQTjkWF3-K6-nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZ50GBxrOAub7attGb8wiUBPIyDX91D1cZaqW_JolU1kzQmvN1mtIyDNExCkK2IA38Fb7uBJvxfObmtONIYMLKyW42S91m4lM28WYTOK3obeaCz1p9oZBfuCfF6ekdWElC9pIUomZcnxcRyRxmv62ViPYBaT7bFA83rxuQ2CzvNYiOOGJveY1Ad9SwFOyr4cWkp1XPYz9jZ-9lyeZgTtN2v15O5pXSR8LMM_zzPHdrdWZ1E8KKwo07THTfRGnTGwlMtYXxIVwwqae0-iNufTYJCShRYHdJFoKGd0iWdNur4HJ1ZPLbqbDM2UM_5DxWaSRs27_QfMsKNrDlIujXx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUA1Krx_TXeOcPuThIbtGq7v26kmT7duuzuSpZyAYWq2UMi29ONOj4UkRvdXMy0wjGYblFPtUkShd16Ea8uRLpb1b_LIyLKGwoGz0WHJNmAHRhHBfe6SLd-_POyZbv-ZdDxHcl65hAnpbksHuwCKPpJedJ3fmOF1j2FwjJqmmF5YWngj3n3rt1rFU1q9eSU0vi1S8tU9Mad-ZxHnk68M7K5oLscvvHjj56rjwDCTT8Tx-HpNmgdiiJaF3LkilffRn5X_jdASTlxmQPii4Jzx4crr5ufZSUnBV_lm3HVZXM-V2BEakA6YG-KkCT7GMrjS56JwDGYGTcjO2aoEfQNuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6YAIKT-RPc988efvD5aLAJbVDROvoySyv46pg2QX_4dZXD36EWxxlwwrcbuwfkoloxqj5zhJgfX98MZTZ1Ob2V16WQV2mGmkCpYqiTqQ_vwp1iLX0Pfa8iG5IKXcjuGYzUttpmAWE22L8MwhZKylLCV7zmb53x0We5ZVSkV_RM4lMwuaYH5wAZxT3ldW5L5_zYLJ61t399KJX-NJSn1DmIhq11ENAQdNy1Mw7mbe868VbnnKOZQLjFMTGqKVFokQm18prl6HHhLBFPMOf1roFzjRahAyDYw2TjkPYmgihh_dDNg8A1Azvni4PC8VVDmley2bvPt83gGreLyoH0krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=sVRs8OXO1bIPmHIDtAF5l2ccWXt70eJ8_szac25X7rD70qZFfPwNIUDz-lttWLaSmPNVodG4pkFj97h6-VqntdMut7ehAYYXr38GmQv-yCKaWTCgh-dYVLDo63AtWXLv5I5UEWBso2S40Wbef3r34-koVPqGE-eqKWZgNqtea6YY_V-V6YbGBF36L3xroKg99PzpuE7DZArEUmxcpkOD7chIikH6-v-TO5F3DUhO70v4eaDbpwKQ8GUluVCClgMtSZvcZNdsq51Aqf78ByvFKSQ_FmOFTVl4-AE42gN1HjgzSc_71UrODDoS9z4yuqFFRX4QPBI4MRqyEjrSWE2fjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=sVRs8OXO1bIPmHIDtAF5l2ccWXt70eJ8_szac25X7rD70qZFfPwNIUDz-lttWLaSmPNVodG4pkFj97h6-VqntdMut7ehAYYXr38GmQv-yCKaWTCgh-dYVLDo63AtWXLv5I5UEWBso2S40Wbef3r34-koVPqGE-eqKWZgNqtea6YY_V-V6YbGBF36L3xroKg99PzpuE7DZArEUmxcpkOD7chIikH6-v-TO5F3DUhO70v4eaDbpwKQ8GUluVCClgMtSZvcZNdsq51Aqf78ByvFKSQ_FmOFTVl4-AE42gN1HjgzSc_71UrODDoS9z4yuqFFRX4QPBI4MRqyEjrSWE2fjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=E42LU-i9ZOpLB-GldP_lLMwFzyfkbLIKzV1OnhatGFd1gAzuqs_mauoTxQ1HuL6Kc3cmZbe6VOCPbUHvAs7BQeTHZpGo4K9mdH6fmU6iTKxwcweLDBosM8Bo9pTSYa5DS2FS9Yjn5lCxTwxQYeUjbX1oNqolmH4ExSZ6ZexZnJ7IPfqjNdmADgR1AT7JCEO-tuT65mrbKczu2UW2oIdOntkB5rj55WlCy6i8VhUaapV2ySOR93DlLVQktJpICRbRrRX-VBRjMg6TAM1A-3VaO86JV1opS-7rtsEhx0Jgeibu8yDhvYDMnBE50GWmXdmlTyvfVohADsUWmQU0qPqpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=E42LU-i9ZOpLB-GldP_lLMwFzyfkbLIKzV1OnhatGFd1gAzuqs_mauoTxQ1HuL6Kc3cmZbe6VOCPbUHvAs7BQeTHZpGo4K9mdH6fmU6iTKxwcweLDBosM8Bo9pTSYa5DS2FS9Yjn5lCxTwxQYeUjbX1oNqolmH4ExSZ6ZexZnJ7IPfqjNdmADgR1AT7JCEO-tuT65mrbKczu2UW2oIdOntkB5rj55WlCy6i8VhUaapV2ySOR93DlLVQktJpICRbRrRX-VBRjMg6TAM1A-3VaO86JV1opS-7rtsEhx0Jgeibu8yDhvYDMnBE50GWmXdmlTyvfVohADsUWmQU0qPqpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1c-5FYF0tnKzQFS3ZE9b7JwJLtl-o284VGw2D6PPEN-NvUwL5LdlJLPCRuu42SAkEl0B6hmP3Z0kK5e8TwUEfv9Trbtwqb13UoTaQDtov8pdf-M6QprAghANjzW5w39BolPHdj2kNllXTXBwmA0I4S5Y6qj4BNcLsFv8wVKabRBLygpGVbdP_y9_ccehLeNl71gXAobDvOzToc0uYnMLP4xTaRW950aDCd7Fs9Ew8nq85aXnVESNpBDV22UdOlpMkrId_ceYZEcI7OSfoKm5gEc-XbeCV46KuVBnpr9FUZOepk_VtVBAzaqRyDSrOpeOhkvqx9O0cKlw9C5JbPIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focP4ZvXg9pcI9YNkmkUREW_PthfwYalGfixxZAjvUK8i30dD1NK2pAwhfD1CLTcT0fQ6XvqUfAelGmWqVd7SzMvbiCx0kcgd8jSv-R2WBKI7ld5zXIvF6c3CXUA2hUORWvgx7j-M-GxN-4SaBjWSlm-3vzfom_sVwAR0_FJjPHWhIWv7UXvq01qBkZiPsC0Yu8lkXShecnmvQxSTfSuShIsYVrkVnhD3NdMKEY2cik2qa1CSr2WTpf0TO-Xvdpv8s8MV0QGw6AFqxuRs-hIoKcBhgxv2uY4nDpP2sbcV6meSyZNBFwTNiaBGBjNRKNqx4-9R293QrTPlHzQgANWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH8OZErzAFjZEFkdOTFsBbCd6Q32TP1yMma7_Y3YYEreCTYGRd7abgy8UhZAUCGX8eGR2LFrfwSBpS6lBVHgGSSZRpI1kjD__2vftaEVsqY_MUp3xjNg0aqtJkNm2Bjklm7o_wh77oUPfT9GnI8JVIz4E9gxmsX9DFdQ1HWn6U_xAFbRu3rtDNAleoUhf-ZOzzJsP1jnC4Fw7lIaEGwU8HFc7eCwo4NRBJr5wn_bCj-qDapVJ7Mf3dOozidVS5PIn-9uMJQN1cnFiuSpmZK2erElCtxKGh4HcPdv8UwDtgqVn35LlruHDMpn3mjIV-5DTKvu6sRWzXkFfsAa62qMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XseDqgTJgh5gFPsxX7MrNMs29h7iYIxcHASRltdS7bS6fh0nKyEukwawZfc08d3Uykvv-8VOiuOlv-BhM6eYmtPy94zHFHccYaKE_-CmgNEYt6ezaO1T2FaN2kyngavxOv1o9CvZbvRuIdCuDRRziozj4k-MfIh_WMeIthgexN_U3axWDGKKr-YaYW83a_Koz_Zzz8rwFCGPnWiFdWpBlmePUCI7nBE2nm_XYSnmvvD4omRoc41OxolZkzO-4aiU_zCuZlHP4bRrNH3BmIP8iOPcWzlLJ-ppxzj3wU4K5OZ2PyAaAanirrYsM8pm29utgg3-7ge7PrRG-rR6qP0L3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhM-ElbXC_S1Inm-jezDLMl9EpBRX-JmDCpEXr2_ch7RxkGNJ5GFqWscC_o2pMoqm2XB2a2OZLOnznRUfbSfYnQe6z-L1iiOUk3QKB_C2A1aSEqs8vs_aQpRk2dRlDMcHUkVFa1PlDL_gPvcskdSHt-ijP8lb2bMZXPzjYAp0BCKIHtmpVNrUog9FySNyNyoxyQDKK7rDDOcWrANiZ8-VfzVKo8Lghp565gTHT2j7GOBgLf6ZPSRj6zuAzlTJRaEQNGfwqTLQ-GUkfJGy0NpMxaa4aBVoElHN8OJJKwHYODaPkVcX1VxlOIsoYWtE3aAT89v7VCqatuMF9jj1DhIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvGWCx6dPjqUuT_DH_3KdwDolMhRS0YrnjYyiMJpcNFzHmXvnvVaVaKiaxclCWVkPBxwCXkkvHnvMAj5DlFmWWjP-AmZwM0IdKP8FSivnzWm1EeM66G5iJJwARRdXwZ-Rpsr6UEMIqnMufxGFDtuyulBV0PcT1j-VVtgWruRE0fmBP7EYLmzIP8OLH7k4THCPnpgS8KEEjnF0z0QEl4GO8m4zdAH0jlTnb1x0fnBtC3hSq-1K8P91cpY3YMDAroUg7-saGMHCBqKjOu6sUw-7mT0SMQ33yolQKUtbz3sr9cPfQUeZ9AimqrPd-kYS0qZjo6DVPFvZ7g9zVpfpCduDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2wwm5hFLgYAgPqc-e8dUPJiHUYf9Dy0S1DXMR0vOBliRvGW7IYZHw5UHoFKROAB8vh6HRjiES2siHj1MFPkYaPfsxNFXp5VEX1qrnx-WPAOxdkyt_-Oe6vjEHwHbnCQG_a9x17akp1gD79x7JVWM6T_MItoHc-W03c9wM3-HpoUIibQ4IOegtvIXPPauQWraFR0yMz77bRlizGIfiPLYgVkfRK7PjyJesEFrZ29SiimXs1fABfFhxOvxHY1pUvVNWmgkUgVXo1qMT8Mzl3kkvElsDkFTXOkqUxlyzalyHUzOj-yBkwD3f5df8KpfAJL4rrJTn7eHpf8dGIZ8yVeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNg0sJhmfBFz9gLBNqfeE8G-YfIpdXDka5pewccW0OjBpvOaLsORZrKpu5tGCXaUfpspPTLo0QLJ7mgvBgnPicz9D1ICp1p5FN5nbySYvmTEWLWXSA8YubdOykW_v2FDIMOI5X8lYKK37wYqvoKLsbX2xWo5LypkoTqOJt3ex9mwbFm-JyHWa0mghvtmuYl6W2jfaRPjKZyoWZY_3HrF9Q4JkhsBSQheNFhUEL1bEFoTPo3gOrDjGv4vXFPdOSfcCKUH-Sr58t_ZAlafAmrLu6Z7hALns_q_gsYdlRsrLmZhcsic7er5Cm684MR8a1AEBwMInt5aHms_sM2UxdsQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttDMoD01tYM5BGFQ8nVqa7DNfKqEJMxt6x58Wtr-g0GrpYAHM92lPmdU7LSY8kD3uyUO44iseIZqwQxij9TWc766YAcFzvOe8jYEpkNKN3g-XdqhZQsU259B7-nuKo3TKSV-uSfTPoDqIGFuPNM6XTYa7D1oJKY74W1Kr5Cqsp7NGFJVAwG2D9c0iAg6fJpGuhuT8LndpMZ6tPPhPoCOoZQunfioShJ12HxqpiWACsuKuMvQi94a59g-nLcvvRtt0G-50mjZKgI4--jRGtILe6_ZhgBp9_UApU5ZPiWqEj2xf9uo7eUQOgpuaNeus-EU6Tf2w_lQ3Q32p8s6J_UaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=eFYg3cGaQHXPno47vP4blkeZAJiMX7bFKunMCX1OZitp0uyqVNAwGidETFaax1W94FmDfWJJ_arDazKSDQJQ0VqTskE55X3huijx5JTOCbYWvqktBMxqIA5S2cnYyXqVT-sz7DLW36L2zG8zMC3Q9KI7txE7q3qWO8Imlz2ePA5H4y1s8PAyZgz04GTBtjkjsKgSPwdcXQGnFF93PPpR6QJH_rcLuOtXuXiaHDUwhPZrDgFSvUuhyXFxU9Oe_tXy-CLDLTvx_a0vgnEeMYrqAoMR4i0bTIj7znHlNHs4XFdKSaNbsow0UX1kkb6HDdUz1qdGa66JjKKWD_QOdfREDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=eFYg3cGaQHXPno47vP4blkeZAJiMX7bFKunMCX1OZitp0uyqVNAwGidETFaax1W94FmDfWJJ_arDazKSDQJQ0VqTskE55X3huijx5JTOCbYWvqktBMxqIA5S2cnYyXqVT-sz7DLW36L2zG8zMC3Q9KI7txE7q3qWO8Imlz2ePA5H4y1s8PAyZgz04GTBtjkjsKgSPwdcXQGnFF93PPpR6QJH_rcLuOtXuXiaHDUwhPZrDgFSvUuhyXFxU9Oe_tXy-CLDLTvx_a0vgnEeMYrqAoMR4i0bTIj7znHlNHs4XFdKSaNbsow0UX1kkb6HDdUz1qdGa66JjKKWD_QOdfREDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=U4ZIIWTr0pkaKCNFauXXqU9WCn9afEoMU5OKbV-31IiUNPKm3ue2bZjfGsroTB2NhPVBYbl10YaHT3aVRPHOxpnnSx6syeVNKhmhjgUOYR9vKu_yPVBRmgA8MPb_iZczVeqkoRp4Qm9o0LEtUxHquhSU-y0_7WqaJQaWc9RGELaj_MjbT9dGSZgsQX9qoNUDhJkWzjsco4se8e8e5ptU7ntJREZddPpqaCcwf5PXPqsaCUO9VVYCkcHpMUmB2CI7nz01_ANHvzCzNx6Vc0GxtOx6Sw7VO81A9EakTtCdwiJhys1xnexqJCCLv-mmN1mSaDnNEFtBF4UkrUr3R4_h6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=U4ZIIWTr0pkaKCNFauXXqU9WCn9afEoMU5OKbV-31IiUNPKm3ue2bZjfGsroTB2NhPVBYbl10YaHT3aVRPHOxpnnSx6syeVNKhmhjgUOYR9vKu_yPVBRmgA8MPb_iZczVeqkoRp4Qm9o0LEtUxHquhSU-y0_7WqaJQaWc9RGELaj_MjbT9dGSZgsQX9qoNUDhJkWzjsco4se8e8e5ptU7ntJREZddPpqaCcwf5PXPqsaCUO9VVYCkcHpMUmB2CI7nz01_ANHvzCzNx6Vc0GxtOx6Sw7VO81A9EakTtCdwiJhys1xnexqJCCLv-mmN1mSaDnNEFtBF4UkrUr3R4_h6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI1xUwAsCSZCkdsMIZvBbsWJ9vDOM6BWYl6g6gQ0_yAY-IgXNnC0X4DUDwgHwOUpLreupRgBHTIwUIJFLAP5JkK8fpIAAYYSQ4QnRWIQMyGZt70hZPAHIb1c5KcIqozD_TeIlxQKv4YmBiHhqRhYyikrDQFlzWBDKCD-g8oqzGGX-qNLfCjZRYhPFf0F4Eq3s-KA8OEVuLgwp3dX0TK8YMpC2jMsWUjZ-8Lr-eTf-wYmAUnekziV08xD7aclC1FRkLAXuVPUYBiwzcU-MN1m0ISv3a5uTaoTSHEtYMKH_EcLmhaw-eQkw_Oq7rQzVfSKKaFYscvV_-lJHUNuBdpxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=sIBFzXRf5RypSOVvRHCFLffEO3i1Ph9qiR26WTr0-GX2kXUs5ENqnJkbM1pwGvUzQfGwewfPYhyGj9rP_wkpa1ctbGQmWlMt6am_uSP697UyuN9Hv4nE2xq2TrrBX0Do-JJql-1KOhuS4SpjJi2XtP8bjQRRriFUL0Va5ufE37QeuAwTThXXHSceM3aFyGto6QF80gnJ_4IMmSCwNB6dRuC-Cw76-HWY0h54Wia33T6WSETznDb_wgqm66NcvdVYFuz2BZdk_NnSsmGokap1BZvwnD7P7FeJG5M2areEaonB82LVigJkJX7z3eG-u9U4ORdbMfN2heHfhB7bqy0mGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=sIBFzXRf5RypSOVvRHCFLffEO3i1Ph9qiR26WTr0-GX2kXUs5ENqnJkbM1pwGvUzQfGwewfPYhyGj9rP_wkpa1ctbGQmWlMt6am_uSP697UyuN9Hv4nE2xq2TrrBX0Do-JJql-1KOhuS4SpjJi2XtP8bjQRRriFUL0Va5ufE37QeuAwTThXXHSceM3aFyGto6QF80gnJ_4IMmSCwNB6dRuC-Cw76-HWY0h54Wia33T6WSETznDb_wgqm66NcvdVYFuz2BZdk_NnSsmGokap1BZvwnD7P7FeJG5M2areEaonB82LVigJkJX7z3eG-u9U4ORdbMfN2heHfhB7bqy0mGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGffKprdMZDV6DgDmATIeoiAZ9jh-sSqwkTNI-HjIgPTrBmnW8vfP2mH1iYoSXnaDR2DSRF0Cd4Hj2MABkHm5hP_m_3PclnNNg8qZKCgXT86oSemphUTs6RTSo2eSNR8uqwGK6ujCy47ySyT-TWI1-k9T374somryyVx33rVF9hFgNQwjqsU98owxkdj9DIQvnas9lh527EXuAfWhHmCapXaF4QMaUWLCfzKGhNwAoiB06z9wgZZQoCSPt2DDiVgmo38t7rYPQ_duMG7iEN9H0ireSL6XveB9jSKGYrdTFEFkr5_UFGw5mUVcR_t4Xq737la20HJUYfmlbVNodi7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=K-eiZSQhjXlNqtnqYqQsNr506MEwVk6NGcosNAUhKrjiWHY8K6mjIgdVpVW79BP8EDZLsO8yUUVrpx_nzR7fbqm6KZX4wGDwJ_84W-CaAIeWa8QEEqpiYNh9uaCvLnt49EtWqMM8xwl1615aokggWlayrg9WrJ8TAvsMe4LCDPGZJRy4NereoMaKwstWkgbd0MZ-1wtZhJQHrpRCcOTOntiJyLEliwPJ92IbrxOTwXw1FZB1Fvxr20CyIZqqJ1n9b0VpZ5HeYQfR-dLEBP0V1rwE4k6YaadO7SjvtQFwosHbrzrfoRK-TLcmag1JO7jydaBkwzLwXeCWcYDO9uUn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=K-eiZSQhjXlNqtnqYqQsNr506MEwVk6NGcosNAUhKrjiWHY8K6mjIgdVpVW79BP8EDZLsO8yUUVrpx_nzR7fbqm6KZX4wGDwJ_84W-CaAIeWa8QEEqpiYNh9uaCvLnt49EtWqMM8xwl1615aokggWlayrg9WrJ8TAvsMe4LCDPGZJRy4NereoMaKwstWkgbd0MZ-1wtZhJQHrpRCcOTOntiJyLEliwPJ92IbrxOTwXw1FZB1Fvxr20CyIZqqJ1n9b0VpZ5HeYQfR-dLEBP0V1rwE4k6YaadO7SjvtQFwosHbrzrfoRK-TLcmag1JO7jydaBkwzLwXeCWcYDO9uUn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=gBWj8rGvFLpLlnbEkNGgSvyzKf0uG9kQ5FCVkglKmXnrd989kKiITV39L2npx0KVLZLaVe2MU69r829mX5A4Z9IwE1PPYOpnl9KydzvmJT7E2ZezrWXHVzr1D_ZIpZUglBaeLdCMMLEnmKsiaNo7MtpxG1Gyr2G-2xGa_dWrgpcVkbNkSjnFQQLpu5-Qxro9lWpNHXxZVr1AeKtcrVqYf9bsnp0qzsbXrAH7kdfc2y1rTaHvwdYgUAbzXtHnYBPySaQx2Y0gblJlQ4Y5iPKpl48WCo0-RXzgctWzzJJoN7nuKMuYjX6fJwpNFYSIzvDvduZrflQA9ApKbt-LwG-u1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=gBWj8rGvFLpLlnbEkNGgSvyzKf0uG9kQ5FCVkglKmXnrd989kKiITV39L2npx0KVLZLaVe2MU69r829mX5A4Z9IwE1PPYOpnl9KydzvmJT7E2ZezrWXHVzr1D_ZIpZUglBaeLdCMMLEnmKsiaNo7MtpxG1Gyr2G-2xGa_dWrgpcVkbNkSjnFQQLpu5-Qxro9lWpNHXxZVr1AeKtcrVqYf9bsnp0qzsbXrAH7kdfc2y1rTaHvwdYgUAbzXtHnYBPySaQx2Y0gblJlQ4Y5iPKpl48WCo0-RXzgctWzzJJoN7nuKMuYjX6fJwpNFYSIzvDvduZrflQA9ApKbt-LwG-u1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDrrxkg_8HitetcU2FZoQ8zFr-qOeXNxCc-ZYEaBv6E10UL4LkfryERo6ujHFTuCx_F5ahb9qEycR7MKWC8-DxtN-aXMQkeutFEzm1o5KDon2dCcEIZw2YNUkUYKaQ_0ZKtRnRPQ4iS6nXQ5PmWQg5EMa0Oa5IkCh70-6JWUfO3AAxckhSu8i0Vlg0yhVxMImP9QprnUPf3Avi6J4k6JYFubVu4ooFIN-rYgK0vdWg9sgOcW5ALxne35tXfb47QC42AP3m66cJbiaXu8gkh994TGjPYFPkYflimONCxi51FL5t7msFJXZ07_oScN-pNMTAZj4bUOhuzeWeUuDIPrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXUUtwf5_4ReHkUHZ_DC_EbzvFvTobBbiawOU2iEpEtIesTerFUp3OpCwVsvSBsoLo7MKwiSrfcwtxFH4zSgBY0U9DHHMf0kV44M7PZUJmiO-RSiqRenncVUrxGhvjdDd7wOlaX_NYAsKTZx6yTtS0TSH8Ht_YvNrLa8r2npnbU-r4az5B5V6FDbLNqq9KQGtsh0fAonNPdKa99H5goQPeAiO0NmWbe6dpBFIcMnYrIMdxMfzhvbwvYzGZ_IH7EWhGN7dwMWr8K6qqsGTXx7Ao6UAU4BG9a2GNPq9K0agzxH7dgb6yukC5Yw1ivP1Tj5lXo92G5PpKD87Dg7Llesaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNGD5KCuVDcXKyuNmIRShmajx09xdgLDBu055RKYp5RAVY1W6t-anGFIO0XDvzdCkmSZATvMKRmOh066W8Epz3Riw7YOkABDzthUGLIpFS34Ak5EWhyCBpUnnQ5XAbFe1O_skjYB9YWRYhNgD5RWglQsmsvGYhkJ0KCxv7lnZL_vOy6LSXgq5ZWy6VG3eyCBDDQ1TVXD_Db7Iedc-7XRJs4V50LW5LpNjI1VOu23065npx-suBM4jpVngt_TAXHb-J3Enl234wPtlOqZZJdyihkbSOeSMDcoYQ3rFm9BrenAkoZ_rMQA47oJu2Qq-JqDw2yGuLOQJLTHRFmGxp_Egg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4o1NU4Px5I_K1K5Tl8LtFga0JZxu4XYs3AmFHUXPWLit3wdJuYNY3zaE1FONBeNmeqi9ttpb5QpB_QXLKkrJHH9e15tviy5JQPhzr7jFC6JRpZ0SMI5c1Wuofwi7PwqHbOhfYO7wgt0d2PAGOsn-nRP-4IdrVzkOAI3lWz7VXmUlzbgXhn4cFDNeSAGMhA_QNabGqtQlYQNpffVi_kXOM1h7vf72EEMtUT5dR74zxfKTWfUDeuO1npjzVwNJPi8cK5LTCkbb6QH2NIQb35RuHtynQ8HShMgo4nEzr6sb7pIi-x29kMS0JTDNP1-8QMnJnMQLKD58PcjOeJNKMG1Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCKKXT2ATu2isTsRL0rzNJoGO-TGFY-dGk4vRWb4cksj-OOPO1_Woz09brwNUqvXGafqOcssZdDaakI0egaRAjEfYZW4P7c0EFdja1JpTKtmVWYymmiNIzv25cbki8NovIpq9e3hzlqGON_cXC1Ml-zJF4RnmH7c7I4hrrRvLkwcTnBi494_dsH83MW1ZQKxNtIscjCZiGNvGKj_znW0WXtHkdXIIg4p6AvxKqCkJTHBuwFSTxriOrahbcs6qS_FHZY7aBfvN42AXtGfw4vW58trz2tTzM6ww5sT45SdW5Xvrhi6M8mbY1AE7_aGH9_HlmO8UMDAH2iPFySeeVYwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3E1MHEfcyTDjHQEkgXwBfXVZlOjPIHYLutRs0j-QCmQ0niLo0-r2CTqwAyZYrjRqFpzXCI2Yi-YWSeGozx_wcurt08izv99SPRLLkwYifmIeTlVjSTXRfyHZoj9G__21tPXeAI1HyioEijefoVq37jQ1NWaJpnGc5RDDRMGYlfgwD0N8IRtCpFTe8F-TORNAuQ0Ko_SNKimtNkyN3Z5yzkbBqumB4Z85kh7xuJjsYkEAQDIhRh0K1QuopE3TxolNssXA4HbDs7xhMB6V1xgsdRfV8seyuPqxvWjp8fddsN7GnH6PAGFi9jpKAOcPRlMkw9Nst-Z7zIroLp-0nCfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=tNLWuSRSjmWWtmoD3i5XcN7dgwoxlXm-yslYDZNPpEc15ZAIvrYQukWQVDspsQTXdbT1jSShbgKxJ3AMMbNUuZODC0pCyfcS64Zb2ovzKn53Kplo53Ad4XPtXmN3Rsy4C1lBPcANpskxHQdeJxoJtG-DnUhLM4IY21Swz2V59p_T_tt6AyP4lyZhb4QjvNMYk3pDz4UdfXffRy_QuSSuCfJrP0QO3kjXywtZA-jTRfu9AfaF4Xj9CBdXFYQuhwEBqhneEaDzBGNVFQ6GBipjmTiDrtETsmzLvsmcrMzO74lcYj_pvk35FlBV6BthtGckiCgKAS-lWPyE19lKZYdp2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=tNLWuSRSjmWWtmoD3i5XcN7dgwoxlXm-yslYDZNPpEc15ZAIvrYQukWQVDspsQTXdbT1jSShbgKxJ3AMMbNUuZODC0pCyfcS64Zb2ovzKn53Kplo53Ad4XPtXmN3Rsy4C1lBPcANpskxHQdeJxoJtG-DnUhLM4IY21Swz2V59p_T_tt6AyP4lyZhb4QjvNMYk3pDz4UdfXffRy_QuSSuCfJrP0QO3kjXywtZA-jTRfu9AfaF4Xj9CBdXFYQuhwEBqhneEaDzBGNVFQ6GBipjmTiDrtETsmzLvsmcrMzO74lcYj_pvk35FlBV6BthtGckiCgKAS-lWPyE19lKZYdp2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuLhXPb4H18BDkdVpuG3JknHc4oe8QPsmuC0bas1SMDpEGHF7iGs5WJ-KdlD9B_z2ejd7HUuf8p1ro84abj6c6GkvgSvLfKqQf6EpI7m_IGwktG-dYHKhAhQRoUjkxlJqxnQKjak-QGHWY_IUl5-b7pRZJbhqp98B_58d4i3di9-owZcYgEcZ4UVtb775T6Y8gZQ6xsh8dZ0_L8eZOlSUWv484rSxJoJC3m92LF8CAPbvc3Ti7KD-020lDLl2uhSPsyTL9nEAuzC1z9Hn-zp77vgAX5aRTp6g6KIGr3bMqvshMd-ZrxP1Qg7RZ5UYXp2YNmk6B0csfEV-uGshStheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGXiOF1JaNKbkYr0HprfeoZ1_STl8G-ibvdm6jMGBaUUuYD6yDXjccFQA9FKjVfl45e3b_KwpPCYtFVfgzjUGlWVAX0L3Omsx1UP4P_p6oOtboV-j3Vsu9O5ubBttW54pLCK1WSCaeRHR-P5dQzf5aoeVdFvfTP2rmr-kqtsaDFdmZTWPgZ_YboCPSffCDwKkSgDXNk2YTV8KkDN3kgMMYphh4gHX2NxB7QSBTN2w8kD4PJdKaZThG7CkMPROE4Oeda2qgU7xM9RfgL4KBKnp2MiCj7xhGVgICXLHW-CjnWsbIX5AAny7QTTSEQBidnTMovuJK5WueWvIDZrwtY3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIwZWq0sdihjnpNqrYYF7jDhrNs9xvapzdP9AgUARdxBcmSTld1G0NGalUKyCVYKxFVBUn_wKYQJ6BtjOOJ7fCoHGLzEB0U8vg8TEE8OCggK-3XOe6EqdBbw88GUAX9W-nyt3Icr1fhoHmuEXUcLWP9Hd4nRSJhntf5yffKa1hK8-LNK_CLQMyMYSBNZXNzzNI29lSwQ4JBFXL7Z02CysOStibBPmqJU8JVDdw5dxgYm5Mk_XKEMDjGQyuFQWMfWmphPLTlJUZChH8-2sUJhZNibNoixXE7_RywrjZ3RWp8g_kSBcsYaPHNkbXn6DoHD6OZPWZRlArHmT2ZZwmvnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=kWP5JqKFg9tU8LXJEpSuppWBwsSe8aFh-sL6w0YossIuCtZVXC9DvMjxEB08lAMdRN8Zt6tb3XfJpErzMMx79ATJGNiogQJWkytRnAxoWeyFksJjd4fB375xZ-Hx5CQF1IiAcycmPLW3cLNuWXlvJz7tkJJC77pyVCLlbgZuVGF-VjiMJL2DX5w-vIOhntiL9LCowRVm3bIAE1pi6TILvQUS3Ef3qdt1Ka3w81LbTYLdo178qBB1FEanDi6rEjJQdfDR-CXS7oxBVokS0n5YYLAl1uQaY-a3BSgQsRAU3tZl6yT_Lear22F586UhSKTe7WjOq0sPGdEuOOhqqpw9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=kWP5JqKFg9tU8LXJEpSuppWBwsSe8aFh-sL6w0YossIuCtZVXC9DvMjxEB08lAMdRN8Zt6tb3XfJpErzMMx79ATJGNiogQJWkytRnAxoWeyFksJjd4fB375xZ-Hx5CQF1IiAcycmPLW3cLNuWXlvJz7tkJJC77pyVCLlbgZuVGF-VjiMJL2DX5w-vIOhntiL9LCowRVm3bIAE1pi6TILvQUS3Ef3qdt1Ka3w81LbTYLdo178qBB1FEanDi6rEjJQdfDR-CXS7oxBVokS0n5YYLAl1uQaY-a3BSgQsRAU3tZl6yT_Lear22F586UhSKTe7WjOq0sPGdEuOOhqqpw9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEeQKnjCwumLSTyKY784Rge0EHwDzDz--TOIDeEKzqaW0vIqQhuebNG50ejoyD4OnOc8BaqqbDaJ-GebH6iLFdvBCKrvi0044eyUyT4a1IFdGpwzYuNZiY-NYTrjiWtjUhWs8nopC_EzkSULA19Q1Wo2rHDG0VzffR6bjCKVWrfjLpnprmltX3c93S5HWAjglsuM46Fcnr6GsyD2D5WfwmtpkEJjYSx9pSGNFWDSg4dIcSiJql-2e5OXPuBB9ViqJTB2dSBz1-TPTRAK9cQAFPRaWeFX701KWyr6al4UAsT9FCpWAf0HngAayEwqJK9IxOFiImrK7Q2guFCb0335Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dkROOgoo26nsXDGA-Wq-B2XWzJMTQ2rtWKBTAu7wkK17fAN-X4JwZJEI9x20Wa47D6sSZueHZhFeezhwVtGe7iUdVb71mxOf6WyPQlqFYYBH6zDZa4mv5vyegO19Gub7Z3Vk7D793phYoOtNlT-v0S3Lup4nrWVKM6ZzUvgnoC1JusPhLvXb-Phb7yviu87EiBe-uLIH8fYT2Kbp8bE4cB3Ms7p4OTOQpf1j4jPzwDZ5woZx5jF6-lwhs6IJ0EwDEkDmJYJyanlTOY4mxQBjS4JiOnPdZ_LBycXX65FJxx92mPqmDU4uS7WKnKhueT7kramnjVXWdXn7T2vYdQuxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dkROOgoo26nsXDGA-Wq-B2XWzJMTQ2rtWKBTAu7wkK17fAN-X4JwZJEI9x20Wa47D6sSZueHZhFeezhwVtGe7iUdVb71mxOf6WyPQlqFYYBH6zDZa4mv5vyegO19Gub7Z3Vk7D793phYoOtNlT-v0S3Lup4nrWVKM6ZzUvgnoC1JusPhLvXb-Phb7yviu87EiBe-uLIH8fYT2Kbp8bE4cB3Ms7p4OTOQpf1j4jPzwDZ5woZx5jF6-lwhs6IJ0EwDEkDmJYJyanlTOY4mxQBjS4JiOnPdZ_LBycXX65FJxx92mPqmDU4uS7WKnKhueT7kramnjVXWdXn7T2vYdQuxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTvsshOnSzcZmoWUzdVk_J828MO-G5aCoxWRcVibYo_uIDmOSPv9O1f2x2HWyNPgWuCQ4WytPlI0y0gSgE0tpY1uCL3VnrVVVZym50lISv0f6Nc5Ljxn49Sn4s591sLxPe3v51sFPbXqG-EHGsjPuot95MSfwSGDu0X5ieK6fpGMVCX6mtWegeOZJUmJ-QaPlDGKf8e-kXx3jZXL_p6Qdgv4timR0lkUPQ-Bz_DouVaI6gA4MViiJX-xvs_WwQBUYXnFINt_lvLlIgYU2oVa892Phk5WyZ-TTr6oIbbaz7mR3mzLbrXp-G-oI5HsdR2Ngz0aszug7_njkjKIoChyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6366qoyNynrM9fAP16Iqvslx0TvqrJkwSXA_qYev4dN7MQmVKF7clOvljkm5D63-pYAeJOPCHS_h--uinJwl2RrZY8wFHk-38mIQsR-Hx7nVubSzJ7KNk1_6poRFY8J70MNjNfZVr1d6mEpAHDUfclU_ugR9HVIEpO5M8aRlGpuv5wFmKln0t7rDwT4ZHhjHhp_3G9ltHp6xV_MTng0a-PscrQv6B0o7fV19XS60e-8KJB684I2s58v9ejBNZaggzUEvs4Nm_agRFCEGA6g-6Yq8Fqmo8h4fbBuhrS3JtCrSyrjP8Hr-hduYFk9DEc64vhUUzDjNEtXrPBHfg_1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXRCc_JT_twdmYKQMvqg77mCrhPAO1d-iH5CQD3qyogwCszoygvFHQLVzdaWHvjRLK937padwhkaZmBYH_latxLjnIXgbxFPuYiyE4nlDj8QuF-6Yp5URS-CE6gEUlK-8keO4R4au6OlfOXIYQlF5e2NxVlQCzGv9SU57BWfekfXmW4i_owdZukdvjb8lPOSperkLBxOvxCBwvjoXS0x11U99hNxSFWgdHOcB_PBHXQhAWY0OlnBrwjt8I_H5GLXn3EreLeZPHh_A-xmG6m9DTm0vsGULS7qyWQfOIARbjFeCk4dtSv4xH5yc8JF8ZrfP45KTrZmq1v8yCk1Jw8qXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNMli1O1bmtrfx2tFEx5SWXMR10SgCgUwJLM3YfANNwUi4XEdWitH1OsO1ZxS0v4tCpppBd_XhJdHlfs3oT5hMXhx_67zoWP2L_C6x2y2Q_kRDJxIMB4mpXZZM-KwG0scxiOuc5uAs1lgOq5kGfi7G61kfnwL22vmr7vuj2Uyxk9A9UOs5tsfVWNtgT7gGJ-3xqZGhuJNm6r1q2g5X9fpmCh48eNKkuxzWkgovEJXMbjChMh_LAVgQ6XrDJSo-0OrkyBFPMq5vMBmqw5lcElGu0UnruyhufMpoSWBzB8-VCylRxcAepqQP5qYXhzVa1xdbOMoNtE5cGEylKp-PYAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbobicUAPjkaqLBUB6rPp4cdBWL2yz9xb21at275zHgt8EayvXD13FmZa-XvM22gqPml7nDGe0JDH6AZgHH4mtr_dXJkyT_ACXjmpCueCJpQ9e33PDegXeO0FC9xouh7XmPGJrWYsDETrq1m2_o7seBRR224xSeN5guu20PDDfxEw6b8o6soEaJu6YtLbGBVpx33ikZDjTevEQNc93twyIl4pdiYeNwrrBumI8Mm5AiqHdfT32YoQ20wDuQIypyjC8Y5trlQYgOUyqcif2-AN2AjFS2BxIJGI4wGMUHz2x9OEDxISHresbiMEG96a3BKV8mm8574PLGLSWQgy3O-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=OujKrCCAjpPPo0-dsdEzAMQiQyxdNlVCf-kv_-sntwWTDUZZIQDygKf9lgE5w_mvQck9tZdZ2cnN18hVjt7qSQukHDaUNV7nvFRFxBEc8lT6nDRj0PqLkl_RmWNUxNtQggWJdU5u4MqaS1vV3-39zEiafNR_fLLod1c_JenBdL5DtCVT4iDxzZMBmsv7nY9mX6nnuLSMQR6vpjYJudp7Zkt9qPVgNiAKnNaCZ7MQ4_N-l-8tuTbJI0p4Kr1B42CBdP9lp7G7OBZI-UbhYpUt5y5U8NyKoAkWsxSCVcex8-MGy-LlDqqzCyS8a_t83uTmMkjV67kTOgMZe9_0r7JQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=OujKrCCAjpPPo0-dsdEzAMQiQyxdNlVCf-kv_-sntwWTDUZZIQDygKf9lgE5w_mvQck9tZdZ2cnN18hVjt7qSQukHDaUNV7nvFRFxBEc8lT6nDRj0PqLkl_RmWNUxNtQggWJdU5u4MqaS1vV3-39zEiafNR_fLLod1c_JenBdL5DtCVT4iDxzZMBmsv7nY9mX6nnuLSMQR6vpjYJudp7Zkt9qPVgNiAKnNaCZ7MQ4_N-l-8tuTbJI0p4Kr1B42CBdP9lp7G7OBZI-UbhYpUt5y5U8NyKoAkWsxSCVcex8-MGy-LlDqqzCyS8a_t83uTmMkjV67kTOgMZe9_0r7JQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCUSzFtBm8Bg_IJP4O0uw5rUGxdMa5_H1HclFhuk4x9q_coGkS_kpV0puRkcSSAN7KVtrbW8VNc8gvsxuYRdeDnWMSVbfJ1UaZd_hRnwRoxzo_hmu02evRCAAEIWYnVRjw1bC4RRIhiYlxLm-9G5q0Clyuh1pD_2YRmcCrkysZX2bUdruvLgbJz-vzzwtX5QdmVLbkzBLFVwLEfE9nWheEuU7iJ9cQiVqa7tfn5CND6-sYMf80KD0OTDm8hNSvi6Ajp0Wm-lUAxJ-ObJdlm1yhgj9CYqeyYxad-TpdA2WbP5EW1HPsRhAzEjkNS6f8Iy4dc0aFsOR01ihtnsbeybbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=bY_xYsOxeZ8W8ner1yv0hXQzcr0sfMZpJIKu0hFbmrzLOY4zD_NmO7_pZku3jkHFaA8su4dooVme99JIKdb6pDr5XhGbp8NGOM3EZkUrkj2sRORQYuTK0ALtWlmZRlhWEMEEgjt5LqotlDmVE_wE5g6No9tsd-N8105yQiyrti4oE_4GHDI51T5WKZRTHG7nUpwvJyPfp3fZ0KDqDWPc3r1Ml-G0YV3_oj6r59D25eAXuoBfN4PTgbc0a9mF2IdZFlstt0o5Ux87ffMoVHgsRGBryBgxT0z06EC8f2sZyvN_0IKgQ6IG6zvTK9BBTMIG3f-hE0WqbXEe7WTnILyWLZLEnCCLAXMb28LKWA7bKrK7nhHoubXO9ImLqDbiTTThNcl3i2dwNQppwobn1dQvtE-eT3TCvNXB0EacyZNH3wGWTvH6WZLclBclq07DjESeT-q_WrI7nrVucm7Oc3llpSPSrtXE4riZqdDB5SbWqGoMeCkdq0ChAyAiGjNv69Y8a_lbE4NYOaf31JLamznAonbSyFsttD-wCeaVf5Y0iyjfGw7uT2qzH-VUX-pIz_40T82ASCrNARzsytvS_rPMrZtygcwxPmB0dLUeFv9Jm5CZJxjh0wIz4X2Pbrl1MoSXzGQ5vx-HHITaEQiD2QQECg7MHwmjOgkdc5VTWX_0yio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=bY_xYsOxeZ8W8ner1yv0hXQzcr0sfMZpJIKu0hFbmrzLOY4zD_NmO7_pZku3jkHFaA8su4dooVme99JIKdb6pDr5XhGbp8NGOM3EZkUrkj2sRORQYuTK0ALtWlmZRlhWEMEEgjt5LqotlDmVE_wE5g6No9tsd-N8105yQiyrti4oE_4GHDI51T5WKZRTHG7nUpwvJyPfp3fZ0KDqDWPc3r1Ml-G0YV3_oj6r59D25eAXuoBfN4PTgbc0a9mF2IdZFlstt0o5Ux87ffMoVHgsRGBryBgxT0z06EC8f2sZyvN_0IKgQ6IG6zvTK9BBTMIG3f-hE0WqbXEe7WTnILyWLZLEnCCLAXMb28LKWA7bKrK7nhHoubXO9ImLqDbiTTThNcl3i2dwNQppwobn1dQvtE-eT3TCvNXB0EacyZNH3wGWTvH6WZLclBclq07DjESeT-q_WrI7nrVucm7Oc3llpSPSrtXE4riZqdDB5SbWqGoMeCkdq0ChAyAiGjNv69Y8a_lbE4NYOaf31JLamznAonbSyFsttD-wCeaVf5Y0iyjfGw7uT2qzH-VUX-pIz_40T82ASCrNARzsytvS_rPMrZtygcwxPmB0dLUeFv9Jm5CZJxjh0wIz4X2Pbrl1MoSXzGQ5vx-HHITaEQiD2QQECg7MHwmjOgkdc5VTWX_0yio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDfG-LL7h9uPvTgjKBqM_QTPcA-S7QNTJDs0IICeKBxxq-sub0FYaW31nyxgc9bwjr96pgbUYWdpIoHGIrzk7t8S375D2phVa7fufs0eMWoY93WnTRbAXEfu22ajI7xXrZr8RnUrstVkFK9NMlo1EwS3CTQSNy28EC9BjiUZLpNepo03t2A2GiX6UwzzOpgl_tqyRxUtvfEL-kRBeJiW64o2fMlrqXazldbibIG7V8zUG5w_oJY9lDm5BthjRig3O6KYt4rlLuf3-axXrXXMpeySDYQoxKqK1XWfapD8i5sxLShs0BLDSLDvQOuRlllEwYYYhREhiW-0fwQICLcaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llT_Wmx4RTAfhidn-kTxVPyL3bQRuIQzhFRTFHiNMcvz9SYQEgpmO0QGD4TZb5BOhOEO-E3sn7ijA73GjBLMFIQ0DKTzEtYnUcbzjKs5KhV--JSrWUQPuPBxbx6y7rRwBzyZq2YPWHAsfgKpeGkt4MLtVZKr85G76mDSdZKMRjupvw7PgGtCvbLfUm11pf-Q6ognZWCgT1Zctb22nu7w2qSFpQ5KXXn3Yjqc-3RE7VOK1P65beWDRA1GqZQIZ6XJiA_0Uzwsum9T7_ur48RiMK7skFRN1vYHRvRtmeje3_v1AMIp0st3dlqsZQpoxd0cu_hTU6bmorSFWKOZayWzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYIkq0OSxpYQq5jmnKom9sIKr-DYdaxk3fK74ESzXcbkWPHHf6EofN2xObV5W7XOY4l0U45LZ2Rz-4ZysTFjZUjgDKG1g1pKDGM7LM5ZNw4b3aJbNRBrk_j-5AWMPTXe-YDNikAORVfXLSjfqKpYwG2_BGey5gu2wRupCtcJjkIGxgsM4TNoofQH8BX8EChcc42K3u9_zOgBQFyY93GpCRYS07_tyMkhz5FPTgfCru_mE8mR17h_xuxCCOOz5Lszx5x6baQCRuRgIqBTZpI2ukpeKS3_86Jak7DlWGEyuaz_oA6-02f16npGkXcYRjjPUvkqd4woIMY0-93jmb33Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3rN7H2WBp1UespACarw-RFALbzOlvqzXseohh1dM1-CUa_xkDFMuHhV75X0BnuZrdRLCuELZsY-V3XMIQhTeZTbX6phmkKASNjquYpDNiSQreG745wUAF--sOUEytLIA2sefD-nM3pliwBmkpJerMyXhtYEMCcnV1-jucPgOO0mfug5GQ4M5gaKFnnxI8069L9h_1KIWyBvIsp6mbt8RgQhB9URv2aNrJDShgDuIgJsEGuabjusQ-7tcA3t-xME13FBPt_E5pQLNEMWQ78vejWv9M06UqQuHlhwbVqf2k0HIQuJhwGEJ8-qaD6AHoJScaOX6jUcRIwJPXvb_XMPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wap7wrHncA4hXoZ03P7veKgJPxeiWPwrXbZ_knP4EIkyhsOKxPDl63rCQ1f8flC11LP-V9SWro6-s9n3t1-FjCHx09lhms4pB7UW3ms0AjFpTjlIhp-lTK4MDuBecRkWrL1BaErbHnlJLwVYxT-D5wS1NnvaN9G7nSSbyWbMlTL6hUtMOP5TcdjL_GWLZXAW4m6J_tmV-awGDtDi5X-JXwjOtiZ-jzgj0-xmIqP3Um0BCnUaBK1zMw2P5oIuRmFjsrA7KoBDfNWlAaFmA8s_k6oE-lSBnNZvlDlBcQ9tcZPjF0IYnG_HGsXmmgCxFiaAcbVrk6iC79tBv8QU3nAJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6Sk0Kd568fNKepatZ1_WfWpNJwUp45Qx1gwV16-P6OqZs6cBezKA4yQ0mtNk3Ls9m604xKg7kkc71PTGb0arrcMDlgNuk5A5WEv_9_8NB_WOxP9-Ky1_Z1SDZJ_QUaeWfW4EjO82GxcuRpmXLh0tPt0wf_JuYX_v8KHcbxfseitYuvSOI5XZbmhINYNqVXk7LeZ3e-PVe7fIKkpzLsCBlF5TJWl5WKvlty8KYzq4vcubfcCWbN9cy9EfMkIWhaz8Ouk3EJGfv_ZeNSLOf1Hl7WvrywuuJ4mb1aN5xsdKT6F0-U692lBykfSyEegVqgHa-5k87wdVv0zobx-T2skhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8Fh1Q_N-m01mHG4zqhTNOmzhZApi_G219W-UEe6TW57XIZseebJXCODribAuUquauzTCvDVaJ7OeA82wEvZQYYelwYJz40u6YN61V_xhLa8iF3VMKIRg7NrxmL946am2lO0hPGguvP_Ok_apaN_1kijNnkuGz5ROBCowtRVOpz3UqsUsZYCLclvwEqs7j3IaWtJZcHRBsVngbmPc9chbjbFYmWPfZ_BJsc2ApyfyWidRJMKpMqzHkxnnKzAPsTUdxw0sPtRMwQHM8sNqX97sj-I-AMBO-ZLdJoTOKGNVXoAR2iWaazV0qjJF852xcAOLoERdMgztYbSImz8rZ8Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=Fy4oCGsA26B2Zed6iGeO4kL8NooNF-b6evl_-GY0FF_isa163WCWxsdkKbZW2vd007JZReAhnTjYkpHzALKKOmCmA-ZG6gQz7QdtIUOAYi57-wAKjKBVto5jFkY0eWwiGhiNHCTjqi3kUdefepmoV1oX_zQuhxsimhaXYQZg4m7KnX8ZviyMQ85rvkTIxD9Rnra_019rwNSJkE0Oz5NiiAyRpegnuLjVfG0UpMzyshlxIGZijRAY9PY8QQvIWkVsVD8c3JMWWGoDeMq__vLevKDQh_5PglzJ8ntrYakiX_ZgOpresVc7Kto5yL0rMszNmlgFtPrIjomcgADH9VgY1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=Fy4oCGsA26B2Zed6iGeO4kL8NooNF-b6evl_-GY0FF_isa163WCWxsdkKbZW2vd007JZReAhnTjYkpHzALKKOmCmA-ZG6gQz7QdtIUOAYi57-wAKjKBVto5jFkY0eWwiGhiNHCTjqi3kUdefepmoV1oX_zQuhxsimhaXYQZg4m7KnX8ZviyMQ85rvkTIxD9Rnra_019rwNSJkE0Oz5NiiAyRpegnuLjVfG0UpMzyshlxIGZijRAY9PY8QQvIWkVsVD8c3JMWWGoDeMq__vLevKDQh_5PglzJ8ntrYakiX_ZgOpresVc7Kto5yL0rMszNmlgFtPrIjomcgADH9VgY1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkcqaR9JAdrROwMjd_LGnxT2AqwR1ia5-GcUhl56Vziy4shas_IOr6guvStoL4OgE8sbHaOk4sMiW1Dv86Q-ivjuvzaRawn2MneMobyEsn5j7-Dd03rDcvAN1fk98ak9xXONj1i6iWA-qmfVnu0AdmRfh_5HCGtbp7KC9FoHpnAEUbLQ5h51qkBElHrKq8VjVuppw7hh8NCvVIFWfZBl1bAyYt0aIW-5_GS_CpnnXeMU3BchEIbkKZlDV-nqZVU0Y0F_Boo2YUedP6nWo6TzbzFMVR0BRDkoWkIVuuKxAL6FuzzHBsDlNgIlbHax6EsGg-5fr5w0M2oswjxF0pXnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=LLA9lbD8-C5ncFU__1LlO0Y88jJ48t2VyPyB5OXkzgPTdhD334NYkNaNyfNol1FQK3FDM-RzGFr2iV-3cXRL3VXzCA_g_18My0_EWJAsg-zJpaPG-W1S05DdG8O3wCZmI37a4qeddypa2F3w7JI97ZY1egwE8gFZAD-VJ6ZqA86uQ1lw9elKSUVgQFnuJWmA92U6y6n98Vb5miQxQ-ARoiKIMJmMuP-fl8O0SMgu3qI7-cZgnzrhUtrtOlR1JBMxLJ2NfwvA7Sw6hkvI-f6buAY9wy0ldGcA4I1BOl39fBoj6f5r_cLIjkyVaFJpa16bXcnsJlgy939zx0bc51U4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=LLA9lbD8-C5ncFU__1LlO0Y88jJ48t2VyPyB5OXkzgPTdhD334NYkNaNyfNol1FQK3FDM-RzGFr2iV-3cXRL3VXzCA_g_18My0_EWJAsg-zJpaPG-W1S05DdG8O3wCZmI37a4qeddypa2F3w7JI97ZY1egwE8gFZAD-VJ6ZqA86uQ1lw9elKSUVgQFnuJWmA92U6y6n98Vb5miQxQ-ARoiKIMJmMuP-fl8O0SMgu3qI7-cZgnzrhUtrtOlR1JBMxLJ2NfwvA7Sw6hkvI-f6buAY9wy0ldGcA4I1BOl39fBoj6f5r_cLIjkyVaFJpa16bXcnsJlgy939zx0bc51U4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=YgbK9EQL69SBKrkv-U42nJo1tZzrIPIfePL2a9o_qZBgzyis4cW3-4Wcv3LtVd1GIpBBQO9rjERymUJWJLq1KYvJ1S-0-4BBHZREoqDNSrbMiXOjg3Qkci8uATLg8NGh4vYmUOFr4ZbphNFZs-CuydBbJ4_OpZ65wViUS9_WxMRTfsaW02YAUC8vt8pvtzTFQrg604_jTX1CbMKkVEKeZ3m1DRr-p7scqjzRoiUwyYzAJ2Sc3dI90tN8Oy92Yc4YL7OVUwaOh5ClTLHIdAmKLycUL1FREZW4dUYVs-2JIEa9dVgS8DyU-NhS6sK-px81-BVfSLDC3Hm1i6U8oqiyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=YgbK9EQL69SBKrkv-U42nJo1tZzrIPIfePL2a9o_qZBgzyis4cW3-4Wcv3LtVd1GIpBBQO9rjERymUJWJLq1KYvJ1S-0-4BBHZREoqDNSrbMiXOjg3Qkci8uATLg8NGh4vYmUOFr4ZbphNFZs-CuydBbJ4_OpZ65wViUS9_WxMRTfsaW02YAUC8vt8pvtzTFQrg604_jTX1CbMKkVEKeZ3m1DRr-p7scqjzRoiUwyYzAJ2Sc3dI90tN8Oy92Yc4YL7OVUwaOh5ClTLHIdAmKLycUL1FREZW4dUYVs-2JIEa9dVgS8DyU-NhS6sK-px81-BVfSLDC3Hm1i6U8oqiyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5O7TZHIa-nIf-mH3Vs3gmgOvgSwrNBFmw96d88TszmTLjypOHGUHDmP4EmrpHIMhW0S80_ZToi6irIzbGVIT4EQfSgh-ASizWedBkJlvD5m6ot_UQoRXxKiaNmwvn47Cz53DWo6ToC50V66ea89wpVeXUdKBxPZFfh2iuVKxgegk9VYVW1nbVSdyw0eW_ffmoxP5w8LIXaA2w0RLmKU07zLZydNxGoO_k7bilwpCyskZ1wue0SYUlHyyz75ApQ9HdR4Iy1XeDMpep_5nOG-Nie3-nU6hLTb894XbHf1JrxZbw2CuJ-agCx8wnCh3jRDM175LH0DHtlVvCpnj0mM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3OTXjLf5dZs0opSF-QYRFL7O-iwrJvA7tp4QS3kKqxBBqyVtN93Fvd6ZtpxF9P4EUbo7Lp2CGSs-hQEPyl2y-yi72WpxeZuvRBohS-XdD7SaubVGMNXg0sSoUEDHtFVDELNlaCwXSvd_FjbyA530EaCNYELfv0CrmzjdIvbjjls2lzuUO8m--QQh4SDYgwjyfw4a0TkJM_aMc5vf1y2h3qw_4ytKw_HZ_vuDa98XK4vqxr0LNaUw4aLBpDawhIUKX_ZB_fnqiPfITQcq_p8gjvdUPvdos5iI9hWVQedwYNWs5MpPbbzSu1HiT-IRrofNBKT2JG7YmBYUcc016oq_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJMIF5emGFTkwtKccdH8X1_78M4lMuC4_zSczB0w74DT_rK76pHvUIxGe-G3PQn5kNBQiXeP3QxzjTibDqpnga0s0_cYw-5XKu5R0RDGqmhpLSKwBk11pKK_n8b4FO7Ev3hlj5rv9l-9xDktkqAtwQE7hih08_acmx-vU3OoucSM6goR8hBDINnN9xH4fD27NkPnLTO2RONkmkcaIMmQFhQa717xvAa46uc-58P3ZBCdnykFjXg4BIyCkCE114z0Ln_x8pReV60lZnmGBV403dYYYqA-_X6rGTaaNdDs51gIuwBJ61oqYxscldIdcVMh3OLxP5uP3eXUQiow3g_ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9-plxZ3RRaeLHSYDN_Mu-9FirCHlMctibjaRNE9o0nmpOKXYnog4owt7ZUHZuk4jD9seRHESAD9F6KWbju1zFfB9mG0qGckzgWNqX9rDRItk3Pxq4IQ7E4OnyWJq5LsszGgt5-E0wWFCPVFB1UQ_Rrb3Ho7rukjOtzaSAm6Ua6CjKkdfUXBMH6ykr8Z2CHzRWyxwYALICf5RSjixyqXdQIQJ8Iw1iDCQkIPh0E1gKYAEfm-GtEl9IHYbPDJg0o-QKYo-5T57W-PhvS2JM2-sAgS8I828ntwEHn4xkF4LdMXFbhuVGSpCExTFj7pG8Duo_HS4nqgfbbZo1oW5MydAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpVGTtzaVN7ytO9C3EWQfm75Zu5Ulz1i1UxQnNFFslgXRnyXl1UIrZ1DDeFT7X3zNNME-L2__QqvUBhvsWCKm2BBa4unQ7st5T9ZIXOEBKDDQ6lj1NchDGV1_JSD_gWqDRxOJgAsXjDelX5Io3aUzRFsBDcIiEcIVHME-pLgNJWp0-04l-mvcZFNgBjfPqk6IRkBqFXHkQKIYagq-Qz6H8Zu2W5pIGMsydXJLqlYXSgx9ZD4MophWlriUSnXMvin95yCRI7EF3zB6T9j900w8vTzZNzz5oZWfs2YrJWvqk8Zlc2kfZN8zNM-3uO6J64NNZtEuIh4pSKy_MgdgdZpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=ExHSnmkkxZKS2cHqn0VxfQJMd5cZinmA4oaNHUDyIBwmqKFz9I1uspWQj38Z2_5IiqC22Fl-qbckFVArGZMSakHGTgOJt7KgXuzRqSjkAPB4Ip2yFNP4IltWsW4eWvsMEl5E3HMqnN6lBsnMELfMeyryBHaXX-VsYxfrbxwTkCeVIfvxP0DeW65Qtg-czB3JOBrbiDGpPJT3jhvsNlR-wVDeMgmuYm1MPfDE2QsXsF6y2IQsZ0KRPbisejO5ObELPdmMsGL_uDDGD59H82AwqEWAak1HMyh4FSDYCkRAkDFicTWjkE52ZUOQ_99WK6pjmCktMdL6PtusScSgb7TJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=ExHSnmkkxZKS2cHqn0VxfQJMd5cZinmA4oaNHUDyIBwmqKFz9I1uspWQj38Z2_5IiqC22Fl-qbckFVArGZMSakHGTgOJt7KgXuzRqSjkAPB4Ip2yFNP4IltWsW4eWvsMEl5E3HMqnN6lBsnMELfMeyryBHaXX-VsYxfrbxwTkCeVIfvxP0DeW65Qtg-czB3JOBrbiDGpPJT3jhvsNlR-wVDeMgmuYm1MPfDE2QsXsF6y2IQsZ0KRPbisejO5ObELPdmMsGL_uDDGD59H82AwqEWAak1HMyh4FSDYCkRAkDFicTWjkE52ZUOQ_99WK6pjmCktMdL6PtusScSgb7TJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGPMyZbNLyJwaEcMuSk8LF8MuO6Eb4I79gCo8u70a4w_Onlz9SzJuZB6ZjtvhBNgWXm7U0moU35qNnKMs18mBG7qCxszNMFJIkFbHijcowBt4x75UeggFEH3QgE8sJlVkYHujyAVtCaODiKDkms713KxGwkzcGzBwPIiUQLQVx-padn3DsTVsz8sSOZeuoVDsa5z4MiwUhWzPLhNuX7Z3DQ3WjFytZdb3n58oL3UWnpVGbw_zzKpsjgZNLGNCcTv5flJNCdQOY-a0o4gtPC35bbw8-2-rBgrWkPvQmO09y3Sek-PUDwJ5RiZyKCD0XCn904Je1LiuLxxmHxfJ2ahNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkirrHVtbCSglpkUaQcFMtHQxgGBguP2G-0Fc6brOTeLnwbVERJeTf9vswjY_HF6wIUtUfyat-ITRz4TuJHb16hYGLxwcJaAStdZbP9QSYGqYVMAyAHZQwql_9dt3DpLkOQMx3VhltxPVtt1mGU6jMorNV46QKC7SpJ3R1U7mpghGNzvqLWbHZFkah_WDA6Q3JDjXuqj5nGk063Cyiv1WZbPS6zEA7-6hW7nDuCRs7AI-rqIwd8F2rm26XhVjajbgrLqJ5mNT3ojMRNkPw6NUMhMhjvcbgW1vsBHOgZ_0DnLNDZ6YviImGKCUYgBIwmDBbBh_EYT-9onGiAk2H3EwOqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkirrHVtbCSglpkUaQcFMtHQxgGBguP2G-0Fc6brOTeLnwbVERJeTf9vswjY_HF6wIUtUfyat-ITRz4TuJHb16hYGLxwcJaAStdZbP9QSYGqYVMAyAHZQwql_9dt3DpLkOQMx3VhltxPVtt1mGU6jMorNV46QKC7SpJ3R1U7mpghGNzvqLWbHZFkah_WDA6Q3JDjXuqj5nGk063Cyiv1WZbPS6zEA7-6hW7nDuCRs7AI-rqIwd8F2rm26XhVjajbgrLqJ5mNT3ojMRNkPw6NUMhMhjvcbgW1vsBHOgZ_0DnLNDZ6YviImGKCUYgBIwmDBbBh_EYT-9onGiAk2H3EwOqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhloAtzMazcCGW9EASeDveyumG1rRc7hnUbUJlDu6jQH_b3t3AVJJ63pf0eZGE3Mqj-LWIrAPgV_jJWoihMzoaJB2dBjOIGz-hd0WrZbh_7gcrpgSuw4k1j2y8807O0H6pPxBwZkF8E5eBhQ5_gLj4zAEMYuQ8uJZCFgzXWob2q5kWEdq5n2ObPhA4qe0dwJTgI25CcDuYacaivoApuX6vgg8JKT0zQnr4h8wvgT6yPRe8UINqnKwUXiAHkX1vpv5Ur9yzmYprOQLuTGG06TBHsFfdqwVN0JkhytpuMcsvfNkO1V_uIJCtysZbIduGgX2OBJJpoRIqtV-fKPex_pjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgHE1PolQJ9-NP7Wms48nSRZtyHFrhqx2N5p6Bynun_U2kgf5ZFjH7R8QU7OeBoTp6qSuztLL7cYaQJOaT7dk6mA5_yEb5gZM4Cs_ajS7gRKtQeNgP5Eo7FJ_fvLuAgtvj3GjbueEv5lHDLzXXjrw1meDD8sbLYjuCDoMTZutV3SExyPSLmM1PkrDsrHGXw7lYR2PU5ezRkCVMc_8wA2_w0WZmSLH5Yyu4cnUe_uIHUrP2Pqkbk1am1kCs5niiIpmCCISDQMjiId3j-k9IqpP837cUuGhMFwA2V3hReB7qqzNUqdw4kElLDOESHLhEkp05KZjzrX5Nu5j6y2hcD3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-1g1L6Bwwlc4_-cneVigyM5fp_8QTs6yIcebSMZmO4HA6SnCerC3grIyqQG1v1DbZzGtLsUno25mFZFfji580fl-hLx7TGEIe0DsFODo-rEXztDVbVpkwmRpYicc8p2QWHKWRD0ycUULwUG5rq3k6WtrTjbG110uhmJS32SowZwijuK0CtpV-vbyMdRLPerfYEcf4m7hWcE29agsjYBZanUi5ZicQ8ts5B6bOJY9hVCkswINWCA5qNzo-Vm_1dWch_Agq7NBB-CN_0nSMEaeCAkjIs8ofmI-LiRL5iKz_Fvlf7iH0dW9223t1zp3ELDp_pUyThZ4dB1NuQJAFeR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWy6ezNj9wdWGNQJOiDFZ0yipOL9M-_COFF87ZObcavmJhP_CZ_qe6OUb1sd_KLo2RgpdH77CopU6HqPX41y-jajucsTxr-8DaSshUwUpubqUe8AFai-fCwRWTxtTvagiCIytDdGUIwlx3KEPw4py6JkgLKKx5_Mq6nvu-z1qQQ2TfbgiM29i1T3xOkOdymC2HrYbHd3W73njoWRcsblXYO7sFuR4AzUWLFaSKddVIV2ULz-9POKMqUHx8m_1Esn7DAY_oLip5BBUb-kT22r1LvVqT5yg9WyH15vAToMLf0SaYmjKzCMWv8T61wWmjkayBrOe1KEGWtb2rhrNQq9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYtwCJGWpBPb84XctQqMictcHCgeirDAGrrOyIMrmL5KFY144108El3Yq0Ajt35HLr5heonnD_-y8HEraeKwvlHBtLbhowrmze-bvFdENf7TeDS-PxM5M8BpuzjLsJscr1I8ucqupOz_9C8n7reonudPSy2kHc4CD6Xu974HmAsk96U0Jf4KqXKSl83-Eo2X0lHtxJCPCUyLHYLP9CGerxzYftz4MbSsPP3IvhUTG0rscNOL8CIaEqGK3qbkDoJEjs1IA7jyZr-tyuwY253TfPCffxHc4e3AP3QJ8wqn34HEyCUS79GuxJQxwskg_lRqxsOvRt10QYlPCfrPCBisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfm7IkoVXgGjB04Lwy3Gd9CNwNdt0JB6ndNNh2vw496injRpIF2Yjx7o_wjxWfpduxrIJPttXBPfUC78RjF5agJR3pFr89oDAJnauE6yTlboSQn8g2UN0m9c1mVgAP9RYJpP8j6GZbTxNMpPOLmfVBuYN0d1sHj9osdlHQ0FKVXQ6NGsfiKp9lawkMabaL4-qQeyOmi-3TA_hvaVyCdvfUWCOr3wsaKCsAW6D9tuU81AhcLdUnOQUm_ViII3LxF88JkGgMK9yY7r75uvYYOspxV2bGbE-5yb5GPciTFZnMmNOP5Xv_ugjmLJb1H_YYoRx6HobeYzBiF3wbYEppS-IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evw-jG7EGuqnLLnLUsp-XlMlGt4hYkRyFrzP2VdfBTDq-bc_J0hrFU2dimwocnITsipI1oSGcVG6zklcwV2GMsrb6uZ3E1-VkSKlcBsXwuuiX3nj4T_vGxxoPgnELXQb3ct5_37zZje9XsFwiPWhS0klXKPU7PhjCG4VKFefiRpiMgHH2JWOheLGVH4EzWMNeEe0-bwi1lEgb_D6z5vhiU-0Oiab5Crr-WeGJ3TgbLILxyLqALJHxUzQheHZsOnHmdesc07m6_a1TDPA0E2BupAM5nALPVAyJaDdcU4JsHv4uQBWe-Etq24xTMgAp4lvc65hG7aQ_Phtq902jqvgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
