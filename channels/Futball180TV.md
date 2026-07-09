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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 606K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-99206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=m2_x_l4mdatq49be17G0Ms6RAFmO2rIGW4Ay_15cCpmQUINt7LT7m3tWHsfCMPJS2LDYBbZim2erhAlSVaEMWSuN32g7vdPCZUgux_dOxug6K8F1OtCeav5bISRwDYjh1vgQ3U_lJCqRVKZMECnK7GCh_YIqv9BVj1FDYTnapCefww_V7iFGcTLyPpX8Bz2LymCYK5JmjgU_cj2Y04WdCfhRSIB8L0ZZPr5WKD_YjHnLj8q2EGU-ym6BP4AWYF0Dm4TG0MrEdSEuhlTtikm1iN-J3Mt_uHpug21gHsP80dTLNsrhnBvdT6UlpQnRa7gaPGuuuPD3R_inmlBm7Cgp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=m2_x_l4mdatq49be17G0Ms6RAFmO2rIGW4Ay_15cCpmQUINt7LT7m3tWHsfCMPJS2LDYBbZim2erhAlSVaEMWSuN32g7vdPCZUgux_dOxug6K8F1OtCeav5bISRwDYjh1vgQ3U_lJCqRVKZMECnK7GCh_YIqv9BVj1FDYTnapCefww_V7iFGcTLyPpX8Bz2LymCYK5JmjgU_cj2Y04WdCfhRSIB8L0ZZPr5WKD_YjHnLj8q2EGU-ym6BP4AWYF0Dm4TG0MrEdSEuhlTtikm1iN-J3Mt_uHpug21gHsP80dTLNsrhnBvdT6UlpQnRa7gaPGuuuPD3R_inmlBm7Cgp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
تعطیلات دروازه‌بان کیپ‌ورد در کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/99206" target="_blank">📅 18:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=OvDM7nhdiWtXJi5WL5XI8YZv8x1PinmCwE4VLHspo1MPc4dVqMNw6aHiUy-yNmxl9gv73u6846lrmoHpOafjSwMzIx90OXgROOuid3JOY1CM6CaJ4mVd3TL9ow8KWWVPPV3MK5svo5GnQpGfdbwN4vBkbveCa6S4CBwkhsG1vGlpXMcvNsNzAYF_dp9M0cZlyPKvvfCgDmoa41ign_3hE8R_QqXOLPX4_T7F2vO35tVp1ncN92mofco38PhooT4HKcU8y3f2xGNF38X2MLkhlIBEZKFBw2vD7FbFnFxPk2i4S_G5rLRN6z20PSg9WWV3x326A1VVOn_JhHB9mVGmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=OvDM7nhdiWtXJi5WL5XI8YZv8x1PinmCwE4VLHspo1MPc4dVqMNw6aHiUy-yNmxl9gv73u6846lrmoHpOafjSwMzIx90OXgROOuid3JOY1CM6CaJ4mVd3TL9ow8KWWVPPV3MK5svo5GnQpGfdbwN4vBkbveCa6S4CBwkhsG1vGlpXMcvNsNzAYF_dp9M0cZlyPKvvfCgDmoa41ign_3hE8R_QqXOLPX4_T7F2vO35tVp1ncN92mofco38PhooT4HKcU8y3f2xGNF38X2MLkhlIBEZKFBw2vD7FbFnFxPk2i4S_G5rLRN6z20PSg9WWV3x326A1VVOn_JhHB9mVGmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر آرسن ونگر در خصوص حضور کلوپ روی نیمکت مانشافت
: کسی شکی در مورد کیفیت کلوپ ندارد. اما همانطور که بازیکنان خوب مربی بزرگ لازم دارند، مربی بزرگ هم به بازیکنان خوب نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/99205" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=bEVKDZjEgDAhNXIxv-VDvCjuwgJ7ccAJjGtaqWDD4IxNZofvdkglTYJb7CQqqOwNnVY23BHDgqbARpX82MWucm1RT6Xk-qjZwFY5Cin7_W9XJXeAHNw1X5-oUoRZ1yQBI23K3pvoWfSsinjmQaXEMRSpzqR-vfKVdCSYhFEuauI01HNKvI14a4xnqgdcdFbYaDyFcKJm_K8mqs17oQmxyjEafNk1eXoQ4Cd_HUKIOrcY_5ISodxOLy2w40mvKcV_l1J_owR8K5iL8890m10Wl8itE_ZqgtVCCuxS33GyyNUTXup0gPhUf54WyhbRiOqK0k3FUXt8MJb4kYgeeGp00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=bEVKDZjEgDAhNXIxv-VDvCjuwgJ7ccAJjGtaqWDD4IxNZofvdkglTYJb7CQqqOwNnVY23BHDgqbARpX82MWucm1RT6Xk-qjZwFY5Cin7_W9XJXeAHNw1X5-oUoRZ1yQBI23K3pvoWfSsinjmQaXEMRSpzqR-vfKVdCSYhFEuauI01HNKvI14a4xnqgdcdFbYaDyFcKJm_K8mqs17oQmxyjEafNk1eXoQ4Cd_HUKIOrcY_5ISodxOLy2w40mvKcV_l1J_owR8K5iL8890m10Wl8itE_ZqgtVCCuxS33GyyNUTXup0gPhUf54WyhbRiOqK0k3FUXt8MJb4kYgeeGp00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
نظر جالب مرتضی تبریزی بازیکن سابق استقلال و تیم ملی در مورد اشکان دژاگه و مواد مخدر جدیدی که فوتبالیست های دنیا به راحتی از آن  استفاده می‌کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/99204" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=Y56DnCJkYEshQjJdZ5L6hpI0pxBnJsahFKMC5cfPQWslg5r5qbyHB_iocszUC8xlzBtKYddx5_1OF9VFEUjUPLRXJgjFiEKK9i2JVrP-OwjyUwtYQSQpH5A_5WItrgAUYlz3B3PfPUdO_cscNTK0GY9eE6-dCjZHGMYed7SqsK-a5oAx9OWbADiZybp6RTUi3jJIw2qZ5ZMUCE-zvRQ7MiZdoPN0kVu-Ml7cpqIRqUlhcwCvA8D3OYM8xQ_u9O6a3snIiIJ-O42tZTgFMdZbpR_oW_j-GiOmqj0Wld7wylRVpalFe4ArZ049KzS_2c57dC4_yyuRYuV0LW3WJtq56DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=Y56DnCJkYEshQjJdZ5L6hpI0pxBnJsahFKMC5cfPQWslg5r5qbyHB_iocszUC8xlzBtKYddx5_1OF9VFEUjUPLRXJgjFiEKK9i2JVrP-OwjyUwtYQSQpH5A_5WItrgAUYlz3B3PfPUdO_cscNTK0GY9eE6-dCjZHGMYed7SqsK-a5oAx9OWbADiZybp6RTUi3jJIw2qZ5ZMUCE-zvRQ7MiZdoPN0kVu-Ml7cpqIRqUlhcwCvA8D3OYM8xQ_u9O6a3snIiIJ-O42tZTgFMdZbpR_oW_j-GiOmqj0Wld7wylRVpalFe4ArZ049KzS_2c57dC4_yyuRYuV0LW3WJtq56DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🇳🇱
به مناسبت بازی مرحله ¼نهایی آرژانتین مروری داشته باشیم بر بازی پرحاشیه دوره قبل این کشور در همین مرحله مقابل هلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/99203" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1F99m_1mSjmR1u4AczX0UvTeS4Ndb5Q5LYhoTE6SV0ydeczH_UwsV0EU_WKMJUEJi7-ymrSYoGnfs-DUNkAwDYOfInnpkFljBIZoyKmkbki96l0Bm8WXSz5nHT1ystalrIlqS_y5-n33y8g-eAiKpf1BbquU2-atXrf9yXUknoB9ecIphaG3CnPksFuygIuNZmnyhxbREYlW-8ExBWtW-_CHZg7_6c_LE6pBrLLQX9BJIuuz_XtdJL8bTf_l3Y_fPd9S87fXxMAAFSzQJHhECFabFIgsAJZxJfPgjKDxMRhJ9Om4COqOs6aIS5LEZDfQytrdTAa3LjrVWi9I4kMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsi3evXSD2qiN3vtZ5lYwNcTC4zo6QereFC8_GhyR4ovBA6VM6vbVEKs5S4MhdRKzR09QdUIImAblo9aomQuEeNe4AD4I5AuBptxwgr9gNHvfVUvrL72MEEmENeGzWZjWzkdIZQ4HMuLM3jm0JYe0g-KiOHVpZOlzp3nYQpAzxAedJSGgeYys7sP_4V0GvUvRnQzgmq91hpdAlC3X6Pb3zHLloK0GuPAnKT5ZOc8IFdpbLRDmlhpLoBRsmT0xwePnuztI8uZ08lrxqFmUEXMVrL6toRW8gikybrLNMEsxY3lX_vG8DZKhbT09m0zcoQaesgpwpK1sqSo4SduXa50CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
ژابی آلونسو در جلسه عکاسی به عنوان مربی تیم چلسی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/99201" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039d015f28.mp4?token=NWOLFQsdMP8TbsmDugLBJDreQMibc3qDjaJ5SuOymE6vstnr78M7qL2weVROy7wJsjWUwxiMTIYolnQJrp38RHugod3cASWJlevlHAu_UaliSpMwpjWkYsWI5wlJaQE5pWcpJ_JKzwc_Z65VUmXPn-cKULK9nx9hwOqwZEodZj0hoWsOmm9J7RwJ2E9Da8g03YKe2R4dV8-5NlzRbx6bd5_WcEyDjEPSBn8DAQfjJeebkrejXJP_ypxkldW1fqzQhKSEkBGwjb1MDmhp8T9449-v4KTt9HyHogcoAE6TGCkrSqcig5hAjLAeiRGnpTpJdLhhFHUncMMrcHAFd_8vhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039d015f28.mp4?token=NWOLFQsdMP8TbsmDugLBJDreQMibc3qDjaJ5SuOymE6vstnr78M7qL2weVROy7wJsjWUwxiMTIYolnQJrp38RHugod3cASWJlevlHAu_UaliSpMwpjWkYsWI5wlJaQE5pWcpJ_JKzwc_Z65VUmXPn-cKULK9nx9hwOqwZEodZj0hoWsOmm9J7RwJ2E9Da8g03YKe2R4dV8-5NlzRbx6bd5_WcEyDjEPSBn8DAQfjJeebkrejXJP_ypxkldW1fqzQhKSEkBGwjb1MDmhp8T9449-v4KTt9HyHogcoAE6TGCkrSqcig5hAjLAeiRGnpTpJdLhhFHUncMMrcHAFd_8vhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
رونمایی از ارلینگ‌هالند در آستانه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99200" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPnBEjnCZu9yhMaW9yx66hyFuo46rMs6iO4_7QBsmDuu_4DZvpIYsT0x6RgwVY8UdlG_mEzdRUC-X9bopluJ08mUQWv5wfOsZX6jrubaeGlZcLjYmYF-YF5XiWVW5WKNFpW5b3oyE_Qzc8GVwnuwjfZ8HBFSTem30YmLlCuWVp-SpdD-wPPmxKsi9SRc6-fUEClq_e6irbiNwSt82F_I6YLktGv376IDRiB7KeXAZnFOikJHhTA3rmeiE4QVLZzpAYEUGhLMK5rJ2FUP4rcOvkk5Xpod5elNi86mE36KvKThTxqcvJrarTVyJVx8sRlnk9q85m6xHZ7OH1cNTPE20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
باشگاه گالاتاسرای ترکیه درحال آماده سازی پیشنهادی برای جذب ماستانتانو هافبک آرژانتینی و جوان رئال‌مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99199" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=P9PMzFyF7iltMANuTgOCgBiXIRSDKoxRD2RmlZucsYbvdMRMPud4n4K_v0JhQUYauXh4j2qco94m08UtFqdCc3fYqX2HGM0T53grSFJnF9mUCdBeltrYBMcka6sTk_IoTmBOQUpFh292yhU_C0dg6o5I5Mxe1JO7IlhfGZJuRLlNhpa54SjVlqoOdc4O5hig1yacfJDtrOOZNJ77U2Q46KnlDY5iLcrugDQulpoiOvdafo7-pf1sOF2qDvsUQD7ZrCOqaVtFrMWTnV5oqyufMndo6jUkDlgx-1yv1gDwIl2QklOPbis1vTVenIuWurektLoCidqumieItLCpPAitMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=P9PMzFyF7iltMANuTgOCgBiXIRSDKoxRD2RmlZucsYbvdMRMPud4n4K_v0JhQUYauXh4j2qco94m08UtFqdCc3fYqX2HGM0T53grSFJnF9mUCdBeltrYBMcka6sTk_IoTmBOQUpFh292yhU_C0dg6o5I5Mxe1JO7IlhfGZJuRLlNhpa54SjVlqoOdc4O5hig1yacfJDtrOOZNJ77U2Q46KnlDY5iLcrugDQulpoiOvdafo7-pf1sOF2qDvsUQD7ZrCOqaVtFrMWTnV5oqyufMndo6jUkDlgx-1yv1gDwIl2QklOPbis1vTVenIuWurektLoCidqumieItLCpPAitMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
👀
دوربین اختصاصی لیونل‌مسی در صحنه گل‌ سوم آرژانتین به تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99198" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0PHqVshh49__6HuPmd3iUIXSVSgzwhOqHrqdxxzLsD69dGv7q-Tv8exjx7SjuMoayZbKiUECIdwD22ZCTWPt77HXjbICLXzczCpQRpOqdskTHh-yd1C0RoqSRw6NaTVyXo6y9PIlSIkJladfhM6BEu_hljJQdZ5SLWjoifyEQyjPoo0Ue2EO52P5KUrPh_Nf7fIo0bGVZnkGlvzOD9J8iB9FlT2v2u0QtutD_OkOOktjL4Tst69E5SjtAS-DmHqPCltSG7sk0KtPeZEVXjRYJuKNXCXHt88ivhjfeVoQGbVgDd604NizCfsL0Jej8wqzit4siI1ED2V-SzgSvW4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کوبارسی رکورد جوان ترین مدافع که به 5 کلین شیت پیاپی تو جام جهانی رسیده رو شکوند، این رکورد دست مالدینی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/99197" target="_blank">📅 16:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVwh1aT5zYRv_B4OfIarOGyLn2e7TXs5u3_wjpHmRVwuTvEzlDADhVFB2d3KDoREUVFM3ftfLJVQqqrOXmPRXEhBzwzJxGmby8jv7aoIIxOu7a7xet3HaO5C1KjMb_FOOjUeNqEtQp4w9njiFWQWq-kmIOLMwSV6kO444NmwAI3de1M7ZeIIq8xKTIka6V00sOymSL8OdbswVcy7HET09w8AYiJcuVKh3ST-McYoYzTVRm8kCl53vFL8zrNMzryiZHK2Bl01luHBVbml-R7u2C8fmaLd4LX_D8Wpz3R8kK7xbPb5TbWjgZQ7roImFRoDs1HNJoEc1SPfF4Ecw95oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99196" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=RiEi8brA-McOgyT2-9akZK5Lxzym3OVriZtmxkHxynvpsffBiqPsoHJ3_WRGWS9xWepXDqPFhux0meuhkfCycTX7wEbwS4Ld3Hi9iWPetTrDoyB7MAbwFsgl5dmZBXd--Nbsw2gZhkvpLAWtGaNhQJJbBJlLbMSY5-kGzg8WHkCIDkyk-qsW54iIarXerSAHBj2Ou3CHyyOEw_uYtE2VUDoRmAZG4QnIjT-8Q3YdDhQ0btao8VmAqKpAXdgNwRHmbcfauAJXOpg8pRmri6oKaA23otPlSVdsnyfefucU23TKbsHcQIKwwJ1afcgY8sKnK1p5I-zatp9AnNhD9-JbRLuWSklHaHeeHcYZJsttzDcAky2RG2snTv4t5CGQ8OsJ38cewyD8fbUO-a3tO4bMykFBhmGay5P9L8QPCdC2izDJoSBOJLiKGPsBduog40xow1T1gJ93x0-kv06o1unQCaoTrXJUTTiF5yQtRyPYbEOznyi1eajAn3oFJH9cyc2JIg7Ud0FCobsJXOssYk4UlT22BWq-gTXZ6ebSGAe6RoYTjhQZcZ3cAFMs2OZPknrjfzIGRatjtay7o-J6zGZFUMLR3uw-EqoF59OB-zFo25mZy0QM46Jo0RpWjF4-hvHI_IMCoaAjlKGo96qSkAICUWaxTJvZ5mcecuchhlt14kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=RiEi8brA-McOgyT2-9akZK5Lxzym3OVriZtmxkHxynvpsffBiqPsoHJ3_WRGWS9xWepXDqPFhux0meuhkfCycTX7wEbwS4Ld3Hi9iWPetTrDoyB7MAbwFsgl5dmZBXd--Nbsw2gZhkvpLAWtGaNhQJJbBJlLbMSY5-kGzg8WHkCIDkyk-qsW54iIarXerSAHBj2Ou3CHyyOEw_uYtE2VUDoRmAZG4QnIjT-8Q3YdDhQ0btao8VmAqKpAXdgNwRHmbcfauAJXOpg8pRmri6oKaA23otPlSVdsnyfefucU23TKbsHcQIKwwJ1afcgY8sKnK1p5I-zatp9AnNhD9-JbRLuWSklHaHeeHcYZJsttzDcAky2RG2snTv4t5CGQ8OsJ38cewyD8fbUO-a3tO4bMykFBhmGay5P9L8QPCdC2izDJoSBOJLiKGPsBduog40xow1T1gJ93x0-kv06o1unQCaoTrXJUTTiF5yQtRyPYbEOznyi1eajAn3oFJH9cyc2JIg7Ud0FCobsJXOssYk4UlT22BWq-gTXZ6ebSGAe6RoYTjhQZcZ3cAFMs2OZPknrjfzIGRatjtay7o-J6zGZFUMLR3uw-EqoF59OB-zFo25mZy0QM46Jo0RpWjF4-hvHI_IMCoaAjlKGo96qSkAICUWaxTJvZ5mcecuchhlt14kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇩🇪
فینال جام‌جهانی ۱۹۹۰ میان آرژانتین و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99195" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99194" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99193">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99193" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e630de904.mp4?token=UJBNX6z-nXGB6ntldIbJ1JIVszJS0sMFUcosWLkQjfrsrd0A9IEbFKwi0WcL3y18E6hvKrEc2wCgOgKuLxqA3baARSRBxhBU_EB4t8_Jb9o_LGEBaIr-Luj2FDrODVKtf1he3vqT3u4pTXb6HoCoQkYoGKzXoFQ9VPZG8fOJUWIkBUoBQdbEAGVn0rluOY-zf_DnYLlEba-FJQwzQs25Jj66tZuXdjTzBqjTqCvtNRPCFOrNPxr1GGjC1qG3w4u0j9IYj8BMM5aOQc_htZqtFjp4EY1n4o8-oxUMIWE1nFw8bMb8CUzNqVKk9ulpsAmoy4HbpZavpembp814zgFJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e630de904.mp4?token=UJBNX6z-nXGB6ntldIbJ1JIVszJS0sMFUcosWLkQjfrsrd0A9IEbFKwi0WcL3y18E6hvKrEc2wCgOgKuLxqA3baARSRBxhBU_EB4t8_Jb9o_LGEBaIr-Luj2FDrODVKtf1he3vqT3u4pTXb6HoCoQkYoGKzXoFQ9VPZG8fOJUWIkBUoBQdbEAGVn0rluOY-zf_DnYLlEba-FJQwzQs25Jj66tZuXdjTzBqjTqCvtNRPCFOrNPxr1GGjC1qG3w4u0j9IYj8BMM5aOQc_htZqtFjp4EY1n4o8-oxUMIWE1nFw8bMb8CUzNqVKk9ulpsAmoy4HbpZavpembp814zgFJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام یامال به رونالدو در تاریخ ثبت خواهد شد.
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99192" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fb637797.mp4?token=tQ5tllmziT-w52PoZdGNmlpWE7toYK7zf8jUZDWgdMqs4nHHxcFxguPmbazhYElElZbU92jfD_xWQnehP9axdyHztryrATxqVLP4mrupU7lVur4r1kU9bpc0ikCMriqiA3HISsg7lX33b2wWPmhG2Et2YXoEwbgsT3x2vhOM_tNk2DMXgbtrGnImazmjcF0RvbAk1rcPqZP-2KkpPY85WO_Z2BiI0drBMJxpn0dBIfhgWSwiryMHY8Hfl_90F8hrZClJygoUCVIKrahNqZWZCmlsodY6apa5lkHBzJcOsBvtF6PWGfv_2utLOdWGjUF0bXWRYAFPsZYQKvgqF4nMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fb637797.mp4?token=tQ5tllmziT-w52PoZdGNmlpWE7toYK7zf8jUZDWgdMqs4nHHxcFxguPmbazhYElElZbU92jfD_xWQnehP9axdyHztryrATxqVLP4mrupU7lVur4r1kU9bpc0ikCMriqiA3HISsg7lX33b2wWPmhG2Et2YXoEwbgsT3x2vhOM_tNk2DMXgbtrGnImazmjcF0RvbAk1rcPqZP-2KkpPY85WO_Z2BiI0drBMJxpn0dBIfhgWSwiryMHY8Hfl_90F8hrZClJygoUCVIKrahNqZWZCmlsodY6apa5lkHBzJcOsBvtF6PWGfv_2utLOdWGjUF0bXWRYAFPsZYQKvgqF4nMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
🏆
دو قهرمان، دو قاب، با هم و تنها
🇦🇷
🇵🇹
تنهایی کریس رونالدو بعد از حذف پرتغال و مقایسه آن با تیمی پشت مسی، بعد از صعود آرژانتین
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99191" target="_blank">📅 15:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKmHqRUNl4qoQ-11j_69e_jPLKHDS-pwtrH_eO9FH1P2wkIs5a_mOR1iK9tJ9yy6Dl_lpidq-ehm4cViU4z0lxjWrhFFTrB_VTmLt9v2WFaM_fSvqArLpNcjlzjcPmPMxpQJG1xi72Y5BGNLBp5gpufZNKgStiHKDvnWZp0jUgmhBAmW4GK1ZXbU5UQAV0apvAHgxgdt7C4poBv632y0Cwjgyb6jIxD_Xr5Rx9wqQLdMVXIX4kdBAwQhsUQELJVfKno_5w8p_4w_EL3O562oHlA-aI11rAGIUB3yAE1KcYZb5H5yccF7kfiH7ivFUk9GqimzC-TjqWQY1e2EjEH98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99190" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
از کودکی تا تاریخ‌سازی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99189" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
حرف‌های ژوله راجب فوتبال که محمدبحرانی از یه زاویه دیگه برامون تعریف میکنه. جالبه ببینین حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99188" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkChTrs5DheEOn_KcE-7YPTW3o50Fwe8tfnlQwT1FedtzA6GwFoTPxtFtrprtFXi_ckqz_b8vEspPN_wO_6SgVa3M8hKxmazalfCFaBhf0335Ei2xzpJ48MecNv18JphKWgJ1TFKcqx6D9LI9E9FDrnJb6TndM0Ys7L-gAJA8lsnB53CKwOpsZp9ScASohB4iyqdLqoAw2k4UoR4y-8wsfqt5cR2k2aTvyHRKKanskh6L94uRqxh6MseVLDLZ8Se3yU8T1ivHw0MhQTVGIRoZlevn4VgDKA_fonyWczitNCmDKnM5GoMCCqncZgkmDN4qDxAlRtA0jEMaXBAJzemkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkBtFk_ceNmQcN-Gr8vRLpWleEpsg7yRb7SDHD1R5mmTOatXBOyeMuC3nQUGDZRmELg1AQL71d1vJGI4TYCt4Cuw_fM05svvvsp9ALDsUtuwgqYZrcWooCTerjbLcNlhFv_D6WEq5EdlHkOGVqR7ttEsfRsI3uJAFDL-dy9LnIpYB82-ekKPPGVtCPJ-veKYU0aV7Ogo4LJ7mb5XatM5LTryapGRzL_KC-m9vMkV5DGVdPjn4wmgMUcBAjw5lpWCEtMk6_wumvNusmq7RAZhZNuDGYU5F-upFYhf5qek3ATf6QuuxsQSFVZJJ5THwzE8dZgDkadAMT9dqGnA33I11w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت اسکله بنود شهرستان عسلویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99186" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
گزارش ها مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99185" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
فوری؛ از اکثر شهرهای ایران به سمت پایگاه های آمریکایی موشک شلیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99184" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=lSzTT1JN6iJe6Z1MdgSSZCT_5v9E5-liASHJBqz3-OissLeNNxtS2MMPpUcxowRnyNg9V6yoSp4pJpyiiN1uM1C5EYeWJhcoOQmQR4nYmDuH_udm_7ju2kUu9AXGXL9Cq5Guuhhxtjwg3Pyc51ae43Vx_XFjTLeMjQV8usqhume6MrojjEgs8-xXK74aWIKr7Q58vdDqn-l0uRe5EpyGuH0bATMCY2f-xu4OnheIRYP70_T2UsCogG7dnmF37l9XcYXF_HWO5L6keDFtaLtYSwTRETewSO0qX-VqN_S2Y_I2nLe-qht9Xwe3gO44bXn1GtKD9fa1-Ntd8x2d3j_-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=lSzTT1JN6iJe6Z1MdgSSZCT_5v9E5-liASHJBqz3-OissLeNNxtS2MMPpUcxowRnyNg9V6yoSp4pJpyiiN1uM1C5EYeWJhcoOQmQR4nYmDuH_udm_7ju2kUu9AXGXL9Cq5Guuhhxtjwg3Pyc51ae43Vx_XFjTLeMjQV8usqhume6MrojjEgs8-xXK74aWIKr7Q58vdDqn-l0uRe5EpyGuH0bATMCY2f-xu4OnheIRYP70_T2UsCogG7dnmF37l9XcYXF_HWO5L6keDFtaLtYSwTRETewSO0qX-VqN_S2Y_I2nLe-qht9Xwe3gO44bXn1GtKD9fa1-Ntd8x2d3j_-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
‼️
نمایی از سرمربی پرحاشیه مصری در هنگام اعلام مردود شدن گل تیمش مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99183" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeXEPGuSWm1htsKRnV0d4txYhJAMavF_YkLYz8eY4W4CQZ7vHYAv_LZV9BRfJwfCqaRS-FPjwfFr7sxZfdSzg6OiSm2X9yUTDPK4ERRf8ZTSYocBYC8048xi5zjjPhVtHo6D3bLxJa753j7XCC7VAteGa_UVEBWVHgkIFaqncKX7h6J89T19_UXsXKMQQyDY0zyCtRsNgRJVddWXyQMj3zt0RrQnVPVMhs46p1eXVaR7I8RATXR9J2aIwN2xpBtmC1x_qkTDoE1p_tlGCg7RT-GKjDShTY1lE57eU4JUQrK0M45gWLXdmz8L8amC4xo69dzef5z3XTOmLk2WoQpfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه امضای قرارداد ژابی‌آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99182" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ یک مجموعه صنعتی در کشور اردن مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99181" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
از منابع خبری عراق: چند قایق و ناو جنگی آمریکا مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99180" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ گزارشات از شلیک موشک‌های کروز به سمت بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99179" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99178" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=ayVu0wYhrWTrnZLESAsriBbG5YkuJ1vQAiIbZ-ZmdjMWc_zcFBipq5RbQ_SGzFjsnMYablAU3fmodN0b_jq__Vr9WNZXcExCnB7k_ZMVC645HyLGC9-f-0Y6hhTGPXe23LlvzhEqkt9e8XpsEBU2uXUdoIH5V1vmM-8CoF8EGY3KuVOOhTOM9bN-OR7GacQpxzM8DcO8lFeo-4FbfAMqi6zR15rvbMR2jhZT9Tmo324gxD3pHbmIqlG2pX_qAETP2IpOz3rn14QbVAbyMZYLnBI5mW5nnHr1nrCoqbXkyqx4xhwcb0A_vAPV9FOX1ECEcxBchfAYSYwgyljuPvO17w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=ayVu0wYhrWTrnZLESAsriBbG5YkuJ1vQAiIbZ-ZmdjMWc_zcFBipq5RbQ_SGzFjsnMYablAU3fmodN0b_jq__Vr9WNZXcExCnB7k_ZMVC645HyLGC9-f-0Y6hhTGPXe23LlvzhEqkt9e8XpsEBU2uXUdoIH5V1vmM-8CoF8EGY3KuVOOhTOM9bN-OR7GacQpxzM8DcO8lFeo-4FbfAMqi6zR15rvbMR2jhZT9Tmo324gxD3pHbmIqlG2pX_qAETP2IpOz3rn14QbVAbyMZYLnBI5mW5nnHr1nrCoqbXkyqx4xhwcb0A_vAPV9FOX1ECEcxBchfAYSYwgyljuPvO17w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری
؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99177" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
❌
🇮🇷
گزارش‌هایی از شلیک موشک سپاه از نواحی مرکزی ایران به سمت کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99176" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اخبار غیررسمی از شنیده شدن صدای انفجار در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99175" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPcXjhE1jt5khrEyKEflcobSBKcBFTk6KuTrxHCFKDkNxgZPG6n2-JPKQsc51TIHK-7leeTWKVm5Xjl6luMTD1R93lbdAOAS19yMNp0AwRyntNKlkmrB0OHYwUnEyhSw68abVqk_e0zhELbpd6aT7OzY0-fnN6MwY2KszHFmANvS5OK_DyJYUfa5capHpibha-a4wC3zTkQfWqv4La7FKrS6sKLZNcVNIs_2p-Ut-7iKBDMoA12h72s7PDJuc_-WbyYz9L8fqgrHTAV4a3XQNhZLID1MuuZc25Bv3lKBExLupuNjLs3-uT4f3oFWXZFykcY6Smhk8Tbua5XKIe5aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فلوریان پلتنبرگ:
نیوکاسل با فرایبورگ به توافق کامل رسید تا یوهان مانزامبی را با 60 میلیون یورو جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99174" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99173" target="_blank">📅 13:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LQxt8phLwA-U64p0ZB7BYMO94osCaSY-6SeGqnnMOozTiCCuSRiYscLUn-Kv1nZIh95EIH83G5U4R23gxWz7FFBO9HTuuFaQc2LWwNM8W2CmDH3p7edl7fgrQ_MPJ8THgDzPe3ZT1erRRb2yEIr9bFP_SzKjE8517kuI9NROpJH3fo8oAe0mE36MW5V7Jn3MtTgwJNC5RcJzno3TJK9480GnNh6RMNVcZQtU6xER8PrqupS13p_WY37Rj2omVyaCjJ86UgqrdoOy-si0ecX58SWtj3OTdwxka9OuObAhulJ_JSXjlpTVQzfIPFgvyxtuK-ecpFdC8UPRi0_JE1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بهترین ترکیب فعلی جام‌جهانی فوتبال تا پایان مرحله ⅛نهایی با حضور علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99172" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99171" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=f0kT0SZpfcu7LHN1afpiGUNYQmiSv_IzDcKV7fGDsKLmRIa7TxmNyF-F34vs8G21AyZMBc1zysFTjmfHkAIn9h7mfBPTzubphiurg3DRqI_20Snyzu9aavwXi7fgt8ZrJaQAP_Mi7AtzArNMNunuAuNRXhG0dXDq-6AW3lGJEh3ILuw_sQdmCCN-ObSZL8oaozVIBojMQBm5GaRONvInhFz5hiLmwAG_JbF2GkkOA7SO80Bvjzj0wZh26xzu-p_kh2TqSSWdstYruQmRK1kRrMvvHYKuIgsJhxY7ZmHRKuoeRzPUq69n3JOC8-SV9ba00IxmY9xSP7D7YhW-wjL4BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=f0kT0SZpfcu7LHN1afpiGUNYQmiSv_IzDcKV7fGDsKLmRIa7TxmNyF-F34vs8G21AyZMBc1zysFTjmfHkAIn9h7mfBPTzubphiurg3DRqI_20Snyzu9aavwXi7fgt8ZrJaQAP_Mi7AtzArNMNunuAuNRXhG0dXDq-6AW3lGJEh3ILuw_sQdmCCN-ObSZL8oaozVIBojMQBm5GaRONvInhFz5hiLmwAG_JbF2GkkOA7SO80Bvjzj0wZh26xzu-p_kh2TqSSWdstYruQmRK1kRrMvvHYKuIgsJhxY7ZmHRKuoeRzPUq69n3JOC8-SV9ba00IxmY9xSP7D7YhW-wjL4BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👀
هواداران اسپانیا در آستانه بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99170" target="_blank">📅 13:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=ZZtBcCbIEcigoF3nnmuU2Si4k0b0VdO0_4N9B_Yzhp_4Sbl8VYxlMYUJ5W3XyT6NWTmt5-SJnYyD7a0qo91_xgW9xq5piVl1NYYMCwua6gIlqxBY2IuksXfvMb5XvRVjdoX8-MTlI8gRIgC24W8Mbbgnvk9WiMnrdylkREqJVn1FUjCSYL_bNxqoBlGH-1nrDTnQiMll5fVCHdb_-EYy_yRc2A155O1E7GmpCmS5DCgoLOvS-TtIJBhjP_ppK8hfU2dizeTPjWdkpH-aXA119P0bTlZv46cH58Ezo9XjnQ2z_Eowu2Zt3ELQ1q0Eg7B2sKUD_owPFRie-XcrTr2Ziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=ZZtBcCbIEcigoF3nnmuU2Si4k0b0VdO0_4N9B_Yzhp_4Sbl8VYxlMYUJ5W3XyT6NWTmt5-SJnYyD7a0qo91_xgW9xq5piVl1NYYMCwua6gIlqxBY2IuksXfvMb5XvRVjdoX8-MTlI8gRIgC24W8Mbbgnvk9WiMnrdylkREqJVn1FUjCSYL_bNxqoBlGH-1nrDTnQiMll5fVCHdb_-EYy_yRc2A155O1E7GmpCmS5DCgoLOvS-TtIJBhjP_ppK8hfU2dizeTPjWdkpH-aXA119P0bTlZv46cH58Ezo9XjnQ2z_Eowu2Zt3ELQ1q0Eg7B2sKUD_owPFRie-XcrTr2Ziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه‌ورود ژابی‌آلونسو به لندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99169" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1WVQk8q36jYhvoG_wLKtGzsPhDF63zL6cJKptEKNAwn2Wzrxv8SzSGXWpnDsMHUoz8J4vvu02hEE6GRBbs6bK51LJmMHhWxbY30zLkICfbOGcELJwF9mGfiozBfi1XiqBrhaonK5feSN4JZoxd7Z0QsbNEPSb98MWGWASmAbztUDq-RibltE5s_RAgEGJmiA7gkbavOu3FmJY0zmEkysp0PuGn79OJnx1jLjH1CljR-Y1L7ULp0QZn5eZ5xM_5sVhZVVOUXOC-4T4cqcVzYX-21zqlIwDFdjgb7n0iOeXNy8_Mbd2sGIk-EqOBEqY8CGn8uHMroAlIWFZ8Wt7zTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
🏆
کولینا رئیس کمیته داوران فیفا خطاب به اعضای تیم‌ملی مصر: پذیرش شکست از اصول اخلاق در ورزش است و هیچکس نباید داوران را مقصر باخت خود نشان دهد.‌ تیم داوری بازی آرژانتین و مصر کاملا عالی قضاوت کردند و از آنها سپاسگزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99168" target="_blank">📅 13:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99167">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99167" target="_blank">📅 13:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAxzkP2MbsXUM7neMDZH0kpG3E87TdDmdBaixAzVTiQ8bE19TVz8dUqKy7wt-Mz0NDei0c9Ab_ALqOmX1JSrOaHLIng03OYt1RxkXFaykGH0aNfcOUJeDvazQuw_ECq0-ZU5mYWQApDiuyC_k9bR_N9gs16baGryf_VIl_n98KpNuwtlf7MXTaltvqbp95eC7HRVl_4UKFwqKCdgndznL2GXOVe8UQ5iQYoKW4C-8H4QJS8VvQAD1EKNrBJAGq-ldDywNYgaP48AN9dc0u4xgUcVAFxk6RjyoYcmi64Hjyj0L5Ddsz4oOkZXD9GhevaXxlgoE01IYdojcfYzAeAzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99166" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekj_SaE6MiaTVlgA5hAUjfemwhHQit35t1HoevzSQYUFmDO38TnYQdIvebyfBcUyRX643HgWV49ja7PAhooK2RtCoFsL_anfmANDsLWy6sCkZ7lrKs8qe2Hqnh-Zc1cLLfX-HfRjtFLbcsjbaumhVpMS4AXtLvSkCa3ZG64wnr264bHXuQ5E74V8UfHg1Ih64MVL0o9MnUE7ZkPcro5KYkLCHdzmnGnfYOPe2oQlvYGDFl7VfZ7vfXqz97gT2mdmK1jq-pkBcbFTEEdHth0CTl9knBfENGO1v6bxVc0Krh05f6yXbmZzNI07TsbOXv5qPkUdvhrCM3zQw8ySuJx0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
هشت‌تیم برتر جام‌جهانی از دوره 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99165" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99164">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووری
؛ اخبار غیررسمی از شنیده شدن صدای انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99164" target="_blank">📅 12:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇵🇹
این ویدیو یه کم حجمش زیاده ولی ارزش دیدن داره؛ تو این ویدیو به وضوح یه تفاوت جالبی رو ما میبینیم؛ کنار مسی، هم‌تیمی‌هایی که همیشه پشت کاپیتانشون هستن و تحت هر شرایطی واسش سنگ تموم میذارن در سمت دیگه، رونالدو که حداقل در این تصاویر، تنهاتر به نظر میرسه و آدم احساس میکنه فاصله زیادی بین او و هم‌تیمی‌هاش وجود داره. دلیلش رو نمیدونم چیه از شرایط تیم گرفته تا تفاوت شخصیت‌ دو بازیکن، اما یه چیز قابل انکار نیست: کریس در پرتغال اغلب تنها دیده میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99163" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99162">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=M5fzI2eYKMZxPsG0aUJCNHFTXrcfarI195kmvdnGcrU3P_oo7mE20qXu6WQMsDyY4wpc_AK-wAJY-NyPyMwMsaRwC6xUbhiaIKapQiGDCuFDlg4OFYADZ_XeIf5cORZsjZCeVUS2IcvkcAS8YUSq-3kedMDRxBzM7EXewQdhsr-beWRU5ss4kR9KdedFjdR5vHiXgh5JIFowhvVldABmrEqb3K2tA1Ilegfo8AQVxa6-9z6Fy9GAessAfqlLTx96CiFW2LG8wYwpa70crRPJ_Ju2nd2FVp2njETbZncq5qFIvxTu4nRY0NWsyzrbqWu356oJrSDNp1ZpjqP1wmDkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=M5fzI2eYKMZxPsG0aUJCNHFTXrcfarI195kmvdnGcrU3P_oo7mE20qXu6WQMsDyY4wpc_AK-wAJY-NyPyMwMsaRwC6xUbhiaIKapQiGDCuFDlg4OFYADZ_XeIf5cORZsjZCeVUS2IcvkcAS8YUSq-3kedMDRxBzM7EXewQdhsr-beWRU5ss4kR9KdedFjdR5vHiXgh5JIFowhvVldABmrEqb3K2tA1Ilegfo8AQVxa6-9z6Fy9GAessAfqlLTx96CiFW2LG8wYwpa70crRPJ_Ju2nd2FVp2njETbZncq5qFIvxTu4nRY0NWsyzrbqWu356oJrSDNp1ZpjqP1wmDkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط کنفرانس مطبوعاتی براهیم دیاز دو تا از خبرنگارا دعوا کردن و کنفرانس متوقف شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99162" target="_blank">📅 12:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99161">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3CH60M5ci2GISaXXHDYHQz1gmE8AfDsuvC585ITgMIxRJO41y-8BBDVGfEdTQL_hKFCrfZq8aToCh_5z-XEkRccaBVVqJCBUmLYFkqqqQuI_EzR6O1fJDrGPDmMLUhq4pJq2dwRuEIfO51Q_8YIGeWj76hMdLt0Ph_gFsg6L6rbQ-EU1mi0ZRYJcouwnGFAxWoy4FZ3kZSjw9xE9XOvo8LVoQy2bEZ67ZWQKlzGtIIKoCaSUCLJc0Q_k71ADluBavwtz7H8PNyFLXDE5lEh2oyUWlKX794OBmTxz8JD2oK5bbnvrOS9XBPAD2STnDqVM_jcRRBx-_zXaU57q8tDAO60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3CH60M5ci2GISaXXHDYHQz1gmE8AfDsuvC585ITgMIxRJO41y-8BBDVGfEdTQL_hKFCrfZq8aToCh_5z-XEkRccaBVVqJCBUmLYFkqqqQuI_EzR6O1fJDrGPDmMLUhq4pJq2dwRuEIfO51Q_8YIGeWj76hMdLt0Ph_gFsg6L6rbQ-EU1mi0ZRYJcouwnGFAxWoy4FZ3kZSjw9xE9XOvo8LVoQy2bEZ67ZWQKlzGtIIKoCaSUCLJc0Q_k71ADluBavwtz7H8PNyFLXDE5lEh2oyUWlKX794OBmTxz8JD2oK5bbnvrOS9XBPAD2STnDqVM_jcRRBx-_zXaU57q8tDAO60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
Maradona.
🇦🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99161" target="_blank">📅 12:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99160">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=YGJt_vxXjj3qy_iC3YOMGTzAinFv2_njJsqQAnXXNU7ZbmVDRuhYTnnOm6rA3l_760C52TkRACvtIH1CAz2VSvmXu0rUP-8zHdt6zn7vj1gk22bsmAuJEUYeaEdeCC92hkoqGU8Lubx0oGjinfhcMFKl1cx5sX0T6cg1_t-T8EEqbFvvaXXn9e1X2LXnuTv8oVyizMO82BSDTmkKB-O60saNR1-MV0Y1_Sawgj-j4g4-FOwbvXukXOYGBHfS2P7g4h5gw8WLjw7k9JKQRJbypnL_gQkaQXeQjRbfWPJvlX7dwwcbMC-uT005AiOPcbeLbsnG_TkGLhYWolj_te_TwI1u_WRwp-Rl-wKuJVMvU5rBI4fd1rS1OqMvLyE1N5xbCplg6ug5H32V4zsSrODUWQpL1dInV_uYMCEvn8PTq25M2tRJ-NdNKSisOaabkv666Sv6euQ8FeEIM4h9p4RzZAke5VSeKsLBGzNMybpLlxJeAMNxxZAevqTY6CGUsTfIsGAr1IZScuZMZyO0xxKYXxHzLhgnTMoIq6qm54AJdwEBNZvvS4c5rZjO-m6ozi1f-Jb9ak12JeJ6nUp1ul2E6Zgt77Ln3qerl3WfPoOITDlNfOhPlooyF8Dbr8BWW3kvMaN-SqEYFY7_sZ2MIMXhp2zMyh6Lynh7VOjOXcfSrD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=YGJt_vxXjj3qy_iC3YOMGTzAinFv2_njJsqQAnXXNU7ZbmVDRuhYTnnOm6rA3l_760C52TkRACvtIH1CAz2VSvmXu0rUP-8zHdt6zn7vj1gk22bsmAuJEUYeaEdeCC92hkoqGU8Lubx0oGjinfhcMFKl1cx5sX0T6cg1_t-T8EEqbFvvaXXn9e1X2LXnuTv8oVyizMO82BSDTmkKB-O60saNR1-MV0Y1_Sawgj-j4g4-FOwbvXukXOYGBHfS2P7g4h5gw8WLjw7k9JKQRJbypnL_gQkaQXeQjRbfWPJvlX7dwwcbMC-uT005AiOPcbeLbsnG_TkGLhYWolj_te_TwI1u_WRwp-Rl-wKuJVMvU5rBI4fd1rS1OqMvLyE1N5xbCplg6ug5H32V4zsSrODUWQpL1dInV_uYMCEvn8PTq25M2tRJ-NdNKSisOaabkv666Sv6euQ8FeEIM4h9p4RzZAke5VSeKsLBGzNMybpLlxJeAMNxxZAevqTY6CGUsTfIsGAr1IZScuZMZyO0xxKYXxHzLhgnTMoIq6qm54AJdwEBNZvvS4c5rZjO-m6ozi1f-Jb9ak12JeJ6nUp1ul2E6Zgt77Ln3qerl3WfPoOITDlNfOhPlooyF8Dbr8BWW3kvMaN-SqEYFY7_sZ2MIMXhp2zMyh6Lynh7VOjOXcfSrD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
احتمالا بهترین تیم‌ملی تاریخ ایران :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99160" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99159">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=ZwdiAWGRQdRHV1B0mQiKRNbZHI4oQ9bKV2g3OjQmgc0EtKX71FvfngAwoTkcYANPs7gd4HxQLN96FWtihhPPDFykquTjsT3QU_pkLF6OLGC4cWX8PDcI-Onw2IsuT6jBry7shUPLiksbKyAQsOuhpkOcpcZoW7dETJcUVpyM7rwkGNQcPmwtRqG76poYOpxt7vi_W3q3fS7oUeYLA9R_8L4KsDO6nQRcpajyWgQzhaAPjwi2Zt1sU_eQrjsp9NAMBm4cG48avmYa1eLInRhMkDWg7lEAPv-awOxGxp-AhqiDncI3h7UzK8NwQHn-5TNfNlhfWXgFsUDLk4eLqqtSr4RI4oX65IySUtkA7O-laJafr2dcXyhWb13A1nA3Xo6ejBUJ_T0YUqDejkGFr89AIH1vczYHVwu3uyuL-WxSRP8yDnYFrPMlJ5aw-29ym-1a1b8QE0Fl6rSB7GR7jX4IrekeMGrEboQV1066xw5WaNBK9VLtGdEe2XP6GHfLlyUwqWJzmi5JZdXVnn1_pDjMgSH9zAA7eJJmeCIKPqt1FzVIJilcB-Yp2_C6hhiiF_Ec0Z2PnVw_HVP6gMOm9ovGYNuSYg3FPT-vtBOEz7s_bCAVuz06aiIpAozcYK5Jmfuzk8H_qTizZlED-7X_DBUGsbP25EvrewXdslnCwsFays0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=ZwdiAWGRQdRHV1B0mQiKRNbZHI4oQ9bKV2g3OjQmgc0EtKX71FvfngAwoTkcYANPs7gd4HxQLN96FWtihhPPDFykquTjsT3QU_pkLF6OLGC4cWX8PDcI-Onw2IsuT6jBry7shUPLiksbKyAQsOuhpkOcpcZoW7dETJcUVpyM7rwkGNQcPmwtRqG76poYOpxt7vi_W3q3fS7oUeYLA9R_8L4KsDO6nQRcpajyWgQzhaAPjwi2Zt1sU_eQrjsp9NAMBm4cG48avmYa1eLInRhMkDWg7lEAPv-awOxGxp-AhqiDncI3h7UzK8NwQHn-5TNfNlhfWXgFsUDLk4eLqqtSr4RI4oX65IySUtkA7O-laJafr2dcXyhWb13A1nA3Xo6ejBUJ_T0YUqDejkGFr89AIH1vczYHVwu3uyuL-WxSRP8yDnYFrPMlJ5aw-29ym-1a1b8QE0Fl6rSB7GR7jX4IrekeMGrEboQV1066xw5WaNBK9VLtGdEe2XP6GHfLlyUwqWJzmi5JZdXVnn1_pDjMgSH9zAA7eJJmeCIKPqt1FzVIJilcB-Yp2_C6hhiiF_Ec0Z2PnVw_HVP6gMOm9ovGYNuSYg3FPT-vtBOEz7s_bCAVuz06aiIpAozcYK5Jmfuzk8H_qTizZlED-7X_DBUGsbP25EvrewXdslnCwsFays0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
فینال جام‌جهانی ۱۹۹۴ میان برزیل و ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99159" target="_blank">📅 12:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99158">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99158" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRpmo4jQg_aAeqEO_ETRWdBnaXBkBvfRYWr2-OgIqTueix_Y6NtyBOHuTAAy1BYmpSVWGEHEUNyiPnJ0v6bZKywely-hJMudhMDugNkiRLsailSE80mhgRiiUV8zlcmHugEZMs3PUXcK90czNJM0t5K5UW5DKK8ma6VWYbM0DoCtKn5cryZT-hFh4xQcjl6ywDGYlQ6jFih52-gq5Z03tZ8BNIRE7DphBenZsvV0DsiyWHsOEClNI7HVoRdgfKb0ohuuyBXJDY-yp4jRPzbMTI9dgqPHyCMdR2mzZiGqcQhSJTpkQJU6BtT3sHdTmLnWDd8qFEkplL_188-1yFEAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
❌
#فوووووری
؛ اسماعیل سایباری ستاره مراکش بدلیل مصدومیت امشب جلو فرانسه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99157" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99156" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=KcrRkUO1SxituQyN-I81jAP79emwBWSuNPxEadGKXQUqbrzaoDE15YbS3sKW42ctnASw_4TeFfEnrghFgtzyGKH1I1p6iLE_gc7LnwSmtR5WbB--SVXyGs4mrwYup1B6GcSjptiLXsat4uz-4Pv4xlnJXVJgZUeVPf1YUBuOkvDntdkjIUd9xKJgJd9KTkuZjaj20MnrxjEil-aHgFYAoeAzCRPhpnJBrA9cCb5CjZ4jNnE5W3dAWQ-QIiE-wicYGd7Tf3RYyrqyN07f7xFEBOAxgl_g2SRktDBDCPe24Zpd0QFdjcqOwQ5y4jS3VZa6iVnX2pOddJd5kmZCQJPONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=KcrRkUO1SxituQyN-I81jAP79emwBWSuNPxEadGKXQUqbrzaoDE15YbS3sKW42ctnASw_4TeFfEnrghFgtzyGKH1I1p6iLE_gc7LnwSmtR5WbB--SVXyGs4mrwYup1B6GcSjptiLXsat4uz-4Pv4xlnJXVJgZUeVPf1YUBuOkvDntdkjIUd9xKJgJd9KTkuZjaj20MnrxjEil-aHgFYAoeAzCRPhpnJBrA9cCb5CjZ4jNnE5W3dAWQ-QIiE-wicYGd7Tf3RYyrqyN07f7xFEBOAxgl_g2SRktDBDCPe24Zpd0QFdjcqOwQ5y4jS3VZa6iVnX2pOddJd5kmZCQJPONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇷
🇪🇬
حرکت زشت و تحریک‌آمیز بازیکن آرژانتین در مقابل چشمان محمد صلاح!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99154" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو فنا در حال امضای قرارداد 10 ساله با تیم ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99153" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID5brGhZCuj_w0bJGU5iS48WLKAziSbOpTOOic9Q8MiaG2XZEQkJBTkSOe0KJMqcukpukzz-HmoCC1V2VOpjMNSUg10V_qVzAeW3BWvtnN4r33qlQX7ra4wr0cQHhO6gJfg-bLsimMYmZ_wqe6WTYBdbJQPD3SWow1zfxxY2o41tp1wFhsCXf_NyEt3VTcZSc60wW5mCdi1scMXIYObTj1Cey0rZgJs7fVnCgJT0tGMqoH6XVPMk6ippLcnH4HFUpVnlClyUpx0-IdcC8ApD8YMc7tXLWggOxwQtFBMWNNmrPXsIXhTdJHQlqcS_9SsjPRaCfaG9_y3b7EEBmupBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
#فووووری
؛ هانس یواکیم واتسکه، رئیس باشگاه بوروسیا دورتموند:
"ارلینگ هالند علاقه زیادی به رئال مادرید دارد و این را پنهان نمی‌کند. به نظر من، او ظرف دو یا سه سال آینده در آنجا بازی خواهد کرد، نه الان، اما به زودی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99152" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHhPcutX_INxtXm8X42T6lPhDX9qb4jNCRQ4bZE9n7qb2jJpTUbrnRixYJMWztIDEHbl3f3kmwSPReXLgC7rGYEo1UrYD1Sy9U6BjAj3IUqQZUO610qQROycJAoeCUJgNqjYHA6IqiTqTMolL7leHr5itpMisXa2hmQHF---RvAcFEoAdbijleP2zXf583EKQGe9GfVlH9yikTy3LBIg2KrxklIyaxbqK6-ef_cVHFlNP7z_qoA0V2XddI-hPQ0JqBKx8KwAd12peaBiqMWZvwO2g7iFAaPR3zEgNLxxviqyxgkmrhb-Ty1mgXGKyWWqXqF8xbAy2zOW5f5Hb84bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— نیکولا شیرا:
- باشگاه آرسنال و برونو گیمارئش به توافق کامل در مورد شرایط شخصی رسیده‌اند. قرارداد پیشنهادی تا تابستان سال 2031 اعتبار خواهد داشت.
🔥
󐁧󐁢󐁥󐁮󐁧󐁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99151" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تنها چند ساعت تا بازی مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99150" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔥
مرور ده سوپرگل تاریخ مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99149" target="_blank">📅 10:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آنچه در بازی آرژانتین - مصر رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99148" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT_s29aIp-C0AE9dMmOJafcSqr1f7KzvolBDCNKExNjnX5og0M9rzhILxinyBkwXYuFN_5prHBDHCrzQbWWrMAPgD3eZnibvGFbldzvNoYStupHRx0oOWS-RhtT5svBY2f5x0HQF7qr5wf0qS7U7wk4qfKfnoYKyND_BIr_Jz4TrpNL3BQ8YFHzn1iFNald6cVVdp32dyEeYMpfeBGuMdwkkGG7rjFPuDIUYwWpYohxt513I5pb2MUWu0SUCcvNZU6MF2QTZPRbOyHtPnBVcUNy6vcB4n3sgexVvQZHiBvvC-ShejmN_TBBtU8-PV7caT8Apxxj_XPYvqlAB-mAlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99147" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=Sgc9w14KEVDpWiQYiJYc0ATC3c4wjLommCb3mi3KsWm1haIXETZCKbgMe30nR6rSgu7OBsFoE7cpOEE7L4oq0Linwg7uJu242KHuahBuC-CgH1VdGslnBvmv7AvgkFZ_HcQV5LyPRCZSQ_SswMNZDSdDsMvmlZu-63xIwWqtTNiLJu5neaKIF4g-x4Yl44ryKnH05otu8tQdsZsWISg5XxeWetQPhBEfqhw4EO9ovDRMopgupxm6M4KBiUxnyiCnL_BAXzFbjSEqTNSiuPzNInj-zkNDwKQS2iXYAlkSHLL-QBO6woBHj-EdYCJn_eJoHOs3TvTECikaktkFkjr6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=Sgc9w14KEVDpWiQYiJYc0ATC3c4wjLommCb3mi3KsWm1haIXETZCKbgMe30nR6rSgu7OBsFoE7cpOEE7L4oq0Linwg7uJu242KHuahBuC-CgH1VdGslnBvmv7AvgkFZ_HcQV5LyPRCZSQ_SswMNZDSdDsMvmlZu-63xIwWqtTNiLJu5neaKIF4g-x4Yl44ryKnH05otu8tQdsZsWISg5XxeWetQPhBEfqhw4EO9ovDRMopgupxm6M4KBiUxnyiCnL_BAXzFbjSEqTNSiuPzNInj-zkNDwKQS2iXYAlkSHLL-QBO6woBHj-EdYCJn_eJoHOs3TvTECikaktkFkjr6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
شادی عجیب و غریب خانواده آرژانتینی بعد گل‌ سوم و برتری مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99146" target="_blank">📅 09:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=JBfzACGcBN0yXS-pRYPEjkgvB0fGTg7o7Q0_1gASbmAzy-6liYcFMv0uKHjj8GpaHJsXwV3wjWobAd21NZYd4VH53AJXcD0dUUWYEUAQfv07BohyW-x9Pi7EhpZt6MWuZyXr9N1bnlE0E8Fkp7nkBSVCTc2wiqZisA0gxIrMYkURrbdOMRnNu8_hCddRNw4G4mcNva1ZTfL1vwThTNQ5p_E2cUvt_lwkLlq0MlfsxX8vV8fsP2IVqX0J9W-TdvCFGAENSaPDfEQE2TtcUEhD0sjdR8_YgvsU5IX7_Owo2q5VTYu3YHsHkyjKTMgq-EveIjSImLH0kOd9ofZYhTAjrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=JBfzACGcBN0yXS-pRYPEjkgvB0fGTg7o7Q0_1gASbmAzy-6liYcFMv0uKHjj8GpaHJsXwV3wjWobAd21NZYd4VH53AJXcD0dUUWYEUAQfv07BohyW-x9Pi7EhpZt6MWuZyXr9N1bnlE0E8Fkp7nkBSVCTc2wiqZisA0gxIrMYkURrbdOMRnNu8_hCddRNw4G4mcNva1ZTfL1vwThTNQ5p_E2cUvt_lwkLlq0MlfsxX8vV8fsP2IVqX0J9W-TdvCFGAENSaPDfEQE2TtcUEhD0sjdR8_YgvsU5IX7_Owo2q5VTYu3YHsHkyjKTMgq-EveIjSImLH0kOd9ofZYhTAjrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباهات مشکوک داور بازی کلمبیا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99145" target="_blank">📅 09:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG4NmwYiDE295AIqa1E24h0bfcbTOx4VYBrx1uEVb2ARW3oPtMwkVOtzykLR25RE5QNnE-ysbmJogIy3tYpFDSCoPmbMdsB5nNQFGAepxDVswIAdx2tWNfGU_CJaauzT5hFCKGHSrerFNVE6lyPNDvFH-NMSb1yM1VPodJ6FvJhWQM_lTvXSHDWzu0Zk0K8HEynivX9XomesKBrFjbD50oeRy0C5xPd7V5Sbg0wT4EtDPmoBLg0MgDhQ0I7N46AeN4minDJK6aPOHWQvtdyjZIzW-dq9zmYg6GF7I1g4YcPyDpCjYhmpqRpB3wk4vLLh4d2GGH7QBWDckTSjT0eS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVlIoJISRLUbpc0Ti3qMujPwNosyNQEneJLG-iuk-dCUoHW4STd-ZhnCsrSZlwqXS1rTsrVAsSkHsIi3ZdOA7EFYmTWJCyIf1UJZDpoGZD3X8QeindKu8BEjNIeT-my7yzszANhkjxy2KKDksurUfqB36BROHoK811GeuuFTt8382bYWqE-zFA3ofmMWHvKiCijXmjrp-11ddTTOJY43hePN_d4AjyJURAdPhzAvRHltY2HyZckO6FYXrTpaXe1res0wBHz3wotVe3Bu78_KlMj8OkSZkSVds-5IbDrQaP2y91ggud_nW4atypwXW9K37smV5BeEmJeDVtKjQ7s8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=V0842hYtXK6vxu2USifJqO66K3nORjv0YYH8Y8TxM3v0qgufhnx2Hy8JS9o__NNvXmeOYjyXFbDY7LpX-QzztxIyQ9N57fqDa3sY51zFDeKNY-h33vL8BzTXdgpqJhsc8AVMxyS8kQfs0-D9hXxo4lqWQs-dX_o06sksDUpWidtmfHUyRu6hua-_2y9QhXna35oIMrtTL6uoScDXkJFDmsgoBqwUVWgbalxYZGcMqM2vSWcqelzf90t8WGGSWWSw1kr_nQi-c3LAFGKGcvw0rut9laIAxrXsAJkloSgkA5lngeysBJEBl7uTMmJP4qriKCnllaJ-RAXtR1Z02jKttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=V0842hYtXK6vxu2USifJqO66K3nORjv0YYH8Y8TxM3v0qgufhnx2Hy8JS9o__NNvXmeOYjyXFbDY7LpX-QzztxIyQ9N57fqDa3sY51zFDeKNY-h33vL8BzTXdgpqJhsc8AVMxyS8kQfs0-D9hXxo4lqWQs-dX_o06sksDUpWidtmfHUyRu6hua-_2y9QhXna35oIMrtTL6uoScDXkJFDmsgoBqwUVWgbalxYZGcMqM2vSWcqelzf90t8WGGSWWSw1kr_nQi-c3LAFGKGcvw0rut9laIAxrXsAJkloSgkA5lngeysBJEBl7uTMmJP4qriKCnllaJ-RAXtR1Z02jKttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To5_esTKSNf_7vnEp9VVTp4wjkMsXaC5BSMJd4DClyyTilz3zTNROm0qo2u8vHIEeQNJRAC6hP2uVKz0Fy7JHgO2j52Q96VLULtsrym1W-CliqCF4CIPooCjvlquamtd0l7NeGfoAedxH-tzpPPVkdaoJVC54K0Z5We1u0naNMfOd-WgfSUol0bdHHlDD86WeHIbesWXIm6gF8Jr5NU9yzVgp9xufOWBbS4W3nYs6S1Rn1LNNFwHGc1-ZU2yEzCzAX_hnO2UVrYIBpI38rYgHnZ1vjVcp-vcU76LsTstQmmACwa8GqEZ2vppA-9R13XyTm7Sn3tQiQxl1BVDvirbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/99139" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Kl_c3w7k1HiU2jSKWpSjP0X3nv72m08FeJnPVq1sIl8-2Z0yYRY3X5kmamf3GUaHXGTSS_kejTZYnVev3Nv08LV4B2nJy4cyyYVTC6og_3NxuUAauKRJuB-ldxI2dxelkImUHlUxwR71HSo84tOeDpmVT4Z9fJIbuExFMUf_dF-umBwkzdpE-2T835vfOl0ETveZczpy7uOTC4mQxu9EBfzwt2R1YE4MnfR5eI-TnoOffHNWxwsYh5ppTFniWBo8eIP7jlHgD3Jm7x8e4-hav9dQqdf22LnOSCPX_nNLN-XDhv9ZBeRCg11a_4aFYH5h8aU9OHbssj2idxoWBx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تفکیک 3 هزار گل جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/99138" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/99137" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DDFjNy6IGrYpywpT_-uq_ZfAesGg3C4bnJS893zvUHnHKIBXFGF7ubvUPcR76_sc57-WrZwDMdTGh5qPc1oSDPEu6AEYYvcQJ35LvgzLThortF8EtDT_dCgNaSv2quJA7DF7M1b8KE4nVEIljVv-JoS9-Xj6Oae4mmN49HkKBeX7bNrwuCAMOyt7wVtxxEVpTVZ3ZuDJVoRpgnnp6IpGj0ERf7rkx2z7IlEFiLncD4t65pZXhaKpBZBk8iGN7NSzdCBdjlaUD_3wjhmbSTs0IvdkrorXOUCiBuPg51qFzvkWsvuc7gfPXI8Aa2hBFnnDnnhzVykCZwzfNBI4MbY1HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99136" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
رسانه های برزیلی:
ممکن است نیمار در روزهای آینده از فوتبال خداحافظی کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/99135" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enNEBeIWsezVKGmhjqdoCLO6XEi-pUsdNsBmE0Jm9jxT1xrRsNFdoE_IwPLyujzpbTAz07bunkIfsoTPKi7hT4Jemv5DSQIZ6O4g_HyUlg6mXshsbO4ra3xAF5AExBPvkZKvhR_PX3_K1C16JnxUOuIk80SpHCH1na0bSDsGBuhfSPk4Q8ZqSp9GhpsebruZgDifiT2SPO0VK3LDZfiFfOhZUpwdqXlrNL_t5C_SP9Ybf-WY-0obSP-v8TvxD83en8Hfhb1fi3z4rXBv_TRxvQo2CuMtCeOzG-ujMXFzjQwDm5g-abV_OELpmiK7PFpFeXIrAn9h4Px4eLmlENjywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو:
بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99134" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99133">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViLpaYTEezQyl3u8LqGDCfe9tWYpprHUQiKBo3FHTfC5__pNMMs7U2l47x7C0-BuVzo53zeEYj1fR_z4KCOf59iY432DZnw0m-BtDleXIngXpCjQvnlLNBKKrVcJgPALv75xxcZ-oBbPwx6_ZssyzZ3cQIX9rNZ0iC7oCsek4C_5KHhnpCfu1nWSf_kzsqZSLH03mlhxjVjP_eNyE_8V_as2fFVDNgiPGY5JGLCflWsfLIeJ4X1QX3Pn9yIvODca2oAJ_MckWAhhg2Qo3dKqTw4kgJkvhN3R5QYm9h3gGbxcB2ENF487ribWtbdYP979j2IX7wkNA4TrEd2cSuNF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب مورد حملات آمریکا قرار گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/Futball180TV/99133" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99132">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
حملات امشب آمریکا رسما به پایان رسید و تا ساعاتی دیگر حملات سپاه به مواضع آمریکا آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/99132" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6UAvC6Gqc62jbw0XjKCe5jnZNi3gVgqgZZk8_yGKqcE69fDGsbhRj1FJpekRykRFPQBU0Wytweo5b4u0QExTIqJpqTmTdZ6EK6_ULfnQa9U-dZWAzte67taSIvf6R_RTX4tuclwxIPdm-vtH1ShhXwkYLddTqj4QKWB41dys5p4O74qugMYNNCFPSDYF_Mz0Xne-NrqrVXEbooyJL3Fz-oxF1A-rTu5G7k4i3fYMj2sdGp4hoSB5IymhZk3k4jmKkyuiSrw1YRHHIu18J_W0zdnS2nQ0Phn0c4smiwstCmGj839rCAJ7lZcRX5bSxGn0ESCSfgbhaMoT9RVa3EGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زیدان:
لیونل مسی بار دیگر ثابت کرد که بازیکن سیاره دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/99131" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99129">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_kUg8oQTqJua09COb9LZ0zHeb1bOGTbCGpVbyhTYYDuMvIbRKAhU1TMP3GlGC1u64Tu9X8dwT1ZYaMrzSblzZybXBYDIEXRhM8rbpd6thnglqnQAGdkkc0QMuJdbM4-atp_p68myAcPer_NULa_zfcD3x6FIeP0qcgm6hzk5vAw-HMPEmYqdNIgjAzC8FZjDyfq_1jzr1nFs1uDypMB6sf6x46k7RT-RL5EkSyT8pd08lshfeCP0ru6C7RRFtoMIC06ZO2wJ0uTg9VbjO8prUk8Ii4i8vXBsA9F2BrIqwwNa2IipgvVb8KjZbpyZIdWxcRFhBnlfAGzFi4UWDe-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/99129" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از کنگان استان بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/99128" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ttHl-uqAjWrqb_hV9zWRksXo2bqcJE8eOhqNWQq-tZ02Y0Dok6aCU5JK0olG6Wz83hoxOsJGYv0_YsHJUpZMDnA2Fskscr22wYMe7p979o9JXrZjyzqVxB81NxafwcdBZy5EvehrXgubfyobJOjg7s7Vi7RouCfJQV27jwW1T6-8pbq_f8dN8lgSvLOxxKWRgA-eb61LyjYq6zUwRoW7hbOtLrk-Hwh-VmEiEIHAudYsK-83LUcMxmW5t-VCNRq1U32s7FW_nRK1-EsxJrhbEYUHXa9ScrVaep56O230Sy3s1AawgwvqfflkRr74URQYPP56ClAPSDCpklugTiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
محسن رضایی: دشمن متجاوز و هم دستانش به شدت تنبیه خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/Futball180TV/99127" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
یک‌پهپاد آمریکا در جنوب ایران هدف قرار گرفت و سرنگون شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/99126" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
فارس: دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/99125" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJLZHkAYVKF43XRCsrigMMsQS3kmbFSU-DQQdhKBmpRJdw0Samsgx0SERiY5Ib2Y_aHSGO_iWdYmy78je4Hi1F60Qrzy3fGf_WP_o6IqwIlNgsyC9cd4V9u54yF7rsPOi2hhiyOU06wSZvIndlx1nPt83cXnzzPIglBR6b8tB6vLD6_M8PKqAk9xaD9WNNaHeQtNzholKbpSY1VwyxyIUECrboEFQq1Gr7aL3PfreJEEJohFSU56Y7CGTHhzSn9qWmDo-OXPKmgF470iF6TdYLdm6h0QTXl8f6h1raZX8HpGDB_uEkSYdS0-PTDDJrEkX9SRYPYsVcO7VU9svtnitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پست جدید کریستیانو رونالدو:
‏"پرتغال، همیشه و برای همیشه."
🇵🇹
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/Futball180TV/99124" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
مقامات ایرانی: تاسیسات‌نفتی در حملات امشب هیچگونه آسیبی ندیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/99123" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
انفجار های مهیب مجدداً در بوشهر رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/99122" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ انفجارهای شدید در جاسک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/99121" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوووووری
؛ اسرائیل هشدار شلیک موشک از سوی ایران و حزب‌الله را به شهروندان خود اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/99120" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99119">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی: حملاتی که امشب انجام شد، گسترده‌تر از حملات روزهای گذشته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/99119" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در جزیره ابوموسی/صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/99118" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeUBxtQHaY23857FYZbtgkTHOBmC8ENg8EdNa0mYZTCqcALPSUOD6IDmv8yV-E6eXFQucPJFxX3g-cXYNjnqhOUsXN9OTXyNWymkZOrDGP0-jDUEChICp_Iree1uwSnhjJVXgIxOIxfn55iutwVf1pj2dON8U-uq-gpqhm6D2PBUfTROZ9e3i_LytWxPYCv2U7uoDPTtuX2rLLAl3V4apo1ZxXAP4kvmQLV32mcM0h_FZBB0tEgwy_vdWUqPt21mvHcaRNRFw5Fr33-IdMWG9zOkJqKAn_HmUWj0r4JPiQuh4Vg0EZ82cm01c1rL77DRSV1oTwgG4JdmS6bWH1ytpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
تصویری منتسب به شهر بوشهر
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/99117" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کمیسیون امنیت ملی مجلس: بزودی پاسخ قاطع رزمندگان اسلام در سطوح بسیار خاص و ویژه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/99116" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
منابع داخلی: قرار است نیروهای مسلح ایران به زودی حمله‌ای گسترده به پایگاه‌های نظامی آمریکا در منطقه انجام دهند..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/99115" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a36705c.mp4?token=I1HyKd_tSYGZNz2OP6et9UxnIFI-f7YwNRTVDij71fd5KbArbTf5A8tFzGYbcPplmrgMpoYtd81KIB7-A9oeSib5USxhR_AxJNzuTlan4NPxiaCdzq7yp8ezrtyKggZWJaspolYMPxwZLWA8DmSFFnrJIa-gYDZoP-crzoYWYNE1yBX6kKsS1HIil4q9jwf5yRdmixJW4tjoSRP2xoAM0v3KHO4u3h-0ryWkXkPa4pRPewf8mt7SIyg9dbSQqt_qkVhQuWoyJG8H4k6PWlpbR7puSRc_yWqQLAG7gytokZhPkV9j_Af84fa0Y9yW3W4LliiHGHV5b73IZts9Y27i8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a36705c.mp4?token=I1HyKd_tSYGZNz2OP6et9UxnIFI-f7YwNRTVDij71fd5KbArbTf5A8tFzGYbcPplmrgMpoYtd81KIB7-A9oeSib5USxhR_AxJNzuTlan4NPxiaCdzq7yp8ezrtyKggZWJaspolYMPxwZLWA8DmSFFnrJIa-gYDZoP-crzoYWYNE1yBX6kKsS1HIil4q9jwf5yRdmixJW4tjoSRP2xoAM0v3KHO4u3h-0ryWkXkPa4pRPewf8mt7SIyg9dbSQqt_qkVhQuWoyJG8H4k6PWlpbR7puSRc_yWqQLAG7gytokZhPkV9j_Af84fa0Y9yW3W4LliiHGHV5b73IZts9Y27i8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ ویدیو منتسب به حملات امشب آمریکا و انفجارات شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/99114" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووری
؛ پدافند اصفهان فعال شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/99113" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار   @News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/99112" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeZ0Ci3SSWih5thfWwLIliaveFge2b8RIvgcewKEnOGE8etSSPU25_mZkBKb9h_3FtCZ7p8Z4TJOwOOkNyDJaDNtyPHI4xJALplwIMu_l3_x1UIwxL0EGVQn-lP0FECJ6QX7TMEFxoEapCG_2Em_4MNLGvjgerG2Mx5R9sMnmx-ch0InBPXljCnaDwPJn4IOj3S0XlHLn0dJc3l__Kw0rIf0bznIrj73epPMmrM7GP3EDFVGuC0qU7bTTx_0Af2I2QOHEDY5KPqOQFQgDadekmPIpW3ze3ZLIrZnABHKPMOGcXYKzL-WbRj9SIEXiu5UIjoRz9Iv8ENBqFFqFr7rcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
چوامنی تا سال 2031 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/99111" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=Fj-_NHcUbo-CEeu47wvG9SPCsfAXYmkK3CCmgBowe6O7QrnfJQfR8ju9tdJrwwwA8hRYQwRflYUHDI5THvAs5W-yz25dROIg3A47XHRjMWKwEQ6iBnNMY2q9izttCM-6lCtpF9nmjXW7hOcqv-ktIqbWF1vhquglet-HHKJ9t0uyp8zm5OQItY4ebRsF0_8rSaJt4YzbeJqdsfgwfQB_4MXlX97mWwqU2G44yngEkuI_0-8T4D67q8-MEMYPEOE8eSnuxFnD6hPcrKUgaUhsi-cK7a5qGIBCYj25G_KR8LHfLlh90mkJ1swx4VNRUOzZGtoAIUys6AAglo0jrHip3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=Fj-_NHcUbo-CEeu47wvG9SPCsfAXYmkK3CCmgBowe6O7QrnfJQfR8ju9tdJrwwwA8hRYQwRflYUHDI5THvAs5W-yz25dROIg3A47XHRjMWKwEQ6iBnNMY2q9izttCM-6lCtpF9nmjXW7hOcqv-ktIqbWF1vhquglet-HHKJ9t0uyp8zm5OQItY4ebRsF0_8rSaJt4YzbeJqdsfgwfQB_4MXlX97mWwqU2G44yngEkuI_0-8T4D67q8-MEMYPEOE8eSnuxFnD6hPcrKUgaUhsi-cK7a5qGIBCYj25G_KR8LHfLlh90mkJ1swx4VNRUOzZGtoAIUys6AAglo0jrHip3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات متعدد به جنوب از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/99110" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=ciRXpiCBc-_BjgDmdc7pRy6T1I1lzk7CiQe05PQgeN5vZqK0fZUhV3CPr0ZrRMwcJZ_kCFfb13mdnzXV1LMfsrrQDZk9x1RA4B3P0kZWIRXbS7THrL6vX4VssdE6RPkGgL5X5fiyyU0ptJeyJ7nUp61hYW22sZhrNzaTo0cmEJjWQwfEnFncNEFMhbcu6DjiQJK83QF_SaV9XH4cyRG8oUKVWSoMcJUMZ5duQ725eX2mMZS1UWdQsrqheRSOjcpXLwD-ZmJpa0GegaQLsEZ4HNcjfkaL-CTPuweQXnhpT7lFK8vJA-_3NlzxMWJncrMYHK3zqv0OeOZd_a8uq_AKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=ciRXpiCBc-_BjgDmdc7pRy6T1I1lzk7CiQe05PQgeN5vZqK0fZUhV3CPr0ZrRMwcJZ_kCFfb13mdnzXV1LMfsrrQDZk9x1RA4B3P0kZWIRXbS7THrL6vX4VssdE6RPkGgL5X5fiyyU0ptJeyJ7nUp61hYW22sZhrNzaTo0cmEJjWQwfEnFncNEFMhbcu6DjiQJK83QF_SaV9XH4cyRG8oUKVWSoMcJUMZ5duQ725eX2mMZS1UWdQsrqheRSOjcpXLwD-ZmJpa0GegaQLsEZ4HNcjfkaL-CTPuweQXnhpT7lFK8vJA-_3NlzxMWJncrMYHK3zqv0OeOZd_a8uq_AKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نیروگاه اتمی بوشهر هدف قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/Futball180TV/99109" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/99108" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99107" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
بیانیه سنتکام؛ فرماندهی مرکزی ایالات متحده:
‼️
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند. ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99106" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=TlbRAiYLD01sIfgWATwwfqDvwNYDzuioWWJBE6vzxVvrpCV1Vp4y7vesofeodBO5GzP1JrnxuFUiA9Lo-3UYbZllDshkVTNx7QzaRmPuLuixGkxIzh8zlOyQfkSIAlpNna8ayOQGgVU-ChbCoX6GWPuQLFKRfqQawlD7fQ9gvcC2-KJE-wJF7t8cG1qB3CnpXQKFrrJ74yH-rtDwCqFh7SK93XPOMo3vIDq9cjlVpThQcCPL00sQoH60Spg1WPrIGH4uOFkJZUj-8VZCtA1jypIhOns1l6I3wpIXflIkxoX5kdCwJRRWkm8oWmmnT8F4OPGZZebzDWlaBwflF41a9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=TlbRAiYLD01sIfgWATwwfqDvwNYDzuioWWJBE6vzxVvrpCV1Vp4y7vesofeodBO5GzP1JrnxuFUiA9Lo-3UYbZllDshkVTNx7QzaRmPuLuixGkxIzh8zlOyQfkSIAlpNna8ayOQGgVU-ChbCoX6GWPuQLFKRfqQawlD7fQ9gvcC2-KJE-wJF7t8cG1qB3CnpXQKFrrJ74yH-rtDwCqFh7SK93XPOMo3vIDq9cjlVpThQcCPL00sQoH60Spg1WPrIGH4uOFkJZUj-8VZCtA1jypIhOns1l6I3wpIXflIkxoX5kdCwJRRWkm8oWmmnT8F4OPGZZebzDWlaBwflF41a9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/99105" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99104" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99103" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
