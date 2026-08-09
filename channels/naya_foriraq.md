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
<img src="https://cdn4.telesco.pe/file/WtcnwkSwxcv5bdJD5VRIdI9gRzmU3xDkEt-JJ6N4Pxyuvk9DaV0XMMrrhu1zVJ3Sdj47flMag6ibPLcsT-bInNYhKgGSGB3dmxremFcy8AWMRUgpcSIxVp2G03UG8BzvvpAy7K4PHVAxwlgJZzQ5dkujw5vpI9hsVuzCPwgTRk7R6tmDQg9kGjz2BmWJ5DjDGAjcaqaA2NOrbRQVVjlVZyVFfIhOqPRqnOf1_QMFI7VGTvP9sQ82A9wOi1FvEDLRrM40kqnKVxqmDqiea8X1fExQE_R5PzIKN0vgfwi067ZIdUh35nmETyUfHkNN8UCbt3LUOs1FBzgquvzED5LY5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 17:11:32</div>
<hr>

<div class="tg-post" id="msg-87383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/naya_foriraq/87383" target="_blank">📅 16:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/87382" target="_blank">📅 16:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طائرة امريكية كانت متجهة الى قاعدة إيلسون الجوية في الولايات المتحدة تعلن حالة الطوارئ لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/87381" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgYi7eiiHiQt4v8CObwLNaZpNQp53pUreroSMwtbHXu7yHXwkwJn1aHmLuwcNtOtxnmKJ_fCbri53YFx9FVPwaV4QsjtKUaky-p71-rVywaiDI77xIBAsjXJCNdkPzOaxRRV6mrLFdL8kXOS9TbCr4zDrA4uHS9Rups1WjJ29tFLv5noTMfLihh5-g8IXjjdEXkzhBp7oOPNbW9SUBrFUlXG_4cKZF_HR2P57-Rgil1PeCM-G0572FndRLgp9vOmIe00QRPe42zRs2ZkqFC3WW9EYJHO9n4OrlGJtcSBtPtEnmqZAI2O_amGGisjCjO0sMvjY_d9-NyMcoZvsIYo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد وصفها شهداء الحشد بـ"القتلى" وقتلى مرتزقة السعودية في اليمن بـ"الشهداء"
النائب احمد شهيد:
تقدمنا بكتاب رسمي إلى هيئة الإعلام والاتصالات بإيقاف قناة خنجر العْدر قناة الفلوجة الطائفية</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/87380" target="_blank">📅 16:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">القوات المسلحة اليمنية تطلق صاروخًا باليستيًا على منزل حاكم الحديدة المدعوم من السعودية وانباء اولية عن نجاته</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87379" target="_blank">📅 15:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/87378" target="_blank">📅 15:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87377" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=JfCn0SPRi_YKpN4UI2zfUkVvtzph24J66zRSjA78DdPcHBH87IDFp2eUTwu7zDkokZoQ19gVuae4iftS4lQH7tnHxvffk9x8ApY3-tjCxm3Bc3rIs3vSe7HDdu2cJgtSrOpfix1VuhPsuMy3Ydcn6YBkyTEIZCOSad-rQAiwATXppi56_duCRn5Tvv9cb1NNm1rxU2aGtQw87BVMMCc3s7HPOjoylnaee93nz4CCpdPeUsxudpkRSkJ1_jiiex78LG021UDQDnVKKQ_cDC76lFizfWc-UB7ecFYPx4q_XT6BbOLT5KweLpIIdsGd6GQC22R_LkINuolCeQAHEt39Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=JfCn0SPRi_YKpN4UI2zfUkVvtzph24J66zRSjA78DdPcHBH87IDFp2eUTwu7zDkokZoQ19gVuae4iftS4lQH7tnHxvffk9x8ApY3-tjCxm3Bc3rIs3vSe7HDdu2cJgtSrOpfix1VuhPsuMy3Ydcn6YBkyTEIZCOSad-rQAiwATXppi56_duCRn5Tvv9cb1NNm1rxU2aGtQw87BVMMCc3s7HPOjoylnaee93nz4CCpdPeUsxudpkRSkJ1_jiiex78LG021UDQDnVKKQ_cDC76lFizfWc-UB7ecFYPx4q_XT6BbOLT5KweLpIIdsGd6GQC22R_LkINuolCeQAHEt39Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصرع 7 اشخاص و35 جريح من المرتزقة في ضربات أنصار الله على المخا كحصيلة اولية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/87376" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87375" target="_blank">📅 15:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcKOhwLmyaPyXHEqpl1r_UDMZVxffkk-nw1h59lWKKI8x0oEuZdFXJGOjVUHCHgixyOFthYBYUBT0hXED_smvPdAT3t1Zj9_PLR26vFAyngY3DZS5Gh8bsiQxVAOSM6bhxIofwuaNIlpJfA_X_VF3i5jFbbz3fmhjzYk7D_tHNfEWkdJR5esyEvZ8i7PJHQvKAxRSlV4N2SirOqxxBatzlrcqf9u4fArlHYWqgb0k2t8EYv2gmBpiMMNCM1ffqta-UNxqZGlidFJYVCTcJnGV83haxrDPOPO_aySK5bPynATIlsTbAfo-2ST3GBuT8wngVkDh0OIj7O4ZyNMjgC0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/87374" target="_blank">📅 14:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3801856749.mp4?token=r_N02k5ZBVTMWyFsPF5GyegX5XClbSkHPGlodf_Ne35xCRAxGTt4kgtwY9IKJJq5Hkxjl2_c7Oe7dbi8UkZQ2i-rAKTBj7vKubXdnNI7vKHMuZTqeGwjfy-yP5WHusfMI5eyB0RYDUSLAa4Nm3HFrtdenCcNa7ipuRj-ObVgTDTdfHSQinxQvx9sD4X1aUQBtJyJc_XslI1JpK4OZk3HWdCi7sMN8N7Uy_3ErDsgaH_e8dII8KriikJ01kZq37vcdpUO2L9fDUET-7CH5apVEL8265xaVZ1Il9tlM8E4Rhy--dCpgoF-yRyHOXLmnFGdgHrIsKkyIxSojs3jcBeJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3801856749.mp4?token=r_N02k5ZBVTMWyFsPF5GyegX5XClbSkHPGlodf_Ne35xCRAxGTt4kgtwY9IKJJq5Hkxjl2_c7Oe7dbi8UkZQ2i-rAKTBj7vKubXdnNI7vKHMuZTqeGwjfy-yP5WHusfMI5eyB0RYDUSLAa4Nm3HFrtdenCcNa7ipuRj-ObVgTDTdfHSQinxQvx9sD4X1aUQBtJyJc_XslI1JpK4OZk3HWdCi7sMN8N7Uy_3ErDsgaH_e8dII8KriikJ01kZq37vcdpUO2L9fDUET-7CH5apVEL8265xaVZ1Il9tlM8E4Rhy--dCpgoF-yRyHOXLmnFGdgHrIsKkyIxSojs3jcBeJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/87373" target="_blank">📅 14:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY2t-jWsjf866jkxaic-d5SIIQ7YJ2112vmCHmlhDIMAew9SrDRo2hqXVYjluP07FLssqPUBT5PRiHmety4eEesE1BeBN3urYOFmXyfiaw8PJbdW5zNfDC8pdBB5DJrFkUp1Jp43UC1tzBTFFgGRQXwukR9_emDn805HdTAVYveM3QQiWy1H5X-yr-k3BgNYXet0qQsJ0ZlETL8R8Gx8KSL4Vk_znYbx4E-B6cSjKjHYvbxB4ZZx37VSH-Vn84DjIuDvwG51kTBzOej_TFCYcrNZ6nN_AAGGj3K7EadL4dbXRWB76F2xLGC2Ig5GQGcCmsLEiW20YgVcERG1YKz8l_Io" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY2t-jWsjf866jkxaic-d5SIIQ7YJ2112vmCHmlhDIMAew9SrDRo2hqXVYjluP07FLssqPUBT5PRiHmety4eEesE1BeBN3urYOFmXyfiaw8PJbdW5zNfDC8pdBB5DJrFkUp1Jp43UC1tzBTFFgGRQXwukR9_emDn805HdTAVYveM3QQiWy1H5X-yr-k3BgNYXet0qQsJ0ZlETL8R8Gx8KSL4Vk_znYbx4E-B6cSjKjHYvbxB4ZZx37VSH-Vn84DjIuDvwG51kTBzOej_TFCYcrNZ6nN_AAGGj3K7EadL4dbXRWB76F2xLGC2Ig5GQGcCmsLEiW20YgVcERG1YKz8l_Io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/87372" target="_blank">📅 14:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBRK6-10JU8QrMwoIlzfmzEiZVl79P6PdXjzfwE27ff48XGsOrz1oyweMy6fBISa3NwxLIk44ItlhpmHSP9g4P8e6UHATOo1oJiEacNGDkqzPhIGXVzarmUg-MSKBAdKZRyJVlPamuRzGg_Pr_3A0yNL6XKdfZ0BnB_-9-QE5frbHt6OV7tw18oj_SVVgLuAzytqz8widYU8Y0YUmlDSAPdklfQsJes6QFbW-NhSwWezLTdJHnvDWXk32GuN9Kh2wa7P0HrmEbgfEpmmqxNWrNlRtBV4UTCz4xtqpp22LnDcfpufKIT8nAcXgYJJDJJncc1y7DwcOtYt_e1beWnuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القضاء العراقي يطلب من البرلمان رفع الحصانة عن النائب ناظم الأسدي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/87371" target="_blank">📅 14:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/87370" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/87369" target="_blank">📅 14:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87368" target="_blank">📅 14:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87367" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
وكالة تسنيم:
تكليف محسن رضائي ممثلاً للقيادة العليا للثورة في المجلس الأعلى للأمن القومي الايراني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87366" target="_blank">📅 13:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6yhgM3c6oOe0R1fDq_ww2x2kr_IiYLH-7ZCHCu4hUjbYhBvVfn006JKDdeCshOsxheo4WKS89DLWKHR3KCl5OGK7Fyc3Wc7bK6o9Oj7kK3gOw3Q4XGXPYAe1apS6IFwRK3jQCz06eRXrZuosnSI9ZH5LQmXO_6za-4JGo38QBW0ni3wrxmBrlcocl2Y9Y0T6XJBgZ2uZeCeUJwqX8QWIvvKZuLPhdB4kT9xLOEiz4qPfkNNKpkuXMlhl5SopSAusx5Dt_fJ2XnPNTOtcfSf6wFmEVrpmOUMGklx1dXUIbwwsNUA0c-8e4tn2oRQfMZ6Y3Cf9Rf2-7_04UdjrhufZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني لنايا
‏في إطار التغييرات الجارية على مستوى صناعة القرار الأمني والاستراتيجي في إيران، تمّ تعيين اللواء محسن رضائي ممثلاً لقائد الثورة الإسلامية في المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87365" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🔻
بيان صادر عن هيئة الحشد الشعبي
:
تستنكر هيئة الحشد الشعبي، بأشد العبارات، ما صدر عن بعض السياسيين من اتهامات باطلة طالت رئيس الهيئة السيد فالح الفياض، والادعاء بامتلاكه معلومات مسبقة عن استهداف مقرات الحشد الشعبي وعدم إبلاغ القطعات العسكرية، وهي ادعاءات عارية عن الصحة ولا تستند إلى أي دليل أو حقيقة.
وتوضح الهيئة أنها، منذ بدء الأحداث في المنطقة قبل أشهر ولغاية اليوم، وضعت جميع قواتها في حالة إنذار، كما جرى، قبل يومين من الاعتداء، إبلاغ جميع القطعات بضرورة أخذ أقصى درجات الحيطة والحذر، وهو ما أسهم في حقن الكثير من الدماء وتقليل حجم الخسائر.
وفي المقابل، لم يتخذ الفوج الرابع في اللواء 30 جميع الإجراءات الوقائية المتبعة، ما أدى إلى استشهاد العدد الأكبر من منتسبيه خلال الهجمات. وقد وجّهت رئاسة الهيئة بفتح تحقيق مع المسؤولين هناك للوقوف على ملابسات هذا التقصير وتحديد المسؤوليات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87364" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87363" target="_blank">📅 13:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ   بسمِ اللهِ الرحمنِ الرحيم   قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم  رداً على استمرار العدو السعودي في التحشيد لأدواته وتعزيزها بالأسلحة والمعدات واعتداءاته المستمرة في الساحل…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87362" target="_blank">📅 13:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O41mO--63bhyHsKDUaZbxTs7urGizA4zojjtP8k8t9c4EN9h0CgjBeKUHTwmet-0j4ygz4p16_lLuyC0xQ-XP9XQcaCsLoVtn0mkin2BAhEQE8PuYXXqb68aH8Kl7w-lqmkJTqeMa2By-7TRS3jSd45zeWLhJUbQPRAPvR-esUKDKm3YRqvK27_ZIktIPP9kOvjvvLQD3MlJD4ojsCLpd9yTwV8yQ2G47188KOLrQoUWRdbh5OQzMUSgiolaoYT-xQPaHG0mzvmHlKZ3mWq4GxsKVyEgXNBGUArDpuqqmdte6VinmeXXe14Vj14_piIH5GUpKaCdwAJWwJrNopmqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل الطائرة اصيبت بهجوم يمني؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87361" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيم
قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم
رداً على استمرار العدو السعودي في التحشيد لأدواته وتعزيزها بالأسلحة والمعدات واعتداءاته المستمرة في الساحل الغربي ومحافظة تعز وذلك لثني شعبنا العزيز عن تحركه المشروع لمواجهة الحصار الظالم والعدوان الغاشم المستمر عليه منذ اثني عشر عاماً
نفذت القوات المسلحة بعون الله تعالى عملية عسكرية واسعة ونوعية استهدفت تحشيدات  العدو السعودي ومخازن أسلحته في منطقة المخا وقد كانت الإصابة دقيقة بفضل الله وأدت إلى تدمير واسع في تلك المعدات والأسلحة ومصرع وإصابة العشرات بينهم سعوديون وذلك بعدد كبير من الصواريخ الباليستية والطائرات المسيرة.
لن نسمح للعدو السعودي بتحقيق أهدافه المتمثلة في استهداف شعبنا والزج بأبنائه إلى محارق الموت خدمة لأجندته التآمرية لصالح أعداء الأمة وستستمر القوات المسلحة بعون الله تعالى وبالتوكل عليه في رصد وتتبع كافة التحركات والتحشيدات السعودية واستهدافها بشكل دقيق ومباشر، وسيمضي شعبنا اليمني وقواته المسلحة وفقا للمعادلة المعلنة "الحصار بالحصار والتصعيد بالتصعيد،  واستهداف أي تحشيدات تستهدف الشعب اليمني والمحافظات الحرة"
والله حسبنا ونعم الوكيل، نعم المولى ونعم النصير.​
عاش اليمن حرا عزيزا مستقلا،
والنصر لليمن ولكل أحرار الأمة.​
صنعاء، 26 صفر 1448هـ
الموافق 9 أغسطس 2026م.​
صادر عن القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87360" target="_blank">📅 13:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCNWRSiU6C0KrjuMKHnlUnOQOMx09RLUEXlufw2XVgwb0IpbOl9ZIjaqxvWpdegsTcnVxzhCy8VLopvldXAfrxdbMrjSxz8YHNpAAL628qoqVHHBa-BOgoWQUQrC9-tVVbIMN3RVsXykilorz5ZOGcKl7UKj34WYOMDVXa0ajYlCerr4cBgtbPVpBhYK-A2tulDm7eYmLNwVlEEWu6mHwOpY_fLYZkyQC9udjUUMinotNwmLXupbw5UGqckuPUB1TjrPYHGdoQzbaLjiZE1CWvZrJZn6rTpbRoodmHfkkp60nsP0nPCvU2L3DorQyFxmWmT4tjU9bDcoOFlbTNHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل الطائرة اصيبت بهجوم يمني؟</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/87359" target="_blank">📅 13:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">السفارة الامريكية في جيبوتي: طائرة امريكية في حالة طوارئ باجواء جيبوتي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87358" target="_blank">📅 13:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87357" target="_blank">📅 13:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87356" target="_blank">📅 13:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d94b1eab85.mp4?token=Wk3f_K3fc6iR5VnyPPi45gf2xzxIULWE6FgiCCm7Vwdq85t3K4y0etnDpj1CUL1JCInOKqGMTxrMT5APkDbHNYsC-K5NhyczmxWok0ATmBw0PCXt7qcoPK9NFxlDrVEp9ii6-Du-4BqwDfo6pxIpNml2X27lbBRb6CyVOhsZuaw2Ona-h0a8pHIn5QFkO4XfwJosDiyqyEInvJYx3BxdkDhPcXx-AOtCxr9ExhdQVzT8oVWSpPjqXUvgxj7DNa1jJ1rVpJNCUS7ww1laxDEPdOQyMswi_RB6ZQUq3esgAzmK74vZGv-YRvWoWK4P_3MSuE9PWfjCyHBOC7O1InMctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d94b1eab85.mp4?token=Wk3f_K3fc6iR5VnyPPi45gf2xzxIULWE6FgiCCm7Vwdq85t3K4y0etnDpj1CUL1JCInOKqGMTxrMT5APkDbHNYsC-K5NhyczmxWok0ATmBw0PCXt7qcoPK9NFxlDrVEp9ii6-Du-4BqwDfo6pxIpNml2X27lbBRb6CyVOhsZuaw2Ona-h0a8pHIn5QFkO4XfwJosDiyqyEInvJYx3BxdkDhPcXx-AOtCxr9ExhdQVzT8oVWSpPjqXUvgxj7DNa1jJ1rVpJNCUS7ww1laxDEPdOQyMswi_RB6ZQUq3esgAzmK74vZGv-YRvWoWK4P_3MSuE9PWfjCyHBOC7O1InMctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من ميناء المخا الاستراتيجي على البحر الأحمر بعد استهدافه من قبل انصار الله</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87355" target="_blank">📅 12:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87353">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات جديدة تهز ميناء المخا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87353" target="_blank">📅 12:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87352">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏بيان مهم للقوات المسلحة اليمنية بعد قليل.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87352" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">أنصار الله يستهدفون إمدادات عسكرية فور وصولها إلى مرتزقة السعودية في ميناء المخا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87351" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKrxowmHRtiUawQbM828GWzYw0RHlNPnziU0HSF6IHdg5-vna8IwC3EroePFFsb7uJ12MUsXQnsR3m4o5NNDXpArpxvp3l-Z4RxZygWI1rKAgKjLUYGTrAXfiFnYavGcYkj3zkRRJkwX7aCZKfOvu761glgz6HRGFPNYgfi9g8BhMzJbiiU_6msgBjiHBgdPLTaGLUbWFtR0uFizpCn83GQSZYlzOf6DI4vm_T_HWXq_CTnlGJ6YsrvtztSWgD8UVbJTEGacfuOWj4Iu9ZmJP6TUqoAJEyMTiS7iI7RrWv-_2TgMBZ2CUbGvb3YO_Y8Bno_bzPqrhaRJZMVxaTHaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار دوي الانفجارات من ميناء المخا عقب دكه بالصواريخ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87350" target="_blank">📅 12:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20a240712.mp4?token=TTqNmrec5SYYxU1T8WqPNTDVzhKC9RRATDNV-BC1dOPmixCEI8bEO3Kpdy5Le2zzZsF8S9OppxWUJcpO-Z8LoSZoW0Lxl8PpMHtoz_bvq_QjXH1onraheYaNfH4DS5f6EwhWim4CrRZuIFevIg3CoIXwRWcFpXvTfYK1BL1uldZGErSuROww438X-WyrQX9jxUU94XCL2VdW6CjzlPqgqZm0r3g3ZFGa7mfGY-s-KbTB-HFgHiTNWQ_GqDWT5tcvbqRQX-Fl7L9VQ4NFl1hGNhaa8e9zw0gm_7KCfliHIXW3TGyskB4UlQ90shHqq3XZu0C5NO7yE6mv2QKd6V8zpi1kKUtCtycAiz0OdjW7uicqF0Uj_LV50CzLPlhDPzTBnCL30qh_QPw9u-6yQ6HM_Rg4P9Wekzd5tf_zkUgXyHEpXLQo0tpnZmWe3HHN_2PUmwYEym99ARGbmpuDQ1WheBFPWY75xWb0q1glxsjCUAkPoqSVn1sDbv_U-r2JQXX1kIOpsiixKWYFdFV15rtTfLi9CALynsvkwsUXR-ixnYv6NPimeUyLfEsveH7vYjP3ldx3AefNEn2VWO2i-9Zq_Zqc1EqBBT_WQRHIrMkl1PLOAny2G59di95uTj6AMqNN5nJhk4DYluZOOzczpn9wjDTdDO1k_NzFNVqZkpOFOUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20a240712.mp4?token=TTqNmrec5SYYxU1T8WqPNTDVzhKC9RRATDNV-BC1dOPmixCEI8bEO3Kpdy5Le2zzZsF8S9OppxWUJcpO-Z8LoSZoW0Lxl8PpMHtoz_bvq_QjXH1onraheYaNfH4DS5f6EwhWim4CrRZuIFevIg3CoIXwRWcFpXvTfYK1BL1uldZGErSuROww438X-WyrQX9jxUU94XCL2VdW6CjzlPqgqZm0r3g3ZFGa7mfGY-s-KbTB-HFgHiTNWQ_GqDWT5tcvbqRQX-Fl7L9VQ4NFl1hGNhaa8e9zw0gm_7KCfliHIXW3TGyskB4UlQ90shHqq3XZu0C5NO7yE6mv2QKd6V8zpi1kKUtCtycAiz0OdjW7uicqF0Uj_LV50CzLPlhDPzTBnCL30qh_QPw9u-6yQ6HM_Rg4P9Wekzd5tf_zkUgXyHEpXLQo0tpnZmWe3HHN_2PUmwYEym99ARGbmpuDQ1WheBFPWY75xWb0q1glxsjCUAkPoqSVn1sDbv_U-r2JQXX1kIOpsiixKWYFdFV15rtTfLi9CALynsvkwsUXR-ixnYv6NPimeUyLfEsveH7vYjP3ldx3AefNEn2VWO2i-9Zq_Zqc1EqBBT_WQRHIrMkl1PLOAny2G59di95uTj6AMqNN5nJhk4DYluZOOzczpn9wjDTdDO1k_NzFNVqZkpOFOUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي الانفجارات من ميناء المخا عقب دكه بالصواريخ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87349" target="_blank">📅 12:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مراسل نايا في اليمن: أنصار الله يطلقون أكثر من 20 صاروخ باتجاه مواقع مرتزقة السعوديين وجميع الصواريخ تصيب أهدافها</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87348" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87347">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT77JUqTAFMdL_ifJxd9pUZvOkb9LRaIdVYacVpwGuLJopgqu-kzjcqVgcVQrBUTsJ3_EG-fM9cO-SX_6RHdah4HNlG28eMN9ghgtg3A7tz6EqJTs-5D2zc4kDAEPcjuWYVHAhlJmQRRzAaPi_WTpENHmdejcbYcJMPR9TsPGAuxHT2MiBWiXSAq-XXXNr-M7D8CvdBj-clKO9xBJ-M9ZjrGLeW4nh4u1k6BOV_tOF8xj8kF6lziB5v6wwgNzYxTvPtvGw1L6vh4aiqIw-xV8GoGjMV8-BHt2M_Vw8EGc_YQqzJxJG6rIxPk6EmkcHFAqORQ-E9ax--4RyWkyiSrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار متتالية تهز ميناء المخا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87347" target="_blank">📅 12:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmTlP9OEYEjo9YmlI4F-3vMBWt6_83hEhfZjaq4KlaQjKMbSvn9BSm0OfuWtVoeuAOcanJJaQwkxCp3mUvQHaxzEYsw9nW_ynWrq9YlFPCbTHDRUPAlQHEJNNaJYyjqkhD2L7JT3h_0BTcPZJHhxZEoEaDfI3Xv8sBJs6DGEgnnbhGtUuXMPKDqpbhC2Se-p04FxPufotUojGHfT1q0tvjVCzd6COVTGz4pjdpcUXRc7KZ6L__1aH-I8FME1JKTGIx_P47wYsos6ckoKH3RIPFk9X0hQ637orPUuGpefPErU23rQ3KX03ysbGK_ZMzdyruEPh3A1F90wh3cKhK-QxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbUpHmRXZGSuzXq_Gjno6doQ8SjBnn63kAitOmHZu3nHqDyzaDRWmtQkuU_K0iMS26FUFSxx5VVquaM8HoeAMRWNV8dlRXp8zejF-m51jshgXwESp-YV58JMoxK2tBA3eK3UONzrjyd5mGoOejQ3knkS5E_Fxlz4tR7HKQybm9P1VlM643K401SSmCkOwhF7hc2InJyLBobkRcvevjb-QECa9uyEh-_9FQ5_Hsdhp8QFtVpSh5zacDy1N-BplzTMpiLGLN_J-js47aTa1EZvBXPP4ts-1rKuO8kjtvWISg45r-xfGOQKsehFmFQMb7Rj2GEzlbGztDw8jEV4WIpXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvkyBdw2WoJ9BGPXWTja7k8XHbf9Jsxialf4qXuear8v2wGAZuRujjqi_Vqzz3u1uazSLcZ2Q_HOkhqpigdigRPndjiZ8yGxLflR8eOjiqHn9TlnLssibhcw35fsbjs4-imj9SWQb_WQ-6HYngB7QyXF5VLG6SlSEOb-zk64Mrn1w8Bs8Kbj7Dy43g32NE9Fxy_4hpmkUl_-tCw16YxJswX7NVIpS0SqAZYKl8Y5bf2yHrepQof0A3qp9sW9Tq1rWJ4NIn-2Oo0_IPvWRkSJO22MvlPvbMS21SDdCNOyKXdV8kYCFqn7f0_s7I7-_E0KRrm7IhqRWCgDX32GVThSFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات عنيفة غرب تعز</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87344" target="_blank">📅 11:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات عنيفة غرب تعز</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87343" target="_blank">📅 11:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FX6tmso7haY7YLUudPGztu_8cVnDm5bq86DsEamttRoxulcfIbFy3Lh2yteqEtdSPc6dEwl_2DCMaWn7-jfpMyv7j6UsRrJcTA6M2VMUzUDGzS8o7OY0Jv_k7rRA_YUV8XNTOgNVpPLwMzqagsf_pbPY6hWwvxtLv1DEmtCectGhaqo91JSoYlM157ZQF3mF-HXdIz48v7kG4Z-hoa0Pt4xq8l-jyjggFaanxccFK6uTw1TLlUHF0wdq7CHaxK8jw2qhAxPCodIbLS_s5CTe343Sleol1rbzsZ0oUSjnyBfSH3ekU4Ltl9z63rFlC6Vys80KTKVMGuLYH2vdaGnocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpPY9h5FEttV-MHDvD4n8snp_ELsNyN-UV6N66AiB0nxY_O4mIQMIyMH5vjthxuGQ5FjCZpecSygtPn3sPf8RO5NSTtPPP3U3JbGEHjtib4UFQhQyw6ITrvH8-B6JROkuvMD7OvNgXIJ4TxxybHkC_F_Tc5_RX_YAp_MZWDOLYw5qvdL6hQ2Ewq_zXFHGwnXTCajvddoc9G9OD5ikG98SS2LEqLvozDAbtYa5JWTXJBs7xhw32ovhaApk7-M2UKrwq7P4bhhqg-KwbIRsbWDmRAXksNbpL8-wJidiUZ1X0rlE40Ernm_3Hy7fKsd1U2tvUcIhlysuN3K-66fA1yIhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر   أنصار الله في اليمن يطلقون الصواريخ باتجاه مواقع المرتزقة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87341" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله أكبر
أنصار الله في اليمن يطلقون الصواريخ باتجاه مواقع المرتزقة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87340" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87339">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇹🇷
🔻
🇸🇾
إعلام العدو عن تقارير لبنانية: تركيا تدعو إلى اجتماع بين سوريا وحزب الله، معربةً عن استعدادها لشراكة اقتصادية وعسكرية في إطار قوة ستتمركز في لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87339" target="_blank">📅 11:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87338">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj12E1tgebYweqzRT9HkII6AjJ7nZozMWHyLPed_SX44mpXjStMXF640_-VNRQ6EpMQa0H40TCtrAag4TPmbJnV0H-0_8HLggStvEsXPOO09GDRO9IPpD5RcNvannFPlNTxNcw8ulpSKdlKVGCVtTi38TqW2FSqrcH4y3af2vFOtEqFl1NzV5rY4o-3nBuRyGxp5ntmuAGf-uTyneS2pWnxUMVYZ3JtDVpvy7nWfKXitVxpuyfTvSTpZt0yiBDRKRmMVDIceMl_N_YuAq0kkkqoUZUU4kDA4v3cRurMNjf_T6rUecfGbteyCrqZqphti1NrpDNdlsmWxTrQuGSy5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحصار بالحصار
القصف بالقصف
الصاروخ بالصاروخ
هذا ولم ولن ننسى دماء ٢٠ شهيد من الحشد الشعبي العراقي على يد ال سعود الظلمة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87338" target="_blank">📅 10:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87337">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">والعين كل العين على مدينة الملك سلمان
الأغوار وما بعد بعد بعد الأغوار
صديك هندي حضر كاميرا انت نفر زين</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87337" target="_blank">📅 10:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87336">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لبيك يا ابو جبريل
لبيك يا اكرم الكعبي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87336" target="_blank">📅 10:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">المتحدث باسم الحرس الثوري الإيراني: استراتيجيتنا هي الحفاظ على المضيق إلى حين موافقة العدو على جميع شروطنا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87335" target="_blank">📅 10:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87334" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/87334" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87332">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇦
وزارة الطاقة السعودية: اندلاع حريق في إحدى المرافق التابعة لمصفاة أرامكو بجازان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87332" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87331">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر
🇾🇪
تمكنت القوات المسلحة اليمنية بفضل الله من استهداف مصفاة أرامكو في جيزان بطائرة مسيرة وكانت الإصابة دقيقة.
‏يأتي هذا الاستهداف ردا على اختراق العدو السعودي بمسيراته أجواء محافظتي صعدة وحجة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87331" target="_blank">📅 10:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJ_F4MXrw3TSlBYhAvkkHwovlQQMqK3fMcZdEHh8f7Sgw7Xb83tIXRSm9cyx3w4zjMEKcbQ806-P6BYLouhufMyA5uLnqupgmflx8vTtlNdwb7BgaLm9-X_ca9Ilqgu92nc9bceeQWUZlUKhQuyXFReaEOS5KacV8FLHFzWNRmJeDQi25uuYG-8Z1_NjdYu7iPSDRsElA5g9YDF3z3egrZpVFdqj0UGbTsiTc5xmS0UZCnWxoEx9wJLN08MvXBqXBJ9CTja7a9CykWlATmVjee4ruDa-V_ujsPmEQwzAQR-S0vBvMIkKv07PqNYIEQ736SbN4XxnJkKX45SsdD_uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd75zy_MaNfX1M1OREOp955XyqnicNbyqVPZ4e9rybdUACY1lGG_22BNOUlNVPrQM3gbTlnhpjST1Ri-0-iAom4g7aHOS3sQn2kjHF8px5-ddKCWvgD4MDRfHzP49kF3DTNd3tHL0ifmuE3Dpm7XhHS5eTHoC1BfRFZgKwhhzSPDVWo2kEAYyjBoG7kYXu8TiRwlAPZh7yVwZ3PqSWIOH7a3zDuGZs0sPNQ2Hvr8lqH7hV9u9eqeN1IGP1_4iIJ9NtMLhWZXYCjqMAI8_7pF3VS4CLQ0YAqCkyrrJGNshMh6IY6CVhmfLJQj1tyMbSH7K0IdFqDGMi0MkHVzLIAgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvSJlpbsStWmeMIE5uH5dykqR5w2_Et2Ga4QaKETEPaTki8K1QGrFa9DjZBlha8P288oiqREawSNax4MX1tso_m7wZFfosesjvfNV-ISj3Fv8Yn7MsblBL6YZBYR0mCExbke2CgBiL5Z76zg_BupN-XPnwF_tayvMxPMFUY_RgsETnfcfcP3pK_tAuC0LhVTHRY-2WfbRqYxPTHkF1GjsavPMicpxJLCNkyBj3QlHHwkB45-7ezou43HVtEllNkpn2frlBDJlxN7MAFMuXCJpKEZgSVtLC_PfureHvGobtEPDRCznyz6_4sBN9USsEYvYgvDDpRCKzZ9jdYIqXHleg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
أظهرت بيانات نظام مراقبة الحرائق التابع لوكالة الفضاء الأمريكية اندلاع حرائق وتوهج حراري داخل مقر قاعدة اللواء الخامس العسكرية الواقعة بالقرب من منفذ الوديعة على الحدود اليمنية وذلك عقب تعرض القاعدة لسلسلة من الضربات الصاروخية والجوية بالطائرات المسيرة والتي نفذتها قوات "أنصار الله حيث أسفر الاستهداف عن انفجارات متتالية واشتعال النيران في مخازن للأسلحة والعتاد العسكري داخل الثكنة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87328" target="_blank">📅 10:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇱🇧
صحيفة لبنانية: إندونيسيا، وسويسرا، وبريطانيا، وأذربيجان تدعم تفكيك حزب الله عن أسلحته بينما رفضت إسرائيل أي دور لفرنسا.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87327" target="_blank">📅 08:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇦
إستهداف محطة غاز في مدينة الجبيل الصناعية بالسعودية والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87326" target="_blank">📅 05:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87325">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇸🇦
إنفجار في السعودية.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/87325" target="_blank">📅 04:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87324">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇸🇦
إنفجار في السعودية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87324" target="_blank">📅 04:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87323">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0909aea.mp4?token=Prs6lSkPPAaSIEAsFrMVirmQKmbMd0rr8Ol6S8Qm5l33v3K16vPilEBJ2vm-S7pVsVyY8IRMXGQZgQ0W5m5jd9yok7NOHr-WpfqpM2iellNTDZr3Jap59kqoa6sTp9O4eoIubXdkqez7HZ0AlhI3fhAOEN5y4WUs-xrWBPdxDZpE6RiYjUuOZNvdCUkV8AFGL9zQQz91P-is2ezkbSK5FzKHak6Z3H3v7gCRrslOsS5YzgYX9vbLDyML3NOZHJKZVOhuAlA8Vgd6YDf1w2eQxbOtWtmZ-qswH9Iz1O2sehJw9SGLpPsrqQBu5TtBGWPP3fyXvRcqcrKEg7R-0yooBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0909aea.mp4?token=Prs6lSkPPAaSIEAsFrMVirmQKmbMd0rr8Ol6S8Qm5l33v3K16vPilEBJ2vm-S7pVsVyY8IRMXGQZgQ0W5m5jd9yok7NOHr-WpfqpM2iellNTDZr3Jap59kqoa6sTp9O4eoIubXdkqez7HZ0AlhI3fhAOEN5y4WUs-xrWBPdxDZpE6RiYjUuOZNvdCUkV8AFGL9zQQz91P-is2ezkbSK5FzKHak6Z3H3v7gCRrslOsS5YzgYX9vbLDyML3NOZHJKZVOhuAlA8Vgd6YDf1w2eQxbOtWtmZ-qswH9Iz1O2sehJw9SGLpPsrqQBu5TtBGWPP3fyXvRcqcrKEg7R-0yooBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضيحة من العيار الثقيل   الرقم التسلسلي للمسيرات التي عرضتها قناة الحدث السعودية تكشف ان المسيرة هي نفسها التي تم العثور عليها قبل ثلاثة أسابيع في سيطرة واسط .</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/87323" target="_blank">📅 02:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-rSb8fnsAs1cz4UK3BHUm4ebVtCgCP3xL3qHJWbVF6DvWa5DebfXOsyUTdjnA0tcvc7Xap_bo2B1zeXH0nd-LrhDVpqpYLQQZYJEMauHxhlXIajahrZdh90T8_l42YFUTUD33UlNhTZyIDj2YqMphxxbp21BQwqVsZtr_hXo0tPSgoR8HKHt7TFaZGcijB-nTE_GzV7HD4djeAMUIWuNx1MrDDRFnafjEX_0cpoZU8HGSfOvutb0M0fKVjvOyeZ2xGWMfp5UbT_TvFUV04-N80wOE39ZuB84BYmFzNiDqjL5xEZvHL7jDdm9KNG8eHTNuvhLlI4ACGQsm5iVBxk0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصورة لنفس الشاحنة ومن زاوية مختلفة مع شاهد ١٠٧  التي تم عرضها على العربية الحدث السعودية والتي ادعت انها في بابل   تنفرد نايا بالصور للعثور على نفس العجلة لكن قبل حوالي شهر و في محافظة واسط   العربية الحدث ان تكذب اكثر</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/87322" target="_blank">📅 02:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
دوي إنفجارات عنيفة في محافظة ديرالزور السورية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/87320" target="_blank">📅 02:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الو محافظة واسط</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/87319" target="_blank">📅 01:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUHS2DGIftnS46LY29Zyg2jzQ7AweEkKXK9uKnrnkofzLISUY44k3YcLwWa_zY8OXsXxrC6iYEgaA7QDgLvssc6-6-VUe8y-No72iv7MaTEbD05vjDfK1dxJJrrc88SM84s0F7a8sMuRqsuhThOUEwhP698gxHNkMwuxm_PnQodkLQ6_ssNMzv_wtWbhHNq3bzlHaWNf5Eta6O-YEDmQFBuheFSlzAnQbAugaC-X8Ws-HVj6AzdinaNOf1FR8kC6aF-wkixfnhOkqHpS5DN0uxDxIc_26n7U7Rf_l_blLuwU3_R3T15xeFwJ1aJ7ZsZfahXV8b7yenLxF54HB_pwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الو محافظة واسط</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/87318" target="_blank">📅 01:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدر امني لنايا ينفي   قناة العربية السعودية اختلقت رواية من صور تعود لحدث امني حدث في العاصمة بغداد قبل شهر .   المصدر الأمني : لم يتم تأشر اي عملية عثور على مسيرات او أسلحة في محافظة بابل ..  المصدر الأمني اكد لنايا ان الحدث السعودية والتي تبث من الرياض…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87317" target="_blank">📅 01:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq52SjfdDPmEFOgnZUt25vvufiUqObtoNmqPeqd7LYjWPAuFyl4KUSsQSqJt_w6s-wAkPJ-myG2AXSyXwTbVqwZx-3HvfqRKU4K-0bSsb6rWzLzpVYasZQ9Y6u0wcHCZYCOwJEfRvKaaiHr4bFBgvwZypm0_25zQccvEErp9CD4t6zDeLBXQ8ofZgKJ_yNR7iKHcpesdVnJEBA3x0-_4g7FsQvSN-5LVxt8bcX3VMH73OjqiFsi2iDtdoz02MYcmlp1t4o9UTExTx5wUVKGHAGW9D-gZ_fHQhMEYgNDf9tPwW8wq_swTk6EOlijUHLf58hvgBjHStHrYloReR0Zgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر امني لنايا ينفي   قناة العربية السعودية اختلقت رواية من صور تعود لحدث امني حدث في العاصمة بغداد قبل شهر .   المصدر الأمني : لم يتم تأشر اي عملية عثور على مسيرات او أسلحة في محافظة بابل ..  المصدر الأمني اكد لنايا ان الحدث السعودية والتي تبث من الرياض…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/87316" target="_blank">📅 01:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نشرت منصات حكومية عراقية خبر لما اسمتهُ العثور على مسيرات كانت بصدد تنفذ هجمات ، المسيرات كما تبدو في الصورة هي من طراز 107 شاهد ثابتة الجناح ؛ لكن لم يعرف وقت وتاريخ العثور عليها حيث شهد العراق منذ حرب رمضان على حالات امنية تم العثور من خلالها على عدد مختلف…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/87315" target="_blank">📅 01:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOpedcODANWQx1am0Bkhln0IWnGTn8i4dJj6OJndRcY2byVYWFdSrx7pVJKlikh7ys1ZjFOs9Ug-jl-iEZpFVS2O4vLCMmwm3thJildXPk-c_Qc2McN3KNFtp_l-cSyzEpNOFyH0Z21ks-L9TkoCFYIAOqFZAeqsT2SCRVa7G76upWfEFIs5Ri8yiiCmSLrainDq8pkLKdjFQKNMf7921isY173goF_gBunvx1yS0hMGkPwZM5v2I7qmsk-I3i2fBUp3kgcvbI8Wan1TighTVQ_DQqOxTlCst1md3TwDms-rRzk5b4XW9-MC3tkw98X3abhKZ7nhXNrZ8QnylVmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشرت منصات حكومية عراقية خبر لما اسمتهُ العثور على مسيرات كانت بصدد تنفذ هجمات ، المسيرات كما تبدو في الصورة هي من طراز 107 شاهد ثابتة الجناح ؛ لكن لم يعرف وقت وتاريخ العثور عليها حيث شهد العراق منذ حرب رمضان على حالات امنية تم العثور من خلالها على عدد مختلف من المسيرات .</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/87314" target="_blank">📅 01:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي: فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87313" target="_blank">📅 23:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdvXXAVH4-8lv9aWEK_XoklOQqbgJQ7bTIyeSdHIUxa6qM13XTYEYfsQcEre9ZVzekGdnZSaj4lBVNb9uu9qfV92EoQAgeNkJfIK-8YV8EA-Iyb7wi0c439h5E_4BFheRtitNWvomAjlr5mGDo3oW8-3mKdqaaTr3N8JXh9kbX2MF2J2zrtVSt41XOdR-gzKVcnEvExaaTlACvV6d-vevjDnytAuGI4AzAhBk9oCB2Vf7R_UBKuRZVLhH0x7RbH3YfGCtVUVOSvP-AbwjCM81Ebw0TPA0T0sHQVNDKnv_4hrN-L4An0i69JL7yFQk-prfSYP6Q2I65UlsQqzQ5gTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معك يا أبا علي
قائد أركان المقاومة العراقية البطلة</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/87312" target="_blank">📅 23:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118fa7dac6.mp4?token=rYepw5kxtXmwbpFq0Mmw90eJetut_-1qK2w3rKTYaVHnq1ukn_SSK6e4wIG2fsFwF4dWNnkO67SvtnunBcaJesmoBo0SpqkS1TAQ_FFhn-jD-U0t3G8Ct95V5mQqo4rr72dZiNXXEZQGpv-uNpQvez0CiuKs4I8mkZlObccfsw1eC_LRsK-CmQOm2ppCeYek6K2k5eFgj2Pj02MbcKCmMLAD8CR6zEMepwNilutDWuXDHCG-goQpGnZFPzsdapplG6eK6Z4ZyTTFZ3p1PSZOlssuN6Rj5Xgc-oFqRcERXDXjJRrtMXkCXPBSRLs9sC7nCyooGE-ODaqQyTwdTTCwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118fa7dac6.mp4?token=rYepw5kxtXmwbpFq0Mmw90eJetut_-1qK2w3rKTYaVHnq1ukn_SSK6e4wIG2fsFwF4dWNnkO67SvtnunBcaJesmoBo0SpqkS1TAQ_FFhn-jD-U0t3G8Ct95V5mQqo4rr72dZiNXXEZQGpv-uNpQvez0CiuKs4I8mkZlObccfsw1eC_LRsK-CmQOm2ppCeYek6K2k5eFgj2Pj02MbcKCmMLAD8CR6zEMepwNilutDWuXDHCG-goQpGnZFPzsdapplG6eK6Z4ZyTTFZ3p1PSZOlssuN6Rj5Xgc-oFqRcERXDXjJRrtMXkCXPBSRLs9sC7nCyooGE-ODaqQyTwdTTCwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكرم قائدنا الكلف</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/87311" target="_blank">📅 23:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87310" target="_blank">📅 23:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي: فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87309" target="_blank">📅 23:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LONvTWp1Y7kpu_-x24X80rINMolQAnO-WglqCs0ZcxzSs02O1izfBNRYG22VtmjlAgbzIXExfDd_glg2c0jUYH2d_F_5Uxtb4dY5nY6Q9DwMU8eGqadd0mt9m8C-AZAaXtog3FmkmkY9TFd7RRfz-P0gRSm2iiSuDI_OqFMnPuqq4MPzyZVJYWG6ofq77enGCSR4dXKHuq_V-4vzt_y5lTzjQeqAWs8QLmtoTYHwkXAuwnhlQXXqa7L-dioxT-c41jdySVw3_zzrXdWrN84bmBjGLongx0qGn85ItvVauRCcuXiDGyAjcAdowc-AUpRz5ZPiI43PEMrqI615g392lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي:
فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/87308" target="_blank">📅 23:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
مرتزقة السعودية في اليمن:
انصار الله يجددون استهداف مدينة مأرب.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/87307" target="_blank">📅 22:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8iE4YaT7gee7JrVfFrfp4UBpZKgyaWd88BNXnk2ipK9dFDk8f6T1j--h8n1Ck0zNSxdUvLaiAItN8Sx0AkBHtPfxUHhqvv5_4yuqrl_6q9cah0kox3K_sTrIuSyUB8WLjPaESv8FI13VahgWwZZYLyDO5HExYUu4v5yQM4eThCbCbcZX6MOLdonVYYnvp_DM2-af4sbTot1DyH8T5qrd46V6VNlYGn4QcyisGunIhXBaI2u4z1ASxQoDiyENPg_LVtcRh5GBMLgXajbXw1_x1e6XhJJ6TZ5SQiEh_xf5rBG5v8S4OBJxHmx9wqSvv1Ubvi6NBjJ78HDHN4I6-usRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZYc6yicTFy5eu6y8brfByIo-Ic9iMtnDSdH4tilJFFpMDM2dv1PkEnrnVj1Oq3mlScqoJvXexH5iUPNtZqplNot600Si3d9XqKT88PWtHwX-5xUAD0r4ohO4T_OUl6gkh8FBD2jJEG3KdrG1n1fH2QDNFaurQktWyrxTABqi7KuMy8XoIDML15NINKysaez20LTrVXndVhYk7p74Pzo6eWFR6pDRDtldr1vr6vA3z3kwO_cr88w0LKG96PxF-sTDBfWxRLjVwBLexvJUPOaOZkv22XnTqA8Ij2xrtmQ4vlcditJihbRYsA8NtXgjARIySmXsKxzzFCOGgerCmJx-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/87305" target="_blank">📅 21:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzpeUP5FZ3Obuz5zP7I2govg8VRlacF8VjBv2CyUvcFr72_B5fNey_pudbUj-RlL5UJJ3I95RQA3nA1tF6J3VOFficS0qROMARMGEyp4A8srWkyqMY_ZKcZGG-m46gHFJQ7dFTH9DZRqS3uc2tGMzTx8M-A3l2qAnm3_zqIUne1v6ZzP127yRtuQCqfgg2OXl_BwiC_0f_qYB9Z5sEUcFh8AaOsW_ShdIJNOgyeB85H7e7Jb-keD5-VWScgNY_2AKPbV8BlGUS9CAB0cFKc1ORRILtHRgNkfs5YU83UYnaFX8ciiyPhbw34ss6XHkPlifS5WHFRwhk2JbtWtnEY6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدٌ … يحمي حدودَ الوطن .</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/87304" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a735eda5eb.mp4?token=VAovY1UrSusDbidd3A0BmTahxliFGPjdT4nhQy2t_UoJTS1YEq_Rl9Mzi-7zJ0siPKZqW29m_pqxSc4VxnDatRDzWVlrlg47atrCkMxYchxCHQf3Zz1rbt_fPu41amk2kK81mgzK8IfhEiAKh5dgdf_bbUzZIpqVxA5XO6J-FhYbrJa-DsPluRbvQy8Ir2DXnm8Ru3Iu6i0RG_SfDhsEQHl9splIP6BOEREOj8LTYvGP7lANURhZ5Sduhs37JgPs9lOt1hml5PfQiXckAobEgDiJecSJIOK_AcvxYGGsUsJRss98NEh7SOPDgPqpDRBi7W9RdBGodKxYaHmOccwiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a735eda5eb.mp4?token=VAovY1UrSusDbidd3A0BmTahxliFGPjdT4nhQy2t_UoJTS1YEq_Rl9Mzi-7zJ0siPKZqW29m_pqxSc4VxnDatRDzWVlrlg47atrCkMxYchxCHQf3Zz1rbt_fPu41amk2kK81mgzK8IfhEiAKh5dgdf_bbUzZIpqVxA5XO6J-FhYbrJa-DsPluRbvQy8Ir2DXnm8Ru3Iu6i0RG_SfDhsEQHl9splIP6BOEREOj8LTYvGP7lANURhZ5Sduhs37JgPs9lOt1hml5PfQiXckAobEgDiJecSJIOK_AcvxYGGsUsJRss98NEh7SOPDgPqpDRBi7W9RdBGodKxYaHmOccwiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87302" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab4e142d.mp4?token=s7lLuf30ZswMoQVLY-sRKU-r3sQIBGyTCxs65pMgVMBQIzsPRt7kPTwpmqezD6swYTZoT_dmqw-c7SCg0KG44Zr-kgtIk4fdLrqLk6GOMEmEQPJbU-6V-6fzYRtL0D5v477_BKQvkpdCOGdY7Mm3sIYM9iMlJ74k9Ibq-Lne6nIIs32D7-bkAaNRVprBfMGKeFAz2oLByOSbm9bKDZR_HQqt-3spuZSmqfj5r6JhLrLQEtb2mmQ0akIWZSctorgGPMQokQYJ1-vQJiWLLCi8c83hD9kZOMnRa7A7yGB7duo1qEPewqchfDyOb6KYdvGcWuT1RX74lVS6r6EZZsSIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab4e142d.mp4?token=s7lLuf30ZswMoQVLY-sRKU-r3sQIBGyTCxs65pMgVMBQIzsPRt7kPTwpmqezD6swYTZoT_dmqw-c7SCg0KG44Zr-kgtIk4fdLrqLk6GOMEmEQPJbU-6V-6fzYRtL0D5v477_BKQvkpdCOGdY7Mm3sIYM9iMlJ74k9Ibq-Lne6nIIs32D7-bkAaNRVprBfMGKeFAz2oLByOSbm9bKDZR_HQqt-3spuZSmqfj5r6JhLrLQEtb2mmQ0akIWZSctorgGPMQokQYJ1-vQJiWLLCi8c83hD9kZOMnRa7A7yGB7duo1qEPewqchfDyOb6KYdvGcWuT1RX74lVS6r6EZZsSIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87301" target="_blank">📅 19:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
إلقاء القبض على السياسي أحمد الجبوري أبو مازن بتهم فساد في بغداد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87300" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
🇮🇶
فضیلت آن است که دشمنان نیز به آن گواهی دهند.
صدام حسین دربارهٔ جنگ تحمیلی علیه جمهوری اسلامی ایران سخن می‌گوید و بیان می‌کند که ایرانی‌ها به‌خاطر حوادث کویت و تحریم و محاصرهٔ عراق، از گرفتاری او خوشحال نشدند و شماتتش نکردند:
«آن‌ها کینه و دشمنی به دل نگرفتند و از وضعیت ما ابراز خوشحالی و شماتت نکردند؛ بلکه با وجود هشت سال جنگی که با آن‌ها داشتیم، خواهان همکاری هستند؛ و این‌ها از صفات مؤمنان است!»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87299" target="_blank">📅 19:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f5abbbce.mp4?token=UTdu0fXBW2QlQCmPSONyUhxWMav7GiXArgl1pm2M7aDvmm3gIiim5NyXVFap2sWGaKxZWNbxqMd1Ur7l6uHYQQRCg9IfTJ9984TRdeBviIUgnmj2_O8zTCXgW1LDIs5U2mCqj5kWK0FKyV6LmF9CS8yNrOb0N1RjPlTF24p0CGigppXmYISe5GRPDftBY-tNNPAa-CqMsPyzb4SKH9S746B3yolKj1QehBwVIzuMEqF8IwjGB0HS72GjFXwaK-FwrxEiIGWLqmTbD1Y0zjv8hB6iv9ovgr7NiQhIMISRyLOIlypNm0m4YlKnW2vIpLEtPdHSXc2mJs3nWH_9Q-rKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f5abbbce.mp4?token=UTdu0fXBW2QlQCmPSONyUhxWMav7GiXArgl1pm2M7aDvmm3gIiim5NyXVFap2sWGaKxZWNbxqMd1Ur7l6uHYQQRCg9IfTJ9984TRdeBviIUgnmj2_O8zTCXgW1LDIs5U2mCqj5kWK0FKyV6LmF9CS8yNrOb0N1RjPlTF24p0CGigppXmYISe5GRPDftBY-tNNPAa-CqMsPyzb4SKH9S746B3yolKj1QehBwVIzuMEqF8IwjGB0HS72GjFXwaK-FwrxEiIGWLqmTbD1Y0zjv8hB6iv9ovgr7NiQhIMISRyLOIlypNm0m4YlKnW2vIpLEtPdHSXc2mJs3nWH_9Q-rKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
فانس
: الإيرانيون يتألمون ويريدون إنهاء الأمر، إيران أبلغتنا بأنها ستسمح بأقصى حد لتدفق النفط عبر هرمز لكن لا نثق بها.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87298" target="_blank">📅 17:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🇺🇸
امريكا تنهار من الداخل بسبب ايران
إعلام أمريكي : ‏ عائلات 5000 بحار على متن حاملة الطائرات الأمريكية أبراهام لينكولن واجهت وزير البحرية الأمريكية هونغ كاو بسبب مزاعم نقص الغذاء وتلوث المياه وإرهاق الطاقم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/87297" target="_blank">📅 17:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7KKhG_n6U7MSGEiWUYkP3gWhhHtfZm63uTSeFXCPLdfq2lRPulWef34k5rZZKZ64gh9cAIsMLwvzdKnjVgko40nHwDufmNpm-002wBuRYqp9SzO7jZeGOpYeWNCpNe2palp-oSfCCsygwc5_qaEkwkJtQHEW8cZUKFcKuqgFzO7_HX3SvpaSlDq_-F2vWENQ3nr3E283fMkpxIuQJAKmwH79ktxuVlFrd69bBi-HGFV6pnZaJDKqkFkzPKZvk_DMO_rRbAdRY9evnPeYte_AUlU2wOXybErKnnlkxBeX3DWg2fjjudXNMv9T4hPQgsHNiTITlhWdyvDPVmk_4bKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر ذو القدر، الأمين العام للمجلس الأعلى للأمن القومي الايراني:
طالما أن الولايات المتحدة لم تصحح سلوكها، فإن مضيق هرمز لن يفتح. المجلس الأعلى للأمن القومي لن يتزحزح عن موقفه، سواء في الحرب أو في المفاوضات.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87296" target="_blank">📅 17:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0k3eLxomTY6ERBm1yvG_xGETU8YAkdXsmAwcXmksDkYnxq1Mv2lLvChVM5wka1pPCeOu2yXgzzbsur1LN1tPNlSET1TSirtDotWnEO_tPi6qnORdX1n9AeB9QRL7GRV0ps155YfkQf8JRmjzf-1vuL8-Mp6Z0Pao4r8c-MbsIac-htnPP98-3U2XiLvBNwVG7NZ9hS7yGvWHNTJqbYibPKwwcIY0S5YUSf2YLGjIa9OUEuPJWPx7dCrRRbDuKAEfk14hDtqut9wpos2VOHA-D_DOe9gOfl_dP_0uRTqD96gAMZ_-W__91Mhs2MzznNtjNP5pywsZYNqYTBOgdc_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCMg6Ctlg9CtLdjwGJEIV2in-jYSTZMS12wZ7fgOlhchawCnHwxr2iDjM2KxLQDVBiiAUgXW36NRqLrTsbhcyY0-XJPc8_Zmc1MjSiH1J1nMMQKBBy3Gsw2skB6T6_WRiArGu5DF0FpQjygqun8OWTUpSmTjvxWvZQSkthKLl9Bnha2FzQ0Et6e-H987XCv5Wi9_y1ZG0zuylneVRCC3V6VwOs0FR7JX_APejIJzGaX9AEvgXbr0XitR20vHG9iJujG0aKzJ6oy_G98t_T9umAFor7iu0mUV529zCUzCqrlC-HakuEYSy9iMmbMNGrKAZzlnULb_s4tnYR3uY2uclQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علي فالح الزيدي يستقبل رئيس جهاز الاستخبارات العامة السعودي</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87294" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حادثة على بعد 18 ميلًا بحريًا شرق مدينة خصب، في سلطنة عمان.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87293" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Min1FiHl8JSnUVT6LiR3hYqP8F2Kqp48m88ssyWci_tnhKSqBKeuunoZ2D910PwcyLzmmfZoYbsdMl1sKaSVUscr0sUM5q-m2X6kR-v05qBuYQdjUqopgxGetpjcZH0Lw5CGpK0Fy1PQbTUb-UQncjm61BYxY4QOSbEwT4TUaT0MGyE1MLefGuBlRgnomW1gAIqMmk8X1AbgyzDA7jodU_w-nrjXOQkPFJ8-P994N4-vn085XxZlbDy-rFaBYEXfG0W90myPMETBJLmy5reKgoI0mcjk-2sPRH2G4K6uGGUY_datHJIxytvMIeI2PmIwg2yGDGmBeWSm7Bxa2-MvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87292" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87291" target="_blank">📅 16:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvjxkFvpA7FvS--KXKZI-_8esotB0TuERL82I-BqnkBWmuhbBPOt1AHI_LMqcJHpxHalComizi_cR-bwcj51n82afwLGZPW1JY_UHFYLJeumoThHeAqzN3-wM7xLCr19geKsQKr1js90PqaxeNjJc6YoTcKz6x2ngkJqbBnpupSBq3czD8XPFaqIN5uAvT2aMf-aQjsP9LrCJOOkAExptS-BvZypdPXuy0FtWpLuoGuPIIasYNCKPvNmT-krmsW62AWwpQWzr42PHyCSdLAHn3GmPbKD3zkhHu3juGzMQaRmVAUASat9gU1uIzLci0Q7zPMrEsU0Y7KFYfy2zQW76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8CVCa3Prxe1YR-3_xMXi0McRi_wRWjjJ8NZ2tnroohguLkjA8xiroPFPrF9xUOq2e7bSvzHj3GtiJm7qsuM0tCovWDC0jhFc7FELHL6MFZhXpl9vDULb7aSg9cj5fW0aC5L5GQKekdtdjX_Vv0b3I_enmu0TFWEGRjBz83H5_nbWlAS7WQdUX3OEdyHy4U3RHX91xmVJfAjWOS_odojIUMugjy_lio6bdUQIjeTZmSUoF6iObu4u50tUH2WMYOOnqqsafoP7j_A4uiPyNhnYglZ-h6VO5QLDdG5Dp9V1YtqPHv5J7o8hCT1mhbos9q0xCisNwI6sKsUzF4bup2imA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nodv9fDby8yN7d0K-gM8nRPL4tOQZMFDUjOOnsWszGDaRW1dFv2sHan-7wGdUkQNv9HzxztRQoqtAuR2_TzABVvtPg3YmRrP4fuVhF4ZtYpZRjEaoxLR3aziqVvPPUtK1WTJ5uRXYFdZ0GH_caqkZtW7qYv5i6MDsJOimOXNqa4limuyuDK58uFSfxUtiD38X7iKzleif4ji-9lXcUa7-qoOz2v5ynAkhlEPvirtH42EGdJ4dBZqkfJcs8R-PB36An_5-P1_0xp1qCzavLyLg1EM08zo9mddVui9AOmJpwTcop52YKG2sZxTrH6C--yPSyBQpNf4sWuD4MnaNMN4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBOrs1rjp7bpfqY6tu1BVvN-oGrvFZCb5WSSCe0RXLvwU7obMiCh7S9K1J8ElIkOPfaLpHuOTQDhtq13tVwjODl6pFYjIXbzI9oa01asl8bWaccNTA46orJjm6qWxU4Z4puxvoRGcjUho43mJpVyLVk76enpK4hkCKA9KfC4CAVlOXGTDXJuZ67hihXGgbGfYYvGyXclD8HDDDvQ_cH2T2VK003AG1f7MNW5UB7rJVC6Pb6TVJWBkLsbrfe4XM-aCn-spzQ6PvAQKogxx8F7C48-Ebvww8NTHLpogSUhAlvY1tMK3i-yYLN2M0O4NBUeT0rnaTc2sHfuBFXnBHxuaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">السلاح المنفلت في اقليم كردستان
محمد حاجي محمود رئيس الحزب الاشتراكي الديمقراطي الكردستاني يستعرض بقواته في مدينة حلبجة بالاقليم</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87286" target="_blank">📅 16:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سماع دوي انفجار شمالي مدينة مأرب اليمنية وسط أنباء أولية عن سقوط صاروخ اطلقته قوات انصار الله باتجاه المرتزقة</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87285" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
يوم 30 أيلول المقبل يمثل الموعد النهائي لانسحاب قوات التحالف من العراق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87284" target="_blank">📅 15:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قسماً، لن يسقطَ العَلَم.
#هيئة_الحشد_الشعبي
تنشر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87283" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يوجه بتعطيل الدوام الرسمي في المؤسسات الرسميّة كافة ليوم الأربعاء المقبل تزامنًا مع ذكرى وفاة الرسول الأكرم محمد صلى الله عليه وعلى آله.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87282" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
- المفاوضات مع عُمان بشأن الآلية القانونية وإدارة مضيق هرمز، فيما يتعلق بتحديد مسار حركة المرور في مضيق هرمز، جارية، ونحن قريبون جدًا من التوصل إلى اتفاق، لكن فتح مضيق هرمز مرهون بظروف أخرى، منها جبر الأضرار الناجمة عن حالات انتهاك مذكرة تفاهم إسلام آباد من جانب أمريكا.
- خطة فصل حركة المرور السابقة في مضيق هرمز لم تعد مقبولة لدى طهران وهناك حاجة إلى مسار جديد، وهو ما ينطوي بالطبع على تعقيدات فنية وقانونية واسعة.
- نظرًا إلى التعقيدات الفنية والقانونية، نتحدث حاليًا عن مسار مؤقت. وقبل التوصل إلى المسار الجديد، سيتم اعتماد مسار مؤقت ليكون أساسًا للمسار الرئيسي، وفي هذا الصدد جرت مفاوضات بين القوات العسكرية والبحرية في البلدين استنادًا إلى الخرائط الموجودة، ومع الانتهاء من هذه المفاوضات، سيتم تحديد المسار الجديد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87281" target="_blank">📅 14:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
اعلام العدو:
اصيب جندي في
الجيش الإسرائيلي
بجروح متوسطة في حادث عملياتي في جنوب لبنان. وتم إجلاؤه لتلقي العلاج، وأُبلغت عائلته..</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87280" target="_blank">📅 14:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇹🇷
نائب الرئيس التركي يقول ان السعودية ستقدم لهم دعم مالي مقابل الدفاع المشترك.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87279" target="_blank">📅 14:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
السفينة التي تم إستهدافها بالقرب من الساحل العماني في مضيق هرمز هي ناقلة نفط تابعة لشركة أدنوك الإماراتية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87278" target="_blank">📅 14:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87277" target="_blank">📅 13:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87276" target="_blank">📅 13:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇹🇷
تركيا تحد من حركة السفن في البحر الأسود بعد زيادة الهجمات على سفنها.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87275" target="_blank">📅 13:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgfBaJexqq0BAKQc1q-nUNU-wBcfXguenXXEheRo8Z9tfIzH76ZPut8MIHdMxXkuIh5TT_iJCmHMXVVcl1kEo6fP5SxPEaqcDY51N2TLyXKXdfUtE3XKj8yuEM5VIEh9M7padouybiZx8_8XL5xUOgKHS48xHQpkyEGpb1av2cAuWJubz54gZmWHMrv6ed5_XjedoqMRf5hQHP_T67EwcwuMj29lRzI57yBQvpClieRZOhYT9NVAnIK9IAVHez-DYKaNBD7gcujk_3CpFCbgY_fRt3ir21IYgXpAf6FLXBmd39RlUW4FmF4m2Eu-s1tJWX_IwdIF0ikCt87DHJ3tlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس وزراء اقليم كردستان المنتهية صلاحيته مسرور البرزاني: لا يوجد هناك أي جندي أمريكي متواجدًا في القاعدة الجوية "حرير" منذ أكثر من 10 سنوات.
يبدو ان مايكل سوينتون توفي غرقا في شلال كلي علي بيك
😄</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87274" target="_blank">📅 13:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: نجحنا في تأمين المنتجات النفطية رغم تحديات الملاحة وأزمة مضيق هرمز</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87273" target="_blank">📅 12:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئيس حكومة إقليم كردستان العراق:
ندعم الحكومة العراقية في حصر السلاح بيد القوات النظامية فقط
إقليم كردستان تعرض لأكثر من ألف هجوم بالصواريخ والطائرات المسيرة
الهجمات على الإقليم جاءت مباشرة من إيران أو من داخل العراق عبر بعض المليشيات
لا يوجد أي جنود أمريكيين في قاعدة حرير الجوية منذ عشر سنوات</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87272" target="_blank">📅 12:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrrDH-KjzkdQ5d3iaHatSyGRwV4lUdVU84iSYTQ1xtkmzr-IwPK8Y3WZ4Clj2MJ2uGeEVKLafvoBIZptqDPorktPxD6SAu2Sz4vz6SYuFkJrv-Kd3C-mATzTkxn3k2yIxyARa6EVG4ZxSFZIMYRQcU_jkQ5lsv3oWaEy0INcL9Q8pjMCinMd8EWQ91qS3uAEWKI9uxbT60GJP4WxAyeQaWdQF7dIG0gjeFSbvQ3DS4YhCFUC0xBmMHz-It4fMoSIkvBjszemf5jkRSlmQZ6Av00ZPoRkzVeEIdZvYnVGZzDpB6g7V5W4tflLKWhU2WZsfAacz0m7DFc5PStFjfGi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط حيث وصل سعر برميل النفط الواحد إلى مايقارب 84 دولار.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87271" target="_blank">📅 11:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87269">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8DXnc9Ko55QgsETiXQ96I0GVcuBPK7uH8ByQraOTLNHANcgoTAkEzFSuIxMNTkOckE4r58vAWkUeaAIu_c8vKRFJjm5E0aeLPbpFTpvZh26N9f91uu8-0R6d0kp9NiLCq4Z7dXRjBujCuYKdofJdH2_5Rar3VN4DwS4MUgVRZap-10LkseUeKK35mzRnIXb0Ho8qfZiTQA2yrkQ4t2U_AVBPPDn4fgQnpGDNBNKLty9_db9DeWdHmixftVf-MycL1S6wMDoyKXC9omqOLsk7_xw9_ieQqEDWXjiESBqOiguPmcHTDW0QTznFfKSqGCTSiCXo6nsur8nqE4-51f43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02c3829c.mp4?token=iy7zoTJWTQ0hoCT0D_nPnMuIj9BMRtOUxQq6fro6IDDE556uWYVgUgtAvwWiGfBDJNHquDE6N7lP4vSYBvdOo80pGQ_uIRrtN1Y_FQwAVxgAXf_bJelfUcThCfqcXFoTKsMCLX_CF-yKjz-VtW-tFS2e41A0UQ9cn17ZKQ5m3mmIr5KIUieAQbhzLkaPdbtdxbeD5VO11seJLa8zoIWeo2-hfSLspHjOwFKmxtWzvNCqE1LS-Ea0MVbqypHFHEA-KQmYxI3clfQqOo5jdfPcEXSWBrU9EKBwoezQ6CVYKVKK7lnDagjBaoyczuY33lkslBTO8mDAMvOplFSlfhU9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02c3829c.mp4?token=iy7zoTJWTQ0hoCT0D_nPnMuIj9BMRtOUxQq6fro6IDDE556uWYVgUgtAvwWiGfBDJNHquDE6N7lP4vSYBvdOo80pGQ_uIRrtN1Y_FQwAVxgAXf_bJelfUcThCfqcXFoTKsMCLX_CF-yKjz-VtW-tFS2e41A0UQ9cn17ZKQ5m3mmIr5KIUieAQbhzLkaPdbtdxbeD5VO11seJLa8zoIWeo2-hfSLspHjOwFKmxtWzvNCqE1LS-Ea0MVbqypHFHEA-KQmYxI3clfQqOo5jdfPcEXSWBrU9EKBwoezQ6CVYKVKK7lnDagjBaoyczuY33lkslBTO8mDAMvOplFSlfhU9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇾
انفجار مسيرة على إحدى خزانات مصفاة الزاوية في ليبيا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87269" target="_blank">📅 11:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87268">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇪🇬
🇮🇶
السلطات المصرية تحقق في شبهة تزوير قسائم ودائع مصرفية بقيمة تقارب مليون دولار تقدم بها لواء عراقي سابق مؤكداً أنها تعود لوالده المودعة في بنك القاهرة عام 2002 ؛ حيث تم التحفظ على اللواء ومحامية عراقية رافقته وتمت المباشرة بفحص المستندات والتحقيق في ملابسات الواقعة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87268" target="_blank">📅 10:53 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
