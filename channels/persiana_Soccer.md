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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 553K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ0v9ovUfAqxqcvK8roBfrKC3L52A4UjnoWDdTInLl1ulSAJrq7uuXxUnftPpl-7MU3M0Tlza3W-sNLFG53yKIsmOOUS06xsU3DcjFzWkWUM7jWujsJQmBYuAckM1cHIa-5BGv2upVzmkpaUj1p6Xb5gKE0RS9QXlqZ7L9MVV35IV6Rn-BJAMTpCn-NbbpGypY1RSz6PbBKTflArbn3noadlODambS4r2ahEOqv7Q06Z9WAPgueWqrFKC4cbh-aGkAe3SuIMJx5wFJ3viBK5P-s2F6MuIPACDZ_4_0i6q4nmctjwhd1L_TY9NTNXMVl_knb_tId44kgZ4YB5phiBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZeTN5MrJMXgARW-TzZznfoYxqIrvBIIlOlSGc8scUPfI8-kED1v8dFpLJXDD7oqLx_dK4Keqgbi8xcVzy-eVlglEqwRyggo1ZgAQNKo5NK018vffRkcx6mmmz14N1ExxERRhbooVSLi5zUsGD3CCIfvbCZOew677OO4i0fP8hzn0eKy-21KBt_MTEb2mBqRSHf9JrN49ZdGBbZfDeOpgZCxNTy9A7kOJvYCBwoY2gj8y2AjJypNg54ownPyLvwobMkqqlUWKNFmOdeqzI0XBtRpj6YpRBuH1eUKLOtiq7gCFIswvLddm13YwH2zhbfI7Ddm63560i_JiAnsh2ADAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Jg4nNuwtWZ7HOpObUjAk05EC_1APtmdRdugAydHI2RNvFsDsNSO87ejxAbTdzaSeFfGqDWhqukqyZHg0SPEwOI_oXndmseMmuIMdQrzza_CVqxsPCZCvmAzOfLVOqdTkjn5kUtjIbNMEHb7VrdgpvO6bYyxcA6I2uK6HY5Hr1Q5EpvOlDaawoNY0wrAFSSx77TXOYrrEtfBe1g-sNRZLNjH9vjxyjrj4QVilzm9qsXFoo7L6iRsN_DN3Nc4Plb7RJxaxWII5R12Yppo57xuNLGaYZoldqdeuDHWa99qVUBKRan6d2dKpsE3SgvD7ce-WQEInMm7nAdOBhak_qOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdFwBPAmTSiZEgpavRRZzWR2na5_l6A7rkW7OegCTlXpaU8po4ir_Rk4OsBUJZdVJjycquv94I8oUq3aguXZLzvBhi-n94fW4bABu2UOGzeK5hFzE8Y1ajCE68UyJPHWpMuVNS_CZpmYfpkc9Pa0kjFktZHHHeHuqKU7mxosmgUAhI11EAe3_r61K7HoZUuySDW0rcMdOAcsPbWy4HZnQmgMd5grfzxQsec-SR7fMnRZn0MITF94WsV6-wGoR3iEHLNCxK54ieZMLY2UMU1ikzTK0tI9TyyavMELqJwSuni3-dkjAuF_672KYiodpIi1kSXoODJglIjcvr7Q2Nze3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unGyYLy6hAegd0GC-jM4ifYQqQlkZZzCb9wncQTe8psRzl2BzsSAFMoVvEoJwByGWwHoyBcJdlggTQMdrOTY1lumAG-Js9D7jhAm6qjtO-GB1csbCwnzHMtlJN0ERNFbGCBSHXOsCCYsQHI-H8X3w07DV0okDGKgw1oto6FD8s8NYdrutBDvt6OEY89QnQHjg5OUB5yL_0zfDneSOIY956ixyOK5Er8Sp0u5VciecC_InVnAMMEH0wCJrtgMQFo0cX2t2OdjF60eOd40jHkGuhAHt5W8HTljr7AeuUHZ752nDIPdcDz9w7iJl3z089_RHl4fHf3NNsjLbr_XTk6ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9TkAfOOzAWELPk8s1n3Bpn-rH3M6TAmSpM6DvFF_mDnNjTYOXFORvp4SFJ7S22uH6gTaANKFEvGyaNmMf90DoFRdyFD9rYXt2J-A8EWQngkQRvFPmqAvgkU2XZmkRK2qM0fs-0PVnvxVg9pCV0YhJNGJYmxyPBVueROIM1uHvPmZam1CG6BEeosxPSnh3EU1Uk7T1nzDvch8a4HGQf-0WDH2N4RBxbmWlXnlt-crKzrgCGlDBwfDqy9QQxzFF5cUWBQtCZMlU4zLMWiR7NziBsDPCYtQZYnnav8BVb9CiHr0aaIBCsXJ1lqhdzBfIl0WDmTThLBgGgiraJaB0AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwc-7qyEft1wT-ndxx_hdiVXCU0qBnUEGoxI0WeZ6DX8gpo_OdFnxMb0oH0SPn6vAsZzpyYRxn07UM5ZR_1Kll5C4uXFn1_TOSEiNJytzTz8nvnw3HICAIwgBDPNo0PbOM-LV8qHeN1w2moRgs6YX-WvqmrPSD_iJ1Llo5CHBdt2xvm6VIbE_oaCH81VP1u18fsIFF87e0YnEjg6bgHTI5Zc_x1EyN-5kKj8bBFe8qhqPzNksleGEhzm-MnhfGMJEVGe2y4i3AHcvVhbZCOPn1182OuBEHDhK8WzcVGeM1lF9mADv1iDUkNAShR9HqC3xh-Zx-4oF87zkNY23yBtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5eIEcnWQA65ZIy67PMpWw0HZnTE9hCnE8pQlf6JXJAuSk_YUw-e2_1AFXGSmjIeghB-LsQSdgnAxPL8ZBhgs-u_-accrEXlyVAKdZD8UIfXn--5X-kxSWnudiPIIABSgq9X2OqC-t8F6zsh7IEFbP4FpWoaFgkV0wmwOoNjwMhEUOEsA3V-G7eL11qj4lKo3MP3rjxqYTvy0HQZz_gdGtrNgtuJpJNDQCunwlQBRbPIjzYuAhDcEXdDzV4JPUTpNTKBmQk5CeqPuzfphG4DjFa2fqKzXgiaQWDPc4fPsiEzGLevtlNuwKyb1DakPfyvivAR4Fod7Vcu1JrodEPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_dIvFnbwakqCFLH7qW6wvDzmdsrvW4ykxVMshkBi14eLfeUQg3h2wUAGYN04ON9Cr5Erx8MHNJSEJUBUNxpl8gkJdHjtMR0OWUhBRPtyfIP6vcAIq9JnApU0iW1WDSzPSAa39Mon1qsg3pdht5bkZCQb_bRLPixBupO8nNe2jWvAVD04e1500O2Uy-4I9sEbMTjJVztChlblPiet_eDrSPvcvlrY-eWk9kI4mMYwN-b7Rqa3erVsSi9Fun2EVv1Xugmk7WlGsNwMTPtGTYVYwY-AugnsKJw52HewUTw7PocsTFYVIf4PoYQVrVeCFZGze818lUXO_XspeJr79olWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1c92XWqokyFO_vcLOjnIm881no_60acVTJMrVFl162t4wksD-jb3kc1YVOtyLBGkLATeyvqb_ySc3gTwTeZXJ02qdqVGamBYK1-AYhyraKmMrvMQhGs8S9_OmNCoaRU178FAMMT8LEbyXKsfB9w5ibUgmgcxFBX6NH2Qvtq6fvMPWSmzqbOK5J0xC8xTkoOMPnbvLnSaZfGL1rR1wsMGtAPk5KdT4A28amamqq48-PJWVN3i_3mJ77Hx9yL96Cl7skg6TH2-kcQ0KyDgSncmM9YutT18puJABT0Wa1HJJyZHX-YPkGJsJR9uGgwmtslFhT3v-YCyHKoPQWfuqvoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/26359" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3aD-yQv_td-0dLRb9X9WPIU1t2oNZLJNoCX24ahDb3HpNmX_Oj7Wpn_MSEMAlFDF6BG8_5JFgREiLi9ZTMf2_0X43eXETJK8Q2jD3EBJq97ayIGPGcy43jXH-PfNqOxrDkBgrFc2OY29Zuuq3Gxj8KuHYYJc0l21B8w7fz2cva4xW2PjkRherWaBAFX4mO0q4bcqmd-z2-6WElQRdxIk09FH5ryCly3Flwh_q_tFSk2_7t1BqFbx8h80Q9zxG6-eZcYXqZLOyb0RMDyqA9wlKqpHR1HUhevAzQHMLH4vP4FZYbAAT-TbOwcAmaVyO2Q8Xf-HoyrW8k3LWGFkn_p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2jwoK0cZc3hik18ZHZRy7TlgkbFS_OG1KUxBxZdjc6o2OY14MOWGbGyN-uUU7GpCNeha6OQRyhxtvc56EYvaExFG9CPHT1ZWVFBUETuNN0313Q7nvxfjLeeIxoGOV9nJ0kIfftFKITD7CcO5wyPqwFYAoiSteMomWVez1Ys2Y2cWEMRb3QoJT_cwTJ47_ZZoo3AzSozFObHeW-EPnhgbdhVXrs87JSLHYySMZzHcAgceiRZGWOSOrn-BUdhRBHUdKhvH7DAtlQXYUHG8eNgezi4XTIs9F43A-hpbQg5QcoXAc1WGc_CPR5N9XzoD86xhOMlRjDnuRmAaPvtMe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3hsx-5lUESpKLQTlj8idWdTVFXDTttmCSflYHDt1VR3pW4QHnEu6Ww1cbq08CeE6BASxRlcPR6u8fcxY1dBfr3cdMGf7p9zJmim4TUKdi0BPkzD0ArX6jWQua1cnvbNfrLzTPbdHaC_4kcMC-Ab-gp7JjeqcixIFnK7Y8YtMs1UrbiPiIavuFhEi2MO4By_cckpWTZuGVK8TcLOc5c52CJ2x6cQzF2jGqHO6jGUA4CTlYNqUg5tJ7vBXo53s5GJ3GbGuVz8lXroHCHl4J645xR2KoCaStpWcHEHdZmUlMQjvxvj5-dLpQA540KTD_ci5r_x7P2DWMxQfoyHWSUc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwT0W9ddS1AN_HfBzYjYAFcGZnwtA2Gg41d4Y0aOW1vICpgsIv-7kiBpJtPxsRit4xuPDMcf4D_WAXYv2eFEaZDSqcSGjFg8nrZX6rSAQ8U9tBlOMit0ZlrTjUOMLTEFD3P8g_QG0u0dgBvlwEKnxLIRWwMTeCovGSYyIW9uW-72nDZ5CIC44JQVaJ_-d6SsptDPPNH96Uc5q_D54tjHdpkQPfdqQnoEgBdOwUGT8yBGKM4h49Fcy61oHaZMFBKn_4wnJIyA-7gRoXEDFIIcurjmTw-wEz6RvcfS33Cn5Glb2IZ8L5-K2zviyFuIDgNlPs-7Y-URnb1q2XMR6bv3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJJbFZb63tFVSKU_S6oS4yPXsafURms0CrcF_5A8rEIQjXhxLhbGAj-ucIk6QW111CmWXlcj5Q-6d1fSJ8Snp76mNC4VkF2QmU-2wbOvtWUMhvl190cKgVFgVewBG-V0qlJuUQjdrv6S8DYiEWIrX3R2aJ9VfO4Z34790s6TYx921XVIrNYyjyPfVPTjFwwS_fEadmNymgpAkVKhjM7Ey8qxg35Pudj20J5zecjfaK9ZwR8X-67pnRBjF0UiUznhsko6lzVIGxW_eEnJ9Kak9qiMxpGcg40hHlr6q_RtmzMt2Gc91g7ntsSxvgXx957GMjkT2aFIUzWPhYcCcATpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT1fTrPzu4C_PhQM5ozlU9oNZHkzbbUsD178TQLukRksm9ARnJ6Wngptn2IpJOOs4Rsm8gfwbzI0QCWIF5PG3H3a2dzxXNrKnIHFTsTc_oiXZVL43EwQDFySGul8__TwPgxqBhbo2ksc8XlSkTc6MNbLJAhW4HP6rgSf-o8LYqeK-1CJfmFlufxDsgXpbJxL_91c0LaTpdTBVUqwUldOCSetjP3TFNQSCj2RnbOE2CLpWa_5eW_32h0_-kqzcOF35BYKd3j7tfaM1nHElxeAh4VG17QFVw7Bey9o6HYF43jV95P5-XsQ0vdNKjkAQDp_BoYFV4WfqhUBiUzWq8htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhL-7w1TUQ_33jcbFyVaTyHSpO43OwVbkXaT16pg-m9LWn6KBKmgE_PVFlXTiawy8RZetw8W5DwysSWNdhuWzGvThaM8oyUm7Cbff4aDwOMm7jWqnNpkByOu6HDOWJBdaYvaMrpbvfCiVuPg2botEwBI_vUM3NX2DVgz_-U2LNXrGsRfyCAx4k1np8ai2ZCBjm1rQjYRVwEAirhEonOJ4xcQJorBqYrVSVm3gNDREFIgw6mRB_cS5N1Cn-qWsLkyyXxgMLgNlk6hXDTGsd99-jEI-Sx6DijnxulP0G-G_96RJXPQfPh03snrd0LY3W7KxZdH9vtrPj2TYOYgzb-euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3uSNg7L8uWofXmLPQTIWhn7Hl5KVvVUv6BjrrP4vdv74YopVYBmE7_OVjp67gpiyn9Feims7H2-oKIcAPLZNxpXoZVC5sPPo68XyKMVIf8vHtRSFnDqg_x2k64ylRVmd-pWiF6lQG9sUBhhdbOhV_imejhnvqmVu9zcHPqxdsRe8-RBvIRuNbw_OlNi3d0S9__Xp-K68bvB6gTdKgFPICZo-HZOJBBP3Gn0UnYCv7xozKizOJcOCx2DzzRtUfy4-j5ArhMxu0rjUxLqZRK4uxUlfSWqEPja7JaOcdQW359vykt-G6OuD8ZhRB4ALcRzcK2GYjc_k34uXVJDli4nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIHrhGH1pginezTNwD6O6DitAxlxUpWXaKBuAWsCNxgPPGeno17E4AdUFatZxq1gSEwhbQc79l6DX2PxccafKddqN2j4gW27vwzqJN54gPqthDp4j5A9fVdBMuXrPmZC0tDrFZbrqoQtULt1bf_0juWz7EvsVM_8aTcnijaT05yqO8dBYFLHCBnoua3nM6IKnTWNIA3-tLyPg8rgM_43vvLkeJDmfuPaaXnYuHymfh1FuuONm5lQutLEQCpXl9zyn16Kg_Qlh08b67ulxzvff5h2hWMnNwKVJrgMEhSL98FeJT9HZcPfV1TTZC_-0gIT5Mn81jS1P6WUVWVvKbCyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=pydVBk0ADnsnIUrxxp-u7BVTGbNlidMTlFjX6bP-DTz0a32CIGyroxZO3znCnu6KlhibnyH--XcxK4na-rajp0kRAAZOXoKwOJGeBiKIGk_py-PgJFLw_81e7sF6gt4JTqGM37C1L3AER6IDJExcofO3RjJh-6WN8ihszXa1pudjEscv4o9CoYGG_gkiYabIF89uwywEE_X0zK9TCsktK88vslEq98xQR1gpzmilUPcdEPzAFW1sP_WArcQGwHoirGul_ZxzVhdLNVNSk1yJnaxXtPEDVfKuedgXx4o10Wl3BLxE-8A6amI0GOJD-0EWKf8LKiWr9B6v_E_haqph3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=pydVBk0ADnsnIUrxxp-u7BVTGbNlidMTlFjX6bP-DTz0a32CIGyroxZO3znCnu6KlhibnyH--XcxK4na-rajp0kRAAZOXoKwOJGeBiKIGk_py-PgJFLw_81e7sF6gt4JTqGM37C1L3AER6IDJExcofO3RjJh-6WN8ihszXa1pudjEscv4o9CoYGG_gkiYabIF89uwywEE_X0zK9TCsktK88vslEq98xQR1gpzmilUPcdEPzAFW1sP_WArcQGwHoirGul_ZxzVhdLNVNSk1yJnaxXtPEDVfKuedgXx4o10Wl3BLxE-8A6amI0GOJD-0EWKf8LKiWr9B6v_E_haqph3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=ndDpqp2OvORSkB2oX5xu--GtjZiyfofmleliz6KdasIocIQLAoc0XTOGEz7n5U5lg3RZI-MKgV7VRiJT7KrJzZgCdOMU5ya--ZFeEYsiAmbQIotDgoYBt84kaKkpRLTsxZX6FD3h7QBTeG_rxNA0KeCkCv4vnlMSq-Y_4DXCpDOWOcTGi7FJ46sld1qlU8LE5Z7D6j2F11WbVBmcMjOwJ5l1sYdiXLhWFLRZPKsuf0KEKOt-40rH1RL9-Qn4TqbuIPjpJbxSat8UIi57jR5npav5T3cLK6PPCdluXhXPvah969No6g96Y3G8WqhiSWjPqMW5LLI4UJ-mGImxXNfPSJj_KGdcRSs328jFfOrrmHZ8L-h6IjKfKwaoObxAct1jgtk60Tdmg6BFt_G4c7Kmt7z-K7qcmXsPka-PpdfZMdzmLFd542M8wAHmGk6G_S0wu5v-GufMUkPM7ar-RhXQBguFSeQxTRw5J1fsetMlF9H3rwCXOLYIIq0OS5zAp9-x_mbPBOJ44GBZ0C0NfzZYYccZgha-BVQwEVNXZBKr6WgnARQxuJFTOFazriMthbTee3ZF2sObGixzEjC6-wUJbl2yEeR1BVHXKgfMzRK_OGNaw16Ajzadg_Z0kyvN1y_NSp84zaS7XgxQJwtquC2ZYcC8_CIfDZsZU3JehRPDtjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=ndDpqp2OvORSkB2oX5xu--GtjZiyfofmleliz6KdasIocIQLAoc0XTOGEz7n5U5lg3RZI-MKgV7VRiJT7KrJzZgCdOMU5ya--ZFeEYsiAmbQIotDgoYBt84kaKkpRLTsxZX6FD3h7QBTeG_rxNA0KeCkCv4vnlMSq-Y_4DXCpDOWOcTGi7FJ46sld1qlU8LE5Z7D6j2F11WbVBmcMjOwJ5l1sYdiXLhWFLRZPKsuf0KEKOt-40rH1RL9-Qn4TqbuIPjpJbxSat8UIi57jR5npav5T3cLK6PPCdluXhXPvah969No6g96Y3G8WqhiSWjPqMW5LLI4UJ-mGImxXNfPSJj_KGdcRSs328jFfOrrmHZ8L-h6IjKfKwaoObxAct1jgtk60Tdmg6BFt_G4c7Kmt7z-K7qcmXsPka-PpdfZMdzmLFd542M8wAHmGk6G_S0wu5v-GufMUkPM7ar-RhXQBguFSeQxTRw5J1fsetMlF9H3rwCXOLYIIq0OS5zAp9-x_mbPBOJ44GBZ0C0NfzZYYccZgha-BVQwEVNXZBKr6WgnARQxuJFTOFazriMthbTee3ZF2sObGixzEjC6-wUJbl2yEeR1BVHXKgfMzRK_OGNaw16Ajzadg_Z0kyvN1y_NSp84zaS7XgxQJwtquC2ZYcC8_CIfDZsZU3JehRPDtjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=Bqc4MiKtfrxefudXyY72JiArIMHpi9YoEAyLteh-OuL6zH-KmBgdRmkCQt17NjfIRpDY6XVkHSkyqlpeym8rweKp-_3UbQ0DLCKzBsCBpSWEwXiRmG2vjIkDRvmaH6SMfp2LTPwZzXX-SnRMgV-S9VYzAVgTXd8CXuW3bhPp4tj2IxfND7YHd8nO6-sPoQc0fMWYnGt4-SxFZtWdXXm_GJPTW4JTKHcZ8voSojAxk5b9khKXlTybpuQQlfLWbwhIIhVv1h9QDCoc_ZdAxBq2ClRkOoCjRsW3NIklebZWy8v14_yI9HIodrSXSwI_gHUv4pkEaHlZXhFplV-IbyEur4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=Bqc4MiKtfrxefudXyY72JiArIMHpi9YoEAyLteh-OuL6zH-KmBgdRmkCQt17NjfIRpDY6XVkHSkyqlpeym8rweKp-_3UbQ0DLCKzBsCBpSWEwXiRmG2vjIkDRvmaH6SMfp2LTPwZzXX-SnRMgV-S9VYzAVgTXd8CXuW3bhPp4tj2IxfND7YHd8nO6-sPoQc0fMWYnGt4-SxFZtWdXXm_GJPTW4JTKHcZ8voSojAxk5b9khKXlTybpuQQlfLWbwhIIhVv1h9QDCoc_ZdAxBq2ClRkOoCjRsW3NIklebZWy8v14_yI9HIodrSXSwI_gHUv4pkEaHlZXhFplV-IbyEur4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IucihwlKirDlbDR4OqJHNka83Qx23r2kw83tTPsP7B1af6uDtPIln1PsxWwi1FVBT3ZGceOuAUeIv54iU32mB-tkc3oU67T-EXRxsLDuelj_8Ub81BNuIhE6oBB15PPeyHyBEgL1M4Vbi_URINfuUmVv-UoSUwUDONMXvwJb6gydyIpmF1feevnxZ2HQsRnlC2lqRKwxdoUnWWymUGbC9D1tY8ws0HfedynNoAEsMUXM6_Pi8PoMZXeSH7dHbs_v21miJF9VOWfvNxcOKVXHQdlWVgX6Og-q5QLJYBKDuJwtLat4qKIhgR5DOMIIr_MHe8iTaCQnCwg3FuCY7Cedzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=osDbDpjdhdBAXyvZ6mRE3Vt5oO-85RKPuS2BztkYJNU0rZe5FJyhJb4PiXXacZfu4bQzUfXEK-KNiH4qNacyrLI6BlBM2aO1R-zWqh3JqGBamh3GrPrEjvlmQA0ziZdLFA5rMhp8Ic53QxTRvyM5ZsHtn668Pfon5hebtPv5VIZfBSSUAYR7ulmfttWfKz2k8WTPBIyeZersD0ulf16wFf-ot_w5XDmj_hugjoZ_DCbYWCKANs4Vt78_kfrbf5l_cTrZtp6ytldDbjQ20BLbcEuF17Wb5wpNMWAoQR6I7x10BO9IRYBZpabf6bLKGoiQdQNdR_usV6BIpeC14ua1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=osDbDpjdhdBAXyvZ6mRE3Vt5oO-85RKPuS2BztkYJNU0rZe5FJyhJb4PiXXacZfu4bQzUfXEK-KNiH4qNacyrLI6BlBM2aO1R-zWqh3JqGBamh3GrPrEjvlmQA0ziZdLFA5rMhp8Ic53QxTRvyM5ZsHtn668Pfon5hebtPv5VIZfBSSUAYR7ulmfttWfKz2k8WTPBIyeZersD0ulf16wFf-ot_w5XDmj_hugjoZ_DCbYWCKANs4Vt78_kfrbf5l_cTrZtp6ytldDbjQ20BLbcEuF17Wb5wpNMWAoQR6I7x10BO9IRYBZpabf6bLKGoiQdQNdR_usV6BIpeC14ua1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=YuncGC4ufwOdFTFSCrmfGl67nsOMQXrJ4h7p89e_qK2vco3FZ5xtZ1CwAX1fEYpKpJ6LqLdGsvfWM06WFBGGl4QpqPIGfBvJyu-1_DMJV2x1BDmd1BT_Qa-H5Ejl5Bd-x9g64LXeSF3YRQXzYLTk8Y4XhIFYJ0ZiZ2g-z3j3jFOMnP5rVe6QrjFluTNtv2MA6NGI8nIeWuJUm6vSyM9cwmvLwHysNtZ-SiNzXXN6kxobiSv5dABPAcOpEqSKXbVio14kdpVVhp8_p-mEwWDyglFP4dcCjQPJ8TkFa7IfL0uNOPsT2tATLIMOJNzE8tTKLBcNqLPhIA_0n2J98PdP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=YuncGC4ufwOdFTFSCrmfGl67nsOMQXrJ4h7p89e_qK2vco3FZ5xtZ1CwAX1fEYpKpJ6LqLdGsvfWM06WFBGGl4QpqPIGfBvJyu-1_DMJV2x1BDmd1BT_Qa-H5Ejl5Bd-x9g64LXeSF3YRQXzYLTk8Y4XhIFYJ0ZiZ2g-z3j3jFOMnP5rVe6QrjFluTNtv2MA6NGI8nIeWuJUm6vSyM9cwmvLwHysNtZ-SiNzXXN6kxobiSv5dABPAcOpEqSKXbVio14kdpVVhp8_p-mEwWDyglFP4dcCjQPJ8TkFa7IfL0uNOPsT2tATLIMOJNzE8tTKLBcNqLPhIA_0n2J98PdP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnOOgSBjK1dpc5u4IwWlb0wwP9S2NEZkjG-AkEkBNUAUs2KYDsNGRurgCD28pLO1WUpQOrIQJ56nU1E1yUzZHcYs6889BwmAgYiDqWQ4VTt2_bNh-awDX65SSdx9yV0sYvyepmX1lHiImPNowXpWd6KtRLMgZFN13GPYqgets49O-rSq9vnbdI62oDOvWWm0p-mMm05slgQ3Eitb7tLfA2AOvCnbRhm5qAEmnYwZiUmpk0vB5CmOBxGm2v11XdKLb0VJtZ-JN9o7TvHPyGdfCPfKxibh9t83mjdF9QhqXduH3kvKjtKIA5visav-lkf7Yir3W8lkNzpBEZGl_8ughQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=d6yZzExyWPYq9_mN9J6Sf5J5xtIe9A3KurVjxXPomuvfI7srZyq1a1j9kK7iQrDuKxZRfV5sQSaPfw4UVggFz7hLBB4Mc66EBhMDiIs1lnSnVcVSY4OwiOBZTK11sNCoYVjo-iwx6gFku38lKgPIAfQ8TNLI8pNo2EJ-V30RqMl8l8DRjEKqI71TA5toQWhuxdGNZd93MsO0GNf1FeqZ1zUP82i6ST6cGaEKyvHzZFzCp1mDg3d9CRikULbalMWAESDLv1xhFFafUpNvPa7l7ON3JCoCVnjG6TYCWDUtTv2omHpxXvsE-w0X6pvbWHwp97J9Z86hQ-fMbSGTvo3SjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=d6yZzExyWPYq9_mN9J6Sf5J5xtIe9A3KurVjxXPomuvfI7srZyq1a1j9kK7iQrDuKxZRfV5sQSaPfw4UVggFz7hLBB4Mc66EBhMDiIs1lnSnVcVSY4OwiOBZTK11sNCoYVjo-iwx6gFku38lKgPIAfQ8TNLI8pNo2EJ-V30RqMl8l8DRjEKqI71TA5toQWhuxdGNZd93MsO0GNf1FeqZ1zUP82i6ST6cGaEKyvHzZFzCp1mDg3d9CRikULbalMWAESDLv1xhFFafUpNvPa7l7ON3JCoCVnjG6TYCWDUtTv2omHpxXvsE-w0X6pvbWHwp97J9Z86hQ-fMbSGTvo3SjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCOGN0g6remPk6SpBeU8O6ErtHnNbyhIRa7_ILAklz9XD61luApEHqIsHvnbDnbl0h8zrXRhmbzMgBNJiIO7jR6GeIaaXtEmFnvffTtnsG7qlAF1laRdjEblsexyipI5jhVogaMK8jQLByWk86mG4Ip4xlpKD_j8fnm7_LrZmZXKPErryuD4sR1keQIcArJ1YN17mXEmWV5U1AdGaoW5XGvohEFuIgPGWWNh8OBzTgk1gTjpGet248pPLq8JrmCSjV6KK4bQ2-aTmw-PlLEUBMNgxUmFO5bcgr9lUyyJSV5AW9fi6Y1-aSroRkNywZrdDRSQWei3Z7xT0JTIWrNxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUgMKqenCDSGcMggqsR4zb65TWgGeUGou6h3RUxOS2JCDuJjrjVPnlC_eF3UJDbZ1OPkeZAsSBokmZo4NEfEpMaq1bW3hOeHHQGqTDAyd4gZMiKGghvyLOhfSyfGScLIpMgIWfTLtrHmenUqoC1EXASgZz-6Rh4Yn9IcubRyF2LQMtOD0GXhKLFSObU9MTSdQ-qC-opxlfkMwvOtelSKkc3_TLNMUQiWZPevvTZoNL6dldeVDp0Don1PtYeQFDEBClLhycRKzfw_q22L5YoQNAfNYrD46Mm19hqL3EkVgMQ9XnP-DAu2H9BTRUMTOG_oUatwg3QW0-GkJTnrEAYnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY__xl_G1JuwFSFW4y7kaHD6AJ3rE7dnmBD6XBpIyYZmGpmWqQxC9EfiJC_qMYclCxCgL3M_CK9PnvuEVz7Zhp7dynjZrTpRogirS8i21ZOlbOZSZob5H_CvA22XIskhZ5GaxJjAngxYkNYp-rLo03WW9d9yddZO4aJJsPTMfmtgIJOZN569GbNqrxNi1cNfZVeca8c0mspT9y94rD9By149j3PP8yRJ177ER6_lmITL8YifgnSTopChX1MgwHrl7yqVGMYy6ai8o7MbE2_XSncvJqyTqQ1q7gNygGsIIWMQUWENLgJSzRHcYWQtkzMmjDcdSY5ngiLRY1sKPz1YYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp07UL2iNt_Vz1E-6g9by4eIaMRrObHH-V0BK4PDul0lIOHOAJAfxwF8tdjGKd6KWvkRx3jfprPyiqsAdzL7lQeqmNAuEt5roqM1XsFqNN-8aryogD53lstQfmvSmvOwr1fluW9bqTd_it_fPXncMPVgicQOGXsDph1Ng9K-fKo5jVjB6lIDy-s3ysnfXccNoUn4v9qvGY_CX4IbddwZRwqzBvykBSKNy6o8RiI2hWbMzBsf3gtGSiY8NGiDrHjn8xOxNR1zVnZ5KhY1AJKFaOZ7M7jpIQbqVREAIq9_1LXJh1wXnDbJdWPrjAgjb_PdKHWoLeZnGlAuywL5Kr6tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyAns_1ZyYqU7lUHAmASJpr1bsZC5f7fd-nZYR04tI7ufoUeNhZdVGu1gwuJCCDivlmcTDr8-R8AoWaJEsqb_so1cZn4ef4G-OzTbJ_GUDdImKFj0kZbwSeXMslepgXNkPiEU7AbCQ8Xfc55sq7dh55VXDZDv039GkbhkBkAqmKh18Mi6LKe1wll4ZnVZpNSeJkZVa0tKrbwZE4UsM0NO2BTVjwrzBVo3JwpmvMEHn5obscGL40X9sd2wpawX2AZmaV_6hOJXq3Iz-C9fR05pbY0TM2tgFHNGlVKE1zz_vt19z8r5l5Vlzce_IeT26wZMOLOGewWJfcNEsynbNXNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf-V4_xpv0M9QKKTvoARE8pu93A_mn7OzO2o7X4PE-BykWiyAcBwKKgoVa_DK-aIE5dEB-v01RmBKlbdED1qdr94bn9SYfW8WvljDPTJ1ofUklGQLOXuH5VOt-n6lzjq8OitO7C0hd7wBDsecg14OFiglT7p6_u7m4-KbFldX6RZ9dZ5tgwtKxUtiH_detwozeeBOVjUIhXYo50qP4ozfCOKjmhlW6yzRRBDpWBQX1zLt3eMYg8ZXVaXIcsQEIczB0YT5mU_YGaQQW2-lQM2l3UVIz1y6lgDLTshVmaQdtzpbUPCDVHuVECWUN1UENfcieKdt2xc07QDXo5GgQSZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhRlNBh82KgnFvsq0Mds5-YTKXvZXvKkdbWeOuFl1G2Ns-WiTEM-PbC0y7R8RM6fxRwiVNVddPIT7RFFBhMki3vsiBUt7NrvCXlgh2V8T_nHzrAUUvqM66twm2jwFw9cBCPd1cABP-bMBmP9QiUlOoMxqR3Tbq5S3KGakRWeG3OmEbrdWjIAAIKN_SeW0olIP9ZZagDwi6V0_5QB159U5uTkKTFDr9zPa-ZZbmPna_leeL-Tmiz7ke7mSkKj3p0XPfDXaikf4eOKnR8EOld_zpHKP-HPM8cxEUuK6i1uj4O3CFjSVivtOU8BagA47m5Hx7yUSuIDRCqw3DsktJB2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKBa459tKwA-GYJsfC5pk5Dm71iJFoYslMJvsDyvpTOlJFviO4j462TmjLhnmmtATNXjMv90HxvtEoDWDoLmjSFLDG4q13r7CKh9rS_V7Ptg8Yndmf4lXK126j5qCPvmnd84tXh1yd853Bw9qbcfpayLCGjCfjveFqxiWaS99_D_jd_noLCATqQsohxS2O2LfWkHvZGvgcfFyS01jD9ksOgpMGLsvqg-4o5Mp6OmWUbwwCAedGkShF0YpS-FFbCxE0ZHE3zNiTdz3_O1eky64DFgdk1jFSC3sYykSxIPRXTLQhwJ1drOu4mMPEFPTUSBXL8PQ9AXE9sg4JvhDyTWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YycWlWS5TfI9s19uNkcbPgWbKzlKbw0hFHXJef9HwmcuQ8oueNIoUGLfAzmTCwSfgLHJ9RhPjZmqkc7SeMoWCNY49vPiWoVFEomoOqduCw0xSTY_F4vww8Tb1fNhf-qN70T74NDdOXAguLOwFVLIUM-jEvby1n06bLS_WCwTbrFBSrfdsmIDLBmP9wO450hss2wSVhJp2xYCujtDAafhdqOGOE8U0oOTW70Rv_-c-7BYD8ztkYE3xBUsp5gb93aAYqjxCd1MgkWFZi7rK1kMx6H7gdhqWev9VLUx76QIPcRTyDlQEdR8c__tMv1aWbbuTFKZJkC4QntLMSEoXtW3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1IBArj17bjqbf-zb4WCxaS0qdsJk5rb3iguO0IWoCsZkThtkskfUsg-aQJAeWLc2KVChRwwECTbcZL3fSW-NUU69IEirXZfMh4LitwvysAY0l84TyINCem09HBy0UOUESrlWpHHqu_xGGDFH6M_YLApjzvZhkg5BbCWfYDdFOZ00G9uZNL0KcfYDiRrI8_yA4i-5132bj_0IzsUqn56EAl_3Q2hrbtG6qq3LyNsUTod4jptX5uJYZSxNVVXYh9f7zQjBxIuF-oXlTvkw8TZGiwc8em5j_BP7ydXvDsX_4eFt5_d3ydINKhjBvGR4_0c99rDXcNTUEByCUGjpEHung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOn7Lfqyg2_2TYE4wJEyjScUHHQNgLVvEcKGudMzkLb6fNCiLDgJC8cRA7illEqkLmqI4Vz7wF2ptU5IIa8fYGBhEHsHdsV8zidtY267jFLFkeYi_Gma7ZECuNTLB6x96L5qCGWhwP0znLDy_Tx7V_GGyLp_GuGVLTFFg0RphNtqAL2ZYaGAwn89L8G57jaU1bC8MevWLR8xA30iwbSpWCaECQluFSaq-wBx_DchdQp6fSk3OVDHoaIFOzE7DyIRVMgBoH8PJR61AfmQasrJt-FJqGvzZ7N-bbIdpZmJ-4hycyM9d2vFuDF2zrggqUPmZgNYyDlpKkZ0BWJH3AGVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuuVXyt0yqH3VGYmxuQiW0_8St12LQIeLZJqJ6ZmEjaRh4Y07UHTGz3pftjjoO_TXmOcEBz2aqIo8fOJOgYZZ2UMEFlED7vWoJEwOn8MnqoWLwiKDsKz0vVS8P2ygvGxESDNV9CueELJTVXEhnDnWVMu8abypwzDS2JK3Bv9cEPIoi1A0xFuRy_KpHIge6foQeS1L7MCcMMVQXJUFplZTEk3JbA5PA2TX6cV5F7fH23wLFMCA6ZDZpb1Qe1QQbyQliFrQS9YjuyjCWVEHh4NyByS98Vd088hTMXA83n-_YO2Aq9kgbq_lxQADkMDKy1wLW73Lh_8m22QL7QCoXUegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=LmoNuSsfkvwgvxX11LOa63xdbhunhGd1RTvvTx9q3KuuicnsGrZAzq5m19gnZRbQi2rPzj7THp_low_3Xe8o1atq6We4edC-gh5Q9fIoGt4XjLTcb6nkQtVGHEhJbwlGo4ey93_SqxtyDjRb3Ccm9m2LZWG-f-MUJXbX29JJmTqlHyqTTlnr8_UZWELJHlvbhlCjxJSHsoSigO2FjJKibnqT_83ZaVeRnblt5H9ZpQq483CpCFXigrS9wdVwPT0H2yqIx0LWimc-zD4PFstcrl9o6KZ8D-GsO_bRlMpNq4qxQr0RC6pXGM7NuiNRY9AHnIqHGlbPhAvr3vvwM0gfFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=LmoNuSsfkvwgvxX11LOa63xdbhunhGd1RTvvTx9q3KuuicnsGrZAzq5m19gnZRbQi2rPzj7THp_low_3Xe8o1atq6We4edC-gh5Q9fIoGt4XjLTcb6nkQtVGHEhJbwlGo4ey93_SqxtyDjRb3Ccm9m2LZWG-f-MUJXbX29JJmTqlHyqTTlnr8_UZWELJHlvbhlCjxJSHsoSigO2FjJKibnqT_83ZaVeRnblt5H9ZpQq483CpCFXigrS9wdVwPT0H2yqIx0LWimc-zD4PFstcrl9o6KZ8D-GsO_bRlMpNq4qxQr0RC6pXGM7NuiNRY9AHnIqHGlbPhAvr3vvwM0gfFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=MF0Uej8Om5W0pfk3Ce6XTAaKNoDKGnIydVynAHJWvVduL7ss1gEfuP0lYyhW7yjNQoo2haQ_3klv-irCt5Y591siyL90aMAT1kqetA4YkCt16-XbfmqD8Q2rE82M3lCpdS5q9JC52X9mY_ttzIQ9ykq9CDDGhsdmerT1C2rYr1K7QJYzt2qxQbvirhLSimZ58QRGI9S3nB8Mq06s3wCKzuZOfOFrKv6X9Sib2VkYNtcDCjeIKs-kVj7SIup6Enb7yRSe0-8__tAayqpBBUHjwr1fWacJapZ91aKyqyDbMkT_0W0KQKXHdtxWiVp1-EfqbkeNScf5YTIRpoBHaXuJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=MF0Uej8Om5W0pfk3Ce6XTAaKNoDKGnIydVynAHJWvVduL7ss1gEfuP0lYyhW7yjNQoo2haQ_3klv-irCt5Y591siyL90aMAT1kqetA4YkCt16-XbfmqD8Q2rE82M3lCpdS5q9JC52X9mY_ttzIQ9ykq9CDDGhsdmerT1C2rYr1K7QJYzt2qxQbvirhLSimZ58QRGI9S3nB8Mq06s3wCKzuZOfOFrKv6X9Sib2VkYNtcDCjeIKs-kVj7SIup6Enb7yRSe0-8__tAayqpBBUHjwr1fWacJapZ91aKyqyDbMkT_0W0KQKXHdtxWiVp1-EfqbkeNScf5YTIRpoBHaXuJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnOW7ERqmFBsrEhdOfzF4H_ta1NWiYxx1ev3NfvPlS6NWJKLbxhdUz1YClryLYNZZo023bPyb9hYH4SdwYPTcuLMzPHIWomE7Nvks_VaaKRdTDN9S-FM-GQ4s23sTsik6Vi4fnSbl3NE6x8eV-OSDm83ubowltdWGj9twbCalM5fdnWLFSCl69cnIJyVjkcj3Jm1QGsNIO0GNH-Eq9pkJUDmUrkXF07q9ev9wfKMXN_jpfAoccA5QbdmAXlwikfMdfMd3tU2XCwYPMBODG7mrXG7ARWnZmoHku6e2IiQNM-36IiABz5KC_dhH_W7d1vJKsDLbbWfk1bjn87YL6laVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqW8nPB3gk6b8E6mY84GaaFsMoNBf3TaD6xjj5CshIfbp8VGtLrhBR3WC6T7Ui_2_vMtwxXP8T0FLA2-iuJvtQnslZSqoRpVzy6-uNlYwDug0eGy_s6kOS7Vs8WwpI-xYMOXLqGEwVVUyqCX7ymMb62Gwg4cA8l7GejY45iGYkij6po5z2-x-L8kCUZHL2F9mPUg0-xqe48FvIu0g8zye0aDxL_OIV5_FNmjKFH2KsliqZvX2tiqKqYjBD4SI93eZOaGUd6NHthzUpsSPTSLuttDlE0qdlX43860DIZgEQczK7OFfYVuspJmiMnB-qOVoHghWQq9LYklCXylcncWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJNmJQHpqPhL1TOYH7hB4okni2hSr_w2iubk_NGkg558eWHah6kaU1v7WlzUwdPGSnO8UtA2XDQDPVhzIfGWWxURj1s8dpyL8kViPF5NyDE_Gmb4XbsySp-ellNCT0o1TRGupaqYm3cwOrD0zGGoC66vVvMau608FJ0J9oH5z8R6zI_MXvF2lqGR-2aVtjbxoT3mMRfNbsAY-YjgXi_4jybfyvQLVU392xdQ-BQFWYxOcdfoTz8rHYmKkV8JuS7D9WFxEr78JIuRMB18MQb0P_oqO3waPkvJgjcTD3AcIkjbyQeT_iJ_2fLiOb2ZvNFle65p_svItJchIQ58mKSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfg9luIPRcgVL4SvdiHdJCM8Th1s-SlMRfQK_uPOWovOC87hCxUMnQRmlqfXTqBo9BIf_RHMfhNfw_eUOqsvvpzL8IADO0HAEztUvfiTx4iNBA8TiwXYrXgOew1GER-usV_pfFyt-QGjCrQwGh9r6GQsQ-NIprW1-GEdxzMHbgc27MptS2FVamVkEsPtCknfOdJSIHQkok47OtMizpt21-187j6Y1qOIOePzXMtsXRPoR3tUgpzpREJJFx6lukGa6ByneSSJe2FUVha2jC0H-jIIlv4CxDuoxQ-_cug40EHQXQ-yvHsBp7Y4ZbWRybASp3D3VTn4lGBIgH9NI1aumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir6CrDRiA_AZxMydR_OmG1yjCF7f5Zr3DDSFPVJOKk2pgRLJyKlQlUKMKQvKh4vohAHTWvBB48mwxautL29HnbHTjYcC4aIuBQkhwYYnpCyGe0fOuXJH-RmIA6uT8DCpkLGNxbhDuwG1FHdDaT3W14mWokEX43sPhnQAnbTYc_NoNnDtvhKMaeivW4ELu0KVLtuB7R1Bzfe8vlqu86LeHuYAx-FFj1dZE-f7SW43ffo-A-LzZ1PfOQdk2x8JL1xHGUuIPHA07xBkZRVlpJszoMkifkDSd9mqoZtQIjGDtfFRmI3NVQTCZksN_5xaoSIJZA5jjX9jBd15_y7EcI2uOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6HZx4V0YH3qiCVIgH4bA6b7sgAfWSxl6dQAcw1ofolEvvn37Z5XQgF3zpGd1hwAiqdGF5zAnj3UOykuv-NNkMznCohiyvoJLbV44lG57c97hH_2-6lvDMxF-jJiGRoBKJXrq28nT3YnzOYuVoTCNppXKNDUSQErs58trhG0UhkDFYNq0xpoAh3-nMeuP6UfyhxroEu1k_n4YumMfxHunGNXKZCt2doNA3WllpCnitBI3dy09F6HawM5m-M89bjdkLbMEgJRuSGRMgTE-a_TAG8k26TBDdxvZe4gFA1n_6aZIKJCJTc326PyZdz7WOP4pBNZQQjkJJE03ZUrfxzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEi6ZCHxjdBOVstPYJ0ALyEdJ4yR5dO1DpCMHTpm7zBbgAiaQ5jyjrnShUtTsqpGIHzy8_QrAZB-d9udP20_beAmeAnKfPry_ySzyVV1PNwLNNJ-e53JtIRqpSKQzIBVyoL3E0S5qGLvEwi0HnV5sLQVBaMADoRNiWRCLGJyMcM-HufoVx51l_V5BQCVqTx4xkXPxotIF1vhnXlk8nYuk49eVgtUQ6GZMP5PHcWjKFKhTsUUOLscQkTBM5YUL7vIk49SJPZkXlJReEwByd9VNr91JLhPdhIpbfMlGgysav5wU7MAKww91UQphipmu6zpbnWCis7guXRYlfzB5o9vOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBX1ChFuyfoZ6xi1-mrSH2WhGEywaws0x7FPqnHCgv6JnC02wSUBIY8VIbmogH27gnQudIujXRO_N_OOz9h24m0Wuvo2w5qtoQuJBdcALyt_0QugLR42Bn39JmPy9L5BqkafrRJQTuZ_2p12zxpr29Kd42iwpHfqNuFEisZxwsoiXGhKYVA7sKek6Hd0mMBfcHPgQDJFJE07aCwMvO7gQo5CeCdyCmMaODkwGAkfMvwzdHru6W78orzdTBuEXgSyzNAm6UI6gjPTSaS45GKBds1rsZUqwUfyZx924DupOMnjvFjmldqaZwIt7rxVENBVtK7zQnml_9GoZYMx9XmXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6IfrQpgbpT6NBRjI3gp8ykMsyYGbZPO0pdqFL1xYRHM7t4RfJhyTBYr6wnj4DwuMvOHvYuR_k1oUM5yPvT3qDEecxyiH-Fhopsabe0NMHWt8YcHclSUn-dOoRZIm9D8tJ-GGq8wFo6X6TsLidWMe1eWLRgVJMMTYj6Jk-dhM7PYUnHlMiBQzXZfCYH3E-4SP4wGb64fQqBC0CMhnAuwGY-uuBnRpghEJu-7fXDAKc42zpLWKT8KVw2hCg6ugPezLYJEVvuAhNAEGbs3zVzTuwD-ikOtERx34887S58LB4dF9d-rCJCDHMOwDoCM3auzqEYHOzonDDmH3A-MwxzpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjUw775NHCrtEmeBYfMPVvaf6cUHbQqc25p-R_dtRSC0Q9uGm8GOlpkMVjFKywAKiVDveY8P42Aw-9TA64wv33UXT5lTr-HV7qAmKobE9XefNWDCYSDZ3Btj41ClMDZQ7ZQiSvQZay0B5QZhLLQ1MkLyLJA_GJirXp-4jojDVtMkrS6GmpuTt8Og5gOP9R0HCNvn2OqUULEi3HqiaCq9F9FLdckeLjN4Ykwf2tQWCKO2CWko3FNcKVyUc5mQtJh9GyRcwb0FQlFud5lDf6CQN-btfwjI3Zk_1EfPlSRUG9Nmu6P1BdbfnZtMLXXnblB1h3ywVQfsfnnG0nRNJo7wQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAJqJHx3WvK5ElCpUxrr-pzvvquknO4QN8qWtdjYgCA-ewIRDFuPOp0ZAOh_Nj6hnT-G_RzSA8RTQn87vQrk-ktqLnj4KrP0ryl3EgzHR-s9kyMe-mjKj0A4sOZYorQV5TSQ_m5B-nkjFXWbwAd3XBV6D7F2R41CGSt-N_7BRgGaU23IKyvdtEaI7k9In0mhfMmPhO2u3iDaDjPTwfSXhRK1Zd3sI65WOxGhf1JMYEm6iW_xzaF-7SWjyovAY0WoCK1bY402DCcycwEoVrfiWAftv9xSZgt0mK_DTx3CcuA25m02Ge8UncNvNzCzTPRSw-w90v8brqH5qwbc-Il2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMPg67UbXJa0VWfGJ0Okc4GA7Q222U2u2I8IYur1Wq0pA8Ja1XZK2q5xdisALZS61Jcpa-ZNx6heqIT4IPGLbox4ydSZdhB8Q20F6-Sc2j7-WWx1Gmxu8g_3zVnQ0W4rkXaBe3nkKp-N_FGG82X2ZZjKB-1skV5v8HZafmsLcjJn_9ZlX3FbAmrv7a2KhCeuU8ZTAm4xdjykZz7gllKqX-q2APRm7OfcEsNAs5VnhAHjJrvScKsLQOKuwarkWWhsOhgcL6BQiK0damnKh1X8diyk7V196_jmjMri6ws4_NnwkUsgLq38F4LJ0KET3kAomf2augXaHW7lwBgKmA51fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sepek2SQfZbRcAXptTpeieXsasmHC_wCWBmz2CJHTtCt95jPfgwG5lMQ7TkrRCYHYHGWgdgkdOfIPr1kuNxdPi-KHbqLH0pivJQWMglMXXdKzcmVN8NKy3ABAZ-lTz2pkwRn_5emnmBDolh9TBec8p4Dsbq5JVwzJ_PlYu4GA33DsD2MytlPUUkeg2zRQUy3m2DzC_7zskmdKYW5BBTeQDeajvS8F0r5l_ZNvA8U4WR00FAUUCKx4vVI-JGyJ_dyrniJEhu_X2F98rADsv2BGgblnJn4pPZzOf_0Qd6Zx74QZbQzCUNgdhMnFP2yKpJ47zDWhA7PgNguHgi0-rLk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBlne-l3SIutS3Ag1oC59MuL2dpuz6JJkttmtXD9DsnJcNlCx1h28IBy5F9JKdHBVo5CrgxuLRiuvSCtJwAFBw5J0jbxNM-Sj2Lpyel1bgZ5h3j7Jd6JXWoRsUDU-CCzejJl7b2rZ5fJdCg7T0NZATrOsv0aZxTKAYKmXP7GIynjwskPQD-5vN6MkT0-KimoniPbPzJVOEs4pV7kkHqXB2Kr6pJJIhEtEM7DK5mNcq0oaoN70A-i38UvMk19Jth6Nh70PyigFDpo7ycVYLJFxKmXl7tKU3GApA-19dVQoODJNrGnm-GadprXND51iRbfrAH7E7AfSfwChtSRXxXR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCZUoUwjwum8qIT-M8Y9z64ALuYhJPwBGGf9wXLkMgiGVLuzajEbWWp8nt3kSqHS5OhxLkDq3XgMLQdAimBcPt8e1B3749fHBakWzPj0RDQ3-9FR6XC5X99o6oupmcThbd90ioSw90Q0jnlzNzpG61mEkJBA4wXiFoKPn12RonlxPecN_GJUDDyDfmBpmIhkrRvZaU2wz1yolYkA-VImBvsfNiE7FT_PVNYMvVnrSGrpT7CocTG438jo5FJzx7FIcYcsrTFVFCUyxoBQyYCubTEN4Ro318tIjnQLSa3poFf7OaM7C60PXi1c0n3ocxCZw_5o-O_DBw-DpBwD2_pBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TD627tmbscIWRPwfTJgu1ZT0u7a1qbVNh1axQppKhhZJFOhElHfNoyGOOgiNqISrfy4q0coIpckHS7lBUe-EXs8R51rhLbLJOr_Cwy_pMnHvUVc91e1e2qnjvxAsQ6DM9heqCDCztklihwTkRAEG80zUtuvNYTUZq9ymG9CgZlkuw6NaYmRBIn1qBUXrOldCYPMLjF-PunCuFmA8tY5jOOjTuxoLf2Zkq5pIZgWyETOVl7FS_s5YMTNaEnBCs030URF0IXY9g7qRZ1FXz73fOW_h3HfaX5hlmuHFbFIXPcKoLguGx4XGmWqebfFXClJvp3Sc9C2eHsrcOfHAzlHp0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnIj0zUobrL1bsIN-e2OIHg-MiPpPJqsQdzf56z4IKVokuts5YT8wbiPOyrPaJK1YlgbZ9DbLeN64Nt-6vhbSmbz2V5R5QHcqk-3ZRPfHJk5J40qp7vPvTXZQ1wwAMf6hTn0UA7B94Bi7z1XjJeeOIKBMt5FCAljVC-rvwxYu8GjtijgYuCZ6E8jLnPJB_-0TmBCfwwmqUUsTN9vwzKJLqV4CQGPBBYjWWzftLFmkCvPAxnhk0p7XJoTiotdF9ROUm89MAr4udFs0L1lLNKEVB8KeJgiSamnJvxIaXfVxdW_Vss8o8kSqLm-FsrD47rkqhfFKp4FJTrPyyOWxvmikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXB8SypnwLLQcVs_iyPMVpFiXv_8aNihrf-8cuEI3kPZHiuDp9NHh8-aAfcPIuRX21JTo-BeZ3NRjhBLeyG-eWzoqUAoIavNyB05tm5mxm-o2L99FREuxU9GKVKXfQUk5ub2XNFUNeA3nplGnu_F2SOixRCPglh7ioiRHH52JvG6gqti2anr4jy6weq6ov2hGzQKkAgR6_M8sYBq2WNvjTE8jPF96PNYFlDeSIPKBUQZmYRjZsbpB-Gj7khLBFxRBKCV9iVPnwV43tX99Y-cfg8CAdyfZe0iwdzbi0eVvt52PHPY9548IFgYRpLPk6w9Xcx8ewCYu3I7gkBywSRoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPRlXDWSWe0hZ4JiavUJIUB6M9pVgVXQPAQKvEWA3Lwt1qVfkljF0rSvn0GeE7yK8VsQJQNpDZtXX6q3NBhv-b3FHnEByVFDARvSN0VqfF7285bxMf1ZhvEDnHfZ2b_EdV-aCo06nI_musauiT089QPAwcGNNlUM4FKry5rgWInlttBPiLe96LRVibn0RXpjtUMO23LdJjPYCQ4gWDteELUaWex9yPViTXRhXPp9iQiF47ME1wHBBnczvQNefmVJeYKVH3x75u2GJdsDF2X2PsIyk0zX-DysY_nB3wfK7FpvUiafGc6MizMJVmOGSYQyVBSU18-MBZ0v7R1eQPikhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6dGSDJtLgf_R5IVWFGnKSa2JJGrd4M6LhB56VrzHasXimJANZHHC36cKHRnK0Qqtf8OQnCVGDLLjLFO4hESdMW4CP081la57m-hpZMFHVeuhlK5Vwf1ZSpGnQPeIzPI1u5BukeENydzhgRqrYkGrSl_dgCvSeycNZMrejKjq_GKQIq6bOxr22Ek1VkXbMKrYJxU0PaUz7kZQAFQJCF6o5AFqVOrIbwYAic8FU2pGOEe7dZRVzmlQjlDrFj0eskPFEMlMg7ab_Fa4iKeM4g40awCPagyBtx-8etL3tdP5U2kQfI1pCOlaYeogg89nwUeQ6YhnYcJCv1IQpLfd8MSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKNLO7aRJRi45mPwfsQ8RqBgI65Ung7VvdMTvAplfnMPR781sP4qwjq8HZqvVM8plEo0UYhcWvJtqnlNuzaH83DJoReetUrYYdvFLaxkPvkkkpZ5BRNTNAFHHZeYB9xo4T8zD18grYwV4TEZ4OoRNLL2UZ1zwN0hbSQ72XTAL2kcDGNjyCGh-Qh4rEnYDOvu3mXct4Y36txg9bgEt6NtVuInOz9Pgbz8nWjZOJcObZYobXsCxEOoZPqMo74K1VW3z1dJwHY27wvmVNhI42Yyq8rFJyBzy2sE5ppTzgDKJa530KWnPp44ZfuK0IHdCmPADKd6PnyOcdxGXXCx_cRKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0M7Ao3RrV83Yla6WnWFDdEz2Nc_YWnSt67-wNLOlSoW6IJOMuXZjWhlXpFSyYp5MzsPcXsL0pVQOv-_W4L0lUPoD4ZpBsGTB9E4eBRfbxg2S2Tr8cR_Zn7wVja6J9MJvjbgI9cpnh9g5uQRs58y-XuOOzRjuVk8wpy-yZ6lKi_gln_Uz3bi0ed5g5ba_rOiB4L5HFl9KRsC9Jt4V4qWLYO5n-QUmhfSfOViVMTNCXXPb_HTNf4vq_Fjikgp-JeP43sGHwoIrKHzzp3fJuy2TzwrftQ8sm9nuYHpT5ZENYOrMXNkD16Pur3XEISyxA_7ngPSP1fIvawl3mbU_xhcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDZwA-joZBTmHxgnUrsEKFXaHeSZwsSVMJj2eqTpGghFU_jiZcVOgs65zUeGx1vGD4TWHsQL7ZiUtXw1NpivTkbFt4VLV8MPjsCd0w7Agp7VXwiK7J3iedF-zvlI7ROGz0yQBUzX1UezJWhYdZd34iTvLnRRBKhZprnh-6TlBvb430HKjbCoLJOwOYAoeUw2BhGgl9hUiX9GSRmRfm2hEDr_UwGJeehgg8GUBEjKGln6_g7B8mOzou7-h2W5U1tYOF5xiHc9JlKDk8FkRiNAJu484P-vFxRRTUcXWZMn3iLTbsOQqoc6sMgJPKGh0q4Zqj_mCormKi8UbS_SEBWGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhn7WN8sYipWQox5c84Ou7taXyQfx7xGpgZ0z_RhWH66TIp-dOgMJ8ZaBIP8thcoIaKFcfRDlm8ooBvHgvbiZ48SeCaCdLqlF9y9h4BINgZaSdaVBdZRzLOOAMogvHj8sHLXhxfUU7UBDaP5DuL_0kNl9GQQFRDF2DP4xe7oNy9wQkq_bk04YWOfsmg4URXeFtIKqdqp0y4PHdFfW88CU2y16OMwNfp1_H4uc6AyzHmpL8PEyiMpiKCwbyNhVccyxEYgoa2aaJx9wynyvNiM9-jpzDGX9iX43wjoJPMBrdQrL3JafuDCIXDUIlswQQyolsOfOTHkx3qfTWzi5sXoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtyEgkGyDtIGMZ7GIxm7QgIbz42mzZGk1rzUvywaHpdivxKLkwiSrmkGvoKWhK9c0KoO6ThOBvSv5c_OLMJ_AEVaK_n-57RE83HoeiPMC943inWXXMfOo1upJn81EUT4fyTvX8NsLnMFxSPmRvyQGV9HRbK42iF5mHuDNHzdMZCLFLt8WlgLHlU4QDfExB3nXP_VbAiKMghpMepIx0cqbbb7Q7PyfeDbhP3MesnOO9tvPCbdo-CfMfK6S66LrB3DviGEMLBX-IX_uupTnogg3BQJ126nmJXthm5qvBPR5PraQu4_BdZ6_4a2tEhUZRPbGuZz46ehxhFYXDxEkk9mJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB6hLLQKRx9VOOAnFuudAx-gD-R0fQk_BZNxJve-5h5oOCkKP_VDVvgiVL4LjEuPsAO5B8Fcq2tFeIP_wD2MfErdQ4HQe5TUOggEy5davlyYRCGahlk3SBeNpsXsR09MHFTSLSw0dELDu4jBRBrUY8vxzFi2X3QTujP_daWHcIXd1QPtN7q0xj5QAv5hToZNgZRqBNgGof2iZKIGbUrn1iyCraJRcRBwwVUt28ok119R2A-UOuP3pduQrW5uLtWOY0GIyVB7ZIlfnszFKQ1lHDssuUnlF9Fa3ldOMDWVgoIC8jN4TOx5oIhbnsJes--GQSntEPVnvg6e9gKUohdguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PStK2wTDxYrY9ELuwmobS-DzwnfyfEGKggh5kQ2xKFYD2Xg-aRKBQSmxdVcsclqa2C8Bwje9FoajUx5GpqRMgF-bwEP0EMyPhvIBwNfXkGxyFadeTqwBhkgD7zb7l6A13plBnKUdXV7v_i66IZBL91XBLnZoYN9SBko1DZl3RvuH7KEbO9IlFNrBhukO6XofSVsdBwCuFHgt6Ls2jJ5AW5hSEdVL2GtoDXUd505Eojn3M6qLyPjKpQvTIl4ZMGKyDeoHD1XUT8nhWjdA-epn1QFRNbWSQ6ULK72zmE_JX0TIz1IicJquN6eA_7tGlUl7uaqZWc2he4TKZP_Y8VmwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4T2y_aADI6nImoFevVX7J_-yNVQ5mpQYkvfiMjZ3Sy0r0HGZQCx9ms7p5NnzgdgF_-Md2V99Ab2elR16uV9mrpm3RozcbGX-CMsGN57JLBbZdcOZKQUFnZiSdzAmEt8hex6-8BE1qOlEfZ-JmlOKhgyoyBb7PoKO_2Kmxpw3qtnxYvn2yI4i3Nh98iJ1Zy-P2ackNh_E7h2QnXu6jLb1D-d6Fa6SJAwaEBZyF6_XaxtU2lemFuSufwxJCA1kVuhrhhNjLlC_aPpo6StT7v7PRgg_W9RwZOZ-Z5NNPL3AFuXQqsbjzhQ0WLfB9BvK-ZSY5S4FbAfIMfkRJliPBlOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTKwrTG6auuhZ4gxvQbqP1jYmpF68EAvr_dN75lDPI8Lgm3GpuJPApl8v4X24bOS3V32_Xs3MAoDKOsHia0Rxkz1MBh4I8SfWNEJPgGQVqJms_ZnNAJGrnxAxmLwa0UQZvYqDvUednMSwJCdRjaLify-t4GwsxM9erWEqBiAR6BcF0zv9nhrbGUxspmMFkjqcS-JaHkLRajbacWp_BbiuXpb1S-meL7Ayw8mVKny54dYaH00KE9aJTBjuojBwgYhFtUP1GcYUkvb8cj2lKAoselCiUjz97wxaHYIhb04EqkJepO1wvJsVgXlL8fkYrzZUlsnuHTLPvQJOOIBowtfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxMYmiZAraEvkfW5IyoloDU4mMm3n2mfpvEfBjqaHkVVh-rpsQZHjr4lJhNtds5rVuZmUH3XR8K_FD5rLyWDa0S_Xs9KdQHmpZI8S0I-CYIVCPvrOhAEWd6BSHOOxcyuzA1j7lysW-eoKXG_8U4D1Oof0Ed25KQ_dSd7I1wmKjh9wZsVja6E1RBqU20P7oHqoyMtPmTNRXUc7PfVb3Y73azuAb4UIYL72M5xKk_bMpk5kcnn2EN_yribvCNz5hYVz-JurqJGYLh7AuGt-JV07nq5IB-T5UB1pMOXoFEUgksNkAFlbCkT0WQMdEOgd0nMbkcW3A2vJsU1PcNqBCa0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A65UcljDxguIFojNj96yt9x97TTTJtixx8u1TJHnYG5dKT4NhoaJND2XF_zBzFWeAFcFyT8iHBH0BFtIjPNMbavEn-xA8sSAL5PdOV7df3ZkXdRBIXrEt6pxwO-LTZG8EZcCUq4JxkEQUmmHORTZvaIUUN44yR_gUZi7sNzA0fZVsULMb_I_uTDg304XCfm_f40LFR3x7U6du0KqqfuNqbj8QjFNnFvhmkZlKBPO1cc-R4DdnqR0_wFO4zRbu9O8S_zJkFcmuyTG-H9vPFEJqjZaf-rB4YXQOe7K7ub5Aw4cNa7vu9uPTGgTdI547M3qnxAQoSY08Qn9a_aD1Pe5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgVmrmYZrJHQaeapchJzOxLOTPd-PVkRhO-Xzfkyb_Oiv7LaiRqtk2bCwGLVNcKBzmy2M60kmIE1q7zCG9DI1zUf-4k7iF3i8zVX8opjkFHO2nZGv-5f6yaMLZxTxEIAIx2vHMX9Tg6eqX4Yi0F_f-QRAXdVJ4gemox0XQTGKHeErpLxwMhQA1dDC8OBHCKEM5MTLz2sM2mYRE6XKrg5OXjT4O_-n6t07SbdAzWxziBEiwIXwOPYmFOfFsEfHWceDogqHTcc85YTwy5V_6zjx7D02BmO1-S9p13NLW8jXlSxyFsgJdV9actR7U68ijifgVwkch_U2pJJBkmpR-evbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=d-L2VmHy6OqlsjqwASOhUsj1_RsQ7QSeI96XjQyQbm6hZJxP4SGHrlq_4rBsZg5S70qAW3CmXOe6nPxo3eHkXdc8b0NwMjKpSHtH6PTKGKrGbu2sp6ER4CMh5NwPeqRGwhYUZUqWcsE0G71zEqzpzwZXdPd9pVuM_b19owL7HxbRHRKQb0qs1oQqAjHCAdXW7NdBZ5CAguus_Iz9NxqtRwBvKna3mNNEiQlH2nGeUCrJQU1LN88c9y3Nca1wYgDsHn7Q700GOA88125hNulP_r6565lgWJ4PnpQ8xRhqoXgWKAdSfJBuTsOBLjDa9nsD6iEBfMSvX-OGZOWqDWIU7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=d-L2VmHy6OqlsjqwASOhUsj1_RsQ7QSeI96XjQyQbm6hZJxP4SGHrlq_4rBsZg5S70qAW3CmXOe6nPxo3eHkXdc8b0NwMjKpSHtH6PTKGKrGbu2sp6ER4CMh5NwPeqRGwhYUZUqWcsE0G71zEqzpzwZXdPd9pVuM_b19owL7HxbRHRKQb0qs1oQqAjHCAdXW7NdBZ5CAguus_Iz9NxqtRwBvKna3mNNEiQlH2nGeUCrJQU1LN88c9y3Nca1wYgDsHn7Q700GOA88125hNulP_r6565lgWJ4PnpQ8xRhqoXgWKAdSfJBuTsOBLjDa9nsD6iEBfMSvX-OGZOWqDWIU7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_TDQniQyfgtl2RLRZ3jbQCLWZNTQX7-RX87SeJdciU3jQD2zaDvJSGj3X_n6pg2T3B_QVh-ddyvw3TdoMw2J9xXhTPc0Y2V2CGKZocYoVUEzoUMJSyGmLkXGDl0DNSmwK3JwoaNjuMAsgRhw1ROC7H3DD45CkcdIB3ncNsiXflN6oNmDatdSSPMsm0Az40mVCd2ODE5WChAek06N_InevsUduoUZyZso1JOR6JEaerlIS5ESC_bPvNqPMthhJExp_e73khdE5a1I5TLKcYht5TBTg0nFDyha1EvDGQTqX9w1rTeRUgjtF4yBf3IxS1bviiGtBIpUrDdNiPExGHyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=B8WahVo1RNaQWkL4YLD3NW14EKHmplTSWvRjls-pijidGw5eahsRxYRgRTLww56QvikJ7XD0ebJGz52OBpc3nYmYMYmfOUYOjoNRVE_XAHYzCErpDW01NEPcQBfKJwsIlFcTcufpKNHzeV1a0OtaRau3AmG15JBLDPyeoSp2B32M33TBKJA7JzFlHFJDXZKfa9Xw3UIW2ozOqZ4A9WOVUKAVHFskgilp1vm1K8DSh4CsXo-Eqa_b_-f8MqOSipPM4INLz6gBxX0htBylFDveV5qPNft77Wk6ePZ9_dgSXMZ1vW6_6IV61lIO58eSe0h0BBHsWmPhYCEctLlhvoC9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=B8WahVo1RNaQWkL4YLD3NW14EKHmplTSWvRjls-pijidGw5eahsRxYRgRTLww56QvikJ7XD0ebJGz52OBpc3nYmYMYmfOUYOjoNRVE_XAHYzCErpDW01NEPcQBfKJwsIlFcTcufpKNHzeV1a0OtaRau3AmG15JBLDPyeoSp2B32M33TBKJA7JzFlHFJDXZKfa9Xw3UIW2ozOqZ4A9WOVUKAVHFskgilp1vm1K8DSh4CsXo-Eqa_b_-f8MqOSipPM4INLz6gBxX0htBylFDveV5qPNft77Wk6ePZ9_dgSXMZ1vW6_6IV61lIO58eSe0h0BBHsWmPhYCEctLlhvoC9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSAgdzXEQwlxBL5yj-PEAdcMTBYO0vPIeXjF970deknfdv0DxGUvssNfRXpPMEbqdP2OKbSIKAnGN69N7dN96DGQ-R2EbZh8XuP9e4_OsKcYSP-bbG8j4NPwCLxqynNrxpgr25C0DuqZow6eVqNUwT9RshCBmhRkFFnmpalkEiXZte-zc1kPmUoqa0Bma5l4Vxd-f-k_pB_BxL0_TzvAgIYw0xnmKdDRZ1c2JMlQ-T-p_70823YDcsVjmW8pmPOR_I-bTT_7p0c221vYGQHiffXVvOGZ2IbW9nwSxiQ35i5XvIeiXnBX4pIm5HQqjz8SLepnDU1VCZLmgrdC0y-RKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPKxjKuTNqYrGx-ESDNRaBq91t-ybsGyknIkejF7bT5wgOyFi9tqjr1UgwB_XyuJSjR9bq5nEyq8DnODT0WFZepttC6H1xInrHeZSoF6xy71b78p_7mqMOWKJDaHiFxbCeFH_OHMYTScKMsYwUlUZjjjqZvN4PFOSAjGp3XHqqw_sYHrqpKyQV0V-nSEQInSc0o9061DLYqG4d40Hb7Uc1-pgCcF5MLpxJACQXaCJvowsXOQGFQQMX55Bb7sDudnuLkxt2_gA_czF48Is1aOsw9pz2Zh4fy5oxhd7VdyPjFzor3yLJ219tjlZkfq0s7l66zz0aNqyinmUSyvPkNqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ahj3PYAl3apQ4hh_ZqMmGu9j2Y0gOKzMyf9C-trpwY-IrYtxJIx404qrsqhV-2UFAGY3tZSQAMvNyrNe3Dy89_xgWI0c1tB4QWGw0g4bteKitDh2FsCQnOIe21WMcbZU-C3OZncg95ftkuME2OdIzX9g8oD_rDHAvOXWvc6_4ZG5bO1yseaRN-2Y839bwazzx9HkpeN3mANA70we9_44nikn7wSU0d9zXXiJjLjrJ4c085hYEu4lIrhkD28LXabJprF9LlxqP77TL_Zz7cld--P1srpqY6WcuZzkPm8pFxdf784VTHHEowumlrRJ6PnbNLeQ1qreN7f634YR6EHn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ahj3PYAl3apQ4hh_ZqMmGu9j2Y0gOKzMyf9C-trpwY-IrYtxJIx404qrsqhV-2UFAGY3tZSQAMvNyrNe3Dy89_xgWI0c1tB4QWGw0g4bteKitDh2FsCQnOIe21WMcbZU-C3OZncg95ftkuME2OdIzX9g8oD_rDHAvOXWvc6_4ZG5bO1yseaRN-2Y839bwazzx9HkpeN3mANA70we9_44nikn7wSU0d9zXXiJjLjrJ4c085hYEu4lIrhkD28LXabJprF9LlxqP77TL_Zz7cld--P1srpqY6WcuZzkPm8pFxdf784VTHHEowumlrRJ6PnbNLeQ1qreN7f634YR6EHn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
