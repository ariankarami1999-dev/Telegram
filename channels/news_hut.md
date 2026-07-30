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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/et-fccib55eslOMEVbD73D4-Z8-sk9HrN5QGPetS7Sgacck-K3VwY6xkQ4lXJNzoExH52T5rHRbhh0mnE3vGyhW3Pt0FaH8yHOfxyVaEgq_VOvOLhmjOt6G7qEzOHgwdMTjGpB4c2IcbH8UWVSLIHGwkeLQap8pFooiPvB0HEsN8VPfmIJ2ek3gsvL_Cvpqw2uIHLXDNtMHLsV0rYYDt7l6Y6CTr0k_dN9WzOSHi9K0BqN26VUUPaH2WDD4fUZ7CiAO-Y-ytwc1lqWCnr_9paV0ICFYLOC0G9U-e-EJHEvoZseUIcEBKP60wn2HZut6470ic0m8IcPB5x9XrTLrLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBhBfOZ2RHAlWjwbjxviJYLYlYScUGXRiWGPYRjyuJfkJJwjtEPeOFSakrseImM-rcX02dfi3QiSCHgYtAPEE0cy3mipNpIOhJ2-Rgw7nntcqy1iOa5_YcbMxGRYaNZ_LSbys8Pove9nkvu-CJhsIuEiVxL5NaVS_oM0IzZiUMTvWw5KFIhVJ2e9hbBAK_p53_21Khq7AXkUFQEXRpQkvBb_OKVHssoQLmPeU1ZD4PJfrx36ZxYlhNNFNbSbvsKZ6ryGW0MdoZZg1TX1QHsDCDCV4teYoq6vGBaQjNFJen9ngw7w4zNB3yxDdJIlZu7xOgnk9caAXbrrg0tcrHSgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5tshjScOqoxyy2zCmi75fZHUfeHJTjRbOC2GRgs57mnboHqXA5Ha1b_-fSYbuk76EnfqI3VCKMsIWbkg_pi9CwQ9CFAfaKn7OZ7_BiiLmcR4Bj7MIrRfvrLYmojRHbFupFfS1oGIB7elrYF0WS_yefprvILM2_TM9KJDxOF1gITNXLex2pQ4S6HAnwSn6p6ecu744XI3OnPuQ3S7tztbhiH-jxO1mmSRDsG2NZe6O7qtlfjZ1O57-TKQXKr5AIkWUoAbDVMBXbUAPq0uJEYsgVVWVo6RV8JoPJPZ3HzIXu-8JNDtCrKI74v2Ee8g4r8KbUEyZTLukBSKagwMIzxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcBBQOU50mu1zjgPoS_TyHADiTZjeR4N2jT82_U1Riz5kIVa_JeGOMTWmhXxl4nuBz-XyTEVUZAxAvlBs0TNDssbvPQAli9dLh7dkfN2QjqS-fY-qNExRNR00PCp13RFRGbSU_G_jmyQorbIQJJ-_rQIvA2QD8ECOO8PUELIqaDyQ85zjaXXcfCKpVbKjuLJ9bGYsHAqstBcozJrjWhsxvTZQgGD-rRIsTHaEa-1aWc4-31ixyRr496pAu2lZL7psQ-wT9k4awoVRrj5sYNjcYU2WKTdSY8fLT9PGZQaiOWLea2PABjIolTVTbbARlakPqk2ZbvXdNm_caM2m0tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOBjBZ5BgCF9Ly74FCMz_P1u8e5b3sOtNVFSAStzdwzaLJvrjvNuzhkgzNbEv14N2WF2HKGkLZBnBRs-IPJGnPsB_fVkn4sOsOVyDnO6M78V3t_ymhX6KhJeNP7JxHX2lrmUC_uEPZveFFAEm1O33mOO3204cmbb-u0wxm-ogOc1tscF5EL8EcOocQa_4j4uDmasJBFe-gwjIniuEKTzuQCnEyfa5rvDWgw-2lxgT4IZAx546cYtVQt65XcUL0HIyy5DuJwL_CmuUioqrIP2T0sMZ7fC7ghlxereEDN0qf6R325IKxAjgpGef5I7z-HwItFYwSSDQGB39F7mlb5rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRIvvsQDyiWv9EyJLkMBXXJtL_TG2oIToPTeBe3lzqHoROkO6m6Vwdy6MDh-INgzYoyiRNeBUjAiqoxDGjJz6ijjTN9Tk0ctSsd6J47QkBqWZmh7RV1eheoEASjmxu0lf4NCcxQUJo06WBJeToajM6SLKKdcqRkOPPqPchcsoMog3KeTPmzcrLZD7V9y07wjeS4LxTfheQkD0_kciL7segk5SQ8QG5q74v1VV72HqujHPWL6MxZOxFAZ9F9kW0Bgbg4qu9JYeFk-reoGAIFUaFEsRuEf6ZN21YhHmx44_0cjGchoj-Cmmc11dE0PgeJ4GTKIumqEHYQfjwESEsfE7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bERYZWhZwUAs39VmbdueLslRK24ZFHe8EODyK-sLB3lngXy53h6DbknZEf0mHumT6bzrwvZa5sdkyP3mxoezzn-ujPp-9W9d85BrZJzOIqh78pDLlWKc3ndJo3cEy06LeZDjWXPoO4GaKGiiBTVqdKA-lkbh2GwKobbCsz6dSv8WRJiFjXYcUgYYl7LynstO30HOUs2e-DTmhTIriZkYEIHN0TJ3BxF3aqgHlgprMKvbUIQM3H6kROA4DUEPXoTPJOTH7MqfPkb8OZwAfNwv_DnjMp-dsdJu49WM6G7ogR9P0jBl1QvLQVhXW7XehszFAKBv_m6LnIRw5OaZ7ogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRkLBHQlgs5TMioXCcBCpEeLa847ZFogBNnnRmpVnIkh31gFytBIrlPSIYZCBjpl1uKM476-UAveRVrNyFRqRgC-1mI6DcM48pCviMXWlxGx19qyJuZzPnZ9lVcJe9C96dtgfM8egD7ZWkLs0K2YCy1YJoLCtfjCXOuP-nSsBCFfyfpDfaxrbXwDKgUvbciu9_hLHz5DI9PCRL2CXDlegTNFTTKwzMzaLRucOWDJhX_0hwl_sUiYYxH5l2jzBAjxUiswUcW6uCa-rKRadQCMJZ9aScECK0Weov4jKOh8GO2MvuuWfZXkmx0c7JjPTCvfjRsGUldEsQFylmvtJo42wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnlUjLzTwh-cBiegQMGhgSgF_yhY5pig2vsbnXdc8dfQKSFEw7UXQH61FUpbFvDDc6ZsGLbCW5uvd1hpi_eEANULqm1qhtz_tvZn1psPdSPi8UoURdJLxGCUGZw5ZxnpAv--qXb9jBbfgGbBxuvqDnPKnfW0-y4ZaaXPN7O3dTOqHCgSsm1_uyvIq6GK7ztAbOh9ab1YghO7w1snzRoiTOp2oDoNrk3g_6ViQH7iqgfolQwwfPcO1O7Al2h4fsOyXWEjRrCca77KY8ydzi7dQYCgH-Lnvn4d5zA9lR7kDKC6OeQ2Xln0qw20Vi9ydiVxzc3aI_bbH8K-Wrsd91wsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MryE288iiuyg2pyqk1Lzqq7bl5o1GZ1NsyrD3fy1DBQpOV1ffBnnJ_8kQYO46Oi-65YvDmmFiRHGZUdE_dfx_D9wW1antRZ3mCqsRKmyQVKNti3cmOchdImBjUJhsKnvXySftSLgjISqm49JZIyzEA4TGSBimrpqHKeMvrikGM_094zXW96luHqv09R0nOpHNoGLenn78BHCdkAHkmx2jGBQeh_givX3d4Ex4tClGm0bNlQ6Uxty9AjRMEctCqAqp5T6CjrGeG7iVVcBEv9QeeTm71B02cEqEQH-AZZDwOSXeeuYEbXi7LqlBcD2PX6fCbCaug0G39hfjs0iqfuVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyIyJpepVSUEtaZC80UZCAHbugqk0ItCrsnwj8_LSDJrEiF0oaqKaz5U8hINvpmPA0UjJK80TecUDxeXQ-7teGrVmCRaNbm3tpaygTQnGOlqPdizJPFX7e6IE9iY7WYZbW2r4BTn061s8lN23nnqoeOs1m4jeGu_epkmHRMvovglvGi5yrtVXPyKvMFF4VTEHMH6RGw-JxC7EvcR8B4GR-sKw8lme2gAF59pGD0IWZQE8JnhRYDIshlBUHQLuBG0UJmi4qJqnpmE1gfuLlz0jMFGk-0sKXDqAtBe2R_fRsT2hDIAwRrRMGll7Vzjxoqmhnu29Ivj_SomG0APB-40OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMzXuYnpbfYhPNe3mIHRMjVQ2T0Gmt0DpWbD13CY9g85dyVndzdqyWCrgS1e4tXk2puC_txtM6PU9D6iWy8KMDNyuWhfr3eEJvR6BiKMJQvVtajhYGy4BclKDDuGgt55KmHmwLMqPYTkXLyQZk_O5jdprhhiqWIRW2qVCX_6twQ3LOzTFJZWpyXrr7HfzaqAEQzlibIJcgeyvNI6J7gzEQ-xNrSYGy5E-XZDHPbHG-d8RTxFaira5q0Fozvhs2srS9TZOgbOG9brg-RTHo0Y0YNZLcduesiyTWzjVz5j1dQDLEmXRIKjOr6XaJnxPGn_0rrhGfEoWez0XFPW5hftjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=dQj17Cl971RWB_fH4eKpebz62YrIjJB5l-Ihp0I1L5lkFtCCDgcvP_T1VcSeZNne4RM0GM8F1MAs0EcbhVWf5iuyTjbbk2j1KxbHG3VQamQhkEkVl7NR09uLtLAfFrDnXdyKUif__NdZ1GXuVYLO6OQK252Ni-IZoUL79oe0IuZERMSV-IWmWKl6oHUyic0X819FCLV4RCO0jd-9bTXFg9n_2NbEG1znSBVu0rWpS21sf-sqzlpH5zG6o2H0-Alh-jNpi1CDQwNk9S1FDUjbDebRUW1Na96h_n6u0nYHJQrApGnjDwiKWkSvYWQvrPB0cnR_VXGVqmRhG7-hc45dHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=dQj17Cl971RWB_fH4eKpebz62YrIjJB5l-Ihp0I1L5lkFtCCDgcvP_T1VcSeZNne4RM0GM8F1MAs0EcbhVWf5iuyTjbbk2j1KxbHG3VQamQhkEkVl7NR09uLtLAfFrDnXdyKUif__NdZ1GXuVYLO6OQK252Ni-IZoUL79oe0IuZERMSV-IWmWKl6oHUyic0X819FCLV4RCO0jd-9bTXFg9n_2NbEG1znSBVu0rWpS21sf-sqzlpH5zG6o2H0-Alh-jNpi1CDQwNk9S1FDUjbDebRUW1Na96h_n6u0nYHJQrApGnjDwiKWkSvYWQvrPB0cnR_VXGVqmRhG7-hc45dHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=e7PmdsHpUH8JQAbpptd8T7B3fSLQR442Q15XyVB1QiRKJo7yMtv2wdt1sBcYw5-iEnnpGiYJ7As-ZFenVyibsGbkTu8Fep1mveKZBheqGv2Ns1MrYbFpleofqB2UAHeCG6oE2g7OBDVVVEyaMQpf-0U7Hy-aXCIPfljWKDDJ26IA2RkySa9KPK-Mfb4v9-7tKotBTfy0sZrWDMVyV-HGoyg8mH9lonmoJXvhM5Nl0C53fa_Q9MRQDI4ja07XSC2cSKFpUR6WZ7exWuWwCd6hD90g4-CVurJ3gXTpioxhji00aoFXqjx9PoSLGddU8q5_-igSXjC98V7oflCxnGEKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=e7PmdsHpUH8JQAbpptd8T7B3fSLQR442Q15XyVB1QiRKJo7yMtv2wdt1sBcYw5-iEnnpGiYJ7As-ZFenVyibsGbkTu8Fep1mveKZBheqGv2Ns1MrYbFpleofqB2UAHeCG6oE2g7OBDVVVEyaMQpf-0U7Hy-aXCIPfljWKDDJ26IA2RkySa9KPK-Mfb4v9-7tKotBTfy0sZrWDMVyV-HGoyg8mH9lonmoJXvhM5Nl0C53fa_Q9MRQDI4ja07XSC2cSKFpUR6WZ7exWuWwCd6hD90g4-CVurJ3gXTpioxhji00aoFXqjx9PoSLGddU8q5_-igSXjC98V7oflCxnGEKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=Ab2bO3VZMSpKTf7f2gzUzToIAOEU1uYzaESjOIKHc17gjHg-ZIHNt9XxeJdZ4rEJa3VkAvMWKtKUdnycDuQP8ybsFmATmpIjVoCmSmOB3gsP3eZVEhA06Ds-QpTO_cNLLHPJGnZvSCqJEn2nWvKo8NHjHP5Q9fJwTVYld-CZ2282cLgCJsux1Ug5fFi3CUwd8rN7th9Fg89X1iL_iUeflfRHngCc7xr2wpS20JZDHdU555vgFC99K8LXRuMjBFZio03CD6lp2x7GNikrBFtM7yTQ1a_RhtMUlf5HDXmhWAR6jfxL-ZyKlk1lT-Ls8gfW3L6ssLZIIBhCoh3_tRyYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=Ab2bO3VZMSpKTf7f2gzUzToIAOEU1uYzaESjOIKHc17gjHg-ZIHNt9XxeJdZ4rEJa3VkAvMWKtKUdnycDuQP8ybsFmATmpIjVoCmSmOB3gsP3eZVEhA06Ds-QpTO_cNLLHPJGnZvSCqJEn2nWvKo8NHjHP5Q9fJwTVYld-CZ2282cLgCJsux1Ug5fFi3CUwd8rN7th9Fg89X1iL_iUeflfRHngCc7xr2wpS20JZDHdU555vgFC99K8LXRuMjBFZio03CD6lp2x7GNikrBFtM7yTQ1a_RhtMUlf5HDXmhWAR6jfxL-ZyKlk1lT-Ls8gfW3L6ssLZIIBhCoh3_tRyYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=V_IKhvBhXLTIKUQYreuGjyLnAschS6XmvXB5sDbxQZ867vKMHOQRUvuZpdYcGOQ1UTcgv61jyIsju6h6NQE96T5cw4fx0uvChXOtuCC-pvOT0C3WTtOek0MSba5GouwxB-97H3NZRzXv0H-T3VC9qxBMRIG7jaVOkWSZPpoiyjlASpBA2hnhZof3F8gaYNwQ0IHEs6WkhG1WcRM1_IKPvwhoHC3zdwD9_sC9AibnZMbB2PMso03oLzHh5wBW3v6BJcZ1IZkICim8p_07SjsEBFSLb4jifefb53Qj1XSUC31Igwj4fivVzJbjePPeO6HGxxUh_VOYy6ugZyoETwGW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=V_IKhvBhXLTIKUQYreuGjyLnAschS6XmvXB5sDbxQZ867vKMHOQRUvuZpdYcGOQ1UTcgv61jyIsju6h6NQE96T5cw4fx0uvChXOtuCC-pvOT0C3WTtOek0MSba5GouwxB-97H3NZRzXv0H-T3VC9qxBMRIG7jaVOkWSZPpoiyjlASpBA2hnhZof3F8gaYNwQ0IHEs6WkhG1WcRM1_IKPvwhoHC3zdwD9_sC9AibnZMbB2PMso03oLzHh5wBW3v6BJcZ1IZkICim8p_07SjsEBFSLb4jifefb53Qj1XSUC31Igwj4fivVzJbjePPeO6HGxxUh_VOYy6ugZyoETwGW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKHaPCV73H46xp9cM_Uq9f7Z1Da8b32AdMEg-i0PhEtjLTmOVLU5CmrogpUb4d4uw4RvPicDbS568md8KfRRSK5l0_RwVGQlKjw3SCeMCcCRRxWlB_6LRbW-dvdTv_ZF-uqv4k7K_57wLHE9FNUo26Tp_JmrL0Bysm-gycxDvvOlkl0pm3MtEwa0hwW4zCVxSVnOF1GGLhCx3lcbo4rIrB6ID2wxE1XfXBuPNX6SN8ezMb0iEf_1rPyp4CiBfyGVithuTxJyitVK-PY623oOE_ivQcs17uwmXLMMtqtNKmfqRvlL-fY1s72zfn_U1hpEOF7BvWUpO1ubw2LqMByLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgTLJUO2k6cXmi31KRlQSE_xzP3tnvI9rRhhWpnhQYTVb-Mf9xdDi9k-Ma2aovKKlUN6IZnoXt2TWgp7mHgeUXyGlue0Xg8qVRKthV5NFG3AEKr-gbk4aUdx7sZOkp6Up44Tn_Snt-diPqsn0QxHexzOBoA2ynvLO_bIwyaiLt2A_fzez_EAWZv4paC_Fq2AC7JbaQFoVvon0cMVKZv8T0AEokkYDvIzjXKRg51DpYY5u3iBwDjR-W3NJ2XRfDZP3cH5MqulVe2ExCrq4xv3ZaLKP8xgpJGntq1-r6RJDMW-oqZAJrKs_UzzUnBok9wD8dmHm4PGsnY1kIzRXGMgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=Yq90WKKGy2NyfxcxeZyROu7eN_ar4FT5H2AS_MFQLcmGMTNnDxffTnEupThUcyoJDPumaeEhxTx7MjWmXbMWZ2MQTi7W4V4UpcRp4DxX3YMkipBtHVKpge13wWLfqvE7iHryfKvitaIeBDT7_XSLq4ssPPFnULOQmXfQG2TfBTzcRavBSAKlCyuMXEvlxqLZNLO4cZt9-jh4fFdB8GCp5DhPL7wuvD7Dk8evqbaJxswbd3OiEu_9pfcKsekY2CDf644ywu9YvAMPm4lzBSq04uNSmeyylak0GwpkvU-rIMGbFUwBjR7UKWu4bedaH4sd_JOPAKxmgYYY8Kl0x552IUDOIfAX58wX4Td-eoGK5oWircmATnXXMLQ62qLEh0Pjye0hv-6e-V018DEeU0Qicuhrt8YzAxG5gUiUOKySq_V9f21FWlQwfOZj3c3pD2fohcmOwowW0kvD3su33m30AthJJyTr4jfiTUbA32KXmRuvcwe6pGXNPahv990HDximBYXvTwgks7cIrby0xPI9aon0Tpz-nutUxD-J-73msG6C382ghHFJXLMbo7mFDTvV6WhOtSNUMCwL0fhh1090I4xoAqozI1DYpsmE37qmffdZ66Bffjw-SbiVubejzT3Ct01ZETmYyQyY2fRu9qVTb9ksdGxDN2asOzR4B2cTCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=Yq90WKKGy2NyfxcxeZyROu7eN_ar4FT5H2AS_MFQLcmGMTNnDxffTnEupThUcyoJDPumaeEhxTx7MjWmXbMWZ2MQTi7W4V4UpcRp4DxX3YMkipBtHVKpge13wWLfqvE7iHryfKvitaIeBDT7_XSLq4ssPPFnULOQmXfQG2TfBTzcRavBSAKlCyuMXEvlxqLZNLO4cZt9-jh4fFdB8GCp5DhPL7wuvD7Dk8evqbaJxswbd3OiEu_9pfcKsekY2CDf644ywu9YvAMPm4lzBSq04uNSmeyylak0GwpkvU-rIMGbFUwBjR7UKWu4bedaH4sd_JOPAKxmgYYY8Kl0x552IUDOIfAX58wX4Td-eoGK5oWircmATnXXMLQ62qLEh0Pjye0hv-6e-V018DEeU0Qicuhrt8YzAxG5gUiUOKySq_V9f21FWlQwfOZj3c3pD2fohcmOwowW0kvD3su33m30AthJJyTr4jfiTUbA32KXmRuvcwe6pGXNPahv990HDximBYXvTwgks7cIrby0xPI9aon0Tpz-nutUxD-J-73msG6C382ghHFJXLMbo7mFDTvV6WhOtSNUMCwL0fhh1090I4xoAqozI1DYpsmE37qmffdZ66Bffjw-SbiVubejzT3Ct01ZETmYyQyY2fRu9qVTb9ksdGxDN2asOzR4B2cTCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=lpjwTXNcLnpO0kjI_ph0yEpSknImMS-lWmS0abcnlKcxf5N-T5-rCoCbjlA_53LMQCsOddQ8MFz153bAsKgpYqIGXzAsyplCxYvDp2dKkeU8DKe4PLS4yZzy-amm9zZNP9dGyrtmWawHliAAHpbw-NybTsnLrDxAvLXL30UY1YnFAtAr3etFfOBYiPJjMXuL7PQ5H1vicoTWK5MClV3kuXDkjuwB8DO6s_g3A1SNGXgI56zwQOU-R-v7p8L1xRdDqcpQqAKSzA7UN8Uy7N6z1zouVHKR-eixJKi837aJcu9R-x0r2_bXY7JEN6nAflpoQZgNESGVZRf9UdSJT317yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=lpjwTXNcLnpO0kjI_ph0yEpSknImMS-lWmS0abcnlKcxf5N-T5-rCoCbjlA_53LMQCsOddQ8MFz153bAsKgpYqIGXzAsyplCxYvDp2dKkeU8DKe4PLS4yZzy-amm9zZNP9dGyrtmWawHliAAHpbw-NybTsnLrDxAvLXL30UY1YnFAtAr3etFfOBYiPJjMXuL7PQ5H1vicoTWK5MClV3kuXDkjuwB8DO6s_g3A1SNGXgI56zwQOU-R-v7p8L1xRdDqcpQqAKSzA7UN8Uy7N6z1zouVHKR-eixJKi837aJcu9R-x0r2_bXY7JEN6nAflpoQZgNESGVZRf9UdSJT317yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSLk-TS7jEg2Ls0nqoxjROQqTXNvylkHdjNITpOxDLqDC3zpa8yLzwnTMqXZEa6xEBxV-BdXVKqQHClRKEHH_7mCHzC_k_2o94gOR5Muc4Nm_ZYWV1p1FToqzCXPhsKyG7QrOOoQGHYtUx7WYrZ1jzEoSr27auuxHhret6HK3jzc4EYwB_NYEAGh2IB_QfcqtpyrsgcYWSvyByOFP6VECDJJ134m5aLqAY27b3p7ZOJC5-LXjfrkLJBLtUkY4tcd4WaqNH0lCUbJXxCporxQRXSWhJ9cnEagd0RgHl1qBL0gcaDha7XyONtIovB_ddB5khYw8sq8sj8MvBpaG4dA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=tX8W8apUeds6_dSQ-Go5ALICilGY_QaCOP1G6DscF-rau9lvx3Smkrk17u3XAmRS3BZkKN5dkTLJaGiEvqKvKhq__X75LkMj3ZIKiSiTgU4Z_7YzqmjT4NLUGgtMvcLmOLJtUCqCJXGfh9O8rT4YaTqZt-HKgR_SJiiO5hvl8ZJ1kMogX9xtU5fJhLoI97cAmBx_2wvl16dZ_AoWDu0MNHYrC38qvYIa2xF14I8ipTqGhjxAARr1ZqStQ169OQakpBoPFL78Av_QtxaTieQqFVNjNuluLE1X-0Kl2iP8PIobDRL2cfcfqAUazSLbQu2cK8eOFV-h5mZhI4nmDrHomw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=tX8W8apUeds6_dSQ-Go5ALICilGY_QaCOP1G6DscF-rau9lvx3Smkrk17u3XAmRS3BZkKN5dkTLJaGiEvqKvKhq__X75LkMj3ZIKiSiTgU4Z_7YzqmjT4NLUGgtMvcLmOLJtUCqCJXGfh9O8rT4YaTqZt-HKgR_SJiiO5hvl8ZJ1kMogX9xtU5fJhLoI97cAmBx_2wvl16dZ_AoWDu0MNHYrC38qvYIa2xF14I8ipTqGhjxAARr1ZqStQ169OQakpBoPFL78Av_QtxaTieQqFVNjNuluLE1X-0Kl2iP8PIobDRL2cfcfqAUazSLbQu2cK8eOFV-h5mZhI4nmDrHomw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=Q5H-Hn529ZhzcHK9dBdCK1KsSjxOTYI0CWjV9UEOTJwAk5d3PTFWNGhpz9JC_sg4OSFKvPCWrkZyK0w2MsHHbMBqf7B8d0BSQ8YcBOJtaWXPaw1aZnjv18cDWXzfJp4FLfh_ztl2kV8MNr1XlJx1rzA4XpEWXNoPHn1jyUsFhiIblYWE0xqjVKOMpyuC5CtQprtVNnvRgbGgYJamI0VpI9URSSHZv63fJM4Q1IphfsdWx05TVLDqNdBvCyAquMaiDozNHq6-jdNhQCP4EFn6WzPpHbQVaUK9gYpqAYWtzzjGtv--tt2IfTJlaEcMkZhpEv8zBm_wxamDpAqm43hYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=Q5H-Hn529ZhzcHK9dBdCK1KsSjxOTYI0CWjV9UEOTJwAk5d3PTFWNGhpz9JC_sg4OSFKvPCWrkZyK0w2MsHHbMBqf7B8d0BSQ8YcBOJtaWXPaw1aZnjv18cDWXzfJp4FLfh_ztl2kV8MNr1XlJx1rzA4XpEWXNoPHn1jyUsFhiIblYWE0xqjVKOMpyuC5CtQprtVNnvRgbGgYJamI0VpI9URSSHZv63fJM4Q1IphfsdWx05TVLDqNdBvCyAquMaiDozNHq6-jdNhQCP4EFn6WzPpHbQVaUK9gYpqAYWtzzjGtv--tt2IfTJlaEcMkZhpEv8zBm_wxamDpAqm43hYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcIAdz2X8PE-ZWYR3xwCwD0ySNUJvPwQGSsbbwn3eNo6VA7hPqtHrl-CHv_wdb2nmjt9qqnGFeR4Od-WRnyYQmMie3YCIUYCwc4nT-NHkPJ0hHl1YVs6UcGKqhuNKHTRLQTM6xSKhAbvX1WifFDxIUM3XKfLCjF5ygOXv3mTeSr-luOFKpOkfkBPI4BrO5WI_O8Fv8Hs84TnX2HXH3mNN4XT3WIGAgPLpvZJxGl6JUHNk7haOZ3aYPOIHf_xVZ4DVBoxwhPIT1_Kfzg1KqTGEteQeoW58JBOs8YCWKYQEqhdBrXee2hXcKXbDxPt4vlpkJw8KaHZnwMg3V8qvdOXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUV4SQDLgtyZ-DqLhrLAgyeHTmxH0b7wkBdrb7e3ZTMd5ug8-rT26gleV9Wd8l4S6LFQBiUBywsMeiUBbruciDSuoKe_cmGvtjjB9JlpLBuqFEPFF0bTpPXnWXbzxr8fztqoR4mYYOxTFrHqnKGjAivsqc6NkyAbCwWE3gulg2aSJRdRdGSe_pvuwjejdrITEVYpP-3ZH-xjdudEjdSr0H4BroDwinW79pQKEtoltHvJk9ev7zrWJEIi0YgmQs_W7iV2QFTPcryOCPQZxmSAqfUWVGrRftC6FfB6pARg1gIzq9J82207HTxJKR1JNmkVWmg-uf9mgMsl-bXFm_RlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttRCV3r4rzlm5DMz1Z8kdvmmK_eXxqhQbO7TvPY9TM6B4pKJC1jtqkZkJMsxY5BLjldAk9WkoGG2Z8xYORFNvmq77_2C8huLsu0O9pf1XD8e9h7rMPG1iWQVvb5bylyxlJSTmHQYe3qXaHXPoXocIJN_5lXHr1ysu8EQ1Ux9CYRxqpYESocX-iteYnAec2MOTM3f66XWFzRhh14dP07tPtTRpsikGwMhvGpDjmpQ2y4EvA2TC7J7BByFnK0St65Y5d7_kHW__f00cJeNLbdYolacWU6Eanpk62N0i-9iGZLykVkLEw-VLlPzZg405yqfbbN5-WBWGBFMwtYnmaFzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5beWq433JvoMGDZIiSm1WnZPs2T6KHRhdn3MaHpdk3FxjYTbPNvQ9xOy4iS7jUEfTpWZn_LbwjEB-LZAcw7C79Zws3j3SLq0_LL-CMVqiZ2K60ypuU_FwpBrzf_sae9VxiBMgZtqBhlOpFiEjln_Vk-16r83gUHBFrY6GlUaWmGsQxdn1rwVx-n_M-aIdHh-v7OwJsbB8vU0UxhJ0h4xFjNssjYA1tbEJiPlNZrFcu9ok4zEaN8H8HR579wfuWw7z2CC6TNvzbikVX2rT59ZDzb2EuM0pOvUSWPxwiXyTrkdGwKgmW5M0TWB7dY5UKWyh2mOnh1WLPcTWxrl9QjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=EXwiOI3CnXjgJzJOw8FYYD2GgQ1xxvu8KsdQDRtAcaELM8NGYcvJT9y_JqeGSOxnE-Hn6pV7uG7D99dfcNzXQYHC0Pprkl4SWnOggz9VEU4VzZPc4TihZIE829H3hQbZFHRit1Z7duEIZ9NPgfDSrw_iI6hgyhJFMYHl-2Fx-2v8gesgm84p5lWMekj-yeKPUg0gYXttWIq1rU4Pj-sYP2SAaNj9ACWoH1yjvQMAosfrqipod-0euaWqpj_DPmxJT3mtpNSjSIJOHKOw4ZSQuOF6hVPgwGDIGw4Mo_x1HaR0yY_5PI2x_3RLgPfWj6ZHbtPwXPZjTLFfRxvFrSvmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=EXwiOI3CnXjgJzJOw8FYYD2GgQ1xxvu8KsdQDRtAcaELM8NGYcvJT9y_JqeGSOxnE-Hn6pV7uG7D99dfcNzXQYHC0Pprkl4SWnOggz9VEU4VzZPc4TihZIE829H3hQbZFHRit1Z7duEIZ9NPgfDSrw_iI6hgyhJFMYHl-2Fx-2v8gesgm84p5lWMekj-yeKPUg0gYXttWIq1rU4Pj-sYP2SAaNj9ACWoH1yjvQMAosfrqipod-0euaWqpj_DPmxJT3mtpNSjSIJOHKOw4ZSQuOF6hVPgwGDIGw4Mo_x1HaR0yY_5PI2x_3RLgPfWj6ZHbtPwXPZjTLFfRxvFrSvmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFQEM63TnELzndnjFS6fcJXdWqL1LMz31P4fbAh3EjS0BjfG3lAbo_Ixi1XqTlenPidXUrDqquuaFFntXHLTZ9kWmi6K_iIZ4nw57pnDBRzy5gUfyWimBnUU_HEtk1xX2zlRDsMDaE_6PqCJJ-HYLxaB5WICuTr4swoeB8S07w7TmVxc7qwcahA4jzl_VJS2eGhUAkpDhTifHHzDinrnrr9fno19PcGGe3XVpPARe6d3GSaTAAAtRi_b-xA_tgH3c1DW38UHTmhj5Mn48CdhVg6jjwCT7bP_sZ23u3SAKNsXAHWgthWwSga3EtPvKuD4IxZSCtLSbeBi5QOm7HfUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=dcydCbOTXyvq1Rn3YpOfsAheOwqRvFEUSTQ0rP4GvyE6zVwsNb0ldt5W-f9Eeb0dIlC2arfDIdfJ9g3-TE-_XdNOA3_J6mE8R7XZX-eBe8xFj0czp8Z8BNKGsZEfaXWz_VltVjjd6A0lGxJOw5ihkFSwRcxnNd9P80fjpuPhvNds1z-hXZhfpkTbsbFzOVKS1BdbGdWyd7uNkjrnU67TQPwwzSa9i6PTRMyIQRZh-CVZMdgZXx9nZ_aj5lxXhbIAFhp3XgfOPzRjjDO5LJoFcx5prEBfDlAFT71F5OkI5qE11g8_fpvZyLsn7CDrIwzS8f8gqJyz9bSOI2ywwtJbTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=dcydCbOTXyvq1Rn3YpOfsAheOwqRvFEUSTQ0rP4GvyE6zVwsNb0ldt5W-f9Eeb0dIlC2arfDIdfJ9g3-TE-_XdNOA3_J6mE8R7XZX-eBe8xFj0czp8Z8BNKGsZEfaXWz_VltVjjd6A0lGxJOw5ihkFSwRcxnNd9P80fjpuPhvNds1z-hXZhfpkTbsbFzOVKS1BdbGdWyd7uNkjrnU67TQPwwzSa9i6PTRMyIQRZh-CVZMdgZXx9nZ_aj5lxXhbIAFhp3XgfOPzRjjDO5LJoFcx5prEBfDlAFT71F5OkI5qE11g8_fpvZyLsn7CDrIwzS8f8gqJyz9bSOI2ywwtJbTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=dXwbPoqhLXvpOZ1qbmRdQ5rw4jDoaNkpKlJWotTgWi5r9R1HQoJLANswLM3_MlKNDfq_AYbjv4vymwAQaSltbuF_P1pllgC620-QEDsnUxStL5IvT6iwbDyB2YGxs40TP8zWqCiiQgc2G0Ttt4s9ffNnIdKjuZVx3I7Sdag78qCkAaszMj7O2-tNJqqljcmrFJ8tr36wRqXAlxBfLkI6v9Wl2DoE5r_TdDmFt3_i5p6UtcGlLC5PG6mZJD8uE2tQkAK9IW9IVBBIKnDlYIksBo1bIbslCLm5mHzaTHaF9FO-0lEXozP8gCtz9XKiWgZ14O15oKSxMXyLb7XcZaiBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=dXwbPoqhLXvpOZ1qbmRdQ5rw4jDoaNkpKlJWotTgWi5r9R1HQoJLANswLM3_MlKNDfq_AYbjv4vymwAQaSltbuF_P1pllgC620-QEDsnUxStL5IvT6iwbDyB2YGxs40TP8zWqCiiQgc2G0Ttt4s9ffNnIdKjuZVx3I7Sdag78qCkAaszMj7O2-tNJqqljcmrFJ8tr36wRqXAlxBfLkI6v9Wl2DoE5r_TdDmFt3_i5p6UtcGlLC5PG6mZJD8uE2tQkAK9IW9IVBBIKnDlYIksBo1bIbslCLm5mHzaTHaF9FO-0lEXozP8gCtz9XKiWgZ14O15oKSxMXyLb7XcZaiBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu_tDsUsI8q2biWAn_rmeyBZV4WWlaW-W42c7kZ7vPrmnzzvU89SFLKVR1Rcly59Y6MmQIwzVgBGYVCeUa_ndnr3dEbZrLvzxO341kTflt2tSNzmawEjL-LvcRZqHiYk_zTLfn3AStp4VFn3uKKr0rIV7txVmueucOPR4WukgvEJEqFVF3R7lAkwa0_py0RZpBT30belhJuKvkQNtGvw0NlMUA_NwqsJyT3OBZqOuyK66H-kjMAZYiZUC8CohF_f_EbraaNCE0DZc-CcV8da-hzFG4V92MK870DFLPD0eqrxO24UvToNiGqp_BCQscX3cubdVYy61BY1PBfSS0uucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=Pc4SKGQIgwZ2KnIsfT8nJOkX9nMZiwf3YsibEJnd2n9EzgEdtMTj1Oj8v1v90ioFCI73enlPDIrS6b3A10-tlHsFRadtecgwIKz-DWZZl95TNVS33W66qIz3-5CmJkDGoZneMTtSNFw7qu_hNgCoe9M_ofBskVvNZRE5fUpC8zwu9iGhRvpIjmj-I_DdyhQNVZzNWlFTgFER4H9cVPBomgqIcCRVPsgn-L6WWKpGA8MTF7nPph-_Ho1l1tQA4jZmPWyv64WqmxXZ3I_x3zZdHOnCR0GNZMY3Fjlm8U6LMCk_kk_yChOnY7_DcVK6dhgau-dOdLepKiEJ5cdJnMq6Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=Pc4SKGQIgwZ2KnIsfT8nJOkX9nMZiwf3YsibEJnd2n9EzgEdtMTj1Oj8v1v90ioFCI73enlPDIrS6b3A10-tlHsFRadtecgwIKz-DWZZl95TNVS33W66qIz3-5CmJkDGoZneMTtSNFw7qu_hNgCoe9M_ofBskVvNZRE5fUpC8zwu9iGhRvpIjmj-I_DdyhQNVZzNWlFTgFER4H9cVPBomgqIcCRVPsgn-L6WWKpGA8MTF7nPph-_Ho1l1tQA4jZmPWyv64WqmxXZ3I_x3zZdHOnCR0GNZMY3Fjlm8U6LMCk_kk_yChOnY7_DcVK6dhgau-dOdLepKiEJ5cdJnMq6Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdX9XUoAwLVwvoZR50Be6o2LP95HNyfAZPCaWRSf6cg7kMr2x0m5F-R0Ev8JFmeQg4S-l-wgB-i5ZeNs8wM8r_oRA3wcW2XLT6ToPOgIvtihprqpBlSL-d2qk8yiyobOQ66UDkolMB7_AHEMZJR0Ho-pvPgIQBxZbPLWQuOWhsWKCfQ-UAB2cyzGkr3BBrjxo_wvYryR7qTu3cIdCU04tkoMVi8IIC5w6TYv-p1ppffVFPH4LtOk_4Y0RjWCM6WBpdfHTwleC8NKOl-U4Y8qN9unmzmPmGoXQdNcOWRhbiETxERewfsjSp4Nfx5vnjqZtnVra3kVzJeprsQdwBGWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWUhV9qHqJvAD9kAf0-p9JTnq9Tm-13QpY0Q0mMlCr3xH_x6KJXr8Orpyh1kmGWqOc4e3WAy6GoFxQolLHtxGxKEuCcW2aIPPsRFT13adbFF-RAiCAgYSuG8ZW4VlH8j7IwKqZRjMQ9LGsrowIrpBv3p-PkbGaQE7IKVgOyBk4vNFqUPM34P_xsNAjFVYXtFqx_DIn5ZK1XJF81dArtddEDfONRHAwtREDyY25og2hh-631WvylN75rr3SwYu5wrOfFymUR0Ng9RfdCYC0hEuLH3t8ftlKcfP5yClOYasElti2p3KOwis4lk4I3WInyXN231Dteiix2Bsn5oNO1SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=rDjsZkkVLDDHXH1eUlkz7ILP1U3hhySGadZLG1i3idOyFv7qGFd5bNKUsrPrVE4NHsfkncVVyd-SbiLp68Fep38nH8UJJ5g2GU2nCptDdw8XRDJa3HUsxeSlCq_jxB8BDk6PCkCDekkroM0RFga9hv-jI-QaqZ62k9VVn_3XYV8StIlifSgStGpFhKiGJtOvHMfPOehv9Vcc1v_QYAk2W8x5RV_bKBPTulzcNNQ6mF9wtoJabPuLP8ib9BpftURRLOtLqt41aQDh2KXa5ZU1RuURdniVi9wt76VRJ1BZ77BKAqIwrfWvbN13fsLW-5AtUjeE5hufSz_O3RWZqQJj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=rDjsZkkVLDDHXH1eUlkz7ILP1U3hhySGadZLG1i3idOyFv7qGFd5bNKUsrPrVE4NHsfkncVVyd-SbiLp68Fep38nH8UJJ5g2GU2nCptDdw8XRDJa3HUsxeSlCq_jxB8BDk6PCkCDekkroM0RFga9hv-jI-QaqZ62k9VVn_3XYV8StIlifSgStGpFhKiGJtOvHMfPOehv9Vcc1v_QYAk2W8x5RV_bKBPTulzcNNQ6mF9wtoJabPuLP8ib9BpftURRLOtLqt41aQDh2KXa5ZU1RuURdniVi9wt76VRJ1BZ77BKAqIwrfWvbN13fsLW-5AtUjeE5hufSz_O3RWZqQJj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9js5ysv1CjgpNq61k3CPo_P6eV4IJy0qLgkuIjTIB-b5WWaDU8fOm7EFHXbp6bLdHxCxN1zZ8uPw7miiIZHRv7TMJisB2w5eU8UPTIYjmmeoYNbpf_yUtxBLi-24d-BgmN9fXv2UzamamPL_xJGk9b554HO54kJVGSQHrKv2fLolDEGtp8WaYnvCzr2a1tDm06Y1GyBK7IFFWZii8IyrtXneE9dKMzZKEZrCwNalbIkeOHcPTKdLDEIOxuaApLa_9xYKhhtwA_Fk9NaVajxXE_Mq3gu8wsVlxopESq8tgKvTGJuJj0x8wZfTDxyG8cdw1p_tCAbd5p9wnreQ8SO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXMspyRqlU0Uy1TpSufOU9hIreC7Suojnnxw1FofCfcsR3oV1D7vYMusSCoGL48ZXyD4URGa_9FL8FSlwc5-2xuB_WF4UoBLNNsZiEMnXmf2PV1_IwvKbg73Nn4zewV_eTPm16ZPagp7t7ygnlFcKCaQtuMszhdyKTdjIUkRFqjpoVvYEyKqAlvj0Bc7d0ZFvRor7icGHArr8VSHyxL75BpciLOsDzJPpzc_T7BPPGI6odrcYP2YFr5jabawufUtkUDEYkgD2f0X6CU_7pvCUzoyUV9zYYIj62pyJBdGyHUgU6ff7Oh9ghEItcy5hxze-IXV_vorFvMqfTgyzuJ1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=CTAg-GrUgrDC3JLgB658-CKsWGkk9_xP-DJpQbXWxlK5ZO1k7txmubxBjVWrbrdmlppDe_K2lR3GJxDERKwgePp1p37N3xnrTyCn-16HRTrDtWIw14dnvb6mrD28myHKHXaVxUkNIVqkjdHhHlWUhaACC_MD2n5tAwVMJdOWGrIHRvPCp-f91PP_OpTQOsbWs6Hb4R6cs_w0h_bjii2yH_fGuo2G93H1994DgZ7nbiNVdCfe-DXde22t0sTtkKPjI2UxiQ4XTsZfnwNyV5-qIvMnRnoGq4Gc_BiP0WJ243r4RnAz4mPI5H_4G80IzQHdRjN8GcCalGodHc1CPADWOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=CTAg-GrUgrDC3JLgB658-CKsWGkk9_xP-DJpQbXWxlK5ZO1k7txmubxBjVWrbrdmlppDe_K2lR3GJxDERKwgePp1p37N3xnrTyCn-16HRTrDtWIw14dnvb6mrD28myHKHXaVxUkNIVqkjdHhHlWUhaACC_MD2n5tAwVMJdOWGrIHRvPCp-f91PP_OpTQOsbWs6Hb4R6cs_w0h_bjii2yH_fGuo2G93H1994DgZ7nbiNVdCfe-DXde22t0sTtkKPjI2UxiQ4XTsZfnwNyV5-qIvMnRnoGq4Gc_BiP0WJ243r4RnAz4mPI5H_4G80IzQHdRjN8GcCalGodHc1CPADWOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=qt4hCDx_PC7DMCIK2ZtqI0dcyDZHu2bBg3Ulku_7a1F_J6vEhz2qfPxXr-jZ2CP8Nd1Ke5v5TP0Szc0Ux5FwjrWxMD-BBMiZ4WAEgLQOLCKoS4lly07tGw1tw-P7MzlsJuopLchtkAAVTJ-VTYt-en8oZrZpAmKeKIcvJmIerIe7Q-HdYH_FcZBKxR0YSM1X1RbBPuf3fv7rgAYzb_ia3qBFeLAIMD52QvnCh5ZlsFeUyHlxlNIsDCQrChsVAayFre_HXHz1fdEyZcmBkt6cJyrjPL4KmnYxgt5RbiHkeUkGC6sNZ-JUIQw2CYNhcsxoiykxnC52dFK5vb3CoMP3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=qt4hCDx_PC7DMCIK2ZtqI0dcyDZHu2bBg3Ulku_7a1F_J6vEhz2qfPxXr-jZ2CP8Nd1Ke5v5TP0Szc0Ux5FwjrWxMD-BBMiZ4WAEgLQOLCKoS4lly07tGw1tw-P7MzlsJuopLchtkAAVTJ-VTYt-en8oZrZpAmKeKIcvJmIerIe7Q-HdYH_FcZBKxR0YSM1X1RbBPuf3fv7rgAYzb_ia3qBFeLAIMD52QvnCh5ZlsFeUyHlxlNIsDCQrChsVAayFre_HXHz1fdEyZcmBkt6cJyrjPL4KmnYxgt5RbiHkeUkGC6sNZ-JUIQw2CYNhcsxoiykxnC52dFK5vb3CoMP3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0aOLbAZ5ki-x-1yA-ETabnX0Fspq7PfdhXxV1U4hJs5ImtQwdOLJmXD-wQBN0LBGbo1fkro_D0hY0IN_lQLtPLqqKdF67Gn0UbunGZIjgXCt9o_trma4SGYNfUYJz51Pb9JdYFZVo8OQuJcgwl1phJU8ZKMzv0rpb6MMwk_7hCQ3egUB0-b9hhRDeODsKg3-dvBbV0nVzdN8kGvKgx969uw2CC4M4o5LBk4gWDgU7SwMEuSAwUQuTGxPj9gU9gqnWtqTnjvijxePfRKgN0AIHmJWNcLQVA5yRZ3okcA4BNwgdwR4wAX_vBpBMRXV51FIu7kYgFxMUB4x4AUsgTc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=izj5yumewLupemsuyOkLgQC3p00GXhuvYTv9Rq5D02T6Y-ooNc6RpXO2NrwJQlz_Hq_T_d3r3zkM85tptFFqPoR7v1wmOR554kZEII5BmPLpHcclcKCfbrO7xMPdJpygwlhCp9y_oV9w2zr29pwqpVzrlaWXToXKKW_dLfhE79hwz6A2M4EwEmILz4Qo0HrET--4aSMa1E5-7PEqrGA7VbM-YeUz3mOPBcpyfRrPC_zSOT_m1tLJxsnFKbANWqq9_SZBEdPyw3fjKWwyBgDjICsLsxOXlMsfe9xLbIXkxUyYrOjx2kLE-rqGCu54R8kS-tIPVxjABv-NBTQbIHzJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=izj5yumewLupemsuyOkLgQC3p00GXhuvYTv9Rq5D02T6Y-ooNc6RpXO2NrwJQlz_Hq_T_d3r3zkM85tptFFqPoR7v1wmOR554kZEII5BmPLpHcclcKCfbrO7xMPdJpygwlhCp9y_oV9w2zr29pwqpVzrlaWXToXKKW_dLfhE79hwz6A2M4EwEmILz4Qo0HrET--4aSMa1E5-7PEqrGA7VbM-YeUz3mOPBcpyfRrPC_zSOT_m1tLJxsnFKbANWqq9_SZBEdPyw3fjKWwyBgDjICsLsxOXlMsfe9xLbIXkxUyYrOjx2kLE-rqGCu54R8kS-tIPVxjABv-NBTQbIHzJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=DkU12hywAcLLafdnGlrY7NKuGKkHubE9LuGuOIfgkZhuE63RYJ8lXw_HAIuptU1X2JDkBWqjOCq5dT6TJoEN4rN0A4MQNqkGGnP4xiSvacQ8QJy6g3IXKREJNPpaQrK-PkyVreUBCIZj9_QM7y4wesBGMJ13_im08XxfBNLQ65TCDFyyGrz99--Qm-Nfiu_H8K3sRPkWyO_EbGDlrfQAX9TAX7qYUcpnPcX4q20tuZpV84pAKFBQ-dKUknqNUymp96g2wGQCSSX6wDrI7YpieYaWtX9HmX44798rKwNFx1qyfqOz5x71ceeir6OC8-sKTJlMkaVVpkuO2r5U2YI_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=DkU12hywAcLLafdnGlrY7NKuGKkHubE9LuGuOIfgkZhuE63RYJ8lXw_HAIuptU1X2JDkBWqjOCq5dT6TJoEN4rN0A4MQNqkGGnP4xiSvacQ8QJy6g3IXKREJNPpaQrK-PkyVreUBCIZj9_QM7y4wesBGMJ13_im08XxfBNLQ65TCDFyyGrz99--Qm-Nfiu_H8K3sRPkWyO_EbGDlrfQAX9TAX7qYUcpnPcX4q20tuZpV84pAKFBQ-dKUknqNUymp96g2wGQCSSX6wDrI7YpieYaWtX9HmX44798rKwNFx1qyfqOz5x71ceeir6OC8-sKTJlMkaVVpkuO2r5U2YI_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=qC8LgeboyENXBVzrmPdXthHwKJJBF4_J1DqUY7YdXM1-gvzl9vvoWdSyAIRIu0m_lVzt_EmdwuRqZUb45C0eZM4jCQ7i7iHpXsYuhNa4awnQJsTLMG2H2azsr3QvRKtrzqRj2TXSU4m8PizncYNTIZx9oCPgaoRsNHBB4xAjixADaHEUXG7Z_elVbjfc6EIH9XR6Soow9_L9mysQsg2H1ov5A6uCgLt4giQNwXny4ge1AnYVQwBAIBvYLUMHPEkIiHkvb8zWcVeyQubpnxhI_yNIeQ7NwwMPwfE5x_25CvDWerYMDJfXSdhGTLaU8pCj3qP7zr5F3APINRO4AvXOKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=qC8LgeboyENXBVzrmPdXthHwKJJBF4_J1DqUY7YdXM1-gvzl9vvoWdSyAIRIu0m_lVzt_EmdwuRqZUb45C0eZM4jCQ7i7iHpXsYuhNa4awnQJsTLMG2H2azsr3QvRKtrzqRj2TXSU4m8PizncYNTIZx9oCPgaoRsNHBB4xAjixADaHEUXG7Z_elVbjfc6EIH9XR6Soow9_L9mysQsg2H1ov5A6uCgLt4giQNwXny4ge1AnYVQwBAIBvYLUMHPEkIiHkvb8zWcVeyQubpnxhI_yNIeQ7NwwMPwfE5x_25CvDWerYMDJfXSdhGTLaU8pCj3qP7zr5F3APINRO4AvXOKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=czFkiWghwl264J7xGYXap8jT8CcVQcyOubbM1cs6XJng6-I3j_8t2TrOhvcH9DmAN-fxKn8z3Ca0udJO3M5-jMQZgitwGAet3oXtX3VMx3IGrzfnNS2WySEcS6Nu-5W5UU54ZJTaKDfLYikTo3l3csFHtRAF3J25SIiQrR3hhfZFBi0oR34dJuh9upRoiwFtlix-R1pV_G2ftWElIwU4pyKxrOHR6MfbF2OWienIwd5qAWRFIuYnSHcL1ZREcHZTgJss90k_Ix_gcVBi2mxwkqjOu0j16_4FRM0OxfnQvrq7GDo1VnPCGIl_zxarF92kfyDU_AHIu7JnSmrBfNBtPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=czFkiWghwl264J7xGYXap8jT8CcVQcyOubbM1cs6XJng6-I3j_8t2TrOhvcH9DmAN-fxKn8z3Ca0udJO3M5-jMQZgitwGAet3oXtX3VMx3IGrzfnNS2WySEcS6Nu-5W5UU54ZJTaKDfLYikTo3l3csFHtRAF3J25SIiQrR3hhfZFBi0oR34dJuh9upRoiwFtlix-R1pV_G2ftWElIwU4pyKxrOHR6MfbF2OWienIwd5qAWRFIuYnSHcL1ZREcHZTgJss90k_Ix_gcVBi2mxwkqjOu0j16_4FRM0OxfnQvrq7GDo1VnPCGIl_zxarF92kfyDU_AHIu7JnSmrBfNBtPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2TvpoVtPlT_QnSOs90QBUTu1aigN7rqQof9KXE7IxhLt89LhLx-aQBUYETWYKQON7xmC0PNuPrD0C9Admbxo12OLwLMHmpaXZ49lQZGhFZ0j0uglA7DU6UQZf-YXuxWnVH0cV6CnAd-D9fv4pdwhfahSpCy9mDh--YNfmKiomVvSfZOGiAmK3nPA5emsHU-C6i0-xg-sQJ5ad3Pvvai_HQrgaH_1RGxVwYLjYb18Y1OlyMRsBpIrzOzku6-IEcjb37QUE3E85drdrr5xRkweXGCnxAtsBumMCLLCR3z8ePl1FX8PM_Z2FmnluEpolet3bmEu1QgzzUBm7Q-DRblfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9THqGTE1IR0E1STG1sg5HmuoOxC8JvmlQ4sADLUHgryUSBs6-wK1WiSwlqMyde6WgKofWAAyUmdRAcHMirtVn_seXQfstYpsHeTyhOT71OjETvkiIdh02nLI71YCxC5drEfq_ZZlfRq9UxQcql61PELhcCFzLDOpuZhf2Gv5-fgFz_lSj0YRpnB-y1PVQaYdC-NxBzOBphiTD6RDs7cxZC0MwmezEICNwOBSBbGEWsT-PaoBnZIajCY-O3cNPeJeTaQBLHu24YITkiqxHxPjn-Yh1uTNycE14xOMaIwXeaUEUUZGzjEwzMt4czrW89-nHADU00FiYWvLjwED-T00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=Hly3qp1buyM0YnxyXIkrK0ZZ-Is1ijF2_ArZYi2d3BLPIfmkqrmuUeeEQrMkkiafy4cHvyOQLxBohJBBr9xMSah0tQk4CHaytPYefDgf0F6Xy0yM3Tr2Ww37lRI88UOzpgfjq1iaNka7_WFooa4qX09yNcRkLVTMqRUPorB2cADtlpQg1gZeYCHm7q8XuALoMsNu1eHAh8LJI86tT_3XEKI_UpO-cC-21Oq9QjhF6-gYpNWgT-TIvwWqsGTUoiWcdnHbDWqfVD9ABl8lm-5-calhqX6Z6lctcJ-DOliTMzOzo5mAGCEbSdcnJRWd9tGOOBg5y1bxwbZo_q-bJj64Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=Hly3qp1buyM0YnxyXIkrK0ZZ-Is1ijF2_ArZYi2d3BLPIfmkqrmuUeeEQrMkkiafy4cHvyOQLxBohJBBr9xMSah0tQk4CHaytPYefDgf0F6Xy0yM3Tr2Ww37lRI88UOzpgfjq1iaNka7_WFooa4qX09yNcRkLVTMqRUPorB2cADtlpQg1gZeYCHm7q8XuALoMsNu1eHAh8LJI86tT_3XEKI_UpO-cC-21Oq9QjhF6-gYpNWgT-TIvwWqsGTUoiWcdnHbDWqfVD9ABl8lm-5-calhqX6Z6lctcJ-DOliTMzOzo5mAGCEbSdcnJRWd9tGOOBg5y1bxwbZo_q-bJj64Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCIS7fZFlQMJ1IpDFHc7WAjwszG9LSsH7yqqAXtFyGVsz5rqrdqICXOcQuNONVzEu8gOcJ5aIlKBg8KrVqLDKa1UoytKv2s6MyGM3Y1sgfflTOrIW6PjBirjdbO1vEyzHX3liD9FBnJvbY1vQbWrL40zrU0mytAl7hNliDWPR_g7_bstOWkQGUfqcgjUjWg1FT-1cuj2Yo0fRdFcYy3j7vWto77jpnIVLmZpVLF9FTEBxXlX-h9jOLcWUiQ7rPRZ8aq14d_MvBpOxj9opbQR14XSRXHcF7ywMSAsLMrU2H2qS1fxsmxQtlaLkuML-FIsWUX2qsM7zvHknnQFXLA6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofuIS_lOKHk5iIag3nrhQqyu_CMU5OY55047NKkZIWgRfLVRgaYuSeVf3aEJoUkuhST1mnzEgM6bUQMAAgXsWz0lO5GEfQGhEkWxzAmCnOcc_7QPSWTKpYYlWObKOIWoRWL8luliIhCbrpid4tjya-0U04XGwyeZX9aAHluoUhNXAVbMjLgA6SQG1XrwK3e03tzrMleigiLYI8aWr3zx6Dt8LMKmUiUyN4voWkbcgGRTnKtEyi7xsRwKO2ZTwSKrWCsyf5xBt6uOiS_zf8m9qFzi9HPFty00Qxfj0hKzT9mUpG5eYZ2kVhMljKLAD8f1ndgs3cPloF7p3s1fP2NIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rA5MItFpsgmL0w3Hr_4bHSzS1cKYe70yISM_tE_jlUrNH00HOqjNbOW4a8FYExpi9hpw8v4VBhB6Ye-fB-FnOgLOJ3yczsC6tylgxw5MYniL2G3Ax1p6PF9ayPSY-4KpPlYEvedHWXOU0-gfjXzpfPV1L9bGEWrWi80dyRY_5lW1PYCXSpLUWciL_zYOL4r5tTPZ6LtgHMOSl7nP57412cyi9J16k8cx_OeBhi4I45IMGCEdvY0YV5paFG2PLawFTwSQ0WDPwVYjko0cVC1VySC0dIQRXgDlh75YPRZrT8loYZc5_QbF8n3YOQjrNzy4h4Hk946adjiZ37b0IPsP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-TRPxyWv88QJ0-B5wWfFqWQMNFd623Pokgsv5wwaqmBn_S2tDK2UskgaLiE5o76QB-OhzmTYJVSbLabhXFNvCWhmxYgolZLG1BJrJJ8U-r1rZNI6QMu1xqRzM3vQfkoQtIHh5Gw_HAGEJFiNN2lt7hAl1YkM9kYjEpbVjO2Yc1mQ2HrMTRUsNQ4vwLQGCnnzx35GkC9iaWErRkYh_lArZOtf4H5F5wrjY_rXGBpaBoq9Ih2Gtfe6Rw2HEL9p7CKB8vOfs3huKrNQgzk5vbVEwpfCD-PVPhJMYx9Bg9c4giDiWw6rYRlBpyHWpct1dMiBOEPK8SEVABIFU14zCPUZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=u4v894CQCPcKkmDnDx2Cqjqr0Hju2cFv01KWNBT2JmzqNpqpaGnFcS-5_1PrDZTHOrl2K_jvp5adylczc5sFCebXonKjfoXzRIEwqahv9xJyVPSNQh4Qosn02OtVXSqBmPKOnEBhrNZot2rcefGCyIO0caeiAJL5jMn6q-LXC_AAF2YcJRjK34YiWnqXQtLwFdSi4A8CVEUJ8N7ZcPF6zxY5_jCUIRgjKX1AEJXjcHw7DfEruiAhsRVwJrsT_X9uvKU4sdDkZP8_VbNGdqLICsMFd2lL-zoyIZQUR7HAlv1A6NWKQE9ZcatPF51dv7MP88ncCRGpa9u2gjxyjedy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=u4v894CQCPcKkmDnDx2Cqjqr0Hju2cFv01KWNBT2JmzqNpqpaGnFcS-5_1PrDZTHOrl2K_jvp5adylczc5sFCebXonKjfoXzRIEwqahv9xJyVPSNQh4Qosn02OtVXSqBmPKOnEBhrNZot2rcefGCyIO0caeiAJL5jMn6q-LXC_AAF2YcJRjK34YiWnqXQtLwFdSi4A8CVEUJ8N7ZcPF6zxY5_jCUIRgjKX1AEJXjcHw7DfEruiAhsRVwJrsT_X9uvKU4sdDkZP8_VbNGdqLICsMFd2lL-zoyIZQUR7HAlv1A6NWKQE9ZcatPF51dv7MP88ncCRGpa9u2gjxyjedy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PunnaLENyZV8V6Y3k-SLiiprkBaZCCtTkjWdr1snJDETLKFPsn9-rIep4mOh3_h4SJ5o4_rvcRcAF5txFhYvIoZfyuzWxhkIl-Gww9xHqO8KLy11F2xgEMbsTeCM9fv4PormNgylRd8DPmROAfJPhcZmRbpm-fnxpFbpDgpa45Jx7yf8ZI1cu2lSar6UuDH1uHSQaOUO9UTOc1catFnt24-IAajHjzcumL_YUwgA-YwqxxIxTUcZGKsegQc9AbI5rLuGjQGbaPiGz6YRBmDmPiWOBJV2WfR5RKvNYvHmnJDegFxRSH2MK9kRBxMHz-cOKs3dBMgZLPXsQZZ633DMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ahAh9OWBPX83zjQ10HHzOJ-mHT5bSs81a22kgPxxBAjRr8rG0Fii2i_fS5PDBLpQYUOIIljjg9OWn8-FCnVkQdCSBc9mCfcpftbJPqWHQ0uW_NKo2RFc_mllc3qmGm-kK2AIZyVmQevoFg3IUQtKor7w2v_OcXlr3XjwnEjUyKwicF9aA2zkHIZ02xEtpGJ1B33xdpibYcgltp9lW8sNY4GNvQT7N3hdg4KbA5Q4piWDaml_tgm6LplTxcGv8n8_38Zx9FvHGH1pJ39N0eE_yHmWVKXWj35CMQFhCVIhQQPuNOcb8uCuidHaHf0kaEiZLX0N1j9UnhKBR2PsPObVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ahAh9OWBPX83zjQ10HHzOJ-mHT5bSs81a22kgPxxBAjRr8rG0Fii2i_fS5PDBLpQYUOIIljjg9OWn8-FCnVkQdCSBc9mCfcpftbJPqWHQ0uW_NKo2RFc_mllc3qmGm-kK2AIZyVmQevoFg3IUQtKor7w2v_OcXlr3XjwnEjUyKwicF9aA2zkHIZ02xEtpGJ1B33xdpibYcgltp9lW8sNY4GNvQT7N3hdg4KbA5Q4piWDaml_tgm6LplTxcGv8n8_38Zx9FvHGH1pJ39N0eE_yHmWVKXWj35CMQFhCVIhQQPuNOcb8uCuidHaHf0kaEiZLX0N1j9UnhKBR2PsPObVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBCgGrWuHCourld4xHoybmTNx8X1JNHjkHXMHQETCgLxKFSt3qXomyNcdlOVi-quvqOOaxAFA9pxagrFHtaLvlmA-AJwrCgCt7JGBVr8y0XdBPicOEjYJKvSgHqxjif1dMCgolx27f9O52ibMg60BSGxdSd8A2jX_12EN4Dv2zbx6vi_VeyO09HtFyUAt-_K2G2BxQfb9Yyftel2lHUh3oGZbfJUdZ96cnWwrTDTVH7EfazOJPQRhr32m7CTbmWr3hc_Y44CHjWOEtehWEa1vmGpIIlfeqKrg1kubuEZsticKwKBxkNE3YlD4wp_w0rf0GUbxqfbrku1kMshQTgR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyQYSzkZePY37hCLYNTp8JSyBJOHFzOZHAERF3awJP7i_BDhurP3C_Nkp4BNpWb3ywwiXEYS_Jwaw5bi8W7A3EomTSgd9hkMg6h1fM1v71wWY6rTQjEsxF-yi0kYMbH9LxNcr4w-v6hHa6_TL_8zbbc122zaWtzAkSuUMh37hWQChr6ZiwcSA0b-OX6-421VkuwOS0bQrOR6_55w6iAGQh9YMmJCexWvHzDJIW1c-8y2Iq78uqqJI9XPLCuMTCifPl1uLodqkzlyUtSqf83EvLPeB1cW3-83u4_zGgaJg9LHnwzgiM_GUqy5hN1FrIi5eTCzP8TT4s6daJV4H6zsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=FImfGC50En8oZyzsGTH3Uo_Pstkv_7jlVll1lEJfqn-nrnE8WnfWNMFANq2RmguZO8o-fpeTZ5L8LLX6Yop178TPVmqpxZeDZi4MaV2jAZMMgBND6WyhDUjQQx0RFpwod3ZDJ8YHGXJFYmalJ2R11NgVYaMuhWvXZaBPHD2-S_zXLRRbxy7hUEYADuuyFlB0hHOi-cLBLbY4xUpI_WzDghtGWtRYSEtgv13mzsxwXNhUtYtZUZsgZOlVhCXSrOQgVlCUQsZB0b8D5JlOQ_UN07nm1JvSEbmdrYkq0-5sPK5EnQ8THU806qNJVXsN152razMcvqqyikDi1vZ3RecLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=FImfGC50En8oZyzsGTH3Uo_Pstkv_7jlVll1lEJfqn-nrnE8WnfWNMFANq2RmguZO8o-fpeTZ5L8LLX6Yop178TPVmqpxZeDZi4MaV2jAZMMgBND6WyhDUjQQx0RFpwod3ZDJ8YHGXJFYmalJ2R11NgVYaMuhWvXZaBPHD2-S_zXLRRbxy7hUEYADuuyFlB0hHOi-cLBLbY4xUpI_WzDghtGWtRYSEtgv13mzsxwXNhUtYtZUZsgZOlVhCXSrOQgVlCUQsZB0b8D5JlOQ_UN07nm1JvSEbmdrYkq0-5sPK5EnQ8THU806qNJVXsN152razMcvqqyikDi1vZ3RecLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2OaFiH-oBSUAkxaen95XvutK_uLk1_3lN2RO7rdeJ4AKhC8Bn4c75VBEPkNaO5GAWUKR7r0oF3nGbD0VN-T4bM8Cn5R9T3q_fMWi53xcli_P0mRLeLMs4Qtj5KFyu3gDHYHyOTc49rNC_axsrdl2TAzFzWcXanygSM99c-fqSrqNdcX1NnPKPIrNyemJQHZQgYEAH-UWOK9yZ1cXzxZ7TQhWuUop3ySCTREk6KUYAKckbxP0koLQpaeRm05NAdCI0236enG84j6RDupHZhVzZI8l-Fd1Yv1cRcrRY6WARDmj8xMuuMZ5ldMRoV7gp_jmjBfB5yqsZmJ893xi4PwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=iKqFt1WEJ9Ny4g3OqaK2uwp7ow5cuRwKqut6YhLmXX6kb1baqj_tKrpffKsWGU6Kg2i8HqzXQhCCNHlTvgvmbUFjvLmACeslcLv_rWzwq8_mJ9BP60jtIUXR374m7vo-mDR14TlSN8B1J6XjeGw7G3qjpBU8HHw8TY2xNW-6Uv0UH1IpkIrLvHwjcDI7O6AwpJ3NjKOaBpNDemjpZOdexJhQsqKs-E6US4lkrWSosUbz336W-hvP6rhGzfuOjTATkKyF5BAMaXAhygNID_FrLJXtwgT2YmuqAogkkzgBW8jX67mluccz1sFmyy5xHeEAzppnrWqoZJ-xdGPQomhqE6VJXI1Kw4X61hiLYl-2HxGaSPa-d4zzfHWRWVndjQv2WBWO3-SPZonM-5qQ-AJhaOfz8V7OLYLhAxgLCGiVFpmboWlqAfGv8deakTRJiWbk7dsZzFjMPSyZBjhIZsorJ1aOiLf1ibc8KVX7OXKxpSj5MZAAm6YqmQk_hBy6MkV4AA6mVYXy-d3KEMi3XTpdu6sLMeKifgrMwNPDBuhv1IfocKDqvUeJhU_bcfipbQWj-_SUJGl6tXyXvI8NYmmeul_spLE8Aq-4iXz0Zj2jPl8LIyCvA0CCjgoHfMH_SxGIX3sfEw0UBq2qjRlzEgj2Ms4W1PGfx8Csfs_HLi70s7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=iKqFt1WEJ9Ny4g3OqaK2uwp7ow5cuRwKqut6YhLmXX6kb1baqj_tKrpffKsWGU6Kg2i8HqzXQhCCNHlTvgvmbUFjvLmACeslcLv_rWzwq8_mJ9BP60jtIUXR374m7vo-mDR14TlSN8B1J6XjeGw7G3qjpBU8HHw8TY2xNW-6Uv0UH1IpkIrLvHwjcDI7O6AwpJ3NjKOaBpNDemjpZOdexJhQsqKs-E6US4lkrWSosUbz336W-hvP6rhGzfuOjTATkKyF5BAMaXAhygNID_FrLJXtwgT2YmuqAogkkzgBW8jX67mluccz1sFmyy5xHeEAzppnrWqoZJ-xdGPQomhqE6VJXI1Kw4X61hiLYl-2HxGaSPa-d4zzfHWRWVndjQv2WBWO3-SPZonM-5qQ-AJhaOfz8V7OLYLhAxgLCGiVFpmboWlqAfGv8deakTRJiWbk7dsZzFjMPSyZBjhIZsorJ1aOiLf1ibc8KVX7OXKxpSj5MZAAm6YqmQk_hBy6MkV4AA6mVYXy-d3KEMi3XTpdu6sLMeKifgrMwNPDBuhv1IfocKDqvUeJhU_bcfipbQWj-_SUJGl6tXyXvI8NYmmeul_spLE8Aq-4iXz0Zj2jPl8LIyCvA0CCjgoHfMH_SxGIX3sfEw0UBq2qjRlzEgj2Ms4W1PGfx8Csfs_HLi70s7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=WIlAHAccyB0j_JIR_0HsbI5Ou7PQsffRlwp3SE2t8_IirP2eajLVShFpUxwOWX6jc9zqIen311iDQjHe1lWxJ4PGNw_ozU4-zLWFav54wzyru_sIIluPL0pbguxP17bd6rOmQ6HljYxafFVOrZjNOS5aDHj-3Ou9xl9n1dwlazh6AnXCqXKcUexYl-plGmJv6kSIL3vzotKyT2vv9USbCqNmFeNZwFaGpJvkSqsG-Bov02l2Dgw0r-SIizsp7gVWIm7pFFPR7P0K9wsL3D1Hi2RDjOtiiMQwah69dyXpntydcfkjE4pHyXXFaNkdZVbRDMv-SY76qq_7gn-LDPdFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=WIlAHAccyB0j_JIR_0HsbI5Ou7PQsffRlwp3SE2t8_IirP2eajLVShFpUxwOWX6jc9zqIen311iDQjHe1lWxJ4PGNw_ozU4-zLWFav54wzyru_sIIluPL0pbguxP17bd6rOmQ6HljYxafFVOrZjNOS5aDHj-3Ou9xl9n1dwlazh6AnXCqXKcUexYl-plGmJv6kSIL3vzotKyT2vv9USbCqNmFeNZwFaGpJvkSqsG-Bov02l2Dgw0r-SIizsp7gVWIm7pFFPR7P0K9wsL3D1Hi2RDjOtiiMQwah69dyXpntydcfkjE4pHyXXFaNkdZVbRDMv-SY76qq_7gn-LDPdFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSJ9Z03Llkm-mf43LWE6TIINVHnZWdwF4Y5cs46oxZd1om9cM6eZ7rXqvyLE94sGxK32Jpmuw55FkVC-nHb2ke3l_7wU3Fke6oVPGGUjaCRuu1vTZXC0uK8UjrvBbfDSz_A4NCyKrCyfShAyqAXpwqHjpaKuXmUusUMGktXbYzwy2ee52S5cRaeKOwfxCDyq1hUfoXIoQtd8f-YwVuy4fmu3z_-HYwDOdeOtj4jXhuzXV6B_S9rFinbTmULFcv8qJcEB2Bvd-DjphrBkrHa1PA4eD7e4n3x-JYs3jpYAVaCkCk0Wkv2jFu6dr1HuGIL7GSsyolpHa7Ols_q1Wg1yyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=tL50KmR_KJwvjPx2R-RwwjfOPek3Sx0ZhgRDjCSngL-IKpWm8oGE878MGOZS0fzTEpGawK-QmuGu2GVe3-pGHcG2OKFhyYG662NYA55im1Ecx9Ge3eeqA4TNxlOvIbf9Xm_mdyxyypeZUS1VXZz9PvblZrBcnCC8Nenqt-_59IOETg-vmAX9MmAIr-BT64hgELlLvtBaSOcLdrycptlpMN2cy9man2l6HJyWOy8uCgeqYvDsFP-Jw8O5cmOrl-yVU1gEZEWbFwP9D5aQBhdbIC4FsQIpIpb7hhdXaaReGVmUUOnPN0bQDYUdA9MXrZSapdOiFS5_0x25Hpyh5GMDxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=tL50KmR_KJwvjPx2R-RwwjfOPek3Sx0ZhgRDjCSngL-IKpWm8oGE878MGOZS0fzTEpGawK-QmuGu2GVe3-pGHcG2OKFhyYG662NYA55im1Ecx9Ge3eeqA4TNxlOvIbf9Xm_mdyxyypeZUS1VXZz9PvblZrBcnCC8Nenqt-_59IOETg-vmAX9MmAIr-BT64hgELlLvtBaSOcLdrycptlpMN2cy9man2l6HJyWOy8uCgeqYvDsFP-Jw8O5cmOrl-yVU1gEZEWbFwP9D5aQBhdbIC4FsQIpIpb7hhdXaaReGVmUUOnPN0bQDYUdA9MXrZSapdOiFS5_0x25Hpyh5GMDxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=L__Jbxb8_GkW4qYXsDipnnEvKdtg5mZHADO8aqjyU7c7Hilblq6HTKOkESV2d_3AuolX7cucYu_yBXFi7xV3uwX6v6IDv-BK_ZDxWakQXxjPdOaGPp6qUldMyUF8lZajOHK9U9XppzbJdilFqtCsWM6C8MoEFiVBsPVo5Oy2Ky3b_d4a5eevR-lFgJzRR5fTR0kiVp4d2Nk0HS8MlvO0e0pF30f50k7Gz9sSyRC1HQ0QDr9VRVDC-SpCmSSRit7UESLNTLA50ygI5WspS1VqUuXVN_kcsC9Yw468j9kV2I9Df1GxK42bsjljoIetlSWfmB02nK0nRflQObzDzZll_w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=L__Jbxb8_GkW4qYXsDipnnEvKdtg5mZHADO8aqjyU7c7Hilblq6HTKOkESV2d_3AuolX7cucYu_yBXFi7xV3uwX6v6IDv-BK_ZDxWakQXxjPdOaGPp6qUldMyUF8lZajOHK9U9XppzbJdilFqtCsWM6C8MoEFiVBsPVo5Oy2Ky3b_d4a5eevR-lFgJzRR5fTR0kiVp4d2Nk0HS8MlvO0e0pF30f50k7Gz9sSyRC1HQ0QDr9VRVDC-SpCmSSRit7UESLNTLA50ygI5WspS1VqUuXVN_kcsC9Yw468j9kV2I9Df1GxK42bsjljoIetlSWfmB02nK0nRflQObzDzZll_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFEngbKze60A75iKKuvIO6Ojw34YD0aTWrGUoAiTt02WcEHO-Id_jVGhHPfIFiOwI5e9kByILLaBWXTgdbIk9y0P0rf2ZEjGa36KL_iUq1FJ3ITYPxR0wYcdD33XYwzbxULzxjHIGcjIP-ZFd9-Gc7hu9NYgBZBodvMqTHUYaXhw3EyuZLtiUCBPj_I8hsfyDtPh8bLyz8L4pD-sIX7hKEI4Xu-YAgFyKWkfEXI7wuD1APSqtNY1xltPRVqyu_0Dk50bMzK4sNnsCc1yJXGYHnENnmNBD5_nDAw8BW423WOKdsDrwrXtD99qodTiEYcbONp9NhlQPkDllHQZLO4N6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=LwnomeGyewtKbjwqQA-__YxEtwqvFcYscwos0iBRyt5qoouhbXSnF1ty2L1WMWWRmxdRCLGDp9cdNc6qOgCyKcwfrsLr3Ce6SWf2HHskZ9gAvZF9YHH8elpvMPcrgBWD3aVghrwyO-RY6aJDD8Am-7ykrvIdTJoffskkvlh6n71ZulbDRiL6mTwYwvdcR4eTgo6ijXbZJ2b5EqWSQHHGq8oii4lg9ZxWgMel96HJGQxOP7QkxU6NTm-dRf8OYAfFv0mQRa_c8Xxs8DbKM3W1lJ5dmq4VFpeomCUX23i9XE_kimxgvMJl5P_T6J1Okx0K65Wy-nBtP3e-aVRLJ6_6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=LwnomeGyewtKbjwqQA-__YxEtwqvFcYscwos0iBRyt5qoouhbXSnF1ty2L1WMWWRmxdRCLGDp9cdNc6qOgCyKcwfrsLr3Ce6SWf2HHskZ9gAvZF9YHH8elpvMPcrgBWD3aVghrwyO-RY6aJDD8Am-7ykrvIdTJoffskkvlh6n71ZulbDRiL6mTwYwvdcR4eTgo6ijXbZJ2b5EqWSQHHGq8oii4lg9ZxWgMel96HJGQxOP7QkxU6NTm-dRf8OYAfFv0mQRa_c8Xxs8DbKM3W1lJ5dmq4VFpeomCUX23i9XE_kimxgvMJl5P_T6J1Okx0K65Wy-nBtP3e-aVRLJ6_6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSMqXxx3-pK12ed9jT1z13onUjhLgCHsdRxn5wqBRwdLSryScpWZKYDNxmOjOeh3TjbdiJTZyFlCNtOfxisxJ3kPw2aauMETJtoaB4rdndDnk54FHd9mXGvXvjh0D0kXWvp4ikxp5-Z8dPba-tNNpVWjcwiAGIioAO96Jchc3t0Y66ctMEieOMvqr8XNf6yL8tjzJq_paqgA9vyK0uYlFyh-dbv9R6EU3NqU-QYe89IMetRkpHtwcuANFnSiaxndvIgnfM7XIHYKmHmSH-JXY_CZAhiOh69KWq5OQuSXkFRV3HzPhUcMqjWnDZlYZYejHU6q9h4_MONWuyQCiJxUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
