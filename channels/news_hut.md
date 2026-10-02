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
<img src="https://cdn4.telesco.pe/file/YmqNIKjdIh--LI_sOAN07dVg4VPClKAAHfZAWQDq62PLwbYs2lU0lTtHtf1Kc9kb3BdCNLS_RpAy4BV9OFOs9iCKiZr38F-z_bHxHhmz0J_oB2tKI303t5Z0VWXbMMyeUG7lWOuJytFOzD93UxHTRIPBnLXze3tF0yOC3R4isKa8DwuCZWSX6AQ5XJS4yWxM3WOuMuKt-PeTMIl3u8XBESYQTAzve9XlSDxyf-CKCy5s6xbj46F06uz-8JZYdFbxivJQLj8L4qM66ZEvIT21u23ATjd1chxIkHi473gyKLRw_hM3BIws8TefpE4KJxXCZN_l88vSe3JQEjt9rchuYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 03:23:49</div>
<hr>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvMfrXc7HIJy84Tik6EuotH_x9DJRYqj_kxN2CC0AjJDG-JJj7YwTFAEzCW2DC7-aWI4oUQkwHfdFNevnE2_V2O-Lwsa_1aWDwB1bNtC_Z65G7ACUieeDUGHNx1lAuYt2pcCrno1RR-YnPIe_DWHq66XKV-3gA4FZLliWaKkM0YHlIKursW0pGpx8xgf3Eudhn0laR5kjdXH-ig9HwHCzA_BOJwuaBSiURR6B_B-4t4qSzVz1kDRHTl2y6Wd_8sz4y5Y_WU8jJAVh6gLvL-OrpnflGRC066Fm91hgCFvN3PtbowtaaHRdzLJTsAefX1jBK29V0IYoAivbekXY4IgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=ODk8vXW78iFasQHDP8Mo4wMLossu0RdbQj_nV49WcF1bCdBkF1pAPhjEYN7yQQ8k5JxxUcota4uKEaJ82lQHYA9QuHx3CS34IUGhOCJ_Kl-q2jnCDqN38qMz06tVvw23-8M9bi8aZFWVccTuUBu-mJtGWxHdCoElmQRteRuJc42SWgi7BNGHQICZP4TvEynhtOJ3CYTebIYItEOOhYS3XmgclZOByi-tiCEGJCiC3d1DvqrBvCWnZv4bPTUdz8AzygaPPa31vUEiqA7i41S4AAUgd2NK6fFO97GFyiZnVkkt5ftHA87aKOWpq_Yf6tYc3j2xd4HNS62osYSdE5LPRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=ODk8vXW78iFasQHDP8Mo4wMLossu0RdbQj_nV49WcF1bCdBkF1pAPhjEYN7yQQ8k5JxxUcota4uKEaJ82lQHYA9QuHx3CS34IUGhOCJ_Kl-q2jnCDqN38qMz06tVvw23-8M9bi8aZFWVccTuUBu-mJtGWxHdCoElmQRteRuJc42SWgi7BNGHQICZP4TvEynhtOJ3CYTebIYItEOOhYS3XmgclZOByi-tiCEGJCiC3d1DvqrBvCWnZv4bPTUdz8AzygaPPa31vUEiqA7i41S4AAUgd2NK6fFO97GFyiZnVkkt5ftHA87aKOWpq_Yf6tYc3j2xd4HNS62osYSdE5LPRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=YRDvwxR2LgDzZaLjkTNIxz7bQOtljJrszvnyF97S8sGYkAjg1O9DErjiS0UKa6svoyNbIL7B1d82jCNmxLqGvVlnSOg5S4It6j_qY5yVULZTkOE3DCuu37MWlqXUH20-Ng4Zwc2Xz-gDLHh93p0TnUHf7TO4WvDeVNlyUu-szz76vYTw1ESKqKatm5CCc0kXSZzHEFV0DBPCjV9VVfL_r6ioJwUahiTPx6n5dFL-AAT8FAmmZxp5jLgXsNb65pkX31xCdR29bdNGkXaRZs4NqM2PxY7bVxg6EMvqv6_K_hRyl2fk72HhJaLAaQCTK2BdMOCn5m-KaU3pC-z6e5MvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=YRDvwxR2LgDzZaLjkTNIxz7bQOtljJrszvnyF97S8sGYkAjg1O9DErjiS0UKa6svoyNbIL7B1d82jCNmxLqGvVlnSOg5S4It6j_qY5yVULZTkOE3DCuu37MWlqXUH20-Ng4Zwc2Xz-gDLHh93p0TnUHf7TO4WvDeVNlyUu-szz76vYTw1ESKqKatm5CCc0kXSZzHEFV0DBPCjV9VVfL_r6ioJwUahiTPx6n5dFL-AAT8FAmmZxp5jLgXsNb65pkX31xCdR29bdNGkXaRZs4NqM2PxY7bVxg6EMvqv6_K_hRyl2fk72HhJaLAaQCTK2BdMOCn5m-KaU3pC-z6e5MvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=ZkEeQCj9TL2WP1LOQrANzm7YO8fQZKGTqWf8hgZvzyJ43Q1zq6EpizPZ4uj6PBgN2jYPhTJ6MAmU9afO1VwvnDS8pjQNxHU1kKR-lGtdn30H6QEujUjEE9Cnx-WWtqsUKNp3hjlAwuZ29l8ow4FdQ3N6V_p46Zr_VFwAzu2LAGTwz9-9xVNnL9_3AJWMyJq7DDQQTfxcGFAOLQ4Cx0Mc7sG4QWrP0_HSWtTdAMlKgnNw_ESNoEU2LD-nWlOL_d4ekdOtl3onvQUKqKJ-2878OFRA63OD4ZBqz6vLZ-1T6XEArqUFJao1IjdnOFgJqSMTc9amSpMssN5iDcgkTaf-1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=ZkEeQCj9TL2WP1LOQrANzm7YO8fQZKGTqWf8hgZvzyJ43Q1zq6EpizPZ4uj6PBgN2jYPhTJ6MAmU9afO1VwvnDS8pjQNxHU1kKR-lGtdn30H6QEujUjEE9Cnx-WWtqsUKNp3hjlAwuZ29l8ow4FdQ3N6V_p46Zr_VFwAzu2LAGTwz9-9xVNnL9_3AJWMyJq7DDQQTfxcGFAOLQ4Cx0Mc7sG4QWrP0_HSWtTdAMlKgnNw_ESNoEU2LD-nWlOL_d4ekdOtl3onvQUKqKJ-2878OFRA63OD4ZBqz6vLZ-1T6XEArqUFJao1IjdnOFgJqSMTc9amSpMssN5iDcgkTaf-1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=e-r8bggTmkZ3pm52xxkezNkjPn0mY8QJMEVgNGIbxf60-9jbXDixdxaGXtDavA77AA3Js5BOGP_mrZF_W8ZTWdBB-xiOlV2gjFDXP7m7DqcAMCTgZARmFulvfWF0e8JocQuCZP23WpwlqOQI2vOgvZ2ZnssByB2eX2pF9a5VtUJyif5VSqxewIOcuGm08BPvnfSnAfL8jm5O6knbCkPsTHYpKPk05UqH_sx3TN1rUf5DYE7grsebZXi_kwQ0KuZiuMvLW7GZlEBQitxQdkxS86naMQwQeXbHBjuAVzv4zfBQ_n5I2KcX14oJoZgGyWss_oX0ijNqfeRPLHL3VXr_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=e-r8bggTmkZ3pm52xxkezNkjPn0mY8QJMEVgNGIbxf60-9jbXDixdxaGXtDavA77AA3Js5BOGP_mrZF_W8ZTWdBB-xiOlV2gjFDXP7m7DqcAMCTgZARmFulvfWF0e8JocQuCZP23WpwlqOQI2vOgvZ2ZnssByB2eX2pF9a5VtUJyif5VSqxewIOcuGm08BPvnfSnAfL8jm5O6knbCkPsTHYpKPk05UqH_sx3TN1rUf5DYE7grsebZXi_kwQ0KuZiuMvLW7GZlEBQitxQdkxS86naMQwQeXbHBjuAVzv4zfBQ_n5I2KcX14oJoZgGyWss_oX0ijNqfeRPLHL3VXr_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vqklP_ay8My2JC-ik5G1UJTT68jqUiyCJ0eXHNG3-X6G1ocSRCue0i1rOvv2oPUq-Epif-hZkmxGjyYM1sB49TOG6ebxSoWRpPlrOpU_a5zjVM01uG11SSSDuc-l-WKNGLcp278tdj6ollfvKoCWrlFlUDEBb0zGGrA34iovFAY2mqu0lsNcu6j-BdHOSjk8qPepn3CZsO1N-vIdrC7NuPavI0AGce806m8_BegQ6t_pmIM-EX3_REAmwcqGCN5ZDkXTfWpx7JyTbqSPSDcV1n1TIuv4QWLVsroGzUsHXeZIDJte0U0FPoNa1h4vmDZwgXyi2Hv45SpehPeiizLXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=R8MXJa2FX84Ti20IHmAPhZsp2ZDpd6--8SZ14cbT-5c46G1eDEIkBeMOtU7_7UHt1efQit1bnd-iwVA6znQ5KQSqyk9FGllD_jlfAdMY0XlzhbILkoCQ6N0knzY-0NKmmnVfosBTBM-UpVBuSSYIggntJY4KuiVMpGBc8yXtYkXrlF5M2BbEN2fGqQ3zWgqMSpeYER98wYnAPYD5xtrykr0Mcwty0Y8MN6uonX-CIExmQZf3BCe9vCXv25ZOjtohw49-xcDGRv0Lv2-yAEhT1KLVkO3IrxMdyZN6avbl4HkRUpUu9VmyRTBumojvevEmqvfb8D0j97k8Zjts-snPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=R8MXJa2FX84Ti20IHmAPhZsp2ZDpd6--8SZ14cbT-5c46G1eDEIkBeMOtU7_7UHt1efQit1bnd-iwVA6znQ5KQSqyk9FGllD_jlfAdMY0XlzhbILkoCQ6N0knzY-0NKmmnVfosBTBM-UpVBuSSYIggntJY4KuiVMpGBc8yXtYkXrlF5M2BbEN2fGqQ3zWgqMSpeYER98wYnAPYD5xtrykr0Mcwty0Y8MN6uonX-CIExmQZf3BCe9vCXv25ZOjtohw49-xcDGRv0Lv2-yAEhT1KLVkO3IrxMdyZN6avbl4HkRUpUu9VmyRTBumojvevEmqvfb8D0j97k8Zjts-snPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=gVHt6U_v_YP69XMIwwxSMK3Q2hwUNpD1zWOOFCQ1sksJKlI8vzZ-4tD648p5IoRBChRE0-if4dTvTsfW95yGc43ONnis9dT71TzV2ixYcB03ZhDdJdRP2wwIK2MDwdIbg1PBSlKSUqz7Gm4VN1_50CPgG5H_oiM0R4gi-vlGgCn9p5DJ3zqkAfgjCxJ5jZlCVaWkD3StQgcUZNfxlPiOPxZbDA36jK-Ya7kdw0H3My2tzZJSfshGb6-emHKtxQUxTVNHtndgFVct2xJOW5p_cK2Ae0H90_30mCKg3a1Osyjc4vQCZDq3EvovfwvN1yezAqr_BlkuBIqMkMlwduULj2glsvgaNrGqwI4nRuU6EV9xlf2vZ0QiXiGbFJfpm8MZV7wiPZo950PXJU8aI63f9AuEWw2w8_5PeBiqynEdJ7nETYeBfiBz7Jd2TlARzi1A8xFrVRXgfet4vrviw5iCjrvHCLG37HggtAiVKzwJ4JbgsuUMvo4EfvO4LTcEpEAspW74b8QSvqc-lZMoBmftqDUUiuJGGpcrSXcmjDouME6MFStoAo3K8LGvwfoTktBNQwnLxWmEn5ErxjVq5sG08y7eF_FyuQK8MTp8xO_pTAZOWjoAast8g3gcvbT8I3iWB7ZNkTWMu5L1XU16Dh4eouoJPxdZeTgXV6_ya10gTxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=gVHt6U_v_YP69XMIwwxSMK3Q2hwUNpD1zWOOFCQ1sksJKlI8vzZ-4tD648p5IoRBChRE0-if4dTvTsfW95yGc43ONnis9dT71TzV2ixYcB03ZhDdJdRP2wwIK2MDwdIbg1PBSlKSUqz7Gm4VN1_50CPgG5H_oiM0R4gi-vlGgCn9p5DJ3zqkAfgjCxJ5jZlCVaWkD3StQgcUZNfxlPiOPxZbDA36jK-Ya7kdw0H3My2tzZJSfshGb6-emHKtxQUxTVNHtndgFVct2xJOW5p_cK2Ae0H90_30mCKg3a1Osyjc4vQCZDq3EvovfwvN1yezAqr_BlkuBIqMkMlwduULj2glsvgaNrGqwI4nRuU6EV9xlf2vZ0QiXiGbFJfpm8MZV7wiPZo950PXJU8aI63f9AuEWw2w8_5PeBiqynEdJ7nETYeBfiBz7Jd2TlARzi1A8xFrVRXgfet4vrviw5iCjrvHCLG37HggtAiVKzwJ4JbgsuUMvo4EfvO4LTcEpEAspW74b8QSvqc-lZMoBmftqDUUiuJGGpcrSXcmjDouME6MFStoAo3K8LGvwfoTktBNQwnLxWmEn5ErxjVq5sG08y7eF_FyuQK8MTp8xO_pTAZOWjoAast8g3gcvbT8I3iWB7ZNkTWMu5L1XU16Dh4eouoJPxdZeTgXV6_ya10gTxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe73pjQiiRg9_yZDML463Yq9ogFeP_tEfXxgWtSAEE78U3oVduYURij0KVLumG0oUTtwFoVqgxqNqXuIAb4O05o_sy7MzcbL_Q6jwyZ_bpJZEhgUzX_QJu-WxapD6qeFvTMXI7VQpr_ERsThyBuzTn7mhQDPYSDNBbNVNvPU08T5oj5t_d1N1wwJuTL5SzV2CGQ-CkbBNElNKU7LwcDJnXMiXA415M_g9H1jC6QD-aXYKUcZhoO7_AHkYTEF8hmt97oqTA7_c5XAr3zO1zrlMkszmanhelLuQCNz6fCHk8tm_jQWpSKJoPCl-R01Ad0M7E_denxKwKvGMkK3lRo92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=KPOV29ZnzXP-4AOcTcuGVgXldj_8nrmKZdr9E4dMZl3nfMLH9YR3NiEG5oDjLjcmFAiIlZ51-hBuZKlgint3KBrFKwV1K75Cnm0BsaYnJ9oxJhE3Cbt1jvujy80zvZBKa2OmX4N8VSwNo8KuddgU7Al65_W95Au2NCJDaA_TTm-m-NyHnvZCXAFSOmOJtEoXVUDMqRD_HTyer1eiEc8IANh5ZBe70u5QgdpX9tkLsE8LQdsvgaFxicYCsDBLLilmQUm88-guvTJvSQXKj7VxhoE0eOCOwWPFLZHBeMPosMH1J6sGK4-DoZcKM4M4_NMIJnVcPW0-JoOJL188JFcA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=KPOV29ZnzXP-4AOcTcuGVgXldj_8nrmKZdr9E4dMZl3nfMLH9YR3NiEG5oDjLjcmFAiIlZ51-hBuZKlgint3KBrFKwV1K75Cnm0BsaYnJ9oxJhE3Cbt1jvujy80zvZBKa2OmX4N8VSwNo8KuddgU7Al65_W95Au2NCJDaA_TTm-m-NyHnvZCXAFSOmOJtEoXVUDMqRD_HTyer1eiEc8IANh5ZBe70u5QgdpX9tkLsE8LQdsvgaFxicYCsDBLLilmQUm88-guvTJvSQXKj7VxhoE0eOCOwWPFLZHBeMPosMH1J6sGK4-DoZcKM4M4_NMIJnVcPW0-JoOJL188JFcA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9yhuTmQZJwNLyt4c5uUB6QfQDNLPAr-8KJVdvbhxMCrxSZvJ8VT1SYfZznjdgCmAw5Kj1gsVF38rzCdLDI2FDJWwdrFK0QB0X0afLQlzfjSvWj68UBl_MXS8cMNpI95LUpT0G7IBZrD1CkFBE-daJwA76BKaoHwzi4zt6N4WinaP6SBr1UNqsdBIFDe6iTlKlHIQKuLjd7pQi85a916KA_ta_CRoSGVTMo1hHg110NctTbe_NDlmFXFVGuCnFzv2XJHGBT3ygOpWl_zpehHNfJJuJG_LmTuOFDxYiCR-UrNUbH7iGG2nKmfv9Zu9x4frEKad0GhH8CFeH0p8uPnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=eGXKoK0tP_a35y0cxJXcf-oczn5SJg5rV9Er8DS0GS8aX7PHZb_Ed7AhSAM-uTxfQvWKvOv1kh2t0fyvyzY6oP-Zb1u4zguoh1fUlU-tPYFZ2rgfjw5N0SSwflu_RZT4LIThSVpuUFKaEc7s10B-XqgU8CShw99hM_mCSvIiwjzQEJOno4cGzIpdw0oxx3MOHpj2UUgfJLtPUlF33-FfKir8jhHJi27ybyck6ygatvQaYOT6DvNWBritx-jryowjG42Rqzi6Rr51X1i-NftAcY9v4HY007Ndxoj7Dhfh09soBCQaoFCdex3w_hqiKEEj2Q04hun_AC5FK2X3cIi2Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=eGXKoK0tP_a35y0cxJXcf-oczn5SJg5rV9Er8DS0GS8aX7PHZb_Ed7AhSAM-uTxfQvWKvOv1kh2t0fyvyzY6oP-Zb1u4zguoh1fUlU-tPYFZ2rgfjw5N0SSwflu_RZT4LIThSVpuUFKaEc7s10B-XqgU8CShw99hM_mCSvIiwjzQEJOno4cGzIpdw0oxx3MOHpj2UUgfJLtPUlF33-FfKir8jhHJi27ybyck6ygatvQaYOT6DvNWBritx-jryowjG42Rqzi6Rr51X1i-NftAcY9v4HY007Ndxoj7Dhfh09soBCQaoFCdex3w_hqiKEEj2Q04hun_AC5FK2X3cIi2Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=EZJ_K1emhNORIs4qj-R6JcDi5Na2MltRQ33rdaVS7NjOeHwF4bFxxRZZoq3C5pz57DPIi1lfS9bOL5DVz0zmFhrgblb497vwNM-gQ2JRb66SjB1oVbzKfSgb2862zJ6gMGsvbxOWlm5fNk16yZzzfdAyyNm4xLFiZ7j2Lg7lvMIoOSyfhJLk2PdkUV-vn3MfCFeWuNG5eKWYqOrV_TXELXXgdyOA9wA7vUTIjQotzZFsDc8g_i7g2rXqxYy_X5uGWpBiPrgCpEMf0ovvY8-wQaKHRF1AnWiNGqW3krX30IK2dXU3xp0MU01Txa8ZmTvzVym6MF-vkwWltF3z9TfBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=EZJ_K1emhNORIs4qj-R6JcDi5Na2MltRQ33rdaVS7NjOeHwF4bFxxRZZoq3C5pz57DPIi1lfS9bOL5DVz0zmFhrgblb497vwNM-gQ2JRb66SjB1oVbzKfSgb2862zJ6gMGsvbxOWlm5fNk16yZzzfdAyyNm4xLFiZ7j2Lg7lvMIoOSyfhJLk2PdkUV-vn3MfCFeWuNG5eKWYqOrV_TXELXXgdyOA9wA7vUTIjQotzZFsDc8g_i7g2rXqxYy_X5uGWpBiPrgCpEMf0ovvY8-wQaKHRF1AnWiNGqW3krX30IK2dXU3xp0MU01Txa8ZmTvzVym6MF-vkwWltF3z9TfBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=HOhzxWLQhPkgvtsx_vY2aDHeIc559JmFI8zIoEmqoJtEXfFRffKtmbvJZokOrFfFfeXy71ljD-159eMhJasPJXA0hI7ptrxevBVi3cGLlvWoweCcCo5C6XCGpWP_mMQnfLMXB93Zixe0anROYz-loeLRC3mNS_9vIWzdmcwudmiVkuO_zJr3wTsWf5xB88zGTFE0qlDZW0wIvuiYjMBhvNfIlcM5M4oqz24VD8a6Y1Svk_1gToW4dxHyN98pTkbCO47_UnvjHH8bXitUaL_ws20aLG3pKGpBfkzpWadWQKhUoqWlfFBb29xs6Qu-KLELRvxG4LuX9zRieN3aPMyYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=HOhzxWLQhPkgvtsx_vY2aDHeIc559JmFI8zIoEmqoJtEXfFRffKtmbvJZokOrFfFfeXy71ljD-159eMhJasPJXA0hI7ptrxevBVi3cGLlvWoweCcCo5C6XCGpWP_mMQnfLMXB93Zixe0anROYz-loeLRC3mNS_9vIWzdmcwudmiVkuO_zJr3wTsWf5xB88zGTFE0qlDZW0wIvuiYjMBhvNfIlcM5M4oqz24VD8a6Y1Svk_1gToW4dxHyN98pTkbCO47_UnvjHH8bXitUaL_ws20aLG3pKGpBfkzpWadWQKhUoqWlfFBb29xs6Qu-KLELRvxG4LuX9zRieN3aPMyYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=cqjygdbvakyKhJkUI9OBBxGenh05QzI1qxY1s6PC2ebwxiLnE4E-tTMshIIUFfni9D2FkNvJFoUPYCnVohLl5EdaxEhq06Xd68c9ecvXDCFIj4iSvwyjYlkcLVai2UQgjAm-nimNC09lOq7dgOD3NfqPCZn4L53-H89d8LcOB7vfU0wfqiZV1Ntmch_6XTF9icqcM4oQLYYEhxpyUzk0Kbb1kY1T28C2OGAI4zfJICoeplM0HB4kVGN2GlJN4W1bpk6PojeVSEooTpsSbipfXAkxhlaM-hTcPdKYkMMw2noc0-yJrSqS3TIhx2g-674xTih5UsdRL9XC8RLJrl3pmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=cqjygdbvakyKhJkUI9OBBxGenh05QzI1qxY1s6PC2ebwxiLnE4E-tTMshIIUFfni9D2FkNvJFoUPYCnVohLl5EdaxEhq06Xd68c9ecvXDCFIj4iSvwyjYlkcLVai2UQgjAm-nimNC09lOq7dgOD3NfqPCZn4L53-H89d8LcOB7vfU0wfqiZV1Ntmch_6XTF9icqcM4oQLYYEhxpyUzk0Kbb1kY1T28C2OGAI4zfJICoeplM0HB4kVGN2GlJN4W1bpk6PojeVSEooTpsSbipfXAkxhlaM-hTcPdKYkMMw2noc0-yJrSqS3TIhx2g-674xTih5UsdRL9XC8RLJrl3pmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdlogpJK4EXOZRqaiIYhFo6Uzh-6L58keEVQybdijsZXorvJenGVmIdQP-e7er8rizlsjhN4sHMpdk08GcTUT6Q7tgucFFHfEWZz4JqFxdEjc_EmaaZRw565_epyPgVWcnQZ7bbqXNbV2eexHJsJmLXjBD5O4WzgnHJvX50zPDc_2kNmFZ2ahqhZ2syPGUz5M20z1iC7eT_uIh2Grh3DENARxqMyNQ4IdJ9ddJjO_P67GuydOfHDsbn7Fwj-25Cr5zrU5ULd7I3bM10rzcXtbWo3ChXhETsD52VCRqOfvlNdhcCbP-Hs6iz_mCdLwoWabCBZiaJauHafDKOgpZc66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=a4z5aTkKywsko8Qrd-DLQLlQxxTR5Z7ms23pEeSLielJXhklAIxRCg0ZGUyFYXLug6Y6U0HBtAIjzxS1t_cPqDrZWk5g2DDjL-ii5Jf5dOzmmbmURtEZcV6sM8beH2DuDcvImPjlupSOMT657nByf9ECKFVQaGNHtgrhpaoFoyWjPhgxeotJyFukVOmvoHUYLvtQ6XIeEJEDONys21oT0E08TuyvXZ9A2xrDmp2_L9jSVMt6n6EL2IGywx-TJ4gXEHvqrmerEEaKjmUaRBOnf8OwtokR2kzlzf4MRZOJLVD8dm1EBoHwrReGQb2ZF_GGlRjavgtraZhmZ59RRd8Jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=a4z5aTkKywsko8Qrd-DLQLlQxxTR5Z7ms23pEeSLielJXhklAIxRCg0ZGUyFYXLug6Y6U0HBtAIjzxS1t_cPqDrZWk5g2DDjL-ii5Jf5dOzmmbmURtEZcV6sM8beH2DuDcvImPjlupSOMT657nByf9ECKFVQaGNHtgrhpaoFoyWjPhgxeotJyFukVOmvoHUYLvtQ6XIeEJEDONys21oT0E08TuyvXZ9A2xrDmp2_L9jSVMt6n6EL2IGywx-TJ4gXEHvqrmerEEaKjmUaRBOnf8OwtokR2kzlzf4MRZOJLVD8dm1EBoHwrReGQb2ZF_GGlRjavgtraZhmZ59RRd8Jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=KQkN9dl3UXKc3ZszE_5Afll0JuEMPsgE6SPxDaHtXFi99sZWvO2Dp5ul19rlnI69k_5z5j2Rv73fA1biwJMU9Hmke4SPlI5dHgElmMWzBDYFJlxpIxhxepgYRdQcXIg0nBzwCqvk00DR-Hm2hVqS4BmmmdazFzn898ZbZSAnSATBqG6mw1QHoEwMRFRzotNPSLIaogOOlYBNz0La6mXWplx6sEbymoGkDWeULfh8QnYud8qvOsF1Irn8tlhRHdjelIrhY4-Bvxq77029W0a0-2r8J1N6mNzaELuiXUbIsU3iJQy1xdwQ0JFWvZigZgo1BF_WD4GKBEb6cSWIEoUKjxMdBz43kjcISmrmPbVldpsTsXK4f6iEdUEifki--L8PWGQgrctiN58XedZhKi3ZVOxF4tFPG25kg6hKT4KCxNrHtZ6MrURHEaP7HPTTeAXr7nZrmw5fpwDLTezAkNClbYljLxaXYC7bTA89y2Lh4XVRO3xEO-HGn74mgMBi5JimT5DDtHWI5BY_TBindP0Ym0Bf6infPXnvm-e10HYYK5wc08HmdsQBnkZnhrKBb288I1SluQijAMvi1eLZhYSlRaYcAzo4SiXEXRBy8ZcFTHjzImlCF9dB4HruOJEXuynRDV5gmSOpcBqgiLWxucIlJLeb6uRdevNptGEeG344Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=KQkN9dl3UXKc3ZszE_5Afll0JuEMPsgE6SPxDaHtXFi99sZWvO2Dp5ul19rlnI69k_5z5j2Rv73fA1biwJMU9Hmke4SPlI5dHgElmMWzBDYFJlxpIxhxepgYRdQcXIg0nBzwCqvk00DR-Hm2hVqS4BmmmdazFzn898ZbZSAnSATBqG6mw1QHoEwMRFRzotNPSLIaogOOlYBNz0La6mXWplx6sEbymoGkDWeULfh8QnYud8qvOsF1Irn8tlhRHdjelIrhY4-Bvxq77029W0a0-2r8J1N6mNzaELuiXUbIsU3iJQy1xdwQ0JFWvZigZgo1BF_WD4GKBEb6cSWIEoUKjxMdBz43kjcISmrmPbVldpsTsXK4f6iEdUEifki--L8PWGQgrctiN58XedZhKi3ZVOxF4tFPG25kg6hKT4KCxNrHtZ6MrURHEaP7HPTTeAXr7nZrmw5fpwDLTezAkNClbYljLxaXYC7bTA89y2Lh4XVRO3xEO-HGn74mgMBi5JimT5DDtHWI5BY_TBindP0Ym0Bf6infPXnvm-e10HYYK5wc08HmdsQBnkZnhrKBb288I1SluQijAMvi1eLZhYSlRaYcAzo4SiXEXRBy8ZcFTHjzImlCF9dB4HruOJEXuynRDV5gmSOpcBqgiLWxucIlJLeb6uRdevNptGEeG344Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=Os-_FVNq0yB6pDonkisE_Una4Rlm-knp3qawt1Z8vQFCYdGvLq_Y2q1_kVQBF3kXyyOSU-fzprIXkO0pqOXMsi03hYF1cCcKKk7fQdJr5rimVfVPS8qm6muKC4xoMt3tL8ARRNK2O9gtGYvdTWA8I3XTJDl6xsgUtR_er-CS56pRZpAc0IkRjoOedcgN0LFc94q5q7b_mLKFDipU0ZOgI-RmEo-hdZQCyEFL_iPowSHylhQ_vDQEIdCaC80DT_5deGDicbvA6wek5VurnN9J29grWKlEy5i_t4X0otyFbE3q4DxrrOCMfCCi-pFnbY9xqjQc6c04X8aN1ap3tNBVQTL1pTUir_9h19bovL3D-xnP979eShyZqJtAK6mvPb08fS4sf_tkvsFOWZs1ppvsIE7oq_sBmfRCBVPvGO1vQfC6T1BDYZaaDgLN7d2tU2GVxMBGRqxnOwDdIHlCuGhJMlGJF_cL-a4K29BvcwmFPP7OaVjsXMvQMatam3irfCcIOdAtk5QFp8DhR_jMgmmJRnErd6ezFk_rM2IeBCzPptWedSwrN1lWiCRHLxfUPF3QJq6e91-qBTJnkMNRayvXt-PpDlevWn6zJfztxddGv53u8Nl6g8WHy1JOEiBXikHE2Pkg_penssaN_BnNkv5zrqoSsX_kaQpwRrdBLDlm5ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=Os-_FVNq0yB6pDonkisE_Una4Rlm-knp3qawt1Z8vQFCYdGvLq_Y2q1_kVQBF3kXyyOSU-fzprIXkO0pqOXMsi03hYF1cCcKKk7fQdJr5rimVfVPS8qm6muKC4xoMt3tL8ARRNK2O9gtGYvdTWA8I3XTJDl6xsgUtR_er-CS56pRZpAc0IkRjoOedcgN0LFc94q5q7b_mLKFDipU0ZOgI-RmEo-hdZQCyEFL_iPowSHylhQ_vDQEIdCaC80DT_5deGDicbvA6wek5VurnN9J29grWKlEy5i_t4X0otyFbE3q4DxrrOCMfCCi-pFnbY9xqjQc6c04X8aN1ap3tNBVQTL1pTUir_9h19bovL3D-xnP979eShyZqJtAK6mvPb08fS4sf_tkvsFOWZs1ppvsIE7oq_sBmfRCBVPvGO1vQfC6T1BDYZaaDgLN7d2tU2GVxMBGRqxnOwDdIHlCuGhJMlGJF_cL-a4K29BvcwmFPP7OaVjsXMvQMatam3irfCcIOdAtk5QFp8DhR_jMgmmJRnErd6ezFk_rM2IeBCzPptWedSwrN1lWiCRHLxfUPF3QJq6e91-qBTJnkMNRayvXt-PpDlevWn6zJfztxddGv53u8Nl6g8WHy1JOEiBXikHE2Pkg_penssaN_BnNkv5zrqoSsX_kaQpwRrdBLDlm5ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MN_LDcklptL00HFWquWo4G1I3hSeebr1PXKfrZC6oUnwJWM6t4KQJFhRsqxx8Afq50QploWQ8HEuGc-T6EJymuc-9kXwngFW9jnj7Aeu-hUNAXPvPeb2mrx2f2_MBnu1zQ0WjFERig9wIj2Xue5-TMAD2D_n2CzEn4ZbGvxakm6LUnHTP-0Ut3z0J1WDJU9st0Y6UjetBBh7LRl7taLh8ll1k8sKCwcNmMeEm91FKDVy-X3OZpxnX-MXNd7Wvr93wlaZMPr61thV2QdDBjHuAyD3R5s7EoVXxPHvDYD2IYKLEczPuDMNpGAVU4H45v6hT-wBPKI6j2h-aIUyKuYIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGlWCVlOFtjVOdin9xYtYEXxkbaRgDAGqadm20otpI7D6iJgTBueivoQMUdftWXpyB_Kau5vt7WVvp5bIiz3I2gVVf3YUAaYIy7x8A-ysCaOpUj7-KKfkbtWWdnmkMV09eXOQJiqmeCbcvGy7ne40vL51RCuZHLSe5VpEAW5HBA_eaT_kF5-yPMzOWxEnxxS5TCnXxgJO9lAtgl-jrsWGAT_O4g5EDX0kX91V6u6DIVUr754JRif0XgAEqqGragiT2y-iyNJdKLP-E8GnSxCKaQs6qoXG3XGpxAE6WDhjSdn2LVz5v4WKmv3YKJigM1fx9d1LRtRGBB-E2xyc15fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=mIGXUNoaXFh7gPkIYh-5jUK8qfmFQ0ihcy3hIG8m37hqq3e_hcNdv5XnBT0ME_Fw04n7JO_L1Z7LitVwUr1SMyYLRoeTWowYRmkXtIp7joR7CdEG52vU0gBtBS9W-uxuiwgM6UmJFYx-KqlKXbWjwloWh77L1Of0r-qM5x8X-8m2AU8klh8LBgSUzGnJ7u1CM32qepAhjtFRbRh2ugSuMEtR_hnuCGrFn5d9JeU8c_YUekVIpx3EviAHQiNzjX81i_Zmfkh6-AQiqyOMcfa5XLWexH9fpwlT_2SwamCyHQ993MMOa1cu3zyJdXKo5DfemPbAH6cS5hZ7YuOKcMmNJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=mIGXUNoaXFh7gPkIYh-5jUK8qfmFQ0ihcy3hIG8m37hqq3e_hcNdv5XnBT0ME_Fw04n7JO_L1Z7LitVwUr1SMyYLRoeTWowYRmkXtIp7joR7CdEG52vU0gBtBS9W-uxuiwgM6UmJFYx-KqlKXbWjwloWh77L1Of0r-qM5x8X-8m2AU8klh8LBgSUzGnJ7u1CM32qepAhjtFRbRh2ugSuMEtR_hnuCGrFn5d9JeU8c_YUekVIpx3EviAHQiNzjX81i_Zmfkh6-AQiqyOMcfa5XLWexH9fpwlT_2SwamCyHQ993MMOa1cu3zyJdXKo5DfemPbAH6cS5hZ7YuOKcMmNJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX5kfykdfByqslIolmRaT_1MPyiymJ84yN7QqeIgo3JFdmjjhkxnHnuDqKgZxsqfL7cYrmWqreWKAEE_x9RrjZiYBNT7cctG37dQF7W3K9lvYRq9okB9ysqsZn0IUQ8miHHmReppsxY-MAS6BKoH-4YnslzCll137RNioCfO3RwsCrSwR_CFChAdU5zlXEfOuMKYOrPY_s-SkUCiBx63QduhoHs50h-pvVOg6Ez_5yBrEw14ILtKVohf6Hg_HHUqxR5454fOMa_xcZzlwjiUSNKkx8-xI1cqsrRnvk6xOeuGX-vimBZBUoYFCOLe9E4bhyDl0-ILg5nIiJ_Wed55ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=HLvRpidriE3cC9jHtFyTn1_1xJW2A2BrSj_BEQwHAZv6IDUUOkvDw_8crbzCxLzQa65diOYbkIEHTQRq4nJDxpv8I332eDyaHOjyDuLtI4WtsvdTU0ZOyB-a26suE2Pma9HTxbmrIaOsAMauYPzDvo_4_pjRomAGHjYVC_5WfhUezil6NbGPO_lG3SE1BuD3SKYEDg0N-_EB1nadrjhB0QGknyDvSNnOoWBilitAsAr4wiOOqqgy_K7PXtM429m2q28vjgatyFqojLBU7PALZNYgIx4_9NOJGIVztSrtM6WJ08sYB8iIQbm7NjmU2nsOnzEDaHEyOSviIo7MU0O3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=HLvRpidriE3cC9jHtFyTn1_1xJW2A2BrSj_BEQwHAZv6IDUUOkvDw_8crbzCxLzQa65diOYbkIEHTQRq4nJDxpv8I332eDyaHOjyDuLtI4WtsvdTU0ZOyB-a26suE2Pma9HTxbmrIaOsAMauYPzDvo_4_pjRomAGHjYVC_5WfhUezil6NbGPO_lG3SE1BuD3SKYEDg0N-_EB1nadrjhB0QGknyDvSNnOoWBilitAsAr4wiOOqqgy_K7PXtM429m2q28vjgatyFqojLBU7PALZNYgIx4_9NOJGIVztSrtM6WJ08sYB8iIQbm7NjmU2nsOnzEDaHEyOSviIo7MU0O3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72613" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a16936d012.mp4?token=MbIEgO4Lp-ke3HGcY8cOM6tuXZfwjhYjSizN9B_CUcl11hRN2uDAf1NUqPmNOPt9Yq4-c-ndQSwm1zAALokheQwFfxj0F4lvtMlmaYu9Fm4D2R85RfkX7872TZLZbo8GmEZB4QAbmOXI9nyXE0vkc6uaMuPKNI6S9-np_BhsWJK94_1kFBmtH2ThLMJrrEneLSl4x3y0Ws3oWSloDdkqWAE6hFxMfeIq2-NXTUVFmEkdY1zGDObBWXx90LirjxwA2-x12RwtsDq3SWkAmVBSRraoYq2McTn-z15EqkzyR8tdps4NfWr7dsYhbYa32r8DSLCOwWUeL8sVJgvkZ8WcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a16936d012.mp4?token=MbIEgO4Lp-ke3HGcY8cOM6tuXZfwjhYjSizN9B_CUcl11hRN2uDAf1NUqPmNOPt9Yq4-c-ndQSwm1zAALokheQwFfxj0F4lvtMlmaYu9Fm4D2R85RfkX7872TZLZbo8GmEZB4QAbmOXI9nyXE0vkc6uaMuPKNI6S9-np_BhsWJK94_1kFBmtH2ThLMJrrEneLSl4x3y0Ws3oWSloDdkqWAE6hFxMfeIq2-NXTUVFmEkdY1zGDObBWXx90LirjxwA2-x12RwtsDq3SWkAmVBSRraoYq2McTn-z15EqkzyR8tdps4NfWr7dsYhbYa32r8DSLCOwWUeL8sVJgvkZ8WcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی مملکت یه سری مهمونی میگیرن که توش با تم و استایل دهه هشتادی شرکت میکنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72611" target="_blank">📅 09:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtzzcBx_k8QfH8EPEjvud_lM6EJLKRca_aJVfioq23tIPsXiipo7Zav8IlQOlO_vWz0M_HPigKEadHyW1il_AdzHOCjaVL3uZaX9KHCFdm8I7RHTTwm-U6XZpbM_yx4nsIWWt_JigWsABHL0Orr4ZZtVyXIXPWhfc_nKGxK2hyTW9mluGyk4VqU3Uq-hSvzwF1ymIUI9W0kfHvweK3oi_KewFkmLSac5nx1w_M7QdKrPUW1bJU0KlqDkbf2cY5IOSL4r_SN_LS0C1SIRDYIoNBPptb-0WEWhgwdp187BCyHqOQn-dJ-a_MpyAVNdjUy2lEl3ZwXs8lGDeJVgbIMdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده با اعمال تحریم‌های جدید علیه بخش‌های خودروسازی، ریلی، تولیدی و فولاد ایران، دامنه «عملیات طرد اقتصادی» (Operation Economic Outcast) را گسترش داد؛ بخش‌هایی که به گفته واشنگتن، با کاهش درآمدهای نفتی ایران در پی محاصره دریایی آمریکا، اهمیت فزاینده‌ای یافته‌اند.
وزارت خزانه‌داری مجوزهای جدیدی برای اعمال تحریم‌های بخشی علیه صنایع خودروسازی و ریلی ایران صادر کرد و شرکت‌های بزرگ خودروسازی از جمله «ایران‌خودرو»، «سایپا»، «ایران‌خودرو دیزل»، «پارس‌خودرو»، «زامیاد» و دو شرکت «نیرو موتور» را در فهرست تحریم‌ها قرار داد.
همچنین تأمین‌کنندگان خارجی در اندونزی، امارات متحده عربی، ترکیه و هنگ‌کنگ به اتهام تأمین قطعات خودرو برای تولیدکنندگان ایرانی و کمک به حفظ شبکه‌های تدارکاتی بین‌المللی آن‌ها، تحریم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72610" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc6fwi8wTxR_-pfw3JVtq6TB1xTrlGbAiGDZfrjcjbt0Q5ThJhJs8l0WFi_ERS3PS5j4yy_fM65HkFUgaQOKGfqpaGbr67fuJctDrqHZqYJTea-U-knRGyN7qaGa7CS0rNbAVpUSQ6wB1u0MRG6B692ntQ_1S5ddDb9yr1ZWOVV7mOdMQqcPxJV44yAxVXZ7VqQkk0g2SlZ2q_xwOnRNIlpt-fSZM-IcqSbjCbZVamhtFpm5xQdzFopsY4jpkmAxTkw9WIH-hHVFiMVml98MpZ1gxDh031besgJJ6My5m998p-wVe2AM9e9kq-ic9Pn85MdTdxXKR5E_4KOZDVqmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=eQUSwmZ4oWrHr3KewtJP63YIXXxP-sd-rLGT__aMDVFZY4p7zfTHrVER96a-qJlo7pRCb5psZy1njL5X-dJoD4jZJlFqpBa426_7RxPblHB5sobAekYcKLIPEAbWcXBLNHjGp0ZKZiVRHIu5hbxewoSRmpuNPojLEJU1D23irBUYhwKFq7gZopJcMQMurrIMGZKRsaPA50t4q8AbbSmTI5guF_d7lUN8UKuDQJOXnMkzOk9AErdqjbpPesi7yPvTZ4GBzHrUDr878Nd-QGlg_8v0NmrlOAiIldtTKTZUsEtkHo81PPeftBNDKm_qgFB9wFekkSh3A7YcGQqEx6fSIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=eQUSwmZ4oWrHr3KewtJP63YIXXxP-sd-rLGT__aMDVFZY4p7zfTHrVER96a-qJlo7pRCb5psZy1njL5X-dJoD4jZJlFqpBa426_7RxPblHB5sobAekYcKLIPEAbWcXBLNHjGp0ZKZiVRHIu5hbxewoSRmpuNPojLEJU1D23irBUYhwKFq7gZopJcMQMurrIMGZKRsaPA50t4q8AbbSmTI5guF_d7lUN8UKuDQJOXnMkzOk9AErdqjbpPesi7yPvTZ4GBzHrUDr878Nd-QGlg_8v0NmrlOAiIldtTKTZUsEtkHo81PPeftBNDKm_qgFB9wFekkSh3A7YcGQqEx6fSIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=ptN_nNAEmrLw5CLN6wgaHSfv6fZdIouN-Ow_gzZppDaP03gmdkCYurDFO_M5n1JY4ZDdHtX40V4z4VBvnmG1ByoGBhd941EuRVKq0hkTE6Ev5s0ZI593X_8py7wsTnD7Ge7VfTYqv_9GbHxf89b_3lH_iRJ_rdmZNtfMK_SjU81RzDuIDHVp8Z8GDK8Az-1hcS5BEjmhSPxh_epvE57Xc-txktEoIDkQZNXGebmpPCPluuvJJp1fqxJBUs-AvCDA-aE61F9OT5Ino2PcIAI6WKKIWqQgHBe31RTPe4xyIuH4rvvmXVNoq1AtunmNh7suOTEz6LDTzc_VqwGvGGtF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=ptN_nNAEmrLw5CLN6wgaHSfv6fZdIouN-Ow_gzZppDaP03gmdkCYurDFO_M5n1JY4ZDdHtX40V4z4VBvnmG1ByoGBhd941EuRVKq0hkTE6Ev5s0ZI593X_8py7wsTnD7Ge7VfTYqv_9GbHxf89b_3lH_iRJ_rdmZNtfMK_SjU81RzDuIDHVp8Z8GDK8Az-1hcS5BEjmhSPxh_epvE57Xc-txktEoIDkQZNXGebmpPCPluuvJJp1fqxJBUs-AvCDA-aE61F9OT5Ino2PcIAI6WKKIWqQgHBe31RTPe4xyIuH4rvvmXVNoq1AtunmNh7suOTEz6LDTzc_VqwGvGGtF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=mNb5tTEMgfc1wlvUA3m6L-7Q5xjQLgXtHITa-ZjgwJT6fKzrH2EICERa-K2qriYpt51rXKQZ0k2qqiwGrldlakNaTiYT6dnClSkad3MuXfhUGGg2VkA4f7mHp1C6wVDIG-bQSAYLEX7a-6WFNl1Imm41rxm8s6Y4Xu3xPeZ60KMqFzjAZW-ETI-pq-f91E7Yt8tpD-uMl6TDMpyI6LQrEXvuUCWeNurWpP45kAchAxo7m5GUuJ3OmUqFZ3vR_8YDP9JEPFfR4lRte25VJkUZyzgBDbZ7YPtD3nI3b3Khd-nRtQMcjoXfVR0vXwuk4TN_9E2NPJ1fvndOLcqH7D8HrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=mNb5tTEMgfc1wlvUA3m6L-7Q5xjQLgXtHITa-ZjgwJT6fKzrH2EICERa-K2qriYpt51rXKQZ0k2qqiwGrldlakNaTiYT6dnClSkad3MuXfhUGGg2VkA4f7mHp1C6wVDIG-bQSAYLEX7a-6WFNl1Imm41rxm8s6Y4Xu3xPeZ60KMqFzjAZW-ETI-pq-f91E7Yt8tpD-uMl6TDMpyI6LQrEXvuUCWeNurWpP45kAchAxo7m5GUuJ3OmUqFZ3vR_8YDP9JEPFfR4lRte25VJkUZyzgBDbZ7YPtD3nI3b3Khd-nRtQMcjoXfVR0vXwuk4TN_9E2NPJ1fvndOLcqH7D8HrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=An8TkrIEFzaOSQECfx075JwFJeQIJ-ZTzPPInQeytcuVbMIhsdV6N8YE-2raZdgtLVR3UL_-etY-MQTFI9rz8TEkU80UbsWagIOeeTK-OSp1khvLGJpNrYOM_nczBOkO7Nfh8b4iM2XagbUkXfqNzMpqNwcZuYgJ3h8qmBgMYpt1RhqZMiGqihBFujmJ0DxvRgOpkQeCBqdPY-4a5yevXjhAc3dvnegwmFxvF03M0ZsqKvcjMFWlseACSxDJL488VL3i3-XIschz5sYUSYj-2hCkc7duyJVM1LnQODLdxMFWVXuq9XQFoJJxjwyypppAxfsCRUz9TPhw7t5DZGYZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=An8TkrIEFzaOSQECfx075JwFJeQIJ-ZTzPPInQeytcuVbMIhsdV6N8YE-2raZdgtLVR3UL_-etY-MQTFI9rz8TEkU80UbsWagIOeeTK-OSp1khvLGJpNrYOM_nczBOkO7Nfh8b4iM2XagbUkXfqNzMpqNwcZuYgJ3h8qmBgMYpt1RhqZMiGqihBFujmJ0DxvRgOpkQeCBqdPY-4a5yevXjhAc3dvnegwmFxvF03M0ZsqKvcjMFWlseACSxDJL488VL3i3-XIschz5sYUSYj-2hCkc7duyJVM1LnQODLdxMFWVXuq9XQFoJJxjwyypppAxfsCRUz9TPhw7t5DZGYZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=vrbjtN5HWRpyQJZwRjiYCPnOPmo5mD7kwvo6nGPUGsTjJQhGd8_EUxfStwUeaaC4g3YU3nrq_mlM7OAQ7G0JPmDJDc4kgp3_s_oQTC68l2LQJ-yqoEuUBnipxMONzDUP-d-oYp-kZUgpZQx64z13LUpaWttA_qtzlD6HVAf-riSa8coBwUhvIfb8SVzSIox_jDZD-47QhGcwyCEyTYWFBZl2V2qViNIvj8U4DL4zuBOpp31byMYmPKsQ3qgICnwNRdI9mHDfvNjxp1kf0U9QQJXdt6x2q2wBCqcxuug3mL6Xm31N0WmXOK_MEgLrGVCLfqMwaWbMPNspxKGSOxSb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=vrbjtN5HWRpyQJZwRjiYCPnOPmo5mD7kwvo6nGPUGsTjJQhGd8_EUxfStwUeaaC4g3YU3nrq_mlM7OAQ7G0JPmDJDc4kgp3_s_oQTC68l2LQJ-yqoEuUBnipxMONzDUP-d-oYp-kZUgpZQx64z13LUpaWttA_qtzlD6HVAf-riSa8coBwUhvIfb8SVzSIox_jDZD-47QhGcwyCEyTYWFBZl2V2qViNIvj8U4DL4zuBOpp31byMYmPKsQ3qgICnwNRdI9mHDfvNjxp1kf0U9QQJXdt6x2q2wBCqcxuug3mL6Xm31N0WmXOK_MEgLrGVCLfqMwaWbMPNspxKGSOxSb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=CX_9PaLKB___ODfROQnB3_iUFhMSvkPqfVnn27I_pX6laFTLsf6kfLYeIzuLe_6QLiX0XEt5Xy3uLTox3Z8MOKkWcs5uDsn5RdeZSRDzWW-ekLg2jbwXdGQFi9D5UvO-qzXQSFzfioWI0BXo2lHLiR4IP4qu-9n8nzDNzaYsLKMDikbot5HKN7ho1s49yU66cgo9YHMqqtdahmL63lJknI3XwwjGAxAg87h86FpXTUSOGnzjExUuRSEGV4pK79eSbzSjEkdqDgkJQyc1rJMjXZXWFr4WIfvZgBU5EzBoGFFguLRw8mp7ThcChlnWM7kLZbfjc3gb0h8yJAT4dcDy1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=CX_9PaLKB___ODfROQnB3_iUFhMSvkPqfVnn27I_pX6laFTLsf6kfLYeIzuLe_6QLiX0XEt5Xy3uLTox3Z8MOKkWcs5uDsn5RdeZSRDzWW-ekLg2jbwXdGQFi9D5UvO-qzXQSFzfioWI0BXo2lHLiR4IP4qu-9n8nzDNzaYsLKMDikbot5HKN7ho1s49yU66cgo9YHMqqtdahmL63lJknI3XwwjGAxAg87h86FpXTUSOGnzjExUuRSEGV4pK79eSbzSjEkdqDgkJQyc1rJMjXZXWFr4WIfvZgBU5EzBoGFFguLRw8mp7ThcChlnWM7kLZbfjc3gb0h8yJAT4dcDy1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImHHZlnMaQ8y36ypUtfu4ejD8BIMJKZOKHUzsDo2u3y3n6cT224_LVc8Yn8l3AMXqCrofRiwmNuocphRt7Y-PsQnvJz9v3jMPusaNaMhK01aunUWqMA1nCMrsk-0SCaM_FJ2WTvdPYeV9n8b1_CVBHa2r_0jj3J3mEAfdQ372xoksY15wnty105afdYv_SWxeQBnuy7bzhY9rVF1ZhIpIRxku4C38cXQDAsMbA0W4HRXqZdJz4KApw1qg9Tum38LZGZeYaWVhlo-6jjB2Edn6xmDgWltnAOinQ0m7v7Eggrwpw9jLiGc8FPIB1FMaVEjQu_TJ2oyD_EPL9ANhmvXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=MgBwnBhNXuOXM0y3LXkRdHpqyzizC5O6KsuuMSimWWVglWgYzfbHKVADnd70dNnoq30rIN3K8LJTx-MBO7_Bi-p-fpLfvijCwdrmp49BJPfbUSeG1NuQ7qkELzh-gKh8dI76B_nyoON9tps83dohdpIQmfx4IYhB3FZempxPcmOXvuNShjJXvgjR5avl7SJGkE01tX9yaQJR1wQDgxxGFkdX4mIl7Gnv42zjJLXawqSfxioeJLrtKxI4EG0jTWJ6ULxKZlEbpwFeDMzmalLKme1kQxQxdwyRPLTX4Qqq1C4VZkxx-HvglEcEwlRU0BEvU8MzbvUInEo4JppqBu_HaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=MgBwnBhNXuOXM0y3LXkRdHpqyzizC5O6KsuuMSimWWVglWgYzfbHKVADnd70dNnoq30rIN3K8LJTx-MBO7_Bi-p-fpLfvijCwdrmp49BJPfbUSeG1NuQ7qkELzh-gKh8dI76B_nyoON9tps83dohdpIQmfx4IYhB3FZempxPcmOXvuNShjJXvgjR5avl7SJGkE01tX9yaQJR1wQDgxxGFkdX4mIl7Gnv42zjJLXawqSfxioeJLrtKxI4EG0jTWJ6ULxKZlEbpwFeDMzmalLKme1kQxQxdwyRPLTX4Qqq1C4VZkxx-HvglEcEwlRU0BEvU8MzbvUInEo4JppqBu_HaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J38Bn9usCeCHCsa_mqrPF0rDvtmH1eNTFK73DdJvX5abtt-jqCGPou9H_-diYlRA9wE3l2kLB6vCAqa4Mc9-aXGN4z-8EAlXSu3ix6TOFaXjvH8TyENdbvcdTWE2mOE_mUZW69OTPhR38oEqRweeQgJx5xezS-76CzrVyq4ooMGZbNuRUtZc0EK6Wj1fRAf_vSlNfbbdgSxR_X12AgMo12HyuovkXq2CmqEFgzyTxeX1XnOwYc-B5KbtIZBQy19DsKVf8kbpDMHKB83-z4UJYJriHUlpDwM1iFlV-z4e9nsT-x3m6b1Lk4QGeve5i6-6w4szQJTSEiyvipZD2b0Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7e65pv3sosxb_luLcq6HwKUhz-doswBFvWOll4rK8zJQdAKLwrS1-BzfGA9zfFU0zyPe9fHDQYGW70MaiKNKZG9-Z6l1jjY5bDi7S1CrUpbar1KCPPgD23KtsFaKqXPmgKKjUEphtlyNSLtBBFBOvBGiRDXiqXqYPFvVTSdTyc0Gmr8rCKPP-fYfubb7-ZJOT4lB_srmIN_RCdqZrqmLjdH-bX_L4coT4ufY-umMOse7yJyBri7nifEi2UKm4gAU5tYJWevOtsQ7a6k-swWWQyMcGYNfXdAiUEoLZIZ8Q0uDr5kZRAILv5iXRfDP_5bpuR4dHlRPcJnZUMpvUGUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=XPXKpVmo7waBpSnIr3G5nooKyXKrH9j53el4Z4OjXXGHDvfKH1xt8IGkQPiVa0zxwHzID-iC_chNPkxtcvOuTu2im7_27YpHAnVwQIRx07P1sDFhd_sI56OU8pdld14u9Z0vA4DECcuh282i1N2jUTGKQPXpxkfnHge6C-9ev9o1qnRXbCSReX4aOplJLW3sgzmfUUrCvApFExhGj1TL-CRhkHIFIsr1E-6fNA3Jo-eC29V6h0RAOvcpPOKRJb0A6pwcjoyc9RIFhxfdmg_qra2EnlxCIqE5zWMzwAw5SeBLsbsMxahRJrv8vBxPAh9evsBbsfz9Ldy_p5wBfABnpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=XPXKpVmo7waBpSnIr3G5nooKyXKrH9j53el4Z4OjXXGHDvfKH1xt8IGkQPiVa0zxwHzID-iC_chNPkxtcvOuTu2im7_27YpHAnVwQIRx07P1sDFhd_sI56OU8pdld14u9Z0vA4DECcuh282i1N2jUTGKQPXpxkfnHge6C-9ev9o1qnRXbCSReX4aOplJLW3sgzmfUUrCvApFExhGj1TL-CRhkHIFIsr1E-6fNA3Jo-eC29V6h0RAOvcpPOKRJb0A6pwcjoyc9RIFhxfdmg_qra2EnlxCIqE5zWMzwAw5SeBLsbsMxahRJrv8vBxPAh9evsBbsfz9Ldy_p5wBfABnpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHjjTzkbFZS9LO_WYro9YGWn0XCq9HTqG-z6e6NBeUn1nsEHiso3x672g4c3SjpwFshKe39mVA1k7o84H-lILlEBJQI3NYB-LV8mOATjZ4K8keFyZ-T2TpnWgGF3JObxMEW3p_M7TR1K8MhN0oGcPvZoNntPGwbuMb28D1G71K0wOy-IdjLIwvlVQ09rdy8pox6o2VFWqBXSuFbtiUcwvX5wsowJ0QxsiDC2VsJoRJgn_3e0qRkK76tOAyn2vCG0cy4LMj2FR6USZtOrXqFqWE6UatMUrfkPPnjx4mmq1qdAy4-0jjoBM6bCC7LeRhKJdyH1p0ejY16RpbM4gtUnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=UnqC1_JfExJlwlP702cxwgiJWKO6k1dVOkGzZjeqzNBrUNr8_OHtzp-Y25Ap5qaIICtvAf5Y8j7WfP-YlxQCIpBqEO4gbMJ1n1XEAiU1jTN5ZmZzOfYcJ08qjFzKhdOSq1Nk_Z_vwXzyhQzQOOxAWBnJFbdom5-yAaafWcOUJUY-Wk4SRP1vWym6vi-w9V93w9T3UT1HSARywj9tptIO_0yLUb7DGBxnuQu_QL9P26PVfrcnARXA1-yyywgzS1SVZXonSiRQWkEvKvVDNSaJ311GtyZmO6mDCvh5jXgfky-2jM35GSm5YbjSvlX5FON_yYGPV6naTaHOpG5DW7LnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=UnqC1_JfExJlwlP702cxwgiJWKO6k1dVOkGzZjeqzNBrUNr8_OHtzp-Y25Ap5qaIICtvAf5Y8j7WfP-YlxQCIpBqEO4gbMJ1n1XEAiU1jTN5ZmZzOfYcJ08qjFzKhdOSq1Nk_Z_vwXzyhQzQOOxAWBnJFbdom5-yAaafWcOUJUY-Wk4SRP1vWym6vi-w9V93w9T3UT1HSARywj9tptIO_0yLUb7DGBxnuQu_QL9P26PVfrcnARXA1-yyywgzS1SVZXonSiRQWkEvKvVDNSaJ311GtyZmO6mDCvh5jXgfky-2jM35GSm5YbjSvlX5FON_yYGPV6naTaHOpG5DW7LnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=s3ebUrLkAVxosJOtrnlAKA9xUXC8JSBtHpuEsLXzQSD7hXicntunv4rfuWtZqAU1xYG9XTGfOS0YbzRYXUFqMhAgQ9mP5fE5EerIkVtR1zNCdXuC199lalcS0cCjl0EHHKwzJBx-tEM5Zc7Uz2otOSaRU7Jya5dSf4ZQUrqBzMRkqf5zaa8LmxdUB_qt9TNyEir_dvnydZvF_ryCvpu6TwvsTT8B1qO7HRfD2iyQ7euAURfYd5uhzbDuoPCKB8d5Ieu4r-4XwfiaHht8v94cQunOXinkWvWakwmtwmzdt-3auAGdLA2X6iLF1ktH7ylAr8ZDwP0GyWFJvLUITSeyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=s3ebUrLkAVxosJOtrnlAKA9xUXC8JSBtHpuEsLXzQSD7hXicntunv4rfuWtZqAU1xYG9XTGfOS0YbzRYXUFqMhAgQ9mP5fE5EerIkVtR1zNCdXuC199lalcS0cCjl0EHHKwzJBx-tEM5Zc7Uz2otOSaRU7Jya5dSf4ZQUrqBzMRkqf5zaa8LmxdUB_qt9TNyEir_dvnydZvF_ryCvpu6TwvsTT8B1qO7HRfD2iyQ7euAURfYd5uhzbDuoPCKB8d5Ieu4r-4XwfiaHht8v94cQunOXinkWvWakwmtwmzdt-3auAGdLA2X6iLF1ktH7ylAr8ZDwP0GyWFJvLUITSeyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=ZXK7fuxKRCvJQIOdQhQ5aARSF74dg-Scc8I3xaCfUKm-IL13nUrpFc9fWwp6JV5paN_vpNeEY-SJvRrbnLOWUw-deKz9SVTqoOTVdX5JJO70dL62k20Kt-FKooy28cTwTDXfl5PTTyQrLjgZevCW5I-v8HWMhPrdvbeXm_A4KCDaTojtJ1IAdniIu_1d1ryGZJFwLGBawGbPGbWrZN7nQhJufmxPVFZCiyqO54QAv2YGsJvLEORq1r97yAqYn2hr4RD2xf-kLfNGf0Cd9vzYO_WbzBV1W5Xhc5-utWAMyhxH5e5OTjDx2LiSt4m4n9CXz6d-Wc2Uiv29QYicglxFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=ZXK7fuxKRCvJQIOdQhQ5aARSF74dg-Scc8I3xaCfUKm-IL13nUrpFc9fWwp6JV5paN_vpNeEY-SJvRrbnLOWUw-deKz9SVTqoOTVdX5JJO70dL62k20Kt-FKooy28cTwTDXfl5PTTyQrLjgZevCW5I-v8HWMhPrdvbeXm_A4KCDaTojtJ1IAdniIu_1d1ryGZJFwLGBawGbPGbWrZN7nQhJufmxPVFZCiyqO54QAv2YGsJvLEORq1r97yAqYn2hr4RD2xf-kLfNGf0Cd9vzYO_WbzBV1W5Xhc5-utWAMyhxH5e5OTjDx2LiSt4m4n9CXz6d-Wc2Uiv29QYicglxFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=lnwCsP03dQ5CEihGfqlH65wbdJVwZp3G9-P7r1NLrwyVpL-dkDKkJiHVQNH-5d99vYV-MjN5i22KehJCuTz2iR7a6FuvCsxuU2DQ-UC__XxKdfVURm49CuMtUdpBDvpHyZBl8IaWF6gTsoUgEooWjP_WJKYmQZzGs6IN0Ma6qbdFqBsGBlWHK7j6IXjYVHTuZ925D3XRjzqwI_weo6UrBaWCAHAfrumA20Afpos_cF0axQMUk0wrIalLuijPKkXnWgOPiA7KS-U46zTEfa3Ne9PtwyuaC5Sr-gg61_gj8KOPySI-BNw2WCko7Hj17Pzvko71zd8EkDKZdaWDzWA23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=lnwCsP03dQ5CEihGfqlH65wbdJVwZp3G9-P7r1NLrwyVpL-dkDKkJiHVQNH-5d99vYV-MjN5i22KehJCuTz2iR7a6FuvCsxuU2DQ-UC__XxKdfVURm49CuMtUdpBDvpHyZBl8IaWF6gTsoUgEooWjP_WJKYmQZzGs6IN0Ma6qbdFqBsGBlWHK7j6IXjYVHTuZ925D3XRjzqwI_weo6UrBaWCAHAfrumA20Afpos_cF0axQMUk0wrIalLuijPKkXnWgOPiA7KS-U46zTEfa3Ne9PtwyuaC5Sr-gg61_gj8KOPySI-BNw2WCko7Hj17Pzvko71zd8EkDKZdaWDzWA23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=Rdj7pnISU63c5Lsze3i_2vEB3dP1ENGiQ5zSfBKCa90KWysje8wR4ffRSJbNNat9y1WNQTp71rBbQSWYNOe40FT0oZ4aQzAT3PQw09Ahz-MoxgM_vMfDH-udcz4DLg5-kF6e4VjR7zCqFFDNK_iYAleHPVb-SebjB4YnhfbR2Cmi-WvJQPSpVzs3WG_AHP55oRMSazoLGnXKCbkLOcwq1U_Szc2jOiTHoIh5IVVY7YOkC3nHugAL8Zsl_zaddpd13n28x36t_qusmNqlcrIaM5K3pBzbadvMy4by4W34LRcnNtweimAwSQMK6O6Ox-9ndIUV0c_QfBTQXULeEGiTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=Rdj7pnISU63c5Lsze3i_2vEB3dP1ENGiQ5zSfBKCa90KWysje8wR4ffRSJbNNat9y1WNQTp71rBbQSWYNOe40FT0oZ4aQzAT3PQw09Ahz-MoxgM_vMfDH-udcz4DLg5-kF6e4VjR7zCqFFDNK_iYAleHPVb-SebjB4YnhfbR2Cmi-WvJQPSpVzs3WG_AHP55oRMSazoLGnXKCbkLOcwq1U_Szc2jOiTHoIh5IVVY7YOkC3nHugAL8Zsl_zaddpd13n28x36t_qusmNqlcrIaM5K3pBzbadvMy4by4W34LRcnNtweimAwSQMK6O6Ox-9ndIUV0c_QfBTQXULeEGiTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=hSQCd65z25VcVLuY1LxVriHtABqYZQ9V8l6sZpAo8E1w6eJHOamG-oVwoY1fcBrlAcGwptkhRjnSqkqRrP48jf5ND8tdweM9wUV0KbbGFl2397IFify8-OxyQYLXctPqW7ucFV2PCgAZdY1Q3Suadgu0RxHRqkWTJ55GaSg5V3Oma_Nhe2dnBxgd1vEa_mqKm3vxCPTiCxjmr0pVoAuMSboTK867sRTpOJvJn_XQsEQf8VBmKO8gfZ-V5x7Z-pt1ZwMcTE5N6Q0y7KL96fDw6hwAQrr4nereG37GgUBJLb4z581wFkAkcUuONEyZ8H26x66CYzgOpnlrC_lYSqN2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=hSQCd65z25VcVLuY1LxVriHtABqYZQ9V8l6sZpAo8E1w6eJHOamG-oVwoY1fcBrlAcGwptkhRjnSqkqRrP48jf5ND8tdweM9wUV0KbbGFl2397IFify8-OxyQYLXctPqW7ucFV2PCgAZdY1Q3Suadgu0RxHRqkWTJ55GaSg5V3Oma_Nhe2dnBxgd1vEa_mqKm3vxCPTiCxjmr0pVoAuMSboTK867sRTpOJvJn_XQsEQf8VBmKO8gfZ-V5x7Z-pt1ZwMcTE5N6Q0y7KL96fDw6hwAQrr4nereG37GgUBJLb4z581wFkAkcUuONEyZ8H26x66CYzgOpnlrC_lYSqN2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=cUwwE2uS9nYk5VRQ4q0bRcrwokHKhVl648i312_CTOhCsbYGtCDpqKeYFiHS55hrbjP3rOlIR24MUvmlpc_QK8zfsr2WXWeaVu5WmVTgIU6EmERMfRIg0QRwYLApHQbKwR-w8dMjNPi0CmYD_KlQriJHH_Kxh_ETbxGzeQPxNZ-NUs3rVMFXccEFtsnT10LbEo5ZMgKKwYcvO01wJvk1yQYr63Oc6cuXWEMr4Q8di5DSt_RvTrgkt6DzsRc4rO0EkOO1RS1TrBL1OrMO25tHxWS64O6xKIPWGgBcrCWAauIeBBo8_l_wuiBAPrTrC06RV_wWBbSZDuDNbWOR5z1aqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=cUwwE2uS9nYk5VRQ4q0bRcrwokHKhVl648i312_CTOhCsbYGtCDpqKeYFiHS55hrbjP3rOlIR24MUvmlpc_QK8zfsr2WXWeaVu5WmVTgIU6EmERMfRIg0QRwYLApHQbKwR-w8dMjNPi0CmYD_KlQriJHH_Kxh_ETbxGzeQPxNZ-NUs3rVMFXccEFtsnT10LbEo5ZMgKKwYcvO01wJvk1yQYr63Oc6cuXWEMr4Q8di5DSt_RvTrgkt6DzsRc4rO0EkOO1RS1TrBL1OrMO25tHxWS64O6xKIPWGgBcrCWAauIeBBo8_l_wuiBAPrTrC06RV_wWBbSZDuDNbWOR5z1aqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Pqo7pAnxFJFb3I6brgkGsHRFE4TgHylXfMCGbJHNuiLbYyFhHLpEGK8gnvmFTgwk_1C41mp9M6TFsR9dmJI3pexTVdMEfqNbGiO0-EGUkyFLiYZPiKNSe338jJdbcwpTqkNRRUK90Ccd3b7wLX5Bds68Yd_QST6Z9mDVsU5zqM2NsJ7tlLONfGM5O9vNhRmX30UN6RQ-iNXXnxX8f-vBI-LlTZvzbpMrNN4cTUsSomvgaQAlEJ0tJI_dl-_JVm1U5VRGVyS8MnlKVlKIEycIMTBYCZBYZ-igMWQxSH556qp-I8D8hbmbXG3ntdIuRZg9o5tE6KzhWeTsTegvjPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72581" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#مهم
؛
یک
مقام آمریکایی:
ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، سن‌دیگو را به مقصد خاورمیانه ترک کردند.
گروه عملیات آبی-خاکی «ماکین آیلند» نیز دوشنبه گذشته سن‌دیگو را به مقصد خاورمیانه ترک کرد.
حدود  ۲۲۰۰ تفنگدار دریایی در قالب این گروه آبی-خاکی به خاورمیانه اعزام می‌شوند.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو گروه عملیات آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
با این تمرکز نیرو در خاورمیانه، فرماندهان گزینه‌های متعددی برای مواجهه با ایران در اختیار خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72580" target="_blank">📅 18:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jm2rAn93S8zdQ38D3xgCBRg0rgwSb8QzZ_qNpymk1oD7-Pfkqiyl8ra-Ru5h1p14cA_5FZSmGgLGr_R8FjPBLHeZOdRTAWhSAtZa2q7-HGULldAuYRogqCgA7aJtJxhNz_DPydg_22zuo8w31muSo5HGac_7ywyXZSqDcxzCYB6QxYpIkiZDOVlVqcq9AWn3pfBHq_YZeyvSlrdm_T4m5_2s1YX2tFl0gCSD-KI9zwRYfnIkhh0Rq6Fv3P-I-0KTrrOffOQ-5JLhsLN_OKFEpj1Kz5bqko_ET3WfnrJy-zneScP4mj5Ybhs6sY82Bfyso-urA4AVT1En2ykWDxwTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد، خواننده آهنگ سنی نردن گوردوم، از بدن فوق جذاب و عضلانیش رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72579" target="_blank">📅 17:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=YCLVGQkuRK6kCmHuiv0ydZ2IdXCFRPtEguBCnxvpzXs_fuByfkBMclH7rQolA3QtkeTi4ytMskosIcLbZJB2zr3zxXR8Gbd-z0xV7RQRVxAJivdFXMQqgSTY34toScHAVlNssIwTE0R2d2WMSckS2K114ONWySgFJRXU7fF3D0sLlOPIdGJ-a3CZJL8l1BsTnPCihOrLinwvVC_6TTcqTytATKSDhdZncjKu-TxDy02KCfftJQhyKIpd3efrlZZ_1WperqOBHLODEuK9rre6YRKP8cIveYiiVzZh0Ev2Md4jT22_2J9Rpb6eyJ6OHFLpbAqRG5MX14wPxrNPOrrFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=YCLVGQkuRK6kCmHuiv0ydZ2IdXCFRPtEguBCnxvpzXs_fuByfkBMclH7rQolA3QtkeTi4ytMskosIcLbZJB2zr3zxXR8Gbd-z0xV7RQRVxAJivdFXMQqgSTY34toScHAVlNssIwTE0R2d2WMSckS2K114ONWySgFJRXU7fF3D0sLlOPIdGJ-a3CZJL8l1BsTnPCihOrLinwvVC_6TTcqTytATKSDhdZncjKu-TxDy02KCfftJQhyKIpd3efrlZZ_1WperqOBHLODEuK9rre6YRKP8cIveYiiVzZh0Ev2Md4jT22_2J9Rpb6eyJ6OHFLpbAqRG5MX14wPxrNPOrrFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=c9T0VPuTDl0XJIYhzc67wYZ-GWmBNv7LjME65DhNOH6AVYqqJTUgxaR3p1J781dJ9iLmH1JZPNDpmgIi68_mtvt_8_D7JMhhMr3EiYafwtzKbQ0FSZjUhzPYXP4YkgtTFNNsmmYlQ-cHbpxJ3Y9zrQ6JCcEOWPexj-gqN14F2jYzWX-LBY2RXAFU6lsMjZxyX2SHt8JG9b6aSE0DJH5Rkeb0VnEiIH8eMAqt04dwQ2BZF55X3OONwCpFOVfrs4DuJN-24hnQgS3EABrNlwRCTsdHAqAyWFdbJoKcUHsXLbU9tdcAg70ObD78g1AGtG3wwBmrmvFXCN6ziOLYnjmeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=c9T0VPuTDl0XJIYhzc67wYZ-GWmBNv7LjME65DhNOH6AVYqqJTUgxaR3p1J781dJ9iLmH1JZPNDpmgIi68_mtvt_8_D7JMhhMr3EiYafwtzKbQ0FSZjUhzPYXP4YkgtTFNNsmmYlQ-cHbpxJ3Y9zrQ6JCcEOWPexj-gqN14F2jYzWX-LBY2RXAFU6lsMjZxyX2SHt8JG9b6aSE0DJH5Rkeb0VnEiIH8eMAqt04dwQ2BZF55X3OONwCpFOVfrs4DuJN-24hnQgS3EABrNlwRCTsdHAqAyWFdbJoKcUHsXLbU9tdcAg70ObD78g1AGtG3wwBmrmvFXCN6ziOLYnjmeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=KA-_DxboYevv2JZfpThzseYCWLY4lI-XR2Ve7yz0tph3EcCvsURmc8I2RNnZLTVGhWgAqmBeLV_apK_go6MPqnTpxKXHs4WRymltVSIENoA0Sdb9wucwT1rvze_RiWtK46f22czsFvz5GHUFqPw3wb5Q4okZibVRFowaHp8TzqIyB6DFt4uI9w_EM5kEPXOV7QqUKwRJQN-lfu_RO7sVbEIkJVO1NXfqNRfh4v1WKUUt5DdwF4q_QDDo3Q7nWGyZjDW_eMeRrpVhybBdTfcY6-EzPuVWS0penDXZqJO9uo7eMGMYt2lkXcK-UMt1bRtWvRZ1kHYE5O1vAFi8flgRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=KA-_DxboYevv2JZfpThzseYCWLY4lI-XR2Ve7yz0tph3EcCvsURmc8I2RNnZLTVGhWgAqmBeLV_apK_go6MPqnTpxKXHs4WRymltVSIENoA0Sdb9wucwT1rvze_RiWtK46f22czsFvz5GHUFqPw3wb5Q4okZibVRFowaHp8TzqIyB6DFt4uI9w_EM5kEPXOV7QqUKwRJQN-lfu_RO7sVbEIkJVO1NXfqNRfh4v1WKUUt5DdwF4q_QDDo3Q7nWGyZjDW_eMeRrpVhybBdTfcY6-EzPuVWS0penDXZqJO9uo7eMGMYt2lkXcK-UMt1bRtWvRZ1kHYE5O1vAFi8flgRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟
ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم، اما می‌خواستم پیش‌تر بروم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72569" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.  ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.  سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟  ترامپ: چون با نابودی ایران، صلح را…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72568" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سؤال: در مورد ایران، آیا قصد دارید پس از انتخابات میان‌دوره‌ای، حملات هوایی را تشدید کنید؟ گزارش‌هایی در این باره وجود داشته است.
ترامپ: ممکن است. ما سلاح‌های زیادی در اختیار داریم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72567" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.
ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.
سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟
ترامپ: چون با نابودی ایران، صلح را در جهان برقرار می‌کنیم. به عقیده من، تا زمانی که ایران وجود دارد، هرگز نمی‌توان به صلح دست یافت.
@News_Hut
| time</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72566" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو با مسافری که به توقف حمله به کابین خلبان فلای‌دوبی کمک کرده بود، ملاقات کرد و به او گفت: «بدون شما، می‌توانست یک یازده سپتامبر دیگر باشد.»
یانیو حیون، لوله‌کشی که هنوز پیراهن خونین به تن دارد، گفت که مهاجم را خفه کرده و کنترل‌ها را به عقب کشیده است.
او به نتانیاهو گفت که برنامه‌های تحقیقات سقوط هواپیما را از تلویزیون تماشا می‌کند و به این ترتیب می‌داند که چگونه باید کنترل‌ها را به عقب بکشد.
او هیچ سابقه هوانوردی یا نظامی ذکر شده در گزارش‌ها ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72565" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=YEgpRfpkSfoqeHnSxL0dCfAk_xMuCLOrRJGgvWeSadeI-Vl0B_DWx3i2x2ojd-DACxsD0FMJ_s8vNd-OnyTlatT3IDAdt7Q9a6Wq9gDjKBv1079KWVxRBfPVvOO_tIuzCD--GXHgI7s1_vN6FzzmYTxOeYb9JMBCsS5fTvJRMchUbxw2UC1vmkydh-ruR56pSdLHN6n-QZodSIaeiLcdZdn7wW8hyewwNyXLWnNuIJBoEC8Sc_HQ-oiqQE3gBF4IADGg_Jim67I5TPgWhycf_cAvSpEfjqPhtERQz-0r4t1HPyka6mnYSp73oCkVGV_8TszHrzfQl3UDRRpxf8okGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=YEgpRfpkSfoqeHnSxL0dCfAk_xMuCLOrRJGgvWeSadeI-Vl0B_DWx3i2x2ojd-DACxsD0FMJ_s8vNd-OnyTlatT3IDAdt7Q9a6Wq9gDjKBv1079KWVxRBfPVvOO_tIuzCD--GXHgI7s1_vN6FzzmYTxOeYb9JMBCsS5fTvJRMchUbxw2UC1vmkydh-ruR56pSdLHN6n-QZodSIaeiLcdZdn7wW8hyewwNyXLWnNuIJBoEC8Sc_HQ-oiqQE3gBF4IADGg_Jim67I5TPgWhycf_cAvSpEfjqPhtERQz-0r4t1HPyka6mnYSp73oCkVGV_8TszHrzfQl3UDRRpxf8okGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام جمهوری اسلامی:‌
گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل وارد کشور شدن، مردم در محلات مراقب باشن.
جریاناتی در محلات استقرار پیدا کردن تا عملیات‌های ترور انجام بدن.
اومدن نتانیاهو به امارات رو جدی بگیریم. طرح نتانیاهو اینه که به‌جای اسرائیل از امارات بجنگه.
+البته این چیزا رو میگن تا تو اعتراضات احتمالی بخاطر تور و گرونی بهونه قتل‌عام دوباره مردم رو داشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72564" target="_blank">📅 14:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-0CRD5FK_adzv1VbbvV8oncFEVimkVkB5MIAmPM4Lysxuqjdw3bqrYQdZOqB0XbbGMcM90dMM3KeUgOcUtM3DOd_Znga9WS3jO_9PweUbiK998gktyW9Hwlozm2E30Bthr0JR0N68xVjl83og53KBBlf75z11F2kkSFoVEbolJlllucuVmYdFFWm552hgC1inJjTuitu-sYp3NgdyBa4FhHYdfaGrgm9aztxz62QLaC-HPhezRKgY1Tq_XQm2te1jXRA2VEbiiXgiNeFZVssN9eqlPq9_ZNYFyBxk3agEfvqPoxA2-BURMidDQrhpJExeCrB1FgiyWOKvM0WaSAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: ممکنه ظرف دو هفته «چیزی از اقتصاد ایران باقی نمونه».
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72563" target="_blank">📅 13:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEVuZMXcm5EMpr81QMyAOTeHZL8iY5bpvWGqckefF4H9Jw6n8pSXeBOAKBxVOZs8y0vaFkrsefOoed826m2pomrT5XkVlxoTn1Vu99qkQTBvcrzcbZihCJKtzRGnzIqkbdaWywbvtAdmIAqs2XiRxkx7quHIzW_kpQU0iwfEr7oVsdqENd24U3XahKD9qNp5EP3xsIfFqhBPcodB8OoKaIctn-SZNSQCa7PDIw_HkKGeezDoxhu9JACoifSQ27CSVmLyJS1mt93KZkgDcu5QS9TZ3YS6g__pJjndw7REIPm2UAS2H7hTvz-CINcuxHr6rnHXruLUn0gVgUdPKrXmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCQBFKGwamP3uaP-v5qg6vJmGM7nCq8moPwbZL5uwSf_c6o9nquNFjP-U6sARyKbbUTgXNmnFJbG7GfpH_r23mRlvKdGkGlclcgMDreicYEVoYHMssXmoIWFIOQvpXhx0YvEHuArGKo2bh7V5bUoBbLPPeqZYN-wDD94tXDulaRi0JC9dXojuGgDdqm6DR0fhMZyI8p0-PdPa5Zy6zN2_lxSrpsOoz5biW1WPVrqUuOUBStTd1l_fwdZ0q1pKOD1QMHDE6K6FZ0PyK6nPby7OGo6Rih0W6SE5wBdQYT6mkjuE-oE1AdYHpNVHN4_l3AynwgRXpUiju3wILKQMzmX7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیژن مرتضوی که همین دو سه روز پیش گفته بود شایعات باور نکنید و نمیام ایران دیروز لایو گذاشته که اومده تهران
+پست چند ماه پیش بیژن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72561" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ee82707.mp4?token=mbZqcrFpzLzpwNrlC_H5pRsRBpJZCcSkygwQLWAKYNLzWyzulmOl8TlyNq5hm0a4jiwhj_ZOrvoSc8qw1uBJqGJm2FnjW-gu4X9VgyT3Az4Q097bIFa_UwM6Kz-vT1uI74ymenlxuh2D3IHSMgcSK16HgGwZ9YkmDRzn3Ocbs5RbyZzjrkj5cH7soHUW6StnELoR-ZDpymL7h10ySqvPFCz_ekplngSBOADY5EbkRHC8i4qm0Bt51nK7gP8T9HhJ1eXHXnZv1PgzHzBnW0YWm486AJgfQJwhsti62k3EAuHkWS961q463e6Y1b8NbGEI1T5zPzN6YVSiaf1FVJ7bTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ee82707.mp4?token=mbZqcrFpzLzpwNrlC_H5pRsRBpJZCcSkygwQLWAKYNLzWyzulmOl8TlyNq5hm0a4jiwhj_ZOrvoSc8qw1uBJqGJm2FnjW-gu4X9VgyT3Az4Q097bIFa_UwM6Kz-vT1uI74ymenlxuh2D3IHSMgcSK16HgGwZ9YkmDRzn3Ocbs5RbyZzjrkj5cH7soHUW6StnELoR-ZDpymL7h10ySqvPFCz_ekplngSBOADY5EbkRHC8i4qm0Bt51nK7gP8T9HhJ1eXHXnZv1PgzHzBnW0YWm486AJgfQJwhsti62k3EAuHkWS961q463e6Y1b8NbGEI1T5zPzN6YVSiaf1FVJ7bTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد حافظ حکمی معاون وزیر ارتباطات و فناوری اطلاعات با اشاره به قابلیت‌های فعلی استارلینک و فعال شدن قریب‌الوقوع «Direct to Cell» تو سط ماهواره‌های استارلینک و امکان اتصال مستقیم تلفن‌های همراه به ماهواره گفت:
«اگر استارلینک فراگیر شود، وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!»
اگر قابلیت اتصال مستقیم گوشی‌های موبایل به ماهواره‌های استارلینک فعال شود، سازوکارهایی مانند رجیستری تلفن همراه عملاً کارایی خود را از دست می‌دهند و شناسایی گوشی و مالک آن غیر ممکن خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72560" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72559" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh16uV_6wYb7IbTAp5PhY8VTEwTPRllYMpbthn9ZBvIjgGMt1E6q6njA2GoD_bOh9HXrBGkkrv096rWaRo7qvmwYQuw0LofvMq1tsNoH0F9JQ_RAe8yvz-DuwQvGt5CmJGYymZYXibIKveyerpJevSkpoixFwaNNQ9_T1dYdl5gQ6k882FxVj1h_EPPKKBxhx_XGhO7ww_NHdAqgcASdZMo7DT1vVRrbIAY-Mu4HLuOxMKFlTfd81OHgTQakJl7Vx0QI90fuKiqv_7SBc-Tkn3ygbpm6d4iScmRUSFJqvtKGLjt3xmFzcBGhVOtP4WZ7j3yMuVs1riWZQaPDkr606w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72558" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9t5q7gEQ7eaqYYpErWIuXXI0eiZXYYLnOD_u8COBLuG1tuYCTWgbiBC7lkSfemGpPyAazeB6zxnXTabGUKmuarBHODxumFBbsMbFjHPUevGtjuPk3CoeJkaCExQRPZSQ8VFoqmyl2Q7gqWPbCjnA29I0ypM_kwr8PKChAL5_CLcRZTfrGWJHeZJJu3ReqTDcT4klH3LA6Gg01tiED4ATuMZrbhDZEB3gdspt1_H7nbKSfKsLvRQ_0ZLHzS69SNyRavtAS_UlkHeQ-bgvPmBOyapy6BaCDBwTTJ-SnzHZTd6otJEW7RtF9QoFX3kq_uPgTSIRj_bdPRtpzutU7HgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد که نیروهای آمریکایی در چارچوب محاصره بنادر ایران، مسیر ۱۲۵ کشتی تجاری را تغییر داده‌اند. این رقم نسبت به گزارش روز جمعه، حاکی از تغییر مسیر ۳ کشتی دیگر است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72557" target="_blank">📅 12:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=YKDeWyF-SaQ-eEU4KIXeunjnHcJInlWEgJo_tZ_0Bg0JmXKxw5eucfOUCN5um8Jz90q1J7-_8IWZxm6cSi7Vh8L712e_SGXXrq-DM0d37tLE1ag4P0tSy8mJHQb3kjcorEevYSnGqQVX3kw1qPZnzaGav9F6Vo5HqmuwtKAbGuZi6PoK_Gms9iuM3a0MaC0QN8DXpccXnDOZxy__lGP3a4lMXcJ5BIB48OaT3WZeo8q3w_1Yaej6ZFi2RBRt4Zd8jUydpPZiN6A-WhlBZGZEim_lldys9Hj5xvRlNhJIZM6InOhuAbiiL4SD42amgMFcPMXXpGKd4AoZGa6mUyjoBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=YKDeWyF-SaQ-eEU4KIXeunjnHcJInlWEgJo_tZ_0Bg0JmXKxw5eucfOUCN5um8Jz90q1J7-_8IWZxm6cSi7Vh8L712e_SGXXrq-DM0d37tLE1ag4P0tSy8mJHQb3kjcorEevYSnGqQVX3kw1qPZnzaGav9F6Vo5HqmuwtKAbGuZi6PoK_Gms9iuM3a0MaC0QN8DXpccXnDOZxy__lGP3a4lMXcJ5BIB48OaT3WZeo8q3w_1Yaej6ZFi2RBRt4Zd8jUydpPZiN6A-WhlBZGZEim_lldys9Hj5xvRlNhJIZM6InOhuAbiiL4SD42amgMFcPMXXpGKd4AoZGa6mUyjoBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر از هموطنان رفته بودن شمال که توی مسیر پلنگ مازندران رو هم دیدن:)
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72556" target="_blank">📅 11:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbT3PQLYl4d0VIpnW19meby6QZ99DPcJvJ2EptnQSS5WyRWbTGVlxEKFVOxLUg_ax01nkFo9K2696DFKRgsxO0WfRM08uOjuLciUVCYEpXyaDdVmYy3A_RManYHP0JH-rL9bJEQmrew-vs4imE0nUsFcfsnNFE3XXuKle2AvF0koom_V37XKxMPvcooUIFO4VuGC00IICn2UPUoO0A7yq7chGAFXZMPd90dvUsGJg_TfwF4gF9HoAQ-bNnNbPxBuL19kqNiCgDSoEzIqFUxsRRJ5FlHRraK4iUbk-GwksAnAuJ2z7rCgbNqOClPyg0v-gX9x0LtZ7oXnlt7TM_Lsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛اکسیوس:مارکو روبیو وزیر امور خارجه بعد از اینکه مذاکرات میان آمریکا و ایران در روز دوشنبه به بن‌بست خورد،به هیئت نمایندگی ایران ازجمله عباس عراقچی دستور داد که فوراً امریکا رو ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72555" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=X0JPWYONL9OQ0H3yG9YMe4BEfSMtfGed-lKQwNVgcwiJ5ziT3q4slpMfVmeA5oU6amTnSS8uUyEM5FATHt69pGkv9XPpC6kThhj2RKtykmRHHGobaJyVXPmJ3B9iNvVpI-pFeymJxOEB5pixvcna3sFR1cUNNs3JGOFvHcNfbkLwapVoVwWAVdCS-Hj08Yegia7C8AdTFfi2CFtQNW0NCHmfw6FFct4P6ms_9l7WeQOFdG4XW4MkwoY-zD8fjI8nAOjmo3LxtE-wJ9AOtBsBC58_ngQz_jup4i9sXTAuf9l5-p-tkuCQlU_FZVeqwLTKuY9RkWBNMSwbrS6nsd0nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=X0JPWYONL9OQ0H3yG9YMe4BEfSMtfGed-lKQwNVgcwiJ5ziT3q4slpMfVmeA5oU6amTnSS8uUyEM5FATHt69pGkv9XPpC6kThhj2RKtykmRHHGobaJyVXPmJ3B9iNvVpI-pFeymJxOEB5pixvcna3sFR1cUNNs3JGOFvHcNfbkLwapVoVwWAVdCS-Hj08Yegia7C8AdTFfi2CFtQNW0NCHmfw6FFct4P6ms_9l7WeQOFdG4XW4MkwoY-zD8fjI8nAOjmo3LxtE-wJ9AOtBsBC58_ngQz_jup4i9sXTAuf9l5-p-tkuCQlU_FZVeqwLTKuY9RkWBNMSwbrS6nsd0nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از وبینارهای مملکت بین یه دختر به اسم "پرنیان" که پزشکی قبول شده بود و "اشکان" که کنکور مردود شده بود، یه مسابقه برگزار شد.
نتیجه جوری شد که همه آخرش ایستاده اشکان رو تشویق کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72554" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pg50ZlN-2Ili6q-Nt-yRs3AYIIiVNzA07NVWoDZWtjS1hI_tdXIcvQGkxX9iqFPmVkQCd45boZ4IY5qEDHIF6WLqrPMPQhus7lM_GnVI9b8nPFoPDpK0LbFPbPBIUg26_GZCnkrz9IDsSq8ara71vgOya7jP46duu9N9Knhffcy3AKkWNwuiLXl25cEjwkeMu3200MQUz0HCvIVehEeplOvzuBwwcJUtPcooPPgLRd8BynwvGch0QW-3p4UA7rfefE-RTiV4nmuiWq7Xe5kbeE0-ib-f8o73a3C2TDuFk4VBQpPQyCA_Hf5kVCx2Y60sMvk0his1T_yLQGjdfundqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AiUxi-LC_csMRBFSltU9iZrbL7qYHnDnWOfkbhsWM5SP2bYQ70AREYgA3EnNt5I_T7a9qo5SELjPNfWT0ZsxuzdowxnLnSdR_eXRiHBC9IlUhcTNyx1w9IVXkAEzeJ_dQgshVVH7cwVi9q0Cta14IQOxqn78yA5cAQ5uL4fFgbl9T17Balq5tdAoTh1ayEB6keBrDWGDDW7ACdJZs4RBvxQ4zKfn_RFFYAHmqPgjbY89PZsc3XnYU57kfxy5SIvY9Q0nSItqXfpdYSuKtgaJ_0k4qeFGd8V7IXXGCOSpzoN5svNwpsJle-qAv3x22pVsjHqaKENFkqB89qh2ZQd7jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از حامیان حکومت: من 13 ساله که یه بیماری درمان نشدنی دارم، دکترا قطع امید کردن و گفتن و تا آخر عمر درگیرشی.
تا اینکه یه شب رهبر شهید اومد به خوابم، بهم گفت درسته من کشته شدم، ولی مملکت رو اداره میکنم.
یهو اسمم رو صدا زد، مصطفی! رفتم جلو و بهم انگشتر هدیه داد، صبح که از خواب پاشدم دیدم الله اکبر! هیچ اثری از اون بیماری نیست و کامل شفا گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72552" target="_blank">📅 10:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72551">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=J24Bm1DSLCsUruQxHWS2goIniSkagbavjh2slGW5ZoFHn5ctAwSgB6yafT_VNGuGKFjPI-iOtyDW-8wfmfDtQo_vO9s8nf0w0V-VvScshwRv2djljI310XR-tC7pM3l6IULyREDKCmAloSB57wUAYzXH4gweBip4s7ChuU8VYPmJA7rElWgCchBYhB-slSy4T0sl0-O1x3vvkg1dgtcLOjGaGeVLZw9hOx7xxhXjuSJPcZ3d2Spp3Va5hNS1m736WqdcpiGsd6jlJuOY_DNuUI_Kf-PU74IwzHQ7YXgvk0_V68ir9iqn-JQazD3ipU_6Y7RKKCoxtKUyr__dUZZEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=J24Bm1DSLCsUruQxHWS2goIniSkagbavjh2slGW5ZoFHn5ctAwSgB6yafT_VNGuGKFjPI-iOtyDW-8wfmfDtQo_vO9s8nf0w0V-VvScshwRv2djljI310XR-tC7pM3l6IULyREDKCmAloSB57wUAYzXH4gweBip4s7ChuU8VYPmJA7rElWgCchBYhB-slSy4T0sl0-O1x3vvkg1dgtcLOjGaGeVLZw9hOx7xxhXjuSJPcZ3d2Spp3Va5hNS1m736WqdcpiGsd6jlJuOY_DNuUI_Kf-PU74IwzHQ7YXgvk0_V68ir9iqn-JQazD3ipU_6Y7RKKCoxtKUyr__dUZZEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کلاسای دانشگاه مملکت، یدونه پسر، با ۵۰ تا دختر، همکلاسی شده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72551" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Qqq3e6F_3h84Siw_sTe1i9qA294fp1jwsZNqUHEtKgEvUVH_Fv1m__zz15FttMOXIvyIHQ2BC3fa1MsPnjYNuKIMnwwLHGpT0bUGWuSJSnyvcaOAth32X_z_575O4gsoMeP1IxzTbWlJNZX9Lp4XzmDm8323eSWCrmSaKhNLaD3L0-dyv0H0Ks--nqp4ILOHX7ZJFpOZ6mcoxmZ8apkXYuw3iE0MieJ5OKH1pgEGueQhUIze6BTWx7_gNdxkxnrbljJXpPL4a8mv2atVdH3Iw4egHuBXXdJXGxe2d3cCgy7ko1ghp3nYje9_lYzd4iXgcgAnBrqBH-Llu6Gwn2fn2jJKD1FQ80PYLuJiPreWO_SkVhs7lNCZSSlcu7aDKf3agjGgFkXQk8oexyDcV1bWZasK9A6ONx7r-j_HuXkLUxFExhMil5M7EcNIibWGxVumj4j8lceV0-VksvpheaobWb1EHk-LQ-kkXe0R_wO80AJHxLzUCvCzH-ZZUAn-yR9wHeATAXeodCqukNHz9D_1KhFQ33-1Fgml6umIapPu9mb-G-InPCjJ8hhC1hDlwuexTnlmLwigbzxElH2M1UQtMAbDQjTRZwVZvegOnATSpNclX0msFv7hCvRyabdZD2TPenHaIOvzOWoJfapj9kdW3gmUEJsctDzL7vOFTA2CNUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Qqq3e6F_3h84Siw_sTe1i9qA294fp1jwsZNqUHEtKgEvUVH_Fv1m__zz15FttMOXIvyIHQ2BC3fa1MsPnjYNuKIMnwwLHGpT0bUGWuSJSnyvcaOAth32X_z_575O4gsoMeP1IxzTbWlJNZX9Lp4XzmDm8323eSWCrmSaKhNLaD3L0-dyv0H0Ks--nqp4ILOHX7ZJFpOZ6mcoxmZ8apkXYuw3iE0MieJ5OKH1pgEGueQhUIze6BTWx7_gNdxkxnrbljJXpPL4a8mv2atVdH3Iw4egHuBXXdJXGxe2d3cCgy7ko1ghp3nYje9_lYzd4iXgcgAnBrqBH-Llu6Gwn2fn2jJKD1FQ80PYLuJiPreWO_SkVhs7lNCZSSlcu7aDKf3agjGgFkXQk8oexyDcV1bWZasK9A6ONx7r-j_HuXkLUxFExhMil5M7EcNIibWGxVumj4j8lceV0-VksvpheaobWb1EHk-LQ-kkXe0R_wO80AJHxLzUCvCzH-ZZUAn-yR9wHeATAXeodCqukNHz9D_1KhFQ33-1Fgml6umIapPu9mb-G-InPCjJ8hhC1hDlwuexTnlmLwigbzxElH2M1UQtMAbDQjTRZwVZvegOnATSpNclX0msFv7hCvRyabdZD2TPenHaIOvzOWoJfapj9kdW3gmUEJsctDzL7vOFTA2CNUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اولین موشک اتمی جمهوری اسلامی در  ایتا و روبیکا آزمایش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72550" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QGB57s9gtxLy_OBDAQ6XYpGr0nSdUNO29RDneEcxTFkUaw1L9II6rM7sQgegsgThRmtci6qzFWEp5m1BT3wW6wwzJ6-KpRm7eybOiJLSSax2IOO3FGWTubEAUmjBMB7HsVyEOveGQrvX-cBjlQnbAn4o21__2VwYs5IQe9vce-29_xizoCzPOUO6RbFrvaNKNx5eBp9JzflvkCCA9So53GULCoNKU-8WBeN3XvoxuU2JdbtV-i5aov4NxvKQSS-Zjd4LBw2-DZ0DjoFqtmVPaPTWw55AH-85lOLMTx9KRYWK5C3wIEcuTtUUJ0Kif-ciMlU9IEU0qrCTo9Jpd9bGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QhxyagFuFpcJ9ac82v-P7EtG5VejYeQXK4jdObLC_Vkpe-aI8Pw15_INMiqVmsR9b5r6U83P0wNenyEWklKRQHVK6K92kAbGJorA-SzczV7iFtkd_9I-A3sSoNi0LI2OmUxlQGtgkd9NDtTkZSiCBw3omiJG_j62WD_sA_JQwvYmdmr0CoQnnevwKJNeb-b5XLq4bi-SvIexse_YtPuHFss3y40iEEevs5rRaX0TmMZeG9BY2nf9rwBiTRxvIqjJc0OGeGN8JAjm0cu1Cf9-Gy8UZBFkJkG_Xp0yCMdQn3YPr5bClyPIBgtKG1TY7F9wBHcIdg7j2bzqLymf3mb5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrvncBux67vF_nTVRTrGavo7iY5Ujs9gdIwcYOfvPWzLgcWzyI7OCC6P4gTA3zmfFsfWwxJSk5kfp0GfULTna5GD0aJk_Cy8NxLnBxPDgNtZwKIKF7wlb1d95rXxJW8KGni5cD3Yx6nQbOUxp6kiL7FW-lQMoYBB3pe6DOdCOxjVQY1Om57gcPTXknPbSlZ8l-0J5FtpOFMxgskcUxeVt05WWiBITyzPfrTRVUFP5ZKrB6aySzlXdb2kcsPA0FzCqOYvc8Y8aZJTGALuYoPtnzGKGoae_WJ_24jOI0ws5UZwnSpCIZ7G4Im0kljcElt4v_JgLKGLWOVvvGQP0wX2Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=besceTWoFXrOxu_5d9WmASCPin6aWVCr7TtKBpXhMRHhBdBCYaGQeHXz-WN_VJM3YBBQRy2jbDVBctc5mV7gIfZxwGBdU39KnrXGOxHrU__m_2nmSp8xr7uQ5dzfD6FN4Z4QrDVpxnVtsbE-19ZUZ6PlqC3t1h1d4Hc6053nTZna4oTFoN1nLbr0MRrYScU6s-Sss53tuCoYJjuKBcbyW6MDkSTpG5ne9dedEd112aJUoxJhmHkKsmIx1fD7ccXwMxXJhwXh64SLkJauoxFJonRQkbH4MCZ-P-jkvZYFnvMr0wd2w6yRuvm-WVKU38lV_7_0HWbL749SQLaUyNzVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=besceTWoFXrOxu_5d9WmASCPin6aWVCr7TtKBpXhMRHhBdBCYaGQeHXz-WN_VJM3YBBQRy2jbDVBctc5mV7gIfZxwGBdU39KnrXGOxHrU__m_2nmSp8xr7uQ5dzfD6FN4Z4QrDVpxnVtsbE-19ZUZ6PlqC3t1h1d4Hc6053nTZna4oTFoN1nLbr0MRrYScU6s-Sss53tuCoYJjuKBcbyW6MDkSTpG5ne9dedEd112aJUoxJhmHkKsmIx1fD7ccXwMxXJhwXh64SLkJauoxFJonRQkbH4MCZ-P-jkvZYFnvMr0wd2w6yRuvm-WVKU38lV_7_0HWbL749SQLaUyNzVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دارن خودشون به جنایت جمهوری اسلامی اعتراف میکنن!
دو روز پیش توی بندر کنگان، مامورا می‌ریزن خونه یه نفر و جلو خواهرش به رگبار میبندنش!
انگار گزارش داده بودن اینا گازوئیل قاچاق میکنن و مأمورا ریختن در خونشون، تا پسره درو باز میکنه، به رگبار میبندنش.
پسره، باباش جانباز شیمیایی جنگ هشت ساله بوده و خونوادش ۲۰۰ شب و هر شب توی تجمعات شبانه شرکت میکردن!
حالا خواهرش پست گذاشته که مردم راست میگفتن، این حکومت قاتله، ما اشتباه کردیم، داداشم و رفیق بی گناهش رو به رگبار بستن.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72546" target="_blank">📅 09:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72545" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/news_hut/72544" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJdM2DuJ4vbg6cmWMutU0H4yE2Zwx1J3tYJDypSkVUPyYfAMUuf2IMBo9-6sRF69EwMKZVn-GwV5snFFoKBisAnyigYDpt2c2hZXXECb6CcAOpyPY0kije99p32Ux73v77hJQwoyoAYGkyJJzyqxpq3tXF7rXmeZZtyh65K3ifyvOC94i_5rgnnBML5DJH_u35rilpCk3uULBad3VtIlkFGbNSom4bzWPSnvDXAY1NeI0afDMpsnsbwbQH2RT1nx432k3A9OakAnC6Ggl1eY2yPSZHKWrFTu1iK4_O0-4MHrP9ZsKcIjpaAX0bRV2nbEdKh8iWV4lTxR-VHArCNuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز پنج فروند سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز؛
+دارن نفتکش رد میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72543" target="_blank">📅 01:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=FIeH1tzga7gpzei4nbgXTYE15dfHTIf_gHof54dBL18VCpDA1QJXcOxQTj-bzHqm-zCczq4Mdu6Gx-Tvz5rvrdHUc8M2FwWRQZTh1nXciomZV675C5mwEKYCaAZJrC7qw0pNIFgxYJJlLeTBzh_mSYZibZwLSIxCz0F8NJwGo1BbOVPD8HhB9cv9BYmRBxIV5aPqV_nPHycOMSoPWGgAq9WAu_cYPYgtlq8Dfh7qm62xfeRV4vDMYr3mOF5tixnmKhh45T5j0uYxOyiPj4xnapbxIugbVGM4h_1Tgfgb4TUkqMi3kcA3lWDPnKtrdyEjhZbrC5kHu9y0jRQ_uVfuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=FIeH1tzga7gpzei4nbgXTYE15dfHTIf_gHof54dBL18VCpDA1QJXcOxQTj-bzHqm-zCczq4Mdu6Gx-Tvz5rvrdHUc8M2FwWRQZTh1nXciomZV675C5mwEKYCaAZJrC7qw0pNIFgxYJJlLeTBzh_mSYZibZwLSIxCz0F8NJwGo1BbOVPD8HhB9cv9BYmRBxIV5aPqV_nPHycOMSoPWGgAq9WAu_cYPYgtlq8Dfh7qm62xfeRV4vDMYr3mOF5tixnmKhh45T5j0uYxOyiPj4xnapbxIugbVGM4h_1Tgfgb4TUkqMi3kcA3lWDPnKtrdyEjhZbrC5kHu9y0jRQ_uVfuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:
شما ایرانی‌ها را دیوانه توصیف می‌کنید. چطور می‌توان با آدم‌های دیوانه به توافق رسید؟
ترامپ:
شاید هم آن‌ها را منفجر کنید. ما باید در این باره تصمیم بگیریم. یا آن‌ها را منفجر می‌کنیم یا توافق می‌کنیم. زمانش دارد فرا می‌رسد. ماجرا خیلی زود به پایان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72542" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=KFkwF1OT_wX0qntptTt9K_ninD1QmQdjloLcr9QHI32dqzrVr6Yvb0dn5h1Eyeh0QgefArqAAXvUXtcNzjmgGsc0SXVc2He_clZJ6fDq6GQ-xnc5NbNbVxzYJAEjyFq_qGTi3XHRMvy3Stiej1Sjtncswf8KoajKU2_nqmWSwfZ5W6nOJvtESCo8oqEjz24k-7kRgaqCV6e-lmgvqe4_yiNsaOPG71pzx7Ly7Yprajq_s2FTcwfsENhqcMdZpOSSxmLtoyhjL69IHePdAnuh_Vp2ReQfSWnexqP2gtfJAjt_x7WYgwIUGzUoQuld1Zo_vcBxqSqYn6yrw9XUZs-Irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=KFkwF1OT_wX0qntptTt9K_ninD1QmQdjloLcr9QHI32dqzrVr6Yvb0dn5h1Eyeh0QgefArqAAXvUXtcNzjmgGsc0SXVc2He_clZJ6fDq6GQ-xnc5NbNbVxzYJAEjyFq_qGTi3XHRMvy3Stiej1Sjtncswf8KoajKU2_nqmWSwfZ5W6nOJvtESCo8oqEjz24k-7kRgaqCV6e-lmgvqe4_yiNsaOPG71pzx7Ly7Yprajq_s2FTcwfsENhqcMdZpOSSxmLtoyhjL69IHePdAnuh_Vp2ReQfSWnexqP2gtfJAjt_x7WYgwIUGzUoQuld1Zo_vcBxqSqYn6yrw9XUZs-Irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رهبران ایران با تمام قوا برای به دست گرفتن کنترل می‌جنگند؛ اما کنترلِ چه چیزی؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72541" target="_blank">📅 00:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=eWIitt4xkTmTMnzGI8eCtR8LqA0M_RSysxEeNJhmi-iPmbBjOUTuD1Khk1B4mBzLwuS_hL1tRZc7BM755gNkElBNqm-Tb9z2VxtpiJn-aMJGCcxDWh3R4GQYsjgZVdhVht6FSZ0KbTeOeiOkHroCIV1cc1gSV7EaGg2fqpfn6CwQaJVIGKCeMmWITG6i9AbP5M4y1Dfc3pshejrnZuL2GIETC8b4P4GzLsCaGwYXgQpwpf9QkRlyhSedgTuy8pf9Qn0kL1NblG4poSEH32BqQK1jFm9MkOClCh-4YLbes1CFVh96oUbJSKW-3wFIhM1wWpL5XNqk7WA7rnt1xMRPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=eWIitt4xkTmTMnzGI8eCtR8LqA0M_RSysxEeNJhmi-iPmbBjOUTuD1Khk1B4mBzLwuS_hL1tRZc7BM755gNkElBNqm-Tb9z2VxtpiJn-aMJGCcxDWh3R4GQYsjgZVdhVht6FSZ0KbTeOeiOkHroCIV1cc1gSV7EaGg2fqpfn6CwQaJVIGKCeMmWITG6i9AbP5M4y1Dfc3pshejrnZuL2GIETC8b4P4GzLsCaGwYXgQpwpf9QkRlyhSedgTuy8pf9Qn0kL1NblG4poSEH32BqQK1jFm9MkOClCh-4YLbes1CFVh96oUbJSKW-3wFIhM1wWpL5XNqk7WA7rnt1xMRPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=fAflQSZfB_1X5EPMqgUGJtqK7wCeP0bmw6wqnFdVEomI898wGfT31UYoXdTM7G0gZe40TcrkF0KX40xE6tZhOuEKYUCl6UdxIjesGUfPWPxdCF7t1xv0dArfeq85k0tzxnHD5adRIr4fVK8xbao3V6cXIRRZB95Npz_VQ8Dh7dUhic_p6YbGF8L1ORuTgq5GAebwchXJ2J8FLWKDNTBrMzSjcO1_nMj2zsObN5AYXubHTIe4cR1pwCksAgEmoF778LSTNwCMBDyyGnzkMbD7UM4-cWQF55ygq0gjgLXH66Ggnsy8wjX9_mS9Y6XrIcgQ6pJuErwVSGBG9PIiRlm6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=fAflQSZfB_1X5EPMqgUGJtqK7wCeP0bmw6wqnFdVEomI898wGfT31UYoXdTM7G0gZe40TcrkF0KX40xE6tZhOuEKYUCl6UdxIjesGUfPWPxdCF7t1xv0dArfeq85k0tzxnHD5adRIr4fVK8xbao3V6cXIRRZB95Npz_VQ8Dh7dUhic_p6YbGF8L1ORuTgq5GAebwchXJ2J8FLWKDNTBrMzSjcO1_nMj2zsObN5AYXubHTIe4cR1pwCksAgEmoF778LSTNwCMBDyyGnzkMbD7UM4-cWQF55ygq0gjgLXH66Ggnsy8wjX9_mS9Y6XrIcgQ6pJuErwVSGBG9PIiRlm6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
