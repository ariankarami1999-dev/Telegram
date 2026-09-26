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
<img src="https://cdn5.telesco.pe/file/m51dmwXhcIGukHD-4zyFjn-wfXOEgzVfysImEuOILdut0QuXa4tM5z1LfdT1v4XlNcOIATxOGAucvYdSEVqF5OHxhmQVX0NHF0rh05D0ifeACeNS2qjr7ECe33wRTwW7HiA8TXgKLSeTwWPRJThLbyCD_AppRQXdnEFU_8RUyCuNv0yzBTftOX4nf4VHVCvC0YPK-YCNiv1rB639nXlMse9hV2bhdNp42ZbazJUWzOPdNxq4LetAP7NdAvBR5eNi3OWMZQ5M79GqWPWbeN4Pq3Im5qXhmyDKqQhUSxnjIUT2xsEbgjoXBvImPmO_2_hL3mPfCkmZovyDx28uVuEfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 400K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5jjk7AuyaHdzFsq0kCdSElTZMbkgMjBn7aNKiBrDnvdG8DbEuK-hnCmI14Ctc4_NvilF2lRlw3xNQIUovFRK5RAcp7NXHpt4r0I9czra_UBK-TTHeVlzcWq5KTXZndyiL1E9Xh8KN8Bk-RUUD_QqrQqL9hEJsw0GviZ3KGAdtg1ii8OOWo7wqx4nGWeDmhqxFcwagen6GrOWgiZWGK7rE0Y6I3bxawC6B_3BlU0tdcHVaJ3plpEXIU-UCCN2HfIalAe69r_kFOwEw288ILDIp9GjpQvW5EOv7CGyQ8aqbGT6rEVv9XAG9m-ySwKdyJXYitvsbGpjnDfI2-q0IxE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEnJThVaxbOkDPDNl_8lPFXnxUjrrOhtOlotfZnZ4ao9AmHNN1gADi-Xliqjcz1D4ESM9JNf9aZPhdeuEVEw2IpRYo5jmo0fIazJR3k3-_VKkFtPFBtsXlRBH9ADje7SbrzeWWQbWLCZ5t3Ui4i9jKlAcknLGMF4oOWJNuQ6gh-UIU3Jlp7NgHrshJgu_UrVZS7Wx3bvI4vyQAKvLs-Q0XG5oBCGURMMAvHrNv-XN_AI1vHDBbiApnqJrjqyuzS6SLnTa4le-eGISrsD_xaAHjX82GAMiOYEjXSdCcLrWHPFWSRMaSr4zCJUXU_HgWdirryoT7UoL-xU9d3fvLe18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=RZpFPmcFrqSFp1S27jnblze4Tr1hkpwG2mhErgYAsFbgzStH2rybs-oz0DUbovCnY1hgy5r5vV7dqR_PuPko9zD1G2WmfTB8pw4pHGN6JxpLoKC5AH2zN9qjuHcSe-JxGULA609Vb40lS0uUBbZUmWWthN9DKa17hu6yCCctTVuPecl2whvHXW182XDayzzIrfwZERz07IeOrfmed8VkCFZz1McBPIInZHzJYGX__xwtx4EPIHrtiBst1qvZCtkc3nOu5-yWv8gjUN9-JpumVmS30M5GxA4-XzLIaGCnlZmojamGIKG5ytgvUdwSXwxuWdn-S6B7nkeezVCtT2ljcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=RZpFPmcFrqSFp1S27jnblze4Tr1hkpwG2mhErgYAsFbgzStH2rybs-oz0DUbovCnY1hgy5r5vV7dqR_PuPko9zD1G2WmfTB8pw4pHGN6JxpLoKC5AH2zN9qjuHcSe-JxGULA609Vb40lS0uUBbZUmWWthN9DKa17hu6yCCctTVuPecl2whvHXW182XDayzzIrfwZERz07IeOrfmed8VkCFZz1McBPIInZHzJYGX__xwtx4EPIHrtiBst1qvZCtkc3nOu5-yWv8gjUN9-JpumVmS30M5GxA4-XzLIaGCnlZmojamGIKG5ytgvUdwSXwxuWdn-S6B7nkeezVCtT2ljcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvIP3aT1E0QarzO9XZZqIYvHywEoo17N59Ot7Z69xa7tjpukpdmGvz94RJiGEjOHurI1ckqi4pG6oZbev6SaM9ms7xbwPpt3B298hRwfFYWYCURJMcXcVjd02FWCCK2ixrlk7zfSNPRbGeMfF5lqG1Ig1V1AF4d2PZuP33KlfTuGMla49YNQTpswh3iZyThJFbhUvlnOpA2DF3NHlx5552VFw57zzdbwYtbLFzLVZdh00H9lkagIJ0Q4Z_-aIRb9tdBhHdrEVqU9MlfGm2fe8Ptfxzacp8SfXYpKEv1yJdpKShAyqtw6r4h7BIbWG_I3l10hNNYRfDZtsQ1WIU9Xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfo2YaF_d-5bAeHuUHZxHb5xDHDkE3it8DNxNWdVCEJ8fJEiIyRTmoe7ypFMWK8gGHap6SyMpnCdUCaxwphVudXqRKmgfcZve0P7fUleLLzE4p1ZnMaKoWPWXCmPfAc7K-eKE9whxyRAN51CMC9yxTHQt-EbBteHDSEmGczgHeu_UNOhWqKSMvQh4ImgGgfJh2OPtb_N-PFyIlVwGOpjPfOoDnT8sCj2VhaUAUtCnj-YQ9LhAJQCRpDhensTUx1dJM06qiPpeVUx9il06wsMJQX4BacqxcYS3VRHDf2ZkuoGqZ578UXVAshzA3BY6SkKJBM9MPI5KYgZ5xNG-gL_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbhoU_dXR3Okk9Jxb_cIlow-KFasIvehVCL_We81M7suZi50Zvdp89mcowxsD477c1xJ_Uu1RvG2Nz5XzVw_3A61rMKWeLLwQrTlJKgVsy1968rDortlJvw7s4VDoQlef7s2ST2qBVJPIQcF39k90WUzAGNOqP8uVuoNxLjjjysxM2yAS5VjVMme9TgFwvAGIUHzUeUT_QUh7mmIZ1Ux4skVM4cnJ6K-gxq_5-GP38XxjnCCbxVjPsXQqhB5SnczEUZAQS2jByWJEFB3oYGhjNfoalC_7jTlULVyAjV-E5mAeZCQDf9zi6-9IPhFF2OQPFtXt33uxHjDk9X_Q4EeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC3Ve-rVUV-NDb-JeyoAqssEUXVKc9dL2LqQgwctnIOkWtWcD3T74kqJhzCUSXcqobg1qxY6ArPE4O7t5Nut2ujl_NCbvQgPlYsfv5k4wQODPDkspD0dILgprodzwd8upL_FxXpcu8cRfwOppVpYkMccNoW48aFXNMGzM5-yAQ2C5UckU2f2E4u4pAwbtKEILWxdc4kAU8Cjsdz6uopazjnODrdMBqKLSq3ApJ0_JKYdDOjEsTnwsI16acs0D54deVbiAHXowWhsSMnZBKmWOR7NZ8z_t4NhBZ4x7g7Gx94JjWZet105gPVSdlyzSgHbrKYZTw5iYYdbDmKRyslFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107275" target="_blank">📅 01:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcF-SXIRt72KGiXP7Vw9RB3x7A4HAuywURx54B7fQlZaAjI6GBioCuw_PIo_DS8WFfkm3WbtdDjhv64ihods4Ty6-HPN9Rb9D_yFGTUGcL6B5SaTVdszU51TlBgGuCbNFnJMdjEMEKaHGaSpwezRo6zE7N_mvG8yUM9ERxzwC6ceyhu0DE132pTMVG_Fk3x1ZgRrbAPgFYx-ZccTDdJSGsY_yJUsRBvpJJOWCiOESGdsuMCF8Rppmv2QdsB8ezL5HarJmcDzJ3J0PUQ71NZCzjQF-rs3nCzf3GS8YVWj31107Kp6EuXKGlOHQ_92B2xy-5ws1hagJeEeTkBXJbFeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• امباپه به 107 بازی ملی رسید و رکوردی را که قبلاً باتریک ویرا ثبت کرده بود، شکست.
• او هشتمین بازیکنی در تاریخ تیم ملی فرانسه است که بیشترین تعداد بازی را در این تیم داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107274" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107273">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAXmAfLMlEYgRFgZ0FeA4h41b90kw7Qb3kQaUXGRhV-eq2yu7FF7Cj9tgY9mjcajMFp4t4qbNCSmuryUBrnu2kC1nI17hF1_IIgEBqbW6PcVxOGsUWzv_vphTnw9db4HUXZ88EZp3MJTU1sJVu1oAPO18TLf286f2oSOrRFoQcG3NarAzysaaCH-UWdeKQFTfYPALrWfzrv-RhxLMorCMg9xyEgVcr3oWRukjXMjDUbKl7IysE_7EGWjXB81cnLuul2aWp3PfILkDCPri9yUtabaq--m6kQadU_T4FplnzKJ-1JEYHwsnxtDU0z6cexoi0J-ZkBThqMmoZ2yIVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107273" target="_blank">📅 00:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAOGM4cKCN2omM6T4KKiola1lHdxLNmk-GciK-8ji-33-bf5shqGGjc2d67QN6hVRUa-gcGFLpDO1gTWm44-paru5M4qcs03PAgwh7Cd6pAF_HKrVEIE5mB2eCs0SoKhSEArV8CdLBFy0IOVrKGa5BzGKk0I9xIN3Ex75yyojX7arr3Xb8bF9loyRSG2ctfm-LzSGa66bE-DZSEo8zzWt3s6DegIA0rFTJnmnFr6LGrPFsyD6rcH1JQdP579d0IKfGV_m64x1vpmR4Aihi2UMDrKOeDXtCfUHOGTrBR3lh_SVDatR-ORbibzjjN7OLRkV3_B-_2p259dM93wdtnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107272" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107271">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=Jkx01chCbkcQ6jjwSIfr7Ml4fCcbjm9aDM2NRSNaGtXBf0SsbW525-iVLAlN6AvgK2lKs53Sz1MNGNtsgW6ygxzdwBhSiTGFsoGIo1NLQNw_X20-yBNC9DGfvIN64f2eLSb4zBvu3Up4j6Gt5zmwG-Z8TPRn0WLVmoalVqSVbmgfrQBQp_YkRrgckDAQlLuOtSQxcTvnRSATuKzDx8EUXjdBELEIMfT_4PZ5BIyYZ1ujWGcxfj8Bz_0Magq-_rUmEPVrXu-McOJr4-Ug3y8h3VqDuC-uKjXiPOMwe_GbJ1bl3p7JrpJAAnGXMs53xCo6HRq3LlzNz3k952eix1B6VC9h2hEZyttxkL7LcpmfdLGLYlhKPcLZ7cI-6x3_kL9ZZn3bA6J69j5fAz3uLYtGSPhxqY6fFKfu_JhXmtAkKjDQL7GziXJ-QkXpoJCryoLJfUCwCET2jtV-XZiIIxrU9SlE7KOdLUIedm5k8JuLV0G8zCKdwJOy9n59mjSYE9AcNe4wDDh3gQpPuZdZUEsev52xhe14qoe76nr9aIV2VQjvWByDtL5xNMzvpOtlR1bTKhrL-vvhbImC0ZVW3c3t57y9qbZNZ_niMaCMi6mcj8dNFGZxYYvg0O8bwmkUSrlfxCyCC1T1jd4P_sM_Dpkod1-OoAhHT2hiIaVEWxNRVTk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=Jkx01chCbkcQ6jjwSIfr7Ml4fCcbjm9aDM2NRSNaGtXBf0SsbW525-iVLAlN6AvgK2lKs53Sz1MNGNtsgW6ygxzdwBhSiTGFsoGIo1NLQNw_X20-yBNC9DGfvIN64f2eLSb4zBvu3Up4j6Gt5zmwG-Z8TPRn0WLVmoalVqSVbmgfrQBQp_YkRrgckDAQlLuOtSQxcTvnRSATuKzDx8EUXjdBELEIMfT_4PZ5BIyYZ1ujWGcxfj8Bz_0Magq-_rUmEPVrXu-McOJr4-Ug3y8h3VqDuC-uKjXiPOMwe_GbJ1bl3p7JrpJAAnGXMs53xCo6HRq3LlzNz3k952eix1B6VC9h2hEZyttxkL7LcpmfdLGLYlhKPcLZ7cI-6x3_kL9ZZn3bA6J69j5fAz3uLYtGSPhxqY6fFKfu_JhXmtAkKjDQL7GziXJ-QkXpoJCryoLJfUCwCET2jtV-XZiIIxrU9SlE7KOdLUIedm5k8JuLV0G8zCKdwJOy9n59mjSYE9AcNe4wDDh3gQpPuZdZUEsev52xhe14qoe76nr9aIV2VQjvWByDtL5xNMzvpOtlR1bTKhrL-vvhbImC0ZVW3c3t57y9qbZNZ_niMaCMi6mcj8dNFGZxYYvg0O8bwmkUSrlfxCyCC1T1jd4P_sM_Dpkod1-OoAhHT2hiIaVEWxNRVTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107271" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107270">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107270" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107269">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107269" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107268">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک به ایتالیا توسط میکا گودتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107268" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107267">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ایتالیا یکی از بلژیک خورد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107267" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107266">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvDSJ_e9jW9VQ3cMg3skn5jhropYC1P_5TN_vOKkxycREOlo16k2mH-7d17y1_3lZ_LAV93_oAWAHLy1E6MTaLhNkFtcjTzZ-kZapg32_x7uoJGK5GXiMQMJqE-SJwSNsdtsG6IFDbnCUpAbNfdVRPwVPIuEshebfEXFRucofFAZPZmy4SwEN0OPpI5VTmtLJUrm-pj_sAyYhImJ2CNypjHeX0ptDqZj3VaydPgIb1PNymfDvNbA9KsdS4fAJ9kaVq1do1UsI6BGBlT2jyq_fOypZwXzwlJFQTTkFRiJItSw75O2AqvvSWFxkduLD87WaGDosZ9Irlc_yk4Y9k5MxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107266" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjT5C0PxxLaZFvm5xdvj258UAXoYCXCMvrHNcF2fYG_GuXRpICbazxRRS-YGW88zTBTWlzE-aWSQgnsBw9Zyoocy4vC-Eufvyn6GsdjWf_ot6G261W_LkwDN-exnz_3gMCmi3kpKnO8wh9MG8ClMB-AOZBPIBNIiyY96ht15aIuzeTm4NSD5iWnnI6gl9bE6YwFLGPyIVy_pTrQUezgIj6R4fBnAVZGVIleF0HAjhK9EALhGc7PAKYr7HN5xPHLIIDS_vr9evuqbgDDS3SnvMJaLa64JrZAK1O9wFspwLnq9nIGeV1Ym9TtyxUGUmSbP6w9D4izxWEmWh2QjtRmw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایتالیا و بلژیک | لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107265" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfCbnESiW9MClZqOA4L-n8i8qPk15KNgUFZ3lq6TjrwPw8amcophgLOH-MgyOUiXBwGq1QtJN050bgwvxWJaAaLP11JaAB4ojOTeDrDlpPWrSltoJUitS3FYo4dz1HYLn5qr3TzW1kcPmjqslBTnu-8ZVxIyCShrg08Pm2X9BMNABaY_dHyRhAg_asWnD4WIfVMKZAKWz_q_Slub9wYbhKOmiOLsUa0jVoPvXG2sgOsB6347BymFbc6Q0rvGEM7dQ5xCt_CmsExA4YMUAi0TdrdCxdJrOeoUDDyuBhr4Gd9bbgg_FJp0tT9VDdqyU1xLp-SBfug9mUu51_4LCEQv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه و ترکیه؛ لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107264" target="_blank">📅 21:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=kmmujNFiH0_FSk6qu9hwrNFGOqrGbfNCjRntdTX8MiYsUr302Xig9YcXHSmLbcmcPmK3ZkV0T2kKQvGTmuxLIjL0LNz3_rR6gGKuZr_-hA2jYfZitptASAB_7CTjQmzbbu_uPJqa2DJYnupWmVVb8Mo8foS9Ak4IwWp0j9JygzqIQkWvri74NLNyHg0Ek2KjtLZjuk7B81HBIroofiKKrTy79Iwz9RntFwUIViBZxxFVoDQcCvFtJLC-XKeTl3cogC7lzlweyfXYkQQDHGYzVedorrStMdTtdnQh2b9MHw1TiAnBRQtfPBcR8k3NCPPbiEvdisFXEakybdLDM0RgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=kmmujNFiH0_FSk6qu9hwrNFGOqrGbfNCjRntdTX8MiYsUr302Xig9YcXHSmLbcmcPmK3ZkV0T2kKQvGTmuxLIjL0LNz3_rR6gGKuZr_-hA2jYfZitptASAB_7CTjQmzbbu_uPJqa2DJYnupWmVVb8Mo8foS9Ak4IwWp0j9JygzqIQkWvri74NLNyHg0Ek2KjtLZjuk7B81HBIroofiKKrTy79Iwz9RntFwUIViBZxxFVoDQcCvFtJLC-XKeTl3cogC7lzlweyfXYkQQDHGYzVedorrStMdTtdnQh2b9MHw1TiAnBRQtfPBcR8k3NCPPbiEvdisFXEakybdLDM0RgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=ttf6jZbOYA0bfKDZBe2ANR0v6V2sMk1iucajqa559imi5oMh5LmfKgotViNIlXMm8a1w-ZfNIIbv3n7Sib1EYHc_bho89xEcwafSzS8gaJsZPdeTJaKNOL__dNYHVTXFAdntjAfwHuczcF4_NbTrKuU1HwBXBnWPY3PCTHiEsAZM1Q12evxb_xFpbUVskqF1jl5LytSwUZByaGy36uDu4bMZtBRIScSonYEvHx73JbwbWdyKahGVP2aT_jzRJCagRircAStxKylEm4mqzBR8jRyyuEphqlQa0uGxI3r_JuTy1wyQ-UHGhwXyAYj6RkwfrPvKsO_mvYbonVWPVNxWXHVmyMHRD7dRDwH2ejdNih26AtsSa3rUQjkDQUfeW9LE5gmIbjsgoeueu8imdNMv-t5raewFHDw8pvE-uLOd-7MHYH5vYiODq5olBnUkCcY099MvZyNpoJmePUlizU514ysqOT3fXQQgMyZkCBWKDL0cMHEjlwPR4-1zjuGcYcu4dNO36bF__y0rsN4NXKkF0Vate-lrYts5DwcshnZ9JHaqUtc_9QG2o49ImukAjJpzQdOn64yW9SQXsrmNHDG9no8C5ZXbOgs5wFryNYz75ZZG77bfkCyoUiYOo4jq4HndULPkf7iSljeYtslp3BqsungsBqw0V7SYLhyjt0dW69g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=ttf6jZbOYA0bfKDZBe2ANR0v6V2sMk1iucajqa559imi5oMh5LmfKgotViNIlXMm8a1w-ZfNIIbv3n7Sib1EYHc_bho89xEcwafSzS8gaJsZPdeTJaKNOL__dNYHVTXFAdntjAfwHuczcF4_NbTrKuU1HwBXBnWPY3PCTHiEsAZM1Q12evxb_xFpbUVskqF1jl5LytSwUZByaGy36uDu4bMZtBRIScSonYEvHx73JbwbWdyKahGVP2aT_jzRJCagRircAStxKylEm4mqzBR8jRyyuEphqlQa0uGxI3r_JuTy1wyQ-UHGhwXyAYj6RkwfrPvKsO_mvYbonVWPVNxWXHVmyMHRD7dRDwH2ejdNih26AtsSa3rUQjkDQUfeW9LE5gmIbjsgoeueu8imdNMv-t5raewFHDw8pvE-uLOd-7MHYH5vYiODq5olBnUkCcY099MvZyNpoJmePUlizU514ysqOT3fXQQgMyZkCBWKDL0cMHEjlwPR4-1zjuGcYcu4dNO36bF__y0rsN4NXKkF0Vate-lrYts5DwcshnZ9JHaqUtc_9QG2o49ImukAjJpzQdOn64yW9SQXsrmNHDG9no8C5ZXbOgs5wFryNYz75ZZG77bfkCyoUiYOo4jq4HndULPkf7iSljeYtslp3BqsungsBqw0V7SYLhyjt0dW69g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=PGN5v3H-ABodRQ_ZzQeV-NkztbAWLMqZWBGMTh2_8zDvrlHx-cQYvO6AU1Bb8eDvUF1sCs_lUPOV5iA3mVBD2fLLGlZ5NBnJ0KUA7ouDnltd8LyvcUDEwHwZG79ALwa0CKms-lHS2bfrZg7v0EObcJICXkFj5n6y9UWc6Fx8DifAjfEhcZTo4AmzitWcIAmQ_K-eSATqFW7zpX1r19cBc_mSDffFqTKtH8F59B9NZb2NKoLs11jt8Jy6U1RoWNgVGbnH1P1kUyZsuZX0vttbG6Idsl9XXwdfiVXFBoZL2Q3jFjZQUsGlMQxsJCD2BTx1fONQDOrg-aRc96_Z-EAjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=PGN5v3H-ABodRQ_ZzQeV-NkztbAWLMqZWBGMTh2_8zDvrlHx-cQYvO6AU1Bb8eDvUF1sCs_lUPOV5iA3mVBD2fLLGlZ5NBnJ0KUA7ouDnltd8LyvcUDEwHwZG79ALwa0CKms-lHS2bfrZg7v0EObcJICXkFj5n6y9UWc6Fx8DifAjfEhcZTo4AmzitWcIAmQ_K-eSATqFW7zpX1r19cBc_mSDffFqTKtH8F59B9NZb2NKoLs11jt8Jy6U1RoWNgVGbnH1P1kUyZsuZX0vttbG6Idsl9XXwdfiVXFBoZL2Q3jFjZQUsGlMQxsJCD2BTx1fONQDOrg-aRc96_Z-EAjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=iCVXhut5TEnunDrfDgZOfWXiJNeGgjGtF67emjWrR4SmCU_7Fa0Y2XkzDT8pQF8gfGCZoM3AEiVJOaR-LygQHRCIbiHyh3u0WX5zrihci1LvR61j01oQ3JeEmqOclN-Vmv8tyHmHbRQJ_zLXWZHBPOTmuKZbgWri07bdbUtrXAzSDCHJt4z3RkJDPtkSlDpdJhqmFkpNjy-ST0nEWcCuIDMtJLg-q5_Jardsf34C_FozUJm_dDrbfL2blO_mSIn11sSnsHnx_MJdnpZ6B5J8cn_9JEan46vTYPN-b1GXpQSgic00OcqDKOSTlEq87lYbDk_UNR-8n3m4vgNcDYnxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=iCVXhut5TEnunDrfDgZOfWXiJNeGgjGtF67emjWrR4SmCU_7Fa0Y2XkzDT8pQF8gfGCZoM3AEiVJOaR-LygQHRCIbiHyh3u0WX5zrihci1LvR61j01oQ3JeEmqOclN-Vmv8tyHmHbRQJ_zLXWZHBPOTmuKZbgWri07bdbUtrXAzSDCHJt4z3RkJDPtkSlDpdJhqmFkpNjy-ST0nEWcCuIDMtJLg-q5_Jardsf34C_FozUJm_dDrbfL2blO_mSIn11sSnsHnx_MJdnpZ6B5J8cn_9JEan46vTYPN-b1GXpQSgic00OcqDKOSTlEq87lYbDk_UNR-8n3m4vgNcDYnxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=Dj8MOUvkNOuK8a83VivKAO-aucDTXAZFDtq2sMWHqGoCxvyfJ_qMuFBln8f3Wn5z6z7YyEyKakAd31MBgdJEWqUBzHLOUVXjhSYn7pK-A3hZIOL1prQGaP2Mk6KrI5AaBqn2jeZeip6KSRDzTX8ZnzO7k00U2E9sh2Rd4gOrnx2UUml4xYiDThknLw-HDt30ej_2BWjz09yKRA9cbwvmsZ93sxzO215oXn-T-rlfDwOQdW0a-Ecz_CzZGDLge--inilZ0rPqSv1EDkyYg0E5AkL8vK25GKtmaKTjYJgeEoX_3Y4EbwAHOpDNYvERaXDQapEghUIZ2x8YQmYS4kekHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=Dj8MOUvkNOuK8a83VivKAO-aucDTXAZFDtq2sMWHqGoCxvyfJ_qMuFBln8f3Wn5z6z7YyEyKakAd31MBgdJEWqUBzHLOUVXjhSYn7pK-A3hZIOL1prQGaP2Mk6KrI5AaBqn2jeZeip6KSRDzTX8ZnzO7k00U2E9sh2Rd4gOrnx2UUml4xYiDThknLw-HDt30ej_2BWjz09yKRA9cbwvmsZ93sxzO215oXn-T-rlfDwOQdW0a-Ecz_CzZGDLge--inilZ0rPqSv1EDkyYg0E5AkL8vK25GKtmaKTjYJgeEoX_3Y4EbwAHOpDNYvERaXDQapEghUIZ2x8YQmYS4kekHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSLWbbWqJm7XskMnXNjhSXzO4XK9hZnJaM8pBVb51QdsACjzX_rtcPA7-ydZceaL6dMnaZMSajCuEF8ak-GWaTUOd6UgnIpo_ToAkhjXI8m434tR-Ab_lsN0PRVb7wsbf3tjoECqQKVjKjTWJV9-bvBlnodE9CHorjY1YE7sgl-LIUquQSgfx6csYIpH4tz9Ot4grLPR2D0AZOJxkSVdpWpavOvRrWdA8-4l0rqbzDzbxrxkKv_GSroksbkIUNoc_PQPMGaNy5gYs9hgQ0jl8vQhuJyMJPqwJRjXyMuNp2TLdpnq1I7T7Op39bWjaV2irpnDpLM_4JupdnVKwkPmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=bwgWjteTYRzV_ZWZXWd_IZHPwGAOsmE7Xp-JqtTW-iJFYGi1jFYPtEC9fgsnIXR373j88caSCdGTkHz0sYefVEuDx7NDGC1tUFHP1nv8zdGqeRp7wohxcHI8-CWHsMPpvPR8_A8mvoukRfM9eN-nl8Xq_tOCST4Jw_JZ70Wr10XHPcmazw4_qkAmLbVvabOovLbIU1dy19kWpWw5WEfOTPmERF2onQHGX_OzLXLgAcl6kYBdRjDsFRg1po8N9FFzd92NZS1XQfqi8X9eSpU_A5XBgC-TfMjSTrfcckAzTg4WsSZh6onNRcuDYupQiCdlgSPxz0A6Uu9VQyWFbGr6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=bwgWjteTYRzV_ZWZXWd_IZHPwGAOsmE7Xp-JqtTW-iJFYGi1jFYPtEC9fgsnIXR373j88caSCdGTkHz0sYefVEuDx7NDGC1tUFHP1nv8zdGqeRp7wohxcHI8-CWHsMPpvPR8_A8mvoukRfM9eN-nl8Xq_tOCST4Jw_JZ70Wr10XHPcmazw4_qkAmLbVvabOovLbIU1dy19kWpWw5WEfOTPmERF2onQHGX_OzLXLgAcl6kYBdRjDsFRg1po8N9FFzd92NZS1XQfqi8X9eSpU_A5XBgC-TfMjSTrfcckAzTg4WsSZh6onNRcuDYupQiCdlgSPxz0A6Uu9VQyWFbGr6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW7BOQVTeBTC5MATlUHLUWNZjCHgIrcJ3OqVIiGO6gHyjWHFkpJ_xBe52opFe6pHuuoZLayZmoI4f3ZlM2AIFccPWu-x8oT-PpLZZRovN4qcQgRJXbpGLsy2b1a03TzGDPs5KMP8g77ShRzjL6QchemYwrTYvyTbqt5fqocxovxPnRlPSVgwR1WPgTNiB-Su1fD-v2utWZGYO-nTi5SrLl49VgQm6VBXNWXczTeZekxm4Oex_1nXN0db94w_6VdhEVjcMc-q2YzSaKRi6ExoL2EuoHGF9r6NHcxmmZPUfLe36b8tvcPrviW0zVeWJeeUF1klrPb-M6rKstUDwHqjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v18VBI0SDTvCFMsvCJcyiFPbsi_q00Td3ICadZRqRPvpYLBf3dwPIFkD608KM-HqiK7RqlqHVyZsIC82Hj4VX7PXQszZPJhpfvanO5YazDzDGo6-eZZFXrvs7pOxbA2oO0ejmO4af_b729OknMZxva4BZVjV-sZx5uT_M8yP1vXy3FvCY4F9heOK_gx_b6qdNt9YJg8w9hYAJbPi9kY7wn6DiqoUZ_txpTR9N3DkbCuHtYaAuH0ob1CjayQX39ONsWDWFtSqC3_xQEzv1VTRACk-mjVmtOb-sJeWQ1uGLSeXrF-XPqzcQ4x2MFmFu0Tznb855D8b3MM3CSvPO22idA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLMbWiBpwLCaeYZTdpdMQPyn4ETQpQYkolC16HowlVZKTlWDjGC1Dk6Z5GvpBuBXj0JcuPnZDrPKrPCd4xlbL_5gxecuGCvNk0SDOKE2U2URaccceQiMhh6CfI49R4nahigHapqfZa-Bqfryw2fyccqmD_jJwdap8uayYArtbtsWMH-kfDq79aHK6nEE814WZs8VrWAQmZvBujmzrnqh-kW0A02yiKm7edquEOSoLx-qqKcZQBvhk1l2deCZ0ZUmcQKhxKkc8DsNn-EvA7z-NqLde_S81pAd-B69a9jBZQTBv1HW8zZK6_5ki6BFbUblMYUAwbOgt740z2wfcRytOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107251" target="_blank">📅 17:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZzCwsNsLj7PKplPfdmFgxUwhWmGGw1l_J5_UgCE31rvn2hUW1K1HFDrpwSqyoaD_R-iO8eI1cXi6xlCI-pLaNHEUI610wlzSxNPjcoBcftLuJxrXL-9iJbPMTbxYGindrbIWXSvBEFOm6Puc7YZeQ2fcTOsIW3p_yElBpgWPNJV4oaSS3R-P-ZLrwKc2onVfLd-UolMqNFNZ1SDg0mv3M7dn6yhNtHyUp6f4Y6sx29bzv393sdntRtSdGRQvXcB6olEwJX541GoFLTZr_KqC1-DBPvPCvoxoyy2r3sk0NcvS9yPzSmE7Jso3AI1_xo_Ltf-o5fOgjQe90b2hA8khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز در مورد تحریم‌ها تصمیمی گرفته نشده و روند رسیدگی ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107250" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638e170672.mp4?token=o6Rgj3yrWD1UXba66yH_D5ph0D9C5mOXuYl2aV2KBWRHb713N673Z0Splch9VVE-vd4h69ZSR-AojInoK6j7oKSphtMtkBqQOKwSXidE9xQZC2e4fj5TOeNvDcE5Tuausr66DUtX2I2V6t0CFCbW0uIFlzcrXZbuF5BeXeGnmKPvjZMqpXIOcYNk9jZyp3KLJ-NudEogjRHhgpVbrobbXL2Gn3aKRVbgkXzWiT47Dqbx7UhIAr2bBozXujQQmm__dkknMf1in5mVh6LX6C8kKMRWH23kgeH46unVg-SwdIcPNpQ5__pZSl6vKBnpoP4qZylcg3iC0QAutABq-Guwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638e170672.mp4?token=o6Rgj3yrWD1UXba66yH_D5ph0D9C5mOXuYl2aV2KBWRHb713N673Z0Splch9VVE-vd4h69ZSR-AojInoK6j7oKSphtMtkBqQOKwSXidE9xQZC2e4fj5TOeNvDcE5Tuausr66DUtX2I2V6t0CFCbW0uIFlzcrXZbuF5BeXeGnmKPvjZMqpXIOcYNk9jZyp3KLJ-NudEogjRHhgpVbrobbXL2Gn3aKRVbgkXzWiT47Dqbx7UhIAr2bBozXujQQmm__dkknMf1in5mVh6LX6C8kKMRWH23kgeH46unVg-SwdIcPNpQ5__pZSl6vKBnpoP4qZylcg3iC0QAutABq-Guwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
هادی چوپان: من حکومتی نیستم هنوز فکر میکنم دارم خواب می‌بینم؛ وطن‌پرستی دلیل حکومتی بودن نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107249" target="_blank">📅 16:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=u6GSNZxJV0FBEkXbdrWrOo0diARNdIrd7RE-m8FGsM3barXQABhTAIqO11y7xgnO8GSt2OMfNl2pLbhYQPHUeAm0Qg-Wtio2apMrHPP-Bp9s-ILFYmchMKc-5IlZfmuNvoB-XXZ7eMPnXi4IqpkE-zOdQRADah8dSXieohKQE3tvOoY0F9l0OBPvh5Pdot4GLVIW66b5xfST4KIsos0d7UGoi_sH3v-rNNMD08cPv3kIaVC4igvPbBHWMsyxPk62MqrRq9Ilf69USZFmeWSoWriA-SQNGtUIsyeu5TshAN4ziLKSjGNRroW47AykJLSl57hE8YAJ3tox-0HFrC3eHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=u6GSNZxJV0FBEkXbdrWrOo0diARNdIrd7RE-m8FGsM3barXQABhTAIqO11y7xgnO8GSt2OMfNl2pLbhYQPHUeAm0Qg-Wtio2apMrHPP-Bp9s-ILFYmchMKc-5IlZfmuNvoB-XXZ7eMPnXi4IqpkE-zOdQRADah8dSXieohKQE3tvOoY0F9l0OBPvh5Pdot4GLVIW66b5xfST4KIsos0d7UGoi_sH3v-rNNMD08cPv3kIaVC4igvPbBHWMsyxPk62MqrRq9Ilf69USZFmeWSoWriA-SQNGtUIsyeu5TshAN4ziLKSjGNRroW47AykJLSl57hE8YAJ3tox-0HFrC3eHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
عادل فردوسی‌پور: کاش زلاتان ابراهیموویچ یه روزی برای تیم دیگو سیمئونه فوتبال بازی می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107248" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c917893c10.mp4?token=uwfjjEA3cOBmxuL-Vt4KGTnTJhoXDDftRTudOkf6wBmjSDKWNcWu65CFYmvL1Ql1-xwm1N-kTXCoVmlEY5R8PQ2mF0N-jEeQK3oZoV7Fn7UkvZdB-l34SX8mVAv0oLCkI4bdkHheLb8dDDZ4SqMjphOd1CQOSWv6GYS0imd5qjr6hYNgda5c7Te_IKwuFyklySYMnpd5HtsEE7XbDuGSGNjEQweFGZgqm64DuGTS95GOGLaqbZcYGzp3U5m199FDu3NBvi292OIFNcJaw0SusvTFAmNBMGoeqAVoqTuvQIjzte6w4JaJe1HTvKa0GicFswjo5mc8gYLMchjSdhLyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c917893c10.mp4?token=uwfjjEA3cOBmxuL-Vt4KGTnTJhoXDDftRTudOkf6wBmjSDKWNcWu65CFYmvL1Ql1-xwm1N-kTXCoVmlEY5R8PQ2mF0N-jEeQK3oZoV7Fn7UkvZdB-l34SX8mVAv0oLCkI4bdkHheLb8dDDZ4SqMjphOd1CQOSWv6GYS0imd5qjr6hYNgda5c7Te_IKwuFyklySYMnpd5HtsEE7XbDuGSGNjEQweFGZgqm64DuGTS95GOGLaqbZcYGzp3U5m199FDu3NBvi292OIFNcJaw0SusvTFAmNBMGoeqAVoqTuvQIjzte6w4JaJe1HTvKa0GicFswjo5mc8gYLMchjSdhLyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
صحبت‌های شنیدنی رودری درباره تفاوت‌های اساسی فلیک‌ و پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107247" target="_blank">📅 16:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=ivlbW-WsEf3JcC1u1bSlZxxzQ9iqpb1KCg7p3Q3PRIoz5hyMSsNSldP6VxoW7BEV5KcpkWfKV1MbWXgJuhFJKkcNTuT8KGzJzQcgAgAgfjhHlUh7oOkyytT-BgYddQ2bbG2vNFxEEP0bvmN9kXf9hmunK5Cyk7NPr71Wo9x5dW8yEDS-G3aCofkf5jI00F0es2_zvBFg_XKrYqmP5mORfQ1mantd4dHkLpNFQzbm-ytc8w5KlUB333HhKbzxuywr63hB-uyThkFk3uIcwvJvMXFlxEYRDNKa0LSav6wor0Bl2DNa_sCcOeWprIFyoC2A0apx3YeD9CmzU49emT993w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=ivlbW-WsEf3JcC1u1bSlZxxzQ9iqpb1KCg7p3Q3PRIoz5hyMSsNSldP6VxoW7BEV5KcpkWfKV1MbWXgJuhFJKkcNTuT8KGzJzQcgAgAgfjhHlUh7oOkyytT-BgYddQ2bbG2vNFxEEP0bvmN9kXf9hmunK5Cyk7NPr71Wo9x5dW8yEDS-G3aCofkf5jI00F0es2_zvBFg_XKrYqmP5mORfQ1mantd4dHkLpNFQzbm-ytc8w5KlUB333HhKbzxuywr63hB-uyThkFk3uIcwvJvMXFlxEYRDNKa0LSav6wor0Bl2DNa_sCcOeWprIFyoC2A0apx3YeD9CmzU49emT993w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آندره‌اونانا گلر ترابوزان‌اسپور از روزهای خودش در فیفادی؛ معلوم نیست چه غلطی‌میکنه
🥸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107246" target="_blank">📅 15:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=VI7geM4pyKs6luq7SEQ7PnlE-OzXePkmE3Agwxdf5KNXp6X2UlgdIBF1BtDFzPLF0hWLg50n4fo5VsYCL-4VxHdMpMcl3kRrE8ybZ-mN67Qe6jPx_ove_AyUzqD-TrRSP5NldIquyC0hhDsGMguhJiNzm9-vCYJrWCv-FvW0eCAKG9MtmMtc63hY6zFceH0nBHaNKqOvc87Y_M5dP-x4pPHPdral87svq9vcMgvdUJLbcLdYQVwfK8UqmIsUEcit52eKtQT2q-M8Ec-_nRwz5WCoAcDyJr4eeZ4hi_LpKj9ztf0wIK5TikWCK3XEgdsAdELDnBVlpwIJ8HXkdi4jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=VI7geM4pyKs6luq7SEQ7PnlE-OzXePkmE3Agwxdf5KNXp6X2UlgdIBF1BtDFzPLF0hWLg50n4fo5VsYCL-4VxHdMpMcl3kRrE8ybZ-mN67Qe6jPx_ove_AyUzqD-TrRSP5NldIquyC0hhDsGMguhJiNzm9-vCYJrWCv-FvW0eCAKG9MtmMtc63hY6zFceH0nBHaNKqOvc87Y_M5dP-x4pPHPdral87svq9vcMgvdUJLbcLdYQVwfK8UqmIsUEcit52eKtQT2q-M8Ec-_nRwz5WCoAcDyJr4eeZ4hi_LpKj9ztf0wIK5TikWCK3XEgdsAdELDnBVlpwIJ8HXkdi4jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=hCFTGjSNUhjUoIznmhxO9c5M7GbtKA-pG8zCgSX1tpLCrqE0IumWJ5PI_6Uem-PWSKzBGFsnVyweyV_3AMO2HIqUlOO5V80-1-0fofsukvup3p_8spQe8pghBVeET1caR4OOUsjPP_CmvKn_M_0VsClP8lTN-i4sDKhDzGsgUH6qgbHXq8jPN8qjG5KHSfZHN9-n5wqa830M-qDcbniXQG9sIi2MGACW5Z5V0KVQe1FWPmjOvjTogxotBgyAWtHOvbgcuzf-C-aMO3iqphCBRyaPWZxe9f-wfi-JOPcef-9VATcnTsxC94OgcoOD_vCZgKvRehKNHHfCo4U87S31pXQUE9eSfZugUpZjs5EQTP-loDVvLY9c4DA9uf-wz0-UxJwu6_IBTmiNihq6R9rBd4HfBpzRqzTOBrMgwbjb_Q3_DYjCE1P6gkr9Y-rP1ndKQZxv7TSSmzl_WjXD0PCrvsbByCJ52vKvhPZwpESHClK4fN8L5-Fi7EkrxJIHKfJIwUnreawoC-Ak8KKSWer04fHf8XdJIdj4ZOzJwymgedXvXX7dLlOG1Wp9hiQ1NqoalwOIJrAgCU3UmYiHtnm5a9Ps0zzDTxDLhSOMz8ZRoGgW0IG6TJlo97LSCSGUDtH10yrvcwWnYZFlSa82CD_ZMJML3SmAt-4fJ5lb2hgGuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=hCFTGjSNUhjUoIznmhxO9c5M7GbtKA-pG8zCgSX1tpLCrqE0IumWJ5PI_6Uem-PWSKzBGFsnVyweyV_3AMO2HIqUlOO5V80-1-0fofsukvup3p_8spQe8pghBVeET1caR4OOUsjPP_CmvKn_M_0VsClP8lTN-i4sDKhDzGsgUH6qgbHXq8jPN8qjG5KHSfZHN9-n5wqa830M-qDcbniXQG9sIi2MGACW5Z5V0KVQe1FWPmjOvjTogxotBgyAWtHOvbgcuzf-C-aMO3iqphCBRyaPWZxe9f-wfi-JOPcef-9VATcnTsxC94OgcoOD_vCZgKvRehKNHHfCo4U87S31pXQUE9eSfZugUpZjs5EQTP-loDVvLY9c4DA9uf-wz0-UxJwu6_IBTmiNihq6R9rBd4HfBpzRqzTOBrMgwbjb_Q3_DYjCE1P6gkr9Y-rP1ndKQZxv7TSSmzl_WjXD0PCrvsbByCJ52vKvhPZwpESHClK4fN8L5-Fi7EkrxJIHKfJIwUnreawoC-Ak8KKSWer04fHf8XdJIdj4ZOzJwymgedXvXX7dLlOG1Wp9hiQ1NqoalwOIJrAgCU3UmYiHtnm5a9Ps0zzDTxDLhSOMz8ZRoGgW0IG6TJlo97LSCSGUDtH10yrvcwWnYZFlSa82CD_ZMJML3SmAt-4fJ5lb2hgGuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947-hVVOPKIkee8XjUDC5Bfw5YGdL4PQ700G4nO-dIdSd8vgYJ-iUDZku9IQIrFruzH9Rt4Cor5i_jrugMCLursxRqSc6AKK_I9ZD7T8JkoxO_RabcPLWNol4g99-bGqPDOk2vL4PCzOxTdyf0MF1Jr3aOZey-Yd6u_Xjgdn9i9J1oJR9M8loSuZdQHIIW3xX9Kp3cs-eV-2UT3VUeJYKr3DBdynJlO46sMJD54ZW45ZARu80AwZj6D8u-p0A8_FKMuKvfUnW8I-XuuHHrtHdOzayicl-TkMMr_a93cjk0URXJjCHIA4xFNuV0suTkJZOa3w20BMgC8cM68f3BFkvSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947-hVVOPKIkee8XjUDC5Bfw5YGdL4PQ700G4nO-dIdSd8vgYJ-iUDZku9IQIrFruzH9Rt4Cor5i_jrugMCLursxRqSc6AKK_I9ZD7T8JkoxO_RabcPLWNol4g99-bGqPDOk2vL4PCzOxTdyf0MF1Jr3aOZey-Yd6u_Xjgdn9i9J1oJR9M8loSuZdQHIIW3xX9Kp3cs-eV-2UT3VUeJYKr3DBdynJlO46sMJD54ZW45ZARu80AwZj6D8u-p0A8_FKMuKvfUnW8I-XuuHHrtHdOzayicl-TkMMr_a93cjk0URXJjCHIA4xFNuV0suTkJZOa3w20BMgC8cM68f3BFkvSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxnRJ4qeLqLLeYC-3Vjpq7hRq-M9tbjAzOEoDEyOu6cnyvLtP_FbP09YhyE4ulp51jYozexbW0IfDPik5U_Lzg4QxYfN9cIM-xXxc02JTXrfb581v5fvbj6G8Ry4hY2Z_HHEmpLul6DxNeufz25aU8ZwX3taXA-4yNqU-LM0UsRmarRta2op0Mg9mFFOkJpE4Lt35YRafsCTUPjMQ_O0tq9n2vubN9e2jnlUc2eQEizEqfjNSH_tgT144HaWlraVHuAd5GdJqzlighL3_WTW2A71Hh7MJwZwEc_l8JreEEbK-eAwYV8ATBLo-B4XCWNQzsC4ViB6l_BxOmx_rnf-LD08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxnRJ4qeLqLLeYC-3Vjpq7hRq-M9tbjAzOEoDEyOu6cnyvLtP_FbP09YhyE4ulp51jYozexbW0IfDPik5U_Lzg4QxYfN9cIM-xXxc02JTXrfb581v5fvbj6G8Ry4hY2Z_HHEmpLul6DxNeufz25aU8ZwX3taXA-4yNqU-LM0UsRmarRta2op0Mg9mFFOkJpE4Lt35YRafsCTUPjMQ_O0tq9n2vubN9e2jnlUc2eQEizEqfjNSH_tgT144HaWlraVHuAd5GdJqzlighL3_WTW2A71Hh7MJwZwEc_l8JreEEbK-eAwYV8ATBLo-B4XCWNQzsC4ViB6l_BxOmx_rnf-LD08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=oUrSDzPX5EGbtMFZqvyNaB4qB6PZ0x-gBUzgn7eEeo0cgm7e_EkMs5AYax9GG5GuNTurnbxwkXyLBbBiLCGiUfuYAyokDrrmCZlsWP-ECCLT3B6tekfEfkw6Gbu6Z7tLEPH2R0jeBpMKSIm9Vw6DIpfpfJWqsSxscO9CmIWt97H7ncC6jBnm2J9ybvbxcOJxJtDUtuy8jce1kUyCClgKwGq4klXZ9cBgQo51z-5nyiMDwPtE0gRy-iNB5HAIw9dpMwqGcbD-cdD-shG9GgMhhYp4689qmXK9BFYhB6POg2AIFYAoHnIbA4BxMj4tvETTaJKFjPc0PDY-SnHqmo1KDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=oUrSDzPX5EGbtMFZqvyNaB4qB6PZ0x-gBUzgn7eEeo0cgm7e_EkMs5AYax9GG5GuNTurnbxwkXyLBbBiLCGiUfuYAyokDrrmCZlsWP-ECCLT3B6tekfEfkw6Gbu6Z7tLEPH2R0jeBpMKSIm9Vw6DIpfpfJWqsSxscO9CmIWt97H7ncC6jBnm2J9ybvbxcOJxJtDUtuy8jce1kUyCClgKwGq4klXZ9cBgQo51z-5nyiMDwPtE0gRy-iNB5HAIw9dpMwqGcbD-cdD-shG9GgMhhYp4689qmXK9BFYhB6POg2AIFYAoHnIbA4BxMj4tvETTaJKFjPc0PDY-SnHqmo1KDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Itfw5_q0LoX42x0auFV3qTMSc6hDqkD7OnoIDjmxZ36WrLUAdSwiF8QWBpJO6i8Tta9f4tLC3KrFfBUiG35nCunVyNZXIhfAD5TMQoib2rChYX5dcX4O-HLYAGPUZEqUZyNWPF-XDo8XwqGPA2aYNf-F8mHDYsmAxefrsPbFYQGgA9sMNBM2SK_S5hJkRdvsN0VNGq93PdIKoSuFbCFBC7X-d8duUsbCGN4S1H3Qmy9j8Sg08oF0_0jErEY-KcwNFo_YNMVitdKTX5yJvTCPDX1uSR0dPdqWfzCfnpMmMDD24JNke8P7bThkSDSaQPMsYYcO7_zEX8ZVP1xONIK8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0QMMux833Y-RiRjolejYjlm3xzXjJkrixi0cRFWYU9I28EhDawMUDBgc2pm9KjEE0Hh6wOxNMmHTgzYZaSaXlPO7CozNFiGnSlc28D2-KaHPO6z_8nX9L2VdKFzGhyuwmMnezqAV-CnnK3tbRjfIL0B8H5pkRpyzXipk-Fk1dwgA64-iqc6lktROblkbioVba9yBN-di_tl8JoEGWkicQHLBZp0kMAiTrrtsdvFYsr5WDLaFtFDfgldgJp3rdxw6Z1XGXcdgOXLwYrjIZMXZjPxdNr79WIr4Jzm9LJ8-jW9Ml5EdJFakCAt4l4K-KSSU2j7UK8S1_vQCzpvvkCkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TY5YPU4EG0pPzmIamAlhgT-FXbog035O9L19J9syHbSFE1iPoWpi7X-0ZWl08FzmmihBuV9dmy4obrlL1FBGq2KOth31XazLyc6oBhUk6aelPeXqMhfNHSg13Uj3tczYmyTUdvjZ_4HI7-oQhbIGVfHX30PysYbcVXBR-vFW7k9b0Tgf3IvRH4zGfGA5JQq_g4TG0jDbg8z9MolQHj4Zo3IymHBI9o45NXbT4yToAuIFJqCigilaVEopDx-Ja2aMAvC4Jq5zwJQ4rxwYD8gi1JPnm3-1Q5yyXqOu4evmyXrYrXfLcBU0wOVTvxVcwOzfSQ9ZWEv6U9Fcll-n-2WGCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuXUFgy9JEMdBdORlzR8cPXLOTLzTs73YL-Z5WycMC7Q4zklt8CqU-YKevuSpxzWofrfRWXCCRlhkC53I8E8SEPCVX3e3q18diZg4rFArQce5caKzZOHhG1xxwetJFelirRJlXrntwZdsLCGHj5jY3Hgw9kRBeuR2eW_3JXSca6-VbqjaH3Q2O-AVjIYiYdfWCe7OcpC_MrLyDCFiJgq_bdsSlXQX6YAyioMpOxQJN-0o5XMO3jXWWhwMQ6evtC3VHiYaXYK0Co6JC76zumyjYIb5uYh1FtVL4okS8GIGNLDjSACKL-Yh9BZ1VbnJMl6PCoIB8EsWNW-pzwoW35Z7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107235">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=P-3pviqWVGsGpmeYdAwsz-hunAXBwzR_lG0q0SZfCm6Il7tGUkhTcHriPT9x-iACP_WwXgiuA9dq_hqQCh8l_Z2U4mJin8lYhFPsfZLLzA-eePUSS_XdARgxsHTfdBFS5pxHFp7fvXaJO3dw6Mn1k3HVPfiWALJnDdQAkFRgbkjhMyjLA3_Qq_tA-nDdXcbz1ozMfEGMDmwoE_TL9JIpMisygAuHlmON0XDL63i0JCqPP7J1Qm_XK4wVejmBiK_Xfe0tQAcQPPk3eMMyNRPN5LsjaKYxJH8thBA8kE9hs0CXh_hFnoYCYlxJnDVYCbxvgzEVw6ARh6KApikX4BdPSSDd_S7ZkHs1sIE2UHDm17EPIdrNvMmq_LJa6nC1tcuOnQswFF6sHJ6pjz3wxuVG5IozlvPoY8OXon9cwdmDeR9JId6PQSrBrFK9Vhy9brQ3V87lqUBgutmaq0KFAmnpL4Nvkqum4e2Xywnv1TZ3lfH3QQ9QRW8fHKodVoxtZvfSvU2DWb209VK2H677u8DtZd-PwKObztO1ulrR27438NQ4ooxcoYQvaMnTUGmlKxFpwzBbmFZjJcyV2RHn6VgXxC3HUxQ2P1o1-WTMOY3y0v_2wDjIThbSSR4_EaCi2QfpRXVmQJu_gGBd85HSfuWjXMRd5ZT2N4aMmTGFaJAez9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=P-3pviqWVGsGpmeYdAwsz-hunAXBwzR_lG0q0SZfCm6Il7tGUkhTcHriPT9x-iACP_WwXgiuA9dq_hqQCh8l_Z2U4mJin8lYhFPsfZLLzA-eePUSS_XdARgxsHTfdBFS5pxHFp7fvXaJO3dw6Mn1k3HVPfiWALJnDdQAkFRgbkjhMyjLA3_Qq_tA-nDdXcbz1ozMfEGMDmwoE_TL9JIpMisygAuHlmON0XDL63i0JCqPP7J1Qm_XK4wVejmBiK_Xfe0tQAcQPPk3eMMyNRPN5LsjaKYxJH8thBA8kE9hs0CXh_hFnoYCYlxJnDVYCbxvgzEVw6ARh6KApikX4BdPSSDd_S7ZkHs1sIE2UHDm17EPIdrNvMmq_LJa6nC1tcuOnQswFF6sHJ6pjz3wxuVG5IozlvPoY8OXon9cwdmDeR9JId6PQSrBrFK9Vhy9brQ3V87lqUBgutmaq0KFAmnpL4Nvkqum4e2Xywnv1TZ3lfH3QQ9QRW8fHKodVoxtZvfSvU2DWb209VK2H677u8DtZd-PwKObztO1ulrR27438NQ4ooxcoYQvaMnTUGmlKxFpwzBbmFZjJcyV2RHn6VgXxC3HUxQ2P1o1-WTMOY3y0v_2wDjIThbSSR4_EaCi2QfpRXVmQJu_gGBd85HSfuWjXMRd5ZT2N4aMmTGFaJAez9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دلیل عدم دعوت مهدی قایدی به تیم ملی؛ ناراحتی قلعه نویی از عدم واکنش قایدی به صحبت‌های یک مجری در یک گفت و گوی تلویزیونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107235" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107234">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=p_4SEKbq66GYUMI9_LRwYus7UYb79vWne0-VHL-GuwAbs4CxVkRc6oGTPwxI0L52RvDKI1kjEJZ8ux1_OGtHRCJgVuju-2MEkjJ8zg_vX2vHEVV4OSPFYn4IB2gG0IWcukCz43S8-4w9ssmd2cthTDVWIH_of3KNn3_wcmu0CFwgGn0ubW2raBkb8y_769HWgrLtQUnIrW7TWNPE-ZIbXuJwftFy0krq2Wuxsl6Gi9hm-S8laSDh8Wi0FrLSmZMLmFvCkp4-Q1U3Sapq_hfbxaPT6qimQxMAjYxGSqYaT-giWRtB4aXH9rAJBx1csBlofIIh_P6--3Bynf9VaWssdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=p_4SEKbq66GYUMI9_LRwYus7UYb79vWne0-VHL-GuwAbs4CxVkRc6oGTPwxI0L52RvDKI1kjEJZ8ux1_OGtHRCJgVuju-2MEkjJ8zg_vX2vHEVV4OSPFYn4IB2gG0IWcukCz43S8-4w9ssmd2cthTDVWIH_of3KNn3_wcmu0CFwgGn0ubW2raBkb8y_769HWgrLtQUnIrW7TWNPE-ZIbXuJwftFy0krq2Wuxsl6Gi9hm-S8laSDh8Wi0FrLSmZMLmFvCkp4-Q1U3Sapq_hfbxaPT6qimQxMAjYxGSqYaT-giWRtB4aXH9rAJBx1csBlofIIh_P6--3Bynf9VaWssdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
درگیری با عارف آقاسی و تهدید سامان فلاح؛ دلیل دعوت نشدن کنعانی‌زادگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107234" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107233">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107233" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107232">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFVKJcEB1GypwOE2oTvpGfBLQoHHXWD7lehiQfuDzZq512dJMpHFHUPhhdEHGq0LCDQc-TFlvHRY6xhr2-zW_xYw2oWu6aW68uA0JRRazijobQ1B2Pc78Td-DM_aa5fvILBM-94wmaLKWakqWwcFzRY0J_OM0DaujTfcLjO8w8qsiqSm926mc-HkQPsDybEXPTLN3yOWqOfQgKRDiK5lNIvt4fbANtxzlOF0lvKKYs3W_LIqb1pBj7SHbstU9S9t5gesRixmD0MbVIKgc8jMIKdy5T8GnN4MlfbIlq2thL6tg5o71RUEp1wqLqLyeG5WdrWngJEQcTxE0Fj9VNJwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107232" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107231">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=CwwNMxPzxLjMR3njg6yt_ds5nzwLoWa-hHgWyhyEiV0azF3xRVdDI4k5d6rSZY73yR-QpOS1TwuGxYnlvofGXV40JpBRmp8PP_3Vmeqb-M3dEUX3ZFvByDuJfRYkwYbYfu4QDz9eJRCbWlRyElQxSFxJQ_hAK0lHWU6erM-a_jqbVaaCntzWWN4fDVuYosOer2yq_V1vPxaW2ZqbwVHqWMDDK6-YHnbo_kUc9ZDY2tQMd6REWQojxu4UWk3VnT-i8zZxTi0a5arNg2Br7ZBtyNCoahXYNCDscSkgUsWjxIHbNd04T0T1Nnh5B0lmqlRYyxlenFvZdt6HuhX1SDYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=CwwNMxPzxLjMR3njg6yt_ds5nzwLoWa-hHgWyhyEiV0azF3xRVdDI4k5d6rSZY73yR-QpOS1TwuGxYnlvofGXV40JpBRmp8PP_3Vmeqb-M3dEUX3ZFvByDuJfRYkwYbYfu4QDz9eJRCbWlRyElQxSFxJQ_hAK0lHWU6erM-a_jqbVaaCntzWWN4fDVuYosOer2yq_V1vPxaW2ZqbwVHqWMDDK6-YHnbo_kUc9ZDY2tQMd6REWQojxu4UWk3VnT-i8zZxTi0a5arNg2Br7ZBtyNCoahXYNCDscSkgUsWjxIHbNd04T0T1Nnh5B0lmqlRYyxlenFvZdt6HuhX1SDYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107231" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107230">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
بهانه‌‌های عجیب حسین‌عبدی در بدو ورود به تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107230" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=liWnf70k2m1HRdQ-ttcFzNP3PqeG7-FQPbZmt7_W_HNQtcffyzjuh_2SflAqBE4PAO4qoAQDG1DFWrRyTzve9IZexNXZjWjGU-jGBtdMg2SVZElatoAbK059cJ9t79IE1vHxV2UsWtVGkb-ZXhblISp8g-YQilE6OsjkONugI8SL73zdZmyyZVWN0FvEXhiS1zGHQ9E3ihsm8frw7Ts6agWy--FxMgs48AdJFCt30hiWlKMBLhuSjs6rNaeJl0X1iA1fomb1igAtudaDGq6MY1Ya5kJ0DDZx1o7o08T3Mj8reLZHE7kb2nn4Oo7Hri5frivVmRnCb_3APbFxkoj0-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=liWnf70k2m1HRdQ-ttcFzNP3PqeG7-FQPbZmt7_W_HNQtcffyzjuh_2SflAqBE4PAO4qoAQDG1DFWrRyTzve9IZexNXZjWjGU-jGBtdMg2SVZElatoAbK059cJ9t79IE1vHxV2UsWtVGkb-ZXhblISp8g-YQilE6OsjkONugI8SL73zdZmyyZVWN0FvEXhiS1zGHQ9E3ihsm8frw7Ts6agWy--FxMgs48AdJFCt30hiWlKMBLhuSjs6rNaeJl0X1iA1fomb1igAtudaDGq6MY1Ya5kJ0DDZx1o7o08T3Mj8reLZHE7kb2nn4Oo7Hri5frivVmRnCb_3APbFxkoj0-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
دیدار هانی رامبد پرافتخار ترین مربی بدنسازی دنیا با بهروز تابانی قهرمان سنگین وزن ایران حاضر در مسترالمپیا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107229" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی محمد احمدزاده سرمربی سابق ملوان که این‌سال‌ها به شغل دیگری مشغول شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107228" target="_blank">📅 11:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjwPPot97cHAHkcBEkJdnh8R3VuE9vLrm4jgFNJdyZKkVGARS920BX3RsnluPUn6a3ZL9LPklPxfbHSBVX9Lve8TbDcF5SvzZArFWu-B5OzcVP5th3Ncrr-xTg6suAwbySfR8BgJXY4mSbH4rlLrTc3VpncY67zWBizI4dCzvj-x6hnUx7kRzFx-A-wk9GCd82KlHV2_Bco6G9VJurFUH4XM__nEw99_qAJvpCnFO_U1abZ17Ji1jQgIQM0F0DUu2-vFE1boQg0Zh8LXahdwjf3qrwC0F9TOwYjtz_LITqrSqaFwB87Uo95p8KIO-zabwevH4MN8CAHmxKsPirHlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عذرخواهی اسماعیل قلی‌زاده بازیکن تیم‌ملی امید و استقلال: از همه مردم عذرخواهی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107227" target="_blank">📅 10:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAEP2S3bjKvn70oRTTNeW8id6gt3MeZcibNvvBpn_EOHoxIhTYH8DNhk1lrShwy9lWAyJwyeMu38ye00codNThYLRM5HDuEBcrA8ncXbyIPuZQUJnBSr5Pwflw9rutoxa28VH9VquFQcc-YImaQ8nEnpw79E8mJZ3qzrzE1MD0pUJzQrNkPhelmyeS41nB2vyufZnKZXSblYPb65IbkdYCTS4pF99LPYm87AxFlV2mxMqyQ21yPpEp470ncaHumJYIuxU3e8HFc3cSGdpI0uPGX3bUlxni92s9B7qJOh8Iwkbqh_KfakfGp6AhJvioorvfh7rMA3TQdHfPDrROLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تیبو کورتوا: بدون شک من عملکرد بسیار بهتری از کاسیاس، نویر، بوفون و ... داشتم و خودم را از آنها بهتر و برتر میبینم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107226" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOkPYTUn2-mmNEiWm1VR5GxAjJYap_qOVHCf-E646OyYnV_rgUoXRgGZ2F6WB5S3s_AZwe4g9RFpbNbE7EovWN3vjHHG0t9bwZB-Ps60sxQ-BymduhRcga30d-5fJgWH9Ovwa2tDMAjLVUh_Ki0n6PxC0NlXD5zOxH7GKmcb1GDvo-f5x5rD-ph5Iz7LHk0VdIUrmehdr_N-zmGcBBfPCvXYIngLsXoH1NuHXt4z9AIdu8KXNZJam2oZAKxaKhzqtL9PfJ2D4XXCqT_7tZtOWEZlnU8rFGT1QfKyZ7Jax1muZjdRJswk8u6J70mJcth7nceodtRauPwVLMO3uXWv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
رودری ستاره بارسلونا:
🔻
"من در حال کشف چیزهای جدید هستم. بازی با پاریس در ماه آینده، به همراه رئال مادرید در ال‌کلاسیکو، تجربیات جدیدی خواهند بود. احساساتی که قبلاً نداشته‌ام و مشتاقم به عنوان بازیکن بارسلونا آن‌ها را تجربه کنم. و اگر مجبور باشم یک بازی را انتخاب کنم که بیشترین اشتیاق را برای آن دارم، پاریس سان ژرمن را انتخاب می‌کنم، زیرا آن‌ها در حال حاضر بهترین تیم هستند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107225" target="_blank">📅 10:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19143fc835.mp4?token=V5f-ssKvnI_jJsOeUFvv8YQtM01LmWUzMkzpjcWS5eNzJl7xUfYQz45esk84f6W7vp1j0tISvtlgFiK8XG89-ChNIGbKZ_enaxwf3nFpjOP4TRXVC19vANCozRLM6GKIbnc_-8PUNjWYRQpzo3LewMXWQBQdKrEN9nw_FsqK14ZzSug2o-RTqrgCLVjReGLJs9v1U0DNU9n9wDcqx-5oTyrNbFhaG26bxyZ5hdkY-PAD2RZJFgdMeXrvzvO3t5_C4ZgHBVVZ8_G3I6VswaTzX0OvSCWMzIHQvtJVXAv4jJzqsAsqIUjZOZPL_yshp5fS19u_HgebFjpvn29q7UenfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19143fc835.mp4?token=V5f-ssKvnI_jJsOeUFvv8YQtM01LmWUzMkzpjcWS5eNzJl7xUfYQz45esk84f6W7vp1j0tISvtlgFiK8XG89-ChNIGbKZ_enaxwf3nFpjOP4TRXVC19vANCozRLM6GKIbnc_-8PUNjWYRQpzo3LewMXWQBQdKrEN9nw_FsqK14ZzSug2o-RTqrgCLVjReGLJs9v1U0DNU9n9wDcqx-5oTyrNbFhaG26bxyZ5hdkY-PAD2RZJFgdMeXrvzvO3t5_C4ZgHBVVZ8_G3I6VswaTzX0OvSCWMzIHQvtJVXAv4jJzqsAsqIUjZOZPL_yshp5fS19u_HgebFjpvn29q7UenfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌صحبت‌های بامزه ابوطالب‌حسینی رو برای دوستان خرج‌نکنتون بفرستید
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107224" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=s4ERzHpXeOnlUhByel1g3_IMPIKO3apiai3sTgJn8wLqGRjf6pht2hvPl08XSPD7USuVhBLkN6EeydddQqAQG7xBBVf5hD-Tf8TgMuKXiahm6UmNH2Hlj5P-TTBo6V9I9NOZ4ynfK9lUcBPbs_VsPM0UQ-Dpdqh8Unyf34rp_ZCrWdxIZPFdbgg4lYn6sGs4wn4_XwV56REGW35diKagkm8v60Mrqk8GEkbiw-tOHv_lZeb6PJ6ujenDIrM-QtQi28fye35nZWRW5k3k4yIffxoH5m6FsMRzSGthAuiHNQMXzqeuZmRNBBNw5AMx_1r3i1UwXQk7Msm8IIaR624Idw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=s4ERzHpXeOnlUhByel1g3_IMPIKO3apiai3sTgJn8wLqGRjf6pht2hvPl08XSPD7USuVhBLkN6EeydddQqAQG7xBBVf5hD-Tf8TgMuKXiahm6UmNH2Hlj5P-TTBo6V9I9NOZ4ynfK9lUcBPbs_VsPM0UQ-Dpdqh8Unyf34rp_ZCrWdxIZPFdbgg4lYn6sGs4wn4_XwV56REGW35diKagkm8v60Mrqk8GEkbiw-tOHv_lZeb6PJ6ujenDIrM-QtQi28fye35nZWRW5k3k4yIffxoH5m6FsMRzSGthAuiHNQMXzqeuZmRNBBNw5AMx_1r3i1UwXQk7Msm8IIaR624Idw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
و بشنوید از زندگی سخت دیومانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107223" target="_blank">📅 09:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=e99VFxZ_5JRXD8TM0VcYll4yHAnIsIV8j0QRJVgBkEvdNwE2zb9s8JpNopvUAQJLOMBE80jRdto0bkKP3d1C-uKRoJYAc4OuHcIneDJeyzk-C8kpsAmtM-4r3uEPFLEw5rqoOPPDxcXTKGVoUlJHs7MNfsxmRfRwfTLZsZb_mdjKMF2dgcGPx66n6vyi_Zo8WoldLpCFDURW5YYLCdbdFI7sRa-Oi9FFoteG_VlyiWPU1ZjXe2qAVsd84zODl_mY5AcwKtMmEgA-iitsheiaT2Wb3lGsA1Xnt9NdALKuqob3JW4eXoTBwbQrbaS0zGXBo1Vkh7ng6GIf-vncwrKW2VTHswCPAmTQboX0Auco-DUlQvYHYSWwYIBX7iN1M7w39BVr1aSqFWIxjRBwOq6Ns6TuMWUMLQqDheIWWOnrPa0tSvT1--Ipv527YZg5NtEZWPzdowz9bYDR_9b08hkwy0oTf23irjy8FywG3Qgv5FniKoKv2jxo8jnkTNCE6sS_9oKo3NIGL9Y21NJ_nXrAcuSc6Q-y6UHUdf17wTkl4ZD_rO1wcmvqpmOCGBdlwqvWcV-E5pWfaFjEYuXwTdgWvgGqRp7u5plDVpD9LSxCuBXNaEkCU-TQ7U1OjIXZiiCMhcyxlev1Wk-O__MoptOowTUcvbWw745VFSwknoJlbPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=e99VFxZ_5JRXD8TM0VcYll4yHAnIsIV8j0QRJVgBkEvdNwE2zb9s8JpNopvUAQJLOMBE80jRdto0bkKP3d1C-uKRoJYAc4OuHcIneDJeyzk-C8kpsAmtM-4r3uEPFLEw5rqoOPPDxcXTKGVoUlJHs7MNfsxmRfRwfTLZsZb_mdjKMF2dgcGPx66n6vyi_Zo8WoldLpCFDURW5YYLCdbdFI7sRa-Oi9FFoteG_VlyiWPU1ZjXe2qAVsd84zODl_mY5AcwKtMmEgA-iitsheiaT2Wb3lGsA1Xnt9NdALKuqob3JW4eXoTBwbQrbaS0zGXBo1Vkh7ng6GIf-vncwrKW2VTHswCPAmTQboX0Auco-DUlQvYHYSWwYIBX7iN1M7w39BVr1aSqFWIxjRBwOq6Ns6TuMWUMLQqDheIWWOnrPa0tSvT1--Ipv527YZg5NtEZWPzdowz9bYDR_9b08hkwy0oTf23irjy8FywG3Qgv5FniKoKv2jxo8jnkTNCE6sS_9oKo3NIGL9Y21NJ_nXrAcuSc6Q-y6UHUdf17wTkl4ZD_rO1wcmvqpmOCGBdlwqvWcV-E5pWfaFjEYuXwTdgWvgGqRp7u5plDVpD9LSxCuBXNaEkCU-TQ7U1OjIXZiiCMhcyxlev1Wk-O__MoptOowTUcvbWw745VFSwknoJlbPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
❌
زیباترین ورزشگاه ایران، درست در کنار یک آرامستان؛ بررسی شرایط عجیب ورزشگاه تیم نیکاپارس چالوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107222" target="_blank">📅 09:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTIJ4H5Qckm9d8nZ4Xoi3Lb1vIJvgB01S_icQZQCjdLPtGVvD8iKzhqmYMRwOD9OT7BNaKvCSngaN-9NdtKAMvZhGtIFDJ0zwp5Vbk5G4lkSeux3yKxLoiYOawfoGi5IrHm3QhfD-awMuLovvsJZqkNfKjZhvU0Z0gqVoe9AWI93V8JlM0kbjNGruKVl1EU_KAmuj8ZjNtwZ4gVnO2CdhnomMmEUKDM8kAsSZkOW1nkN7st7xcAGtVwcNoqXdv18PBbA0BswSX91C1zo3EWvVhgEQRnXcIF_Qn1gE73bti7h3wucaIO0jBbFkW0wh1WdfxjLUAkRJ8U5SNH1PHdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
دین‌هویسن مدافع رئال‌مادرید: شکست مقابل اتلتیکو تقصیر من بود و بابت این موضوع متاسفم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107219" target="_blank">📅 01:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw4y7daYRYdEiDXuO7oPVNEX6y_dRiLws9CGnWMxt_7C5SoLpA0k-kyoJiUsLqlXQT-rm1vZeZ3yf-JPovOBubywClnB8SRGcujEn0SQlI8hXIzg3-UL9-sl3yu7yZfEVR8wKeZWt087i-nAWbMrtY4w5TgSZRUw_6KPjtVmXfvkoktz5jtg3u6b6OKhIJS9Hagn_AT0ME201OCVmxjHS3aGQLP3wTDp4sWSBcxdNUsYMLLm7Pl_CWsZi0uyqA-tvEkJUXCFAbxutbaWUWACSlkQ4ZI2WbPLdwkfE-q4QVmSTu7TG1spUzsBwSkQ4ZqPal-u5xKDbS9oY4TF93rQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
مبین‌دهقان بازیکن تیم‌ملی امید و الوحده امارات مورد توجه سهراب بختیاری‌زاده قرار دارد و در نیم‌فصل قرار است مذاکراتی برای جذب این بازیکن از سوی استقلال آغاز شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107218" target="_blank">📅 00:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=UNaGdXsTaJA4T1CJOnLPXlG0XZT4zdpWOK7afE77NUqFuIPVtoFf8jhhArDfVNjMMhcTtKfJZXnTg2JdjmhU2ooX5f8M3IGvS0ew00JVT2Kx8IeU63SARNVBIFaEyyo3BTEgMUZZS0eVzTvQEFdR76fxaXc9Op7nB9dHaa3Gddg9eFb67BmPv0s-uo9g1op9bRJlI2d_iRgpDUWattvuMSihLBRdCbL0PY5mNQY-tzUaCHzrdAps0NmbY1V-vX-La_Hm3Oo3HcxRo-0MC6p99weeDHM10mBA1uFaQl0TF0w7f-tqIBHMXjKgoekkN__O6TE1UZtJQu2ODTYq44NcCW7aLOkmxY1lX1adL17fwpWhagCtKsRO5710ITv6iSpG9CmXZ_x8DiKt0e8chCniN9TsxSXJeSgIOC02t9Ps-koBQwbT_yJraFg29F2hRe-TinXX1A2V96oR57wM9FRGETbwJUjnKoncUm9wbE5ugZ2lzUUtP4812VXADrDbhr4FVtOK3Oqg4MrirdzA8qXhmPPGZmAzsgRxyFvxtUM4KeeJrtW37WfY2Puz1KECXKoI7s_CA3PS6Euo6Pfe_2Pt_2KPnFLrfbyJxS1Yn6jABGfq5cqWD_5UayrKpvpOC_7uCfrL263oF9aubpFBuH_2jRebbmKDzkZp7PWnoL9kQBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=UNaGdXsTaJA4T1CJOnLPXlG0XZT4zdpWOK7afE77NUqFuIPVtoFf8jhhArDfVNjMMhcTtKfJZXnTg2JdjmhU2ooX5f8M3IGvS0ew00JVT2Kx8IeU63SARNVBIFaEyyo3BTEgMUZZS0eVzTvQEFdR76fxaXc9Op7nB9dHaa3Gddg9eFb67BmPv0s-uo9g1op9bRJlI2d_iRgpDUWattvuMSihLBRdCbL0PY5mNQY-tzUaCHzrdAps0NmbY1V-vX-La_Hm3Oo3HcxRo-0MC6p99weeDHM10mBA1uFaQl0TF0w7f-tqIBHMXjKgoekkN__O6TE1UZtJQu2ODTYq44NcCW7aLOkmxY1lX1adL17fwpWhagCtKsRO5710ITv6iSpG9CmXZ_x8DiKt0e8chCniN9TsxSXJeSgIOC02t9Ps-koBQwbT_yJraFg29F2hRe-TinXX1A2V96oR57wM9FRGETbwJUjnKoncUm9wbE5ugZ2lzUUtP4812VXADrDbhr4FVtOK3Oqg4MrirdzA8qXhmPPGZmAzsgRxyFvxtUM4KeeJrtW37WfY2Puz1KECXKoI7s_CA3PS6Euo6Pfe_2Pt_2KPnFLrfbyJxS1Yn6jABGfq5cqWD_5UayrKpvpOC_7uCfrL263oF9aubpFBuH_2jRebbmKDzkZp7PWnoL9kQBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بومیان استرالیایی این‌شکلی از بازیکنان برزیل استقبال کردن
👀
💥
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107217" target="_blank">📅 00:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107216">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgL9ApANtAxM8CvDht5jXdq6sUyHXrScXr-WcZnb-hZSUZv2EHs7wh2LMxXkG0Iup1qvM7W421-ICrBi22uXr3qtRFbUeGrb3HgpW9J12TURJ67zDLuPY4NoMD2Art8VGHOpo7ffnstjf5ANY_hR7cw-9r9ojZYsrUFiSOMganU-Mv2x51-liBtu69bi-3anu6HoCRm1_EQIn-qml3srsXFvTrXe-t6fGKQmjT91PsSUDEDjleKJgp_AC0cMEbjZdTXuyY2PAg0VqnXFVriH-Wfy-paZfVOI5ABpz518ux23SfTi3GcGV0hD80zJmN5WxSxDnTUY_Xk095kkC9pw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
نتایج‌بازی‌های امشب لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107216" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOeDMOqCm3WHgfQ9rflc6UOK-KiAox2EeeqVb-wNNgzrb9akEQuav57Q1SobymG_NeVIDIYoVDRv8x24x54be9EVRVi5pfqNXMVyemoxDfW-_rtXxlXNTVqseplxdzXFFpTyvnq7WUBBkfXVR6xFPErwTR_ciZVEEj1nptXeT9rRGBlW85o1YadY0Uzr631VcPwsQ6rylzZOuRJxHpT3HXqRqjlwJNpvweK9vmByN83b1sqqLCtTLFmqTWIPxilV04O_kYUiBc0rqo5ZRIkAPAVKhXOuxDU40J7RtQMN-2FfBgjHSY6vFfrk9mxd92ISNakAhL36sBxnfyIkq_9jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107215" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی: چرا همش با ازبکستان بازی میکنیم و میبازیم؟ با این تیم در جام ملت‌ها هیچی نمیشیم. بازیکن جوون هم که نداریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107214" target="_blank">📅 23:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOdJfrBT4wLr8uEW-YUiKAh_iaDq0Wb9oNGurAGw--hK9vJaoeRM7WBawjGkCcX_y76YSelfk2GwtniNd-TlsLqz1YidNy5zTiCy0IqfrKB4A5YX2TkuvrQxk0q51BYPrclIqM1QLD_t5R3FEo_UDurwDz-9xg2sv-gzmckUqOZdNbMVgtGyrBeXucJIN4ZrciicdREKm3OWxqITnhjCO2mkHNuL2yKOhUPxxYxaZuRlKmxtHnHleYPm2er2t7wnb9x0HUyzZmKydALEykSIVGVip-Dffw_KgjiWh40y4UTo8wzM4ET3fhDo_p2WOWkg0CSxSdc09lVvw5U17McWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدووووو زدددددد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107213" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107212" target="_blank">📅 23:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnvPxF3zxG-Kcnw09Sg1-xw3g4dSe8ThaoH31whKJ18G5YmnE06pOt7gVjiWo_iSc9WZy1K3D4EOsLvcmKYxCZArPnHQ6Be2cTWIlN38ijvdXEavUjjyn_Qvi_9GgrB4ldOKWYQydLdVv44bhQRCCvOxZ58X0hnJbtDnffQmVe20ExpTpM2KYYVvZh7g7zu8C4mzKJm7qLAtXRT7lJK3j4vbQUMRyl8TRmObdMgdgSzpk5yVVPWunIsFObzFzR6XcZWh0-kYuvO3jfxNdnVVd60-cqXSCK-28cCkGbIQGtwX6dVARBFjtPk2O7nTMw_6c56zl7fZNJLpQi6PHtX8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107211" target="_blank">📅 23:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEMPGkmersSZtJQAg-DYUNaeeFui760pJcdpj0YqH9KsdFi0RKEzdbKhksQ3dO9eZVbFBkVrijO7X3qIbqlaFdlCU6EZ1RRfCHkOVIzfxo56C2tzmuaolHrIBCJXhI1aNRBAikkjzjblGbc-Z1NZVdl2zNHndJXBcCKcWqw9ZskgM5Mq_TcBqzQGkaD2-cbfTpjfyoFlHjdqKNvfXQuskS17zupVv2lt6-nNNX-AyPShnBf5a5EfRv-akRuKZ4IwdN62vCE0GPvoPMEbCFSRTH3Wk205gW6G_n0p3wc3oeV0hTnCQWN5mcpv5ng6H1aIgg8WHvotogQWys8s7CUiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107210" target="_blank">📅 23:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZRDn9o7XArqKIiOuAqQeNNHRW68k__3soXgJdWwBTOzZQD8yW9BK5qPrxu-tq98EvfuvYMfpyy-z_DL4h4gjc4ejcRxfe2l7s7un6CmkjAmaEiZAmvuMTt1urfzTHXrTqQODYS45ihYXadkagNT7EY6v2HtQ4iY2MH1I2brCHE0mmZPxD858CXKL42O9q2ugP1tMXEMKERvi4ESWJMRUT2AjANQAF_EIgM4C_hA2xNBaLdvVUiEW--5uFQYeKW7oCufOrv9_MngjuS8Nt7auCiJLL30L2FlLQ_Cw4xyHHnn4_lF6p6jmmBU2ihde4eiMNrumWT3eUO2JKth0iKkAAbs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZRDn9o7XArqKIiOuAqQeNNHRW68k__3soXgJdWwBTOzZQD8yW9BK5qPrxu-tq98EvfuvYMfpyy-z_DL4h4gjc4ejcRxfe2l7s7un6CmkjAmaEiZAmvuMTt1urfzTHXrTqQODYS45ihYXadkagNT7EY6v2HtQ4iY2MH1I2brCHE0mmZPxD858CXKL42O9q2ugP1tMXEMKERvi4ESWJMRUT2AjANQAF_EIgM4C_hA2xNBaLdvVUiEW--5uFQYeKW7oCufOrv9_MngjuS8Nt7auCiJLL30L2FlLQ_Cw4xyHHnn4_lF6p6jmmBU2ihde4eiMNrumWT3eUO2JKth0iKkAAbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=gNt7n_wyrAC4TxY57jfabAel2tNxkrltQGbtS4MSQbyV67u4rGrItYo1NCW-y3avBie3d3paTO6DEXI-c4-MVsUeh-yNV_Pdo1ZbxWeqBajdk6pp-GI6A3Y9iqg8iTptVC_sCf_79txqHlU39LynfZWg7FfqcinF7KVZXaS9P3L7iE34k6KQ8-4dBQ15bJrRvweptxbvMmxaDyIi-KZaxYJEVo8kpmNm_58EetZLQgcry0fVWykbSZrZd0cUTcb4IXP-NSQSsQViIXeWiCwys_ZEGRvx5qAuSQMAKdE2_7L1IyvrlazYdY49-I2i_PyVqPiGJgUvju9zopD3fy-DSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=gNt7n_wyrAC4TxY57jfabAel2tNxkrltQGbtS4MSQbyV67u4rGrItYo1NCW-y3avBie3d3paTO6DEXI-c4-MVsUeh-yNV_Pdo1ZbxWeqBajdk6pp-GI6A3Y9iqg8iTptVC_sCf_79txqHlU39LynfZWg7FfqcinF7KVZXaS9P3L7iE34k6KQ8-4dBQ15bJrRvweptxbvMmxaDyIi-KZaxYJEVo8kpmNm_58EetZLQgcry0fVWykbSZrZd0cUTcb4IXP-NSQSsQViIXeWiCwys_ZEGRvx5qAuSQMAKdE2_7L1IyvrlazYdY49-I2i_PyVqPiGJgUvju9zopD3fy-DSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=ptOHFqmFCEPcEPM-NPotOJJUhmrqyk4Z1-j5Zj02CE1O6P1dlve5RkfSYl7F46LmSjAC5dHIN5lAVNqBnLxSznXN6aVFhaou8TlSVuvbs7rtpzwDRLvDRwflXBU6djjIASyYNzhEhXHpYqQhST4iA7da2h3DKYvIjGkSxo83FQ1brlke-Tfvfie0-8PAIGU26mk6BEjBC-1qObXXGa4w8JpQiACPTlu2uCnEnWYbF55IcfyYuElk_yD-qzeIClo753QiPqvc6UhHfxJ29nHh8Ook3NJYDojq3Q1ucAPa7CnMH1PmMdYmdcsPH2iYMrVvnuOhEvgaRgCpzrfhkU_4aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=ptOHFqmFCEPcEPM-NPotOJJUhmrqyk4Z1-j5Zj02CE1O6P1dlve5RkfSYl7F46LmSjAC5dHIN5lAVNqBnLxSznXN6aVFhaou8TlSVuvbs7rtpzwDRLvDRwflXBU6djjIASyYNzhEhXHpYqQhST4iA7da2h3DKYvIjGkSxo83FQ1brlke-Tfvfie0-8PAIGU26mk6BEjBC-1qObXXGa4w8JpQiACPTlu2uCnEnWYbF55IcfyYuElk_yD-qzeIClo753QiPqvc6UhHfxJ29nHh8Ook3NJYDojq3Q1ucAPa7CnMH1PmMdYmdcsPH2iYMrVvnuOhEvgaRgCpzrfhkU_4aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=CVP2pLYmELTL0fqyNKi5m0fqvSm91v3qwrGm6ybdIGkrteY5UYEJjkLvM5cFBd5RvrT8_Me4XeVw98tRJ7geHBXvX-bKNiqQdn_3uF4NWUx0v4gx3BQJhSEjjJRNhQ_YlzPnCTtidKwwF429NBKj8k_xIJYwsYMUUclf2-74cW-iMQHQvQr6ZFrI6oiuy7mDFaM8S7qNeNHHZZBa1ukx1oA3fr2PePCpTOp34QEgJj9ZMDejyjutot0jTOT1dxB1HqrA6Vm6q53sPY8qARm_h_S_CxaVTVXPpOz8YNrNYnOEufw4Qu82pLSQ4RBIKTR344iuOdtTdnJ43rFQS32X6phk0doCXJp9RO8QrM3f8XPmBxv2faGX49skYWEogrvkmo5rsPi5haO51j10gjceir3OhMUGn3rSNyf-LdcFmCfnMDSM-OtDJ2Iy0ALUZ2YzcAgPwllPKTc8FxR0_qeOkcevCsYAgNcuc3YP4GZ99pfAibbByN3apEhu7E0CfOLvNbQmx6DS2LvsKIiJn7FB8fzv8MC5k-Y1p1a56lbP-nzLYvW2hsFKrL25IXzSXgZToeGotlQuhgGm8Lw_jyfdoiItxQXZzviTgB5AxlWqVLrMImHp-zrN3mOQt4TcPdhgcyj6iDdKhSti4d8wtE4jd-fRTmOdc_9ytnFzVrjeMV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=CVP2pLYmELTL0fqyNKi5m0fqvSm91v3qwrGm6ybdIGkrteY5UYEJjkLvM5cFBd5RvrT8_Me4XeVw98tRJ7geHBXvX-bKNiqQdn_3uF4NWUx0v4gx3BQJhSEjjJRNhQ_YlzPnCTtidKwwF429NBKj8k_xIJYwsYMUUclf2-74cW-iMQHQvQr6ZFrI6oiuy7mDFaM8S7qNeNHHZZBa1ukx1oA3fr2PePCpTOp34QEgJj9ZMDejyjutot0jTOT1dxB1HqrA6Vm6q53sPY8qARm_h_S_CxaVTVXPpOz8YNrNYnOEufw4Qu82pLSQ4RBIKTR344iuOdtTdnJ43rFQS32X6phk0doCXJp9RO8QrM3f8XPmBxv2faGX49skYWEogrvkmo5rsPi5haO51j10gjceir3OhMUGn3rSNyf-LdcFmCfnMDSM-OtDJ2Iy0ALUZ2YzcAgPwllPKTc8FxR0_qeOkcevCsYAgNcuc3YP4GZ99pfAibbByN3apEhu7E0CfOLvNbQmx6DS2LvsKIiJn7FB8fzv8MC5k-Y1p1a56lbP-nzLYvW2hsFKrL25IXzSXgZToeGotlQuhgGm8Lw_jyfdoiItxQXZzviTgB5AxlWqVLrMImHp-zrN3mOQt4TcPdhgcyj6iDdKhSti4d8wtE4jd-fRTmOdc_9ytnFzVrjeMV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=rlYFQYLS6_YZCbST-28WofW4tPoylg76lAcdkE97SjbQJf0NLO4eRwtwio7qPyGBtKDXhRq9_ptx7iCjHbJsecFuKN14VQvw5z87VaszmcDU_FHZq-8H_BoAgGNitgC4-n4frc9RzoCaO6GUR-7wmM7Xq8dZ1A4lbDjsPJGEka6i3KJPb42w89zA6RDoFGJQHGAhZfE5jHukyOyUvtOUrxpPl2o49lnPvfJV28fGyi3J2D54Bk4bW4cT-QBUebPgzviPGGa7wfmu-Mn4WDZ_bNHFf6fXHqyHKcznytXm0yQi7eNfJhZdpzOKlsetUZQS0OSXTt-iegxximC3bEirJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=rlYFQYLS6_YZCbST-28WofW4tPoylg76lAcdkE97SjbQJf0NLO4eRwtwio7qPyGBtKDXhRq9_ptx7iCjHbJsecFuKN14VQvw5z87VaszmcDU_FHZq-8H_BoAgGNitgC4-n4frc9RzoCaO6GUR-7wmM7Xq8dZ1A4lbDjsPJGEka6i3KJPb42w89zA6RDoFGJQHGAhZfE5jHukyOyUvtOUrxpPl2o49lnPvfJV28fGyi3J2D54Bk4bW4cT-QBUebPgzviPGGa7wfmu-Mn4WDZ_bNHFf6fXHqyHKcznytXm0yQi7eNfJhZdpzOKlsetUZQS0OSXTt-iegxximC3bEirJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4NzPFK-nOIxqP5twmIItes5z5I5gWl8aKIKx7nxBomIac_9geEiuc73GHSQXkccG37w2djiBMeq1m-euK7eHF8KoSeIvyy5O81LodpcTyFzhtClcrz0309sdlGk2yj-_c9_VzX97IAMFUG3E5LSAspNtTZCNojURmEUu6zXyX2_quFmWXNLmIZ30y_5nRdjAjJg_DaKyIPs5G_ssWeM9I_S_OX_EgqaY5J9GY7vIXMRVxuo0jW4UivgnBBARskO3K83HKgG-kqAUiAcDiurO6QbD5Lvmb6HU1CjOtNV52JUgiWaqL86CHv9QLOiwVA-f0OorhlFJvZ8d4xERPg22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Xvqfuys9EHYbfwUNU_ykUKUZ4Gs_rCyBkpkB-mqaQY_0sHa3SbT1pVsdP1Ok8gn4XKey7xS9lklIgR_7BldobPSaLdbiA-HFfLK16O0BlUaex_FEI9QDwXbjW2XkYUypSfzRd08S5iRbrxAE9IQWxVkaEBbgDzwACt8PqjfOUYduGNQ0o2wTFfiPd5ubUhs5JTQUwJKdyeGG3VbAqrOX0ef-SyAWBt5qxIxgoMt36KzDrH0NAa39ruiLWRtVfibtqmW6nZNE_CKku-qLrOax45cHm2YAzxKxIaT7WZd-HTPEhgYNvvmA7pKe-yatHWwD48yd2oG8SuxjVh0yz03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
ترکیب تیم‌ملی پرتغال مقابل ولز با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107203" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=ZacMnHAn2ph3GU_STNBI0fd7xYg7sHYC9CEbIKVwUwt1oBrfvclKw89zbNJTdujnPFZm7261Hd-upsPrTWc54JA_6eBZrIC9U2ltdEXFSD65QQi3DmDPTHNYZRxh5XUMLdZtSpli27H0TnIiUn2D5NWJZ4nleggLzr_ceNNSDBtQDvsVHbhMbrV-qIAHZ1sZ5VM_IuVHKM9DvjD2tkRrZXjlgIre6H6dJ5D-lrvb4dHRSrSGxPr50JHQBOKR1p_8y1sawGbvep-MEzBpFPWKBFUfQIos1uHGLvsQD2cVtkrAO4amCxi15JZdf0p0xbLDa3uubNlmgplM0UVwpvd50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=ZacMnHAn2ph3GU_STNBI0fd7xYg7sHYC9CEbIKVwUwt1oBrfvclKw89zbNJTdujnPFZm7261Hd-upsPrTWc54JA_6eBZrIC9U2ltdEXFSD65QQi3DmDPTHNYZRxh5XUMLdZtSpli27H0TnIiUn2D5NWJZ4nleggLzr_ceNNSDBtQDvsVHbhMbrV-qIAHZ1sZ5VM_IuVHKM9DvjD2tkRrZXjlgIre6H6dJ5D-lrvb4dHRSrSGxPr50JHQBOKR1p_8y1sawGbvep-MEzBpFPWKBFUfQIos1uHGLvsQD2cVtkrAO4amCxi15JZdf0p0xbLDa3uubNlmgplM0UVwpvd50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107202" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVeVXfSI6t4H4RQsHIVTSLMeWywDi8HKJalP-_ECQDXXjk5yqcPtyZ-l6uSUJBp9c3ZPJlHJAOHsrT8waE6VUufLg0OJKMhQXCPnqaREzD2hRePciQgw2jDw4YehcO_DRiETEQ4YiL-ucW74Y6mZvGm93JQ1ztX2hSGGoVHNeQN-5H4WDxjPHqxyZ38mWPHDvoqx_uSr1sAg5AFk5BMWAIZe4RdVxaEkpr5xGMNXwK8Nb-GItoIoX8TD-0JPRQ2bMQuxSG81F3zEde_PbbuBYaC9DLB-1X__piaYn0_ufqgXqZl7XchGgxawKkWIMNNlPHuzJ6eUd6IZGJJHJbTkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
🇩🇪
اسکای اسپورت: بایرن مونیخ در حال بررسی امکان اقدام برای جذب دنی اولمو از بارسلونا در پنجره نقل‌وانتقالات ژانویه است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107201" target="_blank">📅 20:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=su7pfiLS4RJRpK0WnJWVMWUxzQ7fMPw0R3qqFlA6gm6ZHoFV1IvVdJMpkv3XBFAQvyGZUq-X9r4bQP7vKe9GAMk3FfFxx4ywRuLhqsNP9PXij0i8-Xsd2ErN0JLNpEtbz2UP3OpXSFFyTPJqZQg1NqQvphp_TR36z5Ucg2W28ILqXir-PD2dQK75WCurUiyHIseuCGtfKLWjqxCxSXJuxDOZFX0_03vgm3BgLI1aES_5cxHJ3VbxlZKWUcHM8FPjmfycZSK0CYViKV0ORvdofIeO3j0isq0Plkt3QoakdkWAtlLOz5wKRrG3ADKXucBZ-hJ9O1hu2ihvaehRMtILLh33yaD3PR6Y8YWGfC3N25D4a4DHI-wG4tJNNI84HXH0z-iJN3rAJHfVthsmvem8fP1JzXA2A217BzRDaRV1awfPKGrgFWID_lJA9WJ3ygonK8VpvUw20GYVSXJlnzdPc8Bfkk_Z2rLssnqLB0KfzFxNhMdNWcjiApMI0IMYZNqLOn38aGiELF_FcYJEAhIrv9YFWe46ifcLBUsKnMlLxF9myN_8bTthjM7IyFN_7bRnuiPvRqwwQm0GwCzfiiysbZIp-yBvDzrcCkuOLFUIK7GYMF2D8VrERAtLDHVLvWSuCMSiZ_xxCCHMqHR6wAYFA5n0FheeG4W6z5SDnvqdQ48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=su7pfiLS4RJRpK0WnJWVMWUxzQ7fMPw0R3qqFlA6gm6ZHoFV1IvVdJMpkv3XBFAQvyGZUq-X9r4bQP7vKe9GAMk3FfFxx4ywRuLhqsNP9PXij0i8-Xsd2ErN0JLNpEtbz2UP3OpXSFFyTPJqZQg1NqQvphp_TR36z5Ucg2W28ILqXir-PD2dQK75WCurUiyHIseuCGtfKLWjqxCxSXJuxDOZFX0_03vgm3BgLI1aES_5cxHJ3VbxlZKWUcHM8FPjmfycZSK0CYViKV0ORvdofIeO3j0isq0Plkt3QoakdkWAtlLOz5wKRrG3ADKXucBZ-hJ9O1hu2ihvaehRMtILLh33yaD3PR6Y8YWGfC3N25D4a4DHI-wG4tJNNI84HXH0z-iJN3rAJHfVthsmvem8fP1JzXA2A217BzRDaRV1awfPKGrgFWID_lJA9WJ3ygonK8VpvUw20GYVSXJlnzdPc8Bfkk_Z2rLssnqLB0KfzFxNhMdNWcjiApMI0IMYZNqLOn38aGiELF_FcYJEAhIrv9YFWe46ifcLBUsKnMlLxF9myN_8bTthjM7IyFN_7bRnuiPvRqwwQm0GwCzfiiysbZIp-yBvDzrcCkuOLFUIK7GYMF2D8VrERAtLDHVLvWSuCMSiZ_xxCCHMqHR6wAYFA5n0FheeG4W6z5SDnvqdQ48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خیابانی: تیم‌ملی با امیر قلعه‌نویی تا دلتان بخواهد به تیم ازبکستان باخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107200" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=SeE7-llxjCRwUwhKAA4bYf_Yq2eH-NTIlP28I9Cd3-VjV5T10hnwQxnR8veOSUrP8LI0DeWKTPS5ezMTc_3VW0kO8WuHGq2bKjAUzKc_fwsvreKbE4-TCF7qyBgqp5PRwIkzpcN14oH735m5xYkmRLnW2n5mp3edFF8JLvnjhcDC8-5kx1sAnMXiMiFXUqgryITShfqktB4h8iuozmf1-4MvqFdCHPDpKKeuqWrlb8rMTofGYGqW-3fcryqsL0cToDL-GGwiJHt9rNwiV0GAvANgMnLSXHqxaWN1YTUpea61nBtO-f08qch0HqrUZFYwlRZjXJfIfXadCw1LFGKB5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=SeE7-llxjCRwUwhKAA4bYf_Yq2eH-NTIlP28I9Cd3-VjV5T10hnwQxnR8veOSUrP8LI0DeWKTPS5ezMTc_3VW0kO8WuHGq2bKjAUzKc_fwsvreKbE4-TCF7qyBgqp5PRwIkzpcN14oH735m5xYkmRLnW2n5mp3edFF8JLvnjhcDC8-5kx1sAnMXiMiFXUqgryITShfqktB4h8iuozmf1-4MvqFdCHPDpKKeuqWrlb8rMTofGYGqW-3fcryqsL0cToDL-GGwiJHt9rNwiV0GAvANgMnLSXHqxaWN1YTUpea61nBtO-f08qch0HqrUZFYwlRZjXJfIfXadCw1LFGKB5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقادات تند جواد خیایانی از بازیکنان تیم ملی امید
: برای کره نه مدل مو مهم بود نه قیافه. بازیکنان میلیاردی دو زار بازی نکردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107199" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohfchtb0VrkSRWA1YPA9KpSizbGrOD3I79t5Ii9dB4Jp_m6ShbRIE9sZC3pU9YJ63cu4e_Fxp4chxwZ-EMONGfW4Y14xQOSjIGm0o7RS1cPG4tTq8jt89Rw27bfws7eXJnxEbC_O35ZzqymZdXw8Gh1PLh2QH1LBcudZ9ZIh1G62YlQDDuw3MN27HfIqRYG1Ty1U5QlwFjKxofTGEkPAZm8_-VFq_klxfkq93EaRUH_3PrU8tOMCbpKIiPxmH5hzg86GSuLTKwjSwhR0z_egEdv2FeJFFGr0TUreh0Cqviupw1DLy03ign0jNDxIDecVL20fQH1hXGDg6jNioRTrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107198" target="_blank">📅 19:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=MVICWi-wZi5LeUpL1Js6l7Yt_UEMrCjHSXgSR90-7t4PmCZ3JJ2hNa4g21XydsLM_mXECXaoJCHC9X-VquP9CGfgg1F8Kj0KfzyzzhlXAHzzMP83PtF8J3ujRlWJIosY_0ivnFJE7QcJIa0GgKST5UmOvwKK_XsGtCxi3lMalKVE9ORwwih7PBOfZcaRTayOl1DCcpMVQRAMOfI52cP5n-jEgy1DoFifVyeekNNwdsKA5g8yKaZy080YuqGKQezDETuN_1mCNJcyllMFAmJtaLbATP5Jigfha7Jta4uaGXj98DQTrWbrGO-vfEVttqgpwtdbtmoxc-z3XbtlwfbXIx2M6a5058D7azNV_-AtiMeDjgUe3A5b3cgXoNe3MXni3YiSbuIihN1wnlvv5x1Zulek7GhOBga7NHuLYUigzzVxlXMD68PF94nhAVq2AWBPYBLiqcqzXJWrZeSfBZkAlPxWPkuBiPkQyL6CpidlcK9nPyC_A5GyaHXRecURlIgunAt2OLI_X-bJoe4XHjrWqXU5t0LO7aSBb3fQhQUNjty8lofe-AvxYZhDYyN80ojyF1B6OL3yuxqnVeuqQmCNeMO2wj0fER03LNp0lM3vMNGt_grC7ofU0HmtyQRzxOJ8Xvm7KkhFJYfvpDNXcTB8AxARXVXTfftGHDOjcJd389M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=MVICWi-wZi5LeUpL1Js6l7Yt_UEMrCjHSXgSR90-7t4PmCZ3JJ2hNa4g21XydsLM_mXECXaoJCHC9X-VquP9CGfgg1F8Kj0KfzyzzhlXAHzzMP83PtF8J3ujRlWJIosY_0ivnFJE7QcJIa0GgKST5UmOvwKK_XsGtCxi3lMalKVE9ORwwih7PBOfZcaRTayOl1DCcpMVQRAMOfI52cP5n-jEgy1DoFifVyeekNNwdsKA5g8yKaZy080YuqGKQezDETuN_1mCNJcyllMFAmJtaLbATP5Jigfha7Jta4uaGXj98DQTrWbrGO-vfEVttqgpwtdbtmoxc-z3XbtlwfbXIx2M6a5058D7azNV_-AtiMeDjgUe3A5b3cgXoNe3MXni3YiSbuIihN1wnlvv5x1Zulek7GhOBga7NHuLYUigzzVxlXMD68PF94nhAVq2AWBPYBLiqcqzXJWrZeSfBZkAlPxWPkuBiPkQyL6CpidlcK9nPyC_A5GyaHXRecURlIgunAt2OLI_X-bJoe4XHjrWqXU5t0LO7aSBb3fQhQUNjty8lofe-AvxYZhDYyN80ojyF1B6OL3yuxqnVeuqQmCNeMO2wj0fER03LNp0lM3vMNGt_grC7ofU0HmtyQRzxOJ8Xvm7KkhFJYfvpDNXcTB8AxARXVXTfftGHDOjcJd389M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله تند خیابانی به فدراسیون: باید چه کار کرد که کادرفنی تغییر کند؟ نتیجه افتضاحی برابر ازبکستان بود. آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107197" target="_blank">📅 19:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzCz2FmpLnKObHifpa7ZDiNIk71oAq9NmBvCxhVyITbt3EgOa-D9vuhz-yTnMa8UFPz2Cho1nWmJu_AImhMPZvTGl7yhDqRRDGOMtzCoZkj6SXW48swehN_fjMs2bxjjJdjg5qvTcsOsG9A-BL0fWY-7lUlzL0nDd-b-9zDz-ZCByeOzfcLvRZDfvEWZyCgBPtZwk3nbK41JUE-eVRv4Q7qM7QrVwux-UzZV0RaMtvhA3hYBM7WL_KPK4_KyLZf8gZonse4GhXOGjdcwE1cKx9RMDvuvMUBaO-iIHlilu4cJ-BYZAhUzHVZcmnfhPfXT2ImtwRRwlE2zza4oQQiB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی دوستانه؛ به پیرمردها امیدی نداشته باشید؛ قلعه‌نویی با دستمزد ۱۵ میلیاردی پیش به سوی یک جام‌ملت‌های تاریخی می‌رود!
🇮🇷
ایران
1️⃣
-
3️⃣
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107196" target="_blank">📅 19:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd6jNQU74Y9xqi9tSXIL94jOBh2Jt8ptONR3GMM9PLI7sGIeW014W7N2BF3jNo_dDio6wBhyDkhFEgkZi3Y8gaQOpbXsTzijfsf3FgcKnnaIkEQm3egzyWLcbrOgDpLjSEKSorXyIqmMUIKOljv-vnX0iSUZ1SyrtvsNw0CaAg0Teg2-Qw_4eOYsb1wg0oLi3llQVlus9KdGFS1tQKfB8wrTynKn5-MfRbYPliEsdTwzFCXpfXnjNJD0IBhvsNWyogBMG3GgO7zD6giA9mNkpUnWucXMkuVhec5plS3YsfAVtydmRyZvaCbKQmsR3iN4sEb6IK-j_Ue4W7H7LY4HTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107195" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=pGzEZv0mftpDlqYF_JCGEcwxpLl8Sg_T2PCwIsq6rlUWhXCJLhLc0EaDtudnG9d_6PrRvxL2Oq8ZazLM3HqvGJewYUJNDd2pf_CYHJN8jN_QIq9mffnVft2VQlkDIxQhK7QQU_Gk5sAI3m7FouoG0ddcMi-ZFN8aRnh3tIzDA_B9S9FTIz22m78f8N50n-8rjYP-UfkbmXMZow_Vm7Yz-_UJ7thV5j2oaFcVxDHVTO14i93h3KXqj2GojDQwFZhPdJICad4hMSUa-Ga1Lfehz2eArFwD0gKBU3ZCCMV4xSPHlHpvlIIdGmTomiwnG4NAqQxHul2zJ6C_yc04ekp_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=pGzEZv0mftpDlqYF_JCGEcwxpLl8Sg_T2PCwIsq6rlUWhXCJLhLc0EaDtudnG9d_6PrRvxL2Oq8ZazLM3HqvGJewYUJNDd2pf_CYHJN8jN_QIq9mffnVft2VQlkDIxQhK7QQU_Gk5sAI3m7FouoG0ddcMi-ZFN8aRnh3tIzDA_B9S9FTIz22m78f8N50n-8rjYP-UfkbmXMZow_Vm7Yz-_UJ7thV5j2oaFcVxDHVTO14i93h3KXqj2GojDQwFZhPdJICad4hMSUa-Ga1Lfehz2eArFwD0gKBU3ZCCMV4xSPHlHpvlIIdGmTomiwnG4NAqQxHul2zJ6C_yc04ekp_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107194" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=Pa5nZ4DHqMGczlcz7jZvYkb6QlN-P849WZNcLjr8q6Ki2HUwWyHejNS29l7H7pCKxHXjTZco0e7EPKWW2oa4t2YThuFdMp6M7mBe1-lzrEC00HFIywpe4tePojVgTeX8KvAnSkVcvj9SfsBhjx40sjzcmiHYtwCTBkpvHh3a4ca-Ann_jDCa3oy_Fqeq-yF12mfSCeSH45fiymMNoCF3eMW5hUQbV2MBwUPW1VLZyTAn9Ycao_Y9LTiVRF-CkAJGqCtyq3j6iy3epguJwt9MEwAroYWMxMYMk3z2NPrk6rJX9A71vc4AL6XEefweIVXc71yWNMMjS43mW4Z0qV8MtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=Pa5nZ4DHqMGczlcz7jZvYkb6QlN-P849WZNcLjr8q6Ki2HUwWyHejNS29l7H7pCKxHXjTZco0e7EPKWW2oa4t2YThuFdMp6M7mBe1-lzrEC00HFIywpe4tePojVgTeX8KvAnSkVcvj9SfsBhjx40sjzcmiHYtwCTBkpvHh3a4ca-Ann_jDCa3oy_Fqeq-yF12mfSCeSH45fiymMNoCF3eMW5hUQbV2MBwUPW1VLZyTAn9Ycao_Y9LTiVRF-CkAJGqCtyq3j6iy3epguJwt9MEwAroYWMxMYMk3z2NPrk6rJX9A71vc4AL6XEefweIVXc71yWNMMjS43mW4Z0qV8MtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=QzzW5dplLNWFx3PZkOsj6CxTJfS9UXVR3w6FzfrH-CqIDQTBYBwIEa4TmnXJE-MZQXunwbfge3v7ionwEo6V20q6QrjQ_O0PbaIaiJootsnkTFF0otTqkc6eu7GsxpD-nq0RhJiZl4GKeT8VBYoAStz1hKj5InBaZ8xUvXxMj_fWRDoecWAXsuwxY9WctfblTzaFJmdLYs0JzJ3vA-_Bx-7_6iZk0nRp_RUxRguTZ-aq8dQ-ss1UCp1lbbzubdOPhpQmG5cSlV02TtKIoLI4NjSV6oXWnNq7UDFAnZ9y-1RosBwEe23dZIwWz100hMDRev2eUFQS33bhQlVFi2ct9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=QzzW5dplLNWFx3PZkOsj6CxTJfS9UXVR3w6FzfrH-CqIDQTBYBwIEa4TmnXJE-MZQXunwbfge3v7ionwEo6V20q6QrjQ_O0PbaIaiJootsnkTFF0otTqkc6eu7GsxpD-nq0RhJiZl4GKeT8VBYoAStz1hKj5InBaZ8xUvXxMj_fWRDoecWAXsuwxY9WctfblTzaFJmdLYs0JzJ3vA-_Bx-7_6iZk0nRp_RUxRguTZ-aq8dQ-ss1UCp1lbbzubdOPhpQmG5cSlV02TtKIoLI4NjSV6oXWnNq7UDFAnZ9y-1RosBwEe23dZIwWz100hMDRev2eUFQS33bhQlVFi2ct9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=T7W4yWnAHo_W8NJBNDQvQ-VJ4zqjlCfJDyyZv-wQ9LOMNi99ulEy4MJlBG8w-iW4vQ44nTfpRgPDCYPGhBM4OA7XMzQpk1FXFj_4GqCSIydQoagLgEIiA19TZGSbScc2556f-4a7ZGesw0vTIpMhsCWI6b2O78RXwtYu_xNpmzmddaZD58eInnrk1JApisKnGr6IDhvOrZJBuRdVmy3aCtTwv1_0nYDdDEYAIuOEzeMw97oosp06a-_m_g8yY5b4Oy-zQKfFj69oKBqFQFb73RRjV-4ywMP3DeZ7m9Q-hbO3YueGPrQOLaLeRFfuFAzpdeR36DXgGwtrUIKU5ajzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=T7W4yWnAHo_W8NJBNDQvQ-VJ4zqjlCfJDyyZv-wQ9LOMNi99ulEy4MJlBG8w-iW4vQ44nTfpRgPDCYPGhBM4OA7XMzQpk1FXFj_4GqCSIydQoagLgEIiA19TZGSbScc2556f-4a7ZGesw0vTIpMhsCWI6b2O78RXwtYu_xNpmzmddaZD58eInnrk1JApisKnGr6IDhvOrZJBuRdVmy3aCtTwv1_0nYDdDEYAIuOEzeMw97oosp06a-_m_g8yY5b4Oy-zQKfFj69oKBqFQFb73RRjV-4ywMP3DeZ7m9Q-hbO3YueGPrQOLaLeRFfuFAzpdeR36DXgGwtrUIKU5ajzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfKELXlkt4qvl1IB6uX2HOU3h4wI8uFf4KziW5ZlwGNt1nay221KkAZJPIdIu6Kms_VOJJWsNdaZRtFJjlGOiItxuhOy9G9SeXxyIJcq3CCgYqXA6zZa_PhY2A-Edfp_EIpGSqGjUOoEtkM4LsoOHT1o3N8WcTro-QqA9XMyZEoEYLInGU0EGfX1jy4Lq_vCYvemUewLJQIkBZHj9yn1LtHwVRMbNBLHLcLZnhGnYJEHxeQHpTu2TR4MEw-RjL1sshULcvctJ41xTpSUhvrZlGbri1S-RAAX1KGmTSDa9e6xwtGjfaoD3h3Fj9Dy6qa1M88K5q8zokWahm8bGYrHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPG5EzTa4Ri97oJor8iT6Ecx6FjQ6NnTzzdtivhJhWjorcO4riyuYUST0YJAS-F9ZU6aYy5XChm92Sxn-8bbPwmgjVefP53xz0RDp3UOmkCU2ILMj3KjubtWCaOKzoE7015uTkS0D5_fXQmqk5OFWH3GY0e3Z-3uU4L_sDtr9FxJa9K2Ny5QARLZBz8YZc49e0HSHckQdXnqHEx6HBaeJm7O1U5TS4DC2tsoBccq7EX8EzYptpn7n0gvMVUTWzLzefi0rvxuerpyhvDXfI4qBz5yf12L2hg3_-uWaMxBIraFKcJOfQCP7H0HcA39SAZ0-0BATTz_zZDJxK1C4zwiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj6XXLycr8LgIvexNRsHnsKVelk_a5CGXrLOOslOeA3n70SwOmeSPPz9dgsDAwIFCC7qIXZt0zsm3niO0bfNJ4_WCssbla43ezncFioAvCYZvp00VQKrPBSy1NGmTkq-jHuOk8H77HhKjIiLNHpnz7T_V1A4xxek7ZP25kNhtLAtEwuAaaOb8Y4P7_m9u2ImIX9VjDsbzQ14KjxDyHdcT48TnkGALMSXi932FJOxTd4CkZZIzbHxqwM2VTb4Tes-TPOHKCjY_861aow4RI8ozn86qlQzQUb0OAalCa0ztaCnMWvETcqhzgdyKfsJpkUH0VE0EXR_k0e9hwQhqxe7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RG7Bc06kxPKL0_PYuX5RMey2zSlnC6Q-xUY0pIkKPeDGr51JYpr1Zyhay4xrKzpqdOXydkodh6U2QSM0K9wrcjJBeu87LoYq2W_wfgYc6i0S2wq_PQjAgagpi-ua-IG9D63jC2Qq_Pz4zbOjXP-sshmn_XeurolRsdak_UWd7dOfqsxDo4aRg2IhkWztHp5veAwH_Wy1Yiflbr9ZRe1nnz3v6MT891Mt5B0abRsFKaLRCuMe5A0NLrCQBbsielnee1HxDKTjZ6u3GSvaqpsvdwJYNeKVRFh9schdKACOyatMpNVx2mO5f1qDP-nFSPfjLOvN4NwxnMOvCKFx9rcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDIqfvVbtyQM0VlVHyAXFMYBy32wDidCWYpTAXYiduZQFdN8fuQMZX23DLaDc0U-8KwrwBkaj3fsadp5ju2QyxpDTPsnMzzSLb3hx7nDPS23c3O0_FwE0rbC4JBTrs4EB_ni_1VdPxojyUKY30RofDg9Y4TPBVhFlnjxou8jekRCmGwGrmaKl6xH7jnSdUBgh-PSr8hiS9MBwFtgtXKUxX363ZIRS3oHAK-QtbjGQEElQyZgcwfyGr9mCNzzpVFfvsZLIHXhQvjXvId0B7SLoP2oo4Z6bp3o-_jN5D2SiXtu2yfILrtVqZCJDDLwCvIsvdA7NwkIIe6c_0mB2VU5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=ZTMvJdWufZBUOMLHNUORENZE6i0qe6oYBvCDGSACOPkhsELMal_5_YS2FTccLK2JoO9mAMYMGoYLF_svmUOASNdjozwMuPqI3Nl8cjiDI_9V70X1DrRM-05RzH_x0ouJ2DxLdHUrjf0BQnfEA56ecX4VCQbX4BQSGn3C3SaRtShkcuULe1ybYralXYdZkh9w5K_RrwUEMpiFPsxxB8d_Doc2Cvj7SaKBNrIQz4uucB5HxHd7ENc1PY0yCGp6OYyoxgbGdq_Sn-UUJJ-ChS0NvHX2RgjhAJdMyaHyUC3xzCgJLCQdlZGNOxNucFSxPBldz6gCkpg1KvIjJ0MZVjRsiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=ZTMvJdWufZBUOMLHNUORENZE6i0qe6oYBvCDGSACOPkhsELMal_5_YS2FTccLK2JoO9mAMYMGoYLF_svmUOASNdjozwMuPqI3Nl8cjiDI_9V70X1DrRM-05RzH_x0ouJ2DxLdHUrjf0BQnfEA56ecX4VCQbX4BQSGn3C3SaRtShkcuULe1ybYralXYdZkh9w5K_RrwUEMpiFPsxxB8d_Doc2Cvj7SaKBNrIQz4uucB5HxHd7ENc1PY0yCGp6OYyoxgbGdq_Sn-UUJJ-ChS0NvHX2RgjhAJdMyaHyUC3xzCgJLCQdlZGNOxNucFSxPBldz6gCkpg1KvIjJ0MZVjRsiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
