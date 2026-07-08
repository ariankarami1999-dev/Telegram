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
<img src="https://cdn4.telesco.pe/file/BCbA99rckAyKz2GUIxK4n71XL3x2mQYFDupAxHeCekMjFIzYziLS5kITo4WSQrRd0aSKY_Y3kr4i-InYzeFCNN-x_mer4qJ1d4_UpcGREWErMNA5-fvghmWC2oKvX0eB0VCeaG7SckV7N_tVi67TvDKaxfXxORHQwpy6E0WxHGdAYSbguh7NKXoLzt5gSXRQHJzHsX0MWAZ-__vEc0Q1JKOlJ9Lg5fBy8NtJnh8KLA8ZltSWHp1NCeWcZ_osCe_dVe4roiB6xSngN7piXZqAXiuU6rs__ILQvjJ8ShjJhcADycnDKp7A2b7pxmy5Ryy63B1jUTXG25h8cq285G7v7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 341K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 05:22:29</div>
<hr>

<div class="tg-post" id="msg-16803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آلارم حمله موشکی در بحرین فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/withyashar/16803" target="_blank">📅 05:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/withyashar/16802" target="_blank">📅 05:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8524de4243.mp4?token=ilA-RliLRa6eXZWDKnbGMUBXsVGtBJ_bTifLkbG1toPV-nm5eBv46cxdfMks3ZFxsK3kaJ47rTKQn3WbsWuMvN5DyvldcCbRdZGiiDU-gA-4_pdv7GdEGkIvWjdHLjxLDT7lkKhkChiB46UWmJoXv8fof9JzzaRlkhEvETge2pysWXgGa1R4bUuG-qv6Xhj_Z3BLdvffBzyuTqt9Q25J5z89Z5kz7bQQL61obEl7AZJC5-YnmPG-yddf1LkRe47XpFER7veTuHV2kN6toV2CU99ZAm7x2IX6k5Lp_P7zzdhIOqSsVydGwB863sxpQYFoOjPRp6aysgcjXYCy5SEe_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8524de4243.mp4?token=ilA-RliLRa6eXZWDKnbGMUBXsVGtBJ_bTifLkbG1toPV-nm5eBv46cxdfMks3ZFxsK3kaJ47rTKQn3WbsWuMvN5DyvldcCbRdZGiiDU-gA-4_pdv7GdEGkIvWjdHLjxLDT7lkKhkChiB46UWmJoXv8fof9JzzaRlkhEvETge2pysWXgGa1R4bUuG-qv6Xhj_Z3BLdvffBzyuTqt9Q25J5z89Z5kz7bQQL61obEl7AZJC5-YnmPG-yddf1LkRe47XpFER7veTuHV2kN6toV2CU99ZAm7x2IX6k5Lp_P7zzdhIOqSsVydGwB863sxpQYFoOjPRp6aysgcjXYCy5SEe_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله به اسکله ی صیادی بندرکوهستک
@withyashar</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/withyashar/16801" target="_blank">📅 04:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ffa8fddf.mp4?token=qSxSzo5soAD1Rjga20VW8sn9rNPsE-X4fcJw8sHDnlskp4tqml-pT9kGUjq4QJAKrTPhNNlJdUEk8AFPgK8x9FPUzKiknEkn_uO1NmUHVAGACV-lvkciq8NBVYQRhA9UibzmBJFby9uVUe8d5bI2ZL-LYOt5aUX6FlLmh3Vx5kdNOeXkF4H12xtz91hwlKqnXQ9GQzqCT6V_LihbLYpuJQWFbGDObDCYKeA00Lg6QcteMCXDJ3QrriJ7kySP9fdnHPakRrQH8Pnriu5nB8aNelSTcwVlPP-ZK5cE1lUHU4avZIJL_RsreUpd9_4Q81h4C97DTxUu8ENdIf3O851R5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ffa8fddf.mp4?token=qSxSzo5soAD1Rjga20VW8sn9rNPsE-X4fcJw8sHDnlskp4tqml-pT9kGUjq4QJAKrTPhNNlJdUEk8AFPgK8x9FPUzKiknEkn_uO1NmUHVAGACV-lvkciq8NBVYQRhA9UibzmBJFby9uVUe8d5bI2ZL-LYOt5aUX6FlLmh3Vx5kdNOeXkF4H12xtz91hwlKqnXQ9GQzqCT6V_LihbLYpuJQWFbGDObDCYKeA00Lg6QcteMCXDJ3QrriJ7kySP9fdnHPakRrQH8Pnriu5nB8aNelSTcwVlPP-ZK5cE1lUHU4avZIJL_RsreUpd9_4Q81h4C97DTxUu8ENdIf3O851R5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک بالستیک الان بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/withyashar/16800" target="_blank">📅 04:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3d8e2a2.mp4?token=BfB0Bk5fXAs-UOcFDjhgcl7NeWf6OMfOA4QF26mAjwnULKzSR3GFg7OMJTscVJO8CE8K7j-rdllD79ZClwR_eopis-o1wdft8-TZHoJ7pJ-8Z04ATF8oMWp5_lAu5ygeRu-8Xjete2UmpZpBxCL0sln3793U5QUkRRoG4vwZMTjdtZarnsDqprPu3DPeD_zSLvLlcaeJGUvFuIss_HKmRDtWD-A8xEznBFqR37dAPsFSnD29sjVwTjplfPwRCO-9jAc4GP82c57ML9KrfCU3FR0azgdVDnrQBfJ2njVV4XZaTr00G1EH-Pg4xTReCl9lRAK1XpgF2oM4ijjHuNGvbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3d8e2a2.mp4?token=BfB0Bk5fXAs-UOcFDjhgcl7NeWf6OMfOA4QF26mAjwnULKzSR3GFg7OMJTscVJO8CE8K7j-rdllD79ZClwR_eopis-o1wdft8-TZHoJ7pJ-8Z04ATF8oMWp5_lAu5ygeRu-8Xjete2UmpZpBxCL0sln3793U5QUkRRoG4vwZMTjdtZarnsDqprPu3DPeD_zSLvLlcaeJGUvFuIss_HKmRDtWD-A8xEznBFqR37dAPsFSnD29sjVwTjplfPwRCO-9jAc4GP82c57ML9KrfCU3FR0azgdVDnrQBfJ2njVV4XZaTr00G1EH-Pg4xTReCl9lRAK1XpgF2oM4ijjHuNGvbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شلیک موشک از خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/withyashar/16799" target="_blank">📅 04:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴄᴀʟʟ ᴍᴇ Kasra 🎙</strong></div>
<div class="tg-text">بندر امام رفتم سیگار بکشم زدن
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/withyashar/16798" target="_blank">📅 04:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون پرتاب موشک بالستیک از تبریز
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/withyashar/16797" target="_blank">📅 04:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عبور جنگنده‌ها از آسمان شهر بوشهر همین الان
@withyashat</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/withyashar/16796" target="_blank">📅 04:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خوزستان بندر امام همین الان زدن
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/withyashar/16795" target="_blank">📅 04:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eb15d06f.mp4?token=JoPHyxllhp55te31jC13BMt3Qn2ng30n5WzPYDjeItZfeJM_ttMcoHgYNYldx7ifFwgwi6D10-Kapl5DBkq_hYGZNWxF91ApKRowoa6IbXKHVtqCpwyR_YPA66Yh1F_FDNtq6nD-4_vB8_RMRn3yTuxkoAl3sUQ5PM12aGs-cxron4ovG8LLYoOOTUN8cagOwj20rEqvLL7Ea36kL287BuDDi0tOn4_6ZtfvpJEnGBx2AmKahRp15D8dUG342RI3v7x9l4zGRYApqacGYNLomuxNhOrOZXu5ExRLvM324tGy-tl-PWfbMAme-et4GepqhGXuooQ5hnJ7TdxGkhRoeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eb15d06f.mp4?token=JoPHyxllhp55te31jC13BMt3Qn2ng30n5WzPYDjeItZfeJM_ttMcoHgYNYldx7ifFwgwi6D10-Kapl5DBkq_hYGZNWxF91ApKRowoa6IbXKHVtqCpwyR_YPA66Yh1F_FDNtq6nD-4_vB8_RMRn3yTuxkoAl3sUQ5PM12aGs-cxron4ovG8LLYoOOTUN8cagOwj20rEqvLL7Ea36kL287BuDDi0tOn4_6ZtfvpJEnGBx2AmKahRp15D8dUG342RI3v7x9l4zGRYApqacGYNLomuxNhOrOZXu5ExRLvM324tGy-tl-PWfbMAme-et4GepqhGXuooQ5hnJ7TdxGkhRoeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوهستک سیریک الان زخمی هم داشته
@withyashar</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/withyashar/16794" target="_blank">📅 04:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3052fe68.mp4?token=Qf1Pr83j_xoiSQcBpsfNMxTbAj_p5jy4aXhwMB8IyIROXXaOIOX_JHTh05HGMR-85jtU-7QmOdZ-yRYkSgPZRAVO8j8Mg2hTyrTXcXmw59l9Ko1N3w9HZAX8as9fxapvyfpB54D8fFRLx9GiYuS6s7IjP6r75E_G21oa-HOATSN4O9IKceQgYOrJPBrXNImCUwT17EsJt-XV6Eu2Xfl21PM2IAbBJq8_Cv9ObPdbH0FPtw1vprLH5f8_zEiQmMSb1xnOiicA36BDJU5kLflrZxNPq7K_mJg00mzHe1bVJnqs5bjJ7tdOXX_KGl8rlVY6c2wAjxTumk_LEzT50xVP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3052fe68.mp4?token=Qf1Pr83j_xoiSQcBpsfNMxTbAj_p5jy4aXhwMB8IyIROXXaOIOX_JHTh05HGMR-85jtU-7QmOdZ-yRYkSgPZRAVO8j8Mg2hTyrTXcXmw59l9Ko1N3w9HZAX8as9fxapvyfpB54D8fFRLx9GiYuS6s7IjP6r75E_G21oa-HOATSN4O9IKceQgYOrJPBrXNImCUwT17EsJt-XV6Eu2Xfl21PM2IAbBJq8_Cv9ObPdbH0FPtw1vprLH5f8_zEiQmMSb1xnOiicA36BDJU5kLflrZxNPq7K_mJg00mzHe1bVJnqs5bjJ7tdOXX_KGl8rlVY6c2wAjxTumk_LEzT50xVP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله کوهستک ، سیریک الان
@withyashar</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/withyashar/16793" target="_blank">📅 04:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD5elMlr5dR_9rpqLqWnjCIYLzOBd4yqtNWsjR_cvNV9OgxQamwdDbQMaBGCzcsE_lnenzX3hTUhKkR6oz7bVtV_RAYRI0LvRKYErGG9wzqiorOzyO8AUeADcG6clNlS5X0FFNDcxz1jgKlxUmUC4WEMQiogphGqiBr880BX5JK1VUVQnVxLoRaL5WHyRAI8QYnsDrx5eDiVLWqJV6sswTjNX82JKhbukICxNc4-unv9jIgodOjX8--14zWK0hzjCSFjtn0tHmbZkyEF_2JcvvItXrNbY-pV0BE5n6AgnuGzz9hzCcoHiDxYpo81MxyXzn4hdRyH7PQ0jCrPbS1OWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله کوهستک
@withyashar</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/withyashar/16792" target="_blank">📅 04:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گویا از بندر عباس پهپاد گازی ‌ول دادن ، صدای پهپاد شاهد شنیده میشه @withyashar</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/withyashar/16791" target="_blank">📅 04:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شلیک موشک از سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/withyashar/16790" target="_blank">📅 04:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسمیت، خبرنگار ارشد نیویورک تایمز :
یه مقام نظامی آمریکا گفته؛ حملات هوایی علیه ایران فعلاً ادامه داره و قراره تا یه مدتی ادامه پیدا کنه، تمرکز حملات هم روی چندین هدف نظامی ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/withyashar/16789" target="_blank">📅 04:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گویا از بندر عباس پهپاد گازی ‌ول دادن ، صدای پهپاد شاهد شنیده میشه
@withyashar</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/withyashar/16788" target="_blank">📅 04:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسکله کوهستک و پایگاه موشکی کرپان زدن در‌غرب سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/16787" target="_blank">📅 04:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شلیک موشک از سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/withyashar/16786" target="_blank">📅 03:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16785">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قشم و زدن باز الان
@withyashar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/withyashar/16785" target="_blank">📅 03:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16784">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دو انفجار در خورموج بوشهر شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/withyashar/16784" target="_blank">📅 03:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16783">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان بعد از شنیدن خبر حمله، سریع شال و کلاه کرد و فلنگ رو بست تا مجبور نشه با اتوبوس برگرده تهران. هواپیمای مراج وی هم اکنون وارد حریم هوایی ایران شد. @withyashar</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/withyashar/16783" target="_blank">📅 03:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16782">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بوشهر انفجار سمت بندر دیر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/withyashar/16782" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش صدای انفجار بلندی از سمت خارگ ارسالی از بندر گناوه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/withyashar/16781" target="_blank">📅 03:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجار در قشم
@withyashat
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/16780" target="_blank">📅 03:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">موج جدید حملات آمریکا شروع شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/16779" target="_blank">📅 03:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش انفجار بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/16778" target="_blank">📅 03:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من دارم توهم میزنم یا بازم صدا میاد؟</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/16777" target="_blank">📅 03:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommojijen</strong></div>
<div class="tg-text">من دارم توهم میزنم یا بازم صدا میاد؟</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/16776" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سه تا انفجار دیگه بندرعباس
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/16775" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVOOndL0GVFG46KGdiwi3-5ilHGUsRbWQQoTeBRZglA2iK-q4ml2oZP3mTXLteRbLgz00raUx8Ib1jxB3csMmKjHD5BWx1fUNw4At_DL1m84euxB9Oqydn-guoru50XvdamTBKec13YTXo-2ATqPspeh4bu-DRi0Pbj9xqSPEpxkoWCBZUcuUiaQzHkCIJ6QGX5-cr01cO8UYQEe-K1O51TIVDRapw3hlmq5HfefHJ5v9BNeN7NypAK4zSC7-Yr3qAj7pnyTzPzChfhNNuGMrsyNYsZuZDp-Ax3Se2F0c8pWXptbLG4vBcPAGdaNg5qMEp_XQRjMbJl_K4_NrZYVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه انفجار بندر شهید حقانی @withyashar</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/withyashar/16774" target="_blank">📅 03:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیکلاس کریستوف ستون‌نویس نیویورک‌تایمز: به نظر می‌رسد جنگ ترامپ با ایران دوباره در حال ازسرگیری است
علاوه بر حملات هوایی، آمریکا لغو تحریم‌های نفتی علیه ایران را نیز پس گرفته است. این موضوع صرفاً یک نوسان یا اتفاق گذرا نیست، اما دست‌کم برای من هنوز مشخص نیست که آیا ما به سمت یک جنگ تمام‌عیار بازمی‌گردیم یا وارد سایه‌ای تیره‌تر از منطقه خاکستریِ میان جنگ و صلح خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/16773" target="_blank">📅 03:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">لحظه سقوط هواپیما باری پاکستان @withyashar</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/withyashar/16772" target="_blank">📅 03:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=rNi3ouoByEHYcxOSq_5Cssseyi0cMAlgQX5fNLWkENVaGeB9ZNUVR3NCKqn2xeaL_9a0tlnp4w4HDV0sXlHDeaDcryfiDE4YIyh2RoI1duh9lcMawB2WH99Lvl1wVqaDLvMwpfCfzodVYd6hVuFWMuWCnRd-XUoXKV3KHX4kNtkBikikH6hTtArE9hKR6Eep-bgV-n5Re6n0hkM6vaTrPAO_8Y5B1QmQiInSkNIdDoyd-JgY6fN211sNyOt1PAsZ5wmNQhzLZhU1dV_kZdo28D5RKicxOMCXvYzITZHCM3VJUf0vSPRep032iOb9feKEOUYdeaWaq5UnerZOq-kgyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=rNi3ouoByEHYcxOSq_5Cssseyi0cMAlgQX5fNLWkENVaGeB9ZNUVR3NCKqn2xeaL_9a0tlnp4w4HDV0sXlHDeaDcryfiDE4YIyh2RoI1duh9lcMawB2WH99Lvl1wVqaDLvMwpfCfzodVYd6hVuFWMuWCnRd-XUoXKV3KHX4kNtkBikikH6hTtArE9hKR6Eep-bgV-n5Re6n0hkM6vaTrPAO_8Y5B1QmQiInSkNIdDoyd-JgY6fN211sNyOt1PAsZ5wmNQhzLZhU1dV_kZdo28D5RKicxOMCXvYzITZHCM3VJUf0vSPRep032iOb9feKEOUYdeaWaq5UnerZOq-kgyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این این این تحلیل ممباقر‌ الان میچسبه
@withyashar
🤣
✌🏾</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/16770" target="_blank">📅 03:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
طی ساعات آتی احتمال شعله‌ور شون جنگ بزرگ وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/withyashar/16769" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/withyashar/16768" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/16767" target="_blank">📅 02:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMf78tnfnByV_QB4n5oL4ediMntVuds8LjmqKjp7Xt-t_dRJonFM_IMTsv5rVLTNS6Ik4fcz8eOmHbdp6VxOwxIrDX4C9R7JTRnoSOdTbp4GG9nr9ZwsrJdbpOSJNDYdHR2gcF5nmJo9crITEgmbErjDmOy4u2tq9x3f17ogOnH6AGuzVxob39p9EGLvUtGAbI32Jb_mfWWfoWArGsBhdbL4uZ5L3vYAdNH8qe2MqFzW2w3ZOdh0D-nIK4SYJNGui7qEkSpVqkmvh1tGMfFkIkpOxx8CEcwCE4f42BmPyhFY8De3bXer5CiyfcVF6bLiqyf1GPzzGR6RMRq5HAKMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این صحنه هم باید تو تاریخ ثبت بشه ! کالکشن تمام هواپیما های آمریکا یکجا
🤣
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/16766" target="_blank">📅 02:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiSOakPv4IOVXo9_wmLoEDIpn3m4bZE0-axdEfxkr8SvHH4K--siNpvYamX18JWSoRh0qge_xYrd3LhE2fnPJl0gKVaQ-0IolagAmkwJAeb-QmdFHf-VJnTSGJL-sLybULZCd2HDihdV13-A3DftwvLo83ghUlD9qykP56jSVQVyMcKA0BwvDBEKDzcxSiY_27BbwWnm4nqQGZhTi7zkHdi5qfXgt8JLU0WnObvkHKvhCcqxlRM43qSkwlzhKp9zhAHiEKb5xrO7vuVsOBQlVXzr7q5zrxMo2fjHzdT4Y_3xGEWbq3ymDk7_mIAKhaYIwERmOsTickrB5FvZwRZYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بعد از شنیدن خبر حمله، سریع شال و کلاه کرد و فلنگ رو بست تا مجبور نشه با اتوبوس برگرده تهران. هواپیمای مراج وی هم اکنون وارد حریم هوایی ایران شد.
@withyashar</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/withyashar/16765" target="_blank">📅 02:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اتاق جنگ با یاشار : ایران و آمریکا رفتن فینال لیگ خلیج فارس برای تصاحب تنگه طلایی
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/16764" target="_blank">📅 02:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قشم ، حاوی الفاظ رکیک
🔞
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/16763" target="_blank">📅 02:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/16762" target="_blank">📅 02:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKU7WhVvO_8O1WWTsY1gIl2mrG7LaiXKLnlR-KLxmxpBw8BovcD86kYR55lQdE4varFr_2PghIQpPf4JsPdF3RMzBO5YKJJHjxqL__KjZ4dTwskZj71nye591Nw-a2YLLwuaWwttmZ51CpoF6DonuPRSp6OnX_jZjGiaIsAcAKG-z9UF5jHtIfJmTw3uk_y4n0-skvPMhR8nPQ5fkJSUAhgsMg4-g9XAL84sdaUh7Jvd7SOjYHCa62QIDhiauOU9taUqXJy1n1pfWkijdCJ_RB5lImsQek047RHWGY1egv-hc6tcKDcd2eV3J3RgDGt2OSnKFErh5eUvL293TYlWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد @withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/16761" target="_blank">📅 02:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/16760" target="_blank">📅 02:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسرائیل قشنگ داره لبنان رو می‌کوبه تا جمهوری اسلامی جواب بده، اونم بیاد ملحق شه
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/16759" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوباره از اصفهان جنگنده بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/16758" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الان وقت مسخره بازی نیست !</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/16757" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری‌ های رژیم : چیزی‌نیست بازار ماهی فروش ها و چنتا کشتی ماهیگیری رو زدن
@withyashar
😳
🤣</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16756" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منابع غربی : حضور ترامپ در ترکیه خطری نخواهد داشت زیرا آنها متقابلا میدانند مراسم تشییع  خامنه‌ای به حاشیه و اختلال کشیده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16755" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدای جنگنده در ‌آسمان بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16754" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بندر عباسسسس دوباره االان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16753" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKEqOv_luT39Njfd7POGCvVAWLCOAKx-96_B8ZARkJ5g8fsctNFnWxe9TCys7LeDEjUE8PX1FIXRxb1MPWnXMHxbNT1Fmi0K_rS9T1SP7P3rkK6_WAsGaMmHzfExYzktlGFZ4146AgCwCixLfjZuNcoZrIAWE2wjRaNpJVqkGWdIqz4IMEoMQ4GE5f5XyxSV7nz2QSFoDGuawIzG_hDTcqo47qM3vFcR9DqkQbFfRbRa_Z5Dirs_Csqj6ar_8NzyZUzmJMnyv0Mi7ndD2CPgVpJ7E5GCTPk2BTY5cWn6OZZk7jZCm411h4Lf-2R-nytXyY9k7K-2wuBRXRl4x7sZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان دوباره زدن
@withyashar
حملات ادامه دارد..</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/16752" target="_blank">📅 02:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش از بسته شدن تنگه هرمز @withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16751" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مقام آمریکایی : حملات  امشب ۵ برابر بزرگتر از ۱۰ روز پیش است
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/16750" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش از بسته شدن تنگه هرمز
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/16749" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوبار سیریک رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16748" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c9f2899.mp4?token=ILLaUCkX28xMqkYUt_p_0rv71N3jWgnU7rrt84rLnlar25aUA4aR2IXPAvfjQWqbTyeElqdKco_lRuRdUB2NUNp3taxWPjqkXMvE9u0OTk6pUnqf71GBgKPH1yUA89SHdPng4vui6q723UxsypU3ZaBeqSJsQnKKnoQ2Kkd48hJZZCOa-mTcPHtZDeYhIlogSNzEQBoowaSRrnZ-hl7Ocvv4AAewT4FYyu4QXVU9ryayVy_L6oRUm9xT4Yw8xbAgFFIrLv3ZpPcyg53E2TDlat5dJMNubN692x5N7aP4n_SLsWch3V90_hL3hh8mMr7Sw9BBqeQ-C4E3Xn43aOrmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c9f2899.mp4?token=ILLaUCkX28xMqkYUt_p_0rv71N3jWgnU7rrt84rLnlar25aUA4aR2IXPAvfjQWqbTyeElqdKco_lRuRdUB2NUNp3taxWPjqkXMvE9u0OTk6pUnqf71GBgKPH1yUA89SHdPng4vui6q723UxsypU3ZaBeqSJsQnKKnoQ2Kkd48hJZZCOa-mTcPHtZDeYhIlogSNzEQBoowaSRrnZ-hl7Ocvv4AAewT4FYyu4QXVU9ryayVy_L6oRUm9xT4Yw8xbAgFFIrLv3ZpPcyg53E2TDlat5dJMNubN692x5N7aP4n_SLsWch3V90_hL3hh8mMr7Sw9BBqeQ-C4E3Xn43aOrmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم ، حاوی الفاظ رکیک
🔞
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/16747" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ناصری،عضو مجلس : دقایقی دیگه موج جدید و بی پایان حملات سپاه آغاز میشه این بار شدیدتر و ویرانگر تر.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16746" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کویت و بحرین دچار قطعی سراسری برق شدند!
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/16745" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9748bcf07b.mp4?token=FuKiHAh085G9nkuiMMqdYuRXJHl1VayAruexYfb0ys3sG3g8_qyniWHLWdnTYiZzUbWhlpd9Wwa1cLYwqJ_5hJUNUMtfrg4Uv8y8yfhpxmr6e5mqSwsKebEWEmXxsIONEllwmY7noX1u95a17cxeIpHIwx4odmXMSDa6p4OiWSUBqhLUDEA4CzEbOM5JaiEgzi5-609b4DW2znTwv84IIgTJGuZ0sneSGmIBhf47htW6dmYCCx7ykOQQu5YBFawCy8Ow4cFto4U6mCyRvWtVNn--X8W1cCEdF2DG6R7L1h12QOX3daVQ10AKCjKiNUjE316HYfr9D7QVvY3SLN0_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9748bcf07b.mp4?token=FuKiHAh085G9nkuiMMqdYuRXJHl1VayAruexYfb0ys3sG3g8_qyniWHLWdnTYiZzUbWhlpd9Wwa1cLYwqJ_5hJUNUMtfrg4Uv8y8yfhpxmr6e5mqSwsKebEWEmXxsIONEllwmY7noX1u95a17cxeIpHIwx4odmXMSDa6p4OiWSUBqhLUDEA4CzEbOM5JaiEgzi5-609b4DW2znTwv84IIgTJGuZ0sneSGmIBhf47htW6dmYCCx7ykOQQu5YBFawCy8Ow4cFto4U6mCyRvWtVNn--X8W1cCEdF2DG6R7L1h12QOX3daVQ10AKCjKiNUjE316HYfr9D7QVvY3SLN0_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار ها در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/16744" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwUohaVqrHEVNt2EmUSsk-MlFdm1r5flb5SWsysWYBiBPiNo3YOJeth2fTwEXYu7t2rq3cZ_I6xLmqipKcDXg2_pJ9F624fY69CMslSkliXrKvTQavX4rad3uQIcE0sgqYoLC21sr49L5SeS02xJ-ImTikvD4IYdioxw7BxstpjB42_MGlc1RuN0lj1Pc1_1E8hlM5oStf0yNjhtvrjSZdxZaTtdThqR5AkI4rJ0Ys79Fx3DChP5cBioKplsP111oXlKrH3twp2yHCrh1N43C8tZzNnd-FEi9B3HBy3miE7dERB2x5yKizW6E6CgZwF1sYZZa9vZKZ5FWZUYb5Dbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان سرخ بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16743" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دستگاه های اخلال گر GPS در سراسر خلیج فارس و تنگه هرمز فعال شدند  حتی تا کیش‌ کاملا در سیگنال قرمز فرورفته @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/16742" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/16741" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری بین المللی وابسته به سپاه:
پرسنل نیروی دریایی سپاه دستورالعمل‌های اولیه را دریافت کرده‌اند تا از تردد تمامی کشتی ها از تنگه هرمز تا اطلاع ثانوی جلوگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/16740" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAW2QHkYgAHv0BEE4XpJQ7Sf6Tg5aEWUvEIegRTnk1_jtnKrNeHWck28Bg13rhjmcTj08ZfgGlEDECRawaF-8YJJ1XhO37srVk0i4Pk3dAyMQpXXHYplIypBEy1P3qbwZuIR_6T31GVGoo3odtU6Pyqwj3sfXpDjN43bLbNR6521yw_phEKw6kBGk1OIG2thMr1vI18QKX0EC3cXI3Aq6RbnDjZ8JHsOPVRUyz0aWl0z3D_iniErnsCpHuyQfAkNJY-NkHehdBEvlUf4hxMEiwYp6PXKAfuPaFFOlHB2H39wGdgltzyKaDX_A-XCfH9HVlqVqyzygvrzgNGSa7tgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/16739" target="_blank">📅 01:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سی‌ان ان : شدیدترین تبادل آتش از زمان آتش‌بس!  هم‌زمان با دور تازه حملات آمریکا، ایران کویت و بحرین را هدف قرار داد. یکی از شدیدترین تبادل‌های آتش از زمان آغاز آتش‌بس در شرایطی رخ داده که مذاکرات همچنان شکننده و ناپایدار توصیف می‌شود. ۹۴ روز بن‌بست؛ تنگه هرمز…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/16738" target="_blank">📅 01:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام آمریکایی به سی ان ان :
حملات هوایی امشب آمریکا به ایران مجازات آنها است، نه متناسب با کار آنها
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/16737" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56eee461b5.mp4?token=PczE4c08HrLo2umptJFay6SfMasGY7qnTmBuvDJlEDdE3DTz8PLR6LIjZncgGxovpk9Q65wwM5AKes50XM3mTv4ROBXfOdS_6MbHiDMd4ZWvDE-WDh6JN0XdjeVRABZbpktkb8Rv72H9f-QE6VOYJRcbXuzcLX35UJ-7Y7ZLJsgtJSM16aS8IVL8eWvu9RxmSMKJseb48mLV0O9mfQizsW-dDlcjEExYF1LOzVE3dEMRjlvLbSAPac3Tfy0eut3bjGCC3sSbmHj5dzYJDLQoltMD0Tc31wew2kwnjGKHqaFDPURzZXUP8cz-3bIzJoV6BUXiekJ_LO4i91aQDYNmrheSj5IBeuFuZdQR_Ow6hQyeHgSuFC82baNTaFtCkWPMSCcBlYBDENT72nPlTgjCxuxJBxVoAyRavgoDrohb__PA04-HZGIdnLMTOBt86VMftWdjo6S_PN0VW9Zu2V9NP8kL42_zbahcq4fOsvh6RU9m1bbubtxkrIMYT0RE6N7tftQwmkgHT28-FqN-8ypx37ajunMskk0NFKp38Llq4IUMVxUqrdPgzmN67fDBhrSn6dbguJZh1pF8Ma4KSu4QPQn_qWbHuWuAdKqcfXazdhnqChGVfCTZkSrBtOIpWTDMNcnAA0UreLFsxOljTciOeXtMJgVEmXDFOfA3TghScF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56eee461b5.mp4?token=PczE4c08HrLo2umptJFay6SfMasGY7qnTmBuvDJlEDdE3DTz8PLR6LIjZncgGxovpk9Q65wwM5AKes50XM3mTv4ROBXfOdS_6MbHiDMd4ZWvDE-WDh6JN0XdjeVRABZbpktkb8Rv72H9f-QE6VOYJRcbXuzcLX35UJ-7Y7ZLJsgtJSM16aS8IVL8eWvu9RxmSMKJseb48mLV0O9mfQizsW-dDlcjEExYF1LOzVE3dEMRjlvLbSAPac3Tfy0eut3bjGCC3sSbmHj5dzYJDLQoltMD0Tc31wew2kwnjGKHqaFDPURzZXUP8cz-3bIzJoV6BUXiekJ_LO4i91aQDYNmrheSj5IBeuFuZdQR_Ow6hQyeHgSuFC82baNTaFtCkWPMSCcBlYBDENT72nPlTgjCxuxJBxVoAyRavgoDrohb__PA04-HZGIdnLMTOBt86VMftWdjo6S_PN0VW9Zu2V9NP8kL42_zbahcq4fOsvh6RU9m1bbubtxkrIMYT0RE6N7tftQwmkgHT28-FqN-8ypx37ajunMskk0NFKp38Llq4IUMVxUqrdPgzmN67fDBhrSn6dbguJZh1pF8Ma4KSu4QPQn_qWbHuWuAdKqcfXazdhnqChGVfCTZkSrBtOIpWTDMNcnAA0UreLFsxOljTciOeXtMJgVEmXDFOfA3TghScF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آغاز حمله
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/16736" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش ترور هدفمند در بندرعباس @withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/16735" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmtTz6Hx7zof_ZOfHX1rWcf-qVU_qLS8FU_0Hbh4_Ixzu6mCdNK1T64h6LVA6HNaj_pjOdqfxIt0ylEO0JWAOQsL8fAg0N43DgcvcCVtve1WqSnQPCpR-DM7uf4NFx-jQOeLP4f17nGPwoGPKkDvA0XrgyaJimx1B_FY6bCr_moyZ6ZNWRkftFu-IJPWkG3V3ljBzxvESJU5TgFl0kwivyb0IPJrNMWq8Kp7DUKb770-qfx2i5FO3E-V_hLvWx6gLjYuKb5NfdmvhQyRFrVKisJiCXEReIVdukMHp415Dcp2QnYv37iI2iqccS81G-IgAaYjMorOqK87OKjK4ImXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/16734" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDpozonp5eXl6DsETY6RjtVeoQQdsgAaB43tPRf2GZlrrqGtEPz0FVcn2W9rD62wEkbbFNkbpACbZpXDvJDE_NtWqiGFlV2L24aDugCj8ElzAzQFyOqTWdrzk4usczuG8MSap6F1wM2NsUKRjKoKzq37hV0rUD5rjJUo2WJdHlR4QoXOl7ezrwh-FvyoV4ImRzn5riJpgylZP0FgPmJcMhZn44wTeB_2izeID8ZVO-TdCkunTl--MVoyNIYfCYKsyAYT06p5JjNw8VaUooJii-3_AXMrzBJ8vJRGiKmTUOAyLw7KPxdh0YnazukkEoHr8JLgJRmRh_2iFC-4ysjm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش ترور هدفمند در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/16733" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgDR7m5IvdqauN5uvjo1b-jZsS7pZhXrAF-nNPn-oyYAVt0JuBqur8RaI7Cyr_cRSpCsw0lReUv19n1a-BI7xOksYJ29SYrgElGpOScQG5488QeqvAfBIqUIT7tJIi42PC8Zu2gHRtTSHwxCt9htRfOx3tjkY1zsY-ERg8JHBDcOgwqxfe3BmF-d2CUY6d8Wa-URD988GHwMWg-8rcgvgd64uW63wgLbx79lUUJh53eAsgtNHSb8uRez9lXzhOvqpc0ifXtcvPUl8DWq5Kt9vbf67TOP7nYOZ625EK6AwXwrcnL8kWkzhiVnPYnythRDar5PuQy4K34jafxYK7gCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/16732" target="_blank">📅 01:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496c7aa925.mp4?token=vkL8BlAF25LtqCiJosBtdusscMpVxPCdFLbLL5u2FR0LH-nfpKxPNbFi0FUWAwz1mrAsfYMhJRxrBcWGhW20Y-0yUCXf49AlsCB2O1-OgoryrsiQeQVe30EqQ_ELQYwMenI6i5Qqa1EXJfNx89ImhRLl2Tewz2IrV2x87D8KQcBH7FIlGyTnSfGFSe152xOAQklJTi1zZ0KoP8scxMcbD6tDukZQnGrrMvJhMsPZm90SuunLvoNszIYaJdiJwTL-S9tfS7UxSNIzxH0GWwc3XvuIGaxikIpeUacVjmgkr0AkEiJ2u4R_U39KgIXc_4uIn1z6m6T7ZB1v6RVSFbWa3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496c7aa925.mp4?token=vkL8BlAF25LtqCiJosBtdusscMpVxPCdFLbLL5u2FR0LH-nfpKxPNbFi0FUWAwz1mrAsfYMhJRxrBcWGhW20Y-0yUCXf49AlsCB2O1-OgoryrsiQeQVe30EqQ_ELQYwMenI6i5Qqa1EXJfNx89ImhRLl2Tewz2IrV2x87D8KQcBH7FIlGyTnSfGFSe152xOAQklJTi1zZ0KoP8scxMcbD6tDukZQnGrrMvJhMsPZm90SuunLvoNszIYaJdiJwTL-S9tfS7UxSNIzxH0GWwc3XvuIGaxikIpeUacVjmgkr0AkEiJ2u4R_U39KgIXc_4uIn1z6m6T7ZB1v6RVSFbWa3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار بندر شهید حقانی
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/16731" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28bfa928a.mp4?token=NZSLgRueSRY_K7hw8Ptty55udU8OIhUm0A1FRZdRVSodmJ04J84eTc_ax7ByZrRltUzkLDbiS-URVAw6RJ7mr6Wcsuz1b3sTz89iclf426gVDj6yEjPM0VTDrf29WtzzKtdJT9JIjtdFWrwfbF7MSccPxvGj6v-cBpWFy6X_ug3nzwCWCPjIu22l0Orz0OlPErzD3YL3veJpyL1lr9EYRKK_2Ohe48YqgQ5ccVy1Kqa_5ZF3Z0CWWf0a4xchx_9fZqtWrMKtpqxjGMJU3L2024giaNMT8iPeoboV1_KXBRZngRYDi4OFHZSs3IkT8owpOFjuSWP_oh3pLIFVSw_u9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28bfa928a.mp4?token=NZSLgRueSRY_K7hw8Ptty55udU8OIhUm0A1FRZdRVSodmJ04J84eTc_ax7ByZrRltUzkLDbiS-URVAw6RJ7mr6Wcsuz1b3sTz89iclf426gVDj6yEjPM0VTDrf29WtzzKtdJT9JIjtdFWrwfbF7MSccPxvGj6v-cBpWFy6X_ug3nzwCWCPjIu22l0Orz0OlPErzD3YL3veJpyL1lr9EYRKK_2Ohe48YqgQ5ccVy1Kqa_5ZF3Z0CWWf0a4xchx_9fZqtWrMKtpqxjGMJU3L2024giaNMT8iPeoboV1_KXBRZngRYDi4OFHZSs3IkT8owpOFjuSWP_oh3pLIFVSw_u9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون
بندر شهید حقانی
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/16730" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da252b259.mp4?token=uXElUErpvC_HKgvE_jv3Vcnpg7gh1HJYt7iFmbUZSRcfaV25t8Uu6EN9y-XcqBRVFDTi38WxU78wtBsOt_AHpbh6lXCAEUiB5flyzjrlUHy-bCEJqODAVhAGnkXPKE_MGT86QUX4C7HUgPzpHxfuTRYUX5Hp2ZVWDyI_3wrrdRuCzCVlb21xy6JkIyhbQO_Q4SafoJMxP5euK4ZdvyPAxsiZc4i1WrEJtnFzr0tgOgVRnixVA5uwMw9-xQI_470OQxZgwmsV_Uh_ozCwxjmApPYK5uC1DGhvaAVWj4py8qcM4wd5NmAQ1LelT_Px6tu_QgMmyHn66iCiDf5ysJmovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da252b259.mp4?token=uXElUErpvC_HKgvE_jv3Vcnpg7gh1HJYt7iFmbUZSRcfaV25t8Uu6EN9y-XcqBRVFDTi38WxU78wtBsOt_AHpbh6lXCAEUiB5flyzjrlUHy-bCEJqODAVhAGnkXPKE_MGT86QUX4C7HUgPzpHxfuTRYUX5Hp2ZVWDyI_3wrrdRuCzCVlb21xy6JkIyhbQO_Q4SafoJMxP5euK4ZdvyPAxsiZc4i1WrEJtnFzr0tgOgVRnixVA5uwMw9-xQI_470OQxZgwmsV_Uh_ozCwxjmApPYK5uC1DGhvaAVWj4py8qcM4wd5NmAQ1LelT_Px6tu_QgMmyHn66iCiDf5ysJmovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/16729" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda8d61e99.mp4?token=rhR1C_RB0nRqsGaubgGm3cn_cf0YCVyLck9O0xfd5qdpArZP3EE5Zg0cfbIQW_EToYT1IRwr02pdUu1uGEAKI33H9g0jk0RQjeQ6lXvM0nOSWB2YY4dg9_bY8dI7wngk9uZWQ0G6CpS2eS0saaVeMAWAbdsgDh_cqbqU3Y0FW2XMF5m0L9SsVUWmntsrQglaANIFbx1FJ9mlz8B7OpOhGmsuQzhcHzRnErTfi18pA5_5Jk__msXBH70rzsgPm2b5cG05BaMpRgG0CIyLHWdt0SMvwJpbjPVakJfMyVGxm3RWIWwfVaoxKc_Sdjj3KtyXTF5LqErHlbwO78cbvQl9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda8d61e99.mp4?token=rhR1C_RB0nRqsGaubgGm3cn_cf0YCVyLck9O0xfd5qdpArZP3EE5Zg0cfbIQW_EToYT1IRwr02pdUu1uGEAKI33H9g0jk0RQjeQ6lXvM0nOSWB2YY4dg9_bY8dI7wngk9uZWQ0G6CpS2eS0saaVeMAWAbdsgDh_cqbqU3Y0FW2XMF5m0L9SsVUWmntsrQglaANIFbx1FJ9mlz8B7OpOhGmsuQzhcHzRnErTfi18pA5_5Jk__msXBH70rzsgPm2b5cG05BaMpRgG0CIyLHWdt0SMvwJpbjPVakJfMyVGxm3RWIWwfVaoxKc_Sdjj3KtyXTF5LqErHlbwO78cbvQl9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بندر
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/16728" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/16727" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16726" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رسانه های داخلی میگن سپاه قصد داره همین امشب پاسخ بده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16725" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0RVVyKIVEmzZW_EPOxhJ0mLTI1ogycz-Q6ntWZzljqOs9Eqo6fguPDz0QOa9t895SZVt5ISK85f7lytpvEf8VhhNiyNrgT6_no7HBkTqqPn59ybypOIA-wuGLmIJYiBTCCmjCd_99THUiTHngZxajHmciaouZaX9BCcsujoMIKtCSaFFbsHCBV2718gH0RhqwJ5nDwfVoD0fS75DNGAtIYooE9RLYAxF_RexddZbUruiuhOfpKPgUKHjzAvXuyM-zElQLBsLR8dRVVhJ0elA1mShgI0Y5Avwinj5XtAQaOgd-IheQPDd_j6pGrFPoI2uu2FGExzEtNkR_MlI45u4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه انفجار سیریک
😳
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16724" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/16723" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش ها از حملات هوایی به قایق های تندرو نیروی دریایی سپاه در اسکله بندر سیریک.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16722" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiIDVtQdNTKnxfzESNc_ApQAZSXsSYlEk1Q-PB-6-2miuSfuMdo6ycMnaLfQM2gOhYgGSshU-oJGC5ClczLeQjjuJPXwb2UwaYbBeaMfhLaWu9iNfERVhnAKxRDR4dv1H33RCv3if9MpQ1t8fpZodNcKHPvaTmKvnM1HiqzdBO0fI8TAsiTiyWqwTecacM4cgZ2UUiJM89FZAUvEjzdUlUVTlY2Snf_T-iwrG9rz0CAgNbScopMlnkUuTaY2yQvOwrtt7CfVkR2hVonfwkm1zy8qYGtAEML60oifSzFFJOEYGprYsPEyPZQHCDvNFrdI6zV32XS_eVOdV5gxUoGC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مهیب در
اسکله سپاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16721" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار دیگر در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16720" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHo2GCDW58CLWN0bcRhaxuvutx0eSqoLsEkSmBtrDdC42CTfQrbvcnMZkGT0_meGqf5K-Fz1OO5TKPV4qytNrzICgVhF8Llm4xMku6E3ejN94FeZeeYk05F9PfB4HL5TylihuOvbw1V8lkgaaM74aawGctR9n6vHz8nkOSUcdk5oPZ-LRGYH8aid2vZWEZaJn-GEEjtdI_Dwf3R4U3fuuh8Rqq5bhXbDw-rzpq6043CNvjqZAWz-9SjYRoDNkFK_zgh1t_dx_gXwcwnQnM2heK8LvSWeMsLWM-e7n4RJQ4-yYyVspkUlFrAVt5tTeD__qb72ocjkoMwUbDCfnb3mKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس هم اکنون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16719" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روشن شدن آسمان به علت انفجارها در پایگاه هوایی بندرعباس.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16718" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پرواز جنگنده های شیفت آلرت نیروی هوایی ارتش از اصفهان به سمت جنوب
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16717" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idLGvhhMl6VPTJng1M_iCnO2RbpbhYbdWbv5mVGhkhXzy44iDOW06IbE8zQ2lWkmRFeu93U7Cm9IbyBFL1Go4SNsSlO5DTU1dL0IP_EkxbXhO7iUPoP9AWXVDlMKRytQCFa5-uspjJjul_3tUP1Wywtr9QGIytQEByvc_bS1y7QL1uCMwkETna12IYeMYYOaDdW-7bmsTdOrtgBff5cyxgqqxMECJCgx2SIsjfqR_1DzlEd8h7L7YdV_bNeW8f3SJyI2dVP_i5uZ5Vma48E6_djAiTW63zwbIFlmk06rT09y1C1USOKTZFb6NztIDJ02uNuI51JbFdr1aDs7_Zpmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون اسکله سیریک
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16716" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فرودگاه بندرعباس که روز گذشته پس از چند ماه شروع به کار کرد، دقایقی پیش مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16715" target="_blank">📅 00:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارهای جدیدی در نزدیکی جزیره قشم گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16714" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارهای بندر عباس به قدری شدید است که پیامهای بسیار زیادی از شهرهای اطراف دریافت میکنم که این موضوع را تأکید‌ و تایید میکنند.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16713" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">همین الان بندرعباس رو 6 تا صدای انفجار بلند فجیح اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16712" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یاشار بندرعباس 11 انفجار رادار های دریایی اسکله رجاییی
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16711" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سنتکام:نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنن
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16710" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16709" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سامانه های پدافندی در بندرعباس فعال شدند.
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16708" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16707" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری اینتل : هشت بمب به یک پایگاه دریایی متعلق به سپاه پاسداران انقلاب اسلامی در سیریک اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16706" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16705">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هم زمان حملات هوایی اسرائیل به جنوب لبنان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16705" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16704">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صدا و سیما: برخی منابع خبری از شنیده شدن صدای چند انفجار طی دقایق اخیر از محدوده قشم و بندرعباس خبر می دهند.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16704" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16703">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجار در جزیره‌ی هنگام
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16703" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
