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
<img src="https://cdn4.telesco.pe/file/hIuGvJSyWv7e0pfT0duJG5ZKbWz1UJ47rSzSkhdTTafNlcq2NCdhPlaoyoqxJiAXGfzuKj1hBWkBhNkPAshTSIJ-OJG8Gb_zWzKs3RGUXoOaeZGpugzuAECazilHsIaZN0GKqFWD2pSKdib8O_p9_7aNnJ_iaQg_YvoeOnqGjd91c4ixQEzSzZ5SO4n9YOlUolfJmODdHo-Xn1eJ-lCO5l-FfI9SCp4QCLdvSMKM4DQJCQoVY49wPhYm8cXRqqdj4THEGDCMOUATxBeu3EwZpE3zj5OsVUI5s6la5TwL_iATw302ssiPoY-wUwYjfxmnzp0deFimXp43qg3IQVsXfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XclirMHnNPE9R583h4viXvbz7HW7Q38VvbEQbTGyYbC_BjT5jiXKfs3I6fmdKWZ6wBki7BB6T5CgISULXMk2kdzOqxCEGigC8IlFT_goZxGtVGVgvmHxnuTz2Hju-50FYu8OyZn1ZGjlTAXdSQXzp2ti0nxHspzgOMUApW5b1ParLuCdlFWOWxR1ht9MYsVwxrXsR8hgJ9SKu0tMZacPaoiAXUpLwRv9JNiF99fAL1Gsy9IsUCDGflvRJWm8w8JZjTGO_ric1M_zrTpmYLiQ0CMKSiF2WKKOrAc267yDNbtd0725NZffoDyPqqNF73SNErm8de8k0Sv0FUQ0ksFxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQfNUPLXqF4oV7Bvp-w6z0zeq4wq3hvi7L-6v8jxDDV71jujNi1sXzqLrSMFR1jpfjQ0STbBEcRaEMa73Ds8vaHg3SJgJCfYZkhcOd79lxnlzIroqHTXihidpV8CiCgKhW6WR2GnDqzfkX93Oda-bdgIzH4DZfIDVECdFVTnkKNY_dky9kosnDuxFSI9pKqgpTVYal2oySZBJungAZHhn1sGfDYzMG1BodmJveyqXobrkx7fJYSt466NmQxs0nHVu6yw44vJbORwHskBnSZWRfckghJzXoC-lzMhUO-mpbMtPlcoHHe06MTcVm_bxPxBietwIICYoqh3RQ-0iOuc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjbCnIU9n9ZFYxSLASrCAmV0HyP7Y1DlD3kKEWbiSg5x0oFzsndcvEKUW-aMfdct5-Md_OiH976nNSLTJoU7E5sazhpwGpQYmcWSdAPEsJImSoG5T-44uXZzo79qBACDZe3g_HhZD2TJ7KALv1kHLywiRqZEm0X2_-2GI-f3Hec6t2689rT7qPoohiYw8FLhnJMEsyBJjhB-g7OWCjeq0ZxPUjcbrClDNkVGGgmiexldofdF85m3_SucTXQK8IXh8DgMFG12JtM4E8jQccHpOdoh5yLseawyGtO_ZitjHA79aDQ40JbL13jDJsFrk_dxyoizAy6oB13u1n_xGvlQ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8QaVCiSgjqKt3lQNkGke4WP7wKPCum7YPspOz_5vRPvpstcqyTq_zrrVmbxOErTruSgZugM8HuQhLki4SjNCYSBPuGpkz22zKMNwOW0LfL41rri8ng7f-Z2a4R06K4hi8NxND4cKdJHlf_h8sm6F9nWNi8LTZbcniF0vKJQfdV86BMvRYkhXPDy3NKt2tAeqzWm-aAunsCxfOMggPCJHsoRY1xazl-sJhe77BpialtfVTafOugdThvsM0Ba22G19xkZbitMPpW2g4wMhzNnKKr3ds4Pd7_Fb8u9BNnAxFSWf3wOCHzv5CuTxWy9s_vqDIuYmEL05QiCr0FffOm_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0yFpXdHUEN-PFI8WC0-o3kibSmjTAjugpFZTY-mgkF61uBSj1MH9LRjzFl3L_3-dlSbrumV7A1aspc-iStpMjz-p0BjUi3jQAAYuznFe0TwGJHbhhtkohMAZ6yd0bGhdkCVGBQvXae1BwOBIuuTBFDmT8pT3xVpiMW8u8_VKJ4iM0ZuLPRABBpuWyQfw8S8daxZ7iYocGp4d7cJOFZS_Fe2A3vFnqgoC-rLR9RZKqZ6VCx23eCX8Tsd3roHrGD7bTvTDFi57J9DEUO31WEskkzLSIlF2aOwHk8V5z_SsyLneVgv6QI9E4EXPrx3LhJ8WXiyCrXGxxINuuaPQ19WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qMT9zzcCutRbQ6rO7KjoShWi0j5uONoM76s1s-IR2Grq41urFIFcgfIpFPYVSrj6ueTXTNorPpkBosJLjXJmYHlisNGcy1xIe0MMuA0HeFAGU-Gfs6K5rP49IBkPehOxaI_q6uKFLLZQuzwqHHhHC2jPU3qUcvIWUwVYZUqWXWPyK-c9WTqzAGDU8n_f7mbXg4pGbP76LEs7ZAeLXd3d-HQ2kbYiip2CXJFdzax9qw9C-aqcrwnFm77ogE8BqOQasZx9jitEDaKkqGvoG8H-BGFit6enxblmIpbZbS225SEKEaJvDj0i7xHw0o5wDVOMQxycUccmoVhm6bmXQj-XPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0UhY4FjdKvZlVF6Sh-inuefri5dvi5_hGgFGH04teDmzJOvVN5XtdL9AAVOO1cgu-pPAwTIG8tbaUheat16BVBEHXyaer2JtUnhWV4cFqECmrh5TH6c4WMkvBE-FoKk6SaFMWELP1iu-ESNlOTccez5vRijPNwGECbhMPcbRoqEtV86imqqfIuw6rbEoVRkW0v9BnCsY5tjD1G03URTj22hgbVBwmf9IhmEfp5cCPh_D9AHyCzdmwO7guGLRTupcEQxJZ4FuvGWwe4fMzGY25EoidhBnL20IdC7x8XTRPaYfwCVAC3be1RAzYVzCqGyfizLJsQzoDCJP64N1iLwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkpEHFhS8tUeKasqd1LXL-FOdbDmH1wiGoKzGPVuWgHvEymV-k9DxEbOYlIUuPb03ghkVUJyDHxv4OXGzgxPgNJzzvwpYNgs5cyMsJ-2AEx4Ve-UXyfGbTJoGDsj07s9LDEzPAU4n2fdJWirQOFxXk3-2MnOUkBz1uI5I8-BrnuYsWg4XbvLUsPPhIRL5gVfx4A_gY-nguzhlqa9QJwA1AkqosYfJAGauJCK3k_iiYgUvYzzELK_xNm3v41b0DRO57GsDSDra7GbbVi4b3Y2m4DQJgKudJ2XO4HEUYP7aBYU0tKflG4NRx9gjHWqteH9b993gRwDkpVi9QQOol43YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=QTMTSfycvoeidzDzxUdLTGR2Yj2v3XCXB8-5XVf3Ku3T-4vCU9owcQGwYYwchiGi73ZfsjcR5mXGdfN4ST2PeOdSzCf1Qm1Yc2T3vG-G0VObj_k_NnONTc9bxZ8quzf8bfbDWYUeYZ5Zw7V31CpPPonQTWgfQYj93Zt9wh8xW1iNUm8JmU-Kcfx3xIDGqjhzbJd5LC0CBQCuD4in9aArP0A4XpWmygf73CcCuVLGi42xE7eIiScGFD4eZIK7XEVLntt5l38dczQqZ3CF2EIIjpXKbIh6feCyiCMhvOt_SzAHTxEvivyVYjwaT1wt28Gib12EtyBmiEVQxfg1a9GA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=QTMTSfycvoeidzDzxUdLTGR2Yj2v3XCXB8-5XVf3Ku3T-4vCU9owcQGwYYwchiGi73ZfsjcR5mXGdfN4ST2PeOdSzCf1Qm1Yc2T3vG-G0VObj_k_NnONTc9bxZ8quzf8bfbDWYUeYZ5Zw7V31CpPPonQTWgfQYj93Zt9wh8xW1iNUm8JmU-Kcfx3xIDGqjhzbJd5LC0CBQCuD4in9aArP0A4XpWmygf73CcCuVLGi42xE7eIiScGFD4eZIK7XEVLntt5l38dczQqZ3CF2EIIjpXKbIh6feCyiCMhvOt_SzAHTxEvivyVYjwaT1wt28Gib12EtyBmiEVQxfg1a9GA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=Hr37j7mBNZzsK2l56Q9M7hJizKBAcbVb11PFrgX3q_0GiKNLeZCjV64F8mh2DUvuIPohK-2_qN2if6Rj4O3xS6iUlcoIwf76TiTjtEGdqoRWBvCEzWlT2wLyg8fG6K67YW3XwpjxK9WgQC8vKjZ-Ow_EeHutYnB-D9fo80QSUIFvP5UWZQYD2SCeo7HVdvMA1fZP_rt6-RRLEXXaMspuzavB5BTZ54a7_3NEOWVPouC8Kye9oStzw28Em0tPmJbuyCDJLEISguujLC0UEz4EgQhTbMpwiHjb5nn0b5ucaCEQOolML3m9eLbbicTYWJLmgn9mUNtK3AP4WndGjLENMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=Hr37j7mBNZzsK2l56Q9M7hJizKBAcbVb11PFrgX3q_0GiKNLeZCjV64F8mh2DUvuIPohK-2_qN2if6Rj4O3xS6iUlcoIwf76TiTjtEGdqoRWBvCEzWlT2wLyg8fG6K67YW3XwpjxK9WgQC8vKjZ-Ow_EeHutYnB-D9fo80QSUIFvP5UWZQYD2SCeo7HVdvMA1fZP_rt6-RRLEXXaMspuzavB5BTZ54a7_3NEOWVPouC8Kye9oStzw28Em0tPmJbuyCDJLEISguujLC0UEz4EgQhTbMpwiHjb5nn0b5ucaCEQOolML3m9eLbbicTYWJLmgn9mUNtK3AP4WndGjLENMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=WXvjT4FIDSB8AlPw7Ja7hcMuvCc_q2uOxsR_x2aIai_pp1j6o7ZrtJG3-yaZ04DC1QeIhLEh7SLTTORLjOXPL3EMtHCPjPqFpXMMg4WQoFRnDuUdl_BNJhwz7A_ynhi5ggxArN6O66R40VG9rV4_hrxbb2M88hpkrys4FIFUezhPWe0406rDEMxmbAQDgAjKmROcy8ymvcf8rd-ktUqyU9hcqIREP2DXgIcvIg4t4_V8U5tL_cffp372vPApTSMpogYZX5EY25951OCkpx_mFSAf69w6wA0a_4o_NVpHfCE5YfsLmSwxkLmHQowdyZ_pWFhr78Szhq1XyRBjPTRsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=WXvjT4FIDSB8AlPw7Ja7hcMuvCc_q2uOxsR_x2aIai_pp1j6o7ZrtJG3-yaZ04DC1QeIhLEh7SLTTORLjOXPL3EMtHCPjPqFpXMMg4WQoFRnDuUdl_BNJhwz7A_ynhi5ggxArN6O66R40VG9rV4_hrxbb2M88hpkrys4FIFUezhPWe0406rDEMxmbAQDgAjKmROcy8ymvcf8rd-ktUqyU9hcqIREP2DXgIcvIg4t4_V8U5tL_cffp372vPApTSMpogYZX5EY25951OCkpx_mFSAf69w6wA0a_4o_NVpHfCE5YfsLmSwxkLmHQowdyZ_pWFhr78Szhq1XyRBjPTRsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2ONNq2hDzGlgb6Ud4dSjiwddobvkn5GxEOTyWf0UFip-mS61bzCXSqqCOMgVIvJa2Goqv1zCznSCBdX86nx1V2uc-Dc2MitHws_6io-u9R9coEMxnKLZt3RKDHo02Br7OCFN3idQfzvJ6JdNP95mOl3K4N378KDBHZfmT21ssN4TlsgvOOPFAPHoikAYSrjXbrUwqI2Vnkj7S13RROacoNe82v1BbV4Eq3z50j5ZaBD-qakzTldY5qRTQp47LRfZkcUXfcK47wdWGzgQdoILJ71quBFeuWdIIG_fqzABHyvy3jdHsdF62wR3mNHqukygheA-mhUUjxFO3bpCjWzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=qfUwLk5CLb0TvFOUW7nyA1sMtpx2pMUDagMy_RPkWWNomCNSKB21ODBujAxg5AXtANdS7iATgiEhILih87POnWLqPtWFG-dbqYNrJAnAjiG-grX_Xh1LwU1P76z_ca6UJ5dzgFUfFFqL6NGzyQtXFKyEH5WpAZ1eHchd5-pnkYxnx_IBCR5cqKyjKM42Msf6YhMQ-VPN4SqIN7OoIUO0hQE-HA-VfpphTGERR4ItuOeGDY-CkX1g-y__IU_i_sZwHRU747mUi0JhtvOaXQMllapVA1MJcjPSIw-3sQJWowKdayHt32i8ZHGLjWewcV64g0-7iwKlML-48A-WATq9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=qfUwLk5CLb0TvFOUW7nyA1sMtpx2pMUDagMy_RPkWWNomCNSKB21ODBujAxg5AXtANdS7iATgiEhILih87POnWLqPtWFG-dbqYNrJAnAjiG-grX_Xh1LwU1P76z_ca6UJ5dzgFUfFFqL6NGzyQtXFKyEH5WpAZ1eHchd5-pnkYxnx_IBCR5cqKyjKM42Msf6YhMQ-VPN4SqIN7OoIUO0hQE-HA-VfpphTGERR4ItuOeGDY-CkX1g-y__IU_i_sZwHRU747mUi0JhtvOaXQMllapVA1MJcjPSIw-3sQJWowKdayHt32i8ZHGLjWewcV64g0-7iwKlML-48A-WATq9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ALmZiLBAjMyAbgDgJPfgXHT6nHe6puJpZYIXiI-DA58maZDuPgoq31KE0sTiYq6MaDz8X47U_4kgE-HjoqsN5rPHmRDbc9Iojfi8atKrMiuafRqQ9zxvhSIOsdMUABvZgn5npXrt-3A0YAHb6UozuZ_jS4f-WPcqFwkUQzH25ZxXJS_FP__lNKWKt1yphn2h2allTj4t1P1vs5ugTLjxbzXW7daST1C95zYy9T4egIdyr660Nr0XJg7TCQSYxhrx94GuVifFvi38O_gcdkoeBQd_W4G6q5nH7BE1ffOVJPVBuXKHAjKkRbMAoURQoBnvhULAMES4vV5y-g9N8UageQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ALmZiLBAjMyAbgDgJPfgXHT6nHe6puJpZYIXiI-DA58maZDuPgoq31KE0sTiYq6MaDz8X47U_4kgE-HjoqsN5rPHmRDbc9Iojfi8atKrMiuafRqQ9zxvhSIOsdMUABvZgn5npXrt-3A0YAHb6UozuZ_jS4f-WPcqFwkUQzH25ZxXJS_FP__lNKWKt1yphn2h2allTj4t1P1vs5ugTLjxbzXW7daST1C95zYy9T4egIdyr660Nr0XJg7TCQSYxhrx94GuVifFvi38O_gcdkoeBQd_W4G6q5nH7BE1ffOVJPVBuXKHAjKkRbMAoURQoBnvhULAMES4vV5y-g9N8UageQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=ZCbG4RA3SYv3FxBbsxSXhdS5ZYSinQMjsfVckRI-NpAgs1ddqlEeIT0o1lqh_LOieKk18eo5GsNnMGEfuBnnN4pRxSG_zThuVIgV4nd7fjmIfEvfrvKSOPdcK_-N1tPT8KyIeR9reptrNMONpNNJRG_hA6Z6be5Ju65vkn0AjRZZ8-p45HPjMBqijczjcYfifdiLveVRpu08G0aizeMDUBOdr9d4hIsdQRlv9wWUm2H-H3C7h7o0bHrbhMFi0le2gVTynKYPUTdTzS5tFoWs6zEXctsKNLVhgVGdMbNFoXmpdEyN7RBZVEZ80ckigKA0of8H0vYwBX2b1NEgYLeFnDjwpZtyuSADia4UvQSiizAAi9UV8X083RaFexxUYaygFkx0-9B8F0pkI_M91q0zRD5ADcgUpmMxHXsuk-8ihYfd2pWEqvxgXwFoAIwYJtkuVFSI0pBuFEFTwa0JohzExTGmGpDtbJXM9beMptogcTA4obZ8TkfHSA_t6pSiutkUzDLJxEqbyrK0ZCq3nI5E76eAhknNdBMF_vBCM2M-JKN9HEtaZrUr02X0IUbqoWmUY36NiWSrKAyHDAKk9SisObWGZKjU9ZRsC4SuPX5JcHD7Dg4p751_lu-sllYfuoDSqKhofQs4SSVtN3HpcuZjoxgbo5Rpk1IQSIxMW4SzdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=ZCbG4RA3SYv3FxBbsxSXhdS5ZYSinQMjsfVckRI-NpAgs1ddqlEeIT0o1lqh_LOieKk18eo5GsNnMGEfuBnnN4pRxSG_zThuVIgV4nd7fjmIfEvfrvKSOPdcK_-N1tPT8KyIeR9reptrNMONpNNJRG_hA6Z6be5Ju65vkn0AjRZZ8-p45HPjMBqijczjcYfifdiLveVRpu08G0aizeMDUBOdr9d4hIsdQRlv9wWUm2H-H3C7h7o0bHrbhMFi0le2gVTynKYPUTdTzS5tFoWs6zEXctsKNLVhgVGdMbNFoXmpdEyN7RBZVEZ80ckigKA0of8H0vYwBX2b1NEgYLeFnDjwpZtyuSADia4UvQSiizAAi9UV8X083RaFexxUYaygFkx0-9B8F0pkI_M91q0zRD5ADcgUpmMxHXsuk-8ihYfd2pWEqvxgXwFoAIwYJtkuVFSI0pBuFEFTwa0JohzExTGmGpDtbJXM9beMptogcTA4obZ8TkfHSA_t6pSiutkUzDLJxEqbyrK0ZCq3nI5E76eAhknNdBMF_vBCM2M-JKN9HEtaZrUr02X0IUbqoWmUY36NiWSrKAyHDAKk9SisObWGZKjU9ZRsC4SuPX5JcHD7Dg4p751_lu-sllYfuoDSqKhofQs4SSVtN3HpcuZjoxgbo5Rpk1IQSIxMW4SzdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxZlKmi4b8n9qnvuFx5sw4_cA1wCXJTvebQ4-nQPVX57DMVWnByld9BEehGV66yXU7UnW0WJTbPro8l2LoBt0u0KRNL9luS_bTNuVdBU2aaUBRElqAxX1zeyH5ovPhCKWp4mlidW8stF6yfcbU4YWPfLBo4HMCvitrhovHH5-0Nmfm1tusYm7kUwLnPJCEK6OONatvVqUn1txb6k1PPzERKE2vlCV5ZK56-GsMK5ZanSkQmHeBV5OMcYQvyyjft4TA_weMkkoWjlOWit39TUWGFRlnsKHhwxnu5Kb7EWEukT2m1uitR6IsP40nSJUxI7QEhKkWjmP4liDVWOSDB7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaNk5Bhmk34tOFhNSUnp4OTOXtXmakuWlusfClGRCnG1rMergtUj4tc7ri_h1l83uXlaUVTa1_7T2ELoGBLd_SG0CMSZvdNuBHMRDSBrajaxur6CS3gV-A5Qkk7oPG5x66erxsOV7qd7pijHY5UWRf-6exhJPnyCiruZc39wgaABQvkNWCUMCBNCk6kyC9jyZZaf6YfifemVgOMKmlNZY5x80A5ozfBETyooYDjkZo2oY5vpyfUaOFhgMWRH4bp3ssx4Jb632ivH4KvxWKhwzqVntFmC5QFbOKzQ3O6F1fc5JY-HmIbWerlOgik2dAr2f3THSQm8tSA6uegMkut4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=MGBfTc-yZ_JOFBTXzdzhSXgP0mYf3thQvhSGsHhF1rskSudEVYQQGMGEsDfDND0WfhUJ1RR8hPQv2jOWP29Lad4_r8LdF8MCAvcj12qbakO9vWAx0EHel_kGzxJyeG9zNuIT0lQBH1rDGMv0zqdTAhkrtHoVNC4w-uwpQYZ64knwYsgMkZp3MHk471CAkJyaLEUeUHen1DtOlEEqEdiBhcYYlGlmzJwWa-MDf2lvyBKBCKi7ORN_WNvtVzI_wkp_l3HK4OYkG4x2HYZhDtdI5iSZk1gktraS2aBC51aNgJakMpLZY2vAhlp01PHNJn5Zlb1m9mgJFmlvf_EB7ES0aT7fcOy56iP04Boco0bKbhuuMVSHBviUw7yVI_YeQMwcFmtZam49toQs9pt8n1iwr9FB0GVHdDEJ26aPstl34B6xuU2d6IH979VmU0vOE3dWKGY9JDVH9kXDJ9vjVwl0ZmAsj6CcjUlHb_5WrwgWKmEesh33SF3wYPJBVrFmwlNEzq1H8sa8KRboPtAthzcwurwgv9JR8KDdCkTXvTgBR_047ygWHg6DkGihobQbq8LvgPbVaR8h6OUwDM0P3AWEDmrn0_u6WHfeXHEjgnpphPGY_BGPk0EdX6_evnOIruOYIc6wiH5r0ccngvrGe3CT0G3MG0i0B09ClQcNzytMsGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=MGBfTc-yZ_JOFBTXzdzhSXgP0mYf3thQvhSGsHhF1rskSudEVYQQGMGEsDfDND0WfhUJ1RR8hPQv2jOWP29Lad4_r8LdF8MCAvcj12qbakO9vWAx0EHel_kGzxJyeG9zNuIT0lQBH1rDGMv0zqdTAhkrtHoVNC4w-uwpQYZ64knwYsgMkZp3MHk471CAkJyaLEUeUHen1DtOlEEqEdiBhcYYlGlmzJwWa-MDf2lvyBKBCKi7ORN_WNvtVzI_wkp_l3HK4OYkG4x2HYZhDtdI5iSZk1gktraS2aBC51aNgJakMpLZY2vAhlp01PHNJn5Zlb1m9mgJFmlvf_EB7ES0aT7fcOy56iP04Boco0bKbhuuMVSHBviUw7yVI_YeQMwcFmtZam49toQs9pt8n1iwr9FB0GVHdDEJ26aPstl34B6xuU2d6IH979VmU0vOE3dWKGY9JDVH9kXDJ9vjVwl0ZmAsj6CcjUlHb_5WrwgWKmEesh33SF3wYPJBVrFmwlNEzq1H8sa8KRboPtAthzcwurwgv9JR8KDdCkTXvTgBR_047ygWHg6DkGihobQbq8LvgPbVaR8h6OUwDM0P3AWEDmrn0_u6WHfeXHEjgnpphPGY_BGPk0EdX6_evnOIruOYIc6wiH5r0ccngvrGe3CT0G3MG0i0B09ClQcNzytMsGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=ulh_imdW0xP4yLUdK5xfAaERDAIZVajUS6_RdV5dd62F0kqRdERJUK3jcxgUEqmyHblBXj6zm4pcZJXWwF8XH7KoFwio_arPA0FBZOyA7ozt1wgr_61wQLyM99ReP-_XDOsTkWSqwuufqlh7AvLN6wXm2ug0Ky527mL5NAtO8Ca5qTi-SJih4nH9FXbcEoegHh03thhq_rMYyiB076QZty_xrN8KzzpyJdyE1Wn2YRygdYrHbWTtXGZ1uAVnSaYdQYfNudFSmexxqji_djwJRw3cwAwyMgy7UrCZ6UJ-tWIOr0ZDJGnMXOxsNFxB14LCh1kTfHUrA4Pj-n4hMMrxdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=ulh_imdW0xP4yLUdK5xfAaERDAIZVajUS6_RdV5dd62F0kqRdERJUK3jcxgUEqmyHblBXj6zm4pcZJXWwF8XH7KoFwio_arPA0FBZOyA7ozt1wgr_61wQLyM99ReP-_XDOsTkWSqwuufqlh7AvLN6wXm2ug0Ky527mL5NAtO8Ca5qTi-SJih4nH9FXbcEoegHh03thhq_rMYyiB076QZty_xrN8KzzpyJdyE1Wn2YRygdYrHbWTtXGZ1uAVnSaYdQYfNudFSmexxqji_djwJRw3cwAwyMgy7UrCZ6UJ-tWIOr0ZDJGnMXOxsNFxB14LCh1kTfHUrA4Pj-n4hMMrxdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=O9RbaC77ajQjLaMA2MmuK7oK8PBeOkMJdKzUImrOlRjo5XqwOp0w8xlYRY47t6GtRX7W96Ld9l4vjU5z6PmECuzc1DmQu0l4X65PdrcYI-TwM9TXQtZOOgmTS0eTGacD_RqOQ2gDA26H3LH8Q4T-BmusAF_AuEOgiUs1tUvJ8ag7d9imwJhWbb9dtJcq3IdNwbPJzXw_J87ROD0oMiId66uP-XzM21LZcAXZLb4PnyYnSNJEHyWps7sRk-vgGF2V5iYE-AFtarNlY_ebqXKOSbnthF_SrL4CxgkHdte9774LuXEs3WESCzJ2S0FBXc2-VHQKm4eiVoUacTwF-nrBuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=O9RbaC77ajQjLaMA2MmuK7oK8PBeOkMJdKzUImrOlRjo5XqwOp0w8xlYRY47t6GtRX7W96Ld9l4vjU5z6PmECuzc1DmQu0l4X65PdrcYI-TwM9TXQtZOOgmTS0eTGacD_RqOQ2gDA26H3LH8Q4T-BmusAF_AuEOgiUs1tUvJ8ag7d9imwJhWbb9dtJcq3IdNwbPJzXw_J87ROD0oMiId66uP-XzM21LZcAXZLb4PnyYnSNJEHyWps7sRk-vgGF2V5iYE-AFtarNlY_ebqXKOSbnthF_SrL4CxgkHdte9774LuXEs3WESCzJ2S0FBXc2-VHQKm4eiVoUacTwF-nrBuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd4vATKPnPKUe9vzyQa3do-BG01oAA0oxUDRWyAW_Xi7cKKinUarlih35BqEYaCfzXRaWrgkCGaaYCT9qlRL-O1MJpQEJOod3L2YubfUNNmcWE6B7Vk6NKr_IKxzqF_BzhbfQx2gojrMk9Ijc1JeOl_IUDwhzXv2D0Cis23DAWNNeIEu6MSDClMV9biLZhPSqBaDuX71m9HjtyECJaVVE86NXpcnLGZzA8YIsegt36NJRsikqQy1JvVdi1BXNpwGi2qkSBNtEVGEExD9Zxm4FkWW1fQziB9peQOK553oeQgrCmfYV5aNwajVxxb3Z3B9g-OqM5_iyCmgnlM0kMwwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYV9jWuDKX7tl9CJmJIDtAjFtQSevu6sPPlcMqz7TRmS3PSsd2AhSTOJwoGVJp6KvI5TmaVh47YRa9g_xiYfFQj5gnML7RwvoU3vBZ5t2drUpMJzUae47suRbTu9KwXuPCZeRmcctrRtxUgSaU0dBiOQCA0x1D_qVDqno6LlMkvk5uP4yvLm5_H_0Xjto6SPJVD1m1cOCCej6EevkupJDFPOxQPZcOgDjf1ftLYPe3aFeqsyP4ckhEDlQk2j7eI3ojsHg_RmXpSBuCsTxcEOkB2luBwugJf6mcnJauwXr81KWWd4_nrVOq9iAJYgLzSzGbxQ4qn_Ph2ZbcHLjYWlvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouXYypYnbib_zvGrNudGfo98X3uazGvoUH4eqqtTfNhp-INFBPXFoTLThIi3FMZ8qx66NFBCmaBbyLojNbCshSbBjjJmKgo_p17Wio3eT9BBqQx0UUjaW9b_KjdhyKmE5h_qDeTh0VS9d4mj_sNKKf2dSVV8gZGic1mLQJAUJL4lVVktFfRwU57HDFwQHgWG3rXGzm35d_TH-FKJZKYczvdVrz8VcIDlg6RPJkF29PayeqxQos9zqM5pSWIbmtFFsF3XwuucCRm49Lzig67H_dejLRVTKBlbrSfO8-aOmI6iGuApgHhqMsaIuLxfRG_xfU-zr9jLXC54GDXq1-_EyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnyQGiU7KmtdASIXJk9HolrPCRESHS7VJbGbqWIsE1eP1ckmn-ocB4svLiXw1DwrEAfuiYR-JwMLwg8ygle2GPPBC4_w-sqbh6DWpcS5LJhlGFewp3_DgKzDPe5mpenlfGQ4mlNBWhpctSoOjLIAzKzwkMxmpTsXn8OVOMcrL9Y_jB4bjcGsuGO-Vy76eZy2yiYlDGZFaX3QxwimHYDvmwBhLDNMA5ut1CSFMNeKBvzM4EzcST3AHnzF9bJ7R7VXHDoOdBIoekqKT8VlHxdJKFTfDjY-xTU_i8MzYl3lyFVAaO5c49-kHiV-3O-oOGGvI2bSsZHyYeZeXL-Msu3Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=SnAdICGpivka2H8QzsRUJ9Da4Vc7rvP4uwvLG9wtEToejJe-5uX4C83pJ7qFFY3ZZ2DCVK_FxvdYiaogO_pAzZ9kT5pxSK7HTwQSxF1roT2fCd2znok9LpUmLpWists0c-mqljjViJPzkO413SJWZYsPNKh-QAg66yeF0fWuHzbWGX7Px7NIUFOr2xFvocy8jGMM47dUQeZCXolA3SgdmD6Kv1pFigZzmQr0G6RdyP9wmAIRGjJt2qCeIRXgTDBjNcv9F_ciq73crX8IlxJyorcm-URk9X-xT9GMog89_O-lrTVcsLZIs9NIs5AGcbbPd8XLVIPvMuOWRiCBXVaOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=SnAdICGpivka2H8QzsRUJ9Da4Vc7rvP4uwvLG9wtEToejJe-5uX4C83pJ7qFFY3ZZ2DCVK_FxvdYiaogO_pAzZ9kT5pxSK7HTwQSxF1roT2fCd2znok9LpUmLpWists0c-mqljjViJPzkO413SJWZYsPNKh-QAg66yeF0fWuHzbWGX7Px7NIUFOr2xFvocy8jGMM47dUQeZCXolA3SgdmD6Kv1pFigZzmQr0G6RdyP9wmAIRGjJt2qCeIRXgTDBjNcv9F_ciq73crX8IlxJyorcm-URk9X-xT9GMog89_O-lrTVcsLZIs9NIs5AGcbbPd8XLVIPvMuOWRiCBXVaOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=P_H3Pe0N5U3L8lmA3MNLpgKu3a79GK-QE4FjGamr9oXp0OptzU3etihZFaamIxM_nXCMdbbkvjKFkPiFFLNbmKPRQzjWvLUlQW0NOggxz6H957fDL3eqorFlARwo1ZC-_G9H7AGxCJ7fOz-9jPpgMNgcMCZ43qWs-Mu9V7RSwk0kJXztE2e7okLjSJp7sFJs12_nFj-7XOyFN347-krD5o6Snqamy7zRjg0r-3GoKGAgMe51v6jznjq5PTovSqfUclxlgeQN1zaX36Y6m-MlDFNqa3EdvjdyJgcHOl-R_yIe5DAwA0bROWD1WPBwQK1inLKIA507EYcPg2gnuU0ZTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=P_H3Pe0N5U3L8lmA3MNLpgKu3a79GK-QE4FjGamr9oXp0OptzU3etihZFaamIxM_nXCMdbbkvjKFkPiFFLNbmKPRQzjWvLUlQW0NOggxz6H957fDL3eqorFlARwo1ZC-_G9H7AGxCJ7fOz-9jPpgMNgcMCZ43qWs-Mu9V7RSwk0kJXztE2e7okLjSJp7sFJs12_nFj-7XOyFN347-krD5o6Snqamy7zRjg0r-3GoKGAgMe51v6jznjq5PTovSqfUclxlgeQN1zaX36Y6m-MlDFNqa3EdvjdyJgcHOl-R_yIe5DAwA0bROWD1WPBwQK1inLKIA507EYcPg2gnuU0ZTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=SC8EYe3ztnBcrCOqeX-_qznJLknjwd4klbt23xxhBkYF0ETi-m2oB2Rcp3-rjpeqLa3cwSnS2br45LAbKJF_Kh20bIDFoR_QjL3SNBkk3bu7jLTi1oPYglWiVEoolDqBfa_PVVvrkEvfm9VRmAqLfVUxp1PtSuxj3EBn4gegfKRZZ4v95fKlqS74cWrm21wbwUrG3wniBpNFPthcpytBDiILfVbOKl7ccP9nOakMtRGSbjCnDMoKEfDj7e0uz8OQVtYXYTqvEQpRcL9KIGgpCiVPztKAYh1sl8KXvNavEHbIT5OI5m9jdGZZg9XxBbE5NhFm07I4M8RgyLeU8MJe3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=SC8EYe3ztnBcrCOqeX-_qznJLknjwd4klbt23xxhBkYF0ETi-m2oB2Rcp3-rjpeqLa3cwSnS2br45LAbKJF_Kh20bIDFoR_QjL3SNBkk3bu7jLTi1oPYglWiVEoolDqBfa_PVVvrkEvfm9VRmAqLfVUxp1PtSuxj3EBn4gegfKRZZ4v95fKlqS74cWrm21wbwUrG3wniBpNFPthcpytBDiILfVbOKl7ccP9nOakMtRGSbjCnDMoKEfDj7e0uz8OQVtYXYTqvEQpRcL9KIGgpCiVPztKAYh1sl8KXvNavEHbIT5OI5m9jdGZZg9XxBbE5NhFm07I4M8RgyLeU8MJe3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=n6SEP9CKZtQQi43NdRXAkacIK4vU66_JcT7EdtNwO3na7aZo1nlmWu-5Yrznx6X2qUmJMBR_eKPI3nALT8hljjtmO4ym5nTDdqMvJArrvXAcKSe5o8v8v00fgjDEiGfU0z_4EuGHCvIaEBj4n0fiqw6u0x1WerM9_03YFPxVfSiP220TBVTErhNX8OpGJyv6aO0kDPSip6YYe1pO4QYxnFtOkkz4T7975cFiNYzPX8XBdtbMysAfLqsI8cExhyHr7Y4JR4o6LgAJ3OqEAT82bEQwclEPAn0P7_-QLCPMgTtSib9dBMFi73WYpoKaU4OWA0jWjBk7dffXu747qk18BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=n6SEP9CKZtQQi43NdRXAkacIK4vU66_JcT7EdtNwO3na7aZo1nlmWu-5Yrznx6X2qUmJMBR_eKPI3nALT8hljjtmO4ym5nTDdqMvJArrvXAcKSe5o8v8v00fgjDEiGfU0z_4EuGHCvIaEBj4n0fiqw6u0x1WerM9_03YFPxVfSiP220TBVTErhNX8OpGJyv6aO0kDPSip6YYe1pO4QYxnFtOkkz4T7975cFiNYzPX8XBdtbMysAfLqsI8cExhyHr7Y4JR4o6LgAJ3OqEAT82bEQwclEPAn0P7_-QLCPMgTtSib9dBMFi73WYpoKaU4OWA0jWjBk7dffXu747qk18BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=W1tNaBbGsSnOTLZZJF-p8gQH3vB4V1I5I-t9rirHEd_QTqw_m8AxolDCZjTIzwkxrm23cx69S2glGpZOUZhT1WQrUaczTjNs7760wpHvfXQPB0znZUAVjJUf_vhbSY4s9ENPzKN9u9NNns-B9Ybt0cQHwKHI9JEto3WnPkNDWRvPc9zPIvalcAXnHJ32MEQhE9IBS3PMFKBzZeF1iHtBrGlEhTLWKmYsDcs-0NRhgLVPodRlhry7pfajTKNHdk5V2iH7e6oUq4WRPUj3hVmyK6Op3TV9UAkrDjvlrctF-ooMcR9aEj8laHQk1f-hE-cAwU5uq-qNwSoOk4Cjk-DVLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=W1tNaBbGsSnOTLZZJF-p8gQH3vB4V1I5I-t9rirHEd_QTqw_m8AxolDCZjTIzwkxrm23cx69S2glGpZOUZhT1WQrUaczTjNs7760wpHvfXQPB0znZUAVjJUf_vhbSY4s9ENPzKN9u9NNns-B9Ybt0cQHwKHI9JEto3WnPkNDWRvPc9zPIvalcAXnHJ32MEQhE9IBS3PMFKBzZeF1iHtBrGlEhTLWKmYsDcs-0NRhgLVPodRlhry7pfajTKNHdk5V2iH7e6oUq4WRPUj3hVmyK6Op3TV9UAkrDjvlrctF-ooMcR9aEj8laHQk1f-hE-cAwU5uq-qNwSoOk4Cjk-DVLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=KZrLENEUl90O4vfHr9Bovm7JzIsk3k-z5QG6Swuds8ska8bw0RmYjcduBqGpvNZBdSfGDz3iSwb02LQLILpEFyYM9hW-n8ye_Mog5N8TTEny6E_4wbmn04dgYU2fyZJ6RoevraCbt2_iormzDjkfwyHwn48VZhMKYQFm08QdVaymy2PHthp00p2xSgrulHS9tShLVCsf0WxciIbxzaFkxUVDSx6FCVn8Vz-sn06FsW6MLWkeaGtVmEK9vgtf8MxbznAmR2ckNwXG-IyJR7l36AZbwb0diBa8MNcMWQPspuSxOfW_CwkYALaLuLLvXzLuLKLw44J6IqgY2JVJ3FQuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=KZrLENEUl90O4vfHr9Bovm7JzIsk3k-z5QG6Swuds8ska8bw0RmYjcduBqGpvNZBdSfGDz3iSwb02LQLILpEFyYM9hW-n8ye_Mog5N8TTEny6E_4wbmn04dgYU2fyZJ6RoevraCbt2_iormzDjkfwyHwn48VZhMKYQFm08QdVaymy2PHthp00p2xSgrulHS9tShLVCsf0WxciIbxzaFkxUVDSx6FCVn8Vz-sn06FsW6MLWkeaGtVmEK9vgtf8MxbznAmR2ckNwXG-IyJR7l36AZbwb0diBa8MNcMWQPspuSxOfW_CwkYALaLuLLvXzLuLKLw44J6IqgY2JVJ3FQuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=FGeGkJW3-Ex0nUg-U833CNPMY1iuAP6I8CNUpFO7nQInLpds4Hx9nzq0X2MEAWpO5K1qyG6lSNq584gVLNlvEQtuBdGTWeI4Pb4Lw3PhrnNRJGJzPlbeQvBSD-5IttfCrY__BkOAyvdm-CEXX5-3wDozrYLj41q1VkUJTkqst-k_kQRfk_lAww3nm1XOIs5rHfbZz42cHSZp2GEIPPmZbr8G1dRNPuW10LdGA93OR2mkm1ldQOy5-6SOWXsA9jfAX21qScWkBBdAApSYuCKpzGl9MXrkjJShhNARpXgILb5ONpkGE56qDuMGU1i4v6dFix8nakJ0vl9ube5vaAXVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=FGeGkJW3-Ex0nUg-U833CNPMY1iuAP6I8CNUpFO7nQInLpds4Hx9nzq0X2MEAWpO5K1qyG6lSNq584gVLNlvEQtuBdGTWeI4Pb4Lw3PhrnNRJGJzPlbeQvBSD-5IttfCrY__BkOAyvdm-CEXX5-3wDozrYLj41q1VkUJTkqst-k_kQRfk_lAww3nm1XOIs5rHfbZz42cHSZp2GEIPPmZbr8G1dRNPuW10LdGA93OR2mkm1ldQOy5-6SOWXsA9jfAX21qScWkBBdAApSYuCKpzGl9MXrkjJShhNARpXgILb5ONpkGE56qDuMGU1i4v6dFix8nakJ0vl9ube5vaAXVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=LbdsBoI76csJJNXaTj8aUD5f-7-lq0NVNN2DSYwqA65gUoxAxNqlqqFA0jkRGLFXdbRqchRcuBBsH80rswE3N9GE1Z_v3YIW7eTiSTpPfkqAI7yJ2jSgtdj7yPgGdyYomyeZUJTsqFLBWpyzVex6-s1daNCFzuJ3K2q8Rlq9Q8Tcdx_Ix8i-14QminFip6CIVo3Jf5H07lbw8nn3IpDO1WFp-FARhbZkQTRWeScd-0EOVXnhZlIJAj9dx1c6w-OA1b8Jf_kij0G9mMoyRxCKyD8rb5L--hOIp01AJWrG__ESTKLEJW1w4SP9YnoukZQdqLJJDJSAyy6kMJD5XpGBew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=LbdsBoI76csJJNXaTj8aUD5f-7-lq0NVNN2DSYwqA65gUoxAxNqlqqFA0jkRGLFXdbRqchRcuBBsH80rswE3N9GE1Z_v3YIW7eTiSTpPfkqAI7yJ2jSgtdj7yPgGdyYomyeZUJTsqFLBWpyzVex6-s1daNCFzuJ3K2q8Rlq9Q8Tcdx_Ix8i-14QminFip6CIVo3Jf5H07lbw8nn3IpDO1WFp-FARhbZkQTRWeScd-0EOVXnhZlIJAj9dx1c6w-OA1b8Jf_kij0G9mMoyRxCKyD8rb5L--hOIp01AJWrG__ESTKLEJW1w4SP9YnoukZQdqLJJDJSAyy6kMJD5XpGBew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=W9S3EzPKK-fKIPC-trrehcqGLAD1Rae5JyXumeJnzW5jKN-ruhXdxaFmddgkxIJDksJtU6-mM-ELCSCO77efKAhs9lsLNrAK8Wzz2ob8Cwla9xrOHeAe_UQjf5ea2cvLLaqDg47csapYx88qbMdGUoaN49QxWLPRe5h7KETP_nF_6R8DZVtG-3-haRowtYLy4qvvywjimDPYLmUW0WBS70YcHmiOn_3ladpBlmLYSA_ZsB0_K4SCc0_tnGeA1SUaByLOWtO_zWoS57uWBo2Ku3doYzvu9WtuZPdXxHKQXMT8NB8ZgyZo6EeIbiAHfSvZWgMvX_L94KJHDO-zV6m7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=W9S3EzPKK-fKIPC-trrehcqGLAD1Rae5JyXumeJnzW5jKN-ruhXdxaFmddgkxIJDksJtU6-mM-ELCSCO77efKAhs9lsLNrAK8Wzz2ob8Cwla9xrOHeAe_UQjf5ea2cvLLaqDg47csapYx88qbMdGUoaN49QxWLPRe5h7KETP_nF_6R8DZVtG-3-haRowtYLy4qvvywjimDPYLmUW0WBS70YcHmiOn_3ladpBlmLYSA_ZsB0_K4SCc0_tnGeA1SUaByLOWtO_zWoS57uWBo2Ku3doYzvu9WtuZPdXxHKQXMT8NB8ZgyZo6EeIbiAHfSvZWgMvX_L94KJHDO-zV6m7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyn2EJFAIcNcZmuXvXf29Vt6Enk0Fww6ZCBR9eZtznJ_5pbIioXFCQgjUuitVzLSBjH9ag4yoQPZXCTf14xZMOF-t4zlbWULxTxODMTy7TPG5Ii5-46HTLqHi1XHd5JZD8xeZ5F8h6b7s6uRvSJY_yZBczF2pCb-HRkSswsiPtGpF3L6oDEv37UZ_N-PsIeqbdmW-NTbIxVu_f7rwWZXYJ1g-0FoYEt6LAM8qtsvn2V5qcz3K95m4UHhV1w6edoE5sxgvLg25Y8Yiedsny1F2DYnZCx9ondzQJqsT2LyJnTr7VfvqvIc4RKoywYHJ8RudAMmzLBnz0hbA_nuB_GA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtGH9_yF_Ch8cOSf-6KT__OCoXFloyOLlkR9BBipoKt5TsPFiELHGSj6N4Tn80drZBIlfAkuUvsYAE4d44ase_IY2pLeOJwEWvSt4vxYMBodnj8AqJOzmlGavIodNAtJhFmEvhjUhLbGI8aQ128oa8RVEmz_UyNnJFAHVCUeB_ToK7FmmZgly2bTwQzR3RwukswnrJWrr4DW8ZW5YC9_lNMgWgKd5lmVurSBsD1oShDFNUW6pXc3yPS3l_lKqrQY3o9QvNMges99Df0x2yMDwziGXnNK4XuQ9PdokUk1A-bYbNfnqC_yNNqA1UaN5FjjC2AmClrQB2pGx0tLvF77xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvlvdBw9yy83M1esJ55CvsZ9fExymfMUZNHiTJW4rFFKLYw_LBQIyxJOlNcoeOZ7P7TDIm4Yj8eDcLCY1Mxv2sQNATBUxR3kwMnt5PNBBQIg2e5va5oyYe6SWIcrnefm9rXHBiGaRvuk-KcJuepEzWT0AkK673M8LG6hDgiEvmPtTO2B7Qjl6veOW6Vfaz35bHFvLIq8DmfPrd3llBS6F5HUd6K_Nw3eB8TWV43H56UlvlrA0YcIoKxabFliVlsPvFOoclvyNXNkNNXcyt68IX6J20nrgiM3Mim4slni8MEhAC1gtjw8UufcMRlujIRKJ9_mGDBENSxmjl3heLkUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTTn69glh0FWUMFiy7QLO1KG_wbe6NUTkJR3tXna-AZwtFXoZUbyCsGlQBNAuejnwrGZSBPUDe25fjgkF2sLLQuBps59iFbEWR4j1Rq9GCcYXKkZ0NRk2WuwC4_ulhomTy0-YU2kC7xv9VSP_Nvxcp7FMHOx24C4HtpnDI2DOoMHpYwYgvbxvvPDUoQpC3JtZEiFbKQEFqO-0j3L5zG4gtY16WtdQmo8IDcjrz0Kc_Q02jTBCMYxLJIabMVB_Kv6LhAbGajmLEJb8XQOQ4HJFgxUc9Fe1VQV2BSztQeIS3k3FlAXpZiQPAR9i__TW456yivdt7uaMWTyiqAmNkNrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=nFTZkVzFDiJMd0VYGBe3_c50RS1nuapzcXma693jXQ4mI9XGzsomyK120BzFTv9a7h3oWMzlcyy_qW9KNmRKEXcv1n3mAbNJab92px_W9cZtYFICdKpcFsWFVO2yDukjF-EfABs6dx458Z9OPcWcbwvYXG80bWX56UlCcKaeggEUqR2rH57IZXqlS52lelJJWtyMhVDXKMBwF5Eu6s5Rp-9-CmVkk8JCTtoD94BDyjELJR7E165_eU3XVJVfyY8JOvRlPyDRNXmG92dvThcaqmddxInQG2UIXJ2HOaSG5xPqm8Tvx7zorQyAKhPSSTiSQPlKpfmfV5ZWG8P3b5ZzvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=nFTZkVzFDiJMd0VYGBe3_c50RS1nuapzcXma693jXQ4mI9XGzsomyK120BzFTv9a7h3oWMzlcyy_qW9KNmRKEXcv1n3mAbNJab92px_W9cZtYFICdKpcFsWFVO2yDukjF-EfABs6dx458Z9OPcWcbwvYXG80bWX56UlCcKaeggEUqR2rH57IZXqlS52lelJJWtyMhVDXKMBwF5Eu6s5Rp-9-CmVkk8JCTtoD94BDyjELJR7E165_eU3XVJVfyY8JOvRlPyDRNXmG92dvThcaqmddxInQG2UIXJ2HOaSG5xPqm8Tvx7zorQyAKhPSSTiSQPlKpfmfV5ZWG8P3b5ZzvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=TS5-VFtkI9jrqDg7NhDZyLWE_i-v8dBKCymPVt16Uu7_A91hZNKSLah0UDhqU7ACM1EZDkBCoQsXuvCZalU2vdPZGzt7GxqEplTtJUwnjiFM-di2vF_FplrPI2qKqoSakNw67SCD4w-hkpkwu8LNbotYP9q2eYiQVJawzQKmCaVKTccP7WhZstrMQYBnn5T5gj7eKGZh61aF3ny1HLgS8D9wBHj38hwVpAPwinJhKezrWITI7nKhrNlM3EMDjm79MXjmtu_S_q_utUry9AN9uyA64CpO6wxpKa8tUPzmjXRpFgTA6ESFu6Sj7dcx5B-j7NHA8aaPxLjM35AdW4yW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=TS5-VFtkI9jrqDg7NhDZyLWE_i-v8dBKCymPVt16Uu7_A91hZNKSLah0UDhqU7ACM1EZDkBCoQsXuvCZalU2vdPZGzt7GxqEplTtJUwnjiFM-di2vF_FplrPI2qKqoSakNw67SCD4w-hkpkwu8LNbotYP9q2eYiQVJawzQKmCaVKTccP7WhZstrMQYBnn5T5gj7eKGZh61aF3ny1HLgS8D9wBHj38hwVpAPwinJhKezrWITI7nKhrNlM3EMDjm79MXjmtu_S_q_utUry9AN9uyA64CpO6wxpKa8tUPzmjXRpFgTA6ESFu6Sj7dcx5B-j7NHA8aaPxLjM35AdW4yW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=k8iNzULD4gB_Z_21N2h6CRGSQLFjyabPom-G_tkx0IgusNmt8c2MxjwUxNJet5mOxzRtrH4eA2jJX_Q6WU-3MB_Z_L5AK3Ad8ZtzKDCqRaOavpf13TxjgcQynLRbkECO8brMpxvHyHV18sW8eNgjT5CVH3ZtbPr8453XdLmuwVP1jTT0EC25Rbj7vIGjns25_5qNG8PwGakuP0CKi29loSiz2KsMc3U1bh6mMbO_hmfJFbAV5GPu8huqoRsWegyWC3XvBlw9EI9zVhZjv1w-G9eACqZqryOwOoUFGMQsaJzLT397-BS-udguRIWGLBln8hOmcUh90HqgxfsrhBcD7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=k8iNzULD4gB_Z_21N2h6CRGSQLFjyabPom-G_tkx0IgusNmt8c2MxjwUxNJet5mOxzRtrH4eA2jJX_Q6WU-3MB_Z_L5AK3Ad8ZtzKDCqRaOavpf13TxjgcQynLRbkECO8brMpxvHyHV18sW8eNgjT5CVH3ZtbPr8453XdLmuwVP1jTT0EC25Rbj7vIGjns25_5qNG8PwGakuP0CKi29loSiz2KsMc3U1bh6mMbO_hmfJFbAV5GPu8huqoRsWegyWC3XvBlw9EI9zVhZjv1w-G9eACqZqryOwOoUFGMQsaJzLT397-BS-udguRIWGLBln8hOmcUh90HqgxfsrhBcD7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPIFqKv9f4U16KMMpPUwk7-iAG4eSwsb_7YsNn2gjBrD6kPZ1JG8BXSDhj2gsxEvxJavT_9gw20ad4AJCyc_MyOtlrT2iFpK0zRbWleeDwDSXXAZlxbvnl8qmKNX4hW1S0RT7KgIjGMJGXaHvk9Vh_W0_7JtvP-ogU1PIkTfN9OW1SL1TV4ZfqE4HX2FUVfCwLHmxyxCHE6MTD2xTZ0zJTLLB5lqf57kYVo7uN6Z5MAU-AQsywVXc8dQqUgFKATwSPIb1bAkIthIRreDa4EhHvhjnuzN81mt1LKNHjezp7coSmDmDcX_9TYv-GbRnPcA1zLeKJ0l1XWj0jOW246uYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=NQ72hex4Hcu-67vBWRq6TC9QCzljPG-wPO0O3dADCmE-SevIT6p1cZVPhOM9puMN7TKz69I7XqFNl-E4KDeS4qaR56U8MFkLlHb7xqH1FhjKr5rkgPmPB13ODPVxwHzD9pS4leJvM2SF_kXMA9jGGs87RMFwnrn1TrS-1cqzZw8DuBf_ADsZ93oNP_25-q2WeWsy4KiJ9gqXx2cdL1JF3YgHdaO38SY4zIaxeZDFZBRaY0BFwVvmgIoXwkwpxYNZz051UG-Je22xexQERLGx7RzzD5z5QCRckRs5eA4-1fssYFjBrPo46tFuUyeb0Swtlkx3_ywBVRcTwWyevO185g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=NQ72hex4Hcu-67vBWRq6TC9QCzljPG-wPO0O3dADCmE-SevIT6p1cZVPhOM9puMN7TKz69I7XqFNl-E4KDeS4qaR56U8MFkLlHb7xqH1FhjKr5rkgPmPB13ODPVxwHzD9pS4leJvM2SF_kXMA9jGGs87RMFwnrn1TrS-1cqzZw8DuBf_ADsZ93oNP_25-q2WeWsy4KiJ9gqXx2cdL1JF3YgHdaO38SY4zIaxeZDFZBRaY0BFwVvmgIoXwkwpxYNZz051UG-Je22xexQERLGx7RzzD5z5QCRckRs5eA4-1fssYFjBrPo46tFuUyeb0Swtlkx3_ywBVRcTwWyevO185g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=q8VaIEQjtgiZ2eHOHemi9e2BPdxZ8K-uzL6nOESkrOK0rzRyOFqrX60c5IoNli7hFtLF6XeU3jmr4dfbbM0C4PLEUDKZix-uTWX9JAQVP0PblzeZcor5O2DpSug7Fgk4XkOlKox5Vij0RAhHym1IsVIiUazET1YdG6hwtbGmJLwy6HBmlQ72dP3eXvtV2qR7s0UcSdnGlq_-kux5jhoJx6TeuGVWDNVCTGlwhGz_IcKh1n106Z8KDehXyrg88QzBHJSSgKQu4nW7pl6bkAnmeyFXLwlM5xI7ZF2J7Ad_2pVFUJDSsJPdv7zYqCYYCKauBAAX14_XczSdiHu2ECE6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=q8VaIEQjtgiZ2eHOHemi9e2BPdxZ8K-uzL6nOESkrOK0rzRyOFqrX60c5IoNli7hFtLF6XeU3jmr4dfbbM0C4PLEUDKZix-uTWX9JAQVP0PblzeZcor5O2DpSug7Fgk4XkOlKox5Vij0RAhHym1IsVIiUazET1YdG6hwtbGmJLwy6HBmlQ72dP3eXvtV2qR7s0UcSdnGlq_-kux5jhoJx6TeuGVWDNVCTGlwhGz_IcKh1n106Z8KDehXyrg88QzBHJSSgKQu4nW7pl6bkAnmeyFXLwlM5xI7ZF2J7Ad_2pVFUJDSsJPdv7zYqCYYCKauBAAX14_XczSdiHu2ECE6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLe1gIKdDYYFMUVoyquAMHWxDgGvlHax2kcEyikpBOKbNseFWZ9TRMUpxYiR3kIRIM13oihDmi3P2lJ8r0cACiTSZSGALFNycTx7WiTPQtOsEGVMV5aLt0WNsVPnA7LFFqrUx6I6ruaE5uXFEld291WDnHgRqgGNWzKdp8TK7QSgmBMrTD1kkbuGZ1yfWu7VBFBOrisO5ynThKVGD2qra6jgsl_VGsETTnZkBLym5C3tKfNyw2789WFI6NWo6EcLk-jgxjCLNve_fQpd_6IzC8kOoNqtypKo5Lo1WngP118e6F4iwV0eXdoU0Utmn4N21qF_ozq3F0GVgZ5gkB4tQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=avT3p4IEvidHYtg34x80GmDVXPyAGsgNY6c613CrJc7sOSqiHP0Rgk9SwzlO3ViCP0gJsj4ZgewUvh8aoHrwvmF4aVbOCPAOTImQEWS1mZHuSAZvF5m03AFKJW8XxbWNG0trGB2ulWLKS67n2w6OVWwMDOTcqfXSZ520RLcZdJJsglhYa6GiPOHFiCsnRkEOfsVKZio-jAANXHSdmTwwQ9NF7wBnv8FIeHJKoSMRQV4ddzRVEOQwBoYEL6qAwXKl3C2hUROF-1JflOaygW06SS9IyDSWytNupxTGCbxKoBUu_KXnMogubcZ5cQi9eIsdaKvdyBtn_MkNBjgZhtaNxZI6oZwbY_EOS8Sy7kWT8T9ds1Bo6Je20kB1c0qqq9dWaRq-RZ8GJGD23AkQGjIhL04zhLb3hohaFDDbskzystLxIJP3TVqhEDpE2H5T2KrzRZlkKbz0e9MgXfB8ufkvkSZww2UEKdlA9kv0n70e1nqt7oWwTTAD5BT7CiMpxwOnTsBRwZB_TvIlvjzu6sLl7U3YNAOpFJe46kcrmuoRRc7lXIPwcw8duGqFTqb4BlrGbET80GkrA-fN2zXX1_HZB2aFj_o0GegV9w53q-ilsxBiHHzX2fQFHPBihG5owGmiodg0l-bagoDjcmUrQbS5qqxTOtWRr4pAxSDCwH2nFAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=avT3p4IEvidHYtg34x80GmDVXPyAGsgNY6c613CrJc7sOSqiHP0Rgk9SwzlO3ViCP0gJsj4ZgewUvh8aoHrwvmF4aVbOCPAOTImQEWS1mZHuSAZvF5m03AFKJW8XxbWNG0trGB2ulWLKS67n2w6OVWwMDOTcqfXSZ520RLcZdJJsglhYa6GiPOHFiCsnRkEOfsVKZio-jAANXHSdmTwwQ9NF7wBnv8FIeHJKoSMRQV4ddzRVEOQwBoYEL6qAwXKl3C2hUROF-1JflOaygW06SS9IyDSWytNupxTGCbxKoBUu_KXnMogubcZ5cQi9eIsdaKvdyBtn_MkNBjgZhtaNxZI6oZwbY_EOS8Sy7kWT8T9ds1Bo6Je20kB1c0qqq9dWaRq-RZ8GJGD23AkQGjIhL04zhLb3hohaFDDbskzystLxIJP3TVqhEDpE2H5T2KrzRZlkKbz0e9MgXfB8ufkvkSZww2UEKdlA9kv0n70e1nqt7oWwTTAD5BT7CiMpxwOnTsBRwZB_TvIlvjzu6sLl7U3YNAOpFJe46kcrmuoRRc7lXIPwcw8duGqFTqb4BlrGbET80GkrA-fN2zXX1_HZB2aFj_o0GegV9w53q-ilsxBiHHzX2fQFHPBihG5owGmiodg0l-bagoDjcmUrQbS5qqxTOtWRr4pAxSDCwH2nFAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=l2layl9izy0LTCPJnPh6fQdfAJFpK5T7_hqFWQaaX6hYoc87qdzY77LZzVS1VRxMkcsJ8JMkM_Eg5I05-V0y_cadetsGGUD_mcvfDd8VpN_NHJayzty5sTDvifd9yxywYa4Y_MvXHYJkDNreaJw4WoTFiNLb2Os_aM7aPER4U7Lm5AtRfX2DjrUk7gtZmoTh3LmFdmJqA4_9JcQgZa_56D7xZ8PzO6I8gBtumIETXAzJmCANQwRGVxpwqeMPWP_WmN5P30CZDHsJT3FkXZh1UuVv57Bo5mgaaFQn5_mHq-FHc_gZb5kD48QVmg9kbiLrfYzS1blkTQN4Y_5Ao82weoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=l2layl9izy0LTCPJnPh6fQdfAJFpK5T7_hqFWQaaX6hYoc87qdzY77LZzVS1VRxMkcsJ8JMkM_Eg5I05-V0y_cadetsGGUD_mcvfDd8VpN_NHJayzty5sTDvifd9yxywYa4Y_MvXHYJkDNreaJw4WoTFiNLb2Os_aM7aPER4U7Lm5AtRfX2DjrUk7gtZmoTh3LmFdmJqA4_9JcQgZa_56D7xZ8PzO6I8gBtumIETXAzJmCANQwRGVxpwqeMPWP_WmN5P30CZDHsJT3FkXZh1UuVv57Bo5mgaaFQn5_mHq-FHc_gZb5kD48QVmg9kbiLrfYzS1blkTQN4Y_5Ao82weoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=K1FBMfbzkT3sPHvYUGgO14MM4MbOBTlQJaex2k1pa4L1H_jx4UX2rIWybXyCWPQtAu5FpnS0J_yy2O62z_nVjXhTS-DA9vCSCMZii35GBncpHyd0q9Aae306_kQbJoQMQKgwYZezopzfCpBYFV4oM67j7SekzrPfw3bquQaIymoc0LDhGNf1bzPefuhZRc5AGJhUhKMUncrK3urgBTp759MpfCQxM5uB6CKGmHV6r_3AEpY0hQQdUtnsIfZWYGsHi42PPX3BxDZxv1HBz0ZfnRGqy78mygcd1qr1o6I7exvfKAJUduXYTbV8IOyp8IIR-5lQcKhpAFVboORnkuO8QmQYre9ArgQDFVKJub82oTV0gWYPBpIP58pwNB60nOs9uztIHgYX_E_tJErxvSaYJaSTHUELmG16WZV-7jZ4cEf_uznNwd2Z7cKMp6ecl3bubjiYvETYabZkoeGPTyuPQORPDXdHa5CDIvvHaJbfiC5iWEjR3QeOJD5t7ToyzH5gjYdqDNGsUSWUTTZkvLp9Ys30lMj5SSCpjjklCxZQH8wyolN5oxqYpT7dTkHNUAOvh89NWHekDtEo-mMCJSRGjwmHyfO2MBA-oyK1vj2mQml8mYO0WngQcGxAwNYLF-lt-VAHfR9mzNpTrFw6s37WkBONDk7Yj6CjWho8Cw7sEV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=K1FBMfbzkT3sPHvYUGgO14MM4MbOBTlQJaex2k1pa4L1H_jx4UX2rIWybXyCWPQtAu5FpnS0J_yy2O62z_nVjXhTS-DA9vCSCMZii35GBncpHyd0q9Aae306_kQbJoQMQKgwYZezopzfCpBYFV4oM67j7SekzrPfw3bquQaIymoc0LDhGNf1bzPefuhZRc5AGJhUhKMUncrK3urgBTp759MpfCQxM5uB6CKGmHV6r_3AEpY0hQQdUtnsIfZWYGsHi42PPX3BxDZxv1HBz0ZfnRGqy78mygcd1qr1o6I7exvfKAJUduXYTbV8IOyp8IIR-5lQcKhpAFVboORnkuO8QmQYre9ArgQDFVKJub82oTV0gWYPBpIP58pwNB60nOs9uztIHgYX_E_tJErxvSaYJaSTHUELmG16WZV-7jZ4cEf_uznNwd2Z7cKMp6ecl3bubjiYvETYabZkoeGPTyuPQORPDXdHa5CDIvvHaJbfiC5iWEjR3QeOJD5t7ToyzH5gjYdqDNGsUSWUTTZkvLp9Ys30lMj5SSCpjjklCxZQH8wyolN5oxqYpT7dTkHNUAOvh89NWHekDtEo-mMCJSRGjwmHyfO2MBA-oyK1vj2mQml8mYO0WngQcGxAwNYLF-lt-VAHfR9mzNpTrFw6s37WkBONDk7Yj6CjWho8Cw7sEV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=uO1sxaAQjmIT3nnOBUDveJ5AbhoxMBjMOAPKrfcdXTBinjsY3Z639bHC6sLJbrSfxq4fKEeJ5Tbd1xsRJlgbo46a9LiUSkH6OFsvMpJMlALh21-wQ0oej6jWY7zXFKRgWO_PZMLG9BrgcOSubE7YmlHhGRhyx8puuURgplJkFJxYgDg58h7UnpMfkinlY8BJraP4yM22aTDBheqj00YbNtxS1acLmEzEDSBVd26a6q0hATcDiBzI5RBdizuDpQzGt9p_IeHivqw9oVIlKaKvO5E-UMO2WaO_CM8-gEVb8XaYNg7cfB2r9ABWDh1KKuMk_egafhLcYVV-RXibm6-ASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=uO1sxaAQjmIT3nnOBUDveJ5AbhoxMBjMOAPKrfcdXTBinjsY3Z639bHC6sLJbrSfxq4fKEeJ5Tbd1xsRJlgbo46a9LiUSkH6OFsvMpJMlALh21-wQ0oej6jWY7zXFKRgWO_PZMLG9BrgcOSubE7YmlHhGRhyx8puuURgplJkFJxYgDg58h7UnpMfkinlY8BJraP4yM22aTDBheqj00YbNtxS1acLmEzEDSBVd26a6q0hATcDiBzI5RBdizuDpQzGt9p_IeHivqw9oVIlKaKvO5E-UMO2WaO_CM8-gEVb8XaYNg7cfB2r9ABWDh1KKuMk_egafhLcYVV-RXibm6-ASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=gRbHb8bDHDR4hHyL9neymlPOUtLOXUtpQiIa5GOOFA4LpiOq-pZfvrhUa8fVlQtafQiNuKbb5zPVdrk0rrO0k6H7rf1tZGLiHT3XIhrLj2d3UX4sRefTObUp7ouMDGpbtO8uu2r0-FPUkT__VldQkcKgVYdVOrazr2PXZf1P2qGkIVio0YDesYA3x82JtAQ3xNLnMbdQ2M8_dbGwSzmF4H1AgHvxN4Tt_k3pXea8S5iBGWSLl5qaosjhhMEaQ-xjYQllbu10PtQidiPpYLPfWv4LFU0B2vuBTA__IITf5jWdRHKZNk5-LAf1XauU0kX1jjHV90TD0r2l3w6v-O2zyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=gRbHb8bDHDR4hHyL9neymlPOUtLOXUtpQiIa5GOOFA4LpiOq-pZfvrhUa8fVlQtafQiNuKbb5zPVdrk0rrO0k6H7rf1tZGLiHT3XIhrLj2d3UX4sRefTObUp7ouMDGpbtO8uu2r0-FPUkT__VldQkcKgVYdVOrazr2PXZf1P2qGkIVio0YDesYA3x82JtAQ3xNLnMbdQ2M8_dbGwSzmF4H1AgHvxN4Tt_k3pXea8S5iBGWSLl5qaosjhhMEaQ-xjYQllbu10PtQidiPpYLPfWv4LFU0B2vuBTA__IITf5jWdRHKZNk5-LAf1XauU0kX1jjHV90TD0r2l3w6v-O2zyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=d9vjsVUx5EDCZiu2OaX4mx9ItxRMKbyUQ_nboxAPbHKIMD-wvCFf0eGruQObHjC37Si6uhVaSMBkz9t6VG9vHIWjqIkStW4Iwmq5-6Sxbm8wwP4q2RyWLTSs73TEFeUW6dYxU8dUQXNyDVVJ1WRnpzxo2niOjIvbNzD_M9xiwx35JGC4t3oGuzGKRzEjUs19vhuqK2P0VD9RqMSRy5gesywZyVM99g_b-C5AjohvcxdVjwPNBrfqAECjq19ZtU3suP_piYyzIhTwPnPIPRPIpaveLJe7L0zc6smfGJvUmcmojP0uT_4HCuBpaxD9hDPhrxtM3Jv54Ef-pqdOy0gRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=d9vjsVUx5EDCZiu2OaX4mx9ItxRMKbyUQ_nboxAPbHKIMD-wvCFf0eGruQObHjC37Si6uhVaSMBkz9t6VG9vHIWjqIkStW4Iwmq5-6Sxbm8wwP4q2RyWLTSs73TEFeUW6dYxU8dUQXNyDVVJ1WRnpzxo2niOjIvbNzD_M9xiwx35JGC4t3oGuzGKRzEjUs19vhuqK2P0VD9RqMSRy5gesywZyVM99g_b-C5AjohvcxdVjwPNBrfqAECjq19ZtU3suP_piYyzIhTwPnPIPRPIpaveLJe7L0zc6smfGJvUmcmojP0uT_4HCuBpaxD9hDPhrxtM3Jv54Ef-pqdOy0gRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=qcp4AARb6ZszpTzWi6CaTOp9vtMB9MD7G0S9MYzt6EyeOcE4sCawm9_tNQBt6uoXHa-Ivz-94ra_gq7hF39SKrvVhS7bliD0OcuOG38eZR2HjBLi_u4wM_R1LO4FjRlsm-N_ug3YEZ-aCW8yYF0cEaZYZDW7ki8S_Rmxsg9yRsMCw2EojdEwveqxNVxD7LLAyOYHp1gb3WuwP9F16nkTdhICm0ni7agPoFc11ZzIA6ha8Vgi4j1ocnpTXvBJCBjl3JIS3gp1AUTisZHcAK4dElb5Q2wV6TM2I-cz4vpg3IpCPtc08qeW8N5jPeZKAsB5MPogKNAaxcqiBusVpcHLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=qcp4AARb6ZszpTzWi6CaTOp9vtMB9MD7G0S9MYzt6EyeOcE4sCawm9_tNQBt6uoXHa-Ivz-94ra_gq7hF39SKrvVhS7bliD0OcuOG38eZR2HjBLi_u4wM_R1LO4FjRlsm-N_ug3YEZ-aCW8yYF0cEaZYZDW7ki8S_Rmxsg9yRsMCw2EojdEwveqxNVxD7LLAyOYHp1gb3WuwP9F16nkTdhICm0ni7agPoFc11ZzIA6ha8Vgi4j1ocnpTXvBJCBjl3JIS3gp1AUTisZHcAK4dElb5Q2wV6TM2I-cz4vpg3IpCPtc08qeW8N5jPeZKAsB5MPogKNAaxcqiBusVpcHLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=KgM6-2i5mxqywhr7V172KsOAGXbZZjErOUljde9BVrGiyTJs88Z695wpOK9gfuNsl7A7-pC94FYDSbAF86HSsy5-ER5g9uUpDm-AdNEL4gnpc2sQUVH_e-RSLFR6B-hkOsUJkUCC_8DlMcvema5RjAepiG-Bkpm0Hpvi0LpyJ-oAPNKJ1mFHe9CDDuQXuWbCF1aOEjyQbWBj0mzKnOhjt0nhAmL2jvFQsJvxHjGH-_7XXn_VmY70P_R4fT_zVswkNLFKyJQyqAeBUyjU089JawA7O8ez47yCGm7EO1_umvKE5QiftZmk2QIY9jVUZ837qtNo8Iul9z490YXFphj4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=KgM6-2i5mxqywhr7V172KsOAGXbZZjErOUljde9BVrGiyTJs88Z695wpOK9gfuNsl7A7-pC94FYDSbAF86HSsy5-ER5g9uUpDm-AdNEL4gnpc2sQUVH_e-RSLFR6B-hkOsUJkUCC_8DlMcvema5RjAepiG-Bkpm0Hpvi0LpyJ-oAPNKJ1mFHe9CDDuQXuWbCF1aOEjyQbWBj0mzKnOhjt0nhAmL2jvFQsJvxHjGH-_7XXn_VmY70P_R4fT_zVswkNLFKyJQyqAeBUyjU089JawA7O8ez47yCGm7EO1_umvKE5QiftZmk2QIY9jVUZ837qtNo8Iul9z490YXFphj4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcUC0LgraNrOnqxQX4UvIn-gmSbxtibw3oSM9a9fbHmOdTmN_2POaBtLuRqzuiKw-z3gsMTswIWXDIPsHcxLv66V_EJnQylte-B4kob4wGSni7kV55-AewIv0Ozl2RKfWj9J0-o77oTPY_Jo4AB7DCx3GOX2rrtkOsGjBkXyxxOvS-kOSQ9MYb7i-ZKhVtdLc8UJ96gF76Jskf3SIMi6Qmi_f8y5jOv3AI_OsodWKX4VK7xVpIyAoOSYmWvWHT1FdLvdD-P7xRDJa8r7Jz9cggFVvtPGalKZf0BXE4AJpMIbJixCWumwKcRW961f7DTgCN-VHCtJlEDbkgjGw6g7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=p6ScDE6UF4AhuhYW77BwBdHjZS8Y5-9uDjdBvcpK9a79MoXMu_VVrjCTjDMnwn1oZLz_WDhOoi_V7Gkoh40t4LntNd2KAR2Rgq1zrCqyPqirgs6Yg97A3oiHc9_1BjT31maMAgwgrvIXSdEvkxsWPxongZ_ge2FpoQWKRQBdnR7imqF0R5x2yPU7OXQEkr9EtgZZrUh-a1rw5v9q7PqrEa8HYUIZ0yzgcCZRu0fVm0pLhCr4sR6Ljr18NCAnKMlLO9H_dB1-jcXrxoNQtqmWq4X7e123veWpT2yLi4lrhSbv-8Rz0Z-ZhRlrm7XjPPjRxRT4eBJG2qF9WjwoSjEQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=p6ScDE6UF4AhuhYW77BwBdHjZS8Y5-9uDjdBvcpK9a79MoXMu_VVrjCTjDMnwn1oZLz_WDhOoi_V7Gkoh40t4LntNd2KAR2Rgq1zrCqyPqirgs6Yg97A3oiHc9_1BjT31maMAgwgrvIXSdEvkxsWPxongZ_ge2FpoQWKRQBdnR7imqF0R5x2yPU7OXQEkr9EtgZZrUh-a1rw5v9q7PqrEa8HYUIZ0yzgcCZRu0fVm0pLhCr4sR6Ljr18NCAnKMlLO9H_dB1-jcXrxoNQtqmWq4X7e123veWpT2yLi4lrhSbv-8Rz0Z-ZhRlrm7XjPPjRxRT4eBJG2qF9WjwoSjEQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtdZDWxv3viQlGpHTdQrBCmHeMv_kLpQSdQeBspSzE7Lh93y01jBpbpmM8NlrjGsdVR8Ip14Q36IyJuAIqPdX-HrGcHyod5RgNajRhNVkw_aUWsUK1pPOxtNoZkskxLKwB6GwYD5NZ4w6c8EYdeP7AFKycB4tEUkP7qQOq7SvipgGzKCeh9YyX7hY0gbIN8k6YeQm6aNYoNNgG4whfKZ46g57V-ZSl-DlYl4Td6AvJMMCrvw56rghVRt2CPEmApZeUObPrLTcKV-tBg7IeH5BvzMODs52-fUS1mfiJy_klrGlMsC3E_UgB9pMoq8ufLHeQDWAnc6jcHZuB9dK72qEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkgE--FJGtA-PBTnMUfIuIl7dRN-S3smy3SwYPEWryhFyICFQv5l2YklFZXG3D21CDKBdHN0M2hvKfXkE_ssw9Jm6SvMXgRFgdTBCKgBo5YhZZr2pn59VStP6cIqmrgpP0O3OzeiWK2hicWIFXIR7xwa89ls8ho7TixIDKPEPsGXEsvHzOWBcblKV5R3pfIVsJ6pWXYRxtLJAhF42klIyb9507BUVK09GH4G9jUnIGWGi6sJipg4GXUDetuau2eQjBNBviPtCOQETI57iszVtFWhk13om4OVg8lcrmYIJtaEIDr6KQt027ZNgKsu__wijDZO-9BzURTGoZUjHOm_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6m-RONVinXwuIkH0nO9cRFBTZP2LMOQ1-DVq5YxnXPvCHSlQ7aagjQgmcrs-u0YyIAYUDRfSnmYXcQrj-hIdxIvpZmAEMUx1VTddCc8iHAbaUjY6TYn1NgeUPTiwRz8156Ol8cliOKuhvaxN9HHk1sAePNJc9rFMtCndMrU_i8paEKI2_yFXmnd6FzWdk7VpYjabNsmndn9-yrwI6ux8R97xPCDywc9E2c-oMX9vxGnE6356f-9n8fQiid7WD7EIJlDnO670Mz2FxSISJuSYZ0TeOKTcsVBnT3xiMamkT6Z_oDTHFPkjMVyN-wQFrk7byZLDQEKyO2AXD68B9R8uuSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6m-RONVinXwuIkH0nO9cRFBTZP2LMOQ1-DVq5YxnXPvCHSlQ7aagjQgmcrs-u0YyIAYUDRfSnmYXcQrj-hIdxIvpZmAEMUx1VTddCc8iHAbaUjY6TYn1NgeUPTiwRz8156Ol8cliOKuhvaxN9HHk1sAePNJc9rFMtCndMrU_i8paEKI2_yFXmnd6FzWdk7VpYjabNsmndn9-yrwI6ux8R97xPCDywc9E2c-oMX9vxGnE6356f-9n8fQiid7WD7EIJlDnO670Mz2FxSISJuSYZ0TeOKTcsVBnT3xiMamkT6Z_oDTHFPkjMVyN-wQFrk7byZLDQEKyO2AXD68B9R8uuSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_7FLIx_1HqdnpRT69d0ZdaYh3EHWpneuM9sMxj5Xwee8va11_PRJ6xDEqqdzpu8Y25P_nH2Kr3u4_VaGltw7Qz7x_0y9EpaAeWs-USGJ8tLyIc270n5DLbXr8ZK3tPT_KD4r1Nt16D1WtF184UdPZxQFedmOSDMZ44PKFW8BiDFlLN4dmKgzZs680JkSOmNjR0Y3mbiazi7AJcaILRJ4sh6ptI1wao29YNLuIvzuLuNjmQ3JyoemaGtnJZvPOI6BUvT81Hu5bVkWlQvzURkJgEv6EAj3dxcI9Mg8NjwGhT9pEliDrFXBkPtJyDcAKe45RzgvnuR9mFDClYcx2fjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2D9xlyAaxdSosIJta3jUUbP0Sl9HLSk8ihtL3MrJ9WvC-AH4n0k4YC8EaqQTkebNgR_2p24nUITaygojRaqwekdj6vRjCH5se1xNPbJnvuP5qa4jRc833ealFi0LwsFAUN8wh8Gs-E8pStCnTuGfWsjGQnv-Y4P4QPwV02iEaz19wXTA9ynvK80CrO0f-cLWyXQ2dfXYmZ6IMU_KDF8sQ9imqzYC2Nurxit7dXjBRkVLwft6Kk0tksX6l2WKvMsiBfwWUPQcq7YJssM2Td59rpgDCIPDMpsITSfadH6A5PGUil8uxzPu8MwpLDVx1naA3mNTyb5qW-J2MHxBwREKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=Ej1kaByX-KIOgtEHsRwGuyzQQzluYPI22Lyb2Wmp7zt2ov5xwZBZsQ2u5vNTR91AwqXhPxIZEyT88HCoTootxRGYotIRTsp07y4tc67WcEQxRm9qPdva3UZhdHY-NGlcQiGtsFzX_-E6Dfe0K2Tr7VTgZRZA_ZN-4lackO1htdry-TxvTfgYdbq12HTbApfbe44oRBhoD6LCIuZZpY8usSAzqx_HRKvrDJaQYj9Lj9_3ICVZwXRdE6gAOobc9ZeqaNjEx-h9ahbcQTN91KIkXBUuphInsQw_H3M0XskRAj_AxFrg2E004yAPYy4pWSc2Aj53ClvPjrSPbl553miXbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=Ej1kaByX-KIOgtEHsRwGuyzQQzluYPI22Lyb2Wmp7zt2ov5xwZBZsQ2u5vNTR91AwqXhPxIZEyT88HCoTootxRGYotIRTsp07y4tc67WcEQxRm9qPdva3UZhdHY-NGlcQiGtsFzX_-E6Dfe0K2Tr7VTgZRZA_ZN-4lackO1htdry-TxvTfgYdbq12HTbApfbe44oRBhoD6LCIuZZpY8usSAzqx_HRKvrDJaQYj9Lj9_3ICVZwXRdE6gAOobc9ZeqaNjEx-h9ahbcQTN91KIkXBUuphInsQw_H3M0XskRAj_AxFrg2E004yAPYy4pWSc2Aj53ClvPjrSPbl553miXbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc2GIS3QAOxyQiyfP8kjCJKSUlaYFKfgrQugoX_WiuLV1s3A6aYjGEojvVMlX1Iuupg1wlop9oteLJS3EJ1DZqxnUphKBEyE2Puepa6xHrCf8quBR7l4lLza8JE6ujvVCViyrTAcVnmeFae61Nr93Kj7sQCp8Rui2_HRxtvXclia6NXqAiujLzZgr9vTuIIMd76qxswQzbY_nYJwwZJac5Cz5D5kGQJ0spI20b7rXZeODxQe503eBViKiTofm8q5RYrrOTXcUOglrLh2w4RtVmFYJUuTTwO5H5EIQ0Z0D8LH6yTRmD7XnMQO544KHqyl8nKZZR7tF-Q31H2we4OzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQkiq97okfzstJQ_K50MV1csXT_-4WHyHjVHWUjLy4b_XXD_RHvE7DXl2JPpA2b-Q3wvbOpWEQfhMWybtooIFW7xN_LSivOZm2utJSS-g_nSpbIW6zID9UvbKDmDoJRxd3-xWANI1b2NHzi9QLebx9_CXmQMIY_Cn7XNdYtrv7AnCADF7PKui4KazEmsFe3PFudYT7oOeo3OO0WvRTfe5LAN9Iby_lZ-Ybx8kD92FqqNwuhIt4r6MQz1TVXyZfUvSpt4HTjTORqVNjQFHgutcM7KvxvZKh2N7beGWdUYQ8sDD4K1_2PvKA5HxUM1WGM5tYLFYdX0TjLp1YNAikux1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=qCYMDKPVZfxQMaciCy8R9PZ77ZEBCUVH8GFFM5dcOzixG0Sw3RJzMgqBLJ_1cmjvsEvdJrspzMwbdjZcP2mH-MPLHIjt89odYfJf0lo-ri5zizRko-GMhmm0xp0-R7fyllO2V4bTNgsyOzGhY1RlGP5n6JX5yVVtyWd8v8RUgYf2ekfcV_bnA_B_QRCQ20kF-D-vmI2X5NDeiK6r_mTecaGvMWXL8BPy-JXtZaJguoWGIjIASurmlavqmzi-lFTXy_TPgVlz2cRnXV71ky6C9TkNtxrMCr2OBPPYPDD-qoLfHd_kW-hhSSg5lEbqu0dXQWFheR6AoQkZo16PGR4UIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=qCYMDKPVZfxQMaciCy8R9PZ77ZEBCUVH8GFFM5dcOzixG0Sw3RJzMgqBLJ_1cmjvsEvdJrspzMwbdjZcP2mH-MPLHIjt89odYfJf0lo-ri5zizRko-GMhmm0xp0-R7fyllO2V4bTNgsyOzGhY1RlGP5n6JX5yVVtyWd8v8RUgYf2ekfcV_bnA_B_QRCQ20kF-D-vmI2X5NDeiK6r_mTecaGvMWXL8BPy-JXtZaJguoWGIjIASurmlavqmzi-lFTXy_TPgVlz2cRnXV71ky6C9TkNtxrMCr2OBPPYPDD-qoLfHd_kW-hhSSg5lEbqu0dXQWFheR6AoQkZo16PGR4UIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s53KrA9ghFk1N4lMlAphYkI6aRqVCQJ_l5ptTop4cYOEc7k-61qgkAkvnqBbi2PGJWVIfDAEuIegVv7aWC5bApgsfVCVXvksOipxnu2KFVM-uXPhWFCKcaLR31pBNTu072OJRQ4OkvAkIo8lJW_C7Ptcd4wkUDGcHhl_r-6esMJjfN4pmJgvzKOR0sHwXGj7b4PN55wjOo4TUFsc8CYLGYOLZQJD9oPcRgOa2eLEq2REM0xhuM-jmRYPQ4DenqdqjBh5fdo7rtsPz5ut7sPj60zuvzH9ehVmBrnVTJsb07TNC1KNlx4h5jMX3MD7zZgbQBOOvOG_BvAtvRNqP05p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL0ctmTNNqBd-19y6c26AZ-AdTlN2HBCw3DQ3eA2D2OCfu8B9YVNDoZP0wYfOcckwSWK39-hN7k1nzk-aYNJ2KCEzaDKjXQy63Rc1gfTVGfuyCIybWbqnkO5VoXg9zvdagPj-OMv73IeI5UK8ZhZMxzsF5kg0hMd2aPzdNoAKTDeRP81oIKjUi-pJvFpXIkMOWXgnTsWe3iNi-TDyqQS2OI3gLoI8CKoAThrcuW7E4GbbdD-CFnFlA9LLvX-FSECivCnBqhOqGZ6QbjYJExpQk6z6Jw40XJdX9GvzoK8gdUnS17rJsD7A-Zd1yhZru_-vbegvkIPv9QU1FCGOYEbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6sjiok1M9ay9XToPTfN-_D9nMT3axp4xbuRZqMKGu0iMJaHoqNUfxufQ6gm8Ux4eGIL4A6ev22nXRm3kwy7Rp3JCTRGZb-mUinGjMgeqpr8qmgYYMGAtmjSEsJicQ0J-IqLDKNuRAvRMQ0qJk_TcQvMwXz63SJE5nMX6szlH5Oyy9-sjcelvoTZzqC3cwxt5Hok_WBlrFSildgv9-6m-YflZXZbEwlZYR8-j8Oilc4D_1ZDNwwzsCKKDMkgF1B8SUv7CYb0f4nFDcuaW5qCkMAXyw8BG3oMi1owQuCTCyZ4Bpfa46dCPxVg74w6EYqRjGZjwzs4AvYzhDX-xixogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BizQDhfGT0ukCiOafQQcuNaRIKjM6ub7XKjKMDg4lZXsqhD4z00HcGolEbuU-TRETLskYLniBhg4Irn_7RshPGnYyartsQ-KMZywVMGp2nAu8wfKSKaW0jYUz8Ig67sxJoP9LsM9gAGTCVyL5HN3L8T1Gnqq0yoSA0WPxJIwEHQqnFbUdFaVkR45BydwjCy8oiYKjevYt7Nk67KUvEEA8UBO6b9sB9LpFwF_pkOONFpEg9vydeqXXuLVqHkSlvAumys2N7t8LIjIA42NGSO9uAaI-PSnqfVNcFd_aAm6MQ-1uTPyRquWXntMECa8AHdrhr4FBq1iV6NVMherj19_4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=Gkfpa5jkDUs-eIW9_hEEQe_2SjS9AYbmCVYFkjydq0p9y2yWX5NRImiMSi6psHvWhDyiDtTSd6pSi5eFju1Uyx2KyOjugjIYKk7yoepdHnKLQzODIv6nAJ3bpk01H6WSD76ojnK7GCKP39Fk--NJvATC6iMPtdFqfnkhjpAw2Z-nbIiUXX1JZ5UuMEeJ5lL2qMmb_Mls63B37TOc3Rlpc51LQHeDS9zj7oTtzPWefBm6pD82kwtEqVtgtFiKr5oLxczRiD5CKPfi9BQ83_HcsPWyMRBRwfYQC4ljYFmPFBj-Duy2_Vo0S0zeQSJrMJ7sSLuAAfMj6b83U9JzmKKb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=Gkfpa5jkDUs-eIW9_hEEQe_2SjS9AYbmCVYFkjydq0p9y2yWX5NRImiMSi6psHvWhDyiDtTSd6pSi5eFju1Uyx2KyOjugjIYKk7yoepdHnKLQzODIv6nAJ3bpk01H6WSD76ojnK7GCKP39Fk--NJvATC6iMPtdFqfnkhjpAw2Z-nbIiUXX1JZ5UuMEeJ5lL2qMmb_Mls63B37TOc3Rlpc51LQHeDS9zj7oTtzPWefBm6pD82kwtEqVtgtFiKr5oLxczRiD5CKPfi9BQ83_HcsPWyMRBRwfYQC4ljYFmPFBj-Duy2_Vo0S0zeQSJrMJ7sSLuAAfMj6b83U9JzmKKb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xfx6FsoGzG6mp1PDDE0KrKS3dfj42s69vNJnk5lqwj6Pamo9zIWw9OV7cSwDpLsBZDJL_jtJZRPXsEaoTFc7p60Fm0GdVaUce4PItot_iDXYv0qIKgVRBgXFRsTYX4Y8kpKQ_FiO7_nN59z64zmy9PG6WnARN9QJ4zTWFXhQi6IGEd6-9qH1B3moYEGeys0l0oSD0F-gWeIqNgL-UgQOY8LqrOY5ioQM63aYN_yUGQCI_M1k7_31VwJiCrUzGc9EgXvDPsRH6ylGl6u0zQyvipMPoS4vdTS1NeyYmNb-RJvBqud_h3ejZdBCobrsmPjlRwhOmM2QI4B-NpTp7Tas2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=feUE6ENS8FMjWmVhrYylmLyYrIdnvIJoviyFv0Xcdmbi_42Oe0SsFLZ1nvU-LVOT5-OvODH7B-yOzv1dPJKfMuX_cQfVAxnNt3HhJhT2NEgQXCeKY5skHcQdz8oXiA3qopvSwz5pdAH-9r37i10xKbAb5BZa8omzQUwBhMUd0J6_GsC96QiiuAKZ3PEyJdj7ZtU6p-CjUNnyhktMTaGclR7B8YB8EOhPEMlvWe2YzXhhtyXdvjukZ2JY4UO1Jbc1fQK9Y4YQ5FLfbTUp3tBBGyqn3vsjmiuUkpTEQxS-gctbCHrC1VH-hYrEZjtowPMaAdRUN1z4RnBuEcTPGDleGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=feUE6ENS8FMjWmVhrYylmLyYrIdnvIJoviyFv0Xcdmbi_42Oe0SsFLZ1nvU-LVOT5-OvODH7B-yOzv1dPJKfMuX_cQfVAxnNt3HhJhT2NEgQXCeKY5skHcQdz8oXiA3qopvSwz5pdAH-9r37i10xKbAb5BZa8omzQUwBhMUd0J6_GsC96QiiuAKZ3PEyJdj7ZtU6p-CjUNnyhktMTaGclR7B8YB8EOhPEMlvWe2YzXhhtyXdvjukZ2JY4UO1Jbc1fQK9Y4YQ5FLfbTUp3tBBGyqn3vsjmiuUkpTEQxS-gctbCHrC1VH-hYrEZjtowPMaAdRUN1z4RnBuEcTPGDleGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=b7fyCpKMClWat_bsV4fIFhaBjjtSOcJopkPbGp0BVtfR1GYq0g91MDEMpl0N50z-4gsli7tHG3mP-l3I4EdE9McefowqlDjk9Qk9nTW4psEpM0Q3Y3kfHXkTHup0jDR_5fY7OwI1Op4UwxaZ0pS2hWh--0vmNBgKMgJF8oxwfsJ3UE4KgO34OBqgQ1IYbMnxj-rBPDoD5QfeFBj3CDDnC2j8HorwT-oZPwV4RMpZ40I99jlJ1R1mEch5D_8jJik_0_C7oHIpUBmvbBRfdK2tc3RRPC5FSCmSXQzyas933n2C-5KuDx9ul3W4iQg7YxoIUBmwk7croLnIfSCipSZHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=b7fyCpKMClWat_bsV4fIFhaBjjtSOcJopkPbGp0BVtfR1GYq0g91MDEMpl0N50z-4gsli7tHG3mP-l3I4EdE9McefowqlDjk9Qk9nTW4psEpM0Q3Y3kfHXkTHup0jDR_5fY7OwI1Op4UwxaZ0pS2hWh--0vmNBgKMgJF8oxwfsJ3UE4KgO34OBqgQ1IYbMnxj-rBPDoD5QfeFBj3CDDnC2j8HorwT-oZPwV4RMpZ40I99jlJ1R1mEch5D_8jJik_0_C7oHIpUBmvbBRfdK2tc3RRPC5FSCmSXQzyas933n2C-5KuDx9ul3W4iQg7YxoIUBmwk7croLnIfSCipSZHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=vowfoZzC14AUcINzxohYGS14w2LDxtGp13NSVV-2UGhRej4MyuSuj_0QX5L1wUG6eGI6c3l7hnuFOF9dJMaK1uIDDMChKRruTNbJNrLvzbpvW0JuMEoAagofktkHL65RduxfQ2K2FmIT6tEeRxjbuJx3ZABFLp9hXnELI54T4dsQg0kO9Eo2AtoeqJu1SKBkOFCPQRuL1ww-i75Hw4BUWpL6O5HGRr3YMnxl0typQGMV47Ent6dHox11FnAv3KIK5tixipwrLxzGxKCSojU1foMhE2SqU_s4bQhhOan2jpQp3THoSIDX8d3Z0IqdBwYGitWVWS2lWcJV1cy1BTJgPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=vowfoZzC14AUcINzxohYGS14w2LDxtGp13NSVV-2UGhRej4MyuSuj_0QX5L1wUG6eGI6c3l7hnuFOF9dJMaK1uIDDMChKRruTNbJNrLvzbpvW0JuMEoAagofktkHL65RduxfQ2K2FmIT6tEeRxjbuJx3ZABFLp9hXnELI54T4dsQg0kO9Eo2AtoeqJu1SKBkOFCPQRuL1ww-i75Hw4BUWpL6O5HGRr3YMnxl0typQGMV47Ent6dHox11FnAv3KIK5tixipwrLxzGxKCSojU1foMhE2SqU_s4bQhhOan2jpQp3THoSIDX8d3Z0IqdBwYGitWVWS2lWcJV1cy1BTJgPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
