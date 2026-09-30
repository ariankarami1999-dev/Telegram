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
<img src="https://cdn5.telesco.pe/file/ZW7l5BbdOaRH2QaHB2PDZQKTk7RmrJ9NYhtmm-3fC-xQItcinGT9ReVJ2OgEOXRyH44yccQMG1clTkUhSqe1qNNNIwpR6EZRTWHuT1Ry0a8XMnKsFmGr0CYg0v_yUAd1d3JDl9zM9WAaG-dMmiAPy5EJupkrr_UFmVvGumBlDv0va1Q0fOmgHxQ_LRJOWk1ZCKh5UZ9vVRCv58rJwNyWtCIBQZ85WbF_xO0HgGZgBuJ7kdEZeLZxrvfY0KAG0Pe-c7NNXUynGrwf6HHBVeHsCvSlhplCoV5bgJLBWWW0MzO4bw5SpnFZE1TUYLkyV4sFxqXvg_vxE9HuNwHAShKj6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 396K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=lhukTe-2RDLky5BONssmPwxwXxFQbWug-PPjVi0NPU9wkn_mcRxY6OEOm6K_-2hOWms8YnngRaaVQwELC0Ve0_1ksQv-0F0FVK2YWhFrLvpWw26yrWsjfh3_P2L_nKFoWRMeuYN5GzG7oXbOqwVBQN95pvs55nVSazill3magRCnVkoVIrWRps88ZY_GwgNEfcNr0xCdc-M9KyR0QwTH9gKy3jSIDxgnrlfgXXbAEuKUt6r-Lk7oi2MkGCMgnBhzW1zsSY_qBcn6GAHIVgUdzS_EX8b6ExL8_w0bpPmQ4Y44fdPP_KT5x5_a6wk2m710o53FqCw74pKPtLS4MwjiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=lhukTe-2RDLky5BONssmPwxwXxFQbWug-PPjVi0NPU9wkn_mcRxY6OEOm6K_-2hOWms8YnngRaaVQwELC0Ve0_1ksQv-0F0FVK2YWhFrLvpWw26yrWsjfh3_P2L_nKFoWRMeuYN5GzG7oXbOqwVBQN95pvs55nVSazill3magRCnVkoVIrWRps88ZY_GwgNEfcNr0xCdc-M9KyR0QwTH9gKy3jSIDxgnrlfgXXbAEuKUt6r-Lk7oi2MkGCMgnBhzW1zsSY_qBcn6GAHIVgUdzS_EX8b6ExL8_w0bpPmQ4Y44fdPP_KT5x5_a6wk2m710o53FqCw74pKPtLS4MwjiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=c6SJo9rX1D8osbd6XRzOEoe8c30X8M9TR5zIc54VugRb9cAHdYPZKPKdFz-6Xl0ePZQk4OOzRZ1F42tTqWOJe4ArQs7widO3YdAzYPJ8LnTILpKebIPtwj4NNWk9YZTwNtLfB-_oInxwvaOm31WDKTOVA4mngLbV0wW9HlAXzoU4lBRbG4TQBnMkNmRKaJuKnfGdLrCYJDwUNZ6aHrNY4KX5wqMeChQKotSzGWbhDM2IuFsVi6ELV4mEv4NfjgNYBYniZukEUb1gI25MFpkWX-oMfQLJpQOjygdr5kV3rAKqKMKXG71vJZNWvZgwGnTDclDjRab1dX1Ug6qo8Tp9j0QLFE5XZSyjSYZoDTmiIYsWVWrqfM9XztmoW_KO0wtAT2KGEfX1LGReUUC0RKZowLHhqB0pVno2fbTL9EgvgqxN1PLrzXA_u5dbaKfKF91zyror8LYJQxmHgJvWY_fSNLmWh-wQoxUHDbKV2KpLC_C03OykDnn-87w_O15CLou2tqd8r3965Dayosgw8XOfhH6DolTwEpU7YsVksr7K3y5iAddt24m-vhwmYufysDBkU7gYI69CMgkpR9cjxVT459oR4Q7dym2ixbYESj3KvKtSGovkuOURQ-i-3rVRKqWl3zi6GtkVMxlqyg3hLx0xrjdfIuNVwLJaLvn7lEt93QU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=c6SJo9rX1D8osbd6XRzOEoe8c30X8M9TR5zIc54VugRb9cAHdYPZKPKdFz-6Xl0ePZQk4OOzRZ1F42tTqWOJe4ArQs7widO3YdAzYPJ8LnTILpKebIPtwj4NNWk9YZTwNtLfB-_oInxwvaOm31WDKTOVA4mngLbV0wW9HlAXzoU4lBRbG4TQBnMkNmRKaJuKnfGdLrCYJDwUNZ6aHrNY4KX5wqMeChQKotSzGWbhDM2IuFsVi6ELV4mEv4NfjgNYBYniZukEUb1gI25MFpkWX-oMfQLJpQOjygdr5kV3rAKqKMKXG71vJZNWvZgwGnTDclDjRab1dX1Ug6qo8Tp9j0QLFE5XZSyjSYZoDTmiIYsWVWrqfM9XztmoW_KO0wtAT2KGEfX1LGReUUC0RKZowLHhqB0pVno2fbTL9EgvgqxN1PLrzXA_u5dbaKfKF91zyror8LYJQxmHgJvWY_fSNLmWh-wQoxUHDbKV2KpLC_C03OykDnn-87w_O15CLou2tqd8r3965Dayosgw8XOfhH6DolTwEpU7YsVksr7K3y5iAddt24m-vhwmYufysDBkU7gYI69CMgkpR9cjxVT459oR4Q7dym2ixbYESj3KvKtSGovkuOURQ-i-3rVRKqWl3zi6GtkVMxlqyg3hLx0xrjdfIuNVwLJaLvn7lEt93QU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=jY50wJQ93VhSfqzH1D8CoZYi9GyH4Rms7L9cZYk7A7rAjnlrwo_9YQtFK_x6SEA6MTE9hpvUvTx08HghNVzPZW9dPJGqOScRT5RGsHaC1oKYe_lIx89vpfTLwn-A-PPDurX5LCXaMAl1jQhx9Cfsnov8UvArg6_dXEnJwpHJin5-d9leH2Mn6_4TqvAQGwIc1TDn-_w8wDIaD_EEAfMF4rdGQKY8hRdQ4MKP8QxbAbJebrocUyjduTOyBywfsMPa5REC5tqEtg7pxO12jQNPKoWq5ccFpnqfiWqXqcMYoNHcQZRr_eD53m6lsJPBf000u2DvGkFLvibA02T6fOL0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=jY50wJQ93VhSfqzH1D8CoZYi9GyH4Rms7L9cZYk7A7rAjnlrwo_9YQtFK_x6SEA6MTE9hpvUvTx08HghNVzPZW9dPJGqOScRT5RGsHaC1oKYe_lIx89vpfTLwn-A-PPDurX5LCXaMAl1jQhx9Cfsnov8UvArg6_dXEnJwpHJin5-d9leH2Mn6_4TqvAQGwIc1TDn-_w8wDIaD_EEAfMF4rdGQKY8hRdQ4MKP8QxbAbJebrocUyjduTOyBywfsMPa5REC5tqEtg7pxO12jQNPKoWq5ccFpnqfiWqXqcMYoNHcQZRr_eD53m6lsJPBf000u2DvGkFLvibA02T6fOL0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=QfGecErjrDAb7LwhMt6vYd2ym0p3IUKYoBwxT-SK-wdlwk9XZBwt2TpmbAgLD0pF7cFXgg_8VXSodkva2_NA3NUYDGgrx0Zl3CoU_TAu9iAJ5K_H3sC3yuNdVr8X7wU-bmcF8QG9owF9vEvAa8FLKbngwf6PUQe9tLXuawGHP2xEnwr9Q_MxPWCTstXm3N133-XDXuz3KczwlEx371jDo8ZKRkdIx6IY8Sspg6eRriJzVk3f6jvBc90hllDZP1QuhsqLT_USLYq59iVsqO8UKc_Ebw8311LcBKcEX6sqaIbambGSpOvh1yNi29KIEm_XARp2EjpDtq8DkNjZk0Nvq7nHrUxqjK-9VUQGYxA9_nLzjG3IKDDRicyEMu8cQhYq1WHuGkUdSfHhCmP4Adky2Nj358jQbTe3M5PmypnM1C9AtcjRxgn9-Q5IKPJAOIjx466fZ6067uYJgFokjx_O2CpBtIU2J8ncEPohysJ2B5h0vxBOHPfDMYgSg_Y62TytaSlmcGiUc78pftZMo-AotBidL-bwQB3jzZHYay6SUIfet8BP1skiC-GW6-q5XTTAiikTByV_pjHHFKz1DO-OUw1ab7BNWXhLU7iRJqCIFxhuCGmAWZyWE1Wfa2XYHlh3H8Yj5EyNEh9igzulVtfT2jNP9Y7puKjTDig2N3dZQG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=QfGecErjrDAb7LwhMt6vYd2ym0p3IUKYoBwxT-SK-wdlwk9XZBwt2TpmbAgLD0pF7cFXgg_8VXSodkva2_NA3NUYDGgrx0Zl3CoU_TAu9iAJ5K_H3sC3yuNdVr8X7wU-bmcF8QG9owF9vEvAa8FLKbngwf6PUQe9tLXuawGHP2xEnwr9Q_MxPWCTstXm3N133-XDXuz3KczwlEx371jDo8ZKRkdIx6IY8Sspg6eRriJzVk3f6jvBc90hllDZP1QuhsqLT_USLYq59iVsqO8UKc_Ebw8311LcBKcEX6sqaIbambGSpOvh1yNi29KIEm_XARp2EjpDtq8DkNjZk0Nvq7nHrUxqjK-9VUQGYxA9_nLzjG3IKDDRicyEMu8cQhYq1WHuGkUdSfHhCmP4Adky2Nj358jQbTe3M5PmypnM1C9AtcjRxgn9-Q5IKPJAOIjx466fZ6067uYJgFokjx_O2CpBtIU2J8ncEPohysJ2B5h0vxBOHPfDMYgSg_Y62TytaSlmcGiUc78pftZMo-AotBidL-bwQB3jzZHYay6SUIfet8BP1skiC-GW6-q5XTTAiikTByV_pjHHFKz1DO-OUw1ab7BNWXhLU7iRJqCIFxhuCGmAWZyWE1Wfa2XYHlh3H8Yj5EyNEh9igzulVtfT2jNP9Y7puKjTDig2N3dZQG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=iIk4c6J6NvIAF7_pGJZbD3H5O6Xu0mqy_k3KxSy6pybCQuYD6fKHct2qQly-Ns44HhsR2EzQ1BpV2uf13UO2cblGrMWVbhBpaseDTZHEzO-vq1xjIjfsOjpYc0cnx6BnoktKDLpBfU-NafBqD-aC6-LDEXWKdup0xIEOfiu0uzKwNocX5xUc0UYo86MG1-rvAcrSuWUPUakt-I3TjH5OaC5TbA_8am2b2N-y8OsdFoLEyO2W84HQvf2YO1Ouk4nBEXUfMGXnrHE89D_bkJOnxR9g5u6hMbVLCrG-_hp1G9rJhZOFHCXBJz29zvluSnmkSwZnp_TIQhlN0-il_mobJ6fwVJJ-2ka3oJLJ-mAvOgZf_X7NtPlcYWNL-dEaEbF-A169kwXW4M0q5m9zlA0eiLBy5Mzy_C3o1-XEWFi3ifREjGqO3QEp9bjj9kf9IXVDQV1Cif1-9njSMgJ7b7ZxQvJ9tOno_kmzDEc8PjBTq72al0i-SWPh9yK7GdlpYENS2ijuqrcBaHbPVoGnBRi-CJ5SlFdbV29Fmrx7ulfsnXthdBHxWUfsWJSM7zhJEPe8KdV3jf8WJQs7UFXSGpUSNCc9ngn8Ktfw4kOl9_JUwDHPgzq-AnxzQ64yT105ukSyI_uEDHvcR4yHlCGuRgoAx3lLtXhYfWllUqMBl-3sPKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=iIk4c6J6NvIAF7_pGJZbD3H5O6Xu0mqy_k3KxSy6pybCQuYD6fKHct2qQly-Ns44HhsR2EzQ1BpV2uf13UO2cblGrMWVbhBpaseDTZHEzO-vq1xjIjfsOjpYc0cnx6BnoktKDLpBfU-NafBqD-aC6-LDEXWKdup0xIEOfiu0uzKwNocX5xUc0UYo86MG1-rvAcrSuWUPUakt-I3TjH5OaC5TbA_8am2b2N-y8OsdFoLEyO2W84HQvf2YO1Ouk4nBEXUfMGXnrHE89D_bkJOnxR9g5u6hMbVLCrG-_hp1G9rJhZOFHCXBJz29zvluSnmkSwZnp_TIQhlN0-il_mobJ6fwVJJ-2ka3oJLJ-mAvOgZf_X7NtPlcYWNL-dEaEbF-A169kwXW4M0q5m9zlA0eiLBy5Mzy_C3o1-XEWFi3ifREjGqO3QEp9bjj9kf9IXVDQV1Cif1-9njSMgJ7b7ZxQvJ9tOno_kmzDEc8PjBTq72al0i-SWPh9yK7GdlpYENS2ijuqrcBaHbPVoGnBRi-CJ5SlFdbV29Fmrx7ulfsnXthdBHxWUfsWJSM7zhJEPe8KdV3jf8WJQs7UFXSGpUSNCc9ngn8Ktfw4kOl9_JUwDHPgzq-AnxzQ64yT105ukSyI_uEDHvcR4yHlCGuRgoAx3lLtXhYfWllUqMBl-3sPKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If3DVxdN1tA6Ew0t7RnsIbmRFsP2sjwgJbPfXDPCYzgjokQgEsEgmcVHGGRr-Z1XxK1kN8yZRVQMKiSa8d9b7CemBzn4CYdLNE6P8IFJCIqvg-WAAoKQaxRA8YBRSG1gYcaSoQ6AjY_nWhH7wgbhpTL_8jtNpOxq50lvsyC69YJewQ0dWTfPA6SOapNNmfl-bgcFy0VY2fipeUpDe1iKppTxzuRB9dX71UmPU2RPBK0Y13cLQIj9GUaOr3ArAzM-Mu4lvHny_s7HSFlGtA_0cM1dL3gzM1PN-o-S2bMzD1EtBGrY-sGgOnA2FlG4APMmtzArUrUXbQROybxDG3SYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ترکیب منتخب دور‌دوم لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/107538" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
🎙
صحبت‌های شنیدنی رسول‌مجیدی درباره کیفیت آکادمی‌های فوتبال اسپانیا که زمینه‌ساز نسل‌سازی‌و قهرمانی در جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/107537" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107536" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/107536" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7gwlW9lAES99BaaGcYkN1O_44FA7TlBTJSzCHSZ2Oy_NXJ96vluGCK9B3UVLmyKLEvREcjygL6xntnn5VmXP7RBO60SuBc-RKTuhnjN7Rm0i9fipDt_audksCqV-AeREBStWTLlxLpL9FtPLn_g7tJo0TwXQeRbL5_J8nTS_lMISRepQc6AQn4au3C9w2GL-eksd3tA2kp53anL1swNhoZONkvknwPpS5a-OmhT3C41G59fmXJksQKR9kTDEf4_hFH6XSGCVQeYx7-DqA20n8EAmxovndLERyyb-tuWukAsMPFVc8tYAK-q7oyWJy6iXMwWEZM3DemycsqlABfzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/107535" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUqoA6PdmefKnrXfGCEOTif8FOwKpS4ZzPqRU-SqAnvBDfmk9Jy6z56-mpBkqNHZ155BVrxqYRdZPiElo5zAq0u5thUic39FJ284rgKio4YPE-UIydroL8VI7UlKt6xV18Pi_up75R3lY2uRWbyiTRj8ulkJBVdIkTcYy9jKH7kyOGs1DLDH-OSYODv5Xn4WcJdZfgHyyz9QBiOcLAtutks-FmI_ConINux3dGiiYh8S70XECBogr2FEesR2Rv6btAH84sOoDOsTopigGWx_DKgDZOg4Qus1js_zN9ODyfteg5fKL4_hLK6arQ9XCTlqkpPAn3YB3R_hOPtGVoy30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
رومانو: رافینیا اردوی برزیل رو ترک میکنه و برای مراقبت بیشتر به بارسلونا برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/107534" target="_blank">📅 10:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFP_vNoEDbHEWPME5qVz6Ta1jzVjaJ9-onQQWTgVol0EplfrZKXOII_LX_UofOXpy-XkvpByXf8Jgfe3vCRZ3gWLR2lRbBLE7LhmBNF4TPIVNxizbIejfzeU2Y2U5jk6SCKivC1AnS1r3lgmiBrxjp5OUKN9Wsqk5-8DCIWOATi7h_AOPqlDc6CxnTux14BwwnbdCDm9Bm-M6qFxwyUO40kuFljSgAe7qr8FHh2hRXLPgxNd7mq3o-2iuRvqy0mqDRR3PYGS2qntOgif3FvpgYV8VI1jmcytPRFY6Ckt_SmrnM6emF-9ypcUuoTh7OYdlxeLr5F4LMw6z-ijOKDc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🇪🇸
اسکاتلند تنها تیمی که توانسته اسپانیا تحت هدایت دلافوئنته را در یک بازی رسمی طول ۹۰ دقیقه شکست دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/107533" target="_blank">📅 10:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M12P2rm5g3yQh9WhaYRmsLSYE3Ap9OM3wG37aRS8OkbGpbDPfdWywPGOmyDys1lF4JLXQsavujYLuUs_NP8ggOVKVrU3H5XNQLwaeHyLdfbZQBKd4sEQ_3_vuxAL-n0mBqa8_NQwBWChTHIklwhBMp2tuVXlHuFOtVBcuqN9LXf5lqQaDVknmQZKO0qkAFby6QqbxC5yjXYuPLNrG8bseRYIPNryysJQVw6Jm4Lo9XJWEG9kisQQwUP-i6cgXJ4eVgnRxCxQeYkVTGuCnVugIDtZ89sKs2tYDnusACgzqrrolljE_UEhDZwA29SfbM5M5atBMijCyc7mqVk6buyxqYEf9FrlqChgQq-czIuO6wvb-hav-5hDgqa3bBLWOf0iF0CT6nbNg52IYy5v-cdE2YHv41GsOMJrnCTsDo2fH48ZgPj3GgaDTY4FEWL5PRcX_NIdb-BjGbrj5rLQK9zOqjVfVRU7yHHH34xhGcrhALveq76w_Vcc1duRvaHeBFx7APsGUlSr5iNc3HdSDhWymdqEKuaKkCbuyplP5hpULiiW9dfuW80_AsnnFKLM8MRsdxf-S9iyZw24jQU_BzQdpH4m72vMM0-PLZz7rYxTH77Dk1lQMIgZ-8k7q_46dbREwlwBV0GIDxJiJUJ3Ho5W7J0tHYlanyQITnAgfZvMD8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M12P2rm5g3yQh9WhaYRmsLSYE3Ap9OM3wG37aRS8OkbGpbDPfdWywPGOmyDys1lF4JLXQsavujYLuUs_NP8ggOVKVrU3H5XNQLwaeHyLdfbZQBKd4sEQ_3_vuxAL-n0mBqa8_NQwBWChTHIklwhBMp2tuVXlHuFOtVBcuqN9LXf5lqQaDVknmQZKO0qkAFby6QqbxC5yjXYuPLNrG8bseRYIPNryysJQVw6Jm4Lo9XJWEG9kisQQwUP-i6cgXJ4eVgnRxCxQeYkVTGuCnVugIDtZ89sKs2tYDnusACgzqrrolljE_UEhDZwA29SfbM5M5atBMijCyc7mqVk6buyxqYEf9FrlqChgQq-czIuO6wvb-hav-5hDgqa3bBLWOf0iF0CT6nbNg52IYy5v-cdE2YHv41GsOMJrnCTsDo2fH48ZgPj3GgaDTY4FEWL5PRcX_NIdb-BjGbrj5rLQK9zOqjVfVRU7yHHH34xhGcrhALveq76w_Vcc1duRvaHeBFx7APsGUlSr5iNc3HdSDhWymdqEKuaKkCbuyplP5hpULiiW9dfuW80_AsnnFKLM8MRsdxf-S9iyZw24jQU_BzQdpH4m72vMM0-PLZz7rYxTH77Dk1lQMIgZ-8k7q_46dbREwlwBV0GIDxJiJUJ3Ho5W7J0tHYlanyQITnAgfZvMD8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
واکنش فردوسی‌پور به مصاحبه‌های فرمایشی و سفارشی ملی‌پوشان: سردار آزمون، با سابقه بازی برای مورینیو، وادار به گفتن چه حرف‌هایی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/107532" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481359e02.mp4?token=q3Yv8SmMX_TOEOISrVBPnkPmqYwY1J2FGKBBuQ1Cs4P2qvEwaFhnKNLaIqDr0xefOO_3Nanpllzicx5ZtM-WRuyeHBCHx-yIi0GVuug3LfkkpSNhSt-aaEogvdsXp9zMd-yQZd1g2qwoadXuo6r2NfJCb8XCpcEYGNke931dmso9OSbToAXfALZ3yxebCZfYa5u8Vn_mGo3HA5qLq12EtYsvq1aOPz9xGmRIcybvRNt3Gy7NjkLKy5Bo2xToCf7rV5ztL2w-DguoYJhxR9NyHGVrPdXXL9yQ0l23YqZIKMluYQjTQijM1iNnXnTv1G9pg1T-fsOirngpUt3mmzu7Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481359e02.mp4?token=q3Yv8SmMX_TOEOISrVBPnkPmqYwY1J2FGKBBuQ1Cs4P2qvEwaFhnKNLaIqDr0xefOO_3Nanpllzicx5ZtM-WRuyeHBCHx-yIi0GVuug3LfkkpSNhSt-aaEogvdsXp9zMd-yQZd1g2qwoadXuo6r2NfJCb8XCpcEYGNke931dmso9OSbToAXfALZ3yxebCZfYa5u8Vn_mGo3HA5qLq12EtYsvq1aOPz9xGmRIcybvRNt3Gy7NjkLKy5Bo2xToCf7rV5ztL2w-DguoYJhxR9NyHGVrPdXXL9yQ0l23YqZIKMluYQjTQijM1iNnXnTv1G9pg1T-fsOirngpUt3mmzu7Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
شهریار مغانلو و دانیال‌ اسماعیلی‌فر:
🔹
چند روز پیش بیرون بودیم رفتیم یچیزی بخریم، یه نفر دیگه هم اونجا بود و خواست خرید انجام بده و پولش نرسید و رفت؛ بنده‌خدا اینقدر عزت‌نفس داشت نموند که ما واسش حساب کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/107531" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=SbVYWUDI9a7FtwRvDuvB7CapsR_He8o_QTzVMVd-X7wVZKasyWvc8U67-l099x8nPJZq8r3aFwQaWnlakYCL1lUzbNJcRFDxgV7kOPvovV6q1pRV5bwwct0LPE1nql46M3jl4qTv-Hj08bP5kkbZ0fBQOYYkIpnB9cWw0uiJhgCX31Z0ylTudG8Pvkyp24791jwhQhj7D5fErE8anzRbYifX2EPq0cyTSiP006xIkmGClnFb46XDGsFEdC2SqPh6zB-erNI37UPOecbhdvd021XKIVmT4DtGdoPT4PH9wb-E3lZm1HJmLm2jpInPABAm_msJsHIk_KHIUIRSnqkv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=SbVYWUDI9a7FtwRvDuvB7CapsR_He8o_QTzVMVd-X7wVZKasyWvc8U67-l099x8nPJZq8r3aFwQaWnlakYCL1lUzbNJcRFDxgV7kOPvovV6q1pRV5bwwct0LPE1nql46M3jl4qTv-Hj08bP5kkbZ0fBQOYYkIpnB9cWw0uiJhgCX31Z0ylTudG8Pvkyp24791jwhQhj7D5fErE8anzRbYifX2EPq0cyTSiP006xIkmGClnFb46XDGsFEdC2SqPh6zB-erNI37UPOecbhdvd021XKIVmT4DtGdoPT4PH9wb-E3lZm1HJmLm2jpInPABAm_msJsHIk_KHIUIRSnqkv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
میثاقی: سردار تو وضعیت سربازیت چطوره؟ معافیت تحصیلی داری؟
‼️
سردار آزمون: نمیدونم ولی میدونم دکترای فیزیولوژی ندارم، اصلا چرا باید بتو جواب بدم به نظام وظیفه جواب میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107530" target="_blank">📅 09:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlT3BELtC1Jz4qutcdBrDH-Di7LHG_KkZbd0_MBUfX7u5Hhaurtk3JDQnG-_rdmOPK9B-73xhgn-iPM_LiQ1LNqylVIX25NaseUkte_3PXxqatEPmLI6kfDtLXP8vAvTJ_sARRX4vs7um8s6vzb2hKDBqNE2hXm3aXYz1GNwu5OLzrv3LKOysvuIVbtka_FwWcHjzEukoYmOQyib9dY4yTvyVtvV6jC_Uf_CLVMhQkqeMiD6_UUGDZH5hAJQfD2CIuQeDc98ebhfoeDJBimJ96BbycDFstfHHvsgaIGtqM4UAub6qIBcfoiJhLZOiIG8gP2-JKHzs9zZYnOVchl9OblI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlT3BELtC1Jz4qutcdBrDH-Di7LHG_KkZbd0_MBUfX7u5Hhaurtk3JDQnG-_rdmOPK9B-73xhgn-iPM_LiQ1LNqylVIX25NaseUkte_3PXxqatEPmLI6kfDtLXP8vAvTJ_sARRX4vs7um8s6vzb2hKDBqNE2hXm3aXYz1GNwu5OLzrv3LKOysvuIVbtka_FwWcHjzEukoYmOQyib9dY4yTvyVtvV6jC_Uf_CLVMhQkqeMiD6_UUGDZH5hAJQfD2CIuQeDc98ebhfoeDJBimJ96BbycDFstfHHvsgaIGtqM4UAub6qIBcfoiJhLZOiIG8gP2-JKHzs9zZYnOVchl9OblI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇫🇷
آنالیز تیم‌ملی فرانسه تحت‌هدایت زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107529" target="_blank">📅 09:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107528" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107527" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107526">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=BewH5ZKKfeIj-wXakqM_Drjz0YQowr3P9ojVGXE8pMlI3pLwt4CVcK8jjdMI8t1t560CpYHBGfCMm_xPsWlV1BDyb6c7skyxHmEDCQuPS-tAFN0U52g00xGRrAErkGBXskUYbI0zgnDtes-fPnNaIc5bAOGxDBmcAAfR2GgZqpFOPC4oXOfbbfW1YOK4_gmZtEg5gcVO_Ew19_ZR4T7EqohT-knUmCUcCGTHLndjstqNlNoThsAoYCrS10FN55tfK_C6JVSGl4FZBMJykNvSeZgXiNrk2gcSnxp5bwBYQjfsrNyMLkieE5ZXNCAymLDV4QzIQ4aDOP3o1PgZp0jTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=BewH5ZKKfeIj-wXakqM_Drjz0YQowr3P9ojVGXE8pMlI3pLwt4CVcK8jjdMI8t1t560CpYHBGfCMm_xPsWlV1BDyb6c7skyxHmEDCQuPS-tAFN0U52g00xGRrAErkGBXskUYbI0zgnDtes-fPnNaIc5bAOGxDBmcAAfR2GgZqpFOPC4oXOfbbfW1YOK4_gmZtEg5gcVO_Ew19_ZR4T7EqohT-knUmCUcCGTHLndjstqNlNoThsAoYCrS10FN55tfK_C6JVSGl4FZBMJykNvSeZgXiNrk2gcSnxp5bwBYQjfsrNyMLkieE5ZXNCAymLDV4QzIQ4aDOP3o1PgZp0jTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
کنایه‌های سنگین ژوله به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107526" target="_blank">📅 00:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107525">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQN5HqfFjyBz_vsdYT8f73X4HrCpcoxUCiz91lVRnBp_x8mu8xgXawxKP5iC5q4tHysY6LH14mzdxiVhHajjX42VPf0lhwwOOeny0Z_HCxx1L0EdkSPsV-qlG3z2wV4vZdnl0xnasCnJBxFj1Z6rPRPc7c7iV-v87LucVwP-A5nTuJuoKkukvfGAzma_cFVrHV6nfcL7qcAuj9aHsdzAIu5tFivFYpUEyJdmF-slKRqlAPTxNdagFyqajP50n0FwKCSnki4gwxKGKuwSsDCaYAr-1ItSS2hbRldxpZKTxUhPjsbSCTiYeYuGqxkTAa1SaSDFmmEE0d0DZrURw783uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعتراض میثاقی به باخت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107525" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MomElupu4cGDQnaC9Kr9BBPg5zYXDww_DiX2FVGRMkqlyIw1oHJuy0iuUzIbCwS4s9CpuvJwujL4b2ETvr8CBVHK7Gk-KJcDJuoetRyfVtsH40EC8rmrEe8TdvbBb4OK4qsjEXKxp9ty-QuawYRIFWr4BR-RLOq5-TBDi9ExFHPfPJ-lYg5DFWw4UjgBcQONAk67aHlyo1x6Sv4Wq8MchhBW6VmF7NoP3_DVWO-dbSAkvQPiiRUk64F4MlaaAqA7PGUn4CxhkbleUgcn9p7wsPj00bVQX8QK0Wo1wpx5CyGnrkrsBRTU58AB08YjrbDUsOZlNaeOo-m9OTYKuZlA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
پایان بازی؛
🇪🇸
اسپانیا ۴ - ۱ کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107524" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=da0Rd2K96S1xaICJM-ByQQ4GGAvzS89Pq7MqfO0YyWhBL8OoR1gpAnb-g4n22uCVyKKz91IyUQ-2-UL5KSKISyAr4GTUTh3HMpZdOWa68frbNrTC5wdfRyrbUaOWYtRcV3fPLyeiXRrRK5h42nu8R_TlydtOE6uZ6a91cjH-7p3pNqlg0TCkP69-03hBcVKEbpvN__JmGCvuTCdhKja6Ezf5pyP94K5q4IL-1kfWy5MoX3_A0wjh-_hy7O-YgJkj-ukdLbMvhqGYY6145KzKViRwLEKzAfGr6RX5sEIhr39bvnU5BbuBoJj5pOtcCxb7vHZVhKZfSrbTkS2-mJRMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=da0Rd2K96S1xaICJM-ByQQ4GGAvzS89Pq7MqfO0YyWhBL8OoR1gpAnb-g4n22uCVyKKz91IyUQ-2-UL5KSKISyAr4GTUTh3HMpZdOWa68frbNrTC5wdfRyrbUaOWYtRcV3fPLyeiXRrRK5h42nu8R_TlydtOE6uZ6a91cjH-7p3pNqlg0TCkP69-03hBcVKEbpvN__JmGCvuTCdhKja6Ezf5pyP94K5q4IL-1kfWy5MoX3_A0wjh-_hy7O-YgJkj-ukdLbMvhqGYY6145KzKViRwLEKzAfGr6RX5sEIhr39bvnU5BbuBoJj5pOtcCxb7vHZVhKZfSrbTkS2-mJRMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107523" target="_blank">📅 23:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگگل سوم اسپانیا به کرواسی بازم یامال
😐
🔥</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107522" target="_blank">📅 23:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=CoALdKgcljXOsdr_ygRjqx6e8aT4ecPxBiNwxEe8FzMme_IB6HyHNLezC4VpmV1BRCyEXi4pGEfppWdasnQncFHI1KAeyUh_u9ppL3OnqCGWciHnGIt8tZAyucpB0q8XROIyxQTssS9udC4XXcW-RqOKYK2drbPOePK-2kcM5bRsotJl7bLpoZpTa_XI3FKGYSqrNq-Y5J9lcwZstLBS-EMlZ9p3Qx0br5OG_ZBiRsrhEv--uGKyG9lYyeExfm1s0S5x1hl4m-iu1pHfXL1a9yZOMKb3n41vn75eIITBWttyJrhUxJY5YEKZiT3lBx3jbMqafp7T5-FxWI-Ch-LQRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=CoALdKgcljXOsdr_ygRjqx6e8aT4ecPxBiNwxEe8FzMme_IB6HyHNLezC4VpmV1BRCyEXi4pGEfppWdasnQncFHI1KAeyUh_u9ppL3OnqCGWciHnGIt8tZAyucpB0q8XROIyxQTssS9udC4XXcW-RqOKYK2drbPOePK-2kcM5bRsotJl7bLpoZpTa_XI3FKGYSqrNq-Y5J9lcwZstLBS-EMlZ9p3Qx0br5OG_ZBiRsrhEv--uGKyG9lYyeExfm1s0S5x1hl4m-iu1pHfXL1a9yZOMKb3n41vn75eIITBWttyJrhUxJY5YEKZiT3lBx3jbMqafp7T5-FxWI-Ch-LQRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNWD6nthcZNVvEPlUGLfwhjxEoZo9fqgz-RogqTZWrYrhjvubRIjHCgBSfGYoGOqDMVA0uaIsTVFX8QzarojRj_jesrZq6EWP8h7ZjS8Mu6rSF1hYA2PeYb66jlb_luuiXAfs2W82Qwpw2ocR99rAkIo_rcNFrT_7w2t66511-evJHnz85pr0uWYnJ3cG3A2HACW9eJk-cpBvy6_xEy8foUqaIvOmXbdFeOARVk-hte_f7OA-IkYjiINxwAvLJnkkuEP3j2LnVBhlgUebE_7zm1nDtASPAXk5TU5OLntDNZ6AGIAMxRApWmSACqIr01lYHGqhjQb1zTaxyDUsSiDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdBRPu5F6J0YFuJMCfdP_9bsDAO3JXGJmDopTzvl3_5aAz8cUims4Sa-IbCzczVpYYVD1RZX4tw0yHkNBelQeWPSEOrkF_A2-K2-ewyhnLbVdU5llHULTwY_6RdrKx0F2MFH1NPCiK9CPRWv5VUkZ_E8qRQu1Ehp8aJ0y14CwS_EqvgmmNLiZS-GNibel_WVH-94Re7E7h2yAUcCcM0xTZo_iAxthYMwuBzWfoFg4vA8hv6kpPetHVWufIC4lflzGbcYAUfjlwA1c9-P0R1mcF3sa8nN6-_fk0iL_gGBIm6ek0ELNrYgbKOm89XMiQ01uBFRbheDZwN109DHSg-5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=CK1wKXAV7RNB44e_oUOjAdphf03hBnAnKoFL09blr280a9_93bn8x8CpFgKqyoafarCXcdc_RhtZfijKsV6ZrzQoffyqBdqbjlevtbYhSWHD66x5LiESlaybFoGCbQcMxFMZnmOG7YutjaXAIfWW9OJouwqZsd2cLtcomC9cV5cFfou-R9DeHIar4fPnI8_4SMlFYIAfocKP1z2R2IttzBh6PLTJarxLfbtyFcd45M-66ZdddS-BLOdx24TQspC-UIfo347DjrhFlhvqqJgVi7IwGE6KP4xqt43St48a6t6SkGiJu-NjznQ-WN_wvwTT0biecirIx8VTA-kw4WvnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=CK1wKXAV7RNB44e_oUOjAdphf03hBnAnKoFL09blr280a9_93bn8x8CpFgKqyoafarCXcdc_RhtZfijKsV6ZrzQoffyqBdqbjlevtbYhSWHD66x5LiESlaybFoGCbQcMxFMZnmOG7YutjaXAIfWW9OJouwqZsd2cLtcomC9cV5cFfou-R9DeHIar4fPnI8_4SMlFYIAfocKP1z2R2IttzBh6PLTJarxLfbtyFcd45M-66ZdddS-BLOdx24TQspC-UIfo347DjrhFlhvqqJgVi7IwGE6KP4xqt43St48a6t6SkGiJu-NjznQ-WN_wvwTT0biecirIx8VTA-kw4WvnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC4gSXO3KL6LX9ihATvedbCGY9PpKyJCEWdzWtT8qCkFLybAJ8ipvKh_kFbyx-0ApfWYxlqv_jMpljcerCPEzxk8O0F-KD6G1Vo9dAEgxT4nth0aMvvDPOKUeoC_iB73dfAAIN2fqETJoPZDr__mZHbuceCCtLxjC6Pm7G2I8lxY4dMFpNQHkTzP2iPngv39ovGzdGxwoUzln_LXw1Dh0Iprhli0U7HJR5_pYfva2rm6RZ1G7uR-hoIIH15DzdGJphgd6UWZg8OUdpLqhDCkTFr7RZCy09kaqJSPqef96Wye9djzqNgSAT1y0WCH6qSLHsobDvHo9MzxFXrynOXwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY9bBu_OLGFYLAMxDoYS3SexPMHRwc4Htko9UcDJb4KccbUe8Fk0uczwRGCRkJLIW0KfzF1sH_Jc58apZXCatf1Ov7bID90W6vS0z6ot9niiLcyMOOTvqp9TKiutDYLusdISanXW9ZNTvRmq0H97WoGrd7jL5JkXe8glmBk3Ulch4LZ7m5zazEJFTNaCyZek1-nkKwJXOYuxZyIBwEGRB3IZzXUQbQ4v1_6yCWnSvrFmUS5hSrRZJsoBH8ucsKEDKo9R6MEGkt_2CgBDK3xWUCpSSFbAgZ6Fe23J5NBFkZxhR3DUX41G3gAxSHo34yffzH2MHEviso8wcLtg4bSGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=cBhPsauoMWH7kyShFqXAFNw0zMGotlkcA3FrRAGguYtCUsKB88uPPUpHgjPw0XM9NCV5i5hWeR-NZx7Y8L_5yDqRepgJhEHFCDWV_ARdWuRj4CqYKQZ4DnJAHOyjU-myr11kJ2JqkJ0AuASQc1ut9Cvb-oisS8aYkRUnl2R1M3VcY14Olsr65kbzEpPg6aSVOua0xLtD-sr6m6GuzAFP9mufewMaut5nT82XXFDZw-ejLY4D4JKrUYnsxSPHj9mCEm5HgLkrzya1x9bDrVP_PHcGGNfMRd5bBqr7Elt6audoiHXvfJIOXwgb8O1FLB0lWAdoES3qQXYNyDusZ2viKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=cBhPsauoMWH7kyShFqXAFNw0zMGotlkcA3FrRAGguYtCUsKB88uPPUpHgjPw0XM9NCV5i5hWeR-NZx7Y8L_5yDqRepgJhEHFCDWV_ARdWuRj4CqYKQZ4DnJAHOyjU-myr11kJ2JqkJ0AuASQc1ut9Cvb-oisS8aYkRUnl2R1M3VcY14Olsr65kbzEpPg6aSVOua0xLtD-sr6m6GuzAFP9mufewMaut5nT82XXFDZw-ejLY4D4JKrUYnsxSPHj9mCEm5HgLkrzya1x9bDrVP_PHcGGNfMRd5bBqr7Elt6audoiHXvfJIOXwgb8O1FLB0lWAdoES3qQXYNyDusZ2viKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل دوم روسیه به ایران توسط گلوین (35)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107509" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
گل‌دوم روسیه روی سوپر کاشته حریف!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107508" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=JsSv2cXdHyhktkwzrsyzAewCHlFXAmiZckH6Jv51zFjaFOxA0khbU0tfkoFsBmSmFoqySq-SL-43vgsfidX0rcqLZUeO41G06SEYi3PNpPlrvjXoHfFmX0phDZK8HY5rAv3tsY1sm0QPDOuty4dQrktfc9uEsE7O025S7nqwl9VNaRVNqVGGKTto9WmHNu3yqp0apScja54iUHZnRnk19U-3NA9oZDmM2A672OAScGiwFrui0fhDN-5afRVDEKFqsQ87ugOAD5qTjb7K5Y-Bm8wCObAUm6vPWQzfY9mWxLICgBQKOc_vikN0246PTI1MoE8Uzp9Pmr-ATEerwA9IKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=JsSv2cXdHyhktkwzrsyzAewCHlFXAmiZckH6Jv51zFjaFOxA0khbU0tfkoFsBmSmFoqySq-SL-43vgsfidX0rcqLZUeO41G06SEYi3PNpPlrvjXoHfFmX0phDZK8HY5rAv3tsY1sm0QPDOuty4dQrktfc9uEsE7O025S7nqwl9VNaRVNqVGGKTto9WmHNu3yqp0apScja54iUHZnRnk19U-3NA9oZDmM2A672OAScGiwFrui0fhDN-5afRVDEKFqsQ87ugOAD5qTjb7K5Y-Bm8wCObAUm6vPWQzfY9mWxLICgBQKOc_vikN0246PTI1MoE8Uzp9Pmr-ATEerwA9IKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇷🇺
گل اول روسیه به ایران توسط گلوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107507" target="_blank">📅 20:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روسیه یکی به تیم قلعه‌نویی زد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107506" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-NeggMkbew7A2ZcxDR8ktBv6RRbsRF1W_4gOzvz5JMgoI-tKgIXuRh3zJIa3hl1ED2zjcBLXyKyp6w-ndqTPUueIieJjIuszUB1xOod2nTmeuNjDd-BdUbImXRb7VrisX5rmyr2vyfCRZpMzQvZu2g00QDgXMWGyXNTFDhMos4a86UeCv2bpyilrX4V4mwrUompkKZkWoxo8WuswJTgMa5yFsirEQzTSOHL4VnT0rcRSmTblHJQhEGpCZp9yYKWczzXiPikqac_im2zzpQFqRXJ26w_gkDBtwR7EOpblijaAxGyAu1QmmnepMCdJAVq8FmxX_Q1i3bH9rnkwJ7_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد  این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:  منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107504" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbW28HR_PTOO8znqRRc1QAEuwswkPsb7whRBwDyDIj-nHJluD_DimVLFIWServp6NbeMslcVt6mMTVrFA3Nl3IhzcCB355XXywjcD2lJ4BWgQ66hmsOb3coV1QIJCSIVMT9gHSerLH3bH5UVXIz4r8BZ08ft9CKZthS1rG-n8IRnatXMBOAm2RM3LP97OhVN7br7LygWn8OynuAyOJZFuxkhnSpVkMvrahI7BWh9DpL-kH0PH0nUM4GeH7uDEGHO77c_D34kdSCMyIAYe9PNnyRRTqh1AwvfjeaZWQgT46HPhFYh05k6nlvhqhhahC00NIrSEFESqlt5eP-yitnfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد
این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:
منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو طرف را به‌درستی منعکس نمی‌کردند. این باشگاه همچنین به توافق‌های «صوری» دیگری نیز اتکا کرده بود تا درآمدهای خود را به‌صورت مصنوعی افزایش و هزینه‌هایش را کاهش دهد.
این باشگاه صورت‌های مالی نادرست ارائه کرده و وضعیت واقعی مالی خود را از حسابرسان و نهادهای نظارتی فوتبال پنهان کرده بود.
منچسترسیتی به‌طور قابل‌توجهی محدودیت‌های هزینه‌کرد مالی لیگ برتر و یوفا را نقض کرده بود. در جریان تحقیقات لیگ برتر، منچسترسیتی چندین مورد از وظایف خود در زمینه همکاری با لیگ و رعایت حسن نیت کامل را نقض کرد که از میان چهار مورد ادعاشده، سه مورد تأیید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107503" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=YxhdwuzybbCPUxOveKtIh3eH0xibFG9eMOC-TQuFmwDCqUwptnKqoWnN99ULGkoOZ0qVXWlYqzVopVPZtk6y4anChCCUuVN6YL8mMhZtIYcg2rWXpd93O9RCJHG4bpYJmR61U0Aah5RSuPjueOFtRsw6A7Ry_4KJlyAA8l4XH9aKz4JaR1N4DQ5pbKrf9vDmtA1pWtwcPaWoxNYP8YXyI9nxauxj2xDvTnW_4F-3tRKEpiut23HR7kBS8wnB86jMgXnAh5pBtCfvedCuQS8A2Ycw2_Z-bnnBH4KehXBwgOWCHHFhcX41nuxeHZxw77zgWQS5rsDDVpiraiHw3Jc2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=YxhdwuzybbCPUxOveKtIh3eH0xibFG9eMOC-TQuFmwDCqUwptnKqoWnN99ULGkoOZ0qVXWlYqzVopVPZtk6y4anChCCUuVN6YL8mMhZtIYcg2rWXpd93O9RCJHG4bpYJmR61U0Aah5RSuPjueOFtRsw6A7Ry_4KJlyAA8l4XH9aKz4JaR1N4DQ5pbKrf9vDmtA1pWtwcPaWoxNYP8YXyI9nxauxj2xDvTnW_4F-3tRKEpiut23HR7kBS8wnB86jMgXnAh5pBtCfvedCuQS8A2Ycw2_Z-bnnBH4KehXBwgOWCHHFhcX41nuxeHZxw77zgWQS5rsDDVpiraiHw3Jc2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باهم ببینیم قطعه ی زیبایی که استاد جواد خیابانی برای گلر تیم ملی، علیرضا بیرانوند تو مترو خوندن
🗿
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107502" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107501" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfM6VeKCB1xs6_LRiYFY90MoxD5cGYux-kN_Jc1_wIRaqmJVQUHThjkbixmT7DdnCcvLrof99b9nW4YX1TdH0lS5ILGLXx3xZYdupQbNnjncwntmaFfEFeebAmWE2gAWpS3vrPEKpBKq-9Ly5tFjqo8IBhrdzhr41DArVSbtRIH9EttP5xQQjq-En4ABi2YdBW_tEAVKlnHD5Zp1B0jbxDws_JxaZeRKOe4xlc_Cc5l-sbUdYoy4wVaBFil6hZYGWhjBXtDMbgvi7-zlU8Y0r6KzhdsFn-0ulc2EWu_747VbpOKQf4G6bX1j9OZsD4s950ldmds7DTtcKO6o3LjPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107500" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTItXmAzQjxZirRm2K0vX6hcUMk9EaSRw5fFeh6pp-1X7RtFYmfzNrJ8EFNqH9GYmob5uQW8ObSij3_TwcV-hmNatdir9ar-Nz-oI2VovTxCNc6lFrsKRiQh-kiJ5F23HyVla9_oIb16nwCUuMavkxBL1Fh-15M72hUZHIymUnJK0cfTTJ7FCmWJWEzOh3O8GiHNOnG1WQxx3MSewKcxAFWo2xrvSanBxZtvcmibcoFQuDdLWg9iotFxIqozQNB_x5bVZsVpYM74iWBLEn28yj4X76dIFCFEqF0N9-QO76rDxL-Fo48YabZcHjYksMAbUMBPpoY0_Q2cfARvM_O5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
رونالدو بدلایل نامشخص در تمرین امروز پرتغال حاضر نشده. تیم ژسوس قراره فرداشب با دانمارک بازی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107499" target="_blank">📅 19:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKeOcU2kHSJxP3tTDuyqx_PZxC-c-HJ7u48jAVf01AlBHWuJce8pH-J8j5Q8KyK6yha9QI3g5xOJdSmn89e7Yd5-kymshKRfDguCFV3K0zhXctPMajWM8z5vgM8z3_omMvc-KuFxTgLBpYQFhyzgg8_W1NgVXtZ3VEo8mkSOsHEqG4kvviAgmynT2d96lqOCFG1E9q0x_l9sgKeG-t5aVrAWBkFijiH8N9LBz6T2AV0VrFvgn6upWqYqDZOEcLUenZ0wiBaB9Mb9qOwkPtjI8P3bvep6dyZ4pSZSSrM1nFfOEpai710UfI2hUWdGHPLkRt5oRHH1oNRkRgAqCr2InA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHfq9eIKjUsFN2XgtcgBIlgU8AUCvSi-kLhXzHQKyTCofmVjY1dat9kLSKzncxfDsP_pusRq32BLYxv9RWMRnEtKIjT2rLvkUVINwxDBC9eoVEAciH7WWFLys7B6H7zHENzKgeXGVGuVW-TAEz7JtR9YbqXsq1LL5UMrEMeSYHWKovJEmHO887SKQi-z37awaq0HbQlWRgcZ1uz09GFVEYpVPtHYUFTWU5ssKi2xFPHK7rd7Id5_FVKsR748G7lZN7Ck2ddrzAbpDDPJzLoqsLJ8bj-tLAE2RUhmc1y6NNu7_auV41dU5djzHMIKlgew6qM_gcWU4ok0HTo-m50Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St_nzex2VJ6-6n1HnqeKCfh_Yl9SyPpr9cct2qUOSgqDQK1TPPpgdXprZujGrw5io00SaP51FKJuNufQ2Ni8XpmeHsZcigWAuCg7ZOZp59uhx6I3YSU27tJHQ0wPxxUuf58l_pH89J-v0j2komyu30d0wgVNIoNb2pqCYVVY-7yEZrdCWfrn2ayQaJj1JOgLVw-AX3RXfYzam01Y95c7vDDPuGVKLOLRbHHl_tQjmPzauFtZYX4fIEDseX6aZ7VH9PhB5B1G3pEL6Gr0yfNN8j87BqcANm3aUB4aVUerevYKmDB3q8m8UvtVzK9dzuE2oeD7ryvej07jcPhVJejcNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=cmrbHPqSHakf03_HXUYnxJzmsoPOTcEKt_56Hkm0UPwmVCjsPF1wVH6U8UUtTyrIe06TEvE_cxNsB3h2K3v7rdRUFjkMRRNMgtYJNndJhKLfJF9qsXDIWSxjJJe3FJkd3icAtoUp0pZYBFri-NDIEyfdVGSwwMYh8XppOa6CVU0HFpDZp-jlCOLs_6EWUaNvcO-DAdAsApdiGYhyjWzcnEQKJlGZMmXfccLScdnlIuh-68yA3od8grfjEFXgl5tj66qbHmzE1vhuBaKkYo56QmIE1C3rxZg44ynCwREK5DzcTIl3_BPVp05uulAc8JKqKJSKQkyNs53FLZygAzcq1nxHGr6zfMF2t1j6xqknWHXnVBAGQXXw9cJ1eDLj0g9q1ujJsXhUJPMbiVCTZqBPwur2ZCUNYQiPkBDgrAbt6ofA5SF9D2A-T638wMHlUG6k0N83kW4VGQYNcn_fk0t_vbvjWqzBvU-ctGvNwAFidYAB2QNwtdLQNZO-_VM0XaCfopH38BmTYZnEWt0vz66bokQguK-wjw-M-9rpR2fDdTtDUsxMSgmOMvaGRoH9e97tHaqspqHLjKsnIANoiQHvXclHrRHfISVmDU-Ef3UXNKcKsr7agmja5N7vBqt6H4qbIJ1RrrAtaU8yoQbJWxKYtAaNh4ix8W0xjqeHG0QyAg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=cmrbHPqSHakf03_HXUYnxJzmsoPOTcEKt_56Hkm0UPwmVCjsPF1wVH6U8UUtTyrIe06TEvE_cxNsB3h2K3v7rdRUFjkMRRNMgtYJNndJhKLfJF9qsXDIWSxjJJe3FJkd3icAtoUp0pZYBFri-NDIEyfdVGSwwMYh8XppOa6CVU0HFpDZp-jlCOLs_6EWUaNvcO-DAdAsApdiGYhyjWzcnEQKJlGZMmXfccLScdnlIuh-68yA3od8grfjEFXgl5tj66qbHmzE1vhuBaKkYo56QmIE1C3rxZg44ynCwREK5DzcTIl3_BPVp05uulAc8JKqKJSKQkyNs53FLZygAzcq1nxHGr6zfMF2t1j6xqknWHXnVBAGQXXw9cJ1eDLj0g9q1ujJsXhUJPMbiVCTZqBPwur2ZCUNYQiPkBDgrAbt6ofA5SF9D2A-T638wMHlUG6k0N83kW4VGQYNcn_fk0t_vbvjWqzBvU-ctGvNwAFidYAB2QNwtdLQNZO-_VM0XaCfopH38BmTYZnEWt0vz66bokQguK-wjw-M-9rpR2fDdTtDUsxMSgmOMvaGRoH9e97tHaqspqHLjKsnIANoiQHvXclHrRHfISVmDU-Ef3UXNKcKsr7agmja5N7vBqt6H4qbIJ1RrrAtaU8yoQbJWxKYtAaNh4ix8W0xjqeHG0QyAg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=aIMe2_GZEIQPnyO6pc-DzFoYaU1zqZowkc9M1lM7ud-gxcVBFFims8RwKZ_IHVD_WYyG-MmC2BmRNwJC9I4Q2vvflTH_2bJtUEjHGPgD5_YsiY2KDEBmpr6znFLSe9hmcRHISH5UWZQClBnS71GcIlBb_sXxotJPY9f4x4jJ_ZGaQBuWUlIfeTfqGSXnMpqL-2qwb0IVZCjsw3zagBsKXEkzrznpDOa7sT48Yxyjko0QDYcV8Bsl2BnEs0ChUteuBOk_hUgnTrOOkjM6W6BeiStbSVDaEpKUwkJCzavOsIdgDBu8tqldPV1ZC7usw9Q-G3pMPq5nNFCaepvUf0x2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=aIMe2_GZEIQPnyO6pc-DzFoYaU1zqZowkc9M1lM7ud-gxcVBFFims8RwKZ_IHVD_WYyG-MmC2BmRNwJC9I4Q2vvflTH_2bJtUEjHGPgD5_YsiY2KDEBmpr6znFLSe9hmcRHISH5UWZQClBnS71GcIlBb_sXxotJPY9f4x4jJ_ZGaQBuWUlIfeTfqGSXnMpqL-2qwb0IVZCjsw3zagBsKXEkzrznpDOa7sT48Yxyjko0QDYcV8Bsl2BnEs0ChUteuBOk_hUgnTrOOkjM6W6BeiStbSVDaEpKUwkJCzavOsIdgDBu8tqldPV1ZC7usw9Q-G3pMPq5nNFCaepvUf0x2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=WWhAsSvPI0Bdi0YKNRmz2komBuYXJ3wFgaiVwyq4P8rQ0mtoQHyDaE7iogAsio42GEgxSaVy8OfKbk7AU9dpubSKtxk1lt3mmAO8Ix7PjIdgOTtObpfpmm4xX1rB_ozkpp08natodtQ33G2DoJCV-InGzLcqEa_siE867YrHdDavpHzYkAxURS0fMLTAie7SRV6FFtga1O-8DlIVzqhDrkc_IFRmeAkA7p3kfXeqNZFBhJMdV-l6iAleI9UDiAFffYLZnWLpGT832wZ06jkYF4kGI1CVqQIZ0cl4vneDaKWgIa8QRzZhYc6LjsSwksngmbOjucUb2JPWJ-Jct8X4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=WWhAsSvPI0Bdi0YKNRmz2komBuYXJ3wFgaiVwyq4P8rQ0mtoQHyDaE7iogAsio42GEgxSaVy8OfKbk7AU9dpubSKtxk1lt3mmAO8Ix7PjIdgOTtObpfpmm4xX1rB_ozkpp08natodtQ33G2DoJCV-InGzLcqEa_siE867YrHdDavpHzYkAxURS0fMLTAie7SRV6FFtga1O-8DlIVzqhDrkc_IFRmeAkA7p3kfXeqNZFBhJMdV-l6iAleI9UDiAFffYLZnWLpGT832wZ06jkYF4kGI1CVqQIZ0cl4vneDaKWgIa8QRzZhYc6LjsSwksngmbOjucUb2JPWJ-Jct8X4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=u72q6wxb5ozzS5crWg6A6O1l2tA_qz9aG72IXP0Bva64Dn1WHiuBepqr2UPCvee_KwGx-QJZ3yfJ0YXecWuMGX9ufQN_A_o2rISG7MN-32DLTdO2JToLcSRWnkpFJNWHMh_WJNsaa_nFpgxcye957A0baTS0N5UM02PxeNSui4dIfPIhZJNZ5nOv4wRAVOlW9ajDoZkrNyVUmVhLtzdKZzGvD4CmbHEqgZn98Oicf9rm7OtVP8SQ91U7Rhi7UHhWbyXQflLSpmzQYnB5OaPRN_OXTE8tZE_c-p7Hn1T7h4C47ZOCXrsgALa_rLSEtEopPE-jFqH8Zt8ZSva9ElgxkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=u72q6wxb5ozzS5crWg6A6O1l2tA_qz9aG72IXP0Bva64Dn1WHiuBepqr2UPCvee_KwGx-QJZ3yfJ0YXecWuMGX9ufQN_A_o2rISG7MN-32DLTdO2JToLcSRWnkpFJNWHMh_WJNsaa_nFpgxcye957A0baTS0N5UM02PxeNSui4dIfPIhZJNZ5nOv4wRAVOlW9ajDoZkrNyVUmVhLtzdKZzGvD4CmbHEqgZn98Oicf9rm7OtVP8SQ91U7Rhi7UHhWbyXQflLSpmzQYnB5OaPRN_OXTE8tZE_c-p7Hn1T7h4C47ZOCXrsgALa_rLSEtEopPE-jFqH8Zt8ZSva9ElgxkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=fmi6FO0ab4ktdAI3y8fTzmCDE-2MovJQwKjCr2q8ot8iqxsT6Qp2xD0EZLQruEc64BDnZMCbpB05l9f-HR2NRfj8wQmP19DjTzKXtglVYsSlpByvCrUn_PPcvSfyuprr4OKsoDFslGqlA3mJbgUBKPXJFOIMfa7iqADde58DZIxUvhBFp0Eu7nCK2TBqLf-RtgG8mtrEgHhFS0RgZqucGNI8IRnKb4IaBfg-mz6F29z5mUznhGiUigR-_SXE4ueHRc-pHS_naoM25gMUPHyQaQZv1lb_UrV67HEPvQXNGY06pGvA_1jRyjwG3gRP5YSQ6ijswmZ78j4eRQ1q_utOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=fmi6FO0ab4ktdAI3y8fTzmCDE-2MovJQwKjCr2q8ot8iqxsT6Qp2xD0EZLQruEc64BDnZMCbpB05l9f-HR2NRfj8wQmP19DjTzKXtglVYsSlpByvCrUn_PPcvSfyuprr4OKsoDFslGqlA3mJbgUBKPXJFOIMfa7iqADde58DZIxUvhBFp0Eu7nCK2TBqLf-RtgG8mtrEgHhFS0RgZqucGNI8IRnKb4IaBfg-mz6F29z5mUznhGiUigR-_SXE4ueHRc-pHS_naoM25gMUPHyQaQZv1lb_UrV67HEPvQXNGY06pGvA_1jRyjwG3gRP5YSQ6ijswmZ78j4eRQ1q_utOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdUAxvcPJn5ZeSZZmeV-n9d2rx380bGkiuriherz9deWuPgnQjahC6KO9PrwqDrz9MUBlKVlgmUMPBmc4WoH8ZHYjTmzt72gzFrhvbITgkVZP2359BQnv8QcvV9aVyyowSGAas-HR20Q5vnQiNeDQwcMm9j8AB_-8XgsqKhKlW4s4h9cTm7ymsxsOHEherL_KS_RgJwWCvpYXZuB1EQ6GwLWPg9W1GDRh7bnlz7yKRH20ByXvLgilGxr0YSHHSroR6BHPpxwQ870Ie0RjwyJ7AtPgUTH1H1gqvS6EAUP1DPvPWtZsfNfCJz_Qg7AQLhuiCfQ1q2p0OIlwpTTteN29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=Q--eFy8Eb84IgFIkC_18hbQkcjIOCnPcfoJc5ANlrWkN8Gtf9-lSTFvYuhC-pKaLxqSdqMk2M0vJOS6BBkzxpEyYlfwTF9Oxsktp2rlkg4ycBksVRn177dWUqX5d7-SZawLx79uUgwRKewSmQx_uDab01ENsM4wZ_SjKCwsPlo7AbhCdipncJW-gQEodzx6osLh_1BNSX7pTrVhtaj7BbTXB2MTuSNWKInj-AyHp26-duqLaL1RRHKoHIGo8xq1pkGL7vbj7oxgqXyDMR-rHyqMi-WzyvIBJId4GUspOYM8QE0c2uvFneojLnMxI4szSkABRxnlNaLfWga-SU6TERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=Q--eFy8Eb84IgFIkC_18hbQkcjIOCnPcfoJc5ANlrWkN8Gtf9-lSTFvYuhC-pKaLxqSdqMk2M0vJOS6BBkzxpEyYlfwTF9Oxsktp2rlkg4ycBksVRn177dWUqX5d7-SZawLx79uUgwRKewSmQx_uDab01ENsM4wZ_SjKCwsPlo7AbhCdipncJW-gQEodzx6osLh_1BNSX7pTrVhtaj7BbTXB2MTuSNWKInj-AyHp26-duqLaL1RRHKoHIGo8xq1pkGL7vbj7oxgqXyDMR-rHyqMi-WzyvIBJId4GUspOYM8QE0c2uvFneojLnMxI4szSkABRxnlNaLfWga-SU6TERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_zGGcgK3U8WdjO9AIEffKM6XbvJG_jrUuHZOmr0IxdEwyQAdvy1gTgapKLIevQGCzxYExIv4H17KMkqep1oT126q00eyXpaZtmGB5APufkW8zeLeBkR9IndnPhyvlfUZ8A_vmv60Fq0Ptujs1gJ_ZjgE2Fm_GxjJOIUVdckjrv3S62gj39ZB04r6BHi4l6yuowLFXPv_mZ6PEoA3bT9hY4-IQgmJjcJk0Eb9fj4mqTV__dUt5fKfKwOlE1govLovJKUORsUiFCKSv7RagWH66n2-dX5PY4oxkEwrGsPMcoHROOf19kQP05nxo6gZXAa0aoAj8J1t5WKu5kaSLFw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=s2JxWsAvpPyH8fBYfsNVO4vcnQ-sfXTvUFgZ_mzWvTbx7zsIrA5iqeSAkdr31GFxAq5AqqHuvWP3OuX9MH0HAnzDDmhcjXSvtuRQrCVo1VfZn8GqRAJETWfdn8cqBRGlVpSYcmILBxFIyaG0vkRNBwhGCzXEop1DDAlqdNuIAJ1w4j60RwhI86tQ4nT75OGfolYzleNL9ZCQMYQ_i6X83Kl9fC55DItJXpJJQxccV-lRkzkduAWxiDq-1gsoJScW-tMf8vaMQjerYYMuNcuYtbUjIPrC0ZURUbxmpp_zjrBpwPlslTkMdWvvVhprZ_Teb9DI2s5N9yFkXB0Hh9U_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=s2JxWsAvpPyH8fBYfsNVO4vcnQ-sfXTvUFgZ_mzWvTbx7zsIrA5iqeSAkdr31GFxAq5AqqHuvWP3OuX9MH0HAnzDDmhcjXSvtuRQrCVo1VfZn8GqRAJETWfdn8cqBRGlVpSYcmILBxFIyaG0vkRNBwhGCzXEop1DDAlqdNuIAJ1w4j60RwhI86tQ4nT75OGfolYzleNL9ZCQMYQ_i6X83Kl9fC55DItJXpJJQxccV-lRkzkduAWxiDq-1gsoJScW-tMf8vaMQjerYYMuNcuYtbUjIPrC0ZURUbxmpp_zjrBpwPlslTkMdWvvVhprZ_Teb9DI2s5N9yFkXB0Hh9U_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldTTmBV6UROAubrAuykA04Pn-iLtHMsG8WIRzksuA26zcEJIfF5HcWd67H3ls-ZhohRa70mAvuAOK009qTF5VaaUoip2vHFmKAhYtJvlSa_3bSZ-GFoaB_fjCDU6NZwyyRJzePyJdpOtetmqa5pAG4Oy3obROAanjeY4kxZhthw_kOTjJXLPCw6ahQvC0-hohC9H1uo5oOLxwaxj2Ou3eAQiEcwvEsjjlpouqnI3-YVFE5hr4dYUDSTFVLWX-_sATgv1cGV6X5a_7p9OfOSkNSywzAAalFbwAnZtXQExbQDW2zGp_jbyCLkwmr3X4q4fjy_1-ErUv6MAUNrHXdTGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3x1S-jmUG9R_c79FdFYr1CLfUUOJWQvIIKlltvgg4qtWjwdy255zsCqD6DHO7zIqAayzB6yHGaEnP8sAPgHr2fRIXB1inqGBTmQIlmsJSSbyefPEZzMsRKykitOgO4lr2VnhiWoIVczZerz2wckKVhod0WF-mKnEkUvgQT9FkaPwp4aY6F1wnwszz8q7n_vaHjDWwDyUUBdLljedxB1TvI0VIzQb_yDfn8ivP2bXfJ5DEmzrcccxT3QYPXYLzABcLacAEaYTKd5bCtZpJpGUDTPusQjpKgzApyjwlYzv727kGK0o7j8KKGA8XSjtJAf7C9VvJW2LSVyrYuW2LEiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti799Yx3lu0kIO32Vr8EWd_6INaKsUIYsPVFZYOydx4ept0AyHk35XemnpLDG6Q51aXwsliYFw3s_kUMgQHQHydtGZF80Zl_kRNFqWr6jju8OKAs4J4yXiZuAk4ZvKRbUBCXxZOGxE-8hNUkz6z0YWtYfeoAgyC213x-zQJ5q3LDWwGkb3Jnx2CVHoqEsnf_d9gSimUzLfegk_oaW_qvA3PKTzliS__WfqrJ7e3P54O4OCmMOkvSPMMvgsdG_FDZDzT1V1KDfaA18czHisvzSnYsten3t65s1R5BLruZO-qxWNipNO8kBZJg0grcLuvkJMldz59J3D5Ll0YrJRJk0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN__bDkPpO_RqEPRAi2WW_k_5U_bbNfeP7el7R9c0n5bn3tqnF4UChrJ_ZSOmoPQC3uF1_bnGWMRH5aClm4YdqE9-DrEEaMrJwg28vWCnJdyYengaZQQUT7eYaVkrQ_qPhTDyc-3tmpvCjb4kBqckeuo2Ks3tIyUjWseg5cB4uxw5DNBbKC2oTrqrzzRfjiujXthSQdn_wJ9ZtUodRjpURizjk7tfDy2OEZ4ZshLECBJF-ammoezn1-8jfk6dqEVQ2R0Fzvz_HROHTQuGi3VvCN8ndME1b-Yn0AeAs0ETEPNHXx95_jpk3e6b0q4rHsXcUZnQRtMVlX4wRnKOPsYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=XklZ6-zAh9ofC87Z8htbt-uRibSSYtQNPZpLueaTS4mjaJ7xJ19mb-VTBcNusYeQ7_4KrJY4WGW6SZxvqJ2EMaaav2GOunOCJyNpquRlx_-CFjj8NnnZvfccRMmx_JJ1rMCOBMhXJTGJdTyzSaDZM2kKgMNLzOOEMv4oddVETJHMGGSgEaZFkwRcJc97pPAnKfGyAExunWhyhb8nMRLM0-ryY5u1pPFyBTvoId4sU6p9PTOaBw-hOHsEPTHu1NJe9Duti-weNe17jb62iZLJDZk5cC6_z3tFuYLdTyitkW_ycw2PTvcqEw_E_tcX0r2VVJny9P2RFRdby8QUx_cX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=XklZ6-zAh9ofC87Z8htbt-uRibSSYtQNPZpLueaTS4mjaJ7xJ19mb-VTBcNusYeQ7_4KrJY4WGW6SZxvqJ2EMaaav2GOunOCJyNpquRlx_-CFjj8NnnZvfccRMmx_JJ1rMCOBMhXJTGJdTyzSaDZM2kKgMNLzOOEMv4oddVETJHMGGSgEaZFkwRcJc97pPAnKfGyAExunWhyhb8nMRLM0-ryY5u1pPFyBTvoId4sU6p9PTOaBw-hOHsEPTHu1NJe9Duti-weNe17jb62iZLJDZk5cC6_z3tFuYLdTyitkW_ycw2PTvcqEw_E_tcX0r2VVJny9P2RFRdby8QUx_cX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=Uw1FHV8t8bILy5hsCw3M-2BMjjxYfoAoXlfSj5mr3cQDGCwMMvb7LmrohtUHPGORQL264fGMthi8GgTT9i8pZwxj1Vh7CWwfigqjBd9NtSed1TpyP6kf80nxRlih5Ym5wvkCaZNtu3qRFB7kjtz9AENZBYAhEJIG5jpQR3sNC81HQBKB4tHiZEHal0_jWOeUl6KQJjQscFz4MCrLWK3QhhkHsvkTpnwqwA0PeWiTFnWuap_fCRj_6fvX1q8D0pTkgUUlrYu25lTGoZo64iQHjDTfRbwiH2uPxevZ9giNcENk9-o90zKwI0KPA0HIkUVDfuIATQuXwZy0CmDr_DDgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=Uw1FHV8t8bILy5hsCw3M-2BMjjxYfoAoXlfSj5mr3cQDGCwMMvb7LmrohtUHPGORQL264fGMthi8GgTT9i8pZwxj1Vh7CWwfigqjBd9NtSed1TpyP6kf80nxRlih5Ym5wvkCaZNtu3qRFB7kjtz9AENZBYAhEJIG5jpQR3sNC81HQBKB4tHiZEHal0_jWOeUl6KQJjQscFz4MCrLWK3QhhkHsvkTpnwqwA0PeWiTFnWuap_fCRj_6fvX1q8D0pTkgUUlrYu25lTGoZo64iQHjDTfRbwiH2uPxevZ9giNcENk9-o90zKwI0KPA0HIkUVDfuIATQuXwZy0CmDr_DDgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=kOkRYN5EhZCd29YJM4giNvdb-7XGTPXAkoL7a4C0nzHCt_Za52YoDnAeEXt7_CSGGUt4jYlaeE1cPF2vsHrYtsg8BhFCVvbO9xOngkAkWyBRocXUDfNQLX2Vr9FA7eUExV8arsynUVJ3FEEwUGENq1VU7WmRNngKzZiZGNnaAYOMCeMlalDhxJOiJp1EwcYXriz3UDJBDsqrppour97pP7AWJ59SkuMge-IQVz7VijLa5rywl3teVo_zv4Xopjw7svcY6BYnTjhTSifdw0-RYLYp5qtTOLoBnleHXPWRAqJCxqmovbYxKf54WrOW8iDzO_lF1npe0AWWKU8VdV84QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=kOkRYN5EhZCd29YJM4giNvdb-7XGTPXAkoL7a4C0nzHCt_Za52YoDnAeEXt7_CSGGUt4jYlaeE1cPF2vsHrYtsg8BhFCVvbO9xOngkAkWyBRocXUDfNQLX2Vr9FA7eUExV8arsynUVJ3FEEwUGENq1VU7WmRNngKzZiZGNnaAYOMCeMlalDhxJOiJp1EwcYXriz3UDJBDsqrppour97pP7AWJ59SkuMge-IQVz7VijLa5rywl3teVo_zv4Xopjw7svcY6BYnTjhTSifdw0-RYLYp5qtTOLoBnleHXPWRAqJCxqmovbYxKf54WrOW8iDzO_lF1npe0AWWKU8VdV84QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد نصرتی بازیکن سابق تیم‌ملی: آقای قلعه‌نویی آن مصاحبه مهدی‌قایدی را نادیده بگیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107470" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=Hmk3Oly0hJ2mpAOShKOmljThRQETS8V7sXmGUJWveHblAYhxsnZe00JwjiU5ZQLnKaoK4FlPp0Xde6RiZTxPv7XbjsEvOJGV3q-neX-Or4rllS0SdOVx3ZIWxPA2G3lxPvsCMiPK-_AuAeszNdpK8T6LMMz94WDcb75-8P3JRLmKas1vXjp__bt-scnSgV4eoCRkFtyq1PvJj4TVcHbImbu23rCXYvO5ghWTrSXyB2RQZ02m2w1mDrtr-3c0ZVn3r33FyZ9x7vGg_YgSjieqD6hCkKVx7Tb1OoGoyhDkOYpn8N2ra_4bWErdohMdk1Yng3Kz0loDODN1XknAskBaOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=Hmk3Oly0hJ2mpAOShKOmljThRQETS8V7sXmGUJWveHblAYhxsnZe00JwjiU5ZQLnKaoK4FlPp0Xde6RiZTxPv7XbjsEvOJGV3q-neX-Or4rllS0SdOVx3ZIWxPA2G3lxPvsCMiPK-_AuAeszNdpK8T6LMMz94WDcb75-8P3JRLmKas1vXjp__bt-scnSgV4eoCRkFtyq1PvJj4TVcHbImbu23rCXYvO5ghWTrSXyB2RQZ02m2w1mDrtr-3c0ZVn3r33FyZ9x7vGg_YgSjieqD6hCkKVx7Tb1OoGoyhDkOYpn8N2ra_4bWErdohMdk1Yng3Kz0loDODN1XknAskBaOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تشکر هانی رامبد از مردم ایران بابت‌ حواشی اخیر: مرسی از حمایتتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107469" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-GBnZzzlf2SSZH49BQwO2KG5kCXwTurHFL2_khqJyCOvaZX3TJw6jIAOogQpexfbcnqz6m9zIoUrWXVGG8KtaF5HYFOI_QX3rXad2wRWgKJS2nx27j4JdoHUndgJQIVa73K9970QvAM5QbN61gHTcGrjlLdMN68S8VGvaizOW47nnKO-Wq_aojvtvhaNHaPPnElZE-tr2Kj5thWCWFwQlEQf_xmvGS89iRCxlPLfVS6FrL9UcL1G6PIl9S01oTOUi5BvTTc4TyfTR8V4T-a5KZjhN39IP3aOdaitElmfrwH_4YQMRqHlrTW-NdpoR4UVaZLXW2CrK2eHYs2Os5pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‼️
تیم ملی اسپانیا هیچ‌گاه در دیدارهایی که لامین یامال را در ترکیب اصلی داشته، شکست نخورده :
🔴
۲۹ بازی؛ ۲۳ برد؛ ۶ تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107468" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=d1Job2AGtSJofN6uloRB8GRYGcSXPaP5n3hg_L6A12qodDFDE2riYAip0jyEwAWqZy_m-ML50_l4h0qr6c5HDz6cnk-L8FzeF51LKJJhiWoKP5_R-FvoAHvjnD2sbatSg-ooDC_7zELAUtpJ9FuCK5JgR7VXzNNYeSomk0utMsX3H-RnS-ohfovUlxOj9QxB_SMqFAH0ILXgNFA5rMiu9Q6pKFdUlEySJs_EMvjZ52FzD1LBhZ5jElZEyLP-3hxEj05ETP4wkKT8EOgo6tLlPquEqoz3fZT4JrW1OSfjFdVItusMRs3c5y55pF_lno9LKxcALul4iv0x2pPoMbOXnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=d1Job2AGtSJofN6uloRB8GRYGcSXPaP5n3hg_L6A12qodDFDE2riYAip0jyEwAWqZy_m-ML50_l4h0qr6c5HDz6cnk-L8FzeF51LKJJhiWoKP5_R-FvoAHvjnD2sbatSg-ooDC_7zELAUtpJ9FuCK5JgR7VXzNNYeSomk0utMsX3H-RnS-ohfovUlxOj9QxB_SMqFAH0ILXgNFA5rMiu9Q6pKFdUlEySJs_EMvjZ52FzD1LBhZ5jElZEyLP-3hxEj05ETP4wkKT8EOgo6tLlPquEqoz3fZT4JrW1OSfjFdVItusMRs3c5y55pF_lno9LKxcALul4iv0x2pPoMbOXnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
پرونده قهرمان فصل نیمه تمام؛
جنگ بر سر جام نامرئی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107467" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE3-sdZ0fVOIWppI0eyApRWx_HuRiccUpsnmaiC3ScBdxShDpjUD9-zu0XePHj7TDI-YYoQtSXUxWe5nGgOyjZuzOkd18HFfj8lSPWxD6CnpfO41U-RpnmGCUs4TodqZnTU-YIrLUV1oAG3cIsvTLcWxbIT6AuvM5-OV8vYASMdmPbinr6biR-CXWT59rnw_NiG9NafuPGXImPbhzx05jIqDUgXIhVWwiCH3JbOi_g7kcPfMjX_tme2wAQj83LST52aXWAlG5UIE6-hhAA0dUessfxSloEFsCsZ1vbzdSXNeIomIRJDFJAq8ZeCKpytuDvBZBWnW1rZcQWbkv34_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=G6Q3GMxRDrd44HbDtvGHqlp3PkXl1PIHw7pSuUHcGT7Hbuoya5tojwD71qjP_DjUic9-PUP6EwT65Bz42l1ycyqiLEqHuHpXYCig46bwXUKSy8fcVXxezqLbHVtwHDusNbudy_-5f4HHpQ0ta17bEmLHivN_a2hlQr6ZrOpKfjZzafqaAogL52fcjQgeDLwzbll7yW1FDhK_1hMSQjgH4NVHsS0QBRG_251SMzYnlU1MU2vwD6x6ImZzCUwXE9IP38M8F6CSgXF4XqYiIINdex9w7v1WtVSwq8T9SB4pKi9CocwVxgon2S08lkNlVcqASAaNR2SLVfL42qC889XdeJApswMpp1ycpLvaTYAVvBDDV3f9pL_-fcLSEiF-SAJcTSFcneUytfxlCUOlqqlZA_RTVZl_Ebv_grG57Av4XlbiE8zVWD_wtBYCQ8pYaSFtUi0bskiIdk1JngbIY6HZNhUYvQ2_S0kRsd0eTJE9SwefG34O9Fhaw06aWuILaErRXAHAumv2mYhFUNRIWp-sh2vD3h3z8wEZghkZE2Bp2fQkhxF6ToaO4H2Zx5pBD-ZBqLs2bm6ufDNGAUbl4HKxh9Qu8uHPfeHMYviX3PxgQuqVW94y64Q8_9Jd2bsfO4nvoGJMtGywZoEU-XraoBN9Zfc95TJQAHDEEaebTQU78ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=G6Q3GMxRDrd44HbDtvGHqlp3PkXl1PIHw7pSuUHcGT7Hbuoya5tojwD71qjP_DjUic9-PUP6EwT65Bz42l1ycyqiLEqHuHpXYCig46bwXUKSy8fcVXxezqLbHVtwHDusNbudy_-5f4HHpQ0ta17bEmLHivN_a2hlQr6ZrOpKfjZzafqaAogL52fcjQgeDLwzbll7yW1FDhK_1hMSQjgH4NVHsS0QBRG_251SMzYnlU1MU2vwD6x6ImZzCUwXE9IP38M8F6CSgXF4XqYiIINdex9w7v1WtVSwq8T9SB4pKi9CocwVxgon2S08lkNlVcqASAaNR2SLVfL42qC889XdeJApswMpp1ycpLvaTYAVvBDDV3f9pL_-fcLSEiF-SAJcTSFcneUytfxlCUOlqqlZA_RTVZl_Ebv_grG57Av4XlbiE8zVWD_wtBYCQ8pYaSFtUi0bskiIdk1JngbIY6HZNhUYvQ2_S0kRsd0eTJE9SwefG34O9Fhaw06aWuILaErRXAHAumv2mYhFUNRIWp-sh2vD3h3z8wEZghkZE2Bp2fQkhxF6ToaO4H2Zx5pBD-ZBqLs2bm6ufDNGAUbl4HKxh9Qu8uHPfeHMYviX3PxgQuqVW94y64Q8_9Jd2bsfO4nvoGJMtGywZoEU-XraoBN9Zfc95TJQAHDEEaebTQU78ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=CjY0D_Hqx_43bxI7PBhx1bUmcX52WCS53Z1cIKdy1kawvbiZpRuAim1mGOVRfuPX1jr5N_eFJ82MDYlqkQa5n3AfKgTEUNhaR7ruFVMirZ0VWFM9q5rJrYftu4WhgJ48_1_jAFplj-Zqw-xCvlWMDI1fbKyRt7cj1pvo9ecunOeHnkS4d6Rv5GCJZ_1-hzArwAFyy6dCHUq4SXMKTFsdKSxJyCr3KodyqBFyFsq-qp4ZIfXvN2vk-UZgB6v3bP85Bw7BAHyOJUBljxFvKJ0XWaRyl6sUwaz3AQKm1aCUyUP83A4YCyFdFS0QQXi5buN8I9M1EAnmIwM0nNL4H6wbsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=CjY0D_Hqx_43bxI7PBhx1bUmcX52WCS53Z1cIKdy1kawvbiZpRuAim1mGOVRfuPX1jr5N_eFJ82MDYlqkQa5n3AfKgTEUNhaR7ruFVMirZ0VWFM9q5rJrYftu4WhgJ48_1_jAFplj-Zqw-xCvlWMDI1fbKyRt7cj1pvo9ecunOeHnkS4d6Rv5GCJZ_1-hzArwAFyy6dCHUq4SXMKTFsdKSxJyCr3KodyqBFyFsq-qp4ZIfXvN2vk-UZgB6v3bP85Bw7BAHyOJUBljxFvKJ0XWaRyl6sUwaz3AQKm1aCUyUP83A4YCyFdFS0QQXi5buN8I9M1EAnmIwM0nNL4H6wbsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=E95PpUd_umuNwK2vgaHBzggJr2WlajWskiWS5ZKnTXO0BF155g99LLmIcM_5gTUaCPYer6ZVFwr7m0q3YUSSXY3WopZfL_BsMfwh96acbz-JGiJ5VlNvAj-GxrX9PP9jussJIvo55IafVF6HtgfQSDhUGHlPRuoeY0N6vMwIQB6IXvGCxK8EAlckBrSg2hBKWbiz2IM3FNlkIpQFkbvQHreXV8jK9_LnpaKblFbk7LHUOLBEEdvlwujWnPmx6OfREbQQYnZ-k-y_JAKZH5zbKSvSu-Ti4ZVFuIxV63L-5iwzpY6tzwFRt6eDSFtM8FNMgsfUEos5-dOvHNo_Y9aNfoTQJUx-zeXse_mOkkHeiN3CCU7tyCRFjCl_P-p7gvjXaEJuvyF9PsoUQwGVAIHdo3aJuODw5ZyKteCRO2XAkNJLqEvtpsvL_32xVviS9_eH-F5_mbgknqVb7afAiI-gPQxoV8hOvoj5v6azgAz4KbuICNkzKwr0uVBQjvRQQ63nH5aI3qpOYYEOkuDTE-v12EMiEZNAOUy4_g7vIIfMyCm9x2e8sj6KyNpNdElGxyTa1-XIEyeSkHv_M8HZfKRHGxUZ3wz-unTWv4l6bqSC_BgxpiK9Ik6Zn6Jriw8Uzemz5t48KSDHxC4Xrrh7scrWqELt1VNFUtAE3ZWpQvm-LS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=E95PpUd_umuNwK2vgaHBzggJr2WlajWskiWS5ZKnTXO0BF155g99LLmIcM_5gTUaCPYer6ZVFwr7m0q3YUSSXY3WopZfL_BsMfwh96acbz-JGiJ5VlNvAj-GxrX9PP9jussJIvo55IafVF6HtgfQSDhUGHlPRuoeY0N6vMwIQB6IXvGCxK8EAlckBrSg2hBKWbiz2IM3FNlkIpQFkbvQHreXV8jK9_LnpaKblFbk7LHUOLBEEdvlwujWnPmx6OfREbQQYnZ-k-y_JAKZH5zbKSvSu-Ti4ZVFuIxV63L-5iwzpY6tzwFRt6eDSFtM8FNMgsfUEos5-dOvHNo_Y9aNfoTQJUx-zeXse_mOkkHeiN3CCU7tyCRFjCl_P-p7gvjXaEJuvyF9PsoUQwGVAIHdo3aJuODw5ZyKteCRO2XAkNJLqEvtpsvL_32xVviS9_eH-F5_mbgknqVb7afAiI-gPQxoV8hOvoj5v6azgAz4KbuICNkzKwr0uVBQjvRQQ63nH5aI3qpOYYEOkuDTE-v12EMiEZNAOUy4_g7vIIfMyCm9x2e8sj6KyNpNdElGxyTa1-XIEyeSkHv_M8HZfKRHGxUZ3wz-unTWv4l6bqSC_BgxpiK9Ik6Zn6Jriw8Uzemz5t48KSDHxC4Xrrh7scrWqELt1VNFUtAE3ZWpQvm-LS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
توضیحات میثاقی درباره شکایت اندونگ و کاریله از باشگاه استقلال
⚪️
محمدحسین میثاقی: در این هلدینگ خلیج فارس یک نفر نیست بپرسد که اندونگ کجاست؟ چه کسی قرارداد کاریله را امضا کرد؟ آقای تاجرنیا الان وقت آن است که مطب و آپارتمان خودت را بفروشی تا سهم خودت از این اشتباه را پرداخت کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107459" target="_blank">📅 00:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=On0Ah-oDBrFuNi8Pjh0ShNyYTbpxd0wV_acrJcejWS0rwiKvURN0mSj3baWVbQ2IRvW6TimzCGCUolk6qub0-VYNNV1ceFUHDQsDv3K6uIPAyObpQMKUuz2amASsoWQ_GMUykB5xhC81O3ogdM9B52L5Fh20KF9GIPe0K9C4fn0RgcO3sbp034GEEDzAjQWXHiYHyBKMarujw38bL43jZcoVW2oWNEdVVmrgAUu6An2n8sLE6sv2X_HFsEDO42TzAc3FwfzVvNkQMQ4EKzEHBfXfgT_IsT_44uRH0GqKrkBEeeE7CNDOcsVAePG3bS83NGbfYe6fCV2MX5aClyw50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=On0Ah-oDBrFuNi8Pjh0ShNyYTbpxd0wV_acrJcejWS0rwiKvURN0mSj3baWVbQ2IRvW6TimzCGCUolk6qub0-VYNNV1ceFUHDQsDv3K6uIPAyObpQMKUuz2amASsoWQ_GMUykB5xhC81O3ogdM9B52L5Fh20KF9GIPe0K9C4fn0RgcO3sbp034GEEDzAjQWXHiYHyBKMarujw38bL43jZcoVW2oWNEdVVmrgAUu6An2n8sLE6sv2X_HFsEDO42TzAc3FwfzVvNkQMQ4EKzEHBfXfgT_IsT_44uRH0GqKrkBEeeE7CNDOcsVAePG3bS83NGbfYe6fCV2MX5aClyw50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
⚽️
خوشحالی فوق‌العاده زیدان پس از گل پیروزی بخش فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107458" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=dMt3F_Ytc0XrlKfMT-UdzXRXOoScpXBwj6RTv_kZZz2LTNxLm2Vgn7Ta9vw8RHA1KuOaW00ChvaggULbpAyw6d_xuQb5b6y2xn0BUalUrrPpRjbZ5REWXiN1M0zDEYPpUdwdkTMnCCGcngpMdKFC6EwRWEdN6LTFe_bMwicFS8CneXplHIEegl6XRCjFqtQMR6XaK_TuMIg0hc0qx0Gaofzq6BaymIx938MEwMkmpCyvmeCRYJwL5odpWwA-3dGSVsavCw3aY4asYslJk74CSu-eiDXz9Co6Bfrszg1Ykn02YhkjWoXbWR0jsdbOsJ9ZmiglB_tnjXxXc9e23k0Y0gz5-fsRW8bkbleZpqUJnMzWavGvgPHSZqtuM1W-a4XzV46fgO7CcDS43wchEAR8wBmYOmRz9VbNFIHSB3NaVQZLzYTg4d6iWMymEuapxuUCCHnbES53ZhsDz8Y9Gt1g2HBSyPq2rIQXhI4KpOVB2qAJFB-42iy3zwkeMAs5p0zzhs8sK4yB1caqCUZjArW_5GGBXxDMAA1T4UehHCOhm8vQRMbyxZ_JL2-gVkwT-JSPo4P-XoLFYJ67izmXNVt5q4VyrKpllRD5PKd1qiDTpCDxnVCiWQymjLZOPxp4ifpJkb9twzgc4kVZg2TZLDEbYoT3XrnrPEX0nK4YiZTFyic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=dMt3F_Ytc0XrlKfMT-UdzXRXOoScpXBwj6RTv_kZZz2LTNxLm2Vgn7Ta9vw8RHA1KuOaW00ChvaggULbpAyw6d_xuQb5b6y2xn0BUalUrrPpRjbZ5REWXiN1M0zDEYPpUdwdkTMnCCGcngpMdKFC6EwRWEdN6LTFe_bMwicFS8CneXplHIEegl6XRCjFqtQMR6XaK_TuMIg0hc0qx0Gaofzq6BaymIx938MEwMkmpCyvmeCRYJwL5odpWwA-3dGSVsavCw3aY4asYslJk74CSu-eiDXz9Co6Bfrszg1Ykn02YhkjWoXbWR0jsdbOsJ9ZmiglB_tnjXxXc9e23k0Y0gz5-fsRW8bkbleZpqUJnMzWavGvgPHSZqtuM1W-a4XzV46fgO7CcDS43wchEAR8wBmYOmRz9VbNFIHSB3NaVQZLzYTg4d6iWMymEuapxuUCCHnbES53ZhsDz8Y9Gt1g2HBSyPq2rIQXhI4KpOVB2qAJFB-42iy3zwkeMAs5p0zzhs8sK4yB1caqCUZjArW_5GGBXxDMAA1T4UehHCOhm8vQRMbyxZ_JL2-gVkwT-JSPo4P-XoLFYJ67izmXNVt5q4VyrKpllRD5PKd1qiDTpCDxnVCiWQymjLZOPxp4ifpJkb9twzgc4kVZg2TZLDEbYoT3XrnrPEX0nK4YiZTFyic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری
باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
محمد
حسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107457" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b959785a.mp4?token=fD3XTj20Gr07wLgxti1W4KmQXLe7lMiQWmASU7nFqProyjjywe5Nv4XKcAen4SMCuJiLzJzMsPruV84Z-2bbkrtrtgO3DUowf0Fgqr-sO-N8SaRGa81IJT8Zk1XuAGCSjwogWzk8HBop2OpOK8CUFXxqIFd636O46l4tzCw3f3HAh7depzuHKwNFwlTHiClZYHlLq40Zy-RVQ7KFMXKg_X_ze2_4O4LNJWd-y00nXFhS6nA4FcNLkNrRy-jWcj6GfBHUtNPG0mAOvRf2f-AmlV2JbhpMNQM3V-ysp-58wL7MJwXssedfST1V6gbP6sy7XAYHMgfgpvIeOkHzn_r3k2SYwEGcK7dinT0kZHEqQr15OR1n28dOxj7LuMy51c7hoEyDtWU57sCS7r3buY9tl2VGgdA95T8hMzYJHm9dBQx-UggYWU4p1l4Q9Pb9poK_OLD9Rt02ydnEFItMi7t1YknEYTmtkXGoXYcjOb5-ybxJddQC-2JzbmQsj9r_F4cebhIbBkUZ0s07bmhfDxJtf1MK4YuQSYL8l3Pd0pe9NBWDw32On1tmxHvC9CZ2scWG3AAEOAqyQNzRuYk1jG6J7vRUWGf1Q8RSVZZjaT6g7X3PRfD4tXmCIJlCTceh9q9Z-Uy0nKkd1vmRQ-KeDjwK2lvK6KT-lfGBO4jveQvYkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b959785a.mp4?token=fD3XTj20Gr07wLgxti1W4KmQXLe7lMiQWmASU7nFqProyjjywe5Nv4XKcAen4SMCuJiLzJzMsPruV84Z-2bbkrtrtgO3DUowf0Fgqr-sO-N8SaRGa81IJT8Zk1XuAGCSjwogWzk8HBop2OpOK8CUFXxqIFd636O46l4tzCw3f3HAh7depzuHKwNFwlTHiClZYHlLq40Zy-RVQ7KFMXKg_X_ze2_4O4LNJWd-y00nXFhS6nA4FcNLkNrRy-jWcj6GfBHUtNPG0mAOvRf2f-AmlV2JbhpMNQM3V-ysp-58wL7MJwXssedfST1V6gbP6sy7XAYHMgfgpvIeOkHzn_r3k2SYwEGcK7dinT0kZHEqQr15OR1n28dOxj7LuMy51c7hoEyDtWU57sCS7r3buY9tl2VGgdA95T8hMzYJHm9dBQx-UggYWU4p1l4Q9Pb9poK_OLD9Rt02ydnEFItMi7t1YknEYTmtkXGoXYcjOb5-ybxJddQC-2JzbmQsj9r_F4cebhIbBkUZ0s07bmhfDxJtf1MK4YuQSYL8l3Pd0pe9NBWDw32On1tmxHvC9CZ2scWG3AAEOAqyQNzRuYk1jG6J7vRUWGf1Q8RSVZZjaT6g7X3PRfD4tXmCIJlCTceh9q9Z-Uy0nKkd1vmRQ-KeDjwK2lvK6KT-lfGBO4jveQvYkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌تماشایی مایکل‌اولیسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107456" target="_blank">📅 00:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=QMkgoa7hFC_I_yyVjEQaFhhoQIL9M6lW74KhJ_BMb4Eqlf9-JxM8JdKx26Kfe0mEKLszGbfXqIAfRUT4k7_b1LNpjPQ3HbrZpcnjjmzTWdenqNocf-FVLrMwEYUjeLBhXFryheFNsHjJRK1cX1G_mgrwduVprtH-EbbvYn9n5wKucTB1VnTWedvXxTDNNKFrHcUDqR2F-qsCoyh50MsD_piUNsdVDbEw56wmB7tf4OjPT817ugvwl5_XqhIJQk4MNu5gq2mJOWGvdncqdt4KQ6vrvhGdyyopYpn09IjZiVB-GsnyL3BVjolHd2lVppz4PoqTcI6SZRukGQ53rvVz6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=QMkgoa7hFC_I_yyVjEQaFhhoQIL9M6lW74KhJ_BMb4Eqlf9-JxM8JdKx26Kfe0mEKLszGbfXqIAfRUT4k7_b1LNpjPQ3HbrZpcnjjmzTWdenqNocf-FVLrMwEYUjeLBhXFryheFNsHjJRK1cX1G_mgrwduVprtH-EbbvYn9n5wKucTB1VnTWedvXxTDNNKFrHcUDqR2F-qsCoyh50MsD_piUNsdVDbEw56wmB7tf4OjPT817ugvwl5_XqhIJQk4MNu5gq2mJOWGvdncqdt4KQ6vrvhGdyyopYpn09IjZiVB-GsnyL3BVjolHd2lVppz4PoqTcI6SZRukGQ53rvVz6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
امیرمهدی ژوله جایگزین ابوطالب حسینی شد و برنامه فان فوتبال 360 رو اجرا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107455" target="_blank">📅 00:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=D-uqvXWGNWchpSoe2uJ88elrEEzXfZ6G0blowIaEjEwBDSznj_2jQ-zEmK-dfwqKlqGgphUL2FYm1721Gd3EYGjY-DkkwQ1HIckoQSiaARg-F1XMtbABOy3ry72IDixGTYVkKR8b4IdurYaYAOlHKcbpn1WEu3Cge5GSGXgVfePMVcQEO02PMaPHk8lXdsKFCF4wOQLTYZkjj7nlzOYz76i460I0oV718gdseuU7MdnrkNMD5ibkSo18nXnO4-yCHOrqGxaWuqmpgqlVyfmRSA8XoB2ZDiXxdgl8BftYImvcAKDF7VJcekEhujfHbAaVpCX7Q-Lau8MXJ-z0jKUijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=D-uqvXWGNWchpSoe2uJ88elrEEzXfZ6G0blowIaEjEwBDSznj_2jQ-zEmK-dfwqKlqGgphUL2FYm1721Gd3EYGjY-DkkwQ1HIckoQSiaARg-F1XMtbABOy3ry72IDixGTYVkKR8b4IdurYaYAOlHKcbpn1WEu3Cge5GSGXgVfePMVcQEO02PMaPHk8lXdsKFCF4wOQLTYZkjj7nlzOYz76i460I0oV718gdseuU7MdnrkNMD5ibkSo18nXnO4-yCHOrqGxaWuqmpgqlVyfmRSA8XoB2ZDiXxdgl8BftYImvcAKDF7VJcekEhujfHbAaVpCX7Q-Lau8MXJ-z0jKUijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
سوتی سمی عادل فردوسی‌پور و ریختن لیوان آب روی میز که با خنده‌های آسانی همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107454" target="_blank">📅 23:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=GJ_DlhqssqT-5jpimFzlzxgowcQZrIApHATmuB8OWdWGrz_pSko7ji7IXqpjily87pfL7M-e4e8aHrnWrlhQAE9itKeNNa2ycktfG_PbiKBKuHS2xXhx4REAv4pwssNGO32zg3bwlaAZMVUMuCkV-6ug-NbFwusqZu84Y2W_MF2NF7FQxczQJ3LTMByH_RnxAsOJSWq4XQJvbIN06w4iMzKn-ArCcy4D8rR0EU6yrospjN2FtS_-zS7dU9jf_lwvMdVxXWOOU9V7MmutLbjK1AxfalrF0Xm6ouG0_deASeBgTmzfMztLZihNk3VlQH3sQc9GtcfU9XqecYpHl1qwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=GJ_DlhqssqT-5jpimFzlzxgowcQZrIApHATmuB8OWdWGrz_pSko7ji7IXqpjily87pfL7M-e4e8aHrnWrlhQAE9itKeNNa2ycktfG_PbiKBKuHS2xXhx4REAv4pwssNGO32zg3bwlaAZMVUMuCkV-6ug-NbFwusqZu84Y2W_MF2NF7FQxczQJ3LTMByH_RnxAsOJSWq4XQJvbIN06w4iMzKn-ArCcy4D8rR0EU6yrospjN2FtS_-zS7dU9jf_lwvMdVxXWOOU9V7MmutLbjK1AxfalrF0Xm6ouG0_deASeBgTmzfMztLZihNk3VlQH3sQc9GtcfU9XqecYpHl1qwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سردار آزمون: دیروز به زنوزی زنگ زدم و گفتم یه وقت نکند من را گردن نگیری/ انتخابم برای بازی در ایران تراکتور است مگر اینکه خودشان نخواهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107453" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=mlvREYCJs9kT2D-TC_XA6QZkxi1xnw2GguM5KmbWBP96HCPlXhR_hvda13rJS0Bek2Kl8j99MjEr2dCVFC1MfV_D7hA2swxR87a6y9Rqo733IigiQrH5CAg6zTaoWE5xzfi3G0dTRhDG2iE7SlIWWBqcKFk4DEkjXdeIF66VW9YnJv9dMtFHAAD6knzzApS2bAdEbeJhbtMWHS0wufymyYSPj0PS2rPTL8RndwANE8h_NayP5pnkuk9bmVyAhzr1UUD02Qh5ozoAI9c1i8KJWBaAlsCHZxmsiJH5hzmkVbWxxT95lo1eG17vj6gk_6fE59R-dVa5PzyWlWpQSULk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=mlvREYCJs9kT2D-TC_XA6QZkxi1xnw2GguM5KmbWBP96HCPlXhR_hvda13rJS0Bek2Kl8j99MjEr2dCVFC1MfV_D7hA2swxR87a6y9Rqo733IigiQrH5CAg6zTaoWE5xzfi3G0dTRhDG2iE7SlIWWBqcKFk4DEkjXdeIF66VW9YnJv9dMtFHAAD6knzzApS2bAdEbeJhbtMWHS0wufymyYSPj0PS2rPTL8RndwANE8h_NayP5pnkuk9bmVyAhzr1UUD02Qh5ozoAI9c1i8KJWBaAlsCHZxmsiJH5hzmkVbWxxT95lo1eG17vj6gk_6fE59R-dVa5PzyWlWpQSULk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های سردار آزمون با بیرانوند درمورد رنگ مو و سربازی‌اش
🟠
همسر بیرانوند باز برایش حنا گذاشته ولی اصلا بهش نمیاد. یکی اکرم خانم (همسرش) و یکی اکرم عفیف او را در زندگی بدبخت کرده‌اند!
🟠
خدا کند علی در فجر مویش را نزند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107452" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
جنس متفاوت غافلگیرکردن یاسر آسانی!
👍
🇮🇷
خوش‌قلب و خیرخواه، مثل ستاره آلبانیایی استقلال؛ وقتی یاسر تصمیم گرفت برای اعضای نیازمند باشگاه، موتور و خانه تهیه کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107451" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
از ختافه، ژاپن و عربستان پیشنهاد داشتم
🇮🇷
واکنش آسانی به پیشنهادهایی که بعد از فصل اولش در جمع استقلالی‌ها دریافت کرد؛ بهشان گفتم فقط وقتی پیشنهاد استقلال آمد به من زنگ بزنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107450" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
درباره رامین با ساپینتو حرف زدم؛ گفت برش می‌گردونم!
صحبت‌های یاسر آسانی درباره رابطه‌اش با رضاییان، اتفاقات جنجالی بعد از بازی با الوصل و پادرمیانی بین او و سرمربی سابق!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107449" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎙
🇮🇷
توضیح آسانی درباره تکنیک‌های کری خواندن، از بازی مقابل پادیاب تا داربی برابر پرسپولیس!/ در استقلال، از تمام لحظات لذت می‌برم و خیلی خوشحالم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107448" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f025096.mp4?token=dKhVKAsScB6nkDsHVhA-0YONqKPpdLNpOaYhkLo2UU15CpzyDfUxR09qwtYM8jbTgCRI8WIVuN104sowZllOfpQvXjn0jJPm_EeHuvYBUuQ7TnF1qnGq_Wgh90NCYsM5kBKycNKUGpMoxzEg4mbMgb4zPm0xXyeycSLyjKw0r5kEGelO94rQJsVNyLTegCv9JjzfPqbXeKIiFr91ugrhsOSOtIODh6FZAPKTiJh8O4D5J5ZbPNqOzLcHGF8bVaZKZHs6TbkrGbAAzULV-LDdQTKGYS6qiFaYZLJC6Zl9TuHVIzZxSn0gjsCo0O6sCb783yOZzOlVQTovU8HrCyoGN7xFnEbAodsua7pMcYEDLIZjXP5lgCIOSNo1OqpJqs7W23tVgK6mr2nfiL94Q3077jHlADL1-r80JbyOlyI0dQN98QGLyFOHV8Y8tlWyP4PkWv0c1e5ivAFoJAQ1pekpG6TZfIvqU3Axv7n9qDNp-ddaRezbZAURZd9BcCWDr3DhDI8p0YEqO_VHEDv5UqS1LjrgzAcrGWmKvYlkkdmsrQQgOMnIhS76-z2txyBttL_6X8A2c8OLRoDSejghcr_nIRUvhZItx-ffRGDeFUALnedIB1OivA1RltsLwwDl_xPfU4fxH5I7eOxf-BTqDYke2kLUGoZsnez-B1CE-uTOfdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f025096.mp4?token=dKhVKAsScB6nkDsHVhA-0YONqKPpdLNpOaYhkLo2UU15CpzyDfUxR09qwtYM8jbTgCRI8WIVuN104sowZllOfpQvXjn0jJPm_EeHuvYBUuQ7TnF1qnGq_Wgh90NCYsM5kBKycNKUGpMoxzEg4mbMgb4zPm0xXyeycSLyjKw0r5kEGelO94rQJsVNyLTegCv9JjzfPqbXeKIiFr91ugrhsOSOtIODh6FZAPKTiJh8O4D5J5ZbPNqOzLcHGF8bVaZKZHs6TbkrGbAAzULV-LDdQTKGYS6qiFaYZLJC6Zl9TuHVIzZxSn0gjsCo0O6sCb783yOZzOlVQTovU8HrCyoGN7xFnEbAodsua7pMcYEDLIZjXP5lgCIOSNo1OqpJqs7W23tVgK6mr2nfiL94Q3077jHlADL1-r80JbyOlyI0dQN98QGLyFOHV8Y8tlWyP4PkWv0c1e5ivAFoJAQ1pekpG6TZfIvqU3Axv7n9qDNp-ddaRezbZAURZd9BcCWDr3DhDI8p0YEqO_VHEDv5UqS1LjrgzAcrGWmKvYlkkdmsrQQgOMnIhS76-z2txyBttL_6X8A2c8OLRoDSejghcr_nIRUvhZItx-ffRGDeFUALnedIB1OivA1RltsLwwDl_xPfU4fxH5I7eOxf-BTqDYke2kLUGoZsnez-B1CE-uTOfdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
گفت‌‌وگو با یاسر آسانی، درباره واکنش عجیبش به دعوت‌نشدن به تیم ملی آلبانی: حالا می‌توانم برای استقلال بهترین بازی‌هایم را انجام دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107447" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=tQTYlBjjF8JZiiUE4gxM71CIsc3GEdR5FWl53nKGhjbpagrhlj4Oo6igaHMiSJHFHcMhoS3M02awIpk9Pz3v6L9jZDBYAL9zbUcloJo2E34V168O5QR_ARy42CsRtR2etv656qsDmWjezDLUmHI8P4hc5bmLzXazvijLsQSsl9UbNbChWdzBYETWz8dQh3JwZNF6x4DT4ZfRvHhB8hhW4nYRTQcL2qTut5IpYLEMHK7Dgz3yuyFgZ2OfzCV57DbQtEBt0ZHR3ki-GFbU1YX5tTkZh6I5hbFYvFpnOlJGWpMDUPdsLh7vHneV6RSSaKKFiwRaZOx4LAJedXCtMX9rNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=tQTYlBjjF8JZiiUE4gxM71CIsc3GEdR5FWl53nKGhjbpagrhlj4Oo6igaHMiSJHFHcMhoS3M02awIpk9Pz3v6L9jZDBYAL9zbUcloJo2E34V168O5QR_ARy42CsRtR2etv656qsDmWjezDLUmHI8P4hc5bmLzXazvijLsQSsl9UbNbChWdzBYETWz8dQh3JwZNF6x4DT4ZfRvHhB8hhW4nYRTQcL2qTut5IpYLEMHK7Dgz3yuyFgZ2OfzCV57DbQtEBt0ZHR3ki-GFbU1YX5tTkZh6I5hbFYvFpnOlJGWpMDUPdsLh7vHneV6RSSaKKFiwRaZOx4LAJedXCtMX9rNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حسین‌
عبدی: رفتن به المپیک ربطی به سرمربی ندارد!
‼️
خیابانی: پس گواردیولا هم بیاید همین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107446" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgHIDWYSKIptBzrCqmVcwmWTiCvA5hvd_T5tIrPAFZyvk8s66cMOktsQf9sGxnLoeZr1JuXxAVVdQ1UV1W-FmFWC3zNnJWM7XlYFD3jDqNbNADlkPbAV24QYtShmEKgS9ZEwufuk3IKlBi5eaVBPdDcKojr9-g-_J1yqzpHUWFMu2OB2O5kCUKLeO9--L97uJs8DPIYXfoV5CRal-JskLKz4k8RNZYRTeyGKC8TZrJ0nQhfbacCm46JaQMFikaAjD6ELl-q80tfkXyZ5CRMxN9u1K1zbmFjRJZ7RcmUjdC5JARVPX7TgSnHDglfzqi124_GzedNYutdxMwQ_1q9krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=dD8zcYuBb87bQIK0ZaRyj6RBoWuGG-lYVZKk1hdvoFynD7e7nyjEUoqXg-pxh241OFUHK52mnbGLm_aIGgza_t8iV2uFTsmqguvKDbt7cEq11EzwLAw_GTh-TMuYg5zZwM92A0jctGY84jnmtXnXhLETJRH8hQst1hyIH0z53TVjsG1EDMwan3umc6t9604akH2qjWlGRPWYd-5k7tvtzwZIHWPgJyQc6yTgdCqF5liIY0a0vQYPkJbraOaumehDPB7pfhkA14rLMat2C8JFrQheAAP9BD-WVqFVZn3sk40ouVH1iw4wDZVhYu2_TU2WmZuHQt2ae-dNWRCdj0n6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=dD8zcYuBb87bQIK0ZaRyj6RBoWuGG-lYVZKk1hdvoFynD7e7nyjEUoqXg-pxh241OFUHK52mnbGLm_aIGgza_t8iV2uFTsmqguvKDbt7cEq11EzwLAw_GTh-TMuYg5zZwM92A0jctGY84jnmtXnXhLETJRH8hQst1hyIH0z53TVjsG1EDMwan3umc6t9604akH2qjWlGRPWYd-5k7tvtzwZIHWPgJyQc6yTgdCqF5liIY0a0vQYPkJbraOaumehDPB7pfhkA14rLMat2C8JFrQheAAP9BD-WVqFVZn3sk40ouVH1iw4wDZVhYu2_TU2WmZuHQt2ae-dNWRCdj0n6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzpCoIqKtOEWWiKNrfxEqPvq4kkvAEtjQSaY6a8Da0z_czu7BgHn74PZYbjvJw7uLm2aCYB1Irx9WCMNU8GOpcByiOWy4KcLbzXfADoEw8TvEf_rbysXAlvNxRa9RDawQQvws5hE6ypoBTq0euXPZ3UBTBNL1YzVLqfeE1DsZhWBLwl9aG0jjqLOPn2ulou6_NGP0F-6M34Y6_x920xBTLvgPZEwgQ4LXH7AsED0cjdJZQAhmQLBgTK5K3SvH7hXx00q1ffnBK3IAV4lhUgLA57oqYaLB-z0OasIXzEU16EVO0yDop9nS1TJesx3-xbQvT7ebi4PMiFNUs_dPqoPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjRUQpz29HMiIs_7dF0rPaJuskalntqGdaRfHFoMdaQHgOAah7HtEkqkI33_6Y7c5ocva07cEE4RGKMM1_gnxRUIYWPoWR6tpxMtIUivG9HShFNBo6oEIlx7MzSQeBvouTZVzrSKzQ7yScfxZVvazAhL6LAp3V-iwL_YqsRzggbCjmkdFY_8vcpHBBalMYKlhNuUcXIylKIa5HzUUh9GcdDV0HFfWBgssFmFDrvm3zoYTAMKMKd-BZsJiUCKLYvCSCukYiD_e5HNFKjWQZGnKMroWkeom1QQGho1RgCcjw9KPBTshUEYf8Zmrrz3ISFgAnSmqPQzGgTLhKCPs3ru-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=DoH_abxk6y5RvpUbRBaj4pQ8XkEn3KuRgdENixS5rguJlrVVAlJJPydrbjH9LKnZWl4Bh5T5YdjCXAbpnQAkP23JhedRVCN1NzeQGZPRNMLfKTwpuke7R5rs6bprPw4XSWmh9zJKqCXVfddIOYMvn81TAvrwn1sk4SA0HzUn-a5cBvlFTZ47TRM5fczIss5LyU1TSEr_g-_WNqnJryJIJ3XTBaKJzIuSfW7RF9YydGE7Vnoe4iZZuSnxMMXXE4gCYn_KLXc_5S89pPnSq6m_Dik5EXWdUfx1GRNHsD35xDdpULrUniBjaXGsa1ZzEdJBjIANl5VrB8VnQ4uieNLKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=DoH_abxk6y5RvpUbRBaj4pQ8XkEn3KuRgdENixS5rguJlrVVAlJJPydrbjH9LKnZWl4Bh5T5YdjCXAbpnQAkP23JhedRVCN1NzeQGZPRNMLfKTwpuke7R5rs6bprPw4XSWmh9zJKqCXVfddIOYMvn81TAvrwn1sk4SA0HzUn-a5cBvlFTZ47TRM5fczIss5LyU1TSEr_g-_WNqnJryJIJ3XTBaKJzIuSfW7RF9YydGE7Vnoe4iZZuSnxMMXXE4gCYn_KLXc_5S89pPnSq6m_Dik5EXWdUfx1GRNHsD35xDdpULrUniBjaXGsa1ZzEdJBjIANl5VrB8VnQ4uieNLKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
