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
<img src="https://cdn1.telesco.pe/file/M4I3l4xnUS9IEBeDLpKFwylp3F2u5GAu4tBpzM7jwAMVfOGEkaq_yYR7iqeJuJ12LbuaUIIJrmbYt-eydXPPf4MdaznEPMKc0dTzCJomE2tSQVe_-OyesFIfsuiKFEIGVwsl1h5hJPTi-IFznAgmVgIj0yup9X3egbl9E2aHQzKO3xHAntEnLp9Lc4ZH10UuTfMElToeHTrJFre-0lcOIV6KQAX0oYyT1l18YjikRiXeFZSlACbFyIfQEl46g0JJkrdMqVLu9tVuM0vyHt_u3x1fnL7NXsNI4y9SYSrJo1BQCkZP6WldoAUYOeSkhesnKVjddM0q4a1g--CDjRJmgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 123K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 03:27:44</div>
<hr>

<div class="tg-post" id="msg-3177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینور کلا تعطیل شد آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/MatinSenPaii/3177" target="_blank">📅 03:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YL-TXEufqqXlIspNSsX2gdedSYZvrGFaeOAHzG2lMRp0THYIUddHhZORujGtwDyQdQ62jLXHVZy_PC5KiOY7hUi5sjlFIZwZqDj4YMWRQhlF_eYGjSM8W3WhbxKknmgiJHw6RgZo_1_8JrjC-liBfYsFSRqDi8wUa6yFw05JJTATBOARiotazURh7l8hZVDTC2bx3rO0foA0w8MrpHBPAOljY22ZYv7rNODVTh5UTfLOvvH0Mf7bxL1OUNuXoai5Jotn-thhornbIFCtDXXifqd3_lX3rHjzL5H6L-HrniUllL64CWm78vV-YARrQ9G61SlzMUVB8_CTfHDkGHVzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینور کلا تعطیل شد
آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/MatinSenPaii/3176" target="_blank">📅 02:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spoof-SNI-Configs-List-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی کانفیگ ویژه‌ی SNI Spoof با پورت 40443 بود واستون جمع کردم از کانفیگای خودم و بچه‌ها و هرچیزی که توی کانال‌ها گذاشتن، توی این فایل txt واستون قرار دادم</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/MatinSenPaii/3174" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">با این کانفیگ‌ها تست کنید:
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&type=ws&host=www.creationlong.org&path=%2Fassignment#1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?encryption=none&security=tls&sni=sni.111000.indevs.in&fp=chrome&type=ws&host=sni.111000.indevs.in&path=%2F#2</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/MatinSenPaii/3173" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/MatinSenPaii/3172" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">Matin SenPai
pinned «
انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3171" target="_blank">📅 02:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkub6-57DQYH_MqLcN0_xYH8GCYrgSqumdFvW_hZ5XpTHCQqz57VcjVAqq2ytld5_HtepfamFytvQto8BVpB-TVDj22mLapjy6RjnsbQh--4kH25l0_1xq9g1y82_9udl174XKzOBnl5YJR89joVf6DMJkdBJll6RxAZ9DAUIUnmCuNA08lDjVcGBGblEgCohW16gxdtDhDsOYCeDyAbk8RrvrOkxr3S9C98oBqKzU9cMmCkyatSAD__R3lI4Zo3wKEFSKtFl7n5-jJifN_9iDpitWTOFj6m_kmkM43-cHzFbMaZt0UC78h6vqmY6mHu1bOXavqxhQ0Ffx4ULlQmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها واسم فرستاده از اسپوف
برید ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/3170" target="_blank">📅 01:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/3169" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست:
https://t.me/MatinSenPaii/2627
جیسونش هم این:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
پینگ بگیرید ممکنه به جای 229، 230 نیاز باشه بذارید</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/MatinSenPaii/3168" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/3167" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مجددا، از تمام کسایی که استار میزنن زیر پست‌ها و یا دونیت‌های کوچیک و بزرگ می‌کنن تشکر می‌کنم. من قدردان همه‌تون هستم
❤️</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/3166" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3165" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://guardts.ir/f/19995aceb6bb…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/3164" target="_blank">📅 23:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k0RWgTvpesaY_JmCyjt69J3ucgcebBVWnJs9Be0pX7G6Tju7eB8gCYLN30frwevrjpUNvUFqiC0UtcZDSGUXgNTBrOYlgCOw7NW43AB4ljh529gkymRuHpmrM8G9mAriZ_u7X6byHKYDrNj06Y-D61TCMVAWWBx-bw9H6Gc553UA3ZdCpggSCS4RoC45bn_joBhYKp-PlUH6BrdHBi3u3zJQnRdJ3mcvJPL3sy0i1Tlf8pwHE1F6g6EicfStvfvayy4ZMSK07upDm-vAPJzepg0L8GPWzHtLuU7_AxbFEHhWQ0KK9lUgUe28v7qDBIag-TxG3u98_7-WPeg5BAfbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای میت، من با گوشی و لپ تاپ خودم روی دوتا جیمیل چک کردم و تماس برقرار شد و همون صدای Echo گوش‌خراش معروف میکروفون هم بین گوشی و لپ رد و بدل شد. نمیدونم چرا برای این دوستمون جواب نداده</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/3163" target="_blank">📅 23:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/3162" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3161" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">17.1 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 20 اومد چهل دقیقه پیش(توی ویدئو ورژن 19 استفاده شده بود)
و روی این ورژن،
Github.com
هم باز میشه به راحتی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/3160" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moein.bpf</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یکی از دوستان این رو دادش:
این برا سینگ باکسه اپ ها هم میاره یعنی لازم نی از مثلا سایت گوگل میت استفاده کنی با اپش میری</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3157" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">متأسفانه جمنای و گوگل کولب باز نمیشن چون ما تحریم هستیم. یعنی از خارج تحریم هستیم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/3156" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">با تشکر از
@patterniha
، برنامه‌نویس پروژه، علت ضبط این ویدئو اول این بودش که مقدمه‌ای باشه بر روشی که برای یوتوب می‌خوام بگم، دوما این بودش که حس کردم این پروژه به اندازه‌ی کافی دیده نشده.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/3154" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">certificate_generator.bat</div>
  <div class="tg-doc-extra">56 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلهای سرتیفیکیت جنریتور(ویژه ویندوز)
