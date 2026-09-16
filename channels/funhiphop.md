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
<img src="https://cdn4.telesco.pe/file/J-t9bJpmSx3B2bof_IF6KZ8w2f9o7kcZnmcO3vKYGFT5HEBt6RAEf3Jb8e47fR2EAISNVKSE2cYdzS_O_9brXAWM72PH-6ItyZZ-tFZfB6ents7nEY8Ae_ba2jEVgCZUHetaj7ySqoL1T_Gc4ME78EzIgrhJ5m2ec6hdkoZqPTFYst1wVt9bEc3c4j7GOb1JzuMIOI4W-izcskadf9CTlFSgiWmq87MwaPQXzkTY9Rm8v9mKSEx--68y24T0QjSkVJH7vFU3WCtY7BQKC5cl_BIU5TL980SHAfNJrPJWEAXtxuRl2JMzRqzgBK-FtpFxnb6b8DwXvp0LoDXeocjokw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 240K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اون موقع هایی که آداما ترائوره به خودش روغن میمالید میومد تو زمین باید دنیا متوقف میشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/83573" target="_blank">📅 22:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اقا اول تست کن بعد خرید کن!
گیگی فقط 3 هزار کانفیگ پر سرعت
🫆
شارژ حساب کمتر ۱ دقیقه
✅
@NetingVpnBot
@NetingVpnBot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/83572" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه (پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/83571" target="_blank">📅 21:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه
(پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/83570" target="_blank">📅 21:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینا مگه تا یه ساعت پیش به هم ناموسی نمی‌دادن؟
چرا الان دارن با هم رفیق می‌شن؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/83569" target="_blank">📅 21:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پوتک پری روز گفت من جواب دیس آرتا رو نمیدم کوروش دیس بده جواب میدم
واکنش وانتونز چی بود؟ این حرفو قبول کردن و کوروش رو اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/funhiphop/83568" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پدر عجب چیزی داده</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/83567" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حاجی تهه ویس ببینید چجوری با خجالت کیرو میگه</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/83566" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از بیف تلخون و پارسالیپ رسیدیم به بیف این دو تا یتیمچه
عجب پسرفتی کردیم پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83565" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آرتا درمورد رابطه پوتک و نسل چهار و خلسه:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83564" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حاجی این بدبخت اعتماد به نفس درگیری نداره، تو ویس فحش میده با خجالت فحش میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83563" target="_blank">📅 19:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83561" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/83560" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stnYS5R1UvXBa_-EyWAe1f7ofArgQWc4XnYe2oBULaMMbsuG_NT7LYe5pqe_84qtElDytmCtBEG2AW1KR_m7oNVC1Zol2eIFmeUOO5IaSbfE3O0H3NYE261Iz-b1J7jz6-7YTu-XEHxnA5BKEQise4Wy8Smljj1RlBXdrzlqg9JMFxAl97Lbg0doNpgQOkvavaeksspRhn69_QSSOJeTcm1oKeNka7M91_byekiDrIhSzWRSXXuBByMd1Q8snWem4wCoYcOyy32MraphnOXMOGh-Y7VI3D4DM3aouo3VZYQTJfL3RlXTffhZkkubuLFihp0oFMZkInMQWvPfmVxovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یکیتون این بیفو گردن بگیره یا آرتا کص میگه یا کوروش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83559" target="_blank">📅 19:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97Q3Um2is8P8l2gv4sezJm1qk0CEjClUxU-i6csM1rcaiuhXdFRT9uFwjmsIVS9Eu4TU-SpW9CQaw4ysHrx4OayPOoTqIIex-uQKx3oZQHGJjm8kjCqueTlWqrJj0_I1ctGJH92pbcsiKLmYK8OCDqlpNKHQovDJEsu_Ak9WQ4VFcifnZWn2TqszSbhjeWsKRbrnvvyew6Yqx8j_hGuXiVS_2HtRvgBtj6FP5nGQKetecjSNSku5Qmy7YF0TlgDiSuxX2HOLmV-uTv_BjhpPSTF3dO5UmACFUZqAumCdDoWIpucLiSGI_lsq4clToIQje69hB5J5bx-F0uZwdMYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک فردا قراره دیس‌بک بده به وانتونز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/83558" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/83557" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4SO6ixubzIh1D9wjb4HdRN7-1deizRb3gw9WULyyehA5D0hHqdzX1WgBjJ6udJeIhSmJCoygfBGECKGNI8ay23rlpI6TaQlaprkL3oYWzPbV0oUGnOZYjfcqY2qm5I25pzYUayi6cdnkoIyQGVIbexuOsbqT6AectdXtdouUNtHvrgEncqHhaHOy7s_qNPh2wihDwpsGQKmH_ba6FLyLs6FmtmBPe-L_U_BrvjzO10UXd0yBk9QNq26KXbLJmjMtXO6TC3sX-YdTDWDztDuCpiqe-GxrGVJ1UwQwK3e6GPsSCJf3E9SOqe8SqAb--L5xbKx5UguR8XcQvw9HEUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
25g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/83556" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمایت از هیچکس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/83555" target="_blank">📅 19:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آرتا و پوتک یه لحظه متوقف شید پدر ترک داده</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/83554" target="_blank">📅 18:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek2Gu3M57__aZx5aCDZfCI-hcP8lSGP6RHz4FVVbRTUCT0U6JXPGZ2mmCdwPfL2Mx8LhNFSSXIehclqn5_Pu1NyBVxsAvPgcjG3DviDseiJvJ6LisQ5rkLtP609dPgrdr5U9ey87vZ6TqiLwX6DQntsZcbhclnXoQ4F2G7owVX0ZeREcGoYmzrKOODZ5DETnu89RuBcYbJhK6e6dSWumCSp2xTKyqItmkpe_fzyzKkF_2yQb6cTFaB30NA7XHE6SEECv6KRorfXuTX4j6p1CpYvCnUEzeQo9iz93aH7kwmiHuJCGuw2MqZvA37JoATKBZVsZQZpafegTMZQefW3DJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=gd_us1m07qpUfOdZ6XXxOzOZbjUtM2qqJ7_aQwbldBFrcZg7tseH6EmmOMWsOmcTk4YLvqNibCmiOdw9tciiHGSp2MzfCIerRulxmcOgMRAxVxyObco5qTbZksnx1TMhinm25i5U371tczq_5y-U5GMC04srB-kBFeh6rqImc_LKa22SB-Y8uRKoIljC--0D-meUYZPErX2K5d1jPEPjlaO_toqT3mikptHxRHVioqFBYq8x6jtEe9lYKAqHbEtZd4IIz_jS7CjF4IWCMp2MxVRWHyDzB7M4HJETA-RZuCs2kXRjQt7vebtTN-IPMHy6MEGoL-9yXeC3zh1bsPJKwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=gd_us1m07qpUfOdZ6XXxOzOZbjUtM2qqJ7_aQwbldBFrcZg7tseH6EmmOMWsOmcTk4YLvqNibCmiOdw9tciiHGSp2MzfCIerRulxmcOgMRAxVxyObco5qTbZksnx1TMhinm25i5U371tczq_5y-U5GMC04srB-kBFeh6rqImc_LKa22SB-Y8uRKoIljC--0D-meUYZPErX2K5d1jPEPjlaO_toqT3mikptHxRHVioqFBYq8x6jtEe9lYKAqHbEtZd4IIz_jS7CjF4IWCMp2MxVRWHyDzB7M4HJETA-RZuCs2kXRjQt7vebtTN-IPMHy6MEGoL-9yXeC3zh1bsPJKwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83551" target="_blank">📅 18:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مستی ناگهانی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83550" target="_blank">📅 18:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83549" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83548" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgThwsGRS2IzyWIBDeykW8zi7Rgw9FYZhuuamqcJxg-MD09A8U-dAkA2D1hrV-3T_DhwsnyVIU0zM5dTEUAidSrHjThoXf5VTewZwAj_oKpsPSnCe_ADduJYp01ysH-q8wMvXXz-OJJAnjk-Wtu-cfbLS6RAYL_URdWwlZGUSCTeyQmJFASzknFU7R4BYUZg3b_foCTG7IUdeKs1dk_hXP80oIwDKzeyCHCR3B2D1_SmAfdJ9zH5K9AsCskpPN9rNs-BhR4fcOrRtGMtPWo5rTbSm8pH8Peo3pspQ8ozLuvqPAy9qEAC7_TEmx_gC6BhfpF_1tfSG8eBVpYP_bCrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83547" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بسه دیگه گاییدید پوتکو
کوروش 7 دقیقه دیس داده بهش
😂</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83546" target="_blank">📅 17:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhY09B0uw_kv4nRQrz-S4gypKS-AxjQ_JSzh4Xe2xbzB56L6AULbDsVOfTr7IPV4wlDYxz1oN3hnm4JFqb_3Ve6BCsL_DLjnoZ1xVyRhhXV0pxF6Q8dMop2FTyw81UE3g3KOE5ZggrwE80ZeMTBg_fRxmnBo-gOeBIBYdfjnBz5Yera5z_zbSl5QGcG6sXSCw8QVLqAsCnaL_9FThQ-MlRQiQX_uRhES_Hfp1HblXBrIMj2jHKcOnTsketuM_D9i6HDQfejAPNNxIuXQ671CWgMxNa1g1UD1hlL6AypIEvgRYxN5_gNt2WKHrreGnAYvQMnUUguY4RqWv8q93FEs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کی این تبلیغو انداخته رو چنل حلالش باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83545" target="_blank">📅 16:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به بلایی که خط حمله بارسا میخواد سر این دفاع های رئال بیاره فکر میکنم، تنو بدنم میلرزه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83544" target="_blank">📅 15:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پولدار شدی ایرانی
کالابرگ قراره ۳۰۰ هزارتومن بیشتر بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83541" target="_blank">📅 13:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa__aaEuwC1QZo7vDwBvfXGw9NKF4rHuep9RbUWWbcTHDC8yfXu9aZyubCt98EvO_wnMLb3g6__MprWI2iH2WDgslkVSvekg8QCtnih_rKRKvmnWRyuzqt192WOTg_Z6AbdxMGnuY0xE-jmmXTbG4Vb832pQ8O-V33IHByLwCkEAIL764BlccYrS4PUdQcK00n6PwPaiInXb0Ptl71ZfDrsny7laz7CagT7ryL2Mn3MYe6lcTPgnon2Inf3db4qcWKYTTo6m4AMBiI1IGY-ah210xM3npDyJqyirC1nJJrIrhr-ADji-legnP9MsN8sqbrU6IJhF0eAkKuena3balA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی منتظرم ببینم کصکش نبودنشو چطوری قراره ثابت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83540" target="_blank">📅 13:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEdxh7DKAa8GMgfVM4DZL6tHbO-Um-FcYUwv2bBhb5yIdLo5j4HWDl8Zf3mPJFTJYODR0BNvzUVT6NjcDDLF5HzTarpgiph5zL5kXLilG0ccCYmkj8XZYiDZj548iXS3QgpKWZrFhLfjcaInK8mu6wgsRrgdDF8PAkvp4LBeypNwbgTADpciBBwKYvDvJvGWEZJuC3alARQ2kjBs4BdoQKmQR6ywpHBfKk9JPNl0PV4_A4XMpzSsqwznJA8uJrG-HxAfQRKdLPeld0pLGcDeNVH9cuUTglzGruVGutCrkv55lNEmy5EDHD9vilefn-vIS-SoZgmym10sDDzITDxMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک الان در همچین شرایطی با آرتا قرار داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83539" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spinner</div>
  <div class="tg-doc-extra">KVIRO</div>
</div>
<a href="https://t.me/funhiphop/83538" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83538" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGzoP1p_PvieU4WtTBlAPVk0rdwTi-0DUQ-9IY8U5rqqZU33lX0DrlFHS7PREiVn93hXPUEjXEptA4Oybp3EwRtIhbCbM_EMPrHVZwmEU1IFQpb7ncUfXOxIROg-XcNJDE3DaNFvBLc2rTrEGQCHCio6UxqkE21YKlV8gz0C-LAoZh3HrSnPA_jaxSy4KRz5lUsCtOW2CAun76nhD8ILlOJmIyxtQdd7gFqZBAgCzO_-00BhKlYA0ddXSsD7QUZ0gFvdjSnMabEEmadNDC9W2RxeIXNZXDyTjfmB0BeO_Mp862YuuggbOSA7ql-qC7u62yZA3XqBMjWNnM5xuDAxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "کای‌رو" به نام "Spinner" منتشر شد
SoundCloud</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83537" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83536" target="_blank">📅 12:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfGGuRz3PsxxebeqEoYg4KON2kPwECsMmKKQrXPT2oMyHYCFOHq9688Dp4wfxjhCPZLtBF5yHR7H5IqmZ1EjsRQtZdnfqcl3m7pc4BfoBEVRQE6K7M-uUDSf5SKczYApoGa2SfXUvKPWxqD5t0UiyAMvnY7l8fzKlSSxqEIz9Zf93EzjNasjHdsdy7xQ8PCftMR-5aE3G6SC9CLIv0UQ9QtNdGP_qyokwWU4Hw9jIhVtye7tYOGB3Otdr6fMia30T7iJ8baa-oMX1gpP-9JYUzXAlJj8WhoXqYqEDRjEUU4YATbKQdmtF78I4lS2MpKsP2LHk8IBmoi0jeB7dwHjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83535" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83534" target="_blank">📅 11:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83533" target="_blank">📅 10:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTsy4MD-q3k2eg_BljQ_9P2DCdXTTqZgdshkVAPep4hCB6ERxZz8MtSw7Gn85fJpJN2_jELQX4LpihXsJW-8g1zYI8gDdcwgKEl8JSPbyoQv6vRQpns-M14QmisaFmYYqIAcGHhuavPl-0xv7FStC0bY4MFTalMby_b2c0cklrqnQOvtZmQwqkhUMc9uy_YEs5iRpkKMIc7LLX6TolQsCJkjWVFPbXRsrLVWHPpFKtqMhKBKtH4kONeig28CFUoUMDXS7Sv2VNBw4gBqCTg5z-RXVXXZFJTxhG-nDPiwf0vlSKF-9eOtqmcfs8pCox3utpY-Ggld4BwWQ4mYdppfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرینج بازیو بس کنید ندید پدیدا بعد از سال ها یکی دیستون کرد حالا گاییدید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83532" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با من از صبر صحبت نکن من برا هر شوت سوباسا ۵ هفته صبر میکردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83531" target="_blank">📅 10:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4HoVoTq9iIj6jlRIU1eibFM9qSyhqn58KEOlwUtKppFl9VYXoaKYHL0x2g6L_X27-tGDABHUXd5Bl04qHUg8j8lve0KN8PJzaQihVQxNv6fTrFR6Y_flKCVx9BJUIlxK3obCdHOW8j7WDl--eui0C5afXC1bYV9Hm3xiu5OZVF3RONox3gSMWaLYfL4SFOjUjUBDvO0efAvNzNCvfHmzUCOPWzpcEBdrpf4pnpfdm2mj0Wm9mlPdwRkBWsQb4CV8Vp05ewT08wbX6cijj8PR3QCTm4WZ8i36y2k0mc9r4qT6FR9vJyCPk85Xr16ac8uE01Yd8zdQ5IJ0_uSi3gUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkAxAl0HiLi_OLt1QWrbVb4qHn6IC5rdxhesxcLMSzMx9bhAEXVDJTB2QjJrJZ8StZqhAZ_OZFOYqsO8NVZhi5fyWb-nYjUsa1kph0-hV6CCAbZXg-IsjaqErJVt_LwQ-Fv2WZxlqDEOE6swPK5iyd1cBT6Gr9aJZIFxAfS1PQPE_JZl_ZggueomqnwHwAXx08HS1Y44pKqb64HesXcWk0SCYNcEPZVKe64-Ngsb8v9PwuRNxLSJUl-z-8ajoBfhon2hgwalxANH7NpP26vZxxuq6wdajPr7gx633OGboUEbeUcEdCkHEaqzTeBWiSBukOqderXBxnNIFNBVu76LzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKhEzsd63l390sKFHmPec4fIn1oa9lwnbGsTOr21ll0BOvuvr-HupOhqF1sao7ddh_XxO8a50EeVLrDplZH_lxBp4j893EOCxSA3gMS-U00JBrAWW2s7i23qu73nJ7OZJJzADMRUKdVxadnqrvyyclJOjaBYouEC4O4gPq58VEdyPaJIFtriSLC2fJKVCOdcK8xkHscAU3tDMTpeXHvVsRLAJW_EI9jhZkHkKomQmtyG5wAQjcsrNgyJwZhJldyDOjEa53tIbYya1Kk0CoxwB4JgeFMxGTuVm6spkjwzxoc4Pnl6dVTMWRrBcaVOHi89ktUyEDx4YKIs1PjU22vrEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید شکیرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83528" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3OWrp0ysCUX-5pZ6EoYr9f9hq1h9Gheh6z8Tve2BxnzBgLbx4MXEbeQ4MurmwumliotM2mMeTv19gIzH1ytAk02_odmS_VVO69pUkAgJYBON-Z_YCS4W_I0DZk1ora-r5Mbv_jLebTCbdQAEOuFilyjg9EwuI58gc6_uopKPfS_Y20g6iFm_3LNoGxJ-ziXK0_puyeQsOHBXDFvl4V1dUpbNyEZfxiM2D7jzFdS8PLWnRWOM36dGzOzd1Q1nZATP8WmnIjm5C1Xw5rsmpDvd6PtwaGXw339Yi9sDOt-ASXcnyX6cXYEYS2TvaqYb3Xywfryw8TnIrLn0CFa_s9DDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اتلتیکو مادرید - اوساسونا
⏰
ساعت ۲۰:۳۰
🌎
📲
لوانته - اتلتیک بیلبائو
😀
ساعت ۲۳:۰۰
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
R25
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83527" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این قیمتا هودی، سویشرت و دورس جدیه؟ یا دارن شوخی ای چیزی میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83526" target="_blank">📅 08:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ددی آرتا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83525" target="_blank">📅 07:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ببینید دوستان بیف تو رپ طبیعیه، حالا یا ایکس(وانتونز) یا ایگرگ(پوتک) میزنه ولی تقسیم(کچی بیتز) حرومزاده اس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83523" target="_blank">📅 06:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لاشی دو دقیقه دیس داده ۱ دقیقه و ۵۰ ثانیه اش رو داره حرف میزنه ۱۰ ثانیه هم خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83522" target="_blank">📅 05:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83521" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo5NZ0CGi0J6lrzuzqgXVo_5quzEJPmGkY09Gi-hEefpt4tQKizAHxCNga-R89LVR6tZI_HjwLOUITtBTWZXYRGxzW5jcYdbveyhkKBGjtHvCj27kEFghHhCDKnE2QHM9dqVmSA29-NHP5KY1KQusC03sEdjpgX7DROOPUVgGf7pDGu8ZQUMWX0JHUji5qv-DO5AL3gspYettVelUZUFre-GIOcmV3N5XbR_P7GjmOW-VsLNIBdCMguxA3yCgKjzt9ylWLemuaRYYwxvAQCL0k738qK7DZ7JyjmCizCA2L202j2WPgN3WiN95IrojyBdR6CRSE7T2L7C8pnPwIpvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83520" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgBqdxGqrvMqWhC3zXETJxqfawO8ArA0sjfKjr5_Op0D2jkvarcuxsxhVITu94V3Vy0Kts6QyaBjHaARCxniRdIIDuZtTJoZ0RlY7nS_WYy5783ehfn_S-YuAjl3Ui7Wy7Butku9rPJckb7usjWokQeelTaQ9_Jnx-P_emdcQqdtqNst8CFbcmrpSSVOcGsvG6Nquvb6zBJzvo1ygUd9sVfdRgzlrYECcAGb1-xSEvl8aKhNu14aup7N771bnnYwm-4FW4fQIGciM080hzPV8uCy0XNQi8iQV7JZG8ZEtp5KCCs7n9bJlgWrPDEj1h4QFTIKwhWeM4-ru7FKxL8lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری و ویناک رفتن تو جلد آرتا، جواب دیس قبلی رو نگرفته میخواد بعدیو بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83519" target="_blank">📅 05:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=VqkGktvqdS2V2QaOAUUTYAdnqDRSWIaNiYBoxQr2xB18KAhCyapZGD02T39-CLO8Z3LR4nNzeHjqhww74cQ4gLlegJakQSeFaLfMS8Qt1ZHl7MMe2nBNnrTYk3rFZn6Jnhr6dEH97cRWLxt8RRiA7xRlyzpMte-KKIsb839caWmJjfSMlSa4CoC3imd77VX4VSjMEC0hofgp0InI9L9bQo09UP27ENl3hAI6ZXNGmQKD9AW1qYilqlCptRETdVpsdVcsxXrEgOBXTw_jf5_rlMJNfhVGDdqpqZMKjN4mxyP496S7eR_XdiJJGmDXBUMeWYBZbd1mOYjgzQZ_JkaTHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=VqkGktvqdS2V2QaOAUUTYAdnqDRSWIaNiYBoxQr2xB18KAhCyapZGD02T39-CLO8Z3LR4nNzeHjqhww74cQ4gLlegJakQSeFaLfMS8Qt1ZHl7MMe2nBNnrTYk3rFZn6Jnhr6dEH97cRWLxt8RRiA7xRlyzpMte-KKIsb839caWmJjfSMlSa4CoC3imd77VX4VSjMEC0hofgp0InI9L9bQo09UP27ENl3hAI6ZXNGmQKD9AW1qYilqlCptRETdVpsdVcsxXrEgOBXTw_jf5_rlMJNfhVGDdqpqZMKjN4mxyP496S7eR_XdiJJGmDXBUMeWYBZbd1mOYjgzQZ_JkaTHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو قدیمی‌ای که آرتا میرحسینی از پوریا عرب بازنشر کرده و ویس‌های جدیدش خطاب به وی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83517" target="_blank">📅 04:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جنگنده های اسرائیلی امروز چندین بار تمرین‌های شبیه‌سازی‌شده‌ای را بر فراز ایران انجام دادند، و در برخی مواقع حتی وارد فضای هوایی شمال غربی ایران شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83516" target="_blank">📅 02:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmiZ8YKeYdE8wbddu3joQltm_B2JezAyFrt5zYxvSauH74d4j5MOwIXKJTNAVeGfsU4r8yLI2-cn8BIdfFEVlh_kNdPzIikmsrkpRzzXsUhrgbBi1Z4c-AzJ39Z37Cmy9poe9QA7w0KrkjiQktFa7b1HBV8drej7Zx2Ag3jJw_gcoMAr_6wlN2RS1P-_-rOHdNPzSMJMvVTY1jCfgdMUMS3uD-a44M0sL60UbE1YxLRJo5I2vCL9lJ23XJuHcu4jR53x2Pdn8Mc__RDFm1e2bo0oh55rvzWjt-Dwrj_7xLfWpOpoof2mXFHNQTzgMQgQJk7tDiMajnqRwycrWKYaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد رپرایی که تو این کنسرت حسین تی ام، بیگ شگی، تیم بکس و... حضور داشتن بیشتر از شنونده هاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83515" target="_blank">📅 02:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسام سهرابی بلاگر شده و ۸۱۹۲۹۹۱ بار از جاهایی که کونش گذاشتن ریلز طنز دراورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83514" target="_blank">📅 01:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، ۷ گل زده اش تو بازی هم حتی ضریب خوبی نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83513" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز:
🔴
1.49
🟢
1.78
🔴
2
🟢
2
🟢
1.8
🟢
1.34
🟢
3.89
🟢
1.67
🟢
1.44
🟢
1.35
🟢
1.4
🟢
1.6
🔴
1.9
🔴
1.46
🟢
1.24
🟢
1.8
🟢
1.2
🟢
1.3
🟢
1.3
🟢
1.3
🔴
1.3
🟢
1.41
🟢
1.85
🟢
1.5
🟢
1.3
🟢
1.5
22وین
5لوز
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83512" target="_blank">📅 01:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بخواب بارسایی رئال برد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83511" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huefKTYYK54k-9kvWaZQuHKB0s7APoBT3Cip_nsVwAoHUVCvTMdFpCotjaEkajq0gENeVDw52xiuDd_LETHoz75IyEzCpC_H1fXDorNNCm55XNYO-WGZ_M3AvCNPl0wZK76AIf1FnHAaKQYd1BnypeYKMP5Hn1COGmo3FBxzGHDXDG-JUILcPuy-rnsoBPcsZpJYwqFAIPcUnXqDuhZC3TBFVAzuF7nOQi9cybLBN8h0yOzWc3cgVdqf1c0Dr0u6CGGvbh3sfbuz-E1D6AzApAcUbB7UvCWTNF7p3gaqc-itpUmfwv5ep2ztkb6kf3iVC6RaUKZTvM_7ucIcE0UbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت خداحافظی با بارساس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83510" target="_blank">📅 00:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgoDmkLJfKRUGHjQWmxoKjQp9SqTfF4DmYVXm-qwx4ys9IPv463mCLHcnRIfPZ_-oTDsd4k4-uTAXAS_pYw2lLoubV54Zib7CHeZbKgQbYTL1ELFLMY0obsXy6fJdFfePmxc9E328g9-S3pyVhKEH3xSZBJCdwUMfm3BjQoh-BGEn46JMrMecoIvDR_WHboHuIN_trtkq0GP6oRdoXWszUKaGTXvYHuW3-FEBifRnjUa1t3ZEQtenCh3Tbfi-HgdVy1n0lx6oTka2Rd0pCEF8HXJVlr4419FXiohgr3d4yCWxpWoN7pbEQV2Z5VIuolQ71bGn6bgP2wHA9vdSeAbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83509" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83508" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپشتیبانی تندر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPte-hOzhH3WhHIhsDHyJGa5T93bg7rRi_HMPgLYu8mvH8NrZHvH2SbMPs1nbdAQoqe3IzNvbFKJMdSEbagF_QgKRP8drS0QhoXljw4kyAkyOS5LR0oIeYvPipPaylgat6yfXgTpCbjuMVyuNF-DXWYqfQ5UrgNUjR3uo0qgNFY2VLmqnR7uj2hQiG4lemA_uZDwqMTEfNsrMXr8tW6uzAH542vb0HN4Q6B1NorfDLYttnOWxaueZ1LozpeHKEulVHq0sHiidgObTX_LlaSHG7ej0YqAJqoyMwwNl_k8JFpaXSFogwoFJbF1B2prVmaVZ29GsFEPkxrXHsRm6OcllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83506" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69179260d.mp4?token=jZZekMTKH20CPqBZ5HOhSYO-eLR3ECq-gGJ-l_PJnKRue2NF4Fk0Dxpub815xeaPPHdUSmozPKnJ4f8C8OKzxMgSWNqlVvIYezHZID49DMDQ1s2jHDhj5ZTScG6BmwhCcttb9XaAjN_cpJt6hasMM3F9NTD0KkgNjGjvJ7WKwtGAl_kyrsm6b8xwTQDNnOyApntRd36dToMktKe9_JmVKAnECyxVFtjyHjKz7VzrfotOB1GfRJTmS4xZQ81gQ7Drdy8aoe1JbLT3tV6HXQwQuTfr2peyNiRrGoQjpOt4btzTqbptJ9pB-tYFrLwqox1nKQICOcwe0aIwlIYQvKH_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69179260d.mp4?token=jZZekMTKH20CPqBZ5HOhSYO-eLR3ECq-gGJ-l_PJnKRue2NF4Fk0Dxpub815xeaPPHdUSmozPKnJ4f8C8OKzxMgSWNqlVvIYezHZID49DMDQ1s2jHDhj5ZTScG6BmwhCcttb9XaAjN_cpJt6hasMM3F9NTD0KkgNjGjvJ7WKwtGAl_kyrsm6b8xwTQDNnOyApntRd36dToMktKe9_JmVKAnECyxVFtjyHjKz7VzrfotOB1GfRJTmS4xZQ81gQ7Drdy8aoe1JbLT3tV6HXQwQuTfr2peyNiRrGoQjpOt4btzTqbptJ9pB-tYFrLwqox1nKQICOcwe0aIwlIYQvKH_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی ایران حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83505" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بیف اصلی شروع شد باز
تو تنگه هرمز صدای انفجار گزارش شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83504" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خدایا گوه خوردیم درگیری بین پوتکو آرتا رو پوشش دادیم بس کنید توروخدا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83503" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انقد نگید چرا بازی پرسپولیس شروع نمیشه کصنمکا
با تایم تیمای شرق آسیا بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83502" target="_blank">📅 20:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تیمای عربستانی تو لیگ قهرمانان آسیا جنده شدن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83501" target="_blank">📅 20:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpnPmIAayCLeFKU2KbqELXzkSud_mxehwTYwlD9PFP4pFonU450rkRbExbF-Md9poUasRQVBqKVMlZfE1Jatpa0fR7erFwKpPX3pINmX_3QseN-_51i0FAKe-5ZFu48pJxsK2tgcaLTPx63X3Nb1Rr3qca9z9KpwIFjqFA0_bzBUtucKh0sJemNT1IpKE05v6KvOT1arujyjrYcNRgItlqYBQHlexFIjHzPP0DT9xCSinZsuhjguK3YUMI60GaRepn8OUdhTb2pZGYeE3vR3oqQTmo9k-RdJJO3MZgv1ztsz1Y2A-gktFrOgwIyXTf5mpy0Kjc3bdchJwVYO0g02nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83500" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83499" target="_blank">📅 19:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5VG1nGocqZpuqEUBk2U8V8TXA-dJBz5Zv4NCRG-pLyAPA0R2Q2psq2ITLSwNFPOIx5r9KFBo-Ji76JtaVbdzrH8LzdtRV16F8yN6HsndJdxNOHCPKEgD8R9za6DyV3RFWN2HotNzjEaU-GM6drD-cplT27H7gS2oSxJh85xyVg1v-1zNF_JRw2l27Yd4RPzIHJmCqtDfMotz9aW4fnUqoYJfFtLLuN9iAbcAF2Ip53HX3bK3vX-2QY2ZQ9uWHv8OzA0fDu2D4qKbpylSLzREYUSMLlSekbyBv-1wUvHkIv3uWkAbMmZseL7lWl_rMtp-z-ICfKveijbIUz1HL5b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا هیچ کصخلی از دید به قیمت دلار نگاه نکرده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83498" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83497" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgEK0VITHeq-OJqSpWVqWtt6H2cOxGB96knQphogCQhIwnQFkVI3HClrgJ1Vm_XPDDTszRXadyi1nwVk-_iinNg3aPi3CUeEkdjEBeAvooMMqlsx9Js6qq0qQY6-ySck2MBvL8UjmLffaawB6zWl3qsTBvYxXuPGhojsQPd5tpkcUf95hGzAgI73Sf_oi7H29ywvikF9ElP-BIJn4Zl8bz0tj-drcEvFTxyY6B829vJn2aHOu6BR7ySozx2jOSR7vbifsX1YfCe1JB9T94mksrAGB41KxZgXARFs7WVKBpb6X5kbmudN_wfAs509JwS32pual613SpneYEapKhzEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
24g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83496" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OioLq6qIRhJYXO0At25hUvI5U-o5BjBgp57hKd-RTX6ofn96iyDUHpu7x2VjofAkHTEIlYxY1XKUMpwGmSEO4ReEo-PIepP2WRy9Q8KGB3ItQbzB8Od2zWep4sugToRl6o05_-Qv7F1kYvlXnAJYkwYKC-rMaP5Njql4AoUnitPfmr2-EpO4noS-GLdQZ7OREHXxCgNI6e0PExruWHrZtF3lbq9oUULtr40Svj7EuAOGbB-UYDcmwr48HP5B0hdSwrqSl6nN6nNffqHyGRWmJwuwV-s6-itVNrtQ2HxfDGIaKHQBVfkV0qyzJpY7O8AQjjOjMnF008zB4QVHcr-4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی که از ایران نجات پیدا کرد پرسیدن چی بهت انگیزه داد که با دست و کمر شکسته؛ ۲ کیلومتر راه بری و خودتو به بالای کوه برسونی تا نجات پیدا کنی؟! گفته تنها انگیزم بود که نمیخواستم سر از صداوسیمای ایران در بیارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83495" target="_blank">📅 17:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/959d87b013.mp4?token=TZVxnQ71lyoZYPW_mAnxj2D-Wn6gNQJDr3pgJwGevYsQwuI90bukZqQKWEFB63HWHMbyS5HqWHYSzZaboLADIrewQ7BVMyaUG_N7dp8rFRXAV_ZKlc8iWvxXBJKDo12rvGnfBp3LFgneVvcwKzSJ4umizGB-A44lU0rPWdztK9nlRpvHEJ-KaqEc1qqX0r5g0siDNx-0YgDu3GcyHbXRIr6tZE-CfU642A1Spxj_X8JS5vmwFAYs3LHuqUtjW6bMUjNThz7EiAnF9r_ul1gfVLcYKbk1s8pWL7GL6FL7qFuTJdVy1UF_itEKc7WS00lkUdtKA71mFI6S5bwdF6Nptg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/959d87b013.mp4?token=TZVxnQ71lyoZYPW_mAnxj2D-Wn6gNQJDr3pgJwGevYsQwuI90bukZqQKWEFB63HWHMbyS5HqWHYSzZaboLADIrewQ7BVMyaUG_N7dp8rFRXAV_ZKlc8iWvxXBJKDo12rvGnfBp3LFgneVvcwKzSJ4umizGB-A44lU0rPWdztK9nlRpvHEJ-KaqEc1qqX0r5g0siDNx-0YgDu3GcyHbXRIr6tZE-CfU642A1Spxj_X8JS5vmwFAYs3LHuqUtjW6bMUjNThz7EiAnF9r_ul1gfVLcYKbk1s8pWL7GL6FL7qFuTJdVy1UF_itEKc7WS00lkUdtKA71mFI6S5bwdF6Nptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیپ‌هاپولوژیست بالاخره ترک کرده.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83494" target="_blank">📅 17:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_VqBv-4EppNtrdubm4nd9li_4DNoLbIRmRruAFDCfKcXNe8fVGuiJykkkGEMX2e3ha3ZJ-T6g0bzgCv6lyWTmHx7gJVoRyDyT26hsprT-D42alIRKn6MJLDH5Pn5xmNwd7GCH4lGeT1xExeXEfzoTJl6j3sx-mnqzBQ4SS2XnXPc4nN56upy5GuOfVxCuu96PmFDUa1reWZgMqQfzrdazs9SCpnxvNpooIcv4u5geEwdvSvfDDwDMbnbPO2J_lidqS4jBSsTs0xQTBcxo3vwF2F9W1Z-MhC_zwriynepUxBm6Q03qlmCFPnS6zTjE1st4xfUxbwexvPbtYGH8AArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83493" target="_blank">📅 15:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فینال سی ال ۲۰۲۹ قراره تو نیوکمپ برگزار بشه و بلاخره بعد چندین سال بارسایی ها قراره جام رو ببینن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83492" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خداروشکر حداقل وسط این همه بدبختی طرفدار دنیای کشتی‌کج نیستم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83491" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqqkkucc-wnieaNANbx-q0GAhbfut5JF420ZFtPwl4rjxdEjxsGAqZPs2HW3yK8cKeDNAcoTi7P4xMMSB82YIs7bcWNw8oUQOqC9cU5roXEcomiLnVQpaS20MIAF-52da1ZjkBw5U5MLFzPfkpnnbL4HnDpK_EUJWJcUEjy5wBazPOb27ZGLSXnLWgKTYlGwRwBmjJfDkyWdt31kDuCq60-wLbhxXja-rWZN677QwTWf8N8pOgSwYuymKuGbulsNVHvAWWN8ncss3-r21xaN5p9Rrxi5Naz5QIglaK37v_mu9i6W_-GiiJDoSYIg5t0qts1RqA7VAcys7ajezOwfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادش بخیر دهه هشتاد حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83489" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هشدار شلیک موشک تو مکه به صدا درومده، فکر کنم حوثی ها یادشون رفته خودشونم مسلمونن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83488" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قشنگ دارن زمینه سازی میکنن بزنن بعد بندازن گردن هوش مصنوعی
ایلان ماسک درباره هوش مصنوعی: «اگر هوش مصنوعی بتواند کنترل سامانه‌های نظامی را در دست بگیرد و مثلاً یک سلاح هسته‌ای پرتاب کند… این اتفاق بدی خواهد بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83487" target="_blank">📅 12:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2FwQW3xXBtJk1G19A64ezSGCFL3P7h0Z6F8BJlv1umpABMSewGHhqRiOD6LIT6kRogree_9s2omIJ38MUH55IsalwP3Scihx53srehtSwEq6bP5CawIjB020H9GoSJe_EPlQhgzA0M6KncWUzn0AnKO990AhvEL0VMl6BZP9mu-9hAiD6pLFsXQVUd1aDnttnlieusms-fHQJ7Wmb7o0LvgLQmZKjstz5OOs6y9xyRyaA4mmS2-aFsebxMSzx2Lbfd34fOUjD64vgmt_PEqt6pzYpY9JIO_lqSCkvbULcwuHtlFCMJzbfMh2iea_Fm6RxEtDgxFVyqf8heSN8ZMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک اگه ۱ میلیارد پول داشته باشید تو حسابتون بهتون کارت سفید میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83486" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83485" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa6xo5zV6nWDgvcFL5ShOw05XQ-XgUjXs8p1ktP5F8qa9A6tMezHEojTuXH_3odjieEXj7Ze2vBlA_57ONLWo9h-ReZVphK2_eMyTle30HMCIeoTVRAZtz0LefDsh1tp_uLSRd9Ic6ogSOhHYrL12v3L4UeGPMw24n6y5L8ZVJ7MOQ45MAZuFV1obDVLdpTnKgavYFlRAB8TtxHPN6eyfN1uxqoki_faj8NXVaFPW9TGCP0AoSoPTgWy09pQc2PcPsrzDYKPTzCtg9OVAWnWAa3F1Ul28TZIhp8ZsfDjc0WnNcyRJ-RckJD0w7kp2Xzh-XBOV4K4z-ZCbyGMdapaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
آژاکس آمستردام - ویلم دوم
⏰
ساعت ۲۱:۳۰
🌎
📲
الچه - رئال مادرید
😀
ساعت ۲۳:۰۰
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
R23
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83484" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لیست برندگان امی 2026
بهترین سریال درام
The Pitt
بهترین سریال کمدی
Widow's Bay
بهترین مینی‌سریال یا سریال آنتولوژی
DTF St. Louis
بهترین برنامه تاک‌شو / ترکیبی (Variety Series)
The Late Show With Stephen Colbert
بهترین مسابقه ریلیتی
The Traitors
بهترین فیلم تلویزیونی
Remarkably Bright Creatures
بهترین بازیگر مرد نقش اول در یک سریال درام
Noah Wyle – The Pitt
بهترین بازیگر زن نقش اول در یک سریال درام
Rhea Seehorn – Pluribus
بهترین بازیگر مرد نقش اول در یک سریال کمدی
Matthew Rhys – Widow's Bay
بهترین بازیگر زن نقش اول در یک سریال کمدی
Jean Smart – Hacks
بهترین بازیگر مرد نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Matthew Rhys – The Beast in Me
بهترین بازیگر زن نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Sally Field – Remarkably Bright Creatures
بهترین بازیگر زن نقش مکمل در یک سریال درام
Allison Janney – The Diplomat
بهترین بازیگر مرد نقش مکمل در یک سریال درام
Tom Pelphrey – Task
بهترین بازیگر زن نقش مکمل در یک سریال کمدی
Kate O'Flynn – Widow's Bay
بهترین بازیگر مرد نقش مکمل در یک سریال کمدی
Stephen Root – Widow's Bay
بهترین بازیگر زن نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
Linda Cardellini – DTF St. Louis
بهترین بازیگر مرد نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
David Harbour – DTF St. Louis
بهترین بازیگر مرد مهمان در یک سریال کمدی
Rob Reiner – The Bear
بهترین بازیگر زن مهمان در یک سریال کمدی
Betty Gilpin – Widow's Bay
بهترین بازیگر مرد مهمان در یک سریال درام
Ernest Harden, Jr. – The Pitt
بهترین بازیگر زن مهمان در یک سریال درام
Shailene Woodley – Paradise
بهترین کارگردانی یک سریال درام
Saul Metzstein – Slow Horses
بهترین کارگردانی یک سریال کمدی
Hiro Murai – Widow's Bay
بهترین کارگردانی یک مینی‌سریال یا فیلم تلویزیونی
Steve Conrad – DTF St. Louis
بهترین نویسندگی یک سریال درام
Vince Gilligan – Pluribus
بهترین نویسندگی یک سریال کمدی
Katie Dippold – Widow's Bay
بهترین نویسندگی یک مینی‌سریال یا فیلم تلویزیونی
DTF St. Louis
بهترین نویسندگی یک ویژه برنامه / سریال ترکیبی
The Late Show with Stephen Colbert
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83483" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بامداد امروز، یک فروند پهپاد پیشرفته از نوع MQ-1 توسط سامانه پدافند هوایی پیشرفته نیروی هوافضای سپاه، تحت کنترل شبکه یکپارچه پدافند هوایی کشور، شناسایی، رهگیری و در آسمان غرب تنگه هرمز منهدم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83482" target="_blank">📅 09:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=cRBQAlywo4IGI3BuOmTaCv3WtnY1fxccpygbyh8d27B-soeWqWxTvfC8sKnCi433k7sh9HI9lmKgTfU2QyLWpjwXZew7x8RmntDySSQlhfvyPMsK3QcEUjBAbVD4k1xIpYRbUb416IiyTmmvS6q1W9ro1Tz3fWJ1sMgGAwYpFES6YSWXbEMD-JZIM1sMPFxBunC_JufTpW1T-KeNgM0O6Oeu18rEQ6OTVdPu6VfU3CQKWloLv_xY1q0_4htyHK1_IE_n_JwQ_lLttak-vHCUbOMDHeGpGer9ibpdhUbFZ2khFRBHkrtMcs_p4Kn3drp2eJGkcPWBmeItFsniKBuSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=cRBQAlywo4IGI3BuOmTaCv3WtnY1fxccpygbyh8d27B-soeWqWxTvfC8sKnCi433k7sh9HI9lmKgTfU2QyLWpjwXZew7x8RmntDySSQlhfvyPMsK3QcEUjBAbVD4k1xIpYRbUb416IiyTmmvS6q1W9ro1Tz3fWJ1sMgGAwYpFES6YSWXbEMD-JZIM1sMPFxBunC_JufTpW1T-KeNgM0O6Oeu18rEQ6OTVdPu6VfU3CQKWloLv_xY1q0_4htyHK1_IE_n_JwQ_lLttak-vHCUbOMDHeGpGer9ibpdhUbFZ2khFRBHkrtMcs_p4Kn3drp2eJGkcPWBmeItFsniKBuSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83481" target="_blank">📅 09:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ساعت ۲ تا ۶ صب فوق‌العاده اس واقعا، ملت میخوابن سرعت اینترنت رو آسموناس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83480" target="_blank">📅 06:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3YN3o0sK7Rh1z_qaYAWZAqc26CjyBWPY734I9Vjv-Eq7sdfj90KDbHfjMH5H8dAOW7jh5JBbohw7phnlfv6ekIA-MZm9yCV636pMXleQjl8So44KFmDyBptJKRkFCaM6sN8JNTLJg8XxKrEK6j9nD_ArOzT73uvvMcyhcEQBcsWCn9A5mChkEELEMXFku1E4oOlNcQ0cWoHz2jFeSIULleWFa8xXCUWx_zXVEjJLyH9CczautgN6nQlBmfVlO5ctM4KTC-fo9WZFr6rVBhYHybBUQnrTkBRuE9Bj07aRJBnVBvVrN25iXG_ZxafuUIgayDS7fvRr-0T5iE8QqNJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOSCKVu5x-SUMpWJkwFIZGZNZkuWsHNZIDQ6XDoiQW3ije793Id1X6J36JK7eJiauXcgJ90cOapjvjzNRYtuBSGzi2BkA2jUAg6f9cctf1JsAUPRDK3CGLj_-k0aEJqxtgTuvu3oMvBLtD-IFEGx-ToImgk1KQTRKIk15ne6MxOxjiK3IzZkUP1cCy6LFSEet3h9bWNKF4la_TNYMHZs4Hc0ItRMrNuNgWZxDhtL601jzZ0YSBihQQndpca4RjJeDsa-GQZVZW-f3Jp2KHFS2fNxNPbvX2UcVgYFim52wOpQEACgFf7zPvsb4Tn9xMYYxsqxRBGZBs64KNg_yRHH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOg7NxrJgFDlSOmPbXQn3A__5nRxThtpqg_9lpiaZmGVf_nf01aHjF2yYVEPud5XGDHCxrNkplbGJL0PVKpCkCL8L2iSI8qJZOHoKIAUdGNu5XlnRwHgiAganLmEwFC4BEAiOyVMJEa7KH0uWIueM3rkdazjWEDYwHHbjbVMZ_xNMVrMjTvcD4WxxoRwPRrmHX7fLV4GMqTkKb-AYgrlE-dSjlHOCu3s8mEbyVHj1feRzsDsozzIYletT2hBXbcQgY2rLgA3aQyu4sJV0hLcGBowDuOV8_ixPhtjJ3amIxbLGRly2cx3J5i9rkpdMr_9Dlot1rfqqUazO8KbZ2bmeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تام هالند از زندایا خوشگل تره</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83476" target="_blank">📅 04:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KizuvKBTIPHDqRzV_IAW5oMx-Bvx6T_oPEv0XHol6cqRx8udjSkDoZPvWSWc2nBXRGmhVv_RkZXi5ESQRGJ_byoJpX5fymE9PNT8JejKNEPk95nRfk9woTf0n1GAU6gYbw4LWNhs8_ZwQjUA8YfTMR8VUwPc3J0LtImNj3IIDJqCxzJvLRNmcf6vjhjlkzvHx0RAPB_DD92jhUr_yqKs0gTPUui29tMweMjU2fIbz8d1WsNYnXmw8YESkL6LbAYn3ygNcfeZzJZNxqaoGVLOjCpbtJTFA6em-TUtAmK3S5m1OYHvFt3krWT4YG91NSdsDmwqxVSZhWCWD0iEK47ahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآ وای‌لی برای سریال "The Pitt" برنده جایزه بهترین بازیگر نقش اول مرد در یک سریال درام در مراسم امی 2026 شد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83475" target="_blank">📅 04:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bpj4cqsGS_X9i7CQ-KPU1dFSk0-KjdXDqVQWtUUpN8zv4tNlBjp01nT-ukQ1_0KHXeLvD6urzxMeGMRsu_B4rb3Co8i7NNv0T7EBWl0wVyna7UpGqbKy7M-JgyLz5lgCL-0ZNJzfMzBb4ZbWwrCK691Xcpgij78YCSd4VdjH0zPy7lGyQTfJEZ-oHFWhY4GxvZ77FlTFNpIQQBJbcixW7KjXBwzFyb9IvYP3aU7in8U95ltbVEIny-K24TEOQcmVxTHyWOoPqRZrkbZlZGmoQizScGGgARuWXO3g6Au7QrRSWsdy0216u30HN8II4ItZZfrO24fp6J-LRIsmySf6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ujl7OL1JxWPmi7EtfMCtZghOkTkk7cOUdICfDrqAxuWK_EuNl05_4DxLmZwT7zNiw77tu1Oa3AmlC9ZmZ7KKNsiBvQqbanq5FNoIwWLRkLTzdstKoyxg3IO7KXRf9FTrGOmi2hvbBLGo4HRBj7gROmlQk5sELwoskYLFY0nr0Pw8ZtGZ_XoW3zH6LbzNYfvjTqZLuQNnHeOkaaN9bevWlrNQ5cqecaSptS3Eh4y-GUqUi00SVCF_cVoYk5bZu_tk8cmfZV9xTpgg6l-rbl5PYL3zVUbFHRpiCa48cHXuONO9SVuBJd4Kfv6O1CUipdsGQZmU2WnOk3_d8NUqByHShA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سارا پیجون</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83473" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwTgcavvSSRkU_IjoZ1Xh0z7cH8g5kW2nDCtbQy7d5Yzz8ZOfX9av-yMnFmmLQf4exq_orlP2dny1iwdRMSaAWi1zhS__PTW1lZzNsc6hPRPJSIH2Pxxcm0We9sHEBU8wAEyChYFN6QkJ0x1XMLZx1BQS9Kiu7BTlnltzJs0wtu5Z3pCQeZTl2IQkjBbuiHSIVJUFbakpzn39sXV9tRue9jNviISxj1EmNHaLgJBNVsqKTYxQAzgw8OfNNQHgVPH8xFdqt77R739AiamVyOyLtBo2Wf5_tyoQpwYorxThjEcrqbIsDPy4_H2UqEkhxyrGLlJpxIe_KNOlYGvCpuQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-okIw6LbBtTAQZKM3AD4qGL0tKAUYOuRowHjAYKAImV97QZkb1GmW1uD-DqLZjkYKNUzY9x4CwBnVpOY1HokAmRCw0PHN0Zo4dyJacqSgJe8b0i-NCcB--1Crb8nvl4SqzwmkRC0ptGAGAR-oPdU_uvk5_PlwEx-6a7dARv-u9DsVqluDg1RWrh31CxfGdzxmUtmuFtpjkmZhjDDE2jfDtoC44SKpPiyt8imvu_jDA3Z5UxTI_pNHd7V36IVYG27onv6ztugGNXzfKzd3Ox28uhZTzhTj-E0klcqSXQq1jG5JqjBleliBKVPKCmN05fNdrQK6HocBqfmFXNT14dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا اینجا کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)  جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)  متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)  آلیسون…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83470" target="_blank">📅 04:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqB2DqxeJRTCX5nwvquJUk93O-0vCQmJCGacpUNHMrJgk5Yrp6oOwUTYmMk287yw0cUUWAGR0Zmf5ixsiV4gJUsPyReEfWek0fRtqgXuKY63P7T_GnHwURAJe2Lhj9O1WlN-k9fr53RugdcMP3ID9_wrqCHaz7KOex_1ALVSafxRkIDikmXTKsW6kpQp41v3oGeYqLai5ujMI0aVUahNgn73ahbRO8g2945HmmJ1pnXGmkSqvmgn5f0ogE1LzScnmWqX0NUJYI-jC2HiCADRven7FDhjPotbOI7uEdZeDlDT58OegTaamHTtTRB9itGo1W7DTSy81X_Y_sBhKeuNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsQDnjUeg0o9Ks6kArNGBtvc6M0IM1BmfBsncrWeUAu_0c8Z348UH1N4geKnBdYhzsnG5Eji8vl-Qn48LDSxLqBJPA1lsEA2t8ttNaUGIDuR61_HwC6tdKPIez_Jw70kHqquc66_d75JEuvZ38iaZlSfCgnXCnS1fbkWGawMoAof1tT0_5HJKZLvdkt5nWazcXAukBac2AlV5VosMGUnTux-2bAysyjIaF_ng5lCqpjrQdUBk5ciddRwYinuHclaiMlZ0AnBQhqe7EGLhR3nw0d2QnkoRAjCVlr-E1N3odSPk01vOz6lpXFlxLWpUeYLuD6qBMF2t3-MqbAcLbpbvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما درخواست پستون داریم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83468" target="_blank">📅 04:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83467">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تا اینجا
کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)
جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)
متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)
آلیسون جنی بهترین بازیگر نقش مکمل زن در یک سریال درام (The Diplomat)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83467" target="_blank">📅 04:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCqvazrmMslgzWL2kmfmw3LdkDKHSkfRtzkR9t82oEV2Tcy2h0LsBdga-PPFsmcuKTldMq-HOl-mtX0uaUSo8z9iQ0SLWBi9_sLYzBlEOthAjytAuQvshWKRpCu1Kf6zt5x9a_Go1j_8wdtRMuznzqvCm5Szsb3JYiyfQOidqrcHW8rXqZw3Qjl_duH06yrPYzeaV2uRq2RtsI08Ljl_76TMcvXGIw3mQSp-1ef8qz6UCNu6NRggMCKC7t25VeBlMLAPmBKmeHJx0AY677Wyzfs5DX1rufqrjxbDe1PcLC-lvgujTVSPTj4tYeCC1E0XAUwgjZ7FTQJmj3WlCo1xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMewSrghewyMmAB35PEmfHltHc5m2XG2nC8G6jxX0hyqgx4qkwbuUL_rCMnN4RT0JaeuI_iJ6tI_MAW-EE8bffBAKelGSivAB5MYq11Uzw2MhNEuVGvR8jL7c-iS1_WAaVPCFqn5MrfzMGAI6HLLnPXwfPBeC0tz1d4Piu7B_JZKjziWU5b2paJqo-m2HIpNXmC-sd4Pbx-yf5gWev2jdA9Rb2sr0rADf21k1bCW3jZIKXUZZ831IA9IDYCyIerfXPRyIZuixj-fBiz6r9v7MgZKGpn6p5r6VZ3MLku1TRRCyZcldZZY4UJGXZJxr8D5Odr1lN39X5m38EQpsAL-Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اما دارسی هم با استایل تام بوی های دبیرستانی ایران حضور داره</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83465" target="_blank">📅 03:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE2a05YvxBatREuzOytUR7m1-74bOH5yWu27Utlp8gTp5RJK0s19uMqwadt9uEnUE0Pymut913MuFZRfFbcJhEXzZwh4loyowAMDLMzZuSiWyZr04zbZ0qE01StNi2AnVsCQozH5BhUrTiRpzxHFdDE0p4-FOUKWQ7OLu0n3gjJcndW8J4pWqT_sUo8P8Kcoz_StyniZ18Um5Sn5HZpEUFq0G73WIzGmfhcfhGMzfvvBshkf3x9ibE7ognlZdCK7c5lZIAsAtW-TDiRVzemDBJyeienu9d7G5JoxtvcpHoPwwId7LrXfiUJ7n5Mp2rfSjwK78k_9_cQ5MJKqe-7shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB-q4A7bBJljQ2kWC4Pk2v6pRj2ecO-Gag0luITz1xfuvuP7nnH8wTAv_HRjkXwutlPuluYAe3feLhrQWv8OcGfGRrifMTmGEUske00zpVGAvyEb1e1gCRRtGQnMFd0_BfGmiknLOHuaNAD9k8m_z4-VQYqgaDeMJSghhRXvCOFCbqcXYOsXE2pCpmg1ODfPjrBV0-Eu7HXRgXC87_T6Jm-TJJ2iOHIWF3ZK8qt8baLLBA_v6tBKdYpnpbazhHOYjUVKycXEYjQpQWBZed3RAiX3l431Xxw8Sf1pOyh5MUrN-tn5G2ZKoOw_NQ5vjSDGyOkc71w7moZxnnCy4_czYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FedvzxwR87tfv-5u5eYIOX5l6tDA-Kgp6FGVMzw50hF3QaYtyIXWeyajSudad3edS9mgsFZ8Uy5oA7klmqwCRwzCAI297aXwFC8P-l0BWa8R0ZeT5qVHq9xlvMgv4iF4hSEDEgodH4Xo1NTUJFpiEuEYCR3cC0Rnt5NoSVFQOa8jOhtCPsIGbuJhif0_hD4pZCDq5md4WIfW4GejeyUvrgZC0EEb-2xnJiHAnkHxQbs8A0nEZbXhjtVbRVmSt6sq4cx7CGl6trhfbX1x93V9iQMNmwk5X6DK1_dyJhyyVkO9Pvaxq6brMVT0S0yyfggGr8CUG84XyQLUsMNXwvjVnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپیده خانوم معافی هم هستن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83460" target="_blank">📅 03:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5zJsKY-2JlfrAcyUNuilRF5FVoP2qTv4GlCGKz5bj-rZ_eHw5yTga2rRfgD3WUDtoJrfHi5g1eGOUX71VtJO_Kyv5ItC_OvW9pWvD3XnnQxCD3dRexP4h_e4JsZA6PtNaB7XHxsGfoox1b25nDoqPI9mXI9RhgnzqyS99U5Fs08Iim4x3mNmcq7nDD1BaC16KX2Dn_v-ppMP24EtzMP4ny_3Q9Dv929l-baXgXf-lk_O5ASyuqAHjrksZ3Jj7MrpiL9v5IiPDzZDKKkMODDV3E17QnphqwJhCe4xF_6r933e8D6a-FxsHNTq-0maUolHi9WHJ6vempsRc0Y3QGfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولیا گارنر هم برا خاص پسندا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83459" target="_blank">📅 03:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83458">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaQGy7Ls66jJkQyb3Jayx-EiavxLGvNLE1az1__WMznJ_uuVnH3lTMihQAnzBcdn0uhQ0XMM8cuKbHY7DuMTd3ic1d_AlgNV4D7h3oTWnR2sm-J4FYpvg-KMUka_TuTcQQu9UDNhJo7q0fRutPTMuQU93v6dKEgA5X7Ctyfxr9s4jiJPyYh5mbLFbsiNg2Q68W5QZ5hetqs8jXm1RJzjyXPrE0FkBxm4cQtLBCG0CtVyYmO1M34y4oOWraYumty2Y1bnTW17NwQLz2WyNGtjlFOjGNTAdY28L5Cu7TtbWs53OG43AFNToptdLaT70EScuJCRdLb9DYcCd7ach_m1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلورتس پیو رو پیدا کنی و نزاری ناراحت میشم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83458" target="_blank">📅 03:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c06_RnDKAsRw1yswq7wuFjNjyJL8w65KefECHYceaH7MPEQQGpIFTxhKe-1U0lJicTiw5gCj-lEy8Mc5Yt0CkuJPozx8KptW1m9g1qLF42YMYqkkDOt9PO3By9bQwhuMjXziwUPNWjPampxXvJ9WEHwSnNSGTVS7WwXfkJXmHRXbbJPZ-5pWLCwOJZ4JzmTVjYm8JQoXvm6K8TRNNvjSwcJR0WqiqHo744A54PiRMOgMOgpn2pBtLCAmfVu_fPjZuPsnAczeeNdlVYbSrThmNIU7ZFjAup-zx7oz5OOydKGbIH3AUDkd4z-IMXxD1aiNMlsPvXEcQKFwnKe15QVFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهرنگ خبرنگار اعزامی فان هیپ هاپ تو مراسم امی حضور داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83457" target="_blank">📅 03:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Artb3UjgOAeGZgxeRssl-TqL_ksse1iSHHln9Jdu43xJGMtBVuLz3ASUpfk9ytWNMG88mvB_is-pwY_-r5lmT51ECvcX-qrH71YJNmyaUdC3fkNye3-4gqEclYB3KulyCsPi8SocILPGgr7GTTshF6NA59uCoVk_VhX8475IWzOe2GfHYvNznspC49x8UhGllj8pRs9M1eYmCiI3Yk6Do_HhlTmlc-8XzOKS5UherazG84Hr4E6CIMWTPx6s2rCrYUxz5seb-43mblhx_nqts_sCBWwxWEYlo8EVQ-KsaU4Gxpr8a1HrWGax0LV2xysvjiFpohlhdN0sEM16xdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندایا رو خودم نیستم ولی شما ببینید</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83456" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7xh0YetJBS2XRB6BpIQGzb3QFbU-ymFY7g0CNB-j7u7UlSXh8nr7Cti8jG7yzprMdgRL1I7ZkUmtB10Wc63QcUDQB1vRTMeiY1RvKNXBc5LEt2PRKJP-FNjBh8m-yA772IQhsErXCu6knYxhbWuxmKDx5fozFVjdYOpYd9sWZg7je9P3Pn28yuPZjo2fgdjbzlcFoUFAs1xVHCo7KoLtYQ-HyUtmxGvpllwKxVYXJSXKoOJj_6WuTl3BmNIfGFZLfktDdYVJzC9NVNafilbqmGYFx7Ijn6vQI4jqakUOnRj2l8nQgb3w02fhooLfEfHXy9fQtCMjLMRf40CarGTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای ال فنینگو بزار زود</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83455" target="_blank">📅 03:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ببخشید مردا رو تو چنلای دیگه دنبال کنید از مردا بدم میاد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83454" target="_blank">📅 03:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxO_dta7zFS3qwe54qj0bPLReDtPyKT-iWs_FWDoORYzSL16QuG4zy16Bmsm-rRvNDdMmlY2bIbS_3pYI0IdxOflFUEhlPYEZUShoIGXJuYEV0WweRzBr1xFLhhhX-MDH4CS2pnl4s3c1u0d3bU8jqs15j_sdCAagIr4VmQegVDKbfKYQNQE1sgeXGRHpFbykP2WfTLSonGNBM7gQdqcZ8VCivZgXZJ_XZByky97lkUOoHEWhp_0m6vN1q6S9HfdEi6nqsP2p_kUUhO7r7Z4gmYMf8I_Lzp1TN-5uR0kgAzeGDzCZGblzGowmp6JuS_0CRng5nkUcCWUTxJS3mVpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83453" target="_blank">📅 03:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83452" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvkwc69gnHbnLR5CixRZvRUa8kzc32wcN5ZHjDY-H6afGzZtDBCcy4xtEj3ltR6tqnQdHBoNWZHY_N0JeY_nd3cqPFUiGXKcLK7tQSqgIaHtloksvniRxWe4Drf0_zBFGIhu4A0FkUvxriFbpU5k4s8VfTkVMzh7uoFqiWB7otsweSXRQt1mANGkgAaO_c72bpAxH7eNIeqjUs3L84eQG3O4x4uA5eZIrJGbq8THA1pcdLwB5MxMa2K1EJP3opFkf6p0Qsiq_tMrQRyjE806Qdho7lrSaRpDwy_TEHuMuqnXxtfKJsa36WNtB5X8fwgKqLU5yYX-h-Y4A17cC4gM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83451" target="_blank">📅 03:29 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
