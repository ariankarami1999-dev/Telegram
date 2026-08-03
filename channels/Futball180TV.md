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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 499K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
<hr>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7gT1QiNqLKATi9zuC_NKYoEWaM3i9kkSo4OIRWZRf6dcRUZn4gQKULC38QGjqL3OkeqUYuWtH5di4Oz6spTFqYbeJyylV__ZQxWfI5tkraFnLu1Jp3ZaKSnok22ABacQ3PjsPhU9JdnMgdPFJJ2o4nSVWzYOq3dwQBDzUDw48g0yoz-lU7p4GAHS5PH3dn2mJHAG3c7hSLPPuXlT5GxWCUgqsfVC6cKgUZ7-roduPmrGVdrH4JaBbeTrloaUvTYtZYYnqjP0-pu7cvX-D95nRKM1Li1kjsZ2v1zVV31Akh6-daSLH7edKpfaP_0H_tb0HXRO_7H5Aos2zk5gabsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAfdqxt1D6Zv-5lQmh-q8sigVOHnQHg1yXi8TmF9SPn8tTRlM14sgRhREYzL-ugJ_TQ93z7bzqDORE7w-OahFYf-8XHeqR8G8LdiOQj1uU2MH8rGogJykb0PK-Kw7CaVcvNnwFIJ2fMGfpq9fjgyy1PnNHfb_PgF-buAOLPBgUuwOIxtJsexrhDQJREV-jrROq2Gyl53unF1Oi7wC-Qyf5uMDYiRTelEUVXSI81fKHs1KZzH_4fi7IqZigiEs6xrIoj6p3pMIYrVLAb1d3X0xAnwdiI-40c2FLVkIcmJxW4SfGvChriZScr85VxF_beqChRY40wL4bNVYfWf5zhmTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRn9Zwurded4par3QENiQODDuEBbdTPBt6N5MN-WyYGz5si9tgoOOLTfvHtavxvRX1cLUKqz4vRVoUbwjIncxcla2iXPSvaPdKSProFb6r0UDfl3nzVUuwfRNke_t6hsAJ_-iQlttzOi2Ddd3J4IoJFETOQY6xJkQizN9PhSe4SxK8MYSofXWdzckU-qREh59rjE_Z7yrZl5YjHz-ysAFQ78MnbLWFNn_ZT8MqfuhygRgBKGFMKxc22xkkKdUGNxrhyoj5tD5atc4iNszR7BO824sxF-v3Ixcd6v5esM-7T0ngMYz0WA_Fd5s5ZM8920RD6glJPn_tMrBszYk4plSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3MSHLdEA93RxTZRq0k0OwRw64pmHCfntfS_cB8GzQdllWsHAxsfIgqsydAvqMb4WtuEp-38JZGOLVAe9HzsgYSyczClys2HF6W8Gztewc25_OBuWg9zRL-Tt_BMXLyhjWmrMJxULbav35C50gChw_LaXs5xez9xBjD4M1HQoR_gD-aUFToRgtBPLbZ76Se6CgJgDgq_79mgqoBTnWT3UAeTFUTzgi4wYhFXhsyoHbOrpqyeoSGy5BeivgJWp0Y7bbQLzePUcAaL6qQe2QmOFswaQAlMcRW-AvBhryqkuV5ILHwvT9qym042MmfDVmc2xT7HXGKwF51fRx2DMFsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQT9816BZr-y___1Zcl1Nv8owJg4TgzTJdm_12YJ1zOSzxMT3aq0eAdFn9r6DgOBug7d42XJE8e6Q1HQYyEf0h-4wBEsbOUBqxd4AXl-KMmhpo-I9RJMQBHmw0bC5KQ1eGaFLtXSBpm6-WmpMgEHGT75ac0smzcIQsIRWmqa5aEDISqucZdxjjMU6F55mfFXF7039BHFSjipsDMvuYB9C2Aog28KGoPQZQy0QroFmLTUvREw0pnydtjxtUwM_QLMj2ppNCK0hRxRo57NJdgOHK3rb44exNsr_y2TLyrKXR-M8yZ0yOmPXdW1tClkLnFOyFyJXUExMCnfdvUmShKeGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx5XO6NMefhBIwQT-6zEs4rLexupecnmfet_0JqDODeyGwu_n-zZnEiWgTeYg5Z8FXCK1gKvE6mJbQatc0OtHi4CqJH_Tvk1nc49h_OPNL3xpwDpK8mAvN7PbGA2zXmNQcGcs6tVCP7y7Z_RHs9lOscypbcYhzizgtGSz_QT47DbRdtz548brvqfvrNOS72D9WRRwgGk3AS0HJilJE0iL0qMPI_WtbjIT_J-i3j8eLV5MnsbnRaQxd3vGIIRr-zBcYiAnEkYu2LQ1INeRGe_FYxrkz71r5Ljy2bBC-zKPBcjpWWM0PvGHCdwqDEhryH_OmBBWdkbecOVyUr54FBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pXyRH4BvmWjGQB_0vBf3MFFW9OJo4AVDnG0UgRZDjkicT2de07iSyh2Npec8j-DW9-xdv-WvwlFajkgKgprOAhqlIogOhQgUbKmAlqtFyC6SK4XRE_vpr7IlVHb8my5tl9Wkqdrad77Jz488EgLF_MU2d_PZRK8GkDga5z0SfY3Wo721oQ5MDu1PY7GfEgGCosSO99kO3nWBMXjD3QOzVqCISGPH-0DVVHX2f3tUQbutZWFZa4nfVQNwAzhtsXJAzdAe1Ex3ycZP1abvMIuFtWPqlteIJriiwwWBCw_bghrUISDfk_IYGIeoaYlKoIKb6kb44kW623LOvehA3iWC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcQLUGi-Sr88dgpO_s0h2dNKiVzoM-SFk0tcZ8wqnup8yBYjlrMb89N5DMtlA6-5UVLVS31Tzz3yqfQpsNPTZ7N_S4i1psIlfTYeaVJx7PRWcs1nYpETrn92NVBb0_6yrrLDwNswSOGnZykAJlESpr59yiuH4druKRpQXm2m2Y-LxMNdCJOQTeqM8nWdWiCUOx8ww_2h-724GPh5T-5Su3vqjWhkY163KAKG6opujPqDdoGOe2ID-hEBE_uK2srS1JEP8x8-bmxXlfuoXeD-3vx8k_ZNM2tQsvYCBesRwq5CPY35ocnDdP4TQloGVMzVOGFXg6hN5M-8ygw7VPzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCAz7t4jTYD4buu1vpnvFphl5OYcOzqjZPgvcDFQoO7AZAn_mYSuSRnXJW40c8v9usD05q8C3ufdbZBkZDsjAnnG0WV0IDE1UCb-NzaeVPwUKUdFWCSNNMNnQeus2z_zkzz1LkLzBzgVjNEfFTBi_D4n8luokoxcMempvTrwnnbcFSIlKD3zc-DLGFvH6egYEkbCCy-Eu8Z7gR6T5d4zzzmbKx85SOzYDBDvLq-jfSr7OK-ePMBg_W5AVdMDGzCRGHOpZthcpdmc3FTDgy91HudEX-ddWhvI0ql3MMIfx8hYrdlY-Hzfzd-SImwEc0PIZq4UYpzsbnCCiiZtzt9UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEA_HyimysYkoN1OPqa-ySsQ4dkk5VklLOUKLtpc1QzG7BmSHptD5U19EcQOu1s6SjdZvyyZQWS1HWYBaOtG1xSIebTkOZnEFVXVro8oB4mHuu8xtgLWBA-IHkWcYg26OOWvb9Ar3zIK9auFYwAaP2I2psR2BrwSRYiJ8kccWVL1OKzL0UvI9I2LW0d1A85ctSWkU1GiO9RYuPNzEsyc-awAS3hya-DES8mwUbxx_XFBlL0OKoKtr5LUOzgJ4gNMr7e0MaUAFX2Gwi27ygNoB7fJjg5EaZQJ2yvh_beT32qtV_3CmwtgZIUB4yv7CnOVQLPItLU1w9-EltcVauYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwJueIpBSmSfl8eoUsIt-zRLfMN4oB8zQuiWMP43Zl2nJYPtRQ6Uq6p810_sF7X3Nrt1GuYB4GwCPLpV9WQtJNQf3R2E5jOZKGWq5mOvJaQJnPghuTmG4M9ix3RzbE86ewLtPtAqo9CVYt_BFH-ctDXgNC-3GdkGQSokDKDQiM21IQoMKkl8yPdeTH852GmO5NRd3gaLdrOmY4BcH58JwnwH0RA4K-eIydwUx0dHRC8YgfApXnO6LZ9ylELxWlXu45xEWk0okOUx_cgrBuFYp4-SammqTjC8AAq6M_4jLX9-0VL_OjTJQcDuaW41f2kTiSzMFb1kYbEjq4iY76ullA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnyKCdiK8cxNLPDT-sk67osyULAR2zL9x8tMjkF0zGr8wuScyby8nG-0-SrZ2V2lUZwPn6mj3lRtJgrCiC1_nFZfi-K58kunEaDJG5ierYotCfOQuoXy06Vos-PtOJ488RAmMklU3S2qVJt_Gz99j2Tzg0637UgCRvWlV_2kAgKs_UM4ufDoWSSeTSCJI-R2eg-eVL8QuzIvK-eMNNiKZQlB2C0THI09aWd66a69WMVwOoCv6ZF7Uc1oq1-OSu2YpGKOJVbIIxDnfTe3qWDkCHhLmAg_nAEHokzuL0rl2znD_r-gcxZFQYGJvRcLMnBPraKQ1-_5K8U22npKoKbfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkR0Ki79ECeVNClilmNuAe_9pBUNs23aF-nB-tSyGtkVU2Rg-FdMEcAI0ALm2UJ8VpcmrSXa5bHJS6_tbqMtGPkkEM5V9tjxg1mGv1TvYuctK_cJvoT9rRWKjuc37yjVh2XbGKXF8zpKh-P7S_EUCJEXaizgEGTQWzU9by86fTfzwQHfSLMUa6-HWraS6TdUS-XgqGD0dqwG2LQHB7cEjsPNT-qTenT04xvEViwZ0x43jaze6HsYt1JD8U5QVBWZmvSaIlUO7K_EMvbz3PF-Ym7BCDZ7GGGC_GUgO-_w4OSe5dBL4iJogotK8qwBd-n-AwaR0oCq6raoqNZycRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2j_5JLWu3ShREelKFxbUNpSKUPq7ksT2BSTLeQFP7Xnw1sn_U6R_Ig52OE6gx2uTTfdRjl5F70GVbuTQ7He-4Nzh_43iGpiMZKj7aXKyq_IQj-BRaNeDCMo-UmQ0H2uL6J04YzAWvFK-hif3rO0KZmGP8TTfe1w5f4P2oXTCLqNHWd2fCoAFaiZZsSs78HaR_C9NGIpeA2hlGqb29-nfdD_UUnWtD8RRk5gMDUNQVUVlbjgEaMeL7-ViEDWNJHnIAKflE7PhgiITqQDoOg_k9wQsUNYaLo-T86eIrIGDwPaC5fAKI04ze_tiT9PEag1HOZUg3EwhKmiaFDEZx6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30fls_VuilR6tSDXxrcEZhtFqqztCGRfLraT8m7ZP3y9F4wsG84_s0h0oqQXbsWgIV9m2FW2JYou26ODDJlOHAtMJ7HjpRSUAaUEojWjke_n57LBS4UzZoCaoiWDrkxoheqcNoTR9qd7IXKtXMecnxnaSTGPiN5zHGmroJ0osANIY7pZLPeG6TwF8_WgNpJ9GCUY0nvyoj_EArXIZAm9ABuYy45UhB4IvCtGpP8ZPwJeh5KhyQiw0d5GwGFncqqGWwydNe5Xs1Y8DMXUNBwp8fGC-kHU0hv_56ILIeUjbjNupRQd7H86dXKmXwFOTpwR8hJdTWnU60v8XXSDpwUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjul3lpHp3q7ENDfyKmZ9RrIwFbbTur56-t1N3olLUO9EhaNJCcoehTtJbjBr8czMXgj1qVa9Yvt0jAwHYlfF_OPlLaIE2N3viOWLbQHBf_i8ftdcPTSHLGqjFcKx1r32qLc7Gl3hwGDf060fUFe9T7iWzvJ1EKNSDwvjDrtKiWkvZrB-27MJCbuRtJXpLa6_s-TBLXlMGYylrJfUX8apAZgcvOKzXxHXHiL0C3h8Qu0Vm6obG9StaS4hLAElthIYyHu-6GL3aISzomcgSOTZ3KDJ0UFPLSfoA-Y00P62Vx6qDFYrrbjmRmopjD5ZSXCUWl5duo12scqQuFTm-M3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUFBCnDvcbB91E7_KyoHpUsZQrVfXsMiIv8ucHrts4Cv_yb8V3Ll5LjdhVj6t1bhbrTuvRUfyCJdhyRJrt48JEKhwLMG9JYAEmR9vkXfkkxjeU1C_2Lp6zWlptbY6tPeg87VSKCPVAajfCfQquoDUsXIU9hyBiuH9KAYYDekf3ohB9FZihlBR0opuIUHJYvLtnzT1vhgjANj9C9LpqNTD43juxzLh72t1yb7rR8obVtGixUshS1Lzfe3cTruUD_dPlR7aDC4ySkBowv2l9_H7hvpX5uI3I_hSmeb4mHfghFzomzVUswjDsLrdEfAQCimYucABbXZXoopBs8FipoPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBZqillcVD2_apzjoS3sxrYxxM5Ol0rGWdn-oS25qFsEM6tHTXXGbmcfa49jwYBe9fk8_m5RooMXkNAj-DDXivLu9NUvTDmX4D4TezlHgSDmnKLL_xRPJSHMYCGl37tjpBRx8ZpRDtKsKLal_XdWDni0VFBKvPVtPaxWJVQUO6tzoL2qf7nlmngLqqx9BLxFwamrw9YK89u-fsHrlRqMQzqxBKV_CrDyEg051_YDQdDAtDYpV_5gMmyi5thBBUSmu2x9oGAhLIRIzTm3rp8iPPUvAL3Jws5vPnk7k_X7v963k1CxVelRb_9nJD0IR0hA49OalXZumDkyPDH31j4LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5GPY5T7G4CTRsrUQlWEvL11gURgwoyhZ0qFAHDt0299BJ3tcipUz2_GrRe0m7fa6ZUDwE5wdqT-hlT7YQf3P1ks4DGW49MPvWsD8rfJGEVJJbhGcqMjOU89HQWWj_9IYnDDiYR3fAfwZwh1ymR98RBrx2T1rhg1qIYy23IDKajGzS4507KjBwVJz8OTnI243eb1FAr98xc8oqCPDQa6ycfTXezjEBY1WobHNYmiOwCYbDBNPf4NV0RWCmAY3FjgnZdp_gJ8j9MlKCK0JCuwAmW1iKwiImDdXOKTAi224-dWDjXV__IYp01FL08UMcIOqr0xo3ZFbL4MQftoQzagXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-OzwQ05mh0nQ-PjOfV-RUyKwLPgsUzFzl6AjF8bZXhgcNfEC-e_gv6A-peld5WUgbmT59QzIErut_NK5YAQIGDjWklwi0oeLciFug3JRRbZ7w4bsTcHw0biW3KwtoqWoSaY---Lz3wa2VMAqzsB1jxf_9KAsFY3qT1qsHN_oQXhLXmnlt9drvYlYRJvqeBuYkyE65bfsLFe6OQEhiZHfR_i2pZ4bC2b5JJZRMoidI3FXUcNXc_OIfN0hngIOgGaMLO7USFfRPptVgSRrOJMCOQdvsW4f_Hhubf0L58gNBMMdTcvOV2nrtjvLDpFp033l9eI2yvnP27we3p7vCzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvoWGrKpkTncmSmE4W5sgwMFwKGWiTvZR74HxxgMJdeUFSwSt5KdsJjoZ-vybcB0gX7pnaF7_JsP4TsCYaJcevCJ5AvqPR5x547u8EtWLXTgnoDra9uc68ILi5zBSKkJNbM3NEkZRZK9YaKyfa4RyWMmKQZCBYGUKf2rsl9wUWRjNYF5IcmbmWUe4zPzBjdFYd9H4Om87QpSbwduqPLM35rkJf-gWre2btEfmdy3CXkGhQ321qB35sfOtQ4Fj1JNwqn0FsVjhLgg86mXfVeLqDl2wotSqbInAbgMd2fWtQlXihAw4qXtWXeMML5gw8Ca8A3pUGZ_qzvdnZBmhGzjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjJ9-wGIJbb-_spwvzoaqoS5BH1ZcpnUfrfP71jCpgemY21sbywFinPQdlWbQUAAxklVyFTznbnqksSjrjEaF1Ad0u9F4Mz5XQk2awWDXa9agGCbgOSiEgsKLFis_c0qnUg0eEXKdaxMKfxUUws74HXDumIoEVOs7lglNLcS0YxFI-I5sMMvNy8z7PKUdAo1EfDx4ctI2t0_sCV3KzAOqstcgW2MQi-rXs8YzyVydmtpY8TLJ8oXbxqukdFrJ0UOipjofS5D4Q2bx4ukDoF-ljO0X6b0k0kBfB8zt_uDOeKJViFtVE8Q7QpyKfBwtnKX2aFLuhoDaxpa5ChlViZVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC_mDDTRK7WlX6oE3tJ36xn-6aZcVM1Fk4JsTOFEVXo-NwwlUIIp24yqcajJ6Kr6VOyG4NU4SIemryjy6MCJD4iXfzXk74o1adv18XiOWayjXyCBMBjHT1WG1KVUDjDzSBVP7jN5DNPHVVQ4KXmrkdpTNTOwRFHFYdCLnMascGcQIsJYAtmyCn1u576CEhndoRzsiP58C2-9nsloyJuU-TKIbR2Qnf4Io9vPwz4HrDZtHwOutLgeKkK5FW_6iNJd2sM5mWFmpMDzdaOExyoahaU-NqK7TFk2uiWPKEY5ra9dJ0joZ0YCJrsz5daGJ5AbwXBywvqmTVngEAQy48KEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=dh_LI5XW1NajRoLnce4LzgxP-3leGaFPdLdDqFZE0b5dbjZw4KG0Q_kmwbQ7qJjoGzR_07Z5SuzQocbnILYyKNK2ijmH-38zywt12L5TGTKxDrj6hY2C3eby55MBoGpJBpYJMi3VGzRoUe2ZwybzzPS0o0D5FvnKrcFYuqeBMyM5-i_F87UgmekhfC3_qQ1iNpj9Tt6pYgXq-ewtZ05sF5IdxkgbIzsm0ZembI9a7IlZ27Ypiv88QPakhx94oKjrqCDAih3M3SypYm3tCi6zlHzGTIjnksNr8IvP1PkUZ0-5UVaPZVto8l7gsAKs4684ImTM4qSwn76677WaljvnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=dh_LI5XW1NajRoLnce4LzgxP-3leGaFPdLdDqFZE0b5dbjZw4KG0Q_kmwbQ7qJjoGzR_07Z5SuzQocbnILYyKNK2ijmH-38zywt12L5TGTKxDrj6hY2C3eby55MBoGpJBpYJMi3VGzRoUe2ZwybzzPS0o0D5FvnKrcFYuqeBMyM5-i_F87UgmekhfC3_qQ1iNpj9Tt6pYgXq-ewtZ05sF5IdxkgbIzsm0ZembI9a7IlZ27Ypiv88QPakhx94oKjrqCDAih3M3SypYm3tCi6zlHzGTIjnksNr8IvP1PkUZ0-5UVaPZVto8l7gsAKs4684ImTM4qSwn76677WaljvnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=Dvu2GnruyvKlAAxfpvwh7MrrbRV966r15AFhnap4bBqVBjuGCB1ZSQKUrcCMJGOcKhxVHlm7FblMRj9Q444Y3gBili3plG_MsCYk_lhezDlCD3OsweiBQf7GAeRV3JD7lVaaMz0TN1eK9apBwOEQAnkHTxBJXND9hbPIM1Be4o4z08HwZgT7MeuqboMb6pxKLuI_HNNnWEBkaxUpUFmGi2fv-2rExmn9hap0PypoWs-dzDzGTLxB9qu-GW_lTwWK-FoNPhoQH23D_PuRxeLc91kV74mmPF9rgfZnBU31aiijtl5ZlK3Cbd4dC4XECCx4RZTDnbD3nWIuo03xcuQ_EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=Dvu2GnruyvKlAAxfpvwh7MrrbRV966r15AFhnap4bBqVBjuGCB1ZSQKUrcCMJGOcKhxVHlm7FblMRj9Q444Y3gBili3plG_MsCYk_lhezDlCD3OsweiBQf7GAeRV3JD7lVaaMz0TN1eK9apBwOEQAnkHTxBJXND9hbPIM1Be4o4z08HwZgT7MeuqboMb6pxKLuI_HNNnWEBkaxUpUFmGi2fv-2rExmn9hap0PypoWs-dzDzGTLxB9qu-GW_lTwWK-FoNPhoQH23D_PuRxeLc91kV74mmPF9rgfZnBU31aiijtl5ZlK3Cbd4dC4XECCx4RZTDnbD3nWIuo03xcuQ_EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kckSvwvlOCuWHe6WV9q843OTFtXM5qkyx4ja5muKRyhuuDnbUoRQtDpiG6guFVAlmu5fQRnDE6n_OwpNWp4Lf9jnX1kcNobZJTDodJc72OCE2_HfCoVbxQXoDtIAqODpHxS0cGss8P_LrBSQ_U-YT-L4IaJr2Ue7ci3JNEIYIPCIA2ZJUCUZe1j38bDJGIKmSZpMb1piQX395JGwvMuJ12kog0wu6dKl_b1_pw91l4kP0mbx15y7TRjxRIKaW5HVEPgf3xxFk9aQDJFl125bO7P68KKlEP11Hgo6Wh4Uu-R6_ACSK9A2tzNUm_8TphCuzg2NEwzgRN4hAY26KRvSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WazBk0aJLdq0O8FZSLz4qeIZfXTYKRAJzR57G7dQ2WrHoka3p7E5N1W-On5urm87T8YhgdcB_DE4xN5bjJgGs3W3XMhIWIYP_uCqDvr_LzOqO8I8-pwKJWYHiXfmjD0la0aRBBHgeTmwpJ9EEVMIH8n0t6nXVSiGFSZpQpXINd7CBg85Awl1Cc6jgkb6b0mZ3bXj2oIKK_VdDYkDqC_6NlZT0OOo_ayn9N2CFNXYjWUeo4CjJpvW_fYfNwMX9mUMsCO2-8tgd1SKdGrCWib9YTFRB8Hka6nWXzPDIV1b9Kb1Ybzvy0jWK0qq7pBOasOrCy3IHaoYE27MzshGLJAZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=LftJnTI8OjgsyHGsJ9FuaV0CHLZUbBLq9HVYMXr-F3nq5DxQVGHrWMYKbFo4QOsPm6C22jz8K4H4gWINzWNrzWEyopS32iq46bOqAy1XKO8va0qSwFUbYNYGWdQ0sSyPR8skZZXjTRuzC1oZ2pnXrpT_Di4JYbmS8SxwZp9pYLJU6eVBwRKNhbGJ8w37fJsrVMNOY53fqomDR3wH3pMbrmY2xYv5NbEJD2BqRTrWr7Bcv1Kou5ipXxmolURYPT5y7ttXR8Iqel_VkK68o8dBFI_8bmn_dh86L3-Dc4tivU070Bf0r0E5qNYReBVT9nHkpwi6gsHhx1I2kGIvT3sZ4YmU1zRXMb5NmXUd1tohmhx9fQgVr-sSwsM_L8djujsoAAfNx9sDd2hkpUnYbwqPOJWrA4GqT5DJ9kuv4bvXJRoFyi04MreRxHwo1nnEtekfK3Ut1bROfVOLnSBPvpwyF3vFW_I5FV6-aoeYyJ-s3M4J8kyMptvc3b_CqFIcZRWfK38WWqgTN_4ExArcBlgs4M4IHpWgriZtIGmmaCIuKITcdIjTEJ_WiEbzPSaHIsYDgdX1tzeMebepD3x-p_kEPrmRdGZGWB_qSGjEa5NcMsUQ5RDRkh1xzCt493cSsCT0g5DPbRvcPq9sRcWdU7EGNY5QuKqQLV6C90nOcw2iSWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=LftJnTI8OjgsyHGsJ9FuaV0CHLZUbBLq9HVYMXr-F3nq5DxQVGHrWMYKbFo4QOsPm6C22jz8K4H4gWINzWNrzWEyopS32iq46bOqAy1XKO8va0qSwFUbYNYGWdQ0sSyPR8skZZXjTRuzC1oZ2pnXrpT_Di4JYbmS8SxwZp9pYLJU6eVBwRKNhbGJ8w37fJsrVMNOY53fqomDR3wH3pMbrmY2xYv5NbEJD2BqRTrWr7Bcv1Kou5ipXxmolURYPT5y7ttXR8Iqel_VkK68o8dBFI_8bmn_dh86L3-Dc4tivU070Bf0r0E5qNYReBVT9nHkpwi6gsHhx1I2kGIvT3sZ4YmU1zRXMb5NmXUd1tohmhx9fQgVr-sSwsM_L8djujsoAAfNx9sDd2hkpUnYbwqPOJWrA4GqT5DJ9kuv4bvXJRoFyi04MreRxHwo1nnEtekfK3Ut1bROfVOLnSBPvpwyF3vFW_I5FV6-aoeYyJ-s3M4J8kyMptvc3b_CqFIcZRWfK38WWqgTN_4ExArcBlgs4M4IHpWgriZtIGmmaCIuKITcdIjTEJ_WiEbzPSaHIsYDgdX1tzeMebepD3x-p_kEPrmRdGZGWB_qSGjEa5NcMsUQ5RDRkh1xzCt493cSsCT0g5DPbRvcPq9sRcWdU7EGNY5QuKqQLV6C90nOcw2iSWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=Y38Lmj9XxC2z0M1MmchodaAp-PLBPIgOSEW23FiDAff5Lu5Gcol0FdDxJytrTeByjuTV_hdMTkdvmihqP4OhrS_4cTtl4swFwJPF4aikGRjlzDfpcKMJbBHP09ATvgHwii347NHAwGcytH7On1G6IctZ-f41R34gkEMVVyyKaYOtbuVo68taOj0tLtihauJQjTW7DcNJawSHiBD7gcvdcGWNUueiBlDNWZOL20lkIZUdCJxkfw2_BkE9KjaeRPcNe8x3lBLjyb5o6EUd10vxIMQE-p-GC7-ycPNWwBBYuWmdZzSwCJiUaElUvhjje2YoebG-isHnjZp6oMnUq8rILg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=Y38Lmj9XxC2z0M1MmchodaAp-PLBPIgOSEW23FiDAff5Lu5Gcol0FdDxJytrTeByjuTV_hdMTkdvmihqP4OhrS_4cTtl4swFwJPF4aikGRjlzDfpcKMJbBHP09ATvgHwii347NHAwGcytH7On1G6IctZ-f41R34gkEMVVyyKaYOtbuVo68taOj0tLtihauJQjTW7DcNJawSHiBD7gcvdcGWNUueiBlDNWZOL20lkIZUdCJxkfw2_BkE9KjaeRPcNe8x3lBLjyb5o6EUd10vxIMQE-p-GC7-ycPNWwBBYuWmdZzSwCJiUaElUvhjje2YoebG-isHnjZp6oMnUq8rILg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw8UVr_vZgRCyjKRNwwgfeB9nVjwmj1dKEyYvV_ZiWloqyH-MkkYySfFomfjZxnHNXvsHKkLl4-mVs1EQayF5uUkIECOsQfgUVi6h0txAYnPArntZtvJhQd_G5dPjh-wHRUmWRJRVtCYv8l0gsavgCF8OM9qQtH_iQyBay3wbd78LQfPZRQEd_eJ9XyAUhFPyS8W0mkdU77gM_Oe0KAHMlP5RESDr-2sLQhwvuDGGU7xiCBv0TDMKdaAHDGpjOpIXlbuCvKfD36kMJyZwqLaipCikuJqbFUD5JjWFxzYwtRO2eoswaxYeskLe73v16ENnAiJojZ7iypTLRPJE6BSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go3sqNqxvhB46ewpfH8BTRApA_f7-3EpQtymXf68rCjiqPwuJRnAABDDWecVee2HGJKO9MgVhZjD0s3oQ4bA3Sd0NPjA57uWF5YsCvUKAF8ZkEaMriSij2bG2FFs7UwtaZJBZ1u6-kp6O6aopMzSin2zupsn0Wsc8Sv2uzaPkNRQOge82eqkmVLz3tUiUppeuw4WeOTJFqd-Z4sIYIOf7CEqYY327A25l83Mz4fRiMY3t5NV0ZEEhN5i2_93wvS3vbo1QXKdOclmWbHZiCyAcaOhEkEPqoCzoDRVa_Y7AvRBa1c-DEZF_KfPGMUa0pewN4_TbNM5jhvl81ef0H7Bkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFDUpgahVbKbm94E0Q6CwCBI8g-tGnWizlDCIonKvrCSBvaJA53VNXJUXp7Ui24iv6RTgmaNvvJbassgD1ZKgJcRyHg-WL3TlhZCBExOxBKy1WB18J9UhAZRGaXVECd7PbxWn5AlPKG_0OU96rGb-7DctkxKiFvrwOqgE0FssIDQcqQf0CIPxB7QUzUo2aX3CoG3U0DLYEptJmSSFKv7gA2NoRAHbxsO_kcoluQN0vHgpN4cOxW5dbibcfTIDA5RY7DA3ue8-gccS_ZDmswD98ranfEh2z8zh4KYgzRaISNKajcKDa4OnJvajw9ajf1CHl-W5192Qr1Y0oQJ-KukOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrCeEh2seq9S-blPqFEiOgJmpTkla7AtjwOLCPFevOmDRYfYkmhr6H9DTeqTvzMLBwzvANIj_SF0dyhGJuQexMiJX8O3C3vJw1Ygj6fwEgvF6LMQEia7la_CHUCWmDLFVsxepP_33KmNd-KaSJ_xe1QTwPSv-oxKUAjB37qC4vo4IDNJv5tMPcIdjYy1Cjs9KZCL5L7yrFrKr2VpvYeNiWElO6nFfKNzz4qp-2ddmxz_mvLnAqEFcr84erXeXROIX3QWvRAk6OMgsThx_jz7xtaLRpYg1batKihpNnzdreucb08XM-NUSxLKIRndGC_B3JZ7kyHuMehD92KWW-YSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBPLoFuJJs08EWTx_hJ_XKdY7WK7yoJXVnwDeGZbwz8bIBqTcUdz5tYZUZ9VW3vPsRHVGiVz0HvNAw_Of5G-7V9jdeIKLVTprT7-Z0y-yHx5aojBVIs7MUqL9YDFjz-B7YlKVdiSnxOv0yxCR5S0XpWBS2cKyAVWoBWNYEnCcPCtZu1duRqRjcWfk76lQ3Y53D_dTTkuQScWINJZuVaanHoliD3tBeJ_UVsaWk8KO6rrJHfLM3lvP52YEIQbVhpAXDle0n23XIqWxD7DwZogrlWIOskEidA1ZW0U5mdxDn8Ix28WpX5pRP9Nx9mfS4K1dxa9MrAlxA_05OAe4vg5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBc9fK9f1rQV5XL7kaXhmFM3fiAJEIrz3Jw71VcTOX7lKc5IzaQxKwMHm8r4rQQyXPbMIeEZ9psQe0V4M-_c2G2E5WLwEwQXIXnF-DixVjkLYVdANSwfaqHs1xM1-0jIE5kZI1kkpyQrGD-Rxo6rOjHNK_RCQiYyNKP1ENFqPWc7r1yNVuBNHyA9ePpd2aGd3gQSeselnmXsp38YQfioAmgMHsYL2NWVVYmoz0qDccCMC8695VEc688SMosYi06IXIt0VnrJbqRQo9rHqpl39k99UufR7kIXhyondXU1m2x04NLO7fZ8kwHdtPLt_eKoW0sICru5c1SscHY70JcMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=QE8YiNVKXUkwWuMbDRJMqgI0MtMzOn8VYBCh5CuZdPYglaiXW_k9kovKbs6Esl-JGLgflbrSvELPWroSsIBqkjt0dBTKO0lcVwK80K-tDO88sVctk7PJa3OAXsJ4p5uNyUBalJJGlH-NpsOyNQeLn0kqQscGMgfu0x6pTIFFGcuZxwlErQUdhiVHvz66NZhjCayM3k7c6beu_y6osT2QdDd_uy68TLqZLPJ6_oIHR3kBT-wur8eqHcvXlKlQXC7HRUwE7X7uBdc0DTMfqBtID9Siec1Giln5TLyBFuLNGvSmKpOa6AHXYh5fUTW6ae92ftEuQo-jl86TCK6Tkocqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=QE8YiNVKXUkwWuMbDRJMqgI0MtMzOn8VYBCh5CuZdPYglaiXW_k9kovKbs6Esl-JGLgflbrSvELPWroSsIBqkjt0dBTKO0lcVwK80K-tDO88sVctk7PJa3OAXsJ4p5uNyUBalJJGlH-NpsOyNQeLn0kqQscGMgfu0x6pTIFFGcuZxwlErQUdhiVHvz66NZhjCayM3k7c6beu_y6osT2QdDd_uy68TLqZLPJ6_oIHR3kBT-wur8eqHcvXlKlQXC7HRUwE7X7uBdc0DTMfqBtID9Siec1Giln5TLyBFuLNGvSmKpOa6AHXYh5fUTW6ae92ftEuQo-jl86TCK6Tkocqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=Pru899TSupaBl90nLeX25W478JBFvG1NT0xMotgn4m6KrNXs5lj9C6aXPfVFyyLjgY0dTom7MRsCVks4nqVyo_-QsXz6MYxk8QkBym2EquJo9VsArGD6RVcPySdzPGR6W0WsXhO50pXuUp9oVVa5aVBD7X6_PFEdpkabGC_tS29uxnNuYaTFkVN53lkMfExKAtyHh8FDgVJsLaU8hPmerBFj0dOf_NNXjMgkxwDngKrZgVnHWr6kkR_lOkmW-4sEEdG6isyyhbrrpPmKo6R0-F7S9ZThzas80YwPaKJhqj_GBJv3JfAnJmEImA0E860OPHLP8UEP6hd6LCH-3fWZhzBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=Pru899TSupaBl90nLeX25W478JBFvG1NT0xMotgn4m6KrNXs5lj9C6aXPfVFyyLjgY0dTom7MRsCVks4nqVyo_-QsXz6MYxk8QkBym2EquJo9VsArGD6RVcPySdzPGR6W0WsXhO50pXuUp9oVVa5aVBD7X6_PFEdpkabGC_tS29uxnNuYaTFkVN53lkMfExKAtyHh8FDgVJsLaU8hPmerBFj0dOf_NNXjMgkxwDngKrZgVnHWr6kkR_lOkmW-4sEEdG6isyyhbrrpPmKo6R0-F7S9ZThzas80YwPaKJhqj_GBJv3JfAnJmEImA0E860OPHLP8UEP6hd6LCH-3fWZhzBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyug1ox7xhxjRdMpmjtIEeGQLLhxEkjOS43jZUUCLd53Z6PzK4NEVGvK0HEn4mPKvpqxtYDNx2eOV0WxkeWntJbDMgvCEIdhi7dz1AJDM1-0vaEtZ54HucJRaypLoWEtER1WAe2EmATGw4guT6t9vPjZGbo36B1I3UNhmqOvgbEJB0Cj7tG-oPllC6qH4DUkoEM37j4la-aQvlaH6KK5tgQB4TDLb_ltrRKY5gEcWgO0eKH0C1XQE8lTjaDpBaX2MOC5Evp0kiUyfZGlfDK7SbJQucP1pzwXIPrDHhPzp1cJ1X7zWE7VF3uRzGNx8Hw2Bua7beHTK56VSztR-2shbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mer5KFmH13epgA1nTuqCbkVVjo4JyekTLy42j5nPexFEqNkvNduistIGQImAv1GaEPmqPXKWe7899Ngt6hnuuo_L2CwOdzADqrSIZEVcromm2RmW_r7VsEZsl1S3vmZz9O5ihNrhe1urjF_9uSnqYFetKEXY5vGRmdsM6gSJweDNRelfqGuEN9c4ESlPBtVMnNsSeNyDw1ktacnF6AXQtgV-iSsuxPda85qJdW9DrnM27tLRcKwrNb3_l1qvgrCjvbiVgCu-Kr2dKGmqH20uw769xNMzoInXBgmj9UJQLvZMm8-iLIFX2fVmlIPw8oe65Z7kTqKOJ_Ghr9m0Op-dwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvpLCIV7YgE7i_HITw0T-RlTa9jn2Gd7r-g5lQKBPpxoFkxKgxfdRkARCJCCis4yefuxISCkHzVYETETRIMdEjvx1oud87zw0eeWXoFve9abvrVX-MoYV-Fj7lQ7w_ofei8rKwkmX5vQNq0hbPTSBdBdMGR_uxbm8ivvGZZHCDNlZrQYHCmpDsLmY_YOMYe0xrDwcSwrAId8pIqPBRKDFH6knQXEcVRTDglR_fMxejnHQU_t7TDBqqGScttSgkQsLNHmN8Veeiu94VF6A7XdWejJVP4UIBrASZJiIUeCcKn6YnTLMxEmaZ2HuCUY4ih6a6BuyB9AgiSrtJeA2kQFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEljjt5v8Udo9PSexsrfDefJUd3r7GKHxcFmMWvoGGCALr6le50ABZlfWIBLdb-_2V-lMloJZKgYae-BgOpFw0CCScZBHL0Q0R7VGCN3DDHFNklV7E1r0cUPIOa5g2N8YhAVTeQJPfLEnUZlGPwJWu4Z8g2MtJOfrldxceUG2JhBzCB_dnhku4rmF6_CtjDM3J_qYbJGQo-PvOB6I3VrzfXF1XCxV-GuuVGVl0uOC6T3rD-G7bWmQJe4rBgaAariOVGOpUJKnDf4v9y5optGf7WV_n5gucu-w6m-BNySRZb_CS5132_-J6PK2ggzPCqcAzs3_Ai-bGlb8IwMZAggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=XXGgzRAO23KNFTbmd2pJ-U6D5PATAoHbGZ8hbcSzZnSsBr0bEFkxEd0Gi9F6H-XpjdeTIy0DdAjf9PvvGhH4ui1dLn6JfDwVHFUuVagUxk8zzsQGLR8Z8az1PTwEKqNzEeN596Al4X7OedFMqNj0WwwSAjcypigNjlLRSt0_o5sqtnHdmtEk7rWAal5WODbRrf1toO7pfXD_QXq4a_GK_g8_JVjTT2nTuTWJqkjEv1Zfxn3og-rMdzWHHPVxH6NizOltzL2w43-PpHhjQnPvLhj1MmQ9pBgEniZnFDpf6aOuPqqgHS-W75GDteXAxvSqijOIACrrdf8EScM4mqa_UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=XXGgzRAO23KNFTbmd2pJ-U6D5PATAoHbGZ8hbcSzZnSsBr0bEFkxEd0Gi9F6H-XpjdeTIy0DdAjf9PvvGhH4ui1dLn6JfDwVHFUuVagUxk8zzsQGLR8Z8az1PTwEKqNzEeN596Al4X7OedFMqNj0WwwSAjcypigNjlLRSt0_o5sqtnHdmtEk7rWAal5WODbRrf1toO7pfXD_QXq4a_GK_g8_JVjTT2nTuTWJqkjEv1Zfxn3og-rMdzWHHPVxH6NizOltzL2w43-PpHhjQnPvLhj1MmQ9pBgEniZnFDpf6aOuPqqgHS-W75GDteXAxvSqijOIACrrdf8EScM4mqa_UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=JjILd4eDxHiGpGk8MNQVsSjVcBYcxZdwqYdx4hECM55urb8DRp8uqBPw45N4utINHadmbfcn3cvlUXkVRRSMKKR5rN37Mx0wzVsgjKi40CMPGiRyre5vKObZNh0Mziclfph-6TnSLDMNH3JGcK4lfi_vDH_LbbCMkn0FNC2cWwNGVwvT4Cd2HWsRyDZ5nyhIy8wbUaL3Z2R6KUnyZ2EHUXtd4uCjneaLnCpM4O-7DtYTA6scnwuIejUHq0ZWQXdd0uYSNm-bxwSW6xN_F84NmpO1dnNogy7tX-VkhQlgDjUwyRWNj2M8vO55JSY131CboBWQ6m-F963DKsn6Q0jcEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=JjILd4eDxHiGpGk8MNQVsSjVcBYcxZdwqYdx4hECM55urb8DRp8uqBPw45N4utINHadmbfcn3cvlUXkVRRSMKKR5rN37Mx0wzVsgjKi40CMPGiRyre5vKObZNh0Mziclfph-6TnSLDMNH3JGcK4lfi_vDH_LbbCMkn0FNC2cWwNGVwvT4Cd2HWsRyDZ5nyhIy8wbUaL3Z2R6KUnyZ2EHUXtd4uCjneaLnCpM4O-7DtYTA6scnwuIejUHq0ZWQXdd0uYSNm-bxwSW6xN_F84NmpO1dnNogy7tX-VkhQlgDjUwyRWNj2M8vO55JSY131CboBWQ6m-F963DKsn6Q0jcEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6IHUIJGcUe-8i5JVW95V6t7I8R3i-HRDU7aJgfOpMd49caISkvf3jSCjsWpaAoNeQ1qd8VNw5yxwQzUGkz8kNve9lD5ZjXqRx0ic3xuWXwY7fj0qq77Z1gjbGj9BRHRgKy6urV5XDrbOy8-ID6zyX_SRRax2_oxuxHC9PyURmxX16NnuETt-B5_EDcxY-bAuRVgHXqDOBwWcPdkzVmyPTCdVPZ7pvEJ8D9OCnVbp-ytgVNiW01dU6wFbTQoEZhQHh6TcLGhz9toVysVk-aRX10joV6SP54OA6heVguFlIkFGE70DYYp18XZRwn2bV09TzGHH9IUgEyXI6BkCsAjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZAwb13WKRwSbp0fEAAgS7cfU3kItTrduMx4P09nQRsEVhpwtdnC3kw-tSeq9ry1QLhknoedpEuJoCFSqSXb15u550dtqhF_BT6Kq15ijzjz_wUKDNou7Mtsjc4uRhtMSkPS_JslgJ-CM-Q93af4F6HqCN-9O76J5k5SCcnQ5ou94NejDzE8jnRqpoOGNlOxJs0xHxKcjDl64dcJ9Ow1o3FgE_OAPNIxLh1PoyJaizSRAYb6Aofyt5LxvZgFiWPeGhFAL_1OYHJiOOHpZnqgdYF_h40yXd7A1fF27QBrcn7M70xq2OXz3E6VL6P3HOfNZ-YlAkT5DjKZdMbOJJDDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvypZvi96JSGCCeuw5NhonaLAZb75WqWXCbXroTuPd0Bb0o10C86T0r-EXT0F118rD5_qd0Y40ZCvnGnORwCxzmO0_Ml5Nw6vWr7doutyIfxizlIMSfjMCWbhrywSwd_Qji9EBcftfEnA9CkGVZ8MHge2S-BTVzl-F7JaocrZJGnhNHmHaCJ2C_pfb3Qixpg9PiWcvBes0zY6iWnpg1Yw66K61likYOdSBEnE286Z-zkNhwfG_W-Cgmu5POvyOdzlb8TwS0Rojdg5uKLhjyiIW-d5f_SaPV_3moPZv6jfppPOoOo3xEdU5SKLpfZ0IKBFo-BSEMfIh1vHBNNCXEK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6I17fA8uvZuke0D5lU2C973PEkhTj3YsRA528LuM5JzQeArtqC5Mm9Ud8nDUD9LVNtJCyWdEmJenrCqvyhipMvhf-aF1uTeybziog3XL-f9htsjsXfcBSwPOJS5iJZWXF4fnPgsxPyci7g9Fkal9BDsDSEa9CrH_NPtmw_l9xfBoE0m4oCgmf6xxNz4rGVfQTrWv7WAxEuAV3n5vkZmv5BEn0Q5O69AtvihU7QKkJj5nUXRmz2ybmi728ijg8UWuYeu3t0N1Z5ZSnVLPKIcIT4kkZ7eE6WO-Z23xxSlbQ8aA0MfiA-ZXMFRVr-7M_Xc_9WWi4sdniwfaiu2GxjiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=EIlqcdNM8mmvawxfR3iBX4911HhDSaImd7L6eLdzDlxfDjPzzF_J-iAMSG1WdVx0qRaR_rBoeQWmIfA3B-vLpVV8r573Js36moO---pMP9rkusGEsAnw136bDnLR-90ij-n3FC7BzrmeofG4G37EVLi6mGrz3XHkC4QZC8Zclx9k6XXdCInFmrK-0GwckAZ73MCMhsWgxbObSTY5JjLzbxvKDgdmpivlUqpK-5KhOWkpBqsGkBVNHvLQVyrY-VZkP8P5SLZ8AL1Iw2-BiNV9u1ylOXsZJ9B1P4VJ7isOfHlNz1Hkst0huoNxd82DbWswbDMmcB7dwwXNcT12dVVT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=EIlqcdNM8mmvawxfR3iBX4911HhDSaImd7L6eLdzDlxfDjPzzF_J-iAMSG1WdVx0qRaR_rBoeQWmIfA3B-vLpVV8r573Js36moO---pMP9rkusGEsAnw136bDnLR-90ij-n3FC7BzrmeofG4G37EVLi6mGrz3XHkC4QZC8Zclx9k6XXdCInFmrK-0GwckAZ73MCMhsWgxbObSTY5JjLzbxvKDgdmpivlUqpK-5KhOWkpBqsGkBVNHvLQVyrY-VZkP8P5SLZ8AL1Iw2-BiNV9u1ylOXsZJ9B1P4VJ7isOfHlNz1Hkst0huoNxd82DbWswbDMmcB7dwwXNcT12dVVT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kArzA5w29HJS6iM9bf2hygSeY-ewex1gLuQZkk105z7P09AKxTRZQ8rlf3yhdFLcfrHNOnxx3Y_pT443lhPN104J8Zv8dwii-6TLjlezXZcZmwG1zZ6t7G-3Iz5G_wfjy0OTieXLMPFvYF0HO6FD3iYNRQCbH_rXVlSu0hPYXkZ80LuUSMMxMyg4MQlrqbcGhP_4SbXY5t-Cq0N5VMlO09jyU3WAfcrUPRh1x3p3fPyTG-PeXovrRKfrsUjKFMnCCwDBHaTzrq-yPnGQ-Q9fmCglV_oVegoRJOR6qT16VLGOHIXzH9R-HeJA0CR48GHNA3W1jn3GYpytm10UDYBD0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=S3k6If_z1ujcx2visxJYYykmrNihNZ98l-nJyGuDxUEiT6HJ0S4R1BmTbT0nUD9YoBRQw3R7K36KJSWlID_jXaqmAPpMFBF-RxB4_jaN9iZpdQSvayQBRL9T_q2LhiXWV9eu7IKFZjboweYhhKMLgxEjy9HARtSvjpv_sUdGp-dy6m379yZPE6DiVQY2OAcJVSBFHU2J15WXnRTErPoNwgjdwyFx0OwqwOC7YQu1gk-JChqKabgEDAz8QzNrNP-K90RsYgJ6YMn4XzyJvL7bHmImxppdXvNH7XywH_hdgUuKu-T5o2acwXycsEM-3Vlz8hOJze80WWwaYEvpMD3rzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=S3k6If_z1ujcx2visxJYYykmrNihNZ98l-nJyGuDxUEiT6HJ0S4R1BmTbT0nUD9YoBRQw3R7K36KJSWlID_jXaqmAPpMFBF-RxB4_jaN9iZpdQSvayQBRL9T_q2LhiXWV9eu7IKFZjboweYhhKMLgxEjy9HARtSvjpv_sUdGp-dy6m379yZPE6DiVQY2OAcJVSBFHU2J15WXnRTErPoNwgjdwyFx0OwqwOC7YQu1gk-JChqKabgEDAz8QzNrNP-K90RsYgJ6YMn4XzyJvL7bHmImxppdXvNH7XywH_hdgUuKu-T5o2acwXycsEM-3Vlz8hOJze80WWwaYEvpMD3rzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkD1h64OEgw9thk8rql5eISEsY-TlPOSTjlBKp6XQ56u4TRX2m6ITms-UyNhweSJui96MivVUSsDbUQEiZgGgfIc1gFzd9XUNbhfvuzniHXKXZ-2M_Dl9G4E79oXvti3i5xEJyqkmlp1s2xBiNWYMhui-z6HCNDJugGzPibsHBdYx_xSqIJoc4GS0bZQsKQD1qD1PuK8XLuL5Rvm90o0IAq5ySH4_EYmp1KuYTK3L6CE3FdvHsTlDPrwVZq1wZQ-LO9uWPrEzXq7oe__WtWeEogF8AfbyNGOWHCeFgg6GD6UD78RuyQwsJzXqUBIKnmEm04fQEBQRWQTMbBSN5DdA2bc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkD1h64OEgw9thk8rql5eISEsY-TlPOSTjlBKp6XQ56u4TRX2m6ITms-UyNhweSJui96MivVUSsDbUQEiZgGgfIc1gFzd9XUNbhfvuzniHXKXZ-2M_Dl9G4E79oXvti3i5xEJyqkmlp1s2xBiNWYMhui-z6HCNDJugGzPibsHBdYx_xSqIJoc4GS0bZQsKQD1qD1PuK8XLuL5Rvm90o0IAq5ySH4_EYmp1KuYTK3L6CE3FdvHsTlDPrwVZq1wZQ-LO9uWPrEzXq7oe__WtWeEogF8AfbyNGOWHCeFgg6GD6UD78RuyQwsJzXqUBIKnmEm04fQEBQRWQTMbBSN5DdA2bc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohuyrEpRe6sU3DVlAdp0kAQe4fVvkGBHy2VTwBvV7WcEwmnN6glsPUCrVs-vpEdywcNxtIt78Wge9cYbqHurZucze_BVkm1WTu3sLReNo-PqHHFukH3FeAgZDO08fE5gI6z2XfeGFSyLPTmYF6XYcsNyNK9P1bNoeKDSS9_9lcuP9MNxrc4dtbUKXJ_gjc_VFXmJjPM-9JPKVq6mov0qBm01_77Iq9GLgGcHIthtdP-b7WMkM5_c1p_Geg44yJ9JJpR0CHAytFvZj30GsJALRzxQn-9XV9t__ngAA7w1FFNGxJBXx2kyihpQ0vGDenxI5Rw_yCjlL8yrbR4cvI_KHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBkbFrdasCLu4aVlzZ1lNEjpwpy53pkZv62rGFNb0W65Tk5algFbhswSlflcllxsuMj8jt9Orugpjh3chxuScesFr8shX6yrabuumzHLHCJAL-0RAgZH4K2Dy1C609cM8AWnfdRVezzFm75yoJdDb_zBH-s-uko-wKIlRX5_Q-4gYJfiFkjR60RCMZNeJo-azi_1TbDXRwrkx393LHsGpy9X1TmxDtwwmU1DDiQ_WBIDFWPnG1_a-7Ag9mgMf0mX-zV3rCTBTbCTF1278yz8jf_dDF00mw1NeJFS26JGM7hkUewV8y4hN6D3TZ3lyqcfvh8I78I5mZv6rsy2ntHE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVWF-2tW9KfwJov13oJx7-Kq8RIPOjZm0NbWeBg3rmSe0EDfIe03TmCjIcmOQJb7taWAnIqsay3csit8Tz8VH5w62DtQjW15BIwmyUKgwLlVXK8JyWxoxVQz90_R2boXXVSZAnUZx1A2q-IcPFM5Jj7O1HH3tUlnbgfMdy35zeR0cmfxQy3c6lFeqiXFHW8Pm1qdUC9R3kz0AJR8zMaJS2gbZqHtAYKP5KCqh_Y-7pXX8zUuXdgOLDcwjutIWMtIFqMPYYL4vft94seWsbVrARGvR9KgC1g10poxpV3UbI9Rr78hKjWtcO4MMLlWaFypMoj0Ee6c8GKDz-OvZM7y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgS6jLDIBuPRkNFhnjf-DTYRMTC5UgEl-upaXo4hHvGnsb1cF1X16eiNZVMB1-ExYo2kTIO9aWjQZDT_jPllQx2XOuwrDXVO0XCn85JFtpBqBVzkXCsk_pJtKRR1mgyLgbCtUDK-06XrniiCyo0kK4a2xkYAPn_XaJiZivgR-zxj6Bl0YOR1KBWdpe6Xj7BehmWltoxqkc6-8cUOm0S_dUMobMFxTO5abRrSS_utG9jdy9DDxGcnNJvnaNkT_gS_BJl6_7ySpG8k6MguvpKKcHVprRPBoJd1jpd0o6doxodx7D4WDgKHZlbFNsCKIa9GHcDbthe9V2dT90awEGg-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW6AYjrepm4Wf_KMm5UNEHVdaZ4rQfWhLbDHfG2MIffOf0JLfIyjVYORIl-73UrV5NhIBXhPUrSrsKTxHJHwEdnoHd6LRn6ScqkDd0yITbMFDyaX7_V8fHTGq-gwMP2Y4mTpvzgXFgY-o6gb5Ltw0pkb97p_rgTEmS5o0c7q7Pn9wDO06CwtJ9zvQpLGQK5dlYFN6Mb46Mf-bSMJdlR63oM2MgX5Xg6LbHya5OncDR02VwGKVajX2BWRn83G3NYTigBxp6Lne-BgQDBtCk3s-s3V-5y0yNPcKyGp5XuUj4J32rfbZ91A6bHgG2MuEqFG4_9fB_DJaHnij8UvL5gs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhz_fXnuPUSA3DY0FWEMBZvbr23NcL5T_qFu6ueC0FJD073-k2PbrMAF4hLR91s_q6mmT1afPLTg_UdAS16YY2100dwWimrtrcs2DNwoEXtOODpsLDNSnqF3hGOCQr-98I3Ao5XIhZjL8t_-n5FPrMGPYKgKgd1lLGqjBtUC_hw9Xq0DOp5x_DHukeJKDGtQYoEZchQ-I8hcySJ48qPSxkbD4w7n6uR05IK43Kd0IyjGKyrh4Izf3MtCr8IRgMOhGVlrT5xyXu6__qdm-hyL0PmNp4N6JzSu7yUPIBWvFfGe-wkdP4x2WCXC6ENTGtSr3nIgRZGI0k0Qj-EkdrwADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=tUXlQC7_oqTAWQ1RGUhLG7kCE4x6AcyX22EB4HB3qytlxDPjtxUaxYDudmpZvcPAq9ypGxc8GLXa6-txnNOJ_sZsWWtqNOWxaY7wD5PWk9LJwvYApya2ArjANUe7TJ1yxrSZaYfVJPQmqUa_YbemU2oclNtPuevvPg86kk2NO3-w5BFm1mzS5UUufeKhlRgo0zcSGoox8hdTXBN46bZYQKhb28Oww3gsFskMTuNCDzRLRStBKtOB7gYEmBqjBAEXghatOcRxt84cMynLX8pJ_gyhOldGO5XSVYQIUUEhdSBeGkgF9G-YwsC3dSJtkXLdmLoQn1HpgI4QB1pk1GnBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=tUXlQC7_oqTAWQ1RGUhLG7kCE4x6AcyX22EB4HB3qytlxDPjtxUaxYDudmpZvcPAq9ypGxc8GLXa6-txnNOJ_sZsWWtqNOWxaY7wD5PWk9LJwvYApya2ArjANUe7TJ1yxrSZaYfVJPQmqUa_YbemU2oclNtPuevvPg86kk2NO3-w5BFm1mzS5UUufeKhlRgo0zcSGoox8hdTXBN46bZYQKhb28Oww3gsFskMTuNCDzRLRStBKtOB7gYEmBqjBAEXghatOcRxt84cMynLX8pJ_gyhOldGO5XSVYQIUUEhdSBeGkgF9G-YwsC3dSJtkXLdmLoQn1HpgI4QB1pk1GnBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=bJQPhwTOYysYskOew6ar-3A4zOr8ggz23mUXMI4m8u0pnaj82UZxSgh0RGMCnX2ZC3lnJZkpFuJLZ7PZHUh_GFFY2tOD2rYh2ffpqXQXoTWqHjAkTy74Ef2Jcm4VEXzj8KmT2Ibp1QqbDaQ7YoNenc2Elxvq5sflYX_eAK0PUj_Wua3jdNtPPa8xd8vcKM-ihBm9IAoiggmMCuwNWtoLyQ2Yks3AWxv07RGiV1C4i3pUMeF2z33Q7TVaR9sRxTJU2WlXOhZNtZVESbw-atNDzD8OCCEHKvC602-8AqkIaKbNNGD8O7SDTMQ4buAhVefscYbwdoA6tG2BCb4_yTn8IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=bJQPhwTOYysYskOew6ar-3A4zOr8ggz23mUXMI4m8u0pnaj82UZxSgh0RGMCnX2ZC3lnJZkpFuJLZ7PZHUh_GFFY2tOD2rYh2ffpqXQXoTWqHjAkTy74Ef2Jcm4VEXzj8KmT2Ibp1QqbDaQ7YoNenc2Elxvq5sflYX_eAK0PUj_Wua3jdNtPPa8xd8vcKM-ihBm9IAoiggmMCuwNWtoLyQ2Yks3AWxv07RGiV1C4i3pUMeF2z33Q7TVaR9sRxTJU2WlXOhZNtZVESbw-atNDzD8OCCEHKvC602-8AqkIaKbNNGD8O7SDTMQ4buAhVefscYbwdoA6tG2BCb4_yTn8IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=Kr3CiinvmPu0VmCF5cr1gQxLsExv2YQNZYx_XsofU3sRKa1iovM3n0MihGKVHGrc7sYjXwcU52R1S5K94-2QpngskQGgKTtwLx_-WlpPJEhTLuUrCbHmRIx1H0rweERSbDUmnewP6VHTeHvTY4Wab4tAImHGmk0tBjtMN_SfZ31A3FPcyVkEDx4VhvvzyWT9pwAX_ph0U8kyTZ5kkyTHofNd1kptckyjkckNeOPnfhatYD_TpQZeOtpuYCC5hWHEOelHGgV-7hRuNpV2zidO485GPD6WugFb9KfTglWaw6gATMeZVFwZL3H0D6aZLgQAb4OLVaKwGWVMs3vga4p_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=Kr3CiinvmPu0VmCF5cr1gQxLsExv2YQNZYx_XsofU3sRKa1iovM3n0MihGKVHGrc7sYjXwcU52R1S5K94-2QpngskQGgKTtwLx_-WlpPJEhTLuUrCbHmRIx1H0rweERSbDUmnewP6VHTeHvTY4Wab4tAImHGmk0tBjtMN_SfZ31A3FPcyVkEDx4VhvvzyWT9pwAX_ph0U8kyTZ5kkyTHofNd1kptckyjkckNeOPnfhatYD_TpQZeOtpuYCC5hWHEOelHGgV-7hRuNpV2zidO485GPD6WugFb9KfTglWaw6gATMeZVFwZL3H0D6aZLgQAb4OLVaKwGWVMs3vga4p_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=Jok2j2fX93kXNwS5O5LJgoCgKge2ALl6NGJ3_Y7G6lJClD6iQF4wkTxtOwvJbCIF7FV0wufHR0Y1QBuiAyZonKQ2pxJdJQtTRHVaGZbxC0XWnxr-JJirQZqktPrKpZw63zNiF1AwA2-FTMrqidSQ_s_mMV-KfM21YoNTG1JuZwmJN3sftKuNygciFJS-B4iHWxGzvaXAqrVYk16VwNVXS-12LCLGThWE6ijjr9L_9E8u9G8h9aGugBpwzNJGu1pVqossy7qDwcApxtuCG_TegP8QxxZZ_iWMZs4axn_snzv_L9yt1PED7docO0DtQNfGXe3ekLZV55Xicj_SltDkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=Jok2j2fX93kXNwS5O5LJgoCgKge2ALl6NGJ3_Y7G6lJClD6iQF4wkTxtOwvJbCIF7FV0wufHR0Y1QBuiAyZonKQ2pxJdJQtTRHVaGZbxC0XWnxr-JJirQZqktPrKpZw63zNiF1AwA2-FTMrqidSQ_s_mMV-KfM21YoNTG1JuZwmJN3sftKuNygciFJS-B4iHWxGzvaXAqrVYk16VwNVXS-12LCLGThWE6ijjr9L_9E8u9G8h9aGugBpwzNJGu1pVqossy7qDwcApxtuCG_TegP8QxxZZ_iWMZs4axn_snzv_L9yt1PED7docO0DtQNfGXe3ekLZV55Xicj_SltDkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=l7NahYbAXgqBS_1825O4GirqmXu5erlxbtSwVoyWMVF3eDOEOw4ffh-rQYcqX1UJYvq-18FYFstnPHrqtdoLSDw1gk7tessdBA_dgxuA3hKXu1k2Rk-wbgZZRqfItjp9bixaj9qgwxc93p2K8IZryycd86hilhrq52rvYAhGh3B1Ge7b71rKvbdZ7fDJ98pk4nGQ23ItwUqxzU86YINtjwH-HTTRASLFdtcJppTYMvlHJ4vSv_K9H1bJPAc8uKgsQqQ3xIqx9LXAAnclKS8l3aS5DJWLN1NwOoXZRSy48q7aflwxxAj7XjM9BTHFOyQEa4dhyXnQ6O2CIBWOMZZSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=l7NahYbAXgqBS_1825O4GirqmXu5erlxbtSwVoyWMVF3eDOEOw4ffh-rQYcqX1UJYvq-18FYFstnPHrqtdoLSDw1gk7tessdBA_dgxuA3hKXu1k2Rk-wbgZZRqfItjp9bixaj9qgwxc93p2K8IZryycd86hilhrq52rvYAhGh3B1Ge7b71rKvbdZ7fDJ98pk4nGQ23ItwUqxzU86YINtjwH-HTTRASLFdtcJppTYMvlHJ4vSv_K9H1bJPAc8uKgsQqQ3xIqx9LXAAnclKS8l3aS5DJWLN1NwOoXZRSy48q7aflwxxAj7XjM9BTHFOyQEa4dhyXnQ6O2CIBWOMZZSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=QFqGVM7Z1pIFHK59ZmGLaj0VDUTvAvIhqIoPpARfwrS6o7Kdw4vtuBqeosRgZznf3P1wNfnzlhp0xht9RPziODqhTuUb5OYWLuSgBgwB49K9s5Dq8H-TNDRhKaNIHD6DfEvslaOl1goxeG3MkFkMZQvtg2wwDH9cLcbPZS1IRJECF_0aWl9B7u9kHXvSYKYcb9L3c7_5H7cDLpUZme7CZA201UTG2BV1APqDZhynPmBOBNHUCnBQESZlmghV_u51XrZPrHHHlLyxqtu55N5B041eWS90llJKAMU5eFxvBMatKoJurOhngGozKQsWi_JQt8GX5_O23mpOw_tYnKaFEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=QFqGVM7Z1pIFHK59ZmGLaj0VDUTvAvIhqIoPpARfwrS6o7Kdw4vtuBqeosRgZznf3P1wNfnzlhp0xht9RPziODqhTuUb5OYWLuSgBgwB49K9s5Dq8H-TNDRhKaNIHD6DfEvslaOl1goxeG3MkFkMZQvtg2wwDH9cLcbPZS1IRJECF_0aWl9B7u9kHXvSYKYcb9L3c7_5H7cDLpUZme7CZA201UTG2BV1APqDZhynPmBOBNHUCnBQESZlmghV_u51XrZPrHHHlLyxqtu55N5B041eWS90llJKAMU5eFxvBMatKoJurOhngGozKQsWi_JQt8GX5_O23mpOw_tYnKaFEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=imTZcBoHILzen527h6IYlDGOHNcWETIrilqscyYVirQgFnFQECSXF6xfXOE_64O5h9g6K2zsmMfe0fzSPbubhscpEQP4pLQBzZjOq1iA84qDJ-hzFi0L2eGmhudri0vpOPBY7EylRlprc3WNXBOxDuYc-0DZFyti_fRWpN-XMb4IWGaQR07Z_VCSnsJmSu6CA0i2wlJfeR5VqIa93kxB-6jBIn125PNO7bHgQ1rtJOGTqkJgdOjsyH3pMI5tkWR61rk-5GQ18pfuqw0udtKswTJCuy75Qq3vAC1u7KNNWWeMIGupLHeJ9J1rRcqk3s_GKddgJqREHzzLN_-SaHlwSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=imTZcBoHILzen527h6IYlDGOHNcWETIrilqscyYVirQgFnFQECSXF6xfXOE_64O5h9g6K2zsmMfe0fzSPbubhscpEQP4pLQBzZjOq1iA84qDJ-hzFi0L2eGmhudri0vpOPBY7EylRlprc3WNXBOxDuYc-0DZFyti_fRWpN-XMb4IWGaQR07Z_VCSnsJmSu6CA0i2wlJfeR5VqIa93kxB-6jBIn125PNO7bHgQ1rtJOGTqkJgdOjsyH3pMI5tkWR61rk-5GQ18pfuqw0udtKswTJCuy75Qq3vAC1u7KNNWWeMIGupLHeJ9J1rRcqk3s_GKddgJqREHzzLN_-SaHlwSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FF34jHXt4OjI3DFAxOEav2UB1szUq6Jxpud3GMryGSpfYcv-1b-U8KjjHUmouQsgxKj9cxPsgXf1vMnRSxbuKlI0GQ0cYLoiV1kE8OKU1ULkrMzaiRHtUUi06S-XxW5M0nB-FcsprvV0OTX4ZbWzROvks109026TaFdQ-Teo-AjL1QaSIcjdL1EB2R_XdBNBgy9eRlGWDhvI1AAzDjDMUBcrXyxwPcohZcw_26R43lrKsVyuF3ZMG18YRB6nJYnMAsbYd-RGFDPGc9XipRbkSl5dBQ-amKuoENCDKrZz0Q5bdOI_szGRUAOti1xJgLt-tIPTTYWbtSOHIi7sIGeb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=axXQQRRZGTMYwiswo_JZM5keV6_L4uVcFzazibTs0PiCl9O36yDmM6X2-BxKmJD7BqgqDX5le8Y-2E6BFnh2bQvIjRk_dCIOLQbUeeThYgIYr8FzD8LlS-AISpRuUGocXpqdQaotp4sJx0sv-M6onrCQdu9XSVssOl7050kEzAquAjjq_grdDwqr6sJlkLrBnv9jd2rPujT23AgzXgL8zU9wWU332FY44OoT8fvCR6Y-86Ab6OC6vgAvNqWCwBLKv-XJujo-f2sMeyRI6AgICpoDSo0dlL6f9XvtozDwqOhnIIt9n1LBxwV98Tf2K9loO8vrsG5qU13gIJQvv7Fa0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=axXQQRRZGTMYwiswo_JZM5keV6_L4uVcFzazibTs0PiCl9O36yDmM6X2-BxKmJD7BqgqDX5le8Y-2E6BFnh2bQvIjRk_dCIOLQbUeeThYgIYr8FzD8LlS-AISpRuUGocXpqdQaotp4sJx0sv-M6onrCQdu9XSVssOl7050kEzAquAjjq_grdDwqr6sJlkLrBnv9jd2rPujT23AgzXgL8zU9wWU332FY44OoT8fvCR6Y-86Ab6OC6vgAvNqWCwBLKv-XJujo-f2sMeyRI6AgICpoDSo0dlL6f9XvtozDwqOhnIIt9n1LBxwV98Tf2K9loO8vrsG5qU13gIJQvv7Fa0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk-l_ehF3Unb4aAlWX2Ortvoh7PY2x09bDR1U8M1nB17VrvcfPWHav2GLb1g_ZlKDQ-6w7zo_8S698nlhnEwOzuLfOge5OS4LubEP8XW0vd_MPDzlUqG-KmBTjROvph7zac_3DeoGcsTQFdoMakfqO98HW8MdL_Wt8SB3fy3kY18F2I_ybiMCqfUDmd46xHKeQBAln4nx5uhq-_pSWGMgaValQnJMrKpOWWtVCc9bTF6AtB868zWYCBhlhfeJCTfghk8w_TBevxOXXzResjh5PUZcEVPczCPk8oMV4lAqv3CHnvTRwLBqcvX5JUJhhxTIoBqhFn0tkzTbFU5DDAejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=Yqq4C0mOi_zWktIlihZPYtclhH2Hm0CeVUB2xS5Bj3oEYfSFdEbER7H_Q8DAu9l5C5YfpRbuTn2j3i8xrEKaXdDGzggykazQ8OBlcF3T7LfFt7NL-qZr_ZLMnsaetmSyBJfQoMbssIYEzE5w9s15fU3_3VZIlT0388C_JuAMG7XEouDOE_xbfWJqOD0I4andxmMiRml-OoFCIC5vQe6uwgORWVILuSdmqpugOowOBetFKlTs3ZNV4M9c13QmqzsMgKj6I8LTGmOyEisa5w7ILqlE0kcJDgft6xkNs-gix1Lp1vS-clBDd8GdFWKBD_TcL4h-hMNq-S8PemC6Gz427Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=Yqq4C0mOi_zWktIlihZPYtclhH2Hm0CeVUB2xS5Bj3oEYfSFdEbER7H_Q8DAu9l5C5YfpRbuTn2j3i8xrEKaXdDGzggykazQ8OBlcF3T7LfFt7NL-qZr_ZLMnsaetmSyBJfQoMbssIYEzE5w9s15fU3_3VZIlT0388C_JuAMG7XEouDOE_xbfWJqOD0I4andxmMiRml-OoFCIC5vQe6uwgORWVILuSdmqpugOowOBetFKlTs3ZNV4M9c13QmqzsMgKj6I8LTGmOyEisa5w7ILqlE0kcJDgft6xkNs-gix1Lp1vS-clBDd8GdFWKBD_TcL4h-hMNq-S8PemC6Gz427Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ERZahGI8TSGvwTlhh4OIOY4-VRlCnc7jHRf0Up7G2SAgUCo7tnjKKFSGH3f81I6ys7L6_golXt9zqRTOo2LvV81qKRYxq76sROdUnHzTzLFJLmpt70v9lN9X8t-KpCYr7ULULflAewrQZABFNWsoo5snORdii9oV-c5EFM4NXukIML4NrEhaUBGD-qClsDgz7RtEVYjtKMQNwh_r-yvZIKwh8Xe3C_SFOM_HBV9sCWoVmBU3eBL6nMXr8-2JP-XZMilIFOztIGLDudda6m8ubdCMypvb8t8c25XlZwFgK13NGIbgrpVkIJ1ccteneSCRaF4WVITcr7Ft05F_8jK7uG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ERZahGI8TSGvwTlhh4OIOY4-VRlCnc7jHRf0Up7G2SAgUCo7tnjKKFSGH3f81I6ys7L6_golXt9zqRTOo2LvV81qKRYxq76sROdUnHzTzLFJLmpt70v9lN9X8t-KpCYr7ULULflAewrQZABFNWsoo5snORdii9oV-c5EFM4NXukIML4NrEhaUBGD-qClsDgz7RtEVYjtKMQNwh_r-yvZIKwh8Xe3C_SFOM_HBV9sCWoVmBU3eBL6nMXr8-2JP-XZMilIFOztIGLDudda6m8ubdCMypvb8t8c25XlZwFgK13NGIbgrpVkIJ1ccteneSCRaF4WVITcr7Ft05F_8jK7uG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/toR7Ejdgn0QR8fJcx_YJzLIAEwvh1DzNvEpSyjBUkyKIXc03GDrpGm8LQe2soJ96hSPWThW8PfEjtyL5MTLkkilNMFD991ooApBhrEdJiTG3nfljF96Ai8rqhiuRA3BJ7BE1xLEmUBmx3jp5KCZ5djNjE2dEFdeiu_WpuZpypXt_v-FPFTCPecLmfWQZUjg-29tjiP44FNglMhWjeGfIVWdX3Zlfzram20S8qIiI3VZXAPGNwV0RRlkSKo6b0S9-uiOuPnTcdLSYAutmAFYY4rcyQlZw18y6ptTmgkUZU7Uhv1b8vuzttd51ZPFlCcvC3BsZ_V8B47u05jmEEV4uog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=qvzjlevEp88dH71AGmRloeBJe_uc78gUxq183PhGemAFM8P28VjMpTUW6PDBaK6B0BwxyYAtRmMUSMuNi6y4IbFNm7TtZSXYjwbvuBs0yeQ__W06MfS4HJ9munzYqrygvZsmp19SIaZxYr3UTB55rr2INQypDmxvesPTNnnA0eaKMr5Usk4G_W4ISVWCtz5YNrcVJ1X5fldLSOXOwsyL4sAQ2mHHRftLccl1KMMjetyU8T1slt6UdlCPO_5TOzoPZ-70_0wTy_VXGPETOKObtDylBeIC3rTZPqNk9qldz-kJX-McKS0rOdHdsfYrj2yNdxMde0_iaTz6yckv2x8aKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=qvzjlevEp88dH71AGmRloeBJe_uc78gUxq183PhGemAFM8P28VjMpTUW6PDBaK6B0BwxyYAtRmMUSMuNi6y4IbFNm7TtZSXYjwbvuBs0yeQ__W06MfS4HJ9munzYqrygvZsmp19SIaZxYr3UTB55rr2INQypDmxvesPTNnnA0eaKMr5Usk4G_W4ISVWCtz5YNrcVJ1X5fldLSOXOwsyL4sAQ2mHHRftLccl1KMMjetyU8T1slt6UdlCPO_5TOzoPZ-70_0wTy_VXGPETOKObtDylBeIC3rTZPqNk9qldz-kJX-McKS0rOdHdsfYrj2yNdxMde0_iaTz6yckv2x8aKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxQ44kg2iA6nEUKdacibqvVcVPBehSf22f77ZMU9PhYWSwCCcxyxnoqQ00uLOp79lYAK0tGqhXHPPhy074wKXkoxwkfO8eCVUMqOxUj3DWbYDaeoC0UGLA2VuNRMHy4q8ftu4uOka0_Y3vC8LmEI2RkdxSA9LHfBIUxT9wjdx-9pXKbmb8aKXGKHy8myN9HWIB6id2zOgYYkQAzU5Ia3T4kmgueEEwD9a351_Il28lRztdfSIeW0H181k_g1luh4PFAEh6i94BdWWRTJKmiP6i_IFHwA2sG6a9rYu5A5eFI9SFJ-v4YMNNmXwLDpFUb1iFMvWSC4EEA45qepE0cwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoLxX64qSnMSgu89Stf2pIESJGlRwHIihUKWBOYVQXeP9iFW0oE3nRFkvsZM83M-f-_oGHgUQmpmZB-0B2Tbd4S-jNzfDN2wmVFh5RxoATwsWC-lBtBReIhLkfl17zdXleOl_vgmI290S1caO25YEPfulDD2qcXEvTt3lm1cpMAJFqSfzOtgvPqktdNwoHuahJw-IOMiLpyzmgSYWPmHyc_h7bbMVG7chTjSHchyvm92Aq7M66vlg3qnVTkNLyGVKLlxY3CszzPfH9c_VyXyhs98yyruHD5-E9A-1deXdo79vceEren1DZPOf9FxrO7Y52aCHVm5HmBNvS-0bqQOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZHWhtpVy8hIceVWRwjBiVohfiliU8SFsIWYxCMCsMM23FC8H_3Yz3hILv1EGaOnUC8gxKvKZzFVPxzc0B5HZO0vgzFcwSOPKLCJw62aTEmw_Cnsx_qQwK6RoL7ZuDMYNgxdlMGsZiU05LcvbnbsTPC0U7JmL7ieuex37No6XNP8QQMPhG2JrImKcNrZ9pXe_INqNTWi4jmdMmRrkNS5wUU_iX81HIif52rWifl2Okr6FcMalu5iisV-7JVi-SK4tzgZ3tXEIiP77lUFffP6G8GIhb0r9_hjgNr9Ooq-GYuAKIhpa_pbU-bGoFCxql-Ur8q6tgj7CPx5v3D8skHqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwJxmHTcBWPEcjKYtL172q6vjrSWeyQhjnjFGss88TrT0uJ2tbB130373n4tMNtDmUNjLCB2qhE1DD6ZKTAm94zf8-4tQtqUUYBAxjvN1hOUHYOQ-gfjIvP_ygH4aaxjiUizAlC17lgwUazItdoYlsWoiPgLE-fBIW5fMn2_EpO4PVl8jZKF9ckgrPcH1--g0mN74FjbDTzsyc4VDVDZj2S_zTX0POEmqOza57iLvbP9aov2YA_vMhW0mKI58QK2g3vfzQ6e6xshLHNMuQjke6KxyyVWJFKoj74i9Yrwz-SW6H3shWxaLMznUf5wHZroMoXy6slWbCGEcWB6dWBfpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsXSdl3anbC_zU9gtnVL1e4o046yJuxsZ762hfukH-HyBe_cDbrSO7ODEDHf2Nw_EHwd2GWQridrImTMaN4T5QnurbknZbG1smGIU-KQlj2GG4VErhxv7GsLC1UP8Kpk77GORsj9wA7aJxVPcSwl4exrBOL5m575ITZ4fm0DQTjqTf_bpXMOGL4CUgCtj2Y27kSBgG4QHUBmFQE2U0QGOShCY-IApiCuzILIzLDqovzektYTmO_VcB_UBS_rwH5ryCRdn96N8da9vJIChr_m50j8YCbfNKhXc-h5cJ9ZYw2KqSAeVx43EcZUr7wTNACX8Fx0DshSfGRx-jK377CA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iiu6l4kt0g_RwD5QdsBi00U5cCeVYDrsFtqo2PvzLZTg0xGRA4pBl2nWcSAQO5P8bVCP3G0eRzFWM7ZRQIfzpWIBYEd9sPP4fHDfF9NSLslpufqDxdbg10VWHH46e7UN-E2mcH0gh1TvDBmTrlUfw7M8DkQIdCcUbGewmcfex6TQ6n4TcFkPV6UCQp56rL2RhSigWU6avaLAx2Flp9zt0ZUhnpP_-e-uisv5tu-A-WM9DqR-lPBOZkhuhq-Il-0R3zTGPCVdnUJZT_qddZSo-SN4XZ7_P8lwmYEEBTCWCao7O0yVWKo_7Rc5wSeJtJJ3hrKPGDEQCWTO_ZzJxVR96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL-BtdJIHOdTAk3iB8UO7VBgGp23YB7fZJfnjNLAlP5kxOhZYIw5NHA0TgFHHrA8fGRdMlJr3pAcENhmdYOVowYmayBJXF7rzbVL9zxKLdgC595EwbP9dayzaJVcBThaePhqGUGfIWJd6kFmBBdcjGKfg58Kgjprf-b5j1sNWCvpeBf2sAgIqOIlPtAtYKuC9wOLQfwaPqhX1sGx0Oihr2q72iXjQs13bVqiuYBVLo7Gm0VpOYEsZBNoLAh4G39ECrG7sHrMGKAMnupkPSzDZyfCq4sBqsvH84g_SfA04crs1fujMD5CVW4r-knM-bAFyuYJroOCLAfuEkLIF29-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cty3lgP52XVkC_EKYXC4Ipq4r_NCQuSnxVyU4frg9j8QZb8xtfaFRhbLILSWn-lqQiqolzX0lNcwrkiks1ACyd7LvngipGL3O6La-tdiJyxfdzVvGDiCVdh-eewzeqP6G_NbRUxj_OpmkOjDv-hleUwnUPO_z0J9oOU2equFhdNYUgD38XQZAHajLlzwyzRlATIxXRhe7Beo2gkJBG0ggcGA_kRrnlfHeHJT3BWAgmtI6MS3kSKqNopYzUtCyFTbF_gpx8Ty8o6TryXl552nNZ5KZveW5KziCY_waDhZjASRRZYy-3jtbGfqchUPmg6zsRcNfaJ4zL4Ej2wwgBs58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID2Aycb1kS--gwruOX3PglcrIK3T92vhFaRPxCp8OQ45gei5NIwa-b_NQ7cLpmazehiuBK22fh2vnhUZCOsCEnpJXMqMu-UImNjbk9_P_NvKLgM-RtiRSK8M-nd5UBBYGTTUc19fX7tkCxnvCqeJJfMtLArn6I8h5Mvm_Jwr3sx6BUbmi7xEN6O2g7hjjrO2NnWiAkAI3O6VtIaNOHfciNbOysnLoYd-UEcvPs9hdSw5YksHeJ6yw-jyNufc0EW_enKKVIHxqtQNTn2jotAor4dMlra9uGfURgrdfwd1AVmiL6Cfb-_BA5CnPO-MZuMQiUfjiYLd4lyfPzq_N3mU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
