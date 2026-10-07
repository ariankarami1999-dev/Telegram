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
<img src="https://cdn5.telesco.pe/file/n4rxAIpbi3a270GR_k1zoKXdIz3ujaV0dzUoEYW-anVbR6QjJl65uVGEdk6LbzkoLfEbYRdxKFxHUa_IcuhfNVflWoLbLu2rUNyfabDQMPaPRAOI6ej8tNVELaZe7s24YyMwkzUvFBxooNWFCsFQwI4JjhZHYJWlo9G1VnT1HRVDh-G-nLg7xjsizSY_cu7tMcdOpNCE9TropFn59btkKN69_L7eu0HeeXBQOTx3PDlDru8ke-wlr0QfJQh593kYGt_L0LqStJ_mJulKQipr7zTzpkmgIDRAsZo8h8gQ1cSWS8P5ypM9SkSZhhsDWlE0GCu3dgX4tVj4ACtnIaFALw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 389K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-108006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=IdL147opSF6ig21HCfV357RDfPS7KWwnSpOZ3o-eoWDDzaxaPDuPVR4BQcbXjDKPI5sd1Hogyg3Fan6D_DTAtVZfoUvLNd7FOvhWG3quwiuanLaSVjLe_nIYeBUPgeiKrzWdHUhLlOm-8P-mUzhH7cz4fGtWeTL7lBTD9yVR2LhefxEN1IwlwduLSchZ88nCL47ebG5mxp4QYkDBR0kKGXWuYCTpJYBhNTBXx5JFxcalYxhSBUZ60fhx1Fs8l641Nr__iW3jHblhLbEBqM72SqKRjEI0Kiyzcpoww_ns8fd-3YwL_tdHuqEjMCB5FNOI3QoXBKM6m4FXqNnoLHIdUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=IdL147opSF6ig21HCfV357RDfPS7KWwnSpOZ3o-eoWDDzaxaPDuPVR4BQcbXjDKPI5sd1Hogyg3Fan6D_DTAtVZfoUvLNd7FOvhWG3quwiuanLaSVjLe_nIYeBUPgeiKrzWdHUhLlOm-8P-mUzhH7cz4fGtWeTL7lBTD9yVR2LhefxEN1IwlwduLSchZ88nCL47ebG5mxp4QYkDBR0kKGXWuYCTpJYBhNTBXx5JFxcalYxhSBUZ60fhx1Fs8l641Nr__iW3jHblhLbEBqM72SqKRjEI0Kiyzcpoww_ns8fd-3YwL_tdHuqEjMCB5FNOI3QoXBKM6m4FXqNnoLHIdUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
کنایه ابوطالب‌حسینی به مصاحبه اخیر مربی تیم‌ملی: امیر خان ما رو بهمون پس بدین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/Futball180TV/108006" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR7jtsasLGPz0Ukj-ybERu4vFGvA1PqkEp4RdsW0mQH_q5uWDg1DKR9eg9QvCaogd1BEtM41rSo7JGFaHaBuCr62osu2CbOO4aoHMyZnYv-nOCnA9oI2CRWDFzVwmzidMyfQRn5vqam1YlHd_LCcM8Gr3KxE_-4zlr3SG-Yd9NCSecgk7Onc4GQh5lohxuyENGMdbZrRgmFy0xz8nwFnGbqKdEdh8WNv38XjPPPLTf0lsCVWiwzyEyBy9TNe0a9ONI2bpvGKpQf0PXsF3AVW9T7H-PCWGxtr_Gx0w4OlQ31GEp0nChNdvKZlv00XST9oTUMU_ljPTa3AzasTC55__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای بازی با تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/Futball180TV/108005" target="_blank">📅 12:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TZ9S4P5pNjCWiqC3kg58JUXkSlM-HGVEnvsvP7mSARAudpf0WUoa5njQhATk7BXDIgmqdmxqy16Z2cSiWFDjqA007orDvNinfqbNm8Qd8ZNka45J8F2YdzdbzDwdjGbzwiVrtM0MF_yy9b425WNSWrkKJbsCEr6fvJ8LwwzGP2weCmVJpc5ZMv1KzDO6OoQffOS8on76UjtZzm1Pn_LakLPyGLdiamslT1MzfpmihFvWDDlGS6thpomgF30pzqKJ_hq-ClFU2DaMv7BuxT-S88A3-VrTEsn2sHJ_WiW7dfJdVNYgE-uipaqti80Gg1Khnf2md7yYpBOgS_KHKnUGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TZ9S4P5pNjCWiqC3kg58JUXkSlM-HGVEnvsvP7mSARAudpf0WUoa5njQhATk7BXDIgmqdmxqy16Z2cSiWFDjqA007orDvNinfqbNm8Qd8ZNka45J8F2YdzdbzDwdjGbzwiVrtM0MF_yy9b425WNSWrkKJbsCEr6fvJ8LwwzGP2weCmVJpc5ZMv1KzDO6OoQffOS8on76UjtZzm1Pn_LakLPyGLdiamslT1MzfpmihFvWDDlGS6thpomgF30pzqKJ_hq-ClFU2DaMv7BuxT-S88A3-VrTEsn2sHJ_WiW7dfJdVNYgE-uipaqti80Gg1Khnf2md7yYpBOgS_KHKnUGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دبیر: اگر اسم قوه قضاییه را می‌آوردم باید می‌ترسیدید؛ خداراشکر فوتبالی‌ها دوم جهان شدن را برای کشتی شکست می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/108004" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=KWUrYLOslc4PLufWFTGt2cMQQB9eY1NqjO833KlpEsj5woqTUm8yZgZrjY-p2UN4z0Te8gE3Plyp1K7UrNSez2oKYfhd7ahsWKbEk4Cmoor-ooEw0XFYUSg717ktUX9vsyX_Ut0FDPvOtk89OwV0rNbqn_2C1Dpa3bIgOz-uttRou__WPxCJYrRJCxgRfGdKOOYJv6LhQQZVwxTHgruGfqwHNsFa7tSwMriqFJ5SG6Yt4hxA78A_JzpEQRvtbRnXq8ycvTiP0ckHBDWp-M8M_qAnmQZNmnRMqbLiFtaYF8NEd6UaAlEK8FaJyl3Na5JiDtcZqMilGiJTpGxhGY7Vo4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=KWUrYLOslc4PLufWFTGt2cMQQB9eY1NqjO833KlpEsj5woqTUm8yZgZrjY-p2UN4z0Te8gE3Plyp1K7UrNSez2oKYfhd7ahsWKbEk4Cmoor-ooEw0XFYUSg717ktUX9vsyX_Ut0FDPvOtk89OwV0rNbqn_2C1Dpa3bIgOz-uttRou__WPxCJYrRJCxgRfGdKOOYJv6LhQQZVwxTHgruGfqwHNsFa7tSwMriqFJ5SG6Yt4hxA78A_JzpEQRvtbRnXq8ycvTiP0ckHBDWp-M8M_qAnmQZNmnRMqbLiFtaYF8NEd6UaAlEK8FaJyl3Na5JiDtcZqMilGiJTpGxhGY7Vo4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
🎙
👍
لئو مسی: از همه کسایی که کمک کردن آرزوی کودکیم برآورده بشه ممنونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/108003" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
👤
طنز فاخر ابوطالب؛ ۸۰ ثانیه تلخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/108002" target="_blank">📅 11:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
الغرافه قطر اعلام کرد که استقلال بدلیل تحریم خطوط هوایی ایران حق پرواز مستقیم به قطر را ندارد و باید راهی جایگزین برای حضور در قطر انتخاب کند. آبی‌ها احتمالا باید ابتدا به عراق سفر کرده و سپس با پروازی مستقیم عازم دوحه شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/108001" target="_blank">📅 11:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
پیام‌ویژه یک مادربزرگ ایرانی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/Futball180TV/108000" target="_blank">📅 11:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFsU2eywaa5lQ1aYfOxI54SMkRVtObGuGVbcP4XaH4FF-4vTTTgowZ6xt8QLyk0i83rv_vPF_IKq8irRpFp63i2e4_DXjsqAehpSlWUhsFQtd7IzFRtYUOVD0uVZ61mjJEEKqFdB8GAT47vA98iJ04YS4UD9zdp2pUAphUBs6IcmewjufICLU87ijqeqX2OJmT4zzamJi4zsqkBdc-c9GX7Veq7SNK9xSOR1Mk0OTPOFsEbYVrQMsXPRZi5tYybJnptkCrm7ezqspj9UrwoKpM1rw1TeSsyVSpajSxmznA2QICFzmvFZC0gRTP-wa7Zy99HVF5R4CsivDz_gdEwa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🐐
☄️
لیونل مسی با همراهی استفانو دی کارلو، رئیس باشگاه ریورپلاته، کارت عضویت خود به‌عنوان عضو افتخاری این باشگاه را دریافت کرد. همچنین یک پیراهن ریورپلاته با نام مسی، به اسطوره آرژانتینی اهدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/107999" target="_blank">📅 11:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107995">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R36X50Cks2u03SyfhChA5dEYOUkj2E2IlRUcTQ3ESItBlhC1DvsNJ60lKBQuXivNjXDRUZWf-012PenQCdnxgDaAbs3MTez6p8OnpjNchcVr1G6vuGroOWZCzPU60j_txBOYeIcHjIWlWdxIoYb7takT5lmmXh2QQGjZ47BddZTh2vfA73YsnjFWDGLsa2CTrdoBcGbmLRHsVbixqyONaIFwzkBOIOmVBrj4tOLUGMO2rNg09hsF6kBjlUgDhR2YwClK3ODYSAVJRdl5LqaSncJwEm1XqP-lriZDz0oz-XJmZdX4BUjn_G7TF7OegO_BwLL7Ww57FFkZs8cQymw3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kghIR-ZmaQgw6_o44uDwgG0AKyM1pUTY7Nl6uT42BDsfpBVy35gXytu1abbAKKrFy03VCNxp9vptOPkBAhpApohRnTnLAeepwoxvtRlF1_6F4mxjJl4cQ_y5kjrTM6JtBLrF41dpF7IHZBcpEofCTpQIrte-ho3BcydR7Ip_4-VQCqOiYrH-a--lEPZMmRzjZ_kGJqhI0V0juMvWn6uAGm6R2obrslQOubjIP-iLL7TvzysKZ2y0kRp5pytZrB0lCrtyLi0Oys35SADzyTgzGTujYzCBixXXToGOJaPVN9X-gnTd3k-Y-36HGai8tJUdWJ7vfhgXrNtDIKT6JfcS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUFt6GsHZLtjZ8p89WJZszZ50OGKDNKSGXks7IqplazYg_3soVLXBCQN2AyoJhs5hKjxKyPoOSe22ee6Htv-nrW0Xf755jrsMeLwYLD5_uAVEC5LaAx1J85Wbda9P9XxWHE1sxgPmEfyuks8_XXqcOsgVYDFOJgKXvjsXfQO_Xoffl6Jh3v-ryz7sqKb-EfP-7_HN6VkNv5ZlA6FSyRcrptn158q1jkf8_ZziMPxLLIgkKSZuq1naMTA1xjBMnFubiO2A3iDw5IrtN_g9Wh8oUrxPmtK3mwpjsc03blv6NgssaQCrRrg03tFhq4tdmsJrqFvir3vjFIn9sUe4sblqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9trBph3UrAvERBPpOuR2T_GjT8MOr_wi5wKMe_Y5uUV9vIo2Pnv7RnFzLR4iejVxEzvuNOd5mHjlySLqbbOxbPjI9b9qDUGdcn3LFj_kK2sfSdHMgon06SgZyryFY4mNog6BmD05LPvAk8HpFEqjDpyBwnQfaqTYrUO6KFlmdiV7VDLj5Bq4rNBDt6iXd__40AvKiVL1h_1iMjmeR4mPpp-efOb0iY5dFeco_ZA5Tmv_PIMreSmqGEtqUJtx4ERP2iRrg5-CN_LVEXtPzrJqYTNEdopcHRBJk8KN66pHDiX8KHN-KJz7GcEXSuHEi63_6vRGcUFmN4JRy_NQPEwVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚪️
کیت دوم و فوق‌العاده ملوان با الهام از تورهای ماهیگیری و امواج دریا رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/107995" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107994">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎙
✔️
😭
لحظه گزارش آخرین گل مسی در آخرین مسابقه‌اش برای آرژانتین توسط جواد خیابانی، رسول مجیدی و نیما دلاوری⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/Futball180TV/107994" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107993" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/107993" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnFJ1-opgG4u2WZj82GwT8w58a06x9VOYj0tT00gt40a7mEaKYcbIBfPLpLejXvUHFrdFidfUJ9XRtWXpklOHump3d9_LL52NctqByFuI8vZtmC5ay95N7HBbZ8hFE-toDZAWxvIPA42YaFRS9I28uySKbNlNj9Te7K-qXNT6un0L8arwpw1-Rt_L40utWKIV4EEmpqvrnvtTIDx99VB6GoaAXBg9OC-4AOi4LNe1_jX6TazffOzK7k3u5kPTHm6U67ek36kdYsfZDTGlR0T4gj9rqLH79pjba3uaRt0I0JC8ic_BUvBQeC0g_auuHM5swQ2idGHjELF02GEED3jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/107992" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های تلخ انزو فرناندز در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/107991" target="_blank">📅 11:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
😭
خداحافظی یار و اسطوره بچگی‌هامون
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/107990" target="_blank">📅 10:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtFYLybTUrHssjt-ELZMOixXrZhF-YGxHEpV_jV0AeMnSXoMIfOKBA-8xvhP3Nmuvx15TB4ZpGpFOCZ-t-izpRNu9xDDd0NRbKT126192FnFrtcgeWt2RQxgoMotXcerH6A-5jufXULnUYww1S5njenm4ImGQ5K29tdFWo5fdxTp6tuLiq6kvqtLDQabqBmmYLk5T0WHXPcD4Pb3_kWFFZJmrF9wwPkxZ4QVZMGv9GybEJJO-2WH3AqqeDT9C2JcQEaom1I3BQKxaBisj-T2KqSEG36_vvhW9daWKlhmo24t7wzS2fvVfFyPxN5d2MH58vIo_iKGCWVbSOQhtl3zPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🇪🇸
🇪🇸
مارکا: هرناندز هرناندز داور ال‌کلاسیکوی پیش‌رو خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/107989" target="_blank">📅 10:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
😭
بازی تو دقیقه ۱۰ به افتخار مسی متوقف شد و کل ورزشگاه مسی رو تشویق کردن. همه هم گریه کردن و اسکالونی کنار زمین همش داشت اشک‌هاشو پاک میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/107988" target="_blank">📅 10:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌دیشب اسطوره از نمایی متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/107987" target="_blank">📅 10:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=XB9uixUDqokbi5jMk6CFAZegNI1ZQI5rI71j-myHqkOyMM1SZWknM-xNtML-w0166Zd7cEYBE3AkQ59SNPHKMVrDN3gil3q9cbcJ4smdyb4K6cbtTbwyBhqbYUwSTKJoCFkzyhCvuVADEMNO7dyHJGsiJIohZirtNByUBCUNLd6iPaGPs9R6e2XG3RO6ikrioSTdvwN81TmeEufNxhWqL8ALOXHhjiPdkrWHmieNk6_s6PQ7Ni6hafTw53bnxYn8n9JpxC2Wos2s_td55B1u2ig2KZzFtePKuNpSpcdKKl0tCk_4hw5XTMKItxMi2W9YseawvQLK7-drHdqOPuLf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=XB9uixUDqokbi5jMk6CFAZegNI1ZQI5rI71j-myHqkOyMM1SZWknM-xNtML-w0166Zd7cEYBE3AkQ59SNPHKMVrDN3gil3q9cbcJ4smdyb4K6cbtTbwyBhqbYUwSTKJoCFkzyhCvuVADEMNO7dyHJGsiJIohZirtNByUBCUNLd6iPaGPs9R6e2XG3RO6ikrioSTdvwN81TmeEufNxhWqL8ALOXHhjiPdkrWHmieNk6_s6PQ7Ni6hafTw53bnxYn8n9JpxC2Wos2s_td55B1u2ig2KZzFtePKuNpSpcdKKl0tCk_4hw5XTMKItxMi2W9YseawvQLK7-drHdqOPuLf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
فوتبال ما شبیه شوروی است اما در مناقصه باید وعده اسپانیا را بدهی تا برنده شوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/107986" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خیابانی: سه ماه دیگه صبر کنید تا بفهمید اسم واقعی من جواد هست یا جمشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107985" target="_blank">📅 09:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ufXsoDdY8CMfZaR7dTbtdBUd0Y7ToOT63j5mrxtwJ5hozH8bmGm-OkCk9RCRC296h5T1qdD9LkWtQ6TH4kPjk7azkDDNx6kBeZ0ihLO2fBlqOXloYtDKRkDJ_y0KDlxkntaU6kII9NoLccge-H3IoTdUh7dbTb0xY0ELqoEBqMptH60_CUa24h2QgLxv41cLAwkXaHzQzBObZtmXBrwq8MEXvxCouE82ljDtROQVA3G-tfz_weGsMe4ct_c9aNsBEwtzc2FrPMCPs4EI5zX2PoAm0yCXLnFBXJvNHv-Y43_Vj68baJaYvraj2cszFcOaushnAdmP0PaKyw12tqOM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ufXsoDdY8CMfZaR7dTbtdBUd0Y7ToOT63j5mrxtwJ5hozH8bmGm-OkCk9RCRC296h5T1qdD9LkWtQ6TH4kPjk7azkDDNx6kBeZ0ihLO2fBlqOXloYtDKRkDJ_y0KDlxkntaU6kII9NoLccge-H3IoTdUh7dbTb0xY0ELqoEBqMptH60_CUa24h2QgLxv41cLAwkXaHzQzBObZtmXBrwq8MEXvxCouE82ljDtROQVA3G-tfz_weGsMe4ct_c9aNsBEwtzc2FrPMCPs4EI5zX2PoAm0yCXLnFBXJvNHv-Y43_Vj68baJaYvraj2cszFcOaushnAdmP0PaKyw12tqOM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پاسخ جالب حمید محمدی مجری تلویزیون و برنامه فوتبال‌120 به دعوت ضیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107984" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نورپردازی و تمجید پهپادی از مسی پس از پایان بازی آرژانتین و بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107983" target="_blank">📅 06:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIfzUVShNmXMOQr899369nPXpYDEUvo_0Dq3WOFQmk0xCfKK6h401QMG0vPuyE-KdnziG_OmTETRsAk6q9YyqpHbxLCClhUbc2P9MhUtV1sqXIke-RnX34V0eIw3ByVVK3B6NoshjKDgyVXp0mGNg2I8G-Hz1s_gxkciqX-sWdcZZgB2XfU5u3KsEnit3R5O09bIKhevGhXjMKmF57pkKh3rdADQIEQz4gavdM2zmZFSkX6QjEl42V7VEfl8ITkrFllPaYP7aGj6F2a2b4elH46LTP8FG5CFSbMLvoY4PGQ1aWsO9s4sL6LLm_wbqfsRAbCU513DQJde9gdpbW1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeyBH-g9Osr3rbjOZB5AWY8XcU9t3mxXhCkvAPu5dasDFujmPHno-9QKmowgpUT1i79v6JDVVBH5GG1E9hsjMWKLBNPptQyBWyyVr2qU-ej3SyFieofcWvCqQxvRnQ4wj3ezHJoIyyYuLfmvWOIphnyvN0iLvaDLSPFJNbECv0_H7W9pkxoIs-lyobDip3IBaR4ghtHLi62X0EYTAq0GkvEkatF7iP-Gw_60TKHY02wpmPYh2NbS00gXrJJZcTBhuCtzL0KVc0ImsaVol17hFdrnLeeGMyxY6nl77lFgSwa3oXTcqPSKUf4VMLy4PLDu4bNbpD2PKH0vpr0Za72_kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😭
😭
😭
اشک‌های دی‌پائول بادیگارد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107981" target="_blank">📅 01:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آرامش‌خاص و لبخند‌های لئو در حین ورود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107980" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL89O6aZGuytaMldxL3nS_cc73r43jkHqmd5KJCwo7sI2rRHWmbdorrJN2wQ3QF7xRFEUOIpK-OjC5ZjyOTquP-SXDE3Y9y-bDRkG9VCxXh__MAlpkACcBU6_7A11U1PkXsgz1vVZYUGd80-cipV5mYX-_0Z_kDHz4XJFrxztKcg1-xhJfD2EqKqwtgGvi95SwgRfVf6zPaLuft69PHIEpJ5UwnUTLN3porQQx6bkNyTxIkk4UkXE3rIbPVTaxcjenppA_HNhg_ObTeZPe95oM7RD7KM2u1HlgnLfFzP-7N852CvV8mtbuMk7CImIe5ztCMpQtiUNyPOu5IV_3ImhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لبخند زدن هاشو ببینیم
🐸
🐸
🐸
🐸
🐸
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107979" target="_blank">📅 01:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvGNSJ5RvHSZF1jupKTDiUjQh0Jma_3k7Ufk8QT8DK6n-6eogJLwoeYu7arBaj_RgD5nf5R8sNdDZyVEhATjLPc_Bp0VcTMEw4GYhOjm8IIHhHNwwWEgtO4bK8U0IT_SSePGun_kZRg0IR7Gw8zlln34_ZPHNRX8ESF2QsU9Ly3WXvwJshEjqPp4NXuGOZyry-2B8lvHsl7ee5Cx3-MCJkz-LFIZnpxIyzRoFbCa0JOZLatUqNesfiXOdab8qg-LB7WVE2n38N2fl6yYzEDCk9Tiun1i_epeww-uLBzNCqXRclfWSKIcaRPj98l6AUGliIrEK7xoWWJyofylEqxMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
لحظه رسیدن لیونل‌مسی به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107978" target="_blank">📅 01:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0rzl4DMct1_KEgmT8sugGU3GmlNYmHTBZ9t-IVs4eMisE-O5NBpjlRycX4R07A9Up-j_QizRsL990xU94bDob9fnTJ015AEQyRO2L6fCFqOejiNqIILwlykKevOSsCfcfQOeEII63bp4LiKQbfjHblilmCdmIKYj1yFMq1N3s_cGxKKBGbAwQf6ZPOr5EgZFFJhF7ra-BI1cdpghfwx92ycOjHn13lscoioceWA71ioRwKhIaA2POOTbgvFSBMxqIZcR88-DOwU8F48X8DhanjqmbcCtgTl1rGoGzrrpcgd74FCiCSWyG9MaPMe2_To_jZyiZ8G6esDj7xfimGdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
نمایی از استادیوم مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107977" target="_blank">📅 01:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😭
استوری امی‌مارتینز از سیل‌جمعیت اطراف ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107976" target="_blank">📅 01:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو فوق‌العاده استادیوم یکساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107975" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZN5Twh459Q9e_3m1cHhtyHt_VlEMVtGQmk-QV9JUO7A3rIsHKJV2KaD1wB74FoXbl5XN_NQYutvGlFJnP-ptkgF5icn7sJ6iR0N-TOSlplMBSLUHUzhTJyNPvXHkhRG5_LwQAAf_R0nCCZZMRpNcuGF5hZ0FzPhQP-ET2ChvCK_bnwEyOxsCRc4tWIM8O0My9E0PSCNFYGsvdFJmhSwkzQ73aableMRMmwW5rfE7UWy5upzSRDT0EzXNJclAXEuDboLKmQQ7128g5R253hz7ugvzRZbeK-JY96QHgwmuEgMZRJGytf-Pueenu5UK8dK2HpyTRtNDGYRMiNcPUIzcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URIIadWTPZrdXt02PCP39SGDR86XEYisZsPNnROo9-Z5PPI_gFZe9_qT_-PRWfSj_CsFdWi3wYACtRhQi3cUO5bM6e7Fd19EAyShtjNPhLncOAefQnPmwLfL-vtPxM6WMBPVA8NY4RBI5SZj8UsLFb5jllcFn2v5X3lyaHUpQhu5rgAmAFeLcQRDKNMvcaV3msgKD-agqQ8Ym9P93jacgRQ-PSn1Wvy_PcoNJ1ldERuIovFYonJoNJ5Mi9i5krbXsIpo7YzssxfX06wmAfPrmDfY0U2YpYNdqHyTA0sIPNBbtALEO1AjkNv4IZ91icCU1gJR9e7yU718Oymlbe4aHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عکس پروفایل آدیداس به شماره ۱۰ آرژانتین
همه اکانت‌های آدیداس در کشورهای مختلف، عکس پروفایل خود را به عکسی از تشکر از لیونل مسی تغییر داده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107973" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینقدر غم امشب زیاده که آدم رمق پست زدن نداره
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107972" target="_blank">📅 01:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVihbgWdk_nkwjvtffm6TuyfXePwfM-8apmMuLTSEmHhkDvRhcLsSo47oFLh-Xdg8QAHqYtCgMeatDE5TxKuco_2XWKta7HVu-5Bp92Qi3rFRKPQLPseO4004DkEtHqs3dB1dtAnAWKY1h0yN6Ok2E-536QDOUsA67dkYMasLyhlXfxTpThlgfkTBJoTuZ_ltb5pO0wjjM_zhna4ajfdSvIa5-TogG1BKd-GBJJA13qgG8z6fgTWPNtAO8b2i8sVyAX4mneK8pEqusGTKgYMTYix_BwcQFDZoEDx93-_YJxWohaSAaQl7tNLSXk3fgXe3q-5y2YDigTNFFs3vWrClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
⚽️
The Last One...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107971" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDkKAXrit-ypZHBNoUqWmlODqInA_neFdwy8v2Rkedv3a9WHkXHuNHzxluKQEHQ6-xqHjPKHmpSDsIThsbHd6zpVliZY6513AFIMlIDcupxKYodsUMd7fwUmQDpKbmqSQ0srlYt1NaLRBVPk428C-tXpH54hXix6ZdlbknCmcyPe46WYCaTcczCj3L_qbEHBLthtcIaxE9Dd_LYRwZXyi9SlDTmu4sHLZ3K-_PlTBfWBe1Payoj9-1PSkVsn_NPqt0wTi30CGKEZiqiO16v_qWsbP0aryEuaQXCfRmZlPynDPy1LJ5cz94A9EBjGYXwIB_x2WvpzlM84a90ZWIqzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107970" target="_blank">📅 01:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wge84qMM5ODe6M2_CXuccHKkdEgRn3f6YhdyYk0ZSiW_bUEPJBOnEbEGC6VoxDN2rQZcN47Xq6oCVgNnN7NTQbLXpJPb_CF8IN1hBbwCskYYHChlEkrWvx9-njp1QB9HdWLs8dbxl10yKwTJGbZzoHmeRwDCip8XmkM5p-MzQgqS17TkCl1Oe5vXt4GDgKFIS2jDSAFZF1hYYUrN59VjqYAu_B9rfeEaMc-nxxippKDSIlcjkPCn2It8Nv6cvDbi9H-u6aGHlosHV80vP5akveSVnnI_pFN2y-zr0PjnDptmbDYjPX6HDmpeKqMuZ6sHElbq06hep6_E-Ad_VbxYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107969" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTu1K514kuQj77nn-LfFaLEi5jRWItcP_MBLE_37Ftw_i-hQl9_sZLrXejZkg88jBpd4yCQZs0chnuxG_nzcEl_8CmaezEcAMyvbtSPaDTIK6GaPYOWc6Ac6fIgJ6NY8ir8ni_O8FLhh5iTWfKPPUyrf8lJOypC5tYYirg2uK4nMy2JmF77oYuOk8qqbya9Ddnr9Uw3UPWDx0x0DXB2Zc4fLYTjuM0aNlOdxq1okNLFH8hfEHJdWPlCaj0sNpI_v2Bq1rMYqgogTj03EiH00EcZ8NirkTj2MvRv2uY7aR-LXsmeSlvRx4UG00MZWh_ukltW6mXmOYHdec90BA_gsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
آمار فوق‌العاده مسی در ورزشگاه مونومنتال:
29 بازی
⚪️
19 گل
⚽️
11 پاس گل
🅰️
30 مشارکت در گلزنی
⚽️
🅰️
✅
هیچ‌وقت مسی در یک بازی در ورزشگاه مونومنتال شکست نخورده است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107968" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=LJejC8ImA9-OQI_A0lqFr5e0ubiNCkfwP14PRMEBa0CVRB_h8Pp3q82Rg4aRcicPISAFMiFsZ48BmAUzXyCGw3fL-EgQ_P0FLnycu5Q_raQamwmUGWWD63vJOmsbhSVLcyUL1AdW6xYAGJq2J_BVxpbWxK04rIwjhE2A0-Am1qVB2K1Ez-obnyy1t4Nj5hBri-2plC4SbVXei7mfqsH4PyTlyA0MsijUodleDRcv-e_pSCbbVKD9j9EuS4jjtDqHrJRAp3FP1aU3U1dOSZCOXOrOD3Ywn6hUK46Tp9Q-TtqCz-waCFe1OscdQwVtEAz5-WAOTMVn8GLEOwn_VrFfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=LJejC8ImA9-OQI_A0lqFr5e0ubiNCkfwP14PRMEBa0CVRB_h8Pp3q82Rg4aRcicPISAFMiFsZ48BmAUzXyCGw3fL-EgQ_P0FLnycu5Q_raQamwmUGWWD63vJOmsbhSVLcyUL1AdW6xYAGJq2J_BVxpbWxK04rIwjhE2A0-Am1qVB2K1Ez-obnyy1t4Nj5hBri-2plC4SbVXei7mfqsH4PyTlyA0MsijUodleDRcv-e_pSCbbVKD9j9EuS4jjtDqHrJRAp3FP1aU3U1dOSZCOXOrOD3Ywn6hUK46Tp9Q-TtqCz-waCFe1OscdQwVtEAz5-WAOTMVn8GLEOwn_VrFfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زلاتان ابراهیموویچ برای تماشای بازی وداع با لیونل‌مسی در کشور آرژانتین حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107967" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=VFg6ZO0LacrbYVfgYV5q1duEj84Lfb-eFqDDNYWyd7AYv9QiVPKc6vEz7jq4FRMOaQ7Ltn1e0qr3Q2bbR4MAvUkevUS7zAtwcqe1IpY1IlHzqyAtENvpKNqGBGkgWNvniCdrYSxMLi4ENnIeEwW_da5ssbyPcZk1_TWjTe3nOT8A7yPb3iOcZl5xlMzpxnZJ0WfV9tIuuAOsPR0cQ5Iu1cgUMXQ8pk578b_GCxqkkdpdd11ScDoDYCsB4HenzcSZFyB7zvNqRdwY-9DcaiTZYDLh69qZ8es1f1TgwmEdv4CfvUpTOmN4y9C_Mr26uPoZ3EZ9OYn-Ony2VaPL0reGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=VFg6ZO0LacrbYVfgYV5q1duEj84Lfb-eFqDDNYWyd7AYv9QiVPKc6vEz7jq4FRMOaQ7Ltn1e0qr3Q2bbR4MAvUkevUS7zAtwcqe1IpY1IlHzqyAtENvpKNqGBGkgWNvniCdrYSxMLi4ENnIeEwW_da5ssbyPcZk1_TWjTe3nOT8A7yPb3iOcZl5xlMzpxnZJ0WfV9tIuuAOsPR0cQ5Iu1cgUMXQ8pk578b_GCxqkkdpdd11ScDoDYCsB4HenzcSZFyB7zvNqRdwY-9DcaiTZYDLh69qZ8es1f1TgwmEdv4CfvUpTOmN4y9C_Mr26uPoZ3EZ9OYn-Ony2VaPL0reGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دویدن مردم آرژانتین همراه با اتوبوس لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107966" target="_blank">📅 00:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L47K0D12YSCG7qtnzxkYd4e_rACli6UxacxTDFZDySAtokBizDHC8IOzGwu3aajcQdaK6jihwEbMXOjE7wJiHCZnBKlQa6s9ThA19tJBrLtZ4hWAT90a8luhp92Je7PW4XmrHo3aX_WAc8HLvEbVzWFK5dDrZrly8BdDxx9J4F4LGL7hx75fOw4afA9pXcpldnsDBBDbRiBBk20EQ1jyEWp1svBd5opiFIwBHKJYZ9OXi3i8aOIJDv865sadNUwAGgoJ8SuY2PkeqUFaqW2LxDhdx3dnkSv8Pz6phQiWd3dJ0WzzWVbHuWQdGE0v-Ju-ZrA-6YAV_0cbJwyfmEcD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽
رتبه‌بندی گلزنان لیگ ملت‌های اروپا پس از پایان هفته چهارم:
🥇
هری‌کین — 6گل
🇫🇷
مایکل اولیسه— 4 گل
🇪🇸
لامین یامال — 4 گل
🇫🇮
لیو والتا — 4 گل
🇮🇪
تروی باروت — 4 گل
🇸🇪
ویکتور گیوکرش — 4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107965" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyKnvRIVLHxB9X8jxHter2-QSkhicOO2CKfJj6XgY2tac7ANbAadZ8FW5UZldHdnJCNXiHvlD5gLYunUtKJncRRUlHqakdQyGkkklZM5n4tjuHu8HnMAuwKZw9WJ98ElqDQJDVQmYbnUZcB4hhzdrCCNxIzgJ0aOB1u6qDc3lHRIelwUdZA6ccYWf-u7s_u9EY4i51nIApbooyQ2GHKwFkuVWST_qKt5mV6qdcOP-1hZoq1IS5cWWhiag21cAckHiP-dkxsfxWAKqGXa2rqyYFHBY0d1hE6XfUrzy6cLnEFG5rdeXeLgmErnFRPNx9YE1ntY4H2lhJYOeY_m_xKBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره در راه ورزشگاه
😍
😍
😍
😍
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107964" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=QXA_LQ9WYtgO2xrj8q5IQmU1PrkENrisGR0ORsKuKVw5u8eNng2Pl2zkgTZ978SzqUC-psaeF3YGkf0v4izZd5hv_7e2CDy4ZlBCms2b3Iqkn8V_u8dY-tZUO1nn7gxQavsoGxd1MJSj2p0SdQNknXQi19JmUGG6QrpM6tThI-znLNipc8AiCP7TR1U8U7ivvLAqCXLWVJ_pxRRbE46doF-iKL7hQcsdXhBE2Bs5gT0DeWJUE1Fd4M1tay0rcyJDNXHDkDEoZHNd-oWZBJ8sGImu7QIQPvWiir7XiFcCJLVxD19tKe9dXwpPqvugCLvZ55aJMeL_RSc_hzi3kD95Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=QXA_LQ9WYtgO2xrj8q5IQmU1PrkENrisGR0ORsKuKVw5u8eNng2Pl2zkgTZ978SzqUC-psaeF3YGkf0v4izZd5hv_7e2CDy4ZlBCms2b3Iqkn8V_u8dY-tZUO1nn7gxQavsoGxd1MJSj2p0SdQNknXQi19JmUGG6QrpM6tThI-znLNipc8AiCP7TR1U8U7ivvLAqCXLWVJ_pxRRbE46doF-iKL7hQcsdXhBE2Bs5gT0DeWJUE1Fd4M1tay0rcyJDNXHDkDEoZHNd-oWZBJ8sGImu7QIQPvWiir7XiFcCJLVxD19tKe9dXwpPqvugCLvZ55aJMeL_RSc_hzi3kD95Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه‌ای از دستاوردهای همتی در بانک مرکزی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107963" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxhDj4DiQfLQ-1cnF5zfRnKgrv_7aOSDY3ApHS91HVwpdpPhXK-sByxno58sXzjWtJf8c40_4NWmq21XrRsSUQkCsCOq7kAlYa2yYthRO_9e7bpM39aRhE7xFqcCzSZg-woU8KHDCKpqwvtqxCw6IkxDETNVYuhBF89-HKYgGT1fIsp_HoJTft00SCQM091UV401UuS3p3jNIhsWIohEpt5OY5rjjDahvbs3GNB5cbVIyXOzZtfCgGm4YgFnIv71R62Jp5UtJoMfJXZKoznCHQwaRFUF7cTBJeOHJ2_UVaO-MpW4lLorQ9zf76ud8zPWPpmWsBZYslmijI_u-XQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107962" target="_blank">📅 00:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcTg66lKWGQQ5nICipBIeMKb_sMEYbDwEtcG65hEXI72z0_2dhq3Q7r3f_2BB8_DxrzJBXpeUxYLj_5W-n67_ou28ontX0Cc7M56HIovhn5jwRTTyg4VmyPdmHwrmzFyy1YK90CL4bxf33wpwvunh5BHH6TMTtzHq92W8hIUNf_79VRopIMH_laEOZyabYNCzVeMk6Jd_u0tAaFRiCZxgHAv3snN91m5QM8Q_5lQ1_nWIcVmRv42XA8NOL_ERjB_2hRSUwRmQUvwRolm2BdSn1gGTX-8w4_YP7vT8HN8u1U-oo5wY7lcjfaFcznYUIFnX0fWpgTPeTs2P1dlqaWpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا به مرحله یک‌چهارم نهایی لیگ ملت‌های اروپا راه یافت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107961" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107960" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107960" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
فیفادی کسشر و طولانی سپتامبر و اکتبر رسما به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107959" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=vl22bQSU85YOZn3LZ-KF6PMv69C8UH1LGPXAjInsbizwoaCn4jr9KuNPLSi66ofJCvZirgHpPN61XcOmjvEfcse8YSujvtDPijcpc9g3SxmKse8TlnpFurZOFAuSZnlei-3r_MycOKT220a0K1_XV32iH3XolkizTksHdQPtfBplDmraTdfESrNgLvK5jvl9oIHf5355UdUbP3ofplayzoKBQRtxEFqXgn2jbfDgg48JhDt2y6zM8VLYJhM813vJLGe2502qSs4cWR4XSRsdWcKzP6ty3i-i35332netB5N6OIoJfpB9x6SRY6Am9NA3CMte6U8kRTXiW0UTsOlWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=vl22bQSU85YOZn3LZ-KF6PMv69C8UH1LGPXAjInsbizwoaCn4jr9KuNPLSi66ofJCvZirgHpPN61XcOmjvEfcse8YSujvtDPijcpc9g3SxmKse8TlnpFurZOFAuSZnlei-3r_MycOKT220a0K1_XV32iH3XolkizTksHdQPtfBplDmraTdfESrNgLvK5jvl9oIHf5355UdUbP3ofplayzoKBQRtxEFqXgn2jbfDgg48JhDt2y6zM8VLYJhM813vJLGe2502qSs4cWR4XSRsdWcKzP6ty3i-i35332netB5N6OIoJfpB9x6SRY6Am9NA3CMte6U8kRTXiW0UTsOlWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107958" target="_blank">📅 00:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=mDfNepFM9nUOG2nTTfSG8todFEHDVwAz1HDVT5oiIvvU8dakQ0tm6RyA8oaHZLun34db-CR_DFozffsPko72OPWKOQWsVDrGW9BqPjhgPwsPjjzPforIXVg0PIsGusqqeF-xglJUURxrxNR0vsGRcSVAb4pgB5bpkEV9Svm16bv9bn6pZsFaJ2JW7_P0KPc4KhNxR1eW2ipy9A9Hhdm7nL4-UAa3v5CUkfB-M3Gw7u-K1FbaMOqmIbUf_pYVpLqWdJymommIxVOSOdM2UI1S51r8D5vKejoKJd4YXYQCzUoQLi9yNe03SYDe3_LrckleBzBw0XmqZxQ74t-w8L31vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=mDfNepFM9nUOG2nTTfSG8todFEHDVwAz1HDVT5oiIvvU8dakQ0tm6RyA8oaHZLun34db-CR_DFozffsPko72OPWKOQWsVDrGW9BqPjhgPwsPjjzPforIXVg0PIsGusqqeF-xglJUURxrxNR0vsGRcSVAb4pgB5bpkEV9Svm16bv9bn6pZsFaJ2JW7_P0KPc4KhNxR1eW2ipy9A9Hhdm7nL4-UAa3v5CUkfB-M3Gw7u-K1FbaMOqmIbUf_pYVpLqWdJymommIxVOSOdM2UI1S51r8D5vKejoKJd4YXYQCzUoQLi9yNe03SYDe3_LrckleBzBw0XmqZxQ74t-w8L31vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107957" target="_blank">📅 00:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=FGxhuS32S-Pd2IEKSdTXFMaAreHDLkhvowFqbgwV4FizxY6JjhxQLbzPmP3nlF4GcYW9MOb0sBYyUPRLr6wUpE3vCIfayXGKE8G0qLgjzB66Gu6_2n6NBfqX2Orad0Ix2BSld1ve-8xHikHr8ia_KfpyyQFY92CIpmP-vvtoBJ5Sx93gI0tJwNc3yPF8GMLiyaEO_oe6i9uD1_XmhImtvvZUCXsVausRQGXYmq5h_TPzT1RozrSTVI27huh7IMBPn-v9-QqKn2SjSodn3RXmIEXddZk7sK6yvyr_HgrTZC7JO7TkrDaILWPuQEnJW2OcDqRl9GXxUylilBtOXIpPhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=FGxhuS32S-Pd2IEKSdTXFMaAreHDLkhvowFqbgwV4FizxY6JjhxQLbzPmP3nlF4GcYW9MOb0sBYyUPRLr6wUpE3vCIfayXGKE8G0qLgjzB66Gu6_2n6NBfqX2Orad0Ix2BSld1ve-8xHikHr8ia_KfpyyQFY92CIpmP-vvtoBJ5Sx93gI0tJwNc3yPF8GMLiyaEO_oe6i9uD1_XmhImtvvZUCXsVausRQGXYmq5h_TPzT1RozrSTVI27huh7IMBPn-v9-QqKn2SjSodn3RXmIEXddZk7sK6yvyr_HgrTZC7JO7TkrDaILWPuQEnJW2OcDqRl9GXxUylilBtOXIpPhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تنها سه‌ساعت تا پایان افسانه لیونل‌مسی در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107956" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=fz9VXWu80-XAJb8Y3ENWWtK6dBaM45Prc7LVA8E82_VyjA7BTNHwIgRb_jEYIJ23zDmSEwDmBXHWflVOil63CQfelLyaqPLcgHbrTrJgR43UH6yG7bfnCgZqs9vdIw1_y_zQmGN-Rw_tI9U-R-nfJnFnYAJ6Gf9y763Ta02S7ef86-jkmUxbtHwAZMz539_Tdo40D2n3YTYiVt9ouw5l6ladZq0Uf7c5wg9kI722nlkL-qI3Rh4Q8gRPU-CGWx-NFws7P7q30MQp26BxoBIckCJFJ0-0D28f7XkWUmbUQZM7GQDkN1zuB-2CuFLNcMz7SfosUlldwTn86eHNiZOZuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=fz9VXWu80-XAJb8Y3ENWWtK6dBaM45Prc7LVA8E82_VyjA7BTNHwIgRb_jEYIJ23zDmSEwDmBXHWflVOil63CQfelLyaqPLcgHbrTrJgR43UH6yG7bfnCgZqs9vdIw1_y_zQmGN-Rw_tI9U-R-nfJnFnYAJ6Gf9y763Ta02S7ef86-jkmUxbtHwAZMz539_Tdo40D2n3YTYiVt9ouw5l6ladZq0Uf7c5wg9kI722nlkL-qI3Rh4Q8gRPU-CGWx-NFws7P7q30MQp26BxoBIckCJFJ0-0D28f7XkWUmbUQZM7GQDkN1zuB-2CuFLNcMz7SfosUlldwTn86eHNiZOZuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
💋
پرواز لباس غول‌پیکر لیونل مسی
به کمک هلیکوپتر بر فراز شهر زادگاه وی ، روساریو ، قبل از شروع بازی خداحافظی لباس غول‌پیکر مسی به پرواز درآمد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107955" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=Y3XVDNm0F4OwC_aW_3f1CDcFFLFAlEZkO693NF24bzXWjUVpJxhKUc3NcFtW2i6_NIYgTbBEWNsxLje0op4iuPOivreSRNRIqrurONVWeldng6zUBZrkdD0KwGDCINz5tBuwVz7BaheRxIQLr0t6iSa_nqS8xbZIZ44g69jDLhW5ddo6IvcAqyzkWXR1RxkZzJixd0YrSa-UTxRGXHkww1BVqVeE0EPuCv_TdypZr0tW7wQ9VpZcJbOcB8BGcvBTCqAIedA0u1Ze0fQ-m-bor8sVr6kQuM0UizIKYAZdGmZZ1XMeCkTyotlBjtlvnxvtX58odJKgqcEek48S5MiKjyJkWVzELeZ8NopD-rTWks3co4uJE7L04CCIMmVvcEum8ZZT-6IUkNPCcupnmLSZ-Isl5AcIgIbbHu6XXzlpGcgyCc2rikw2zhsPdDEplXqsWnia15QSXHEKCsEEFM_tEymvbfeqHfbr1TyepnWmRKW1nPOBqG9czVIvfU54RGJrG7E2XTIIlTn8hIvcUuajd1zy4PQnDseliqD5pZaJSKq1HRGZJSXr1pFin9sxui75sM6JrbZdlaNutlzp1mLN_MQch_HGv9thy-hKeks9q3bah5tUDDc8blTMOUaK2eSwbAdi44auF1-sVlhVPbms14BJwkuPnx83xsxyXgX6RCU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=Y3XVDNm0F4OwC_aW_3f1CDcFFLFAlEZkO693NF24bzXWjUVpJxhKUc3NcFtW2i6_NIYgTbBEWNsxLje0op4iuPOivreSRNRIqrurONVWeldng6zUBZrkdD0KwGDCINz5tBuwVz7BaheRxIQLr0t6iSa_nqS8xbZIZ44g69jDLhW5ddo6IvcAqyzkWXR1RxkZzJixd0YrSa-UTxRGXHkww1BVqVeE0EPuCv_TdypZr0tW7wQ9VpZcJbOcB8BGcvBTCqAIedA0u1Ze0fQ-m-bor8sVr6kQuM0UizIKYAZdGmZZ1XMeCkTyotlBjtlvnxvtX58odJKgqcEek48S5MiKjyJkWVzELeZ8NopD-rTWks3co4uJE7L04CCIMmVvcEum8ZZT-6IUkNPCcupnmLSZ-Isl5AcIgIbbHu6XXzlpGcgyCc2rikw2zhsPdDEplXqsWnia15QSXHEKCsEEFM_tEymvbfeqHfbr1TyepnWmRKW1nPOBqG9czVIvfU54RGJrG7E2XTIIlTn8hIvcUuajd1zy4PQnDseliqD5pZaJSKq1HRGZJSXr1pFin9sxui75sM6JrbZdlaNutlzp1mLN_MQch_HGv9thy-hKeks9q3bah5tUDDc8blTMOUaK2eSwbAdi44auF1-sVlhVPbms14BJwkuPnx83xsxyXgX6RCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به جمهوری چک توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107954" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=GGcdWO8guOBSv7O5rW3ndpTjNwdCRW8sD0t3mN6LKohgyWTLzoQASN-acLwPEw6KmK8WLgFer9Nk4h0kUfUpn4LhVxYzYeRtvj2smnJO2lRjNBQ1Q8m4mkXUQ1JJo_SSkh1Ipl-XIFDBAxZ40m52KOzquSmIOtc0vBR1LBRBMN_M-8yIXXUSqYXvRrk9gbU7MpPeDNhG8hKkycWAi6XfKpWZSFPUIXMgR3Ewiwnt-7Df6Tg0tfhmvLHfjEM_OoU7cVjnLBJNxDsN9ItYdMTh1bBX1Isi5EnkLGyc2rKCSwovE-_P9nzE0iO-SiQOqpzsn_5rwZdkukCsNUOJpyP_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=GGcdWO8guOBSv7O5rW3ndpTjNwdCRW8sD0t3mN6LKohgyWTLzoQASN-acLwPEw6KmK8WLgFer9Nk4h0kUfUpn4LhVxYzYeRtvj2smnJO2lRjNBQ1Q8m4mkXUQ1JJo_SSkh1Ipl-XIFDBAxZ40m52KOzquSmIOtc0vBR1LBRBMN_M-8yIXXUSqYXvRrk9gbU7MpPeDNhG8hKkycWAi6XfKpWZSFPUIXMgR3Ewiwnt-7Df6Tg0tfhmvLHfjEM_OoU7cVjnLBJNxDsN9ItYdMTh1bBX1Isi5EnkLGyc2rKCSwovE-_P9nzE0iO-SiQOqpzsn_5rwZdkukCsNUOJpyP_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
مدل‌موی مارتینز به احترام مسی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107953" target="_blank">📅 22:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu02gDUE8pmP2ttjBJXGmkuULqYAALFLY8F35TuW0KTPXWZh_g1tr_MMx-6tZUNQ2gc0Qd7JC95tQvFM3hbjjvBbxiuyU7n-VxlW09lmzw58uGfHfIbFUr5gx_2dLfOGzS3Kbffda8f-eXu8gnf4-iHSnz-zQ_QWZfSEZwFfpPBX8t-Tis_Ca3giiA3L3k0TNFuBb9kaXgl9opLetErX0nyBveJRywDqGI0CgLLMSObguX3qiSpSybuIQE4hIrk_6TpzB4xV59adjfs4lbFn_PiWCC00OELweuIOmDlfr8HgY1ir1bwzZvzlfTR6WE4ZOOsNMurl0ZF_kCtwdxLWni6us" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu02gDUE8pmP2ttjBJXGmkuULqYAALFLY8F35TuW0KTPXWZh_g1tr_MMx-6tZUNQ2gc0Qd7JC95tQvFM3hbjjvBbxiuyU7n-VxlW09lmzw58uGfHfIbFUr5gx_2dLfOGzS3Kbffda8f-eXu8gnf4-iHSnz-zQ_QWZfSEZwFfpPBX8t-Tis_Ca3giiA3L3k0TNFuBb9kaXgl9opLetErX0nyBveJRywDqGI0CgLLMSObguX3qiSpSybuIQE4hIrk_6TpzB4xV59adjfs4lbFn_PiWCC00OELweuIOmDlfr8HgY1ir1bwzZvzlfTR6WE4ZOOsNMurl0ZF_kCtwdxLWni6us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به جمهوری چک با گل‌بخودی عجیب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107952" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
سیل هوادارای مسی برای خداحافظی در آستانه آخرین بازی مسی برای تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107951" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به اسپانیا توسط ایوان پریشیچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107950" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گگگگل کرواسی یکی به اسپانیا زد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107949" target="_blank">📅 22:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfAQ39ziWxC5H3R_BRMLwlSLtEPrI4y1OyzbUHUTfISDmVp3Q-H8XkVV_wyv5nSiyfjSgLVlC37Kibi5PcKEsyDDEYyziRV8V-fsY5Z8jbHZyyWs4yMKEEqNtKPny5BOjLS2o1_lbffzx_GAOIsFWp13aIU7x9c2jArI8VUQaOroPg18OAH0RBtxzG0wS4V2SiUwGwSpjQhWxdClviflpdw1gaKdCkrsy509kdcqapIOnglrK6lxFDyLTz2XnTwViQgewzPjjEybuTvGKRlqwcMEzWZo6_xG5IyMdbBZ_Trh8bbkCfhh12X51F1mmucg89n2hLVsl3SKDReO6-u1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107948" target="_blank">📅 22:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🇵🇹
اسطوره رونالدو:
🔻
بابت ترک‌ناگهانی اردوی تیم‌ملی از تمام بازیکنان و مردم پرتغال عذرخواهی میکنم. من به عنوان کاپیتان تیم مستحق جریمه و مجازات بدون هیچ تخفیفی هستم
🔻
همچنین به مردم می‌گویم که اگر شرایط ادامه حضور داشته باشم قطعا دوست دارم برای کشورم بازی…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107947" target="_blank">📅 22:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2QdmaWrUPfEYzxNEoq07ZkBnn7xKZh0ShlJg-7eWrPsXjoVh4EVWUC2p9lUbJEIN7VXPp2QeYHJIyQ2fnrXhWz359w7IIzMv9jMa7_2jzIvSOEN7gX_07sTLjeMUqqVPn7ciirH9N2JuCssAhdgv83oQ9c6KO4OFJOtLLhBI_-A8XWqwK8-Au_x_A_5FCa_em0cohqMgOessI6dQZSwFrAdj-GJfMcKQ50bEIcaxNt0s48DqyHFIvw0Vqg9PGm8uOfPMjjq5Q5K2BPowTmax8ejQlePTOjNPbxZQDXzrYlJldYuXGm5PQJ0Z_wobJrKCRhpvHMXJPeiEvHAz0V-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره کریستیانو رونالدو:
🔻
جورجی ژسوس برای اولین بار با من تماس گرفت و گفت که مایل است به صورت حضوری با من ملاقات کند. من موافقت کردم و قرار گذاشتیم در پایان تعطیلاتم با هم ملاقات کنیم.
🔻
آن روز، مربی به من گفت که به من اعتماد دارد و حضور من برای…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107946" target="_blank">📅 22:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107945" target="_blank">📅 22:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال از من خواست که با تیم ملی به همکاری خود ادامه دهم، و همچنین از من در مورد انتخاب مربی فعلی نظر خواست. من به او گفتم که این انتخاب، گزینه درستی است. بنابراین، از انتصاب او خوشحال بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107944" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bze820j7Ki0-qOSj_JG30wf-mtVXkhp4rdtUHXTXGlUaJcmW9tQnbCmfLFiQHbhniNNU_wVIWyAaG6SkMyXp1G5B6_A1tI1Zd4ZTA0bYfswronX4r8zzvJ625GScwx-lN0P9v72CTVD7TNKWXuLSdu2LG9FvRZ-I6tZOKWZ82N6-_xnipLrTn7wOVbuShS-VrXUN0BtwsDXQy6mqlfaqvHZSofDvvDv1lvs0cNrYwhkGBijgOD-fLCRyhHvn9vNvKRkpQIZJiwZYWzgXz1dN09XpR8ZMo8SkqCS7glqEcJ3z9IAYZqGHA8mBLVYDArfm91-abdt3J57OZLxx4JWifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107943" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=KMgSFCBsvILw1uwc9SOWODypDh4KV9KeoGu7jpHAdjv1DFRemBBvvfSloR9ZE6vTKoLnIwamYeHa8_BFmZc2qWd_wPlbc1GgvKYfDWHk4EMomC1XnCRddFt4yaNKzVxI8akpsQjZi9GMYW5HY7j3BtplS3P2XP3uzEgRRyTcIkmNueY_O5IXbh1eRAfUvA9JXKoMvgFACR4_QUUcYayQ91MStxCWf98rdozZuFqoH7U5kKrf_O-qYWeupdKlDyl-OCB0Hynld8jdS-NM4u-xZTdt7aQyqjHLsmWgGh8PUdQ1vJAeZwiYgaVPhwGt60x_rK2JyPFVToHlZ5UxoaSDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=KMgSFCBsvILw1uwc9SOWODypDh4KV9KeoGu7jpHAdjv1DFRemBBvvfSloR9ZE6vTKoLnIwamYeHa8_BFmZc2qWd_wPlbc1GgvKYfDWHk4EMomC1XnCRddFt4yaNKzVxI8akpsQjZi9GMYW5HY7j3BtplS3P2XP3uzEgRRyTcIkmNueY_O5IXbh1eRAfUvA9JXKoMvgFACR4_QUUcYayQ91MStxCWf98rdozZuFqoH7U5kKrf_O-qYWeupdKlDyl-OCB0Hynld8jdS-NM4u-xZTdt7aQyqjHLsmWgGh8PUdQ1vJAeZwiYgaVPhwGt60x_rK2JyPFVToHlZ5UxoaSDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حمله تند خداداد عزیزی به مدیرعامل تراکتور حجت‌کریمی بابت مصاحبه دیشب در فوتبال برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107942" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=YMapKZu_GsVPIXJT1203GUHI4uWi0mvXJSWpjqvyjx5Dbp7e5TFpR2zDJlXNgooZlVvxn6lG3uP4XygB_0jYWTE9wAVS2YesPaQIiJjK5q0NyBWz7TRZ5PBAdkhSejLK3a2f88QdoMwzbf3mawjdsgoO_I29oTeTyGbIX2WMrALoChiHUcSp0NxRCjZGIbxfcYyoZgtBsWZb34yWNtKge8MtCNHQR0lE3xCsmTU0xlpAzlWuJ8QgSCGFFhmoOyWJbb5B8dDPFkHub4WGOH9s9H15BwRKRz4xk2tYpFm8F2n7GghHoDEcmORMj1NBn9fOfa7rBgNCIdD73fw1t1-xbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=YMapKZu_GsVPIXJT1203GUHI4uWi0mvXJSWpjqvyjx5Dbp7e5TFpR2zDJlXNgooZlVvxn6lG3uP4XygB_0jYWTE9wAVS2YesPaQIiJjK5q0NyBWz7TRZ5PBAdkhSejLK3a2f88QdoMwzbf3mawjdsgoO_I29oTeTyGbIX2WMrALoChiHUcSp0NxRCjZGIbxfcYyoZgtBsWZb34yWNtKge8MtCNHQR0lE3xCsmTU0xlpAzlWuJ8QgSCGFFhmoOyWJbb5B8dDPFkHub4WGOH9s9H15BwRKRz4xk2tYpFm8F2n7GghHoDEcmORMj1NBn9fOfa7rBgNCIdD73fw1t1-xbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشاگری بهداد سلیمی از ناداوری در المپیک ریو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107941" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=gZh-Q6YcPiPkgCysa2KyrY7IbEAPP5lG3AyGt-v80v_X4XHBYS6N0mkuK4ZYXIaXleAhs2w_05rr1gAy_8XhwXkTM-dBoeHUhVMUuah0qKvmEiV9qQgDMBq5V1DSg_ZgYuKfm5CFZcx6KGsc6q83lnDkUY9nUXipMC13Buf5WY5sRBjwSRY9bcLqvHoGpZ_H_4YWBzHmjWz26l_SUOF31Oh9WUZUEKYwu2aC_QFDUo1ADQCDfbiYrXto-nRWz_c58m70xHe3noSQmEImgb0yUtayJoV24eJZ9xTVNNlXugzCeRjOLZGTbfgMf0huKqw-h-V_sTxZKw3g_V_7ouy0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=gZh-Q6YcPiPkgCysa2KyrY7IbEAPP5lG3AyGt-v80v_X4XHBYS6N0mkuK4ZYXIaXleAhs2w_05rr1gAy_8XhwXkTM-dBoeHUhVMUuah0qKvmEiV9qQgDMBq5V1DSg_ZgYuKfm5CFZcx6KGsc6q83lnDkUY9nUXipMC13Buf5WY5sRBjwSRY9bcLqvHoGpZ_H_4YWBzHmjWz26l_SUOF31Oh9WUZUEKYwu2aC_QFDUo1ADQCDfbiYrXto-nRWz_c58m70xHe3noSQmEImgb0yUtayJoV24eJZ9xTVNNlXugzCeRjOLZGTbfgMf0huKqw-h-V_sTxZKw3g_V_7ouy0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
علاقه‌خیابانی به گزارش بازی آخر لیونل‌مسی در تیم‌ملی آرژانتین که بامداد فردا برگزار میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107940" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=O5Om610bmDd0gM7x3fYyP1FUXvvzHSsn9Pi9fHtEXlt0aQRaQucSUoruWS_6-cGa37Slpl-YU6QU8dp6uoPCM4u7aEErbPKOxWh-1LzjVzS93v73upof3yDO9pSivCQGdAqhuX3LDPg9gzCzMCJN6pfGuo1ViAuPEApzdnYTGw9scAPiGMj37I12qJzPuIR8tdknK-lkJJixldY8xcBMvd3Xjcno9VZjwPovl_Mnyi6TuWTARsCdhUlJ2e-UrEB577cba_ovQ47ddCQEphTDvnwJVF4YeCQI0t58QE7caolBu7xu_qusSyqul6lDUtb-M7CGyECXUA70AgzOz1xPrXTfrh8lDSbBvDN5fXD3pHX9Pp9snYuCKLwo6NBv64N6PmtrOJ9iGmP34_bGuXMcv4qwimbRkNmRqZ86YArCRcPDNbF4iXU_CQwoVzSBrBZViDJXkcuDWhtnOm2j8oMMdz_MCcFw5OD2mHrz48k0qHIr6XHy2RlZKTp0xurvXkznTjZUW3mv3LOPpdm1vbI7a_gckEd5LIEWxn7KILyK30c4gWehF86ls9SsYrYFFm9bXfSZtLUEHCYWe1OCb5_5vNTSG1G2h-LEAKHQawVqoljJ8z-xpkwAyo30zqBy5V9t2aSlFco_nP_jL416wCb8xSTI8TCwXVK-NMsFh3SGNA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=O5Om610bmDd0gM7x3fYyP1FUXvvzHSsn9Pi9fHtEXlt0aQRaQucSUoruWS_6-cGa37Slpl-YU6QU8dp6uoPCM4u7aEErbPKOxWh-1LzjVzS93v73upof3yDO9pSivCQGdAqhuX3LDPg9gzCzMCJN6pfGuo1ViAuPEApzdnYTGw9scAPiGMj37I12qJzPuIR8tdknK-lkJJixldY8xcBMvd3Xjcno9VZjwPovl_Mnyi6TuWTARsCdhUlJ2e-UrEB577cba_ovQ47ddCQEphTDvnwJVF4YeCQI0t58QE7caolBu7xu_qusSyqul6lDUtb-M7CGyECXUA70AgzOz1xPrXTfrh8lDSbBvDN5fXD3pHX9Pp9snYuCKLwo6NBv64N6PmtrOJ9iGmP34_bGuXMcv4qwimbRkNmRqZ86YArCRcPDNbF4iXU_CQwoVzSBrBZViDJXkcuDWhtnOm2j8oMMdz_MCcFw5OD2mHrz48k0qHIr6XHy2RlZKTp0xurvXkznTjZUW3mv3LOPpdm1vbI7a_gckEd5LIEWxn7KILyK30c4gWehF86ls9SsYrYFFm9bXfSZtLUEHCYWe1OCb5_5vNTSG1G2h-LEAKHQawVqoljJ8z-xpkwAyo30zqBy5V9t2aSlFco_nP_jL416wCb8xSTI8TCwXVK-NMsFh3SGNA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ترویج دروغگویی به دستور فدراسیون و کادرفنی؛ لو رفتن ماجرای تعویض زودهنگام محبی مقابل روسیه در مصاحبه احسان حاج‌صفی؛ ناراضی بود، گفت بخواب زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107939" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=K63bPUy0ifhtLp3TZQxZScEOjcm6EJG4I08rbuD7-onqWCfyeDYj58pxaZTe9tYaRpSDDYGaX44t0CYAshw86F02wmns5ppZ8EhMJ7yLX7cXINQTRytCXueZqHNMEHemhCcm2h6JM3E4pjwykKhg_JyUYJL-blKuB_2JvgTrHDyu4NIoaXxpY49aa49PIUVWWpMJuL9OYlfEOssNlxGZGmdTGFAKZYq47RLGoknVd4FiTTUrNfkrGckGr-Av7vlQ5IqniuvLyEeKJKFzM_FAtUxEKaNNZ8Dg_M7EhQgrAQnFV4Wv3-yardjAx5T_8zkbeTTWaLbjkVwQJYEW7LlgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=K63bPUy0ifhtLp3TZQxZScEOjcm6EJG4I08rbuD7-onqWCfyeDYj58pxaZTe9tYaRpSDDYGaX44t0CYAshw86F02wmns5ppZ8EhMJ7yLX7cXINQTRytCXueZqHNMEHemhCcm2h6JM3E4pjwykKhg_JyUYJL-blKuB_2JvgTrHDyu4NIoaXxpY49aa49PIUVWWpMJuL9OYlfEOssNlxGZGmdTGFAKZYq47RLGoknVd4FiTTUrNfkrGckGr-Av7vlQ5IqniuvLyEeKJKFzM_FAtUxEKaNNZ8Dg_M7EhQgrAQnFV4Wv3-yardjAx5T_8zkbeTTWaLbjkVwQJYEW7LlgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😱
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107938" target="_blank">📅 19:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107937" target="_blank">📅 19:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnUwYxyw7elomVcQSoCL_uMXAlCoEoYEjDy87xuFi2KqeTbZOApvoLQuua_iW7zhGJAf2cOirOQFx9hiXEmqHL7a3jdOiw-wr9P7JnSXHVBOcz0QTK-neE43_dmoEwVF5yq5sBBOWmFyo6QpAnL9f6ay3jMNg1S1cz7GrJQBVJZPfM7hAwhBYxoOeVjfFuy5vOHEDuZCDDp1lW97x7rSmYRR-e83ZjL_FN23kZU9TvzdGjsjnVo0jrxDi0QOGU_7_iV4hjsXsOChDXENzgDnsndawFK2Y9j-s5hWLUOpFS1dR1sMJxKebY7vTPI4okmMV1G5T16wfJnzNQIlFjNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107936" target="_blank">📅 19:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=tLNr127eYvydZmKpDWKJhD0q6zEg78DpWcP1QD4S3juEu2N-eHQIbieSsHLbksMxZqUQlswA2raoj-Bd0CLYb__jaEn46Vk5d834HrZjmC3Yaxbbnjetsj1aM8PYtH8-JzSzJGVnYtpo-PJ5WrxyVrOgh-cJgYSeyha5u63qoyq6XxLxq9qmCtYarKJCbUECEGFUGMDl5CO3aYvJY5gRAMIQkLhUZTtz5_hrpNsHFz5574BI-F9oRayHQYbAlLHEn2OsiP-wWPvL4qdjl3tYuPGMxLzt2ZD0CtzP3NJKFCu6uqmJwBc0jJT5uIgiKQINj8WtINv3GKaQjkoFeiHLkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=tLNr127eYvydZmKpDWKJhD0q6zEg78DpWcP1QD4S3juEu2N-eHQIbieSsHLbksMxZqUQlswA2raoj-Bd0CLYb__jaEn46Vk5d834HrZjmC3Yaxbbnjetsj1aM8PYtH8-JzSzJGVnYtpo-PJ5WrxyVrOgh-cJgYSeyha5u63qoyq6XxLxq9qmCtYarKJCbUECEGFUGMDl5CO3aYvJY5gRAMIQkLhUZTtz5_hrpNsHFz5574BI-F9oRayHQYbAlLHEn2OsiP-wWPvL4qdjl3tYuPGMxLzt2ZD0CtzP3NJKFCu6uqmJwBc0jJT5uIgiKQINj8WtINv3GKaQjkoFeiHLkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
کنایه‌های ژوله به مصاحبه‌ اخیر قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107935" target="_blank">📅 19:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=M1S0Ir5KXwvwpJ4fnH3Hahst8HJPtypIl-OSGGMXZ1PjWAAKq08amRcuH3jbBo-bApUfwOaFBW8zXKTPDeto2IpUNBCSmOyvroRePrf7XQ-E51Bh18V9TH1XsgB37Y5iYicAFjPEQL2CVUhW1X9lVstx9zQtzWDnyXmIgU_SGakw-fx1fnDcJ27ThkEtXUlC1V7dsVp-aD09EwUKOAXWSljw7AXeu3HU5bqu1v9wqxUBbG-wxCiuKGWg6CzJQcNERLzEbLDqpohB1lKOQKlCnkP7Axa_FlpWTm0rQJUO2_XwtZLmEg2Pf4_9uUk3NhNsFqeeTv6p1xvHBQqkMQ50Boi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=M1S0Ir5KXwvwpJ4fnH3Hahst8HJPtypIl-OSGGMXZ1PjWAAKq08amRcuH3jbBo-bApUfwOaFBW8zXKTPDeto2IpUNBCSmOyvroRePrf7XQ-E51Bh18V9TH1XsgB37Y5iYicAFjPEQL2CVUhW1X9lVstx9zQtzWDnyXmIgU_SGakw-fx1fnDcJ27ThkEtXUlC1V7dsVp-aD09EwUKOAXWSljw7AXeu3HU5bqu1v9wqxUBbG-wxCiuKGWg6CzJQcNERLzEbLDqpohB1lKOQKlCnkP7Axa_FlpWTm0rQJUO2_XwtZLmEg2Pf4_9uUk3NhNsFqeeTv6p1xvHBQqkMQ50Boi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پادشاه مسی:
🔻
لحظه‌ای که منتظرش بودم بالاخره رسید، با خیال راحت میرم چون هر کاری از دستم برمیومد انجام دادم، این پیراهن برای من فقط یه لباس نبود، رویایی بود که بهش افتخار می‌کردم و تمام زندگی من بود. ممنونم که این‌قدر دوستم داشتید، همیشه شما رو با خودم خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107934" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciw53FAjAZKU9dETHjT2RxZOP1NO6mHLmwwaBLrqd6YDG3plEtdj6IZvX1AmPrm9S-R7xhiNQ9rgWayaMuXyshGtMNT6fcT6L9hNJCYgDwJ7K8tpWfdzXQCPVuUY9vMwZV2delnFAYCygqKegrir1txpzFMo8dRf512MfZeVPs4Rk2DK0NyG67KtbjklIGGFFlfIcdpyef93xlKeX1EP3ThWyCQYM5gWkrwpoYMtZD-RECPCLIIr_-4J6jEUJMxH66XASvzuRppaOq4Ysh1ehlOptQU0ea1FOEI67Sgrw3MsdBeN9yVgn3qxYbFUO862VoflN5Wvwuvy6GtGTxberw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنی‌کارواخال مدافع سابق رئال‌مادرید به ختافه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107933" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341518f56.mp4?token=fLJFZn1uJN2Mo5xOmFqqvZLwI-yaZ_L8okqz34u1YNIuz0nz0SxzmwEppTzv9i6QPyeI82DEk0HskvPdQXDgiVKRZX_KjOKzwWEGtzbg4H3g9rkY1Dsq4Qrbsm9XFaRY0vVKm6RmD1GDKCIwt78YuoNuRRBYqcOu1CBn-c5gH2B4DCUo6lnv-B0jEvf1RziFFoPmQ1rGSuyHv0TT9HEmfiOWt_bIETzbmYtpX8zV7a-YRm0bAV1e1bvcdbd65J1q6AIMRPstByCw8uwPt-9OYk9eFpQ7yNWJDQgeEWhGiFWbG6M_6-ajvsLEGQztkmlVpikTDv5UVh-M-LteS7_M8adeoBxQqnSEoEMRjbQeZi-aV99x5BZjP8BSXi-DYk1YklxYvCkW5E2Oo_FCj3y2b-7RH2zx5YjML-yKtm6cW8yNEyr0nl65mE1EA-3tDdNSoOcXxJT7-cvbJ9Tmh__NMU3S-RUObG1Q6eIYcVahkyi59LMliOTCIDYzvezvdZ5Az_DBfRAkKuxZvWhkGfDNDpqNyL-0wj5199qZUFlM5XoZ4TE6paZDv08_GCS1EFYxSPiPE1Nr1HEZOI8Q0Gp55E9aKVtk42i37DrJAEOtVzHHEFxsNjHY5ot_WhpXT6cLAE94tfOmxB4NgCnMBTHqu-F-JZmoNE-YGzo1mYcUgRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341518f56.mp4?token=fLJFZn1uJN2Mo5xOmFqqvZLwI-yaZ_L8okqz34u1YNIuz0nz0SxzmwEppTzv9i6QPyeI82DEk0HskvPdQXDgiVKRZX_KjOKzwWEGtzbg4H3g9rkY1Dsq4Qrbsm9XFaRY0vVKm6RmD1GDKCIwt78YuoNuRRBYqcOu1CBn-c5gH2B4DCUo6lnv-B0jEvf1RziFFoPmQ1rGSuyHv0TT9HEmfiOWt_bIETzbmYtpX8zV7a-YRm0bAV1e1bvcdbd65J1q6AIMRPstByCw8uwPt-9OYk9eFpQ7yNWJDQgeEWhGiFWbG6M_6-ajvsLEGQztkmlVpikTDv5UVh-M-LteS7_M8adeoBxQqnSEoEMRjbQeZi-aV99x5BZjP8BSXi-DYk1YklxYvCkW5E2Oo_FCj3y2b-7RH2zx5YjML-yKtm6cW8yNEyr0nl65mE1EA-3tDdNSoOcXxJT7-cvbJ9Tmh__NMU3S-RUObG1Q6eIYcVahkyi59LMliOTCIDYzvezvdZ5Az_DBfRAkKuxZvWhkGfDNDpqNyL-0wj5199qZUFlM5XoZ4TE6paZDv08_GCS1EFYxSPiPE1Nr1HEZOI8Q0Gp55E9aKVtk42i37DrJAEOtVzHHEFxsNjHY5ot_WhpXT6cLAE94tfOmxB4NgCnMBTHqu-F-JZmoNE-YGzo1mYcUgRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
شور عقاب‌های سبز؛⁣ هفته دوم لیگ مراکش و تشویق بی‌نظیر هواداران رجا کازابلانکا در اولین میزبانی فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107932" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_3q0mKg1zTRCepms_HEcUY9g3mgP7Y6XamrL5kpZzHV3CCBNJSjzArIWJd8346e_8TSDBSjpL-YmmN818-RPtpMS82QSQ8BGlnLV8SxaM_kx-bBiGPZiWf3lAVno_ibiL4n-RTwfS5Yx4yJPeoY-OyIQJ9gFQTrk2b9eBbXj55O8qDwWzefLEzrzX_esEIfOTz-3yAShDwPVbSXLLbAh1ljneFWg0OEJN3_zhliDLZRagb58UMDZ6M_jTgf6DMkoMY-qDYt0pUg227byqA7qqozUaF8NB2YNnq7OjL6N9LY_bKzZmPvqt11rLxsWhCtbBX8pKIjI-hM-Jz4i1A9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اسطوره لیونل‌مسی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107931" target="_blank">📅 18:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=pd6RUZsKWRAVHVLF_ULIrwLMIpH6B3XxC1C0j3Acf9LoaMMFiZrs3YzHV8BWTEtV1qre7gf4KqdErDfaUAUHQjjgEKd1_8wnEr24r3dD-8iTPj70CCe-QFObhsEKcxuxH6nWkGbXcNdN3ki3eieloy0gA57rAZEZGzkZbUcY2VIhmenmkUHwHQS0u2SJ74nr-iZ42Xn89hPILKgkbwJG57J2Nv1BCgDxALqlxf2mFJRFopn7hE-r9gFlm74Fg4iIcpzdXXpq1X2UHMq-yELeWW0oVSsrIeiEvD6dgKnDfXK3R3yBZx1BBqJQZHlTr_OlEUdtxKJpA-ht1Idnup8KgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=pd6RUZsKWRAVHVLF_ULIrwLMIpH6B3XxC1C0j3Acf9LoaMMFiZrs3YzHV8BWTEtV1qre7gf4KqdErDfaUAUHQjjgEKd1_8wnEr24r3dD-8iTPj70CCe-QFObhsEKcxuxH6nWkGbXcNdN3ki3eieloy0gA57rAZEZGzkZbUcY2VIhmenmkUHwHQS0u2SJ74nr-iZ42Xn89hPILKgkbwJG57J2Nv1BCgDxALqlxf2mFJRFopn7hE-r9gFlm74Fg4iIcpzdXXpq1X2UHMq-yELeWW0oVSsrIeiEvD6dgKnDfXK3R3yBZx1BBqJQZHlTr_OlEUdtxKJpA-ht1Idnup8KgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
در شهر روساریو، یک پیراهن غول‌پیکر به عنوان ادای احترام به آخرین بازی مسی رونمایی شد.
😲
🇦🇷
این پیراهن در مقابل بنای یادبود پرچم ملی قرار داده شده و روی آن نوشته شده "Gracias" (متشکریم)، که نشان‌دهنده قدردانی از مسی به خاطر تمام تلاش‌هایی است که برای کشورش انجام داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107930" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107929" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tupmypzFUwKOAKS0a_-J9SAz9ZwBfr7yUSxeoqPiaAzsafZ7yklvZadTfVsp97IG7DCbA4TXuPtb8yXDVmm5rXCGChnl-Nx6mbhkUGIbviuecNx_dfbDBK3YUn--Nc5Xz7VlYJlKhPZF8SBRGaLSfQux4FSJfqqvvYZsPz7heik_5VCVggATrzT1IoBpVRtJtyj29JuHreWMVSIwD6MdFBefedbs0gNvb5vv2yVhPH_f4zAvEB_TN0gpGe9NY9jrgWl2dvuO9_zvewJR3GaBqIx93PdxZphKOemP3U1l1q49ER7FRNMWxxolPdpVu_ku7ccmTIgC9krK_CRmfWMG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107928" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=YxiEDqbA9kycTKJK2-O9issIal043IcJdzewS2gf-AHhK3N1SBeG2V2LhYa7Zk6sAGcDX_63jnNy10mnzG9K8cQu30cziBH9qhfYAnomMvBP9OFvLnA6tTVAQ0Tx6HI74XHsskhpJhwW1zuSouyRMVYAqwY8tId2B90Zf3KTZGUX_Mj0evlUxLpgQn7k4oXwcgKDtSMknCSwkzUbeAp5EALoylXttx0K7hrJi2_BygnWY7y54KDxmBRsmIcnOn98Mx23xfZJ1E3LMFONaAQ1hKxVl9NK72AiK5DIIiqtHz9Qjxq8dB13ESChzZH04nADmkwMQTTXQa_J4MwEzOuc1LAO0yv1tmHNpFa2w1BToOSMkxTcMzvmw4-sFTEvnYE8KXEWeaSBMFvMI7-yWRukDfIfGoQG_D4ON8OxK4GNa6HwjPQdKvhw7tPFHJt8QDo-2RxXb81kyFvWIqUPuRIEbTM0XCz6B0CE94D39xlkEfjF9UjQSSWP9NSyspvfJA1Y3E794yXyJOt3ctRyJaW-nS95roq8lJS2X_bRluLoVSsZT2q6HQgTgBdj4A0kjfnN_4SXxFnlUTGVtnPGEG6JmOfS7hfDl6_Wee1PZGqM8F4RvZ1ZePy0CyYnZj5jNkf9ECz87E1IVEwHXrAN2n0cwkbw5_H6Xq2F0Tj4qf9-igU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=YxiEDqbA9kycTKJK2-O9issIal043IcJdzewS2gf-AHhK3N1SBeG2V2LhYa7Zk6sAGcDX_63jnNy10mnzG9K8cQu30cziBH9qhfYAnomMvBP9OFvLnA6tTVAQ0Tx6HI74XHsskhpJhwW1zuSouyRMVYAqwY8tId2B90Zf3KTZGUX_Mj0evlUxLpgQn7k4oXwcgKDtSMknCSwkzUbeAp5EALoylXttx0K7hrJi2_BygnWY7y54KDxmBRsmIcnOn98Mx23xfZJ1E3LMFONaAQ1hKxVl9NK72AiK5DIIiqtHz9Qjxq8dB13ESChzZH04nADmkwMQTTXQa_J4MwEzOuc1LAO0yv1tmHNpFa2w1BToOSMkxTcMzvmw4-sFTEvnYE8KXEWeaSBMFvMI7-yWRukDfIfGoQG_D4ON8OxK4GNa6HwjPQdKvhw7tPFHJt8QDo-2RxXb81kyFvWIqUPuRIEbTM0XCz6B0CE94D39xlkEfjF9UjQSSWP9NSyspvfJA1Y3E794yXyJOt3ctRyJaW-nS95roq8lJS2X_bRluLoVSsZT2q6HQgTgBdj4A0kjfnN_4SXxFnlUTGVtnPGEG6JmOfS7hfDl6_Wee1PZGqM8F4RvZ1ZePy0CyYnZj5jNkf9ECz87E1IVEwHXrAN2n0cwkbw5_H6Xq2F0Tj4qf9-igU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
آنالیز فوق‌العاده سوپر تیم فردوسی‌پور از مصاحبه‌های قلعه‌نویی که واقعا عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107927" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=b-whn_oFvYMvfvFpoD42WLqjUYjKmA9R0rlRUOVKlEQNAdt4-_GtaCTAKc8lauVzTdQz002UzyWsnGoO9ZTlcKdrNeoIaa9EeC0sZlExolnqkpe1QKYrLd8f2IjNFggqlno_W6QkeuSIOt6heWhapHiF9JssjGJjSAEmLAoc0aLoBu47lv0qFlMdqCLflhzlln-tnVl6zUCR_C_ZIKCtvszIBnajYra8AF2WFOURSS5POa7uuMdN45JHjGrbysoxD-gMjk5znQHuScmprz3UXhC4MrPI3B2qq8h-KIqKi-FJFzO3Kucu-6RiB8RahA_5gCFTMrVAT8g-hkWLf4fB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=b-whn_oFvYMvfvFpoD42WLqjUYjKmA9R0rlRUOVKlEQNAdt4-_GtaCTAKc8lauVzTdQz002UzyWsnGoO9ZTlcKdrNeoIaa9EeC0sZlExolnqkpe1QKYrLd8f2IjNFggqlno_W6QkeuSIOt6heWhapHiF9JssjGJjSAEmLAoc0aLoBu47lv0qFlMdqCLflhzlln-tnVl6zUCR_C_ZIKCtvszIBnajYra8AF2WFOURSS5POa7uuMdN45JHjGrbysoxD-gMjk5znQHuScmprz3UXhC4MrPI3B2qq8h-KIqKi-FJFzO3Kucu-6RiB8RahA_5gCFTMrVAT8g-hkWLf4fB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👤
👤
حمله عادل فردوسی پور به میثاقی :
تو که‌ حامی قلعه نویی بودی ؛ آفای محترم لطفا رنگ عوض نکن... الان دیگه حق انتقاد ازش رو نداری...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107926" target="_blank">📅 17:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyYmKuw-05uVuTWb0hhKhK1tSkxEwBgDerkCzdQI2ybgZ7UtX0MPRB9U0NiPBsWtzKWEJU1DGgFvfwxYWcnbVm2o5o39pN2ije0g68cmNvkZU7ksRZ3-aS9lwoYu9ilQkZy-lMYSuxNuqw-xUgb-CLfQRL2El_bSft3hJ9b8n7gGKUU9moFuS5qceh7gqooO9S2Pfbqb9HJSQkck3F7EoubNUDgLnPD_HQU91_Cuv__aVm2UCoxl71E3PTWG__C7vseY9_AoRXSBRgFFUCJmQghjNZzm_qpCJ_0hbSsmiiAXYOycjp34b0BQTNeY3fzaAYDxCKzZfZVF2pNuUB8n9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
آندره ویلاش-بواش، رئیس پورتو:
🔻
برای مورینیو واقعا حیفه که بارسلونا تا این حد قدرتمند باشه. درست مثل زمانی که اینتر را ترک کرد ، بارسلونا در بهترین دوران خودش به سر میبره.
🔻
اما این دقیقا همان چالش‌هایه که مورینیو بیشتر از هر چیز دیگری از آن‌ها لذت می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107925" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مهدوی‌کیا: وقتی شکست می‌خورید باید پاسخگو باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107924" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=BrVLneRmy8OxAPcMjAN7uZdaJBnrSkITpSkaouWI0L-Gz4WcKdKVQTUlLCo2da0nJsh3A2J7QjTis2JAblrNzpL4PFlqXWiGEcGG40aCWMG1UWN6ibUHNmm41mkVotvqLRzk45tYNHv000UU1Mbq9rjyptP8jhBuwoJQuTf26rm9Uy6dq8tkLoB-Tcz2stBzLCDBZpYXR1YrKxXM94N6jFQalfEVKm7_NDXFK5VHpDk570Qa8N9VPA5zKmIa-IPWbb37WGsuMNr7RYgLSrzlfOE-OnCtgipDFPqT1xvNxbfF3XvMTi525OPLhs5L1t1JrOY96X7CTei1QI6rNBTLB4Y817P2jv4czdTNYI8KzAJxnVN0Lkkmjsa1Nib6JxQ0Q_2KBNuBeOay8MIks0M6WpjZQLn-0lKvfYZC-exgLGLB52oy1hGaaAdHQyTyutWb5s1CwWBOu9IOixyAPNG4xaWgPL-oK47U69crDHi8j8jeKxdz5mMoVofU4V_WZ2UokzjYdr3hNKSPO8ZCxtFw7vnVBxpmSYNmmbQU_6vMpBDTIKniVnAFhjm_YLwgIDaearxvrR21cRus8QvRwyL3j0vW584G6OCbn8_EvuF1g3qGuKPCCM9LQfOlkGyjcj9eJSHMqM0aPJOQ4jU0AEBW0N-o_FcdXw23mNc5LRXH1Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=BrVLneRmy8OxAPcMjAN7uZdaJBnrSkITpSkaouWI0L-Gz4WcKdKVQTUlLCo2da0nJsh3A2J7QjTis2JAblrNzpL4PFlqXWiGEcGG40aCWMG1UWN6ibUHNmm41mkVotvqLRzk45tYNHv000UU1Mbq9rjyptP8jhBuwoJQuTf26rm9Uy6dq8tkLoB-Tcz2stBzLCDBZpYXR1YrKxXM94N6jFQalfEVKm7_NDXFK5VHpDk570Qa8N9VPA5zKmIa-IPWbb37WGsuMNr7RYgLSrzlfOE-OnCtgipDFPqT1xvNxbfF3XvMTi525OPLhs5L1t1JrOY96X7CTei1QI6rNBTLB4Y817P2jv4czdTNYI8KzAJxnVN0Lkkmjsa1Nib6JxQ0Q_2KBNuBeOay8MIks0M6WpjZQLn-0lKvfYZC-exgLGLB52oy1hGaaAdHQyTyutWb5s1CwWBOu9IOixyAPNG4xaWgPL-oK47U69crDHi8j8jeKxdz5mMoVofU4V_WZ2UokzjYdr3hNKSPO8ZCxtFw7vnVBxpmSYNmmbQU_6vMpBDTIKniVnAFhjm_YLwgIDaearxvrR21cRus8QvRwyL3j0vW584G6OCbn8_EvuF1g3qGuKPCCM9LQfOlkGyjcj9eJSHMqM0aPJOQ4jU0AEBW0N-o_FcdXw23mNc5LRXH1Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروژه‌ای که هر روز یک شاهکار تازه رو می‌کند!
قرار بود با عایق‌بندی سکوها مشکل نفوذ رطوبت و آب برطرف شود، اما هنوز هم آب از سقف ورزشگاه آزادی چکه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107923" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=l2nkI41qSVya_SEAsT0TxT-vT0iEv1Xi8qWOCjaPGFuo0IAvKB-XLZ-2y4JriIP2nAzjkKy4sCjufTHHcFMmrvx6WcWrm3SVtRyH5VBDKLDlQ0-ZafoiS-FU5LwXxPdcQxGt1Yl-ahKWE69Zetieyp3mWu19MpheBMwO2NkvSFsdm-bxYFWBmjdA3WFQdjKlHEzDbE152VHwB-U6r0JdersPUJCXpzIOZws9U3r-9DQHdUwk07lKYtiK8rpVXzUZ_skviOYMs_onZejilCttF56s_14hcZutZgDUkK-VYiPgRybWVk23nuosaF81i_Id9qj9bNmNEsLCFPZx3Bmmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=l2nkI41qSVya_SEAsT0TxT-vT0iEv1Xi8qWOCjaPGFuo0IAvKB-XLZ-2y4JriIP2nAzjkKy4sCjufTHHcFMmrvx6WcWrm3SVtRyH5VBDKLDlQ0-ZafoiS-FU5LwXxPdcQxGt1Yl-ahKWE69Zetieyp3mWu19MpheBMwO2NkvSFsdm-bxYFWBmjdA3WFQdjKlHEzDbE152VHwB-U6r0JdersPUJCXpzIOZws9U3r-9DQHdUwk07lKYtiK8rpVXzUZ_skviOYMs_onZejilCttF56s_14hcZutZgDUkK-VYiPgRybWVk23nuosaF81i_Id9qj9bNmNEsLCFPZx3Bmmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
✔️
صحبت‌های جالب یاسر‌آسانی پیرامون فرهاد مجیدی اسطوره باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107922" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=o0SlBnrcbHzpXKcZKzGwenKBWonuuZwXCBKwM4wYOXrbbcX3XLWSgVR2LQfEYXXo9kQtSw5q35AQuDitDazAO5YYsGxp0HpzFKDcVTw-C-mpSbMcv1XD9OjRciWd1f-71leWXVRs-n02qYPGl-xT8YdnPA_q1mG5uVY_4RgGALdi1LAfEb7-hdqR0rqBU1L4LuEs41H19FhWgGYILS-w3sODrugjHcS6jLPilwE_G9HgSTK_aj1KMFJ-1r3EkvoprVhXbuZ31g7UbVI4Hzy3J3UHvndSpy0V0T6zSmykqRWMfE7l1-6YpgF_yoHL4Zk7UXY3_ROfdTgIqX8Ft0y-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=o0SlBnrcbHzpXKcZKzGwenKBWonuuZwXCBKwM4wYOXrbbcX3XLWSgVR2LQfEYXXo9kQtSw5q35AQuDitDazAO5YYsGxp0HpzFKDcVTw-C-mpSbMcv1XD9OjRciWd1f-71leWXVRs-n02qYPGl-xT8YdnPA_q1mG5uVY_4RgGALdi1LAfEb7-hdqR0rqBU1L4LuEs41H19FhWgGYILS-w3sODrugjHcS6jLPilwE_G9HgSTK_aj1KMFJ-1r3EkvoprVhXbuZ31g7UbVI4Hzy3J3UHvndSpy0V0T6zSmykqRWMfE7l1-6YpgF_yoHL4Zk7UXY3_ROfdTgIqX8Ft0y-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پشیمانی بزرگ رجب‌زاده؛ باید به پرسپولیس یا استقلال می‌رفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107921" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=fQYoB_5XmTgfieBArqP5asPa9Ialy9Xbxn10zSpbjAuWVTCS4bAOuVJW4GaqnbPVH5kJDSEm0oF3Tu1J2c1a3z60b68yYoev0A4kIbpJuNyo3Jja-avo8R95we-oKFWlzVj9qvp1Hrayo8Ar_TtStUpQrZxv6VLQFCPZ8iXTNi2YIbXaB1xmLTpTW-cn86CX1xXxC1ftOYavWQWC7Kv2ydz7q0E5-UEHKqkMh7cVWX2lyaOk_N0SGnspBp5tubRSOhGWncv6zzXcrbrLzEiCU7YxY6fAd0WFpzDC1D519HzSla_5jlg3niVh4ssgqrzHs-JdfxzUr6uAW8qSxe2Ibw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=fQYoB_5XmTgfieBArqP5asPa9Ialy9Xbxn10zSpbjAuWVTCS4bAOuVJW4GaqnbPVH5kJDSEm0oF3Tu1J2c1a3z60b68yYoev0A4kIbpJuNyo3Jja-avo8R95we-oKFWlzVj9qvp1Hrayo8Ar_TtStUpQrZxv6VLQFCPZ8iXTNi2YIbXaB1xmLTpTW-cn86CX1xXxC1ftOYavWQWC7Kv2ydz7q0E5-UEHKqkMh7cVWX2lyaOk_N0SGnspBp5tubRSOhGWncv6zzXcrbrLzEiCU7YxY6fAd0WFpzDC1D519HzSla_5jlg3niVh4ssgqrzHs-JdfxzUr6uAW8qSxe2Ibw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی سال ۱۴۰۰ در برابر قلعه‌نویی سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107920" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7HmzU-yDL_VXcsQStXOnhWAUwlti3lFMVVXqFVaIi_CmeMRkbBgy07ATnd0cJosLec7TO6PCHunO5vz-ALAq7VT8QrM2Or_svorKrC4dHxTIJhuBM2XP2WL1fn7-d9SAHHWOXvAsVWM911KMUDOLRFUD-lMJ7amE8EqqOTsN4ImeViq_vG2Zjs_FnwSt5ScKeerpsFa4jwKrhHgP2m1vGOb4KKYt41Asg_kkd4EUv57YMy4FObORE-I0adC3VYVidpPUk__1icCnTURD7h204L3cjTeHIW14zWyrYtGwsAudXFee6meHU5udOLTmRolpDNV1B4-MYhfeF_CHQjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
رسانه‌های برزیلی با انتشار این تصویر معتقدن که وینیسیوس به قتل رسیده و بدلش داره برای رئال‌مادرید و برزیل بازی میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107919" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=lKg8TFoQKI9NHuboks3zZmlPZjb08pr83dDAbIFqLOkm-BGaNj40mbyXvsG-9VkQypxTExUdSKc7iiy4fOLqYibNtTWIUmqQeSv3nTf3KBO0WGZT9WTPFDhyFBLAml9qD-WCPp4jn6s3eLE69Xm-CRQESc45UwTsfdHHaileDMhhVvttl0NquWcpIvJL7htL-S8ENUBI86ufUCe4BcNgOeP4SkBgaPRUTGprHVjOmqbU2d3Ig4YJqnYvRKVuTTlGB1UlD4ChX38hszEzIKJ372-mMdV5aCpjAVbFusc_6fWKsUxh4S1FphYT9bJgfcCABx7ZECT9Q_mZT9QJgzwwDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=lKg8TFoQKI9NHuboks3zZmlPZjb08pr83dDAbIFqLOkm-BGaNj40mbyXvsG-9VkQypxTExUdSKc7iiy4fOLqYibNtTWIUmqQeSv3nTf3KBO0WGZT9WTPFDhyFBLAml9qD-WCPp4jn6s3eLE69Xm-CRQESc45UwTsfdHHaileDMhhVvttl0NquWcpIvJL7htL-S8ENUBI86ufUCe4BcNgOeP4SkBgaPRUTGprHVjOmqbU2d3Ig4YJqnYvRKVuTTlGB1UlD4ChX38hszEzIKJ372-mMdV5aCpjAVbFusc_6fWKsUxh4S1FphYT9bJgfcCABx7ZECT9Q_mZT9QJgzwwDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فتح‌الله‌زاده: از استقلال که بیرون آمدم برای مدیریت پرسپولیس هم پیشنهاد داشتم/ تاجرنیا نه مدیرعامل میشه نه میذاره کس دیگه‌ای بیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107918" target="_blank">📅 14:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=Cpv3-0z_-ti5GtDZlFFuXzyWaefgPpe40wATBncMWnO9jGlCcLZI8W6Bab_xqde43safP9JXDo2hnhJLfj8--v6eICYzh0V3MrEeZuglmAFCBRKfzs6x14gQ1N3JIp3-tgb3mLi7PmuLbGP_xm-MFJFk_B9WIvYiz0LJuvdFuAyQ5Y0uAihTFFxHb04d4Q0tP4XhFxNCM4bcQUyR46Ysp2XTFOf-xogYsZA0jM3cnQfYfhKEvTiKKEo8dtvTLXj-e8iB2Cb0NA4aChP-e2Qni-HERBS5T61yoR2sMxsYtFz4-9laRNmwoKZX3ningj4yw4xu4UcsuJwVS6rFtfMzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=Cpv3-0z_-ti5GtDZlFFuXzyWaefgPpe40wATBncMWnO9jGlCcLZI8W6Bab_xqde43safP9JXDo2hnhJLfj8--v6eICYzh0V3MrEeZuglmAFCBRKfzs6x14gQ1N3JIp3-tgb3mLi7PmuLbGP_xm-MFJFk_B9WIvYiz0LJuvdFuAyQ5Y0uAihTFFxHb04d4Q0tP4XhFxNCM4bcQUyR46Ysp2XTFOf-xogYsZA0jM3cnQfYfhKEvTiKKEo8dtvTLXj-e8iB2Cb0NA4aChP-e2Qni-HERBS5T61yoR2sMxsYtFz4-9laRNmwoKZX3ningj4yw4xu4UcsuJwVS6rFtfMzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
👍
تسسترون خالص!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107917" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اعتراف جدید کلثوم: آمار دقیق افرادی که به قتل رسوندم، ۱۱ نفره. یک نفر هم پیش‌از کشته شدن متوجه میشه و نمیذاره اینکارو انجام بدم
😐
⚽️
Channel: @futball180tv</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107916" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8324686f63.mp4?token=ccFUys7fxTkyY4O3acD-XILroO-IUfnC0EYPlhtdlhB1GaFFjfKA3OmjVQqxyXKl4ZTKnStUdwQVr8VOInMvSCzTfgIjbzi4xkPAuLxQ3gAITO2QGJZeOzlKB7DR4VS9H3FBKisZ93ah7geWJfflP2uDGQbOTrk9jII9JOYClM7uFn3ZLh0SoVv-J40CWN3AUezqRO4L8NpkpcJa-xxP3xEwwtCkl97rAbWMtyS-C2jD0yWQmNHLS4okzfT9syz95ao9rO4GIQSQgBdZ7xfiEThNOhzRSDGWw8dA5VOPqMnLNGcDdYVy188hLbOroGCvFduEQM3GwqkG0MCflRArrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8324686f63.mp4?token=ccFUys7fxTkyY4O3acD-XILroO-IUfnC0EYPlhtdlhB1GaFFjfKA3OmjVQqxyXKl4ZTKnStUdwQVr8VOInMvSCzTfgIjbzi4xkPAuLxQ3gAITO2QGJZeOzlKB7DR4VS9H3FBKisZ93ah7geWJfflP2uDGQbOTrk9jII9JOYClM7uFn3ZLh0SoVv-J40CWN3AUezqRO4L8NpkpcJa-xxP3xEwwtCkl97rAbWMtyS-C2jD0yWQmNHLS4okzfT9syz95ao9rO4GIQSQgBdZ7xfiEThNOhzRSDGWw8dA5VOPqMnLNGcDdYVy188hLbOroGCvFduEQM3GwqkG0MCflRArrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس سنگین ابوطالب به هادی چوپان!
هانی رامبد بهت برنامه نمیده؟ خب تو نیازی نداری به برنامه بزرگ‌تر از این نمیشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107915" target="_blank">📅 13:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=bvZoI3YBBJsR2z_mnGwbUZg2pXF2BHOVYO70uXvj4QDGihbeKrMD7tTEQB8SwDqjbLz5JJzUQZMZyOnh7Jal-pC2Z6XRdMsDwaO_IyeevM5zWec36v-1W-Qsr3w5yN5F-TFsWfBJg16-lPigDIwASbK3OUrWOnzyEDGhAsOd5MRUzmmkQapz8auuqyl7oJ3fLvnLY5v_bFf3IF1TYEP7yI8qsYIdVc282r82-TwqJzN5BKiwIObyGCSY9rZLhYV9NVCSgTmSqBO7zAlieWkJ0_A8c9nV5I1Lp4tez0eLrILmDFizOlbMOQtkjl8Bmbrz1i98Ol-7cguYdZz39pcu0k3m6CDK8y6nEqoRPdptfJN8mLCbv9VWFqyJ5KhmWOqRvjeh2ryxAbeTyTzIFFtU89aQleTxHJk1VY0-UZu1-cLDW5TgwsmMhwjqzh6Pfz6ZAuZBPqHcYAGvm1monzAUM8aHGo5Vn_GvzO06sHpNLyHwS6QtbE6i-nrdW49o-bM15_8xsU88WvLK_42xzeMzTHBRiIXyXnJqXqTd7BIvgmK7TMaLvYV9kwKrJypKp5j6DTvBf4s71JgZ1UBdI6t7-irKjnsLnF6AAepqEoyxXewcuLjvBUq7s1-njbEHcjKsibVEELtXBxJcRRS2WdVdQRFOxPlXvX_71T7fYq7K9_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=bvZoI3YBBJsR2z_mnGwbUZg2pXF2BHOVYO70uXvj4QDGihbeKrMD7tTEQB8SwDqjbLz5JJzUQZMZyOnh7Jal-pC2Z6XRdMsDwaO_IyeevM5zWec36v-1W-Qsr3w5yN5F-TFsWfBJg16-lPigDIwASbK3OUrWOnzyEDGhAsOd5MRUzmmkQapz8auuqyl7oJ3fLvnLY5v_bFf3IF1TYEP7yI8qsYIdVc282r82-TwqJzN5BKiwIObyGCSY9rZLhYV9NVCSgTmSqBO7zAlieWkJ0_A8c9nV5I1Lp4tez0eLrILmDFizOlbMOQtkjl8Bmbrz1i98Ol-7cguYdZz39pcu0k3m6CDK8y6nEqoRPdptfJN8mLCbv9VWFqyJ5KhmWOqRvjeh2ryxAbeTyTzIFFtU89aQleTxHJk1VY0-UZu1-cLDW5TgwsmMhwjqzh6Pfz6ZAuZBPqHcYAGvm1monzAUM8aHGo5Vn_GvzO06sHpNLyHwS6QtbE6i-nrdW49o-bM15_8xsU88WvLK_42xzeMzTHBRiIXyXnJqXqTd7BIvgmK7TMaLvYV9kwKrJypKp5j6DTvBf4s71JgZ1UBdI6t7-irKjnsLnF6AAepqEoyxXewcuLjvBUq7s1-njbEHcjKsibVEELtXBxJcRRS2WdVdQRFOxPlXvX_71T7fYq7K9_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حالا محکم بشینید؛ این دور آخره …
چهارشنبه؛ ۲:۳۰ صبح - پایان ۲۱ سال سرمستی در لباس آرژانتین؛ رقص آخر، قدم‌های آخر، قرار آخر
🎬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107914" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpvWAfxLbQxhJU6iqE_N0Mby-HPSwHdLeca--rZxgGUTpib5yakOd1se951C4vR_1wOv7In2KeO_Ua195-mbriTkxkZhhEV9v4lXFtGYNetB0U3ImeSXdYJPP2iveoUA8M55CLW_7UCDaaY_QhCNR5mjMEo_jfuEiYb1EENN1BqwOpdzZpB1lJAeqGyqgZxhU4Fx-w8H6doiHxiH1UTBPErwZMWT0FDBysrZ1WldUNHOHo9ZiYy2XP4ytP-TauL0p_Q4O2gFzFlAbc-PnJ02gwbBhc1WB8uEpumcvIKi1-S2BPorNVYebTnAKhPsn6cCi2pxQJtdb9YMIZpBVXWycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
۱۰ رکورد اسطوره مسی، با تیم ملی آرژانتین:
1️⃣
بیشترین حضور در فینال‌ها: ۱۱ فینال در رقابت‌های قاره‌ای و جام جهانی.
2️⃣
پرافتخارترین بازیکن آرژانتین: ۴ عنوان قهرمانی با تیم ملی بزرگسالان.
3️⃣
طولانی‌ترین حضور متوالی در تیم ملی: ۲۱ سال.
4️⃣
بیشترین بازی ملی: ۲۰۷ بازی.
5️⃣
بیشترین پیروزی با پیراهن آرژانتین: ۱۳۴ برد.
6️⃣
بیشترین بازی با بازوبند کاپیتانی: ۱۴۷ بازی.
7️⃣
بهترین گلزن تاریخ تیم ملی: ۱۲۵ گل ملی
8️⃣
حضور در ۶ دوره جام جهانی و گلزنی در ۵ دوره از آن‌ها.
9️⃣
حضور در ۶ دوره جام جهانی و ۳ فینال؛ تنها بازیکن تاریخ که به این رکورد رسیده.
🔟
اسطوره جام جهانی: رکورد بیشترین بازی (۳۴) و بیشترین پاس گل (۱۳) و بیشترین تاثیر مستقیم روی گل در تاریخ جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107913" target="_blank">📅 12:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=t1hHCdjfvafZzXKHq27sc14tAiqJzwyLr7RX5iEcVhhhC7aBJwIDfwFfU1MpJXUhLqHlJDocl1LgWBT4B3W9NR-h_LSeF2Zap4N6AKUQaAHiPidaejMPz3uwPKYp86ip-qqasz3MybmAnc37JhU2SE8nJg9sWuuRmT6SZ-NjxTqMJVGgSag5PEp8rvar2JtzzrJHQzSbuj8AG7s73B0mz9kHmZk7xE6BW90o7vEXZFxFqU2i6MssUw-7KeKfh4RtZOf9nRk3wU6e7GBfHQKIY2JUf31M5H28z3H2BGSjFhDVszb_YySB379OfOMd7SMY8uJ5Hq9QwRlC3i5qZ5LNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=t1hHCdjfvafZzXKHq27sc14tAiqJzwyLr7RX5iEcVhhhC7aBJwIDfwFfU1MpJXUhLqHlJDocl1LgWBT4B3W9NR-h_LSeF2Zap4N6AKUQaAHiPidaejMPz3uwPKYp86ip-qqasz3MybmAnc37JhU2SE8nJg9sWuuRmT6SZ-NjxTqMJVGgSag5PEp8rvar2JtzzrJHQzSbuj8AG7s73B0mz9kHmZk7xE6BW90o7vEXZFxFqU2i6MssUw-7KeKfh4RtZOf9nRk3wU6e7GBfHQKIY2JUf31M5H28z3H2BGSjFhDVszb_YySB379OfOMd7SMY8uJ5Hq9QwRlC3i5qZ5LNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
ولی این رسمش نبود ...
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107912" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
آخرین پیش‌بینی خوش‌چشم، کارشناس صداوسیما، از تاریخ وقوع جنگ بعدی ایران و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107911" target="_blank">📅 11:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP7MhsefK1tD5Ykstxkj1cxDLMj2XAkQH37dfAxux8dEbJtmX2Al2snjNlDJPNWKXfucgevcWlfDiy7xKValcUv-xfv1NhDTxAHuTuUILXWowqgxwTX8p3iAsvXOajFlv7whAnyF2RJ6Y17uB45ek6J_wDWvZJm9vo8f8qOOGpxY8pGfJ6wXIti8KLUTvA9S2u__nf4-wOXAfEPn6mjs-6NMuXtvuuPuW_AhZj0qtkUGPEV8QncgN4fdR4vTmvIa5QvMVhOxduvKYmDvdKNnSQhIN1ohLlMauKlJolir_P7vIlh0QjUPGhnyag7CUFq6I9878pWxg2J8rhY9fZCXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107910" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
ادامه‌دهنده مطمئن برای راه پدر؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107909" target="_blank">📅 11:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=idfcy8pAAo3q-U3QmBaJ_nUzeUVpIJ6Rh9B85ApyMuxxFx5kr9ZsYu-AsF-UnPwbGdIgjfhQdevKq6e_U8C0Zx5wtViX7GM0PECKLbMWnbIPHdhhw7cO2xf_lDgfsPRfrqnAg__FeK7cixMjqKHaIiONQm1QAKo40umwUWdVF9_Ss3V7q4cWX2uT4Cybs0tlhAupuLEDRLR6GY6BkWJixN6yHjrB5Nhto0-gkQuqi5V8RxmtxSnKWK32gwsnpHDpTFsXpHF0M3CudbSRCsoLIzdyyYObGQs0MD_-q6k-Qsr5644Y5da35Orr-WCLxs8ueQlbqwIQwHPXDne2VN5A4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=idfcy8pAAo3q-U3QmBaJ_nUzeUVpIJ6Rh9B85ApyMuxxFx5kr9ZsYu-AsF-UnPwbGdIgjfhQdevKq6e_U8C0Zx5wtViX7GM0PECKLbMWnbIPHdhhw7cO2xf_lDgfsPRfrqnAg__FeK7cixMjqKHaIiONQm1QAKo40umwUWdVF9_Ss3V7q4cWX2uT4Cybs0tlhAupuLEDRLR6GY6BkWJixN6yHjrB5Nhto0-gkQuqi5V8RxmtxSnKWK32gwsnpHDpTFsXpHF0M3CudbSRCsoLIzdyyYObGQs0MD_-q6k-Qsr5644Y5da35Orr-WCLxs8ueQlbqwIQwHPXDne2VN5A4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب علی‌ضیا از تغییرات باورنکردنی دختر بهداد سلیمی؛ تو ده سالگی هم قد خودش شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107908" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107907" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG7jLc8YqFmTSYbp-KEMfTrNHA6nl5DOBYv5AdmX-AfUVDuN-ecQ7wXJ3WG4pyQAhVnqf10XWHLUSO3hU0af5P3kY4WqrfcoAuBfliC_MfSAt2eP9m8GmZKb-YcSglh7_nfMzlUO_rQcfN8aHUvvVO5HXzTGWEdZv0JrnElAZamIpJFkVyq6DGKFy9dDU-FvJFkIs-rkycSlvZvdRDNhooPn3MbRN1vD4Go2vHwcjy0yFYAZOHqkVP8qqmgbzrzxqgJZH9kB-HY0FZi4n46hP0jhE4UR3M3CxM1k-yFJ4yofrgVrih9vTVjmtks4nmalM685CMs084jsoM2f-kxJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107906" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=ohNuh3ncDCaA-qQHv6B_gAiN8xIdeFcpxOgq21GX9VvKc0Wf4PQA9b1GVHffUKIQgGMGFPBGhSLg8gNq2YEQmVATp18nAVrhUVZbxkBNO3CcZYyFB9b8EUeH7GgGRBVFw1q8-COSol0wYj0LwT3dZWAO_nkMFrJjV65laKN91xbe2Aq3Qwkp7KPe1yY_i5hFI5evcr68vTW2mtxzI6c5vUIA7PVcqZia0ylKqYjkjcdHfsJBaxMqbr_9WxuBIp_flTbnryqlBa5PvEJQctRPd8CyapZN_mKXlfypsfD4orO5TaGg05eCbWeydribEsNWGWJcy1nVeikdUCC1CVP4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=ohNuh3ncDCaA-qQHv6B_gAiN8xIdeFcpxOgq21GX9VvKc0Wf4PQA9b1GVHffUKIQgGMGFPBGhSLg8gNq2YEQmVATp18nAVrhUVZbxkBNO3CcZYyFB9b8EUeH7GgGRBVFw1q8-COSol0wYj0LwT3dZWAO_nkMFrJjV65laKN91xbe2Aq3Qwkp7KPe1yY_i5hFI5evcr68vTW2mtxzI6c5vUIA7PVcqZia0ylKqYjkjcdHfsJBaxMqbr_9WxuBIp_flTbnryqlBa5PvEJQctRPd8CyapZN_mKXlfypsfD4orO5TaGg05eCbWeydribEsNWGWJcy1nVeikdUCC1CVP4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
محاسبه افت قیمت خودرو :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107905" target="_blank">📅 11:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0ELwcZ2slPaML9HGErkc3wpYydldzf9z1EPABzKck2ZMHTQK8Afl4yCwrPhblZQ31-_XPTYhV9t4OClgYUmFIehNxFl3oZvblKynHYdOk9QdAr4_N0o7h1InqyHjawNKGeVUVEOZ8uWEEjU3hCQ-U_R86CU4yb5SfDU-ZsMxffI6alTjMLs_4QyDQ_g31D_E0zjFbkIG9EkRTsjZTn171fpv_Ounj2lCf3zrtjtIhE32JSIJI83KNyPahdT8XJGilCoa4BcaIVeIGgywVXqsXoHRUmPukyao69xYvbZJKL_S344Z_7HhwdZoy_tWRdmmt2ROVowDd81vJoaNzky8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
بیشترین تاثیر‌گذاری روی گل‌ها در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107904" target="_blank">📅 10:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF6C0l5xhEASsbTbBca9u5ZRlTRayxQIKW6VEhHbSjwXVpmEawfFwUsk91x4xxgj10VINwBEHDpPl9caz3AejTae0OvJ_uuOIzfVTmLuKCcbZT5WON2TUVyiUBnvUTxF07fLqfrDhMHEmRcmE8uU3irHS9mjx20tPvAs_8bGyPisMHsmw62uRfSv4JJHa3_g39ZUaW84Wj39kl7JFQJm2S1NpW_buHmqsfvTZrIC64uoN9VTZ5zdpd0cN0JYPTyHijUWpqFt7ZGJagc0kTfvezqk5QEfBqsYiAIJtFjfpshkIEpUgaK_hsKO39uJKb8fdF8nlYuPhkvrk5ymnYn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
؛ رومانو: قرارداد رافینیا با بارسلونا تا ژوئن سال 2030 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107903" target="_blank">📅 10:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sslu7IOQ0bEZv-D5dZ5vpMRqK9sth1OFmy5uRE89uNfMwwzx-iQwkkS0VThqd_Jj94jcQzfzFLnNt2CMMWNxFodtFbIdIsjCTEO1uOYMGOj4CtWymKpRiOTMrxfD0NbxT0BoRzObzBjugvbKTn7yjcS6339zoklMtwyglTSt2RRIBn5xCuH4qAFTvoKgj2I5bsp888CkEAnfSUefG7n_d51NzJHGdKjYc0JXnooP-uv-n9_Bu8Kx0nBYxRKnLMx3AOctUUCA4s85uAAwh9Vh6AXNWJnWzLKVaWsEEIs5DUbSwBNiyjOCE4WgKcoF4OKj8kv209PZMEnzUfhDgXeDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معرفی داوران دیدارهای هفته ۸ لیگ برتر
🔸
🔸
تراکتور - استقلال؛ داور وسط: سیدوحید کاظمی، داور VAR: امیر عرب‌براقی
🔸
🔸
پرسپولیس - صنعت‌نفت آبادان؛ داور وسط: احمد محمدی، داور VAR: میثم حیدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107902" target="_blank">📅 10:16 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
