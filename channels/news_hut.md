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
<img src="https://cdn4.telesco.pe/file/Gu6Hu8AZdNVofx05Txp8WwpBA64Cn9EFg5tLfgP0N0c3ax_GJB-AMqRCTP9z2dE6zHFZ2G967S6hC68ebaLE0Je1AeToMZQunVlXYCpRuEFBNjHxRX1nY_hMyQ3BxpXiOGGoCc16z6kkEBMSFQU0_cfhmN4yb4Udr8xcZkv-Sgu9Qpa-kDN_nXL64CggiqXamFIHkYdWYOzAsE9U4gZ8ppgquGCSsg-VKLoa3UsWaiaM6FM3SZfdKXw-mtDAEA52LODWnwthZxiqho1EjUTeupJxXlqdEXnhE-U2ZeVFxVttKSG8zPvCPLuEwNvGcsiY_b1TM-_8FLURzgyTSH0y6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqaPPRCVQtksZkDyjCQdbkCJ15gKpF5yC7JuQjgCy20Z8hwHPnSpMkBNzfHhzwc0RTb8DPRb1kpy3IZaQ9BfmvHhqjr9QLIJYJv3Y_lRO1pwd22OznSjO021CvnNPg4Xu0TNRzIH22oJAF2PzqJPXtSMCJkNIsXUUdEKgaQYazrEvNhXro97TzpdBL9WEMnfP6EegScJOXJL501FnGY7ZiSyYhtBrcRVeVizcJAcGrU6p7Bh7Tmifkb2vypPb9FZuk2XOsueZTNYD2DzVv1HKPFXns0-MOfqrCZQUiqHes_IE7BGszhn5ogdEYntnqqFzGR82jYwOt5oAxKMKXDVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muHoVZRUBudVyvw88WLl0GGfQEDMM3W-0bbIr6W3h9HBT5tRtUSE16gqMS7tLK0E9uqAvHX561_Z48gpjDwm0wbLRrdOdYZQTRlWy58-aH7F-h--5-NNYRsrVOsnzA_2JlVFh3jxJNZ-vQLrE_Amvl509rEjRkM_Q7W_a4TvJzU3zJPqPdzKkcXVds4UCWWjuCPtSutDMWf200EOHSem4_l8j7y1XF2Xpdxgb0SnB6n9iqKsOVzuV7ViHO07aQqNg6AnORwGVRD7M92eDeUNqMgQURGDr17l94eaIpSyQyb7Wgpk7jaWvv4KFZ0OMexotlRatiz6Ugr4b4WaRzXN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JssHPkVxuAnollLjV1VAcLzXGKWKkL2lZXXF7uDmqjG0oO6dcJUTwYg6VpbYpVIGiAfCG1wbqngC1Hy60trc3unY4ZHIW8CHXMgqHoj3asRDa8bcCoQlHh6trwAsYgEuldF4ldnT9xonEqVlIbfCUGLHlDXnqzPhM0VqwSp5_9tAtOA8w736TJt7uRXW5bHcz8BdG2DNZC9qHqkRMyfwFe7yCTYg1983xm1l7fwSbzEzSdqYVDwjmut4THX3E-dUVQ_uiYeeGxq3VhjJD2CR68mTaRvti06HjceCU6IDi3_0LXiiXizUtQSE-jsoJUKWJs6HSNjJ3vi_fiA0zqHYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-Ye0xTsyem0JczH7hw1FQvsAG_LGJwB8sC0HkKIXAHQnWh0qWM8qskqzm47iLrNSb-x-HTNb1XeJgJEfselW189fYSrKARMCNIwvjSdJ6B3sPmT3AQU7y7WtUB-nbVJ1A4gtdBoYVfpoOWpt4-5CyfmSfVorhfa4_JOlTDvIvtj4FUZ9UeS3PnYrgyLmwBwED-Scdo3vqMNQWJe7SGETig6Jf0me7u0knEYN9xKwHlMtsMIfESfzuKSOPN0TxI7kOyo382qbu1NOG1tcKmAFhfT8aaKsPrqYLTkujdXnaXiOMkmoWXibjaw8gsBngfzxXDDzbxEVWf9PNhg6V0b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jApOcgs5F77Bf7bG5mD-pwJUfTnEHfOU06jm55lhl-oal36ydcS9o0jb9lNm7uuXDuTmZsi7-RKPZas2xrh1ebpGuRGKN2CNf23ivEi_bLx3Cf8tEeGKgJofk9YaaGGiFVkLhvhP44hiYkBM1bbKSh6-NUQZxfm_mYFXH2pPa331jSgvdeWXLSIpBhaRXz1B-0FIcFG94u0Q35BgfIISk0jPx1y2fINc-X4N0opadSyx_9H2RpB-fqKbCAw9NbwJ57tcfTZ98rJntTlhqC469ebBg9wYlWu_e_dPyElLY-HJEyP6XLmpExNNPoZLzrAy3HVMVJVm7oapzxiGEohH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dl-_HK9eR2rLMPKrKgP5Dq1Bqpv8g4xUVz7sTk3aaHvDMzq_flTyGMCqmyYxXUKODeMfjz-5-JVaumjuckzy4HU7tIjyED75U2lRBmR1rvgJVIkYAz56ZD5BPF8vyS1lWC-k4hMnNyjk_OgC1O3qm4iJmvHjhbJSU5WMCh8D142QU5XtBTm5Hv7u6hhrBoI8WkkBxu2c1MP0Ii8WZBI38vDfjpkTu_Wbyp4UOPHujsqPH7Jrp9ci83tDmHFHmMrZ8Jt9WhQ6LOhdcVfdvyTIE3vzFZISpZOssz5ZpGCEpqFRScoEvWpEGMTZuar5LxuMeXCcUcnhrCBzDCGNiob0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISZVKAc1Jjeqp6SmYE5IcBQ0AnLG1dgnUOBJmpJKD-TnOYAcxzwk0qRhsTF1X2tTgUfHAyfG4TkrdDCeD6MmprTm5Hzk940uijLzFCQi7U62sUKXwESj_vAMURsGUW5I_oLUi_7KLaIDS-1JJleRnT-SQ1JtbH65W1MqNYh7VCpKLaTC0bdhHs0siyA_SD-gjtfi3hk3fYrqDp4FiufyJaOcwQvwoMpVVz0VMdJq9QqDyO-GHEg11LQs-LPcMvpf-st_F3XOfdSd42dAiJ1oF6w2IpLmmpm75XF6CU1g8FfellOLaZmssda5_0TcIwBk7kYAOkQwFcNSD3mcoZJUqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=rW7i--O30wOSQFPMHYlApbc6meY7XNHqAQjbsUVRThHwOPq1dKWb9QDvdNFN8Pq1G1nnuJCy4nyVjx7Yus9jLdXYNjHh2vaM7u_42l2jF6PBjHLw-4ZtN2Njn4GfXdnNYC8G_ciHrARtADVAebJMs58RTyQRmPMLWuZSPSh9c87o07xm8nQ1xONQq5i1cFNVWCGRum0-hvtMZJSWDpZ0bvBgL8y4bUwNqqCxvm0Skh6O9wTi2Xd7zcqjbwPt1D9WMpEO3-t7DmucXj3VIeZ0UCirGWrzyDLNzxIEm7nvXBNmFXZtczSlt__ihBTmKDl_hrk7TeX8fWq8IErYOgHHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=rW7i--O30wOSQFPMHYlApbc6meY7XNHqAQjbsUVRThHwOPq1dKWb9QDvdNFN8Pq1G1nnuJCy4nyVjx7Yus9jLdXYNjHh2vaM7u_42l2jF6PBjHLw-4ZtN2Njn4GfXdnNYC8G_ciHrARtADVAebJMs58RTyQRmPMLWuZSPSh9c87o07xm8nQ1xONQq5i1cFNVWCGRum0-hvtMZJSWDpZ0bvBgL8y4bUwNqqCxvm0Skh6O9wTi2Xd7zcqjbwPt1D9WMpEO3-t7DmucXj3VIeZ0UCirGWrzyDLNzxIEm7nvXBNmFXZtczSlt__ihBTmKDl_hrk7TeX8fWq8IErYOgHHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=mgML7miN9GNGXssr5dO03DuEiwnMQGaX5n6Vg-kK1s92qnCWMNls-8cgA8vDpzUACiEl5292vQpxuWTe9oBCEgjfzpzz5FYXSNsXY-h9h-NhXDv2ITX359FE3RazesaVRTuBjcPD4WAmOivChJnt_E4sEiyKrLS6GF97teTUPL7_7uAK7NchvpsgZYgRXxNOUgWKaYN-zneoHTSqvV4l_n01vDvSIhyag4vngC4CZ6bcwFoP1irDUt4fFdDTHaNKWudkNeMnwLKMb4OrnHG910eYRlKzO0g4K6Bz4qATfAgulaTHciU9_NBESvcP90HAlLPlLH8HKkDw0fuW0v92aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=mgML7miN9GNGXssr5dO03DuEiwnMQGaX5n6Vg-kK1s92qnCWMNls-8cgA8vDpzUACiEl5292vQpxuWTe9oBCEgjfzpzz5FYXSNsXY-h9h-NhXDv2ITX359FE3RazesaVRTuBjcPD4WAmOivChJnt_E4sEiyKrLS6GF97teTUPL7_7uAK7NchvpsgZYgRXxNOUgWKaYN-zneoHTSqvV4l_n01vDvSIhyag4vngC4CZ6bcwFoP1irDUt4fFdDTHaNKWudkNeMnwLKMb4OrnHG910eYRlKzO0g4K6Bz4qATfAgulaTHciU9_NBESvcP90HAlLPlLH8HKkDw0fuW0v92aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhHt44KzSIpdvltLOfn0tp1otk3DRgYapxP2BiO4Z77mymxYd_5mxL4lkxRhOEeSLpwzAVbG0IFfVsOzzRBmOwlNUMwM7YlO6w0rjb2q2Vcs2qywg73IWv5St-IK7mqG_Pb4qY6yH9U1fCrqFmSxGlXaoroARCCYcuk8eiy_H96jdpYaY0WUzlHL6ujLX5F5z_Gf-fOV8VnkBRMogzr23V_mV228PKwf1bHp7Pn5EMQfbtDwOS6Ihh-vX8JnV-4E1a2tj77RwCcdjZchvn-bfZXrkbY6fndjpb-RFn0pdqdxO4HXCbniNuAeQR_Iq_9WTyTVG2TkPKboExmZMwAhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r17Kqm6vYEHx43R6WXon7Vm3p5QAm5osoyeD0O6WTEkn9I2X3g9ZSrk1lnzRuro4BHXr3uY_HizA4Tie8wva9UdruT5t0Wl7fSPefbR-lcELIpkEohhvjaKjw4xs1dEMslilRdmVt5hhDvRbh0wldYS1SRAmOmnT81hCYQY4B7ToP77_44x-IAMLfaPBn2wezz5ZZiyFhTOao0HDqVRRVWYIO6IxIYEKIh4NcCBmA9xI-xx8yc_EQ-1CK5NTQngw2WJUKpuhkuLZiMg8E7p6Hh7djgKhaNMTFJycAmKuvWML9MX0wOWCvAdH_2BVE1H0fiXEbciaWxb9weLITSYJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLlEXUYjiMoybAJ9kVcPM6ERHkPR9NyX0jxRoabFJX_ZCWBHFu7IaecVtcaFsEfVRZz_4J3WFgk61YQAe4d2Y5c0iQnYfC3ucRywzGWVo2Tp7u552Wb29vB59Enl8nC6gJU7bEF-EgBfnly5cj4tn0VGN_uNV7Y9fKZ9RzFfsPB4RteBI4MpPaK21-ZGspzcEjdBBBpSWsY4KnirWM82odDrNN7q-YgsZJlVTCVchEp34j27zrWuk7dLaX6Wiw4Jr0FOLZFYRjDhz91CSgkwEwVwcoiID7YpS4J0A_DFIP1vMkhfUt4xjk-fVNYMn_uCc3EpQmqWUipkreS4xdyf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGCq-z4RZJ5MDFQ6SyZkhj4ZfD2xfLTpCrDKFAr7vt6Vy_3BWzkY0MWMXD_A_lZbseFVMz9PmTAWYkqNR9LJUV63_aWV7R8b49lMhMBf4ISbdEyAVwOjoJIj0uHe2OHivSdPCC_YMuD4_YVIq_NdBPjzoXCNLldHtc9k-iZ4fxIlCoA1KNykoU4AccObMV-oVJHQDiM9vnSwBOhuGUNXEnExXDQvRFPdL1kKsmL5idelbgF61eQmxCaMv7f9BFmDamNjQbbWmhk3yg2UNRD2Vv7z_LmQgZuUBLrZyj6Ma26gl8eztLDSX9B7eWJ7iCCTdnDyGGSobsBEdv1sleKe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyIWpY1DmszBbyEVx_0kq1V7lcoNrnzq76IS0BS-m-NF16LImliu562zDm6cCfFbPkH6LjXUva4A2IbstpvbqtHWn-PGPgJ0hzRh3xG7-wdXgtGHXwlmbbnw8oBPzM7u2v5MX8nJHMNq-_l66S2n8VxvNcC7EFhy-ByoYL4vMYQqIXKzO26NsmkjuacGQctcTMHOJw0y_ugY27eQGcdeeu59IzSL9xu60kwrh46Z0Q4tr2TdmrcKxpEN2Oi6UMnGWeAn-cwW6ThQFT9_oSJoy0zpnvi9LPnABtuoblPNjoSU_UnTd6gy5egYHqKfh_rgXv_X2MSGskZoeFxMtwPADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au5n3w2ZZ3Yb1ce-03ox6JhGoC_D7ItBNqmU2GkMDg7WZJvVBoAkxoTFQd_DHbFo3UmDD1Tny-XG1itezhkld5qJkG_uEXxvweGtQGxAkkmTQEPwL1w2xxFUC3WKrFinW-Ddp-P057oqgU43PcCXy99QYZ86V-0eRZnrLK70UYPlozPq-6JRIPYPbbP2PRWzxhnkHpp_TWJXRcUUwkrKvGPRRb1nBCpu18bf0vrzsbAfS-6A8JCiThFQWIPpBRbkyR7wjijSzBriAkUV7QwneKV_jryzqBfmFerNjkfqvaGrGQXIsCGQtCjkzEVTo22JZZ4CBDG-staVepdNXbobyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu7oRBKaNHkYJzktiFPwTKAoeyAPuQXtIpzFp9S7Akm6sYZ0c8DIzUsiWSJMg7iCvBOdFr_Iw7rKcx8sJl-C-tmnus4KDCIRzXkJA99_6TBdBohwznquEk6C-ULEoh367mOrB0Sq6atFa_tlhv3b7KqaVfwvEpSvzIDRV8HtzylHWTaJPLQ_ZMqn8rmBx6JcvLPn5qZ-zzMePIVcM6ahbS7dM_84KNxnySSeGK8rep5JjxmYzaD5t0zTdd1r3SBoMfdf093qcOyEqVqg5qsb8EPq9BMgyexSu4EqnV-M8jXgXkxacHetkxDFPHfsfJan-vYZZUZqfFPOYdRDmIPC2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=RdNM2Yzh0O_bNTTmL2jW62npKDinnht5Z7r0qyOquFadJJd2GIKUulWh2s9lIMOQmMu-1n9tWFjQUogywjGYdNFDi-YzsAl6BR7Rrp6jhhtU68rRW9yAP7VwxnIfHsFWBZXHmfazJ9-z8xu8O7Ml8B8_KL7GUAV3_6jEwqZyQctUoTfkHOUksjTz50eu5wb3hbOrpRlJ6iuirmJXA0fmT8GcfT13N7OwVMA6wHbASIA0019ItRq_-lobVMuXzuIeiAm3rtFJZnNhiEXi3mEh9Nh1geLRQMRXGnBK207z23QBDtGvletqkK4zqdzZXMotTbP3ew9aRkGIARnOhTjrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=RdNM2Yzh0O_bNTTmL2jW62npKDinnht5Z7r0qyOquFadJJd2GIKUulWh2s9lIMOQmMu-1n9tWFjQUogywjGYdNFDi-YzsAl6BR7Rrp6jhhtU68rRW9yAP7VwxnIfHsFWBZXHmfazJ9-z8xu8O7Ml8B8_KL7GUAV3_6jEwqZyQctUoTfkHOUksjTz50eu5wb3hbOrpRlJ6iuirmJXA0fmT8GcfT13N7OwVMA6wHbASIA0019ItRq_-lobVMuXzuIeiAm3rtFJZnNhiEXi3mEh9Nh1geLRQMRXGnBK207z23QBDtGvletqkK4zqdzZXMotTbP3ew9aRkGIARnOhTjrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=lIY2eqMmTONkam5jBrKlkghOKFOXAHnVFZuu_okh4ULbe3L2kQpXMGXj3CHwo1t7vUHLcQWrKzRH-QdA0EDh-9Xp7E5nEexoc1RizesIui1MmgvlXC2PdYoY9Aoy6qJrcnr4ptJ51drVL_1H6Fn5AIhyuhHbbKa02Qxtcp3Mx8Tvbv0UAdUFE2UWiYRIJlbtuPLaG-oUCm9dhUo6oSVdlZoe0fjgYt3rc3YP2dK1P6dvsDrIZCd-8EipfyRodOYQRqAaXFoLadC-UPVjDCAszSwPuxFitdpGjE2g-p2_WcS0FgXhFcR7KbRbKez_PBvrzQRNmfONq6aa8j-Lo-ppPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=lIY2eqMmTONkam5jBrKlkghOKFOXAHnVFZuu_okh4ULbe3L2kQpXMGXj3CHwo1t7vUHLcQWrKzRH-QdA0EDh-9Xp7E5nEexoc1RizesIui1MmgvlXC2PdYoY9Aoy6qJrcnr4ptJ51drVL_1H6Fn5AIhyuhHbbKa02Qxtcp3Mx8Tvbv0UAdUFE2UWiYRIJlbtuPLaG-oUCm9dhUo6oSVdlZoe0fjgYt3rc3YP2dK1P6dvsDrIZCd-8EipfyRodOYQRqAaXFoLadC-UPVjDCAszSwPuxFitdpGjE2g-p2_WcS0FgXhFcR7KbRbKez_PBvrzQRNmfONq6aa8j-Lo-ppPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=dedXlAbfbokbgbQ1z29JtTL2qu8RUzvubtBf2ur8D6-FiHrmZ9bkc-nbdZ0extWg2Ix4wT545jJRGrFq-k2IR5cEoTfyzAFB9YsSTF4pOtKvHdKPndU0yrGKeHxoc9zWqHBnmixaYHmoiSDs9TOSRYYBYi8KpxD0Z9X076kMA5br5uM5X28VkR8ScG_t17MFzNYVfvDl0aebNZOJBnxgk9L6W_iPEQReUW2kCLJzolj0v480ycrLNxzVoQhO3Lc2gEiqdorm1147tOic7dhyr9pmWYo1RC9yp5AMQwKeNoCQfb73NW2kJWR3wAJRaOfojpl-urWrX8rb6v5mS9O82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=dedXlAbfbokbgbQ1z29JtTL2qu8RUzvubtBf2ur8D6-FiHrmZ9bkc-nbdZ0extWg2Ix4wT545jJRGrFq-k2IR5cEoTfyzAFB9YsSTF4pOtKvHdKPndU0yrGKeHxoc9zWqHBnmixaYHmoiSDs9TOSRYYBYi8KpxD0Z9X076kMA5br5uM5X28VkR8ScG_t17MFzNYVfvDl0aebNZOJBnxgk9L6W_iPEQReUW2kCLJzolj0v480ycrLNxzVoQhO3Lc2gEiqdorm1147tOic7dhyr9pmWYo1RC9yp5AMQwKeNoCQfb73NW2kJWR3wAJRaOfojpl-urWrX8rb6v5mS9O82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T04fi0C-Z9g_XG2naOyFIL_CF4mfPah6wHMKI6MbopEkMXR26oVOqfpT-3EZXpVx7bR4uTthSWMo0VkFrpyVYm_SC9e1pvF1N5m17cprSBGDkoFuo_4XHAWbstfvnnAQ5-DiSuw5HPYyWCAf8xpBvdqClO8eSjB3NhLJIDV144FiXGDK3KWh4z-KslVJe_MLVU6w3-Du7pKdauWq3jqPE1cwSYi8zA5ulLI5BmIWHYnnZd9Xdz1yf0KO7r9rCspjZTpzTLnpcdIQ27YeQ3-xIspEYhymBnAe7c7TLOnW1k0xX5tZPSOja1Bk5u4Dlavojm2y20g3WtJbEjmwq4VaOUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T04fi0C-Z9g_XG2naOyFIL_CF4mfPah6wHMKI6MbopEkMXR26oVOqfpT-3EZXpVx7bR4uTthSWMo0VkFrpyVYm_SC9e1pvF1N5m17cprSBGDkoFuo_4XHAWbstfvnnAQ5-DiSuw5HPYyWCAf8xpBvdqClO8eSjB3NhLJIDV144FiXGDK3KWh4z-KslVJe_MLVU6w3-Du7pKdauWq3jqPE1cwSYi8zA5ulLI5BmIWHYnnZd9Xdz1yf0KO7r9rCspjZTpzTLnpcdIQ27YeQ3-xIspEYhymBnAe7c7TLOnW1k0xX5tZPSOja1Bk5u4Dlavojm2y20g3WtJbEjmwq4VaOUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=eENacOPVEQ57GBUe0kax5Kc_nc_oKbFTy4ylD85JlflbA59BE9JeZ91CWgvZYv5DgMhYmwLQLhqMvDbQsxprCc93OW-FhngrfKOA1X2ef7_UJMb6EbvRgNpo-fOlet_bTDOoxOsKusSLPz3iYUP6ZOVAth6YUE4GbVrgedo7gulVngqrhSdzu3oDSSLxRj-yGdEWcWAd8P8b6vswJvIpV26LICD6FmpxRoVG7o66EqZ570Q_frDFcpgg0fPIF3CRzlVQch_uMvtYbQnyNZe3AAa45-D0n3QNCuVW9tSBtSY7zmh3uitGzYMv_wvNrIF08igkWre50gvrexhE7mywbz528nIrMvMqCLWzQiqaVqNfGZ8lIhJGeoBFJ4hZdtDe5IwCWcp8c1jJt170iiGVVAJ-zb8nZjs6AVTP8C78YcnmuYgj5IWHhZrAUpHTPTPYiyRiEjaHwzQwD89OYQGYdZ9QvELmwhVGVSmwgjZe8F9ZFJMaq36c2WvDU7i6lmGYANLBBAdYq2hdBvKwyolhqou52V_Dez_sKB-Rq6OdClWsHyTgqYByYMnLxbS8G7YoXExxT81yL2aZgqvujBvmC-RzK1-cIc4BQWLOqz_VNeIQurNRG60gtafLczjTTxgbcr0cLVQJC7WzOzRclsNEshdiWGyLrH_4Z5Yb7ZGDars" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=eENacOPVEQ57GBUe0kax5Kc_nc_oKbFTy4ylD85JlflbA59BE9JeZ91CWgvZYv5DgMhYmwLQLhqMvDbQsxprCc93OW-FhngrfKOA1X2ef7_UJMb6EbvRgNpo-fOlet_bTDOoxOsKusSLPz3iYUP6ZOVAth6YUE4GbVrgedo7gulVngqrhSdzu3oDSSLxRj-yGdEWcWAd8P8b6vswJvIpV26LICD6FmpxRoVG7o66EqZ570Q_frDFcpgg0fPIF3CRzlVQch_uMvtYbQnyNZe3AAa45-D0n3QNCuVW9tSBtSY7zmh3uitGzYMv_wvNrIF08igkWre50gvrexhE7mywbz528nIrMvMqCLWzQiqaVqNfGZ8lIhJGeoBFJ4hZdtDe5IwCWcp8c1jJt170iiGVVAJ-zb8nZjs6AVTP8C78YcnmuYgj5IWHhZrAUpHTPTPYiyRiEjaHwzQwD89OYQGYdZ9QvELmwhVGVSmwgjZe8F9ZFJMaq36c2WvDU7i6lmGYANLBBAdYq2hdBvKwyolhqou52V_Dez_sKB-Rq6OdClWsHyTgqYByYMnLxbS8G7YoXExxT81yL2aZgqvujBvmC-RzK1-cIc4BQWLOqz_VNeIQurNRG60gtafLczjTTxgbcr0cLVQJC7WzOzRclsNEshdiWGyLrH_4Z5Yb7ZGDars" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=VIEgr3eoRPZ6xKk9AXMtqT05uiGaC9TMIvmaXXJQQpKtZdAFlQTA8V5-VXZuLotM4QjEYFoH1RBM8p5tUJLJ66X4AgfMpPFIHjaYlqEtk7SrWQukMz3YOUNUHETM3kfee2NGDsrkSrmdZigml4vCvzh746regGsOwokxxpf7rhJfi3VHGOMzg-LaBIy5N00LLymWrhmB-RcTxEeBmOd_7pqZCGzW8WyCWHfsDMD9osfF8UkTpd15SgW0GXEoKRYQn1Q8Wvi0ESZwdJvB_x8aC2aKG3Wl2lU8J9kkAKYLERrW21AIiGAZE90TFdBxlzP_yEz81cZ2LcPQV3W6irnZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=VIEgr3eoRPZ6xKk9AXMtqT05uiGaC9TMIvmaXXJQQpKtZdAFlQTA8V5-VXZuLotM4QjEYFoH1RBM8p5tUJLJ66X4AgfMpPFIHjaYlqEtk7SrWQukMz3YOUNUHETM3kfee2NGDsrkSrmdZigml4vCvzh746regGsOwokxxpf7rhJfi3VHGOMzg-LaBIy5N00LLymWrhmB-RcTxEeBmOd_7pqZCGzW8WyCWHfsDMD9osfF8UkTpd15SgW0GXEoKRYQn1Q8Wvi0ESZwdJvB_x8aC2aKG3Wl2lU8J9kkAKYLERrW21AIiGAZE90TFdBxlzP_yEz81cZ2LcPQV3W6irnZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=Al14lrq7i3DHn6pmONQXknuznyB_blUOviT_bl_FMXLZyz3P95WgINDNH6_zW-0YZdMKU3Y52xvypqAlAl3jTY1cJgczaiHiwG6yO6bC5PT-W-e4TS24BZr7YctRoIBi6otaniinrnqktrdnyV0_BVLH7biAJEyt-hSCndnv_ea0QuRNewrsZD9YCfGbODRFQUbHtuIfKsff3e-5CCMn7VlQNFlk5k53-xUXMEdPprSiuT0Y49wFMgs-tw_QMRcV-cIlLcryJR7FZcrPm6SKYy9EGrxjV4L9EsldeSwaZcxQ4qz8hYqNUxd3_AQLu1HGMz4GRc76OuXWesDJDzfqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=Al14lrq7i3DHn6pmONQXknuznyB_blUOviT_bl_FMXLZyz3P95WgINDNH6_zW-0YZdMKU3Y52xvypqAlAl3jTY1cJgczaiHiwG6yO6bC5PT-W-e4TS24BZr7YctRoIBi6otaniinrnqktrdnyV0_BVLH7biAJEyt-hSCndnv_ea0QuRNewrsZD9YCfGbODRFQUbHtuIfKsff3e-5CCMn7VlQNFlk5k53-xUXMEdPprSiuT0Y49wFMgs-tw_QMRcV-cIlLcryJR7FZcrPm6SKYy9EGrxjV4L9EsldeSwaZcxQ4qz8hYqNUxd3_AQLu1HGMz4GRc76OuXWesDJDzfqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=avKll6IZca4nPI_bmwlOjjby5dBcsfZz4ne2CxtnisaH10Cnpw4hehwbAObD8304FeZvYB8hVPmbApIRPlyHF771G14nLOpNrhVBJ1AlX29VE57TkeKFgLpJPXxsrGTsaI9wCVi0n6AuvydwwYShudDg2IKBH58oA5fV1hX9_ZZnCUSpkQPmwm9ZSZN7Opbx8Bu6SKmcdcPhgBnZwLJgBlVPvjNZ-uSJIuuWMsmvgTKC5t1le5svqENnJP2V9yJu25gN84LA82NnnCQLLbpAm1ZtXWQa5q5TI52UF8cwnuDT0wuYr2AjJKQSIF-0vaLdUYk7TqP_fOT55qtiOrTbk0eZ1ct7Afq6ewTwQtHw3BcBMR6ZK4veW9FunzMrKcouPoZaHPMT1fRL49m0OoUyCR96Kibw1Ii_UtLlNAQYMNeLSDbmv7TW8nlb7OplX2pnB_BR2ck19oK4wOzQILKMAs3-GRxZDcFL5_Dsj1ulLaoRxZYicrCSSwVgbQQVXbU-YCHbuUQ9tdFaalSuvPhTlOl45YSQXdhPNLv_tIOknYmFl0AADRrK7k5iaUEWn8MWU7c3ftQ8GU4P36DLecj6KB8b1yrOejb9poqGJ-36mQE0EvIa_OiDu4baFpv1e2Zdk5gqh1FsFKRM_V-w2vqLy5cPoP_Jj0uGYvRAPMfYAug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=avKll6IZca4nPI_bmwlOjjby5dBcsfZz4ne2CxtnisaH10Cnpw4hehwbAObD8304FeZvYB8hVPmbApIRPlyHF771G14nLOpNrhVBJ1AlX29VE57TkeKFgLpJPXxsrGTsaI9wCVi0n6AuvydwwYShudDg2IKBH58oA5fV1hX9_ZZnCUSpkQPmwm9ZSZN7Opbx8Bu6SKmcdcPhgBnZwLJgBlVPvjNZ-uSJIuuWMsmvgTKC5t1le5svqENnJP2V9yJu25gN84LA82NnnCQLLbpAm1ZtXWQa5q5TI52UF8cwnuDT0wuYr2AjJKQSIF-0vaLdUYk7TqP_fOT55qtiOrTbk0eZ1ct7Afq6ewTwQtHw3BcBMR6ZK4veW9FunzMrKcouPoZaHPMT1fRL49m0OoUyCR96Kibw1Ii_UtLlNAQYMNeLSDbmv7TW8nlb7OplX2pnB_BR2ck19oK4wOzQILKMAs3-GRxZDcFL5_Dsj1ulLaoRxZYicrCSSwVgbQQVXbU-YCHbuUQ9tdFaalSuvPhTlOl45YSQXdhPNLv_tIOknYmFl0AADRrK7k5iaUEWn8MWU7c3ftQ8GU4P36DLecj6KB8b1yrOejb9poqGJ-36mQE0EvIa_OiDu4baFpv1e2Zdk5gqh1FsFKRM_V-w2vqLy5cPoP_Jj0uGYvRAPMfYAug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=FUXk0KzYl7e2C0PuHfoBrK_qVnz5CRtFEUCOgmsvIezqRg3NRsfOChsOnScSbigmakuFHQcg62y0pMlZv2889-gZMkqHLpBhth1NtAafajA0ttIGSt9Emqp8zV42JR1df7726RoLeF5NVRfc_rrTBc1yGSYGg7HH-DLi7q8FcdQTiO_zZl7b8JxGoUyPRmDZShztJcbLFqV-sR1ncfzgu-aKjXTvRdRkiAQBk4OjYPTQZwyZvp62jjPQaSIet8Zf9DkmU_p6MknAqHWlC07PdTq2DIwCsEmfj2arabUraOPJsv4vsuXFcQfkMB0xuRg_gFARrSQYv1teMxurWv16wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=FUXk0KzYl7e2C0PuHfoBrK_qVnz5CRtFEUCOgmsvIezqRg3NRsfOChsOnScSbigmakuFHQcg62y0pMlZv2889-gZMkqHLpBhth1NtAafajA0ttIGSt9Emqp8zV42JR1df7726RoLeF5NVRfc_rrTBc1yGSYGg7HH-DLi7q8FcdQTiO_zZl7b8JxGoUyPRmDZShztJcbLFqV-sR1ncfzgu-aKjXTvRdRkiAQBk4OjYPTQZwyZvp62jjPQaSIet8Zf9DkmU_p6MknAqHWlC07PdTq2DIwCsEmfj2arabUraOPJsv4vsuXFcQfkMB0xuRg_gFARrSQYv1teMxurWv16wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=pmTCzO6SDjBUvil4JAY1uXi6fGj6tRE2MC-j3VowviLK6F-5wPqgSUeLCLp8KG9I1yKWJ8zZrDdQDuDRkNwbUcH2fp-Ho9qg4qIqGbolWjda9rDzzWtoArdPaIWOepLIoKL-1RwshzhgFCWqEImj3nhDjo_Zn82sSJQjHckrfgI6NS_nBHeVI7Ne-yOfgsK0ltne4lYcK2O5_11HnV6_yREGJFMXTrsTBRA_Z_QxFM5W3KsYXHv0E5XCfTj2flSHIwPUrDl5DB7dAzViisIyNLfVcgRlC4cE8qr30CinEriZON-rnk_WCBGhh-aZi5B0h4U5mDAGNOVl3gN7fKvcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=pmTCzO6SDjBUvil4JAY1uXi6fGj6tRE2MC-j3VowviLK6F-5wPqgSUeLCLp8KG9I1yKWJ8zZrDdQDuDRkNwbUcH2fp-Ho9qg4qIqGbolWjda9rDzzWtoArdPaIWOepLIoKL-1RwshzhgFCWqEImj3nhDjo_Zn82sSJQjHckrfgI6NS_nBHeVI7Ne-yOfgsK0ltne4lYcK2O5_11HnV6_yREGJFMXTrsTBRA_Z_QxFM5W3KsYXHv0E5XCfTj2flSHIwPUrDl5DB7dAzViisIyNLfVcgRlC4cE8qr30CinEriZON-rnk_WCBGhh-aZi5B0h4U5mDAGNOVl3gN7fKvcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHjh0DLKQZlNqZgnfIIQjQdusQs3PThSVjWnMey7alExw43yFRwtL6lSGrtrsz37vbBC3jaFXlmU2EResNmRLeqQrnpbKurx5ETuVOi9kNjgbuSqj_5-_Xe1ZLDG0rBt_57HuVt5pqI6R0ChluDU3LnmNCuN-v76JULyEPQStwMvg6R0YZYw-NuY07yUhZWwNU0WxvNbh-rH1p80JxiLxU4qvWWoUkZIcq2qanVB61hpGtrNs9hbDwFiAAq7Nwn5gVFlKthqbzdD4gQdPr7g-7wPrr-_gMaW_RPzuo4mcWRtwpyjkuL_tCsf3AemH2EtVJvW3nZ8vO0XGa7ctcSr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cePbGij2Xv0pZ5ADQdDt3eqZiJTpdWd7hk3Bh31OP2Z3FgNmZvsjsnDpbOZ-ULxZ4Wdqr8j76uqLZMwhUiKOcIiE6ZyigXiZdS7I1UeEMZb7bl8z802_Pm_S98l6WTflLg9_zv2ywk7sXingUfym1aqeM9SD5RHX2VZwmeIScib3u7ZbjjB_-6b-fE24mx-NoEquOUHVfN_gwwfc3wxjeO1xQsPCS1cedYjZLQCMDA0SRlG3yf0VLcrsvtdsfdm3-mQToEg453gU6gB2f-wsyHEYyM3aMpGAiq6Sbz29UNRYnZLjUamD_A0Qr2NZwtSH_a_cqfl3QWt8xZ1QZAPOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=b44rRF7tVql6bGHNAArGlwWPETKPad2tM0vKRJdWQLcye9qFzfb8Oth8PsblaRFX8VWDJL6d6q5uQ5N-EcyDVsXeyg4gVj-T81k6S_0CeIFBP4dnw1MFEneHflMum9x8VgIzfEQ6vXXhAj1llh2Ymk6vXAoxoMj44Rx7KdwAF2BqI6S5yn9CkGjiCCrsM_e-sk5ADuwBJs76wewz6PD10iDXCQN596ltGTJc6dODjVviK4IG8wrkVq2aGXxDbL3VMuSLVG3G_gUxCbZClyQxtsIPIakQNdhObbIMeUobMfs3KvSToqLMLG0zixqlG32TANzLr4A0ulF9-aNyjHwoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=b44rRF7tVql6bGHNAArGlwWPETKPad2tM0vKRJdWQLcye9qFzfb8Oth8PsblaRFX8VWDJL6d6q5uQ5N-EcyDVsXeyg4gVj-T81k6S_0CeIFBP4dnw1MFEneHflMum9x8VgIzfEQ6vXXhAj1llh2Ymk6vXAoxoMj44Rx7KdwAF2BqI6S5yn9CkGjiCCrsM_e-sk5ADuwBJs76wewz6PD10iDXCQN596ltGTJc6dODjVviK4IG8wrkVq2aGXxDbL3VMuSLVG3G_gUxCbZClyQxtsIPIakQNdhObbIMeUobMfs3KvSToqLMLG0zixqlG32TANzLr4A0ulF9-aNyjHwoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=v6yk_0pS8iwgaMGALk8ywdASvdj6DTe5ZaBmKANrr4BVgN1by7JylsjfrzxQbHUuVKrOZ8IxTR09xDMtIGPNSGk8fARPApGhtPkoCBYnI6FFiwxuBW7y0MvsMAaySdwq-MHnKukFx6myVtPvMtcPrqMPLHqlghS9SUbh4bD0-xoTJOrjmf3v1dhkmjT-C9kqVX7kdwU8EgHN8bCc3J5TqU_yEq5nrl3CWmn00zwsEtaKBOrKl1OCyX06bJ10A9wof_h_ZXGUyb6pUfSd6YSWuOf6m53N7F3XEllMeXswqRlhF6Rdktqbo-mzum8alTsnhOB9lSlGwz-VTNrbwPgLGAqxY75x6B0rBnMFawEJIJWiWUEZP9A9_CloanzE-z2O-ihAHv12kC6DiGtEOFBG0YgHoswECThnwLJEeSywFYbwU1gHI3yAlhuWh3hF2whjaSjU6mp6kvqp50mcibaAsAE-4TJ1FS1VAJUMr2XNIYCwj9yoE4EDQ7SwyszH8wZvftw6okNQaDdhG8JVZXCZqSmD3JCqNe7Q-RZ4rapkbHWSW4HFVfPCwu3LCJXIJ4777nX3vFaFADvXphAxsq0Xu_HEz_eTsfD1-eF5qKJrYXt9WDPt4gaNNljqq1dKkd95VKZvLdXfC5xRPZuj0voTy3u5MEkOMMxFybfwNHsd8Ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=v6yk_0pS8iwgaMGALk8ywdASvdj6DTe5ZaBmKANrr4BVgN1by7JylsjfrzxQbHUuVKrOZ8IxTR09xDMtIGPNSGk8fARPApGhtPkoCBYnI6FFiwxuBW7y0MvsMAaySdwq-MHnKukFx6myVtPvMtcPrqMPLHqlghS9SUbh4bD0-xoTJOrjmf3v1dhkmjT-C9kqVX7kdwU8EgHN8bCc3J5TqU_yEq5nrl3CWmn00zwsEtaKBOrKl1OCyX06bJ10A9wof_h_ZXGUyb6pUfSd6YSWuOf6m53N7F3XEllMeXswqRlhF6Rdktqbo-mzum8alTsnhOB9lSlGwz-VTNrbwPgLGAqxY75x6B0rBnMFawEJIJWiWUEZP9A9_CloanzE-z2O-ihAHv12kC6DiGtEOFBG0YgHoswECThnwLJEeSywFYbwU1gHI3yAlhuWh3hF2whjaSjU6mp6kvqp50mcibaAsAE-4TJ1FS1VAJUMr2XNIYCwj9yoE4EDQ7SwyszH8wZvftw6okNQaDdhG8JVZXCZqSmD3JCqNe7Q-RZ4rapkbHWSW4HFVfPCwu3LCJXIJ4777nX3vFaFADvXphAxsq0Xu_HEz_eTsfD1-eF5qKJrYXt9WDPt4gaNNljqq1dKkd95VKZvLdXfC5xRPZuj0voTy3u5MEkOMMxFybfwNHsd8Ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=eWuRwRXIYiXX_kVumofGG3PxIVB8R8XoaIFVTyMYJd7QWP16g76QN6icjkBKLQ8UociCUWk-XDdHKcGV7OdeFyQWNLGR2DE3ePHia37F69QrB4g9X6oyROxIoCcwu3yNt3r6ZKgRix5aCu-4ZojJ5WvSOzvplrYy_9J-MJqjwYbPEpnQJ_xDzt_byTnWHFgsyAZ1ivU-OFCvRk3exsZcp_udOnHRrj51f6IobZWLuokUJ5vFw_UN5Rxa980wYBFtHwlHhTV9xdg3BBZ6nBA84Xc84tGAQ6p-eRBMEW4drRPHTFY3PxUyiYFow6yNoes2V8cBeNVUrXpBc4rTVW_now" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=eWuRwRXIYiXX_kVumofGG3PxIVB8R8XoaIFVTyMYJd7QWP16g76QN6icjkBKLQ8UociCUWk-XDdHKcGV7OdeFyQWNLGR2DE3ePHia37F69QrB4g9X6oyROxIoCcwu3yNt3r6ZKgRix5aCu-4ZojJ5WvSOzvplrYy_9J-MJqjwYbPEpnQJ_xDzt_byTnWHFgsyAZ1ivU-OFCvRk3exsZcp_udOnHRrj51f6IobZWLuokUJ5vFw_UN5Rxa980wYBFtHwlHhTV9xdg3BBZ6nBA84Xc84tGAQ6p-eRBMEW4drRPHTFY3PxUyiYFow6yNoes2V8cBeNVUrXpBc4rTVW_now" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=M_ZjuL-8-XTWzxMsvock-o16Dkd1pZvG1agpAej4S_tDmh1eXydu1SgnRfDq3R4hdnKQwxbjZPuVi1BkXGeElDqeYs_3Spw99Rt1L-aUZCjBi-f6CzvcQX8J1AsgzCfHIQJeDJRgB07jXfF4W2iLns-xdBBmA94uyQTJhV3aP2ICHgDXHloywUZaAWfOgmqPStr3AgS3mkkaVGHmkKTFgbZ8L6OFpWQP8dinJp_d-HM7FiNjs7vkn-oRQNSPq3jcy9WbhEPkNH0zJCbkqRs4uSsGjZBWDSyCqOH2o_Df9O2Eupk8pyhaGN_ij5-IV5llgmjLehvto3zhvbdy98FVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=M_ZjuL-8-XTWzxMsvock-o16Dkd1pZvG1agpAej4S_tDmh1eXydu1SgnRfDq3R4hdnKQwxbjZPuVi1BkXGeElDqeYs_3Spw99Rt1L-aUZCjBi-f6CzvcQX8J1AsgzCfHIQJeDJRgB07jXfF4W2iLns-xdBBmA94uyQTJhV3aP2ICHgDXHloywUZaAWfOgmqPStr3AgS3mkkaVGHmkKTFgbZ8L6OFpWQP8dinJp_d-HM7FiNjs7vkn-oRQNSPq3jcy9WbhEPkNH0zJCbkqRs4uSsGjZBWDSyCqOH2o_Df9O2Eupk8pyhaGN_ij5-IV5llgmjLehvto3zhvbdy98FVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=ibPJ3XhwJXZhacQHMJFyVmX8HKAOaJX0eowK6q1_qkAUWzNev1qe9H6cE-AvyauP6KqC1BwaG1LYXy68lllfoY5xC0t97eEvNzuiSmfowNS4KFDUBKifCR7RTeZO9_g7I7RRM4oqvBNaU7Ap0vNFrehsVUlRlH3jpN12tBU7E5ZGhhI6RC4eUOUrfBcchQKd7KgJH9NTsl_dh5L7imahd-Q21pDLPgsvjUbwK5SHAiKoDeBX5REzt4jy6Z-B2sXPTgUGW9QDLUotXgB2frBnlA4o6mkvh2mKyG66xVEtmHZDXCcXmnizu7GA2mmbUYcqkHd2v5_78meLWpN4lCzitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=ibPJ3XhwJXZhacQHMJFyVmX8HKAOaJX0eowK6q1_qkAUWzNev1qe9H6cE-AvyauP6KqC1BwaG1LYXy68lllfoY5xC0t97eEvNzuiSmfowNS4KFDUBKifCR7RTeZO9_g7I7RRM4oqvBNaU7Ap0vNFrehsVUlRlH3jpN12tBU7E5ZGhhI6RC4eUOUrfBcchQKd7KgJH9NTsl_dh5L7imahd-Q21pDLPgsvjUbwK5SHAiKoDeBX5REzt4jy6Z-B2sXPTgUGW9QDLUotXgB2frBnlA4o6mkvh2mKyG66xVEtmHZDXCcXmnizu7GA2mmbUYcqkHd2v5_78meLWpN4lCzitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=cBhzB0HiS0udA49LHZ-hD7K3YvrGdYWaoBm2UWeXoNAmVFv9MjaHYlTEBzOBbqUvscFrXX9hsOHsPc1cCp5OzNk4SV436aa_n7d67EluZHisUIS4GB6lEUs4P2-8-Yoo2VSXs_IWhowKjXZmfbIO7VC2_1kSz0wiP7ckmFxyjeZBQ6P8U_PPxD_zz3vCyG95KuZy4V-euK3tDo26YPkRtoZST0ElSeJ0XUAXcqhUmvBxAdx-U8Gpm9-_iAysPyg_Gh3L_cmj_F9DuhjIDXwQFxOOwNTRKB9bq8n5nlgiees9Bp5rdDlsW_ufAYSDUsWD_BquTB7sfNSpyDztWC_iN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=cBhzB0HiS0udA49LHZ-hD7K3YvrGdYWaoBm2UWeXoNAmVFv9MjaHYlTEBzOBbqUvscFrXX9hsOHsPc1cCp5OzNk4SV436aa_n7d67EluZHisUIS4GB6lEUs4P2-8-Yoo2VSXs_IWhowKjXZmfbIO7VC2_1kSz0wiP7ckmFxyjeZBQ6P8U_PPxD_zz3vCyG95KuZy4V-euK3tDo26YPkRtoZST0ElSeJ0XUAXcqhUmvBxAdx-U8Gpm9-_iAysPyg_Gh3L_cmj_F9DuhjIDXwQFxOOwNTRKB9bq8n5nlgiees9Bp5rdDlsW_ufAYSDUsWD_BquTB7sfNSpyDztWC_iN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD6jnEImkjvJAnMRG9nX0B9aG9lG_9wAeY3Azc-wDvEbHLSsjaOs8QmBbB2n7LQXERIuuHLbHbflB2aNnLR2vl76KPXPu0Ukjwu6V10Fq0i3JV-U0rV_SuUIRTvwddyj40aXgfStHI1pMIWXIj4zyf1FHpeTCkqBNy8MPHGcdY1JJh1T7qOA4rFFg4y7xu6vFEUfxNOYdNPV23B1Bp0T8MC4urP0peMNsp-Efn1Rcu-cClyCOtPLCY2gC_f8InfktqJvNcXi9g1JTs1CgLcf1YAXZDKV6fGjCVlJ5HLBgskq0ZWHu0FZj4NuzCXsTXrYKPAO4s8_TrgeqfXHXoWLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0MksR7-AeBATwGnCGg3RiN2ouO5kvQulDjpXZ9g8bXtwwaqlE2RYKHCWbxjSORyveaDF3eldudTbXz3p80JhVmfcjdMROaChcxoYFnEBJetEtdM5uOQNhX6wVfAn9eUeD_caqgUtpxjlkGwXhNp2aWwZykDYBR6i73Xl5Vgarp0QLDt82cOnBTfSOrLQEKI6ynCFjIE42TsNVsSJccMMzrhHi9_48BaSdJ6csfLDlPFTKUp7V0sUHUml991pMLU3HBJ0JtXkB4Zob3YLmWhgb3vpcU6lH_SmmBKx6s5pEHt-a_WodNSFNafeedHPBeZfwi7iDuVNuyDJrPoYYdz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=l1pi1WGSr2lRQGIP_hoDu41hT05n1b4CMOQGcim-YCwsj4HxiP8FLM-nMznfEh_RHu1CLIpHkwl1Jh-UA6haSTfT5UNvuzaHRpC6kzPk5_8BM6gfPCKKWZLCgaVBkdu877nIWH57M-CM_HKeBy_3jM2s8Wnhacg462_x05GGLfpFSQfySYpnzeszRjKCZ5CjysXRioQebHCKZ_52PGMGTAkm5l8SdoYgJAHs5iwscf3GHRoO-QGP77BS-hgdjKJyWN5d6sNi-KNenKtFT1bMnNRi4zQg-mlF7lj65bPHeBfbiD92GYODBh8Ycpo0itUEAW1QZpZBcvhck6J_pqT8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=l1pi1WGSr2lRQGIP_hoDu41hT05n1b4CMOQGcim-YCwsj4HxiP8FLM-nMznfEh_RHu1CLIpHkwl1Jh-UA6haSTfT5UNvuzaHRpC6kzPk5_8BM6gfPCKKWZLCgaVBkdu877nIWH57M-CM_HKeBy_3jM2s8Wnhacg462_x05GGLfpFSQfySYpnzeszRjKCZ5CjysXRioQebHCKZ_52PGMGTAkm5l8SdoYgJAHs5iwscf3GHRoO-QGP77BS-hgdjKJyWN5d6sNi-KNenKtFT1bMnNRi4zQg-mlF7lj65bPHeBfbiD92GYODBh8Ycpo0itUEAW1QZpZBcvhck6J_pqT8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=MkU0Q5Cc7Gxvt0J-sXkRmMlS4a9TkvIQy1DT5_evKt8T8SS4GF_uiMr_He4jtoLOdqCHSe-JkVaxMo5g4mBD6E7lJbiclHFirfFxswMvSZi-CLEr1R9ejWO7yNnRJPkrD3mP27eN2a0uNw1pgZU_PaY-uDr1OGsyidtwSKpxlDYeA4Wg560eoT8PdI-eZXLuV9gtq2MBb5zS_2hpJW70HlvWptK4wAA232ANZSiQJlEzT7xkBlMDptK3969AyoPyCm9Y9JfO3iNJlrIKvWCHz7LDGuR_28oaI6JyETmVdI5mnM1tTlEqIx9JSyopvpZ6BWhZZ_ksB-oRPU8jBQH5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=MkU0Q5Cc7Gxvt0J-sXkRmMlS4a9TkvIQy1DT5_evKt8T8SS4GF_uiMr_He4jtoLOdqCHSe-JkVaxMo5g4mBD6E7lJbiclHFirfFxswMvSZi-CLEr1R9ejWO7yNnRJPkrD3mP27eN2a0uNw1pgZU_PaY-uDr1OGsyidtwSKpxlDYeA4Wg560eoT8PdI-eZXLuV9gtq2MBb5zS_2hpJW70HlvWptK4wAA232ANZSiQJlEzT7xkBlMDptK3969AyoPyCm9Y9JfO3iNJlrIKvWCHz7LDGuR_28oaI6JyETmVdI5mnM1tTlEqIx9JSyopvpZ6BWhZZ_ksB-oRPU8jBQH5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=sCTyHtRdVcSYsv0_w9HK4Dwd5jVdaOBYIscihMqfpcvMA32NiYy5-9_lOidEYNXGXoVyqh9hRpMZ22OWc0aIo_fMapvubstDV1JrcowWUK-1EoAFBdtGBamuB1Rq9r2Fk84LQeADTt6nBRwyumirXiPtKNpsKV9MSZNVo1rrqDDYtIqhMUpnmM8Rau_clqNOMyAVJkfzqvKQ_4Chyh5emjo-d3IzMKUs6lCHLubmXaYE224i94xnHCPi6rMdaaLU8LZKA8jL-7-fE0rvFQVB5pd8kC6yQB58ZyRkO7YzW0vTFQR2DUkWVhR41ExXIhWanmIj2ewYl5oPaVeHYJZCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=sCTyHtRdVcSYsv0_w9HK4Dwd5jVdaOBYIscihMqfpcvMA32NiYy5-9_lOidEYNXGXoVyqh9hRpMZ22OWc0aIo_fMapvubstDV1JrcowWUK-1EoAFBdtGBamuB1Rq9r2Fk84LQeADTt6nBRwyumirXiPtKNpsKV9MSZNVo1rrqDDYtIqhMUpnmM8Rau_clqNOMyAVJkfzqvKQ_4Chyh5emjo-d3IzMKUs6lCHLubmXaYE224i94xnHCPi6rMdaaLU8LZKA8jL-7-fE0rvFQVB5pd8kC6yQB58ZyRkO7YzW0vTFQR2DUkWVhR41ExXIhWanmIj2ewYl5oPaVeHYJZCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=HdW8ur2Jh99f86McXPjnzJ6XUw06Dw9oyxwAJoZx9qNXeVS99v-5PD725VjV1SzTMnH3bo5ZH08AN4HB_I28Fb-6S9oleJeyvHXtaQuyZAQtj8IVmV-tt6VIob3LMEXg4mIDT987oJTDG3M2iLXv-RZxCRar5MCn1F_MhitU_DRBtDTxvAEf2TBrdUfOu3DoXU4m8KgyKbaQoauWGKvDnHY98Ssyu97W1QHsYf1gSmDKs1jCvKlNHUw25H6-SxbYZ6_9-05evxI4Tonb3XYMGrixVTQG4Bu2jkg-ErWXVnKHOULBbqFhyPDN0apnAmnA4Kb5ofNdiXC94GpIErGU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=HdW8ur2Jh99f86McXPjnzJ6XUw06Dw9oyxwAJoZx9qNXeVS99v-5PD725VjV1SzTMnH3bo5ZH08AN4HB_I28Fb-6S9oleJeyvHXtaQuyZAQtj8IVmV-tt6VIob3LMEXg4mIDT987oJTDG3M2iLXv-RZxCRar5MCn1F_MhitU_DRBtDTxvAEf2TBrdUfOu3DoXU4m8KgyKbaQoauWGKvDnHY98Ssyu97W1QHsYf1gSmDKs1jCvKlNHUw25H6-SxbYZ6_9-05evxI4Tonb3XYMGrixVTQG4Bu2jkg-ErWXVnKHOULBbqFhyPDN0apnAmnA4Kb5ofNdiXC94GpIErGU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=nycWzRO6y_MOOw_TPOuRZ4t2zB5oSo6BjCB35tjgZ4YxzG93caFpjVhyT1ewz--TRPues_7qVZRnCyMP4AapFg4xO0FiHEqq1EKN4rJNTNlzvE-S8a9PG9H0rlVJA4KJagQ7QTSia27i_Z6NLn55Lfn1zuMkvCDI_xqj6vajRBQbWVKZS7aQCGzYRbyPoxer80fYO6h_cnfZpMkQSoJ03tP5DwzvmofqQfi6nq9usFywswe2v4wBiFa_hYBtSr0BcwHWDb1vX0WpAOsQEgyrgfdPtEE-cjn13Kp0apOlxNhJ2_2fCv2MlHK21OkQyx5QLY_ZruzFtcTIRTJueep8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=nycWzRO6y_MOOw_TPOuRZ4t2zB5oSo6BjCB35tjgZ4YxzG93caFpjVhyT1ewz--TRPues_7qVZRnCyMP4AapFg4xO0FiHEqq1EKN4rJNTNlzvE-S8a9PG9H0rlVJA4KJagQ7QTSia27i_Z6NLn55Lfn1zuMkvCDI_xqj6vajRBQbWVKZS7aQCGzYRbyPoxer80fYO6h_cnfZpMkQSoJ03tP5DwzvmofqQfi6nq9usFywswe2v4wBiFa_hYBtSr0BcwHWDb1vX0WpAOsQEgyrgfdPtEE-cjn13Kp0apOlxNhJ2_2fCv2MlHK21OkQyx5QLY_ZruzFtcTIRTJueep8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFfjTJ_4ggfxKCE5uoDqbqivGCvszqun54llnssm4i5fchGnp4iJAAA5WlQhkugUEONiXIAqOef6F-wjH-7cLHtq8dztXxZNazYukcBooqq6LtlPfC1tlVTDSdX2wA54DTn8yGJNwr-wCxXy60lW7rFhrnLtaCk3gXorMS671NpNcjKaw9TIJU-keGU6of0HyISYMv-ut_v0lJDmi-OrazZiweRi4LBQwKCdTRZuPLLbyeJvNpYI1xwquAptP0wtV1QFtN5RZnBnQPaqOwUFEpoA9I9-jMwzNtV5xNh7UPHRy4yhwoYf7Qu2g1Hni042qKmMSBSHpO8TyxirbUopHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Nyi65DAFOaPshtTpxPn0hmZh-OLndixlVC2AFqixn_xT7RLKkIw42QdbuYFVWdVxr11cWfa-LaA2RybYWju-AhEbEm1jB4xTFjf8QpY9I-h-ZBQKVRg-ZFyby5awZldNAkaAj8iqR9ndY39ZqFu62XRbarNsyt7J9s37aR9JNJP0kJao8c2B0eqzPLfHj-BMDQkJpreiXrIBWjQGHP-AAzuaUcvA0qaIos8Jyz6__bWicGOS8CsHQvjl7-UmCuRLyJOOUgJLJT65486u5NQ6bY4fREvJ51vrROZiQGZeuo3viBzyR8xJX6hduLmNod5mSRtVsd-AagoLw51mp5fr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Nyi65DAFOaPshtTpxPn0hmZh-OLndixlVC2AFqixn_xT7RLKkIw42QdbuYFVWdVxr11cWfa-LaA2RybYWju-AhEbEm1jB4xTFjf8QpY9I-h-ZBQKVRg-ZFyby5awZldNAkaAj8iqR9ndY39ZqFu62XRbarNsyt7J9s37aR9JNJP0kJao8c2B0eqzPLfHj-BMDQkJpreiXrIBWjQGHP-AAzuaUcvA0qaIos8Jyz6__bWicGOS8CsHQvjl7-UmCuRLyJOOUgJLJT65486u5NQ6bY4fREvJ51vrROZiQGZeuo3viBzyR8xJX6hduLmNod5mSRtVsd-AagoLw51mp5fr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxo8wR3pU7CwwJEa0AWYt5pQvxx1nxbLkDTSrkIDVpxLaDzWc0zIIYUbC99baMmxDp6ljOwUqg9WJ8RH7L25y9i1ATJuXRwP5moztBWvCMJmj06Tk7TGZYL4gAaRNvYG7ZKtnn3ch6e9nwIWmk42EhN6j5eTkiqkAA5bPjm1wrQQAnY17OAeQ772i-5_4S1E63vTgByjl4S4k_FheyMyyzeO0WsSu2irpH9JysUbERQbp-MqR0OkVJBoBkGAcq9ProSFZuq_7E7pjN1TvmtKT5xIW2H0HJ0NSozS1S3cZV9_iyvWRSB0VzfsdIw8ApBxAQoN-BVNSNp_k0XzWTtSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=P6T8g7z2mAjt2PSP8kdlfranEHRj7m2M7eMYgttfs4poOrRwjx3zadPOvgsLJGxltnogo0c9nt-xG7haWBhip6eHwqOgifjyenG5NOKSJCU_1p6HhQL1rdgh9D-B0krxHl-Z60g86fdbYmJztfThdqq7CBouY2SNi7zcAFY9PTlVgEeapFijUjI1zhIJ6-CDArKrt-6I781mizadhIKYiLt1lKUpjREaLnlPC5_J7jqIj29vEV8iNiTrxZwALrHyGMlXdtrhKlgHg7wTWrR6HGn49eiUwMOOOI3P2zqiQdaUSzHS8dPJQPanZjr5PzcgDADHV3IU5Q882IEv4_nX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=P6T8g7z2mAjt2PSP8kdlfranEHRj7m2M7eMYgttfs4poOrRwjx3zadPOvgsLJGxltnogo0c9nt-xG7haWBhip6eHwqOgifjyenG5NOKSJCU_1p6HhQL1rdgh9D-B0krxHl-Z60g86fdbYmJztfThdqq7CBouY2SNi7zcAFY9PTlVgEeapFijUjI1zhIJ6-CDArKrt-6I781mizadhIKYiLt1lKUpjREaLnlPC5_J7jqIj29vEV8iNiTrxZwALrHyGMlXdtrhKlgHg7wTWrR6HGn49eiUwMOOOI3P2zqiQdaUSzHS8dPJQPanZjr5PzcgDADHV3IU5Q882IEv4_nX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=KxwxnAprp4Pl5UhQ6Ihdj0sye11kCvya3nBWEOkhQgtFDtPCpjg8sar6sCn8GkP1MW45RcJ_rrYvsId-wCEDn5rFtCw2CtqpJY-JZ7BO-SQdtutp5Ph2lNoeZKI1KmhAFYCkFQaZucKyBKFDsE6KuKCq5fPGP56its6G0Rg8jRhj3zDTOX-QSfSDFGC4N9yzqSzvR4j29uaIydh75puohktZ_gojRxLk8l3cHvlCTYA1KRG47yWPuQP2_51xdJsD38C4JD4uwrybxSKBuQKJhMuhoVpfqa3dz13EWXdPSy-HLvA8YE-8vrS8_FqpM0Ddk6NWSB7QPtQlUuAu13XtyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=KxwxnAprp4Pl5UhQ6Ihdj0sye11kCvya3nBWEOkhQgtFDtPCpjg8sar6sCn8GkP1MW45RcJ_rrYvsId-wCEDn5rFtCw2CtqpJY-JZ7BO-SQdtutp5Ph2lNoeZKI1KmhAFYCkFQaZucKyBKFDsE6KuKCq5fPGP56its6G0Rg8jRhj3zDTOX-QSfSDFGC4N9yzqSzvR4j29uaIydh75puohktZ_gojRxLk8l3cHvlCTYA1KRG47yWPuQP2_51xdJsD38C4JD4uwrybxSKBuQKJhMuhoVpfqa3dz13EWXdPSy-HLvA8YE-8vrS8_FqpM0Ddk6NWSB7QPtQlUuAu13XtyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLi_k39RfDN4NJW4LGnhZAhedgl4wxEJv0NXmlrRn9-83na0h1nkjVoFHTQvFDVqgrW88c4PjOwc7CpahR-btzM0qSI9fjJZ_HCSyVx_042fsc92Fgfo8FyYQ7DBqHPrY3qzghGMtPLfPVEvtOnTaolJS-zKAN5bQD4HdxcTCbqs_3qREu-1avneWks57yYwbtE8GVv3DIWv6FqUkFy1A-90WGmmR4Ij-BN_YMVTGwglmmsTrnsXa0occu6kG03eYkw1NZ-_0SdXwR-WCY36HVYapGHxkRigzA7Y2lveHGALTM9BtXO_u7ZqaZs8vQl8tZRIy8a20sy-MLIczwDiH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLi_k39RfDN4NJW4LGnhZAhedgl4wxEJv0NXmlrRn9-83na0h1nkjVoFHTQvFDVqgrW88c4PjOwc7CpahR-btzM0qSI9fjJZ_HCSyVx_042fsc92Fgfo8FyYQ7DBqHPrY3qzghGMtPLfPVEvtOnTaolJS-zKAN5bQD4HdxcTCbqs_3qREu-1avneWks57yYwbtE8GVv3DIWv6FqUkFy1A-90WGmmR4Ij-BN_YMVTGwglmmsTrnsXa0occu6kG03eYkw1NZ-_0SdXwR-WCY36HVYapGHxkRigzA7Y2lveHGALTM9BtXO_u7ZqaZs8vQl8tZRIy8a20sy-MLIczwDiH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=F9DqTPy6RV0duWXp6MX7ODM8VVx92oBmWL_LI5Mtd4YGrZXFgxQapsICtzsO8gcFhy3KjytyKibNuryQqbNCAljUxyTBwelpw9Fi7ZH0MKlu3DZ8wzk7fEIS4-jPABNkcMd9_VF-aINtheYWyxv8tES9Y9OsTJZ-ZsFTh07YC70Py_R6ts4nO0IXiXRPvUt24pxA0iOET5Ch6boii3zYqmUw3PyobTIvtIVJVLU_3SUCXcFCGyisK2Dbq0oLkk1TmHPN9gWo5I9NHAchMlA-12PK6SwbF7uXAH4EXGUuRY7KWbkzTEb2JMekh1DUxw-sGPmUkkp6N47_P1VFpw0R5TeRc3mlhFFY28VtqT6Pf1Czrf_mMt1-gsyTaVIeG22hOFF7f-Qk9rD6Xkw3uPBGL8B9M--UfBez8T-rpE6Wle8tFpP3yuX15fbbeBFPhhWMjMIr7u7zzBg4kDss--n7lxX-lo32GGc4zwF7q4nTICdNnQQO6Zk-FBYGDvgcmJEn4DHbaEa1fIu5tCfPKDZWPajjB0lDtxuldPcV-h1secntRrXZmx4TFSV7QLPRQRQnV3GGDury4Y97H2jQqg0yb-zqgXIlZFu0lxbarL9dAiWwRjQNukTFyDkEk6zGOwTtBZr7J2Pl5QQljRbaAHDqWmVdBdeSBGbVorpGmhk6bJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=F9DqTPy6RV0duWXp6MX7ODM8VVx92oBmWL_LI5Mtd4YGrZXFgxQapsICtzsO8gcFhy3KjytyKibNuryQqbNCAljUxyTBwelpw9Fi7ZH0MKlu3DZ8wzk7fEIS4-jPABNkcMd9_VF-aINtheYWyxv8tES9Y9OsTJZ-ZsFTh07YC70Py_R6ts4nO0IXiXRPvUt24pxA0iOET5Ch6boii3zYqmUw3PyobTIvtIVJVLU_3SUCXcFCGyisK2Dbq0oLkk1TmHPN9gWo5I9NHAchMlA-12PK6SwbF7uXAH4EXGUuRY7KWbkzTEb2JMekh1DUxw-sGPmUkkp6N47_P1VFpw0R5TeRc3mlhFFY28VtqT6Pf1Czrf_mMt1-gsyTaVIeG22hOFF7f-Qk9rD6Xkw3uPBGL8B9M--UfBez8T-rpE6Wle8tFpP3yuX15fbbeBFPhhWMjMIr7u7zzBg4kDss--n7lxX-lo32GGc4zwF7q4nTICdNnQQO6Zk-FBYGDvgcmJEn4DHbaEa1fIu5tCfPKDZWPajjB0lDtxuldPcV-h1secntRrXZmx4TFSV7QLPRQRQnV3GGDury4Y97H2jQqg0yb-zqgXIlZFu0lxbarL9dAiWwRjQNukTFyDkEk6zGOwTtBZr7J2Pl5QQljRbaAHDqWmVdBdeSBGbVorpGmhk6bJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLyWd6gALg2JBlxTByVB_nT8-1Q0pEkK22-4Kg0PKCy23wEX24LpXjKrZSoTsgFV_zDTuEuj3xY8H6hfTa5Xop5kJNWQprHXY0TgatmQfCmc2I9Vrd2xVKvtprEcIMQ-wPS_EvTq4A4LzpKb6gQeMir-Tkb-1pxfp7JFlr8EDEtlFYi3Yz6lnG9pLUOjDy2X89QAaHTD8jS2W1fdtBzljpG3c-c7gQ38kgNWgKuT0OZb8LSmEy3YgZJz7jWk1JWcjkWsnXWyZ7-8AGaQUEa5DBKkp72oQaHQjM7tzwPzYppv7iuzjiy_UUmoLdOr_TNoHUTqIoQ6w0xoueoJFDRa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3WKS8_bp8V4i2siZ1Z7dQr9oC34fYap1QyFqytM8pyttnKyLr0hXBO8WdkOqou0oRl6zycf687W1zN7bmV5SXDN-m9XOzyzO1MhufVfQwGXp_9_MyeENnmFAdrdYqNH40bZtnSxANQpfZtm3dvmAHfokqLJTAMc7ABc5zLfhlVs2kq8TAmQ5YPonFDpmBWdfdpzN5zZP-Pj8u_ehBpgZP34nzWXCgxzKCHT0nDmUI7nr3nTh79khxPAoQgVUkgB17VWd8Fka-l-kG12xBc_e1eldBc2Dv15OPKA1RzqWT3qG8lLPOsbE6tEfEY6T6Uq2RXkI3uMQ0iFdikVVb2mHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRxW40zNjKl3Ru8fxaRrHQ8YMX3Ou4mm2buxYjhmavyQr5Oe-ksiIIbYiuIpTJkXhT-LNd9fvhy5cAoYeGcVuO8Hta3nVIoNehzxYcwRrh5QMsM_29dE01dJp1uqJ-QlC668-r2ctK0zJS8fRzCnYa0UzLUYFnqNQnHl3VLBh5nPod6ZpiJ0KoJR479EwSPnOj6D9AzLhXgks3f4iL66SrZAmNi0iqugU2J8nAEhv3znAfKpcuojr4M4wSdHe32NGTxVSvn_JnOvEZ8s9Ty1_BXzfCpXVESrnSopR9J9g44JySVfDhhRHocQQ1dK4A-WBDN9jSQN73f7cI78ZDrDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=qBxe-QihzPxuQJb_a7gDB2Nq1wTSEnMpaQQFBPFKb1FWiqJhniLK-_Gs4p20c1Rz6CnbeBtwWdOZHolPoNiWxSyN6Rbcwbqpylyl6sPyWCRDO7AujXp3Snbi6E3A05agxWCJJEn2gp91r4fSfLGeblbmiyMw6IY1DlpiDBehJt5buxiIqjUIrffCXxn4H3zZwqnS3WHtegfJiE2lg2KOhr02VrQZdLIJfJhSkvW6t5MZwnFrcd1ZTVrsFtQ1bdZAmyElQovRuj8V6jpUWyRgNSuo675EM9f6tP1QbDn7zwbQhU_MXfi4yI1kE9bENAAGzFD97ipPSZJ6mgWptDXtMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=qBxe-QihzPxuQJb_a7gDB2Nq1wTSEnMpaQQFBPFKb1FWiqJhniLK-_Gs4p20c1Rz6CnbeBtwWdOZHolPoNiWxSyN6Rbcwbqpylyl6sPyWCRDO7AujXp3Snbi6E3A05agxWCJJEn2gp91r4fSfLGeblbmiyMw6IY1DlpiDBehJt5buxiIqjUIrffCXxn4H3zZwqnS3WHtegfJiE2lg2KOhr02VrQZdLIJfJhSkvW6t5MZwnFrcd1ZTVrsFtQ1bdZAmyElQovRuj8V6jpUWyRgNSuo675EM9f6tP1QbDn7zwbQhU_MXfi4yI1kE9bENAAGzFD97ipPSZJ6mgWptDXtMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=fC2oZUz4eUBdRrBmoL8JbpZLYzFY25QPx4s8v4aO2nM8Zx1E3HghLNVPznGv0w4Xb6WzGlEe1kpLkAIvKH2zKIX6_jh1VPkdpysgxXRpza_pABTMYraqL193iRD0pnAzSu9BZbcE4eenCo8uzzaVELGs8aQm523eVftYkwE2TuTinacc5ixOakCH59avO3PE2Yt-0ODiysrn3OaF8HJpWoexvDNug3yr90qeulXqxTdo4bb6gAOPP4euQJt0q2FSYJuJyYKNAmS1YYlk-qoeWNXhtE8RofxbN_njJ8WyPxlxeSzAb5hl561MVNnjFzCzfB_Xuf8QUz9dt3F1s6fQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=fC2oZUz4eUBdRrBmoL8JbpZLYzFY25QPx4s8v4aO2nM8Zx1E3HghLNVPznGv0w4Xb6WzGlEe1kpLkAIvKH2zKIX6_jh1VPkdpysgxXRpza_pABTMYraqL193iRD0pnAzSu9BZbcE4eenCo8uzzaVELGs8aQm523eVftYkwE2TuTinacc5ixOakCH59avO3PE2Yt-0ODiysrn3OaF8HJpWoexvDNug3yr90qeulXqxTdo4bb6gAOPP4euQJt0q2FSYJuJyYKNAmS1YYlk-qoeWNXhtE8RofxbN_njJ8WyPxlxeSzAb5hl561MVNnjFzCzfB_Xuf8QUz9dt3F1s6fQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=DKEENw4-zu7HE8q-w8F07k6u2uREVq2mZAi-LvU0sxtMTALUE8G7OeKGE-yaTJcXoDcQAHVRHuNjJ_N3WoSTaTZWUL4K96umAZvYZ7YTm3Nd43imVo-gjHHRCvCbVXDl_YRC_Wz67IVAXdZLj-Sxq007eownxlagOsEqJ85ZiaTumVgMEUG-R9EUe6P4KSmJlQ1ZQu0ArAPM4qSmaYh28hy90W3bTZS1IiY9J2Snma7yoNgtAkzlPjEfU7j8bx8Fyi-a2uksI325dzWhoWVtIYsrvstdlVtoFGyM4tXAdW30-R3WRimz4KVlUrw47gV6boF7mY4kbdXR40erPzmarg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=DKEENw4-zu7HE8q-w8F07k6u2uREVq2mZAi-LvU0sxtMTALUE8G7OeKGE-yaTJcXoDcQAHVRHuNjJ_N3WoSTaTZWUL4K96umAZvYZ7YTm3Nd43imVo-gjHHRCvCbVXDl_YRC_Wz67IVAXdZLj-Sxq007eownxlagOsEqJ85ZiaTumVgMEUG-R9EUe6P4KSmJlQ1ZQu0ArAPM4qSmaYh28hy90W3bTZS1IiY9J2Snma7yoNgtAkzlPjEfU7j8bx8Fyi-a2uksI325dzWhoWVtIYsrvstdlVtoFGyM4tXAdW30-R3WRimz4KVlUrw47gV6boF7mY4kbdXR40erPzmarg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=KXN_O76UkSlTumpXcmDlYs9PBWID9H-28cuJ9hEyhRuIkfYj3ErEQTotBQseeQpm4MeWRO-gWBgCJukS9f9-Z9kbJdCr2kGtgGm70Ce880mDE64i8FYNUKLsZ7WJNUvNUI2edjEz-uMXM_kAErAGWD_KXFG2Kc8gKbiQqieC5xiqgNF_03gGdd_ZHDK9K-zw_wrm7mC8cU9tvRlygxlO0Xd5GJfxruoQAKdhpFuEcFmL7tkRLWDCzYdXTkT9auh9nk8fEZ05SdoO4pmE9I5g0XuX2tve7vghJep18rT5L5xGYzDodIbj72gBwlkpCFLXLnvTRA0dyMW2dQI77dxPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=KXN_O76UkSlTumpXcmDlYs9PBWID9H-28cuJ9hEyhRuIkfYj3ErEQTotBQseeQpm4MeWRO-gWBgCJukS9f9-Z9kbJdCr2kGtgGm70Ce880mDE64i8FYNUKLsZ7WJNUvNUI2edjEz-uMXM_kAErAGWD_KXFG2Kc8gKbiQqieC5xiqgNF_03gGdd_ZHDK9K-zw_wrm7mC8cU9tvRlygxlO0Xd5GJfxruoQAKdhpFuEcFmL7tkRLWDCzYdXTkT9auh9nk8fEZ05SdoO4pmE9I5g0XuX2tve7vghJep18rT5L5xGYzDodIbj72gBwlkpCFLXLnvTRA0dyMW2dQI77dxPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=ctGAsCWMXKzwfTnlu2klpBSwXtmYUm1nhn52542Fp6sb-T43Fl_lfvCYCO6g9f43xchitGTMhE0gjeGyCMQh5Fh1uElOIgDTsWxHvQHOrj17sOzOGscV6p7-S0lc6brbdxGz8WUD1VhoInK_6F9fMwhQLnDLOq4QGzpWJ6nMiOCwkrtZNSnI60xVqSrW4V0RLBpuXqI3wi0sA9z1WItVH3WvBl-VyuJMbCPxMfCtXCHegA_Nia3RP9NnSFevKlSz3L2yyzGlVRYk8en3TiRLSl3M1F1fV9sYZ7yXaVUpviefqtEDD_dxfiNGmXfBkLXRhndzVu3SPczuLqe7PTr2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=ctGAsCWMXKzwfTnlu2klpBSwXtmYUm1nhn52542Fp6sb-T43Fl_lfvCYCO6g9f43xchitGTMhE0gjeGyCMQh5Fh1uElOIgDTsWxHvQHOrj17sOzOGscV6p7-S0lc6brbdxGz8WUD1VhoInK_6F9fMwhQLnDLOq4QGzpWJ6nMiOCwkrtZNSnI60xVqSrW4V0RLBpuXqI3wi0sA9z1WItVH3WvBl-VyuJMbCPxMfCtXCHegA_Nia3RP9NnSFevKlSz3L2yyzGlVRYk8en3TiRLSl3M1F1fV9sYZ7yXaVUpviefqtEDD_dxfiNGmXfBkLXRhndzVu3SPczuLqe7PTr2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=aTi70qv2gpEhPbk6yuWJqJ_JzbI5f5qqxfKZaPRDLIZMfze7Ni09aqGZxq1MQiDEqf660AobuUQKNr9KsjstQ0WCcDDA9kztbB1JPdmmebENjQVIbgk_MwD7riJxK-cCbZzR-Rx8JepN26_F4rBcIyXKL6a0IGTvV4z6ZTk148txakmkrjjviqP-J4HuupeuXaRxAR2rUFXiUsjD465N_0tAik-NnbJxXc4AZJyBWcWfmeOT4sT6mWb0RAmabX9p-X_hwk-Jly5TSOpY54ePc4eQhv323Re-a1hP3B-L_B_OtZpvQKsm3Uxp2BXv2GUFhBiClHoVXwTf00PP0gmeCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=aTi70qv2gpEhPbk6yuWJqJ_JzbI5f5qqxfKZaPRDLIZMfze7Ni09aqGZxq1MQiDEqf660AobuUQKNr9KsjstQ0WCcDDA9kztbB1JPdmmebENjQVIbgk_MwD7riJxK-cCbZzR-Rx8JepN26_F4rBcIyXKL6a0IGTvV4z6ZTk148txakmkrjjviqP-J4HuupeuXaRxAR2rUFXiUsjD465N_0tAik-NnbJxXc4AZJyBWcWfmeOT4sT6mWb0RAmabX9p-X_hwk-Jly5TSOpY54ePc4eQhv323Re-a1hP3B-L_B_OtZpvQKsm3Uxp2BXv2GUFhBiClHoVXwTf00PP0gmeCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=lvXg9F_qGkCV8YGEmJJcAy-Ok0LkxQ95qH-hvCdYKLKh-pZ68Hysol81Q4Ej9okQ8NYKa8TyvuBAT_23E8l9MP_Z94NFDbPnIeLzzpLEb23K05pI78yH7BUMH9XTtrCLk-iQjyQSDVXXahSWxflEwXgDJ1Bvi5ctBxVuwWRTwWZJW3I2G1wKO-T029-tlYvj8Fvqygo-IT0kOvr9fkNN7iNRR01jApC2vuA9niDhxDDVSdMcwuEiNlD44TTiN-3OCwrig6B2NoRSpk8VH1eSDR1ppJCpsS5IioipZEFoi5Lzv15s8ytblZEHe8FTJ1T9HF26dKWZZKNTFGmU1EE9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=lvXg9F_qGkCV8YGEmJJcAy-Ok0LkxQ95qH-hvCdYKLKh-pZ68Hysol81Q4Ej9okQ8NYKa8TyvuBAT_23E8l9MP_Z94NFDbPnIeLzzpLEb23K05pI78yH7BUMH9XTtrCLk-iQjyQSDVXXahSWxflEwXgDJ1Bvi5ctBxVuwWRTwWZJW3I2G1wKO-T029-tlYvj8Fvqygo-IT0kOvr9fkNN7iNRR01jApC2vuA9niDhxDDVSdMcwuEiNlD44TTiN-3OCwrig6B2NoRSpk8VH1eSDR1ppJCpsS5IioipZEFoi5Lzv15s8ytblZEHe8FTJ1T9HF26dKWZZKNTFGmU1EE9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=LsQE-Qs1ye6XDt3fUJ2zV-6QyNvgVV_w3WE3ZFIfPtNiLbihx1r0mFzcBFqzZ1VjbjguPobZhb9Of5F45d67HbBf1DraIySYwGUS0EmgNexILuFjTLWlp8JAOpY9ugsjBh8NbBTzNLlXmMCv9Wc7G9G5fzPHXNuN4dyH00Ivf2Wq0IZLaoawWDQgVFGFQ6xVjl_L-TBk0ofQMrs7K3BMw9c2eXQvVcaZJLQukT6J2CVaoMtq6pV447rVxWkLjoZYunRDpNbjJRABZFz2LPGTSSWcQI1YVw3R7Vju7HLJnmqa8rEms0xi2tvr3WUBdfxD1U1g0HO3c2cGwkJMf-YXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=LsQE-Qs1ye6XDt3fUJ2zV-6QyNvgVV_w3WE3ZFIfPtNiLbihx1r0mFzcBFqzZ1VjbjguPobZhb9Of5F45d67HbBf1DraIySYwGUS0EmgNexILuFjTLWlp8JAOpY9ugsjBh8NbBTzNLlXmMCv9Wc7G9G5fzPHXNuN4dyH00Ivf2Wq0IZLaoawWDQgVFGFQ6xVjl_L-TBk0ofQMrs7K3BMw9c2eXQvVcaZJLQukT6J2CVaoMtq6pV447rVxWkLjoZYunRDpNbjJRABZFz2LPGTSSWcQI1YVw3R7Vju7HLJnmqa8rEms0xi2tvr3WUBdfxD1U1g0HO3c2cGwkJMf-YXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqC8SGbFLPrq0Aqncu44NxRnqjmypObzcjNz5hXjpBW3_bFElk74MM6fnaAsRWw0xKbNVquFDc4_0RVPv-T0lt6hj1nKlkEhtHn0sHuXWHcRFKnbKJCq6KjGP9j6l7gpG3w-7zWDAPNzYZKehRiBo5dqhpTDlo3OV10SPQqWuqXZ-L9-OrmC7Nqx44RUT08Eu5TFoTQQtn0fiO99ZKRKi7d0xr8BehBg74W99oXad8qnm-Y4yxrZ2F1fC-ZzkscJYmA6fghfciWAmH-0ZfepWDVdK24him5LJ1dn6NtUqTheW0KxL-1CLnOvcGAqEJLnjyZviq9wYsPK3wQ8JEjCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=nYOSWIm6eorT0kGrxsoQj8JrobrtgcfDeIC1dnhjJZ8EkHJUs3i0CRCPbruFzHIlM6IVWVosfBx_XRctoJj8li3P5IIctzC8uJmY72C1Bv1ovPSkTbx3TCA5luh4F_lGPi7W2zqIu06zvGQshOkqPTBKt3PYQ36uxfjNymt_LqE5n52NIzRVLEvnsTHj4zIIGjzJluz70TPGMgenEQ_Yadm80TEjkT-RjNctQBxbRZjjWtVuXO2l0D0m6FJaedjk-U0swMEAK8wqGmoX_Csoo5gzr2KpMB7TG6ksYHS2IpFEYhgd9IZHi2pdvLOO3zw9nisInPxtRMsJbn7aifnDeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=nYOSWIm6eorT0kGrxsoQj8JrobrtgcfDeIC1dnhjJZ8EkHJUs3i0CRCPbruFzHIlM6IVWVosfBx_XRctoJj8li3P5IIctzC8uJmY72C1Bv1ovPSkTbx3TCA5luh4F_lGPi7W2zqIu06zvGQshOkqPTBKt3PYQ36uxfjNymt_LqE5n52NIzRVLEvnsTHj4zIIGjzJluz70TPGMgenEQ_Yadm80TEjkT-RjNctQBxbRZjjWtVuXO2l0D0m6FJaedjk-U0swMEAK8wqGmoX_Csoo5gzr2KpMB7TG6ksYHS2IpFEYhgd9IZHi2pdvLOO3zw9nisInPxtRMsJbn7aifnDeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPlH3IyQwqH0iGqgCqy7vd5CRiNXik2tare1aNodKpRfS7BE4g-ukTqV40BxPeHsb4iWsedAjjAVrsfdFxe1_QfufUHfZgNY385WXzvUoLw3qleoalr3sx7dDbL4qy3i1PMZwuD0OtxktyzAgtWxoSRoxQxxXiB0Jh8OsEVtb9g0ZNQKW5A6guTsZHeN_HMpNTralgOmPdBBXUYSS_DaU5h8_QBYJt-iNk2dfIptl8brZTGj8R98xREQvMlJfx1sKH-NUL3hPT-F8d2uPZuMSxqpMGgvwEov6AAcgQMmDmBDuuLqHEEIhWdzwi7Y4KKIn3uvW4310GC33YLmavTkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y2MmQ95tDHpNenzmmhZsfvq8zZRyV0TxgoLLLMRsjmxo2at2_AbNa_2GkONv-GrdNZcMqZK3CUtSrr-qeKS2R8IBCHJeJylENBV3mj61oYICVyOVsT7TidrpaobXngOQfqozVTds-WsVHcxEMEL1t2NvagUhL6KoHzgBWo5Fn_IMH-J4nk0rolYIPFQn6eH79wNKtqyHde3TfQk1AbL5Dvwrs0rCVIsfLFjj1qqi1LY8aln3_LZkCeunCGaSEPunW6uso6oGEey-LNrlzC5f7505-6hOs4TMUIa6dYJKkFmsxXJusYfWaIwGH4uAOb0bEQ4BCHmuC1rHMyUIh_mY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=Re8iKWAw23j9ek5AudRwkhGjliBEoXNZVjymZ8pJlEeZxi5wbzZ43b3nOV1mXKMO6RbW654utK1CX2SOZX_oQYWYg553e6B6MM-AdjnLgd3A5JkJ5kFlsQ5-0HTKdrElmeGAPGxSuU6AEpIWacOv8LSxVwCh8sTHl83idkHpnQVV7kwBq9tpTyUi5YrhNcMJHj1NdR3eWG36IEKcfQptfuP4KufjEBNF63X1L7h2dAeZsDigYWqxdLDFzQJbC9g5OrzRYXl3iSlJxE_Obd2qolwaIfW4CA7TGPxjb-tK8Ep__hvtcnR7_Xj4tQVuNUZ-lpvNm5hN7U0Dqyg3Xtg50A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=Re8iKWAw23j9ek5AudRwkhGjliBEoXNZVjymZ8pJlEeZxi5wbzZ43b3nOV1mXKMO6RbW654utK1CX2SOZX_oQYWYg553e6B6MM-AdjnLgd3A5JkJ5kFlsQ5-0HTKdrElmeGAPGxSuU6AEpIWacOv8LSxVwCh8sTHl83idkHpnQVV7kwBq9tpTyUi5YrhNcMJHj1NdR3eWG36IEKcfQptfuP4KufjEBNF63X1L7h2dAeZsDigYWqxdLDFzQJbC9g5OrzRYXl3iSlJxE_Obd2qolwaIfW4CA7TGPxjb-tK8Ep__hvtcnR7_Xj4tQVuNUZ-lpvNm5hN7U0Dqyg3Xtg50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=QWXRGhSxlurJ00eU2h1uAmARFq2hTtvwdbsh3l9xjkI1oVDF_650Y7bBbb1S1UREaiEIq0ti_4GjaDQUUbmmRIS0ZftTJYzGcKyjHibtqnoD9Zzhxl0eNGeO35rnYQtFnhVIiOKGKIIisw4OxM14ZUMp_mzN5g-5bojJXH7vBudWtc4cBRnI4WTkkJ_YXDz347aCgyekgrWwrAYsL9wwdwhbjVDDjHMS_wajnELzImqo88CA4IRRNeR3WEv2FNg_gHNulw72DuKtwowopG5FY7_d23tC4SlTbjGxMukdbsWJP3h2ShV4jL8nhXNTWOVtJLkImcbiULpS3w7A1fqjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=QWXRGhSxlurJ00eU2h1uAmARFq2hTtvwdbsh3l9xjkI1oVDF_650Y7bBbb1S1UREaiEIq0ti_4GjaDQUUbmmRIS0ZftTJYzGcKyjHibtqnoD9Zzhxl0eNGeO35rnYQtFnhVIiOKGKIIisw4OxM14ZUMp_mzN5g-5bojJXH7vBudWtc4cBRnI4WTkkJ_YXDz347aCgyekgrWwrAYsL9wwdwhbjVDDjHMS_wajnELzImqo88CA4IRRNeR3WEv2FNg_gHNulw72DuKtwowopG5FY7_d23tC4SlTbjGxMukdbsWJP3h2ShV4jL8nhXNTWOVtJLkImcbiULpS3w7A1fqjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=lVFZS7VZ-7igNIY1UalnEM2IhRQhxLiYMvwzXRgNhQ0u9E-vYq029ld_xe5y6bkGi-irtfZjvYwmhETDlVD6Aim5faE8QZHWZWFyj8cuTYGKfKytqKefXmd4ipGqdAPNLC-oj06CuoGJ5uVRoQeZ9m24m4ju6VlZ_i7UAvYZh_SQ1j36-lF9J4n3oGzPPN3epKAlcfDmujeLLgAourlmH7Vqptoi1PvoRUTTgz94sUoPodM7oPd9p4N_XKWCC4VH599Z_vjVTgNd23tfta-orI2WrI62Fo6IGZ8730N_en12jQTaQUBrwsY8_PFgVlngMrXy75JcZRJvMAbQPVdagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=lVFZS7VZ-7igNIY1UalnEM2IhRQhxLiYMvwzXRgNhQ0u9E-vYq029ld_xe5y6bkGi-irtfZjvYwmhETDlVD6Aim5faE8QZHWZWFyj8cuTYGKfKytqKefXmd4ipGqdAPNLC-oj06CuoGJ5uVRoQeZ9m24m4ju6VlZ_i7UAvYZh_SQ1j36-lF9J4n3oGzPPN3epKAlcfDmujeLLgAourlmH7Vqptoi1PvoRUTTgz94sUoPodM7oPd9p4N_XKWCC4VH599Z_vjVTgNd23tfta-orI2WrI62Fo6IGZ8730N_en12jQTaQUBrwsY8_PFgVlngMrXy75JcZRJvMAbQPVdagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=NBW0s7FzDP5kOafxmij7e6ZinYPaT26B7UYCD8qpFvPRHHzhTpCH5k9h7hTggLpq0Qax9OBNPDSpWd_rCjaZxDUhF7YZ7mPcuRidtGuLWCENbqDVbvKMXUbCxI99QV4EAAED9R80e83NMG-KifCQQwUv_jnUq1Xh_6V9inU0rpm3cizepYJMkne9fmswPwpbemCuRwb5-W4aMzlmu5CMfs9wYCV5MjkdqV0tfTRoEBY5XZIn5HFRQ_pVtg10PwlBbgzIizZf60KJ1Qr4AsvM5_f71eCXaMdn-2JXXibwS7ddHHIXKY7DUqSVNZQiZVkIaWxMTKNuvbEfqaMMrpU-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=NBW0s7FzDP5kOafxmij7e6ZinYPaT26B7UYCD8qpFvPRHHzhTpCH5k9h7hTggLpq0Qax9OBNPDSpWd_rCjaZxDUhF7YZ7mPcuRidtGuLWCENbqDVbvKMXUbCxI99QV4EAAED9R80e83NMG-KifCQQwUv_jnUq1Xh_6V9inU0rpm3cizepYJMkne9fmswPwpbemCuRwb5-W4aMzlmu5CMfs9wYCV5MjkdqV0tfTRoEBY5XZIn5HFRQ_pVtg10PwlBbgzIizZf60KJ1Qr4AsvM5_f71eCXaMdn-2JXXibwS7ddHHIXKY7DUqSVNZQiZVkIaWxMTKNuvbEfqaMMrpU-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=INMORCMbU7-nOa53i6nZi6ESY9Jpq-H7EO8t4aa1Or_qlv0oz7l27SaQais3KzDsBqfAbhdPMkY5WUbtzyusJxl6fblcsLC2Gnjf4bHJIWpWkq3qSHjWPLRnkAN87NMk-NkdjhjI0ERH65uZAlMoYYiLMFj4z75mGTI9SCBkVcoHuPIkpuxT_Zoswio4OtpsrLr1jzmtNKPWsJholSqZ-N0vBkQ1ZcAKgCoe1rBJkj9IuRrf_ilq0KM1z-nUjQOaZYe5ygn5ujzhkxhT5GsCRM5ZYip9b3owMM4k78jB80DpLGyXC_gyjMIeZm-C1HqYi07aBFOelf2_Dtq2uJ_MOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=INMORCMbU7-nOa53i6nZi6ESY9Jpq-H7EO8t4aa1Or_qlv0oz7l27SaQais3KzDsBqfAbhdPMkY5WUbtzyusJxl6fblcsLC2Gnjf4bHJIWpWkq3qSHjWPLRnkAN87NMk-NkdjhjI0ERH65uZAlMoYYiLMFj4z75mGTI9SCBkVcoHuPIkpuxT_Zoswio4OtpsrLr1jzmtNKPWsJholSqZ-N0vBkQ1ZcAKgCoe1rBJkj9IuRrf_ilq0KM1z-nUjQOaZYe5ygn5ujzhkxhT5GsCRM5ZYip9b3owMM4k78jB80DpLGyXC_gyjMIeZm-C1HqYi07aBFOelf2_Dtq2uJ_MOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=MlUvBw6tY8PUhrVYOMeHFO7xE6plhfohcfam-pNx8sy5xhoLmCGhZUlEQKvWdY8hnMqZJUdOVou8m4E8MnsPTWNTBG88xg4nEQ-VN4ernm2V331JlcDPcBiD3wnB6RE4RZERbW5RdqCrE8tuX9zN96JUE0oXr_3MVBST6zsuMguCxXZqpKt9aZq86vZi6IGcB8CqDPH8ruu2LNtsOUdjQPqcaj66ogf3meqoMMjNBZkhwRkIp7DQeuch-hm_3b7MkHQXs1UfmysZOXqevB1pm9im6yCIkKbEXZwe_ZT3J3lP3MvqvTcgNSXCBBCUQvM2x0eU3yh4EonD_bv2r8ndbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=MlUvBw6tY8PUhrVYOMeHFO7xE6plhfohcfam-pNx8sy5xhoLmCGhZUlEQKvWdY8hnMqZJUdOVou8m4E8MnsPTWNTBG88xg4nEQ-VN4ernm2V331JlcDPcBiD3wnB6RE4RZERbW5RdqCrE8tuX9zN96JUE0oXr_3MVBST6zsuMguCxXZqpKt9aZq86vZi6IGcB8CqDPH8ruu2LNtsOUdjQPqcaj66ogf3meqoMMjNBZkhwRkIp7DQeuch-hm_3b7MkHQXs1UfmysZOXqevB1pm9im6yCIkKbEXZwe_ZT3J3lP3MvqvTcgNSXCBBCUQvM2x0eU3yh4EonD_bv2r8ndbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=GqvEyeEA_esce1fF0nGvoufJcD_66gGnq4JnuTbCOU1xnRUdUKl--Nh5DjUgf_c4-SEOhdGBRZ_fa7dHZo74qkt7CtKSuwBrKuoB5r5Ph2_Nu2UY_55qOSB7GCd9f3inwZe1V0PtUi7o1LZA_nUt2JMdJY3Hdq6oOkKU7srLUdBB2MSSk1A8NTtZtzcGpHSyet4gw120clZqLeB0uN557cnRbWmuHKTl3Oz5Ziw8kjcEMeZgon124MLB392Vs3hJb8dtCaojgBkgRJ8HK5MASXeJYBrra_MsxOkBlP6fsmuJFUfRCYoYjJLFd4QSkjGkjBJjzIE3ciLgS0nlSuD1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=GqvEyeEA_esce1fF0nGvoufJcD_66gGnq4JnuTbCOU1xnRUdUKl--Nh5DjUgf_c4-SEOhdGBRZ_fa7dHZo74qkt7CtKSuwBrKuoB5r5Ph2_Nu2UY_55qOSB7GCd9f3inwZe1V0PtUi7o1LZA_nUt2JMdJY3Hdq6oOkKU7srLUdBB2MSSk1A8NTtZtzcGpHSyet4gw120clZqLeB0uN557cnRbWmuHKTl3Oz5Ziw8kjcEMeZgon124MLB392Vs3hJb8dtCaojgBkgRJ8HK5MASXeJYBrra_MsxOkBlP6fsmuJFUfRCYoYjJLFd4QSkjGkjBJjzIE3ciLgS0nlSuD1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=v0quGu3ihjl6yjC7u4ID6Y_adgsiNEIqmXTcfLUtH16arHISTs5AKlN4EVq5OiVrqShKj0N2vnfodzdM_1150qxHA8dFxvjCuwivTVRWyNfIGhGekmiCVArlk5cNxaD5lTsiTK_c_CKK28Vp8OMH_ppOyvrrMCAjx9qWgRfDxPOzJsvocYpejgVBW8vyYsAiNZTrQOy1sf_VNRYKCv0cEICmOxpW1-sVdZSQ5-11BJ1Fmp7sdhmTbQP7pDTDCDjNahPwTMZapoocyztBCUH-ip9ESztjfuaSS4cAk1uQDBg2CzMDWUUSUV4oAfEFtUUTshzPSGprlAWuijJDodKd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=v0quGu3ihjl6yjC7u4ID6Y_adgsiNEIqmXTcfLUtH16arHISTs5AKlN4EVq5OiVrqShKj0N2vnfodzdM_1150qxHA8dFxvjCuwivTVRWyNfIGhGekmiCVArlk5cNxaD5lTsiTK_c_CKK28Vp8OMH_ppOyvrrMCAjx9qWgRfDxPOzJsvocYpejgVBW8vyYsAiNZTrQOy1sf_VNRYKCv0cEICmOxpW1-sVdZSQ5-11BJ1Fmp7sdhmTbQP7pDTDCDjNahPwTMZapoocyztBCUH-ip9ESztjfuaSS4cAk1uQDBg2CzMDWUUSUV4oAfEFtUUTshzPSGprlAWuijJDodKd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjJa2Q93lmZEQq5MrDy9n7WNLJ3RDm4lI_5HHtKzinvAt1nu_itzAiFJsmJWP6p1KdAmZRsUJOMH6crxEAjd0ah2rCkz7GL7_elQADmcfV1Urr5WkvLplvFBY5SkrdldnTZ1hZwRyBBgNrVU9vm0_V3aTRpZpvNh7jTe85HnWpH34pll-K3jNxLlWp6EgthxGPTmZMELLc4O-UGvzOWUWbcN2sUq_pHzvXQmXEAkFKqrFK93ccB3bzr1DQMeWVJ--Zio5ld-L_l3uPT5WxNNWwLObi76Gx0prMoVmYnplVpdGRzhqa1kODmX-DRfgxzo09BjjGsi9DSXGn1KegdFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xey-0yfLxQGHkriyPnzDBFBw3xN7v9rXGwUfV6o-WOA2_FfKuhKInG6284Iusjn9IVleT2intpCyh7cHiuyRyDulSqoSAZjQ8Ror0ZJuD2deccHN1KCmqQwOPFW11VgCVqgpueS8u-LpRVYOaBgb4YxQe_ZXtaxWL3ccujznOZj3jAswvQCBKh7NFIWvPxDyebK1YpjOGmU_37pLXUHVUf9axwBhW2YY4xGmITwNfaHjltaK0ePj_5ZgmQYbSLt0Na40ValQI1UpCvVckB_FHPU0zhvTO81pxw41S9E3teBWQmOltqCx9ZPoxuZvO32zrL_jGKYC8lPxQJ_jim8a2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=A7Qkg9tqmGQ9Q424HaIv9SoJ89nWS0s1J__bNg1_rVGoAjH2BtRWFZJdYbqlrOzbkX5dVxxiW3nyIg329jA-JRgQZbBNf-GjlY9kcusKrgMUT8CjMLzHPAGFVH3BuIP9quSSyFbjITKgxsQMBZIeudK5X6o_LGK1AlKty9YkiidUihNsEa_UyqGku6y4p-u1o3rTH3UCEdPAop2D50wIVuI5WpmkpMJsBWFwnPLymGZqleu6EWLCsngpOyxsHboc03edqNhZ_1VJ8dOqF362ETUr_yBTjeuKAw-Vwo-cX96OYhkIh_XtPcKCDCiFq9GLTXBWCeEQR8h6C_eMAC1iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=A7Qkg9tqmGQ9Q424HaIv9SoJ89nWS0s1J__bNg1_rVGoAjH2BtRWFZJdYbqlrOzbkX5dVxxiW3nyIg329jA-JRgQZbBNf-GjlY9kcusKrgMUT8CjMLzHPAGFVH3BuIP9quSSyFbjITKgxsQMBZIeudK5X6o_LGK1AlKty9YkiidUihNsEa_UyqGku6y4p-u1o3rTH3UCEdPAop2D50wIVuI5WpmkpMJsBWFwnPLymGZqleu6EWLCsngpOyxsHboc03edqNhZ_1VJ8dOqF362ETUr_yBTjeuKAw-Vwo-cX96OYhkIh_XtPcKCDCiFq9GLTXBWCeEQR8h6C_eMAC1iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=du0RgKoovS7MLa9Cf449bmUdlMd_5JB1lkCngaz9xim2lRqjceue1PypUqnlCdAKRZVZ8Y2c4CXYHJXFavNjt28VKjeba-kE3SUTjvNDaWUGCp29fllldEyumNK9zQS_u7oK_c3yAZzv7kHzVqztNtUwuMyQKVII16323GrLFKh1Z2FGG0tt8eYHQN9LCNt6IVKcnYtJuDYJt9X4BOUoSKRhxBcWd87lzh_2MUFPhJnuSekQXrmfT5BzS_UwTFe3KiaGem2KvEMdYNZgfbdz15cKiN7gySKOYM2AzbU7_RvhMjq4MHMcsvTFdJW8g54cikm4NnrIn0xwZb6Pj5dcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=du0RgKoovS7MLa9Cf449bmUdlMd_5JB1lkCngaz9xim2lRqjceue1PypUqnlCdAKRZVZ8Y2c4CXYHJXFavNjt28VKjeba-kE3SUTjvNDaWUGCp29fllldEyumNK9zQS_u7oK_c3yAZzv7kHzVqztNtUwuMyQKVII16323GrLFKh1Z2FGG0tt8eYHQN9LCNt6IVKcnYtJuDYJt9X4BOUoSKRhxBcWd87lzh_2MUFPhJnuSekQXrmfT5BzS_UwTFe3KiaGem2KvEMdYNZgfbdz15cKiN7gySKOYM2AzbU7_RvhMjq4MHMcsvTFdJW8g54cikm4NnrIn0xwZb6Pj5dcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=Z4rGo-qdQOkmk7VjJRxGIYSBEe8Nyv23RUk-DNWnxmeXgNGfttYmwXpAe1-lrZCOJHnw85REGQis_AVc-yUr9rIKujh7PD_xhIpn5ubdtnk__kkqHSstYBFxnSjIT3xQbNwtiERH1xUHzs_Sc92b4STghRJLtegjBJRNG_G6b3HvpIZrhhkG1W7Rwj35nC9iq8hz-gk7n8bXBPNr6P4OErX2369_Sf0QmdDCMJPu11zMo64iZB0xA6FjjARVHEaYFsqJTDR5apxlsCe0tfTMsK8ftoOfH-JjOpQMVIrEwURjPWe1hcc__nPqM-_4IuT3c5yjYjlruLVb58o0hiHaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=Z4rGo-qdQOkmk7VjJRxGIYSBEe8Nyv23RUk-DNWnxmeXgNGfttYmwXpAe1-lrZCOJHnw85REGQis_AVc-yUr9rIKujh7PD_xhIpn5ubdtnk__kkqHSstYBFxnSjIT3xQbNwtiERH1xUHzs_Sc92b4STghRJLtegjBJRNG_G6b3HvpIZrhhkG1W7Rwj35nC9iq8hz-gk7n8bXBPNr6P4OErX2369_Sf0QmdDCMJPu11zMo64iZB0xA6FjjARVHEaYFsqJTDR5apxlsCe0tfTMsK8ftoOfH-JjOpQMVIrEwURjPWe1hcc__nPqM-_4IuT3c5yjYjlruLVb58o0hiHaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=Bd005VA2ba7IDWSL05TrkDlK5mi6Q-ECkX-44Z3KU2XDkryvvQs5KIjTgONG56XN8bxiaF9MjW9JBln-t_A7ScY3OdLelr31ZdlPgY2d8Jp5Skis94o0QOYI13pAS8_LpyWS1HN8DDRmpiVoTfCI9h6o8ipokDrA0gDcj_dIB39emyVbxcR1SuibpaRlclqSb0DMw4GgzmVT5smqBWN0BSSZ3fwsNgPLEYrlM_T1Ei-PmzUuU6fHudq9Royi6n5xIDO0RkDRf6mcVwhUIklkHHZraWji5V_tIC0qabKg6keuSQqPQaLZWnmGhRGfpkVJ6096r3Yk4R5vc0QWsAdMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=Bd005VA2ba7IDWSL05TrkDlK5mi6Q-ECkX-44Z3KU2XDkryvvQs5KIjTgONG56XN8bxiaF9MjW9JBln-t_A7ScY3OdLelr31ZdlPgY2d8Jp5Skis94o0QOYI13pAS8_LpyWS1HN8DDRmpiVoTfCI9h6o8ipokDrA0gDcj_dIB39emyVbxcR1SuibpaRlclqSb0DMw4GgzmVT5smqBWN0BSSZ3fwsNgPLEYrlM_T1Ei-PmzUuU6fHudq9Royi6n5xIDO0RkDRf6mcVwhUIklkHHZraWji5V_tIC0qabKg6keuSQqPQaLZWnmGhRGfpkVJ6096r3Yk4R5vc0QWsAdMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=SLjPJlpUzp7Fy667JthItHvc-vtchhCUb6H902hYpAWZwCsLxi0p_WJiresdc4grdcBpfV2YlBCKUwqW0cyLCL-XC70-KROQX0k2d7Qfyt3ex28VhJtpJzaz5NKIO8PRNgx2i0OKcb4HmwN2NCzQqPXVeIYqCOLdqjT4vP6GZON9G2TCHu2CKFUkuLDNtWiHCizPgGbEl2yeAPqdx2MFV1EbwIvgwUlqpKGXv1q3c4k1TLVe7SLrE8bk83hmFBC77LzfcuK1DWeH7OluNQM7mD3jhNK1gslyzP4lxYhmCyggDkisclGR-Bi_47PehwBJbnx_tKSz913sioMwkZ-JSYsv36Vx61vIBEKX-LtMpl-Lx8bjKtZX_yKlivfmaV0mx_DTGNINQaTRLjLJhmap8_YA5uAaUhPsvGlf1IIgf3aFuhXWgo-KxJGpgV0fsM8ZeTEh7ZdXP5CSBnpT5uZaRSapk_fxiNvxw9pqniH6cuVNWBi8Ok8cIPUMnQpd6OcnxzCVaP3NyQKqWQ8zJWgrQLlIgIoNvBcg1gILaIDSK6-SPA1LjfFep027BlSxEo6oDb8ufcZSB-zUZYoN_v7YcVQqc_2bsDW6AAL_bxQB1SWRzJrPG2WU0ZNbo9PjUNgnzhR6fHp2ZaxQ3SveHuv3oc416dfHs5FlOtNJU6F1_Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=SLjPJlpUzp7Fy667JthItHvc-vtchhCUb6H902hYpAWZwCsLxi0p_WJiresdc4grdcBpfV2YlBCKUwqW0cyLCL-XC70-KROQX0k2d7Qfyt3ex28VhJtpJzaz5NKIO8PRNgx2i0OKcb4HmwN2NCzQqPXVeIYqCOLdqjT4vP6GZON9G2TCHu2CKFUkuLDNtWiHCizPgGbEl2yeAPqdx2MFV1EbwIvgwUlqpKGXv1q3c4k1TLVe7SLrE8bk83hmFBC77LzfcuK1DWeH7OluNQM7mD3jhNK1gslyzP4lxYhmCyggDkisclGR-Bi_47PehwBJbnx_tKSz913sioMwkZ-JSYsv36Vx61vIBEKX-LtMpl-Lx8bjKtZX_yKlivfmaV0mx_DTGNINQaTRLjLJhmap8_YA5uAaUhPsvGlf1IIgf3aFuhXWgo-KxJGpgV0fsM8ZeTEh7ZdXP5CSBnpT5uZaRSapk_fxiNvxw9pqniH6cuVNWBi8Ok8cIPUMnQpd6OcnxzCVaP3NyQKqWQ8zJWgrQLlIgIoNvBcg1gILaIDSK6-SPA1LjfFep027BlSxEo6oDb8ufcZSB-zUZYoN_v7YcVQqc_2bsDW6AAL_bxQB1SWRzJrPG2WU0ZNbo9PjUNgnzhR6fHp2ZaxQ3SveHuv3oc416dfHs5FlOtNJU6F1_Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=CprNrI4G6HwvGfFmr6bwIT1scA76L6Re3JOoDGCDMCcbbBRsqZx4kNtkvXRk-a5SERzbNv-oa6VD5BJcLByDIk5JJB2kDIlR8OwxJtROHbUf0q8bd2hdWzG_-bVwBWEfzQyRMCIhOVUcgEJ6G-HHS-TG0PxJqWMpaqhshgpRT4MxXXgLnBArv1S0lLdFmq0aOLx32RO6RTa2AaEmhus4juFG_9FUXBc2_D36dKLc_s3UACrO3tioIlpmuDv4In_WzGyHKzVE4oc7mpo0c7UEGPgkp_Pn8C0hyGSUAThA1Jrq7TScjwiHzCr2D2XGNAAwv8vKJ0Wbkhp_AuURmBuOeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=CprNrI4G6HwvGfFmr6bwIT1scA76L6Re3JOoDGCDMCcbbBRsqZx4kNtkvXRk-a5SERzbNv-oa6VD5BJcLByDIk5JJB2kDIlR8OwxJtROHbUf0q8bd2hdWzG_-bVwBWEfzQyRMCIhOVUcgEJ6G-HHS-TG0PxJqWMpaqhshgpRT4MxXXgLnBArv1S0lLdFmq0aOLx32RO6RTa2AaEmhus4juFG_9FUXBc2_D36dKLc_s3UACrO3tioIlpmuDv4In_WzGyHKzVE4oc7mpo0c7UEGPgkp_Pn8C0hyGSUAThA1Jrq7TScjwiHzCr2D2XGNAAwv8vKJ0Wbkhp_AuURmBuOeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
