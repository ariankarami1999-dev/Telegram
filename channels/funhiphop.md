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
<img src="https://cdn4.telesco.pe/file/uIm0T3pqXlX0hc23FIrGPxlJLeKuXvfe0ignZCdQokZy-GW2J21jvP_-YP7Vmlj4KX_iHGG1AtCyx3a0qc78GVEraDJ-DVxCYSWquFSn-LBfXfiTdjrSulepeghzHEB5SYSXOHxQukzQLpZzMoBlursnDpxAzpbHiVicUnc2yvuJ0JHJcQ6FSQfrwrJvz8hT77LdyAt4Qx0Lq8aVdwXp2dXPIFDo5XY3Bn6N94meXlYDHlOHzIgFS2IleA5F8YkD7aa17E82rt-WUk__1gpyS7ANVMMt_jG_W2y_6jqGS2l5DjmITIDuMOfm2pTvPiHwog3eoUGWk6CVLc9ZAYFK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کامنتا بنویسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/funhiphop/76998" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بانو آنا د آرماس ببینید.  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/76997" target="_blank">📅 18:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpLyBrt3gpXhUd-XfKQBjRwthIax1XfDIG3iV3cfDfCZDCXIg7qOJH3Dz2HIdT8XbTcrb8hiejY46Ye398NpfkoMy0tK1WPYN8Gh4ZRVbwvSXtvusglhB67i2w0Uqp1MhMxuBk5khUbhqlBhM7vUcgnKecB2-0HQquyFhy02K4u6I6Irq8OBbY9Y2diSROyFCc9GK3sib2UWvqJq8YQM_KmAHewUjsxtrnhPtVwozEFLfhUrNrQK6WHaOyVZiEQRUHnCikzK99tbj3HH6HV_vsvtjkNm-UY6UC6y7jdpMBi-L8xDdWvn9QpSTYsJxtxCC1MDk4U515xGAoNsXCNjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txl2FoaZUfHcYfuZh8SIYALVLgn1TnO1i_cIw6_oY3j5wf6l5fUgSt7ogNqluaRq7e-fRrJ63AMK3SWjXQRAzFGzrAVE8cf5rKWSuDQIBySPe599_LnZypCiX3sjzLFttEsJKg2FbVAzt1F1hqKtv2HW-9wIfBkc2Sds0geq3Hi1z5mgljWP1fsB9YwTr1QpglW0bh029wLrg0VRPB81Beusz1FpkJyjjeDoNecDJnhTiiEG9zzs_Ehl02eVMNdbZpQsZSho9WhJr05pNIqphpxpn_L4Y0WDa9xjLWu6bssf0TF4F1FUtW-1lUzy84_yWQXIFcKI2OITGSdLQvl-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjRQBdPKjSt3PrfUPO0VPgC2W1xQdlmnBYiXDVrktO4E34qVhxCq9l5fWZcBOBhGgF37P5xLyfoA2YxvUq6SM1nt9su9bZEyj4qCRGLKc5RdL0FKuXx5rCHe4fAshBDxy52Ydwdgh6jYxAbjK_HTdQWQyjPU4CwJy0rJpQhby1wQpStAva6zKoNDPkDKQgA_SB0bivq-SlcNMWOp9fsGu7n358Viw1GrtTsnyvpcfcqITbQA5JPqQgK1zTcmmulE0VVBTv3GLDTZKqkz684NWuL93V9OVdx_fadRwGNDLD5Val4OJjrbE2foxjMq_8Ra49-BJeq1k5h0A4kVtK4vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNhhVsQ_x3HfV_QJFJHZoJuQjzF4V_B5gEQ-Ge-xac3IpUOCvNTD9VQxqlV0lr4rt3KtEyR5vr2GUWfKxplP4IoDMTW8Asgtkcx7TDGGPFvBESQEVOSLO7NVzpALc4n4e49-0X6B58y6VL_TiWlP7uzWEPM9BM1B-pVAJ5orOF4kKEGKuQ3P3hhUkKOrlFEDsFjXlev-g5sHG2OizPv5thlr3mW7J_Ys3KmTc5QwgX05RDwl4fUkWKmIe-BT_F4TZeJCMlVLg260UB7LUroRW7fRS8OLN41T9emcPxWNSlos2c5GQncCewe7HZTRuGamQbbIVr4LDVZd-4PZlwIzBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو آنا د آرماس ببینید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/76993" target="_blank">📅 17:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OctgiX7yFvH6uGokFZFA3ZwdKfMSWo0QPTviGLTkzHjagUfH7OGxiktwKtP22Gx2xrqQr33CrChNKCFj1ByKIIBMFgFOBWZGgNDFlMF34E8HCUGHaBs7ZGeONo5xnTR5aA7jijRckFhzKpC-MhacvhgNeN2XUMYPFYOQaq1LsfPcrnc-cfSwmXh0kIMpD2hFb8EqC7kvgyeS0swSTiamicHbXSx49MpjTcFLnS8hfHRK1kN93jh21Mcq5xF-0CqQlYUjNqcf3BuL7hxWe_BRUoe_b2fkojuWq_4QBU7uXRm_LBoVowqIaaiByAP1JTLoN6r_W6ChT9Z6bbO0eDUX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای ممبرای ۱۵ سالمون؛ اسکین وینیسیوس جونیور به بازی فورتنایت اضافه شد، برید عشق کنید
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/76992" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/76991" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex7ZTRIEDMTVcVZHoDi5f6FAUf8XHk9UD3dFrV7RPXxtcCs6dJWVrcsqyJROcVHSsWoYGiGo4gqOETzDoaJ_MsBSVrsQswoD8zGABvG3WMsI5aA_w4hMlcI6WUnqJBYPnR_LRSUsW2EuiDt4Wrt0qV851acWI1QQJqieVMv807931zVESpaQxKDfdgCeFHelUuW2QkKDUl9PLo3azCaC66GUguoj7Z63zrixzMZ5ex12pg8HX3wJJWSt7VSsOiCpHZnymrLWqmt6yhEAHJckuBgaFX1Wfo-O2vPNCPsZmF74f2PTKefSC0zqqZ91SBz7JGWuB3C7KwyE6jY9sH0ioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g16
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/76990" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ داخلی پارت 2
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/76989" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خلسه هم آدم جالبیه، به ویلسون میرینه میگه وصلی، بعد همزمان با جی‌جی هنوز رفیقه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/76988" target="_blank">📅 17:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جمهوری اسلامی پاکستان ۲۰ هزار نیروی سرکوبگر به مناطق آزاد جامو و کشمیر جهت سرکوب معترضین ارسال کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/76987" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJIdSHZUeU9ab6zm2c0hLKpLq6XU35o3R3CvdMQhQgZta4g0WH_s6Cv0JBcEbn5n3tUk-NmH_wVaJq9QAqqjXOh2BQp-WxkZQzDIaaqyMnbQfb0O7X4iSjObe4R3NimuNwrocYaiWiGhQ9cYs5PaImlD_TEF_ORKb9WJRfua2TqMwFsYM21iYbh0yp6ONQyzk1NOP42WWuw5bJEQTdmXpQ_0IViv5QcGU1FuDLKox_A8wHND4AFuf-74tfz1UM48RYJNKqT16gXsGXsT7QPs0dnvO5KD7gFSOykjcFu6TaO3VYVQKUtLbbdHdsgiCMRhVHpL-QrzhlNiJp3C61_XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز سلام و عرض ادب میخوام یه ذره بی ادب شم تو این ویدیو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/funhiphop/76986" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">او اینقدر بزرگ و قهرمان بود که حتی دشمن خونی او یعنی دونالد ترامپ
اورا "سان آف اِ بیچ" یعنی خورشید ساحل به معنی بینهایت و قدرتمند خطاب میکرد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/76985" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iR96A7GLvDDg3KgvHwDbdGELlRb35AvGc-09ptlpMkxZg9VEdXfa4M8GP5tclz40Z1zNJeNBqcguCPl9TkYmsyByq3_wS1zU4ZR0mQwGjIu02XvznH3BsJNcmDWuLuNZ42ZADDO5fSaA8kaSZzjz9_zij8Q1kfq3TGfwDzgUJdPJK74TSwlGrcaQsFpFPGLzZaDbAvZNHu--F3mpCEd5aUKheRqhGtkosmiePsBE3Sl-YOAcFGZnXfTRVdJzbuSVX2uGZ3dCxCIIwQDpcFu_f4GZZPpwWyvEp-P4AFLA2mc-Cgs47RoAP6ips005AHay_Si0fjxOy6c9sJi3YVShsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX3sQ-nnCA-v9c65q2FJ66HPC8gsWDnIqKR3EB75KJCcFcApYsxB-ORbkVu2_3BN-hrjQRuVF-HQ9HpguAB14939NJlrJudvlCxDyumEr3iZJvapUsLns8py7yXsWOUL6YTwNSXHo7FIiRyWEpzp012zmA5a2ceUdX2KN0t_JnwFpRb4OlHJAXFudmciYjfYKKcfI2Jy3gQSYoCxOgArgwHzDD2XPCiz7IWab1YyCgVFFzKH_Beh-F8GBNAYmYkaDk66GSd2co9BzUTQ2ITCRkhuG9za9nV7qakNwQv4tW16J1YcXz4lhfH3oQs8gW5UCffY9zHwbjXNg4X_sHhPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان این وسط بازی نبودا، خیلی واضح اونوری بود</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/76978" target="_blank">📅 14:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">استوری جدید امیرحسین قیاسی  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76977" target="_blank">📅 14:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIuNraQ73HRa0MMt3SPXG-7YQG_Orfmd3MOROtadgpKq8j5zKx15_A4yHGVyDDre0WImmMVb7v7-Nb8TrrYL9G7A5uz6_rxqDEOIlE6otjVOnS8okmUtbHrfVoPcgBQrAUMVDlNxk8-TA8q0eVt74jUzEKoXd-HWxZWstxNq3kpzFQQGNBlnfu6ODwHKUArY9he_fHm3wDD62Tg7SYCW3N1KbFeaNCRqrzL2wmRmluAAONRpwTo_vkLHNFYGCexKJ9AaTCyU-R2R9rim5JKAtf2QVT8lm72M0AryRVsgAo5FyUhznri_5dqty3s0RgPBjuD3yj2XYdOoe_X198WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAbxlFmyi3kMk_LqGw7DapCxQ_5w37J4KI6C1wes307BubjZNiqxT732-OK5umVWP1x3pUs8X8sxAwba1hwLoloxMRNDe8wTFBoRDfx453BHaltIlp8egvCIyj7ZbK_WOySFPtrnAqbjEHBE-ssZV8XOKdCxq2cKtvNXbaWhKp1PFB2p3xufvZXWHZynmQmckrHe_oYWKmX9miBktjr0diMg4K3AHeiVk3NSbrRJsTwF_lzm1aYVw5iNrT9o44EzltJKr9x4BsvsZvFmHxvwj0gRs1-O0Js_mUYKksXocFhNmF1UyGYmKRZlnoQ0gLQhZM5JW3m8pIXuQZbxtjs4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcSb3EfnZWVTT12e2PtZZ3sPesecjC7XJwCCQlKsOY2T5ttGNXfWlX4L-8yupUfhDo_Oz_zt8eDbz1nu8zPaRC-L758HBKuVfYe1Z6Xj5_ot_-aDHrM0iFEZhMAutnEw_3pTEucWNoqVcx2EMy1A85X7BpbDvtBsufaIoMPHnZWHeia4iXrHmNnkmut2c0k9CXzno47io81w7J031neTmGVA1Dx5GGACb6qty7qKgcSnq5kOhXESOFmvjlJlZuvIS-UCocmwHJKMDSQ9W7M59yG6AoV-jt2VlJ26O0F78H8fNXVebC2XVguq3C6igcMJOk5GX07MIdhbTE-pX7FTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncg57xqyRinV5QNwYA0cedu92e0ZD2ZBPEdExLOyHB5pRSLBHfFOFdPtvTWS2MW87PKDm2SvW7TLlPnwN5lGQFyLJMhY1huaxx-Y4vHw7Qdm2yswR2NKtgylzwwrbux-vR2OTFBFTYiEj7sq--eLRAdSCk4e5zO0pYk6pGLw9--bRhpWK_WLqUVdm_wudj5XcPeqZZKldcU0y05Qy27o0yB0CF-M9U6IWKZNN9widQzOErz5Zs9D3XXbYSqPHM0i0om1bbKPFAHWA_QSglcKqleYve5p2eLLB4fRFedV2Kvp6f6jkQwS9H9eLRLoJXToBVJrz731ZR5ISeUMjusFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iON55MiHP0KTlMLJMtuYGlVyX0tXhsLxDvXbJ5enG3ZC6nsQQuodyXCfWwoAvQykcWFu_is4aZ2pLJ4ew3PXhq2hVwZZRU0DcBcz11H2H-aGApDl3jR7pt2fFwvv_YrL-tWbm51ZRsPoo-S2dqjMFE5nP1rkJZhqBNrIcDYWTgiPtuXIhKrsHuQmGPrjf8aNffxDrdJ5VncSvczjkTGs_nDzzwpPJEStvD78--SGqzKPdWsT68ITSwFwP__VE0_qI2XLHzFEjW7O2Hm_ddyO-CjJnZZgPF6mSmxQX57SUILhVnYhNfigb_SeXxTWUTkREEc_hX1Qy0F6RNbsC6BPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwhnzduc8t4e2zmU-Wq2DdpdtqilwiOwMnpnVJLAV7YKIowSAwbUTFA1dp2kUyZkSpBJAXUizH1Ge1EM_ZyGhjEjUXHuVrCGBW1bLfzqVKA-CeWKOh-2-3MrbG4zh9Uehwm7GjixsqB6hl04U2PXdnVrAvuadnFEN6A_K1-rm1W4cnoqbj5yRU_Tw96fXZkM81rIPp5wVe9IDd-klLjIaUrdfM6gDXqHZ3TNPPnZGahjMUwa4HpWkiVBM8BEXRxZxl2cQRt6Bacb2jvQGXlo4hQokee6t5IuwCAwFZHy5HMz3Qrdhkrsmvw-prEdhU2cyK4GffLFcQF7LhfmF1wQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpK8isyomUSf9HDtqeLF-YESUsSjOJ5Sf5u6PqMoO2X-NAw4FKmjdrQhM7sf-UHneZOBFsG-oJAk1UQslMrrpcctnZa-AtqaGJsXJB1eTipH94XeoybQvVjH8RzMCOeMb9rttt4e3lz8uuuad-nChmHodCjE31N9CBn6G9qWQQjTxe4Myr_I07RZk7HKIfVcpN5XtPmBqK6YvINETeI75UJNtWWEkMY2fVJZt1q29n_2bvSXzt1OwLO90HK6Gz8lgacDT8Fnqf8eKhdlBCXf50W16jKHmwbkjf-sziPRRi666mzpYhjItgaALEsiSmy60SBCkaR1cloPt1OYTxVRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RTogO0CIabb9nOzRrlrubxcJ7B72oy3TyPEmNCLhMaJjZsjmGyEORz7-aqMaoGns40z70tSGuRZKStR0j86aI870cCF4rmvjejY1ulcCwYtSdECEFIHTpnP88LnhZID5k9Znoz2Noz6q6wWc6E3Kc7pdBIl1YPwVGHvsN7Uj3_h_MNxc3p5n5pl7CvQu-ivhQI6GJ9sxEAL5bZdjFJsKzfOnGttYimaCMAuvU1GCjYikrACbVkXT2J6xjmxtyrTJcL5LwjubkHuCV_qjAb0b-K3RsQFDHbvNj_ro6s8zfsrytyprusxDHs68eEsUzWSLE2Ez9g4pgnp3-UNYGflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فنای اسپرز بیایید بالا میخوام بخندم بهتون</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76954" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76953" target="_blank">📅 11:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0fllZ3RCduHURYfk_OOcQvD49kXG4DQwhM1pTOewbdrmn4GbMDMw7gWcLQIbXgrDpZ9xLtHXIM8sRzE_Fxq6u-M3dc807x82bRTXsgy22i2OVuY8HPKQzavLBAoD4WvxFaHZ3SGMP_qt6pRRgauA7fY0O6Yqs1brr7VB2zAF3zEY1UPJOcAYsnyDPvDQVh9bUGO2g-_nf7R9foNNClN6DXBfhkr500EqTi9WibJ03y2pfrAOj8PfNb3Q_nVQjkGIbWInmIoi0qriRHKdR4YGvXeq-2_UraNtEHn4qVqdgv0SY93pD6beC7f0E91GLCQkF4ENj3k3UcRAEaBBvVJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم سریال جدید اسپایدر نوآر با بازی نیکولاس کیج رو حتما ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76952" target="_blank">📅 10:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شایعه شده که خولیان آلوارز رباط داده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76951" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9mqgIpdPXEit9T7VP4wY183Vw0w18U0DN1tc_7uDQqvLQ_66kigH0oXrD9IExr9IpEGmYCtWJU1rqKLFeUnFq_W7xKt4kdsrHqJNjATh8olat13atCx2lmeRRB4YL1-y-tTv4kY6jbwVEhDWXompwFMkRz3OSXRphsvjGCBFxkJ1G0NkpBMSfV4RM0wt4cdrAd2QxLvp94FnqiQISRrgHG0vO8LooFcN-mIAkIvzT-n-xLDf2AEdvVK4wswuQH2fiCEFCzurEUOfhNHrwawyWIOMlNPeBHX6DV0QJv_4pZIR8BVL8_kdeSX8Evgfw7kQg4hn3P07hnFeHJIEaZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو : رک و پوست کنده بهتون بگم، ناصر کیرشم دست پرز نمیده چه برسه به ویتینیا و نوس، پرز رفته دنبال جذب اولیسه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76950" target="_blank">📅 09:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbS4mauxdHn8mp0hQoANhDPRo6gXt9C21CZ59lLaM2w75zLRb2bRthvPhebAydLKYADbQ28NttUQqeLm9ZnE8t1m1Dy2moU2TE5u2y7mipgloe26MfuPIjzaollPUW2HnLFvAt1SJAGsG_0eRag1gRjnsJvBDHM5kjnkIuuTY9fqWyQns4zY4YB_Ph2zSA3Rfl8hrqMmp-TJOi9wzJ9eOpEOrSZM4f7QmvNwcb_WFjATmxuU8ZLexBGj9_cPKuXcu60TmasYDPCSp7vlqsvGYEosemSnQnZgkD0YJagA43ZF2n7LxAwh6JCWRH-P3S_ZsFCNkbMbj_AOatA9AONZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI82lzNuME284R2oLHsSUEeo76BoSxUhazGvlhZdFVEOLzzIGeiq1-X02lmG22yniZ7fkZOphgiFkh7YYUs_eUlClEgo07HoJqcgKkytBLRY7EOxo5IPQy2skQG9MMH6y_fV1gkNA50m4m-e7W_tQ5mdJJtYn_da3S9cFvnA0PaP2HhN8UIWSz5UyQM3qD0gY0l_FpTb55_tvvigCW26aHKAl0fqiXkIyPKZE4osVhJewqdfLhAxv2jEASDh2Xa9MR_fqBfRNM4rfKPJT0SfKIgT-uHBfubE-rQD7v4ApzpFM9lQj25nxtkGWiLrs-8rBgQ1RdngwZvk8Nq9AH1Lpg.jpg" alt="photo" loading="lazy"/></div>
</div>
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
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76948" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6cwuq6q2ifRBedJk2QRvE_kowZPzlTc6C-3poEGUI8C9HO6ie-rJaRrBe1ywkMbhjJUNdxUB7GMgqFtiVhllhKU33Zg-CGyATYiRDsGK5-V8UIlppM-D7PbyaNulCMKXY5OYgyeiCDezV0TcgnMn4BUODh5G_AvV5ersV5Nbozd6kuv4zZrE-AUB5-69FzCLbhv7Iu3UWvVkJgEWX32jR1NkllUrrek0JSUq7PTFepF988cukiRT2VsPeovccOJdJHbrnVOd6hANAkowaevqxiInf0iENLB48HSVHNXvP79D9A79L4_CqpnPKDY7xV96UczTfTMqTwsSqPKgR14Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
R16
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76947" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">روابط عمومی کل سپاه :
بسم الله القاصم الجبارین
فمن اعتدا علیکم فاعتدوا علیه بمثل معتدی علیکم
ساعت ۰۱.۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مقرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت دو، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76946" target="_blank">📅 07:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76945" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76944" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMZaNXullTHzjyt6xBfNpzj4cFvUZdQRl2pegyFoBU85SLT64WvUGFq0YtTU_NCdxgSDJZQerQ6agAS4iW-RY8muclGKwVb_NB-oOmRvrW3ph6Z7yBKjtBQAEeP2TpzVYqQ0qTNlC3jBuyZczXcetz88c7Ci6cUVYPt17CwJxe9TJrK5ULWPNGjgEa5PncWAc8vBijiIea8QAl8mGRns5YKabhkcMOE7UFrATNrDe4Ejs6HUxl066OtFovjlpmYgoSONYnIe_MbqOPSWdqmYjVXuVzJw3DyK-xp0WrOuVrv2tpCS6eOmQ0vPHKTW3zUJdV-3njfgzLT-g9W1XPfLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsllOPh9ChruR63ASDrgr7bDs8FHOS4msPaAY9xKdnqsXQqS37uOqTTOw5K0SEItJlyAKs8ouPshKp6G2RD84bX7Cs2Dw925KRpIkDNrt8wHVKV7BJM74RezQMN5dQF9YUrkH1c0tCkXocaK2uSoPBkvpVa6_xkmdVbYfnPpYSlfQwQzzoQd9F8e0XTtkEIgQsIws4n54lEyPuUy55ru8bATsifzDW6_4dG_VXMMb4gVYNCFzOGXW2kCFXvp2EMEqe5JHbwQ-N-KpQc4lWHWW1TSe_oUIdGl8N6GLlKNsc7N8so6eC92dg1oSu8kwDaLsElRUZibIcbkbDk4d9UTRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=cLhe7gQnqfN3pzB6oiRlRpcSnPh0u5a8eavYiAMlXpVv8mPlnp5BIcFgDSAPN-gUZLGHHBQlkYfBuRvEF-ulQEMw48W1wMXow-9BA8xvdDivSDaPIU5h0POmG6sLM66Mht9qyn0ikEJnWqpw_R7zB6FMp-JgklAOcAmf8YLUJsNlKv263n28Nz5aNOhgmS9FTRTR-QrfiW6CVLu55Zwpf2AC7w4mgVY7RjXKzNvWbxTWvWrXZz8jyY5dAKuiYY20fE0fRBEXTSipqSafFjaX7LsNCLpMqT47HYVl5W3KOiCXFs2JF03YjTwhcOedQDLssBgdPshKs0QV2gRfKHhJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=cLhe7gQnqfN3pzB6oiRlRpcSnPh0u5a8eavYiAMlXpVv8mPlnp5BIcFgDSAPN-gUZLGHHBQlkYfBuRvEF-ulQEMw48W1wMXow-9BA8xvdDivSDaPIU5h0POmG6sLM66Mht9qyn0ikEJnWqpw_R7zB6FMp-JgklAOcAmf8YLUJsNlKv263n28Nz5aNOhgmS9FTRTR-QrfiW6CVLu55Zwpf2AC7w4mgVY7RjXKzNvWbxTWvWrXZz8jyY5dAKuiYY20fE0fRBEXTSipqSafFjaX7LsNCLpMqT47HYVl5W3KOiCXFs2JF03YjTwhcOedQDLssBgdPshKs0QV2gRfKHhJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=WlN9fUxETNsJlyqTQixkY3ImvxervJRu_p5irEB8AONyK0WY6U9_6ot9n9OsG7MWPbwS1luD1-F4RDHI34ReSIM7tyxv6EAHzjjjfLwyvxhVrvwCgmsPa60w_NDJUYv72VMkKQe6R-nqUUi6-gyTDTE6cI-5wSe5W6O6z63FTJmJtDKRIpOkgRwDSb1M-59suXMh0_xQmZlxFhbLW0nzGuxDc6HQrW-mB7gX45dSZ9O120KaSdc4QdVKy9rbPEaMbeNldYASHTA_pm5Mam3qQlCPYJPvAuDPky6xN0wBIlY36dTSrcxIuerYOHYPGDyyMwXy4tZQ1HeenF8AQ_9giw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=WlN9fUxETNsJlyqTQixkY3ImvxervJRu_p5irEB8AONyK0WY6U9_6ot9n9OsG7MWPbwS1luD1-F4RDHI34ReSIM7tyxv6EAHzjjjfLwyvxhVrvwCgmsPa60w_NDJUYv72VMkKQe6R-nqUUi6-gyTDTE6cI-5wSe5W6O6z63FTJmJtDKRIpOkgRwDSb1M-59suXMh0_xQmZlxFhbLW0nzGuxDc6HQrW-mB7gX45dSZ9O120KaSdc4QdVKy9rbPEaMbeNldYASHTA_pm5Mam3qQlCPYJPvAuDPky6xN0wBIlY36dTSrcxIuerYOHYPGDyyMwXy4tZQ1HeenF8AQ_9giw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM8PcaHl6_mM3t4PBnPvkohIldGkSPIEto3cESPx4EIC2urIL8HhGk7lzERVT23wpbTePlfyN7IIvFBb91EnGLJjNEr6h6F-lOrvqsvA-KkXCzF8PSl7LEAJayA4vUQcFFDqOjtv4NePqK2i2U4iuJXM4oJP2TqoS3OIdiTOVE24xbGl8EDJ-PNrw8exAAWqvr9YkifNUw9XzdbHDt67pkmNOejMsGi5PZ0pWbxL9x4JAYrGKmL47HaiPHJc2DpeepHkWElkZhkDepm6b9jpbwgAFOA55aUvoiJopo8g-aTzRRBj1TYgcOp6tECEn8nTwkrVvQoD2fuXoB-LWcWZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=pnhY8jPgeIWnhpDoPLDRdOY2mvwP0qWncI69p_3_kiNmOkN_u5yitmucnm_PrK3A0w5ZiEpQeHZTFwINvMjkoaOxa3VBt-lC98_sYgDGeuKyIkuZKCDAuoqSKTkO1emmAsbL7rzHYPCue-ycFIyO3B9RgxFha3eQpOdQ3xa3WzcK7nHMzy_xOmtdSqGlmUFNmrACwJ4df6dyeQ4O0WNgp8KNZs43fhgA0RywztIWxtZVW-MKoJp6vo_7FFVgRUIRxaPOHA6v69JNhZbwqiKi5xWXQTa8mZLT3fwqSQDmOB1tQRgS9IDzignc4GY1MX7h-uFCL7cegQCwaAgYyiijRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=pnhY8jPgeIWnhpDoPLDRdOY2mvwP0qWncI69p_3_kiNmOkN_u5yitmucnm_PrK3A0w5ZiEpQeHZTFwINvMjkoaOxa3VBt-lC98_sYgDGeuKyIkuZKCDAuoqSKTkO1emmAsbL7rzHYPCue-ycFIyO3B9RgxFha3eQpOdQ3xa3WzcK7nHMzy_xOmtdSqGlmUFNmrACwJ4df6dyeQ4O0WNgp8KNZs43fhgA0RywztIWxtZVW-MKoJp6vo_7FFVgRUIRxaPOHA6v69JNhZbwqiKi5xWXQTa8mZLT3fwqSQDmOB1tQRgS9IDzignc4GY1MX7h-uFCL7cegQCwaAgYyiijRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8bqLp15KlrszJXghEgd3flO-WaPnPutZ_Ysi3pTFuU7G6sYepUWq3kqlmhgl8bZBtUvzRvaU9ezqrdBXm7VweUmn7v4wfIXD8jC9aniwAn5IoydO_NRAdzg86yUSVrVistuTKMsB8JBp3_F3vgBZY1DYxnG4vX0a7C1-anrcy9rQ-8GAvn0WO2cYgkERGnG3EuVDeQo_zS8SASklnr4y8ohPwGXx_7D3CXwpofiy3BmgYSAeocv0TO4D1bIdwJaSiSH-oJX__02hqxmTOE7buyvJ3LRmMpsqIFR80N2Yh53VVLsqblY0DVqEwYtIfysKccGju4fRF1AZforyJUU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej7zWwJXkhjDT-ISz_XUlEiFYvYHK1MvgwbGNVYBb5qbmXWSU00wfPNV-1NzK9lB-7uVyFgmbqZIs38DWBVQDcyOk1a_DKeM7lw_WxUUR1czKlb29JRmn5qIlB0XqttVYOxh3AuzvgOY1HfwWekXcm-JLdsWPU8WXfJRmjwrajB00XWChIYzQgMIf5EFLlOKH1fUHQSvsgFhGQtRPy4p3M2LeTB_Xb_nKlYamfgarRc5vW3w99dKawFU46tqFB5bWVs588o2y_I8GRSne0S8_9x-kLyBEcWWLDXQwH5mtChBYPb7tko1C7Wi2Sdb-tD02LSRK_hMCCOidX14VOF6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=AZNqbpVH83P5NxSABG7feOewXyIWJXcd654L3VMJWUW1GGFdXBqCkF8wK1qxQvJTwYgwQM2YRmtNPR2IuMzso6YrxwQWaBJNzR7Aw-ST9WQjhEzPT5xphAE9kiVQg8BKxbG01IsQ8b5nAc6mjoYm7cYPpNAErRIRly2OVcB8JAlub-9kFmC3K1Qwc7lNUu7dG32yhv0qPAAzTHnGdVE-THBzoVKzRSpV4hsJsQYPBWDXw_Wg6dkHWtcKO110pdyEeEUA9as_KmM3Uy6GTeEc3bHd9t0LhiI-ryo7mtHpAJsCRg5oBNKbgtjMaiFguYmfTkF0czcyvYoGyHEOPR61qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=AZNqbpVH83P5NxSABG7feOewXyIWJXcd654L3VMJWUW1GGFdXBqCkF8wK1qxQvJTwYgwQM2YRmtNPR2IuMzso6YrxwQWaBJNzR7Aw-ST9WQjhEzPT5xphAE9kiVQg8BKxbG01IsQ8b5nAc6mjoYm7cYPpNAErRIRly2OVcB8JAlub-9kFmC3K1Qwc7lNUu7dG32yhv0qPAAzTHnGdVE-THBzoVKzRSpV4hsJsQYPBWDXw_Wg6dkHWtcKO110pdyEeEUA9as_KmM3Uy6GTeEc3bHd9t0LhiI-ryo7mtHpAJsCRg5oBNKbgtjMaiFguYmfTkF0czcyvYoGyHEOPR61qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9EQTmR87p2IQKE42WBPUHTNjQf7xqNoEdOFloME-iZEDw585mK88R6mDW5p0v2NEUECy_mcsp23Yqkx3pcCjwh2OaOPRMMokea5pH1UMXrGk83sg8mRsUwQcpuoAiw1GlAj3fIwMyvQlczWcaB3-oKBDaUDCO3ZRj3K1RxkJYlLtwYssnzUgwoF-3rSQN30rj0YzdKUUw6IXWoNDTV6prwrO-f4HcQYkVPiRYwbB3-sa8tAsJHCKjS5giMppyftaiYCkrIbAUq1f4TRDdosBfi6Da9yHsurXMOez1RGgv4hzLVw6WazjHmYyYojKgRLIAgDCGTk4UMGpN2GkTqRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH4oxEhoceGeslocAbVPjidgctW_YkWsNS6fFitG6yvLO7YY65e0JzOZjkiD788C0dmyz0Y6NcFUK-oElIVBNmKAzSB7iOhNhEK9CrsaY7QutZiET_Vw_NHYpbJ6gRx4YfJcE14YhZsAZ1LmSFUF2bAnxncejAaOMD0ZgoOhDblweVD6ehOX2HHwIjrPDugrK9aYQWoEMhKeoyFfzKWvFSrtZkqBZJoLD4PSHulJGOxTjYcDxdLJN3SbcAv6SZHSppiCV7N7xH7tZZvBnNGvf2Ht_1kmDDETcmZ1Z5Dl1vEjoXFZ1AH212yzwthNuLqj7_hzE3FYp8FGne7PR9qlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjpe193VVUWEiwz1PoXgGH52FoweEDcX4Gu6ghYG-i3u1ilfYqXBK6BLTaJ3AVQbkJvWxXYLx2ISbhTI6Kknl5oHG_1lvSMA4oljFyhi3bvbFcjMC-GwVXjIsUoZy0yUDcsT9AkS4m_s18Sn7FiclRL2sxrjcldhFbQ0DinC-1I2YaNK95S2GMobWr7z2IHvHuLudhrM51rZJpV_U9KMeTrmT8qWmz6nLP_yZUhMARtZWfAgOlPLhn9CZBh_Svb1iEb4H8zSfW5HgWmrqj9CXUAM9P2cw0Q0SJnyYuAAam0Hl6Z_XVts6jzsONv9lgVXoMBKeReBntfxZSNeXfPCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g15
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5U9F5n3xaxrA9d58IHqlTVfItUyjcmjNtzh04RFoVyHDJnKtV_hAwMjWW4_WZyddTGM076p1CHoY0Exxs28KUgA3gIyF153yat_SmU9JzRIy-gyTs5I_gkTfNPXY87XD7OoWqCccaiEezrxobuAmgcnB4TX81PW_ibHlqNsPN95yRfID-CVLQNxMBcqqKimPEJM_m2yut0rfubI0sINpEYYs23AEMZaqTn7lMbNp4yZsFWVWHCkE9AB99bbxZKm5Qd4LF36rpDwFBZ-PiAPVbgizvYWGOVAAOaoS7bn-kebq3szhAzPxJs1Xi3mjJ2fLoT5pSsDpqYNjPaYvDQBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC9EM1XRPvAYxUwR_PKutEhh6x0u4qHupEx9AWhNKyPbMnqahUZ6niWJ2zNEH9dwOuJhHkJvNX5qRCw_FACcCkI1ogS7k1Q0PP-bPF_J5kUoCuhdTBU66fZKVR43VnFVBiH7XfvOxcHEaJtY5jI5RFKO3Kc2WRVe4hcoXZTNkvYADpiVcQPtKH89_7WqOZcbwcjvGgtL2r9r2VpHqSSgzEa7BeKcWU2d0kGlkF8cZvWdntTC29sYmdxoopkNndB5ReJ0r18E8ZrUeCX-Hu4gRqx7CpW0D9OAyUIt1nb7ox9fMT2KUeVKHSWhlyXSsK4ck1ppx_7Vb-oTeZAKFMgoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HICSNvBZXF4IN8GhhgMe4bmzZiHtwLzE1EGGWaKk-79oNUNCcvAdOlrI0cboWzGRltAQrD5Rp2x-cqq4mjAGTUHNJ-Rr58IL4THNVTMjYpkDvheqqJ76G_-pSr8g1DTc244nme3Fa51ahwFv2WuijTsXebWzNMYihofXOeyRki7a7IF-SRFSZlhazjrzPa-nDoGGmM5zQF1MoxJT-fsbX8xxMBJA9UHuXSwdpiXSThB1c32z-h8d-UKLTiQujohp_4GPNvh6XIoARjr5sw0SEyhRV_3DPoONuy5ViFX8nRv2skr-YZQ435C1Jx9j8rFAIw0o8xmru1YXWeG2W211MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=K0PSbYropZqAU20Q9HBK90RXkvfYHfhjQ1xwGV7lKsGFy6xjNxRUAVaoiMtPERDDkRG6p0c74TZ78K2GBaX7W988wZDExxLJi_Klv7O-o_-_5_mEEJ1Pjp_meIjHSs1AozOXEaU6QIaF4hFmfn4Ogkf18bFO11rvVttElaTc2RxxfEQBbad-Dvr-jo1aeu4Cdhjk4AcoKPP1KFB7u_Cva98CwDB6T0pOYc38quTWCwTI65ATgYdW7aOoL-BSmSc5RmA5g9H5HDBtx6hdjtvuuVdkNWG7eaMtsDlQgVSNk9ZNKDkVJkcUs9AY-8zvYxLM3hwX6F6j5Drs6zLShUo1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=K0PSbYropZqAU20Q9HBK90RXkvfYHfhjQ1xwGV7lKsGFy6xjNxRUAVaoiMtPERDDkRG6p0c74TZ78K2GBaX7W988wZDExxLJi_Klv7O-o_-_5_mEEJ1Pjp_meIjHSs1AozOXEaU6QIaF4hFmfn4Ogkf18bFO11rvVttElaTc2RxxfEQBbad-Dvr-jo1aeu4Cdhjk4AcoKPP1KFB7u_Cva98CwDB6T0pOYc38quTWCwTI65ATgYdW7aOoL-BSmSc5RmA5g9H5HDBtx6hdjtvuuVdkNWG7eaMtsDlQgVSNk9ZNKDkVJkcUs9AY-8zvYxLM3hwX6F6j5Drs6zLShUo1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXOmVq4Xhuz9kgxjPhqxHCEs2_OC4vWmAKEPqI3vOeF5f2Wrn2_nYsMgLDsYw7joIDcm0XuB8tVLhDDYNBo_4bjy9xL9RxTefcH3fkjzKWEFLr4e-OZr8GvzXocqOtULAeLdd3wC-NNRQImBz1Pbw3umV60DOqUB0cc06E2VYvZYH-_VcbGw2W9vZlf7mblVcRcWjNj9Djwmb1La9QQl_mZMPBQKt4op9UK4RHGUGZJORGcuxycFWc1r-mPb8ryQ4ExJpcZpgpDO2xLWH7ulWGm4jgcgofvrIeaJQ4F_KCUmDR16kwhEx5MxCY3-oY-KNKtJL7kfmS77tSItvzrzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn5anJi_ae3QqwFbFo5Vk6YOE1F2noxQGWG7nc6RIVBB_OjLLybN21qZsEx7H7xity2T-m8eIRKhEdu6HDYmNNNdDx1vJoG6y92cylK2y-F_UMBxStjwDjsPPSs4tF_nyq0RRAJNVTSkR2kk2FPYqgWNssVcL-3NxoyxGVQIQBM7aHycz77DTmasUxU5eTpOtfugXah04d6VK8HmnNrT3n2XMi4qthM3Gg0y_F8FIlCShNewAsLJb93vMEUvgIh9Xp-VqlKG0PBN_C9-kIiC4B0iOZolGC5juBmUbOebQIhGC5oxyFHUlfN63DtVuakq64MeTvd5MX4Y_91wbKtyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnEqRS3SWdzHdbrzdtzzwKeMv1nNcxKCNhEBrQ4CnB46Fski3R1P84Txvb50HB7id7MpeeezcgS-bI-rAlJ7a7XQu3sVaZW3Mu11tbBx963YVLi61LPdQp0cxdgWCWSBYmBwE4TzhKsEY8X0mpFsSmyYna4Mf2S4ztf3_FmQ-K_4-w1or54mLVth2oatk_H21SEm1tueC8hgzvYKRnmB8Ly34lFelKFma2MRp4UZUJqPzjpzhvotO39FTluadLEzfD3NCzMKZy72WqaOp6fgemab9PSqoojfpY67sruUNvlEx60U1GE1YE3cQPyAEqbcKeWfwnvGRL8AppmD6nyzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sreBiRt6le7RYPZQHtdZrSQSlMHl3NjyXFsuoKogfqsoKbHo6jMYs7uwgfNIMTsr4G1RVcZqGceGprNTCegLuWiaNE-ETl5U5oBiCcdtLQkbAxAECFR2QT09jayn-XSTg1h0cN2cQe7WZLN1iR3gP7F-w-vuuvDT8lt4VcL7VA9jLegBuSTjEkTy9cWb-5udfpsE8tOReIKx7mPCWuTDiJvbZCFUVkJPjA_ZV2TKKFRIUeOBvZdLkrKqEuEuqQ-2Knw7rPC5I0xnsCx-PuvabXNRiHLgZSPO7CwNSKB8ei5q4SDaXTkIeRqPsoubhOyt-EQ_hZiBq8ARPSKbgnva2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3ORLlbqdEyVTH7nPw-IwdteOZIDM2LndVRYRDech40AVBFfuixFMh0fcKGeAcxIXHa6UR97f5HTNZLvq7X3dYHhP5sns8VvkYrHKULiWFo_nnILud5I3ZcNp9pjJIdv7SKIrStqMuP4BMQje1Wq0yFTDVxuNXeKB9d_Uh6yHTd08FNkRa-0tY2uwvE6thlPLeibF1sWJjZVHxCiaSMkjYoMv1JSL0nPTBNv1uexassZQaQoDTzOUUTEJwmUL4ov9LrNM5PeghfcNR5pAmjithO5ul9I9ybQAHYJEgJ9YP1112ZecA8iiYqw1omDAGLoQJ6pyyQQ6wq02jfpE2KaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBVyOIxEPXXVKcBc6d7GMIi4w0BFp-X5BOjf0b6En2JDqAURGQ2vVsrQ1P_v91qhxPoYXzuLFP4MSe7Oi-fLN5WYtDnnaFOKT7PtQEnk9L8L0POuZonzpmFn_i5mfdT69l6K06tdbNtVmTZEOguat6Eh_XsioRnz0HQNXnURJ6QJZCjNiDEYVL3rP2XmRO8N1Imv7HPXy5cRRLqF1cxHFdRXuYJdGF6fuQNwNb9upSbyaazwOTLWk-154ymTeQCj8UtWLBjCQ8d6XNUholdoeH97RCRRCwl4yOOhIhqU_Ex11DRIZ8iE7woUbXm5-_ThqB1hwhz0nBZxxUWJW2mpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeBp5YV1Q40ZlxifQw-S3ROZC9nyRufIoE4WUaqPVZPPi2pJqAxDGf5TLAPvCzLsLvhG7C3zWHPNonp87Gnz4aDaPig8IKCz2lXo2Lm9INDUlwuyJiNKKW-5ZAXjnKTo3-ljZOoYcYFLd1i3AGPbtjXWRQCDqnkm_-jy0_8HDCeSzaqxD3eWTo9QHK88YJDwizrqfnZX8aMFBh6XHJk2cUWqKmE2pXHOipusnCeTIu-xcuICmZIFduQ4ZtLFemvhf4126mYufE9-BYSgshNjpBtII4EDXZ7kxtvsYqsDYYi2TZ7FradxbCEZb01REbkvTyen5lSkKwBN1AkRUNIvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdzgbqY5T-HRwfeazsXLmcST0x6gEZZtvz5WXdiYh0Gr3CU0iMmbDwnnScYiaQvUrhxPD6oNZS9Yw76Nr_y3JYEq8AKG7u32fy9CRxRNQqSNWi0w2M23Wx3Ht9cWBAVylbyTk4LzhLnpJi1MZs4JL1qsJFk_SYrRpLptBIxtcPxCOBt6jdDMQk_FzV-deEE6MavbEvOCtQlouxNKKLgeTfRo7CahuvKGdZup6UfMUC8YoAkFJ37yNhKVzgoGNK7LOrGowjmtfA4QtfUdqhyfVkBNoaTJk3EQ2I31h0gCjrIK1Ss3pAxK8LQPBC9HtR82dqdXi86I73TtmAyauJEgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_P0IIIoMWwLnmWU1fTLKToWIuzrP8TBdpHSvwVI8In1TbkFuOMpspPvne-IRWWHFtkbP-rjYhH0sLRxXMhmZHFCPMG84AUjxjRdbMzndcp78CMKJIlyzB0pX6uN78Wrg13hcalMQQDxM0O6_0B4T8FNWMWt3-TRwmjd-KatzdQTyYKP4ErmkUAprcE4gGDkCLMEvto5v-R5jcH5rru2sS-nDjY-CTYck20o2Cmpnw6hvkUHKQHk6_3kfCjuhzcAAeQVeQwLGzadRs1maLlb-HCkkKkBuQq6CFpkyehk3GnmuCqTsdBdbRExCbsqtRZRnYEmmi_iZwfbdexHgDSqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
