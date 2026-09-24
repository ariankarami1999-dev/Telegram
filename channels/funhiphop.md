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
<img src="https://cdn4.telesco.pe/file/oUgmBj3vJh4rP-RssZh4ouOyeV4EjuIKhHmK5-MCDX-lD46_FrrJ50-aUiT_w6yS4b7e1g-Yy13VtNTNZ6fFf3WqxQ06yKR4CJlATgD3fTXQ-cNikAkES35Sqohhk_Inh5irqSvhg1N65tYgS9e6Ht1CJ6GcmCBJ2j_re4lHPN6XyX67YVNTMgWIBbYN3giZCNht0mrLBPMKs-Te33l892eDE7Zk_jmfb02Id5Y65uMrrRPKkRJ0KwnGz4YVxVnwgY9GhkQPyuejMIoIAkQnv5VJTlDl6jy4QjmIvEV6wWT92ubArA-lfLP2KE90WdRS-r1GYRDEcVdH6BWTC7w-Ag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrLx1Q0mydHwYrRpCjQNavxEjXal9TbLu2U6czPqHmvyc0Az5Zt1jmLL7ysbs7zlFloI2zEqEOBAGyKhAWN7n8CVG5ytoO2Il9KsxFRt82B4DwZ4zinZHQpWXxwTuwe76ZOkmA4sUeWxP5lbOlxv-84Q9GgEx5et_gPjQWDeX98EWUyasNdvL_Yb54zBQ8FjwU0V-14nbP2pRDF0Xlr8jX3Yv4TKRDhBPQcA-klufmUM8mrQ1fE30SRhJYfF2JxojO8aHXYcQmpBuq9AQ2lCxfCzKjbOzgDKWqrjCyNxeWxADCQseeKN24xw3Cf_CNnH1YgKmHXze05JY1Ot4eBXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
نروژ - دانمارک
⏰
ساعت ۲۲:۰۰
🌎
📲
پرتغال - ولز
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R2
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/83987" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2YVqTxm4VgUjzDcEWmm2ceOZePjyvoBveAL8yxleGFkozK7_HeRM5NMcNx4qFqyDja0vk7OZKWXs2v4ySMZIi33bf46XdWkNTDbi5ng1rnBgvAZXuwG1EvHPIlFq3XxGdQCmL5Qg8myIKQh9gS0WlBQIAxAdWC4RPesXjVRsSzQAwnBMR5Cvl8gVdJ_Kq4hls2RzoTja274uYm8hixGfFEXGTuvqilujCm3AW2NBnynKMigTNHk3q4L3EiJG6cXyMQBTL9mxHJ4zQu_2139zCmZ5dIQ6y36Pl2gQWWomvsCgHDyly4jIL9qACujtuCz9fPAxVHt2zJtUri79dU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqT5TXjtXU-txeLVa2BpnJnKe7W5BIHVlC4BsyCx33EThEDaSnW6S0h0eTMEf7fwGMmGdIv-PlMU2_NIN_UD93JMo1PbLXi5TneriMOAEqNUQrWrVSz7fH4lqq3hK3_r3vTVgHbbY47Rx1BdL6xxWPwFownp--ltH9oekj3yED5kZUZ0UJlTaZsByS9Ewte-JJiXfykDfWungYASFNtU-IHEHxdfvvslBUyIDQTrx5kbmXZAU2xNmy5dG-peQX8gY1AOwUqpR2SWmw_1GZ1l-xRmguCDODuMNuGXps1JMmOI71HHj8qd001M4q3IOjJC4yGPqEpa3zNh6BmpP0LT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9Ot7l_u5d__8hTa5VR5r4wGc2weEqayPxljOGW_gp54BhIC8T69LbW8En7xqw4NGaaiubuATXeyu4As8iIvxiuDfU2gTamKd2gnkk7WoEg4g7evINteC0P26G-t0EgwAOmhTfzim2cukgELGMViaHPI40r8Wd1xdUdktai9lel6iMRA2FtXE3E3tHqnEKkakXjCjw7nXwXVoLCwH7y4Uh9_N7l8nfDtBAglj2B8hWhjdk3MvliG65De1eAEsUbJh9SNKxoz8cQHfgKHRt6E3rNDQLZPx8WyG0wmi1xs8Es6AoON4CSjEDrj2m9jSC9KwI_Wl-lHMMSyovfRo8oxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBuk1cOj8Oyji_CdM-JJpJAnHL2EM9fzATwkWDo--EXCeXy2Hfxzd4jFnU6aAyJdug8GSjANMWGiS5oqBCcJZjehJi8DsFDHKhOGK9x9IroE9NQLsrmG8aIrM14hp-K35MY_v34tZhPGQKvgv_5K2Qx6lY0h7OyOKpQc9WsLu5RKtPBy2zjmzBmkjp_z8Q9I97yhruYMiQO-kqOGybgYt1LPuW1qzKuALb5MUcGv0a35XHKOiGVhm4aeCpo73HsqEhqqb0dnMJw7qE5ermz_g1ndF8aRdWxlDKP91_6EfJXCRCW0J6rhe4OKO-2uCp1uDM7LjZ_jQ3woPW4pCYSEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrlmhVYgJfOqy7MFcBBirTlU5Z8eIY0QyBBZ9hgJuq5cOfzFnN0ymB9Rt9vqgarYlFwT8y60QE_eSuWsp5vGS3b3bDig1YTd94UgkvwiD96aqcqnwn8cqhgGw6xdBZTq10RXvEI6IMmf8oGuGnFr6Z7pRPlXLQnk9ljcQkvy8moKiiBMb6TFd-eOeikiYke4ZMx38cNmA7d2HOwDB_ADtdiXKzBIevXC9h7CRZBS8dkLfKeXXJ4Y0AoiZbFrECVTAh0Fb50-u4QKfJmSmTQmVEw4Q6tov2mHVpF321-qalj1HUVEGIiTWq4wdzqvTpsyp-8YwSW2aYaezpEuReYY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=g_8aiWwacjQSxLzL-UPvOzDdzPeiPZboxIJWoKuBsBr1qvvMAMmhM14VGnPxb32SpWbwq_m4aUagYH3MXRGNIS7k5fOeZGlf8W0hX6s5idPqoCjqQX3gjSwcbDl95h_E2peASjpolKVdbNk8Yy9bUIrBXvaElAhMIg1tdoaPLWFZ9slnToe-YizVwAXVqjFmDZZID-_BkowPgg1YF5raE3avKWKmFZeXQHWOr3SvCqv4yMVyWcn19Syhl3geITUme-O0Ar7qP5pRZ5a3CpPxEgZBmeYBsWMdEN1SGyKbZ8lcaJwjWFCWEiQaLbMKhvnyoSOLcIoQT_216DXoKLXHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=g_8aiWwacjQSxLzL-UPvOzDdzPeiPZboxIJWoKuBsBr1qvvMAMmhM14VGnPxb32SpWbwq_m4aUagYH3MXRGNIS7k5fOeZGlf8W0hX6s5idPqoCjqQX3gjSwcbDl95h_E2peASjpolKVdbNk8Yy9bUIrBXvaElAhMIg1tdoaPLWFZ9slnToe-YizVwAXVqjFmDZZID-_BkowPgg1YF5raE3avKWKmFZeXQHWOr3SvCqv4yMVyWcn19Syhl3geITUme-O0Ar7qP5pRZ5a3CpPxEgZBmeYBsWMdEN1SGyKbZ8lcaJwjWFCWEiQaLbMKhvnyoSOLcIoQT_216DXoKLXHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VskAgDfGalp2Z1arubtsp3Oo4qSsHjjxQl68wrQ5e99UQXd3mRVLJBOaFkLthzX05mKPG1DCYKQTe913FlKQVbP14H_1nTPZiEQuYXZqzdOOrLnHVl8e5psR32XX7bhdYcbd8Rg3dTu3kLov1LK6cT3-eWf58fOx1VjB_qynDbTV56t2TjtTxVLgHdk7g47oZNI2MsSAHgP8TSWsH3YmHEx9D7c-_msXZpY7eE82Y3sBjoxzwfaPSOiws2-a3R7TROdtBim-0rPvWLt0Pcq5r1DmRyEcspJbJURaDxDD6yQnYuWEAM15N_ZYsiQGnslNFxRg1W9KgrTRXhz_-Hoh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی دو روز شکل آدم بود باز طاقت نیاورد ریش‌هاش رو بگا داد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83975" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=JyR52FRsqZVXS_tvn8895fTxIMK3VpIkqg5din78zw5hhDwyDHYd8ukaK9qr-JaRfw_uzfVaHgHypG98YGSKGa1V_RLpPWR5Y6XzVn5KnEBWfUUF4iJzm6Vl60gvZqOFTqgjeUFo8KxWVZmMjtRrtT9CCGIZnzbTvrQrB2Ib451lvHv71eycLbN72XwrM56K1ERXONuvWWLapxIsHRSWrOPHoX5ydsEzG3uL5rgJjUjuRRNwwI_UvEBqefDUGnNqB31rxSO-m9XgFukjz4CDL03B9bCAQoEXn8B7pd3HQkQbkaEcHCpc-gcJKIR5EsvaiJw1nv5NQmRYXu1emZfJ_KNvkncC-IARk-uVQXTNTAO7TKdDtVdzHDpTa07NqLK64RcRGQ2PvP5O_FDxVa8w2FrCr6HWuUeHpFKmRQr-IOtfzivZljPH7gjMEXBcGaRBTIzoXqngTLtSxcyiUvFfGVtdAJf1xQppKzdDM75pemD1ae5HGQ9eVJqCeFcm644dfiesF72vUeph-kBpi5PQ9M-maXnfQ5X6aN9E5z8SCWsEVGwGVroev6ZkrNXl6JInOgSC9FxqBjSLde6VxjNQlGBBX8qN0aALy9eNi0wpmbc_j9ZkgFGxNy71cdPUlJtys6hF838TxojwQSoxbMhWCSlGM8ydsHNuIrOU3C8kwRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=JyR52FRsqZVXS_tvn8895fTxIMK3VpIkqg5din78zw5hhDwyDHYd8ukaK9qr-JaRfw_uzfVaHgHypG98YGSKGa1V_RLpPWR5Y6XzVn5KnEBWfUUF4iJzm6Vl60gvZqOFTqgjeUFo8KxWVZmMjtRrtT9CCGIZnzbTvrQrB2Ib451lvHv71eycLbN72XwrM56K1ERXONuvWWLapxIsHRSWrOPHoX5ydsEzG3uL5rgJjUjuRRNwwI_UvEBqefDUGnNqB31rxSO-m9XgFukjz4CDL03B9bCAQoEXn8B7pd3HQkQbkaEcHCpc-gcJKIR5EsvaiJw1nv5NQmRYXu1emZfJ_KNvkncC-IARk-uVQXTNTAO7TKdDtVdzHDpTa07NqLK64RcRGQ2PvP5O_FDxVa8w2FrCr6HWuUeHpFKmRQr-IOtfzivZljPH7gjMEXBcGaRBTIzoXqngTLtSxcyiUvFfGVtdAJf1xQppKzdDM75pemD1ae5HGQ9eVJqCeFcm644dfiesF72vUeph-kBpi5PQ9M-maXnfQ5X6aN9E5z8SCWsEVGwGVroev6ZkrNXl6JInOgSC9FxqBjSLde6VxjNQlGBBX8qN0aALy9eNi0wpmbc_j9ZkgFGxNy71cdPUlJtys6hF838TxojwQSoxbMhWCSlGM8ydsHNuIrOU3C8kwRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب رو بیت کاگان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83974" target="_blank">📅 20:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCEzUImEpmNKflA6dZ-krzb3GCE_Dc-IkQML0d7aKE7u-tLozg-k3mYVPqDkrXiAMad9mE_PEY-FHtBKIZs4hc3gEycpAAI0W0pSC6vP9G2bFkE1IWn38Gyp0yvanlys5Ue0jQWHDVutGrXmdBEqumuJBSrbj34OmOrDmKeyXSfD16xkO55a98KVuH0ytMAl1CRB9ZNNVZVlE3DhCQBtZ9ebMwH6BCb70aq8wz_NUccwRD9aM1U-zcRmMXi3ErPJVFLcymub7zjWwFj0TXLpiKY3-OgFmVQb_1Oq1QMxUW9VYi6YAMlcp4Ac1WwnvRjXoYIFs05cCJZ6e3BnAeFSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف:
رئیس‌جمهور پزشکیان فقط از طرف یک دولت صحبت نکرد؛ بلکه صدای یک تمدن ۳۰۰۰ ساله بود. او صدای قدرتمند شجاعت، مقاومت و قدرت جمهوری اسلامی ایران بود.
زنده باد ملت سربلند و مقاوم ایران.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83973" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83972" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=Zh_ho6ug1s4E8Peu-1PLIxcU3wrYJY6jDPVjf6LUjsCi7xLm3vYYs7dTwbgwn5t9ejlTISRgmRH0DFJy40w2tEHwZhdmaoV5Ot-xYSn2JRCQNdeRgHLN_6nY52tBta4FBPLjJ0g5C4RbDPbtAz-75hxbzBZkjsIxiAEKscThwPbb11OAOxDIBxevcFMtNG5QlMjVLKEpQMtczIUADa8PWhUDEVCNZvXIjjzLs5NFlspfU4RqbQcgp82x1T3yDxcwQMAqPHxdN6tpp32QQjh850G550-IVrBoMVqqcVw2C6-iXXGrFyWQuMulMbyI-bYI-RxQN1zaFqMeyC_0k0zj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=Zh_ho6ug1s4E8Peu-1PLIxcU3wrYJY6jDPVjf6LUjsCi7xLm3vYYs7dTwbgwn5t9ejlTISRgmRH0DFJy40w2tEHwZhdmaoV5Ot-xYSn2JRCQNdeRgHLN_6nY52tBta4FBPLjJ0g5C4RbDPbtAz-75hxbzBZkjsIxiAEKscThwPbb11OAOxDIBxevcFMtNG5QlMjVLKEpQMtczIUADa8PWhUDEVCNZvXIjjzLs5NFlspfU4RqbQcgp82x1T3yDxcwQMAqPHxdN6tpp32QQjh850G550-IVrBoMVqqcVw2C6-iXXGrFyWQuMulMbyI-bYI-RxQN1zaFqMeyC_0k0zj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g1
🅰
📎
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83971" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=Iz-nB-H8fFFaDo-CBItZ4TaJqJQL1Yd94DW6LfNzeHUu7I8u38JaXZ6cUIWvB-XwLlD8ELLwsSlwZn2zknXhqm9kIDF3DdnjL7cNaFj_c0V8ETeJY70JDQDilg1zO6L9zHm3gsIWCDKuSJW2lvKW9PXQJmgi5Q2Xxm_sc65Ex1ACh90_Htwq6mH42ChdFb25VD6xeVC-jr0vp_LXk21ulh02DI4tU_yM4FC8ylQcCIgcvPp8ZFUj7ZUvloderCpNJa9tIK52PUhY5N6O0LfvVZUNM6s7FY2wfw3iC4DVI5ondYBnpqAy9q_zzAhxapOuX5g6vzpVZR6f_QBjJWfS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=Iz-nB-H8fFFaDo-CBItZ4TaJqJQL1Yd94DW6LfNzeHUu7I8u38JaXZ6cUIWvB-XwLlD8ELLwsSlwZn2zknXhqm9kIDF3DdnjL7cNaFj_c0V8ETeJY70JDQDilg1zO6L9zHm3gsIWCDKuSJW2lvKW9PXQJmgi5Q2Xxm_sc65Ex1ACh90_Htwq6mH42ChdFb25VD6xeVC-jr0vp_LXk21ulh02DI4tU_yM4FC8ylQcCIgcvPp8ZFUj7ZUvloderCpNJa9tIK52PUhY5N6O0LfvVZUNM6s7FY2wfw3iC4DVI5ondYBnpqAy9q_zzAhxapOuX5g6vzpVZR6f_QBjJWfS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
من فکر کنم تاکتیک ایرانی‌ها اینه که فکر می‌کنن تو انتخابات آینده دموکرات ها پیروز میشن و اگه پیروز بشن دیگه ترامپ مجبوره بیخیال ایران بشه و از جنگ خارج بشه.
و خب جواب من اینه که خ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83970" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تسنیم:
عراقچی دیروز خودسرانه و بدون اطلاع دادن به نهادهای مربوطه و مجتبی خامنه‌ای، زنگ زده به ویتکاف و باهاش لاس زده و مذاکره تکنیکی کرده و برا همین باید توبیخ شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83969" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حین سخنرانی پزشکیان، نماینده‌های:
1. ایالات متحده آمریکا
2. بریتانیا
3. آلمان
4. فرانسه
5. اسرائیل
6. سوریه
7. لبنان
8. عربستان
9. مصر
10. امارات
11. الجزایر
12. لهستان
13. سوئد
14. دانمارک
15. کانادا
16. ژاپن
17. جمهوری آذربایجان
18. مالزی
19. نیوزیلند
20. استرالیا
21. جمهوری خلق کنگو
22. اکوادور
23. قبرس
24. ایسلند
25. مکزیک
سالن مجمع‌بین‌المللی‌سازمان‌ملل رو ترک کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83968" target="_blank">📅 18:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=qWS8Id2905AqN-crspFgdXd2Km63Cx3bd7CqOPBaAPf9ygsycVuxYGwDsA3jTax84e4tmPozvgMTJUS_OEFRsw5RFPJDzRluHw2xt-iFik0uV4i4Qxjm63uWsb93dxLpidxGrovhbpmz4HKnPzFKba4cv-aUz51mY24312ghCb8Sb3HL3eFX-AueRAbLST4gqb176hkeM6rdMAFsHkzeXUh_2OxWzdAVjOrhzyb1mpJ8_zAJm_HfosGw2IU9tIBcVy1sMrmtZ08zlqxhEq_fUl5Tau_Fp60gwwE9PIqDEDSkrBH4v1FvW1dZLM9E5qtq-FLeAWXQRPpdTWPpXJbURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=qWS8Id2905AqN-crspFgdXd2Km63Cx3bd7CqOPBaAPf9ygsycVuxYGwDsA3jTax84e4tmPozvgMTJUS_OEFRsw5RFPJDzRluHw2xt-iFik0uV4i4Qxjm63uWsb93dxLpidxGrovhbpmz4HKnPzFKba4cv-aUz51mY24312ghCb8Sb3HL3eFX-AueRAbLST4gqb176hkeM6rdMAFsHkzeXUh_2OxWzdAVjOrhzyb1mpJ8_zAJm_HfosGw2IU9tIBcVy1sMrmtZ08zlqxhEq_fUl5Tau_Fp60gwwE9PIqDEDSkrBH4v1FvW1dZLM9E5qtq-FLeAWXQRPpdTWPpXJbURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQlowjNrAj9ghhEjRRohHZo7X0IzpC3yULyJy6X-6R2cZkhKazlerJ9u2lD23z_t6vucKAcMlOT8CZ8f9xkbZThCIZyjuAKrnP3ws5_W2E45RoTxFKcqeOAc5KSPYdAuN6a2dBwPehBX-NMzphGKscdmOOOOm_3JSDQV5R-7CP121PKF9JgaYbGNxU4BX-8Ww85OLKamfcU3Y2i2hduzpDIwgZ4X_IDNKpnyW8dXtdvgI-EFfUQ8BqG7I7UgzaYEpuq5ChhvSRL5CLrgA13AgJiV8TH8xn8QVibtruNhOj_UHsMs2bE2dRTEJepXNzBF1_dGU3xpgyPr7mDzpaC5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOQCUqxlBItLEcGLQMqj0B4aoAujkKDur51p36Qoc29Tz4MpwyWNzb0PgNCEoUH40TtNvkznTOVs2yfJDgbKf4TevaBNurD45v4LKDYrO7kELtujIm_7sUc9EGom60YSY1zXNVAQNAWmCENuXdCvVlQ43aPswUdcvPJeONAHyj1E00LMxlDs2gM81trzkO825TnFRzDYjfvM6rJspUaFqWzh607xG5Tx3DHNkR3pxg1bx8E0A3AubYJDrg2h2K9S8KWi72G_OJSl63iWUtfFDV5DMVSPd5J-Vwp8hdIXnXOI3LXeYhe5tIRX5bZz2rLrvGpFI2yIO1ibRvjZ5ceH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwNncMb0fHRNhbAQFPyhmTaY_9MoqviAqM_-z474fA2Kcf4EJFNWuFU7t69knTwSvHeEaAsU78LZp1xefF3AFdCLWg5C5ALjQdz-RCMTOiMf5uvRJipFYB__S0lCn7-nBepsB5sMe4WhxqTGEDws5fPgSaXFbbG9rqDAgGT3O-8dy6TYubXw8Hgt1OoFuH_FJyhoOPo88SLwSEByeDgJpVMNRYFH1pPhs31tmbKcn3pqIbnCQ8er-vlZvTI67IMILVgCxKcHMVZVWs8wfHQmF1VmxuOeM2QkIkKJwMUMk8TG26dN-nGKnMaRMQxM7lPj7uq8E56MLn1LAVNUsWr2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بترکونی رئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83961" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کوروش وانتونز:
به زودی یه برنامه یوتیوبی میزنم که هیچکس دیگه نخواد چنل پوتک رو دنبال کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83960" target="_blank">📅 14:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">استاد خوش چشم تحلیلگر ارشد صداسیما: کیری قوی ایم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83959" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شرکت کننده های عشق ابدی قشنگ ۲۰۰.۳۰۰ سال وسطن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83958" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spYebKs-kY7KdhIImP8dUyT9FwiwAuIs0xlbv8o8nT2kkzSjvD_rSZ2xOQz2zMot-WpZzJMgeqE9RFvPK9dkvcQBBjCcwnWvI-Rhbt1GXbIxVzwASUTuDQDP0OV0lz8vClNKjKNY_SJ4vV89bhhkbFTLM3lFxnLzDovCM_Q2CqoQL6sadSc4FUlmPaiAr-lPEdph2xZUe61i9H9O3mAvBS9bJMmWdcS0Hvx4bt1cFs1zy6R-Cu_euAQ5W0Boxc_FMacQk6ix2z1NcPitkOwGKxWS8lYfCItp3GaWpJLoeU3-fAIrYcg5zLI-iJHAqY0FvGRQug9jKBzMY_YefD69Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالتی هستیم که تورم به ۱۵۰ درصد رسیده، محاصره شدیم و هیچی وارد و خارج نمیشه و داریم بگا میریم، به دلیل بگا رفتن پالایشگاه ها و پتروشیمی ها و کارخونه های فولاد بعضی اجناس تولید داخلی حتی ده برابر شده، تو پمپ بنزین ها باید دوساعت صف وایسیم که ۲۰ لیتر بنزنین بدن بهمون
و تو این شرایط دغدغه‌های ذهنی ویدا سادات:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83955" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBZL3vU1ZpdOylI-T1nw1phsCeT8BKzxHy7gAgziskxmi8cFqnWydqAFTCFCfFcYKrP0Lh9xYL4iZE0E7ip6LM4TD1wZMfLpwMv2QQlO9dzZkPKH-ukYg90-AISbn47qWH4lnRqWjztt4zbMZ7WBQ1Y4E86cCcLADuVHoSpBsGNp85jmB6gU8O7oNdUVjeE5hsCRGfGD2y35EUFAPWxJ5qKP47ywvS2s3BLPFbMBMZ1wMeUmT9sxtCOaNtrjRmLPqXctt6tf8Vpt6WRZ26cO96RlFDJ5d4Mcuj4N2Xcm8_8S-wBKK03A4lIDfaNTVTgJM154SaEaHhF1m-651axUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - اسلوونی
⏰
ساعت ۱۷:۳۰
🌎
📲
ایتالیا - فنلاند
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R1
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83954" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp9r60Dws6k1O3osF70gbOSPr8WtlxEsY4mwb56Ncv7wggjSAc8jKirCsJYwt2qc2HNGUNTRrSHzhykF2kLLQyeRqTmKiVnd4LHAngGMOKPPAnvm9tB8L1WPn4gbFsMxhOiP8s-z9UHYc6He0K1PURyKvWr7BQF5repxb3i5xUUkzmDA9vKvzYO4USp-_NQhTvLaVrF_2s-D5NkVrDGWT9aBkqkF72MycB6pYnd_LB7pNwjrqvTm_tMhUnHEifbJrLYoOaMXvt6_Te5O-pNrh3aAMN1rGbhlvdxPcTAIZSrBQqcwu5zPo4Sck3E23xWd5Ux0VUjFw0hHC-byzHP1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان بیژن بودا، از خلبانان نیروی هوایی شاهنشاهی ایران و از اعضای خانواده نیروی هوایی، درگذشت
او سابقه پرواز با دو جنگنده F-4 Phantom II و F-14 Tomcat را در کارنامه خود داشت و از خلبانان باتجربه این دو جنگنده به شمار می‌رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83953" target="_blank">📅 09:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اونی که امروز نمیره عقل نداره، بچه زرنگ امروز میره با معلما رفیق میشه از شنبه دیگه نمیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83952" target="_blank">📅 09:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مدرسه چطوره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83951" target="_blank">📅 08:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8MFXBf1sVAPznG9isdJ-erK3FY0vMcCuSbeW8y08jZnLlTlK2WyTQ0OT1odxrLnwYA4Lu8lpwbLy6MITr39ENHw7ZgIgafxJy9Tkj3wshq9OOyFS87CcqNqCsxPykpoWK9oOoYA2qTmaIa9S4k-7Vv07WikdJfSkSbxPsALLtcWkkV5lmWVjLdGYkw2J57K5YdXBHt2rZspw0OHLLougVnVOC8ZuQD4T4JbH6YKpfpOY0xjpdMeHG57ntnWdd-HUTSZpMtJ816aJ2iN78-Q5C0d3NPmWQkubU7UdN31gI-4ZNQnxjOw6TojnbOKNW980anFKDRZNSXlRWDR4cXBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=qGWCr_LBD4EH4XCdKZVKuorLCCqTIBKuQmVeqH3v1QstW7jFiSe0pgie-Q66d62hkk0gZXezDssYnMlXAzb7vZ07kVCcDitGrK6qR1ZISoUFaZynXNoAGoszI19JLy1CRZ4YR0q1IgRFdubEV3iNe3dzM4Mw9DnPMA6-3Nezbn8tEHYF1wt2Qxho9leqvFtpUp5bZZuQoI1WTuJBtTU_J3CDPAL7fzQ69ojmfCn4gxdORSaX1plFa8B2nDztsAmBQ5N0klHR6vZAPYcXOjZ78xsMKdcTxPv17gGEjtFG_7VXKl89MJU8Jqj6_VPaDmZzcEw5xggXDGeNwbp1vpn1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=qGWCr_LBD4EH4XCdKZVKuorLCCqTIBKuQmVeqH3v1QstW7jFiSe0pgie-Q66d62hkk0gZXezDssYnMlXAzb7vZ07kVCcDitGrK6qR1ZISoUFaZynXNoAGoszI19JLy1CRZ4YR0q1IgRFdubEV3iNe3dzM4Mw9DnPMA6-3Nezbn8tEHYF1wt2Qxho9leqvFtpUp5bZZuQoI1WTuJBtTU_J3CDPAL7fzQ69ojmfCn4gxdORSaX1plFa8B2nDztsAmBQ5N0klHR6vZAPYcXOjZ78xsMKdcTxPv17gGEjtFG_7VXKl89MJU8Jqj6_VPaDmZzcEw5xggXDGeNwbp1vpn1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ_XsRvaC35ZkwaCmJg9Yg7Smospx-j-C4N5fa2fjHVngeaVe0HFUWBQhBbW7C4MsgfcrHK91X0dK8YNAc-T4NV4b86K-u3caVhoEAmTV4MTZ0nZcFALlF59gte0RksbFx_1Cer2w-WX3KOLbAbG_mUREwP-y_9YLC4tgt2G0yUhxotdnh8D8AiewvnOsv-Std43si7EpkbNhLi3gzs7UOebHfdSWj9Kklshw4xcIMv_regbDTdP-0R8Z-_upe8lWNB80VqGqXFlqqUrQjbIeHFgi9KMPYm_25K_IxGrnyO8UBcKb1dphXg7OGYcoPt2WynjdU6gPYGx3AUrXk3MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSRmtyfmwtTmADpjrYDK5DuHFHojtSL7ym7M_9FogwmaoSivEx0PiV4TOTkORsHpIdGGnz3O-n7fR95m0p6aNlrXi8bIQRH_5m8F2fBMN-KM-RIpk0Ar67lZVVBe5EePltdzG8WCwgvPAVviE6BWxAU2hIDRx6ZYJ0wL9mHaRt8YijTlT0mDI7TZkN8qRIWJgFN_G7KoUVcH4X06i6akGJahbOqY5BS9sNioR872i_hZnxfR4sSf6tbr1hx2FqWJPiqrJfLn8e7K52vju8v-VSObht_2fHTavtPk5RTrjdHp70OxTGHolg1s2AdbNt8jujatn8uzrT_oGayHEYaCQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=hpTvLAvgshHAwIziDkl03XZSQfOB7ESexkiQ8KoomQqBrU8ss1OAAzTpwMLF_HliR9Coj51Ns1J4BMyuiZSD4sUU4RDM7Ye8KkSaFoWBlQmcVIekkAJw8hh2oeAtDJh1tOF1myOXWbvgSAk8RzSXQBDKgp61fMXOAUL4wdFcFjAJi-0V4AmIltc_30VDMWfYIHfRSsL5qUSDr6FupwDXnB6o1BGmDV3SMzym57mGmFD4vA-p6PssrK76fGAqkhD2McGrX9rIdt2SQexBaL5K1dD-5oONkxQU9hxDWpn0j9s8cdHCfLOpFTAvszPnYtspzCySFH30qNJT6eVEq5sqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=hpTvLAvgshHAwIziDkl03XZSQfOB7ESexkiQ8KoomQqBrU8ss1OAAzTpwMLF_HliR9Coj51Ns1J4BMyuiZSD4sUU4RDM7Ye8KkSaFoWBlQmcVIekkAJw8hh2oeAtDJh1tOF1myOXWbvgSAk8RzSXQBDKgp61fMXOAUL4wdFcFjAJi-0V4AmIltc_30VDMWfYIHfRSsL5qUSDr6FupwDXnB6o1BGmDV3SMzym57mGmFD4vA-p6PssrK76fGAqkhD2McGrX9rIdt2SQexBaL5K1dD-5oONkxQU9hxDWpn0j9s8cdHCfLOpFTAvszPnYtspzCySFH30qNJT6eVEq5sqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx758443Z86TH1ktgeMGNP9g4uIXeDzSoqkW8SdcNEsWAUBYY_70CaecRTXpEfGYCy4_YPyr_G6XiKDdLnecZkwk5J7oaezF0xmkt1tmXZ-8-QpG5eXd4UwkjnnmkwESm5gRApNx3jnmZqmnigE-ehhSy6veK_bXG3fKPfYB-m1Gtf7yMzRKCG7X6GCyNjYV3ves844n9cCUR9Gjfc28jxBmAES8UgN0-zSemQ_OFbvTfJ82Ey_Up5Ty4YAJ3toRHqPIRLmzBKIYP8nbEBeutAxgInNmVZGnmA8diuSCuX_-RwfgS4afm4c6RbWe6JEwQqTbQfP2ukUT6SL97xrMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8382999db1.mp4?token=DRjzYnKUG0R4xXowQkDVcwdVNS4I-0cg4-fGBcfpBJtcuaovOwSoGUZAHWjGr40EBG4mLPV8XByQV2ITwQ-MVERkmvFr19mt1C5hoQL9Z_k_jaklaovhF6CKW6W_yILY33lzUsXd3ezekNDPg2PvWctKwKuUI5JOG3tuNiPEB9iolzc1uaBAnzJd1IlsP-TcUwtnFib0yEG6ySN5mDBDSl3suiNrW5jKDL6JEkQ7I-xKtsSXj5vRefhSkPzTK7DRnumVAj-2w_UX7zgr7JevLawJLjMa_KTHletpsnqARUWQBa4tocjUnRC5qaWkf5LYso_4IiZXwBPlLpJS_lxROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8382999db1.mp4?token=DRjzYnKUG0R4xXowQkDVcwdVNS4I-0cg4-fGBcfpBJtcuaovOwSoGUZAHWjGr40EBG4mLPV8XByQV2ITwQ-MVERkmvFr19mt1C5hoQL9Z_k_jaklaovhF6CKW6W_yILY33lzUsXd3ezekNDPg2PvWctKwKuUI5JOG3tuNiPEB9iolzc1uaBAnzJd1IlsP-TcUwtnFib0yEG6ySN5mDBDSl3suiNrW5jKDL6JEkQ7I-xKtsSXj5vRefhSkPzTK7DRnumVAj-2w_UX7zgr7JevLawJLjMa_KTHletpsnqARUWQBa4tocjUnRC5qaWkf5LYso_4IiZXwBPlLpJS_lxROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو سرحال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83936" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان تروخدا شوخیاتون با باز شدن مدرسه رو تموم کنید، اینا انقد تعطیل بودن الان از خداشونه مدرسه باز بشه چند روز برن مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83935" target="_blank">📅 19:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سالی یه بار یه خبر میاد که یه زندانی حکمش اعدام بوده بعد از چند سال عفو خورده و آزاد شده، بعد از آزادی از ذوقش سکته کرده مرده، نمیدونم چرا این خبر هر سال داره تکرار میشه، بس.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83934" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کی فکرشو میکرد یه روزی نتانیاهو، پزشکیان، ترامپ و رضاپهلوی همزمان تو نیویورک باشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83933" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=kEmsPUNYsPvxMrAhJYfw5JZhtk6T4PB12Oik3gO9B-V553Aaw6Sxm_Y3ChgVSM5LO5lJlsKQfNvE8aioSCZDG0irRJiHva9bMqLEi5kJb2o3Z1RCSXrvMTtQp9xHbriXGYvylONTVj0RfOQ3vvVCBPdZwmcO6OEXouW7U7yXWJfwoOvWbKO30BAffWh84gaMD8ekYnty2EQ5WSV9yEr4NS9WCbsgUSuSX6wZuL0WPNSdnHdPf462xY8NqzpH06MyX8fveTypziz6FD0I9oM4nSaAwROmj0ti5iGQko813f0fF1t8ZZd3mX_LrzdxOHb-acZGnpfLs_tXpa1Q-mYDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=kEmsPUNYsPvxMrAhJYfw5JZhtk6T4PB12Oik3gO9B-V553Aaw6Sxm_Y3ChgVSM5LO5lJlsKQfNvE8aioSCZDG0irRJiHva9bMqLEi5kJb2o3Z1RCSXrvMTtQp9xHbriXGYvylONTVj0RfOQ3vvVCBPdZwmcO6OEXouW7U7yXWJfwoOvWbKO30BAffWh84gaMD8ekYnty2EQ5WSV9yEr4NS9WCbsgUSuSX6wZuL0WPNSdnHdPf462xY8NqzpH06MyX8fveTypziz6FD0I9oM4nSaAwROmj0ti5iGQko813f0fF1t8ZZd3mX_LrzdxOHb-acZGnpfLs_tXpa1Q-mYDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برا کی ویدیو میگیری مشتی فنای تو ماماناشون گوشی‌شون رو هفته پیش گرفتن ازشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83932" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83931" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه سوالی که هرچند وقت یبار میاد تو ذهنم اینه که کوتینیو چطوری دلش اومد هفتمی و هشتمی رو بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83929" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d48Yn9k4FnF1q8Okwx2dQ3z5kkRdMer3Dhe5qrbbIDD5P_3dgMNFAbZ4sO99pKJ0FUo-Mn7dS5p2ZhhI78Jm9INUxBVI1rMB6hltsQ2IBDSSrDa71apejASgNewjwu0TKYTm1gPA4BM5dayvJfqay0Aob_b0yHb4P4lcviGTVJ-g7iWTX4UzwoTyFS9anICxQJJNMPXTJBlBFDnxYqWvcstVLBXhbeV4jrKNaKDTiuPTcVJVZoHcuhdil6LCgsbDhFYqCErnwLdXNiw2BrjUEExeSzYwzc5kQAXgJnDQlwELx_o-5EvWXcpHTiQBnNF4OXReR9S7u3vGFUpYguz2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین خاطره ای که از جوونیت یادمه با حسین خاک تو ماشین بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83928" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83927" target="_blank">📅 15:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huGoUI0FlYb7dKiKvqgFjom-YZj-Bkwy7V6ebDTJT2MjPRIipR-mgSg5jWFR1zk-QHZfSqahCFV4uS7svzdokr2JAMn_hu_LEuFrXjnWuYP0uDYCoMvP4LlfOcmAyEw_21_I_Xe9vFp9I6tqlKWEfgRNxi8-7R3RQOE_IzTKZjJULnxesHEYKc-sPMO-M-lJjvMYYNQcaZKg6u1ricPXkSmisHQQQlYEJodnHjWYxq3VqMKXjXnb03kfJENPSCBEGiGhii-fPFnZIMDCuqjwaSKV4usZhtd96jjPOCJ8DH2jPR4CcqxJfwIVdC41tR9GP48OpYwedzjlXZo4NPzCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83926" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شهریور ۱۳۵۹؛ روز آغاز تجاوز عراق به ایران
ساعت ۱۳:۳۰ روز ۳۱ شهریور ۱۳۵۹، عراق با حمله گسترده هوایی و زمینی، تجاوز به خاک ایران را آغاز کرد. ایرانیان در دفاع از سرزمین خود ایستادند تا ایران به دست ارتش متجاوز عراق نیفتد؛ جنگی که پس از نزدیک به هشت سال، با برقراری آتش‌بس در ۲۰ اوت ۱۹۸۸ / ۲۹ مرداد ۱۳۶۷ متوقف شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83925" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بکیرم
ماکه پول نداریم سفر داخلیشم با هواپیما بریم
🤣</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83924" target="_blank">📅 13:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از فردا محاصره هوایی هم شروع میشه و هیچ هواپیمایی از ایران حق خروج از کشور و هیچ هواپیمایی حق ورود به ایران رو نداره
احتمالا بعد عملی شدن این بزودی محاصره زمینی هم شروع میشه و کلا زندانی میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83923" target="_blank">📅 13:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83921" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسعود رفت نیویورک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83920" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی تو تا الان همچین استعدادی داشتی اون کصشرارو میخوندی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83919" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83918" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کوروش وانتونز گفت که می‌خواد یه سایت بزنه که توش رپرای مطرح رپفارسی (مثل سروش هیچکس) به صورت ناشناس رای بدن که کی برنده بیف بود تا امثال پوریا پوتک با بات خریدن و جو سازی نتونن خودشون رو برنده بیف جا بزنن.
همچنین در ویس دیگری در ادامه اعلام کرد که زنش او را به خاطر فحاشی‌ها و توهین‌های زشتش در بیف اخیرش با پوریا پوتک سرزنش کرده و به همین دلیل او اکنون یک انسان باادب است که از توهین‌های ناموسی و زشت خود به شدت پشیمان و به طور جِدّ در صدد تکرار نکردن آنهاست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83915" target="_blank">📅 01:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب برگردید بخیر گذشت
صرفا رادارا یه تهدید نشون دادن برا همین جنگنده ها پرواز کردن، بعد فهمیدن خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83913" target="_blank">📅 00:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من به شخصه اروپا رو به خویشتن داری و کاهش تنش ها دعوت میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83911" target="_blank">📅 00:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/83909" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/83907" target="_blank">📅 00:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نخست وزیر عراق اعلام کرد همه گروه‌های مسلح عراق سه ماه فرصت دارن که خلع سلاح بشن و اسلحه هاشون رو به دولت تحویل بدن و اگه ندن باهاشون برخورد میشه و مجرم شناخته میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83904" target="_blank">📅 00:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNyTEtbJJ1yfdP7y_4D5PhE6MUUtfAvM8lqN5Nszlu_SidFjU9tWiXhp2nHtd0HjJpZoegjuP7VR-dIVon74Xy4tJvEfAZf5GmIIbC1dOQew6B6SeqKV7OI9JDx3z10nmcF6mXKIsXwDf8AKmY8hV3hAfysfk52jsidDG8UG4Y68ovq4iC1GplNoq588OocQ6sLHv57VmpXplYSsTRIEmEt8y4Jj5y8ouybWjqEB56TuQFVrSYMuv_I4z2YlLmr1PvEGXAewxzmgJ0WIGCPnUGZ-ePSeLf2fbKlmWTGQ39022VZbMzkc_Whor4WkUjzaJe8GYJoVBM8pF344M7JBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح حرفه ای بودن نیرو ها رو میتونید از کلت توی جا خشابی تشخیص بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83903" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCXbS5tmLp5Uw9jxTYuluDBoF2e2N-gTOvEh9xBuzFXXm3gEm-Ugb77iUtzyFQgwcMfVnEkuOgK3JMZweQUrq0MT3vDblIb0DZVv8PQaPhUSWjRjlc5LpUJp2cgS7pjB1Y3kbBE8p6gA8UZ8xhtTpE85uquWUhQRn8i2CJ0-NyxtKGCFDFr1x9lMWD1aDyKK0jVZX5XqV3MIc5A-Uq_7OwF07GmxnN4Uac6PZzfu-TrrHlQN2k-_Rh5_UaZFmU4VcLAp215qvsswo2K-5IF1dyg3m7ScQBGe8k_WIhwSv_87GpADamV63CRDRWDOpCqunQWVEDCv8uPVzdy5_MVVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نمیتونم به جیک پاول فحش بدم اونوقت بسنت چنلمونو تحریم میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83902" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tmbe0fD3bTc2idG3zga4R9nfaJibcSr0OezVQSxDWMtJbZuuRTaPsQWtW2bYVjpDoE5Ba93sB4xTIs3-Ldi_6Ajgp5-2CvTopvuvFBUhdiTMmtiQokgOfS5FCvhJWRNhoidHs4eHk1WlC3qou52c5qK0-QIUU6EybqPsMyvPGbYLeVPJUicnGfPX8bm2vJ_qAtw1qHPaSrDLL9TE4SouslfvgHEBBL5LhxgmQihUvSuvtxShmxlJswRYCTisFcqfERNeNqgdFQ9i6y25B1AN76zHN3Lx-3oe3Owp-eOJ99Rf7nf8qgqTd_Z0U667TWdWlEf4vcnn5tJEBd2kFxdGURD77hdOm6m09Fig0rVvbVRR2dLLidOybqZUCsFgHO6XEXVedDGFJTW_krNwAlbm-tu64im326Vj40yUszFqvmU_l79vfxDiXpMAbcdHL0_vKwdippnX5Ct7TD51Tq5acnQBZCyZADq6sHI4AeT5UZT159sjJbreA46709kXi1YyBBbt9Qy6oOglxFmYwdHzmCFlQHTzcJKbdNOrfMBfgipZLMyq0DROi6oweUTicC7mcO0JirHM_VCHzUhPKFZBgkjbGoGkxoRembaTmw0xxtQOt3Po6fyUzI3_Y8W1aLyamAolOxKl0cZmXK2dfiZ5oaPKZqPxKwQjyXtX3DvugTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tmbe0fD3bTc2idG3zga4R9nfaJibcSr0OezVQSxDWMtJbZuuRTaPsQWtW2bYVjpDoE5Ba93sB4xTIs3-Ldi_6Ajgp5-2CvTopvuvFBUhdiTMmtiQokgOfS5FCvhJWRNhoidHs4eHk1WlC3qou52c5qK0-QIUU6EybqPsMyvPGbYLeVPJUicnGfPX8bm2vJ_qAtw1qHPaSrDLL9TE4SouslfvgHEBBL5LhxgmQihUvSuvtxShmxlJswRYCTisFcqfERNeNqgdFQ9i6y25B1AN76zHN3Lx-3oe3Owp-eOJ99Rf7nf8qgqTd_Z0U667TWdWlEf4vcnn5tJEBd2kFxdGURD77hdOm6m09Fig0rVvbVRR2dLLidOybqZUCsFgHO6XEXVedDGFJTW_krNwAlbm-tu64im326Vj40yUszFqvmU_l79vfxDiXpMAbcdHL0_vKwdippnX5Ct7TD51Tq5acnQBZCyZADq6sHI4AeT5UZT159sjJbreA46709kXi1YyBBbt9Qy6oOglxFmYwdHzmCFlQHTzcJKbdNOrfMBfgipZLMyq0DROi6oweUTicC7mcO0JirHM_VCHzUhPKFZBgkjbGoGkxoRembaTmw0xxtQOt3Po6fyUzI3_Y8W1aLyamAolOxKl0cZmXK2dfiZ5oaPKZqPxKwQjyXtX3DvugTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار رو به جلو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83901" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKUX3mDD5qNXn0_r2F8K5B_WQPUfnjkTgAFHvezfibVIX2xZJhl-tUZR5Z1o2x2CA0C-sTDffr2rSnD8uqhwsQQNfhpGv_rYj3lyjgKd_AJ_F9cHho7bwGjB3RCsnHRppSaneWTvd-SJYnCJbuIbu86r6MI5OsIez0Wgwkmy5pC5E-6BuOZ06dI9tw4mg3N6_eS8CqFh_T1QYwGOVccq--q0gMyWtXZjLwFNWY2sfcFqcH38o-y0ji9gb3i3Po0rUS3QpbTTaUAYRF58X97GGtbMn5ah-eMFJZ3TwBsz1Q2i-pAyP58B3Pd9jzzTNr68LW6Fb6QPHsWCHyj_gBt1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی چیه این؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83900" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: کسایی که میگفتن "۱۲ سال دیگه بخاطر گرمایش جهانی میمیریم" الان میگن "هوش قراره مارو به کشتن بده"، در کل به این کصشرا گوش نکنید، هوش مصنوعی خیلی ام چیز خوبیه و قرار نیست بشریت رو به گا بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83899" target="_blank">📅 21:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83898" target="_blank">📅 19:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=W5xEaaxnubViXAHm5UBgZoWerH3mRZAec_LHRd3e5Pb8RuQq45kWUAY9v3N-o-mRpq0zOGqj5BAnbldp4yiWZGx6CqmqACyI9bml4-gvOn0f-oZoperCvjVq2km3me017uU1RN0XRe5rsf_8iFNDsa9hGoTnGlKz4CV5Nd9j3BCGpi8jwo1XU6RUgdLPw3_U43INrVtmKommkTYIscFwAEWTFThyE4Rj4lcKBKap-NF5u_I8oCQkmsDHRgayvRdb3_2QzE-jidj2GM0rkaIYUAFmWpOrH1Wr_JV4TyXaczvsS3jCk-gZaLljWwjXK0aBb2J4bzPCEqMYTzgMhvTaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=W5xEaaxnubViXAHm5UBgZoWerH3mRZAec_LHRd3e5Pb8RuQq45kWUAY9v3N-o-mRpq0zOGqj5BAnbldp4yiWZGx6CqmqACyI9bml4-gvOn0f-oZoperCvjVq2km3me017uU1RN0XRe5rsf_8iFNDsa9hGoTnGlKz4CV5Nd9j3BCGpi8jwo1XU6RUgdLPw3_U43INrVtmKommkTYIscFwAEWTFThyE4Rj4lcKBKap-NF5u_I8oCQkmsDHRgayvRdb3_2QzE-jidj2GM0rkaIYUAFmWpOrH1Wr_JV4TyXaczvsS3jCk-gZaLljWwjXK0aBb2J4bzPCEqMYTzgMhvTaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حس میکنم بعد قطع شدن ویدیو کامران و هومن به شاهین نجفی پیشنهاد تریسام دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83897" target="_blank">📅 19:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=AV1uuZ0tF3w3dSSZkHjHB5FHpNmpEmWinw37HX0-A_yF3Gt9GK-C6x20xHnbYTn5CK3us4rjuZ7Pe07DdVMc4tUIADd-hO5qk6bXf76rKhihD2GWW39mI5ON3COb3K1B2Y2v1pT0h2xfvDFdgjjABV-5WaHKcs4AnkfLbs3_6TK-xba2_COjDUy2X2lTpAe4OcZQRW0m-1ZjylEAUUNbU8UqEf7HIo3yLG390cTxQhuF9NTPtctutimJWgJgfkH4j7HAnkJqCsVDz_lBi8AcFhhIQ4xNZJ2CzriqAxd6jv7NhtLYI6wfwhMcp2S4FcLQiatLsu1RaKMES_V9iPNLNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=AV1uuZ0tF3w3dSSZkHjHB5FHpNmpEmWinw37HX0-A_yF3Gt9GK-C6x20xHnbYTn5CK3us4rjuZ7Pe07DdVMc4tUIADd-hO5qk6bXf76rKhihD2GWW39mI5ON3COb3K1B2Y2v1pT0h2xfvDFdgjjABV-5WaHKcs4AnkfLbs3_6TK-xba2_COjDUy2X2lTpAe4OcZQRW0m-1ZjylEAUUNbU8UqEf7HIo3yLG390cTxQhuF9NTPtctutimJWgJgfkH4j7HAnkJqCsVDz_lBi8AcFhhIQ4xNZJ2CzriqAxd6jv7NhtLYI6wfwhMcp2S4FcLQiatLsu1RaKMES_V9iPNLNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بین دخترای دبستانی:
میدونید من اسمم رئیس جمهوره؟!
دخترا: ببببلهههه
مسعود: میدونید پدرم کارمند بوده؟!
دخترا: ببببلهههه
مسعود: آفرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83896" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکبار امتحان کافیست
👆
👾
🙂‍↔️</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83895" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2TEyY8eG0ugF33xVq1o3dmFqx2Lwb1fk8sPq1ZKVWxRQmDKM4ewd6WIn-R0guSsqQ9CMDvNvy3TL4MQavSkgeWAqNp0ZNUEWaqi5Qze9DHxbCbJJ7j-dnTU8Bcr18fw2bZiyDnJQV21pTXkD2WVrPnhVTesH5OWajXZu13gx4utiSmf_iaGfzYDV3dJwXKZENJ3WvG9QJU0MqewQGB3GnHfRDW9wDd1qDEVaBGLfIW7IXwu997t3jBXhzycX2htgxZ9atFkIV9c0R5SV43xzvx-W0k4aEdObI8av8lw85jHfTAgwd18zvH0wpfoWgeMeI1Z1X95BEMqfjlBR7jYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83893" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFqnG-GoQjNX02VRamRbkeaa-CdHVCIU6lFiTaYXyf9ip1N97HRKBDzxycO3ajBrzsGEKr2-UfaovllB5w6hgSs1dNC1cGNl1coxziuB-q0mgS-R_TizFdn0GMpyTITIGLdwmVt1H76TxnZ591yvflUI6WBb_Qb-Xbkzesb4U7n6R4HQ_VeCdJq-UocYB_nYL8KXxe5O5LmmoV7XMmUygG3UvEneEzrkVQHfJUHqtYJNrBRDJfTvMZ7xf8ynPHxtSckKlkpRcCL8Wq63t95uWWjAsuSEhSJA14_cOivDByWHEKTsTHuI3382EKeqCx5ksAudUKVhd_M3t1oRFuiW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=nD4kocpWOKM1QxepNR5JR5NEm-05X20HaiEusNuTMSPGdQi3kvd8Dbnwa4f0rg2xLGw2-WmvcN3531K3Lw5D1KyE0py-UjhXqpiyciw_QD9U4X8u8XsrEs5mRxBXVxxzYZ7QubYjcY9gAhtWB1G6aLFYaF2WDiDCIb9qA79QIXvDerKkaZLAdQnxnTsjm2AT8aVou3-TS2_t7iOoYLiFpnHIx2FzsEbiQGGeMVrZ8AYyTqvABW68uWfQE45E6OEPqXcGSukGdSkpRuMeb7W0as4LspJJshFDOUBDAIoeNZriyVoTxPqzChcDLWsNDC8IWNas1ztX_xaC4dAc0rVwaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=nD4kocpWOKM1QxepNR5JR5NEm-05X20HaiEusNuTMSPGdQi3kvd8Dbnwa4f0rg2xLGw2-WmvcN3531K3Lw5D1KyE0py-UjhXqpiyciw_QD9U4X8u8XsrEs5mRxBXVxxzYZ7QubYjcY9gAhtWB1G6aLFYaF2WDiDCIb9qA79QIXvDerKkaZLAdQnxnTsjm2AT8aVou3-TS2_t7iOoYLiFpnHIx2FzsEbiQGGeMVrZ8AYyTqvABW68uWfQE45E6OEPqXcGSukGdSkpRuMeb7W0as4LspJJshFDOUBDAIoeNZriyVoTxPqzChcDLWsNDC8IWNas1ztX_xaC4dAc0rVwaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشکان کاگان یه ویدیو از حضور ابوطالب و رپ کردنش تو استودیوی کاگان منتشر کرده که به شدت طبیعی به نظر می‌رسه ولی خود ابوطالب اصرار داره که هوش مصنوعیه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83891" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع داخلی میگن مجتبی خامنه‌ای اجازه دیدار پزشکیان با دونالد ترامپ رو صادر نکرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83890" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHALAi9HVqr-RBuusMiZcv8voQs2xAefWacfgGRjj2RKWUkDZ07xYHpb0R_Q8UfQFnNqzO4H4gGiCAkGrcjp8w5k95srIRlPOo-5TXcIEjHWjLtVHXI2XlhzzyTeXJ9YgXIAwI3zI3v3p_IxcIHY3vhRjRZVxHWaD0RgC4r_9KylqddRk8uFG76F7EoZ118Y8b7IE66xp2s_KZ33625sq9RF999VLCBlLVM1_jRsPqF2hI_f5Eb_u8e7oi4CAbQmJwTgdkqobSsvYF1dGDTmNTcQISIvOMl4miKWQP7O1SeMxGOWpQQzXay715mORhLxA8TK4FKox4lrIlsMGwwGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کپشن دیگه‌ای این زیر بنویسم میان منو می‌برن پس سلام
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83889" target="_blank">📅 17:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2zJ0v25R7IVVA-PScSOzxmfXRmICoMrAUGkTwHcxiLJn_nujnu1Bc7mLXG-zb0OOO-gA-4qRqoa7LDAnptGvPpz9awKpqsknB_dwPzFG_s9xq3WkCkhHYBaM9YhfMtHaF5eCm1mnTTZ6rAl8bgNXz3JLnWjYh-jNrcOLBdFJVcHzfPNYveEpidPUxnsfwSwdNDtNt55FzAYCbB-_zg5kUXxP58ozf--u02VdXYiDYT4mnQWGCE6yKLST4si11aKPsms07F_QeqvMKSoXhfQWG2jXUaNl4kfFmmaMmRDKCp53yXpNI04xLLtIcFBU67NDV8xC3GIGIVnjiV0ivaMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بازیکن فلیک بود میرفت نیمکت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83888" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU-xmwkon3X0_6QiHhyosshJlY-rLCHtSjOYxeD292CLa81wnfOhyOaUujU-0CwpY8dCD5PJseew_m46BKiclY_2Fcax9romflDFK_vNi8BbI2REGwlw398af_bvZq-8MiEE3XQZehN-6pCRptqTN5hR2wXTnl87PkZuiE4AM_cszSK40ogKK2bsmroEBFzALUHWcmuoTYBP7TKaRApYNHz7_IUXSCAz_HWycWnCTn6EGIoYKGdR8j85vUkIUCLMJM9fPrHxNZmLfxW4M0HrDNKbYa-X6ykaD_yP5GlzBAytsfBx-4eBzix0Ks2AOhhpgndn07dwqz0BrdPDLtqVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83887" target="_blank">📅 16:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=hMYYZMqQG0UyRLjbYangMuecLvFZoP-yG-CV3Yd7AgfRC_nlC-y-f9DGDTJWyonR4BBrUQvjnOgeM1PooSf_JJIRom7162tn7lDyDxisLXeu--BTm5pp_gIYGtvcHyDoWYbxua1vhZw4c0zSpXl0M3KtbjkqXCYvTeNpgsYAPYnYymfaR62CFH34Q01VmfOLkxgy2Gfi8LFpHZifbkSgXyeKXhV2HzYEF7cxLwI_7G-HsYU4JQ-S-oHa4-hqugoBonlrbJvXGz7zq9dplRcbBxucRvD5pWBTdvr0gCqaGKvUP-At2QlRVpjevWLw1k7hGgEEh6GMTA1FPYgEBypSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=hMYYZMqQG0UyRLjbYangMuecLvFZoP-yG-CV3Yd7AgfRC_nlC-y-f9DGDTJWyonR4BBrUQvjnOgeM1PooSf_JJIRom7162tn7lDyDxisLXeu--BTm5pp_gIYGtvcHyDoWYbxua1vhZw4c0zSpXl0M3KtbjkqXCYvTeNpgsYAPYnYymfaR62CFH34Q01VmfOLkxgy2Gfi8LFpHZifbkSgXyeKXhV2HzYEF7cxLwI_7G-HsYU4JQ-S-oHa4-hqugoBonlrbJvXGz7zq9dplRcbBxucRvD5pWBTdvr0gCqaGKvUP-At2QlRVpjevWLw1k7hGgEEh6GMTA1FPYgEBypSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی سطح طنز مرجع تقلید هامون»»»»»»»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83886" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آقا کامران یک نسل چهار</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83885" target="_blank">📅 15:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آقا شما بد جلویید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83884" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcCbbvkd9KeqjN_Xu2u3PxophtWor04zqxCGShEWQfP2tWOW3X6RH58AObU-sISMZfBSDLQbeD-6FNYbxEcYajSJ-Qed5e_pl6wKViMRLHca14-KfQ8NC1uYnm502dp8qPvvLMsP4Y-jkCFC5iPJbHUwQ4q7G2l0p3LB5toOYAqvzAmTvveC-lDPYRuE5cCi9PcEV8QoyvgJJnFmKfWNbJ5-CgcrgPzC06mHIi7ReAcEyxuCS-BRnk6EeT2cBqF6pZ_Kvaf9ruXM6IdrYVNXQbjE2dN0qcXdAdSRX2FJtl0hpwJwuyVr-B6pxp72krUG3dilpKIFaNqWfgWQO1tz6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا شما بد جلویید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83883" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یا یه رفیق دیگش سرطان افتاده بود تو خیابونا تهران میگفت چرسی پیدات کنم زنتو میگام</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83882" target="_blank">📅 14:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83881" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83880" target="_blank">📅 14:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیرانوند گفته چون تتو دارم مشکل اعصاب روان دارم، پس معافم کنید از سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83879" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خیلی وقت پیش ی پیشگو گفته بود ی یوفو میاد و نیمار رو از زمین بازی میبره، احتمالا همونان فقط تو ترافیک گیر کرده بودن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83878" target="_blank">📅 13:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INXB2DWK9mD3HbtcAaFpaYm5URfe7mktWcorFz7nIGJjLCjZhRcgBFulghlWAms-RjGVXy0NgNEKuaTAJ3I5j9caszVq_In1N6lZMPiTojA-MS_zpl6QDUV_b2a4ib2I9IxjXGIS4tNIJpIO46yUFt84TPeS5fX7A1EIhi7APhI9XZcHM6cvvHV-lowSf6V7kZxaKcXQIztrmUzGe2FmdWYRHqrS9pK7wtLrxk4sp1xrKDd3l7XWfGwoSnjUCAgoMGIuz4srx7pzchaxKcNA7xgjtzSAzsuj-dX7v_idOtAyzFDsnQ7AbqhQHaIqOdGqZE4UqrB8hHBqsez9zxRmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادرا یوفو رو هم گردن گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/83877" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=gguvA0fmsXVT6INNecSLJrXJbcMO64-GazzTcm3X2pVXnpt_xpW_RlaowbZEhm_0R0dcnQuwcrgG8yjz12JLK1uuicAqqn-xawPuynQf46wWR43BtB40AFpVbkhKYirtNLdngUtE-5MAhHl5c-NgHBmq6NHnowJBp_Lg5_9emG8rkCu1JdCSWAuxbMm584Fwq1RIWnRPHac7lwl1msBU_E8kvPggWC72puBpwn92gOy54ROvWs52uR0k68_QwvRFCO9tVZ40gRSLJMQ7P-HxJRbovIAsQjcV0s2aiC3E4jC9j3Y7jtMzuYU0wPxq3OgWGVtj1o80qnHiCifMStWELQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=gguvA0fmsXVT6INNecSLJrXJbcMO64-GazzTcm3X2pVXnpt_xpW_RlaowbZEhm_0R0dcnQuwcrgG8yjz12JLK1uuicAqqn-xawPuynQf46wWR43BtB40AFpVbkhKYirtNLdngUtE-5MAhHl5c-NgHBmq6NHnowJBp_Lg5_9emG8rkCu1JdCSWAuxbMm584Fwq1RIWnRPHac7lwl1msBU_E8kvPggWC72puBpwn92gOy54ROvWs52uR0k68_QwvRFCO9tVZ40gRSLJMQ7P-HxJRbovIAsQjcV0s2aiC3E4jC9j3Y7jtMzuYU0wPxq3OgWGVtj1o80qnHiCifMStWELQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83876" target="_blank">📅 12:14 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
