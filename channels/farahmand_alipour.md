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
<img src="https://cdn4.telesco.pe/file/jWXPGVeNDJNu7KZoJPxhu9h7SB0oKcYWtXN6TM1cbmhYDyGV2qI0tjyCjcO73x0bx4xGJTS_EyPh-1nSQhJcRWG5ev_f1wCeo0Sh6gKtO9DCzR-FwAGre3XXC_NMJPsJQOsXoeVvD5svwWY3UW62fTTiwQlYWVw6LfjvmWBWVjUdJrbky4glOemIZ6FKJr3myCu1o0HH1uWp1pAndyUxUuNQNUUnX46OCwKhtlrJUIzJbq2qEA-kOHOiwWp0zJF4ftKLbmADDR1-dYPfxbBcfjNuDnMnb98dOEfKnYnfrQToKxVGq5hVBNQdEemU81UjDfkoxRjc5HhN_GK0CoGb7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpWKK1f6GSdx1XJYF6aT0hQmPwc12h1RS9u4c8-F-oCfckATc-AbLIo1g-1lSj1YbYnqLQn3NosFT-rtYTcQUqL6miPxg_TE-uxT6MEWOxB2wsgkMllbHGPHRduExqRsz-hkX63JKWvVHm_Jd2YeT_90fzVVIlGOftOKEkqBzj87KPPyBG2HeeEBE8xWv3nxIocGYAnzZQxHLbQkqL5bLxs8aZCHVczdFSCJW5-XiHv_6jABE7sNZiA2HA5ehl8xhy2MpR3a_S68Qt_4BNwkxdJnVOSsK7bGQZpavb6UFQaAOxWrFjo1rtVtjyuyN1bgQvhDGAAF9Rie3o6wx-5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQbr2QQISjVSia5hYpUZ8i9fYCdVLkSDje6yu5sne8rOE7svuV4afU3gQ-vIYkZ1LCPriPDcIPjLBQf6jP-rX1gvroTzLceNsmGaW9cyYvG7W3CNxGO6GHpL_zn1VMQ8xsLHtTeunRwcMvAW_B8ssGdpuMDRBhR8KFgNwT8pAdBRXJcXmTPNXMe6l_xg7OeyLg6M0FMNfGmiaZ5SrXzwAY0D783h2D0dfiUdar57sRIbVgVBvLFJ9_buGsu35IcbDRB6Cl0gJmVjduyLcB0XOoFL5xpZvpcAhXjNRAc7TW4AvzLZJ-k4x5y_5k1KX5ULDQUri7V1Ag1XInH93CvuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE3Cq2IarY8X-_Ou6fz_-qdBGWOOAVF32SgEn3wpQ7GxdTW9gJJMpVsTqkxf4WfRWLsiIC47_6L4dqaTawOmQ0EA_R6CvyqrgXe_0V6178I_-cWEtPwoPZ2qb3Do0qZ0xwmnFgG74TyLte6p3amF0VGUX5xff88KckCTAZwVwIdr6bNlBDONk98nNenh5ynX8fDU_RH5_5JMtLMGqjZX7znw2kWW5mnExr9dycuYTt3lEgX5PL0EbeUFsQ2o4oMmC_JI8rZ8Jv_5cWTImMpBaEelpQa28fYWLWiOKmpk_YpBh7lwD1kAwiWoq0BQeWL0lwESN2nkNvTWwPSIX__Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKSWjSmIZRGZCkiIdztiiXPmw7MI6TsWnzLxX_AJEyaXn6s1X9kzMjbMn30_ayUlpX43jgOi2hKsaylIDAERPdR9wiSz5wIZY5ruhOBz29lqEnvQ8OJA3QE3xoOOn07hJ7aPaXAstfulhyboeoyMGoOar8LOWvMcfcxoR66Axqafd-J0EBZkLg8Tgqglw7jCnAyFzoOgDi0j_ZqkFDps8E3JXU0zNqWCiK4fh1l6htJhQKhgNfpm6bWuusQnRQwpD1aIG4rIAakmimFuyal57AGRH7BjzW98Pm2p6etv_0cHru_OKew9GdlilnK61ISD1nMQic1SZi4rPobpk4Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=i2cePFwMNwWAoBTXsjaJSrSyUO2LHWL6UCtFDZj_qpD1S8MpHHymOqrQTJQUrl7hZ0Fq9sW-UsgwrGfbDqkWYOPpcBEIw2AGvZTCQO94mTCumSEK1gPMztWo5HNvyDDg3Mf8yoG_wAgdIvvf-EfdL026wf4bIHQr16Eax4w7R9HCTUnFWp7WOveUneBOuGR82AYI8zVfvRBdd__asNm9eSEQuLsdE0rbCzVMFcfMynsnD7PB9ohyfNCgcvAzaeufDzg5s-Mf0-Hy8YDhCSie4tshZKas-0ztLm2rOSedG0ZWcW85sfMCAQUAoDRpNTPNKzKSUOG-GZ7LkTkCcA8ChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=i2cePFwMNwWAoBTXsjaJSrSyUO2LHWL6UCtFDZj_qpD1S8MpHHymOqrQTJQUrl7hZ0Fq9sW-UsgwrGfbDqkWYOPpcBEIw2AGvZTCQO94mTCumSEK1gPMztWo5HNvyDDg3Mf8yoG_wAgdIvvf-EfdL026wf4bIHQr16Eax4w7R9HCTUnFWp7WOveUneBOuGR82AYI8zVfvRBdd__asNm9eSEQuLsdE0rbCzVMFcfMynsnD7PB9ohyfNCgcvAzaeufDzg5s-Mf0-Hy8YDhCSie4tshZKas-0ztLm2rOSedG0ZWcW85sfMCAQUAoDRpNTPNKzKSUOG-GZ7LkTkCcA8ChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoeSXsrBu2SwGXH3CORN6LJT0I3HJVRsecWcRwDcuwmM61kuIpJwmCsIjqY_HyhsP1NJARCH8-KbqoEC-QP_vzZ9umDgIGA0tXN2HBENxtpeLYltrkJYjq6_IxA6nn_qtHFjEvSZzE6Y4M_0qHPlI6AjztP6GeT02hGMCIix1MV91ceXI96bxKc1Z27gUAaPMkjjdMTAopFVNlQP5WuG--5w7imM3ZMlztQlSZUQg0O2IKUdu0qBSpNlkPakRKReK4gbVtMYS_ZcZDvNUdnQ0KGAu62YoM-bC0Quyox9YqjMKgFnmEWPj0DagW65aLGvxFdiFAoCXVBzZbLGdhOqUeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoeSXsrBu2SwGXH3CORN6LJT0I3HJVRsecWcRwDcuwmM61kuIpJwmCsIjqY_HyhsP1NJARCH8-KbqoEC-QP_vzZ9umDgIGA0tXN2HBENxtpeLYltrkJYjq6_IxA6nn_qtHFjEvSZzE6Y4M_0qHPlI6AjztP6GeT02hGMCIix1MV91ceXI96bxKc1Z27gUAaPMkjjdMTAopFVNlQP5WuG--5w7imM3ZMlztQlSZUQg0O2IKUdu0qBSpNlkPakRKReK4gbVtMYS_ZcZDvNUdnQ0KGAu62YoM-bC0Quyox9YqjMKgFnmEWPj0DagW65aLGvxFdiFAoCXVBzZbLGdhOqUeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQlqSADDudZDr2N-RkA7eaojGehR1i2Lx3mb6TZ8DeYP1HFTT9qNmNXgvS464_1WlIBBSgStUa_QNzaiRwl6-QZMtIeWKzBqvlqOcWVhOe1WsEe2BLiRK9hvWHr3O58npfT2M9FdFD8Y7caU5EXpv6TYyo4Y0vKj5Un_q6AZb_WIqxb2U4AesCXIT3q9Qry47VnFkM_xFbhfx4CgboOG8MIRzjMVnmOig7x8wYq2Ba8hdapniN9XwJCzdVMxkKNIqOvffxFMrqTESsFi4ptGdmMKneWbOR_5qd4jHJVMcU0GcoCHKaJl4vDgX_8m5iImIwpz8-x160hqdiLYEV8ZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Fw2mz7cubEnkPn7pzOQxOw7MOzFYNlLXQEYUadc1I_pQhb7MknJAtFlJNMuTKaB0JlWWrT20H8yEL2XId0U8kSDX7VsenAUJ7zARIVzQ50IPW-P6feHCLio4EdrGd7YP70L4ObHnFkORIandYmcEPT9JCBPw1xce1lODbeCAh-tQay1wIR9WgppQxRT03gcC5XN19xodmNOUJDGTWRUAKLuMwYPwfVB0tS3un9Kw8zQsNl_ptBahjvbtFhnq_dc-s004lR0LOJ7f-UwuT11LePUlOJKtUur174oJyfJ4ud8fbl3fMDmq-o65xbl9CDyibnplomB00pCtBdfJ7Z3BEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Fw2mz7cubEnkPn7pzOQxOw7MOzFYNlLXQEYUadc1I_pQhb7MknJAtFlJNMuTKaB0JlWWrT20H8yEL2XId0U8kSDX7VsenAUJ7zARIVzQ50IPW-P6feHCLio4EdrGd7YP70L4ObHnFkORIandYmcEPT9JCBPw1xce1lODbeCAh-tQay1wIR9WgppQxRT03gcC5XN19xodmNOUJDGTWRUAKLuMwYPwfVB0tS3un9Kw8zQsNl_ptBahjvbtFhnq_dc-s004lR0LOJ7f-UwuT11LePUlOJKtUur174oJyfJ4ud8fbl3fMDmq-o65xbl9CDyibnplomB00pCtBdfJ7Z3BEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8opU_9kQPkWAtFQdr0Uqjf0hWVkvX5wylE9q9xx56-9Q50MpfOvya_-HzZaCqckBC6w63-jhbRq6UHhjXFObHp9hDbU0FT4bY3a4T1LS-NIXG_LtdxhTU_bDdz50M5hwsT-sjfPPT1lf_iOqGDAKHW4vjznLhJnXMKQ5T92Rel1OxWsQdVfMY_KBszVaSaKmTzcSImANlDUqK-J3hpInzTKcZ_rSejEMZxDNSldR4rI8At2ngztHQ7Wbh7L62Qd3hfIXpSUoNA__GQmb6QYAco-vzY9fXOl4tf6J04E-RaoznUKuk6Wu5ATmxf6sncbgyWSnBy-oj93mUAHs3zOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=S0eeN1dyfV82ffl5J89LIGAUvESg8DI9RKnWGvvyTJNNrYhp4cBqkXuHP8Ay-RHZRVmdDRDVn3_vjUqMKFRl34d2WIm-yWZUInpAYpkn0GIZVlwqfiU57DAcxT7Mxvbsyk6TpYPtG0_5YNQymn2ZeoYAJxyJwAfh9YARGYzEC7OcYan5OeyFw4Bpi2oRSGXv1Oi7McBvKii8Z3C9Uh5cYrR_YVytg11eRg34Fgx3QVYGZ3jHJu3RAriCbo8WOqBiJN3lp4jLTTmenNLp7N0TfjPjqcv-sLtflkrCXW0y7A9XuRjR0P-Dc4k10TNiYbqG9EFwym6XwO0PKAk673UBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=S0eeN1dyfV82ffl5J89LIGAUvESg8DI9RKnWGvvyTJNNrYhp4cBqkXuHP8Ay-RHZRVmdDRDVn3_vjUqMKFRl34d2WIm-yWZUInpAYpkn0GIZVlwqfiU57DAcxT7Mxvbsyk6TpYPtG0_5YNQymn2ZeoYAJxyJwAfh9YARGYzEC7OcYan5OeyFw4Bpi2oRSGXv1Oi7McBvKii8Z3C9Uh5cYrR_YVytg11eRg34Fgx3QVYGZ3jHJu3RAriCbo8WOqBiJN3lp4jLTTmenNLp7N0TfjPjqcv-sLtflkrCXW0y7A9XuRjR0P-Dc4k10TNiYbqG9EFwym6XwO0PKAk673UBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h6dkVZ6lc01YXaxYV5WjntUAqLg0DzhOZwYwG2XkP-9wOTJBTFeCac0ze-TbwLbVSeJhNYOK0i5ohuJjC5Ot8OyXMYz4pb3dg5G4HA8fpPBFEApXT_INT0hkmuElTRbNXFXXKp8h_EFQNRyNjWRO-LjsK5iSdo_XZ71RGRDEKuWbxvJvOn1l6nxXxiixu78c6xwDP3Y8z6cxqfzqv_uL_NoXs3s_iDkNpTEiEiW7hU9RiBDsu8yXTKEhBntUr6IuHlUITdlzgRXYHDU45x10pWQgtIcr-5B_bkbN-S1KmBGJ9azactHIeyBuMJXiLiNRi2rbOiHfEFUk_WMm8LdJxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h6dkVZ6lc01YXaxYV5WjntUAqLg0DzhOZwYwG2XkP-9wOTJBTFeCac0ze-TbwLbVSeJhNYOK0i5ohuJjC5Ot8OyXMYz4pb3dg5G4HA8fpPBFEApXT_INT0hkmuElTRbNXFXXKp8h_EFQNRyNjWRO-LjsK5iSdo_XZ71RGRDEKuWbxvJvOn1l6nxXxiixu78c6xwDP3Y8z6cxqfzqv_uL_NoXs3s_iDkNpTEiEiW7hU9RiBDsu8yXTKEhBntUr6IuHlUITdlzgRXYHDU45x10pWQgtIcr-5B_bkbN-S1KmBGJ9azactHIeyBuMJXiLiNRi2rbOiHfEFUk_WMm8LdJxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=rddUGxWMOnUkOIyYGTUZZT_eU9z4ohHqFVXTC1LgOS8xIYeBm3DOBAaUo1MW59F7VMhoZiy5664qzzSKRAMY3fIUTtlAXtkndra0ygo3n6nXrFJAcVpk1zjiG8g_xkTuByDg3esjqha2VlEPdvTAYqHCLNDFJArdMPlY2bxCH_Sa5CGsg5EeoS6j48XzJao5guZWribmdRYr_7RiqAvwwUmJ3MyrCLKnwNG9vFcaoCqozmfS1hyQWc69P1Nn1u_L5c6DjF-2aC83MPdkkCs8__1chXJ3FMeK08645Tr51v2vb37GatTRe9MhUlgehaQ2ujEe_bRCJadYv7Ka7wJs4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=rddUGxWMOnUkOIyYGTUZZT_eU9z4ohHqFVXTC1LgOS8xIYeBm3DOBAaUo1MW59F7VMhoZiy5664qzzSKRAMY3fIUTtlAXtkndra0ygo3n6nXrFJAcVpk1zjiG8g_xkTuByDg3esjqha2VlEPdvTAYqHCLNDFJArdMPlY2bxCH_Sa5CGsg5EeoS6j48XzJao5guZWribmdRYr_7RiqAvwwUmJ3MyrCLKnwNG9vFcaoCqozmfS1hyQWc69P1Nn1u_L5c6DjF-2aC83MPdkkCs8__1chXJ3FMeK08645Tr51v2vb37GatTRe9MhUlgehaQ2ujEe_bRCJadYv7Ka7wJs4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sXAk9_eWCxaiAjORqO1YV8Gkx7zKeTPTCgiEO4gTwyMhlhaA7G_pTqKMs_wjLjkV1tjX8vmcltONhkHVzYh2MmnK8cp9xhnGtFOn9wFmEsOeYPYno5bw15M2sp-AqrkmwrJfDRLAvD7ZRD_9_MX0lbukAcEm538EKZcaJdZ9bGOg1owVXW5yzFG08kwq9CQAhzAQWBNgC35oa-OgNmJ9OntiKO4bAIySJUl9RRfMBYcsM0u4T7NHLsQVcYs1iJ9f9v4uBviIqjiH__QMS9qt6c-TlC2hUmNPmQnotWr1_k6kCoaFy3cVNO6PiimfZjhpvR3VDZBYjj-kbVhR3mHGRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sXAk9_eWCxaiAjORqO1YV8Gkx7zKeTPTCgiEO4gTwyMhlhaA7G_pTqKMs_wjLjkV1tjX8vmcltONhkHVzYh2MmnK8cp9xhnGtFOn9wFmEsOeYPYno5bw15M2sp-AqrkmwrJfDRLAvD7ZRD_9_MX0lbukAcEm538EKZcaJdZ9bGOg1owVXW5yzFG08kwq9CQAhzAQWBNgC35oa-OgNmJ9OntiKO4bAIySJUl9RRfMBYcsM0u4T7NHLsQVcYs1iJ9f9v4uBviIqjiH__QMS9qt6c-TlC2hUmNPmQnotWr1_k6kCoaFy3cVNO6PiimfZjhpvR3VDZBYjj-kbVhR3mHGRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjStbH0j4Q1yn0BWhdcSLkD0HvX__UN2QBrkxN9c25xmNN7dC3cgjUu8SrcWZ1DQrFZxQmxzyi5LOKI29N6_f6eZeYgXOesvoTwvht_tyDMI4i92T8-2CSLKmzQaOGTafAyLZwrIk87mzS8BK5OfYQNcNenVlx7qAX55ETMDfjH6VJOEV3F0_SujYE4x1aLNwBAJEIx4ETMNeENLGHBXZeLfMhQ-h5sjj9FMajKbAuAKZp_9Ho_HdE30Ls_Ye4TSodzJmiYwk4csm-v6PO9qGYR6Klgte6Nc9i60mtk87_y_0OaXH9o74RejNaZDGVrDKt2m-rzxU02ILbFj8xXYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI7C46wIX2aQDZjfSW4QknPn4JHh4yhMLboj-emW3CBmHbuxDAJU5Z4r4jexNZO1tnboBWLJMUUY8REBVlbpi1IipbRt0zL0ggRrMC2M8RBYfqYqlvQFE1uMQD4F0zlGju9Pg-v9SLfvZTKowPgZZeZOGEi3q358YQOIlx4c4Q5c29F3auoNI9VYo0rg1uJmdowXL8CIhow627Ep6jS8K8ru93KRNouW_rt4bz-L6bDds8fsIiSKVU6XzP3BX6JGOK-gH2lKOY9c367PN-fZ-wEYchMCBsKhY_8FxbTUFXs3QbwFpNmqt3LFfOAXJHYEb_WrLb6aT-EVm9TAbvyuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckGLGRoSkoOijXv8kricTBbTAjWEIH1fkVgUzLL5UkPnn-sOo51tMLMW4LimawDP6vpm3UHqJU2emKvNQit2wSAxNWZVCFZ9LjNVe1gTxfNUWJlC5eOCkvWKiN5MzySzkKDAsDaw9u22pvr7iLz5OXAHiuyNzumXu6zs0GSTiToTv-wedaTsnNSwemeGwDMeJ-XSp5ttO3wHTRxr60I5cMbWCnOYOMzWIHDQOp5vJiDpHJ9WtyLT7XhbGMqCkh5cXhurRjdzh2jporDb82K4AUpfgBa3vRKmDNy2n4rLNfeu4i4aG12CzNn0NT0bQS3El0PI4Nk3R3d76GqvSqGO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=QLDunqQ4ZqwYYd8wmFqcqKXx8CsM26_E-65mXDrsFxmKBByLWZ21GMcadzDGq3K2rLxxUEYwwKDOnxIte_Am5TwtnfzEsqDMUMDom6Nw6b7hitqnAFBao6n3Y2_I4ImU651pwJq4zRkH5mxxqyS3mIzQn49twQAVdnvnzu8xQ8T4eHtUx467jXISXei05hsJr2bvsf_q2LcxyM5_V6Clobk-HsRudgQ6amDhXgm5m8UQOFIC15tRNEQCaGQnk09yw9TvCTYfwLta39ZiGAtk_Y9NAubxPUVY4ljQ3Dd4KVDgmdLtytS89wnGXHpK1r2hSjb1hSYvnKInezjxFN9Uiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=QLDunqQ4ZqwYYd8wmFqcqKXx8CsM26_E-65mXDrsFxmKBByLWZ21GMcadzDGq3K2rLxxUEYwwKDOnxIte_Am5TwtnfzEsqDMUMDom6Nw6b7hitqnAFBao6n3Y2_I4ImU651pwJq4zRkH5mxxqyS3mIzQn49twQAVdnvnzu8xQ8T4eHtUx467jXISXei05hsJr2bvsf_q2LcxyM5_V6Clobk-HsRudgQ6amDhXgm5m8UQOFIC15tRNEQCaGQnk09yw9TvCTYfwLta39ZiGAtk_Y9NAubxPUVY4ljQ3Dd4KVDgmdLtytS89wnGXHpK1r2hSjb1hSYvnKInezjxFN9Uiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pliJhZ00wPP0ZICYUEOD4shK5EmLmQWOJ8MiqJmm6BrTnnKZjPNQ5a0szyAFGLfw_5ZhY9_ENBs5z3SONIP8EhOWD03QGHQKh0U9xembbovYJm-1juipNCuDeNzXZNtuHmaDCYvTAijPKMIozDBpk-IJHSmgR7OE-1YJV8yAuowdhIOgfwamkYDfmerSLH5s1DWBNCuGtWqop_eQgikXAE8XNjS_gT1KkV05I9AQW9yOZT9GkTlMNVidThxOKlgGWIR053X3DCnrOkEQkKEwxfqnX2Dkq8jmRmesApiGasgKbozCFvEbNMxozOl4KoBZtvIE5yBokyzdaR8YZtyxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=v2_ulxziWZskEdsOgIrLgS6FJ8EAFlpwdN-Ar104mAbqyaLVtTxbhaExVsgz2BBrfS-2Pa4uc0egaYRJwji1bX0VfTvT2SAXw0jojBfz01WH3OVx4hLuuyGB-z-ORpLIuCsiRA4IvxYAvd6EElfxH4Xdu3cOgralhjGedrGSd_oxSQauLA_tcQJvuTZet0Xps9sPYwU3ptrog3lOqRzq0Ptc3_GIA_Lx4DRzF_MSwM0zP2KUdnqvCSwQowrWTxOBOtYfuygvEp2jc-7guARI4xaSSpmYUbfRWdqxeIsZqiZKqfLDQGWo422lhSwXhp0oia8-1GgGwT6NC6fUFw8YQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=v2_ulxziWZskEdsOgIrLgS6FJ8EAFlpwdN-Ar104mAbqyaLVtTxbhaExVsgz2BBrfS-2Pa4uc0egaYRJwji1bX0VfTvT2SAXw0jojBfz01WH3OVx4hLuuyGB-z-ORpLIuCsiRA4IvxYAvd6EElfxH4Xdu3cOgralhjGedrGSd_oxSQauLA_tcQJvuTZet0Xps9sPYwU3ptrog3lOqRzq0Ptc3_GIA_Lx4DRzF_MSwM0zP2KUdnqvCSwQowrWTxOBOtYfuygvEp2jc-7guARI4xaSSpmYUbfRWdqxeIsZqiZKqfLDQGWo422lhSwXhp0oia8-1GgGwT6NC6fUFw8YQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFzf6_GqqHfQMk9HU2nl_S3tQ8VSCFFvEqmACAzXw1NDvYp7YUkLHKix7gE5SmvZXdZX5tyFtBow7afuT4b69zhs7vQQdnZjs5Lui0k4P0ZBh1BMuEHHqqq5D8_O06qKH4dsvQyEmzZhMitvh-m6U7Th2hmE8U3X8Jk_pKN2Iydk0emAhOptGuWY_wSGpVaVsPMNK6nEr_jP1zf_W_A18WPJ0Yo-SnJOkMjVKykKIGSrk8E3MjKKzajQEfAgDiYpYdS_xtQL6dfrw94yKSAB_tEFV-GSsRjDP83Lv6surRF8FJjR-dMpHG3dHDamCuxqSSBof7M1LAkIQeV6NRhTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kC4ktYoRVJeO11qYOi4WwEyMvrQ5B27gJ6u-rHojQh6MHiwixGiMc3horxwLxvrmdwRP3FdpLRj-BzhUuuGhNy7B4bnGCgU7f61iKZAiseI8X5PCHFVNZe2AJXhZQa-Miq5Z567knN22s9LzJoybDqa8qIhYCXq9_E6Kkma1GlIZyUGIBWJjq4n1AifUQW9FNzkomL9RFAbmTBXIjcgukVJ2lvrCFQl_lGFfDWBCpW7Z496iswV7SqKSM9d64hc8VDIdmkj7Z-usLYoU4R_TTdi7vtN2fWqLg6HaaDSdDEE5t_FOQ1LIU1Y-07EkUvoAEKGclPCk5dBRDjUDQq3ZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=CTMRHLcw8pn_aKsJOdDPAd34A6LXcYc3gjsk4Mct4U-FhNaHqd6RgfMgFG2ZGZLqdGGWHuH46ekanv4pPx7_TCIh22jjTUSqYQbstcksf9uTJtv02nZWhbWovt1iSd7ZqCDi5q3e-ssqACzJyqfE36fY1J4yFRQFX4Ul_enslQ7oEau4gwPPU1nbl3B6fDVMyiw4rLujV4Hz2upJ1zuNmv-O0BrOQLCnplKx-gi1DmuJwpj45Qi5lAYvoh0blBK62HMEyZ1bX03Hggub6ouB_iGoKI0EcLFSJpGJKVXslEBaUHxl0-WfJhgIxe53cyFS4y48f-KTZwFk6fL-k7kKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=CTMRHLcw8pn_aKsJOdDPAd34A6LXcYc3gjsk4Mct4U-FhNaHqd6RgfMgFG2ZGZLqdGGWHuH46ekanv4pPx7_TCIh22jjTUSqYQbstcksf9uTJtv02nZWhbWovt1iSd7ZqCDi5q3e-ssqACzJyqfE36fY1J4yFRQFX4Ul_enslQ7oEau4gwPPU1nbl3B6fDVMyiw4rLujV4Hz2upJ1zuNmv-O0BrOQLCnplKx-gi1DmuJwpj45Qi5lAYvoh0blBK62HMEyZ1bX03Hggub6ouB_iGoKI0EcLFSJpGJKVXslEBaUHxl0-WfJhgIxe53cyFS4y48f-KTZwFk6fL-k7kKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4b4xy1qH_sSB2bTmMkwK-vPTDSmKiOBXmi4McboNh1NK0U9o-L9Ckoa2ynyDJgs9PvsHOO86f36wiw22HbvteU5pUK6iser1in3zgRvxV_t-AQ9vkNURxUq-3RzWJverhxIv2WtsGwfNmxabmOScJTOUXt4Lg1GGg-Ktu3yIwr_9ETSDgDl8Hw8yPf_GToOoJoRl5sqF0LsnIRolpO6Dzw2xWwHs2iTSfUBzg1bQ1y1-MVFErz6xA8j_AVLeWtywfM-jtvRhbGOFbRFD-G4xvbMXke_btwciUbA-p7uidV6jv49xhLEY9j04Ihijhgxx7tciXl2EDsr9UwPLxBsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLCO_kjuVo996kV-6PwN6P3qyLgdrXBosu6B5lbCrjtjki5KxpicQ7vTIDUBbT2zBX7PSaVEAs66j4dxxk2pfFMxWN6a0yUaXU_bmaTxk3_f4BpGZPPr8gV65e1vqRCNMD-NdmC1ROuWojG4gF-fvyBNQXFMZx5Xd_R2foFK-ia-AMK72HjlWmIS52kk_CPHZEUWi3sHLagGhKys2N4XW9LP4nAQDJpBhGj6jgW6SI-5J1LHiO3ltmZOBri2wQcrkTQw-o5ZKK7F_26CQPZXr47_UD_wtejEQfGZ1SwCCs07H6D66h8ANiCbUD6QkvxtDdtYp2maVexcL6Sn0EsyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oawJeQfPyoYkCYewyU1XyYgaRWUOBwXJvp8PvEKNdzFE1rWP_-xXVSRej8EGtdE68YhKqOfXduDYix8BUv5UkQN6go9mdV8DmuYbjXW-aEqIgAZZcqsKdwQyXeo7JCmmKcGRboNFaGePthzPbGTp9DsOQnUMnP7dNU8HAnyUu_I9FBLtrSNxCYvbyFAw1076BK1dxCLEwo-P9-AsVnWflsCNOOus_MZHfwKBPM-QOnpNqBKLSH0OzIFmgdVYV7ZJcz8ZhrOMjuC4BNj8JefkzRUySJWwAY5UW_TBHO2PldpvM1xNlNzBmGtKUkMkEW8yCfaCJBzDSnPgJbIvNfiSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra7Lxx02cLrFlWI0o1uyE9Zw50l3g-lzwK10F8Gfl0kM15ln1uiyayortgVdFwqvRspSdprnmGsVdpU5nSCfmYZOb__phwU0fxXyUNrhMs1__7srutSNYfKFpGtaE5VpLbxyx5eBokJkvPJZO7DnCCjigeK3T0BcKND8oyMqSG0lT_WjJOMym_dUQsp3ZzF24ak4rcRyr6ZhUeaBa2Nkhq19E0UpDKbxiH96aBWZtNpnD3eKFhDgvALm9IZV98CIT07jtbbp9EzYPUzXeUuWLGqCJ8MmrxERMtdiWTNAVLqkWRmo7U_SLfrHjIldG6glVi6VU4iaC5tjkqP9lFDWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReyWFeeiylgenyS0isXo0IMTX_t_Htqs4ZXSBakLTGsZLqQI0TTZI7GAIe82e-KrJUch2bWhSp6ma2gVKM1fxKDRi8pbEA-RpYzzUqA6Lk2UOJveWkI5-UIg4-Ib9_3XrLcp-mbd1uK44oxBmQm5LwxtbOSRQv0QMl870TblvRRSdzu_MM9-7nNcT5Zv2B5P2aOpCdkn5dFQrTXf9PsWDOLAmscwS6-2xD4lAlxt7tqXY04foR4xe5sNJ2tMTZKPUZBUcuewm12TlGgwAXNhzCZKN8qjJ1bfjVfIakjVvtjdO7Fds5ksMMI78AZgRIMEDWsbGbskKDLD1BOw1WJ87g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_qwPeFKEl4lkgonXkJmA92SUFG0RSYXEXdzdrm7oKxmaQf-GbQBe2Rs5J98YGD6UzTZFT6rePP9SMrPjTA1kDlwE7OggYrb3rfXd8H0u2y0mwyEpnsPMEdAj0zM4-IL5MOZjLxGfczkW55cAMqR1AMiQ0Emnm3szsWjuL8ZuVCffBiOOaufz2wc3PtDufxOI9y246T30V4CLDpSXdrzkrCG-tY7JL5E6WVrt3fnV6tNjmBRw0tR0k-3lz1qfZ8ozgQOTC-65t_ZPJiXqqQzYpAZtr0xOusL_h-USqcR775ngfvD1qorWZqTmOFgqJ9v785j4ESGYqu1jQK3Yfs7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=VDf00E_NvbE9MiCRxQRTgAo-keFoN4B09H5ofM2NCP0JPsbtLEBGuIvOW02Fve1ankpoQ39hCaC3Fvv_41K40WuqoTYEhHE50DJmcyjvKsG8GvF7dqU4e4wkT449N3BFNnDZVlCJ5-wogFiSy4S3Q-DXjgKM08r1_f0ii9gb6dxUVSNE20iP6aj0jAMndolQ19tQ4dAaP4OnVDTIFTmOsOkOPilnXj3QcBw91ogPnyo1krLYLt7kLVZha06a2rpx1JfZ7a1CSQ5YmIC0BHBH2pbvfegCvRKfclJw1GZ7ej2ij9AkRjCzwqeQm-FTrITaV3AfeB4td-XPSntLv3uNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=VDf00E_NvbE9MiCRxQRTgAo-keFoN4B09H5ofM2NCP0JPsbtLEBGuIvOW02Fve1ankpoQ39hCaC3Fvv_41K40WuqoTYEhHE50DJmcyjvKsG8GvF7dqU4e4wkT449N3BFNnDZVlCJ5-wogFiSy4S3Q-DXjgKM08r1_f0ii9gb6dxUVSNE20iP6aj0jAMndolQ19tQ4dAaP4OnVDTIFTmOsOkOPilnXj3QcBw91ogPnyo1krLYLt7kLVZha06a2rpx1JfZ7a1CSQ5YmIC0BHBH2pbvfegCvRKfclJw1GZ7ej2ij9AkRjCzwqeQm-FTrITaV3AfeB4td-XPSntLv3uNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZwMU2DleDtAzsr1UB15ZMcoJkvtq7va1ayysZleGRQVx6AcQj6pHYjpLIt_oJM7dsvroF1U6kyaS_Mf2O8Q-6JZuFESr65aPIJGs44t2ssEzPCwzv8nUdoUhTm4pDiYsuuvk0zciRHJ3fYEy1RWNNoIK_RR0CgB2CwTLZI_gX5wq6iC_HG8JGUf__2oSlugbIPZIxpofVdWjR2GmN5XpQD1JODWJQhtP-jYEgtyfo1vpsonuoqAt5DdB63wZOijE3O-b_HV2bjthwWmJ5iAhWYfElo0ZOf9Z_eO2pjuYXc49RJvnyYYdkZqsi-H-CeBtxwjeV6zi6T8jirM0WDFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=iIoiP6oJ9FCqLU0fh-Xpw1UM2_E4E_XNBkZVYsfzdyhmfCDv1CZIHsD3TgTm6qgJiafvU7ua-mpwkPNF6YlWBm9ys1RyFpxTfhYCYTpIk67L-M51APLRpBBEYpmfxdDYEhm_vhYZBzQZuEdursoaCzs7AIUMygUKH9aZdX7TD9CzdqppH_PFyUPyBL4s27PlHUveaLZ5A3sfSSJ_bNI3E1y98o1a8LscrRHYLLt1QZuR5HwCZVzJb9GPXd6v-l-qTkV7lPqLJ6Pgje1wx4hRW7rRuvsKrkoC4bv6hxvZj555Ocmk0m8wvw6b1ahLEeJsDyXoraKG2ry2oCc3C1LrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=iIoiP6oJ9FCqLU0fh-Xpw1UM2_E4E_XNBkZVYsfzdyhmfCDv1CZIHsD3TgTm6qgJiafvU7ua-mpwkPNF6YlWBm9ys1RyFpxTfhYCYTpIk67L-M51APLRpBBEYpmfxdDYEhm_vhYZBzQZuEdursoaCzs7AIUMygUKH9aZdX7TD9CzdqppH_PFyUPyBL4s27PlHUveaLZ5A3sfSSJ_bNI3E1y98o1a8LscrRHYLLt1QZuR5HwCZVzJb9GPXd6v-l-qTkV7lPqLJ6Pgje1wx4hRW7rRuvsKrkoC4bv6hxvZj555Ocmk0m8wvw6b1ahLEeJsDyXoraKG2ry2oCc3C1LrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=RaQLLiLGSIPBYaK_6P0yiJuCQeGcXEDXEz11MEXZk4INkR5e6tbibXQhabecn_lu__w8W4WMgZYjdRQBi6KRgsD47psaDGms6trPqIvBiwriLqgIX25wSQ55SiX3rNhLWEju9eGr0QIp3pBWHaX2wqvb6BeKQ1BRz_kskGd-t_sFHB5OO93UGHf93RHzaqDLJdocAegeS3N41S7gKIIiMJysrIP8Id-seKq-1aupjCWTJ89H6ur_EjAiML8QitOvM2n4ARUOeinqwHEBci-okzX3JJzXZNvO2qMY4zE2JJHFfgL4WGa5NDzyzSGxzd2uHizGxp1Xn5MJkWMadBGWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=RaQLLiLGSIPBYaK_6P0yiJuCQeGcXEDXEz11MEXZk4INkR5e6tbibXQhabecn_lu__w8W4WMgZYjdRQBi6KRgsD47psaDGms6trPqIvBiwriLqgIX25wSQ55SiX3rNhLWEju9eGr0QIp3pBWHaX2wqvb6BeKQ1BRz_kskGd-t_sFHB5OO93UGHf93RHzaqDLJdocAegeS3N41S7gKIIiMJysrIP8Id-seKq-1aupjCWTJ89H6ur_EjAiML8QitOvM2n4ARUOeinqwHEBci-okzX3JJzXZNvO2qMY4zE2JJHFfgL4WGa5NDzyzSGxzd2uHizGxp1Xn5MJkWMadBGWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw1AHGgD0cYwLKV8sDT7bq2IfZpG1OcvQwzpZmW6RhQBNJgqraXAgKEvzQGOWZ7_NWgshuXc5yzUrImgQOt8VFvSEAhPJYLQDZ0uEiBvErog0k88FCvU9w6XCj8-afECK0k61CKlYQP5U2i5wJ8aP_cynBRWvrwiVp_LJ7yJ3nmw-A_2RcrYIY_2L-knSYVm62KuVsiWv0H7nipkB5HZwsoUeNhs8YW8u8DbayNuQAkcY13IkRchKBuRXf7BaREmFIJhkhP5aFHC6Smmwk_TEEJp27qdGgJLpxduOj-w3T1QAaNmhECsD_rdxPGWPdRgWuHCahpl_osfkuGqICgC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=HtTqxD-EC9h_aH1blXgUDHKp50-rx5ztXymIhX5DkJTTyfCR5UntM1PI3pV-SFqxYB1f2ddx-IWfFXRxArbvxqornxvrQd8Y3dPuz1GcRmce_v8zu7Qg69gs-zsuF-ZYOZCckVXQAuRWgp5aHQ8HgPuQtM5sJ9gIrJWHwyO3DtvEoTIiM9KFgpy4sOIr3p6pA0jqMducmZZgU2evCTVGAlCy88rww2NZ0En2dQxtTvzd83LZp09p7yXrk7qqhY9BU7f6G4vN7IaJQUgl0lVsKHCeLs3VViDfOvC3JQwOWcCkbgzNTKZTZKi14zkkFK6q3x2zyk4f80Erxe3lG6E19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=HtTqxD-EC9h_aH1blXgUDHKp50-rx5ztXymIhX5DkJTTyfCR5UntM1PI3pV-SFqxYB1f2ddx-IWfFXRxArbvxqornxvrQd8Y3dPuz1GcRmce_v8zu7Qg69gs-zsuF-ZYOZCckVXQAuRWgp5aHQ8HgPuQtM5sJ9gIrJWHwyO3DtvEoTIiM9KFgpy4sOIr3p6pA0jqMducmZZgU2evCTVGAlCy88rww2NZ0En2dQxtTvzd83LZp09p7yXrk7qqhY9BU7f6G4vN7IaJQUgl0lVsKHCeLs3VViDfOvC3JQwOWcCkbgzNTKZTZKi14zkkFK6q3x2zyk4f80Erxe3lG6E19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq8ypLHq-GThyb8yRdkqYBjcD44TdUwqKeqS2-YQfDHtVRxcTO19SC9Ts2i7wayP9aqzXTIDcR0G6p5RBJNXMF0xaiPRFRetLbecMi3Z_VMqDdKeTawbZSehCLYFLyfYgwiuYt1P6rPhnDJtXnkxi5TJlOBM-tg1mIuGSijhpnR0K9rpDG_dgE_yVqQD3EoEooACZassUNjWxTxOIeFTSKlWmtYCVrcnjV0s84ILsPjnvEyf4fYrxX-_oHkFF35dX6S5lcNHSYgV_eeU18vSesD4_mVwWrIIpVSN59xNvECg_5FT-TKxNWL21cGtFdNc7g7AKLfJoCEEW4_KQ7GjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2uPdUz6lyljY1w0P7Krq6BFJXBl4qIkQ5hm5Cp5gOZfXXtJRqtEwqdAw-JLYnEzrO2DLEzuFKjc6_kSLfpKsVoXwGIFhjF1vy3oppSy7wChYoynnSgr2OrPyZ8lqKXV0QWSObWf4ubvDLlEAT0WEi-cEsYmsN1AkaglM0A7JMMOiPzGi6rq8tM5jsSYEQb3MpftsVRjIlXBWuLvTb0wRACS8yPgTcQLgsPO7evA7alURdWZ4jByYXHgdKUDndD0ZXjJCpbEJkypSI2czuX2LXynkAtQcx1xtRNx5aKXJFGNS5mrwoTnhDi4JeF46JcjJ9b-GZ1i8oXUjpY542q8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BStf23lZB3e15kgcs8g_sgbHscpYgIZFVu0D3YHSQyREQLTiaPw07FB_HnzYBdvt3ny0uEam7QIjWEwlIRjeglrSZXYY8V_TEsrjF1Id9YW3mPhrLugRiXfxt9aQDgcQo3HYPvehCss9LWS5V1s0K1lR_9WJAIwHCq032Tuw49KRqYe8epUfpNmIZuvOPHl3LSQ-viFdLm8YwCflrzp5qADOZhoJM-z-pX--hE0f8E6WiOQ6gi49bINIIBhHZVHZtw467Su7jKmOg-Uxzz3qd1cEEEy6ggVVf0ffFlBKA85NDBrSXjvCnon1ZJeRsbzjfiFGfDWMoOp6FqsFn3s4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmAlhbJYNaU6xfDg7o5XxzyQMPz9yNMdbP9UGLzVJ-aJ78REYSQy_DCAnxD833C8VG8J65T5alClmO7y81b5WJOecdUb-LhMtXffGJPtZOET4JdZKRmUT28IjuulMBYgdt4dP25bwFo2eNL--IlW-ZGnlP4lQ0AThqJ8qgrlkxEJ2lA7Np9kvfQNf6nLL605Uebw8cp6fjCQicz2hsiHL8Od8I1EDfXl5YNMT7m6VJ4Dwz1TN5M_ga8Yk7z7KPRvY2a6oagnQKDOkwtqEBlTJ-sMOJnSCXZkmGKYPVCA1iMueGsB4lJKY2X5ymT3l2eHyYc0UVxKfzGfFxAzGyLQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a78_IPF8cMbo6jpWsLXlsAnSsXiTekiZr5-dkgAts3IpmB797RBQ6YDq2-3u-Nqy8EwNkt4Tf-_IHdaI7z9eggAuALkyjI5z95ZveFaQz6Nf8YV7cY3g2MQOq7BWo28QqqI-uF36um2thsxBe1HqfsDj2BijaNqKIT0lzhYBrY_0_O0I2__-fJVvcXNBZKMdaQWmkARulx6VY2grt63xcEcL7P4h9JMB7vvmoMgry-TMDGMLnP561nUSXKK660AbzpHDI1DxYe_boh16qgRh4SUTyN4uDOG1geMXP0rb39mdfNK8kKnvZJTuH_SERoZUzRbJNwDe9IRjzXIB7oaUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkGNhhZVnMJrAGYUKTJF26xF7AiTkHpDYkeBE23aAxMaCDrp0huPAwYP6WBR4YlJNy4U0GVAgQxOuX5s7-QF0KBtu8tGB_nWywX2gOwcCu8aY13x6qFmQ1MVzR5i4wRcrxM4NqRWCk6aCGzbA26h8QuXPcdyIrrSBhflUdHnq6iBB-kN0tJ6BAyrC_Ja9E-a5RjDVsFw4u7vYKpXAPs7Ugmr8Ht0By57SC5-7t3Gpm36xwZCNE2WfBsR5GcAHxizTq9om-wqF5FMSZBoAwK23dJ9itASQRTyKGb93kj1uFKVNAhuFOgf_RtisdQxzNkclpJgfGcHHT43UeEFmhvWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=Bh4knP1n8_Jqgp96u3i0PqSCpAVbveA2Zow5SLTZdAxrIePyIXHeQPTNXDywiCCcMod1DzAvED_7YbNABM-uzEPhoMrSSkafEu6RmVF3a4nEB1xGTizTq4sqZWLBSGSoCCgUMuM9cbizRe1_GbjqwpKY3bTuCBXnMo734Dv43COxIGrcCxZ7dtkBwepkPBTV4NKcW9QqaKaSLn89RMt3L-nGyEAWtKm2deVxUQ1m7lVd1FC9QJ7wZ6oK-UuzfRCxARIJHbhZAjVpwYCFx0WA9Of9R_HvS7KD1URzBMfbhIW8FrFRaBeVS5ho06ZuMdbxyTeLyuTs79JYf7Q-SPXJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=Bh4knP1n8_Jqgp96u3i0PqSCpAVbveA2Zow5SLTZdAxrIePyIXHeQPTNXDywiCCcMod1DzAvED_7YbNABM-uzEPhoMrSSkafEu6RmVF3a4nEB1xGTizTq4sqZWLBSGSoCCgUMuM9cbizRe1_GbjqwpKY3bTuCBXnMo734Dv43COxIGrcCxZ7dtkBwepkPBTV4NKcW9QqaKaSLn89RMt3L-nGyEAWtKm2deVxUQ1m7lVd1FC9QJ7wZ6oK-UuzfRCxARIJHbhZAjVpwYCFx0WA9Of9R_HvS7KD1URzBMfbhIW8FrFRaBeVS5ho06ZuMdbxyTeLyuTs79JYf7Q-SPXJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=nWVSDNefdsL5FOTdrSK31kZ7B9lf29NRUdT6GelWNRYhmSuY3eZFVh4JOkE9Wm5UCzSoKoNYlAwYQhmrr6FoPDTXoEHEZGyTU8eCPj7ft3FhjYu1rBQQnAUaT-QF86f5kvJITSjxnYw99JYVDRCBUUj1syRGR3ftY7ePRsaHB17owpxIeIpCSddBtlSPJdXzck10n2xjnIOr6qge0Kh7Wnqq-UzAhVYoMbCn1Eq_yiCP9BeBmGEMMv1hdKsoCP-PPhXKBDkAcRg1fjKhO3ylq6DX0tf0B7IhbBaQvYhYcK73Gqg-bmih2PJOYW_a2VmxEZ_Sz7myQynm1jDSONvsPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=nWVSDNefdsL5FOTdrSK31kZ7B9lf29NRUdT6GelWNRYhmSuY3eZFVh4JOkE9Wm5UCzSoKoNYlAwYQhmrr6FoPDTXoEHEZGyTU8eCPj7ft3FhjYu1rBQQnAUaT-QF86f5kvJITSjxnYw99JYVDRCBUUj1syRGR3ftY7ePRsaHB17owpxIeIpCSddBtlSPJdXzck10n2xjnIOr6qge0Kh7Wnqq-UzAhVYoMbCn1Eq_yiCP9BeBmGEMMv1hdKsoCP-PPhXKBDkAcRg1fjKhO3ylq6DX0tf0B7IhbBaQvYhYcK73Gqg-bmih2PJOYW_a2VmxEZ_Sz7myQynm1jDSONvsPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=H3MUkTV_2vdIKrIipJPiEUcJYL6HSPr0Grn0AVuopL7XTDvK2aOsr8RVJzRWz_ul6q_nN4bVMPLcEMQhvrnrtfTNzpSM68_rYgKFblgRZJ0N41UqD7xAH8kWKmVyPwHJE3fYIzleZkp92o3uqFV6JAk3iD_OQP-8prBMinHG5xIDzZ5z_aadcxM_H1e4nyN7WolnyUs8xyJPDo75OMXdSG6Xd5Dqtgi0_e5RPheDGfUu0gK8RL9fvEUVWWF2wOcbEIBX3RYv1wwQp9Mht-83dB4rxB_OaginDHzzJUcbEKMO_2nREatCJPDqgSgT-rGrFqOXBM9AXq9RClGP9ALYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=H3MUkTV_2vdIKrIipJPiEUcJYL6HSPr0Grn0AVuopL7XTDvK2aOsr8RVJzRWz_ul6q_nN4bVMPLcEMQhvrnrtfTNzpSM68_rYgKFblgRZJ0N41UqD7xAH8kWKmVyPwHJE3fYIzleZkp92o3uqFV6JAk3iD_OQP-8prBMinHG5xIDzZ5z_aadcxM_H1e4nyN7WolnyUs8xyJPDo75OMXdSG6Xd5Dqtgi0_e5RPheDGfUu0gK8RL9fvEUVWWF2wOcbEIBX3RYv1wwQp9Mht-83dB4rxB_OaginDHzzJUcbEKMO_2nREatCJPDqgSgT-rGrFqOXBM9AXq9RClGP9ALYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=QLZV8bfZk1pMV-4Py3Doiw0wwQliZxXgQmYU989_Ol5NPIxIT9MZyFNFAjEkA81WoiyvHfw7S6RjmcmwX8csAbB0OwsCluhj6cgbbowCthXrBHA-IKs0H5AamQsIkm_UNMCOZSLw32BVL20Y5rRt9DMYhrqcNm8PGKwfPkaORogs3K_hQaZpLmHiL-h2ne9v1-jAjeqpmcfBO5i7ijgd4GwawijpHx443Q6kG1QxBX5tgnvhAy7DRKPZQRDlhaz6hTztKRFwyBGthm-mqKoX9gvY2RBqEmyueoFQ8O3mMhUc9nteKrds0dAZl3vgnIb3wgbhFPzu8X5aYXxOS2p5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=QLZV8bfZk1pMV-4Py3Doiw0wwQliZxXgQmYU989_Ol5NPIxIT9MZyFNFAjEkA81WoiyvHfw7S6RjmcmwX8csAbB0OwsCluhj6cgbbowCthXrBHA-IKs0H5AamQsIkm_UNMCOZSLw32BVL20Y5rRt9DMYhrqcNm8PGKwfPkaORogs3K_hQaZpLmHiL-h2ne9v1-jAjeqpmcfBO5i7ijgd4GwawijpHx443Q6kG1QxBX5tgnvhAy7DRKPZQRDlhaz6hTztKRFwyBGthm-mqKoX9gvY2RBqEmyueoFQ8O3mMhUc9nteKrds0dAZl3vgnIb3wgbhFPzu8X5aYXxOS2p5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqkwCYMHx9pvEaDun34FAZGoIMQpPp6ZT8z2iHG59MZMR5kdeHNAKjlPL6_YRVRFNYXCS5lCoNt9nrzoWM-lT_bMu8rhbiWuDpzjREnDJm2FAk1fxbE2GHkiTY3i15S3l4qjL8C18MVDYnPk8Jx18R4MnxDAg7aZa0Terc27FoiNNQx-3MPWhirIr9OcmEN33IRiPyQbgKWdr2bC2lTkQ3NXCRRsLB5_aSVW52Ki3B5AWdekLHz3wFDnrQQwahaCGHcO0KWKM6T6sPF6Om4QHeZlyekrxc7zRl5Fa842JzdFin9WYWTx2NSywo4p7Bo1HaxfMZkDT-4sbCLV6vdUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=qmbd1Vsyg0t2KX6lrS0sEXHnKXSJjyDbVLRQcLT4m7HNpVra9m2Nk0psidVybmJBG-wzOyXbZQYptzRjEt7tc6eyrQ6hKZTy3wjRAG6fJQ6iY5OIgTqfIuhjp1scCnvij_sNvRBFgacJCt_aB_4lz-B8dRlLt42OPFsenHLnusZuBaahjfumqUfqf7mhqB5b4Ap5_gtK5FeE4pkBCoB_Jg9hpdq7M1_pSQdVavSLRl6nFX40YHX8R-_eF96JCKsevbVyvCn22LIudHxt1IW4J8i46ThCATyHZl-7PNoCsyhGIznqYps3An62Oe2jTxaop9Inm7d2iGWucaMZOZi7Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=qmbd1Vsyg0t2KX6lrS0sEXHnKXSJjyDbVLRQcLT4m7HNpVra9m2Nk0psidVybmJBG-wzOyXbZQYptzRjEt7tc6eyrQ6hKZTy3wjRAG6fJQ6iY5OIgTqfIuhjp1scCnvij_sNvRBFgacJCt_aB_4lz-B8dRlLt42OPFsenHLnusZuBaahjfumqUfqf7mhqB5b4Ap5_gtK5FeE4pkBCoB_Jg9hpdq7M1_pSQdVavSLRl6nFX40YHX8R-_eF96JCKsevbVyvCn22LIudHxt1IW4J8i46ThCATyHZl-7PNoCsyhGIznqYps3An62Oe2jTxaop9Inm7d2iGWucaMZOZi7Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYtyHBjiLnYw7gUFqiuJwY9F-4R9Qxf3Zkq0yzi_noFGypJ8qK7mzIC_74J2Rhpf1QkoLwJnjkuF8Y_kurBdBKctP6G69qoolBg1CbM4L7J1P9NCAtUPfvQR_NQcPYFfbMv3LI71moiqPBnbgxw8uqfto6kbxh3ogoDDeAL3v9A3pigGeVM7AXCiNL9kt5c5uj1gI6hVHqhNfhK_vCEEx2JKoRB4yKd49NJyZcXtl2_N2_FQ_gt-h6Y5_dy8bqkHg-PR6XShIkjtBFA4_XllUCNbZ4WnbK61R_mgD670KUGEwuR9haSICP6DXSC3kQF6-QDQcBWkCpFFoMJftPRHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=lDiqClNazfNL1Wu4ouwEIMUCG-MZ3EZh6N2N5xfd582FXkSq4VUHJz2kyGNdfJlTxpo6SV2OVpr3d-HRpbTYGZpPNhQqFUbixa8uFmnxyrcunvXteoAetRIXI5euparKpRx9JedT0aox2liSWPsN8UbB0UaNjXTffvUlArf7fTjIxl3Dia_6jyupkSDvIrV7GcHLkRESqKtI__Qo3nrtqoPUBYFWA_smpxkMXB_5Rr6_onTzyaNYimoqvI0riMrntJAJv7yJcEt-InBUWIPdFnzppVSmWF1vrRt3oZRcY1jtT4qKOqhYfQ497KH2zDdxMpDhieZUtPHqbk6UdV44SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=lDiqClNazfNL1Wu4ouwEIMUCG-MZ3EZh6N2N5xfd582FXkSq4VUHJz2kyGNdfJlTxpo6SV2OVpr3d-HRpbTYGZpPNhQqFUbixa8uFmnxyrcunvXteoAetRIXI5euparKpRx9JedT0aox2liSWPsN8UbB0UaNjXTffvUlArf7fTjIxl3Dia_6jyupkSDvIrV7GcHLkRESqKtI__Qo3nrtqoPUBYFWA_smpxkMXB_5Rr6_onTzyaNYimoqvI0riMrntJAJv7yJcEt-InBUWIPdFnzppVSmWF1vrRt3oZRcY1jtT4qKOqhYfQ497KH2zDdxMpDhieZUtPHqbk6UdV44SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=XttDgwZoUqJnB_Lak-JIACHtduex5h_5pm0ALSFCPpyTry56RRFqYpokCjSLdmkyXcv4BdYlrbZ89LwBNT08-KQ_7AUX4hVtaZqHc5vMhPMIk-LabLXqgSdGs0E-Mnre-8Zuh8wQ_rQLE5GRD0cebuwBJUw2ko-p-Jl2JPryA104UQTBCT2-FO0kwTYk0IB1LYcgbpuXOKcMivBqlUJIl8XayxcJLQpbef3fLy1-p3Qkm-CdiCmKYvn5y03YGWTsUbSCyyb02yWYTjCIGg5uOUMbXz4jy-UqTilNMOIRWT2Ca91BXoUQqCNAtVi_NlC0uRyIMEEaMO0X7NsCgZgAOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=XttDgwZoUqJnB_Lak-JIACHtduex5h_5pm0ALSFCPpyTry56RRFqYpokCjSLdmkyXcv4BdYlrbZ89LwBNT08-KQ_7AUX4hVtaZqHc5vMhPMIk-LabLXqgSdGs0E-Mnre-8Zuh8wQ_rQLE5GRD0cebuwBJUw2ko-p-Jl2JPryA104UQTBCT2-FO0kwTYk0IB1LYcgbpuXOKcMivBqlUJIl8XayxcJLQpbef3fLy1-p3Qkm-CdiCmKYvn5y03YGWTsUbSCyyb02yWYTjCIGg5uOUMbXz4jy-UqTilNMOIRWT2Ca91BXoUQqCNAtVi_NlC0uRyIMEEaMO0X7NsCgZgAOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=hpMqHLde7uhEZQPwoXKd5eml6zmsFeTgNrTIi8nvH1GDmoYzillxtOUqfwFDxfTf7nmufGqxR5kOUYcCiNYca2sTnqwKLpT17F6qZwdc7EBXcybCi6DtR8SJuw4jg5KuSyEqPDAP3fDBz4FI8E7xek9g_N_CCFn4OnSOINmvI66jssSNp4ocYpo12Fr4aCi3dHdK6oR9-2ysMMB2eyDh9LEFumkJMZAwexaBmtOdmPYaY-1lLRmbaDZB_br-xqgkWPuIpiFDdi_2c-kYd5ULjYSyx3vbQooG6wxo7kUs8lPehueKeYdlEL87UH309WKDR7_HrKGBF2MntZtpqMMntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=hpMqHLde7uhEZQPwoXKd5eml6zmsFeTgNrTIi8nvH1GDmoYzillxtOUqfwFDxfTf7nmufGqxR5kOUYcCiNYca2sTnqwKLpT17F6qZwdc7EBXcybCi6DtR8SJuw4jg5KuSyEqPDAP3fDBz4FI8E7xek9g_N_CCFn4OnSOINmvI66jssSNp4ocYpo12Fr4aCi3dHdK6oR9-2ysMMB2eyDh9LEFumkJMZAwexaBmtOdmPYaY-1lLRmbaDZB_br-xqgkWPuIpiFDdi_2c-kYd5ULjYSyx3vbQooG6wxo7kUs8lPehueKeYdlEL87UH309WKDR7_HrKGBF2MntZtpqMMntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=QnJabYgLRy4oeMPKLllFiEy9arscw_uAZlh6RARU1UgCTSG6ctnhaTedVnVvC7FRPF7Vtm4qgO8qgr5hhXA5bUC8IiuuKvQm6AIQC31qyFROpWCVn4EbW6QCzX-OB0CZZMXtp9ePCEwLSon7pbXAfWF8XV_m8D-n_w3cL4SYHvfXP9z0bREUJOoSdGbmjcgf4pn7B-68bWCZZx1InDKMQRMpLo9lhegCvgunPXTXwHuleGbgvBNpsLDHnqlEbb0foqhJxw0atPRIkDdyLYw7z8trqZNjC-tekkIw760R2PCikPX71aFziXWJPqPbUIvkSMZzSXmzWNd86gDoIi6VwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=QnJabYgLRy4oeMPKLllFiEy9arscw_uAZlh6RARU1UgCTSG6ctnhaTedVnVvC7FRPF7Vtm4qgO8qgr5hhXA5bUC8IiuuKvQm6AIQC31qyFROpWCVn4EbW6QCzX-OB0CZZMXtp9ePCEwLSon7pbXAfWF8XV_m8D-n_w3cL4SYHvfXP9z0bREUJOoSdGbmjcgf4pn7B-68bWCZZx1InDKMQRMpLo9lhegCvgunPXTXwHuleGbgvBNpsLDHnqlEbb0foqhJxw0atPRIkDdyLYw7z8trqZNjC-tekkIw760R2PCikPX71aFziXWJPqPbUIvkSMZzSXmzWNd86gDoIi6VwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=g-xj8YLmWpXe21k_UYDTow8R_PWzot5253FCRxoDf3iWgF2cz0XkTWYkdnaxWroICuZJAzghu8TBCdMFWng98e3Sa6EF6nwcC7bEdv7m34htOT0YwuEQ9zb9u0qsPR4a1qwoBMInNJ7F8yoZ6Rl9_c8_9b768OicV7fZ75CPsxgIEFvVBnJmWyCRN4hq2wKFt92WeljYafxxgj4lenMHxpqKJL1ThKfCqjvTN4mcYb6lERGUzu9Z6DZNRtyDED_VqnbmtqAXDqhds6DcS3ulkmDNOg2ezH2i1xoI7kEVbt0nqzeDGjFVj4qi3z_w40ckA1fFtr7586TPHYBGUsD3KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=g-xj8YLmWpXe21k_UYDTow8R_PWzot5253FCRxoDf3iWgF2cz0XkTWYkdnaxWroICuZJAzghu8TBCdMFWng98e3Sa6EF6nwcC7bEdv7m34htOT0YwuEQ9zb9u0qsPR4a1qwoBMInNJ7F8yoZ6Rl9_c8_9b768OicV7fZ75CPsxgIEFvVBnJmWyCRN4hq2wKFt92WeljYafxxgj4lenMHxpqKJL1ThKfCqjvTN4mcYb6lERGUzu9Z6DZNRtyDED_VqnbmtqAXDqhds6DcS3ulkmDNOg2ezH2i1xoI7kEVbt0nqzeDGjFVj4qi3z_w40ckA1fFtr7586TPHYBGUsD3KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WXeg6SEjA2xgvMrLw6KY0b6kRIHRnOuhSxaAcaBEWnqErv1RUyjjvw7Iqr2-nZW-F_i-8xu04MR-KU7GNVreT5ZScS2fDVYkLl_ihiDOLRCn9plkOea4s3_vsOENSmoA3En1mI-xnUCsjlHb5UjgT5C02F-lfN0dGy2t0R7vzbqRuDzqZZSl_hXsWLrbWZN67VVHJAbvhbQo-zrPhj8iwpX3pJGnrPrWhasQZBGa7yE2VMuBPdRRDH_Z2Uhv-UdO21sBkz21fXA7J4FPH1xPWkUo3BzCwBTSS9qt2fpqcwGAHujGi7pRV7OFP-kLw6xOM5znZgXp21YUDvkvOkT1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WXeg6SEjA2xgvMrLw6KY0b6kRIHRnOuhSxaAcaBEWnqErv1RUyjjvw7Iqr2-nZW-F_i-8xu04MR-KU7GNVreT5ZScS2fDVYkLl_ihiDOLRCn9plkOea4s3_vsOENSmoA3En1mI-xnUCsjlHb5UjgT5C02F-lfN0dGy2t0R7vzbqRuDzqZZSl_hXsWLrbWZN67VVHJAbvhbQo-zrPhj8iwpX3pJGnrPrWhasQZBGa7yE2VMuBPdRRDH_Z2Uhv-UdO21sBkz21fXA7J4FPH1xPWkUo3BzCwBTSS9qt2fpqcwGAHujGi7pRV7OFP-kLw6xOM5znZgXp21YUDvkvOkT1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=UxKLK5AYYDPG0rBCTEPuHfjVUMzvaMsxDPhROvfz8YHmvQD2VT2yhX_Qky9nT1gVtCOGbUSMAGUsZ241_p8Ck7UGx6QO6h4I86IwhGrbEYRJx0tCYhP95x8V0NY3Rq3MZySoYnWApP1PkVwy3Pm_KHy_AABPBUjtRTBXTbicr0HltdT528NYe8UBfEjWQOkz6p0sr0wzifgRnsWK1Fb841QJfN_4g1vALhXSqqj_snW__6-m0V58EYS1plCalYbgReC90QadcBggWw0NNLpeOg_IDVbZJzWUmQdjzZkZ1vDXPUGmE1TLaZEhpikh5YEV2Tpcj4jwip-LERfb6djjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=UxKLK5AYYDPG0rBCTEPuHfjVUMzvaMsxDPhROvfz8YHmvQD2VT2yhX_Qky9nT1gVtCOGbUSMAGUsZ241_p8Ck7UGx6QO6h4I86IwhGrbEYRJx0tCYhP95x8V0NY3Rq3MZySoYnWApP1PkVwy3Pm_KHy_AABPBUjtRTBXTbicr0HltdT528NYe8UBfEjWQOkz6p0sr0wzifgRnsWK1Fb841QJfN_4g1vALhXSqqj_snW__6-m0V58EYS1plCalYbgReC90QadcBggWw0NNLpeOg_IDVbZJzWUmQdjzZkZ1vDXPUGmE1TLaZEhpikh5YEV2Tpcj4jwip-LERfb6djjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVkm5mKx84Ls5T8yUzcUqe0Nr8XjaHiktHFA-caEv5vJ1_0xarh_jEHY2zXSt0pXCdsFS6RaIGMnHgA8UA8xY3_zOafJtxM9bK-BYl9_g5g9Cq-wkrMqzqTmJ9A3LMIfnuHLHwlgT2Wf9hMojxag6LtdZQ5vUnqmiW62zfDXG13Kt_42DX0zZ3CziY6lJ7fYX0nhn-_7WdHjwEbhaPsTaOpXbAwDA5rO2qBKKToLdec7vM7q-XMhWGoVUAVCzhMYZZyNfmAUK3cDsiXw5TD-HUdi8jKUfQHOjlTf3Z2-GE1qpBx2emypaaQcqru40jgIwjGtO7YmfKp6-KHE4FWgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV9YsLZZKAHpjj8ky_Wh7BFvx_6sWov0R4Fx1Rw3Ey-COa-gs-G8ZbYoYFTI64MdE2tx7fuPQmlRJ_Kyw0o9zsEyfzS9jYJUcPB9yWcQHpg4yTk20VEjnZzZlrLmjaFbh2JC6ZYvFVfhH54P4KqF3HlEptxRY6OS0J2ZQhQqAjBOvG1AOJyH_6NV2tSd6y2woTVd2VIksU2ny2VsHiEnyjiXLzSMbrjcoH6dNndW7WmX-9qfhYd2oEHR-epFnCKMJAM3q-mTS-ZOsY5EidOf2qlAJI-4-0ojaoO9pDdLPH1Y42SOqH4R6KT1m2oD4rKUuf0m6uB5HePDh75VAtmyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=lcQFB__rXp41oVFe0HHRGlsDToRvVp638aQgjuZAb0FMPCM04Q6HkrZ0C6qKIzmbs_nEaU7n47eCPRnKYB1cR02IcJjZJ9o8GXfSuj8vfpN06QEI5QJfDZ9LUvMxuS8axMjkrmuWS5Xxc5_wnhWeNDW_ExZe449L9e6yW1TuEun08hF_TExMtubaRO7qdykG7L0BRdTNvqatmtBjF-tmXn4hlv3Txfq753c94ZJlTF51apwUcmlaBNID3lu_Zo-TIUgWyHwRYNeBJWJ9f0Y4irh1NZ7uvh-5QV2KSnnsKUfiwgB4yzXrYZk19BVk4dcLItVS6H33UHH-BS9xQsTA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=lcQFB__rXp41oVFe0HHRGlsDToRvVp638aQgjuZAb0FMPCM04Q6HkrZ0C6qKIzmbs_nEaU7n47eCPRnKYB1cR02IcJjZJ9o8GXfSuj8vfpN06QEI5QJfDZ9LUvMxuS8axMjkrmuWS5Xxc5_wnhWeNDW_ExZe449L9e6yW1TuEun08hF_TExMtubaRO7qdykG7L0BRdTNvqatmtBjF-tmXn4hlv3Txfq753c94ZJlTF51apwUcmlaBNID3lu_Zo-TIUgWyHwRYNeBJWJ9f0Y4irh1NZ7uvh-5QV2KSnnsKUfiwgB4yzXrYZk19BVk4dcLItVS6H33UHH-BS9xQsTA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azrU0FtO4dM9si2YGywc5GA8toYkT2qCKKE2T9sgRiAreVmUTc7bvDktlIXyxzVNNLYAItosYwzMY7pfgWmvlqVNaMLXK0tcKwM_Zv8HnuIVr-r94mFWpNzFd0tvRkbfGkueWrvDvIx2IDh4-ngMW3PE_VYibef-e0a1ObdXco4dBa3qYcdpnwVU5dmJkKnhpRmaVGQCM76njTLWoak3vqVS69GZnnvVAQnUd-JiDYoGJXGAzHqSgAv388ha3IKJHRaxK-gReKuc-FR2y1GP19pxYvEa41OkxUv_hL81lHeOj9nRve6yk43XVML6OwJ3cbdLNlBAMeKoCexxQ2ASQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki443OWwN0xdarAQnPvEabwbf0Ypa9_lmmm8aRv0mZfKG9lirAPw2ZdYQZiOV78MfDr6Fm7NIHDQd6xAPJ71_5hSkFjk-0HoM4huL4eFZPGgvQdBDZ4T0iUp1Ubhepb39WfhLVQdaLWaI96bNa6MMsf7OIo5-bEox86SUZ0QEruYBNsB2UwVuI47e2wvXe_RkTr2K7CNpKwDtaJzw49NUKMRWad0LoFP7CjlajzsRSCsqnJaJn8_GY4ezOO0bLyCt01VzxAq8AY3BL1VPPa54-BhIXRmzuQR1Mfv0bVR_w4gg86_DJqJsAC7a5kbMTE87iR8GtrOrGcyf8Fm1IDjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=ByEKEFIq9RR_USWw8MuZfAg-T_F4PDCSi_D_eDgH-BdNExoxyIHOgtmybQ0_lr4jmEsaJhiF9-pclDbx919WhQ8UOtQOJa6aFj-aM-pHw3DP05MiNtQ8ZDEQhcc-iBga-VxEWV5q3qj0rnhVI5GdYX1STeCSXLNhy7OTjH2bU9RHwl9fNSEQ4eZOuhv4TU99gZJnI7EyGxHLF_xZ4-W04aSj4mw8e2y61GZKGK89fb1B3zAzIY2ViIs8gdo9aXypiisdH2f9xE6zdjuTDzWqXHBEG33bUM5hqDQGNzXcktTnFKnPZ4zdaDvgWKcBkUjiGztuBEwYmaTNBlHV5_ALbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=ByEKEFIq9RR_USWw8MuZfAg-T_F4PDCSi_D_eDgH-BdNExoxyIHOgtmybQ0_lr4jmEsaJhiF9-pclDbx919WhQ8UOtQOJa6aFj-aM-pHw3DP05MiNtQ8ZDEQhcc-iBga-VxEWV5q3qj0rnhVI5GdYX1STeCSXLNhy7OTjH2bU9RHwl9fNSEQ4eZOuhv4TU99gZJnI7EyGxHLF_xZ4-W04aSj4mw8e2y61GZKGK89fb1B3zAzIY2ViIs8gdo9aXypiisdH2f9xE6zdjuTDzWqXHBEG33bUM5hqDQGNzXcktTnFKnPZ4zdaDvgWKcBkUjiGztuBEwYmaTNBlHV5_ALbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
