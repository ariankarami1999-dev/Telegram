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
<img src="https://cdn4.telesco.pe/file/t3KQqeGcR1_NBhvsWyql0PxRp4R6cuLImz-ePVi3w5nAE6lI0HTwIzLtLF_xmnkYU_BKmCQv87m9cjyrrGBecsx4f7ZZ1xVEbtjMOEo8QmKbnHCKmAV-DxyR6hnKLGCnhg_F6Fz45jC1LIhjTa0mPdqE96nW64kdmmfWimTLvK5DYvZK2pe2yppFGKxOkSSJRGx_P5usGmfeMejkRYhWAJH9nlCMoO39sxsQrTOoQsvXl_q62ZYqa_AU8XIUe8E5HwzSxQC8EaXd65XErPIxoRnoqVYSvBq5h6SQo_xAv6sKtDwhwliZU9QvSWfATF2sXboDBNixC14FErCt8seHhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-129711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981bb19642.mp4?token=PW6wImi3ytsoDQE0pvVVM4F_MeL0ekfKFuEtCvmnDPNAUyP4O3oAEic_jGHhRxvvqsmD85ZP2gTNp6EpboyEBD4IQxk3RXPyrhywXEG4kA7y3DzXeDwMHoHxGT4bfOvQsYXKbsi6a_Ba41I-9sPLuSx5fs1EaALWX-GbP22ZDsCb-Uc3PihalNayJbhlzpOiTHBsLmBCy5gHVaN9tMc_HHvsEx_TsP6h5Msr0s2IBl93h2qa6CDrIP2sggDfe5HjcFMHN2bPYnCqnbUstB8hwpjiBIFcmpLRyJ8ackMZKbwUL6wI3FOJ6Rl1kznbHMdSoljs4zdvckahHyUHRzQdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981bb19642.mp4?token=PW6wImi3ytsoDQE0pvVVM4F_MeL0ekfKFuEtCvmnDPNAUyP4O3oAEic_jGHhRxvvqsmD85ZP2gTNp6EpboyEBD4IQxk3RXPyrhywXEG4kA7y3DzXeDwMHoHxGT4bfOvQsYXKbsi6a_Ba41I-9sPLuSx5fs1EaALWX-GbP22ZDsCb-Uc3PihalNayJbhlzpOiTHBsLmBCy5gHVaN9tMc_HHvsEx_TsP6h5Msr0s2IBl93h2qa6CDrIP2sggDfe5HjcFMHN2bPYnCqnbUstB8hwpjiBIFcmpLRyJ8ackMZKbwUL6wI3FOJ6Rl1kznbHMdSoljs4zdvckahHyUHRzQdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از عجایب ایرانی‌های خارج از کشور همین که لحظاتی قبل گل میگفتن بیشرف، بعد که گل شد خوشحالی کردن، بعد که آفساید شد هم خوشحالی کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/129711" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=q_JutGAwNbM5eUZjM42cArbEPW8Yg8vTQLZPXjzVnhwRmxv_1E6nCzspetP-Dxl02pWahMr4JyPtcm1x-2qFkbm_gLDGJj_0ldMqf6LSLI0jkUd1GhGpJ_3RvoK_NqipZhFRnQ-RSxtOlhgjBTq93Il8Q09WF2RyoUwlls-_5tprTO9sjC7sd4Oj8-CkhtBwKvp01tOvj_DmUPFxMAa7pdewVeQUhFkgO_5TRrV55gybl7Z0iWP2OBXvbn61TcdLrgPkhph5wMciTH9gI0FChGjjIUnLW18aBcUc6wFFkV3-YBuGjKwKQGoEg1IW8QkOCbEmVAPWhPfaMVcnTnUAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=q_JutGAwNbM5eUZjM42cArbEPW8Yg8vTQLZPXjzVnhwRmxv_1E6nCzspetP-Dxl02pWahMr4JyPtcm1x-2qFkbm_gLDGJj_0ldMqf6LSLI0jkUd1GhGpJ_3RvoK_NqipZhFRnQ-RSxtOlhgjBTq93Il8Q09WF2RyoUwlls-_5tprTO9sjC7sd4Oj8-CkhtBwKvp01tOvj_DmUPFxMAa7pdewVeQUhFkgO_5TRrV55gybl7Z0iWP2OBXvbn61TcdLrgPkhph5wMciTH9gI0FChGjjIUnLW18aBcUc6wFFkV3-YBuGjKwKQGoEg1IW8QkOCbEmVAPWhPfaMVcnTnUAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که بلژیکی‌ها برا بیرو ساختن
@AloSport</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/129710" target="_blank">📅 16:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
جی دی ونس: این توافقی نیست که ایالات متحده آن را به منطقه تحمیل کند، این توافقی است که منطقه با ناامیدی، از ایالات متحده خواسته است تا آن را اجرا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/129709" target="_blank">📅 16:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BypDjd9M-xXak6qbnF55JmvvZKkje1_3wCgUYT3DSaBhdGgaBy_kiW8JZylL1YeWxE9TFo3enIJO0lx7j4ij9Bam7jSA-YwaV1NFs49n72dp5TWuLLOf2oxAo5-VGFP7xLg08O7ANAXNDAMiIOPergGTxgLpalrmoGpYmwMYvuMW-rVOnio5KXIBlQaFip89qzERVCvl_6EUowdoKwToRf69Frx1pEHKlVOoa4TOL8n0s9LvhHS2l4De2jmLBu5D9RKJg8tp7UxqgLilybn8QKxGZdX9ajeDmC7i6V2ouSGp46kZz3n1vjXQm-262TxhwZZJquzISo7q7kPtA2y5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله ثابتی به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129708" target="_blank">📅 16:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=DOjLgj5KAK7pKaw5kqQ6lJQF2CjNzzZf8ON4qhLtjwUMFRBVS5HbXWNMHuWJ8owksmVTl7sDgvnN1tjJzudtWNMlGU7LpuIEeVqT-1-321rrLoVUUN-W625yYTa6jVr5LP7t6oEijw_SybxqhKzwdKrzs_H54zWVS9z7xm6BeIed-0rHQ-PgDfHtIgSEIDByjw1uKcoTs1cJvTP6c0j43G50aEONaB511RmK2di2GRUmdpx6Sy7_XZYs8AqaDqawTPnEPCBpPMfFEEw4vhcwhXRrB5XlK3YT9HuJKASDSGmtJ4tEdCG704PCsEJRj1cifpDvLZaj6NQ7Qmw3E2kDTKTi_Si6Nbot0LxNcMgpZJ1nfykNt2ApUM_BupK72LU0Q-F6HpIIrItwq3kDBZ2vpGz53uPde0wdRHXc4M0fKxkh1ZQVKE_b7Si9_YG8g5hvBHMTIyDjHbc7JzqcuanyhjhuhVmKQbZSqHFZaQ0iYMU2ouh7wfMeNFZmhRTO9xCFL6HfY-TwPcTFK0BrTv5WPPrkL5JgsLA8muOEowBjxRBzMV8GK7BBEEMVqaInu1B8EmmfDCpvP1IxGV9YL8o7yauxK-H6memhB4unlbsMz7OFDyefQMKwfhgEejnlth3J7w1SA4HgY7eTEUeBK9iY6OqjjrsSWAU3-urUq8eQOL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=DOjLgj5KAK7pKaw5kqQ6lJQF2CjNzzZf8ON4qhLtjwUMFRBVS5HbXWNMHuWJ8owksmVTl7sDgvnN1tjJzudtWNMlGU7LpuIEeVqT-1-321rrLoVUUN-W625yYTa6jVr5LP7t6oEijw_SybxqhKzwdKrzs_H54zWVS9z7xm6BeIed-0rHQ-PgDfHtIgSEIDByjw1uKcoTs1cJvTP6c0j43G50aEONaB511RmK2di2GRUmdpx6Sy7_XZYs8AqaDqawTPnEPCBpPMfFEEw4vhcwhXRrB5XlK3YT9HuJKASDSGmtJ4tEdCG704PCsEJRj1cifpDvLZaj6NQ7Qmw3E2kDTKTi_Si6Nbot0LxNcMgpZJ1nfykNt2ApUM_BupK72LU0Q-F6HpIIrItwq3kDBZ2vpGz53uPde0wdRHXc4M0fKxkh1ZQVKE_b7Si9_YG8g5hvBHMTIyDjHbc7JzqcuanyhjhuhVmKQbZSqHFZaQ0iYMU2ouh7wfMeNFZmhRTO9xCFL6HfY-TwPcTFK0BrTv5WPPrkL5JgsLA8muOEowBjxRBzMV8GK7BBEEMVqaInu1B8EmmfDCpvP1IxGV9YL8o7yauxK-H6memhB4unlbsMz7OFDyefQMKwfhgEejnlth3J7w1SA4HgY7eTEUeBK9iY6OqjjrsSWAU3-urUq8eQOL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
همانطور که رئیس جمهور ترامپ گفته است ، گاهی اوقات این آتش بس ها به این معنی است که شما کمی کمتر شلیک می کنید.
🔴
اما ما می خواستیم اطمینان حاصل کنیم که هماهنگی مناسبی را تنظیم کرده ایم تا اگر تیراندازی رخ دهد ، اگر حزب الله به اسرائیل شلیک کند ، یا اگر اسرائیل پاسخ دهد ، یا اگر درگیری های دیگری در منطقه بوجود بیاید ، ما در واقع با یکدیگر صحبت می کنیم و می دانیم که چگونه تیراندازی را متوقف کنیم و چگونه منطقه را امن تر کنیم.
🔴
ما هم اين کار رو کرديم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129707" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=vu48AiiNBnLfXK8F8aZAY3ZRgBxYpanEuG5ZIMECp5cFKh6byc7UL9uX6dK61HmQq2zolIk6Tn7lnsHdCc2koNzt2FiuFd39qkRRzYQEL1cMJuKX0P5E_9TV7OvhZMD6DEdAxzSNm2PTm2LqWBHgF1OnGV2ONJfJxmp4n2lBTX8ofdj34pVZacrHTNevWsOT_Ev1aQgKVc7vNNRxZOhmugK-cVoxVlVBe7DXgjUMJXEJaVYqiRz5RcWvzXF1GgCQJnl9tWex4u3MdOCuj5_nP3UwCl4Bu2P9xHF-0uSMenEIiCq1kqlhu2dzV_vJ-vwb2-lfoqc3eMWuyGU96f7KV72z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=vu48AiiNBnLfXK8F8aZAY3ZRgBxYpanEuG5ZIMECp5cFKh6byc7UL9uX6dK61HmQq2zolIk6Tn7lnsHdCc2koNzt2FiuFd39qkRRzYQEL1cMJuKX0P5E_9TV7OvhZMD6DEdAxzSNm2PTm2LqWBHgF1OnGV2ONJfJxmp4n2lBTX8ofdj34pVZacrHTNevWsOT_Ev1aQgKVc7vNNRxZOhmugK-cVoxVlVBe7DXgjUMJXEJaVYqiRz5RcWvzXF1GgCQJnl9tWex4u3MdOCuj5_nP3UwCl4Bu2P9xHF-0uSMenEIiCq1kqlhu2dzV_vJ-vwb2-lfoqc3eMWuyGU96f7KV72z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
دیروز روز خیلی خیلی خوبی بود ما پیشرفت های خوبی داشتیم.
🔴
ما دقیقا کاری رو کردیم که میخواستیم انجام بدیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129706" target="_blank">📅 16:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=tZIKOLnKAOgSSQc9zVWfKH_bfvA3I9dSJmnsqmUygIWTDR7HTYzhRTcVUmGKRSyEHazQikGh5Smdv0dCEGIh_rzwPhrj89phzdC7ui858-2ODLxFZ0MojA-Tth2W0HAR4HjY32pdrrureb3LIQn5Jc2Anii9hcRRimmBpXq6QMInKVN3uZglgMNGE8rMShB3H33jZ4nc5BQc98SN79B_WzIteskageyULdyCkG91MXT8sXnw6K0qzga2n3zcfcwoDqd-qKf90lnNsx1k13lKH_n5kaC1ubiXMhGxBqXxyISsekIVgqZki3-2ejwpq2M6SpHnGD7NWKh5eEjcT9w-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=tZIKOLnKAOgSSQc9zVWfKH_bfvA3I9dSJmnsqmUygIWTDR7HTYzhRTcVUmGKRSyEHazQikGh5Smdv0dCEGIh_rzwPhrj89phzdC7ui858-2ODLxFZ0MojA-Tth2W0HAR4HjY32pdrrureb3LIQn5Jc2Anii9hcRRimmBpXq6QMInKVN3uZglgMNGE8rMShB3H33jZ4nc5BQc98SN79B_WzIteskageyULdyCkG91MXT8sXnw6K0qzga2n3zcfcwoDqd-qKf90lnNsx1k13lKH_n5kaC1ubiXMhGxBqXxyISsekIVgqZki3-2ejwpq2M6SpHnGD7NWKh5eEjcT9w-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فشاری شدن عوستاد خوش چشم از عادل
عوستاد خوش چشم
❌
عوستاد معکوس
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129704" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=fs3kXAK9c9YyhyS9bmcT7WLI2_BOIOKc_-_VPOBkXwrWSvGoRXMmV6WyqoQcu16jim133X5moGuKDg1JiZ7m1v6_GuyK5cA6rz6o068UHNWiz0A2jT441rd4rP30e8wV60ysEkcAQMmm1RXqDpG5nx-kUsfMaQiKF2h7yfOLqCDaONnGDcA37cr5NLfjJ22dXoF18ZeDMGNekLbbcyEP2EiugrhjkMaJjiYieWp31DAIVeXdJYyoM3_jLF7qRTFl95X005UfIzYb-P9CwbNyCOLZcDZ0hP2o9zgG7FfUtVA9VNOoq2rK44oTT7Zq8kJY3K65Vj12KVwfu4YO_Lo-zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=fs3kXAK9c9YyhyS9bmcT7WLI2_BOIOKc_-_VPOBkXwrWSvGoRXMmV6WyqoQcu16jim133X5moGuKDg1JiZ7m1v6_GuyK5cA6rz6o068UHNWiz0A2jT441rd4rP30e8wV60ysEkcAQMmm1RXqDpG5nx-kUsfMaQiKF2h7yfOLqCDaONnGDcA37cr5NLfjJ22dXoF18ZeDMGNekLbbcyEP2EiugrhjkMaJjiYieWp31DAIVeXdJYyoM3_jLF7qRTFl95X005UfIzYb-P9CwbNyCOLZcDZ0hP2o9zgG7FfUtVA9VNOoq2rK44oTT7Zq8kJY3K65Vj12KVwfu4YO_Lo-zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی : ایران از تنگه هرمز عوارض نخواهد گرفت، بعد از ۶۰ روز آمریکا از تنگه هرمز عوارض خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/129703" target="_blank">📅 15:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ونس : من نمی‌تونم ۶۰ روز اینجا بمونم؛
برمی‌گردم آمریکا، تیم‌های فنی کار رو ادامه می‌دن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129702" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جی‌دی ونس: معامله نهایی خانه است. ما پایه را گذاشتیم. هنوز خانه را نساخته‌ایم، اما پایه‌ای موفقیت‌آمیز بنا کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129701" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=HFuqxJaG8vfB7UhGO9LU5pt3_4lEOpBruwlSFsvEmdSax0yTaLRjiaXDuMvjj6c5a67eW2Lt1ehKBuPEdfWROsUKynjDncp-f7M1nI4qXidVzGl84k-NkxBawmXSJFp0_BayL0LKIk-3wGD2fwayTbJk2rsPyCe9f9rswMB1_z-5vqEi00JSbTYurmr_pimpdfVjWPM7J1mWoTVgGg_Y99uB03pckGXiGcW4YrbjaYc0V0KTd-lHGIPKnVspw1nXtC-ddF99ueffSJ3sDC5UKOnXMbFJDHqCi0fn_0PmdIUwgUd7LEsLERDSFLJNYt0Qu6FoPXBKEuRgjUSP6c1Sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=HFuqxJaG8vfB7UhGO9LU5pt3_4lEOpBruwlSFsvEmdSax0yTaLRjiaXDuMvjj6c5a67eW2Lt1ehKBuPEdfWROsUKynjDncp-f7M1nI4qXidVzGl84k-NkxBawmXSJFp0_BayL0LKIk-3wGD2fwayTbJk2rsPyCe9f9rswMB1_z-5vqEi00JSbTYurmr_pimpdfVjWPM7J1mWoTVgGg_Y99uB03pckGXiGcW4YrbjaYc0V0KTd-lHGIPKnVspw1nXtC-ddF99ueffSJ3sDC5UKOnXMbFJDHqCi0fn_0PmdIUwgUd7LEsLERDSFLJNYt0Qu6FoPXBKEuRgjUSP6c1Sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل در رسانه‌های اجتماعی تهدیدهایی مبنی بر ترک جلسه وجود داشت اما آنها جلسه را ترک نکردند.
🔴
ما دیروز به ایرانی‌ها گفتیم: «وقتی شما به چیزی که ما نسل هزاره ممکن است آن را یاوه‌گویی بنامیم، می‌پردازید، نمی‌توانید انتظار داشته باشید که ترامپ پاسخ ندهد.»
🔴
وقتی آنها چیزهایی می‌گویند که حقیقت ندارد، ترامپ به آن پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129700" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
قطر: مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران در حال بررسی است
🔴
محمد بن عبدالرحمن آل ثانی نخست وزیر و وزیر خارجه قطر به الجزیره گفت که با یادداشت تفاهم میان امریکا و ایران به پایان جنگ دست یافتیم.
🔴
بن عبدالرحمن در ادامه هدف از یادداشت تفاهم میان واشنگتن و تهران را توقف جنگ و زمینه‌سازی مذاکرات اعلام کرد.
🔴
وی اظهار داشت که مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران و مسائلی دیگر مانند امنیت و تنگه هرمز، با منطقه در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129699" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
جی دی ونس: آنچه جارد و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپ است.
🔴
اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129698" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ونس: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/129697" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
جی‌دی ونس درباره لبنان:
در ۲۴ ساعت گذشته، احتمالاً وضعیت در لبنان از هر زمان دیگری آرام‌تر بوده است.
🔴
۲۴ ساعت قبل از آن هم نسبتاً خوب بود.
🔴
البته ۷۲ ساعت قبل مقداری تیراندازی وجود داشت.
🔴
این یک روند در حال پیشرفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/129696" target="_blank">📅 15:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ونس: ایرانی‌ها با دعوت از بازرسان بین‌المللی به کشور خود موافقت کردند؛ این گامی‌بسیار مهم است
🔴
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129695" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
جی دی ونس: ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم. این تنگه باز است.
🔴
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
🔴
دیروز روز خیلی خیلی خوبی بود.
🔴
ما پیشرفت خیلی خوبی داشتیم.
🔴
ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129694" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان : اجرای تفاهم‌نامه میان تهران و واشینگتن به مسیر صحیح خود بازگشته و تنگه هرمز برای دریانوردی باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129693" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار العربیه: ‌جی‌دی ونس و هیئت آمریکایی همچنان در اقامتگاه بورگن‌اشتوک حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129692" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129691" target="_blank">📅 13:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: بدون وا دادن وارد مذاکرات شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129690" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72e9e80d1.mp4?token=Fe9w2jtTprHOqkGGOd6seV_o3s49pHP-1SVq5rNovLSMJ-BfROsV8Ry4LQYGsiHpfxfdyl5vAWmSWxUs-JobB6tDj1dHYANN0pvtukvHfx7UBN_FdKgApt_V45wmuUwjnJWQBars9TcqVQNnzNKMY0ik45onniomugRZGnsKTFG3xc2zI6opl8TgQ00qLfymI-V5nRI0Pic7vXo8OxoFAdE5C7xiu1RnrsXq5rB8BQDVuywEldHaiHx1YgAv3dDdA8HfRicFe-sxql9OwOu2XYgpA8qauBCzNXJagVO44BS0mcJI3GaKyGxFd6z5OfXIyUnQmIPEI5UNGqGwzVPoag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72e9e80d1.mp4?token=Fe9w2jtTprHOqkGGOd6seV_o3s49pHP-1SVq5rNovLSMJ-BfROsV8Ry4LQYGsiHpfxfdyl5vAWmSWxUs-JobB6tDj1dHYANN0pvtukvHfx7UBN_FdKgApt_V45wmuUwjnJWQBars9TcqVQNnzNKMY0ik45onniomugRZGnsKTFG3xc2zI6opl8TgQ00qLfymI-V5nRI0Pic7vXo8OxoFAdE5C7xiu1RnrsXq5rB8BQDVuywEldHaiHx1YgAv3dDdA8HfRicFe-sxql9OwOu2XYgpA8qauBCzNXJagVO44BS0mcJI3GaKyGxFd6z5OfXIyUnQmIPEI5UNGqGwzVPoag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از بازسازی پل B-1 کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129689" target="_blank">📅 13:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شهباز شریف نخست‌وزیر پاکستان: نخستین نشست کمیته عالی‌رتبه در چارچوب یادداشت تفاهم با موفقیت به پایان رسید
🔴
گفت‌وگوها منجر به پیشرفت‌هایی از جمله توافق بر سر یک نقشه راه برای دستیابی به توافقی نهایی ظرف ۶۰ روز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129688" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مرکز آمار ایران: رشد اقتصادی ایران به ۰.۲ درصد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129687" target="_blank">📅 13:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
🔴
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
🔴
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
🔴
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129686" target="_blank">📅 13:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129685" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
توانیر : در تابستان خاموشی خواهیم داشت/ محدودیت تأمین برق در بخش‌های کشاورزی، خانگی و تجاری در بهار امسال نسبت به سال گذشته ۶۸ درصد کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129684" target="_blank">📅 13:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تسنیم به نقل از منبع نزدیک به تیم مذاکراتی: ایران بازگشایی تنگه هرمز و مذاکرات آتی را منوط به اجرای بند‌هایی درباره لبنان و ایران، صدور اسقاطیه‌های تحریم نفت و شروع آزادسازی اموال می‌داند
🔴
تا بند ۱۳ با اولویت ماده یک درباره لبنان اجرا نشود، ایران تعهدات خود را بازگشت پذیر می‌داند و مذاکرات هسته‌ای آغاز نمی‌شود
🔴
هیچ مذاکره‌ای با رافائل گروسی، مدیر کل آژانس بین‌المللی انرژی اتمی صورت نگرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129683" target="_blank">📅 12:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkr9c1b60sxIG33VittGotP15jJs2SUcneQYs9LBUpXhnxi3EHp3Ph5DYj6hgREG57PtfOVfEQlz8XwSvHIf_VacNqM6cFwyBnMvTxmOyYUSYQQE9Aoq-JvpMhUdEYCn9GNg7mnLqeLQmkerATrJQZNJs03WaDu3QIZ3BHGRETmwtYlyv9PRzoIU-oEZDwh_8mJXBr16R3UyugodwHoC8cwhXlbJEgMhXj3wBp8GoF0RPTHkGNl2kQe7OjRXjahZDNN-g_SaC3C8yuk256ZqvorwsPJVzZq2WNUK2ovxp6p0rTk1ErvJaPIwsS-R2B7B19mZfGZh8WD2OL9Ax22k-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :یا مجلس رو باز میکنید یا اونجا رو به توپ‌ میبندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129682" target="_blank">📅 12:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ایتا از دسترس خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129681" target="_blank">📅 12:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXwM3ujaTpRFRGmBGEFdwgNp52neT7KNebILdih-Fr-wJkTiuzwTzCZ-aEDZ9NzrZhK_Vu8YhhN9BUrPATa8AE5T4enMtb0WQyK5t-mzCHT7KSphZTLfPFGN8eRSl8qUdsijKW5VbDiCyiyOfN1XH_9HEBzi6CKLdDd7NJx_bRuquY06lTBK5UeTTNaT569ucPA7chKhSviOdrHHh_2E_NQRnfDn4tdl8ebg4GujUaAFE5BNHDstJnyCk0cu64CL8S5xKTTHdLPuxNMkgC8jPhXPS2wA-VlnRt5B8hAxjZY-1djVxiJeNz-4xCD9YdRb_9A0V6ENeLrDn2y5XrJ9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNdDIB8DapLoBBktJHfKUkV_m1oYpyn0HGldarapHZ_MdGZxgBXy38M9ArU0zDAG6Mjy1xJAmwcD-KGFKTXbWqgEOqj724jhePwRx3eS0EHSQeZALUYOxx_DO83fo2vwUXE0JprjY3zdX0gL3r70UZKTAYtN9tIzIC8cRw1PI9_W6bxUQtklsErXXfUQKGQOghbe8VChPd_ONYT4wxQ2CGvSBRezXqNcEQBGsJjccm6d0HqNSGO8x6EAOrNa8r756j6vWqOac0beGkiHmPiXu4PkkO6bgI2BUdwuRYaEyWxWd7qJje1G7soB6Iax108jaalmOFFAxtvBcsjdJ5OuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6E9PQDAbp7OGvhdiS1SkSGcNct6jnGQH_M4e0tNzHP44XF2AgWx2x8e66-M4TFLyiKYvpTZgi5hLuXdJwyl2TRU1qdEl7vzMtEsawF_Qr6nQ0WP0AkvjpWAFVmXOiNwTuATPOyVoWcmEtNPw3KHmsEUJsyS4c06Hk9zAgKGk9W8vhUsb9ah4iEpfnggRxKaKu0xR3A5dMCZxWqvMPTXKprNe_X0n5kbPctDCNNIjLIXQu1UybP0u094q4OxGQ7fNX3SKUecYgCG2kVMdxT0jLicHIajTw3AmhhuL_LqfXh-eYUoK7lSLF-8m_ecuMi1rH1NFB92CwsfgOS8hTJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZV6MP6V4NkoppjGQ5rZHMgsXCODmaSy1fELOe4cjwnopG_a7BHN9Xq7EawwMk3ZZlbTMJHGwebbKycBNByM3d1ZmIkz8E6fQD8CLZ6S2j_dZk_Jt472v0_2HbzOP95iKgPiRSDTwI2xInmVbvxMChFUCT3_qChzJ9DtrJ_Wht33_Jy6V5B2xC1iqc5LXK63U5OGzEjyY6kwsA3qwAVLA-W4kNpvA6CL43-zOBdf9AUGsCHjMh6SH4jThlCb2zDhQCO933XVD1yR8mSD5n_oZ-aex_XtyqGsnqDMcNjNFYMuzJ946OZpIxxTQCjL031RMIwUvfBMpB6cQDbMhEx89-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqF5h_O6VHyhOwwK7QBrnNIZdvzFy5ebkbmyq6dKczyoCvfVQnzKv8wGo7-fHIojAzbzqU-cm4qyjLRMd5FD1wFah2MuDrbSaiw3PV1AkKuBIWQRDSJ69FiZK-98cYXzMnuXerJWG7didt9i1abamJIwceMheSzEJLWX2H9gvxsSo0iKr5eJ9iywBd68rISsNDOTZPliKs1VfqlVeU2EO9qQ23EmFILzRBksNGAclGpmAOsw5o-7Foi1RlQDD9r1EQk8FPWFk7olmjbOvEmBjVpE5svhyzN-5Zy3oiFlRDpoAqmEofk96HJh2_-DRRXnDmNOL6r1CcbnAi0QrY0ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODU25yKivjvAlhwa6zSoC3vbhghkF1L8MyNf2s5NJOSwfl9TdvG9l7S7kohuMs7W8sE59BBckIcfU9CPUhR3j_tZrI-4jfJrkLOpCEwm_O5rAIsjB0UjUB4--ngZmhobNX7H9-m5MENsTlc33QQFW2ULeLb27_HRCTZfceLZ2waqBCByH4AHuuBjic_Mm8avxUfGpnbujChtPIRmS6zJgZwJO8jLU7twvZWz1tW0lHvSOnNqFfMRHY0fBuqWqtMCKtMj7GeqP3R9hB4mk6kUZfjWmI4A4y8Sq6U2yX4dqW7nM_BdWBVPLmriE0ZhY25UVZdiUB3myp_OXfVtQddhyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7d85b4c4.mp4?token=CXdI5mdNkwE7Z6WlQLnB7wT2NGGqyOfr2YRBqu9-JVEBubQSA6kwLtVl9MTnRhjcI-YFcmdWMlbK5FkF2dln_EPlLVn40hkFLh70K1pcTw_cZaC5wIW4STXq-PMvV0t1kpFhThuFRUS9OPsnobu3eM7L8I0-PXvWLT4oln61inVlpHhCFFsi6vxVtB9BFSIDOPHqKFsc_KY6XIKuCRV5l1AQ51bPYcWnhNN8rgLQAMGoaVgB0nMvZk-UYq8asuvVItYuF61dMBAxH6LlQBirgwE-S1IPQO4fr3GPEjRfiloZ1DNq6OqCY3k_Rz5AKSrbTdvy2dNfMNfbaRFzmQckEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7d85b4c4.mp4?token=CXdI5mdNkwE7Z6WlQLnB7wT2NGGqyOfr2YRBqu9-JVEBubQSA6kwLtVl9MTnRhjcI-YFcmdWMlbK5FkF2dln_EPlLVn40hkFLh70K1pcTw_cZaC5wIW4STXq-PMvV0t1kpFhThuFRUS9OPsnobu3eM7L8I0-PXvWLT4oln61inVlpHhCFFsi6vxVtB9BFSIDOPHqKFsc_KY6XIKuCRV5l1AQ51bPYcWnhNN8rgLQAMGoaVgB0nMvZk-UYq8asuvVItYuF61dMBAxH6LlQBirgwE-S1IPQO4fr3GPEjRfiloZ1DNq6OqCY3k_Rz5AKSrbTdvy2dNfMNfbaRFzmQckEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از تجمع امروز دانش آموزا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129673" target="_blank">📅 12:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKZonD6EPHssoc9AxwjnWVvvazV497FZwl8yUm0zK1YUQjAErB2UTtBogPhqe6Gjc0ac65NWEyViwtdmLTsjWOo68sKl6Px8bqwkBQn-bV1DW9YuIM0RvH4sXIi0dXxucPjmWC9rSQlHUrY7TW0q0YP0KWcgQ6EAq5ryyQ7TjlRdNeW9uIgj35YIYyY2Iz3Q7snqrfa_kEtG4dg5tq5ljqIDRl1M7HSm39YbQ92Y0YoxAT8zMrJnYIWc3esEENtLml0lAPnRQqWiOhnVkeqetEvYkG-gfdpjosdB5g7sG_aaY38QwzDeJSElJexO9PUSTgiwW7hG8hV0wDhE4X_TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2759594a5f.mp4?token=GOu1nsgkjkBC3DZTpm9bAUgn9GQT8WRgrgYvS1ckVPnPraMOsJry8szrhO0Mbtf7hIeJuzcerVIlYepAHbXUT73X4rdGm93cS25eOTXWoDoY5WW7z3xfIEJ2AR3JFjAeIeW6Znkiki7e1qcEy5sJmjr8ezZcsivXxkDqO-LeSWyUA6uEI-jr5KBAa2iptfR6Q7WmAgQaxCY8W1xsX__kY5Nph_od21u5jOgRKH5H1_eo6grEYStwkOvjvoysRxRXZNEYvoRvD2Ga7wOeU2XMSSJyW06vc2FI43vayFBkPFoGPurS0O_FBFEFd7ISUfwBR2njN8rpGS4P71qGoaDBZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2759594a5f.mp4?token=GOu1nsgkjkBC3DZTpm9bAUgn9GQT8WRgrgYvS1ckVPnPraMOsJry8szrhO0Mbtf7hIeJuzcerVIlYepAHbXUT73X4rdGm93cS25eOTXWoDoY5WW7z3xfIEJ2AR3JFjAeIeW6Znkiki7e1qcEy5sJmjr8ezZcsivXxkDqO-LeSWyUA6uEI-jr5KBAa2iptfR6Q7WmAgQaxCY8W1xsX__kY5Nph_od21u5jOgRKH5H1_eo6grEYStwkOvjvoysRxRXZNEYvoRvD2Ga7wOeU2XMSSJyW06vc2FI43vayFBkPFoGPurS0O_FBFEFd7ISUfwBR2njN8rpGS4P71qGoaDBZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دانش آموزا امروزم تجمع داشتن و تونستن خسروپناه رو تک گیر بیارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129670" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg6emUw4_PZYdO4jFrfv6G_mkdLHyBD61IN-jKHlBX374Ih51l_sBLoa_NKeyFRoKS7UpXyeIYsBlW4YxunvW51haRP0Pb-vmwhB7-4oA1RQMCQFag93fNEG2ymo79hKlqeFo6BFbaL0lxKKjI_OKHe1L5VWqsrhajSmyKjmjp1MuxV2DsBSJjozbfDcqECPk8HmN9luyOpE5FiiZNkcd98al4QO8RHYlhS1JC6HyaFnppYrMsWxuN0tcFArjdPNr33VTkQYOsQqX1HCnfr_R36cISnQEJPSd3FrmGWTvKQCMANGMROA7NfHtcZYBdPuQb-gE1CmnLqN0wcLI156Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی: میانجی‌گری خستگی‌ناپذیر پاکستان و قطر، پیشرفت قابل‌توجهی برای پایان جنگ لبنان به ارمغان آورده است.
🔴
محدودیت‌های صادراتی نفت و محصولات پتروشیمی برداشته شد، محاصره لغو گردید، بخشی از دارایی‌های مسدودشده آزاد شد و طرح بزرگ بازسازی و توسعه برای ایران نیز آغاز گردید
🔴
اولین آزمون: ساز و کار هماهنگی و کاهش تنش در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129669" target="_blank">📅 12:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szup57xQ05j_SWJ9FnanlDx1NZlQGTA5ruqkMW4lKuxYoKqdPHEOvldMrCeVFmOgO55OqbnKlhPKoNUIv1-CshM_s40gcYbToCxtcgYvWI3-PyETR02UdWEgX3PcO59dov_fioUjTzmy4PaXAKmw3d7_10OIiFUYTiubVBOFiifw_LvrePfDPCtHFcUlGAV9vqKJJNrzv0HzXo4CZZ43MAKQ6zcXZgfUB9KVpRwqhee6UEFUpt_own-NEA-KrCdNrdl7KoxQI2VrHifKqdt34t94OXcKVGE6bk2HQJDYhTyuaVqQe5y1VpBDuYfYlA7gQv4bnDjhqDROl0vjE4wElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
🔴
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129668" target="_blank">📅 12:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6vFp2Y-RLmDODMZsD3-_ryoJ1FXHQmYIlPUrvW-sAXsGEkXIjZoMfm6WthVDV9B09F7X4iIkr8H-K6P1awCsnGxXCYKiLTocVoM3CEFX-M0vAg3ilekzeRpUSTY2UTs4A7AFBPg2sreBicFNflRmWGxJ67udKX2Z9Whvpwpj-EbfFGhxhcrbxDtRK1bfs_MHrcTQxhjYtE-SRh8DQkdMI3hzqFSvh6rDJoeMR4hP3KRLKhllWeJCvtRGgaFI5QiSHQFI-pCuqz55YistvWANG9iFwTjaLEIMuPAY4eYv1BkcETjLUf7ZEqGaK1pZPV2KVUjqb9GmYH7mHBO_Y7-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیات ایران همین اکنون از باند فرودگاه زوریخ تیک آف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129667" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مذاکرات فنی ایران و آمریکا در مورد سازوکارهای اجرای یادداشت تفاهم اسلام آباد و تشکیل گروه‌های فنی مربوطه از امروز (دوشنبه) در سوئیس به ریاست غریب‌‌آبادی برگزار می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129666" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: ما برادر بزرگ کشورهای منطقه هستیم؛ برادر بزرگ، هوای برادرهای کوچک رو خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129665" target="_blank">📅 12:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6112aecb98.mp4?token=M6n7A1nnKvIfodfABkFHLukJ88JxF0IKEe14k_tQYxL29b1C-cAym_s7zLNvNIunAasG2fyp88m7M4fDDpAzJdC9mji8PSvQ0Sji3Y2VnZeVAFAh-MeFqCv8aiFluTGQaWa8PoG9z_tcZGfRxnT1_alM7-MWAdAjkuYkcqRMWEajbKNRPxt_C-7T84_qEABrOF650LzEuSqJzgaFZISFrkdtqPNssqplXOaqA3kWTzoy-9nFtadPc8dz8CZd3_UQvSwSyPNng2Dv3JPNsLMGAJ2dR4i6JQRExOUjZghERsryAYAxGq755TVlzCKaASIoDtgghPHv3QM1aRYPWENKCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6112aecb98.mp4?token=M6n7A1nnKvIfodfABkFHLukJ88JxF0IKEe14k_tQYxL29b1C-cAym_s7zLNvNIunAasG2fyp88m7M4fDDpAzJdC9mji8PSvQ0Sji3Y2VnZeVAFAh-MeFqCv8aiFluTGQaWa8PoG9z_tcZGfRxnT1_alM7-MWAdAjkuYkcqRMWEajbKNRPxt_C-7T84_qEABrOF650LzEuSqJzgaFZISFrkdtqPNssqplXOaqA3kWTzoy-9nFtadPc8dz8CZd3_UQvSwSyPNng2Dv3JPNsLMGAJ2dR4i6JQRExOUjZghERsryAYAxGq755TVlzCKaASIoDtgghPHv3QM1aRYPWENKCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حمله هوایی ارتش اسرائیل به یک خودرو در شهر غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129664" target="_blank">📅 12:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiN0wc6_Mj2_AR3h4VKIgMwpEhDq7Szc-6QG8tqpGph0ZrMwrQvQg9BBlIay_WyYgAbNb3-HMQJetPCuq8jOGyQahGF6529oTXByWgNI6CKRnPsnb9jv-J0uq50N6qRalQ4h6xvC_GoZ_YCCVeLTzahFxiP5bdiuazeuxb3O0gxyqlyXSMyp0xVZM2s0UO4mvDk-oVcbxn_-KAOLPJI3KdWxkWwSsNB6bkuLX9OaUVYvTzYHpUc_yqHmmYTQ7B-VhdeRD0mROd2NXk6j9t7_z_YZT6WBvZvV4AfJ-T75wSRDjDYvMW_xwg3We_YqPJDj1Hb2mnnljjbw-GAfHanfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط کِیر استعفا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129663" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH4neC0v3TxknHcLapbGP71mRSu-PMjhuAWT9g2wmnezjpa9qd2mPpf23mvBaRcRA8GPjtjh7lyBxa-SUwjJ5mmyuZu8CxpRYxHA1r0uei-8R1g4ERYeRlgOUeSCaAaSw_SqSt_wFsCGgdbQGW3LFyxOlewW-rdkUdiCwJ9YhhxrzR_xJjKeDrZflSbssUblfoU2RwGplrK4Zg8-8wrGgawc6bupIYVaiDmcmZpEB-hdY9E9thJ8VSp780Ts8kuafw7UeDclOI_6JCW1xivqrWHAQHiW4Fs3LdhEiLjA8aB9iRIU2IW7KErFmRRHhJi04_jlWUDHnlZsDjvkRm5KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
🔴
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/129662" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر اقتصاد: آزادسازی پول های بلوکه شده آغاز شده و بانک مرکزی اقدامات لازم رو برای دریافت پول فراهم کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129661" target="_blank">📅 11:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U19YAPlZNxGplYkHhfS_kp47U5Nv52WVZuRGjNdiXtp5kit_pJukhRRu0sEKDKbg7C1abYhb3VisQJJCkQGUN30KWGyXRbR1evuPj6CKWdpffq0CCaVS4-FdPj6U0OYU9-gh9nsvvFWBgIsEcvVBnnQygoAzKtR43Q9OvfOdnNMFPSVeLh1NZmjRrLlhuyZ3iA6jIsnAn3ijwTrjZdrEFTO4VIUJXaH39giom2tEI2gcZ_i6-fDRCBLgWes6hwC2-QsDmY9ZCzWESGoGZVtrM_gFQUwS58q_lhZWvG7TQ-QvwefcIVBDiQWxGEafsYg9u251w2JIUKsxFHWgl1DN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
چشمم آب نمیخوره که توافق انجام بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/129660" target="_blank">📅 11:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خارجه ترکیه درباره مذاکرات ایران و آمریکا: دو مسئله وجود دارد؛ اول، ممکن است که حل فوری جزئیات فنی آسان نباشد و گاهی شاهد بن‌بست باشیم، باید برای این امر آماده بود
🔴
دوم، همیشه اسرائیل در کمین است تا به محض یافتن فرصتی، در مسائل کارشکنی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/129659" target="_blank">📅 11:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هیئت ایران محل مذاکرات سوئیس را به مقصد تهران ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129658" target="_blank">📅 11:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خضریان، نماینده مجلس: در توافق با آمریکا تثبیت نیروهای مسلح این کشور(آمریکا) در منطقه را پذیرفته‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129657" target="_blank">📅 10:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxFmh9_TwshNRiIBqkCDQb3emyW5DIwO8GDxlIIucU8pkFzNWf98aXr_VEtnWGtxScCx0-EWmKffYc6BO2Qlqkl42s1lA17sKE1jrE5Ub-NGRTlmru8rWDlVW3Mv8DG4FATB7vK_CXQqsLDxJ6J4efJ25PZiLjLtFDXJV0_1N-ZPnAsBDIdMly01khkZcb3PdW1KgUQQmB9IU_izLzFY4yugmvN6pOfTAhymtjCD0VWt90JOrC8rVWIPK5i8FqHEG79lq7ultHrgCiwv8wGHw28hktFufeWjqHHWDFbfX3fMqhiFQvH13YhOh8e7zpTU9s1mATHZfPXsgI9S6-OuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: عراقچی نوشت ایران معافیت‌هایی برای صادرات نفت و محصولات پتروشیمی دریافت کرده و برخی از دارایی‌های مسدود شده آزاد شده‌اند.
🔴
مقامات آمریکایی این موضوع را تأیید نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/129656" target="_blank">📅 10:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
هیئت‌های پاکستانی و قطری اعلام کردند که مذاکرات آمریکا و ایران در سوئیس طی شب گذشته «پیشرفت‌های امیدوارکننده‌ای» داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129655" target="_blank">📅 10:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129654">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxsQfah9iFz6u6g4dIadtCzb3dONAQc2niEkLITEa7AErnWX_hitcbzBvpiHFJA7AfWMX3wZ4ypx7JtH28vzgvh9WgDGMdq62qXpxFk5AKDwaI8Fgik0KQJQ2MKM0b2fk0aVe2_Mmk2ct6c3RctLDuCmyq9Dht0qZbJDcbnDJ3l8bZZ0f6VBnxZaZDc9I_-k7YmDUHsL4e_4I-F82170_5gPYlv6i3cUkrpSl9llY2Ml2NAtUofKEqaO_5xDrfUwYMuN3ak_z1YgOwP8kxhacW5aVMSthnefhD7tuIzGmajlrRtOnthznIH6qqXBPbhkXHHtZX54j1Qla8Am655kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:شما تهدید می‌کنید؛ ما اقدام می‌کنیم
🔴
تنگه هرمز نه کازینوی شخصی شماست و نه حیاط خلوت دزدان دریایی مدرن؛ این‌ها آب‌های حاکمیتی ایران است و تصمیم نهایی با مردم شریف ایران و نیروهای مسلح شجاع آن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129654" target="_blank">📅 10:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر دفاع آلمان: در نهایت، دونالد ترامپ مشکل بشته شدن تنگه هرمز را ایجاد کرد، نه ما، اما ما در بازکردن دوباره آن ذینفع هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/129653" target="_blank">📅 10:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw7ZgYH9fBQRxRP_CRpI_dX6iuQD9e9Bc5e2r0if4qy1nCkFiaiVtUY-WqYXBJxt4xi35t3YlGKjiqtBi-l5EzQnNPJjbYES5EX55dX8UyH2QxMKsA_mO5fsTM9Ft7gWYOTryWWj_XOwScTYxzSeN3567-SHX5Pho7MQ0DLIB2qJ35MY5ygKmsOk9PTR2HRTMA6dCI5eNtezlvTrzOgOGFcLo1GxHmwy1UxU0c9dU8IvK1TYxWlGumS_afxLlcfjSpyxFbJTlcMMoW9GdsQbBysXbHsNVqI64HF-ShqeeV7bxRxw0q2-XPtQwNkX7VXJfScb0sP2O5gHACEbaMk0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مذاکره نخست‌وزیر قطر و ونس معاون رئیس جمهور امریکا در حضور جراد کوشنر داماد و فرستاده ترامپ در حاشیه مذاکرات سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/129652" target="_blank">📅 10:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">️
👈
وزیر دفاع آلمان:
ترامپ مقصر بسته شدن تنگه هرمز است
🔴
وزیر دفاع آلمان اعلام کرد که رئیس جمهور آمریکا مسئول بسته شدن تنگه هرمز و باز شدن این تنگه در راستای منافع اروپا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129651" target="_blank">📅 09:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
تانکر ترکرز:
ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/129650" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJij6Igu5BqxDwjO9lGVgS_qeUdpLaBgj7YURq08Z_ByF3nSmGR-WV3510wdFA1HgfmxYp3s_cqdK5s8PzotpMkUwB1A0Dcg3lBh_ywXI-UnNj72M4YYXAyS7mziYJHUax9B4qAHUBslmfxy5sSH68QOCFYz6ykvxwSsn4fVphIZr22hK-jIQoS3Gh_V2vupMZTTaamvrfHQCmg1dYXKLCAmomfUKiyxKoBodkvYurQxYJdn8RXtAq1_zpv3-Lf0FthEUugwseiA4iTNRMikXC-y4s4SBcu5hDPAOtc-pIDN-o6HO9LaC3zGrR7nRHUo9h_dORTEyS9sXJEpfAwBHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سدهای کشور چقدر آب دارند؟
🔴
بر اساس آخرین آمار از وضعیت مخازن سدهای مهم کشور، میزان پرشدگی سدهای مهم کشور تا ۳۰ خردادماه، ۶۶ درصد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/129649" target="_blank">📅 09:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/129648" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شهباز شریف: امیدواریم مذاکرات به سندی منجر شود که صلح و رفاه جهانی را تقویت کند
نخست‌وزیر پاکستان:
🔴
انتظار دارم مذاکرات جاری در سوئیس به میانجیگری اسلام‌آباد و دوحه برای پایان دادن به جنگ آمریکا و ایران، به «نتایج بسیار سازنده‌ای» منتهی شود.
🔴
امیدواریم وقتی به خانه‌هایمان برگردیم، سند فوق‌العاده‌ای در دست داشته باشیم که صلح، پیشرفت و رفاه را در سراسر جهان ارتقا دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129647" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129646">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بقائی: اظهارنظر تهدیدامیز امریکا باعث شد ایران حاضر به ادامه نشست چهارجانبه نباشد
🔴
در زمان نشست چهارجانبه اظهارنظر تهدیدامیز امریکا منتشر شد که باعث شد ایران اعلام بکند در چنین شرایطی حاضر به ادامه نشست چهارجانبه نیست.
🔴
قطر و پاکستان تلاش کردند گفتگوها ادامه پیدا کند و ما گفتیم به صورت چهارجانبه نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/129646" target="_blank">📅 08:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129645">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvnnVk0jmY4e8-IjAfB19QFvBHw2bWueGXe_hgi8-dd5drUTDFZyJCvwh0iWaOxq-_BVv522wuvOqV0U8cNPndhpcpzy7KjC-Pv2Y5vHeEg5DHFPUQLh9nVBoh91tbymh29JtmroylZCj5nJOmS6zCzgwvmY0jMpv267div8-CO8gWxXP835dVa2cZvHFbokC8Kw6L_qPDuEI5Z8nbn94bRqm3cO91X1BlC0wZvnpZiil1hgw4ymDzLIu3XpNNQl1fj3KsENoYNs9gbyVHnRL8pERruKB4jSa-JP8hf8CdfJlKOoirKKchNcPFKgaRgwINe6d9XfvDBN_pRWe1979g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:
ایالات متحده، بر اساس تفاهم خود با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تحریک‌آمیز رژیم صهیونیستی در لبنان است و باید پاسخگو باشد.
در صورت تهدید علیه ایران، ما آمریکایی‌ها را مسئول خواهیم دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/129645" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ARCX64__7J0Y4I2PIkK4T-z2ZFIi7bLtQSNSVQ5bTpkqiOVphmkNyGaw5jo6vO8hqR6AWYBsHbqxXZ1ngt4h8t5I_lU7fSYYj1hVfatN-Grku2Hn80fMOHWneGigJX5N3LeoRbMompU8AV92fE9MqSQDUyxp2d1acM_ysghIMn01iQ1zGfOI6we5aliom-7zp0WlhjW6GyuAtxCvuYkSC3-zssPZlYyAcx2Fga-84k6Vez3RZHesCnE73YHB7vL2ik7gX8A5luwFaqYuw52jFWK6KF8ibFEI9TEyU3sog8D-MnBuAIuxBBjCZTKQyVrU6V1JZYiIQyr_5iiBeWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جای اینا تو جام جهانی خالی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/129644" target="_blank">📅 01:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgM_xru60rCjbk6zQ81BBBMPD6dhU48e2asayXjTt9G1vm2bTRGJo80srBGS3YFjr3XqvvEdkX4sX1YySIDqt05Y77uBsb__nm-vqTHRWJp5o4lpGbyT2QBwyGPJCp5lpqWf3klnLocJfrGN7vU83c23cT-sAtWBPNYYypG1DUI7gFlE1DyGkIqlczZay_VJLdkev4ibFOXQEZ2ByxX7_GS1hPYaz9ZXYrdJ75blSCzd0ocY4iUliXue66zmoGa8OOyfS7yyNd8XR7JsmsNcJuxy540hpZ31MVf_7HvprMSxlKGGzWudtqnPwqJMLoJZfxxNwM3Unh45qU-AdiFHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : نیویورک تایمز نوشته بعد از نزدیک چهار ماه جنگ، تقریباً هیچ چیز عوض نشده
جدی؟!
🔴
ارتششون عملاً از کار افتاده، نیروی دریایی و هواییشون نابود شده، موشک‌ها و پهپادهاشون و توان تولیدشون تقریباً از بین رفته
🔴
رده‌های بالای رهبریشون حذف شدن، تورم سر به فلک کشیده
🔴
اقتصادشون به هم ریخته، سربازهاشون حقوق نمی‌گیرن، تنگه هرمز بازه، نفت همچنان داره جریان داره
🔴
و بازار کار و بورس آمریکا رکورد زده.
ایناست که عوض شده؛ و تازه این فقط بخشی از ماجراست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/129643" target="_blank">📅 01:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8518f567d8.mp4?token=WEirKV6Z15e9W4Ml67Pm80kNjvj5RWtZmM-dUDbwd1tAxjQiCZ2H_m1e5akwZRHxAvD3Ap_bJsDIIxIXCo-lj28Es8QVfL1OHyGvtjNr0YcPuuT7oFpBqORMonEBzU3gBANPonx8AE_o4EhX1tZRz4XjHwwGHrICcI4sdaw7snOF9Q1899K4oUbEZIwq0am9ocXVAXj5edF_XnqMQC3WHWjPfSdRiZz1Agqgtpm6Y8-u2yS6FxREC_yrdGC98ktbB9tKYsuHMpLnG8C-ls4nN7AtfrGaNNjpCi-uN3ZsTEp3uA1SuHfVvHOLlxO3D6tSQuR1XB0apinWbzpEoqVgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8518f567d8.mp4?token=WEirKV6Z15e9W4Ml67Pm80kNjvj5RWtZmM-dUDbwd1tAxjQiCZ2H_m1e5akwZRHxAvD3Ap_bJsDIIxIXCo-lj28Es8QVfL1OHyGvtjNr0YcPuuT7oFpBqORMonEBzU3gBANPonx8AE_o4EhX1tZRz4XjHwwGHrICcI4sdaw7snOF9Q1899K4oUbEZIwq0am9ocXVAXj5edF_XnqMQC3WHWjPfSdRiZz1Agqgtpm6Y8-u2yS6FxREC_yrdGC98ktbB9tKYsuHMpLnG8C-ls4nN7AtfrGaNNjpCi-uN3ZsTEp3uA1SuHfVvHOLlxO3D6tSQuR1XB0apinWbzpEoqVgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام: مردم لبنان کمک در راه است
حزب‌الله مدت‌هاست که کشور شما را ترور می‌کند. این موضوع به زودی به پایان می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/129642" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قلعه نویی: تیم برتر بودیم و باید میبردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/129641" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آکسیوس به نقل از یک دیپلمات آمریکایی:
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/129640" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بلژیک اخراج داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/129639" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بچه‌ها بریزیر تو الو اسپورت
⬇️
⬇️
⬇️
@AloSport
@AloSport
صحنه‌های جذاب بازی رو اونجا میزنیم</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/129638" target="_blank">📅 23:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فاکس نیوز: مذاکرات همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/129637" target="_blank">📅 23:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نیمه دوم شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/129636" target="_blank">📅 23:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa19e4420f.mp4?token=JpX7vCxdfUjiaywxdaxrcNvP28PPSiIfp00BkrTcm6GldFj23kM1MhWtafdJreS4yfAiDOY6ZGkgbhO-BKABw2ReYexgNy35M6pyNC9lFUTDo9jUVbBRBe_imvy2WMMzPPYmyCavEK0N7VKKkZ5-MFslsfPes7U3LWd8YHlh6ZKTCdWJ3mYmRN8Dl4hL2a_pVRea1aYxeusJEFB9BYdSbJUny8Vv7529qHPX5qaGvcd6-wJi4zmzTGB2w4Ec3ZewBcHDFaNOdwW7vVFwGVuSFi9em7-URT3_FdbqQ2ne3m12MAfSuJMDeHFV4vPVFXWuEJVzKHTC4bHvQZHqwZhvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa19e4420f.mp4?token=JpX7vCxdfUjiaywxdaxrcNvP28PPSiIfp00BkrTcm6GldFj23kM1MhWtafdJreS4yfAiDOY6ZGkgbhO-BKABw2ReYexgNy35M6pyNC9lFUTDo9jUVbBRBe_imvy2WMMzPPYmyCavEK0N7VKKkZ5-MFslsfPes7U3LWd8YHlh6ZKTCdWJ3mYmRN8Dl4hL2a_pVRea1aYxeusJEFB9BYdSbJUny8Vv7529qHPX5qaGvcd6-wJi4zmzTGB2w4Ec3ZewBcHDFaNOdwW7vVFwGVuSFi9em7-URT3_FdbqQ2ne3m12MAfSuJMDeHFV4vPVFXWuEJVzKHTC4bHvQZHqwZhvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/129635" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjJbLGxmry6C4HtcSwRkCT2tbsq_VCF01pKW_QSYbbdkRQuWJkRgpasJ4ejFz7ghP40WlCkxeSr93GJ5w8b3N5MSIGiGO-zzu7_86r7b8mDuUxdYnJ675u8tW_hDTPMcQDJy-ZIjXSp6nQQmlU8tdUvo2tRmHp9b5c1fWsVoLr2HZbsmdut2WjOeD05hRId1wjUdmm6zzUgz-M4r6BbcJXUkLObdh_i-DRZPf88HUa_3dAX3pvOmkfVRCPpNc-zhqR3rqOWsynptalapRKW-oYakQvMHH142gr5clAaPlMRbve8WcIVM3gGlCEic9byXidiArzUXxiEfFbILQ9uAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار خارق‌العاده نیمه اول
🔥
@AloSport</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/129634" target="_blank">📅 23:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/129633" target="_blank">📅 23:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjMyMCKztYeGmGavFKFDjRpppGGHOOC_vECXycjwzMTWb4D6Fwbn6Sf9ERN_qHYR28xwk6HRCvOxkmlHo4uNiKao-oEvhFlQWbyjDv3dJKZ4EbjVKX3irrZYMpx4othmFS94Hs4v2bBfLLHCoHBTfrxBgd2mpzjwmcIFER891MyN5lsd5QJW-3n_nTGwZmRZ28q2x_uv7iVUZopo8KQzpAocOnAHk_16DYF8Y8aIovruAtmuHEYyKscImSdmMNbAOKa7DNRLq3T6q2H6Cc__ggkQE4smSXhzbnAKfqCLj_6NxAPLLT3ooA-lRgJblSNTgWvaPb9hWc9UrFAxQx2x9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/129632" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز از شنیده شدن صدای انفجار شدید در دوحه قطر خبر داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/129631" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز از شنیده شدن صدای انفجار شدید در دوحه قطر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/129630" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe7c09349.mp4?token=QLWtrvWn4gzB9wF03wdGOTrM1pZzbPdsQMAMH70YCCsvsI0zYZ06MliFq-e7UabZGwIdjgS5GK-oM1wFSqcybtL8Q-GwLX5IeKXqy3iZkg6w7mdk-XP8GM_qq1DmrJ7g1bx3i31b1obCza7lU-POKboEILmyc4o7hVlw75neQrWm0MywHx-1VD4nqctONC0lEwfwY20fD729_A8BwooDlBqc_hsv5qDuANd5c_TLHSR_2MT5r22zzCofxz2en-SD1haED5p1bJnyxmGe4ug2whRimOib08rqidimWAppR5uG3s-5eYW-QkSC1q-yDoZye6l4CZ4tZODcsoM79_Rc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe7c09349.mp4?token=QLWtrvWn4gzB9wF03wdGOTrM1pZzbPdsQMAMH70YCCsvsI0zYZ06MliFq-e7UabZGwIdjgS5GK-oM1wFSqcybtL8Q-GwLX5IeKXqy3iZkg6w7mdk-XP8GM_qq1DmrJ7g1bx3i31b1obCza7lU-POKboEILmyc4o7hVlw75neQrWm0MywHx-1VD4nqctONC0lEwfwY20fD729_A8BwooDlBqc_hsv5qDuANd5c_TLHSR_2MT5r22zzCofxz2en-SD1haED5p1bJnyxmGe4ug2whRimOib08rqidimWAppR5uG3s-5eYW-QkSC1q-yDoZye6l4CZ4tZODcsoM79_Rc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به علی الاصول گفتن‌های بی پشتوانه و بیجا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/129629" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-dQ9KW1ihYXNMkyZvy3XbJCH4WJp8GKYe5ntU_-HEiIN81jaa5aJHYPoa752UsrzCBDldPhH8lMPNwyOdjrSMcW_MyCyGh8u4_N1pOOO6WbhQOQknLasY5qt4tNE_W6x51t4DfIVOei0oHEWUl6pKVOXqH_ldhD2KjN6qcpXd_Y2LErqZ5ir0GMYvQikkfixquTrMWTActNFyHflSgZ8LRt5qpHIhwTSQGkphWxOW_hWTcA74OVHTwQwneuNCld7eoed81H36sVNh6jQiPworAs3-vSJlBYuRiT4OPirO0nKoRBteddDLBoy22sWqXf7ogcvlDvjjAVgcm_C_qjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/129628" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
صدا و سیما حلال خور، حق پخش رو دزدیده و پولی نداده و خودش کلی تبلیغ چپونده تو زمین و دور زمین
#دزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/129627" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مجری صدا و سیما:  گل‌های ایران افسایدشم قبوله
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/129626" target="_blank">📅 23:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مجری صدا و سیما:
گل‌های ایران افسایدشم قبوله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/129625" target="_blank">📅 23:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
زلنسکی: دیروز ما با حمله به پالایشگاه نفت آن‌ها در منطقه تیومن پاسخ دادیم. اگر بخواهیم دقیق صحبت کنیم، فاصله حدود ۲۰۷۰ کیلومتر بود.
🔴
پهپادهای جدید ما با موفقیت به هدف اصابت کردند. مسیر واقعی پرواز آن‌ها حدود ۲۵۰۰ کیلومتر بود.
🔴
آن‌ها قادر خواهند بود ۳۰۰۰ کیلومتر و حتی بیشتر پرواز کنند. این‌ها پهپادهای جدید هستند—پهپادهای خوب.
🔴
آن‌ها به فاصله‌های بیش از ۳۰۰۰ کیلومتر خواهند رسید، چون ما می‌دانیم تمام کارخانه‌های نظامی آن‌ها کجا قرار دارند، تأسیسات نفتی‌شان کجاست، مخازن گازشان کجاست و غیره.
🔴
ما به ابزارهایی نیاز داریم که بتوانند مسافت‌های دورتر را پوشش دهند. و ما در حال ساخت آن‌ها هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/129624" target="_blank">📅 22:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ایران گل زد که آفساید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129623" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو: ما در برابر یهودستیزی مبارزه خواهیم کرد.
🔴
ما در برابر بی‌اعتبارسازی خود مبارزه خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/129622" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آسوشیتدپرس:
هیئت ایرانی و آمریکایی هنوز در سوئیس در حال مذاکره هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/129621" target="_blank">📅 22:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نتانیاهو، درباره رژیم ایران :
فکر می‌کنم ما شرایطی رو فراهم کردیم که رژیم ایران سقوط کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/129620" target="_blank">📅 22:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نتانیاهو:ما یک «منطقه امنیتی» در غزه ایجاد کردیم.
🔴
ما یک «منطقه امنیتی» در سوریه ایجاد کردیم.
🔴
ما یک «منطقه امنیتی» در لبنان ایجاد کردیم و تا زمانی که لازم باشد آن را حفظ خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/129619" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
صداوسیما: ادامه‌ی برنامه‌ی مذاکراتی هنوز مشخص نیست
🔴
واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس جمهور آمریکا مهم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/129618" target="_blank">📅 22:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شبکه کان اسرائیل: ارتش اسرائیل شروع به کاهش نیروهای خود در جنوب لبنان کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129617" target="_blank">📅 22:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو:
در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد.
و در اسرائیل می‌گویند من هر کاری را که او بخواهد انجام می‌دهم.
هیچ‌کدام درست نیست. ما رهبران کشورهایی مستقل و با افتخار هستیم.
من نماینده منافع اسرائیل هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/129616" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سی‌بی‌اس:
دولت ترامپ خواستار عقب‌نشینی جزئی اسرائیل از جنوب لبنان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/129615" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 دوست دارید کی ببره؟</h4>
<ul>
<li>✓ ایران</li>
<li>✓ بلژیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/129614" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بیرانوند: دروازه رو مثل تنگه میبندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/129613" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxvvc53VcO-2hPX1kKQ-mo6Z7fPRajoBC6MeU-Ia4KHltltzuHv-aqy-sYNjfKtAuaVC6fWrJ2hSfpya3qo2vkF6LNaReHlm3uLgSSgXXRbz9_oQbYtZSm6wCY18qmmHVTWeOIMn3AhZ41G_cgeMrejhCnsupruacrQ-3FPbcu7uJ8eTWwI_0MdI1aX0AgK5O9fyHnghqjmWgh9uL_rtUPZKqbv9NKYBBpcYtCCs8qcSCNh4uciph7qnljrw7rk4CATHzlsbhxY7bxqwf6ZxuxFwYUo85x6QkMV2I5Yz7qFE5IpTo-Xhg-g8O7XHpCMSAFpNPz0AHIJVGf9AjcyEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نکات فنی قلعه نویی به تیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/129612" target="_blank">📅 21:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی کند، به مذاکرات باز نمی گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/129611" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdQYSg-y-acQDYXk-l-cm9U26LzkriEeOuHvImP_l3spfJuiOFCYt1qXx-Lc0yQTk6TB2LPSdmoO8zug6NHLWXP9lLXBMt74JGWHxSr2o20DWGp6qNqIw5mr7pO54ZlWY5a1XhuC6elYXkRL4sZSlYeZN3MNE2X_5jap--dbaEOvN4QK22a1Er6KP2oloDH6wQJlkbG-jkT4BwVyDowatyYO4U56oUgX_0qWAj1RApqstM3hEOxgQTqMU2W2wJbFqV3106KHKuRIPgNY9X5KdCPA8UH67pzq3VXdEs9Vd4w4bpMiHGMAuBm0a1uRe5IXtzXzTilwLfwRiArheibYsySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdQYSg-y-acQDYXk-l-cm9U26LzkriEeOuHvImP_l3spfJuiOFCYt1qXx-Lc0yQTk6TB2LPSdmoO8zug6NHLWXP9lLXBMt74JGWHxSr2o20DWGp6qNqIw5mr7pO54ZlWY5a1XhuC6elYXkRL4sZSlYeZN3MNE2X_5jap--dbaEOvN4QK22a1Er6KP2oloDH6wQJlkbG-jkT4BwVyDowatyYO4U56oUgX_0qWAj1RApqstM3hEOxgQTqMU2W2wJbFqV3106KHKuRIPgNY9X5KdCPA8UH67pzq3VXdEs9Vd4w4bpMiHGMAuBm0a1uRe5IXtzXzTilwLfwRiArheibYsySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی در مصاحبه جدیدش علنا به حکومت دوره آقای آیت الله خامنه‌ای انتقادات سخت وارد و اعلام نیاز به رفراندوم کرده است
🔴
ضرغامی گفت مردم باید تصمیم بگیرند که چه سرنوشتی داشته باشند و خودکامگی کار فرعون بود.
#تغییر_پارادایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/129610" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی‌برای کاهش تنش تنظیم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/129609" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خطاب به اونایی که ۲شبه علی الاصول راه انداختن
🔴
اصول خدمت به مردم و راحتی زندگی مردمه که سما درکی ازش ندارید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129608" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/129607" target="_blank">📅 20:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqAenoNVpaGAffRX0zQ-yDRjApCCQiQeTJaByssnmq40TRslCmTT6gYZBmufClk4D083yWaKmHckgApn0LAp-z8VVF5gcjdNqml7EbtelWJm_RPpYqiJSUEgPJPS4qSonraxfAzwe0CCI_gxeMfMu0gY2ixfO7lBjeQ4X0UHHkkIzjGRUM39i-5I1YzV0kyU23H_tNEEFfwtPKLrgcfCFA7mjaCoLh34T3sp3R3zZcpAhtiSS7UIuwAaGbh2cxv1X3wfWw_zxUl-kWOLHRnaRxMbAKbo0Yo4fTvv1aLqhEntsruwSSKtzF70eQrOMCb5Jq1zLYmnD3NSNpogrw7xTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
ترکیب ایران مقابل بلژیک
@AloSport</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129606" target="_blank">📅 20:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی به محل مذاکره برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/129605" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoTaI7iFgw_B2iCLLKHeeysVFDnbMIVzdrUNDuFmRefQC8Eho2uw_P5RhggfELa11C-MUPC_gmMMPtMu-3Ofqq5rQFMv_ywr6k6n4RpabIdwsnlE8egXuAVWD9vD1sLWQesixcSv_j4LFP4-I5CPj-bGMrL7dgOr9vE575KBrfmNA_O3BrlWamZ9uVmXR1Ydz5O9c2rqv65WpzfgtfHw7a8Q4jynwtiuDPw8Evw2_F59MhrAqLc2KpBPEzSBcdDu2NaWopjNmrVz_wTN7Ti5V5wNjPh_gU3b-dLVGz_Expqd0QGR36Bz3mJtgDhBB1yBITCIYHlo0B99CZ-93yD5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/129604" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/129603" target="_blank">📅 20:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده:
ایران مصمم است روند اجرایی شدن تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند.
🔴
نشست امروز در سوئیس، برای پیگیری اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵ است.
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
🔴
بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
🔴
گفت وگوهای امروز، متمرکز بر اجرای بندهای مزبور، به‌ویژه بند ۱، و نیز مرور تدابیری است که برای اجرایی کردن بندهای ۱۰ (موضوع صادرات نفت ایران) و ۱۱ (آزادسازی دارائی‌های مسدودشده ایران) پیش‌بینی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/129602" target="_blank">📅 20:34 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