و
کانفیگ MITM (ویژه اندروید و ویندوز)
لینک گیتهاب پروژه:
https://github.com/patterniha/MITM-DomainFronting
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/3152" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود
این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.
لینک داخلی ویدئو:
https://guardts.ir/f/19995aceb6bb
لینک داخلی V2rayNG:
https://guardts.ir/f/7ae1503cd755
https://c224731.parspack.net/c224731/v2/v2rayNG_arm64-v8a_v2.1.7.apk
لینک داخلی V2rayN:
https://c147793.parspack.net/c147793/v2rayN_windows64_v7.20.2.zip
⚡️
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
لینک سایت Regery برای سرتیفیکیت جداگانه روی اندروید:
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
لینک فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/3152
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد MITM، تحریم سرویس‌های گوگل رو دور بزنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3151" target="_blank">📅 21:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/3150" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عالی بود
تمام 133.9 کیلوبایتی که برای این ویس دادم ارزششو داشت
🤣
🤣</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3149" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmohammad</strong></div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3148" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">rdnbenet-windows.zip</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3147" target="_blank">📅 19:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVxR9PAk-fKZ1uOJf6eByx-4ROlXNrlhWQRqIpGIG_1FkO2xWVGNrTrHmOusZlZuW7uJZsPFVxygywGP-_tF5KnzF7x3wkIBJcJY0fm88QPJPO973qcj5QPbfE_HisJQaQ4nDQa7dUDa-5edFlcdrnUHu4AWu9ia6dat_X1HhckgWYBPI7v-alpjGUNewCieJsmiPf8UJWDplatBBSpakhJOuyBmF1AYdtT8UToTdabSVojyf__7VOK_cBo4iukJ_gkFV_I4q7BaqjKNeJvaxdMsMZAC8zCFP1vMhDuf_dEoK4M2P5HmvuysenBw2A4H1BGi4_Jra7lseNrCjdqLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه متد یوتوبه زیاد ساده نیست، اما خب قابل تحمله و زیاد هم پیچیده نیست. اون شکلی نیست که بتونید راحت برید توی یوتوب بچرخید، اما خب محدودیت حجمی و... هم نداره.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3146" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رفقا متد بله رو چندتا از دوستای متخصص توصیه کردن که اصلا نه انجام بدیم نه من آموزشش رو بدم. بر پایه‌ی سروش هم یکی الان دیدم نوشته بود و واسم فرستاده بودین. چون حتی سر متدای ارسال فایل هم اکانت یه سری از بچه‌ها بسته شده بود توی روبیکا و بله</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3145" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب با این اوصاف من آموزشه رو می‌ذارم. چیز پیچیده‌ای هم نیست اصلا
دوتا ویدئوی مجزا میشه اما چون خلاف قوانین یوتوبه فقط اینجا می‌ذارم</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3144" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-poll">
<h4>📊 اینایی که میزنن دیدن نتایج ایران نیستن یا حال ندارن چک کنن؟</h4>
<ul>
<li>✓ ایران نیستم</li>
<li>✓ ایرانم. حال ندارم چک کنم</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3143" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3141">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-poll">
<h4>📊 بفرمایید که،</h4>
<ul>
<li>✓ meet و drive بسته‌ان یا یکیش بسته‌ست❌</li>
<li>✓ هر دو واسم بالا میان راحت✅</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3141" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گوگل میت چی؟ :)</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3138" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qp5v5095_1IDgVH4nHGHc3Pe129wR31d9xG1oWeC7TSDHth-Ipea8tqhQL4qm6GE2qtusjq-WKtYTCF7IxLLEcP0XE3PQqm3f2hKCAjUbeOpx0CPwfYb1HJ9lnMzYV0xzcUEg1cLYuu9pSg0svEBcXwA6lqBhTsJiEkErmO-uemdA0smD9JLa93bJ88oDY8wDZlOnEbgVw1t8B3UQdhnOGn1IBX3zL6z2Fu_WdTb2Urn8YsrdpEE_zqqEYynTh3nD1nxQfG6bMMfWcKQ4uwQ67UMzwteL4_QATI1EXdqx7lCHfIpA_gE-ryGqkh7u6NKaiw2t6zsonafLBX_DocDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3137" target="_blank">📅 17:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3136" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان،
drive.google.com
روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3135" target="_blank">📅 16:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بذارید بگم که چرا از زبان پایتون خسته شدم برای توسعه‌ی Back-End:
اول از همه، magic methodهای افتضاحش. یعنی هی باید __init__،__ str__،__ repr__، __add__، __getitem__ و هزارتای دیگه رو یادت باشه. که این باعث میشه هی دست به دامن ai بشی. و همینطور باعث اینکه خیلی وقتا نفهمی  چی داره پشت صحنه اتفاق می‌افته. یه operator ساده می‌نویسی، و یه magic method جادویی صدا زده می‌شه که اصلاً معلوم نیست کجاست. وقتی می‌خوای دیباگ کنی، باید بری دنبال این متدهای مخفی قبیله‌ی برگ(!) بگردی. و کلاً خیلی implicit و غیرشفافه.
دوم اینکه اینترپرتری یا مفسریه. یعنی خط به خط اجرا می‌شه. تا نرسه به خط ۲۰۰، نمی‌فهمی اون خط مشکل داره. باید کل برنامه رو ران کنی تا به اون خط برسه و بعد بفهمی "آها، اینجا یه typo داشتم" یا "این متغیر تعریف نشده بوده". یعنی عملا یه کد بیس بالای 5 هزار خط پیرت میکنه. از اون طرف توی زبان‌های کامپایلری مثل Go یا Rust، قبل از اجرا خود compiler همه‌چیز رو چک می‌کنه و بهت می‌گه کجاش اشتباهه. همه‌ی ارورا، یک جا. ولی توی پایتون باید خودت خط به خط بری و ارورا پیدا کنی.
سوم اینکه type safety نداره. یعنی یه متغیر الان string هست، یک ساعت دیگه int می‌شه، بعدش list می‌شه. تو runtime متوجه می‌شی که "اوه، اینجا یه list بود و برنامه کرش کرد". Type hintها هم که فقط تزئینین، اجباری نیستن و موقع runtime چک نمی‌شن.
چهارم اینکه performance خیلی ضعیفه. برای یه API ساده که ترافیک بالا داشته باشه، باید چندتا سرور بزنی بره بالا. حالا همون کار رو با Go بنویسی، با یه سرور راه می‌افته.
پنجم، dependency management و packaging اش یه فاجعست. pip، virtualenv، conda، poetry، pipenv... هرکس یه سازی میزنه برا خودش و شما باید به اون ساز برقصی. requirements.txt هم که دچار conflict میشه خیلی وقتا. Python 2 هم هنوز توی یه سری از پروژه‌ها هست که تبدیل کردنش بدبختیه.
خلاصه اینکه پایتون برای scriptهای کوچیک و زمینه‌ی هوش مصنوعی و ماشین لرنینگ خوبه، ولی برای production backend واقعاً اعصاب خورد ‌کنه. و من رفتم سراغ یه زبان compile شده که از همون اول بگه کجا اشتباه کردم، نه اینکه وسط شب production کرش کنه. مثل گولنگ یا حداقل حداقل تایپ‌اسکریپت.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3134" target="_blank">📅 16:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3133" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3128" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q44Ld-Z6r4KT9D_L0mZHRS2sWxxYDL6EQ076C7Qj7UaepCwyCkaBpKvAD6RiD6Wf9quoWGqYja6VpD_Cu3d0J_o-LHvfxGzCM-QjlZy16zTzjhhkBxBJ9RiM21tJ-Y5PwSiYkBF8p2h9udKMNtz0KFi6f4lkyEGVrIxAfdApbFm2u0RbBjc6yiE2Yh0SxjjTOpx73Y27_3-JdUvhHHX4mtKaREV3tl8qys9ZJ0BUizvweBZJ5SRrpQF6q1h3XAVrGU6WQrLwmS_gojfVbvr3M6Und6J9HIR9FlHRMzGo-SZvZnmMm2NOpdy_ZBj8HWBZEVwMFL7q-15XcqEmhYyGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان. مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.  هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3127" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با گوشی هم میتونید باز کنید دیگه اون Index رو
یکی توییتر پرسیده بودش</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3126" target="_blank">📅 12:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه چیز جالب توجهی پیدا کردم که راجبش ویدئو بسازم. به درد خیلیا میخوره
ترکیب یه متد حال حاضر هست، با یه سایتی که اصلا هیچکس نمیشناسه. انقدر گشتم که پیدا کردم
برای VPN نیستش. برای دسترسی رایگان به محتوای یوتوبه
سر کار هستم الان، تموم که شدم واستون ویدئوش رو میگیرم</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3125" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OG_4DgMbgBfBE6sWyUuJ48_ndZdKG1-_ETS91fczE-3U5pMecu2N4gr4-PsnwRPtl_xJtsg9LlmahqeF1NCn59-qL54aC4gMX9Dngu4DBMafGiAr3ruJaQeWcgyUgqp9LBtnfr2_AAlMkhpLHniXYNLR3gZRWCgcdWxL7WTb5haYR6uz9hFPQGI0Vdwy7Kaz8k9DknpTCqcyC8LwCa4hciTSluYZLeHOZAlNvD571O0r0aXsDDSysY_RVywe_umLXBQBqV_YR8AFrknqqDloS_1lkAfjraVsIzE_ZRVd94GRf-Adk8p2fzZJ8qpsoMQsmPbZSWX4fhpMSv1xYoq4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LD_dtSodoSESRPctlBIDXWKYg87FPj0u78C3HNN_UgHWz8nB6VKBJb3uftsCjEXb3CMSYLXqU_2_DNrftTwuSIb_KmPKSRaoYjyXcU0yHb5fISXB9LrSE75ujh1ninegwp-scR6-5-gKOlKAobRBKcu-yJzOXAnLnbiu4jG8s2h2WmPI-oBFxvFHu2VgxxSbsnUk770sUSnVa5j5Z8Z2gjDwbRrJ2DB5OuY8OtNJl7FZ0LF9hMegxtZ1Pj3_vHyZ6WHTgf0ONlIBfAEXFMHvSQd22oEQCM--F46vPZ4g3rzcs3nVeyj99Xu_CjrmZmEFRJv5oVEe4AaVPNsetpngzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فایل رو روی سیستم Extract کنید و بعدش راست کلیک کنید روی index.html و Open with chrome رو بزنید</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3123" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cdn-ip-finder-main.zip</div>
  <div class="tg-doc-extra">723 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3122" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3122" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fle2obtsP6JjOfJ-QZx4Htni99J49wOj1isKwVPPRDH26R6nckE3tHuGLpJezcrrojfjUSljTJopFLrf-OZa65g-MfTrdTZscKcrLvHHEmaKOAo5rX3Ae1czNBIWCQcscq_WRzgk2YZLTKlBm6liQMNoHGXYF-DPB7rFzT6umls9Pk6hqEIFuL9rdmjQDA0s405Ffz6Bg_3F02v5WIjuQc8FN3yiP9p2HdMR8H1_0A5McrttfRkpRb_NhspUiQe_bs_tj0EhLSvOQBzgz42ThD9T8-h9GmKH9rNg8e53k_-_s6bf3lKLHFt2HPewf5hIIK8zsWPBkHLZhNMgAKHjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر اسکنری که دیروز توی کانال قرار داده شده بود رو برداشته، و توسعه‌اش داده و تبدیلش کرده به یه اسکنر پر و پیمون تر. این هم پروژه‌اش هست:
