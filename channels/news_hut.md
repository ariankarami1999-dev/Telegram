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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9fLWH6pOFQDtAWaRrlGBSZHeflZZk9HVBfdCAbeoMNCA_hEe_mdk8qPJHRWjAbTJ8vpNSxDKD47MPHHSYvBxB_rm6kSaZ4nWGlLy35_g8U1kXkBurxq5yNDCHl87VZ-00lA7WBgyffGYYb2xmopWLPcqNE_11r3kjdTJLqRn5TSbQZowJKf5R5uf3beCl7xbXEAPBgDnnGlW9qyJYgR2pSjP1-cOlm57o2S36hgeJwdip_DO_HV-hU8dNnZ3Yng5NL3AWtKAZ8YjYtqm-S8DK_oPghQRoh5oeEgQqWmrKiTai7jBEprtKH2vOzigB0SyGluDkVNMhrovR8fi1UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh3fX4vDRDMJLy6yTLWL-2smCQh__1TilPtaFOYeHh9rEcPOh6E9YD6A_5pcLwe6WsKRxx85VTZ2muu3M53ecf_zhbahSIxDlWPjDeUU3kZAMDgfSJPjIFezAsTYSBCURHgB7eJCkZJkar2YTpIkVh4yQQHCOHPMmQr0A0UxXfQH6EKbwjLFLgSH_B3hjfGahvWDi-1isXdHD6IlcCr2KJlhqbhGXrUAV-BjWJlXpGuPyw2XtRUEotx6GRNgY6U1_XqQrbxbL1ox2p9IQY2-Uejq1zgFlBp7SfhAKORO4-cEF1XhuHVwK4cZx2eFNRf2uxZpl-T2IakeaTsL2QjQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBQR8FinZQPg_rF83P-491OUCBhjH4gWDgSw0nxtVCLy336gvZ8vmcb4Bl5l3TofbdIicjwxwuTUsgf6Ho8hwF-PwVxPm5Tp7eqqHS_hU8AlCVLyPyGZ4g5RTi8iRRiItLB5ke5q1SBdKxQ1kxzqgDsKIs31LIyZLL_VK0Ellc7jkTSqxKOcZ930ie_3jk97U_EKQFelsatVsY7Z1TJpulDOlu4ui44wAGYvv5J2O5agnazyYUMCfT1FtZcEFOrxHvMWYXVNVo3AqYQ76V8FfZgB4zWNiDbnubyE9ymRtoM42ZDAAGtL0o75WWoj_VQK1V3NiFVL4z8eoZoRpKsxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzPDK1d78ZZrNveDda3ibRqfh7XAgfgc4SHhHbyw3iwYn5diBasuWFCqOzlmT-NzWOLFZMu7YgqueKGGKTfKp5u9Z113lCUsTw5h6NvjsFUsNjLzy5eM3niN60frbq4zXaL4EB8SdCZJBMQJXzbdqvUMhU49CUIzCzcyP2XGW6P8UCwQh0YSO246C6flJ44Dw5h1xvxV3zwdZSMpyHi6P6F0sKpj6dp7MKflBeLqNIBGvGej9OvmgtkxWXb172G71DGIe_-M2CNR-I-kyfNPdXxWkZJ-7xJTEpt3ye2z9XFl1HeNthcswPd6CoThmLeYB7kfGEaxVfVoh9MShysgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdyGZEQu2mAS4NnT3tL_aBrONKD8G3ZGd67v5Je3jTQ0lz4DQ9iNyq6UGTnEVU2F__dVUgdjfVL6V0bPFhiKoa9PVBfi3_A2pa2CEMV5PCUKq5Tc7XPMJfoHQL-0K-PrOIyt3rCEG67_J-zdOZQe-gOGluziWzkMvfGzMPBlNJhCu0p9kZukAHJZoEtm-HcNtn514ZKd__xLwqxNATn77Uprzbwl4OUf3bI04JG30jG-k_E3LvWy4zg2kVxnn-Eyg5_-pk30jakyPx4xFGp1rUz8oNnvnk0-JE6iDFYCU-12dEF5ldRsZf57jwwhFl4BP4kQWp0lZxpMMtwmBzRqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2Qr-t9v5KPtgHn63Lbn21DoaFI0jeMST9-f6SIhVguyRbl-ShzxF_5AUIjMS314AiEUV4S1xj7pku7Y5H1-ZkwYFeIwqSzBqs10YZihMRHS9-DeIUecELIrsEZHcpiCtIfG2AmqoaTKpZHQ0Sp8Lxj0Fh53U-WmX6WW1YV74E7UOVJCO84EvkHHAK4PGwciH8y6wDeIcJVV0MOjYDwA646DwAveXVO6s9_ZQDYvrbJSkLyM-hhXxt7O-DRSunfVuEu2CY48auz1js-3HEljPofKbLUnwk5sgz43ClzIhREKAn7qqdTv2QQpcGvYKWPgcXUbU-7h0l4GkqXYOhDuJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=B8VmWDOsz0J-fflxwKHSmJe4vn5DgMS_Jb73GbvA4jsXP0tvAxOOAcrUOiMJtKzNVZlKzbSpiICX9hP1H0CAD24uWW3tqbo4slN-bH7HzPgfHF_PxLwjWfGSUPBQS585bqqUlSPT84gXgnMSwjM2_C-ErMKZhzWyZmcvnPiFmqPdsNxjDpcM1VUnZHdsGHqKdl49Nff4-hkvAbjM4tvJtD5zozQcOBxMBUNG-bT_Cc60P5NSxzIaUjpcjhejp9wLEjp5ujP7pd7JEmQIsjCMsKOMLJG4ByFuI-kdO7qBPqOx8B3l0RPOUFN0lMZNTiWRaySjfRFUHamI6BH3qi0r0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=B8VmWDOsz0J-fflxwKHSmJe4vn5DgMS_Jb73GbvA4jsXP0tvAxOOAcrUOiMJtKzNVZlKzbSpiICX9hP1H0CAD24uWW3tqbo4slN-bH7HzPgfHF_PxLwjWfGSUPBQS585bqqUlSPT84gXgnMSwjM2_C-ErMKZhzWyZmcvnPiFmqPdsNxjDpcM1VUnZHdsGHqKdl49Nff4-hkvAbjM4tvJtD5zozQcOBxMBUNG-bT_Cc60P5NSxzIaUjpcjhejp9wLEjp5ujP7pd7JEmQIsjCMsKOMLJG4ByFuI-kdO7qBPqOx8B3l0RPOUFN0lMZNTiWRaySjfRFUHamI6BH3qi0r0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MF55sVkMx6tJwMq7iEV5cmHfiEJgNyK8dZvkvfK944Mc897vksBO9OS0yd3I0h-THTlgugwUVO-B_ODfh2Wp-DKWhMFn7NR02zXKjjo-3zI7ldgeRe27UkbWIZ8111oy7F5fDRtQCpoXTG4BfVFCycrZtixftIzj_HbTQyrA6Ybr17Q3J-Lf6UdA3S6Cj7rIt_waVLcJKOKZ5PqlddpRBlEoM5Dk4wC7SUgZRP67OYo_pae7KEWEASDmC2b4UOHl-7Oy_UTBxr0uAz8FUv5g3I2Z2v1Fh39Mf6bnDND6MFnNO8QE431UPXtuepmnv_AHAhehJedc2TKzvQfxUg4b_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_dyHqVFbzlAhCW9qC6bLeHjS_1dIPa4DH_BaaTYBGsqNKrcBWipWFWz7lDHK1uREA84ElSyN4EHmQ9scU9s4C5iaJs_Zu0G02Ja_moEAwEeRFJ--ePMO7NPAhniL1RE2Z-vLznvERf6r8HGEFnqWNx5x34zD4bd8hG6MEm4u-lyVzXxvi3ZzCHL8qsajtVIGVmL9hg1VNFHxCTENVPmSAgIgTVFV7BJP8lBbdP6kFl6wMBkWXv7z56rP7Oft8_38ShP2hNJXiPYgRrOONwS7XocW8Vj8BfG_KqojCRofNYwMVVLlN--A7lVKpWB8zpj6DmNsv-ou9IPAvH1toKIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4SiBeuFip66tG-OMYnXwo44le9Vwu22SxgprTP-et7LAUIGMR9kIir3J25MvRZyqJdfzzN5Qi0psPkRoniGE1RBBguqrAqaq_WBMRktVOGbNUcW_az-BaYfN2mu7eTthunjhdzRQyn9EfzGIaRmoV_uyFBXADFgaOFFS5jkEkG6iJ-B3gycrow3mvvR3uO0juIZwNyQqn4i6TQtw5wfnks_22t3wzcyY66OgZ7nkbFWerkLGaJ2tAyza7Ucfwgr3wp8HZfO69PlCXpTe2UESYNuoWRXRhEhe-5GkvkiMCtmk3GedwkjrnAlCXlLxjDQG4c1FTcafoHsjJS7aLAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=OirU70hTBtw_mLwloGcQ_8J4RTiPedGODYFn5UXdTuxNCwIyyzQTDpT1Gp_QTv0fzXmNJAQgHZUHQaZmqkwnWlsp1i6Q20vYpgytzSMgSS7ryxMbyXS0Hif3jOH4RlKzvSaoDPt4Z5ZCxzJhUITYTtHPOWkPweicXzoqeGmzmG1Jvju0RdPWhZp9U-A7lvHz-ybWmd6FNP5Ya6_C99liVVjonmq8zVDtopaAHmVwxS5Qo3790HGQ86uhVmRkP9aDjtWT8ASLcLNaowE0cBhdp2bR5I7khIGgPCqMRmAlnT12dmRnei4FjvVv8iVR44C_KS1A8V3AlsYEN5E59YlEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/medpshxi4F1_GbKim-wVmRkCPWHGTGNxV_USprlLa_T1fbqYe7GuvRInthe7QUuhn5fYMysCX4H3QkH6MoHLNHVZf2K2qJbAXnuhUv77-cCokRkfcAqU46XQJ7qGH20Yi92cbcvHS0AdnLTH8t_KaqHPY0ShbXjpTuMPm4D-YxwPGCkBrUeIbcQyP1-h2eZwsW9Cf4ONZEasdwLq0xXRgKC4u-akLTnGJp3-NYtjUyrJYjpDnkUf416D1eONEAmB1uLtnLsigpXNFy37iEmjuhM_NR1OI_3zH9kZynbCw4nUUf8GPOYTVkOHmfBcUXf_mfymx3dIV7lgCZg8Puo1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=TRA63dmhJcI7_D0CNoIy0InKNRvK2jb6VNI3yRzEvk_xHXoTkSbysiTk4z0kYcDN6RinZR_IHMQEiVmn1n2ldczRwcbPXqij9v2-4fFLC10DRmyL8fBZj7ra43MhgEcJh1Qa635sM8cPC5hZbaasYLpld4Kui_-zhl4f9t9-GQJR2a-p_W3yc21arFj5Ho3QRkzGFip8y9wlNJfb08jSgm_1ukaDC5YKhKpCJzRxQ8pXriGtwABqbfXepoJp-vd6EK40b2JRV-9TGH7ki2bU5zTUjNTJen9Jccx8rf11Yvb9gWWcG34i1hBkV0aPhqNKZvE9oOizUa9MsIl6dC5xtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=TRA63dmhJcI7_D0CNoIy0InKNRvK2jb6VNI3yRzEvk_xHXoTkSbysiTk4z0kYcDN6RinZR_IHMQEiVmn1n2ldczRwcbPXqij9v2-4fFLC10DRmyL8fBZj7ra43MhgEcJh1Qa635sM8cPC5hZbaasYLpld4Kui_-zhl4f9t9-GQJR2a-p_W3yc21arFj5Ho3QRkzGFip8y9wlNJfb08jSgm_1ukaDC5YKhKpCJzRxQ8pXriGtwABqbfXepoJp-vd6EK40b2JRV-9TGH7ki2bU5zTUjNTJen9Jccx8rf11Yvb9gWWcG34i1hBkV0aPhqNKZvE9oOizUa9MsIl6dC5xtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=sz4soi9FwETMCyX4thdNZ2pY_-KFCbNgBZ6zgz4FZIN0A_SW6w0VDzJlcqjpWQSGBLf5dNYYUVnuuOe3S3nWDaLn7W0GMCdY9pmcq95N4_lFteDYTBWyC5H3tUF3akp4TLoiBe3YVxqwAg2XMpf5UXxVJafYKoqkZ1bq39PzyqmNvC0cnGq_VR8pOVIL2bXPDZjR229JrK_9oFtdgg2cBsnf5VissQTYNSDKUrEjoFlYNbcDDKm3LAA0qWyTu9qEgzSuAxbF9MwFFJ5VxEMLBN77TVCDpFnKckZw-5-dgEDxKqv-A9cNawubJugCczqztV_xIIkoBygrhc4W1Rc7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=sz4soi9FwETMCyX4thdNZ2pY_-KFCbNgBZ6zgz4FZIN0A_SW6w0VDzJlcqjpWQSGBLf5dNYYUVnuuOe3S3nWDaLn7W0GMCdY9pmcq95N4_lFteDYTBWyC5H3tUF3akp4TLoiBe3YVxqwAg2XMpf5UXxVJafYKoqkZ1bq39PzyqmNvC0cnGq_VR8pOVIL2bXPDZjR229JrK_9oFtdgg2cBsnf5VissQTYNSDKUrEjoFlYNbcDDKm3LAA0qWyTu9qEgzSuAxbF9MwFFJ5VxEMLBN77TVCDpFnKckZw-5-dgEDxKqv-A9cNawubJugCczqztV_xIIkoBygrhc4W1Rc7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=pVRGSgo4kSi0ePf562_k4n9wKw8rLV7-c0gObPG3A-Lv5sEr__P4tY--ylao42SzqxvFdt6AQsIxDskwTKfIFpKfBnCj9apWwp4r0h-0QPIIeYhuxjMqBwM6GG2B9xkKzktYrOaUXSIfg_AY3a22QbMgQD3ghVjwDFmzs14adKpTOPIkcndZMDmTefGCDNhEF-LG1teWmryCFVblb4431UXpXKTpCMJGKZudNf2vaS9US1I4ExJldJKECF-vXpAAbcsXfiNV4BVcDBoOmhzx6lsQAL6X1ywNs-dFcOqyY__xn269hFqItbz_2L1VqeBVlN0nijNuEGhiur-BzKsyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=pVRGSgo4kSi0ePf562_k4n9wKw8rLV7-c0gObPG3A-Lv5sEr__P4tY--ylao42SzqxvFdt6AQsIxDskwTKfIFpKfBnCj9apWwp4r0h-0QPIIeYhuxjMqBwM6GG2B9xkKzktYrOaUXSIfg_AY3a22QbMgQD3ghVjwDFmzs14adKpTOPIkcndZMDmTefGCDNhEF-LG1teWmryCFVblb4431UXpXKTpCMJGKZudNf2vaS9US1I4ExJldJKECF-vXpAAbcsXfiNV4BVcDBoOmhzx6lsQAL6X1ywNs-dFcOqyY__xn269hFqItbz_2L1VqeBVlN0nijNuEGhiur-BzKsyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCnoHU62srAq5QC0Jt0qO2YFw8qc1ilu_FhWhsTqAzxLUjX5bHxVgsoJLP8tyPoXTbf1oQoeqcbFevzmqlWdzpSBUzLqtklyu20NI-A-wcbPzUoI5N9w1F1yyQCT9l7D5XZX-e6QYEoIVfieJeG9VSjopONZSwaUzzJJjZBYQOyIDwmhFOiJdi83ZL2-gsy_aaJe3He6InJ6RYmLBWa-g55c91Vas8cJdkWKawDtuf_YoS3n7F4d4yEuAGFeSr6tr_1u2VxMd1RXzD_bGJWbM1tBHhuLEUzVGLuj-Ej1swr1zl-r8ZSMAso39XcuWuXbTP5ZlJAVLrPYh7fHc22ldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onJa64OPRxsktUbbnzAIzDIhzZw5A8cX5-c9asFs-3LM1EHBk8OhxQbHB1gtMqzpebuL1M1wLfpsi7YEKpfeZXZ_1g7U72kv-lQVliLtF1MUB2rwrd-nxr9MRS5J5BoqOS1xGDvxQH4PzV1NQSParyfiDi6SMp6ok8ehLtOyaqKi4si5MI2Mm6U7a4f6Qi9ejaMtC74DezHmkmd9hFLsmsLCS1YQv7Zybnn7KSsgwk_1E5AoJa0y_A1y7GJE8-6GM65xDYw9t5C6wejCK2sFxujgEJOMeaRPTEES7vHJDJAFEKyXejs8giZ3Zo-GhMkGayqpaEwks7JOAgnmZXN28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMoUvYLLQRMMXt2Qq-IiDjjg2VlnChNrJEKnhcX-asvq-fxM445uconLDK03jReJdOrKBS67u95lTyete6Fwd1hAkJjPawWGMyui0_M1cBzFZF4L2EN8nAcnIiylk57erBjY1mlJ2degO8FL7FzzNA3F7mW2giQQpWkR6fOtgUDS95XKiZjokzVdYQD53wPtvn-Rx60S8MklQ4S_dEmdWy7bZKAyJM_0xKMO_xam1nti4gzXCwhBO2iHmk9ULsDQZ1oO4Xe30VSHlCuhIYMsOs57CDwum9xYOb2_OEhI_Jaikq4bP8b5eaEGqbiKmIbnFx2sNcBwY87vZPcTU4Ha6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=UE58ei9mh2UUVgaPM8X39bOHEAvZUvWnh36qnwOuHnJn1Sc6-1W4K7a79s0WH7Hd61zmGYr6TviCw3RjtML8PjfcoT9OrzGQWuALk8DdnudoYrc96oZKne3ghzklFqRSH0xerLwOGa2qoQtJazkzCA3MzVJ5IsqiLihlKrTxBtfaPJbQ6O29s5wUmYSs40GrhcXJZidDfjviT83kpYACQHdZRsyLyT_31c6YL1sIB5TooEQkrBY3Aey3chJ_MJiWuwZbQdSmjkxJ71Qekb9fbNsgij4qFLVWIV0fbVP3yasSs63PFaYFqk8sTKGhqXX6yqUgW8y3iQjuPrIkT7M_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=UE58ei9mh2UUVgaPM8X39bOHEAvZUvWnh36qnwOuHnJn1Sc6-1W4K7a79s0WH7Hd61zmGYr6TviCw3RjtML8PjfcoT9OrzGQWuALk8DdnudoYrc96oZKne3ghzklFqRSH0xerLwOGa2qoQtJazkzCA3MzVJ5IsqiLihlKrTxBtfaPJbQ6O29s5wUmYSs40GrhcXJZidDfjviT83kpYACQHdZRsyLyT_31c6YL1sIB5TooEQkrBY3Aey3chJ_MJiWuwZbQdSmjkxJ71Qekb9fbNsgij4qFLVWIV0fbVP3yasSs63PFaYFqk8sTKGhqXX6yqUgW8y3iQjuPrIkT7M_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiTE6k7sJ9_OIULoSy5Y_zR3XabvpYhIWpYSSxYZaxiiAaMTyxMySbZ3T-MHAuTMMjNYqgAlz2TlzohOaQz0gQceDASiAXkT600aLgnQDaUyIbLBh-Kkz-mVGN0Jw32nNL55lNIlv1i4nrnS_1vZSl9QcdPoMKXqfuLANxAACIdGejCDOaWzFW0zKeB4P4XbS3kfW1K3SkYMSTDE58V9s0kRLxNZZQ3TWBrxXO8m06dUixYwFbsiSh_DD2mNcqI2P-RNEp6eZBsNmIUWtw0LpjDEvTe51PtlBODxx5FtlnO-dlP99QBd10PaVm0KevrI-AmIPClS9hFLuR-XwdpJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=gGS_W-fxnAmasusGuCeOc6ZyicLO_afeAcH_W2uZJlP5pCeUQ2YECjAmVBAlrYs9WwbwDgPIlOp435_lcZXv60iGmeuKltvXxLDkrm-A5ZcCFtjnLL3yePmpjxPOkkMarAn8jnchlhuCTvxx35q9Nkx_7roSqer0zy9Ls44B3Ul207yemylNx6rpur6Q8ecUj-mFQAk1NOcXZaK6kWB5kSxSTmI6MUEor_p2D4woxHdBoaEtHu0YHC4dewPEmvMK66zH6hZk9G9uxM1rKTweuH1TTnbO9j3886TUP05muweCYoYIDvU6-7h0nTNLWf7s_qU2WjZuwfdj3jcnAIh-h2w-p8HBuQhjFkJOcuRF4VhNpIfLEJi4eCBi0CdJinI_QatxnkfIuP1ktMT_wxAoWV43ZAukBifO2QFe8T5Xbiz_r6y0MHLJs_CQv_ZxbW_j-9zttvdQl3ZCxoNQRxnP6Ew0HUlsS8q8_TLle8xYKvcRw5OigOj7XcvdYeBHJZfqVO3Uh4NlSLgq0GFchmjGGaBjQn0gPq5_O7YM1Y5GkhwwafefOb9lPRQJnOTKXX-kBd5978Kia6Vq2wXZp5bElNPQjY0wYfT0peeZM4ns53IXv6ZHgOErCFd1C-OAiXmEtA6Q0IsqYTNAO-KpRvsoJQuWePbSHnLZh95r8qaN6R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=gGS_W-fxnAmasusGuCeOc6ZyicLO_afeAcH_W2uZJlP5pCeUQ2YECjAmVBAlrYs9WwbwDgPIlOp435_lcZXv60iGmeuKltvXxLDkrm-A5ZcCFtjnLL3yePmpjxPOkkMarAn8jnchlhuCTvxx35q9Nkx_7roSqer0zy9Ls44B3Ul207yemylNx6rpur6Q8ecUj-mFQAk1NOcXZaK6kWB5kSxSTmI6MUEor_p2D4woxHdBoaEtHu0YHC4dewPEmvMK66zH6hZk9G9uxM1rKTweuH1TTnbO9j3886TUP05muweCYoYIDvU6-7h0nTNLWf7s_qU2WjZuwfdj3jcnAIh-h2w-p8HBuQhjFkJOcuRF4VhNpIfLEJi4eCBi0CdJinI_QatxnkfIuP1ktMT_wxAoWV43ZAukBifO2QFe8T5Xbiz_r6y0MHLJs_CQv_ZxbW_j-9zttvdQl3ZCxoNQRxnP6Ew0HUlsS8q8_TLle8xYKvcRw5OigOj7XcvdYeBHJZfqVO3Uh4NlSLgq0GFchmjGGaBjQn0gPq5_O7YM1Y5GkhwwafefOb9lPRQJnOTKXX-kBd5978Kia6Vq2wXZp5bElNPQjY0wYfT0peeZM4ns53IXv6ZHgOErCFd1C-OAiXmEtA6Q0IsqYTNAO-KpRvsoJQuWePbSHnLZh95r8qaN6R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=SgbJ53rCZyKjS5XguVXOp_LYCF-oV3jdPDyL-CigguipWnaZhEKILhRAUXedt-FvQVaznHRPfqBPus3wguUuizIzu2abcd-R8aYa3uG23Dh5bzZI3E5J2SGERuDyS9f5Z9r_Ls6AzYFAwN42qp4zXTgUWQ25MLHvTml9fpU55a-Vz-pxYlf-DKlNz_gXtDrMYxyyq6d0cqmLprkX4EOYAo7bG-Hq-lA8V0li8E0iQOe4g6mjLMPNX-eraY86FBpT5py6SOnUcmRdmsT0J0oRkQ8W7qMn8pis3E5CUa2FZiiJRVkbl0zOwFM-ABXxN6ms8lm5cBnhsWWzGZ-gVs_vrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=SgbJ53rCZyKjS5XguVXOp_LYCF-oV3jdPDyL-CigguipWnaZhEKILhRAUXedt-FvQVaznHRPfqBPus3wguUuizIzu2abcd-R8aYa3uG23Dh5bzZI3E5J2SGERuDyS9f5Z9r_Ls6AzYFAwN42qp4zXTgUWQ25MLHvTml9fpU55a-Vz-pxYlf-DKlNz_gXtDrMYxyyq6d0cqmLprkX4EOYAo7bG-Hq-lA8V0li8E0iQOe4g6mjLMPNX-eraY86FBpT5py6SOnUcmRdmsT0J0oRkQ8W7qMn8pis3E5CUa2FZiiJRVkbl0zOwFM-ABXxN6ms8lm5cBnhsWWzGZ-gVs_vrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=llNC-Lu-DYyqTvKMfTkPrpiOeBt3H3gzvwcgBjRbnMlGRpSiBnrKsiB_jKIhi0a0--qHqgm-HN4HVAdLita63_uu7n-rjnarlBCVCVeWsBLHF-7o0l7EHlH1AMRnlWEp_R9LXxPt0TsvtrSlmDR91zbVv2ftao_rSuLXrkyNju8993shVft9DAz6vwx378OayX8ZldW-g_QhMQoAfe0KREqbvFKonAPRx2sIy0wm3pHEkJhCBT0M04Tv188954RWglFk2aLw2clmZynepw-il7PDpHhRqfO71YuhkNvmmuv6vzxB0N797S92vTQCChlXalBY1hRB48CUKiL0oFbEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=llNC-Lu-DYyqTvKMfTkPrpiOeBt3H3gzvwcgBjRbnMlGRpSiBnrKsiB_jKIhi0a0--qHqgm-HN4HVAdLita63_uu7n-rjnarlBCVCVeWsBLHF-7o0l7EHlH1AMRnlWEp_R9LXxPt0TsvtrSlmDR91zbVv2ftao_rSuLXrkyNju8993shVft9DAz6vwx378OayX8ZldW-g_QhMQoAfe0KREqbvFKonAPRx2sIy0wm3pHEkJhCBT0M04Tv188954RWglFk2aLw2clmZynepw-il7PDpHhRqfO71YuhkNvmmuv6vzxB0N797S92vTQCChlXalBY1hRB48CUKiL0oFbEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcxUUdv6tnK7nlin7bP9LlHUcXSwvIwTMnuTfMlquyCAZbS6xLoNiBJXxqwMdD365Qlmyy59KGyjkPJsYPODTRzirOK90k-zPoELZ09p6ycOFxvFcMzz3lgIQO-UgCzhWZmT-ahyR9HS0wibd2b5WJgtbBGTyMxlUPXLTPCsmj5Ha0Xoem0hdl98oLr9WHumB7_ghM4_wWNdSmOTViCsfNrPAoX0hPvHOwQWMd12zxdpz0ptK7z_Zh2ynj6eymK5uGX1Ifdua4wDpuxNbVEXKqOTxl1h2DLif7PPYPWiJYyKZoJebormFuuDGRH_OtMy593t-egWGnhs8__aofkFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=bmMg0rnIySyfE3B4O35GPKETgrALWjmfPUbtVxoSj9GtUE9eYgR0bStufaVcKqhDJ-h7fMJTuzWAmnJZHvWTtdQMscIm_9ULy8-eTl7aKcp5Qoc_EX57dlAz-2AHgn2kHj6zW8gxCVNmURAxSxfd5g5vNbH2dFkjPuOpQ_-G9l-7H8NizSI-tsGIsrN_77XrEe1GTtuPoXD1F_UIM_esc1zNmaJaHqG7VUeQ2aM4E-3_bB74GORtiJoIG7Pv3qdkA8iUpW-legcPctHt4-7xZhYSqhfS-lAHqGJNdbyJoCEBsz1wve9dZBIh9ub2YJrBX4pV2sBRX8JFJd-DKYAMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=bmMg0rnIySyfE3B4O35GPKETgrALWjmfPUbtVxoSj9GtUE9eYgR0bStufaVcKqhDJ-h7fMJTuzWAmnJZHvWTtdQMscIm_9ULy8-eTl7aKcp5Qoc_EX57dlAz-2AHgn2kHj6zW8gxCVNmURAxSxfd5g5vNbH2dFkjPuOpQ_-G9l-7H8NizSI-tsGIsrN_77XrEe1GTtuPoXD1F_UIM_esc1zNmaJaHqG7VUeQ2aM4E-3_bB74GORtiJoIG7Pv3qdkA8iUpW-legcPctHt4-7xZhYSqhfS-lAHqGJNdbyJoCEBsz1wve9dZBIh9ub2YJrBX4pV2sBRX8JFJd-DKYAMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=n1fcVA0yxGsDX9juKDKtJIGLqQTh14WQSbZn73XB9iMnO_jYuHezleaDsvYplP64f5W6o2zPY7jEhtzAYBRup8GG4wdNQyZCDA3oOUegTkgQ_bG25DI95fs7ZkcGAooLJWZqIuWfbRPfnd-QHlrN-_9VgCE4ZY2o_bRre671JnuEtYaic9dUPd688mcH7Osyx-xmriqrtYqZ3R0lKYHqtrlqtgLIFzjLDB7L2XyFg6rjGfpVol5tSLGroSG_mra0stcRk67SviS6sJy7ZZmBWk9W9QMJoIs7P-4m3upZN_RtJMAufUaQdFs6OfXfJ2U9bAJSdBUEV-ok4SPwLMw3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=n1fcVA0yxGsDX9juKDKtJIGLqQTh14WQSbZn73XB9iMnO_jYuHezleaDsvYplP64f5W6o2zPY7jEhtzAYBRup8GG4wdNQyZCDA3oOUegTkgQ_bG25DI95fs7ZkcGAooLJWZqIuWfbRPfnd-QHlrN-_9VgCE4ZY2o_bRre671JnuEtYaic9dUPd688mcH7Osyx-xmriqrtYqZ3R0lKYHqtrlqtgLIFzjLDB7L2XyFg6rjGfpVol5tSLGroSG_mra0stcRk67SviS6sJy7ZZmBWk9W9QMJoIs7P-4m3upZN_RtJMAufUaQdFs6OfXfJ2U9bAJSdBUEV-ok4SPwLMw3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUSMdDn9YHQoGrENoAukKEIwv4FWnu--qpodNV2g_BFmHcne2-tzMzY_XZGt-ajr-J525mMwrqaNVMG7-1qeOjlGAbCqJzewS6lRqpx4p3KxYBGkSuMnLbK7HnOuNS2P5jLMfPcLiiEGIRUIpgOmh_nKqhS7TmjKn6lU3dUQHE1pCWbOeXld6dCt8t96zkfu4JL1trXMK1NoXiO3xfHJT5vRzJuW-FMldjUHsw1lTmfocZTQjGeWtxAfRTZ7eUpj5QxTa4-CrSMks-lqTMeE-2EO-HoVYRm6y-gvC4rqgZ2y3jYqEkedsOdlNrOh3lI3P42eDD2oa4QSnB7KxzJjUOH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUSMdDn9YHQoGrENoAukKEIwv4FWnu--qpodNV2g_BFmHcne2-tzMzY_XZGt-ajr-J525mMwrqaNVMG7-1qeOjlGAbCqJzewS6lRqpx4p3KxYBGkSuMnLbK7HnOuNS2P5jLMfPcLiiEGIRUIpgOmh_nKqhS7TmjKn6lU3dUQHE1pCWbOeXld6dCt8t96zkfu4JL1trXMK1NoXiO3xfHJT5vRzJuW-FMldjUHsw1lTmfocZTQjGeWtxAfRTZ7eUpj5QxTa4-CrSMks-lqTMeE-2EO-HoVYRm6y-gvC4rqgZ2y3jYqEkedsOdlNrOh3lI3P42eDD2oa4QSnB7KxzJjUOH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=UjaFkHjPSqurbywaIrC3xAMBRtG1tkXh-FV0PoJlF_yCtapX_6m4Y4XTQEUu2wiKvW3nLUuAWzuTr60-NmmSMLosSzxMiB3oFDxvQHqu8P8wVGLGmDiYL9EVM0x_8R2tC7KyOJUejJFOHTWEB5cKkqN6m_5F_l0UDxabd_Op6xInqACrCzDKPoMAkf5XgnCGZjnoSUzhbuO7T4IGwVas_UfoZph6l_-Cgp6EDXbma3o6YaTSYDQq8RSA0n9BQEjGSF9eXuhf47lMPG3qepUkPQAIhNiHDzHD3a_qepT0TYEdCt0f5X9DmYrx2_j_t9le2psqsnMwL2aIUDDml-6cFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=UjaFkHjPSqurbywaIrC3xAMBRtG1tkXh-FV0PoJlF_yCtapX_6m4Y4XTQEUu2wiKvW3nLUuAWzuTr60-NmmSMLosSzxMiB3oFDxvQHqu8P8wVGLGmDiYL9EVM0x_8R2tC7KyOJUejJFOHTWEB5cKkqN6m_5F_l0UDxabd_Op6xInqACrCzDKPoMAkf5XgnCGZjnoSUzhbuO7T4IGwVas_UfoZph6l_-Cgp6EDXbma3o6YaTSYDQq8RSA0n9BQEjGSF9eXuhf47lMPG3qepUkPQAIhNiHDzHD3a_qepT0TYEdCt0f5X9DmYrx2_j_t9le2psqsnMwL2aIUDDml-6cFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=nHzmzAAUOlPEj544qDNRl2XsyL8HygFLv8V8ZBNrJu8h7-FGOJR_tuxwVUGUBHV-WDkHopT3PKiVr9koZ53nk1wlt-H_et_Svpcf-hKRNMlliU0ZNT74N4etuRMHf-8QwvxWCzFjgDrwDVzYPkJwiezUM9D7b91CaI-6rSgqRC5pFIXVtMInH_dmcCsatDLW74ZwN1yfRfZAoqbvvXrYXS2rMVKBNoHM5Ew5lpKU09RPsvthrKUYAg1YHnon2oTHmUavmrhY8kanS8tr93mf4vS9B0xNAdkVjujdOOaMr59ULe-rLuvKh_KAr2GQlB_edAptGv2RQw6bjKF0Up4Few" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=nHzmzAAUOlPEj544qDNRl2XsyL8HygFLv8V8ZBNrJu8h7-FGOJR_tuxwVUGUBHV-WDkHopT3PKiVr9koZ53nk1wlt-H_et_Svpcf-hKRNMlliU0ZNT74N4etuRMHf-8QwvxWCzFjgDrwDVzYPkJwiezUM9D7b91CaI-6rSgqRC5pFIXVtMInH_dmcCsatDLW74ZwN1yfRfZAoqbvvXrYXS2rMVKBNoHM5Ew5lpKU09RPsvthrKUYAg1YHnon2oTHmUavmrhY8kanS8tr93mf4vS9B0xNAdkVjujdOOaMr59ULe-rLuvKh_KAr2GQlB_edAptGv2RQw6bjKF0Up4Few" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=FSyzRKiTxtxGc1f0IO84IM6Y9feuABiMqTS63tqQk-a8WVaIJfcdPRsaFBf-2AKu_Po4jg5wYjiCO6IWFjnpGGZlZ6UL7IVxBqVYhbfGKln7XJRG7nsjxiZ0fb5GuscRgjMEZrEahNkYZBEmv56plNYujnFjQQvZmXWA2ndkrXCyJDQxyPp_WzpI69j5wJ8fDO9mr4HFUShmNu3FMiA8xn6y17npCuSeSVUUMw7a_2ox75i1a5c0YoRodxqcc40hC8aMk9GcVUkJ7D_C4yWPAuEhUDWa7zkMhH8KPpjWXgdoJ18SwclQQ1oyA7DzoEcqXsm7442UPLy4oTj_oIFdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=FSyzRKiTxtxGc1f0IO84IM6Y9feuABiMqTS63tqQk-a8WVaIJfcdPRsaFBf-2AKu_Po4jg5wYjiCO6IWFjnpGGZlZ6UL7IVxBqVYhbfGKln7XJRG7nsjxiZ0fb5GuscRgjMEZrEahNkYZBEmv56plNYujnFjQQvZmXWA2ndkrXCyJDQxyPp_WzpI69j5wJ8fDO9mr4HFUShmNu3FMiA8xn6y17npCuSeSVUUMw7a_2ox75i1a5c0YoRodxqcc40hC8aMk9GcVUkJ7D_C4yWPAuEhUDWa7zkMhH8KPpjWXgdoJ18SwclQQ1oyA7DzoEcqXsm7442UPLy4oTj_oIFdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=HD9LkNT7-QyShMXy26Wc0Y8NAnSkWwawzM8ieXQA33aXK9PO61pI_7_9pB8jehCZi6YCYFpsjcAQknTpnMUz9_wxCaYuOaGiPZvsOrEEr-G38XIe4Umw7oyAY9Pmv37cZQMvg2lMo7_5coR4R9Xy7FpgH40unr6PYJw7HfmkF__hz9s-6OGifvxCTPN1e8RN_frd9b-bCSb5KZ4dolIi4kog0HWTQoUITvW88nzilF258_IGbMU1TONq5pwdIiKLE_iYhBUBJW225EVIgmnvoZBrjuUTCMvipDJdDKz9u0MbPUGBjN3-HbQQ72fZmd9QQxhkPbzZbjAJ-WMLxIGvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=HD9LkNT7-QyShMXy26Wc0Y8NAnSkWwawzM8ieXQA33aXK9PO61pI_7_9pB8jehCZi6YCYFpsjcAQknTpnMUz9_wxCaYuOaGiPZvsOrEEr-G38XIe4Umw7oyAY9Pmv37cZQMvg2lMo7_5coR4R9Xy7FpgH40unr6PYJw7HfmkF__hz9s-6OGifvxCTPN1e8RN_frd9b-bCSb5KZ4dolIi4kog0HWTQoUITvW88nzilF258_IGbMU1TONq5pwdIiKLE_iYhBUBJW225EVIgmnvoZBrjuUTCMvipDJdDKz9u0MbPUGBjN3-HbQQ72fZmd9QQxhkPbzZbjAJ-WMLxIGvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=Vicda7ALAV9DzLGWDCk5mGnGjQQgWOS6ecnpG6vEjIQwQzZreNA8-KhnUg6ifl97Bf6xKcQZK-nIrymz9mRzD_L5aL5a-Nz7C0Q8zl7Aw3xwYk_36fyr2IV-FBIDoHveCMgupg4jKHfFtp-6dvUOR_o-0lwoofWHoU4h3FfiB1bQ6neaBNnbLvtYV94t__dlPAhknjQ1ld1MHAPScsUBxKvBF8pPUS7avml7qhj6xNhXKSQuRitre2v96pDaO3TDuBeFbImFe4DHoP7uRmpIRK45yU6svw_nGhXPxmGidvo9iiTsOK1TGZE58EZpzaBDcv3bnYPcQhJZxSVGaLvzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=Vicda7ALAV9DzLGWDCk5mGnGjQQgWOS6ecnpG6vEjIQwQzZreNA8-KhnUg6ifl97Bf6xKcQZK-nIrymz9mRzD_L5aL5a-Nz7C0Q8zl7Aw3xwYk_36fyr2IV-FBIDoHveCMgupg4jKHfFtp-6dvUOR_o-0lwoofWHoU4h3FfiB1bQ6neaBNnbLvtYV94t__dlPAhknjQ1ld1MHAPScsUBxKvBF8pPUS7avml7qhj6xNhXKSQuRitre2v96pDaO3TDuBeFbImFe4DHoP7uRmpIRK45yU6svw_nGhXPxmGidvo9iiTsOK1TGZE58EZpzaBDcv3bnYPcQhJZxSVGaLvzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=XZ46e_A-TC1sTLwwi7_2anCrunHXSpL9rEk5v-LyW8BenIwocApBeV8hzAkw1VE6XAWBTVJL2ldvGs54n6uFaapiZcoFOBR25uueKWG891lAPpj6I8giPZhlsUDcawhuwZfuydtrigydln9_qYBkg4BgeMcpWzSC-A2LzIXMItU6HRYgBzIpmPCdWIkW-LEhNwalhPRivOnyz_WnwjT4KSVFLwmzA_FzwIria63lFv4eaPNaxs6Z5dFjvwtk44zMoFyb-aUodT4Z3IgVdXImcTgnN5Ub9VK_SihLgwFcgN2bEzTlQyS31PgxbPj4TdBFUnAgmD90lIVE5UK4sQf5pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=XZ46e_A-TC1sTLwwi7_2anCrunHXSpL9rEk5v-LyW8BenIwocApBeV8hzAkw1VE6XAWBTVJL2ldvGs54n6uFaapiZcoFOBR25uueKWG891lAPpj6I8giPZhlsUDcawhuwZfuydtrigydln9_qYBkg4BgeMcpWzSC-A2LzIXMItU6HRYgBzIpmPCdWIkW-LEhNwalhPRivOnyz_WnwjT4KSVFLwmzA_FzwIria63lFv4eaPNaxs6Z5dFjvwtk44zMoFyb-aUodT4Z3IgVdXImcTgnN5Ub9VK_SihLgwFcgN2bEzTlQyS31PgxbPj4TdBFUnAgmD90lIVE5UK4sQf5pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=ldDglphvlvG2WZMchxrQjzPg8yPE72gQwkPd0Kq4brIKDOObTn_-Am8wO037U0rLZYbbmf9vt1FwkYM3mOPIPbD1ayLAtKHv3M9HCTIoZF1E3TQpfnFRwa8nS_MQjPxZDP8neTqRPmJoBdcRADzHA6_rG0pIM5dBBU2yIQF4PPUK6EKZhVyvFGTrOsubTzqgoHQThwdEyTJI1mmJbxvH7pKdy8af04XVJYVyLb6gMQ9I7zx7DLJUfjujR9D8wRckrpyHMbZTs9oZy-Knf5IaeTv_SSfuSEMKJgJXPmzGR0Y9jLiw0ynFeDwKpzem-HqawoxYH3DtTOH3kK5n5phWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=ldDglphvlvG2WZMchxrQjzPg8yPE72gQwkPd0Kq4brIKDOObTn_-Am8wO037U0rLZYbbmf9vt1FwkYM3mOPIPbD1ayLAtKHv3M9HCTIoZF1E3TQpfnFRwa8nS_MQjPxZDP8neTqRPmJoBdcRADzHA6_rG0pIM5dBBU2yIQF4PPUK6EKZhVyvFGTrOsubTzqgoHQThwdEyTJI1mmJbxvH7pKdy8af04XVJYVyLb6gMQ9I7zx7DLJUfjujR9D8wRckrpyHMbZTs9oZy-Knf5IaeTv_SSfuSEMKJgJXPmzGR0Y9jLiw0ynFeDwKpzem-HqawoxYH3DtTOH3kK5n5phWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=Zu096tdsWhkzqN6zKeJO9Ueb2ZL8OPk9j1ZlhfvouPFwpruKf0VwUkd2XtMtxRmrZ0uNJ5t2e1aoWginq4zm_Qbq7fIuRrKMWJmS4kYeTIbHnHMJLMXfpDhv86z2mYyQ4S38Tgj4dRtbE6PoSt-FnxMZxnbFi2YSrlzAXcYUcBfaA17sGZVw_MDkiUUO3gY8l_gtRZSjyqVUhbAv44r9bFnvv0unoH9BnvuBbzP0xgi0xuARnwviHu04fz2ioFGTb22qKuSkj79vofgKYRPTa03DYYXL8Fl7hBG3V_1Yu3DcoIoFQbhK3oh6W8RAZZGIJiopipEcZbKfzSj4FmmQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=Zu096tdsWhkzqN6zKeJO9Ueb2ZL8OPk9j1ZlhfvouPFwpruKf0VwUkd2XtMtxRmrZ0uNJ5t2e1aoWginq4zm_Qbq7fIuRrKMWJmS4kYeTIbHnHMJLMXfpDhv86z2mYyQ4S38Tgj4dRtbE6PoSt-FnxMZxnbFi2YSrlzAXcYUcBfaA17sGZVw_MDkiUUO3gY8l_gtRZSjyqVUhbAv44r9bFnvv0unoH9BnvuBbzP0xgi0xuARnwviHu04fz2ioFGTb22qKuSkj79vofgKYRPTa03DYYXL8Fl7hBG3V_1Yu3DcoIoFQbhK3oh6W8RAZZGIJiopipEcZbKfzSj4FmmQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUVrZ2tnf-e-djFwZuOxGOJGVoemi8mNuoCSiFZ_dZogUnRcrWa5oGqLeWoeWk2nVZCwr3dLFuVsEdE5EiOJwzf20lC2Mix10TFZHnMZeUbqRt3kg5w1ypIrObsjlsfLocZTRdzA2-H6nVgCjcaG4M35Ayl16wU93Awwh2Epue2rpXJgPqXMbuvimhnfOlPUT7vjYHEXwzmVS0pS3V5gyFxln7BgwvCxt9Lp-S4kd83Lci0BOH9gJ6RMovQ76-YrG40EPeNDACvz70DuusnFeRfVXyV1VIbWNnTdnMhNvPTe4-j64dRBx1BdfC4MJjDVC7g36xpNmI3lywOU9dm8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=TJJRZkMC-1lOFTnnMBlzDfhih-aCb7ZGL3pV9nUqPBPTznwwvnROxI31m5vEFY40PHIDpQi6dif-ZngfNsoVA-Dt8tJH3nE47qcLF-3wJjRgAUOPeFRTCG8sVGLnZzJKCYWrZNYqHV4yTJZAiumpLHPtWbiMjxcEAGNcCw-NMaPe7cYTBvqxqSckl-tFk-wWiOTN_QExBez1VfEFosP9g-Cyg-d4viy6U-XxV1685qoENAuYpuXYypM4FhnXzx_tpU92sA7k1qPHut_WebM6Z4BU51mLOcX3lJgO2T0VR33_tJwtNYps0tKq9et3R1Qq_ATuMMFDqQqxDhgBBnqfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=TJJRZkMC-1lOFTnnMBlzDfhih-aCb7ZGL3pV9nUqPBPTznwwvnROxI31m5vEFY40PHIDpQi6dif-ZngfNsoVA-Dt8tJH3nE47qcLF-3wJjRgAUOPeFRTCG8sVGLnZzJKCYWrZNYqHV4yTJZAiumpLHPtWbiMjxcEAGNcCw-NMaPe7cYTBvqxqSckl-tFk-wWiOTN_QExBez1VfEFosP9g-Cyg-d4viy6U-XxV1685qoENAuYpuXYypM4FhnXzx_tpU92sA7k1qPHut_WebM6Z4BU51mLOcX3lJgO2T0VR33_tJwtNYps0tKq9et3R1Qq_ATuMMFDqQqxDhgBBnqfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo_90i6S6C48ynRiFXQ_4Kg4a44n9NgSViLvJBdep3eMrTh-NlE9cMWQMMqBiOWIkBueQ0cSnSPzM0MvMCQbLNRjjfO7E8V0gGayLVjZQl7iV7xThZXIM_XTWeOxS1pirAtLOikqWqoKL5B5OEzzq24s8zELmuOMgt_xPr1uuSAP3y5jLaEi2MmsRengNpVRkOqJEw84sqXn0vqidmLbOR0KL_NS1472YTFHUIO4JZTcZ5VV3QuETo3-xJRmZypBd-DEfDPRLZOiEzQT_tGIVW_On0ioYIVFSkkq10NhZumgKY5YIZqlLRcU1c22a6ZN3NPXftWBzGDWbFqRRFVPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=OFFx5F18rNk1ULJhXcbwtant5dQsRq9xfTOnxii23VYCtprjkCzdHeBFIm0JAl2NNsMQVAD1CLVvJataQTo4uxbfiRl7dPTtCVu_iL7nAu8ElwizozvTB6jnlJCVLnCVwvALgPrypxFpbmqi0y-P05QRmnukcUW8HzddpJgYhs_dsJthxgIeU1z7RM_O5TyHfM7k9mGtsikBEQubfs8cXSCDYZN3CijupPA1gQMyRjxhy7w6h2Ao3pxuAmu65PP2Riy3D4ON37BM9UOxbyK4WlPnd4-8Vbe-0MESIiG-ByBLg60d3ibCKohL-0CrYguSgL9zo4qL24ygKCQKknE1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=OFFx5F18rNk1ULJhXcbwtant5dQsRq9xfTOnxii23VYCtprjkCzdHeBFIm0JAl2NNsMQVAD1CLVvJataQTo4uxbfiRl7dPTtCVu_iL7nAu8ElwizozvTB6jnlJCVLnCVwvALgPrypxFpbmqi0y-P05QRmnukcUW8HzddpJgYhs_dsJthxgIeU1z7RM_O5TyHfM7k9mGtsikBEQubfs8cXSCDYZN3CijupPA1gQMyRjxhy7w6h2Ao3pxuAmu65PP2Riy3D4ON37BM9UOxbyK4WlPnd4-8Vbe-0MESIiG-ByBLg60d3ibCKohL-0CrYguSgL9zo4qL24ygKCQKknE1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=iKdQQa_NKqcLM6yWyKNLpXpyXp1sZ9_HHQXum_SlNATNtEiRQUbPolO0GXCsVdRYlFUBPHZ3u35Ckb9NMvAhgsPUmW5FrCYmAzkJ-1b9gFMBKWR85CLc7zV3N61z8OzmmTSBaJl2EDPhNkPedxRfb-nXXW6Tn0Uvg5ViWwsrgWZEoJxxNY_PMTf-qRCEV8B6-YJk8oNeebzjrJ-tyDLPOtjKITxdPnwcK-kBbn22sSwmIrPfpBappvOdQhI9E54WbY1PDZLL2b1PzPshbPgn5LZ19jKlu8rD8hUgI_Amn8UsnJYbhGiCjBzbaU--lVx3XKiUt5HJB73dzKoYrbt0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=iKdQQa_NKqcLM6yWyKNLpXpyXp1sZ9_HHQXum_SlNATNtEiRQUbPolO0GXCsVdRYlFUBPHZ3u35Ckb9NMvAhgsPUmW5FrCYmAzkJ-1b9gFMBKWR85CLc7zV3N61z8OzmmTSBaJl2EDPhNkPedxRfb-nXXW6Tn0Uvg5ViWwsrgWZEoJxxNY_PMTf-qRCEV8B6-YJk8oNeebzjrJ-tyDLPOtjKITxdPnwcK-kBbn22sSwmIrPfpBappvOdQhI9E54WbY1PDZLL2b1PzPshbPgn5LZ19jKlu8rD8hUgI_Amn8UsnJYbhGiCjBzbaU--lVx3XKiUt5HJB73dzKoYrbt0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkKpHMC8KKIMiPugGySacB2Pay28ILoEsyyjVqGJ0ujIGOxXZI1uH8jvr6Zm4QEJbG-kI-B5oc1G9vaN3LM850Cprl_Mgv0MyoNTIXyO694gQlv1mNR5iJY-VLTKdrmi023lhWtvzgrm44MTd5TxKFuWCELf6pTq6CZ1LyTa5mPXcioMgcucgqZa3G0LG4Tzquwip6Rw9xDfHe_21F5Rs80PqfJlb1b8uU-ab68RyiJ-oOToRP_BH4rqqPgXfzaFSJCFQxF-Qa1DESWNjoH2H0lI_q1i-yMROZ2IlcFgiPgzWbw416P78Rm1W6HnxOyGXapLGLEuYmTLV46Mcrxcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fefDsUD38o_gzyl_MT2OFcxmPf7nljDFxCKaGNRgC1dMmPhTiGZerZfWzjKFDWqtYUK4y-zCZAIqSHF6xkBAQjHpv9jNN3PdRaMNnXpugH2pDU3b_ftt7AxvqdyqbfEh8DtT6hfwkT6ZcWyXJrRUtwlIp88qO1sxWNqF58yRdZUKMqzx0Al7QuQrhleqaCoaBDV9dh3QQiPHj923rlFRjzUvNX2CYUqg2SIW-2GI9b-XzUalt8YvnSPCLadB3PkvZAJuciM0GB5Mz1iRJUa8r69y5in1vE84jTp0LI89-ATDiuDx7vZ8_zrvOBZQcIo2hV1YJsndbqKttklqRXdTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuEQd2RsppiNcL7EZWt2rn7BqVyLdFzPR0pITAtuw88NQmhRAqmvmBUC1sgdUfLNMHFjn0Eusxcv-kdkMrAz2GzWXx5tR459NpmXsVD0DMS8xZGWIFJl1eAfUC7L8ujPplcbJUAsCwzN3_gfTPBl3Sjdpxgajio1prsyhRkJH3ajqeWgxZx8_pk32w2H0xa-2rzpq3o_ZYHTmIBxuiKrBnTWyMygrM6PphGIJ2UO6D1A7oQOxzGkHsu8OwOLDYRrbypuJld0VQ1NCCYgUe4UgArKGfsbxWug8QivBqX0SHFqejGiuWkpqKDG6rOasC6s4Iurbz1mNKg-qVF1phtQWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=OyQpaelh0jmIxVl_dvL5ovuHsOX54VGZERmJHj9uOjrHS8Fn5CGRvyVo0yw0r4DRESDUJQIO9kOok8536GDrNQnROI7PDSMldVTeZZC50xTXIvvx5U9YXJAJ7c25GxLGh-9y9g1vrEOIkO1szIK6ICWerarx3MOXMscIqiTTzUDv5gz7DyvrhLS3-E99Nvwg2ppHvB0mPH8HEt88fpDeyqRiqAR8ahKp4Jdm82rtY0-t4E_ruj9DnECsYx-WgoqNpzLqC8l7kP0Km00N9VaLRMVlGzwSeZ9IMSNWFf9b-6S_cfPhPd2vxfmIfmeCuJ8xMW1FtJGKrgmgO5TF3HCMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=OyQpaelh0jmIxVl_dvL5ovuHsOX54VGZERmJHj9uOjrHS8Fn5CGRvyVo0yw0r4DRESDUJQIO9kOok8536GDrNQnROI7PDSMldVTeZZC50xTXIvvx5U9YXJAJ7c25GxLGh-9y9g1vrEOIkO1szIK6ICWerarx3MOXMscIqiTTzUDv5gz7DyvrhLS3-E99Nvwg2ppHvB0mPH8HEt88fpDeyqRiqAR8ahKp4Jdm82rtY0-t4E_ruj9DnECsYx-WgoqNpzLqC8l7kP0Km00N9VaLRMVlGzwSeZ9IMSNWFf9b-6S_cfPhPd2vxfmIfmeCuJ8xMW1FtJGKrgmgO5TF3HCMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=rC9mxyI9srs4LbAfXtylPT37IV9kw3m9OGhb4wuM1ZUpeGNnJDJfkbkEc_HzMyjLIhB_EZobitVufIrANOOhkHlqJNG3KriSvyeLcDnb_Tz1NLMaIrIDE_9cRLHMSUywsksMDzYXukDt47hKHQGcZmVjobNKbFzsTii7EEbsd8PLUzYc2upsV6SNYeyeRplyE6D76tp8xijfHfI6uTXJrsTFQvq1A6scT9aDWFcKWz-afjelJTU18mVh97dTA6ab78fTpsa5G-JCgq3MoYIPCJ5lIrcSgHeq7WCzykKbN5-tm_lTlHnNTcBt3mOK73j_tUqfRiXWvPeX_2SvqxDlrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=rC9mxyI9srs4LbAfXtylPT37IV9kw3m9OGhb4wuM1ZUpeGNnJDJfkbkEc_HzMyjLIhB_EZobitVufIrANOOhkHlqJNG3KriSvyeLcDnb_Tz1NLMaIrIDE_9cRLHMSUywsksMDzYXukDt47hKHQGcZmVjobNKbFzsTii7EEbsd8PLUzYc2upsV6SNYeyeRplyE6D76tp8xijfHfI6uTXJrsTFQvq1A6scT9aDWFcKWz-afjelJTU18mVh97dTA6ab78fTpsa5G-JCgq3MoYIPCJ5lIrcSgHeq7WCzykKbN5-tm_lTlHnNTcBt3mOK73j_tUqfRiXWvPeX_2SvqxDlrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qb4aQGGOb7GDYuja9GYjlHYVwuxGinieJWC6PYwToYsQt7reQKhxH6asXyUhDPZqxVxG2qzILwdfoQRsUZbPsaY2Exyznw5cuZlpdTgg9cnc-p-CgISyrGZvy_DaeHokEpevlsstyoNNLcLc7gxahWq7d-AMmAtePJoDAHZyWtNgOx28Dk0T38PFW_ZsbLxO5pYbuBUQLcxvbiUfcXFnkug-4A5Db_elOfjJUgES193bTz2dx0m240ltZNvmBW_P_jDnqhSbDXGek1AX4M3-PLX09HaU2B8hl0Dt5X1tSosU3GMOwQcBzuqy13A_dJVIMmHttZrhwqAZfQbSZC0-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=R1y8UU_CweeeJk5o2uHNL42VyyRabCka-CMErENhageHJVNMrwezltuEOVYTtmOAJMhmJT_4zgYy96yep3_Nq3LG_95FPG4NZ8etyrxipahCgxpo5BzPixdl6U6mijMYS0qVxcOiUhvZVxycsyXSfuuchaxw9QpKk3L2ugQfREMwdwQ8yyMnJSMPIjqD8NPPFE9AAkvBYUoJ-2r7Fg_er2j8CLw-ojj-8rdG3wFY156fmlaKgpm6HKuO-kxukeBYmCDnBePR9iTXIS8ZrmdLXvN4z4VHxyTbCuP3hCuW5VLvV8Nsos_cvnJUiF3X6QrVYPoZ6GM0r_210mohD_EY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=R1y8UU_CweeeJk5o2uHNL42VyyRabCka-CMErENhageHJVNMrwezltuEOVYTtmOAJMhmJT_4zgYy96yep3_Nq3LG_95FPG4NZ8etyrxipahCgxpo5BzPixdl6U6mijMYS0qVxcOiUhvZVxycsyXSfuuchaxw9QpKk3L2ugQfREMwdwQ8yyMnJSMPIjqD8NPPFE9AAkvBYUoJ-2r7Fg_er2j8CLw-ojj-8rdG3wFY156fmlaKgpm6HKuO-kxukeBYmCDnBePR9iTXIS8ZrmdLXvN4z4VHxyTbCuP3hCuW5VLvV8Nsos_cvnJUiF3X6QrVYPoZ6GM0r_210mohD_EY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VddnjlfHRO3ITamAp_BT6r_SD-Lu2-5-7L3IDXpYJawKF_2PvJIBsCm2Ku5ZKCvvxb3MdBS2Iacr4Eau9rOOkXGlM1cJA7eZJxA9Te1OauXCpIUzKcTOhjaxuDnSF4nZIqVmp0LBo0UodLZQZ-_Gg4lAI_1AMboKG5kUMEp9beBR3BTqGUZI11w7gD3YmLsj98g8s_-t7hog2ILpjlsuzcgntOSQDtxpglzGddtodYOWL-WNIDDHcS5DzUA1gp0ycYyu_uYQy_BwydlGshqO_Zf-cK3o0TZHl5mbb94ZbJaiGC1DcTNKtv9K3Iood9IOkawMtIvwcgJnO-rFPbL9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXFzmhyuN4qX0H3mXgfoGuXBXvBsCmtNJkaCAWothSI851FE33vg8Iu8Ab3o8Trv72x-fADVEEZLGwCthjVfwe2U2aH7GO05UdAV5Fq07m4A9_MlITY-88UJwiq9nU8Aer2RetD8tTpQrMIeB6z6OX9s1HzngwiAEV29wFD4deiyPNKCGs2mBzlxLdGmendGYhgNXBpGAg3GDfBrydWeyAsrGp8J7L9zs__loxGdveo5WxfVHJsDp0IHXSLkXnOdFIDTTFnN4-8cmSiRLqEY5__mkTpJh-6C8h08lyLrI8DE_3cAiFgNI2BaLrgjgmFHDtHblsINUrtluEycJw7svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=MuCLcPD5FcpJUT96-ZFquLn8E_eLFw8NDw91I6dCzuD8FWqFddBZBNlLayVGAUNHsPPfGYxEb03oC66qnE_CRhjgZMFT_3KxI_67OgDE8oqNw5HR3ydSps08Rq2vZ-lWJWKt19jqyAWebEvd8yWD9TWOVusEGDUOASCZt6UEeML-17-x4wXjTZRvG3lQ8IpF2safvQ_K8xtwJFO-VfyZ29urCAXIAqDpcgunNx0bijAwUrWNkFDql6j8KhLNRcqcFlU18glVEOvj473NKiNBcNxz24W64S4oSqSIKLy3mDOpmr_u1KPzHja-_3IcM9iW_UoKHALW1hevk_XE6DQ4XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=MuCLcPD5FcpJUT96-ZFquLn8E_eLFw8NDw91I6dCzuD8FWqFddBZBNlLayVGAUNHsPPfGYxEb03oC66qnE_CRhjgZMFT_3KxI_67OgDE8oqNw5HR3ydSps08Rq2vZ-lWJWKt19jqyAWebEvd8yWD9TWOVusEGDUOASCZt6UEeML-17-x4wXjTZRvG3lQ8IpF2safvQ_K8xtwJFO-VfyZ29urCAXIAqDpcgunNx0bijAwUrWNkFDql6j8KhLNRcqcFlU18glVEOvj473NKiNBcNxz24W64S4oSqSIKLy3mDOpmr_u1KPzHja-_3IcM9iW_UoKHALW1hevk_XE6DQ4XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9uuD7zznu6iyI1Qi--zKA9OaZU2nfXrigObX2YbernOsUmkndWq6Uu9p_CCN_fsAvw21g3k8MrRt3tC-dt8kgRkmqDyCdHIH67fcACsvwyvKfE0ikemLoICCpH9C4PcnYnTW8-3LHqlKBEW91Ey3oi9cJfWjSgvsmxs-bHWnlUu5VEHmvvnjf_FC41SnK3CozdnqopoG-HTtPZTgPjfaalTXGtjeHF7eSEs08eVvRAZdxhVaEaO07wGnVH3bOcWEwm1Ycwb4mW4T6yk3aaQUeOzWgYqbazI9zsCMy7Fy_k83Alls69eodopkZzyl1ncyRYm9rGHiRKklxIKW_6ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YN2Jlp-Dz8OrKtTzvPGkCp1zxsvyHWhEd0GeHZa1fhkt-PUrTsHBpRJ7DWkcalxUDvQeU6bgU2aPD_WdODA2sVhKe_-1rPdWonDifosWlcYWbaxJgAt15TTPHWdoY7Dpmmucx7Ax7CL_Q0AfShjg_4_IX0UhrrOO01oodVzl9qZ25-CccnPgtkqF5G0bXz8lZ9W54fOrEPqMUbqqSVVms3MGKnEG6EiyjG8iy9aN-YJVhHBXzKanCqLsaFYgKiknBTizU9UI4aORbZJXKqTLkmNHJXTzfa9ZraYjR3UVkKmrj1WCT-grvByxKn3VCaPe8wI5VW7LUzydDbliRwypvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YN2Jlp-Dz8OrKtTzvPGkCp1zxsvyHWhEd0GeHZa1fhkt-PUrTsHBpRJ7DWkcalxUDvQeU6bgU2aPD_WdODA2sVhKe_-1rPdWonDifosWlcYWbaxJgAt15TTPHWdoY7Dpmmucx7Ax7CL_Q0AfShjg_4_IX0UhrrOO01oodVzl9qZ25-CccnPgtkqF5G0bXz8lZ9W54fOrEPqMUbqqSVVms3MGKnEG6EiyjG8iy9aN-YJVhHBXzKanCqLsaFYgKiknBTizU9UI4aORbZJXKqTLkmNHJXTzfa9ZraYjR3UVkKmrj1WCT-grvByxKn3VCaPe8wI5VW7LUzydDbliRwypvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=OeWCRz7xDfuK067U3WjrzTqEBiSCvseZPRXwyvpjdt9rcxHSSl56xtIaFOr9jhu9ujTjcwVRAdbHnTAHzHHYddDl8TisBPxafvgLuv5x5-imZLBWW_PM5vZE1e7jnrEiJ5M78eoX2PnUMsA7cAlDAbznl2WxOc5hLQdIcsg1anZFF-cjikgs_SkR0N9gp5DgSTGTNzgEZaOYkluvcpzqG8dIjT-QlI6bHn1m_hbkAWCwEYQBOSPb-01MsHLGN8j47yuSJaWjprBmCnwYgM0HSWV1OylAXv5_lBS0d_LaBrDlQm3X6JCJIrXcJA-m2GvfR0FK1rfR2MtQ6j2LClygzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=OeWCRz7xDfuK067U3WjrzTqEBiSCvseZPRXwyvpjdt9rcxHSSl56xtIaFOr9jhu9ujTjcwVRAdbHnTAHzHHYddDl8TisBPxafvgLuv5x5-imZLBWW_PM5vZE1e7jnrEiJ5M78eoX2PnUMsA7cAlDAbznl2WxOc5hLQdIcsg1anZFF-cjikgs_SkR0N9gp5DgSTGTNzgEZaOYkluvcpzqG8dIjT-QlI6bHn1m_hbkAWCwEYQBOSPb-01MsHLGN8j47yuSJaWjprBmCnwYgM0HSWV1OylAXv5_lBS0d_LaBrDlQm3X6JCJIrXcJA-m2GvfR0FK1rfR2MtQ6j2LClygzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZckPhrt-HkgR3fnIwNAa5YQ5fJBczjOl0I8eKUnMYPclUGKhfrzftr6-RVOX8JXRxsw9yoY_7dk6TMYluRHjcsN8zH0-D4lTQbBI_ymZvXETLcGF67ucenN7AxkG3ABPsiHRJYO-5YBks4sl30g0xI3GO5FzINSYsaKjHE5ruA7LoQi3klPoc8dB2W1d_RXqMLB05dRiaUpclAy_4XDJujRi6ZxEVdXGJyu6QvNrNyJrDLcTCFvFMad9OdwJuJcQdJMVoTWhMo98aNknydlgYQa8szgQilizx2Ypgw_7Oqsi3mZJHCMp1dIzAdFTwkIth92G5eNyxd-CcojN0botIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODLVbuQXIuJfjcU__rUO3TXMIt4sa_LkF2hhDY9Osmjy2FYsEpv1C5wTKyHO_hTQzwHc34jGQU6l8xkRjd74NyhLamtjUmHXfIBDzYbitHWBCm4DbBVFsgHALgin6ppSuU36p-YjpLdCWn1RR6w3bqLEP3qU4-4_CzviZeMXU4sgereryv3b8L6sgfVpNXR23KX98T0E7VJjW17aOpA-nY9ey2VpSGI_QWY6PNp6Tja9_YdX1qromdl8jztBRjqHzeSpYGk_3yV7B6M4q0OFqcnpKXzwVIAY2eZi3Tddn_Qv-z7uxpl6569NdA-T4IiCs00dHMb8hGohAsvhIVPjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=VurJ-GElgduJx5QEK7BkajEFE1L-ftsScUYM4pf7m8Nx0poiK6Jqjo8fxKj307PyLm8ESu_TyPgMDm8xH3RAeeclECbPahLIjFf5uamx7ZqvFH9ZPhWjYbPtcFqVvz4bJWSqP3NhESNdgM_V1vU9ZRQ7x2btKlCkV4KdCsT6tIFUAJOXzJMhL0aPOKLJJ4Zsp-y1vaFg1Cp8KXaRDqL5CWk1iDdpEaeY0EzV-QxkcHSeT0EuCVwAfaVLTUiLDv7B-x9uyfJ7s9p6koRRnGDL_LDyJHbDFibPOMNQ9U-RODUsHgWK91UHd0feWPj5tgkVfxLjkALMBcJoaYMcddEQEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=VurJ-GElgduJx5QEK7BkajEFE1L-ftsScUYM4pf7m8Nx0poiK6Jqjo8fxKj307PyLm8ESu_TyPgMDm8xH3RAeeclECbPahLIjFf5uamx7ZqvFH9ZPhWjYbPtcFqVvz4bJWSqP3NhESNdgM_V1vU9ZRQ7x2btKlCkV4KdCsT6tIFUAJOXzJMhL0aPOKLJJ4Zsp-y1vaFg1Cp8KXaRDqL5CWk1iDdpEaeY0EzV-QxkcHSeT0EuCVwAfaVLTUiLDv7B-x9uyfJ7s9p6koRRnGDL_LDyJHbDFibPOMNQ9U-RODUsHgWK91UHd0feWPj5tgkVfxLjkALMBcJoaYMcddEQEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISSFzaLCP8FcyVClwbm43N8tELueJiDFTQvUXuU6rszYpszCE4ImrCB-2GSFF98By7vHvPuOBj9pDcITe3u5SZchqykbHIHULeNh0T-fVeU1DBYZRyOvQm1N0d0aKEgVJHpxATBhRrzB5Q4RvVKIahXFXN0NlKotzvCs0C2L4bLwwvi8PDw7_ENp1ly5sxJu3iSM2srxS7DuklTMTrET-LYarnbB67CUfwjh36EjtnWK0skJGT-pMpK2jRtEZ64c-zljYTVcBi9BtqCTdD2-MqUEfxTJbhpL4_rQInEj7SrMmLDyPzmcD1eOyxdr1EMXt2a16ygkc7_-HaMbZilRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=eK516Q8Tl_3PQNlrlVafOok9JGN6PJ5SVKq1N2KAm29rCUy_9PvyGkyJB9OEuxho54gDLpMlGAjiIOOIo-L6isjrIk9ATPKhamrRaUWlCBuRoG4yTli8ueOO-AYZrT0tGc10Q93DndBk_rUYnQfv43wTavUv5qYUXPS9nwmE5Pc6nBrhaFd5saox07MNSF8xwIWTSdxisOM5oxXwacTPtUMSATUUai10RiMvg9npyGeEiVolLmAVcJdk3I3HQ1R5c2vXATa9PCZPL9R2uR4r4pPuLOyWyLQdvnktuRpZLTK7oIxM2ulHuN5pa1MJaEcox0mRZ-4bN_NUsoxezjalWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=eK516Q8Tl_3PQNlrlVafOok9JGN6PJ5SVKq1N2KAm29rCUy_9PvyGkyJB9OEuxho54gDLpMlGAjiIOOIo-L6isjrIk9ATPKhamrRaUWlCBuRoG4yTli8ueOO-AYZrT0tGc10Q93DndBk_rUYnQfv43wTavUv5qYUXPS9nwmE5Pc6nBrhaFd5saox07MNSF8xwIWTSdxisOM5oxXwacTPtUMSATUUai10RiMvg9npyGeEiVolLmAVcJdk3I3HQ1R5c2vXATa9PCZPL9R2uR4r4pPuLOyWyLQdvnktuRpZLTK7oIxM2ulHuN5pa1MJaEcox0mRZ-4bN_NUsoxezjalWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHzyu_IuF_splkh1s8-rLl3DH_jdvq6hwbNmR6V8rpZB50yzSnr4pMr8djv96XuyCRWARwfdqrO9rmLxitPpGx4gX4G3mJSa--8-uoguLj4E6ZTYie2bMji4fNTTJ6SdXYD1YjcHCfMLe09u7Y4x-K6cDMw1ryzVDgXkgVdXv0_dBZxG_hqq6HoolueepW9Z-l5urZYQNsMfRzsbpGu1LjSOM8mzAUeElr5kh5R2aCTSa3oQSGTKZeIuUR_wQtd_ZmtiL1h3LUOrkXS1m-hl3Pg_VZXTMuUB7NLGcOkDNI6rVbUsCQTy_M2cTRUILlpnEstk8CHc7kKbofz-LFhC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=C3QG15fYeHGO3fwC_Zr0LjtdxZp-jRytbKvDWHSasyJEwRzawPG3bRqRFH9QSsWT82oiMMEDc5WakVzpt1A_1itxQdwQfSFENjpP2Nag4WOUQKTCtkHTupqelEKuzQqGJMm7tYDJS05seLx67h1B4x5U9Q5zjzy1wSC72s461bd67xoTxQ0mYycXSTAjOB7W-7-wH6xmpB28cSIcq7A7hZQL4RNgMFANAkSy9YuVQ2ii05QmrAnDcna2xegvOV5nO782J_OxMPAz4DMtwmq17mItENhK-deTU6oeEZKm7nQdFIRLKaAQK8ZJR64xirV788nnf_yATUVLUGrhr-F4ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=C3QG15fYeHGO3fwC_Zr0LjtdxZp-jRytbKvDWHSasyJEwRzawPG3bRqRFH9QSsWT82oiMMEDc5WakVzpt1A_1itxQdwQfSFENjpP2Nag4WOUQKTCtkHTupqelEKuzQqGJMm7tYDJS05seLx67h1B4x5U9Q5zjzy1wSC72s461bd67xoTxQ0mYycXSTAjOB7W-7-wH6xmpB28cSIcq7A7hZQL4RNgMFANAkSy9YuVQ2ii05QmrAnDcna2xegvOV5nO782J_OxMPAz4DMtwmq17mItENhK-deTU6oeEZKm7nQdFIRLKaAQK8ZJR64xirV788nnf_yATUVLUGrhr-F4ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=A-ixdZE7j57Mq1rDG8s7SexxWtyTroTrFGE7_FhGNgMTuJGk0NqJRSHmhRGR7jZGU78vJgOe9muGVnBDtYkQfI9Gzfa7fkNA4FjM8LITAxvqIpahuKg-PerybWplUUykkMtRgSAuuB4ylsjL5DFXXYslSiMyHVxhmDFi27-EU0mpkvjO9pueThDJoAWt9qzND7LOZfUCB4C6hWry94mifGmVaSYwrmLTLXKNF_vMmMKlAwhGBlPEkNawCnOolym4No_SX5lX5v5bBVCQ2S97WBUTCXbTHI4GBLQCvVqE3s3dqcklI7hkc1Uvllb-Tn1zVbZdcaZ0OiOG2iExvrABeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=A-ixdZE7j57Mq1rDG8s7SexxWtyTroTrFGE7_FhGNgMTuJGk0NqJRSHmhRGR7jZGU78vJgOe9muGVnBDtYkQfI9Gzfa7fkNA4FjM8LITAxvqIpahuKg-PerybWplUUykkMtRgSAuuB4ylsjL5DFXXYslSiMyHVxhmDFi27-EU0mpkvjO9pueThDJoAWt9qzND7LOZfUCB4C6hWry94mifGmVaSYwrmLTLXKNF_vMmMKlAwhGBlPEkNawCnOolym4No_SX5lX5v5bBVCQ2S97WBUTCXbTHI4GBLQCvVqE3s3dqcklI7hkc1Uvllb-Tn1zVbZdcaZ0OiOG2iExvrABeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvRcdVzfP3EYvHnAcIEfAR5-ZVqmBdepuC3J4BhEjq-P5tomRnNAc-4-YCjnED6EYt3rBy8K7CvFh6fJQhv0b6Fq_GEZIYqiX6eTtLskTYFE-Bka2KVV2BWSwGq_gpEg4H_bJSKf4PW4ci_QnN91V3-rDeDzbAE-K3o2n6YnXe8zP17KJRnA5xMkKP_8gSzCln3FPFdNyt0jYHHNSvNqS1kDY1lzEtulTnb76EeRW-agan3fmQdIKuxIJ0_6L-VRtpUt1gl4tSKHc34Uw-YTb9Tkk4zLoca5EPfw0mgY7bpAefRG4E_nJy0X5vsi3HB0R55tX_79nJZWUjUIu4ePsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6mCA0XXQ3ECD9Eim7B8V9ehYxgpIBE75Yaz0UgBgBBYl0yLDZ80tj80GGbAnDHTQlL4Z3jlLDs2vYb3nC64HmbHDq7s4ZttCIgi4_eLFovL04jIQWpk7gaw0pZjKp6x9cip4KRSmbO2phIHu6DdQVinllJjky0srkWKPEQxkkkxxhV4wEAxIgUSDp7XCARm11D_DuVzwUlMKcyhYnR41SfXDCjICZ41fp5ZRIy0NpEjdhfGYgW4uXBK5ZZvFtPDxk0pWm0yT5TQ0nEk69cG4K47gj1DUJCH0RcgEVCrsb-M88XZ7HwOP4VxluaSQOoWOKH3smVYpHbTfXMajFQaPLU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6mCA0XXQ3ECD9Eim7B8V9ehYxgpIBE75Yaz0UgBgBBYl0yLDZ80tj80GGbAnDHTQlL4Z3jlLDs2vYb3nC64HmbHDq7s4ZttCIgi4_eLFovL04jIQWpk7gaw0pZjKp6x9cip4KRSmbO2phIHu6DdQVinllJjky0srkWKPEQxkkkxxhV4wEAxIgUSDp7XCARm11D_DuVzwUlMKcyhYnR41SfXDCjICZ41fp5ZRIy0NpEjdhfGYgW4uXBK5ZZvFtPDxk0pWm0yT5TQ0nEk69cG4K47gj1DUJCH0RcgEVCrsb-M88XZ7HwOP4VxluaSQOoWOKH3smVYpHbTfXMajFQaPLU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8OKAoE-VWT7_z5vPbwVGOdJMcenK2oC39huc_KupUtriyOQRpTgUteHG9UTn2WqAfWbdlokvH-JMqP3CGhpuZHEOyBmdhIIIuhrrsb_7cgERNAJ-dDW8qpz4qQ6cPkN499etluZnUUhAyUYuzPS312ZeMl59D8vWRvpGnJ1iRXy8cEtVPqmXJQ55UkOksXihTTYL7cLmj2PpzY4Ouw2lNVAPiZg4KEFASR6hvOlXtITSVzke8oRot__KzcurOoKo8pXCeCk6ZD01cqhkQrI0_Wv7VPgJh3bbkgqrhm3TYlpGWdAOfp83hYKz3Y3McljzH_OBfygm4lrWOw5XlxO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfoo90hFiqaWaTS5_8zlUgqXbvxrLG0-XJqsrd__f7uaEIo9sGjlHA7lrGycoKMlbJrgne5P1KAvInrs0BVSF4ZlWtHHFOu1BaiweAG82v_xmknQviZH-UmOqXbBE8aqjZu8ZF7I-8rAo6XnpqZWH--MnxKf9qOJmlP45is4nfmx2m_g_37fNxEcYuknuSh854UyMbq8IvfrVKKFLPuKW6oHxpG3PoRP1a99f1-s9elH2qNoD_H82U5SyAA6Ett_qU4YYohCG1itdp2t5V_tPCf-OTt9ixJ14gKm8iCCeXcmrbLYBmjOMF-qH3v73-qzajX45kDRs36_B-bkpk3S8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=r-aMSVAFoQumrqItNkA2wlJrUBesXCUVFDFldMxznH2_Yd2qGTgtxBNzUFAh6bQb45MCNmBSjjZmR--et1oDzWsY6ia-kvk6pa8yb1WBQD6yMbghlw1lolvaX6MrRHBFS0ICvvxIuCjeaUbgEMhQAxRmPxnzMxOfALaVmfiMoE6fcDnes-n992Siv4DMfwXlt7HYi8rLybJROOERZiRhSLLG04gB98mz3jErlaHWkHPH4q0Sr6s5hKNNfZxfVb0YY0FH8llTLXCn9y5hLGb4cdwFsAjFiDaiPenY2dtXfN-oacZbqbDonfRgw-jMyvdZKLTznFEh6fBISGaLzw_trw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=r-aMSVAFoQumrqItNkA2wlJrUBesXCUVFDFldMxznH2_Yd2qGTgtxBNzUFAh6bQb45MCNmBSjjZmR--et1oDzWsY6ia-kvk6pa8yb1WBQD6yMbghlw1lolvaX6MrRHBFS0ICvvxIuCjeaUbgEMhQAxRmPxnzMxOfALaVmfiMoE6fcDnes-n992Siv4DMfwXlt7HYi8rLybJROOERZiRhSLLG04gB98mz3jErlaHWkHPH4q0Sr6s5hKNNfZxfVb0YY0FH8llTLXCn9y5hLGb4cdwFsAjFiDaiPenY2dtXfN-oacZbqbDonfRgw-jMyvdZKLTznFEh6fBISGaLzw_trw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=NuDUvrfX_4BpM2TAa993vfpHZIfxOsdll-V-XmT7Rn9U6qLXGJzMxe5BtS5FHHpr_ZQf02GGeTTAbTJOqNGV7UI53C80hYS22stSeWQUobshmliQkiTW2KlLcCJai3n6fi9aR1vG5B2fdYFbRSGeq97Pir2xx7N4J5SlCO1yI4eYDhEwccZ55MfiiA1L3qiym1Gp3YE2lcEDBVfjif0mRPBaYK12fPIPl8SSeK0NEamBu2qQdRwJoXjeKCfvShX-XYgG6ze8RZZfXiX5-fyli3u8azjyS2xzTLK4DN-v8-uqn8neSdx6pv_kVLNDRna5c4CB6ZE9KK8xmuWvnkmHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=NuDUvrfX_4BpM2TAa993vfpHZIfxOsdll-V-XmT7Rn9U6qLXGJzMxe5BtS5FHHpr_ZQf02GGeTTAbTJOqNGV7UI53C80hYS22stSeWQUobshmliQkiTW2KlLcCJai3n6fi9aR1vG5B2fdYFbRSGeq97Pir2xx7N4J5SlCO1yI4eYDhEwccZ55MfiiA1L3qiym1Gp3YE2lcEDBVfjif0mRPBaYK12fPIPl8SSeK0NEamBu2qQdRwJoXjeKCfvShX-XYgG6ze8RZZfXiX5-fyli3u8azjyS2xzTLK4DN-v8-uqn8neSdx6pv_kVLNDRna5c4CB6ZE9KK8xmuWvnkmHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=AEHEdP75TbZoJpHx8hZZoVjIIyhONjKg7S-I144JN8I733haV3MtC1ooau9x34pNhmXDcn-uBxstiptbvhmWcryTCm_pko4OYsjLAfCJx9WEGkCM8hoyRHCQ9CzdpOt4qQEZ3eSzbwkUoo0AqKB818hrppKXdrLBcONugcWUT_WxuirvNSBHxHeWcwhrtnfuITI6UAjKZ_8HwHQA6rvwrGfzp4S3grI9ukLgHKg3jh82OK3GBqNP79l8Mcq_FTYnurMLGE3OL-q41C8bhfcg0Fd5j3NHkLafqTYTKwqXdOeirhfVtLBbe12z8SdIK_vG_aDrJzD2TTO_9O3SSbnDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=AEHEdP75TbZoJpHx8hZZoVjIIyhONjKg7S-I144JN8I733haV3MtC1ooau9x34pNhmXDcn-uBxstiptbvhmWcryTCm_pko4OYsjLAfCJx9WEGkCM8hoyRHCQ9CzdpOt4qQEZ3eSzbwkUoo0AqKB818hrppKXdrLBcONugcWUT_WxuirvNSBHxHeWcwhrtnfuITI6UAjKZ_8HwHQA6rvwrGfzp4S3grI9ukLgHKg3jh82OK3GBqNP79l8Mcq_FTYnurMLGE3OL-q41C8bhfcg0Fd5j3NHkLafqTYTKwqXdOeirhfVtLBbe12z8SdIK_vG_aDrJzD2TTO_9O3SSbnDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=d8UTW5s8zPVsCl5VYNlWksvwgNXVL98GyPTd96GLfkEXliIIJR5IM2nL2JJUp42tMGR3W3TAjVgMBITRqZpQlujAhqaBdBm6BuVN-LhdxbQZ9jq_tx3ui83HGjjp_wVf4CkAziV6G_9UbKfDZmaXtRax6FUQi5gmXHyRxvLD-ihW6OZ5JR_kFq2c2yq8gzQhzohpA1HPrnv8s_xmcZTko6icXJVlcgGeRd7HyRshCFYd2lBIJytnobZBu1PIGo2IWNcWx0g_ASBQeud5eNynfbLxH-iiqMoZndXRVFWCPk30Gvpv91b6JvbsCs93VoqZy59P01Df2jeaNhZfp3SCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=d8UTW5s8zPVsCl5VYNlWksvwgNXVL98GyPTd96GLfkEXliIIJR5IM2nL2JJUp42tMGR3W3TAjVgMBITRqZpQlujAhqaBdBm6BuVN-LhdxbQZ9jq_tx3ui83HGjjp_wVf4CkAziV6G_9UbKfDZmaXtRax6FUQi5gmXHyRxvLD-ihW6OZ5JR_kFq2c2yq8gzQhzohpA1HPrnv8s_xmcZTko6icXJVlcgGeRd7HyRshCFYd2lBIJytnobZBu1PIGo2IWNcWx0g_ASBQeud5eNynfbLxH-iiqMoZndXRVFWCPk30Gvpv91b6JvbsCs93VoqZy59P01Df2jeaNhZfp3SCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AEl9SsHIK2CXp2zp2604AslT3acsY0u9dpZS6WzCvU80IE1BFx_KWv9rqu8xTYwjveyz5iw9Ak5sbUb7hzPe0mHl_U0Ey3WR_Put502GGv-8RFOIL_2NrgGkPSpF_psp7JHU_J-mmWZaXaILKSsG1M7GiwFCOJvSjSPjLjIGRf6W7vqf4AT3Ri41oJ072FiuH-cqVt6PCIV_dal-F_pmwmMbmNda8u1p6CnmJY_T8soopTGHdrtEJ-YipaXWKCxts7PWfoY_VtAj4-rhVuIxjfz3dhYL9AXieKMf1Af0Y5J5gH71cl5JbTiXEGgD3WZ1362CqF90o7LMaJsii9swPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AEl9SsHIK2CXp2zp2604AslT3acsY0u9dpZS6WzCvU80IE1BFx_KWv9rqu8xTYwjveyz5iw9Ak5sbUb7hzPe0mHl_U0Ey3WR_Put502GGv-8RFOIL_2NrgGkPSpF_psp7JHU_J-mmWZaXaILKSsG1M7GiwFCOJvSjSPjLjIGRf6W7vqf4AT3Ri41oJ072FiuH-cqVt6PCIV_dal-F_pmwmMbmNda8u1p6CnmJY_T8soopTGHdrtEJ-YipaXWKCxts7PWfoY_VtAj4-rhVuIxjfz3dhYL9AXieKMf1Af0Y5J5gH71cl5JbTiXEGgD3WZ1362CqF90o7LMaJsii9swPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=v2_8Vpf2hSR9LdK_rZTOwcP1bOfNCHb15nU-fkO6U541RB_qDRdY85XVv6XBVultH9JmZyTAfqc2MRkiThFY5cKzEEJsfbh90sBIvDIrsx2OTnGM33LmWIQWu_4HPZy-ibv1xnCWFh2bY7ln7z0yKF20Qfr6cZ5cAVXu9ZNHEtU-zu9NkevP3Do-BI5taqFHfQsoyhj093Us5DN2vbpjMQyR3FjF_DuR3tJhSbp6YvuVSEY11Wicx5GzuK5zy8y_XETjc1sMZGXpGoPiMIADvT8RKDUZrHSAJVMvIP_o5sHGS0kVCwf-7Xpk6GvP8xEA7DVCSKGPouQMm3uy6MHCFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=v2_8Vpf2hSR9LdK_rZTOwcP1bOfNCHb15nU-fkO6U541RB_qDRdY85XVv6XBVultH9JmZyTAfqc2MRkiThFY5cKzEEJsfbh90sBIvDIrsx2OTnGM33LmWIQWu_4HPZy-ibv1xnCWFh2bY7ln7z0yKF20Qfr6cZ5cAVXu9ZNHEtU-zu9NkevP3Do-BI5taqFHfQsoyhj093Us5DN2vbpjMQyR3FjF_DuR3tJhSbp6YvuVSEY11Wicx5GzuK5zy8y_XETjc1sMZGXpGoPiMIADvT8RKDUZrHSAJVMvIP_o5sHGS0kVCwf-7Xpk6GvP8xEA7DVCSKGPouQMm3uy6MHCFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=QMM01Y0QRfMpjidmafnPQK_yH_-rfbi8YPHSbmLRnLNQW-xnEtW8Ba1Pm2Fgm33Ce1NEEY3yoNY6iqpaHtExGvmrkwQAFjyq4Gt5M54E03chHDE_OLwCg3vyHU2-c0tyL6Y612cvnuaudIG-UfW71ykwLWaWgPzsLQMgkVNqfe4CluNBzOyMX_BtIXFQ8ou-bmhfqaBiRH4eXjyYA1A1tUeHNFLzoly6UijiZXTJd1MzHVc59UzB-NLf4NPm_dpZzz6WR8kFkIKO1lFyYBEwnSpESdrcA8VqwsyoQ6VBchCGWJR6zT6MwZvxWXGYqIwa5EleIpb7MTRaxTaR75hhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=QMM01Y0QRfMpjidmafnPQK_yH_-rfbi8YPHSbmLRnLNQW-xnEtW8Ba1Pm2Fgm33Ce1NEEY3yoNY6iqpaHtExGvmrkwQAFjyq4Gt5M54E03chHDE_OLwCg3vyHU2-c0tyL6Y612cvnuaudIG-UfW71ykwLWaWgPzsLQMgkVNqfe4CluNBzOyMX_BtIXFQ8ou-bmhfqaBiRH4eXjyYA1A1tUeHNFLzoly6UijiZXTJd1MzHVc59UzB-NLf4NPm_dpZzz6WR8kFkIKO1lFyYBEwnSpESdrcA8VqwsyoQ6VBchCGWJR6zT6MwZvxWXGYqIwa5EleIpb7MTRaxTaR75hhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH1n_fCBwvMwa1hrx3eJ110A2_GfR1rNOzoznf0mBNfn9tsCV5-HdpPijEATfqiysnZpBb4dAuFRsWhmWkLjCN4aaBIs9qSr5fNLm8gMB1egc0Swyu5507reMsZ0d7020x_Ll2pWYxdLnbtkMiCrryozVONZVMQvdn8_pL9u3fDZIIqsQa1oolOzMmwVS19SVHx1izU2YlPVdVpR0S0ascnjvmuVzBHirZ-0oHnDjdwMFIU5x7FluW-EgQn0yjmR9alVyoj58jvw5EzRcEdmPSqGbpZ3ZTh1ERXleQ-UyQfEZsrj1eWmgOzZEq4RmdrEWR-MRF63t2U1o3oeHF8lkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3XHJ6_XfUe_yARVeybhWEBC3XI8M0xPRQw3Vlip1qiE3a8FxFnvez8vQb-Q48O2gCAf9TPaMC0z8MVT865ssl6LpWZlT384dsK-IUyWMhRrew-c_pxZYfcaPFQ1BqnXJM2Wlz39UEVW6mpspBEooFZjEuSSVSkfsfpsURNBtxMEIaC3_UYU5CTyX_qAOPKZL8jKdaFKxsNgkg_TEDTUtSA76QAxvs4wSp3HJghch3qP99klohrnPG7nZgd1o7_jwqQWrBO3TumkwpOr7J7N88F8OUi7dnBxDG3glzV3fWC1X7xQ3nNO1EkAsb7bpqAd4fOIStfg7HrGdraesX4bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UlnaVYT_FYvCpsdH5zK7zIrBgNKG6xJ7kaNUMXdgMMELkBxdmOeHTIWc5qOKgZNO694Bjv1vnwUSHK4jMzgq4qfAm0PpQXrJZRImagqxfIPub5P_dhYeENJnKYuNxgF1ppLHMbrU_owzKBFA8_e76UUCL1qpC31CVnxsOSpcwM90R7w6j74v4THfTzAFus9kTJk0mKxodHgy5N_k7i0oBtFLvDIuDKUm78dJ2jL5NYWeOntqugRAjNFTzUXSKBTvhQ2dVX4E9S7msAyHO6YQ7lKJ8oZbpjVuzm5BE6mJzExpGg7J4k0kpdWQPjwllqhhOeVbXqivI-qiUhFAyO34fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UlnaVYT_FYvCpsdH5zK7zIrBgNKG6xJ7kaNUMXdgMMELkBxdmOeHTIWc5qOKgZNO694Bjv1vnwUSHK4jMzgq4qfAm0PpQXrJZRImagqxfIPub5P_dhYeENJnKYuNxgF1ppLHMbrU_owzKBFA8_e76UUCL1qpC31CVnxsOSpcwM90R7w6j74v4THfTzAFus9kTJk0mKxodHgy5N_k7i0oBtFLvDIuDKUm78dJ2jL5NYWeOntqugRAjNFTzUXSKBTvhQ2dVX4E9S7msAyHO6YQ7lKJ8oZbpjVuzm5BE6mJzExpGg7J4k0kpdWQPjwllqhhOeVbXqivI-qiUhFAyO34fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=sAF78h4tCxD2oVT_NFsKdntbu8KU4cdnyWULQLdum7y8_ZZsM7xTXZnWW3CGW7vr4rPwqAi7V1gSHkFMFXq_bVPFWw5sBjKK31YIMbTXmRJQC-h8AdTviVllxuTRqeKxGPrxu4HdX6u-razUb8l9tMc_Bendl4BhVPfFsdKxdVpRu_ncv7kABzK6u_yrWwDIu0wsZ1qkfznqenxY3zcobQq-2V2wo2FHfFG_j8k5tW5Q8qYCxMygwNA5JqxuhGJKOvTSy8T76BXi0D44nkdBswEEFUnTnMkLTOVr2Xdt2PVHJlNlS4ilUvM3EOj7bUG-Wyw9shlSLmtMH1fK9QxySQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=sAF78h4tCxD2oVT_NFsKdntbu8KU4cdnyWULQLdum7y8_ZZsM7xTXZnWW3CGW7vr4rPwqAi7V1gSHkFMFXq_bVPFWw5sBjKK31YIMbTXmRJQC-h8AdTviVllxuTRqeKxGPrxu4HdX6u-razUb8l9tMc_Bendl4BhVPfFsdKxdVpRu_ncv7kABzK6u_yrWwDIu0wsZ1qkfznqenxY3zcobQq-2V2wo2FHfFG_j8k5tW5Q8qYCxMygwNA5JqxuhGJKOvTSy8T76BXi0D44nkdBswEEFUnTnMkLTOVr2Xdt2PVHJlNlS4ilUvM3EOj7bUG-Wyw9shlSLmtMH1fK9QxySQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
