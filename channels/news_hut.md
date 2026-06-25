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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 14:05:40</div>
<hr>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghmdfMax2F0hr66slIwHj6W0aUFGdByCgKpxzCPncqED9V3c4jJB9nRyrgy38zCUPREjMWnUnW_RKW8IHWGoR_UNB4-t_QinAn2SANCIcCJyf_oXh_XShuXiv17D-BLakCM9srUWwzpic33NHNPgNFV0ZvAG6AVqzkLOJaGM108WAQOsA007R2EpVW-aKpmy1PIM11ax2-vIfkzlvrE3W44nsy901l2Y93hnj0qSM6_Ruj8KUpcKq6aGqh142QtKiCVQQ6trbwTkWtVh56FgsQcybSetwVuFXbaOqd-EGIRNeFnnUd_w4vkOzbJ_up3VACyhjkcZoD4rn-HzRCI6UDz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghmdfMax2F0hr66slIwHj6W0aUFGdByCgKpxzCPncqED9V3c4jJB9nRyrgy38zCUPREjMWnUnW_RKW8IHWGoR_UNB4-t_QinAn2SANCIcCJyf_oXh_XShuXiv17D-BLakCM9srUWwzpic33NHNPgNFV0ZvAG6AVqzkLOJaGM108WAQOsA007R2EpVW-aKpmy1PIM11ax2-vIfkzlvrE3W44nsy901l2Y93hnj0qSM6_Ruj8KUpcKq6aGqh142QtKiCVQQ6trbwTkWtVh56FgsQcybSetwVuFXbaOqd-EGIRNeFnnUd_w4vkOzbJ_up3VACyhjkcZoD4rn-HzRCI6UDz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=UCPVHZLlEMFsk5PAjBupeIrqIxctUmjJYwO1ENycvwO33sU2tfYjburQJFIC2VGAVky6zpyq8C9pEyHcTfof6uLpX9m196bqlHgb_hPMI0IWPpkuYn4SxcbtdMIDfyrsZrQ0YMnH4mHdOxZfgfG-3n9pNM2owzQqCcMzrVLaPs7YGtE3BOJScUaGjzZH29yO5gdZMpI28RL5E3sX75ubcvn_4ldQPBr2nffvsEZaXl6uw4SiXhvEHiAnGXBuJAbPAG22v4px8ajE0vp18toz7u-B2QpHzDhAW4ACpEh2OmNwUKkskAqeEXx10aYzaTIjQZ7_8fVksSIbCHrQ_-uj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=UCPVHZLlEMFsk5PAjBupeIrqIxctUmjJYwO1ENycvwO33sU2tfYjburQJFIC2VGAVky6zpyq8C9pEyHcTfof6uLpX9m196bqlHgb_hPMI0IWPpkuYn4SxcbtdMIDfyrsZrQ0YMnH4mHdOxZfgfG-3n9pNM2owzQqCcMzrVLaPs7YGtE3BOJScUaGjzZH29yO5gdZMpI28RL5E3sX75ubcvn_4ldQPBr2nffvsEZaXl6uw4SiXhvEHiAnGXBuJAbPAG22v4px8ajE0vp18toz7u-B2QpHzDhAW4ACpEh2OmNwUKkskAqeEXx10aYzaTIjQZ7_8fVksSIbCHrQ_-uj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVaJLvGAl3DMspMR8Dw8wMCjDR2FZnhwZuJOE6rmyQpvOZOCWsOATv9th9ceKOYlCHWhBRNiYwcxQvDKxwfmeS8VfpYFhCiKAOk7xU7qHxGzxmVV20YXV8nqeSmr_2aEgtb86B4IRP5epFtTm3iYbZrbCkhiGVPQozRX2WtoLUhO62sJstTeoI1hbQ8ggMxcbbDTaK0yWbCSmNuyaJmCZOmcZfZF5UcaeFhNWapqlbHL_92MUWzPBI2JaI2HThn3n0ecjJRq93YP-2MR4jumqrcUIBB7bvllTxbk2Xw3SPyitd1KtUaf5qeuXeCICahUcyJOr_qTo4xaXEIwkQ68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhADblqcx_-IfzWpUPgHlIimFk6IHNkcn1YrdwHBMoxw_lCSZeF4Mrw6xc-AYBdXvSp5uwBYJ2W12BS11mQcpW5ZFO_gKMe3CaYScdXprfMbgmwzMZLy-sd--V36zMpkRqnRjLWGY4IBeULOz0iLCO6Urpw2wrjZOhacK5fba_KUv2JAXt5-gkm2yjnEED63ECkv6vkhvmGRjmC3Fcqjy8OachSz_FbWjq0kp_uak6Fq61qzrb0AiD2fOjYiHYIh-z78R8THOIDd3ZS3tHOi_AoRf1gMt-1AwcIl46EcNFvUYpSGp3xVa2lkvGUsL_aOEdTMG-OLOlB2CPpfhCjqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=skB2kOB7AN2gK18uLzFBUQaqIm2ZhjZPhVSziydyV3DI-21rK1nOEUovzTcOU6j96qmei3T6tnt218qnKsUsBmnWpp5kpDxRLKzOxp1tTvCvYKS_I6eNPwwyr54rVghvo8GLRk15y5vGvhGrUKRdA11U14DjJs2sHiDvwPbEWS_EGb3O2umVCeBwrsJ5dpfsmxY81tQCT_dz0Mga9jJBkWk2lekHlPY6r_vvCLSf07SXqh4rKO2xSVFfF8z354PEnYUpIF7Qmg-sdV-l3rRI5n06C51KW7dXyCfjVJZfBGTV7BUGl2BWdqpOT5p9nHu3LWWy00PA1HZGv-w4mwOBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=pOmV6pv9zT2f4uK8rPAqPwElMW8SAXR3ZB3zdJlRpA_Yk-fNqOmAvsQ9wgve_1yRhDQLOVyPJA15ey6Tb1Yv4V27B-sp-OKoH5yvwi9hqMkM3HWZ6nXbdpOKJ6k7xePUO_0uJ2vsNDR3GxDdWa4ZEqojXR33XJzadBEd6Ngo5hbr8YAX2028sbR5i6WaeA-AWqx16RG7HkJ7zismdU-5RHfYGaqZtWI9G7mwhDQ_iVdtm_vE1h-lLEYN2uQrHXabaztRppFYGjayA6b9Pb6aaH_nDvZEmj2lBigQJKs9mMF7B1T69GMiUhk8In65rq5XuDU62A_5G_eM7MOUHBiMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=V0GAlOEIq9jq-SEJiXwIGSy99YC-37u4jDgL64fTIrEOFDX8qfM04qqd-89gx7Zds6G-dacLDMqzejIiRnnvSinrm0iEOF61fbRie8h4K8Enix46xjReMGOygEQ4By5v6bgzNZSLXT08ezooJk5XI6gio6U4AhkJr6vS5MoFzHWs-wUz9hsgpJ3-I7G-QPdGWoSAjv_4oFlqAkYpeJkJkY4zyF_-yo6LIqNhnh9zD2HUUVgR60NF6ijYIQp_2LfVWrTUqYgSq4TTVBJcr2t7HjMXLc9nbqwk3Y3gQS4Hm0CVKGnjYLFWfBRtkRCKoaWLFw6HA8W7KYHGhjB_UBwGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=enpSl44m1ZaFIt0n5K5rEm7JQ0tWY99TNlCqghFjt1XBVmSRZWwJFkwAvFrz26_iPkwpyPqO7wl5Lkr-YdNpK9lnIBkJWAVkcsIbkm1yUtJ1-d_v31pPvGtUVd3Y8ADHIWO9ptLwrMzQnA4_9zxFNkuUruHRU5j8NwaVzW80fyAAgt-SgHIIRr5xrh9s-7TfeIdeQeepb4_Qc3AKQMpAsF8EVneApAr5jc3PjpG8KfrVEOzbo6IekGW4dXj4ttcPrLskobAO9Ut4VdCIiCGEo8h04EUwHpY8jCvrF2CdQcuXAurMH7bRhCqukoLG66H9jkV6-RkxayVM251VB-PSYB7BW4uuTsDt-KEHZrntFA7KdmRnaWsNZWGqfNeRvVJoSVxbZg0KvtWNEShbZ8uZ7xCEevT3g59ZaOxSH7tx__9nSKT-PpEQZOPTK6SgN_l3eO88zqp5fSKWiRk62KJf0k6WTbRSpkhxNZo1JNINdsgMKn92OrIn51tFzAQUPHF7QWG3HhBZLBF1dqLQsi7RKnPxrx2hnMp57_gU9Ix4yTNBg1Cwgf41BKdby3OOsgBObblxCWsNR-iGFMeW2SyzaELwsjXAhZc8vUqHGe-8p_ivZsO9SjsriHqlk66331RAk1gtYI1Tn2UU9P74D_qwo47-3xewyrhA47DqhRp4KfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7AvCv_PpXyOpZ1OhHftVcAqTR2gGUOFk5ok1UlFF_3b0woVLToo2gd6XH_CZVVh9MnxSIIqncx68J1rcLpRisTidybVj5Rb-mPeBJJzY2fVmiDhn-7OesWyecFheN5vBCTGDLye0oF_plGIU2cTIc6ZHXKtPtpB1sJTcHvnNwYIl1nzFlTaQtSOhs9HVeIu0XPLxMNcqEweInJUVj-gr1MeFY-63DWgb-pOSre0GIguPG8YSgyhnPAcf0LGcZEZlC6a1G5zd7i0mc4kTehAcr2S16i8ZP-uvkxrEwYDzigS7upM-mWGiSHSFjCNN1qJc4H1y2YQBRQv3ducR8_wzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IRgMS3NMtSBAkJeRBFZUlzZx_IE53OIZ4cOCYWYlHpI5oNKiom6VwWr6hUrjyAme8rDOjz_hx6vyuwgy5w3pCmcxE4DTEES8zuYf9uraAy6MP_PGJ9VgxHg7sA5m9pKdbxutXQc0kvbUEjasDiu0NWC9iG8gqSBQCvC82LD89uh53X8vUP24kZkqkF1WLGG8_COdzplBGp8rbIJD8Fiko2LyRBAb3hBmEOBp6iJexwiSlFfmEI39rNbYKZwSoki_16yscuZgNUE_UP4_FenjEWSe-K4m16IMPnsu404abrNBRhMa9Mj7tFyzZc0Q3RIY25MqMgYmfbcShbE_mY8rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=m4xis0tNkJH4KtG6lTcVjEf5602uOUyW7GZ-WTJPyH9MgpiUFrv6_syNKnOnkh3enamdnNLd6XzMvNMR8Jkya3gPcrON6cI6Xp-b_nmsoggSqXkrzAYtkwPu943_pgLIVyE9JJrQkzpcinzqitg4TnRdncUq6o13VPSoOTRj3vxaTDyZzXuYL839GrLFQmvVPRG3bKQel4JwD6BER-az3UlcmnIzgH_y4A7AFk9RELJLf4NSu6jcwmYUMDJhPBzjf31_4iVA6Nm7w8VzxGhZvdNmMPWtBlbRJ5yG18_154SuHi81QYwlXlHp1vhcqDG1QA72rqbgOXPcdCwoJfy7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=Pwxb3rhip5iRBX2OqYsBNyavQqLhTnNlRteSjnrxPmllCHJxbg3W568rPvhNr0jsqXkAwsMULadhHSj-rZGtkxFZj_X98PSYisDdBsPs7DYvidzg_0MZhVE0kzH7S1JAHtXjt4YX03qKDMDkwHokhd2sCyl5eUo_ejZKJewh9hT654fbiQ9OuD14H3znSuVRI7D5MTPGqNSs4TFxRM0DwSSpZ9t7yOkmUVU61nVgnatfOfgesBvM1pWLMKPD_0_hI4Lme3E-0Wx26NrrjkelWvI9wmXntDgzc4lCTni1RF4rPnm5yCIlyuKx9Q_gQvEJybwM9AnSv5KcAfSFy0wUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf83llMcxzFzCG1JUl28AxVsqfDU6LsnH5QzxyykXH6Za9oDc7f35TmVF1dL2VDcmRg7TyTlj2b_VjROmy7_dBTiyPTHoUTUKBq7-Q_TLSDjExVKNX3uPRJfyPKZwzd5A7kud1Lo6Qj8SekGSjyNyskjlBocDL_eVBo7BTXLLAn4FPnpjLDbcgW_r9uc3m5bEUmohilHLBDTD6GgFlr-jT7aQ8xbC43cvg-nPI4Zr7iWDjlBK_DxBuMyJzArzVoQWSr0tsVZS035zYnpMPnTarzApSwunbhysEbKnspwF3ent2jrzcNIaNUAJ-5vIiUpzHpc0PYBZLXFdTFm1FLtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=ILYYpWdax5JWwEHwoxSlcNlrsoOWAVLPbjE2CcTM3LsAohSsor2TgxuuNFH7ywdbu3lrUzG18DG7PS_ZPN6JrrfkK5G9QboHkzZRmWb4hwKiA1NGwpCAvkCq4n7vqlOlltZdSThnP5xVXjk87_a_2xUafz-Tu_vQ9yeznyiuyADx-j5ltttMfB0T8BfP1LOQWR8tbQw2X_DjzosVxergnMg1ARG8G6N1TEvNvFW-ip_1vrD6KudExelaOl_Y3mL8K23TNKGWcmu8lNyM1qNU-D0ZlWDNZhZ_qItSNK0Jw47OPxUxbShK7pq4884wD0aDN6yDs6NlbEBfKomWEclclg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCvNyyKFqsy76GYzl04zVFmewxcsaej-Bg7Incf45UhzepV-Riz2cAHXpQALWmg7sGeH8DnZbzztcAPlKLWEyB56RDO6uo6OndGVhpHe75kbf0aGiaGd9eLoHhIgjdy3pQZdarP8NUHydkQKqoPR_mEXkGWWG3CqJWaXmSi4Tv6umqsEqZq8JicmxTGTvJhXUAAE-FhRn4tNyE6WxljnVSDSXy0mqMN7mrZqNCqGofxzyUQAsi82iLATCZ0Z8rZfFWDL1HD4kWWQoFaMacymgJeNwiLFYbcMAao6maDcX7e-A9TzUs3701dSpir1g-hcfx74ILCr-_daOb4vc_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn-x7ttPWc_9zpRzCeH1oxNGFxad5rfy02hrc284azN-7SblDg0agTWBm9k9jns41yhlM1erbER8NWCLsNk5s3zGluQNJKbhQ9lYdTElJiT5YQkrJH_x6VpBlq7e-uBTUSJi5ymGk0LcVBM_daBQHQUioALnUjQvXvM8ivGsRkcxo_k0guNhjphZa_iNoU3EfM-LAqDv-TlxAZKfjPI8F2yEsMSRod4SSxWfQEHjEgzq1uvvzwkcPU2ZU1FuYwuHcUrXClE277uyw78451gjtpKDNxA-QwqT7LiXwBlcSBE15YV_00F6DcL-ZJOJZ-Bxs4jcFlcAOUlJm_egl8XyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWC8tVNL1QbL3OWpsyFatW1Wellno3JBNiCONWZ8B9U_MuxGemDE-41gd8meBTwGOVpzuzIESByrDoTjQ4dmuUYKX6LgaxSiMNC-to1YWe5Z8ykQFO4RmXTZrA0jMVr4KIOnFfYIgLh4f7cIdhpal5P7AGINbEolhsKCG_bioTY7tKxLLJg_Axstc5RAVYaMeWH7BMNs3lsnUAPrOLg0rWVekYZ_Hwqz5S03kQflRSOK6rNuLzUMMMpCG0BQ5wE1p7d9gmE4kMAVMtCTxfbb07JDLAc6dGCK253bzPN4y8ukaE34ov1zrHlAy3_3kU6nB-hzHFaouQTymOo_AQNNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=qQBPJaQqFEXA16voNbupPxd-0ZclijzlsUo8Qqs_0jLB2JptRKg2-cKOxDYtcKQa0_Vt5XkarF7G4QpestmqtgDUSbQaKhQYjPsa70A6Qzvx9S89JsYmVpq2-AAkLW49q4KMua1OagzpugzKsIwmul5qq_2f48FffBy_LaYn-oiSJ0HSkfPq-fgtWoRayLyLK44dZutsGNhyiVnrFacuCSJICB6GRj3CVmeUYYuVyDx7BsprFulw3bSgd0oiqjRqu_r4jxE51EMkLB2uR_Y2ve3Y-G1CWZACqFQg4Fo6nPnAvvz7JdSmdlDWbr-A4Fmru9ggZ58jyBnREbYtRUyP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=qQBPJaQqFEXA16voNbupPxd-0ZclijzlsUo8Qqs_0jLB2JptRKg2-cKOxDYtcKQa0_Vt5XkarF7G4QpestmqtgDUSbQaKhQYjPsa70A6Qzvx9S89JsYmVpq2-AAkLW49q4KMua1OagzpugzKsIwmul5qq_2f48FffBy_LaYn-oiSJ0HSkfPq-fgtWoRayLyLK44dZutsGNhyiVnrFacuCSJICB6GRj3CVmeUYYuVyDx7BsprFulw3bSgd0oiqjRqu_r4jxE51EMkLB2uR_Y2ve3Y-G1CWZACqFQg4Fo6nPnAvvz7JdSmdlDWbr-A4Fmru9ggZ58jyBnREbYtRUyP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Z1ME5deu1LoFpGrNj7yI40ZMz1eKmEnsHWba7mnB_TEfj2vaFq9MYNx8157fjB1IWLL-sAChuFG5ccNDV_7znenJX97MSlZdzDNTE74QhJSZeQKtfeaitn6GtYfkSr0VLBFbfpXYHdMJ1rZuzRQk-xlwpnWXWwiqDTIksNw2v7PAiNYkleefZzfZ8HKbe3KQptauJ0FtjzHKRSUn43IPJpIDVUPH87Z3l7x-9lkHXsobwcqa4K2ICEzOFOaOkyG4L7RqA2ugoVDqc-piPIQgYjnyAh4_R8jLcqwKUdpWFs7z_Pcw3bnJ9KXH2v7kNFz4oiOlemhJ5v9w7bCBjHD2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Z1ME5deu1LoFpGrNj7yI40ZMz1eKmEnsHWba7mnB_TEfj2vaFq9MYNx8157fjB1IWLL-sAChuFG5ccNDV_7znenJX97MSlZdzDNTE74QhJSZeQKtfeaitn6GtYfkSr0VLBFbfpXYHdMJ1rZuzRQk-xlwpnWXWwiqDTIksNw2v7PAiNYkleefZzfZ8HKbe3KQptauJ0FtjzHKRSUn43IPJpIDVUPH87Z3l7x-9lkHXsobwcqa4K2ICEzOFOaOkyG4L7RqA2ugoVDqc-piPIQgYjnyAh4_R8jLcqwKUdpWFs7z_Pcw3bnJ9KXH2v7kNFz4oiOlemhJ5v9w7bCBjHD2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=cfIl_f5RiLjBIK-PXzPyjoJTLqGQiGNjQxsay1LilZcGpucr_n5SW-M6hEktqzSSB7PQDbfvtTjoXMU3YeYNP0rDm01mZUDWpguT6x-AKAs3Jpo7RB6jubVhm8f7CnbF3NeSbgPQVt9Yu9DseC20q6CRJCMqUUHOK6VrA-opxzhcRLEnDWTT0CJB_cCchcrOF2oqp_CYjVyvX3uoKtuwyaU6TvOcgVdkbRZ9QqwQ8__Rl-0QCIzpUu5QlGWMgbz1JPw2SpVl38eGw3ug6Ne_KRTjKfrWiZM2vBf79SO8oU9MXLsr-4PGgR2aZ0TGd7E94Ln0SZpbyV6Lsc9kCwFyCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=cfIl_f5RiLjBIK-PXzPyjoJTLqGQiGNjQxsay1LilZcGpucr_n5SW-M6hEktqzSSB7PQDbfvtTjoXMU3YeYNP0rDm01mZUDWpguT6x-AKAs3Jpo7RB6jubVhm8f7CnbF3NeSbgPQVt9Yu9DseC20q6CRJCMqUUHOK6VrA-opxzhcRLEnDWTT0CJB_cCchcrOF2oqp_CYjVyvX3uoKtuwyaU6TvOcgVdkbRZ9QqwQ8__Rl-0QCIzpUu5QlGWMgbz1JPw2SpVl38eGw3ug6Ne_KRTjKfrWiZM2vBf79SO8oU9MXLsr-4PGgR2aZ0TGd7E94Ln0SZpbyV6Lsc9kCwFyCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=f55AhcWqFhAJ7UXsUnDGIaGC9Cnbq_Sw3TgDXtklHw3XJNsAScJo25P9UEARNw2dDH7CBBz80b7648DDusjIoWX_wB36Thk8vYNtx-fIrd1JgZOrHFjBFi10aCoyABDABdtJfl1s11aw98Tecgabb_VeT6fDCElNNGeUm-oJZhdv5paOEn4eZQjht7b9Cr552wl1gcL3C2-HFfu4qHKsy026mYarlHuT4omWKZCgkTHCSrc_jNPHCFNFR1JK9Iqo7nLyqyNqwx-o4VBPVRVBrCQaRu7oiIKMp9hIDR2nyhyY0RAPXH8ztSS66AOUVxWCuqjyYretTeU9ZzH27Sa5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=f55AhcWqFhAJ7UXsUnDGIaGC9Cnbq_Sw3TgDXtklHw3XJNsAScJo25P9UEARNw2dDH7CBBz80b7648DDusjIoWX_wB36Thk8vYNtx-fIrd1JgZOrHFjBFi10aCoyABDABdtJfl1s11aw98Tecgabb_VeT6fDCElNNGeUm-oJZhdv5paOEn4eZQjht7b9Cr552wl1gcL3C2-HFfu4qHKsy026mYarlHuT4omWKZCgkTHCSrc_jNPHCFNFR1JK9Iqo7nLyqyNqwx-o4VBPVRVBrCQaRu7oiIKMp9hIDR2nyhyY0RAPXH8ztSS66AOUVxWCuqjyYretTeU9ZzH27Sa5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=bEN0mb_Vr8LDXuzUAJcp4mxnL4WXVbIJ38rcngrfXaQtuX0KFeRJsYvZMiogzEydn7lCFVRDWlfHK2urqjHEUGwxKxLiTTfwMnB3R7NUtPvGMOCODiax7wo4t6j3QvhL-rUKOpKOwaqFZrXh7UaDjh3i5aHFuYrVfH86yGMwrFowndHXM8dA3uwDLFiw9lF8fWmi0FzfP8U05TqbQ4h6Q7Zny8DFswL0eQpde3Gd1PtdJ_xSCOlptEn1X4K9685n_PRa6lugUkCPFPW4Nyrpn__xzUH2MzX5-Yuzpu0d3G1LnC-vZxT2ttVGF0S1BQ0OLfhRxPn0Nnpmyih0BlRFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=bEN0mb_Vr8LDXuzUAJcp4mxnL4WXVbIJ38rcngrfXaQtuX0KFeRJsYvZMiogzEydn7lCFVRDWlfHK2urqjHEUGwxKxLiTTfwMnB3R7NUtPvGMOCODiax7wo4t6j3QvhL-rUKOpKOwaqFZrXh7UaDjh3i5aHFuYrVfH86yGMwrFowndHXM8dA3uwDLFiw9lF8fWmi0FzfP8U05TqbQ4h6Q7Zny8DFswL0eQpde3Gd1PtdJ_xSCOlptEn1X4K9685n_PRa6lugUkCPFPW4Nyrpn__xzUH2MzX5-Yuzpu0d3G1LnC-vZxT2ttVGF0S1BQ0OLfhRxPn0Nnpmyih0BlRFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=mhkmr2SYjFb_KMDTzjj4r1r2BVKPT1FqgZJHlO7ybmL1EVpqLTUqI_neA9ZqK-ZgdQMOkDre4unVFVqP2eLG2ZT0bMshL6IbUkhirZi8wWxVOOAb6J-OtpORx31MD1sf2WosGDfBviiZ0xgJn1ZLpSQey5AQqgfSdFHcwna5u_ESktNb2jarM3L47NTREScpN1NEcGqPuch4oemlCYLrsamhfKVTwEhUCoxfO4nCRgpF8m6QKXGBMhggsTL0eiKjd2vjG6iZ1-TJPis5UfSoueBM-K7dy00CXVNG_qfnfTRhk6cAHL6mC1gQjje0tS1bFK0tGf67igqilorFRXEz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=mhkmr2SYjFb_KMDTzjj4r1r2BVKPT1FqgZJHlO7ybmL1EVpqLTUqI_neA9ZqK-ZgdQMOkDre4unVFVqP2eLG2ZT0bMshL6IbUkhirZi8wWxVOOAb6J-OtpORx31MD1sf2WosGDfBviiZ0xgJn1ZLpSQey5AQqgfSdFHcwna5u_ESktNb2jarM3L47NTREScpN1NEcGqPuch4oemlCYLrsamhfKVTwEhUCoxfO4nCRgpF8m6QKXGBMhggsTL0eiKjd2vjG6iZ1-TJPis5UfSoueBM-K7dy00CXVNG_qfnfTRhk6cAHL6mC1gQjje0tS1bFK0tGf67igqilorFRXEz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=myxW50oYL6O-tOzwzkd10Z0dCSJAFEEFmfh4UmLZWeClBwy0e5_6ABku9FGYXX5gCJvFPj_7_6QoanwUT1qG-X6375C7lRXasxRzOiA5XQvRd05sIHDowCvwiLgVMtlX1iTuuLK-Ues9PBBKcfnp25uwCrCwaLepNjYtUarAcyFMBjJFWv_JGzIn9s946J-Sp0dEKGCmbNiIVL6om1LHc2fQNrjoYC6ppc22HuNuZTVz1Lue2eiAFUNuqxk_79YdEv3mpamduDgDgdlfXmp4L73u_8axqgS91gnCr5YRXxrzR1tZ5tPyjBBOZy_R9HVRhOI3NR974marHjDtJD14rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=myxW50oYL6O-tOzwzkd10Z0dCSJAFEEFmfh4UmLZWeClBwy0e5_6ABku9FGYXX5gCJvFPj_7_6QoanwUT1qG-X6375C7lRXasxRzOiA5XQvRd05sIHDowCvwiLgVMtlX1iTuuLK-Ues9PBBKcfnp25uwCrCwaLepNjYtUarAcyFMBjJFWv_JGzIn9s946J-Sp0dEKGCmbNiIVL6om1LHc2fQNrjoYC6ppc22HuNuZTVz1Lue2eiAFUNuqxk_79YdEv3mpamduDgDgdlfXmp4L73u_8axqgS91gnCr5YRXxrzR1tZ5tPyjBBOZy_R9HVRhOI3NR974marHjDtJD14rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=OVDRAOd4E4xxzbcP68xOkKGvdhXTNIsQQ5gGjejaCFYoZvJvt5on0_HHKqV-Geg5cboV0EJ9UklhKr6dIutoaB2FOA-WA-4IJlQySgrZa99DLX5R_0TEFCZ_hxrXZXWuVbaww7SHtKOcKogoZpdKu1cu0r6IxSuLBSUwiVy-SeBhIBcS7w1XWF13q3o8znCeneyoj8jae_SMxMNaCh44x_ATkY3RFm8EmNM-sPp9wCTUHiFiGjKl1DGJOWfjNsIK_ch5nYOWjK3tin8a4opG99mPOv1HyvpvTuwstzjlKWJC7Ojqo2UbemAI7jsTQDI6NmNOI-7Wi08dqe0FfzpdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=OVDRAOd4E4xxzbcP68xOkKGvdhXTNIsQQ5gGjejaCFYoZvJvt5on0_HHKqV-Geg5cboV0EJ9UklhKr6dIutoaB2FOA-WA-4IJlQySgrZa99DLX5R_0TEFCZ_hxrXZXWuVbaww7SHtKOcKogoZpdKu1cu0r6IxSuLBSUwiVy-SeBhIBcS7w1XWF13q3o8znCeneyoj8jae_SMxMNaCh44x_ATkY3RFm8EmNM-sPp9wCTUHiFiGjKl1DGJOWfjNsIK_ch5nYOWjK3tin8a4opG99mPOv1HyvpvTuwstzjlKWJC7Ojqo2UbemAI7jsTQDI6NmNOI-7Wi08dqe0FfzpdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=Les-_6qJ2EDhNbQa3JgPbFGitptYDO8Mjm4V3HmaQwJABoMOHoo8_JqvUXNcp6n42ZLwiubGyQeYGf0nQRMOeYsSUyyfyIJ4UKcciPB6x9ju6a0hZTRhrBKLmoyKPNzP-FAq3Iy0vnmhwe-FnCPccdOEecwhsA1ExDinnMYFlV79fYEo6QBBL1kTMgNuXaGu7HrdncPa-dg7iCSzWZSFoxVI0u7-7l9EJRHmf8OxWKTT2vgDOKkRdN7bejwRLag-Iy6kIWTc-afd4XT7shu0KgNA1svmDFBfMmQ6gLaPWA8KiiPjPuBONXrFSGI5vy0UT3TAMPYADKqj_VbAubsnFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=Les-_6qJ2EDhNbQa3JgPbFGitptYDO8Mjm4V3HmaQwJABoMOHoo8_JqvUXNcp6n42ZLwiubGyQeYGf0nQRMOeYsSUyyfyIJ4UKcciPB6x9ju6a0hZTRhrBKLmoyKPNzP-FAq3Iy0vnmhwe-FnCPccdOEecwhsA1ExDinnMYFlV79fYEo6QBBL1kTMgNuXaGu7HrdncPa-dg7iCSzWZSFoxVI0u7-7l9EJRHmf8OxWKTT2vgDOKkRdN7bejwRLag-Iy6kIWTc-afd4XT7shu0KgNA1svmDFBfMmQ6gLaPWA8KiiPjPuBONXrFSGI5vy0UT3TAMPYADKqj_VbAubsnFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=Wig3-TAHUVszW2nsepB7xIwZVmrLxLD9wby2DWSLgEUXfkgoyOaFykpJGpPZOX3sAJXit_PF_AF6JbL5IlXP1fXmVOBfNg-inPAut3CfDIk4hV9-_mGqmHWkQaIr-_OSQaubElU1qzZ2EGRNqSEt95ahHw6lBYRRRnu0LoUQ6Ro57sNPWAwSFIc2UoM0NzGCTODwNvj_0NxCcmxPLLCzyooxk8ZMUgkvoPSwSRGArVlGvQybWK9UpNLTclREUAsZwzw5gUkdoaKe0c1B3LttUs7cv4p6NgsCa_SyuGBYJIcHFgbKoNgCwOJNmc8jTRisSEVBIGxGxw8v5c-FH74JQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=Wig3-TAHUVszW2nsepB7xIwZVmrLxLD9wby2DWSLgEUXfkgoyOaFykpJGpPZOX3sAJXit_PF_AF6JbL5IlXP1fXmVOBfNg-inPAut3CfDIk4hV9-_mGqmHWkQaIr-_OSQaubElU1qzZ2EGRNqSEt95ahHw6lBYRRRnu0LoUQ6Ro57sNPWAwSFIc2UoM0NzGCTODwNvj_0NxCcmxPLLCzyooxk8ZMUgkvoPSwSRGArVlGvQybWK9UpNLTclREUAsZwzw5gUkdoaKe0c1B3LttUs7cv4p6NgsCa_SyuGBYJIcHFgbKoNgCwOJNmc8jTRisSEVBIGxGxw8v5c-FH74JQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/essFBmdJsv6kEKgOzfaQg8yRVS-dWI5Y3L-M9thLBd_L1aHoP5HgFJHAVHLNHLjTdk0X98fxwXed9qy9KBjApW6PSKGQ1sHun5cJuBv0UfTe2n1Y1QKevYl2SKGlsXNtdIqHg5iDmqB5-6bcr32nx3-dXOrYWOSN6SUNJoNq2oEo-y4asUlBJvdehtGHVJOcoy0jtACd3x90dkd0ocrS4NZdmZKfj5oZ8QZkEGePnGvMFvUf7drXdcKYXt5VPMbnkQXagp2uBFBB8q3y663U8HwEAFDaQKYo2PSatz3-s3GXAmn_mCSeTrS6So7pOob1omBE_NP_yC4QFj7_UtQa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qanIfVADwGaSnBUKf5LsaypiAtYK3KeAwnpgQ3VuifNH785kjeHxJLEQbWzqD7tRftBL_adjuPkVKHReGsbMlTo0S-S01glnaYzpGRyG--0vPW5pVI2gazBsnRKUypeB1rEUtGLursJzrIOPEXK-jjQvavJNTY1tapuEEGHfNPutO-p86c-1wBK5ueoUmXwXb17hw6eSMe8675RegbRAMSgNcOLxdHEcxZTDsFYkjjKTt5j0-Z-l2dp054ChB229q3hxuo8FwuFENIYED46qQqOmG3q_7_mRaL2H2ctW0vJGVFvybQyWyiNQBNuSdZprlLkh9BccmD_9V7-BS_E1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Qxt_Nw9aboZWvVv5OzQ7xt_P3b-OvdJvl4dsuUgBDnWRVE1WATblltGL53Pn39ppkx4hh4NWTLgqFLAOhWN6N9xXD53CDavrOh6BFRrZs-Ma4svYpm3NHJTP79Bf3ishFDe3XjTs5T1ZsAOR6lBbnLFes7fJCTornCd-JoT_pP_vQYt1l2Oe2u9R0HqMsNa_pDOJ_-83dQL7BXOs1q9yHjFC1_pvPv30ZxC3zabZFiiOHWMsmfiO-duseGzs8MhDJE4_2DDvt5dXAi_qYGjN0pPmvmncLf38VUXWrTe3Ij98YYyLUTtHNaNC0gTRefwCY9UzpiT9Im370DiOqUBMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Qxt_Nw9aboZWvVv5OzQ7xt_P3b-OvdJvl4dsuUgBDnWRVE1WATblltGL53Pn39ppkx4hh4NWTLgqFLAOhWN6N9xXD53CDavrOh6BFRrZs-Ma4svYpm3NHJTP79Bf3ishFDe3XjTs5T1ZsAOR6lBbnLFes7fJCTornCd-JoT_pP_vQYt1l2Oe2u9R0HqMsNa_pDOJ_-83dQL7BXOs1q9yHjFC1_pvPv30ZxC3zabZFiiOHWMsmfiO-duseGzs8MhDJE4_2DDvt5dXAi_qYGjN0pPmvmncLf38VUXWrTe3Ij98YYyLUTtHNaNC0gTRefwCY9UzpiT9Im370DiOqUBMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=lNEGaYonvKgGF8669x_od-HkiO9jJ6na-IF9IV0wkuh4v-C5deYgP6Z01_byKxIQtmlK0Op4k-rLp_TgphCukW7nx8LcUnMI29ufSEm9VLg16qGVcSaIdGvBK7CED_L1e6vO05YjSfmVoF-CGT3Dmlv4lu5XJx12f6ojClwVz-3F9xWh9uBcAppLOg48kFHVVfTu-TQqSK1ycxFMkKJDZ5P7JjANTaDTdneHseWaiGvZtKw0LKPid3ExRjYi9Pf2hS2dwR4c5nNG3h_qgX8g9UW4p_HY8ZGQvp1AlRCIrjhmGt71wcQKnQp96ffOEWrQzDIPVNxEBLe57PD3opBjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=lNEGaYonvKgGF8669x_od-HkiO9jJ6na-IF9IV0wkuh4v-C5deYgP6Z01_byKxIQtmlK0Op4k-rLp_TgphCukW7nx8LcUnMI29ufSEm9VLg16qGVcSaIdGvBK7CED_L1e6vO05YjSfmVoF-CGT3Dmlv4lu5XJx12f6ojClwVz-3F9xWh9uBcAppLOg48kFHVVfTu-TQqSK1ycxFMkKJDZ5P7JjANTaDTdneHseWaiGvZtKw0LKPid3ExRjYi9Pf2hS2dwR4c5nNG3h_qgX8g9UW4p_HY8ZGQvp1AlRCIrjhmGt71wcQKnQp96ffOEWrQzDIPVNxEBLe57PD3opBjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=KZikcNJ5SBv9d1zSFFUID_KZdvBAQjhVNotYMj4a6mYVIKufSN_iouCG1kUVs_FRAHYLw3lg-9pJmaoO7jTnGHNR-rthevk-F_is7bJBsKnAG7Vcs_rcn3S-sXnuP3isI3ZytqV3m02Yknd5DyUmTaG3RsGKbXKnfA9zhtaTPDYjvXxdaOY5h9eOXqcbA6eqyIn_PJYwfirrIomgbxZHLU_yiAktvVMcG9z-Odm2bjp5hdycF3uu331_zEL_a870AnaDcVce5k4YWeIIqXeoGyNGN54dMGipVXkqmY_Q2O7BZ8Ezty1GvL_7hBgCSWIJmX911dZ1FYpWpLEh3SurXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=KZikcNJ5SBv9d1zSFFUID_KZdvBAQjhVNotYMj4a6mYVIKufSN_iouCG1kUVs_FRAHYLw3lg-9pJmaoO7jTnGHNR-rthevk-F_is7bJBsKnAG7Vcs_rcn3S-sXnuP3isI3ZytqV3m02Yknd5DyUmTaG3RsGKbXKnfA9zhtaTPDYjvXxdaOY5h9eOXqcbA6eqyIn_PJYwfirrIomgbxZHLU_yiAktvVMcG9z-Odm2bjp5hdycF3uu331_zEL_a870AnaDcVce5k4YWeIIqXeoGyNGN54dMGipVXkqmY_Q2O7BZ8Ezty1GvL_7hBgCSWIJmX911dZ1FYpWpLEh3SurXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=oATGGuSYOGAibe8F2Rk3pm8vcBH26T09NaDu_zxhyzWzD3o_dZX5zi7xWWuTxAa1VCd2tRbIiEjlTSC_PBIh6RNaeEcpxj1xqam8C2GBh_pZ4XieEJWVj4TtrJ5ipqN5mLKfJ-xP5MHb482HUhMkXmHrR4il3bxUMATg1AuuJU5J9yB1F0IPyBEpVlOPkAEGozaNjkR2zbbzxfuzHLUwfV9s-J6mnIffMCZdQi-CyNfPWIKFo2CWUZvthwYJSCrN2b9tQYN4lCO8aQxrPc2gVe2xF6Pz2dCwpNPwckD024Nk2bVWyiEFjzTNNjeMB53IJW8oa31nqiA4q7GljXIenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=oATGGuSYOGAibe8F2Rk3pm8vcBH26T09NaDu_zxhyzWzD3o_dZX5zi7xWWuTxAa1VCd2tRbIiEjlTSC_PBIh6RNaeEcpxj1xqam8C2GBh_pZ4XieEJWVj4TtrJ5ipqN5mLKfJ-xP5MHb482HUhMkXmHrR4il3bxUMATg1AuuJU5J9yB1F0IPyBEpVlOPkAEGozaNjkR2zbbzxfuzHLUwfV9s-J6mnIffMCZdQi-CyNfPWIKFo2CWUZvthwYJSCrN2b9tQYN4lCO8aQxrPc2gVe2xF6Pz2dCwpNPwckD024Nk2bVWyiEFjzTNNjeMB53IJW8oa31nqiA4q7GljXIenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7brWto_bGsqBQZfB5SjskU8YbnRgLHCHJuFrQE41YMhu1QNDLhsjYJkkxsk-OtGQHiyb2l1guu8Gia_gWzVgyguXsuOhFpHkwx3ApPpA3rKZAkhShF95yefVywgnMW2ZUgzthzvC-o_7RGSdRCdQjVv08qNV9W-UdgdmQ5pr3N7dytzC7-bIExnv4jCXmSNZ3yZgzEOwEQWcxhroC-7hlLudX3NgBQ9olD9_dFUY50j-vAnQxafFbYBpVV1oOSeciaHtTp-hcWVdE7S34Dk3Fh6JQ3XJg5kc5JqtXJdES5kfnpjDgKRRt9yC1xcTV2UM13qoOOrO_X7tWgTf0RvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDqDS9IP-XaALnWh2gf4UUxg1ZQ7jehKkM692FXZcdAcxnmBpUKfM6REf-f_BHE5iqdunbLrLGIgN6Ec6M_-Sr1Bi-XBQVxlZwQ9ioFwCziaUoOYYMbeLD2k3M8UhlEEeXYLfMNV5HK8nqSXTEFz_N0EqRMxvLUP7vHSRHwd863Kko6wdxLFTVVFG4lnSFbJsGHHcXWj_2JH82tIQlNDtFUAtmaZKoMQyQp9Q35hee94nIi7bc1ys9wtrsXGWiI9nX5DDZevoEIdRUTGObgon0Ub7wS8vRKaU7tMls6MgfX218z_OimRLRB2WUhwc8V2Yc7gm-GSKsscZ3aS4xXFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug3EvcP31pJ8q1qlLZzeSyAq-cMQwGAzpvph1iGSHHZW29P4HzvR4gfqzT_IKpdtgsrkSULZBx9CL_pqdG9bVqD3kfZE3I5Q7RZmLmW2OtJ1l8MLhnaOuhujvu8NA08iEl4cgQb2M0j_wXENHkXn8hx5wWPqM6RtCvy2DVpmkgsQ3ooqaT9bQpJIp2-wEV1ZnDfCsEWCYIVem_OQFiKTrZVN2z7fMR39MpSGobrsbPcGd7nbuQVMi3_H2DtrULpBzsJIjgCNGSsJsIUfoMUAYmVRwDlyeXGstQqQWTK7-7RGgIQxDRC2PkFyDImBlwUdxk8DimdCWjI9M9MLGCX1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=NgiRANaazIlVuwuAz2_J1hkUY4HIFDzUYCkXwuoDurS_cMFtJ9Vocbe4IyVu3iREQH-xDNEe74oK0X6bBIjjjFxjFx2gvWQU4AIbzn2ToFb2EsNRpH--OKh0a82ggvgt5K5usVfKMdq-Ey8x6kXzVZUeKPj-F6VmTCenQxT8Xh5sRxpWf402VnJEHAOPTarRJlNb7TnOtxxhM_i3-udrnwms-xo4SpCtoVaBpOmJ4x5mvfyq3Ee8ffQPKasMpmks-db2sBGIk7FXixCD3UMPB7suNA4PK1yKqLV2gr-Drc2-9vogC-oJ9v3NFtbuS2B4ypmVZ9qwODNgQbH2lGGHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=NgiRANaazIlVuwuAz2_J1hkUY4HIFDzUYCkXwuoDurS_cMFtJ9Vocbe4IyVu3iREQH-xDNEe74oK0X6bBIjjjFxjFx2gvWQU4AIbzn2ToFb2EsNRpH--OKh0a82ggvgt5K5usVfKMdq-Ey8x6kXzVZUeKPj-F6VmTCenQxT8Xh5sRxpWf402VnJEHAOPTarRJlNb7TnOtxxhM_i3-udrnwms-xo4SpCtoVaBpOmJ4x5mvfyq3Ee8ffQPKasMpmks-db2sBGIk7FXixCD3UMPB7suNA4PK1yKqLV2gr-Drc2-9vogC-oJ9v3NFtbuS2B4ypmVZ9qwODNgQbH2lGGHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=bUiT5qxbDeNCf3c6LLtaUPSCn3zUMNt_nYKnM3yaGKFtWy3O6wZlGfdzftkmz5q9YczGzWzNZfK5LEKSPa_kcHCMDiZHAtWxy0NdTiZROPXw6skALJFFn7QXCsec0lzbfOyoHnKMJgwPtehGWFc2S9OMUZKO975sNPCR8K5poa-TqVE2YlRRmOGbHfYuSS_52Tvg2tdoKYsTyoOLyiDBmIfzASb1WPovS0ZOWjmCrHu5wd24tbO-V8ynXAI_w3KfyD2x3k_dombFDgaL8MAhuinBWuFaFhc4hBPn2LdzANnpqcx6qdZwyYHX_pKDzsr0gIJo1x8kjfEKxYgqBnKe1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=bUiT5qxbDeNCf3c6LLtaUPSCn3zUMNt_nYKnM3yaGKFtWy3O6wZlGfdzftkmz5q9YczGzWzNZfK5LEKSPa_kcHCMDiZHAtWxy0NdTiZROPXw6skALJFFn7QXCsec0lzbfOyoHnKMJgwPtehGWFc2S9OMUZKO975sNPCR8K5poa-TqVE2YlRRmOGbHfYuSS_52Tvg2tdoKYsTyoOLyiDBmIfzASb1WPovS0ZOWjmCrHu5wd24tbO-V8ynXAI_w3KfyD2x3k_dombFDgaL8MAhuinBWuFaFhc4hBPn2LdzANnpqcx6qdZwyYHX_pKDzsr0gIJo1x8kjfEKxYgqBnKe1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-a58AjbKpKYjFjhEcD2SBgPRaE8CD5vc6ISIGlpWo8ula76mgwh-_r9EevFJFN5C5-RG-7CCHB7gtMByfPswRtcp9rsF3rteSZqwwE17n7xS7tIg0KN63pPclzBuWKfLRqj447jaLxCmAUn9v2RrcA-_igMn-Do_a0XVKrzvUotu-rcKNI_23m3izeD28zhVJhp8PfdVex_p1a_9N6-NvD9OdrJreD1pY0QoJonDswZFyfQUftKjO3xPHwoqQjMvfRgMF-EitWsm8VD21AEHIaKK-FDy3qYnnLxxSvjQFO8XG1QEwORpecB_r8G3kL7M26sIW4PPjoOSP6EbM15gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=eJ45inIOPbtZ4P5d4AHlff2poKbKGm3OkBrThlki_FtrEfFheHJBj2aS3qoRrE41TVqHlz1cLtgpB5rVLkYlIKbnmag6KA00viCsxa9mXXrS7XHZaFBlOY7syAcuNu7D8wsq9y1OrdXtMvAdjzvQB2YuKjRdJ12ceiOd3TNs65QMcHO7ff8SkBtsG2IxqXyfRa7FPS0pF9Tr5X7kmrle3_g-Q2YYmMxWGiKhb8Cag7Zq823nWV78KrHkIQR67bheu19eQ79aPBOir1qrw_12V9YLs3wUaUlr0LKw3cTywWCZzm6x4AqeMGo3TrwmQiMOztNPRVpsTEVfjbXEjVZkTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=eJ45inIOPbtZ4P5d4AHlff2poKbKGm3OkBrThlki_FtrEfFheHJBj2aS3qoRrE41TVqHlz1cLtgpB5rVLkYlIKbnmag6KA00viCsxa9mXXrS7XHZaFBlOY7syAcuNu7D8wsq9y1OrdXtMvAdjzvQB2YuKjRdJ12ceiOd3TNs65QMcHO7ff8SkBtsG2IxqXyfRa7FPS0pF9Tr5X7kmrle3_g-Q2YYmMxWGiKhb8Cag7Zq823nWV78KrHkIQR67bheu19eQ79aPBOir1qrw_12V9YLs3wUaUlr0LKw3cTywWCZzm6x4AqeMGo3TrwmQiMOztNPRVpsTEVfjbXEjVZkTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=fiZXJoyKq7JiRvOh4lcTrF7uq7bK-Ptuve8lK94q7HK2nJwDitop_1Ok1YS_MP2_yRqf8Kp6iONLzpvaMzKlSWfAIYz8mX2JRNv_mKFMBVLHL0rmOkB1jyXc-lPYP37daI4Lv1F4T91ij5LlAK29XZBswctzcC2bjoXBVm6qsVvWtdrJwalwHLA015GYTnAhtkXsFtlOg1CoSupXcXVmgQ0zc7zwEI4E1HeHsWpW8blWApFfdaxut8yUUjlorcnX1Uq-8UkvXOJkio-q8j0GkCHtNtP6qKQ7FlHIX2fPv_BPM-pOtADeIolgq7qOiI7_ZCS5sQeXVKb2NhRSZbZL0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=fiZXJoyKq7JiRvOh4lcTrF7uq7bK-Ptuve8lK94q7HK2nJwDitop_1Ok1YS_MP2_yRqf8Kp6iONLzpvaMzKlSWfAIYz8mX2JRNv_mKFMBVLHL0rmOkB1jyXc-lPYP37daI4Lv1F4T91ij5LlAK29XZBswctzcC2bjoXBVm6qsVvWtdrJwalwHLA015GYTnAhtkXsFtlOg1CoSupXcXVmgQ0zc7zwEI4E1HeHsWpW8blWApFfdaxut8yUUjlorcnX1Uq-8UkvXOJkio-q8j0GkCHtNtP6qKQ7FlHIX2fPv_BPM-pOtADeIolgq7qOiI7_ZCS5sQeXVKb2NhRSZbZL0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=NG2_zg9owy9dTgpDrTHa7GmtCRDy8MslttQa3ZsIWiEOtWqng8i8Ac6pplztdBfNVrrLxibc_Iw7I37Pl0DoStYwIalKGJZ2UfyAzNpjJ77nrTA3qIwH-rL-Yz7mKnSuI0oAZQkb57RMn7isDEw-Ge0OZCHQBsm4LyIXCaITiny97K2bgeEOwKuBzgUu6Dv6kFm1d75ILqjhgOOeN77n7JwdwSIrM9vMVTwBeg2ypr39luVpyNE6xV8X4HZud94PPaq4OYm0uoAV16NfXlaNTn5KxBXozq-R_0Ual8XAvdKjZwIVKXxthETDVUsbhRKRLK--KhXCYh4nhOL_k6_xVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=NG2_zg9owy9dTgpDrTHa7GmtCRDy8MslttQa3ZsIWiEOtWqng8i8Ac6pplztdBfNVrrLxibc_Iw7I37Pl0DoStYwIalKGJZ2UfyAzNpjJ77nrTA3qIwH-rL-Yz7mKnSuI0oAZQkb57RMn7isDEw-Ge0OZCHQBsm4LyIXCaITiny97K2bgeEOwKuBzgUu6Dv6kFm1d75ILqjhgOOeN77n7JwdwSIrM9vMVTwBeg2ypr39luVpyNE6xV8X4HZud94PPaq4OYm0uoAV16NfXlaNTn5KxBXozq-R_0Ual8XAvdKjZwIVKXxthETDVUsbhRKRLK--KhXCYh4nhOL_k6_xVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=Z_2RiW92RMxvXUstP1Qm0T3QrYlJM7xGDymGtT5ecoGX6wqw2rg6cdKV4EZ9uLzEHx_9B70U5eA9wvj3j12H00kPjIGka-qDs9s69IfbpMBRsQ3sKD4V2DTMEYI_B0-K9Vp-hPlvZzae54s-hefV2yIIvO0fYk0BC2DWVcgCEiXKowLBgkmxR3LmfDWu9ZvSlfunOj9JQacwxi9ODE5tR3fWuao3qVQKOENdjVUUGHMJUOTrzn2L-OkDcmDAvTv-MO5nEVps_UCbE9NH9NFG80xDTpKpr1XDgkEgfYHjFXojBAnUC0Gnvr65u6ALURjIuk4UaZ1Dl-1LTr7zYbhofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=Z_2RiW92RMxvXUstP1Qm0T3QrYlJM7xGDymGtT5ecoGX6wqw2rg6cdKV4EZ9uLzEHx_9B70U5eA9wvj3j12H00kPjIGka-qDs9s69IfbpMBRsQ3sKD4V2DTMEYI_B0-K9Vp-hPlvZzae54s-hefV2yIIvO0fYk0BC2DWVcgCEiXKowLBgkmxR3LmfDWu9ZvSlfunOj9JQacwxi9ODE5tR3fWuao3qVQKOENdjVUUGHMJUOTrzn2L-OkDcmDAvTv-MO5nEVps_UCbE9NH9NFG80xDTpKpr1XDgkEgfYHjFXojBAnUC0Gnvr65u6ALURjIuk4UaZ1Dl-1LTr7zYbhofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=iKyQvNUsUQorInkip_hwqaTb5_evk-vrMLjNax5fZJxq_AfHQErrQLKinlqmLAhVAXtCxGPDkM2pypwpkXJMXM3h1W5c7nC6HcKqk9ttS88U5CHhgmThdjrApkjNngpVWO2wBSUOFvBvsw8Vz8WMj9PuN5Ll03Y1fZY2Yt_BSt1hN6gcwTkBGjfq5U21RT7-uVTl2ihfWMQ4ylaJYP02LAP0Q4sDczVWpITrViKpWfs8pPJ5rDuTExtC3cPWVvpiFYB7OBa7jTq5T5PprZa2Swex1MqoDFQIekcW2OJgsbgOxWrGwj2a3xG2488-kGcDv3FF0LwBtFQdhmg5uulwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=iKyQvNUsUQorInkip_hwqaTb5_evk-vrMLjNax5fZJxq_AfHQErrQLKinlqmLAhVAXtCxGPDkM2pypwpkXJMXM3h1W5c7nC6HcKqk9ttS88U5CHhgmThdjrApkjNngpVWO2wBSUOFvBvsw8Vz8WMj9PuN5Ll03Y1fZY2Yt_BSt1hN6gcwTkBGjfq5U21RT7-uVTl2ihfWMQ4ylaJYP02LAP0Q4sDczVWpITrViKpWfs8pPJ5rDuTExtC3cPWVvpiFYB7OBa7jTq5T5PprZa2Swex1MqoDFQIekcW2OJgsbgOxWrGwj2a3xG2488-kGcDv3FF0LwBtFQdhmg5uulwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=fYyEyhejnkNbgYPJkzt1k9pLy2Mur60OpvRS8S4Ha82kKB4QNWCJgej-ZQTXqrBa0uDW3d7uIRpkjsDJnJwmdpVpWt_BfAJ4MKLKg4fmS6_K6GwGAev79QmwlUhg9JYRJ-WC1xtpYgaV8gWKarZYfJ4IkQ9XkFSMDIaKKAYlyDSGlJ7cj_uSyEkcdCWqD1pdJpHaV2pcdcX3y9If6c2QFjWlWIWOxE6G4E_WDQDe48S55YZLQ7VZuwnMCr6CYwWOUFu0LnpUeSiWs5aA2M-N_7CXtwWMLJkXq40oQzXGd1citC6GkOy-g8ACS8VrL_etr2VnctgvEq7FmM_4kaV3-aAQP9HwUj-MypGQ7C1L3KS82eMlI1mxduRxwQjmONcU3L5dU8j61Yd8px1cM0JNh-0Zq-azPHizQSMejEvpiDj9xAla7d1uvpl9EX0I-lDLwSaOQioygOcnvxLTl9ZH1jd6kD264GQZ470ltoR3Wst960QDYi3-3_3vtv_Gq6l1Vst6WoOuiscaVDuaGWwWOA424vneJx4O52Q_skmzng_UVoASsJVmd2hsahvyvmaAdHH3puCWlomYmcTaef-3L3A-Xruzu_2xUeEgH6KflbuHHQj1j_rubNQCIDG8_ETu-39qB2PYIcYXTvutS_ORPwW4_HLr-ys_5lbWA-v4-JI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=fYyEyhejnkNbgYPJkzt1k9pLy2Mur60OpvRS8S4Ha82kKB4QNWCJgej-ZQTXqrBa0uDW3d7uIRpkjsDJnJwmdpVpWt_BfAJ4MKLKg4fmS6_K6GwGAev79QmwlUhg9JYRJ-WC1xtpYgaV8gWKarZYfJ4IkQ9XkFSMDIaKKAYlyDSGlJ7cj_uSyEkcdCWqD1pdJpHaV2pcdcX3y9If6c2QFjWlWIWOxE6G4E_WDQDe48S55YZLQ7VZuwnMCr6CYwWOUFu0LnpUeSiWs5aA2M-N_7CXtwWMLJkXq40oQzXGd1citC6GkOy-g8ACS8VrL_etr2VnctgvEq7FmM_4kaV3-aAQP9HwUj-MypGQ7C1L3KS82eMlI1mxduRxwQjmONcU3L5dU8j61Yd8px1cM0JNh-0Zq-azPHizQSMejEvpiDj9xAla7d1uvpl9EX0I-lDLwSaOQioygOcnvxLTl9ZH1jd6kD264GQZ470ltoR3Wst960QDYi3-3_3vtv_Gq6l1Vst6WoOuiscaVDuaGWwWOA424vneJx4O52Q_skmzng_UVoASsJVmd2hsahvyvmaAdHH3puCWlomYmcTaef-3L3A-Xruzu_2xUeEgH6KflbuHHQj1j_rubNQCIDG8_ETu-39qB2PYIcYXTvutS_ORPwW4_HLr-ys_5lbWA-v4-JI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=BBs90d3eUUQWnMMeYpCH_9iGZM_9ONqZM7hekX70POYRlqRl6TvArFZaxwSdJ84DFk4ordPOEHiPpGrwXh6m3j2yEhyrggc1WwHePpsk35e2Ux7uZsJ2Tl7r9ydkdBYvEt4no1MVFkNqMQGapW6lmbZRMuqPr69dS2C9vzYMwar8Oxr84-kePDxvblDg4aWsAM9YlvMPXEmb_fg9FpousU301KmzOdd3IK25N-iLaU1bMlndnoHJhPSJWw3XwvhUvw46BLtjc72B11B4ONP86EAQMTgDIw7upQV-1hFklqkIMKdUwMndxSbfESQ5QtNoaJ4vUvEOVrVvkOjSZLrXRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=BBs90d3eUUQWnMMeYpCH_9iGZM_9ONqZM7hekX70POYRlqRl6TvArFZaxwSdJ84DFk4ordPOEHiPpGrwXh6m3j2yEhyrggc1WwHePpsk35e2Ux7uZsJ2Tl7r9ydkdBYvEt4no1MVFkNqMQGapW6lmbZRMuqPr69dS2C9vzYMwar8Oxr84-kePDxvblDg4aWsAM9YlvMPXEmb_fg9FpousU301KmzOdd3IK25N-iLaU1bMlndnoHJhPSJWw3XwvhUvw46BLtjc72B11B4ONP86EAQMTgDIw7upQV-1hFklqkIMKdUwMndxSbfESQ5QtNoaJ4vUvEOVrVvkOjSZLrXRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=VSkJfejyOrmCUzKGQmjgx2QjGU7XUirKnYSyDneI0jbBbmr7vC_OlSW7TOWORtVwwWZNYmD7hhtaHXuomq1jR5tRL76ScR3j-cjue8Ian71atUnjfVEHAUqwpYawYgbFnb6I1YdU6yymAmx81Vi9l6IXCjEK9T6XCEIOUjq2y4757-1NeekYYcKqUQCwEPR0ziCz0RBJH00fLRPP5vuwobJpQqRY6jUP_4U523fhO6a_OYF9IvbQTflvzZiW1xJu-JvaxYyh9J_tzQ9U6lRZAyWc8aM9UI3qpzuc7Y91E-uMlimk4j9OYyIn4VOdj88sPbjbqDZznJmwizvvUIAwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=VSkJfejyOrmCUzKGQmjgx2QjGU7XUirKnYSyDneI0jbBbmr7vC_OlSW7TOWORtVwwWZNYmD7hhtaHXuomq1jR5tRL76ScR3j-cjue8Ian71atUnjfVEHAUqwpYawYgbFnb6I1YdU6yymAmx81Vi9l6IXCjEK9T6XCEIOUjq2y4757-1NeekYYcKqUQCwEPR0ziCz0RBJH00fLRPP5vuwobJpQqRY6jUP_4U523fhO6a_OYF9IvbQTflvzZiW1xJu-JvaxYyh9J_tzQ9U6lRZAyWc8aM9UI3qpzuc7Y91E-uMlimk4j9OYyIn4VOdj88sPbjbqDZznJmwizvvUIAwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZAKlv7ZtJ-2zbKBpEDSYt4d4T1LoWCv4c9A1xx9duPh5puA9DX5mXBYK0AlOj0VUs9log_CWeJ5p1cUsKny-pBZNWn0Z06ZZz0Ig_1DXgPpU1jrhwSmsKSzlpfsxruv7LN7QehFaS5dPXiFo_1UlpWVltD8FzJpAFaT4tlo58yqy8bqzIR9dqWOVgC5WnIFqHhlhWDSrgReuuSYxFzr9unDuMt_JPEjZiHNFYS8GBJGeVh1hah1hoVds9QZpNG3n2BMBE-FmciUJV_bptkwC1CyTNEm8kvHLlAZgfH8eKVvvjkMNfCbaByY4xc_233MAF4HhhFV5oUzGGof3YNpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=POIT4UMR8_eIXza_qatHZI-7mGZgfGmVGJL6mulp03L4be82IOtayi-mEb6ck1ridAt_psPqhshuX0RUh35AvrQ2P_0fZ9h35HtsrOA7fdRRKHc28b89sOyWTTca6X8lQekaup-2wzNJE9z5SfCznao7V-zu0EKGk_6jHQEWd1iyc_dOekFCQj8Jb8CnKDNG9u97ESoDGxhBde5KWwsOzbXb6UY1OdmjPCErMLDnpUMR2Tkyz6WdAhK3Re_bRi3W-s0RSyzlLopEHd1XKZPP9wPxHxo-Kb-8UeCSo7Zjk9j45PbhRP5vkBMEDOSEsaNpvLLNNe-MKV8QtUwzokGqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=POIT4UMR8_eIXza_qatHZI-7mGZgfGmVGJL6mulp03L4be82IOtayi-mEb6ck1ridAt_psPqhshuX0RUh35AvrQ2P_0fZ9h35HtsrOA7fdRRKHc28b89sOyWTTca6X8lQekaup-2wzNJE9z5SfCznao7V-zu0EKGk_6jHQEWd1iyc_dOekFCQj8Jb8CnKDNG9u97ESoDGxhBde5KWwsOzbXb6UY1OdmjPCErMLDnpUMR2Tkyz6WdAhK3Re_bRi3W-s0RSyzlLopEHd1XKZPP9wPxHxo-Kb-8UeCSo7Zjk9j45PbhRP5vkBMEDOSEsaNpvLLNNe-MKV8QtUwzokGqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=HPxR3sr69sdcUIz7IhJTj5jVwSOlv_Wm02YuFxWXoAPdddh3sR-Udi0bvIjxfnp8SqVybE_ML7S8-zeOfOZFXnldiPzeTceuP0Srqsc3kJAmshn4nX4zAVMNN29xyStiICh4pihq702KYECIOop5mHgFkEJHihtCkIYsMgGMPurZdVUeOtBD_s0stfiQyKs60mN-72LP6bhixKQjS_Sb05pE2UstCeNjFTIHWUSpvZYXpJ0Uc7gl6rKOroTzKhBmXrMEnYRAgLECzHolPUixxdUEMjSLsFqLYKvqJQWTApayp9njy0b5-Ibnh-adySjZhoDGZ1Tc8DT0rak4dHeRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=HPxR3sr69sdcUIz7IhJTj5jVwSOlv_Wm02YuFxWXoAPdddh3sR-Udi0bvIjxfnp8SqVybE_ML7S8-zeOfOZFXnldiPzeTceuP0Srqsc3kJAmshn4nX4zAVMNN29xyStiICh4pihq702KYECIOop5mHgFkEJHihtCkIYsMgGMPurZdVUeOtBD_s0stfiQyKs60mN-72LP6bhixKQjS_Sb05pE2UstCeNjFTIHWUSpvZYXpJ0Uc7gl6rKOroTzKhBmXrMEnYRAgLECzHolPUixxdUEMjSLsFqLYKvqJQWTApayp9njy0b5-Ibnh-adySjZhoDGZ1Tc8DT0rak4dHeRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMxAaskVv5VfGFaqHeiARmm_8sFRmwoHz_gKXwVf-dAz_buEC6uZupIumva-WDC-ExJyZCjrXOOoXk-tXpbUhSOTiDNiHmsom5FyUClphyr-vRuJRH5Uo8KCCTGGejC_px99FHTkdVJ2CQpKX58s3xoFm_e09C0dtD1Pk3lFhxPdo0OWv02DlQ2E_s27mxraaZfR4eT5VKCQtSBIsVCl1fEByAZ4dyfAfplIoARAukNfdJdUWdGKvnJLyN2LAeWxT3t8AHwCsIYuL_eFqimOJZAXxSCcjqQlltZK-BChkv1ufhzXWsHD7fsBvkpHdoyksjGS8WBSXnFVmAhRurQEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=mhvHzsdabHJTYO_xJeL26DldQeJJb57jmRKg1j-AlMZS2Absj-giCNZiemcuNyQB6ErjQuIkVp3A3CzOJNbHLX6SgDAg9mDQ8T72-FpQ8fbapPwsoLX-TekzrtvZb5645SQuNsvOYC8OsRtPRwbXHmlfGdU9yF_cFkXF_faDBUv1nRita2XF5EW8_lbN0a2zz5O6KMUl0u_W8ZYjH-GiC0kD9Z55UUcAmGIQL3tY8cW5m3IFO3tOo3PO07kIB3IQzwpSxhkgh61hQi5X_wiHTlKdf5iohi4iQC5CpO07JFhOf_wDb-ixa9KAZdfpqHI-2uRSi-R198oh4VG-0Bdcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=mhvHzsdabHJTYO_xJeL26DldQeJJb57jmRKg1j-AlMZS2Absj-giCNZiemcuNyQB6ErjQuIkVp3A3CzOJNbHLX6SgDAg9mDQ8T72-FpQ8fbapPwsoLX-TekzrtvZb5645SQuNsvOYC8OsRtPRwbXHmlfGdU9yF_cFkXF_faDBUv1nRita2XF5EW8_lbN0a2zz5O6KMUl0u_W8ZYjH-GiC0kD9Z55UUcAmGIQL3tY8cW5m3IFO3tOo3PO07kIB3IQzwpSxhkgh61hQi5X_wiHTlKdf5iohi4iQC5CpO07JFhOf_wDb-ixa9KAZdfpqHI-2uRSi-R198oh4VG-0Bdcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=JGwuiCz9FXj8_j8y2RfFO24bUNOkkpP8vm4c0XQS9u-NtRWd47FAxB6VEEvl7YSsEUZlh2Xi-JeppViLZbzpYCeebacnDkXNhKlGnH3MwiEBAPilTSa8s9UkqNGN5HoAkcPm0_gWHq1XbboxfRfOBm-cZegSlsOh4E_3C-fV2ll2X_YNtZetUIvN6mr8LEpasmsp9cARtKqLOUTj6vyFDa3n6eS2GEpPnZvSK0ajkUo9-T_sdY2fPKcYiUFHJzye3IcVM2wH5GjUuw3a-xQD4pv0ycRQelfrSzPVNkbW-loc_-NGaoZmfhGQfh6m447FS1JEy1tyT71lgYxfFPN2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=JGwuiCz9FXj8_j8y2RfFO24bUNOkkpP8vm4c0XQS9u-NtRWd47FAxB6VEEvl7YSsEUZlh2Xi-JeppViLZbzpYCeebacnDkXNhKlGnH3MwiEBAPilTSa8s9UkqNGN5HoAkcPm0_gWHq1XbboxfRfOBm-cZegSlsOh4E_3C-fV2ll2X_YNtZetUIvN6mr8LEpasmsp9cARtKqLOUTj6vyFDa3n6eS2GEpPnZvSK0ajkUo9-T_sdY2fPKcYiUFHJzye3IcVM2wH5GjUuw3a-xQD4pv0ycRQelfrSzPVNkbW-loc_-NGaoZmfhGQfh6m447FS1JEy1tyT71lgYxfFPN2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=VGkh0KxDTvHEa_8xMqxnBL_0_t_o3oUhNIVgMq-SNQEquNLTrAIF-O8c1MvlhvvUOQsIg8n22DXW_UB8nqrgVoTgnQuisQ_pGdBYDDHysBQ_ddBoE2h3PK7Ebh-NDXsZS8N-n9Slsruo76yGMJbGi4vU9ckaZpLRrbl04UchNjMT9L-JpY11u4JXH7y8-G8rip3lJRD2an3Zhi_ubQbwSUB0O75wb-a2ldnaj4lM3vikFVS0FvIh5nq_QUTeRHYS9WJOTDpQ7Bf94He567Vf1gr3L8GUBzR2HTFKBvskweMnsw0RfNSs-vp0qIl4nzVAlVz9f_8I_GnY1TjoYgmIVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=VGkh0KxDTvHEa_8xMqxnBL_0_t_o3oUhNIVgMq-SNQEquNLTrAIF-O8c1MvlhvvUOQsIg8n22DXW_UB8nqrgVoTgnQuisQ_pGdBYDDHysBQ_ddBoE2h3PK7Ebh-NDXsZS8N-n9Slsruo76yGMJbGi4vU9ckaZpLRrbl04UchNjMT9L-JpY11u4JXH7y8-G8rip3lJRD2an3Zhi_ubQbwSUB0O75wb-a2ldnaj4lM3vikFVS0FvIh5nq_QUTeRHYS9WJOTDpQ7Bf94He567Vf1gr3L8GUBzR2HTFKBvskweMnsw0RfNSs-vp0qIl4nzVAlVz9f_8I_GnY1TjoYgmIVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=hSKS_i5jf5V_m4r_fwM_lL47Hh8zJYRrGIq56_38Jc3AKZRctZtXsgn_Eqnr6SHJs1ls_WZxWf3xopkQMeG-G_zEkES1PmjkbcvxOaKNEpBJOSVSfoQi7pY3OfsOBjsgf-pg2ZBhY1B40BepdtJLHLVvQ3H52Pk6_v2CQZTac5qfW5WPKK1f8nd-tSvIngfyRRTnsZptjBVTS47h84P1Fzym07nDslZEv46QN7fWRtE6hP4aVf9ylShJLA1LndAMC5QkHhsem9vFzN3C8oDy2RPh6kizf6yPHAmnoZy5yjsP9Wal5-E9-KhgKpcpAFwLcvLpKwexzaU9kCIFkIHolA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=hSKS_i5jf5V_m4r_fwM_lL47Hh8zJYRrGIq56_38Jc3AKZRctZtXsgn_Eqnr6SHJs1ls_WZxWf3xopkQMeG-G_zEkES1PmjkbcvxOaKNEpBJOSVSfoQi7pY3OfsOBjsgf-pg2ZBhY1B40BepdtJLHLVvQ3H52Pk6_v2CQZTac5qfW5WPKK1f8nd-tSvIngfyRRTnsZptjBVTS47h84P1Fzym07nDslZEv46QN7fWRtE6hP4aVf9ylShJLA1LndAMC5QkHhsem9vFzN3C8oDy2RPh6kizf6yPHAmnoZy5yjsP9Wal5-E9-KhgKpcpAFwLcvLpKwexzaU9kCIFkIHolA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=L9K0Hq69pDmwiIT6FS77kcJ4tAJ4QAXNXwgh7NcYuNbvuSBZAACM_4lsPxGZO9sOrgeX6ZRoXEqlDeOaq09iKTD1n3Mwl7A1TG_SVjpmmWPL94ih7Bw-TnD7q1eS9bSbkfKS8N-Yv_C8jONREYXSwPm2-Zn6wYINppWfWM9HIEWXqq3T6_qEmpTbxOT4oxFgeyKkLjHvlR9uJPIjyK_e-e5Rg-qyqyfR7TvVybyP6NF0zxWL58oUs0DKnNfXEK8QHjEIY_V4jJhX4OJb6xHk8DWlInDMNKg73BhrOVG_gKb_anv6er3xKa2-BRtUly_z-0qkW6M6cMj0hIWTLg3WWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxFUF2Oe8EHnI8vKtLvTf11rc0HKzYg2YfJTXBHa0zjx9QgW8PFITPBE9xLDtFv6WKFdl6ETRQfpkiIQfz3UsXxK1hqcEedcLdsAjLfBvhC_p3jB1mNY7UtMCmPTIWn29RZFQxPgj_k6__RzLhydUMkU1dM_st9M4XFET1fQTU9wgYnPbOl1XpIehIgCVsvLtBcGe6dQRtHpwrzHwLByzqHqL4cUfo0dGbJxMLpBHGgQb-fLP5ZxuCAgX6icvQS4aFZOhjforgRo_ExV1gWvk0Eklp2nIp06q4wFEKmfBo18aStspTYCtT0-CT7HV4J8gzUeb2HaMKs2wcpvO5Qing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