https://github.com/hossein8360/cdn-ip-finder</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3121" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایرانسل:
95.100.69.108
104.83.5.203
92.122.166.146
104.66.70.133
104.121.0.17
104.83.5.65
92.122.166.168
104.83.5.82
92.123.104.67
104.110.191.57
92.123.104.7
104.109.250.232
96.16.122.74
23.40.63.69
23.73.2.161
138.201.54.122
144.76.1.88
94.130.33.41
95.216.69.37
185.137.25.214
94.130.70.160
94.130.50.12
37.255.133.30
104.81.104.13
92.122.73.138
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
92.122.166.141
104.83.5.216
172.237.127.6
104.81.108.10
23.73.2.148
81.91.145.2
65.109.34.234
81.12.72.218
185.143.232.122
96.16.122.66
88.221.168.138
92.122.166.175
96.16.122.82
96.17.207.149
96.17.207.151
23.220.113.51
5.160.13.85
142.54.178.211
63.141.252.203
96.17.207.135
2.23.168.144
2.23.168.254
2.23.168.250
2.23.168.96
2.21.239.29
184.86.103.210
23.36.162.202
95.101.29.30
2.23.170.80
185.200.232.16
2.16.245.188
95.101.23.82
185.200.232.34
184.28.230.87
2.16.19.136
2.23.168.174
50.7.5.83
2.23.168.47</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3120" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plQUwuPTBCLAuUhiySyMqxXjpGkEUPyL0DChPO_Vk6SlvQnproV3O5sQ_Oe8YW9kRI68k-t1Zb3daOPOol8J0fsa6xGN1V_k4BYa27r6O10cZHYUDc87mW3drdR5PCSwxWI-qEbJ5aHdIr7dsSMg5SCcWarvXpjSSyb7sgmScGn9NXE_vj1NPOHHSe2EpbPQPNeG4y2TmYtAqgvUpFhy5CgnG0LYFK4Ttqg72KsYr5j-fw8GAgMzWtyXDfALa_5vpjQJ3MiTPAawK7pjawUvczusH9uEp4BOmBcxCilCEbEHq41OFf0lukUKUvWoy1kQfe-P__hjxi07e6JjNdWgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینطور تغییر APN به
google.com
رو هم امتحان کنید. گویا روی ایرانسل بیشتر جوابگو بوده. من خودم روی همراه اول فقط با همون لیست آیپی‌هایی که دیروز گذاشتم وصلم به شیر و خورشید</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3119" target="_blank">📅 10:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یکی از دوستان این نکته رو گفته بودش در مورد وارد کردن آیپی‌ها:
من چندین دفعه هم با سامسونگ هم شیائومی تو برنامه مهسا‌ان‌جی امتحان کردم
و یه چیزی فهمیدم که خیلی عجیب بود اما درست بود.
هنگامی که آی‌پی ها رو پس از اسکن، کپی می‌کنید که داخل برنامه وارد کنید حتما باید آی‌پی ها هرکدوم یک خط رو جداگونه داشته باشن
اینجوری مثلا
20.68.81.211
20.63.74.811
و اگه جداگونه نباشن و مثلا اینجوری کنار هم وارد بشن
23.96.52.41
86.52.17.76
و...
برای من متصل نمیشن و این رو امشب فهمیدم و با برنامه MahsaNG از سر کنجکاوی امتحانش کردم و در کمال ناباوری جواب داد و متصل شد الانم دارم آپدیتای گوشیمو انجام میدم.
و برای این که بدون زحمت خاصی جدا جدا هرکدوم یک خط رو در بر بگیرن، پس از اسکن کپی کردم، تو تلگرام ارسال کردم و از تلگرام کپی کردم و تو برنامه وارد کردم و درست شد.</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3118" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQulPWcq4Llw1JRi4E8vnUAg8Ce0lkm6Cp6jCcE_fsKSEeINt_30jgKI4eFC6-iak-PqYe7HNg7HqwZ9nK7TI0wpdOm18Cw4FpJxC3Ve6H9PFUeIn4tl7HRFJHQ2Hvy28bVWHtbD3iqguyMDsOQMjq1OR7JvzPIu9fCTTQ2sqIToGO2YOqXH__Zm8Upg5685V2QfvFx_bN3tg5KBivxTGTpqGr-25RY6rAB1QqhUnWVTdAaG2JGEpgqHK0vcHUUwAuoC4Odgv7Tm0OO_xcu1e9Wf2vPLv_crmivn75XTXud-SwNPgSRK07JeHwhkpoEF55TSI0ur65_m7PrII0EtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9e2Ktsgkfz9IYNMrZ1rTvZ1-aayEdDYU2-FqrKLgco0iQ3mAzSo9T2JGiKr0hqPFHifLFo2wAi47Tl8Agnyt8MkRL7BYKAtC9Gr9hU4cBoiPIDqRV2NjlIycRU7qyq1TljsXiw6-c3eX1VVoF8LcZe6GCM_gm0TnCa0tK59RBLZXSBHveY3O9lUyRx0ftpQ0-T0DJIpgCDmpx4_Jn6YRAE8AzhUXtZS6Kl5zrknRvwvNQPBdJTE0IDvSqXtF7wYsDJu21Na66U_9y7tnNeiqCAT3j9nZvgSwJhkh1uEydXgJEkNBu-KAOVOsmGKWaEZ2VhJ901lFlWoP2vYsq8eNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
