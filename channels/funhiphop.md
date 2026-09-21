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
<img src="https://cdn4.telesco.pe/file/ewYgmAiQoAO5tSPyrplbGDmnZHEGcTR4rkQuFLk2VoUXlgE6QR2eX9XHvfYnmc9Oe-dlUeH8dSpOqG2zXTwe-I_RMP8XuhVmfvYlKuqBTNIO3giwjWBHl7Epon21MHTARkjQoJEqsH7Fc5xpkzIWfdunvrej0dlO_TAY06DWr1G0XTxb3deXuq7vXv-XWUsifIXP4F24QwnkzSp5-Avk78DQAYxIz0WUSOaLLAHpLWQxe1lwwt75Qo3xBK_rYEm38qO18yOouMkHBTkCjs6rYg-nAI2CEToyZkicc88DJEsGmG_FZuKFNznpPnmpem-reFkUzvTo_hYJdrZZY_GsFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inIc8quU1eFkPoMhbzBabHH4hVhhpSu3OQueTLSbuNdhZywPLPi9bvS2asRItfO9Qfl6LCOhIp87FHJK2v7eJfREqBubjBbRCJRxILh3XlkUO0I1bG3UaseoQX4jHLBcHM4P0KowwkBSOmlIJmlzRqm_7bP-gTicUWUii6PP1Dbz4ESjoXAM9IPGtJ9q_ZSlhHYoq9mUEq4NGvI1y_XVs7BukXsoQGBUYkcoQiJFP8G8J5NXfyTgz5yj9Cq4cl4y2JfUOBq9Oq3oIdcuMuQurwBjtukNPlAClijS9b9VSZHFVLUQ-BKsoXYMZ2HjDI3OrZPxDhJt9ATL01iLf0w1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا شما بد جلویید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/funhiphop/83883" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یا یه رفیق دیگش سرطان افتاده بود تو خیابونا تهران میگفت چرسی پیدات کنم زنتو میگام</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/83882" target="_blank">📅 14:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/83881" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/83880" target="_blank">📅 14:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیرانوند گفته چون تتو دارم مشکل اعصاب روان دارم، پس معافم کنید از سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/83879" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خیلی وقت پیش ی پیشگو گفته بود ی یوفو میاد و نیمار رو از زمین بازی میبره، احتمالا همونان فقط تو ترافیک گیر کرده بودن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83878" target="_blank">📅 13:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtW1MDQvlV66iqkQJP40YZ43VRhUjnbR2zG-dUi7SOVK2x_VMyTFknMMD4tToD93wGuCUEQSBNiMoU_tgSG5Ghmti0Efu9c-2zHK26qh-079KinyczbQkksN5IWr-otEQObN-kujejvMuw-hdT1W0j6dbJhzhT35srmdaCBKcjkQpHKphd6cKgHNZmnN1QSo4Ge33hwLrKkloAVVD9dxGlc_nuXTP08-g3u4-HEJgEWLkpMonhFWhEd12EZ_EH5tUZMK1wSa9w90E9jHTu7uui_GrZPTjdFj5RnYLnjhpeh3q5_MIb1PQFOWSB92n16CWQThlEeWCRs00ZyQFhZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادرا یوفو رو هم گردن گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83877" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=eCnO0hYgdPZ1I-7pnpo3qmpg6GUk35hTfD5QyD4VF8QcOQgfsKp3BWA-0Ptsw_3NWxlatGmTPUt8zLmLDKnUIZjXOImMsqcpNNSv9kUq3RZ9vU9tR1TAPetbwP_vvTh1GIngHwLP9AHkEgMSFVv_knXfy4OC2ymF4wlWwTtxWwWpO8Ui08RYQ6ZXtvBu7KLIYMYFj0G77NyyEa3jMqIHvXzhDJq5MR0pX2tZOWfniYmF_4BBL59slgxjn5sV6OB7lbgNefwvm_lXb3o2SA6ooqwt8mi_5zSHTDRHhvc9_g0K8sxXDykmzShrhpaG6wyryZpGmIjIdWAfxbL2KbyqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=eCnO0hYgdPZ1I-7pnpo3qmpg6GUk35hTfD5QyD4VF8QcOQgfsKp3BWA-0Ptsw_3NWxlatGmTPUt8zLmLDKnUIZjXOImMsqcpNNSv9kUq3RZ9vU9tR1TAPetbwP_vvTh1GIngHwLP9AHkEgMSFVv_knXfy4OC2ymF4wlWwTtxWwWpO8Ui08RYQ6ZXtvBu7KLIYMYFj0G77NyyEa3jMqIHvXzhDJq5MR0pX2tZOWfniYmF_4BBL59slgxjn5sV6OB7lbgNefwvm_lXb3o2SA6ooqwt8mi_5zSHTDRHhvc9_g0K8sxXDykmzShrhpaG6wyryZpGmIjIdWAfxbL2KbyqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83876" target="_blank">📅 12:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhH6HVhJWmMgCVE3r60KyRYq8-sb4ONSPSWJOGEylncZyYrRfcsCE2IMYy40_Z9Brwly2LKNByWlWDmVRmqptCyncqKm3cF1RZ69EeNMRwwzreCFX30uYcEOX7AZibsH52iLvMbDdNK-P77eTWzZlo9vSaT11mfV4EppFqLGwuIdgSBfE8NMwtyUEHeOxM4jkOmaZGosVbA7rtqCU9t5G8a-eftp1tc6IsQhKrAYop12C4mTkm5TGAOHTgnCo49KMTkFjuH5poI_Y3bj1Ecl5SKSXbPSRwxl4pbMo9KzMLn13Bg62kFDdO-dQ5kqv3hb3j4Xhw3usbZa2DN5JnRTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجوری حساب نیست اگه میخوای علاقتو بهش نشون بدی یه کار دیگه ازش لیک کن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83875" target="_blank">📅 11:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iO42olTK1ghmWEufAKdJ5G9B9dfJhj7Fk1YxLG8zh76Lidq9W2-GWblc9m8bkw8sm_1CPv-J6IhuQm0mUpAqKzPLNOME6r7xGmJKiXneHcNSWW3l3unB6d3M9oB3KqmwYjGL-tJFHuT4zEH2oaxYMHogmUuo74NCLWZKgtW9S_YJCtAGqCif5XkBXntd_I13L1Yh3aQj0Y7r1ozs3kZZL43pKYtK1wNQ3PXJYkIM_jESaOLMsY32sD8BtCWaAUP7LzWam7D-TG3onT9RQC_IE2d11VP0aUe9bxkgtewkm8MwHTmSbELmWhosx9Dugb8jGYogWVltmemmnEM5is1KcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iO42olTK1ghmWEufAKdJ5G9B9dfJhj7Fk1YxLG8zh76Lidq9W2-GWblc9m8bkw8sm_1CPv-J6IhuQm0mUpAqKzPLNOME6r7xGmJKiXneHcNSWW3l3unB6d3M9oB3KqmwYjGL-tJFHuT4zEH2oaxYMHogmUuo74NCLWZKgtW9S_YJCtAGqCif5XkBXntd_I13L1Yh3aQj0Y7r1ozs3kZZL43pKYtK1wNQ3PXJYkIM_jESaOLMsY32sD8BtCWaAUP7LzWam7D-TG3onT9RQC_IE2d11VP0aUe9bxkgtewkm8MwHTmSbELmWhosx9Dugb8jGYogWVltmemmnEM5is1KcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83874" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83873" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9b9R8YT84vZmuAftZUpPejTQj1nNSobYITrZgDWhg7j_dFIxgsa5SjPBUuoS0A2MyAPkxPyTF398xD4OzD9NmNyqNqZIyx76cnL8RyKiL0OvO0Co9flN9jL-bKetkxuE64NfExs6z-qbC8HagEplj7-unvo8VzJF5V_NaLsXpjeKHDqV8UTbZ_l7WXyjGnS_v-Aododpa_J4XNqU-dn291VGEqStnbFvT87J3dff_-kjGoO2kpzOnDGnts0YhP_7fmH19RmYFi1YAptWLLGPMPdZQPVbjGtMpFtCDRbQDmcmVFKC9vJSV0VNjdKgDktS3lvBV_cgfVQDHqpJLgItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - جمهوری چک
⏰
ساعت ۱۷:۳۰
🌎
📲
اسلوونی - صربستان
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
R30
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83872" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgNhSrLnI4zzQm6kJjwLA7rc_ErUj3bzFONxe4TdF2DMkm5L6FM42PXEhatJQt_Br4Od-4kayyDxmL_eI1cvoWbDny6cn0nOUdtuZVJvlPDNqXWpoHpLOp49fktX2S92isvlDXqRJSnNCzE8Dfirp3CA19gnmP9V4Gx6zr5pofjD_zsg7syT8ENyQkUt0SJV3vQvSdvQvVGmBnvLNhqt0BXiVNOlWc183SSoZ7POJVpbmlGCti5usfrF-I7e8FiyIh76BF0QhLnbpWTMmKHFniFETLxUNa7nRPATagrywDvoI6Htv8ZXKilRbjlPbhttzUxz1d14umwsXV-8_cJFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممم عجب شب عجیبیه، دیده شده در آسمان تبریز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83871" target="_blank">📅 02:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og98ENghO_iXKX0zox6pEKhZxnD6n1S3hRQDG8m_7EwdeElzFS1KZ6PVe2WV3cqsvQeG_vA_nt9lkTJScJOLzdddTzxLNed2arRljzNPcaT6hnkDOTwhjiHBAjDnyn4cM1fbVkGbmAG95ODjj5qKwTiDUYdbXErUF8qmJ4ZvEVMR8eC-lW-JPh87feQBz4HJgumYQs6kwI6gqGvrRy2c283SQGZxcDdrYovp16Dfdfz_PaIFCKFjPtc0MzJZRSkFKxaq32Mdm2_QvsvryZB26vuz2mYKGkspcG73dBIancTZIG8oXa-mz44Q4uGYF8DJjGVyTbSP0WZAVIAX5E841w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83870" target="_blank">📅 02:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83869" target="_blank">📅 01:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83867" target="_blank">📅 01:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83866" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاید یادتون نیاد ولی خیلی سال پیش ی بنده خدایی با فوتوشاپ ی ویدیو درست کرده بود که از آسمون بادمجون میبارید و تا مدت ها مردم فکر میکردن واقعا تهران بارون بادمجون اومده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83865" target="_blank">📅 01:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83864" target="_blank">📅 01:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد  @FuunHipHop | FaRib‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83863" target="_blank">📅 01:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد
@FuunHipHop
| FaRib‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83862" target="_blank">📅 01:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شبیری زنجانی مرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83861" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4-w9j0lFj55aukUbt4a4TF8OpbN-quBlWWFbxWuKJSxG5M4BzLLF8LHVnNzbC6suDcKeK-1JRUNOU3Itt8HarwpY1Frccj2HIb4fEmFH__NA8KOYJfMk7D1x7UsbJOeIWNApkni4c1NifaxoRKoZChsUbwSIQiMx6R2c5NSMfe8QN7sGDcHAodRMmH6AtO66vyYYnCZ9ZgCGrgLTNZ4Gg2anIlNOZdThXtlHfOeJXjEgL9wMh6pZo6CL1WnDBVWfDFkiP7sVBMAZdHfhu_Slr8DAypI3kjzLOO9OuGflMXEIElxg4TQ0_YyBBMk1nLujjbjPNL1mOfrSKMdmKcXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبیری زنجانی مرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83860" target="_blank">📅 01:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU8CVOqexpy_j4h81wu3A-qCB4-cuHk0oQA1262uvgWkjZJ8sXY5FlHNGvT-1RfK6lPWkQ83ARAgheXFvF6jPuMvZ2oiNFVYG4jmUhHDhpYHt3qr4bwkPAne4p3xijq8LK28WO9uS1UTXgA63OFsNkmo8XmBb_C4SAeok_fkPZfFmiDd09-q3AFxJLxz4hgSYNd9d36Zd-evSd8BxPa-mdqIdNwR6xYMH09A_WCIMNYPdtmLlg_9bn-deKUrmncjNuV_Zm7fKFp6IQ8WdTLsrhRFTgsnOBClK-Mof86am5covXw9gZxyefUgGLn6l5a6gZFqTZEo7wRfY9zh0Q6-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozCw7v2BJx4kFfzSWdHTWxjXsXTZRpA7-puvZkQ9Kjff1XPe92wCUju9XTaLnEeY-7Qdxz_5aTsanz6U9t6xhWiSMiyT7YVvCOUQfLKV98M13xT319w19O8d8DFowYTQ4ZeCeqr7NgaVhz_RX1BDVUEqbBJK6M_neZHJA0aapRU2hmXlMyp5dIc2hcOxy473d6wi-RsqWs1LdeZx1sXeFnnLtPfAxjgQnh01YCJX9EZO4OLGT1magUgh39rzS1y8D-pbVYAC3OMIeFRqq9uWmtVpLcJt2dr5wwWVkzJIGgieXNf-IKRLI9mWNGIhRb_tiQrQ583ancnYaqVhEoFFLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چقدر زود پروژه حکومت لو رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83858" target="_blank">📅 00:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4G2D_P1l43hCGHQCEV_fukn9uY9RSB9X0luCT_DnzFmoqKgX73trJCJI2y2cb3tx-pVad__OB0URltCucFiiMiqiBBBdv_dCNdZCh2Pg42iF8jc2nao7edF1CzGZ_llDcdM5tBSNyEIZ2twIxlvai9HaXz3VE2BPJjw7eQoIhSQfySWPw4ZbzfXJ89AQxVqJavZYxz-20p2bGFNdV8lVdVhbPzwHQ9Zc5Lkcwjn_jk_Wzqtt6jRoMHJVkhX6Q6mutaHXakmL0_4VAXTBE3n0hHDHFlwYQQ583ZJBGX1CqzTErH7P51We7D4ANJBxyhbGvweyJyQiqffi8Bi5D1BeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان امیر تتلو را آزاد کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83857" target="_blank">📅 00:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همون منبع
کیری
به طرز چشمگیری موثقم گفته که صدا پدافند میاد و جنگنده های جمهوری اسلامی دارن بر فراز تهران گشت میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83856" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">طبق منبعی
کیری
به طرز چشمگیری موثق بزودی جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83855" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsnZNHSUf4OC6UgbN-8kifSgaKOrnW3O_ZA7CcR5iy_mP6jykklcGbEK8QesFnrPI52Vv9OIp9bDuKmG0MvUnCZiohBGSYQKccoFTAPKZoH9l_09J25ZlomQWGTI_hswQAy-9CeOWW6AmMHQBceJ-Uxj9I4HTfnBLMI_daQ7b9B3R6f-AOSTGoCcUJ8E_La9Tzg1jKWIGbKERkOVoaQf6WPzRVTpLLbNYJEdqRJ6x3gA9cSITCo4K90WfhGEAmcS4_BvAZaxkhBgUbwoYu31kr71kv5w3H31TZx8lYUPQjrVHMTmUZle0q-KLYcK9nr8I8c0-HABH2QBlmGpPasGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که براشون سوال شده امیرمحمد بزرگ شه چه شکلی میشه داداششو ببینن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83854" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به امباپه اعتماد کنید، الان میزنه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83853" target="_blank">📅 19:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بمب خندست این مورینیو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83852" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این کورتوا چرا نمیمیره</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83850" target="_blank">📅 19:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رئال باز پیشرفت کرده پارسال همین موقعا ۵ تا خوردن از اتلتیکو، ولی امسال فقط ۲ تا خوردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83849" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یاسر آسانی > وینیسیوس
عارف اغاسی > هویسن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83848" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سر رئالو بریدن</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83846" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بابا دربیارید شماره 4 رئالو از تن این بچه کونی
حداقل خطا میکنی مردونه خطا کن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83845" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوتا کارت قرمز مستقیم داور تا الان نداد به بازیکنا اتلتیکو</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83844" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamL_tp8AIgXmf93bWUgwrOj5kJVIpq-u_OLF8oI3AZRnUKA0pyo1570hn1Oh6rtFBLYLdbLtJJAa8Xq8M8PBV0QKDVojjqoyKBcARrq7TXkNikPn9N-eiFKhRx67vYxNSzoiJSMR3V0i5K2O91sYtLklYzoJHJ6JRw4Aa1ejplS01pfELNSvP1DRSQdKYj7bmuYksnwiZcJwpLiVLQsW3hC20fVW-aD01LI-PWvu-Nruvy_7FrUg6LHVWC8gfOiN76lf5B7ech_GCwDBBbWHQWvJUyT1Oxj9Rv78P_ILbHiA16IQmBaLkBtTk6TS1a6XERdW_MCpg36tn_SX5IGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید با دایرکت دادن دونیتش کنید میخواد پول دکیو جور کنه پس بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83843" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMIrjkzVL5nlfzZAxc6THv4HM2soAnfo29QE_kgnXrwukDBY557KWYoOkWhtJnJlF4fCPyCi8ITIWlepzp1ErbKco8b7U-l2-O-N2Fibx3eDiHxYda76FqiDPCroowsZKOpgtDNQ1K0MW9Sxuu7eQ7g6w2QNHVBpcT1Yny2XEIHntceIyZ6KQRC3Q-f8bScg457_C6Iokjb2MMiwgEe6oh0YbPEKiVauKE2cnDXFTX8EEX-rQ8NPNk7g-8qIqKH9Gc2dlP99ii6uYgE1RCj2jAuyzd2Bml63Chk9f2Krqkty9aQ1QKd5zH0IRNrzicYHPADBEiEtV7gxp_dwB_o9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت دربی مادرید الماس مادرید رو ببینیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83842" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9TkT7evL5U4nctq2ptU9ncO6oR9A4Dc5OIVjQxScyf1B5K76DjRBwKsiIkTQGVMC7cxpu66UdFZG4jzokJZo9-2Eo_aXHi55YCzEjL-CzllWrjl2e072KqfkOvZ4plsBERoiHoTzvD71Y7Hj3nlUVxtC4VrHDzslqKtgP6sRoDoZ3Kj4JnIjL66qtooqEgfldb3xhnQfBLRJV1X_FcQCFw9sla9Qmn7hAoD35-BGVN4Tk1nsnAUuiKswgigigMOnGLJ7uubcSHJdh6NJoIrbOaU5gqNtw8__hyLjRgrn1G3pvdbQEjeNLQlHb9M2M8zKKy8i1oWNPX8H8JXBMpH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g29
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83841" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83837" target="_blank">📅 16:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جنگ کنسله
صداسیما اعلام کرده حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83836" target="_blank">📅 16:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83835" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83834" target="_blank">📅 15:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امشب یا یمن کونش پارس یا ما، همه شواهد نشون از عملیات آمریکا تو خاورمیانه میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83833" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قرارگاه خاتم: آمریکا میخواد با چراغ سبز کشورهای حاشیه خلیج فارس بهمون حمله کنه، بزنید همرو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83832" target="_blank">📅 14:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83831" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=hgMpQbPPFsUCodQM2M4tJJwBDRBEHDPqsW9JsObl8NDidYYjHmEwniNTxad07hrbTLSJKbYJfjS9ayC_cBMENFwzpI17EZ4llXu-sL9B3DAGeCNWoHpyPJtVqWAHyRK1FMOpr6asIQdVikPF5VozolKWrsgP2jYEubfuY8AMoOJJIb4AAEEXZ8Z_1MYM_3R0cbkv_zaSRb4lDdn7feswyF1ICMsH4fYg5qOgQTJqoGOLCV4V1LOY1K9ubIomB6fjyG4YgfZ_3ZhEFCJ1eOUvNVmkV2xJfHkRWiTrWIirwyLHUZfSLvM0UsLnKaMaSHWTqOi7AxtHdHW0eczGVctd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=hgMpQbPPFsUCodQM2M4tJJwBDRBEHDPqsW9JsObl8NDidYYjHmEwniNTxad07hrbTLSJKbYJfjS9ayC_cBMENFwzpI17EZ4llXu-sL9B3DAGeCNWoHpyPJtVqWAHyRK1FMOpr6asIQdVikPF5VozolKWrsgP2jYEubfuY8AMoOJJIb4AAEEXZ8Z_1MYM_3R0cbkv_zaSRb4lDdn7feswyF1ICMsH4fYg5qOgQTJqoGOLCV4V1LOY1K9ubIomB6fjyG4YgfZ_3ZhEFCJ1eOUvNVmkV2xJfHkRWiTrWIirwyLHUZfSLvM0UsLnKaMaSHWTqOi7AxtHdHW0eczGVctd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83830" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=McLYefi97al8oyrGZ45wBpr3igYHxS68JSwtJD3aaSuRMDhzRMQZcixEfn5JEXHlB5JNbT4-6g6ez4lwVlDeQdnndqeNpwQ1h1F9rU-yhDYsQwFwIamsneV8s6PqOG6deu5O4tZSYZXYD4fJK6xPiWe8foFlIR51ppWPmJhf4YaY_bvCuXt5m2rE9R7KbYa-mUA0Kstrn-xItsX9SzKOHo_p7zJnnIp1aA_CK5-uyyaTjYD77lAmJnjf2HfZvHB6g9tWg0g9L9ghPkpbYusDVLQ8EFLzwejjKTgrgpk1NfdWnqdNHWUPnWN58bU0AnkZIp8vN0RyN102xhTb719OLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=McLYefi97al8oyrGZ45wBpr3igYHxS68JSwtJD3aaSuRMDhzRMQZcixEfn5JEXHlB5JNbT4-6g6ez4lwVlDeQdnndqeNpwQ1h1F9rU-yhDYsQwFwIamsneV8s6PqOG6deu5O4tZSYZXYD4fJK6xPiWe8foFlIR51ppWPmJhf4YaY_bvCuXt5m2rE9R7KbYa-mUA0Kstrn-xItsX9SzKOHo_p7zJnnIp1aA_CK5-uyyaTjYD77lAmJnjf2HfZvHB6g9tWg0g9L9ghPkpbYusDVLQ8EFLzwejjKTgrgpk1NfdWnqdNHWUPnWN58bU0AnkZIp8vN0RyN102xhTb719OLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83829" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=mp-6sJxahY5iriCJfQ5PaVuyOfe8PAIQcr-3mC4gKUD21odsDdXxVZNWG9W1clh-9PIFXOXeKNsFVR9mCj3D79Ns4BoT61R-mPSyZEXKTa70W1dM1bTvi0I6Mn9GE6ATe7qjn_8hfKuduXEbhbrfIBBLk5j3OTtVz0gzhJj951RNEU_Fh-OolV2Gh35ov_T5DASayox8T4BBsq44v1lFGGDE3WUvG_qay1cIRMGNomGNYbgE8aFS0l5NLxeZiDjDvt3yoyxHGYpQNueltsW1ADZRfJjLIysCLzPXa1BYgAr0rjkBLMBb1P2aE0Wns23OGhsm-iVKSswaxgL2c1kjow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=mp-6sJxahY5iriCJfQ5PaVuyOfe8PAIQcr-3mC4gKUD21odsDdXxVZNWG9W1clh-9PIFXOXeKNsFVR9mCj3D79Ns4BoT61R-mPSyZEXKTa70W1dM1bTvi0I6Mn9GE6ATe7qjn_8hfKuduXEbhbrfIBBLk5j3OTtVz0gzhJj951RNEU_Fh-OolV2Gh35ov_T5DASayox8T4BBsq44v1lFGGDE3WUvG_qay1cIRMGNomGNYbgE8aFS0l5NLxeZiDjDvt3yoyxHGYpQNueltsW1ADZRfJjLIysCLzPXa1BYgAr0rjkBLMBb1P2aE0Wns23OGhsm-iVKSswaxgL2c1kjow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طناز بعد جدایی از شاهین افسرده شده و هر روز داره با آهنگای غمگین ویدیو میگیره و گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83827" target="_blank">📅 12:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=f-SQ355lG4S4J_5ZLCb7dS5wvgl_dgoNRSKz3zoYZfrFxKSZeQ-KYTKMYdcO-kCPimT9j_VfLoytnRr_VafKeuotSeUJoWta-N7y7tkEKHETrMGplGPx6jnRqcuMB6YZZfyVLOcWeiBW13A-mjturdpgy0ygqdyGctUbHROSFl9poKGfhRhhdJ8nBctLSJUk_V0w8W_kXQdqk9EaMRjxoExAGn0dGvSpyTBHjVwsSQMEmND6mN9hicMXNv4UbaI6JuthLL4OITkRiUXGcyvoEBcOrmTkK25LRHtf-piyz9ifVoTDhzCgzl0uGPdi8d07zFHY69WO3YYixPKcdRnn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=f-SQ355lG4S4J_5ZLCb7dS5wvgl_dgoNRSKz3zoYZfrFxKSZeQ-KYTKMYdcO-kCPimT9j_VfLoytnRr_VafKeuotSeUJoWta-N7y7tkEKHETrMGplGPx6jnRqcuMB6YZZfyVLOcWeiBW13A-mjturdpgy0ygqdyGctUbHROSFl9poKGfhRhhdJ8nBctLSJUk_V0w8W_kXQdqk9EaMRjxoExAGn0dGvSpyTBHjVwsSQMEmND6mN9hicMXNv4UbaI6JuthLL4OITkRiUXGcyvoEBcOrmTkK25LRHtf-piyz9ifVoTDhzCgzl0uGPdi8d07zFHY69WO3YYixPKcdRnn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83826" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWUYFK7qzMWfsqfDP07A2NBJDpX4TkVwVZXIswB950XfqJXwlvyhExOt7zwaefIwwS8o5x7acvmLathQDYGhgsCxuehi-82S0M3gdFLkwhGfeNiQJuO4mFHvEIHKVkH56i-629bKDMP7oDr97iIiebnpDIt561h_HlQGmRoVTL6Z1oMO-HmDKZMuE6keq7qwdSmSEP3Fh1CX--pJRjtdnyNitlgXq6d3-07yjzLwPxH0EGTjh3XSxqsKsDwfyN7XtW6FPQvDqgRF3pHgUeZK_uRujJhlElkNUQ7HBlgbsljrcElZhdD2g2Uj7ona_L_Ml1uG8cKDMAgz0yDI9AVOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بورنموث - لیورپول
⏰
ساعت ۱۶:۳۰
🌎
📲
آث میلان - لچه
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
R29
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83825" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83824" target="_blank">📅 11:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83823" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83822" target="_blank">📅 11:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صرافی او ام پی فینکس بالای ۳ ماهه پول مردمو به بهانه های مختلف بلوکه کرده و نمیده، همه مدیراش هم داخل ایرانن، حتما باید فرار کنن که براشون پرونده سازی و پیگیری بشه؟ حالا اگه فعالیت سیاسی داشتن زیر یه هفته بازداشت میشدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83821" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxf9hWCa5z0--hvo4osHyw-QK6HciZkK-jgOpR1Ljy06RFZH7gApA6L9FXGyF1jzTJsmm61J-sLNb0Px0TYgoTxrLenctRyz_aa9WdLblydhR2U5AesrMW4oC_wl4glNELygRjaadxF1bso7l-QGk2F2pDD8SxXMvgLAHEWanf7g1uH6f4K7ExuB_ZIrVIQYTKIAY-6Y6JTfa47MiXjMp_OzVmlr7uvCMd4xs41KYiJkpfF_mqeyD94abza5JsMAWuDpPbqTnSpmuu3is7IX2ukGsoxJ0c_28YtfGET6r1_bH0-WE-HXj9RlPX1ptpwMdbnWUld9p6vTrTHxIm9jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلوت کنید این‌بار واقعا تعویقه
تمام برنامه‌های عمومی‌ای که ترامپ برای امروز داشت (از جمله سخنرانی‌هاش) به صورت ناگهانی و یکجا لغو شدند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83820" target="_blank">📅 05:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlRO0Iloq0GpYklRc3LgaXXByK8wi2Z31neJQLQWhgzTHJqHoiRLmDr9ndom3-vviSvNuqUK94b3AhEDdxE2WJBOIQ3UL3RGZ2Au7wxnWc6aXZfD9E1GUsgh3st33sE2YFX4-luRzMVO61iMxaHBvgLL2TpgUMwPcGBdeMdPZdKpFfW6suEna7BOflWbzbmAGNpdRq_l8uYRTO-K8rIcyoeNvHkWiwrX_5tfQuf_usWbObsLVrGLIYfgiQXiqSDPx16yqR1bUC64CGMcsGhUczM9s1VfbTKvniZpXtenvZLGyaATFdyR4puup9UHccLKAgCxKMBFnwAHAlOnlWb4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/83818" target="_blank">📅 02:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیتزا فروشای اطراف پنتاگون سکته لاپایی زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83817" target="_blank">📅 02:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حاجی میگن ترامپ یهویی برگشت کاخ سفید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83812" target="_blank">📅 02:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83811" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83810" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی.
تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل، فلسطین، اردن، قطر، عمان، کویت، عراق، عربستان و سفارت مجازی آمریکا در ایران به صورت جداگانه و فوری صادر شدن.
یه هشدار کلی هم وزارت خارجه آمریکا برا کل شهروندان خاورمیانه صادر کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83809" target="_blank">📅 01:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKOQnOTcGGWLUB3TJMjbUMdz3TtkNcFuLb0FOim1ntG7yzkG5l70rb-hw5tQ4rqp9jSFVF-eaV_iUOEk26J8eC4PqsDaAWZus4M1wNrhPz-bJOuiwBQqIOsEzSA79hfMdrbj-RdbcBXLo0bklt142I3oesUuHASZh6wvSjXTtcjtri8q5tfHu9-pp8ineCR5EWAUKHknWM5s39sFvWZWy1norAJdKMrUqbtpkL7WS0xYZDbVf_8hN7bKj1oB3dYqQZ2NLkuFlt8OJJfiFQXJXgjkSM26vzH0puXChyBpdI7koORv801csKN-h5gdtZeDPeQxoP4HMfaczxScfFz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر نمیدونید باید بگم سازنده جنگنده A-10، یعنی شرکت فیرچایلد ریپابلیک(FairchilDRepublic) یه زمان لوازم خونگی هم میساخته مثل ماشین ظرفشویی.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83808" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎓
آکادمی فتحی  انتخاب رشته تخصصی کنکور ۱۴۰۵  با ۱۶ سال سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما  مشاوره در ۳ جلسه: ① بررسی رتبه و شناخت علایق ② بررسی رشته‌ها و شرایط قبولی ③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83805" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCHJFCtPxDTk-e_a32CqT_mIViPIg-9nOh2v9gdQjiJvEvtqUvgpovRYfjLaM2F-jpps9ksw7CLVNoyWAtlilDTsMh1IMfHvZB_AfITSbq1hJHcGpF-641xCOxoXq_WnUYthTYRN3_Ina35eMpaYm35dbfqxqSZX_RBo_m77FKaEKkT2e7TnHH1sM627rcbVA94hM1y44YlD9xHfc6JoHyB4pDlRkq5jknKMgvRMFGmkApMAxB9aBc5gy_851RyYD9f4V8GAGPMgkFlvMyyGFxNNnjuOd7W-oy42p9yl5trn-CxvQWMap0ENPf6v0uSzXjtFsVLtjyMFUuQO8Kd3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
آکادمی فتحی
انتخاب رشته تخصصی کنکور ۱۴۰۵
با
۱۶ سال
سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما
مشاوره در ۳ جلسه:
① بررسی رتبه و شناخت علایق
② بررسی رشته‌ها و شرایط قبولی
③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری و آنلاین
«انتخاب رشته آگاهانه، شروع یک مسیر تازه»
https://t.me/+XFqj-oe9FrdmYzBk</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83804" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، یعنی چی کلا ۳ گل با یه نیمه اول سخت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83802" target="_blank">📅 00:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83800" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه زن دومم داشته انگار پوتک که اسمش دُرسا عه و فرار کرده</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83797" target="_blank">📅 00:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83796" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83795" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جواب آرتا به دول سه سانتی گفتن پوتک: لابد آمار غلط داده دخترت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83794" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83793" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کیر تو آرتا داداشم رافینیا چه هتریکی کرد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83792" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83791" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pao74XGGQQ_1LJYtee1lHGt41_DSiz0a-sLXycczSMfHA2rWJPlAxa5QSrgJSVnbFTOVEuzb27x4-hikOlnIH8nIa4V0hUaeWjcZMt6k2aGF35R1a33Ktpm0h20m6tCo2MqAIZFSG_RqSijPR8QPURJ8ba9gaIqIlS3bumEBLw7UpRHzR06Y9XryTsCsIUea2mkuLtRiqujjx73Xy_l_PlC0IJqNQ1FuyDpWIq1EgOsQ3Qut35hx2Ya8NoeN_I9LN0EI7EAHyZ14ydu1nhWjl3hhnHpP2vtZcBVG21hOequKCCAZzl0gkeArEpuzcYq2T9F3hkrzhLWlm7e336l87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83790" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83788">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کسحل رسانه ای به من ربطی نداره ینی چی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83788" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به من ربطی نداره ولی اگه پوتک هرچی گفته دروغه اینهمه فشار برا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83787" target="_blank">📅 23:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83786" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کوروش به معنای واقعی کلمه دیوونه شده
داره به تمام مخاطبایی که رو پستای فحاشی تو چنلش ریکشن پوکر فیس (
😐
) می‌زنن سنگین‌ترین فحش‌ها رو می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83785" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83784">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کوروش وانتونز همراه با این ویس، آیدی یک اکانت تلگرام با نام محمد باقری را در چنلش شیر کرده و مدعی است که این اکانت، اکانت تلگرام پوریا پوتک است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83784" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83783">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPxeCWbaz6hq2Viif2mEauMwKW-3JIS_-JgDckAjxOnoY8SjsK5k_XT1RwgurD2l-kaMjTs77lgd5M6VIWpOC_rWQ9CYmidRBOxsV1oGld-VNpR6kBYXgJkF1ooH7MvdN4SoMtkhg0Ou4qKq2gbApyBzSuN_jF5ThkcxjZvz0DjfKVG1fq5dpAB9Xv-zNLvNTkehGMip3smQ4HMj1_E0NWnjvINZmjn2qmISepzjeiFVNntNFIPmRDYReSb4iY6KY3Y8ujaOIb9I5jZU7QG5oP9y-AqylQwHIpvbQ9D-ue_iOksVSTqnx5X3R4gOw7_mWqJMuClSmmeIG7Sg8bGguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83783" target="_blank">📅 22:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrJ_vZoWYvnRYb_A00SxZ2SYmMjmPB2cxkmIxHICNemVB5psIhSULEIQXXN54ugjJLAU6U7LBke2H0qUA_0AhwV4RmtEKbuB4qXT8LOt-4jrTFnSnftBjYAq3boQWRqbOJiJAydjlX0zx2uj2O9uKjzWkRvVrPE_aOEypztcFmfh2sdAv19K_5hBgqZ0XiHzOr-JVeKMv0Wn9RPJBvMVzOD4ZkJI-QP-hLW1gYlXqH_MOODqD8L9Of2wHcAN-AUxrUcN_51-49Q_g0c9ybXawRuNZBuzPzIJXjJz93And6xOVzg941hC_RFCVOIC1pFyEpb0jk_2Vo9LbvkfiN6qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83782" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب با این پست اعلام کرد که دیگه با فوتبال ۳۶۰ و عادل فردوسی پور کار نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83781" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83780">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUGtWqzI0RdIn7Lz0uWVKByt1pmcxHeRI_6cRSngmBW9gi-p4sxsPG9Wq-4iDVMHY2APsp71sMtT6YxUPKmjp3s9dOgsStpigAAmOz-bjdBEPe40I-FHMAbRBedcz-ZQNJFBmhJIIxbMaTZm2f02CMtymWdTJwbdSrWTwa_QVNMMDhNs189dCbYhJQQZEFMXA6FOh5uyQHQqbtaMQCWXg9QnECmISU-ZaAd83gyV-9UBjmNXOQXeDQpo_hqovx6eZx6Md4iIUYiYXLbsl77pE8bpVGIB239eiL0cYLj9ikXf2yqI5DY6BpLs8aIz-b_BKN5OIpniY9S_mMSFUPiowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرتو گاییدم چرا تموم نمیشی تو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83780" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83778" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کوروش وانتونز با استناد به
یک کامنت
،
دیس‌ترک خود
را پر پانچ‌ترین دیس‌ترک رپ‌فارسی نامید و به فدایی فحاشی رکیک کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83777" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=U2ZBqNPTNONvil0zdeT9XU8klgY6sjeZzrJdTcO2F4Uzl88oDabxxUiv00eH5qLtphu9-CWg_r15ThYOJ7BYOMrnv0l6yUp7Jf6jOnhKILCwAzIakmoXyWbgHW6DmaxiuREP4La1w5FtoUSHkpo_0oqF3J9Z0vKdRSjFxEBKOYwFiDptKAqy9W41CQR4qsImEXavhCFEIW6QXlE1JhQyqYodChrIreXNxDC0x2Yeqaks3K9tz3OLcPiJDxJgWBwnFyH2cwCJbeNJjtxRtoqPBh8qVib2GfPv5KC-ewvKLXbnQNlK0p9_ksuX3cfFUKp_aefPtKGNy8-DGcHkCY1QKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=U2ZBqNPTNONvil0zdeT9XU8klgY6sjeZzrJdTcO2F4Uzl88oDabxxUiv00eH5qLtphu9-CWg_r15ThYOJ7BYOMrnv0l6yUp7Jf6jOnhKILCwAzIakmoXyWbgHW6DmaxiuREP4La1w5FtoUSHkpo_0oqF3J9Z0vKdRSjFxEBKOYwFiDptKAqy9W41CQR4qsImEXavhCFEIW6QXlE1JhQyqYodChrIreXNxDC0x2Yeqaks3K9tz3OLcPiJDxJgWBwnFyH2cwCJbeNJjtxRtoqPBh8qVib2GfPv5KC-ewvKLXbnQNlK0p9_ksuX3cfFUKp_aefPtKGNy8-DGcHkCY1QKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیانو اینجوری تهدید کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83776" target="_blank">📅 20:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سهام شله با کون خورد زمین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83775" target="_blank">📅 18:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83774" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83773" target="_blank">📅 18:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdD8CzANbLw4rSm4ftMuW3g4rdYEd4mz2l_h-dp0sjWWpJoSIRZc_7kohHEJ-5wepm9GE_BoEftq4zAWR6ZB9_tQ_zPqQho2DL1TiwnvK_Bgnp8ESqBSdwHeub1YO2jBpmBAivkX0X46-FaZ3rbFk1r6kB-gvhpmcbvY-F4j5Cl-URwvGwKfRr-O2n7YY9UX73BIY01ScsTlMWrpPwwwHCdrnukeYdpV7Wmvl8vVPvEikHSGuM1Qqfuw8XMgTp2clkmcoHRzXUadGB348V6fFrFiuAhrWzze06nMB7Pn1e7EKb-SaeyosGAtgHQN7cLGququ3VrmjOmjE2_fqxrNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حافظه_تاریخی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83772" target="_blank">📅 17:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83771" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83770" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvHO3WWXc_1uxBI-yoQe016qlb4ZjGCMQTJEnKypBPnZoL5WA2nDM6sGQbNL1KugtQ4ySEWAfSC1lllXFMYSGv1pRhQq2hWFygu5mrwtdTJdtzmVQ1LZKP7eDCUA080a7Ijrs9rVHx1gba2k3Z6rklfILYg_q1VMlvGNp2EXLvfwWRdyU_KJiP69ZUqUWMs_k3GzYbZsB15iQRzCH_EliLW4CXaWiy-S5-99cVt-MhfRS3BBAHXRzl65s1QV9znFHxeMDxuiOilWN_GReF1CYu8UJo-6FhnURyO5WL2Q_Nzqeguwzk81UWs48YVQcWCz3o7HFOYq-jRFq_ubpvJn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83769" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqzsD8kNxlEEXXNdf0D6uSfZf_AWv0FcahKRV0dyucM7VCDrHIdJ8GAaqed8mkflOMYIPJkU7yb7rwXKXR4Cc3NRtVsESnjPjUB8j1yZohXM3qy_uYB9q-8fpei0pu45CMvGpd-zo3YMJZnW-2MW3BljwPx__CZZbeVgs6klb65UJYoMlOIeWmcvAu62b3VCoToTvfYodhtuakSIQ5H7OT04CGhIGbaKXjwP5NCnPg83dY0QUjXuV6Ttz7yiFtPjAw7WJIOoi04J_kCtZraxhShzHnYBQ7nueBdoqmTSSf_j4DAEWvpQ22whP878rKABCAXbtjAljFpcA_COXbaSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83768" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcp-QS4xn5ZELTKPD_QdFDevms0PBvNgRQhOR_lWVf2CEeHVqzZwGYgX1d40Nq0JVtyC66dQxk6-uQi7EDCqoct1l6Vb1zHnjRXI8mOZZJeTjKhC2oLf2VOuX8Iv3w8vU6qd52_gYFb6S8xJu9vOp5X9XUxJIynNBFG1raywiuWcQ5fSPs8K2BJECXWwkwBZGRvIwWxEdkh_5TamVcLgT2VUdelrgyIcw5OP-Z1WTSbnPNZOxO06_tsjLB67hbnK6uB27hNcsszTfPxqBY-iih-o8gjCzypKl930Dy-OKFz1dFRNef7JcI63tkp44e8AVJEuVe-mPnJ3qJiVo_2ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر قذافی که 7 ماه پیش آخرین امید مردم لیبی بود و مردم لیبی خواستار برگشتنش بودن و داشت با رسانه ها اوکی میشد تو سن 53 سالگی ترور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83767" target="_blank">📅 14:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به قول امیر پارسا و ناگهان کص ننه چلسی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83766" target="_blank">📅 14:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خروج رسمی امریکا از شورای حقوق بشر سازمان ملل.
آمریکا اعلام کرد عضویت و مشارکت خود در شورای حقوق بشر سازمان ملل را پایان داده است. وزارت خارجه این کشور شورای حقوق بشر را به ترویج ادبیات ضد آمریکایی و مماشات با رژیم های متهم به سرکوب مردم متهم کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83765" target="_blank">📅 13:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7CINoD6b1Ft8wEQIInEEUNPqkRB7r-EEItvbG3xuC9FybJ-m5G5cFPjBjCHAwRpeGtFsrd6-j4ZagXzBllCd-IqbV-h8uRkAf21bhm2VOyMuRasy7qYaCZ_8uevQbb7D3FMJxrxXNHzu8_ANr-MOu7xsvHzcrj4ju0bvG0fpSHv7liFnxuogjrnCzqVj6IsbQUpaPtSnjXAtYMBUz0Kkq4U_FG6STXKgqOS30smgNSPE1KPqr944NZVXSxOYaDeNmckQS7CA8hQbMo8iJFomfx9x7Ujj29r7l2ORgD_6OMkoQNfsyrZ3wcNW3jNcZOqKGx0FhudhAv_SaLTbsr4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسدالله مادرت گاییدس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83764" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=K3KtyZJGUnEwv8p0u0Mppi2FUtWKnLFQgKs91jowNvP97PXtf0k6NYA5slKPq5echAsIpznebW4b2Tq-DkmfGjK5TVNv7FeFpnBGRs82xFzLC9SQe4iucWfMdT700H2kCPDCsVT5_ZduB0laF31h_y5z3a7lxrwvQ8kYJLwCKzWn4VnM-G3R7BkwYcEJTTgseyVMcNFmqGJngvchhRIlxtnr2lkzUTtcPLNH6yvev178Hy8lvT7nGIRzw8Zgelq_nMllvjekDWbRE67lw6ScL87XnpxASZO_SAhkah6hUCNy9N91fVLHwSFRv-L7PJ9xiEv7Cd3jXlY1s8xqU7cEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=K3KtyZJGUnEwv8p0u0Mppi2FUtWKnLFQgKs91jowNvP97PXtf0k6NYA5slKPq5echAsIpznebW4b2Tq-DkmfGjK5TVNv7FeFpnBGRs82xFzLC9SQe4iucWfMdT700H2kCPDCsVT5_ZduB0laF31h_y5z3a7lxrwvQ8kYJLwCKzWn4VnM-G3R7BkwYcEJTTgseyVMcNFmqGJngvchhRIlxtnr2lkzUTtcPLNH6yvev178Hy8lvT7nGIRzw8Zgelq_nMllvjekDWbRE67lw6ScL87XnpxASZO_SAhkah6hUCNy9N91fVLHwSFRv-L7PJ9xiEv7Cd3jXlY1s8xqU7cEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مصدومیت خوان گارسیا فلیک داره رافینیا رو تو پست گلر تست می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83763" target="_blank">📅 11:59 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
