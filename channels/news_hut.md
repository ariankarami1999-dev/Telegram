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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZL8fXf9MwS-K3NRHY7QwXqjFOxyJuEXPWSTbqVtH_h-mOSq30yxS25WYWq3MFiLe0CID52RlTTd8xVeoBcZHejWwkkD7nUkWSA0tOY8rtnMEe3nUDPFNa61DNoO5vTi9LK_8vWt6ZIkBjfGosw-whTFd21xNjCbaaBZZMNms0ucZx9EACCoJQBh2vAlAt9RmyRRzpJb5sJkfJ8EWshTQedXHJZMt4I332CqPRCnnc5abRYNtFN6XCCdq9v_kmDxXOjqnzK7E0s_ZGs8Kz9EHOGfsCsfokIvN4-_oqzinsRoUlgv9seY4KtzlFGLq9FxA51xhE_JDHDJLBo7z830Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HftnfSSMsJg0my09wnU_gWoj7YBKJi9n6gqk6UAlK1HsYH6a8WqcYugE7Vdbah6Br_byWkbzWttbFST7NoFV2Xv3GtFWE1kicBoxVCGDP4_Wyw5F6c60oBcTXquTq6n_O84Ej9Ldo4IWzfgMyy9E06MdISQlYST4TadhWEEfPTnn8QRg3iDldk5TCSSjmK_vmiEsCB-EnZtBj-2sDblVQ3dPtEowZrI2LQ3dMbxxsT2wasakQLwGaRkiPxTQd90hPbeMEFEb7mSZxNOivIHTUY_fgYXbCNoM1ZuRqmty35b8LkjJ8Aond3hK7aJMNXGA3nUHlPN2IDfYUqJWDA7W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5SpthHiUKkyl_1yXcKj9u2x1xmXQJuKRsQvZ7AC7R6hItuwYGuDqKEftMMn5jCUwfEQcPC8279o0VjWdN1Ls9anijyVLLYDujdAGWrFhE6Ue3fjU4IWhThZHgel3UW4Gd8GwZvUea3L7Iz1yR0ZBWlvsX0vR0nQ7sJ6--vx1gTCOCwu-OZ4dZFJmLlFdTwYchnauU482KI6-VtRiAusZ29qIry4J7BSltezzV-5sl6uDxjGhcWRi58Hg2EY3l6GuYBticEmkeJKtReDk8oswdn3PC8K06LlYtCKTjzj4dAYwJ-SqKAYoqpIonUjJzDpvV21ZjmSqSReyXfqF2u1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raOYel0Gj_FV8S2WmMTDETKE5krbF0VO8ThVsoJ5rPcGHFjdkjdJEchu74ogZE3iy5BPHn1XLcO51zg9z2fK6vshMXttULa1Oj6iLJFpg3cpOBjoVQbwH2bDfxvtECMp_x-rA7IEtF-XlR7ieQYTbj1p7Xuk5arodyhssKeoK6TXyHqb0jgjf-QvIwUVIzVaNCfbFb3VPuw4mIk3wob7LyCDOnBsSR43DLKv_slTJhMnyWdVQU9mmxWPwR9AplECPBlgv6XSdQLRH88VCNBjfSwXXAMWostj-ngNl_Dw4XJTMy3AXonTaPW8Rq-VKb5W9fcbev4mnfhsQt_O1-zuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kowQ9Ujb1aFv7NE-VJ4O1UtrUiwvYn-Tp_gOYcCC9intS2vg_vcyPoS53kZnVHrgNNKK4cJIkg7148f1OWr4pfFVo4m6GPkI1FfYlj45ZfpG0unn8oBJg_y-bE8mBuRlujbTra7JSETafA5HxTWNRPsrnf6U7LwUcJf4JkNk7icVKrJEa5D1u4N5rGp73lSDZgJSV_gYf2AqNvx4R_xG65mdF_1XDLQK_nOsgAHyJMy4Q_dCYZgEn-xbKTQm6O90ORTEKij8RWDtsYMZ3FI_t9NY1TS601mHlmiTuf66eudIffJuu85qpOz78PyOu7ONcdbF9TaZfILpCATsKzoynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXQjf6WRE1ISMxo9dagc4Krqqt_EAQ0eVtvezu1o13439Euwy7ZQcvmsUIvRcvyraR2l3bKsDluOVBul8x7rB2nV9dU5EkcqAmXQuqavlJ57qy8n6JZilycA9uNefLIpNQyLOyod1QzTgcNLA0p5hphupyG5dXDWYu9uisRQIo45s2Ad_a0T5Sshu-0ZIAQBAQO-DBD4xgOyUL6LFKcj0XUAgseDpNjSpcBnh7ILyxJSv2KVlGn8QkHzQL9CUol9n3MQFc7eYJAlTPCEe3U-Yc5LwyYzUtmnxtQ9lLq6FpCvbDiRHxdHiAV_Vx2PCTmNdYixg1nXP6geKPK5v_nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi7BttRD_VR5EK9QC8cUXdoDUzZbQ0xZBg4QqOiwpK3IABA-J3_7HhZloHFKXbAESOsKMS4CqnKhGsi_xUBigEaaf6fdE-MTGO-3q4xOzTDVm-NjoWJsVrGPrsDmoePIBg_9oInEiUG2QKu0-FUYGLoFpGLhgYrahJ3MNUqB6LBDxcmcrivse2lNotPKcAD8ATTCTDJyvxqhOqIRC0JrXI9StuySMbaakcCTFq9wi9G2k0blT1kuLQECiURV6PoQRbPRgUNRlox7aO3ggmyJ5PFfLIgCLKKMT7JTLwOxqTEpJJxQEAl7mfxQVRrLDD-ARQQyogmmBotlUkPWWDRgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcKRR0ukohSmu2TwdLkfo7lZRvoRYl46BVhrtxUkFtEwZAZaLO7j3cnn8HmfgLtNPq1lmLpWyOBz4k9yMfdw5OBwrNQibH-EKcEpVtpSvMb9yUSLuY-N5nBpCs1J_BaKxEBKGTe2l_QHuqk9JirdAsMmqBSsKqXjqo0aesRJDh1WuCRo5OolSsEiMlR7UcclQdwlIC-2Zj8nzMGSGUuFzWeIZj1Y2t2tDwCObfQKAlwmi_enpxfIQ2qHwMJSb0VtUcTLxrsYadD2DpOg0PR0YMz_XDXG2ZfatWHA8CsK4PqOlYuW7tgzGyrjT6fBTAMT_XabExl5riKocOWSbFKg3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2nxrlVHIFxVOibw0bcckepEoDzXIrdUVRkRcukWeAHF6I5N8AfeJdfoffFEzfOnwNevucUVv5bo6ZNH8jQ5Pzlq0KavZnpAeyP7qEhUIygfZZPyOao3_8UXFnzYXKr90Rks1emUunjWToC8pTHroe_C-_O3klGTun4J97LOiLfIx-KGy5h_cbE76tKI8x4Z3_Sf4jOoaG2i4hSwsU7U0XB2lH-t-AfwspayzfwnJsvhCpscuBYoPudNsKcWogs2QdHGLXuUjsh6CH1XRJSyRKu-bNdX-Gx1laEjKovJO_M4DDp9KihdDzMdpCLG3qK5pTdotBRYnbL0OAy2UDHRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSEvhXWR_reVlvuXq34y4-0ZGZQPuSiLwOh5G5PsbaArkWlSjxCIhXgrVXyGIp7fgE9fLqmfCYRMIZsq9rbFO2B-PTFfa73PmQgastYVSrEIjyfTPRSe_1htFUkh2WdO4x9-QuefVDXFJjkXLH1jyNa0mgUVu-kKbcn6H036gbwBEcVEHeoYyAb4hNqLxbXF4V-SMTEimYpv9o1sooNJ5SIoIkhSNn_18obKJRpdWZi5vo051vtuZCRPDQXMxB3_vgxNrqWSQKCHxU37uHPquya7XmNGayQMDb_7p9vSjHgRbj04_g8hVnzvwgk25jqARgyhdnhtltYFlEx4UzOhWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khUIkCtQDwJtTPXDTO430S4btMi--AT8V0egBuU3LYRm5tv8U1jreuvWjNEqxl3fknLzSskmA9VQCnzhF7NWlQL_GSZZC9gASBSDFezsP6YaCXycC_6lwVo0fx87TsGmLk8y0-UZTx-H5To-CENzi_nHgqYirQD6-e2YImqMEOFQlEcIKSwV-O0vPwtxmR98ODTEBHu54EdHU64ReqTX4L3zYrtIwdEHPYbVvg5k4ZILMfw11pe4SPiLHg5uOUdhV1pYL7FAAiJR06nzWbP32pJpXE-FzFqoPuxTj2LMWvw7mYGqViDEKwQkxZ1KF5MKc590ojcJjcKDRMRbeYrOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPDkojMbdYkRpMrRAG_cbIiO5Nf5aM8J-a5ZdSqFosXYLocPrvP3wknkpBI7mT3FL99qeb84-zOlM4QM8K2NchcR6Bovb4-OZcK-lH7tDfHlqNm_tn2QfSxknVbzWcoPksRw7YjX52opnBVImGAePt4wkJT_tgdimueUISAyBWIJElLMX-YKRif_Pz5lEciP1yhs3QD5OeKeEgT1UU4iHM64eHNcAk84jK8umg4JKmcYcBTPU1Bvm6ZM9ESCC2OvfuYM-1yOjakj6zkRqOrpye4M1SeKLr3uBenW-FY_z91qgNOEklDLxLs1n_E_U3K1Gz_eQshrwsIV2qrk2SlZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlKCOHv4Yunle2gAUKWDal40VjLkks4qglW7bxvrL1T-7urfTU2_iiu9dXu8YDqecUYIDjLHQ_PdNK77EMs_iqeFV2wZ1u-1tb54zLR19zSiiC2P19HrXx-LGX0gBoQLgTh2SCSIzXMsIJZ3x_JDv7BqIydCWSI47e83DSKpBrNo0-ec5sjZ3YIHAbopNHi4Zb8etMEFusQJFMHl8MvPDB9wvruDZ6PsBs2irvK76ksK-cEyf4WyB5dbaS92WqHtWNLt3TZmEH_GISLAmGXMwWq_D8NeyD64YIIlmYmUiFTfBngln8md70pF2xmqG72Ff3JxiCRYPvPXLWpXy7LlMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=NJc6FwMtIbpnsLURfFsFIH54cHW1I-Rm8auG0zI6jd0Vj44bFcexWwb5CAr_DL2xIJVN-EtyZQfgkFNipP9_l4enzcvlBWH_g4WtjggcTwbSLTmOsdZd-TQqlbHvFPgKzG3IAp7SQav_JhvU0GYI1iCNWJCNEe6k1X6V1Ks8j68FVPuYeEEulZUKixs9y2Tt3nW_UwXd6rx3OjM-9GV1qC5CEqBrzYzHgpZbO2GCvHpTqHteV-Z2_gwKIFB2rjnqmreh3k9D_O37q5LirevVbphT7oblsqWzqhQ_efcmdVjStXHcexzS5HgxHxfA5jAw3SQ9A0bgeNFIfdL8IgzljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=NJc6FwMtIbpnsLURfFsFIH54cHW1I-Rm8auG0zI6jd0Vj44bFcexWwb5CAr_DL2xIJVN-EtyZQfgkFNipP9_l4enzcvlBWH_g4WtjggcTwbSLTmOsdZd-TQqlbHvFPgKzG3IAp7SQav_JhvU0GYI1iCNWJCNEe6k1X6V1Ks8j68FVPuYeEEulZUKixs9y2Tt3nW_UwXd6rx3OjM-9GV1qC5CEqBrzYzHgpZbO2GCvHpTqHteV-Z2_gwKIFB2rjnqmreh3k9D_O37q5LirevVbphT7oblsqWzqhQ_efcmdVjStXHcexzS5HgxHxfA5jAw3SQ9A0bgeNFIfdL8IgzljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=HOU-1gFoVVO8cBL6zA5pYqIorXwsukwzmrU3DqOHBr_j_QJ0qGliiyuGcBtNHFVRKOx-44AocCmdpPVWwd0St8oRCK5fvVKvl98h6qYkQuKUzW5v-wohKs7B4wTPeqB_RgI8zkGC_ll6oafodhUSOE2m_swK8mUIBLW7aZqd_yX-V8-7aTKhpasQ-wxvpWtDvLPb8xGyap7UZeeL29W4x_rAIxH4BM3bxzlkXXB-bYjkj8TghHh6YU4cKdJ_VVhM8VgVGYT3-J2Ni3J7clgVcYoenuvHiWblFeCn1bsJSk-ojRHlDm77JM2eQWCTdeqXHff19iekXrfEEDzwe3Jcmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=HOU-1gFoVVO8cBL6zA5pYqIorXwsukwzmrU3DqOHBr_j_QJ0qGliiyuGcBtNHFVRKOx-44AocCmdpPVWwd0St8oRCK5fvVKvl98h6qYkQuKUzW5v-wohKs7B4wTPeqB_RgI8zkGC_ll6oafodhUSOE2m_swK8mUIBLW7aZqd_yX-V8-7aTKhpasQ-wxvpWtDvLPb8xGyap7UZeeL29W4x_rAIxH4BM3bxzlkXXB-bYjkj8TghHh6YU4cKdJ_VVhM8VgVGYT3-J2Ni3J7clgVcYoenuvHiWblFeCn1bsJSk-ojRHlDm77JM2eQWCTdeqXHff19iekXrfEEDzwe3Jcmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=Nw55AKAbu7HzaxJ4CYk7PjjOsvsPb56g1wkGpfMjZzBpjG660XCF2Oc_it6CngBDBU4tsGWsiEzq5NSJSrKa1Gma3qkP9veK_4f4qc7uoXghvTUFHP6jfclLGdB-MaE4uxVarBdPRPy4neW6RBUlM-i8Rsge24FNhzrO2NeL3vlWhRmIwI3XRwmfQCmvx5a2fo3KkH0_s30OyH-NIdD5a-nbELU2ZP4MsJNaj877_k3hZYOqM-4Vb_eoDPvEjQwCmZHi13mbfS2JDXtC0AlNsdTUJgd_OhRivs4wrxhAkRDjM5OJyeuC5CEkIdvKl0wDLH9-u-BemShpG3wmnxBpuDb8D-q-0O6f90OzXe1kIT5iqW3ZTE8gwPoE2hraxDSENWCZUwZWTgkjmjJG_CkqwpG9a8Gitbl1TdLGI6WzaBYB3hdeCj09_le7qJQQf1Ti8I0opMwWkCmmA77sLxDx7izfeHWh8G4LLXR2zhZ6P9rECQTIdfw1Y0suZEArSsu_2yi18xZd9UK50Wli3WK0EiBdyRLQaSF0MKbhyTEZkvjpV3nxtlQz1xVAge4JxTWWWROWtIYqjrVrz7XAFXSpMwb0o7tOquBvnoECnWTxodnKahutySo-dpzcxpp9Gad96m0bgNAy6WZa-WidUY13bgz1tGbobjv0B5Qc5CYTOr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=Nw55AKAbu7HzaxJ4CYk7PjjOsvsPb56g1wkGpfMjZzBpjG660XCF2Oc_it6CngBDBU4tsGWsiEzq5NSJSrKa1Gma3qkP9veK_4f4qc7uoXghvTUFHP6jfclLGdB-MaE4uxVarBdPRPy4neW6RBUlM-i8Rsge24FNhzrO2NeL3vlWhRmIwI3XRwmfQCmvx5a2fo3KkH0_s30OyH-NIdD5a-nbELU2ZP4MsJNaj877_k3hZYOqM-4Vb_eoDPvEjQwCmZHi13mbfS2JDXtC0AlNsdTUJgd_OhRivs4wrxhAkRDjM5OJyeuC5CEkIdvKl0wDLH9-u-BemShpG3wmnxBpuDb8D-q-0O6f90OzXe1kIT5iqW3ZTE8gwPoE2hraxDSENWCZUwZWTgkjmjJG_CkqwpG9a8Gitbl1TdLGI6WzaBYB3hdeCj09_le7qJQQf1Ti8I0opMwWkCmmA77sLxDx7izfeHWh8G4LLXR2zhZ6P9rECQTIdfw1Y0suZEArSsu_2yi18xZd9UK50Wli3WK0EiBdyRLQaSF0MKbhyTEZkvjpV3nxtlQz1xVAge4JxTWWWROWtIYqjrVrz7XAFXSpMwb0o7tOquBvnoECnWTxodnKahutySo-dpzcxpp9Gad96m0bgNAy6WZa-WidUY13bgz1tGbobjv0B5Qc5CYTOr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=YFv0iEgPDOHQ8-i7wBr5-_x6saCJId6suAwD_PPFpZbcg8M-mWxqfmqfnCCjmUaj1LiUPEeuBgzvlYndC1ChTDRnlvyNsrHPSX1_aSFxPLZVmY86KFWJ066bMmBawl5HFDeZ4_SdQ8j04Xxpx4R2SoIeFwRB_FkwdizhIBsN8NP8Euc-8UV-MeeHn7rbdkVbBWMy5CiSXWNbSUSHLmbEnwB-ya2fSlpRW5Dx9MHvr0AO5LY98TJJpwPwnZ2Ia9ChNsBVB7v2dHgV_f9ua3Ogenp05CAy-ISiGf5VaihJPIT-vUqsHw9qkD-XV0N8k0LC8aIPoquaSokDcBqWT3DHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=YFv0iEgPDOHQ8-i7wBr5-_x6saCJId6suAwD_PPFpZbcg8M-mWxqfmqfnCCjmUaj1LiUPEeuBgzvlYndC1ChTDRnlvyNsrHPSX1_aSFxPLZVmY86KFWJ066bMmBawl5HFDeZ4_SdQ8j04Xxpx4R2SoIeFwRB_FkwdizhIBsN8NP8Euc-8UV-MeeHn7rbdkVbBWMy5CiSXWNbSUSHLmbEnwB-ya2fSlpRW5Dx9MHvr0AO5LY98TJJpwPwnZ2Ia9ChNsBVB7v2dHgV_f9ua3Ogenp05CAy-ISiGf5VaihJPIT-vUqsHw9qkD-XV0N8k0LC8aIPoquaSokDcBqWT3DHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdqIYbpIvtpnc3Ju1fVVELpHmTHDtLB9gWEd5URgVN9vGm5oeCGbRvXxPG2SXFrbSpj_xuzSmTDrau96yk5Jv0hwLsHnTkZviOqacGMkboO9ai7rRKk_Ay2sVwVXSWrL4ypJ5n_ZP8oZ4D7qQ73dxMAsIgrbnSFTfQ_iw5rtFORwSrEsSIz66dUxWmIPTS_E6cJhG5n1q5mvEGJ7J5FxtvkeBBs1BCQRjMPsKeip_6ny6Ge4R1mEKpnpINOlFE2xNgx6tz78kDUHfXXkzrS3VCClV8jxp3zIiw2LpPe6FUf8wGZTkJP-ju49-ZLq1H-cu8-oYAdRnVZElipbKHLNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbTLRuFi7ZLw9uCsoaDH50V2VPS6rTPj60FflO8fxBZgAoLxzzAUrV9MrTa9v51pYhI1X4zeocFycZnI7ULJ6u-ajQQuRZrcQtKwEhRfgFuPvmnkjtPK1zYQAqRE4uVTpILGqH5qrIsl_X97rSNafANsST34r-jTkLh-cTcpVW3RlobVi_abCv-vWBpTpXrEmRrh53VTsdW4wH7CHgSAcbE8nPP8WlUTTfL2OK1zXaQWqB-iVTk1x7iupnZgYLwEK0L0IKpQJ4vUaZb1JO6yKT-KvhUmXC31r7lbEvrinZ1S3IWWbuZPA9d9bnwnPAHWOPBCBVd4nn6xFwUENGQSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5RxWnaL54IDJJ6kdCYJtUYiW8U07R-1iurnp0F03-O3XZ9sEcMLqwkz5sByh-vK63Ys8xRUwqRTp-uPXiTNtc81Chp0DNmaMBMqXhEFuAlDcmpYMXQGWw9llp1JHKj-szrPKBoWC4qTcIDtkb3Bl2Zg6RHb5L93K_bkLUkQuohjCi8TndyoaTi2a42677lEpRW9KxE-bdgtdU6ygahTui6BaB8TKFr7eme9wF14FNzGmeGZTeKUCFs8gzA-iR4eXbP_ciN9Z4yCnW9dMQEUqe0RVhaxOkjqY-sBZpCdQykwMA_bTnqPVn3mjWMb6qrQxvlkxVOaNFcrT1dl1MZKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXSVE3iHs5SPACAdqyl66rbXOkm4oNBOSdlG1FL440JNSQrwjphRC6mVnmMfWViU1soaVDpsEEx3nebjDrMT4iu1dclfgNaSQRA-OdlI3IUMK2FJ6h7BBAAW_-tfeYO8vCliTar7jtQCTXu6vkTAL4L97MKdvuEueZhOxrBPbHEiyaQT0aAVnNJb0Z5C87fKYURZXUJ5kzvxzilIOi78tcpBodMKLm_-5ePxsvwTufN4JPOc4DaEcpO1lOShVMud9RNS-LKljZ8J1mXRnZOOmqctcAGP6IksBkX6AmAu9hMxsGEnD69qFGBDFO2O4m1yMmxZG_RGdutN_O59tfoUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=W-eivpaNr9If4SVaXVcLKWrZKk8M19zeXOCFcUKeh6hckIkhstlR4hn_xAy3b4GPStZxWvnKW3-l5JKnXgppUm-xooXclk2OC3vlCdBiAhnhoxudMkAYUNGrIYcc44rbwrJ7ZUrRVmeVTptRnZZOekb0kxUqmcur6pe_zmyH2R1hSCkDpZWPRSTaGaokZSlEnkjlrevFUB922YsH9dBRRN42FiY9-kP404d0OdAC-XF5RbKuWLFBIKDw9DVAAtUJKh0ESC9V4vMx1itVpuAjDHJ6G4vCKSYqFeP-GyYCqo7OiWu26zXl2fGvs7Mz1ox1ktIw85kRgYjvEes7jFlPOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=W-eivpaNr9If4SVaXVcLKWrZKk8M19zeXOCFcUKeh6hckIkhstlR4hn_xAy3b4GPStZxWvnKW3-l5JKnXgppUm-xooXclk2OC3vlCdBiAhnhoxudMkAYUNGrIYcc44rbwrJ7ZUrRVmeVTptRnZZOekb0kxUqmcur6pe_zmyH2R1hSCkDpZWPRSTaGaokZSlEnkjlrevFUB922YsH9dBRRN42FiY9-kP404d0OdAC-XF5RbKuWLFBIKDw9DVAAtUJKh0ESC9V4vMx1itVpuAjDHJ6G4vCKSYqFeP-GyYCqo7OiWu26zXl2fGvs7Mz1ox1ktIw85kRgYjvEes7jFlPOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=g6KmVjLr-h6CIERPp8AyVJu3GrGdfSsZgMNm_-hiEwsK01HrLWCpQEf2vNJgbDBhyd8I_tUgu8DFjCSN7de2-RoW6DU5BybF9eHZIl6doXzNm74C-AYDHArMuBXkTgR4wWrNX30eGeChjBdQx2Wgdzh3vVdITS_pF0xoQzITjUO9uw2Wql0hMKbWkApW_rjsfGB8JEaAy--UCGrcgNbztihpAC8lOpw9fq2OCq1QFAH4OKk7MPo4_Zv-GSIBd5t4pwtCHtocgESkPUvEHwPxogkTBLr4Je6CiB-YdVp5s-qH1LCXjNGsz3BOfPH5BRDhAv8ubfkWV9nEKY7z1Jy-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=g6KmVjLr-h6CIERPp8AyVJu3GrGdfSsZgMNm_-hiEwsK01HrLWCpQEf2vNJgbDBhyd8I_tUgu8DFjCSN7de2-RoW6DU5BybF9eHZIl6doXzNm74C-AYDHArMuBXkTgR4wWrNX30eGeChjBdQx2Wgdzh3vVdITS_pF0xoQzITjUO9uw2Wql0hMKbWkApW_rjsfGB8JEaAy--UCGrcgNbztihpAC8lOpw9fq2OCq1QFAH4OKk7MPo4_Zv-GSIBd5t4pwtCHtocgESkPUvEHwPxogkTBLr4Je6CiB-YdVp5s-qH1LCXjNGsz3BOfPH5BRDhAv8ubfkWV9nEKY7z1Jy-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=lyp58RQ-M9DbEw3MARpCkJ0F72WwV4Pjm4dWTXMJwgtW5rzSg6eosIqlAL6Y2WpI-A1_hvKfaCLhjJh3BvEred1FGaong9qYnMrUKHQZsOZxHsQIAvVjRAmW21hBqjTBRyG46bYY4ZiI_rm8kuXs744LJJWXEphz3s38YYZ4lREe4RwrCiPF4yI_PtBy-sb6NAX92_6gkzRZwyTr7E9Mzlg49aJcZIrEHBqcIOgqfJJqgD9TO8IqNlDM4hYT1rMpBKrOEsM1vdz0eNO278a3gfWRYwNrn6tbLo9Wfvor73MydvtfYGR8YY8tX8ciUHldCuDQ7yx2YtLBdF5TCLLs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=lyp58RQ-M9DbEw3MARpCkJ0F72WwV4Pjm4dWTXMJwgtW5rzSg6eosIqlAL6Y2WpI-A1_hvKfaCLhjJh3BvEred1FGaong9qYnMrUKHQZsOZxHsQIAvVjRAmW21hBqjTBRyG46bYY4ZiI_rm8kuXs744LJJWXEphz3s38YYZ4lREe4RwrCiPF4yI_PtBy-sb6NAX92_6gkzRZwyTr7E9Mzlg49aJcZIrEHBqcIOgqfJJqgD9TO8IqNlDM4hYT1rMpBKrOEsM1vdz0eNO278a3gfWRYwNrn6tbLo9Wfvor73MydvtfYGR8YY8tX8ciUHldCuDQ7yx2YtLBdF5TCLLs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfSQf6x0B4QHpTayjpCRuh5HCdpc_ouZowqHcVfmZk-VMk4Z7iZL_tH1dZtL7jIZmaXup9n_fNAVLT9IlxYOH8JzCe8JiN5xJ0L7zrc5fJtLRUGNBVaG33i-ZiYGHVc4WRM7Xt8UA2l-Y9SwkvUgzlFmR2FFrgWfIUXT8341zkd6J_-niSJgSCGSs3l4pnr1IUIJlSz7T9OP6P-a65PykjtvjwkBmM0gzEZMoqZvVuXrcass4ki7T2iil2Qria3ZsXnTGmgctf-dIxlvSq75suODna9SDlwcMACieFzwGAdniBCFv4uS8f00YS2WTfRK-zYLRHHa1uQMaMARdwd32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYhbp7M-tUlJIV1J0TU_w0aR8I0W1MXT2Y_3lOhsp3DhlJGpBeo_n0yMWnMux6nlvCZAfiu0URGpUCYIZ0qJWXfb-r3c_N5tVdaykJVyuHr2T_Z2j-xyecavGxS1tTT2G76GIIvaS66FNSUYD1gM5rFPmwm-aH_0wjg0Ovcuz1DPj870yGTO_XMSJsk-M3B6GqqVXW_GjN9oFZoUxrHAZq_9XlqR2IeC_R7C6n0fPPf2ZEs45eI4tFJD18o3qEea0vTNO0j2tNoEPK6euDTD4_UqPlabStwaakbkrSsaqGU2v63igG7iB9Npys9Cusgedval03xZ5su9kdvrqctPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=C8SCXNM5CCfr-rf6B46VeWa1EpiT70QER3D4SSr-1E6rJyUl3mRk_n6TxkFwq1YrHxtA8_e-Fd1Tji2GFMvgVdlLxO8z3onK0p4QHShPyvnyyllFi1BVg71hMB582bexzJHwLw-lFi4lrRPm5JnN_xwOpoCGkZk1aLKMWxaVtzrJeVVO5aNdG03xn_GJxs2gHaDix_kcSmJzYCC_PreBR1yMhaXe1AP7WSH8jcr-hs7SoghdS40XGiXxSkiVI_GfQSQ4klSaMUkzD3yHjr9Ki1u7OeewzEv9H3Zt_CVXHBbIR_C-Z1HZRMXuIsig0SYOP-Ekc4yd5jZKsdgMePDXlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=C8SCXNM5CCfr-rf6B46VeWa1EpiT70QER3D4SSr-1E6rJyUl3mRk_n6TxkFwq1YrHxtA8_e-Fd1Tji2GFMvgVdlLxO8z3onK0p4QHShPyvnyyllFi1BVg71hMB582bexzJHwLw-lFi4lrRPm5JnN_xwOpoCGkZk1aLKMWxaVtzrJeVVO5aNdG03xn_GJxs2gHaDix_kcSmJzYCC_PreBR1yMhaXe1AP7WSH8jcr-hs7SoghdS40XGiXxSkiVI_GfQSQ4klSaMUkzD3yHjr9Ki1u7OeewzEv9H3Zt_CVXHBbIR_C-Z1HZRMXuIsig0SYOP-Ekc4yd5jZKsdgMePDXlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=netNhnP0ZXT6WZJok3wAZOzI0biiDwrfmDZq9uLYE6UYl2SEOvGZ0HcWLe18GFjtc8mKks5tCX0Qi6bpVVgyk7kbmv3B_xP0oZEpioEWYhKVUxQP0YUGZ4oIrdlHgmAKXA4jNdfLw-9lTRwpe-3IwtS4-NM8TNEgcDmk9tf9AZupfcD3m35v92Kudlxgumfxr5ZMdLIeK7xcWuQUkC3zHE-2RvpEessmYzPGBlPvHIsUFohDbWAGoBd7zLIB2ErBqTwJN4oy7lvZTOCzjLccfAa6mi1GYPOEzS7ElyOXjSs2TzqtXG9gTkRlVvdsmYAFTiAzjmX-KzfJ-yIIjYuMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=netNhnP0ZXT6WZJok3wAZOzI0biiDwrfmDZq9uLYE6UYl2SEOvGZ0HcWLe18GFjtc8mKks5tCX0Qi6bpVVgyk7kbmv3B_xP0oZEpioEWYhKVUxQP0YUGZ4oIrdlHgmAKXA4jNdfLw-9lTRwpe-3IwtS4-NM8TNEgcDmk9tf9AZupfcD3m35v92Kudlxgumfxr5ZMdLIeK7xcWuQUkC3zHE-2RvpEessmYzPGBlPvHIsUFohDbWAGoBd7zLIB2ErBqTwJN4oy7lvZTOCzjLccfAa6mi1GYPOEzS7ElyOXjSs2TzqtXG9gTkRlVvdsmYAFTiAzjmX-KzfJ-yIIjYuMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-6zCzmX-IFMKERvfLbdKnpH7yXrLb2eSd6IUOztp-j_ABmw49uZll-XjdCYPXp7ecLFCH9adjl3mCcOP1q-cTjaeCb3XXE4ryiWF4R5FRtyb3T3lzhor4M2V4JzD6t5xhAGtR7Yf8Dx53-wRBUKVLD8LZCAIgpMw70rRuuidg7JHFdZJWNr-RFZkNImtJcMX1w_WmNnGU-WTNRT7Ndp7yg2EweB1gK9DxjmV18yBJdAJKhFcK1gckinUEBvEFxInblw5oP2pCinMEOAq_TT-e423Kjt2n_SbEZWW72n1oY7HPNqhNCJ9f8vW6yHFr820U3BmENgu5Mb3tQnwq5uvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=NH3tc3BXNalnz25UXr8xMi9t43l6LTVD9WuVCDzX_Pr7HBkt2eLn_O_g3IBXzwhCp5L1n-Dh3MxnHu82pXzcSAaJUjcFnNg0wJao8IqIuf6wh9o0QtSeto0W0xF6dbKUuSUfEpOV1G5lRzazgRpdz4Xe_ABX_3UnJqPigTOeJT56Awdu3ES77eZiZnC_s83k_D_u7ZOO3rrMiFSTZ2QSnNS4xXOGzPZnI53BSRNpjHTRrZHBLP5SjLEX6KFl1nvcAL28uaarTcKtS2PZGIgIEPl97CPu25uNZGGn_5Dzez643hYxUg9EZmwcRNG-AHSBJzmOTjldXkzUyrf-fBS5Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=NH3tc3BXNalnz25UXr8xMi9t43l6LTVD9WuVCDzX_Pr7HBkt2eLn_O_g3IBXzwhCp5L1n-Dh3MxnHu82pXzcSAaJUjcFnNg0wJao8IqIuf6wh9o0QtSeto0W0xF6dbKUuSUfEpOV1G5lRzazgRpdz4Xe_ABX_3UnJqPigTOeJT56Awdu3ES77eZiZnC_s83k_D_u7ZOO3rrMiFSTZ2QSnNS4xXOGzPZnI53BSRNpjHTRrZHBLP5SjLEX6KFl1nvcAL28uaarTcKtS2PZGIgIEPl97CPu25uNZGGn_5Dzez643hYxUg9EZmwcRNG-AHSBJzmOTjldXkzUyrf-fBS5Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaDoAppjo41IDN7Ct_auobLnbggo6M13QFoa8-kGEm07vPf3ZSdT084v7hEdEdwRyo5VS-kPE6h3YzxRmDFaioBOTT-zYwHJHjnsesqVjiEAW9wDPiqifIdMsPQb8sqQeAP1iUNyPTkavguQUIThbbkn8m1k6uIG37quVeWGvVu__3jxJqumLaF0FaFaro3XggOMToVAYBtganyb571ED_3i_K3o665O2VW9g1yCVANmZwaUaQ68mIxNEXEoHvpvjdMytIUUZ0wP0hoAUzcJGybyXd264IVBX8WFJj158DDz8KiP68_4qfFTttgGMWEMe_SNZXlV9xJ9lvjXInFSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=HhS8Y074O0PZygIfCyjfkeQ-PPzo3TIySXWIiao07FaNbu8VIYE0PPy5PaYDA7HbOJ9a1hiyw3m8MZNPNzSIaCpVgDruo5T0obwK0cCASevhQeWJWlggpXFXvdXH_hAyhbvnKTPpjB9d46zWQVaKZUtHm_BwhJwmI4S9s7YPIPeIkCa95C2nR6FrgO0OWvGa29urAJEOYQ4LvjwawAp3HwMvXZCFqpDpNbQi27BrH7-LwDb9ZiHVBF3de-Gv7sc4wcMUtcUxGXIn74SQmo5dm2g1DolGuaoKI5M2TKzR_FPcJnPEUf_Uf06JwsRtb2lrMfnx2Oa1AWUe8VsHpJo3Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=HhS8Y074O0PZygIfCyjfkeQ-PPzo3TIySXWIiao07FaNbu8VIYE0PPy5PaYDA7HbOJ9a1hiyw3m8MZNPNzSIaCpVgDruo5T0obwK0cCASevhQeWJWlggpXFXvdXH_hAyhbvnKTPpjB9d46zWQVaKZUtHm_BwhJwmI4S9s7YPIPeIkCa95C2nR6FrgO0OWvGa29urAJEOYQ4LvjwawAp3HwMvXZCFqpDpNbQi27BrH7-LwDb9ZiHVBF3de-Gv7sc4wcMUtcUxGXIn74SQmo5dm2g1DolGuaoKI5M2TKzR_FPcJnPEUf_Uf06JwsRtb2lrMfnx2Oa1AWUe8VsHpJo3Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=Ixskz9Sxa-r0LzKtYaTZczAwkJIjtf45S5Iv1oDz6bk4p0x1O_RzDoDqw9rYjBFN36i5ezffWAYBx3QAzKKZnNAYnP_RgrLnma1CsGQZ_TO5_BgyGkMriC_rhAYdhEM6TUj6DN8xsgp93tWIIEyrui0PYlU8P9mUgJEyFTmwOvl0odIICY0dIhu4BDmcbxFXZNYQINsJzLJ3zl2ldTrL95bEet_SgcDgL0S38yKYMwBmaiilRBE7f5IC4bSQfPJ5g8i1fpjIS40mWNDPPW9o3DWxpoElljvbY6bd5n7GdZe5s598XVAMAT4YNDNkBErmWhDdzcMcDcq04YvC_QAtZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=Ixskz9Sxa-r0LzKtYaTZczAwkJIjtf45S5Iv1oDz6bk4p0x1O_RzDoDqw9rYjBFN36i5ezffWAYBx3QAzKKZnNAYnP_RgrLnma1CsGQZ_TO5_BgyGkMriC_rhAYdhEM6TUj6DN8xsgp93tWIIEyrui0PYlU8P9mUgJEyFTmwOvl0odIICY0dIhu4BDmcbxFXZNYQINsJzLJ3zl2ldTrL95bEet_SgcDgL0S38yKYMwBmaiilRBE7f5IC4bSQfPJ5g8i1fpjIS40mWNDPPW9o3DWxpoElljvbY6bd5n7GdZe5s598XVAMAT4YNDNkBErmWhDdzcMcDcq04YvC_QAtZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
