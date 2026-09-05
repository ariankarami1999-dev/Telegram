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
<img src="https://cdn4.telesco.pe/file/eII8z0bwA8bBVUD34swM21dNMax7ssuvKq5jcKkAROwb9A3JpiJMILiGSlOdQwlcFxdgVxN1ZgP6W9oDQrwA8oA1fHhtQtjgBphbCb6GR4KTfQCwxxC2ztOHf7FWshAE-V3yT_3huTSb3cHzSK-Jj9X6-6hJKRwlS2ktj4V_RpKLiwWRT4rPqhohbcVVdOxa9X9817-Ag5yVeAZSMxUZ2jg8oph7uiYa9jVWAqPbbbdTWSOv-_pa7aFFVcxvoiMli-x1FIK4X1a87PpcgzZ9W0bx01_c_aY22Xq9ZqSDdsLOD--oI6UDBJVPEzjhobjS3tLS4qIJ4Rl28a8mfxYIVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 00:05:49</div>
<hr>

<div class="tg-post" id="msg-460378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGbfkY5CafsbqwLsA3hw-EBb3tnKlT_kc7WwqmsswtyRbPgbs9m-8feead3toTsNkneM9ZEK9dzjjATgxHtE5BU0OSRHvO2PeJb65AljmGW3MUCuCBdD-5BQR_W6HgzZK0ULrLKdfsvCd0y5maxcuM2n1HzsT4-TXhMo0VviiTs761sHVdGDVZZFDpIPtdW8B0rjyUVy9DVI2vHp_LsYcDSfdXh5nB_9iILlTqjeHpQtb4IAD_cDhnYZrNzw5Mp_4zI7NVHQBuk6F_t2z1mMBVdBshCAUQCz9rRNmI0lWkh9FyQGrp3SlM-JqE_TQwomhszmjO36eMTthgn-oLbTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
🔹
طبق اطلاع خبرنگار فارس، تمامی افرادی که در این کلیپ حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/460378" target="_blank">📅 23:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f867ea1e.mp4?token=aAf0mlcW9Svjh7odjwznEoXNte6MhuulvU80SJyiiWy4KpPaCFnrV6Ncrg6pcDuBhL01WS0szAbxbStvLfDzV2QRU1l-EdlgnmlxPUMZeSthj6-FyKtzCwgMfxHNRqWql1iKr5kYjC7khLrnta5QxTYQ3Ygvq_NYM_VHzbgh72Xp4bjkHzljbn4UHS2LifSCGYjMzt4ERNXvgvUswqiK6GWdTxt3JR5lV5SRuB1G2x8dLpmTrlFhuQeHFHEGnpB8q3IfGV2dU8Z1KPGl62yqn86t_4jErwpFNtaLSzMhyAMSZtAPha42MGeY-JFaGCIFDaEIBx4l71sPJOebdS3yOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f867ea1e.mp4?token=aAf0mlcW9Svjh7odjwznEoXNte6MhuulvU80SJyiiWy4KpPaCFnrV6Ncrg6pcDuBhL01WS0szAbxbStvLfDzV2QRU1l-EdlgnmlxPUMZeSthj6-FyKtzCwgMfxHNRqWql1iKr5kYjC7khLrnta5QxTYQ3Ygvq_NYM_VHzbgh72Xp4bjkHzljbn4UHS2LifSCGYjMzt4ERNXvgvUswqiK6GWdTxt3JR5lV5SRuB1G2x8dLpmTrlFhuQeHFHEGnpB8q3IfGV2dU8Z1KPGl62yqn86t_4jErwpFNtaLSzMhyAMSZtAPha42MGeY-JFaGCIFDaEIBx4l71sPJOebdS3yOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌ جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد
🔹
رئیس پلیس راهور خراسان‌رضوی: این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/460377" target="_blank">📅 23:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a5fdd274.mp4?token=XkGrS7TGQHTOSb7LrGM-ZtTJid3fQIDeIps8Sq7-82q-ERay-ZKUiRefewysty_1NUz8vSvMzF6m1V5WDEmpiOjmkXJBRICFja8HgFSvfq6WmPuDKijD1c96CfvgtvMkcvTi9tgE6J-HZIxCwwtHVXa4il7zHT52D2rtYBc5JaYpGReoyYPm_kVb9mwbDPL-ZVLCitl9aAqaMOOCJBjl-ocoVixm9KBGrgeiwBRu4ORHZXdHGlcWMvMf1V53e5mgRX69665yiKYeVGZ034SFa2aDK362xLHvbggVx8gkx5b73ZCo1b1qyA7LyWv4saJPCSNbwE6vYAeFjH0uitCPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a5fdd274.mp4?token=XkGrS7TGQHTOSb7LrGM-ZtTJid3fQIDeIps8Sq7-82q-ERay-ZKUiRefewysty_1NUz8vSvMzF6m1V5WDEmpiOjmkXJBRICFja8HgFSvfq6WmPuDKijD1c96CfvgtvMkcvTi9tgE6J-HZIxCwwtHVXa4il7zHT52D2rtYBc5JaYpGReoyYPm_kVb9mwbDPL-ZVLCitl9aAqaMOOCJBjl-ocoVixm9KBGrgeiwBRu4ORHZXdHGlcWMvMf1V53e5mgRX69665yiKYeVGZ034SFa2aDK362xLHvbggVx8gkx5b73ZCo1b1qyA7LyWv4saJPCSNbwE6vYAeFjH0uitCPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پزشکیان آسانسور را ممنوع کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/460376" target="_blank">📅 23:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52e71799c1.mp4?token=HPZDeoL0aahsFzrTfmXacbhWbbGBQ0N_AoN_9-40-MqwWA55stnEvyGCWPiszLwKsPnAdiXz-GVuf4pUfv3LbuHeG10srCf0qFjw3RP_7MOxPbz_WDxNbRtN9iWPVPe-xb8Hj4Gmmesd5kXwIPOZ21sBpT-kdoROWDNKOHsGnd4xyZQzSaqmCDWO0dP4ZBUSf1u-GxPZfRJShcPTtii1zOkLsgr0dTXdAB2zq8SDcTpaZtKEmx62cWtsIwN7gSfnT1CD2LAVaDNsmNYz_w5xXzFcBMQysyCYgY79GgbiwCZ_64ip2bJQzK63teDUBm0FsR-ws-Lu3RBMaTQsNCqFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52e71799c1.mp4?token=HPZDeoL0aahsFzrTfmXacbhWbbGBQ0N_AoN_9-40-MqwWA55stnEvyGCWPiszLwKsPnAdiXz-GVuf4pUfv3LbuHeG10srCf0qFjw3RP_7MOxPbz_WDxNbRtN9iWPVPe-xb8Hj4Gmmesd5kXwIPOZ21sBpT-kdoROWDNKOHsGnd4xyZQzSaqmCDWO0dP4ZBUSf1u-GxPZfRJShcPTtii1zOkLsgr0dTXdAB2zq8SDcTpaZtKEmx62cWtsIwN7gSfnT1CD2LAVaDNsmNYz_w5xXzFcBMQysyCYgY79GgbiwCZ_64ip2bJQzK63teDUBm0FsR-ws-Lu3RBMaTQsNCqFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پای کاربودن کاشمری‌ها در ۱۸۹ شب ایستادگی
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/460375" target="_blank">📅 23:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108f6a8d6e.mp4?token=ajtx3K1Jd_jg29thMbcRsKilkPzfX8CxAeoBm662nfxMl704fMOJnAKKhRWbnhKY5yxzCbXu3v_CK13eZ1w9EDcbnbTkx7FDqNiul9wcAz0Pht5JSzq79LOksigsi19U6Q2jWQBnJQY5-YKsgPfmx-aSNUiqgky0CzWgQBLPdB7Bg00JKZC7SQ3hgfY4DDrbCdpCJYIbySDk2lKFWrx3Xw3ukxWAb5xAu5WAXNOfo7zy6MRoHbDp7FLQ5yfFXVfMksrBUMiSdulUF6OTSEG21AZZSSbQHyzpwqBZ7RMSFGAc4Dn3N3GO-VRl1gVQgK3PnV_1zpDYFqlbg6GTUfG-jWyjOnpTt9dTrsV1Dle2ki9wjCzbh9O-1_KUI3vO92zFSt9o50_bLCbbqzeLaErm8t64EWffGp86SoMit6Q_-2CLX7BzEMOBCezYwmNvkPfQ5IV3HzXqHJJtqkU2C0oJMm8smxUWmukB4AWTYBw944DHOrY37gKx9fKYX_Ed41_p1cC26aONONul97wgtJUVsSVcg_g8hxNcNZb0VX4SnE-gdWjDEZd06r90yuaNx44CX7zxtoW4OcAkI-EKVOyi862UCsq27gmQyMRaXRUxhfMHotqqFk6DodoDTM_pEiIljnQihOPeLGOClx6yvjFkR_Qm6dwtdvQr7S96k5H8l6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108f6a8d6e.mp4?token=ajtx3K1Jd_jg29thMbcRsKilkPzfX8CxAeoBm662nfxMl704fMOJnAKKhRWbnhKY5yxzCbXu3v_CK13eZ1w9EDcbnbTkx7FDqNiul9wcAz0Pht5JSzq79LOksigsi19U6Q2jWQBnJQY5-YKsgPfmx-aSNUiqgky0CzWgQBLPdB7Bg00JKZC7SQ3hgfY4DDrbCdpCJYIbySDk2lKFWrx3Xw3ukxWAb5xAu5WAXNOfo7zy6MRoHbDp7FLQ5yfFXVfMksrBUMiSdulUF6OTSEG21AZZSSbQHyzpwqBZ7RMSFGAc4Dn3N3GO-VRl1gVQgK3PnV_1zpDYFqlbg6GTUfG-jWyjOnpTt9dTrsV1Dle2ki9wjCzbh9O-1_KUI3vO92zFSt9o50_bLCbbqzeLaErm8t64EWffGp86SoMit6Q_-2CLX7BzEMOBCezYwmNvkPfQ5IV3HzXqHJJtqkU2C0oJMm8smxUWmukB4AWTYBw944DHOrY37gKx9fKYX_Ed41_p1cC26aONONul97wgtJUVsSVcg_g8hxNcNZb0VX4SnE-gdWjDEZd06r90yuaNx44CX7zxtoW4OcAkI-EKVOyi862UCsq27gmQyMRaXRUxhfMHotqqFk6DodoDTM_pEiIljnQihOPeLGOClx6yvjFkR_Qm6dwtdvQr7S96k5H8l6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان خاموش‌نشدنی شاهرود در شب ۱۸۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/460374" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vACTbnZrrI14_EHN-o1_cloOign2zJwjcWhdsP8BqUQGJCReO_-AHJeAZPAISktvAH-Tgz_QDqD8Bra9XWgHJLNmBJMb8xlLuc7ngSigGO76XabhBN_taTfQO3_1UDspVwv7wFyHSZPL9BGkjUlke3Xc32u8RwzlGKO_Ln77UNZW7bjLDEsOcTgTkvrkLH--0F_aYFvgiOhi6RfP8m9QOkvFoYu4ynMUJeniNCSWsedTNnvVwcIIHU1pv-0arVFStDTHCgo4rqtnr2qJeVN376TIR4g6l5TabkVqHBhbauhjBtFQBlM2_IIrpZNVm20tP0j2wyhBX12lWa9q891MkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
🔹
علی محمدی: در ۱۰ روز منتهی به ۸ شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.
🔹
حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل ارادۀ نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/460373" target="_blank">📅 23:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc4c5204a.mp4?token=K7udbajEcq5v-PDC7IG-ld0cStkYhFsCiZ57-SQBZvsmTsJuuYCrXrQ5WziqMRrDf_vW8_vyjS3WomWqcqby73vMUCvGMQQL5ZYAGJy73He8MEdL1N2D0DE34JIFWZZZAXMaDdB7h48GNMzVyl44OC_C7fdKurPhqvuXEspXs40kLhgyzee3gRa_Lx7ePb8OEYRFLIMEZ1HPxZf_O7sINTV5Oz0yrV4aoEdcU-zZBAUGpLQK-qNJuM82y1xcgu7Pwl0RladoKpuoGSf-TAOfvXARtIxVMrnJRIFbhgLqW6dr8q6zNlhkCgu-q4P3gZNY1gvo3QAsP4qe7tzNwHFaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc4c5204a.mp4?token=K7udbajEcq5v-PDC7IG-ld0cStkYhFsCiZ57-SQBZvsmTsJuuYCrXrQ5WziqMRrDf_vW8_vyjS3WomWqcqby73vMUCvGMQQL5ZYAGJy73He8MEdL1N2D0DE34JIFWZZZAXMaDdB7h48GNMzVyl44OC_C7fdKurPhqvuXEspXs40kLhgyzee3gRa_Lx7ePb8OEYRFLIMEZ1HPxZf_O7sINTV5Oz0yrV4aoEdcU-zZBAUGpLQK-qNJuM82y1xcgu7Pwl0RladoKpuoGSf-TAOfvXARtIxVMrnJRIFbhgLqW6dr8q6zNlhkCgu-q4P3gZNY1gvo3QAsP4qe7tzNwHFaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌پناه: ماهانه ۵ تا ۶ میلیون تومان از حقوق رئیس‌جمهور صرف مدرسه‌سازی می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/460372" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646bd8b55d.mp4?token=uSpcauPgG3xMEm601Hfulj83wJvjkZtReipPU8EyoqniG6fjHrC3EqpZFTne3AGzqeR11HAxkkoIDOwCTYnCNgj6cGtZkBqi4F6_Azy3Q25VTCv-H4c7rTRQBjrzbqr1vtQ_jlPq6ClOROkCnOy5ER3Ycgn3HzeIxoGNJV9eDuuDAmXVZRjkuFMoPE8_z9MQds0Xzm3cYPZXYsR2Q_wSr1AdS2mMG08Ubcr3AA9UCCB-TF1T_m8oITH0jwIzjmw6cefmhPeSoaIr9JoLmirgaWH_D6POTIr1hSZOTjUaFEt0vmEeNdBkViDHVegPndmQP8gwdpk7DQw1YIny-hwSjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646bd8b55d.mp4?token=uSpcauPgG3xMEm601Hfulj83wJvjkZtReipPU8EyoqniG6fjHrC3EqpZFTne3AGzqeR11HAxkkoIDOwCTYnCNgj6cGtZkBqi4F6_Azy3Q25VTCv-H4c7rTRQBjrzbqr1vtQ_jlPq6ClOROkCnOy5ER3Ycgn3HzeIxoGNJV9eDuuDAmXVZRjkuFMoPE8_z9MQds0Xzm3cYPZXYsR2Q_wSr1AdS2mMG08Ubcr3AA9UCCB-TF1T_m8oITH0jwIzjmw6cefmhPeSoaIr9JoLmirgaWH_D6POTIr1hSZOTjUaFEt0vmEeNdBkViDHVegPndmQP8gwdpk7DQw1YIny-hwSjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه قضائیه: مدیرانی که نسبت به اهداف جدی نباشند از دستگاه عدلیه برکنار خواهند شد
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/460371" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FV29y4Dy2q7_sn6jhi_0t--DFravQ9t6dC5yXgmS3SFYeSl7tISh0f8fqC4BARN7HwfSc8APG5TlFoeL9hgbTucRxHSoWJqnR6R9p4Qy-vrvUz5RwIJgrpQ6Zk-YNREFI69drZFknUiVfPWJpYQSZuHuVFDfGZ_cW8Lv7v28lkWpo3EZYbGfBodoJG-srtkB0Q9oQGu0kCEt24g5QHyvZo1S-_ngZiYD9rXEJB7cVksbvnvyxdYaP81ZHOga-TDrmT-QtCgNb2pz8yweuw8gI4-l2_ZhtyI3ChTHRvFY3Ae6wdXyUR65ZXYC5mo7iuXgIu3pFRYovhk8IsfJAkgi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnmMuXd6PpJUHByAWWZ37-p3UnE91DRCfWwTBb3f4FyCBjEzV27A9Knsj2ErorgasmkfX8sjrR9r8IJ5LzqQNCCJ1i8BESrQEQ1y0MdxdXtUnZRWhMTEI9st7eKMWhT2pa5R1LJq4Nd3FesFWUJ_jEzs8sS5MLE5_dZWjTAeiyDcuplXJEZZan5EttXhinaZo-Kul7d0PUUGhrLRwRa7u0W3omEXcbuF4bxdWdhl0V6Ep_mkal809yDfI8CE2SMqidFOwsJn5KkTdpacCsbOqW-x70qZinb00ejCGPIdbkIbixj-QcqYssSTglFbDWpG_bvGkhxlZ7F41g1fhG_hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOP3CdkR8iYV2zGQwF-MYJGBvYUvcx1G6zPonzlMgmirwYlvApU3jHfpWCmHBh35_yCGDOKlOfmhXcLz2yYR61FWkkpCEUrhgcgeUJpIE9rwbW7O5wm4K2vsW8fxSNd-lY3c6_w6RGgPF8sCa5oEEIdBIPxahw55G8tr8Q1jJx39Uadm75qQQWVP2caNaxBupyDB7xIZMkLTN0FS8EAOpThV2J6LwGsQ278EYhxUTUbGW1uEd-lE4ohZ7i9p68PK4b772lq6UYuPEkW0TqMwOwohTgTuVb1JbrkJzshrI4qn0nERtsborVn51Vgcit80aGd2QFHeAE1IhJ7yrwum6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی‌شده نداریم
🔸
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند. @Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460368" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2L_z2u7VBAp922DpOFIx2DAjVXP5TsRotZu2ShKngnDA0KvH5LE7dj2XmrB0aopslETsOA8x6Sy6DEoHV-Ee44zRi-eeqpa-ZA5gHBmLLpXeS-4YFsK13QWNeSKuhnqLRRw2YxaJbjTZDs8gCKZ3IZu2JbQNeWeE9tOSAWfFgXBPvetwjKDRVIftagMCGP5TXpVvnf04BgwrXVwBomjaE_5WgfLYNxHnDg-fhoMEAb3zp9rQg6W4GSyajkxNhmvFou9BCMhe97lXaQaWxSAO1OkGM9nDXfA8pJWuCwGBuJJtXUDDG6P2J2AZu45kVLEimndwVLWpElBWibWC96WtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcf35c0a4.mp4?token=NFrF3nelmy9tOwb3NA71zSiZ8dMbrmTEu8PrlTL1oxEuCzwzMCk7PY7K1DSZaZ5lYREVFv0QwtGLcOtxT_GQiy_roWjiq0gUjfcyjK-8i7LuiSBbscHUxbqi2h27wPfYZSYpy0IMqG_kxtuk4zxmpyv7812NfGw9nIXgzpwdjJKAr31vdeqhoweSzlwqdPz47ifGoP5iB7kTEyGiT5VI7vg-dUgMvPJFlA6OFgtrnWQS4ekmZLc4Em5VBFCerOwbaSw3W_NxZMw5SQ4lEaP1KRy8yCvqv4FGm4lYGT1jkkSA-rqo5R5rOR4D0V0jO3OXEy1cVLyRMVzNHhX5XU_ikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcf35c0a4.mp4?token=NFrF3nelmy9tOwb3NA71zSiZ8dMbrmTEu8PrlTL1oxEuCzwzMCk7PY7K1DSZaZ5lYREVFv0QwtGLcOtxT_GQiy_roWjiq0gUjfcyjK-8i7LuiSBbscHUxbqi2h27wPfYZSYpy0IMqG_kxtuk4zxmpyv7812NfGw9nIXgzpwdjJKAr31vdeqhoweSzlwqdPz47ifGoP5iB7kTEyGiT5VI7vg-dUgMvPJFlA6OFgtrnWQS4ekmZLc4Em5VBFCerOwbaSw3W_NxZMw5SQ4lEaP1KRy8yCvqv4FGm4lYGT1jkkSA-rqo5R5rOR4D0V0jO3OXEy1cVLyRMVzNHhX5XU_ikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد
🔹
صبح امروز ارتش تروریست و متجاوز امریکایی در یک اقدام وحشیانه و از سر استیصال در بسته‌بودن تنگه هرمز به ۳ فروند نفتکش ایرانی حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/460366" target="_blank">📅 23:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZMGlIJ2XsspU4Ol887K2rOQr5RXEDEbGpzxy3devN_1_zQT21PaS45VRSDMdf6kUy76YBXsB32XWOvfenzpP9eJ1eNgLoigo6PF1RIuGIia6FPhJD69xF1VqD15aLsQZFnVc2kFHkQsSK7nWrfWvQMlTWUE84i12GUFMtAWzF8pWLNzwUINATEtUdZraKUiSsiV3HgdVI5NlH7CFXTk_8wPYkAFWlD1qM_CjsgTw4EzZae2UFvkjymjEPcsDH-JCYKJ66YcCLNEIwg2VZ8Wq5OrmDxpN_2ImxgmgWaqPfDPuOjuY-TvER7CmNozcQAeW9UV7drnLh28CUnFpGzCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد
🔹
صبح امروز ارتش تروریست و متجاوز امریکایی در یک اقدام وحشیانه و از سر استیصال در بسته‌بودن تنگه هرمز به ۳ فروند نفتکش ایرانی حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی دریایی سپاه در پاسخ ۳ فروند نفتکش در مسیر غیرمجاز تنگه هرمز و ۳ فروند شناور وابسته به امریکای کودک‌کش را در مناطق دیگر مورد هدف قرار دادند.
🔹
نیروی دریایی سپاه درپی این اقدام به تمامی شناورهای حاضر در خلیج فارس و نزدیک تنگه هرمز اعلام می‌کند:
🔹
فریب ارتش تروریست آمریکا را نخورده و از هرگونه تحرک مشکوک به منظور عبور از آبراه های غیر مجاز اجتناب نمایید؛ در غیر این صورت مورد هدف قرار خواهید گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/460364" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1986a916fd.mp4?token=Y1DEX9XM4CSmpuaFw0P0E3uOthx1Uz0uR-dpgyh89XHxaW-hi3uuy6wUSmTvmt9f0hTSKWbigo8Wu4RRVjKd2NFdKm-tOew8SRkl05NAIKnKVjVDSJs91_6nW4_5OFsbozZWlaMtFTryC3rQxGj0KE09oOX-ZfxTTSo4lUq_YD0gJ3TPMokA4EXiHdHh55_IsqP09jwZEfWrmOQMSnuNdSWMyA1Yb4rvIdvfUExF-Q5oqpW7Sm6pgPYv_UK8ZkWH_DUTrZHzV92CpBZt60jUcFaerHHrBbBofvtVqMZ3NNpYu8ekN1O6dx7djLUIfNdXawUeot3BBTzj9uqW9xvo9xSqN7zMcYhEIO9ej1VFuV7viI67bF259sTsjyhSLCNKCcv9drC5CVbdtOvCMsyq40HChDz3EsnMDkL1AqOYreP3lyKsyNUW54dKlm8frN_3plQoWH8gpJR146u2pY4OUO1-tHVxrHz3wT6RiTTntQdjU6qXOIIICW6SgnjHAF4Kts1-ieEpMRqGOd40RrOAW1syGDLRiugPtx2mpnJo-3qC1e87axejjDL2oVo51Rs4X5mwC7_3T3FEN_UwkArQIdZWFBI0fIdX_QnI_ah2XYSTCoUtyUxkl1w9gltU2HmuKcvvA-doWhDeZen1Tq_2km7Om6GLgpR3E-kVBpRz4tE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1986a916fd.mp4?token=Y1DEX9XM4CSmpuaFw0P0E3uOthx1Uz0uR-dpgyh89XHxaW-hi3uuy6wUSmTvmt9f0hTSKWbigo8Wu4RRVjKd2NFdKm-tOew8SRkl05NAIKnKVjVDSJs91_6nW4_5OFsbozZWlaMtFTryC3rQxGj0KE09oOX-ZfxTTSo4lUq_YD0gJ3TPMokA4EXiHdHh55_IsqP09jwZEfWrmOQMSnuNdSWMyA1Yb4rvIdvfUExF-Q5oqpW7Sm6pgPYv_UK8ZkWH_DUTrZHzV92CpBZt60jUcFaerHHrBbBofvtVqMZ3NNpYu8ekN1O6dx7djLUIfNdXawUeot3BBTzj9uqW9xvo9xSqN7zMcYhEIO9ej1VFuV7viI67bF259sTsjyhSLCNKCcv9drC5CVbdtOvCMsyq40HChDz3EsnMDkL1AqOYreP3lyKsyNUW54dKlm8frN_3plQoWH8gpJR146u2pY4OUO1-tHVxrHz3wT6RiTTntQdjU6qXOIIICW6SgnjHAF4Kts1-ieEpMRqGOd40RrOAW1syGDLRiugPtx2mpnJo-3qC1e87axejjDL2oVo51Rs4X5mwC7_3T3FEN_UwkArQIdZWFBI0fIdX_QnI_ah2XYSTCoUtyUxkl1w9gltU2HmuKcvvA-doWhDeZen1Tq_2km7Om6GLgpR3E-kVBpRz4tE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست‌ها چه نقشه‌ای برای رسیدن به مرکز ایران داشتند؟
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/460363" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJLmti2CjHBYviSdDL6CHBTb346gTK74k-T4o-4iUqjzwBYywKfA9o00cdqC29yiF6v9XrJANV5DJHMw3k1WA9PkSWtvMPltvGMunokE7BvH6IvUqaHTyJEOdEqmHGFcFsByJdKLVI151RpoGZBeFfNxdRs89_YAyEp_zLOBzy5wf9haBuGzp1B3HZyTDptXa8z90m_HqpvetJLO7UC2k3N9nXCwSF2ejNAqQph5P2hl43fOQAcUcDhyQeoaGoRQrqYBPtVrFF-xPqEVPJFUJd44LtZCKl27DWeAUsKP2QMBiQ9RXW-iychgjlf_Vx09tLkhKR-l1vzqJmlq6gW-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحشت نهادهای امنیتی آمریکا از گسترش جنگ با ایران
🔹
شبکه ۱۴ اسرائیل شامگاه امروز اذعان کرد نهادهای امنیتی آمریکا، به شدت نگران گسترش جنگ با ایران هستند.
🔹
این نهادهای امنیتی ابراز نگرانی کردند که احتمال دارد نیروهای مسلح ایران تصمیم به تشدید و گسترش حملات خود بگینگرند.
🔹
یک مسئول آگاه اسرائیلی که در جریان گزارش‌های مراکز امنیتی آمریکا قرار دارد گفت که «این ارزیابی، مبتنی بر واقعیت است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/460362" target="_blank">📅 22:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9oAU93J9AopzGjY7rBFMbKInjkFIBykZUWqWBCmEmj3TQLerX8cStgcYWp71vLYYqXRJnF7LH4FVAWiamxVW6TvvO0HrshNoTlCSztF-kYnhaYNed0YqR3RzCzuW8JEMImTDqaOsmorwnrJJJqxrqeE6hunVmAHdV8suqiMBiRBJLexvDqM-Yl16L3hJt4yyXLn9DA3tPrrRfYjnH-ADngoCshMa37aMDAD4ytLkt_DK192wPbX_PamoGTVFK191xW4JS0oM9nvbNoKNsSlFW8Wre1y8wPI8kb29gQvSgWHhjPoYJSGfBNu8KQm8uNhvFY1Nzg-TLA8owigGGfegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌  ۱۰ شهریور؛ روزی که خبرهای خوب از راه‌های مختلف رسیدند
🔹
«بسته خبری امید امروز» روایتی است از اتفاق‌هایی که شاید هرکدام به‌تنهایی یک خبر باشند، اما کنار هم تصویری بزرگ‌تر از حرکت، ساختن و ادامه‌دادن را نشان می‌دهند.  پروازهای عبوری دوباره به آسمان ایران…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/460361" target="_blank">📅 22:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1931c9227a.mp4?token=U41nFbLZkeaGtHvasw2w--SEA-weS5terArXYEWQ6hOSoOMTY-Y6OV6jfp5ggNlTZo-G8nPIwEcOYcym68lPcCFqS4Wjat6iA8aMjIEk3-5VI2mMd54bX0C6cZ8qS-JaNk47_IK2oeIlgjBzGYChl7mbjKnpovnX31S6pLj3QYmWvPynp48T4-fCf7zdEFXScZGfKhZG7CPRz9-aG0am1Ayd8QYQ02F5De28xyGfJKL79nPSWIduYSonHYSw-39PoyUlVdl80u2P9rX-u6SIEWxQJnZdNLchJqgJJausMmJEJwBlgtZ-BzcVh7gMogdpJ15j80wZU1VLuW2Zvr9WilhPqLXWPFs-gdlfyXhXXko8lqaE9GkxGv5w7ej0ZI03i5AYuoO4TSHC24UM0YSV50mjG4IPvi-cvOZy624BhAg2464R5ixQ-2U9Dt8Y68iixhzfTd4q4hMqr1rxpQODL4SJhUuMnGHaAFtdCkkg9Q7X_yCKzcoraMphgRHHbE_hnRIoSKZGRpQgXXG83Fks76PyVh1DSODUUNFNA8sHyvK_B9ao2AsJazy0C5a10LbH8grk3W4WbfeOoTxxd5FpyxehJMZdaO-5UIFoB7dWR34MDgpfF9qI6SXS4Vl_oqvyZ5Dd7uSR_A7V3zCEO5JpefFbeoENjn4bXdkyrtP5Dag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1931c9227a.mp4?token=U41nFbLZkeaGtHvasw2w--SEA-weS5terArXYEWQ6hOSoOMTY-Y6OV6jfp5ggNlTZo-G8nPIwEcOYcym68lPcCFqS4Wjat6iA8aMjIEk3-5VI2mMd54bX0C6cZ8qS-JaNk47_IK2oeIlgjBzGYChl7mbjKnpovnX31S6pLj3QYmWvPynp48T4-fCf7zdEFXScZGfKhZG7CPRz9-aG0am1Ayd8QYQ02F5De28xyGfJKL79nPSWIduYSonHYSw-39PoyUlVdl80u2P9rX-u6SIEWxQJnZdNLchJqgJJausMmJEJwBlgtZ-BzcVh7gMogdpJ15j80wZU1VLuW2Zvr9WilhPqLXWPFs-gdlfyXhXXko8lqaE9GkxGv5w7ej0ZI03i5AYuoO4TSHC24UM0YSV50mjG4IPvi-cvOZy624BhAg2464R5ixQ-2U9Dt8Y68iixhzfTd4q4hMqr1rxpQODL4SJhUuMnGHaAFtdCkkg9Q7X_yCKzcoraMphgRHHbE_hnRIoSKZGRpQgXXG83Fks76PyVh1DSODUUNFNA8sHyvK_B9ao2AsJazy0C5a10LbH8grk3W4WbfeOoTxxd5FpyxehJMZdaO-5UIFoB7dWR34MDgpfF9qI6SXS4Vl_oqvyZ5Dd7uSR_A7V3zCEO5JpefFbeoENjn4bXdkyrtP5Dag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم وداع با خلبان شهید حسین مهدویان در قزوین
🔹
شهید «حسین مهدویان» در حملهٔ اخیر دشمن آمریکایی به خوزستان به شهادت رسیده بود.
🔸
مراسم تشییع و تدفین پیکر این شهید فردا ساعت ۱۰ صبح از امامزاده اسماعیل(ع) قزوین به سمت گلزار شهدای این شهر برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/460360" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-doFwmyVM4ibopr65Vj78jZDF_MQyc7n25KbYfG0cQaHMaKaudIdir4DUBonvBS8YKt9Fkr_Xs3rkTXGjCI94djz1Mao97yCfPLMWFmwLOd7u2Tf6QQmfPRHUQgmNInkZXqJ0uFmzdxUi3rb6u7PeHdXhLCySOfU2QoWRNIC6aLJZq21ax7HRKGhAxu-_D5gSN-9yE0J7gd2R8jAnHe5tpIU2qx9z_BptsJpwQw4wucrNASRi24t7ae0lZR8oD17ELCz5igBnLVOPcYlZJeOepVXyMCLmP4KTEHQ1F1vBvvl2HJJrMYjnwhzJVYRM7RY4Imfpm6u-xy5LrzfKg4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند خرید و فروش سلاح جنگی در دورود
ِ
لرستان
🔹
فرماندهٔ انتظامی لرستان: مأموران یک باند ۳‌نفرهٔ خرید و فروش سلاح و مهمات غیرمجاز را در یکی از روستاهای اطراف شهرستان دورود شناسایی و اعضای آن را دستگیر کردند.
🔹
در این عملیات، ۷ قبضه سلاح جنگی (کلت کمری)، ۲ قبضه سلاح شکاری و ۵۵ فشنگ کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/460359" target="_blank">📅 22:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460358">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPjA5OsN2YjuzDnC_SiLn8ls5VJ0QYin6JvgHm69GYnJpicXlQDLzTmctwMOArOnjmA0MZInhgd_2HG-akbuQvH1EygBsxTGD47QVlJOWwDeIflCwUGiFDxjmAq_5wfL56ydNe8TMsUGvt5RqK3hihgTKnAGWQW1PSc09mz7zGeJDUBKeekvgyFxcOUvoreenu69kCcwdEmq0ex4pAs_CviSrpQUpwokMLjxoVoIV5BfWKcm-8GykOLysNh9z5iDxbVD8zANKOcjZ10m-01qDpux3G4SpyEyRol1F7WjuOP3oN-JqUum0KkWGXKtHnfn1FIoaW7Q-trwD7n-kiLuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پوتین با نمایندگان ترامپ و کورسوی امید برای صلح
🔹
نمایندگان آمریکا امروز به‌منظور حل‌و‌فصل جنگ اوکراین به دیدار رئیس‌جمهور روسیه رفتند، در حالی که پوتین در این دیدار مسیرِ صلح را «راهی دشوار» خطاب کرد.
🔹
به گزارش خبرگزاری تاس، این دیدار هشتمین ملاقات رودرروی پوتین با ویتکاف و سومین مذاکراتِ داماد ترامپ با رئیس‌جمهور روسیه درباره مناقشه اوکراین به شمار می‌رود.
🔸
ترامپ در کارزار انتخاباتی‌اش مدعی بود که یک روزه به جنگ روسیه و اوکراین پایان می‌دهد، اما اکنون بیش از یک سال و نیم از دور دومِ ریاست‌جمهوری او می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/460358" target="_blank">📅 22:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460357">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmKhbDUJTa5PTKmOsti3TL15L42Umv6UO8FtS_L3fQM-N0JTUOTGEok3P7K-rxtsvVzZd9wDoBjEBYYJoipgRqMn1fJyI8B_L510Ha8Rg23uMwVjwbZ5bQ58_yEaQSJ05exy3QqDVsyYkgc_yfMZ9svssrqmUf0HVoBeoVXenhf5S36fBUAxkmPSA1c0xRwdQdj9lZklr3T5jTAfwF0MEwyGXnGEypHm40uGujIiG9ehIJ3Am6frVopvrf7bxPOU8vH8ZGu0yFdApuNPa-VqHRkdUXqs5tLB52PdHnWjxC9-ViKL92NEf-_7MviHMJTTBTh8u9JMYqmO09fpb6TebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تصمیم غلط دربارهٔ بنزین، تورم تازه‌ای به راه می‌اندازد
🔹
صبوری، اقتصاددان: مسئله بنزین تقریباً در تمام کشورهای دنیا موضوعی حساس است و افزایش قیمت آن معمولاً با واکنش‌های اجتماعی همراه می‌شود.
🔹
همین حالا نیز در برخی کشورها، پس از افزایش قیمت بنزین و انرژی در نتیجه شرایط جنگی، شاهد اعتراضاتی بوده‌ایم. بنابراین حساسیت نسبت به قیمت بنزین مختص ایران نیست.
🔹
حتی اگر دولت سیاست‌های حمایتی برای جبران آثار افزایش قیمت در نظر بگیرد، افزایش قیمت بنزین در نهایت باعث کاهش رفاه اجتماعی می‌شود.
🔹
زیرا در سبد مصرفی خانوارها خود را نشان می‌دهد و هزینهٔ حمل‌ونقل و در ادامهٔ هزینهٔ سایر کالاها و خدمات را افزایش می‌دهد.
🔹
به محض این‌که تغییری در قیمت بنزین اتفاق می‌افتد، بخشی از مردم و فعالان اقتصادی انتظار دارند قیمت سایر کالاها و خدمات نیز افزایش پیدا کند. این همان انتظارات تورمی است که در اقتصاد ایران بسیار قدرتمند شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/460357" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460356">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d3efdffc.mp4?token=vbnisEOzmrAoxQ31VBsfcA1Icqx9gHy7jDlF-GJKOaBATPufmpBJ_es3ZD6RNn7niq6WUpOXY7ZWcxEDgNWD6u5Lq6nUwXcrDJAuYNLyYAKBP2eWindRTjXDVXDAuziUXQN8THuF2iaMMPdOXoCsEkAMNOSpiT02KMvXO_YqrrLd8XngXpyDjZ3atH3yRU7s692SikMftyphM1lzfaZJKqx9aQ2cB8xtJyKuPwkLA_0iKm_nXNaiTCGOaONDnI8lHbh6jS_O5OOjBKXiku6kIfaflFJRALsjItCjhwoQqcl9w67oiQxbqVdmli3KdiNRMhK9HAcWTPsetDuY4jAooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d3efdffc.mp4?token=vbnisEOzmrAoxQ31VBsfcA1Icqx9gHy7jDlF-GJKOaBATPufmpBJ_es3ZD6RNn7niq6WUpOXY7ZWcxEDgNWD6u5Lq6nUwXcrDJAuYNLyYAKBP2eWindRTjXDVXDAuziUXQN8THuF2iaMMPdOXoCsEkAMNOSpiT02KMvXO_YqrrLd8XngXpyDjZ3atH3yRU7s692SikMftyphM1lzfaZJKqx9aQ2cB8xtJyKuPwkLA_0iKm_nXNaiTCGOaONDnI8lHbh6jS_O5OOjBKXiku6kIfaflFJRALsjItCjhwoQqcl9w67oiQxbqVdmli3KdiNRMhK9HAcWTPsetDuY4jAooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی بروجردی‌ها در خیابان به ۱۸۹ شب رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/460356" target="_blank">📅 22:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من سال گذشته پیاز کاشتم و کیلویی ۳ هزار تومان فروختم. با این همه هزینه و مشکلات، حتی کود شیمیایی هم به‌سختی پیدا می‌شود؛ وقتی قیمت یک محصول سر زمین به ۵۰ یا حتی ۱۰۰ هزار تومان می‌رسد، باز هم سود چندانی برای کشاورز باقی نمی‌ماند؛ چون هزینه اجاره زمین، بذر، کود شیمیایی، کارگر، گازوئیل که باید لیتری ۳۰ هزار تومان خرید، سم و هزینه برداشت، همه بر عهده کشاورز است و در نهایت چیزی برای او باقی نمی‌ماند. چرا دولت جلوی گرانی بذر را نمی‌گیرد؟ چرا کود شیمیایی به کشاورزان نمی‌دهد؟ چرا سهمیه گازوئیل کافی اختصاص نمی‌دهند تا کشاورزان مجبور نباشند گازوئیل آزاد بخرند؟خدا به داد کشاورزان برسد.
🔹
داروی متیل‌فنیدات (ریتالین) در کل استان آذربایجان شرقی کمیاب شده است. به‌جز دو سه داروخانه در تبریز، در بیشتر داروخانه‌های استان این دارو موجود نیست و فقط هر دو سه ماه یک‌بار، آن هم به تعداد بسیار محدود، عرضه می‌شود. این در حالی است که این دارو تولید داخل است. چرا باید با کمبود آن مواجه باشیم و بیماران مجبور شوند داروی خارجی تولید سوئیس را از بازار آزاد تهیه کنند؟ قیمت هر ورق ۲۰ عددی این دارو حدود ۲ میلیون و ۵۰۰ هزار تومان است. پزشک برای پسرم روزانه ۶ عدد تجویز کرده که یعنی حدود ۲۰۰ قرص در ماه. من کارمندم و با حقوق ۳۰ میلیون تومان، چطور باید ماهانه حدود ۲۵ میلیون تومان برای داروی فرزندم هزینه کنم؟
🔹
لطفاً پیگیر حذف اداره و رفتن نیروی کمیته امداد امام خمینی(ره) از دهستان طرود در ۱۳۰ کیلومتری جنوب شاهرود در استان سمنان باشند. در شرایطی که خدمت به محرومان باید بیش از پیش مورد توجه دولت باشد، نباید اداره کمیته امداد از دهستان حذف شود و مددجویان، به‌ویژه افراد سالخورده برای انجام کارهای خود مجبور به طی مسافت طولانی و پرخطر تا شهرستان شوند. تا امروز اداره کمیته امداد در دهستان فعال بود.
🔹
با وجود گذشت ۶ ماه از سال هنوز معوقات فروردین و اردیبهشت بازنشستگان تأمین اجتماعی پرداخت نشده و زمان واریز آن نیز مشخص نیست. لطفاً برای تسریع در پرداخت این معوقات پیگیری کنید.
🔹
لطفاً موضوع کارت امید مادران را هم پیگیری کنید. با وجود گذشت ۵ ماه هنوز خبری از صدور و تحویل این کارت نیست.
🔹
لطفاً پیگیر کپسول‌های گاز CNG خودروهای نیسان آبی باشید. مدت زیادی است تاریخ کپسول خودروی ما گذشته، اما به ‌دلیل هزینه بالای تعویض  توان پرداخت آن را نداریم. هزینه قطعات خودرو و لاستیک بسیار بالا رفته و شرایط مالی مردم سخت است. خواهش می‌کنیم مسئولان به فکر رانندگان نیسان و هزینه‌های سنگین تعویض کپسول‌ها باشند.
🔹
از پردیسان قم پیام می‌دهم. لطفاً موضوع قطعی مکرر برق را پیگیری کنید. چندین بار در روز بدون اطلاع قبلی برق قطع می‌شود و کسی هم پاسخ‌گو نیست. چندین بار در سامانه «برق من» اعتراض ثبت کرده‌ام اما متأسفانه هیچ رسیدگی‌ انجام نشده است.
🔹
برج ۱۰ پارسال از کارخانه سایپا خودروی اطلس با فروش تحویل فوری خریداری کردم، اما با وجود گذشت ماه‌ها، هنوز خبری از تحویل خودرو نیست.
🔹
لطفاً به وضعیت پروژه گل نرگس اصفهان رسیدگی کنید. ۱۵ سال است که این پروژه بلاتکلیف مانده و زندگی ما را نابود کرده است.
🔹
سه سال پیاپی از کمیته امداد یاسوج درخواست وام استیجاری می‌کنیم و همیشه می‌گویند در اولویت هستید ولی به بانک معرفی نمی‌کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/460354" target="_blank">📅 22:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7c44040b.mp4?token=XPxZDUb6PvQ7fJy95HWQHh-pgnlz-IYpXPlhqDjD7Qi0EN-c5rjU4mnPSMdlC2-eX2yL-qRqWRUxoL1555SkqwVNlg7sry3PBjYkAmW1aGdi6_q8NDs9FHBYYXpNQLpPM2upDFHluykIKEi6yLSaiRzpJbna0Cj6mRXqKzdvI-3Or0hrAngVhME5VI8bpXbr-CLC134mbiXYb6Sd1bcIrY97hXtJHg7gf0eM5Ad1NoQEJ_oO-q4TvsZOn5SLlPuVh36o4Kz99htLEdsgc6k-KNeBZyDI0WjnXKLEVOHXhQ_R46kOqntR4zvcrfvjceUbkUan_4fo8xkrOsY-36THow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7c44040b.mp4?token=XPxZDUb6PvQ7fJy95HWQHh-pgnlz-IYpXPlhqDjD7Qi0EN-c5rjU4mnPSMdlC2-eX2yL-qRqWRUxoL1555SkqwVNlg7sry3PBjYkAmW1aGdi6_q8NDs9FHBYYXpNQLpPM2upDFHluykIKEi6yLSaiRzpJbna0Cj6mRXqKzdvI-3Or0hrAngVhME5VI8bpXbr-CLC134mbiXYb6Sd1bcIrY97hXtJHg7gf0eM5Ad1NoQEJ_oO-q4TvsZOn5SLlPuVh36o4Kz99htLEdsgc6k-KNeBZyDI0WjnXKLEVOHXhQ_R46kOqntR4zvcrfvjceUbkUan_4fo8xkrOsY-36THow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: دستگاه‌های دولتی را ملزم کرده‌ایم که فقط از بنزین ۵ هزار تومانی استفاده کنند  @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/460353" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b961cb87.mp4?token=MdUCJ14UxGU_WIFuOdelLsF6Z-4TMEx2nESZqV47kWjsF65WZjVa4b6kJfVabOZAvzRAzyvMrQNa2JVRntpCFYbrD4akxCfoSDzAowNNLii_7bxZPTJjuOwvPhMOHocq4A03NDMc0L9FjxQ22985u9Cxc9m_y-pZWBj8n6HV4XG3E9a8Rdlfc_i7QNZZApzhfb_vVpWNDnSnQFNJjrCcTbHdMrJXPsBiCi6NM--rghoravytWpDw5P9s-eDtYW0OMaH5iOdVNnzoHdi308EIpaR_a4LoROow_8S_IOX_sB9ubfEzcmCUSAo5ND63sA4UODMPW3SN-LTiHCkEkgawpWukpH7qmlTgMRMNQTRDhwWRg6lXXDSr_89cX4MHQSOPRKjUq49TtcNO21zHptl88En7hkxzu4_vkgLSl-0wF3_CJFYVajkHG2A5k8XVQUHyv1CCJ-i-axY6Taj6OVdPc2kAWc8geXj8BNPV7Q1RFwsHD84bBLBpcX7yElQyp74KgnRgUJI3Trv1juhP8PhJnfmGXse4Pmyiio_eg2Fgud7pBkiXX6dvBUIKLPB55oXqvSR8mLLVQzCSsVg175UDxRaAu9ksFlCQcDQ1Qxx_CdQJrQ0xLEWPxoskSJGimGRCvClcTVsc1Kvj-dprxayBz4W9VoJwmIMpAFBen5_sGRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b961cb87.mp4?token=MdUCJ14UxGU_WIFuOdelLsF6Z-4TMEx2nESZqV47kWjsF65WZjVa4b6kJfVabOZAvzRAzyvMrQNa2JVRntpCFYbrD4akxCfoSDzAowNNLii_7bxZPTJjuOwvPhMOHocq4A03NDMc0L9FjxQ22985u9Cxc9m_y-pZWBj8n6HV4XG3E9a8Rdlfc_i7QNZZApzhfb_vVpWNDnSnQFNJjrCcTbHdMrJXPsBiCi6NM--rghoravytWpDw5P9s-eDtYW0OMaH5iOdVNnzoHdi308EIpaR_a4LoROow_8S_IOX_sB9ubfEzcmCUSAo5ND63sA4UODMPW3SN-LTiHCkEkgawpWukpH7qmlTgMRMNQTRDhwWRg6lXXDSr_89cX4MHQSOPRKjUq49TtcNO21zHptl88En7hkxzu4_vkgLSl-0wF3_CJFYVajkHG2A5k8XVQUHyv1CCJ-i-axY6Taj6OVdPc2kAWc8geXj8BNPV7Q1RFwsHD84bBLBpcX7yElQyp74KgnRgUJI3Trv1juhP8PhJnfmGXse4Pmyiio_eg2Fgud7pBkiXX6dvBUIKLPB55oXqvSR8mLLVQzCSsVg175UDxRaAu9ksFlCQcDQ1Qxx_CdQJrQ0xLEWPxoskSJGimGRCvClcTVsc1Kvj-dprxayBz4W9VoJwmIMpAFBen5_sGRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفر مجازی به مدرسه و گلزار میناب میسر شد
🔸
قالب مجازی مدرسهٔ شجرهٔ طیبهٔ میناب را در
اینجا
ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/460352" target="_blank">📅 21:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1ec93d48.mp4?token=MIY6N_t429PP6oAyRMUOdxdrBb_7hy0fVtN0-jOQN_ykBKljUjZ-WUVIH3VbTS5rmLWsEtXXwer-VInaOBLEYVR59a-vf6M0aEkZxLmThFXxqo9Gj2ULxYM-aJoKfayDLQ5H0dogh-Yu5vyDRQC9R2GrrfTdtmWDP5jncUap5nZKjVftFfI1rkvdxJO7bujSeJeB3ZHxepcDmNj7XDtX2WXJeU9sT31Nx3Ngo-mifEo72TTsHYkt0WnXwogSwSeX8H_YGRZnTQSxqPz3v6Pnd7nzOw4ReYBDFaqL8QIGB4oXm25z9SUxBEVTuzEbhljod2cOQcJ1D_33OvxAsA49-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1ec93d48.mp4?token=MIY6N_t429PP6oAyRMUOdxdrBb_7hy0fVtN0-jOQN_ykBKljUjZ-WUVIH3VbTS5rmLWsEtXXwer-VInaOBLEYVR59a-vf6M0aEkZxLmThFXxqo9Gj2ULxYM-aJoKfayDLQ5H0dogh-Yu5vyDRQC9R2GrrfTdtmWDP5jncUap5nZKjVftFfI1rkvdxJO7bujSeJeB3ZHxepcDmNj7XDtX2WXJeU9sT31Nx3Ngo-mifEo72TTsHYkt0WnXwogSwSeX8H_YGRZnTQSxqPz3v6Pnd7nzOw4ReYBDFaqL8QIGB4oXm25z9SUxBEVTuzEbhljod2cOQcJ1D_33OvxAsA49-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌پناه: در یکی از جلسات استانی یکی از حاضرین به رئیس‌جمهور گفت «استعفا بده» اما ایشان با متانت پاسخ داد
🔹
نگاه رئیس‌جمهور این است که حتی مخالفانش هم بتوانند بدون لکنت‌زبان با او صحبت کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/460351" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmFAuGwYFptb7MrlyiZEh_7wQR2Xbagw3rif55AtQTPAP6E3b8JTD3QC9oUjWtb4YB7hclMShddmrIhClrflnhtuveKpxAqd9D0vf_aDv_PZbATaCKDzd7y4R-f30--ArTxmz2cAI-s4uHR-yu6pHor4hdEPs7wbnHglSq_Q8Ta36_hlzJK1qVRQVfkE0nq3cJDxbXUgF7nWDkQeJfSEAaQfSh8cyFWGF1MvF2xJ4nOEWoiVjb3gcszZ5exnsWTFPVbiSPKeZHj0U-GUFATDWJS2EjrbPz0EeBj2l3YIGWr7Qr-QOmkGL09d_MpceYRPgiAhHqFTqlkCONrMeoQonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/460350" target="_blank">📅 21:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e633fa345e.mp4?token=Gmcy6wURon9N0vwGWphhoFpHCauEU0mHmOxP296su9qdLq6rlPDrVR2i7ln9rUHlVC5wqYRoq9-IpzrDLAih-Pc-NpM12lRvU5K_5xClAy-ppli9cy5puu-CFr1MGkD8x4UCcGfmgIu3SBcPMxWq_guRO51USsmhoc1VEe2jo0c5CYOH-jB1NTeB-MvaeSBLDwcSTU9AXRFLDNKsz7GHSjNITVzdgbAKVHXCcYZpLqZjgcWBf988BYCTV3nz9imKDIhhzFkX8xQOHVtxlf5T3SbwU9vVsNBtJ0pjiGGR25v6SNL5p-ubdn5T_NgYYni4Uv6TlabphT8SjrKtJdbsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e633fa345e.mp4?token=Gmcy6wURon9N0vwGWphhoFpHCauEU0mHmOxP296su9qdLq6rlPDrVR2i7ln9rUHlVC5wqYRoq9-IpzrDLAih-Pc-NpM12lRvU5K_5xClAy-ppli9cy5puu-CFr1MGkD8x4UCcGfmgIu3SBcPMxWq_guRO51USsmhoc1VEe2jo0c5CYOH-jB1NTeB-MvaeSBLDwcSTU9AXRFLDNKsz7GHSjNITVzdgbAKVHXCcYZpLqZjgcWBf988BYCTV3nz9imKDIhhzFkX8xQOHVtxlf5T3SbwU9vVsNBtJ0pjiGGR25v6SNL5p-ubdn5T_NgYYni4Uv6TlabphT8SjrKtJdbsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دادستان تهران: به دستگاه‌های مسئول دربارهٔ کارت‌های بازرگانی اجاره‌ای تذکرات جدی داده شده است
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/460349" target="_blank">📅 21:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51287f30a.mp4?token=lNdgB_JbyWqErAiWcDiFygH7COt1elVX-zSL_QsPJwN2JA_SaB407qZVULMUvOx2bbaQhuXFTGG_CRUuzw-pL_eK4ueYvwf3bbU9o-j3yotqJlkDp355nShEGHpvWCHaen5FlE9vA_ucXQcsJQ79ph-ZkGwD3U5woJmSv6m4UewAluyW1LGGlp5NcblQ1H6VmDqveh6VLIVe9-mcF74WMVDaNGCxg3UYj-ERfZSNcJPICqrB9Ch_3sojeKUFoBhYTgYaEXbfrahhEKeyYRWors16eJlPjljPDjUqBPa2P4FCdzODkFfO1kXEq3ahBMzaMYoO2AJrUKpOnm0znsNkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51287f30a.mp4?token=lNdgB_JbyWqErAiWcDiFygH7COt1elVX-zSL_QsPJwN2JA_SaB407qZVULMUvOx2bbaQhuXFTGG_CRUuzw-pL_eK4ueYvwf3bbU9o-j3yotqJlkDp355nShEGHpvWCHaen5FlE9vA_ucXQcsJQ79ph-ZkGwD3U5woJmSv6m4UewAluyW1LGGlp5NcblQ1H6VmDqveh6VLIVe9-mcF74WMVDaNGCxg3UYj-ERfZSNcJPICqrB9Ch_3sojeKUFoBhYTgYaEXbfrahhEKeyYRWors16eJlPjljPDjUqBPa2P4FCdzODkFfO1kXEq3ahBMzaMYoO2AJrUKpOnm0znsNkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت وزیر جنگ ترامپ از حملهٔ ایران به ناوهای آمریکا
🔹
هگزث: اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را غرق می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/460347" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkESVi-XngEpFT-UfQDvoReGAXIHPHhCD6i99zUVkZsGQu4-2fMOBqgGJi40SOR49O6WyKzAy44tkb3AteAHY71mTJNYbmN3r-X1mjzou1srUeacwjd939HtK3N3E71jV-H5cWtd8McYyUDPN6F4VelQirx4jMPAyWFSC-5Od22BRRLBEQoBny1UHX1BffIk0QypTRikn07Uw5ffJ_S6BGLDmePYviB8JUxkkliftf63u3-78EkRvSHVRjDlnh4Ab8intnoDOYAqtjXVe5DDBCCUs9MzWAM_D56lA1sHZCyYqJKzIXd27NkU7HM8k_3ydyuR66kdv1EaDcNp7Iu1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت وزیر جنگ ترامپ از حملهٔ ایران به ناوهای آمریکا
🔹
هگزث: اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را غرق می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/460346" target="_blank">📅 21:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9327dbf73f.mp4?token=HKITowcC-3nzlU6dqNjElOiYM6Je5d_ocDAh_xQYzfcvYKl3NtzgLmLjS_haGOUfR-g8oyHik_UaHkuA0Wg4B5XrMdzwTe6XQEDx8ONQOtrm5ExPQ3mTtuBn-92Cq6HuCjNDEZ8bV1UUK93hNBAY093PvAW-gN42eIYZNpTBMiG3z-APyUguc0DzrIims2WwBUgYzXrZb-lBVu7aQCZImqnVpFoXOObDRAisyLhkhNJM-zV-G4WXEeMTR2yCTin4Dvl3M7W912rXnKlAYcdkdLntCic05ktywL2ZHs5rnndEnXsEStqIaTek2k4_r3ND3nwaDGh7V-oSPsfk6tlDGkhPcnfodeJF_uYZRKHt-FCt9Dn2UkOKPXjcRvzU3UyH_48L_H2lzoHgm1XU6Le4Cs3pkKBQqX02rdZIM9ySwLN_mTBT-cpecDwMBgs9dfJ7pT1rw70qu-1FrLN-fvQLKjxax_bk16h5PAbiKKOxbQYemCskfomdflMrFJrgzaqfrU2AIXi7Q_lrG1Au9XiAhAGimmnUh7EWlGKmjcWQ38JwhKGDuGP13AKNw8jwinsVLhKmoejf4LfbEqEnC8P8qiJGEYmAx1mr__LCaGROhO1TOpUq5tCWkG7p7oAEZl5NsN83yofbKWZMBhZqzH4FxnJq_dMYfEBmfaBL4gpfEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9327dbf73f.mp4?token=HKITowcC-3nzlU6dqNjElOiYM6Je5d_ocDAh_xQYzfcvYKl3NtzgLmLjS_haGOUfR-g8oyHik_UaHkuA0Wg4B5XrMdzwTe6XQEDx8ONQOtrm5ExPQ3mTtuBn-92Cq6HuCjNDEZ8bV1UUK93hNBAY093PvAW-gN42eIYZNpTBMiG3z-APyUguc0DzrIims2WwBUgYzXrZb-lBVu7aQCZImqnVpFoXOObDRAisyLhkhNJM-zV-G4WXEeMTR2yCTin4Dvl3M7W912rXnKlAYcdkdLntCic05ktywL2ZHs5rnndEnXsEStqIaTek2k4_r3ND3nwaDGh7V-oSPsfk6tlDGkhPcnfodeJF_uYZRKHt-FCt9Dn2UkOKPXjcRvzU3UyH_48L_H2lzoHgm1XU6Le4Cs3pkKBQqX02rdZIM9ySwLN_mTBT-cpecDwMBgs9dfJ7pT1rw70qu-1FrLN-fvQLKjxax_bk16h5PAbiKKOxbQYemCskfomdflMrFJrgzaqfrU2AIXi7Q_lrG1Au9XiAhAGimmnUh7EWlGKmjcWQ38JwhKGDuGP13AKNw8jwinsVLhKmoejf4LfbEqEnC8P8qiJGEYmAx1mr__LCaGROhO1TOpUq5tCWkG7p7oAEZl5NsN83yofbKWZMBhZqzH4FxnJq_dMYfEBmfaBL4gpfEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح نخستین مدرسۀ شبانه‌روزی هوشمند پلیس با حضور رئیس‌جمهور
🔹
ایدۀ تأسیس این مدرسه که در ۲۲۰ روز ساخته شده و به بهره‌برداری رسید، از سرلشکر شهید باقری بوده و به گفتۀ سردار رادان این طرح در شش استان دیگر اجرایی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/460345" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f33bddeb2.mp4?token=IADoSv2p0AIpzYaLchtUmROIYWv6f-d2jFGZZsptRuBxPzthi4jGUXyI9cVJ8X0uFftdi2_kCoSGmsoITqPjxgSEYT77J0Yn_D5Nq-7jRfrMgukm0fwdYvE1GpQpNamTmrnsle_hsRwR5FRrjvau4k9rGR0JxccgLJopmm_6thW9i7lRu-UYRehrqMr0_4C_5OuQ_riB5_3wGc0BeBy9Ul1GZARYEm-JvLZ2ZvwHEhqryTYFaxIR02o8LBrcxCpmu0-rXg50EY2JnflF3ZoiGauKDIY6fjjVdNpXPn6xkXnvXXnNXgNTuO9Mrn3SApkAssrbBKYbd9gLsL4kfHrPBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f33bddeb2.mp4?token=IADoSv2p0AIpzYaLchtUmROIYWv6f-d2jFGZZsptRuBxPzthi4jGUXyI9cVJ8X0uFftdi2_kCoSGmsoITqPjxgSEYT77J0Yn_D5Nq-7jRfrMgukm0fwdYvE1GpQpNamTmrnsle_hsRwR5FRrjvau4k9rGR0JxccgLJopmm_6thW9i7lRu-UYRehrqMr0_4C_5OuQ_riB5_3wGc0BeBy9Ul1GZARYEm-JvLZ2ZvwHEhqryTYFaxIR02o8LBrcxCpmu0-rXg50EY2JnflF3ZoiGauKDIY6fjjVdNpXPn6xkXnvXXnNXgNTuO9Mrn3SApkAssrbBKYbd9gLsL4kfHrPBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا با این سربازها می‌خواهد قدرت‌نمایی کند؟
🔸
کاربران فضای مجازی در حال دست‌به‌دست کردن تصاویری از سربازان آمریکایی هستند که تیزرهای هالیوودی آمریکا را زیر سؤال می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/460344" target="_blank">📅 21:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460341">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عصبانیت وزیر جنگ ترامپ از حملهٔ ایران به ناوهای آمریکا
🔹
هگزث: اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را غرق می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460341" target="_blank">📅 21:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W49H8OjHthyH8_a3e9SLkvzMJ-l4SVlVvZyuHwjqQQzxNMykbo4qS_UvjiJPBTpyxJTi4Y0UfhkbyWwoIqUPWodDLMwnvmLvZ-Pm69RFxlu255VCfD94RRdb4N4IhftZIt9mXkeshamvzkOwn1F0e9HeJK8vhi5snf7FQkMWiTKzYUMiXVQxPwIwiGlRErM7zah4N-8O10G3QmZKzLNVH-DGz24NgVrBXRU-bZgMoDxZJz-nE4ZHX2FgjPP1rmu6VsnKcckvR-QeWC1R82Dy7LO-2N5fq_QeQBIO9gp8Sg4aysUM5xfPnMjjPw5-F__Y1Jxsu5sOd71AG49gdT1HXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، حردانی را از استقلال کنار گذاشت
⚽️
بختیاری‌زاده: تا زمانی که من سرمربی باشم حردانی دیگر در استقلال جایی نخواهد داشت.
⚽️
او  فقط به خاطر صحنه ضربه ایستگاهی در دربی کنار گذاشته نشده و از اول فصل ۳ بار به خاطر بی‌نظمی به او تذکر دادم.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460339" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac6e51157.mp4?token=CLfH_kBrXrWxmx6MHLctrTIiaYZ5an4unoT-2zZglbmsPudEi_6FErFECvNCetxVIC1kWZbmvewjUp56UUrqeOpkjIX9927NNJ-yjLD5NDjBaUKhOklORN8f3sPOt6bkFbeVVsM4oSDycDNKywa-5esBPnPqOaTZ-lSBUSj53kcotYO0MYy7rJ4mv5bjkPt8qdpS-DqPejbBl-tsna2aauY8DAE-lxd715PJzo7y7idaH091GF7S4EMQwTdMPu7fRUxgatYofoJ2_3Mw6Or_9cB1ih7pcmWnHGEOvQCgx-3RAUoTZDiwv_lH9Kt5U0ednYOgS5Nuy4nlpLGGbLSruRezQ7hoHIgC3_Cb66bk3Q4w7g0snorze6FYW1KIhhjb9FoEEl3fPwRX1lT2vELHbN8_1pPCkheK1S-tHJV6y2sU9bS9qVnFpYH6IORfHlVniLZdAENAYb1eRWl-5iJL9SFXh1H4mnn6x7rjjE8dSxpmVwIDfwRHgotCkmXVJzQLQ0enVZ8SSEvCNsjFWKSLnqAIpklja-Ac4D6Kyuvw8AyBZyxdh-sEnoFebm8Sgrt4EMLlk9xddcJ-Jsz_lN8rFilzFYcFqZiV-2l952FrF7rx3hh_qtU4lLdMcnbVuSP0Sna51hJgAcGhbFmfw2CL4L9xgeph5FF7ubkvoI5S3Z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac6e51157.mp4?token=CLfH_kBrXrWxmx6MHLctrTIiaYZ5an4unoT-2zZglbmsPudEi_6FErFECvNCetxVIC1kWZbmvewjUp56UUrqeOpkjIX9927NNJ-yjLD5NDjBaUKhOklORN8f3sPOt6bkFbeVVsM4oSDycDNKywa-5esBPnPqOaTZ-lSBUSj53kcotYO0MYy7rJ4mv5bjkPt8qdpS-DqPejbBl-tsna2aauY8DAE-lxd715PJzo7y7idaH091GF7S4EMQwTdMPu7fRUxgatYofoJ2_3Mw6Or_9cB1ih7pcmWnHGEOvQCgx-3RAUoTZDiwv_lH9Kt5U0ednYOgS5Nuy4nlpLGGbLSruRezQ7hoHIgC3_Cb66bk3Q4w7g0snorze6FYW1KIhhjb9FoEEl3fPwRX1lT2vELHbN8_1pPCkheK1S-tHJV6y2sU9bS9qVnFpYH6IORfHlVniLZdAENAYb1eRWl-5iJL9SFXh1H4mnn6x7rjjE8dSxpmVwIDfwRHgotCkmXVJzQLQ0enVZ8SSEvCNsjFWKSLnqAIpklja-Ac4D6Kyuvw8AyBZyxdh-sEnoFebm8Sgrt4EMLlk9xddcJ-Jsz_lN8rFilzFYcFqZiV-2l952FrF7rx3hh_qtU4lLdMcnbVuSP0Sna51hJgAcGhbFmfw2CL4L9xgeph5FF7ubkvoI5S3Z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قتل‌عامی که نمی‌شود آن را اتفاقی دانست
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460338" target="_blank">📅 20:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0b92a715.mp4?token=fPO-luncKUQ6PsT7s5FRjDx-ylOvMC1j2V1N_RC10D42lyl6qYW8HSiUY7jkxy_9LpCHQb5B33xfqyHRDbquiMlqURfRHdNRSllgyD5CbPk09rUCCb75HQDAWJ2v5E1IuLwqxSeU6SVA2sPz7JUp6yOizxkwAl39TkoJiH8KM4a2cXeHv9Q0v-B5-abDxqEUjGvMoBLxGrPIBLBxF1rwhn92nL85PBHcwpRAo4pIlw3IUlKUIJ7JUjL30IFnfo1P4H3QOiVbCW9q-_f4LyesGwfyDoLyIaDbYXhvD5Y2cofI7YrpDuy1NorZjpLpYWpiRuMs7mN0pguaRaP4aNhfw1WoOLHztkeTzVkHNHh45xf7dodZkjgyk9qXtVTajULKFLNNk-3FLMf7gv13ACQIZ4fUgDPyfFRA48_3uB4FXvUyY4t-mKrIGKNKbWZhruNap8MGMmerHznKaXQCoIPoQyWPYovxc69un3n2Nt1BPoNtOtiWxt9S2BmGsToJfHACTyP_xXQnZ0HtRUwpxIXazpB9TgfmahQ1Rg48YHLyowmzWCP59W_FzC5rige569-DdFQPYTVDfTK0Y_HKCXoT9mwDjF328BzlxY-7tKtLuPT3FsYvP72hGRyQY0bTHU1qaiCWoEAJZcN1SvKqPAJ0XJmRQNhpCvYh4COTgmK0jyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0b92a715.mp4?token=fPO-luncKUQ6PsT7s5FRjDx-ylOvMC1j2V1N_RC10D42lyl6qYW8HSiUY7jkxy_9LpCHQb5B33xfqyHRDbquiMlqURfRHdNRSllgyD5CbPk09rUCCb75HQDAWJ2v5E1IuLwqxSeU6SVA2sPz7JUp6yOizxkwAl39TkoJiH8KM4a2cXeHv9Q0v-B5-abDxqEUjGvMoBLxGrPIBLBxF1rwhn92nL85PBHcwpRAo4pIlw3IUlKUIJ7JUjL30IFnfo1P4H3QOiVbCW9q-_f4LyesGwfyDoLyIaDbYXhvD5Y2cofI7YrpDuy1NorZjpLpYWpiRuMs7mN0pguaRaP4aNhfw1WoOLHztkeTzVkHNHh45xf7dodZkjgyk9qXtVTajULKFLNNk-3FLMf7gv13ACQIZ4fUgDPyfFRA48_3uB4FXvUyY4t-mKrIGKNKbWZhruNap8MGMmerHznKaXQCoIPoQyWPYovxc69un3n2Nt1BPoNtOtiWxt9S2BmGsToJfHACTyP_xXQnZ0HtRUwpxIXazpB9TgfmahQ1Rg48YHLyowmzWCP59W_FzC5rige569-DdFQPYTVDfTK0Y_HKCXoT9mwDjF328BzlxY-7tKtLuPT3FsYvP72hGRyQY0bTHU1qaiCWoEAJZcN1SvKqPAJ0XJmRQNhpCvYh4COTgmK0jyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیش از ۶ ماه حضور؛ مردم همچنان برای ایران به خیابان می‌آیند
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460337" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7993c3473a.mp4?token=pQSWkCVhwf-BHspWzulejuuKKPjZMxOaY4r-WvVnjTSpgGcS2S9kgZAjrpGbHRBCEYuqCUNgYh0h3B8kccWthty3Ju4L0VfhmcwxO4wU7Je5fbHaj5tES2uqkUqMismv2Ftb466_drlcek7M1k4m3wTYvV29OPRpSeTqK0gnWXosuVGAs9plDAHQGNw01vKWyt0B5KxuHrq_4xfqiTsZs0BUUzSjdKQtOy6YczI9NkZ2O-w7JRYizbX7urDUlzlabbE1QK8zCIMUdJWwpd9Y59hGrnp57u_LgBlSEbia3pkO1VOliHFxZ-2ah86dij-t3DepWo2N7bIG--cEGIltkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7993c3473a.mp4?token=pQSWkCVhwf-BHspWzulejuuKKPjZMxOaY4r-WvVnjTSpgGcS2S9kgZAjrpGbHRBCEYuqCUNgYh0h3B8kccWthty3Ju4L0VfhmcwxO4wU7Je5fbHaj5tES2uqkUqMismv2Ftb466_drlcek7M1k4m3wTYvV29OPRpSeTqK0gnWXosuVGAs9plDAHQGNw01vKWyt0B5KxuHrq_4xfqiTsZs0BUUzSjdKQtOy6YczI9NkZ2O-w7JRYizbX7urDUlzlabbE1QK8zCIMUdJWwpd9Y59hGrnp57u_LgBlSEbia3pkO1VOliHFxZ-2ah86dij-t3DepWo2N7bIG--cEGIltkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت میدانی خبرنگاران از تپه علی‌الطاهر لبنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460336" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1fa49b79.mp4?token=cNOBM4DdwI793ypcbidVGB_JG7m_ykZaLtPRJ05ef5MCpSIh4g9Zt3VXp5ytSve4gIr3diripY48CuquD02RLJYyeFE3zEO7i-7BAudLBYRA4ip64Yw7cD1HPGMAevCPtb2hTrpFCQpQ7et9XE6mH43jfMDDyXu4BJo31UXb4W7ehohhSkEyjZDvx5QtP-oQ6zP5QcpJ3391M599qDiMOWJhGSbFzZAERM2Cva45zofBNSFEPBH9O11Gki8onPCqENPCqoONTHIJev8FJiBHehNIpnfJ2rU9muv-FcLEwiCe8JHD8EYOq8XZcu5JPNdY6JDFe_tJ1vey48GabON7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1fa49b79.mp4?token=cNOBM4DdwI793ypcbidVGB_JG7m_ykZaLtPRJ05ef5MCpSIh4g9Zt3VXp5ytSve4gIr3diripY48CuquD02RLJYyeFE3zEO7i-7BAudLBYRA4ip64Yw7cD1HPGMAevCPtb2hTrpFCQpQ7et9XE6mH43jfMDDyXu4BJo31UXb4W7ehohhSkEyjZDvx5QtP-oQ6zP5QcpJ3391M599qDiMOWJhGSbFzZAERM2Cva45zofBNSFEPBH9O11Gki8onPCqENPCqoONTHIJev8FJiBHehNIpnfJ2rU9muv-FcLEwiCe8JHD8EYOq8XZcu5JPNdY6JDFe_tJ1vey48GabON7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در شمال تل‌آویو
🔹
منابع خبری گزارش دادند یک فرد مسلح به سمت نیروهای امنیتی رژیم صهیونیستی در شهر «نتانیا» تیراندازی کرده است.
🔹
برخی منابع اسرائیلی مدعی شدند این فرد مسلح یکی از نیروهای نظامی این رژیم است که دست به این تیراندازی زده است.
🔹
این منابع ادعا می‌کنند این فرد نظامی با مشکلات روانی مواجه بوده و دست به این اقدام زده است. گفته می‌شود نظامیان صهیونیست این فرد را به ضرب گلوله کشته‌اند.
🔹
در حال حاضر، نیروهای امنیتی اسرائیل محل تیراندازی را محاصره کرده و به هیچ کس اجازه نمی‌دهند به این منطقه نزدیک شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460334" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afGrPomM3IFfyFj22JimTidRy3-1hqajuCFY4x-ZecS3Dwxtg_KbJ4OXyIni_Wa4Awuyeh6mvsYvuYufJFwnPumHGhLKPi7Mryi9yr1kHGek24mlgsrVjmpNFnOJziS4H87js5DgwwzekaVLdNOPHupwv6gI4ux_Fi3m_0yk_Spr2qVbiR3eeh5sySrZ2oQnnc32XLfbgDd2gx5qy9qyHMS8KoOYDTKnPiH56NBdDs7f7xylAKvNSUTTm5LoOIlGE_Dd_wMPpSq-3hvA67he-m-O0jCvSU6_LB7haloKYPjgOve5XZB2usMOXuMdAYCD-vIFx5wf4z3wU8mwbDuqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سنتکام: ۳ نفتکش ایرانی را هدف قرار دادیم
🔹
فرماندهی مرکزی ایالات متحده روز شنبه اعلام کرد که ایران «چندین» حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی انجام داده و مدعی شد که آمریکا سه نفتکش را هدف قرار داده است.
🔸
سنتکام در بیانیه‌ای مدعی شد: نیروهای…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460333" target="_blank">📅 20:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aawWo1v8QoDQ1mNfCfPvPRER4WmiL5L_xid_8MvGK6kcG7iKEt5GDxo6jFRTvriC8trT0EwzArZs5J50_jB9Do2ny7eZydWQP17hGsVmOj-YJdguHDBZGM_IceYWlaWGmCBxQZrnH3EBO9H_cRgrnYYhQ1eQx1J8yWZS-uxprWTCMvzryzsIZCd09J_JkgyutqTxXz25SCXjvSaEiLzZgcSOFKon2zj71YhHu9JdZqn9tqZawjf9uim_25IkBrNdJFeyubpaxTHZ15MrnYL5MqSVwXrqaD6bThLwcCq0Zh2MzhFxVqrBGLhbQ5aa-BUTyA6arZ1__HTtek8GmbZ9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
افتتاح متمرکز هزاران پروژه‌ خانواده ارتباطات در سراسر کشور
رویداد ملی «یک ایران متصل» به‌زودی با حضور جمعی از مسئولان دولتی و فعالان حوزه ارتباطات و اقتصاد دیجیتال برگزار می‌شود. در جریان این رویداد ۷۹۴۷ پروژه ارتباطی و فناوری اطلاعات در سراسر کشور با برقراری ارتباط مستقیم با ۳۱ استان به بهره‌برداری می‌رسد.
«یک ایران متصل» قرار است تصویری از دستاوردهای دوساله وزارت ارتباطات و تلاش خانواده ارتباطات کشور برای توسعه دسترسی عادلانه مردم به خدمات دیجیتال، افزایش پایداری شبکه و تقویت زیرساخت‌های اقتصاد دیجیتال ارائه دهد.
هدف نهایی این طرح‌ها، کاهش فاصله مناطق مختلف کشور در برخورداری از زیرساخت‌های نوین و نزدیک‌تر شدن به مفهوم عدالت ارتباطی است.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/460332" target="_blank">📅 20:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خوزستان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKgAnRkIM11odOUhxVKr1bWKXio7DAv4v534AWPXD7nht1hN9HC25bffoTj5flkUE83Thr-cCzTYI0FcFuz4sSKvX6qex27kwDb9nAiTjszoFuIv1y81EK4cd-9-VbsczOvlRRBIRUWaLmKzSsvOgpUoOufDcPsE9tXpOne5VYnlNIZN0huBQ4GNQk1hl7QTLU3jjnx_es9stPskcaMHYy-vSsQPqPr6YMW1x9Akgssm7eGRMJdZV1VFlqjaxz5RSZRJvXIBL3qCj5QurPxI8IP9QRRRmXbTbpvkRfoS9M4QSaKsIGcV6V884pkGCIHCYaCuulQuKdJOh9nQi3inQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی بر حال و آیندهٔ صنعت فولاد در جهان، خاورمیانه و ایران
🔹
مدیرعامل شرکت فولاد خوزستان و نایب‌رئیس انجمن تولیدکنندگان فولاد ایران با تشریح تحولات صنعت فولاد جهان، خاورمیانه و ایران در یادداشتی تحلیلی بر حال و آیندهٔ صنعت فولاد در جهان، خاورمیانه و ایران را تشریح کرد.
📎
متن یادداشت را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460331" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/460330" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774f07ed16.mp4?token=DIpnPm3vqAygR8NtH186rpuWgsInfn_g6qOZsulucC_SkSGVVVcvxU_l3FQM5qDCR3J1wYX2XDv7EEjgRtcJqdrvKcbezndjtRS8eKaLJcQN0zw7rP0kglc3GZa1bcAsZqxp2MSB0BYlqIWs9Y3V_u9GRVq7bjZ7o1Mjoj39CNmbY6qYdtPtNGimqFQHhrkNoxJmLkFIMOa24YiqDrFQmKucVIlHLPjeSMuzWyCmh8KqB15NuCBrcmrIosFBIxvhvObXMBJegszobkBLYDZwhAYT-6Lxt238-mqTK05NhoIkiU1vTsDoM0SUF5J8Tpuawzel3PqipQ-L5579chq2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774f07ed16.mp4?token=DIpnPm3vqAygR8NtH186rpuWgsInfn_g6qOZsulucC_SkSGVVVcvxU_l3FQM5qDCR3J1wYX2XDv7EEjgRtcJqdrvKcbezndjtRS8eKaLJcQN0zw7rP0kglc3GZa1bcAsZqxp2MSB0BYlqIWs9Y3V_u9GRVq7bjZ7o1Mjoj39CNmbY6qYdtPtNGimqFQHhrkNoxJmLkFIMOa24YiqDrFQmKucVIlHLPjeSMuzWyCmh8KqB15NuCBrcmrIosFBIxvhvObXMBJegszobkBLYDZwhAYT-6Lxt238-mqTK05NhoIkiU1vTsDoM0SUF5J8Tpuawzel3PqipQ-L5579chq2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزارت اقتصاد: شرکت‌ها و سازمان‌های عمومی غیردولتی سهام‌های تودلی خود را واگذار کنند
🔹
معاون سیاست‌گذاری اقتصادی وزیر اقتصاد: تمامی موارد مشمول مادهٔ ۵ قانون برنامهٔ هفتم در دستگاه‌های اجرایی، شرکت‌ها و سازمان‌های عمومی غیردولتی شناسایی و از سوی وزارت اقتصاد اعلام شده؛ این مجموعه‌ها مکلف به واگذاری سهام تودلی خود هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/460328" target="_blank">📅 20:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی‌شده نداریم
🔸
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند. @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460327" target="_blank">📅 20:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=droTWyVq3zRYSCZwOZQg9SDsRaBTrqNBDWCwOclWGJGwP4TJHIXt74HrQ9Q0NSWfzYaqHYPWg4tyjIYnu28u_xYd8TrcBvZXb9UIM7fCZTqqAyglUaGOJz_RSafJjNk2nIcmiLPAQ1ay94aVdKIpsOxifZ7jnZg_8g-1DCSdoipbZUQmW2AHyM_04XWMGkgvpnEqKchnFarddgZhFV_IXWTBnj0W1SIBIj1Fqu0Ul7pbT6AMBS1QME9akwE9nOkefficcz-LCQm8rWbJRCoSFopxpFDvPq0TLMvWMmqNY_qyHYflfLtaGqS6nI2h4nEAYffAmHmwqBdQP2v5GpaxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=droTWyVq3zRYSCZwOZQg9SDsRaBTrqNBDWCwOclWGJGwP4TJHIXt74HrQ9Q0NSWfzYaqHYPWg4tyjIYnu28u_xYd8TrcBvZXb9UIM7fCZTqqAyglUaGOJz_RSafJjNk2nIcmiLPAQ1ay94aVdKIpsOxifZ7jnZg_8g-1DCSdoipbZUQmW2AHyM_04XWMGkgvpnEqKchnFarddgZhFV_IXWTBnj0W1SIBIj1Fqu0Ul7pbT6AMBS1QME9akwE9nOkefficcz-LCQm8rWbJRCoSFopxpFDvPq0TLMvWMmqNY_qyHYflfLtaGqS6nI2h4nEAYffAmHmwqBdQP2v5GpaxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی‌شده نداریم
🔸
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460326" target="_blank">📅 19:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3aaaac38.mp4?token=su-I6FJIz1KeLp26_s22fdtldDiTpMR7t1d8gOXdKe3vyp98I7lkbs8HO0KNEidw8Qmc5_IYq_G9vkHVQNhBRB4c0EFfDbBq5mW1wNsMJfthKduBe1JS9AIhg6CniVaxRl5sw8A13vapDfv3RQV9yhxhMYA5OEEG4jokHUnxSmN6EaYraW1jZNftDAjEW0Sd_wZ_VRJKWe-1Zcw9bJh4Oxa5GE9deA-lsoc1KEXRn-lWF-jCFMs5LsVFgFf9f-aHirkUOvAw0nPBhrL7FMB_BnX1riTrxk97iSPv55IUxEn-Djwm1Idtidd-GrexBmnzvyr-JETNyMvY3zeSDOqCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3aaaac38.mp4?token=su-I6FJIz1KeLp26_s22fdtldDiTpMR7t1d8gOXdKe3vyp98I7lkbs8HO0KNEidw8Qmc5_IYq_G9vkHVQNhBRB4c0EFfDbBq5mW1wNsMJfthKduBe1JS9AIhg6CniVaxRl5sw8A13vapDfv3RQV9yhxhMYA5OEEG4jokHUnxSmN6EaYraW1jZNftDAjEW0Sd_wZ_VRJKWe-1Zcw9bJh4Oxa5GE9deA-lsoc1KEXRn-lWF-jCFMs5LsVFgFf9f-aHirkUOvAw0nPBhrL7FMB_BnX1riTrxk97iSPv55IUxEn-Djwm1Idtidd-GrexBmnzvyr-JETNyMvY3zeSDOqCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند برای تراکتور پاس‌گل داد
🔹
در جریان دیدار تراکتور و گل‌گهر، گل اول تراکتور توسط حسین‌زاده و روی شروع‌مجدد خوب بیرانوند به‌ثمر رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/460325" target="_blank">📅 19:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJvX1KjCyGp8Y8h73vfTn_D-5CAPlo29aaPYrHTwXYksOHyH1Mop6FFkaIeoJB-SsxgsPU8XAfMDsEmzGxpso4GMxiN4tr6lrcaAvOB_UXfBvE0AZ9a0tmEHsPbUerfuMy3AgDHl2sMjW-RchQVK9Xl1VMNlacV0WdRt8AvK-X4IlSJd8jUoRREIfnehLF7sF196gdb40i-BbzRFN-jv1BFZrPMjB9wGUPrtMtj2cSiLecLZSsfvcccXvn5oJT3ceaur1AkynKjrqrZPU96XNkVtzrjlx3aua036ZVqei14nytyHOPaf5mIBO039M3iUzI_pz9W21oNQcbYaO2-luw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۱۱ شهروند سنندجی در آتش‌سوزی تانکر سوخت
🔹
رئیس مرکز فوریت‌های پزشکی کردستان: در پی وقوع آتش در یک دستگاه تانکر حامل مواد سوختی در پلیس‌راه سنندج - همدان، ۱۱ نفر از شهروندان جان خود را از دست دادند و ۵ نفر نیز مصدوم شدند.
🔹
به محض وقوع حادثه، تیم‌های عملیاتی آتش‌نشانی و خدمات ایمنی شهرداری سنندج  به محل اعزام شدند و عملیات خاموش‌کردن‌آتش را آغاز کردند.
🔹
علت دقیق وقوع آتش‌سوزی و جزئیات مربوط به جان‌باختگان و مصدومان، نیازمند بررسی کارشناسی و اعلام رسمی دستگاه‌های مسئول است.
📝
اطلاعات تکمیلی پس از مشخص‌شدن جزئیات منتشر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460323" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90712c8bd.mp4?token=jx9vBCx7T5hFqDfwQiFrw60s86qBfBP5m7K2XMZCkXWc7tRCxtGdQWq2w8VGxDTWUm7VYBm6enGjqdHlJQ1MIluJkpiWuX15--EAcVffcxfqRethBRC0HqvPMTf4zOsgv2rnRCeOrZohuIddXLpe0FQdbWk9JJBUCA4Ue5dKYthyp1SZW-2oG1FaY5cCAy1EnE-nIo-fkvKJ_8WMXRIbYbKNO_L8kn4IQGY48L0kn8-OjzJNq82YhpHhoNOTDiQvxsK8lwLVs1BZv06JciVwwk_Q07w2ao_tavbHunUbDtKz1jHNM2PdxpzDUvBGvp4Y1iMYAdgSPCbMku_4xjGifw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90712c8bd.mp4?token=jx9vBCx7T5hFqDfwQiFrw60s86qBfBP5m7K2XMZCkXWc7tRCxtGdQWq2w8VGxDTWUm7VYBm6enGjqdHlJQ1MIluJkpiWuX15--EAcVffcxfqRethBRC0HqvPMTf4zOsgv2rnRCeOrZohuIddXLpe0FQdbWk9JJBUCA4Ue5dKYthyp1SZW-2oG1FaY5cCAy1EnE-nIo-fkvKJ_8WMXRIbYbKNO_L8kn4IQGY48L0kn8-OjzJNq82YhpHhoNOTDiQvxsK8lwLVs1BZv06JciVwwk_Q07w2ao_tavbHunUbDtKz1jHNM2PdxpzDUvBGvp4Y1iMYAdgSPCbMku_4xjGifw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/460322" target="_blank">📅 19:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5ef53ffd.mp4?token=nSsEUZtPQIkNio8vlEQMNNEGMGfoOOdAWcPVQE2aoOewjgGBrVi9JkCfplzGFOx4kuJint17OYoalkXnM_u_VUYByGLJkazakCwulLBtV4mFaVDMSvboaZfqXsh1UbYFE0UHyL9pZYvDoF4yfz_2nlCApZXbWcdwan_k-jU0mdJO8Lghm0beQUiEhWMZ4PQnDvOZLL3MOraS6BZkKQbLoJ9-9blmi32HQ7POc192W04YoQOMqkI8e-Rpi15rsVFA3FtJgKDjVWd78yhl6R4MT8G9cbW_mTpCUZvIpEQVhUOwcRW5V830d4zbPpxPGhIE9ZT_Pbzx08sb32pCA9X4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5ef53ffd.mp4?token=nSsEUZtPQIkNio8vlEQMNNEGMGfoOOdAWcPVQE2aoOewjgGBrVi9JkCfplzGFOx4kuJint17OYoalkXnM_u_VUYByGLJkazakCwulLBtV4mFaVDMSvboaZfqXsh1UbYFE0UHyL9pZYvDoF4yfz_2nlCApZXbWcdwan_k-jU0mdJO8Lghm0beQUiEhWMZ4PQnDvOZLL3MOraS6BZkKQbLoJ9-9blmi32HQ7POc192W04YoQOMqkI8e-Rpi15rsVFA3FtJgKDjVWd78yhl6R4MT8G9cbW_mTpCUZvIpEQVhUOwcRW5V830d4zbPpxPGhIE9ZT_Pbzx08sb32pCA9X4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند برای تراکتور پاس‌گل داد
🔹
در جریان دیدار تراکتور و گل‌گهر، گل اول تراکتور توسط حسین‌زاده و روی شروع‌مجدد خوب بیرانوند به‌ثمر رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/460321" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934d60155e.mp4?token=BU2o46FovP6Pndh7QFLQR7nv7HYEIzxL_ZMLGTBq3-XPDgLkA_yYrm6oldUdAJAUCtxOGUCyivasU0GmlEMTsVZsLn_KUA4unENttM3T6xkBrsOvTgCkbJhK8jryL3LyVMb6NhDKnEjDxtIvsqfiZ532-4wBniuqRZNGhupRKVyZYElCUeek7TrQeYFeIWifzwrxeWPpw71NZsuDqrQXz_5fddQ0s90X-pwZp0WRj6yxYV7Db9_Qmf3aqHRUWOO3Y1RqkNvaaObgqG1rIKs4eFzWmlCGPUMpdLDLlXyQM8gtAsjAejzrBleRh90LH-xVT7A-IG4K54HHFevXyp5cXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934d60155e.mp4?token=BU2o46FovP6Pndh7QFLQR7nv7HYEIzxL_ZMLGTBq3-XPDgLkA_yYrm6oldUdAJAUCtxOGUCyivasU0GmlEMTsVZsLn_KUA4unENttM3T6xkBrsOvTgCkbJhK8jryL3LyVMb6NhDKnEjDxtIvsqfiZ532-4wBniuqRZNGhupRKVyZYElCUeek7TrQeYFeIWifzwrxeWPpw71NZsuDqrQXz_5fddQ0s90X-pwZp0WRj6yxYV7Db9_Qmf3aqHRUWOO3Y1RqkNvaaObgqG1rIKs4eFzWmlCGPUMpdLDLlXyQM8gtAsjAejzrBleRh90LH-xVT7A-IG4K54HHFevXyp5cXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان‌باختن ۲ خلبان اف۴ در یونان
🔹
رویترز: درپی سقوط جنگندۀ آمریکایی متعلق به ارتش یونان، هر دو خلبان جنگنده جان خود را از دست دادند.
🔸
این حادثه امروز در خلالِ نمایش هوایی در پایگاه تاناگرا در شمال آتن رخ داد و جنگنده در فاصله حدود دو کیلومتریِ فرودگاه سقوط کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/460320" target="_blank">📅 19:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeed2da28d.mp4?token=YX9fUIwCv_oo3NwHrd6qOZTnB7WHZsN3T0GuwHnX2vh8VcXv7YkZw5N5-j-S-ApZqvjY4JQVhdCUP0GQhCFz8AdUF2kzvUdNI8X8HpMPCq-yoATc9RQCTb8bSTWSfHNZXVkxfKZLdVHT_GwDsBv8gWRDUls8nAyAmPbTIppchndQ1gqS2Y9Jqj811DQynrJpkTcWZzA0X40x1Pk2tKdQI57Uh_vy0hgmVoufNviQdWbi8mtQ2-PFUNSZNr7EiJGqWpuuSOljuyNev1fliE9LwiFUrYNHmR-2-wwLcVvNCJkYGGlKOgXV8WJ6QEYoAE3ON3XzBAYolnqe3N7umd9OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeed2da28d.mp4?token=YX9fUIwCv_oo3NwHrd6qOZTnB7WHZsN3T0GuwHnX2vh8VcXv7YkZw5N5-j-S-ApZqvjY4JQVhdCUP0GQhCFz8AdUF2kzvUdNI8X8HpMPCq-yoATc9RQCTb8bSTWSfHNZXVkxfKZLdVHT_GwDsBv8gWRDUls8nAyAmPbTIppchndQ1gqS2Y9Jqj811DQynrJpkTcWZzA0X40x1Pk2tKdQI57Uh_vy0hgmVoufNviQdWbi8mtQ2-PFUNSZNr7EiJGqWpuuSOljuyNev1fliE9LwiFUrYNHmR-2-wwLcVvNCJkYGGlKOgXV8WJ6QEYoAE3ON3XzBAYolnqe3N7umd9OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: در سفرهای استانی آقای پزشکیان مخالف بودند که جمعیت زیادی به استقبال ایشان یا اطراف خودروی ایشان بیاید.  @Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/460319" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3910de1b1.mp4?token=otU05fYDng6K4IsbLGByM8x4qR9Lb-K5h88ODPl289Ysj6b1FBw2K_Wbk3pTYhf4RNJtCnu3nrCb3MsIU0oqtCuteHtVlXuPXOps2k9mjIATlKoeqVB6cnXvwhcVlIgXIomy1dtA_CwH7CWnX0EFKIesnpxHt0G_0-JnohI0B7QY1YhqRGFtmrDXB4yPSqX0AIOhJr-nIRa-AvKKVuDE0PowvrKJq7c7dqHpEQtRw4D2egDIPrEcjYxpjPDq4rmrceYIKZHGGXeU4bHZ-0AA2EC4m1xOV5O7eLPCmFLk2kUgRVKNIcqPbDfegxK2GTgjS6H1B7gUwl_wqBKabwT6Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3910de1b1.mp4?token=otU05fYDng6K4IsbLGByM8x4qR9Lb-K5h88ODPl289Ysj6b1FBw2K_Wbk3pTYhf4RNJtCnu3nrCb3MsIU0oqtCuteHtVlXuPXOps2k9mjIATlKoeqVB6cnXvwhcVlIgXIomy1dtA_CwH7CWnX0EFKIesnpxHt0G_0-JnohI0B7QY1YhqRGFtmrDXB4yPSqX0AIOhJr-nIRa-AvKKVuDE0PowvrKJq7c7dqHpEQtRw4D2egDIPrEcjYxpjPDq4rmrceYIKZHGGXeU4bHZ-0AA2EC4m1xOV5O7eLPCmFLk2kUgRVKNIcqPbDfegxK2GTgjS6H1B7gUwl_wqBKabwT6Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: در سفرهای استانی آقای پزشکیان مخالف بودند که جمعیت زیادی به استقبال ایشان یا اطراف خودروی ایشان بیاید.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/460318" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4gFNfRvvioGpopbbuOChxFNSTdkZ4vw7fzTA84s5UOcKXiCq9zJnXoylcmMY6uCIPGLtQZkDZuC04MGYGWJx8AWU63HUb6BxiODs096H3vr_Q8-p3UIlDF-NHvalMkOCtX00ZoTIPf2LAx40oKQ8XcMms7AUtAgc9lRwD3y48v3SD_dVkzboJBNbToZFot1ewhBBsxcdW4kuqeKkxJ6ZJkqeuons5ATiS7IryIh5rFPXT9k3oZDdaYEPAcuNTi3iNnTPdAWANQ7lUN79OG_8TIRLnMUdyDQb1O3GWsoqMr2TbikjRKPRrlw76ZSMdNR7fFNfuxDa4_97alSdofoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ امنیتی در تنگۀ هرمز و در نزدیکی سواحل عمان
🔹
سازمان عملیات تجارت دریایی انگلیس خبر داد که برای چند شناور در شمال سواحل عمان حادثه روی داده است.
🔹
برخی منابع خبری نیز اعلام کرده‌اند که چند کشتی و شناور در تنگۀ هرمز هدف حمله قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460317" target="_blank">📅 19:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph6fmUmblqZu6AAQjbyq-9jVppybQVYYnAhDIA704tJ1BgcjSamcET9psmfm9n46vRZ9SPDX300gJe-TBobk8mcSfe0e9GI9PlQ-wSedNXz6tkWNCXl8Smbm0uSi7ybKhFxhCa1UTop4gEC7iGsbhI-cNd-NBC_B5RvIrZqQo4UcjO02gW_05xUVfoh_EPtIzVMbkjcQa_fC2Ckyz5bZNSUFX9Za8h6nfC9sCq-zZmnGuF3Kq_BhYHY2hpHsDojToRUaYvcaSuR_OKtqOXc_fpzFM9KTa01BtPIJlTj48n953kbjjgmbQjcU3ptwmtNs4Bim62GS3X0wFdckA5rU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازماندگان از تحصیل امسال می‌توانند به مدرسۀ مجازی بروند
🔹
مسئول مدرسۀ مجازی هلال‌احمر: از سال تحصیلی جدید دهک‌های یک تا ۵ کشور خصوصا بازماندگان از تحصیل می‌توانند رایگان در مدرسۀ مجازی هلال ثبت‌نام کرده و توسط استادان مجرب آموزش ببینند اما کلاس‌های حضوری برای یک میلیون دانش‌آموز بازمانده از تحصیل، سال آینده آغاز می‌شود.
🔸
به گفتۀ وزیر آموزش‌وپرورش، حدود یک میلیون دانش آموز ۶ تا ۱۸ سال در کشور به دلایلی مانند مشکلات اقتصادی، خانوادگی و اجتماعی از تحصیل جا مانده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460315" target="_blank">📅 19:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دستیار همتی: پول نفت همچنان به کشور می‌رسد
🔹
دستیار رئیس بانک مرکزی در امور ارزی: محدود شدن صادرات نفت به معنای «متوقف شدن فروش نفت یا وصول منابع حاصل از فروش‌های قبلی نیست.
🔹
حتی در صورت ایجاد محدودیت در صادرات و فروش، «منابع حاصل از فروش‌های گذشته» همچنان می‌تواند وارد چرخه تأمین ارز شود.
🔸
چند وقت پیش رئیس بانک مرکزی گفته بود که «ما نفت صادر نمی‌کنیم و این یک واقعیتی است»، ذخایر ما را آمریکا مسدود کرده و به آن‌ها دسترسی نداریم.
🔸
اما آمارهای وزارت نفت نشان می‌دهد که این وزارتخانه از ابتدای سال تاکنون ۹ میلیارد دلار درآمد نفتی را در اختیار بانک مرکزی قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/460314" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG1KUOGwj_KIyrr-JVUauZqSBX-FvaXI3AVL3T1QYd8armYW0u71MZDbH8IWrdq20xMPkcAA70NcxN_2Zj8VgydjoiC6zwgz79SaJnjyY6_A9zOVKI_d14LxsWD7oovAP2MQ3MCRVjGqJFwKyuoWvZLSIuxun1sVvqkRfqhKEAbUq4eotQVnYrg4zg2NEPhpPuBOnC3mbrPoSdZwnOTsYP1B8YWqZzJWvHE-GASdHLEP3H7jsCRDPA5QGFmOnh7Cxg6QXyvoVgIvbOKNunUk24dNpEjLSuRgNl5SkWm8EHjyPZgfpS8sy93oJ8LiZ2BxscBZhPKPBWf7S_N655qtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: در مدارس دولتی هیچ مدیری حق دریافت شهریه هنگام ثبت‌نام را ندارد
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/460313" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prGmX1OtLKhPBwGcUse46N1044qEZLN9V2G8FiwnZ1VZ8Z-0f3R_d9aVFchsNs82Ks9baN5TfxpZ3-t22praeMDG6i_gzpx5hPyMS0-7AKETyOmIItzdR556HwL4Y0UGrJIuLkysyKyicLep7aeKJ_neXzJgViDsZdvetyyGx9YbS-tA3h7t4BqlK6zUg06FR9UeOyIaU76QpvJfgIDhKaq8R_ChNNF483Dz9jS8TXrPSGlLCXnVcpwTcLNhodTwWSmSrlBk6YVrIPJxMCdB7k46zLSsT-IVjk8DfFWTxinoEIGVK7WhFWsuNP0BQcRRNat0KRgeO6UEXU83Hm6-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر بیش از ۸ هزار شهید غزه هنوز زیر آوار مانده است
🔹
سخنگوی دفاع مدنی نوار غزه: پیکر بیش از  ۸ هزار شهید همچنان زیر آوارهای غزه باقی مانده و به دلیل حجم ویرانی و کمبود امکانات، عملیات جستجو و بیرون آوردن اجساد با دشواری مواجه است.
🔹
یکی از برج‌ها در اطراف خیابان العشرين در شمال اردوگاه النصیرات، در طول جنگ مورد حمله قرار گرفت و در آن زمان بیش از ۳۵۰ شهروند و آواره در آن پناه گرفته بودند.
🔹
تیم‌های دفاع مدنی از آغاز جنگ تاکنون موفق به بیرون آوردن حدود ۱۶۰ جسد از این مکان شده‌اند. لذا ۱۹۰ جنازه همچنان در این ساختمان، زیر آوار قرار دارد.
🔹
عملیات جستجو و بیرون آوردن اجساد در این شهر با امکانات ابتدایی از جمله فقط یک بیل مکانیکی صورت می‌گیرد و همین مسئله باعث شده عملیات بیرون کشیدن جنازه‌ها بسیار دشوار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460312" target="_blank">📅 18:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک نفر در رابطه با پروندهٔ دختر اشنویه‌ای دستگیر شد
🔹
چند روز پیش دختر جوان اهل اشنویه که چند روزی مفقود بود در حالی که شرایط جسمانی نامناسبی داشت در پیرانشهر پیدا و به یکی از مراکز درمانی منتقل شد.
🔹
او به دلیل شدت جراحت وارده دچار مرگ مغزی شد و خانوادهٔ او با اعلام رضایت برای اهدای اعضای بدن این دختر جوان، تصمیم گرفتند از مرگ او، زندگی تازه‌ای برای بیماران دیگر بسازند.
🔹
دادستان عمومی اشنویه در این‌باره گفت: پس از دستور ویژه برای بررسی و پیگیری مرگ این دختر جوان، یک نفر متهم در ارتباط با این پرونده هنگام خروج از مرزهای غیرمجاز در استان کردستان دستگیر شد.
🔹
تاکنون خانوادهٔ مقتول در دادگاه اعلام مفقودی یا علیه کسی شکایت نکردند اما با توجه به جزئیات پرونده و جریحه‌دارشدن احساسات عمومی، دستور ویژه برای پیگیری این پرونده صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/460311" target="_blank">📅 18:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ساعت کاری ادارات تغییر نکرد
🔹
با ابلاغ رئیس سازمان اداری و استخدامی، ساعت کاری فعلی تا پایان تابستان باقی خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/460310" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-H70MgkXnWSa31rXov4ie4-n9M70-uQ71YY409Ig6fU56zPqqqRq5PR77TYzABoUWhcTqqHwt91dRgFQsBoe8-rGtP8lcVgvu2tTIn5u6TBcesgiDPlEW8L9GrOJImq44dhPMNnZkRZadUfLPS9q-ws4VBjXZ102rNfDIb9qX9mzsLCxzTlP95HRGyS6kbsuMjMSqCjzbAb6I1TAs1oIdjaFBGPV_Y02kERaThD37zz-ZibMT28U_f8K9BlM7wX1o-R6YIhgXOKK7PQqT8mSPAM9Z7yurtrFb49TiTiFUYHZrBZae-lf4-IAA4SK42ZIW3Q1RtSgQeC9Au4Sd0fUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djW-iLKAn56SIGyKuTFHA0yXTVbBZA3dgaJMSmsA2BLLLHEdyyXM505hT-nlRCSyUkiSgGFrrvzEKhL5Vd0Idj-DtlnRKk27fvq6VZVbCZ57rkrdU9wnOsMu5f8zaNHc1oh5mwBKTJBSwWiTsOA0d8fqqyyPGyagBikgshL7cgbKWBPsfbEGTff2Pk3kmmOY9gCZyPsC-S2iFSWPfkIsY4o2Gnqpwc3-DAxt21tdCPaLfjQRztFnTo4YRzzmU6Bg9-AvdB6qGww-WYvjSEmn7wM9opeyt7G5cr_Pv8OG_S-1WAVLkGITpdG5_8AM6G42HSfD2wz0Kb-emFPraGM06Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ علیه ایران؛ مهم‌ترین عامل پشیمانی رأی‌دهندگان به ترامپ
🔹
دونالد ترامپ که خود را یکی از موفق‌ترین و بهترین رؤسای جمهور آمریکا معرفی می‌کند، در همین مدت دو سال، با به راه انداختن جنگ علیه ایران، حدود ۴۵ درصد از رأی‌دهندگان به خود را پشیمان کرده است.
🔹
طبق نتایج نظرسنجی انجام‌شده توسط مؤسسه نویگیتور، حدود سه‌چهارم (۷۴٪) از این افراد، عملکرد ترامپ را تأیید نمی‌کنند؛ این در حالی است که این رقم در بین کل آمریکایی‌ها ۶۰ درصد است. همچنین نزدیک به چهار‌پنجم (۷۷٪) از عملکرد رئیس‌جمهور خود در زمینهٔ اقتصادی ناراضی هستند، در حالی که این رقم در بین کل آمریکایی‌ها ۶۳ درصد است.
🔹
علاوه بر این، نارضایتی رأی‌دهندگان به ترامپ در حوزه‌های سیاست خارجی، قیمت بنزین، قیمت مواد غذایی و مراقبت‌های بهداشتی، همگی به بالای ۷۰ درصد رسیده است. در این بین، بالا بودن قیمت سوخت و مواد غذایی با ۸۳ درصد، بیشترین میزان نارضایتی مردم آمریکا را به دنبال داشته است. جنگ علیه ایران مهم‌ترین عاملی است که به افزایش این قیمت‌ها منجر شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/460308" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsFGB4AO3kZPGENIQbA2_BXnRtHJVbXW_FN0MW3eprsEkWwHbcpJZ9y7qBJwz_Hd-bZ-jDpQgz-OcV7KcLPOBlQqBnUdb2dpueA6xHGWP9Sda_PTPFIQUK7mJLaz51jvp_IKH1QzZrXNtjVAMyVeQmaqZbKOh4dx0v05uSSDIGa2--4KlV5RKUxxLjrqu18tkUiJr-dRyYGnI0GONRzXvptNjDqBKKSA2tqjm8Sy6mTKVS4TnOpx7j_4pB5nv9d4OyuJGm5AU1xRCXhl7_gu_cf0MJnUdmKk4Y6b7atzCVSdXwppHmfKcanzYOL3bBnAd7l48EFVl0utFPbh37c0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با حملهٔ سنگین موشک‌های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460307" target="_blank">📅 18:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTOI0jVBKgm9HjJIscVSenUkEFHM4moPlEZhpAlDQ7InHajhAo0wmn-IT1oEoDst9casMMid5YO1NhoPkXmQN7Mi8ILemCaBzJlhQWa73_lXlNiy0krnQZmqJ6S3UMIs0sEIxi9fFJBmmcklc2I_4YZ-XvKr_uJnpwiG0J78E99mvhPy2D0dWZVxjXkwSQ75t-NDnvhLnpMn5DGmd62XCdtS5ndYLNU-8Np_Y07CJKY71jov0vNd8yTl1FLzKJsKsiuxBVtnPmBb3Uyl9fIbqQfgBJzFL3lkfP2D1RrPhirSgUrJdaBHlVOc_rXEFQ32Z12z40CbrROQmcd2b1eqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۲ هزار تُن برنج وارد کشور شد
🔹
وزارت کشاورزی: یک کشتی حامل ۲۲ هزار تن برنج وارداتی در یکی از اسکله‌های هرمزگان پهلو گرفته و عملیات تخلیه و بارگیری محموله روبه اتمام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/460306" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYroOi2RH7af_8Bxcki9bGNVqlWX7JVoiFDvpVILq2rFOLgQQQFi5gQQ3BOzNtFiabc5rbLObX19KLejb45QuXFf3aSO2cg8jcBghHVGV63FhCSg51h_kORJnSmpZ-CM7aGK22PlfF6k3ATyi-NjTTkc5bpkmaAOIXAHxTTQZ5BcLyOgGHVWVdX0x9hN_cvlRd0VY7nBYX-VqQnnSS609Cnz9N_j32-BZaLylOViYcIKQo71Adem96wMGFltEkV-jBpy6qd6MxF3rbTGJg7WrBlKe_kF-WBEwd2jSIKeWmVa_ZhPxBbvb0VNK5tKmaaWjC5YL7k5TqwykM5_aUdcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت پایین‌ترین سطح صادرات نفت سعودی در ۹ سال اخیر
🔹
خبرگزاری آمریکایی بلومبرگ: صادرات نفت خام عربستان سعودی در ماه آگوست به پایین‌ترین سطح خود در حداقل ۹ سال گذشته رسیده است.
🔹
حملات به کشتی‌های سعودی در دریای سرخ، محموله‌های این کشور را از طریق مسیری که…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/460305" target="_blank">📅 18:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqKxXccLG9dHpnvcrRDTNKRzPXl-SH4TUxlpsXY37D5g2IitchER0sYOx0YuyJBQduCXOMOzbEzfstJ9HVD1gn47GFlZwETOMLAaozD4wYrGJqzxjYEGw8mNnaXZ3hbDGnomkMgPMxT_zSs8k_lQ0i_BUTxJ6x2CgceXDa-VDymDTfg7X14kOnUbR7kAdXCa1H4OuV3bmzI6ItTsDjNWnY5DJn9DmDpW4-wJMtzVgAvAu5UVhjCtziraoJUtF52jlS8_6gyGeBIv6_q0GyRiEQoQzOrQ0lvqhEau8Tiay_vDCuyX5PPKCOLa8fambtxB8j3YC7nyFfAtAoj2SZHKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانسل: روند تمدید خودکار بسته‌ها جدید نیست؛ کاربران: پس چرا شرایط تغییر کرده؟
🔹
پس از انتشار گزارش‌هایی دربارهٔ تمدید ناخواستهٔ بسته‌های اینترنت ایرانسل، این اپراتور در جوابیه‌ای اعلام کرد که قابلیت تمدید خودکار موضوع جدیدی نیست و تغییری در سازوکار آن ایجاد نشده است.
🔹
ایرانسل می‌گوید در خطوط اعتباری، مشترک هنگام خرید بسته می‌تواند تمدید خودکار را انتخاب کند و در خطوط دائمی نیز این قابلیت برای برخی بسته‌ها به‌صورت پیش‌فرض فعال است و هنگام خرید به کاربر نمایش داده می‌شود.
🔹
اما این توضیحات درحالی مطرح شده که شماری از کاربران در روزهای اخیر از تغییر روند پیشین خبر داده‌اند؛ از جمله اینکه در بسته‌های اعتباری، گزینهٔ تمدید خودکار اکنون به‌صورت پیش‌فرض فعال است و کاربر برای جلوگیری از تمدید باید خودش آن را غیرفعال کند. در برخی بسته‌های دائمی نیز گزینه‌ای برای انتخاب‌نکردن تمدید هنگام خرید دیده نمی‌شود و کاربر باید پس از خرید، تمدید خودکار را جداگانه لغو کند.
🔹
از سوی دیگر، پیامک جدید ایرانسل دربارهٔ بسته‌های اینترنت نیز ابهاماتی ایجاد کرده است. در پیامک‌های اخیر آمده که بسته‌های ۵۰۰ مگابایت و بیشتر، با رسیدن حجم باقی‌مانده به ۵۰ مگابایت یا رسیدن تاریخ انقضا، به‌طور خودکار تمدید می‌شوند؛ درحالی‌که متن این پیامک با اطلاع‌رسانی‌های ماه‌های قبل متفاوت است و مشخص نمی‌کند این قاعده دقیقاً برای چه بسته‌هایی اعمال می‌شود.
🔹
این موضوع پیش از این نیز محل اعتراض کاربران بوده است. در سال ۱۳۹۸، اعتراض‌هایی دربارهٔ تمدید خودکار برخی بسته‌های ایرانسل مطرح شد و سازمان تنظیم مقررات و ارتباطات رادیویی (رگولاتوری) اعلام کرد موضوع را پیگیری می‌کند. پس از آن، ایرانسل امکان لغو تمدید خودکار را برای مشترکان فراهم کرد و روش‌های غیرفعال‌سازی را اطلاع‌رسانی کرد.
🔹
اکنون پرسش اصلی این است: اگر این سازوکار تغییری نکرده، چرا تعدادی از کاربران از تغییرات هنگام خرید بسته، فعال‌شدن پیش‌فرض تمدید و متفاوت‌شدن پیامک‌های اطلاع‌رسانی خبر می‌دهند؟
🔹
به نظر می‌رسد راه‌حل روشن این است که ایرانسل، تمدید خودکار را به‌صورت پیش‌فرض غیرفعال کند و انتخاب فعال‌کردن آن را به خود مشترک بسپارد؛ یعنی کاربر اگر تمدید مستمر می‌خواهد، آن را فعال کند، نه اینکه ابتدا تمدید فعال باشد و مشترک مجبور شود برای جلوگیری از آن، هر بار به‌دنبال لغو آن بگردد.
🔹
به‌ویژه در مورد خطوط دائمی، اگر قرار باشد مشترک بعد از خرید هر بسته یک‌ماهه دوباره برای غیرفعال‌کردن تمدید خودکار اقدام کند، عملاً اختیار انتخاب از زمان خرید بسته به مرحله بعد منتقل شده است؛ درحالی‌که بهتر است این انتخاب از ابتدا و هنگام خرید، کاملاً در اختیار کاربر باشد.
🔸
اگر شما هم در روزهای اخیر با تمدید ناخواستهٔ بسته و به‌تبع آن کسر هزینه از شارژ یا اضافه‌شدن هزینه به قبض مواجه شده‌اید و نسبت به این رویهٔ اپراتور اعتراض دارید، می‌توانید شکایت خود را از طریق سامانهٔ تلفنی ۱۹۵ و وبسایت
195.ir
ثبت کنید تا موضوع توسط سازمان تنظیم مقررات بررسی و در صورت احراز تخلف، اپراتور ملزم به اصلاح روند شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/460304" target="_blank">📅 17:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای سنتکام: ۳ نفتکش ایرانی را هدف قرار دادیم
🔹
فرماندهی مرکزی ایالات متحده روز شنبه اعلام کرد که ایران «چندین» حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی انجام داده و مدعی شد که آمریکا سه نفتکش را هدف قرار داده است.
🔸
سنتکام در بیانیه‌ای مدعی شد: نیروهای سنتکام ۵ سپتامبر، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
🔹
ارتش آمریکا افزود که ایران با موشک‌های بالستیک حملاتی علیه دو ناو جنگی آمریکایی انجام داده است.
🔸
سنتکام در این باره اعلام کرد: «یک ناو هواپیمابر و یک ناوشکن موشک‌انداز آمریکایی با موفقیت از چندین حمله بی‌دلیل ایران جان سالم به در بردند.»
🔹
سنتکام مدعی شد که در این حملات، هیچ یک از پرسنل آمریکایی آسیب ندیدند.
🔸
ارتش آمریکا در طول جنگ بارها اقدام به سانسور خسارات وارده به پایگاه‌ها و تجهیزات آمریکایی در منطقه نموده و یا تلفات و خسارات را به صورت قطره‌چکانی علنی کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460303" target="_blank">📅 17:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460299">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqLqj6rmfD8ZzCuztzCFpXBvDAdnX5JXIPPyh0matAwDGCKwngfGWskeC8-0_imWE95VR9nMEMY2d09wVZDTyOGHTybvDr2mKqE6252ue2-byoh0L7IsYl_rZxPw8KLv8R6m_zHNmv2vqsiADd46iQcE6AlC9NCDY5qVSs-x17nIEIkpZ1qqcTdIOe1GDw6XKOOEf1baJSNSoTMiObaVXzhcI2lo0aWrrON31VXwC1LZ8Al-7golAZrYf6Y6K3EygXvCFqtp_VnTe11miay9kK0E6y2XUz2r-evAaWi8fSJ5zfWFMpjmU2Fw-Wg42O-0CoAibR0hTgg8trAnvyyaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارش معکوس برای انتخاب مدیرعامل جدید استقلال
🔹
جمع‌بندی هیئت‌مدیره استقلال و مالک تیم برای انتخاب مدیرعامل وارد مراحل پایانی شده و تا ۲۲ آبان تکلیف مدیریت باشگاه مشخص خواهد شد.
🔹
در فهرست گزینه‌های مدیرعاملی استقلال نام‌هایی چون عزیزی‌خادم، محمد مؤمنی و چند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460299" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f010400df.mp4?token=R9Dokj4YFBHjT_9TheGFXmWiPXaICqKb8uH2CQ6bPIc4LW-256AVK46Pzt2UWXN6RrJEJQ6pX-PN3RvxmXofmKa0k6Lqx8Q87na5hbow3VZnRLNmqb2JDvq1C9zWeNeLNR--iBLTV5hnkakaPpieOtOpzOnevo6DkehQIaTUNpZ2qPNOT-gSGGIk3fcHLc5ycf5jPEkhY8lnBaRSUuNJ4ZI7ybGDiMogtJVxeRSG1CyDqT6pqHIu6QWS4hKEppTZGTtzbc6x3-UkEApMVSmyPxoGMHRd83jKGf_e_NCAojD1VXcfzWvfhsXWkucS-zbps8szxX4i7Sbp1klAsEmoFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f010400df.mp4?token=R9Dokj4YFBHjT_9TheGFXmWiPXaICqKb8uH2CQ6bPIc4LW-256AVK46Pzt2UWXN6RrJEJQ6pX-PN3RvxmXofmKa0k6Lqx8Q87na5hbow3VZnRLNmqb2JDvq1C9zWeNeLNR--iBLTV5hnkakaPpieOtOpzOnevo6DkehQIaTUNpZ2qPNOT-gSGGIk3fcHLc5ycf5jPEkhY8lnBaRSUuNJ4ZI7ybGDiMogtJVxeRSG1CyDqT6pqHIu6QWS4hKEppTZGTtzbc6x3-UkEApMVSmyPxoGMHRd83jKGf_e_NCAojD1VXcfzWvfhsXWkucS-zbps8szxX4i7Sbp1klAsEmoFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌مقام حزب اعتماد ملی: دوگانه‌سازی میان جنگ و صلح وقتی در وضعیت جنگی قرار داریم، تضعیف‌کننده کلیت کشور در برابر متجاوزان است
🔹
نباید به‌گونه‌ای صحبت کرد که تصور شود ما جنگ‌طلب هستیم. ما اساساً صلح‌طلب بوده‌ایم و هستیم. طرف مقابل جنگ را به ما تحمیل کرده و ما ایستادگی کرده‌ایم.
🔹
رشادت‌ها به خرج داده شده، شهادت‌ها به وجود آمده و مقاومت‌ها صورت گرفته است. این واقعیت را نباید به‌گونه‌ای القا کرد که گویی ما صلح‌طلب نیستیم و حکومت ما نیز صلح‌طلب نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/460298" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460291">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XorXful04ZjRYOJ8TtQDvbaem31TtEqPjINGavZS5z766ZaCCowZ77VDylACz85LBck14YTZptxW9_ttDjwGEeZtGXMANXLKS5qT4ymh5ujMDcYrxWTI3TPiBZObU99zLJQlus6XOQ22IP8FNytPCZwlyPORHwu-7nNzbeYtrjib0i8L6utxzHWP467oo09UtyWXJ2G79OBTQwd6GHUMxBgxlNihXM9LA21SGjJq4MWHTbG-pZ-VJv5OPA_v3fitftz7F4g8dW3ERjhMS9Lm420LLIA8tzkGEEVvZxmdjWIhMpDF18TZ3wSXtKiu7vFNn8o97a_Q2SHfGzE3bmJv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZFOIb7mxnVPa0_cIaAp-w0SZbkfua6dYvch-VXd6-Vxe12G2o9HST5gF0xI14SuJK9hX1Ii3j1-zkVCEPHcaxHlCgv3a1hUHjkQRTlEb0DOh7zdhoDSs2qz2LAI47ml3gtOM7yoez97bebSefnSixj9CNQFTJbxC7gpGwM9lgvffUki26ADi6cAaDd4Vpusvik3W_EIA2GOispvWoEvPTMs5k5Fyb8EEb773S3WpXDuSCTZ_NQU8G_gM4wKqF1OkzDdvZs_-GyOM6UzRuOHyP9iLpMeSTyFwN0fm0nhc7XD5B9w0xGAQAHvIBLV-csAdlDWBZpgjhTGNlWzy9zf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFxQK9NqL1n_7fTRPWzrSeQoSdikv09V0kn-Pv-51flUCeP2jx2HMadNF6X4HiLgzgX6n2OFWX8-UglI3eQzPXsaYyjSzuRMT2P8Wl6v8_Emrg-ZQ6W3Y273HNqFa0dg8BCo75w4oJNk1f4GFFfzs87oJ5-qlUFCsvAFa_2N3p4ir3t3hrLo08nMFgVxhZyf2pnrHQPPCekSzyDzv9DAImj4_IG-2IWqsPb4ij5iW73XBKdCFYz30n0E-A50K7t_rA5zt97FPMdy-qno1grIKFCmr5FafJrv7vhbEK-xom9s718s9G5hirwfrpoz08tEDRU5uGXDragXJbjN-cC-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMdUFJLemqdZLgzXSFXWCVhctXI7g5Sb9sHcR5JVnJyp4HQKmuxPTYA4EhCP05OEfooOok7Lno6i4I_jz7j1n97w8PhY_52iD6ki4yAll-bmcfpoGk4v6QabJxRWfjB3ulrENWbt9kiPsOpbwM-m3Mi8ijsxN91D_kCPW46p02SHUXA4pDofRtSk8OqsgolUYrab6BbbhWtlnuJTqWuUmDpE09wlkNdm3PbK4nvQ-hY69Fjk870B_YYqj9BQCPxLk28tMaCJE2PqaE8CTxHXIiA5OH7nq1-_kyZG6qjRdgCvCRhB3OsvdVcUqU5iHGKMVP6pOxl0H4SsYWRJ-nf-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JowoefoxOKUJ5w6vgqwn5-iDjZXMwFyjTa0ogM9JMy83oJsd4tZvfSNR8GkwdIEgkK5wjkl-mRepQDYV2BK37hyFLuUZHXtlmZw684DJzXlPGHDbINU-GAXbqAPcv6lX522hfzEETJaqc-oG0pIOYJA1jYdfgzjq-3DebjtLVHv9P6padjftUtaVUy27xN2FM6zJ2gZ4ioRmvel-ihjJYj6q79MV_MB0Ib517NiDRiYM2Be1D57Bb379Eqz9d-otCkiy25viAlxpraoAgL8J8nKTrsqYGeit5rLzTDe9vmnnA5BCN_QaaKNphEzj8ofg2ekaJ7OSXVfYp8TWLNdUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXpFyO4mM-x7oBk_PVnjDOTqqzqQXn4Gzpy8yFwtlTj_FqM-gJn-dYh-S696zivFJEdOoYkLa7_eFzgu3s5lZbwI68XeNHi2Hs-3QL-BEK84RnJDvPNC-DsG0I3ZVoqBpsiqbD7j6IOIwIH16IV2fDp3ngSF4DoWqhkKzIKeSx4J-rI3DdWUo3rnEx7otcYWocCrmncDDmHILU1-zQc2-2y9LD1UknhieIvSw_snMCHGXc1NqER4btA4UnDAnQIOx9-Sd3677Oz6M7jbT-SIldE1RPh8JKPj1OLrt6wpwD1G2oSopgRi14kzuHL6nTee4xOeujj4K1V7RMMZQKOswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YN7hfQfptRM1zeDakcnVg8TQucXjVURqRa-2YBgyIrZsuJeNvAV7bkGgxGFxza0JZIp1ziftznWzyFmD74Z-cOeyNQHDTgPcqv4ZW1K5ww2_K2Qgrw_ok-FUunDxnqc25aunnBH_LmwGnTW6pozjZ3TpICTNQR_EvR0qEZirQu7GYfTixPnZMwsCm7wBsow9wfikm1DL_5hi3QLau4we5kCJwFiYHEOLDNOMkvYjhmrHuRszQ7WMVdyQSF3t_9eIY2iqjbOS2aZxPFONT3aWVt9D6j_lURFnHAqYBs6toMZFeAQdO86akH1R956pctwOnwSwmXujGit4nGhvRNPWxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قزوین در قاب تاریخ و معماری
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460291" target="_blank">📅 16:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460290">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c613f59c63.mp4?token=Vn78PkMAhjoib8NS4NxCW2nvU2lTITWo4lQuZHOinfZ5k7UrxDjY5vI3GieSPlTLfXRnDfrqlz9r5Jg5LPOKvAkdX3O_1liAgFMP2i9yo0DCwLoJiCu4NCCFLSjoAAYdxcgGu7vRGUVnASOF351E6xqpKbhQTXnzAYH7ongxlstcInr0nE7Tx0WaOEtJqd5inLsz23KDqKRJ9GurI5XhpVjVDcuo_WjSneW1xKX1mr0TYfMw7DB9d5-TX-gEh_nbZEgk8P_DK7HZRJw0X0io7GE3xLyP-VDTeKsUwp-grhwS1wEm4rS8Q3fzdQI7Q3IrZ5KJHfvwj_lC6ta-EOvyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c613f59c63.mp4?token=Vn78PkMAhjoib8NS4NxCW2nvU2lTITWo4lQuZHOinfZ5k7UrxDjY5vI3GieSPlTLfXRnDfrqlz9r5Jg5LPOKvAkdX3O_1liAgFMP2i9yo0DCwLoJiCu4NCCFLSjoAAYdxcgGu7vRGUVnASOF351E6xqpKbhQTXnzAYH7ongxlstcInr0nE7Tx0WaOEtJqd5inLsz23KDqKRJ9GurI5XhpVjVDcuo_WjSneW1xKX1mr0TYfMw7DB9d5-TX-gEh_nbZEgk8P_DK7HZRJw0X0io7GE3xLyP-VDTeKsUwp-grhwS1wEm4rS8Q3fzdQI7Q3IrZ5KJHfvwj_lC6ta-EOvyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سند کلیدی ساماندهی فضای مجازی در انتظار ابلاغ رئیس‌جمهور
🔹
رمضان‌نژاد، رئیس ساترا: شورای‌عالی انقلاب فرهنگی پس‌از جلسات متعدد، سند سیاست‌ها، ضوابط و الزامات حوزهٔ صوت و تصویر فراگیر را در آبان پارسال نهایی کرده. این سند که اهمیت بالایی در ساماندهی فضای مجازی…</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/460290" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460289">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIFvyu5V1xhfQ9apT4bubQVugeDwZu4yDpSjxzynWYM3VJbxoQx7KY7I-nVxiUBujPSvCjds--neWhbeXjI0DNzyimMN-fWsVled2S9hglpOakg2RHqj-lZYwoFty0DZQtju1NnPX2SevhS0_ukyqiOPy5I1tEa-GRTWRwNODHzXsTEtMXB-MOyuz8x4amaJ8wURltJOQUV13rCqsTz2yp8ahYP1gQurl57Fy4qWbcY1gOuqzrsLke53Aa5HnwArzFHLN0FUk-cy_SIM9BvgwWJg5KXz2ZbBnwf1yIkFmeKLDYSB2uEYU10xmWve4yUEVRpF_pn13oWsaPPx6tBFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور: دوران صرفا تولید و مصرف فناوری در ایران تمام شده؛ به‌دنبال مرجعیت فناوری هستیم
🔹
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در جمع نخبگان استان آذربایجان غربی گفت آنچه از یک دوره مسئولیت باقی می‌ماند، نباید به چند ساختمان و تجهیزات محدود شود؛
مهم‌تر از آن، ساختن توانایی‌هایی است که کشور را برای نسل‌های بعدی فناوری آماده کند.
🔹
او
هوش مصنوعی، فناوری کوانتومی، زیست‌فناوری، نیمه‌رساناها، رباتیک و فناوری‌های فضایی
را از حوزه‌های اثرگذار بر آینده کشور دانست و تأکید کرد که ایجاد ظرفیت به‌تنهایی کافی نیست؛ این ظرفیت‌ها باید به
کاربرد، حل مسئله و خلق ارزش
برسند.  افشین همچنین تأکید کرد که هدف ایران نباید فقط
استقلال فناورانه
باشد؛ در حوزه‌های منتخب باید به سمت
مرجعیت فناوری
حرکت کرد؛ یعنی ایران نه‌تنها فناوری را مصرف یا تولید کند، بلکه در تعیین مسیر آینده آن نیز نقش داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/460289" target="_blank">📅 16:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460288">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXHIVrATx5p6PvyIJKnb06GXHlyVpZWoUPs1T56wKAzH0fTn9gc89Tx7h3zskHYsHjtECl3ARUlFb-5afbAXU0oPj98q4SUUbOCy9bdHEsZxPbDEBbyfy0cEuxyLADBEmlWvF-6Ij_6Pw6E9-84RUFlur1yiGmDbjh-TiTnWatr2U3ILPMbuAmBUayYzBvqfybO-eh4EjaS7JXfymYZ2_R1eoHoWhKEdh8dbkTjNlTY1zD3oWsqjlKWakt0-15VGZ2nF4Ek9pih7KvcQn_hNrts_puba87rXqGqZPEhnODyIL7UyDCMIDxLLs2zKQQH4pAD2zBDyCEcK7i9RxRMXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☀️
📈
فقط در کمتر از نیم ساعت، سهامدار ۱۰۶ نیروگاه خورشیدی شوید!
🗓
یکشنبه ۱۵ شهریور
#پذیره‌نویسی
نماد
«نور»
آغاز می‌شود.
💰
فرصتی متفاوت برای سرمایه‌گذاری در صنعت انرژی خورشیدی؛
هم سهمی از نیروگاه‌ها داشته باشید، هم از ظرفیت رشد این بازار استفاده کنید.
⚡️
۱۰۶ نیروگاه خورشیدی
📊
ورود آسان از طریق پذیره‌نویسی
🌱
شش گام تا سرمایه‌گذاری در یکی از جذاب‌ترین حوزه‌های انرژی آینده
⏳
اگر به سرمایه‌گذاری در انرژی‌های تجدیدپذیر علاقه دارید، نماد
#نور
را  زیر نظر داشته باشید.
🔔
این پست را برای کسی بفرستید که دنبال فرصت‌های جدید سرمایه‌گذاری است.
@economy_100</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/460288" target="_blank">📅 16:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460287">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/460287" target="_blank">📅 16:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460286">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0W35PDIUH_bkFNoafvflE7Q45W-8zD9B5wj6VcWb_-QMh_fssgt5__iwvdTJbibuaKjA2dkep_lTYAemv7eAqn_Lf3cWQcR2aCoQz_9tZcAYWX-LWO4zwDBBko1GwwNVPqpCMLuWOLJtbya5CAuOFHYJq1U69czNWD3ZYZSFvb2cpGo7-pPMdOjkqZor6MgHk_Le6SBsKumzpwrA_tK5_qyZ2Had_DdvF-SPU9_Dm5VM2r5gqQa2m-HpO0zAvmCE54DuKnUNGzYiOqWIJ2Hb9hFO1XLmgnJZaV3eTzWnvtG_EO9clkc4vLkX8DGlSFxRTvp34MPf4w-DHbI2gFZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دلار ۲۲۰ هزار تومان شد؟
🔹
دلار در بازار آزاد امروز درحالی از ۲۲۰ هزار تومان فراتر رفت که صبح امروز ۲۱۴ هزار تومان قیمت خورده بود.
🔹
بررسی اطلاعات مرکز مبادله نشان می‌دهد، تقاضای واردکنندگان به‌عنوان اصلی‌ترین تقاضای دلار در ایران کاهش یافته و آن‌ها حاضر…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/460286" target="_blank">📅 16:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460285">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حق‌التدریس معلمان ۲ برابر می‌شود
🔹
سخنگوی آموزش‌وپرورش: از اول مهر حق‌التدریس معلمان شاغل و بازنشسته ۲ برابر می‌شود.
🔹
براساس مصوبۀ سران قوا، امکان ۲۴ ساعت تدریس در هفته برای این افراد وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460285" target="_blank">📅 15:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460284">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3161e7c676.mp4?token=HM-X4gR_9MjcrApVYS8IBI1pa_BBm4qrVVMQrA8cu0nGZIIJhExuDCdopZCtgv1AKteGcjTSGj_HAXzJZeRr3U6kbsgJQQ7OYsT-n3qvnLoPwwlDEbznLN2RQ0TEu1i_wXXn6XtnoUlrFJYqW2Sljmbc0wuzYVd6YC-q6bx4XAicp064GYRBL9V8h8kDh2QdHxyc8wu_igP7j4PU-l-PBdowMMRc8SgnJWfoteNtlWYQAg0OieiiedTS6znXQ6IB4yy40V6smPFlKAvo-aKuiFHFSXAZtMxg63SbmXHT7xxFEs0QUETtOdsmNKCSyoT-EIZ-B7B8kGuCr2EaVgKP0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3161e7c676.mp4?token=HM-X4gR_9MjcrApVYS8IBI1pa_BBm4qrVVMQrA8cu0nGZIIJhExuDCdopZCtgv1AKteGcjTSGj_HAXzJZeRr3U6kbsgJQQ7OYsT-n3qvnLoPwwlDEbznLN2RQ0TEu1i_wXXn6XtnoUlrFJYqW2Sljmbc0wuzYVd6YC-q6bx4XAicp064GYRBL9V8h8kDh2QdHxyc8wu_igP7j4PU-l-PBdowMMRc8SgnJWfoteNtlWYQAg0OieiiedTS6znXQ6IB4yy40V6smPFlKAvo-aKuiFHFSXAZtMxg63SbmXHT7xxFEs0QUETtOdsmNKCSyoT-EIZ-B7B8kGuCr2EaVgKP0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ رئیس ساترا به ۲ شبههٔ مطرح‌شده از سوی وزیر ارشاد
🔹
جدایی وظایف: تولیدات نمایش خانگی وظایف مستقلی دارد و بار اضافه بر صداوسیما به‌ویژه در زمان بحران، محسوب نمی‌شود. هر بخش، از جمله ساترا، استقلال عملیاتی خود را دارد.
🔹
پرهیز از ساده‌انگاری: مسائل فرهنگی…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460284" target="_blank">📅 15:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460283">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15628a403.mp4?token=HZ3oe1p2jauu5F-oc8qBeFfPyVInbLHbw43dzbxSjicDuwWWtZAZ0Hb-N9X-4hA2r7_d1Lxi-26h44yDKUki8Fe48QQqkOCD2lowt2S3dBhwdrjcKs4QPLGGHkjClnPgeX1zK_otx4EKFhHIEKNK7Qhb-oWfzVD9dZpTOG7dGReCa2YJde3kijxR7BRyOrhWnTBOk1mVCHALPW-zd_Hf-BR07_002xAda6FuFvcrNvIPvGAzL5y5H8vVrEiyuVBK3B2MecghD1WDhcj8LnYpW3LtI2n9zoN5qD20ZtHC92Xi51FQTlJZe2oDswR6r9BXb9PdzNOZgXwvdWLDweTpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15628a403.mp4?token=HZ3oe1p2jauu5F-oc8qBeFfPyVInbLHbw43dzbxSjicDuwWWtZAZ0Hb-N9X-4hA2r7_d1Lxi-26h44yDKUki8Fe48QQqkOCD2lowt2S3dBhwdrjcKs4QPLGGHkjClnPgeX1zK_otx4EKFhHIEKNK7Qhb-oWfzVD9dZpTOG7dGReCa2YJde3kijxR7BRyOrhWnTBOk1mVCHALPW-zd_Hf-BR07_002xAda6FuFvcrNvIPvGAzL5y5H8vVrEiyuVBK3B2MecghD1WDhcj8LnYpW3LtI2n9zoN5qD20ZtHC92Xi51FQTlJZe2oDswR6r9BXb9PdzNOZgXwvdWLDweTpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ رئیس ساترا به ۲ شبههٔ مطرح‌شده از سوی وزیر ارشاد
🔹
جدایی وظایف: تولیدات نمایش خانگی وظایف مستقلی دارد و بار اضافه بر صداوسیما به‌ویژه در زمان بحران، محسوب نمی‌شود. هر بخش، از جمله ساترا، استقلال عملیاتی خود را دارد.
🔹
پرهیز از ساده‌انگاری: مسائل فرهنگی و نظارتی نیازمند تحلیل دقیق و موشکافانه است؛ نه کلی‌گویی و ساده‌سازی. اگر با عجله و بدون تعمق قضاوت کنیم، جفا به مردم، فعالان و نظام است.
@Farsnart</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460283" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d134db331.mp4?token=UK26juR5mIMsLtEqfh7X-HOWZn2XmSNeTjox3UE-pQFeG2mSOhbbgsoCBjzo6DX6qke8zkyc05gO2bUmVQZ3qdb52K_aTx11Yal8tdyNQkXTxttG88jqCMJ1a46bf_F7-lMcNLNdqriLOBNtkUQKvULVAaQi9Jdt4PDHPbFgfEtbic4YTv4qFHfbpulxfbW_7aHubwOaTyn5__rlE-teNmQK_ZVuejGfvg94ZzOtN0sZqfJp3AqNaoe67AfyhXJC8N2vM1mu2K-JLn9WLYPdFXBHDVdz2dJwufAE_QmL-iYn_EmP-r-y_MduodommeOfXz3pyaz6rx3ehkH_aP8UUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d134db331.mp4?token=UK26juR5mIMsLtEqfh7X-HOWZn2XmSNeTjox3UE-pQFeG2mSOhbbgsoCBjzo6DX6qke8zkyc05gO2bUmVQZ3qdb52K_aTx11Yal8tdyNQkXTxttG88jqCMJ1a46bf_F7-lMcNLNdqriLOBNtkUQKvULVAaQi9Jdt4PDHPbFgfEtbic4YTv4qFHfbpulxfbW_7aHubwOaTyn5__rlE-teNmQK_ZVuejGfvg94ZzOtN0sZqfJp3AqNaoe67AfyhXJC8N2vM1mu2K-JLn9WLYPdFXBHDVdz2dJwufAE_QmL-iYn_EmP-r-y_MduodommeOfXz3pyaz6rx3ehkH_aP8UUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گشت‌زنی خرس قهوه‌ای و ۲ توله‌اش در منطقهٔ قورخود خراسا‌ن‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/460282" target="_blank">📅 15:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPZ2auXXhQCZF3aH8WbJY3vOoEUgaXLT09vSl9YIPYRD4n-L4DXxOoxirYI-xRE5p8IYyWHJPE4aLES3CSg5NODwr8fIk-S1iwGJLRtMQI3vIvTpnaQtk3ftg60VV4t9tUnc4nszvIz7jvdo27IzIV_kPUdYzFUL_yABkg317uf-vQps-hMy_XIl11mS3plqu1rGIHCSoyKjKI9rFTTQLMe8WHg6WZ2fGnfAHz6NGMIO6ZzfvKPes7hblrNbPS-guJ2MovG_JF6yXB9cnCKcZooDb2agTtvIcAObty-9BoclKEQfEjVAOr9Sk45LJUJEk5BQPF_JTNZDSC5ve04Hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت مرغ کاهش یافت
🔹
براساس گزاش میدانی، هر کیلو مرغ به ۲۷۰ هزار تومان و ران مرغ به ۲۰۰ هزار تومان کاهش یافته است.
🔹
وزارت کشاورزی اعلام کرده نهاده به حد کافی وارد شده و بخشی از آن توزیع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460281" target="_blank">📅 15:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8wSgPSwmoOQ6PLPiJxN7RJXjgyPRSfnA289qMGQX98HypECG79EbuJ-ZZFURv5TbCdOlAIfA2U72n_UmSRz4ca9r6X6mdFdqBQ0Mzw7hE94JOmQuAH4EsLaeCawoCOjq3JQmFl9TZbRbMt6sNYseoZ9ZyNtcQ_kczOcYphqbV7VVnrIbQkyi1-f65CdKDrXiB0VTqjzVn6yWZn1dCAML-BBSMYNpXdMrUqjn0VUiR7U9D0owusaKSZRhybPhZBfefpxgzxKob1ED4C746Bx4lWR8ST5pvFl8FdJNNUfLbY8dGAjkP7bqwLGSMJqzfu1KmrrWLVJeWmhDw8y709cZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460280" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460279">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1dd13a95.mp4?token=M15XvvfeT8CkFTmePcMiSQtfX_6jt0k_f8GA7QTFzkpnyh6_frilFzmZ2VitwTpz30ARt_FYpuomLQ4dIXwBJ87dpIzKvh_wn3LaKnFYv3S6gD3geVC7MqS1SfScTRSiRNLy_1j0Fd0vJbWoGmIISJdk0wQV2AEAfQNRqxu2-AVJRSvPaR0f-Nt6YUq1eUI0AfQHca8JNeYKD9m1-Vdbyo5VkyorTIs-WkjzhvnVL4_Dg6R4Qkt4sxJUepAX3jAXYNETWI_P_12FY7MB6T3seJeJmUUexhJV90nh418gVCsyOhqlcgx_jTaxEC35plT2dD23V2UBvKSPeWUt1tFkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1dd13a95.mp4?token=M15XvvfeT8CkFTmePcMiSQtfX_6jt0k_f8GA7QTFzkpnyh6_frilFzmZ2VitwTpz30ARt_FYpuomLQ4dIXwBJ87dpIzKvh_wn3LaKnFYv3S6gD3geVC7MqS1SfScTRSiRNLy_1j0Fd0vJbWoGmIISJdk0wQV2AEAfQNRqxu2-AVJRSvPaR0f-Nt6YUq1eUI0AfQHca8JNeYKD9m1-Vdbyo5VkyorTIs-WkjzhvnVL4_Dg6R4Qkt4sxJUepAX3jAXYNETWI_P_12FY7MB6T3seJeJmUUexhJV90nh418gVCsyOhqlcgx_jTaxEC35plT2dD23V2UBvKSPeWUt1tFkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف رازهای ۵ هزارسالهٔ جدید در شهر سوخته
🔹
در جدیدترین کاوش‌های باستان‌شناسی در شهر سوختهٔ زابل یک بازی فکری، یک شانهٔ استخوانی نقش‌دار، بازماندهٔ مواد ارگانیک و سفالینه‌های جدید کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460279" target="_blank">📅 15:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460278">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b653dcb2d4.mp4?token=Bcni_mR_33X6LExKVMJZXqQ0izd9vr7mD1k5Zzhc8JQWGRQ0rF9V75zOzj0nWCTNKtp3kBxiWEz2Sui_TUlnirE2Cc6-AV_RS_6WA4m6onGhzHaBzCozrNiWvd6WvP91WkGkGx4NvtrwBxcUt1muh-tgCGeu9wYmWe6EYqVfV5pzvPZ-T46iSdOQWaEgscP1_ErwwvjG50p8ElR3zXZ6cuL5XJ_seJ50V9Ywy-KxL7U3Wzf5gPGs8Scs-W_BGOudxHQj0LWn4Dn2SKREf3TjrtEJ5UdAZS-2PY2XEjDq5Rkjp9LrWZYARUvAp-u4ttLWXwYiVzjqZhbpJmuW8Cn4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b653dcb2d4.mp4?token=Bcni_mR_33X6LExKVMJZXqQ0izd9vr7mD1k5Zzhc8JQWGRQ0rF9V75zOzj0nWCTNKtp3kBxiWEz2Sui_TUlnirE2Cc6-AV_RS_6WA4m6onGhzHaBzCozrNiWvd6WvP91WkGkGx4NvtrwBxcUt1muh-tgCGeu9wYmWe6EYqVfV5pzvPZ-T46iSdOQWaEgscP1_ErwwvjG50p8ElR3zXZ6cuL5XJ_seJ50V9Ywy-KxL7U3Wzf5gPGs8Scs-W_BGOudxHQj0LWn4Dn2SKREf3TjrtEJ5UdAZS-2PY2XEjDq5Rkjp9LrWZYARUvAp-u4ttLWXwYiVzjqZhbpJmuW8Cn4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از دوشنبه دمای هوا کاهش می‌یابد
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460278" target="_blank">📅 14:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460277">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f0a87538.mp4?token=E4w2gXUNAcr8dsAA6k4R2lQbKQ3y5lF49pkyZpu9AAQ7IElX0ALC-y5exmnmQXT7VWoBkAlowKDVqXyKloHYUIwSvPi66Z5rXm9jY0yClGUQUH-MOWSx2_pfaIxpNhgMfWXaObNMApwmaUvwsrVbZTSnP5J-a6iAaWiCXuVfMoFIz8Ef4kk8nExrjI1LcSEMODq78-dyYPJCm107RY9Wusr3v07YB0hsoSbKTQMALMYjibVRkxbZHaQUzOon84FPm6R-gxo4t3fHv1jNE7Uurx9O2WXhW3on6LqAjd9fE27mQ9Q46BgZMXrl-jXm99tkUQG6uAbemkO6jBu2ElRY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f0a87538.mp4?token=E4w2gXUNAcr8dsAA6k4R2lQbKQ3y5lF49pkyZpu9AAQ7IElX0ALC-y5exmnmQXT7VWoBkAlowKDVqXyKloHYUIwSvPi66Z5rXm9jY0yClGUQUH-MOWSx2_pfaIxpNhgMfWXaObNMApwmaUvwsrVbZTSnP5J-a6iAaWiCXuVfMoFIz8Ef4kk8nExrjI1LcSEMODq78-dyYPJCm107RY9Wusr3v07YB0hsoSbKTQMALMYjibVRkxbZHaQUzOon84FPm6R-gxo4t3fHv1jNE7Uurx9O2WXhW3on6LqAjd9fE27mQ9Q46BgZMXrl-jXm99tkUQG6uAbemkO6jBu2ElRY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی گاز: شدت مصرف انرژی در ایران از همهٔ کشورها بالاتر است
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460277" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460276">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f302008996.mp4?token=BiFVazWIKyTKJeEoofRP0CwTh7ePUqpOHUT-3Jua50RemF-X8m_En9Mn7BwJ2FaZgr-kwQAv0lMYFr4aCMlTAyZ9cVFzEYwuyRiKo3hEwqG7PPfoaZ4u-30xT6ghZckFNrWSDWSuOqlWkt_6agWoeQneYvZbtxF5pE_ZKha_pPCzvEe6tIpPaSyUIC5kqkgnvT0Nhf1nXZIOObq8itD1FWCQFjdbbbx6DAFhQkJvxB3YTmPiUArs3AmotrLFf1pcHFztN9S5ItDKOppj0-8nQ5lZXA3bF68c9V2eVgXr_8Jsp8wwy2CaiRKGC2KOj5_Hm-6eFgCb8AJmecOdOpBxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f302008996.mp4?token=BiFVazWIKyTKJeEoofRP0CwTh7ePUqpOHUT-3Jua50RemF-X8m_En9Mn7BwJ2FaZgr-kwQAv0lMYFr4aCMlTAyZ9cVFzEYwuyRiKo3hEwqG7PPfoaZ4u-30xT6ghZckFNrWSDWSuOqlWkt_6agWoeQneYvZbtxF5pE_ZKha_pPCzvEe6tIpPaSyUIC5kqkgnvT0Nhf1nXZIOObq8itD1FWCQFjdbbbx6DAFhQkJvxB3YTmPiUArs3AmotrLFf1pcHFztN9S5ItDKOppj0-8nQ5lZXA3bF68c9V2eVgXr_8Jsp8wwy2CaiRKGC2KOj5_Hm-6eFgCb8AJmecOdOpBxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صنعت کفش با صدای زنگ مدارس رونق گرفت
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460276" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkFng0ORrwS5jXFp__WJLPnPe2BinabS0SSYqlDGoeVV2r2VISOz8kTN5FBulWIDVzxsAKeGKZny-5ClM2W5m2ZdwOGwZtic4Gohktx0QCS9jIBNH8skV2xEC29T0s2tZiAGwakJVs0tEAl61Xv68QcVq1T327FfSnFNYWL4Blc32JrU7c_3a7fUD8fKROiP_ZLYzcr2KgVU6BivlPmrUNEryM-6h1Z8Io8tuBqjDQbJZyZBv-1S1jcAC25QHk9--mfiy_QGOajNlGk8HLUp5AqAxymEnn9aJT889UUeFCcm4qcEKh86VhAmn1jFzDnqJfT3x8vkvSDU5PhRpFY9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد فروش محصول در هلدینگ خلیج‌فارس شکست
🔹
در شرایطی که سال گذشته کشور درگیر دو جنگ تحمیلی بود و صنعت پتروشیمی از این جنگ آسیب دید، بر اساس صورت مالی منتشر شده «فارس» در کدال، گروه صنایع پتروشیمی خلیج‌فارس توانست برای اولین‌بار میزان فروش محصول خود را به رقم بی‌سابقه ۹۳۱ هزار  و ۴۶۳ میلیارد تومان برساند.
🔹
این میزان فروش، حاکی از افزایش ۵۶.۴ درصد میزان فروش در سالی است که حدود دو ماه از آن صنعت پتروشیمی کاملاً متاثر از شرایط جنگی بود.
🔹
نکته قابل توجه این است که این افزایش فقط شامل رشد ریالی و دلاری فروش نبوده و تولید نیز علی‌رغم تمام مشکلات ناشی از جنگ در این گروه در سال ۱۴۰۴ نسبت به سال ۱۴۰۳، رشد داشت.</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/460275" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460274">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duy1mMrC9WsCoAEPFehv62m-QQ6xSgiH-18MNHCVQz7W91mVDeEyrIhYs5s9jeUp9EGjvpjmyz5QcAfN0yZRLNG0lxi1p8djnOvMIo5GdeJw_2ftpFJrXQk3FVVQkdqVhbGW8giwBzcZLTN3TMbdj3wEd8_sDp43CdrRPUEqNwaFrMBT2rRuDiqUKUE0i2GZOpKFHCWJQjIfLTLgwDLzg82SU3_KbXpicqoUA7kdr7OZQXmmFTk3PgLQphf47z3iSha7irkISoszr_bmD0q5X5Q3tfSkgXnRqUxAQwvGgN6G7HQI9Im0_BMd3nDYGcsLQGidRBQqq7o0mVHVlIqPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
آدرس جدید دسترسی به سایت و پیشخوان مجازی بانک مهر ایران
🔹
آدرس‌های جدید سامانه‌های بانک قرض‌الحسنه مهر ایران به شرح زیر اعلام می‌شود:
🌐
سایت بانک مهر ایران
qmb724.ir
🌐
پیشخوان مجازی (مهر من)
my.qmb724.ir
🌐
چت بات
qbot.qmb724.ir
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/460274" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460273">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/460273" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460272">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc3n_A3ra5eaYd2kbTR_8UBMRGgiNcc-_MIZiAhYg3dc5TJWhVYOp__0-JdbjOLDwpZkoLzvy9pTzS2D51rAYeZPrfFHtwbDoP5naETVkio6MzfBcklCj48stknfZ1jtKk0r3vXqTQpbFTFioewMBntHQ4YhJNF2tvk-97SLX5nl6bjJm1Ezkifo9MEfuNNVDlJU5Xp1Ym6jVGhqxaJjdotslE6QTbbsJdxFlXOEqbQZ2XzO4F8Xsin06QGPL_48UCC0XoXvTq6OeKVgGSGEpjCw_GW8dGhKz9bFAMZpdp7sKp-Xdu-AcrVpxxxIYGa9UdTql9j1DNqsfpazUSsgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم سنگین فدراسیون فوتبال علیه قایدی
🔹
با رأی کمیتۀ وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش، مهدی قایدی به پرداخت ۱۸۰ هزار دلار بابت اصل خواسته و حدود ۵۵۰ میلیون تومان بابت هزینۀ دادرسی محکوم شد.
🔸
نیکومنش مدیربرنامۀ سابق قایدی است که گفته می‌شود واسطۀ انتقال او به شباب الاهلی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460272" target="_blank">📅 14:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460271">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da34dd991f.mp4?token=lQnAlGGgYxDT3AIqmE-lZQJnmRA-cVQwckInuh8A1mUPVGZPyOwCYPAvt0qjP74nQjin15LOblCjCbqsKsRjDdXBvnM5e5xtiRz7ryFAEN7Us-HldVjeAODmUVLcNGI8r1Dyj5slF4OoQhAd_0NaDJ7tlxv9vmOtCuNNJ_DnW8Lvgf_LqEGd6LSbGHToS8WCcSEn1O5Vwx22N9vlQ1zNmoUylAQG8pjMadveMN87UM5eKiCTmOeLI5uKlbhXhheDGYxmCeKFaCKdMy3MVPT4XeukXEgA4zBpZ-pfxGsSTeET63FxOkbDhnMBJY8U9a_Yt2sqRh6IDXU36oYgpG91kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da34dd991f.mp4?token=lQnAlGGgYxDT3AIqmE-lZQJnmRA-cVQwckInuh8A1mUPVGZPyOwCYPAvt0qjP74nQjin15LOblCjCbqsKsRjDdXBvnM5e5xtiRz7ryFAEN7Us-HldVjeAODmUVLcNGI8r1Dyj5slF4OoQhAd_0NaDJ7tlxv9vmOtCuNNJ_DnW8Lvgf_LqEGd6LSbGHToS8WCcSEn1O5Vwx22N9vlQ1zNmoUylAQG8pjMadveMN87UM5eKiCTmOeLI5uKlbhXhheDGYxmCeKFaCKdMy3MVPT4XeukXEgA4zBpZ-pfxGsSTeET63FxOkbDhnMBJY8U9a_Yt2sqRh6IDXU36oYgpG91kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک جنگ و ۲ شکست ثمرهٔ ترامپ در تقابل با ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460271" target="_blank">📅 14:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f08242582.mp4?token=unDHFTRI_WrkwBh9qKG4Z2I8h0EuMqE8KFvMMpiPmUMFwnRlFcnUODDBjkA-Grlu38_Mgbpggi2mq_bV7uqD77Z7MryyXW8VbGwm4u5Ikm58lqnnmZAaZKg7z8EUolUcF8aYdwE2SeDG28vKeEU2ZcPOijdY4SXtcHAP1v0GnWXW5aqAt340FUlWbolya1Am2OBcXUYwfM04EXlZfiCTfNjXayF0h1lA4HM0w3PH28Qa3ZTltx2Z4x_iHLARRUdGkXXCK5vOZW_XKjy0OD8yJ4hJegaamuJDFZFZIslVS_qVX52diCnwP2Kn5S87pQHB8e1kPDUK2U8CE5b5aq-O0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f08242582.mp4?token=unDHFTRI_WrkwBh9qKG4Z2I8h0EuMqE8KFvMMpiPmUMFwnRlFcnUODDBjkA-Grlu38_Mgbpggi2mq_bV7uqD77Z7MryyXW8VbGwm4u5Ikm58lqnnmZAaZKg7z8EUolUcF8aYdwE2SeDG28vKeEU2ZcPOijdY4SXtcHAP1v0GnWXW5aqAt340FUlWbolya1Am2OBcXUYwfM04EXlZfiCTfNjXayF0h1lA4HM0w3PH28Qa3ZTltx2Z4x_iHLARRUdGkXXCK5vOZW_XKjy0OD8yJ4hJegaamuJDFZFZIslVS_qVX52diCnwP2Kn5S87pQHB8e1kPDUK2U8CE5b5aq-O0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از گشت‌وگذار آهوهای میاندشت که قبلاً ندیده‌اید
🔹
روزی رسیدن جمعیت آهوهای میاندشت به ۲۰۰ رأس آرزوی محیط‌بانان بود، اما حالا بیش از ۳ هزار آهو در این پناهگاه زندگی می‌کنند.
🔸
پناهگاه حیات‌وحش میاندشت جاجرم در خراسان‌شمالی ۸۵ تا ۹۰ هزار هکتار وسعت دارد و بخش مهمی از حیات‌وحش آن را آهو تشکیل می‌دهد.
این ویدیوها در ۲۱ مرداد امسال ثبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460264" target="_blank">📅 14:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460263">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e70915585.mp4?token=b1G7oRG8mVMFcOKHCGykm4pQ0CZV_7hbSwAo0jUmg8xYa4Fr0JD9-U6m3TMtZwZmH94MUvvItEO9bQlx4Ch8bYKZRiI41nWt4JsGo8jqWS4aEG3MYsCXiBx1MNsy-Al6AzyEP0kZgTHe53oO7IFVWmbdGZQU3MhfXMUCtjT1hhJtVQGNEo5K4oD2PXJ76jlSGgFetnf_vQA085tFTYCHrlfgg_cm-nI3e1lr7a7VsRsfHzbpB_arHZXH3WZe74v1cPewoS4VdjGPp1att07G6mknzsrK9YvTQNFqnpuBN6-6dABeiQy1du8D4kAbQuyGKyHkNDHplp3fwnwWCkhgy62BWpwGpq2MW9StTfTfQaaJIMnQnQjHsSuEi7g5UaWR7hcUC6YRRHnjjBABqi72KKia-3q9x_5xGP_vwmasEfnqEGhqtHuA65SqJu-ZC5GM58OdA_C8wmdmVnJNSHExe9mpJKjD7BIi8B8beC4NuCIOKmn3qrKlB58n093iDE_h7XLdXdiZbLpKo1HT_sTB8LLNloJGQ1jVC8PmHc-PrsbY48jrAyTs-h9oKAc7C7BHEoUsal6fY74u-oau287gP5sPjH2lF-kPiBEWrmtL2KakwQhfNRfZWAM2ZsMs62lG4b3BgeujMFnA6satCwFEL3FsrI-cAolmXLDmFKdBydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e70915585.mp4?token=b1G7oRG8mVMFcOKHCGykm4pQ0CZV_7hbSwAo0jUmg8xYa4Fr0JD9-U6m3TMtZwZmH94MUvvItEO9bQlx4Ch8bYKZRiI41nWt4JsGo8jqWS4aEG3MYsCXiBx1MNsy-Al6AzyEP0kZgTHe53oO7IFVWmbdGZQU3MhfXMUCtjT1hhJtVQGNEo5K4oD2PXJ76jlSGgFetnf_vQA085tFTYCHrlfgg_cm-nI3e1lr7a7VsRsfHzbpB_arHZXH3WZe74v1cPewoS4VdjGPp1att07G6mknzsrK9YvTQNFqnpuBN6-6dABeiQy1du8D4kAbQuyGKyHkNDHplp3fwnwWCkhgy62BWpwGpq2MW9StTfTfQaaJIMnQnQjHsSuEi7g5UaWR7hcUC6YRRHnjjBABqi72KKia-3q9x_5xGP_vwmasEfnqEGhqtHuA65SqJu-ZC5GM58OdA_C8wmdmVnJNSHExe9mpJKjD7BIi8B8beC4NuCIOKmn3qrKlB58n093iDE_h7XLdXdiZbLpKo1HT_sTB8LLNloJGQ1jVC8PmHc-PrsbY48jrAyTs-h9oKAc7C7BHEoUsal6fY74u-oau287gP5sPjH2lF-kPiBEWrmtL2KakwQhfNRfZWAM2ZsMs62lG4b3BgeujMFnA6satCwFEL3FsrI-cAolmXLDmFKdBydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی که امروز با ایستادگی این ملت به عزتمندی در جهان شهره شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/460263" target="_blank">📅 14:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460262">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8-iUYZysNzOKqTcqi7g60x3cBQxK59ZaK9-GLuXxGvRC1V0FTycmagACIn5m0WilacV2e8jq6Q6f8cp6Au7FKAzEwd66w232yffdUvBKDdVWmFlmMYRRWQdWvsfHwwsT6h3H_yZkfsVyB1-vlNzzMXlVnIpGK44WMSWPxtTeJX9zWflt4vAcocpMROOhp0EY7MOXqb9J9cZ-YhYzk3Kx7U5PNSwKXIil71a1SCMt0TNwL--Atnzskx2ON-pAHYGRgJXVmSyRoo2WyAC5y1eDMcH_ypZndDJ1KQQHtEIQt7gpMpn8yZG8pS_KuqSxZscwOtJQpr7JumL23mlcWefNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، صالح را نمی‌خواهد
کاپیتان استقلال از برنامه‌های سهراب خارج شد
🔹
‼️
بر اساس آخرين پیگیری‌ها، سرمربی استقلال درباره صالح حردانی از موضع خود کوتاه نیامده به نظر می‌رسد قید حضور حردانی در جمع شاگردانش را زده است.
⏺
سریالی از بی‌انضباطی‌های حردانی باعث شده تا در نهایت بختیاری‌زاده تصمیم به اخراج بازیکن ملی‌پوش خود بگیرد. از نظر سرمربی تیم، کاپیتان دوم آبی‌ها بعد از بازگشت از جام جهانی منزلت پیراهن استقلال را از یاد برده و دیگر بی‌انضباطی‌های او از سوی کادر فنی قابل‌تحمل نبوده.
⏺
حضورنیافتن در تمرین، نوع رفتار در مواجهه با دیگر اعضای تیم و تلاش برای دخالت‌های غیرمتعارف باعث شده تا بعد از ماجرای ضربه کاشته دقایق پایانی دربی، سهراب نام صالح حردانی را از لیست تیمش قلم بگیرد.
⏺
با این اوصاف صالح فعلاً به طور کامل از برنامه‌های فنی بختیاری‌زاده خارج شده و سرمربی استقلال معتقد است تا زمانی که او روی نیمکت تیم بنشیند، حردانی اجازه بازگشت به جمع آبی‌پوشان را ندارد و تا این لحظه هم از موضع خود عقب‌نشینی نکرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460262" target="_blank">📅 14:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460261">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bbc47942.mp4?token=TFgvquIrSQvhj1zU_MYzENfk1-mq4Ypf9JXOceYIsiiGKi8FIMQqzbnPl5GyNtoL2qWvhMMi_RHRUFZYf_eUo-AOCtZEOiuBXSr4JT2q4At-Wo3WlryaLASp4xIB14DXM79KZKYPXaTTdcQ2Qa6LFVMKRT5H0RbGQ-lX5hB1xYIAT9xrUilCUrea280Qivlu6GKBO8Y1ErqwW-plBtpd_BNJ55q_9TX6jCL3PriZOvwB4vlJNPYO5yDAp5ldiRjg5kxs4REAOex4pZ6l279YJ9MrXE_xOal4T-M6C7ifed0CwZ18Kx3_kOJinJN-7KwxJhllf8pLf5yxH8IMYqSQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bbc47942.mp4?token=TFgvquIrSQvhj1zU_MYzENfk1-mq4Ypf9JXOceYIsiiGKi8FIMQqzbnPl5GyNtoL2qWvhMMi_RHRUFZYf_eUo-AOCtZEOiuBXSr4JT2q4At-Wo3WlryaLASp4xIB14DXM79KZKYPXaTTdcQ2Qa6LFVMKRT5H0RbGQ-lX5hB1xYIAT9xrUilCUrea280Qivlu6GKBO8Y1ErqwW-plBtpd_BNJ55q_9TX6jCL3PriZOvwB4vlJNPYO5yDAp5ldiRjg5kxs4REAOex4pZ6l279YJ9MrXE_xOal4T-M6C7ifed0CwZ18Kx3_kOJinJN-7KwxJhllf8pLf5yxH8IMYqSQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نباید از کسی عقب بمانیم
🔹
ان‌شاءالله خدا کمک کند تا راه حضرت ابراهیم را برویم و بت‌شکن باشیم.
🔹
یاد نگرفتیم با هم‌فکری به یکدیگر کمک کنیم، یاد گرفتیم دستور بدهیم و دیگران اطاعت کنند؛ اینجاست که کار خراب می‌شود.
🔹
وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم. ما نتوانستیم آنها را درست آموزش بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460261" target="_blank">📅 13:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460260">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هلاکت ۲ تروریست در سیستان‌وبلوچستان
🔹
نیروی زمینی سپاه: یک تیم تروریستی وابسته به آمریکا و رژیم صهیونی که قصد انجام اقداماتی بر روی اهداف از پیش تعیین‌شده در سیستان‌وبلوچستان داشتند، مورد ضربهٔ قاطع قرار گرفتند که منجربه هلاکت ۲ نفر از آنها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460260" target="_blank">📅 13:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460259">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade139bc91.mp4?token=WSTgc4OIRzSuR5oBQFzSRqoEQeY0RdC2PeaURa9cv-1NnbxzW_9wICpGhK8-y3mVkU3mcxW5MQARZ04muFrP1y6tc9upjy2CpLg835TdI-YnBVW15j0rzF_c0e1NvEjg9lmSsiabBl3sHVyoBmfx-rcl6qsHboXb0qKVH9I2hD0Q33cZeTa9arzRiICJrmqhY29OdVKEgTC8eouaoQJukaPQcfRpth_vXArWUetKyYOLQ-SgyFNKqhBR4fVUwDWwH5ww9TAlOuxTMD0Y5YatWeHBzfuCJKX3wpE7RnDXqoeRFcBnq31dGw2kpfBUXCNLQyixc8n-1Ani6x5FegXSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade139bc91.mp4?token=WSTgc4OIRzSuR5oBQFzSRqoEQeY0RdC2PeaURa9cv-1NnbxzW_9wICpGhK8-y3mVkU3mcxW5MQARZ04muFrP1y6tc9upjy2CpLg835TdI-YnBVW15j0rzF_c0e1NvEjg9lmSsiabBl3sHVyoBmfx-rcl6qsHboXb0qKVH9I2hD0Q33cZeTa9arzRiICJrmqhY29OdVKEgTC8eouaoQJukaPQcfRpth_vXArWUetKyYOLQ-SgyFNKqhBR4fVUwDWwH5ww9TAlOuxTMD0Y5YatWeHBzfuCJKX3wpE7RnDXqoeRFcBnq31dGw2kpfBUXCNLQyixc8n-1Ani6x5FegXSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلار ۲۲۰ هزار تومانی از کجا آب می‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460259" target="_blank">📅 13:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460258">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXtlMQCtPoW9ppjKLa2nxd_9VNqFgoGe7k2yBbNzIHHCrMce4G2-efDds8MwpP07ga2Xgt0Ty3jwzFHx23IGvYiGB2ZK7oK1_HCO-vUAUtvl5m_kGCM58Fm1d2gJMtfCLQ_yF-DitF9xqt5ifYE2vWEB3maus7ksOmkqoGYMpV5NG4KljPbRaFZW5NtJRw27L-UprDw6qsXj83EQELfzjLTFq5J2UdwuoW0T-rAqUhA7BPKi6KrFtOKTCAxbhZO9F28xqTmFR9XJ2FJNbASvedXXXSXBzyTcHOrTGJ1kGkwCXu3swfTf8y40KN8nONp5LDIZONJ1oJOfprlUpkJMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول بازار سرمایه، رکوردها را جابجا کرد/ سود خالص «فارس» به بیش از ۱۸۷ هزار میلیارد تومان رسید
انتشار صورت‌های مالی هلدینگ خلیج فارس نشان می‌دهد که این شرکت در ۱۲ ماه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به تحقق سود بیش از ۱۸۷ هزار میلیاد تومانی شده است.
این رقم نشان دهنده جهش ۴۸ درصدی سود خالص «فارس» نسبت به مدت مشابه سال گذشته است. همین موضوع سبب شده تا سود خالص هر سهم این شرکت در دوره مدیرعاملی شریعتمداری از ۱.۰۲۰ ریال در دوره مشابه سال گذشته به ۱.۵۱۰ ریال برسد.
هلدینگ خلیج فارس همچنین موفق به ثبت درآمد عملیاتی بالغ بر ۱۱۲.۲ همت شده است.
این عملکرد درخشان فارس در سالی رقم خورد که کشور با ۲ جنگ تحمیلی مواجه شد و تعدادی از شرکت‌های تابعه هلدینگ خلیج فارس مورد هجوم و اصابت پرتابه‌های دشمن آمریکایی-صهیونی قرار گرفت.
عملکرد مدیرعامل، مدیران و کارکنان «فارس» در میانه ۲ جنگ و روزهای جنگی منجر به رشد ۱۸ درصدی درآمدهای حاصل از سود سهام شرکت‌های زیرمجموعه «فارس» شد و این درآمد به ۷۵.۴ هزار میلیارد تومان رسید.
این صورت‌های مالی نشان می‌دهد که رشد سود «فارس» متکی بر درآمدهای سرمایه‌گذاری این غول بازار سرمایه است.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460258" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX_nh6ch3cqkiPwIxkP-NBU8k_NZQzfT56XX5laCC1WhPrjfQFm642Vd0rJVyWoM44aHnHWmXqEs91mTyIQYmWka8c4hMSGp0Qid3iyc1BYkMHBvYkKO7th-TvDhNkL1apfo9jEOr7EXu_w1K7Zq9Oakqdjp7oJAnE4BLOIMkXsAlI-__XwiEMjAV-N_agGPWSOlo1dcp4H68F_EcPo9vS3wtbipjHUDrEVLqpBIVk_lhGH99oQdNJz9T3Mt6sjSDOG7cIRlbq79FzKyluafiMXLq3ZEYX81WPOy_a1G5ERt-NUEV0BkwEpGt5hb0jSWeuXKg-UOJOAYf8-9xzOeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
خرید ۳۳هزار میلیارد ریالی شرکت ملی مس از تامین‌کنندگان بومی؛
🔰
تأمین اقلام و تجهیزات مس ایران از استان کرمان ۱۳۱درصد افزایش یافت
🔻
ارزش تأمین اقلام و تجهیزات مورد نیاز شرکت ملی صنایع مس ایران از تأمین‌کنندگان بومی استان کرمان در پنج‌ماهه نخست سال ۱۴۰۵ با رشد ۱۳۱درصدی نسبت به مدت مشابه سال گذشته، به بیش از ۳۳هزار میلیارد ریال رسید.
🔹
براساس گزارش مقایسه‌ای شرکت خدمات بازرگانی معادن و فلزات غیرآهنی ایران، ارزش خرید اقلام و تجهیزات مورد نیاز شرکت ملی مس از تأمین‌کنندگان استان کرمان در پنج‌ماهه نخست امسال به ۳۳هزار و ۱۹۹ میلیارد ریال رسید؛ این رقم در مدت مشابه سال گذشته ۱۴هزار و ۴۰۳ میلیارد ریال بود.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Tb
@mespress_ir</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460257" target="_blank">📅 13:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/460256" target="_blank">📅 13:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a0985eb1.mp4?token=C0xRsJr1akAxyD5PPPEniAD-xkffXz3ejYNrxAOfFIAhy78BSjUY7VR7Uae69pChlU6JdgXAGcBTTSj-TY_W-xMyIe3hFhHljHfz7akY8fgzr2f3dBYVWzoWTDSHrcgZY5RIkau1aIoRKs7rVeHmpGGv8pHDQXAlffUXDJS8_Ke4BNb1Rba0h-Nb5b67P46ovMO4Dn-C6UEwHNE-V32cWmY6Ty2B27WRWQ_8nAninFqwT8LnE1w2WY-hTFIEg3RDP-mNGlAQnPH9k2wPvyEXtNa2M_2ZGslt3RyBWgJNkiPZplRFEJl71gr7o07uKbhIwWbp2ppz7mqPlurMm61NgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a0985eb1.mp4?token=C0xRsJr1akAxyD5PPPEniAD-xkffXz3ejYNrxAOfFIAhy78BSjUY7VR7Uae69pChlU6JdgXAGcBTTSj-TY_W-xMyIe3hFhHljHfz7akY8fgzr2f3dBYVWzoWTDSHrcgZY5RIkau1aIoRKs7rVeHmpGGv8pHDQXAlffUXDJS8_Ke4BNb1Rba0h-Nb5b67P46ovMO4Dn-C6UEwHNE-V32cWmY6Ty2B27WRWQ_8nAninFqwT8LnE1w2WY-hTFIEg3RDP-mNGlAQnPH9k2wPvyEXtNa2M_2ZGslt3RyBWgJNkiPZplRFEJl71gr7o07uKbhIwWbp2ppz7mqPlurMm61NgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: امروز ممکن است این صدا، صدای ایران باشد؛ اما فردا ممکن است صدای هر یک از کشور‌های حاضر در این سالن باشد
🔹
در سال‌های گذشته افغانستان، عراق و اخیراً ونزوئلا مورد تجاوز نظامی جنایتکارانه و غیرقانونی آمریکا قرار گرفتند و هزاران نفر از مردم غیرنظامی…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460255" target="_blank">📅 12:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31bbe4143.mp4?token=IE9drkvIVRq2FsC92Nx2t3lP2_ZCbJkDa9Wtz5TW9qAS0nkt0Fad6sVaGM4zdVxfcZHOGpfHW75JStEXjokMyMa-gpO5QwLLD8SGRDtUMZch3aLUKCkgsBvw8ngfdB4Idc9QA-kBPOn-xqS_BR509Sn4JFFEwJIYEGZ8O0tHa9sihApcWzotVkoxsYNkv_7eTByDSlCbasAiSQ-miNjmWntyo8tajuEh4JAA6Mk6Oisn8eqgxCJqVhXcE5Nkr1AyKuatJrVI0mFInOghz4nOQDTY4Ted1nH8TpbO8cf0ROc6qUx3RimXHIguu4kQyWkBtfwm-tzl7vjBdL-7Hgqd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31bbe4143.mp4?token=IE9drkvIVRq2FsC92Nx2t3lP2_ZCbJkDa9Wtz5TW9qAS0nkt0Fad6sVaGM4zdVxfcZHOGpfHW75JStEXjokMyMa-gpO5QwLLD8SGRDtUMZch3aLUKCkgsBvw8ngfdB4Idc9QA-kBPOn-xqS_BR509Sn4JFFEwJIYEGZ8O0tHa9sihApcWzotVkoxsYNkv_7eTByDSlCbasAiSQ-miNjmWntyo8tajuEh4JAA6Mk6Oisn8eqgxCJqVhXcE5Nkr1AyKuatJrVI0mFInOghz4nOQDTY4Ted1nH8TpbO8cf0ROc6qUx3RimXHIguu4kQyWkBtfwm-tzl7vjBdL-7Hgqd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: اقدام آمریکا و رژیم اشغالگر قدس علیه ایران مصداق بارز جنایات جنگی است؛ اما متأسفانه شاهد بی‌اعتنایی سازمان‌های بین‌المللی به این جنایات هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460254" target="_blank">📅 12:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlbWrbuzokGJpwYB5DKgiPR7VEdskqTEo_QhQ3Atev4vjOfKSnJCxvJFJr5dQb5VzGVYkAjH9bzOnrwHF4LbJbWSr6YkqDAEHsCArZhTzMCwQ0Bxd2v2lBk5qzSdPaXU6Wb76q5FjZg6x54mwOA0--rRsHK67TUEP0BFjHwcHjrOyWtuZAf2SekuwkyUeu2EARbvtqcaDyF6UPnveu0PBsmgGcbnPvdhJqkt_rKMpJHqdlDGgaKKv43GpgdfgQOPp5EB_9CdmVZM4S3Q0I35q6tWCxw7zjxj0jFfBXpGlLcsTVJOOPz2vXXdUVri7x7oX7IZFheYuSb2j773R4YpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به ۶ میلیون و ۶۰۰ هزار برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۷ هزار واحدی به ۶ میلیون و ۶۰۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/460253" target="_blank">📅 12:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460252">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=iFTPFsOWfE5VPGNnDP3UpMQ8_iVlB9N0eaQKZs0fB4BINxg5b9S_9cExHCmSPqCd0uCgYFxuVjfxcFH928t-IVPqeu3HExRWSuDAC6LyJarqfy3rlxPZ2y0ydOxpYYkJNFnG1cxNG0O_xLDPxaBH-zmXRwkPShKQk9H9UTTxsHkC53kl_OudlUIBMMrinPbf0i31diY5LXHCrqouzrIB4qRumOjX2-NrOGHYRsjBWkVg3VmOWDuxCDSzx3GV0HlZEwmkf2dU6TnXkCi8-tdPCLcNaWwFthcnNy5EbcYG4u22f-CNX_Hy5WQX8N1VtzQMUgySIFmvmGIJ9LkuPsW4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=iFTPFsOWfE5VPGNnDP3UpMQ8_iVlB9N0eaQKZs0fB4BINxg5b9S_9cExHCmSPqCd0uCgYFxuVjfxcFH928t-IVPqeu3HExRWSuDAC6LyJarqfy3rlxPZ2y0ydOxpYYkJNFnG1cxNG0O_xLDPxaBH-zmXRwkPShKQk9H9UTTxsHkC53kl_OudlUIBMMrinPbf0i31diY5LXHCrqouzrIB4qRumOjX2-NrOGHYRsjBWkVg3VmOWDuxCDSzx3GV0HlZEwmkf2dU6TnXkCi8-tdPCLcNaWwFthcnNy5EbcYG4u22f-CNX_Hy5WQX8N1VtzQMUgySIFmvmGIJ9LkuPsW4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: نظام‌های قضایی نباید نسبت به نقض حقوق بنیادین انسان‌ها، کشتار غیرنظامیان، آوارگی اجباری ملت‌ها، خسارات وارده به زیرساخت‌ها و بی‌کیفرمانی عاملان جنایات بین‌المللی بی‌تفاوت باشند.  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/460252" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f55e58a6d.mp4?token=RhUBXg4yrfdysPzBufVMtzepNwhxvUV3kF6cnGRzty9nlxdoVfEzIn1bLLGZeAcRSjoKvwvpk7uatkYg9NnFeqrqIOrpb5hGsqXDwwebWLUPp04fFVvD3BZ3pPeBCtWtoORdZPoLoYoLqDrYu81s8S9a8RQ2Nxd7hxBNCiHIYMuIrywjFx6LYNapLy4IF4SRbcOxJJgeDwyAF-TkcK1DCxoQ6fCDJO_2H33xvKbV3DIHvSNTQbJj6zFMnYUiiQwuyvX6AFxKzYBEPHXLorpsoC0ii4oeKywz6Dzw4BzXYgd6Lvh9H4Ib-R2feMLumCEGmJCJKkxukqB7rjIOyZly5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f55e58a6d.mp4?token=RhUBXg4yrfdysPzBufVMtzepNwhxvUV3kF6cnGRzty9nlxdoVfEzIn1bLLGZeAcRSjoKvwvpk7uatkYg9NnFeqrqIOrpb5hGsqXDwwebWLUPp04fFVvD3BZ3pPeBCtWtoORdZPoLoYoLqDrYu81s8S9a8RQ2Nxd7hxBNCiHIYMuIrywjFx6LYNapLy4IF4SRbcOxJJgeDwyAF-TkcK1DCxoQ6fCDJO_2H33xvKbV3DIHvSNTQbJj6zFMnYUiiQwuyvX6AFxKzYBEPHXLorpsoC0ii4oeKywz6Dzw4BzXYgd6Lvh9H4Ib-R2feMLumCEGmJCJKkxukqB7rjIOyZly5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستادگان ترامپ عازم مسکو و کی‌یف می‌شوند
🔹
استیو ویتکاف و جرد کوشنر در حالی قرار است فردا و پس‌فردا ابتدا به مسکو و سپس به کی‌یف سفر کنند که واشنگتن مدعی است برای ازسرگیری مذاکرات ۳ ‌جانبه میان روسیه، اوکراین و آمریکا تلاش می‌کند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/460251" target="_blank">📅 12:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460250">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b9829fb4.mp4?token=G0CI6-F3jmTGVt11zPr28I41WUOpss6PmkTG4Bq0DIwHvSbNpvNaFXEYXXm9JsbO0T7LSToqICtSWbdCdQYtGN2dc5NcrHm7a2zkWKAOF6IuPs4q1eM6AxJYFoNLx-4GnTmWrU_mYnukenBzb8mup-Nh-RQpN_QnapTw8nU30NBkkavQaET5NICyehhXIzWOYEteZNSiL6q3g2MUihqr0nwN_HO-2sVg8xaBIjSuHIdQEmFGsty1dOAF3AADkmr0XMNWeI62B5m6uTm2hkahfLtuZQdj_vLxYHfje1vVGm_zDAe-PU60Ys1KeVQNbtPKq8CUay1DDnzORk1_TZqrmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b9829fb4.mp4?token=G0CI6-F3jmTGVt11zPr28I41WUOpss6PmkTG4Bq0DIwHvSbNpvNaFXEYXXm9JsbO0T7LSToqICtSWbdCdQYtGN2dc5NcrHm7a2zkWKAOF6IuPs4q1eM6AxJYFoNLx-4GnTmWrU_mYnukenBzb8mup-Nh-RQpN_QnapTw8nU30NBkkavQaET5NICyehhXIzWOYEteZNSiL6q3g2MUihqr0nwN_HO-2sVg8xaBIjSuHIdQEmFGsty1dOAF3AADkmr0XMNWeI62B5m6uTm2hkahfLtuZQdj_vLxYHfje1vVGm_zDAe-PU60Ys1KeVQNbtPKq8CUay1DDnzORk1_TZqrmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بریکس نقش فزاینده‌ای در شکل‌دهی به نظم نوین جهانی دارد؛ ما خواهان نظمی هستیم که در آن هیچ قدرتی خود را فراتر از قانون نداند.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460250" target="_blank">📅 12:31 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
